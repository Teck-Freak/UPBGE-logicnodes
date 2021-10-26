from bge.types import KX_GameObject as GameObject
from uplogic.nodes import ULOutSocket
from uplogic.nodes import ULParameterNode
from uplogic.utils import STATUS_WAITING
from uplogic.utils import is_invalid
from uplogic.utils import is_waiting


class ULChildByIndex(ULParameterNode):
    def __init__(self):
        ULParameterNode.__init__(self)
        self.from_parent: GameObject = None
        self.index: int = None
        self.CHILD = ULOutSocket(self, self.get_child)

    def get_child(self):
        parent: GameObject = self.get_socket_value(self.from_parent)
        index: int = self.get_socket_value(self.index)
        if is_waiting(parent, index):
            return STATUS_WAITING
        elif not is_invalid(parent):
            if len(parent.children) > index:
                return parent.children[index]
        return STATUS_WAITING

    def evaluate(self):
        self._set_ready()
