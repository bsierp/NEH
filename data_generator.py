from random import randint

# A script that generates in a format that is accepted by algorithm
# f = open(input("Enter file name: "), 'w')
# task_quantity = int(input("Enter data quantity: "))
task_quantity = 10
machine_quantity = int(input("Enter machine quantity: "))
# machine_quantity = 10
f = open("test", "w")
f.write(str(task_quantity))
f.write(' ')
f.write(str(machine_quantity))
f.write('\n')
for i in range(0, task_quantity):
    for j in range(machine_quantity):
        f.write(str(randint(1, task_quantity)))
        f.write(' ')
    f.write('\n')
f.close()
