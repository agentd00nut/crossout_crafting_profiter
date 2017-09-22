import requests, json
# $(".item-title").each( function(x){ console.log( '"'+$( this ).text()+'": '+$( this ).parent().attr("href").split("/")[2]+',' ) })
engineer_rare={
    "littleboy6lb":61,
    "spitfire":4,
    "ac43 rapier":34,
    "improved radiator":108,
    "weapon cooler":78,
    "ammo pack":68,
    "fuel+ tank":433,
    "scope":69,
    "balloon tyre":390,
    "baloon tyre st":388,
    "loot container":90
}
engineer_legendary={
    "Relic container ": 209,
    "Porcupine ": 56,
    "Firebug ": 341,
    "Scorpion ": 49
}

lunatic_rare={
    "at wasp": 44,
    "growl":60,
    "sledgehammer":2,
    "light engine":80,
    "explosive spear":72,
    "buzzsaw": 73,
    "rocket booster": 129,
    "light generator": 77,
    "studded wheels st": 59,
    "chained wheel st": 87,
    "chained wheel": 121,
    "studded wheel": 104
}
lunatic_epic={
    "Thunderbolt ": 1,
    "Cricket 1M ": 38,
    "Gas generator ": 48,
    "Small track ": 62,
    "Improved Cooler ": 66,
    "Improved engine ": 131,
    "Lancelot ": 84,
    "Druzhba 2 ": 92,
    "'Hermes' booster ": 143,
}
lunatic_legendary={
    "Hammerfall ": 3,
    "Harvester ": 46,
}

nomad_rare={
    "MM5-4 Vector ": 7,
    "Attack drone ": 94,
    "ST-M23 Defender ": 74,
    "Wyvern ": 64,
    "Racing wheel ST ": 379,
    "Hazardous generator ": 52,
    "Engine ": 112,
    "Chameleon ": 100,
    "Racing wheel ": 383,
    "Radar-detector ": 142,
    "Landing gear ST ": 389,
    "Landing gear ": 395
}
nomad_epic={
    "MG13 Equalizer ": 31,
    "Spectre-2 ": 40,
    "AC72 Whirlwind ": 32,
    "Charged radiator ": 86,
    "Hardened track ": 63,
    "Missile drone ": 79,
    "Powerful radar-detector ": 122,
    "V8 Engine ": 71,
    "Chameleon Mk2 ": 82
}
nomad_legendary={
    "Reaper ": 33,
    "Retcher ": 55
}

scavenger_rare={
    "Trucker ": 39,
    "Judge 76mm ": 70,
    "Heavy generator ": 41,
    "Auger ": 51,
    "Twin wheel ST ": 83,
    "Large wheel ST ": 113,
    "Twin wheel ": 91,
    "Turret Deployer ": 123,
    "Powerful Engine ": 65,
    "Improved radar ": 152,
    "Large wheel ": 116
}
scavenger_epic={
    "Executioner 88mm ": 45,
    "Pyre ": 6,
    "ZS-34 Fat Man ": 8,
    "Armored track ": 42,
    "GL-55 Impulse ": 30,
    "Expanded ammo pack ": 75,
    "Powerful engine Mk2 ": 117,
    "Powerful radar ": 136,
    "Missile turret ": 124,
}
scavenger_legendary={
    "Hurricane ": 54,
    "Mammoth ": 47,
}


def fetch_price( item ):
    id=str(item);
    
    headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
    r = requests.get("https://crossoutdb.com/data/recipe/"+str(item), headers=headers)
    
    if( r.status_code != 200 ):
        print( "Error fetching "+item);
        return 1;
    
    j = r.json() 

    sell_price = float( j['item']['formatSellPrice'] )
    sell_price_adjusted = sell_price - (sell_price * .1)
    cost = float( j['recipe']['recipe']['sumSellFormat'] )
    profit = round(  sell_price_adjusted - cost, 2)
    instant_profit=profit-5

    return {"cost":cost,
        "sell_price": sell_price,
        "sell_price_adjusted": sell_price_adjusted,
        "profit":profit,
        "instant_profit":instant_profit
    }

def find_profits( item_list, list_name ):

    print(list_name)
    for item, id  in item_list.items():
        price = fetch_price( id )
        if( price['profit'] > 0 ):
            #print( "    '", item, "'        cost:",price['cost'],"  profit:",price['profit'] );
            print("    %22s    cost:%4.2f  profit:%4.2f profit_cost_ratio:%4.2f" % (item, price['cost'], price['profit'],  (price['profit']/price['cost']) ) )
            



# Edit these following lines to control what is output

find_profits(engineer_rare, "Engineer Rares");
find_profits(nomad_rare, "nomad Rares");
find_profits(lunatic_rare, "Lunatic Rares")
find_profits(scavenger_legendary, "Scavengers rare");

find_profits(nomad_epic, "nomad_epic")
find_profits(lunatic_epic, "lunatic_epic")
find_profits(scavenger_epic, "scavenger_epic")
