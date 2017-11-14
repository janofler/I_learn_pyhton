# python3 dungeon crawler with several dungeon, classes and moving monsters

import random 
import subprocess

legend = """
sign      what it is
   # _ _ _ _ wall
   . _ _ _ _ floor  
   > _ _ _ _ stair down ( use command: down)
   < _ _ _ _ stair up ( use command: up)
   @ _ _ _ _ hero ( move with a,w,s,d)
   M _ _ _ _ Monster ( dangerous!)
   B _ _ _ _ Boss    ( very dangerous!)
   P _ _ _ _ princess (save her!)
   f _ _ _ _ food  (use e to eat)
   $ _ _ _ _ gold
   k _ _ _ _ key
   d _ _ _ _ door (you need a key to open)
   h _ _ _ _ healing (use command heal)
"""



#d1 = """
################################
#.....>.....$.f.......#.......P#
#.......M.....................B#
################################"""
d1 = """
########################################################################
#.fM....#................#...............#............#...........#....#
#h......##..............#...........M.....#....MMMM..#.............#...#
#k.......##............#...######..........#........#....##.........#..#
########...#..........#...#......#.f..##....#......#....#..#.........#.#
#..#>#.#.f.M#....h...#...#...#####...#..#...f#....#....#....#.........##
#.#...#.#....########..f#...f.....f.#..f.#....#..#....#ffffff#..f......#
#.##..##.#.............#.....M.....#......#..........#........#...M....#
#..#..#...#...M........#..........#........#.....M..#.........#........#
#..#..#....#.f.....k...#############k.......#....k.#..........#........#
####dd######......h....#............#....h...#######..........##.f.....#
#..........#...........#............#..........................#.......#
#..........##########............f..##############...###########.......#
#.....f....#........#......fM......k...................................#
#...........#.......#..................................................#
#............#####################################################.....#
#.#.........f..........f.........#.......f......#....................#.#
#..#.......#....#..........#........#...........#.........M.........#..#
#...#...........#............#.....#.......##......................#...#
#....#.......f.........#....#.........#.......#...................#....#
########################################################################
"""

#d2 = """
################################
#>....<.....$.f.......#.#......#
#.......M...............M......#
################################"""
d2 ="""
######################################################################## 
#k...............M#............M.........M...............M#............#
#................#....####.................................#...........#
#.........M.....#.....#MM#.....####################........#...........#
#..###................####......#.................#..........#.........#
#..#.#.........##................#..f..............#.....M....#........#
####dh######.###h##...............#.................#..........#.......#
#..........#..#....###............#..................#.........M#......#
#..........#..#.......####........#......-............#..........#.....#
#...k....M.#..#...........#########....#################d.........#....#
#f......$...#..h###############...........h.............f#..........#..# 
######...###................#....#.....#################d.........#....#
#....#....#................#....#.M................M..#.......M..#.....#
#....h#....#........M.#d###....#............h........#.h........#......#
#...$..#.$..#.........#d##..$.#.....................#..........#.......#
#.......#.M..#........#>#....#.....#################..........#........#
#...######....##########....#.......#.............#..........#.........#
##................M........#.....M...#..#..#####.#..........#..........#
#.#.......$........f......#..f........##..#.....#..........#...........#
#..#.....................#................................#...........<#
########################################################################
"""

#d3 = """
################################
#.....>.....$.f.......#.#.3....#
#.......M.........k....d.M..B.P#
################################"""


d3 ="""

########################################################################
#.......#.M............f.........M....f...#.#..........................#
#......#.................................#...#...............h.........#
#.....#..#########################......#.....#........................#
#....#...#.......................#.....#.......#.......................#
#...#....#.#......#......f...M..#.M...#..f....#......f.........#######.#
####..f.#..#..M....#..h....§...#.....#.$.....#...h............#......#.#
#......#..#.........########.##..f..#.......#.h..............#.....###.#
#.....#....#.........#.......#.....#.......#...$$...........#.....#....#
#...h#......#.f.......#######.....#......#.................#.....#.....#
#.f..############................#......#.................#....##......#
#........M......#..f........f...#......###################..h.#........#
#.............f..#.............#......#......................#....Mf...#
############h.....#h..#####.###h.....#......................#.M..B.B.M.#
#...........#......#..#...#.........#......................#...M.B.M..M#
#........$$$f#......###.ä.#######............h............#.....M.M.M..#
#.............#.......MMM.#..............................#........B.B..#
#...........h..#.....f....#....$$......h...M....h.......#..M...M.......#
#...............#########.#............................#.......M.......#
#....h....................#...........................#.........B.....P#
########################################################################
"""


