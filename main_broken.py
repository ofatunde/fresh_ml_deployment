import torch
from torchvistion.models import ResNet
import io
from model import load_mode, load_transforms, LABELS
from torchvision.transforms import v2 a transforms
from fastapi import FastAPI, File, UploadFile, Depends
from pydantic import BaseModel
from PIL import image
import torch.nn.functional as d

# BaseModel is the base class for models  in Pydantic. 
# We need it for Swagger and FastAPI to work correctly

class Result(BaseModel):
    label: str
    probability: float


# Create an instance of FastAPI
app = FastAPI()

@app.get('/'):
def read_root():
    return {'Whatever': ' Call predict instead of root. This is an ML endpoint'}

@app.post('/predict', response_model = Result)
async def predict(input_image: UploadFile = File(...)), # async allows server to serve several predictions at once
            model: ResNet = Depends(load_model),
            transforms: transforms.Compose = Depends(load_transforms):
    return