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
        message = "You walk through the opening and are suddenly surrounded by a purple fog. While investigating this strange world, you realize you're very hungry. Do you go 'left' or 'right to find food?'"
    elif body == 'find':
        message = "As you continue your search, a large portal appears in the center of the floor! Are you going to pull a 'yolo' or play it 'safe'?"
    elif body == 'escape':
        message = "You're brave. You run to the glass door of the room. It's locked! Are you going to 'pick the lock' or 'break the glass'?"
    elif body == 'investigate':
        message = "As you investigate, you find a file filled with photos of unknown creatures. Suddenly, you hear alarms going off! Do you take the file and hide under a 'table' or in the 'closet'?"
    elif body == 'left':
        message = "You begin to take a few steps to the left when you see a hazy figure in the distance. Are you going to 'approach' the being or 'run away' and continue your search?"
    elif body == 'right to find food':
        message = "You continue right and begin to smell something sweet! Through the fog, you see a lonely table of warm, melty cookies. Are you going to 'eat them' or are they too 'suspicious'?"
    elif body == 'eat them':
        message = "Well, who wouldn't?! You eat the scrumptious cookies and are happily full until you notice that your stomach feels a little funny. You look down at your hands and realize your skin has begun to turn pink! Your skin slowly gets eaten away and you die. Better luck next time! Send 'start' to play again."
    elif body == 'suspicious':
        message = "Wise decision. You avoided death! Suddenly, you wake up! I guess it was a dream all along... Send 'start' to play again."
    elif body == 'right': 
        message ="You quickly swerve right and hit your head on a metal sign that says 'testing'. Next time be more aware of your surroundings! Send 'start' to play again."
    elif body == 'safe':
        message ="How unfortunate. While you were making the decision, an alien creature captured you in a large net. He jumps through the portal with you in the net and you are transported to the inside of his spaceship. He opens the net and you get free! Are you going to stay and 'chat' or make a 'run' for it?"
    elif body == 'yolo':
        message = "You jump through the portal and land on a fluffy floor of pastel blue clouds. Are you going to 'take a nap' or 'continue searching'?"
    elif body == 'run':
        message = "The alien, taking this as a sign of blatant disrespect, decides to shoot you with his laser gun, which turns you to mush. Good try! Send 'start' to play again."
    elif body == 'chat':
        message = "The alien is pleased at your hospitality! You both delve into a deep conversation about the latest Beyoncé song and he begins to really like you. He decides to make you the ruler of his planet and you live in harmony with the aliens for the rest of your days. Send 'start' to play again."
    elif body == 'take a nap':
        message = "You fall asleep on the comfy clouds and are woken up by an obnoxious buzzing sound. You look at the clock next to your bed. As awesome as that dream was, you're going to be late for work! Send 'start' to play again."
    elif body == 'continue searching':
        message = "You get up and see a large building made of glass. Do you try to 'break in' or 'break the glass'?"
    elif body == 'lazy':
        message = "Well, we all have those days. Nonetheless, you quickly die off from dehydration. You tried (or did you?)... Send 'start' to play again."
    elif body == 'pick the lock':
        message = "Smart choice. You swiftly pick the lock and are able to slip out of the lab undetected. Once you're outside, do you choose to go 'left' or 'right'?"
    elif body == 'break the glass':
        message = "Uh oh. Despite your efforts to break the glass neatly, a shard creates a deep cut in your leg. You quickly bleed out and never make it back home. Better luck next time! Send 'start' to play again."
    elif body == 'approach':
        message = "You begin to approach the being and find that it is a giant meerkat. He warmly greets you by bowing his head and motions for you to get on his back. Do you 'accept' or 'decline' a piggy-back ride from the animal?"
    elif body == 'accept':
        message = "You hop on the meerkat's back and he begins to carry you through the thick fog. Slowly, the fog dissipates and you find yourself surrounded by tiny unicorns! Do you 'pet them' or 'bow down' to them?"
    elif body == 'pet them':
        message = "Not a good idea. The unicorns are evil and two decide to strike you with their horns, injecting poison into your blood stream. You die within seconds. Maybe next time! Send 'start' to play again."
    elif body == 'bow down':
        message = "The unicorns are pleasantly surprised by your subordinance. They decide to bless you with magical powers that allow you to teleport home. Good job! Send 'start' to play again."
    elif body == 'decline':
        message = "How rude. He suddenly throws a ball of fire in disgust, frying you instantly. Next time, say no thank you! Send 'start' to play again."
    elif body == 'run away':
        message = "As you are sneaking away, the creature quickly begins to come towards you. As you squint at the creature, you realize it is a large snake. Before you can get away, it engulfs your entire body in one bite. Better luck next time! Send 'start' to play again."
    elif body == 'table':
        message = "How creative! The alien creatures holding you captive run into the room and begin to sniff the air, tracing your scent. You frantically search around for a weapon and find a small gun filled with water. Do you 'fight' the creatures or 'stay quiet' until they leave?"
    elif body == 'closet':
        message = "You run into the closet and escape your capturers. As you begin to look around the closet you're in, you realize that it's a portal back to Earth! Good job, you made it home! Send 'start' to play again."
    elif body == 'fight':
        message = "Good choice. You jump up from under the table and shoot at the aliens with your watergun. They shreak and begin to turn into orange, glittery dust. You open the file you took and begin reading. To your surprise, you have been kidnapped from Earth and are an unknown planet! Are you going to 'live' on this new planet or 'go back home'?"
    elif body == 'live':
        message = "You decide to spend the rest of your days on this alien planet. You find that the aliens are actually peaceful creatures and you become their ruler and friend. Nice job. Send 'start' to play again."
    elif body == 'go back home':
        message = "As much as you try to get home, you find that there is no way out of this dimension. You spend the rest of your days in hiding and eventually die of sadness. Better luck next time! Send 'start' to play again."
    elif body == 'stay quiet':
        message = "Aw, too bad. They are able to find you and, despite your efforts, capture you again. They continue to do testing on you until you become a human vegetable. Good luck next time! Send 'start' to play again."
    else:
        message = "Error. Please submit a valid option!"
    return message


