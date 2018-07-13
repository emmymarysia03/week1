import sys

def bintooct(bin):
    l = len(bin)
    convert = ""
    result = ""
    if "." not in bin:
        if l % 3 == 2:
            convert = "0" + bin
        elif l % 3 == 1:
            convert = "00" + bin
        else:
            convert = bin
        x = 0
        while(x < l):
            c = convert[x:x+3]
            add = bintodec(c)
            result += add
            x += 3
    else:
        first = bin[0:bin.index(".")]
        last = bin[bin.index(".") + 1:l]
        fconv = ""
        lconv = ""
        a = len(first)
        b = len(last)
        if a % 3 == 2:
            fconv = "0" + first
        elif a % 3 == 1:
            fconv = "00" + first
        else:
            fconv = first
        count = 0
        while(count < a):
            f = fconv[count:count+3]
            add = bintodec(f)
            result += add
            count += 3
        result += "."
        o = 0
        if b % 3 == 2:
            lconv = last + "0"
        elif b % 3 == 1:
            lconv = last + "00"
        else:
            lconv = last
        while(o < b):
            h = lconv[o:o+3]
            add = bintodec(h)
            result += add
            o += 3

    print("Your result is: " + result)

def bintohex(bin):
    l = len(bin)
    convert = ""
    result = ""
    if "." not in bin:
        if l % 4 == 3:
            convert = "0" + bin
        elif l % 4 == 2:
            convert = "00" + bin
        elif l % 4 == 1:
            convert = "000" + bin
        else:
            convert = bin
        x = 0
        while(x < l):
            c = convert[x:x+4]
            add = bintodec(c)
            if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                result += add
            else:
                if add == "10":
                    result += "A"
                elif add == "11":
                    result += "B"
                elif add == "12":
                    result += "C"
                elif add == "13":
                    result += "D"
                elif add == "14":
                    result += "E"
                elif add == "15":
                    result += "F"
            x += 4
    else:
        first = bin[0:bin.index(".")]
        last = bin[bin.index(".") + 1:l]
        fconv = ""
        lconv = ""
        a = len(first)
        b = len(last)
        if a % 4 == 3:
            fconv = "0" + first
        elif a % 4 == 2:
            fconv = "00" + first
        elif a % 4 == 1:
            fconv = "000" + first
        else:
            fconv = first
        x = 0
        while(x < a):
            c = fconv[x:x+4]
            add = bintodec(c)
            if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                result += add
            else:
                if add == "10":
                    result += "A"
                elif add == "11":
                    result += "B"
                elif add == "12":
                    result += "C"
                elif add == "13":
                    result += "D"
                elif add == "14":
                    result += "E"
                elif add == "15":
                    result += "F"
            x += 4
        result += "."
        o = 0
        if b % 4 == 3:
            lconv = last + "0"
        elif b % 3 == 2:
            lconv = last + "00"
        elif b % 3 == 1:
            lconv = last + "000"
        else:
            lconv = last
        while(o < b):
            h = lconv[o:o+4]
            add = bintodec(h)
            if(add != "10" and add != "11" and add != "12" and add != "13" and add != "14" and add != "15"):
                result += add
            else:
                if add == "10":
                    result += "A"
                elif add == "11":
                    result += "B"
                elif add == "12":
                    result += "C"
                elif add == "13":
                    result += "D"
                elif add == "14":
                    result += "E"
                elif add == "15":
                    result += "F"
            o += 4
    print("Your result is: " + result)

def bintodec(bin):
    l = len(bin)
    dec = 0
    if "." not in bin:
        for x in range(l):
            n = bin[x]
            num = int(n)
            num *= 2** (l - 1 - x)
            dec += num
    else:
        first = bin[0:bin.index(".")]
        last = bin[bin.index(".") - 1:l-1]
        a = len(first)
        b = len(last)
        for x in range(a):
            n = first[x]
            num = float(n)
            num *= 2** (a - 1 - x)
            dec += num
        for x in range(b):
            n = last[x]
            if(n == "."):
                continue
            num = float(n)
            num *= 2 ** (0 - (x + 1))
            dec += num
    return(str(dec))

def mod(a, b):
    orig = a
    while a > 0:
        a = a - b
    if(a < 0):
        a += b
    return(a)

def add(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))

def sub(a, b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))

def mult(a, b):
    result = 0
    for x in range(b):
        result += a
    print(str(a) + " * " + str(b) + " = " + str(result))

def div(a, b):
    rem = mod(a, b)
    result = 0
    oa = a #stores the original value of a, since a is modified when dividing
    if(rem == 0):
        while a > 0:
            a = a - b
            result += 1
    if(rem > 0):
        a = a - rem
        while a > 0:
            a = a - b
            result += 1
    rem = float(rem)
    result = result + rem/2
    print(str(oa) + " / " + str(b) + " = " + str(result))

def pow(a, b):
    result = a
    for x in range(b - 1):
        result *= a
    print(str(a) + "^" + str(b) + " = " + str(result))

def min(nums):
    min = sys.maxsize
    for num in nums:
        if num < min:
            min = num
    print("The minimum number in your list is " + str(min))

def max(nums):
    max = -sys.maxsize - 1
    for num in nums:
        if num > max:
            max = num
    print("The maximum number in your list is " + str(max))

def helper():
    o = input("Enter the number corresponding to your desired operation: (1) addition, (2) subtraction, (3) multiplication, (4) division, (5) power, (6) modulo, (7) min, (8) max, (9) binary to decimal, (10) binary to octal, (11) binary to hex: ")
    if(o != "1" and o != "2" and o != "3" and o != "4" and o != "5" and o != "6"):
        while(o != "1" and o != "2" and o != "3" and o != "4" and o != "5" and o != "6" and o != "7" and o != "8" and o != "9" and o != "10" and o != "11"):
            o = input("Please enter a valid operation option: ")
    op = int(o)
    if(o == "1" or o == "2" or o == "3" or o == "4" or o == "5" or o == "6"):
        a = input("Enter your first number: ")
        b = input("Enter your second number: ")
        num1 = int(a)
        num2 = int(b)
        if op == 1:
            add(num1, num2)
        if op == 2:
            sub(num1, num2)
        if op == 3:
            mult(num1, num2)
        if op == 4:
            div(num1, num2)
        if op == 5:
            pow(num1, num2)
        if op == 6:
            rem = mod(num1, num2)
            if(rem == 0):
                print(str(num1) + "%" + str(num2) + " = 0")
            else:
                print(str(num1) + "%" + str(num2) + " = " + str(rem))
    if(op == 7 or op == 8):
        numList = []
        i = ""
        while(i != "q"):
            i = input("Please enter a number to add to your list. Press q when you are done entering numbers: ")
            if(i == "q"):
                break
            else:
                num = int(i)
                numList.append(num)
        if(op == 7):
            min(numList)
        if(op == 8):
            max(numList)
    if(op == 9):
        num = input("Please enter a binary number to convert to decimal: ")
        print("The result of your conversion is " + bintodec(num))
    if(op == 10):
        num = input("Please enter a binary number to convert to octal: ")
        bintooct(num)
    if(op == 11):
        num = input("Please enter a binary number to convert to hex: ")
        bintohex(num)

helper()
