def cesar(message, k):
    return "".join(
        chr((ord(c) - (o:=ord('a' if c.islower() else 'A')) + k) % 26 + o)
        if c.isalpha() else c
        for c in message
    )
cesar("je suis un codeur",3)