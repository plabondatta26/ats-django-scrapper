import PyPDF2

# creating a pdf file object
pdfFileObj = open('1642602487.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
# print(pageObj.extractText())

data = pageObj.extractText().split(':')
data_dict = {}
print(data)
for i in data:
    i = i.strip()
    k=''
    v=''
    if i == 'Seller Name':
        k='seller_name'
    elif i == 'Seller Email Address':
        k= 'seller_email_address'
    elif i == '':
        pass
# closing the pdf file object
pdfFileObj.close()