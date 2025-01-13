# Advanced Encryption Tool

The **Advanced Encryption Tool** is a robust application for encrypting and decrypting files using the AES-256 encryption algorithm. It provides a user-friendly interface and strong security measures, making it ideal for protecting sensitive files.

---

## Features

- **AES-256 Encryption**: Uses AES-256 with GCM mode for authentication and integrity.
- **User-Friendly GUI**: A simple and intuitive graphical interface for file encryption and decryption.
- **Secure Key Derivation**: Password-based encryption with PBKDF2 for generating strong keys.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Requirements

- **Python 3.8 or higher**
- Required Python Libraries (install via `requirements.txt`):
  - `cryptography`
  - `PyQt5`

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/advanced-encryption-tool.git
cd advanced-encryption-tool
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Tool

1. **Run the Application**:
   ```bash
   python gui/app_gui.py
   ```

2. **Encrypt a File**:
   - Enter a strong password in the GUI.
   - Click "Encrypt File" and select the file you want to encrypt.
   - Choose a location to save the encrypted file.

3. **Decrypt a File**:
   - Enter the same password used for encryption.
   - Click "Decrypt File" and select the encrypted file.
   - Choose a location to save the decrypted file.

---

## Packaging the Application (Optional)

To create a standalone executable:

1. Install **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. Package the application:
   ```bash
   pyinstaller --onefile gui/app_gui.py
   ```

3. The executable will be available in the `dist/` directory.

---

## Troubleshooting

- **Invalid Password**: Ensure the password matches the one used during encryption.
- **Corrupted File**: If the file was modified or corrupted, decryption will fail.
- **Dependencies Not Found**: Run `pip install -r requirements.txt` to ensure all dependencies are installed.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

Developed by [Your Name](https://github.com/yourusername).

---

## Screenshots (Optional)

You can include screenshots of the GUI here to help users understand the interface.

