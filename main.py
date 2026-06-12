import numpy as np

# ================== CORE ==================
def tent_keystream(N, x0, mu):
    epsilon = 1e-12

    if not (0 < x0 < 1):
        raise ValueError("x0 must be in (0,1)")
    if not (0 < mu <= 2):
        raise ValueError("mu must be in (0,2]")

    x = x0
    K = np.zeros(N, dtype=np.uint8)

    for _ in range(100):
        x = tent_map(x, mu)
        x = (x + epsilon) % 1

    for i in range(N):
        x = tent_map(x, mu)
        x = (x + epsilon) % 1
        K[i] = int((x * 1e6) % 256)

    return K

def tent_map(x, mu):
    return mu*x if x < 0.5 else mu*(1-x)

# ================== TEST DATA ==================
text = "Hello World"
data = np.frombuffer(text.encode(), dtype=np.uint8)

# ================== ENCRYPT ==================
x0 = 0.123456
mu = 1.999

K = tent_keystream(len(data), x0, mu)
C = np.bitwise_xor(data, K)

# ================== SAVE FILE ==================


