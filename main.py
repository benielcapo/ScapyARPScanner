from scapy.all import *

def SendARP():
    startIndex = len("Ether / ARP is at ")
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2, verbose=0)
    answers = {}
    for device in ans:
        answer = str(device.answer)[startIndex:]
        answer = answer.replace("/ Padding", "")
        macAndIp = answer.split(" says ")
        ip = macAndIp[1].replace(" ", "")
        mac = macAndIp[0]
        answers[ip] = mac
    return answers


def PrintStyled(data, dashMultipler = 50):
    print("IP\t\t\tMAC")
    print("-" * dashMultipler)
    for deviceIp in data:
        deviceMac = data[deviceIp]
        print(f"{deviceIp}\t\t{deviceMac}")

devices = SendARP()
PrintStyled(devices)
