"""G-GMD: geometric measurement and dimension (sets 75-82)."""
import math

from qb import S, B, sa, mc, tf, work
from common import gd, NTS, proof

PI = math.pi


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


EXP = 'Any valid explanation. '


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def pv(k, unit, den=1):
    """'kπ unit ≈ decimal unit' for a volume or area kπ/den."""
    ex = ('%sπ' % k if den == 1 else '%sπ/%s' % (k, den)) if k != 1 else ('π' if den == 1 else 'π/%s' % den)
    return '%s %s ≈ %s %s' % (ex, unit, d1(k * PI / den), unit)


# ---------------------------------------------------------------- oblique solid sketches (not to scale)
def ell(cx, cy, rx, ry, a0=0, a1=360, dash=False, n=36):
    out = []
    for i in range(n):
        t0 = math.radians(a0 + (a1 - a0) * i / n)
        t1 = math.radians(a0 + (a1 - a0) * (i + 1) / n)
        p = (cx + rx * math.cos(t0), cy + ry * math.sin(t0))
        q = (cx + rx * math.cos(t1), cy + ry * math.sin(t1))
        out.append(('seg', p, q, {'dash': True}) if dash else ('seg', p, q))
    return out


def cylinder(r_lab, h_lab, desc, rx=1.6, h=3.0, h_px=230):
    ry = rx * 0.3
    it = ell(0, 0, rx, ry, 180, 360) + ell(0, 0, rx, ry, 0, 180, dash=True) + ell(0, h, rx, ry)
    it += [('seg', (-rx, 0), (-rx, h)), ('seg', (rx, 0), (rx, h)), ('seg', (0, h), (rx, h), {'dash': True}),
           ('seg', (0, 0), (0, h), {'dash': True}), ('text', (rx / 2, h - 0.22), r_lab), ('text', (0.3, h / 2), h_lab)]
    return gd({}, it, h=h_px, desc=desc, note=NTS)


def cone(r_lab, h_lab, desc, rx=1.6, h=3.0, slant=None, h_px=230):
    ry = rx * 0.3
    it = ell(0, 0, rx, ry, 180, 360) + ell(0, 0, rx, ry, 0, 180, dash=True)
    it += [('seg', (-rx, 0), (0, h)), ('seg', (rx, 0), (0, h)), ('seg', (0, 0), (rx, 0), {'dash': True}), ('seg', (0, 0), (0, h), {'dash': True}),
           ('ra', (0, 0), (0, h), (rx, 0)), ('text', (rx / 2, 0.2), r_lab)]
    if h_lab:
        it.append(('text', (-0.3, h / 2), h_lab))
    if slant:
        it.append(('text', (rx / 2 + 0.45, h / 2 + 0.2), slant))
    return gd({}, it, h=h_px, desc=desc, note=NTS)


def sphere(r_lab, desc, r=1.6, hemi=False, h_px=210):
    ry = r * 0.3
    it = ell(0, 0, r, ry, 180, 360) + ell(0, 0, r, ry, 0, 180, dash=True)
    it += [('arc', (0, 0), r, 0, 180)] if hemi else [('circle', (0, 0), r)]
    it += [('seg', (0, 0), (r, 0)), ('text', (r / 2, 0.18), r_lab)]
    return gd({}, it, h=h_px, desc=desc, note=NTS)


def sq_pyramid(s_lab, h_lab, desc, h_px=230):
    A, Bq, C, D = (0, 0), (2.4, 0), (3.3, 0.8), (0.9, 0.8)
    O = (1.65, 0.4)
    T = (1.65, 3.0)
    it = [('seg', A, Bq), ('seg', Bq, C), ('seg', C, D, {'dash': True}), ('seg', D, A, {'dash': True}),
          ('seg', A, T), ('seg', Bq, T), ('seg', C, T), ('seg', D, T, {'dash': True}), ('seg', O, T, {'dash': True}),
          ('text', (1.2, -0.3), s_lab), ('text', (1.95, 1.7), h_lab)]
    return gd({}, it, h=h_px, desc=desc, note=NTS)


def cube(desc, extra=(), h_px=220, s=2.2, dx=0.9, dy=0.7):
    A, Bq, C, D = (0, 0), (s, 0), (s, s), (0, s)
    A2, B2, C2, D2 = [(p[0] + dx, p[1] + dy) for p in (A, Bq, C, D)]
    it = [('seg', A, Bq), ('seg', Bq, C), ('seg', C, D), ('seg', D, A), ('seg', Bq, B2), ('seg', C, C2), ('seg', D, D2),
          ('seg', B2, C2), ('seg', C2, D2), ('seg', A, A2, {'dash': True}), ('seg', A2, B2, {'dash': True}), ('seg', A2, D2, {'dash': True})]
    return gd({}, it + list(extra), h=h_px, desc=desc)


SECTORS = gd({}, [('sector', (0, 0), 1.4, 0, 45), ('sector', (0, 0), 1.4, 45, 90), ('sector', (0, 0), 1.4, 90, 135), ('sector', (0, 0), 1.4, 135, 180),
                  ('sector', (0, 0), 1.4, 180, 225), ('sector', (0, 0), 1.4, 225, 270), ('sector', (0, 0), 1.4, 270, 315), ('sector', (0, 0), 1.4, 315, 360),
                  ('seg', (2.4, 0), (6.8, 0)), ('seg', (2.4, 1.3), (6.8, 1.3))]
              + [('seg', (2.4 + 1.1 * i, 0), (2.95 + 1.1 * i, 1.3)) for i in range(4)] + [('seg', (2.95 + 1.1 * i, 1.3), (3.5 + 1.1 * i, 0)) for i in range(4)]
              + [('text', (4.6, -0.35), 'about half the circumference'), ('text', (7.1, 0.65), 'r')],
              h=240, desc='Left: a circle of radius r cut into 8 equal sectors. Right: the 8 sectors rearranged, alternating point-up and point-down, into a shape close to a '
                          'parallelogram whose base is about half the circumference and whose height is about r.', note=NTS)
CYL = cylinder('r', 'h', 'Right circular cylinder with base radius r and height h (dashed radius on top and dashed height through the center).')

