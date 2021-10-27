#######Morse Code Translator by Karanjit Gill######

"""A Dictionary the various text, number, and symbol translations in Morse Code"""
Morse_code_trans = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}

text_to_translate = input("Please enter what you would like to translate into Morse Code: ").upper()
text_list = list(text_to_translate)
translationRead = ""
rawTranslation = ""
for trans_char in text_list:
    for morse_char in Morse_code_trans:
        if trans_char == morse_char:
            translationRead += "|" + trans_char + " " + Morse_code_trans.get(morse_char) + " "
            rawTranslation += Morse_code_trans.get(morse_char)
print(translationRead + "|")
print("Raw Morse Code: " + rawTranslation)
