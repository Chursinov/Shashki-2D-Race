# Shashki-2D-Race

2D game. Move car and avoid approaching obstacles. Simple Tkinter game with primitive gameplay.

## Controls
* You can control *player_car* using keyboard arrows (Left, Right), or [A] / [D] keys
* Try to avoid incoming obstacles, such as *road hole* or *green car*

## Code
* This minigame was made using tkinter.
  * Game consists of just 6 labels and 1 button:
    * *background_label*,
    * *player_label*,
    * *car_label*, 
    * *hole_label*,
    * *score_label*, 
    * *lose_label*,
    * *lose_button*.
  * Background is just an image in Label.
  * All objects, such as cars, holes are Tkinter.Labels. 
  * Loss window is a basic Label with text and button, that restarts the game.
* Minigame uses one infinite loop for all actions:
  * loop allows to move label down which gives the illusion of speed.
  * loop checks car collision.
  * loop checks coordinates of obstacles, and respawns them in case of exiting the window.
* Respawn method:
  * Game spawns two obstacles at random road lines and at a short distance from each other.
* Left and Right methods:
  * Game checks player's location and moves him to the next lane, according to the tapped key.
## Errors and bugs
  * It's a tkinter loop, so there are few bugs, such as:
    * in some frames obstacles can disappear.
    * when player recieve lose label, he can still move the car, that removes from the screen.
    * oncoming car can spawn with the road hole, creating mess in game window.
    * oncoming car and road hole can spawn in the same lines, as in previous loop.
## Plans
  * Add Tkinter.Scale to edit game road lines/
  * Fix old obstacles and add new, such as traffic cone, oil puddle, coin, adding +10 scores.
  * Add new themes to the game, like winter/rain and new car textures/colors.
  * Add *high score* and *new record* variable.
## Gameplay
![gameplay](https://github.com/Chursinov/Shashki-2D-Race/blob/master/gameplay.gif)
