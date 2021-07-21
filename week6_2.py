pi  =   3.14
def circumference(r):
    result  =   2*pi*r
    return  result
def circular_area(r):
    result  =   pi*r*r
    return result
def can_skin(h,r):
    'funtion to calcula serface of can'
    result  =   ((circumference(r)*h)+(2*circular_area(r)))
    return result

print(can_skin(10,10))