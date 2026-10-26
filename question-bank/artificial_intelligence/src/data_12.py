"""Path: code assistance (AI.CODE.01-10). Every runnable Python example is executed by CODE() and its printed output
is checked; error messages are shown as prepared text in Python 3's simplified format."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.CODE.01
READ = ('A PROGRAM is a list of instructions a computer follows in order, top to bottom. In the language PYTHON, '
        'a VARIABLE is a name that stores a value: "price = 4" stores 4 under the name price (the "=" means "store," '
        'not "is equal"). "*" multiplies, "+" adds and "/" divides. print(...) shows a value on screen. To read code, '
        'go line by line and track each variable\'s value, like keeping score on paper. In the example, price is 4 and '
        'count is 3, so total is 4 * 3 = 12, and the last line prints 12.')
READ_F2 = ('Two more patterns appear constantly. An IF statement runs lines only when a condition is true: "if age >= '
           '16:" means "if age is at least 16." Lines indented under it belong to it, and an ELSE part runs otherwise. '
           'A FOR LOOP repeats lines once for each item in a list: "for n in [1, 2, 3]:" runs its indented lines three '
           'times, with n being 1, then 2, then 3. Indentation (spaces at the start of a line) shows which lines belong '
           'together.')

READ_EX = CODE('''
price = 4
count = 3
total = price * count
print(total)
''', out='12')
IF_EX = CODE('''
age = 15
if age >= 16:
    print("Can apply")
else:
    print("Too young")
''', out='Too young')
LOOP_EX = CODE('''
for n in [1, 2, 3]:
    print(n * 2)
''', out='2\n4\n6')

S_CODE01 = SET(
    'AI.CODE.01',
    M=sec('Read a few lines of Python and predict what they do', READ, [
        Q('In this example, what does the program print?', '12',
          ('7, because the program adds the price and the count together before printing the total', 'it multiplies'),
          ('4', 'that is price'), ('total', 'it prints the value, not the name'),
          '4 * 3 = 12.', calc=lambda: 4 * 3 == 12, ex=READ_EX),
        Q('What does "price = 4" do in Python?', 'Stores 4 under the name price',
          ('Checks whether price is already equal to 4 and prints True or False on the screen', 'that is =='),
          ('Prints 4', 'no print'), ('Deletes price', 'no'),
          '"=" stores a value.'),
        Q('If the second line were "count = 5," what would print?', '20',
          ('9, because changing the count to 5 adds 5 to the price of 4 instead of multiplying', 'it multiplies'),
          ('12', 'count changed'), ('5', 'that is count'),
          '4 * 5 = 20.', calc=lambda: 4 * 5 == 20, ex=READ_EX),
        Q('In what order does Python run these lines?',
          'Top to bottom',
          ('Bottom to top', 'reversed'), ('In random order', 'no'),
          ('Only the last line', 'no'),
          'Instructions run in order.'),
        Q('What does print(...) do?', 'Shows a value on screen',
          ('Sends the program to a printer so a paper copy of the code is made for you', 'not in Python'),
          ('Stores a value', 'that is ='), ('Multiplies numbers', 'that is *'),
          'Displays output.'),
    ]),
    B=[sk('Trace variables on paper',
          'TRACING means following a program line by line and writing down each variable\'s value as it changes, '
          'like a scoreboard. Example: line 1 "a = 2" (a is 2). Line 2 "b = a + 3" (b is 5). Line 3 "a = 10" (a is '
          'now 10; b stays 5, because b was already calculated). Line 4 "print(a + b)" shows 15. The key habit: when '
          'a variable changes, cross out its old value and write the new one, and do not change other variables unless '
          'a line says so.', [
              Q('After line 2, what is b?', '5',
                ('2, because b is given the same value as a, and the "+ 3" part is ignored by Python', 'adds 3'),
                ('3', 'a + 3'), ('10', 'later'),
                '2 + 3 = 5.', calc=lambda: 2 + 3 == 5),
              Q('After line 3, what is a?', '10',
                ('2, because once a variable is given a value it can never be changed by a later line', 'it changes'),
                ('5', 'that is b'), ('12', 'no'),
                'a is replaced.'),
              Q('After line 3, what is b?', '5',
                ('13, because b automatically updates whenever the value of a is changed by a later line', 'it does not'),
                ('10', 'that is a'), ('2', 'no'),
                'b was already calculated.'),
              Q('What does line 4 print?', '15',
                ('7, which is the original value of a added to the original value of b from line 2', 'a changed'),
                ('12', 'no'), ('a + b', 'prints the value'),
                '10 + 5 = 15.', calc=lambda: 10 + 5 == 15),
              Q('What is the key tracing habit?', 'Update a variable only when a line changes it',
                ('Update every variable on every line, even when the line does not mention that variable', 'no'),
                ('Track only the last line', 'no'), ('Ignore numbers', 'no'),
                'Cross out and rewrite.'),
          ], why='A learner who cannot follow code practices the underlying skill of tracing variable values line by '
                 'line.')],
    F1=sec('Predict the output of short programs', READ, [
        Q('What does this program print?',
          'Too young',
          ('Can apply', 'condition false'), ('15', 'not printed'),
          ('Nothing', 'else runs'),
          '15 >= 16 is false, so else runs.',
          calc=lambda: not (15 >= 16),
          ex=IF_EX),
        Q('If the first line were "age = 16," what would print?',
          'Can apply',
          ('Too young', '>= includes 16'), ('16', 'not printed'),
          ('Both lines', 'only one branch runs'),
          '16 >= 16 is true.',
          calc=lambda: 16 >= 16,
          ex=IF_EX),
        Q('What does this loop print?',
          '2, 4 and 6 on separate lines',
          ('1, 2 and 3 on separate lines', 'it doubles'), ('6 only', 'prints each time'),
          ('12', 'no sum'),
          'Each n doubled.',
          ex=LOOP_EX),
        Q('How many times does the loop body run?', '3',
          ('6, because the loop runs once for every number that it prints out on the screen', 'once per item'),
          ('1', 'once per item'), ('2', 'once per item'),
          'Three items in the list.', ex=LOOP_EX),
        Q('In "x = 7" then "x = x + 1," what is x afterward?', '8',
          ('7, because a variable cannot be used on both sides of the same "=" sign in Python', 'it can'),
          ('1', 'no'), ('71', 'not text joining'),
          '7 + 1 = 8.', calc=lambda: 7 + 1 == 8),
    ]),
    F2=sec('Read if statements, loops and indentation', READ_F2, [
        Q('What does "if age >= 16:" mean?', 'If age is at least 16',
          ('If age is exactly 16 and no other number, so 17 and 18 would not count at all', '>= includes more'),
          ('If age is under 16', 'reversed'), ('Set age to 16', 'not assignment'),
          'Greater than or equal.'),
        Q('What does indentation show in Python?', 'Which lines belong together',
          ('How important each line is, with the most important lines indented the furthest', 'not importance'),
          ('Nothing; it is decoration', 'it matters'), ('Comments', 'no'),
          'Blocks of code.'),
        Q('In "for n in [5, 10]: print(n)," what prints?', '5 then 10',
          ('15, because a for loop adds up every item in the list and prints the total once', 'no sum'),
          ('n twice', 'prints values'), ('Nothing', 'it prints'),
          'Each item in turn.'),
        Q('When does an else part run?', 'When the if condition is false',
          ('Always, right after the if part has finished, whether the condition was true or false', 'only when false'),
          ('Never', 'it can'), ('Before the if', 'no'),
          'The other branch.'),
        Q('A loop goes over a list of 4 names. How many times does its body run?', '4',
          ('1, because a loop body runs only once no matter how many items are in the list', 'once per item'),
          ('0', 'it runs'), ('8', 'no'),
          'Once per item.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.02
WHY = ('AI-generated code often LOOKS right: neat layout, sensible names, helpful comments. It can still be WRONG, '
       'because the model predicts likely code rather than proving it correct. Common problems: logic that works for '
       'one example but not others, misunderstood requirements, missing cases such as an empty list, and calls to '
       'functions or settings that do not exist. To check code: read it and trace it, RUN it on several inputs whose '
       'correct answers you already know, and compare results. Passing one test does not prove the code is right.')
WHY_F2 = ('Confident explanations make wrong code more convincing. A tool may describe what code "does" based on what '
          'it was supposed to do, not what it actually does. Comments can be wrong too. Trust behavior over '
          'descriptions: run it, and test the boundaries (the smallest, largest, empty and unusual inputs). When '
          'the code will affect money, safety, privacy or other people, have someone experienced review it before '
          'it is used.')

AVG_EX = CODE('''
def average(numbers):
    return sum(numbers) / 2

print(average([4, 6]))
print(average([3, 6, 9]))
''', out='5.0\n9.0')

S_CODE02 = SET(
    'AI.CODE.02',
    M=sec('Explain why code that looks right can be wrong and how to check it', WHY, [
        Q('Why can generated code be wrong even when it looks neat?', 'The model predicts likely code without proving it',
          ('Because neat code is always wrong, and only messy code can actually work correctly', 'not true'),
          ('Because computers cannot run neat code', 'no'),
          ('Because comments stop code from running', 'no'),
          'Prediction, not proof.'),
        Q('In this example, which result is wrong?',
          '9.0 for [3, 6, 9]',
          ('5.0 for [4, 6]', '5.0 is right'), ('Both results', '5.0 is right'),
          ('Neither result', 'one is wrong'),
          'The average of 3, 6, 9 is 6.',
          calc=lambda: (3 + 6 + 9) / 3 == 6,
          ex=AVG_EX),
        Q('What is the bug in the same example?',
          'It always divides by 2',
          ('It uses sum', 'sum is fine'), ('It prints too much', 'not the bug'),
          ('Its name is wrong', 'not the bug'),
          'It should divide by len(numbers).',
          ex=AVG_EX),
        Q('What does the example show about testing?', 'Passing one test does not prove code right',
          ('Testing is a waste of time, because the first test already showed that the function works', 'reversed'),
          ('Two tests are always enough', 'not always'), ('Code never needs tests', 'no'),
          'Test several inputs.', ex=AVG_EX),
        Q('What is the best way to check code?', 'Run it on inputs whose answers you know',
          ('Ask the tool that wrote it whether it is correct, and accept the answer that it gives', 'not independent'),
          ('Check that it has comments', 'not enough'),
          ('Count its lines', 'not a check'),
          'Known answers reveal errors.'),
    ]),
    B=[cs('Compare checking code with checking a calculator you built',
          'Imagine you built a calculator and want to know if it works. You would not just admire the buttons. You '
          'would type problems you already know the answer to: 2 + 2, 10 - 3, 5 * 5. If one gives a wrong result, '
          'you know something is broken, even if the others were right. Generated code is like a new calculator: '
          'neat appearance proves nothing; known-answer tests do.', [
              Q('Why type 2 + 2 into a new calculator?', 'You already know the answer',
                ('Because 2 + 2 is the only problem that any calculator can ever solve correctly', 'no'),
                ('To make it faster', 'no'), ('To clean the buttons', 'no'),
                'Known answers reveal errors.'),
              Q('The calculator gets 2 + 2 right but 5 * 5 wrong. Does it work?', 'No; one wrong result shows a problem',
                ('Yes, because getting the first problem right proves that every other answer is right', 'no'),
                ('Yes, mostly', 'still broken'), ('It cannot be known', 'it can'),
                'One failure matters.'),
              Q('Nice-looking buttons prove what?', 'Nothing about correctness',
                ('That every answer the calculator gives will always be correct for any problem', 'no'),
                ('That it is fast', 'no'), ('That it is cheap', 'no'),
                'Looks are not tests.'),
              Q('Generated code is like what in this comparison?', 'A new calculator to test',
                ('A calculator that has already been fully tested by thousands of people over many years', 'not yet tested'),
                ('A broken calculator', 'not necessarily'), ('A math book', 'no'),
                'Needs testing.'),
              Q('What should you test code with?', 'Inputs whose correct answers you know',
                ('Inputs chosen at random whose correct answers nobody knows, so the test is fair', 'cannot compare'),
                ('No inputs', 'no'), ('Only one input', 'not enough'),
                'Known-answer tests.'),
          ], why='A learner who trusts neat-looking code can compare testing it with checking a calculator on known '
                 'sums.')],
    F1=sec('Check generated code in practice', WHY, [
        Q('A tool writes a function to count vowels. Which test helps most?', 'Run it on "banana" and expect 3',
          ('Read the comment at the top that says "counts vowels" and accept that it does this correctly', 'not a test'),
          ('Check it has a good name', 'not a test'),
          ('Count its lines', 'not a test'),
          'A known answer: a, a, a.'),
        Q('Generated code calls a function the tool named "sort_smart," which does not exist. What will happen?',
          'An error when it runs',
          ('The computer will create the missing function automatically, based on its name', 'no'),
          ('It will run normally', 'it does not exist'),
          ('It will print the name', 'no'),
          'Invented functions fail.'),
        Q('A function to find the largest number works on [3, 9, 2]. What else should you test?', 'An empty list and negative numbers',
          ('Nothing else, since working on one list of three numbers shows it will work on every list', 'not proof'),
          ('The same list again', 'no new information'),
          ('A list of colors', 'wrong type'),
          'Test boundaries.'),
        Q("Code will calculate students' grades. What extra step is wise?",
          'Have someone experienced review it',
          ('Use it immediately for every student', 'affects people'), ('Delete the tests', 'no'),
          ('Make it shorter', 'not a check'),
          'Higher stakes, more review.'),
        Q('Which shows that code really works?', 'Correct results on several known-answer tests',
          ('A long, confident explanation from the tool describing exactly what the code is doing', 'not proof'),
          ('Neat indentation', 'not proof'),
          ('Many comments', 'not proof'),
          'Behavior is evidence.'),
    ]),
    F2=sec('Trust behavior over descriptions', WHY_F2, [
        Q('A tool explains its code "removes duplicates," but running it leaves duplicates. Which should you trust?',
          'What the code actually does when run',
          ('The explanation, since the tool knows its own code better than any test that you could run', 'behavior wins'),
          ('Neither', 'behavior is evidence'),
          ('The comments', 'can be wrong'),
          'Run it.'),
        Q('A comment says "# adds tax," but the line subtracts. What does this show?', 'Comments can be wrong',
          ('That the subtraction must be correct, because comments are always checked before code runs', 'no'),
          ('That tax is negative', 'no'),
          ('That the code will not run', 'it runs'),
          'Read the code itself.'),
        Q('Which inputs test the boundaries of a function that handles ages?', '0, a very large age, and a missing age',
          ('Three typical adult ages, such as 30, 35 and 40, which cover the most common situations', 'not boundaries'),
          ('Only 25', 'one value'),
          ('Only names', 'wrong type'),
          'Smallest, largest, missing.'),
        Q('Why do confident explanations make wrong code more convincing?', 'They make you less likely to test it',
          ('Because confident explanations actually change the code so that it works correctly', 'no'),
          ('Because they are longer', 'not the point'),
          ('Because they contain numbers', 'not the point'),
          'Tone discourages checking.'),
        Q('Code will handle customer payments. What should happen before use?', 'Experienced review and testing',
          ('Nothing, since payment code written by a tool is always reviewed by a bank automatically', 'not true'),
          ('Only a spell check', 'not enough'),
          ('Only a quick glance', 'not enough'),
          'Money needs review.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.03
REQ = ('A REQUIREMENT says what the code must do, stated clearly enough to check: "Given a list of test scores from 0 '
       'to 100, return the average rounded to one decimal place." EDGE CASES are unusual inputs that often break code: '
       'an EMPTY input (no scores), ZERO, NEGATIVE numbers, very LARGE values, MISSING or WRONG-TYPE data (a score '
       'typed as "ninety"), and BOUNDARY values exactly at a limit (0 and 100). When you ask a tool for code, state '
       'the requirement and the edge cases, and say what should happen for each, such as "if the list is empty, '
       'return 0 and do not crash."')
REQ_F2 = ('Unstated requirements get filled in by guesses. "Sort the names" leaves open: alphabetical or by length? '
          'Uppercase before lowercase? What about "Ana" and "ana"? A tool will pick something, and it may not be what '
          'you need. Write down examples of inputs with the expected outputs; these EXAMPLES double as tests later. '
          'If you are not sure what should happen in a case, decide that first, because the code cannot be right '
          'about a rule nobody chose.')

FIRST_EX = CODE('''
def first_letter(name):
    return name[0]

print(first_letter("Maya"))
''', out='M')

S_CODE03 = SET(
    'AI.CODE.03',
    M=sec('State requirements clearly, including edge cases', REQ, [
        Q('What is a requirement?', 'A checkable statement of what code must do',
          ('A list of the programming languages that the programmer would personally prefer to use', 'not a requirement'),
          ('A guess about what users want', 'not checkable'),
          ('The program\'s file name', 'no'),
          'Clear, checkable.'),
        Q('Which is an edge case for a test-score average?', 'An empty list of scores',
          ('A typical list of five scores between 70 and 90, like the ones most classes have', 'typical case'),
          ('Scores of 80 and 85', 'typical'),
          ('A list of ten scores', 'typical'),
          'Empty input often breaks code.'),
        Q('In this example, which input would break the function?', 'An empty name ""',
          ('"Maya," since names with four letters are too long for this function to handle correctly', 'it works'),
          ('"Al"', 'works'), ('"Zoe"', 'works'),
          'name[0] fails when there is no first letter.', ex=FIRST_EX),
        Q('Which is a boundary value for scores from 0 to 100?', '100',
          ('57, because it is close to the middle of the allowed range of scores', 'not a boundary'),
          ('72', 'middle'), ('85', 'middle'),
          'Exactly at the limit.'),
        Q('Which request includes an edge-case rule?', '"If the list is empty, return 0 and do not crash."',
          ('"Write the code for the average quickly, and make it look clean and professional."', 'no edge case'),
          ('"Make it fast."', 'no edge case'),
          ('"Use good names."', 'no edge case'),
          'Says what to do in an unusual case.'),
    ]),
    B=[cs('Compare edge cases with testing a door lock',
          'When a locksmith tests a new lock, they do not only try the right key once. They try the wrong key, no key, '
          'a key pushed in halfway, turning it very hard, and the lock in freezing weather. These UNUSUAL situations '
          'are where locks fail. Edge cases in code are the same idea: the unusual inputs, such as empty, zero, '
          'negative or wrong-type, where code is most likely to break.', [
              Q('Why does a locksmith try the wrong key?',
          'To see how the lock handles unusual situations',
          ('Because the right key never works on any new lock', 'no'), ('To damage the lock', 'no'),
          ('To save time', 'no'),
          'Test unusual cases.'),
              Q('"No key at all" is like which code input?', 'An empty input',
                ('A typical input that the code was mainly written to handle on a normal day', 'not unusual'),
                ('A very large number', 'different'), ('A correct name', 'no'),
                'Nothing provided.'),
              Q('Freezing weather is like what in code?',
          'Unusual conditions',
          ('Normal use', 'not normal'), ('A comment', 'no'),
          ('A variable name', 'no'),
          'Stress conditions.'),
              Q('Where do locks and code most often fail?', 'In unusual situations',
                ('In the most common situation, the one that the designer tested most carefully', 'least likely'),
                ('Never', 'they fail'), ('Only on weekends', 'no'),
                'Edge cases.'),
              Q('What is the lesson for code?', 'Test unusual inputs, not just the normal one',
                ('Test only the normal input once, because unusual inputs never happen in real life', 'they happen'),
                ('Never test code', 'no'), ('Only test long inputs', 'too narrow'),
                'Edge cases matter.'),
          ], why='A learner unsure what edge cases are can compare them with testing a lock in unusual ways.')],
    F1=sec('Write requirements with edge cases in practice', REQ, [
        Q('Ben asks: "Write code to split a bill." What key detail is missing?', 'How many people and how to round',
          ('Which color to use for the numbers on the screen when the result is finally shown', 'not key'),
          ('The programmer\'s name', 'irrelevant'),
          ('The restaurant\'s address', 'irrelevant'),
          'Inputs and rounding rules.'),
        Q('A function divides a total by the number of people. Which edge case matters most?',
          'Zero people',
          ('Four people', 'typical'), ('Two people', 'typical'),
          ('Three people', 'typical'),
          'Dividing by zero crashes.'),
        Q('Which requirement is clearest?', '"Return the total price including 8% tax, rounded to cents."',
          ('"Make the price thing work properly with tax and everything else that might be needed."', 'vague'),
          ('"Do prices."', 'vague'),
          ('"Handle tax."', 'vague'),
          'Specific and checkable.'),
        Q('A form asks for age. Which input is a wrong-type edge case?', '"twelve" typed as a word',
          ('12, typed as a whole number in the box exactly the way the form designers expected', 'typical'),
          ('15', 'typical'),
          ('30', 'typical'),
          'Text where a number is expected.'),
        Q('A score must be from 0 to 100. Which two inputs test the boundaries?',
          '0 and 100',
          ('50 and 75', 'not boundaries'), ('20 and 30', 'not boundaries'),
          ('60 and 61', 'not boundaries'),
          'Exactly at the limits.'),
    ]),
    F2=sec('Fill gaps in requirements before coding', REQ_F2, [
        Q('"Sort the names" leaves which question open?', 'Alphabetical or by length?',
          ('Nothing, since every program in the world sorts names in exactly the same order', 'not settled'),
          ('Which keyboard to use', 'irrelevant'),
          ('Which font to show', 'irrelevant'),
          'Unstated rules get guessed.'),
        Q('Why write input examples with expected outputs?', 'They clarify the requirement and become tests',
          ('Because examples make the code run faster on every computer that it is installed on', 'not the reason'),
          ('To make the request longer', 'not the point'),
          ('Because tools need exactly ten examples', 'no'),
          'Examples double as tests.'),
        Q('You are unsure whether "Ana" and "ana" count as the same name. What should you do?',
          'Decide the rule before coding',
          ('Let the tool decide quietly', 'risky'), ('Ignore the question', 'leads to bugs'),
          ('Delete one of the names', 'not a rule'),
          'Choose the rule first.'),
        Q('What happens when a requirement is unstated?', 'The tool fills it with a guess',
          ('The tool always asks you a question first and never guesses anything on its own', 'not always'),
          ('The code refuses to run', 'not usually'),
          ('Nothing at all', 'something is chosen'),
          'Guesses may not fit.'),
        Q('Which example helps clarify "remove extra spaces"?', '"  hi   there " becomes "hi there"',
          ('"Make the text look tidier and cleaner by fixing any problems with spacing in it"', 'vague'),
          ('"hello" stays "hello"', 'no spaces involved'),
          ('"Spaces are bad"', 'not an example'),
          'Concrete input and output.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.04
TEST = ('A TEST runs code on a chosen input and compares the result with the EXPECTED result you worked out '
        'yourself. A good test is one that would FAIL if a particular mistake were present. To catch a mistake at a '
        'limit, test the limit itself. Example: the rule is "18 or older is an adult." A function using "age > 18" '
        'looks right and gives True for 20, but it wrongly gives False for 18. Only a test with age 18 reveals this. '
        'Choose tests by asking: "What mistake might be here, and which input would expose it?"')
TEST_F2 = ('Tests can be weak in several ways. A test whose expected answer was copied from the code\'s own output '
           'only checks that the code agrees with itself. A test that uses only typical inputs may never reach the '
           'buggy part. And a test that checks too little, such as "the result is a number," passes even when the '
           'number is wrong. Strong tests use expected answers worked out independently and target the boundaries '
           'and special cases.')

ADULT_EX = CODE('''
def is_adult(age):
    return age > 18

print(is_adult(20))
print(is_adult(18))
''', out='True\nFalse')

S_CODE04 = SET(
    'AI.CODE.04',
    M=sec('Choose a test whose expected result would reveal a defect', TEST, [
        Q('What does a test compare?', 'The code\'s result with an expected result you worked out',
          ('The code\'s length with the length of another program that solves the same problem', 'not a test'),
          ('Two programmers\' opinions', 'not a test'),
          ('The code\'s speed with the internet speed', 'no'),
          'Actual versus expected.'),
        Q('In this example, which test reveals the bug?', 'is_adult(18)',
          ('is_adult(20), because 20 is the most typical age and therefore the best test of the rule', 'it passes'),
          ('is_adult(30)', 'passes'), ('is_adult(50)', 'passes'),
          '18 should be True but gives False.', ex=ADULT_EX),
        Q('What is the bug in the same example?',
          'It uses > instead of >=',
          ('It uses the word "age,"', 'allowed'), ('It prints too much', 'not the bug'),
          ('It has no name', 'it does'),
          '18 or older needs >=.',
          ex=ADULT_EX),
        Q('What makes a test good?', 'It would fail if a particular mistake were present',
          ('It always passes, which shows that the code is working correctly every single time', 'not useful'),
          ('It is very long', 'not the point'),
          ('It uses random inputs', 'not targeted'),
          'Targeted at a mistake.'),
        Q('To catch a mistake at a limit, what should you test?', 'The limit itself',
          ('A value far away from the limit, where the code is very unlikely to make any mistakes', 'misses it'),
          ('Nothing', 'must test'),
          ('Only typical values', 'misses it'),
          'Boundaries expose errors.'),
    ]),
    B=[sk('Pick the input that exposes a suspected mistake',
          'Work backward from the mistake. Ask: "If the code had this mistake, which input would give a different '
          'answer from the correct code?" Example: a free-shipping rule says "orders of 50 dollars or more ship free." '
          'Suspected mistake: using > 50 instead of >= 50. Inputs 30 and 80 give the same answers either way. Only '
          'input 50 differs: the correct rule says free, the mistaken one says not free. So 50 is the test to run, '
          'expecting "free."', [
              Q('Which input exposes > 50 versus >= 50?', '50',
                ('80, because larger orders are always the best way to test any rule about shipping', 'same either way'),
                ('30', 'same either way'), ('100', 'same either way'),
                'Only 50 differs.'),
              Q('For input 50, what should the test expect?',
          'Free shipping',
          ('Not free', 'rule says or more'), ('An error', 'no'),
          ('Half-price shipping', 'no'),
          '"50 or more" includes 50.'),
              Q('Why do 30 and 80 not help?',
          'Both rules give the same answer for them',
          ('Because 30 and 80 are not real prices', 'they are fine'), ('They are too large', 'no'),
          ('They crash the code', 'no'),
          'No difference to detect.'),
              Q('What question drives the method?', 'Which input gives a different answer if the mistake exists?',
                ('Which input is the largest number that the program is able to handle without crashing?', 'not the question'),
                ('Which input is the most common?', 'not the question'),
                ('Which input is easiest to type?', 'not the question'),
                'Target the difference.'),
              Q('Rule: "under 13 pays child price." Suspected mistake: <= 13. Which input exposes it?', '13',
                ('5, because young children are the main customers who pay the child price at the door', 'same either way'),
                ('20', 'same either way'), ('12', 'same either way'),
                'Only 13 differs.'),
          ], why='A learner who chooses tests at random practices the underlying skill of picking the input that '
                 'separates correct from mistaken code.')],
    F1=sec('Design tests that catch mistakes', TEST, [
        Q('A function should give a discount to orders of 100 dollars or more. Which test is most useful?',
          'An order of exactly 100, expecting a discount',
          ('An order of 500, which is so large that it should definitely get the discount in any case', 'misses the limit'),
          ('An order of 20, expecting no discount', 'misses the limit'),
          ('No test', 'must test'),
          'Test the boundary.'),
        Q('A function should count words. Which test could reveal a mistake with extra spaces?',
          '"hi  there" (two spaces), expecting 2',
          ('"hello," a single word with no spaces at all, which is the simplest possible test', 'no spaces'),
          ('"one two" with one space', 'typical'),
          ('An empty test', 'not targeted'),
          'Target the suspected mistake.'),
        Q('Ana writes a test expecting the average of [2, 4] to be 3. The code returns 3. What does this show?',
          'The code passes this test',
          ('That the code is correct for every possible list of numbers, including empty lists', 'one test'),
          ('That the test is wrong', 'it is right'),
          ('Nothing at all', 'it shows a pass'),
          'One pass, not full proof.', calc=lambda: (2 + 4) / 2 == 3),
        Q('A function should reject passwords shorter than 8 characters. Which input tests the boundary?',
          'A password of exactly 7 characters, expecting rejection',
          ('A password of 30 characters, since longer passwords are the most important ones to check', 'far from limit'),
          ('A password of 15 characters', 'far from limit'),
          ('No password', 'different case'),
          'Just below the limit.'),
        Q('Which expected result should a test use?', 'One you worked out yourself',
          ('Whatever the code printed the first time it ran, since the code is the best source of answers', 'circular'),
          ('A random number', 'not a check'),
          ('The tool\'s guess', 'not independent'),
          'Independent expected answers.'),
    ]),
    F2=sec('Spot weak tests', TEST_F2, [
        Q('A test\'s expected answer was copied from the code\'s output. What is the problem?', 'It only checks the code agrees with itself',
          ('Nothing, because the code\'s own output is always the most reliable expected answer', 'circular'),
          ('The test is too long', 'not the problem'),
          ('The test uses numbers', 'not the problem'),
          'Not independent.'),
        Q('A test checks only that the result "is a number." Why is it weak?', 'It passes even when the number is wrong',
          ('Because numbers can never be checked by tests in Python, only words and letters', 'not true'),
          ('Because it is too strict', 'too loose'),
          ('Because numbers are not results', 'they are'),
          'Checks too little.'),
        Q('All tests use typical inputs. What might they miss?', 'Bugs at boundaries and special cases',
          ('Nothing, since typical inputs exercise every single line of code in every program', 'not always'),
          ('Spelling mistakes in comments', 'not the point'),
          ('The program\'s file name', 'irrelevant'),
          'Untested paths.'),
        Q('Which test is strongest for a function that returns the largest of three numbers?',
          'Largest in last place: (1, 2, 9) expecting 9',
          ('(9, 2, 1) expecting a number of some kind', 'checks too little'), ('(5, 5, 5) expecting a result', 'checks too little'),
          ('No test', 'must test'),
          'Specific expected answer, tricky position.'),
        Q('Where should strong tests focus?', 'Boundaries and special cases, with independent answers',
          ('The most common input only, run many times in a row to make sure it gives the same result', 'not enough'),
          ('Random inputs with no expected answers', 'cannot compare'),
          ('Only the program name', 'no'),
          'Targeted and independent.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.05
ERR = ('When Python hits a problem, it stops and shows an ERROR MESSAGE, often called a TRACEBACK. Read it from the '
       'BOTTOM: the last line names the error type and a short explanation, and the line above names the FILE and LINE '
       'NUMBER where it happened. Common types: NameError (a name that was never defined, often a typo), TypeError '
       '(mixing types, such as adding text to a number), IndexError (asking for a position that does not exist) and '
       'ValueError (a value of the right type but wrong content). Use the message to find the problem before asking '
       'a tool to fix it, and include the full message when you ask.')
ERR_F2 = ('The line named in a traceback is where Python noticed the problem, not always where it started. A wrong '
          'value created earlier may only cause an error later. Fixes suggested by tools can hide errors instead of '
          'solving them, for example wrapping code so the error is silently ignored. Prefer fixes that address the '
          'cause, and after any fix, run the original failing case again to confirm the error is gone and the result '
          'is right.')

IDX_EX = TEXT('scores = [90, 85, 77]\nprint(scores[3])\n\nTraceback (most recent call last):\n  File "grades.py", line 2, '
              'in <module>\n    print(scores[3])\nIndexError: list index out of range',
              label='Prepared code example (Python 3) and its error message, simplified. Shown only; nothing runs.')
NAME_EX = TEXT('total = 50\nprint(totl)\n\nTraceback (most recent call last):\n  File "shop.py", line 2, in <module>\n'
               '    print(totl)\nNameError: name \'totl\' is not defined',
               label='Prepared code example (Python 3) and its error message, simplified. Shown only; nothing runs.')
TYPE_EX = TEXT('age = 15\nprint("Age: " + age)\n\nTraceback (most recent call last):\n  File "card.py", line 2, in '
               '<module>\n    print("Age: " + age)\nTypeError: can only concatenate str (not "int") to str',
               label='Prepared code example (Python 3) and its error message, simplified. Shown only; nothing runs.')

S_CODE05 = SET(
    'AI.CODE.05',
    M=sec('Use an error message to locate a problem', ERR, [
        Q('Where should you start reading a traceback?',
          'At the bottom',
          ('At the very top', 'it does not'), ('In the middle', 'no'),
          ('Nowhere; ignore it', 'it helps'),
          'The last line names the error.'),
        Q('In this example, what type of error is shown?', 'IndexError',
          ('NameError, because the list called scores was never defined anywhere in the program', 'it was'),
          ('TypeError', 'no'), ('ValueError', 'no'),
          'Position 3 does not exist.', ex=IDX_EX),
        Q('In the same example, why is position 3 out of range?', 'Python counts positions from 0, so they are 0 to 2',
          ('Because lists in Python can only hold two items at most, so the third item is ignored', 'no'),
          ('Because 77 is too large', 'no'),
          ('Because print cannot show lists', 'no'),
          'Three items: positions 0, 1, 2.', ex=IDX_EX),
        Q('In this example, what caused the NameError?', 'A typo: totl instead of total',
          ('The number 50 is too large for Python to store under any variable name', 'no'),
          ('print is misspelled', 'it is not'),
          ('The file name is wrong', 'no'),
          'A name never defined.', ex=NAME_EX),
        Q('When asking a tool to fix an error, what should you include?', 'The full error message',
          ('Only the words "it is broken," since the tool can work out the rest by itself', 'too little'),
          ('Nothing', 'too little'),
          ('Only the file name', 'too little'),
          'Full message, plus the code.'),
    ]),
    B=[sk('Read the last two lines of a traceback',
          'Most of what you need is in the last two lines of a traceback. The LAST line has the error TYPE and a short '
          'explanation. The line just above it (usually) shows the code that failed, and the line above that names the '
          'FILE and LINE NUMBER. Example ending: \'File "pay.py", line 7\' then \'rate = hours / 0\' then '
          '\'ZeroDivisionError: division by zero.\' That tells you: file pay.py, line 7, dividing by zero.', [
              Q('In the example, which file has the error?', 'pay.py',
                ('ZeroDivisionError, which is the name of the file where the problem happened', 'that is the type'),
                ('line 7', 'that is the line'), ('rate', 'that is a variable'),
                'Named in the File line.'),
              Q('Which line number?', '7',
                ('0, because the error message mentions division by zero in the last line', 'not a line number'),
                ('1', 'no'), ('2', 'no'),
                'From the File line.'),
              Q('What is the error type?', 'ZeroDivisionError',
                ('pay.py, which is listed just above the line of code that caused the problem', 'that is the file'),
                ('line 7', 'no'), ('hours', 'no'),
                'The last line.'),
              Q('What is the problem?',
          'Dividing by zero',
          ('A misspelled variable name', 'not this one'), ('A missing file', 'no'),
          ('Adding text to numbers', 'no'),
          'Division by zero.'),
              Q('Which two lines hold most of the information?',
          'The last two',
          ('The first two', 'reversed'), ('The middle two', 'no'),
          ('None', 'they help'),
          'Read from the bottom.'),
          ], why='A learner overwhelmed by tracebacks practices the underlying skill of reading only the last lines.')],
    F1=sec('Locate problems from error messages', ERR, [
        Q('In this example, what is the problem?', 'Adding text to a number',
          ('The variable name "age" is not allowed in Python, so the program cannot run at all', 'allowed'),
          ('The number 15 is too large', 'no'),
          ('A missing file', 'no'),
          'TypeError: str plus int.', ex=TYPE_EX),
        Q('In the same example, which line has the problem?',
          'Line 2',
          ('Line 1', 'no'), ('Line 3', 'there is none'),
          ('Line 15', 'that is the age'),
          'Named in the traceback.',
          ex=TYPE_EX),
        Q('int("ten") gives "ValueError: invalid literal for int()." What does it mean?', 'The text is not a number Python can convert',
          ('The program forgot to define a variable called "ten" before using it on this line', 'that is NameError'),
          ('The list is too short', 'IndexError'),
          ('The file is missing', 'no'),
          'Right type, wrong content.'),
        Q('A NameError names "prnt." What is the likely cause?',
          'A typo for print',
          ('A missing list item', 'IndexError'), ('Dividing by zero', 'no'),
          ('Text plus a number', 'no'),
          'Misspelled name.'),
        Q('Before asking a tool for a fix, what is a good first step?',
          'Find the line and error type yourself',
          ('Delete the whole program and start again', 'unnecessary'), ('Ignore the message', 'it helps'),
          ('Restart the computer', 'not a fix'),
          'Locate the problem.'),
    ]),
    F2=sec('Trace errors to their cause and confirm fixes', ERR_F2, [
        Q('An error appears on line 20, but the wrong value was created on line 5. Where is the cause?',
          'Line 5',
          ('Line 20', 'not always'), ('Line 1', 'not stated'),
          ('Nowhere', 'there is a cause'),
          'Errors can surface later.'),
        Q('A tool "fixes" an error by making the program ignore all errors silently. What is wrong?', 'It hides the problem',
          ('Nothing, because a program that shows no errors on screen is always working correctly', 'not true'),
          ('It is too short', 'not the issue'),
          ('It uses Python', 'not the issue'),
          'Address the cause.'),
        Q('After applying a fix, what should you do?', 'Rerun the original failing case',
          ('Move on without testing, since the tool already confirmed the fix would definitely work', 'confirm'),
          ('Delete the test', 'no'),
          ('Ask for another fix', 'test first'),
          'Confirm the fix.'),
        Q('The error is gone, but the output is now wrong. Is it fixed?', 'No; the result must also be right',
          ('Yes, because removing an error message is the same thing as fixing the problem', 'not the same'),
          ('Yes, if it is fast', 'no'),
          ('It cannot be known', 'it can'),
          'No error is not the same as correct.'),
        Q('Which fix addresses the cause of IndexError from scores[3] on a 3-item list?', 'Use a valid position, such as scores[2]',
          ('Hide the error message so that the program keeps running and prints nothing at all', 'hides it'),
          ('Rename the list', 'not the cause'),
          ('Add more print lines', 'not a fix'),
          'Fix the position.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.06
REVIEW = ('Tools can EXPLAIN code in plain words, which is helpful for learning. Treat an explanation as a STARTING '
          'POINT: it may describe what code was meant to do rather than what it does. A CODE REVIEW checks code LINE '
          'BY LINE against its REQUIREMENTS. For each line ask: What does it do? Is it needed? Does it match the '
          'requirement? Is anything missing? Comments, names and explanations can all be wrong, so check the actual '
          'statements. Example: a comment says "return the largest number," but the code uses min(), which returns '
          'the smallest.')
REVIEW_F2 = ('A good review also looks for what is NOT there: a missing check for empty input, a requirement that was '
             'skipped, or an unhandled error. Large changes are hard to review well; ask for small changes you can '
             'read in full. If you cannot understand a part of the code, that is a finding: ask for a simpler version '
             'or an explanation you can verify by running small examples, rather than approving it.')

BIG_EX = CODE('''
# Return the largest number in the list
def biggest(nums):
    return min(nums)

print(biggest([4, 9, 2]))
''', out='2')

S_CODE06 = SET(
    'AI.CODE.06',
    M=sec('Use explanations as a starting point and review code against requirements', REVIEW, [
        Q("How should you treat a tool's explanation of code?",
          'As a starting point to check',
          ('As proof of what the code does', 'not proof'), ('As useless', 'it helps'),
          ('As a replacement for running it', 'no'),
          'Helpful, but verify.'),
        Q('In this example, what does the program print?', '2',
          ('9, because the comment says the function returns the largest number in the list', 'comment is wrong'),
          ('4', 'no'), ('15', 'no sum'),
          'min() returns the smallest.', ex=BIG_EX),
        Q('In the same example, what is wrong?', 'The code uses min() but the requirement is the largest',
          ('The comment uses the word "largest," which is not allowed in Python comments', 'allowed'),
          ('The list is too short', 'no'), ('Nothing', 'it is wrong'),
          'Code does not match the requirement.', ex=BIG_EX),
        Q('What does a code review check?', 'Each line against the requirements',
          ('Only that the code has comments and that the variable names are long and descriptive', 'not enough'),
          ('Only the file name', 'no'),
          ('Only the indentation', 'no'),
          'Line by line, against requirements.'),
        Q('What can be wrong in code besides the statements?', 'Comments, names and explanations',
          ('Nothing; only the statements in a program can ever contain any mistakes at all', 'others can mislead'),
          ('Only the spaces', 'no'),
          ('Only the colors', 'no'),
          'All can mislead.'),
    ]),
    B=[cs('Compare reviewing code with proofreading a recipe',
          'When you proofread a recipe for a friend, you do not just read the title ("Easy Chocolate Cake") and say '
          '"looks good." You check each line: is it "1 cup sugar" or "1 tablespoon"? Is the oven temperature there? '
          'Did they forget the eggs? The title is like a code comment: it tells you what it is supposed to be. The '
          'lines tell you what will actually happen. Code review is proofreading each line against what the code '
          'should do.', [
              Q('Why not stop at the recipe title?',
          'It says what it should be, not what the lines do',
          ('Because titles of recipes are always wrong', 'too strong'), ('Because titles are too short', 'not the point'),
          ('Because cakes have no titles', 'no'),
          'Check the lines.'),
              Q('The recipe title is like what in code?', 'A comment',
                ('A test that runs the code on several inputs and compares the results with answers', 'no'),
                ('An error message', 'no'), ('A variable', 'no'),
                'Intent, not behavior.'),
              Q('Checking "cup" versus "tablespoon" is like what?', 'Checking each line\'s details',
                ('Reading the title of the recipe twice to make sure that the cake is called the right thing', 'not detail'),
                ('Counting pages', 'no'), ('Choosing a font', 'no'),
                'Line-by-line review.'),
              Q('Noticing missing eggs is like what in a code review?', 'Finding something missing',
                ('Finding a misspelled comment that does not change what the program actually does', 'not missing'),
                ('Running the code', 'no'), ('Renaming a variable', 'no'),
                'Look for what is not there.'),
              Q('What decides whether the cake will work?', 'The actual lines',
                ('The title of the recipe, which tells the baker exactly how the cake will turn out', 'not the title'),
                ('The photo', 'no'), ('The page color', 'no'),
                'Behavior comes from statements.'),
          ], why='A learner who reviews only comments and titles can compare code review with proofreading a recipe.')],
    F1=sec('Review code against requirements in practice', REVIEW, [
        Q('Requirement: "Return the number of students who passed (score 60 or more)." The code counts scores above 60. '
          'What is the issue?',
          'It misses students who scored exactly 60',
          ('Nothing, since a score of exactly 60 is so rare that it can be safely ignored in practice', 'requirement includes it'),
          ('It counts too many', 'too few'),
          ('It uses numbers', 'no'),
          'Above 60 excludes 60.'),
        Q('A tool explains code as "sorts names alphabetically," but output shows them by length. What should you trust?',
          'The output',
          ('The explanation', 'behavior wins'), ('Neither', 'output is evidence'),
          ('The comment', 'can be wrong'),
          'Behavior is evidence.'),
        Q('During review, you find a line whose purpose you cannot tell. What should you do?', 'Ask about it and test it before approving',
          ('Approve it anyway, since lines you do not understand are usually the most clever parts of code', 'risky'),
          ('Delete it without checking', 'may break things'),
          ('Ignore it', 'risky'),
          'Unclear code is a finding.'),
        Q('Which review question asks about missing parts?', '"Is anything the requirement needs not here?"',
          ('"Is the variable name long enough to describe exactly what the variable is used for?"', 'naming'),
          ('"Is the font readable?"', 'no'),
          ('"Is it short?"', 'no'),
          'Look for omissions.'),
        Q('Which is the best use of a code explanation?', 'To learn what to check, then verify by running',
          ('To replace testing entirely, since a clear explanation proves that the code is correct', 'not proof'),
          ('To skip reading the code', 'no'),
          ('To decide the requirement', 'requirements come first'),
          'Starting point.'),
    ]),
    F2=sec('Review for what is missing and keep changes reviewable', REVIEW_F2, [
        Q('Code divides by the number of items but never checks for zero items. What kind of finding is this?',
          'A missing check',
          ('A naming problem', 'not naming'), ('A comment problem', 'no'),
          ('No problem', 'it can crash'),
          'Something absent.'),
        Q('A tool proposes changing 400 lines at once. What helps review?',
          'Asking for smaller changes',
          ('Approving all 400 lines quickly', 'risky'), ('Reading only the first line', 'not enough'),
          ('Skipping review', 'risky'),
          'Small changes are reviewable.'),
        Q('You cannot understand part of a generated function. What is the right response?', 'Ask for a simpler version or verify with small examples',
          ('Approve it, because code that is hard to understand is usually more efficient and better', 'not a reason'),
          ('Pretend you understand', 'no'),
          ('Remove the whole program', 'excessive'),
          'Understanding is part of review.'),
        Q('A requirement says "log every failed login," but the code logs only some. What is this?', 'A skipped requirement',
          ('A style choice that the programmer is free to make without checking the requirements', 'not optional'),
          ('A typo', 'no'),
          ('A faster design', 'not the point'),
          'Missing behavior.'),
        Q('Which review finding is most serious?', 'An unhandled error that can crash the program',
          ('A comment that uses slightly informal language, such as "grab the list" instead of "get"', 'minor'),
          ('A blank line', 'minor'),
          ('A long variable name', 'minor'),
          'Crashes matter.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.07
GIT = ('VERSION CONTROL keeps a history of code changes. A popular tool for it is called Git. A COMMIT is a saved '
       'snapshot with a short message ("Fix average for empty list"). A DIFF (difference) shows what changed '
       'between versions: lines starting with "-" were removed and lines with "+" were added. REVERTING undoes a '
       'commit by applying the opposite change. A good habit with AI help: COMMIT BEFORE accepting generated changes, '
       'so you can see exactly what the tool changed in the diff and undo it if it breaks something.')
GIT_F2 = ('Commit messages should say what changed and why, so others (and future you) can understand the history. '
          'Small commits that each do one thing are easier to review and undo than one huge commit. Generated changes '
          'sometimes touch files you did not expect, such as settings or unrelated code; the diff reveals this. Never '
          'commit secrets like passwords, because version history keeps them even after you delete them from the '
          'latest version.')

DIFF_EX = TEXT('- total = price * count\n+ total = price + count',
               label='Prepared example (a diff in a fictional project). Shown only; nothing runs.')

S_CODE07 = SET(
    'AI.CODE.07',
    M=sec('Explain commits, diffs and reverting', GIT, [
        Q('What is a commit?', 'A saved snapshot of code with a message',
          ('A promise from the programmer to finish the project by a certain date in the future', 'not the meaning'),
          ('An error message', 'no'),
          ('A deleted file', 'no'),
          'Snapshot plus message.'),
        Q('In a diff, what does a line starting with "+" mean?',
          'It was added',
          ('It was removed', 'reversed'), ('It is a comment', 'no'),
          ('It has an error', 'no'),
          'Plus means added.'),
        Q('In this example, what changed?',
          'Multiplication became addition',
          ('Addition became multiplication', 'reversed'), ('Nothing changed', 'a line changed'),
          ('The variable was renamed', 'no'),
          '"*" removed, "+" added.',
          ex=DIFF_EX),
        Q('What does reverting do?',
          'Undoes a commit with the opposite change',
          ('Deletes the whole project and its history', 'not reverting'), ('Copies the project', 'no'),
          ('Runs the tests', 'no'),
          'Undo a change.'),
        Q('Why commit before accepting generated changes?', 'To see what changed and undo it if needed',
          ('Because tools refuse to change code that has not been committed first in every project', 'not the reason'),
          ('To make the code run faster', 'no'),
          ('To hide changes', 'no'),
          'A safe restore point.'),
    ]),
    B=[cs('Compare version control with save points in a video game',
          'In many video games you can SAVE before a hard level. If things go badly, you LOAD the save and try again. '
          'Each save is like a commit: a snapshot you can return to. Comparing two saves to see what changed, such as '
          'items gained or lost, is like a diff. Going back to an earlier save is like reverting. Saving before '
          'letting someone else play your game is like committing before accepting AI changes.', [
              Q('A game save is like what?',
          'A commit',
          ('A diff', 'not a diff'), ('A bug', 'no'),
          ('A test', 'no'),
          'A snapshot.'),
              Q('Comparing two saves to see what changed is like what?',
          'A diff',
          ('A commit message', 'no'), ('A revert', 'no'),
          ('A new game', 'no'),
          'What changed.'),
              Q('Loading an earlier save is like what?', 'Reverting',
                ('Committing a brand-new change that adds a new level to the game for every player', 'no'),
                ('Deleting the game', 'no'), ('Buying a game', 'no'),
                'Going back.'),
              Q('Saving before a friend plays is like what?', 'Committing before accepting AI changes',
                ('Deleting every save file so that your friend can start the whole game from the beginning', 'opposite'),
                ('Turning off the game', 'no'), ('Changing the controls', 'no'),
                'A restore point first.'),
              Q('Why save before a hard level?', 'To return if things go badly',
                ('Because saving makes the next level easier to beat on the very first try', 'no'),
                ('To end the game', 'no'), ('To change the music', 'no'),
                'Safety net.'),
          ], why='A learner new to version control can relate commits, diffs and reverts to game save points.')],
    F1=sec('Use commits and diffs with AI changes', GIT, [
        Q('Ravi lets a tool edit his project and now tests fail. He committed before the edit. What can he do?',
          'Revert to the earlier commit',
          ('Nothing, because changes made by a tool can never be undone once they have been accepted', 'he can revert'),
          ('Delete the project', 'unnecessary'),
          ('Ignore the tests', 'risky'),
          'The commit is a restore point.'),
        Q('A diff shows "- if age >= 18:" and "+ if age > 18:". What changed?', 'The rule now excludes exactly 18',
          ('The rule now includes more ages than before, such as 17, because > is a larger sign', 'it excludes 18'),
          ('Nothing important', 'it matters'),
          ('The variable name', 'no'),
          'Boundary changed.'),
        Q('Which commit message is most useful?', '"Fix average to handle an empty list"',
          ('"Changes," which tells everyone that something in the project was changed at that time', 'vague'),
          ('"stuff"', 'vague'),
          ('"asdf"', 'meaningless'),
          'What and why.'),
        Q('Why read the diff after a tool edits code?', 'To see exactly what it changed',
          ('Because diffs fix every bug automatically when they are opened and read by a person', 'no'),
          ('To make the code longer', 'no'),
          ('To rename files', 'no'),
          'Know what changed.'),
        Q('A diff shows only "+" lines and no "-" lines. What happened?', 'Lines were only added',
          ('Every line in the file was deleted and replaced with completely different lines', 'no removals'),
          ('Nothing changed', 'lines added'),
          ('Only comments were removed', 'no removals'),
          'Additions only.'),
    ]),
    F2=sec('Keep history clear and safe', GIT_F2, [
        Q('A diff from a tool edit shows changes to a settings file you did not ask about. What should you do?',
          'Review those changes before accepting',
          ('Accept everything, since tools only change files that were needed for the requested task', 'not always'),
          ('Ignore the diff', 'risky'),
          ('Delete the settings file', 'risky'),
          'Unexpected changes need review.'),
        Q('Why prefer small commits?', 'They are easier to review and undo',
          ('Because large commits are not allowed by any version control tool that exists today', 'not the reason'),
          ('Because small commits use more storage', 'not the reason'),
          ('Because they hide changes', 'no'),
          'One thing per commit.'),
        Q('A password was committed and then deleted in the next commit. Is it gone?', 'No; history still has it',
          ('Yes, because deleting it in the latest version also removes it from every past version', 'history keeps it'),
          ('Yes, after one day', 'no'),
          ('Only if the file is small', 'no'),
          'Never commit secrets.'),
        Q('What should a commit message say?',
          'What changed and why',
          ('Only the date and time', 'not enough'), ("Only the programmer's name", 'recorded already'),
          ('Nothing', 'loses meaning'),
          'Clear history.'),
        Q('Which history is easiest to understand later?', 'Small commits with clear messages',
          ('One huge commit called "update" that contains every change made over three months', 'hard to follow'),
          ('No commits', 'no history'),
          ('Commits with random messages', 'hard to follow'),
          'Clarity for future readers.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.08
DEPS = ('Programs often use LIBRARIES, also called PACKAGES or DEPENDENCIES: code written by others that you install '
        'from a public collection, such as PyPI for Python. AI tools sometimes suggest a package that DOES NOT EXIST, '
        'and attackers can register those invented names with harmful code. This is sometimes called '
        '"slopsquatting." Researchers studying code-generating models (USENIX Security 2025) documented such '
        'invented package names. Before installing a suggested package, check that it exists, that it is the one you '
        'intended (not a look-alike name), and that it shows signs of trust: an active project, real documentation, '
        'and use by others.')
DEPS_F2 = ('Look-alike names are a related risk: "reqeusts" instead of "requests," or a package with an extra word. '
           'Even real packages can be abandoned or compromised. Prefer well-known packages your course, school or '
           'workplace already uses, record exact versions, and do not add a dependency for something a few lines of '
           'your own code can do. When unsure, ask someone experienced before installing.')

S_CODE08 = SET(
    'AI.CODE.08',
    M=sec('Check that a suggested library exists and is trustworthy', DEPS, [
        Q('What is a package or dependency?', 'Code written by others that your program installs and uses',
          ('A box that a computer is shipped in, which contains the cables and the instructions', 'not the meaning'),
          ('An error message', 'no'),
          ('A comment', 'no'),
          'Reusable code from others.'),
        Q('What can go wrong when a tool suggests a package?', 'It may not exist, and attackers can register the name',
          ('Nothing, because tools only ever suggest packages that have been checked for safety', 'not true'),
          ('It may be too popular', 'not the risk'),
          ('It may have documentation', 'not a risk'),
          'Invented names can be exploited.'),
        Q('What is "slopsquatting"?', 'Registering package names that AI tools invent',
          ('Writing very messy code on purpose so that other people find it hard to read and copy', 'not the meaning'),
          ('Deleting old packages', 'no'),
          ('Sorting a list', 'no'),
          'Exploiting hallucinated names.'),
        Q('Which is a sign of a trustworthy package?', 'An active project with real documentation and users',
          ('A brand-new name that nobody has used, with no documentation and no project page at all', 'warning signs'),
          ('A name that looks like a famous one', 'warning sign'),
          ('No description', 'warning sign'),
          'Signs of trust.'),
        Q('Before installing a suggested package, what should you check first?', 'That it exists and is the intended one',
          ('That its name is short enough to type quickly without making spelling mistakes', 'not the check'),
          ('Its logo color', 'no'),
          ('Nothing', 'must check'),
          'Existence and identity.'),
    ]),
    B=[cs('Compare package checks with checking a contractor',
          'Before letting a contractor into your home to fix wiring, you check they are real: a business that exists, '
          'reviews from other customers, a license. You would be wary of someone with a name almost like a famous '
          'company\'s but one letter off, or a company nobody has heard of that showed up uninvited. Installing a '
          'package lets someone else\'s code into your program, so it deserves the same check.', [
              Q('Why check that a contractor exists?', 'Because you are letting them into your home',
                ('Because contractors who exist always do perfect work, so existence is all that matters', 'not enough'),
                ('To get a discount', 'no'), ('To learn their age', 'no'),
                'Access requires trust.'),
              Q('A name one letter off from a famous company is like what?', 'A look-alike package name',
                ('A well-known package used by thousands of programmers and checked carefully', 'opposite'),
                ('A commit', 'no'), ('A test', 'no'),
                'Impersonation risk.'),
              Q('Reviews from other customers are like what for a package?',
          'Signs it is used by others',
          ("The package's file size", 'not the comparison'), ('Its error messages', 'no'),
          ('Its name length', 'no'),
          'Evidence of trust.'),
              Q('Installing a package is like what?', 'Letting someone else\'s work into your project',
                ('Writing every line of the program yourself without using anyone else\'s code', 'opposite'),
                ('Deleting a file', 'no'), ('Running a test', 'no'),
                'Trusting others\' code.'),
              Q('What is the lesson?', 'Check a package before installing it',
                ('Never use code written by anyone else, under any circumstances, in any project', 'too strong'),
                ('Install anything suggested', 'risky'), ('Only use paid packages', 'not the point'),
                'Verify first.'),
          ], why='A learner who installs packages without thinking can compare it with checking a contractor.')],
    F1=sec('Check suggested packages in practice', DEPS, [
        Q('A tool suggests "pip install easy-pdf-magic-tools." You find no project page. What should you do?',
          'Do not install it; look for a well-known alternative',
          ('Install it quickly, since a missing project page just means the package is very new', 'warning sign'),
          ('Install it twice', 'no'),
          ('Rename it and install', 'no'),
          'No evidence it is real or safe.'),
        Q('A suggestion says "reqeusts." What should you notice?', 'It is a look-alike of "requests"',
          ('Nothing, because small spelling differences in package names do not matter at all', 'they matter'),
          ('It is a newer version', 'not shown'),
          ('It is a test file', 'no'),
          'Misspelled look-alike.'),
        Q('Which package choice is safest for a class project?', 'One the course already uses',
          ('A package that a tool invented a name for, since invented packages are designed for the task', 'may not exist'),
          ('A random new package', 'unknown'),
          ('One with no documentation', 'warning sign'),
          'Known and trusted.'),
        Q('A tool suggests a package to add two numbers. What is the better choice?',
          'Write the one line yourself',
          ('Install the package', 'unneeded risk'), ('Install three packages', 'worse'),
          ('Skip adding numbers', 'no'),
          'Avoid unnecessary dependencies.'),
        Q('Where should you check that a Python package exists?', 'Its page on the official package index (PyPI)',
          ('In the tool\'s answer itself, since the tool would not suggest a package that did not exist', 'circular'),
          ('A random forum', 'not reliable'),
          ('Your memory', 'not reliable'),
          'Check the official index.'),
    ]),
    F2=sec('Manage dependency risks over time', DEPS_F2, [
        Q('A real, popular package has had no updates for years and has open security warnings. What is the concern?',
          'It may be abandoned',
          ('No concern', 'can be abandoned'), ('It is too popular', 'not the concern'),
          ('It has too many users', 'not the concern'),
          'Old, unmaintained risk.'),
        Q('Why record exact package versions?',
          'So builds are repeatable and changes are deliberate',
          ('Because package managers refuse to install anything', 'not the reason'), ('To make files longer', 'no'),
          ('To hide which packages are used', 'no'),
          'Predictable dependencies.'),
        Q('A student is unsure whether a package is trustworthy. What is the best step?', 'Ask someone experienced before installing',
          ('Install it on the school\'s shared computer first to see whether anything bad happens', 'risky'),
          ('Install it and hope', 'risky'),
          ('Share it with classmates', 'spreads risk'),
          'Ask first.'),
        Q('Which name is the most suspicious?', '"numpy-official-secure-v2"',
          ('"numpy," which is a widely used package for working with numbers in Python programs', 'well known'),
          ('"pandas"', 'well known'),
          ('"requests"', 'well known'),
          'Extra words can mark look-alikes.'),
        Q('Do real packages ever become unsafe?', 'Yes; they can be compromised',
          ('No; once a package is real and popular, it can never become unsafe in any way at all', 'they can'),
          ('Only on weekends', 'no'),
          ('Only if renamed', 'no'),
          'Ongoing vigilance.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.09
SECRETS = ('A SECRET is a password, API key (a code that lets a program use a paid or private service) or similar '
           'credential. Never write secrets directly in code that will be shared or committed; store them separately, '
           'for example in a settings file kept private or an ENVIRONMENT VARIABLE (a value set outside the code). '
           'Also never paste secrets into a chat with an AI tool. A second risk is UNSAFE INPUT: code that takes what a '
           'user types and builds a command from it can be tricked. SQL (Structured Query Language) for databases is '
           'a classic case: inserting typed text straight into a query lets attackers change the query.')
SECRETS_F2 = ('Generated code often uses placeholder secrets ("API_KEY = \'your-key-here\'"), and people replace them '
              'with real keys in the same spot, then share the file. If a secret is exposed, CHANGE IT (rotate it) at '
              'the service right away; deleting it from the code is not enough. For input, use the safe methods a '
              'language provides, such as PARAMETERIZED QUERIES that keep user text separate from the command, and '
              'treat everything a user types as untrusted.')

KEY_EX = CODE('''
API_KEY = "sk-live-4f9a2c7e1b"
print("Connecting with key", API_KEY)
''', out='Connecting with key sk-live-4f9a2c7e1b',
    label='Prepared code example (Python 3) with a fake key. Shown only; nothing runs.')
SQL_EX = CODE('''
name = input("Name: ")
query = "SELECT * FROM students WHERE name = '" + name + "'"
''', runs=False, label='Prepared code fragment (Python 3). Shown only; nothing runs.')

S_CODE09 = SET(
    'AI.CODE.09',
    M=sec('Spot exposed secrets and unsafe handling of input', SECRETS, [
        Q('What is an API key?', 'A code that lets a program use a private or paid service',
          ('A keyboard key that programmers press to run their code faster than usual', 'not the meaning'),
          ('A variable name', 'no'),
          ('An error message', 'no'),
          'A credential.'),
        Q('In this example, what is the security problem?', 'The key is written directly in the code',
          ('The variable is called API_KEY in capital letters, which Python does not allow', 'allowed'),
          ('The code prints a message', 'not the main problem'),
          ('Nothing; keys belong in code', 'they do not'),
          'Secrets should be stored separately.', ex=KEY_EX),
        Q('Where should secrets be stored?', 'Separately, such as in an environment variable',
          ('In a comment at the top of the code, where every programmer can find them quickly', 'still exposed'),
          ('In the file name', 'exposed'),
          ('In a chat with an AI tool', 'never'),
          'Outside shared code.'),
        Q('In this example, why is the query unsafe?',
          'Typed text goes straight into the query',
          ('The query is written in capital letters', 'not the risk'), ('It uses the input function', 'not by itself'),
          ('The table is called students', 'irrelevant'),
          'Attackers can change the query.',
          ex=SQL_EX),
        Q('Should you paste a real API key into an AI chat to get help?', 'No; never paste secrets into a chat',
          ('Yes, because chats with AI tools are completely private and are never stored anywhere', 'risky'),
          ('Yes, if it is short', 'no'),
          ('Only on weekends', 'no'),
          'Keep secrets out.'),
    ]),
    B=[cs('Compare secrets in code with a house key under the doormat',
          'Leaving a house key under the doormat is convenient, but anyone who looks there can get in. Writing a '
          'password or API key directly in code is similar: anyone who sees the code, or a copy of it, can use the '
          'key. Keeping the key in your pocket, separate from the house, is like storing secrets outside the code. '
          'And if the key might have been copied, you change the lock rather than just moving the key.', [
              Q('Why is a key under the doormat risky?', 'Anyone who looks can find it',
                ('Because doormats damage keys over time, making them stop working in the lock', 'not the reason'),
                ('Because keys are heavy', 'no'), ('Because doors are locked', 'no'),
                'Easy to find.'),
              Q('A secret written in code is like what?', 'A key under the doormat',
                ('A key kept safely in your pocket, separate from the house and away from strangers', 'opposite'),
                ('A locked safe', 'no'), ('A doorbell', 'no'),
                'Exposed to anyone who looks.'),
              Q('Keeping the key in your pocket is like what?',
          'Storing secrets outside the code',
          ('Writing the secret into a comment', 'still exposed'), ('Posting it online', 'no'),
          ('Giving it away', 'no'),
          'Separate storage.'),
              Q('If the key may have been copied, what should you do?', 'Change the lock',
                ('Move the key to a different doormat, since moving it is just as good as changing the lock', 'still copied'),
                ('Ignore it', 'risky'), ('Paint the door', 'no'),
                'Like rotating a secret.'),
              Q('In code, "changing the lock" means what?', 'Replacing the exposed secret with a new one',
                ('Deleting the line with the secret from the newest version of the code only', 'not enough'),
                ('Renaming the variable', 'not enough'), ('Adding a comment', 'no'),
                'Rotate the key.'),
          ], why='A learner who does not see why secrets in code are risky can compare them with a key under the '
                 'doormat.')],
    F1=sec('Handle secrets and input safely in practice', SECRETS, [
        Q('Mia shares her project online and realizes her real API key is in the code. What should she do first?',
          'Change the key at the service right away',
          ('Delete the key from the code and assume the problem is solved, since nobody saw it yet', 'may be copied'),
          ('Make the repository bigger', 'irrelevant'),
          ('Ignore it', 'risky'),
          'Rotate exposed secrets.'),
        Q('A tool asks you to paste your password so it can "test the login code." What should you do?', 'Refuse; use a fake test password',
          ('Paste it, because tools need the real password to check whether the login code works', 'never needed'),
          ('Paste half of it', 'still risky'),
          ('Email it instead', 'still risky'),
          'Use fake test values.'),
        Q('Which line handles a secret more safely?', 'Reading the key from an environment variable',
          ('Writing the key in a comment next to the code that uses it, so it is easy to update', 'exposed'),
          ('Printing the key at startup', 'exposed'),
          ('Saving the key in the file name', 'exposed'),
          'Kept outside the code.'),
        Q("A form's code builds a database query by adding typed text. What is the risk?",
          'An attacker can change the query',
          ('The query will run more slowly', 'not the risk'), ('The text will be misspelled', 'not the risk'),
          ('Nothing', 'it is a risk'),
          'Unsafe input.'),
        Q('Generated code contains "API_KEY = \'your-key-here\'." What is the safe next step?', 'Load the real key from a private setting',
          ('Replace the placeholder text with your real key in the same spot and share the file', 'exposes it'),
          ('Delete the line', 'code may fail'),
          ('Share the placeholder', 'not the issue'),
          'Keep real keys out of code.'),
    ]),
    F2=sec('Respond to exposed secrets and untrusted input', SECRETS_F2, [
        Q('Why is deleting an exposed key from the code not enough?', 'It may already have been copied',
          ('Because deleting lines of code in a file is impossible once the file has been shared', 'possible'),
          ('Because keys grow back', 'no'),
          ('Because code cannot be edited', 'no'),
          'Rotate the key.'),
        Q('What does "rotate a secret" mean?', 'Replace it with a new one at the service',
          ('Move the secret to a different line of the same code file so it is harder to find', 'still exposed'),
          ('Write it backward', 'no'),
          ('Encrypt the file name', 'no'),
          'Issue a new secret.'),
        Q('What do parameterized queries do?', 'Keep user text separate from the command',
          ('Make the database query run on a schedule every hour without any user input at all', 'not the meaning'),
          ('Remove the database', 'no'),
          ('Print the query', 'no'),
          'Safe input handling.'),
        Q('How should code treat what a user types?',
          'As untrusted',
          ('As fully trusted', 'risky'), ('As a secret', 'no'),
          ('As a comment', 'no'),
          'Untrusted input.'),
        Q('A tutorial\'s generated code prints the API key at startup "for debugging." What is the risk?', 'The key can appear in logs or screenshots',
          ('No risk, since printed text disappears from the screen as soon as the program finishes', 'logs keep it'),
          ('The program runs slower', 'minor'),
          ('The key gets longer', 'no'),
          'Do not print secrets.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CODE.10
MAINT = ('Code is usually read and changed far more often than it is written. Generated code you cannot explain '
         'becomes a problem when it breaks or needs a change. Keep code MAINTAINABLE: clear NAMES (total_price, not '
         'x2), short FUNCTIONS that each do one thing, COMMENTS that explain why, and a README (a document explaining '
         'what the project does and how to run it). Every piece of code in use should have an OWNER: a person who '
         'understands it and is responsible for fixing it. If no one can explain how it works, it is not ready to '
         'rely on.')
MAINT_F2 = ('Maintenance problems build up quietly. "Magic numbers" such as 0.0825 with no explanation leave the next '
            'person guessing (is it a tax rate?). Duplicated code means a fix in one place is missed in another. '
            'When a tool generates a large solution, ask for a simpler version, add tests that describe how it should '
            'behave, and write down any decisions. When the owner leaves a team or class, hand over the knowledge, '
            'not just the files.')

NAMES_EX = CODE('''
def f(a, b):
    return a * b * 1.0825

def price_with_tax(subtotal, quantity):
    TAX_RATE = 0.0825  # local sales tax
    return subtotal * quantity * (1 + TAX_RATE)

print(round(f(10, 2), 2), round(price_with_tax(10, 2), 2))
''', out='21.65 21.65')

S_CODE10 = SET(
    'AI.CODE.10',
    M=sec('Keep generated code understandable, documented and owned', MAINT, [
        Q('Is code read or written more often?', 'Read and changed more often',
          ('Written more often, because each line of code is written many times and read only once', 'reversed'),
          ('Neither', 'it is read'), ('Only written', 'no'),
          'Maintenance dominates.'),
        Q('In this example, which function is easier to maintain?', 'price_with_tax',
          ('f, because short names like f, a and b are faster to type and always easier to understand', 'unclear'),
          ('Both equally', 'one is clearer'),
          ('Neither', 'one is clearer'),
          'Clear names and an explained rate.', ex=NAMES_EX),
        Q('In the same example, do both functions give the same result?', 'Yes, 21.65',
          ('No, because functions with different names always calculate different results', 'same math'),
          ('No; f gives 20', 'it gives 21.65'),
          ('No; one crashes', 'both run'),
          'Same math, different clarity.', calc=lambda: round(10 * 2 * 1.0825, 2) == 21.65, ex=NAMES_EX),
        Q('What is a README?', 'A document explaining what a project does and how to run it',
          ('A file that the computer reads before every program to make the program run faster', 'not the meaning'),
          ('An error log', 'no'),
          ('A password file', 'no'),
          'Project documentation.'),
        Q('Who should own a piece of code in use?', 'A person who understands it and fixes it',
          ('The AI tool that wrote it, which will maintain and fix it forever without any help', 'tools are not owners'),
          ('Nobody', 'needs an owner'),
          ('Whoever used it last', 'not responsible'),
          'Clear responsibility.'),
    ]),
    B=[cs('Compare maintainable code with a well-labeled kitchen',
          'In a shared kitchen with LABELED jars ("sugar," "salt"), anyone can cook. In a kitchen of unlabeled jars, '
          'only the person who filled them knows which is which, and when they are away, someone puts salt in the cake. '
          'Code works the same way: clear names and comments are labels. A README is the note on the fridge explaining '
          'how things work. The OWNER is the person who restocks and keeps it organized.', [
              Q('Labeled jars are like what in code?',
          'Clear names and comments',
          ('Very short names like x and y', 'unclear'), ('Error messages', 'no'),
          ('Passwords', 'no'),
          'Labels help others.'),
              Q('Unlabeled jars cause what problem?', 'Only one person knows what is what',
                ('Everyone in the kitchen always knows exactly what is in every jar without looking', 'opposite'),
                ('Jars break', 'no'), ('Food is cheaper', 'no'),
                'Hidden knowledge.'),
              Q('The note on the fridge is like what?', 'A README',
                ('A commit message that explains a single change made to one line of the code', 'not the comparison'),
                ('A bug', 'no'), ('A test', 'no'),
                'How things work.'),
              Q('The person who keeps the kitchen organized is like what?', 'The code\'s owner',
                ('The AI tool that generated the recipe ideas for the meals cooked in the kitchen', 'not the owner'),
                ('A guest', 'no'), ('The fridge', 'no'),
                'Responsibility.'),
              Q('Salt in the cake is like what in code?', 'A mistake caused by unclear code',
                ('A successful new feature that customers asked for and that works exactly as planned', 'opposite'),
                ('A faster program', 'no'), ('A new commit', 'no'),
                'Confusion leads to errors.'),
          ], why='A learner who sees no value in clear code can compare it with a labeled shared kitchen.')],
    F1=sec('Keep generated code maintainable in practice', MAINT, [
        Q('A club uses a generated script to track dues, but nobody can explain how it works. What is the risk?',
          'No one can fix it when it breaks',
          ('No risk, because generated scripts never break and never need to be changed by anyone', 'they can'),
          ('It will run too fast', 'not the risk'),
          ('It uses too little memory', 'not the risk'),
          'Unowned code is fragile.'),
        Q('Which variable name is clearest?', 'total_price',
          ('x2, because short names save typing time and every programmer knows what x2 means', 'unclear'),
          ('tp', 'unclear'),
          ('thing', 'unclear'),
          'Says what it holds.'),
        Q('A generated function does five different jobs. What improves it?',
          'Splitting it into smaller functions',
          ('Adding a sixth job to the same function', 'worse'), ('Removing all comments', 'worse'),
          ('Renaming it to "do_all"', 'not a fix'),
          'One job per function.'),
        Q('Which comment is most useful?', '"# Round down because the store never charges partial cents"',
          ('"# This line of code does something," which reminds readers that the line is important', 'uninformative'),
          ('"# code"', 'uninformative'),
          ('"# hi"', 'uninformative'),
          'Explains why.'),
        Q('Before relying on generated code at work, what should be true?',
          'Someone can explain how it works',
          ('It should be long', 'not a sign'), ('It should have no comments', 'no'),
          ('It should be secret', 'no'),
          'Understanding first.'),
    ]),
    F2=sec('Prevent quiet maintenance problems', MAINT_F2, [
        Q('Code contains 0.0825 with no explanation. What is this called?',
          'A magic number',
          ('A secret key', 'not a key'), ('A comment', 'no'),
          ('A test', 'no'),
          'Unexplained value.'),
        Q('The same calculation is copied in three places. What problem follows?', 'A fix in one place may be missed in others',
          ('Nothing, because copied code always gets updated in every place at the same time', 'it does not'),
          ('The program runs faster', 'not the point'),
          ('It is easier to read', 'not usually'),
          'Duplication risk.'),
        Q('A tool generates a 300-line solution for a simple task. What should you ask for?', 'A simpler version',
          ('An even longer version with more features, so it is ready for any future need', 'harder to maintain'),
          ('Nothing; use it', 'hard to maintain'),
          ('A version without tests', 'worse'),
          'Simpler is easier to own.'),
        Q('The student who built the class website is graduating. What should happen?', 'Hand over knowledge, not just files',
          ('Nothing, since the files contain everything anyone will ever need to maintain the website', 'not enough'),
          ('Delete the website', 'unnecessary'),
          ('Change the password and tell no one', 'loses access'),
          'Transfer understanding.'),
        Q('Why add tests to generated code you will keep?', 'They describe and protect how it should behave',
          ('Because tests make the code shorter and remove the need for any comments or README', 'not the point'),
          ('To slow it down', 'no'),
          ('To hide bugs', 'no'),
          'Tests document behavior.'),
    ]),
)

SETS = [S_CODE01, S_CODE02, S_CODE03, S_CODE04, S_CODE05, S_CODE06, S_CODE07, S_CODE08, S_CODE09, S_CODE10]
