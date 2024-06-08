import time
import math

#Raka Eldiansyah Putra
#21120122140150

# Fungsi untuk menghitung integral dengan metode Trapesium
def trapezoidal_integration(f, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Fungsi f(x) = 4 / (1 + x^2)
def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Fungsi untuk menghitung galat RMS
def rms_error(actual, predicted):
    return math.sqrt((actual - predicted) ** 2)

# Nilai-nilai N yang diuji
N_values = [10, 100, 1000, 10000]

# Menjalankan pengujian
for N in N_values:
    start_time = time.time()
    pi_approx = trapezoidal_integration(f, 0, 1, N)
    end_time = time.time()
    error = rms_error(pi_ref, pi_approx)
    exec_time = end_time - start_time
    print(f"N = {N}:")
    print(f"  Pi Approximation = {pi_approx}")
    print(f"  RMS Error = {error}")
    print(f"  Execution Time = {exec_time:.6f} seconds")
    print()

# Contoh Kode Testing
def test_trapezoidal_integration():
    test_cases = [10, 100, 1000, 10000]
    results = []
    for N in test_cases:
        pi_approx = trapezoidal_integration(f, 0, 1, N)
        results.append((N, pi_approx))
    return results

# Menjalankan contoh testing
test_results = test_trapezoidal_integration()
print("Test Results:")
for N, result in test_results:
    print(f"N = {N}: Pi Approximation = {result}")
