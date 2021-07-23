def charles(n):
    ans=n*n+n+41
    return ans

x=eval(input("Enter number of prime numbers to generate : "))
flag=False
for i in range(0,x):
    val = charles(x)
    if(val > 1):
        for i in range(2, val):
            if(val % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break
    
    if(flag):
        print("NOT Prime Number : ",val)
    else:
        print("Prime Number,", val)

