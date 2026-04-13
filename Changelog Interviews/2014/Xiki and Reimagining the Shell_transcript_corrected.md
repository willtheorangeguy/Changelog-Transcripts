[0.00 → 13.84] welcome back everyone this is the changelog where our member supported blog podcast
[13.84 → 19.66] and weekly email come what's fresh and what's new in open source check out the blog at the
[19.66 → 26.40] changelog.com our past shows at five by five dot TV slash changelog, and you're listening to episode
[26.40 → 34.62] 126 jarred and I talked to Craig much about wiki a cool new project that brings the power of shell
[34.62 → 41.08] commands to everyone it's a pretty wild and deep conversation we have with Craig so definitely
[41.08 → 47.42] hang on to your seats today's show is sponsored by digital ocean code ship and top tile we'll tell
[47.42 → 52.72] you a bit more about our friends at code ship and top tile later on, but digital ocean is simple cloud
[52.72 → 60.08] hosting built for developers in just 55 seconds you can join over 150 000 developers who deploy
[60.08 → 68.88] daily to digital oceans SSD cloud enjoy the ease of use and speed of a SSD only cloud create droplets
[68.88 → 75.98] manage your DNS build a new server from a snapshot save a ton of time installing rails docker GitLab
[75.98 → 82.14] and more with one click installs you can even scale your infrastructure with their intuitive API
[82.14 → 90.56] sign up today and use the code changelog July or changelog august to get a 10 hosting credit when
[90.56 → 95.46] you sign up head to digitalocean.com to get started and now on to the show
[95.46 → 105.52] we're joined today by Craig much he is uh I don't know Craig you're doing some crazy stuff um some are
[105.52 → 111.76] saying change the way shell works um you're here to talk about this very cool project you
[111.76 → 118.76] have started I guess 10 years ago Ricky which is super powerful for the shell and uh and some
[118.76 → 124.86] pretty cool stuff so we also have jarred Santa on the call as well doing some uh some
[124.86 → 131.98] heavy lifting here right jarred yo what's up how's it going guys yes yeah I'm here heavy lifting um i
[131.98 → 136.24] don't know what that is but uh that's how it goes but Craig welcome to the show finally i you're a
[136.24 → 141.16] listener of the show right yes big fan how many changelog shows have you listened to
[141.16 → 146.90] oh man probably about some somewhere around 10 just like sort of like spread out uh all over the place
[146.90 → 155.66] you got a favourite money chance um let's see i uh I'm a big fan of rethink dB so that was a good one
[155.66 → 161.84] that was a good show um I didn't know we're going to have a quiz section I'm a big fan of avid's and a
[161.84 → 167.10] huge fan of pair programming so that was a pretty good one for me as well yes yeah I think
[167.10 → 173.44] a lot of people have uh have enjoyed that show as well it's a good show cool yeah totally so I guess
[173.44 → 177.40] let's kick off with I guess why we're on this call you reached out to us a couple of days ago because
[177.40 → 182.20] you got a kickstarter ending we'll fast-forward to like the now present and kind of rewind and play
[182.20 → 187.48] back cool but like right now you're dealing with a pretty much what I can tell is a 10-year-old
[187.48 → 193.24] project that's uh just now kind of getting some real limelight you've been using for a very long
[193.24 → 197.58] time, but now you also have a kickstarter going on to kind of help fund it to the next level and this
[197.58 → 204.00] isn't the first time we've had an uh an open source project on the show that's primarily start well not
[204.00 → 208.26] primarily but started from a kickstarter and so that's where you're at right now why don't you
[208.26 → 213.94] give the listeners kind of an intro to who you are and kind of what Ricky is and what you're doing and
[213.94 → 221.36] maybe even why my kickstarter okay yeah sure um I'm uh I'm a coder first and foremost I've always
[221.36 → 226.70] kind of loved coding i uh grew up in Ohio kind of started out like most of us just kind of hacking
[226.70 → 231.96] around and doing things doing a bunch of coding that i really kind of got excited about
[231.96 → 238.36] um went to school got beaten down a little bit and uh taught i to do some structure my first
[238.36 → 243.72] consulting job i I really bought into the like high structure o-o stuff for everything and uh
[243.72 → 250.14] kind of had phases back and forth but I've always had a kind of rebellious streak against uh against
[250.14 → 256.10] high structure high abstraction and um I've kind of uh kind of that was my cat in the background
[256.10 → 264.48] she says hi um so I've kind of always had this uh rebellious streak and I've kind of I feel like
[264.48 → 272.38] over the last um 10 years I've kind of watched people kind of also gain a rebellious streak like
[272.38 → 276.76] for example you used to not really be able to just have a hash that wasn't acceptable and like
[276.76 → 281.60] pass around the values of a form field now everyone does it there used to be no such thing as Jason you
[281.60 → 287.40] had to have objects and structure for everything now everyone will put something into Jason uh wikis are
[287.40 → 294.44] becoming a big thing and uh i sort of you know had all these ideas that i kind of suppressed and
[294.44 → 299.82] squashed and just used on my own uh it's actually more like 13 or 14 years from the beginning but it
[299.82 → 304.32] started out pretty rough, and it didn't even have a name in the beginning it's just a bunch of
[304.32 → 313.50] collections of uh of Elisa uh stuff basically where I could expand stuff in the shell and uh run um
[313.50 → 319.36] expand file paths in the shell navigate files and then um run shell commands like in a text buffer
[319.36 → 327.28] um and i just had a few like moments where I realized like wow you actually can do these very
[327.28 → 333.76] flexible things but have them be in a pretty nice structure sort of like the first time I saw wiki it
[333.76 → 339.94] blew me away i kind of thought wow you can actually have that just these big text files where you uh put
[339.94 → 346.44] free form text in with headings and then that's you know just a flat namespace uh you know where
[346.44 → 353.16] you've got like uh everything dumped in you've got a project page next to a page of contacts next to
[353.16 → 358.08] everything else and like wow that simple thing can like to be a better solution than like a big massive
[358.08 → 366.22] uh file you know uh shared directory of of of stuff for your company, or you know it can be
[366.22 → 371.46] can be better than SharePoint so yeah I've kind of like held on to this Ricky idea for a long time
[371.46 → 377.96] and I've kind of come to believe its kind of a pretty big missing piece in the landscape of um
[377.96 → 386.14] of tech and um i uh so I was working for banks and insurance companies in Ohio eventually kind of
[386.14 → 395.00] realized I needed to get out um and I moved out to Silicon Valley uh to San Francisco decided I was
[395.00 → 401.82] going to work on my startup memorize.com which i I did and had interns and uh part-time employees
[401.82 → 408.14] and uh kind of probably should be focusing on that now but instead decided to take a big risk and work
[408.14 → 418.46] on this uh crazy open source thing full-time Ricky um and uh the kickstarter uh I think now is the
[418.46 → 422.92] time to bring it to the world if you look at my uh GitHub page you'll see a lot of issues of
[422.92 → 429.86] people saying like hey uh had really liked this but had a hard time installing it um and that's
[429.86 → 434.44] sort of because I've been I've been neglecting people um I've basically wanted to make it for
[434.44 → 440.14] myself I use it for everything for development and notes and everything and um I've kind of
[440.14 → 446.18] intentionally let it let the installer be crappy for a while because I almost didn't want people to
[446.18 → 450.58] use it because I had all these features that's a good way to not let them use it is just kept
[450.58 → 456.20] a feature suppressed yeah I'm not even I'm super proud of that but I wasn't really suppressing
[456.20 → 459.80] features it was just I wasn't improving installer because I would spend time on it, and it would take
[459.80 → 466.02] a lot of time uh but I had these this like list of three huge things I wanted to do and i just
[466.02 → 469.54] recently I've kind of finished them up so now I'm to the point I'm like all right it's ready for the
[469.54 → 475.46] world and uh kickstarter seemed like a good way to reach out so you have a really solid video on
[475.46 → 480.60] the kickstarter page but for those listening can you give kind of the elevator pitch for wiki
[480.60 → 486.26] um what it does and how it's different from what we currently have sure um yeah there are a lot of
[486.26 → 494.76] ways of describing wiki the simplest way is it's like a command line uh, but it's a better way of
[494.76 → 499.98] running shell commands it's not meant to replace the command line it's meant to augment it um so for
[499.98 → 506.24] example if you do an l instead of then having to do a CD to like you know the fourth directory that
[506.24 → 511.52] you see on the screen and wiki you can just move your cursor down to that fourth directory and then
[511.52 → 518.88] control enter to expand so you can navigate directories like um kind of like a GUI app um
[518.88 → 524.94] and then when you run shell commands you can uh you can type a prompt on any line in basically a big
[524.94 → 530.00] text area by just typing a dollar sign rather than being restricted to the uh you know the single
[530.00 → 536.56] prompt at the bottom as is the case with traditional shell consoles and then anytime you run a command
[536.56 → 542.78] you can immediately type to incrementally filter down the output and then with many commands you can
[542.78 → 550.02] move your cursor down to the output of like say git if you uh type git, and you move your cursor down to
[550.02 → 556.16] log and control enter it'll expand that and run the git log command for you and if you then move it down
[556.16 → 563.56] to a commit and expand that it'll go one little deeper and show you know your commit message
[563.56 → 569.18] and all the files, and then you can drill in and uh interact with the output as though it was like a
[569.18 → 576.10] GUI tree so it's very free form just like a wiki yeah very free form you can edit anything
[576.10 → 584.82] so in practice i I suppose um how many users has it had I know you have on your video a couple of guys
[584.82 → 589.78] who said I've been using it for seven years I'm sure that's not in the current form but in this
[589.78 → 594.16] in the one that you show in the video where it's free form, and you can click here, and you can
[594.16 → 599.02] drill down in trees and stuff how many people uh have been using that or how long have you been
[599.02 → 605.14] using that in practice and how does it feel as opposed to what we currently do the uh drilling into the
[605.14 → 611.30] file trees has been there since pretty much the day one so that my two uh friends that have used it
[611.30 → 615.74] for years and years they use that the file tree drilling into the output of shell commands is
[615.74 → 620.66] relatively new so there aren't many people that that use it um and there are a few people here and
[620.66 → 624.62] there out of the net that have got it installed um it's hard for me to estimate it's relatively low
[624.62 → 630.74] number because the installation is kind of not great uh as far as how it feels um I don't know
[630.74 → 635.28] like some people it's hard to say I think it's an individual experience like some people
[635.28 → 641.38] just really get it, and they're like whoa I can see how this these you know two or three things
[641.38 → 646.34] would be an improvement I can filter down I can drill in I can copy and paste a command and run it
[646.34 → 651.16] again and still have the old outputs and I can delete the lines and the output that i I want because
[651.16 → 654.94] like you said that everything's free for you can edit everything and some people just say like well
[654.94 → 660.96] wait a minute why wouldn't I just use my shell to me, it feels just sort of natural and
[660.96 → 665.36] like and like obvious improvements for you know for some cases not all it's not meant like it's a
[665.36 → 669.00] different place the shell there are some things the shell is like really great at like asynchronous stuff
[669.00 → 678.62] it kind of feels like not exactly like this but it kind of feels like um like what is the like
[678.62 → 683.58] like kind of an IRB session where you can kind of jump into what's the other kind of really awesome
[683.58 → 688.94] IRB jarred the one that's out recently I don't use a proc is it what is it called again
[688.94 → 694.76] PRI right yeah PRI that's what it is um actually did a pairing session with Conrad Erwin one of
[694.76 → 700.08] Erwin one of the PRI guys uh yeah PRI is awesome yeah it seems a little bit like I mean obviously that's
[700.08 → 707.38] you know ruby but um this is kind of everything it seems a little like what that provides but on a
[707.38 → 715.42] grander scale for the entire shell yeah it's um it's their a little different uh like basically
[715.42 → 721.82] in wiki everything is just happens from a text file uh so you know when they when you run a command
[721.82 → 727.12] the output is just inserted as text into your text file then you can save it uh PRI is kind of more
[727.12 → 734.02] along the lines of like you know um a REPL and has some other cool integration points but yeah when i
[734.02 → 739.12] when I got together with Conrad Erwin uh several months ago we had some really cool ideas for kind
[739.12 → 745.10] of the two complementing each other like making a wiki interface a wiki command that could call the
[745.10 → 750.34] PRI features and sort of drill in and like CDs into the functions and stuff I want to get back to
[750.34 → 755.00] that at some point because I think that'd be really awesome I was going to say I think interactions are
[755.00 → 759.70] really it seems like from your kickstarter that's one of the main focuses of your development uh roadmap
[759.70 → 766.64] is to get it integrated into vim into Emacs into sublime text and so on um right now is it kind of
[766.64 → 773.58] in its own world, and it's not really integrated into the environment well right now it supports um Aquaman
[773.58 → 780.54] and Emacs okay those two text editors Aquaman is basically a very user-friendly version of Emacs where
[780.54 → 786.12] you can command c command v uh you can use the mouse to select text, and you can type to replace you know
[786.12 → 792.88] it's very much like a mac native text editor uh so that's the editor I recommend people to use
[792.88 → 796.18] they can, you know if they don't like Emacs they don't have to really know it's Emacs they can use
[796.18 → 802.14] the menus and stuff, and they can use you know command s to save etc so it runs in that as sort of the
[802.14 → 810.14] default, and then it also runs in like base uh, uh Emacs and terminal Emacs and yeah there's
[810.14 → 815.98] tentative vim support, but it's very, very weak there's a tentative sublime support, but it needs
[815.98 → 818.96] to be improved which is what the kickstarter is half of what the kickstarter is about
[818.96 → 826.20] um and there's this brand new ash where you can run it right from the in the shell console it's not
[826.20 → 832.38] released yet that's I'm going to do first and that'll let people just type ash space you know
[832.38 → 836.84] get on the command line, and they don't even have to worry about setting anything up it'll just pop up
[836.84 → 842.18] and I'll have uh stuff right there on the screen saying hey type control q to quit and type control e to
[842.18 → 847.74] expand so that's probably going to be the defaults that just ash right from the I'd be pretty good
[847.74 → 853.14] for learning people too like you know just getting started you get all those all the feedback basically
[853.14 → 860.72] from the CLI that's already present for git, and you know do you want to do a push or do you want to
[860.72 → 866.66] pull this kind of things are like already accessible, and it's also keyboarded navigable so it's not like
[866.66 → 870.04] you have to move your mouse around but though you could right you can double-click on things if you
[870.04 → 878.98] want as well you're right so you said ash um this piece of it does it pop its own window when you do
[878.98 → 883.86] that because I know it's very interactive clickable um or can it take over your current terminal session
[883.86 → 890.06] or does it pop its own UI it takes over the current terminal session what's actually happening behind
[890.06 → 896.74] the scenes is it's launching uh Emacs okay but I'm overriding all the keyboard shortcuts uh including
[896.74 → 902.18] including escape I'll make escape actually cancel out so it won't confuse people uh so as far as most
[902.18 → 906.64] people are concerned they don't even have to know what it is I'll have all the key shortcuts on the
[906.64 → 912.94] screen they're all they're all remapped not all of them you can use the base uh Emacs shortcuts if
[912.94 → 917.34] you know them but yeah it's just it's just actually running within Emacs and just customizing the heck out
[917.34 → 923.34] of it, and it's doing it in a way that's not interfering with uh your normal Emacs config if you have it which
[923.34 → 930.68] is a big you know challenge that I've had that makes a lot of sense I was wondering how you're
[930.68 → 936.26] accomplishing that what about operating system support is this uh Linux and mac at the moment
[936.26 → 942.58] yeah Linux and mac um there's a pull request for uh for windows support out there um that might
[942.58 → 948.44] might go a little bit of the way toward uh windows support I'd like to do windows support um
[948.44 → 953.30] now that I've got all this publicity from the kickstarter I think if it passes I'll be able
[953.30 → 957.42] to reach out to people afterward and say like hey people that know how to do this process
[957.42 → 962.46] communication and windows like pair with me and help me on it but I don't I'm not promising windows
[962.46 → 965.70] support as part of the kickstarter even though a lot of people want me to just because I don't
[965.70 → 972.64] you know I've already kind of promised a lot but I do want to do it well uh jerry do you think it
[972.64 → 976.36] makes sense to dab down kickstarter kind of go I want to i was thinking about going into the past a bit
[976.36 → 980.70] to try to figure out where this what was the problem you kind of tackled where did this come
[980.70 → 985.60] from what's the history it's like 10 years old so it's not like it's a year old it's its pretty
[985.60 → 991.48] dated yeah in terms of its age you know not so much not good and I'm interested in I guess a little
[991.48 → 996.00] bit of the technical implementation I'm sure for a 10 plus year project it's probably gone through
[996.00 → 1001.86] different forms I know it seems to be written in ruby at the moment but perhaps not always so I'm
[1001.86 → 1006.48] definitely interested in the history of how you developed it cool yeah originally it was an
[1006.48 → 1014.34] Elisa right um i originally just absolutely hated and despised Emacs because I started from like a
[1014.34 → 1019.44] mac GUI uh you know actually I started before that that's not true I did my first experience was apple
[1019.44 → 1026.70] 2e and basic uh when I was really young and then um then i you know got a mac and just loved it loved
[1026.70 → 1030.88] it loved it went to college, and they're like here use Emacs and I was like where's your knowing where are the
[1030.88 → 1037.42] menu items this is horrible uh I started using PICO instead which is where I got the inspiration for
[1037.42 → 1042.00] seeing the keyboard shortcuts on the screen I was just talking about but then i kind of fell in
[1042.00 → 1051.20] love with Emacs and uh loved what it did and like just the free form aspects of it but i always
[1051.20 → 1058.06] hated the default keyboard shortcuts and still kind of do and um i I use it for all kinds of things and
[1058.06 → 1066.40] it seemed like a one big missing piece was a cool file navigation and i I always want to be able to
[1066.40 → 1074.08] have kind of extreme flexibility um and the file navigation that was kind of ideal for me was being
[1074.08 → 1080.06] able to control edit anything at any time so you know if I have a directory of say you know 20 models
[1080.06 → 1085.70] and I only care about uh two of them and one starts with a and one starts with a z I don't want to
[1085.70 → 1089.80] scroll back and forth between the two I want to delete the ones in between just temporarily you
[1089.80 → 1098.96] know hide them from the view so I made basically a file browsing uh you know format which is just
[1098.96 → 1104.72] you know the most obvious thing you can do which is like you basically type a path with slashes and
[1104.72 → 1110.60] then if you want to make it multi-line you can uh you indent two spaces so you know like
[1110.60 → 1119.66] um slash project slash and then line break space and then my project basically taking that
[1119.66 → 1126.70] and making that navigable the uh keyboard shortcuts and then later the mouse um so yeah it started out
[1126.70 → 1133.02] as Elisa I made that in Elisa I made the uh running shell commands which is pretty similar since you type
[1133.02 → 1138.00] a dollar sign space and like ls, and then it inserts the result indented two spaces underneath
[1138.00 → 1145.86] uh implemented the filtering down and um tons of keyboard shortcuts and just kept changing things
[1145.86 → 1152.16] over and over and over and eventually discovered i uh well I became a ruby programmer in the meantime
[1152.16 → 1158.40] and just loved ruby and DHH kind of just rocked everyone's world with rails, and you know had
[1158.40 → 1166.74] this just beautiful combination of sort of um uh flexibility and yet structure where it was needed in
[1166.74 → 1171.72] rails and i just totally bought into it became a rails programmer loved ruby because I liked the
[1171.72 → 1178.28] oh stuff I could do in java but love the i I started out with pearl and loved the flexibility of pearl and
[1178.28 → 1184.96] ruby was like a perfect marriage of the two so I found this uh library called ELR like Elisa for ruby
[1184.96 → 1190.96] written by one of the core ruby guys this guy named rubidic and uh that let you program
[1190.96 → 1200.08] inside remex but using ruby instead of Elisa so I ported to that and my product I ported uh you
[1200.08 → 1205.40] know my big code base to that uh named it Ricky around that time uh my productivity shot up about
[1205.40 → 1211.12] like 2x or 3x um I do like lisp but for this particular uh application ruby was just a great
[1211.12 → 1217.86] fit a lot of text processing etc processing um yeah it's been it's been ruby for
[1217.86 → 1228.40] maybe seven or no more like eight or nine years now I think so i I know one of the major drawbacks
[1228.40 → 1233.06] that you mentioned for people getting started with it has been the setup slash install process
[1233.06 → 1241.40] some of that that's the blame on you know ruby as a choice I know uh recently we had on uh
[1241.40 → 1248.00] Jeremy signs uh who you know has a post where uh he was distributing command line tools in ruby and
[1248.00 → 1251.94] and switched to go because of the know the universal binary that you can just drop in
[1251.94 → 1258.28] is ruby some in the ecosystem some of the reason why the setup process has been not
[1258.28 → 1265.60] streamlined yet um I suppose uh ruby is probably I mean at this point the ruby landscape is pretty
[1265.60 → 1271.84] good because ruby 2.0 is installed by default on the mac on Linux people you just tell them to
[1271.84 → 1276.02] install something, and they say okay right on the mac if you like say install a different version of
[1276.02 → 1281.00] ruby it's a big challenge but uh with mavericks ruby 2.0 is installed by default and I can just use
[1281.00 → 1287.08] that it has Emacs installed by default I can just use that you know behind the scenes um I should I
[1287.08 → 1292.52] should mention that uh beginning a couple of years ago I started supporting other languages so even though
[1292.52 → 1300.34] wiki is implemented in ruby you can make wiki commands uh in python JavaScript coffee script
[1300.34 → 1308.70] uh several different languages nice talk about these commands yeah um the coolest part of wiki is
[1308.70 → 1315.10] that you can make your own commands uh wiki is very wiki inspired which you know you're probably
[1315.10 → 1322.44] not surprised because it's its called wiki which is your know uh wiki with an x instead of a w um i first i
[1322.44 → 1328.96] called i I was calling that uh expandable wiki is kind of what wiki was short for um the first i
[1328.96 → 1334.56] called it executable wiki now I'm leaning toward expand wiki actually for x i k i so it's
[1334.56 → 1341.84] very it's very wiki inspired you can uh type the name of a command and if it doesn't exist it'll pop
[1341.84 → 1348.08] up and say hey this command doesn't exist do you want to create it using a text file or a ruby script
[1348.08 → 1353.44] or a python script or a directory structure where the directories and files are your menu items
[1353.44 → 1362.46] or a class where it'll just take the methods in your class and use them as the menu items and then
[1362.46 → 1370.38] when you type the name of that command let's say uh like Adam is a command we'll uh you know than
[1370.38 → 1375.58] you'll be able to just type Adam on any blank line and double click, and it will run your file
[1375.58 → 1383.48] and basically as time goes on I can, I've I've kind of had more and more ideas about hey here's this
[1383.48 → 1389.90] obvious way of making a command and they kind of get simpler and simpler and to me, I think for uh
[1389.90 → 1396.96] what wiki tried it does it try to like make uh make it so that all the simplest possible ways of
[1396.96 → 1404.68] making a little command with like an UI of like kind of menu items uh exists uh so wiki is like
[1404.68 → 1410.84] you know one use case is better shell console the other use case is the quickest way to make an UI on top
[1410.84 → 1416.56] of code like a working UI so you can just take the command that you've written it's got its own little
[1416.56 → 1423.54] UI, and you can just pass it to a friend, and they can run it exactly is there a distribution
[1423.54 → 1429.56] mechanism or is it like you know email me this text file, or you know whatever yeah there 's's
[1429.56 → 1436.94] no uh central repository yet aside from um basically my git repository the uh you know you
[1436.94 → 1443.52] know the homebrew model of if you have an uh you know a new package you just give it to the main
[1443.52 → 1447.56] guy, and he'll check it in for you, I mean that's what I've got now basically but down the road yeah
[1447.56 → 1452.64] having something sort of like ruby gems or NPM is probably going to be a fit at some point
[1452.64 → 1458.50] so how many built-in commands are there just off the top of your head uh several hundred I'd say
[1458.50 → 1463.36] roughly like 400 or something um probably more but some of them there are kind of silly and useless
[1463.36 → 1470.72] but uh over a couple of hundred pretty, pretty useful ones the uh I should say at kind of the intro to
[1470.72 → 1477.00] the command uh discussion that the hello world for making a command is just made a text file say
[1477.00 → 1485.24] named hello dot top dot TXT, and you put uh world in the file, and you just drag that into a special
[1485.24 → 1490.18] directory and then that immediately is a command and that direct by default that directory is just
[1490.18 → 1495.16] the commands' directory in your home directory or any other directory that you designate as being in
[1495.16 → 1500.72] your is a key path, and you said earlier ruby python several languages just put those languages in
[1500.72 → 1505.80] there they run exactly just drop it in and then and yeah so where do you see the power something like
[1505.80 → 1511.44] that coming up like give us some examples of to expand on you know we've got some people listen
[1511.44 → 1514.88] to the show they're thinking okay well how can I be practical maybe they've already got some ideas but
[1514.88 → 1521.70] can you give us some things and some ways that you've used that specific feature set yeah sure um since
[1521.70 → 1527.78] it's so easy to make commands you know uh I've I've made a ton of them that like normally would
[1527.78 → 1531.06] have taken me like way longer I've written eclipse plugins, and it's that's like you know
[1531.06 → 1539.60] uh huge you know process to plan out what your UI is going to look like um and wiki you don't
[1539.60 → 1543.80] even worry about the UI you just dump out some text, and it displays it to the user, and then you can
[1543.80 → 1549.52] like fix it later make it look more organized later um a good example is just actually last night
[1549.52 → 1557.46] my friend Jeremy and i uh got together and paired to make a Heroku menu, and we did it in like a half an
[1557.46 → 1564.04] hour it's just this flat file with kind of like if else and uh you type uh Heroku on the
[1564.04 → 1570.68] command line um with wiki shell which is ash it's the new kind of easy way of interacting with
[1570.68 → 1580.50] wiki you can just type ash space dash Heroku, and then it shows you uh Heroku and then underneath that
[1580.50 → 1586.28] it lists out all your apps, and you can move the cursor down and drill into each app, and then it has
[1586.28 → 1590.22] items for each app of things that you want to do kind of like you know you would have in a GUI
[1590.22 → 1596.14] uh so there's a config option underneath your Heroku app you can expand that it shows you the
[1596.14 → 1603.20] config parameters, and then you can edit and then uh save those back by control e the same way you
[1603.20 → 1610.78] expand and collapse you can there's a log item you can expand the log and um type to filter down
[1610.78 → 1617.40] um you can there's a browse option i actually just posted a video on the kickstarter page and i
[1617.40 → 1623.38] tweeted it uh to at wiki on Twitter uh if you want to check it out was that update or something like
[1623.38 → 1631.74] that so let's go let's get Heroku back all right let's get Heroku to back wiki yes my new strategy
[1631.74 → 1637.50] that's a nice way to get their support right yeah I hope it works that's that's my plan for getting
[1637.50 → 1643.48] that uh 50 of the kickstarter goal and put that link in the show notes then it's awesome yeah a
[1643.48 → 1647.42] ton of people retweeted that this morning it was awesome people saying like hey Heroku check this out
[1647.42 → 1651.84] maybe you should back wiki yeah I'm going to reach out to companies probably a bunch of different ones
[1651.84 → 1658.12] and tell them like hey there's a ten thousand dollar reward that will get your logo on um
[1658.12 → 1666.98] on ziki.org and xsh.org for a year and the eternal gratitude of the thousands of developers that
[1666.98 → 1672.34] are excited about wiki let's pause the show for just a minute give a shout-out to our sponsor
[1672.34 → 1678.12] code ship is a hosted continuous deployment service that just works you can
[1678.12 → 1682.00] easily set up continuous integration for your application in just a few steps and
[1682.00 → 1687.78] automatically deploy all your code when your tests pass code ship has great support for lots
[1687.78 → 1693.76] of languages test frameworks as well as notification services they easily integrate with GitHub or Bitbucket
[1693.76 → 1701.74] and can deploy to cloud services like Heroku AWS notice google app engine or even your own servers
[1701.74 → 1706.68] setup takes only three minutes get started today with their free plan and make sure you use the
[1706.68 → 1714.74] code the changelog podcast that's the changelog podcast is the code to get a 20 discount for three
[1714.74 → 1720.88] months on any plan you choose head to code ship.io and tell them the changelog sent you
[1720.88 → 1728.04] I noticed in the screenshot at least of the opening video that you're talking about it's the
[1728.04 → 1735.88] wiki shell command so ash it looks like a space and then a dash Heroku yes, yes is that what you meant
[1735.88 → 1739.82] is that what you said earlier did I miss that I think I said that okay because I thought you said
[1739.82 → 1746.12] because I know you can kind of pre-pin the wiki show in front of something like ls and
[1746.12 → 1751.80] something, and you can get that so this is a little different this is like a flag yeah if you pass a
[1751.80 → 1763.44] flag xsh space dash foo that's a wiki command if you do ash space foo that's it'll treat that as a
[1763.44 → 1767.38] shell command okay gotcha that's why I was trying to connect the dots out than yeah, and they're
[1767.38 → 1773.04] kind of similar you can make both of them have um interaction like that's that's a new wiki
[1773.04 → 1782.60] feature if you type ash space uh like who am I uh and then enter that'll open up who am I, and it'll
[1782.60 → 1786.94] run it is'll show you the output indented two spaces underneath and if you double-click on the
[1786.94 → 1793.30] or in a shell console it would be control e to expand the output uh then wiki will pop up and say
[1793.30 → 1799.16] like hey it looks like you're trying to interact with the output of this command um there isn't a
[1799.16 → 1803.80] wrapper for it yet do you want to create one, and then you can, it'll walk you through giving you a
[1803.80 → 1811.50] little template of just making a script in any language you want and then basically you make that
[1811.50 → 1819.48] output look at what was uh expanded, and usually you make it like call you know shell out to the command
[1819.48 → 1825.28] and do something that's relevant so you can make wrappers for commands so you can interact with uh you
[1825.28 → 1832.50] know the outputs of you can just go in and expand the output of uh another good example is like uh PS if
[1832.50 → 1838.76] you want to kill processes I've got a wrapper built in where you can type ash space PS, and then you can
[1838.76 → 1843.22] go move your cursor down to one of the lines of the output and then uh control e to expand that
[1843.22 → 1848.12] and it'll kill the process for you so interacting with the output of commands kind of like it's a GUI
[1848.12 → 1853.28] you know like you've got the've got stuff on the screen sometimes you don't want to like type
[1853.28 → 1859.60] another command underneath that you know has uh retyping some of the output like it's right there
[1859.60 → 1865.50] why not just move your cursor down and say hey do the relevant thing to uh to this line of output
[1865.50 → 1872.22] that's awesome I've spent years I probably had this ingrained in my fingers now how to type you
[1872.22 → 1878.02] know PS aux pipe it into grew for a specific word and then grab the PID and kill the PID, and it's like
[1878.02 → 1882.66] a two-step process that I've just done so many times I'm sure there are ways even inside just bash to make
[1882.66 → 1888.66] that you know more simple but being able to interact like a GUI seems like it would really be beneficial
[1888.66 → 1894.16] to me in that specific circumstance this might be about the same time the listeners are saying things
[1894.16 → 1901.58] like is this real life my brain just exploded my mind is blown holy mother of god uh my life just
[1901.58 → 1906.96] changed forever these are quotes on your kickstarter, but these are things that uh I'm sure people are
[1906.96 → 1912.46] saying because that's when I saw that I was like that's insane you know to be able to do that and
[1912.46 → 1917.50] like you said jarred it's its kind of like ingrained in your brain to type certain commands and certain
[1917.50 → 1923.30] flags to things and grew for stuff when you don't really have to do that now it's its you just
[1923.30 → 1929.98] made the lives of so many so much easier yeah, thanks let's not mention the uh hacker news comments that
[1929.98 → 1937.22] are like you are an idiot I hate you that's just life right that's what happens yeah I wanted to
[1937.22 → 1941.40] kind of talk about the know what is your know arguably a marketing campaign that you've had going
[1941.40 → 1947.96] because you've gotten sticky on tech crunch uh number one on hacker news I think Linux journal it world
[1947.96 → 1954.62] um these are major outlets, and you know it's an it's a shell console right I mean I'm not trying to
[1954.62 → 1959.96] belittle it but at the end of the day like tech crunch doesn't usually cover these things um
[1959.96 → 1965.04] how did you get so much exposure for a project that you've had put so much time into kind of
[1965.04 → 1970.24] behind the scenes and now all of a sudden explosion it's hard to say I think it's probably the videos
[1970.24 → 1976.20] I put a ton of time into the videos and just implementing a bunch of features like I think the
[1976.20 → 1980.16] ash thing recently kind of pushed me over the top and I was in the middle of the kickstarter I had all
[1980.16 → 1985.88] my friends advising me like hey spend your time like you know sending emails to people and reaching
[1985.88 → 1988.54] out to the media I was like no I'm just going to hunker down I've got like you know
[1988.54 → 1994.84] uh 20 days left but I'm going to spend five days implementing this ash thing because I think i
[1994.84 → 2000.04] can make a video and people will just appreciate the like you know seeing that in action so just
[2000.04 → 2004.74] doing videos of showing a lot of cool stuff happening and getting rid of the pauses
[2004.74 → 2012.10] and getting to the point making yourself get to the point really quickly um yeah it's been it's been
[2012.10 → 2019.66] really cool um the linux.com article and the tech coach article were like almost more positive
[2019.66 → 2024.60] than I would have ever you know dared to dream about like they know kind of said like uh
[2024.60 → 2029.72] particularly uh Carla Schroeder who's like just an amazing person she wrote the um
[2030.40 → 2037.94] o'Reilly's Linux cookbook and the Linux networking cookbook um she's like you know kind of one of my idols
[2037.94 → 2044.64] now actually and uh having her say like wiki is the next big thing in free and open source software
[2044.64 → 2050.20] and it's revolutionary, and she doesn't use the word lightly that's just blowing my mind and I'm so happy
[2050.20 → 2054.82] with that I did like reach out to a few people but I guess it kind of snowballed on the downside of it
[2054.82 → 2061.96] I've got like you know the big outlets like you said uh tech crunch in particular and giving me amazing
[2061.96 → 2067.42] coverage and I'm still just about at half of my goal so it's sort of bittersweet
[2067.42 → 2073.60] like where do I go from here you know this is something that Tim Caswell covered jarred not
[2073.60 → 2078.92] long ago when we talked to him, you know similar I mean he'd done two rounds of you know fundraising
[2078.92 → 2085.42] first one was a kickstarter second was a bounty source and uh you know he was building ask at the
[2085.42 → 2092.46] time to dovetail into t-edit, and you know his story was a bit more successful and I think it was
[2092.46 → 2098.24] only because Mozilla stepped in and and and gave like 30 000 to kind of complete the goal or something
[2098.24 → 2104.16] like that, but you know we're seeing open source look for funding more often in your case it's a
[2104.16 → 2109.00] little different Craig because you've got a startup you're doing you took a pause from that to work on
[2109.00 → 2114.92] something that's open source and then also kickstart it so it's its slightly different but
[2114.92 → 2121.16] yeah it's kind of a bummer that you're not getting I guess more funding traction on your kickstarter
[2121.16 → 2127.38] yeah just for the record my startup is not making any money so I'm not I'm not asking for uh
[2127.38 → 2133.98] like a bonus here like if is this passes so how do you live than I'm on wiki if off uh savings okay
[2133.98 → 2138.48] must be a lot of money consulting especially if you're in Silicon Valley right
[2138.48 → 2144.92] yeah well I've got roommates here so we keep them keep the rent down um but yeah my new plan is to
[2144.92 → 2148.38] reach out to companies I think it's I think it's actually a huge opportunity companies blow
[2148.38 → 2152.18] you know just thousands on like sponsoring conferences they don't blow it it's its you know
[2152.18 → 2156.36] it's good right it's a good way to spend it but they know they spend money on um
[2156.36 → 2161.14] recruiting and advertising and thousands of thousands and like wiki's sort of like gotten
[2161.14 → 2164.78] all this publicity, and it's just sitting out there waiting for someone to kind of like
[2164.78 → 2172.16] a company to rescue it, and you know uh they would have tons of kind of like really cutting edge
[2172.16 → 2176.38] tech people that are like really into just the very cutting edge those are like the fans of wiki
[2176.38 → 2182.48] you know they would have those people saying like wow thank you uh you know engine yard
[2182.48 → 2188.82] or thank you Heroku or Mozilla for saving this unfortunately I can't have the uh donation any
[2188.82 → 2195.02] bigger on kickstarter than 10 000 so I'm going to need to like to get maybe three or four companies to uh
[2195.02 → 2200.88] send you know donate 10 000 which I think isn't much, and you know in return i will make such a
[2200.88 → 2205.86] big deal out of you know tweeting and emailing all the kickstarter backers saying like hey this company
[2205.86 → 2212.64] saved wiki um you know on the screencast showing uh you can even buy the.com you can be like you know
[2212.64 → 2218.84] such and such company save ziki.com and put up like a landing page and I will tweet that everywhere
[2218.84 → 2223.34] yeah right that'd be crazy another thing I mean you've got your get-up too we had chat on the show
[2223.34 → 2228.56] not long ago talking about get up and uh yeah listen to its kind of a bummer you got one dollar per week
[2228.56 → 2233.30] coming to you listen everybody you got one dollar a week this guy's been building this open source
[2233.30 → 2240.54] project for 10 years okay that's like a cent uh you know yes it's not even cool it's its that's kind of
[2240.54 → 2243.98] what I get for having a crappy installation like if all these people excited about it, and they try to
[2243.98 → 2249.00] install it, and they're like well you know five different errors so maybe if you fix the installation
[2249.00 → 2254.16] process you get more get up yeah hopefully it used to be higher it used to be more than a dollar
[2254.16 → 2258.08] but i actually uh actually found out that most of that was coming from my mom
[2258.08 → 2268.42] sad true story awesome so in um on the kickstarter page you talk about wiki's future I know
[2268.42 → 2273.44] we kind of covered a bit of it but can you kind of paint the picture of like what's the trajectory
[2273.44 → 2279.50] where are you going with it and as best as you can fill in the gaps for us cool yeah the future of
[2279.50 → 2287.38] wiki's it's morphing into a language um it's you know basically just a kind of diminish free-form way
[2287.38 → 2294.74] of like making a user interface so um you know if you take a step back and look at what user interface
[2294.74 → 2301.56] is let's say you have like a foo menu in your you know your GUI menu bar, and you click it and then you
[2301.56 → 2307.80] see bar what's the difference between that and seeing a foo icon on your desktop it pops up and
[2307.80 → 2314.70] it shows you bar uh typing foo in your shell command, and it shows you bar as the outputs you go to a URL
[2314.70 → 2320.66] you know foo.com, and you see bar up here there 's's something fundamental there that can be
[2320.66 → 2325.68] abstracted out and to me the simplest way of doing that and like you know a lot of other languages
[2325.68 → 2330.92] like python and coffee script are using this two-space indenting uh it's just this sort of
[2330.92 → 2339.40] natural thing so why not have just a dead simple uh kind of language slash syntax of representing you
[2339.40 → 2346.46] know an UI where you just type a word in free-form text, and then you double-click on it or to do a
[2346.46 → 2350.84] keyboard shortcut, and then you see the output and of course from there if that's indented two spaces
[2350.84 → 2357.18] underneath you could have multiple lines of output you know and uh you each one of those lines of
[2357.18 → 2361.62] output themselves can be an option, and you can expand those, and you indent that two spaces more
[2361.62 → 2365.90] underneath so four spaces and then at that point basically you've got like a tree that looks just
[2365.90 → 2373.84] like any you know tree that you see in like a left nav of you know a standard application
[2373.84 → 2381.80] um but if you keep things simple, and you keep things boiled down as a text format you can bind
[2381.80 → 2390.82] of represent just about any user interface as just an indented textual tree and um you know I think
[2390.82 → 2396.66] it's it is absolutely insane to me that there isn't a simple format where you can define an interface
[2396.66 → 2403.28] it's like we'll make a little animal uh you know program and underneath it, you've got like mammals and
[2403.28 → 2408.42] lizards and underneath mammals you've got uh whatever dogs and cats so you want to make that
[2408.42 → 2416.68] structure and deploy it as a know navigable websites as a shell command as a mobile app where
[2416.68 → 2421.24] you know you it's a mobile app called animals, and then you double-click it, and it shows you two options
[2421.24 → 2426.70] mammals and lizards or whatever I said uh, and then you know we've got all these devices coming out like
[2426.70 → 2433.54] all these I've got a pebble I love it there are like 10 smartwatches coming out um and they all
[2433.54 → 2441.98] have their own separate APIs and I think the world is just totally ripe for having this dead simple uh
[2441.98 → 2447.18] language where you can just type something out uh basically the navigation of you know a program
[2447.18 → 2451.78] and then deploy that to all these devices of course if you want to make a pebble app that does something
[2451.78 → 2457.94] useful or iPhone app you'll probably at some point have to call like a native method but I say make
[2457.94 → 2463.24] the structure first make that deploy everywhere so you can navigate around um and then if you have to
[2463.24 → 2468.90] do something whatever iPhone specific then you know on top of this universal structure of your navigation
[2468.90 → 2476.42] you can, you know conditionally say like all right they clicked on um phone call if platform is iPhone
[2476.42 → 2481.16] then make phone call, and you know if you want to make it look pretty then you can do all kinds of
[2481.16 → 2486.78] stuff that you know we already have tools like this to like style uh the output to move things around
[2486.78 → 2491.60] and not make it just a nested structure but out of the box with wiki you can just type um you know
[2491.60 → 2501.88] something like uh animals and indent uh mammals and lizards underneath, and then you can uh navigate that
[2501.88 → 2507.96] and use it in the shell command you can go to the wiki web server that's built into wiki and you can
[2507.96 → 2514.16] see a mobile interface so it'll show like in you know like a little mobile uh pill button style the
[2514.16 → 2521.04] menu items so uh mammals and lizards, and you can click on mammals, and it will move over like you know
[2521.04 → 2527.34] like uh slide over like a standard mobile interface and um from your text editor as well if you have a
[2527.34 → 2532.90] wiki plugin for your text editor you can type uh animals and uh double click or control enter and
[2532.90 → 2540.12] it will uh insert this underneath um and from there you can do all kinds of things where it's not just
[2540.12 → 2548.00] this trivial example you can add headings and paragraphs uh like I said um uh wiki is very wiki
[2548.00 → 2553.12] inspired their wiki syntaxes for tons of stuff like I said there's a wiki syntax for running a shell
[2553.12 → 2558.24] command it's just dollar sign space and then the wiki syntax for heading is just an angle bracket
[2558.24 → 2564.32] space um and then the heading syntax for a bullet point is just like a dash space you know with two
[2564.32 → 2568.90] space indenting so you can type those things in the commands as well and then when you display that in
[2568.90 → 2574.54] a mobile interface it can show you it can render the heading as a larger font size, and you can
[2574.54 → 2580.16] make you know actually an app that's like read only uh that actually has some like useful content you
[2580.16 → 2584.60] can make that with just zero code and that could deploy to everywhere like a cool example I think is
[2584.60 → 2590.70] like uh if you go to a conference they could say like hey got the conference schedule uh in this
[2590.70 → 2598.22] global format you can deploy it on your watch you can deploy it on your cell phone um on you know
[2598.22 → 2603.78] and basically any device and then even though it's like static content it's very useful, and you could uh
[2603.78 → 2609.22] navigate around on your um pebble to see the schedule, and then you know of course
[2609.22 → 2616.44] from there having embedded code is gonna pop up as a know as a need very quickly if you want to do
[2616.44 → 2624.16] something you know more than a static uh app so the way I do that is uh underneath a menu item
[2624.16 → 2629.00] you can uh there's a wiki syntax for code embedded underneath a menu item which is this exclamation mark
[2629.00 → 2636.98] space, and you can have multiple lines of a method and uh you know that can call your you know
[2636.98 → 2644.12] your library that has your code very well-structured out in a way you know you can have your menu items
[2644.12 → 2649.84] delegate to that and I've got a bunch of other ways of having dynamic code like you can have a class
[2649.84 → 2657.16] that has a kind of routing string that'll route back and forth between methods um and uh and different
[2657.16 → 2662.34] paths and pass arguments and kind of sophisticated way but kind of the number one rule in wiki is like
[2662.34 → 2669.38] by default the absolute simplest way of doing something uh should work like if is you can do
[2669.38 → 2672.20] something with a class you should be able to do with a script as well when you want to
[2672.20 → 2677.50] if you can do that you should be able to take a text file and uh make that be you know sort of a command
[2677.50 → 2678.14] or a program
[2678.14 → 2686.66] my mind is blown I'm just thinking like you got language in there you've got a shell you know a
[2686.66 → 2691.52] shell augmentation you know it's meant to be you know kind of going tandem with your shell already
[2691.52 → 2699.16] um I mean it is seems personally to me, it just seems like it's such an audacious kind of goal to
[2699.16 → 2704.98] hit and the things you're talking about um I wasn't expecting to go there what about you jarred
[2704.98 → 2711.32] no not really I'm wondering now I mean 80 000 on this kickstarter what is that like a six month
[2711.32 → 2717.40] runway for a year runway maybe you're in San Francisco so three weeks what is that
[2717.40 → 2725.52] um okay I mean I can make it stretch out for uh I can make it stretch out for a year um but uh yeah
[2725.52 → 2730.48] if it does pass that's going to be you know like kind of a milestone where it means people kind of care
[2730.48 → 2736.22] and uh what I'll what I'll spend my time doing um I mentioned uh early on uh when I was talking about
[2736.22 → 2741.48] how much I like avid I mentioned I'm a big pair programming fan and uh if it passes I'm just going
[2741.48 → 2747.14] to reach out and pair with everyone on wiki I've I've done that I've done the know avid's uh
[2747.14 → 2752.06] pair with me tag right and I've I've uh it's been a while because I've been like heads down coding by
[2752.06 → 2756.18] myself which i kind of actually don't like to do but I've made myself do it to get like all these
[2756.18 → 2760.40] features into wiki before that I was reaching out and pairing with tons of people like I paired with
[2760.40 → 2767.42] a lady in London uh this really awesome dude I connected with in um Argentina and then people
[2767.42 → 2771.50] you know half of have been remote and half have been people in San Francisco
[2771.50 → 2777.76] I've met at coffee shops and uh done like maybe 25 pairing sessions with people, and they've all just
[2777.76 → 2783.88] been fantastic like even people that weren't super techie like they just had so many ideas of stuff i
[2783.88 → 2787.76] didn't think of, and we sat down and like made a command, and you know a half an hour that just
[2787.76 → 2793.76] whatever shelled out to uh you know that scraped some website and listed like the world cup uh
[2793.76 → 2799.54] you know results um, or you know done something more sophisticated so that's what I want to do
[2799.54 → 2804.90] with my time and I think if I have this you know year of time to just like to reach out and pair with
[2804.90 → 2810.28] everyone that that will be the beginning of something else like uh you know let it'll get
[2810.28 → 2815.16] build up a team of people kind of taking it and running with it and making your own commands right
[2815.16 → 2820.22] and well one thing we talked about recently with uh with chad Whitaker was talk to your users
[2820.22 → 2825.98] because when he came on the show it seemed like he had had this gap between what he thought getup was
[2825.98 → 2833.84] and what he and I think what the users were using it for um where your plan with you know pairing that's
[2833.84 → 2837.90] speaking to your users right I mean if you want to see the success of wiki you're going to have to
[2837.90 → 2844.20] um get in the trenches and speak with people and talk to people and get feedback in real time and
[2844.20 → 2849.68] manage the community i I can't say that your job over the next year is going to be easy so for those of you
[2849.68 → 2854.80] out there listening to the show it's hopefully it's Tuesday um of next week which you don't even
[2854.80 → 2858.78] know what today is, but it doesn't matter you got a few days left to back this thing on kickstarter
[2858.78 → 2864.92] five days left yeah I mean give or take five days to back this project and show your support for this
[2864.92 → 2871.40] if this is something that's uh you know of use to you let's see this thing get done um but yeah i
[2871.40 → 2876.74] can't imagine that you've got the next year of your life that's going to be fun but not easy
[2876.74 → 2883.88] yeah I mean pairing for me makes it easy actually like if i can pair with people like
[2883.88 → 2887.26] I know I'm not going to slack like obviously you can't slack off you don't want to slack right if
[2887.26 → 2892.04] you're pairing with someone um so i yeah I'm actually looking forward to I think i actually
[2892.04 → 2897.04] just got done with the painful part the last like six months of making myself sit by myself now I'm
[2897.04 → 2902.04] like looking forward to kind of getting out there and having fun again actually but yeah if is anyone
[2902.04 → 2909.02] thinks it's cool um check out the video go to xsh.org, and you can see kind of like a better way
[2909.02 → 2914.90] of running shell commands for many use cases not all right there in the top and especially people
[2914.90 → 2921.98] that work for cool companies um that you know back open source projects and sponsor conferences
[2921.98 → 2928.04] I think wiki is like a really kind of actually kind of cheap way of uh getting a lot of publicity
[2928.04 → 2934.52] uh I think if I can get a few companies to back it can do some amazing things and um yeah looking
[2934.52 → 2938.34] forward to just reaching out and pairing with people again and having a great time
[2938.34 → 2942.24] doing this stuff getting people's ideas you have to be one of his first pairs jarred yeah totally
[2942.24 → 2946.88] I'm ready you guys should both you guys should both pair with me, I promise it'll be fun everyone's
[2946.88 → 2952.68] had a great time doing it sign me up sign you up how do you get on the list wicked uh
[2952.68 → 2960.64] well with you guys I'm you're on the list now uh anyone else just tweets me uh at uh you know
[2960.64 → 2965.72] wiki x i k i on Twitter and just say like hey I want a pair, and we'll, we'll pick a time and do it
[2965.72 → 2971.16] I'm not looking for like commitment we know usually we'll just pick like an hour and if it goes
[2971.16 → 2974.98] well you know if we both like it go for two hours and then no commitment after that I'm not looking for
[2974.98 → 2981.16] people that like try to rope into contributing to the project on an ongoing basis and just like i honestly
[2981.16 → 2986.24] think just reaching out and pairing with people um I mean this is like avid's idea and other people's
[2986.24 → 2993.20] I'm late to the game in it but I think you know just connecting to like you're you're a dev maybe
[2993.20 → 2996.58] you're a junior dev maybe you've been out there for a while you're like sitting around you're like okay
[2996.58 → 3000.84] time for my next project or time to have some like fun and learn some new stuff what better way than
[3000.84 → 3007.60] just to go tweet pair with me or just reach out and spend an hour with someone who like knows a
[3007.60 → 3013.52] project and just have this amazing high energy pairing session where you're just learning stuff
[3013.52 → 3019.58] and firing up firing off questions um like to me that's such a win-win for most people there
[3019.58 → 3024.64] are some people that just do really well coding by themselves uh and those people are super valuable
[3024.64 → 3031.54] um and uh, uh, but you know probably about half the population is very motivated by kind of being
[3031.54 → 3036.82] social and for those people um I think this is going to be one of the biggest ways that people
[3036.82 → 3043.56] just find new projects find new jobs um you know uh find team members there's going to be like hey work
[3043.56 → 3049.22] with me on this, and they'll work with you know three people in four or five hours and then the
[3049.22 → 3053.74] people that hit it off they'll, they'll work a little more, and they'll be like hey we had a great time
[3053.74 → 3057.52] working on you know this little open source thing I was working on why don't you consult with me on my
[3057.52 → 3062.74] project and then why don't you know work for my company or why don't I work for your company like i um
[3062.74 → 3067.60] I think the future of software dev is going to be just so open and embrace and like uh
[3068.42 → 3072.64] um so social that uh i just yeah get excited when I think about it
[3072.64 → 3078.42] let's pause the show for just a minute give a shout-out to our sponsor top towel now we've been
[3078.42 → 3083.10] working with top towel for about a year now almost a year now, and we thought it would make sense to
[3083.10 → 3089.56] circle back and talk to some of our listeners who have applied to top towel and have been accepted
[3089.56 → 3093.58] because only about two to three percent of the engineers who apply make it past their strict
[3093.58 → 3099.44] elite engineering process and Daniel Luzon a long-time listener and fan of the changelog
[3099.44 → 3106.36] is now living the dream he's an elite engineer at top towel and I say living the dream because he's
[3106.36 → 3112.40] now able to have 100 control of the types of projects and technologies he's working on as well
[3112.40 → 3118.64] as the rate he wants to charge Daniel earns 100 of his income as a top towel engineer, and he wanted me
[3118.64 → 3123.82] to pass on his seal of approval of the top towel experience for those of you out there who are
[3123.82 → 3128.28] freelancing or like to test out freelancing you've got to check out top towel if you think you have
[3128.28 → 3135.12] what it takes head to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to get
[3135.12 → 3142.76] started tell them the changelog sent you speaking of speaking and even being social um do you have any
[3142.76 → 3149.22] upcoming since you've done the the the conference track of talking at Rubicon strange loop and others
[3149.22 → 3154.66] do you have any upcoming conferences you'll be at to speak about wiki in addition to like your next
[3154.66 → 3159.04] year of coding and pairing I've kind of laid off on the conferences because they take a lot of time
[3159.04 → 3163.20] yeah I'm glad I did I'm glad I did those conferences because like all the time I spent on the
[3163.20 → 3168.46] presentations helped me with my like uh way of explaining wiki to people and I use a lot of those
[3168.46 → 3175.28] thoughts uh in my kickstarter stuff um I'm going to be on ruby rogues uh excited about that nice
[3175.28 → 3180.52] uh and I think a couple of weeks here uh and if the kickstarter passes yeah I'll probably try to do the
[3180.52 → 3185.24] conference thing again and just really reach out there and start spreading the word I'll get ash out
[3185.24 → 3193.74] there like soon um because it's all of a sudden like really kind of practical now and I'll get
[3193.74 → 3200.40] a one-line installer so you can uh you know hopefully like uh apt get install ash and then
[3200.40 → 3208.06] right away you can type you know ash space dash HTML, and then you can just type some HTML uh you know
[3208.06 → 3213.04] modify the sample it gives you and then um control enter and then bam it shows on the browser and then
[3213.04 → 3221.84] you can type uh ash space dash CSS uh to try out some CSS you can do bootstrap um and then just in a
[3221.84 → 3226.64] couple keystrokes you know have a bootstrap layout that you can just uh type I've got like a wiki
[3226.64 → 3231.84] syntax, and you can drill into some examples you can get a working bootstrap layout uh node rails
[3231.84 → 3237.10] you'll be able to type ash space dash node and then just expand out controller and then modify the
[3237.10 → 3241.34] controller and bam you've got like a know you're trying out things in node controller um
[3241.34 → 3247.12] yeah uh I think that'll that'll uh the ash stuff I think will demo particularly well at conferences
[3247.12 → 3252.48] uh so I'll definitely want to do some of those again like I've gotten perfect feedback uh at
[3252.48 → 3258.50] conferences but people have said like hey seems really cool I don't know how it would fit
[3258.50 → 3264.72] into my workflow like I'm not going to switch to a new text editor um in my text editor now i kind of
[3264.72 → 3272.82] like it how it is um so people haven't uh my cat doesn't like it the cat's a vim user and won't
[3272.82 → 3281.46] talk to me um but uh yeah now that I've got ash out there that answer to that objection is
[3281.46 → 3287.64] easy it's like oh here's how you incorporate it next time instead of doing uh you know uh PS and
[3287.64 → 3292.82] then uh kill you just do ash space PS or next time you're doing a git, and you forget a command you just
[3292.82 → 3300.68] do a ash space git, and then you can um you can drill into the output you can also see code this is a
[3300.68 → 3304.62] couple kind of cool features these are a couple kind of cool features I haven't mentioned yet um
[3304.62 → 3311.30] slow down I'm starting to stutter getting too excited there are a couple of cool features with
[3311.30 → 3316.54] shell commands uh where you can look at the history of a command and narrow down and rerun it
[3316.54 → 3325.20] you can also mark you know commands with particular options as favourites, and then you can um type ash space
[3325.20 → 3330.86] dash f git for example, and it will show you your favourites, and then you can pick one and run it
[3330.86 → 3336.82] again nice um, and you can also there's documentation kind of that comes along with it where you'll see
[3336.82 → 3344.60] like the examples for common ways of using the git command like uh you know you'll, you can drill into
[3344.60 → 3351.88] examples I think ash space uh dash e uh space git that'll show the examples that's probably how it'll
[3351.88 → 3357.88] it'll end up being, and then you can drill into like undo just move your cursor down and expand undo
[3357.88 → 3362.54] and it'll say like you know undoing the changes to one file, and it'll show you that it's that you
[3362.54 → 3367.06] know that's the git checkout command, and you can just actually run it right from there and then you
[3367.06 → 3372.74] know undoing your repository git reset and then undoing it and wiping out your changes git reset dash
[3372.74 → 3379.36] so now you can actually kind of uh drill in to those examples and then run them uh right from where
[3379.36 → 3383.72] you're you're looking at the documentation that sounds really powerful for beginners who are
[3383.72 → 3389.52] trying to you know learn a specific tool also for you know even power users who you know I've been
[3389.52 → 3395.02] using the git command for years, but there's you know there are things in there that I have never come
[3395.02 → 3401.00] across, and you can kind of this it uh amps up the discoverability yeah when you're navigating a tree
[3401.00 → 3406.34] structure than if you're trying to you know google around for how do I do this and get yeah totally and
[3406.34 → 3410.40] and you know to all you command line people that say the command line works great I totally agree i
[3410.40 → 3416.72] love the command I'm not looking to replace man etc uh like basically I'm building on top and adding
[3416.72 → 3422.28] a few new features that work in some use cases uh I'm not saying they're better across the board but
[3422.28 → 3427.10] but sometimes you know having more options is kind of awesome I'm really looking
[3427.10 → 3433.28] forward to um getting people to contribute to these like uh you know I've added a few of my favourite
[3433.28 → 3437.82] get examples on my own but once I get this out there and get people using it and adding their own
[3437.82 → 3443.78] uh you know menu items underneath the get examples I think it's going to turn into something really
[3443.78 → 3448.98] awesome I think one feature to that you may not have really touched on that I think is kind of like
[3448.98 → 3454.14] a little hidden gem is like you can even browse databases you got support from my sequel rethink dB
[3454.14 → 3458.48] because you're a fan of it couch dB and all the other you know awesome DBS out there but
[3458.48 → 3463.68] being able to even you know dive into a database and browse around like that that's even kind of
[3463.68 → 3468.60] neat as well and I'm assuming just because of what you've said already that you can even run commands
[3468.60 → 3476.32] and interact with the output and save back to the database yeah that'll now be uh ash dash tables
[3476.32 → 3481.48] that will list out your database tables, and you can type to narrow down or move your cursor down and
[3481.48 → 3486.82] expand a table, and it will show you the records, and then you can type to filter those down, and then you can
[3486.82 → 3494.72] just edit in line um and then Ctrl e to save that back to the database yeah that's uh something that
[3494.72 → 3501.42] in my uh presentations I always get a good gasp from the audience at that point i was going to say I was
[3501.42 → 3505.46] like that's that's where I fell over I almost fell out of my seat when I read that part of the
[3505.46 → 3511.14] the Dom editing also people really like when I show uh expanding out the Dom and then updating the Dom
[3511.14 → 3516.96] and having it reflect in the browser right away yeah that's that's intense right there jarred is
[3516.96 → 3520.86] anything else you want to cover before we go into our traditional super awesome questions
[3520.86 → 3526.02] no just to say you know for anybody out there who wants to see this in action looks like zicky.org
[3526.02 → 3532.32] slash screencasts has a bunch of stuff up there of course the kickstarter page also has a handful of
[3532.32 → 3538.62] things yeah the slash screencast is a little out of the day I need to update that uh yeah xsh.org has a
[3538.62 → 3543.30] really cool it's the newest uh screencast at the top and then that has a link to the kickstarter
[3543.30 → 3548.24] which has the newest videos cool well even so I mean you know even if they're a little data you
[3548.24 → 3552.04] can go there and get excited about where it's been, and you can only imagine where it's going so
[3552.04 → 3555.60] yeah yeah don't feel like you can't go and watch them because jarred you were probably impressed
[3555.60 → 3562.08] right yeah I was watching uh can your shell console do this which is that first one about a three minute
[3562.08 → 3566.44] video where you kind of build like what if it could do this what if it could do this and then yes I like
[3566.44 → 3572.74] that one as well it can that was very uh were you guys like were you guys super annoyed by my
[3572.74 → 3578.56] repeating what if you could no not exactly I mean I got so hammered for that I didn't think so
[3578.56 → 3582.12] I mean I felt like you were trying to make a point when you make a point you repeat yourself
[3582.12 → 3586.78] I've deleted like 10 YouTube comments that were just what if you could what if you could what if
[3586.78 → 3591.14] you could what if you could what if you could what if you could not place a comment here and go away
[3591.14 → 3597.54] that's I deserve it I mean i I hammer other people's projects to haters what happens when
[3597.54 → 3604.54] you throw yourself so 80 grand you're looking for 80 grand on this kickstarter um yes could be as much
[3604.54 → 3608.76] as five days left when you're listening to this you're about halfway right now at the date of
[3608.76 → 3615.78] recording um and today's date is friday, July 11th uh just so everybody's aware the show should be out
[3615.78 → 3622.58] um July 15th so if you're listening to it July 15th, or after you've literally got days possibly
[3622.58 → 3629.74] even seconds to go and back this thing so uh you can, you want to do a quick rundown maybe of a couple
[3629.74 → 3634.62] of your favourite not all of them but a couple of your favourite um rewards is that what they're called
[3634.62 → 3638.18] yeah rewards and kickstarter like some of your favourites maybe just kind of
[3638.18 → 3644.38] glaze over some of the cool ones that uh that stand out yeah yeah um for 35 bucks you can get a
[3644.38 → 3650.40] wiki t-shirt it's an American Apparel 50 50 really nice t-shirt um I did a went back and forth with
[3650.40 → 3655.96] the design uh like five times to get it right uh it's really nice digital print with a gradient on it
[3655.96 → 3664.82] um, and then you can do I think for what do I have it for uh 300 I think um you can do a pairing session
[3664.82 → 3670.40] with me um let me bring up the page so I can tell you the actual number I've got a couple different
[3670.40 → 3674.28] ones with pairing session that's one of my favourites because I love to pair people pair
[3674.28 → 3683.44] with people um you can pair with me on a menu for your project um and I'll include it in the wiki
[3683.44 → 3691.14] distribution um I think that's the uh currently the uh, uh early bird ones are sold on that i
[3691.14 → 3697.16] think so now it's um 300 um which i think is a good way to fund an open source project if
[3697.16 → 3701.96] you're transparent about including people's stuff, and it doesn't get in your way and users can override it
[3701.96 → 3707.02] uh that's kind of one of my plans like uh after the kickstarter I'll say for a company that's
[3707.02 → 3713.36] got like a know commercial project, and they want their command included uh just for you know
[3713.36 → 3717.46] for a few hundred I'll just stick it there by default it won't get in anyone's way if they don't want to
[3717.46 → 3722.38] use if it's not going to pop up at them and say like hey this needs to be used it'll be just
[3722.38 → 3727.50] if they type that you know if you type Heroku or whatever it'll be there for you to use and the
[3727.50 → 3734.40] commands are so they're so tiny there's a few k or a few not even a k a lot of times of text that
[3734.40 → 3740.04] they don't bloat anything um there's a reward there where you can pair with me and I'll make a video
[3740.04 → 3746.10] of the um of the know little command that we make for your tool your project and then I'll publicize
[3746.10 → 3756.06] that uh my absolute favourite one is the ten thousand dollar uh category which why is that
[3756.06 → 3760.98] because it's ten thousand dollars and right now there are zero okays so right now there's zero we
[3760.98 → 3767.82] want at least one maybe two maybe five would if I would make this a kickstarter pass that would
[3767.82 → 3771.98] be amazing there you go i think with three we could still get it to pass so with that I'll put
[3771.98 → 3778.50] your logo on xsh.org and ziki.org we can make it kind of big if you want because like it's totally
[3778.50 → 3786.46] worth that and I'll spread the word everywhere that your company rescued wiki and um I'll tweet I'll
[3786.46 → 3794.30] send uh emails to my what is it 1300 backers I've got a couple of thousand Twitter followers I'll tweet it
[3794.30 → 3799.90] a lot um because honestly it's like it's in my interest to spread that out right now as much as I can
[3799.90 → 3805.46] because that will encourage other companies to back it a lot I'll tweet it a lot I got a question
[3805.46 → 3812.60] for you um and I don't want to be a Debbie downer by any means but I'm thinking maybe the audience
[3812.60 → 3819.46] might be thinking what will Craig do if it doesn't if it doesn't succeed if it doesn't if this kickstarter
[3819.46 → 3829.34] fails and doesn't fully fund yeah uh thanks Debbie downer just kidding um no I'll just kind of
[3829.34 → 3835.56] regroup at that point I'm going to keep working on it regardless plan b then i kind of thought about
[3835.56 → 3840.88] maybe doing a smaller campaign for just ash but god the thought of like redoing all this again and
[3840.88 → 3845.60] trying to be like a cheerleader again and saying like hey everyone remember me well now I'm like
[3845.60 → 3849.98] you've got this big thing again I'm harassing you about like I'll probably take a break if I do it
[3849.98 → 3856.84] maybe a smaller one for just ash but uh I'll keep working on it for myself regardless because I've
[3856.84 → 3861.16] used it for myself I can't stop working on it like I've got all these things that i
[3861.16 → 3866.70] see as like obvious next steps like using uh the tree structure as actually a data structure it's
[3866.70 → 3875.32] sort of like a combination of a hash and an array um and like all kinds of stuff that i and make i
[3875.32 → 3880.12] want to make a little generator where you can take these two space indenting structures and generate a
[3880.12 → 3884.36] pebble app and that's like that's easy to do I think and like to generate the code for pebble
[3884.36 → 3889.58] app during the code for iPhone so I'll keep doing it for myself I just won't jump in and do sublime
[3889.58 → 3894.10] support and vim support right away because I'll have to probably actually get back to another project
[3894.10 → 3902.18] to make money other ways basically, so this is literally saving Ricky for the yeah for the for
[3902.18 → 3907.58] the time for the time I mean it'll still live on but the trajectory the feature set the direction
[3907.58 → 3913.88] the future that you painted out during this show all of that just in case no one's listening all of
[3913.88 → 3921.22] that is not exactly riding on this, but it's certainly going to lift it up it will give Ricky a very strong
[3921.22 → 3928.86] chance of playing a big role in the uh immediate future of tech and bringing this you know what i
[3928.86 → 3936.06] think is just something that the world absolutely needs a dead simple structure for you know defining a
[3936.06 → 3941.44] uh working UI, and you know we can spread that to the world it's open you can incorporate that into
[3941.44 → 3948.42] your projects um you know it's its it's its very open like I feel like if we want something like
[3948.42 → 3953.00] super, super open that's going to like to take all these devices that are out there now that have these user
[3953.00 → 3958.32] interfaces and make and you know an open language and structure I feel like we as developers have to do
[3958.32 → 3965.72] it ourselves like companies are have vested interests in making their own proprietary languages like if we want
[3965.72 → 3970.74] another like HTML which is revolutionized the web and like before that it was like AOL they controlled
[3970.74 → 3977.22] every you know the America online which was great, and you know they couldn't like to make a standard
[3977.22 → 3980.94] themselves they just had to make something that worked for them, but you know it was so far
[3980.94 → 3987.42] from being open and the rev the HTML basically just made everything possible like mobile wouldn't be
[3987.42 → 3992.72] mobile without HTML um you know it just revolutionized everything and made everyone
[3992.72 → 3998.56] you know able to be a web developer and just made everything spread we need HTML for like a
[3998.56 → 4003.74] general purpose UI like we need that, and it's got to be like as simple as possible like trends right
[4003.74 → 4006.62] now are moving that direction anyway if you like new languages like coffee script instead of
[4006.62 → 4011.60] they're like moving the direction of just like you know you do like uh here's my class and then
[4011.60 → 4015.90] underneath that I've got like you know a colon and underneath that I've got b colon so it's its
[4015.90 → 4020.54] happening now you know like it like the world is moving that direction let's make it you know let's make it
[4020.54 → 4026.22] open and as flexible as possible and take control of it ourselves you know cool well lets uh let's
[4026.22 → 4030.96] lets uh what's the call to arms I guess besides back it which we've which pretty much punched that
[4030.96 → 4036.32] in the face um what is the call to arms for the community how can people step in how can people
[4036.32 → 4041.64] help out besides I guess or I guess you can say backing if you want, but that's that's I think it's
[4041.64 → 4048.46] pretty obvious uh yeah how about reach out to companies and get them to back it like I actually had to
[4048.46 → 4055.22] late last night i I tweeted this uh Twilio thing saying hey uh everyone help me um get Twilio to
[4055.22 → 4061.22] back this like after this I'm going to make another uh video for uh probably Mozilla and a couple other
[4061.22 → 4067.60] companies um and the first ones that do it are going to get going to get like the most press
[4067.60 → 4074.10] so if you work for a cool company that donates to open source and uh sponsors you know uh
[4074.10 → 4078.80] cool conferences like seriously walk to the office and say like hey check this out
[4078.80 → 4086.62] you will get a bunch of press if you support it okay um yeah everybody uh tell your friends
[4086.62 → 4093.22] tell your co-workers tell your boss tell your leaders to support this if they can um you were
[4093.22 → 4098.26] you were my best friend right now and uh let's talk about programming hero like uh we've talked a bit
[4098.26 → 4102.48] about your history a bit but so do you have any programming heroes you want to plug here on the
[4102.48 → 4110.86] show today yeah uh ward Cunningham is my programming hero only one uh I would say DHH also
[4110.86 → 4116.68] with rails but ward Cunningham is definitely uh at the top like i he's he's the
[4116.68 → 4122.90] guy that wrote the original wiki um I remember working for a bank on a pretty cool team, but you know
[4122.90 → 4127.82] if you work for a bank it's its about money it's not about programming it's about not crashing the
[4127.82 → 4133.26] prod server and losing a million dollars you know in a half an hour so I was kind of like disgruntled
[4133.26 → 4139.00] by all the structure that everyone had to go through and uh this guy joined our team, and he installed a
[4139.00 → 4143.06] wiki and I remember looking at this you know seeing a wiki for the first time and thinking like
[4143.06 → 4150.36] holy crap that's you know you can do that like this breaks every rule that I've learned in school
[4150.36 → 4156.26] and with like structure like you know uh you just make you know i think every programmer
[4156.26 → 4161.46] should make a wiki like new programmers just an exercise you just like make one database table
[4161.46 → 4166.74] with a column of like name and then a column of contents, and then you give people this big text
[4166.74 → 4171.10] area we can just type in any text, and then you like search and replace these little like syntaxes
[4171.10 → 4180.34] like equals into you know headings HTML headings and with this like you know two fields and um
[4180.34 → 4183.84] searching and replacing and then of course you make links too you make a structure for links
[4183.84 → 4192.36] you've got this incredible uh you know versatile system that you know turned into Wikipedia basically
[4192.36 → 4200.26] and you know defeated uh and CARTA and all these like highly structured uh gooey tools so that
[4200.26 → 4207.22] just that just was like an awakening for me like i kind of i I felt like before that point I almost had
[4207.22 → 4212.14] the idea of doing something kind of like a wiki but never even dared to think about or suggest
[4212.14 → 4218.26] it because I knew I'd be laughed at like oh here 's's this guy's uh design for the system he's
[4218.26 → 4222.14] going to have a big text field and dump everything else into it and search and replace like you know
[4222.14 → 4231.04] lets uh let's not hire this guy um but uh yeah ward Cunningham is a hero because he does stuff like
[4231.04 → 4238.22] that, and he also has like these huge like oh, oh design pattern chops like the first wiki was for
[4238.22 → 4245.00] augmenting the Portland uh pattern repository which is like a bunch of strongly typed oh, oh design
[4245.00 → 4253.10] patterns so he's this guy that can use this you know high abstraction and complexity where it's
[4253.10 → 4258.86] uh where it fits and does a good job and where he sees an opportunity just to like to do this really
[4258.86 → 4267.54] flexible thing uh he'll just do it um and uh i I've I've sort of uh tried to adopt that seems like
[4267.54 → 4272.96] he's like uh on the patterns and extreme paragraph sorry patterns and extreme pair programming or
[4272.96 → 4276.92] extreme programming I want to put pair programming in there because you said a couple of times then well
[4276.92 → 4281.98] he actually he was like one of the guys he and uh like was one of the guys that invented pair programming
[4281.98 → 4289.40] uh which I also like I'm obsessed with right, right that's that's um we'll link him in the show notes
[4289.40 → 4294.28] as well ward thank you for your awesome service to the software development community that's yeah check
[4294.28 → 4299.94] out uh check out uh his projects he's working on some really, really awesome stuff I've actually
[4299.94 → 4304.46] had the opportunity to uh skype with him for quite a while, and he's he's brainstormed with me
[4304.46 → 4310.84] and wiki um smallest federated wiki is what he's kind of designing its his project it's sort of the
[4310.84 → 4315.36] next version of a wiki where it's that's federated out you can have your own and share it's its kind
[4315.36 → 4321.60] of mind-blowing uh check it out well um Craig I want to say thanks man for coming on the show today
[4321.60 → 4325.82] it's certainly been great to kind of get to know you and what you're doing with wiki and the future
[4325.82 → 4330.66] of it um you know all I can say is you know we hope that when people listen to this they get excited
[4330.66 → 4335.88] about it, and they go and back your kickstarter, and they help save wiki from a different future
[4335.88 → 4340.06] um and, and thanks for coming on the show let's lets uh everyone say goodbye
[4340.06 → 4342.64] yeah, thanks so much guys I had a great time
[4342.64 → 4356.82] you
