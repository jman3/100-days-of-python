day 6 - Python functions & Karel



## Escaping the maze

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# 1. make sure the robot has a wall on its right side
while front_is_clear():
    move()
turn_left()

# 2. follow along the right edge of the maze
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```


https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json