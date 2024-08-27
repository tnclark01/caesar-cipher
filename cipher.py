def caesar_cipher(text, shift):
    result = []

    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Compute the new character with the shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Compute the new character with the shift
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            # Non-alphabetical characters are added as-is
            result.append(char)
    
    return ''.join(result)

# Usage
if __name__ == "__main__":
    text = "GO BIG BLUE!"
    shift = 5
    encrypted_text = caesar_cipher(text, shift)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
# add your code here
