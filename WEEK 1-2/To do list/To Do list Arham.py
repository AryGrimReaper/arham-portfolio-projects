# Empty list to store tasks
tasks = []

print("Welcome to your To-Do List App!")
print("Type 'done' when you're finished adding tasks.")

# Loop to collect tasks
while True:
    task = input("Enter a task: ")
    if task.lower() == "done":
        break
    tasks.append(task)

# Show all tasks
print("\nHere are your tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
