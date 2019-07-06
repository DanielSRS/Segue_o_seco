# *******************************************************************************
# Autor: Daniel Santa Rosa Santos
# Componente Curricular: Algoritmos I
# Concluido em: 05/07/2019
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor,tais como provindos de livros e
# apostilas,e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************

from copy import deepcopy

# ----------------------------------------------------------------------------------------------------------------------
#                                      Inicializando variáveis necessárias
# ----------------------------------------------------------------------------------------------------------------------
tipo_de_aparelho = 0
adicionar_setor = 'x'
nome_do_aparelho = 'x'
contador_de_setores = 1
mais_setores = True  # Controla a adição de mais setores
setores = []  # Armazena os dados coletados
setor_auxiliar = []
aparelho_auxiliar = []
taxa = 0
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                   Loop para contabilizar os dados de n setores
# ______________________________________________________________________________________________________________________

while mais_setores:
    # ------------------------------------------------------------------------------------------------------------------
    #                                 Loop para contabilizar todos os tipos de aparelho
    # __________________________________________________________________________________________________________________

    while tipo_de_aparelho < 5:
        # ______________________________________________________________________________________________________________

        # --------------------------------------------------------------------------------------------------------------
        #                                      Alterna entre os tipos de aparelhos
        # --------------------------------------------------------------------------------------------------------------
        if tipo_de_aparelho == 0:
            nome_do_aparelho = 'ar-condicionados'
        elif tipo_de_aparelho == 1:
            nome_do_aparelho = 'Computadores'
        elif tipo_de_aparelho == 2:
            nome_do_aparelho = 'geladeiras'
        elif tipo_de_aparelho == 3:
            nome_do_aparelho = 'lampadas'
        elif tipo_de_aparelho == 4:
            nome_do_aparelho = 'televisores'
        # ______________________________________________________________________________________________________________

        # --------------------------------------------------------------------------------------------------------------
        #                                       Recolhe dados do aparelho em contexto
        # --------------------------------------------------------------------------------------------------------------
        while True:
            quantidade_de_aparelhos = input(
                '\n\nQuantos {} existem no {}° setor: '.format(nome_do_aparelho, contador_de_setores))
            if quantidade_de_aparelhos.isnumeric():
                break
        if int(quantidade_de_aparelhos) > 0:
            aparelho_auxiliar.append(int(quantidade_de_aparelhos))
            while True:  # tratando entradas invalidas
                potencia_do_aparelho = input('Digite a potência do aparelho: ')
                if potencia_do_aparelho.replace('.', '').isnumeric():
                    break
            aparelho_auxiliar.append(float(potencia_do_aparelho))  # adiciona a lista

            while True:  # tratando entradas invalidas
                horas_de_uso_por_dia_do_aparelho = input('Digite a quantidade de horas de uso por dia do aparelho: ')
                if horas_de_uso_por_dia_do_aparelho.isnumeric() and int(horas_de_uso_por_dia_do_aparelho) <= 24:
                    break
            aparelho_auxiliar.append(int(horas_de_uso_por_dia_do_aparelho))  # adiciona a lista

            while True:  # tratando entradas invalidas
                dias_de_uso_do_aparelho_por_mes = input('Digite a quantidade de dias de uso por mês do aparelho: ')
                if dias_de_uso_do_aparelho_por_mes.isnumeric() and int(dias_de_uso_do_aparelho_por_mes) <= 30:
                    break
            aparelho_auxiliar.append(int(dias_de_uso_do_aparelho_por_mes))  # adiciona a lista
        else:
            aparelho_auxiliar = [0, 0, 0, 0]
        tipo_de_aparelho = tipo_de_aparelho + 1  # Passa para o próximo tipo de aparelho
        setor_auxiliar.append(deepcopy(aparelho_auxiliar))  # Copia os dados dos aparelhos para lista de setor auxiliar
        aparelho_auxiliar[:] = []  # Limpa a lista auxiliar
        # ______________________________________________________________________________________________________________
    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                              Adiciona um novo setor
    # ------------------------------------------------------------------------------------------------------------------
    setores.append(deepcopy(setor_auxiliar))
    setor_auxiliar[:] = []  # Limpa a lista auxiliar
    while adicionar_setor != 'A' and adicionar_setor != 'a' and adicionar_setor != 'B' and adicionar_setor != 'b':
        print('----------------------| Deseja adicionar mais um setor? |----------------------\n\n')
        print('[A] - Para adicionar outro setor à contagem')
        print('[B] - Para finalizar as contagens\n\n')
        adicionar_setor = input('Digite sua escolha: ')
        if adicionar_setor == 'A' or adicionar_setor == 'a':
            contador_de_setores = contador_de_setores + 1
            tipo_de_aparelho = 0  # Permite ao programa executar novamente o primeiro laço de repetição
        elif adicionar_setor == 'B' or adicionar_setor == 'b':
            mais_setores = False
        else:
            print('Opção inválida, digite novamente!\n\n')
    adicionar_setor = 'x'  # Permite ao programa voltar a executar esse laço quando houver mais um setor
    # __________________________________________________________________________________________________________________

# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                              Realiza os calculos de consumo (em KWh)
# ----------------------------------------------------------------------------------------------------------------------
tamanho_lista = len(setores)  # verifica quantos setores foram inseridos

for contador in range(tamanho_lista):  # Calcula o consumo em kwh em cada tipo de aparelho
    # print(setores[contador])
    for contador_dois in range(5):  # esse for está na lista de um setor, cada setor tem 5 aparelhos (também litas)
        kwh_auxiliar = setores[contador][contador_dois][0] * (setores[contador][contador_dois][1]/1000) \
            * setores[contador][contador_dois][2] * setores[contador][contador_dois][3]
        # print('consumo aparelho')
        # print(kwh_auxiliar)
        setores[contador][contador_dois].append(kwh_auxiliar)  # adiciona consumo do aparelho ao final de sua lista

kw_setor = 0
for contador in range(tamanho_lista):  # Calcula o consumo em kwh em cada  setor
    for contador_dois in range(5):  # esse for está na lista de um setor, cada setor tem 5 aparelhos (também litas)
        kw_setor += setores[contador][contador_dois][4]
    setores[contador].append(kw_setor)
    kw_setor = 0
    # print(setores[contador][5])

kw_total = 0
for contador in range(tamanho_lista):  # Soma o consumo dos setores para encontrar o consumo total
    kw_total += setores[contador][5]
setores.append(kw_total)
# print('\n\n\nTotal de kwh: {}'.format(kw_total))
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                    Definindo a taxa utilizada para os calculos de gastos
# ----------------------------------------------------------------------------------------------------------------------
if setores[tamanho_lista] < 31:  # Consumo em KWh
    taxa = 0.17512250
elif 31 <= setores[tamanho_lista] <= 100:
    taxa = 0.30021000
elif 101 <= setores[tamanho_lista] >= 149.99:
    taxa = 0.45031500
else:
    taxa = 0.50035000
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                    Realiza os calculos de gastos (em R$)
# ----------------------------------------------------------------------------------------------------------------------
for contador in range(tamanho_lista):  # Calcula o consumo em kwh em cada tipo de aparelho
    # print(setores[contador])
    for contador_dois in range(5):
        RS_auxiliar = setores[contador][contador_dois][4] * taxa  # calcula o valor gasto ppo cada parelho
        setores[contador][contador_dois].append(RS_auxiliar)  # adiciona gasto do aparelho ao final de sua lista
        print('Gasto do aparelho: {}'.format(RS_auxiliar))

RS_setor = 0
for contador in range(tamanho_lista):  # Calcula o gasto em R$ em cada  setor
    for contador_dois in range(5):
        RS_setor += setores[contador][contador_dois][5]
        setores[contador].append(RS_setor)
    RS_setor = 0

RS_total = 0
for contador in range(tamanho_lista):  # Soma o gasto umo dos setores para encontrar o gasto total
    RS_total += setores[contador][6]
setores.append(RS_total)
print('\n\nGasto total: {}'.format(RS_total))

gasto = setores[tamanho_lista + 1] * 0.27 + setores[tamanho_lista + 1] * 0.0165 + (
    setores[tamanho_lista + 1] * 0.0761) + setores[tamanho_lista + 1]  # calcula gasto com impostos
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                          Exibição dos resultados finais
# ----------------------------------------------------------------------------------------------------------------------
for contador in range(tamanho_lista):
    print('{}° setor:'.format(contador + 1))
    print('\tar condicionado:   {} kwh'.format(setores[contador][0][4]))
    print('\t                   R$ {}'.format(round(setores[contador][0][5], 2)))  # imprime o valor arredondado
    print('\tcompputadores:     {} kwh'.format(setores[contador][1][4]))
    print('\t                   R$ {}'.format(round(setores[contador][1][5], 2)))  # imprime o valor arredondado
    print('\tgeladeiras:        {} kwh'.format(setores[contador][2][4]))
    print('\t                   R$ {}'.format(round(setores[contador][2][5], 2)))  # imprime o valor arredondado
    print('\tlampadas:          {} kwh'.format(setores[contador][3][4]))
    print('\t                   R$ {}'.format(round(setores[contador][3][5], 2)))  # imprime o valor arredondado
    print('\ttelevisores:       {} kwh'.format(setores[contador][4][4]))
    print('\t                   R$ {}'.format(round((setores[contador][4][5]), 2)))  # imprime o valor arredondado

print('\n\n\nComsumo total em KWh: {}'.format(setores[tamanho_lista]))
print('Gasto total: R$ {}'.format(round(setores[tamanho_lista + 1], 2)))
print('Valor da conta de luz: R$ {}'.format(round(gasto, 2)))
# ______________________________________________________________________________________________________________________
 