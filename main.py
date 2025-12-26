from pass_chkr import pss_strng_chckr
from port_scanner import port_scanner


def main_menu():
	print("Welcome to my first formal Python Project!")
	print("Choose your tool")
	print("1. Password Strength Checker")
	print("2. Log File Analyzer")
	print("3. Port Scanner (Simulated)")
	print("4. File Integrity Checker")
	print("5. Brute Force Simulator")
	print("6. System Info Tool")
	print("7. Exit")

	while True:
		choice = input("Enter your choice (1-7): ")
		if choice == "1":
			pss_strng_chckr()
		elif choice == "2":
			log_file_anlyzr()
		elif choice == "3":
			port_scanner()
		elif choice == "4":
			file_integ_chkr()
		elif choice == "5":
			brute_force_sim()
		elif choice == "6":
			sys_info_tool()
		elif choice == "7":
			print("Goodbye!")
			break
		else:
			print("Invalid input, try again.")

if __name__ == "__main__":
	main_menu()

