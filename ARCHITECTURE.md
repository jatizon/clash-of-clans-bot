# Arquitetura do Projeto - Clash of Clans Bot

## Visão Geral

Este projeto implementa um bot automatizado para o jogo Clash of Clans usando uma arquitetura baseada em **Behavior Trees** (Árvores de Comportamento). O bot utiliza detecção de imagens na tela e controle de mouse para interagir com o jogo.

## Estrutura de Diretórios

```
clash-of-clans-bot/
├── clash_of_clans_bot/
│   ├── __init__.py
│   ├── bot_main.py                    # Ponto de entrada principal
│   ├── btree.py                        # (Legado)
│   ├── coc_api.py                      # API do Clash of Clans
│   ├── coc_api_test.py                 # Testes da API
│   ├── test.py                         # Arquivo de testes
│   ├── buttons.json                    # Configuração de botões
│   │
│   ├── control/                        # Módulo de Controle
│   │   ├── controller.py               # Controlador principal (interface unificada)
│   │   ├── mouse_wrapper.py            # Wrapper para controle de mouse
│   │   └── screen_detector.py          # Detecção de imagens na tela
│   │
│   ├── bot_logic/                      # Lógica do Bot
│   │   ├── __init__.py
│   │   ├── status_enum.py              # Enum de status (SUCCESS, FAILURE, RUNNING)
│   │   │
│   │   ├── nodes/                      # Nós da Behavior Tree
│   │   │   ├── __init__.py
│   │   │   ├── node.py                 # Classe base Node
│   │   │   ├── action.py               # Nó Action
│   │   │   ├── sequence.py             # Nó Sequence
│   │   │   ├── selector.py              # Nó Selector
│   │   │   ├── repeat.py               # Nó Repeat
│   │   │   ├── parallel.py             # Nó Parallel
│   │   │   ├── inverter.py             # Nó Inverter
│   │   │   ├── always_success.py       # Nó AlwaysSuccess
│   │   │   ├── always_failure.py       # Nó AlwaysFailure
│   │   │   └── status.py                # Alias para StatusEnum
│   │   │
│   │   └── behaviors/                  # Comportamentos do Bot
│   │       ├── __init__.py
│   │       ├── behavior_tree.py        # Árvore de comportamento principal
│   │       │
│   │       ├── attack/                 # Comportamentos de Ataque
│   │       │   └── attack_main.py      # Comportamento principal de ataque
│   │       │
│   │       ├── homevillage/            # Comportamentos da Vila
│   │       │   ├── homevillage_main.py # Comportamento principal da vila
│   │       │   ├── collect_resources.py # Coleta de recursos
│   │       │   ├── new_achievement.py  # Novas conquistas
│   │       │   └── use_builder.py      # Uso de construtores
│   │       │
│   │       ├── util_behaviors/         # Comportamentos Utilitários
│   │       │   └── click_close_button.py # Clicar em botões de fechar
│   │       │
│   │       └── validate_screen/        # Validação de Tela
│   │           └── validate_screen_main.py
│   │
│   └── images/                         # Imagens de referência
│       ├── attacking/                   # Imagens de ataque
│       ├── common/                      # Imagens comuns
│       ├── home_village/                # Imagens da vila
│       └── shop/                        # Imagens da loja
│
├── pyproject.toml                       # Configuração do projeto
└── requirements.txt                     # Dependências
```

---

## Módulos Principais

### 1. Control Module (`clash_of_clans_bot/control/`)

Responsável pelo controle de hardware e detecção de elementos na tela.

#### `controller.py` - Controller

**Classe:** `Controller`

Interface unificada que encapsula todas as operações do bot. Recebe `mouse` e `screen_detector` no construtor.

**Métodos:**

- `__init__(self, mouse, screen_detector)`
  - Inicializa o controller com mouse e screen_detector

- `click_button(self, image_path, confidence=0.7, time_await=0.1, delta_x=0, delta_y=0) -> Status`
  - Procura uma imagem na tela e clica nela
  - Retorna `Status.SUCCESS` se encontrou e clicou, `Status.FAILURE` caso contrário

- `deploy_troops(self) -> Status`
  - Deploy aleatório de tropas (5 cliques aleatórios na tela)
  - Retorna `Status.SUCCESS`

