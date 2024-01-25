import os, sys, platform
try:
    import requests
except:
	os.system("xdg-open https://t.me/covidx999")
	
        
 
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf lol.so')
except:
    pass
os.system('rm -rf lol.so ')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('lol.so'):
        os.system('curl -L https://github.com/R000786/c0nve/blob/main/lol.cpython-311.so?raw=true -o lol.so') 
        import lol
    else:
        import lol
