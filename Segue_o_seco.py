from copy import deepcopy

# ----------------------------------------------------------------------------------------------------------------------
#                                      Inicializando variáveis necessárias
# ----------------------------------------------------------------------------------------------------------------------
tipo_de_aparelho = 0
adicionar_setor = 'x'
nome_do_aparelho = 'x'
contador_de_setores = 1
mais_setores = True
setores = []
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
        quantidade_de_aparelhos = int(input(
            '\n\nQuantos {} existem no {}° setor: '.format(nome_do_aparelho, contador_de_setores)))
        aparelho_auxiliar.append(quantidade_de_aparelhos)
        if quantidade_de_aparelhos > 0:
            potencia_do_aparelho = float(input('Digite a potência do aparelho: '))
            aparelho_auxiliar.append(potencia_do_aparelho)  # adiciona a lista
            horas_de_uso_por_dia_do_aparelho = float(input('Digite a quantidade de horas de uso por dia do aparelho: '))
            aparelho_auxiliar.append(horas_de_uso_por_dia_do_aparelho)  # adiciona a lista
            dias_de_uso_do_aparelho_por_mes = float(input('Digite a quantidade de dias de uso por mês do aparelho: '))
            aparelho_auxiliar.append(dias_de_uso_do_aparelho_por_mes)  # adiciona a lista
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
tamanho_lista = len(setores)  #verifica quantos setores foram inseridos

for contador in range (tamanho_lista):  #Calcula o consumo em kwh em cada tipo de aparelho
    # print(setores[contador])
    for contador_dois in range (5):  #esse for esta na liista de um setor, cada setor tem 5 aparehos (cada aparelho e uma lista)
        kwh_auxiliar = setores[contador][contador_dois][0] * (setores[contador][contador_dois][1]/1000) * setores[contador][contador_dois][2]  \
            * setores[contador][contador_dois][3]
        # print('consumo aparelho')
        # print(kwh_auxiliar)
        setores[contador][contador_dois].append(kwh_auxiliar)  # adiciona consumo do aparelho ao final de sua respectiva lista


kw_setor = 0
for contador in range (tamanho_lista):  # Calcula o consumo em kwh em cada  setor
    for contador_dois in range (5):  # esse for esta na liista de um setor, cada setor tem 5 aparehos (cada aparelho e uma lista)
        kw_setor += setores[contador][contador_dois][4]
    setores[contador].append(kw_setor )
    kw_setor = 0
    # print(setores[contador][5])


kw_total = 0
for contador in range (tamanho_lista):  # Soma o consumo dos setores para encontrar o consumo total
    kw_total += setores[contador][5]
setores.append(kw_total)
# print('\n\n\nTotal de kwh: {}'.format(kw_total))
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                    Definindo a taxa utilizada para os calculos de gastos
# ----------------------------------------------------------------------------------------------------------------------
  if setores[tamanho_lista] <= 50:  # Consumo em KW
    if setores[tamanho_lista] < 31:
        taxa = 0.18842532
    else:
        taxa = 0.32301484
  elif 50 < setores[tamanho_lista] <= 149.99:
    if 50 < setores[tamanho_lista] < 101:
        taxa = 0.44187518
    else:
        taxa = 0.25776052
  elif setores[tamanho_lista] >= 150:
    if setores[tamanho_lista] > 220:
        taxa = 0.75879587
    if 149.99 < setores[tamanho_lista] <= 220:
        taxa = 0.26557855
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                          Exibição dos resultados finais
# ----------------------------------------------------------------------------------------------------------------------
for contador in range (tamanho_lista): 
    print('{}° setor:'.format(contador + 1))
    print('\tar condicionado: {} kwh'.format(setores[contador][0][4]))
    print('\tcompputadores: {} kwh'.format(setores[contador][1][4]))
    print('\tgeladeiras: {} kwh'.format(setores[contador][2][4]))
    print('\tlampadas: {} kwh'.format(setores[contador][3][4]))
    print('\ttelevisores: {} kwh \n'.format(setores[contador][4][4]))

print('\n\n\nComsumo total em KWh: {}'.format(setores[tamanho_lista]))
# ______________________________________________________________________________________________________________________
