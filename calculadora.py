from art import tprint
tprint("CALCULADORA", font="block")


def mais(um, dois):
    return um + dois

def menos(um, dois):
    return um - dois

def vezes(um, dois):
    return um * dois

def dividir(um, dois):
    return um / dois

dicionario_operacao = {
    "+": mais,
    "-": menos,
    "*": vezes,
    "/": dividir
}

def calculadora():
    continuar = True
    num1 = float(input("Escolha o primeiro número: "))

    for keys in dicionario_operacao:
        print(keys)
    while continuar:
        operacao = input("Escolha uma operação: ").lower().strip()
        num2 = float(input("Escolha o proximo número: "))
        resultado = dicionario_operacao[operacao]
        resposta = resultado(num1, num2)
        print(f"{num1} {operacao} {num2} = {resposta}.")

        if input("Você deseja continuar? (sim/nao): ").strip().lower() == "sim":
            num1 = resposta
        else:
            continuar = False
            if input("Deseja iniciar nova operação? (sim/nao): ") == "sim":
                print("Comece sua nova operação.")
                calculadora()
            else:
                break

calculadora()
