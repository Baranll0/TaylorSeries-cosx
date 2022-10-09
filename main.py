import math

n=int(input("Kacıncı terim: "))
x=(math.pi/5)
a=1
b=1
c=1
sinus=1
for i in range(2,n+1,2):

    sinus=sinus*-1
    a=pow(x,i)
    b=b*i*(i-1)
    c=c+sinus*a/b
gercek=math.cos(math.pi/5)

print(f"Gercek deger:  (n={n-1} icin) {round(gercek,5)}")
print(f"Yaklasik deger: (n={n-1} icin) {round(c,5)}")
kesme=gercek-c
print(f"Kesme: (n={n-1}) {round(kesme,5)}")


