import torch
class Resnet3D(torch.nn.Module):
    def __init__(self,out_classes=11):
        super(Resnet3D,self).__init__()
        self.Resnet = torch.hub.load('facebookresearch/pytorchvideo', 'slow_r50', pretrained=True)
        for parameter in self.Resnet.parameters():
            parameter.requires_grad= False
        self.Resnet.blocks[5].proj = torch.nn.Linear(2048,out_classes)
        self.soft= torch.nn.Softmax()
        
    def forward(self,x):
        x=self.Resnet(x)
        return self.soft(x)
        
            