"""Master sprite (idle stance, facing right) for the dark elf bruiser.

Every part is a hand-placed bitmap: rows of palette characters, one character
per pixel. No shape calls, no rotation, no scaling. A part is pasted at an
integer offset; '.' is transparent.
"""
from PIL import Image

# ---------------------------------------------------------------- palette --
# index, character, hex, use
PALETTE = [
    (0, '.', '#FF00FF', 'transparent'),
    (1, 'K', '#080808', 'outline, deepest shadow, hair'),
    (2, 'd', '#181821', 'steel shadow'),
    (3, 's', '#313142', 'steel base'),
    (4, 'h', '#5A5A73', 'steel highlight'),
    (5, 'g', '#9494A5', 'steel glint'),
    (6, 'r', '#6B1010', 'ember dark'),
    (7, 'R', '#D62118', 'ember, war paint'),
    (8, 'O', '#FF6B39', 'ember hot core'),
    (9, 'u', '#4A4242', 'skin shadow'),
    (10, 'm', '#7B7373', 'skin base'),
    (11, 'l', '#ADA5A5', 'skin light'),
    (12, 'n', '#8C8473', 'horn shadow'),
    (13, 'H', '#D6CEB5', 'horn'),
    (14, 'W', '#FFFFFF', 'eye white'),
]
CHAR_TO_INDEX = {c: i for i, c, _, _ in PALETTE}
HEX = {i: h for i, _, h, _ in PALETTE}

CANVAS_W, CANVAS_H = 160, 128
AXIS_X = 80        # centre of the feet
GROUND_Y = 119     # row of the lowest foot pixel


def rgb(hexstr):
    return tuple(int(hexstr[i:i + 2], 16) for i in (1, 3, 5))


def grid(text):
    rows = [r for r in text.strip('\n').split('\n')]
    w = len(rows[0])
    for r in rows:
        assert len(r) == w, 'ragged row: %r (%d != %d)' % (r, len(r), w)
        for c in r:
            assert c in CHAR_TO_INDEX, 'unknown palette char %r' % c
    return rows


# ------------------------------------------------------------------ parts --
PARTS = {}

PARTS['hammer_head'] = grid("""
...........KK..
.........KKhgK.
.......KKhKssK.
.....KKhhsKsssK
...KKhhssssKsdK
.KKhKssssddKKK.
KhhsKssddKK....
KhssKsddKK.....
.KssdKdKK......
.KdddKK........
..KKK..........
""")

PARTS['hammer_shaft'] = grid("""
KhsK........
KhsK........
.KhsK.......
.KhsK.......
..KhsK......
..KhsK......
...KhsK.....
...KhsK.....
....KhsK....
....KhsK....
.....KhsK...
.....KhsK...
......KhsK..
......KhsK..
.......KhsK.
.......KhsK.
........KhsK
........KhsK
""")

PARTS['far_arm'] = grid("""
.KKKKK..........
.KddddK.........
.KddddK.........
.KsdddK.........
..KdddK...KKKK..
..KsddKKKKssssK.
..KKKKssssKsssdK
..KddKsdddKssddK
..KdddKKKKKsdddK
...KKdddddKddddK
.....KKKKKKKKKK.
""")

PARTS['far_blade_main'] = grid("""
..........KK
.........KgK
........KhsK
.......KhsdK
......KhsddK
......KsddK.
.....KssddK.
....KssdddK.
....KssddK..
...KsssddK..
..KsssdddK..
..KssdddK...
.KsssdddK...
.KssddddK...
.KKKKKKK....
""")

PARTS['far_blade_low'] = grid("""
........K
......KKK
....KKgK.
..KKshK..
.KsssdK..
KsssdKK..
KdddKK...
KKKK.....
""")

PARTS['far_dome'] = grid("""
..KKKKKKK...
.KssssdddK..
KsssddddddK.
KsdddddddddK
KRRRRRRrrrKK
KKKKKKKKKKdK
.KssdddddK..
..KKdddKK...
....KKKK....
""")

PARTS['far_thigh'] = grid("""
KKKKKKKKKK..
KdssssdddK..
KdsssddddK..
KddddddddK..
.KdddddddK..
.KddddddddK.
.KddddddddK.
.KKKKddddKK.
.KdsdKKKKdK.
..KsssddddK.
..KdsddddddK
..KddddddddK
..KKdddddddK
...KKKKKKKKK
...KsssddddK
...KdsdddddK
...KKdddKKK.
.....KKKK...
""")

