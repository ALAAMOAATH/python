class Solution:
    def romanToInt(self, s: str) -> int:
        translete={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }

        result=0
        arry=[]

        for i in range(len(s)):
            arry+=s[i]




        for i in range(len(arry)):
                if (len(arry)==0):
                    break
                if(len(arry)>1):
                    if (translete[arry[0]]<translete[arry[1]]):
                        result=result+(translete[arry[1]]-translete[arry[0]])
                        del arry[1]
                        del arry[0]
                    else:    
                        result=result+translete[arry[0]]
                        del arry[0]
                else:    
                    result=result+translete[arry[0]]
                    del arry[0]
        return result 











