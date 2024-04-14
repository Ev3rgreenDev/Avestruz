import multiprocessing
from mpmath import mp
from mpmath import *
import random
import time

mp.pretty=True

def calculate_pi(x):
    mp.dps = x
    pi = mp.pi
    print("Recurso 1 alocado, processo iniciando.")
    time.sleep(1)
    print(f"Processo 1 (π) será calculado:")
    print(pi)

def calc_fib(y):
    mp.dps = y
    fib = fibonacci(101)/fibonacci(100)
    print("Recurso 2 alocado, processo iniciando.")
    time.sleep(2)
    print("Processo 2 (FIBONACCI) será calculado:")
    print(fib)

def calc_euler(z):
    mp.dps = z
    euler = mp.e
    print("Recurso 3 alocado, processo iniciando.")
    time.sleep(3)
    print("Processo 3 (EULER) será calculado:")
    print(euler)

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
            print ("Deadlock encontrado, processo 1 será encerrado")
            # Terminate - may not work if process is stuck for good
            p1.terminate()
            p1.join()
        else:
            print("Recurso 1 liberado!")
        
        if p2.is_alive():
            print ("Deadlock encontrado, processo 2 será encerrado")
            p2.terminate()
            p2.join()
        else:
            print("Recurso 2 liberado!")
        
        if p3.is_alive():
            print ("Deadlock encontrado, processo 3 será encerrado")
            p3.terminate()
            p3.join()
        else:
            print("Recurso 3 liberado!")
