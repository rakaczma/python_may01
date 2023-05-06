class Enemy:

    def __init__(self, name='Enemy', health=0, hit_power=0):
        self.name = name
        self.health = health
        self.hit_power = hit_power

    def take_damage(self, damage):
        remaining_health = self.health - damage
        if remaining_health > 0:
            self.health = remaining_health
        else:
            self.health = 0
            print("Enemy is dead.")

    def __str__(self):
        return f"Name {self.name}. Health: {self.health}. Hit power: {self.hit_power}"


class Troll(Enemy):

        def take_damage_troll(self, damage):
            super().take_damage(damage)
            if self.health == 0:
                self.health = 100


troll = Troll("Troll", 100, 100)
troll.take_damage(50)
print(troll)
troll.take_damage(51)
print(troll)
#
# troll_with_name = Troll("Troll")
# troll_with_health = Troll("Troll", 100)
# troll_with_power = Troll("Troll", 100, 100)
#
# print(troll)
# print(troll_with_name)
# print(troll_with_health)
# print(troll_with_power)