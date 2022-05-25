from classes.Manager import Manager
import timeit
import tracemalloc


def main():

    m = Manager("test")
    start = timeit.default_timer()
    task_list = m.calculate_permutation()
    end = timeit.default_timer()
    print("Czas:", str(end - start).replace('.', ','))


if __name__ == "__main__":
    tracemalloc.start()
    main()
    print("Zużyta pamięć:", tracemalloc.get_traced_memory()[1], "Bajtów")
    tracemalloc.stop()

