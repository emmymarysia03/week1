print("Forwards stars:")
numstars = input("How many lines of stars would you like to print?")
x = 1
stars = ""
while(x <= int(numstars)):
    stars += "*"
    print(stars)
    x += 1
print("Backwards stars:")
num2 = input("How many lines of backwards stars would you like to print?")
stars2 = ""
n = 1
while(n <= int(num2)):
    stars2 += "*"
    n += 1
o = int(num2)
while(o > 0):
    print(stars2)
    stars2 = stars2[0:o-2]
    o -= 1
print("Star waves:")
numwaves = input("How many waves of stars would you like?")
sizewaves = input("What is the biggest number of stars you like in a line?")
a = 1
while(a <= int(numwaves)):
    b = 1
    star = ""
    while(b <= int(sizewaves)):
        star += "*"
        print(star)
        b += 1
    l = int(sizewaves)
    while(l > 1):
        star2 = star[0:l-1]
        print(star2)
        l -= 1
    a+=1
print("Dollar sign pyramids:")
len = input("How big would you like your pyramid to be?")
g = 1
k = int(len)
while(g <= k):
    y = int(len)
    q = y - g
    print(q*" " + "$ "*g + q*" ")
    g+=1
'''
print("Pascal's triangle:")
lines = input("How many lines of Pascal's triangle would you like?")
'''
