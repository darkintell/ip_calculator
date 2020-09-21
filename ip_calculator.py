from modules.ip_tool import calculate
import re

class IpCalculator:
    def __init__(self, ip, netmask):
        self.ip = ip
        self.netmask = netmask
        self.listed_ip = self.ip.split('.')
        
    #Validate ip and netmask for correct ranges
    def validation(self):
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
        
        if self.netmask.isnumeric() and 0 <= int(self.netmask) <= 31:
            is_valid = True
        
        else:
            print("Netmask range is invalid.(0-31)")
            return False
        
        return is_valid
    
    #Show Binary Form of IP Address
    def show_bin(self, ip):
        bin_ip = [str(bin(int(i)))[2:] for i in ip.split('.')]
        s=[]
        for i in range(len(bin_ip)):
            if len(bin_ip[i])!=8:
                bin_ip[i] = ((8-len(bin_ip[i]))*'0')+bin_ip[i] 
                
        return('.'.join(bin_ip))
    
    #Show Valid Hosts in Network
    def show_hosts(self):
        return 2**(32 - int(self.netmask)) - 2
    
    #Show Ip Class
    def ip_class(self):
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
            
    #Calculate The Netmask and Wirldcard ip
    def netmask_wildcard(self):
        netmask = int(self.netmask)
        bin_ip = (netmask * '1') + ((32 - netmask)*'0')
        listed_ip = []
        for i in range(0,32,8):
            listed_ip.append(str(int(str(bin_ip[i:i+8]),2)))
            
        
        wildcard = [str(255 - int(listed_ip[i])) for i in range(0,4)]
        return(('.'.join(listed_ip)),'.'.join(wildcard))
    
    #Calculate The network, broadcast, min and max ip 
    def ip_detail(self):
        ip_listed =[int(i) for i in self.listed_ip]
        netmask = int(self.netmask)

        if  0<= netmask <=7:
            return(calculate(netmask, ip_listed,1))
            
        elif 8<= netmask <= 15:
            return(calculate(netmask, ip_listed,2))

        elif 16<= netmask <=23:
            return(calculate(netmask, ip_listed,3))

        elif 24 <= netmask <= 31:
            return(calculate(netmask, ip_listed,4))
    
   
def print_with_indentation(message, ip, binary='') :
    max_indent = 70
    a = len(message)
    b = len(ip)
    c = len(binary)
    d = int(a+b+c)
    indent = int(max_indent - d)
    f = 17-len(message)
    print(message,(' '*f),ip,(" "*(70-(d+f))),binary,"|")
    
def menu():
    print("-"*76)
    print("-"*27," IP Calculator v1.0 ","-"*27)
    print("-"*24,"  Website : bambootech.ir ",24*"-")
    print("-"*27," Creator : Salvatore","-"*27)
    print("-"*76)
    
if __name__ == '__main__':
    menu()
    ip = input("IP-Address# ")
    netmask =input("Netmask(0-31)# ")
    data = IpCalculator(ip,netmask)
    if data.validation(): 
        print("-"*76)
        print_with_indentation("| Address:", ip,data.show_bin(ip))
        print("| Class of IP:",data.ip_class())
        print("-"*76)
        print_with_indentation("| Netmask:",data.netmask_wildcard()[0],data.show_bin(data.netmask_wildcard()[0]))
        print_with_indentation("| Wildcard:",data.netmask_wildcard()[1],data.show_bin(data.netmask_wildcard()[1]))
        print("-"*76)
        print_with_indentation("| Network:",data.ip_detail()[0],data.show_bin(data.ip_detail()[0]))
        print_with_indentation("| Broadcast:",data.ip_detail()[1],data.show_bin(data.ip_detail()[1]))
        print("-"*76)
        print_with_indentation("| Host Min:",data.ip_detail()[2],data.show_bin(data.ip_detail()[2]))
        print_with_indentation("| Host Max:",data.ip_detail()[3],data.show_bin(data.ip_detail()[3]))
        print("| Hosts: ",data.show_hosts())
        print("-"*76)
    
    
    