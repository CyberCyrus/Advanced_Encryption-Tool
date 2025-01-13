import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QLabel
from encryption_tool.encryption_tool import encrypt_file, decrypt_file

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Encryption Tool")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()

        self.password_label = QLabel("Enter Password:")
        self.layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.encrypt_button = QPushButton("Encrypt File")
        self.encrypt_button.clicked.connect(self.encrypt_file)
        self.layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt File")
        self.decrypt_button.clicked.connect(self.decrypt_file)
        self.layout.addWidget(self.decrypt_button)

        self.setLayout(self.layout)

    def encrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt")
        if file_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Encrypted File")
            if output_path:
                password = self.password_input.text()
                encrypt_file(file_path, password, output_path)

    def decrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Decrypt")
        if file_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted File")
            if output_path:
                password = self.password_input.text()
                decrypt_file(file_path, password, output_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())
