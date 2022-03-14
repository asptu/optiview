
bl_info = {
	"name": "OptiView",
	"author": "Asptu#0003",
	"version": (0, 1, 0),
	"blender": (2, 80, 0),
	"description": "Provides the ability to swap high resolution materials between the viewport and the final render, https://github.com/asptu/optiview#optiview",
	"location": "",
	"warning": "bad code lol",
	"category": "RENDER"}


import bpy


# Activates Render Texture

def main(context):
    
# Switches to Solid View so you don't have to load in the texture

    my_areas = bpy.context.workspace.screens[0].areas
    my_shading = 'SOLID'  # 'WIREFRAME' 'SOLID' 'MATERIAL' 'RENDERED'
    
    for area in my_areas:
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = my_shading

# Swaps from VIEWPORT Material Output to RENDER Material Output
                
    nodes =  bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes :
            if node.label == 'RENDER' :
                node.is_active_output = True
            if node.label == 'VIEWPORT' :
                node.is_active_output = False

# Defines the RENDER Operator

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Render Material"


    def execute(self, context):
        main(context)
        return {'FINISHED'}
    

# Activates Viewport texture

def main2(context):
    
# Swaps from RENDER Material Output to VIEWPORT Material Output

    nodes =  bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes :
            if node.label == 'VIEWPORT' :
                node.is_active_output = True
            if node.label == 'RENDER' :
                node.is_active_output = False

# Defines the VIEWPORT Operator

class SimpleOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator1"
    bl_label = "Viewport Material"


    def execute(self, context):
        main2(context)
        return {'FINISHED'}
    
# Adds the custom Material Outputs 
    
def main3(context):
    
# Deletes the existing Material Output

    mat = bpy.data.materials['Material']

    node_to_delete =  mat.node_tree.nodes['Material Output']

    nodes =  bpy.context.active_object.active_material.node_tree.nodes
    for node in nodes :
            if node.name == 'Material Output' :
                mat.node_tree.nodes.remove( node_to_delete )
                
# Creates 2 new Material Outputs
                
    nodes = bpy.context.active_object.active_material.node_tree.nodes
    links = bpy.context.active_object.active_material.node_tree.links

    viewport = nodes.new('ShaderNodeOutputMaterial')
    render = nodes.new('ShaderNodeOutputMaterial')


    render.location = (400, 0)
    viewport.location = (400, 200)

    render.label = "RENDER"
    viewport.label = "VIEWPORT"
    
# Defines the Add Outputs Operator
                
class SimpleOperator3(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator3"
    bl_label = "Add Outputs"


    def execute(self, context):
        main3(context)
        return {'FINISHED'}
    
    
# Render Properties Panel

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "OptiView"
    bl_idname = "ayo"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Viewport Texture Button
        layout.label(text="Optimised Material:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("object.simple_operator1")
        

        # Render Texture Button
        layout.label(text="Full Quality Material:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("object.simple_operator")
        
# Node Properties Panel

class ADDON_PT_Panel(bpy.types.Panel):
    
    bl_label = "OptiView"
    bl_idname = "ADDON_PT_Panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Node"
    
    
    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"    

    def draw(self,context):
        layout = self.layout

        # Add Outputs Button
        layout.label(text="Add Material Outputs:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("object.simple_operator3")
        

#register junk
def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimpleOperator2)
    bpy.utils.register_class(SimpleOperator3)
    bpy.utils.register_class(ADDON_PT_Panel)

def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(SimpleOperator2)
    bpy.utils.unregister_class(SimpleOperator3)
    bpy.utils.unregister_class(ADDON_PT_Panel)

    

if __name__ == "__main__":
    register()
