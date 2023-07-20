from game.components.power_ups.power_up import PowerUp
from game.utils.constants import MACHINE_GUN_TYPE, MACHINE_GUN, SPACESHIP_MACHINE_GUN

class MachineGun(PowerUp):
    def __init__(self):
        super().__init__(MACHINE_GUN, MACHINE_GUN_TYPE, SPACESHIP_MACHINE_GUN)