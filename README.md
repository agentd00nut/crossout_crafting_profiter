# crossout_crafting_profiter
Always know what item to craft to make the most profit.
Make custom lists of items to track profits for.

![Example Run Of Program](/imgs/Capture.PNG?raw=true "Example Run")


Note: Profit values already account for 10% fee from the market!

Note: Technically if you are renting the workbench for only 5 items at a time you'll want to make sure you are making atleast 5$ of profit on each item you sell... we recommend renting more than 5 at a time.

# How to use

Edit the lines at the end of the program to configure what factions you want to see data for `find_profits(nomad_rare, "nomad Rares");`

The first argument is a list of items you want to find profits for, the second argument is just the name you want to appear before that lists output.

Only positive profit is output.

# What do all these numbers mean?

Cost: This is the cost if you were to buy all the materials required to make this item by right clicking on the required materials and "buying now".

Profit: If you subtract the cost from the current "Sell now" right click option for the crafted item you'd get this number.  The 10% market tax is included so don't take another 10% off of this!

Cost Profit Ratio:  Simply the cost divided by the profit.  Incase you want to "Most effeciently" spend your money.

Realize that the profit reported is WORST CASE scenario.  If you take the time to place the highest buy order and sell your item for the lowest sell order instead of using the right click quick menu you will make anywhere from 10-20% MORE on the item.

Buying from the right click menu means filling the current lowest sell order.  Instead you can use the trade menu to overcut the highest buy order.  Usually the difference between the lowest sell order and highest buy order is >10% since people are trying to buy and sell the items on margin and there is a default 10% tax to sell things on the market.  Thus by trading on the highest buy order you instantly save 10%.
The Same goes for selling your items.  Instead of fulfilling the highest buy order, just undercut everyone by .01 and place the lowest bid order on the market.
This is all a little more work but you'll make a lot more money in the long run.

If you are really in a hurry though you can just use the right click menu and still make the projected profit!

Lastly, realize that this does NOT account for the cost to rent the work bench to craft the item... Its up to you to understand that if you buy 5 work benches and only make $4.00 profit on all 5 items you've just lost $5.


# Custom list generation.

We use https://www.crossoutdb.com/ to get our data.
Lists are in the format of `"Custom name this doesnt matter":<ITEM ID>`  The item id is the number at the end of this url `https://www.crossoutdb.com/item/31`.
So if you want a list to have the MG13 Equalizer you might do `mylist={"Mg 13 Equalizer!!!!":31}` and feed that to `find_profits(mylist, "My custom list!");`

