import pyttsx3 
import PyPDF2

file = input("Enter Pdf Location : ")
reading_pdf = PyPDF2.PdfReader(file)
pdf_pages = len(reading_pdf.pages)
print(pdf_pages)

for i in range(0, pdf_pages):
    pdf_speaker = pyttsx3.init()
    choose_page = reading_pdf.pages[i]
    pdf_text = choose_page.extract_text()
    pdf_speaker.say(pdf_text)
    pdf_speaker.runAndWait()
