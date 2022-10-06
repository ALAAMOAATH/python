class Solution:
    def reverse(self, x: int) -> int:
        if(x>-2147483642 and x<2147483642):
                
                y= str(x)
                result=""
                if(x>=0):
                    for i in range(len(y)-1,-1,-1):
                        result+=y[i]
                    if (int (result)>-1463847412 and int (result)<1463847412):
                        return(int (result))
                    else:
                        return 0
                        
                else:
                    for i in range(len(y)-1,0,-1):
                        result+=y[i]
                    if ((int (result)*-1) >-1463847412 and (int (result)*-1) <1463847412):
                        return(int (result)*-1) 
                    else:
                        return 0   
                    
        else:
            return 0


alaa=Solution()
print(alaa.reverse(-2147483642))
