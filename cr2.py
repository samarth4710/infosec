import random
import math

# these are some required functions main code starts from line 109
# Caesar cipher
def caesar_cipher(input_text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_text = input_text.lower()
    output = ""

    for char in input_text:
        if char == " ":
            output += " "
        elif char in alphabet:
            loc = alphabet.find(char)
            new_loc = (loc + shift) % 26
            output += alphabet[new_loc]
        else:
            output += char

    return output


def encrypt_caesar():
    inp = input("Enter Message: ")
    shift = int(input("Please input shift key (just enter any positive integer): "))
    encrypted_message = caesar_cipher(inp, shift)
    print("Encrypted Message:", encrypted_message)


# Substitution cipher
def decrypt_caesar():
    out = input("Enter the encrypted message: ")
    shift = int(input("Please input shift key required to decrypt message: "))
    decrypted_message = caesar_cipher(out, -shift)
    print("Decrypted Message:", decrypted_message)


def generate_substitution_key():
    lotus = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    key = list(lotus)
    random.shuffle(key)
    return key


def substitution_cipher(text, lotus, key):
    output = ""
    for char in text:
        if char in lotus:
            loc = lotus.index(char)
            output += key[loc]
        else:
            output += char
    return output


def encrypt_substitution():
    lotus = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    key = generate_substitution_key()
    print("Characters:", lotus)
    print("       Key:", ''.join(key))

    inp = input("Enter message to be encrypted: ")
    encrypted_message = substitution_cipher(inp, lotus, key)
    print("Encrypted Message:", encrypted_message)


def decrypt_substitution():
    lotus = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="

    out = input("Enter the message to be decrypted: ")
    key = list(input("Enter the key: "))

    decrypted_message = substitution_cipher(out, key, lotus)
    print("Decrypted Message:", decrypted_message)


# RSA
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def new_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def mod_inverse(e, phi):
    for l in range(3, phi):
        if (l * e) % phi == 1:
            return l


# Diffie-Hellman
def calculate_public_key(prime, generator, private_key):
    return pow(generator, private_key, prime)


def calculate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)


print('''
                       _                              _           
                      | |                            | |          
  ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| '__| | | | '_ \\| __/ _ \\ / _` | '__/ _` | '_ \\| '_ \\| | | |
| (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \\___|_|   \\__, | .__/ \\__\\___/ \\__, |_|  \\__,_| .__/|_| |_|\\__, |
            __/ | |              __/ |         | |           __/ |
           |___/|_|             |___/          |_|          |___/ ''')


