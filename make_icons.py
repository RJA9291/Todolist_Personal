#!/usr/bin/env python3
"""Generate TaskField PWA icons (PNG): indigo gradient + white checkmark.
Pure Python — no Pillow. Produces icon-180/192/512.png. Pair with icon.svg."""
import zlib, struct, math, os

OUT = "."
TOP = (99, 91, 255)     # indigo #635BFF
BOT = (49, 46, 129)     # indigo #312E81
MARK = (255, 255, 255)

# checkmark polyline in unit coords (0..1), scaled to icon size
PTS = [(0.27, 0.52), (0.44, 0.69), (0.75, 0.33)]

def dist_seg(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    cx, cy = ax + t * dx, ay + t * dy
    return math.hypot(px - cx, py - cy)

def make_icon(size, path):
    W = H = size
    ss = 3
    half = size * 0.058   # half stroke width -> ~0.116*size stroke
    segs = [(PTS[i][0]*size, PTS[i][1]*size, PTS[i+1][0]*size, PTS[i+1][1]*size) for i in range(len(PTS)-1)]

    raw = bytearray()
    for y in range(H):
        raw.append(0)
        t = y / (H - 1)
        bg = (int(TOP[0]+(BOT[0]-TOP[0])*t), int(TOP[1]+(BOT[1]-TOP[1])*t), int(TOP[2]+(BOT[2]-TOP[2])*t))
        for x in range(W):
            hits = 0
            for sy in range(ss):
                for sx in range(ss):
                    fx, fy = x + (sx+0.5)/ss, y + (sy+0.5)/ss
                    d = min(dist_seg(fx, fy, *s) for s in segs)
                    if d <= half:
                        hits += 1
            a = hits / (ss*ss)
            if a <= 0:
                raw += bytes((bg[0], bg[1], bg[2], 255))
            else:
                raw += bytes((int(bg[0]+(MARK[0]-bg[0])*a), int(bg[1]+(MARK[1]-bg[1])*a), int(bg[2]+(MARK[2]-bg[2])*a), 255))

    def chunk(typ, data):
        return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff)
    png = (b'\x89PNG\r\n\x1a\n'
           + chunk(b'IHDR', struct.pack(">IIBBBBB", W, H, 8, 6, 0, 0, 0))
           + chunk(b'IDAT', zlib.compress(bytes(raw), 9))
           + chunk(b'IEND', b''))
    with open(os.path.join(OUT, path), 'wb') as f:
        f.write(png)
    print(path, len(png), "bytes")

for s, p in [(180, 'icon-180.png'), (192, 'icon-192.png'), (512, 'icon-512.png')]:
    make_icon(s, p)
print("done")
