from unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.game_is_running = True
        self.player = player
        self.enemy = enemy

    def _check_players_hp(self) -> str:
        if self.player.hp <= 0 >= self.enemy.hp:
            self.winner = "Ничья"
            return self._end_game()
        elif self.player.hp <= 0:
            self.winner = f"{self.player.name} проиграл битву"
            return self._end_game()
        elif self.enemy.hp <= 0:
            self.winner = f"{self.player.name} выиграл битву"
            return self._end_game()

    def _stamina_regeneration(self):
        if self.player.stamina + self.STAMINA_PER_ROUND > self.player.unit_class.max_stamina:
            self.player.stamina = self.player.unit_class.max_stamina
        else:
            self.player.stamina += self.STAMINA_PER_ROUND
        if self.enemy.stamina + self.STAMINA_PER_ROUND > self.enemy.unit_class.max_stamina:
            self.enemy.stamina = self.enemy.unit_class.max_stamina
        else:
            self.enemy.stamina += self.STAMINA_PER_ROUND

    def next_turn(self):
        if self._check_players_hp():
            return self._check_players_hp()
        if self.game_is_running:
            self._stamina_regeneration()
            self.player.stamina = round(self.player.stamina, 1)
            self.player.hp = round(self.player.hp, 1)
            self.enemy.stamina = round(self.enemy.stamina, 1)
            self.enemy.hp = round(self.enemy.hp, 1)
            return self.enemy.hit(self.player)

    def _end_game(self):
        result = f"{self.winner}"
        self.game_is_running = False
        self._instances = {}
        return result

    def player_hit(self) -> str:
        player_hit = self.player.hit(self.enemy)
        enemy_hit = self.next_turn()
        return f'{player_hit} {enemy_hit}'

    def player_use_skill(self):
        player_hit = self.player.use_skill(self.enemy)
        enemy_hit = self.next_turn()
        return f'{player_hit} {enemy_hit}'
