from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    def skill_effect(self, user: BaseUnit, target: BaseUnit) -> str:
        self.user = user
        self.target = target
        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."

    def _is_stamina_enough(self, user: BaseUnit) -> bool:
        self.user = user
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect(user, target)
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    name = "СВИРЕПЫЙ ПИНОК"
    stamina = 6
    damage = 12


class HardShot(Skill):
    name = "МОЩНЫЙ УКОЛ"
    stamina = 5
    damage = 15


class Superpower(Skill):
    name = "СВОИ КУЛАЧКИ"
    stamina = 6
    damage = 13


class Imbagun(Skill):
    name = "ПУШКА-ИМБУШКА"
    stamina = 10
    damage = 22


class BookStrike(Skill):
    name = "ЗНАНИЯ ИЗ КНИГИ"
    stamina = 4
    damage = 16