- `check_image_exists(self, image_path, confidence=0.7) -> bool`
  - Verifica se uma imagem existe na tela
  - Retorna `True` se encontrada, `False` caso contrário

- `detect_on_screen(self, image_path, confidence=0.7, time_await=0.1) -> StatusEnum`
  - Detecta se uma imagem está na tela
  - Retorna `StatusEnum.SUCCESS` ou `StatusEnum.FAILURE`

- `adjust_screen(self) -> Status`
  - Ajusta a tela (zoom out + centraliza)
  - Retorna `Status.SUCCESS`

#### `mouse_wrapper.py` - MouseWrapper

**Classe:** `MouseWrapper`

Wrapper para controle de mouse usando `pyclick.HumanClicker` para movimentos mais naturais.

**Métodos:**

- `__init__(self, human_clicker)`
  - Inicializa com um HumanClicker

- `move(self, x, y, movement_duration=0.1)`
  - Move o mouse para coordenadas (x, y)

- `move_relative(self, dx, dy, movement_duration=0.1)`
  - Move o mouse relativamente à posição atual

- `move_to_center(self, movement_duration=0.1) -> Status`
  - Move o mouse para o centro da tela

- `center_screen(self) -> Status`
  - Centraliza a tela (zoom out + move + drag)

- `hold_down(self, button='left')`
  - Mantém o botão do mouse pressionado

- `release(self, button='left')`
  - Solta o botão do mouse

- `drag_screen(self, dx, dy, movement_duration=0.1)`
  - Arrasta a tela (drag)

- `click(self)`
  - Clica com o botão esquerdo

- `right_click(self)`
  - Clica com o botão direito

- `double_click(self)`
  - Duplo clique

- `zoom_out(self) -> Status`
  - Faz zoom out (scroll para baixo 10 vezes)

#### `screen_detector.py` - ScreenDetector

**Classe:** `ScreenDetector`

Responsável pela detecção de imagens na tela usando `pyautogui`.

**Métodos:**

- `__init__(self, images_path)`
  - Inicializa com o caminho base das imagens

- `_get_image_position(self, image_path, confidence) -> tuple | None`
  - Método privado que retorna a posição (x, y) de uma imagem na tela
  - Retorna `None` se não encontrada

- `detect_on_screen(self, image_path, confidence=0.7, time_await=0.1) -> StatusEnum`
  - Detecta se uma imagem está na tela
  - Retorna `StatusEnum.SUCCESS` ou `StatusEnum.FAILURE`

- `check_image_exists(self, image_path, confidence=0.7) -> bool`
  - Verifica se uma imagem existe na tela
  - Retorna `True` ou `False`

---

### 2. Bot Logic Module (`clash_of_clans_bot/bot_logic/`)

Implementa a lógica do bot usando Behavior Trees.

#### Status System

**Arquivo:** `status_enum.py`

**Classe:** `StatusEnum` (Enum)

Valores possíveis:
- `SUCCESS = 1` - Operação bem-sucedida
- `FAILURE = 2` - Operação falhou
- `RUNNING = 3` - Operação em andamento

**Arquivo:** `nodes/status.py`

Alias `Status = StatusEnum` para compatibilidade.

---

### 3. Nodes Module (`clash_of_clans_bot/bot_logic/nodes/`)

Implementação dos nós da Behavior Tree. Todos os nós herdam de `Node` e implementam o método `run(indent=0)`.

#### `node.py` - Node (Classe Base)

**Classe:** `Node`

Classe abstrata base para todos os nós da Behavior Tree.

**Métodos:**

- `run(self, indent=0) -> Status`
  - Método abstrato que deve ser implementado pelas subclasses
  - `indent`: nível de indentação para logging

- `_indent(self, level) -> str`
  - Retorna string de indentação para logging

- `_format_args_kwargs(self, args, kwargs) -> str`
  - Formata argumentos e kwargs para logging

#### `action.py` - Action

**Classe:** `Action(Node)`

Executa uma função arbitrária e retorna seu status.

**Métodos:**

- `__init__(self, action_func, *args, **kwargs)`
  - Inicializa com uma função e seus argumentos

- `run(self, indent=0) -> Status`
  - Executa a função e retorna seu status
  - Se a função não retornar Status, assume `Status.SUCCESS`

#### `sequence.py` - Sequence

