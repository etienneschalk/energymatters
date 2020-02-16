import os 

# Folders ----------------------------------------------------------------------
folders = {}

# Root is the location of this config file
folders["root"] = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
folders["assets"] = os.path.join(folders["root"], "assets")
folders["images"] = os.path.join(folders["assets"], "images")
folders["fonts"] = os.path.join(folders["assets"], "fonts")
folders["json"] = os.path.join(folders["assets"], "json")
folders["maps"] = os.path.join(folders["assets"], "maps")

# Fonts ------------------------------------------------------------------------
fonts = {}

fonts["default_size"] = 22  # default size of the pixel font (11 or 22)
fonts["font_name"] = os.path.join(folders["fonts"], "RetroGaming.ttf")
fonts["default_antialiazed"] = False
fonts["default_color"] = (0, 0, 0)


# Images -----------------------------------------------------------------------
images = {
    "EmptyBlock": os.path.join(folders["images"], "EmptyBlock.png"),
    "GeneratorBlock": os.path.join(folders["images"], "GeneratorBlock.png"),
    "ModifierBlock": os.path.join(folders["images"], "ModifierBlock.png"),
    "ReceptorBlock": os.path.join(folders["images"], "ReceptorBlock.png"),
    "TransporterBlock": os.path.join(folders["images"], "TransporterBlock.png"),
    "Arrow": os.path.join(folders["images"], "Arrow.png"),
    "Tile": os.path.join(folders["images"], "Tile.png"),
}
