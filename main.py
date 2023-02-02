@namespace
class SpriteKind:
    hit = SpriteKind.create()
    Inventory = SpriteKind.create()
@namespace
class StatusBarKind:
    XP = StatusBarKind.create()

# variables
direction = 0
X = 0
Y = 0
dmg = 10
MC_xp = 0
health = 0
MaxXp = 10
XpText: TextSprite = None

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
slime = sprites.create(assets.image("""slime"""), SpriteKind.enemy)
statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
statusbar.attach_to_sprite(slime)
statusbar.value = 100
slime_xp = 1
def SlimeHit(sprite, othersprite):
    statusbar.value -= dmg
    pause(500)
sprites.on_overlap(SpriteKind.hit, SpriteKind.enemy, SlimeHit)

# Tutorial Tilemap
def Tutorial():
    tiles.set_current_tilemap(tilemap("""tutorial"""))
    tiles.place_on_random_tile(MC, assets.tile("""start"""))
    tiles.set_tile_at(tiles.get_tile_location(2, 3), assets.tile("""TutFloor"""))
    tiles.place_on_tile(slime, tiles.get_tile_location(28, 3))
Tutorial()

# directions
game.splash("press a to attack")

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
        game.splash("inventory closed starting game")
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
        
        # invN
        invN = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, inventory_close)
controller.menu.on_event(ControllerButtonEvent.RELEASED, inventory)

# MC Walk
controller.right.on_event(ControllerButtonEvent.PRESSED, RightWalk)
def RightWalk():
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
