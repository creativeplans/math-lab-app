"""Entrepreneurship sets 57-62: Foundation 8, bookkeeping basics. Numbers are practice assumptions."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 57: why bookkeeping and receipts matter
WHY = ('BOOKKEEPING is recording every money event in the business: sales, expenses, owner transfers and loans. Each '
       'record should show the date, amount, who it was with, and what it was for. A RECEIPT or invoice is the proof. '
       'Good records let you see whether you are making money, prepare taxes, answer questions from a tax agency, '
       'apply for loans, and catch mistakes or theft. Record transactions soon after they happen; trying to rebuild a '
       'year of records from memory is slow and unreliable.')

s57 = SET('ENT.BOOK.01',
    M=sec('Explain why records and receipts matter and what each record needs', WHY, [
        Q('What is bookkeeping?', 'Recording every money event in the business',
          ('Designing the shelves where the business keeps its books', 'a pun, not the meaning'),
          ('Choosing which products to put on sale each week', 'that is merchandising'),
          ('Writing a business plan for investors once a year', 'that is planning'), 'Bookkeeping records money events.'),
        Q('Which detail belongs on every record?', 'The date, amount, other party and purpose',
          ('The weather and the owner\'s mood on that day', 'not needed'),
          ('Only the amount, rounded to the nearest hundred', 'incomplete'),
          ('Only the customer\'s favorite product', 'not needed'), 'Each record needs these details.'),
        Q('What does a receipt do?', 'Proves a transaction happened',
          ('Replaces the need to record the transaction at all', 'still record it'),
          ('Guarantees the expense will be tax deductible', 'not guaranteed'),
          ('Shows how many followers the business has online', 'unrelated'), 'Receipts are proof.'),
        Q('Which is a reason to keep good records?', 'To see whether the business makes money',
          ('To make the office look more organized to visitors', 'not the main reason'),
          ('Because records automatically lower all prices', 'not true'),
          ('Because records replace the need for a bank account', 'not true'), 'Records show results.'),
        Q('When is the best time to record a transaction?', 'Soon after it happens',
          ('Once a year, from memory, just before taxes are due', 'unreliable'),
          ('Only when a tax agency asks a question about it', 'too late'),
          ('Never, if the amount is under 100 dollars', 'small amounts add up'), 'Prompt records are accurate.'),
    ]),
    B=[cs('A diary for money', 'Bookkeeping is like keeping a diary, but only about money. Each entry says when, how much, '
          'with whom, and why: "May 3, paid 42 dollars to Paper Plus for boxes." A receipt is like a photo that proves '
          'the diary entry is true. If you skip the diary for months, you will not remember what each payment was for, '
          'and nobody can check your story.', [
        Q('Bookkeeping is like a diary about what?', 'Money', ('Weather', 'not money'), ('Sports scores', 'not money'),
          ('Favorite songs', 'not money'), 'A money diary.'),
        Q('A receipt is like what in the diary picture?', 'A photo that proves the entry', ('A blank page in the diary', 'no proof'),
          ('A torn page', 'not proof'), ('A pen', 'a tool, not proof'), 'Receipts prove entries.'),
        Q('Which is a complete entry?', '"May 3, paid 42 dollars to Paper Plus for boxes"', ('"Spent some money at a store this week on things"', 'missing details'),
          ('"Boxes"', 'missing details'), ('"42"', 'missing details'), 'When, how much, with whom, why.'),
        Q('What happens if the diary is skipped for months?', 'You forget what payments were for', ('Your money doubles by itself', 'no'),
          ('Taxes disappear', 'no'), ('Nothing changes at all', 'memory fades'), 'Records must be timely.'),
        Q('Why can someone else check a diary with photos?', 'The photos are proof', ('Photos are pretty', 'not the reason'),
          ('Photos replace numbers', 'they support numbers'), ('Photos hide mistakes', 'opposite'), 'Proof allows checking.'),
    ], why='A learner who misses MAIN may not see what a record must contain; a money diary with photos makes it concrete.')],
    F1=sec('Apply it: improve a record-keeping habit', WHY, [
        Q('Sam writes "supplies 85" on a sticky note with no date or store. What should he add?', 'The date, store and what was bought',
          ('A smiley face to show it was a good purchase', 'not useful'),
          ('Nothing, because the amount is enough by itself', 'incomplete'),
          ('The total of all his personal spending this month', 'not this record'), 'Complete records need details.'),
        Q('A seller keeps receipts in a shoebox but records nothing for a year. What is the main problem?', 'Rebuilding the records will be slow and error-prone',
          ('Shoeboxes are illegal for storing receipts', 'not illegal'),
          ('Receipts expire after one month and become invalid', 'not true'),
          ('There is no problem as long as the receipts exist', 'records are still missing'), 'Prompt recording is better.'),
        Q('Monthly records show sales of 3,400 dollars and expenses of 3,650 dollars. What do they reveal?', 'A loss of 250 dollars',
          ('A profit of 250 dollars for the month', 'wrong sign'), ('A profit of 7,050 dollars for the month', 'added'),
          ('Nothing useful about the business at all', 'they reveal a loss'), '3,400 - 3,650 = -250.', calc=lambda: 3400 - 3650 == -250),
        Q('Which habit makes receipts easier to keep?', 'Photographing each receipt the day you get it',
          ('Throwing receipts away once the item is used up', 'loses proof'),
          ('Keeping receipts only for purchases over 1,000 dollars', 'loses many'),
          ('Asking stores never to give receipts at all', 'loses proof'), 'Same-day photos protect records.'),
        Q('A lender asks for a year of income records. Which owner is ready?', 'One with monthly records and receipts',
          ('One who remembers roughly what she earned last year', 'not proof'),
          ('One with only a bank card and no statements', 'incomplete'),
          ('One who kept records only for the first month', 'incomplete'), 'Complete records support applications.'),
    ]),
    F2=sec('Handle the complications: missing proof and messy records', WHY, [
        Q('A receipt for a 60-dollar business purchase is lost. What is a sensible step?', 'Use the bank or card statement and note what it was for',
          ('Make up a new receipt that looks like the old one', 'false record'),
          ('Delete the purchase from the records entirely', 'records become wrong'),
          ('Record it as twice the amount to be safe', 'false record'), 'Statements can support the record.'),
        Q('An owner finds cash sales missing from records because they were never written down. What fix helps most?',
          'Record every cash sale at the time with a simple log', ('Stop accepting cash from any customers', 'not necessary'),
          ('Guess the total of cash sales at the end of each year', 'unreliable'), ('Only record card sales from now on', 'still missing cash'),
          'Cash needs its own same-day record.'),
        Q('Records show 12 payments to an unknown vendor. What might that reveal?', 'An error or possible fraud to investigate',
          ('Nothing; unknown vendors are always fine to ignore', 'risky'),
          ('A guaranteed tax refund for the business', 'not related'),
          ('That the bank account should be closed today', 'too early'), 'Records help catch problems.'),
        Q('A tax agency asks about a deduction from two years ago. What helps the owner answer?', 'Kept receipts and records for that year',
          ('A memory of roughly how much she spent', 'not proof'), ('A screenshot of a competitor\'s website', 'unrelated'),
          ('A new receipt printed today for that year', 'not genuine'), 'Kept records support answers.'),
        Q('Which statement is accurate?', 'Good records are proof; memory alone is not.',
          ('Records are only needed by large companies with staff.', 'all need them'),
          ('Receipts are only useful on the day of purchase.', 'they matter later'),
          ('Bookkeeping means only counting cash once a year.', 'too narrow'), 'Records make claims checkable.'),
    ]))

# ------------------------------------------------------------------ Set 58: categorizing and a simple ledger
LEDGER = ('A LEDGER is a list of every transaction with columns such as date, description, category, money in and money '
          'out. CATEGORIES group similar items: sales, supplies, shipping, rent, advertising, software, owner draws. '
          'Consistent categories let you total each type and spot trends, such as shipping costs rising. A spreadsheet '
          'or simple bookkeeping software works. Example running balance: start 500, sale +200 = 700, supplies -80 = '
          '620.')

s58 = SET('ENT.BOOK.02',
    M=sec('Keep a simple categorized ledger and running balance', LEDGER, [
        Q('What is a ledger?', 'A list of every transaction with columns',
          ('A legal agreement among the owners of an LLC', 'that is an operating agreement'),
          ('A promotional flyer that lists product prices', 'not a ledger'),
          ('A bank\'s yearly report on interest rates', 'not a ledger'), 'A ledger records transactions.'),
        Q('Which category fits "paid 35 dollars for postage on orders"?', 'Shipping',
          ('Owner draws taken from profits', 'not shipping'), ('Sales from customers', 'money out, not in'),
          ('Rent for the workspace', 'not rent'), 'Postage on orders is shipping.'),
        Q('Start 500, a sale of 200, supplies of 80. What is the balance?', '620',
          ('780', 'added both'), ('380', 'subtracted both'), ('220', 'subtracted from the sale'),
          '500 + 200 - 80 = 620.', calc=lambda: 500 + 200 - 80 == 620),
        Q('Why use consistent categories?', 'To total each type and spot trends',
          ('To make the ledger look longer and more impressive', 'not the purpose'),
          ('Because each transaction needs a brand-new category', 'opposite'),
          ('To avoid writing the amount of each transaction', 'amounts still needed'), 'Consistency enables totals.'),
        Q('Which tool can hold a simple ledger?', 'A spreadsheet', ('A paper coffee cup', 'not a record tool'),
          ('A product photo', 'not a record tool'), ('A billboard', 'not a record tool'), 'Spreadsheets or software work.'),
    ]),
    B=[mathb('Keeping a running balance', 'A running balance adds money in and subtracts money out, one line at a time. '
             'Start with the opening amount. For each line: if money comes in, add; if money goes out, subtract. Example: '
             'start 300; +150 = 450; -60 = 390; -40 = 350. Check: opening + total in - total out = 300 + 150 - 100 = 350. Both ways should agree.', [
        Q('Start 200, then +50. What is the balance?', '250', ('150', 'subtracted'), ('200', 'not changed'),
          ('50', 'only the change'), '200 + 50 = 250.', calc=lambda: 200 + 50 == 250),
        Q('Start 250, then -70. What is the balance?', '180', ('320', 'added'), ('170', 'arithmetic slip'), ('70', 'only the change'),
          '250 - 70 = 180.', calc=lambda: 250 - 70 == 180),
        Q('Start 100; +40; -25; +10. What is the balance?', '125', ('175', 'added all'), ('75', 'subtracted all'), ('115', 'missed +10'),
          '100 + 40 - 25 + 10 = 125.', calc=lambda: 100 + 40 - 25 + 10 == 125),
        Q('Opening 400, total in 300, total out 250. What is the closing balance?', '450', ('950', 'added all'),
          ('350', 'subtracted in'), ('50', 'only in minus out'), '400 + 300 - 250 = 450.', calc=lambda: 400 + 300 - 250 == 450),
        Q('Money spent on supplies is added or subtracted?', 'Subtracted', ('Added', 'it goes out'), ('Ignored completely', 'it counts'),
          ('Doubled', 'no'), 'Money out is subtracted.'),
    ], why='A learner who misses MAIN may lose track of a running balance; this practices adding and subtracting line by line.')],
    F1=sec('Apply it: record and total a week', LEDGER, [
        Q('A week: sales 120, 90, 150; supplies 45; shipping 30. What is the total of sales?', '360', ('285', 'subtracted costs'),
          ('435', 'added costs'), ('270', 'missed a sale'), '120 + 90 + 150 = 360.', calc=lambda: 120 + 90 + 150 == 360),
        Q('Same week. What is sales minus supplies and shipping?', '285', ('360', 'sales only'), ('75', 'costs only'),
          ('435', 'added'), '360 - 75 = 285.', calc=lambda: 360 - 45 - 30 == 285),
        Q('Which entry is categorized well?', '"Jun 4 | Ad on local site | Advertising | out 25"',
          ('"Stuff | 25" with no date or category given', 'incomplete'),
          ('"Jun 4 | Ad | Sales | in 25" for money paid out', 'wrong category and direction'),
          ('"Something online, maybe 25, maybe 30"', 'vague'), 'Complete and correct.'),
        Q('Shipping was 80 dollars in March and 140 dollars in April with the same sales. What does the category total reveal?',
          'Shipping costs rose and should be checked', ('Sales doubled in April', 'sales were the same'),
          ('Nothing; categories never reveal trends', 'they do'), ('Rent was paid twice', 'not shown'),
          'Category totals show trends.', calc=lambda: 140 > 80),
        Q('A payment to the owner\'s personal account is categorized as "supplies." What is wrong?', 'It should be categorized as an owner draw',
          ('Nothing, because all money out is supplies', 'wrong category'),
          ('It should be categorized as sales revenue', 'money out, not revenue'),
          ('It should be deleted from the ledger', 'it happened'), 'Use the right category.'),
    ]),
    F2=sec('Handle the complications: mixed and split transactions', LEDGER, [
        Q('One store receipt has 60 dollars of business supplies and 20 dollars of personal snacks paid on the business card. '
          'How should it be recorded?', 'Supplies 60 and an owner draw of 20', ('Supplies 80, since it was one receipt', 'mixes personal'),
          ('Ignore it, since it was a mixed purchase', 'records become wrong'), ('Sales 80, since the card was used', 'not sales'),
          'Split the transaction.', calc=lambda: 60 + 20 == 80),
        Q('An owner changes category names every month. What problem results?', 'Totals cannot be compared from month to month',
          ('The ledger becomes more accurate each month', 'less comparable'), ('Taxes are automatically reduced', 'no'),
          ('Nothing; names never matter', 'they matter'), 'Consistency matters.'),
        Q('The ledger balance is 1,240 but the bank shows 1,190, and a 50-dollar fee is missing from the ledger. What should '
          'happen?', 'Add the 50-dollar fee to the ledger', ('Change the bank balance to match the ledger', 'cannot'),
          ('Ignore the 50-dollar difference forever', 'records wrong'), ('Delete a sale worth 50 dollars', 'false'),
          '1,240 - 50 = 1,190.', calc=lambda: 1240 - 50 == 1190),
        Q('A refund to a customer of 30 dollars is recorded as a new sale of 30 dollars. What is the effect?', 'Sales are overstated by 60 dollars',
          ('Sales are overstated by 30 dollars only', 'counted both ways'), ('Sales are understated by 30 dollars', 'wrong direction'),
          ('There is no effect on sales', 'there is'), 'It should be -30; recording +30 is off by 60.', calc=lambda: 30 - (-30) == 60),
        Q('Which statement is accurate?', 'Clear, consistent categories make records useful.',
          ('Any random category is fine as long as amounts are right.', 'categories matter'),
          ('Ledgers are needed only for businesses with employees.', 'all benefit'),
          ('A ledger replaces the need for receipts.', 'both needed'), 'Categories turn data into information.'),
    ]))

# ------------------------------------------------------------------ Set 59: invoices, bills, receivables, payables
AR = ('An INVOICE is a bill YOU send to a customer; until it is paid, it is money owed TO you, called ACCOUNTS RECEIVABLE. '
      'A BILL from a supplier is money YOU owe, called ACCOUNTS PAYABLE. A good invoice shows your business name, the '
      'customer, an invoice number, the date, what was provided, the amount, the due date and how to pay. Track both '
      'lists: who owes you, and whom you owe, with due dates. Paying bills on time protects your reputation with '
      'suppliers.')

s59 = SET('ENT.BOOK.03',
    M=sec('Track invoices and bills as receivables and payables', AR, [
        Q('Money customers owe you is called what?', 'Accounts receivable', ('Accounts payable owed to suppliers', 'money you owe'),
          ('Owner contributions to the business', 'not owed by customers'), ('Retained cash in savings', 'not owed'),
          'Receivables are owed to you.'),
        Q('A supplier\'s bill you have not paid yet is what?', 'Accounts payable', ('Accounts receivable from customers', 'owed to you'),
          ('Revenue earned from sales', 'not a bill'), ('An owner draw from profits', 'not a bill'), 'Payables are what you owe.'),
        Q('Which item should appear on an invoice?', 'An invoice number and due date',
          ('The owner\'s personal bank password', 'never share'), ('A list of the owner\'s other customers', 'private'),
          ('The supplier\'s cost for the materials', 'not needed'), 'Numbers and dates help tracking.'),
        Q('Receivables total 2,400 dollars and payables total 1,100 dollars. What is the difference?', '1,300 dollars',
          ('3,500 dollars', 'added'), ('1,100 dollars', 'payables only'), ('2,400 dollars', 'receivables only'),
          '2,400 - 1,100 = 1,300.', calc=lambda: 2400 - 1100 == 1300),
        Q('Why pay supplier bills on time?', 'It protects your reputation with suppliers',
          ('It guarantees customers will pay you sooner', 'not linked'), ('It removes the need for any records', 'still record'),
          ('It doubles your sales the next month', 'not linked'), 'Reliability builds trust.'),
    ]),
    B=[cs('IOUs going two ways', 'An IOU is a note that says "I owe you." In a business, IOUs go two ways. When you finish a '
          'job and send an invoice, the customer holds an IOU to you: that is a receivable. When a supplier sends you a '
          'bill, you hold an IOU to them: that is a payable. Keeping two lists, "owed to me" and "I owe," stops both '
          'kinds from being forgotten.', [
        Q('A customer who has not paid your invoice holds an IOU to whom?', 'To you', ('To the supplier', 'no'),
          ('To the bank', 'no'), ('To nobody', 'they owe you'), 'It is a receivable.'),
        Q('A supplier bill means you owe whom?', 'The supplier', ('The customer', 'no'), ('Yourself', 'no'),
          ('The state', 'not this bill'), 'It is a payable.'),
        Q('"Owed to me" is which list?', 'Receivables', ('Payables', 'I owe'), ('Expenses for the month', 'not a list of owed money'),
          ('Draws', 'no'), 'Receivables are owed to you.'),
        Q('"I owe" is which list?', 'Payables', ('Receivables', 'owed to me'), ('Sales', 'no'), ('Assets', 'no'),
          'Payables are what you owe.'),
        Q('Why keep two lists?', 'So neither kind of IOU is forgotten', ('To confuse the owner', 'no'), ('To avoid paying', 'no'),
          ('Because keeping only one list is illegal', 'no'), 'Tracking both prevents misses.'),
    ], why='A learner who misses MAIN may confuse the two directions; IOUs going two ways make it clear.')],
    F1=sec('Apply it: manage the two lists', AR, [
        Q('Invoice 104 for 600 dollars was paid; invoice 105 for 450 dollars is unpaid; invoice 106 for 300 dollars is unpaid. '
          'What are receivables?', '750 dollars', ('1,350 dollars', 'included the paid one'), ('600 dollars', 'the paid one'),
          ('300 dollars', 'only one'), '450 + 300 = 750.', calc=lambda: 450 + 300 == 750),
        Q('A supplier bill of 400 dollars is due in 5 days. Cash is 300 dollars and a 500-dollar receivable is due in 10 days. '
          'What is the best action?', 'Ask the supplier about timing before the due date', ('Ignore the bill and say nothing', 'harms trust'),
          ('Pay 300 dollars and claim it was full payment', 'dishonest'), ('Cancel the customer invoice', 'loses money'),
          'Early communication helps.', calc=lambda: 300 < 400),
        Q('Which invoice is missing something important?', 'One with no due date or payment method',
          ('One with a number, date, items, amount, due date and method', 'complete'),
          ('One showing the customer and business names and an amount and due date', 'mostly complete'),
          ('One listing the work, total and how to pay by a due date', 'mostly complete'), 'Due date and method are key.'),
        Q('A business owes three bills: 120, 85 and 240 dollars. What are payables?', '445 dollars', ('325 dollars', 'missed one'),
          ('360 dollars', 'missed one'), ('205 dollars', 'missed one'), '120 + 85 + 240 = 445.', calc=lambda: 120 + 85 + 240 == 445),
        Q('Why number invoices in order?', 'To track each one and spot missing invoices', ('To make each invoice look official only', 'not the main reason'),
          ('Because customers prefer large numbers on bills', 'not the reason'), ('To change the amount owed later', 'not allowed'),
          'Numbering supports tracking.'),
    ]),
    F2=sec('Handle the complications: disputes and duplicates', AR, [
        Q('A customer says an invoice was never received. What should the owner do?', 'Resend it and confirm the correct address',
          ('Double the amount as a penalty right away', 'unfair'), ('Write it off without asking anything', 'loses money'),
          ('Send the same invoice to all customers', 'wrong'), 'Resending is the simple fix.'),
        Q('An owner paid the same supplier bill twice. What should she do?', 'Ask the supplier for a refund or credit',
          ('Ignore it because the supplier will notice', 'may not'), ('Stop buying from that supplier forever', 'overreaction'),
          ('Record it as a sale', 'not a sale'), 'Recover the duplicate payment.'),
        Q('A customer disputes part of an invoice: 200 of 1,000 dollars. What is undisputed?', '800 dollars', ('1,000 dollars', 'all'),
          ('200 dollars', 'disputed part'), ('1,200 dollars', 'added'), '1,000 - 200 = 800.', calc=lambda: 1000 - 200 == 800),
        Q('Receivables are large but cash is low. What does this suggest?', 'Collecting from customers is the priority',
          ('The business has no customers at all', 'not true'), ('Payables should be ignored', 'still owed'),
          ('Prices should be cut immediately', 'not the issue'), 'Collection brings in cash.'),
        Q('Which statement is accurate?', 'Receivables are money not yet in hand.',
          ('Receivables can be spent today like cash.', 'not cash yet'), ('Payables are money customers owe.', 'reversed'),
          ('Invoices are optional for all businesses.', 'needed'), 'Owed money is not cash.'),
    ]))

# ------------------------------------------------------------------ Set 60: owner money in the books
EQUITY = ('In the books, owner money is kept separate from income and expenses. An OWNER CONTRIBUTION increases the '
          'owner\'s stake (called owner\'s equity) but is NOT sales revenue. An OWNER DRAW decreases owner\'s equity but '
          'is NOT a business expense for a sole proprietor or most LLCs. A LOAN from the owner is recorded as money the '
          'business owes back. Mislabeling these makes profit look wrong: a contribution recorded as a sale inflates '
          'profit; a draw recorded as an expense hides it.')

s60 = SET('ENT.BOOK.04',
    M=sec('Record owner contributions, draws and loans without distorting profit', EQUITY, [
        Q('An owner puts 1,000 dollars into the business. Is it sales revenue?', 'No, it is an owner contribution',
          ('Yes, it counts as sales for that month', 'not from customers'),
          ('Yes, but only if it is spent the same day', 'still not sales'),
          ('No, it is a business expense instead', 'not an expense'), 'Contributions are equity, not revenue.'),
        Q('What does an owner draw do to owner\'s equity?', 'Decreases it', ('Increases it each time', 'opposite'),
          ('Leaves it exactly unchanged', 'it decreases'), ('Turns it into revenue', 'not revenue'), 'Draws reduce equity.'),
        Q('If a 1,000-dollar contribution is recorded as a sale, what happens to profit?', 'It looks 1,000 dollars too high',
          ('It looks 1,000 dollars too low', 'wrong direction'), ('It looks exactly right', 'distorted'),
          ('It looks 2,000 dollars too high', 'counted once'), 'Mislabeling inflates profit.'),
        Q('How is a loan from the owner recorded?', 'As money the business owes back', ('As sales revenue for the month', 'not revenue'),
          ('As an owner draw from profits', 'opposite direction'), ('As a supply expense', 'not an expense'),
          'Loans are liabilities.'),
        Q('A draw recorded as an expense does what to profit?', 'Makes it look too low', ('Makes it look too high', 'opposite'),
          ('Has no effect on profit at all', 'it lowers profit'), ('Doubles it', 'no'), 'Expenses reduce profit.'),
    ]),
    B=[cs('Money moving in the family versus money from customers', 'Picture a family bakery. When Grandma lends the bakery money, '
          'that is family money moving in, not a cake sale. When the baker takes money home, that is family money moving '
          'out, not the cost of flour. Only cake sales are revenue, and only business costs like flour are expenses. '
          'Mixing family moves with sales and costs gives a false picture of how the bakery is doing.', [
        Q('Grandma\'s loan to the bakery is what?', 'Family money moving in, not a sale', ('A cake sale', 'not from customers'),
          ('A flour expense for the cakes', 'not a cost'), ('A tax', 'no'), 'It is not revenue.'),
        Q('The baker taking money home is what?', 'Family money moving out, not an expense', ('The cost of flour for the week\'s cakes', 'not a cost'),
          ('A cake sale', 'no'), ('A loan', 'not this'), 'It is a draw.'),
        Q('What counts as revenue?', 'Cake sales', ('Grandma\'s loan', 'no'), ('Money taken home', 'no'), ('A gift', 'no'),
          'Only customer sales.'),
        Q('What counts as an expense?', 'Flour for the cakes', ('Money taken home', 'draw'), ('Grandma\'s loan', 'liability'),
          ('Cake sales', 'revenue'), 'Business costs only.'),
        Q('Mixing family moves with sales gives what?', 'A false picture', ('A true picture', 'no'), ('More money', 'no'),
          ('Lower taxes', 'no'), 'Mislabeling distorts results.'),
    ], why='A learner who misses MAIN may treat owner money as income or costs; a family bakery separates them.')],
    F1=sec('Apply it: correct the labels', EQUITY, [
        Q('Records show sales of 5,000 dollars, including a 1,500-dollar owner contribution. Expenses are 3,000 dollars. What is '
          'the true profit?', '500 dollars', ('2,000 dollars', 'included contribution'), ('3,500 dollars', 'sales only'),
          ('1,500 dollars', 'contribution only'), '(5,000 - 1,500) - 3,000 = 500.', calc=lambda: (5000 - 1500) - 3000 == 500),
        Q('Expenses of 4,200 dollars include 1,200 dollars of owner draws. Sales are 6,000 dollars. What is the true profit for a '
          'sole proprietor?', '3,000 dollars', ('1,800 dollars', 'kept draws as expense'), ('6,000 dollars', 'sales only'),
          ('4,200 dollars', 'expenses only'), '6,000 - (4,200 - 1,200) = 3,000.', calc=lambda: 6000 - (4200 - 1200) == 3000),
        Q('An owner lends 2,000 dollars and the business repays 500 dollars. What does the business still owe her?', '1,500 dollars',
          ('2,500 dollars', 'added'), ('2,000 dollars', 'ignored repayment'), ('500 dollars', 'repaid amount'),
          '2,000 - 500 = 1,500.', calc=lambda: 2000 - 500 == 1500),
        Q('Which label fits "moved 300 dollars from my savings to buy a printer for the shop"?', 'Owner contribution',
          ('Sales revenue from customers', 'not sales'), ('Owner draw from profits', 'money in, not out'),
          ('Refund to a customer', 'not a refund'), 'Money in from the owner.'),
        Q('Why does correct labeling matter for a loan application?', 'Lenders look at true profit', ('Lenders ignore records', 'they review them'),
          ('Labels change the bank\'s interest rate directly', 'not directly'), ('Labels are only for taxes', 'also lending'),
          'Accurate profit supports applications.'),
    ]),
    F2=sec('Handle the complications: unclear transfers', EQUITY, [
        Q('An owner moved 800 dollars into the business without saying whether it was a loan or a contribution. What should '
          'she do?', 'Decide and document which it is', ('Record it as sales to be safe', 'wrong'), ('Leave it unlabeled forever', 'unclear'),
          ('Record it as an expense', 'wrong'), 'Documentation removes doubt.'),
        Q('Two partners contribute 1,000 and 3,000 dollars. They agreed contributions affect ownership. What share did the '
          'first partner contribute?', '25 percent', ('33 percent', 'used 1,000 / 3,000'), ('50 percent', 'equal split'),
          ('75 percent', 'reversed'), '1,000 / 4,000 = 0.25.', calc=lambda: 1000 / 4000 == 0.25),
        Q('A corporation pays its owner-employee a salary through payroll. How does this differ from a sole proprietor\'s draw?',
          'Salary through payroll is usually a business expense', ('It is exactly the same as a draw', 'structure matters'),
          ('Salaries are never allowed for owners of any business', 'they are for corporations'), ('It is recorded as sales', 'not sales'),
          'Structure changes the treatment; ask a tax professional.'),
        Q('Draws exceed profit for the year. What happens to owner\'s equity?', 'It goes down', ('It goes up', 'opposite'),
          ('It stays the same', 'it changes'), ('It becomes revenue', 'not revenue'), 'Taking more than profit reduces equity.'),
        Q('Which statement is accurate?', 'Owner money moves are recorded, but not as sales or (for draws) expenses.',
          ('Owner money never needs to be recorded at all, since it is the owner\'s own money.', 'must be recorded'),
          ('All owner money is revenue.', 'not revenue'), ('Draws are always deductible expenses.', 'not for sole props'),
          'Correct labels keep profit honest.'),
    ]))

# ------------------------------------------------------------------ Set 61: cash and accrual basics
BASIS = ('There are two common ways to record when income and expenses count. CASH BASIS records income when money is '
         'received and expenses when money is paid. ACCRUAL BASIS records income when it is earned (for example, when '
         'the work is done and invoiced) and expenses when they are incurred, even if payment happens later. Example: a '
         'job finished in December but paid in January counts as December income under accrual and January income under '
         'cash. Many small businesses start on cash basis; tax rules on which method may be used vary, so ask a tax '
         'professional.')

s61 = SET('ENT.BOOK.05',
    M=sec('Tell cash basis from accrual basis with a timing example', BASIS, [
        Q('Under cash basis, when is income recorded?', 'When money is received',
          ('When the customer first asks for a quote', 'too early'), ('When the work is advertised online', 'not income'),
          ('When the invoice is designed in software', 'not received'), 'Cash basis follows money in.'),
        Q('Under accrual basis, when is income recorded?', 'When it is earned', ('Only when cash arrives in the bank', 'that is cash'),
          ('Only at the end of each tax year', 'not the rule'), ('Only when the owner takes a draw', 'unrelated'),
          'Accrual follows earning.'),
        Q('Work done in December, paid in January. Under accrual, which month gets the income?', 'December',
          ('January', 'cash basis'), ('Both months equally', 'not split'), ('Neither month', 'it counts'), 'Earned in December.'),
        Q('Same job under cash basis: which month?', 'January', ('December', 'accrual'), ('Both months', 'not split'),
          ('Neither month', 'it counts'), 'Received in January.'),
        Q('Who should be asked about which method a business may use for taxes?', 'A tax professional',
          ('A customer who likes the products', 'not qualified'), ('A social media follower', 'not qualified'),
          ('The supplier of packaging', 'not qualified'), 'Tax method rules vary.'),
    ]),
    B=[cs('Counting when you hand in homework versus when it is graded', 'Imagine counting a homework assignment as "done" '
          'either when you finish it or when the teacher hands back the grade. Accrual is like counting it when you '
          'finish the work. Cash basis is like counting it when the grade (the money) comes back. The same assignment '
          'just lands on a different day depending on which rule you use.', [
        Q('Counting when you finish the work is like which basis?', 'Accrual', ('Cash', 'when payment arrives'),
          ('Neither', 'accrual'), ('Both', 'just one'), 'Accrual counts when earned.'),
        Q('Counting when the grade comes back is like which basis?', 'Cash', ('Accrual', 'when earned'), ('Neither', 'cash'),
          ('Both', 'just one'), 'Cash counts when money arrives.'),
        Q('Does the amount of work change between methods?', 'No, only the timing', ('Yes, it doubles', 'no'),
          ('Yes, it halves', 'no'), ('Yes, it disappears', 'no'), 'Only timing differs.'),
        Q('In the picture, the "grade coming back" stands for what?', 'Money received', ('Work finished', 'accrual'),
          ('A new assignment', 'no'), ('A late fee', 'no'), 'Cash basis waits for money.'),
        Q('Why might the same job land in different months?', 'The two methods use different moments', ('One is illegal', 'no'),
          ('The job changed', 'no'), ('Customers decide the month to use', 'no'), 'Different timing rules.'),
    ], why='A learner who misses MAIN may not see the timing difference; homework counted at two moments shows it.')],
    F1=sec('Apply it: place income and expenses in the right month', BASIS, [
        Q('A plumber finishes a 900-dollar job on March 28 and is paid April 5. Under cash basis, how much March income does '
          'this job add?', '0 dollars', ('900 dollars', 'accrual'), ('450 dollars', 'split'), ('5 dollars', 'confused date'),
          'Cash basis records April.', calc=lambda: 900 * 0 == 0),
        Q('A shop receives a 300-dollar supply bill in June and pays it in July. Under accrual, when is the expense?', 'June',
          ('July', 'cash basis'), ('August', 'neither'), ('Never', 'it counts'), 'Incurred in June.'),
        Q('In May, a consultant invoiced 4,000 dollars and was paid 2,500 dollars of it. Under cash basis, May income is?',
          '2,500 dollars', ('4,000 dollars', 'accrual'), ('1,500 dollars', 'unpaid part'), ('6,500 dollars', 'added'),
          'Only cash received counts.', calc=lambda: 2500 == 2500),
        Q('Same consultant under accrual: May income is?', '4,000 dollars', ('2,500 dollars', 'cash'), ('1,500 dollars', 'unpaid'),
          ('0 dollars', 'it was earned'), 'All earned work counts.'),
        Q('Which method shows more clearly how much work was done each month?', 'Accrual', ('Cash', 'follows payments'),
          ('Neither method', 'accrual does'), ('Both always match', 'not always'), 'Accrual matches income to work.'),
    ]),
    F2=sec('Handle the complications: switching and mixing methods', BASIS, [
        Q('An owner records some income when invoiced and some when paid. What is the problem?', 'Income may be counted twice or missed',
          ('Nothing; mixing methods is recommended', 'confusing'), ('Taxes are automatically lower', 'no'),
          ('It makes records more accurate', 'less'), 'Pick one method consistently.'),
        Q('Under cash basis, an owner prepays 12 months of insurance (1,200 dollars) in January. What does January show?', '1,200 dollars of expense',
          ('100 dollars of expense', 'accrual-style spreading'), ('0 dollars of expense', 'it was paid'),
          ('2,400 dollars of expense', 'doubled'), 'Cash basis records it when paid.'),
        Q('Under accrual, the same 1,200-dollar insurance covers 12 months. About how much is recorded as each month\'s '
          'expense?', '100 dollars', ('1,200 dollars', 'all at once'), ('12 dollars', 'moved decimal'), ('0 dollars', 'it is used'),
          '1,200 / 12 = 100.', calc=lambda: 1200 / 12 == 100),
        Q('A business wants to change its tax accounting method. What should it do first?', 'Ask a tax professional about the rules',
          ('Change it silently in the middle of the year', 'may cause problems'),
          ('Use both methods at once', 'confusing'), ('Ask a customer', 'not qualified'), 'Method changes can have rules.'),
        Q('Which statement is accurate?', 'Cash and accrual differ in timing, not in total amounts over time.',
          ('Accrual always shows more profit.', 'not always'), ('Cash basis is illegal for every kind of business to use.', 'not true'),
          ('Accrual ignores unpaid invoices.', 'it includes them'), 'Timing is the difference.'),
    ]))

# ------------------------------------------------------------------ Set 62: P&L, balance sheet, cash flow
FIN = ('Three common reports summarize the books. A PROFIT AND LOSS statement (P&L, or income statement) shows revenue, '
       'expenses and profit over a period, such as a month. A BALANCE SHEET shows, on one date, what the business owns '
       '(assets, like cash and equipment), what it owes (liabilities, like loans and unpaid bills), and the owner\'s '
       'equity: assets = liabilities + equity. A CASH FLOW statement shows where cash came from and went during a '
       'period. Each answers a different question.')

s62 = SET('ENT.BOOK.06',
    M=sec('Read the three basic reports and match each to its question', FIN, [
        Q('Which report shows profit over a month?', 'The profit and loss statement',
          ('The balance sheet on one date', 'snapshot, not profit'), ('The cash flow statement only', 'cash movement'),
          ('The supplier\'s price list', 'not a report'), 'The P&L shows profit.'),
        Q('Which report shows what the business owns and owes on one date?', 'The balance sheet',
          ('The profit and loss statement', 'over a period'), ('The cash flow statement', 'cash movement'),
          ('A marketing plan for the year', 'not a report'), 'The balance sheet is a snapshot.'),
        Q('Assets are 10,000 dollars and liabilities are 4,000 dollars. What is equity?', '6,000 dollars',
          ('14,000 dollars', 'added'), ('4,000 dollars', 'liabilities'), ('10,000 dollars', 'assets'), '10,000 - 4,000 = 6,000.',
          calc=lambda: 10000 - 4000 == 6000),
        Q('Which is a liability?', 'An unpaid bank loan', ('Cash in the business account', 'asset'), ('A delivery van owned', 'asset'),
          ('Inventory on shelves', 'asset'), 'Liabilities are amounts owed.'),
        Q('Which report best shows where cash came from and went?', 'The cash flow statement', ('The balance sheet', 'snapshot'),
          ('The profit and loss statement', 'profit, not cash'), ('A customer review page', 'not a report'),
          'Cash flow tracks cash movement.'),
    ]),
    B=[mathb('Using assets = liabilities + equity', 'The balance sheet equation is assets = liabilities + equity. If you know '
             'two of the numbers, you can find the third. To find equity: equity = assets - liabilities. To find assets: '
             'add liabilities and equity. Example: liabilities 3,000 and equity 5,000 means assets are 8,000. Check by '
             'adding back: if equity = assets - liabilities, then liabilities + equity must equal the assets you started with.', [
        Q('Liabilities 2,000, equity 7,000. What are assets?', '9,000', ('5,000', 'subtracted'), ('2,000', 'liabilities'),
          ('7,000', 'equity'), '2,000 + 7,000 = 9,000.', calc=lambda: 2000 + 7000 == 9000),
        Q('Assets 12,000, liabilities 5,000. What is equity?', '7,000', ('17,000', 'added'), ('5,000', 'liabilities'),
          ('12,000', 'assets'), '12,000 - 5,000 = 7,000.', calc=lambda: 12000 - 5000 == 7000),
        Q('Assets 6,000, equity 6,000. What are liabilities?', '0', ('12,000', 'added'), ('6,000', 'equity'), ('1', 'ratio'),
          '6,000 - 6,000 = 0.', calc=lambda: 6000 - 6000 == 0),
        Q('Which equation is correct?', 'Assets = liabilities + equity', ('Assets = liabilities - equity', 'wrong sign'),
          ('Equity = assets + liabilities', 'wrong'), ('Liabilities = assets + equity', 'wrong'), 'The basic equation.'),
        Q('Assets 4,500, liabilities 1,500. What is equity?', '3,000', ('6,000', 'added'), ('1,500', 'liabilities'),
          ('4,500', 'assets'), '4,500 - 1,500 = 3,000.', calc=lambda: 4500 - 1500 == 3000),
    ], why='A learner who misses MAIN may not rearrange the balance sheet equation; this practices it.')],
    F1=sec('Apply it: answer questions with the right report', FIN, [
        Q('An owner wants to know if March was profitable. Which report?', 'The March profit and loss statement',
          ('The balance sheet from last year', 'wrong period and type'), ('A list of customer names', 'not a report'),
          ('The supplier\'s catalog', 'not a report'), 'The P&L answers profitability.'),
        Q('A lender wants to know how much the business owes in total today. Which report?', 'The balance sheet',
          ('The profit and loss statement', 'period results'), ('A sales flyer', 'not a report'), ('A tax receipt', 'not a report'),
          'Liabilities appear on the balance sheet.'),
        Q('A P&L shows revenue 8,000 and expenses 6,500. What profit does it report?', '1,500 dollars', ('14,500 dollars', 'added'),
          ('6,500 dollars', 'expenses'), ('8,000 dollars', 'revenue'), '8,000 - 6,500 = 1,500.', calc=lambda: 8000 - 6500 == 1500),
        Q('Profit was 1,500 but cash fell by 700 because the owner bought equipment for 2,200. Which report shows this cash use '
          'clearly?', 'The cash flow statement', ('The profit and loss statement alone', 'misses equipment purchase'),
          ('A customer survey', 'not a report'), ('The logo guide', 'not a report'), 'Cash flow shows the purchase.',
          calc=lambda: 1500 - 2200 == -700),
        Q('A balance sheet shows cash 2,000, equipment 3,000, a loan of 1,500 and unpaid bills of 500. What is equity?', '3,000 dollars',
          ('5,000 dollars', 'assets only'), ('2,000 dollars', 'liabilities only'), ('7,000 dollars', 'added all'),
          '(2,000 + 3,000) - (1,500 + 500) = 3,000.', calc=lambda: (2000 + 3000) - (1500 + 500) == 3000),
    ]),
    F2=sec('Handle the complications: reports that seem to disagree', FIN, [
        Q('The P&L shows a profit, but the bank balance fell. What could explain it?', 'Cash was used for equipment, loan payments or draws',
          ('The P&L must be fake', 'not necessarily'), ('Profit and cash must always match', 'they can differ'),
          ('The bank made a mistake on every single statement', 'unlikely'), 'Different reports measure different things.'),
        Q('A balance sheet does not balance: assets 9,000, liabilities 3,000, equity 5,000. What is the gap?', '1,000 dollars',
          ('9,000 dollars', 'assets'), ('8,000 dollars', 'sum'), ('0 dollars', 'it does not balance'), '9,000 - 8,000 = 1,000.',
          calc=lambda: 9000 - (3000 + 5000) == 1000),
        Q('What should the owner do about that gap?', 'Look for a missing or mislabeled record', ('Add 1,000 dollars of fake equity', 'false'),
          ('Ignore it because reports never balance', 'they should'), ('Delete the balance sheet', 'not a fix'),
          'An imbalance signals an error.'),
        Q('An owner reads only the P&L and misses that a large loan is due next month. Which report would have shown the loan?',
          'The balance sheet', ('A marketing report', 'no'), ('The P&L alone', 'not liabilities'), ('A customer list', 'no'),
          'Liabilities are on the balance sheet.'),
        Q('Which statement is accurate?', 'Each report answers a different question, so review all three.',
          ('One report tells everything an owner needs to know about a business.', 'not true'), ('Reports are only for big companies.', 'all benefit'),
          ('Cash flow and profit are the same report.', 'different'), 'Use them together.'),
    ]))

SETS = [s57, s58, s59, s60, s61, s62]
