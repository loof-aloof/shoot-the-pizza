def on_a_pressed():
    global bullet
    bullet = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 5 5 5 5 5 . . . . . . . 
                    . . . . 4 4 4 4 5 5 . . . . . . 
                    . . . . e e e 4 4 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        dude,
        68,
        1)
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global Pizza
    info.change_score_by(10)
    Pizza.destroy(effects.spray, 200)
    music.ba_ding.play_until_done()
    Pizza = sprites.create(img("""
            . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . e e e e e e e e . . . . . . 
                    . . . . . . e e e e e e e e e e . . . . . 
                    . . . . . . e 2 5 5 5 5 5 5 5 5 . . . . . 
                    . . . . . . e 2 5 5 f f 5 f f 5 . . . . . 
                    . . . . . . e 2 5 5 f f 5 f f 5 . . . . . 
                    . . . . . . . e 2 5 5 5 5 5 5 . . . . . . 
                    . . . . . . . e 2 5 5 f f f 5 . . . . . . 
                    . . . . . . . . e 2 5 f f 2 5 . . . . . . 
                    . . . . . . . . e 2 5 5 5 2 . . . . . . . 
                    . . . . . . . . . e 2 5 5 2 . . . . . . . 
                    . . . . . . . . . f e 2 5 f . . . . . . . 
                    . . . . . . . . . f . e 5 f . . . . . . . 
                    . . . . . . . . . f . . . f . . . . . . . 
                    . . . . . . . . . f . . . f . . . . . . . 
                    . . . . . . . . f f . . . f f . . . . . .
        """),
        SpriteKind.enemy)
    Pizza.set_position(randint(0, 120), randint(0, 120))
    Pizza.follow(dude, 20)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    game.over(False, effects.splatter)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bullet: Sprite = None
Pizza: Sprite = None
dude: Sprite = None
scene.set_background_color(13)
dude = sprites.create(img("""
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . 5 5 5 5 5 5 5 5 5 5 5 . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . 2 f f f f f f f f f f f f f . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . 2 5 f f f f f 5 f f f f f 5 . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . 2 5 5 f f f f 5 f f f f 5 5 . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . 5 5 5 f f 5 5 5 f f 5 5 5 b b b b b b . . . . . . . . . . . . . 
            . . . . . . . . . 5 5 5 5 5 5 5 5 5 5 5 5 5 b b b b b b . . . . . . . . . . . . . 
            . . . . . . . . . 5 5 5 5 5 5 5 5 5 5 5 5 5 f f . b . . . . . . . . . . . . . . . 
            . . . . . . . . . . 5 5 5 5 f f f 5 5 5 5 . f f b . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . 5 5 f 5 5 5 f 5 5 . . f f . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . 5 5 5 5 5 5 5 . . . b b . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
dude.set_position(13, 11)
info.set_score(0)
controller.move_sprite(dude)
Pizza = sprites.create(img("""
        . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . e e e e e e e e . . . . . . 
            . . . . . . e e e e e e e e e e . . . . . 
            . . . . . . e 2 5 5 5 5 5 5 5 5 . . . . . 
            . . . . . . e 2 5 5 f f 5 f f 5 . . . . . 
            . . . . . . e 2 5 5 f f 5 f f 5 . . . . . 
            . . . . . . . e 2 5 5 5 5 5 5 . . . . . . 
            . . . . . . . e 2 5 5 f f f 5 . . . . . . 
            . . . . . . . . e 2 5 f f 2 5 . . . . . . 
            . . . . . . . . e 2 5 5 5 2 . . . . . . . 
            . . . . . . . . . e 2 5 5 2 . . . . . . . 
            . . . . . . . . . f e 2 5 f . . . . . . . 
            . . . . . . . . . f . e 5 f . . . . . . . 
            . . . . . . . . . f . . . f . . . . . . . 
            . . . . . . . . . f . . . f . . . . . . . 
            . . . . . . . . f f . . . f f . . . . . .
    """),
    SpriteKind.enemy)
Pizza.follow(dude, 20)