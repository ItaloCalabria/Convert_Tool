def converter_moeda(valor, taxa):
    return valor * taxa

def conversor():
    print("Bem-vindo ao Conversor de Moedas!")
    print("1. Real para Dólar")
    print("2. Real para Euro")
    print("3. Dólar para Real")
    print("4. Euro para Real")

    escolha = input("Escolha a conversão (1/2/3/4): ")

    valor = float(input("Digite o valor: "))

    if escolha == '1':
        taxa_dolar = 5.30  # Taxa de conversão Real para Dólar
        resultado = converter_moeda(valor, taxa_dolar)
        print(f"R$ {valor} equivale a ${resultado:.2f}")
    elif escolha == '2':
        taxa_euro = 6.20  # Taxa de conversão Real para Euro
        resultado = converter_moeda(valor, taxa_euro)
        print(f"R$ {valor} equivale a €{resultado:.2f}")
    elif escolha == '3':
        taxa_dolar = 5.30  # Taxa de conversão Dólar para Real
        resultado = converter_moeda(valor, 1 / taxa_dolar)
        print(f"${valor} equivale a R${resultado:.2f}")
    elif escolha == '4':
        taxa_euro = 6.20  # Taxa de conversão Euro para Real
        resultado = converter_moeda(valor, 1 / taxa_euro)
        print(f"€{valor} equivale a R${resultado:.2f}")
    else:
        print("Opção inválida.")

conversor()
