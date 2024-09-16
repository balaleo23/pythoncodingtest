
import qrcode

Data = input("Enter the text or URL: ").strip()
file_name = input("Enter the file_Name with extension : ").strip()

qr = qrcode.QRCode(
    box_size=10,
    border=4,
)

qr.add_data(Data)
image = qr.make_image(fill_color ='black', back_color= 'white')
image.save(file_name)
print(f'QR Code Saved as {file_name}')



