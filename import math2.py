import math

def harmonic(N):
    return sum(1.0/k for k in range(1, N+1))

import math

def sin_theta(N):
    # Harmonic number H_N
    HN = sum(1.0/k for k in range(1, N+1))

    # Compute cos(theta_N)
    cos_theta = 0.5 + HN / N

    # Clamp to valid domain [-1, 1]
    if cos_theta > 1.0:
        cos_theta = 1.0
    elif cos_theta < -1.0:
        cos_theta = -1.0

    # Compute sin(theta_N) using the identity
    # sin(theta) = sqrt(1 - cos^2(theta))
    sin_theta_value = math.sqrt(max(0.0, 1.0 - cos_theta*cos_theta))

    return sin_theta_value


N_list = [
    2,3,4,5,6,7,8,9,10,
    15,20,25,30,40,50,
    75,100,150,200,300,
    400,500,750,1000,
    2000,5000,10000,75000,100000,1000000,70000000
]

print("N        sin(theta_N)")
for N in N_list:
    print(f"{N:<8} {sin_theta(N):.12f}")
