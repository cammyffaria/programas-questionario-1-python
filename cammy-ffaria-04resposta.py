print('Some dois números inteiros ou reais quaisquer')  # O print é um reminder ao usuário sobre por que ele precisa da
# execução do programa

# Solicitar ao usuário que digite um número qualquer, podendo ser inteiro ou decimal:
a = float(input('Digite um número: ').replace(',', '.'))  # em seguida solicitar ao usuário que digite um
# segundo número para que o programa possa calcular a soma entre ambos:
b = float(input('Digite outro número: ').replace(',', '.'))  # Float dá ao usuário a liberdade de  poder
# executar o programa normalmente quer escolha um número inteiro ou decimal. O replace garantirá que a ação do
# programa seja executada quer o usuário digite um número inteiro ou decimal, independentemente de usar vírgula ou ponto
# para separar as casas inteiras de decimais.

soma = a + b  # a comando pede ao programa que some os dois números escolhidos pelo usuário

#Então mostrará ao usuário o processo utilizado para calcular, seguido do resultado que, pode ser um número inteiro ou
# decimal - depende da escolha de entradas do usuário.
print(f"{a} + {b} = {soma}") 
if soma.is_integer(): # em python, 'is_integer' faz uma verificação se a soma se resulta em um número inteiro.
    print(f"Seu resultado é: {int(soma)}")
else:
    print(f"Seu resultado é: {soma}") # então aparece para o usuário o resultado da soma.