PARTS['far_shin'] = grid("""
KKKKKKKKK.....
KsssddddK.....
KdsdddddKKK...
KdddddddKsgK..
KddddddKKKK...
KKKKKKKKK.....
.KssddddK.....
.KdsddddK.....
.KddddddK.....
.KddddddK.....
.KKKKKKKKK....
.KssdddddK....
.KdsdddddKKK..
.KddddddddssKK
.KdddddddddddK
.KKKKKKKKKKKKK
""")

PARTS['chest'] = grid("""
....KKKKKKKKKKK....
..KKdssssdddddKKK..
.KsshssdKKKdddddKK.
KsshhssssdKdssdddK.
KshhsssssdKdsssddKK
KRRssssssdKdssssRRK
KKKRRssssdKdssRRKKK
KsdKKRRssdKdRRKKddK
KssddKKRRdKRRKdsddK
KsssdddKKRRRKKdsddK
KRRsssddKKKKKdssRRK
.KKRRssssdKdssRRKK.
.KdKKRRssdKdRRKKdK.
.KsddKKRRdKRRKdddK.
..KsddKKKRRRKKddK..
..KKsdddKKKKKdddKK.
""")

PARTS['abdomen'] = grid("""
KsshsssdddddddK
KKKKKKKKKKKKKKK
.KshsssddddddK.
.KKKKKKKKKKKKK.
""")

PARTS['belt'] = grid("""
KKKKKKKKKKKKKKKKK
KshhsssssdddddddK
KKKKKKKKKKKKKKKKK
""")

PARTS['near_thigh'] = grid("""
.....KKKKKKKK
.....KshhsddK
....KsshsdddK
....KssssdddK
....KsssdddK.
...KssssdddK.
...KsssddddK.
...KssddddKK.
..KKKKdddKK..
..KshhKKKdK..
.KsshssdddK..
.KsssdddddK..
.KssdddddK...
KKsddddddK...
KKKKKKKKKK...
KshhssdddK...
KsssssddKK...
.KKsdddKK....
...KKKK......
""")

PARTS['near_shin'] = grid("""
.........KKKKKKKK
......K..KshhsddK
.....KgKKKsssdddK
.....KhsKKsddddK.
......KKKKKddddK.
.........KKKKKKK.
........KshhsddK.
........KsssdddK.
.......KssssdddK.
.......KsssdddK..
.......KKKKKKKK..
......KsshssddK..
....KKKsssddddK..
..KKshssddddddK..
KKsssdddddddddK..
KKKKKKKKKKKKKK...
""")

PARTS['tasset'] = grid("""
KKKKKKKKK
KhhsKdddK
KhssKdddK
KhssKdddK
KhssKdddK
KhssKdddK
KhssKdddK
KhssKdddK
.KhsKddK.
.KhsKddK.
.KhsKddK.
.KhsKddK.
..KhKdK..
..KhKdK..
..KhKdK..
...KKK...
....K....
""")

PARTS['head'] = grid("""
........K..K...
.......KHKKHK..
.....KKKnKKnKK.
...KKKddKKKKKKK
..KKddKKKllllmK
..KdKKKllllmmmK
..KKKKllKKKlKKK
.KKKKKlRWWKlWKK
KllKKlRRRRlRRmK
.KlmKllRRllRmuK
..KKKlllmmumuK.
....KllmmmmmuK.
....KlmuuuumK..
.....KlmmmmuK..
.....KKmmuuK...
.......KKKK....
""")

PARTS['near_arm'] = grid("""
.KKKKKKKK.
.KshhsddK.
.KsssdddK.
.KssddddK.
KKsdddddK.
KsKKKKKKK.
KshhsdddK.
KsssddddK.
KKKKKKKKK.
""")

PARTS['near_forearm'] = grid("""
....KKKKKKK.
.KKKKshhsdK.
KgsKsssdddK.
.KKKsdddddK.
...KKKKKKKK.
...KshhsddK.
...KsssdddK.
..KssssdddK.
..KsssddddK.
..KssdddddK.
..KKKKKKKKK.
..KshhsddK..
.KssssdddK..
.KsKsKsKdK..
.KhKsKsKK...
..K.K.K.....
""")

