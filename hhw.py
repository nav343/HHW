"""
Autumn Holiday Homework 
CLASS: 11th B
CHAPTERS: List Manipulation
        : String Manipulation

TYPE C: Programming Practice (Pg 349, 350, 394, 395) -> ANSWERS
"""

# For styling :)
import subprocess
import time
def Col(string: str, color: str = "LIGHT_WHITE", bold:bool= False) -> str:
    col = {"BLACK" : "\033[0;30m",
    "RED" : "\033[0;31m",
    "GREEN" : "\033[0;32m",
    "BROWN" : "\033[0;33m",
    "BLUE" : "\033[0;34m",
    "PURPLE" : "\033[0;35m",
    "CYAN" : "\033[0;36m",
    "LIGHT_GRAY" : "\033[0;37m",
    "DARK_GRAY" : "\033[1;30m",
    "LIGHT_RED" : "\033[1;31m",
    "LIGHT_GREEN" : "\033[1;32m",
    "YELLOW" : "\033[1;33m",
    "LIGHT_BLUE" : "\033[1;34m",
    "LIGHT_PURPLE" : "\033[1;35m",
    "LIGHT_CYAN" : "\033[1;36m",
    "LIGHT_WHITE" : "\033[1;37m",
    "BOLD" : "\033[1m",
    "FAINT" : "\033[2m",
    "ITALIC" : "\033[3m",
    "UNDERLINE" : "\033[4m",
    "BLINK" : "\033[5m",
    "NEGATIVE" : "\033[7m",
    "CROSSED" : "\033[9m",
    "END" : "\033[0m"}
    return f"{col.get(color)}{col.get('BOLD') if bold else ''}{string}{col.get('END')}"

"""
Chapter 1: List Manipulation
"""

QL = [ 
      "Write a program to increment the elements of a list with a number",
"Write a program that reverses a list of integers (in place)",
"Write a program that inputs two lists and creates a third, that contains all elements of the first followed by all elements of the second",
'Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10',
"Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed",
"Write a program to check if a number is present in the list or not. If the number is present, print the position of the number. Print an appropriate message if the number is not present in the list.",
'Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M.',
"""
    Q7> Create the following lists using a for loop:
    (a) A list consisting of the integers 0 through 49
    (b) A list containing the sqaures of the integers 1 through 50
""",
'Write a program which rotates the elments of a list so that the elements at the first index moves to the second index, the elements in the second index moves to the third etc and the elements in the last index moves to the first index',
"Write a program tha reads the n to display the nth term of Fibonacci series",
"""
    Q11> Write programs as per the following specifications
    (a) Print the length of the longest string in the list of strings str_list.
    Precondition: the list will contain at least one element.

    (b) L is a list of numbers. Print a new list here each element is the corresponding element of the list L summed with number num.
""",
'Write a program to read two lists num and denum which contain the numerators and denominators of same fractions at the respective indexes. Then display the smallest fraction along with its index.',
'Write a program to display the maximum and minimum values from the specified range of indexes of a list',
"Write a program to move all duplicate values in a list to the end of the list",
"Write a program to compare two equal sized lists and print the first index where they differ.",
      ]

def Q1():
    #Q> Write a program to increment the elements of a list with a number
    lst = eval(input("Enter your data: "))
    num = int(input("Enter the number by which you want to increment the elements: "))
    for i in range(0, len(lst)):
        lst[i] += num
    print(lst)

def Q2():
    #Q> Write a program that reverses a list of integers (in place)
    lst = eval(input("Enter some integer data: "))
    for i in range(0, len(lst)):
        lst[i] = int(str(lst[i])[::-1])
    print(lst)

def Q3():
    #Q> Write a program that inputs two lists and creates a third, that contains all elements of the first followed by all elements of the second

    # By using built-in methods
    lst1: list = eval(input("Enter some data (L 1): "))
    lst2: list = eval(input("Enter some data (L 1): "))
    lstRes = []
    lstRes.extend(lst1)
    lstRes.extend(lst2)
    print(lstRes)

"""
    # By making custom algorithm
    lst3: list = eval(input("Enter some data (L 1): "))
    lst4: list = eval(input("Enter some data (L 1): "))
    lstRes2 = []
    for i in lst3:
       lstRes2.append(i) 
    for j in lst4:
       lstRes2.append(j) 
    print(lstRes2)
"""


