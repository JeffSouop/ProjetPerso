from PdfDetect import extract_text_from_pdf
from ImageDetect import extract_and_display_text


################################################################   TEST FICHIER PDF   ####################################################################

def Extract(path):
    if path.lower().endswith('.pdf'):
        extracted_text = extract_text_from_pdf(path)
        print(extracted_text)

################################################################   TEST FICHIER IMG   ####################################################################

    elif path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            text = extract_and_display_text(path)
            if text:
                print(text)
    else:
        print("Format de fichier non pris en charge.")
