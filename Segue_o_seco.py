# Iniciando a construção do sistema, para o MI de Agoritmos e programação I

# --------------------------------------------------------------------------------------------------------------
#                                           listando variavéis
# --------------------------------------------------------------------------------------------------------------
tipo_de_aparelho = 0
nome_do_aparelho = 'ar condicionados'
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

while mais_setores:
    # -----------------------------------------------------------------------------------------------------------------
    #                                    Loop para contabilizar todos os tipos de aparelho
    # _________________________________________________________________________________________________________________

    while tipo_de_aparelho < 5:
        # _____________________________________________________________________________________________________________

        # -------------------------------------------------------------------------------------------------------------
        #                                           Alterna entre os tipos de aparelhos
        # -------------------------------------------------------------------------------------------------------------
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
        # _____________________________________________________________________________________________________________

        numero_de_aparelhos: int = int(input(
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
            print(consumo_do_setor)
            contador_do_loop = contador_do_loop + 1
        tipo_de_aparelho = tipo_de_aparelho + 1
        contador_do_loop = 1
    # __________________________________________________________________________________________________________________

    while adicionar_setor != 'A' and adicionar_setor != 'B':
        print('----------------------| Deseja adicionar mais um setor? |----------------------\n\n')
        print('[A] - Para adicionar outro setor à contagem')
        print('[B] - Para afinaliar as contagens\n\n')
        adicionar_setor = input('Digite sua escolha: ')
        if adicionar_setor == 'A':
            contador_de_setores = contador_de_setores + 1
            adicionar_setor = 'x'  # Permite ao programa voltar a executar esse laço quando houver mais um setor
            tipo_de_aparelho = 0  # Permite ao programa executar novamente o primeiro laço de repetição
        elif adicionar_setor == 'B':
            mais_setores = False
        else:
            print('Opção inválida, digite novamente!\n\n')
    print('\n\n\nCheguei aqui!!!!')
if consumo_do_setor <= 50:
    taxa = 0.18842532
elif consumo_do_setor > 50 and consumo_do_setor <= 149.99:
    taxa = 0.25776052
elif consumo_do_setor >= 150:
    taxa = 0.26557855
consumo_geral = consumo_do_setor/1000
gasto_geral_sem_impostos = consumo_geral * taxa
gasto_geral_com_impostos = gasto_geral_sem_impostos * (27/100) + gasto_geral_sem_impostos * (1.65/100) + \
    gasto_geral_sem_impostos * (7.61/100)  # ICMS  PIS COFINS
print('\n\n\nConsumo geral: {} Kwh'.format(consumo_geral))
print('Gasto geral: R$ {}'.format(gasto_geral_sem_impostos))
print('Valor da conta: R$ {}'.format(gasto_geral_com_impostos))
print('\n\n\n\n\t\t\t\t\tFim do programa')
