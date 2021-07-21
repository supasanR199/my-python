
def greader(a,b,c):
    score   =   a+b+c
    if score>=80 and score<=100:
        return'A'
    elif    score>=75    and score<80:
        return'B+'
    elif    score>=70    and score<75:
        return'B'
    elif    score>=65    and score<70:
        return'C+'
    elif    score>=60    and score<65:
        return'C+'
    elif    score>=55    and score<60:
        return'D+'
    elif    score>=50    and score<55:
        return'D'
    elif    score>=0    and score<50:
        return'F'
def score_cal(a,b,c):
    return a+b+c

stduents_score  =   {}
sou_file    =   open('stuScore.txt','r')
outfile =   open('b.txt','w')
outfile.write('============================================================\n')
for i   in  sou_file:
    ids,number,sc,sc1,sc2 =   i.split()
    stduents_score[i]   =   [ids,number,float(sc),float(sc1),float(sc2)]
    outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(stduents_score[i][0],stduents_score[i][1],stduents_score[i][2]\
        ,stduents_score[i][3],stduents_score[i][4]\
        ,score_cal(stduents_score[i][2],stduents_score[i][3],stduents_score[i][4]),\
        greader(stduents_score[i][2],stduents_score[i][3],stduents_score[i][4])))
    stduents_score[i]   =   [ids,number,float(sc),float(sc1),float(sc2), greader(stduents_score[i][2],stduents_score[i][3],stduents_score[i][4])]
outfile.write('============================================================\n')
sou_file.close()
count   =   len(stduents_score)
outfile.write('Count\t=\t{}\n'.format(count))
count_A  =   0
count_Bp =   0  
count_B  =   0
count_Cp =   0 
count_C  =   0
count_Dp =   0 
count_D  =   0
count_F  =   0  

for i   in  stduents_score:
    if  stduents_score[i][5]    ==  'A':
        count_A =  count_A+1
    elif    stduents_score[i][5]    ==  'B+':
        count_Bp    =count_Bp+1  
    elif    stduents_score[i][5]    ==  'B':
        count_B    =count_B+1
    elif    stduents_score[i][5]    ==  'C+':
        count_Cp    =count_Cp+1
    elif    stduents_score[i][5]    ==  'C':
        count_C    =count_C+ 1
    elif    stduents_score[i][5]    ==  'D+':
        count_Dp    =count_Dp+1
    elif    stduents_score[i][5]    ==  'D':
        count_D    =count_D+1
    elif    stduents_score[i][5]    ==  'F':
        count_F    =count_F+1
outfile.write('A\t=\t{}\n'.format(count_A))
outfile.write('B+\t=\t{}\n'.format(count_Bp))
outfile.write('B\t=\t{}\n'.format(count_B))
outfile.write('C+\t=\t{}\n'.format(count_Cp))
outfile.write('C\t=\t{}\n'.format(count_C))
outfile.write('D+\t=\t{}\n'.format(count_Dp))
outfile.write('D\t=\t{}\n'.format(count_D))
outfile.write('F\t=\t{}\n'.format(count_F))

