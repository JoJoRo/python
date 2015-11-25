# Detects an input that correspond to an email,
# of the form: (one letter)(letters, digits, '_')@(letters)(dot)(two or three letters)

import sys
import re

#EMAIL:
pattern = r"^[a-z][\w]+@[a-z]+\.[a-z]{2,3}$"
regexp = re.compile(pattern, re.IGNORECASE)

for line in sys.stdin:
	result = regexp.search(line)
	if result:
		print("\x1B[32;40m" + "Pattern matched:" + "\x1B[0m")
		sys.stdout.write(line)
	else:
		print("\x1B[31;40m" + "Pattern not matched!" + "\x1B[0m")
