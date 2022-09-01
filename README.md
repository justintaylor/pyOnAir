# pyOnAir
Trigger an on air light (via GPIO) when DB flag is set




## work machine






## lights controller

#### create ram drive for DB
1. Create a new directory
  `sudo mkdir /onair`
2. Give all users access
  `sudo chmod 777 /onair`
3. Share the folder on the network
    1. Install Samba
      `sudo apt-get install samba -y`
    2. Start and enable the Samba service:
      `sudo systemctl enable --now smbd`
    3. Open the file:
      `sudo nano /etc/samba.smb.conf` and add the following to it, updating the path as necessary
    ```
    [Public]
    path = /onair
    browsable = yes
    writable = yes
    read only = no
    force create mode = 0666
    force directory mode = 0777
    ``` 
4. Save and close the file. Restart Samba with:
  `sudo systemctl restart smbd`
5. Add additional user for remote access:
  `sudo adduser onair`
6. Give the user access to the share

    `sudo smbpasswd -a onair` (will need to specify a password, can be same as user acct.)
    
    `sudo smbpasswd -e onair` 