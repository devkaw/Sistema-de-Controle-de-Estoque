dic = {}
while True:
    print('Bem vindo ao Sistema de Controle de Estoque, aqui você poderá eliminar os estoques, adicionar estoque e ver o estoque existente.')
    print('------------------------------------------------------------------------------------------------------------------------------------')
    decisao = int(input('''
1) Adicionar estoque
2) Ver estoque existente
3) Eliminar estoque
4) Fechar o programa
                        
'''))
    print('------------------------------------------------------------------------------------------------------------------------------------')
    if decisao == 1:
        decisao3 = int(input('''
O que você deseja fazer?

1) Registrar um novo produto e seu estoque
2) Adicionar estoque a um produto já existente
                             
'''))
        print('------------------------------------------------------------------------------------------------------------------------------------')
        if decisao3 == 1:
            nomedoproduto = input('Digite o nome do produto que você deseja adicionar: ')
            quantidadedoproduto = int(input('Digite a quantidade de estoque do produto informado: '))
            dic[nomedoproduto] = quantidadedoproduto
            print('------------------------------------------------------------------------------------------------------------------------------------')

        if decisao3 == 2:
            nomedoproduto1 = input('Digite o nome do produto que você deseja alterar o estoque, exatamente como você o registrou: ')
            quantidadedoproduto1 = int(input('Digite a quantidade de estoque atualizada do produto informado: '))
            dic[nomedoproduto1] = quantidadedoproduto1
            print('------------------------------------------------------------------------------------------------------------------------------------')


    if decisao == 2:
        print(f'''
O estoque atual é:
{dic}
''')    
        print('------------------------------------------------------------------------------------------------------------------------------------')
    

    if decisao == 3:
        decisao2 = int(input('''
O que você deseja fazer?

1) Deletar um tipo de produto e todo o seu estoque
2) Deletar uma certa quantidade de estoque de um certo produto
                             
'''))

        
        print('------------------------------------------------------------------------------------------------------------------------------------')

        if decisao2 == 1:
            nomedoprodutopradeletar = input('Qual é o produto que você deseja deletar? Coloque o nome do produto exatamente igual a como você o registrou: ')
            dic.pop(nomedoprodutopradeletar)
            print('------------------------------------------------------------------------------------------------------------------------------------')

        if decisao2 == 2:
            nomedoprodutoparadeletar = input('Qual é o produto que você deseja deletar uma certa quantia? Coloque o nome do produto exatamente igual a como você o registrou: ')
            quantidadedoprodutoparadeletar = int(input('Quantas unidades desse produto deseja remover? '))
            dic[nomedoprodutoparadeletar] -= quantidadedoprodutoparadeletar
            print('------------------------------------------------------------------------------------------------------------------------------------')

    if decisao == 4:
        print('Obrigado por usar o meu programa!')
        print('------------------------------------------------------------------------------------------------------------------------------------')
        break

input('Pressione qualquer tecla para fechar: ')