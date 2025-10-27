#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Gerenciamento de Reservas de Passagens Aéreas
Companhia Aérea: FlyMeToTheMoon

Projeto Acadêmico - PBL2
Disciplina: Algoritmos e Programação de Computadores

Este sistema implementa:
- Estruturas condicionais (if/else)
- Estruturas de repetição (for/while)
- Operadores lógicos
- Entrada e saída de dados
"""

# Estruturas de dados globais
lista_voos = []
lista_reservas = []
contador_reserva = 1

def inicializar_sistema():
    """
    Inicializa o sistema com voos pré-cadastrados
    Aplica: estruturas de dados, operações básicas
    """
    global lista_voos
    
    # Estrutura: [código, origem, destino, assentos_economica, assentos_executiva, assentos_primeira]
    voos_iniciais = [
        ["AA001", "São Paulo", "Rio de Janeiro", 150, 100, 50],
        ["BB002", "Rio de Janeiro", "Brasília", 120, 80, 40],
        ["CC003", "Brasília", "Salvador", 100, 60, 30],
        ["DD004", "Salvador", "Recife", 90, 50, 25],
        ["EE005", "Recife", "Fortaleza", 110, 70, 35]
    ]
    
    # Estrutura de repetição: for para inicializar voos
    for voo_dados in voos_iniciais:
        voo = {
            'codigo': voo_dados[0],
            'origem': voo_dados[1],
            'destino': voo_dados[2],
            'assentos_economica': voo_dados[3],
            'assentos_executiva': voo_dados[4],
            'assentos_primeira': voo_dados[5]
        }
        lista_voos.append(voo)
    
    print("Sistema inicializado com sucesso!")
    print(f"Total de voos cadastrados: {len(lista_voos)}")

def menu_principal():
    """
    Exibe o menu principal e gerencia as opções do usuário
    Aplica: estruturas de repetição (while), estruturas condicionais (if/elif/else)
    """
    # Estrutura de repetição: while para manter o programa rodando
    while True:
        print("\n" + "="*50)
        print("    SISTEMA DE RESERVAS - FlyMeToTheMoon")
        print("="*50)
        print("1. Fazer Reserva")
        print("2. Consultar Voos Disponíveis")
        print("3. Listar Todas as Reservas")
        print("4. Gerar Bilhete de Embarque")
        print("5. Cancelar Reserva")
        print("0. Sair")
        print("="*50)
        
        # Entrada de dados
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite apenas números!")
            continue
        
        # Estruturas condicionais: if/elif/else
        if opcao == 1:
            fazer_reserva()
        elif opcao == 2:
            consultar_voos()
        elif opcao == 3:
            listar_reservas()
        elif opcao == 4:
            gerar_bilhete()
        elif opcao == 5:
            cancelar_reserva()
        elif opcao == 0:
            print("\nObrigado por usar o sistema FlyMeToTheMoon!")
            print("Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

def fazer_reserva():
    """
    Realiza uma nova reserva de passagem
    Aplica: estruturas condicionais, operadores lógicos, entrada/saída de dados
    """
    global contador_reserva
    
    print("\n" + "="*30)
    print("       FAZER RESERVA")
    print("="*30)
    
    # Mostrar voos disponíveis primeiro
    if not lista_voos:  # Operador lógico: not
        print("Nenhum voo disponível no momento.")
        return
    
    consultar_voos()
    
    # Entrada de dados: código do voo
    codigo_voo = input("\nDigite o código do voo desejado: ").upper().strip()
    
    # Buscar voo - estrutura de repetição e condicionais
    voo_encontrado = None
    for voo in lista_voos:  # Estrutura de repetição: for
        if voo['codigo'] == codigo_voo:  # Estrutura condicional: if
            voo_encontrado = voo
            break
    
    # Estrutura condicional: verificar se voo existe
    if voo_encontrado is None:
        print("Voo não encontrado!")
        return
    
    # Mostrar tipos de classe
    print("\nTipos de classe disponíveis:")
    print("1. Econômica")
    print("2. Executiva")
    print("3. Primeira Classe")
    
    # Entrada de dados: tipo de classe
    try:
        tipo_classe = int(input("Escolha o tipo de classe (1-3): "))
    except ValueError:
        print("Por favor, digite apenas números!")
        return
    
    # Estrutura condicional: validar tipo de classe
    if tipo_classe < 1 or tipo_classe > 3:  # Operadores lógicos: < , > , or
        print("Tipo de classe inválido!")
        return
    
    # Verificar disponibilidade - estruturas condicionais e operadores lógicos
    disponivel = False
    if tipo_classe == 1 and voo_encontrado['assentos_economica'] > 0:  # Operadores: == , and , >
        disponivel = True
        classe_nome = "Econômica"
    elif tipo_classe == 2 and voo_encontrado['assentos_executiva'] > 0:  # Operadores: == , and , >
        disponivel = True
        classe_nome = "Executiva"
    elif tipo_classe == 3 and voo_encontrado['assentos_primeira'] > 0:  # Operadores: == , and , >
        disponivel = True
        classe_nome = "Primeira Classe"
    
    # Estrutura condicional: verificar disponibilidade
    if not disponivel:  # Operador lógico: not
        print(f"Não há assentos disponíveis na classe {obter_nome_classe(tipo_classe)}!")
        return
    
    # Coletar dados do passageiro - entrada de dados
    print(f"\nClasse selecionada: {classe_nome}")
    nome_passageiro = input("Digite o nome completo do passageiro: ").strip()
    
    # Validação básica do nome
    if len(nome_passageiro) < 2:  # Operador lógico: <
        print("Nome deve ter pelo menos 2 caracteres!")
        return
    
    cpf_passageiro = input("Digite o CPF do passageiro (apenas números): ").strip()
    
    # Validação básica do CPF
    if len(cpf_passageiro) != 11 or not cpf_passageiro.isdigit():  # Operadores: != , or , not
        print("CPF deve conter exatamente 11 dígitos!")
        return
    
    # Criar nova reserva
    nova_reserva = {
        'numero': contador_reserva,
        'nome': nome_passageiro,
        'cpf': cpf_passageiro,
        'codigo_voo': codigo_voo,
        'tipo_classe': tipo_classe,
        'classe_nome': classe_nome
    }
    
    # Adicionar reserva à lista
    lista_reservas.append(nova_reserva)
    
    # Atualizar disponibilidade do voo - estruturas condicionais
    if tipo_classe == 1:
        voo_encontrado['assentos_economica'] -= 1
    elif tipo_classe == 2:
        voo_encontrado['assentos_executiva'] -= 1
    elif tipo_classe == 3:
        voo_encontrado['assentos_primeira'] -= 1
    
    # Incrementar contador
    contador_reserva += 1
    
    # Saída de dados: confirmação
    print("\n" + "="*40)
    print("    RESERVA REALIZADA COM SUCESSO!")
    print("="*40)
    print(f"Número da reserva: #{nova_reserva['numero']}")
    print(f"Passageiro: {nova_reserva['nome']}")
    print(f"Voo: {codigo_voo}")
    print(f"Classe: {classe_nome}")
    print("="*40)

def verificar_disponibilidade(voo, tipo_classe):
    """
    Verifica se há assentos disponíveis para o tipo de classe especificado
    Aplica: estruturas condicionais, operadores lógicos
    """
    # Estruturas condicionais e operadores lógicos
    if tipo_classe == 1 and voo['assentos_economica'] > 0:  # Operadores: == , and , >
        return True
    elif tipo_classe == 2 and voo['assentos_executiva'] > 0:  # Operadores: == , and , >
        return True
    elif tipo_classe == 3 and voo['assentos_primeira'] > 0:  # Operadores: == , and , >
        return True
    else:
        return False

def consultar_voos():
    """
    Exibe todos os voos disponíveis
    Aplica: estruturas de repetição, estruturas condicionais, saída de dados
    """
    print("\n" + "="*60)
    print("                VOOS DISPONÍVEIS")
    print("="*60)
    
    # Estrutura condicional: verificar se há voos
    if not lista_voos:  # Operador lógico: not
        print("Nenhum voo cadastrado no sistema.")
        return
    
    # Estrutura de repetição: for para percorrer voos
    for i, voo in enumerate(lista_voos, 1):  # enumerate para numeração
        print(f"\n{i}. Voo: {voo['codigo']}")
        print(f"   Rota: {voo['origem']} → {voo['destino']}")
        print(f"   Assentos Disponíveis:")
        print(f"   • Econômica: {voo['assentos_economica']}")
        print(f"   • Executiva: {voo['assentos_executiva']}")
        print(f"   • Primeira Classe: {voo['assentos_primeira']}")
        
        # Calcular total de assentos
        total_assentos = (voo['assentos_economica'] + 
                         voo['assentos_executiva'] + 
                         voo['assentos_primeira'])
        print(f"   • Total Disponível: {total_assentos}")
        print("-" * 50)

def listar_reservas():
    """
    Lista todas as reservas realizadas
    Aplica: estruturas de repetição, estruturas condicionais, saída de dados
    """
    print("\n" + "="*50)
    print("            TODAS AS RESERVAS")
    print("="*50)
    
    # Estrutura condicional: verificar se há reservas
    if not lista_reservas:  # Operador lógico: not
        print("Nenhuma reserva encontrada no sistema.")
        return
    
    # Estrutura de repetição: for para percorrer reservas
    for i, reserva in enumerate(lista_reservas, 1):
        print(f"\n{i}. Reserva #{reserva['numero']}")
        print(f"   Passageiro: {reserva['nome']}")
        print(f"   CPF: {reserva['cpf']}")
        print(f"   Voo: {reserva['codigo_voo']}")
        print(f"   Classe: {reserva['classe_nome']}")
        
        # Buscar informações do voo
        voo_info = buscar_voo(reserva['codigo_voo'])
        if voo_info:  # Estrutura condicional: if
            print(f"   Rota: {voo_info['origem']} → {voo_info['destino']}")
        
        print("-" * 40)
    
    print(f"\nTotal de reservas: {len(lista_reservas)}")

def gerar_bilhete():
    """
    Gera bilhete de embarque para uma reserva
    Aplica: entrada de dados, estruturas condicionais, saída de dados
    """
    print("\n" + "="*40)
    print("      GERAR BILHETE DE EMBARQUE")
    print("="*40)
    
    # Estrutura condicional: verificar se há reservas
    if not lista_reservas:  # Operador lógico: not
        print("Nenhuma reserva encontrada no sistema.")
        return
    
    # Entrada de dados
    try:
        numero_reserva = int(input("Digite o número da reserva: "))
    except ValueError:
        print("Por favor, digite apenas números!")
        return
    
    # Buscar reserva - estrutura de repetição e condicionais
    reserva_encontrada = None
    for reserva in lista_reservas:  # Estrutura de repetição: for
        if reserva['numero'] == numero_reserva:  # Estrutura condicional: if
            reserva_encontrada = reserva
            break
    
    # Estrutura condicional: verificar se reserva existe
    if reserva_encontrada is None:
        print("Reserva não encontrada!")
        return
    
    # Buscar informações do voo
    voo_reserva = buscar_voo(reserva_encontrada['codigo_voo'])
    
    # Estrutura condicional: verificar se voo existe
    if voo_reserva is None:
        print("Erro: Voo da reserva não encontrado!")
        return
    
    # Saída de dados: bilhete formatado
    print("\n" + "="*50)
    print("           BILHETE DE EMBARQUE")
    print("="*50)
    print("         FlyMeToTheMoon Airlines")
    print("="*50)
    print(f"Reserva: #{reserva_encontrada['numero']}")
    print(f"Passageiro: {reserva_encontrada['nome']}")
    print(f"CPF: {reserva_encontrada['cpf']}")
    print(f"Voo: {reserva_encontrada['codigo_voo']}")
    print(f"Origem: {voo_reserva['origem']}")
    print(f"Destino: {voo_reserva['destino']}")
    print(f"Classe: {reserva_encontrada['classe_nome']}")
    print("="*50)
    print("    Apresente este bilhete no embarque")
    print("="*50)

def cancelar_reserva():
    """
    Cancela uma reserva existente
    Aplica: entrada de dados, estruturas condicionais, estruturas de repetição
    """
    print("\n" + "="*35)
    print("        CANCELAR RESERVA")
    print("="*35)
    
    # Estrutura condicional: verificar se há reservas
    if not lista_reservas:  # Operador lógico: not
        print("Nenhuma reserva encontrada no sistema.")
        return
    
    # Mostrar reservas existentes
    print("\nReservas existentes:")
    for reserva in lista_reservas:  # Estrutura de repetição: for
        print(f"#{reserva['numero']} - {reserva['nome']} - Voo {reserva['codigo_voo']}")
    
    # Entrada de dados
    try:
        numero_reserva = int(input("\nDigite o número da reserva a cancelar: "))
    except ValueError:
        print("Por favor, digite apenas números!")
        return
    
    # Buscar reserva - estrutura de repetição e condicionais
    reserva_encontrada = None
    indice_reserva = -1
    for i, reserva in enumerate(lista_reservas):  # Estrutura de repetição: for com enumerate
        if reserva['numero'] == numero_reserva:  # Estrutura condicional: if
            reserva_encontrada = reserva
            indice_reserva = i
            break
    
    # Estrutura condicional: verificar se reserva existe
    if reserva_encontrada is None:
        print("Reserva não encontrada!")
        return
    
    # Confirmar cancelamento
    confirmacao = input(f"Confirma o cancelamento da reserva #{numero_reserva} de {reserva_encontrada['nome']}? (s/n): ").lower().strip()
    
    # Estrutura condicional: verificar confirmação
    if confirmacao != 's' and confirmacao != 'sim':  # Operadores lógicos: != , and
        print("Cancelamento abortado.")
        return
    
    # Liberar assento no voo - buscar voo e atualizar
    voo_reserva = buscar_voo(reserva_encontrada['codigo_voo'])
    
    # Estrutura condicional: verificar se voo existe
    if voo_reserva is not None:
        # Estruturas condicionais: liberar assento conforme tipo de classe
        if reserva_encontrada['tipo_classe'] == 1:
            voo_reserva['assentos_economica'] += 1
        elif reserva_encontrada['tipo_classe'] == 2:
            voo_reserva['assentos_executiva'] += 1
        elif reserva_encontrada['tipo_classe'] == 3:
            voo_reserva['assentos_primeira'] += 1
    
    # Remover reserva da lista
    lista_reservas.pop(indice_reserva)
    
    # Saída de dados: confirmação
    print("\n" + "="*40)
    print("    RESERVA CANCELADA COM SUCESSO!")
    print("="*40)
    print(f"Reserva #{numero_reserva} foi cancelada.")
    print("O assento foi liberado para novas reservas.")

def buscar_voo(codigo):
    """
    Busca um voo pelo código
    Aplica: estruturas de repetição, estruturas condicionais
    """
    # Estrutura de repetição: for para buscar voo
    for voo in lista_voos:
        if voo['codigo'] == codigo:  # Estrutura condicional: if
            return voo
    return None

def buscar_reserva(numero):
    """
    Busca uma reserva pelo número
    Aplica: estruturas de repetição, estruturas condicionais
    """
    # Estrutura de repetição: for para buscar reserva
    for reserva in lista_reservas:
        if reserva['numero'] == numero:  # Estrutura condicional: if
            return reserva
    return None

def obter_nome_classe(tipo):
    """
    Retorna o nome da classe baseado no tipo numérico
    Aplica: estruturas condicionais
    """
    # Estruturas condicionais: if/elif/else
    if tipo == 1:
        return "Econômica"
    elif tipo == 2:
        return "Executiva"
    elif tipo == 3:
        return "Primeira Classe"
    else:
        return "Classe Inválida"

def main():
    """
    Função principal do programa
    Aplica: chamadas de função, estrutura do programa
    """
    print("Inicializando Sistema de Reservas FlyMeToTheMoon...")
    print("Carregando dados...")
    
    # Inicializar sistema
    inicializar_sistema()
    
    # Executar menu principal
    menu_principal()

# Execução do programa principal
if __name__ == "__main__":
    main()