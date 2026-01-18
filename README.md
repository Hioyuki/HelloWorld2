# Networking Project: Python UDP/TCP Client-Server Communication

## Overview
This project demonstrates a Client-Server networking model using Python's `socket` library. It includes both TCP and UDP implementations to showcase the differences between connection-oriented and connectionless protocols.

## Networking Realization
- **Model**: Client-Server
- **Protocol**: UDP (and TCP as secondary)
- **Message Structure**: Text-based commands (UTF-8 encoded)

## Development Environment
- **Language**: Python 3.12
- **Hardware**: Raspberry Pi (Kali Linux) as Server, MacBook Air as Client
- **Libraries**: `socket`, `datetime`, `random`

## Unique Requirements
I have implemented the following additional requirement:
- **Three different kinds of requests**: The server responds to "time", "lucky", and "help" commands with specific data processing.

## How to Run
1. **Server (Raspberry Pi)**:
   ```bash
   python3 udp_server.py
