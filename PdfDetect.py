from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_file_path):
    try:
        images = convert_from_path(pdf_file_path)

        extracted_text = ""

        for i, img in enumerate(images):
            page_text = pytesseract.image_to_string(img)

            extracted_text += f"Page {i + 1}:\n{page_text}\n"

        return extracted_text

    except Exception as e:
        return f"Error occurred: {str(e)}"