xset = set()
yset = set()
x = int(input("Lütfen bir sayı giriniz:"))
y = int(input("Lütfen bir sayı daha giriniz:"))

for i in range(1, x + 1):
    if x % i == 0:
        xset.add(i)
    
for j in range(1, y + 1):
    if y % j == 0:
        yset.add(j)
        
ebob = max(xset.intersection(yset))
print(ebob) 

ekok = min(xset.intersection(yset))
print(ekok)
