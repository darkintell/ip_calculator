def ip_assemble(listed_ip, network, broadcast, min_ip, max_ip, part):
    ips =[0,0,0,0]
    if part ==1:
        ips[0] = '.'.join([str(network),'0','0','0']) #Network
        ips[1] = '.'.join([str(broadcast)+'255','255','255']) #Broadcast
        ips[2] = '.'.join([str(min_ip)+'0','0','1']) #MIn_ip
        ips[3] = '.'.join([str(max_ip)+'255','255','254']) #Max_ip
        return ips
    
    elif part ==2:
        ips[0] = '.'.join([str(listed_ip[0]), str(network), '0', '0'])
        ips[1] = '.'.join([str(listed_ip[0]), str(broadcast), '255', '255'])
        ips[2] = '.'.join([str(listed_ip[0]), str(min_ip), '0', '1'])
        ips[3] = '.'.join([str(listed_ip[0]), str(max_ip), '255', '254'])
        return ips
    
    elif part ==3:
        ips[0] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(network), '0'])
        ips[1] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(broadcast), '255'])
        ips[2] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(min_ip), '1'])
        ips[3] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(max_ip), '254'])
        return ips
        
    elif part ==4:
        ips[0] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(listed_ip[2]), str(network)])
        ips[1] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(listed_ip[2]), str(broadcast)])
        ips[2] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(listed_ip[2]), str(min_ip)])
        ips[3] = '.'.join([str(listed_ip[0]), str(listed_ip[1]), str(listed_ip[2]), str(max_ip)])
        return ips

def calculate(netmask,ip,part):
    a = int(netmask%8)
    x = 8 - a
    b = 2**x
    y = 256 // b 
    list = []

    for i in range(0,256,b):
        list.append([j for j in range(i,i+b)])
      
    # network, broadcast, min_ip, max_ip =0
    for i in list:
        if part ==4:
            if ip[3] in i:
                network = i[0]
                broadcast = (i[::-1][0])
                min_ip = i[1]
                max_ip = (i[::-1][1])
                return ip_assemble(ip,network, broadcast, min_ip, max_ip, 4)
            
        elif part ==3:
            if ip[2] in i:
                network = i[0]
                broadcast = (i[::-1])[0]
                min_ip = i[0]
                max_ip = (i[::-1])[0]
                return ip_assemble(ip,network, broadcast, min_ip, max_ip, 3)

                
        elif part ==2:
            if ip[1] in i:
                network = i[0]
                broadcast = (i[::-1])[0]
                min_ip = i[0]
                max_ip = (i[::-1])[0]
                return ip_assemble(ip,network, broadcast, min_ip, max_ip, 2)
                
        elif part ==1:
            if ip[0] in i:
                network = i[0]
                broadcast = (i[::-1])[0]
                min_ip = i[0]
                max_ip = (i[::-1])[0] 
                return ip_assemble(ip,network, broadcast, min_ip, max_ip, 1)
            