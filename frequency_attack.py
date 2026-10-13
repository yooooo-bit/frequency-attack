ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getLetterCount(message):
    # Returns a dictionary with keys of single letters
    # and values of how many times they appear in the message.

    letterCount = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
        'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
        'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
        'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
        'Y': 0, 'Z': 0
    }

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def getItemAtIndexZero(items):
    return items[0]


def getFrequencyOrder(message):
    # Returns a string of alphabet letters arranged
    # from most frequently occurring to least frequently occurring.

    # First, get the frequency of each letter.
    letterToFreq = getLetterCount(message)

    # Second, make a dictionary of frequency counts
    # and the letters having that frequency.
    freqToLetter = {}

    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # Third, sort letters with the same frequency
    # according to ETAOIN order.
    for freq in freqToLetter:
        freqToLetter[freq].sort(
            key=ETAOIN.find,
            reverse=True
        )
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # Fourth, sort the frequencies from highest to lowest.
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(
        key=getItemAtIndexZero,
        reverse=True
    )

    # Fifth, create the final frequency order.
    freqOrder = []

    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def englishFreqMatchScore(message):
    # Returns the number of matches between the message's
    # frequency order and normal English frequency order.

    freqOrder = getFrequencyOrder(message)

    matchScore = 0

    # Check the six most common letters.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1

    # Check the six least common letters.
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore


def decryptMessage(message, key):
    # Decrypts the message using the substitution key.

    plaintext = ''

    for symbol in message:
        if symbol.upper() in LETTERS:
            # Find the encrypted letter in the key.
            index = key.find(symbol.upper())

            if index != -1:
                decryptedLetter = LETTERS[index]

                if symbol.isupper():
                    plaintext += decryptedLetter
                else:
                    plaintext += decryptedLetter.lower()
            else:
                plaintext += symbol
        else:
            plaintext += symbol

    return plaintext


# ---------------------------------------------------------
# CIPHERTEXT
# ---------------------------------------------------------

ciphertext = """ZOZM NZGSRHLM GFIRMT DZH Z YIRGRHS NZGSVNZGRXRZM, OLTRXRZM, XIBKGZMZOBHG, ZMW XLNKFGVI HXRVMGRHG. SV DZH SRTSOB RMUOFVMGRZO RM GSV WVEVOLKNVMG LU XLNKFGVI HXRVMXV, KILERWRMT Z ULINZORHZGRLM LU GSV XLMXVKGH LU "ZOTLIRGSN" ZMW "XLNKFGZGRLM" DRGS GSV GFIRMT NZXSRMV. GFIRMT RH DRWVOB XLMHRWVIVW GL YV GSV UZGSVI LU XLNKFGVI HXRVMXV ZMW ZIGRURXRZO RMGVOORTVMXV. WFIRMT DLIOW DZI RR, GFIRMT DLIPVW ULI GSV TLEVIMNVMG XLWV ZMW XBKSVI HXSLLO (TXXH) ZG YOVGXSOVB KZIP, YIRGZRM'H XLWVYIVZPRMT XVMGIV. ULI Z GRNV SV DZH SVZW LU SFG 8, GSV HVXGRLM IVHKLMHRYOV ULI TVINZM MZEZO XIBKGZMZOBHRH. SV WVERHVW Z MFNYVI LU GVXSMRJFVH ULI YIVZPRMT TVINZM XRKSVIH, RMXOFWRMT GSV NVGSLW LU GSV YLNYV, ZM VOVXGILNVXSZMRXZO NZXSRMV GSZG XLFOW URMW HVGGRMTH ULI GSV VMRTNZ NZXSRMV. ZUGVI GSV DZI SV DLIPVW ZG GSV MZGRLMZO KSBHRXZO OZYLIZGLIB, DSVIV SV XIVZGVW LMV LU GSV URIHG WVHRTMH ULI Z HGLIVW-KILTIZN XLNKFGVI, GSV ZXV. RM 1948 GFIRMT QLRMVW NZC MVDNZM'H XLNKFGRMT OZYLIZGLIB ZG NZMXSVHGVI FMREVIHRGB, DSVIV SV ZHHRHGVW RM GSV WVEVOLKNVMG LU GSV NZMXSVHGVI XLNKFGVIH ZMW YVXZNV RMGVIVHGVW RM NZGSVNZGRXZO YRLOLTB. SV DILGV Z KZKVI LM GSV XSVNRXZO YZHRH LU NLIKSLTVMVHRH, ZMW KIVWRXGVW LHXROOZGRMT XSVNRXZO IVZXGRLMH HFXS ZH GSV YVOLFHLE-ASZYLGRMHPB IVZXGRLM, DSRXS DVIV URIHG LYHVIEVW RM GSV 1960H. GFIRMT'H SLNLHVCFZORGB IVHFOGVW RM Z XIRNRMZO KILHVXFGRLM RM 1952, DSVM SLNLHVCFZO ZXGH DVIV HGROO ROOVTZO RM GSV FMRGVW PRMTWLN. SV ZXXVKGVW GIVZGNVMG DRGS UVNZOV SLINLMVH (XSVNRXZO XZHGIZGRLM) ZH ZM ZOGVIMZGREV GL KIRHLM. GFIRMT WRVW RM 1954, QFHG LEVI GDL DVVPH YVULIV SRH 42MW YRIGSWZB, UILN XBZMRWV KLRHLMRMT. ZM RMJFVHG WVGVINRMVW GSZG SRH WVZGS DZH HFRXRWV; SRH NLGSVI ZMW HLNV LGSVIH YVORVEVW SRH WVZGS DZH ZXXRWVMGZO. LM 10 HVKGVNYVI 2009, ULOOLDRMT ZM RMGVIMVG XZNKZRTM, YIRGRHS KIRNV NRMRHGVI TLIWLM YILDM NZWV ZM LUURXRZO KFYORX ZKLOLTB LM YVSZOU LU GSV YIRGRHS TLEVIMNVMG ULI "GSV ZKKZOORMT DZB SV DZH GIVZGVW." ZH LU NZB 2012 Z KIREZGV NVNYVI'H YROO DZH YVULIV GSV SLFHV LU OLIWH DSRXS DLFOW TIZMG GFIRMT Z HGZGFGLIB KZIWLM RU VMZXGVW."""


# ---------------------------------------------------------
# FREQUENCY ANALYSIS
# ---------------------------------------------------------

print("===== LETTER FREQUENCY =====")

letterCount = getLetterCount(ciphertext)

for letter in LETTERS:
    print(letter, ":", letterCount[letter])


print("\n===== FREQUENCY ORDER =====")

frequencyOrder = getFrequencyOrder(ciphertext)

print(frequencyOrder)


print("\n===== ENGLISH FREQUENCY MATCH SCORE =====")

score = englishFreqMatchScore(ciphertext)

print(score)


# ---------------------------------------------------------
# SUBSTITUTION KEY
# ---------------------------------------------------------
#
# Frequency analysis is used to study the ciphertext.
# After comparing the frequency pattern with English,
# the substitution mapping for this particular ciphertext
# is:
#
# Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Plain : ZYXWVUTSRQPONMLKJIHGFEDCBA
#
# This is the Atbash substitution pattern.
# ---------------------------------------------------------

key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'


# ---------------------------------------------------------
# DECRYPT
# ---------------------------------------------------------

plaintext = decryptMessage(ciphertext, key)


print("\n===== DECRYPTED MESSAGE =====\n")

print(plaintext)