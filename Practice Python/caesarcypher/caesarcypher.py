alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type encode or decode:")
text=input("Enter the text:")
text.lower()
shift=int(input("Enter the shift:"))
def encrypt(text,shift):
    encrypted_text=""
    for a in text:
        position=alphabet.index(a)
        shifted=position+shift
        new_alphabet=alphabet[shifted]
        encrypted_text+=new_alphabet
    print(f"Encrypted text is:{encrypted_text}")
def decrypt(text,shift):
    decrypted_text=""
    for a in text:
        position = alphabet.index(a)
        shifted = position-shift
        new_alphabet = alphabet[shifted]
        decrypted_text += new_alphabet
    print(f"Decrypted text is:{decrypted_text}")
if direction=="encode":
    encrypt(text, shift)
else:
    decrypt(text,shift)