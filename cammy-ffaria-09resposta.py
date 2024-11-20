print('Calculadora de �rea') # T�tulo do programa

#O programa pede que o usu�rio insira as informa��es relevantes para que o c�lculo da �rea da sala seja efetuado.
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Digite um n�mero v�lido.")

largura = obter_numero('\nDigite a largura da sala: ')
comprimento = obter_numero('Digite o comprimento da sala: ') 


# O c�lculo � feito com base nas informa��es inseridas pelo usu�rio
area = largura * comprimento # Note que o c�lculo do programa s� funciona com salas de formato regular, por exemplo,
# salas quadradas ou retangulares, pois s� pede a inser��o da metragem de duas das paredes.

# Por fim, o programa exibe uma mensagem personalizada com a �rea total da sala para o usu�rio
print(f"\nA �rea total da sala � de {area}m�")