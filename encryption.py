text = """  
_____  __  __   _____   ______                                   _            _____                            _                      
 |_   _||  \/  | / ____| |  ____|                                 | |          |  __ \                          | |                     
   | |  | \  / || |  __  | |__    _ __    ___  _ __  _   _  _ __  | |_  ______ | |  | |  ___   ___  _ __  _   _ | |_  _ __    ___  _ __ 
   | |  | |\/| || | |_ | |  __|  | '_ \  / __|| '__|| | | || '_ \ | __||______|| |  | | / _ \ / __|| '__|| | | || __|| '_ \  / _ \| '__|
  _| |_ | |  | || |__| | | |____ | | | || (__ | |   | |_| || |_) || |_         | |__| ||  __/| (__ | |   | |_| || |_ | |_) ||  __/| |   
 |_____||_|  |_| \_____| |______||_| |_| \___||_|    \__, || .__/  \__|        |_____/  \___| \___||_|    \__, | \__|| .__/  \___||_|   
                                                      __/ || |                                             __/ |     | |                
                                                     |___/ |_|                                            |___/      |_|                
"""
print(text)
img = input("Enter the path of image: ")
key = int(input("Enter the Key: "))

# Encryption
def encryption(): 
    with open(img, "rb") as file:
        meta = file.read()
        data = bytearray(meta)

    for index, values in enumerate(data):
            data[index] = values ^ key

    with open(img, "wb") as image:
        image.write(data)

    print(f"The path entered is: {img}")
    print(f"The key entered is: {key}")
    print("The Encryption is Done!")


# Decryption
def decryption():
    with open(img, "rb") as file:
        meta = file.read()
        data = bytearray(meta)

    for index, values in enumerate(data):
            data[index] = values ^ key

    with open(img, "wb") as image:
        image.write(data)

    print(f"The path entered is: {img}")
    print(f"The key entered is: {key}")
    print("The Decryption is Done!")

response = input("Enter your choice:\n 1 for encryption \n 2 for decryption \n")
if response == '1':
     encryption()
elif response == "2":
     decryption()