**Classe:** `Sequence(Node)`

Executa filhos em sequência. Retorna `SUCCESS` apenas se todos os filhos retornarem `SUCCESS`. Para no primeiro `FAILURE` ou `RUNNING`.

**Métodos:**

- `__init__(self, children)`
  - Inicializa com lista de nós filhos

- `run(self, indent=0) -> Status`
  - Executa filhos sequencialmente
  - Mantém estado entre chamadas (continua de onde parou se `RUNNING`)

#### `selector.py` - Selector

**Classe:** `Selector(Node)`

Executa filhos até encontrar um que retorne `SUCCESS`. Retorna `FAILURE` apenas se todos falharem.

**Métodos:**

- `__init__(self, children)`
  - Inicializa com lista de nós filhos

- `run(self, indent=0) -> Status`
  - Tenta filhos até encontrar sucesso
  - Mantém estado entre chamadas (continua de onde parou se `RUNNING`)

#### `repeat.py` - Repeat

**Classe:** `Repeat(Node)`

Repete a execução de um filho um número determinado de vezes ou indefinidamente.

**Métodos:**

- `__init__(self, child, times=None, stop_on_failure=False, stop_on_success=False)`
  - `child`: nó filho a ser repetido
  - `times`: número de repetições (None = infinito)
  - `stop_on_failure`: parar se filho retornar FAILURE
  - `stop_on_success`: parar se filho retornar SUCCESS

- `run(self, indent=0) -> Status`
  - Repete a execução do filho
  - Mantém estado entre chamadas

#### `parallel.py` - Parallel

**Classe:** `Parallel(Node)`

Executa múltiplos filhos em paralelo (todos são executados a cada tick).

**Métodos:**

- `__init__(self, children, policy='Sequence')`
  - `children`: lista de nós filhos
  - `policy`: 'Sequence' (todos devem ter sucesso) ou 'Selector' (pelo menos um deve ter sucesso)

- `run(self, indent=0) -> Status`
  - Executa todos os filhos
  - Avalia resultados de acordo com a política
  - Mantém estado entre chamadas

#### `inverter.py` - Inverter

**Classe:** `Inverter(Node)`

Inverte o resultado do filho: `SUCCESS` vira `FAILURE` e vice-versa. `RUNNING` permanece `RUNNING`.

**Métodos:**

- `__init__(self, child)`
  - Inicializa com um nó filho

- `run(self, indent=0) -> Status`
  - Executa filho e inverte o resultado

#### `always_success.py` - AlwaysSuccess

**Classe:** `AlwaysSuccess(Node)`

Sempre retorna `SUCCESS`, independente do resultado do filho. `RUNNING` é propagado.

**Métodos:**

- `__init__(self, child)`
  - Inicializa com um nó filho

- `run(self, indent=0) -> Status`
  - Executa filho mas sempre retorna `SUCCESS` (exceto se `RUNNING`)

#### `always_failure.py` - AlwaysFailure

**Classe:** `AlwaysFailure(Node)`

Sempre retorna `FAILURE`, independente do resultado do filho. `RUNNING` é propagado.

**Métodos:**

- `__init__(self, child)`
  - Inicializa com um nó filho

- `run(self, indent=0) -> Status`
  - Executa filho mas sempre retorna `FAILURE` (exceto se `RUNNING`)

---

### 4. Behaviors Module (`clash_of_clans_bot/bot_logic/behaviors/`)

Comportamentos de alto nível do bot. Todos são funções que recebem `controller` como parâmetro e retornam uma Behavior Tree.

#### `behavior_tree.py` - BotLogicBehaviorTree

**Função:** `BotLogicBehaviorTree(controller) -> Node`

Árvore de comportamento principal do bot. Combina `HomeVillageBehavior` e `AttackBehavior` em paralelo.

**Estrutura:**
```
Repeat
└── Selector
    ├── Action(click_button, "reopen_game.png")
    └── Parallel (policy='Sequence')
        ├── HomeVillageBehavior
        └── AttackBehavior
```

#### `attack/attack_main.py` - AttackBehavior

**Função:** `AttackBehavior(controller) -> Node`

Comportamento de ataque. Inicia ataque, encontra match, e gerencia tropas durante o ataque.

