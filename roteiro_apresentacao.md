# Roteiro de Apresentação — Sistema de Reservas (Vídeo 10–12 min)

- Tom: profissional e acessível, linguagem simples e objetiva.
- Integrantes e papéis: Ana (Negócio), Bruno (Técnico/Código), Carla (Testes/Usuário).
- Materiais de apoio: `fluxograma.jpg`, `pseudocodigo.txt`, `plano_testes.txt`, `melhorias_futuras.txt`, código `sistema_reservas.py`.
- Tempo total estimado: 11m45s.

---

## 1) Introdução (30–60s)

- Tempo: ~45s
- Visuais: Slide título “Sistema Simples de Reservas” + nomes dos integrantes + objetivos.

Falas:
- Ana (10s): "Olá! Somos Ana, Bruno e Carla. Vamos apresentar nosso Sistema Simples de Reservas de Voos, desenvolvido para a disciplina de Algoritmos e Programação."
- Bruno (20s): "Mostraremos requisitos, fluxo da solução, pseudocódigo, implementação em Python e testes funcionais. O foco é clareza, simplicidade e fundamentos sólidos para evolução."
- Carla (15s): "Ao final, trazemos melhorias planejadas e abrimos para perguntas. Vamos começar pelos requisitos do negócio."

Transição: "Com o contexto em mente, seguimos para os requisitos."

---

## 2) Requisitos do Negócio (1–2 min)

- Tempo: ~1m30s
- Visuais: Slide “Necessidades do Cliente”, bullets de funcionalidades e restrições.

Falas (Ana):
- "Necessidades: consultar voos disponíveis; reservar assento informando dados mínimos; listar reservas realizadas."
- "Funcionalidades implementadas: inicialização de voos em memória; consulta de voos; reserva com validações básicas (nome/CPF não vazios, checagem de assentos); listagem de reservas."
- "Restrições/considerações: sem banco de dados; interface em linha de comando; dados voláteis em memória; foco didático para testes rápidos."

Transição: "Agora, vamos visualizar o fluxo da solução."

---

## 3) Fluxograma da Solução (1–2 min)

- Tempo: ~1m30s
- Visuais: Exibir `fluxograma.jpg` em tela cheia; destacar blocos e setas durante a fala.

Falas (Bruno):
- "O sistema inicia carregando voos pré-cadastrados. Em seguida, exibe o menu principal com quatro opções: 1) Consultar voos, 2) Fazer reserva, 3) Listar reservas, 0) Sair."
- "Lógica principal: o menu lê a opção e direciona para a função correspondente. Em reserva, verificações críticas: o voo existe? há assentos disponíveis? nome e CPF foram informados?"
- "Ao confirmar, geramos número sequencial de reserva, decrementamos assentos do voo e exibimos o resumo. Em qualquer falha de validação, mensagem clara e retorno ao menu."

Transição: "Do desenho para a lógica, vamos ao pseudocódigo."

---

## 4) Pseudocódigo (1–2 min)

- Tempo: ~1m30s
- Visuais: Exibir `pseudocodigo.txt`; destacar blocos principais.

Falas (Carla):
- "Estruturamos a lógica em passos simples e diretos."

Pseudocódigo (resumo):
```text
variáveis globais: voos = [], reservas = [], proximo_numero = 1

função inicializar_voos():
  adicionar 3 voos (codigo, origem, destino, assentos)

função mostrar_voos():
  se voos estiver vazio -> imprimir "Nenhum voo cadastrado"
  senão -> iterar e imprimir cada voo

função buscar_voo_por_codigo(codigo):
  para cada voo em voos:
    se voo.codigo == codigo -> retornar voo
  retornar None

função fazer_reserva():
  se não há voos -> imprimir e retornar
  mostrar_voos()
  ler codigo; buscar voo
  se voo é None -> imprimir e retornar
  se voo.assentos <= 0 -> imprimir e retornar
  ler nome, cpf
  se nome=="" ou cpf=="" -> imprimir e retornar
  criar reserva com numero = proximo_numero
  adicionar reserva em reservas
  proximo_numero += 1
  voo.assentos -= 1
  imprimir confirmação

função listar_reservas():
  se reservas vazia -> imprimir
  senão -> iterar e imprimir cada reserva

função menu():
  loop infinito: imprimir opções, ler entrada
  if 1 -> mostrar_voos
  elif 2 -> fazer_reserva
  elif 3 -> listar_reservas
  elif 0 -> sair
  else -> opção inválida

main(): inicializar_voos(); menu()
```

Transição: "Agora, vamos abrir o código e relacionar com o que vimos."

---

## 5) Algoritmo Desenvolvido (2–3 min)

- Tempo: ~2m30s
- Visuais: Exibir `sistema_reservas.py` com zoom nos trechos principais.

