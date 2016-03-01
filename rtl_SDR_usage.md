# RTL SDR USAGE

#### Installation
1. sudo apt-get update
2. sudo apt-get install git
3. sudo apt-get install cmake
4. sudo apt-get install libusb-1.0-0.dev
5. sudo apt-get install build-essential
6. git clone git://osmocom.org/rtl-sdr.git
7. cd rtl-sdr/
8. mkdir build
9. cd build
10. cmake ../ -DINSTALL_UDEV_RULES=ON
11. make
12. sudo make install
13. sudo ldconfig
14. sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
15. RESTART LAPTOP

#### Testing
1. sudo rtl_test -t

Normal behavior:
```
pagliacci@anton:~$ rtl_test -t
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Supported gain values (29): 0.0 0.9 1.4 2.7 3.7 7.7 8.7 12.5 14.4 15.7 16.6 19.7 20.7 22.9 25.4 28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6 
[R82XX] PLL not locked!
Sampling at 2048000 S/s.
No E4000 tuner found, aborting.
pagliacci@anton:~$ 
```
2. if error:
```
Kernel driver is active, or device is claimed by second instance of librtlsdr.
In the first case, please either detach or blacklist the kernel module
(dvb_usb_rtl28xxu), or enable automatic detaching at compile time.
```
Need fixing.

#### Fixing
1. create "no-rtl.conf" in /etc/modprobe.d
2. write in it: 
```
blacklist dvb_usb_rtl28xxu
blacklist rtl2832
blacklist rtl2830
```
3. eject device
4. sudo rmmod dvb_usb_rtl28xxu rtl2832
5. PROFIT!
