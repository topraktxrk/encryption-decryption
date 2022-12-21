import string
import os
import datetime

def encrypt_decrypt(text, shift, action):
    """
    Encrypts or decrypts the given text by shifting each character by the specified number of positions.
    
    Parameters:
        text (str): The text to be encrypted or decrypted.
        shift (int): The number of positions to shift each character.
        action (str): Specifies whether to encrypt or decrypt the text. Must be either 'encrypt' or 'decrypt'.
    
    Returns:
        str: The encrypted or decrypted text.
    """
    # Create a string containing all printable ASCII characters.
    ascii_printable = string.printable
    
    encrypted_text = ""
    for ch in text:
        # Check if the character is printable ASCII.
        if ch in ascii_printable:
            # Shift the character by the specified number of positions.
            if action == 'encrypt':
                encrypted_ch = chr((ord(ch) + shift) % 128)
            elif action == 'decrypt':
                # Shift the character by the opposite of the specified number of positions.
                encrypted_ch = chr((ord(ch) - shift) % 128)
            else:
                raise ValueError("Invalid action. Must be either 'encrypt' or 'decrypt'.")
        else:
            # Leave non-printable ASCII characters unchanged.
            encrypted_ch = ch
        encrypted_text += encrypted_ch
    return encrypted_text

# Get the text from the user.
text = input("Enter the text to be encrypted or decrypted: ")

# Get the shift value from the user.
shift = int(input("Enter the shift value: "))

# Get the action (encrypt or decrypt) from the user.
action = input("Enter 'encrypt' to encrypt the text or 'decrypt' to decrypt it: ")

# Encrypt or decrypt the text.
encrypted_text = encrypt_decrypt(text, shift, action)

# Construct the file path.
file_path = os.path.join(os.getcwd(), 'encrypted_text.txt')

# Check if a file with the same name already exists.
if os.path.exists(file_path):
    # Increment the number at the beginning of the filename.
    i = 1
    while os.path.exists(file_path):
        file_path = os.path.join(os.getcwd(), f'{i}_encrypted_text.txt')
        i += 1

# Save the result to the file.
with open(file_path, 'w') as f:
    f.write(encrypted_text)
