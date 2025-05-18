from .quality import QualityNode
from .scene import SceneNode

NODE_CLASS_MAPPINGS = {
    QualityNode.NAME: QualityNode,
    SceneNode.NAME: SceneNode,
}
