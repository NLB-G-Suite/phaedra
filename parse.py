import os
from sets import Set

# split -l $[ $(wc -l sentences_unique.txt|cut -d" " -f1) * 85 / 100 ] sentences_unique.txt

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

    sentencesUnique = Set()
    sentences = []

    lines = text.splitlines()
    for line in lines:
        if ':' in line:
            splitline = line.split(':')
            author = splitline[0]
            text = splitline[1][1:]
            matched = False
            for user in blocked_users:
                if user in author:
                    matched = True

            if not matched:
                print(text)
                authorsUnique.add(author)
                authors.append(author)

                sentencesUnique.add(text)
                sentences.append(text)

    print('unique authors: ' + str(len(authorsUnique)))
    print('authors: ' + str(len(authors)))

    print('unique sentences: ' + str(len(sentencesUnique)))
    print('sentences: ' + str(len(sentences)))

    textsFile = open('sentences.txt', 'w')
    for sentence in sentences:
        textsFile.write(sentence + '\n')
    textsFile.flush()
    textsFile.close()

    textsFile2 = open('sentences_unique.txt', 'w')
    for sentence in sentencesUnique:
        textsFile2.write(sentence + '\n')
    textsFile2.flush()
    textsFile2.close()