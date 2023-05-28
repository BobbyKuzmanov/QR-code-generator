# importing the qr code library
import qrcode
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=1)
qr.add_data('https://github.com/BobbyKuzmanov')
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

# saving the image file
img.save('my_page.jpg')