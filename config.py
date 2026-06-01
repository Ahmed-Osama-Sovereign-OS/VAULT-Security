import os
import platform

class Config:
    PROJECT_NAME = "VAULT"
    AUTHOR = "Ahmed Osama"
    VERSION = "1.0.0"
    
    # مسارات النظام (يعمل على ويندوز حصراً)
    BASE_DIR = os.getcwd()
    VAULT_DIR = os.path.join(BASE_DIR, "secure_vault")
    
    # إعدادات التشفير (معيار AES-256)
    KEY_FILE = "vault.key"
    
    # التحقق من أن الجهاز ويندوز
    if platform.system() != "Windows":
        raise OSError("This system is designed for Windows architecture only.")
        
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)
