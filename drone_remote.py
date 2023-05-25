import speech_recognition as sr
import socket

class DroneRemote:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to the drone.")

    def send_command(self, command):
        self.client_socket.send(command.encode())

    def disconnect(self):
        self.client_socket.close()
        print("Disconnected from the drone.")

    def recognize_speech(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("Recognized speech:", text)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print("Speech recognition service error:", str(e))

    def run(self):
        self.connect()
        while True:
            command = self.recognize_speech()
            if command == "take off":
                self.send_command("takeoff")
            elif command == "land":
                self.send_command("land")
            elif command == "move forward":
                self.send_command("forward")
            elif command == "move backward":
                self.send_command("backward")
            elif command == "stop":
                self.send_command("stop")
            elif command == "disconnect":
                self.disconnect()
                break
            else:
                print("Unknown command:", command)

# Example usage
remote = DroneRemote('localhost', 5000)  # Replace with the drone's IP address and port
remote.run()