def Q4():
    #Q> Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10
    lst: list[int] = eval(input("Enter your data (integers between 1 and 12, both inclusive): "))
    for i in range(0, len(lst)):
        if lst[i] < 1 or lst[i] > 12: print("ERROR: Invalid, numbers must be between 1 and 12"); exit(1)
        lst[i] = 10 if lst[i] > 10 else lst[i]
    print(lst)

def Q5():
    #Q5> Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed
    lst: list[str] = eval(input("Enter your data (strings): "))
    for i in range(0, len(lst)):
        lst[i] = lst[i][1:]
    print(lst)

def Q6():
    #Q6> Write a program to check if a number is present in the list or not. If the number is present, print the position of the number. Print an appropriate message if the number is not present in the list.
    lst: list[int] = eval(input("Enter your data (integers): "))
    num = int(input("Enter a number: "))
    if num in lst:
        print(f"{num} exists in the list.")
        print(f"First occurrence of {num} in {lst} is at position: {lst.index(num)}")
    else:
        print(f"{num} does not exist in your given list")

def Q7():
    """
    Q7> Create the following lists using a for loop:
    (a) A list consisting of the integers 0 through 49
    (b) A list containing the sqaures of the integers 1 through 50
    """
    lst1, lst2 = [],[]
    for i in range(0, 50):
        lst1.append(i)
    for j in range(1, 51):
        lst2.append(j**2)
    print(lst1, lst2, sep='\n\n')

def Q8():
    #Q8> Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M.
    L = eval(input("Enter the first list: "))
    M = eval(input("Enter the second list: "))
    if len(L) != len(M): print("ERROR: Lists must be of the same size"); exit(1)
    ResList = []
    for i in range(0, len(L)):
        ResList.append(L[i] + M[i])
    print(ResList)

def Q9():
    #Q9> Write a program which rotates the elments of a list so that the elements at the first index moves to the second index, the elements in the second index moves to the third etc and the elements in the last index moves to the first index
    lst: list = eval(input("Enter your list: "))
    lst.insert(0,lst.pop())
    print(lst)

def Q10():
    #Q10> Write a program tha reads the n to display the nth term of Fibonacci series
    def Fib(n: int) -> int:
        if n == 1 or n == 0: return n
        else: return Fib(n-1) + Fib(n-2)

    fibLst = []
    n = int(input("Enter n: "))
    for _ in range(1, n + 1):
        fibLst.append(Fib(n))
    print(fibLst.pop()) if n != 0 else print(0)

def Q11():
    """
    Q11> Write programs as per the following specifications
    (a) Print the length of the longest string in the list of strings str_list.
    Precondition: the list will contain at least one element.

    (b) L is a list of numbers. Print a new list here each element is the corresponding element of the list L summed with number num.
    """
    # Part a:
    str_list: list[str] = eval(input("Enter your data (strings): "))
    maxLen = 0
    for i in str_list:
        if len(i) > maxLen: maxLen = len(i)
    print(maxLen)

    # Part b:
    L: list[int] = eval(input("Enter your data (integers): "))
    num = int(input("Enter a number: "))
    resList = []
    for i in L:
        resList.append(i + num)
    print(resList)

def Q12():
    #Q12> Write a program to read two lists num and denum which contain the numerators and denominators of same fractions at the respective indexes. Then display the smallest fraction along with its index.
    print()
    num: list[int] = eval(input("Enter the numerator (integer): "))
    denum: list[int] = eval(input("Enter denominator (integer): "))
    resList = []
    if len(num) != len(denum): print("ERROR: Lists must be of the same size"); exit(1)
    for i in range(0, len(num)):
        resList.append(num[i]/denum[i])
    print(min(resList))

def Q13():
    #Q13> Write a program to display the maximum and minimum values from the specified range of indexes of a list
    lst: list[int] = eval(input("Enter your list (integer): "))
    start = int(input("Enter the starting value: "))
    end = int(input("Enter the ending value: "))
    resList = []
    for i in range(start, end + 1) :
        resList.append(lst[i])
    print(f"Maximum Value in the given range: {max(resList)}")
    print(f"Minimum Value in the given range: {min(resList)}")

def Q14():
    #Q14> Write a program to move all duplicate values in a list to the end of the list
    lst: list = eval(input("Enter your list: "))
    sep = []
    dup = []
    for i in lst: dup.append(i) if i in sep else sep.append(i)

    # Extra fancy version of the above 2 lines :)
    # dup = [i for i in lst if i not in sep and not sep.add(i)]
    for j in dup:
        if j in sep: sep.remove(j); dup.append(j)

    dup.sort()
    print(sep + dup)
    

