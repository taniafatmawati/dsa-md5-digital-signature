from dss_hash import modinv,hash_function

def dss_verify(m, r, s, p, q, g, y):
    # Proses verifikasi
    e = m
    s_inv = modinv(s, q)
    w = (s_inv % q)
    u1 = (e * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

def main():

    kalimat = input("\nMasukkan kalimat (maksimum 64 karakter)\t\t: ")
        
    if len(kalimat) > 64:
        print("\n\nError: Jumlah karakter melebihi batas maksimum.\n\n\n")
        return
    
    # Nilai hash pesan
    m = hash_function(kalimat)

    # Input kunci publik (p, q, g, y); tanda tangan (r, s)
    p = int(input("\nMasukkan nilai kunci publik (p) \t\t: "))
    q = int(input("Masukkan nilai kunci publik (q) \t\t: "))
    g = int(input("Masukkan nilai kunci publik (g) \t\t: "))
    y = int(input("Masukkan nilai kunci publik (y) \t\t: "))
    r = int(input("\nMasukkan nilai tanda tangan (r) \t\t: "))
    s = int(input("Masukkan nilai tanda tangan (s) \t\t: "))

    # Proses verifikasi
    is_verified = dss_verify(m, r, s, p, q, g, y)
    if is_verified:
        print('\n\n------------------------------------------')
        print('--- Tanda tangan digital terverifikasi ---')
        print('------------------------------------------\n\n')
    else:
        print('\n\n----------------------------------------')
        print('--- Tanda tangan digital tidak valid ---')
        print('----------------------------------------\n\n')

if __name__ == "__main__":
    main()
