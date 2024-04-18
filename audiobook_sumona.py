import pyttsx3
import PyPDF2

book=open('object_oriented_python_tutorial.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
speaker.say('hello admin pannel,i am sumona banerjee presenting you audiobook about python book which can read a pdf file')
page=pdfReader.getPage(7)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()