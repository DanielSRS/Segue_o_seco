# Iniciando a construção do sistema, para o MI de Agoritmos e programação I

# --------------------------------------------------------------------------------------------------------------
#                                           listando variavéis
# --------------------------------------------------------------------------------------------------------------
tipo_de_aparelho: int = 0
nome_do_aparelho: str = 'ar condicionados'
potencia_do_aparelho: float = 0
horas_de_uso_por_dia_do_aparelho: float = 0
dias_de_uso_do_aparelho_por_mes: float = 0
consumo_do_aparelho: float = 0
numero_de_aparelhos: int = 0
contador_do_loop = 1
outro_contador_de_loop = 0
adicionar_setor: str = 'x'
contador_de_setores = 1
consumo_do_setor = 0
consumo_geral = 0
gasto_geral_sem_impostos = 0

# -----------------------------------------------------------------------------------------------------------------
#                                    Loop para contabilizar todos os tipos de aparelho
# _________________________________________________________________________________________________________________

while tipo_de_aparelho <= 5:
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

    print('Quantos {} existem no {}° setor: '.format(nome_do_aparelho, contador_de_setores))
    numero_de_aparelhos: int = int(input())
    while contador_do_loop <= numero_de_aparelhos:
        potencia_do_aparelho = float(input('Digite a potẽncia do {}° aparelho: '.format(contador_do_loop)))
        horas_de_uso_por_dia_do_aparelho = float(
            input('Digite a quantidade de horas por dia de uso do {}° aparelho: '.format(contador_do_loop)))
        dias_de_uso_do_aparelho_por_mes = float(
            input('Digite a quantidade de dias por mês de uso do {}° aparelho; '.format(contador_do_loop)))
        consumo_do_aparelho = potencia_do_aparelho * horas_de_uso_por_dia_do_aparelho * dias_de_uso_do_aparelho_por_mes
        consumo_do_setor = consumo_do_setor + consumo_do_aparelho
        print(consumo_do_setor)
        contador_do_loop = contador_do_loop + 1
    tipo_de_aparelho = tipo_de_aparelho + 1
    contador_do_loop = 1
# __________________________________________________________________________________________________________________

while adicionar_setor != 'A' or adicionar_setor != 'B':
    print('Deseja adicionar mais um setor?/n/n')
    print('[A] - Para adicionar outro setor à contagem/n')
    print('[B] - Para afinaliar as contagens/n/n')
    adicionar_setor: str = input('Digite sua escolha: ')
    if adicionar_setor != 'A' or adicionar_setor != 'B':
        print('Opção inválida, digite novamente!/n/n')
