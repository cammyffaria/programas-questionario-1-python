print("Calcule seu IMC") # e casos de programas com operadores matemáticos acho completamente pedagógico que a pessoa
# seja informada sobre qual a finalidade do cálculo que será executado

# Logo em seguida, começa a interação do programa com o usuário:
peso = float(input('Digite seu peso: ').replace (',','.')) #na maioria dos casos o usuário colocara seu peso da forma
# que apareceu na balança com todas as casas decimais possíveis. o float garantirá que o programa funcione com qualquer
# número inteiro ou decimal. O replace permitirá que o programa funcione corretamente quer a pessoa opte por usar
# vírgula ou ponto para separar as casas decimais.

altura = float(input('Digite sua altura em metros: ').replace(',','.')) # quanto à altura, acontece do mesmo modo

# O programa então calculará o IMC do usuário:
imc = peso/(altura ** 2)

#O resultado impresso será o valor do IMC do usuário.
print('Seu IMC é: ', imc)

# Adicional: Não foi pedido na tarefa, mas optei por mostrar ao usuário se está dentro, abaixo, ou acima do peso visto
# que apenas saber o valor do imc não vai sanar sua dúvida de forma prática, já que provavelmente terá que pesquisar o
# resultado no google para obter esta informação. Lembrando que em caso de atletas ou pessoas comuns que treinam força
# regularmente (exemplo: praticantes de musculação, yoga, calistenia, gisnástica ritmica ou pilates) o IMC é um cálculo
# impreciso pois é muito provável que o resultado trazido seja equivalente à obesidade, mesmo que o usuário apresente
# visual atlético; neste caso o recomendado é a utilização de uma balança de bioimpedância.
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9: #Elif é muito fácil de lembrar pois na Turquia é um nome próprio feminino, mas, dentro do
# python seria o equivalente a "else if", e basicamente indica que existem mais de duas possibilidades determináveis
# em alguma situação.
    print("Peso normal")
elif 25 <= imc < 29.9: # '<= numero < número' indica um intervalo limite entre dois elifs
    print("Sobrepeso")
else:
    print("Obesidade")

