
import os
from cryptography.fernet import Fernet
from config import Config
from logger import log_action

class VaultManager:
    def __init__(self):
        self.key_path = Config.KEY_FILE
        self._load_or_create_key()
        self.cipher = Fernet(self.key)

    def _load_or_create_key(self):
        if not os.path.exists(self.key_path):
            self.key = Fernet.generate_key()
            with open(self.key_path, "wb") as f:
                f.write(self.key)
        else:
            with open(self.key_path, "rb") as f:
                self.key = f.read()

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted_data = self.cipher.encrypt(data)
        file_name = os.path.basename(file_path)
        with open(os.path.join(Config.VAULT_DIR, f"{file_name}.locked"), "wb") as f:
            f.write(encrypted_data)
        log_action("ENCRYPT", f"File locked: {file_name}")

    def decrypt_file(self, locked_file_name, output_name):
        locked_path = os.path.join(Config.VAULT_DIR, locked_file_name)
        with open(locked_path, "rb") as f:
            data = f.read()
        decrypted_data = self.cipher.decrypt(data)
        with open(output_name, "wb") as f:
            f.write(decrypted_data)
        log_action("DECRYPT", f"File unlocked: {locked_file_name}")
