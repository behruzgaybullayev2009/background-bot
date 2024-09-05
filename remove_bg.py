import requests

import requests


def removebg(FILE_NAME):
    API_KEY ='4KTuro3qXZ4j86WuKwfSRFCm'


    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': FILE_NAME,
        'size': 'auto',
        'bg_image_url':'https://burst.shopifycdn.com/photos/city-lights-through-rain-window.jpg?width=1000&format=pjpg&exif=0&iptc=0'

    },
    headers={'X-Api-Key': API_KEY},
)
    if response.status_code == requests.codes.ok:
      
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    return rasm