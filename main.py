@namespace
class SpriteKind:
    hit = SpriteKind.create()


# variables
direction = 0
X = 0
Y = 0
dmg = 1

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

# enemy
slime = sprites.create(assets.image("""slime"""), SpriteKind.enemy)
statusbar = statusbars.create(20, 4, StatusBarKind.enemy_health)
statusbar.attach_to_sprite(slime)
statusbar.value = 10
def SlimeHit(sprite, othersprite):
    statusbar.value -= 1
    pause(500)
sprites.on_overlap(SpriteKind.hit, SpriteKind.enemy, SlimeHit)

# Tutorial Tilemap
tiles.set_current_tilemap(tilemap("""tutorial"""))
tiles.place_on_random_tile(MC, assets.tile("""start"""))
tiles.set_tile_at(tiles.get_tile_location(2, 3), assets.tile("""TutFloor"""))
tiles.place_on_tile(slime, tiles.get_tile_location(60, 3))

# directions
game.splash("press a to attack")

# death
def slimedead():
    slime.destroy()
statusbars.on_zero(StatusBarKind.enemy_health, slimedead)

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
