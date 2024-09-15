# QR Code Generator 
This Python project is a QR code generator that allows users to input data (like a URL) and generates a QR code image file. I started with a simple program and added several enhancements, such as a function-based structure, user-friendly messages, and a task completion notice.

## What I Learned in this Project
~ Converting Code to Functions: Improved the structure of the code by organizing it into functions for reusability and better readability.
~ Adding User-Friendly Messages: Introduced welcome, end, and task completion messages to enhance user experience.
~ Handling User Input: Improved handling for user inputs like data (URL) and file names.
~ File Extension Handling: Automatically appended the .png extension to the file name if not provided by the user.
~ Error Handling: Added checks to ensure the user provides data (e.g., URL) for QR code generation.
~ External Libraries: Gained practical experience with the qrcode and Pillow libraries for QR code generation and image handling.

## Requirements
To run this program, you need the following Python libraries:

~ qrcode[pil] (for generating QR codes)
~ Pillow (for image manipulation)

## You can install them via pip:
~ pip install qrcode[pil] Pillow

## How the Program Works
Welcome Message:
~ The program starts by displaying a welcome message to the user.

Input Collection:
~ The program asks the user to input data or a URL for the QR code.
~ It also prompts the user to input a file name to save the QR code image.

Automatic File Extension:
~ If the user doesn't provide the .png extension in the file name, the program automatically adds it.

QR Code Generation:
~ The program uses the qrcode library to generate the QR code, with high error correction.
~ The QR code has customizable fill and background colors (default: black fill, white background).

Saving the QR Code:
~ The generated QR code is saved to the file name provided by the user.
~ A success message is displayed after the QR code is saved.

End Message:
~ After the QR code is saved, the program prints a task completion message, thanking the user for using the generator.

## How to Run the Program
~ Clone the repository
~ Navigate to the project directory

~ Run the Python script

python qr.py

Follow the prompts to enter the data/URL and filename.
Example Output

### When running the program, you may see output similar to the following:
Welcome to QR Code generator
Enter the data or URL for the QR code: https://github.com/yourusername
Enter the file name to save the QR code: my_qr_code
QR code saved as my_qr_code.png
Thanks for using this QR code generator!
If you liked this, please comment on my LinkedIn account

The file my_qr_code.png will be saved in the current directory, and the program will end with a thank-you message.

