print('Total Consumido')  # Título do programa

from datetime import datetime

data_hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print(f'{data_hora_atual}')
input('Digite o número da mesa: ')


def obter_quantidade(nome):
    while True:
        try:
            return int(input(f'{nome}: '))
        except ValueError:
            print("Digite um número válido.")


# O programa pede ao usuário a quantidade consumida para cada item
print(f'\nDigite a quantidade consumida para cada item - apenas números:')
hamburguer = obter_quantidade('Hambúrguer')
cheeseburguer = obter_quantidade('Cheeseburguer')
fritas = obter_quantidade('Fritas')
refrigerante = obter_quantidade('Refrigerante')
milkshake = obter_quantidade('Milkshake')

# E pede ao usuário que confira as quantidades antes de prosseguir. É obrigatório que o usuário interaja com o programa 
# através dos comandos "ok" ou "voltar" para que as próximas ações aconteçam corretamente.
while True:
    print(f'\nQuantidade consumida: \n{hamburguer} Hambúrgueres '
          f'\n{cheeseburguer} Cheeseburgueres \n{fritas} Fritas '
          f'\n{refrigerante} Refrigerantes, \n{milkshake} Milkshakes')

    resposta = input(f"\nDigite 'ok' se as quantidades estão corretas ou 'voltar' para reinserir: ").strip().lower()
    if resposta == 'ok':
        break
    else: # Caso tenha inserido alguma quantidade errada, o programa permite que ele reinsira as informações sem a 
        # necessidade de ser reiniciado.
        print("Digite novamente a quantidade: ")
        hamburguer = obter_quantidade('Hambúrguer')
        cheeseburguer = obter_quantidade('Cheeseburguer')
        fritas = obter_quantidade('Fritas')
        refrigerante = obter_quantidade('Refrigerante')
        milkshake = obter_quantidade('Milkshake')
        
# Ao comando positivo do usuário, todas as ações seguintes acontecem de forma automática:

# A partir da informação fornecida acima, o programa consulta os dados dos itens do cardápio
preco_hamburguer = 8.00
preco_cheeseburguer = 9.50
preco_fritas = 5.50
preco_refrigerante = 5.00
preco_milkshake = 8.00

# consulta a fórmula do valor total gasto para cada item consumido
total_hamburguer = hamburguer * preco_hamburguer
total_cheeseburguer = cheeseburguer * preco_cheeseburguer
total_fritas = fritas * preco_fritas
total_refrigerante = refrigerante * preco_refrigerante
total_milkshake = milkshake * preco_milkshake

# e a do valor total da compra
total_compra = total_hamburguer + total_cheeseburguer + total_fritas + total_refrigerante + total_milkshake

# então exibe o valor total consumido para cada item
print(f'\nConsumidos: \n{hamburguer} Hambúrgueres: R${total_hamburguer:.2f} '
      f'\n{cheeseburguer} Cheeseburgueres: R${total_cheeseburguer:.2f} '
      f'\n{fritas} Fritas: R${total_fritas:.2f} '
      f'\n{refrigerante} Refrigerantes: R${total_refrigerante:.2f} '
      f'\n{milkshake} Milkshakes: R${total_milkshake:.2f}')

# E valor total da compra
print(f'\nTotal da compra: R${total_compra:.2f}')

# Por último, o programa exibe o cardápio para que o valor de cada item possa ser conferido individualmente pelo cliente
print(f"\n \nCardápio: \nHamburguer.....R$8,00 \nCheeseburguer.....R$9,50 "
      f"\nFritas.....R$5,50 \nRefrigerante.....R$5,00 \nMilkshake.....R$8,00")
