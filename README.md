# Clash of Clans Bot

Automation bot for Clash of Clans that uses computer vision and behavior trees to manage your village automatically.

## Features

- Automatic resource collection (gold and elixir)
- Builder and Laboratory upgrade management
- Automatic selection of suggested upgrades
- Automatic obstacle removal
- Attack system when resources are low
- Achievement rewards collection
- Automatic game state detection
- Disconnection and popup handling

## Architecture

The bot uses a Behavior Trees (BT) based architecture to organize decision logic and action execution. This architecture provides a modular and extensible structure where each behavior is defined as a tree of nodes.

### Behavior Trees

Behavior Trees are hierarchical structures that represent complex behaviors through the composition of simple nodes. Each node returns one of three possible statuses:

- **SUCCESS**: The action completed successfully
- **FAILURE**: The action failed
- **RUNNING**: The action is in progress and needs to continue on the next tick

### Node Types

The system implements the following node types:

#### Selector
Executes children in order until one returns SUCCESS. If a child returns RUNNING, the selector maintains state and continues from that child on the next tick. Returns FAILURE only if all children fail.

```python
Selector([
    Sequence([...]),  # Try this sequence first
    Sequence([...]),  # If it fails, try this
    Action(...)       # Last option
])
```

#### Sequence
Executes children in order until all return SUCCESS. If a child returns RUNNING, the sequence maintains state and continues from that child on the next tick. Returns FAILURE if any child fails.

```python
Sequence([
    Action(check_condition),  # First check
    Action(execute_action),    # Then execute
    Action(cleanup)            # Finally cleanup
])
```

#### Action
Encapsulates a controller function and executes it. Returns the status returned by the function (SUCCESS, FAILURE or RUNNING).

```python
Action(ctx.home_village_controller.check_has_builder)
```

#### AlwaysSuccess / AlwaysFailure
Decorators that force a specific status regardless of the child's result.

### State Structure

The bot manages different game states through the `StateController`, which automatically detects which screen the game is on. Each state has its own behavior tree:

- **HOME_VILLAGE**: Main village - manages resources, upgrades, obstacles
- **ATTACK**: During an attack - controls troops and combat actions
- **ATTACK_MENU**: Attack menu - prepares armies
- **SHOP**: Shop - manages purchases
- **PROFILE**: Player profile - collects rewards
- **UPGRADE_MENU**: Upgrade menu - confirms upgrades
- **HOMESCREEN_POPUP**: Homescreen popups - closes popups
- **DISCONNECTED**: Disconnected state - attempts to reconnect

The main `BotLogicBehaviorTree` uses a Selector that checks the current state and executes the corresponding behavior tree.

### Context and Controllers

The system uses a Context pattern that centralizes all controllers and shared resources:

- **Context**: Main container that maintains references to all controllers
- **Controllers**: Classes that encapsulate specific actions (mouse, vision, business logic)
- **Intention**: Intention system for communication between behaviors
- **Blackboard**: Shared data storage between behaviors

### Execution Flow

1. The main loop (`bot_main.py`) runs continuously
2. On each tick, the `StateController` detects the current game state
3. The `BotLogicBehaviorTree` selects the appropriate behavior tree for the state
4. The behavior tree is executed, returning SUCCESS, FAILURE or RUNNING
5. If RUNNING, execution continues on the next tick maintaining internal state
6. The process repeats

### Behavior Tree Example

```python
def HomeVillageBehavior(ctx):
    return (
        Sequence([
            AlwaysSuccess(Sequence([
                Action(ctx.intention.not_set),
                Action(ctx.home_village_controller.unselect_building),
                Action(ctx.home_village_controller.center_screen),
                Action(ctx.home_village_controller.try_collect_resources),
            ])),
            Selector([
                Sequence([
                    Action(ctx.home_village_controller.check_has_builder),
                    Action(ctx.home_village_controller.choose_builder_upgrade),
                ]),
                Sequence([
                    Action(ctx.home_village_controller.check_has_lab),
                    Action(ctx.home_village_controller.choose_lab_upgrade),
                ]),
                # ... other options
            ])
        ])
    )
```

This structure ensures that:
1. First executes always necessary actions (resource collection)
2. Then tries different options in priority order
3. Each action can return RUNNING to continue on the next tick

## Installation

### Prerequisites

- Python 3.8 or higher
- Clash of Clans installed and configured (preferably on Android emulator or PC)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/your-username/clash-of-clans-bot.git
cd clash-of-clans-bot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- `pyautogui`: Mouse and keyboard automation
- `opencv-python`: Image processing and computer vision
- `numpy`: Numerical operations
- `mss`: High-performance screen capture
- `python-dotenv`: Environment variable management
- `coc.py`: Clash of Clans API (optional)
- `Pillow`: Image processing
- `pyclick`: More human-like click simulation

## Usage

1. Make sure Clash of Clans is open and visible on screen
2. Run the bot:
```bash
python -m clash_of_clans_bot.bot_main
```

The bot will automatically detect the current game state and execute appropriate actions based on the corresponding behavior tree.

## Project Structure

```
clash-of-clans-bot/
├── clash_of_clans_bot/
│   ├── behaviors/          # Behavior trees for each state
│   │   ├── home_village_behavior.py
│   │   ├── attack_behavior.py
│   │   ├── upgrade_menu_behavior.py
│   │   └── ...
│   ├── context/            # Controllers and context management
│   │   ├── controllers/    # Specific action logic
│   │   ├── context.py      # Main container
│   │   ├── intention.py    # Intention system
│   │   └── blackboard.py   # Shared storage
│   ├── drivers/            # Low-level drivers
│   │   ├── mouse.py        # Mouse control
│   │   └── vision.py       # Image detection
│   ├── enums/              # Enumerators
│   │   ├── state_enum.py   # Game states
│   │   ├── status_enum.py  # Node statuses (SUCCESS/FAILURE/RUNNING)
│   │   └── state_behavior_map.py  # State -> behavior mapping
│   ├── images/             # Reference images for detection
│   │   ├── home_village/
│   │   ├── attack/
│   │   └── ...
│   ├── nodes/              # Behavior tree components
│   │   ├── node.py         # Base class
│   │   ├── selector.py     # Selector node
│   │   ├── sequence.py     # Sequence node
│   │   ├── action.py       # Action node
│   │   └── ...
│   └── bot_main.py         # Main entry point
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Configuration

The bot uses template matching-based image detection (OpenCV) to identify elements on screen. Reference images are located in `clash_of_clans_bot/images/`, organized by game state.

### Adding New Features

To add new features that require image detection:

1. Add the image to `clash_of_clans_bot/images/[state]/other/`
2. Create methods in the appropriate controller using `vision.get_image_position()` or `vision.is_image_on_screen()`
3. Add Actions to the corresponding behavior tree

### Creating New States

1. Add the new state to `enums/state_enum.py`
2. Create the controller in `context/controllers/`
3. Create the behavior tree in `behaviors/`
4. Add the mapping to `enums/state_behavior_map.py`
5. Add state detection to `context/controllers/state_controller.py`

## Important Warnings

- This bot is for educational and personal automation purposes
- Check Clash of Clans terms of service before using
- Bot usage may result in account ban
- Always test on a secondary account first
- Use at your own risk

## Contributing

Contributions are welcome. To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions, suggestions or issues, please open an issue on GitHub.

---

Note: This project is not affiliated, endorsed or sponsored by Supercell. Clash of Clans is a registered trademark of Supercell.
