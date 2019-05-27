from copy import deepcopy

# ----------------------------------------------------------------------------------------------------------------------
#                                      Inicializando variáveis necessárias
# ----------------------------------------------------------------------------------------------------------------------
tipo_de_aparelho = 0
contador_do_loop = 1
# outro_contador_de_loop = 0
adicionar_setor = 'x'
nome_do_aparelho = 'x'
contador_de_setores = 1
consumo_do_setor = 0  # vai ser apagado
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
        #                                     Alterna entre os tipos de aparelhos
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
        #                                          Recolhe dados do aparelho em contexto
        # --------------------------------------------------------------------------------------------------------------
        numero_de_aparelhos = int(input(
            '\n\nQuantos {} existem no {}° setor: '.format(nome_do_aparelho, contador_de_setores)))
        # while contador_do_loop <= numero_de_aparelhos:
        if numero_de_aparelhos == 0:
            consumo_do_aparelho = 0
        else:
            potencia_do_aparelho = float(input('Digite a potẽncia do {}° aparelho: '.format(contador_do_loop)))
            potencia_do_aparelho = potencia_do_aparelho/1000  # Converte de w para KW
            horas_de_uso_por_dia_do_aparelho = float(
                input('Digite a quantidade de horas por dia de uso do {}° aparelho: '.format(contador_do_loop)))
            dias_de_uso_do_aparelho_por_mes = float(
                input('Digite a quantidade de dias por mês de uso do {}° aparelho; '.format(contador_do_loop)))
            consumo_do_aparelho = (
                potencia_do_aparelho * horas_de_uso_por_dia_do_aparelho * dias_de_uso_do_aparelho_por_mes)
        aparelho_auxiliar.append(consumo_do_aparelho)
        consumo_do_setor = consumo_do_setor + consumo_do_aparelho  # ATENÇÂO
        # contador_do_loop = contador_do_loop + 1 ---Não é mais útil
        tipo_de_aparelho = tipo_de_aparelho + 1
        setor_auxiliar.append(deepcopy(aparelho_auxiliar))
        aparelho_auxiliar[:] = []  # Limpa a lista auxiliar
        # contador_do_loop = 1  # Reseta o loop para uso com outro tipo de aparelho  # Inútil
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
#                                      Definindo a taxa utilizada para os calculos
# ----------------------------------------------------------------------------------------------------------------------
if consumo_do_setor <= 50:  # Consumo em KW
    if consumo_do_setor < 31:
        taxa = 0.18842532
    else:
        taxa = 0.32301484
elif 50 < consumo_do_setor <= 149.99:
    if 50 < consumo_do_setor < 101:
        taxa = 0.44187518
    else:
        taxa = 0.25776052
elif consumo_do_setor >= 150:
    if consumo_do_setor > 220:
        taxa = 0.75879587
    if 149.99 < consumo_do_setor <= 220:
        taxa = 0.26557855
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                          Realiza os calculos finais
# ----------------------------------------------------------------------------------------------------------------------
consumo_geral = consumo_do_setor
gasto_geral_sem_impostos = consumo_geral * taxa
gasto_geral_com_impostos = gasto_geral_sem_impostos + gasto_geral_sem_impostos * (27/100) + \
    gasto_geral_sem_impostos * (1.65/100) + gasto_geral_sem_impostos * (7.61/100)  # ICMS  PIS COFINS
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                        Exibição dos resultados finais
# ----------------------------------------------------------------------------------------------------------------------
print('\n\n\nConsumo geral: {} Kwh'.format(consumo_geral))
print('Gasto geral: R$ {}'.format(gasto_geral_sem_impostos))
print('Valor da conta: R$ {}'.format(gasto_geral_com_impostos))
print('\n\n\n\n\t\t\t\t\tFim do programa')
print('\n\n\n\n\t\t\t\t\t')
print(setores)
print('\n\n\n\n\t\t\t\t\t')
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                       Calculo usando listas
# ----------------------------------------------------------------------------------------------------------------------
tamanho_lista_setores = len(setores)
contado_lista_1 = 0
gasto_aparelho = 0
gasto_Setor = 0
consumo_lista_setor = 0
gasto_tipo_aparelho = 0
gasto_geral_sem_impostos = 0
consumo_tipo_aparelho = 0
consumo_geral = 0

while contado_lista_1 < tamanho_lista_setores:
    droa = 0
    while droa < 5:
        tamanho_lista_aparelhos = len(setores[contado_lista_1][droa])
        contado_lista_2 = 0
        while contado_lista_2 < tamanho_lista_aparelhos:
            gasto_aparelho = setores[contado_lista_1][droa][contado_lista_2] * taxa
            print('\t\t\tconsumo: {} gasto {}'.format(setores[contado_lista_1][droa][contado_lista_2], gasto_aparelho))
            gasto_tipo_aparelho += gasto_aparelho
            consumo_tipo_aparelho += setores[contado_lista_1][droa][contado_lista_2]
            contado_lista_2 += 1
        print('tipo de aparelgo: consumo {} gasto: {}'.format(consumo_tipo_aparelho, gasto_tipo_aparelho))
        gasto_Setor += gasto_tipo_aparelho
        consumo_lista_setor += consumo_tipo_aparelho
        gasto_tipo_aparelho = 0
        consumo_tipo_aparelho = 0
        droa += 1
    print('******* por setor. consumo {} gasto {}'.format(consumo_lista_setor, gasto_Setor))
    gasto_geral_sem_impostos += gasto_Setor
    consumo_geral += consumo_lista_setor
    contado_lista_1 += 1

gasto_geral_com_impostos = gasto_geral_sem_impostos + gasto_geral_sem_impostos * (27/100) + \
    gasto_geral_sem_impostos * (1.65/100) + gasto_geral_sem_impostos * (7.61/100)  # ICMS  PIS COFINS
# ______________________________________________________________________________________________________________________

print('\n\n\n\n\n\n')
print('Consumo geral: {}'.format(consumo_geral))
print('Gasto geral sem impostos: {}'.format(gasto_geral_sem_impostos))
print('Gasto geral com impostos: {}'.format(gasto_geral_com_impostos))
