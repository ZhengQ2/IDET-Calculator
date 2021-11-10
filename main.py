#
# MIT License
#
# Copyright (c) 2021 Zheng Qiu
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
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

print("x\t\ty\t\tr\t\tq\n"\
      + str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0))
x1 = x
y1 = y
r0 = r

x = 0
y = 1
r = x*a+y*b
q = 1
q0 = q

print(str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0))

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
    print(str(x) +"\t\t" + str(y) + "\t\t" + str(r) + "\t\t" + str(q0))
