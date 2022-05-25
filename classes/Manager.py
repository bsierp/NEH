from classes.Task import Task


class Manager:

    def __init__(self, filename):
        f = open(filename, "r")
        first_line = f.readline()
        first_line = [int(s) for s in first_line.split() if s.isdigit()]
        self.task_num = first_line[0]
        self.machine_num = first_line[1]
        self.task_array = []
        i = 0
        for line in f:
            i += 1
            self.task_array.append(Task(i, [int(s) for s in line.split() if s.isdigit()]))

    def calculate_cmax(self, t_list):
        c_list = [[0 for _ in range(self.machine_num + 1)] for _ in range(len(t_list) + 1)]
        for i in range(1, len(t_list)+1):
            for j in range(1, self.machine_num+1):
                c_list[i][j] = max(c_list[i - 1][j], c_list[i][j - 1]) + t_list[i - 1].machine_times[j - 1]
        return c_list[len(t_list)][self.machine_num]

    def calculate_permutation(self):
        weights = []
        permutation = []
        for task in self.task_array:
            weights.append(sum(task.machine_times))
        permutation.append(self.task_array.pop(weights.index(max(weights))))
        weights.pop(weights.index(max(weights)))
        for i in range(self.task_num-1):
            task = self.task_array.pop(weights.index(max(weights)))
            weights.pop(weights.index(max(weights)))
            c_list = []
            for j in range(2+i):
                permutation.insert(j, task)
                c_list.append(self.calculate_cmax(permutation))
                permutation.pop(j)
            permutation.insert(c_list.index(min(c_list)), task)
        return permutation
