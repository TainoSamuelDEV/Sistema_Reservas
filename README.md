# Sistema de Reservas

Este é um sistema desenvolvido em Python para o projeto acadêmico da disciplina de Algoritmos e Programação de Computadores. O sistema foi criado para a companhia aérea fictícia FlyMeToTheMoon e tem como objetivo substituir o sistema manual de reservas baseado em papel.

## O que tem
- Consultar voos disponíveis
- Fazer uma reserva
- Listar reservas

## O que NÃO tem
- Classes de serviço (econômica, executiva, etc.)
- Bilhete de embarque
- Cancelamento de reservas
- Banco de dados (usa listas em memória)

## Como executar
1. Python 3 instalado
2. No terminal, vá até a pasta do projeto
3. Rode:
   ```bash
   python sistema_reservas.py
   ```
OU
4. Execute o arquivo `sistema_reservas.exe`

## Funcionamento rápido
- Os voos já vêm cadastrados com poucos assentos
- Ao reservar, o sistema reduz o número de assentos daquele voo
- As reservas ficam guardadas enquanto o programa está aberto