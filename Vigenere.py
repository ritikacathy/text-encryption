text = 'Ritika Catherine!'
custom_key = 'chicken'

def vigenere(message, key, direction=2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    key_index = 0

    for char in message.lower():
        if not char.isalpha():
            # to check if the character is not alphabetic.
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)] # = key[0%6=0] = p
            # = key[6%6=0] = pythonp
            # = key[7%6=1] = pythonpy
            key_index += 1

            # declaring offset variable to find the index of python letters in alphabet
            offset = alphabet.index(key_char) # 15
            index =  alphabet.find(char) # find 'h' in alphabet
            # h is 7 in alphabet, in decryption l is 11
            new_index = (index + offset*direction) % len(alphabet) 
            # 7 + 15*2 % 26 = 37 % 26 = 11
            # for decryption: 11 + 15*-2 % 26 = -19 % 26 = 7
            encrypted_text += alphabet[new_index] # nothing + alphabet[11] = l
            # for decryption: = nothing + alphabet[7] = h
    return encrypted_text

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')