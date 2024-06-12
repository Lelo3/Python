import math

def calcola_perimetro():
    print("Scegli una figura geometrica per calcolare il perimetro o l'area del triangolo:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("4. Triangolo (area)")

    scelta = input("Inserisci il numero corrispondente alla figura scelta: ")

    def calcola_perimetro_quadrato():
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print(f"Il perimetro del quadrato è: {perimetro}")

    def calcola_circonferenza_cerchio():
        raggio = float(input("Inserisci il raggio del cerchio: "))
        circonferenza = 2 * math.pi * raggio
        print(f"La circonferenza del cerchio è: {circonferenza}")

    def calcola_perimetro_rettangolo():
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = 2 * (base + altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")

    def calcola_area_triangolo():
        base = float(input("Inserisci la lunghezza della base del triangolo: "))
        altezza = float(input("Inserisci l'altezza del triangolo: "))
        area = (base * altezza) / 2
        print(f"L'area del triangolo è: {area}")

    if scelta == '1':
        calcola_perimetro_quadrato()
    elif scelta == '2':
        calcola_circonferenza_cerchio()
    elif scelta == '3':
        calcola_perimetro_rettangolo()
    elif scelta == '4':
        calcola_area_triangolo()
    else:
        print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    calcola_perimetro()