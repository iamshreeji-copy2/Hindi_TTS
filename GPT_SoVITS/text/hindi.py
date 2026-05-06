import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Refined ARPA mapping for Hindi
def g2p(text):
    # GPT-SoVITS English ARPA symbols
    arpa_symbols = {
        "AH0", "S", "AH1", "EY2", "AE2", "EH0", "OW2", "UH0", "NG", "B", "G", "AY0", "M", "AA0", "F", "AO0", 
        "ER2", "UH1", "IY1", "AH2", "DH", "IY0", "EY1", "IH0", "K", "N", "W", "IY2", "T", "AA1", "ER1", "EH2", 
        "OY0", "UH2", "UW1", "Z", "AW2", "AW1", "V", "UW2", "AA2", "ER", "AW0", "UW0", "R", "OW1", "EH1", "ZH", 
        "AE0", "IH2", "IH", "Y", "JH", "P", "AY1", "EY0", "OY2", "TH", "HH", "D", "ER0", "CH", "AO1", "AE1", 
        "AO2", "OY1", "AY2", "IH1", "OW0", "L", "SH"
    }

    # Transliterate to ITANS
    itrans = transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    
    # Pre-clean ITRANS to remove non-alphabetical characters except space and basic punctuation
    itrans = re.sub(r'[^a-zA-Z\s.,!?]', '', itrans)

    mapping = {
        'a': 'AH0', 'aa': 'AA1', 'i': 'IY0', 'ii': 'IY1', 'u': 'UH0', 'uu': 'UW1',
        'e': 'EY1', 'ai': 'AY1', 'o': 'OW1', 'au': 'AW1',
        'k': 'K', 'kh': 'K', 'g': 'G', 'gh': 'G',
        'c': 'CH', 'ch': 'CH', 'j': 'JH', 'jh': 'JH',
        'T': 'T', 'Th': 'T', 'D': 'D', 'Dh': 'D', 'N': 'N',
        't': 'T', 'th': 'T', 'd': 'D', 'dh': 'D', 'n': 'N',
        'p': 'P', 'ph': 'F', 'b': 'B', 'bh': 'B', 'm': 'M',
        'y': 'Y', 'r': 'R', 'l': 'L', 'v': 'V', 'w': 'W',
        'sh': 'SH', 'Sh': 'SH', 's': 'S', 'h': 'HH',
        'M': 'M', 'H': 'HH',
        'z': 'Z', 'f': 'F', 'q': 'K',
        '.': '.', ',': ',', '!': '!', '?': '?'
    }
    
    phones = []
    i = 0
    text_len = len(itrans)
    while i < text_len:
        found = False
        for length in [2, 1]:
            if i + length <= text_len:
                chunk = itrans[i:i+length].lower()
                if chunk in mapping:
                    ph = mapping[chunk]
                    if ph in arpa_symbols or ph in [".", ",", "!", "?", " "]:
                        phones.append(ph)
                    i += length
                    found = True
                    break
        if not found:
            if itrans[i] == ' ':
                phones.append(' ')
            i += 1
            
    return phones

def text_normalize(text):
    return text.strip()
