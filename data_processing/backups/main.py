from image_processing import *
from sound_processing import *

ans=True
while ans:
    print ("""
    1.Encode an image
    2.Decode an image
    3.Convert an image into a .wav file
    4.Decode a .wav file
    E: exit
    """)
    ans = input("What would you like to do?: ") 
    if ans=="1":
      file_path = input("File to encode: ")
      text_to_encode = input("Text to hide: ")
      new_file_name = input("Name of the new file: ")
      encodeImage(file_path,new_file_name,text_to_encode)
    elif ans=="2":
      file_path = input("File to decode: ")
      print(decodeImage(file_path))
    elif ans=="3":
        image_path = input("File to convert: ")
        new_file_name = input("Name of the new file: ")
        createWavImage(image_path,new_file_name)
    elif ans=="4":
        audio_path = input("File to decode: ")
        print(readData(audio_path))
    elif ans=="E":
      sys.exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 
