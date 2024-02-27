class vigenere():
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = ""
        self.message = ""
        self.cipher = ""

    def setKey(self, key):
        self.key = key

    def setMessage(self, message):
        self.message = message

    def encrypt(self):
        self.cipher = ""
        keyIndex = 0
        # Loop through each letter in the message
        for letter in self.message:
            # If the letter is in the alphabet
            if letter in self.alphabet:
                # Find the index of the letter in the alphabet
                letterIndex = self.alphabet.find(letter)
                # Find the letter in the key that corresponds to the current letter in the message
                keyLetter = self.key[keyIndex]
                # Find the index of the key letter in the alphabet
                keyLetterIndex = self.alphabet.find(keyLetter)
                # Add the letter to the cipher by finding the letter in the alphabet that is the sum of the letter index and the key letter index
                self.cipher += self.alphabet[(letterIndex + keyLetterIndex) % 26]
                # Move to the next letter in the key
                keyIndex = (keyIndex + 1) % len(self.key)
            else:
                self.cipher += letter
        return self.cipher

    def decrypt(self):
        message = ""
        keyIndex = 0
        for letter in self.cipher:
            if letter in self.alphabet:
                letterIndex = self.alphabet.find(letter)
                keyLetter = self.key[keyIndex]
                keyLetterIndex = self.alphabet.find(keyLetter)
                message += self.alphabet[(letterIndex - keyLetterIndex) % 26]
                keyIndex = (keyIndex + 1) % len(self.key)
            else:
                message += letter
        self.message = message
        return self.message

    def get_message(self):
        return self.message

    def get_cipher(self):
        return self.cipher

def main():
    v = vigenere()
    key = input("Enter the key: ")
    message = input("Enter the message: ")
    v.setKey(key.upper())
    v.setMessage(message.upper())
    v.encrypt()
    print("Encrypted Message:")
    print(v.get_cipher())
    print("Decrypted Message:")
    v.decrypt()
    print(v.get_message())

if __name__ == "__main__":
    main()