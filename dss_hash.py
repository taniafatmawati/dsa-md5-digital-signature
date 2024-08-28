# Variabel untuk fungsi F
F_operations = [
    ['ABCD', 0, 7, 1],
    ['DABC', 1, 12, 2],
    ['CDAB', 2, 17, 3],
    ['BCDA', 3, 22, 4],
    ['ABCD', 4, 7, 5],
    ['DABC', 5, 12, 6],
    ['CDAB', 6, 17, 7],
    ['BCDA', 7, 22, 8],
    ['ABCD', 8, 7, 9],
    ['DABC', 9, 12, 10],
    ['CDAB', 10, 17, 11],
    ['BCDA', 11, 22, 12],
    ['ABCD', 12, 7, 13],
    ['DABC', 13, 12, 14],
    ['CDAB', 14, 17, 15],
    ['BCDA', 15, 22, 16]
]

# Variabel untuk fungsi G
G_operations = [
    ['ABCD', 1, 5, 17],
    ['DABC', 6, 9, 18],
    ['CDAB', 11, 14, 19],
    ['BCDA', 0, 20, 20],
    ['ABCD', 5, 5, 21],
    ['DABC', 10, 9, 22],
    ['CDAB', 15, 14, 23],
    ['BCDA', 4, 20, 24],
    ['ABCD', 9, 5, 25],
    ['DABC', 14, 9, 26],
    ['CDAB', 3, 14, 27],
    ['BCDA', 8, 20, 28],
    ['ABCD', 13, 5, 29],
    ['DABC', 2, 9, 30],
    ['CDAB', 7, 14, 31],
    ['BCDA', 12, 20, 32]
]


# Variabel untuk fungsi H
H_operations = [
    ['ABCD', 5, 4, 33],
    ['DABC', 8, 11, 34],
    ['CDAB', 11, 16, 35],
    ['BCDA', 14, 23, 36],
    ['ABCD', 1, 4, 37],
    ['DABC', 4, 11, 38],
    ['CDAB', 7, 16, 39],
    ['BCDA', 10, 23, 40],
    ['ABCD', 13, 4, 41],
    ['DABC', 0, 11, 42],
    ['CDAB', 3, 16, 43],
    ['BCDA', 6, 23, 44],
    ['ABCD', 9, 4, 45],
    ['DABC', 12, 11, 46],
    ['CDAB', 15, 16, 47],
    ['BCDA', 2, 23, 48]
]

# Variabel untuk fungsi I
I_operations = [
    ['ABCD', 0, 6, 49],
    ['DABC', 7, 10, 50],
    ['CDAB', 14, 15, 51],
    ['BCDA', 5, 21, 52],
    ['ABCD', 12, 6, 53],
    ['DABC', 3, 10, 54],
    ['CDAB', 10, 15, 55],
    ['BCDA', 1, 21, 56],
    ['ABCD', 8, 6, 57],
    ['DABC', 15, 10, 58],
    ['CDAB', 6, 15, 59],
    ['BCDA', 13, 21, 60],
    ['ABCD', 4, 6, 61],
    ['DABC', 11, 10, 62],
    ['CDAB', 2, 15, 63],
    ['BCDA', 9, 21, 64]
]

# Variabel T[i]
T = [
    0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE, 0xF57C0FAF,
    0x4787C62A, 0xA8304613, 0xFD469501, 0x698098D8, 0x8B44F7AF,
    0xFFFF5BB1, 0x895CD7BE, 0x6B901122, 0xFD987193, 0xA679438E,
    0x49B40821, 0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA,
    0xD62F105D, 0x02441453, 0xD8A1E681, 0xE7D3FBCB, 0x21E1CDE6,
    0xC33707D6, 0xF4D50D87, 0x455A14ED, 0xA9E3E905, 0xFCEFA3F8,
    0x676F02D9, 0x8D2A4C8A, 0xFFFA3942, 0x8771F681, 0x69D96122,
    0xFDE5380C, 0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70,
    0x289B7EC6, 0xEAA127FA, 0xD4EF3085, 0x04881D05, 0xD9D4D039,
    0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665, 0xF4292244, 0x432AFF97,
    0xAB9423A7, 0xFC93A039, 0x655B59C3, 0x8F0CCC92, 0xFFEFF47D,
    0x85845DD1, 0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1,
    0xF7537E82, 0xBD3AF235, 0x2AD7D2BB, 0xEB86D391
]

