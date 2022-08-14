from dataclasses import dataclass
from typing import Dict

from skills import Skill, FuryPunch, HardShot, Superpower, BookStrike, Imbagun


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass: UnitClass = UnitClass(
    name="Воин",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

ThiefClass: UnitClass = UnitClass(
    name="Вор",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

WarlockClass: UnitClass = UnitClass(
    name="Колдун",
    max_health=45.0,
    max_stamina=35.0,
    attack=1.2,
    stamina=1.0,
    armor=0.9,
    skill=BookStrike()
)

SuperheroClass: UnitClass = UnitClass(
    name="Супергерой",
    max_health=55.0,
    max_stamina=30.0,
    attack=0.7,
    stamina=0.8,
    armor=1.3,
    skill=Superpower()
)

CheaterClass: UnitClass = UnitClass(
    name="Читер",
    max_health=50.0,
    max_stamina=30.0,
    attack=1.4,
    stamina=1.3,
    armor=1.1,
    skill=Imbagun()
)

unit_classes: Dict[str, UnitClass] = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    WarlockClass.name: WarlockClass,
    SuperheroClass.name: SuperheroClass,
    CheaterClass.name: CheaterClass
}
