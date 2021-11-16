# optiview
OptiView is an incredibly simple viewport optimisation addon which uses multiple Material Outputs to swap between a Material with less detail in the Viewport and a full resolution Material in your render.

### optiview is currently in very early development and has very limited functionality, scroll down to see functionality road map.

# Usage

To activate this addon, download the Source-Code.zip under releases, then once downloaded extract the optview.zip and install the optview.py under preferences, (for more information on installing addons see: https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#installing-add-ons)

Once installed, you will have access to 2 new 'OptiView' panels, one located in the **Render Properties tab** and the other located in the **Shader Editor.**
After you have created your material for your object, go to the 'OptiView' panel in the **Shader Editor** and click the **Add Outputs** button, which will create 2 new Material Output nodes, one named RENDER for your higher quality textures/materials and the other named VIEWPORT for your more optimised materials for a better viewport experience as seen in the screenshot below:

![Demo](https://github.com/asptu/optiview/blob/main/examples/2.PNG)



# Functionality Plan

- Automatically switches to Render Texture when you Render image/animation. (Removes the need for buttons)
- Add the RENDER and VIEWPORT material outputs when a new material is created.
- Automatically detect shader links for the Material Outputs?
- Automatically switch back to Viewport Texture once finished rendering.
