allTask = []
if len(allTask) == 0:
    print('Nothing in Task. Please add something')
    task = input('Enter a task\n')
    allTask.append(task)
    print('Task added succesfullu')
else:
    task = input('enter a task')
    allTask.append(task)
    print('Task added succesfully')

val = int(input('Press 1 to show all tasks'))
if val == 1:
    for i in allTask:
        print(i)
