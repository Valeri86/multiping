import subprocess

ip_group_1 = [1, 2, 3, 4]
ip_group_2 = [5, 6, 7, 8]


ip_group_1_mapping = {
    1: "host1",
    2: "host2",
    3: "host3",
    4: "host4"
}

ip_group_2_mapping = {
    5: "host5",
    6: "host6",
    7: "host7",
    8: "host8"
}

print("#########################")
print("### Group 1           ###")
print("#########################")
print("")
for p in ip_group_1:
    ip="1.2.3." + str(p)
    result = subprocess.call(['ping','-c','2',f'{ip}'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT)
    #set hostname according to ip from dictionary ip_group_1_mapping
    group_1_host = ip_group_1_mapping.get(p)
    if result == 0:
        print ("ping to", group_1_host, ip, "successful")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ :-)")
        print("")
    elif result == 2:
        print ("no response from", group_1_host)
    else:
        print ("ping to", group_1_host, "failed")
        print("--------------------------------------------------------- :-(")
        print("")

print("#########################")
print("###   Group 2         ###")
print("#########################")
print("")
for p in ip_group_2:
    ip="1.2.3." + str(p)
    result = subprocess.call(['ping','-c','2',f'{ip}'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT)
    #set hostname according to ip from dictionary ip_group_2_mapping
    group_2_host = ip_group_2_mapping.get(p)
    if result == 0:
        print ("ping to", group_2_host, ip, "successful")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ :-)")
        print("")
    elif result == 2:
        print ("no response from", group_2_host)
    else:
        print ("ping to", group_2_host, "failed")
        print("--------------------------------------------------------- :-(")
        print("")
