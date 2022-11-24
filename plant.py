class Plant:
    def __init__(self):
        self.leaf_mass = 0
        self.stem_mass = 0
        self.root_mass = 0
        self.starch_pool = 0

    def get_plant(self):
        return {'leaf_mass': self.leaf_mass,
                'stem_mass': self.stem_mass,
                'root_mass': self.root_mass,
                'starch_pool': self.starch_pool
                }

    def grow(self, rates, dt):
        print("Growing Plants:" , rates, "for ", dt, " Seconds")
        self.leaf_mass += rates[0] * dt
        self.stem_mass += rates[1] * dt
        self.root_mass += rates[2] * dt
        self.starch_pool += (rates[3]-rates[4]) * dt

    def get_total_plant_mass(self):
        return self.leaf_mass + self.stem_mass + self.root_mass
