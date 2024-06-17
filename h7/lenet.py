import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # First convolutional layer: input channels=1, output channels=8, kernel size=3
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        # Second convolutional layer: input channels=8, output channels=16, kernel size=3
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)
        # Fully connected layer: input size=4*4*16, output size=10
        self.fc1 = nn.Linear(4*4*16, 10)

    def forward(self, x):
        # Apply first convolution, followed by ReLU and max pooling
        x = F.relu(self.conv1(x))  # Output size: 24x24x8
        x = F.max_pool2d(x, 2)     # Output size: 12x12x8
        # Apply second convolution, followed by ReLU and max pooling
        x = F.relu(self.conv2(x))  # Output size: 12x12x16
        x = F.max_pool2d(x, 3)     # Output size: 4x4x16
        # Flatten the tensor
        x = x.view(-1, 4*4*16)     # Output size: 256
        # Apply fully connected layer
        x = self.fc1(x)            # Output size: 10
        return F.log_softmax(x, dim=1)
