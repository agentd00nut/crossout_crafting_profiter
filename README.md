# crossout_crafting_profiter
Always know what item to craft to make the most profit.
Make custom lists of items to track profits for.

![Example Run Of Program](/imgs/Capture.PNG?raw=true "Example Run")


Note: Profit values already account for 10% fee from the market!
Note: Technically if you are renting the workbench for only 5 items at a time you'll want to make sure you are making atleast 5$ of profit on each item you sell... we recommend renting more than 5 at a time.

# How to use

For now you need to manuall edit the lines at the end of the program.
`find_profits(nomad_rare, "nomad Rares");`

The first argument is a list of items you want to find profits for, the second argument is just the name you want to appear before that lists output.

The program only shows profits for items that are positive... So if you make a custom list and none of the items are profitable they won't output.


# Custom list generation.

We use https://www.crossoutdb.com/ to get our data.
Lists are in the format of `"Custom name this doesnt matter":<ITEM ID>`  The item id is the number at the end of this url `https://www.crossoutdb.com/item/31`.
So if you want a list to have the MG13 Equalizer you might do `mylist={"Mg 13 Equalizer!!!!":31}` and feed that to `find_profits(mylist, "My custom list!");`

