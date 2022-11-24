from plant import Plant
from dynamic_model import DynamicModel
from gametime import GameTime


class Game:
    def __init__(self):
        self.model = DynamicModel()
        self.plant = Plant()
        self.gametime = GameTime.instance()

    # dt in seconds
    def update(self, dt, player_actions, actions):
        self.interface_player_actions(actions)
        self.model.calc_growth_rate(list(player_actions['growth_percentages'].values()))
        rates = self.model.get_rates()
        self.plant.grow(rates, dt)

    def interface_player_actions(self, actions):
        for action in actions:
            bar = getattr(self, action)
            result = bar()
            print(result)

    def test(self):
        return "happy"
