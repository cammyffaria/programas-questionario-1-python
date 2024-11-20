print('Running Tracker \n') # Título do programa

# A ação do programa acontece de forma interativa com o usuário. É possível perceber por meio do travessão, utilizado 
# para indicar uma fala nos textos da língua portuguesa:
print('- Quantos metros você correu hoje?')

# Então o programa converte a distância corrida pelo usuário em quilômetros por meio de uma operação matemática simples:
def metros_para_quilometros(metros):
    return metros / 1000

metros = float(input('Insira em números: ').replace(',', '.')) # A linha considera que o usuário possa digitar um número
# decimal usando ponto ou vírgula
quilometros = metros_para_quilometros(metros)

#Por fim, o programa congratula o usuário por seu desempenho e mostra a quilometragem percorrida por ele em números
# inteiros ou decimais.
if quilometros.is_integer():
    print(f"{metros} \nParabéns!!! Você correu {int(quilometros)} km hoje.")
else:
    print(f"{metros} \nParabéns!!! Você correu {quilometros:.2f} km hoje.")