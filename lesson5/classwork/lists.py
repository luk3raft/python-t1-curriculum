colors = ["red", "green", "blue", "yellow", "purple", "orange"]


print(colors)
print('first color:', colors[0])      
print('second color:', colors[1])     
print('third color:', colors[2])      
print('fouth color:', colors[3])      
print('fith color:', colors[5])      
print('sixth color:', colors[6])    
# Accessing and printing individual colors by their index  



colors.append("pink")
# Adding a new color to the end of the list
print("after append", colors)

colors.insert(2, "gray")
print("after insert", colors)

# Inserting a new color at index 2

colors.insert(0, "black")
# Inserting a new color at the beginning of the list
print("after insert", colors)

colors.remove("red")
# Removing the color "red" from the list
print("after remove", colors)

colors.pop()
# Removing the last color from the list and reterns it
print("after pop", colors)

popped_color = colors.pop()
# Removing the last color from the list and storing it in a variable
print("popped color:", popped_color)

print("after pop with variable", colors)

popped_color_at_index = colors.pop(2)
# Removing the color at index 2 and storing it in a variable

print("popped color at index 2:", popped_color_at_index)
print('list after popping at index 2:', colors)
colors.append("blue")
blue_count = colors.count("blue")
# Counting how many times "blue" appears in the list
print("number of blues:", blue_count)

index_of_yellow = color.index("yellow")
# Finding the index of the color "yellow" in the list
print("index of yellow:", index_of_yellow)
print("after pop at index 2", colors)
# Finding the index of a specific color in the list

colors.sort()
# for integers it does ascending order
# for strings it does alphabetical order
# for floats it does ascending order    
# Sorting the list of colors in alphabetical order
print("after sort", colors)

colors.sort(reverse=True)
# Sorting the list of colors in reverse alphabetical order
#equivalent to: colors.reverse() after colors.sort()
print("after sort reverse", colors)
print("length of colors list:", len(colors))
# Printing the length of the colors list
