import sys
import os

# Add the project root to sys.path
sys.path.append(os.getcwd())

from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

# Gujarati text example: "મારું નામ રવિ છે" (My name is Ravi)
text = "મારું નામ રવિ છે"

# Transliterate Gujarati to IAST (International Alphabet of Sanskrit Transliteration)
# which is closer to phonetics than basic Romanization
iast_text = transliterate(text, sanscript.GUJARATI, sanscript.IAST)
print(f"Gujarati: {text}")
print(f"IAST: {iast_text}")

# Now let's try to map it to ILSL12 labels as provided by the user
# This is a manual mapping based on the user's provided list.
gu_to_ilsl = {
    'અ': 'a', 'આ': 'aa', 'ઇ': 'i', 'ઈ': 'ii', 'ઉ': 'u', 'ઊ': 'uu',
    'એ': 'e', 'ઐ': 'ai', 'ઓ': 'o', 'ઔ': 'au',
    'ક': 'k', 'ખ': 'kh', 'ગ': 'g', 'ઘ': 'gh', 'ઙ': 'ng',
    'ચ': 'c', 'છ': 'ch', 'જ': 'j', 'ઝ': 'jh', 'ઞ': 'nj',
    'ટ': 'tx', 'ઠ': 'txh', 'ડ': 'dx', 'ઢ': 'dxh', 'ણ': 'nx',
    'ત': 't', 'થ': 'th', 'દ': 'd', 'ધ': 'dh', 'ન': 'n',
    'પ': 'p', 'ફ': 'ph', 'બ': 'b', 'ભ': 'bh', 'મ': 'm',
    'ય': 'y', 'ર': 'r', 'લ': 'l', 'વ': 'w', 'શ': 'sh', 'ષ': 'sx', 'સ': 's', 'હ': 'h',
    'ળ': 'lx', 'ક્ષ': 'ksh', 'જ્ઞ': 'gn'
}

# Simple function to convert Gujarati to ILSL12 labels
# This is a naive implementation; a real one needs to handle matras (vowels) correctly.
def gujarati_to_ilsl(text):
    # Using a library to get phonemes is better, but let's see what IAST gives us.
    return transliterate(text, sanscript.GUJARATI, sanscript.ITRANS)

print(f"ITRANS: {gujarati_to_ilsl(text)}")
