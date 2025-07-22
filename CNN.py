import torch
import torch.nn as nn 

class Model(nn.Module):
    def __init__(self,in_channels):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels,16,3)
        self.pool1 = nn.MaxPool2d(2)
        
        self.conv2 = nn.Conv2d(16,32,3)
        self.pool2 = nn.MaxPool2d(2)
        
        self.flat = nn.Flatten()
        self.fc = nn.Linear(5*5*32,10)
        
        
    def forward(self,x):
        x1 = self.pool1(self.conv1(x))
        x2 = self.pool2(self.conv2(x1))
        out = self.fc(self.flat(x2))
        return out