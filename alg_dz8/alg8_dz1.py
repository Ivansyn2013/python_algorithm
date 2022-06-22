import hashlib


def rabin_karp(s, t):
    gg = 0
    len_t = len(t)
    has_t = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_t + 1):
        has_temp = hashlib.sha1((s[i:i + len_t]).encode('utf-8')).hexdigest()
        if has_t == has_temp:
            gg += 1

    return gg


def get_all_substr(stri):
    if stri == '':
        return -1

    result = set()
    for i in range(1, len(stri)):
        for j in range(0, (len(stri) // i)):
            result.add(hashlib.sha1(stri[i * j:i * (j + 1)].encode('utf-8')).hexdigest())
    print(result)
    return f'Substrings in string = {len(result)}'


print(get_all_substr('assgg'))
