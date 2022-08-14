from typing import Any

from flask import Flask, render_template, request, redirect, url_for

from base import Arena
from classes import unit_classes, UnitClass
from equipment import Equipment
from unit import BaseUnit, EnemyUnit, PlayerUnit

app = Flask(__name__, template_folder='templates')

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

arena = Arena(player=heroes.get("player"), enemy=heroes.get("enemy"))


@app.route("/")
def menu_page():
    return render_template("index.html")


@app.route("/fight/")
def start_fight() -> Any:
    arena.start_game()
    return render_template("fight.html", heroes=heroes, result='Да начнётся бой!')


@app.route("/fight/hit")
def hit() -> Any:
    if arena.game_is_running:
        res = arena.player_hit()
        return render_template("fight.html", heroes=heroes, result=res)
    else:
        return render_template("fight.html", heroes=heroes, winner=arena._end_game())


@app.route("/fight/use-skill")
def use_skill() -> Any:
    if arena.game_is_running:
        res = arena.player_use_skill()
        return render_template("fight.html", heroes=heroes, result=res)
    else:
        return render_template("fight.html", heroes=heroes, result=arena.winner)


@app.route("/fight/pass-turn")
def pass_turn() -> Any:
    if arena.game_is_running:
        res = arena.next_turn()
        return render_template("fight.html", heroes=heroes, result=res)
    else:
        return render_template("fight.html", heroes=heroes, result=arena.winner)


@app.route("/fight/end-fight")
def end_fight() -> Any:
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero() -> Any:
    if request.method == "GET":
        header = "Выберите персонажа"
        classes = unit_classes
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        return render_template("hero_choosing.html", result={
            "header": header,
            "classes": classes,
            "weapons": weapons,
            "armors": armors
        })

    if request.method == "POST":
        equipment = Equipment()

        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor_name = request.form["armor"]
        weapon_name = request.form["weapon"]

        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        player.equip_armor(equipment.get_armor(armor_name))
        player.equip_weapon(equipment.get_weapon(weapon_name))

        heroes["player"] = player
        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy() -> Any:
    if request.method == "GET":
        header = "Выберите соперника"
        classes = unit_classes
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        return render_template("hero_choosing.html", result={
            "header": header,
            "classes": classes,
            "weapons": weapons,
            "armors": armors
        })

    if request.method == "POST":
        equipment = Equipment()

        name = request.form["name"]
        unit_class = request.form["unit_class"]
        armor_name = request.form["armor"]
        weapon_name = request.form["weapon"]

        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class))
        enemy.equip_armor(equipment.get_armor(armor_name))
        enemy.equip_weapon(equipment.get_weapon(weapon_name))

        heroes["enemy"] = enemy
        return redirect(url_for("start_fight"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
