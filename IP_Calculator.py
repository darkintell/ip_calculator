
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
    
    #Show Binary Form of IP Address
    def ShowBin(self):
        bin_ip = [str(bin(int(i)))[2:] for i in self.listed_ip]
        s=[]
        for i in range(len(bin_ip)):
            if len(bin_ip[i])!=8:
                bin_ip[i] = ((8-len(bin_ip[i]))*'0')+bin_ip[i] 
                
        return('.'.join(bin_ip))
    
    #Show Valid Hosts in Network
    def Show_Hosts(self):
        return 2**(32 - int(self.netmask)) - 2
    
    #
    def IP_Class(self):
        ip_listed = self.listed_ip
        first = int(ip_listed[0])
        if  0<= first <= 127:
            return 'A'
        elif 128 <= first <= 191:
            return 'B'
        elif 192 <= first <= 223:
            return 'C'
        elif 224 <= first <= 239:
            return 'D'
        elif 240 <= first <= 255:
            return 'E'
            
        
if __name__ == '__main__':
    test = IP_Calculator('0.255.255.0','')
    print(test.IP_Class())
    