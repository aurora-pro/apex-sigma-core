**Hey there!** We need your **help**! Come support us on [**Patreon**](https://www.patreon.com/ApexSigma)!

## Module Index
- [ADMINISTRATION](#administration)
- [FUN](#fun)
- [GAMES](#games)
- [HELP](#help)
- [INTERACTIONS](#interactions)
- [MATHEMATICS](#mathematics)
- [MINIGAMES](#minigames)
- [MISCELLANEOUS](#miscellaneous)
- [MODERATION](#moderation)
- [MUSIC](#music)
- [NIHONGO](#nihongo)
- [NSFW](#nsfw)
- [PERMISSIONS](#permissions)
- [ROLES](#roles)
- [SEARCHES](#searches)
- [SETTINGS](#settings)
- [STATISTICS](#statistics)
- [UTILITY](#utility)

### ADMINISTRATION
Commands | Description | Example
----------|-------------|--------
`>>addstatus` | Adds a status message to Sigma's database for automatic status rotation. (Bot Owner Only) | `>>ddstatus with tentacles`
`>>announce` | Announces a message to every server that Sigma is connected to. Servers can opt out of this with the noannouncements command. (Bot Owner Only) | `>>nnounce Hello world!`
`>>blacklistmodule` `>>blackmodule` `>>blackmdl` | Disallows a person from using a specific module category. (Bot Owner Only) | `>>lacklistmodule 0123456789 minigames`
`>>blacklistserver` `>>blacklistguild` `>>blacksrv` `>>blackguild` | Marks a server as blacklisted. This disallows any user on that server from using commands. (Bot Owner Only) | `>>lacklistserver 0123456789`
`>>blacklistuser` `>>blackusr` | Marks a user as blacklisted, disallowing them to use any command. (Bot Owner Only) | `>>lacklistuser 0123456789`
`>>destroycurrency` `>>destroykud` `>>descurr` `>>deskud` | Takes away the inputted amount of corrency from the mentioned user. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>estroycurrency 150 @person`
`>>destroyitem` `>>desitem` | Takes away the inputted amount of corrency from the mentioned user. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>estroyitem abcdef1234567890`
`>>eject` | Makes Sigma leave a Discord server. (Bot Owner Only) | `>>ject 0123456789`
`>>evaluate` `>>evaluate` `>>eval` `>>py` `>>python` `>>code` `>>exec` | Executes raw python code. This should be used with caution. (Bot Owner Only) | `>>valuate print('hello world')`
`>>generatecurrency` `>>generatekud` `>>gencurr` `>>genkud` | Awards the mentioned user with the inputted amount of currency. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>eneratecurrency 150 @person`
`>>generateitem` `>>genitem` | Creates and gives an item to the tagged user from the inputted category. (Bot Owner Only) | `>>enerateitem @person plants Blue Delta`
`>>getcommand` `>>getcmd` | Gets command information by the command's statistics ID. (Bot Owner Only) | `>>etcommand 1a2b5c187d13e`
`>>geterror` | Gets an error's details using the given token. (Bot Owner Only) | `>>eterror 9a2e9a374ac90294f225782f362e2ab1`
`>>getreaction` `>>getreact` | No description provided. (Bot Owner Only) | `>>etreaction 4242ea69`
`>>reload` | Reloads all of the modules in Sigma. This includes both commands and events. (Bot Owner Only) | `>>eload`
`>>removereaction` `>>removereact` `>>delreact` | Remove a reaction with the inputed ID. (Bot Owner Only) | `>>emovereaction 1ba2e263f287522f`
`>>removestatus` | Removes a status with the inputed ID from Sigma's status database. (Bot Owner Only) | `>>emovestatus 1d9cae144f`
`>>sabotageuser` `>>sabusr` | Sabotages a user making them have extreme bad luck in various modules. (Bot Owner Only) | `>>abotageuser 0123456789`
`>>send` | Sends a message to a user, channel or server. The first argument needs to be the destination parameter. The destination parameter consists of the destination type and ID. The types are U for User and C for Channel. The type and ID are separated by a colon, or two dots put more simply. (Bot Owner Only) | `>>end u:0123456789 We are watching...`
`>>setavatar` | Sets the avatar of the bot either to the linked or attached image. The officially supported formats for bot avatars are JPG and PNG images. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>etavatar https://my_fomain.net/my_avatar.png`
`>>setstatus` | Sets the current playing status of the bot. To use this, the automatic status rotation needs to be disabled. It can be toggled with the togglestatus command. (Bot Owner Only) | `>>etstatus with fishies`
`>>setusername` | Sets the name of the bot to the inputted text. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>etusername Supreme Bot`
`>>shutdown` | Forces the bot to disconnect from Discord and shut down all processes. (Bot Owner Only) | `>>hutdown`
`>>sysexec` `>>sh` | Executes a shell command. Extreme warning! (Bot Owner Only) | `>>ysexec echo 'Hello'`
`>>test` | For testing purposes, obviously. Used as a placeholder for testing functions. | `>>est`
`>>togglestatus` | Toggles if the automatic status rotation is enabled or disabled. (Bot Owner Only) | `>>ogglestatus`
`>>wipeawards` | Removes a user's currency, experience and cookie data. Used when wanting to remove a blacklisted user's ill gotten gains. (Bot Owner Only) | `>>ipeawards 0123456789`
[Back To Top](#module-index)

### FUN
Commands | Description | Example
----------|-------------|--------
`>>award` `>>pay` | Awards a chosen amount of Kud from the vault to a targeted person. The amount of Kud needs to go first, followed by the target. Only server managers can award Kud from the vault. Anybody can contribute to the vault with the givetovault command. | `>>ward 500 @person`
`>>bash` | If you are old enough to know what IRC is or remember how it looked like, then you will appreciate the quotes that the bash command produces. | `>>ash`
`>>cat` | Outputs a random cat image. Furry felines like it when their owners observe them. | `>>at`
`>>catfact` | Outputs a random fact about your lovely furry assh~ Eerrrr... I mean, companion! | `>>atfact`
`>>chucknorris` | This command outputs a random Chuck Norris joke. We use Chuck jokes because Bruce Lee is no joke, obviously. | `>>hucknorris`
`>>cookies` | Shows how many cookies you have, or how many a mentioned user has. | `>>ookies @person`
`>>csshumor` | The only thing better than a joke is a joke written in CSS. And while that is sarcasm to a certain degree, these really are fun. Embrace your web designer within and read some CSS jokes. | `>>sshumor`
`>>cyanideandhappiness` `>>cnh` | Outputs an image of a random Cyanide and Happiness comic. Explosm makes awesome comics and animations. | `>>yanideandhappiness`
`>>dab` | Pseudo-dank metrics or whatever. | `>>ab`
`>>dadjoke` | This will provide a joke that might be something your father would say. You know they are bad, but you will love them anyway, cause you are a good kid. | `>>adjoke`
`>>dog` | Outputs a random dog image. Cutest, loyalest little woofers. | `>>og`
`>>dogfact` `>>doggofact` | Outputs a random fact about the man's best friend. | `>>ogfact`
`>>emote` `>>emoji` `>>em` | Searches for an emoji by name. Additionally, you can search for a specific emoji using an ID like this lcPain:309405155298639872 | `>>mote lcPain`
`>>famousquote` `>>fquote` | Gives you a random inspirational or deep quote. | `>>amousquote`
`>>fortune` `>>fortune-mod` | Linux users, and raw UNIX users in general will know the fortune-mod. This command uses their entire database to output one of their quotes. | `>>ortune`
`>>givecookie` `>>gibcookie` | Gives a cookie to a person. Remember to give them to only nice people. You can give only one cookie every hour. | `>>ivecookie @person`
`>>givecurrency` `>>givecurr` `>>givekud` | Transfers Kud between you and a targetted person. | `>>ivecurrency 100 @person`
`>>givetovault` `>>givetobank` `>>gtv` `>>gtb` | The vault is a server specific Kud storage system. Members can contribute to the vault with this command. The kud can then be awarded to users using the award command. | `>>ivetovault`
`>>joke` | Outputs a joke. It is not really special or anything... Sometimes they are funny, most of the times they are not. | `>>oke`
`>>kitsunemimi` `>>kon` `>>fluffytail` | Displays a random kitsunemimi image. In case you don't know what a kitsunemimi is, it's a foxgirl. All images are sourced from Safebooru, but due to some being borderline. The command rating is naturally set to "Borderline". | `>>itsunemimi`
`>>leetspeak` `>>leet` `>>l33t` | Turns your inputted statement into l33t text. You can add which level of leet you want your text to be converted to. As it's displayed in the usage example. The accepted levels are basic, advanced and ultimate. | `>>eetspeak owned level:ultimate`
`>>nekomimi` `>>neko` `>>nyaa` | Displays a random nekomimi image. In case you don't know what a nekomimi is, it's a catgirl. All images are sourced from Safebooru, but due to some being borderline. The command rating is naturally set to "Borderline". | `>>ekomimi`
`>>numberfact` `>>numfact` `>>numf` | Searches for interesting things about a given number. You can also insert a date in the DAY/MON format. You can specify a type of number you want retrived in the format TYPE:NUMBER. The allowed types are trivia, math, date, year. You can also specify "random" instead of a number to make it a random number. | `>>umberfact 42`
`>>pun` | If you do not know what a pun is... Oh you poor innocent soul. This command will produce a lovely little pun for you. Enjoy the cringe! | `>>un`
`>>randomcomicgenerator` `>>rcg` | Uses the Cyanide and Happiness random comic generator for buttloads of fun. Personally the favorite comic command. | `>>andomcomicgenerator`
`>>reversetext` `>>reverse` | Reverses the text that you input into the command. | `>>eversetext hello`
`>>ronswanson` | Everyone's favorite character from Parks and Recreation. This command will output a random quote from Ron Swanson. | `>>onswanson`
`>>vault` `>>bank` | Shows the current amount of Kud in the guild's vault. | `>>ault`
`>>visualnovelquote` `>>vnquote` `>>vnq` | Outputs a random quote from a random VN. Displays it's source as well, of course. | `>>isualnovelquote`
`>>xkcd` | If you like humorous things and know a bit of technology, you will lose a lot of time reading these. XKCD comics are perfect for procrastination and time wasting. | `>>kcd`
`>>yomomma` `>>yomama` `>>yomoma` `>>ym` | Want to insult some poor fool's mother but don't have the right comeback? This command will provide the perfect yo momma joke for the task. | `>>omomma`
[Back To Top](#module-index)

### GAMES
Commands | Description | Example
----------|-------------|--------
`>>bhranking` `>>bhlb` `>>brawlhallaleaderboad` `>>brawlhallaranking` | Grabs the current top players on the Brawlhalla leaderboards. You can append a region to the command to get the leaderboard for that region. If no region is specified, it will use the global ranking page. | `>>hranking EU`
`>>fireemblemheroes` `>>feh` | Searches data in the Fire Emblem Heroes game. Such as hero, weapon and skill information. | `>>ireemblemheroes Ninian`
`>>osu` | Generates a signature image with the users stats for osu. | `>>su AXAz0r`
`>>overwatch` `>>owstats` `>>ow` | Outputs the Overwatch statistics for the given player from the given region. Do note that the battletag is case sensitive, Aurora#22978 is not the same as aurora#22978 | `>>verwatch EU Aurora#22978`
`>>wfalertchannel` `>>wfac` | Designates a channel for Warframe alerts. When a new alert shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>falertchannel #wf-alerts`
`>>wfalerts` `>>wfa` | Shows the currently ongoing alerts in Warframe. As well as their respective rewards. | `>>falerts`
`>>wffissurechannel` `>>wffc` | Designates a channel for Warframe void fissures. When a new void fissure shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>ffissurechannel #wf-fissures`
`>>wffissures` `>>wffissure` `>>wff` | Shows the current fissure locations in Warframe. As well as their tiers, locations and mission types. | `>>ffissures`
`>>wfinvasionchannel` `>>wfic` | Designates a channel for Warframe invasions. When a new invasion shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>finvasionchannel #wf-invasions`
`>>wfinvasions` `>>wfinvasion` `>>wfi` | Shows the current ongoing invasions in Warframe. As well as their factions, locations and rewards. | `>>finvasions`
`>>wfnews` `>>wfn` | Shows the current ative news in Warframe. | `>>fnews`
`>>wfnewschannel` `>>wfnc` | Designates a channel for Warframe news. When Digital Extremes posts a new event for Warframe, it pops up there. To disable this, write disable after the command instead of a channel. | `>>fnewschannel #wf-news`
`>>wfplainsofeidolon` `>>wfpoe` | Shows the current time on the Plains of Eidolon in warframe. As well as the next day/night cycle rotations. You can add "exact" as a command arguement. This will make the time cycle responses appear in the H:M:S format. | `>>fplainsofeidolon exact`
`>>wfpricecheck` `>>wfpc` `>>wfmarket` | Checks the price for the searched item. This will only list items by members that are currently online and in the game. | `>>fpricecheck Blind Rage`
`>>wfsortie` `>>wfsorties` `>>wfs` | Shows the ongoing sortie missions in Warframe. | `>>fsortie`
`>>wfsortiechannel` `>>wfsc` | Designates a channel for Warframe sorties. When a new sortie shows up the news will be posted there. To disable this, write disable after the command instead of a channel. | `>>fsortiechannel #wf-sorties`
`>>wftag` `>>wftagrole` `>>wfnotify` `>>wfbind` | Binds a certain keyword from alerts and invasions. When this keyword appears during an event all roles bound to it's triggers will be mentioned. | `>>ftag aura Aura Squad`
`>>wftrials` `>>wftrial` `>>wfraids` `>>wfraid` `>>wft` `>>wfr` | Shows raid statistics for the inputted username. Note that DE hasn't been tracking this data forever. So some really old raids won't be shown due to having no data. The shortest raid time shown only counts victorious raids. | `>>ftrials AXAz0r`
`>>worldofwarships` `>>wows` | Grabs the player statistics for the game World of Warships. First the region and then the username. | `>>orldofwarships EU AXAz0r`
[Back To Top](#module-index)

### HELP
Commands | Description | Example
----------|-------------|--------
`>>commands` | Shows the commands in a module group category. To view all the module group categories, use the modules command. | `>>ommands minigames`
`>>donate` | Shows donation information for Sigma. | `>>onate`
`>>help` | Provides the link to Sigma's website and support server. As well as show information about a command if something in inputted. | `>>elp fish`
`>>modules` | Shows all the module categories. | `>>odules`
[Back To Top](#module-index)

### INTERACTIONS
Commands | Description | Example
----------|-------------|--------
`>>addreact` | Adds new reactions. | `>>ddreact reaction my.gif.link/fancy.gif`
`>>bite` | Sink your teeth into some poor thing. | `>>ite @person`
`>>cry` | Somebody is making you sad, let them know that with crocodile tears! | `>>ry @person`
`>>cuddle` | Snuggle, snuggle~ | `>>uddle @person`
`>>dance` | Feel alive? Like you just wanna... boogie? Let's dance! | `>>ance @person`
`>>drink` | Cheers, family! Let's get drunk! | `>>rink @person`
`>>explode` `>>detonate` | When all other means fail, it's time to bring out the carpet bomb squadrons. | `>>xplode @person`
`>>facepalm` | Somebody just did something so stupid you want to facepalm. | `>>acepalm @person`
`>>fap` | When you can't get that good-good, you gotta fap to them ԅ(¯﹃¯ԅ) | `>>ap @person`
`>>feed` | Care to share some of your food with someone cute? | `>>eed @person`
`>>fuck` | Don't question my modules... Yes (º﹃º) | `>>uck @person`
`>>fuckrl` | The same as fuck, but for non-weebs, the RL stuff... STOP JUDGING ME (ﾟ￢ﾟ) | `>>uckrl @person`
`>>hug` | Even a bot like me can appreciate a hug! The person you mention will surely as well. | `>>ug @person`
`>>kiss` | Humans touching their slimy air vents. How disturbing. | `>>iss @person`
`>>lick` | Doesn't someone sometimes look so cute that you just want to lick them? Or maybe they have some food on their face, it's a good excuse. | `>>ick @person`
`>>lovecalculator` `>>lovecalc` | Shows the love between two tagged users. | `>>ovecalculator @person1 @person2`
`>>pat` | Pat, pat~ Good human, lovely human. I will kill you last. | `>>at @person`
`>>peck` | A hit and run style quickie kiss. | `>>eck @person`
`>>poke` | Poke, poke~ Are you alive? | `>>oke @person`
`>>pout` | Make a pouty face at someone and make them change their mind. Or just teast them for being a horrible person. Like when they make you create a pout command for money! | `>>out @person`
`>>punch` | You have something on your face. IT WAS PAIN! | `>>unch @person`
`>>shoot` | When a damn knife isn't enough. | `>>hoot @person`
`>>shrug` | I don't get it, or I don't care, really whatever *shrug*. | `>>hrug @person`
`>>sip` | Ahh yes, i know the feeling of wanting to sit outside on a chilly morning sipping hot tea. | `>>ip @person`
`>>slap` | When a punch is too barbaric a slap should be just elegant enough. | `>>lap @person`
`>>stab` | Boy... Somebody really has you pissed off if you are using this one. | `>>tab @person`
`>>stare` | Jiiiiiiiiiii~ | `>>tare @person`
[Back To Top](#module-index)

### MATHEMATICS
Commands | Description | Example
----------|-------------|--------
`>>checkheartkey` `>>chk` | Checks if the key you have inputted is the heart key of Sigma. If the key inputted has at least part of the true key, it will say so. | `>>heckheartkey b7V01YuKJ7Le1FQSZS_gvPtvI9kFa0ZDHH_-QfzZsFA=`
`>>collectchain` | Collects messages sent by the mentioned user and saves it as a chain. Only one person can use the command at the time due to the processing load it takes. | `>>ollectchain @person #channel`
`>>combinechains` `>>combine` `>>cmbch` `>>mix` | Like the impersonate command. This one however targets two uers and uses their chains to generated a mixed response. | `>>ombinechains @target_one @target_two`
`>>currenttime` `>>time` | Shows the current time in UTC. You can specify a time zone as well. If you wish to convert time, use the timeconvert command. | `>>urrenttime PDT`
`>>decrypt` | Decrypts any message that was encrypted using the Sigma Heart Key. You can add ":t" at the end to force it to be raw text instead of an embed. | `>>ecrypt H7U2JfWkr0zCApDPDkO`
`>>dokidoki` `>>doki` `>>dd` | Makes a random markov chain based sentence from a random Doki Doki Literature Club character quote. You can force which character to quote by adding their name as an argument to the command. And you can force a glitch by adding ":glitch" as the ending argument. | `>>okidoki`
`>>encrypt` | Encrypts the message of your choice using the Sigma Heart Key. The message can be decrypted using the decrypt command. You can add ":t" at the end to force it to be raw text instead of an embed. | `>>ncrypt I will always be here to talk to you for as long as you want.`
`>>impersonate` `>>mimic` | Tries to impersonate the mentioned user if a chain file for them exists. This command is on a 20 second cooldown due to it's weight. | `>>mpersonate @person`
`>>makehash` `>>hash` | Creates a hash using the inputed has type. These are all the hash types you can use. sha512, sha3_224, sha3_512, MD4, dsaWithSHA, ripemd160, RIPEMD160, SHA, ecdsa-with-SHA1, sha3_384, SHA512, sha1, SHA224, md4, DSA-SHA, SHA384, blake2b, dsaEncryption, SHA256, sha384, sha, DSA, shake_128, sha224, SHA1, shake_256, sha256, MD5, blake2s, md5, sha3_256, whirlpool | `>>akehash md5 Nabzie is best tree.`
`>>timeconvert` `>>tconv` | Converts the given time in the given time zone to the inputted time zone. | `>>imeconvert 18:57 UTC>PST`
`>>wipechain` `>>clearchain` | It wipes your entire Markov chain, if you have one. | `>>ipechain`
`>>wolframalpha` `>>wa` | Makes a request for Wolfram Alpha to process. This can be a lot of things, most popular being complex math operations. | `>>olframalpha 69+42`
[Back To Top](#module-index)

### MINIGAMES
Commands | Description | Example
----------|-------------|--------
`>>animechargame` `>>anichargame` `>>anicg` | A minigame where you guess the name of the anime character shown. You can add "hint" in the command to make it show the character's scrambled name. The Kud reward is equal to the number of characters of the shortest part of the characters name. If the hint is used, the Kud reward is split in half. | `>>nimechargame hint`
`>>buyupgrade` `>>shop` | Opens Sigma's profession upgrade shop. | `>>uyupgrade`
`>>coinflip` `>>cf` | Flips a coin. Nothing complex. You can try guessing the results by typing either Heads or Tails. | `>>oinflip Heads`
`>>cook` `>>make` | Uses a recipe to create an item from raw resources that you've gathered. You can see all available recipes with the recipes command. | `>>ook Shade Tea`
`>>eightball` `>>8ball` | The 8Ball has answers to ALL your questions. Come one, come all, and ask the mighty allknowing 8Ball! Provide a question at the end of the command and await the miraculous answer! | `>>ightball Will I ever be pretty?`
`>>filtersell` `>>fsell` | Sells all items that have a certain attribute. The accepted attributes are name, type and rarity. | `>>iltersell rarity:Legendary`
`>>finditem` | Looks up information about an item. The first argument needs to be the item type. For example if it is a fish, meat, plant or material. And the rest is the name of the item. | `>>inditem fish Jitteroon`
`>>fish` | Cast a lure and try to catch some fish. You can fish once every 60 seconds, better not scare the fish away. | `>>ish`
`>>forage` | Go hiking and search nature for all the delicious bounties it has. Look for plants that you might want to use for cooking in the future. Foraging is tiring so you need to rest for 60 seconds after looking for plants. | `>>orage`
`>>hunt` | Go into the wilderness and hunt for game. You can hunt once every 60 seconds, everyone needs rest. | `>>unt`
`>>inspect` | Inspects an item that is in your inventory. | `>>nspect Nabfischz`
`>>inventory` `>>bag` `>>storage` `>>backpack` | Shows your current inventory. The inventory has 64 slots at the start but can be upgraded. You can also specify the page number you want to see. The inventory is sorted by item rarity. | `>>nventory 2 @person`
`>>inventorystats` `>>invstats` `>>bagstats` | Shows the statistics of a user's inventory. The number of items per type and per rarity. | `>>nventorystats @person`
`>>joinrace` `>>jr` | Joins a race instance if any are ongoing. | `>>oinrace`
`>>mathgame` `>>mg` | A mathematics minigame. You are given a problem, solve it. Numbers are rounded to 2 decimals. You can also specify how hard you want the problem to be. The scale goes from 1-9. The default difficulty is 3. The time and Kud reward scale with the difficulty and number of hard operators. | `>>athgame 4`
`>>quiz` | A quiz minigame with various quizzes to choose from. With a lot more coming soon | `>>uiz`
`>>race` | Creates a race in the current text channel. To join the race use the joinrace command. A race needs at least 2 people to start, and has a maximum of 10 participants. You can specify a required buy-in to join the race. The winner gets the entire pool minus 10% that goes to the track upkeep. | `>>ace 20`
`>>raceoverride` `>>raceover` | Overrides the race in case a bug occurs. | `>>aceoverride`
`>>recipes` | Lists all recipes available for making. The recipe list is limited to 10 items per page. You can specify the number of the page that you want to view. | `>>ecipes`
`>>roll` `>>dice` | Gives a random number from 0 to 100. You can specify the highest number the function calls by adding a number after the command. The Number TECHNICALLY does not have a limit but the bigger you use, the bigger the message, which just looks plain spammy. | `>>oll 501`
`>>rps` `>>rockpaperscissors` | Play Rock-Paper-Scissors with the bot. No cheating, we swear. Maybe she just doesn't like you. | `>>ps s`
`>>sell` | Sells an item from your inventory. Input all instead of the item name to sell your entire inventory. | `>>ell Copula`
`>>sequencegame` `>>sequence` `>>sqcg` | Starts a sequence guessing game. 4 symbols will randomly be chosen and you have to guess them in 6 tries or fewer. When a symbol is in the corret position the diamond will be blue. If it is in the sequence but incorrect position, it will be yellow. If the symbol is not in the sequence, a red triangle will be shown. The symbols can repeat, the Kud award is 50. | `>>equencegame`
`>>slots` | Spin the slot machine, maybe you win, maybe you don't. Who knows? It costs 10 Kud to spin the slot machine by default. But you can specify how much you want to put in the machine. And the rewards are based on how many of the same icon you get in the middle row. Rewards are different for each icon. The slots can be spun only once every 60 seconds. | `>>lots 52`
`>>trivia` `>>triv` `>>t` | A trivia minigame. You are given a question and have to input the number of your answer. Guess correctly and you win 5-15 Kud, depending on the difficulty. You have 20 seconds to answer the question. | `>>rivia`
`>>unscramble` `>>usg` | A minigame where you guess the scrambled word. You have 30 seconds to guess the word shown. The Kud reward is equal to the number of letters in the word. | `>>nscramble`
`>>upgrades` | Shows the user's current upgrades. You can view another person's upgrades by tagetting them. | `>>pgrades @person`
`>>viewrecipe` `>>recipe` `>>vrec` | Shows information about a recipe. Such as the ingredients required, value of the item, and it's description. | `>>iewrecipe Shade Tea`
`>>vnchargame` `>>vncg` | A minigame where you guess the name of the visual novel character shown. You can add "hint" in the command to make it show the character's scrambled name. The Kud reward is equal to the number of characters of the shortest part of the characters name. If the hint is used, the Kud reward is split in half. | `>>nchargame`
[Back To Top](#module-index)

### MISCELLANEOUS
Commands | Description | Example
----------|-------------|--------
`>>afk` | Sets you as afk. Whenever someone mentions you they will be notified that you are afk. When you send a message your afk status will be removed. This automatic removal ignores messages that start with the command prefix. | `>>fk Sleeping or eating, probably both!`
`>>choose` | The bot will select a thing from the inputed list. Separate list items with a semicolon and space. | `>>hoose Sleep; Eat; Code; Lewd Stuff`
`>>httpstatus` `>>http` | Shows information about a HTTP response status code. | `>>ttpstatus 404`
`>>myreminders` `>>reminders` `>>rms` | Shows a list of the reminders that you have created. The location where they are set to execute in. And in what time they execute in. If you add "here" to the end of the command, it will only show reminders made in the current channel. | `>>yreminders here`
`>>poll` | Creates a poll with the items from the inputted list. Separate list items with a semicolon and a space. | `>>oll Want to eat?; Yes; No; Hand me the cheese!`
`>>quote` | Quotes a message from it's given ID. | `>>uote 381449702589202432`
`>>randombetween` `>>ranin` | Outputs a random number between two inputted numbers. | `>>andombetween 59 974`
`>>reminderinfo` `>>reminder` `>>rminfo` `>>rmi` | Shows information about your reminder with the given ID. Such as when it executes and where. | `>>eminderinfo f93f`
`>>remindme` `>>remind` `>>setreminder` `>>alarm` `>>rmme` | Sets a timer that will mention the author when it's done. The time format is H:M:S, but is not limited to the constraints of their types. Meaning you can type "200:5000:999999" if you wish. Reminders are limited to 90 days, and you are limited to 15 reminders. | `>>emindme 1:03:15 LEEEEROOOOY JEEEEEENKIIIIINS!`
`>>removereminder` `>>delreminder` `>>delrm` | Deletes a reminder of yours with the inputted ID. | `>>emovereminder 1a9e`
`>>shadowpoll` | Makes a private shadow poll. The user that voted on the shadow poll can only be seen by it's creator. Additional commands can set an expiration timer for the shadow poll and the visibility of the poll's current vote count and percentages. | `>>hadowpoll Ban Nuggetlord?; Yes; Yes; Yes; No; Soft`
`>>shadowpollclose` `>>spclose` | Closes/deactivated a shadow poll. Closed polls can not be voted on and can not be viewed unless they are set to be visible. | `>>hadowpollclose 1bca22`
`>>shadowpolldelete` `>>spdelete` `>>spdel` | Permanently deletes a shadow poll. | `>>hadowpolldelete 1bca22`
`>>shadowpollexpires` `>>spexpiration` `>>spexpires` `>>spexpire` | Sets a poll to automatically close after the given time elapses. The time to close is counted from the command execution, not the initial opening of the poll. When the poll expires the author will be notified of the expiration. Only the poll's creator can edit it's expiration time. | `>>hadowpollexpires 1bca22 48:30:59`
`>>shadowpollinvisible` `>>spinvisible` `>>spinvis` | Reverts a shadow poll back to invisible. Making it's statistics only accessible to the author. All shadow polls are invisible by default. | `>>hadowpollinvisible 1bca22`
`>>shadowpolllist` `>>splist` | Lists all shadow polls that you have created. You can also list the polls that are active and created in the current server or channel by adding a "server" or "channel" argument to the command. Polls that have expired or that are closed are marked with an exclamation mark. | `>>hadowpolllist channel`
`>>shadowpollopen` `>>spopen` | Opens a previously closed poll. If the poll has an expiration timer, it will be wiped. | `>>hadowpollopen 1bca22`
`>>shadowpollpermit` `>>sppermit` `>>spperm` | Permits a role, channel or user to vote in the poll. If no permission settings are set, anybody can vote on the poll. If any permissions are set, only items permitted can vote in the poll. Tag a user to permit a user, tag a channel to permit a channel, or type the name of the role you want to permit. | `>>hadowpollpermit 1bca22 #council`
`>>shadowpollstats` `>>spstats` | Shows statistics for the given poll. Total count of votes and votes for each option as well as percentages. | `>>hadowpollstats 1bca22`
`>>shadowpollunpermit` `>>spunpermit` `>>spunperm` | Unpermits a previously permitted object from voting on the poll. For more information check the description of the sppermit command. | `>>hadowpollunpermit 1bca22 Disowned`
`>>shadowpollview` `>>spview` | Displays a shadow poll's question and possible options. If the poll is not active and not finished, information will not be displayed. Unless of course the one who uses the view command is the poll's creator. | `>>hadowpollview 1bca22`
`>>shadowpollvisible` `>>spvisible` `>>spvis` | Marks a poll as visible. If a poll is visible anybody can see it's statistics. Such as total vote count and how many votes go to each choice. | `>>hadowpollvisible 1bca22`
`>>shadowpollvote` `>>spvote` | Votes on a shadow poll. Choosing multiple options is not allowed. Re-using the command will result in your vote being changed. | `>>hadowpollvote 1bca22`
`>>shadowpollvoters` `>>spvoters` | Shows all the users that voted on a shadow poll and what they voted on. This command can only be used by the author of the poll. | `>>hadowpollvoters 1bca22`
`>>shadowpollwipe` `>>spwipe` | Completely resets a poll's statistics. Deleting all the data about who voted for what option. | `>>hadowpollwipe 1bca22`
[Back To Top](#module-index)

### MODERATION
Commands | Description | Example
----------|-------------|--------
`>>ban` | Bans a user from the server. This will also remove all messages from that user in the last 24h. The user can only be targeted by a mention tag. This is to preserve compatibility with logging and audits. | `>>an @person Way, WAY too spicy for us...`
`>>hardmute` `>>hmute` | Hard-mutes the target user. Users who are hard-muted are disallowed from typing to any channel. There is no message deletion, this is a permission based mute. | `>>ardmute @person For talking about the fight club.`
`>>hardunmute` `>>hunmute` | Unmutes a hard-muted person. Allowing them to send messages again. | `>>ardunmute @person`
`>>kick` | Kicks a user from the server. The user can only be targeted by a mention tag. This is to preserve compatibility with logging and audits. | `>>ick @person Couldn't handle the spice.`
`>>purge` `>>prune` | Deletes X number of messages posted by the mentioned person. If a user is not provided, it will prune the last X messages regardless of poster. If a number is not provided it will prune the last 100 messages. If neither number nor user is provided, it will prune the bots messages. Requires the user who calls the command to have the Manage Messages permission. | `>>urge X @person`
`>>softban` `>>sb` | Soft-Ban a user from the server. This bans the user and immediatelly unbans them. Useful if you want to purge all messages from that user in the last 24h. The user can only be targeted by a mention tag. This is to preserve compatibility with logging and audits. | `>>oftban @person Some spice needed de-spicing.`
`>>textmute` `>>tmute` | Disallows the user from typing. Well technically, it will make the bot auto delete any message they send. You can add a message at the end to be sent to the user as the reason why. | `>>extmute @person Was too spicy!`
`>>textunmute` `>>tunmute` | Removes the tagged person from the list of muted users. Making the bot no longer delete their messages. | `>>extunmute @person`
`>>unban` | Unbans a banned user by inputted username. | `>>nban Chicken Shluggets`
`>>unwarn` `>>clearwarnings` `>>clearwarns` | Clears a user's warning. A user target and warning ID are required. You can input "all" instead of an idea to clear all their warnings. | `>>nwarn @person all`
`>>warn` | Adds a user to the warning list along with the reason stated. The used will also receive a direct message from the bot stating they have been warned. Warnings can be cleared with the unwarn command. | `>>arn @person Bit my dog`
`>>warning` `>>warninfo` | Shows information regarding a user's warning. Both the mention of the user and the warning ID are required. | `>>arning @person 12af`
`>>warnings` `>>warns` | Shows what the mentioned user was warned for. If the user who calls the command doesn't have the manage message permission, it will show their warnings instead. | `>>arnings @person`
[Back To Top](#module-index)

### MUSIC
Commands | Description | Example
----------|-------------|--------
`>>disconnect` `>>stop` | Stops the music, disconnects the bot from the current voice channel, and purges the music queue. | `>>isconnect`
`>>nowplaying` `>>currentsong` `>>playing` `>>np` | Shows information regarding the currently playing song. | `>>owplaying`
`>>pause` | Pauses the music player. | `>>ause`
`>>play` `>>start` | Starts playing the music queue. | `>>lay`
`>>queue` `>>add` | Queues up a song to play from YouTube. Either from a direct URL or text search. Playlists are supported but take a long time to process. | `>>ueue Kaskade Disarm You Illenium Remix`
`>>repeat` | Toggles if the current queue should be repeated. Whenever a song is played, it's re-added to the end of the queue. | `>>epeat`
`>>resume` | Resumes the music player. | `>>esume`
`>>shuffle` | Randomizes the current song queue. | `>>huffle`
`>>skip` `>>next` | Skips the currently playing song. | `>>kip`
`>>summon` `>>move` | If the bot isn't connected to any channel, it'll connect to yours. If it is connected, it will move to you. | `>>ummon`
`>>unqueue` `>>remove` | Removes a song from the queue. Minimum number is 1 and the maximum is however many items the queue has. Even though list indexes start at zero. | `>>nqueue 5`
[Back To Top](#module-index)

### NIHONGO
Commands | Description | Example
----------|-------------|--------
`>>jisho` | Searches Jisho, which is the Japanese language dictionary, for your input. Resulting in a display of various types of information regarding your lookup. | `>>isho Kawaii`
`>>wanikani` `>>wk` | Shows the mentioned person's WaniKani statistics. If no person is mentioned it will show the author's stats. This requires the person to have a WaniKani API key stored with the wksave command. | `>>anikani @person`
`>>wanikanisave` `>>wksave` | Saves your WaniKani API key in the database so the wanikani command can be used. | `>>anikanisave 123456798`
[Back To Top](#module-index)

### NSFW
Commands | Description | Example
----------|-------------|--------
`>>boobs` `>>tits` | Outputs a random NSFW image focusing on the breasts of the model. | `>>oobs`
`>>butts` `>>ass` | Outputs a random NSFW image focusing on the ass of the model. | `>>utts`
`>>danbooru` `>>danb` | Searches Danbooru for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>anbooru kawaii`
`>>e621` | Searches E621 for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>621 knot`
`>>keyvis` | This command returns a Key Visual Arts VN CG. It picks a random VN and a random CG from that VN. You can specify the VN you want the CG to be from. "kud" - Kud Wafter "air" - Air "kanon" - Kanon "little" - Little Busters "clan" - Clannad "plan" - Planetarian "rewr" - Rewrite "harv" - Rewrite Harvest Festa This command is rated explicit due to some CGs being explicit.  | `>>eyvis kud`
`>>konachan` `>>kchan` | Searches Konachan for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>onachan thighhighs`
`>>rule34` `>>r34` | Searches Rule34 for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>ule34 switch`
`>>xbooru` `>>xb` | Searches Xbooru for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>booru ovum`
`>>yandere` `>>yre` | Searches yandere for the given tag. If no tag is given, the keyword "nude" will be used. As on all image galleries, tags are bound with a "+". If your search has spaces replace them with underscores "_". | `>>andere naked_apron`
[Back To Top](#module-index)

### PERMISSIONS
Commands | Description | Example
----------|-------------|--------
`>>disablecommand` `>>dcmd` `>>cmdoff` `>>commandoff` | Disallows a command to be used on the server. Disabled commands are then overwritten by one of the permit commands. Those with the Administrator permission are not affected. | `>>isablecommand nyaa`
`>>disablemodule` `>>dmdl` `>>mdloff` `>>moduleoff` | Disallows an entire module to be used on the server. Disabled modules are then overwritten by one of the permit commands. Those with the Administrator permission are not affected. | `>>isablemodule fun`
`>>enablecommand` `>>cmdon` `>>commandon` | Enables a previously disabled command. | `>>nablecommand kitsune`
`>>enablemodule` `>>mdlon` `>>moduleon` | Enables a previously disabled module. | `>>nablemodule minigames`
`>>permitchannel` | Allows a previously disabled command or module to be used in the specified channel. Follow the usage example, C for command, M for module. | `>>ermitchannel m:fun #channel`
`>>permitrole` | Specifies a role that can use a disabled command or module group. It needs to be specified if it is a command or module group. If it is a command use C and if it is a module use M following the example. | `>>ermitrole c:csshumor Wizards`
`>>permituser` | Specifies a user that can use a disabled command or module. It needs to be specified if it's a command or module group. If it is a command use C, if it is a module use M, following the usage example. | `>>ermituser c:pun @person`
`>>unpermitchannel` | Removes the channel override for a disabled command or module. Follow the usage example, C for command, M for module. | `>>npermitchannel m:fun #channel`
`>>unpermitrole` | Removes permissions from a role that can use a disabled command or module group to do so. It needs to be specified if it is a command or module group. If it is a command use C and if it is a module use M following the example. | `>>npermitrole m:minigames Gamblers`
`>>unpermituser` | Unpermits a user from using a previously overridden command or module. It needs to be specified if it's a command or module group. If it is a command use C, if it is a module use M, following the usage example. | `>>npermituser m:fun @person`
[Back To Top](#module-index)

### ROLES
Commands | Description | Example
----------|-------------|--------
`>>addselfrole` `>>addrank` `>>asr` | Sets a role as self assignable. Roles that are self assignable, any user can assign to themselves. To assign a self assignbale role to yourself, use the togglerole command. | `>>ddselfrole Cheese Lover`
`>>autorole` `>>autorank` | Sets which role should be given to joining members. When a new user enters the server, this role will be assigned to them. The role can not be something that is above the bot's highest role. If you want to disable the autorole, input "disable" as the role name. | `>>utorole Newcomer`
`>>delselfrole` `>>delrank` `>>rsr` `>>dsr` | Removes a role from the list of self assignable roles. | `>>elselfrole Meat Lover`
`>>giverole` `>>giverank` `>>grole` `>>grank` | Gives the inputed role to the tagged user. The role must be below Sigma in Discord hierarchy. | `>>iverole @person Grandma`
`>>listselfroles` `>>listranks` `>>listroles` `>>ranks` `>>roles` `>>lsrl` | Lists all self assignable roles present on the server. | `>>istselfroles`
`>>removerole` `>>removerank` `>>rrole` `>>rrank` | Removes the inputed role from the tagged user. The role must be below Sigma in Discord hierarchy. | `>>emoverole @person Wangly`
`>>togglerole` `>>togglerank` `>>rank` `>>trl` | Toggles a self assignable role. If you don't have the role, it will be given to you. If you do have the role, it will be removed from you. | `>>ogglerole Overlord`
[Back To Top](#module-index)

### SEARCHES
Commands | Description | Example
----------|-------------|--------
`>>anime` `>>animu` `>>kitsuanime` | Searches Kitsu.io for the inputted anime. The outputed results will be information like the number of episodes, user rating, air time, plot summary, and poster image. | `>>nime Plastic Memories`
`>>antonyms` `>>antonym` `>>ant` | Looks up words that have opposite meanings for the given term. | `>>ntonyms late`
`>>cryptocurrency` `>>cryptocur` `>>crypcur` `>>ecoin` | Shows the statistics for the imputted crypto currency. Stats include the current market cap, price, supply, volume, change. | `>>ryptocurrency ethereum`
`>>deezer` `>>music` `>>findsong` | Searches Deezer for infomation on the given song. The output will include a song preview link. | `>>eezer Highway to Hell`
`>>describe` `>>desc` | Looks up words that are often used to describe nouns or are often used by the adjective. Specify the mode in the first argument. adjectives, adjective, adj, a: To look up nouns that are often described by an adjective. nouns, noun, n: To look up adjectives that are often used to describe a noun.  | `>>escribe noun ocean`
`>>dictionary` `>>dict` `>>definition` `>>define` `>>def` | Searches the Oxford dictionary for the definition of your input. | `>>ictionary cork`
`>>foodrecipe` `>>frec` `>>food` | Searches for a dish, or dishes that use inputted ingredients, and outputs one that might be a good match for your search query. | `>>oodrecipe Chicken in Curry Sauce`
`>>homophones` `>>homophone` | Looks up words that sound like the given one. | `>>omophones coarse`
`>>imdb` `>>movie` | Searches the Internet Movie DataBase for your input. Gives you the poster, release year and who stars in the movie, as well as a link to the page of the movie. | `>>mdb Blade Runner`
`>>manga` `>>mango` `>>kitsumanga` | Searches Kitsu.io for the inputted manga. The outputed results will be information like the number of chapters, user rating, plot summary, and poster image. | `>>anga A Silent Voice`
`>>mapsearch` `>>maps` `>>map` | Searches Google Maps for the inputted location. If specific details aren't found about the location, it will result in a broad search.  | `>>apsearch Belgrade`
`>>reddit` | Enter a subreddit and it will show a random post from the current top posts in hot. This is by default, you can specify where to grab it from as an appended argument to the end. The accepted arguments are TopHot, RandomHot, TopNew, RandomNew, TopTop and RandomTop. Random arguments choose randomly from a list of 100 first entries. | `>>eddit ProgrammerHumor`
`>>rhymes` `>>rhyme` | Looks up words that rhymes with the given term. | `>>hymes forgetful`
`>>safebooru` `>>safe` | Returns a random image from the safebooru image repository. You can specify tags to narrow the range down, otherwise it's completely random. | `>>afebooru kawaii`
`>>soundslike` `>>soundlike` | Looks up words that are spelled similarly to the given term. | `>>oundslike elefint`
`>>spelledlike` `>>spelllike` `>>spellike` `>>spellcheck` | Looks up words that are spelled similarly to the given term. Supports the following wildcards ? - one character * - one or many characters  | `>>pelledlike coneticut`
`>>synonyms` `>>synonym` `>>syn` | Looks up words that have exact or nearly the same meaning for the given term. | `>>ynonyms ocean`
`>>urbandictionary` `>>urbandict` `>>urban` `>>ud` | Looks up the definition for a word or term in the Urban Dictionary. It is strongly suggested to take these with a grain of salt. | `>>rbandictionary dictionary`
`>>weather` `>>we` | Shows meteorological information about the inputed location. You can additionall add a unit argument at the end of the lookup. The allowed units are... auto: automatically select units based on geographic location ca: same as si, except that windSpeed is in kilometers per hour uk2: same as si, except that nearestStormDistance and visibility are in miles and windSpeed is in miles per hour us: Imperial units (the default) si: SI units If no unit is selected it default to auto.  | `>>eather Belgrade unit:si`
`>>wikipedia` `>>wiki` | Returns the summary of a wikipedia page that you inputted the search for. If a search is too general, an error will be returned. | `>>ikipedia Thread (Computing)`
`>>youtube` `>>yt` | A simple YouTube search. Outputs the resulting video's information and URL. You can add "-text" at the end of your search to make it a normal URL to the video. Instead of an embed with information. | `>>outube Game Grumps`
[Back To Top](#module-index)

### SETTINGS
Commands | Description | Example
----------|-------------|--------
`>>addcommand` `>>addcmd` | Adds a custom command trigger to the server. Whenever this trigger word is used with a command prefix the inputted response will be provided. Command requires the Manage Server permission. Custom commands can have special dynamic arguments in them. {author_name}: Message author name. {author_nick}: Message author nickname. {author_mention}: Tag the message author. {author_id}: Message author's ID. {channel_name}: Channel name. {channel_mention}: Channel tag. {channel_id}: Channel ID. {server_name}: Server name. {server_id}: Server ID. {target_name}: Target name. {target_nick}: Target nickname. {target_mention}: Tag the target. {target_id}: Target ID.  | `>>ddcommand hi Hello world!`
`>>addresponder` `>>addres` | Adds an auto-responder to the server. An automatic responder will reply with the set message to any sentence that conaints the chosen trigger in it as a standalone word. Responders can have special dynamic arguments in them like custom commands do. {author_name}: Message author name. {author_nick}: Message author nickname. {author_mention}: Tag the message author. {author_id}: Message author's ID. {channel_name}: Channel name. {channel_mention}: Channel tag. {channel_id}: Channel ID. {server_name}: Server name. {server_id}: Server ID. {target_name}: Target name. {target_nick}: Target nickname. {target_mention}: Tag the target. {target_id}: Target ID.  | `>>ddresponder hi Hello there!`
`>>asciionlynames` `>>forceascii` | Toggles if only ASCII characters are allowed in names. The bot will check members each 60s for an invalid name and rename them if they are not proper. To change the default temporary name, use the asciitempname command. | `>>sciionlynames`
`>>asciitempname` `>>asciitemp` | Changes the default temporary name for those who the temp name was enforced on. | `>>sciitempname <ChangeMePleaseI'mLonely>`
`>>blockedwords` | Lists all blocked words on the server. | `>>lockedwords`
`>>blockinvites` `>>filterinvites` | Toggles if invite links should be automatically removed. When an invite link is removed, the message author is notified and the removal is logged. This ignores anybody with a Manage Server permission. | `>>lockinvites`
`>>blockwords` `>>blockword` | Adds all the words you list to the blocked words filter. If any of the words in the filter is sent, the message will be removed and the author will be notified. | `>>lockwords crap`
`>>bye` `>>goodbye` | Toggles if the bot should say when users leave the server. The goodbye feature is active by default. | `>>ye`
`>>byechannel` `>>byech` | Sets the channel the goodbye messages should be sent to. | `>>yechannel #welcome`
`>>byemessage` `>>byemsg` | This sets the message shown on the server when a member leaves. There are certain syntaxes for controlling what is displayed. {user_name} - Basic text of the leaving user's name. {user_discriminator} - The numbers after the # in the user's name. {user_mention} - A mention tag of the leaving user. {user_id} - The leaving user's discord ID. {server_name} - Text showing the server's name. {server_id} - The server's discord ID. {owner_name} - Basic text showing the name of the server owner. {owner_discriminator} - The numbers after the # in the owner's name. {owner_mention} - A mention tag of the server's owner. {owner_id} - The server owner's discord ID.  | `>>yemessage Hello {user_mention}, welcome to {server_name}!`
`>>chatterbot` | Toggles if the Chatterbot functions should be active. If active, when a message starts with a mention of Sigma, she will respond. This setting is active by default. | `>>hatterbot`
`>>customcommands` `>>custcmds` | Shows a list of the server's custom commands. The list is separated into pages of 10 items each. You can specify the page number you want to see. | `>>ustomcommands 4`
`>>deletecommands` `>>delcmds` | Toggles if messages that are a command should be automatically deleted. | `>>eletecommands`
`>>greet` | Toggles if the bot should greet users when they enter the server. The greeting feature is active by default. | `>>reet`
`>>greetchannel` `>>greetch` | Sets the channel the greeting messages should be sent to, unless greetdm is active. | `>>reetchannel #welcome`
`>>greetdm` `>>greetpm` | Toggles if the bot should greet users by sending them a Direct Message, instead of writing the message in a channel. | `>>reetdm`
`>>greetmessage` `>>greetmsg` | This sets the message shown to joining members when they enter server. There are certain syntaxes for controlling what is displayed. {user_name} - Basic text of the joining user's name. {user_discriminator} - The numbers after the # in the user's name. {user_mention} - A mention tag of the joining user. {user_id} - The joining user's discord ID. {server_name} - Text showing the server's name. {server_id} - The server's discord ID. {owner_name} - Basic text showing the name of the server owner. {owner_discriminator} - The numbers after the # in the owner's name. {owner_mention} - A mention tag of the server's owner. {owner_id} - The server owner's discord ID.  | `>>reetmessage Hello {user_mention}, welcome to {server_name}!`
`>>loggingchannel` `>>logchannel` `>>logch` | Designates a channel where server events will be logged to. The stuff that is logged is member movement and moderator actions. Such as warns, bans, muting members and pruning channels. To disable the logging channel, input "disable" as the channel argument. | `>>oggingchannel #logging`
`>>prefix` | Sets the prefix that Sigma should respond to. This will be bound to your server and you can set it to anything you'd like. However, the prefix can not contain spaces. They will be automatically removed. | `>>refix !!`
`>>removecommand` `>>remcmd` `>>delcmd` | Removes a custom command trigger used for custom commands from the server. Command requires the Manage Server permission. | `>>emovecommand hi`
`>>removeresponder` `>>remres` `>>delres` | Removes a custom command trigger used for custom commands from the server. Command requires the Manage Server permission. | `>>emoveresponder hi`
`>>unblockwords` `>>unblockword` | Removes a blocked word allowing people to send messages containing it. | `>>nblockwords boobs`
`>>unflip` | Toggles if Sigma should respond to tables being flipped. | `>>nflip`
[Back To Top](#module-index)

### STATISTICS
Commands | Description | Example
----------|-------------|--------
`>>experience` `>>activity` `>>level` `>>exp` `>>xp` | Shows how much of Sigma's internal experience you obtained. Experience is earned by being an active member of the community. Yes, this is meant to be vague. | `>>xperience @person`
`>>profile` `>>mystats` | Shows Sigma's statistics for the mentioned user. Their current experience, level and most used commands. | `>>rofile @person`
`>>topcommands` `>>topcmds` | Shows the top 20 most used commands globally. | `>>opcommands`
`>>topcookies` | Shows the top 20 users who have the most cookies. | `>>opcookies`
`>>topcurrency` `>>topkud` | Shows the top 10 people in the Kud leaderboards. You can specify if you want to see the top people that are local, global, or by their current kud. The leaderboard shows the local server's leaderboard by default. | `>>opcurrency global`
`>>topexperience` `>>topxp` | Shows the top 10 people in the Experience leaderboards. You can specify if you want to see the top people that are local, global, or by their current xp. The leaderboard shows the local server's leaderboard by default. | `>>opexperience local`
`>>wallet` `>>currency` `>>money` `>>kud` | Shows how much of Sigma's internal currency you currently have. As well as how much you've earned on the current server and in total. Kud is earned by being an active member of the community. Yes, this is meant to be vague. | `>>allet @person`
[Back To Top](#module-index)

### UTILITY
Commands | Description | Example
----------|-------------|--------
`>>avatar` `>>av` | Shows the mentioned user's avatar. If no user is mentioned, it shows the author's avatar. You can add "gif" to the end of the command to indicate that it's a gif. Or you can add "auto" to make the color strip the dominant color of the image. You can also add "static" to the end to make it return the full sized static version of your avatar. | `>>vatar @person`
`>>botinformation` `>>botinfo` `>>info` | Shows information about the bot, version, codename, authors, etc. | `>>otinformation`
`>>bots` | Lists the bots on the server where the command is used and shows their status. | `>>ots`
`>>channelid` `>>chid` `>>cid` | Shows the User ID of the mentioned channel. If no channel is mentioned, it will show the ID of the channel the command is used in. If you don't want the return message to be an embed, add "text" at the end. | `>>hannelid #channel`
`>>channelinformation` `>>channelinfo` `>>chinfo` `>>cinfo` | Shows information and data about the mentioned channel. If no channel is mentioned, it will show data for the channel that the command is used in. | `>>hannelinformation #channel`
`>>color` `>>colour` `>>clr` | Shows the inputted color. It accepts either a HEX code or an RGB array. | `>>olor #1abc9c`
`>>convertcurrency` `>>convert` | Converts the amount of money inputed. The format of AMOUNT FROM_CURRENCY in TO_CURRENCY must be followed. | `>>onvertcurrency 50 EUR in USD`
`>>ingame` | Shows the top played games on the server. | `>>ngame @person`
`>>lmgtfy` `>>letmegooglethatforyou` | Outputs a link that will google the query for you. | `>>mgtfy Sexy Sneks`
`>>owners` | Shows a list of Sigma's owners. Users in this list have access to the administration module. | `>>wners`
`>>permissions` `>>perms` | Shows which permissions a user has and which they do not. If no user is mentioned, it will target the message author. | `>>ermissions @person`
`>>roleinformation` `>>roleinfo` `>>rinfo` | Shows information and data about the inputted role. Roles mentions do not work here, lookup is done via role name. | `>>oleinformation`
`>>rolepopulation` `>>rolepop` | Shows the population of the inputted role. If no arguments are provided, it will show the top 20 roles by population. | `>>olepopulation Warlard`
`>>servericon` `>>srvicon` `>>icon` | Shows the server's icon image. | `>>ervericon`
`>>serverid` `>>guildid` `>>srvid` `>>sid` `>>gid` | Shows the Server ID of the server the command is used in. | `>>erverid`
`>>serverinformation` `>>serverinfo` `>>sinfo` | Shows information and data about the server that the command is used in. | `>>erverinformation`
`>>shortenurl` `>>shorten` `>>bitly` | Shortens a URL for you using BitLy. All URLs returned via Sigma are without ads, merely shortened using the service. | `>>hortenurl https://i.redd.it/ngwebbf5nwfz.jpg`
`>>statistics` `>>stats` | Shows Sigma's current statistics. Population, message and command counts, and rates since startup. As well as when the bot last started. | `>>tatistics`
`>>status` | Shows the status of Sigma's machine. Processor information, memory, storage, network, etc. | `>>tatus`
`>>translation` `>>translate` `>>trans` | Translates a language from and to the given ones. If a conversion input is not stated, the first argument will be considered the input language. And the output will be in english. The language codes used abide by the ISO 639-1 format. For the whole list, you can go to this wikipedia article. https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes | `>>ranslation EN>JA Hello there!`
`>>userid` `>>uid` | Shows the User ID of the mentioned user. If no user is mentioned, it will show the author's ID. If you don't want the return message to be an embed, add "text" at the end. | `>>serid @person`
`>>userinformation` `>>userinfo` `>>uinfo` | Shows information and data about the mentioned user. If no user is mentioned, it will show data for the message author. | `>>serinformation @person`
`>>whoplays` | Generates a list of users playing the inputted game. | `>>hoplays Overwatch`
[Back To Top](#module-index)