SETS = [
    # ------------------------------------------------------------------ 75. GMD.A.1 circumference argument
    S('HSG-GMD.A.1', 'Informal arguments for the circumference of a circle',
      target='Give informal arguments (similarity, rolling, and limits of polygon perimeters) for the formula C = πd = 2πr for the circumference of a circle', strand='core',
      covers=['GMD1-circle'],
      main=[
          proof('Regular hexagons are inscribed in and circumscribed about a circle of radius 1. Their perimeters are 6 and 4√3 ≈ 6.93. Explain why this shows that 3 < π < 2√3 ≈ 3.46.',
                ans='Explanation:', method='Compare the circumference 2π with the two perimeters, then divide by 2.',
                key='The circle lies between the two hexagons, so 6 < C < 4√3; with C = 2π this gives 3 < π < 2√3 ≈ 3.46.',
                note=EXP + 'Essential: the inscribed hexagon is six equilateral triangles of side 1 (perimeter 6); the circumference is between the inner and outer perimeters; C = 2π · 1; divide by 2. '
                           'Invalid: quoting π ≈ 3.14 as the reason.'),
          proof('Explain why the ratio of circumference to diameter is the same number (π) for every circle, so that C = πd = 2πr.', ans='Explanation:',
                method='Use the fact that all circles are similar.', key='Every circle is a dilation of every other, so C and d scale by the same factor and C/d is constant; that constant is called π.',
                note=EXP + 'Essential: circles are similar (dilation); lengths scale by the same factor k; C₂/d₂ = kC₁/kd₁ = C₁/d₁.'),
          proof('A wheel with diameter 70 cm rolls one full turn along level ground without slipping, and a student measures the distance traveled as 219.9 cm. Explain why that distance is the '
                'circumference, use the measurement to estimate π, and say why a measurement supports the formula but does not prove it.', ans='Explanation:',
                method='Relate each point of the rim to the ground it touches; divide distance by diameter.',
                key='Each point of the rim touches the ground once in one turn, so the distance equals the circumference; 219.9 ÷ 70 ≈ 3.141, close to π. A measurement has error and covers one wheel only.',
                note=EXP + 'Essential: rolling without slipping lays the rim along the ground; C/d ≈ 3.141; evidence versus proof.'),
          proof('A regular hexagon is inscribed in a circle of radius 5. Find the hexagon\'s perimeter, compare it with the circle\'s circumference, and explain what happens as the number of sides increases.',
                ans='Explanation:', method='Split the hexagon into six triangles from the center; compare 30 with 10π; describe the trend.',
                key='Perimeter 30 < 10π ≈ 31.4; with more sides the perimeter gets closer to the circumference.',
                note=EXP + 'Essential: six equilateral triangles of side 5 (central angles 60°, two radii), so perimeter 30; 30 < 10π; more sides bring the perimeter closer to the circumference.'),
          proof('Regular polygons with 6, 12 and 24 sides are inscribed in a circle of radius 1. Their perimeters are 6, %.3f and %.3f. Explain what these values suggest about the circumference and '
                'how the formula C = 2πr follows for a circle of any radius r.' % (24 * math.sin(math.radians(15)), 48 * math.sin(math.radians(7.5))), ans='Explanation:',
                method='Describe the trend of the perimeters, then use similarity (scaling by r).',
                key='The perimeters increase toward 2π ≈ 6.283, the circumference of the unit circle; a circle of radius r is the unit circle dilated by r, so its circumference is 2π · r.',
                note=EXP + 'Essential: the inscribed perimeters approach the circumference from below; the limit for radius 1 is 2π; dilation by r multiplies lengths by r.'),
      ],
      back=[
          B('Circumference formulas', '7.G.B.4', [
              sa('Find the exact circumference of a circle of radius 4.', 'Answer:', key='8π', note='Form required: exact value.'),
              sa('Find the exact circumference of a circle of diameter 9.', 'Answer:', key='9π', note='Form required: exact value. C = πd.'),
              mc('Half the circumference of a circle of radius r is', ['πr', '2πr', 'πr²', 'r/2'], note='½ · 2πr.'),
              tf('C = 2πr', key=True, note='Formula.'),
              tf('A = 2πr', key=False, note='A = πr².'),
          ], align='exact',
            why=why('the student does not know the formula being justified.', 'the argument explains it.', 'states and uses the circumference formula.')),
          B('Perimeters of regular polygons', '3.MD.D.8', [
              sa('Find the perimeter of a regular hexagon with side 5.', 'Perimeter:', key='30', note='Any equivalent form.'),
              sa('Find the perimeter of a regular octagon with side 2.5 cm.', 'Perimeter:', key='20 cm', note='Any equivalent form.'),
              mc('A regular 12-gon has perimeter 36. Each side is', ['3', '12', '36', '432'], note='36 ÷ 12.'),
              tf('A regular polygon with n sides of length s has perimeter ns.', key=True, note='Equal sides.'),
              tf('A regular pentagon with side 4 has perimeter 16.', key=False, note='5 × 4 = 20.'),
          ], align='supporting', num=4,
            why=why('the student cannot find polygon perimeters.', 'the polygon argument compares them with the circumference.', 'computes perimeters of regular polygons.')),
          B('All circles are similar', 'HSG-C.A.1', [
              tf('Any circle can be mapped to any other circle by a translation and a dilation.', key=True, note='Similarity.'),
              sa('A circle of radius 2 is dilated to radius 6. By what factor is the circumference multiplied?', 'Factor:', key='3', note='Any equivalent form.'),
              mc('Circles of radii 3 and 12 have circumferences in the ratio', ['1 : 4', '1 : 16', '1 : 9', '3 : 4'], note='Scale factor.'),
              sa('Why does C/d not depend on the size of the circle?', 'Answer:', key='Both C and d are multiplied by the same scale factor.', note='Any equivalent answer.'),
              tf('A larger circle has a larger value of π.', key=False, note='π is constant.'),
          ], align='supporting',
            why=why('the student does not see why π is a constant.', 'the circumference argument uses similarity.', 'uses similarity of circles.')),
      ],
      f1=B('Trap π between inscribed and circumscribed polygons', 'HSG-GMD.A.1', [
          sa('A circle has radius 1. Find the perimeters of the inscribed square and the circumscribed square, and use them to write bounds for π.', 'Answer:',
             key='Inscribed 4√2 ≈ 5.66, circumscribed 8; 5.66 < 2π < 8, so 2.83 < π < 4.', note='Form required: both perimeters and the bounds. Inscribed side √2.'),
          sa('Inscribed and circumscribed regular 12-gons of a circle of radius 1 have perimeters about 6.212 and 6.431. What bounds for π do they give (to the nearest hundredth)?', 'Answer:',
             key='3.11 < π < 3.22', note='Form required: both bounds. Divide each perimeter by 2.'),
          tf('Using polygons with more sides gives closer bounds for π.', key=True, note='Both perimeters approach the circumference.'),
          mc('Why is the circumscribed polygon\'s perimeter larger than the circumference?', ['The circle lies inside it, and a curve inside a convex shape is shorter than the shape\'s boundary',
                                                                                                'Its sides are curved', 'It has fewer sides', 'Its radius is smaller'],
             note='The circle is enclosed by the polygon.'),
          sa('Archimedes used 96-gons and found 3 10/71 < π < 3 1/7. Write these bounds as decimals to the nearest thousandth.', 'Answer:', key='3.141 < π < 3.143',
             note='Form required: both decimals. 3 10/71 ≈ 3.1408 and 3 1/7 ≈ 3.1429.'),
      ], prog='same-course deepening', demand='Bound the circumference from both sides and turn the bounds into an estimate of π.'),
      f2=B('Extend the circumference argument to arcs and curved boundaries', 'HSG-GMD.A.1', [
          sa('Use the circumference formula to explain why an arc with central angle 90° in a circle of radius 6 has length 3π, and find its length to the nearest tenth.', 'Answer:',
             key='The arc is 90/360 = ¼ of the circle, so its length is ¼ · 2π · 6 = 3π ≈ 9.4.', note='Form required: the fraction-of-the-circle reasoning and the value (rounding to 0.1).'),
          sa('Explain why the length of an arc is proportional to its central angle, so that an arc of θ° has length (θ/360) · 2πr.', 'Answer:',
             key='Equal central angles cut off congruent arcs (a rotation about the center maps one onto another), so the 360° of the circle split the circumference 2πr in proportion to the angle.',
             note='Any equivalent explanation using equal angles ↔ equal arcs.'),
          tf('A semicircular region of radius 5 has perimeter 5π.', key=False, note='The perimeter also includes the diameter: 5π + 10.'),
          mc('A running track has two straight sides of 100 m and two semicircular ends of radius 30 m. Its length is about', ['388 m', '294 m', '388π m', '200 m'],
             note='200 + 60π ≈ 388.5 m.'),
          sa('The circumference argument used inscribed polygons whose perimeters approach 2πr. Explain why inscribed broken lines (chords) can be used the same way to measure the length of an arc.', 'Answer:',
             key='Chords that split the arc into smaller and smaller pieces form broken lines whose lengths increase toward the arc length, just as the polygon perimeters approach the circumference.',
             note='Any equivalent explanation of the limit of chord lengths.'),
      ], prog='same-course deepening', demand='Extend the circumference argument from whole circles to arcs and boundaries made of arcs and segments.',
        builds='Builds on FORWARD 1: polygon bounds for the whole circle become chord approximations and proportional arcs.')),

    # ------------------------------------------------------------------ 103. GMD.A.1 circle area argument
    S('HSG-GMD.A.1', 'Informal arguments for the area of a circle',
      target='Give informal arguments (dissection into sectors or rings, similarity, and estimation) for the formula A = πr² for the area of a circle', strand='core',
      covers=['GMD1-area'], num=103,
      main=[
          proof('A circle of radius r is cut into many equal sectors, which are rearranged as shown. Explain why this shows that the area of the circle is πr².', fig=SECTORS,
                ans='Explanation:', method='Describe the base and height of the rearranged shape and what happens as the number of sectors grows.', key='Area = (half the circumference) × r = πr · r = πr².',
                note=EXP + 'Essential: the shape approaches a parallelogram (rectangle); its height approaches r; its base is half the circumference, πr; area = πr · r = πr². '
                           'Invalid: "the formula says so" or measuring one drawing.'),
          proof('A circle of radius r is cut into many thin rings, like the layers of an onion. Each ring is cut open and straightened into a thin strip, and the strips are stacked from shortest '
                '(at the top) to longest (at the bottom). Explain why the stack approaches a triangle and why its area is πr².', ans='Explanation:',
                method='Find the lengths of the shortest and longest strips and the height of the stack.',
                key='The strips have lengths 2π · (distance from the center), from about 0 to 2πr, and the stack is r tall, so it approaches a triangle with base 2πr and height r: ½ · 2πr · r = πr².',
                note=EXP + 'Essential: strip length grows in proportion to the distance from the center; outer strip 2πr; height r; triangle area ½bh = πr².'),
          proof('Use similarity to explain why the area of a circle of radius r equals r² times the area of a circle of radius 1. Then use the fact that the unit circle has area π to write the formula.',
                ans='Explanation:', method='A circle of radius r is a dilation of the unit circle by factor r; describe what a dilation does to areas.',
                key='A dilation by r multiplies every area by r², so A = r² · (area of the unit circle) = πr².',
                note=EXP + 'Essential: circles are similar; areas scale by k²; the unit circle\'s area is π; A = πr².'),
          proof('A quarter circle of radius 10 is drawn on a grid of unit squares. Counting full squares and estimating the partial ones gives about 78.5 squares. Explain how this supports '
                'A = πr² and why counting is evidence rather than proof.', ans='Explanation:', method='Compare 4 × 78.5 with πr² for r = 10.',
                key='The whole circle covers about 4 × 78.5 = 314 squares, and π · 10² ≈ 314.2, which agrees. Counting is approximate and checks one circle only, so it supports but does not prove the formula.',
                note=EXP + 'Essential: the scaled-up count (about 314); comparison with 100π; evidence versus proof.'),
          proof('Explain why the area of a circle of radius r is more than 2r² and less than 4r², using an inscribed square and a circumscribed square, and check that πr² fits these bounds.',
                ans='Explanation:', method='Find the area of each square in terms of r.',
                key='The circumscribed square has side 2r (area 4r²); the inscribed square has diagonal 2r (area 2r²); the circle lies between them, and 2r² < πr² ≈ 3.14r² < 4r².',
                note=EXP + 'Essential: both square areas from r (diagonal 2r gives area ½(2r)²); the circle is between them; 2 < π < 4.'),
      ],
      back=[
          B('Area of a circle', '7.G.B.4', [
              sa('Find the exact area of a circle of radius 4.', 'Answer:', key='16π', note='Form required: exact value.'),
              sa('Find the exact area of a circle of diameter 12.', 'Answer:', key='36π', note='Form required: exact value. r = 6.'),
              mc('A circle has area 25π. Its radius is', ['5', '25', '12.5', '√5'], note='r² = 25.'),
              tf('A circle of radius 3 has area 9π.', key=True, note='π · 3².'),
              tf('Tripling the radius triples the area.', key=False, note='The area is multiplied by 9.'),
          ], align='exact',
            why=why('the student does not know the formula being justified.', 'the argument explains it.', 'states and uses the area formula.')),
          B('Area of a parallelogram', '6.G.A.1', [
              sa('Area of a parallelogram with base 9 and height 4?', 'Area:', key='36', note='Any equivalent form.'),
              tf('A parallelogram has the same area as a rectangle with the same base and height.', key=True, note='Cut and slide.'),
              mc('A parallelogram\'s area is', ['base × height', 'base × slanted side', '½ base × height', 'base + height'], note='Perpendicular height.'),
              sa('A parallelogram has base πr and height r. Area?', 'Area:', key='πr²', note='Any equivalent form.'),
              tf('The slanted side is the height of a parallelogram.', key=False, note='Perpendicular height.'),
          ], align='exact',
            why=why('the student cannot find the area of the rearranged shape.', 'the argument ends with base × height.', 'finds parallelogram areas.')),
          B('Scale factors and area', '7.G.A.1', [
              sa('A scale drawing uses factor 3. A region of 5 cm² on the original covers how much on the drawing?', 'Area:', key='45 cm²', note='Any equivalent form. 3² · 5.'),
              sa('A square of side 2 is enlarged by factor 4. New area?', 'Area:', key='64', note='Any equivalent form.'),
              mc('Enlarging a figure by factor k multiplies its area by', ['k²', 'k', '2k', 'k³'], note='Both dimensions scale.'),
              tf('Halving every length of a figure multiplies its area by ¼.', key=True, note='(½)².'),
              tf('Enlarging by factor 3 triples the area.', key=False, note='9 times.'),
          ], align='supporting',
            why=why('the student does not know how area scales.', 'the similarity argument uses k².', 'scales areas.')),
      ],
      f1=B('Area of a circle as a limit of regular polygons', 'HSG-GMD.A.1', [
          proof('A regular n-gon is inscribed in a circle of radius r. Its area is ½ · perimeter · apothem. Explain why this approaches πr² as n increases.', ans='Explanation:',
                method='Describe what the perimeter and apothem approach.', key='The perimeter approaches 2πr and the apothem approaches r, so the area approaches ½ · 2πr · r = πr².',
                note=EXP + 'Essential: perimeter → circumference; apothem → radius; substitution.'),
          sa('Find the area of a regular hexagon with side 2 and apothem √3. Compare with the area of its circumscribed circle (radius 2).', 'Answer:', key='6√3 ≈ 10.4 < 4π ≈ 12.6',
             note='Form required: both numbers. ½ · 12 · √3.'),
          tf('An inscribed polygon always has less area than its circle.', key=True, note='It lies inside the circle.'),
          mc('As n grows, the apothem of an inscribed regular n-gon approaches', ['r', '2r', 'πr', '0'], note='The sides approach the circle.'),
          sa('Why do mathematicians call this an "informal" argument?', 'Answer:', key='It relies on what the shapes approach (a limit) without a formal proof of the limit.', note='Any reasonable answer.'),
      ], prog='same-course deepening', demand='Give a second, polygon-limit argument and connect perimeter and area formulas.'),
      f2=B('From area to volume: stacking disks', 'HSG-GMD.A.1', [
          sa('A stack of 40 identical coins, each a disk of radius 1 cm and thickness 0.2 cm, forms a cylinder. Find the exact volume.', 'Volume:', key='8π cm³', note='Form required: exact value. π · 1² · 8.'),
          tf('A cylinder can be thought of as a stack of congruent disks.', key=True, note='Layers.'),
          mc('The volume of a stack of disks of area πr² and total height h is', ['πr²h', '2πrh', 'πr²', '⅓πr²h'], note='Base area × height.'),
          sa('Explain how the area of a circle is used to find the volume of a cylinder.', 'Answer:', key='The volume is the base area πr² times the height h.', note='Any equivalent explanation.'),
          sa('Each disk in a stack has area 12 cm² and the stack is 5 cm high. Volume?', 'Volume:', key='60 cm³', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Use the circle area as the base of a volume argument (the next part of the same standard).',
        builds='Builds on FORWARD 1: once the circle\'s area is justified, it becomes the base area in the cylinder argument.')),

    # ------------------------------------------------------------------ 76. GMD.A.1 cylinder volume
    S('HSG-GMD.A.1', 'Informal argument for the volume of a cylinder',
      target='Give an informal argument (stacking congruent cross-sections and Cavalieri\'s principle) for the formula V = πr²h for the volume of a cylinder', strand='core', covers=['GMD1-cylinder'],
      main=[
          proof('Explain why the volume of the cylinder shown is V = πr²h.', fig=CYL, ans='Explanation:', method='Think of the cylinder as a stack of thin congruent disks.',
                key='Each layer is a disk of area πr²; stacking layers to height h gives volume (base area) × (height) = πr²h.',
                note=EXP + 'Essential: congruent circular cross-sections of area πr²; volume = base area × height, as for a prism (layers of unit thickness); result πr²h.'),
          proof('A right cylinder and an oblique cylinder have the same radius r and the same height h. Explain why they have the same volume.', ans='Explanation:',
                method='Use Cavalieri\'s principle.', key='At every height both cross-sections are disks of area πr², so by Cavalieri\'s principle their volumes are equal: πr²h.',
                note=EXP + 'Essential: equal heights; equal cross-sectional areas at every level; Cavalieri\'s principle cited. Invalid: "they look the same size".'),
          proof('A cylinder has radius r and height h. A square prism has base area πr² and the same height h. Use Cavalieri\'s principle to explain why the two solids have the same volume, '
                'and conclude the cylinder formula.', ans='Explanation:', method='Compare the cross-section areas at every height.',
                key='Every horizontal cross-section of the cylinder is a disk of area πr², and every cross-section of the prism has area πr²; equal heights and equal cross-section areas give equal volumes, '
                    'so V = (πr²)h.', note=EXP + 'Essential: both cross-section areas named and equal at every level; equal heights; Cavalieri\'s principle; prism volume Bh.'),
          proof('Explain why V = Bh works for both prisms and cylinders.', ans='Explanation:', method='Describe the cross-sections of each solid and how the volume is built from them.',
                key='Both have congruent cross-sections of area B at every height, so the volume is B times the height.',
                note=EXP + 'Essential: congruent cross-sections parallel to the base; layers of thickness 1 (or thin layers) each of volume B; h layers give Bh.'),
          proof('A cylinder of radius r and height h is approximated by prisms whose bases are regular polygons inscribed in its base circle. Explain why the prism volumes approach πr²h.',
                ans='Explanation:', method='Describe what the polygon base areas approach as the number of sides grows.',
                key='Each prism has volume (polygon area) × h; as the number of sides grows, the polygon area approaches πr², so the volumes approach πr²h.',
                note=EXP + 'Essential: prism volume Bh; inscribed polygon areas approach the circle area; conclusion.'),
      ],
      back=[
          B('Volume of a rectangular prism as layers', '5.MD.C.5', [
              sa('A prism has a 4 × 3 base and height 5. How many unit cubes are in one layer, and what is the volume?', 'Answer:', key='12 per layer; 60', note='Form required: both.'),
              tf('V = Bh, where B is the area of the base.', key=True, note='Layers.'),
              mc('A prism has base area 20 and height 7. Volume?', ['140', '27', '70', '200'], note='B × h.'),
              sa('A prism has 6 layers of 10 cubes each. Volume?', 'Volume:', key='60 cubic units', note='Any equivalent form.'),
              tf('Volume is measured in square units.', key=False, note='Cubic units.'),
          ], align='exact',
            why=why('the student does not see volume as stacked layers.', 'the cylinder argument extends it.', 'computes prism volume as layers.')),
          B('Area of a circle', '7.G.B.4', [
              sa('Exact area of a circle of radius 3?', 'Area:', key='9π', note='Form required: exact value.'),
              sa('Exact area of a circle of diameter 10?', 'Area:', key='25π', note='Form required: exact value.'),
              mc('A = ', ['πr²', '2πr', 'πd', 'πr'], note='Formula.'),
              tf('The base of a cylinder is a circle.', key=True, note='Definition.'),
              tf('The area of a circle of radius 2 is 4.', key=False, note='4π.'),
          ], align='exact',
            why=why('the student cannot find the base area.', 'V = (base area) × h.', 'finds circle areas.')),
          B('Cross-sections parallel to the base', '7.G.A.3', [
              tf('A slice of a right prism parallel to its base is congruent to the base.', key=True, note='Same shape and size.'),
              sa('A cylinder is sliced parallel to its base. Describe the cross-section.', 'Answer:', key='A circle congruent to the base', note='Any equivalent answer.'),
              mc('A rectangular prism sliced parallel to its 3 × 4 base gives a', ['3 × 4 rectangle', 'triangle', 'smaller rectangle', 'circle'], note='Congruent.'),
              sa('Why do all horizontal slices of a cylinder have the same area?', 'Answer:', key='They are all congruent to the base.', note='Any equivalent answer.'),
              tf('Horizontal slices of a cylinder get smaller toward the top.', key=False, note='That is a cone.'),
          ], align='supporting',
            why=why('the student does not see the congruent layers.', 'the argument depends on them.', 'describes parallel cross-sections.')),
      ],
      f1=B('Cavalieri\'s principle with different shapes', 'HSG-GMD.A.1', [
          sa('A cylinder with base area 50 cm² and a square prism with base area 50 cm² both have height 8 cm. Compare their volumes.', 'Answer:', key='Equal: 400 cm³ each', note='Form required: the comparison with the value.'),
          sa('An oblique cylinder has radius 3 and vertical height 7 (its slanted side is 9). Find its exact volume.', 'Volume:', key='63π', note='Form required: exact value. Use the vertical height, not the slant.'),
          tf('Cavalieri\'s principle requires equal cross-sectional areas at every height and equal heights.', key=True, note='Statement.'),
          mc('Two stacks of 30 identical cards, one straight and one slanted, have', ['equal volumes', 'different volumes', 'equal surface areas', 'no volume'], note='Same cross-sections.'),
          sa('State Cavalieri\'s principle in your own words.', 'Answer:', key='Two solids with the same height and equal cross-sectional areas at every level have the same volume.', note='Any equivalent statement.'),
      ], prog='same-course deepening', demand='Apply Cavalieri\'s principle to solids with different shapes but equal cross-sectional areas.'),
      f2=B('Use the cylinder volume formula to solve problems', 'HSG-GMD.A.3', [
          sa('A can has radius 4 cm and height 12 cm. Find its volume to the nearest cubic centimeter.', 'Volume:', key='%d cm³' % round(PI * 16 * 12), note='Rounding to the nearest whole number required. 192π.'),
          sa('A pipe 2 m long has inner radius 0.1 m. Find the volume of water it holds, to the nearest thousandth of a cubic meter.', 'Volume:', key='%.3f m³' % (PI * 0.01 * 2),
             note='Rounding to 0.001 required. 0.02π.'),
          tf('Doubling the height of a cylinder multiplies its volume by 4.', key=False, note='Volume is linear in h, so it doubles.'),
          mc('Doubling the radius of a cylinder multiplies its volume by', ['4', '2', '8', '6'], note='r².'),
          sa('A cylindrical tank has diameter 6 ft and height 10 ft. Exact volume?', 'Volume:', key='90π ft³', note='Form required: exact value. r = 3.'),
      ], prog='cross-standard extension', demand='Use the justified formula in measurement problems with units and rounding.',
        builds='Builds on FORWARD 1: the same base-area × height reasoning now computes real volumes.')),
]

_s = 2.2
CUBE3 = cube('Cube with one top-front corner joined to four other vertices: a solid diagonal of the front face, a solid diagonal of the top face, a dashed diagonal of the left face, '
             'and a dashed space diagonal to the back-bottom-right corner. These segments split the cube into three congruent square pyramids with a common apex.',
             extra=[('seg', (0, _s), (_s, 0)), ('seg', (0, _s), (_s + 0.9, _s + 0.7)), ('seg', (0, _s), (0.9, 0.7), {'dash': True}), ('seg', (0, _s), (_s + 0.9, 0.7), {'dash': True})])
PYR = sq_pyramid('s', 'h', 'Square pyramid with base side s and height h (dashed segment from the apex to the center of the base).')
CONE = cone('r', 'h', 'Right circular cone with base radius r and height h; the height is dashed and meets the radius at a right angle.')

SETS += [
    # ------------------------------------------------------------------ 77. GMD.A.1 pyramid argument
    S('HSG-GMD.A.1', 'Informal arguments for the volume of a pyramid',
      target='Give informal arguments (dissection of a cube or prism, Cavalieri\'s principle, and stacked slabs) for V = ⅓Bh for every pyramid', strand='core', covers=['GMD1-pyramid'],
      main=[
          proof('A cube with edge s is split into three congruent pyramids that share one vertex of the cube as their apex, as shown. Use this, together with scaling and Cavalieri\'s principle, '
                'to explain why EVERY pyramid with base area B and height h has volume ⅓Bh.', fig=CUBE3, ans='Explanation:',
                method='(1) Find the volume of one of the three pyramids. (2) Stretch it vertically to any height h. (3) Use Cavalieri\'s principle to compare any pyramid with a square pyramid of the same base area and height.',
                key='Each of the three pyramids has volume ⅓s³ = ⅓(s²)(s). Stretching vertically by h/s multiplies the volume by h/s, giving ⅓s²h. Any pyramid with base area B and height h has '
                    'cross-sections B((h - y)/h)² at height y, the same as a square pyramid with base area B and height h, so by Cavalieri\'s principle its volume is ⅓Bh.',
                note=EXP + 'Essential: (1) the three congruent pyramids fill the cube, each with base s² and height s, so ⅓s³; (2) a vertical stretch extends this to any height; '
                           '(3) cross-sections are scaled copies of the base with area B((h - y)/h)², so Cavalieri\'s principle extends it to any base shape and apex position. '
                           'The cube case alone is NOT sufficient for full credit.'),
          proof('A triangular prism with base area B and height h is cut into three pyramids (tetrahedra), as Euclid did. Pairs of these pyramids have congruent bases and equal heights. '
                'Explain why each pyramid has volume ⅓Bh.', ans='Explanation:',
                method='Use the fact that pyramids with equal base areas and equal heights have equal volumes (Cavalieri\'s principle), applied to two pairs.',
                key='Pyramid 1 and pyramid 2 have equal bases and heights, and so do pyramids 2 and 3, so all three have equal volume. They fill the prism (volume Bh), so each has ⅓Bh; '
                    'pyramid 1 has the prism\'s base and height.',
                note=EXP + 'Essential: two equal-volume pairs give three equal volumes; their sum is Bh; one of them has base B and height h, so V = ⅓Bh.'),
          proof('In a class experiment, a hollow square pyramid and a hollow square prism have the same base and the same height. It takes three pyramids full of sand to fill the prism. '
                'Explain what this shows about the pyramid formula and why it is evidence, not a proof.', ans='Explanation:',
                method='Relate the prism volume Bh to the three pyramid fillings, then discuss measurement.',
                key='The pyramid holds about ⅓ of the prism, Bh, which supports V = ⅓Bh. The experiment has measurement error and tests one pyramid only, so it does not prove the formula for all pyramids.',
                note=EXP + 'Essential: the ⅓ relationship with the prism; evidence versus proof.'),
          proof('A cube with edge 6 is split into three congruent pyramids that share one vertex of the cube as their apex. Find the volume of each pyramid, then show that ⅓Bh gives the same value for one pyramid, '
                'and explain why this agreement is a check, not a proof for all pyramids.', ans='Explanation:', method='Divide the cube\'s volume by 3; then compute ⅓Bh for one pyramid.',
                key='Each is 216 ÷ 3 = 72; one pyramid has base 6 × 6 = 36 and height 6, and ⅓ · 36 · 6 = 72. One numerical case cannot cover every pyramid.',
                note=EXP + 'Essential: 216 ÷ 3 = 72; B = 36 and h = 6 for one pyramid; ⅓Bh = 72; a single case is evidence only.'),
          proof('A square pyramid has base side s and height h. Imagine it built from n stacked square slabs, each of thickness h/n, where the slab k steps from the top has side ks/n. '
                'The total slab volume is (s²h/n³) × (the sum of the squares 1², 2², 3², and so on up to n²). For n = 10 and n = 100 this equals 0.385s²h and 0.338s²h. Explain how this supports V = ⅓s²h.', ans='Explanation:',
                method='Describe what the slabs approach and what the coefficients approach as n grows.',
                key='The slabs approach the pyramid as they get thinner, and the coefficients 0.385, 0.338, … approach ⅓, so the volume is ⅓s²h.',
                note=EXP + 'Essential: the slabs approximate the pyramid more closely as n grows; the coefficient trend toward ⅓; conclusion (an informal limit argument).'),
      ],
      back=[
          B('Volume of a prism', '7.G.B.6', [
              sa('A prism has base area 36 and height 6. Volume?', 'Volume:', key='216', note='Any equivalent form.'),
              sa('A cube has side 6. Volume?', 'Volume:', key='216', note='Any equivalent form.'),
              mc('V = ', ['Bh', '⅓Bh', '2Bh', 'B + h'], note='Prism.'),
              tf('A cube is a prism.', key=True, note='Square base.'),
              tf('A prism\'s volume depends on the number of its faces.', key=False, note='Base area and height.'),
          ], align='exact',
            why=why('the student cannot find the prism\'s volume.', 'the pyramid is a third of it.', 'computes prism volume.')),
          B('Base area of a pyramid', '6.G.A.1', [
              sa('A square base has side 10. Area?', 'Area:', key='100', note='Any equivalent form.'),
              sa('A triangular base has base 6 and height 4. Area?', 'Area:', key='12', note='Any equivalent form.'),
              mc('The base of a square pyramid is a', ['square', 'triangle', 'circle', 'rectangle that is not a square'], note='Definition.'),
              tf('B in V = ⅓Bh means the area of the base.', key=True, note='Area.'),
              tf('B is the length of a base edge.', key=False, note='Area.'),
          ], align='exact',
            why=why('the student uses an edge instead of the base area.', 'B is an area.', 'finds base areas.')),
          B('Split a volume into equal parts', '5.MD.C.5', [
              sa('A box of volume 60 cm³ is split into three equal parts. Volume of each?', 'Volume:', key='20 cm³', note='Any equivalent form.'),
              sa('Three congruent blocks fill a cube of volume 27. Volume of one block?', 'Volume:', key='9', note='Any equivalent form.'),
              mc('A solid made of non-overlapping parts has volume', ['the sum of the parts\' volumes', 'the largest part\'s volume', 'the product of the parts\' volumes', 'the average volume'],
                 note='Additivity.'),
              tf('If three equal pieces fill a prism, each piece has ⅓ of the prism\'s volume.', key=True, note='Equal shares.'),
              tf('Cutting a solid into pieces changes its total volume.', key=False, note='Volume is additive.'),
          ], align='supporting', num=4,
            why=why('the student does not see why "three equal pieces" means one third.', 'the dissection argument depends on it.', 'splits volumes into equal parts.')),
      ],
      f1=B('Cavalieri\'s principle for pyramids', 'HSG-GMD.A.1', [
          sa('A square pyramid and a triangular pyramid both have base area 50 cm² and height 9 cm. Compare their volumes.', 'Answer:', key='Equal: 150 cm³ each', note='Form required: the comparison with the value.'),
          sa('An oblique pyramid has a square base with side 4 and vertical height 6. Find its volume.', 'Volume:', key='32', note='Any equivalent form. ⅓ · 16 · 6; use the vertical height.'),
          tf('Two pyramids with equal base areas and equal heights have equal volumes even if their apexes are in different positions.', key=True, note='Cavalieri.'),
          mc('Why do two pyramids with equal base areas and equal heights have equal cross-section areas at every level?', ['Both cross-sections are scaled copies of the bases by the same factor',
                                                                                                                 'Their bases have the same shape', 'They have the same slant height', 'They have the same apex'],
             note='Each cross-section at height y is the base scaled by (h - y)/h.'),
          sa('A cross-section of a pyramid halfway up has what fraction of the base area?', 'Fraction:', key='¼', note='Any equivalent form. Scale factor ½.'),
      ], prog='same-course deepening', demand='Extend the argument with Cavalieri\'s principle to oblique pyramids and pyramids with different base shapes.'),
      f2=B('Use the pyramid volume formula', 'HSG-GMD.A.3', [
          sa('A square pyramid has base side 9 m and height 10 m. Volume?', 'Volume:', key='270 m³', note='Any equivalent form.'),
          sa('A rectangular pyramid has a 6 in. by 4 in. base and height 7.5 in. Find its volume.', 'Volume:', key='60 in³', note='Any equivalent form. ⅓ · 24 · 7.5.'),
          tf('A pyramid with the same base and height as a prism of volume 90 has volume 45.', key=False, note='It has ⅓ of the volume: 30.'),
          mc('A pyramid with base area 48 and height 5 has volume', ['80', '240', '120', '53'], note='⅓ · 240.'),
          sa('A paperweight is a pyramid whose triangular base has base 6 cm and height 5 cm; the pyramid is 8 cm tall. Find its volume.', 'Volume:', key='40 cm³',
             note='Any equivalent form. B = 15; ⅓ · 15 · 8.'),
      ], prog='cross-standard extension', demand='Apply the justified formula to computation problems.',
        builds='Builds on FORWARD 1: the ⅓Bh formula, justified for any apex position, is now applied.')),

    # ------------------------------------------------------------------ 104. GMD.A.1 cone argument
    S('HSG-GMD.A.1', 'Informal arguments for the volume of a cone',
      target='Give informal arguments (limits of pyramids, Cavalieri\'s principle, and stacked disks) for V = ⅓πr²h for a cone', strand='core', covers=['GMD1-cone'], num=104,
      main=[
          proof('Explain why the volume of a cone is ⅓πr²h, using pyramids.', fig=CONE, ans='Explanation:', method='Think of pyramids whose bases are regular polygons with more and more sides.',
                key='Pyramids with regular n-gon bases inscribed in the circle have V = ⅓Bh; as n grows, B approaches πr² and the pyramids approach the cone, so V = ⅓πr²h.',
                note=EXP + 'Essential: pyramid volume ⅓Bh; base polygons approach the circle (B → πr²); the pyramids approach the cone. Alternative: Cavalieri comparison with a pyramid of equal base area and height.'),
          proof('A cone has base radius r and height h. A square pyramid has base area πr² and the same height h. Use Cavalieri\'s principle to explain why the cone\'s volume is ⅓πr²h.',
                ans='Explanation:', method='Compare the cross-section areas of the two solids at the same height y.',
                key='At height y both cross-sections are copies of the bases scaled by (h - y)/h, so both have area πr²((h - y)/h)²; equal areas at every level and equal heights give equal volumes, ⅓πr²h.',
                note=EXP + 'Essential: the scale factor (h - y)/h for both solids; equal cross-section areas; Cavalieri\'s principle; the pyramid formula ⅓Bh with B = πr².'),
          proof('In an experiment, three cones full of water exactly fill a cylinder with the same base radius and height. Explain what this shows about the cone formula and why it is evidence, not a proof.',
                ans='Explanation:', method='Relate the cylinder volume πr²h to the three cone fillings, then discuss measurement.',
                key='One cone holds about ⅓ of πr²h, which supports V = ⅓πr²h; the experiment has measurement error and tests one cone, so it does not prove the formula.',
                note=EXP + 'Essential: the ⅓ relationship with the cylinder; evidence versus proof.'),
          proof('A cone with radius r and height h is approximated by n stacked disks of thickness h/n; the disk k steps from the top has radius kr/n. The total disk volume is '
                '(πr²h/n³) × (the sum of the squares 1², 2², 3², and so on up to n²), which equals 0.385πr²h for n = 10 and 0.338πr²h for n = 100. Explain how this supports V = ⅓πr²h.', ans='Explanation:',
                method='Describe what the disks approach and what the coefficients approach.',
                key='As the disks get thinner they fit the cone more closely, and the coefficients approach ⅓, so V = ⅓πr²h.',
                note=EXP + 'Essential: the disks approximate the cone better as n grows; the trend toward ⅓; conclusion.'),
          proof('A cone has base radius r and height h. A plane parallel to the base cuts the cone at height y above the base. Explain why the cross-section is a circle of radius r(h - y)/h, and why '
                'this fact is what makes the cone\'s volume ⅓ of the cylinder\'s rather than ½.', ans='Explanation:',
                method='Use similar triangles in a vertical cross-section through the apex; compare how the cross-section areas shrink.',
                key='The small cone above the cut is similar to the whole cone with ratio (h - y)/h, so the radius is r(h - y)/h. The areas shrink like the SQUARE of that ratio, πr²((h - y)/h)², '
                    'so most of the volume is near the base and the total is ⅓πr²h, less than the ½ a linear shrink would suggest.',
                note=EXP + 'Essential: similar triangles give the radius; area scales by the square of the ratio; link to the ⅓ factor (via Cavalieri or slab sums).'),
      ],
      back=[
          B('Area of a circle', '7.G.B.4', [
              sa('Exact area of a circle of radius 7?', 'Area:', key='49π', note='Form required: exact value.'),
              sa('Exact area of a circle of diameter 8?', 'Area:', key='16π', note='Form required: exact value. r = 4.'),
              mc('The base of a cone is a', ['circle', 'triangle', 'square', 'sector'], note='Definition.'),
              tf('The base area of a cone with radius r is πr².', key=True, note='Circle area.'),
              tf('The base area of a cone with radius 2 is 4.', key=False, note='4π.'),
          ], align='exact',
            why=why('the student cannot find the base area.', 'the cone formula is ⅓ × base area × height.', 'finds circle areas.')),
          B('The cylinder volume argument', 'HSG-GMD.A.1', [
              tf('A cylinder\'s volume is πr²h because it is a stack of disks of area πr².', key=True, note='Set 76.'),
              sa('Cylinder radius 3, height 5: exact volume?', 'Volume:', key='45π', note='Form required: exact value.'),
              mc('A cone fits inside a cylinder with the same base and height. The cone\'s volume is', ['⅓ of the cylinder\'s', 'equal to the cylinder\'s', '½ of the cylinder\'s', '⅔ of the cylinder\'s'],
                 note='Cone vs cylinder.'),
              sa('A cylinder holds 60 cm³. A cone with the same base and height holds', 'Volume:', key='20 cm³', note='Any equivalent form.'),
              tf('A cone is a cylinder with the top cut off flat.', key=False, note='It comes to a point.'),
          ], align='supporting',
            why=why('the student cannot compare a cone with its cylinder.', 'the factor ⅓ compares them.', 'relates cone and cylinder volumes.')),
          B('The pyramid volume formula', 'HSG-GMD.A.1', [
              sa('A pyramid has base area 30 and height 8. Volume?', 'Volume:', key='80', note='Any equivalent form.'),
              tf('V = ⅓Bh holds for every pyramid, whatever the shape of its base.', key=True, note='Set 77.'),
              mc('A pyramid and a prism have the same base and height. The pyramid\'s volume is', ['⅓ of the prism\'s', '½ of the prism\'s', 'equal to the prism\'s', '3 times the prism\'s'], note='⅓Bh.'),
              sa('A pyramid has volume 40 and height 6. Base area?', 'Area:', key='20', note='Any equivalent form. 3 · 40 ÷ 6.'),
              tf('A pyramid has half the volume of the prism with the same base and height.', key=False, note='One third.'),
          ], align='exact',
            why=why('the student does not know the pyramid result.', 'the cone argument compares the cone with pyramids.', 'uses V = ⅓Bh.')),
      ],
      f1=B('Volumes of frustums (cones with the top cut off)', 'HSG-GMD.A.3', [
          sa('A cone has radius 6 and height 12. The top cone of height 4 is cut off by a plane parallel to the base. Find the exact volume of the remaining frustum.', 'Volume:', key='416π/3',
             note='Form required: exact value. Whole cone 144π; small cone radius 2, volume 16π/3; 144π - 16π/3 = 416π/3.'),
          sa('A cup is a frustum with bottom radius 3 cm, top radius 4 cm and height 6 cm. Extend it to a full cone and find the cup\'s volume to the nearest cubic centimeter.', 'Volume:',
             key='%d cm³' % round(PI / 3 * (16 * 24 - 9 * 18)), note='Rounding to the nearest whole number required. Full cone height 24 (radius 4); removed cone height 18 (radius 3); ⅓π(16 · 24 - 9 · 18) = 74π.'),
          tf('A frustum\'s volume is the large cone\'s volume minus the small cone\'s volume.', key=True, note='Subtraction of non-overlapping parts.'),
          mc('A cone is cut halfway up its height, parallel to the base. The small top cone has what fraction of the whole cone\'s volume?', ['⅛', '½', '¼', '⅓'], note='(½)³.'),
          sa('Explain why cutting a cone halfway up leaves 7/8 of its volume in the bottom part.', 'Answer:', key='The top cone is similar with ratio ½, so its volume is (½)³ = ⅛ of the whole; 1 - ⅛ = 7/8 remains.',
             note='Any equivalent explanation.'),
      ], prog='same-course deepening', demand='Combine the cone formula with similarity to find volumes of frustums.'),
      f2=B('Use the cone volume formula', 'HSG-GMD.A.3', [
          sa('A cone has radius 3 in. and height 8 in. Find its volume to the nearest tenth.', 'Volume:', key='%s in³' % d1(PI * 24), note='Rounding to 0.1 required. 24π.'),
          sa('A cone-shaped cup has diameter 6 cm and height 9 cm. Exact volume?', 'Volume:', key='27π cm³', note='Form required: exact value. r = 3.'),
          tf('A cone with the same base and height as a cylinder of volume 90 has volume 45.', key=False, note='It has ⅓ of the volume: 30.'),
          mc('A cone has base area 48 and height 5. Its volume is', ['80', '240', '120', '53'], note='⅓ · 240.'),
          sa('A pile of sand is a cone 2 m tall with base radius 3 m. Find its volume to the nearest tenth of a cubic meter.', 'Volume:', key='%s m³' % d1(PI * 6), note='Rounding to 0.1 required. 6π.'),
      ], prog='cross-standard extension', demand='Apply the justified formula to computation problems with exact and rounded answers.',
        builds='Builds on FORWARD 1: the cone formula, combined with similarity, now computes real volumes.')),

    # ------------------------------------------------------------------ 78. GMD.A.3 cylinders, pyramids, cones
    S('HSG-GMD.A.3', 'Use volume formulas for cylinders, pyramids, and cones',
      target='Use the volume formulas for cylinders, pyramids, and cones to solve problems, giving exact values and rounded values with units', strand='core', covers=['GMD3-cpc'],
      main=[
          sa('A cylinder has radius 3 cm and height 10 cm. Find its volume, exact and to the nearest tenth.', 'Volume:', fig=cylinder('3 cm', '10 cm', 'Cylinder with radius 3 cm and height 10 cm.'),
             key=pv(90, 'cm³'), note='Form required: both the exact value and rounding to 0.1, with units.'),
          sa('A cone has radius 6 ft and height 8 ft. Find its volume, exact and to the nearest tenth.', 'Volume:', fig=cone('6 ft', '8 ft', 'Cone with radius 6 ft and height 8 ft.'),
             key=pv(96, 'ft³'), note='Form required: both, with units. ⅓π · 36 · 8.'),
          sa('A square pyramid has base side 10 m and height 12 m. Find its volume.', 'Volume:', fig=sq_pyramid('10 m', '12 m', 'Square pyramid with base side 10 m and height 12 m.'),
             key='400 m³', note='Any equivalent form, with units. ⅓ · 100 · 12.'),
          sa('A cone has diameter 10 in. and slant height 13 in. Find its volume, exact and to the nearest tenth.', 'Volume:',
             fig=cone('', None, 'Cone with diameter 10 in. and slant height 13 in. (the slanted edge from apex to base is labeled 13 in.); the height is not labeled.', slant='13 in.'),
             key=pv(100, 'in³'), note='Form required: both, with units. r = 5; height √(169 - 25) = 12; ⅓π · 25 · 12.'),
          mc('A cylinder and a cone have the same radius and height. The cylinder holds 600 mL. The cone holds', ['200 mL', '300 mL', '600 mL', '1,800 mL'], note='⅓.'),
      ],
      back=[
          B('Area of a circle', '7.G.B.4', [
              sa('Exact area of a circle with radius 6?', 'Area:', key='36π', note='Form required: exact value.'),
              sa('Exact area of a circle with diameter 10?', 'Area:', key='25π', note='Form required: exact value.'),
              mc('A base of radius 3 has area', ['9π', '6π', '3π', '9'], note='πr².'),
              tf('Squaring the radius comes before multiplying by π.', key=True, note='Order of operations.'),
              tf('πr² with r = 3 is (3π)².', key=False, note='9π, not 9π².'),
          ], align='exact',
            why=why('the student cannot find the base area.', 'every formula uses it.', 'finds circle areas.')),
          B('Find a missing side with the Pythagorean Theorem', '8.G.B.7', [
              sa('A right triangle has hypotenuse 13 and one leg 5. Other leg?', 'Leg:', key='12', note='Any equivalent form.'),
              sa('A cone has radius 6 and slant height 10. Height?', 'Height:', key='8', note='Any equivalent form.'),
              mc('Radius, height, and slant height of a cone form a', ['right triangle', 'square', 'circle', 'equilateral triangle'], note='Height ⊥ base.'),
              tf('The slant height is longer than the height.', key=True, note='Hypotenuse.'),
              tf('The slant height can be used as the height in V = ⅓πr²h.', key=False, note='Use the perpendicular height.'),
          ], align='exact',
            why=why('the student uses the slant height.', 'volume uses the perpendicular height.', 'finds heights with the Pythagorean Theorem.')),
          B('Evaluate a formula and round', '7.EE.B.3', [
              sa('Evaluate ⅓ · 36 · 8.', 'Value:', key='96', note='Any equivalent form.'),
              sa('Round 90π to the nearest tenth.', 'Answer:', key='282.7', note='Rounding to 0.1 required.'),
              mc('96π ≈', ['301.6', '301.5', '96.3', '3,016'], note='Use the π key.'),
              tf('Using 3.14 for π may change the last digit of a rounded answer.', key=True, note='Use the π key.'),
              tf('⅓ · 100 · 12 = 1,200', key=False, note='400.'),
          ], align='supporting',
            why=why('the student makes arithmetic or rounding errors.', 'answers need exact and rounded forms.', 'evaluates and rounds.')),
          B('Which solid uses ⅓?', 'HSG-GMD.A.1', [
              tf('Pyramids and cones use V = ⅓Bh.', key=True, note='Pointed solids.'),
              sa('Which has the formula V = Bh: a cone or a cylinder?', 'Answer:', key='Cylinder', note='Any equivalent answer.'),
              mc('V = ⅓πr²h is the volume of a', ['cone', 'cylinder', 'sphere', 'prism'], note='Formula.'),
              sa('Why does a cone have ⅓ of the matching cylinder\'s volume?', 'Answer:', key='Three cones fill the cylinder (the informal argument).', note='Any reasonable answer.'),
              tf('A pyramid uses V = Bh.', key=False, note='⅓Bh.'),
          ], align='supporting',
            why=why('the student mixes the formulas.', 'choosing the right formula is the first step.', 'matches solids and formulas.')),
      ],
      f1=B('Composite and hollow solids', 'HSG-GMD.A.3', [
          sa('A silo is a cylinder (radius 4 m, height 10 m) topped by a cone (radius 4 m, height 3 m). Find its exact volume.', 'Volume:', key='176π m³', note='Form required: exact value. 160π + 16π.'),
          sa('A pipe is a cylinder of length 20 cm with outer radius 5 cm and inner radius 4 cm. Find the volume of the material, exact.', 'Volume:', key='180π cm³', note='Form required: exact value. π(25 - 16)(20).'),
          tf('The volume of a composite solid is the sum of the volumes of its non-overlapping parts.', key=True, note='Additivity.'),
          mc('A cylinder (V = 300) has a cone with the same base and height carved out. Remaining volume?', ['200', '100', '300', '0'], note='300 - 100.'),
          sa('A pencil tip is a cone of radius 0.4 cm and height 1.5 cm on a cylinder of radius 0.4 cm and length 15 cm. Find the total volume to the nearest tenth.', 'Volume:',
             key='%s cm³' % d1(PI * 0.16 * 15 + PI * 0.16 * 1.5 / 3), note='Rounding to 0.1 required. 2.4π + 0.08π.'),
      ], prog='same-course deepening', demand='Combine and subtract volumes for composite and hollow solids.'),
      f2=B('Mass from volume and density', 'HSG-MG.A.2', [
          sa('A steel cylinder has radius 2 cm and height 5 cm. Steel has density 7.85 g/cm³. Find the mass to the nearest gram.', 'Mass:', key='%d g' % round(PI * 20 * 7.85), note='Rounding to the nearest gram required.'),
          sa('A cone of ice cream (radius 3 cm, height 10 cm) has density 0.55 g/cm³. Find the mass to the nearest gram.', 'Mass:', key='%d g' % round(PI * 30 * 0.55), note='Rounding to the nearest gram required. 30π cm³.'),
          tf('Mass = volume ÷ density.', key=False, note='Mass = density × volume.'),
          mc('A pyramid of volume 400 cm³ is made of material with density 2 g/cm³. Mass?', ['800 g', '200 g', '402 g', '1,600 g'], note='2 × 400.'),
          sa('A gold cube has volume 8 cm³ and mass 154.4 g. Find the density.', 'Density:', key='19.3 g/cm³', note='Any equivalent form.'),
      ], prog='cross-standard extension', demand='Use the computed volume as one step in a density model.',
        builds='Builds on FORWARD 1: computed volumes (including composites) feed a density calculation.')),

    # ------------------------------------------------------------------ 79. GMD.A.3 spheres and composites
    S('HSG-GMD.A.3', 'Use the volume formula for spheres, including composite solids',
      target='Use V = 4/3 πr³ for spheres and hemispheres, alone and combined with cylinders and cones', strand='core', covers=['GMD3-sphere'],
      main=[
          sa('Find the volume of a sphere with radius 6 cm, exact and to the nearest tenth.', 'Volume:', fig=sphere('6 cm', 'Sphere with radius 6 cm.'), key=pv(288, 'cm³'),
             note='Form required: both, with units. 4/3 π · 216.'),
          sa('Find the volume of a ball with diameter 10 in., exact and to the nearest tenth.', 'Volume:', key=pv(500, 'in³', 3), note='Form required: both, with units. r = 5.'),
          sa('Find the volume of a hemisphere with radius 3 m, exact and to the nearest tenth.', 'Volume:', fig=sphere('3 m', 'Hemisphere (half of a sphere) with radius 3 m on a flat circular base.', hemi=True),
             key=pv(18, 'm³'), note='Form required: both, with units. ½ · 4/3 π · 27.'),
          sa('A capsule is a cylinder of radius 3 cm and length 10 cm with a hemisphere on each end. Find its volume, exact and to the nearest tenth.', 'Volume:', key=pv(126, 'cm³'),
             note='Form required: both, with units. 90π + 36π (two hemispheres make one sphere).'),
          mc('An ice cream cone (radius 2, height 9) is topped by a hemisphere of radius 2. The total exact volume is', ['52π/3', '28π', '12π', '44π/3'],
             note='12π + 16π/3.'),
      ],
      back=[
          B('Cubes of numbers', '6.EE.A.1', [
              sa('6³ = ', 'Answer:', key='216', note='Any equivalent form.'),
              sa('5³ = ', 'Answer:', key='125', note='Any equivalent form.'),
              mc('3³ = ', ['27', '9', '6', '81'], note='3 · 3 · 3.'),
              tf('2³ = 8', key=True, note='Cube.'),
              tf('4³ = 12', key=False, note='64.'),
          ], align='exact',
            why=why('the student squares or triples instead of cubing.', 'the sphere formula uses r³.', 'computes cubes.')),
          B('Radius from diameter', '7.G.B.4', [
              sa('A ball has diameter 10. Radius?', 'Radius:', key='5', note='Any equivalent form.'),
              tf('Using the diameter in 4/3 πr³ makes the answer 8 times too large.', key=True, note='2³.'),
              mc('A sphere with diameter 12 has r³ =', ['216', '1,728', '144', '36'], note='6³.'),
              sa('A sphere has radius 2.5. Diameter?', 'Diameter:', key='5', note='Any equivalent form.'),
              tf('The radius of a sphere is twice its diameter.', key=False, note='Half.'),
          ], align='exact',
            why=why('the student uses the diameter.', 'the formula needs the radius.', 'converts diameter to radius.')),
          B('Multiply fractions by numbers', '7.NS.A.2', [
              sa('4/3 · 216 = ', 'Answer:', key='288', note='Any equivalent form.'),
              sa('½ · 4/3 · 27 = ', 'Answer:', key='18', note='Any equivalent form.'),
              mc('4/3 · 125 =', ['500/3', '375/4', '125/3', '500'], note='Numerators.'),
              tf('4/3 · 27 = 36', key=True, note='27 ÷ 3 × 4.'),
              tf('4/3 · 6 = 24', key=False, note='8.'),
          ], align='supporting',
            why=why('the student makes fraction errors.', 'the coefficient is 4/3.', 'multiplies with fractions.')),
          B('Cylinder and cone volumes', 'HSG-GMD.A.3', [
              sa('Cylinder radius 3, length 10: exact volume?', 'Volume:', key='90π', note='Form required: exact value.'),
              sa('Cone radius 2, height 9: exact volume?', 'Volume:', key='12π', note='Form required: exact value.'),
              mc('A cylinder and a cone with radius 3 and height 4 have volumes', ['36π and 12π', '12π and 36π', '36π and 36π', '12π and 4π'], note='⅓.'),
              tf('Two hemispheres of radius r make one sphere of radius r.', key=True, note='Halves.'),
              tf('A composite volume is the product of the parts.', key=False, note='Sum.'),
          ], align='exact',
            why=why('the student cannot find the other parts of a composite solid.', 'composites add cylinders and cones.', 'finds those volumes.')),
      ],
      f1=B('Scaling spheres', 'HSG-GMD.A.3', [
          sa('The radius of a sphere is doubled. By what factor is the volume multiplied?', 'Factor:', key='8', note='Any equivalent form. 2³.'),
          sa('A sphere fits exactly inside a cube with side 6. Find the exact volume of the space in the cube outside the sphere.', 'Volume:', key='216 - 36π', note='Form required: exact value. r = 3.'),
          tf('A sphere of radius 3 has 9 times the volume of a sphere of radius 1.', key=False, note='Volume scales by 3³ = 27.'),
          mc('A balloon\'s radius grows from 10 cm to 15 cm. Its volume is multiplied by', ['3.375', '1.5', '2.25', '5'], note='1.5³.'),
          sa('A sphere and a cylinder have the same radius r, and the cylinder\'s height is 2r. What fraction of the cylinder\'s volume is the sphere\'s?', 'Fraction:', key='⅔',
             note='Any equivalent form. (4/3 πr³)/(2πr³).'),
      ], prog='same-course deepening', demand='Reason about how sphere volume scales and compare it with related solids.'),
      f2=B('Model real objects as spheres', 'HSG-MG.A.1', [
          sa('Model Earth as a sphere with radius 6,371 km. Estimate its volume in cubic kilometers, in scientific notation to 3 significant figures.', 'Volume:',
             key='1.08 × 10¹² km³', note='Rounding to 3 significant figures required.'),
          sa('A basketball has circumference 75 cm. Model it as a sphere and find its volume to the nearest 100 cm³.', 'Volume:',
             key='%d cm³' % (round(4 / 3 * PI * (75 / (2 * PI)) ** 3, -2)), note='Rounding to the nearest 100 required. r = 75/(2π) ≈ 11.94 cm.'),
          tf('Modeling an orange as a sphere ignores its small bumps.', key=True, note='Modeling assumption.'),
          mc('A scoop of ice cream is modeled as a sphere of radius 3 cm. Its volume is about', ['113 cm³', '36 cm³', '28 cm³', '339 cm³'], note='36π.'),
          sa('Give one reason a sphere is a good model for a ball bearing and one limitation of the model for a pumpkin.', 'Answer:',
             key='A ball bearing is nearly perfectly round; a pumpkin has ridges, a flattened shape, and a stem, so the model is only approximate.', note='Any reasonable answer.'),
      ], prog='cross-standard extension', demand='Choose a sphere model for a real object, compute, and judge the model.',
        builds='Builds on FORWARD 1: scale reasoning helps judge large and small real objects.')),

    # ------------------------------------------------------------------ 80. GMD.A.3 solve for a dimension
    S('HSG-GMD.A.3', 'Solve for an unknown dimension from a volume',
      target='Use the volume formulas for cylinders, pyramids, cones, and spheres to find an unknown radius, height, or edge', strand='core', covers=['GMD3-solve'],
      main=[
          sa('A cylinder has volume 360π cm³ and radius 6 cm. Find its height.', 'Height:', key='10 cm', note='Any equivalent form, with units. 36πh = 360π.'),
          sa('A cone has volume 96π in³ and height 8 in. Find its radius.', 'Radius:', key='6 in.', note='Any equivalent form, with units. ⅓πr² · 8 = 96π → r² = 36.'),
          sa('A sphere has volume 36π m³. Find its radius.', 'Radius:', key='3 m', note='Any equivalent form, with units. r³ = 27.'),
          sa('A square pyramid has volume 256 ft³ and height 12 ft. Find the side of its base.', 'Side:', key='8 ft', note='Any equivalent form, with units. ⅓s² · 12 = 256 → s² = 64.'),
          mc('A cylinder holds 500 cm³ and has height 10 cm. Its radius is closest to', ['4.0 cm', '15.9 cm', '7.1 cm', '2.0 cm'], note='r = √(50/π) ≈ 3.99.'),
      ],
      back=[
          B('Solve a one-step equation with a coefficient', 'HSA-REI.B.3', [
              sa('Solve 36πh = 360π.', 'h =', key='10', note='Any equivalent form.'),
              sa('Solve ⅓x = 12.', 'x =', key='36', note='Any equivalent form.'),
              mc('Solve 4x = 108.', ['27', '104', '432', '25'], note='Divide by 4.'),
              tf('To solve 36πh = 360π, dividing both sides by π is allowed.', key=True, note='π ≠ 0.'),
              tf('To solve ⅓x = 12, divide by 3.', key=False, note='Multiply by 3.'),
          ], align='exact',
            why=why('the student cannot isolate the unknown.', 'the formula becomes an equation.', 'solves one-step equations.')),
          B('Square roots and cube roots', '8.EE.A.2', [
              sa('Solve r² = 36 for r > 0.', 'r =', key='6', note='Any equivalent form.'),
              sa('Solve r³ = 27.', 'r =', key='3', note='Any equivalent form.'),
              mc('∛125 =', ['5', '25', '41.7', '15'], note='5³ = 125.'),
              tf('√64 = 8', key=True, note='8² = 64.'),
              tf('If r³ = 8, then r = 4.', key=False, note='2.'),
          ], align='exact',
            why=why('the student cannot undo the square or cube.', 'radius problems end with a root.', 'takes square and cube roots.')),
          B('Rearrange a formula', 'HSA-CED.A.4', [
              sa('Solve V = πr²h for h.', 'h =', key='V/(πr²)', note='Any equivalent form.'),
              sa('Solve V = ⅓Bh for B.', 'B =', key='3V/h', note='Any equivalent form.'),
              mc('V = 4/3 πr³ solved for r³ is', ['3V/(4π)', '4V/(3π)', 'V/(4π)', '3πV/4'], note='Multiply by 3/(4π).'),
              tf('Solving V = πr²h for r needs a square root.', key=True, note='r = √(V/(πh)).'),
              tf('Solving V = Bh for h gives h = VB.', key=False, note='V/B.'),
          ], align='exact',
            why=why('the student cannot rearrange a formula.', 'it organizes the solution.', 'solves formulas for a variable.')),
      ],
      f1=B('Find dimensions to meet a target volume', 'HSG-GMD.A.3', [
          sa('A drink can must hold at least 355 cm³ and have radius 3.3 cm. What is the smallest height, in tenths of a centimeter, that meets the requirement?', 'Height:',
             key='%.1f cm' % (math.ceil(355 / (PI * 3.3 ** 2) * 10) / 10),
             note='Form required: a height in tenths that meets the constraint (round UP). h = 355/(π · 3.3²) = %.3f.' % (355 / (PI * 3.3 ** 2))),
          sa('A spherical tank must hold at least 1,000 m³. What is the smallest radius, in tenths of a meter, that meets the requirement?', 'Radius:',
             key='%.1f m' % (math.ceil((3000 / (4 * PI)) ** (1 / 3) * 10) / 10),
             note='Form required: a radius in tenths that meets the constraint (round UP). r = ∛(750/π) = %.4f; 6.2 m would hold only about %.1f m³.' % ((750 / PI) ** (1 / 3), 4 / 3 * PI * 6.2 ** 3)),
          tf('To double the volume of a cylinder while keeping its radius, double its height.', key=True, note='Linear in h.'),
          mc('A cone has the same volume as a cylinder of equal radius. The cone\'s height is', ['3 times the cylinder\'s', 'equal to the cylinder\'s', '⅓ of the cylinder\'s', '9 times the cylinder\'s'],
             note='⅓πr²h₁ = πr²h₂.'),
          sa('A cube has the same volume as a sphere of radius 3. Find the cube\'s edge to the nearest tenth.', 'Edge:', key=d1((36 * PI) ** (1 / 3)), note='Rounding to 0.1 required. ∛(36π).'),
      ], prog='same-course deepening', demand='Solve for dimensions in applied settings with rounding and comparisons between solids.'),
      f2=B('Design a container that meets constraints', 'HSG-MG.A.3', [
          sa('A cylindrical vase must hold 2,000 cm³ and be 20 cm tall. Its radius must be at least 5 cm to fit a bouquet. Does the design work? Explain.', 'Answer:',
             key='Yes: r = √(2000/(20π)) ≈ 5.6 cm, which is at least 5 cm.', note='Form required: the conclusion with the computed radius.'),
          sa('A conical paper cup must hold at least 150 cm³ and have radius 3.5 cm. What is the smallest height, in tenths of a centimeter, that meets the requirement?', 'Height:',
             key='%.1f cm' % (math.ceil(450 / (PI * 3.5 ** 2) * 10) / 10),
             note='Form required: a height in tenths that meets the constraint (round UP). h = 450/(π · 3.5²) = %.3f.' % (450 / (PI * 3.5 ** 2))),
          tf('A container\'s volume requirement fixes each of its dimensions.', key=False, note='It fixes only a relationship: many (r, h) pairs give the same volume.'),
          mc('A cylinder must hold 100π cm³. Which (r, h) works?', ['(5, 4)', '(4, 5)', '(10, 10)', '(5, 20)'], note='25 · 4 = 100.'),
          sa('Give two different cylinders (radius and height) that each hold 64π cm³.', 'Answer:', key='For example r = 4, h = 4 and r = 2, h = 16.', note='Any two (r, h) pairs with r²h = 64.'),
      ], prog='cross-standard extension', demand='Use the solved formulas to check a design against several constraints.',
        builds='Builds on FORWARD 1: solving for dimensions becomes a step in checking a design.')),
]

CUBE_DIAG = cube('Cube with a shaded cutting plane through the front-bottom edge and the back-top edge, slicing the cube diagonally.',
                 extra=[('poly', [(0, 0), (_s, 0), (_s + 0.9, _s + 0.7), (0.9, _s + 0.7)], {'fill': True})])
CUBE_CORNER = cube('Cube with a shaded triangular slice cutting off the top-front-right corner; the slice passes through points on the three edges that meet at that corner.',
                   extra=[('poly', [(_s, _s - 0.9), (_s - 0.9, _s), (_s + 0.45, _s + 0.35)], {'fill': True})])


def spin(shape, axis, desc, h_px=200):
    it = [('poly', shape, {'fill': True}), ('line', axis[0], axis[1], {'dash': True})]
    return gd({}, it, h=h_px, desc=desc)


ROT_RECT = spin([(0, 0), (1.2, 0), (1.2, 2.4), (0, 2.4)], ((0, -0.6), (0, 3.0)), 'Shaded rectangle with its left side on a dashed vertical axis of rotation.')
ROT_TRI = spin([(0, 0), (1.4, 0), (0, 2.4)], ((0, -0.6), (0, 3.0)), 'Shaded right triangle with one leg (the vertical leg) on a dashed vertical axis of rotation.')
ROT_SEMI = gd({}, [('sector', (0, 0), 1.4, -90, 90), ('line', (0, -2.0), (0, 2.0), {'dash': True})], h=200,
              desc='Shaded semicircle whose diameter lies on a dashed vertical axis of rotation.')
ROT_GAP = spin([(0.8, 0), (1.8, 0), (1.8, 2.4), (0.8, 2.4)], ((0, -0.6), (0, 3.0)),
               'Shaded rectangle standing beside a dashed vertical axis of rotation, with a gap between the axis and the rectangle\'s left side.')

SETS += [
    # ------------------------------------------------------------------ 81. GMD.B.4 cross-sections
    S('HSG-GMD.B.4', 'Identify cross-sections of three-dimensional objects',
      target='Identify the shapes of two-dimensional cross-sections of cylinders, cones, spheres, prisms, and pyramids for planes in different positions', strand='core', covers=['GMD4-cross'],
      main=[
          sa('A plane cuts the cube as shown. Name the shape of the cross-section.', 'Shape:', fig=CUBE_DIAG, key='A rectangle (not a square)',
             note='Any equivalent answer. Two sides are cube edges (s) and two are face diagonals (s√2).'),
          sa('A plane cuts off one corner of the cube as shown. Name the shape of the cross-section.', 'Shape:', fig=CUBE_CORNER, key='A triangle',
             note='Any equivalent answer. (Equilateral if the three cut points are equally far from the corner.)'),
          mc('A right circular cone is cut by a vertical plane through its apex. The cross-section is', ['a triangle (isosceles)', 'a circle', 'an ellipse', 'a rectangle'], note='Two slant edges and a diameter.'),
          sa('Name the cross-section of a cylinder cut by a plane (a) parallel to its base, (b) perpendicular to its base through its axis, and (c) slanted, cutting the curved side only.',
             'Answer:', key='(a) circle (b) rectangle (c) ellipse', note='Form required: all three.'),
          sa('A sphere of radius 10 is cut by a plane 6 units from its center. Name the shape of the cross-section and find its radius.', 'Answer:', key='A circle of radius 8',
             note='Form required: the shape and the radius. √(10² - 6²) = 8.'),
      ],
      back=[
          B('Cross-sections of right rectangular prisms and pyramids', '7.G.A.3', [
              sa('A rectangular prism is cut parallel to its base. Shape?', 'Shape:', key='A rectangle congruent to the base', note='Any equivalent answer.'),
              sa('A square pyramid is cut parallel to its base. Shape?', 'Shape:', key='A smaller square', note='Any equivalent answer.'),
              mc('A square pyramid cut vertically through its apex and two opposite base edges\' midpoints gives a', ['triangle', 'square', 'trapezoid', 'circle'], note='Through the apex.'),
              tf('A vertical cut of a rectangular prism parallel to a side face gives a rectangle.', key=True, note='Congruent to the face.'),
              tf('A cut of a cube parallel to a face can be a triangle.', key=False, note='It is a square.'),
          ], align='exact',
            why=why('the student cannot picture basic slices.', 'harder solids build on them.', 'names cross-sections of prisms and pyramids.')),
          B('Properties of polygons', '5.G.B.4', [
              sa('A quadrilateral with four right angles and unequal adjacent sides is a', 'Answer:', key='rectangle', note='Any equivalent answer.'),
              tf('Every square is a rectangle.', key=True, note='Hierarchy.'),
              mc('A polygon with six sides is a', ['hexagon', 'pentagon', 'octagon', 'heptagon'], note='Name.'),
              sa('A triangle with two equal sides is', 'Answer:', key='isosceles', note='Any equivalent answer.'),
              tf('A trapezoid has no parallel sides.', key=False, note='At least one pair.'),
          ], align='supporting',
            why=why('the student cannot name the shape found.', 'answers are polygon names.', 'classifies polygons.')),
          B('Parts of solids', '6.G.A.4', [
              sa('How many faces does a cube have?', 'Faces:', key='6', note='Any equivalent form.'),
              sa('What is the shape of the base of a cone?', 'Answer:', key='A circle', note='Any equivalent answer.'),
              mc('How many edges meet at each vertex of a cube?', ['3', '4', '2', '6'], note='Corner.'),
              tf('A cylinder has two congruent circular bases.', key=True, note='Definition.'),
              tf('A sphere has one edge.', key=False, note='No edges.'),
          ], align='supporting',
            why=why('the student does not know the parts being cut.', 'cut points lie on edges and faces.', 'names parts of solids.')),
      ],
      f1=B('Areas of cross-sections', 'HSG-GMD.B.4', [
          sa('A cube has edge 4. Find the area of the diagonal cross-section through two opposite edges.', 'Area:', key='16√2', note='Form required: exact value. 4 × 4√2.'),
          sa('A cone has radius 6 and height 12. Find the area of the cross-section parallel to the base at height 4 (measured up from the base).', 'Area:', key='16π',
             note='Form required: exact value. Radius at that level = 6 · (12 - 4)/12 = 4.'),
          tf('A sphere of radius 5 cut 3 units from its center gives a circle of radius 4.', key=True, note='3-4-5.'),
          mc('A cube can have a cross-section that is a regular', ['hexagon', 'octagon', 'pentagon', 'heptagon'], note='Plane through the midpoints of six edges.'),
          sa('A square pyramid has base side 10 and height 15. Find the exact area of the cross-section parallel to the base 5 units below the apex.', 'Area:', key='100/9 (about 11.1)',
             note='Form required: exact value or rounding to 0.1. Side 10 · 5/15 = 10/3.'),
      ], prog='same-course deepening', demand='Compute the areas of cross-sections, not only name their shapes.'),
      f2=B('Use cross-section areas to compare volumes (Cavalieri)', 'HSG-GMD.A.2', [
          sa('Two solids have height 10 and every horizontal cross-section of each has area 7. Compare their volumes.', 'Answer:', key='Equal: 70 each', note='Form required: the comparison with the value.'),
          sa('A hemisphere has radius 5. Find the area of its cross-section 3 units above the base.', 'Area:', key='16π', note='Form required: exact value. Radius 4.'),
          tf('Cavalieri\'s principle can compare two solids of different heights.', key=False, note='The solids must have equal heights.'),
          mc('A hemisphere of radius r rests on its flat base. At height y above the base plane (0 ≤ y ≤ r), its horizontal cross-section has area', ['π(r² - y²)', 'πr²', 'πy²', 'π(r - y)²'], note='Pythagorean Theorem.'),
          sa('Explain why cross-section areas are useful for finding volumes.', 'Answer:', key='Volume can be built from thin slices; equal slice areas at each level give equal volumes.', note='Any reasonable answer.'),
      ], prog='cross-standard extension', demand='Use cross-section areas in a Cavalieri comparison (advanced strand).',
        builds='Builds on FORWARD 1: computed cross-section areas become the input to Cavalieri\'s principle.')),

    # ------------------------------------------------------------------ 82. GMD.B.4 rotations
    S('HSG-GMD.B.4', 'Identify three-dimensional objects generated by rotations of two-dimensional objects',
      target='Identify the solid generated when a two-dimensional figure is rotated about a line', strand='core', covers=['GMD4-rotate'],
      main=[
          sa('The rectangle is rotated 360° about the dashed line. Name the solid formed.', 'Solid:', fig=ROT_RECT, key='A cylinder', note='Any equivalent answer.'),
          sa('The right triangle is rotated 360° about the dashed line. Name the solid formed.', 'Solid:', fig=ROT_TRI, key='A cone', note='Any equivalent answer.'),
          sa('The semicircle is rotated 360° about the dashed line. Name the solid formed.', 'Solid:', fig=ROT_SEMI, key='A sphere', note='Any equivalent answer.'),
          sa('The rectangle is rotated 360° about the dashed line, which does not touch it. Describe the solid formed.', 'Solid:', fig=ROT_GAP,
             key='A hollow cylinder (a cylinder with a cylindrical hole through the middle, like a pipe)', note='Any equivalent description.'),
          mc('A right triangle is rotated about its hypotenuse. The solid formed is', ['two cones joined at their bases', 'one cone', 'a cylinder', 'a sphere'], note='Each leg sweeps a cone.'),
      ],
      back=[
          B('Rotation of a point about a center', 'HSG-CO.A.4', [
              tf('In a plane, rotating a point P (P different from the center O) 360° about O traces a circle with center O and radius OP.', key=True, note='Every image is OP from O.'),
              sa('A point 3 cm from an axis is rotated about the axis. What does it trace?', 'Answer:', key='A circle of radius 3 cm', note='Any equivalent answer.'),
              mc('A point ON the axis of rotation', ['stays fixed', 'traces a circle', 'traces a line', 'disappears'], note='Distance 0.'),
              sa('A segment parallel to the axis, 2 units away, is rotated about it. What surface does it trace?', 'Answer:', key='The curved side of a cylinder', note='Any equivalent answer.'),
              tf('Points farther from the axis trace smaller circles.', key=False, note='Larger circles.'),
          ], align='exact',
            why=why('the student cannot picture what each point traces.', 'the solid is made of those circles.', 'describes traced paths.')),
          B('Cross-sections perpendicular to the axis', 'HSG-GMD.B.4', [
              tf('A solid of rotation cut perpendicular to its axis has a circular cross-section (or a ring).', key=True, note='Every point traces a circle.'),
              sa('A cone is cut perpendicular to its axis. Shape?', 'Shape:', key='A circle', note='Any equivalent answer.'),
              mc('A pipe cut perpendicular to its axis gives a', ['ring (annulus)', 'circle', 'rectangle', 'triangle'], note='Hole.'),
              sa('A sphere is cut through its center. Shape?', 'Shape:', key='A circle (a great circle)', note='Any equivalent answer.'),
              tf('A cylinder cut perpendicular to its axis gives a rectangle.', key=False, note='A circle.'),
          ], align='supporting',
            why=why('the student does not connect rotation with circular slices.', 'it checks the solid named.', 'names those cross-sections.')),
          B('Names of solids', '6.G.A.4', [
              sa('Name the solid with two parallel circular bases and a curved side.', 'Solid:', key='Cylinder', note='Any equivalent answer.'),
              sa('Name the solid with one circular base and an apex.', 'Solid:', key='Cone', note='Any equivalent answer.'),
              mc('All points equidistant from a center in space form a', ['sphere', 'circle', 'cylinder', 'cone'], note='Definition.'),
              tf('A cone has one flat face.', key=True, note='Its base.'),
              tf('A sphere has a flat base.', key=False, note='It has none.'),
          ], align='supporting',
            why=why('the student knows the shape but not its name.', 'answers name solids.', 'names solids.')),
      ],
      f1=B('Volumes of solids of rotation', 'HSG-GMD.B.4', [
          sa('A 3-by-5 rectangle is rotated about its 5-unit side. Find the exact volume of the solid.', 'Volume:', key='45π', note='Form required: exact value. r = 3, h = 5.'),
          sa('A 3-by-5 rectangle is rotated about its 3-unit side. Find the exact volume of the solid.', 'Volume:', key='75π', note='Form required: exact value. r = 5, h = 3.'),
          tf('Rotating one rectangle about two different sides can give solids with different volumes.', key=True, note='A 3-by-5 rectangle gives 45π about its 5-unit side and 75π about its 3-unit side.'),
          mc('A right triangle with legs 3 (on the axis) and 4 is rotated about the leg of length 3. Volume?', ['16π', '12π', '48π', '9π'], note='r = 4, h = 3: ⅓π · 16 · 3.'),
          sa('A semicircle of radius 3 is rotated about its diameter. Find the exact volume.', 'Volume:', key='36π', note='Form required: exact value.'),
      ], prog='same-course deepening', demand='Find the dimensions and volume of the solid generated.'),
      f2=B('Design an object as a solid of rotation', 'HSG-MG.A.3', [
          sa('A lathe turns a 2 cm by 10 cm rectangle about its 10 cm side to make a wooden dowel. Find the exact volume of wood.', 'Volume:', key='40π cm³', note='Form required: exact value.'),
          sa('A designer wants a cone-shaped lampshade by rotating a right triangle about a 30 cm leg. What other leg length gives a base of diameter 40 cm?', 'Leg:', key='20 cm', note='Any equivalent form.'),
          tf('A hemispherical bowl can be modeled by rotating a right triangle about one of its legs.', key=False, note='That gives a cone; rotate a quarter-circle.'),
          mc('To make a ring-shaped washer by rotation, rotate a rectangle about a line in the rectangle\'s plane, parallel to one of its sides, that', ['lies outside the rectangle', 'contains one side', 'passes through the rectangle\'s center', 'cuts through the rectangle off-center'],
             note='The gap between the axis and the rectangle becomes the hole.'),
          sa('A vase is made by rotating a rectangle 6 cm wide and 20 cm tall about a line in the rectangle\'s plane, parallel to its long side and 2 cm from it, outside the rectangle. Find the exact volume of material.', 'Volume:',
             key='1,200π cm³', note='Form required: exact value. Outer radius 8, inner radius 2: π(64 - 4)(20).'),
      ], prog='cross-standard extension', demand='Use rotations to design objects with given dimensions.',
        builds='Builds on FORWARD 1: volumes of rotated figures are used in design.')),
]
