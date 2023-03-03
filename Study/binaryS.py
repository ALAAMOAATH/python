import math
def binary(array,target):
    min =0
    max =len(array)
    while max>min:
        mid=math.floor((min+max)/2)
        if(target==array[mid]):
            return mid
        elif (target>array[mid]):
            min=mid+1
        else:
            max=mid

            
    return "not found"

print(binary([1,2,3,4,5,6,7,8,9],-99))




