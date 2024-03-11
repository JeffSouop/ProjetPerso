import pytesseract
import cv2

def extract_and_display_text(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            print("Erreur: Impossible de lire l'image.")
            return None

        text = pytesseract.image_to_string(img)

        if text.strip() == '':
            print("Aucun texte n'a été extrait de l'image.")
            return None

        return text
    
    except Exception as e:
        print(f"Nous avons une erreur : {e}")