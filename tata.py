def pattern(n,loop):
    for i in range(0,loop):
        k = 2 * n - 2
        for i in range(0,n):
            for j in range(0,k):
                print(end=" ")
            k = k - 1
            for j in range(0, i+1):
                print("*", end=" ")
            print("\r")


n  =    int(input(print("Input level tree:")))
loop   =    int(input(print("Input  tree:")))
pattern(n,loop)