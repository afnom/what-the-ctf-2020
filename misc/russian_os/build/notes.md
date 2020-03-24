# russian_os

Seriously, a better challenge name needs to be found.

Aim of challenge: hack into russian operating system and retrieve file.

Only access to the system is via a custom "russian terminal", which is actually a python script that jsut translates everything into russian characters, sends data really slowly and restricts commands that can be typed.

Beyond understanding the terminal it's basically a privesc challenge. One of the commands is wisdom, which is a homebrewed version of fortune. catting the wisdom program shows it is a python script which calls `head`, and that it gets its input file from an environment variable `quotes_file`. An `ls -l` on head shows it has a sticky bit set, that can read the flag.txt file.

To get the flag the user just has to export `quotes_file=/home/comrade/flag.txt` and then run `wisdom`.

To run the challenge use the dockerfile provided:

```
sudo docker build . -t russian_os
sudo docker run russian_os
```

which will hang, then nc into the container on port 1111 and you should get a lovely

     WЭЛЧОМЭ ЧОМРЯДЭ!!!!
Энтэр чоммянд>

(I really want to make the banner some russian ascii art but can't find any)


## fun trivia

If you use a basic online transliterator you get this 
`JaFNOM{1n''shhovijet''Rjushhshhija''fl4g''chjaptjurje''y0ju}`

some great russian sayings in the quotes file:

	Every vegetable has its day

	Every sandpiper praises their own swamp
