# import pytesseract
# import cv2
# import math
# from PIL import Image
# def extract_and_display_text(image_path):
#     try:
#         img = cv2.imread(image_path)

#         if img is None:
#             print("Erreur: Impossible de lire l'image.")
#             return None

#         text = pytesseract.image_to_string(img)

#         if text.strip() == '':
#             print("Aucun texte n'a été extrait de l'image.")
#             return None

#         return text
    
#     except Exception as e:
#         print(f"Nous avons une erreur : {e}")

from numba import cuda
import numpy as np
import cv2
import math
from PIL import Image
import pytesseract

@cuda.jit
def cuda_image_to_string(img, result):
    """
    CUDA kernel to perform image processing.
    This function runs in parallel on the GPU.
    """
    i, j = cuda.grid(2)
    if i < img.shape[0] and j < img.shape[1]:
        result[i, j] = img[i, j]

def extract_and_display_text(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            print("Erreur: Impossible de lire l'image.")
            return None
        
        result = np.zeros_like(img)
        threadsperblock = (16, 16)
        blockspergrid_x = math.ceil(img.shape[0] / threadsperblock[0])
        blockspergrid_y = math.ceil(img.shape[1] / threadsperblock[1])
        blockspergrid = (blockspergrid_x, blockspergrid_y)
        cuda_image_to_string[blockspergrid, threadsperblock](img, result)
        cuda.synchronize()
        result_pil = Image.fromarray(result)

        text = pytesseract.image_to_string(result_pil)

        if text.strip() == '':
            print("Aucun texte n'a été extrait de l'image.")
            return None

        return text
    
    except Exception as e:
        print(f"Nous avons une erreur : {e}")
