# TODO: Make a dictionary of ASCII to Braille

# NOTE: I originally wanted to keep the braille as ints, but leading zeros are an issue. welp.
asciiToBraille = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    'space': '000000',      # blank character (000000) for spaces
    'caps': '000001'        # Source: https://braillebug.org/braille_deciphering.asp
}

# TODO: Make a function to convert
def solution(s):
    # Init outside because of scope
    convertedWord = ''

    # IDEA: Go through the entire word and append each character to the converted string
    for character in s:
        # CASE: Space
        if character == ' ':
            convertedWord += asciiToBraille.get('space')
        # CASE: Lowercase letter
        elif character == character.lower():
            convertedWord += asciiToBraille.get(character)
        # CASE: Uppercase letter
        else:
            convertedWord += asciiToBraille.get('caps') + asciiToBraille.get(character.lower())

    print(convertedWord)
    return convertedWord

solution('The quick brown fox jumps over the lazy dog')

# Expected Output: 000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
