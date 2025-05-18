from .constants import get_category

class CompositionNode:
    NAME = "Composition 🎥"
    CATEGORY = get_category()
   
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "girl": (["none", "1girl, 2girls, 3girls, multiple girls"], ),
                "boy": (["none", "1boy, 2boys, 3boys, multiple boys"], ),
            },
            "optional": {
                "custom_prompt":  ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "make_composition"

    def make_composition(self, girl, boy):
        return (f"{girl}, {boy}",)