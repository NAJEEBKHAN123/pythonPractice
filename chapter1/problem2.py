 
import os

# select the where you want from you os 
directory_path = '/MERN STACK/E-shop/E-Commerce-Dynamic-web'

# use this module to list the directory contents 
contents = os.listdir(directory_path)

# print the contents here 
for item in contents:
  print(item)