
stds    =   {}
def students(number_of_students):
    for i in  range(number_of_students):
        print('Enter score of students {}'.format(i+1))
        mid =   int(input('Midteam: '))
        final   =   int(input('Final: '))
        lab =   int(input('Lab: '))  
        result  =   ((mid*35)/100)+((final*35)/100)+lab
        stds[i]  =   [mid,final,lab,result]

def print_stds(number_of_students):
    print('========================================')
    print('No\tMid\tFinal\tLab\tResult')
    for i in range(number_of_students):
        print('{}\t{}\t{}\t{}\t{}'.format(i+1,stds[i][0],stds[i][1],stds[i][2],stds[i][3]))
    print('========================================')
    
def print_conclude(number_of_students):
    maxs_mid    =   []
    maxs_final  =   []
    maxs_lab    =   []
    maxs_result =   []
    for i   in  range(number_of_students):
        maxs_mid.append(stds[i][0])
        maxs_final.append(stds[i][1])
        maxs_lab.append(stds[i][2])
        maxs_result.append(stds[i][3])
    print('Max\t{}\t{}\t{}\t{}'.format(max(maxs_mid),max(maxs_final),max(maxs_lab),max(maxs_result)))
    print('Min\t{}\t{}\t{}\t{}'.format(min(maxs_mid),min(maxs_final),min(maxs_lab),min(maxs_result)))
    print('Avg\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}'.format((sum(maxs_mid)/len(maxs_mid)),(sum(maxs_final)/len(maxs_final)),(sum(maxs_lab)/len(maxs_lab)),(sum(maxs_result)/len(maxs_result))))
    

number_students =   int(input('Enter number of students : '))
students(number_students)
print_stds(number_students)
print_conclude(number_students)




