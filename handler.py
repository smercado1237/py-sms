def response_handler(body):
    if body == 'start':
        message = "You wake up in a dim, empty room. After your eyes adjust, do you 'stand up' or 'go back to sleep'?"
    elif body == 'stand up':
        message = "You stand up and begin to take in your surroundings. Are you going to 'search' for a way out or 'wait' for someone to find you?"
    elif body == 'search':
        message = "You begin to feel around the walls and floors for secret openings. After pressing on a corner of the wall, you discover that it is a secret door! Do you 'open it' and leave the room or try to 'find' another way out?"
    elif body == 'wait':
        message = "While you are waiting, you fall asleep. Suddenly, you are woken up by a loud noise coming from behind you. Do you 'play dead' or 'defend' yourself?"
    elif body == 'play dead':
        message = "Not courageous, but ultimately a good choice! The loud banging stops, and when you decide to get up, you are alone again. Are you going to keep being 'lazy' or 'find' a way out?"
    elif body == 'defend':
        message = "Courageous, but not a good idea! When you confront the banging, you find a small creature in the corner. It swiftly comes towards you and pricks you with a needle. When you become conscious again, you are on a lab table. Do you 'escape' from the lab or 'investigate' it?"
    elif body == 'go back to sleep':
        message = "You fall back asleep and when you awaken again you find yourself on a lab table. Do you 'escape' from the lab or 'investigate' it?"
    elif body == 'open it':
        message = "You walk through the opening and are suddenly surrounded by a purple fog. While investigating this strange world, you realize you're very hungry. Do you go 'left' or 'right' to find food?"
    elif body == 'find':
        message = "As you continue your search, a large, hazy opening appears in the center of the floor! Are you going to pull a 'yolo' or play it 'safe'?"
    elif body == 'escape':
        message = "You're brave. You jump off the lab table and run to the glass door of the room. It's locked! Are you going to 'pick the lock' or 'break the glass'?"
    elif body == 'investigate':
        message = "As you investigate, you find a file filled with unclear photos of unknown creatures. Suddenly, you hear running footsteps coming towards the lab! Do you "
    elif body == 'left':
        message ="NOT DONE"
    elif body == 'right':
        message ="NOT DONE"
    elif body == 'safe':
        message ="NOT DONE"
    elif body == 'yolo':
        message ="NOT DONE"
    elif body == 'lazy'
        message = "NOT DONE"
    elif body == 'pick the lock'
        message = "NOT DONE"
    elif body == 'break the glass'
        message = "NOT DONE"
    else:
        message = "nothing"
    return message