import os
import json

picroll_path = os.path.join(os.getcwd(), '+James/Code_Projects/DigiverseDownloads/+digiversedownloads(github)/Slideshow/PicRoll')

output_path = os.path.join(os.getcwd(), '+James/Code_Projects/DigiverseDownloads/+digiversedownloads(github)/Slideshow/PicRoll/images.json')

extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
images = []

for filename in sorted(os.listdir(picroll_path)):
    if filename.lower().endswith(extensions):
        images.append("PicRoll/" + filename)

with open(output_path, "w") as f:
    json.dump(images, f, indent=4)

print(f"Found {len(images)} images. Written to images.json!")
for img in images:
    print(" ", img)