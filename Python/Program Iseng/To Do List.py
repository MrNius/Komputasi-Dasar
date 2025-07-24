class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Tugas '{}' ditambahkan.".format(task))

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Tugas '{}' dihapus.".format(task))
        else:
            print("Tugas '{}' tidak ditemukan.".format(task))

    def show_tasks(self):
        print("Daftar Tugas:")
        for index, task in enumerate(self.tasks, start=1):
            print("{}. {}".format(index, task))


def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            task = input("Masukkan nama tugas: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Masukkan nama tugas yang ingin dihapus: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Keluar dari program To-Do List")
            break
        else:
            print("Opsi tidak valid. Pilih 1, 2, 3, atau 4.")


if __name__ == "__main__":
    main()
