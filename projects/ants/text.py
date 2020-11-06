
"""
from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)

# test proper call to death callback
original_death_callback = Insect.death_callback
Insect.death_callback = lambda x: print("insect died")
place = gamestate.places["tunnel_0_0"]
bee = Bee(3)
ant = FireAnt()
place.add_insect(bee)
place.add_insect(ant)
bee.action(gamestate)
bee.action(gamestate)
bee.action(gamestate) # if you



from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)

#  Testing fire does damage to all Bees in its Place
place = gamestate.places['tunnel_0_4']
fire = FireAnt(armor=1)
place.add_insect(fire)        # Add a FireAnt with 1 armor
place.add_insect(Bee(3))      # Add a Bee with 3 armor
place.add_insect(Bee(5))      # Add a Bee with 5 armor
len(place.bees)
place.bees[0].action(gamestate)
"""




"""

from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))

# Testing bodyguard performs thrower's action
bodyguard = BodyguardAnt()
thrower = ThrowerAnt()
bee = Bee(2)
# Place bodyguard before thrower
gamestate.places["tunnel_0_0"].add_insect(bodyguard)
gamestate.places["tunnel_0_0"].add_insect(thrower)



from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
#
# Testing bodyguard performs thrower's action
bodyguard = BodyguardAnt()
thrower = ThrowerAnt()
bee = Bee(2)
# Place thrower before bodyguard


gamestate.places["tunnel_0_0"].add_insect(thrower)
gamestate.places["tunnel_0_0"].add_insect(bodyguard)
gamestate.places["tunnel_0_3"].add_insect(bee)
bodyguard.action(gamestate)

#print(gamestate.places["tunnel_0_0"].ant)
#print(gamestate.places["tunnel_0_0"].ant.contained_ant)


from ants import *
from ants_plans import *
beehive, layout = Hive(make_test_assault_plan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
#
# Testing TankAnt action
tank = TankAnt()
place = gamestate.places['tunnel_0_1']
place.add_insect(tank)
for _ in range(3):
    place.add_insect(Bee(1))

print(place.bees)
tank.action(gamestate)
print(len(place.bees))




import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
ants.bees_win = lambda: None
# QueenAnt Placement
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
tunnel = [gamestate.places['tunnel_0_{0}'.format(i)] for i in range(9)]
tunnel[1].add_insect(back_ant)
tunnel[7].add_insect(front_ant)
tunnel[4].add_insect(impostor)
impostor.action(gamestate)
print(impostor.armor)            # Impostors must die!
print(tunnel[4].ant is None)
print(back_ant.damage)           # Ants should not be buffed
print(front_ant.damage)

tunnel[4].add_insect(queen)
queen.action(gamestate)
print(queen.armor)             # Long live the Queen!

print(back_ant.damage)




import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
ants.bees_win = lambda: None
# QueenAnt Removal
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
place = gamestate.places['tunnel_0_2']
place.add_insect(impostor)
place.remove_insect(impostor)
print(place.ant is None)        # Impostors can be removed
place.add_insect(queen)
place.remove_insect(queen)
print(place.ant is queen)




import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
ants.bees_win = lambda: None

# Testing damage multiplier
queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)] for j in range(9)] for i in range(2)]
# layout
# queen_tunnel: [Back, Guard/Guarded, Queen, Front, Bee     ]
# side_tunnel : [Side,              ,      ,      , Side Bee]
queen = ants.QueenAnt()
back = ants.ThrowerAnt()
front = ants.ThrowerAnt()
guard = ants.BodyguardAnt()
guarded = ants.ThrowerAnt()
side = ants.ThrowerAnt()
bee = ants.Bee(10)
side_bee = ants.Bee(10)
queen_tunnel[0].add_insect(back)
queen_tunnel[1].add_insect(guard)
queen_tunnel[1].add_insect(guarded)
queen_tunnel[2].add_insect(queen)
queen_tunnel[3].add_insect(front)
side_tunnel[0].add_insect(side)
queen_tunnel[4].add_insect(bee)
side_tunnel[4].add_insect(side_bee)
queen.action(gamestate)
print(bee.armor)
back.action(gamestate)
print(bee.armor)
front.action(gamestate)
print(bee.armor)
guard.action(gamestate)
print(bee.armor)


"""



from ants import *
from ants_plans import *
beehive, layout = Hive(make_test_assault_plan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
#
# Testing TankAnt action
tank = TankAnt()
place = gamestate.places['tunnel_0_1']
place.add_insect(tank)
for _ in range(3):
    place.add_insect(Bee(1))
tank.action(gamestate)
print(len(place.bees))
#3

# Error: expected
#     0
# but got
#     3



# Error: expected
#     True
# but got
#     False





