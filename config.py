import os
import platform

class Config:
    PROJECT_NAME = "VAULT"
    AUTHOR = "Ahmed Osama"
    VERSION = "1.0.0"
    
    BASE_DIR = os.getcwd()
    VAULT_DIR = os.path.join(BASE_DIR, "secure_vault")
    KEY_FILE = "vault.key"
    LOG_FILE = ".vault_log.txt" 
    
    if platform.system() != "Windows":
        raise OSError("This system is designed for Windows architecture only.")
        
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)
