import torch
import pandas as pd
import torchvision
from pytorchvideo.data.encoded_video import EncodedVideo
from torchvision.transforms._transforms_video import (
    CenterCropVideo,
    NormalizeVideo,
)
from pytorchvideo.transforms import (
    ApplyTransformToKey,
    ShortSideScale,
    UniformTemporalSubsample
)

class load_dataset():
    def __init__(self,path="dataset/train/" , meta_name = "metadata_train.csv"):
        self.meta = pd.read_csv(path + meta_name)
        self.path=path
        self.transform =  ApplyTransformToKey(
            key="video",
            transform=torchvision.transforms.Compose(
                [
                    UniformTemporalSubsample(10),
                    torchvision.transforms.Lambda(lambda x: x/255.0),
                    NormalizeVideo([0.45, 0.45, 0.45], [0.225, 0.225, 0.225]),
                    ShortSideScale(size=200),
                    CenterCropVideo(crop_size=(200, 200))
                ]
            ),
        )
        
    def __len__(self):
        return len(self.meta)
    
    def __getitem__(self,idx):
        return self.transform(EncodedVideo.from_path(self.path+self.meta.iloc[idx]['video_name']+'.avi').get_clip(start_sec=0, end_sec=1000))["video"] , torch.tensor(self.meta.iloc[idx]["labels"])