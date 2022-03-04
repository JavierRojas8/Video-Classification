import sys
sys.path.append("src/")
import torch
from dataset import load_dataset
from model import Resnet3D

usecuda= True
## Se crea instancia de carga de videos
train_dataset = load_dataset()
train_loader = torch.utils.data.DataLoader(train_dataset,batch_size=1, shuffle=True)

#se instancia el modelo
model = Resnet3D()
if usecuda:
    model= model.cuda()

### se recorre el dataloader y se hace una inferencia, videos listos para entrenar el modelo    
for video, label in train_loader:
    if usecuda:
        video = video.cuda()
        label = label.cuda()
    prediction = model(video).argmax()
    print(prediction, label)