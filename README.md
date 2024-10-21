# Web-Sockets
In this assignment, I developed a real-time communication application using WebSockets. The server modifies messages sent by the client by appending a random number and returns them. I tested the reliability of the WebSocket connection by sending 10,000 requests from the client to ensure that no messages were dropped.

Key Features:
Full-duplex Communication: WebSocket enables simultaneous message exchange between the client and server.
Server Logic: Each message received by the server is modified with a random number and sent back to the client.
Client-side Testing: The client sends 10,000 messages to verify the reliability of the WebSocket connection.
User Interface (UI): A simple web interface allows users to interact with the WebSocket server, sending messages and receiving responses in real time.
