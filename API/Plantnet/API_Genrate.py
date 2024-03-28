import requests
import os
import json
import dotenv
import urllib.request
import dotenv


dotenv=dotenv.load_dotenv()


def image_generate(txtimg):

        url="https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
        Fal_API_KEY=os.getenv("Fal_API_KEY")

        headers = {
            "Authorization": Fal_API_KEY,
            "Content-Type": "application/json"
        }
        payload={
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        "prompt": f"(masterpiece:1.4), (best quality), (detailed),{txtimg}",
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t",

        }

        response = requests.post(url, json=payload, headers=headers)
        data = json.loads(response.text)
        result=str(data["image"]['url'])
        with open('flower/image.jpg', 'wb') as f:
            img=f.write(requests.get(str(data["image"]['url'])).content)
        
        return result


def Plant():
        url = "https://my-api.plantnet.org/v2/identify/all"
        PlantNet_API_KEY=os.getenv("PlantNet_API_KEY")

        headers = {

        }
        payload = {
            "api-key":PlantNet_API_KEY
        }
        files={
            "images" : open("flower/image.jpg","rb")
        }
        response = requests.post(url, params=payload, headers=headers, files=files)
        data = json.loads(response.text)
        plant_name=str(data['bestMatch'])


        print(response.status_code)
        return plant_name



text2img=image_generate("red flower with yello plant")
plant_name=Plant()
print(plant_name)



