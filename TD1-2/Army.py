class Army:
    def __init__(self, chef, moralBase):
        self.chef = chef
        self.moralBase = moralBase

    def _get_chef(self):
        return self.chef

    def _get_moral(self):
        return self.moralBase

    def _set_chef(self, chef):
        self.chef = chef

    def _set_moral(self, moralBase):
        self.moralBase = moralBase


    def __str__(self):
        return '{}'.format(self.chef, self.moralBase)

    def get_total_morale(self):
        return float(self.chef.boostMoral) * float(self.moralBase)