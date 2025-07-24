import random

def main():
    print("Selamat datang di permainan Tebak Angka!")
    lower_limit = int(input("Masukkan batas bawah tebakan: "))
    upper_limit = int(input("Masukkan batas atas tebakan: "))
    
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    guess = None
    
    while guess != secret_number:
        guess = int(input("Tebak angka antara {} dan {}: ".format(lower_limit, upper_limit)))
        attempts += 1
        
        if guess < secret_number:
            print("Tebakan terlalu rendah!")
        elif guess > secret_number:
            print("Tebakan terlalu tinggi!")
    
    print("Selamat! Anda berhasil menebak angka {} dalam {} percobaan.".format(secret_number, attempts))

if __name__ == "__main__":
    main()
