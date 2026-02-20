port time
from datetime import datetime

file_name = "task.txt"

def Task():
    try:
        with open(file_name,"r", encoding="utf-8") as file:
            a = file.read()
        print (f"{a}\n")
    except FileNotFoundError:
        print("file not found")

def Update():
    while True:
        it = input ("enter time duration: ")
        note = input ("write your teask: ")

        if not note or not it:
            print ("please enter your time duration and task!!")
            continue

        now = datetime.now().strftime("%I:%M %p")
        data = f"updated {now}| Time duration [{it} hours]| Your Task: {note}\n"
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(data)
        print ("save sucssfull")
        break

def Delet():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            read = file.read().splitlines()

        if not read:
            print("No tasks to delete!")
            return

        for index, item in enumerate(read, start=1):
            print(f"[{index}] {item}")

        choice = int(input("\nEnter task number to delete: "))
        
        if 1 <= choice <= len(read):
            deleted_item = read.pop(choice - 1)
            
            with open(file_name, "w", encoding="utf-8") as file:
                for task in read:
                    file.write(task + "\n")
            print(f"Successfully deleted: {deleted_item}")
        else:
            print("Invalid number!")

    except ValueError:
        print("Please enter a valid number!")
    except FileNotFoundError:
        print("File not found!")

action = """\nTo Do App
==================
[01] Today Task
[02] Update Task
[03] Delet Task
[04] Exit
"""
def main():
    while True:
        print(action)
        inp = input("Action number: ")

        if not inp:
            continue 

        match inp:
            case "1":
                Task()
            case "2":
                Update()
            case "3":
                Delet()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Press only 1-4")
                time.sleep(2)


if __name__=="__main__":
    main()
