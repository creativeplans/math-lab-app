from qb import S, B, sa, mc, tf, nl, plot, draw_write, table
from common import (clock, BLANK_CLOCK, ruler, beaker, bargraph, picgraph, blank_picgraph, tline, fline, fdot, grid)

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
          sa('A field trip goes from 9:40 a.m. to 12:15 p.m.\nUse a number line to find how long the trip is.', 'Time:', key='2 hours 35 minutes',
             note='155 minutes is also correct.'),
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
    S('3.MD.A.2', 'Measure and estimate liquid volumes and masses in liters, grams, and kilograms',
      main=[
          sa('How many liters of water are in the container?', 'Liters:', key='6 liters', fig=beaker(10, 1, 6, 'L', label_step=2)),
          mc('Which object has a mass of about 1 kilogram?', ['A pineapple', 'A paper clip', 'A car', 'A grape']),
          tf('A bathtub holds more than 1 liter of water.', key=True),
          sa('Would you measure the mass of a bean in grams or in kilograms?', 'Unit:', key='Grams'),
          plot('Shade the container to show 3 liters.', beaker(5, 1, 0, 'L'), key='The container shaded from the bottom up to the 3-liter mark'),
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

    # ------------------------------------------------------------------ 3.MD.B.3 (picture graph)
    S('3.MD.B.3', 'Draw a scaled picture graph to represent data',
      main=[
          plot('Make a picture graph of the data. Each ● stands for 2 votes.\nApples: 6 votes, Bananas: 10 votes, Grapes: 4 votes',
               blank_picgraph('Favorite fruit', ['Apples', 'Bananas', 'Grapes'], '2 votes'),
               key='Apples: 3 symbols; Bananas: 5 symbols; Grapes: 2 symbols (each ● = 2 votes)'),
          mc('In a picture graph, each ● stands for 5 books. Ty read 20 books.\nHow many ● should be drawn for Ty?', ['4', '20', '5', '15']),
          sa('A picture graph has the key ● = 3 cars. The row for red cars has 5 ●.\nHow many red cars are there?', 'Red cars:', key='15'),
          tf('If ● = 4 students, then 7 ● stand for 28 students.', key=True),
          sa('Data: Dogs 8, Cats 12, Fish 4. You will make a picture graph with ● = 4 pets.\nHow many ● go in each row?', ['Dogs:', 'Cats:', 'Fish:'],
             key='2; 3; 1', note='All three are required.'),
      ],
      back=[
          B('Draw and read a picture graph with a single-unit scale', '2.MD.D.10', [
              plot('Make a picture graph. Draw one ● for each pet.\nDogs: 4, Cats: 3, Birds: 2', blank_picgraph('Pets', ['Dogs', 'Cats', 'Birds'], '1 pet'),
                   key='Dogs: 4 symbols; Cats: 3 symbols; Birds: 2 symbols'),
              tf('In a picture graph where ● = 1 child, 5 ● stand for 5 children.', key=True),
              mc('Use the picture graph.\nHow many children chose soccer?', ['4', '3', '2', '5'], fig=SPORT_PICS),
              sa('Use the picture graph.\nHow many more children chose swim than tennis?', 'More:', key='1', fig=SPORT_PICS),
              tf('In the picture graph, tennis has the most votes.', key=False, fig=SPORT_PICS),
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
          tf('A line plot shows each data value as an X above a number line.', key=True),
          mc('Which number line works best for a line plot of {1/8}, {3/8}, and {5/8} inch?',
             ['A line from 0 to 1 marked in eighths', 'A line from 0 to 1 marked in halves', 'A line from 0 to 8 marked in ones', 'A line from 1 to 2 marked in fourths']),
          sa('Lengths (inches): {1/2}, {3/4}, {1/2}, {1/2}\nIn a line plot of the data, how many X\'s go above {1/2}?', 'X\'s:', key='3'),
          tf('In a line plot of {1/4}, {1/4}, and {3/4}, there are 3 X\'s above {1/4}.', key=False),
      ]),
      f2=B('Use operations on fractions to solve problems with line plot data', '5.MD.B.2', [
          sa('The line plot shows rainfall on 5 days.\nWhat is the total rainfall?', 'Total:', key='2 1/2 inches', note='20/8 and 5/2 inches are also correct.', fig=RAIN),
          tf('The two days with {1/4} inch of rain had {1/2} inch in all.', key=True, fig=RAIN),
          mc('What is the difference between the greatest and the least rainfall?', ['{5/8} inch', '{3/8} inch', '{7/8} inch', '{1/2} inch'], fig=RAIN),
          sa('If the total rainfall had been spread equally over the 5 days, how much would have fallen each day?', 'Each day:',
             key='1/2 inch', fig=RAIN),
          tf('The total of {1/2}, {1/4}, and {1/8} is {3/14}.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.B.3 (bar graph)
    S('3.MD.B.3', 'Draw a scaled bar graph to represent data',
      main=[
          plot('Make a bar graph of the data. The scale counts by 2s.\nRed: 8, Blue: 12, Green: 6, Yellow: 10',
               bargraph(['Red', 'Blue', 'Green', 'Yellow'], [0, 0, 0, 0], 2, 'Number of students', ymax=14),
               key='Bars that reach 8 for Red, 12 for Blue, 6 for Green, and 10 for Yellow'),
          mc('A bar graph has a scale that counts by 2s. A bar ends halfway between 6 and 8.\nWhat number does the bar show?', ['7', '6', '8', '14']),
          tf('On a bar graph with a scale that counts by 10s, a bar for 40 ends on the fourth line above 0.', key=True),
          sa('Which scale is better for a bar graph of 10, 25, 40, and 35: counting by 1s or counting by 5s? Explain.', ['Scale:', 'Explanation:'],
             key='Counting by 5s',
             note='All the numbers are multiples of 5 and go up to 40, so counting by 5s fits them with fewer lines. Both parts are required.'),
          tf('On a bar graph with a scale that counts by 2s, a bar for 9 ends exactly on a labeled line.', key=False),
      ],
      back=[
          B('Draw and read a bar graph with a single-unit scale', '2.MD.D.10', [
              plot('Make a bar graph.\nApples: 4, Pears: 2, Plums: 5', bargraph(['Apples', 'Pears', 'Plums'], [0, 0, 0], 1, 'Number of fruits', ymax=6),
                   key='Bars that reach 4 for Apples, 2 for Pears, and 5 for Plums'),
              tf('In a bar graph, a taller bar shows a greater number.', key=True),
              mc('Use the bar graph.\nHow many children chose red?', ['5', '4', '3', '6'], fig=COLORS),
              sa('Use the bar graph.\nHow many more children chose red than blue?', 'More:', key='2', fig=COLORS),
              tf('In the bar graph, green has the most votes.', key=False, fig=COLORS),
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
          tf('The point (4, 0) is on the y-axis.', key=False),
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
              mc('A book is 8 cubes long. A box is 2 cubes longer.\nHow many cubes long is the box?', ['10 cubes', '6 cubes', '16 cubes', '8 cubes']),
              sa('A rug is 9 shoes long. A mat is 3 shoes shorter.\nHow many shoes long is the mat?', 'Shoes:', key='6'),
              tf('If the paper clips overlap when you measure, the count is still correct.', key=False),
          ]),
      ],
      f1=B('Add mixed-number lengths in word problems', '4.NF.B.3.d', [
          sa('A pencil is 3{1/4} inches long and a crayon is 2{3/4} inches long.\nHow long are they laid end to end?', 'Length:', key='6 inches'),
          tf('Ribbons of 2{1/2} inches and 1{3/4} inches laid end to end are 4{1/4} inches long.', key=True),
          mc('A snail crawls 1{1/4} inches and then 2{2/4} inches.\nHow far does it crawl in all?', ['3{3/4} inches', '3{1/4} inches', '1{1/4} inches', '4 inches']),
          sa('Three sticks are {1/2} inch, {3/4} inch, and {1/4} inch long.\nWhat is their total length?', 'Length:', key='1 1/2 inches',
             note='1 2/4 inches and 6/4 inches are also correct.'),
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
          sa('Shell lengths (inches): 2, 2{1/2}, 2{1/2}, 3, 2{1/2}\nIn a line plot of the data, how many X\'s go above 2{1/2}?', 'X\'s:', key='3'),
          mc('Which number line is best for a line plot of 1{1/4}, 1{1/2}, 1{3/4}, and 2 inches?',
             ['From 1 to 2, marked in quarters', 'From 0 to 1, marked in halves', 'From 1 to 2, marked in halves', 'From 0 to 10, marked in ones']),
          tf('The line plot shows that 2 leaves are {3/4} inch long.', key=True, fig=LEAF4),
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
          tf('{1/2} inch and {4/8} inch go above the same mark on a line plot marked in eighths.', key=True),
          mc('Lengths (inches): {1/4}, {2/8}, {3/8}, {1/4}\nIn a line plot marked in eighths, how many X\'s go above {2/8}?', ['3', '2', '1', '4']),
          plot('Make a line plot of the data.\nBead sizes (inches): {1/8}, {1/4}, {1/4}, {1/2}', fline(0, 1, 8),
               key='Line plot: 1 X at 1/8, 2 X\'s at 1/4, 1 X at 1/2'),
          tf('A line plot marked in eighths has a mark for {1/3} inch.', key=False),
      ]),
      f2=B('Use operations on fractions to solve problems with line plot data', '5.MD.B.2', [
          sa('The line plot shows the juice in 4 glasses.\nWhat is the total amount of juice?', 'Total:', key='2 cups', fig=JUICE),
          tf('If the juice were shared equally among the 4 glasses, each glass would hold {1/2} cup.', key=True, fig=JUICE),
          mc('How much more juice is in the fullest glass than in the emptiest glass?', ['{1/2} cup', '{1/4} cup', '{3/4} cup', '1 cup'], fig=JUICE),
          sa('The juice in the two {1/2}-cup glasses is poured together.\nHow much juice is that?', 'Juice:', key='1 cup', fig=JUICE),
          tf('The glasses with less than {1/2} cup hold {3/4} cup in all.', key=False, fig=JUICE),
      ])),
]
