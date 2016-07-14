## Print a Box

# Given a height and width, print a box consisting of * characters as its border. You will prompt the user to enter the height and width. For example, given the height of 4 and the width of 6, you should print:
#
# ```
# ******
# *    *
# *    *
# ******
# ```

def print_a_box(height, width):
    for i in range(0, height):
        if i == 0 or i == (height - 1):
            print "*" * width
        else:
            print "*" + (" " * (width - 2)) + "*"

height = int(raw_input("height? "))
width = int(raw_input("width? "))

print_a_box(height, width)
