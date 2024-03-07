# ¿Cuál es la suma de los primeros 100 números naturales?

n = 100
sumatoria = 0

for cont in range(1,n+1):
    sumatoria = sumatoria + cont
    
print("La sumatoria de los primeros",n,"naturales es",sumatoria)