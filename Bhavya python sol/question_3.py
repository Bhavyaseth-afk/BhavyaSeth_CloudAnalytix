from PIL import  Image
import imageio
import matplotlib.pyplot as plt
import requests

url = input()

r = requests.get(url)
with open("img.jpg", "wb") as f:
    f.write(r.content)



pic = imageio.imread("D:\Downloads\Bhavya python sol\img.jpg")
plt.figure(figsize = (5,5))
plt.imshow(pic)


print('Type of the image : ' , type(pic)) 
print('Shape of the image : {}'.format(pic.shape)) 
print('Image Hight {}'.format(pic.shape[0])) 
print('Image Width {}'.format(pic.shape[1])) 
print('Dimension of Image {}'.format(pic.ndim))