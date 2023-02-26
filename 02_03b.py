from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.hasPriority = hasPriority
        self.taskDesc = taskDesc
    def __str__(self):
        return f"Task: {self.taskDesc}, Priority: {self.hasPriority} "

toDoList = deque()

def add_task(task):
    if task.hasPriority:
        toDoList.appendleft(task)
    else:
        toDoList.append(task)

def do_task():
    return toDoList.popleft()

def print_tasks():
    for t in toDoList:
        print(t.taskDesc)
    print()



def main():
    print(toDoList)
    add_task(Task("Flow through foundational practices"))
    add_task(Task("Take a break", True))
    add_task(Task("Finish breakfast"))
    print_tasks()
    add_task(Task("Prioritise quests", True))
    print_tasks()
    do_task()
    add_task(Task("Tidy strategy board", True))
    print_tasks()

    return

if __name__ == "__main__":
    main()