# Terminal Snake Game

A classic "Snake" game implemented in Python using the `curses` library.  
Play directly in your terminal!

## Features

- Terminal UI (cross-platform with `curses`)
- Arrow key controls
- Randomly spawning food
- Score tracking
- Game over on wall or self-collision

## Requirements

- Python 3
- `curses` (included on Unix; on Windows, install with `pip install windows-curses`)

## How to Run

1. Clone this repository or save the `snake_game.py` file.
2. Open your terminal.
3. Run the game:

   ```bash
   python snake_game.py
   ```

4. Use the **arrow keys** to direct the snake.
5. After a game over, press **q** to quit.

## Notes

- Make sure your terminal window is at least ~24x80 for the best experience.
- On Windows, you may need to run:

   ```bash
   pip install windows-curses
   ```

## Screenshot

```
+------------------------------------------------------------------------------+
|                                                                              |
|   Score: 3                                                                   |
|                                                                              |
|                           #################                                  |
|                           #               #                                  |
|                           #               #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #        #      #                                  |
|                           #################                                  |
|                                                                              |
|                                   Game Over!                                 |
|                                Press 'q' to quit.                            |
+------------------------------------------------------------------------------+
```

## License

MIT License
