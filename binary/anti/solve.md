# anti

## Exploit

Simple!

	$ error <obfuscated cat function>
	$ cat flag.txt

## Explanation

The file that is received is a minified python file with a link to the
minifier. Some googling should reveal that it has been obfuscated. Without
too much hassle, the user should be able to deobfuscate it a little.

After deobfuscation, the user should see that the program resembles a shell
of some sort. However, it does **not** run arbitrary commands using
subprocess.run or an equivalent. Instead the only main commands, `cat` and
`ls` are implemented internally.

The `error` command should draw the user's attention - as well as being a non
standard command, it also includes a call to eval. However, the input to eval
will have been filtered to only include letters and periods. As the user does
not control the input to this command at any point, this is not exploitable
to give full code execution.

To solve the challenge, the user must find the vulnerability in the `cat`
function. The argument `chunks` is never actually reset between function
calls (due to the fact that objects are passed by reference, not by value),
therefore, it is possible to load the flag into the `chunks` list and then
print them out on a subsequent call.

At this point, the user should notice that it is not allowed to make another
call after a single `cat`. After one `cat`, the program will exit. To solve
this, the user should set the error function to `cat` itself. This will
invoke it a second time, allowing the flag to be printed.

## Reason for difficulty

This challenge is difficult mostly because of the rabbit holes it sends you
down.

The fact it is a shell will lead users to immediately try and get code
execution, probably through the eval function, which is doable. However,
without being able to control the parameters, this will prove very difficult.
Instead, to solve the challenge, the user must realize a very subtle bug in
the code and exploit it carefully.
