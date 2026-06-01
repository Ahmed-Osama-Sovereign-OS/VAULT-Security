# VAULT Security System - Official Documentation
**Author:** Ahmed Osama

## 1. Overview
VAULT is an offline-first security suite for Windows. It operates without external servers to ensure 100% privacy.

## 2. Security Protocols
- **Encryption:** Uses AES-256 (Fernet) for all file-locking operations.
- **Data Erasure:** Uses multi-pass overwrite (DoD standard) to prevent forensic recovery.
- **Network Safety:** Monitors active sockets to prevent unauthorized data exfiltration.

## 3. Command Reference
| Command | Description |
| :--- | :--- |
| `python cli.py encrypt <file>` | Encrypts and locks a file in the vault. |
| `python cli.py decrypt <file>` | Decrypts a file from the vault. |
| `python cli.py shred <file>` | Permanently destroys a file. |
| `python cli.py monitor` | Lists all active network connections. |

## 4. Audit Logs
All actions are recorded in `.vault_log.txt`. This file is hidden in your system directory for privacy.
