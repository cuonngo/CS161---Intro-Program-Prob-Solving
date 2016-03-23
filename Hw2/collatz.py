# Copyright (c) 2011 Cuong Ngo
# Hailstone sequence
for number in range(2, 21):
    n = number
    print("n =", n)
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    print("length of sequence:", count)
input("\n\nPress enter key to exit.")
