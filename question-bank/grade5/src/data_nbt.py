from qb import S, B, sa, mc, tf, nl, table, shape, poly, rect, plot, stack, draw_write, work, LONG_DIVISION, DIVISION_ALGORITHM
from common import bar, hgrid


def amodel(side, parts):
    """Division area model: one side length, then (width, top label, area label) for each part."""
    total = sum(w for w, _, _ in parts)
    h = 1.4
    polys, texts, x = [], [], 0
    for i, (w, top, area) in enumerate(parts):
        w = 1 + 1.6 * w / total          # not to scale, so small parts stay readable
        polys.append(poly([(x, 0), (x + w, 0), (x + w, h), (x, h)], [None, None, top, side if i == 0 else None]))
        texts.append((x + w / 2, h / 2, area))
        x += w
    desc = 'Area model (not to scale): a rectangle with side length %s, split into %d parts. ' % (side, len(parts))
    desc += '; '.join('part %d: length %s, area %s' % (i, top, area) for i, (_, top, area) in enumerate(parts, 1)) + '.'
    return shape(polys, texts=texts, fs=1.15, desc=desc)


ALG = ('The standard algorithm: one partial product for each digit of the second factor (with regrouping), each lined up '
       'by place value, then the partial products added. Another method (area model, repeated addition) earns partial credit.')


