import sys

scriptPath = "C:\\Users\\Yabba\Documents\\Projects\\SeniorResearch\\OBJ2CNN\\ScriptsBlender"
sys.path = [i for i in sys.path if i != scriptPath]
sys.path.append(scriptPath)
import os
import bpy
import bpy_extras
from opRandPoseInViewV2 import randLocRotInView
from opMorbingTime import randMorbing
from opMaskProcess import procMask
import pprint
import numpy as np
#import time
from datetime import datetime
from datetime import time
from mathutils import Euler
import random
import math

outPath = "C:\\Users\\Yabba\\Documents\\Projects\\SeniorResearch\\OBJ2CNN\\OutputPics\\WhiteBall\\"

outPathPics = outPath + 'pics\\' 
outPathMask = outPath + 'masks\\' 

pp = pprint.PrettyPrinter(indent=4)

cam = bpy.data.scenes['Scene'].camera
obj = bpy.data.objects['Sphere']
morb = bpy.data.worlds["World"].node_tree.nodes["Environment Texture.001"]
light = bpy.data.objects['Light']

picCount = 512
random.seed('XF8B') 

timeStart = datetime.now()
for i in range(picCount):

    data = {'BBox' : [0,0,0,0], 'BBox3D' : []}  
    data['BBox3D'] = randLocRotInView(obj,cam,4,12)['BBox3D']
    randLocRotInView(light,cam,4,20)['BBox3D']
    randMorbing(morb,2000)

    #mask rendering
    bpy.context.scene.render.stamp_note_text = ''
    bpy.context.scene.render.filepath = '{}pic{:03d}.png'.format(outPathMask, i)

    bpy.context.scene.render.film_transparent = True

    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 1
    bpy.context.scene.view_settings.gamma = 1
    bpy.context.scene.view_settings.exposure = 32

    bpy.context.view_layer.update()

    bpy.ops.render.render(write_still=True)

    #mask operating
    data['BBox'] = [ np.around(p, decimals = 4) for p in procMask('{}pic{:03d}.png'.format(outPathMask, i))]

    #Color pic rendering
    bpy.context.scene.render.stamp_note_text = str(data)
    bpy.context.scene.render.filepath = '{}pic{:03d}.png'.format(outPathPics, i)

    bpy.context.scene.render.film_transparent = False

    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 10
    bpy.context.scene.view_settings.gamma = 1
    bpy.context.scene.view_settings.exposure = 0

    bpy.context.view_layer.update()

    bpy.ops.render.render(write_still=True)

    pass


timeEnd = datetime.now()
timeDuration = timeEnd-timeStart

print('{} pictures created in {}'.format(picCount, timeDuration))


#print(obj.location)