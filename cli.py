import sys
from vault import VaultManager
from shredder import Shredder
from monitor import NetworkMonitor

def run_vault():
    vault = VaultManager()
    if len(sys.argv) < 3:
        print("Usage: python cli.py [encrypt/decrypt] [filename]")
        return
    
    cmd, file = sys.argv[1], sys.argv[2]
    if cmd == "encrypt":
        vault.encrypt_file(file)
        print(f"File '{file}' locked into secure vault by Ahmed Osama.")
    elif cmd == "decrypt":
        vault.decrypt_file(file, f"decrypted_{file}")
        print("File decrypted successfully.")

def run_tools():
    if len(sys.argv) > 1 and sys.argv[1] == "shred":
        Shredder.secure_delete(sys.argv[2])
        print("File shredded permanently.")
    elif len(sys.argv) > 1 and sys.argv[1] == "monitor":
        print("Monitoring Network Connections...")
        for conn in NetworkMonitor.get_active_connections():
            print(f"Process: {conn['process_name']} | IP: {conn['remote_ip']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["encrypt", "decrypt"]:
            run_vault()
        else:
            run_tools()
    else:
        print("VAULT Security System - Ahmed Osama")
