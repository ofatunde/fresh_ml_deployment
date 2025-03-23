import os
import wandb
from loadotenv import load_env

load_env()

wandb_org = os.getenv('WANDB_ORG')

# This will give an error if the key is not set
assert 'WANDB_API_KEY' in os.environ, 'Please enter the WandB API key'

# This will work if we have WANDB_API_KEY set
wandb.login()
print(wandb_org)

wandb_org = os.getenv('WANDB_ORG')
wandb_project = os.getenv('WANDB_PROJECT')
wandb_model_name = os.getenv('WANDB_MODEL_NAME')
wandb_model_version = os.getenv('WANDB_MODEL_VERSION')

artifact_path = f'{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}'

artifact = wandb.Api().artifact(artifact_path,type = 'model')

MODELS_DIR = 'models'
LABELS = ["freshapple", "freshbanana", "freshorange",
"rottenapple", "rottenbanana", "rottenorange"]

MODEL_FILE_NAME = 'best_model.pth'

os.makedirs(MODELS_DIR, exist_ok = True)


artifact.download(root=MODELS_DIR)

# def download_artifact():
#    wandb.login()

# Returns the model architecture with random weights
def get_raw_model() -> ResNet:
    architecture = resnet18(weights = None)
    architecture.fc = nn.Sequential(
        nn.Linear(512,512),
        nn.ReLu(),
        nn.Linear(512,6)
    )

    return architecture

# Returns the model with the weights from the WandB artifact
def load_model() -> ResNet:
    download_artifact()
    model = get_raw_model()
    # load the model state (weights, layers, names)
    model_state_dict_path = Path(MODELS_DIR) / 'model.pth'
    model.load_state_dict(model_state_dict, strict = True) # to avoid weird errors
    model.eval() # avoids batch normalization and dropout
    return model

def load_transforms() -> transforms.Compose:
    return torchvision.transforms.Compose(
        [tranforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize


        ]
    )