from .constants import get_category
from .utils.configs import Config, get_config_list, get_config_obj

class QualityNode:
    NAME = "Quality 🖼️"
    CATEGORY = get_category()
   
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "config": (get_config_list(Config.QUALITY), ),
                "nsfw": ("BOOLEAN", {"default": False})
            },
            "optional": {
                "custom_prompt":  ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "make_quality"

    def make_quality(self, config, nsfw,  custom_prompt):
        config_obj = get_config_obj(Config.QUALITY, config)
        result = config_obj['prompt']
        if nsfw == True:
            result += f", {config_obj['nsfw']}"
        result += f", {custom_prompt}"
        return (result,)
