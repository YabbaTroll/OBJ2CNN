import sys

scriptPath = "C:\\Users\\Yabba\\Documents\\Projects\\SeniorResearch\\BlenderScripts\\Corsair"
sys.path = [i for i in sys.path if i != scriptPath]
sys.path.append(scriptPath)
import os
import bpy
import bpy_extras
from opRandPoseInView import randLocRotInView
import pprint
#import time
from datetime import datetime
from datetime import time
from mathutils import Euler
import random
import math

outPath = "C:\\Users\\Yabba\\Documents\\Projects\\SeniorResearch\\Output\\Corsair13\\"


pp = pprint.PrettyPrinter(indent=4)

cam = bpy.data.scenes['Scene'].camera
obj = bpy.data.objects['F4U-4B']

picCount = 128
random.seed('XF8B') 

timeStart = datetime.now()
for i in range(picCount):

    datum = randLocRotInView(obj,cam,20,30)

    bpy.context.scene.render.stamp_note_text = str(datum)
    bpy.context.scene.render.filepath = '{}pic{:03d}.png'.format(outPath, i)
    bpy.ops.render.render(write_still=True)

    pass


timeEnd = datetime.now()
timeDuration = timeEnd-timeStart

print('{} pictures created in {}'.format(picCount, timeDuration))


#print(obj.location)