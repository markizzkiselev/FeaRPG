from PIL import Image


def resizer(image, width, height, new_name):
    img = Image.open(image)
    new_image = img.resize((width, height))
    new_image.save(f'{new_name}.png')
    return f'{new_name}.png'
