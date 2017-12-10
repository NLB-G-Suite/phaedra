import os
from sets import Set

def doc_to_text_catdoc(filename):
    (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
    fi.close()
    retval = fo.read()
    erroroutput = fe.read()
    fo.close()
    fe.close()
    if not erroroutput:
        return retval
    else:
        raise OSError("Executing the command caused an error: %s" % erroroutput)

if __name__ == '__main__':
    blocked_users = []
    blocked_users.append('[Speaker icon]')
    blocked_users.append('environment. Create a free account')
    blocked_users.append('FREE. They are waiting for you right now!')
    text = doc_to_text_catdoc("phaedra.doc")

    authorsUnique = Set()
    authors = []

    lines = text.splitlines()
    for line in lines:
        if ':' in line:
            splitline = line.split(':')
            author = splitline[0]
            text = splitline[1]
            matched = False
            for user in blocked_users:
                if user in author:
                    matched = True

            if not matched:
                print(author)
                authorsUnique.add(author)
                authors.append(author)

    print('unique authors: ' + str(len(authorsUnique)))
    print('authors: ' + str(len(authors)))