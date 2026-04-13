[0.00 --> 16.42]  welcome to go time your source for diverse discussions from all around the go community
[16.42 --> 23.54]  we are back new year same go adjacent podcast goodness we have a lot of fun stuff in the works
[23.54 --> 29.58]  so subscribe now and hang with your fellow gophers throughout 2023 thanks to our partners at fastly
[29.58 --> 35.12]  for shipping our shows super fast all around the world check them out at fastly.com and to our
[35.12 --> 42.22]  friends at fly host your app servers and database close to your users no ops required learn more at
[42.22 --> 56.08]  fly.io okay here we go hello there and welcome to this very special new year's edition of go time
[56.08 --> 62.12]  i'm matt riah today we're having a special new year's fireside chat and where i'm from it's
[62.12 --> 66.62]  traditional this time of year to thank people for all the hard work and all the effort that goes into
[66.62 --> 71.80]  things they do across the year and i just want to say thank you to all the wonderful co-hosts of go
[71.80 --> 78.46]  time uh natalie angelica chris johnny ian john and all the guests that join us it's such a great show
[78.46 --> 83.16]  i love listening to it and i want to do a special tribute to the editors and the sound technicians
[83.16 --> 89.90]  they go above and beyond i think every year and deserve a bit of recognition just listen to this
[89.90 --> 95.60]  fire crackle at this fireside event it's just you know you can hear it it's in hd it's amazing
[95.60 --> 101.38]  and listen in the distance birdsong they're fading as the winter sun sets across these snowy rooftops
[101.38 --> 108.06]  you can almost hear water trickling underneath the frozen surface of a stream right so not just water
[108.06 --> 114.20]  it's underneath kind of a layer of ice so it's muffled in some way isn't that beautiful an
[114.20 --> 119.02]  articulated lorry careens around an icy corner three chickens emerge and cross the road without
[119.02 --> 124.54]  mention and the camera slowly zooms into a fire around which there are some people having this
[124.54 --> 131.46]  fireside conversation i wonder what they can hear let's meet the guests and my co-hosts it's john
[131.46 --> 137.60]  calhoun hello john what can you hear hey matt i hear a tea kettle as it begins to boil over the fire
[137.60 --> 143.92]  so i pick it up and slowly pour a cup for everyone oh that's lovely we're also joined by chris brando
[143.92 --> 150.98]  hey chris what can you hear i can hear popcorn popping faintly from the kitchen smells delicious
[150.98 --> 156.72]  and i i hear someone with a salt shaker salting an already made batch it's gonna be pretty good
[156.72 --> 162.26]  oh that sounds great yeah we'll be sharing that popcorn with ian lobshaw is also here hello ian
[162.26 --> 167.30]  what can you hear oh well it's sunny in brooklyn uh the icicles outside my window are dripping
[167.30 --> 174.34]  the subway goes by and it rumbles the building a bit some of the icicles fall free and crash the
[174.34 --> 180.72]  sidewalk you hear a pedestrian yelp and surprise as it falls in front of them oh wow yeah and i heard
[180.72 --> 186.54]  all of those things excellent well let's get started then i just think like this is it
[186.54 --> 194.10]  new year fresh start like i always feel at this time of year that we can really do anything you
[194.10 --> 199.06]  know we can achieve anything and it's really about january the 10th i realize that's not the case there's
[199.06 --> 205.58]  uh life is just as hard as it was but i remain optimistic but tell me like what are you excited
[205.58 --> 212.84]  about anything in particular so i can jump in and say one of the things that i've seen recently which
[212.84 --> 218.40]  i think you wanted to talk about later matt is uh htmx which i haven't gotten to use it but uh
[218.40 --> 222.94]  looking at it was pretty cool yep especially because i always like seeing technology that
[222.94 --> 229.62]  gives us sort of a i guess allows us to sort of build more modern things but also brings it back
[229.62 --> 234.36]  to like the simpler approach that we're kind of used to rather than over complicating things yeah i tend
[234.36 --> 240.02]  to shy away from technology that's really over complicating stuff so for anybody who hasn't seen it
[240.02 --> 245.50]  htmx is like a way of generating html on the server side like you normally would with like a
[245.50 --> 250.24]  static server side rendered web application but it allows you to build something that feels a little
[250.24 --> 256.12]  bit more like a single page application yeah so it's funny because it's like we sort of go on this
[256.12 --> 261.36]  evolution all the time of that's how it used to be it used to just generate html on the server and
[261.36 --> 266.44]  some sites actually still do it like that i think github by and large has this kind of model where
[266.44 --> 271.76]  the server generates all the content and it ships it as one thing and it just gets rendered in the
[271.76 --> 276.84]  front end and then of course we added we started making that front end richer with javascript and
[276.84 --> 284.26]  interact more interactive elements more sort of loading data as you go and so is hmx kind of a mix
[284.26 --> 288.88]  of those from what i've seen it seems very much to be a mix of that but it's also interesting like you
[288.88 --> 293.38]  said you know some sites still do it the old way but like in my mind i think there's way more sites
[293.38 --> 298.04]  generating server-side html than people realize it's just you don't read about them because nobody
[298.04 --> 302.62]  wants to read about technology that's been around working for 10 years they want to read about like
[302.62 --> 308.60]  what somebody just came up with last week yeah isn't php still powering like 60 of the internet
[308.60 --> 315.28]  those are all html server-side generated and they work really well it's just it's one of those things
[315.28 --> 320.52]  that i don't know it's easy to get caught up in the i want the most modern cool thing but i really
[320.52 --> 325.04]  enjoy seeing technology that kind of takes us a step back and like thinks like how can i get back
[325.04 --> 328.90]  to that simpler approach while still getting some of the benefits of what we've learned in the last
[328.90 --> 336.06]  10 years i think it's an honorable pursuit really the simpler stuff is easier to maintain so you know
[336.06 --> 341.68]  there's already you'll get benefits from having stuff simpler and the htmx has the advantage i think
[341.68 --> 346.84]  of like you wouldn't have a javascript framework at all running in the browser so it still does partial
[346.84 --> 352.94]  updates from what i can tell so you still only ask for bits of html to update bits of the page
[352.94 --> 359.52]  but that's kind of done in a declarative way so you still get that ajax-y kind of feel but it's
[359.52 --> 365.12]  obviously much easier than writing all that stuff manually all right matt what are you excited about
[365.12 --> 373.10]  well how could we not mention chat gpt i mean i am quite excited about where ai will take us
[373.10 --> 379.46]  at least just from the sort of thinking of features and capabilities it could be delivered and and the
[379.46 --> 385.08]  sort of interactions you have could be so much more natural it obviously has flaws but have you tried
[385.08 --> 391.16]  chatting with it anyone i have yes what did you ask it i did a couple coding things like generate
[391.16 --> 395.52]  a react element or a component that does this and things like that and i've spoken to other people
[395.52 --> 399.52]  have done things like that in part because like you were saying earlier about keeping things simple
[399.52 --> 404.90]  so you can maintain them i also see gpt as being a tool that could potentially allow one developer to
[404.90 --> 410.44]  do kind of the work that multiple developers have done in the past or like there have been times where
[410.44 --> 414.64]  people said like the full stack web developers kind of going away but i see tools like chat gpt
[414.64 --> 419.50]  possibly bringing that back to have one person who sort of maintains a pretty complex application
[419.50 --> 424.88]  so i like experimenting with stuff like that to see like okay what all can this do can it help me do
[424.88 --> 430.10]  some stuff so i don't really have to like master react or something else that i want to use how do
[430.10 --> 435.02]  you think it compares to like copilot like it seems more versatile but i've not used copilot yet so
[435.02 --> 440.22]  so i haven't used copilot that much because i've been doing a lot of recording for like course type
[440.22 --> 445.02]  stuff and i had copilot on and i was loving it but then i went to record and all of a sudden it would
[445.02 --> 449.44]  like give me a block that was like meant to be the entire lesson i was recording and i'm like well
[449.44 --> 454.20]  that's not very useful if like it just throws it all up there so i'm like well i've got to turn this off
[454.20 --> 457.88]  for the time being because it's not useful can you set spoilers to false it wasn't as useful it was
[457.88 --> 465.08]  like too useful yeah i used it i used copilot and yeah found it like i don't think it's gonna well
[465.08 --> 470.62]  i don't know about this idea of it replacing people like but when you're writing code that's a bit
[470.62 --> 477.12]  repetitive but has a pattern that's predictable like sometimes in unit testing like you sometimes
[477.12 --> 483.38]  end up writing a list of things it does that stuff very well picks example data very well and so it
[483.38 --> 488.74]  does you can see it's kind of carrying a lot of context but you still have to select from that
[488.74 --> 493.74]  you have to choose still what's right and what's wrong so you are still very much in control of
[493.74 --> 499.88]  what code goes in the best way i've seen it like described is like it can make developers much more
[499.88 --> 505.64]  productive but i don't expect my mom to suddenly start building web applications next week like no
[505.64 --> 509.02]  matter how powerful it is i think there's always going to be some limitation that you kind of have to
[509.02 --> 514.14]  have an understanding of what's going on yeah is your mom not wet not in web is she more like
[514.14 --> 520.58]  she's not in web back end she's more of a hardware person oh my hardware yeah no she does not program
[520.58 --> 527.40]  at all oh not yet i think it's uh with chat gpt and also to some degree copilot i think we're getting
[527.40 --> 532.12]  a little bit better at understanding that we're not building these things to replace people but more
[532.12 --> 537.18]  to augment and help people something that's been a failing of ai in the past if it's been like oh we're
[537.18 --> 542.72]  going to replace all of these people and all these industries will go away and then like it just
[542.72 --> 547.36]  like immediately fails the nazi test or something like that and i feel like now we're being much more
[547.36 --> 552.64]  careful about what these things are meant to do and we're making them much more effective so i'm kind
[552.64 --> 557.74]  of excited to see us kind of move more in that direction as an industry and start learning from
[557.74 --> 562.42]  the mistakes we've made in the past some of these confuse me though because like i saw i have a friend
[562.42 --> 567.92]  who plays roblox with her kid and the one game she was playing was like gas station attendant like
[567.92 --> 571.96]  you're basically working as a gas station attendant and i'm like i'm just imagining somebody building
[571.96 --> 576.56]  ai that learns from this to like like i don't know like is that really a fun game like it's just so
[576.56 --> 580.02]  weird to me but i'm like i could see somebody building an ai that's like let's learn how to be
[580.02 --> 584.92]  a gas station attendant from all these people but like you said all it takes is a couple kids who
[584.92 --> 588.74]  when they're playing a game usually you're like how can i break this or do something silly
[588.74 --> 593.32]  so it's like where do you actually get the data to learn from for this stuff not sure i'd be happy
[593.32 --> 599.00]  with a terminator doing the petrol i'd just be worried like also if it walks around it probably
[599.00 --> 604.24]  makes sparks that's dangerous to have a petrol station and then it's always asking about john
[604.24 --> 608.78]  connor and it's like i don't know john connor can you just give me unleaded it like forces you to use
[608.78 --> 613.66]  like the least environmentally friendly gas yeah exactly because it's paid for by big oil it's like i'm
[613.66 --> 621.94]  gonna kill all these humans yeah it's a shell terminator shell the best terminators at some
[621.94 --> 626.90]  point there's that we are gonna get in legal trouble hopefully we don't kick the year off
[626.90 --> 632.60]  that way you think shell is listening to our podcast and giving us grief yeah maybe we should
[632.60 --> 638.44]  just offset that and just say shell we do a great job just do a little nice advert for them as well
[638.44 --> 643.74]  you never know shell could write all of their software and go it's possible that just means we
[643.74 --> 648.46]  need to like say a couple nice things about their gas i'm sure they've got some sort of additive they
[648.46 --> 655.40]  put in it or something they say it cleans your engine so oh i find it hard to believe that something
[655.40 --> 660.24]  that's burning gas in your engine is actually cleaning it might help a little bit but well if it does
[660.24 --> 666.12]  clean your engine doesn't that mean all that dirt goes out the exhaust so it pollutes me yeah keep it in
[666.12 --> 671.36]  your engine just dirty dirty boys and girls we don't want that in the air and in our lungs
[671.36 --> 676.98]  no but do clean up the air actually that's something i get quite excited about is innovation
[676.98 --> 684.84]  in climate technology you know more awareness around like clean cities and the london low there's a lot of
[684.84 --> 690.66]  people annoyed our drivers annoyed but the there's the extending the low emission zone in london to be a
[690.66 --> 696.46]  much wider area so this means you basically pay if you have a car that's giving pumping poison into
[696.46 --> 701.20]  people so you yeah you can still put poison in people but you're gonna have to pay for the pleasure
[701.20 --> 706.76]  which is better than it just being free when they used to just be able to put poison in you for free
[706.76 --> 713.56]  so i'm quite excited about new technology new innovation there and what could come a lot of that
[713.56 --> 718.64]  stuff is definitely intriguing i guess i'm kind of i'm in a weird position where i drive a
[718.64 --> 724.62]  bigger truck that burns gas right that's partially out of like necessity like right now they're like
[724.62 --> 729.96]  the f-150 electric truck just doesn't work for a lot of the things i want to do so like an example
[729.96 --> 733.44]  is if you want to haul a camper or you want to haul a trailer with new equipment or something on it
[733.44 --> 738.54]  it's got very limited range at the moment so i'm like optimistic to see where it can go especially
[738.54 --> 744.60]  when you see like didn't tesla recently released their semi truck their electric semi truck so like
[744.60 --> 748.58]  seeing that and it has i think it's supposed to have like a 400 mile range which is fantastic the
[748.58 --> 753.30]  problem with like the f-150 lightning is i think the range when you're towing is like 120 miles or 150
[753.30 --> 759.36]  miles and then you have to charge for like an hour and that's not really gonna work that well yeah so
[759.36 --> 764.90]  i'm curious to see where it goes but i have to like refrain myself from getting too excited because i
[764.90 --> 768.60]  know it's not going to work for me so i don't want to get excited about something i can't like have
[768.60 --> 773.52]  why do you need the 400 miles range is that just how close the nearest shops are to where you live
[773.52 --> 777.18]  it just depends on like what you're doing or where you're going like an example is like if you've
[777.18 --> 781.58]  only got 120 miles that means you can basically get to someplace an hour away and get back without
[781.58 --> 785.28]  a charge yeah and sometimes you're going places that don't have electricity to charge while you're
[785.28 --> 789.74]  there are you going places that don't have electricity i am actually going to places like
[789.74 --> 795.16]  that i also drive to like north carolina quite frequently which is like 360 miles don't they have
[795.16 --> 799.18]  electricity there i mean they have electricity there but like i'm not going to get there in one trip
[799.18 --> 803.02]  right yeah i got it and then the other part of that is like if you go to charge with a trailer on
[803.02 --> 807.16]  no like because i have a camper we go camping a lot and if you try to charge with a trailer on
[807.16 --> 811.70]  trying to find a charging station that you can pull into and be like hey let's plug in and take all the
[811.70 --> 817.06]  stations with my trailer yeah like that's not going to make anybody happy right i think electric cars are
[817.06 --> 822.24]  one of those interesting places where it's like i think we got the innovation slightly wrong by trying
[822.24 --> 827.44]  to like go all in with like let's put giant batteries in cars and i feel like the what was it like a
[827.44 --> 832.88]  chevy bolt or volt whichever one was like the hybrid but it was like oh we have like a small gas engine
[832.88 --> 838.16]  and we have a bunch of batteries and the batteries will get you like 60 to 80 miles or whatever and
[838.16 --> 841.48]  then you have the gas engine for if you want to go further it's like that's the perfect model for like
[841.48 --> 847.04]  so many people and it would have just like eliminated gas for so many people and it feels like that was
[847.04 --> 851.50]  like that type of hybrid model would have gotten us further faster and instead we're just trying to
[851.50 --> 855.00]  be like no we're going to build things that don't have gas at all and then it's just like
[855.00 --> 860.14]  very tricky to actually make those things work i feel like we do that a lot in tech as well so it's not
[860.14 --> 865.16]  just like yeah the one upside though to like going all in the way they did is i feel like it really
[865.16 --> 870.16]  forced the like infrastructure for charging stations to really quickly come along so like
[870.16 --> 874.40]  that's an upside to going the way we did but i agree with you that going with the hybrid approach
[874.40 --> 878.62]  for a lot of things is a much easier way to get people in especially when it's like not something
[878.62 --> 882.86]  drastically new you know they can still go to a gas station it's not like a change of what they're used
[882.86 --> 887.64]  to and then there's also like all the i guess i'm kind of waiting to see what the technology
[887.64 --> 892.74]  does for things like weed eaters and like like lawn equipment essentially because we've all
[892.74 --> 895.78]  probably lived somewhere where like you hear people going around running this equipment and
[895.78 --> 900.70]  they run like terrible gas that's like half oil there's burning and like into the environment
[900.70 --> 906.54]  all day long just burning it up and i'm sure that's got to like contribute a lot to pollution and that
[906.54 --> 910.14]  sort of stuff and those things seem like things that you could pretty easily replace with batteries
[910.14 --> 914.94]  where like they could have a truck with like a couple extra batteries on there and just swap out every
[914.94 --> 920.74]  different job site yeah like battery powered lawn equipment is uh those like really cool spaces
[920.74 --> 925.72]  especially for like even just like at a human level like leaf blowers are terrible for your hearing
[925.72 --> 930.74]  because they are so loud and just having ones that don't need to be loud because it's just like a
[930.74 --> 937.80]  battery powered thing would be good from a humanitarian perspective as well where do you blow the leaves to
[937.80 --> 942.38]  it depends on where you live like where i live like part of your taxes if you live in the borough
[942.38 --> 946.80]  is they actually pay somebody to come around with like a big truck that has like usually it's like a
[946.80 --> 951.44]  vacuum that sucks them up and mulches them so everybody sort of blows them into a big pile next
[951.44 --> 955.58]  to the road and then the truck drives up the road and sucks them all up and mulches them oh that sounds
[955.58 --> 960.74]  amazing i'd love to watch that happen i've never seen anything like that i'll put a link to that on
[960.74 --> 965.94]  youtube in the show notes for anyone like me that would love to see a great big machine sucking up loads of
[965.94 --> 971.20]  leaves but i feel like this sort of ruining autumn though as well like i'd be like can you just leave
[971.20 --> 975.80]  autumn for a few more days you know it's my favorite season well it's fun when everyone has the giant
[975.80 --> 980.66]  piles of leaves in the front yard like on the street you know it's yeah it's still kind of nice
[980.66 --> 986.90]  oh you kick through them or jump in them have a frolic that sort of thing why not yeah so dogs love to
[986.90 --> 991.86]  like run through piles of leaves as long as they're just running through piles of things and not making
[991.86 --> 996.86]  them that's the danger you never know you can't just jump in assuming it's going to be a nice
[996.86 --> 1003.98]  like a disney film a fresh bed of autumn leaves there could well be spikes in there that someone's
[1003.98 --> 1009.12]  put in maliciously so be careful kids my daughter actually did that when i think when she was three
[1009.12 --> 1013.54]  like we had a pile of leaves and she had seen a video of like a kid jumping in a really massive pile
[1013.54 --> 1017.26]  and this one wasn't that big and we thought she was just going to run through it and she just went
[1017.26 --> 1023.28]  and just like dove like just fell in and she came up crying and i felt so bad and i'm like i did not see
[1023.28 --> 1028.98]  that coming yeah but she hasn't done it since so she learned her lesson i guess yeah well it's a
[1028.98 --> 1033.76]  brutal way to learn you've got to be careful with disney films because i once tried to get loads of
[1033.76 --> 1039.84]  little birds to help me get dressed and took me longer to get dressed if anything it was no help
[1039.84 --> 1045.02]  whatsoever so you just got to be careful what you want what you believe from those animated documentaries
[1045.02 --> 1052.84]  so talking about batteries towards the end of 2022 there was a kind of major breakthrough in fusion
[1052.84 --> 1059.36]  energy and this is something that i'm very excited about because for the first time they were able to
[1059.36 --> 1064.80]  get out more energy than they put in so they put a lot of energy in to sort of spark it and initiate it
[1064.80 --> 1071.34]  and there's a tiny bit of fuel and then that fuel essentially through the reaction ends up releasing
[1071.34 --> 1079.94]  now more energy i think 50 50 more than what was put in so it's kind of viable turns out science has
[1079.94 --> 1086.04]  nailed it again what do you think of this are you excited i mean that was only like at the like
[1086.04 --> 1090.48]  reaction level right they didn't like generate more energy than they put it like they didn't capture that
[1090.48 --> 1097.12]  right right but they got out they saw that was at least possible for the first time i guess that was
[1097.12 --> 1101.74]  the breakthrough right you know you sound skeptical ian you're not into this you don't work for big
[1101.74 --> 1108.92]  oil you don't work for shell maybe maybe um no i mean fusion what do they say it's always 20 years
[1108.92 --> 1114.58]  away yeah never 19 i don't know right i think it would be cool but definitely skeptical i think there's
[1114.58 --> 1121.14]  a lot of challenges to overcome yeah i'm sure that's true but very brutal view there so book your ideas
[1121.14 --> 1126.82]  up science because ian so far is not impressed john are you impressed by that you're excited by
[1126.82 --> 1133.66]  this idea of free clean energy i mean i think all of like any free clean energy tech or even just a
[1133.66 --> 1138.94]  like more efficient energy advancements are interesting to read about even nuclear stuff which
[1138.94 --> 1145.24]  i feel like the u.s especially is very anti-nuclear for the most part but it's interesting to read about
[1145.24 --> 1149.74]  which is weird because you've produced some of the best superheroes that way i'm surprised there
[1149.74 --> 1154.10]  aren't more more support for it so what you're saying is it's not that people don't want nuclear
[1154.10 --> 1157.68]  energy they just don't want superheroes they're worried about that they don't want the mutants
[1157.68 --> 1162.32]  having the special powers and they can like see their wi-fi and stuff that was in one of the shows
[1162.32 --> 1167.10]  one of the shows that i think it was heroes one of the characters somehow could connect to
[1167.10 --> 1174.34]  wi-fi but like so he has to know the http protocols like think of all the stuff he has to know in order
[1174.34 --> 1180.48]  to make that work smart guy i'd like to know like how he developed this superpower yeah because you'd
[1180.48 --> 1183.40]  think that they would have to be like ingrained into him but there's no way he's like mentally
[1183.40 --> 1188.34]  thinking i know oh we better send this header he's like brought up in a best buy and he was able to
[1188.34 --> 1197.08]  learn it from a young age you think you only tap into http no https yeah yeah well obviously they can't
[1197.08 --> 1202.54]  decrypt stuff like that in his brain can you like what's he and what does it look like oh i don't know
[1202.54 --> 1206.60]  anyway i thought you got limitations on the guy who can just mentally connect to wi-fi
[1206.60 --> 1212.38]  yeah you suppose he can not just connect but you effectively use it right i assume i don't know
[1212.38 --> 1218.00]  i mean the writers of tv shows never know how any of this technology works so yeah we can't dig too
[1218.00 --> 1222.92]  much into it shame is it i don't know chris every hacking movie i've seen they're spot on
[1222.92 --> 1230.20]  you type launch terminal or something and then you're in yeah you got to get through like this the 20 or 50
[1230.20 --> 1234.82]  firewalls that they got set up and there's a nice gooey giving you a oh you've broken through
[1234.82 --> 1239.32]  this or the hackers have gotten through this many firewalls yeah yeah i love how there's also always
[1239.32 --> 1243.96]  a progress bar for like cracking the password it's like we know it exactly this time we're going to
[1243.96 --> 1248.70]  get the right one yeah yeah we know which one it is yeah i like that you would have a cube the cube
[1248.70 --> 1253.34]  has got to be completely full and then it clicks together one by one as the different sectors are
[1253.34 --> 1259.84]  completed that's also very uh they nailed it sometimes don't they well so fusion energy chris
[1259.84 --> 1265.64]  you've got to be excited about that haven't you i guess i'm kind of here just like nuclear energy is
[1265.64 --> 1271.30]  actually like pretty good and has a lot of the same kind of features but people are like scared of it
[1271.30 --> 1275.74]  because they fear the worst yeah the same thing with like people fearing flying because they're just
[1275.74 --> 1279.70]  like oh but i heard about like some planes that fell out of the sky and it's like yes yeah and you
[1279.70 --> 1284.08]  can probably name most of them which means it happens basically never right and i was watching
[1284.08 --> 1289.86]  some interesting stuff on nuclear fission generation and people are all scared of like
[1289.86 --> 1294.12]  radioactive material but the video i was watching kind of pointed out that like yeah there's more
[1294.12 --> 1301.24]  radioactive material put into the air every year by mining coal than there is from all of the material
[1301.24 --> 1306.28]  generated from all of the nuclear pens we've ever had because there's radioactive stuff all over the
[1306.28 --> 1310.98]  place and mining coal is just doing that and we spew into the air in the process so it's just like
[1310.98 --> 1317.16]  a lot of the fears around nuclear stuff is unfounded but i feel like nuclear fusion could head down the
[1317.16 --> 1323.10]  same path where people could be really scared of the downsides of like uncontrollable things whether
[1323.10 --> 1327.68]  they can actually happen or not yeah so i feel like there's like we have to figure out how to solve
[1327.68 --> 1332.70]  that problem before we can kind of move forward because yeah people people like what they already have
[1332.70 --> 1336.34]  even if what we have is already super dangerous right same thing with like flying where people are
[1336.34 --> 1340.70]  like i'm gonna drive instead and that's like you are much more likely to die while driving than die
[1340.70 --> 1349.00]  while flying so driving is terrifying yeah happy new year everybody yeah i kind of know what you mean
[1349.00 --> 1354.44]  i think fusion is a lot like i don't think it can melt down in the same way i think that has kind of
[1354.44 --> 1359.40]  safety properties but like you say it doesn't the facts often don't matter when we get into
[1359.40 --> 1365.84]  you know don't have a go at the flat earth people you do you i mean it's like most nuclear plants are
[1365.84 --> 1370.84]  designed in a way where they also can't really melt down but people don't believe that so because
[1370.84 --> 1375.00]  it has happened that's it i guess once it's happened well i could also see the fusion one
[1375.00 --> 1381.42]  like doesn't fusion allow us to like simulate things that happen in stars yeah yeah or something
[1381.42 --> 1385.48]  like that so i could see people being like oh we're gonna have like a star that could essentially
[1385.48 --> 1390.32]  explode and like be as hot as the sun or something like i'm not saying that can't happen i'm saying i
[1390.32 --> 1394.28]  could see people like making these weird leaps when they read something or they'll be like hey you
[1394.28 --> 1399.98]  might create a black hole somehow and destroy the planet like that's exactly what i was thinking yeah
[1399.98 --> 1406.26]  well that could have happened that was very unlikely but when they switched on the cern particle accelerator
[1406.26 --> 1411.36]  at that time it was apparently a tiny chance it could make a black hole and swallow the earth just
[1411.36 --> 1415.90]  didn't but you've got to be able to fail it's like we just won't tell anybody yeah ask for forgiveness
[1415.90 --> 1419.76]  instead of permission is that one of those that's it don't worry about it to be honest john even you
[1419.76 --> 1426.38]  just positing what could be made up like that's how conspiracy theories i think start on go time
[1426.38 --> 1432.86]  and they get out of hand we're joking but i don't think they i mean in that fusion experiment i did it
[1432.86 --> 1438.06]  got up to what three million degrees celsius that's pretty hot that could melt some stuff yeah we could
[1438.06 --> 1443.06]  melt the moon if we wanted to with that i reckon i feel like when you get to a certain temperature
[1443.06 --> 1449.20]  it like my brain just does not process like yeah you wouldn't get much thinking done at 3 000 degrees
[1449.20 --> 1454.70]  john no i don't think so once you get to 2 000 you'll be like i'm doing i'm going to step out five
[1454.70 --> 1462.36]  minutes because it's getting a bit the thing about this is so imagine it works and we have these new
[1462.36 --> 1468.30]  power stations they use fusion it's clean it's basically limitless i guess the price of energy
[1468.30 --> 1473.66]  becomes negligible because it's just solved essentially so this is the future i'm painting
[1473.66 --> 1480.36]  what are we then excited about what changes in our lives and i think transport is probably one area
[1480.36 --> 1486.08]  where things are going to change if energy is limitless and free i don't want to burst your bubble
[1486.08 --> 1492.08]  but i don't think energy will ever be free well they're gonna just keep charging us i mean they
[1492.08 --> 1495.70]  definitely have to like pay to like there's got to be a network to get energy everywhere so you've
[1495.70 --> 1499.74]  got to have people you pay for for that stuff negligible i don't know what percentage of the cost of like
[1499.74 --> 1505.08]  running electric company is keeping the power lines up and everything but good point fine so maybe it's
[1505.08 --> 1509.22]  still pay but i don't know it's going to be like your phone bill when you get unlimited data
[1509.22 --> 1515.72]  you can just do as much electric stuff as you like i think if fusion happens and energy is like free i think
[1515.72 --> 1521.04]  all of a sudden desalinating water is super easy and so many people's lives are saved just because
[1521.04 --> 1525.50]  we can give them clean water like a great one that's what i'd be excited about yeah there's other
[1525.50 --> 1531.46]  health ones i think as well like i would get like loads of fridge freezers and have them at the arctic
[1531.46 --> 1537.34]  you know there's big ones that have ice machines on the front jam the front so the ice constantly is
[1537.34 --> 1542.50]  just coming out whenever it's ready and just leave them running and get loads of them like a whole
[1542.50 --> 1547.80]  warehouse full and you're just starting to replenish the ice and cool the planet of the air i literally
[1547.80 --> 1554.58]  think there's a startup that is working on big lasers that beam heat into space in the arctic
[1554.58 --> 1560.92]  to cool it back down like real thing oh really oh wow that's good a lot of science does get invented
[1560.92 --> 1565.74]  on go time i mean it's they're jokes to us but they don't know that i don't know i'm gonna be
[1565.74 --> 1570.72]  contrarian again like some of our problem isn't even power generation it's like our electrical
[1570.72 --> 1575.56]  infrastructure so we can generate more power than we can actually transfer i think it was like in
[1575.56 --> 1580.94]  vermont they wanted to build another i think it was a solar farm and they were basically like
[1580.94 --> 1585.22]  no because we don't have the transmission lines to do anything with this electricity like
[1585.22 --> 1590.72]  it would just go nowhere i mean i also think about places like africa where there's just no
[1590.72 --> 1594.56]  infrastructure like even if we had fusion energy i don't think it would really help them at this point
[1594.56 --> 1600.46]  so like there's a lot of other logistical issues that come into play yeah yeah but it's definitely like
[1600.46 --> 1607.12]  a lot of the energy transfer is is wasteful i guess so we can afford that waste maybe for a bit
[1607.12 --> 1612.12]  so it might give us an advantage i don't know if how good is this wireless power thing
[1612.12 --> 1618.40]  where because i'm like i feel myself like being like my uncle that's skeptical of new technology now
[1618.40 --> 1623.80]  like the idea that as long as a device can just see your phone it sort of beam forms on it and
[1623.80 --> 1630.18]  fires energy at it to charge it i mean i don't think we can get past the inverse square law right so
[1630.18 --> 1638.54]  go on tell us about that i mean as distance doubles power decreases by 4x right so as you go out
[1638.54 --> 1643.68]  turn it up though well then if you step close to it you yeah don't go close to it matt's trying to
[1643.68 --> 1647.70]  tell everybody it's safe while he's also just like beaming it burning anybody who gets near the source
[1647.70 --> 1653.86]  yeah i think you'd need you definitely need to put up some signs and just be like it's recommended
[1653.86 --> 1659.96]  diversion this way around the planet don't go in this line but no do it high up or underground like
[1659.96 --> 1664.74]  yeah i don't know i can't solve all the problems what about drones though like drones i think could
[1664.74 --> 1671.32]  be for transport when we've got unlimited power you could order a drone on your app like a big one it
[1671.32 --> 1676.66]  flies down like a big it's like a car you get in it you can have a couch or a bed you know what i mean
[1676.66 --> 1683.14]  charge your phone plug that in and it flies off and just drops you off places matt you're coming up
[1683.14 --> 1687.14]  with all of the ideas that are like we have good ways of solving these problems already they're just
[1687.14 --> 1692.48]  poorly deployed there's a lot of logistical problems with like that's why like drone delivery
[1692.48 --> 1697.96]  doesn't exist because like yeah the faa requires that you can see the drone while you're flying it
[1697.96 --> 1702.72]  and also just like like a lot of people don't have like backyards and things where you can like land a
[1702.72 --> 1707.60]  drone and also like i don't trust a lot of people i don't trust drones to just be flying it's like the
[1707.60 --> 1712.34]  same thing with like flying cars it's like we can't deal with cars people driving in 2d space i don't
[1712.34 --> 1716.96]  want them driving in 3d space but there's a whole other d to get into if you if you're gonna crash
[1716.96 --> 1722.96]  just go into one of the other d's and plus it would be from the beginning automated only so it
[1722.96 --> 1728.16]  wouldn't be humans driving them i think i like that even less oh that means software engineers are in
[1728.16 --> 1732.98]  charge of making sure this stuff doesn't break and i yeah that's a good point we don't know what
[1732.98 --> 1737.50]  we're doing i mean in matt's defense yeah drones delivering batteries sounds a lot better than
[1737.50 --> 1742.30]  drones delivering missiles yes oh so the drones are delivering what they can just drop down on your
[1742.30 --> 1746.64]  car and change your battery while you're driving along that'd solve your range problem i didn't
[1746.64 --> 1750.22]  know what you were talking about having a drone where you get inside and charge your phone i think
[1750.22 --> 1754.56]  it'd be a little more practical to like drop off a battery and leave but no get you want to get in
[1754.56 --> 1759.74]  it and have that whole experience and it should be able to like get in london at like 9 p.m
[1759.74 --> 1765.34]  and it's going to fly you to edinburgh overnight so you just get in it's like a hotel room you go to
[1765.34 --> 1772.66]  sleep smooth ride you mean like a a sleeper train it's like a sleeper drone but yeah now we've somehow
[1772.66 --> 1778.80]  wound up in vtols and now we're like oh that's yeah it could go on a train like they could fly from
[1778.80 --> 1784.26]  your house and like or pick you up nearby some people have balconies you know in the cities they
[1784.26 --> 1788.90]  could just climb out on their balcony and just climb onto it up some steps do it safely obviously
[1788.90 --> 1793.82]  then you're straight on the drone off you go maybe it puts on a sleeper train it's more efficient
[1793.82 --> 1799.40]  but you're just in this capsule that's got it's just like screens so as far as you're concerned
[1799.40 --> 1802.78]  you could be underground like listen to that you could be underwater listen to this sound
[1802.78 --> 1808.68]  we're underwater now and you can hear that and i don't know we've whooshed out of the ocean
[1808.68 --> 1814.54]  and now we're whooshing you can hear the wind blowing as we fly through the air excellent work
[1814.54 --> 1820.04]  there by the sound crew so when you said that you believe like for the first of january to like the
[1820.04 --> 1824.26]  10th you believe you can do anything with your code yeah or with anything you weren't joking were you
[1824.86 --> 1831.64]  yeah i felt like we could write software for this uh just as an open source project just assume just
[1831.64 --> 1837.82]  mock out the hardware very common practice all right yeah i think we need like a recap of like
[1837.82 --> 1841.32]  at the end of january to be like when you're back to realistic mode
[1841.32 --> 1845.64]  yeah you'd be like no none of that'll work and i'll be miserable like you going no that's not
[1845.64 --> 1849.82]  gonna happen forget it you're right down it's supposed to be new years i think we'll see some
[1849.82 --> 1855.02]  awesome stuff i just i'm looking at more incremental things i guess yeah i feel like the way to be
[1855.02 --> 1860.20]  successful with your new year's resolutions is to set same things that you can actually achieve
[1860.20 --> 1864.90]  okay that's a good idea so let's talk new year's resolutions then because i do have one
[1864.90 --> 1871.14]  and that is to read more fiction i always find as i get into fiction i'm just thinking this isn't
[1871.14 --> 1877.64]  true and then i think i could be reading something that's true and i sort of don't really get on with
[1877.64 --> 1884.34]  it is that sacrilege sacrilege chris i feel like we just need to like swap then because i can pretty
[1884.34 --> 1889.82]  much only read fiction i don't know why just for whatever reason i like when i'm reading it's more
[1889.82 --> 1895.18]  of like a relaxing type thing for me or yeah shutting my brain off when you say swap i mean like
[1895.18 --> 1900.08]  we both take about 50 of what we're reading and somehow like make our brains accept the other
[1900.08 --> 1904.94]  person's 50 yeah so we're swapping some of our brain then basically yeah just a little bit maybe
[1904.94 --> 1909.56]  i'll take your left side and you'll take my left side oh there you go probably could do that if only
[1909.56 --> 1915.28]  we'd uh less safe about our nuclear strategy we could relax the nuclear safety rules and roll the
[1915.28 --> 1919.56]  dice and see what happens i think you could get some stuff like that it'd be great so what do you read
[1919.56 --> 1924.48]  now matt like i read a lot of history bits i've been reading a lot of management books
[1924.48 --> 1929.56]  they're quite interesting i've got a book here called but how do it know which takes you from
[1929.56 --> 1936.42]  a logic gate like nand gates and then tells you how to make a bit and then how a processor works
[1936.42 --> 1941.26]  and kind of all the way up building a computer there's another one online someone talking about
[1941.26 --> 1946.36]  where you go nand gates to tetris which i think is quite cool so it's stuff like that where i feel like
[1946.36 --> 1951.68]  i'm learning something but of course i'm sure you learn things from fiction but you're still like
[1951.68 --> 1956.00]  you're reading for enjoyment it's not like uh like when you say like a management book to me that
[1956.00 --> 1959.82]  doesn't sound like something i'd read for enjoyment it's more like i'm reading this to better myself
[1959.82 --> 1965.68]  yeah that's the thing like i need to just be okay with reading something for its own sake probably
[1965.68 --> 1971.04]  maybe that's it i've revealed too much about myself what's your new year's resolution i have a very
[1971.04 --> 1976.76]  simple one i don't want to buy a new iphone this year i still have the 13 i want to do the full
[1976.76 --> 1984.90]  two years at least ambitious goal i'm gonna resist what feature would you not be able to resist if this
[1984.90 --> 1989.58]  if tim cook gets up and he's like nah you know does it in his voice i can't do it it's offensive
[1989.58 --> 1996.34]  probably how do what's the feature he announces and you're like right i'm throwing that new year's
[1996.34 --> 2002.58]  resolution in the bin i'm having it well i mean if it's anything like the last like six years
[2002.58 --> 2008.04]  nothing like yeah i feel like smartphones are already like smart enough i guess he's like you
[2008.04 --> 2012.92]  never have to charge this ever again you know yeah just it has a fusion power thing in it you know
[2012.92 --> 2020.14]  yeah that'd be good you never have to charge it again but you might get hot if you stand in certain
[2020.14 --> 2026.26]  parts of your house i'm like hoping an apple engineer is watching this and somehow emails ian in
[2026.26 --> 2031.28]  they're like for one dollar you can upgrade it can't be free because he's got to actually buy it
[2031.28 --> 2037.00]  but you just want him to fail essentially just to see how like committed he is to this yeah and apple
[2037.00 --> 2043.02]  because it sounds like an easy resolution okay if someone was like yes new iphone for a dollar i
[2043.02 --> 2048.02]  would fail i'm sorry just it would happen but what if it had little helicopter blades on the back
[2048.02 --> 2054.50]  and you could say like phone come here and then it's like little helicopter blades come on this
[2054.50 --> 2060.26]  listen to them now you can hear them switching on like a little drone up the phone flies comes over
[2060.26 --> 2066.06]  to you and it lands in your hand and you never have to you never lose your phone again i think i might
[2066.06 --> 2072.62]  pay to get rid of that one actually you don't want to find your phone i don't want a phone with spinning
[2072.62 --> 2077.92]  blades on it no yeah be careful do be careful around them they are lethal if you if you're not careful
[2077.92 --> 2082.78]  you gotta duck out the way i feel like i used to be someone that would upgrade my phone every year
[2082.78 --> 2087.62]  and then somewhere along the path i just stopped i guess it was like with the iphone 10 like i got
[2087.62 --> 2092.38]  the iphone 10 and then i like wasn't interested in upgrading and then i was like okay now this thing's
[2092.38 --> 2098.78]  like slow very slow and it's annoying so then i got like a 12 and that's where i am now i'm just kind
[2098.78 --> 2105.58]  of like i don't know i like i was like oh the 13 and the 14 came out i was like yeah i'm like okay maybe
[2105.58 --> 2110.54]  when the 15 comes up maybe i'll be in this like every three year yeah upgrade cycle sort of thing
[2110.54 --> 2116.28]  like i objectively know it does nothing new nothing better like there's no reason to buy it
[2116.28 --> 2123.82]  but i still want it i yeah apple's done a good job advertising to me over the years yeah i don't
[2123.82 --> 2127.64]  think it's just phones that pull that off though like there's a lot of things where people want the
[2127.64 --> 2134.88]  new one even if it's not significantly improved yeah i'm guilty of that a bit but i i also do that
[2134.88 --> 2140.06]  thing try and resist it and two years is what i also try and do like because i used to do that
[2140.06 --> 2145.64]  exact same thing every year like you know there'd always be someone to hand it down to like in the
[2145.64 --> 2150.50]  family there's people so it was always like it's kind of kind of an excuse really i can get the new
[2150.50 --> 2154.78]  phone and then someone else gets a phone and that's like you know i could turn that into a good thing in
[2154.78 --> 2161.30]  my brain instead of a bad thing but yeah i try not to it's not as bad in that sense like my mom's
[2161.30 --> 2165.68]  always done that like my sister gets a new phone my mom takes her old phone right and you know then
[2165.68 --> 2169.52]  they do something with the you know the old one but in that case my mom's running like four years
[2169.52 --> 2174.16]  behind my sister's you know every two years or something so it's not like terrible but and i get
[2174.16 --> 2178.30]  how that makes it easier to rationalize yeah no but that's good he's doing some good
[2178.30 --> 2185.08]  ian's rummaging around in the background there i was gonna try to find my stack of old iphones
[2185.08 --> 2192.94]  he's got like a computer museum wow so ian is definitely not handing them down
[2192.94 --> 2199.22]  well some of them are broken you know yeah oh what happened to that one i have no idea
[2199.22 --> 2203.68]  probably dropped it i'm not a case person so but wouldn't drop it if you had the little blades
[2203.68 --> 2206.70]  on the back because it would just notice with the accelerometers it's falling
[2206.70 --> 2213.36]  and then spins up the little chopper tiny chopper it's called hope no one's around so it doesn't
[2213.36 --> 2217.92]  like chop your finger off or something well if they're around they'll catch the phone yeah that's
[2217.92 --> 2223.88]  not how that works well yeah if they're not good then maybe they deserve a little blade in the hand
[2223.88 --> 2228.64]  just as a reminder you never like fumbled your phone trying to like catch it and it still falls
[2228.64 --> 2231.90]  but you would i think you'd get used to it'd be like i've dropped my phone everyone step back
[2231.90 --> 2236.58]  get back i've dropped my phone you know the first version is not going to be as good are they so
[2236.58 --> 2240.90]  it's going to be a bit more dangerous the blades will probably be enormous as well so
[2240.90 --> 2246.20]  bear that in mind for the first version mvp in it apple's trying to get rid of the sim card slot
[2246.20 --> 2251.72]  and the charger they're like we need more space in the phone they're gonna put blades why do you
[2251.72 --> 2257.56]  think they're clearing out the space for you don't battery but not so far actually that's one thing
[2257.56 --> 2263.44]  when you get a new device like that the battery just seems like it lasts forever in those first few
[2263.44 --> 2269.08]  weeks when you're not used to it and it's probably just is peak performance they just last forever my
[2269.08 --> 2274.92]  when i got my last phone it was like two days that i hadn't charged it and it was still fine
[2274.92 --> 2279.64]  i don't really believe it do you have all your apps installed no i can't use it if it drains the battery
[2279.64 --> 2284.40]  you can't use it at all if you want it to last two days whenever you get a new phone do you transfer
[2284.40 --> 2288.88]  all your apps over or do you like start fresh and like install them as you need them i start fresh
[2288.88 --> 2293.44]  because i used to love setting up devices like because it was so nostalgic for me i'd get like
[2293.44 --> 2299.68]  a computer for christmas maybe and then you know had to learn it and had to just spend hours setting
[2299.68 --> 2306.44]  it up and figuring out what it could do and the workbench or the desktop software whatever and i sort
[2306.44 --> 2312.24]  of like kind of liked that same thing for iphones for a while and then now i'm just like no i don't
[2312.24 --> 2316.70]  want to i don't want the hassle now it's the first time i feel like it's i'm sort of getting old
[2316.70 --> 2323.04]  because i lost that a little bit i feel like i'm getting old when i like don't do updates for stuff
[2323.04 --> 2326.54]  all the time because i'm like i just need to get work done i don't care about updates anymore
[2326.54 --> 2332.20]  when i was young i'd do like every update as soon as i could yeah i've like gone so far on the other
[2332.20 --> 2338.26]  end of the adoption scale now with especially os updates so terrible with os like i'm still running
[2338.26 --> 2345.18]  ios 15 some of my computers are still running the older mac os's i'm just like eh what mountain lion
[2345.18 --> 2350.94]  he's still running mountain lion not that old i feel like the hard part for me is like the minute
[2350.94 --> 2355.24]  you like every time you do an update and it like hurts your productivity or like you spend half a
[2355.24 --> 2358.86]  day trying to fix something because of the update yeah like when you're younger you kind of go through
[2358.86 --> 2361.82]  it and it's like whatever but then you hit a certain point where you've just done it so many
[2361.82 --> 2365.78]  times that you're just like i don't want to waste that time i've got kids and other stuff i need
[2365.78 --> 2370.88]  to focus on this is not something i want to spend a day doing yeah it took me a full week when we
[2370.88 --> 2375.84]  upgraded to m1 max like just to get everything running it was a nightmare
[2375.84 --> 2405.82]  practical ai is a weekly podcast that's making artificial intelligence practical productive and
[2405.82 --> 2411.74]  accessible to everyone if the world of ai affects your daily life this show is for you
[2411.74 --> 2417.76]  from the practitioner wanting to keep up with the latest tools and trends spacey is really a library
[2417.76 --> 2423.02]  that lets you put together a whole nlp pipeline of the different things you might want to do and
[2423.02 --> 2426.98]  extract from your text you know you're not just interested in predicting one thing you might want
[2426.98 --> 2431.78]  to read in your text you want to find the individual sentences you want to find out which concepts
[2431.78 --> 2437.72]  are mentioned in the text like which person names organizations dates and then you also maybe want
[2437.72 --> 2443.70]  to predict something about like what's in the text to the ai curious trying to understand the concepts at
[2443.70 --> 2449.70]  play and their implications on our lives would you rather be spending your time improving your blue
[2449.70 --> 2457.94]  score by 0.1 on french to english or would you rather have a breakthrough on kind of that under-resourced
[2457.94 --> 2465.60]  language that by the way has 350 million people using it in underprivileged areas around the world
[2465.60 --> 2472.28]  here's your expert hosts my name is chris benson i am a principal ai strategist at lockheed martin
[2472.28 --> 2478.84]  and with me as always is daniel whitenak a data scientist with sil international hey how's it going today daniel
[2478.84 --> 2483.72]  please listen to a recent episode and subscribe today we'd love to have you as a listener
[2483.72 --> 2489.18]  i still don't have an m1 mac that was the one that like when you were talking about upgrading that was
[2489.18 --> 2493.12]  the one that almost got me yeah and then i like thought about it and i'm like the few things that
[2493.12 --> 2498.26]  this would speed up aren't things that i can't just like do overnight like you know video processing
[2498.26 --> 2501.92]  or something i'm like i can just do it overnight and come back the next day yeah and it really doesn't
[2501.92 --> 2506.64]  make a difference i think go compiles a little bit faster i don't know i mean i don't care about any of
[2506.64 --> 2512.14]  the compiler thing the thing i like about the m1 and the m2 max is that they have instant awake so
[2512.14 --> 2516.84]  you just open it and it's just on yeah i think i hate it about intel lap like macbooks is that like
[2516.84 --> 2521.34]  you hadn't turned it on in a couple days like over the weekend you open it and then it just like
[2521.34 --> 2527.52]  takes like 10 minutes before it's like okay i'm gonna work now and then fans come on and they're
[2527.52 --> 2532.02]  blowing all this heat out and it's killing your battery it's just an unpleasant experience but with the
[2532.02 --> 2537.28]  apple silicon you just kind of open the thing and it's like oh hello you can use me now i feel like
[2537.28 --> 2543.48]  that's a huge productivity boost yes i agree i'd love to actually track that like it's real to write
[2543.48 --> 2549.40]  like log how much time you gained through the year and it's possible you could no i mean literally like
[2549.40 --> 2556.60]  opening apps i mean you know you still fall foul to standard like an app will sometimes it just gives
[2556.60 --> 2561.54]  you the beach ball of death and then you're spinning for a while but you're not immune from that but
[2561.54 --> 2567.56]  general when stuff's working like you opening like the mail app opens at the same speed as if it was
[2567.56 --> 2572.32]  already open but the window was hidden and you just bring in the window to the front it's like that quick
[2572.32 --> 2580.06]  and i don't know that that's worth something just that i don't know it just feels fast i mean it is fast
[2580.06 --> 2583.64]  it would have been more useful when i still worked in an office but also like
[2583.64 --> 2589.14]  the display engine being so much better where you can just like plug your computer into a dock and
[2589.14 --> 2594.62]  then it just the displays just work and there's not that flickering nonsense that happens where it's
[2594.62 --> 2599.62]  just like trying to figure out how to actually display on all these different screens yeah like
[2599.62 --> 2604.02]  that i wasted so much especially when it would just break and have to like restart my whole computer
[2604.02 --> 2611.36]  and all i wasted so many hours of my life trying to dock or undock my macbook and like that's just kind
[2611.36 --> 2616.40]  of like not a thing anymore yeah but if you if you never have to undock your macbook that doesn't
[2616.40 --> 2620.78]  really matter it's not going to be an advantage to you i also don't think i've ever heard the fans
[2620.78 --> 2627.88]  on this thing you know i used to spin up docker and a jet engine for a good 10 minutes and now nothing
[2627.88 --> 2633.94]  yeah and the battery life that's the other thing like it's not just that it does things faster even if
[2633.94 --> 2640.34]  you can't notice it it's quicker you will notice that i did video editing one day i was doing video
[2640.34 --> 2648.30]  editing and like multiple renders i was doing like docs stuff email slack slack and still had like
[2648.30 --> 2655.68]  70 battery at the end of the day so i can run all four electron apps now and seven chrome tabs it'll
[2655.68 --> 2660.32]  be great starting to feel like this is like an intervention where like john you cannot keep using
[2660.32 --> 2665.48]  that intel mac it's not okay i mean if you're doing like video and audio editing it's like i remember i
[2665.48 --> 2670.82]  watching the reviews and it was like oh yeah we did this compile it was like faster which was cool
[2670.82 --> 2677.78]  but like it used three percent battery on the macbook and the m1 and it used like 80 or 90 percent
[2677.78 --> 2683.88]  battery on the intel and so it's like oh okay well that that's different so i think like those are the
[2683.88 --> 2688.22]  things too where it's like i can actually continue using my computer while it's doing other things or
[2688.22 --> 2694.82]  still have like battery left after i do this long compile or not or this long render or whatever export yeah
[2695.48 --> 2702.48]  also if you're using pro res like the m1 max and m1 pro or just kind of like just hit play you don't
[2702.48 --> 2708.46]  have to render i was still doing video editing that would be so beautiful yeah same for logic pro i use
[2708.46 --> 2714.28]  that music editing software and that used to be i mean this now well i have i also have this ridiculous
[2714.28 --> 2720.60]  machine that's i shouldn't have really done it because i spend most time in email but it's just
[2720.60 --> 2726.72]  unlimited as far as like i've never i don't have time to record that many tracks when making a song
[2726.72 --> 2733.28]  you know so it's like it's beat me now i don't need that much i can i can render songs be rendering
[2733.28 --> 2738.82]  video at the same time like you can just really push it and it does a kind of cracking job and you can
[2738.82 --> 2745.40]  run 10 dock containers yeah you can run docker and a slack and a couple of tabs that's just far too many
[2745.40 --> 2750.60]  docker containers i mean if you're running kind everyone like kubernetes on top of docker you know
[2750.60 --> 2755.84]  you could get a all right we can move away from apple they're gonna i hope they're spending or
[2755.84 --> 2762.10]  sending us sponsorship money at this point yeah they should at least uh sell ian that iphone for a dollar
[2762.10 --> 2767.56]  after all this talk does anyone want to just for balance say something horrible about apple
[2767.56 --> 2773.64]  chris you live in a litigious country i'm not mad at apple right now i don't have anything bad to say
[2773.64 --> 2779.86]  about them you can just be like that darn 30 yeah then move on that mouse you have to flip upside
[2779.86 --> 2785.68]  down to charge or oh yeah that pencil that you lollipop with an ipad i mean they do have some
[2785.68 --> 2791.28]  stupid designs i think when it comes to that 30 thing i'm more mad at the industry and people than
[2791.28 --> 2795.98]  i am at apple and i feel like that's a hot take maybe that's an unpopular opinion oh but like when
[2795.98 --> 2800.60]  the iphone first came out and steve jobs was like we're gonna use html5 for everything and everybody
[2800.60 --> 2805.90]  was like no go f yourself you're gonna build us an app store and they give us native apps and then
[2805.90 --> 2812.54]  they did and then like 10 years later everybody's like hey why are you charging so much money for
[2812.54 --> 2817.60]  this thing that we force you to build and put a lot of money into that's not fair we want something
[2817.60 --> 2821.24]  that's open and it's just like that you could have had it if you had just all worked together
[2821.24 --> 2825.32]  and tried but you didn't want to so you can now like sleep in the bed that you made thank you
[2825.32 --> 2831.52]  yeah you tell them people don't like that yeah i mean in their defense a lot of people complaining
[2831.52 --> 2836.14]  now probably weren't involved in the original decisions yeah but that's not how like you gotta
[2836.14 --> 2840.76]  pay for the mistakes of the past like that's what we all gotta do that's just life just those guys
[2840.76 --> 2844.62]  who are about to retire they're like no no no you go ahead and build something i'll let some other
[2844.62 --> 2849.24]  sucker deal with it yeah i mean like that's how like generational wealth works if it works for wealth
[2849.24 --> 2853.68]  it should work for the bad things too can't only be the good thing i'd be like saying okay well we
[2853.68 --> 2857.56]  can't borrow any code from the past because the people in the past wrote it like if we get to
[2857.56 --> 2862.12]  inherit their code we also get to inherit the other decisions that they made yeah and some of those
[2862.12 --> 2869.46]  decisions were bad ones like not using html5 to build apps and just because like we got there right
[2869.46 --> 2874.14]  like if you look at browser apis now they can do like most of the things that you want to do in a
[2874.14 --> 2878.10]  native app they're still kind of not as advanced as we'd like but they're getting we can do like
[2878.10 --> 2882.68]  bluetooth integration you can do file storage you can do all this stuff so it's possible to get there
[2882.68 --> 2888.64]  but everybody was just like now we want what we like and then we get electron apps and uh i think
[2888.64 --> 2893.64]  what i like best about that is there's literally mobile apps that can do everything perfectly like
[2893.64 --> 2898.14]  reddit's an example but they'll like pop up a big thing it's like would you like to go to the app
[2898.14 --> 2903.28]  though and you're like no just let me see this reddit page in my browser yeah when they invented deep
[2903.28 --> 2908.64]  links i was like okay this has gone too far like you're just reinventing browsers like just yeah what
[2908.64 --> 2912.34]  are you doing yeah that reminds me chris what you're saying in the uk we have the
[2912.34 --> 2918.96]  royal mint and we have the national debt and this is a very kind of uh interesting example of
[2918.96 --> 2925.18]  where you can't have the good and not the bad the royals uh cheeky now we've got a new king though
[2925.18 --> 2929.74]  don't say anything wrong because i think legally can just cut my head off if he wants to i think
[2929.74 --> 2935.82]  that's still an old law that applies so fingers crossed that doesn't happen he's got to make an example
[2935.82 --> 2941.30]  of somebody yeah this is why we got rid of monarchs now we just have whatever we have in this country
[2941.30 --> 2946.18]  yeah chris is like look at how much better it's been over the last eight years yeah but at least
[2946.18 --> 2951.64]  you chose your lunatic i had to go back far enough at least you chose your lunatic i mean comparatively
[2951.64 --> 2957.54]  the uk is not the the shiny example to pick as the they haven't been much better than the u.s they've
[2957.54 --> 2962.84]  had a lot of better trouble there what you mean just like we have yeah a little bit pick like
[2962.84 --> 2968.18]  canada seems to be doing all right right like they don't yeah what's going on there what doesn't
[2968.18 --> 2972.02]  canada have some sort of relationship with the queen though yeah i mean they're still like a
[2972.02 --> 2977.12]  commonwealth country so yeah they still have a monarch so now they technically have a king yeah
[2977.12 --> 2982.06]  i think i don't know if he's allowed to cut their heads off but you know fingers crossed just for the
[2982.06 --> 2987.26]  quality of it i don't wish any ill of canadians but if he can slice my head off with no trouble
[2987.26 --> 2992.52]  i sure as heck hope he can also slice your heads off i don't care how polite you are yeah i don't know
[2992.52 --> 2997.26]  if the king is if that king can actually slice your head off well this is it didn't find out do i mean
[2997.26 --> 3000.54]  that could be the thing in the u.s because you know we have presidents that said they could shoot
[3000.54 --> 3007.94]  people on fifth app and they wouldn't get arrested yeah oh yeah true well there we go have we talked
[3007.94 --> 3013.84]  about go at all in this episode i feel like oh yeah i forgot about that this is ungo time is there
[3013.84 --> 3018.68]  anything in go that we're looking forward to this is kind of new year's chat i mean like when we talked
[3018.68 --> 3024.08]  about htmex it was kind of related because you can use it with go like in my mind it like there's a
[3024.08 --> 3028.00]  little bit of a benefit there so you think we fulfilled our contractual obligation so we can
[3028.00 --> 3033.84]  pretend like we had some go in there cool yeah i know it's not new but i've been looking at code
[3033.84 --> 3042.34]  that uses some generics so there's some code around atomics and i'm like i don't hate this as much as i
[3042.34 --> 3046.52]  thought i would but i think that's because it's being used properly i think if it was being used in a
[3046.52 --> 3052.08]  mess way i'd be very upset about it but i'm like is this the pointer type the atomic pointer that's
[3052.08 --> 3058.20]  typed with generics i think so i don't know well i think it's like in part of tailscales code base
[3058.20 --> 3063.58]  where we just have like a syncs package that has these nice like typed atomic values yeah so you
[3063.58 --> 3067.04]  don't have to do typecasting when you get the value it's just like very nice i'm just like i like
[3067.04 --> 3073.26]  this this is yeah this is pleasant i mean generics were 2022 so i think it's a good time to look back
[3073.26 --> 3078.90]  and they were released in 2022 right am i losing it good question we should check that i'm sure the
[3078.90 --> 3084.36]  internet will tell us it was 118 right that has to have been this last year beginning of 2022
[3084.36 --> 3090.78]  really yeah wow okay and i think there's only one example in the standard library of generics being
[3090.78 --> 3096.34]  used and it is that generic pointer in the atomic package so you can say like the atomic package lets
[3096.34 --> 3102.82]  you protect things concurrently so you can kind of update you can make do operations and guarantee
[3102.82 --> 3106.56]  that only one go routine is going to change that memory at a time so you can have that sort of
[3106.56 --> 3113.20]  safety there and then the pointer thing lets you basically point to any object and you specify the
[3113.20 --> 3118.58]  type and then you've just got the sort of type safety you can't then put the wrong type of thing in that
[3118.58 --> 3124.06]  pointer that would be otherwise possible to do so i think that's that's it it's nice to see those
[3124.06 --> 3129.10]  cases where it's used well and sort of surface them and i feel like that's something we could do this
[3129.10 --> 3134.24]  year in this new year we could do an episode on looking back at generics where have we seen it
[3134.24 --> 3140.64]  used well where have we not seen it used very well and see what what lessons there are there there are
[3140.64 --> 3145.96]  a couple proposals in right now that i'm also excited about like the uh i don't know if it's
[3145.96 --> 3151.92]  actually a proposal or just like a discussion about the like the built-in iterators i don't know if
[3151.92 --> 3158.26]  you all read that yeah do you want to just describe it briefly it's been a while basically there'll be
[3158.26 --> 3163.98]  they're talking about adding so we can use the range operator kind of natively for
[3163.98 --> 3170.22]  custom iterators i think it also changes the kind of the loop dynamic so that the variables
[3170.22 --> 3175.02]  redeclared every time inside the loop so you know that var we have to say like i equals i or
[3175.02 --> 3180.66]  define the variable again that'll go away which i know is one of the big things that causes issues
[3180.66 --> 3185.40]  so that's exciting as well yeah i don't know can someone else explain the iterator thing better i
[3185.40 --> 3190.90]  i haven't read the like post but based on what you're saying that sounds like what i would expect
[3190.90 --> 3194.90]  when you say there's like an iterator proposal it's just something so you can make your own type
[3194.90 --> 3199.32]  and you can do like a four thing in range or you know a range loop essentially over it yeah exactly
[3199.32 --> 3205.32]  and they're defining like kind of two types like a push and a pull iterator i couldn't tell you the
[3205.32 --> 3209.80]  fine details but it covers all of the use cases in the standard library right now which i think is
[3209.80 --> 3215.58]  pretty cool well we'll try and find dig that out and put a link in the show notes for anyone
[3215.58 --> 3222.06]  interested in the iterators i do i mean one of the things i like about the way that it works today is
[3222.06 --> 3226.86]  you know there's nothing nothing magic going on when you range over something because you can only range
[3226.86 --> 3233.50]  over those native types those built-in types so you know what's happening whereas as soon as you have
[3233.50 --> 3238.92]  your own iterator you could be doing expensive operations in there and that would be hidden so for
[3238.92 --> 3244.20]  example if it's paging if you're iterating over some data and once you reach the end of the page or
[3244.20 --> 3248.16]  as you're approaching the end of the page it fires off another request to get the next page
[3248.16 --> 3255.72]  like how is that surfaced and how do you handle failures in that code and like that's i think one of
[3255.72 --> 3261.26]  the challenges that people will have there must be some kind of error handling in this api i guess
[3261.26 --> 3267.16]  yeah i think the function can return an error yeah which is interesting i agree that it's a little bit
[3267.16 --> 3271.72]  weird it's using the range operator to do things like that but i think it outweighs
[3271.72 --> 3278.14]  like there's so many different ways things do iteration now and i think it's unclear a lot of
[3278.14 --> 3283.54]  times how it works and i think there's a whole i don't know a whole swath of errors that we can
[3283.54 --> 3288.12]  or mistakes program mistakes that we can just eliminate yeah i would imagine part of this stems
[3288.12 --> 3294.86]  from the fact that like most other languages have a way to say like for thing in like iteratable thing
[3294.86 --> 3298.92]  yeah and like because of that when they come to go from another language it's not like
[3298.92 --> 3304.50]  historically like when i first started programming i swear that type of syntax wasn't common like a
[3304.50 --> 3308.94]  for loop with like an i equals zero i is less than length and like i plus plus was like the way you
[3308.94 --> 3314.16]  iterated over stuff yeah and then as more languages have introduced this i feel like it's kind of tricky
[3314.16 --> 3319.02]  in the sense that people switching from another language just aren't used to that syntax so what is
[3319.02 --> 3322.88]  clear and readable to me might not be clear and readable to somebody who learned to program in like the last
[3322.88 --> 3327.14]  couple years yeah i mean you're right the higher level languages have let you do this for a while
[3327.14 --> 3333.54]  and again it's like when it's used properly it's kind of perfect the cases we do have to watch out for
[3333.54 --> 3339.46]  is where it gets abused or or where we end up hiding things that are happening but i think as long as
[3339.46 --> 3345.76]  we're careful uh then yeah i'm all for it so i can say like going back to go stuff i think one of the
[3345.76 --> 3349.96]  things this year that kind of excited me was i think it was the first year that go modules didn't like
[3349.96 --> 3355.52]  basically lead to a big issue of some sort or confuse me at some point which i feel like go
[3355.52 --> 3360.04]  modules came out a long time ago but i feel like there's always been like little things here and
[3360.04 --> 3365.04]  there or like the go tooling has changed gradually over time and this for whatever reason felt like
[3365.04 --> 3370.88]  the first year we're like it just worked smoothly most of the year i 100 agree with that this is the
[3370.88 --> 3377.80]  year we upgraded and after one attempt that failed miserably so yeah i feel like i feel like this is
[3377.80 --> 3383.20]  where i wanted go modules to be in 2019 i'm just like the tooling is there i think that's the thing
[3383.20 --> 3388.16]  that's happened is like all of the tooling has come together finally like the language server is like
[3388.16 --> 3392.86]  robust enough now that it can handle most of the things it needs to handle we figured out all of the
[3392.86 --> 3398.66]  kinks i hope like this does become like a a lesson for not just like the go community but other
[3398.66 --> 3402.44]  communities and making sure that like your tooling and everything is there and you haven't like
[3402.44 --> 3409.36]  just bake the idea and put it out there yeah i'm i'm excited that modules finally just feels like a
[3409.36 --> 3414.98]  boring technology that's just kind of like it's there you use it it works you don't have problems yay
[3414.98 --> 3423.94]  nice well on that high note i think good time to end this lovely fireside new year's special
[3423.94 --> 3430.00]  episode of go time thank you so much i really enjoyed that uh it's nice to hang out um i hope you have
[3430.00 --> 3439.94]  and had nice holidays um get to get to have a nice break there pleasure to chat ian john chris until
[3439.94 --> 3447.32]  next time thank you goodbye you can say goodbye and then i'll play the music if you like bye bye everybody
[3447.32 --> 3448.06]  bye
[3448.06 --> 3459.08]  this has been your first episode of go time in 2023 thanks for listening
[3459.08 --> 3464.90]  plus plus subscribers stick around for three bonus minutes that hit the cutting room floor
[3464.90 --> 3471.76]  by matt's request change log plus plus it's better do you have guest or topic ideas for us
[3471.76 --> 3478.28]  let us know at go time.fm slash request and if you get value from the pod pay it forward by recommending
[3478.28 --> 3483.70]  go time to your friends and colleagues send them to go time.fm or just have them search for go time
[3483.70 --> 3488.54]  in their favorite podcast app we're pretty much everywhere you want to listen thanks once again to our
[3488.54 --> 3493.52]  partners fastly and fly for supporting go times continued production to the mysterious breakmaster
[3493.52 --> 3498.94]  cylinder for these dope beats and of course to you for making go time part of your life we love that
[3498.94 --> 3503.08]  that is all for now but we'll talk to you again next time on go time
[3503.08 --> 3514.80]  edit
[3514.80 --> 3519.06]  or
