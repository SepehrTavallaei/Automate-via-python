
file = open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/01-simple-writing/text.txt','w')

file.write('Helloo')

text = """

second text

third text
"""

text2 = '\nHello again'

file.write(text)
file.write(text2)