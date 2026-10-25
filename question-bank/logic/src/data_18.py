"""Logic sets 52-54: patterns from a stated rule family; rearranging letters; weighings."""
import itertools
from functools import lru_cache
from lq import S, B, FW, mc, tf, sa, values, lesson

FAMILY = ('Rule family: the complete sequence is made by one of these rule types, though the terms shown may fit more '
          'than one. (1) Add the same number each time. (2) Multiply by the same number each time. (3) Add amounts that '
          'grow by the same nonzero number each time (for example +1, +2, +3, ...).')
LETTERS = 'Letters are numbered by their place in the alphabet: A = 1, B = 2, ..., Z = 26.'


def fits(seq):
    """Which family rules fit a numeric sequence: returns a list of (rule number, next term)."""
    out = []
    d = [b - a for a, b in zip(seq, seq[1:])]
    if len(set(d)) == 1:
        out.append((1, seq[-1] + d[0]))
    if 0 not in seq and len({b / a for a, b in zip(seq, seq[1:])}) == 1:
        out.append((2, seq[-1] * seq[1] // seq[0] if seq[1] % seq[0] == 0 else seq[-1] * seq[1] / seq[0]))
    dd = [b - a for a, b in zip(d, d[1:])]
    if len(d) >= 2 and len(set(dd)) == 1 and dd[0] != 0:
        out.append((3, seq[-1] + d[-1] + dd[0]))
    return out


def next_term(seq):
    f = fits(seq)
    assert len({n for _, n in f}) == 1, 'ambiguous: %s %s' % (seq, f)
    return f[0][1]


def pos(s):
    return [ord(c) - 64 for c in s]


def letter(n):
    return chr(64 + n)


# ------------------------------------------------------------------ Set 52: patterns from a stated rule family
def s52():
    return S(52, 'Identify the rule in a stated family that fits a sequence, and continue it',
             main=[
                 sa(FAMILY + ' What is the next term of 3, 7, 11, 15, ...?', 'Next term:', str(next_term([3, 7, 11, 15])),
                    'Rule (1): add 4 each time. 15 + 4 = 19.', compute=lambda: str(next_term([3, 7, 11, 15]))),
                 mc(FAMILY + ' Which rule fits 2, 6, 18, 54, ...?', 'Multiply by 3 each time',
                    [('Add 4 each time', '2 + 4 = 6, but 6 + 4 = 10, not 18'),
                     ('Add 4, then 12, then 36', 'those amounts do not grow by the same number each time'),
                     ('Multiply by 2 each time', '2 x 2 = 4, not 6')],
                    'Each term is 3 times the one before.', check=lambda t: t.startswith('Multiply by 3')),
                 sa(FAMILY + ' What is the next term of 1, 2, 4, 7, 11, ...?', 'Next term:',
                    str(next_term([1, 2, 4, 7, 11])),
                    'Rule (3): the amounts added are 1, 2, 3, 4, so next add 5: 16.',
                    compute=lambda: str(next_term([1, 2, 4, 7, 11]))),
                 tf(FAMILY + ' The sequence 5, 10, 20, 35, ... follows rule (3).', True,
                    'The amounts added are 5, 10, 15, which grow by 5 each time.',
                    check=lambda: [r for r, _ in fits([5, 10, 20, 35])] == [3]),
                 values(FAMILY + ' ' + LETTERS + ' The letters C, F, I, L follow rule (1) by their numbers. Give the next '
                                                'letter.', [('x', 'Next letter =')], "x == 'o'", {'x': 'O'},
                        'C, F, I, L are 3, 6, 9, 12: add 3. Next is 15, which is O.',
                        wrong=[{'x': 'M'}, {'x': 'N'}, {'x': 'P'}],
                        method='Checked: next number %d is letter %s.' % (next_term(pos('CFIL')), letter(next_term(pos('CFIL'))))),
             ],
             back=[B('Strategy: write the differences', 'guided_strategy',
                     'Students guess the next term from the look of the numbers. Writing the differences (and, if needed, '
                     'the ratios) tests each rule in the family exactly.',
                     lesson=lesson('Write the differences',
                                   ['Under the sequence, write the difference between each pair of neighbors.',
                                    'Equal differences: rule (1). Differences that grow by the same amount: rule (3).',
                                    'If neither, divide each term by the one before; equal results: rule (2).'],
                                   'Worked example (a different sequence)',
                                   ['Sequence: 4, 5, 8, 13, ...'],
                                   ['Differences: 1, 3, 5. They grow by 2 each time: rule (3).',
                                    'Next difference 7, so the next term is 13 + 7 = 20.']),
                     qs=[
                         sa('Write the differences of 2, 5, 9, 14. What is the last difference?', 'Difference:', '5',
                            'The differences are 3, 4, 5.', compute=lambda: str(14 - 9)),
                         tf(FAMILY + ' The sequence 10, 7, 4, 1, ... follows rule (1).', True, 'It adds -3 each time.',
                            check=lambda: [r for r, _ in fits([10, 7, 4, 1])] == [1]),
                         mc(FAMILY + ' Which rule fits 1, 4, 16, 64, ...?', 'Rule (2)',
                            [('Rule (1)', 'the differences 3, 12, 48 are not equal'),
                             ('Rule (3)', 'the differences 3, 12, 48 do not grow by the same amount'),
                             ('None of the rules', 'multiplying by 4 each time works')],
                            'Each term is 4 times the one before.',
                            check=lambda t: t == 'Rule (%d)' % fits([1, 4, 16, 64])[0][0] if t.startswith('Rule') else False),
                         sa(FAMILY + ' What is the next term of 50, 45, 40, 35, ...?', 'Next term:',
                            str(next_term([50, 45, 40, 35])), 'Add -5: 30.',
                            compute=lambda: str(next_term([50, 45, 40, 35]))),
                         tf(FAMILY + ' The sequence 3, 6, 12, 24, ... follows rule (1).', False,
                            'The differences are 3, 6, 12, which are not equal. It follows rule (2): multiply by 2.',
                            check=lambda: 1 in [r for r, _ in fits([3, 6, 12, 24])]),
                     ])],
             f1=FW('Rules for letters and far terms', 'Harder: letter sequences and later terms.', [
                 values(FAMILY + ' ' + LETTERS + ' The letters B, D, G, K follow rule (3) by their numbers. Give the next '
                                                'letter.', [('x', 'Next letter =')], "x == 'p'", {'x': 'P'},
                        'B, D, G, K are 2, 4, 7, 11; the amounts added are 2, 3, 4, so add 5: 16, which is P.',
                        wrong=[{'x': 'O'}, {'x': 'N'}, {'x': 'Q'}],
                        method='Checked: next number %d is letter %s.' % (next_term(pos('BDGK')), letter(next_term(pos('BDGK'))))),
                 sa(FAMILY + ' What is the 10th term of 4, 7, 10, 13, ...?', '10th term:', str(4 + 9 * 3),
                    'Rule (1), add 3. The 10th term is 4 + 9 x 3 = 31.', compute=lambda: str(4 + 9 * 3)),
                 tf(FAMILY + ' Knowing only the first two terms, 3 and 6, is enough to know the third term.', False,
                    'Rule (1) gives 9 (add 3) and rule (2) gives 12 (multiply by 2), so more terms are needed.',
                    check=lambda: len({n for _, n in fits([3, 6])}) == 1),
                 mc(FAMILY + ' The first three terms are 1, 2, 4. Which statement is true?',
                    'Rule (2) and rule (3) both fit, giving 8 or 7 next.',
                    [('Only rule (2) fits, so the next term is 8.', 'rule (3) also fits: add 1, then 2, then 3'),
                     ('Only rule (3) fits, so the next term is 7.', 'rule (2) also fits: multiply by 2'),
                     ('Rule (1) fits, so the next term is 6.', 'the differences 1 and 2 are not equal')],
                    'Three terms cannot tell rule (2) from rule (3) here.',
                    check=lambda t: t.startswith('Rule (2) and') and sorted(n for _, n in fits([1, 2, 4])) == [7, 8]),
                 sa(FAMILY + ' What is the 8th term of 2, 6, 18, 54, ...?', '8th term:', str(2 * 3 ** 7),
                    'Rule (2), multiply by 3. The 8th term is 2 x 3 to the 7th power = 4374.', compute=lambda: str(2 * 3 ** 7)),
             ]),
             f2=FW('Work with the rule as a formula', 'Expert: general terms and first terms past a limit.', [
                 values(FAMILY + ' The sequence is 5, 9, 13, 17, .... Give the 25th term.', [('t', '25th term =')],
                        't == 101', {'t': 101}, 'Rule (1), add 4: the nth term is 5 + 4(n - 1). For n = 25: 5 + 96 = 101.',
                        wrong=[{'t': 105}, {'t': 97}, {'t': 100}]),
                 sa(FAMILY + ' In the sequence 3, 6, 12, 24, ..., which term is the first one greater than 1000? Give its '
                             'position (1 for the first term).', 'Position:',
                    str(next(n for n in range(1, 40) if 3 * 2 ** (n - 1) > 1000)),
                    'Terms: 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536. The 10th term, 1536, is the first above 1000.',
                    compute=lambda: str(next(n for n in range(1, 40) if 3 * 2 ** (n - 1) > 1000))),
                 sa(FAMILY + ' What is the 10th term of 1, 3, 6, 10, ...?', '10th term:', str(10 * 11 // 2),
                    'Rule (3): add 2, 3, 4, ... The nth term is 1 + 2 + ... + n, so the 10th is 55.',
                    compute=lambda: str(sum(range(1, 11)))),
                 tf(FAMILY + ' A sequence that follows rule (1) with a positive amount added will eventually pass every '
                             'number.', True, 'Adding the same positive amount again and again grows without limit.'),
                 mc(FAMILY + ' ' + LETTERS + ' Which letter sequence follows rule (2) by the letters\' numbers?',
                    'A, B, D, H', [('A, C, E, G', 'that adds 2 each time: rule (1)'),
                                   ('A, B, D, G', 'that adds 1, 2, 3: rule (3)'),
                                   ('B, C, E, H', 'that adds 1, 2, 3: rule (3)')],
                    'A, B, D, H are 1, 2, 4, 8: multiply by 2.',
                    check=lambda t: [r for r, _ in fits(pos(t.replace(', ', '')))] == [2]),
             ]))


# ------------------------------------------------------------------ Set 53: rearranging letters
WORDS = ['MELON', 'LEMON', 'SOLEMN', 'TEARS', 'RATES', 'STARE', 'TASTE', 'STATE', 'LISTEN', 'SILENT', 'ENLIST', 'TINSEL',
         'PLANE', 'PANEL', 'PLANET', 'LEAN', 'LANE', 'NEAT', 'ANT', 'TAN', 'PEN', 'NET', 'TEN', 'PALE', 'LEAP', 'PLATE',
         'PETAL', 'SPOT', 'STOP', 'POTS', 'TOPS', 'POST', 'RATS', 'STAR', 'ARTS', 'NIGHT', 'THING', 'DUSTY', 'STUDY',
         'NOTE', 'TONE', 'STONE', 'ONSET', 'NOTES', 'BREAD', 'BEARD', 'BARED', 'HEART', 'EARTH', 'HATER']
BANK = 'Word list (the ONLY words allowed): ' + ', '.join(WORDS) + '.'
ANAG = 'An anagram uses exactly the same letters, each as many times, in a different order.'


def key(w):
    return ''.join(sorted(w.replace(' ', '').upper()))


def anagrams(w, words=WORDS):
    return [x for x in words if key(x) == key(w) and x != w.upper()]


def from_letters(src, words=WORDS):
    """Words that can be spelled from the letters of src, each letter used at most as often as it appears."""
    from collections import Counter
    have = Counter(src.upper())
    return [w for w in words if not Counter(w) - have]


def s53():
    return S(53, 'Find anagrams and letter-bank words within a supplied word list and letter rules',
             main=[
                 mc(BANK + ' ' + ANAG + ' Which word on the list is an anagram of LEMON?', 'MELON',
                    [('SOLEMN', 'SOLEMN has an extra S'), ('LANE', 'LANE has different letters'),
                     ('TONE', 'TONE has different letters')], 'MELON uses M, E, L, O, N once each, like LEMON.',
                    check=lambda t: t in anagrams('LEMON')),
                 values(BANK + ' ' + ANAG + ' Give a word on the list that is an anagram of STARE.', [('w', 'Word =')],
                        "w == 'tears' or w == 'rates'", {'w': 'TEARS'}, 'TEARS and RATES use A, E, R, S, T.',
                        wrong=[{'w': 'STARE'}, {'w': 'STAR'}, {'w': 'TASTE'}, {'w': 'ASTER'}],
                        method='Checked: anagrams of STARE on the list are %s.' % anagrams('STARE')),
                 tf(BANK + ' ' + ANAG + ' LISTEN, SILENT, ENLIST and TINSEL are all anagrams of one another.', True,
                    'Each uses E, I, L, N, S, T once.', check=lambda: len({key(w) for w in ('LISTEN', 'SILENT', 'ENLIST',
                                                                                          'TINSEL')}) == 1),
                 sa(BANK + ' How many words on the list can be spelled using the letters of PLANET, each letter at most '
                           'once?', 'Words:', str(len(from_letters('PLANET'))),
                    'Check each word against P, L, A, N, E, T: PLANE, PANEL, PLANET, LEAN, LANE, NEAT, ANT, TAN, PEN, NET, '
                    'TEN, PALE, LEAP, PLATE, PETAL: 15.', compute=lambda: str(len(from_letters('PLANET')))),
                 mc(BANK + ' Read the letters STOPAN from right to left. Which word on the list appears as a block of '
                           'neighboring letters in that backward reading?', 'POTS',
                    [('STOP', 'STOP appears forward, not in the backward reading NAPOTS'),
                     ('SPOT', 'the letters S, P, O, T are not neighbors in that order in NAPOTS'),
                     ('PAN', 'PAN is not on the list')],
                    'Backward, STOPAN reads NAPOTS, which contains POTS.',
                    check=lambda t: t in WORDS and t in 'STOPAN'[::-1]),
             ],
             back=[B('Strategy: sort the letters', 'guided_strategy',
                     'Students compare words by eye and miss a letter. Writing each word\'s letters in alphabetical order '
                     'turns "is it an anagram?" into "are these strings equal?".',
                     lesson=lesson('Sort the letters',
                                   ['Write the letters of each word in alphabetical order, keeping repeats.',
                                    'Two words are anagrams exactly when their sorted letters match.',
                                    'To check whether a word can be spelled from a set of letters, cross off each letter as '
                                    'you use it.'],
                                   'Worked example (different words)',
                                   ['Are DIRTY and DIRT anagrams? Are CAFE and FACE?'],
                                   ['DIRTY sorts to D, I, R, T, Y and DIRT sorts to D, I, R, T. DIRTY has an extra Y, so '
                                    'they are not anagrams.',
                                    'CAFE and FACE both sort to A, C, E, F: anagrams.']),
                     qs=[
                         sa('Write the letters of NOTE in alphabetical order (no spaces).', 'Letters:', key('NOTE'),
                            'E, N, O, T.', compute=lambda: key('NOTE')),
                         tf(ANAG + ' STONE and NOTES are anagrams.', True, 'Both sort to E, N, O, S, T.',
                            check=lambda: key('STONE') == key('NOTES')),
                         tf(ANAG + ' TASTE and STATE are anagrams.', True, 'Both sort to A, E, S, T, T.',
                            check=lambda: key('TASTE') == key('STATE')),
                         mc(ANAG + ' Which word is NOT an anagram of SPOT?', 'SPOTS',
                            [('STOP', 'STOP uses S, P, O, T'), ('TOPS', 'TOPS uses S, P, O, T'),
                             ('POTS', 'POTS uses S, P, O, T')], 'SPOTS has an extra S.',
                            check=lambda t: key(t) != key('SPOT')),
                         tf(ANAG + ' BREAD and BEARD are anagrams.', True, 'Both sort to A, B, D, E, R.',
                            check=lambda: key('BREAD') == key('BEARD')),
                     ])],
             f1=FW('Letter banks and joined parts', 'Harder: build words from parts and from letter banks.', [
                 values(BANK + ' Join one part from the first group to one part from the second group to make a word on the '
                               'list. First group: PL, ST, HE. Second group: ART, ANET, ONE. Give the word.',
                        [('w', 'Word =')], "w == 'planet' or w == 'heart' or w == 'stone'", {'w': 'PLANET'},
                        'PL + ANET = PLANET, HE + ART = HEART and ST + ONE = STONE are all on the list.',
                        wrong=[{'w': 'START'}, {'w': 'PLONE'}, {'w': 'STANET'}],
                        method='Checked all 9 joins: listed words %s.'
                        % [a + b for a in ('PL', 'ST', 'HE') for b in ('ART', 'ANET', 'ONE') if a + b in WORDS]),
                 sa(BANK + ' ' + ANAG + ' How many words on the list are anagrams of EARTH (not counting EARTH itself)?',
                    'Words:', str(len(anagrams('EARTH'))), 'HEART and HATER.', compute=lambda: str(len(anagrams('EARTH')))),
                 mc(BANK + ' You may use the letters S, T, O, P as often as you like. Which is the longest word on the list '
                           'you can spell?', 'All of SPOT, STOP, POTS, TOPS and POST tie at 4 letters',
                    [('STOP is the only longest word', 'SPOT, POTS, TOPS and POST also have 4 letters'),
                     ('STONE', 'STONE needs N and E'),
                     ('SPOTS', 'SPOTS is not on the list')],
                    'Only 4-letter words from S, T, O, P are on the list, and there are five of them.',
                    check=lambda t: t.startswith('All of') and sorted(w for w in WORDS if set(w) <= set('STOP')
                                                                     and len(w) == 4) == sorted(['SPOT', 'STOP', 'POTS',
                                                                                                 'TOPS', 'POST'])),
                 tf(BANK + ' ' + ANAG + ' NIGHT and THING are anagrams.', True, 'Both sort to G, H, I, N, T.',
                    check=lambda: key('NIGHT') == key('THING')),
                 sa(BANK + ' ' + ANAG + ' Group the list words into anagram families (words with the same sorted '
                                       'letters). How many families have exactly 4 or more words?', 'Families:',
                    str(sum(1 for k in {key(w) for w in WORDS} if sum(key(w) == k for w in WORDS) >= 4)),
                    'LISTEN, SILENT, ENLIST, TINSEL; SPOT, STOP, POTS, TOPS, POST; STONE, ONSET, NOTES (only 3). So 2 '
                    'families.', compute=lambda: str(sum(1 for k in {key(w) for w in WORDS}
                                                          if sum(key(w) == k for w in WORDS) >= 4))),
             ]),
             f2=FW('Phrases and hidden words', 'Expert: anagrams of phrases and backward readings.', [
                 mc(BANK + ' ' + ANAG + ' Spaces do not count. Which pair of list words, written together, is an anagram '
                                       'of the phrase PAST TEEN?', 'TASTE PEN',
                    [('PETAL NET', 'it has an L and no S'), ('STAR PEN', 'it has an R and only one T'),
                     ('NEAT POTS', 'it has an O and only one E')],
                    'PAST TEEN has A, E, E, N, P, S, T, T. TASTE (A, E, S, T, T) and PEN (E, N, P) use exactly these.',
                    check=lambda t: key(t) == key('PAST TEEN')),
                 tf(BANK + ' Every word on the list that is also a list word when read backward has 3 or 4 letters.', True,
                    'The pairs are NET and TEN, SPOT and TOPS, STOP and POTS, RATS and STAR.',
                    check=lambda: all(len(w) in (3, 4) for w in WORDS if w[::-1] in WORDS)),
                 values(BANK + ' Give a word on the list that is also a word on the list when read backward.',
                        [('w', 'Word =')], ' or '.join("w == '%s'" % w.lower() for w in WORDS if w[::-1] in WORDS),
                        {'w': 'STOP'}, 'NET, TEN, SPOT, TOPS, STOP, POTS, RATS and STAR all work.',
                        wrong=[{'w': 'POST'}, {'w': 'STONE'}, {'w': 'LEMON'}],
                        method='Checked every list word read backward: %s.' % [w for w in WORDS if w[::-1] in WORDS]),
                 sa(BANK + ' How many words on the list can be spelled using the letters of STONE, each letter at most once?',
                    'Words:', str(len(from_letters('STONE'))),
                    'NOTE, TONE, STONE, ONSET, NOTES, NET, TEN: 7.', compute=lambda: str(len(from_letters('STONE')))),
                 sa(BANK + ' ' + ANAG + ' How many words on the list use exactly the letters of NOTES, counting NOTES '
                                       'itself?', 'Words:', str(len(anagrams('NOTES')) + 1),
                    'STONE, ONSET and NOTES: 3.', compute=lambda: str(len(anagrams('NOTES')) + 1)),
             ]))


# ------------------------------------------------------------------ Set 54: weighings
SCALE = ('A balance scale compares two groups of coins: one side goes down, or the two sides balance. All coins look the '
         'same. All genuine coins weigh the same; the one odd coin is heavier unless the question says otherwise.')


@lru_cache(None)
def need(n):
    """Fewest weighings that always find the one heavier coin among n (worst case), by searching every first weighing."""
    if n <= 1:
        return 0
    best = None
    for k in range(1, n // 2 + 1):
        rest = n - 2 * k
        worst = 1 + max(need(k), need(rest) if rest else 0)
        best = worst if best is None else min(best, worst)
    return best


def worst_after(n, k):
    rest = n - 2 * k
    return 1 + max(need(k), need(rest) if rest else 0)


def s54():
    return S(54, 'Plan weighings or questions and find the least number that always identifies the answer',
             main=[
                 sa(SCALE + ' There are 9 coins and one is heavier. What is the least number of weighings that always finds '
                            'the heavy coin?', 'Weighings:', str(need(9)),
                    'Weigh 3 against 3. If one side goes down, the heavy coin is among those 3; if they balance, it is among '
                    'the other 3. Then weigh 1 against 1 of the 3. One weighing cannot work: it has only 3 outcomes for 9 '
                    'possibilities.', compute=lambda: str(need(9))),
                 mc(SCALE + ' There are 9 coins and one is heavier. Which first weighing lets you always finish in the fewest '
                            'total weighings?', '3 coins against 3 coins',
                    [('4 coins against 4 coins', 'if one side goes down, 4 suspects remain, which needs 2 more weighings'),
                     ('1 coin against 1 coin', 'if they balance, 7 suspects remain, which needs 2 more weighings'),
                     ('2 coins against 2 coins', 'if they balance, 5 suspects remain, which needs 2 more weighings')],
                    'Splitting 9 into three groups of 3 leaves 3 suspects whatever happens, and 3 needs only one more '
                    'weighing.', check=lambda t: worst_after(9, int(t.split()[0])) == need(9)),
                 tf(SCALE + ' With 3 weighings you can always find the heavier coin among 27 coins.', True,
                    'Each weighing splits the suspects into three groups (left, right, off the scale): 27, then 9, then 3, '
                    'then 1.', check=lambda: need(27) <= 3),
                 values(SCALE + ' What is the largest number of coins n for which 2 weighings always find the one heavier '
                                'coin?', [('n', 'n =')], 'n == 9', {'n': 9},
                        'Two weighings have 3 x 3 = 9 outcome patterns, so at most 9 coins; and 9 works by splitting into '
                        'threes.', wrong=[{'n': 8}, {'n': 10}, {'n': 6}],
                        method='Search: largest n with need(n) <= 2 is %d.' % max(n for n in range(1, 40) if need(n) <= 2)),
                 sa(SCALE + ' There are 10 coins and one is heavier. What is the least number of weighings that always finds '
                            'the heavy coin?', 'Weighings:', str(need(10)),
                    'Two weighings give only 9 outcome patterns, which is fewer than 10 possibilities, so 2 are not enough. '
                    'Three are: weigh 3 against 3, leaving at most 4 suspects, then finish in 2 more.',
                    compute=lambda: str(need(10))),
             ],
             back=[B('Strategy: each weighing has three outcomes', 'guided_strategy',
                     'Students weigh half against half. Remembering that a weighing has three outcomes (left down, right '
                     'down, balance) leads to splitting the suspects into three groups.',
                     lesson=lesson('Each weighing has three outcomes',
                                   ['A weighing can tip left, tip right or balance: three outcomes.',
                                    'Split the suspects into three groups as equal as possible: two on the scale (same size) '
                                    'and one off it.',
                                    'After w weighings there are at most 3 x 3 x ... (w times) outcome patterns, so at most '
                                    'that many coins can be told apart.'],
                                   'Worked example (a different count)',
                                   ['There are 3 coins and one is heavier. How many weighings?'],
                                   ['Weigh coin 1 against coin 2. If one goes down, it is heavy. If they balance, coin 3 is '
                                    'heavy.',
                                    'One weighing is enough.']),
                     qs=[
                         sa('How many different outcomes can one weighing on a balance scale have?', 'Outcomes:', '3',
                            'Left side down, right side down, or balance.', compute=lambda: '3'),
                         tf(SCALE + ' With 3 coins and one heavier, one weighing always finds the heavy coin.', True,
                            'Weigh 1 against 1; a balance means the third coin is heavy.', check=lambda: need(3) == 1),
                         mc(SCALE + ' There are 5 coins and one is heavier. You weigh 2 against 2 and they balance. What do '
                                    'you know?', 'The fifth coin is the heavy one.',
                            [('One of the four weighed coins is heavy.', 'a heavy coin on the scale would tip it'),
                             ('Nothing yet.', 'a balance clears all four weighed coins'),
                             ('You must weigh again to know.', 'only one coin is left as a suspect')],
                            'All four weighed coins are genuine, so the coin left off is heavy.'),
                         sa('How many outcome patterns do 2 weighings have in all?', 'Patterns:', '9',
                            'Each of the 3 outcomes of the first weighing can be followed by 3 outcomes of the second: 9.',
                            compute=lambda: str(3 * 3)),
                         tf(SCALE + ' With 4 coins and one heavier, one weighing always finds the heavy coin.', False,
                            'One weighing has 3 outcomes, but there are 4 possibilities.', check=lambda: need(4) <= 1),
                     ])],
             f1=FW('Bigger groups and comparisons', 'Harder: more coins, and finding the heaviest of different weights.', [
                 sa(SCALE + ' You may use 4 weighings. What is the largest number of coins among which you can always find '
                            'the one heavier coin?', 'Coins:', str(max(n for n in range(1, 200) if need(n) <= 4)),
                    '4 weighings have 3 x 3 x 3 x 3 = 81 outcome patterns, and splitting into thirds each time handles 81 '
                    'coins.', compute=lambda: str(max(n for n in range(1, 200) if need(n) <= 4))),
                 mc(SCALE + ' There are 6 coins and one is heavier. You weigh 2 against 2 and the left side goes down. Which next '
                            'weighing is sure to identify the heavy coin?', 'One left-side coin against the other left-side coin',
                    [('One right-side coin against one coin that was left off the scale', 'both of those coins are genuine, so '
                                                                                   'they balance and nothing is learned'),
                     ('The two coins left off against each other', 'those coins are genuine; the heavy coin was on the left'),
                     ('All six coins again, 3 against 3', 'that repeats work and may not finish')],
                    'Only the 2 left-side coins are suspects. Weigh them against each other: the one that goes down is '
                    'heavy.'),
                 tf('You have 3 weights of different sizes and compare them two at a time on a balance. Finding the heaviest '
                    'always takes at least 2 weighings.', True,
                    'Each weight that is not the heaviest must lose at least one comparison, and one weighing has only one '
                    'loser. Two weights must lose, so 2 weighings are needed.'),
                 sa('You have 8 weights of different sizes and compare them two at a time on a balance. What is the least '
                    'number of weighings that always finds the heaviest?', 'Weighings:', '7',
                    'Every weight except the heaviest must lose a comparison, and each weighing has one loser: at least 7. '
                    'A knockout tournament uses exactly 7.', compute=lambda: str(8 - 1)),
                 values(SCALE + ' Give a number of coins n from 20 to 30 for which 3 weighings always find the one heavier '
                                'coin.', [('n', 'n =')], 'isInteger(n) and n >= 20 and n <= 27', {'n': 27},
                        'Three weighings handle up to 3 x 3 x 3 = 27 coins, so any n from 20 to 27 works; 28, 29 and 30 do '
                        'not.', wrong=[{'n': 28}, {'n': 30}, {'n': 19}],
                        method='Search: need(n) <= 3 exactly for n up to %d.' % max(n for n in range(1, 60) if need(n) <= 3)),
             ]),
             f2=FW('Least weighings, proved', 'Expert: lower bounds from counting outcomes.', [
                 sa(SCALE + ' There are 7 coins and one is LIGHTER (not heavier). What is the least number of weighings that '
                            'always finds it?', 'Weighings:', str(need(7)),
                    'The same splitting works for a lighter coin: weigh 3 against 3 (or 2 against 2), leaving at most 3 '
                    'suspects; then one more weighing. One weighing cannot tell 7 cases apart.',
                    compute=lambda: str(need(7))),
                 mc(SCALE + ' Why can 2 weighings NOT always find the heavy coin among 10?',
                    'Two weighings give only 9 outcome patterns, but there are 10 possible heavy coins.',
                    [('10 is an even number.', 'evenness is not the issue; 8 coins need only 2 weighings'),
                     ('You cannot put 5 coins on each side.', 'you can, and it still would not be enough'),
                     ('The first weighing must use all 10 coins.', 'it need not use every coin')],
                    'Each possibility needs its own outcome pattern, and 10 > 9.'),
                 tf(SCALE + ' With 4 coins and one heavier, 2 weighings always find the heavy coin.', True,
                    'Weigh 1 against 1. If one goes down, done; if they balance, weigh the other two.',
                    check=lambda: need(4) <= 2),
                 values(SCALE + ' Give a number of coins n from 20 to 90 for which 3 weighings are NOT enough but 4 weighings '
                                'are enough to always find the one heavier coin.', [('n', 'n =')],
                        'isInteger(n) and n >= 28 and n <= 81', {'n': 50},
                        '3 weighings handle at most 27 coins, and 4 handle at most 81. So n from 28 to 81 works.',
                        wrong=[{'n': 27}, {'n': 82}, {'n': 20}],
                        method='Search: need(n) == 4 exactly for n from %d to %d.'
                        % (min(n for n in range(1, 200) if need(n) == 4), max(n for n in range(1, 200) if need(n) == 4))),
                 sa('You have 4 weights of different sizes and compare them two at a time on a balance. What is the least '
                    'number of weighings that always finds both the heaviest and the lightest?', 'Weighings:',
                    str(min_max_weighings(4)),
                    'Compare A with B and C with D. The heaviest is the winner of a second comparison between the two '
                    'winners, and the lightest is the loser of a comparison between the two losers: 4 weighings. A search '
                    'of every strategy shows 3 are never enough.', compute=lambda: str(min_max_weighings(4))),
             ]))


def min_max_weighings(n):
    """Least number of comparisons that always identifies both the heaviest and the lightest of n different weights,
    found by searching every comparison strategy over the orderings still possible."""
    perms = list(itertools.permutations(range(n)))  # perms[i] = rank of item i
    pairs = list(itertools.combinations(range(n), 2))

    @lru_cache(None)
    def solved(state):
        return len({(p.index(n - 1), p.index(0)) for p in (perms[i] for i in state)}) == 1

    @lru_cache(None)
    def can(state, depth):
        if solved(state):
            return True
        if depth == 0:
            return False
        for a, b in pairs:
            left = frozenset(i for i in state if perms[i][a] > perms[i][b])
            right = state - left
            if left and right and can(left, depth - 1) and can(right, depth - 1):
                return True
        return False
    full = frozenset(range(len(perms)))
    return next(d for d in range(0, 10) if can(full, d))


SETS = [s52(), s53(), s54()]
