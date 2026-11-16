"""Render the master sprite: stage sheet and comparison with a reference.

usage: python3 render_master.py [reference.png ...]
Reference images are pasted as they are (1x pixel art on any background).
"""
import sys
from PIL import Image
import master_sprite as ms

GREY = (128, 128, 128)
PAD = 3


def rgb_on_grey(canvas, box):
    x0, y0, x1, y1 = box
    im = Image.new('RGB', (x1 - x0 + 1, y1 - y0 + 1), GREY)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            v = canvas[y][x]
            if v:
                im.putpixel((x - x0, y - y0), ms.rgb(ms.HEX[v]))
    return im


def up(im, k):
    return im.resize((im.width * k, im.height * k), Image.NEAREST)


def hstack(ims, gap=16):
    w = sum(i.width for i in ims) + gap * (len(ims) + 1)
    h = max(i.height for i in ims) + 2 * gap
    out = Image.new('RGB', (w, h), GREY)
    x = gap
    for i in ims:
        out.paste(i, (x, h - gap - i.height))
        x += i.width + gap
    return out


def main():
    final = ms.compose()
    x0, y0, x1, y1 = ms.bbox(final)
    box = (x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD)
    stages = [ms.compose(part_filter=f) for f in (ms.stage_silhouette, ms.stage_flat, ms.stage_shaded)] + [final]
    hstack([up(rgb_on_grey(s, box), 4) for s in stages]).save('out/master_stages_4x.png')
    refs = [Image.open(p).convert('RGB') for p in sys.argv[1:]]
    mine = rgb_on_grey(final, box)
    hstack([up(mine, 8)] + [up(r, 8) for r in refs]).save('out/master_compare_8x.png')
    hstack([mine] + refs, gap=4).save('out/master_compare_1x.png')
    ms.to_image(final).save('out/master_idle.png')
    # report
    im = Image.open('out/master_idle.png')
    assert im.mode == 'P'
    rgba = im.convert('RGBA')
    used = sorted({v for row in final for v in row if v})
    allowed = {ms.rgb(h) for h in ms.HEX.values()}
    off = sum(1 for p in im.convert('RGB').getdata() if p not in allowed)
    print('sprite size %d x %d, feet row %d' % (x1 - x0 + 1, y1 - y0 + 1, y1))
    print('colours used (excluding transparent): %d' % len(used))
    print('off-palette pixels: %d, semi-transparent pixels: %d' % (off, sum(1 for p in rgba.getdata() if 0 < p[3] < 255)))


if __name__ == '__main__':
    main()
