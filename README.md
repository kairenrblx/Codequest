# Codequest by AI

A Python-based Minecraft-like game using Pyglet and OpenGL for rendering and NumPy for optimized calculations. The game features procedural world generation and a basic rendering engine using sammyers PythonCraft GitHub repository as a reference/example/template.

## 📂 Folder Structure
```
/Codequest
│── /worldgen              # World generation system
│   ├── generate_world.py  # Generates the world file
│   ├── world.json         # Stores world data
│── main_game.py           # Runs the main game
│── requirements.txt       # Dependencies (Pyglet, NumPy, Noise, OpenGL)
│── README.md              # Instructions for usage
```

## 🔄 How It Works
```plaintext
User runs generate_world.py  →  Saves world to worldgen/world.json
                    ↓
User runs main_game.py  →  Loads world.json  →  Renders world in Pyglet
                    ↓
         User interacts with the game (movement, blocks, etc.)
```

## ✅ How to Use
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Generate the World
```bash
python worldgen/generate_world.py
```

### 3️⃣ Run the Game
```bash
python main_game.py
```

## 📜 Dependencies (requirements.txt)
```
pyglet
numpy
noise
PyOpenGL
```

