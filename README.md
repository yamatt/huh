# HUH?
A command line search for Humble Indie bundle games to see if they've gone on sale.

# What?
A Python program that you can use to generate wishlists for the humble bundle. It will search the humble website for the games in your wishlist file, compare them to your specification, such as whether they have Linux, work in Steam and cost below 10USD.

# How?
This is all done in a configuration file that you specify (or exists in your home directory). That file is then used to look up the unofficial API behind Humble and reports on any games that match your minimum criteria.

#Usage
There are two actions to HUH. One is to find the game you want to add so you can get all the relevant details for your wishlist. The second is the matching process that will tell you if a game has met your criteria on the wishlist.
## Searching
To search simply use the following command on your command line:

    huh_search FTL
 
 This will then search for the game FTL and bring back matches in the following format.
 
     FTL: Faster Than Light: (ftlfasterthanlight_storefront) at 5.99GBP

The first part is the "human" name for the game, the one that you recognise. The second part, in brackets is the "machine" name for the game. The one Humble and HUH use to identify the game uniquely in Humble's catalogue of games. The final value is of course the price, in this instance 5.99 pounds.

You can then use this to edit and build your wishlist file.

## Wishlist File
The Wishlist file is a YAML file that contains an array of Game definitions. Here is an example:

    ---
    games:
        - machine_name: ftlfasterthanlight_storefront
          human_name: FTL
          price: 5.00
          currency: GBP
          os: linux
          platform: download

A game dictionary is specified in the file. Then a game. In this game Faster Than Light.

-  `machine_name` this is what is used to identify the game in the search
- `human_name` the criteria used in the search. If this does not find the game in the humble store it cannot perform the matching criteria.
- `price` the maximum price you are willing to pay for the game.
- `currency` and in what currency. The value here is determined by Humble but this is usually your usual currency value. For the USA that is USD, for the UK it is GBP and Europe it is EUR. Be aware if you are searching in another currency Humble may not return that currency to your location and HUH makes no attempt to do any sort of currency conversion.
- `os`this is the operating system the game must run on to meet your criteria. In this example `linux` is specified. Meaning the game won't match in your wishlist unless it runs on Linux. Other values are `osx` and `windows`.
- `platform` this is the distribution channel you wish to download the game on. If you want only non-DRM games then use `download` if you are happy to use Steam then use `steam` here.

## Matching
Matching is done using the following command on your command line.

    huh

This by default (on Linux machines) looks in `~/.huh-wishlist.yaml` for your your wishlist file. You can also specify a particular file (such as in your Dropbox folder) by using the `--wishlist` flag like so:

    huh --wishlist ~/Dropbox/huh-wishlist.yaml

HUH will then go to Humble and request the games based upon your wishlist file to determine if any are on sale. You should get results like this:

	rymdkapsel costs 4.99GBP and runs on mac, linux and windows and is available through download and steam.
	Mini Metro (Early Access) costs 4.49GBP and runs on mac, linux and windows and is available through download and steam.

Which gives you a lot of details about the cost, what the game will run on and how you can get access to it.
