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
    enemy_health2 = StatusBarKind.create()

# variables
health = 100
direction = 0
X = 0
Y = 0
dmg = 10
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
EnemyNumber = 0
AttackEnemyValid = False

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

# enemy fight 

def SlimeFight():
    global SlimeN, SlimeFightStillGoing, SX, SY, SX2, SY2, EnemyNumber
    fight()
    EnemyNumber = 4
    SX = 15
    SY = 12
    SX2 = 15 + 15
    SY2 = 12 + 16
    slimeCreate()

def slimeCreate():
    global SX, SY, SX2, SY2, SlimeHealth1, SlimeHealth2, SlimeHealth3, SlimeHealth4 
    if EnemyNumber >= 1:
        # 1
        slime1 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime1, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime1.set_position(SX, SY)
        SlimeHealth1 = statusbars.create(20, 4, StatusBarKind.enemy_health)
        SlimeHealth1.attach_to_sprite(slime1)
        SlimeHealth1.value = 100
        SY += 32
        
    if EnemyNumber >= 2:
        #2
        slime2 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime2, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime2.set_position(SX, SY)
        SlimeHealth2 = statusbars.create(20, 4, StatusBarKind.enemy_health2)
        SlimeHealth2.attach_to_sprite(slime2)
        SlimeHealth2.value = 100
        SY += 32
        
    if EnemyNumber >= 3:
        #3
        slime3 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime3, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime3.set_position(SX2, SY2)
        SlimeHealth3 = statusbars.create(20, 4, StatusBarKind.enemy_health)
        SlimeHealth3.attach_to_sprite(slime3)
        SlimeHealth3.value = 100
        SY2 += 32
        
    if EnemyNumber == 4:
        #4
        slime4 = sprites.create(assets.image("""slime"""), SpriteKind.Slime)
        scaling.scale_by_pixels(slime4, -4, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        slime4.set_position(SX2, SY2)
        SlimeHealth4 = statusbars.create(20, 4, StatusBarKind.enemy_health)
        SlimeHealth4.attach_to_sprite(slime4)
        SlimeHealth4.value = 100
        SY2 += 32
        

sprites.on_overlap(SpriteKind.player, SpriteKind.Slime, SlimeFight)

def fight():
    
    # tilemap
    tiles.set_current_tilemap(tilemap("""FightRing"""))
    
    # background
    scene.set_background_image(assets.image("""DungeonFight"""))
    
    # MC
    tiles.place_on_tile(MC, tiles.get_tile_location(7, 3))
    controller.move_sprite(MC, 0, 0)
    
    # Button
    button()

# Button
def button():
    global select, A, C, Walk, MSprite, SlimeHealth4
    MSprite = sprites.create(assets.image("""ChoiceButton"""), SpriteKind.Random)
    MSprite.set_position(80, 95)
    # select
    select = sprites.create(assets.image("""Select"""), SpriteKind.Random)
    A = True
    C = True
    Walk = False
    animation.run_image_animation(MC, assets.animation("""AttackStance"""), 500, True)

def SelectPosition():
    global SON, SelectChoice
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
            MSprite.set_image(assets.image("""AttackWho"""))
            F = True
            D = False
        if F == True:
            while AttackEnemyValid == False:
                attackenemy = game.ask_for_number("attack enemy 1, 2, 3, 4")
                if attackenemy >= 1 and attackenemy <= EnemyNumber:
                    AttackEnemyValid = True
                else:
                    game.splash("invalid enemy")
            if attackenemy == 1:
                SlimeHealth1.value -= dmg

    if D == True:
        global E, C
        if SON == 4 and SelectChoice == 4 and controller.A.is_pressed():
            MSprite.set_image(assets.image("""ChoiceButton"""))
            E = False
            C = True

game.on_update(SelectPosition)

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
    game.splash("press a to attack")
    game.splash("press menu for inventory")

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

# attack
controller.A.on_event(ControllerButtonEvent.PRESSED, Swing)
def Swing():
    if Walk == True:
        if direction == 1:
            animation.run_image_animation(MC, assets.animation("""
                UpSwing
            """), 250, False)
            pause(250)
            hit = sprites.create(assets.image("""UpHit"""), SpriteKind.hit)
            hit.set_position(X, Y)
            hit.follow(MC, 800)
            pause(500)
            hit.destroy()
            UpWalk()
        if direction == 2:
            animation.run_image_animation(MC, assets.animation("""
                RightSwing
            """), 250, False)
            pause(250)
            hit = sprites.create(assets.image("""RightHit"""), SpriteKind.hit)
            hit.set_position(X, Y)
            hit.follow(MC, 800)
            pause(500)
            hit.destroy()
            RightWalk()
        if direction == 3:
            animation.run_image_animation(MC, assets.animation("""
                DownSwing
            """), 250, False)
            pause(250)
            hit = sprites.create(assets.image("""DownHit"""), SpriteKind.hit)
            hit.set_position(X, Y)
            hit.follow(MC, 800)
            pause(500)
            hit.destroy()
            DownWalk()
        if direction == 4:
            animation.run_image_animation(MC, assets.animation("""
                LeftSwing
            """), 250, False)
            pause(250)
            hit = sprites.create(assets.image("""LeftHit"""), SpriteKind.hit)
            hit.set_position(X, Y)
            hit.follow(MC, 800)
            pause(500)
            hit.destroy()
            LeftWalk()

# world map
def WorldMap():
    if level == 1:
        tiles.set_current_tilemap(tilemap("""WorldMap"""))
