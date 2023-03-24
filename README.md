# OBJ2CNN
A system for turning 3d models into CNN models that can be used for object classification/detection/segmentation

This project aims to explore the possibilities in using computer rendered images to train neural networks. Several modifications will be done to input datasets before and after rendering to determine what can assist computer vision in different scenarios. 

## File List :
**Everything here is to be considered unfinished, as many paths are hard coded**
- ScriptTesting.blend
: Main blender file that objects are rendered in
- AutoImport.py
: Python script that automatically imports and renders objects from a chosen directory, used inside ScriptTesting.blend
- Trainer.ipynb
: A Python notebook thats being used to generate a CNN based on the output of AutoImport.py 
- DetectTester.ipynb
: A Python notebook thats being used to quickly test the accurracy of models generated with Trainer.ipynb  

## Input 3D Model Directory Format (.obj file format)
```
└── ObjectSet/
    ├── Object_1/
    │   ├── Object_1.obj
    │   ├── Object_1.mtl
    │   └── textures/
    │       ├── tex1
    │       ├── tex2
    │       └── ...
    ├── Object_2/
    │   ├── Object_2.obj
    │   ├── Object_2.mtl
    │   └── textures/
    │       ├── tex1
    │       ├── tex2
    │       └── ...
    ├── Object_3/
    │   ├── Object_3.obj
    │   ├── Object_3.mtl
    │   └── textures/
    │       ├── tex1
    │       ├── tex2
    │       └── ...
    ├── Object_4/
    │   ├── Object_4.obj
    │   ├── Object_4.mtl
    │   └── textures/
    │       ├── tex1
    │       ├── tex2
    │       └── ...
    └── ...
				
