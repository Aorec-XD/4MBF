import os

cookie=input('INPUT COOKIE :')
token=input('INPUT TOKEN : ')
open('.cookie.txt','w').write(cookie)
open('.token.txt','w').write(token)
os.system('python 4MBF.py')
