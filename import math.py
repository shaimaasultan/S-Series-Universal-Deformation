import math

def harmonic(N):
    return sum(1.0/k for k in range(1, N+1))

print("N\tcos1/2+H/N\tcos1/2+H/N^2")

for N in [2,3,4,5,6,7,8,9,10,15,20,25,30,40,50,75,100,150,200,300,400,500,750,1000,1500,2000,5000,7500,10000,15000,20000,30000,40000,50000,75000,100000,150000,200000,300000,400000,500000,750000,1000000]:
    H = harmonic(N)
    cos1 = 0.5 + H/N        # Correct scaling (converge to 1/2)
    cos2 = 0.5 + H/(N*N)    # CORRECT scaling (converges to 1/2 faster than cos1)
    print(f"{N}\t{cos1:.12f}\t{cos2:.12f}")
