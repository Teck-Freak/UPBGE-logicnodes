from mathutils import Vector
from uplogic.nodes import ULOutSocket
from uplogic.nodes import ULParameterNode
from uplogic.utils import is_invalid


class ULVectorXYZ(ULParameterNode):
    def __init__(self):
        ULParameterNode.__init__(self)
        self.input_x = None
        self.input_y = None
        self.input_z = None
        self.OUTV = ULOutSocket(self, self.get_out_v)

    def get_out_v(self):
        x = self.get_socket_value(self.input_x)
        y = self.get_socket_value(self.input_y)
        z = self.get_socket_value(self.input_z)
        v = Vector((0, 0, 0))
        if not is_invalid(x):
            v.x = x
        if not is_invalid(y):
            v.y = y
        if not is_invalid(y):
            v.z = z
        return v.copy()

    def evaluate(self):
        self._set_ready()
