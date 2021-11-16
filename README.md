# optiview
OptiView is an incredibly simple viewport optimisation addon which uses multiple Material Outputs to swap between a Material with less detail in the Viewport and a full resolution Material in your render.

**optiview is currently in very early development, has very limited functionality and also is pretty bad code, contact Asptu#7386 if you run into any problems**

# Usage

To activate this addon, download the Source-Code.zip under releases, then once downloaded extract the optiview.zip and install the optiview.py under preferences, (for more information on installing addons see: https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#installing-add-ons)

Once installed, you will have access to 2 new 'OptiView' panels, one located in the **Render Properties tab** and the other located in the **Shader Editor.**
After you have created your material for your object, go to the 'OptiView' panel in the **Shader Editor** and click the **Add Outputs** button, which will create 2 new Material Output nodes, one named RENDER for your higher quality textures/materials and the other named VIEWPORT for your more optimised materials for a better viewport experience as seen in the screenshot below:

![Demo](https://github.com/asptu/optiview/blob/main/examples/2.PNG)

Once you have your 2 Material Outputs created you can attach your more complex materials into the RENDER output and the more optimised versions into the VIEWPORT output. When you're ready for rendering you'll want to navigate to the **Render Properties tab** and scroll down until you see the 'OptiView' category, within said category you'll see 2 different buttons. If you're about to render an image you'll want to click **Render Texture** which will automatically switch your view to solid mode and switch to your full quality render material. After finishing rendering you'll want to make sure you click on the **Viewport Texture** button to switch back to your optimised textures as the addon will not do it automatically. (see functionality plan)

![Demo2](https://github.com/asptu/optiview/blob/main/examples/1.PNG)

Other than that, the addon pretty much has no other functionality for now, please contact Asptu#7386 on discord if you run into any problems or you have any suggestions for features and happy blending!

# Functionality Plan

(None of these features are confirmed but are just things I would like to add to the addon)

- Automatically switches to Render Texture when you Render image/animation. (Removes the need for buttons)
- Add the RENDER and VIEWPORT material outputs when a new material is created.
- Automatically detect shader links for the Material Outputs?
- Automatically switch back to Viewport Material once finished rendering.
- Ability to cycle between higher or lower quality versions of an image texture.
- Learn Modal Operators -_-
