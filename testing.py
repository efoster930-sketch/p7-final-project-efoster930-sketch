from adventurelib import Room, Item, when, say, start, set_context

class Bag(set):
    def find(self, name):
        name = name.lower()
        for item in self:
            if name == item.name.lower() or name in (alias.lower() for alias in item.aliases):
                return item
        return None

    def __contains__(self, value):
        if isinstance(value, str):
            return self.find(value) is not None
        return super().__contains__(value)

    def take(self, name):
        item = self.find(name)
        if item is not None:
            self.remove(item)
        return item

Room.items = Bag()

current_room = starting_room = Room("""
You are in a dark room.
""")

valley = starting_room.north = Room("""
You are in a beautiful valley.
""")

magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.
""")

mallet = Item('rusty mallet', 'mallet')
valley.items = Bag({mallet,})

inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
        if room == magic_forest:
            set_context('magic_aura')
        else:
            set_context('default')


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

@when('cast', context='magic_aura', magic=None)
@when('cast MAGIC', context='magic_aura')
def cast(magic):
    if magic == None:
        say("Which magic you would like to spell?")
    elif magic == 'fireball':
        say("A flaming Fireball shoots form your hands!")

look()
start()