**Estrutura:**
```
Sequence
├── Action(click_button, "start_attack_1.png")
├── Action(click_button, "find_match.png")
├── Action(click_button, "start_attack_2.png")
├── Repeat (times=20, stop_on_success=True)
│   └── Action(click_button, "barbarian_attack_icon.png")
└── Repeat (stop_on_success=True)
    └── Sequence
        ├── Action(deploy_troops)
        ├── AlwaysSuccess(Action(click_button, "barbarian_attack_icon.png"))
        └── Selector
            ├── Action(check_image_exists, "shop.png")
            └── Action(click_button, "return_home.png")
```

#### `homevillage/homevillage_main.py` - HomeVillageBehavior

**Função:** `HomeVillageBehavior(controller) -> Node`

Comportamento principal da vila. Executa múltiplos comportamentos em paralelo.

**Estrutura:**
```
Parallel (policy='Sequence')
├── Action(adjust_screen)
├── NewAchievementsBehavior
├── CollectResourcesBehavior
└── UseBuilderBehavior
```

#### `homevillage/collect_resources.py` - CollectResourcesBehavior

**Função:** `CollectResourcesBehavior(controller) -> Node`

Coleta recursos (ouro e elixir) em paralelo.

**Estrutura:**
```
Parallel (policy='Sequence')
├── Action(click_button, "gold_to_collect.png")
└── Action(click_button, "elixir_to_collect.png")
```

#### `homevillage/new_achievement.py` - NewAchievementsBehavior

**Função:** `NewAchievementsBehavior(controller) -> Node`

Gerencia novas conquistas.

**Estrutura:**
```
Parallel (policy='Sequence')
├── Sequence
│   ├── Action(click_button, "new_achievement.png")
│   └── Action(click_button, "claim_achievement.png")
└── Inverter(ClickCloseButtonUntilNotFoundBehavior)
```

#### `homevillage/use_builder.py` - UseBuilderBehavior

**Função:** `UseBuilderBehavior(controller) -> Node`

Usa construtores para construir e melhorar edifícios.

**Funções auxiliares:**
- `_NewBuildingBehavior(controller) -> Node`: Comportamento para construir novos edifícios
- `_UpgradeBuildingBehavior(controller) -> Node`: Comportamento para melhorar edifícios

**Estrutura:**
```
Repeat (times=5, stop_on_failure=True)
└── Selector
    ├── Parallel (policy='Sequence')
    │   ├── Sequence
    │   │   ├── Action(click_button, "builder_suggestions.png")
    │   │   ├── Action(click_button, "suggested_upgrades.png", delta_y=35)
    │   │   └── Selector
    │   │       ├── _NewBuildingBehavior
    │   │       └── _UpgradeBuildingBehavior
    │   └── Inverter(ClickCloseButtonUntilNotFoundBehavior)
    └── Parallel (policy='Sequence')
        ├── Sequence
        │   ├── Action(click_button, "builder_suggestions.png")
        │   ├── Action(click_button, "suggested_upgrades.png", delta_y=100)
        │   └── Selector
        │       ├── _NewBuildingBehavior
        │       └── _UpgradeBuildingBehavior
        └── Inverter(ClickCloseButtonUntilNotFoundBehavior)
```

#### `util_behaviors/click_close_button.py` - ClickCloseButtonUntilNotFoundBehavior

**Função:** `ClickCloseButtonUntilNotFoundBehavior(controller) -> Node`

Tenta clicar em botões de fechar até não encontrar mais nenhum.

**Estrutura:**
```
Repeat (stop_on_failure=True)
└── Selector
    ├── Action(click_button, "close_1_shop.png")
    ├── Action(click_button, "close_2_profile.png")
    └── Action(click_button, "shield_close.png")
```

#### `validate_screen/validate_screen_main.py` - ValidateScreenBehavior

**Função:** `ValidateScreenBehavior(controller) -> Node`

Valida a tela atual (implementação pendente).

**Função auxiliar:**
- `validate_screen()`: Função placeholder

---

## Fluxo de Execução

### 1. Inicialização (`bot_main.py`)

```python
1. Cria HumanClicker (pyclick)
2. Cria MouseWrapper com HumanClicker
3. Cria ScreenDetector com caminho das imagens
4. Cria Controller com MouseWrapper e ScreenDetector
5. Cria BotLogicBehaviorTree com Controller
6. Executa BotLogicBehaviorTree.tick()
```

