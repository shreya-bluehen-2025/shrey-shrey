from designer import *
import random

World = {"doggy": DesignerObject,
         "message": DesignerObject,
         "score": int,
         "time": int,
}

WIN_THRESHOLD = 5

# Change 1: Swap out the rectangle for an image of your choice.
def create_the_world() -> World:
    return {
        "doggy": image("doggy.webp"),
        "message": text("purple", "Score:", 20, get_width()/2),
        "score": 0,
        "time": 0
    }

def spin_the_doggy(world: World):
        world["doggy"]["angle"] += 1

def move_the_doggy(world: World, x: int, y: int):
    world["doggy"]["x"] = x
    world["doggy"]["y"] = y

def teleport_the_doggy(world: World):
    if world["time"] % 60 == 0:
        world["doggy"]["x"] = random.randint(0, get_width())
        world["doggy"]["y"] = random.randint(0, get_height())

# Change 2: Create a timer field that increments every update; instead of teleporting at random intevals,
#have the rectangle teleport every 60 updates.
def tick_clock(world: World):
    world["time"] += 1

# Change 3: Modify the message to also show the current timer.
def track_the_score(world: World):
    score = world["score"]
    time = world["time"]
    world["message"]["text"] = "Score: " + str(score) + " " + "Time: " + str(time)

def check_doggy_clicked(world: World, x: int, y: int):
    if colliding(world["doggy"], x, y):
        world["score"] += 1

def the_score_is_high_enough(world: World):
    return world["score"] >= WIN_THRESHOLD

def flash_game_over(world: World):
    world["message"]["text"] = "Game over, you won!"
    
    
when("starting", create_the_world)
when("updating", spin_the_doggy)
when("updating", teleport_the_doggy)
when("updating", track_the_score)
when("updating", tick_clock)
when("clicking", check_doggy_clicked)
when(the_score_is_high_enough, flash_game_over, pause)

start()