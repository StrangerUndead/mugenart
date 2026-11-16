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
............KK..
..........KKhgK.
........KKhKssdK
......KKhhsKssdK
....KKhhssssKsdK
..KKhKssssdddKK.
KKhhsKsssddKK...
KhhssKsddKK.....
KhsssdKKK.......
.KsddKK.........
.KKKK...........
""")

PARTS['shaft_upper'] = grid("""
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

PARTS['shaft_lower'] = grid("""
KhsK......
KhsK......
.KhsK.....
.KhsK.....
..KhsK....
..KhsK....
...KhsK...
...KhsK...
....KhsK..
....KhsK..
.....KhsK.
.....KhsK.
....KKhsKK
....KgssdK
.....KKKK.
""")

PARTS['far_arm'] = grid("""
KKKKKK...........
KddddK.....KKKK..
KdsddK....KsshsK.
KdsdddK..KsssssdK
.KdsddK..KssssddK
.KddddK.KKsKsKddK
.KdsdddKsdKdKdKK.
..KdddKssddKKK...
..KddKsssddK.....
..KKKssdddK......
..KsssdddKK......
..KKdddKKK.......
....KKKK.........
""")

PARTS['far_thigh'] = grid("""
.KKKKKKKKK...
.KdssssddK...
.KdsssdddK...
.KddsddddK...
..KdsssdddK..
..KddsddddK..
..KKKKddddK..
..KdssKKKdK..
...KdsssdKKK.
...KddssdddK.
...KdddsdddK.
...KdddddddK.
....KdddddddK
....KdddddddK
....KdddddddK
....KKdddddKK
""")

PARTS['far_shin'] = grid("""
..KKKKKKK.......
.KssshsddK......
.KsssddddKK.....
.KsddddddKgK....
.KdddddddKKK....
..KKKKKdddK.....
..KssdKdddK.....
..KdssdddK......
..KdsddddK......
..KddddddK......
..KddddddK......
..KddddddK......
..KKKKdddK......
..KsshKdddK.....
..KsssdddddKK...
..KsdddddddssKK.
..KddddddddddddK
..KKKKKKKKKKKKKK
""")

PARTS['gorget'] = grid("""
.KKKKKK.
KsshsddK
KssssddK
KKsdddKK
""")

PARTS['chest'] = grid("""
.......KKKKKKKK....
...KKKKssssddddKKK.
.KKshsKKsssdddKKsdK
KsshhssKKssddKKssdK
KshhssssKKKKKKsssdK
KsshsssssdKssssdddK
KRRssssssdKssssdddK
KKKRRssssdKsssddRRK
KsdKKRRssdKssdRRKKK
KssddKKRRdKsRRKKddK
KsssdddKKRRRKKdsddK
.KssssddKKKKKdssdK.
.KRRsssssdKsssdRRK.
..KKRRsssdKssRRKK..
..KsKKRRsdKRRKKdK..
...KsdKKRRRKKddK...
...KssdddKKdddK....
""")

PARTS['abdomen'] = grid("""
.KsshssddddddK.
.KKKKKKKKKKKKK.
.KshsssddddddK.
KKKKKKKKKKKKKKK
KshhsssssdddddK
KKKKKKKKKKKKKKK
""")

PARTS['near_thigh'] = grid("""
....KKKKKKKKK
....KshhsdddK
....KsshsdddK
...KsshssdddK
...KsshsdddK.
...KssssdddK.
...KsssddddK.
..KKKKsddddK.
..KshhKKKdK..
..KsshssKKK..
..KssssdddK..
.KsssssdddK..
.KssssdddK...
.KsssddddK...
.KssdddddK...
.KKdddddKK...
""")

PARTS['near_shin'] = grid("""
.........KKKKKKK.
........KsshhsdK.
...K....KssssddKK
..KgK..KsssssdddK
..KhsKKKssssddddK
...KKsdKKsdddddK.
.....KKKKKKKdddK.
........KshsKddK.
........KsshsddK.
........KssssddK.
........KsssdddK.
.......KssssddK..
.......KsssdddK..
.......KKKKsddK..
......KsshsKddK..
....KKsssssdddK..
..KKshssssddddK..
.KsssssdddddddK..
.KKKKKKKKKKKKKK..
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
...KKdsdKKKKlmK
..KdsdKKKKllllK
..KsdKKKlllllmK
.KKdKKKlKKKKlKK
KKKKKKlRRWKlRWK
KllKKlmRRRRmRRK
.KlmKKlmRRmmuRK
..KKKKlmmmmumuK
.....KlmmmmmuK.
.....KmmuuuuuK.
......KmmmmmuK.
......KKmmuuK..
........KKKK...
""")

PARTS['near_arm'] = grid("""
.......KKKKKKK
.......KsshsdK
......KsshsddK
......KsssdddK
.....KsshsddK.
.....KsssdddK.
....KsshsddK..
....KsssdddK..
...KsshsdddK..
...KsssddddK..
..KKsssdddKK..
..KKKKKKKKK...
""")

PARTS['near_forearm'] = grid("""
...KKKKKK....
.KKKshhsdK...
KgsKsssddK...
.KKKssdddK...
...KKKKdddK..
....KshKddK..
....KsshsdK..
.....KsssddK.
.....KsshsdK.
......KsssddK
......KssdddK
......KKKKddK
......KshsKdK
.....KsssdddK
.....KsKsKdKK
.....KhKsKdK.
......K.K.K..
""")

PARTS['near_cap'] = grid("""
.....KKKKKKK....
...KKsshhsssKK..
..KsshhsssssddK.
.KsshssssssdddK.
KsshsssssssddddK
KssssssssdddddKK
KKssssddddddKKK.
.KKKKKKKKKKKK...
.KRRRRRRRRrK....
.KKsssdddKK.....
...KKKKKK.......
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
.....KhhsssdK
""")

PARTS['near_blade_low'] = grid("""
K..........
KKK........
.KgKK......
.KhhsKK....
..KhsssKK..
..KKhssssK.
....KKssssd
......KKsss
........KKs
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
..KhsssK
""")

PARTS['far_cap'] = grid("""
...KKKKKK....
.KKssssddKK..
KsssdddddddK.
KssddddddddK.
KsdddddddddKK
KKddddddddKK.
.KKKKKKKKKK..
..KRRRRrrK...
..KKKKKKK....
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
.KsdddddK...
""")

PARTS['far_blade_low'] = grid("""
........K
......KKK
....KKgK.
..KKshK..
.KsssdK..
sssddKK..
sddKK....
dKK......
""")

# ------------------------------------------------------------------- pose --
# Back-to-front draw order: (part, x, y) of the part's top-left pixel.
IDLE = [
    ('shaft_upper', 65, 38),
    ('shaft_lower', 86, 80),
    ('hammer_head', 57, 30),
    ('far_arm', 88, 67),
    ('far_thigh', 80, 86),
    ('far_shin', 83, 101),
    ('chest', 72, 64),
    ('abdomen', 74, 81),
    ('near_thigh', 69, 86),
    ('near_shin', 61, 101),
    ('tasset', 76, 86),
    ('gorget', 79, 61),
    ('far_cap', 87, 59),
    ('far_blade_low', 96, 57),
    ('far_blade_main', 90, 46),
    ('head', 76, 46),
    ('near_arm', 59, 68),
    ('near_forearm', 58, 77),
    ('near_cap', 60, 59),
    ('near_blade_inner', 66, 49),
    ('near_blade_low', 52, 57),
    ('near_blade_main', 56, 44),
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