SETS = [
    # ------------------------------------------------------------------ 5.NBT.A.1 (10 times)
    S('5.NBT.A.1', 'A digit is worth 10 times as much as the same digit one place to its right',
      main=[
          mc('In 5,550, how does the value of the 5 in the hundreds place compare to the value of the 5 in the tens place?',
             ['It is 10 times as much.', 'It is 100 times as much.', 'It is the same.', 'It is {1/10} as much.']),
          sa('In 3.33, the first 3 is in the ones place and the second 3 is in the tenths place.\nHow many times as much is the first 3 worth as the second 3?',
             'Times as much:', key='10'),
          tf('In 0.77, the 7 in the tenths place is worth 10 times as much as the 7 in the hundredths place.', key=True),
          sa('Find the value of the 4 in 642.18 and the value of the 4 in 6,421.8.\nHow many times as much is the second 4 worth?',
             ['4 in 642.18:', '4 in 6,421.8:', 'Times as much:'], key='40; 400; 10 times as much'),
          mc('In which number is the 6 worth 10 times as much as the 6 in 3.6?', ['46.1', '3.06', '60.3', '0.36']),
      ],
      back=[
          B('Each place is worth 10 times the place to its right', '4.NBT.A.1', [
              tf('In 880, the 8 in the hundreds place is worth 10 times as much as the 8 in the tens place.', key=True),
              sa('What is the value of the 7 in 2,740?', 'Value:', key='700'),
              mc('Which number is 10 times as much as 60?', ['600', '70', '6', '6,000']),
              sa('How many tens are in 1 hundred?', 'Tens:', key='10'),
              tf('70 is 10 times as much as 7.', key=True),
          ]),
          B('Tenths and hundredths as decimals', '4.NF.C.6', [
              sa('Write {3/10} as a decimal.', 'Decimal:', key='0.3'),
              sa('Write {47/100} as a decimal.', 'Decimal:', key='0.47'),
              tf('0.6 = {6/100}', key=False),
              mc('Which decimal shows 5 hundredths?', ['0.05', '0.5', '5.0', '0.005']),
              sa('What decimal does the shaded part of the grid show?', 'Decimal:', key='0.23', fig=hgrid(23)),
          ]),
          B('Tenths as hundredths', '4.NF.C.5', [
              tf('{1/10} = {10/100}', key=True),
              sa('How many hundredths are in 1 tenth?', 'Hundredths:', key='10'),
              mc('Which fraction is equal to {4/10}?', ['{40/100}', '{4/100}', '{14/100}', '{400/100}']),
              sa('Find the missing number.\n{7/10} = {?/100}', 'Missing number:', key='70'),
              tf('{3/10} + {5/100} = {35/100}', key=True),
          ]),
      ],
      f1=B('Compute with multi-digit decimals', '6.NS.B.3', [
          sa('Add.\n27.6 + 4.38', 'Sum:', key='31.98'),
          sa('Subtract.\n50.2 - 7.65', 'Difference:', key='42.55'),
          mc('Multiply.\n1.2 × 0.4', ['0.48', '4.8', '0.048', '1.6']),
          sa('Divide.\n7.5 ÷ 2.5', 'Quotient:', key='3'),
          tf('0.3 × 0.3 = 0.9', key=False),
      ]),
      f2=B('Real-world problems with rational numbers', '7.NS.A.3', [
          sa('A diver at -4.5 m descends 2.25 m.\nWhat is the diver\'s new position?', 'Position:', key='-6.75 m'),
          sa('The temperature was 3.5°F. It fell 6.2°F.\nWhat is the new temperature?', 'Temperature:', key='-2.7°F'),
          mc('A stock\'s value changed by -$0.75 each day for 4 days.\nWhat was the total change?', ['-$3.00', '$3.00', '-$0.30', '-$4.75']),
          sa('A bank balance of -$12.40 increases by $20.00.\nWhat is the new balance?', 'Balance:', key='$7.60'),
          tf('-1.5 × 4 = 6', key=False),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.1 (one-tenth)
    S('5.NBT.A.1', 'A digit is worth 1/10 of the same digit one place to its left',
      main=[
          tf('In 44.4, the 4 in the tenths place is worth {1/10} of the 4 in the ones place.', key=True),
          mc('In 2.22, the 2 in the hundredths place is worth what part of the 2 in the tenths place?',
             ['{1/10}', '10 times as much', '{1/100}', 'The same amount']),
          sa('What is {1/10} of 50?', 'Answer:', key='5'),
          sa('What is {1/10} of 0.8?', 'Answer:', key='0.08'),
          mc('In which number is the 9 worth {1/10} of the 9 in 19.4?', ['5.92', '90.1', '9.01', '3.009']),
      ],
      back=[
          B('One place to the right is worth 1/10 as much', '4.NBT.A.1', [
              tf('In 330, the 3 in the tens place is worth {1/10} of the 3 in the hundreds place.', key=True),
              sa('Divide.\n400 ÷ 10', 'Quotient:', key='40'),
              mc('Which number is {1/10} of 3,000?', ['300', '30', '30,000', '3']),
              sa('How many hundreds are in 1 thousand?', 'Hundreds:', key='10'),
              tf('60 ÷ 10 = 600', key=False),
          ]),
          B('Unit fractions', '3.NF.A.1', [
              tf('{1/8} means 1 of 8 equal parts of a whole.', key=True),
              sa('A bar is cut into 6 equal parts.\nWhat fraction of the bar is one part?', 'Fraction:', key='1/6'),
              mc('Which fraction is greater?', ['{1/2}', '{1/8}']),
              tf('A whole cut into 4 equal parts has parts that are each {1/3} of the whole.', key=False),
              sa('What fraction of the bar is shaded?', 'Fraction:', key='1/8', fig=bar(8, 1)),
          ]),
          B('Decimals for tenths and hundredths', '4.NF.C.6', [
              sa('Write {9/100} as a decimal.', 'Decimal:', key='0.09'),
              sa('Write 0.8 as a fraction.', 'Fraction:', key='8/10', note='4/5 is also correct.'),
              tf('0.4 and 0.04 have the same value.', key=False),
              mc('Which decimal is equal to {6/10}?', ['0.6', '0.06', '6.0', '6.10']),
              sa('What decimal does the shaded part of the grid show?', 'Decimal:', key='0.70', note='0.7 is also correct.', fig=hgrid(70)),
          ]),
      ],
      f1=B('Divide multi-digit decimals', '6.NS.B.3', [
          sa('Divide.\n4.8 ÷ 0.4', 'Quotient:', key='12'),
          sa('Divide.\n9.36 ÷ 3', 'Quotient:', key='3.12'),
          mc('Divide.\n0.56 ÷ 0.7', ['0.8', '8', '0.08', '80']),
          sa('Divide.\n15 ÷ 0.25', 'Quotient:', key='60'),
          tf('6.3 ÷ 0.9 = 0.7', key=False),
      ]),
      f2=B('Write fractions as decimals using long division', '7.NS.A.2.d', [
          work('Use long division to write {7/8} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.875'),
          work('Use long division to write {2/9} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.222... (the 2 repeats)'),
          mc('Which fraction has a terminating decimal?', ['{3/20}', '{1/3}', '{5/6}', '{4/7}']),
          work('Use long division to write {9/20} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.45'),
          tf('The decimal form of {1/11} repeats.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.2 (whole numbers)
    S('5.NBT.A.2', 'Multiply and divide whole numbers by powers of 10; write powers of 10 with exponents',
      main=[
          sa('Multiply.\n37 × 1,000', 'Product:', key='37,000'),
          sa('Divide.\n45,000 ÷ 100', 'Quotient:', key='450'),
          sa('Write 10 × 10 × 10 × 10 as a power of 10.', 'Power of 10:', key='10⁴'),
          mc('6 × 10³ = ?', ['6,000', '600', '60,000', '18']),
          tf('820 ÷ 10² = 82', key=False),
      ],
      back=[
          B('Multiplying and dividing by 10', '4.NBT.A.1', [
              sa('Multiply.\n25 × 10', 'Product:', key='250'),
              tf('300 is 10 times as much as 30.', key=True),
              mc('Which number is 10 times as much as 450?', ['4,500', '45', '460', '45,000']),
              sa('How many tens are in 800?', 'Tens:', key='80'),
              sa('Divide.\n7,000 ÷ 10', 'Quotient:', key='700'),
          ]),
          B('Multiplying by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n4 × 60', 'Product:', key='240'),
              sa('Multiply.\n9 × 80', 'Product:', key='720'),
              tf('7 × 30 = 2,100', key=False),
              mc('5 × 90 = ?', ['450', '45', '4,500', '95']),
              sa('Multiply.\n8 × 70', 'Product:', key='560'),
          ]),
      ],
      f1=B('Write and evaluate whole-number exponents', '6.EE.A.1', [
          sa('Evaluate.\n3⁴', 'Value:', key='81'),
          sa('Write 5 × 5 × 5 using an exponent.', 'Exponent form:', key='5³'),
          mc('2⁵ = ?', ['32', '10', '25', '64']),
          sa('Evaluate.\n10³ + 2²', 'Value:', key='1,004'),
          tf('4³ = 12', key=False),
      ]),
      f2=B('Multiply and divide negative numbers by powers of 10', '7.NS.A.2.c', nearest=True, qs=[
          sa('Multiply.\n-3.5 × 100', 'Product:', key='-350'),
          sa('Divide.\n-420 ÷ 10', 'Quotient:', key='-42'),
          mc('-0.06 × 1,000 = ?', ['-60', '60', '-6', '-0.006']),
          sa('Divide.\n7.2 ÷ (-10)', 'Quotient:', key='-0.72'),
          tf('(-10) × (-10) × (-10) = -1,000', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.2 (decimal point)
    S('5.NBT.A.2', 'Place the decimal point when multiplying or dividing a decimal by a power of 10',
      main=[
          sa('Multiply.\n3.82 × 100', 'Product:', key='382'),
          sa('Divide.\n56.4 ÷ 10', 'Quotient:', key='5.64'),
          sa('Multiply.\n0.075 × 10²', 'Product:', key='7.5'),
          mc('Divide.\n2.9 ÷ 10³', ['0.0029', '0.029', '2,900', '0.29']),
          tf('When you multiply a number by 1,000, each digit moves 3 places to the left.', key=True),
      ],
      back=[
          B('Decimal notation for fractions', '4.NF.C.6', [
              sa('Write {35/100} as a decimal.', 'Decimal:', key='0.35'),
              tf('0.7 = {7/100}', key=False),
              mc('Which decimal is 2{4/10}?', ['2.4', '2.04', '24', '0.24']),
              sa('Write 0.09 as a fraction.', 'Fraction:', key='9/100'),
              tf('1.5 = 1{5/100}', key=False),
          ]),
          B('Place value when multiplying by 10 or 100', '4.NBT.A.1', [
              tf('When a whole number is multiplied by 10, each digit moves one place to the left.', key=True),
              sa('Multiply.\n64 × 100', 'Product:', key='6,400'),
              mc('3,500 ÷ 10 = ?', ['350', '35', '35,000', '3,510']),
              sa('Divide.\n9,000 ÷ 100', 'Quotient:', key='90'),
              tf('500 ÷ 10 = 5', key=False),
          ]),
      ],
      f1=B('Compute fluently with multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n2.4 × 0.35', 'Product:', key='0.84'),
          sa('Divide.\n1.44 ÷ 0.12', 'Quotient:', key='12'),
          mc('Multiply.\n12.5 × 0.8', ['10', '1', '100', '0.1']),
          sa('Add.\n0.875 + 12.4', 'Sum:', key='13.275'),
          tf('4.5 ÷ 0.05 = 9', key=False),
      ]),
      f2=B('Powers of 10 with negative rational numbers', '7.NS.A.2.c', nearest=True, qs=[
          sa('Find the value.\n-0.45 × 100', 'Value:', key='-45'),
          sa('Find the value.\n-63.5 ÷ 1,000', 'Value:', key='-0.0635'),
          mc('Find the value.\n(-2.7) × (-10)', ['27', '-27', '0.27', '-0.27']),
          sa('Find the value.\n0.8 × (-100)', 'Value:', key='-80'),
          tf('-5.2 ÷ 100 = -0.052', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.2 (explain the patterns)
    S('5.NBT.A.2', 'Explain patterns in the number of zeros and the placement of the decimal point',
      main=[
          sa('Explain why 46 × 1,000 = 46,000 has three more zeros than 46.', ['Explanation:', ''],
             key='Multiplying by 1,000 makes each digit worth 1,000 times as much, so each digit moves 3 places to the left; the 3 empty places (hundreds, tens, ones) are filled with zeros.',
             note='Must use place value: each factor of 10 moves every digit one place to the left (1,000 = 10 × 10 × 10, so three places) '
                  'and zeros fill the empty places. "Just add three zeros" without the place-value reason is not enough.'),
          mc('Why is 5.7 × 100 = 570?',
             ['Each digit becomes worth 100 times as much, so it moves 2 places to the left.', 'You write two zeros after 5.7.',
              'Each digit becomes worth {1/100} as much.', 'You move the decimal point 2 places to the left.']),
          tf('38 ÷ 10 = 3.8 because dividing by 10 makes each digit worth {1/10} as much, so each digit moves one place to the right.', key=True),
          sa('Mia says 2.4 × 10 = 2.40 because "multiplying by 10 adds a zero."\nGive the correct product and explain her mistake.',
             ['Correct product:', 'Explanation:'], key='24',
             note='Explanation: 2.40 has the same value as 2.4, so writing a zero after the decimal does not multiply by 10. '
                  'Multiplying by 10 makes each digit worth 10 times as much (2 ones become 2 tens, 4 tenths become 4 ones), so the product is 24.'),
          sa('10³ = 1,000.\nExplain how the exponent tells you the number of zeros.', ['Explanation:', ''],
             key='The exponent 3 means 10 is used as a factor 3 times (10 × 10 × 10); each factor of 10 moves the 1 one place to the left, so 1,000 has 3 zeros.',
             note='Must connect each factor of 10 to one place-value shift (one more zero).'),
      ],
      back=[
          B('A digit is worth 10 times as much as in the place to its right', '4.NBT.A.1', [
              tf('In 770, the 7 in the hundreds place is worth 10 times the 7 in the tens place.', key=True),
              mc('Why is 30 × 10 = 300?', ['The 3 tens become 3 hundreds.', 'The 3 moves one place to the right.',
                                           'You add 10 to 30.', 'Each digit becomes worth less.']),
              sa('How many tens are equal to 6 hundreds?', 'Tens:', key='60'),
              tf('In 5,505, the 5 in the thousands place is worth 10 times the 5 in the ones place.', key=False),
              sa('Write the number that is 10 times as much as 408.', 'Number:', key='4,080'),
          ]),
          B('Tenths as hundredths', '4.NF.C.5', [
              sa('Write {3/10} as a fraction with denominator 100.', 'Fraction:', key='30/100'),
              tf('{6/10} = {60/100}', key=True),
              mc('{40/100} = ?', ['{4/10}', '{40/10}', '{4/100}', '{400/10}']),
              sa('Add.\n{2/10} + {5/100}', 'Sum:', key='25/100', note='1/4 is also correct.'),
              tf('{7/10} = {7/100}', key=False),
          ]),
      ],
      f1=B('Explain decimal placement when multiplying and dividing decimals', '6.NS.B.3', [
          sa('Multiply.\n0.3 × 0.2', 'Product:', key='0.06'),
          mc('Why does 0.4 × 0.03 = 0.012 have three decimal places?',
             ['Tenths times hundredths gives thousandths.', 'Because 4 × 3 = 12.', 'Because 0.03 is greater than 0.4.',
              'Because the product is greater than 1.']),
          sa('Divide.\n7.2 ÷ 0.08', 'Quotient:', key='90'),
          tf('1.25 × 0.4 = 0.5', key=True),
          sa('Explain why 4.8 ÷ 0.6 has the same quotient as 48 ÷ 6.', ['Quotient:', 'Explanation:'], key='8',
             note='Both numbers were multiplied by 10 (4.8 becomes 48 and 0.6 becomes 6), which does not change the quotient.'),
      ]),
      f2=B('Write fractions as decimals and explain why they terminate or repeat', '7.NS.A.2.d', nearest=True, qs=[
          work('Use long division to write {3/8} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.375'),
          tf('{3/40} can be written as a decimal that ends.', key=True),
          mc('Which decimal equals {7/25}?', ['0.28', '0.35', '2.8', '0.07']),
          work('Use long division to write {5/12} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.41666... (the 6 repeats)'),
          tf('{2/3} = 0.67 exactly.', key=False),
      ]), num=59),

    # ------------------------------------------------------------------ 5.NBT.A.3.a (numerals and words)
    S('5.NBT.A.3.a', 'Read and write decimals to thousandths using numerals and words',
      main=[
          sa('Write the number in standard form.\nfour and twenty-six hundredths', 'Number:', key='4.26'),
          sa('Write 3.508 in words.', 'Words:', key='three and five hundred eight thousandths'),
          mc('Which number is nine and forty-one thousandths?', ['9.041', '9.41', '9.410', '9.0041']),
          sa('Write the number in standard form.\nseventeen and three tenths', 'Number:', key='17.3'),
          tf('0.072 is read "seventy-two hundredths."', key=False),
      ],
      back=[
          B('Decimals for tenths and hundredths', '4.NF.C.6', [
              sa('Write {6/100} as a decimal.', 'Decimal:', key='0.06'),
              tf('0.5 = {5/10}', key=True),
              mc('Which decimal is equal to {12/100}?', ['0.12', '1.2', '0.012', '12.0']),
              sa('Write 3{7/10} as a decimal.', 'Decimal:', key='3.7'),
              sa('What decimal does the shaded part of the grid show?', 'Decimal:', key='0.58', fig=hgrid(58)),
          ]),
          B('Reading and writing whole numbers', '4.NBT.A.2', [
              sa('Write the number in standard form.\ntwo thousand, four hundred six', 'Number:', key='2,406'),
              tf('5,030 is read "five thousand three hundred."', key=False),
              mc('Which number is eighty thousand, nine hundred?', ['80,900', '8,900', '80,090', '89,000']),
              sa('Write 607 in words.', 'Words:', key='six hundred seven'),
              sa('Write the number in standard form.\ntwelve thousand, fifty', 'Number:', key='12,050'),
          ]),
          B('Naming tenths and hundredths', '4.NF.C.5', [
              tf('Three tenths is equal to thirty hundredths.', key=True),
              sa('How many hundredths are in 4 tenths?', 'Hundredths:', key='40'),
              mc('Which fraction is "five hundredths"?', ['{5/100}', '{5/10}', '{50/100}', '{100/5}']),
              sa('Write "nine tenths" as a fraction.', 'Fraction:', key='9/10'),
              tf('{60/100} = {6/10}', key=True),
          ]),
      ],
      f1=B('Find and position rational numbers on a number line', '6.NS.C.6.c', [
          sa('What number does point P represent?', 'P =', key='-0.3', fig=nl(-1, 1, 0.1, pts=[(-0.3, 'P')], labels=[-1, 0, 1])),
          plot('Plot and label point Q at 0.45 on the number line.', nl(0.4, 0.5, 0.01, labels=[0.4, 0.5]),
               key='Point Q plotted at 0.45, the fifth tick after 0.4 (halfway between 0.4 and 0.5), and labeled'),
          mc('Which point is at -1.25?', ['Point A', 'Point B', 'Point C', 'Point D'],
             fig=nl(-2, 0, 0.25, pts=[(-1.25, 'A'), (-0.75, 'B'), (-1.75, 'C'), (-1.5, 'D')], labels=[-2, -1, 0])),
          sa('What number does point R represent?', 'R =', key='2.7', fig=nl(2, 3, 0.1, pts=[(2.7, 'R')], labels=[2, 3])),
          tf('On a number line, -0.6 is to the left of -0.5.', key=True),
      ]),
      f2=B('Write fractions as decimals', '7.NS.A.2.d', [
          work('Use long division to write {3/8} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.375'),
          work('Use long division to write {5/12} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.41666... (the 6 repeats)'),
          mc('{11/20} = ?', ['0.55', '0.11', '5.5', '0.2']),
          work('Use long division to write {4/9} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.444... (the 4 repeats)'),
          tf('{7/25} = 0.32', key=False),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.3.a (expanded form)
    S('5.NBT.A.3.a', 'Write decimals to thousandths in expanded form',
      main=[
          sa('Write 352.68 in expanded form.', 'Expanded form:',
             key='3 × 100 + 5 × 10 + 2 × 1 + 6 × (1/10) + 8 × (1/100)',
             note='300 + 50 + 2 + 0.6 + 0.08 is also correct.'),
          sa('Write the number in standard form.\n4 × 10 + 7 × 1 + 3 × {1/10} + 9 × {1/1000}', 'Number:', key='47.309'),
          mc('Which is the expanded form of 6.045?',
             ['6 × 1 + 4 × {1/100} + 5 × {1/1000}', '6 × 1 + 4 × {1/10} + 5 × {1/100}',
              '6 × 10 + 4 × {1/100} + 5 × {1/1000}', '6 + 45']),
          sa('Write the number in standard form.\n8 × 100 + 2 × {1/10} + 6 × {1/100}', 'Number:', key='800.26'),
          tf('0.908 = 9 × {1/10} + 8 × {1/1000}', key=True),
      ],
      back=[
          B('Expanded form of whole numbers', '4.NBT.A.2', [
              sa('Write 4,371 in expanded form.', 'Expanded form:', key='4,000 + 300 + 70 + 1',
                 note='4 × 1,000 + 3 × 100 + 7 × 10 + 1 × 1 is also correct.'),
              tf('6,052 = 6,000 + 500 + 2', key=False),
              mc('Which number is 7,000 + 400 + 9?', ['7,409', '7,490', '74,009', '7,049']),
              sa('Write 3 × 1,000 + 8 × 100 + 5 × 1 in standard form.', 'Number:', key='3,805'),
              tf('900 + 20 + 4 = 9,024', key=False),
          ]),
          B('Decimals and fractions with denominators 10 and 100', '4.NF.C.6', [
              sa('Write 0.6 as a fraction.', 'Fraction:', key='6/10', note='3/5 is also correct.'),
              tf('{4/100} = 0.4', key=False),
              mc('Which fraction is equal to 0.25?', ['{25/100}', '{25/10}', '{2/5}', '{1/25}']),
              sa('Write 2 + {3/10} + {7/100} as a decimal.', 'Decimal:', key='2.37'),
              tf('{9/10} = 0.09', key=False),
          ]),
      ],
      f1=B('Write expanded form with exponents', '6.EE.A.1', [
          sa('Write 5,000 + 300 + 20 + 7 using powers of 10.', 'Expression:', key='5 × 10³ + 3 × 10² + 2 × 10¹ + 7',
             note='Writing the last term as 7 × 10⁰ or 7 × 1 is also correct.'),
          sa('Evaluate.\n4 × 10³ + 6 × 10¹', 'Value:', key='4,060'),
          mc('Which number is equal to 10⁴?', ['10,000', '1,000', '40', '100,000']),
          sa('Write 600 + 90 + 1 using powers of 10.', 'Expression:', key='6 × 10² + 9 × 10¹ + 1'),
          tf('2 × 10² + 5 = 250', key=False),
      ]),
      f2=B('Decimal expansions of fractions', '7.NS.A.2.d', nearest=True, qs=[
          sa('Write {3/4} as a decimal.', 'Decimal:', key='0.75'),
          work('Use long division to write {1/6} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.1666... (the 6 repeats)'),
          mc('Which fraction is equal to 0.666... (the 6 repeats)?', ['{2/3}', '{3/5}', '{6/10}', '{1/6}']),
          work('Use long division to write {5/8} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.625'),
          tf('{2/5} = 0.4', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.3.b
    S('5.NBT.A.3.b', 'Compare decimals to thousandths',
      main=[
          sa('Write >, <, or = to compare.\n0.47 ___ 0.405', 'Symbol:', key='>'),
          sa('Write >, <, or = to compare.\n3.06 ___ 3.060', 'Symbol:', key='='),
          mc('Which number is greatest?', ['5.2', '5.19', '5.093', '5.199']),
          sa('Order from least to greatest.\n2.31, 2.301, 2.13, 2.3', 'Order:', key='2.13, 2.3, 2.301, 2.31'),
          tf('0.8 < 0.79', key=False),
      ],
      back=[
          B('Comparing decimals to hundredths', '4.NF.C.7', [
              sa('Write >, <, or = to compare.\n0.6 ___ 0.58', 'Symbol:', key='>'),
              tf('0.3 = 0.03', key=False),
              mc('Which number is less?', ['0.09', '0.1']),
              sa('Write >, <, or = to compare.\n0.75 ___ 0.8', 'Symbol:', key='<'),
              tf('0.42 > 0.5', key=False),
          ]),
          B('The symbols >, <, and =', '1.NBT.B.3', [
              mc('Which symbol means "is less than"?', ['<', '>', '=']),
              tf('9 > 6', key=True),
              sa('Write >, <, or = to compare.\n52 ___ 25', 'Symbol:', key='>'),
              tf('The symbol > means "is less than."', key=False),
              mc('Which statement is true?', ['14 < 41', '14 > 41', '14 = 41']),
          ]),
      ],
      f1=B('Order rational numbers', '6.NS.C.7.b', [
          sa('Write >, <, or = to compare.\n-0.4 ___ -0.45', 'Symbol:', key='>'),
          mc('Which number is least?', ['-2.5', '-2.05', '-2', '0.5']),
          sa('Order from least to greatest.\n-1.2, 0.3, -1.25, 0', 'Order:', key='-1.25, -1.2, 0, 0.3'),
          tf('-3.7 > -3.6', key=False),
          sa('A temperature of -2.5°C is colder than a temperature of -1.8°C.\nWrite an inequality to show this.', 'Inequality:',
             key='-2.5 < -1.8', note='-1.8 > -2.5 is also correct.'),
      ]),
      f2=B('Compare fractions and decimals using decimal expansions', '7.NS.A.2.d', [
          sa('Write {5/8} as a decimal.\nIs {5/8} greater than or less than 0.6?', ['Decimal:', 'Answer:'], key='0.625; greater than 0.6'),
          mc('Which number is greatest?', ['{4/5}', '0.78', '{3/4}', '0.7']),
          sa('Order from least to greatest.\n{2/3}, 0.6, {5/8}', 'Order:', key='0.6, 5/8, 2/3'),
          tf('{1/3} > 0.33', key=True),
          sa('Write >, <, or = to compare.\n{7/20} ___ 0.4', 'Symbol:', key='<'),
      ])),

    # ------------------------------------------------------------------ 5.NBT.A.4
    S('5.NBT.A.4', 'Round decimals to any place',
      main=[
          sa('Round 6.483 to the nearest tenth.', 'Rounded:', key='6.5'),
          sa('Round 12.749 to the nearest hundredth.', 'Rounded:', key='12.75'),
          mc('Round 0.865 to the nearest whole number.', ['1', '0', '0.9', '0.87']),
          sa('Round 39.96 to the nearest tenth.', 'Rounded:', key='40.0', note='40 is also correct.'),
          tf('4.351 rounded to the nearest hundredth is 4.36.', key=False),
      ],
      back=[
          B('Rounding whole numbers', '4.NBT.A.3', [
              sa('Round 4,682 to the nearest hundred.', 'Rounded:', key='4,700'),
              tf('350 rounded to the nearest hundred is 300.', key=False),
              mc('Round 7,249 to the nearest thousand.', ['7,000', '8,000', '7,200', '7,250']),
              sa('Round 85 to the nearest ten.', 'Rounded:', key='90'),
              tf('1,349 rounded to the nearest hundred is 1,400.', key=False),
          ]),
          B('Decimals on a number line', '4.NF.C.6', [
              sa('What decimal is at point A?', 'A =', key='0.6', fig=nl(0, 1, 0.1, pts=[(0.6, 'A')], labels=[0, 1])),
              tf('0.7 is closer to 1 than to 0.', key=True),
              mc('Is 0.43 closer to 0.4 or to 0.5?', ['0.4', '0.5']),
              sa('What decimal is at point B?', 'B =', key='3.2', fig=nl(3, 4, 0.1, pts=[(3.2, 'B')], labels=[3, 4])),
              tf('2.5 is halfway between 2 and 3.', key=True),
          ]),
      ],
      f1=B('Estimate to check computations with decimals', '6.NS.B.3', [
          sa('Round each number to the nearest whole number. Then add to estimate.\n18.7 + 6.25', 'Estimate:', key='25',
             note='19 + 6 = 25'),
          mc('Which is the best estimate of 4.9 × 6.1?', ['30', '24', '36', '11']),
          sa('Estimate 31.8 ÷ 7.9 by rounding each number to the nearest whole number.', 'Estimate:', key='4', note='32 ÷ 8 = 4'),
          tf('29.6 - 10.2 is about 40.', key=False),
          sa('Kim says 3.9 × 2.1 = 81.9.\nUse an estimate to decide whether her answer is reasonable. Write yes or no.', 'Answer:',
             key='No', note='3.9 × 2.1 is about 4 × 2 = 8, so 81.9 is far too large (the exact product is 8.19).'),
      ]),
      f2=B('Use estimation to judge whether an answer is reasonable', '7.EE.B.3', [
          sa('A $24.75 shirt is 20% off.\nRound the price to the nearest dollar. Then use the rounded price to estimate the sale price.',
             ['Rounded price:', 'Estimated sale price:'], key='$25; $20',
             note='$25 - 20% of $25 = $25 - $5 = $20 (or 0.8 × $25). Both parts are required. '
                  'The exact sale price, $19.80, is not the estimate asked for.'),
          mc('A worker earns $19.85 per hour for 9.75 hours.\nWhich is the best estimate of her pay?', ['$200', '$20', '$100', '$2,000']),
          tf('A 6.2% tax on $49.50 is about $3.', key=True),
          sa('Nina says {3/4} × 39.8 is about 40.\nRound 39.8 to the nearest whole number and estimate {3/4} × 39.8. Is her estimate reasonable?',
             ['Your estimate:', 'Reasonable?'], key='30; no',
             note='3/4 × 40 = 30, so 40 is not reasonable (the exact value is 29.85). Both parts are required.'),
          sa('A board is 8{1/4} feet long. It is cut into pieces that are 1{7/8} feet long.\nEstimate how many whole pieces can be cut.',
             'Estimate:', key='4 pieces', note='About 8 ÷ 2 = 4; the exact quotient is 4.4, so 4 whole pieces.'),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.5
    S('5.NBT.B.5', 'Multiply multi-digit whole numbers using the standard algorithm',
      main=[
          work('Use the standard algorithm to multiply. Show your work.\n246 × 37', 'Product:', key='9,102', method=ALG,
               note='Partial products: 246 × 7 = 1,722 and 246 × 30 = 7,380; 1,722 + 7,380 = 9,102.'),
          work('Use the standard algorithm to multiply. Show your work.\n1,385 × 24', 'Product:', key='33,240', method=ALG,
               note='Partial products: 1,385 × 4 = 5,540 and 1,385 × 20 = 27,700; 5,540 + 27,700 = 33,240.'),
          mc('This is the standard algorithm for 508 × 63 with one partial product missing.\nWhat is the missing partial product?',
             ['30,480', '3,048', '1,524', '31,904'], fig=stack('508', '× 63', '1,524', '+ ?', '32,004', rules=[2, 4])),
          work('Use the standard algorithm to multiply. Show your work.\n79 × 86', 'Product:', key='6,794', method=ALG,
               note='Partial products: 79 × 6 = 474 and 79 × 80 = 6,320; 474 + 6,320 = 6,794.'),
          work('A theater has 48 rows with 125 seats in each row.\nUse the standard algorithm to find how many seats are in the theater. Show your work.',
               'Seats:', key='6,000', method=ALG,
               note='Partial products: 125 × 8 = 1,000 and 125 × 40 = 5,000; 1,000 + 5,000 = 6,000.'),
      ],
      back=[
          B('Multiplying by a one-digit or two-digit number', '4.NBT.B.5', [
              sa('Multiply.\n346 × 7', 'Product:', key='2,422'),
              sa('Multiply.\n23 × 45', 'Product:', key='1,035'),
              tf('1,203 × 4 = 4,082', key=False),
              mc('62 × 18 = ?', ['1,116', '1,006', '496', '1,126']),
              sa('Multiply.\n58 × 30', 'Product:', key='1,740'),
          ]),
          B('Multiplication facts', '3.OA.C.7', [
              sa('Multiply.\n7 × 6', 'Product:', key='42'),
              sa('Multiply.\n8 × 9', 'Product:', key='72'),
              tf('6 × 9 = 56', key=False),
              mc('4 × 8 = ?', ['32', '36', '28', '24']),
              sa('Multiply.\n9 × 9', 'Product:', key='81'),
          ]),
          B('Adding partial products', '4.NBT.B.4', [
              sa('Add.\n7,380 + 1,722', 'Sum:', key='9,102'),
              sa('Add.\n27,700 + 5,540', 'Sum:', key='33,240'),
              tf('30,480 + 1,524 = 31,904', key=False),
              mc('6,400 + 394 = ?', ['6,794', '6,694', '6,784', '7,794']),
              sa('Add.\n4,800 + 1,200', 'Sum:', key='6,000'),
          ]),
      ],
      f1=B('Multiply multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n2.46 × 3.7', 'Product:', key='9.102'),
          sa('Multiply.\n13.85 × 2.4', 'Product:', key='33.24'),
          mc('Multiply.\n5.08 × 6.3', ['32.004', '320.04', '3.2004', '31.904']),
          sa('Multiply.\n0.79 × 8.6', 'Product:', key='6.794'),
          tf('1.25 × 4.8 = 60', key=False),
      ]),
      f2=B('Multiply integers', '7.NS.A.2.c', [
          sa('Find the product.\n(-24) × 15', 'Product:', key='-360'),
          sa('Find the product.\n(-12) × (-35)', 'Product:', key='420'),
          mc('Find the product.\n18 × (-21)', ['-378', '378', '-388', '-39']),
          sa('Find the product.\n(-3) × (-4) × (-25)', 'Product:', key='-300'),
          tf('(-6)(-7) = -42', key=False),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.6 (compute)
    S('5.NBT.B.6', 'Divide with up to four-digit dividends and two-digit divisors',
      main=[
          sa('Divide.\n2,016 ÷ 24', 'Quotient:', key='84'),
          sa('Divide.\n7,830 ÷ 45', 'Quotient:', key='174'),
          mc('Divide.\n952 ÷ 17', ['56', '54', '57', '46']),
          sa('Divide.\n3,724 ÷ 38', 'Quotient:', key='98'),
          sa('Divide. Write the quotient and the remainder.\n1,000 ÷ 32', ['Quotient:', 'Remainder:'], key='31 R 8',
             note='Quotient 31 and remainder 8 (31 R 8, or "31 remainder 8"). The question asks for a remainder, '
                  'so a mixed number or decimal (31 1/4, 31.25) is not accepted.'),
      ],
      back=[
          B('Dividing by a one-digit number', '4.NBT.B.6', [
              sa('Divide.\n852 ÷ 6', 'Quotient:', key='142'),
              sa('Divide.\n1,935 ÷ 5', 'Quotient:', key='387'),
              tf('728 ÷ 8 = 901', key=False),
              mc('504 ÷ 7 = ?', ['72', '62', '82', '71']),
              sa('Divide. Write the quotient and the remainder.\n95 ÷ 4', 'Quotient and remainder:', key='23 R 3'),
          ]),
          B('Multiplying to check a quotient', '4.NBT.B.5', [
              tf('To check 2,016 ÷ 24 = 84, you can multiply 24 × 84.', key=True),
              sa('Multiply to check 2,016 ÷ 24 = 84.\n24 × 84', 'Product:', key='2,016'),
              mc('Which product checks 952 ÷ 17 = 56?', ['17 × 56', '17 + 56', '952 × 17', '56 - 17']),
              sa('Multiply.\n38 × 98', 'Product:', key='3,724'),
              tf('32 × 31 + 8 = 1,000', key=True),
          ]),
          B('Division facts', '3.OA.C.7', [
              sa('Divide.\n72 ÷ 8', 'Quotient:', key='9'),
              sa('Divide.\n54 ÷ 9', 'Quotient:', key='6'),
              tf('63 ÷ 7 = 8', key=False),
              mc('40 ÷ 5 = ?', ['8', '7', '9', '6']),
              sa('Divide.\n35 ÷ 7', 'Quotient:', key='5'),
          ]),
      ],
      f1=B('Divide multi-digit numbers using the standard algorithm', '6.NS.B.2', [
          work('Use the standard algorithm to divide. Show your work.\n6,432 ÷ 48', 'Quotient:', method=DIVISION_ALGORITHM, key='134'),
          work('Use the standard algorithm to divide. Show your work.\n25,875 ÷ 69', 'Quotient:', method=DIVISION_ALGORITHM, key='375'),
          mc('Divide.\n14,040 ÷ 52', ['270', '27', '207', '2,700']),
          work('Use the standard algorithm to divide. Show your work.\n9,594 ÷ 41', 'Quotient:', method=DIVISION_ALGORITHM, key='234'),
          tf('11,700 ÷ 45 = 2,600', key=False),
      ]),
      f2=B('Divide integers', '7.NS.A.2.b', [
          sa('Find the quotient.\n-2,016 ÷ 24', 'Quotient:', key='-84'),
          sa('Find the quotient.\n(-952) ÷ (-17)', 'Quotient:', key='56'),
          mc('Find the quotient.\n780 ÷ (-15)', ['-52', '52', '-53', '-765']),
          sa('Find the quotient.\n-(144 ÷ 12)', 'Quotient:', key='-12'),
          tf('(-90) ÷ 18 = 90 ÷ (-18)', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.6 (area models)
    S('5.NBT.B.6', 'Explain division using area models and equations',
      main=[
          sa('The area model shows 1,248 ÷ 24.\nWhat is the quotient?', 'Quotient:', key='52',
             fig=amodel('24', [(40, '40', '960'), (12, '?', '288')])),
          sa('The area model shows 1,692 ÷ 36.\nWhat is the quotient?', 'Quotient:', key='47',
             fig=amodel('36', [(40, '40', '1,440'), (7, '?', '252')])),
          mc('Which equation matches the area model?', ['1,332 ÷ 18 = 74', '1,332 ÷ 74 = 20', '900 ÷ 18 = 74', '18 × 50 = 1,332'],
             fig=amodel('18', [(50, '50', '900'), (20, '20', '360'), (4, '4', '72')])),
          work('Use an area model or equations to divide. Show your model or equations.\n2,184 ÷ 28', 'Quotient:', key='78',
               method='An area model or equations that split 2,184 into parts that 28 divides, for example 28 × 70 = 1,960 and '
                      '28 × 8 = 224, with 1,960 + 224 = 2,184, so the quotient is 70 + 8 = 78. The answer 78 without a valid '
                      'model or equations earns partial credit.'),
          tf('1,248 ÷ 24 = (960 ÷ 24) + (288 ÷ 24)', key=True),
      ],
      back=[
          B('Area models for dividing by a one-digit number', '4.NBT.B.6', [
              sa('The area model shows 576 ÷ 4.\nWhat is the quotient?', 'Quotient:', key='144',
                 fig=amodel('4', [(100, '100', '400'), (40, '40', '160'), (4, '?', '16')])),
              tf('468 ÷ 3 = (300 ÷ 3) + (150 ÷ 3) + (18 ÷ 3)', key=True),
              mc('Which shows 245 ÷ 5 split into easier parts?',
                 ['(200 ÷ 5) + (45 ÷ 5)', '(200 ÷ 5) × (45 ÷ 5)', '200 ÷ (5 + 45)', '(245 ÷ 2) + (245 ÷ 3)']),
              sa('Divide.\n735 ÷ 7', 'Quotient:', key='105'),
              sa('A rectangle has an area of 312 square units and a width of 6 units.\nWhat is its length?', 'Length:', key='52 units'),
          ]),
          B('Area as length times width', '3.MD.C.7.b', [
              sa('A rectangle is 9 units long and 7 units wide.\nWhat is its area?', 'Area:', key='63 square units'),
              tf('A rectangle with an area of 40 square units and a side of 5 units has another side of 8 units.', key=True),
              mc('Which equation gives the area of a 6-by-8 rectangle?', ['6 × 8 = 48', '6 + 8 = 14', '2 × (6 + 8) = 28', '8 - 6 = 2']),
              sa('A rectangle has an area of 36 square units. One side is 4 units long.\nHow long is the other side?', 'Length:', key='9 units'),
              sa('Find the area of the rectangle.', 'Area:', key='30 square cm', fig=rect(10, 3, '10 cm', '3 cm')),
          ]),
          B('Splitting a rectangle to find its area', '3.MD.C.7.c', [
              tf('The area of a rectangle that is 4 by (10 + 3) equals 4 × 10 + 4 × 3.', key=True),
              sa('A 5-by-12 rectangle is split into a 5-by-10 rectangle and a 5-by-2 rectangle.\nWhat is the total area?', 'Area:',
                 key='60 square units'),
              mc('A 7-by-13 rectangle is split into a 7-by-10 part and a 7-by-3 part.\nWhich expression gives its area?',
                 ['7 × 10 + 7 × 3', '7 × 10 × 3', '7 + 10 + 3', '7 × 10 + 3']),
              sa('Fill in the blank.\n6 × 14 = 6 × 10 + 6 × ___', 'Blank:', key='4'),
              tf('8 × 12 = 8 × 10 + 2', key=False),
          ]),
      ],
      f1=B('Use the distributive property with the greatest common factor', '6.NS.B.4', [
          sa('Use the greatest common factor to write 36 + 48 as a product.', 'Expression:', key='12(3 + 4)'),
          sa('Find the greatest common factor of 32 and 56.', 'GCF:', key='8'),
          mc('Which expression is equal to 45 + 60 and uses the greatest common factor?',
             ['15(3 + 4)', '5(9 + 12)', '3(15 + 20)', '15(3 + 6)']),
          sa('Complete the equation.\n24 + 40 = 8(___ + ___)', ['First blank:', 'Second blank:'], key='3 and 5'),
          tf('18 + 27 = 9(2 + 3)', key=True),
      ]),
      f2=B('Factor and expand linear expressions', '7.EE.A.1', [
          sa('Factor using the greatest common factor.\n12x + 30', 'Expression:', key='6(2x + 5)'),
          sa('Expand.\n7(4y - 3)', 'Expression:', key='28y - 21'),
          mc('Which expression is equivalent to 18a - 24?', ['6(3a - 4)', '6(3a - 24)', '3(6a - 4)', '18(a - 6)']),
          sa('Factor out -4.\n-8n - 20', 'Expression:', key='-4(2n + 5)'),
          tf('4(2.5x + 3) = 10x + 3', key=False),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.6 (draw models and explain)
    S('5.NBT.B.6', 'Draw division models and explain the strategy',
      main=[
          draw_write('Complete the area model for 1,472 ÷ 32 by writing the area of each part.\nThen write the quotient.',
                     amodel('32', [(40, '40', '?'), (6, '6', '?')]), 'Quotient:',
                     draw='Areas written in the parts: 1,280 (32 × 40) and 192 (32 × 6)', key='46',
                     note='Grade both: the two areas must be 1,280 and 192 (they add to 1,472), and the quotient 40 + 6 = 46.'),
          work('Draw an area model to divide 1,615 ÷ 19.\nExplain how your model shows the quotient.', ['Quotient:', 'Explanation:'], key='85',
               method='An area model with side 19 split into parts whose areas add to 1,615 (for example 19 × 80 = 1,520 and 19 × 5 = 95); '
                      'the explanation says the part lengths (80 + 5) add up to the quotient because the part areas add up to the dividend.'),
          mc('Lena finds 1,380 ÷ 23 by thinking 23 × 60 = 1,380.\nWhich statement explains her strategy?',
             ['Division finds the missing factor: 23 × ? = 1,380, so the quotient is 60.', 'She subtracted 23 from 1,380 to get 60.',
              'She multiplied 1,380 by 23 to get 60.', 'She divided 23 by 1,380 to get 60.']),
          sa('Explain how these equations show 2,345 ÷ 35.\n35 × 60 = 2,100\n35 × 7 = 245\n2,100 + 245 = 2,345',
             ['Quotient:', 'Explanation:'], key='67',
             note='Explanation: 2,345 is split into 2,100 and 245; 35 goes into them 60 times and 7 times, so it goes into 2,345 a total of 60 + 7 = 67 times.'),
          tf('An area model for 1,512 ÷ 36 can use parts with areas 1,440 and 72, so the quotient is 40 + 2 = 42.', key=True),
      ],
      back=[
          B('Area models for dividing by a one-digit number', '4.NBT.B.6', [
              sa('The area model shows 384 ÷ 6.\nWhat is the missing length?', 'Length:', key='4',
                 fig=amodel('6', [(60, '60', '360'), (4, '?', '24')])),
              tf('An area model for 528 ÷ 4 can be split into 400 ÷ 4, 120 ÷ 4, and 8 ÷ 4.', key=True),
              mc('An area model for 945 ÷ 9 has parts with areas 900 and 45.\nWhat are the lengths of the parts?',
                 ['100 and 5', '90 and 5', '100 and 45', '10 and 5']),
              sa('Divide.\n672 ÷ 8', 'Quotient:', key='84'),
              tf('In an area model for 945 ÷ 9, the side length 9 is the quotient.', key=False),
          ]),
          B('Division as an unknown-factor problem', '3.OA.B.6', [
              sa('Find the unknown factor.\n6 × ? = 42', 'Factor:', key='7'),
              tf('32 ÷ 4 = 8 because 4 × 8 = 32.', key=True),
              mc('Which multiplication fact helps you find 56 ÷ 7?', ['7 × 8 = 56', '7 × 7 = 49', '56 × 7 = 392', '8 + 7 = 15']),
              sa('Find the unknown factor.\n? × 9 = 81', 'Factor:', key='9'),
              tf('To find 27 ÷ 3, you can ask "27 times what number is 3?"', key=False),
          ]),
      ],
      f1=B('Connect the standard division algorithm to partial quotients', '6.NS.B.2', [
          work('Use the standard algorithm to divide. Show your work.\n8,640 ÷ 36', 'Quotient:', method=DIVISION_ALGORITHM, key='240'),
          mc('In the standard algorithm for 5,712 ÷ 28, the first step uses 28 × 200 = 5,600.\nWhat does the 200 stand for?',
             ['Part of the quotient', 'The remainder', 'Part of the divisor', 'The dividend']),
          tf('The steps of the standard algorithm for 1,836 ÷ 17 match an area model with parts 17 × 100 and 17 × 8.', key=True),
          work('Use the standard algorithm to divide. Show your work.\n13,248 ÷ 46', 'Quotient:', method=DIVISION_ALGORITHM, key='288'),
          tf('3,825 ÷ 45 = 95', key=False),
      ]),
      f2=B('Solve real-world problems by dividing rational numbers', '7.NS.A.3', [
          sa('A diver goes down 126 feet in 18 equal stages.\nWrite the change in depth for each stage as a signed number.', 'Change:', key='-7 feet'),
          mc('A business lost $4,320 over 24 months, the same amount each month.\nWhich number shows the change each month?',
             ['-$180', '$180', '-$108', '-$1,800']),
          sa('The temperature fell 22.5°F in 9 hours at a steady rate.\nWrite the change per hour as a signed number.', 'Change:', key='-2.5°F'),
          tf('A change of -$1,512 shared equally over 36 weeks is a change of -$42 each week.', key=True),
          sa('A tank loses {3/4} gallon every hour.\nAfter how many hours is the change in the amount of water -6 gallons?', 'Hours:', key='8'),
      ]), num=60),

    # ------------------------------------------------------------------ 5.NBT.B.7 (add)
    S('5.NBT.B.7', 'Add decimals to hundredths',
      main=[
          sa('Add.\n23.45 + 8.7', 'Sum:', key='32.15'),
          sa('Add.\n15.3 + 6.48', 'Sum:', key='21.78'),
          mc('Add.\n4.06 + 12.9', ['16.96', '16.15', '5.35', '16.069']),
          sa('Add.\n9.65 + 0.8', 'Sum:', key='10.45'),
          sa('Maya had $18.50. She earned $6.75 more.\nHow much money does she have now?', 'Money:', key='$25.25'),
      ],
      back=[
          B('Adding multi-digit whole numbers', '4.NBT.B.4', [
              sa('Add.\n2,345 + 870', 'Sum:', key='3,215'),
              sa('Add.\n1,530 + 648', 'Sum:', key='2,178'),
              tf('406 + 1,290 = 1,596', key=False),
              mc('1,265 + 735 = ?', ['2,000', '1,990', '1,900', '2,100']),
              sa('Add.\n1,850 + 675', 'Sum:', key='2,525'),
          ]),
          B('Adding tenths and hundredths', '4.NF.C.5', [
              sa('Add.\n{3/10} + {45/100}', 'Sum:', key='75/100', note='3/4 or 0.75 is also correct.'),
              tf('{6/10} + {2/100} = {8/100}', key=False),
              mc('{7/10} + {15/100} = ?', ['{85/100}', '{22/100}', '{22/110}', '{85/10}']),
              sa('Write {4/10} as hundredths.', 'Fraction:', key='40/100'),
              tf('{5/10} + {5/100} = {10/100}', key=False),
          ]),
          B('Writing decimals with the same number of places', '4.NF.C.6', [
              tf('8.7 = 8.70', key=True),
              sa('Write 15.3 with two decimal places.', 'Decimal:', key='15.30'),
              mc('Which decimal is equal to 20?', ['20.00', '2.00', '0.20', '200.0']),
              tf('6.4 = 6.04', key=False),
              sa('Write 12.9 with a digit in the hundredths place, without changing its value.', 'Decimal:', key='12.90'),
          ]),
      ],
      f1=B('Add multi-digit decimals', '6.NS.B.3', [
          sa('Add.\n128.47 + 9.605', 'Sum:', key='138.075'),
          sa('Add.\n54.2 + 18.376', 'Sum:', key='72.576'),
          mc('Add.\n0.952 + 3.48 + 11.6', ['16.032', '15.032', '16.132', '4.53']),
          sa('Add.\n99.6 + 0.485', 'Sum:', key='100.085'),
          tf('7.3 + 2.145 = 2.875', key=False),
      ]),
      f2=B('Add rational numbers', '7.NS.A.1.d', [
          sa('Find the value.\n-12.5 + 4.75', 'Value:', key='-7.75'),
          sa('Find the value.\n3.2 + (-8.45)', 'Value:', key='-5.25'),
          mc('Find the value.\n-6.3 + (-2.85)', ['-9.15', '-3.45', '3.45', '9.15']),
          sa('Find the value.\n-4.6 + 10.25', 'Value:', key='5.65'),
          tf('-1.5 + 1.5 = 0', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.7 (subtract)
    S('5.NBT.B.7', 'Subtract decimals to hundredths',
      main=[
          sa('Subtract.\n15.3 - 6.48', 'Difference:', key='8.82'),
          sa('Subtract.\n20 - 7.35', 'Difference:', key='12.65'),
          sa('Maya had $18.50. She spent $6.75.\nHow much money does she have left?', 'Money left:', key='$11.75'),
          mc('Subtract.\n9.04 - 3.7', ['5.34', '6.34', '5.44', '8.67']),
          tf('6.5 - 2.75 = 3.75', key=True),
      ],
      back=[
          B('Subtracting multi-digit whole numbers', '4.NBT.B.4', [
              sa('Subtract.\n1,530 - 648', 'Difference:', key='882'),
              mc('2,000 - 735 = ?', ['1,265', '1,365', '1,275', '2,735']),
              sa('Subtract.\n1,850 - 675', 'Difference:', key='1,175'),
              tf('5,000 - 1,234 = 3,766', key=True),
              sa('Subtract.\n4,206 - 1,519', 'Difference:', key='2,687'),
          ]),
          B('Subtracting mixed numbers in tenths and hundredths', '4.NF.B.3.c', [
              sa('Subtract.\n5{3/10} - 2{6/10}', 'Difference:', key='2 7/10', note='27/10 is also correct.'),
              tf('4 - {35/100} = 3{65/100}', key=True),
              mc('6{2/10} - 1{9/10} = ?', ['4{3/10}', '5{7/10}', '4{7/10}', '5{3/10}']),
              sa('Subtract.\n3{40/100} - 1{25/100}', 'Difference:', key='2 15/100', note='2 3/20 is also correct.'),
              tf('2{1/10} - {5/10} = 2{4/10}', key=False),
          ]),
      ],
      f1=B('Subtract multi-digit decimals', '6.NS.B.3', [
          sa('Subtract.\n54.2 - 18.376', 'Difference:', key='35.824'),
          sa('Subtract.\n100 - 0.485', 'Difference:', key='99.515'),
          tf('7.3 - 2.145 = 5.245', key=False),
          sa('Subtract.\n12.06 - 4.875', 'Difference:', key='7.185'),
          mc('Subtract.\n30 - 0.009', ['29.991', '29.001', '29.91', '30.009']),
      ]),
      f2=B('Subtract rational numbers', '7.NS.A.1.d', [
          sa('Find the value.\n3.2 - 8.45', 'Value:', key='-5.25'),
          sa('Find the value.\n-4.6 - (-10.25)', 'Value:', key='5.65'),
          sa('Find the value.\n-2.75 - 4.5', 'Value:', key='-7.25'),
          mc('Find the value.\n1.2 - (-3.65)', ['4.85', '-2.45', '2.45', '-4.85']),
          tf('-8.1 - (-8.1) = 0', key=True),
      ]), num=61),

    # ------------------------------------------------------------------ 5.NBT.B.7 (models for adding and subtracting)
    S('5.NBT.B.7', 'Use place-value models to add and subtract decimals and explain the method',
      main=[
          draw_write('Shade the grid to show 0.4 + 0.25.\nThen write the sum.', hgrid(0), 'Sum:',
                     draw='65 of the 100 squares shaded: 40 squares (4 columns) for 0.4 and 25 more for 0.25', key='0.65',
                     note='Grade both: 65 squares shaded, and the sum 0.65.'),
          sa('Explain why you line up the decimal points to add 3.6 + 2.45.', ['Sum:', 'Explanation:'], key='6.05',
             note='Explanation: lining up the decimal points lines up digits with the same place value (ones with ones, tenths with tenths, '
                  'hundredths with hundredths), so like units are added; 3.6 can be written 3.60.'),
          mc('Which describes a place-value model for 1.3 - 0.45?',
             ['Start with 1 one and 3 tenths, trade 1 tenth for 10 hundredths, then take away 4 tenths and 5 hundredths.',
              'Take away 4 ones and 5 tenths from 1 one and 3 tenths.',
              'Take away 1 one and 3 tenths from 4 tenths and 5 hundredths.',
              'Add 4 tenths and 5 hundredths to 1 one and 3 tenths.']),
          tf('To find 0.7 - 0.25, you can rename 0.7 as 70 hundredths and subtract 25 hundredths to get 45 hundredths.', key=True),
          sa('Raj added 4.2 + 1.35 and got 1.77.\nFind the correct sum and explain his mistake.', ['Correct sum:', 'Explanation:'], key='5.55',
             note='Explanation: he lined up the last digits instead of the decimal points, so he added as if 4.2 were 0.42. '
                  'Lining up the decimal points gives 4.20 + 1.35 = 5.55.'),
      ],
      back=[
          B('Add tenths and hundredths', '4.NF.C.5', [
              sa('Add.\n{4/10} + {25/100}', 'Sum:', key='65/100', note='0.65 is also correct.'),
              tf('{3/10} = {30/100}', key=True),
              mc('{8/10} + {7/100} = ?', ['{87/100}', '{15/100}', '{15/110}', '{87/10}']),
              sa('Write {6/10} as hundredths.', 'Fraction:', key='60/100'),
              tf('{2/10} + {9/100} = {11/100}', key=False),
          ]),
          B('Rename a unit as ten of the next smaller unit', '4.NBT.A.1', [
              sa('How many tens are equal to 1 hundred?', 'Tens:', key='10'),
              tf('3 hundreds 4 tens can be renamed as 2 hundreds 14 tens.', key=True),
              mc('Which shows 52 renamed so that you can take away 8 ones?', ['4 tens 12 ones', '5 tens 12 ones', '4 tens 2 ones', '6 tens 2 ones']),
              sa('Rename 4 thousands as hundreds.', 'Hundreds:', key='40'),
              tf('7 tens 3 ones = 6 tens 3 ones', key=False),
          ]),
      ],
      f1=B('Add and subtract multi-digit decimals with the standard algorithm', '6.NS.B.3', [
          sa('Add.\n36.075 + 8.9', 'Sum:', key='44.975'),
          sa('Subtract.\n41.2 - 7.865', 'Difference:', key='33.335'),
          mc('Add.\n0.68 + 4.795', ['5.475', '5.375', '4.863', '11.475']),
          sa('Subtract.\n9 - 2.468', 'Difference:', key='6.532'),
          tf('12.5 + 0.375 = 12.875', key=True),
      ]),
      f2=B('Add and subtract rational numbers', '7.NS.A.1.d', [
          sa('Find the value.\n-3.25 + 7.6', 'Value:', key='4.35'),
          sa('Find the value.\n0.8 - 2.35', 'Value:', key='-1.55'),
          mc('Find the value.\n-1.75 + (-0.6)', ['-2.35', '-1.15', '1.15', '2.35']),
          tf('5.5 - 7.25 = -1.75', key=True),
          sa('Find the value.\n-9.4 - (-2.65)', 'Value:', key='-6.75'),
      ]), num=62),


    # ------------------------------------------------------------------ 5.NBT.B.7 (multiply)
    S('5.NBT.B.7', 'Multiply decimals to hundredths',
      main=[
          sa('Multiply.\n3.4 × 6', 'Product:', key='20.4'),
          sa('Multiply.\n0.7 × 0.5', 'Product:', key='0.35'),
          mc('Multiply.\n2.5 × 1.2', ['3', '30', '0.3', '3.7']),
          sa('Multiply.\n0.06 × 8', 'Product:', key='0.48'),
          sa('A pen costs $1.25.\nHow much do 7 pens cost?', 'Cost:', key='$8.75'),
      ],
      back=[
          B('Multiplying whole numbers', '4.NBT.B.5', [
              sa('Multiply.\n34 × 6', 'Product:', key='204'),
              sa('Multiply.\n25 × 12', 'Product:', key='300'),
              tf('125 × 7 = 785', key=False),
              mc('18 × 4 = ?', ['72', '64', '82', '48']),
              sa('Multiply.\n106 × 8', 'Product:', key='848'),
          ]),
          B('Decimals as tenths and hundredths', '4.NF.C.6', [
              sa('Write 35 hundredths as a decimal.', 'Decimal:', key='0.35'),
              tf('0.4 is 4 tenths.', key=True),
              mc('Which decimal is 204 tenths?', ['20.4', '2.04', '204', '0.204']),
              sa('How many hundredths are in 0.48?', 'Hundredths:', key='48'),
              tf('0.06 is 6 tenths.', key=False),
          ]),
          B('Multiply a whole number by tenths or hundredths', '4.NF.B.4.b', [
              sa('Multiply.\n4 × {3/10}', 'Product:', key='12/10', note='1 2/10, 6/5, and 1.2 are also correct.'),
              tf('6 × {5/100} = {30/100}', key=True),
              mc('3 × {7/10} = ?', ['{21/10}', '{21/30}', '{10/10}', '{7/30}']),
              sa('A cup holds {3/10} liter.\nHow many liters do 5 cups hold? Write a fraction.', 'Liters:', key='15/10',
                 note='1 5/10, 3/2, 1 1/2, and 1.5 are also correct.'),
              tf('8 × {2/100} = {16/800}', key=False),
          ], num=4),
      ],
      f1=B('Multiply multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n3.45 × 0.6', 'Product:', key='2.07'),
          sa('Multiply.\n12.08 × 2.5', 'Product:', key='30.2'),
          mc('Multiply.\n0.125 × 0.4', ['0.05', '0.5', '0.005', '5']),
          sa('Multiply.\n7.2 × 1.15', 'Product:', key='8.28'),
          tf('0.03 × 0.03 = 0.09', key=False),
      ]),
      f2=B('Multiply rational numbers', '7.NS.A.2.c', [
          sa('Find the product.\n-3.4 × 6', 'Product:', key='-20.4'),
          sa('Find the product.\n(-0.7) × (-0.5)', 'Product:', key='0.35'),
          mc('Find the product.\n2.5 × (-1.2)', ['-3', '3', '-30', '-0.3']),
          sa('Find the product.\n(-0.06) × 8', 'Product:', key='-0.48'),
          tf('(-1.25) × (-4) = -5', key=False),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.7 (models for multiplying)
    S('5.NBT.B.7', 'Use models and place value to multiply decimals and explain the method',
      main=[
          draw_write('Shade the grid to show 3 × 0.15.\nThen write the product.', hgrid(0), 'Product:',
                     draw='45 of the 100 squares shaded, as three groups of 15 squares', key='0.45',
                     note='Grade both: three groups of 15 hundredths (45 squares) shaded, and the product 0.45.'),
          sa('On a hundredths grid, 0.3 × 0.4 is where 3 tenths (3 columns) and 4 tenths (4 rows) overlap.\nExplain why the product is 0.12.',
             ['Explanation:', ''],
             key='The overlap is 3 columns by 4 rows of small squares, which is 12 squares; each small square is one hundredth, so 0.3 × 0.4 = 12 hundredths = 0.12.',
             note='Must say that tenths times tenths gives hundredths (each small square is 1/100) and that 3 × 4 = 12 squares overlap.'),
          mc('Which explains why 4 × 0.25 = 1?',
             ['4 groups of 25 hundredths is 100 hundredths, which is 1 whole.', '4 × 25 = 100, so the product is 100.',
              '4 + 0.25 is about 4, so the product is about 1.', '0.25 has two decimal places, so the product is 0.01.']),
          tf('2 × 0.35 = 0.70 because 2 groups of 35 hundredths is 70 hundredths.', key=True),
          sa('Lia says 0.5 × 0.6 = 3.0.\nGive the correct product and use place value to explain her mistake.', ['Correct product:', 'Explanation:'],
             key='0.3', note='5 tenths × 6 tenths = 30 hundredths = 0.30, because tenths times tenths are hundredths. She counted the product as tenths. 0.30 is also correct.'),
      ],
      back=[
          B('Multiply a fraction in tenths or hundredths by a whole number', '4.NF.B.4.b', [
              sa('Multiply.\n3 × {15/100}', 'Product:', key='45/100', note='0.45 and 9/20 are also correct.'),
              tf('2 × {35/100} = {70/100}', key=True),
              mc('4 × {6/10} = ?', ['{24/10}', '{24/40}', '{10/10}', '{6/40}']),
              sa('Write 7 × {2/10} as one fraction.', 'Fraction:', key='14/10', note='1 4/10, 7/5, and 1.4 are also correct.'),
              tf('6 × {4/100} = {24/600}', key=False),
          ]),
          B('Multiplication as equal groups', '3.OA.A.1', [
              sa('There are 3 groups with 15 counters in each group.\nHow many counters are there in all?', 'Counters:', key='45'),
              tf('4 × 25 can mean 4 groups of 25.', key=True),
              mc('Which can 2 × 35 mean?', ['2 groups of 35', '2 more than 35', '35 take away 2', '2 groups of 3 and 5']),
              sa('Write a multiplication equation for 6 groups of 4.', 'Equation:', key='6 × 4 = 24'),
              tf('3 × 8 means 3 more than 8.', key=False),
          ]),
      ],
      f1=B('Multiply multi-digit decimals', '6.NS.B.3', [
          sa('Multiply.\n0.24 × 0.5', 'Product:', key='0.12'),
          sa('Multiply.\n3.6 × 0.15', 'Product:', key='0.54'),
          mc('Multiply.\n1.6 × 0.45', ['0.72', '7.2', '0.072', '2.05']),
          sa('Multiply.\n0.08 × 0.7', 'Product:', key='0.056'),
          tf('2.5 × 0.04 = 1', key=False),
      ]),
      f2=B('Multiply rational numbers', '7.NS.A.2.c', [
          sa('Find the product.\n(-0.3) × 0.4', 'Product:', key='-0.12'),
          sa('Find the product.\n(-2.5) × (-0.6)', 'Product:', key='1.5'),
          mc('Find the product.\n3 × (-0.15)', ['-0.45', '0.45', '-4.5', '-0.045']),
          tf('(-0.2) × (-0.2) × (-0.2) = -0.008', key=True),
          sa('Find the product.\n-1.2 × 0.05', 'Product:', key='-0.06'),
      ]), num=63),

    # ------------------------------------------------------------------ 5.NBT.B.7 (divide)
    S('5.NBT.B.7', 'Divide decimals to hundredths',
      main=[
          sa('Divide.\n8.4 ÷ 4', 'Quotient:', key='2.1'),
          sa('Divide.\n3.6 ÷ 0.6', 'Quotient:', key='6'),
          mc('Divide.\n0.45 ÷ 0.05', ['9', '0.9', '90', '0.09']),
          sa('Divide.\n7.5 ÷ 0.3', 'Quotient:', key='25'),
          sa('A rope is 4.8 meters long. It is cut into pieces that are each 0.6 meter long.\nHow many pieces are there?',
             'Pieces:', key='8'),
      ],
      back=[
          B('Dividing whole numbers', '4.NBT.B.6', [
              sa('Divide.\n84 ÷ 4', 'Quotient:', key='21'),
              sa('Divide.\n360 ÷ 6', 'Quotient:', key='60'),
              tf('450 ÷ 5 = 9', key=False),
              mc('750 ÷ 3 = ?', ['250', '25', '2,500', '260']),
              sa('Divide.\n48 ÷ 6', 'Quotient:', key='8'),
          ]),
          B('Division as an unknown-factor problem', '3.OA.B.6', [
              sa('Find 36 ÷ 6 by thinking 6 × □ = 36.', 'Quotient:', key='6'),
              tf('7 × 9 = 63, so 63 ÷ 7 = 9.', key=True),
              mc('Which fact helps you find 56 ÷ 8?', ['8 × 7 = 56', '8 + 48 = 56', '56 × 8 = 448', '8 - 7 = 1']),
              sa('What number goes in the box?\n□ × 5 = 45', 'Number:', key='9'),
              tf('24 ÷ 3 = 6 because 3 × 6 = 24.', key=False),
          ]),
          B('Rename decimals as tenths or hundredths', '4.NF.C.6', [
              sa('How many tenths are in 3.6?', 'Tenths:', key='36'),
              tf('0.45 is 45 hundredths.', key=True),
              mc('How many hundredths are in 0.05?', ['5', '50', '0.5', '500']),
              sa('How many tenths are in 0.6?', 'Tenths:', key='6'),
              tf('7.5 is 75 hundredths.', key=False),
          ], num=4),
      ],
      f1=B('Divide multi-digit decimals', '6.NS.B.3', [
          sa('Divide.\n13.65 ÷ 0.35', 'Quotient:', key='39'),
          sa('Divide.\n9.072 ÷ 2.4', 'Quotient:', key='3.78'),
          mc('Divide.\n0.081 ÷ 0.09', ['0.9', '9', '0.09', '90']),
          sa('Divide.\n52.5 ÷ 1.25', 'Quotient:', key='42'),
          tf('1.8 ÷ 0.006 = 3', key=False),
      ]),
      f2=B('Divide rational numbers', '7.NS.A.2.b', [
          sa('Find the quotient.\n-8.4 ÷ 4', 'Quotient:', key='-2.1'),
          sa('Find the quotient.\n(-3.6) ÷ (-0.6)', 'Quotient:', key='6'),
          mc('Find the quotient.\n0.45 ÷ (-0.05)', ['-9', '9', '-0.9', '0.9']),
          sa('Find the quotient.\n-7.5 ÷ 0.3', 'Quotient:', key='-25'),
          tf('-(4.8 ÷ 0.6) = (-4.8) ÷ 0.6', key=True),
      ])),

    # ------------------------------------------------------------------ 5.NBT.B.7 (models for dividing)
    S('5.NBT.B.7', 'Use models and place value to divide decimals and explain the method',
      main=[
          draw_write('The grid shows 0.6 shaded.\nCircle groups of 0.15 to find 0.6 ÷ 0.15. Then write the quotient.', hgrid(60), 'Quotient:',
                     draw='The 60 shaded squares circled as 4 groups of 15 squares', key='4',
                     note='Grade both: four groups of 15 hundredths circled, and the quotient 4.'),
          mc('Which explains why 1.8 ÷ 0.3 = 6?',
             ['There are 6 groups of 3 tenths in 18 tenths.', 'There are 6 groups of 1.8 in 0.3.', '1.8 - 0.3 = 6',
              '0.3 has one decimal place, so the quotient is 0.6.']),
          sa('Explain how to find 2.4 ÷ 4 by thinking of 2.4 as 24 tenths.', ['Quotient:', 'Explanation:'], key='0.6',
             note='24 tenths ÷ 4 = 6 tenths = 0.6. The explanation must use the unit (tenths), not only "move the decimal point".'),
          tf('4.5 ÷ 0.9 = 5 because there are 5 groups of 9 tenths in 45 tenths.', key=True),
          sa('Sam says 0.8 ÷ 0.2 = 0.4.\nGive the correct quotient and use a model or place value to explain why he is wrong.',
             ['Correct quotient:', 'Explanation:'], key='4',
             note='0.8 is 8 tenths and 0.2 is 2 tenths; there are 4 groups of 2 tenths in 8 tenths, so the quotient is 4. '
                  'Accept a described drawing or a units explanation.'),
      ],
      back=[
          B('Division as the number of equal groups', '3.OA.A.2', [
              sa('18 counters are put into groups of 3.\nHow many groups are there?', 'Groups:', key='6'),
              tf('24 ÷ 4 can mean "how many groups of 4 are in 24?"', key=True),
              mc('Which question does 35 ÷ 5 answer?', ['How many groups of 5 are in 35?', 'What is 35 more than 5?',
                                                         'How many are in 5 groups of 35?', 'What is 35 take away 5?']),
              sa('There are 28 apples. Each bag holds 7 apples.\nHow many bags are needed?', 'Bags:', key='4'),
              tf('12 ÷ 3 means 12 groups of 3.', key=False),
          ]),
          B('Decimals as tenths and hundredths', '4.NF.C.6', [
              sa('How many tenths are in 1.8?', 'Tenths:', key='18'),
              tf('0.15 is 15 hundredths.', key=True),
              mc('How many hundredths are in 0.6?', ['60', '6', '600', '0.6']),
              sa('Write 45 tenths as a decimal.', 'Decimal:', key='4.5'),
              tf('2.4 is 24 hundredths.', key=False),
          ]),
      ],
      f1=B('Divide multi-digit decimals', '6.NS.B.3', [
          sa('Divide.\n3.75 ÷ 0.25', 'Quotient:', key='15'),
          sa('Divide.\n0.096 ÷ 0.12', 'Quotient:', key='0.8'),
          mc('Divide.\n8.1 ÷ 0.09', ['90', '9', '0.9', '900']),
          sa('Divide.\n14.4 ÷ 1.2', 'Quotient:', key='12'),
          tf('0.5 ÷ 0.02 = 2.5', key=False),
      ]),
      f2=B('Divide rational numbers', '7.NS.A.2.b', [
          sa('Find the quotient.\n-1.8 ÷ 0.3', 'Quotient:', key='-6'),
          sa('Find the quotient.\n(-0.6) ÷ (-0.15)', 'Quotient:', key='4'),
          mc('Find the quotient.\n2.4 ÷ (-4)', ['-0.6', '0.6', '-6', '-0.06']),
          tf('(-4.5) ÷ (-0.9) = -5', key=False),
          sa('Find the quotient.\n-0.08 ÷ 0.2', 'Quotient:', key='-0.4'),
      ]), num=64),

    # ------------------------------------------------------------------ 5.NBT.B.7 (real-world)
    S('5.NBT.B.7', 'Solve real-world problems with decimal operations',
      main=[
          sa('The grid shows 0.36 shaded.\nHow much more must be shaded to show 0.5?', 'Amount:', key='0.14', fig=hgrid(36)),
          sa('Juice costs $2.35 a bottle. Ben buys 4 bottles and pays with a $20 bill.\nHow much change does he get?', 'Change:',
             key='$10.60'),
          mc('A 2.5-pound bag of nuts is shared equally among 5 friends.\nHow many pounds does each friend get?',
             ['0.5 pound', '2 pounds', '12.5 pounds', '0.05 pound']),
          sa('A runner ran 3.75 km on Monday and 4.6 km on Tuesday.\nHow much farther did she run on Tuesday?', 'Distance:', key='0.85 km'),
          sa('Tiles cost $0.45 each.\nHow much do 12 tiles cost?', 'Cost:', key='$5.40'),
      ],
      back=[
          B('Word problems with money and measurement', '4.MD.A.2', [
              sa('Pens cost 75 cents each.\nHow much do 4 pens cost, in dollars?', 'Cost:', key='$3.00'),
              sa('A board is 120 cm long. It is cut into 4 equal pieces.\nHow long is each piece?', 'Length:', key='30 cm'),
              tf('Two quarters and three dimes are worth 65 cents.', key=False),
              mc('Ann has $5. She spends $2.25.\nHow much money is left?', ['$2.75', '$3.25', '$7.25', '$2.25']),
              sa('A jug holds 2 liters.\nHow many milliliters is that?', 'Milliliters:', key='2,000 mL'),
          ]),
          B('Hundredths on a grid', '4.NF.C.6', [
              sa('What decimal does the shaded part of the grid show?', 'Decimal:', key='0.45', fig=hgrid(45)),
              tf('The shaded part of the grid shows 0.8.', key=True, fig=hgrid(80)),
              mc('Which decimal does the shaded part of the grid show?', ['0.09', '0.9', '9', '0.009'], fig=hgrid(9)),
              sa('How many more squares must be shaded to fill the whole grid?', 'Squares:', key='36', fig=hgrid(64)),
              tf('0.5 of a hundredths grid is 5 squares.', key=False),
          ]),
      ],
      f1=B('Real-world problems with multi-digit decimals', '6.NS.B.3', [
          sa('Gas costs $3.85 per gallon.\nHow much do 12 gallons cost?', 'Cost:', key='$46.20'),
          sa('A board is 6.75 m long. It is cut into pieces that are 0.45 m long.\nHow many pieces are there?', 'Pieces:', key='15'),
          mc('Rice costs $1.20 per pound.\nHow much do 2.5 pounds cost?', ['$3.00', '$2.70', '$3.70', '$30.00']),
          sa('Lee buys items that cost $12.49, $3.05, and $7.60.\nWhat is the total cost?', 'Total:', key='$23.14'),
          tf('A 2.4-pound bag split into 0.3-pound portions makes 8 portions.', key=True),
      ]),
      f2=B('Real-world problems with rational numbers', '7.NS.A.3', [
          sa('A submarine at -45.5 m rises 12.75 m and then dives 20 m.\nWhat is its final position?', 'Position:', key='-52.75 m'),
          sa('A store\'s profit was -$125.40 in May and $310.15 in June.\nWhat was the total profit for the two months?', 'Total:',
             key='$184.75'),
          mc('The temperature was 4°F. It dropped 1.5°F each hour for 6 hours.\nWhat was the final temperature?',
             ['-5°F', '5°F', '-9°F', '13°F']),
          sa('An account changes by -$2.40 each week for 5 weeks.\nWhat is the total change?', 'Total change:', key='-$12.00'),
          tf('-3.6 ÷ 0.4 = -0.9', key=False),
      ])),
]
