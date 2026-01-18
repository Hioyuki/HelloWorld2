# Networking Project: Python UDP Client-Server Communication

## Overview

### Project Description
As a software engineer focused on networking and security, I have developed a **Client-Server Communication Tool** using Python's native `socket` library. This project demonstrates a connectionless communication system using the **UDP (User Datagram Protocol)**, enabling real-time data exchange between a MacBook (Client) and a Raspberry Pi (Server).

The system consists of two main components:
* **UDP Server (Raspberry Pi/Kali Linux)**: A backend that listens on a specific port (9999), parses incoming datagrams, and returns dynamic responses based on predefined logic.
* **Interactive UDP Client (macOS)**: A terminal-based interface that allows users to send requests and display responses received from the server.

### Purpose of the Project
The primary goal of this project was to master the fundamentals of **Network Programming (Socket API)** and the **OSI model**. By building this from scratch, I aimed to:
* Understand the core differences between **TCP** (connection-oriented) and **UDP** (connectionless) protocols.
* Implement data serialization and encoding/decoding (UTF-8) for network transit.
* Learn how to troubleshoot physical network layers, such as managing routing conflicts between Wi-Fi and Ethernet on a Raspberry Pi.

### Software Demo Video
[Software Demo Video](あなたの動画リンクをここに貼り付けてください)

---

## Development Environment

### Tools & Infrastructure
* **Hardware**: MacBook Air (Client) & Raspberry Pi 4 (Server)
* **Operating System**: macOS / Kali Linux
* **Network**: Direct Ethernet Connection (Static IP: 192.168.2.3)
* **Editor**: Visual Studio Code / Nano

### Programming Language & Libraries
* **Python 3.x**:
    * `socket`: For low-level network interface access (UDP implementation).
    * `datetime`: For generating dynamic time-based responses.
    * `random`: For processing "lucky number" requests.

---

## Networking Realization
This project satisfies the following module requirements:
1. **Client-Server Model**: Distinct programs for sender and receiver.
2. **Protocol**: Implemented via **UDP** (`socket.SOCK_DGRAM`).
3. **Additional Feature**: Support for 3 different kinds of requests:
    * `time`: Returns the current server system time.
    * `lucky`: Returns a randomly generated number from the server.
    * `help`: Displays a list of available server commands.

---

## Useful Websites
* [Python Documentation - Socket Programming](https://docs.python.org/3/library/socket.html)
* [Wikipedia - OSI Model](https://en.wikipedia.org/wiki/OSI_model)
* [Real Python - Socket Programming in Python](https://realpython.com/python-sockets/)

---

## Future Work
* Implement a **Graphical User Interface (GUI)** using Tkinter.
* Add **End-to-End Encryption** for the transmitted data.
* Transition to a **Peer-to-Peer (P2P)** model for file sharing.
