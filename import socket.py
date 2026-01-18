import socket
import datetime
import random

# 全てのインターフェースで待ち受け
IP = "0.0.0.0"
PORT = 9999

# 1. UDPソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind
server.bind((IP, PORT))
print(f"[*] UDP Server listening on {IP}:{PORT}")

try:
    while True:
        # クライアントからのデータと、送り主のアドレスを受け取る
        data, addr = server.recvfrom(1024)
        msg = data.decode('utf-8')
        
        if not msg or msg.lower() == "exit":
            print(f"[*] Received exit from {addr}")
            continue
        
        print(f"[*] Request from {addr}: {msg}")
        
        # 追加要件：3種類以上のレスポンス
        msg_low = msg.lower()
        if "time" in msg_low:
            response = f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
        elif "lucky" in msg_low:
            num = random.randint(1, 100)
            response = f"Your lucky number is: {num}"
        elif "help" in msg_low:
            response = "Available commands: time, lucky, help, exit"
        else:
            response = f"UDP ACK: {msg}"
            
        # 送り主(addr)に直接返信する
        server.sendto(response.encode('utf-8'), addr)

finally:
    server.close()
    print("[*] Server stopped.")