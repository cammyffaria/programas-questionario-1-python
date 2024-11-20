print('Calcule sua nota final')

# O programa requerirá cada uma das notas relevantes para se fazer o cálculo da média:
a = float(input('Digite nota 01: ').replace (',','.'))
b = float(input('Digite nota 02: ').replace (',','.'))
c = float(input('Digite nota 03: ').replace (',','.'))
d = float(input('Digite nota 04: ').replace (',','.'))

# Então fará a soma das quatro notas relevantes para o cálculo da média e, em seguida, uma divisão para definir a média
# simples entre os valores. Neste caso em específico, dividirá a soma por quatro, pois foram usados quatro números base
# para definir a média em questão:
media = (a+b+c+d)/4

print('Sua média final é: {:.1f}'.format(media)) # o código após o comando print formata as casas decimais para que
    # apareça apenas uma casa decimal após a vírgula