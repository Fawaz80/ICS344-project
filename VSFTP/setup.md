# VSFTPD Setup

## Installation
bash
sudo apt update
sudo apt install vsftpd

Configuration

    Open /etc/vsftpd.conf and update:

    anonymous_enable=NO
    local_enable=YES
    write_enable=YES

    Restart service: sudo systemctl restart vsftpd.

Testing Commands

    Connect: ftp <server-ip>.
    Login: user <username>.

