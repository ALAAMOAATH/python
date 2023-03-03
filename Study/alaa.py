# cell=2
# result=0
# # with sum before
# for day in range(1,31):
#     result+=cell
#     cell=cell*2
#     print(f"in day {day} =    {result}") 

# print(result)    
# sum=0
# for day in range(1,31):
#     result=cell
#     sum+=cell
#     cell=cell*2
#     print(f"in day {day} =    {result}") 

  
# print(sum)

# bubble sort

array=[2,3,4,6,7,8,0,10,3,4,6,7,8,3,1,0]
min=array[0]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if(array[j]>array[i]):
            min=array[j]
            array[j]=array[i]
            array[i]=min


print(array)