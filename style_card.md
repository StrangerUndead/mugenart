# Style card: JUS sprites (measured)

Measured in code from two original Jump Ultimate Stars sprite sheets (Jotaro, 198 frames; Dio, 218 frames),
ripped at 1x. Source: https://jojowiki.com/Category:Images_of_Jump_Stars_Games
The sheets themselves are not stored in this repo.

| Item | Measured value |
|---|---|
| Standing height | 56-57 px (Jotaro), 61-63 px (Dio); both are tall characters |
| Head height | 15 px (Jotaro, with cap), 18 px to hair tips / 13 px skull only (Dio) |
| Heads tall | 3.4-3.7 counting hair |
| Head width | 15-17 px including hair; face skin area 6-8 px wide, 8 rows tall |
| Shoulder width | 20-22 px including both arms |
| Hip width | 13-14 px |
| Limb thickness | arm 6-7 px, thigh 10-11 px, calf 6-8 px, ankle 5-6 px (all including outline) |
| Hand | 4-5 px block, 2-3 skin pixels showing |
| Foot | 9-11 px long (up to 15 for the front shoe), 4-5 px tall |
| Body split (Dio) | head 18, chin to belt 12, belt to crotch 12, crotch to floor 19 |
| Colours | exactly 15 + transparent per character, on every full frame |
| Colour values | DS 15-bit: every channel is a multiple of 8, plus 255 |
| Shades per material | 3 for main materials (highlight, base, shadow), 2 for small ones; black is a further deepest shade |
| Outline | 1 px #080808 near-black, 94-99% of edge pixels; not a darkened local colour |
| Black share | 40% (Dio) to 58% (Jotaro) of all opaque pixels |
| Inner lines | black, 1 px: arm against torso, between legs, under chin, belt, cloth folds; black also fills whole shadow areas |
| Light | from the upper left of the screen (behind the back shoulder when facing right); highlight sits 1 px inside the left outline, shadow on the right |
| Shading | flat clusters, no dithering, no gradients |
| View | three-quarter view, torso turned towards the viewer, both shoulders and both legs visible; back foot 1 px higher than front foot |
| Eye | 1 white pixel + 1 pupil pixel beside it (2x1), 1-3 px black brow line directly above |
| Face | no nose; mouth is 2 pixels of the darkest skin tone; skin has 3 tones |
| Canvas | rips are trimmed, no fixed cell; widest frame 156 px, tallest 79 px |
| localcoord, scale | not measurable from sprites; placeholder 320,240 and xscale = yscale = 1 |

## Targets for this character

- 58 px to the top of the head; pauldron spikes to about 63 px, hammer head to about 68 px
- Head 13 px + 2 px horns, shoulders 22 px before pauldrons, hips 14 px
- Fixed canvas 128x96, foot row fixed, axis at the centre of the feet
- 15 colours + transparent, channels snapped to multiples of 8

## Draft palette

| Index | Hex | Use |
|---|---|---|
| 0 | #FF00FF | transparent |
| 1 | #080808 | outline, deep shadow, hair |
| 2 | #293139 | steel shadow |
| 3 | #525A63 | steel base |
| 4 | #9CA5AD | steel highlight |
| 5 | #6B1010 | ember dark |
| 6 | #D62118 | ember, war paint |
| 7 | #FF6B39 | ember hot core (seam flare, shockwave) |
| 8 | #4A4242 | skin shadow |
| 9 | #7B7373 | skin base |
| 10 | #ADA5A5 | skin light |
| 11 | #8C8473 | horn shadow |
| 12 | #D6CEB5 | horn |
| 13 | #FFFFFF | eye white |
| 14-15 | spare | |
