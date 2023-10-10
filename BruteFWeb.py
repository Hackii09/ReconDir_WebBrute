#!/usr/share/python



import requests, sys, time

try:

	if len(sys.argv) != 3:

		print ""

		print "--------------------------------------------------------------"

		print "Code Por Guilherme Martins Vicente"

		print "--------------------------------------------------------------"

		print "github -> https://github.com/Hackii09"

		print "--------------------------------------------------------------"

		print "Modo de uso: python2 http://DominioDoSite.com.br Sua_Wordlist"

		print "--------------------------------------------------------------"

		print ""

	else:

		try:

			print "Testando...\n"



			wordlist = open(sys.argv[2])



			for lista in wordlist:

				req = requests.get(sys.argv[1] + "/" + lista.strip())

				req2 = requests.get(sys.argv[1] + "/" + lista.strip() + "/")

				resp = req.status_code

				resp2 = req2.status_code



				if resp == 200:

					print "Url Bem Sucedida: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				elif resp2 == 200:

					print "Url Bem Sucedida: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				if resp == 301:

					print "Url De Redirecionamento: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				elif resp2 == 301:

					print "Url De Redirecionamento: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				if resp == 401:

					print "Url Nao Existe: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				elif resp2 == 401:

					print "Url Nao Existe: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				if resp == 501:

					print "Url Erro Servidor: " + sys.argv[1] + "/" + lista.strip()

					req.close()



				elif resp2 == 501:

					print "Url Erro Servidor: " + sys.argv[1] + "/" + lista.strip()

					req.close()



		except IOError:

			print "Erro Dominio ou Wordlist Invalidos -> Corrija"

except KeyboardInterrupt:

	print "\nBye!"

