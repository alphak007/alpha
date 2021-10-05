import math
dict1={1:"purple", 2:"red", 3:"blue", 25:"red"}
list1=[[4], [2,3,3], [1,2,3], [17]]

def q1(dict1,list1):
    for i in dict1:
        if dict1[i]=='red':
            pass
        elif dict1[i]=='blue':
            pass
        else:
            dict1[i]='green'

    for i in range(0,len(list1)):
        r,b,g=0,0,0
        for j in range(0,len(list1[i])):
            if list1[i][j] in dict1:
                if dict1[list1[i][j]]=='red':
                   r+=1 
                elif dict1[list1[i][j]]=='blue':
                   b+=1
                elif dict1[list1[i][j]]=='green':
                   g+=1
        rbg=[r,b,g]
        rbg_dict={'r':r,'b':b,'g':g}
        rbg.sort(reverse=True)
        max_value=rbg[0]
        for k in rbg_dict:
            if max_value==rbg_dict[k]:
                sublist_color=k
        #list1[i]=list1[i].sort()        
        if(sublist_color=='r'):
            print(list1[i][-1].sort())
        if(sublist_color=='b'):
            print(list1[i][0])
        if(sublist_color=='g'):
            print(list1[i][0])
q1(dict1,list1)
print(dict1)