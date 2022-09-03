
print('\n---------------------------------------------------\n')
slashInput = input("Enter the any value between /24 to /30 : ")
slashValue = int(slashInput[1:])

def printSubnetMask(slashValue):

    numberOf0s = 32 - slashValue
    numberOf1s = 8 - numberOf0s

    baseSubnetMask = '11111111.11111111.11111111.'
    extraSubnetMask = numberOf1s*'1' + numberOf0s*'0'
    binarySubnetMask = baseSubnetMask + extraSubnetMask

    extraDec = 0
    power = 7
    for i in extraSubnetMask:
        if(int(i)):
            extraDec = extraDec + (2**power)
        power = power - 1
    decimalSubnetMask = '255.255.255.'+str(extraDec)

    print(f'binary_format subnetMask : {binarySubnetMask}')
    print(f'decimal_format subnetMask : {decimalSubnetMask}')

def printMaxSubnets(slashValue):
    numberOf0s = 32 - slashValue
    numberOf1s = 8 - numberOf0s
    print(f"Number of subnetworks are : {2**numberOf1s}")

def printAllHostAddresses(slashValue):

    numberOf0s = 32 - slashValue
    increment = 2**numberOf0s+1
    numberOf1s = 8 - numberOf0s
    baseAddress = '172.16.100.0'

    start = 0;
    for i in range(1,(2**numberOf1s)+1):
        print(f"{i}th subnetwork : ")

        network_address = baseAddress[:-1] + str(int(baseAddress[-1]) + start)
        print(f'    network_address : {network_address}')
        index = 1
        for host in range(start + 1,start+increment-2):
            host_address = baseAddress[:-1] + str(int(baseAddress[-1]) + host)
            print(f'    {index}th host_address : {host_address}')
            index = index + 1
        
        broadcast_address = baseAddress[:-1] + str(int(baseAddress[-1]) + start + increment - 2)
        print(f'    broadcast_address : {broadcast_address}')
        start = start + increment - 1

print('\n---------------------------------------------------\n')
printSubnetMask(slashValue)
print('\n---------------------------------------------------\n')
printMaxSubnets(slashValue)
print('\n---------------------------------------------------\n')
printAllHostAddresses(slashValue)
print('\n---------------------------------------------------\n')