first=int(input())
x=[]

for _ in range(first):
    x.append(input().split('~'))
max=int(x[0][0][:2])*60+int(x[0][0][3:5])
min=int(x[0][1][:2])*60+int(x[0][1][3:5])
for i in range(1,first):
    a=int(x[i][0][:2])*60+int(x[i][0][3:5])
    b=int(x[i][1][:2])*60+int(x[i][1][3:5])
    if(a>max):
        max=a
    if(b<min):
        min=b
print(max, min)
if(max>min):
    print(-1)
else:
    x1=max//60
    y1=max-x1*60
    x2=min//60
    y2=min-x2*60
    print(f"{x1}:{y1}~{x2}:{y2}")
    print("%d:%.2d~%d:%.2d" %(x1,y1,x2,y2))