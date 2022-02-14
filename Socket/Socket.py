import socket 
from util import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f'Scanner: {self.ip}'

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        open_ports = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(open_ports))

@timefunc
def main():
    # IP to scan for open ports
    ip = '172.20.10.9'
    scanner = Scanner(ip)
    scanner.scan(1, 65535)
    scanner.write('./open_ports')
    print(scanner.open_ports)


if __name__ == "__main__":
    main()
