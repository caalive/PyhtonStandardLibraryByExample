# fileName: string_capwords.py

import string
s = 'The quick brow fox jumped over the lazy dog.'


print(s)

print(' '.join(x.capitalize() for x in s.split(' ')))

print(string.capwords(s))