from math import pi

vec = [-4, -2, 0, 2, 4]
print(vec)

squares = [x*2 for x in vec]
print(squares)

pos = [x for x in vec if x >= 0]
print(pos)


pos = [abs(x) for x in vec]
print(pos)


roundPi = [str(round(pi, i)) for i in range(1,6)]
print(roundPi)


