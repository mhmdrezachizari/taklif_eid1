n=int(input())
t=0
for i in range(1,n+1):
    if n%i==0:
        t+=1
        print(f"maghsom elaih ha = {i}")
print(f"tedad maghsom elaih ha barabar ast ba = {t}")