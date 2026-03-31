from scrapy import sniff

packet = sniff(count = 1)

print(packet[0].summary())