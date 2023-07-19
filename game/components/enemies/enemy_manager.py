from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.deleted_enemies = 0

    def update(self, enemy_by_level, bullet_manager):
        while not self.enemies or not len(self.enemies) == enemy_by_level :
            self.enemies.append(Enemy())

        for enemy in self.enemies:
            enemy.update(self.enemies, bullet_manager)        

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []