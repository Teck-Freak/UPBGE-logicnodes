from bge import constraints
from uplogic.nodes import ULActionNode
from uplogic.nodes import ULOutSocket
from uplogic.utils import is_invalid
from uplogic.utils import is_waiting
from uplogic.utils import not_met


class ULSetCharacterVelocity(ULActionNode):
    def __init__(self):
        ULActionNode.__init__(self)
        self.condition = None
        self.game_object = None
        self.vel = None
        self.time = None
        self.local = False
        self.done = None
        self.OUT = ULOutSocket(self, self.get_done)

    def get_done(self):
        return self.done

    def evaluate(self):
        self.done = False
        condition = self.get_input(self.condition)
        if not_met(condition):
            return
        game_object = self.get_input(self.game_object)
        if is_waiting(game_object):
            return
        local = self.local
        physics = constraints.getCharacter(game_object)
        vel = self.get_input(self.vel)
        time = self.get_input(self.time)
        self._set_ready()
        if is_invalid(game_object):
            return
        physics.setVelocity(vel, time, local)
        self.done = True
