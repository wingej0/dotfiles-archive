import json

# Gets colors from pywal wallpaper
def get_colors():
    with open('/home/wingej0/.cache/qtile/colors.json') as f:
        colors = json.load(f)
    
    return colors['colors']

colors = get_colors()
