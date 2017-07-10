import requests, sys
from bs4 import BeautifulSoup

r = requests.get("https://www.crossoutdb.com/");

s=BeautifulSoup(r.content, 'lxml' );

it=s.find(id="ItemTable").find("tbody");

f=open("market.csv", "w")
f.write("item,faction,type,popularity,sell_price,sell_offers,buy_price,buy_orders,margin\n")

for item in it.find_all("tr"):
	title=item.find(class_="item-title ").text.strip();
	
	
	data=item.contents[1].text.strip().split("\n")
	title=data[0];
	faction=data[1];
	type=data[2];

	rareity=item.contents[3].text.strip()
	popularity = item.contents[5].text.strip();
	sell_price = item.contents[7].text.strip();
	sell_offers = item.contents[9].text.strip();
	buy_price = item.contents[11].text.strip();
	buy_orders= item.contents[13].text.strip();
	margin = 	item.contents[15].text.strip();

	
	x="\"{}\",{},{},{},{},{},{},{},{}\n".format( title, faction, type, popularity, sell_price, sell_offers, buy_price, buy_orders, margin);
	f.write(x)

f.close()
