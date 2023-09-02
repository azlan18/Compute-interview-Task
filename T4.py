# Initialize an empty list
my_list = []

# Read the number of commands
n = int(input("Enter the number of commands: "))

# Process each command
for _ in range(n):
    command = input().split()  # Read the command as a space-separated string
    action = command[0]  # Extract the action part of the command

    if action == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
    elif action == "print":
        print(my_list)
    elif action == "remove":
        e = int(command[1])
        my_list.remove(e)
    elif action == "append":
        e = int(command[1])
        my_list.append(e)
    elif action == "sort":
        my_list.sort()
    elif action == "pop":
        my_list.pop()
    elif action == "reverse":
        my_list.reverse()
