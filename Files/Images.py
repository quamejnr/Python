from PIL import Image, ImageEnhance

img = Image.open("img.jpg")
img_brightness_obj = ImageEnhance.Brightness(img)

enhanced_img = img_brightness_obj.enhance(0.2)

# enhanced_img.show()
# enhanced_img.save('img.jpg')
