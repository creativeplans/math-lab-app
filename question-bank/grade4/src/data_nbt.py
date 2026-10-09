from qb import S, B, sa, mc, tf, draw_write, work, DIVISION_ALGORITHM
from common import arr, amodel, amodel2

ADD_ALG = ('The standard algorithm: digits lined up by place value and added from the ones place to the left, with each '
           'regrouping shown. Another method earns partial credit.')
SUB_ALG = ('The standard algorithm: digits lined up by place value and subtracted from the ones place to the left, with each '
           'regrouping (renaming) shown. Another method earns partial credit.')
MUL_ALG = ('The standard algorithm: one partial product for each digit of the second factor (with regrouping), each lined up '
           'by place value, then the partial products added. Another method earns partial credit.')

SETS = [
    # ------------------------------------------------------------------ 4.NBT.A.1 (ten times)
    S('4.NBT.A.1', 'A digit in one place is worth ten times what it is worth in the place to its right',
      main=[
          tf('In 4,440, the 4 in the hundreds place is worth 10 times the 4 in the tens place.', key=True),
          mc('The 8 in 8,325 is worth how many times the 8 in 825?', ['10 times', '100 times', '8 times', 'The same']),
          sa('What is the value of the 6 in 62,904?', 'Value:', key='60,000'),
          sa('Write the number that is 10 times as much as 3,070.', 'Number:', key='30,700'),
          tf('In 5,555, the 5 in the tens place is worth 10 times the 5 in the hundreds place.', key=False),
      ],
      back=[
          B('Hundreds, tens, and ones', '2.NBT.A.1', [
              sa('How many tens make 1 hundred?', 'Tens:', key='10'),
              tf('In 472, the 7 means 7 tens.', key=True),
              mc('What is the value of the 3 in 360?', ['300', '30', '3', '3,000']),
              sa('Write the number with 5 hundreds, 0 tens, and 8 ones.', 'Number:', key='508'),
              tf('In 914, the 1 means 1 hundred.', key=False),
          ]),
          B('Multiply one-digit numbers by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n6 × 40', 'Product:', key='240'),
              tf('3 × 70 = 210', key=True),
              mc('9 × 50 = ?', ['450', '45', '4,500', '59']),
              sa('Multiply.\n8 × 30', 'Product:', key='240'),
              tf('5 × 80 = 4,000', key=False),
          ]),
      ],
      f1=B('Place value in decimals: 10 times and 1/10 of a digit', '5.NBT.A.1', [
          tf('In 3.33, the 3 in the ones place is worth 10 times the 3 in the tenths place.', key=True),
          sa('What is {1/10} of 70?', 'Answer:', key='7'),
          mc('In 6.66, the 6 in the hundredths place is worth what part of the 6 in the tenths place?',
             ['{1/10}', '10 times as much', '{1/100}', 'The same amount']),
          sa('What is 10 times 0.4?', 'Answer:', key='4'),
          tf('In 2.22, the 2 in the tenths place is worth 10 times the 2 in the ones place.', key=False),
      ]),
      f2=B('Write and evaluate powers of 10 with exponents', '6.EE.A.1', [
          sa('Write 10 × 10 × 10 using an exponent.', 'Exponent form:', key='10³'),
          tf('10⁴ = 10,000', key=True),
          mc('Evaluate.\n10²', ['100', '20', '12', '1,000']),
          sa('Evaluate.\n4 × 10³', 'Value:', key='4,000'),
          tf('10⁵ has 4 zeros.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.A.1 (place value and division)
    S('4.NBT.A.1', 'Use place value and division to explain why one number is ten times another',
      main=[
          sa('Use place value to find 5,000 ÷ 500.', 'Quotient:', key='10'),
          tf('900 ÷ 90 = 10 because 9 hundreds is 10 times 9 tens.', key=True),
          mc('Which statement explains why 3,000 ÷ 300 = 10?',
             ['3 thousands is 10 times 3 hundreds.', '3,000 has one more zero.', '3,000 - 300 = 10', '300 ÷ 3,000 = 10']),
          sa('4,000 is how many times as much as 400? Explain using place value.', ['Answer:', 'Explanation:'], key='10 times',
             note='4 thousands = 40 hundreds, which is 10 groups of 4 hundreds. Saying only "it has one more zero" is not a place-value explanation.'),
          tf('60 ÷ 6 = 100', key=False),
      ],
      back=[
          B('A hundred is a bundle of ten tens', '2.NBT.A.1.a', [
              tf('100 can be thought of as a bundle of 10 tens.', key=True),
              sa('How many tens make 1 hundred?', 'Tens:', key='10'),
              mc('Which shows the same amount as 1 hundred?', ['10 tens', '10 ones', '1 ten', '100 tens']),
              sa('Fill in the blank.\n10 tens = ___ hundred', 'Blank:', key='1'),
              tf('A bundle of 10 tens is the same amount as 1,000.', key=False),
          ]),
          B('Multiply one-digit numbers by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n4 × 90', 'Product:', key='360'),
              tf('7 × 60 = 420', key=True),
              mc('2 × 80 = ?', ['160', '16', '1,600', '82']),
              sa('Multiply.\n9 × 20', 'Product:', key='180'),
              tf('6 × 50 = 3,000', key=False),
          ]),
      ],
      f1=B('Divide whole numbers and decimals by powers of 10', '5.NBT.A.2', [
          sa('Divide.\n4,500 ÷ 100', 'Quotient:', key='45'),
          tf('7,000 ÷ 10³ = 7', key=True),
          mc('Divide.\n36 ÷ 10', ['3.6', '360', '0.36', '36']),
          sa('Divide.\n820 ÷ 10²', 'Quotient:', key='8.2'),
          tf('50 ÷ 10 = 500', key=False),
      ]),
      f2=B('Divide multi-digit decimals', '6.NS.B.3', [
          sa('Divide.\n4.5 ÷ 0.45', 'Quotient:', key='10'),
          tf('0.8 ÷ 0.08 = 10', key=True),
          mc('Divide.\n6 ÷ 0.6', ['10', '1', '0.1', '100']),
          sa('Divide.\n2.4 ÷ 0.3', 'Quotient:', key='8'),
          tf('1.2 ÷ 0.12 = 100', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.A.2 (numerals and names)
    S('4.NBT.A.2', 'Read and write multi-digit whole numbers using numerals and number names',
      main=[
          sa('Write the number in standard form.\nforty-six thousand, two hundred eight', 'Number:', key='46,208'),
          sa('Write 309,051 in words.', 'Words:', key='three hundred nine thousand, fifty-one'),
          mc('Which is 72,016 in words?', ['seventy-two thousand, sixteen', 'seventy-two thousand, one hundred sixty',
                                          'seven thousand, two hundred sixteen', 'seventy-two thousand, one hundred six']),
          tf('Six hundred thousand, forty is written 600,400.', key=False),
          sa('Write the number in standard form.\nninety thousand, nine hundred', 'Number:', key='90,900'),
      ],
      back=[
          B('Read and write numbers to 1000', '2.NBT.A.3', [
              sa('Write the number in standard form.\nfour hundred seventeen', 'Number:', key='417'),
              tf('Six hundred five is written 650.', key=False),
              mc('Which is 238 in words?', ['two hundred thirty-eight', 'two hundred eighty-three', 'twenty-three eight', 'three hundred twenty-eight']),
              sa('Write 702 in words.', 'Words:', key='seven hundred two'),
              tf('Nine hundred ninety is written 990.', key=True),
          ]),
          B('Hundreds, tens, and ones', '2.NBT.A.1', [
              sa('What digit is in the tens place of 586?', 'Digit:', key='8'),
              tf('In 249, the 2 is worth 200.', key=True),
              mc('Which number has 7 hundreds, 3 tens, and 0 ones?', ['730', '703', '370', '73']),
              sa('How many hundreds are in 600?', 'Hundreds:', key='6'),
              tf('In 381, the 8 is worth 8.', key=False),
          ]),
      ],
      f1=B('Read and write decimals to thousandths', '5.NBT.A.3.a', [
          sa('Write the number in standard form.\nfour and twenty-five thousandths', 'Number:', key='4.025'),
          tf('0.6 is read "six tenths."', key=True),
          mc('Which is 3.48 in words?', ['three and forty-eight hundredths', 'three hundred forty-eight',
                                        'three and forty-eight tenths', 'thirty-four and eight tenths']),
          sa('Write 12.307 in words.', 'Words:', key='twelve and three hundred seven thousandths'),
          tf('Five and nine hundredths is written 5.9.', key=False),
      ]),
      f2=B('Use positive and negative numbers to describe quantities', '6.NS.C.5', nearest=True, qs=[
          sa('A diver is 30 feet below sea level.\nWrite the diver\'s position as an integer.', 'Integer:', key='-30'),
          tf('A gain of 8 yards can be written as +8.', key=True),
          mc('Which integer shows a temperature of 12 degrees below zero?', ['-12', '12', '-21', '0']),
          sa('A deposit of $45 is written as +45.\nHow is a withdrawal of $45 written?', 'Integer:', key='-45'),
          tf('-5 means 5 more than zero.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.A.2 (expanded form)
    S('4.NBT.A.2', 'Write multi-digit whole numbers in expanded form',
      main=[
          sa('Write 7,345 in expanded form.', 'Expanded form:', key='7,000 + 300 + 40 + 5'),
          sa('Write the number.\n50,000 + 2,000 + 80 + 6', 'Number:', key='52,086'),
          mc('Which is the expanded form of 40,209?', ['40,000 + 200 + 9', '40,000 + 2,000 + 9', '4,000 + 200 + 9', '40,000 + 20 + 9']),
          tf('600,000 + 3,000 + 70 = 630,070', key=False),
          sa('Write 18,504 in expanded form.', 'Expanded form:', key='10,000 + 8,000 + 500 + 4'),
      ],
      back=[
          B('Expanded form for numbers to 1000', '2.NBT.A.3', [
              sa('Write 846 in expanded form.', 'Expanded form:', key='800 + 40 + 6'),
              tf('300 + 9 = 390', key=False),
              mc('Which number is 500 + 20 + 7?', ['527', '5,207', '572', '257']),
              sa('Write the number.\n900 + 60', 'Number:', key='960'),
              tf('200 + 40 + 1 = 241', key=True),
          ]),
          B('Two-digit numbers as tens and ones', '1.NBT.B.2', [
              sa('How many tens and ones are in 47?', 'Answer:', key='4 tens and 7 ones'),
              tf('63 is 6 tens and 3 ones.', key=True),
              mc('Which number is 8 tens and 2 ones?', ['82', '28', '802', '10']),
              sa('Write the number that is 5 tens and 0 ones.', 'Number:', key='50'),
              tf('91 is 1 ten and 9 ones.', key=False),
          ]),
      ],
      f1=B('Write decimals in expanded form', '5.NBT.A.3.a', [
          sa('Write 3.46 in expanded form.', 'Expanded form:', key='3 × 1 + 4 × (1/10) + 6 × (1/100)', note='3 + 0.4 + 0.06 is also correct.'),
          tf('2 + 0.5 + 0.03 = 2.53', key=True),
          mc('Which number is 7 × 1 + 2 × {1/10} + 9 × {1/1000}?', ['7.209', '7.29', '7.029', '72.9']),
          sa('Write the number.\n5 × 10 + 1 × 1 + 8 × {1/100}', 'Number:', key='51.08'),
          tf('4 × {1/10} + 1 × {1/100} = 0.041', key=False),
      ]),
      f2=B('Write numbers using powers of 10 with exponents', '6.EE.A.1', [
          sa('Write 6,000 + 400 + 70 + 2 using powers of 10.', 'Expression:', key='6 × 10³ + 4 × 10² + 7 × 10¹ + 2',
             note='Writing the last term as 2 × 10⁰ is also correct.'),
          tf('3 × 10⁴ = 30,000', key=True),
          mc('Which number equals 5 × 10³ + 8 × 10?', ['5,080', '5,800', '580', '5,008']),
          sa('Evaluate.\n2 × 10³ + 9 × 10²', 'Value:', key='2,900'),
          tf('7 × 10² = 70', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.A.2 (compare)
    S('4.NBT.A.2', 'Compare multi-digit whole numbers using >, =, and <',
      main=[
          sa('Write >, =, or <.\n45,621 ___ 45,612', 'Symbol:', key='>'),
          mc('Which comparison is true?', ['80,099 < 80,100', '80,099 > 80,100', '80,099 = 80,100', '80,100 < 80,099']),
          tf('305,000 < 350,000', key=True),
          sa('Order from least to greatest.\n27,450   24,750   27,045', 'Order:', key='24,750, 27,045, 27,450'),
          tf('9,998 > 10,001', key=False),
      ],
      back=[
          B('Compare three-digit numbers', '2.NBT.A.4', [
              sa('Write >, =, or <.\n482 ___ 428', 'Symbol:', key='>'),
              tf('309 < 390', key=True),
              mc('Which number is greatest?', ['710', '701', '699', '170']),
              sa('Write >, =, or <.\n555 ___ 555', 'Symbol:', key='='),
              tf('640 > 664', key=False),
          ]),
          B('Compare two-digit numbers', '1.NBT.B.3', [
              sa('Write >, =, or <.\n67 ___ 76', 'Symbol:', key='<'),
              tf('58 > 49', key=True),
              mc('Which number is less than 35?', ['29', '53', '40', '35']),
              sa('Write >, =, or <.\n90 ___ 19', 'Symbol:', key='>'),
              tf('42 < 24', key=False),
          ]),
      ],
      f1=B('Compare decimals to thousandths', '5.NBT.A.3.b', [
          sa('Write >, =, or <.\n0.45 ___ 0.405', 'Symbol:', key='>'),
          tf('3.09 < 3.1', key=True),
          mc('Which decimal is greatest?', ['2.5', '2.48', '2.405', '2.09']),
          sa('Write >, =, or <.\n6.70 ___ 6.7', 'Symbol:', key='='),
          tf('0.125 > 0.13', key=False),
      ]),
      f2=B('Order rational numbers using their positions on a number line', '6.NS.C.7.a', [
          sa('Write >, =, or <.\n-8 ___ -3', 'Symbol:', key='<'),
          tf('-2 > -10', key=True),
          mc('Which number is least?', ['-15', '-5', '0', '5']),
          sa('Order from least to greatest.\n4, -6, 0, -1', 'Order:', key='-6, -1, 0, 4'),
          tf('-7 > 2', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.A.3
    S('4.NBT.A.3', 'Round multi-digit whole numbers to any place',
      main=[
          sa('Round 46,829 to the nearest thousand.', 'Rounded:', key='47,000'),
          sa('Round 352,618 to the nearest ten thousand.', 'Rounded:', key='350,000'),
          mc('Round 7,950 to the nearest hundred.', ['8,000', '7,900', '7,000', '7,960']),
          tf('128,476 rounded to the nearest hundred thousand is 200,000.', key=False),
          sa('A stadium has 63,548 seats.\nRound the number of seats to the nearest thousand.', 'Rounded:', key='64,000'),
      ],
      back=[
          B('Round to the nearest 10 or 100', '3.NBT.A.1', [
              sa('Round 84 to the nearest ten.', 'Rounded:', key='80'),
              tf('652 rounded to the nearest hundred is 700.', key=True),
              mc('Round 345 to the nearest ten.', ['350', '340', '300', '400']),
              sa('Round 961 to the nearest hundred.', 'Rounded:', key='1,000'),
              tf('26 rounded to the nearest ten is 20.', key=False),
          ]),
          B('Skip-count by 5s, 10s, and 100s', '2.NBT.A.2', [
              sa('Skip-count by 100s.\n300, 400, 500, ___', 'Next:', key='600'),
              tf('Counting by 10s from 470 gives 480, 490, 500.', key=True),
              mc('What comes next when counting by 5s?\n85, 90, 95, ___', ['100', '96', '105', '99']),
              sa('Skip-count by 10s.\n620, 630, 640, ___', 'Next:', key='650'),
              tf('Counting by 100s from 700 gives 800, 900, 990.', key=False),
          ]),
      ],
      f1=B('Round decimals to any place', '5.NBT.A.4', [
          sa('Round 3.468 to the nearest tenth.', 'Rounded:', key='3.5'),
          sa('Round 14.729 to the nearest whole number.', 'Rounded:', key='15'),
          mc('Round 0.638 to the nearest hundredth.', ['0.64', '0.63', '0.6', '0.7']),
          tf('5.95 rounded to the nearest tenth is 6.0.', key=True),
          tf('8.249 rounded to the nearest tenth is 8.3.', key=False),
      ]),
      f2=B('Compute with decimals and round the result', '6.NS.B.3', nearest=True, qs=[
          sa('Divide. Round the quotient to the nearest tenth.\n10 ÷ 3', 'Quotient:', key='3.3'),
          tf('7.25 × 4.2, rounded to the nearest whole number, is 30.', key=True),
          mc('Divide. Round the quotient to the nearest hundredth.\n2 ÷ 7', ['0.29', '0.28', '0.3', '0.27']),
          sa('Multiply. Round the product to the nearest whole number.\n3.6 × 2.4', 'Product:', key='9'),
          tf('15 ÷ 4, rounded to the nearest whole number, is 3.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.4 (add)
    S('4.NBT.B.4', 'Add multi-digit whole numbers using the standard algorithm',
      main=[
          work('Use the standard algorithm to add. Show your work.\n4,587 + 2,946', 'Sum:', method=ADD_ALG, key='7,533'),
          work('Use the standard algorithm to add. Show your work.\n38,209 + 15,894', 'Sum:', method=ADD_ALG, key='54,103'),
          mc('Add.\n6,078 + 3,945', ['10,023', '9,023', '10,013', '9,923']),
          work('A library had 12,486 books. It got 3,758 more.\nUse the standard algorithm to find how many books it has now. Show your work.',
               'Books:', method=ADD_ALG, key='16,244'),
          tf('In the standard algorithm for 3,685 + 1,476, you regroup 11 ones as 1 ten and 1 one.', key=True),
      ],
      back=[
          B('Add within 1000', '3.NBT.A.2', [
              sa('Add.\n356 + 478', 'Sum:', key='834'),
              tf('609 + 295 = 904', key=True),
              mc('147 + 268 = ?', ['415', '405', '315', '425']),
              sa('Add.\n523 + 389', 'Sum:', key='912'),
              tf('480 + 360 = 740', key=False),
          ]),
          B('Add by place value, making a ten or a hundred', '2.NBT.B.7', [
              tf('7 ones and 5 ones make 1 ten and 2 ones.', key=True),
              sa('Rename 16 tens as hundreds and tens.', 'Answer:', key='1 hundred and 6 tens'),
              mc('Add the hundreds, the tens, and the ones.\n248 + 135', ['383', '373', '483', '313']),
              sa('Add.\n200 + 70 + 4 + 300 + 20 + 9', 'Sum:', key='603'),
              tf('12 ones is the same as 2 tens.', key=False),
          ]),
      ],
      f1=B('Add decimals to hundredths', '5.NBT.B.7', [
          sa('Add.\n35.68 + 7.45', 'Sum:', key='43.13'),
          sa('Add.\n4.9 + 12.36', 'Sum:', key='17.26'),
          mc('Add.\n0.75 + 0.48', ['1.23', '1.13', '0.123', '12.3']),
          tf('6.07 + 3.9 = 9.97', key=True),
          tf('2.5 + 1.75 = 3.80', key=False),
      ]),
      f2=B('Add multi-digit decimals with the standard algorithm', '6.NS.B.3', [
          sa('Add.\n128.406 + 75.89', 'Sum:', key='204.296'),
          sa('Add.\n9.075 + 0.98', 'Sum:', key='10.055'),
          mc('Add.\n46.3 + 8.759', ['55.059', '54.059', '55.159', '131.89']),
          tf('0.625 + 0.375 = 1', key=True),
          tf('12.48 + 3.6 = 12.84', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.4 (subtract)
    S('4.NBT.B.4', 'Subtract multi-digit whole numbers using the standard algorithm',
      main=[
          work('Use the standard algorithm to subtract. Show your work.\n8,253 - 4,678', 'Difference:', method=SUB_ALG, key='3,575'),
          work('Use the standard algorithm to subtract. Show your work.\n60,000 - 27,438', 'Difference:', method=SUB_ALG, key='32,562'),
          mc('Subtract.\n7,012 - 3,456', ['3,556', '4,444', '3,566', '4,656']),
          work('A school raised $15,250. It spent $8,795.\nUse the standard algorithm to find how much money is left. Show your work.',
               'Money left:', method=SUB_ALG, key='$6,455'),
          tf('To find 5,042 - 1,317 with the standard algorithm, you rename 1 ten as 10 ones.', key=True),
      ],
      back=[
          B('Subtract within 1000', '3.NBT.A.2', [
              sa('Subtract.\n732 - 485', 'Difference:', key='247'),
              tf('600 - 278 = 322', key=True),
              mc('514 - 296 = ?', ['218', '228', '318', '222']),
              sa('Subtract.\n905 - 467', 'Difference:', key='438'),
              tf('840 - 390 = 550', key=False),
          ]),
          B('Subtract by breaking apart a ten or a hundred', '2.NBT.B.7', [
              tf('To find 52 - 8, you can rename 1 ten as 10 ones.', key=True),
              sa('Rename 4 hundreds 2 tens as 3 hundreds and how many tens?', 'Tens:', key='12'),
              mc('Which shows 300 renamed so you can subtract 126?',
                 ['2 hundreds 9 tens 10 ones', '3 hundreds 10 tens', '2 hundreds 10 ones', '30 tens 1 one']),
              sa('Subtract.\n400 - 158', 'Difference:', key='242'),
              tf('6 tens 3 ones = 5 tens 3 ones', key=False),
          ]),
      ],
      f1=B('Subtract decimals to hundredths', '5.NBT.B.7', [
          sa('Subtract.\n42.5 - 18.76', 'Difference:', key='23.74'),
          sa('Subtract.\n9 - 3.45', 'Difference:', key='5.55'),
          mc('Subtract.\n6.03 - 2.8', ['3.23', '4.23', '3.75', '3.22']),
          tf('10 - 0.25 = 9.75', key=True),
          tf('5.4 - 2.15 = 3.35', key=False),
      ]),
      f2=B('Subtract multi-digit decimals with the standard algorithm', '6.NS.B.3', [
          sa('Subtract.\n100 - 36.875', 'Difference:', key='63.125'),
          sa('Subtract.\n15.06 - 8.3', 'Difference:', key='6.76'),
          mc('Subtract.\n4.2 - 1.375', ['2.825', '3.175', '2.925', '3.825']),
          tf('50.5 - 0.505 = 49.995', key=True),
          tf('8 - 0.08 = 0.72', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.5 (four-digit by one-digit)
    S('4.NBT.B.5', 'Multiply a whole number of up to four digits by a one-digit number',
      main=[
          sa('Multiply.\n4,236 × 7', 'Product:', key='29,652'),
          sa('Multiply.\n608 × 5', 'Product:', key='3,040'),
          mc('Multiply.\n3,049 × 6', ['18,294', '18,254', '18,924', '3,055']),
          sa('A theater sells 1,275 tickets each night for 8 nights.\nHow many tickets does it sell?', 'Tickets:', key='10,200'),
          tf('2,513 × 4 = 10,042', key=False),
      ],
      back=[
          B('Multiplication facts within 100', '3.OA.C.7', [
              sa('Multiply.\n7 × 6', 'Product:', key='42'),
              tf('9 × 8 = 72', key=True),
              mc('4 × 7 = ?', ['28', '24', '32', '11']),
              sa('Multiply.\n6 × 9', 'Product:', key='54'),
              tf('8 × 7 = 54', key=False),
          ]),
          B('Multiply one-digit numbers by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n7 × 80', 'Product:', key='560'),
              tf('5 × 60 = 300', key=True),
              mc('3 × 90 = ?', ['270', '27', '2,700', '93']),
              sa('Multiply.\n4 × 70', 'Product:', key='280'),
              tf('8 × 40 = 3,200', key=False),
          ]),
      ],
      f1=B('Multiply multi-digit whole numbers using the standard algorithm', '5.NBT.B.5', [
          work('Use the standard algorithm to multiply. Show your work.\n3,214 × 26', 'Product:', method=MUL_ALG, key='83,564'),
          sa('Multiply.\n507 × 48', 'Product:', key='24,336'),
          mc('Multiply.\n1,250 × 34', ['42,500', '42,050', '41,500', '8,750']),
          sa('Multiply.\n289 × 75', 'Product:', key='21,675'),
          tf('406 × 52 = 21,112', key=True),
      ]),
      f2=B('Multiply multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n4.236 × 7', 'Product:', key='29.652'),
          sa('Multiply.\n6.08 × 0.5', 'Product:', key='3.04'),
          mc('Multiply.\n30.49 × 0.6', ['18.294', '182.94', '1.8294', '18.94']),
          tf('2.5 × 1.6 = 4', key=True),
          tf('0.7 × 0.08 = 0.56', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.5 (two-digit by two-digit)
    S('4.NBT.B.5', 'Multiply two two-digit numbers',
      main=[
          sa('Multiply.\n34 × 27', 'Product:', key='918'),
          sa('Multiply.\n58 × 63', 'Product:', key='3,654'),
          mc('Multiply.\n46 × 19', ['874', '864', '884', '414']),
          sa('A box holds 24 cans.\nHow many cans are in 36 boxes?', 'Cans:', key='864'),
          tf('72 × 15 = 1,008', key=False),
      ],
      back=[
          B('Multiply one-digit numbers by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n3 × 40', 'Product:', key='120'),
              tf('6 × 90 = 540', key=True),
              mc('8 × 20 = ?', ['160', '16', '1,600', '28']),
              sa('Multiply.\n9 × 70', 'Product:', key='630'),
              tf('4 × 50 = 2,000', key=False),
          ]),
          B('Break apart a factor to multiply', '3.OA.B.5', [
              tf('8 × 7 = 8 × 5 + 8 × 2', key=True),
              sa('Fill in the blank.\n6 × 9 = 6 × 5 + 6 × ___', 'Blank:', key='4'),
              mc('Which expression is equal to 4 × 8?', ['4 × 5 + 4 × 3', '4 × 5 + 3', '4 + 5 × 3', '4 × 5 × 3']),
              sa('Find 7 × 6 by adding 7 × 3 + 7 × 3.', 'Product:', key='42'),
              tf('9 × 6 = 9 × 3 + 3', key=False),
          ]),
      ],
      f1=B('Multiply multi-digit whole numbers using the standard algorithm', '5.NBT.B.5', [
          work('Use the standard algorithm to multiply. Show your work.\n427 × 53', 'Product:', method=MUL_ALG, key='22,631'),
          sa('Multiply.\n86 × 145', 'Product:', key='12,470'),
          mc('Multiply.\n312 × 64', ['19,968', '19,868', '18,968', '1,248']),
          sa('Multiply.\n2,005 × 18', 'Product:', key='36,090'),
          tf('95 × 95 = 9,025', key=True),
      ]),
      f2=B('Multiply multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n3.4 × 2.7', 'Product:', key='9.18'),
          sa('Multiply.\n0.58 × 6.3', 'Product:', key='3.654'),
          mc('Multiply.\n4.6 × 0.19', ['0.874', '8.74', '0.0874', '4.79']),
          tf('2.4 × 3.6 = 8.64', key=True),
          tf('7.2 × 1.5 = 1.08', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.5 (models and explanations)
    S('4.NBT.B.5', 'Illustrate and explain multiplication with equations, arrays, and area models',
      main=[
          draw_write('Complete the area model for 7 × 38 by writing the area of each part.\nThen write the product.',
                     amodel('7', [(30, '30', '?'), (8, '8', '?')]), 'Product:',
                     draw='Areas written in the parts: 210 (7 × 30) and 56 (7 × 8)', key='266',
                     note='Grade both: the two areas must be 210 and 56, and the product 210 + 56 = 266.'),
          sa('The area model shows 24 × 13.\nWrite the four partial products and the total.', ['Partial products:', 'Total:'],
             key='200, 40, 60, 12; 312', note='The partial products may be listed in any order. Both parts are required.',
             fig=amodel2(['20', '4'], ['10', '3'], [['200', '40'], ['60', '12']])),
          mc('Which equation matches the area model?',
             ['6 × 453 = 2,400 + 300 + 18', '6 × 453 = 2,400 + 50 + 3', '6 + 453 = 2,718', '6 × 453 = 6 × 400 + 53'],
             fig=amodel('6', [(400, '400', '2,400'), (50, '50', '300'), (3, '3', '18')])),
          work('Use an area model or equations to multiply. Show your model or equations.\n9 × 2,146', 'Product:', key='19,314',
               method='Any valid area model or chain of equations that shows how the product is found. Examples: place-value parts '
                      '9 × 2,000 = 18,000, 9 × 100 = 900, 9 × 40 = 360 and 9 × 6 = 54, then 18,000 + 900 + 360 + 54 = 19,314; '
                      'or (10 - 1) × 2,146 = 21,460 - 2,146 = 19,314. '
                      'The answer without a valid model or equations earns partial credit.'),
          sa('Explain why 15 × 12 = 15 × 10 + 15 × 2.', ['Explanation:', ''],
             key='12 = 10 + 2, so 15 groups of 12 are 15 groups of 10 plus 15 groups of 2; 150 + 30 = 180.',
             note='Must show 12 split into 10 + 2 and that multiplying each part and adding gives the same product. '
                  'An array or area model split into 10 and 2 is also a correct explanation.'),
      ],
      back=[
          B('Use area to show the distributive property', '3.MD.C.7.c', [
              tf('A rectangle that is 4 by (5 + 3) has an area of 4 × 5 + 4 × 3.', key=True),
              sa('A 6-by-9 rectangle is split into a 6-by-5 part and a 6-by-4 part.\nWhat is the total area?', 'Area:', key='54 square units'),
              mc('A 3-by-8 rectangle is split into a 3-by-5 part and a 3-by-3 part.\nWhich expression gives its area?',
                 ['3 × 5 + 3 × 3', '3 × 5 × 3', '3 + 5 + 3', '3 × 8 + 3']),
              sa('Fill in the blank.\n7 × 9 = 7 × 5 + 7 × ___', 'Blank:', key='4'),
              tf('5 × 7 = 5 × 4 + 3', key=False),
          ]),
          B('Break apart an array to multiply', '3.OA.B.5', [
              sa('Write a multiplication equation for the array.', 'Equation:', key='4 × 6 = 24', fig=arr(4, 6),
                 note='6 × 4 = 24 is also correct.'),
              mc('The dashed line splits the array into two parts.\nWhich equation matches?',
                 ['4 × 7 = 4 × 5 + 4 × 2', '4 × 7 = 4 + 5 + 2', '4 × 7 = 4 × 5 × 2', '4 + 7 = 4 × 5 + 2'], fig=arr(4, 7, split=5)),
              tf('An array of 3 rows of 9 can be split into 3 rows of 5 and 3 rows of 4.', key=True),
              sa('An array of 6 rows of 8 is split into 6 rows of 5 and 6 rows of 3.\nHow many dots are in the whole array?', 'Dots:', key='48'),
              tf('An array of 5 rows of 6, split into two arrays of 5 rows of 3, has 33 dots.', key=False),
          ]),
      ],
      f1=B('Use place value and area models to multiply decimals', '5.NBT.B.7', [
          sa('An area model splits 3 × 2.4 into 3 × 2 and 3 × 0.4.\nWhat is the product?', 'Product:', key='7.2'),
          tf('4 × 1.25 = 4 × 1 + 4 × 0.25 = 5', key=True),
          mc('Which shows 6 × 3.5 broken apart by place value?', ['6 × 3 + 6 × 0.5', '6 × 3 + 0.5', '6 + 3 + 0.5', '6 × 3 × 0.5']),
          sa('Multiply.\n5 × 0.36', 'Product:', key='1.8'),
          tf('2 × 4.3 = 8.3', key=False),
      ]),
      f2=B('Use the distributive property to write a sum as a product', '6.NS.B.4', [
          sa('Use the factor 4 to write 36 + 8 as a product.', 'Expression:', key='4(9 + 2)'),
          tf('7(10 + 3) = 70 + 21', key=True),
          mc('Which expression equals 5 × 47?', ['5(40 + 7)', '5 × 40 + 7', '5 + 40 × 7', '(5 + 40) × 7']),
          sa('Use the greatest common factor to write 24 + 60 as a product.', 'Expression:', key='12(2 + 5)'),
          tf('3(12 + 5) = 36 + 5', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.6 (compute)
    S('4.NBT.B.6', 'Divide up to four-digit dividends by one-digit divisors, with remainders',
      main=[
          sa('Divide.\n952 ÷ 7', 'Quotient:', key='136'),
          sa('Divide.\n4,815 ÷ 5', 'Quotient:', key='963'),
          mc('Divide.\n2,184 ÷ 6', ['364', '354', '374', '2,178']),
          sa('Divide. Write the quotient and the remainder.\n1,357 ÷ 4', ['Quotient:', 'Remainder:'], key='339 R 1',
             note='Quotient 339 and remainder 1. The question asks for a remainder, so a mixed number or decimal is not accepted.'),
          tf('3,600 ÷ 9 = 40', key=False),
      ],
      back=[
          B('Division facts within 100', '3.OA.C.7', [
              sa('Divide.\n42 ÷ 7', 'Quotient:', key='6'),
              tf('72 ÷ 8 = 9', key=True),
              mc('54 ÷ 6 = ?', ['9', '8', '7', '48']),
              sa('Divide.\n27 ÷ 3', 'Quotient:', key='9'),
              tf('63 ÷ 9 = 8', key=False),
          ]),
          B('Share equally', '3.OA.A.2', [
              sa('28 marbles are shared equally by 4 children.\nHow many marbles does each child get?', 'Marbles:', key='7'),
              tf('When 45 is split into 5 equal groups, each group has 9.', key=True),
              mc('Which expression shows 32 shared equally among 8 people?', ['32 ÷ 8', '32 × 8', '32 - 8', '8 ÷ 32']),
              sa('48 stickers are put into groups of 6.\nHow many groups are there?', 'Groups:', key='8'),
              tf('20 shared equally by 4 people gives each person 16.', key=False),
          ]),
      ],
      f1=B('Divide with two-digit divisors', '5.NBT.B.6', [
          sa('Divide.\n1,736 ÷ 28', 'Quotient:', key='62'),
          sa('Divide.\n5,904 ÷ 72', 'Quotient:', key='82'),
          mc('Divide.\n3,360 ÷ 48', ['70', '7', '700', '68']),
          sa('Divide. Write the quotient and the remainder.\n2,000 ÷ 37', ['Quotient:', 'Remainder:'], key='54 R 2'),
          tf('1,125 ÷ 25 = 54', key=False),
      ]),
      f2=B('Divide multi-digit numbers with the standard algorithm', '6.NS.B.2', [
          work('Use the standard algorithm to divide. Show your work.\n9,516 ÷ 39', 'Quotient:', method=DIVISION_ALGORITHM, key='244'),
          sa('Divide.\n27,648 ÷ 72', 'Quotient:', key='384'),
          mc('Divide.\n15,525 ÷ 45', ['345', '335', '355', '3,450']),
          sa('Divide.\n8,184 ÷ 62', 'Quotient:', key='132'),
          tf('20,808 ÷ 51 = 408', key=True),
      ])),

    # ------------------------------------------------------------------ 4.NBT.B.6 (models and explanations)
    S('4.NBT.B.6', 'Illustrate and explain division with equations, area models, and place value',
      main=[
          draw_write('Complete the area model for 744 ÷ 6 by writing the missing length of each part.\nThen write the quotient.',
                     amodel('6', [(100, '?', '600'), (20, '?', '120'), (4, '?', '24')]), 'Quotient:',
                     draw='Lengths written on the parts: 100, 20 and 4', key='124',
                     note='Grade both: the lengths 100, 20 and 4 (6 × 100 = 600, 6 × 20 = 120, 6 × 4 = 24), and the quotient 124.'),
          sa('Explain how these equations show 852 ÷ 4.\n4 × 200 = 800\n4 × 13 = 52\n800 + 52 = 852', ['Quotient:', 'Explanation:'], key='213',
             note='Explanation: 852 is split into 800 and 52; 4 goes into them 200 times and 13 times, so 4 goes into 852 a total of 213 times.'),
          mc('Ana finds 3,515 ÷ 5 by thinking 3,500 ÷ 5 = 700 and 15 ÷ 5 = 3.\nWhat is the quotient?', ['703', '730', '7,003', '73']),
          work('Use an area model or equations to divide. Show your model or equations.\n1,792 ÷ 8', 'Quotient:', key='224',
               method='Any valid area model or chain of equations that shows how the quotient is found. Examples: split 1,792 into parts '
                      'that 8 divides, 8 × 200 = 1,600 and 8 × 24 = 192, with 1,600 + 192 = 1,792, so the quotient is 224; '
                      'or divide by 2 three times, 1,792 ÷ 2 = 896, 896 ÷ 2 = 448, 448 ÷ 2 = 224. '
                      'The answer without a valid model or equations earns partial credit.'),
          tf('To find 636 ÷ 3, you can divide each place: 600 ÷ 3 = 200, 30 ÷ 3 = 10, and 6 ÷ 3 = 2. The quotient is 212.', key=True),
      ],
      back=[
          B('Division as an unknown-factor problem', '3.OA.B.6', [
              sa('Find 56 ÷ 8 by thinking 8 × ? = 56.', 'Quotient:', key='7'),
              tf('36 ÷ 9 = 4 because 9 × 4 = 36.', key=True),
              mc('Which fact helps you find 45 ÷ 5?', ['5 × 9 = 45', '5 × 5 = 25', '45 - 5 = 40', '9 + 5 = 14']),
              sa('Find the unknown factor.\n7 × ? = 63', 'Factor:', key='9'),
              tf('24 ÷ 3 = 6 because 3 × 6 = 24.', key=False),
          ]),
          B('Find a missing side from the area of a rectangle', '3.MD.C.7.b', [
              sa('A rectangle has an area of 48 square units. One side is 6 units long.\nHow long is the other side?', 'Length:', key='8 units'),
              tf('A rectangle that is 7 units by 5 units has an area of 35 square units.', key=True),
              mc('A rectangle has an area of 36 square feet and a width of 4 feet.\nWhat is its length?', ['9 feet', '32 feet', '40 feet', '8 feet']),
              sa('What is the area of a rectangle that is 8 cm by 6 cm?', 'Area:', key='48 square cm'),
              tf('A rectangle with an area of 30 square units and one side of 5 units has another side of 25 units.', key=False),
          ]),
      ],
      f1=B('Explain division with two-digit divisors using area models and equations', '5.NBT.B.6', [
          sa('The area model shows 1,575 ÷ 25.\nWhat is the quotient?', 'Quotient:', key='63',
             fig=amodel('25', [(60, '60', '1,500'), (3, '?', '75')])),
          tf('An area model for 2,016 ÷ 48 can use parts with areas 1,920 and 96, so the quotient is 40 + 2 = 42.', key=True),
          mc('Which equations show 1,410 ÷ 30?',
             ['30 × 40 = 1,200; 30 × 7 = 210; 40 + 7 = 47', '30 × 4 = 120; 30 × 7 = 210; 4 + 7 = 11', '1,410 - 30 = 1,380', '30 × 47 = 1,140']),
          sa('Divide.\n2,262 ÷ 39', 'Quotient:', key='58'),
          tf('An area model for 1,344 ÷ 32 with parts 32 × 40 and 32 × 3 shows a quotient of 43.', key=False),
      ]),
      f2=B('Connect the standard division algorithm to partial quotients', '6.NS.B.2', [
          work('Use the standard algorithm to divide. Show your work.\n6,912 ÷ 24', 'Quotient:', method=DIVISION_ALGORITHM, key='288'),
          mc('In the standard algorithm for 4,284 ÷ 12, the first step uses 12 × 300 = 3,600.\nWhat does the 300 stand for?',
             ['Part of the quotient', 'The remainder', 'Part of the divisor', 'The dividend']),
          tf('The steps of the standard algorithm for 3,705 ÷ 15 match the partial quotients 200 + 40 + 7.', key=True),
          sa('Divide.\n10,488 ÷ 76', 'Quotient:', key='138'),
          tf('5,616 ÷ 52 = 118', key=False),
      ])),
]
