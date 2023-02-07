n=int(input ())
f=1
sum=0
for i in range(1,n+1):
   x=f*i
   sum+=x
   f=f*i
print(sum)
 