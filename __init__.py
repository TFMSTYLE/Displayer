# SPDX-FileCopyrightText: 2025-2026 The French Monkey
# SPDX-License-Identifier: GPL-3.0-or-later

bl_info = {
    "name": "Displayer",
    "author": "The French Monkey",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Displayer",
    "description": "Toggle multiple objects display",
    "category": "Object",
    "license": "GPL-3.0-or-later",
}

import bpy

try:
    from . import relay_updater
except ImportError:  # the Addon Collection has its own updates
    relay_updater = None

# --------------------
# Utilities
# --------------------

def set_display_type(obj, display_type):
    try:
        obj.display_type = display_type
    except Exception:
        pass

# --------------------
# Operators
# --------------------

class OBJECT_OT_displayer_apply(bpy.types.Operator):
    bl_idname = "object.displayer_apply"
    bl_label = "Apply Display Type"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        selected = list(context.selected_objects)
        display_type = scene.displayer_display_type

        if not selected:
            self.report({'ERROR'}, "No objects selected.")
            return {'CANCELLED'}

        for obj in selected:
            set_display_type(obj, display_type)

        self.report({'INFO'}, f"Set display type '{display_type}' on {len(selected)} object(s).")
        return {'FINISHED'}


class OBJECT_OT_displayer_reset(bpy.types.Operator):
    bl_idname = "object.displayer_reset"
    bl_label = "Reset Display Type"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected = list(context.selected_objects)
        if not selected:
            self.report({'ERROR'}, "No objects selected.")
            return {'CANCELLED'}

        for obj in selected:
            set_display_type(obj, 'TEXTURED')

        self.report({'INFO'}, f"Reset display type on {len(selected)} object(s).")
        return {'FINISHED'}

# --------------------
# UI
# --------------------

class VIEW3D_PT_displayer(bpy.types.Panel):
    bl_label = "Displayer"
    bl_idname = "VIEW3D_PT_displayer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Displayer'

    def draw(self, context):
        if relay_updater:
            relay_updater.draw(self.layout)
        layout = self.layout
        scene = context.scene
        selected = list(context.selected_objects)

        layout.operator("object.displayer_apply", text="Apply Display", icon="XRAY")
        layout.operator("object.displayer_reset", text="Reset Display", icon="LOOP_BACK")

        layout.separator(factor=0.5)

        row = layout.row(align=True)
        row.prop(scene, "displayer_display_type", expand=True)

        layout.separator(factor=0.5)

        layout.label(text=f"Selected objects: {len(selected)}")

# --------------------
# Registration
# --------------------

classes = (
    OBJECT_OT_displayer_apply,
    OBJECT_OT_displayer_reset,
    VIEW3D_PT_displayer,
)

def register():
    if relay_updater:
        relay_updater.register("blender-displayer")
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.displayer_display_type = bpy.props.EnumProperty(
        name="Display Type",
        description="Choose how to display selected objects",
        items=[
            ('BOUNDS', "Bounds", "Display as bounding box"),
            ('WIRE', "Wire", "Display as wireframe"),
            ('SOLID', "Solid", "Display as solid shading"),
            ('TEXTURED', "Textured", "Display with materials and textures"),
        ],
        default='SOLID'
    )

def unregister():
    if relay_updater:
        relay_updater.unregister()
    del bpy.types.Scene.displayer_display_type

    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
