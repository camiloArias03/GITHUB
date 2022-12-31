import qrcode

# Crea el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Añade el contenido del QR
qr.add_data('Hola mundo!')

# Genera el QR
qr.make(fit=True)

# Crea una imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo
img.save("qr.png")

img = qr.make_image(fill_color="black", back_color="white", image_format="image/jpeg")
img.save("qr.jpg")

