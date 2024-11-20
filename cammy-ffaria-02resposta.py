print('Inteiro ou decimal?')

# Solicitar ao usuário que digite um número natural qualquer
entrada = input('Digite um número: ')

# Caso opte por digitar um número com casas decimais, é possível que o usuário utilize vírgula ou ponto para separá-las
# do número inteiro
entrada = entrada.replace(',','.') # 'replace' atuará como um tradutor que transformará o primeiro valor em segundo
# valor, ou seja, neste caso em específico traduzirá a possível vírgula digitada em ponto e, a partir deste ponto,
# reconhecerá o número digitado como decimal. Não funcionou quando tentei colocar ('.', ',') mas sinceramente, não
# entendo por quê.

# O código agora tentará reconhecer se o número digitado é decimal ou inteiro
try: # denota uma ação experimental
    numero = int(entrada) # int(entrada) representa a inserção de um número inteiro qualquer
    tipo = 'inteiro'
except ValueError: # Caso falhe, tentará converter converter o número inteiro para decimal # ValueError é um código
    # obrigatório dentro de ações experimentais no python e, indicará o procedimento a ser executado caso o comando
    # venha falhar.
    try:
        numero = float(entrada) #float (ponto flutuante), é basicamente o diferencial entre número inteiro e número
        # decimal
        tipo = 'decimal'
    except ValueError:
        numero = None # Este código reconhece que letras e caracteres diferenciais não podem ser números inteiros ou
        # decimais, portanto são uma entrada inválida.
        tipo = 'inválido' # Condicional caso a entrada não seja um número. durante o run, a veracidade foi experimentada
        # com meu segundo nome 'Camila', e, com um '@'.

# Mensagem para o usuário
if numero is not None: # if é naturalmente a condição 'se'. 'is not' neste código representa uma condição verdadeira;
    # que o valor digitado é de fato um número inteiro ou decimal. Acredito que em alguns casos o operador verdadeiro
    # posssa ser "is", mas ainda não sei programar bem o suficiente para ter certeza.
    print('O número digitado foi:', numero)
    print(f'Variável: {tipo}') # neste trecho em específico pedi para o chat gpt me ajudar a corrigir para que o código
    # funcionasse e me explicasse o que foi feito. com base em sua explicação: "f" indica uma formatação de string e
    # '{}' é usado para armazenar dados e coleções em elementos únicos. Basicamente, se por exemplo, tivermos
    # "casa = amarela", "casa = palha", "casa = aquário", {} considerará que em resumo "casa" pode ser amarela, de palha
    # ou um aquário; dependerá de algum valor especificado anteriormente.
else: # indica a ação de execução do programa caso a condição seja falsa, ou seja, (neste caso) se em vez de somente
    # algum número inteiro ou natural foi digitado alguma letra ou caractere especial
    print("Valor digitado não é um número válido.")
