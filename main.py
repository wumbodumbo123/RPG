@namespace
class SpriteKind:
    hit = SpriteKind.create()
    Inventory = SpriteKind.create()
    TutExit = SpriteKind.create()
    Slime = SpriteKind.create()
    Random = SpriteKind.create()
@namespace
class StatusBarKind:
    XP = StatusBarKind.create()
    # Slime health
    SlimeH1 = StatusBarKind.create()
    SlimeH2 = StatusBarKind.create()
    SlimeH3 = StatusBarKind.create()
    SlimeH4 = StatusBarKind.create()

# variables
health = 100
direction = 0
X = 0
Y = 0
dmg = 25
MC_xp = 0
H = 0
MaxXp = 10
XpText: TextSprite = None
level = 0
SON = 1
select: Sprite = None
MSprite: Sprite = None
SlimeHealth1: StatusBarSprite = None
SlimeHealth2: StatusBarSprite = None
SlimeHealth3: StatusBarSprite = None
SlimeHealth4: StatusBarSprite = None
A = False
SlimeFightStillGoing = False
C = False
D = False
E = False
SlimeN = 0
slime_xp = 1
SelectChoice = 0
Walk = True
SX = 0
SY = 0
SX2 = 0
SY2 = 0
EnemyNumber = -68
EnemyHitNumber = 0
AllEnemyDead = 0
slime1: Sprite = None
slime2: Sprite = None
slime3: Sprite = None
slime4: Sprite = None
MCX = 0
MCY = 0
MoveForever = True
InventoryUse = True
def MSO():
    while True:
        music.play(music.create_song(assets.song("""
                BackgroundMusic
            """)),
            music.PlaybackMode.UNTIL_DONE)

forever(MSO)

# MC XY
def XY():
    global X, Y
    X = MC.x
    Y = MC.y
game.on_update(XY)

# MC
MC = sprites.create(assets.image("""
    MC
"""), SpriteKind.player)
controller.move_sprite(MC)
scene.camera_follow_sprite(MC)

# MC health
McHealth = statusbars.create(20, 4, StatusBarKind.health)
McHealth.attach_to_sprite(MC)
McHealth.set_offset_padding(0, -12)

# enemy
slime = sprites.create(assets.image("""slime"""), SpriteKind.Slime)

# enemy die
def Death():

    # Slimes
    def Slime1():
        global MC_xp, AllEnemyDead
        MC_xp += slime_xp
        slime1.destroy()
        AllEnemyDead += 1
    def Slime2():
        global MC_xp, AllEnemyDead
        MC_xp += slime_xp
        slime2.destroy()
        AllEnemyDead += 1
    def Slime3():
        global MC_xp, AllEnemyDead
        MC_xp += slime_xp
        slime3.destroy()
        AllEnemyDead += 1
    def Slime4():
        global MC_xp, AllEnemyDead
        MC_xp += slime_xp
        slime4.destroy()
        AllEnemyDead += 1

    # slime func run
    statusbars.on_zero(StatusBarKind.SlimeH1, Slime1)
    statusbars.on_zero(StatusBarKind.SlimeH2, Slime2)
    statusbars.on_zero(StatusBarKind.SlimeH3, Slime3)
    statusbars.on_zero(StatusBarKind.SlimeH4, Slime4)
game.on_update(Death)

# enemy fight 

def SlimeFight():
    global SX, SY, SX2, SY2, EnemyNumber
    fight()
    EnemyNumber = (randint(1, 1))
    SX = 15
    SY = 12
    SX2 = 15 + 15
    SY2 = 12 + 16
    slimeCreate()
    slime.destroy()
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Slime, SlimeFight)

def slimeCreate():
    global SX, SY, SX2, SY2, SlimeHealth1, SlimeHealth2, SlimeHealth3, SlimeHealth4, slime1, slime2, slime3, slime4
    if EnemyNumber >= 1:
        # 1
        slime1 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime1, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime1.set_position(SX, SY)
        SlimeHealth1 = statusbars.create(20, 4, StatusBarKind.SlimeH1)
        SlimeHealth1.attach_to_sprite(slime1)
        SlimeHealth1.value = 100
        SY += 32

    if EnemyNumber >= 2:
        #3
        slime3 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime3, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime3.set_position(SX2, SY2)
        SlimeHealth3 = statusbars.create(20, 4, StatusBarKind.SlimeH2)
        SlimeHealth3.attach_to_sprite(slime3)
        SlimeHealth3.value = 100
        SY2 += 32 

    if EnemyNumber >= 3:
        #2
        slime2 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime2, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime2.set_position(SX, SY)
        SlimeHealth2 = statusbars.create(20, 4, StatusBarKind.SlimeH3)
        SlimeHealth2.attach_to_sprite(slime2)
        SlimeHealth2.value = 100
        SY += 32
        
    if EnemyNumber == 4:
        #4
        slime4 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime4, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime4.set_position(SX2, SY2)
        SlimeHealth4 = statusbars.create(20, 4, StatusBarKind.SlimeH4)
        SlimeHealth4.attach_to_sprite(slime4)
        SlimeHealth4.value = 100
        SY2 += 32
        
