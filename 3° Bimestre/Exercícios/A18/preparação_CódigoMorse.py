CM = {
    ' ': '.......', 'A': '.-',    'B': '-...',
    'C': '-.-.',    'D': '-..',   'E': '.',
    'F': '..-.',    'G': '--.',   'H': '....',
    'I': '..',      'J': '.---',  'K': '-.-',
    'L': '.-..',    'M': '--',    'N': '-.',
    'O': '---',     'P': '.--.',  'Q': '--.-',
    'R': '.-.',     'S': '...',   'T': '-',
    'U': '..-',     'V': '...-',  'W': '.--',
    'X': '-..-',    'Y': '-.--',  'Z': '--..',
    
    '0': '-----',   '1': '.----', '2': '..---',
    '3': '...--',   '4': '....-', '5': '.....',
    '6': '-....',   '7': '--...', '8': '---..',
    '9': '----.'
}

frase = input("Digite uma frase: ").upper()

for c in frase:
    if c in CM:
       print(CM[c], end=" ")