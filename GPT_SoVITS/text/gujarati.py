import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Refined Mapping for GPT-SoVITS
# We map Gujarati sounds to English ARPA phonemes that the model knows.

def g2p(text):
    # Transliterate to ITRANS
    itrans = transliterate(text, sanscript.GUJARATI, sanscript.ITRANS)
    
    # Mapping ITRANS syllables/chars to ARPA
    mapping = {
        'a': 'AH0', 'aa': 'AA1', 'i': 'IY0', 'ii': 'IY1', 'u': 'UH0', 'uu': 'UW1',
        'e': 'EY1', 'ai': 'AY1', 'o': 'OW1', 'au': 'AW1',
        'k': 'K', 'kh': 'K',
        'g': 'G', 'gh': 'G',
        'c': 'CH', 'ch': 'CH',
        'j': 'JH', 'jh': 'JH',
        't': 'T', 'th': 'T',
        'd': 'D', 'dh': 'D',
        'p': 'P', 'ph': 'F',
        'b': 'B', 'bh': 'B',
        'n': 'N', 'm': 'M', 'y': 'Y', 'r': 'R', 'l': 'L', 'v': 'V', 'w': 'W',
        'sh': 'SH', 's': 'S', 'h': 'HH'
    }
    
    # Simple segmentation: vowels and consonants
    phones = []
    i = 0
    text_len = len(itrans)
    while i < text_len:
        # Check 2-char combos
        if i + 1 < text_len and itrans[i:i+2].lower() in mapping:
            phones.append(mapping[itrans[i:i+2].lower()])
            i += 2
        elif itrans[i].lower() in mapping:
            phones.append(mapping[itrans[i].lower()])
            i += 1
        elif itrans[i] == ' ':
            phones.append(' ')
            i += 1
        else:
            i += 1
            
    return phones

def text_normalize(text):
    return text.strip()
