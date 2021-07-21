def mutipul(number):
    int_number = int(number)
    n = list(range(1, 13, 1))
    for i in n:
        print('{} * {} = {}'.format(int_number, i, int_number * i))


def compare(input):
    check = 'End'
    n = len(check)
    for i in range(0, n):
        if input[i] != check[i]:
            return True
    return False

while True:
    while True:
        n = input('Enter number : ')
        if compare(n):
            mutipul(n)
        else:
            break
    print('End program')
    break
