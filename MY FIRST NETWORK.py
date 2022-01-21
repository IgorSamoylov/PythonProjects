import torch
import torch.nn as nn
import torch.nn.functional as F

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class Network1(nn.Module):
    def __init__(self):
        super(Network1, self).__init__()
        
        
        self.layer1 = nn.Linear(8, 32)
            
        self.layer2 = nn.Linear(32, 64)
            
        self.layer3 = nn.Linear(64, 8)
            
       
    def forward(self, tensor):
        tensor = F.relu(self.layer1(tensor))
        tensor = F.relu(self.layer2(tensor))
        tensor = self.layer3(tensor)
        return tensor

network1 = Network1().to(device)
print(network1)

for epoch in range(5):
    data = torch.rand(8)
    data.to(device)
    print(data)

    output = network1(data)
    print(output)


