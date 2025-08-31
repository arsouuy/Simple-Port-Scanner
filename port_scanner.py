import nmap

nm = nmap.PortScanner()
# (safe target) or your local subnet 
target = "scanme.nmap.org"

options = "-sV -sC"

print(f"Scanning {target} ...\n")
nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")

        port_info = nm[host][protocol]
        for port in port_info.keys():
            state = port_info[port]['state']
            service = port_info[port]['name']
            product = port_info[port].get('product', '')
            version = port_info[port].get('version', '')
            extrainfo = port_info[port].get('extrainfo', '')

            print(f"Port: {port}\tState: {state}\tService: {service} {product} {version} {extrainfo}")
