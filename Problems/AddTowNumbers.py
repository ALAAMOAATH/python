l1 = [9,9,9,9,9,9,9]
l2 =[9,9,9,9]

s1=""
s2=""

for i in range(len(l1)-1,-1,-1):
    s1+=str (l1[i])

for i in range(len(l2)-1,-1,-1):
    s2+=str (l2[i])    

result=int(s1)+int(s2)
result=str(result)

arry=[]
for i in range(len(result)-1,-1,-1):
    arry.append(int (result[i]))


print(arry)