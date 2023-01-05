import view
import phone_book as pb
import data_base as db


import os,sys
print('---------------------------------------------------------------------------')
filename = 'phone_book.txt'
print(os.path.abspath(filename))
print('---------------------------------------------------------------------------')
app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd() 
print(os.path.join(app_dir,filename))
print('---------------------------------------------------------------------------')