class Monster():
    number = 0     # each monster has a unique number
    zoo = {}       # all monsters are stuffed into the zoo, with number as key and Monster instance as value
    
    def __init__(self, x=1, y=2, z=0, char=None, name=None):
        """create a new monster"""
        self.x = x
        self.y = y
        self.z = z
        if char is None:
            self.char = "M"
        else:
            self.char = char
        self.number = Monster.number
        Monster.number += 1             
        Monster.zoo[self.number] = self 
        self.hp = random.randint(10,20)
        # values expressed as chance: 1 = 100%, 0.5 = 50%, ...
        # chance to sucessfully attack a non-defending target
        self.attack = random.gauss(0.6, 0.1)     # most values will be around 0.6
        # chance to sucessfully avoid being hit by a standard attack 
        self.defense = random.gauss(0.4, 0.05)   # most values will be very close around 0.4
        # chance to hit critically ( triple damage )
        self.crit = random.gauss(0.15, 0.01)     
        self.mindamage = 1
        self.maxdamage = 6
        if name is None:
            self.name = random.choice(("stinky Goblin", "mighty orc", "sneaky spider", "mad dog"))
        else:
            self.name = name
        self.taunt = random.choice(("my grandmother fights better than you...and she is dead!",
                                    "you are so useless, you don´t even serve as a bad example",
                                    "beginner training is harder than fighting you"))
                               
    def ai(self, playerinstance):
        """returns random dx and dy values for movement"""
        return random.choice((-1,0,1)), random.choice((-1,0,1))
    
    def report(self):
        """tells everything about this monster"""
        msg = "I am a Monster, called {}\n".format(self.name)
        msg += "I have {} hitpoints\n".format(self.hp)
        msg += "I hit with a chance of {:.2f} and defend with a chance of {:.2f}\n".format(self.attack, self.defense)
        msg += "I make between {} and {} damage have a chance of {:.2f˝} making triple damage\n".format(self.mindamage, self.maxdamage, self.crit)
        return msg

class Boss(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z, "B")
        self.attack += 0.4
        self.defense += 0.3
        self.crit += 0.05
        self.mindamage += random.randint(1,3)
        self.maxdamage += random.randint(1,3)
        self.name = "Boss"
        #self.char = "B"
        self.sniffrange = 5    # track player if inside
        
    def ai(self, playerinstance):
        """returns dx and dy. The boss can sniff the hero and chases him!"""
        # use pythagoras to calculate distance to playerinstance
        distance = ((playerinstance.x - self.x)**2 + (playerinstance.y - self.y)**2)**0.5
        # player inside sniffrange?
        if distance <= self.sniffrange:
            if playerinstance.x > self.x:
                dx = 1
            elif playerinstance.x < self.x:
                dx = -1
            else:
                dx = 0
            if playerinstance.y > self.y:
                dy = 1
            elif playerinstance.y < self.y:
                dy = -1
            else:
                dy = 0
            return dx, dy
        else:
            return random.choice((-1,0,1)), random.choice((-1,0,1))
            
class Princess(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z, "P")
        self.name = "Princess"
        #self.char == "P"
        self.attack = 0
        self.defense = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.hp = 1
        
    def ai(self, playerinstance):
        """returns dx and dy values for movement. The princess does not move much around"""
        return random.choice((-1,0,0,0,0,1)), random.choice((-1,0,0,0,0,0,0,1))
    
        
class Hero(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z, "@")
        self.name = "Hero"
        #self.char == "@"
        # -------- edit those values!! --------
        self.attack = 0.8
        self.defense = 0.6
        self.crit = 0.1
        self.mindamage = 2
        self.maxdamage = 12
        self.name = "legendary hero"
        # ------- hero items and stats ------
        self.hunger = 0
        self.keys = 0
        self.food = 0
        self.gold = 0
        self.healing = 1
        
