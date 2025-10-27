# Sistema de Gerenciamento de Reservas de Passagens Aéreas

## 📋 Sobre o Projeto

Este é um protótipo de sistema desenvolvido em Python para o projeto acadêmico PBL2 da disciplina de Algoritmos e Programação de Computadores. O sistema foi criado para a companhia aérea fictícia **FlyMeToTheMoon** e tem como objetivo substituir o sistema manual de reservas baseado em papel.

## 🎯 Objetivos

- Gerenciar reservas de passagens aéreas de forma eficiente
- Verificar disponibilidade de assentos em tempo real
- Evitar problemas de overbooking
- Manter registro organizado de todas as reservas
- Gerar bilhetes de embarque para os passageiros

## 📁 Estrutura do Projeto

```
av2/
├── sistema_reservas.py          # Código principal do sistema
├── pseudocodigo.txt            # Pseudocódigo da solução
├── descricao_fluxograma.txt    # Descrição para criação do fluxograma
├── plano_testes.txt            # Plano de testes funcionais
├── melhorias_futuras.txt       # Sugestões de melhorias
└── README.md                   # Este arquivo
```

## 🚀 Como Executar

1. Certifique-se de ter Python 3.6+ instalado
2. Navegue até o diretório do projeto
3. Execute o comando:
   ```bash
   python sistema_reservas.py
   ```

## 💻 Funcionalidades

### ✅ Funcionalidades Implementadas

- **Fazer Reserva**: Permite criar novas reservas com validação completa
- **Consultar Voos**: Lista todos os voos disponíveis com informações de assentos
- **Listar Reservas**: Exibe todas as reservas realizadas no sistema
- **Gerar Bilhete**: Cria bilhete de embarque formatado para impressão
- **Cancelar Reserva**: Remove reserva e libera assento automaticamente
- **Prevenção de Overbooking**: Sistema impede reservas além da capacidade

### 🎨 Tipos de Classe Disponíveis

- **Econômica**: Classe padrão com maior número de assentos
- **Executiva**: Classe intermediária com mais conforto
- **Primeira Classe**: Classe premium com serviço diferenciado

## 🛠️ Conceitos Técnicos Aplicados

O sistema implementa todos os conceitos obrigatórios da disciplina:

- ✅ **Estruturas Condicionais**: `if/elif/else` para validações e decisões
- ✅ **Estruturas de Repetição**: `while` para menu principal, `for` para listagens
- ✅ **Operadores Lógicos**: `and`, `or`, `not` para validações complexas
- ✅ **Entrada e Saída de Dados**: `input()` e `print()` para interação com usuário

## 📊 Voos Pré-cadastrados

O sistema inicia com 5 voos disponíveis:

| Código | Origem | Destino | Econômica | Executiva | Primeira |
|--------|--------|---------|-----------|-----------|----------|
| AA001  | São Paulo | Rio de Janeiro | 150 | 100 | 50 |
| BB002  | Rio de Janeiro | Brasília | 120 | 80 | 40 |
| CC003  | Brasília | Salvador | 100 | 60 | 30 |
| DD004  | Salvador | Recife | 90 | 50 | 25 |
| EE005  | Recife | Fortaleza | 110 | 70 | 35 |

## 🧪 Testes

O arquivo `plano_testes.txt` contém mais de 30 casos de teste que validam:

- Funcionalidades básicas do sistema
- Tratamento de erros e validações
- Prevenção de overbooking
- Integridade dos dados
- Usabilidade da interface

## 📈 Melhorias Futuras

O arquivo `melhorias_futuras.txt` apresenta 10 sugestões detalhadas de evolução:

1. Integração com Banco de Dados
2. Interface Gráfica de Usuário (GUI)
3. Sistema de Autenticação e Autorização
4. Módulo de Relatórios e Analytics
5. Integração com Sistemas Externos
6. Aplicativo Mobile
7. Sistema de Preços Dinâmicos
8. Melhorias na Experiência do Usuário
9. Sistema de Backup e Recuperação
10. Módulo de Configuração e Administração

## 📋 Artefatos de Entrega

### Parte 1 - Desenvolvimento da Solução
- ✅ **Código-fonte Python**: `sistema_reservas.py`

### Parte 2 - Apresentação
- ✅ **Pseudocódigo**: `pseudocodigo.txt`
- ✅ **Descrição do Fluxograma**: `descricao_fluxograma.txt`
- ✅ **Plano de Testes**: `plano_testes.txt`
- ✅ **Sugestões de Melhorias**: `melhorias_futuras.txt`

## 👥 Informações Acadêmicas

- **Disciplina**: Algoritmos e Programação de Computadores
- **Projeto**: PBL2 - Sistema de Gerenciamento de Reservas
- **Cliente Fictício**: Companhia Aérea FlyMeToTheMoon
- **Linguagem**: Python 3.x
- **Paradigma**: Programação Estruturada

## 📝 Observações

- O sistema utiliza armazenamento em memória (listas Python)
- Os dados são perdidos ao encerrar o programa
- Interface baseada em linha de comando
- Validações implementadas para garantir integridade dos dados
- Código totalmente comentado para facilitar compreensão

## 🔧 Requisitos do Sistema

- Python 3.6 ou superior
- Sistema operacional: Windows, Linux ou macOS
- Memória RAM: Mínimo 512MB
- Espaço em disco: 10MB

---

**Desenvolvido para fins acadêmicos - PBL2 Algoritmos e Programação de Computadores**