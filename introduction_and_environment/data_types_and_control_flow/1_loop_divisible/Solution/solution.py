lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
for i in range(lower,upper+1):
    if(i%5==0 or i%7==0):
        print(i)