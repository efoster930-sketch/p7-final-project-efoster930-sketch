from adventurelib import *

Room.add_direction('right', 'left')


@when("begin")
def intro():
    say("Silence, nothing to hear. You lay motionless in your bed, like a sleeping beast. AHHHHHHHH, the alarm rings, screaming in your ear repeatedly.")
    say("You cover your ears with your pillow but it still continues. Finally, you get up and turn it off.")
    say("The massive robot (a fat one rather than that) comes out the bathroom with steam trailing it and starts brush your teeth, uses mouthwash, and flosses your tooth.")

dormitory = Room("""
You are in your cramped apartment bedroom. The blinds are shut, leaving the room in a dim gray haze. Clothes and old propaganda posters are scattered across the floor. 

On a small metal table rests a dusty trophy from your childhood, its plaque so worn you can barely read your own name.

The room smells faintly of cigarette smoke and machine oil.

This is all you have.

A single door stands on the right side of the room, leading to the hallway beyond.
                 """)

current_room = dormitory

def show_room():
    print(current_room)
    print("Options:")
    for exit in current_room.exits():
        print(f"- go {exit}")
    print("- look")
    print("- quit")


@when('look')
def look():
    show_room()



start()