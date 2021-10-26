from mathutils import Euler
from uplogic.nodes import ULOutSocket
from uplogic.nodes import ULParameterNode


class ULEuler(ULParameterNode):
    def __init__(self):
        ULParameterNode.__init__(self)
        self.input_x = None
        self.input_y = None
        self.input_z = None
        self.OUTV = ULOutSocket(self, self.get_out_v)

    def get_out_v(self):
        e = Euler()
        x = self.get_socket_value(self.input_x)
        y = self.get_socket_value(self.input_y)
        z = self.get_socket_value(self.input_z)
        if x is not None:
            e.x = x
        if y is not None:
            e.y = y
        if z is not None:
            e.z = z
        return e

    def evaluate(self):
        self._set_ready()
