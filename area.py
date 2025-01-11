arquivo = "3.0 4.0 5.2"

PI = 3.14159

a = float(arquivo.split(" ")[0])
b = float(arquivo.split(" ")[1])
c = float(arquivo.split(" ")[2])

print(f'TRIANGULO: {((a * c) / 2):.3f}')
print(f'CIRCULO: {PI*c*c:.3f}')
print(f'TRAPEZIO: {((a+b)*c) / 2:.3f}')
print(f'QUADRADO: {(b*b):.3f}')
print(f'RETANGULO: {a*b:.3f}')