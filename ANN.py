import torch
import torch.nn as nn 



class Model(nn.Module):
    def __init__(self,in_features) -> None:
        super().__init__()
        self.layer0 = nn.Linear(in_features,16)
        self.act0 = nn.ReLU()
        
        self.layer1 = nn.Linear(16,32)
        self.act1 = nn.ReLU()
        
        self.out = nn.Linear(32,10)
        
    def forward(self,x):
        x1 = self.act0(self.layer0(x))
        x2 = self.act1(self.layer1(x1))
        out = self.out(x2)
        return out