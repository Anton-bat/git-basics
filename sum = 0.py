import re

def validate_ip_address(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return "валідний"
    else:
        return "не валідний"

# Перевірка на валідність IP-адреси
ip1 = "192.168.0.1"
ip2 = "192.168.270.1"

print("IP", ip1, "є", validate_ip_address(ip1))
print("IP", ip2, "є", validate_ip_address(ip2))