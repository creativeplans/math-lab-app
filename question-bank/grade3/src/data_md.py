from qb import S, B, sa, mc, tf, nl, plot, draw_write, table
from common import (clock, BLANK_CLOCK, ruler, beaker, bargraph, picgraph, blank_picgraph, tline, fline, fdot, grid, scale)

SPORTS = bargraph(['Soccer', 'Tennis', 'Golf', 'Swim'], [24, 12, 6, 18], 4, 'Number of students', ymax=24)
BOOKS = bargraph(['Mon', 'Tue', 'Wed', 'Thu'], [14, 8, 20, 12], 2, 'Books read', ymax=20)
APPLES = picgraph('Apples picked', [('Ana', 5), ('Ben', 3), ('Cy', 4)], '3 apples', 3)
COLORS = bargraph(['Red', 'Blue', 'Green'], [5, 3, 4], 1, 'Number of children', ymax=6)
PETS = bargraph(['Cats', 'Dogs', 'Fish'], [4, 7, 2], 1, 'Number of pets', ymax=8)
SPORT_PICS = picgraph('Favorite sport', [('Soccer', 4), ('Tennis', 2), ('Swim', 3)], '1 child', 1)
LEAVES = fdot(0, 1, {0.125: 1, 0.375: 2, 0.5: 2, 0.75: 1}, 8, 'Leaf length (inches)')
WATER = fdot(0, 1, {0.125: 1, 0.25: 2, 0.375: 1, 0.5: 1}, 8, 'Water in each cup (liters)')
RAIN = fdot(0, 1, {0.25: 2, 0.5: 1, 0.625: 1, 0.875: 1}, 8, 'Rainfall (inches)')
JUICE = fdot(0, 1, {0.25: 1, 0.5: 2, 0.75: 1}, 4, 'Juice in each glass (cups)')
LEAF4 = fdot(0, 1, {0.25: 1, 0.5: 3, 0.75: 2, 1: 1}, 4, 'Leaf length (inches)')
TRIP_LINE = nl(0, 240, 15, minor=5, labels={0: '9:00 a.m.', 60: '10:00 a.m.', 120: '11:00 a.m.', 180: '12:00 p.m.', 240: '1:00 p.m.'},
               desc='Time number line from 9:00 a.m. to 1:00 p.m., with tick marks every 15 minutes, smaller ticks every 5 minutes, and labels '
                    'every hour. Nothing is marked; the student draws on it.')

CANS = bargraph(['Mon', 'Tue', 'Wed', 'Thu'], [16, 6, 10, 12], 2, 'Cans collected', ymax=16)
BEADS = bargraph(['Red', 'Blue', 'Green', 'Yellow'], [25, 15, 35, 20], 5, 'Number of beads', ymax=35)
HOME_PETS = bargraph(['Cats', 'Dogs', 'Birds', 'Fish'], [5, 8, 3, 6], 1, 'Number of pets', ymax=8)
SNACKS = fdot(0, 1, {0.25: 2, 0.5: 3, 0.75: 1}, 4, 'Snack weight (pounds)')
RAIN6 = fdot(0, 1, {0.125: 2, 0.375: 1, 0.5: 2, 0.875: 1}, 8, 'Rain each day (inches)')
ROOMS = picgraph('Cans collected', [('Room A', 6), ('Room B', 2), ('Room C', 4)], '5 cans', 5)
BOOKS5 = picgraph('Books read', [('Leo', 4), ('Mia', 6)], '5 books', 5)
PAINT = fdot(0, 1, {0.25: 3, 0.5: 1, 0.75: 2}, 4, 'Paint in each can (liters)')
BOLTS = fdot(0, 1, {0.125: 1, 0.375: 2, 0.625: 3, 0.875: 1}, 8, 'Bolt length (inches)')
MILES = grid(5, 20, ystep=5, xlabel='Hours', ylabel='Miles', pts=[(1, 5), (2, 10), (3, 15), (4, 20)])
FRUIT_BARS = bargraph(['Red', 'Blue', 'Green'], [8, 12, 6], 2, 'Number of students', ymax=12)

