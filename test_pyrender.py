import pyrender
import numpy as np
import trimesh

     # Simple test scene (manual, no built-in function)
scene = pyrender.Scene(ambient_light=[0.1, 0.1, 0.1])
     
     # Add a red cube
mesh = trimesh.load('models/model.glb', file_type='gltf')
material = pyrender.MetallicRoughnessMaterial(baseColorFactor=[0.8, 0.8, 0.8, 1.0])
renderable = pyrender.Mesh.from_trimesh(mesh, material=material)
scene.add(renderable, pose=np.eye(4))
     
     # Add light
light = pyrender.DirectionalLight(color=np.ones(3), intensity=3.0)
scene.add(light, pose=np.eye(4))
     
     # Viewer (opens window)
v = pyrender.Viewer(scene, resolution=(800, 600), run_in_thread=False)
v.close()  # Closes after you interact (or auto on quit)
print("Pyrender test successful!")
