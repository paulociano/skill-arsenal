#!/usr/bin/env python3
"""Convert monochrome logos/icons to real SVG paths. Engines: Potrace, VTracer, OpenCV fallback."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET

import cv2
import numpy as np
from PIL import Image

NS = "http://www.w3.org/2000/svg"

def validate_svg(path):
    root = ET.parse(path).getroot()
    if root.tag != "{%s}svg" % NS:
        raise ValueError("Not SVG")
    paths = root.findall(".//{%s}path" % NS)
    if not paths or root.findall(".//{%s}image" % NS):
        raise ValueError("SVG lacks paths or contains embedded raster")
    return len(paths)

def load_and_mask(source, threshold):
    rgba = np.array(Image.open(source).convert("RGBA"))
    if rgba.shape[0] * rgba.shape[1] > 20_000_000:
        raise ValueError("Maximum 20 megapixels")
    alpha = rgba[:, :, 3]
    if np.any(alpha < 255):
        mask = (alpha >= threshold).astype("uint8") * 255
    else:
        gray = cv2.cvtColor(rgba[:, :, :3], cv2.COLOR_RGB2GRAY)
        mask = (gray < threshold).astype("uint8") * 255
    return mask, (rgba.shape[1], rgba.shape[0])

def opencv_trace(mask, size, output, color, tolerance):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    paths = []
    for contour in contours:
        if cv2.contourArea(contour) < 1:
            continue
        points = cv2.approxPolyDP(contour, tolerance, True).reshape(-1, 2)
        if len(points) >= 3:
            paths.append("M " + " L ".join(f"{int(x)} {int(y)}" for x, y in points) + " Z")
    if not paths:
        raise ValueError("No valid contours")
    w, h = size
    ET.register_namespace("", NS)
    root = ET.Element("{%s}svg" % NS, {"viewBox": f"0 0 {w} {h}", "width": str(w), "height": str(h)})
    ET.SubElement(root, "{%s}path" % NS, {"d": " ".join(paths), "fill": color, "fill-rule": "evenodd"})
    ET.ElementTree(root).write(output, encoding="unicode", xml_declaration=True)
    return "opencv-contour-fallback"

def trace(source, output, engine="auto", threshold=128, color="#000000", tolerance=0.8):
    mask, size = load_and_mask(source, threshold)
    if not 0 < np.count_nonzero(mask) < mask.size:
        raise ValueError("Empty/full foreground; adjust threshold")
    with tempfile.TemporaryDirectory() as tmp:
        pbm, png = Path(tmp) / "mask.pbm", Path(tmp) / "mask.png"
        Image.fromarray(mask).convert("1").save(pbm)
        Image.fromarray(mask).save(png)
        if engine in ("auto", "potrace") and shutil.which("potrace"):
            result = subprocess.run(["potrace", str(pbm), "-s", "-o", str(output)], capture_output=True, text=True, timeout=45)
            if result.returncode:
                raise RuntimeError(result.stderr.strip())
            return "potrace"
        if engine == "potrace":
            raise RuntimeError("potrace unavailable")
        if engine in ("auto", "vtracer") and shutil.which("vtracer"):
            result = subprocess.run(["vtracer", "--input", str(png), "--output", str(output), "--colormode", "binary"], capture_output=True, text=True, timeout=45)
            if result.returncode:
                raise RuntimeError(result.stderr.strip())
            return "vtracer"
        if engine == "vtracer":
            raise RuntimeError("vtracer unavailable")
        return opencv_trace(mask, size, output, color, tolerance)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--engine", choices=["auto", "potrace", "vtracer", "opencv"], default="auto")
    parser.add_argument("--threshold", type=int, default=128)
    parser.add_argument("--color", default="#000000")
    parser.add_argument("--tolerance", type=float, default=0.8)
    args = parser.parse_args()
    if not args.input.is_file() or args.input.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp", ".bmp"):
        parser.error("Input must be a local supported raster image")
    if not 1 <= args.threshold <= 254 or args.tolerance < 0:
        parser.error("Invalid threshold or tolerance")
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", args.color):
        parser.error("Color must be #RRGGBB")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    engine = trace(args.input, args.output, args.engine, args.threshold, args.color, args.tolerance)
    paths = validate_svg(args.output)
    print(json.dumps({"output": str(args.output), "engine": engine, "paths": paths,
        "bytes": args.output.stat().st_size, "note": "fallback uses line segments" if engine.startswith("opencv") else "visually inspect output"}))

if __name__ == "__main__":
    main()
