numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese e segundo número:"))

print("Selecciona la operación")
print("Las opciones son estas")
print("Suma: +")
print("Resta: −")
print("Multiplicacion: *")
print("Division: /")
operacion = input("Ingrse el simbolo de la operacion a realizar")

if operacion == "+":
    print(f"Resultado: {numero_1 + numero_2}")

elif operacion == "-":
    print(f"Resultado: {numero_1 - numero_2}")

elif operacion == "*":
    print(f"Resultado: {numero_1 * numero_2}")
    
elif operacion == "/":
    print(f"Resultado: {numero_1 / numero_2}")
else:
    print("La operacion ingresada no es valida")
    print("Vuelva a intentarlo")


print("Hola")


# numero_1 = None
# numero_2 = None


# def pedir_numeros():
#     pass


# def mostrar_menu():
#     pass


# def sumar():