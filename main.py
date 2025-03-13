import math

def main():
    # Datos 
    a = int(input("Ingrese el valor del lado a: "))
    b = int(input("Ingrese el valor del lado b: "))
    c = int(input("Ingrese el valor del lado c: "))
    # validacion
    if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
        print("No es un triangulo valido")
    else:
        print("Es un triangulo")
    triangulo_por_lado
        
    Anguloa= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
    Angulob= math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    Anguloc= 180-(Anguloa+Angulob)

    if Anguloa==90 or Angulob==90 or Anguloc==90:
        print(f"su triangulo tiene un angulo de 90°\es un triangulo rectanguulo\nAngulo A--> {Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C--> {Anguloc}°")
    elif Anguloa>90 or Angulob>90 or Anguloc>90:
        print(f"Su triangulo tiene un angulo mayor a 90°\nes un triangulo obtusangulo\Angulo A--> {Anguloa}°\nAngulo B-->{Angulob}°\nAngulo C-->{Anguloc}°hhhh")
    else:
        print(f"Su triangulo no tiene angulos mayores o iguales a 90°\es un angulo acutangulo\nAngulo A-->{Anguloa}°\nAngulo B--> {Angulob}°\nAngulo C-->{Anguloc}°")


    def triangulo_por_lado(lado1,lado2,lado3):
        if lado1 ==lado2 == lado3:
            print("es un triangilo equilatero")
        elif lado1  ==lado2 != lado3:
            print("es un triangilo isosceles")
        elif lado1 != lado2 != lado3:
            print("es un triangilo escaleno ")

main()






# a6911d9b088bb0379e3bfa9a2e3686138fe73457
