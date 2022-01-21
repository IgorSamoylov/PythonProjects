import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

#img_path = 'D://dog.png'
#img_path = 'D://olga1.jpg'
img_path = 'D://olga4.jpg'

bgr_img = cv2.imread(img_path)
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

# Normalise
gray_img = gray_img.astype("float32")/255

plt.imshow(gray_img, cmap='gray')
#plt.show()


import numpy as np

filter_vals = np.array([
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1],
  [-1, -1, -1, -1, 1, 1, 1, 1]
])

print('Filter shape: ', filter_vals.shape)

# Defining the Filters
filter_1 = filter_vals
filter_2 = -filter_1
filter_3 = filter_1.T
filter_4 = -filter_3
filters = np.array([filter_1, filter_2, filter_3, filter_4])

# Check the Filters
fig = plt.figure(figsize=(10, 5))
for i in range(4):
    ax = fig.add_subplot(1, 4, i+1, xticks=[], yticks=[])
    ax.imshow(filters[i], cmap='gray')
    ax.set_title('Filter %s' % str(i+1))
    width, height = filters[i].shape
    for x in range(width):
        for y in range(height):
            ax.annotate(str(filters[i][x][y]), xy=(y,x),
                        color='white' if filters[i][x][y]<0 else 'black')


import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    
    def __init__(self, weight):
        super(Net, self).__init__()
        # initializes the weights of the convolutional layer to be the weights of the 4 defined filters
        k_height, k_width = weight.shape[2:]
        # assumes there are 4 grayscale filters
        self.conv = nn.Conv2d(1, 4, kernel_size=(k_height, k_width), bias=False)
        # initializes the weights of the convolutional layer
        self.conv.weight = nn.Parameter(weight)
        # define a pooling layer
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        # calculates the output of a convolutional layer
        # pre- and post-activation
        conv_x = self.conv(x)
        activated_x = F.relu(conv_x)
        
        # applies pooling layer
        pooled_x = self.pool(activated_x)
        
        # returns all layers
        return conv_x, activated_x, pooled_x
    
# instantiate the model and set the weights
weight = torch.from_numpy(filters).unsqueeze(1).type(torch.FloatTensor)
model = Net(weight)

# print out the layer in the network
print(model)




def viz_layer(layer, n_filters= 4):
    fig = plt.figure(figsize=(40, 40))
    
    for i in range(n_filters):
        ax = fig.add_subplot(1, n_filters, i+1)
        ax.imshow(np.squeeze(layer[0,i].data.numpy()), cmap='copper_r')
        ax.set_title(f'Output {i}')
                     
    plt.show()

fig = plt.figure(figsize=(12, 6))
fig.subplots_adjust(left=0, right=1.5, bottom=0.8, top=1, hspace=0.05, wspace=0.05)
for i in range(4):
    ax = fig.add_subplot(1, 4, i+1, xticks=[], yticks=[])
    ax.imshow(filters[i], cmap='gray')
    ax.set_title(f'Filter {i+1}')
plt.show()
    
gray_img_tensor = torch.from_numpy(gray_img).unsqueeze(0).unsqueeze(1)


(layer1, layer2, layer3) = model.forward(gray_img_tensor)

viz_layer(layer1)
viz_layer(layer2)
viz_layer(layer3)

