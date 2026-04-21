from zapv2 import ZAPv2
import time

ZAP_ADDRESS = "127.0.0.1"
ZAP_PORT = "8087"
TARGET = "http://host.docker.internal:3000"

zap = ZAPv2(apikey=None, proxies = {
    'http' : f"http://{ZAP_ADDRESS}:{ZAP_PORT}",
    'https' : f"http://{ZAP_ADDRESS}:{ZAP_PORT}"
})

print("[+] Accessing Target ...")
zap.urlopen(TARGET)
time.sleep(2)

print("🕷️  Spider deployed ...")
scan_id = zap.spider.scan(TARGET)

while(int(zap.spider.status(scan_id)) < 100):
    print(f"🕷️ Spider progress is {zap.spider.status(scan_id)}% completed !")
    time.sleep(2)

print("🕷️ activity completed !")

time.sleep(6)

print("Starting active scan ...")
ascan_id = zap.ascan.scan(TARGET)
while(int(zap.ascan.status(ascan_id)) < 100):
    print(f"Active scan progress is {zap.ascan.status(ascan_id)}% completed !")
    time.sleep(4)

print("Active scan completed !")

alerts = zap.core.alerts()
print(f"Total alert found : {len(alerts)}")

for alert in alerts:
    print('-------------------------------------------------------------------')
    print(f"Risk : {alert['risk']}")
    print(f"Name : {alert['name']}")
    print(f"URL : {alert['url']}")
    print('-------------------------------------------------------------------')
