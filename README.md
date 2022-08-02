# NLS Scanner
A Launcher for NLSScan (by HTC/TQN - VinCSS)


## 1. Description
Some modifications in this version:
  - Disable 'Delete NLS file and confirm message box'
  - Change NLS File copied destination
  - Add log file scan to report
  - Remove 'Press Enter key to exit' prompt
  - Add get client basic information
  - Add upload scan result to s3 service


## 2. Build Launcher
```bash
$ pip install -r requirements.txt
$ python nls-util.py build
```

## 3. Reference
 - [RE023] Phân tích nhanh và xử lý loạt biến thể mã độc mới của nhóm tin tặc Panda đã từng tấn công Ban Cơ yếu Chính Phủ Việt Nam đang hoạt động mạnh gần đây: https://blog.vincss.net/2021/07/re023-phan-tich-va-xu-ly-loat-bien-the-ma-doc-moi-cua-Panda-da-tung-tan-cong-BCYCP-VN.html
 - VinCSS-RE-Tools-Ultilities: https://github.com/VinCSS-Public-Projects/VinCSS-RE-Tools-Ultilities/tree/main/NLSScan