def strike(a, d):
    """a strikes against d"""
    msg = ""
    datt = random.random()
    if datt > a.attack:
        msg += "how stupid! {} does not manage to attack properly\n".format(a.name)
        return msg
    msg += "attack sucessfull\n"
    ddef = random.random()
    if ddef < d.defense:
        msg += "But {} manages to avoid the blow in an sucessfull defense manoever!\n".format(d.name)
        return msg
    ddam = random.randint(a.mindamage, a.maxdamage)
    dcrit = random.random()
    if dcrit < a.crit:
        d.hp -= ddam * 3
        msg += "triple damage! {} makes {} critical damage! {} has {} hp left\n".format(a.name, ddam*3, d.name, d.hp )
    else:
        d.hp -= ddam
        msg += "{} makes {} damage! {} has {} hp left\n".format(a.name, ddam, d.name, d.hp )
    if d.hp <= 0:
        msg += "-+-+-+-+-+-  Victory for {} -+-+-+-+-+-+- \n!!!!".format(a.name)
    return msg
    
    
    
def battle(attacker, defender):
    """strike and counterstrike"""
    msg = ""
    msg += strike(attacker, defender)
    if defender.hp > 0:
        msg += "the counterstrike:\n"
        msg += strike(defender, attacker)
    return msg
        
# ------ create hero -------------
hero = Hero(1,2,0)
                
    

# read dungeon files and create level, also create Monsters

level = []         # empty list



for z, dungeon in enumerate((d1,d2,d3)):
    d = []
    for y, line in enumerate(dungeon.splitlines()):
        row = []
        for x, char in enumerate(line):
            if char in ("MBP"):
                row.append(".")  # instead of Monster, the dungeon has a floor
                if char == "M":
                    Monster(x,y,z)  # create class instance of Monster
                elif char == "B":
                    Boss(x,y,z)
                elif char == "P":
                    Princess(x,y,z)
            else:
                row.append(char)
        d.append(row)
    level.append(d)
            

# ---- test monsters

#print(Monster.zoo)

            
# ------- main loop -----

