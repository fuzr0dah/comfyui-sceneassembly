from .constants import get_category

class ImageInvertor:
    CATEGORY = get_category()
   
    @classmethod
    def INPUT_TYPES(s):
        return { 
            "required":  { "image": ("IMAGE", {}) } 
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "invert"

    def invert(self, image):
        result = 1 - image
        return (result,)

NODE_CLASS_MAPPINGS = {
    "Image Invertor" : ImageInvertor,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Image Invertor": "Image Invertor",
}
