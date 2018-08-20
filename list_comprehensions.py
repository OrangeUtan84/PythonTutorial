squares1 = []
for x in range(10):
    squares1.append(x**2)
print(squares1)

squares2 = [x**2 for x in range(10)]
print(squares2)

# what?? =>
squares3 = list(map(lambda  x: x**2, range(10)))
print(squares3)


# create a list of tuples containing a combination of all elements that are not equal
combs1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs1.append((x, y))
print(combs1)


# damn!
combs2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs2)