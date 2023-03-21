import qrcode
from PIL import Image

color_names = ["red", "blue", "green", "black", "orange", "purple", "grey", "brown", "pink", "yellow", "white"]

choice = input("Press 1 for black & white QR code\nPress 2 for different colored QR code\n: ")

# Condition for wrong input
if choice != "1" and choice != "2":
    print("Invalid Input")
    exit()

url = input("Enter the URL : ")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)

qr.add_data(url)

qr.make(fit=True)

imgName = input("Enter the generated image name without format name. i.e youtube\n: ")


# Handling user choice
if choice == "1":
    image = qr.make_image(fillColor="black", back_color="white")

elif choice == "2":
    fillingColor = input("Enter filling color like red, blue, black etc.\n: ").lower()
    backColor = input("Enter background color like red, blue, black etc.\n: ").lower()
    
    if fillingColor in color_names and backColor in color_names:
        image = qr.make_image(fill_color=fillingColor, back_color=backColor)
    else:
        print("Making default colored QR")
        image = qr.make_image(fillColor="black", back_color="white")


image.save(f"{imgName}.png")
print("QR Code image successfully generated!!!")
