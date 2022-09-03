from traceback import print_tb


def checkIP(ip):
        a=ip.split('.')
        if not(( (len(a)==4) and ( 1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int (a[1])!=254) and (0<= int(a[1])<=255) and (0<=int(a[2]) <=255) and (0<=int(a[3])<=255))):
                return 0
        return 1

def decimalToBinary(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] #this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)

ipAddress = input("Enter the ip address : ")
baseip = ipAddress[0:-3]
if(checkIP(ipAddress)):
    baseSubnet = '255.255.255.'
    for i in range(0,8):
        print('\n')
        noOfZeros = 8-i
        noOfOnes = i;
        upperSubnet = '1'*noOfOnes + '0'*noOfZeros
        num = 0
        power = 7
        for i in upperSubnet:
            if(int(i)):
                num = num + 2**power
            power = power - 1
        subnetMask = (baseSubnet + str(num))
        
        ipList = ipAddress.split('.')
        subList = subnetMask.split('.')
        networkList = []
        for i,j in zip(ipList,subList):
            num1 = decimalToBinary(int(i))
            num2 = decimalToBinary(int(j))
            num3 = '0b'
            for i,j in zip(num1,num2):
                num3 = num3 + str(int(i) and int(j))
            networkList.append(str(int(num3,2)))
        reverse_mask = []
        for i in subList:
            if i == '0':
                octet = '00000000'
            else:
                octet = (bin(int(i))[2:])
            new_octet = ''
            for j in octet:
                if( j == '1'):
                    new_octet+='0'
                else:
                    new_octet+='1'
            reverse_mask.append(new_octet)
        broad_list = []
        for i,j in zip(reverse_mask,ipList):
            num3 = '0b'
            for i,j in zip(i,decimalToBinary(int(j))):
                num3 = num3 + str(int(i) or int(j))
            broad_list.append(str(int(num3,2)))
        network_address = '.'.join(networkList)

        print(f'network_address : {network_address}')
        print(f'Host addresses for 1st network for each  subnet : ')
        for i in range(int(networkList[-1])+1,int(broad_list[-1])):
            print(f'    {baseip + str(i)}')

        broadcast_address = '.'.join(broad_list)
        print(f'broadcast_address : {broadcast_address}')
            
        
else:
    print("Incorrect IP!!!")
