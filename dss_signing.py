from dss_hash import modinv, hash_function

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Mengecek faktor-faktor dari 3 hingga akar kuadrat dari n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def key_generation(p, q, h, x):
    # Memastikan bahwa p dan q adalah bilangan prima
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("\n\nError: p and q must be prime numbers.\n\n\n")

    # Memastikan bahwa (p-1) mod q = 0
    if (p - 1) % q != 0:
        raise ValueError("\n\nError: (p-1) mod q must be 0.\n\n\n")

    # Memastikan bahwa 1 < h < p-1 dan h^((p-1)/q) mod p > 1
    if not (1 < h < p - 1) or pow(h, (p - 1) // q, p) <= 1:
        raise ValueError("\n\nError: Invalid value for h.\n\n\n")
    
    # Menghitung g = h^((p-1)/q) mod p
    g = pow(h, (p - 1) // q, p)

    # Memastikan bahwa x adalah bilangan positif kurang dari q
    if not (0 < x < q):
        raise ValueError("\n\nError: x must be a positive number less than q.\n\n\n")

    # Menghitung kunci publik y = g^x mod p
    y = pow(g, x, p)

    return g, y

def dss_sign(m, p, q, g, x, k):
    # Proses penandatanganan
    e = m
    r = (pow(g, k, p) % q)
    k_inv = modinv(k, q)
    s = (k_inv * (e + x * r)) % q
    return r, s

def main():

    kalimat = input("\nMasukkan kalimat (maksimum 64 karakter)\t\t: ")
    
    if len(kalimat) > 64:
        print("\n\nError: Jumlah karakter melebihi batas maksimum.\n\n\n")
        return
    
    # Input kunci privat dan nilai p, q, h
    p = int(input("\nMasukkan nilai p (bil. prima) \t\t\t: "))
    q = int(input("Masukkan nilai q (bil. prima) \t\t\t: "))
    h = int(input("Masukkan nilai h (1 < h < p-1) \t\t\t: "))
    x = int(input("\nMasukkan nilai kunci privat x (0 < x < q) \t: "))

    # Input kunci privat; nilai p, q, h; dan nilai acak
    k = int(input("Masukkan nilai acak (k) \t\t\t: "))
    
    # Nilai hash pesan
    m = hash_function(kalimat)

    try:
        # Melakukan key generation
        g, y = key_generation(p, q, h, x)
        
        # Menampilkan kunci privat dan publik
        print(f'\n\nKunci privat (x) \t\t= {x}')
        print(f'Kunci publik (p, q, g, y) \t= ({p}, {q}, {g}, {y})')

    except ValueError as e:
        print(e)

    # Proses penandatanganan
    r, s = dss_sign(m, p, q, g, x, k)
    print(f'\n\nTanda tangan (r, s) \t\t= ({r}, {s}) \n')

if __name__ == "__main__":
    main()
