import bpy
import sys
from io_scene_usdz import import_usdz

args = sys.argv

if len(args) != 5:
    print("Invalid arguments")
    sys.exit(1)

input = args[3]
output = args[4]

# First import the .usdz model
import_usdz.import_usdz(bpy.context, filepath=input)

# Hide the default camera, light, cube setup in Blender
bpy.data.collections[0].hide_viewport = True

# Now export the scene as a .gltf file
# https://docs.blender.org/api/current/bpy.ops.export_scene.html#bpy.ops.export_scene.gltf
bpy.ops.export_scene.gltf(filepath=output, use_visible=True)

sys.exit(0)
