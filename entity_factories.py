from components import consumable, equippable
from components.ai import HostileEnemy, PeacefulStaticActor, PeacefulWanderingActor
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item
import random
import tcod

def generate_options(options):
    if len(options)==0:
        return {}
    else:
        options_dict = {}
        for i in range(len(options)):
            options_dict[tcod.event.KeySym(i+97)]=options[i]
    return options_dict

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
    interact=lambda *_: (False, random.choice(["You hear the strange whistle of hot air escaping"]), {})
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
    interact=lambda *_: (False, random.choice(["Uogh","Hmph","Huh?","Rhaaou"]), {})
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    interact=lambda *_: (False, random.choice(["Uogh","Hmph","Huh?","Rhaaou"]), {})
)
dev = Actor(
    char="D",
    color=(255,215,0),
    name="Developer",
    ai_cls=PeacefulWanderingActor,
    equipment=Equipment(),
    fighter=Fighter(hp=1000, base_defense=100, base_power=100),
    inventory=Inventory(capacity=1),
    level=Level(xp_given=1000),
    interact=lambda *_: (False, random.choice(["Filler1","Filler2"]), {})
)

def devUnique_interaction(self):
    def interaction(is_hostile, player_interaction_counter, key):
        hostile_resp = (False,
            "Need... Coffee...",
            {})

        resp1 = (True,
                "I can't believe those other FUCKS use emacs",
                generate_options(["politely nod"]))
        resp2 = (True,
                "WHOA! What are you?",
                generate_options(["A sentient program", "A glitch", "A \"player character\""]))
        resp3 = (True,
                "Never mind... doesn't matter. Hey, wait a second, I have an idea...",
                generate_options(["politely nod"]))
        resp4 = (True,
                "I need you to put some other devs in their place. Oh don't worry, they deserve it... They use emacs",
                generate_options(["politely nod"]))
        resp5 = (True,
                "I'll just need you to sneak onto their system through this USB cable... Just go right through there! By the way... if you can do this for me I'll see if I can get you into the internet! Sound good?",
                generate_options(["Sure thing, boss"]))

        responses=[resp1,resp2,resp3,resp4,resp5]

        if is_hostile: return hostile_resp

        if player_interaction_counter>=len(responses):
            resp = (False, "Well go on, then!",{})
            return resp

        return responses[player_interaction_counter]
    return interaction

devUnique = Actor(
    char="U",
    color=(255,215,0),
    ai_cls=PeacefulStaticActor,
    equipment=Equipment(),
    fighter=Fighter(hp=1000, base_defense=1, base_power=1),
    inventory=Inventory(capacity=1),
    level=Level(xp_given=0),
    interact=devUnique_interaction
)




confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger())

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail())
