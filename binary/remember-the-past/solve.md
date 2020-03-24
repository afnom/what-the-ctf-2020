1. Nmap the port to detect an express http server
    - alternatively, just explore
2. Use HTTP POST to send over something with `code` parameter
3. Craft a payload
    - code=require('child_process').execSync('ls -al')