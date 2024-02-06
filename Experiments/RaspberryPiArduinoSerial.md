Connect Raspberry Pi and Arduino using USB-A to USB-B cable

## Serial Communication set-up

### Getting Arduino IDE Ready

1. Ensure serial turned on Raspberry Pi:

    ```sudo raspi-config```

Go to option 3, then select option 6 'Serial', and turn on.

2. Type command to see check cinnected devices

    ```lsusb```

Output should look like this:

    team-member@project:~ $ lsusb
    Bus 001 Device 004: ID 2341:0010 Arduino SA Mega 2560 (CDC ACM)
    Bus 001 Device 003: ID 0424:ec00 Microchip Technology, Inc. (formerly SMSC) SMSC9512/9514 Fast Ethernet Adapter
    Bus 001 Device 002: ID 0424:9514 Microchip Technology, Inc. (formerly SMSC) SMC9514 Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

See the option wheich includes: ```Arduino SA Mega 2560 (CDC ACM)```

3. Find the name of the port the Arduino is connected to:

    ```dmesg | grep "tty"```

Output should look like this:

    team-member@project:~ $ dmesg | grep "tty"
    [    0.000000] Kernel command line: coherent_pool=1M 8250.nr_uarts=0 snd_bcm2835.enable_headphones=0 snd_bcm2835.enable_headphones=1 snd_bcm2835.enable_hdmi=1 snd_bcm2835.enable_hdmi=0 video=Composite-1:720x480@60i vc_mem.mem_base=0x3ec00000 vc_mem.mem_size=0x40000000  console=ttyS0,115200 console=tty1 root=PARTUUID=284c5b33-02 rootfstype=ext4 fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles cfg80211.ieee80211_regdom=GB
    [    0.000463] printk: console [tty1] enabled
    [    3.130159] 3f201000.serial: ttyAMA0 at MMIO 0x3f201000 (irq = 114, base_baud = 0) is a PL011 rev2
    [    5.492439] systemd[1]: Created slice system-getty.slice.
    [    9.078701] cdc_acm 1-1.3:1.0: ttyACM0: USB ACM device

We can see the Arduino is on port ```ttyACM0```.


4. Install Arduino IDE Software on to Raspberry Pi

    ```wget https://downloads.arduino.cc/arduino-1.8.19-linuxarm.tar.xz```

    ```tar xvJf arduino-1.8.19-linuxarm.tar.xz```

    ```sudo bash arduino-1.8.19/install.sh```

Once installed, open the program by double clicking arduino file.


### Getting Python ready on Pi

1. Check python version ```python3 --version```
   1. If missing ```sudo apt install python3```
2. Get python plug-ins
   1. PySerial - ```pip install pyserial```