def Q15():
    #Q15> Write a program to compare two equal sized lists and print the first index where they differ.
    lst1: list = eval(input("Enter data for list 1: "))
    lst2: list = eval(input("Enter data for list 2: "))
    if len(lst1) != len(lst2): print("ERROR: The lists must contain equal number of elements"); exit(1)
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            print(f"Values of the given sets differ at position -> {i + 1}")
            break
    else: print("The values don't differ at all")


"""
Chapter 2: String Manipulation
"""

def P1():
    #Q1> Write a program to count the number of times a character occurs in the given string.
    print("Write a program to count the number of times a character occurs in the given string.")
    string = input("Enter your string: ")
    chars = set(x for x in string if x != ' ')
    counter = []
    for i in chars:
        count = 0
        for j in string:count += 1 if i == j else 0
        counter.append(count)

    print("Your string contains: ")
    for a in range(0, len(chars)): print(f"{list(chars)[a]}: {counter[a]} time(s)...")


def P2():
    #Q2> Write a program which replaces all vowels in the string with '*'
    print("Write a program which replaces all vowels in the string with '*'")
    string = input("Enter your string: ")
    for i in string:
        if i.lower() in ['a','e','i','o','u']: string = string.replace(i, '*')
    print(string)

def P3():
    #Q3> Write a program which reverse a string and stores the reversed string in a new string
    print("Write a program which reverse a string and stores the reversed string in a new string")
    string = input("Enter your string: ")
    revStr = string[::-1]
    print(revStr)

def P4():
    #Q4> Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code and the next three numbers.
    print("Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code and the next three numbers.")
    phNum = input("Enter your phone number (format: XXX-XXX-XXXX): ")
    if len(phNum.replace("-",'')) != 10 or len(phNum) > 12: print("ERROR: Phone number must contain 10 digits"); exit(1)
    if phNum[3] != '-' or phNum[7] != '-': print("ERROR: Number must be of the form: XXX-XXX-XXXX"); exit(1)
    print("Valid Number")

def P5():
    """
    Q5> Write a program that should do the following
    - prompt the user for a string
    - extract all the digits from the string
    - If there are digits:
        - sum the collected digits together
        - print out:
            - the original string
            - the string
            - the sum of the digits
    """
    print("""
    Q5> Write a program that should do the following
    - prompt the user for a string
    - extract all the digits from the string
    - If there are digits:
        - sum the collected digits together
        - print out:
            - the original string
            - the string
            - the sum of the digits
    """)
    string = input("Enter a string: ")
    digits = ""
    sum = 0
    for i in string:
        if i.isdigit(): digits += i
    for j in digits:
        sum += int(j)
    print(f"Your String: {string}\nDigits: {digits}\nSum of digits: {sum}") if len(digits) != 0 else print("Your string contains no digits")

def P6():
    """
    Q6> Write a program that should prompt the user to type some sentences followed by "enter". It should then print the original sentences and the following statics relating to the sentences:
    - number of words
    - number of characters (including white spaces and punctuations)
    - percentage of characters that are alphanumeric
    """
    print("""
    Q6> Write a program that should prompt the user to type some sentences followed by "enter". It should then print the original sentences and the following statics relating to the sentences:
    - number of words
    - number of characters (including white spaces and punctuations)
    - percentage of characters that are alphanumeric
    """)
    sentence = input("Enter a sentence")
    wordsLength = len(sentence.split(" "))
    charLength = len(sentence)
    noAlphaNum = 0
    for i in sentence:
        if i.isalnum(): noAlphaNum += 1
    percentageNoAlphaNum = (noAlphaNum/charLength)*100
    print(f"Your sentence: {sentence}\nNumber of words: {wordsLength}\nNumber of characters: {charLength}\n% of alphanumeric characters: {percentageNoAlphaNum}")

def P7():
    """
    Q7> Write a python program as per specifications given below
    - repeatedly prompt for a sentence s or for `q` to quit
    - upon input of a sentence s, print the string produced from s by converting each lower case letter to upper case and each upper case letter to lower case
    - all other characters are left unchanged
    """
    print("""
    Q7> Write a python program as per specifications given below
    - repeatedly prompt for a sentence s or for `q` to quit
    - upon input of a sentence s, print the string produced from s by converting each lower case letter to upper case and each upper case letter to lower case
    - all other characters are left unchanged
    """)

    while True:
        s = input("Enter a string or 'q' to quit: ")
        if s.lower() == 'q': break
        dupS = ""
        for i in s:
            if i.islower(): dupS += i.upper()
            elif i.isupper(): dupS += i.lower()
            else: dupS += i
        print(dupS)

