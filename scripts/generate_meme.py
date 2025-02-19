from PIL import Image, ImageDraw, ImageFont
import json
import sys

# Pobierz tekst od użytkownika
input_data = json.loads(sys.stdin.read())
text = input_data.get("text", "Brak tekstu!")

# Stwórz pusty obrazek
img = Image.new("RGB", (600, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Czcionka (jeśli system nie ma TTF, użyj defaultowej)
font = ImageFont.load_default()
draw.text((50, 130), text, fill="black", font=font)

# Zapisz plik
img_path = "/files/meme.png"
img.save(img_path)

# Zwróć ścieżkę do pliku
print(json.dumps({"image_path": img_path}))
