import threading
import time
import random

class PasaLoadProgram:
    def __init__(self):
        self.cellphone_loads = {}  # Dictionary to store cellphone numbers and corresponding loads
        self.lock = threading.Lock()  # Mutual exclusion lock

    def add_load(self, cellphone_number, amount):
        self.lock.acquire()  # Acquire the lock

        if cellphone_number in self.cellphone_loads:
            self.cellphone_loads[cellphone_number] += amount
        else:
            self.cellphone_loads[cellphone_number] = amount

        print(f"\nLoad of {amount} added to {cellphone_number}")

        self.lock.release()  # Release the lock

    def check_load_balance(self, cellphone_number):
        self.lock.acquire()  # Acquire the lock

        load = self.cellphone_loads.get(cellphone_number, 0)
        print(f"\nLoad balance of {cellphone_number}: {load}")

        self.lock.release()  # Release the lock

    def simulate_transaction(self):
        while True:
            print("\n1. Add Load")
            print("2. Check Load Balance")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                cellphone_number = input("\nEnter the cellphone number: ")
                amount = int(input("Enter the load amount: "))

                self.add_load(cellphone_number, amount)
                print()

                time.sleep(random.uniform(3, 6))  # Random delay after adding load

            elif choice == '2':
                cellphone_number = input("\nEnter the cellphone number to check load balance: ")
                self.check_load_balance(cellphone_number)
                print()

            elif choice == '3':
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    load_program = PasaLoadProgram()

    transaction_thread = threading.Thread(target=load_program.simulate_transaction)
    transaction_thread.start()

    transaction_thread.join()

    print("\nFinal Load Details:")
    for cellphone_number, load in load_program.cellphone_loads.items():
        print(f"Cellphone Number: {cellphone_number} | Load: {load}")
