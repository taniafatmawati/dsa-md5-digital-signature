from dss_hash import modinv, hash_function

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Check for factors from 3 to the square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def key_generation(p, q, h, x):
    # Ensure that p and q are prime numbers
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("\n\nError: p and q must be prime numbers.\n\n\n")

    # Ensure that (p-1) mod q = 0
    if (p - 1) % q != 0:
        raise ValueError("\n\nError: (p-1) mod q must be 0.\n\n\n")

    # Ensure that 1 < h < p-1 and h^((p-1)/q) mod p > 1
    if not (1 < h < p - 1) or pow(h, (p - 1) // q, p) <= 1:
        raise ValueError("\n\nError: Invalid value for h.\n\n\n")
    
    # Calculate g = h^((p-1)/q) mod p
    g = pow(h, (p - 1) // q, p)

    # Ensure that x is a positive number less than q
    if not (0 < x < q):
        raise ValueError("\n\nError: x must be a positive number less than q.\n\n\n")

    # Calculate public key y = g^x mod p
    y = pow(g, x, p)

    return g, y

def dss_sign(m, p, q, g, x, k):
    # Signing process
    e = m
    r = (pow(g, k, p) % q)
    k_inv = modinv(k, q)
    s = (k_inv * (e + x * r)) % q
    return r, s

def main():

    kalimat = input("\n\nEnter sentence (maximum 64 characters)\t\t: ")
    
    if len(kalimat) > 64:
        print("\n\nError: Character count exceeds the maximum limit.\n\n\n")
        return
    
    # Input private key and values p, q, h
    p = int(input("\nEnter value p (prime number) \t\t\t: "))
    q = int(input("Enter value q (prime number) \t\t\t: "))
    h = int(input("Enter value h (1 < h < p-1) \t\t\t: "))
    x = int(input("\nEnter private key value x (0 < x < q) \t: "))

    # Input private key; values p, q, h; and random value
    k = int(input("Enter random value (k) \t\t\t: "))
    
    # Message hash value
    m = hash_function(kalimat)

    try:
        # Perform key generation
        g, y = key_generation(p, q, h, x)
        
        # Display private and public keys
        print(f'\n\nPrivate key (x) \t\t= {x}')
        print(f'Public key (p, q, g, y) \t= ({p}, {q}, {g}, {y})')

    except ValueError as e:
        print(e)

    # Signing process
    r, s = dss_sign(m, p, q, g, x, k)
    print(f'\n\nDigital Signature (r, s) \t\t= ({r}, {s}) \n\n')

if __name__ == "__main__":
    main()
