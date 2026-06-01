import os
from config import Config
from logger import log_action

class Shredder:
    @staticmethod
    def secure_delete(file_path, passes=3):
        if not os.path.exists(file_path):
            return

        file_size = os.path.getsize(file_path)
        with open(file_path, "ba+", buffering=0) as f:
            for _ in range(passes):
                f.seek(0)
                f.write(os.urandom(file_size))
        
        os.remove(file_path)
        log_action("SHRED", f"File permanently destroyed: {file_path}")
