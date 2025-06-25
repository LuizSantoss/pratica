import pandas as pd
import matplotlib.pyplot as plt
import os
from ydata_profiling import ProfileReport


dados_func = pd.read_csv('tempo_salarios.csv')


def mensagem_saida():
    print('\nOperação finalizada\n')
    input('Pressione ENTER para voltar ao menu de seleção\n')
    return menu()

def media_salarios():
    while True:
        resposta = input('Deseja visualizar a média dos salários? (s/n), "n" retorna ao menu de seleção:\n').lower().strip()
        if resposta == 's':
            print('A média atual dos salários é: \n')
            print(f'{dados_func["Salário (R$)"].mean():.2f}')
            
            mensagem_saida()
        elif resposta == 'n':
            print('Retornando ao menu de seleção\n\n')
            return menu()
        else:
            print('\nDigite uma resposta válida, "s" ou "n"')

def mediana_salarios():
    while True:
        resposta_mediana = input('Deseja visualizar a mediana dos salários? (s/n), "n" retorna ao menu de seleção:\n').lower().strip()
        if resposta_mediana == 's':
            print('\nA mediana dos salários é: ')
            print(dados_func["Salário (R$)"].median())
            
            mensagem_saida()
        elif resposta_mediana == 'n':
            print('Retornando ao menu de seleção\n\n')
            return menu()
        else:
            print('\nDigite uma resposta válida, "s" ou "n"')

def filtro_salario():
    while True:
        questionamento = input('Deseja filtrar por Menor que, ou Maior que ? (Maior/Menor) \nPara sair digite "sair":\n').strip().lower()
        if questionamento == 'maior':
            try:
                valor_flltro = float(input('Insira o valor do filtro: R$'))
            except ValueError:
                print('Insira um valor válido')

            print('\nValores filtrados:\n')
            print(f'{dados_func.loc[dados_func["Salário (R$)"]>valor_flltro]}')
            print('\nBusca finalizada\n')
            
            input('Aperte ENTER para voltar\n')
            return filtro_salario()

        elif questionamento == 'menor':
            try:
                valor_flltro = float(input('Insira o valor do filtro: R$'))
            except ValueError:
                print('Insira um valor válido')
            
            print('\nValores filtrados\n')
            print(f'{dados_func.loc[dados_func["Salário (R$)"]<valor_flltro]}')
            print('\nBusca finalizada\n')
            
            input('Aperte ENTER para voltar\n')
            return filtro_salario() 
        
        elif questionamento == 'sair':
            return menu()
        else:
            print('\nSelecione o tipo de filtro!\n')

def variacao_salario():
    print(f'\nExibindo a variância dos salários: {dados_func["Salário (R$)"].var():.2f}')
    
    mensagem_saida()

def desvio_padrao():
    print(f'Exibindo o desvio padrão dos salários: {dados_func["Salário (R$)"].std():.2f}')
   
    mensagem_saida()

def graficos():
    while True:
        tipo_de_grafico = input('Qual tipo de grádico deseja ver ? (Pontos/Barras)\npara voltar digite "sair":\n').lower().strip()
        if tipo_de_grafico == 'sair':
            input('\nPressione ENTER para voltar para o menu de seleção\n')
            return menu()

        if tipo_de_grafico == 'pontos':
            print('\nO gráfico de pontos dos dados: \n')

            dados_func.plot(kind='scatter', x='Tempo de Serviço (anos)', y='Salário (R$)')
            plt.show()

            print('\nGráfico exibido\n')
            input('Pressione ENTER para voltar \n')
            return graficos()

        elif tipo_de_grafico == 'barras':
            print('O gráfico de barras dos dados: \n')
            
            dados_func.plot(kind='bar', x='Tempo de Serviço (anos)', y='Salário (R$)')
            plt.show()            

            print('\nGráfico exibido\n')
            input('Pressione ENTER para voltar \n')
            return graficos()

        else:
            print('\nDigite um gráfico válido!\n')

