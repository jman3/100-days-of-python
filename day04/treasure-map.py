line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# 🚨 Don't change the code above 👆
# Write your code below this row 👇

column = ["A", "B", "C"]
row = ["1", "2", "3"]

column_index = column.index(position[0])
row_index = row.index(position[1])

map[row_index][column_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")