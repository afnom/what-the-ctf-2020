# PASSWORD CRACKING

I'll give you a hash to crack and a file that's been encrypted with the password I hashed.

The command used to encrypt the flag using the secret value is:

`openssl aes-256-cbc -pbkdf2 -nosalt -in flag1.txt -out flag1.txt.enc -k <PASSWORD>`

where <PASSWORD> is whatever password you recovered from the hash.


Your first step will to be to work out what type of hash I've given you, chef de la cyber (https://gchq.github.io/CyberChef/) has an excellent tool for doing this.

The tools you'll want to use for password cracking are:

https://github.com/magnumripper/JohnTheRipper
https://github.com/hashcat/hashcat

Hashcat is much more powerful, but john the ripper is easier to use, hashcat tends to be very fussy about the format of hashfile it accepts.

Good password lists to use (HINT HINT HINT):

https://github.com/ashleygwilliams/rockyou
https://github.com/danielmiessler/SecLists

This is a good starter guide to password cracking using hashcat, john the ripper is more self explanatory, just run `john --help`

https://www.unix-ninja.com/p/A_guide_to_password_cracking_with_Hashcat

the `hashcat --help` manual is also very useful, but also incredibly long so more useful when you know what you're looking for.