from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)

tasks = []

def show_banner():
    banner = pyfiglet.figlet_format("TO-DO LIST")
    print(Fore.CYAN + banner)

def show_menu():
    print(Fore.MAGENTA + "\n--- MENU ---")
    print(Fore.YELLOW + "1." + Fore.WHITE + " + add task")
    print(Fore.YELLOW + "2." + Fore.WHITE + " * show All tasks")
    print(Fore.YELLOW + "3." + Fore.WHITE + " ✔ mark task as done")
    print(Fore.YELLOW + "4." + Fore.WHITE + " x delete a task")
    print(Fore.YELLOW + "5." + Fore.WHITE + " <- exit")

def add_task():
    task = input(Fore.GREEN + "whats the task?: ")
    tasks.append({"title": task, "done": False})
    print(Fore.BLUE + "✔ task added!")

def list_tasks():
    if not tasks:
        print(Fore.RED + "no tasks here brochacho")
        return
    print(Fore.CYAN + "\nyour tasks:")
    for i, task in enumerate(tasks):
        status = Fore.GREEN + "✔ done" if task["done"] else Fore.RED + "x not done"
        print(f"{Fore.YELLOW}{i + 1}. {status} {Fore.WHITE}- {task['title']}")

def mark_done():
    list_tasks()
    try:
        i = int(input(Fore.GREEN + "which task is done? (number): ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            print(Fore.BLUE + "✔ task marked as done!")
        else:
            print(Fore.RED + "enter a number between 1-5")
    except ValueError:
        print(Fore.RED + "enter a number")

def delete_task():
    list_tasks()
    try:
        i = int(input(Fore.GREEN + "which task to delete? (number): ")) - 1
        if 0 <= i < len(tasks):
            tasks.pop(i)
            print(Fore.BLUE + "x task deleted")
        else:
            print(Fore.RED + "enter a number between 1-5")
    except ValueError:
        print(Fore.RED + "enter a number")

# loop roari
while True:
    show_banner()
    show_menu()
    choice = input(Fore.CYAN + "\nchoose an action (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print(Fore.YELLOW + "bye ho")
        break
    else:
        print(Fore.RED + "x Error try again")
