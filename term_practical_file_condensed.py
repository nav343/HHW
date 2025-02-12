import json
import calendar
import math
def q1():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    opt = int(input("""Choose the operation you want to execute: 
                    1. ADDITION
                    2. SUBTRACTION (DIFFERENCE)
                    3. MULTIPLICATION
                    4. DIVISION (1ST/2ND)
                    5. EXPONENTIATION (1ST^2ND)
                    6. REMAINDER (ON DIVISION OF 1ST BY 2ND)
                    (eg. for addition enter 1)\n"""))
    match opt:
        case 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        case 3:
            print(f"{num1} x {num2} = {num1 * num2}")
        case 4:
            print(f"{num1} / {num2} = {num1 / num2}")
        case 5:
            print(f"{num1} ^ {num2} = {num1 ** num2}")
        case 6:
            print(f"{num1} % {num2} = {num1 % num2}")
        case _:
            print(f"Please choose an option from the menu. The number {opt} does not correspond to any existing operation.")
def q2():
    nums = [int(input(f"Enter {x}{'st' if x == 1 else 'nd' if x == 2 else 'rd'}")) for x in range(1,4)]
    print(f"The largest number from {nums} is {max(nums)}")
def q3():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} == {num*i}")
def q4():
    num = int(input("Enter a number: "))
    sumOdd = num**2
    sumEven = num*(num + 1)
    print(f"The sum of first {num}\nOdd Natural Numbers = {sumOdd}\nEven Natural Numbers = {sumEven}")
def q5():
    numDays = int(input("Enter the number of total days: "))
    years = numDays//365
    addnMonths = (numDays%365)//30
    addnDays = numDays%365 - addnMonths*30
    print(f"{years} year(s), {addnMonths} month(s) and {addnDays} day(s)!!")
def q6():
    year = int(input("Enter a year: "))
    print(f"{year} is a {'' if year%4 == 0 else 'not'} leap year")
def q7():
    print("Welcome")
    choice = input("What do you want to calculate: (A/C)")
    radius = int(input("Enter the radius of the cicle: "))
    if choice.upper() == 'A':
        print(f"The area of the circle is {math.pi*radius**2}")
    elif choice.upper() == 'C':
        print(f"The circumference of the circle is {math.pi*radius*2}")
    else:
        print("Invalid choice")
def q8():
    num = input("Enter a number: ")
    print(f"{num} is a {'Palindrome' if num[::-1] == num else 'not Palindrome'}")
def q9():
    num = int(input("Enter a number: "))
    factors = []
    if num == 0 or num == 1:print(f"{num} is neither prime nor composite")
    else:
        for i in range(2, num+1):
            if num%i == 0:
                factors.append(i)
        print(f"{num} is a {'' if len(factors) == 1 else 'not'} prime number")
def q10():
    def F(n:int):
        if n == 0: return 0
        elif n == 1: return 1
        else: return F(n-1) + F(n-2)
    print(0)
    for i in range(1,21):
        print(F(i))

    """The smaller, efficient, easier way
    a = b = 1
    while(b <= 20):
        print(b, end = " ")
        a, b = b, a + b
    """
def q11():
    num = input("Enter an integer: ")
    try:
        int(num)
    except ValueError:
        print(f"{num} is not an integer")
        exit()
    print(f"Reversed number of {num} is {num[::-1]}")
def q12():
    num = int(input("Enter a number: "))
    n = num
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    for j in factors:
        count = factors.count(j)
        if count%2 != 0: 
            print(f"{num} is not a perfect square")
            break
    else: print(f"{num} is a perfect square")
def q13():
    num = input("Enter a number: ")
    sum = 0
    for i in range(0, len(num)): sum += int(num[i])**len(num)
    print(f"{num} is {'' if sum == int(num) else 'not'} an Armstrong number")
def q14():
    string = input("Enter a string: ")
    print("Your given string is a palindrome" if string[::-1] == string else "Your given string is not a palindrome")
def q15():
    string = input("Enter a string: ")
    print(string.title())
def q16():
    lst: list[int] = eval(input("Enter a list: "))
    num = int(input("Enter the number you want to search for: "))
    print(f"First occurrence of {num} in your string is at index -> {lst.index(num)}")
def q17():
    string = input("Enter your string: ")
    db = {i:string.count(i) for i in string}
    print(json.dumps(db, indent=2))
def q18():
    string = input("Enter a string: ")
    upperCaseChar = 0
    for i in string:
        upperCaseChar += 1 if i.isupper() else 0
    print(f"Your string has {upperCaseChar} number of upper case characters")
def q19():
    string = input("Enter >> ")
    alpha = 'qwertyuioplkjhgfdsazxcvbnm'
    numbers = '0123456789'
    noAlpha, noNum, noEtc = 0,0,0
    for i in string:
        if i.lower() in alpha: noAlpha += 1
        elif i in numbers: noNum += 1
        else: noEtc += 1
    print(f"""Your string has:
          {noAlpha} alphabets,
          {noNum} numbers and 
          {noEtc} other characters.""")
