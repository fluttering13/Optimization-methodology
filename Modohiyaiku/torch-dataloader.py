import torch
import glob
import os
import timeit
import cv2
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

class Dataset0(torch.utils.data.Dataset):
    def __init__(self, data_root):
        self.image_paths = glob.glob(os.path.join(data_root, '*.png'))
    def __len__(self):
        return len(self.image_paths)
    
    def get_item(self, index):
        self.img=cv2.imread(self.image_paths[index])
        return self.img
    
    def get_time_times(self,index,times):
        self.imgs=[]
        [self.imgs.append(cv2.imread(self.image_paths[index])) for _ in range(times)]
        return self.imgs

        
# def test1():
path='./Modohiyaiku/pic/'
data=Dataset0(path)
all_data=data.get_time_times(0,100)

def test1():
    loader = list(DataLoader(all_data, batch_size=10))

def test2():
    loader = list(DataLoader(all_data, batch_size=10, pin_memory=True))


###note that it can't be used in Windows for the feature of num_workers
# def test3():
#     loader = list(DataLoader(all_data, batch_size=10, num_workers=4))    





print(timeit.timeit(stmt=test1, number=1000))
print(timeit.timeit(stmt=test2, number=1000))
# print(timeit.timeit(stmt=test3, number=1000))
