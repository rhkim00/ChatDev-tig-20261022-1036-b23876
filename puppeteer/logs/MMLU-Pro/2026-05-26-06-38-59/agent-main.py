sentence = 'Turtles live long lives • are happy creatures ⊃ they are injured'
print('Original sentence:', sentence)

symbolized_sentence = sentence.replace('•', '∧').replace('⊃', '→')
print('Symbolized sentence:', symbolized_sentence)