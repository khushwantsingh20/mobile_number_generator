def generate_phone_numbers():
    # Open the file to save the phone numbers
    with open("phone_numbers.txt", "w") as file:
        # Generate all possible numbers starting with 63
        for i in range(100000000):  # Loop for 8 digits (since first two are fixed)
            # Format the number as 10 digits with leading zeros if necessary
            number = f"63{i:08}"
            # Write the number to the file
            file.write(number + "\n")

if __name__ == "__main__":
    generate_phone_numbers()
    print("Phone numbers generated and saved to phone_numbers.txt")
