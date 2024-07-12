from PIL import Image
import os

# Define the paths
pictures_dir = './input'
relicbase_path = 'relicbase.jpg'
ID = 1
# Open the 'relic.png' image
relic_img = Image.open(relicbase_path)

# Loop through all files in the 'Pictures' directory
for filename in os.listdir(pictures_dir):
    # Check if the file is an image
    if filename.endswith('.png') or filename.endswith('.jpg'):
        # Open the image
        img = Image.open(os.path.join(pictures_dir, filename))
        img = img.resize((235, 235), Image.Resampling.BILINEAR)

        # Calculate the coordinates to place the image at the center of 'relic.png'
        left = (relic_img.width - img.width) / 2
        top = (relic_img.height - img.height) / 2
        right = (relic_img.width + img.width) / 2
        bottom = (relic_img.height + img.height) / 2

        # Paste the image onto 'relic.png'
        relic_img.paste(img, (int(left), int(top), int(right), int(bottom)))
        relic_img.save("./output/" + str(ID) + '-relic_modified.png')
        print('Image processed:', filename)
        ID += 1
    else:
        print('File is not an image', filename)
        continue
