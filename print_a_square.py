## Print a Square

# Print an nxn square of * characters. You will prompt the user to enter the number n. For n = 5, it should look like:
#
# ```
# *****
# *****
# *****
# *****
# *****
# ```

def print_a_square(num):
    for i in range(0, num):
        print "*" * num

num = int(raw_input("Number? "))
print_a_square(num)
