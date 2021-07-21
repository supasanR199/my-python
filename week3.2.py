def print_loop(numbers):
    number = int(numbers)
    num = 65
    for i in range(0,number):
        for j in range(0,i+1):
            charector = chr(num)
            print(charector,end=' ')
        num = num + 1
        print("\r")

def compare(input):
    check = 'Exit'
    n = len(check)
    for i in range(0, n):
        if input[i] != check[i]:
            return True
    return False

while True:
    while True:
        n = input('Enter number : ')
        if compare(n):
            print_loop(n)
        else:
            break
    print('End program')
    break