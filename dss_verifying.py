from dss_hash import modinv, hash_function

def dss_verify(m, r, s, p, q, g, y):
    # Verification process
    e = m
    s_inv = modinv(s, q)
    w = (s_inv % q)
    u1 = (e * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

def main():

    kalimat = input("\n\nEnter sentence (maximum 64 characters)\t\t: ")
        
    if len(kalimat) > 64:
        print("\n\nError: Character count exceeds the maximum limit.\n\n\n")
        return
    
    # Message hash value
    m = hash_function(kalimat)

    # Input public key (p, q, g, y); signature (r, s)
    p = int(input("\nEnter public key value (p) \t\t: "))
    q = int(input("Enter public key value (q) \t\t: "))
    g = int(input("Enter public key value (g) \t\t: "))
    y = int(input("Enter public key value (y) \t\t: "))
    r = int(input("\nEnter signature value (r) \t\t: "))
    s = int(input("Enter signature value (s) \t\t: "))

    # Verification process
    is_verified = dss_verify(m, r, s, p, q, g, y)
    if is_verified:
        print('\n\n------------------------------------------')
        print('--- Digital signature verified ---')
        print('------------------------------------------\n\n')
    else:
        print('\n\n----------------------------------------')
        print('--- Digital signature is invalid ---')
        print('----------------------------------------\n\n')

if __name__ == "__main__":
    main()
