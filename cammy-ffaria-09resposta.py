print('Calculadora de Área') # Título do programa

#O programa pede que o usuário insira as informações relevantes para que o cálculo da área da sala seja efetuado.
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Digite um número válido.")

largura = obter_numero('\nDigite a largura da sala: ')
comprimento = obter_numero('Digite o comprimento da sala: ') 


# O cálculo é feito com base nas informações inseridas pelo usuário
area = largura * comprimento # Note que o cálculo do programa só funciona com salas de formato regular, por exemplo,
# salas quadradas ou retangulares, pois só pede a inserção da metragem de duas das paredes.

# Por fim, o programa exibe uma mensagem personalizada com a área total da sala para o usuário
print(f"\nA área total da sala é de {area}m²")