from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self, add_enemy):
        self.enemies = []
        self.deleted_enemies = 0
        self.add_enemy = add_enemy

    def update(self, enemy_by_level, bullet_manager):
        while not self.enemies or not len(self.enemies) == enemy_by_level :
            self.enemies.append(Enemy())

        for enemy in self.enemies:
            enemy.update(self.enemies, self.set_deleted_enemies, bullet_manager)        

    def set_deleted_enemies(self, deleted_enemies):
        self.deleted_enemies += deleted_enemies
        self.add_enemy(self.deleted_enemies)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []