# Catch the Fish! (Desktop Game)

Interactive 2D desktop game built with Python and Pygame where the player controls a cat to catch falling fish within a limited time.

Designed to demonstrate real-time event handling, sprite animation, collision detection, sound integration, and responsive game UI development.


## Business Problem

Game development is one of the best ways to practice real-time programming concepts such as:

- Event-driven architecture  
- Continuous game loops  
- Dynamic object management  
- Collision detection  
- Multimedia integration  
- State management  

Many beginner projects focus only on static scripts, without demonstrating interactive real-time logic.

This project solves that by implementing a fully functional 2D desktop game with animation, scoring, timers, sound, and responsive design.


## Solution

**Catch the Fish!** is a complete desktop game built using Pygame.

The system includes:

- Start screen with interactive button  
- Main gameplay loop  
- Game-over screen with replay functionality  
- Animated cat sprite controlled by mouse movement  
- Random fish spawning with dynamic speed  
- Collision detection and score tracking  
- Countdown timer (60 seconds)  
- Resizable window with adaptive scaling  
- Background music integration  

The game uses structured state management to control transitions between screens and maintain a smooth gameplay experience.

## Key Features

### Gameplay Mechanics
- Mouse-controlled animated cat
- Randomly spawned falling fish
- Real-time collision detection
- Score increment on successful catch
- Countdown timer (60 seconds)
- Automatic game-over condition

### UI & Visual Features
- Start screen with hover-effect button
- Play Again screen
- Dynamic window resizing
- Adaptive scaling for:
  - Sprites
  - Fonts
  - Buttons
- Animated sprite frames (controlled FPS)
- Clean pastel-themed design

### Multimedia
- Background music (looped)
- Volume control via pygame.mixer
- PNG sprite assets


## Technical Architecture

The project is structured around a state-driven architecture:

### Game States
- `start`
- `game`
- `game_over`

### Core Components

- Main game loop with FPS control
- Separate functions for:
  - Start screen
  - Game loop
  - Game over screen
- Sprite animation using frame timers
- Dynamic object spawning using `pygame.Rect`
- Frame-independent timing using `pygame.time.get_ticks()`
- Collision detection via rectangle intersection
- Responsive scaling logic for images and fonts
- Continuous background music using `pygame.mixer`

This mirrors foundational principles used in 2D game development.


## Development Environment

- Language: Python 3.9.6  
- Library: Pygame  
- Operating System: macOS  
- Editor: VS Code  
- Assets & Sound: Itch.io  
- Sprite Editing: Piskelapp  


## Tech Stack

- Python 3.9.6  
- Pygame  
- pygame.mixer  
- Random module  
- Sys module  


## Project Structure

```
catch_the_fish/
│
├── main.py
├── sounds/
│   └── CatMusic.wav
├── assets/
│   ├── Box3-1.png
│   ├── Box3-2.png
│   ├── Box3-3.png
│   ├── Box3-4.png
│   └── Goldfish.png
├── PixelOperatorHB8.ttf
└── README.md
```


## Installation

1. Clone the repository:

```
git clone https://github.com/maria-python/catch_the_fish.git
cd catch_the_fish
```

2. Install dependencies:

```
pip install pygame
```


## Usage

Run the game:

```
python main.py
```


## Gameplay Workflow

1. Launch the application  
2. Click **START**  
3. Move the mouse to control the cat  
4. Catch falling fish to increase score  
5. Avoid missing fish  
6. Survive until timer reaches zero  
7. View final score  
8. Click **PLAY AGAIN** to restart  


## Results

- Demonstrates real-time game loop implementation  
- Shows sprite animation and frame management  
- Implements dynamic object spawning and cleanup  
- Integrates sound and multimedia  
- Applies responsive UI scaling  
- Uses structured state management  
- Simulates complete 2D desktop game architecture  


## Learning Outcomes

- Event-driven programming in Pygame  
- Animation timing and FPS control  
- Collision detection using Rect objects  
- Managing dynamic lists of game objects  
- Implementing timers and game duration logic  
- Handling window resizing and adaptive scaling  
- Integrating background music  
- Designing interactive UI buttons  


## Future Improvements

- Multiple difficulty levels  
- Increasing fish speed over time  
- Power-ups and bonus items  
- High-score saving system  
- Leaderboard functionality  
- Background scenery and particle effects  
- Sound effects for catching fish  
- Mobile adaptation  


## Author

Mariia Ilnitska  

Junior Python Automation / Tech Assistant  

**Contacts**

Gmail: maria.ilnitska11@gmail.com  

LinkedIn: www.linkedin.com/in/maria-ilnitska  

Telegram: @mariailnitska