### 2. Execução da Behavior Tree

A árvore é executada em ticks:
- Cada nó retorna `SUCCESS`, `FAILURE` ou `RUNNING`
- Nós com estado mantêm informações entre ticks
- A árvore continua executando até completar ou falhar

### 3. Fluxo de Dados

```
Controller
    ├── MouseWrapper (controle de mouse)
    └── ScreenDetector (detecção de imagens)
        └── pyautogui (biblioteca de automação)
```

---

## Dependências Principais

- `pyautogui`: Automação de mouse e teclado, detecção de imagens
- `pyclick`: Movimentos de mouse mais naturais (HumanClicker)
- `opencv-python`: Processamento de imagens (usado pelo pyautogui)
- `numpy`: Operações numéricas
- `Pillow`: Manipulação de imagens

---

## Padrões de Design

### 1. Behavior Tree Pattern
- Estrutura hierárquica de decisões
- Nós compostos (Sequence, Selector, Parallel)
- Nós decoradores (Inverter, AlwaysSuccess, AlwaysFailure)
- Nós folha (Action)

### 2. Facade Pattern
- `Controller` atua como fachada unificada para todas as operações
- Encapsula `MouseWrapper` e `ScreenDetector`

### 3. Strategy Pattern
- Diferentes comportamentos (AttackBehavior, HomeVillageBehavior) podem ser combinados
- Políticas em `Parallel` (Sequence vs Selector)

### 4. State Pattern
- Nós mantêm estado entre execuções (`_current_index`, `_running_child_index`, etc.)
- Permite execução incremental e resumível

---

## Convenções de Código

### Imports
- Todos os imports começam com `clash_of_clans_bot.` (raiz do módulo)
- Imports absolutos conforme `pyproject.toml`

### Behaviors
- Todos os behaviors são funções que recebem `controller` como parâmetro
- Retornam um nó da Behavior Tree
- Nomes em PascalCase (ex: `AttackBehavior`, `HomeVillageBehavior`)

### Status
- Usar `Status.SUCCESS`, `Status.FAILURE`, `Status.RUNNING`
- `Status` é um alias para `StatusEnum`

### Controller
- Todas as operações do bot devem passar pelo `Controller`
- Não acessar `controller.mouse` ou `controller.screen_detector` diretamente
- Usar métodos do `Controller` (ex: `controller.click_button()`, `controller.deploy_troops()`)

---

## Extensibilidade

### Adicionar Novo Comportamento

1. Criar função em `bot_logic/behaviors/`:
```python
def NewBehavior(controller):
    return Sequence([
        Action(controller.click_button, "image.png"),
        # ... mais ações
    ])
```

2. Adicionar à árvore principal em `behavior_tree.py`:
```python
def BotLogicBehaviorTree(controller):
    return Repeat(
        Selector([
            # ... comportamentos existentes
            NewBehavior(controller),
        ])
    )
```

### Adicionar Novo Método ao Controller

1. Adicionar método em `control/controller.py`:
```python
def new_method(self, ...):
    # Implementação usando self.mouse ou self.screen_detector
    return Status.SUCCESS
```

2. Usar em behaviors:
```python
Action(controller.new_method, ...)
```

---

## Logging

O sistema usa logging do Python para rastrear a execução:
- Cada nó loga sua execução com indentação
- Mostra status de cada filho
- Indica quando estado é salvo ou resetado

Nível de log configurado em `bot_main.py`:
```python
logging.basicConfig(level=logging.INFO, format='%(message)s')
```

---

## Notas de Implementação

1. **Estado Persistente**: Nós mantêm estado entre chamadas para permitir execução incremental
2. **Imagens**: Todas as imagens de referência estão em `clash_of_clans_bot/images/`
3. **Confiança**: Detecção de imagens usa `confidence=0.7` por padrão
4. **Timing**: Ações incluem delays (`time_await`) para garantir que a tela atualize

---

## Estrutura de Imagens

```
images/
├── attacking/          # Imagens durante ataque
├── common/             # Imagens comuns (botões de fechar, etc.)
├── home_village/       # Imagens da vila
└── shop/               # Imagens da loja
```

Todas as imagens são referenciadas por caminho relativo a partir de `clash_of_clans_bot/images/`.