SETS = [
    # ------------------------------------------------------------------ 3.MD.A.1 (tell time)
    S('3.MD.A.1', 'Tell and write time to the nearest minute',
      main=[
          sa('What time does the clock show?', 'Time:', key='4:37', fig=clock(4, 37)),
          mc('What time does the clock show?', ['8:12', '2:40', '8:14', '3:40'], fig=clock(8, 12)),
          plot('Draw the hands on the clock to show 10:53.', BLANK_CLOCK,
               key='The minute hand points to 53 minutes (2 marks before the 11), and the hour hand is just before the 11'),
          tf('The clock shows 6:21.', key=True, fig=clock(6, 21)),
          tf('The clock shows 1:48.', key=False, fig=clock(2, 48)),
      ],
      back=[
          B('Tell time to the nearest five minutes', '2.MD.C.7', [
              sa('What time does the clock show?', 'Time:', key='3:25', fig=clock(3, 25)),
              tf('The clock shows 9:40.', key=True, fig=clock(9, 40)),
              mc('What time does the clock show?', ['11:05', '1:55', '12:05', '11:01'], fig=clock(11, 5)),
              sa('When the minute hand points to the 6, how many minutes after the hour is it?', 'Minutes:', key='30'),
              tf('The clock shows 7:15.', key=False, fig=clock(7, 45)),
          ]),
          B('Skip-count by 5s', '2.NBT.A.2', [
              sa('Skip-count by 5s from 0 to 35.\nHow many 5s did you count?', 'Fives:', key='7'),
              tf('Counting by 5s: 40, 45, 50, 55.', key=True),
              mc('Count by 5s.\n15, 20, 25, ___', ['30', '26', '35', '50']),
              sa('Skip-count by 5s.\n35, 40, 45, ___, ___', 'Next two:', key='50, 55'),
              tf('Counting by 5s from 5, the 9th number is 40.', key=False),
          ]),
      ],
      f1=B('Express hours in minutes and minutes in seconds', '4.MD.A.1', [
          sa('How many minutes are in 3 hours?', 'Minutes:', key='180'),
          tf('5 minutes = 300 seconds', key=True),
          mc('1 hour 20 minutes = ___ minutes', ['80', '120', '70', '140']),
          sa('Complete the table.', 'Missing values:', key='120; 240',
             fig=table([['Minutes', '1', '2', '3', '4'], ['Seconds', '60', '?', '180', '?']])),
          tf('2 hours = 200 minutes', key=False),
      ]),
      f2=B('Convert between units of time, including fractions of an hour', '5.MD.A.1', [
          sa('How many hours is 150 minutes?', 'Hours:', key='2 1/2 hours', note='2.5 hours is also correct.'),
          tf('90 seconds = 1{1/2} minutes', key=True),
          mc('A movie is 135 minutes long.\nHow long is it in hours and minutes?',
             ['2 hours 15 minutes', '1 hour 35 minutes', '2 hours 35 minutes', '13 hours 5 minutes']),
          sa('How many minutes are in {3/4} of an hour?', 'Minutes:', key='45'),
          tf('3{1/2} hours = 330 minutes', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.1 (word problems)
    S('3.MD.A.1', 'Solve word problems about time intervals in minutes',
      main=[
          sa('A soccer game starts at 2:15 and ends at 3:05.\nHow many minutes long is the game?', 'Minutes:', key='50 minutes'),
          sa('Mia starts reading at 6:40. She reads for 35 minutes.\nWhat time does she stop?', 'Time:', key='7:15'),
          mc('A bus ride takes 25 minutes and ends at 8:10.\nWhat time did the ride start?', ['7:45', '8:35', '7:55', '7:35']),
          tf('Ben practices piano for 20 minutes and then guitar for 15 minutes. He practices for 35 minutes in all.', key=True),
          tf('A class starts at 10:50 and lasts 45 minutes. It ends at 11:25.', key=False),
      ],
      back=[
          B('Tell time and use a.m. and p.m.', '2.MD.C.7', [
              tf('Times from midnight until noon are a.m. times.', key=True),
              mc('Which time is in the afternoon?', ['3:00 p.m.', '3:00 a.m.', '11:00 a.m.', '6:00 a.m.']),
              sa('Is 9:00 at night an a.m. time or a p.m. time?', 'Answer:', key='p.m.'),
              sa('What time does the clock show?', 'Time:', key='5:50', fig=clock(5, 50)),
              tf('Noon is written as 12:00 a.m.', key=False),
          ]),
          B('Add two-digit numbers within 100', '2.NBT.B.5', [
              sa('Add.\n35 + 25', 'Sum:', key='60'),
              tf('45 + 15 = 60', key=True),
              mc('20 + 55 = ?', ['75', '65', '35', '85']),
              sa('Add.\n40 + 35', 'Sum:', key='75'),
              tf('25 + 50 = 85', key=False),
          ]),
      ],
      f1=B('Solve word problems about time intervals in hours and minutes', '4.MD.A.2', [
          sa('A train leaves at 9:45 a.m. and arrives at 1:20 p.m.\nHow long is the trip?', 'Time:', key='3 hours 35 minutes',
             note='215 minutes is also correct.'),
          tf('A movie starts at 6:50 p.m. and lasts 1 hour 45 minutes. It ends at 8:35 p.m.', key=True),
          mc('A hike takes 2 hours 40 minutes and ends at 4:10 p.m.\nWhen did it start?', ['1:30 p.m.', '2:30 p.m.', '1:50 p.m.', '6:50 p.m.']),
          sa('Ty practices for 35 minutes each day for 4 days.\nHow long does he practice in all? Write the answer in hours and minutes.', 'Time:',
             key='2 hours 20 minutes', note='The answer must be in hours and minutes, as the question asks.'),
          tf('A 50-minute lesson that starts at 11:30 a.m. ends at 12:10 p.m.', key=False),
      ]),
      f2=B('Solve multistep time problems with conversions and fractions of a minute or hour', '5.MD.A.1', [
          sa('A race has 3 laps. Each lap takes 1{1/2} minutes.\nHow many seconds does the race take?', 'Seconds:', key='270 seconds'),
          tf('A trip of 2 hours 15 minutes is 2.25 hours long.', key=True),
          mc('Ana runs for 0.75 hour and then walks for 20 minutes.\nHow many minutes is that in all?', ['65', '95', '55', '75']),
          sa('A video is 2{1/4} minutes long.\nHow many seconds is that?', 'Seconds:', key='135 seconds'),
          tf('{1/3} of an hour is 30 minutes.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.1 (number line)
    S('3.MD.A.1', 'Represent time-interval problems on a number line diagram',
      main=[
          draw_write('Lu starts her homework at 4:10 and works for 40 minutes.\nShow the time with jumps on the number line. What time does she finish?',
                     tline(4, 60), 'Time:', draw='Jumps that start at 4:10 and add up to 40 minutes, ending at 4:50', key='4:50',
                     note='Grade both: jumps from 4:10 that total 40 minutes, and the time 4:50.'),
          sa('The number line shows a trip.\nHow many minutes long is the trip?', 'Minutes:', key='35 minutes',
             fig=tline(2, 60, pts=[(15, None), (50, None)], jumps=[(15, 50, None)])),
          mc('A number line from 3:00 to 4:00 is marked every 5 minutes. Kim jumps from 3:15 to 3:40.\nHow many minutes is the jump?', ['25', '55', '40', '5']),
          tf('On a number line from 9:00 to 10:00, 9:30 is halfway between 9:00 and 10:00.', key=True),
          tf('On a number line, the jump from 7:20 to 8:05 is 35 minutes.', key=False),
      ],
      back=[
          B('Show sums and differences within 100 on a number line', '2.MD.B.6', [
              sa('Start at 30 on a number line and jump 25.\nWhere do you land?', 'Number:', key='55'),
              tf('A jump from 15 to 45 on a number line is a jump of 30.', key=True),
              mc('A jump from 40 to 75 on a number line is a jump of how much?', ['35', '115', '45', '25']),
              plot('Show 20 + 15 with jumps on the number line.', nl(0, 50, 5, labels={0: '0', 10: '10', 20: '20', 30: '30', 40: '40', 50: '50'}),
                   key='A start at 20 and jumps that total 15 (for example three jumps of 5), ending at 35'),
              tf('Starting at 10 on a number line, a jump of 30 lands on 50.', key=False),
          ]),
          B('Read clocks to the nearest five minutes', '2.MD.C.7', [
              sa('What time does the clock show?', 'Time:', key='12:35', fig=clock(12, 35)),
              tf('The clock shows 4:20.', key=True, fig=clock(4, 20)),
              mc('What time does the clock show?', ['10:10', '2:50', '10:02', '11:10'], fig=clock(10, 10)),
              sa('At 8:45, which number does the minute hand point to?', 'Number:', key='9'),
              tf('At 3:30, the minute hand points to the 3.', key=False),
          ]),
      ],
      f1=B('Use number line diagrams for time problems in hours and minutes', '4.MD.A.2', [
          draw_write('A field trip goes from 9:40 a.m. to 12:15 p.m.\nShow jumps on the number line from the start to the end. How long is the trip?',
                     TRIP_LINE, 'Time:', draw='Jumps on the number line from 9:40 a.m. to 12:15 p.m. that add up to 2 hours 35 minutes',
                     key='2 hours 35 minutes', note='155 minutes is also correct. Grade both: the jumps, and the length of the trip.'),
          tf('On a number line, the jump from 10:45 a.m. to 12:30 p.m. is 1 hour 45 minutes.', key=True),
          mc('A jump of 1 hour 20 minutes starts at 2:50 p.m. on a number line.\nWhere does it end?', ['4:10 p.m.', '3:70 p.m.', '4:20 p.m.', '3:10 p.m.']),
          draw_write('A show starts at 7:35 p.m. and lasts 1 hour 40 minutes.\nShow the jumps on the number line. When does the show end?',
                     tline(7, 180, step=10, every=60, suffix=' p.m.'), 'Ends at:',
                     draw='Jumps from 7:35 p.m. that total 1 hour 40 minutes, ending at 9:15 p.m.', key='9:15 p.m.',
                     note='Grade both: the jumps, and 9:15 p.m.'),
          tf('On a number line, the jump from 11:50 a.m. to 1:05 p.m. is 1 hour 25 minutes.', key=False),
      ]),
      f2=B('Use fractions and decimals of an hour in time problems', '5.MD.A.1', [
          sa('How many minutes are in {1/4} of an hour?', 'Minutes:', key='15 minutes'),
          tf('1{1/2} hours is 90 minutes.', key=True),
          mc('A trip takes 2{1/4} hours.\nHow many minutes is that?', ['135', '125', '225', '150']),
          sa('Mia reads for 0.5 hour and then for 0.75 hour.\nHow many minutes does she read in all?', 'Minutes:', key='75 minutes'),
          tf('{2/3} of an hour is 45 minutes.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.2 (measure and estimate)
    S('3.MD.A.2', 'Estimate liquid volumes and masses in liters, grams, and kilograms',
      main=[
          mc('Which is the best estimate of the water in a full kitchen sink?', ['20 liters', '2 liters', '200 liters', '1 liter']),
          mc('Which object has a mass of about 1 kilogram?', ['A pineapple', 'A paper clip', 'A car', 'A grape']),
          tf('A bathtub holds more than 1 liter of water.', key=True),
          sa('Would you measure the mass of a bean in grams or in kilograms?', 'Unit:', key='Grams'),
          tf('A paper clip has a mass of about 1 kilogram.', key=False),
      ],
      back=[
          B('Estimate lengths in inches, feet, centimeters, and meters', '2.MD.A.3', [
              sa('About how long is a new pencil: 7 inches or 7 feet?', 'Answer:', key='7 inches'),
              tf('A door is about 2 meters tall.', key=True),
              mc('Which is the best estimate of the length of a car?', ['4 meters', '4 centimeters', '4 inches', '40 meters']),
              sa('About how long is a paper clip: 3 centimeters or 3 meters?', 'Answer:', key='3 centimeters'),
              tf('A school bus is about 12 inches long.', key=False),
          ]),
          B('Choose and use tools to measure length', '2.MD.A.1', [
              tf('A meter stick is a good tool for measuring the length of a classroom.', key=True),
              mc('Which tool is best for measuring the length of a crayon?', ['A ruler', 'A scale', 'A clock', 'A measuring cup']),
              sa('How long is the eraser?', 'Length:', key='2 inches', fig=ruler(4, (0, 2), 'eraser', div=1)),
              sa('Name a tool you can use to measure the length of a hallway.', 'Tool:', key='A measuring tape',
                 note='A yardstick or a meter stick is also correct.'),
              tf('A clock is a tool for measuring length.', key=False),
          ]),
      ],
      f1=B('Know the relative sizes of grams and kilograms, and of milliliters and liters', '4.MD.A.1', [
          sa('How many grams are in 3 kilograms?', 'Grams:', key='3,000 grams'),
          tf('1 liter = 1,000 milliliters', key=True),
          mc('Which is heaviest?', ['2 kilograms', '200 grams', '1,500 grams', '20 grams']),
          sa('Complete the table.', 'Missing values:', key='2,000; 4,000',
             fig=table([['Liters', '1', '2', '3', '4'], ['Milliliters', '1,000', '?', '3,000', '?']])),
          tf('5 kilograms = 500 grams', key=False),
      ]),
      f2=B('Convert metric units of mass and liquid volume with decimals', '5.MD.A.1', [
          sa('Convert.\n2.5 kilograms = ___ grams', 'Grams:', key='2,500'),
          tf('750 milliliters = 0.75 liter', key=True),
          mc('Convert.\n3,200 grams = ___ kilograms', ['3.2', '32', '0.32', '320']),
          sa('Convert.\n1.25 liters = ___ milliliters', 'Milliliters:', key='1,250'),
          tf('400 grams = 4 kilograms', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.2 (word problems)
    S('3.MD.A.2', 'Solve one-step word problems about masses or liquid volumes',
      main=[
          sa('A pot holds 9 liters of soup. 4 liters are served.\nHow many liters are left?', 'Liters:', key='5 liters'),
          sa('Each bag of rice has a mass of 5 kilograms.\nWhat is the mass of 6 bags?', 'Mass:', key='30 kilograms'),
          mc('A 36-liter tank is filled with a 4-liter bucket.\nHow many full buckets fill the tank?', ['9', '32', '40', '8']),
          tf('A 450-gram melon and a 300-gram apple have a total mass of 850 grams.', key=False),
          tf('24 liters of juice are shared equally among 3 jugs. Each jug gets 6 liters.', key=False),
      ],
      back=[
          B('Subtract lengths in one-step word problems within 100', '2.MD.B.5', [
              sa('A rope is 85 cm long. 38 cm is cut off.\nHow long is the rope now?', 'Length:', key='47 cm'),
              tf('An 80-inch shelf with 35 inches cut off is 45 inches long.', key=True),
              mc('A path is 64 m long. Ana has walked 29 m.\nHow far does she have left?', ['35 m', '93 m', '45 m', '25 m']),
              sa('A stick is 74 inches long. Lu cuts off 26 inches.\nHow long is the stick now?', 'Length:', key='48 inches'),
              tf('A 90-cm board with 45 cm cut off is 55 cm long.', key=False),
          ]),
          B('Add two-digit numbers within 100', '2.NBT.B.5', [
              sa('Add.\n45 + 30', 'Sum:', key='75'),
              tf('60 + 25 = 85', key=True),
              mc('38 + 27 = ?', ['65', '55', '11', '75']),
              sa('Add.\n54 + 19', 'Sum:', key='73'),
              tf('29 + 46 = 65', key=False),
          ]),
      ],
      f1=B('Solve liquid volume and mass problems that need a unit conversion', '4.MD.A.2', [
          sa('A jug holds 2 liters. Ella pours out 750 milliliters.\nHow many milliliters are left?', 'Milliliters:', key='1,250 milliliters'),
          tf('Four 250-gram bags of nuts have a total mass of 1 kilogram.', key=True),
          mc('A 3-kilogram bag of flour is split into 6 equal bags.\nWhat is the mass of each bag?', ['500 grams', '2 grams', '50 grams', '5,000 grams']),
          sa('A box has a mass of 1 kg 200 g. Another box has a mass of 850 g.\nWhat is their total mass in grams?', 'Grams:', key='2,050 grams'),
          tf('A 5-liter jug fills exactly 8 cups that each hold 500 milliliters.', key=False),
      ]),
      f2=B('Solve multistep problems with metric conversions and decimals', '5.MD.A.1', [
          sa('A 1.5-liter bottle fills 6 equal cups.\nHow many milliliters go in each cup?', 'Milliliters:', key='250 milliliters'),
          tf('3 bags that each have a mass of 0.4 kg have a total mass of 1,200 grams.', key=True),
          mc('A 2.4-kg cheese is cut into 8 equal pieces.\nWhat is the mass of each piece?', ['300 grams', '30 grams', '3 kilograms', '0.03 kilogram']),
          sa('A tank has 4.5 liters of water. 1,750 mL leaks out.\nHow many liters are left?', 'Liters:', key='2.75 liters'),
          tf('Five 350-mL glasses hold 1.5 liters in all.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.2 (mass) — added in 2.0.0
    S('3.MD.A.2', 'Measure mass in grams and kilograms with a scale', num=63,
      main=[
          sa('What is the mass of the bag of rice?', 'Mass:', key='3 kilograms', fig=scale(5, 1, 3, 'kg', 'rice')),
          sa('What is the mass of the apple?', 'Mass:', key='200 grams', fig=scale(500, 50, 200, 'g', 'apple', label_step=100)),
          mc('What is the mass of the book?', ['2 kilograms', '3 kilograms', '1 kilogram', '20 kilograms'], fig=scale(4, 1, 2, 'kg', 'book')),
          tf('The scale shows 700 grams.', key=True, fig=scale(1000, 100, 700, 'g', 'melon', label_step=200)),
          tf('The scale shows 4 kilograms.', key=False, fig=scale(10, 1, 6, 'kg', 'pumpkin', label_step=2)),
      ],
      back=[
          B('Read a length on a ruler', '2.MD.A.1', [
              sa('How long is the stick?', 'Length:', key='5 inches', fig=ruler(6, (0, 5), 'stick', div=1)),
              tf('A ruler is a tool for measuring length.', key=True),
              mc('How long is the ribbon?', ['3 inches', '4 inches', '2 inches', '5 inches'], fig=ruler(5, (0, 3), 'ribbon', div=1)),
              sa('A pencil reaches from 0 to 7 on a centimeter ruler.\nHow long is it?', 'Length:', key='7 cm'),
              tf('A ruler is a tool for measuring how heavy something is.', key=False),
          ]),
          B('Read numbers on a scale that counts by 10s or 100s', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='300', fig=nl(0, 500, 100, labels={0: '0', 500: '500'}, pts=[(300, 'A')])),
              tf('On a number line that counts by 100s, the mark after 400 is 500.', key=True),
              mc('A number line counts by 10s: 0, 10, 20, 30.\nWhat number is halfway between 20 and 30?', ['25', '21', '35', '50']),
              sa('What number is at point B?', 'B =', key='60', fig=nl(0, 100, 10, labels={0: '0', 100: '100'}, pts=[(60, 'B')])),
              tf('On a number line that counts by 50s, the mark after 150 is 250.', key=False),
          ]),
      ],
      f1=B('Express masses in kilograms as grams', '4.MD.A.1', [
          sa('A bag of flour has a mass of 2 kilograms.\nWhat is its mass in grams?', 'Grams:', key='2,000 grams'),
          tf('A 5-kg bag of potatoes has a mass of 5,000 grams.', key=True),
          mc('Which mass is the same as 3 kg 400 g?', ['3,400 g', '340 g', '34,000 g', '3,004 g']),
          sa('Complete the table.', 'Missing values:', key='4,000; 6,000', fig=table([['Kilograms', '2', '4', '6'], ['Grams', '2,000', '?', '?']])),
          tf('7 kilograms = 700 grams', key=False),
      ]),
      f2=B('Convert masses between kilograms and grams with decimals', '5.MD.A.1', [
          sa('Convert.\n1.8 kilograms = ___ grams', 'Grams:', key='1,800'),
          tf('650 grams = 0.65 kilogram', key=True),
          mc('Convert.\n4,250 grams = ___ kilograms', ['4.25', '42.5', '0.425', '425']),
          sa('A box holds 2.4 kg of nuts. 750 g of the nuts are eaten.\nHow many grams are left?', 'Grams:', key='1,650 grams'),
          tf('3.5 kilograms = 350 grams', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.A.2 (liquid volume) — added in 2.0.0
    S('3.MD.A.2', 'Measure liquid volume in liters with a marked container', num=64,
      main=[
          sa('How many liters of water are in the container?', 'Liters:', key='6 liters', fig=beaker(10, 1, 6, 'L', label_step=2)),
          plot('Shade the container to show 3 liters.', beaker(5, 1, 0, 'L'), key='The container shaded from the bottom up to the 3-liter mark'),
          mc('How many liters of water are in the container?', ['8 liters', '4 liters', '9 liters', '6 liters'], fig=beaker(10, 1, 8, 'L', label_step=2)),
          tf('The container has 9 liters of water.', key=True, fig=beaker(12, 1, 9, 'L', label_step=3)),
          tf('The container has 5 liters of water.', key=False, fig=beaker(8, 1, 4, 'L', label_step=2)),
      ],
      back=[
          B('Read whole numbers on a vertical number line', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='7', fig=nl(0, 10, 1, vertical=True, labels={0: '0', 10: '10'}, pts=[(7, 'A')])),
              tf('On a vertical number line, the numbers get greater going up.', key=True),
              mc('Which number is halfway between 0 and 10 on a number line?', ['5', '2', '8', '10']),
              sa('What number is at point B?', 'B =', key='4', fig=nl(0, 8, 1, vertical=True, labels={0: '0', 8: '8'}, pts=[(4, 'B')])),
              tf('On a vertical number line marked 0, 2, 4, 6, the mark just above 4 is 8.', key=False),
          ]),
          B('Skip-count by 5s, 10s, and 100s', '2.NBT.A.2', [
              sa('Skip-count by 5s.\n20, 25, 30, ___', 'Next:', key='35'),
              tf('Counting by 5s from 0 to 20 takes 4 counts.', key=True),
              mc('Count by 10s.\n70, 80, 90, ___', ['100', '91', '110', '900']),
              sa('Skip-count by 100s from 200.\nWhat is the 4th number?', 'Number:', key='500'),
              tf('Counting by 5s: 45, 50, 60.', key=False),
          ]),
      ],
      f1=B('Express liters as milliliters', '4.MD.A.1', [
          sa('How many milliliters are in 4 liters?', 'Milliliters:', key='4,000 milliliters'),
          tf('2 L 300 mL = 2,300 mL', key=True),
          mc('Which is the same as 6 liters?', ['6,000 mL', '600 mL', '60 mL', '60,000 mL']),
          sa('Complete the table.', 'Missing values:', key='5,000; 7,000', fig=table([['Liters', '1', '5', '7'], ['Milliliters', '1,000', '?', '?']])),
          tf('3 liters = 300 milliliters', key=False),
      ]),
      f2=B('Convert between liters and milliliters with decimals', '5.MD.A.1', [
          sa('Convert.\n2.5 liters = ___ milliliters', 'Milliliters:', key='2,500'),
          tf('350 mL = 0.35 L', key=True),
          mc('Convert.\n1,750 mL = ___ L', ['1.75', '17.5', '0.175', '175']),
          sa('0.6 L is poured out of a full 2-liter bottle.\nHow many milliliters are left?', 'Milliliters:', key='1,400 milliliters'),
          tf('0.8 liter = 80 milliliters', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (picture graph)
    S('3.MD.B.3', 'Draw a scaled picture graph to represent data',
      main=[
          plot('Make a picture graph of the data. Each ● stands for 2 votes.\nApples: 6 votes, Bananas: 10 votes, Grapes: 4 votes',
               blank_picgraph('Favorite fruit', ['Apples', 'Bananas', 'Grapes'], '2 votes'),
               key='Apples: 3 symbols; Bananas: 5 symbols; Grapes: 2 symbols (each ● = 2 votes)'),
          plot('Make a picture graph of the data. Each ● stands for 5 books.\nLeo: 15 books, Mia: 25 books, Sam: 10 books',
               blank_picgraph('Books read', ['Leo', 'Mia', 'Sam'], '5 books'), key='Leo: 3 symbols; Mia: 5 symbols; Sam: 2 symbols (each ● = 5 books)'),
          plot('Make a picture graph of the data. Each ● stands for 3 cars.\nRed: 9 cars, Blue: 12 cars, White: 6 cars, Black: 15 cars',
               blank_picgraph('Car colors', ['Red', 'Blue', 'White', 'Black'], '3 cars'),
               key='Red: 3 symbols; Blue: 4 symbols; White: 2 symbols; Black: 5 symbols (each ● = 3 cars)'),
          plot('Make a picture graph of the data. Each ● stands for 4 students.\nWalk: 16 students, Bus: 24 students, Car: 8 students',
               blank_picgraph('How we get to school', ['Walk', 'Bus', 'Car'], '4 students'),
               key='Walk: 4 symbols; Bus: 6 symbols; Car: 2 symbols (each ● = 4 students)'),
          plot('Make a picture graph of the data. Each ● stands for 10 votes.\nCats: 40 votes, Dogs: 60 votes, Fish: 20 votes, Birds: 30 votes',
               blank_picgraph('Favorite pet', ['Cats', 'Dogs', 'Fish', 'Birds'], '10 votes'),
               key='Cats: 4 symbols; Dogs: 6 symbols; Fish: 2 symbols; Birds: 3 symbols (each ● = 10 votes)'),
      ],
      back=[
          B('Draw a picture graph with a single-unit scale', '2.MD.D.10', [
              plot('Make a picture graph. Draw one ● for each pet.\nDogs: 4, Cats: 3, Birds: 2', blank_picgraph('Pets', ['Dogs', 'Cats', 'Birds'], '1 pet'),
                   key='Dogs: 4 symbols; Cats: 3 symbols; Birds: 2 symbols'),
              plot('Make a picture graph. Draw one ● for each child.\nRed: 3, Blue: 5, Green: 2', blank_picgraph('Favorite color', ['Red', 'Blue', 'Green'], '1 child'),
                   key='Red: 3 symbols; Blue: 5 symbols; Green: 2 symbols'),
              plot('Make a picture graph. Draw one ● for each child.\nApples: 4, Grapes: 1, Pretzels: 3, Carrots: 2',
                   blank_picgraph('Favorite snack', ['Apples', 'Grapes', 'Pretzels', 'Carrots'], '1 child'),
                   key='Apples: 4 symbols; Grapes: 1 symbol; Pretzels: 3 symbols; Carrots: 2 symbols'),
              plot('Make a picture graph. Draw one ● for each day.\nSunny: 5, Rainy: 2, Cloudy: 3', blank_picgraph('Weather', ['Sunny', 'Rainy', 'Cloudy'], '1 day'),
                   key='Sunny: 5 symbols; Rainy: 2 symbols; Cloudy: 3 symbols'),
              plot('Make a picture graph. Draw one ● for each toy.\nBalls: 2, Cars: 4, Blocks: 5, Dolls: 1',
                   blank_picgraph('Toys in the bin', ['Balls', 'Cars', 'Blocks', 'Dolls'], '1 toy'),
                   key='Balls: 2 symbols; Cars: 4 symbols; Blocks: 5 symbols; Dolls: 1 symbol'),
          ]),
          B('Skip-count by 5s and 10s', '2.NBT.A.2', [
              sa('Skip-count by 5s from 5.\nWhat is the 4th number?', 'Number:', key='20'),
              tf('Skip-counting by 10s: 10, 20, 30, 40, 50.', key=True),
              mc('Skip-count by 5s.\n5, 10, 15, 20, ___', ['25', '21', '30', '35']),
              sa('Skip-count by 10s from 10.\nWhat is the 7th number?', 'Number:', key='70'),
              tf('Skip-counting by 5s: 5, 10, 15, 25.', key=False),
          ]),
      ],
      f1=B('Make a line plot of measurements in fractions of a unit', '4.MD.B.4', [
          plot('Make a line plot of the data.\nBean lengths (inches): {1/4}, {1/2}, {1/2}, {3/4}, {1/2}, 1', fline(0, 1, 4),
               key='Line plot: 1 X at 1/4, 3 X\'s at 1/2, 1 X at 3/4, 1 X at 1'),
          plot('Make a line plot of the data.\nFeather lengths (inches): {3/8}, {1/2}, {3/8}, {3/4}', fline(0, 1, 8),
               key='Line plot: 2 X\'s at 3/8, 1 X at 1/2 (4/8), 1 X at 3/4 (6/8)'),
          plot('Make a line plot of the data.\nSeed lengths (inches): {1/4}, {1/4}, {1/2}, {3/4}, {3/4}, {3/4}', fline(0, 1, 4),
               key='Line plot: 2 X\'s at 1/4, 1 X at 1/2, 3 X\'s at 3/4'),
          plot('Make a line plot of the data.\nTwig lengths (inches): 1{1/8}, 1{3/8}, 1{1/8}, 1{1/2}', fline(1, 2, 8),
               key='Line plot: 2 X\'s at 1 1/8, 1 X at 1 3/8, 1 X at 1 1/2 (1 4/8)'),
          plot('Make a line plot of the data.\nAnt lengths (inches): {1/8}, {1/4}, {1/8}, {3/8}, {1/8}', fline(0, 1, 8),
               key='Line plot: 3 X\'s at 1/8, 1 X at 1/4 (2/8), 1 X at 3/8'),
      ]),
      f2=B('Use operations on fractions to solve problems with line plot data', '5.MD.B.2', [
          sa('The line plot shows rainfall on 5 days.\nWhat is the total rainfall?', 'Total:', key='2 1/2 inches', note='20/8 and 5/2 inches are also correct.', fig=RAIN),
          tf('The two days with {1/4} inch of rain had {1/2} inch in all.', key=True, fig=RAIN),
          mc('What is the difference between the greatest and the least rainfall?', ['{5/8} inch', '{3/8} inch', '{7/8} inch', '{1/2} inch'], fig=RAIN),
          sa('If the total rainfall had been spread equally over the 5 days, how much would have fallen each day?', 'Each day:',
             key='1/2 inch', fig=RAIN),
          tf('The total of {1/2}, {1/4}, and {1/8} is {3/14}.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (picture graph key) — added in 2.0.0
    S('3.MD.B.3', 'Use the key of a scaled picture graph to find amounts and numbers of symbols', num=65,
      main=[
          mc('In a picture graph, each ● stands for 5 books. Ty read 20 books.\nHow many ● should be drawn for Ty?', ['4', '20', '5', '15']),
          sa('A picture graph has the key ● = 3 cars. The row for red cars has 5 ●.\nHow many red cars are there?', 'Red cars:', key='15'),
          tf('If ● = 4 students, then 7 ● stand for 28 students.', key=True),
          sa('Data: Dogs 8, Cats 12, Fish 4. You will make a picture graph with ● = 4 pets.\nHow many ● go in each row?', ['Dogs:', 'Cats:', 'Fish:'],
             key='2; 3; 1', note='All three are required.'),
          sa('Use the picture graph.\nHow many books did Leo read?', 'Books:', key='20', fig=BOOKS5),
      ],
      back=[
          B('Read a picture graph with a single-unit scale', '2.MD.D.10', [
              mc('Use the picture graph.\nHow many children chose soccer?', ['4', '3', '2', '5'], fig=SPORT_PICS),
              sa('Use the picture graph.\nHow many more children chose swim than tennis?', 'More:', key='1', fig=SPORT_PICS),
              tf('In the picture graph, tennis has the most votes.', key=False, fig=SPORT_PICS),
              tf('In a picture graph where ● = 1 child, 5 ● stand for 5 children.', key=True),
              sa('Use the picture graph.\nHow many children chose soccer or tennis?', 'Children:', key='6', fig=SPORT_PICS),
          ]),
          B('Add equal addends', '2.OA.C.4', [
              sa('Add.\n5 + 5 + 5 + 5', 'Sum:', key='20'),
              tf('3 + 3 + 3 = 9', key=True),
              mc('2 + 2 + 2 + 2 + 2 = ?', ['10', '8', '12', '5']),
              sa('Add.\n4 + 4 + 4', 'Sum:', key='12'),
              tf('5 + 5 + 5 = 20', key=False),
          ]),
      ],
      f1=B('Use a picture graph to solve multiplicative comparison problems', '4.OA.A.2', nearest=True, qs=[
          sa('Use the picture graph.\nHow many times as many cans did Room A collect as Room B?', 'Times as many:', key='3 times', fig=ROOMS),
          tf('Use the picture graph. Room C collected 2 times as many cans as Room B.', key=True, fig=ROOMS),
          mc('Use the picture graph.\nWhich room collected 3 times as many cans as Room B?', ['Room A', 'Room B', 'Room C', 'None of the rooms'], fig=ROOMS),
          sa('Room D collected 4 times as many cans as Room B. Use the picture graph.\nHow many cans did Room D collect?', 'Cans:', key='40', fig=ROOMS),
          tf('Use the picture graph. Room A collected 2 times as many cans as Room C.', key=False, fig=ROOMS),
      ]),
      f2=B('Use operations on fractions to solve problems with line plot data', '5.MD.B.2', nearest=True, qs=[
          sa('The line plot shows the paint in some cans.\nWhat is the total amount of paint?', 'Total:', key='2 3/4 liters', note='11/4 liters is also correct.',
             fig=PAINT),
          tf('The three {1/4}-liter cans hold {3/4} liter in all.', key=True, fig=PAINT),
          mc('How much more paint is in a {3/4}-liter can than in a {1/4}-liter can?', ['{1/2} liter', '1 liter', '{1/4} liter', '{3/4} liter'], fig=PAINT),
          sa('The paint in the two {3/4}-liter cans is poured together.\nHow much paint is that?', 'Paint:', key='1 1/2 liters', fig=PAINT),
          tf('The {1/2}-liter can and one {1/4}-liter can hold 1 liter in all.', key=False, fig=PAINT),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (bar graph)
    S('3.MD.B.3', 'Draw a scaled bar graph to represent data',
      main=[
          plot('Make a bar graph of the data. The scale counts by 2s.\nRed: 8, Blue: 12, Green: 6, Yellow: 10',
               bargraph(['Red', 'Blue', 'Green', 'Yellow'], [0, 0, 0, 0], 2, 'Number of students', ymax=14),
               key='Bars that reach 8 for Red, 12 for Blue, 6 for Green, and 10 for Yellow'),
          plot('Make a bar graph of the data. The scale counts by 5s.\nApples: 15, Pears: 25, Plums: 10',
               bargraph(['Apples', 'Pears', 'Plums'], [0, 0, 0], 5, 'Number of fruits', ymax=30),
               key='Bars that reach 15 for Apples, 25 for Pears, and 10 for Plums'),
          plot('Make a bar graph of the data. The scale counts by 10s.\nMon: 30, Tue: 50, Wed: 20, Thu: 40',
               bargraph(['Mon', 'Tue', 'Wed', 'Thu'], [0, 0, 0, 0], 10, 'Number of visitors', ymax=60),
               key='Bars that reach 30 for Mon, 50 for Tue, 20 for Wed, and 40 for Thu'),
          plot('Make a bar graph of the data. The scale counts by 2s.\nSoccer: 6, Tennis: 4, Swim: 10, Golf: 2',
               bargraph(['Soccer', 'Tennis', 'Swim', 'Golf'], [0, 0, 0, 0], 2, 'Number of students', ymax=12),
               key='Bars that reach 6 for Soccer, 4 for Tennis, 10 for Swim, and 2 for Golf'),
          plot('Make a bar graph of the data. The scale counts by 5s.\nCats: 20, Dogs: 35, Birds: 15',
               bargraph(['Cats', 'Dogs', 'Birds'], [0, 0, 0], 5, 'Number of votes', ymax=40),
               key='Bars that reach 20 for Cats, 35 for Dogs, and 15 for Birds'),
      ],
      back=[
          B('Draw a bar graph with a single-unit scale', '2.MD.D.10', [
              plot('Make a bar graph.\nApples: 4, Pears: 2, Plums: 5', bargraph(['Apples', 'Pears', 'Plums'], [0, 0, 0], 1, 'Number of fruits', ymax=6),
                   key='Bars that reach 4 for Apples, 2 for Pears, and 5 for Plums'),
              plot('Make a bar graph.\nCats: 3, Dogs: 5, Fish: 2', bargraph(['Cats', 'Dogs', 'Fish'], [0, 0, 0], 1, 'Number of pets', ymax=6),
                   key='Bars that reach 3 for Cats, 5 for Dogs, and 2 for Fish'),
              plot('Make a bar graph.\nApples: 2, Bananas: 4, Pears: 1, Plums: 3',
                   bargraph(['Apples', 'Bananas', 'Pears', 'Plums'], [0, 0, 0, 0], 1, 'Number of children', ymax=5),
                   key='Bars that reach 2 for Apples, 4 for Bananas, 1 for Pears, and 3 for Plums'),
              plot('Make a bar graph.\nMon: 4, Tue: 6, Wed: 3', bargraph(['Mon', 'Tue', 'Wed'], [0, 0, 0], 1, 'Books read', ymax=6),
                   key='Bars that reach 4 for Mon, 6 for Tue, and 3 for Wed'),
              plot('Make a bar graph.\nWeek 1: 2, Week 2: 5, Week 3: 3, Week 4: 1',
                   bargraph(['Week 1', 'Week 2', 'Week 3', 'Week 4'], [0, 0, 0, 0], 1, 'Rainy days', ymax=6),
                   key='Bars that reach 2 for Week 1, 5 for Week 2, 3 for Week 3, and 1 for Week 4'),
          ]),
          B('Read whole numbers on a number line scale', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='15', fig=nl(0, 20, 5, labels={0: '0', 10: '10', 20: '20'}, pts=[(15, 'A')])),
              tf('On a number line that counts by 10s, 30 comes right after 20.', key=True),
              mc('A number line counts by 2s: 0, 2, 4, 6, 8.\nWhat number is halfway between 4 and 6?', ['5', '3', '7', '10']),
              sa('What number is at point B?', 'B =', key='30', fig=nl(0, 50, 10, labels={0: '0', 50: '50'}, pts=[(30, 'B')])),
              tf('On a number line that counts by 5s, the mark after 25 is 35.', key=False),
          ]),
      ],
      f1=B('Use a bar graph to solve multiplicative comparison problems', '4.OA.A.2', nearest=True, qs=[
          sa('Use the bar graph.\nHow many times as many students chose soccer as chose golf?', 'Times as many:', key='4 times', fig=SPORTS),
          tf('Use the bar graph. Twice as many students chose swim as chose golf.', key=False, fig=SPORTS),
          mc('Use the bar graph.\nWhich sport was chosen by 3 times as many students as golf?', ['Swim', 'Tennis', 'Soccer', 'Golf'], fig=SPORTS),
          sa('Use the bar graph.\nHow many times as many students chose soccer as chose tennis?', 'Times as many:', key='2 times', fig=SPORTS),
          tf('Use the bar graph. Soccer was chosen by 4 times as many students as golf.', key=True, fig=SPORTS),
      ]),
      f2=B('Graph data as points in the first quadrant', '5.G.A.2', nearest=True, qs=[
          plot('A plant grows 2 cm each week. Graph the points (week, height): (0, 0), (1, 2), (2, 4), and (3, 6).',
               grid(4, 8, xlabel='Week', ylabel='Height (cm)'), key='Points plotted at (0, 0), (1, 2), (2, 4), and (3, 6)'),
          tf('On the graph, the point (2, 4) shows a height of 4 cm in week 2.', key=True,
             fig=grid(4, 8, xlabel='Week', ylabel='Height (cm)', pts=[(2, 4)])),
          mc('A store sells 5 hats each day.\nWhich point (days, hats) shows the total sold after 3 days?', ['(3, 15)', '(15, 3)', '(3, 5)', '(5, 3)']),
          sa('Use the graph.\nWhat is the height in week 3?', 'Height:', key='9 cm',
             fig=grid(4, 12, ystep=3, xlabel='Week', ylabel='Height (cm)', pts=[(1, 3), (2, 6), (3, 9)])),
          tf('On a graph with x = days and y = hats sold, the point (4, 0) means 0 days and 4 hats sold.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (bar graph scale) — added in 2.0.0
    S('3.MD.B.3', 'Read the scale of a scaled bar graph and choose a scale', num=66,
      main=[
          mc('A bar graph has a scale that counts by 2s. A bar ends halfway between 6 and 8.\nWhat number does the bar show?', ['7', '6', '8', '14']),
          tf('On a bar graph with a scale that counts by 10s, a bar for 40 ends on the fourth line above 0.', key=True),
          sa('Which scale is better for a bar graph of 10, 25, 40, and 35: counting by 1s or counting by 5s? Explain.', ['Scale:', 'Explanation:'],
             key='Counting by 5s',
             note='All the numbers are multiples of 5 and go up to 40, so counting by 5s fits them with fewer lines. Both parts are required.'),
          tf('On a bar graph with a scale that counts by 2s, a bar for 9 ends exactly on a labeled line.', key=False),
          sa('Use the bar graph.\nHow many students chose blue?', 'Students:', key='12', fig=FRUIT_BARS),
      ],
      back=[
          B('Read a bar graph with a single-unit scale', '2.MD.D.10', [
              tf('In a bar graph, a taller bar shows a greater number.', key=True),
              mc('Use the bar graph.\nHow many children chose red?', ['5', '4', '3', '6'], fig=COLORS),
              sa('Use the bar graph.\nHow many more children chose red than blue?', 'More:', key='2', fig=COLORS),
              tf('In the bar graph, green has the most votes.', key=False, fig=COLORS),
              sa('Use the bar graph.\nHow many children chose green?', 'Children:', key='4', fig=COLORS),
          ]),
          B('Skip-count by 5s, 10s, and 100s along a scale', '2.NBT.A.2', [
              sa('Skip-count by 10s from 0.\nWhat is the 5th number after 0?', 'Number:', key='50'),
              tf('Counting by 5s: 0, 5, 10, 15, 20.', key=True),
              mc('A scale counts by 5s.\nWhat number comes after 25?', ['30', '26', '35', '50']),
              sa('Skip-count by 100s.\n100, 200, ___, ___', 'Next two:', key='300, 400'),
              tf('Counting by 10s: 60, 70, 90.', key=False),
          ]),
      ],
      f1=B('Read a line plot whose scale is marked in eighths', '4.MD.B.4', [
          sa('Use the line plot.\nHow many bolts are {5/8} inch long?', 'Bolts:', key='3', fig=BOLTS),
          tf('Use the line plot. 2 bolts are {3/8} inch long.', key=True, fig=BOLTS),
          mc('Use the line plot.\nHow long is the longest bolt?', ['{7/8} inch', '{5/8} inch', '1 inch', '{3/8} inch'], fig=BOLTS),
          sa('Use the line plot.\nHow many bolts were measured?', 'Bolts:', key='7', fig=BOLTS),
          tf('Use the line plot. No bolt is {1/8} inch long.', key=False, fig=BOLTS),
      ]),
      f2=B('Read and interpret points on a graph with a scale', '5.G.A.2', nearest=True, qs=[
          sa('The graph shows a bike ride.\nHow many miles were ridden after 3 hours?', 'Miles:', key='15 miles', fig=MILES),
          tf('On the graph, the point (2, 10) means 10 miles after 2 hours.', key=True, fig=MILES),
          mc('What does the point (4, 20) mean on the graph?', ['After 4 hours, the distance is 20 miles.', 'After 20 hours, the distance is 4 miles.',
                                                               'The distance is 4 miles more than 20.', 'The ride is 24 miles long.'], fig=MILES),
          sa('How many more miles were ridden after 4 hours than after 1 hour?', 'Miles:', key='15 miles', fig=MILES),
          tf('On the graph, the point (1, 5) means 1 mile after 5 hours.', key=False, fig=MILES),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (solve with graphs)
    S('3.MD.B.3', 'Solve "how many more" and "how many less" problems using scaled bar graphs and picture graphs',
      main=[
          sa('Use the bar graph.\nHow many more books were read on Wednesday than on Tuesday?', 'More:', key='12', fig=BOOKS),
          sa('Use the bar graph.\nHow many books were read on Monday and Thursday together?', 'Books:', key='26', fig=BOOKS),
          mc('Use the bar graph.\nHow many fewer books were read on Thursday than on Wednesday?', ['8', '12', '32', '6'], fig=BOOKS),
          tf('Use the picture graph. Ana picked 6 more apples than Ben.', key=True, fig=APPLES),
          sa('Use the picture graph.\nHow many apples did the three children pick in all?', 'Apples:', key='36', fig=APPLES),
      ],
      back=[
          B('Solve compare problems with a single-unit bar graph', '2.MD.D.10', [
              sa('Use the bar graph.\nHow many more dogs are there than cats?', 'More:', key='3', fig=PETS),
              tf('Use the bar graph. There are 13 pets in all.', key=True, fig=PETS),
              mc('Use the bar graph.\nHow many fewer fish are there than dogs?', ['5', '9', '2', '7'], fig=PETS),
              sa('Use the bar graph.\nHow many cats and fish are there together?', 'Pets:', key='6', fig=PETS),
              tf('Use the bar graph. There are 3 more fish than cats.', key=False, fig=PETS),
          ]),
          B('Solve compare word problems within 100', '2.OA.A.1', [
              sa('Ty has 45 cards. Al has 28 cards.\nHow many more cards does Ty have?', 'More:', key='17'),
              tf('A red ribbon is 50 cm long and a blue ribbon is 35 cm long. The red ribbon is 15 cm longer.', key=True),
              mc('A school has 62 boys and 48 girls.\nHow many fewer girls than boys are there?', ['14', '24', '110', '16']),
              sa('Kim read 33 pages. Jo read 19 more pages than Kim.\nHow many pages did Jo read?', 'Pages:', key='52'),
              tf('Ann has 70 stamps. Bo has 25 fewer stamps than Ann. Bo has 95 stamps.', key=False),
          ]),
      ],
      f1=B('Solve problems with data in a line plot of fractional measurements', '4.MD.B.4', [
          sa('The line plot shows leaf lengths.\nWhat is the difference between the longest and the shortest leaf?', 'Difference:', key='5/8 inch',
             fig=LEAVES),
          tf('The two {3/8}-inch leaves have a total length of {6/8} inch.', key=True, fig=LEAVES),
          mc('How many leaves are longer than {3/8} inch?', ['3', '2', '4', '1'], fig=LEAVES),
          sa('What is the total length of the two {1/2}-inch leaves?', 'Total:', key='1 inch', fig=LEAVES),
          tf('The shortest leaf is {1/4} inch long.', key=False, fig=LEAVES),
      ]),
      f2=B('Find totals, differences, and equal shares of line plot data', '5.MD.B.2', [
          sa('The line plot shows the water in 5 cups.\nWhat is the total amount of water?', 'Total:', key='1 1/2 liters', note='12/8 and 3/2 liters are also correct.',
             fig=WATER),
          tf('If all the water were poured into one jug, the jug would hold 1{1/2} liters.', key=True, fig=WATER),
          mc('If the water were shared equally among the 5 cups, how much would each cup hold?',
             ['{3/10} liter', '{1/4} liter', '1{1/2} liters', '{1/5} liter'], fig=WATER),
          sa('How much more water is in the fullest cup than in the cup with the least water?', 'More:', key='3/8 liter', fig=WATER),
          tf('The two cups with {1/4} liter hold {1/8} liter in all.', key=False, fig=WATER),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (two-step comparisons) — added in 2.0.0
    S('3.MD.B.3', 'Solve two-step "how many more" and "how many fewer" problems using scaled bar graphs', num=62,
      main=[
          sa('Use the bar graph.\nHow many more cans were collected on Monday and Thursday together than on Tuesday?', 'More:', key='22', fig=CANS,
             note='16 + 12 = 28 and 28 - 6 = 22.'),
          sa('Use the bar graph.\nHow many fewer cans were collected on Tuesday and Wednesday together than on Monday and Thursday together?', 'Fewer:',
             key='12', fig=CANS, note='6 + 10 = 16, 16 + 12 = 28, and 28 - 16 = 12.'),
          mc('Use the bar graph.\nHow many more red and green beads are there together than blue and yellow beads together?', ['25', '20', '95', '10'], fig=BEADS),
          tf('Use the bar graph. There are 10 more blue and yellow beads together than red beads.', key=True, fig=BEADS),
          sa('Use the bar graph. 10 more red beads are added.\nThen how many more red beads than blue beads are there?', 'More:', key='20', fig=BEADS),
      ],
      back=[
          B('Solve compare problems with a single-unit bar graph', '2.MD.D.10', [
              sa('Use the bar graph.\nHow many more dogs are there than birds?', 'More:', key='5', fig=HOME_PETS),
              tf('Use the bar graph. There are 3 fewer cats than dogs.', key=True, fig=HOME_PETS),
              mc('Use the bar graph.\nHow many fish and birds are there together?', ['9', '3', '8', '11'], fig=HOME_PETS),
              sa('Use the bar graph.\nHow many fewer cats are there than fish?', 'Fewer:', key='1', fig=HOME_PETS),
              tf('Use the bar graph. There are 4 more fish than birds.', key=False, fig=HOME_PETS),
          ]),
          B('Solve two-step addition and subtraction word problems within 100', '2.OA.A.1', [
              sa('Jo has 24 shells and Al has 18 shells. Kim has 50 shells.\nHow many more shells does Kim have than Jo and Al together?', 'More:', key='8'),
              tf('A class read 25 books in June. In July it read 15 more books than in June. It read 40 books in July.', key=True),
              mc('A shop had 65 hats. It sold 20 in the morning and 18 in the afternoon.\nHow many hats are left?', ['27', '47', '103', '45']),
              sa('A team scored 34 points in game 1 and 29 points in game 2. Another team scored 70 points in all.\nHow many more points did the other team score?',
                 'More:', key='7'),
              tf('Ana had 40 cents. She spent 15 cents and then got 20 cents. She has 35 cents.', key=False),
          ]),
      ],
      f1=B('Solve two-step problems with fractional data in a line plot', '4.MD.B.4', [
          sa('Use the line plot.\nHow much more do the three {1/2}-pound snacks weigh together than the two {1/4}-pound snacks together?', 'More:',
             key='1 pound', fig=SNACKS),
          tf('Use the line plot. The {3/4}-pound snack and one {1/4}-pound snack together weigh 1 pound.', key=True, fig=SNACKS),
          mc('Use the line plot.\nWhat is the total weight of all the snacks?', ['2{3/4} pounds', '2{1/4} pounds', '6 pounds', '3 pounds'], fig=SNACKS),
          sa('Use the line plot.\nHow many more snacks weigh {1/2} pound or more than weigh {1/4} pound?', 'More:', key='2', fig=SNACKS),
          tf('Use the line plot. The two {1/4}-pound snacks together weigh more than the {3/4}-pound snack.', key=False, fig=SNACKS),
      ]),
      f2=B('Solve multistep problems with fractional data in a line plot', '5.MD.B.2', [
          sa('Use the line plot.\nHow much more rain fell on the two {1/2}-inch days together than on the two {1/8}-inch days together?', 'More:',
             key='3/4 inch', fig=RAIN6),
          tf('If the total rain were spread equally over the 6 days, each day would get {5/12} inch.', key=True, fig=RAIN6),
          mc('Use the line plot.\nHow much more rain fell on the wettest day than on the two driest days together?',
             ['{5/8} inch', '{3/4} inch', '{7/8} inch', '{1/8} inch'], fig=RAIN6),
          sa('Use the line plot.\nWhat is the total rainfall?', 'Total:', key='2 1/2 inches', note='20/8 and 5/2 inches are also correct.', fig=RAIN6),
          tf('Use the line plot. The {3/8}-inch day and the {7/8}-inch day together had 1 inch of rain.', key=False, fig=RAIN6),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.4 (measure)
    S('3.MD.B.4', 'Measure lengths to the nearest half inch and quarter inch',
      main=[
          sa('How long is the pencil, to the nearest quarter inch?', 'Length:', key='3 1/4 inches', fig=ruler(5, (0, 3.25), 'pencil')),
          sa('How long is the leaf, to the nearest half inch?', 'Length:', key='2 1/2 inches', fig=ruler(4, (0, 2.5), 'leaf', div=2)),
          mc('How long is the crayon, to the nearest quarter inch?', ['2{3/4} inches', '3{3/4} inches', '2{1/2} inches', '3 inches'],
             fig=ruler(4, (0, 2.75), 'crayon')),
          tf('The key is 1{1/2} inches long.', key=True, fig=ruler(3, (0, 1.5), 'key')),
          tf('The straw is 4{1/4} inches long.', key=False, fig=ruler(5, (0, 4.5), 'straw')),
      ],
      back=[
          B('Measure lengths in whole inches and centimeters', '2.MD.A.1', [
              sa('How long is the eraser?', 'Length:', key='3 inches', fig=ruler(5, (0, 3), 'eraser', div=1)),
              tf('A ruler can show inches or centimeters.', key=True),
              mc('How long is the clip?', ['2 inches', '3 inches', '1 inch', '4 inches'], fig=ruler(4, (0, 2), 'clip', div=1)),
              sa('A string goes from 0 to 6 on a centimeter ruler.\nHow long is it?', 'Length:', key='6 cm'),
              tf('A nail that reaches from 0 to 5 on an inch ruler is 4 inches long.', key=False),
          ]),
          B('Measure length by laying same-size units end to end', '1.MD.A.2', [
              sa('A pencil is as long as 5 paper clips laid end to end.\nHow many paper clips long is it?', 'Paper clips:', key='5'),
              tf('When you measure with paper clips, there should be no gaps or overlaps.', key=True),
              mc('Which shows a pencil measured correctly with paper clips?',
                 ['Clips laid end to end with no gaps or overlaps', 'Clips with spaces between them', 'Clips that overlap', 'Clips placed in a pile']),
              sa('Same-size tiles are laid end to end along a book with no gaps or overlaps. 9 tiles fit exactly.\nHow many tiles long is the book?',
                 'Tiles:', key='9'),
              tf('If the paper clips overlap when you measure, the count is still correct.', key=False),
          ]),
      ],
      f1=B('Add mixed-number lengths in word problems', '4.NF.B.3.d', [
          sa('A pencil is 3{1/4} inches long and a crayon is 2{3/4} inches long.\nHow long are they laid end to end?', 'Length:', key='6 inches'),
          tf('Ribbons of 2{2/4} inches and 1{3/4} inches laid end to end are 4{1/4} inches long.', key=True),
          mc('A snail crawls 1{1/4} inches and then 2{2/4} inches.\nHow far does it crawl in all?', ['3{3/4} inches', '3{1/4} inches', '1{1/4} inches', '4 inches']),
          sa('Three sticks are {2/4} inch, {3/4} inch, and {1/4} inch long.\nWhat is their total length?', 'Length:', key='1 2/4 inches',
             note='1 1/2 inches and 6/4 inches are also correct.'),
          tf('Three beads that are each {3/4} inch long, in a row, are 2 inches long.', key=False),
      ]),
      f2=B('Convert inches, feet, and yards with fractions', '5.MD.A.1', [
          sa('How many feet is 30 inches?', 'Feet:', key='2 1/2 feet', note='2.5 feet is also correct.'),
          tf('18 inches = 1{1/2} feet', key=True),
          mc('How many inches are in 2{1/4} feet?', ['27', '24', '29', '25']),
          sa('A board is 1{3/4} yards long.\nHow many feet is that?', 'Feet:', key='5 1/4 feet'),
          tf('9 inches = {3/4} yard', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.4 (line plot)
    S('3.MD.B.4', 'Make a line plot of measurement data in whole numbers, halves, or quarters',
      main=[
          plot('Make a line plot of the data.\nPencil lengths (inches): 4, 4{1/2}, 5, 4{1/2}, 4{1/4}, 4{1/2}', fline(4, 5, 4),
               key='Line plot: 1 X at 4, 1 X at 4 1/4, 3 X\'s at 4 1/2, 1 X at 5'),
          plot('Make a line plot of the data.\nShell lengths (inches): 2, 2{1/2}, 2{1/2}, 3, 2{1/2}', fline(2, 3, 2),
               key='Line plot: 1 X at 2, 3 X\'s at 2 1/2, 1 X at 3'),
          plot('Make a line plot of the data.\nWorm lengths (inches): 1{1/4}, 1{1/2}, 1{3/4}, 1{1/2}, 2', fline(1, 2, 4),
               key='Line plot: 1 X at 1 1/4, 2 X\'s at 1 1/2, 1 X at 1 3/4, 1 X at 2'),
          plot('Make a line plot of the data.\nLeaf lengths (inches): {1/4}, {1/2}, {1/2}, {3/4}, {3/4}, {1/2}, 1', fline(0, 1, 4),
               key='Line plot: 1 X at 1/4, 3 X\'s at 1/2, 2 X\'s at 3/4, 1 X at 1'),
          plot('Make a line plot of the data.\nRibbon lengths (inches): 3, 3{1/2}, 4, 3, 3{1/2}, 3', fline(3, 4, 2),
               key='Line plot: 3 X\'s at 3, 2 X\'s at 3 1/2, 1 X at 4'),
      ],
      back=[
          B('Make a line plot of whole-number lengths', '2.MD.D.9', [
              plot('Make a line plot of the data.\nLengths (inches): 5, 6, 6, 8, 6', nl(4, 9, 1), key='Line plot: 1 X at 5, 3 X\'s at 6, 1 X at 8'),
              tf('A line plot shows each measurement as an X above a number line.', key=True),
              mc('Which number line fits a line plot of 3, 4, 4, and 7?',
                 ['A number line from 0 to 10', 'A number line from 10 to 20', 'A number line from 0 to 4', 'A number line from 5 to 9']),
              sa('Lengths (cm): 9, 10, 10, 12\nIn a line plot of the data, how many X\'s go above 10?', 'X\'s:', key='2'),
              tf('A line plot of 2, 2, 2, and 3 has 2 X\'s above 2.', key=False),
          ]),
          B('Whole numbers on a number line', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='7', fig=nl(0, 10, 1, labels={0: '0', 10: '10'}, pts=[(7, 'A')])),
              tf('On a number line, numbers get greater to the right.', key=True),
              mc('Which number is between 4 and 6 on a number line?', ['5', '3', '7', '10']),
              sa('What number is at point B?', 'B =', key='12', fig=nl(10, 20, 1, labels={10: '10', 20: '20'}, pts=[(12, 'B')])),
              tf('On a number line, 9 is to the left of 6.', key=False),
          ]),
      ],
      f1=B('Make a line plot of measurements in halves, fourths, and eighths', '4.MD.B.4', [
          plot('Make a line plot of the data.\nScrew lengths (inches): {3/8}, {1/2}, {3/8}, {5/8}, {3/4}, {3/8}', fline(0, 1, 8),
               key='Line plot: 3 X\'s at 3/8, 1 X at 1/2, 1 X at 5/8, 1 X at 3/4'),
          plot('Make a line plot of the data.\nWire lengths (inches): {5/8}, {3/4}, {5/8}, {7/8}', fline(0, 1, 8),
               key='Line plot: 2 X\'s at 5/8, 1 X at 3/4 (6/8), 1 X at 7/8'),
          plot('Make a line plot of the data.\nNail lengths (inches): {1/4}, {2/8}, {3/8}, {1/4}', fline(0, 1, 8),
               key='Line plot: 3 X\'s at 1/4 (2/8), 1 X at 3/8'),
          plot('Make a line plot of the data.\nBead sizes (inches): {1/8}, {1/4}, {1/4}, {1/2}', fline(0, 1, 8),
               key='Line plot: 1 X at 1/8, 2 X\'s at 1/4, 1 X at 1/2'),
          plot('Make a line plot of the data.\nClip lengths (inches): 1, {7/8}, {3/4}, {7/8}', fline(0, 1, 8),
               key='Line plot: 1 X at 3/4 (6/8), 2 X\'s at 7/8, 1 X at 1'),
      ]),
      f2=B('Use operations on fractions to solve problems with line plot data', '5.MD.B.2', [
          sa('The line plot shows the juice in 4 glasses.\nWhat is the total amount of juice?', 'Total:', key='2 cups', fig=JUICE),
          tf('If the juice were shared equally among the 4 glasses, each glass would hold {1/2} cup.', key=True, fig=JUICE),
          mc('How much more juice is in the fullest glass than in the emptiest glass?', ['{1/2} cup', '{1/4} cup', '{3/4} cup', '1 cup'], fig=JUICE),
          sa('The juice in the two {1/2}-cup glasses is poured together.\nHow much juice is that?', 'Juice:', key='1 cup', fig=JUICE),
          tf('The glasses with less than {1/2} cup hold {3/4} cup in all.', key=False, fig=JUICE),
      ])),
    # ------------------------------------------------------------------ 3.MD.B.4 (measure, then plot) — added in 2.0.0
    S('3.MD.B.4', 'Measure several objects to the nearest half or quarter inch and make a line plot of the measurements', num=69,
      main=[
          draw_write('Measure each ribbon to the nearest quarter inch. Write the lengths.\nThen make a line plot of your measurements on the number line.',
                     dict(k='vstack', prop=True, figs=[ruler(4, objs=[(0, 2.25, 'A'), (0, 2.5, 'B'), (0, 2.25, 'C'), (0, 3, 'D')]), fline(2, 3, 4)],
                          desc='An inch ruler from 0 to 4 marked every 1/4 inch, with four ribbons above it that start at 0: A ends at 2 1/4, '
                               'B at 2 1/2, C at 2 1/4, and D at 3. Below is an empty number line from 2 to 3 marked in fourths for the line plot.'),
                     'Lengths:', draw='Line plot: 2 X\'s at 2 1/4, 1 X at 2 1/2, 1 X at 3',
                     key='A: 2 1/4 in., B: 2 1/2 in., C: 2 1/4 in., D: 3 in.',
                     note='Grade the parts separately: each measured length, then a line plot that matches the student\'s own lengths.'),
          draw_write('Measure each crayon to the nearest quarter inch. Write the lengths.\nThen make a line plot of your measurements on the number line.',
                     dict(k='vstack', prop=True, figs=[ruler(5, objs=[(0, 3.5, 'A'), (0, 3.75, 'B'), (0, 3.5, 'C'), (0, 4, 'D')]), fline(3, 4, 4)],
                          desc='An inch ruler from 0 to 5 marked every 1/4 inch, with four crayons above it that start at 0: A ends at 3 1/2, '
                               'B at 3 3/4, C at 3 1/2, and D at 4. Below is an empty number line from 3 to 4 marked in fourths for the line plot.'),
                     'Lengths:', draw='Line plot: 2 X\'s at 3 1/2, 1 X at 3 3/4, 1 X at 4',
                     key='A: 3 1/2 in., B: 3 3/4 in., C: 3 1/2 in., D: 4 in.',
                     note='Grade the parts separately: each measured length, then a line plot that matches the student\'s own lengths.'),
          draw_write('Measure each nail to the nearest half inch. Write the lengths.\nThen make a line plot of your measurements on the number line.',
                     dict(k='vstack', prop=True, figs=[ruler(3, objs=[(0, 1.5, 'A'), (0, 2, 'B'), (0, 1.5, 'C'), (0, 2.5, 'D')], div=2), fline(1, 3, 2)],
                          desc='An inch ruler from 0 to 3 marked every 1/2 inch, with four nails above it that start at 0: A ends at 1 1/2, '
                               'B at 2, C at 1 1/2, and D at 2 1/2. Below is an empty number line from 1 to 3 marked in halves for the line plot.'),
                     'Lengths:', draw='Line plot: 2 X\'s at 1 1/2, 1 X at 2, 1 X at 2 1/2',
                     key='A: 1 1/2 in., B: 2 in., C: 1 1/2 in., D: 2 1/2 in.',
                     note='Grade the parts separately: each measured length, then a line plot that matches the student\'s own lengths.'),
          sa('Measure each shell to the nearest quarter inch.\nIn a line plot of these lengths, how many X\'s go above 1{3/4}?', ['Lengths:', 'X\'s above 1 3/4:'],
             key='A: 1 3/4 in., B: 1 1/2 in., C: 1 3/4 in.; 2', fig=ruler(3, objs=[(0, 1.75, 'A'), (0, 1.5, 'B'), (0, 1.75, 'C')]),
             note='Grade the lengths and the count separately.'),
          tf('Measured to the nearest half inch, the sticks are 2, 2{1/2}, and 3 inches long, so a line plot of them has one X at each of those lengths.',
             key=True, fig=ruler(4, objs=[(0, 2, 'A'), (0, 2.5, 'B'), (0, 3, 'C')], div=2)),
      ],
      back=[
          B('Measure objects in whole inches and make a line plot', '2.MD.D.9', [
              draw_write('Measure each stick to the nearest inch. Write the lengths.\nThen make a line plot of the lengths.',
                         dict(k='vstack', prop=True, figs=[ruler(6, objs=[(0, 3, 'A'), (0, 5, 'B'), (0, 3, 'C')], div=1), nl(0, 6, 1)],
                              desc='An inch ruler from 0 to 6 with three sticks above it that start at 0: A ends at 3, B at 5, and C at 3. '
                                   'Below is an empty number line from 0 to 6 for the line plot.'),
                         'Lengths:', draw='Line plot: 2 X\'s at 3, 1 X at 5', key='A: 3 in., B: 5 in., C: 3 in.',
                         note='Grade the parts separately: each length, then a line plot that matches the student\'s own lengths.'),
              tf('A line plot of 4, 4, and 6 inches has two X\'s above 4.', key=True),
              mc('Lengths: 2, 3, 3, 3, and 5 inches.\nIn a line plot, how many X\'s go above 3?', ['3', '2', '1', '5']),
              sa('How long is the ribbon, to the nearest inch?', 'Length:', key='4 inches', fig=ruler(6, (0, 4), 'ribbon', div=1)),
              tf('A line plot of 5, 6, and 6 inches has one X above 6.', key=False),
          ]),
          B('Measure lengths in whole inches', '2.MD.A.1', [
              sa('How long is the crayon?', 'Length:', key='5 inches', fig=ruler(6, (0, 5), 'crayon', div=1)),
              tf('An object that starts at 0 and ends at 3 on an inch ruler is 3 inches long.', key=True),
              mc('How long is the key?', ['2 inches', '3 inches', '1 inch', '4 inches'], fig=ruler(4, (0, 2), 'key', div=1)),
              sa('A comb reaches from 0 to 6 on an inch ruler.\nHow long is it?', 'Length:', key='6 inches'),
              tf('A spoon that reaches from 0 to 5 on an inch ruler is 6 inches long.', key=False),
          ]),
      ],
      f1=B('Make a line plot of eighth-inch data and find the difference between the longest and shortest', '4.MD.B.4', [
          draw_write('Make a line plot of the data. Then find the difference between the longest and the shortest bead.\n'
                     'Bead lengths (inches): {1/8}, {3/8}, {3/8}, {5/8}, {1/2}', fline(0, 1, 8), 'Difference:',
                     draw='Line plot: 1 X at 1/8, 2 X\'s at 3/8, 1 X at 1/2, 1 X at 5/8', key='1/2 inch', note='4/8 inch is also correct. Grade both.'),
          draw_write('Make a line plot of the data. Then find the difference between the longest and the shortest pin.\n'
                     'Pin lengths (inches): {3/4}, {7/8}, {3/4}, 1', fline(0, 1, 8), 'Difference:',
                     draw='Line plot: 2 X\'s at 3/4, 1 X at 7/8, 1 X at 1', key='1/4 inch', note='2/8 inch is also correct. Grade both.'),
          draw_write('Make a line plot of the data. Then find the difference between the longest and the shortest seed.\n'
                     'Seed lengths (inches): {1/4}, {1/8}, {1/4}, {1/2}', fline(0, 1, 8), 'Difference:',
                     draw='Line plot: 1 X at 1/8, 2 X\'s at 1/4, 1 X at 1/2', key='3/8 inch', note='Grade both.'),
          draw_write('Make a line plot of the data. Then find the difference between the longest and the shortest wire.\n'
                     'Wire lengths (inches): {5/8}, {5/8}, {3/4}, {7/8}', fline(0, 1, 8), 'Difference:',
                     draw='Line plot: 2 X\'s at 5/8, 1 X at 3/4, 1 X at 7/8', key='1/4 inch', note='2/8 inch is also correct. Grade both.'),
          draw_write('Make a line plot of the data. Then find the difference between the longest and the shortest twig.\n'
                     'Twig lengths (inches): {1/2}, {3/8}, {1/2}, {1/8}, {1/2}', fline(0, 1, 8), 'Difference:',
                     draw='Line plot: 1 X at 1/8, 1 X at 3/8, 3 X\'s at 1/2', key='3/8 inch', note='Grade both.'),
      ]),
      f2=B('Make a line plot of fractional data and find the total', '5.MD.B.2', [
          draw_write('Make a line plot of the data. Then find the total.\nJuice in each glass (cups): {1/4}, {1/2}, {1/2}, {3/4}', fline(0, 1, 4), 'Total:',
                     draw='Line plot: 1 X at 1/4, 2 X\'s at 1/2, 1 X at 3/4', key='2 cups', note='Grade both.'),
          draw_write('Make a line plot of the data. Then find the total.\nSand in each bag (pounds): {1/8}, {3/8}, {3/8}, {5/8}', fline(0, 1, 8), 'Total:',
                     draw='Line plot: 1 X at 1/8, 2 X\'s at 3/8, 1 X at 5/8', key='1 1/2 pounds', note='12/8 and 3/2 pounds are also correct. Grade both.'),
          draw_write('Make a line plot of the data. Then find the total.\nRain each day (inches): {1/2}, {3/4}, {3/4}, 1', fline(0, 1, 4), 'Total:',
                     draw='Line plot: 1 X at 1/2, 2 X\'s at 3/4, 1 X at 1', key='3 inches', note='Grade both.'),
          draw_write('Make a line plot of the data. Then find the total.\nWater in each cup (liters): {3/8}, {1/2}, {7/8}, {1/4}', fline(0, 1, 8), 'Total:',
                     draw='Line plot: 1 X at 1/4, 1 X at 3/8, 1 X at 1/2, 1 X at 7/8', key='2 liters', note='16/8 liters is also correct. Grade both.'),
          draw_write('Make a line plot of the data. Then find the total.\nThread lengths (yards): {1/8}, {1/4}, {1/4}, {3/8}', fline(0, 1, 8), 'Total:',
                     draw='Line plot: 1 X at 1/8, 2 X\'s at 1/4, 1 X at 3/8', key='1 yard', note='8/8 yard is also correct. Grade both.'),
      ])),
]
