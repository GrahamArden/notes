# lan.trigfa.org.uk

My home network is connected to the internet via full fibre provided by [KCOM](https://www.kcom.com/). I'm actually quite pleased with the service I get from them. A number of other services are moving into the area as their monopoly is ending, but currently I see no reason to change.

Various services are provided on the network.  

Note that the links below will only work if your in my house (__Hey, who are you and what are you doing here?!__) or when connected via the VPN:

| Host ip | Host name | OS | Used for... |
| ---- | ---- | ---- | ---- |
| 192.168.1.1 | alpha.lan.trigfa.org.uk | [Synology DSM](https://www.synology.com/en-us/dsm) | [File server](https://alpha.lan.trigfa.org.uk:5001/),  [Syncthing](http://alpha.lan.trigfa.org.uk:8384)|
| 192.168.1.3 | pihole.lan.trigfa.org.uk |[RaspberryPi OS](https://www.raspberrypi.com/software/operating-systems/) | [pihole ad blocker](http://pihole.lan.trigfa.org.uk/admin), VPN server |
|  |  |  |  |
| 192.168.1.11 | lms.lan.trigfa.org.uk | [RaspberryPi OS](https://www.raspberrypi.com/software/operating-systems/) | [piCorePlayer](http://lms.lan.trigfa.org.uk),[LMS server](http://lms.lan.trigfa.org.uk:9000/) |
|  |  |  |  |



I use [PIVPN](https://pivpn.io/) on one of the [Raspberry Pis](https://www.raspberrypi.com/) to provide ad blocking along with a VPN into my home network. 
- A couple of useful guides by Abhineet Gupta to using the pihole are available [here](https://medium.com/@timebarrier/install-pivpn-with-wireguard-on-a-raspberry-pi-with-pihole-19d95ba8d206) and [here](https://medium.com/@timebarrier/setting-up-pihole-and-pivpn-for-privacy-and-security-in-the-iot-era-613dbbb29584)


[up](README.md)
[top](../README.md)
