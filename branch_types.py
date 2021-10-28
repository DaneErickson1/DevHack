import entity_factories

def get_item_chances(floor_number):
    return {
        0: [(entity_factories.health_potion, 35)],
        2: [(entity_factories.confusion_scroll, 10)],
        4: [(entity_factories.lightning_scroll, 25), (entity_factories.sword, 5)],
        6: [(entity_factories.fireball_scroll, 25), (entity_factories.chain_mail, 15)],
    }

def get_actor_chances(floor_number):
    return {
        0: [(entity_factories.devUnique, 10000)],
        3: [(entity_factories.devUnique, 10000)],
        5: [(entity_factories.devUnique, 10000)],
        7: [(entity_factories.devUnique, 10000)],
    }

def new_branch(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    branch,
    max_rooms,
    room_min_size,
    room_max_size,
    get_actor_chances,
    get_item_chances,
):
    return {
        "branch": branch,
        "max_rooms": max_rooms,
        "room_min_size": room_min_size,
        "room_max_size": room_max_size,
        "get_actor_chances": get_actor_chances,
        "get_item_chances": get_item_chances
    }

main_branch = new_branch(
    branch="main",
    max_rooms=1,
    room_min_size=5,
    room_max_size=10,
    get_actor_chances=get_actor_chances,
    get_item_chances=get_item_chances
)

branches = {
    "main": main_branch,
}

def get_branch(branch_name):
    return branches[branch_name]
