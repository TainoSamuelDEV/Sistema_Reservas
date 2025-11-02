# Versão Simples do Sistema de Reservas

Este é um exemplo bem básico do sistema de reservas, pensado para ser fácil de entender. Não tem recursos avançados, apenas o essencial para funcionar.

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
1. Tenha Python 3 instalado
2. No terminal, vá até a pasta do projeto
3. Rode:
   ```bash
   python sistema_reservas_simplificado.py
   ```

## Funcionamento rápido
- Os voos já vêm cadastrados com poucos assentos
- Ao reservar, o sistema reduz o número de assentos daquele voo
- As reservas ficam guardadas enquanto o programa está aberto