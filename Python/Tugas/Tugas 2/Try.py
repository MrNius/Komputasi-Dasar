import random

# Fungsi untuk menghasilkan data acak
def generate_data(num_data):
    data = [random.randint(0, 100) for _ in range(num_data)]
    return data

# Fungsi untuk menghitung distribusi frekuensi
def calculate_frequency(data):
    frequency = [0] * 101 
    
# Inisialisasi array frekuensi dengan 101 elemen (0-100)
    for value in data:
        frequency[value] += 1
    return frequency

# Fungsi untuk menampilkan grafik batang
def display_histogram(frequency):
    for i, count in enumerate(frequency):
        if count > 0:
            print(f'{i}: {"*" * count}')

def main():
    try:
        num_data = int(input("Masukkan jumlah data yang akan dikembalikan "))
        if num_data < 1:
            print("Jumlah data harus lebih besar dari 0.")
            return

        data = generate_data(num_data)
        frequency = calculate_frequency(data)
        display_histogram(frequency)
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
