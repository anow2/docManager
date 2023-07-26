import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_content):
    """
    Extract text from a PDF content.
    
    :param pdf_content: Bytes content of the PDF.
    :return: Extracted text as a string.
    """
    pdf_file = BytesIO(pdf_content)
    reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page_num in range(reader.numPages):
        text += reader.getPage(page_num).extractText()
    return text
