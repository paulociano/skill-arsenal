#!/usr/bin/env node
// Zero dependencies; Node.js 18+. No network, GPU, or API credits.
import {mkdirSync, writeFileSync} from "node:fs";
import {resolve,join} from "node:path";
function buildKit(seed=42){
  if(!Number.isSafeInteger(seed)||seed<0||seed>4294967295)throw Error("seed must be a uint32");
  const width=4,depth=3,n=8;
  function noise(i,s){let x=(Math.imul(i+1,374761393)^Math.imul(seed+1,668265263)^Math.imul(s+1,1274126177))>>>0;x=Math.imul(x^(x>>>13),1274126177)>>>0;return ((x^(x>>>16))>>>0)/4294967295;}
  function ring(i){
    const edge=i%n===0;
    const f=edge?0:(noise(i,1)-.5)*.35,b=edge?0:(noise(i,2)-.5)*.23,d=edge?0:(noise(i,3)-.5)*.28;
    return [[-0.0,-1.5+b],[0,1.5+f],[-.38,1.63+f],[-1.35+d,1.02+f],[-1.35+d,-1.02+b],[-.38,-1.63+b]];
  }
  function tile(t){
    const rings=Array.from({length:n+1},(_,j)=>ring(t*n+j).map(([y,z])=>[j*width/n,y,z]));
    const positions=[],normals=[],colors=[];
    const palette=[[.22,.34,.33],[.15,.22,.24],[.10,.16,.20],[.08,.11,.15],[.12,.17,.20],[.19,.26,.27]];
    function tri(a,b,c,face,variation){
      const u=b.map((v,j)=>v-a[j]),v=c.map((w,j)=>w-a[j]);
      let norm=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];
      const center=[(a[0]+b[0]+c[0])/3,(a[1]+b[1]+c[1])/3+.65,(a[2]+b[2]+c[2])/3];
      const out=face===6?[-1,0,0]:face===7?[1,0,0]:[0,center[1],center[2]];
      if(norm.reduce((s,x,j)=>s+x*out[j],0)<0){[b,c]=[c,b];norm=norm.map(x=>-x);}
      const len=Math.hypot(...norm);if(len<1e-9)throw Error("degenerate face");
      const rgb=(palette[face]||palette[3]).map(x=>x*(.92+.16*variation));
      for(const p of [a,b,c]){positions.push(...p);normals.push(...norm.map(x=>x/len));colors.push(...rgb)}
    }
    for(let j=0;j<n;j++)for(let k=0;k<6;k++){let q=(k+1)%6;const a=rings[j][k],b=rings[j+1][k],c=rings[j+1][q],d=rings[j][q];const v=noise(t*n+j,k+5);tri(a,b,c,k,v);tri(a,c,d,k,v);}
    for(let k=1;k<5;k++){tri(rings[0][0],rings[0][k],rings[0][k+1],6,.5);tri(rings[n][0],rings[n][k],rings[n][k+1],7,.5);}
    return {positions,normals,colors,left:rings[0].map(p=>p.slice(1)),right:rings[n].map(p=>p.slice(1))};
  }
  function glb(mesh){
    const arrays=[mesh.positions,mesh.normals,mesh.colors],count=mesh.positions.length/3,bytes=count*12;
    const min=[0,1,2].map(j=>mesh.positions.filter((_,i)=>i%3===j).reduce((a,b)=>Math.min(a,b),Infinity));
    const max=[0,1,2].map(j=>mesh.positions.filter((_,i)=>i%3===j).reduce((a,b)=>Math.max(a,b),-Infinity));
    const doc={asset:{version:"2.0",generator:"arsenal-modular-terrain-v1"},scene:0,scenes:[{nodes:[0]}],nodes:[{mesh:0}],meshes:[{primitives:[{attributes:{POSITION:0,NORMAL:1,COLOR_0:2},material:0,mode:4}]}],materials:[{name:"Stone",pbrMetallicRoughness:{baseColorFactor:[1,1,1,1],metallicFactor:0,roughnessFactor:.88}}],buffers:[{byteLength:bytes*3}],bufferViews:arrays.map((_,i)=>({buffer:0,byteOffset:i*bytes,byteLength:bytes,target:34962})),accessors:arrays.map((_,i)=>({bufferView:i,componentType:5126,count,type:"VEC3",...(i===0?{min,max}:{})}))};
    const raw=JSON.stringify(doc),jsonLen=Math.ceil(raw.length/4)*4,total=12+8+jsonLen+8+bytes*3;
    const buffer=new Uint8Array(total),view=new DataView(buffer.buffer);
    const u=(off,x)=>view.setUint32(off,x,true);
    u(0,0x46546c67);u(4,2);u(8,total);u(12,jsonLen);u(16,0x4e4f534a);
    buffer.fill(32,20,20+jsonLen);for(let i=0;i<raw.length;i++)buffer[20+i]=raw.charCodeAt(i);
    const bin=20+jsonLen;u(bin,bytes*3);u(bin+4,0x004e4942);
    arrays.forEach((arr,j)=>arr.forEach((x,i)=>view.setFloat32(bin+8+j*bytes+i*4,x,true)));
    return buffer;
  }
  const tiles=[tile(0),tile(1)];
  const manifest={schemaVersion:1,kit:"modular-stone-terrain",seed,units:"meters",upAxis:"Y",forwardAxis:"Z",generator:"arsenal-modular-terrain-v1",status:"prototype",assets:tiles.map((m,i)=>({id:"terrain-"+(i+1),file:"terrain-"+(i+1)+".glb",placement:[i*width,0,0],nominalWidth:width,nominalDepth:depth,triangles:m.positions.length/9,anchors:{left:{position:[0,0,0],profile:m.left},right:{position:[width,0,0],profile:m.right}},colliders:[{type:"box",center:[width/2,-.3,0],size:[width,.6,2.6]}]}))};
  return {tiles,files:tiles.map(glb),manifest};
}
function selfTest(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 for(const seed of [0,42,2026,4294967295]){
  const a=buildKit(seed),b=buildKit(seed);
  assert(JSON.stringify(a.tiles[0].right)===JSON.stringify(a.tiles[1].left),"seam");
  for(let i=0;i<2;i++){
   const f=a.files[i],v=new DataView(f.buffer);
   assert(v.getUint32(0,true)===0x46546c67&&v.getUint32(4,true)===2&&v.getUint32(8,true)===f.length,"GLB header");
   const l=v.getUint32(12,true),doc=JSON.parse(String.fromCharCode(...f.slice(20,20+l)));
   assert(doc.accessors[0].count===a.tiles[i].positions.length/3,"vertex count");
   assert(doc.buffers[0].byteLength===v.getUint32(20+l,true),"bin length");
   assert(28+l+doc.buffers[0].byteLength===f.length,"chunk bounds");
   assert(a.tiles[i].positions.every(Number.isFinite)&&a.tiles[i].normals.every(Number.isFinite),"finite");
   assert(a.tiles[i].normals.every((x,j,arr)=>j%3!==0||Math.abs(Math.hypot(x,arr[j+1],arr[j+2])-1)<1e-6),"unit normals");
   const edges=new Map(),pos=a.tiles[i].positions;
   for(let j=0;j<pos.length;j+=9){const p=[0,3,6].map(k=>pos.slice(j+k,j+k+3).join(","));for(let k=0;k<3;k++){const key=[p[k],p[(k+1)%3]].sort().join("|");edges.set(key,(edges.get(key)||0)+1)}}
   assert([...edges.values()].every(n=>n===2),"closed geometric edges");
   assert(f.every((x,j)=>x===b.files[i][j]),"deterministic");
  }
 }
 assert(buildKit(1).files[0].some((x,j)=>x!==buildKit(2).files[0][j]),"seed variation");
 return "PASS: 4 seeds, 8 GLBs, seam equality, header/chunks, normals, closed edges, determinism, seed variation";
}
const args=process.argv.slice(2);
if(args.length===1&&args[0]==="--test"){console.log(selfTest());}
else {
  if(args.length<1||args.length>2)throw Error("Usage: node generate-terrain.mjs OUTPUT_DIRECTORY [SEED] | --test");
  const out=resolve(args[0]),seed=args[1]===undefined?42:Number(args[1]);
  const kit=buildKit(seed);
  mkdirSync(out,{recursive:false}); // fresh directory only; never overwrite assets
  kit.files.forEach((f,i)=>writeFileSync(join(out,kit.manifest.assets[i].file),f,{flag:"wx"}));
  writeFileSync(join(out,"manifest.json"),JSON.stringify(kit.manifest,null,2)+"\n",{flag:"wx"});
  console.log("Generated prototype kit:",out);
}
