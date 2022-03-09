import torch 
import numpy as np

def train(model, train_loader, valid_loader, epochs, lr , path_save, bs, usecuda):
    criterio = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    if usecuda:
        model = model.cuda()
    for epoch in range(epochs):
        train_loss = 0.0
        for video,label in train_loader:
            if usecuda:
                video=video.cuda()
                label = label.cuda()
            print(video.shape)
            optimizer.zero_grad()
            output = model(video)
            loss = criterio(output,label)
            loss.backward()
            optimizer.step()
            #video = ""
            #label = ""
            #print(loss.item())
            #train_loss = train_loss + loss.item()


