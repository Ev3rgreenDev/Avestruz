import multiprocessing
from mpmath import mp # type: ignore
from mpmath import *
import random
import time

# myList = [10, 20, 15, 5, 10000000, 30]
# ranum = random.randint(0, 5)
# x = myList[ranum]
# precision = x  # precisão desejada
mp.pretty=True

def calculate_pi(x):
    mp.dps = x
    pi = mp.pi
    print("Recurso 1 alocado, processo iniciando.")
    time.sleep(1)
    print(f"π será calculado:")
    print(pi)
    print("Recurso 1 liberado!")

def calc_fib(y):
    mp.dps = y
    fib = fibonacci(101)/fibonacci(100)
    print("Recurso 2 alocado, processo iniciando.")
    time.sleep(2)
    print("Fibonacci será calculado:")
    print(fib)
    print("Recurso 2 liberado!")

def calc_euler(z):
    mp.dps = z
    euler = mp.e
    print("Recurso 3 alocado, processo iniciando.")
    time.sleep(3)
    print("Euler será calculado:")
    print(euler)
    print("Recurso 3 liberado!")


if __name__ == '__main__':
    print("Seus processos vão ser calculados:")
    time.sleep(1)
    while True:

        myList = [10, 20, 15, 5, 10000000, 30]
        ranum1 = random.randint(0, 5)
        ranum2 = random.randint(0, 5)
        ranum3 = random.randint(0, 5)
        x = myList[ranum1]
        y = myList[ranum2]
        z = myList[ranum3]

        # Start bar as a process
        p1 = multiprocessing.Process(target=calculate_pi, args=(x,))
        p2 = multiprocessing.Process(target=calc_fib, args=(y,))
        p3 = multiprocessing.Process(target=calc_euler, args=(z,))
        
        p1.start()
        p2.start()
        p3.start()

        # Wait for 10 seconds or until process finishes
        p1.join(5)
        p2.join(5)
        p3.join(5)

        # If thread is still active
        if p1.is_alive():
            print ("Deadlock encontrado, processo será encerrado")
            # Terminate - may not work if process is stuck for good
            p1.terminate()
            print("Recurso 1 liberado!")
            # OR Kill - will work for sure, no chance for process to finish nicely however
            # p.kill()
            p1.join()
        
        elif p2.is_alive():
            print ("Deadlock encontrado, processo será encerrado")
            p2.terminate()
            print("Recurso 2 liberado!")
            p2.join()
        
        elif p3.is_alive():
            print ("Deadlock encontrado, processo será encerrado")
            p3.terminate()
            print("Recurso 3 liberado!")
            p3.join()