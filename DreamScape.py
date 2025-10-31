import os
import sys
import time
import math
import random
from itertools import cycle

try:
    from colorama import init, Fore, Back, Style
except ImportError:
    print("Installing required library...")
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style

init(autoreset=True)

# Color palettes for different moods/themes
PALETTES = {
    "ocean": [Fore.CYAN, Fore.BLUE, Fore.WHITE],
    "fire": [Fore.RED, Fore.YELLOW, Fore.MAGENTA],
    "forest": [Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.YELLOW],
    "cyber": [Fore.MAGENTA, Fore.CYAN, Fore.LIGHTBLACK_EX],
    "dream": [Fore.WHITE, Fore.LIGHTMAGENTA_EX, Fore.LIGHTBLUE_EX]
}

CHARS = " .:-=+*#%@"
WIDTH, HEIGHT = 80, 24

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def perlin_noise(x, y, seed):
    random.seed(int(x * 92821 + y * 68917 + seed * 31))
    return random.random()

def generate_frame(theme, t, seed):
    palette = PALETTES.get(theme, PALETTES["dream"])
    lines = []
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            nx, ny = x / WIDTH - 0.5, y / HEIGHT - 0.5
            v = (
                math.sin(nx * 8 + t)
                + math.cos(ny * 6 - t * 0.7)
                + perlin_noise(x, y, seed)
            ) / 3
            idx = int((v + 1) / 2 * (len(CHARS) - 1))
            color = random.choice(palette)
            line += color + CHARS[idx]
        lines.append(line)
    return "\n".join(lines)

def animate_scene(theme):
    seed = random.randint(0, 99999)
    colors = cycle(PALETTES.get(theme, PALETTES["dream"]))
    t = 0.0
    try:
        while True:
            clear()
            color = next(colors)
            print(Style.BRIGHT + color + f"\n💭 Dreamscape — Theme: {theme}\n")
            frame = generate_frame(theme, t, seed)
            print(frame)
            t += 0.2
            time.sleep(0.08)
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n✨ Dream ended. Goodbye.\n")

def main():
    clear()
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "🌙 Welcome to DreamScape — ASCII Visual Generator\n")
    print("Themes:", ", ".join(PALETTES.keys()))
    theme = input("\nChoose your dream theme 🌈: ").strip().lower()
    if theme not in PALETTES:
        theme = "dream"
    print(Fore.YELLOW + "\nPress Ctrl+C to exit the dream anytime.\n")
    time.sleep(2)
    animate_scene(theme)

if __name__ == "__main__":
    main()
