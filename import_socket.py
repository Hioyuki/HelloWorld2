import socket

# サーバーのIP（ラズパイの有線IPに変えてください）
IP = "192.168.2.6" 
PORT = 9999

# socket.SOCK_DGRAM が UDP の指定
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[*] UDP Client ready. Type 'exit' to quit.")

try:
    while True:
        msg = input("Message >> ")
        # UDPは送るたびに宛先を指定する
        client.sendto(msg.encode('utf-8'), (IP, PORT))
        
        if msg.lower() == "exit":
            break
            
        # サーバーからの返信を待つ
        data, addr = client.recvfrom(1024)
        print(f"[Server {addr}]: {data.decode('utf-8')}")

finally:
    client.close()