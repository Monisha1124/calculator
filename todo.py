def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks

def clear_tasks(tasks):
    return []

if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Submit assignment")
    print(tasks)