from .constants import get_category
from .utils.configs import Config, get_config_list, get_config_obj

class SceneNode:
    NAME = "Scene 🎬"
    CATEGORY = get_category()
   
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "base_scene": ("SCENE", {"forceInput": True}),
                "quality": ("STRING", {"forceInput": True, "default": ""})
            }
        }
    
    RETURN_TYPES = ("SCENE", "STRING", )
    RETURN_NAMES = ("scene", "quality", )
    FUNCTION = "replace"

    def replace(self, base_scene=None, **kwargs):
        if base_scene == None and not kwargs.items():
            return new_scene()
        result_scene = replace_in_scene(base_scene, **kwargs)
        return result_scene

LIST_SCENE_KEYS = ['quality']

def empty_scene():
    return {value: "" for value in LIST_SCENE_KEYS}

def new_scene():
    return (empty_scene(), "", )
    
def replace_in_scene(base_scene, **kwargs):
    if not kwargs.items():
        return (base_scene, base_scene['quality'], )
    scene = base_scene if base_scene is not None else empty_scene()
    for key, value in scene.items():
        scene[key] = kwargs[key] if kwargs[key] is not None else value
    return (scene, kwargs['quality'], )