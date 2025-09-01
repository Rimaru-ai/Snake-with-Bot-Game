# Snake-with-Bot-Game
Classic Snake game with automated bot opponent and score tracking.
# Snake vs Bot 🐍🤖

A Python-based Snake game built with **turtle graphics** featuring:
- Classic Snake gameplay
- Automated Bot opponent
- Collision rules & score tracking

---

## 🎮 How to Play
- Control your snake with:
  - `W` → Up
  - `S` → Down
  - `A` → Left
  - `D` → Right
- Eat the food to grow and earn **+1 point**.
- Survive longer than the Bot snake.

---

## 🧩 Rules
- **Player hits wall or own body** → ❌ Game Over.
- **Player head hits Bot body** → ❌ Game Over (Bot wins).
- **AI hits wall or its own body** → Bot respawns at random position.
- **AI head hits Player body** → Bot dies + respawns, Player earns **+2 points**.
- Both snakes compete to reach the food.

---

## ⚙️ Installation
```bash
# Clone the repo
git clone https://github.com/your-username/Snake-with-Bot-Game.git
cd Snake-with-Bot-Game

# Run the game
 python main.py
