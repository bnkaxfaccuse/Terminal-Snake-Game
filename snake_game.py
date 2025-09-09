import curses
import random
import time

def main(stdscr):
    # Clear screen and initialize
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)
    stdscr.timeout(100)  # Snake speed (ms)

    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    stdscr.border(0)

    # Initial snake and food
    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    direction = curses.KEY_RIGHT

    # Initial food
    food = [random.randint(box[0][0], box[1][0]-1), random.randint(box[0][1], box[1][1]-1)]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    score = 0

    while True:
        stdscr.addstr(1, 2, f'Score: {score} ')
        stdscr.border(0)
        next_key = stdscr.getch()
        direction = direction if next_key == -1 else next_key

        # Calculate new head
        head = snake[0].copy()
        if direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1
        else:
            continue  # Ignore other keys

        # Game Over conditions
        if (head[0] in [box[0][0], box[1][0]] or
            head[1] in [box[0][1], box[1][1]] or
            head in snake):
            msg = "Game Over! Press 'q' to quit."
            stdscr.addstr(sh//2, sw//2 - len(msg)//2, msg)
            stdscr.nodelay(False)
            while stdscr.getch() != ord('q'):
                pass
            break

        snake.insert(0, head)

        # If snake eats food
        if head == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(box[0][0], box[1][0]-1),
                    random.randint(box[0][1], box[1][1]-1)
                ]
                if nf not in snake:
                    food = nf
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        stdscr.addch(head[0], head[1], '#')

if __name__ == "__main__":
    curses.wrapper(main)
