class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        current = self.head
        while current:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                break
            current = current.next

    def viewToDoList(self):
        current = self.head
        if not current:
            print("ToDo List is empty.")
        else:
            print("ToDo List:")
        while current:
            task = current.task
            if task.isCompleted:
                completed = "Yes"
            else:
                return"No"
            print("Title:", task.getTitle(), "- Description:", task.getDescription(), "- Completed:", completed)
            current = current.next
def display_menu():
    print("Todo List Menu:")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. View Todo List")
    print("4. Exit")


def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.addToDo(task)
            print("Task added successfully!")

        elif choice == "2":
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.markToDoAsCompleted(title)
            print("Task marked as completed.")

        elif choice == "3":
            todo_list.viewToDoList()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
