from sys import argv

script, txt = argv

if txt == 'list':
    txt = open("tasks.txt")

    print "Here is your list"
    print txt.read()

if txt == 'add':
    new_task = raw_input("What would you like to add? ")
    txt = open("tasks.txt", "a")
    txt.write(new_task)
    txt.close()
    print "You added a new task!"


if txt == 'remove':
    task_to_remove = raw_input("What task would you like to remove? ")
