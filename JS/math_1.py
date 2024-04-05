import multiprocessing
from mpmath import mp

precision = 10000000  # precisão desejada

def calculate_pi(precision):
    mp.dps = precision
    pi = mp.pi
    print(f"π será calculado:")
    print(pi)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=calculate_pi, args=(precision,))
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(5)

    # If thread is still active
    if p.is_alive():
        print ("Deadlock encontrado, processo será encerrado")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()



