#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def get_speed_array(filename):
    speed_list = []
    
    fo = open(filename, "r")

    for line in fo.readlines():
        print "data: %s" % (line)
        str_list = line.split(' ')
        #print(str_list)
        speed_list.append(str_list[-2])

    fo.close()

    tmp = np.array(speed_list)
    speed_array = tmp.astype(np.float)
    return speed_array


speed_array1 = get_speed_array("iperf1.txt")
speed_array2 = get_speed_array("iperf2.txt")
speed_array3 = get_speed_array("iperf3.txt")

x = range(max(len(speed_array1), len(speed_array2), len(speed_array3)))

print(x)

plt.plot(x, speed_array1, c='b')
plt.plot(x, speed_array2, c='g')
plt.plot(x, speed_array3, c='r')

plt.xlabel("Time(s)")       #X���ǩ  
plt.ylabel("Speed(Mbps)")   #Y���ǩ  
plt.title("Wi-Fi Speed")    #ͼ����  
plt.grid(True)
plt.savefig("speed.jpg")     #����ͼ  
plt.show()                  #��ʾͼ  