# Fungsi konversi desimal ke biner
def destoBiner(input_desimal):
    if input_desimal == 0:
        return [0]

    binary = []
    temp_desimal = abs(input_desimal)

    while temp_desimal > 0:
        binary.append(temp_desimal % 2)
        temp_desimal //= 2

    binary.reverse()
    return binary

# Fungsi konversi biner ke desimal
def binerToDes(binary):
    desimal = 0
    for bit in binary:
        desimal = (desimal << 1) | bit
    return desimal

# Fungsi konversi desimal ke heksadesimal
def desimalToHex(input_desimal):
    return hex(input_desimal)

# Fungsi konversi heksadesimal ke desimal
def hexToDes(input_hex):
    return int(input_hex, 16)

# Fungsi konversi heksadesimal ke biner
def hex_to_bin(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    return binary_string.zfill((len(hex_string)-2) * 4)

# Fungsi konversi biner ke heksadesimal
def bin_to_hex(binary_string):
    hex_string = hex(int(binary_string, 2))[2:]
    return hex_string.upper()

def cls(value,l,s):
    # Lakukan CLS sebanyak s bit
    return ((value << s) | (value >> (l - s))) & 0xFFFFFFFF

# Fungsi putaran pertama MD5
def putaran(a, b, F, X, s, T):
    binary = hex_to_bin(hex(a + F + X + T))
    temp = cls((a + F + X + T),len(binary),s)
    # Hitung hasil putaran pertama
    a = b + temp
    return a & 0xFFFFFFFF

def fF(b, c, d):
    return (b & c) | (~b & d)

def fG(b, c, d):
    return (b & d) | (c & ~d)

def fH(b, c, d):
    return b ^ c ^ d

def fI(b, c, d):
    return c ^ (b & ~d)

def konversi_blok(kalimat):
    panjang_pesan = len(kalimat) * 8
    kalimat_bin = ''.join(format(ord(c), '08b') for c in kalimat)

    # Hitung panjang padding
    panjang_padding = (448 - (panjang_pesan + 8) % 512) % 512
    kalimat_bin += '1' + '0' * panjang_padding  # Tambahkan bit padding

    # Tambahkan panjang pesan di akhir, gunakan 64 bit
    panjang_pesan_bin = format(panjang_pesan, '064b')
    kalimat_bin += panjang_pesan_bin

    hasil_konversi = []
    for i in range(0, len(kalimat_bin), 32):
        blok_bin = kalimat_bin[i:i+32]
        blok_hex = '{:08X}'.format(int(blok_bin, 2))
        hasil_konversi.append(blok_hex)

    return hasil_konversi

def modinv(a, m):
    # Menghitung invers modulo a^(-1) mod m
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def hash_function (kalimat):
    hasil_konversi = konversi_blok(kalimat)

    # Inisialisasi buffer MD
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325467
    
    # Putaran
    for round_group in [F_operations, G_operations, H_operations, I_operations]:
        for row in range(16):
            X = hexToDes(hasil_konversi[round_group[row][1]])

            # Memilih fungsi berdasarkan round_group
            if round_group == F_operations:
                F_result = fF(b, c, d)
            elif round_group == G_operations:
                F_result = fG(b, c, d)
            elif round_group == H_operations:
                F_result = fH(b, c, d)
            elif round_group == I_operations:
                F_result = fI(b, c, d)

            # Memanggil putaran dengan parameter yang sesuai
            i = round_group[row][3]-1
            a = putaran(a, b, F_result, X, round_group[row][2], T[i])
            a, b, c, d = d, a, b, c

    # Tambahkan hasil akhir ke buffer MD5
    a = (a + 0x67452301) & 0xFFFFFFFF
    b = (b + 0xEFCDAB89) & 0xFFFFFFFF
    c = (c + 0x98BADCFE) & 0xFFFFFFFF
    d = (d + 0x10325467) & 0xFFFFFFFF

    # Format hasil akhir ke dalam satu nilai
    result_hex = f'{d:08X}{c:08X}{b:08X}{a:08X}'

    # Konversi ke desimal
    result_decimal = int(result_hex, 16)

    return result_decimal
