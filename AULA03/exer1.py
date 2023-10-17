palavra = str(input("Digite uma palavra: ")).lower()

letra_a = False
quant = 0

for letra in palavra:
    if letra =="a":
        letra_a = True
        quant = quant + 1

if letra_a == True:
    print(f"Sua palavra possui {quant} letras A")
else:
    print("Sua palavras não possui a letra A")

