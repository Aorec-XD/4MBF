import os
os.system('git pull')
try:os.system('mkdir /sdcard/4MBF-DATA')
except:pass
try:os.system('mkdir /sdcard/4MBF-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/4MBF-DATA/CP')
except:pass
try:os.system('touch .prox.txt')
except:pass
if __name__ == "__main__":
        try:
                __import__("aorec").login()
        except Exception as e:
                exit(str(e))
