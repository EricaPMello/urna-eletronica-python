print('\n\nELEIÇÕES 2022\n\n')

candidatos_prefeito = {"1": "João Marcolino", "2": "Carlos Batista", "3": "Roque Pedroso", "4": "Branco", "5": "Nulo"}
votos_prefeito = {c: 0 for c in candidatos_prefeito}

candidatos_vereador = {"10": "Marisa Cardeal", "15": "Valter Rogério", "20": "Joaquim Melo", "25": "Elton Nascimento",
                       "30": "Maria Vicentina", "35": "Daniela Salazar", "40": "Josemar Coimbra", "45": "Félix dos Santos",
                       "50": "Altamir Miranda", "55": "Marcondes Galdino", "60": "Branco", "65": "Nulo"}
votos_vereador = {c: 0 for c in candidatos_vereador}

opcao = input('Digite 1 para imprimir zerésima ou digite 2 para iniciar a votação: ')

if opcao == '1':
    print('\n\nZERÉSIMA:\n')
    for numero, candidato in candidatos_prefeito.items():
        print(f"Candidato (Prefeito) {candidato} ({numero}): 0 votos")
    for numero, candidato in candidatos_vereador.items():
        print(f"Candidato (Vereador) {candidato} ({numero}): 0 votos")
    iniciar = input('\nDigite 2 para iniciar a votação: ')
    if iniciar == '2':
        print('\n\nIniciando a votação...\n')
    else:
        print('Opção inválida. A votação não será iniciada.')
        exit() # Encerra o programa se a opção for diferente de 2

elif opcao == '2':
    print('\n\nIniciando a votação...\n')

def votar_prefeito(votos, candidatos):
    while True:
        print('\n\nPARA PREFEITO:')
        for numero, candidato in candidatos.items():
            print(f"{numero} - {candidato}")
        voto = input('Digite o número do candidato a Prefeito: ')
        if voto in candidatos:
            votos[voto] += 1
            print(f'Voto em {candidatos[voto]} registrado com sucesso!')
            break
        else:
            print('Número inválido. Tente novamente.')

def votar_vereador(votos, candidatos):
    while True:
        print('\n\nPARA VEREADOR:')
        for numero, candidato in candidatos.items():
            print(f"{numero} - {candidato}")
        voto = input('Digite o número do candidato a Vereador: ')
        if voto in candidatos:
            votos[voto] += 1
            print(f'Voto em {candidatos[voto]} registrado com sucesso!')
            break
        else:
            print('Número inválido. Tente novamente.')

def apurar_resultados(votos_prefeito, candidatos_prefeito, votos_vereador, candidatos_vereador):
    def encontrar_vencedor(votos, candidatos):
        vencedor = None
        max_votos = -1
        for numero, qtd_votos in votos.items():
            if qtd_votos > max_votos:
                max_votos = qtd_votos
                vencedor = candidatos[numero]
        return vencedor, max_votos

    vencedor_prefeito, votos_vencedor_prefeito = encontrar_vencedor(votos_prefeito, candidatos_prefeito)
    vencedor_vereador, votos_vencedor_vereador = encontrar_vencedor(votos_vereador, candidatos_vereador)

    print('\n\nRESULTADO DA ELEIÇÃO:')
    print('\nPREFEITO:')
    for numero, qtd_votos in votos_prefeito.items():
        print(f'{candidatos_prefeito[numero]}: {qtd_votos} votos')
    print(f'\nVencedor: {vencedor_prefeito} com {votos_vencedor_prefeito} votos.')

    print('\nVEREADOR:')
    for numero, qtd_votos in votos_vereador.items():
        print(f'{candidatos_vereador[numero]}: {qtd_votos} votos')
    print(f'\nVencedor: {vencedor_vereador} com {votos_vencedor_vereador} votos.')

if opcao == '1' or opcao == '2':
    while True:
        votar_prefeito(votos_prefeito, candidatos_prefeito)
        votar_vereador(votos_vereador, candidatos_vereador)
        continuar = input('Digite 1 para continuar votando ou 2 para finalizar: ')
        if continuar == '2':
            break
    apurar_resultados(votos_prefeito, candidatos_prefeito, votos_vereador, candidatos_vereador)
else:
    print('Opção inválida.')