def fight():
    global MCX, MCY, MoveForever, InventoryUse
    # MC Position
    MCX = MC.x
    MCY = MC.y

    # tilemap
    tiles.set_current_tilemap(tilemap("""FightRing"""))
    
    # background
    scene.set_background_image(assets.image("""DungeonFight"""))

    # MC
    tiles.place_on_tile(MC, tiles.get_tile_location(7, 3))
    MoveForever = False
    controller.move_sprite(MC, 0, 0)
    
    # inventory
    InventoryUse = False

    # Button
    button()

# Button
def button():
    global select, A, C, Walk, MSprite, SlimeHealth4
    MSprite = sprites.create(assets.image("""ChoiceButton"""), SpriteKind.Random)
    MSprite.set_position(80, 95)
    # select
    select = sprites.create(assets.image("""Select"""), SpriteKind.Random)
    C = True
    Walk = False
    animation.run_image_animation(MC, assets.animation("""AttackStance"""), 500, True)
    game.splash("wasd/arrow keys to select and a to confirm")
    A = True

def SelectPosition():
    global SON, SelectChoice, Walk
    if A == True:
        if controller.down.is_pressed() and SON >= 1 and SON < 4:
            SON += 1
            pause(100)
        if controller.up.is_pressed() and SON <= 4 and SON > 1:
            SON -= 1
            pause(100)
        if SON == 1:
            select.set_position(105, 80)
            SelectChoice = 1
        elif SON == 2:
            select.set_position(105, 90)
            SelectChoice = 2
        elif SON == 3:
            select.set_position(105, 100)
            SelectChoice = 3
        elif SON == 4:
            select.set_position(105, 110)
            SelectChoice = 4
        global D, E, C
    if C == True:
        if controller.A.is_pressed() and SelectChoice == 1:
            MSprite.set_image(assets.image("""AttackChoice"""))
            D = True
            E = True
            pause(100)
    if E == True:
        C = False
        if controller.A.is_pressed() and SelectChoice == 1:
            MSprite.set_image(assets.image("""ChoiceButton"""))
            F = True
            D = False
        if F == True:
            
            AttackTrue()
            def AttackTrue():
                global EnemyHitNumber
                AttackEnemy = game.ask_for_number("enemy 1, 2, 3, 4")
                
                if AttackEnemy > EnemyNumber:
                    game.splash("invalid Enemy")
                    AttackTrue()
                elif AttackEnemy == 1:
                    EnemyHitNumber = 1
                elif AttackEnemy == 2:
                    EnemyHitNumber = 2
                elif AttackEnemy == 3:
                    EnemyHitNumber = 3
                elif AttackEnemy == 4:
                    EnemyHitNumber = 4

            if EnemyHitNumber == 1:
                SlimeHealth1.value -= dmg
            if EnemyHitNumber == 2:
                SlimeHealth3.value -= dmg
            if EnemyHitNumber == 3:
                SlimeHealth2.value -= dmg
            if EnemyHitNumber == 4:
                SlimeHealth4.value -= dmg

            F = False
            E = False
            C = True
            
    if D == True:
        global E, C
        if SON == 4 and SelectChoice == 4 and controller.A.is_pressed():
            MSprite.set_image(assets.image("""ChoiceButton"""))
            E = False
            C = True

    # end fight
    if AllEnemyDead == EnemyNumber:
        global EnemyNumber, A, MoveForever, Walk, InventoryUse
        pause(100)
        tiles.set_current_tilemap(tilemap("""tutorial"""))
        pause(400)
        MC.set_position(MCX, MCY)
        Walk = True
        MoveForever = True
        EnemyNumber -= 1
        A = False
        InventoryUse = True
        

game.on_update(SelectPosition)

# Move
def Move():
    if MoveForever == True:
        controller.move_sprite(MC, 100, 100)
game.on_update(Move)

# MC on start
def MConStart():
    tiles.place_on_random_tile(MC, assets.tile("""start"""))

