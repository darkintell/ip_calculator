
class IP_Calculato:
    def __init__(self, ip, netmask):
        self.ip = ip
        self.netmask = netmask
        self.listed_ip = self.ip.split('.')
        
        