#=============================================================================================================#
#                                                DeepOne/model                                                #
#                                                 Author: Yi                                                  #
#                                             dataset: miniimagenet                                           #
#                                               date: 19, Oct 27                                              #
#=============================================================================================================#

#packages
import torch.nn as nn

#model
def conv_block(in_channels, out_channels):
	bn = nn.BatchNorm2d(out_channels)
	nn.init.uniform_(bn.weight)
	return nn.Sequential(
		nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
		bn,
		nn.ReLU(),
		nn.MaxPool2d(2))

class ProtoNet(nn.Module):
	'''
	protonet architecture
	'''
	def __init__(self, x_dim=3, hid_dim=64, z_dim=64):
		super(ProtoNet, self).__self__()
		self.encoder = nn.Sequential(
			conv_block(x_dim, hid_dim),
			conv_block(hid_dim, hid_dim),
			conv_block(hid_dim, hid_dim),
			conv_block(hid_dim, z_dim))
		self.out_channels = 1600

	def forward(self, x):
		x = self.encoder(x)
		return x.view(x.size(0), -1)