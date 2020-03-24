# drox

This challenge is to decode some communications, encoded with an xor cipher on each message. All messages but one are exactly the length of a block. The xor key is just "xord" so when one message is shorter than the block length it gets padded with 0s and the message ends in the word "xord" repeated in plaintext.

This can then be used to decode all the data in the TCP packets.

**xor.py** is the tool used to encode python socket communication, and **talker.py** generated the traffic. One instance of talker.py is used in listening mode and the other in sending mode.
