import bpy
import bpy_extras
from mathutils import Euler
import math
import mathutils
import numpy as np
import random

def getExtremeVerts(obj) : 
    v0 = mathutils.Vector(obj.data.vertices[0].co)
    exts = {'left':v0, 'right':v0, 'up':v0, 'down':v0, 'front':v0, 'back':v0}
    
    for vert in obj.data.vertices :
        
        v = obj.matrix_world @ mathutils.Vector(vert.co)
        
        if (v.x > exts['right'].x) :
            exts['right'] = v
        if (v.x < exts['left'].x) :
            exts['left'] = v

        if (v.y > exts['front'].y) :
            exts['front'] = v
        if (v.y < exts['back'].y) :
            exts['back'] = v

        if (v.z > exts['up'].z) :
            exts['up'] = v
        if (v.z < exts['down'].z) :
            exts['down'] = v


    return (exts)

#Should use this only when everything is in place
def getBoundRect(obj , cam) : 
    v0 = mathutils.Vector(obj.data.vertices[0].co)
    bnds = {'xMin':v0.x, 'yMin':v0.y, 'xMax':v0.x, 'yMax':v0.y}
    
    for vert in obj.data.vertices :
        
        coord = obj.matrix_world @ mathutils.Vector(vert.co)
        v = bpy_extras.object_utils.world_to_camera_view(bpy.context.scene, cam, coord)
        
        if (v.x < bnds['xMin']) :
            bnds['xMin'] = v.x
        if (v.x > bnds['xMax']) :
            bnds['xMax'] = v.x
        
        if (v.y < bnds['yMin']) :
            bnds['yMin'] = v.y
        if (v.y > bnds['yMax']) :
            bnds['yMax'] = v.y

    return (bnds)



def randLocRotInView(obj, cam, distMin, distMax) :

    data = {'BBox' : [0,0,0,0], 'BBox3D' : [], 'Distance' : 0} 
    
    obj.rotation_mode = "XYZ"
    obj.rotation_euler = Euler( (((random.random()*2-1) * math.pi), ((random.random()*2-1) * math.pi), ((random.random()*2-1)) * math.pi), 'XYZ')
    
    dist = random.random() * (distMax-distMin) + distMin
    
    obj.location = (0, dist, 0)

    safeArea = .6
    
    posX = (random.random()*2-1) * safeArea * (dist * math.tan(cam.data.angle_x/2))
    posZ = (random.random()*2-1) * safeArea * (dist * math.tan(cam.data.angle_y/2))
        
    obj.location = (posX, dist, posZ)

    bpy.context.view_layer.update()

    for c in obj.bound_box :
        data['BBox3D'].append(list(np.around(list(bpy_extras.object_utils.world_to_camera_view(bpy.context.scene, cam, obj.matrix_world @ mathutils.Vector(c))),decimals=4)))

    data['Distance'] = np.around(mathutils.Vector(obj.location).y, decimals=4)

    return data

#todo, figure out why getExtremeVerts['back'] is wrong as hell




    
    

