import fitz
path_file = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/04-workin-with-PDF/ExtractingText/003 students.pdf'
# with fitz.open(path_file) as pdf:
#     text = ''
#     for page in pdf:# this way we can access each page of our pdf file
#         text = text + page.get_text()

# if you want to extract a table from pdf file ypu have to do this:
        # the Library which we wana use is:

import tabula

table = tabula.read_pdf('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/04-workin-with-PDF/ExtractingText/004 weather.pdf',pages=1)
print(table)


