# Initialize an empty list to store the to-do items
to_do_list = []

# Function to add an item to the to-do list
def add_item():
    item = input("Please Enter the task: ")
    to_do_list.append(item)
    print(f"{item} Successfully Added!!")

# Function to display the to-do list
def display_list():
    print("To-Do List:")
    for index, item in enumerate(to_do_list, 1):
        print(f"{index}. {item}")

# Function to remove an item from the to-do list
def remove_item():
    display_list()
    try:
        index_to_remove = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index_to_remove < len(to_do_list):
            removed_item = to_do_list.pop(index_to_remove)
            print(f"{removed_item} Removed Successfully!!")
        else:
            print("Invalid input!! Re-Enter")
    except ValueError:
        print("Invalid input!! Re-Enter")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        display_list()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!! Re-Enter")