# ----------------------------------------------------------------------------------------------------------------------
#                                                 listando variavéis
# ----------------------------------------------------------------------------------------------------------------------
tipo_de_aparelho = 0
nome_do_aparelho = 'x'
potencia_do_aparelho = 0.0
horas_de_uso_por_dia_do_aparelho = 0.0
dias_de_uso_do_aparelho_por_mes = 0.0
consumo_do_aparelho = 0.0
numero_de_aparelhos = 0
contador_do_loop = 1
outro_contador_de_loop = 0
adicionar_setor = 'x'
contador_de_setores = 1
consumo_do_setor = 0
consumo_geral = 0.0
gasto_geral_sem_impostos = 0.0
gasto_geral_com_impostos = 0.0
mais_setores = True
taxa = 0.0
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

        numero_de_aparelhos = int(input(
            '\n\nQuantos {} existem no {}° setor: '.format(nome_do_aparelho, contador_de_setores)))
        while contador_do_loop <= numero_de_aparelhos:
            potencia_do_aparelho = float(input('Digite a potẽncia do {}° aparelho: '.format(contador_do_loop)))
            horas_de_uso_por_dia_do_aparelho = float(
                input('Digite a quantidade de horas por dia de uso do {}° aparelho: '.format(contador_do_loop)))
            dias_de_uso_do_aparelho_por_mes = float(
                input('Digite a quantidade de dias por mês de uso do {}° aparelho; '.format(contador_do_loop)))
            consumo_do_aparelho = (
                potencia_do_aparelho * horas_de_uso_por_dia_do_aparelho * dias_de_uso_do_aparelho_por_mes)
            consumo_do_setor = consumo_do_setor + consumo_do_aparelho
            contador_do_loop = contador_do_loop + 1
        tipo_de_aparelho = tipo_de_aparelho + 1
        contador_do_loop = 1 # Reseta o loop para uso com outro tipo de aparelho
    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                              Adiciona um novo setor
    # ------------------------------------------------------------------------------------------------------------------
    while adicionar_setor != 'A' and adicionar_setor != 'B':
        print('----------------------| Deseja adicionar mais um setor? |----------------------\n\n')
        print('[A] - Para adicionar outro setor à contagem')
        print('[B] - Para afinalizar as contagens\n\n')
        adicionar_setor = input('Digite sua escolha: ')
        if adicionar_setor == 'A':
            contador_de_setores = contador_de_setores + 1
            tipo_de_aparelho = 0  # Permite ao programa executar novamente o primeiro laço de repetição
        elif adicionar_setor == 'B':
            mais_setores = False
        else:
            print('Opção inválida, digite novamente!\n\n')
    adicionar_setor = 'x'  # Permite ao programa voltar a executar esse laço quando houver mais um setor
    # __________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                      Definindo a taxa utilizada para os calculos
# ----------------------------------------------------------------------------------------------------------------------
if consumo_do_setor/1000 <= 50: # Consumo em KW
    if consumo_do_setor/1000 < 31:
        taxa = 0.18842532
    else:
        taxa = 0.32301484
elif 50 < consumo_do_setor/1000 <= 149.99:
    if 50 < consumo_do_setor < 101:
        taxa = 0.44187518
    else:
        taxa = 0.25776052
elif consumo_do_setor/1000 >= 150:
    if consumo_do_setor/1000 > 220:
        taxa = 0.75879587
    if 149.99 < consumo_do_setor <= 220:
        taxa = 0.26557855
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                          Realiza os calculos finais
# ----------------------------------------------------------------------------------------------------------------------
consumo_geral = consumo_do_setor/1000
gasto_geral_sem_impostos = consumo_geral * taxa
gasto_geral_com_impostos = gasto_geral_sem_impostos * (27/100) + gasto_geral_sem_impostos * (1.65/100) + \
    gasto_geral_sem_impostos * (7.61/100)  # ICMS  PIS COFINS
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                        Exibição dos resultados finais
# ----------------------------------------------------------------------------------------------------------------------
print('\n\n\nConsumo geral: {} Kwh'.format(consumo_geral))
print('Gasto geral: R$ {}'.format(gasto_geral_sem_impostos))
print('Valor da conta: R$ {}'.format(gasto_geral_com_impostos))
print('\n\n\n\n\t\t\t\t\tFim do programa')
# ______________________________________________________________________________________________________________________
