import torch
import torch.nn as nn 



class Model(nn.Module):
    def __init__(self,in_features) -> None:
        super().__init__()
        self.layer0 = nn.Linear(in_features,8)
        self.act0 = nn.ReLU()
        
        self.layer1 = nn.Linear(8,16)
        self.act1 = nn.ReLU()
        
        self.layer2 = nn.Linear(16,32)
        self.act2 = nn.ReLU()
        
        self.out = nn.Linear(32,10)
        
        self.dropout = nn.Dropout(p=0.3)
        
    def forward(self,x):
        x1 = self.act0(self.layer0(x))
        x2 = self.act1(self.layer1(x1))
        x3 = self.act2(self.layer2(x2))
        out = self.dropout(self.out(x3))
        return out