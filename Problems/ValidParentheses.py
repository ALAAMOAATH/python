# class Solution:
#     def isValid(self, s: str) -> bool:
#         if(len(s)%2==0):
#             i=0
#             while(i<len(s)):

#                 if(ord(s[i])==40):
#                     if(ord(s[i+1])!=41):
#                         return False
#                 else:
#                     if(ord(s[i+1])!=ord(s[i])+2):
#                         return False
#                 i+=2
#         else:
#             return False
#         return True

# class Solution:
#     def isValid(self, s: str) -> bool:
#         if(len(s)%2==0):
#             a1=0
#             a2=0
#             b1=0
#             b2=0
#             c1=0
#             c2=0
#             for i in range(len(s)):
#                 if(s[i]=='('):
#                     a1+=1
#                     if(a1-a2==2):
#                         return False
#                     try:
#                         if(s[i+1]==']' or s[i+1]=='}'):
#                             return False
#                     except(IndexError):
#                         continue    
#                 elif(s[i]==')'):
#                     a2+=1
#                     if(a2>a1):
#                         return False
#                 elif(s[i]=='['):
#                     b1+=1
#                     if(b1-b2==2):
#                         return False
#                     try:
#                         if(s[i+1]==')' or s[i+1]=='}'):
#                             return False
#                     except(IndexError):
#                         continue     
#                 elif(s[i]==']'):
#                     b2+=1
#                     if(b2>b1):
#                         return False
#                 elif(s[i]=='{'):
#                     try:
#                         if(s[i+1]==']' or s[i+1]==')'):
#                             return False
#                     except(IndexError):
#                         continue     
#                     c1+=1
#                     if(c1-c2==2):
#                         return False
#                 elif(s[i]=='}'):
#                     c2+=1
#                     if(c2>c1):
#                         return False
#             if(a1==a2 and b1==b2 and c1==c2):
#                 return True
#         else:
#             return False
#         return False

# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '()' in s or '[]'in s or '{}' in s:
#             s = s.replace('()','').replace('[]','').replace('{}','')
#         return False if len(s) !=0 else True


# test = Solution()
# print(test.isValid("([({})])"))






        
store=[]
top=-1
def push(x):
    global top , store
    top+=1
    store.append(x)

def pop():
    global top , store
    top-=1
    return store[top+1]
        
def getTop():
    global top , store
    if(top>-1):
        return store[top]

def isEmpty():
    global top , store
    if(top>-1):
        return False
    else:
        return True

def pair(open,exit):
            if(open=='(' and exit==')'):
                return True
            elif(open=='{' and exit=='}'):
                return True
            elif(open=='[' and exit==']'):
                return True
            else:
                return False
        

class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
               push(s[i]) 
            elif(s[i]==')' or s[i]=='}' or s[i]==']'):
                if(isEmpty):
                    return False
                elif (pair(getTop,s[i])):
                    pop()
                else:
                    return False

        if(isEmpty):
            return True
        else:
            return False        

test=Solution()

# print(test.isValid("()"))

push("(")
push("(")
push("(")
push("(")
push("}")

print(pop())

print(top)