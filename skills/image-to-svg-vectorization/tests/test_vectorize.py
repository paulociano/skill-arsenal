from pathlib import Path
import sys
import pytest
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from vectorize import load_and_mask, trace, validate_svg

def test_icon_with_hole(tmp_path):
    source = tmp_path / "logo.png"
    image = Image.new("RGBA", (128,128), (0,0,0,0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((10,10,117,117), fill="black")
    draw.ellipse((40,40,87,87), fill=(0,0,0,0))
    image.save(source)
    dest = tmp_path / "logo.svg"
    assert trace(source, dest, "opencv") == "opencv-contour-fallback"
    assert validate_svg(dest) == 1
    assert 'fill-rule="evenodd"' in dest.read_text()
    assert "<image" not in dest.read_text()

def test_empty_rejected(tmp_path):
    source = tmp_path / "empty.png"
    Image.new("RGBA", (16,16), (0,0,0,0)).save(source)
    with pytest.raises(ValueError):
        trace(source, tmp_path / "out.svg", "opencv")

def test_color_background_threshold(tmp_path):
    source = tmp_path / "opaque.png"
    image = Image.new("RGB", (40,40), "white")
    ImageDraw.Draw(image).rectangle((10,10,30,30), fill="black")
    image.save(source)
    mask, size = load_and_mask(source, 128)
    assert size == (40,40) and mask[20,20] == 255 and mask[0,0] == 0

def test_reject_embedded_raster(tmp_path):
    svg = tmp_path / "bad.svg"
    svg.write_text('<svg xmlns="http://www.w3.org/2000/svg"><path d="M0 0L1 1"/><image href="data:image/png;base64,AAAA"/></svg>')
    with pytest.raises(ValueError):
        validate_svg(svg)
