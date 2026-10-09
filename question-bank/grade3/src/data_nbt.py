from qb import S, B, sa, mc, tf, nl, work

ADD_ALG = ('The standard addition algorithm with the regrouping shown. A correct sum without the algorithm earns partial credit.')
SUB_ALG = ('The standard subtraction algorithm with the regrouping shown. A correct difference without the algorithm earns partial credit.')

SETS = [
    # ------------------------------------------------------------------ 3.NBT.A.1 (tens)
    S('3.NBT.A.1', 'Round whole numbers to the nearest 10',
      main=[
          sa('Round 47 to the nearest ten.', 'Rounded:', key='50'),
          tf('118 rounded to the nearest ten is 110.', key=False),
          mc('Round 685 to the nearest ten.', ['690', '680', '700', '600']),
          tf('234 rounded to the nearest ten is 230.', key=True),
          sa('Use the number line.\nIs 76 closer to 70 or to 80? Round 76 to the nearest ten.', ['Closer to:', 'Rounded:'], key='80; 80',
             fig=nl(70, 80, 1, labels={70: '70', 75: '75', 80: '80'}, pts=[(76, '76')]), note='Both parts are required.'),
      ],
      back=[
          B('Hundreds, tens, and ones in three-digit numbers', '2.NBT.A.1', [
              sa('What digit is in the tens place of 563?', 'Digit:', key='6'),
              tf('In 708, the 0 means 0 tens.', key=True),
              mc('Which number has 3 hundreds, 8 tens, and 2 ones?', ['382', '328', '832', '3,082']),
              sa('What is the value of the 4 in 245?', 'Value:', key='40'),
              tf('In 961, the 6 is worth 6.', key=False),
          ]),
          B('Whole numbers on a number line', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='45', fig=nl(40, 50, 1, labels={40: '40', 50: '50'}, pts=[(45, 'A')])),
              tf('On a number line, 68 is between 60 and 70.', key=True),
              mc('Which number is closest to 30 on a number line?', ['32', '37', '39', '36']),
              sa('What number is at point B?', 'B =', key='87', fig=nl(80, 90, 1, labels={80: '80', 90: '90'}, pts=[(87, 'B')])),
              tf('On a number line, 54 is closer to 60 than to 50.', key=False),
          ]),
      ],
      f1=B('Round multi-digit whole numbers to any place', '4.NBT.A.3', [
          sa('Round 3,467 to the nearest ten.', 'Rounded:', key='3,470'),
          tf('12,845 rounded to the nearest hundred is 12,800.', key=True),
          mc('Round 58,349 to the nearest thousand.', ['58,000', '59,000', '58,300', '60,000']),
          sa('Round 7,996 to the nearest ten.', 'Rounded:', key='8,000'),
          tf('41,705 rounded to the nearest ten thousand is 50,000.', key=False),
      ]),
      f2=B('Round decimals to any place', '5.NBT.A.4', [
          sa('Round 4.67 to the nearest tenth.', 'Rounded:', key='4.7'),
          tf('2.349 rounded to the nearest hundredth is 2.35.', key=True),
          mc('Round 8.52 to the nearest whole number.', ['9', '8', '8.5', '8.6']),
          sa('Round 0.938 to the nearest hundredth.', 'Rounded:', key='0.94'),
          tf('6.45 rounded to the nearest tenth is 6.4.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NBT.A.1 (hundreds)
    S('3.NBT.A.1', 'Round whole numbers to the nearest 100',
      main=[
          sa('Round 382 to the nearest hundred.', 'Rounded:', key='400'),
          tf('749 rounded to the nearest hundred is 700.', key=True),
          mc('Round 650 to the nearest hundred.', ['700', '600', '650', '610']),
          tf('216 rounded to the nearest hundred is 300.', key=False),
          sa('A school has 538 students.\nRound the number of students to the nearest hundred.', 'Rounded:', key='500'),
      ],
      back=[
          B('Read and write numbers to 1000 in expanded form', '2.NBT.A.3', [
              sa('Write 627 in expanded form.', 'Expanded form:', key='600 + 20 + 7'),
              tf('Four hundred five is written 405.', key=True),
              mc('Which number is 300 + 70 + 4?', ['374', '347', '3,074', '734']),
              sa('Write the number eight hundred sixty with digits.', 'Number:', key='860'),
              tf('500 + 9 = 590', key=False),
          ]),
          B('Three-digit numbers on a number line', '2.MD.B.6', [
              sa('What number is at point C?', 'C =', key='350', fig=nl(300, 400, 10, labels={300: '300', 400: '400'}, pts=[(350, 'C')])),
              tf('On a number line, 720 is between 700 and 800.', key=True),
              mc('Which number is closer to 600 than to 500?', ['580', '520', '540', '510']),
              sa('What number is halfway between 200 and 300 on a number line?', 'Number:', key='250'),
              tf('On a number line, 430 is closer to 500 than to 400.', key=False),
          ]),
      ],
      f1=B('Round multi-digit whole numbers to the hundreds, thousands, and beyond', '4.NBT.A.3', [
          sa('Round 6,251 to the nearest hundred.', 'Rounded:', key='6,300'),
          tf('94,512 rounded to the nearest thousand is 95,000.', key=True),
          mc('Round 238,670 to the nearest hundred thousand.', ['200,000', '300,000', '240,000', '238,700']),
          sa('Round 9,950 to the nearest hundred.', 'Rounded:', key='10,000'),
          tf('3,049 rounded to the nearest hundred is 3,100.', key=False),
      ]),
      f2=B('Round decimals to the nearest whole number, tenth, or hundredth', '5.NBT.A.4', [
          sa('Round 13.48 to the nearest whole number.', 'Rounded:', key='13'),
          tf('0.75 rounded to the nearest tenth is 0.8.', key=True),
          mc('Round 2.963 to the nearest tenth.', ['3.0', '2.9', '2.96', '2.8']),
          sa('Round 5.096 to the nearest hundredth.', 'Rounded:', key='5.10', note='5.1 names the same value and is also correct.'),
          tf('9.04 rounded to the nearest tenth is 9.1.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NBT.A.2 (add)
    S('3.NBT.A.2', 'Add within 1000 using place value strategies and algorithms',
      main=[
          work('Add. Show your work using place value or the standard algorithm.\n358 + 276', 'Sum:', key='634',
               method='Any valid place-value strategy or the standard algorithm, with the regrouping shown (for example 300 + 200 = 500, '
                      '50 + 70 = 120, 8 + 6 = 14, and 500 + 120 + 14 = 634). The sum alone earns partial credit.'),
          sa('Add.\n407 + 395', 'Sum:', key='802'),
          mc('529 + 263 = ?', ['792', '782', '702', '266']),
          tf('186 + 614 = 800', key=True),
          tf('475 + 348 = 813', key=False),
      ],
      back=[
          B('Add within 100', '2.NBT.B.5', [
              sa('Add.\n58 + 36', 'Sum:', key='94'),
              tf('47 + 25 = 72', key=True),
              mc('29 + 64 = ?', ['93', '83', '35', '94']),
              sa('Add.\n75 + 18', 'Sum:', key='93'),
              tf('66 + 27 = 83', key=False),
          ]),
          B('Add within 1000 by adding hundreds, tens, and ones', '2.NBT.B.7', [
              sa('Add using hundreds, tens, and ones.\n234 + 152', 'Sum:', key='386'),
              tf('300 + 400 = 700', key=True),
              mc('Which shows the sum 245 + 132 by place value?', ['300 + 70 + 7', '300 + 70 + 5', '200 + 70 + 7', '300 + 60 + 7']),
              sa('Add.\n420 + 160', 'Sum:', key='580'),
              tf('513 + 241 = 744', key=False),
          ]),
      ],
      f1=B('Add multi-digit whole numbers with the standard algorithm', '4.NBT.B.4', [
          work('Use the standard algorithm to add. Show your work.\n3,768 + 2,457', 'Sum:', method=ADD_ALG, key='6,225'),
          sa('Add.\n45,092 + 18,659', 'Sum:', key='63,751'),
          mc('2,806 + 4,395 = ?', ['7,201', '7,101', '6,201', '7,191']),
          tf('9,999 + 1 = 10,000', key=True),
          tf('6,485 + 3,729 = 10,114', key=False),
      ]),
      f2=B('Add decimals to hundredths', '5.NBT.B.7', [
          sa('Add.\n3.45 + 2.8', 'Sum:', key='6.25'),
          tf('0.6 + 0.47 = 1.07', key=True),
          mc('Add.\n12.5 + 3.75', ['16.25', '15.80', '16.20', '4.00']),
          sa('Add.\n4.09 + 5.91', 'Sum:', key='10', note='10.00 is also correct.'),
          tf('2.7 + 1.35 = 3.12', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NBT.A.2 (subtract)
    S('3.NBT.A.2', 'Subtract within 1000 using place value strategies and algorithms',
      main=[
          work('Subtract. Show your work using place value or the standard algorithm.\n623 - 358', 'Difference:', key='265',
               method='Any valid place-value strategy or the standard algorithm, with the regrouping shown (for example counting up: '
                      '358 + 2 = 360, 360 + 40 = 400, 400 + 223 = 623, so 2 + 40 + 223 = 265). The difference alone earns partial credit.'),
          sa('Subtract.\n700 - 246', 'Difference:', key='454'),
          mc('815 - 379 = ?', ['436', '546', '444', '1,194']),
          tf('902 - 518 = 384', key=True),
          tf('560 - 287 = 383', key=False),
      ],
      back=[
          B('Subtract within 100', '2.NBT.B.5', [
              sa('Subtract.\n82 - 45', 'Difference:', key='37'),
              tf('60 - 23 = 37', key=True),
              mc('74 - 39 = ?', ['35', '45', '113', '25']),
              sa('Subtract.\n53 - 17', 'Difference:', key='36'),
              tf('91 - 58 = 43', key=False),
          ]),
          B('Subtract within 1000 by subtracting hundreds, tens, and ones', '2.NBT.B.7', [
              sa('Subtract using hundreds, tens, and ones.\n587 - 243', 'Difference:', key='344'),
              tf('800 - 300 = 500', key=True),
              mc('465 - 120 = ?', ['345', '355', '245', '585']),
              sa('Subtract.\n690 - 250', 'Difference:', key='440'),
              tf('758 - 426 = 342', key=False),
          ]),
      ],
      f1=B('Subtract multi-digit whole numbers with the standard algorithm', '4.NBT.B.4', [
          work('Use the standard algorithm to subtract. Show your work.\n7,203 - 4,568', 'Difference:', method=SUB_ALG, key='2,635'),
          sa('Subtract.\n50,000 - 23,418', 'Difference:', key='26,582'),
          mc('8,412 - 3,756 = ?', ['4,656', '5,344', '4,756', '4,666']),
          tf('6,001 - 2,999 = 3,002', key=True),
          tf('9,350 - 4,875 = 4,575', key=False),
      ]),
      f2=B('Subtract decimals to hundredths', '5.NBT.B.7', [
          sa('Subtract.\n6.4 - 2.75', 'Difference:', key='3.65'),
          tf('5 - 1.25 = 3.75', key=True),
          mc('Subtract.\n10.3 - 4.68', ['5.62', '6.38', '5.72', '14.98']),
          sa('Subtract.\n8.06 - 3.9', 'Difference:', key='4.16'),
          tf('7.5 - 2.25 = 5.35', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NBT.A.2 (relationship)
    S('3.NBT.A.2', 'Use the relationship between addition and subtraction to subtract and to check answers',
      main=[
          sa('Find 500 - 287 by counting up from 287.', 'Difference:', key='213',
             note='287 + 3 = 290, 290 + 10 = 300, 300 + 200 = 500; 3 + 10 + 200 = 213.'),
          mc('Which addition checks 642 - 275 = 367?', ['367 + 275 = 642', '642 + 275 = 367', '367 + 642 = 275', '275 + 642 = 367']),
          tf('Because 318 + 457 = 775, you know that 775 - 457 = 318.', key=True),
          sa('Use addition to check: is 803 - 426 = 387 correct? Show the addition you used.', ['Correct?', 'Check:'], key='No; 387 + 426 = 813',
             note='387 + 426 = 813, not 803, so the answer is wrong (the correct difference is 377). Both parts are required.'),
          tf('Because 245 + 380 = 625, you know that 625 - 245 = 385.', key=False),
      ],
      back=[
          B('Use addition facts to subtract within 20', '1.OA.C.6', [
              sa('Find 16 - 9 by thinking 9 + ? = 16.', 'Difference:', key='7'),
              tf('11 - 4 = 7 because 4 + 7 = 11.', key=True),
              mc('Which addition fact checks 15 - 6 = 9?', ['9 + 6 = 15', '15 + 6 = 21', '9 - 6 = 3', '6 + 6 = 12']),
              sa('Write the addition fact that checks 18 - 9 = 9.', 'Fact:', key='9 + 9 = 18'),
              tf('12 - 8 = 5 because 8 + 5 = 12.', key=False),
          ]),
          B('Use the relationship between addition and subtraction within 100', '2.NBT.B.5', [
              sa('Find 70 - 45 by counting up from 45.', 'Difference:', key='25'),
              tf('Because 36 + 28 = 64, you know that 64 - 28 = 36.', key=True),
              mc('Which addition checks 90 - 37 = 53?', ['53 + 37 = 90', '90 + 37 = 53', '53 + 90 = 37', '37 + 90 = 53']),
              sa('Is 81 - 34 = 47 correct? Write the addition you used to check.', ['Correct?', 'Check:'], key='Yes; 47 + 34 = 81',
                 note='Both parts are required.'),
              tf('Because 42 + 19 = 61, you know that 61 - 42 = 29.', key=False),
          ]),
      ],
      f1=B('Check multi-digit subtraction with addition', '4.NBT.B.4', [
          sa('Use addition to check: is 6,000 - 2,348 = 3,652 correct?', ['Correct?', 'Check:'], key='Yes; 3,652 + 2,348 = 6,000',
             note='Both parts are required.'),
          tf('Because 4,519 + 2,786 = 7,305, you know that 7,305 - 2,786 = 4,519.', key=True),
          mc('Which addition checks 9,104 - 5,677 = 3,427?',
             ['3,427 + 5,677 = 9,104', '9,104 + 5,677 = 3,427', '3,427 + 9,104 = 5,677', '5,677 + 9,104 = 3,427']),
          sa('Find 8,000 - 3,995 by counting up from 3,995.', 'Difference:', key='4,005',
             note='3,995 + 5 = 4,000 and 4,000 + 4,000 = 8,000; 5 + 4,000 = 4,005.'),
          tf('Because 12,450 + 6,780 = 19,230, you know that 19,230 - 12,450 = 6,870.', key=False),
      ]),
      f2=B('Check decimal subtraction with addition', '5.NBT.B.7', [
          sa('Use addition to check: is 5.2 - 1.75 = 3.45 correct?', ['Correct?', 'Check:'], key='Yes; 3.45 + 1.75 = 5.2',
             note='Both parts are required.'),
          tf('Because 2.6 + 3.85 = 6.45, you know that 6.45 - 3.85 = 2.6.', key=True),
          mc('Which addition checks 9.3 - 4.56 = 4.74?', ['4.74 + 4.56 = 9.3', '9.3 + 4.56 = 4.74', '4.74 + 9.3 = 4.56', '4.56 + 9.3 = 4.74']),
          sa('Find 4 - 2.35 by counting up from 2.35.', 'Difference:', key='1.65'),
          tf('Because 1.4 + 2.75 = 4.15, you know that 4.15 - 1.4 = 2.65.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NBT.A.3
    S('3.NBT.A.3', 'Multiply one-digit whole numbers by multiples of 10',
      main=[
          sa('Multiply.\n4 × 70', 'Product:', key='280'),
          tf('9 × 20 = 160', key=False),
          mc('6 × 90 = ?', ['540', '54', '5,400', '96']),
          tf('7 × 40 = 280', key=True),
          sa('Explain how you can use 3 × 8 = 24 to find 3 × 80.', ['Product:', 'Explanation:'], key='240',
             note='80 is 8 tens, so 3 × 80 is 3 × 8 tens = 24 tens = 240. Both parts are required.'),
      ],
      back=[
          B('A hundred is ten tens', '2.NBT.A.1.a', [
              sa('How many tens make 1 hundred?', 'Tens:', key='10'),
              tf('10 tens and 1 hundred are the same amount.', key=True),
              mc('Which is the same amount as 1 hundred?', ['10 tens', '10 ones', '1 ten', '100 tens']),
              sa('Fill in the blank.\n10 tens = ___', 'Blank:', key='100'),
              tf('A bundle of 10 tens is the same amount as 10.', key=False),
          ]),
          B('Skip-count by 10s', '2.NBT.A.2', [
              sa('Skip-count by 10s from 10.\nWhat is the 6th number?', 'Number:', key='60'),
              tf('Counting by 10s from 0, 8 jumps of 10 land on 80.', key=True),
              mc('Count by 10s.\n30, 40, 50, ___', ['60', '51', '70', '500']),
              sa('Skip-count by 10s.\n150, 160, 170, ___, ___', 'Next two:', key='180, 190'),
              tf('Counting by 10s from 0, 5 jumps of 10 land on 15.', key=False),
          ]),
      ],
      f1=B('Multiply by multiples of 10, 100, and 1,000', '4.NBT.B.5', [
          sa('Multiply.\n6 × 400', 'Product:', key='2,400'),
          tf('8 × 3,000 = 24,000', key=True),
          mc('5 × 800 = ?', ['4,000', '400', '40,000', '805']),
          sa('Multiply.\n30 × 40', 'Product:', key='1,200'),
          tf('7 × 600 = 420', key=False),
      ]),
      f2=B('Multiply by powers of 10 and explain the pattern in the zeros', '5.NBT.A.2', [
          sa('Multiply.\n36 × 10³', 'Product:', key='36,000'),
          tf('4.2 × 100 = 420', key=True),
          mc('Which is equal to 5 × 10²?', ['500', '50', '5,000', '52']),
          sa('Explain why 7 × 1,000 ends in three zeros.', ['Explanation:', ''],
             key='Multiplying by 1,000 (10³) moves each digit three places to the left, so the three places on the right are filled with zeros.',
             note='Must connect the three zeros to multiplying by 10 three times, or to shifting each digit three places.'),
          tf('0.6 × 10 = 0.06', key=False),
      ])),
]
