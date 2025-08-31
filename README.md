# Simple-Port-Scanner
This is a small project I made while learning Python and networking. It scans a host (like scanme.nmap.org) and shows the open ports + services running.  Nothing fancy, just me practicing and getting my hands dirty with Python + Nmap.
This script is just a simple port scanner using Python with nmap.
You run it, type the IP of your target (make sure it is a safe target), and it scans it.
It shows if the host is up, what ports are open, and what services are running on them.
I just used the arguments -sV -sC so it also tries to grab version info and run default scripts.