def q20():
    string = input("Enter a string: ")
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1
    print(f"Your string has {count} vowels in it")
def p1():
    lst1 = [1,5,7,10,15,23,76]
    print(f"OLD LIST: {lst1}")
    for i in range(0, len(lst1)): lst1[i] += 10 if lst1[i]%2 != 0 else -10
    print(f"NEW LIST: {lst1}")
def p2():
    list1 = eval(input("Enter a list of numbers containing even number of terms only: "))
    try:
        for i in range(0,len(list1)):
            if i%2 == 0:
                prev = list1[i]
                list1[i] = list1[i + 1] 
                list1[i+1] = prev 
        print(list1)
    except Exception:
        print("Only EVEN number of terms are allowed in the list")
def p3():
    lst = eval(input("Enter a list of numbers: "))
    switch = 0
    for i in range(0,len(lst)):
        if switch == 1:
            switch = 0
            continue
        if (lst[i])%5 == 0:
            prev = lst[i]
            lst[i] = lst[i + 1]
            lst[i+1] = prev 
            switch = 1
    print(lst)
def p4():
    string = input("Enter your string: ")
    count = 0
    for i in string.split():
        count += 1 if i.lower() == 'the' else 0
    print(f"Your sentence has {count} 'the's")
def p5():
    listB = ['AP', 'MP', 'UP', 'CG']
    pos = -1
    for i in listB:
        if i == 'CG': pos = listB.index(i) + 1 # assuming counting index starts from 1 and not from 0
    print(f"CG found at {pos}{'st' if pos == 1 else 'nd' if pos == 2 else 'rd' if pos == 3 else 'th'} index" if pos != -1 else "CG not found in your list")
def p6():
    marks = eval(input("Enter the marks of your students: "))
    print(f"Maximum marks scored was: {max(marks)}")
    print(f"Minimum marks scored was: {min(marks)}")
def p7():
    marks = eval(input("Enter the marks of your students: "))
    toppers = 0
    for i in marks: toppers += 1 if i > 70 else 0
    print(f"{toppers} students scored more than 70")
def p8():
    TupleAge = (2,5,7,10,15,23)
    print(f"Largest value from the given tuple is {max(TupleAge)}")
    print(f"Smallest value from the given tuple is {min(TupleAge)}")
def p9():
    tup = ("Granesh", 'Akash', 'Pradeep', 'Brijendra')
    print(sorted(tup))
def p10():
    price = eval(input("Enter the cost of your items: "))
    print(f"Costliest item costs: {max(price)}")
    print(f"Cheapest item costs: {min(price)}")
    print(f"Total cost: {sum(price)}")
def p11():
    db = {}
    while True:
        item = input("Enter item name (or q to quit): ")
        if item.lower() == 'q': break
        price = input(f"Enter {item}'s cost: ")
        db[item] = price
    for i in db.items():
        print(f"{i[0]} --> {i[1]}") if int(i[1]) > 25 else ''
def p12():
    DYear = {}
    num = 1
    for i in list(calendar.month_name)[1:]:
        DYear[i] = calendar.monthrange(2025, num)[1]
        num += 1
    print(json.dumps(DYear, indent=2))
def p13():print({x:'w3resource'.find(x) for x in 'w3resource'})
def p14():
    db = {}
    while True:
        name = input("Enter name: (or q to exit): ")
        if name.lower() == 'q': break
        rollno = int(input(f"Enter {name}'s roll.no: "))
        marks = int(input(f"Enter {name}'s marks: "))
        db[name] = [rollno, marks]
    for i in db.items():
        print(f"Name: {i[0]}\nRoll Number: {i[1][0]}\nMarks: {i[1][1]}\n\n")
def p15():
    db = {}
    while True:
        name = input("Enter name: (or q to exit): ")
        if name.lower() == 'q': break
        phno = int(input(f"Enter {name}'s phone number: "))
        db[name] = int(phno)
    for i in db.items():
        print(f"{i[0]} -> {i[1]}")
    newName = input("Enter a new friend's name: ")
    newphno = int(input(f"Enter {newName}'s phone number: "))
    db[newName] = int(newphno)
    print('Added!!')
    removeName = input("Enter the name of friend whome u want to remove: ")
    db.pop(removeName)
    print("Removed!!")
    revName = input("Enter the name of friend whose number u want to change: ")
    db[revName] = int(input("Enter the new phone number: "))
    print("Final database: ")
    [print(x) for x in db.items()]
for i in range(1, 21):
    eval(f"q{i}()")
    print()
print("\n\n\n")
for i in range(1,16):
    eval(f"p{i}()")
    print()
