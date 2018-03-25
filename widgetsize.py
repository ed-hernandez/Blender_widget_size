bl_info = {
    "name": "WidgetSize",
    "author": "Ed-Hernandez",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3D > properties-panel",
    "description": "fast change witget size",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
    }

import bpy

class WidgetSize(bpy.types.Panel):
    """creates a panel for the addon"""
    bl_label = "Widget Size"
    bl_idname = "WidgetSize"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()

        row = col.row()
        row.label(text = "WitgetSize")
        
        row = col.row()
        row.prop(bpy.context.user_preferences.view, "manipulator_size", toggle=True, text = "size")
        
        row = col.row()
        row.label(text = "WitgetSize")
        
        row = col.row()
        row.prop(bpy.context.user_preferences.view, "manipulator_handle_size", toggle=True, text = "handle size")

def register():
    bpy.utils.register_class(WidgetSize)
    

def unregister():
    bpy.utils.unregister_class(WidgetSize)
    
if __name__ == "__main__":
    register()
