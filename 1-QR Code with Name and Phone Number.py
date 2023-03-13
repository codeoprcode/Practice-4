import qrcode

print("Get your QR Code")

name = input("Please enter your name: ")
phone_number = input("Please enter your phone number: ")

img = qrcode.make(name + phone_number)

img.save("qrcode.png")

