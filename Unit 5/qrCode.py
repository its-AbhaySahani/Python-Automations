# code to generate multiple qr code
import qrcode

# List of data
data = ['https://www.google.com', 'https://www.facebook.com', 'https://www.instagram.com', 'https://www.twitter.com']

# Loop to generate qr code
for i in range(len(data)):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data[i])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr'+str(i)+'.png')
    print('QR code generated for', data[i])



