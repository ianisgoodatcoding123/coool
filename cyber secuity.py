import re

def detect_intrusion(packet):
    """Detects intrusion based on predefined patterns."""
    # Example: Detecting SQL injection attempts
    sql_injection_pattern = r"(select[\s\S]*?from[\s\S]*?where)"
    if re.search(sql_injection_pattern, packet, re.IGNORECASE):
        return True
    return False

# You can then use this function like any other variable
intrusion_detection = detect_intrusion

# Example usage:
network_traffic = [
    "GET /test.php?id=1 OR 1=1 HTTP/1.1",
    "POST /login.php HTTP/1.1",
    "SELECT * FROM users WHERE username='admin' AND password='password';"
]

for packet in network_traffic:
    if intrusion_detection(packet):
        print("Intrusion detected:", packet)
    else:
        print("No intrusion detected for:", packet)

import re

def detect_intrusion(packet):
    """Detects intrusion based on predefined patterns."""
    # Example: Detecting SQL injection attempts
    sql_injection_pattern = r"(select[\s\S]*?from[\s\S]*?where)"
    if re.search(sql_injection_pattern, packet, re.IGNORECASE):
        return True
    return False
