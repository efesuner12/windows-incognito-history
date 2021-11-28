import subprocess

data = subprocess.check_output(['ipconfig', '/displaydns']).decode("utf-8", errors = "backslashreplace")

print(f"INCOGNITO HISTORY\n{data}")
