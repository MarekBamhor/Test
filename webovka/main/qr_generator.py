import qrcode

qrcd = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)


data = "https://www.youtube.com/"
qrcd.add_data(data)

qrcd.make(fit="TRUE")


qrcd_img = qrcd.make_image(fill_color="black", back_color="white")

qrcd_img.save("QRko.png")
qrcd_img.show()
