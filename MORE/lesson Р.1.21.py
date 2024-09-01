import random
class Enemy:  # создаем класс врага
    def __init__(self, name, health, attack):  # создаем врага
        self.health = health  # присваиваем переданное здоровье объекту
        self.attack = attack
        self.name = name

    def be_attacked(self, attack):  # быть атакованным
        self.health = self.health - attack  # уменьшение здоровья

class User(Enemy):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

enemy1 = Enemy(name="Рыцарь", health=330, attack=10)  # создаем объект класса
enemy2 = Enemy(name="Боец", health=200, attack=18)
enemy3 = Enemy(name="Убийца", health=150, attack=25)
user1 = User("My name", 200, 16)
print(user1.name)

players = [enemy1, enemy2, enemy3]
user_enemy = random.choice(players)
print(f"твой соперник: {user_enemy}")


enemy = user_enemy
enemy_2 = user1
list = [1, 3, 4, 6, 7, "loose"]

hits = 0
win = False
while True:
    if enemy.health <= 0 and enemy_2.health <= 0:  # and - если оба условия верны, or - если одно из условий верно
        print('Ничья')
        win = True
    elif enemy.health <= 0:
        print('Второй победил')
        print(enemy_2.health)  # здоровье второго врага
        win = True
    elif enemy_2.health <= 0:
        print('Первый победил')
        print(enemy.health)
        win = True
    if win is True:
        print('hits', hits)
        break
    hits += 1
    enemy.be_attacked(enemy_2.attack)  # вызываем метод "быть атакованным" и передаем ему атаку соперника
    enemy_2.be_attacked(enemy.attack)

