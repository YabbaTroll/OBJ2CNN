import os
import bpy
from datetime import datetime

timeBegin = datetime.now()
ts = timeBegin.strftime('%Y-%m-%d_%H-%M-%S')
print(ts)

path = "E:\Blender\BlenderWork\^CV Training Dataset Generation\OBJ files"
datasetPath = "E:\Blender\BlenderWork\^CV Training Dataset Generation\Training Data\ScriptTesting"
datasetName = "Test"
dirList = [] 



print("***** **** *** ** *")
print("01 Checking Input Directory\n")
for folder in os.listdir(path) :
    if os.path.isfile(path+'\\'+folder+'\\'+folder+'.obj') :
        #dirList.append(path+'\\'+folder+'\\'+folder+".obj")
        dirList.append(folder)

print(len(dirList)," file\s have been found : ")

for f in dirList :
    print(f)
    
print("")
print("Creating Output directory")
outDir = os.path.join(datasetPath,datasetName+' '+ts)
os.makedirs(outDir)
#print ('outDir = '+outDir)



print("")
print("02- Importing")

cameras = bpy.data.collections['162 Camera Icosphere'].objects
#print(len(cameras))

for p in dirList :
    bpy.ops.import_scene.obj(filepath= path+'\\'+p+'\\'+p+'.obj',use_groups_as_vgroups=True,split_mode='OFF')
    
    plane = bpy.context.selected_objects[0]
    plane.name = p
    
    
    #Should probably this output 'dimensions' around here
    gNode = plane.modifiers.new('PlaneResizer','NODES')
    gNode.node_group = bpy.data.node_groups['SubjectResizer']
    
    outFileDir = outDir+'\\'+p
    os.makedirs(outFileDir)
    
    for c in cameras :
        bpy.context.scene.camera = c
        print(c.name)
        outFile = outFileDir+'\\'+c.name+'.png'
        bpy.context.scene.render.filepath = outFile
        bpy.ops.render.render(write_still=True)
    
    bpy.ops.object.delete()
    print("imported "+ p +"...")


timeEnd = datetime.now()
elapsedTime = timeEnd-timeBegin

print('Total images rendered :'+ str(len(cameras)*len(dirList)))
print('Time elapsed :' + str(elapsedTime))
#print('Generated '+len(dirList)+ 'datasets in  '+ (datetime.now()-timeBegin).total_seconds() +' seconds')
    
    