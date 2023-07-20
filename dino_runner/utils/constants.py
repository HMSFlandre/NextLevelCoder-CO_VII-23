import pygame
import os

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

BULLETS = [
    pygame.image.load(os.path.join(IMG_DIR, "Spell/BulletYellow.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Spell/BulletBlue.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Spell/BulletRed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Spell/BulletBlack.png"))
]

HITBOX = pygame.image.load(os.path.join(IMG_DIR, "Other/Hitbox.png"))
SPELL_CIRCLE = pygame.image.load(os.path.join(IMG_DIR, "Spell/SpellCircle.png"))
CHEN = pygame.image.load(os.path.join(IMG_DIR, "Chen/Chen.png"))

SUNS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/Sun0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Sun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Sun2.png"))
]
MOONS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/Moon0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Moon1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Moon2.png"))
]
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
MOYAI = pygame.image.load(os.path.join(IMG_DIR, 'Other/Moyai.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
GRAZE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Graze.png'))
POINT = pygame.image.load(os.path.join(IMG_DIR, 'Other/Point.png'))
P_SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/ProtoShield.png'))
S_BARRIER = pygame.image.load(os.path.join(IMG_DIR, 'Other/SkullBarrier.png'))
SKULLS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/Skull1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Skull2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/Skull3.png"))
]
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
SHIELD_SILOUETTE = pygame.image.load(os.path.join(IMG_DIR, 'Other/ShieldShilouette.png'))

DEFAULT_TYPE = "default"
