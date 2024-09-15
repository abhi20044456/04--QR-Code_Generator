import qrcode
import qrcode.constants
from PIL import Image

# Welcome message for User
print("Welcome to QR Code generator")

# Function for QR code
def generate_qr_code(data, file_name, fill_color="black", back_color="white"):

    # If user forgot to add ".png" in the file then it automatically add in file name.
    if not file_name.endswith(".png"):
        file_name += ".png"

    # if user for to enter the ulr to convert
    if data_input == "":
        print("Please enter link ")
    else:
        # Creating qrcode object
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10, border=4)
        
        # Add provided data to the QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Generate a image for the QR code with the chosen colors
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the image with given file name
        img.save(file_name)
        print(f"QR code saved as {file_name}")
        print("Thanks for using this QR code generator!")
        print("If you liked this, please comment on my LinkedIn account")

# Ask the user for the data or URL to convert in  QR code
data_input = input("Enter the data or URL for the QR code: ")

# Ask the user for file name to save the QR code
file_name_input = input("Enter the file name to save the QR code: ")

# Call the function to generate the QR code using the user input
generate_qr_code(data_input, file_name_input)
