def Vigenere(m, key, d=''):
    '''
    m:message
    key:Vigenere encrypt key,should be list 
    d:replace dict
    '''
    if d == '':
        d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in xrange(len(key)):
        key[i] = map(lambda i: i-ord('A'), map(ord, key[i]))
    klen = map(len, key)
    kindex = map(lambda i: 0, key)
    m = map(lambda i: i-ord('A'), map(ord, m))
    re = ''
    for i in m:
        index = i
        for j in xrange(len(key)):
            index += (key[j][kindex[j]])
        re += d[index % 26]
        for j in xrange(len(kindex)):
            kindex[j] = (kindex[j]+1) % klen[j]
    return re

if __name__ == '__main__':
    x = 'xpfzxkaqfcrnxlivykaiiy'
    # y = 'heded'
    y = 'skycloud'
    print Vigenere(x, [y])
