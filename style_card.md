# Style card: JUS sprites (measured)

All values measured in code from sprite sheets at 1x. The sheets are not stored in this repo.

Primary references (fan-made JUS sheets of heavy, dark or armoured characters, the kind of sprite the
Jump Force Mugen roster is built from):
- Darth Vader by Rimihf: https://www.deviantart.com/rimihf/art/Darth-Vader-JUS-sprite-sheet-1071825365
- Jason Voorhees by TheHunterDrake: https://www.deviantart.com/thehunterdrake/art/Jason-Voorhees-JUS-Sprite-Sheet-738355476
- Simon Belmont by SmashBracket: https://www.deviantart.com/smashbracket/art/Simon-Belmont-JUS-Sprite-Sheet-898033538
- MG Raiden by TheHunterDrake (crouched idle, used for colour only): https://www.deviantart.com/thehunterdrake/art/MG-Raiden-JUS-Sprite-Sheet-741945067
- Guts by DryMugen (single sprite, about 72 px tall, used for armour tones only): https://www.deviantart.com/drymugen/art/BERSERK-JUS-Sprites-920706978

Baseline (original Jump Ultimate Stars rips): Jotaro and Dio, https://jojowiki.com/Category:Images_of_Jump_Stars_Games

| Item | Vader | Jason | Simon | Original JUS (Jotaro, Dio) |
|---|---|---|---|---|
| Standing height | 61 | 61 | 62 (with hair) | 56-57, 61-63 |
| Head height | 12 (helmet) | 12 (bare) | 16 (with hair) | 15, 18 (with hair) |
| Head width | 13 (helmet flare 18) | 13 | 17 with hair, face 7 | 15-17 with hair |
| Heads tall | 5.1 | 5.1 | 3.9 | 3.4-3.7 |
| Shoulder width, both arms | 21-25 | 18-23 | 22-24 | 20-22 |
| Waist | hidden by cape | 13 | 12 | 13-14 |
| Arm thickness | 7-9 | 6 | 6-7 | 6-7 |
| Fist | glove 5 | 6 wide, 6 tall | 7-8 wide, 5-6 tall | 4-5 |
| Thigh / calf | 5-6 (straight) | 8 / 7 | 7 / 6 | 10-11 / 6-8 |
| Foot | 7-10 long, 3-4 tall | 8-10 long, 4-5 tall | 7-9 long, 2-3 tall | 9-11 long, 4-5 tall |
| Stance width, feet | 22 | 28 | 21 | 24-34 |
| Colours in idle frame | 28 raw, about 12 real | 23 | 22 | exactly 15 |
| Outline | #080808 + #000000, 77% (rest is the sabre) | #080808 + #000000, 98% | #140C0C, 94% | #080808, 94-99% |
| Near-black share | 83% | 75% | 23% | 40-58% |

Shared findings:
- Outline is 1 px near-black on every reference. Simon uses a warm near-black (#140C0C); nobody uses a darkened local colour.
- Bruisers have small heads: a bare head is 12-13 px on a 61 px body (about 5 heads tall). Only big hair brings the ratio down to 3.5-4.
- Light comes from the upper left of the screen on every reference. Highlight sits just inside the left or top outline.
- Flat clusters, no dithering, no gradients, no semi-transparent pixels.
- Three-quarter view, both shoulders and both legs visible, legs apart with a 3-9 px gap, back foot 1 px higher.
- Inner lines are near-black, 1 px: arm against torso, between legs, under the chin, belt, plate edges.
- Eye: 1 light pixel with 1-2 dark pupil pixels beside it and a dark brow line above. No nose. Mouth is 1-2 pixels of dark skin tone. Skin uses 3-4 tones.
- Simon has red face paint: 2 pixels of #B01E21 beside the eye. That is the scale face paint survives at.
- Canvas: sheets are trimmed, no fixed cell. localcoord and scale cannot be measured from sprites.

How black armour is drawn (the key finding for this character):

| Reference | Outline | Shadow | Base | Highlight | Notes |
|---|---|---|---|---|---|
| Vader | #080808 | #0B0B0B | #171717 | #222222 | almost a silhouette; detail carried by chest lights and the red sabre |
| Jason (trousers) | #080808 | #0D0D0D | #141414 | #484848 | highlight in short strips on the lit edge |
| Raiden | #080808 | #202020 | #272727 | #3F3F3F | plus light metal accents #808080 and #C1BFBA |
| Guts | #0C0404 | #1F1320 | #322940 | #5B5D74 | cool violet tint; highlight is about 7% of armour pixels |

Black armour is a near-black base with a small, cool highlight. Mid-grey steel would not match the roster.

## Targets for this character

Guts was chosen as the closest reference, so the master sprite follows its scale and its armour rendering.

- 72 px to the top of the hair (Guts: 72), horn tips at 74 px, pauldron blades to 76 px, hammer head to 90 px
- Head 14 px tall and 13 px wide, face 9 px wide
- Chest 19 px, waist 13 px, thighs 9 px, shins 8 px, boots 13-14 px long
- Feet 37 px apart, back foot 1 px higher
- Armour tone shares: black 42%, shadow 26%, base 26%, highlight 7% (Guts: 51 / 25 / 17 / 7)
- Fixed canvas 160x128, foot row y = 119, axis x = 80 at the centre of the feet
- 15 colours + transparent

## Draft palette

| Index | Hex | Use |
|---|---|---|
| 0 | #FF00FF | transparent |
| 1 | #080808 | outline, deepest shadow, hair |
| 2 | #181821 | steel shadow |
| 3 | #313142 | steel base |
| 4 | #5A5A73 | steel highlight, used sparingly on lit edges |
| 5 | #9494A5 | steel glint, a few pixels on spike tips and the hammer head |
| 6 | #6B1010 | ember dark |
| 7 | #D62118 | ember, war paint |
| 8 | #FF6B39 | ember hot core (seam flare, shockwave) |
| 9 | #4A4242 | skin shadow |
| 10 | #7B7373 | skin base |
| 11 | #ADA5A5 | skin light |
| 12 | #8C8473 | horn shadow |
| 13 | #D6CEB5 | horn |
| 14 | #FFFFFF | eye white |
| 15 | spare | |
