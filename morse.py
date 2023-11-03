class Morse():
    def __init__(self) -> None:
        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            ' ': ' ',  # Space char
        }

    def encode(self, text):
        morse_code = []
        for c in text:
            c = c.upper() #Morse Code is only in upper case
            if c in self.morse_code_dict:
                morse_code.append(self.morse_code_dict[c])
        return ''.join(morse_code)
    
    # def decode(self, text):
    #     # Split Morse code into individual characters and words
    #     words = text.split('  ')
    #     decoded_message = []

    #     for word in words:
    #         characters = word.split()
    #         decoded_word = ''

    #     for char in characters:
    #         matching_key = next((k for k, v in self.morse_code_dict.items() if v == char), None)
    #         if matching_key is not None:
    #             decoded_word += matching_key

    #         decoded_message.append(decoded_word)
    #     return ' '.join(decoded_message)
