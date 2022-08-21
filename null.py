import float_range

for i in float_range.range(10):
    print(i, end=' ')
# >>> 0 1 2 3 4 5 6 7 8 9

for i in float_range.range(1, 5, 0.5):
    print(i, end=' ')
# >>> 1 1.5 2.0 2.5 3.0 3.5 4.0 4.5

for i in float_range.range(5, 1.5, -0.7):
    print(i, end=' ')
# >>> 5 4.3 3.6 2.9 2.2