PARTS['near_dome'] = grid("""
....KKKKKKK....
..KKsshhsssKK..
.KsshhsssssddK.
KsshhsssssdddK.
KshhsssssddddKK
KsssssssdddddKK
KKRRRRRRRRrrKK.
KsKKKKKKKKKKdK.
KsshssssddddK..
.KKssssdddKK...
...KKKKKKK.....
""")

PARTS['near_blade_main'] = grid("""
KK...........
KgK..........
KhhK.........
.KhsK........
.KhssK.......
.KhhssK......
..KhssdK.....
..KhsssdK....
..KhhsssdK...
...KhsssdK...
...KhssssdK..
...KhhsssddK.
....KhsssddK.
....KhssssddK
.....KhsssddK
.....KKhssddK
.......KKKKKK
""")

PARTS['near_blade_low'] = grid("""
K..........
KKK........
.KgKK......
.KhhsKK....
..KhsssKK..
..KKhssssK.
....KKsssdK
......KKddK
........KKK
""")

PARTS['near_blade_inner'] = grid("""
KK......
KgK.....
KhsK....
.KhsK...
.KhssK..
.KhssdK.
..KhsdK.
..KhssdK
..KhssdK
..KKKKKK
""")

# ------------------------------------------------------------------- pose --
# Back-to-front draw order: (part, x, y) of the part's top-left pixel.
IDLE = [
    ('hammer_shaft', 68, 39),
    ('hammer_head', 60, 31),
    ('far_arm', 92, 68),
    ('far_thigh', 83, 85),
    ('far_shin', 87, 103),
    ('chest', 75, 63),
    ('abdomen', 76, 79),
    ('belt', 75, 83),
    ('near_thigh', 69, 85),
    ('near_shin', 60, 104),
    ('tasset', 79, 85),
    ('far_blade_low', 99, 58),
    ('far_blade_main', 94, 47),
    ('far_dome', 90, 60),
    ('head', 80, 46),
    ('near_arm', 67, 68),
    ('near_forearm', 63, 76),
    ('near_blade_inner', 67, 49),
    ('near_blade_low', 54, 56),
    ('near_blade_main', 57, 43),
    ('near_dome', 63, 58),
]


def compose(pose=IDLE, part_filter=None):
    """Return a canvas of palette indices (list of rows)."""
    canvas = [[0] * CANVAS_W for _ in range(CANVAS_H)]
    for name, ox, oy in pose:
        rows = PARTS[name]
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if c == '.':
                    continue
                if part_filter:
                    c = part_filter(name, c)
                canvas[oy + y][ox + x] = CHAR_TO_INDEX[c]
    return canvas


def to_image(canvas):
    """8-bit indexed image using the one palette."""
    im = Image.new('P', (CANVAS_W, CANVAS_H), 0)
    pal = []
    for i in range(256):
        pal += list(rgb(HEX[i])) if i in HEX else [0, 0, 0]
    im.putpalette(pal)
    for y, row in enumerate(canvas):
        for x, v in enumerate(row):
            if v:
                im.putpixel((x, y), v)
    return im


# stage filters -------------------------------------------------------------
FLAT = {'h': 's', 'd': 's', 'g': 's', 'r': 'R', 'O': 'R', 'u': 'm', 'l': 'm', 'n': 'H'}


def stage_silhouette(name, c):
    return 'K'


def stage_flat(name, c):
    if name == 'head' and c in 'RW':
        return 'm'
    return FLAT.get(c, c)


def stage_shaded(name, c):
    if name == 'head' and c in 'RW':
        return 'm'
    return c


def bbox(canvas):
    ys = [y for y, row in enumerate(canvas) if any(row)]
    xs = [x for row in canvas for x, v in enumerate(row) if v]
    return min(xs), min(ys), max(xs), max(ys)


if __name__ == '__main__':
    c = compose()
    x0, y0, x1, y1 = bbox(c)
    used = sorted({v for row in c for v in row if v})
    print('bbox', x0, y0, x1, y1, 'size', x1 - x0 + 1, 'x', y1 - y0 + 1)
    print('colours (excluding transparent):', len(used), used)
    to_image(c).save('out/master_idle.png')
