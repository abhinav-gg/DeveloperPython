import ascii_art

# This project is a simple ASCII art generator.
# The main code is in the ascii_art.py file.
# It is very complicated though, so just use the interface below.

# To get get an image, use 'image = ascii_art.get_image()'
# To convert an image to ascii art, use 'ascii = ascii_art.convert(image)'
# To display an ascii art image, use 'ascii_art.display(ascii)

# Challenge 3: Change the link to https://smartcdn.gprod.postmedia.digital/theprovince/wp-content/uploads/2015/11/astley.jpg?quality=90&strip=all&w=1128&h=846&type=webp&sig=4XdRb19ieybMbo1MaMqXiA
LINK = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQngA3sDiSoA46Dy56OLZjLKD1SqgsS3Qmh1A&usqp=CAU"

image = ascii_art.get_image(link=LINK)

# Challenge 2: Increase the size of the image to 100 so it can be seen more easily
ascii = ascii_art.convert(image, size=20)

# Challenge 1: Use the display function to display the ascii art
print(ascii)