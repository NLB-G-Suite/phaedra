def in_blocklist(blocklist, sentence):
    for entry in blocklist:
        if entry in sentence:
            return True
        
    return False