# Tutorial
def Tutorial():
    tiles.set_current_tilemap(tilemap("""tutorial"""))
    tiles.place_on_random_tile(MC, assets.tile("""start"""))
    tiles.set_tile_at(tiles.get_tile_location(5, 6), assets.tile("""TutFloor"""))
    tiles.place_on_tile(slime, tiles.get_tile_location(31, 6))
    exit = sprites.create(assets.image("""exit"""), SpriteKind.TutExit)
    tiles.place_on_tile(exit, tiles.get_tile_location(33, 6))
def ExitTut():
    global level
    level = 1
    WorldMap()
Tutorial()
sprites.on_overlap(SpriteKind.player, SpriteKind.TutExit, ExitTut)

# directions
def directions():
    game.splash("press menu for inventory")
    game.splash("wasd or arrow keys to Move")

# death
def slimedead():
    global slime_xp, MC_xp
    slime.destroy()
    MC_xp += slime_xp
statusbars.on_zero(StatusBarKind.enemy_health, slimedead)

# inventory
invN = 2
inv: Sprite = None
def inventory_close():
    global invN
    if InventoryUse == True:
        if invN == 1:
            invN = 2
            inv.destroy()
            scaling.scale_by_pixels(MC, -48, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
            scene.camera_follow_sprite(MC)
            MC.set_position(X + 42, Y)
            XpText.destroy()
            game.show_long_text("inventory closed starting game", DialogLayout.FULL)
            controller.move_sprite(MC)
def inventory():
    global invN, inv, MC, XpText, McHealth
    if InventoryUse == True:
        if invN == 2:
            # create inv
            inv = sprites.create(assets.image("""Inventory"""), SpriteKind.Inventory)
            inv.set_position(X, Y)

            # MC
            controller.move_sprite(MC, 0, 0)
            XN = X
            YN = Y
            scene.center_camera_at(XN, YN)
            MC.destroy()
            MC = sprites.create(assets.image("""
                MC
            """), SpriteKind.player)
            MC.set_position(XN - 42, YN)
            scaling.scale_by_pixels(MC, 48, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)

            # MC health
            McHealth.destroy()
            McHealth = statusbars.create(20, 4, StatusBarKind.health)
            McHealth.attach_to_sprite(MC)
            McHealth.set_offset_padding(0, -12)

            # XP
            XpText = textsprite.create("XP " + MC_xp + "/" + MaxXp)
            XpText.set_position(XN - 42, YN + 35)
            XpText.set_outline(1, 6)
            
            # invN
            invN = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, inventory_close)
controller.menu.on_event(ControllerButtonEvent.RELEASED, inventory)

# call direction
directions()

# MC Walk
controller.right.on_event(ControllerButtonEvent.PRESSED, RightWalk)
def RightWalk():
    if Walk == True:
        global direction
        animation.run_image_animation(MC, assets.animation("""
            RightWalk
        """), 250, True)
        direction = 2
        def RightWalkStop():
            animation.stop_animation(animation.AnimationTypes.ALL, MC)
        controller.right.on_event(ControllerButtonEvent.RELEASED, RightWalkStop)
controller.left.on_event(ControllerButtonEvent.PRESSED, LeftWalk)
def LeftWalk():
    if Walk == True:
        global direction
        animation.run_image_animation(MC, assets.animation("""
            LeftWalk
        """), 250, True)
        direction = 4
        def LeftWalkStop():
            animation.stop_animation(animation.AnimationTypes.ALL, MC)
        controller.left.on_event(ControllerButtonEvent.RELEASED, LeftWalkStop)
controller.up.on_event(ControllerButtonEvent.PRESSED, UpWalk)
def UpWalk():
    if Walk == True:
        global direction
        animation.run_image_animation(MC, assets.animation("""
            UpWalk
        """), 250, True)
        direction = 1
        def UpWalkStop():
            animation.stop_animation(animation.AnimationTypes.ALL, MC)
        controller.up.on_event(ControllerButtonEvent.RELEASED, UpWalkStop)
controller.down.on_event(ControllerButtonEvent.PRESSED, DownWalk)
def DownWalk():
    if Walk == True:
        global direction
        animation.run_image_animation(MC, assets.animation("""
            DownWalk
        """), 250, True)
        direction = 3
        def DownWalkStop():
            animation.stop_animation(animation.AnimationTypes.ALL, MC)
    controller.down.on_event(ControllerButtonEvent.RELEASED, DownWalkStop)

# world map
def WorldMap():
    if level == 1:
        tiles.set_current_tilemap(tilemap("""WorldMap"""))
