import sys
sys.path.append("src/")
import torch
from dataset import load_dataset
from model import Resnet3D
from train import train

usecuda= True
## Se crea instancia de carga de videos
train_dataset = load_dataset()
train_loader = torch.utils.data.DataLoader(train_dataset,batch_size=2, shuffle=True)

#se instancia el modelo
model = Resnet3D()


train(model, train_loader, train_loader,100, 1e-3, "./", 3, True)