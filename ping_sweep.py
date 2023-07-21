import subprocess
sys = input("Are you using a linux(L), MAC(M), or a Windows(W) system?:  ").lower()

if sys == "w":
    sys = "-n"
else:
    sys = "-c"

def ping_ip(ip):
    command = ['ping', sys, '2', ip]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return process.returncode == 0

ip_list = [
    # input different IPs here,
    # Separated by commas,
    # Like this:
    # "0.0.0.0,"
    # "1.1.1.1,"
    # Please make sure that they're separated by commas,
    # Or else it will automatically reject them and count it as one ip,
    # Can also input websites
]

accepted = []
rejected = []

print("Pinging...")
for ip in ip_list:
    if ping_ip(ip):
        print(f"{ip} accepted connections.")
        accepted += [ip]
        # accepted += ['']
    else:
        print(f"{ip} did not accept connections.")
        rejected += [ip]
        # rejected += ['']

print(" ---------------- ")

print(f"These ips were accepted, {accepted}")
print(f"These ips were rejected, {rejected}")

print(" ---------------- ")

