from adventurelib import *

Room.add_direction('right', 'left')

@when("begin")
def intro():
    say("Silence, nothing to hear. You lay motionless in your bed, like a sleeping beast. AHHHHHHHH, the alarm rings, screaming in your ear repeatedly.")
    say("You cover your ears with your pillow but it still continues. Finally, you get up and turn it off.")
    say("The massive robot (a fat one rather than that) comes out the bathroom and starts brush your teeth, uses mouthwash, and flosses your tooth.")


@when('look')
def look():
    print("You are in a dark, messy bedroom. Your posters lay around the room and your trophy that you won when you was younger lays on the table.")

dark_room = Room("""
You are in a dark, messy bedroom. Your posters lay around the room and your trophy that you won when you was younger lays on the table.
There's a door to the right side of your room.
                 """)

current_room = dark_room

start()