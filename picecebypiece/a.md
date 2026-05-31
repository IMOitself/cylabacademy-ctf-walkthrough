Piece by Piece
General Skills
Easy
50 pts
7,930 solves
by Yahaya Meddy
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.

SSH to dolphin-cove.picoctf.net:53759 and login as ctf-player with password 8d076785.

Answer:
```
# ssh ctf-player@dolphin-cove.picoctf.net -p 53759
The authenticity of host '[dolphin-cove.picoctf.net]:53759 ([3.13.34.175]:53759)' can't be established.
ED25519 key fingerprint is: SHA256:rdvWhF7Klwlu1EivysxTh/FjeqFI0dSEK5gaelaW9t8
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes 
Warning: Permanently added '[dolphin-cove.picoctf.net]:53759' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
ctf-player@dolphin-cove.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.17.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.
ctf-player@pico-chall$ ls
instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
ctf-player@pico-chall$ cat instructions.txt
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
ctf-player@pico-chall$ file part_aa
part_aa: Zip archive data, at least v1.0 to extract
ctf-player@pico-chall$ cat part_aa part_ab part_ac part_ad part_ae > a.zip
ctf-player@pico-chall$ ls
a.zip  instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
ctf-player@pico-chall$ unzip a.zip
Archive:  a.zip
[a.zip] flag.txt password:
 extracting: flag.txt
ctf-player@pico-chall$ ls
a.zip  flag.txt  instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
ctf-player@pico-chall$ cat flag.txt
```