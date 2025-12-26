import pyfiglet #used for large ascii text
import sys #allows deeper interal communication with host
import socket #allows communication with BSD socket API
from datetime import datetime

common_ports = {
	21: "FTP",
	22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POPv3",
        139: "NetBIOS",
        443: "HTTPS",
        445: "SMB",
        3389: "Remote Desktop Protocol"

}

def port_scanner():
	if len(sys.argv) == 2:
		target_ip = socket.gethostbyname(sys.argv[1]) #translating target domain to ip
	else:
		print("Invalid amount of arguments. Please try again.")

	#Add text to ensure the user that the ports are being scanned
	print("-" * 50)
	print("Scanning Target: " + target_ip)
	print("Scanning started at:" + str(datetime.now()))
	print("-" * 50)

	try:
		for port in common_ports:
			print(f"Checking port {port}")
			#line below: establish socket for the port using IPv4 over TCP setting it to "s"
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1) #no response? next.

			#creates the connection
			result = s.connect_ex((target_ip, port))
			if result == 0:
				print("Port {} is open".format(port))
			s.close()

	except KeyboardInterrupt:
		print("\n Exiting Program")
		sys.exit()
	except socket.gaierror:
		print("\n Hostname could not be resolved")
		sys.exit()
	except socket.error:
		print("\n Server is not responding")
		sys.exit()

if __name__ == "__main__":
	port_scanner()
