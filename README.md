# README
This repo contains some interesting stuff including tools, cheatsheets, articles that can be useful for penetration testing or smth.

###Tools

####Information Gathering
1. [theHarvester] (http://tools.kali.org/information-gathering/theharvester) - tool used to gather emails, subdomains, hosts, employee names, open ports and banners from different public sources like search engines, PGP key servers and SHODAN computer database.
2. [fierce] (http://tools.kali.org/information-gathering/fierce) - a reconnaissance tool. Fierce is a PERL script that quickly scans domains (usually in just a few minutes, assuming no network lag) using several tactics.
3. [dnsmap] (http://tools.kali.org/information-gathering/dnsmap) - sub-domain enumeration tool.
4. [searchsploit] (http://tools.kali.org/information-gathering/exploitdb) - utility to search the Exploit Database archive.
5. [dnsenum] (http://tools.kali.org/information-gathering/dnsenum) - script to enumerate DNS information.
6. [DNSRecon] (http://tools.kali.org/information-gathering/dnsrecon) - one more DNS enumeration script.
7. [enum4linux] (http://tools.kali.org/information-gathering/enum4linux) - tool for enumerating data from Windows and Samba hosts.
8. [BlindElephant.py] (http://tools.kali.org/web-applications/blindelephant) - tool for web application fingerprinting
9. metasploit modules:
  *123

####Post Exploitation Tools
1. **rinetd** - Port forwarding tool
```
Usage: /etc/rinetd.conf
change bind address, bind port, connect address, connect port, than restart as a service (/etc/init.d/rinetd restart)
```

####Password attacks
1. pwdump - Windows utility that exposes the LM and NTLM password hashes of local user accounts from the Security Account Manager (SAM) 
[Download] (https://www.dropbox.com/s/ixs1ac0xgl245ea/pwdump.zip?dl=0) //
[Wiki] (https://en.wikipedia.org/wiki/Pwdump)
2. WCE (Windows Credential Editor) - security tool that allows one to perform several attacks to obtain clear text passwords and hashes from a compromised Windows host.
[Download] (https://www.dropbox.com/s/lncton1vtm3fwzp/wce_v1_3beta.zip?dl=0)

####Utilities
1. Plink - console SSH client for Windows.
[Download] (https://www.dropbox.com/s/g42q3pkrlioym75/plink.exe?dl=0)

###Articles
1. Basic Linux privelege escalation.
[Read] (https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)
2. MSSQLi Cheatsheet
[Read] (https://www.exploit-db.com/papers/12975/)
