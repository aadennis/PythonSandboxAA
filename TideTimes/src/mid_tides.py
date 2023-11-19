

def format_tide_dictation(input_text):
    """
        input_text is the tide table as dictated. 
        Context: In any one calendar day, there are only 2 usable high/low waters 
        (HLWs), give or take, which are the middle 2 of 4. If there are 3 HLWs, then 
        dictate the first 2 of 3. This happens when the first tide of the calendar 
        day swaps from being a high to a low or vice-versa.
        The use of Lima and Hotel is because SpeechToText (STT) engines routinely
        fail to hear Low and High. Ditto Bravo for "new line". For this, the code
        ignores it, and uses the token separator of space to replace with newline.
        An example of input, taken from (flawed) output from dictation, is below 
        in test_text_1.
    """    
    translation_dict = {'lima': 'low', 'hotel': 'high'}

    words = input_text.lower().split()
    translated_words = []

    for i, word in enumerate(words):
        if word == 'bravo': # ignore - just visual punctuation for the dictator
            continue
        if word in translation_dict:
            translated_words.append(translation_dict[word])
        else:
            translated_words.append(word)

    translated_text = ' '.join(translated_words).replace(' ','\n')
    return translated_text

test_text_1 = """
 Lima 082838145008 bravo 085936152210 bravo 093534155672
 bravo 2B101731163813B110930173014B 121229183114 bravo hotel 070115132329 
 bravo 081214143430 bravo 091512153532 bravo 101110163134 bravo 110108172235 
 bravo hotel 110236170809 bravo"""
output_text = format_tide_dictation(test_text_1)
print(output_text)
