
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def devide(a,b):
    if  b   ==  0:
        return(True)
    else:
        return(a/b)
symbol  =   ['+','-','*','/']
def menu(ch):
    if  math[3] ==  True    :
        print("Devide by Zero")
    else    :
        print('Answer is {} {} {} = {}'.format(a,symbol[ch-1],b,math[ch-1]))
print('=====================Menu=====================')
print('1.Add\n2.Subtract\n3.Multiply\n4.Devide')
a   =   float(input('Enter number 1 : '))
b   =   float(input('Enter number 2 : '))
ch  =   int(input('Select choice : '))
math    =   [add(a,b),subtract(a,b),multiply(a,b),devide(a,b)]
print('==============================================')

menu(ch)
