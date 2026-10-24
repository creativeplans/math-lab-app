# Datasets

Every dataset below is **synthetic**: invented for this collection, with values chosen to show the intended feature. The values printed here are exactly the values printed on the question pages; every summary in the answer key was computed from them (src/common.py) and recomputed independently (src/resolve.py).

| Name | n | Values | Unit | Context |
|---|---:|---|---|---|
| S1 books | 15 | 2, 4, 3, 2, 5, 3, 2, 6, 3, 4, 2, 3, 1, 3, 4 | books | Books read over the summer by 15 students |
| S1 cups | 12 | 2, 3, 1, 2, 4, 2, 3, 0, 2, 1, 3, 2 | cups | Cups of water drunk before noon by 12 workers |
| S1 goals | 16 | 1, 0, 2, 1, 3, 1, 0, 2, 2, 1, 4, 1, 0, 1, 2, 1 | goals | Goals scored by a team in 16 games |
| S1 pets | 18 | 0, 1, 1, 2, 0, 3, 1, 2, 1, 0, 4, 1, 2, 1, 0, 2, 1, 3 | pets | Pets in each of 18 households |
| S1 quiz | 14 | 7, 9, 8, 10, 7, 8, 8, 6, 9, 8, 7, 10, 8, 9 | points | Quiz scores (out of 10) of 14 students |
| S1 rain days | 10 | 3, 5, 4, 4, 6, 3, 4, 5, 7, 4 | days | Rainy days in each of 10 two-week periods |
| S1 siblings | 20 | 1, 2, 0, 1, 3, 2, 1, 1, 0, 2, 5, 1, 2, 0, 1, 2, 3, 1, 1, 2 | siblings | Siblings of 20 students |
| S13 cars | 10 | (1, 24), (2, 21), (3, 22), (4, 17), (5, 18), (6, 13), (7, 14), (8, 9), (9, 11), (10, 6) | (years, thousand dollars) | Age and resale value of 10 cars of one model |
| S13 fuel | 7 | (20, 22), (30, 28), (40, 32), (50, 34), (60, 33), (70, 30), (80, 25) | (mph, miles per gallon) | Speed and fuel efficiency of one car in 7 test runs |
| S13 ice cream | 7 | (60, 120), (65, 140), (70, 155), (75, 175), (80, 190), (85, 210), (90, 60) | (degrees F, cones) | High temperature and cones sold on 7 days (the 90-degree day had a power outage) |
| S13 plants | 5 | (1, 3), (2, 5), (3, 4), (4, 7), (5, 8) | (weeks, cm) | Age and height of a seedling, measured weekly |
| S13 shoes | 10 | (6, 72), (7, 85), (8, 64), (9, 90), (10, 70), (11, 81), (12, 68), (8, 77), (10, 88), (7, 66) | (shoe size, points) | Shoe size and quiz score of 10 adults |
| S13 study | 10 | (1, 52), (2, 58), (2, 61), (3, 63), (4, 70), (5, 72), (5, 76), (6, 80), (7, 83), (8, 90) | (hours, points) | Hours studied and test score of 10 students |
| S15 spring | 6 | (2, 15), (4, 19), (5, 24), (7, 26), (8, 31), (10, 35) | (grams, cm) | Mass hung on a spring and the spring's length, 6 trials |
| S16 fit | 5 | (1, 3.5), (2, 4.6), (3, 7.2), (4, 8.8), (5, 11.1) | (x, y) | Five measurements checked against the model y = 2x + 1 |
| S16 small | 4 | (1, 2), (2, 5), (3, 4), (4, 7) | (x, y) | Four points for computing least-squares residuals by hand |
| S17 ice | 6 | (1, 48), (2, 44), (3, 41), (4, 35), (5, 33), (6, 28) | (hours, cm) | Hours after sunrise and thickness of a melting ice block |
| S2 commute | 20 | 12, 25, 8, 31, 17, 22, 15, 40, 19, 27, 10, 33, 21, 14, 26, 18, 35, 23, 29, 16 | minutes | Commute times of 20 employees |
| S2 jump | 16 | 152, 168, 145, 175, 160, 158, 171, 149, 163, 180, 155, 166, 150, 172, 161, 157 | cm | Standing long-jump distances of 16 students |
| S2 pages | 14 | 120, 255, 188, 310, 96, 205, 150, 275, 230, 182, 140, 200, 260, 175 | pages | Page counts of 14 novels |
| S2 temps | 18 | 61, 58, 70, 66, 72, 59, 64, 75, 68, 63, 71, 60, 67, 65, 74, 69, 62, 70 | degrees F | Daily high temperatures in a town over 18 days |
| S2 wait | 18 | 4, 11, 7, 15, 9, 5, 12, 20, 10, 6, 14, 8, 17, 10, 3, 13, 5, 9 | minutes | Clinic waiting times of 18 patients |
| S23 random digits | 8 | 15881399869879730911, 41707536455681518844, 72940557616987168976, 84697880932081967273, 17784864887663440029, 78753477876804571784, 72671475136270107981, 93319084520599728379 | digits | Eight lines of 20 random digits (generated once and printed, so every simulation key is fixed) |
| S28 sleep | 8 | 7, 6.5, 8, 7.5, 6, 9, 7, 8 | hours | Hours of sleep reported by a random sample of 8 students |
| S29 group A | 5 | 14, 11, 13, 12, 15 | cm | Growth of 5 plants randomly assigned to plant food A |
| S29 group B | 5 | 10, 12, 9, 11, 8 | cm | Growth of 5 plants randomly assigned to plant food B |
| S3 dist | 10 | 2.1, 3.4, 1.8, 5.0, 2.7, 4.2, 3.0, 2.4, 3.9, 1.5 | km | Distances 10 students live from school |
| S3 laps | 11 | 12, 15, 9, 18, 14, 11, 16, 20, 13, 10, 17 | laps | Laps swum by 11 swimmers |
| S3 price | 13 | 3, 8, 5, 12, 6, 4, 9, 7, 10, 5, 6, 15, 4 | dollars | Prices of 13 items on a menu |
| S3 scores | 12 | 72, 85, 90, 64, 78, 88, 95, 70, 81, 76, 84, 92 | points | Test scores of 12 students |
| S3 sleep | 14 | 7.5, 6, 8, 6.5, 9, 7, 5.5, 8.5, 7, 6.5, 7.5, 8, 6, 7 | hours | Hours of sleep of 14 teenagers |
| S3 snow | 9 | 4, 7, 2, 9, 5, 12, 6, 3, 8 | inches | Snowfall in 9 storms |
| S4 class P | 7 | 70, 74, 76, 78, 80, 82, 86 | points | Scores of 7 students in class P |
| S4 class Q | 7 | 66, 70, 72, 74, 76, 78, 82 | points | Scores of 7 students in class Q |
| S4 machine 1 | 6 | 498, 499, 500, 500, 501, 502 | grams | Masses of 6 bags filled by machine 1 |
| S4 machine 2 | 6 | 503, 504, 505, 505, 506, 507 | grams | Masses of 6 bags filled by machine 2 |
| S4 plant A | 7 | 5, 6, 6, 7, 7, 8, 30 | cm | Heights of 7 seedlings of plant A |
| S4 plant B | 7 | 8, 8, 9, 9, 9, 10, 10 | cm | Heights of 7 seedlings of plant B |
| S4 store X | 9 | 2, 2, 3, 3, 3, 4, 4, 5, 14 | days | Delivery times of 9 orders from store X |
| S4 store Y | 9 | 2, 3, 3, 4, 4, 5, 5, 6, 6 | days | Delivery times of 9 orders from store Y |
| S4 town A | 8 | 210, 225, 230, 240, 245, 250, 260, 900 | thousand dollars | Sale prices of 8 homes in Town A |
| S4 town B | 8 | 190, 220, 235, 255, 270, 280, 300, 310 | thousand dollars | Sale prices of 8 homes in Town B |
| S5 fish A | 8 | 20, 22, 23, 25, 26, 28, 30, 31 | cm | Lengths of 8 fish from lake A |
| S5 fish B | 8 | 18, 24, 24, 25, 25, 26, 26, 40 | cm | Lengths of 8 fish from lake B |
| S5 rent A | 7 | 800, 850, 900, 950, 1000, 1050, 2400 | dollars | Monthly rents of 7 apartments in building A |
| S5 rent B | 7 | 700, 800, 900, 1000, 1100, 1200, 1300 | dollars | Monthly rents of 7 apartments in building B |
| S5 set 1 | 5 | 4, 6, 8, 10, 12 | minutes | Bus delays on 5 days, route 1 |
| S5 set 2 | 5 | 7, 8, 8, 8, 9 | minutes | Bus delays on 5 days, route 2 |
| S5 set 3 | 5 | 10, 20, 30, 40, 50 | dollars | Weekly savings of 5 students, group 1 |
| S5 set 4 | 5 | 25, 28, 30, 32, 35 | dollars | Weekly savings of 5 students, group 2 |
| S5 team A | 9 | 14, 15, 15, 16, 16, 17, 18, 18, 19 | years | Ages of 9 players on team A |
| S5 team B | 9 | 13, 14, 16, 16, 17, 18, 20, 22, 25 | years | Ages of 9 players on team B |
| S6 miles | 9 | 3, 4, 4, 5, 5, 5, 6, 6, 7 | miles | Distances 9 runners ran on one day |
| S7 bikes | 10 | 180, 210, 195, 205, 190, 600, 200, 185, 215, 220 | dollars | Prices of 10 used bikes |
| S7 calls | 10 | 3, 5, 4, 6, 5, 4, 22, 5, 3, 4 | calls | Support calls received in each of 10 hours |
| S7 hours | 11 | 6, 8, 7, 9, 7, 8, 30, 6, 7, 8, 1 | hours | Hours of screen time 11 students reported for one weekend |
| S7 points | 11 | 12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16 | points | Points a player scored in 11 games |
| S7 race | 9 | 52, 55, 54, 31, 56, 53, 57, 55, 54 | seconds | Times of 9 swimmers in a 50-meter race |
