import pikepdf # A pdf library
from pikepdf import PdfImage
from datetime import datetime
from glob import glob
import pdf2image
import pdf2docx
from docx2pdf import convert

# Methods

def getFileName():
    name = input("Enter PDF Location : ")
    ans = name.replace("\\", "/")
    return ans

def outputFileName():
    now = datetime.now()
    current_time = now.strftime("%I_%M_%S")
    return current_time


print("-------------------------Welcome To The PDF Editor-------------------------\n")

print("Choose an Option\n")
print("1  : Count Pages")
print("2  : PDF To Docx File")
print("3  : Docx To PDF File")
print("4  : PDF To Images")
print("5  : Split PDF Pages")
print("6  : Merge PDFs")
print("7  : Extract PDF Images")
print("8  : Replace PDF Page")
print("9  : Reverse PDF")
print("10 : Rotate PDF")
print("11 : Remove Pages")
print("12 : Encrypt PDF")
print("13 : Exit...")

choice = int(input("Enter Your Choice : "))

while choice != 12:

    if choice == 1:
        old_pdf = pikepdf.open(getFileName())
        print(old_pdf.pages)

    elif choice == 2: # Convert PDF to DOCX

        old_pdf = input("Enter PDF Location : ")
        new_doc_file = "New_Document.docx"

        obj = pdf2docx.Converter(old_pdf)
        obj.convert(new_doc_file)
        obj.close()


    elif choice == 3: # Convert DOCX to PDF
        
        # Microsoft Word (must be installed) To Use This
        docFile = input("Enter DOCX File Location : ")
        convert(docFile, "new_pdf.pdf")

    
    elif choice == 4: # Convert PDF into Images
        
        old_pdf = pdf2image.convert_from_path("ABC.pdf", poppler_path=r"C:\Users\Bhave\Desktop\My Code\Python Projects\pdf to image\poppler-23.01.0\Library\bin")

        for i in range(len(old_pdf)):
            old_pdf[i].save("pdf to image//newImage_"+str(i)+".png", "PNG")

    

    elif choice == 5: # Split PDF into Single Pages
        old_pdf = pikepdf.open(getFileName())

        for n,page_count in enumerate(old_pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(page_count)
            fileName = "File"+str(n)+".pdf"
            new_pdf.save(fileName)



    elif choice == 6:
        new_pdf = pikepdf.new()
        location = ""

        for file in glob("C://Users//Bhave//Desktop//My Code//Python Projects//Python_PDF_Editor//single pdfs//*.pdf"):
            old_pdf = pikepdf.open(file)
            new_pdf.pages.extend(old_pdf.pages)
        new_pdf.save(outputFileName()+".pdf")



    elif choice == 7: # Extract PDF Images
        old_pdf = pikepdf.open(getFileName())

        page_1 = old_pdf.pages[0]
        all_images = list(page_1.images.keys())
        counter = 1
        for item in all_images:
            raw_image = page_1.images[item]
            pdf_image = PdfImage(raw_image)
            pdf_image.extract_to(fileprefix="test"+str(counter))
            counter = counter + 1



    elif choice == 8: # Replace PDF Page 
        old_pdf = pikepdf.open(getFileName())
        
        starting = int(input("Enter Page To Be Replaced : ")) - 1;
        ending = int(input("Enter Page To Which Replace : ")) - 1;

        old_pdf.pages[starting] = old_pdf.pages[ending]
        old_pdf.save(f"{outputFileName()}.pdf")


    elif choice == 9: # Reverse PDF
        old_pdf = pikepdf.open(getFileName())
        
        old_pdf.pages.reverse()
        old_pdf.save(f"{outputFileName()}.pdf")


    elif choice == 10: # Rotate The PDF
        old_pdf = pikepdf.open(getFileName())
                
        degree = int(input("Enter Degree of Rotation : "))

        for i in old_pdf.pages:
            i.Rotate = degree
            old_pdf.save(outputFileName()+".pdf")


    elif choice == 11: # Remove Pages
        old_pdf = pikepdf.open(getFileName())
        
        starting = int(input("Enter Starting Page To Be Deleted : ")) - 1;
        ending = int(input("Enter Ending Page To Be Deleted : "));

        del old_pdf.pages[starting:ending]
        old_pdf.save(f"{outputFileName()}.pdf")


    elif choice == 12: # Encrypt PDF With Password
        old_pdf = pikepdf.open(getFileName())

        password = input("Enter Password : ")
        no_extraction = pikepdf.Permissions(extract=False)
        old_pdf.save(f"{outputFileName()}.pdf", encryption = pikepdf.Encryption(user= password, owner="Bhave", allow=no_extraction))


    elif choice == 13:
        print("Thank You For Using...")
        print("Exited Successfully")
        exit(0)
    
    choice = int(input("Enter Your Choice : "))