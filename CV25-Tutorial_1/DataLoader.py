from pathlib import Path
import numpy as np
from PIL import Image
 
class Dataloader:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
    
    def load_image(self, gray=False):
        """Load all images from the folder as a list of numpy arrays"""
        images = []
        for file in self.folder_path.iterdir():
            if file.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                img = Image.open(file)
                
                if gray:
                    img = img.convert("L")  # Convert to grayscale
                
                images.append(np.array(img))
        
        return images
