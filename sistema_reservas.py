# dados em memória
voos = []
reservas = []
proximo_numero = 1


def inicializar_voos():
    # cada voo tem: codigo, origem, destino, assentos
    # números pequenos para testar fácil
    voos.append({"codigo": "AA001", "origem": "São Paulo", "destino": "Rio de Janeiro", "assentos": 5})
    voos.append({"codigo": "BB002", "origem": "Rio de Janeiro", "destino": "Brasília", "assentos": 3})
    voos.append({"codigo": "CC003", "origem": "Brasília", "destino": "Salvador", "assentos": 2})


def mostrar_voos():
    print("\n=== VOOS DISPONÍVEIS ===")
    if len(voos) == 0:
        print("Nenhum voo cadastrado.")
        return
    for v in voos:
        print(f"Voo {v['codigo']} - {v['origem']} -> {v['destino']} | Assentos: {v['assentos']}")


def buscar_voo_por_codigo(codigo):
    for v in voos:
        if v["codigo"] == codigo:
            return v
    return None


def fazer_reserva():
    global proximo_numero
    if len(voos) == 0:
        print("Não há voos disponíveis.")
        return

    mostrar_voos()
    codigo = input("\nDigite o código do voo: ").strip().upper()
    voo = buscar_voo_por_codigo(codigo)

    if voo is None:
        print("Voo não encontrado.")
        return

    if voo["assentos"] <= 0:
        print("Sem assentos disponíveis.")
        return

    nome = input("Nome do passageiro: ").strip()
    cpf = input("CPF (apenas números): ").strip()

    # validações
    if nome == "" or cpf == "":
        print("Nome e CPF não podem ficar vazios.")
        return

    # cria reserva 
    reserva = {
        "numero": proximo_numero,
        "nome": nome,
        "cpf": cpf,
        "codigo_voo": codigo,
    }
    reservas.append(reserva)
    proximo_numero += 1
    voo["assentos"] -= 1

    print("\nReserva feita com sucesso!")
    print(f"Número: {reserva['numero']}")
    print(f"Passageiro: {reserva['nome']}")
    print(f"Voo: {reserva['codigo_voo']}")


def listar_reservas():
    print("\n=== RESERVAS ===")
    if len(reservas) == 0:
        print("Nenhuma reserva registrada.")
        return
    for r in reservas:
        print(f"Reserva #{r['numero']} | {r['nome']} | CPF: {r['cpf']} | Voo: {r['codigo_voo']}")


def menu():
    while True:
        print("\n============================")
        print("SISTEMA SIMPLES DE RESERVAS")
        print("============================")
        print("1 - Consultar voos")
        print("2 - Fazer reserva")
        print("3 - Listar reservas")
        print("0 - Sair")
        try:
            op = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 1:
            mostrar_voos()
        elif op == 2:
            fazer_reserva()
        elif op == 3:
            listar_reservas()
        elif op == 0:
            print("Saindo... Obrigado!")
            break
        else:
            print("Opção inválida.")


def main():
    print("Iniciando sistema simples...")
    inicializar_voos()
    menu()


if __name__ == "__main__":
    main()
