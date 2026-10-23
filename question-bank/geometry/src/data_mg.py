"""G-MG: modeling with geometry (sets 83-87)."""
import math

from qb import S, B, sa, mc, tf, work
from common import gd, NTS, proof

PI = math.pi


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def d2(x):
    return '%.2f' % round(x + 1e-12, 2)


TREE_V = (2.2 ** 2) / (4 * PI) * 6
BOTTLE = PI * 3.8 ** 2 * 17

SETS = [
    # ------------------------------------------------------------------ 83. MG.A.1 model objects
    S('HSG-MG.A.1', 'Model objects with geometric shapes',
      target='Use geometric shapes, their measures, and their properties to describe real objects, compute with the model, and judge its assumptions', strand='core', covers=['MG1-model'],
      main=[
          work('A tree trunk is about 6 m tall and has circumference 2.2 m. Model it as a cylinder and estimate its volume to the nearest tenth of a cubic meter.', 'Volume:',
               method='Find the radius from the circumference, then use V = πr²h.', key='About %s m³' % d1(TREE_V), note='Rounding to 0.1 required. r = 2.2/(2π) ≈ 0.35 m.'),
          sa('A pile of sand is shaped like a cone with base diameter 8 m and height 3 m. Estimate its volume to the nearest tenth of a cubic meter.', 'Volume:', key='%s m³' % d1(16 * PI),
             note='Rounding to 0.1 required. 16π.'),
          mc('Which shape is the best model for a soup can?', ['Cylinder', 'Cone', 'Sphere', 'Square pyramid'], note='Two circular bases.'),
          sa('A pool is modeled as a rectangular prism 25 m long, 10 m wide, and 1.8 m deep. How many liters of water does it hold? (1 m³ = 1,000 L)', 'Answer:', key='450,000 L',
             note='Any equivalent form. 450 m³.'),
          sa('A pine tree is modeled as a cone. Name one measurement you would take and one way the model differs from the real tree.', 'Answer:',
             key='For example: height and the width at the bottom of the branches; the real tree has gaps, a trunk, and an uneven outline.', note='Any reasonable measurement and limitation.'),
      ],
      back=[
          B('Volume formulas', 'HSG-GMD.A.3', [
              sa('Exact volume of a cylinder with r = 2 and h = 5?', 'Volume:', key='20π', note='Form required: exact value.'),
              sa('Exact volume of a cone with r = 3 and h = 4?', 'Volume:', key='12π', note='Form required: exact value.'),
              mc('Volume of a 2 × 3 × 4 prism?', ['24', '9', '26', '52'], note='Product.'),
              tf('V = ⅓πr²h is the cone formula.', key=True, note='Formula.'),
              tf('A sphere\'s volume is πr²h.', key=False, note='4/3 πr³.'),
          ], align='exact',
            why=why('the student cannot compute with the chosen shape.', 'the model is used through its formula.', 'uses volume formulas.')),
          B('Radius from a circumference', '7.G.B.4', [
              sa('A circle has circumference 10π. Radius?', 'Radius:', key='5', note='Any equivalent form.'),
              sa('A circle has circumference 2.2 m. Radius to the nearest hundredth?', 'Radius:', key='%s m' % d2(2.2 / (2 * PI)), note='Rounding to 0.01 required.'),
              mc('r = ', ['C/(2π)', '2πC', 'C/π', 'πC'], note='C = 2πr.'),
              tf('A tape measure around a trunk gives its circumference.', key=True, note='Distance around.'),
              tf('The radius is C/2.', key=False, note='C/(2π).'),
          ], align='exact',
            why=why('the student cannot get the radius from a measurable distance.', 'real objects are often measured around.', 'finds radius from circumference.')),
          B('Convert cubic units', '6.RP.A.3.d', [
              sa('How many liters are in 2 m³?', 'Answer:', key='2,000 L', note='Any equivalent form.'),
              sa('How many cubic centimeters are in 1 L?', 'Answer:', key='1,000 cm³', note='Any equivalent form.'),
              mc('450 m³ = ___ L', ['450,000', '4,500', '45,000', '0.45'], note='× 1,000.'),
              tf('1 mL = 1 cm³', key=True, note='Definition.'),
              tf('1 m³ = 100 L', key=False, note='1,000 L.'),
          ], align='supporting',
            why=why('the student cannot express the answer in the needed unit.', 'models answer real questions in real units.', 'converts units.')),
      ],
      f1=B('Judge a model against a measurement', 'HSG-MG.A.1', [
          sa('A water bottle is modeled as a cylinder with radius 3.8 cm and height 17 cm. The label says 750 mL. Find the model volume to the nearest mL and the percent error.', 'Answer:',
             key='About %d mL; about %s%% too high' % (round(BOTTLE), d1((BOTTLE - 750) / 750 * 100)), note='Form required: both (rounding to 1 mL and 0.1%). Percent error = (model - actual)/actual.'),
          sa('A silo is modeled as a cylinder (r = 3 m, h = 12 m) with a hemisphere on top. Find the exact volume.', 'Volume:', key='126π m³', note='Form required: exact value. 108π + 18π.'),
          tf('A model that overestimates by 3% may still be useful for planning.', key=True, note='Judgment.'),
          mc('A football (pointed ends) is best modeled by', ['two cones joined at their bases', 'a sphere', 'a cylinder', 'a cube'], note='Pointed ends; other answers with reasons may be discussed.'),
          sa('Why might a cylinder model overestimate the volume of a bottle?', 'Answer:', key='The real bottle narrows at the neck and has thick walls, so it holds less than the full cylinder.', note='Any reasonable answer.'),
      ], prog='same-course deepening', demand='Compare the model\'s result with a real measurement and refine the model.'),
      f2=B('Use the model to estimate mass with density', 'HSG-MG.A.2', [
          sa('A tree trunk modeled as a cylinder has volume about %s m³. The wood has density 600 kg/m³. Estimate the trunk\'s mass to the nearest 10 kg.' % d1(TREE_V), 'Mass:', key='About 1,380 kg',
             note='Rounding to the nearest 10 kg required. 2.3 × 600 = 1,380 (using the unrounded volume %.3f m³ gives %d kg, also accepted).' % (TREE_V, round(TREE_V * 600, -1))),
          sa('A sand pile modeled as a cone has volume 16π m³. The sand has density 1,600 kg/m³. Estimate its mass in metric tons (1 t = 1,000 kg), to the nearest ton.', 'Mass:', key='%d t' % round(16 * PI * 1.6), note='Rounding to the nearest ton required.'),
          tf('A more accurate volume model gives a more accurate mass estimate.', key=True, note='Mass = density × volume.'),
          mc('A pool holds 450 m³ of water (1,000 kg/m³). Mass?', ['450,000 kg', '450 kg', '4,500 kg', '45,000 kg'], note='Product.'),
          sa('Explain how a geometric model and a density work together to estimate the mass of a log.', 'Answer:', key='The model gives the volume; mass = density × volume.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Combine a geometric model with a density to estimate a new quantity.',
        builds='Builds on FORWARD 1: a judged and refined model is used to estimate mass.')),

    # ------------------------------------------------------------------ 84. MG.A.2 area density
    S('HSG-MG.A.2', 'Apply density based on area',
      target='Compute and use densities based on area (people per square mile, trees per square kilometer) in modeling situations', strand='core', covers=['MG2-area'],
      main=[
          sa('A city has 840,000 people and an area of 120 square miles. Find its population density.', 'Density:', key='7,000 people per square mile', note='Any equivalent form, with units.'),
          sa('A circular forest region has radius 3 km and 4,500 trees. Find the tree density to the nearest tree per square kilometer.', 'Density:', key='%d trees per km²' % round(4500 / (9 * PI)),
             note='Rounding to the nearest whole number required. Area 9π ≈ 28.27 km².'),
          sa('Town A has 12,000 people on 30 km². Town B has 9,000 people on 20 km². Which town is more densely populated? Show the densities.', 'Answer:',
             key='Town B (450 per km² vs 400 per km²)', note='Form required: the conclusion with both densities.'),
          sa('A region has a population density of 250 people per km² and is a 4 km by 6 km rectangle. Estimate its population.', 'Population:', key='6,000 people', note='Any equivalent form.'),
          mc('Which is a unit of population density based on area?', ['people per square mile', 'people per mile', 'square miles per person per year', 'people'], note='Count ÷ area.'),
      ],
      back=[
          B('Unit rates', '6.RP.A.3.b', [
              sa('840 items in 12 boxes: items per box?', 'Answer:', key='70', note='Any equivalent form.'),
              sa('$45 for 9 m² of tile: dollars per square meter?', 'Answer:', key='$5 per m²', note='Any equivalent form.'),
              mc('Unit rate for 300 people on 4 km²?', ['75 people per km²', '1,200 people per km²', '0.013 km² per person', '296 people per km²'], note='300 ÷ 4.'),
              tf('A unit rate compares a quantity to one unit of another.', key=True, note='Definition.'),
              tf('600 people on 3 km² is 1,800 people per km².', key=False, note='200.'),
          ], align='exact',
            why=why('the student cannot divide to get "per one".', 'density is a unit rate.', 'computes unit rates.')),
          B('Areas of rectangles and circles', '7.G.B.6', [
              sa('Area of a 4 km by 6 km rectangle?', 'Area:', key='24 km²', note='Any equivalent form.'),
              sa('Exact area of a circle with radius 3 km?', 'Area:', key='9π km²', note='Form required: exact value.'),
              mc('A square region 5 mi on a side has area', ['25 mi²', '20 mi²', '10 mi²', '5 mi²'], note='5².'),
              tf('Area units are square units.', key=True, note='Two dimensions.'),
              tf('A circle with radius 3 has area 6π.', key=False, note='9π.'),
          ], align='exact',
            why=why('the student cannot find the region\'s area.', 'density divides by it.', 'computes areas.')),
          B('Compare ratios', '7.RP.A.2', [
              sa('Which is greater: 12,000/30 or 9,000/20?', 'Answer:', key='9,000/20 (450 > 400)', note='Any equivalent answer.'),
              tf('To compare densities, compare the unit rates.', key=True, note='Same units.'),
              mc('Which rate is greatest?', ['50 per 2 km²', '60 per 3 km²', '80 per 4 km²', '20 per 1 km²'], note='25, 20, 20, 20.'),
              sa('A has 100 trees on 4 acres; B has 120 trees on 6 acres. Which is denser?', 'Answer:', key='A (25 per acre vs 20)', note='Any equivalent answer.'),
              tf('The town with more people is always denser.', key=False, note='Depends on area.'),
          ], align='supporting',
            why=why('the student compares totals instead of rates.', 'comparisons need densities.', 'compares rates.')),
      ],
      f1=B('Convert area units in density problems', 'HSG-MG.A.2', [
          sa('1 square mile is about 2.59 km². Convert 7,000 people per square mile to people per km² (nearest whole number).', 'Answer:', key='%d people per km²' % round(7000 / 2.59),
             note='Rounding to the nearest whole number required. Divide by 2.59.'),
          sa('A lawn of 400 m² needs grass seed at 35 g per m². How many kilograms of seed are needed?', 'Answer:', key='14 kg', note='Any equivalent form.'),
          tf('A density in people per km² is a larger number than the same density in people per mi².', key=False, note='A km² is smaller, so fewer people per km².'),
          mc('A farm plants 2 trees per 10 m². How many trees on 1 hectare (10,000 m²)?', ['2,000', '200', '20,000', '5,000'], note='0.2 per m².'),
          sa('A park of 3 hectares (1 ha = 10,000 m²) has 5,400 visitors. Visitors per 100 m²?', 'Answer:', key='18', note='Any equivalent form. 300 units of 100 m².'),
      ], prog='same-course deepening', demand='Work across area units and rescale densities.'),
      f2=B('Plan capacity from an area density', 'HSG-MG.A.3', [
          sa('Safety rules allow 2 people per m² in a plaza. The plaza is a 30 m by 40 m rectangle. Maximum crowd?', 'Answer:', key='2,400 people', note='Any equivalent form.'),
          sa('A festival expects 5,000 people and wants at most 1.5 people per m². What is the smallest whole number of square meters that meets the limit?', 'Area:', key='{:,} m²'.format(math.ceil(5000 / 1.5)),
             note='Form required: a whole number of m² that meets the limit. 5,000 ÷ 1.5 = 3,333.3…, so round UP to 3,334 (3,333 m² would allow only 4,999.5 people).'),
          tf('When planning for a safety limit, round the capacity up.', key=False, note='Round capacity down (and area up) to stay within the limit.'),
          mc('A circular dance floor of radius 5 m allows 3 people per m². Capacity is about', ['235 people', '47 people', '75 people', '471 people'], note='75π ≈ 235.6, round down.'),
          sa('A circular dance floor of radius 5 m allows at most 3 people per m², and 3 · 25π ≈ 235.6. Explain why the capacity is 235 people, not 236.', 'Answer:', key='Rounding up would exceed the allowed density.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use area densities to set design limits.',
        builds='Builds on FORWARD 1: rescaled densities feed capacity decisions.')),

    # ------------------------------------------------------------------ 85. MG.A.2 volume density
    S('HSG-MG.A.2', 'Apply density based on volume',
      target='Compute and use densities based on volume (mass per volume, energy per volume, organisms per volume) in modeling situations', strand='core', covers=['MG2-volume'],
      main=[
          sa('An aluminum block measures 2 cm by 3 cm by 5 cm and has mass 81 g. Find its density.', 'Density:', key='2.7 g/cm³', note='Any equivalent form, with units.'),
          sa('A cylindrical tank (radius 0.5 m, height 2 m) is full of water (1,000 kg/m³). Find the mass of the water to the nearest kilogram.', 'Mass:', key='%d kg' % round(PI * 0.25 * 2 * 1000),
             note='Rounding to the nearest kilogram required. 0.5π m³.'),
          sa('A heater must supply 20 BTU per cubic foot of room. A room is 12 ft by 15 ft with an 8 ft ceiling. How many BTU are needed?', 'Answer:', key='28,800 BTU', note='Any equivalent form. 1,440 ft³.'),
          sa('A sample has 3 × 10⁶ bacteria per mL. How many bacteria are in 250 mL?', 'Answer:', key='7.5 × 10⁸', note='Any equivalent form.'),
          mc('Water has density 1 g/cm³. Which object floats in water?', ['A 400 g block with volume 500 cm³', 'A 600 g block with volume 500 cm³', 'A 100 g ball with volume 50 cm³', 'A 1,000 g brick with volume 400 cm³'],
             note='Density less than 1 g/cm³ (0.8).'),
      ],
      back=[
          B('Volume of prisms and cylinders', 'HSG-GMD.A.3', [
              sa('Volume of a 2 × 3 × 5 cm block?', 'Volume:', key='30 cm³', note='Any equivalent form.'),
              sa('Exact volume of a cylinder with r = 0.5 m, h = 2 m?', 'Volume:', key='0.5π m³', note='Form required: exact value.'),
              mc('Volume of a 12 × 15 × 8 ft room?', ['1,440 ft³', '35 ft³', '180 ft³', '2,880 ft³'], note='Product.'),
              tf('Volume is needed before a volume density can be used.', key=True, note='Density = amount ÷ volume.'),
              tf('A 1 m cube has volume 3 m³.', key=False, note='1 m³.'),
          ], align='exact',
            why=why('the student cannot find the volume.', 'density uses it.', 'computes volumes.')),
          B('Unit rates', '6.RP.A.3.b', [
              sa('81 g in 30 cm³: grams per cm³?', 'Answer:', key='2.7', note='Any equivalent form.'),
              sa('20 BTU per ft³ for 100 ft³: total?', 'Answer:', key='2,000 BTU', note='Any equivalent form.'),
              mc('500 g in 250 cm³ is', ['2 g/cm³', '0.5 g/cm³', '250 g/cm³', '750 g/cm³'], note='Divide.'),
              tf('Amount = rate × quantity.', key=True, note='Rate use.'),
              tf('Density = volume ÷ mass.', key=False, note='Mass ÷ volume.'),
          ], align='exact',
            why=why('the student divides in the wrong order.', 'density is per unit of volume.', 'computes and uses rates.')),
          B('Products of numbers in scientific notation', '8.EE.A.4', [
              sa('(3 × 10⁶) × 250 in scientific notation?', 'Answer:', key='7.5 × 10⁸', note='Any equivalent form.'),
              sa('Write 2,400,000 in scientific notation.', 'Answer:', key='2.4 × 10⁶', note='Form required: scientific notation.'),
              mc('(2 × 10³)(4 × 10²) =', ['8 × 10⁵', '8 × 10⁶', '6 × 10⁵', '8 × 10¹'], note='Add exponents.'),
              tf('10³ × 10² = 10⁵', key=True, note='Exponent rule.'),
              tf('5 × 10² × 3 = 15 × 10⁶', key=False, note='1.5 × 10³.'),
          ], align='supporting',
            why=why('the student cannot handle large counts.', 'organism densities are large.', 'multiplies in scientific notation.')),
      ],
      f1=B('Use density to identify materials and find volumes', 'HSG-MG.A.2', [
          sa('A ring has mass 9.65 g and volume 0.5 cm³. Gold has density 19.3 g/cm³. Could the ring be pure gold?', 'Answer:', key='Yes: 9.65 ÷ 0.5 = 19.3 g/cm³', note='Form required: the conclusion with the density.'),
          sa('A 1,350 g piece of aluminum (2.7 g/cm³) is melted into a cube. Find the edge of the cube, to the nearest tenth of a centimeter.', 'Edge:', key='%s cm' % d1(500 ** (1 / 3)),
             note='Rounding to 0.1 required. Volume 500 cm³; edge ∛500.'),
          tf('Two objects with equal mass but different volumes have different densities.', key=True, note='Density = m/V.'),
          mc('Oil (0.9 g/cm³) in a 2,000 cm³ jug has mass', ['1,800 g', '2,222 g', '2,000 g', '1,100 g'], note='0.9 × 2,000.'),
          sa('A balloon holds 0.02 m³ of helium (0.18 kg/m³). Mass of the helium in grams?', 'Mass:', key='3.6 g', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Reverse density problems: identify a material or find a volume or dimension.'),
      f2=B('Design within a mass limit', 'HSG-MG.A.3', [
          sa('A truck can carry 12,000 kg. Gravel has density 1,500 kg/m³. What is the largest volume of gravel it can carry?', 'Volume:', key='8 m³', note='Any equivalent form.'),
          sa('A shelf holds at most 40 kg. Books have density 0.8 g/cm³. How many cubic centimeters of books can it hold?', 'Volume:', key='50,000 cm³', note='Any equivalent form. 40,000 g ÷ 0.8.'),
          tf('Mass limits become volume limits by multiplying by the density.', key=False, note='Divide by the density: V = m/d.'),
          mc('A cylindrical water tank must weigh at most 3,140 kg when full (water 1,000 kg/m³, ignore the tank). With radius 1 m, its height can be at most about', ['1 m', '3.14 m', '0.32 m', '10 m'],
             note='3.14 m³ ÷ π.'),
          sa('A concrete block must be under 25 kg. Concrete is 2,400 kg/m³. Will a 20 cm × 20 cm × 30 cm block work?', 'Answer:', key='No: 0.012 m³ × 2,400 kg/m³ = 28.8 kg, which exceeds 25 kg.',
             note='Form required: the conclusion with the mass.'),
      ], prog='cross-standard extension', demand='Turn a mass limit into a design limit on volume and dimensions.',
        builds='Builds on FORWARD 1: solving density for volume becomes a design check.')),
]

BOX = gd({}, [('poly', [(0, 0), (4, 0), (4, 4), (0, 4)]), ('poly', [(0, 0), (0.7, 0), (0.7, 0.7), (0, 0.7)], {'fill': True}),
              ('poly', [(3.3, 0), (4, 0), (4, 0.7), (3.3, 0.7)], {'fill': True}), ('poly', [(3.3, 3.3), (4, 3.3), (4, 4), (3.3, 4)], {'fill': True}),
              ('poly', [(0, 3.3), (0.7, 3.3), (0.7, 4), (0, 4)], {'fill': True}), ('text', (2, -0.35), '20 cm'), ('text', (0.35, 0.35), 'x'), ('text', (-0.4, 2), '20 cm')],
         h=220, desc='A 20 cm by 20 cm square sheet with a shaded x-by-x square at each corner to be cut out before folding up the sides into an open box.', note=NTS)
GRID = gd({}, [('poly', [(0, 0), (8.5, 0), (8.5, 11), (0, 11)]), ('poly', [(1, 1), (7.5, 1), (7.5, 10), (1, 10)], {'dash': True}),
               ('poly', [(1, 1), (2.9, 1), (2.9, 10), (1, 10)], {'fill': True}), ('poly', [(3.3, 1), (5.2, 1), (5.2, 10), (3.3, 10)], {'fill': True}),
               ('poly', [(5.6, 1), (7.5, 1), (7.5, 10), (5.6, 10)], {'fill': True})],
          h=250, desc='A page 8.5 in. wide and 11 in. tall with 1 in. margins on all sides (dashed). Inside the margins are three equal shaded columns separated by two gutters.', note=NTS)

CAN_A = 2 * PI * 16 + 2 * PI * 4 * 10
SETS += [
    # ------------------------------------------------------------------ 86. MG.A.3 physical constraints
    S('HSG-MG.A.3', 'Design to satisfy physical constraints',
      target='Apply geometric methods to design an object or structure that satisfies physical constraints (size limits, slopes, clearances)', strand='core', covers=['MG3-constraints'],
      main=[
          sa('An open box is made from a 20 cm by 20 cm sheet by cutting an x-cm square from each corner and folding up the sides. Compare the volumes for x = 2, 3, and 4. Which gives the largest box?',
             'Answer:', fig=BOX, key='x = 2: 512 cm³; x = 3: 588 cm³; x = 4: 576 cm³; x = 3 is largest', note='Form required: the three volumes and the choice. V = x(20 - 2x)².'),
          sa('Accessibility rules allow a ramp slope of at most 1 : 12 (1 unit of rise per 12 units of run). A ramp must rise 30 in. What is the shortest horizontal run allowed, in feet?', 'Run:',
             key='30 ft', note='Any equivalent form. 30 × 12 = 360 in.'),
          sa('A rectangular pen will use 40 m of fencing. Compare a 10 m by 10 m pen with a 5 m by 15 m pen. Which encloses more area?', 'Answer:', key='The 10 m by 10 m pen (100 m² vs 75 m²)',
             note='Form required: the choice with both areas.'),
          sa('A cylindrical tank must fit in a closet 2 m wide, 2 m deep, and 3 m tall. What is the largest possible volume, to the nearest tenth of a cubic meter?', 'Volume:', key='%s m³' % d1(3 * PI),
             note='Rounding to 0.1 required. Radius 1 m, height 3 m.'),
          mc('A 13 ft ladder leans on a wall. For safety its base must be at least 5 ft from the wall. The highest point it can reach is', ['12 ft', '13 ft', '8 ft', '18 ft'],
             note='√(169 - 25).'),
      ],
      back=[
          B('Volume of a rectangular prism', '7.G.B.6', [
              sa('Volume of a box 14 cm by 14 cm by 3 cm?', 'Volume:', key='588 cm³', note='Any equivalent form.'),
              sa('A 20 cm side with 3 cm cut from each end leaves', 'Length:', key='14 cm', note='Any equivalent form.'),
              mc('Volume of a box 12 by 12 by 4?', ['576', '48', '144', '28'], note='Product.'),
              tf('Cutting larger corners makes the box taller but its base smaller.', key=True, note='Trade-off.'),
              tf('An open box is made from a 20 cm by 20 cm sheet by cutting an x-cm square from each corner. The box\'s base side is 20 - x.', key=False, note='20 - 2x.'),
          ], align='exact',
            why=why('the student cannot find the box dimensions.', 'the design compares volumes.', 'computes box volumes.')),
          B('Use the Pythagorean Theorem', '8.G.B.7', [
              sa('Hypotenuse 13, leg 5: other leg?', 'Leg:', key='12', note='Any equivalent form.'),
              sa('Legs 30 in. and 360 in.: hypotenuse to the nearest inch?', 'Length:', key='%d in.' % round(math.hypot(30, 360)), note='Rounding to the nearest inch required.'),
              mc('A ladder, wall, and ground form a', ['right triangle', 'equilateral triangle', 'square', 'circle'], note='Wall ⊥ ground.'),
              tf('A ladder leans against a vertical wall on level ground. The ladder is the hypotenuse of the right triangle formed.', key=True, note='Opposite the right angle.'),
              tf('The ladder\'s height on the wall is 13 + 5.', key=False, note='Use the theorem.'),
          ], align='exact',
            why=why('the student cannot compute the slanted constraint.', 'ladders and ramps are right triangles.', 'applies the theorem.')),
          B('Ratios and rates', '7.RP.A.2', [
              sa('A ratio of 1 : 12 for a rise of 2 in. gives what run?', 'Run:', key='24 in.', note='Any equivalent form.'),
              sa('Is a slope of 3 : 30 steeper than 1 : 12?', 'Answer:', key='Yes: 3 : 30 = 1 : 10, and 1/10 > 1/12.',
                 note='Form required: yes/no with the comparison.'),
              mc('360 in. = ', ['30 ft', '36 ft', '3.6 ft', '12 ft'], note='÷ 12.'),
              tf('A ratio of 1 : 12 means 1 inch up for every 12 inches across.', key=True, note='Meaning.'),
              tf('A 1 : 8 ramp is less steep than a 1 : 12 ramp.', key=False, note='Steeper.'),
          ], align='exact',
            why=why('the student cannot use the slope limit.', 'ramp constraints are ratios.', 'uses ratios.')),
          B('Inequalities as limits', '7.EE.B.4', [
              sa('The run r must satisfy r ≥ 360. Is r = 300 allowed?', 'Answer:', key='No', note='Any equivalent answer.'),
              sa('A diameter d must satisfy d ≤ 2. Largest radius?', 'Radius:', key='1', note='Any equivalent form.'),
              mc('"At most 3 m" means', ['≤ 3', '≥ 3', '< 3 only', '= 3'], note='Inequality.'),
              tf('"At least 5 ft" allows exactly 5 ft.', key=True, note='≥.'),
              tf('"At most 12" excludes 12.', key=False, note='Includes.'),
          ], align='supporting',
            why=why('the student misreads the constraint.', 'designs must satisfy limits.', 'translates limits to inequalities.')),
      ],
      f1=B('Satisfy several constraints at once', 'HSG-MG.A.3', [
          sa('An open box is made from a 20 cm by 20 cm sheet by cutting an x-cm square from each corner and folding up the sides. Which whole-number values of x give a volume of at least 500 cm³ AND a height of at most 3 cm?', 'Answer:', key='x = 2 and x = 3',
             note='Form required: both values. Volumes 512 and 588; x = 4, 5 are too tall.'),
          sa('A ramp must rise 2 ft and fit within 20 ft of horizontal space. Can it meet the 1 : 12 limit? Explain.', 'Answer:', key='No: it needs 24 ft of run.', note='Form required: the conclusion with the run.'),
          tf('A design that satisfies one constraint may fail another.', key=True, note='Check all.'),
          mc('A rectangular garden needs area 48 m² and width at most 6 m. Which works?', ['6 m wide by 8 m long', '8 m wide by 6 m long', '4 m wide by 10 m long', '7 m wide by 7 m long'], note='Width 6, area 48.'),
          sa('A cylinder 3 m tall must hold at least 10 m³ and stand on a 2 m by 2 m floor space. Is that possible? Explain.', 'Answer:',
             key='No: the largest is r = 1 m, giving 3π ≈ 9.4 m³ < 10 m³.', note='Form required: the conclusion with the volume.'),
      ], prog='same-course deepening', demand='Check a design against two or more constraints together.'),
      f2=B('Find the best design with a function graph', 'HSF-IF.C.7.c', [
          sa('An open box is made from a 20 cm by 20 cm sheet by cutting an x-cm square from each corner and folding up the sides. Write its volume as a function V(x) and state the domain.', 'Answer:', key='V(x) = x(20 - 2x)², 0 < x < 10', note='Form required: the function and the domain.'),
          sa('An open box made from a 20 cm by 20 cm sheet with x-cm corner squares cut out has volume V(x) = x(20 - 2x)². Use a graph or table to estimate the x that gives the largest volume, to the nearest tenth, and that volume to the nearest cm³.', 'Answer:', key='x ≈ 3.3; V ≈ 593 cm³',
             note='Form required: both. (Exact: x = 10/3, V = 16,000/27 ≈ 592.6.)'),
          tf('V(x) = x(20 - 2x)² has zeros at x = 0 and x = 20.', key=False, note='The zeros are x = 0 and x = 10.'),
          mc('For an open box made from a 20 cm by 20 cm sheet, V(x) = x(20 - 2x)². The graph of V on 0 < x < 10 rises and then falls. Its highest point gives', ['the largest volume', 'the smallest volume', 'the cut that makes no box', 'the base area'], note='Maximum.'),
          sa('For an open box made from a 20 cm by 20 cm sheet with x-cm corner cuts, V(x) = x(20 - 2x)² and V is largest near x = 3.3. Why is x = 5 not the best cut even though it is halfway between 0 and 10?', 'Answer:', key='V(5) = 500 < 593; the maximum of a cubic need not be at the middle.', note='Any equivalent answer.'),
      ], prog='later-course extension', demand='Model the design with a polynomial function and find the optimum from its graph (Algebra II).',
        builds='Builds on FORWARD 1: the constraint checks become a function whose maximum is the best design.')),

    # ------------------------------------------------------------------ 87. MG.A.3 minimize cost
    S('HSG-MG.A.3', 'Design to minimize cost',
      target='Apply geometric methods (surface area, area, and volume) to compare designs and choose the one with the lowest cost', strand='core', covers=['MG3-cost'],
      main=[
          sa('A can with radius 4 cm and height 10 cm is made of metal costing $0.002 per cm². Find the area of metal (top, bottom, and side) and the cost, to the nearest cent.', 'Answer:',
             key='%s cm² ≈ %s cm²; cost $%s' % ('112π', d1(CAN_A), d2(CAN_A * 0.002)), note='Form required: the area and the cost. 2πr² + 2πrh = 32π + 80π.'),
          sa('Can A has r = 4 cm, h = 10 cm. Can B has r = 5 cm, h = 6.4 cm. Show that they hold the same volume, then decide which uses less metal.', 'Answer:',
             key='Both hold 160π cm³; A uses 112π cm², B uses 114π cm², so A uses less metal.', note='Form required: both volumes, both areas, and the choice.'),
          sa('A wall 12 m by 3 m has a window 1.5 m by 1.2 m. Paint covers 10 m² per liter and is sold only in whole liters at $8 each. Find the cost to paint the wall once.', 'Cost:', key='$32',
             note='Any equivalent form. 34.2 m² needs 3.42 L, so buy 4 L.'),
          sa('Two closed cardboard boxes each hold 600 cm³: box A is 10 cm by 10 cm by 6 cm and box B is 5 cm by 10 cm by 12 cm. Cardboard costs $0.01 per cm² (ignore thickness and overlaps). '
             'Find the cost of each box and choose the cheaper one.', 'Answer:',
             key='A: 440 cm², $4.40; B: 460 cm², $4.60; box A is cheaper.', note='Form required: both surface areas, both costs, and the choice. A: 2(100 + 60 + 60); B: 2(50 + 60 + 120).'),
          sa('A 4 m by 3.5 m floor is covered with 0.5 m square tiles that cost $3.25 each and are sold individually. Plan A uses these tiles; plan B uses sheet flooring at $11 per m². '
             'Find the cost of each plan and choose the cheaper one.', 'Answer:',
             key='A: 8 × 7 = 56 tiles, $182; B: 14 m² × $11 = $154; plan B is cheaper.', note='Form required: both costs and the choice.'),
      ],
      back=[
          B('Surface area of prisms and cylinders', '7.G.B.6', [
              sa('Exact area of the two circular ends of a can with radius 4?', 'Area:', key='32π', note='Form required: exact value.'),
              sa('Exact area of the side of a can with radius 4 and height 10?', 'Area:', key='80π', note='Form required: exact value. 2πrh.'),
              mc('Surface area of a 2 × 3 × 4 box?', ['52', '24', '26', '48'], note='2(6 + 8 + 12).'),
              tf('The side of a cylinder unrolls into a rectangle.', key=True, note='Net.'),
              tf('A cylinder\'s surface area is πr²h.', key=False, note='That is volume.'),
          ], align='exact',
            why=why('the student cannot find the material area.', 'cost depends on it.', 'computes surface areas.')),
          B('Areas of surfaces with openings', '7.G.B.6', [
              sa('A wall 12 m by 3 m has a 1.5 m by 1.2 m window. Area to paint?', 'Area:', key='34.2 m²', note='Any equivalent form.'),
              sa('A 4 m by 3.5 m floor: area?', 'Area:', key='14 m²', note='Any equivalent form.'),
              mc('A 5 m by 2.4 m wall has a 0.9 m by 2 m door. Paintable area?', ['10.2 m²', '12 m²', '1.8 m²', '13.8 m²'], note='12 - 1.8.'),
              tf('Openings in a surface are subtracted from its area before buying material.', key=True, note='No material is needed there.'),
              tf('A floor of 14 m² needs 14 tiles that are 0.5 m on a side.', key=False, note='Each tile is 0.25 m², so 56 tiles.'),
          ], align='exact', num=4,
            why=why('the student cannot find the area that needs material.', 'cost is area × unit price.', 'finds areas with openings.')),
          B('Unit prices and rounding up purchases', '7.EE.B.3', [
              sa('Paint needed is 3.42 L, sold in whole liters. How many liters must be bought?', 'Liters:', key='4', note='Any equivalent form.'),
              sa('Metal costs $0.002 per cm². Cost of 350 cm²?', 'Cost:', key='$0.70', note='Any equivalent form.'),
              mc('Fabric is $6 per yard, sold in whole yards. You need 4.2 yd. Cost?', ['$30', '$25.20', '$24', '$26'], note='Buy 5 yd.'),
              tf('When items are sold in whole units, round the amount needed up.', key=True, note='Enough material.'),
              tf('3.1 cans of paint can be bought as 3 cans.', key=False, note='Need 4.'),
          ], align='supporting',
            why=why('the student rounds down purchases.', 'real cost uses whole units.', 'rounds up correctly.')),
      ],
      f1=B('Compare designs with equal volume for least material', 'HSG-MG.A.3', [
          sa('A closed box with a square base must hold 1,000 cm³ (ignore the thickness of the material). Compare the surface areas for base sides 8, 10, and 12 cm. Which uses the least material?', 'Answer:',
             key='8 cm: 628 cm²; 10 cm: 600 cm²; 12 cm: about 621 cm²; the 10 cm cube uses the least', note='Form required: the three areas and the choice. h = 1000/s².'),
          sa('A closed cylinder must hold 1,000 cm³. Compare its surface area (to the nearest cm²) for radii 4 cm, 5.42 cm and 7 cm, and choose the radius that uses the least material.', 'Answer:',
             key='r = 4: %d cm²; r = 5.42: %d cm²; r = 7: %d cm²; r = 5.42 cm uses the least.' % tuple(round(2 * PI * r * r + 2000 / r) for r in (4, 5.42, 7)),
             note='Form required: three areas and the choice. h = 1000/(πr²), so the area is 2πr² + 2000/r.'),
          tf('Among closed boxes with a square base and a fixed volume (ignoring material thickness), the cube has the least surface area.', key=True, note='Classic result.'),
          mc('For a closed cylinder with a fixed volume, the least surface area occurs when', ['the height equals the diameter', 'the height equals the radius', 'the radius is as large as possible',
                                                                                                'the height is as large as possible'], note='h = 2r (r = 5.42 cm gives h ≈ 10.84 cm).'),
          sa('Give one reason a manufacturer might NOT choose the least-material can shape.', 'Answer:', key='For example: it is hard to grip, does not fit standard shelves, or leaves too little label space.',
             note='Any reasonable reason.'),
      ], prog='same-course deepening', demand='Compare several designs under a fixed requirement and choose the one using the least material.'),
      f2=B('Decide between designs using expected cost', 'HSS-MD.B.7', [
          sa('Packaging A costs $1.20 per item and 2% of items break. Packaging B costs $0.90 and 8% break. A break costs $20. Find the expected cost per item for each and choose.', 'Answer:',
             key='A: $1.20 + 0.02 × $20 = $1.60; B: $0.90 + 0.08 × $20 = $2.50; choose A', note='Form required: both expected costs and the choice.'),
          sa('The standard metal for a can never fails. A cheaper metal fails 5% of the time, and each failure costs $40 to replace. By how much must the cheaper metal\'s price per can be below '
             'the standard price for its expected cost per can to be strictly lower?', 'Answer:', key='By more than $2.00 (0.05 × $40 = $2.00 expected failure cost)',
             note='Form required: "more than $2.00"; exactly $2.00 cheaper gives equal expected costs.'),
          tf('The cheapest material always gives the cheapest design.', key=False, note='Failures and replacement costs can make it more expensive overall.'),
          mc('Expected cost = ', ['upfront cost + probability of failure × cost of failure', 'upfront cost × probability', 'cost of failure only', 'upfront cost - probability'],
             note='Weighted cost.'),
          sa('Name one cost besides material that a can designer might consider.', 'Answer:', key='For example shipping weight, labor, breakage, or recycling.', note='Any reasonable answer.'),
      ], prog='later-course extension', demand='Use probability to compare design costs that include risk (Probability & Statistics).',
        builds='Builds on FORWARD 1: the least-material design is re-examined when failures carry a cost.')),

    # ------------------------------------------------------------------ 105. MG.A.3 typographic grids
    S('HSG-MG.A.3', 'Design typographic grid systems',
      target='Apply ratios and measurement to lay out typographic grid systems (columns, gutters, margins, and modules) that fit a page', strand='core', covers=['MG3-grid'], num=105,
      main=[
          sa('A page is 8.5 in. wide with 1 in. margins on each side. The text area has 3 equal columns separated by 2 gutters of 0.2 in. Find the width of each column to the nearest hundredth of an inch.',
             'Width:', fig=GRID, key='%s in.' % d2((8.5 - 2 - 0.4) / 3), note='Rounding to 0.01 required. (6.5 - 0.4) ÷ 3.'),
          mc('A poster grid uses the golden ratio (about 1.618 : 1) for height : width. A poster is 60 cm wide. Its height is about', ['97.1 cm', '37.1 cm', '61.6 cm', '120 cm'],
             note='60 × 1.618.'),
          sa('A 12-column grid on a 6.5 in. text area has 11 gutters of 0.125 in. Find the width of each column to the nearest thousandth of an inch.', 'Width:', key='%.3f in.' % ((6.5 - 11 * 0.125) / 12),
             note='Rounding to 0.001 required. (6.5 - 1.375) ÷ 12.'),
          sa('A web page 1,200 px wide uses a 12-column grid with 24 px gutters between columns and no outer margins. Find the column width and the width of an element that spans 4 columns '
             '(including the gutters inside it).', 'Answer:', key='Column 78 px; 4-column element 384 px', note='Form required: both. (1,200 - 11 · 24) ÷ 12 = 78; 4 · 78 + 3 · 24 = 384.'),
          sa('A 6 in. by 9 in. page has 0.75 in. margins on all sides. A modular grid has 3 columns and 4 rows with 0.25 in. gutters in both directions. Find the width and height of each module '
             'to the nearest hundredth of an inch.', 'Answer:', key='Width %s in.; height %s in.' % (d2((4.5 - 0.5) / 3), d2((7.5 - 0.75) / 4)),
             note='Form required: both, rounded to 0.01. Text area 4.5 by 7.5; (4.5 - 2 · 0.25) ÷ 3 and (7.5 - 3 · 0.25) ÷ 4.'),
      ],
      back=[
          B('Proportional reasoning with ratios', '7.RP.A.2', [
              sa('Height : width = 1.618 : 1 and width = 10. Height?', 'Height:', key='16.18', note='Any equivalent form.'),
              sa('Split 6.1 in. into 3 equal columns. Width of each (nearest hundredth)?', 'Width:', key='2.03 in.', note='Rounding to 0.01 required.'),
              mc('A 2 : 3 rectangle 30 cm wide (width = 2 parts) is', ['45 cm tall', '20 cm tall', '60 cm tall', '33 cm tall'], note='15 per part.'),
              tf('Equal columns divide the available width equally.', key=True, note='Definition.'),
              tf('A 1 : 2 ratio means the second is half the first.', key=False, note='Twice.'),
          ], align='exact',
            why=why('the student cannot apply a layout ratio.', 'grids are built from ratios.', 'uses ratios.')),
          B('Operate with decimals', '6.NS.B.3', [
              sa('8.5 - 2 × 1 = ', 'Answer:', key='6.5', note='Any equivalent form.'),
              sa('11 × 0.125 = ', 'Answer:', key='1.375', note='Any equivalent form.'),
              mc('6.1 ÷ 3 to the nearest hundredth is', ['2.03', '2.04', '2.3', '18.3'], note='2.0333….'),
              tf('5.125 ÷ 12 ≈ 0.427', key=True, note='Division.'),
              tf('0.2 + 0.2 = 0.04', key=False, note='0.4.'),
          ], align='exact',
            why=why('the student makes decimal errors.', 'grid measurements are decimals.', 'adds, subtracts, multiplies and divides decimals.')),
          B('Factors of a whole number', '4.OA.B.4', [
              sa('List all factors of 12.', 'Factors:', key='1, 2, 3, 4, 6, 12', note='Form required: all six.'),
              sa('Which numbers from 2 to 6 are factors of 10?', 'Answer:', key='2 and 5', note='Form required: both.'),
              mc('Which is a factor of 12?', ['4', '5', '7', '8'], note='12 ÷ 4 = 3.'),
              tf('12 has more factors than 10.', key=True, note='Six factors vs four.'),
              tf('5 is a factor of 12.', key=False, note='12 ÷ 5 is not whole.'),
          ], align='supporting',
            why=why('the student does not see why some column counts split evenly.', 'equal column groups need factors.', 'finds factors.')),
      ],
      f1=B('Choose grids that support several layouts', 'HSG-MG.A.3', [
          mc('A 12-column grid can also be used as', ['4 columns of 3, 3 of 4, or 2 of 6', 'only 12 columns', '5 equal columns', '7 equal columns'], note='Divisors of 12.'),
          sa('Why do designers often choose 12-column grids?', 'Answer:', key='12 divides evenly into 2, 3, 4, and 6, giving many layout options.', note='Any equivalent answer.'),
          tf('A 10-column grid can be split into 3 equal groups of whole columns.', key=False, note='3 is not a factor of 10.'),
          sa('A 12-column grid has 78 px columns and 24 px gutters. How wide is an element that spans 6 columns?', 'Width:', key='588 px', note='Any equivalent form. 6 · 78 + 5 · 24.'),
          sa('A 6.5 in. text area must hold 4 columns, each 1.5 in. wide, with equal gutters between them. Find the exact gutter width.', 'Gutter:', key='⅙ in. ≈ 0.17 in.',
             note='Exact value or rounding to 0.01. (6.5 - 6) ÷ 3.'),
      ], prog='same-course deepening', demand='Choose and use grids that allow several layouts, working backward from a required column width.'),
      f2=B('Scale a grid layout to a new page size', 'HSG-SRT.A.2', [
          sa('A poster layout is 60 cm wide and 97.1 cm tall. It is reduced to a flyer 24 cm wide with the same shape. Find the scale factor and the flyer\'s height.', 'Answer:',
             key='Factor 0.4; height 38.84 cm', note='Form required: both. 24 ÷ 60; 97.1 × 0.4.'),
          sa('In the poster above, a column is 15 cm wide and a gutter is 1.2 cm. Find their widths on the flyer.', 'Answer:', key='Column 6 cm; gutter 0.48 cm', note='Form required: both. Multiply by 0.4.'),
          tf('Scaling a layout by factor k multiplies the area of each module by k².', key=True, note='Similar figures.'),
          mc('A layout is enlarged by factor 1.5. A 4 cm by 6 cm module becomes', ['6 cm by 9 cm', '5.5 cm by 7.5 cm', '4 cm by 9 cm', '9 cm by 13.5 cm'], note='Multiply both by 1.5.'),
          sa('Explain why a grid keeps its proportions when every measurement is multiplied by the same factor.', 'Answer:',
             key='Every ratio of two measurements is unchanged (k·a/k·b = a/b), so the scaled layout is similar to the original.', note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Use similarity (one scale factor) to resize a whole grid system.',
        builds='Builds on FORWARD 1: a chosen grid is resized to another format with a single scale factor.')),

]
