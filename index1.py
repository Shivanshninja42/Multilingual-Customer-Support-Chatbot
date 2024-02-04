import os
import openai
import requests
from PIL import Image
from urllib.parse import urlparse

openai.api_key = ""

os.environ['OPENAI_API_KEY'] = ""

openai.api_base = 'https://api.openai.com/v1'
openai.api_version = '2020-10-01'

use_azure_active_directory = False

if not use_azure_active_directory:
    openai.api_type = 'open_ai'
    openai.api_key = os.environ["OPENAI_API_KEY"]


inside=input("enter which kind of image you want")

from azure.identity import DefaultAzureCredential

if use_azure_active_directory:
    default_credential = DefaultAzureCredential()
    token = default_credential.get_token("https://cognitiveservices.azure.com/.default")

    openai.api_type = 'open_ai'
    openai.api_key = token.token

import typing
import time
import requests

if typing.TYPE_CHECKING:
    from azure.core.credentials import TokenCredential

class TokenRefresh(requests.auth.AuthBase):

    def __init__(self, credential: "TokenCredential", scopes: typing.List[str]) -> None:
        self.credential = credential
        self.scopes = scopes
        self.cached_token: typing.Optional[str] = None

    def __call__(self, req):
        if not self.cached_token or self.cached_token.expires_on - time.time() < 300:
            self.cached_token = self.credential.get_token(*self.scopes)
        req.headers["Authorization"] = f"Bearer {self.cached_token.token}"
        return req

if use_azure_active_directory:
    session = requests.Session()
    session.auth = TokenRefresh(default_credential, ["https://cognitiveservices.azure.com/.default"])

    openai.requestssession = session


generation_response = openai.Image.create(
    prompt=inside,
    size='1024x1024',
    n=1
)

print(generation_response)

import os
import requests


image_dir = os.path.join(os.curdir, 'images')



if not os.path.isdir(image_dir):
    os.mkdir(image_dir)


image_path = os.path.join(image_dir, 'generated_image.png')

image_url = generation_response["data"][0]["url"] 
generated_image = requests.get(image_url).content  
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

img = Image.open(image_path)
img.show()