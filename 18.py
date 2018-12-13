lower,upper=map(int,raw_input().split())
for n in range(lower+1,upper):
    order=len(str(n))
    sum=0
    temp=n
    while(temp>0):
        digit=temp%10
        sum+=digit**order
        temp//=10
    if(n==sum):
        print sum
 
