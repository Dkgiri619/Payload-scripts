#!/usr/bin/python3
import base64

wordlists = []
with open("tom.txt") as fp: 
    Lines = fp.readlines() 
    for line in Lines: 
        sample_string = line
        sample_string_bytes = sample_string.encode("ascii") 
        base64_bytes = base64.b64encode(sample_string_bytes) 
        base64_string = base64_bytes.decode("ascii") 
        wordlists.append(base64_string)
        
with open('enc.txt', 'w') as filehandle:
    for listitem in wordlists:
        filehandle.write('%s\n' % listitem)
