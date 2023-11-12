import json

# Gets current wallpaper from the pywal cache
def get_wallpaper():
    with open('/home/wingej0/.cache/wal/wal') as f:
        wallpaper = f.read()

    return wallpaper

# Gets colors from pywal wallpaper
def get_colors():
    with open('/home/wingej0/.cache/wal/colors.json') as f:
        colors = json.load(f)
    
    return colors['colors']

colors = get_colors()

# if __name__ == '__main__': 
#     print(colors) 