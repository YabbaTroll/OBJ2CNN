import bpy
import random

def randMorbing(morb, start):
    max = morb.image_user.frame_duration
    morb.image_user.frame_offset = random.randint(start, max)
    pass