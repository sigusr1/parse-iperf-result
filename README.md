# parse-iperf-result  

iperf是经常使用的网络带宽测试工具， 它会给出形如下面的输出：

```

[  3]  0.0- 1.0 sec  2.25 MBytes  18.9 Mbits/sec  
[  3]  1.0- 2.0 sec  1.00 MBytes  8.39 Mbits/sec  
[  3]  2.0- 3.0 sec   768 KBytes  6.29 Mbits/sec  
[  3]  3.0- 4.0 sec   640 KBytes  5.24 Mbits/sec  
[  3]  4.0- 5.0 sec   640 KBytes  5.24 Mbits/sec  
[  3]  5.0- 6.0 sec  1.00 MBytes  8.39 Mbits/sec  
[  3]  6.0- 7.0 sec  1.62 MBytes  13.6 Mbits/sec  
[  3]  7.0- 8.0 sec   896 KBytes  7.34 Mbits/sec

```

本程序就是把上面的数字转换成直观的图标，反应测试过程中wifi的波动情况：

比如下图红绿蓝三条线各代表一次采样，可以看出每次采样wifi的波动都比较大：
![speed.jpg](http://data.coderhuo.tech/blog/speed.jpg)
