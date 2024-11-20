print('Cálculo Salário \n \nQuanto você recebe por hora trabalhada?')
valor = float(input('Digite somente valor sem "R$": ').replace(',','.'))

# um intervalo de horas inteiro ou "quebrado", seguido ou não do indicativo 'h', mas como completa iniciante em
# programação eu realmente não sabia como fazer isso
def converter_horas(entrada):
    entrada = entrada.strip().lower().replace('h', '')
    if ':' in entrada:
        horas, minutos = map(float, entrada.split(':'))
        return horas + (minutos / 60)  # Converte minutos para fração de hora
    else:
        return float(entrada)  # Se for só horas

#O programa pede ao usuário que digite quantas horas trabalhou no mês vigente. Graças ao código anterior, ele pode 
# fornecer esta informação como horas inteiras ou como horas e minutos específicos, desde que, horas e minutos estejam 
# separados por :
horas_input = input('Agora digite quantas horas você trabalhou este mês: ')
horas = converter_horas(horas_input)

# Com base nas informações fornecidas o programa realiza um cálculo simples entre valor e horas
salario = valor * horas
# Então reexibe ao usuário as informações fornecidas por ele, o processo de cálculo e uma mensagem informando o valor 
# estimado a ser recebido.
print(f"Você digitou R${valor} por hora trabalhada e {horas} horas trabalhadas \n{valor} * {horas} = {salario}")
print(f"Você deve receber R${salario}")