while True:
    hammer = int(input('''
    Which method would you like to use:
    press the number corresponding to your desired choice
    
    CAESAR CYPHER -- 1
    SUBSTITUTION CYPHER -- 2
    RSA ENCRYPTION -- 3
    DIFFIE-HELLMAN -- 4
    TO STOP FUNCTION -- 5
    Number? = '''))

    if hammer == 1:
        while True:
            knife = int(input('''
            Do you want to encrypt or decrypt a message?
            Press 1 to encrypt
            Press 2 to decrypt
            Press 3 to stop function
            Number? = '''))
            if knife == 1:
                encrypt_caesar()
                break
            elif knife == 2:
                decrypt_caesar()
                break
            elif knife == 3:
                break
            else:
                print('''
                                            PLEASE ENTER VALID NUMBER''')
        break

    elif hammer == 2:
        while True:
            rope = int(input('''
            Do you want to encrypt or decrypt a message?
            Press 1 to encrypt
            Press 2 to decrypt
            Press 3 to stop function
            Number? = '''))
            if rope == 1:
                encrypt_substitution()
                break
            elif rope == 2:
                decrypt_substitution()
                break
            elif rope == 3:
                break
            else:
                print('''
                                            PLEASE ENTER VALID NUMBER''')
        break

    elif hammer == 3:
        while True:
            gun = int(input('''
            Do you want to encrypt or decrypt a message?
            Press 1 to encrypt
            Press 2 to decrypt
            Press 3 to stop function
            Number? = '''))
            if gun == 1:
                while True:
                    toy = int(input('''
                    If you want to generate public key and modulus common to public and private key, press 1  
                    If you have public key and modulus common to public and private key, press 2
                    to stop function press 3 
                    Number? = '''))
                    if toy == 1:
                        p, q = new_prime(1000, 4000), new_prime(1000, 4000)

                        while p == q:
                            q = new_prime(1000, 4000)

                        n = p * q
                        phi_n = (p - 1) * (q - 1)

                        e = random.randint(3, phi_n)
                        while math.gcd(e, phi_n) != 1:
                            e = random.randint(3, phi_n - 1)

                        d = mod_inverse(e, phi_n)

                        print("Public Key: ", e)
                        print("Private Key: ", d)
                        print("Modulus common to public and private key: ", n)

                        message = input("Write a message to be encrypted: ")
                        cipher_text = [pow(ord(char), e, n) for char in message]
                        print("encrypted message :", cipher_text)
                        break

                    elif toy == 2:
                        e = int(input("Enter private key: "))
                        n = int(input("Enter modulus common to public and private key: "))
                        message = input("Write a message to be encrypted: ")
                        cipher_text = [pow(ord(char), e, n) for char in message]
                        print("encrypted message :", cipher_text)
                        break

                    elif toy == 3:
                        break
                    else:
                        print('''
                                                   PLEASE ENTER VALID NUMBER''')
                break
            elif gun == 2:
                d = int(input("Enter private key: "))
                n = int(input("Enter modulus common to public and private key: "))
                cipher_text_str = input("Enter the message to be decrypted in the form of a list of numbers separated by spaces: ")
                cipher_text_list = [int(num) for num in cipher_text_str.split()]
                decrypted_message = ''.join([chr(pow(char, d, n)) for char in cipher_text_list])
                print("Decrypted Message:", decrypted_message)
                break

            elif gun == 3:
                break
            else:
                print('''
                                            PLEASE ENTER VALID NUMBER''')
        break
    elif hammer == 4:
        while True:
            brick = int(input('''
            Do you want to encrypt or decrypt a message?
            Press 1 to encrypt
            Press 2 to decrypt
            Press 3 to stop function
            Number? = '''))
            if brick == 1:
                while True:
                    rod = int(input('''
                    If you want to generate sender's public key, your private key, and common prime, press 1 
                    If you have sender's public key, your private key, and common prime, press 2 
                    to stop function press 3 
                    Number? = '''))

                    if rod == 1:
                        p = new_prime(1000, 7000)
                        generator = random.randint(2, p - 1)
                        your_private_key = random.randint(2, p - 1)
                        senders_private_key = random.randint(2, p - 1)

                        your_public_key = calculate_public_key(p, generator, your_private_key)
                        senders_public_key = calculate_public_key(p, generator, senders_private_key)

                        print("Common prime:", p)
                        print("Sender's public key:", senders_public_key)
                        print("Your public key:", your_public_key)
                        print("Sender's private key:", senders_private_key)
                        print("Your private key:", your_private_key)

                        your_shared_secret = calculate_shared_secret(p, senders_public_key, your_private_key)
                        print("Your encrypted message is:", your_shared_secret)
                        break

                    elif rod == 2:
                        s = int(input("Enter sender's public key: "))
                        y = int(input("Enter your private key: "))
                        pn = int(input("Enter common prime number: "))
                        your_shared_secret = calculate_shared_secret(pn, s, y)
                        print("Your encrypted message is:", your_shared_secret)
                        break

                    elif rod == 3:
                        break
                    else:
                        print('''
                                                    PLEASE ENTER VALID NUMBER''')
                break
            elif brick == 2:
                s = int(input("Enter sender's private key: "))
                y = int(input("Enter your public key: "))
                pn = int(input("Enter common prime number: "))
                your_shared_secret = calculate_shared_secret(pn, y, s)
                print("Your encrypted message is:", your_shared_secret)
                break

            elif brick == 3:
                break
            else:
                print('''
                                            PLEASE ENTER VALID NUMBER''')

    elif hammer == 5:
        break

    else:
        print('''
                                    PLEASE ENTER VALID NUMBER''')
    break