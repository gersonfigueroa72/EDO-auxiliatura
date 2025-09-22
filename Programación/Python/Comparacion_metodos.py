import numpy as np
import matplotlib.pyplot as plt

# Definimos la EDO: dy/dt = f(t, y)
def f(t, y):
    return y - t**2 + 1

# Solución exacta (para comparación)
def exact_solution(t):
    return (t + 1)**2 - 0.5 * np.exp(t)

# Método de Euler
def euler_method(f, t0, y0, h, n):
    t = np.zeros(n)
    y = np.zeros(n)
    t[0] = t0
    y[0] = y0
    
    for i in range(n-1):
        y[i+1] = y[i] + h * f(t[i], y[i])
        t[i+1] = t[i] + h
    
    return t, y

# Método de Runge-Kutta de orden 4
def rk4_method(f, t0, y0, h, n):
    t = np.zeros(n)
    y = np.zeros(n)
    t[0] = t0
    y[0] = y0
    
    for i in range(n-1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        t[i+1] = t[i] + h
    
    return t, y

# Parámetros iniciales
t0 = 0      # Tiempo inicial (no cambiar)
y0 = 0.5    # Valor inicial  (no cambiar)
tf = 10      # Tiempo final
h = 2     # Tamaño de paso
n = int((tf - t0) / h) + 1  # Número de puntos

# Resolvemos con ambos métodos
t_euler, y_euler = euler_method(f, t0, y0, h, n)
t_rk4, y_rk4 = rk4_method(f, t0, y0, h, n)

# Calculamos la solución exacta
t_exact = np.linspace(t0, tf, 100)
y_exact = exact_solution(t_exact)

# Graficamos los resultados
plt.figure(figsize=(10, 6))
plt.plot(t_exact, y_exact, 'k-', label='Solución exacta', linewidth=2)
plt.plot(t_euler, y_euler, 'ro--', label='Método de Euler', linewidth=1, markersize=2)
plt.plot(t_rk4, y_rk4, 'bs--', label='Runge-Kutta 4', linewidth=1, markersize=2)

plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación de métodos numéricos para EDO')
plt.legend()
plt.grid(True)
plt.show()

# Calculamos y mostramos los errores
error_euler = np.abs(y_euler - exact_solution(t_euler))
error_rk4 = np.abs(y_rk4 - exact_solution(t_rk4))

print("Error máximo:")
print(f"Euler: {np.max(error_euler):.6f}")
print(f"RK4: {np.max(error_rk4):.6f}")

print("\nError promedio:")
print(f"Euler: {np.mean(error_euler):.6f}")
print(f"RK4: {np.mean(error_rk4):.6f}")