
import numpy
import torch
import torch.nn as nn
import torch.functional as F

#numpyArray = numpy.zeros((10, 10))
#numpyArray = numpy.random.rand(3)
numpyArray = numpy.array([1., 2., 3.])
tensor = torch.from_numpy(numpyArray).type(torch.FloatTensor)

print("INPUT TENSOR: ", tensor)


class NeuroNet(nn.Module):

    def __init__(self, weights):
        super(NeuroNet, self).__init__()
        self.Layer1 = nn.Linear(3, 3)
        self.Layer1.weight = nn.Parameter(weights)
        self.Layer2 = nn.Linear(3, 2)
        self.Layer3 = nn.Linear(2, 1)

    def forward(self, tensor0):
        tensor1 = self.Layer1(tensor0)
        tensor2 = self.Layer2(tensor1)
        tensor3 = self.Layer3(tensor2)
        return  tensor1, tensor2, tensor3

weights = torch.as_tensor([[1., 2., 3.],[1., 2., 3.]])
neuroNet = NeuroNet(weights)
result = neuroNet.forward(tensor)

print ("OUTPUT TENSOR: ", result)



