def multipleOfThree():
    n = int(input("Enter a number: "))
    i = 0
    if n % 3 == 0:
        print("This number is a multiple of 3.")
        for i in range(0, n//3):
            print(n, n-1, n-2)
            n-=3
    else:
        print("This number isn't a multiple of 3.")
        for i in range(0, n/3):
            print(n, n-1, n-2)
            n-=3
        print(1, 2)
multipleOfThree()