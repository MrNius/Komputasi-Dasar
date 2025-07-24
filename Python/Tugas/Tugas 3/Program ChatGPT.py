import math

# Fungsi-fungsi yang diberikan
def f0(x):
    return 0

def f1(x):
    return x

def f2(x):
    return (x - 2) ** 2

def f3(x):
    return 10 * math.sin(x)

def f4(x):
    return math.exp(x)

# Fungsi untuk membuat plot primitif
def create_primitive_plot(func, x_min, x_max, partitions):
    x_values = []
    y_values = []
    x_step = (x_max - x_min) / partitions
    x = x_min
    while x <= x_max:
        y = func(x)
        x_values.append(x)
        y_values.append(y)
        x += x_step

    return x_values, y_values

# Fungsi untuk menampilkan plot primitif
def display_primitive_plot(x_values, y_values):
    y_min = min(y_values)
    y_max = max(y_values)
    y_step = (y_max - y_min) / 40

    print("[xmin, xmax] = [{:.2f}, {:.2f}]".format(min(x_values), max(x_values)))
    print("[ymin, ymax] = [{:.2f}, {:.2f}]".format(y_min, y_max))

    for y in reversed(range(41)):
        line = ""
        for i in range(len(x_values)):
            if y_values[i] >= y_min + y * y_step:
                line += "*"
            else:
                line += " "
        print(line)

# Fungsi untuk membuat plot daerah antara dua fungsi
def create_area_plot(func1, func2, x_min, x_max, partitions):
    x_values = []
    y_min_values = []
    y_max_values = []
    x_step = (x_max - x_min) / partitions
    x = x_min
    while x <= x_max:
        y1 = func1(x)
        y2 = func2(x)
        x_values.append(x)
        y_min_values.append(min(y1, y2))
        y_max_values.append(max(y1, y2))
        x += x_step

    return x_values, y_min_values, y_max_values

# Fungsi untuk menampilkan plot daerah antara dua fungsi
def display_area_plot(x_values, y_min_values, y_max_values):
    y_min = min(y_min_values)
    y_max = max(y_max_values)
    y_step = (y_max - y_min) / 40

    print("[xmin, xmax] = [{:.2f}, {:.2f}]".format(min(x_values), max(x_values)))
    print("[ymin, ymax] = [{:.2f}, {:.2f}]".format(y_min, y_max))

    for y in reversed(range(41)):
        line = ""
        for i in range(len(x_values)):
            if y_min_values[i] <= y_min + y * y_step <= y_max_values[i]:
                line += "*"
            else:
                line += " "
        print(line)

# Fungsi untuk mengambil input jumlah partisi
def get_partitions():
    while True:
        try:
            partitions = int(input("Masukkan jumlah partisi pada sumbu x dan y: "))
            if partitions >= 1:
                return partitions
            else:
                print("Jumlah partisi harus lebih dari atau sama dengan 1.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Program utama
if __name__ == "__main__":
    # Fungsi-fungsi yang diplot dan daerah asal fungsi
    functions = [f0, f1, f2, f3, f4]
    xmin_values = [0, 0, 0, -math.pi, -1]
    xmax_values = [1, 1, 5, 2 * math.pi, 3]

    # Menampilkan pilihan fungsi
    print("Pilihan Fungsi:")
    for i, func in enumerate(functions):
        print(f"{i + 1}. {func.__doc__}")

    choice = int(input("Pilih nomor fungsi yang ingin diplot: ")) - 1
    xmin = xmin_values[choice]
    xmax = xmax_values[choice]

    partitions = get_partitions()

    if choice == 0:
        x_values, y_values = create_primitive_plot(f0, xmin, xmax, partitions)
        display_primitive_plot(x_values, y_values)
    else:
        x_values, y_min_values, y_max_values = create_area_plot(f1, functions[choice], xmin, xmax, partitions)
        display_area_plot(x_values, y_min_values, y_max_values)
