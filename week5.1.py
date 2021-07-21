def work_hours(mon,tue,wed,thu,fri):
    return mon+tue+wed+thu+fri

employ  =   {}
in_file =   open('workHours.txt','r')
print('=======================================================')
for line in in_file:
    ids,name,mon,tue,wed,thu,fri =   line.split()
    employ[line] =   [ids,name,float(mon),float(tue),float(wed),float(thu),float(fri)]
    print('{}\tID:{}\tWorks\t{:.2f} hours\t{:.2f} Days'.format(employ[line][1],employ[line][0]\
        ,work_hours(employ[line][2],employ[line][3],employ[line][4],employ[line][5],employ[line][5]),\
            work_hours(employ[line][2],employ[line][3],employ[line][4],employ[line][5],employ[line][5])/5))
print('=======================================================')
for i   in  employ:
    x   =   '* '
    n   =   int(work_hours(employ[i][2],employ[i][3],employ[i][4],employ[i][5],employ[i][5]))
    print('{}\t{}\t'.format(employ[i][1],x*n))
in_file.close()
    
