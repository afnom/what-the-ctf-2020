for i in {1..3}; do

	cp "hash$i" ./passwords_$i

	pass=`cat pass$i`
	# Encrypt
	openssl aes-256-cbc -pbkdf2 -nosalt -in flag$i.txt -out ./passwords_$i/flag$i.txt.enc -k $pass
	# Test
	[[ `cat flag$i.txt` == `openssl aes-256-cbc -d -pbkdf2 -nosalt -in ./passwords_$i/flag$i.txt.enc -k $pass` ]] || echo "ERROR: $i"
done

