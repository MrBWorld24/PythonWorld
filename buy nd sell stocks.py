minimum=float('inf')
maxpro=0

stocks=[215,265,250,200,240,260,230]
for i in stocks:
    minimum=min(minimum,i)
    maxpro=max(maxpro,i-minimum)
print(maxpro)