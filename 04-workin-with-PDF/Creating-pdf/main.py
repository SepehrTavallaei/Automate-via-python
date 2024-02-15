from fpdf import FPDF
from pathlib import Path
# fpdf is a library which you need to install using this command: pip install fpdf

pdf = FPDF(orientation='p',unit='pt',format='A4') # this is an empty pdf document
#          this means the mode of your Pdf file | unit means the standard size system that you want to use in your Pdf file | the size of the Pdf document
pdf.add_page()
image_file_path = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/04-workin-with-PDF/Creating-pdf/001 tiger.jpeg'
pdf.image(image_file_path,w=80,h=50,) # you enter the path of the image that we wana use in the pdf file    \
#         put the image path | width and height of the image (we want to put a value that doesn't destroy the ratio of pur image) | x and y is for location of the image that we wana place
# this is how we save the file:


# now lets add a big heading for our Pdf
# tp add text we use this method:
# to set the font (we have to change the font before we write the text), we use this method:
pdf.set_font('Times',style='B',size=24)
pdf.cell(w=0,h=50,txt='Malayan Tiger',align='C',ln=1) # ln =1 means that we implement a breakLine for that heading
# w=0 means that text/cell will ocupy the entire width of that row

pdf.set_font(family='Times',style='B',size=14)
pdf.cell(w=0,txt='Description',h=25 ,ln=1)
pdf.set_font(family='Times',style='B',size=12)
text1 = """
The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to
Peninsular Malaysia.[2] This population inhabits the southern and central parts of the Malay 
Peninsula and has been classified as nationally critically endangered. As of April 2014, the population was estimated at 
80 to 120 mature individuals with a continuous declining trend.[3]\n
"""
# for Adding mutyLine text to the Pdf we have to use this method:
pdf.multi_cell(w=0,h=15 ,txt=text1)

pdf.set_font('Times',size=15,style='B')
pdf.cell(w=150,h=15,txt='Kingdom: ')
pdf.set_font('Times',size=15)
pdf.cell(w=0,h=15,txt='Animalia',ln=1)
pdf.set_font('Times',size=15,style='B')
pdf.cell(w=150,h=15,txt='Phyluim: ')
pdf.set_font('Times',size=15)
pdf.cell(w=0,h=15,txt='chrodata')


pdf.output('output.pdf')

 