Falas (Bruno):
- "O programa é procedural, com variáveis globais `voos`, `reservas` e `proximo_numero`."
- "`inicializar_voos()`: cria três voos de exemplo com poucos assentos para facilitar testes."
- "`mostrar_voos()`: imprime a lista e lida com lista vazia."
- "`buscar_voo_por_codigo(codigo)`: busca linear — suficiente para poucos itens e código didático."
- "`fazer_reserva()`: validações centrais (existência de voo, assentos, nome/CPF não vazios), criação da reserva, incremento do número e decremento de assentos do voo."
- "`listar_reservas()`: impressão do número, nome, CPF e código do voo."
- "`menu()`: loop de opções com tratamento de `ValueError` para entradas não numéricas."
- "`main()`: inicializa voos e entra no menu — permite execução direta do arquivo."

Destaques técnicos:
- Simplicidade e funções coesas; mensagens claras orientando o usuário.
- Validações básicas suficientes para o escopo didático.
- Estrutura pronta para evoluir (ex.: classes e persistência futura).

Transição: "Vamos conferir o funcionamento com testes práticos."

---

## 6) Testes Funcionais (1–2 min)

- Tempo: ~1m30s
- Visuais: Exibir `plano_testes.txt`; terminal com execução do programa.

Falas (Carla):
- "Executamos cenários de uso típicos e casos de erro para validar o comportamento."

Como demonstrar (terminal):
```powershell
# Executar o programa
python sistema_reservas.py

# 1) Consultar voos
Escolha: 1
# Esperado: exibição da lista de voos

# 2) Fazer reserva válida
Escolha: 2
Digite o código do voo: AA001
Nome do passageiro: Maria
CPF (apenas números): 12345678900
# Esperado: confirmação, assentos de AA001 decrementado

# 3) Voo inexistente
Escolha: 2
Digite o código do voo: ZZ999
# Esperado: "Voo não encontrado."

# 4) Sem assentos
# Reservar CC003 até esgotar e tentar novamente
Escolha: 2
Digite o código do voo: CC003
...
# Esperado: "Sem assentos disponíveis."

# 5) Entradas vazias
Escolha: 2
Digite o código do voo: BB002
Nome do passageiro: 
CPF (apenas números): 
# Esperado: "Nome e CPF não podem ficar vazios."

# 6) Listar reservas
Escolha: 3
# Esperado: listar todas as reservas feitas
```

Transição: "Com base nos testes, propomos evoluções."

---

## 7) Sugestões de Melhorias (1 min)

- Tempo: ~1m00s
- Visuais: Exibir `melhorias_futuras.txt`; slide com roadmap.

Falas (Ana):
- Funcionalidades: persistência (arquivo/banco), cancelamento/alteração de reservas, filtros por origem/destino/data, autenticação básica.
- Técnicas: validação formal de CPF, tratamento de erros robusto, logging e testes automatizados com `pytest`.
- Arquitetura: classes (`Voo`, `Reserva`, `SistemaReservas`), separação UI x lógica, API para integração frontend.
- Escalabilidade: estruturas de dados eficientes, persistência transacional para múltiplos usuários.

Transição: "Para fechar, um breve resumo."

---

## 8) Conclusão (30s)

- Tempo: ~30s
- Visuais: Slide final “Obrigado!” + contatos.

Falas (Todos):
- Bruno: "Resumo: definimos requisitos, explicamos fluxo e pseudocódigo, demonstramos a implementação e validamos com testes."
- Ana: "Apontamos caminhos claros de evolução para robustez e escalabilidade."
- Carla: "Obrigada pela atenção! Abrimos para perguntas."

---

## Dicas de Transição e Edição

- Transições sugeridas:
  - "Com o contexto em mente…" → requisitos.
  - "Visualizando o fluxo…" → fluxograma.
  - "Do desenho para a lógica…" → pseudocódigo.
  - "Agora, no código…" → algoritmo.
  - "Vamos ao funcionamento…" → testes.
  - "Pensando em evolução…" → melhorias.
  - "Para fechar…" → conclusão.

- Dicas visuais:
  - Destacar variáveis e funções com caixas/realces ao explicar o código.
  - Usar zoom no terminal para outputs de sucesso/erro.
  - Inserir cronômetro discreto com tempo de cada seção.

- Preparação pré-gravação:
  - Conferir os arquivos: `fluxograma.jpg`, `pseudocodigo.txt`, `plano_testes.txt`, `melhorias_futuras.txt`.
  - Testar `python sistema_reservas.py` e validar os cenários do plano de testes.
  - Definir quem compartilha tela em cada seção e treinar as falas.

---

## Distribuição de Falas por Integrante

- Ana: Seções 1 (apresentação), 2 (requisitos), 7 (melhorias), parte da 8.
- Bruno: Seções 1 (objetivos), 3 (fluxo), 5 (código), parte da 8.
- Carla: Seções 1 (encaminhamento), 4 (pseudocódigo), 6 (testes), parte da 8.

---

## Checklist Rápido de Gravação

- Slides carregados; arquivos de apoio abertos em abas.
- Terminal pronto na pasta `c:\Users\Admin\Documents\AlgoritmosProg\av2`.
- Execução testada sem erros; exemplos de entrada ensaiados.
- Microfones e compartilhamento de tela funcionando.
- Tempo controlado para manter 10–12 minutos.