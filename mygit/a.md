MY GIT
General Skills
Easy
50 pts
7,554 solves
by Darkraicg492
I have built my own Git server with my own rules!

You can clone the challenge repo using the command below.

git clone ssh://git@foggy-cliff.picoctf.net:64034/git/challenge.git

Here's the password: 1a03c9e3

Check the README to get your flag!

Answer:
read the README.md after cloning.
modify a text on it or something idk.
```
git config user.name "root"
git config user.email "root@picoctf"
git status
git add .
git commit -m "anything here idk"
git push
```
```
git@foggy-cliff.picoctf.net's password:
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 514 bytes | 85.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Commit ignored. Either wrong author or flag.txt not in commit.
remote:    Author: root
remote:    Email: root@picoctf
remote:    Files: README.md
remote: a.txt
To ssh://foggy-cliff.picoctf.net:64034/git/challenge.git
   088b58f..9651266  master -> master
```
create flag.txt file.
```
git status
git add .
git commit -m "anything here idk"
git push
```
```
git@foggy-cliff.picoctf.net's password:
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 255 bytes | 85.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: [ANSWER]
To ssh://foggy-cliff.picoctf.net:64034/git/challenge.git
   9651266..888f132  master -> master
```
