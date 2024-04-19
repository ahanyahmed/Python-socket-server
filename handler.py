import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip().decode('utf-8')
        if data:
            command, string_data = data[0], data[1:]
            print(f'recieved message: "{string_data}" with command letter: "{command}"')
            if command == 'W':
                result = f"The number of words is {len(string_data.split())}"
            elif command == 'L':
                result = f"The number of lowercase letters is {sum(1 for char in string_data if char.islower())}"
            elif command == 'U':
                result = f"The number of uppercase letters is {sum(1 for char in string_data if char.isupper())}"
            elif command == 'R':
                result = f"The number of numeric characters is {sum(1 for char in string_data if char.isdigit())}"
            elif command == 'T':
                result = len(string_data)
            else:
                result = data

            response = str(result).encode('utf-8')
            self.request.sendall(response)