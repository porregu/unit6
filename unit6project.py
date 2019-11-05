number=int(input("until what number you want ?"))
list=[]
for x in range(2, number+1):
        list.append(x)
primes=[]
while len(list)>0:
    track=list[0]
    primes.append(list[0])
    for x in list:
        if x%track==0:
            list.remove(x)

print("this is the primes numbers until ",number, primes)
