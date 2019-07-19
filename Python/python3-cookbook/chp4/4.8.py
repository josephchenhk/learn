from io import StringIO

many_lines = """
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times, this information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
"""
# print(many_lines)
s = StringIO()
s.write(many_lines)


for line in s.getvalue():
    print(line, end='')

s.close()

