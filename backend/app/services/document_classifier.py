def classify_document(text):
    """
    Classify the document based on its content.
    
    :param text: Extracted text from the document.
    :return: Classification label as a string.
    """
    if "Policy" in text:
        return "Policy Document"
    elif "Invoice" in text:
        return "Invoice"
    # ... add more rules as needed
    else:
        return "Uncategorized"
