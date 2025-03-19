# 🐍 Snake Game via Prompt Engineering
![snake-game-screenshot](https://github.com/user-attachments/assets/b531547d-7574-41e3-ada0-ddc18c68ccce)

**My first AI-assisted game development project** - A classic Snake Game created through iterative prompt engineering with ChatGPT.

## 🎮 Features
- **Progressive Difficulty**
  - New orange enemies appear every 5 foods collected
  - Child-friendly adjustable speed (FPS control
- **Score Tracking**
  - Real-time score display
  - Persistent high score system
- **Visual Customization**
  - Custom color scheme for all elements
  - Clean, modern aesthetic
- **Responsive Controls**
  - Arrow key movement
  - Instant restart functionality

## 🛠️ Installation
1. **Requirements**:
   - Python 3.6+
   - Pygame library

2. **Install dependencies**:
   ```bash
   pip install pygame

## ⚙️ Controls
- ↑ ↓ ← → : Move snake
- Q : Quit game
- C : Restart after game over

## 🎨 Customization
Modify these constants in `snake_game.py`:```python

# Visual Settings
BG_COLOR = (25, 25, 40)        # Background color
SNAKE_COLOR = (102, 255, 102)  # Snake color
FOOD_COLOR = (255, 76, 76)     # Food color
CELL_SIZE = 20                  # Game element size

# Difficulty Settings
FPS = 10                       # Game speed (8-15 recommended)
ENEMY_SPAWN_RATE = 5           # Foods between new enemies (1 food = 10 points)

📈 Development Journey
This project was built through AI-assisted prompt engineering:
- Base game structure via initial code prompts
- Progressive feature additions (high score, enemies, etc.)
- Visual customization through color parameter adjustments
- Difficulty balancing iterations
- Final code refinement and documentation

📁 File Structure
snake-game-via-prompt-engineering/
├── snake_game.py    # Main game code
├── README.md        # This documentation
└── requirements.txt # Python dependencies

🙌 Credits
- Developer: Wuillian F. Mendez
- AI Assistant: Deepseek
- Game Framework: Pygame

Created as an exploration of AI-assisted development 🤖💻
Perfect for beginners learning game development concepts!
