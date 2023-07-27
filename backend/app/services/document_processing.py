import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)
    return text

def combine_email_and_document_content(email, document_content):
    """Combine email content with document content."""
    combined_content = email['subject'] + " " + email['body'] + " " + document_content
    return combined_content