msg = ""
turns = 0
while hero.hp > 0 and hero.hunger < 100:
    turns += 1
    # 10% chance to get more hungry
    if random.random() < 0.1:
        hero.hunger += random.randint(10,20)
        msg += "you get more hungry.\n"
    #msg = ""
    # ------ monster movement -------
    for m in Monster.zoo.values():
        if m.number == hero.number:
            continue # exclude hero
        if m.hp <= 0:
            continue
        if m.z != hero.z:
            continue # only move monsters in the same level as hero
        dx, dy = m.ai(hero)  # call AI routine for monster movement
        # check if monster is trying to run into wall or stair
        target = level[m.z][m.y+dy][m.x+dx]
        if target in "#<>d":
            dx = 0
            dy = 0
        else:
            #--- check if running into other monster:
            for m2 in Monster.zoo.values():
                if m2.hp <= 0:
                    continue
                if m2.number == hero.number or m2.number == m.number:
                    continue
                if m2.z != m.z:
                    continue
                if m2.x == m.x+dx and m2.y == m.y+dy:
                    dx = 0
                    dy = 0
                    break
            #---- check if attacking hero -----
            if m.x+dx == hero.x and m.y + dy == hero.y:
                msg += battle(m, hero)
        #---- move the monster
        m.x += dx
        m.y += dy
    # --- hero still alive after attacked by monsters ?
    if hero.hp < 1:
        msg += "a monster attacked you sucessfully. Your game is over\n"
        print(msg)
        break # break out of the main loop
    # ---------- paint the dungeon --------------
    for z, dungeon in enumerate(level):
        if z!= hero.z:
            continue
        for y, line in enumerate(dungeon):
            for x, char in enumerate(line):
                for m in Monster.zoo.values():
                    if m.hp <= 0:
                        continue
                    if m.z == z and m.y == y and m.x == x:
                        print(m.char, end="")  # print the monster instead of the dungeon tile
                        break
                else:       # else after for means the loop finished withou a break
                    print(char, end="")
            print() # new line
    print("==== turn: {} pos: {}/{}/{} keys: {} hunger: {} food: {} hp: {} heal: {} ====\n".format(turns,  hero.x, hero.y, hero.z, hero.keys, hero.hunger, hero.food, hero.hp, hero.healing ))
    print(msg) 
    msg = ""
    dx = 0
    dy = 0
    command = input("your command (or ? for help) >>>")
    # ------ command interpreter ------
    if command == "?" or command == "help":
        print(legend)
        continue
    elif command == "quit" or command == "exit":
        print("bye-bye!")
        break
    elif command == "eat":
        if hero.food <= 0:
            msg += "ERROR! you have not collected any food (f)!\n"
        else:   
            subprocess.call(("espeak","mampf mampf"))
            hero.food -= 1
            hero.hunger -= random.randint(5,15)
            msg += "mhhhmmmm, that was yummy!\n"
    elif command == 'heal':
            if hero.healing<1:
                msg+='you must find healing potions (h)\n'
            else:
                msg+='You feel better\n'
                hero.healing-=1
                hero.hp +=random.randint(10,20)
            continue
    # ---- movement commands -------
    ground = level[hero.z][hero.y][hero.x]
    if command == "down" or command == ">":
        if ground == ">":
            hero.z += 1
            msg += "you descend further down into the dungeon\n"
        else:
            msg += "ERROR! You must stand on a stair (>) to go down\n"
        continue
    elif command == "up" or command == "<":
        if ground == "<":
            hero.z -= 1
            msg += "you ascend one level up into the dungeon\n"
        else:
            msg += "ERROR! You must stand on a stair (<) to go up\n"
        continue
    elif command == "a":
        dx = -1
    elif command == "d":
        dx = 1
    elif command == "w":
        dy = -1
    elif command == "s":
        dy = 1
    # ----------- check if hero runs into wall --------------
    target = level[hero.z][hero.y+dy][hero.x+dx]
    if target == "#":
        msg += "ouch! you run into a wall\n"
        dx = 0
        dy = 0
    # ------------ check if hero runs into door ---------
    elif target == "d":
        if hero.keys < 1:
            dx = 0
            dy = 0
            msg += "You need a key (k) to open this door!\n"
        else:
            level[hero.z][hero.y+dy][hero.x+dx] = "." # replace door with floor
            hero.keys -= 1
            msg += "You use up one key to open this door\n"
    # ------------ check if hero runs into monster ------
    for m in Monster.zoo.values():
        if m.z != hero.z:
            continue
        if m.number == hero.number:
            continue
        if m.hp <= 0:
            continue
        if m.x == hero.x + dx and m.y == hero.y + dy:
            msg += battle(hero, m)
            dx = 0
            dy = 0
            break # hero can only attack one monster per turn
    if hero.hp <= 0:
        break
    # ----- move the hero -----
    hero.x += dx
    hero.y += dy 
    # --------- check if hero found any items -------
    tile = level[hero.z][hero.y][hero.x]
    if tile == "k":
        hero.keys += 1
        level[hero.z][hero.y][hero.x] = "."
        msg += "You found a key ! \n"
    elif tile == "$":
        hero.gold += 1
        level[hero.z][hero.y][hero.x] = "."
        msg += "You found gold ! \n"
    elif tile == "f":
        hero.food += 1
        level[hero.z][hero.y][hero.x] = "."
        msg += "You found food ! \n"
    elif tile =='h':
        hero.healing+=1
        level[hero.z][hero.y][hero.x] ='.'
        msg +='You found a healingpotion! \n'
        subprocess.call(('espeak','A HEALINGPOTION!!!!!!'))
# ================================ end of main loop ====================
print("your game is over")
kills = 0
alive = 0
for m in Monster.zoo.values():
    if m.number != hero.number:
        continue
    if m.hp <=0:
        kills += 1
    else:
        alive += 1
print("you killed or liberated {} monsters, but {} monsters (including princesses) still remain in the dungeons".format(kills, alive))

