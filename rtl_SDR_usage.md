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
