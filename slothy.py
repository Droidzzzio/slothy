#!/usr/bin/env python3

import webbrowser as wb
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SLOTHY")
print(ascii_banner)

print("Requires python 3")
print("[+]USAGE:  python slothy.py domain.com\n")
domain=input("Enter the domain : \t")

wb.open_new_tab("http://www.tcpiputils.com/browse/domain/" +domain)

wb.open_new_tab("http://toolbar.netcraft.com/site_report?url=" +domain)

wb.open_new_tab("https://www.shodan.io/search?query=" +domain)

wb.open_new_tab("https://www.censys.io/ipv4?q=" +domain)

wb.open_new_tab("https://crt.sh/?q="+domain +".%25")

wb.open_new_tab("https://www.google.ca/search?q=site:zone-h.org +" +domain)

wb.open_new_tab("https://securityheaders.io/?q=" +domain)

wb.open_new_tab("https://www.ssllabs.com/ssltest/analyze.html?d=" +domain)

wb.open_new_tab("https://securityheaders.io/?q=" +domain)

wb.open_new_tab("https://www.threatcrowd.org/domain.php?domain=" +domain)

wb.open_new_tab("https://www.zoomeye.org/searchResult/bugs?q=" +domain)

wb.open_new_tab("https://securitytrails.com/domain/" +domain +"/dns")

wb.open_new_tab("https://web.archive.org/web/*/" +domain)

wb.open_new_tab("http://viewdns.info/reversewhois/?q=" +domain)

wb.open_new_tab("https://www.punkspider.org/#searchkey=url&searchvalue=" +domain+ "&pagenumber=1&filterType=or")

#Subdomain Enumeration

wb.open_new_tab("https://www.virustotal.com/gui/domain/" +domain+ "/relations")

wb.open_new_tab("https://findsubdomains.com/subdomains-of/" +domain)

wb.open_new_tab("https://dns.bufferover.run/dns?q=" +domain)

wb.open_new_tab("https://www.dnsdb.org/" +domain+ "/")

wb.open_new_tab("http://api.hackertarget.com/hostsearch/?q=" +domain)

 #find subdomains through dorking

wb.open_new_tab("https://www.google.com/search?q=site:*." +domain)

wb.open_new_tab("https://www.google.com/search?q=site:*.*." +domain)

 #sql dorks

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+username+OR+password+OR+login+OR+root+OR+admin")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+inurl:shell+OR+inurl:backdoor+OR+inurl:wso+OR+inurl:cmd+OR+shadow+OR+passwd+OR+boot.ini+OR+inurl:backdoor")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+inurl:readme+OR+inurl:license+OR+inurl:install+OR+inurl:setup+OR+inurl:config")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+inurl:wp-+OR+inurl:plugin+OR+inurl:upload+OR+inurl:download")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+inurl:redir+OR+inurl:url+OR+inurl:redirect+OR+inurl:return+OR+inurl:src=http+OR+inurl:r=http")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+ext:cgi+OR+ext:php+OR+ext:asp+OR+ext:aspx+OR+ext:jsp+OR+ext:jspx+OR+ext:swf+OR+ext:fla+OR+ext:xml")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+ext:doc+OR+ext:docx+OR+ext:csv+OR+ext:pdf+OR+ext:txt+OR+ext:log+OR+ext:bak")

wb.open_new_tab("https://www.google.com/search?q=site:" +domain+ "+ext:action+OR+struts")

wb.open_new_tab("https://www.google.com/search?q=site:pastebin.com+" +domain)

wb.open_new_tab("https://www.google.com/search?q=site:linkedin.com+employees+" +domain)

 

 


