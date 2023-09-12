c = 9 
def test():
    global c
    c=88
    return c

print(c)
test()
print(c)

