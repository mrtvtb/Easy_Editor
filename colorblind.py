from PIL import Image
def correct_for_protanopia(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            r = int(r * 0.6)
            r = min(max(r, 0), 255)
            pixels[i, j] = (r, g, b)

    return img

def correct_for_protanomaly(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            r = int(r * 0.8)
            r = min(max(r, 0), 255)
            pixels[i, j] = (r, g, b)

    return img

def correct_for_deuteranopia(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            avg = (r + b) // 2 
            g = avg  
            g = min(max(g, 0), 255)
            pixels[i, j] = (r, g, b)

    return img


def correct_for_deuteranomaly(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            g = int(g * 0.8)
            g = min(max(g, 0), 255)
            pixels[i, j] = (r, g, b)

    return img

def correct_for_tritanopia(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            avg = (r + g) // 2  
            b = avg  
            b = min(max(b, 0), 255)
            pixels[i, j] = (r, g, b)

    return img

def correct_for_tritanomaly(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            b = int(b * 1.3)  
            b = min(max(b, 0), 255)
            pixels[i, j] = (r, g, b)

    return img

