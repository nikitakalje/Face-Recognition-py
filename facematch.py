import face_recognition

image_of_elon = face_recognition.load_image_file('./img/known/ElonMusk.jpg')

#first item
elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0] # pylint: disable=maybe-no-member

unknown_image = face_recognition.load_image_file('./img/unknown/jeff1.jpg') # pylint: disable=maybe-no-member
#first item
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0] # pylint: disable=maybe-no-member

#compare faces
results = face_recognition.compare_faces([elon_face_encoding], unknown_face_encoding) # pylint: disable=maybe-no-member

if results[0]:
    print('This is Elon Musk!')

else:
    print('This is NOT Elon Musk.')

