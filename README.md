# Displayer

![displayer-thumb](https://github.com/user-attachments/assets/e71abfd5-1c4e-4690-8eee-196a05c98e7c)

**Author:** The French Monkey (TFMSTYLE)  
**Version:** 1.0.2  

---

## Overview

The Displayer addon allows you to instantly change the viewport display type of selected objects.  
It provides a fast and consistent way to visualize geometry in different shading modes — useful for modeling, look development, or layout organization.  
You can switch multiple objects between Wireframe, Solid, Textured, and Bounds modes with a single click, and reset them at any time.

---

## Parameters

### Display Type
Defines how the selected objects are displayed in the 3D Viewport.  
Available display types include:

- **Bounds:** Shows objects as simple bounding boxes for maximum viewport performance.  
- **Wire:** Displays the wireframe overlay of the mesh for modeling clarity.  
- **Solid:** Shows standard shaded geometry without textures.  
- **Textured:** Displays the object with materials and texture shading.

---

## Operators

### Apply Display Type
Applies the selected Display Type to all currently selected objects in the scene.  
Useful for quickly changing shading modes across multiple meshes.

---

### Reset Display Type
Restores the Textured display mode to all selected objects.  
Use this to revert objects to standard viewport shading after inspection or optimization.

---

## Usage Notes

- Select one or more objects in the 3D Viewport.  
- Choose a Display Type from the options (Bounds, Wire, Solid, Textured).  
- Click **Apply Display** to set the mode for all selected objects.  
- Click **Reset Display** to revert them to Textured mode.  
- Ideal for performance optimization or isolating geometry during modeling.

---

## Install

Needs Blender 4.2 or later. Get the zip from [tfmstyle.com](https://tfmstyle.com), then in Blender open Edit > Preferences > Get Extensions, open the menu at the top right and pick Install from Disk.

To build the zip yourself, run this in the repo folder:

```bash
blender --command extension build
```

The addon is `__init__.py`, plus `relay_updater.py` for its update checks. It depends on nothing but Blender.

---

## License

GPL 3.0 or later. See [LICENSE](LICENSE).
