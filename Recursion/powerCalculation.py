def power(a,b):
    p = 1
    for i in range(b):
        p *= a
    return p

def power(a,b,ans,i):
    if i == b:
        return ans
    ans *= a
    return power(a,b,ans,i+1)
print(power(3,2,ans=1,i=0))