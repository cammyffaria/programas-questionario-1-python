print('Conversor de Temperatura \n') # Título do programa

# O usuário é pedido para digitar a temperatura a qual deseja converter
celcius = float(input('Digite a temperatura em graus Celcius - Utilize somente números: '))

# O programa então realiza o cálculo de conversão de uma temperatura para outra
fahreneit = celcius * 1.8 + 32 #optei por utilizar a forma decimal apenas para não confundir com uma divisão caso eu 
# precise reler o código algum dia

# O cálculo realizado e o resultado da conversão são exibidos para o usuário.
print(f"{celcius} * 1.8 + 32 \n{celcius} graus Celcius equivale a {fahreneit} Graus Fahreneit")