def P8():
    """
    Q8> Write a program that does the following:
    - takes two inputs: the first, an integer and the second, a string
    - from the input string extact all digits, in the order they occurred, from the string.
        - if no digits occur, set the extracted digits to 0
    - add the integer input and the digits extracted from the string together as integers
    - print a string of the form:
      "integer_input + string_digit = sum"
    """
    print("""
    Q8> Write a program that does the following:
    - takes two inputs: the first, an integer and the second, a string
    - from the input string extact all digits, in the order they occurred, from the string.
        - if no digits occur, set the extracted digits to 0
    - add the integer input and the digits extracted from the string together as integers
    - print a string of the form:
      "integer_input + string_digit = sum"
    """)

    integer = int(input("Enter an integer: "))
    sentence = input("Enter a sentence: ")
    digits = ""
    for i in sentence:
        if i.isdigit(): digits += i
    res = integer + int(digits if len(digits) != 0 else '0')
    print(f"{integer} + {int(digits if len(digits) != 0 else '0')} = {res}")

#incomplete
def P9():
    #Q9> Write a program that takes two strings from the user and dsplays the smaller string in single line and the larger string as per the given format (in the book)
    print("Write a program that takes two strings from the user and dsplays the smaller string in single line and the larger string as per the given format (in the book)")
    """
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    larger = str1 if str1 > str2 else str2
    print(str1 if larger == str2 else str2)
    pattern = ""
    for i in range(0, len(larger)//2):
        pattern += larger[i] + (len(larger) -2)*" " + larger[-i] + '\n'
    print(pattern)
    """
    print("incomplete")
    pass

#incomplete
def P10():
    print("incomplete")
    pass

def P11():
    #Q11> Write a program that asks the user for a string (only single space b/w words) and returns an estimate of how many words are in the string
    print("Write a program that asks the user for a string (only single space b/w words) and returns an estimate of how many words are in the string")
    string = input("Enter a string: ")
    print(f"Your string contains {len(string.split())} words")

def P12():
    #Q12> Write a program to input a formula with some brackets and checks, and prints out if the formula has the same number of opening and closing parenthesis
    print("Write a program to input a formula with some brackets and checks, and prints out if the formula has the same number of opening and closing parenthesis")
    formula = input("Enter some formula: ")
    noOpen, noClose = 0,0
    for i in formula:
        noOpen += 1 if i == '(' else 0
        noClose += 1 if i == ')' else 0
    print("Your formula has the same number of opening and closing brackets") if noOpen == noClose else print("Your formula doesn't have the same number of opening and closing parenthesis.\nPerhaps you might have missed one or two somewhere!!")

def P13():
    #Q13> Write a program that inputs a line of text and prints out the count of vowels in it
    print("Write a program that inputs a line of text and prints out the count of vowels in it")
    string = input("Enter a string: ")
    noVowels = 0
    for i in string: noVowels += 1 if i in 'aeiou' else 0
    print(f"Your string has {noVowels} vowels in it")

def P14():
    #Q14> Write a program to input a line of text and print the biggest word (length wise) from it
    print("Write a program to input a line of text and print the biggest word (length wise) from it")
    string = input("Enter a string: ")
    words = string.split()
    noWords = [len(i) for i in words]
    print(f"The longest word in your string contains {max(noWords)} letters")
    print(f"The first occurrence of longest word in your string is -> {words[noWords.index(max(noWords))]}")

def P15():
    #Q15> Write a program to input a line of text and create a new line of text where each word of input line in reversed
    print("Write a program to input a line of text and create a new line of text where each word of input line in reversed")
    string = input("Enter a string: ")
    words = string.split()
    [print(x, end=' ') for x in [i[::-1] for i in words]]

# For running all programs in one go
print(Col("Chapter 1 starts here...", 'GREEN', bold=True))
time.sleep(1)
subprocess.run("clear")

for i in range(1, 16):
    print(Col(QL[i-1], "PURPLE"))
    eval(f"Q{i}()")
    print('\n\n')

print(Col("Chapter 1 ends here..", 'RED', bold=True))
for x in range(5, 0, -1):
    print(Col(f"Clearing in {x} second{'s' if x != 1 else ''}...", "NEGATIVE", bold=True), end='\r');time.sleep(1)
subprocess.run("clear")

print(Col("Chapter 2 starts here..", "GREEN", bold=True))
time.sleep(2)
for j in range(1, 16):
    eval(f"P{j}()")
    print('\n\n')
print(Col("DONE!!!", "BOLD"))
