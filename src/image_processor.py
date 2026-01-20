import os
from PIL import Image

def process_image(image_path: str):
    """
    Loads an image from the given path.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Check extension
    valid_exts = ['.png', '.jpg', '.jpeg']
    _, ext = os.path.splitext(image_path)
    if ext.lower() not in valid_exts:
        raise ValueError(f"Unsupported image format: {ext}")
        
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        raise ValueError(f"Failed to open image: {e}")
