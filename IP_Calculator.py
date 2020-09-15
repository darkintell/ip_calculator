
class IP_Calculator:
    def __init__(self, ip, netmask):
        self.ip = ip
        self.netmask = netmask
        self.listed_ip = self.ip.split('.')
        
    #Validate ip and netmask for correct ranges
    def Validator(self):
        is_valid = False
        ip_seprated =  self.listed_ip
        
        if self.ip.count('.') !=3:
            print("IP is not in normal format.")
            return False
        
        for i in ip_seprated:
            if i.isnumeric() and 0 <= int(i) <=255:
                is_valid = True
            else:
                print("IP is not valid.")
                return False
        
        if self.netmask.isnumeric() and 0 <= int(self.netmask) <= 32:
            is_valid = True
        
        else:
            print("Netmask range is invalid.(0-32)")
            return False
        
        return is_valid
    
if __name__ == '__main__':
    test = IP_Calculator('10.22.100.25','21')
    print(test.Validator())
    