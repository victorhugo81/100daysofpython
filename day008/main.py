# ======================
# Project Name: Day 8 - Caesar Cipher Encoder & Decoder
# Section: Beginner Python Projects
# Description: Python Function Parameters & Basic Encryption
# ======================

from art import LOGO

# Display the game logo at the start
print(LOGO)

# List of all lowercase alphabet letters used for shifting characters
alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def plain2cipher(original_text, shift_amount, encode_or_decoder):
    """Encodes or decodes a message using the Caesar Cipher technique."""
    output_text = ""
    selected_encode_or_decoder = ""

    # If decoding (2), reverse the shift direction by making it negative
    if encode_or_decoder == "2":                      
        selected_encode_or_decoder = "decode"        
        shift_amount *= -1
    else:
        selected_encode_or_decoder = "encode"       

    for letter in original_text:
        # If the character isn't a letter (e.g. space, punctuation), keep it as-is
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the new position by shifting, then wrap around using modulo
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print("****************************************************************")
    print(f"Here is your secret message {selected_encode_or_decoder}d result: {output_text}")
    print("****************************************************************")

def caesar_cipher():
    """Main loop that drives the Caesar Cipher program."""
    should_continue = True

    while should_continue:
        # Keep asking until the user enters a valid direction
        while True:
            # Get the user's choice of encoding or decoding
            direction = input("Type '1' to encode, type '2' to decode: ")
            if direction == "1" or direction == "2": 
                break                               
            print("Invalid input. Please type '1' to encode or '2' to decode.")
            print("****************************************************************")

        # Get the message to encode or decode
        text = input("Type your message: ").lower()

        # Get the shift amount (how many positions to shift each letter)
        shift = int(input("Type the shift number: "))

        # Run the cipher with the provided inputs
        plain2cipher(original_text=text, shift_amount=shift, encode_or_decoder=direction)

        # Ask the user if they want to run the cipher again
        restart = input("Type 'y' if you want to go again. Otherwise, type 'n': ").lower()

        # Exit the loop if the user chooses not to continue
        if restart == "n":
            should_continue = False
            print("Goodbye")

# Entry point - start the Caesar Cipher program
caesar_cipher()