from PIL import Image, ImageDraw
import qrcode

# QR-Code Creator
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,
    border=4
)
qr.add_data("https://www.YourURLgoesHere.com/example/") # URL to link
qr.make(fit=True)

# RGB Colors
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

logo = Image.open("YourImageGoesHere").convert("RGBA")  

# 1 third of QR size
qr_width, qr_height = img.size
logo_size = qr_width // 3  # 33% of QR width
logo = logo.resize((logo_size, logo_size))

# white frame
background_size = int(logo_size * 1.4)  # 40% bigger than Logo
background = Image.new("RGBA", (background_size, background_size), "white")

# white circle
mask = Image.new("L", (background_size, background_size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, background_size, background_size), fill=255)

# placing logo
bg_x = (background_size - logo_size) // 2
bg_y = (background_size - logo_size) // 2
background.paste(logo, (bg_x, bg_y), mask=logo)

# Center Logo
pos = ((qr_width - background_size) // 2, (qr_height - background_size) // 2)

# Pasting Logo
img.paste(background, pos, mask=mask)

# Save
img.save("qrcode.png")
