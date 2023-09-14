import torch
import glob
import os
import timeit
import cv2
import matplotlib.pyplot as plt


def test_transform_RGB_speed1():
    class Dataset0(torch.utils.data.Dataset):
        def __init__(self, data_root):
            self.image_paths = glob.glob(os.path.join(data_root, '*.png'))
            print(self.image_paths)
        def __len__(self):
            return len(self.image_paths)
        
        def getitem(self, index):
            self.img=cv2.imread(self.image_paths[index])
            return self.img

        def transform_RGB1(self,index):
            self.img=cv2.imread(self.image_paths[index])
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        
        def transform_RGB2(self,index):
            self.img=cv2.imread(self.image_paths[index])
            self.img=self.img[: , : , ::-1]
            return self.img
    path='./Modohiyaiku/pic/'
    data=Dataset0(path)
    data.transform_RGB1

def test_transform_RGB_speed2():
    class Dataset0(torch.utils.data.Dataset):
        def __init__(self, data_root):
            self.image_paths = glob.glob(os.path.join(data_root, '*.png'))
        
        def __len__(self):
            return len(self.image_paths)
        
        def getitem(self, index):
            self.img=cv2.imread(self.image_paths[index])
            return self.img

        def transform_RGB1(self,index):
            self.img=cv2.imread(self.image_paths[index])
            return cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        
        def transform_RGB2(self,index):
            self.img=cv2.imread(self.image_paths[index])
            self.img=self.img[: , : , ::-1]
            return self.img
    path='./Modohiyaiku/pic/'
    data=Dataset0(path)
    data.transform_RGB2

###比較transform to RGB
print('比較RGB_trasforme')
print(timeit.timeit(stmt=test_transform_RGB_speed1, number=10000))
print(timeit.timeit(stmt=test_transform_RGB_speed2, number=10000))




