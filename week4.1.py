months  =   ['Jan','Feb','Mar','Aug','Oct','Dec']

def add_months(index,x):
    months.insert(index,x)

def months_remove():
    sum =   0
    for i in range(6):
        months.pop(sum+1)
        sum =   sum+1
    

print(months)
add_months(3,'Apr')
add_months(4,'May')
add_months(5,'Jun')
add_months(6,'July')
add_months(8,'Sep')
add_months(10,'Nov')
print(months)
months_remove()
print(months)