def buscar_salario():
    selecao = {
        'Ana Souza': dados_func['Salário (R$)'][0],
        'Carlos Almeida': dados_func['Salário (R$)'][1],
        'Mariana Oliveira': dados_func['Salário (R$)'][2],
        'Lucas Pereira': dados_func['Salário (R$)'][3],
        'Fernanda Costa': dados_func['Salário (R$)'][4],
        'Roberto Silva': dados_func['Salário (R$)'][5],
        'Patrícia Lima': dados_func['Salário (R$)'][6],
        'João Santos': dados_func['Salário (R$)'][7],
        'Raquel Ferreira': dados_func['Salário (R$)'][8],
        'Gabriel Souza': dados_func['Salário (R$)'][9],
        'Paula Martins': dados_func['Salário (R$)'][10],
        'Ricardo Oliveira': dados_func['Salário (R$)'][11],
        'Camila Rocha': dados_func['Salário (R$)'][12],
        'André Costa': dados_func['Salário (R$)'][13],
        'Beatriz Dias': dados_func['Salário (R$)'][14],
        'Felipe Santos': dados_func['Salário (R$)'][15],
        'Isabela Martins': dados_func['Salário (R$)'][16],
        'Daniel Souza': dados_func['Salário (R$)'][17],
        'Larissa Silva': dados_func['Salário (R$)'][18],
        'Marcos Oliveira': dados_func['Salário (R$)'][19],
        'Carolina Alves': dados_func['Salário (R$)'][20],
        'Gustavo Pereira': dados_func['Salário (R$)'][21],
        'Rafaela Mendes': dados_func['Salário (R$)'][22],
        'Felipe Lima': dados_func['Salário (R$)'][23],
        'Victor Costa': dados_func['Salário (R$)'][24],
        'Adriana Rocha': dados_func['Salário (R$)'][25],
        'Eduardo Santos': dados_func['Salário (R$)'][26],
        'Hugo Oliveira': dados_func['Salário (R$)'][27],
        'Tânia Souza': dados_func['Salário (R$)'][28],
        'Juliana Ferreira': dados_func['Salário (R$)'][29]
    }
    
    while True:
        seleciona = input('Digite o nome do funcionário que deseja buscar: \n para voltar digite "sair":\n')
        if seleciona == 'sair':
            input('\nPressione ENTER para voltar para o menu de seleção\n')
            return menu()
        elif seleciona not in selecao:
            print('\nFuncionário não encontrado, certifique-se de escrever o nome corretamente sem espaços adicionais e tente novamente')
        else:
            print(f'\nSalário do funcionário: {seleciona} é {selecao[seleciona]}')
            input('\nPressione ENTER para voltar\n')
            return buscar_salario()

def relatorio_html():
    while True:
        confirma = input('\nGerar relatório HTML ? (s/n, "n" volta para o menu):\n').lower().strip()
        if confirma == 's':
            if os.path.exists('Relatorio.html'):
                print('\nO relatório já existe')

            else:
                relatorio = ProfileReport(dados_func, title= 'Relatório de Salários', explorative = True)
                relatorio.to_file('Relatorio.html')
                print('\nRelatório .html gerado, voltando para o menu de seleção\n')
                return menu()
            
        elif confirma == 'n':
            input('\nPressione ENTER para voltar para o menu de seleção\n')
            return menu()
        
        else:
            print('\nInsira um valor válido! (s/n)')

def resumo_dados():
    print('\nExibindo o resumo dos dados')
    print(f'\nDados resumidos: \n{dados_func.describe()}')
    
    mensagem_saida()

def menu():
    while True:        
        print('- QUAL DADO DESEJA VISUALIZAR -')
        print('1 ----- Média de salários -----')
        print('2 ---------- Mediana ----------')
        print('3 ----- filtro de salário -----')
        print('4 --- Variação dos salários ---')
        print('5 ------- Desvio padrão -------')
        print('6 ---- Visualizar Gráficos ----')
        print('7 ------ Buscar salários ------')
        print('8 --- Gerar Relatório .HTML ---')
        print('9 ------ Resumo de dados ------')
        print('0 --------- Finalizar ---------')
        
        opcao = input('Selecione: ')

        if opcao == '1':
            return media_salarios()
        
        if opcao == '2':
            return mediana_salarios()
        
        if opcao == '3':
            return filtro_salario()
        
        if opcao == '4':
            return variacao_salario()
        
        if opcao == '5':
            return desvio_padrao()
        
        if opcao == '6':
            return graficos()
        
        if opcao == '7':
            return buscar_salario()
        
        if opcao == '8':
            return relatorio_html()
        
        if opcao == '9':
            return resumo_dados()
        
        if opcao == '0':
            print('Finalizando programa')
            break    

menu()
