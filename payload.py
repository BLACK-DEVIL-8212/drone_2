import socket

class DronePayload:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.connection = None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print("Payload server started. Waiting for connection...")

        self.connection, address = self.server_socket.accept()
        print("Payload connected to:", address)

    def receive_commands(self):
        while True:
            command = self.connection.recv(1024).decode()
            if not command:
                break

            if command == "takeoff":
                self.takeoff()
            elif command == "land":
                self.land()
            elif command == "forward":
                self.move_forward()
            elif command == "backward":
                self.move_backward()
            elif command == "stop":
                self.stop()
            else:
                print("Unknown command:", command)

    def takeoff(self):
        print("Payload takeoff command received.")
        # Implementation for payload takeoff

    def land(self):
        print("Payload land command received.")
        # Implementation for payload landing

    def move_forward(self):
        print("Payload move forward command received.")
        # Implementation for moving payload forward

    def move_backward(self):
        print("Payload move backward command received.")
        # Implementation for moving payload backward

    def stop(self):
        print("Payload stop command received.")
        # Implementation for stopping payload

    def stop_server(self):
        if self.connection:
            self.connection.close()
        if self.server_socket:
            self.server_socket.close()
        print("Payload server stopped.")

# Example usage
payload = DronePayload('localhost', 5000)  # Replace with the payload's IP address and port
payload.start_server()
payload.receive_commands()
payload.stop_server()
