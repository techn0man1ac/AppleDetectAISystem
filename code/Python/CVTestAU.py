# Example: reuse your existing OpenAI setup
from openai import OpenAI
import base64

import pygame 
import pygame.camera 

import serial
import time

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# initializing  the camera 
pygame.camera.init() 
import serial

ser = serial.Serial('COM10', baudrate=115200)

for cycles in range(100):
    # make the list of all available cameras 
    camlist = [0, 2]
    
    # if camera is detected or not 
    if camlist: 
    
        # initializing the cam variable with default camera 
        cam = pygame.camera.Camera(camlist[0], (640, 480)) 
    
        # opening the camera 
        cam.start() 
    
        # capturing the single image 
        image = cam.get_image() 
    
        # saving the image 
        pygame.image.save(image, "filename.jpg") 
    
    # if camera is not detected the moving to else part 
    else: 
        print("No camera on current device")

    # Path to the image file you want to process
    image_path = "filename.jpg"

    # Encode the image to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')


    completion = client.chat.completions.create(
        model="minicpm-v-2_6",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Is there a apple in the image? Please use only \"Yes\" or \"No\" to answer."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
        max_tokens=30,
        temperature=0.1,
    )

    responce = completion.choices[0].message.content
    print(responce)
    responceString = str(responce[0]).lower().strip()

    if(responceString in "y"):
        print("responce == Yes")
        ser.write(b'1')

    if(responceString in "n"):
        print("responce == No")
        ser.write(b'0')

    #time.sleep(1)
ser.close()
