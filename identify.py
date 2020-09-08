import face_recognition
from PIL import Image, ImageDraw
 
 
 
image_of_elon = face_recognition.load_image_file('./img/known/ElonMusk.jpg')

#first item
elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

image_of_jeff = face_recognition.load_image_file('./img/known/JeffBezos.jpg')

#first item
jeff_face_encoding = face_recognition.face_encodings(image_of_jeff)[0]

#Make array of encodings and names
known_face_encodings = [
    elon_face_encoding,
    jeff_face_encoding
]

known_face_names = [
    "Elon Musk",
    "Jeff Bezos"
]

#Load test image to find the faces in
test_image = face_recognition.load_image_file('./img/groups/elon-jeff.jpg')

#find the faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#convert to the PIL format
pil_image = Image.fromarray(test_image)

#Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

#Loop through the faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    #Test for match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    #Draw the box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    #Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

#Display the image
pil_image.show()

#save the image
pil_image.save('identify.jpg')