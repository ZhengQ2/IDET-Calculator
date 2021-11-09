import math

print("Please enter the larger number")
a = int(input())
print("Please enter the smaller number")
b = int(input())

x = 1
y = 0
r = x*a+y*b
q = 0
q0 = q

print("x\t\ty\t\tr\t\tq\n" + str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0) +"\n")
x1 = x
y1 = y

x = 0
y = 1
r = x*a+y*b
q = 1
q0 = q
r0 = r

print(str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0) +"\n")

x2 = 0
y2 = 0

while r != 0:
    q = math.floor(r0 / r)
    x2 = x1
    y2 = y1
    x1 = x
    y1 = y
    q0 = q
    r0 = r

    x = (0-q) * x1+x2
    y = (0-q) * y1+y2
    r = x * a+y * b
    print(str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0) +"\n")
