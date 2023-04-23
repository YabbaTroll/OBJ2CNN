import sys

scriptPath = "C:\\Users\\Yabba\\Documents\\Projects\\SeniorResearch\\ScriptsBlender"
sys.path = [i for i in sys.path if i != scriptPath]
sys.path.append(scriptPath)

import os
import bpy
import bpy_extras
from opRandPoseInViewV2 import randLocRotInView
from opMorbingTime import randMorbing
import pprint

from mathutils import Euler
import random
import math

outPath = "C:\\Users\\Yabba\\Documents\\Projects\\SeniorResearch\\BlenderScripts\\Corsair\\"

print(os.getcwd())
print(str(sys.path) + '\n\n')
pp = pprint.PrettyPrinter(indent=4)

cam = bpy.data.scenes['Scene'].camera
obj = bpy.data.objects['F4U-4B']
morb = bpy.data.worlds["World"].node_tree.nodes["Environment Texture.001"]

#blah
#obj.rotation_euler = Euler( (((random.random()*2-1) * math.pi), ((random.random()*2-1) * math.pi), ((random.random()*2-1)) * math.pi), 'XYZ')

test = randLocRotInView(obj,cam,20,30)
randMorbing(morb,2000)

pp.pprint(str(test)) 

bpy.context.scene.render.stamp_note_text = str(test)
    #outFile = outFileDir+'\\'+c.name+'.png'
    
bpy.context.scene.render.filepath = outPath + 'testPic.png'
bpy.ops.render.render(write_still=True)



#print(obj.location)