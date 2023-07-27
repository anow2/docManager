# /backend/app/services/text_analysis_service.py

def analyze_text(text):
    # Convert text to lowercase for consistent matching
    text = text.lower()

    # Define keywords for each category
    keywords = {
        "Policy Document": ["policy", "coverage", "insured"],
        "Quote Document": ["quote", "estimate", "proposed premium"],
        "Signed Agreement": ["signed", "agreement", "contract"],
        "License": ["license", "certification"],
    }

    # Check for keywords in text
    for category, key_list in keywords.items():
        for key in key_list:
            if key in text:
                return category

    # Default category if no keywords are found
    return "Others"
