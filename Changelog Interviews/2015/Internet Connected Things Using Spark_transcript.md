[0.00 --> 15.00]  welcome back everyone this is the change log and i'm your host adam stikowiak this is episode 150
[15.00 --> 22.40]  jared and i talked to zach sapala the founder and ceo of spark spark is a complete open source
[22.40 --> 27.72]  full stack solution for creating amazing internet connected things you may have seen it on
[27.72 --> 34.18]  kickstarter it's fully open source on github from hardware to software and zach goes deep to school
[34.18 --> 40.22]  us on everything we need to know we have four awesome sponsors for the show today code ship
[40.22 --> 45.94]  app quality bundle top towel and digital ocean we'll tell you a bit more about top towel digital
[45.94 --> 51.10]  ocean later in the show but our friends at code ship released a new feature called parallel ci
[51.10 --> 56.32]  and lets you deploy your code to production 10 times faster than you've been able to do before
[56.32 --> 62.64]  if you want faster tests you have to run your builds in parallel with parallel ci you can now
[62.64 --> 67.80]  split up your test commands into up to 10 test pipelines this lets you run your test suite
[67.80 --> 73.70]  in parallel and drastically reduce the time it takes to run your builds they integrate with
[73.70 --> 79.84]  github and bitbucket you can deploy to cloud services like heroku aws and many more get started
[79.84 --> 86.06]  today for free or use our offer code when you upgrade to a paying plan the changelaw podcast is
[86.06 --> 92.94]  the code again the changelaw podcast that will get you 20 off any plan you choose for three months
[92.94 --> 99.54]  head to codeship.com slash the changelaw to get started and our next sponsor super awesome to have
[99.54 --> 108.20]  them come on it's a time limited deal so listen up app quality bundle it's a time limited deeply
[108.20 --> 115.36]  discounted bundle of web services for building better mobile and desktop apps this offer expires
[115.36 --> 122.86]  it ends on april 15th so there's little time to buy but not little time to use it does not expire
[122.86 --> 131.26]  but what do you get first off you're going to save 89 on a year of century run scope code climate
[131.26 --> 137.56]  circle ci and ghost inspector when combined together each of these services give you complete
[137.56 --> 143.64]  app quality coverage from mobile to web here's the best part what would normally cost you well over
[143.64 --> 149.74]  nine thousand dollars tons of money i mean tons of money for all these services together you're
[149.74 --> 157.46]  going to get all of them for 999 that's one full year of service of each of those services combined
[157.46 --> 163.00]  together that's a huge savings beyond the deeply discounted price once you purchase it like i said it
[163.00 --> 168.70]  won't expire if you're just starting out a new project that needs complete app code quality coverage
[168.70 --> 174.58]  this will pay for itself this is perfect for new projects projects that are growing up and need end
[174.58 --> 179.08]  to end quality coverage from mobile to web or for development shops taking care of their clients
[179.08 --> 185.08]  services for them there's only one single caveat to mention and that it's strictly for new accounts
[185.08 --> 190.08]  only there may be some exceptions to the rule but you'll have to check out the fine print or get in
[190.08 --> 195.98]  touch with them if you've got specific questions check out build better dot software yeah you heard
[195.98 --> 206.30]  me right build better dot software and now on to the show welcome back everyone we got zach zapala here
[206.30 --> 213.38]  with us zapala not zapala i you know zach i was practicing and it was the z in your first name that
[213.38 --> 221.02]  that just had to enunciate the z in the second name uh founder ceo of spark uh hardware cool stuff
[221.02 --> 225.32]  happening in your space jerry's on the line as well jerry what's up man excited to be here excited to get
[225.32 --> 232.60]  schooled on some hardware stuff yes or we begin i mean let's get started with i guess knowing more
[232.60 --> 237.82]  about you zach you yeah in the pre-call we talked a little bit about china the firewall and github so it
[237.82 --> 244.46]  seems like you've got some internationalization behind your belt what's up yeah yeah so um i started
[244.46 --> 251.20]  spark a couple years back uh beginning in 2012 originally we were trying to make uh like consumer
[251.20 --> 255.60]  consumer products really we're really inspired by nest and what they're doing with connected
[255.60 --> 261.82]  thermostats and now uh what is the smoke detector um and i wanted to do the same thing with lighting so
[261.82 --> 268.50]  my dad is deaf uh and i really wanted to make his lights flash when my mom uh texted him uh and so
[268.50 --> 273.06]  you know it's like he's got these hardwired systems to flash the lights when someone rings the doorbell but
[273.06 --> 278.14]  you can't integrate a cell a cell phone with something like that so i thought well what if i
[278.14 --> 283.24]  just added a figured out a way to add a wi-fi module to his lights and then i could create an api and hit
[283.24 --> 288.22]  that api from uh you know do an api integration with twilio or something so that he could get a text message
[288.22 --> 292.94]  and his lights would flash and that turned into this whole product that was called the spark socket
[292.94 --> 296.76]  and this was a consumer product that you could screw into a light bulb socket and screw a light
[296.76 --> 302.36]  bulb on the other end and it would bring it online um and i launched that on kickstarter late 2012
[302.36 --> 309.52]  uh with an unsuccessful kickstarter campaign so we were asking for 250 grand we raised 125 grand
[309.52 --> 316.62]  kickstarter's all or nothing so uh we got nothing but uh we had been invited to join an incubator program
[316.62 --> 322.26]  in china and so we said well whatever we're going to go to china we'll figure it out so uh early 2013
[322.26 --> 328.50]  flew to china with a couple other guys who joined the team since then and and uh um that's when we
[328.50 --> 333.92]  started we sort of over the course of a few months in in shenzhen uh decided what was interesting about
[333.92 --> 337.48]  what we're doing was a lot broader than just lighting and what if rather than trying to build
[337.48 --> 343.44]  our own consumer products we took the tech that we'd built to make our product work and and provide it
[343.44 --> 348.84]  as a platform both on the hardware and the software side um and so we relaunched a kickstarter campaign
[348.84 --> 355.74]  a few months later for the spark core which was the our first wi-fi development kit um open source
[355.74 --> 360.80]  hardware development kit cloud back end open source as well um and that kickstarter campaign was very
[360.80 --> 366.46]  successful so that's kind of what put down put us down the path that we're on now interesting and um
[366.46 --> 371.78]  one thing we gotta say before we get started here is a shout out to member and listener chris
[371.78 --> 378.18]  b champ who has been encouraging us to do more hardware shows in fact uh he gave us a long list
[378.18 --> 383.16]  of ideas i actually found you guys i'm not sure how i found you zach but i found spark maybe it was on
[383.16 --> 387.28]  your kickstarter i don't know and i asked chris i'm like is this interesting to you and he said yeah
[387.28 --> 391.72]  absolutely so uh thanks thanks to chris for doing that we actually have a question from him which we'll
[391.72 --> 398.00]  ask a little bit later but on your home page it says spark is a complete open source full stack
[398.00 --> 405.56]  solution for cloud connected devices as a software guy that sounds a bit vague uh as we get into what
[405.56 --> 409.82]  you guys offer it looks like you have the photon you have the electron what's your guys's core
[409.82 --> 416.60]  offerings yeah so it's it's it's hard to describe honestly because we like the the most important
[416.60 --> 421.32]  thing is for us is full stack so like we basically want to provide all of the tools that somebody needs
[421.32 --> 426.16]  to create a connected hardware product uh and this is if you're a hobbyist and you're building something
[426.16 --> 429.50]  on a weekend or if you're actually a manufacturer and you want to build something in production
[429.50 --> 434.88]  um but if you think about what you need so let's say you are a coffee maker company and you want to
[434.88 --> 439.44]  make a connected coffee maker well so you probably already know how to make coffee makers so you've got
[439.44 --> 446.02]  that covered um and you got to get online so you got to add something some hardware bit that's going
[446.02 --> 450.66]  to bring it online so wi-fi module or a cellular module or something like that so we make those
[450.66 --> 458.58]  and provide development kits for easy prototyping arduino like uh development tools um but with a
[458.58 --> 465.52]  focus on connectivity and then you need the the hardware to talk to something um hardware these
[465.52 --> 471.54]  products are they're embedded they have you know ram that's measured in kilobytes there's no operating
[471.54 --> 477.32]  system so it's not like you can just run uh oftentimes sort of uh you know javascript or something on
[477.32 --> 483.28]  there you have to run c and c plus plus and you still want to have something abstracted something
[483.28 --> 487.64]  easier to work with than just writing this like super low level code so we provide some firmware
[487.64 --> 494.36]  libraries uh a protocol to communicate to a cloud service the protocol is very efficient we're trying
[494.36 --> 499.86]  to do encryption in a very small memory overhead uh and then it hooks up to the cloud and the cloud
[499.86 --> 505.58]  uh quote unquote cloud right everything's cloud uh is um when you say the cloud you just mean the
[505.58 --> 510.22]  internet or well we have a we have our own hosted messaging service you have your own services that
[510.22 --> 514.36]  are cloud okay yeah exactly and the way to like i think the best way to think about it is we try to
[514.36 --> 520.64]  make hardware look like software so you can make a rest api call and like you know tell a device you can
[520.64 --> 528.82]  like post to a device's url slash brew and it'll actually call the brew function in the firmware of the
[528.82 --> 534.38]  of the coffee maker so we've tried to abstract all of the connectivity in the middle and in order to do
[534.38 --> 538.94]  that where we have a hosted cloud service that provides the api endpoint and then the device
[538.94 --> 543.84]  hooks up to that same cloud service kind of on the other end on the on the on the back side where
[543.84 --> 550.58]  um you might usually expect a database um instead you have hardware uh so that's kind of how it uh how
[550.58 --> 556.34]  the platform looks and so we call it full stack because it's um it's web we have you know front-end
[556.34 --> 562.14]  tools javascript libraries um but then it's also firmware and hardware and everything in between
[562.14 --> 568.84]  interesting i think one way that uh helps people kind of understand is to say what can i possibly
[568.84 --> 574.68]  do with this you know wi-fi development kit and honestly i was i wasn't sure until you sent me
[574.68 --> 582.26]  uh to spark.hackster.io which is kind of a community site where people have built uh things on top of your
[582.26 --> 587.98]  guys's technologies and i'm just going to go ahead and read a few of these there's just some hilariously
[587.98 --> 594.68]  cool stuff here um for instance the war kitty war kitty oh that's one of the best which the
[594.68 --> 600.10]  description there is using the spark core gps and an sd card to turn your cat or dog into a wi-fi
[600.10 --> 607.52]  scanning platform yeah so it's like going out there looking for wi-fi hot spots with your cat marty
[607.52 --> 612.78]  mcsleeves is another one which is a jacket with back to the future style variable length sleeves
[612.78 --> 618.94]  um there's a product called the foobar which is a spark powered automated cocktail dispenser
[618.94 --> 625.16]  yeah and one last one the biff shocker which is a delorean security system to prevent
[625.16 --> 631.50]  uninvited drivers it appears that it like wraps around your steering wheel and i don't know if it
[631.50 --> 638.42]  shocks people or there's some like seriously cool stuff and you just kind of like provide what what it
[638.42 --> 644.58]  seems like you guys are providing which is a higher level of abstraction on top of you know cool uh
[644.58 --> 650.78]  connected devices yeah well you know hardware is hard and and um it doesn't have to be it's it's that
[650.78 --> 655.82]  when you're working in that sort of embedded environment and with with so many constraints
[655.82 --> 660.98]  um usually what you're dealing with is like you know you're you're you're poking your registers um
[660.98 --> 665.96]  and that makes it really hard to uh there's so many layers you have to put in place to solve
[665.96 --> 671.08]  problems and i think in the web world we're we're using all used to all these layers being handed to
[671.08 --> 676.42]  us these you know trusted layers of abstraction you get things like you know rails is like very
[676.42 --> 682.42]  complete framework uh for solving web problems you don't have to deal with like tcp sockets but
[682.42 --> 686.38]  usually when you're when you're building hardware you're starting all the way down at the bottom
[686.38 --> 690.96]  that means that it can take months to even get a functional prototype so that's something we really
[690.96 --> 697.56]  wanted to try and solve is let's what can we do to make it as easy to build a connected hardware thing
[697.56 --> 703.38]  as it is to deploy a rail site um and that's where you know all the stuff we had to build comes into
[703.38 --> 710.06]  place well you started at wi-fi and i believe was that your first kickstarter was the for the photon
[710.06 --> 714.62]  actually for the spark core which is sort of the predecessor to the photon so we launched the spark
[714.62 --> 720.64]  core in may 2013 uh we've sold something like 50 000 of those so far uh the photon is its sequel
[720.64 --> 728.44]  and that'll be shipping uh next month very similar just you know next generation so cheaper faster
[728.44 --> 733.60]  better kind of everything everything all rolled into one um and then we just recently launched the
[733.60 --> 738.80]  electron which is our cellular development platform which is interesting because for the electron you did
[738.80 --> 744.80]  another kickstarter this one a massive success i believe it closes by the time the show airs it will
[744.80 --> 753.04]  have closed um but over 500 000 yeah pledging only a 30 000 goal on that one so did you
[753.04 --> 758.70]  were you once bitten twice shy or what was the deal with your goal there well you know for the the
[758.70 --> 762.44]  spark core kickstarter campaign was a ten thousand dollar goal so we tripled the goal actually
[762.44 --> 767.48]  okay last time we raised up more than a half a million last time too i mean for us you know we're
[767.48 --> 772.62]  to be honest we're going to do this stuff anyway um yeah we now we've built a community we've got
[772.62 --> 777.12]  lots of people building all our tools we know that we know that people wanted this you know
[777.12 --> 781.00]  cellular is interesting because it's a whole other set of products like uh stuff that's built with
[781.00 --> 786.76]  wi-fi it tends to be smart home products right so you're thinking about connecting appliances or you
[786.76 --> 792.90]  know your aquarium or um toys or or stuff with pets but when you get into cellular it's a totally it's
[792.90 --> 798.92]  industrial you know you're you're you've got people who want to connect uh sensors on farms and
[798.92 --> 805.28]  heavy heavy equipment and so it's a totally different area um and we had a lot of pull so
[805.28 --> 809.20]  we knew people wanted it so we said well let's just set a low goal because we know we know we know we're
[809.20 --> 814.06]  going to make this thing yeah there's some space happening in the um on the on the outside thing
[814.06 --> 819.42]  you think of a company i know called sky catch that does drone stuff and they're doing you know
[819.42 --> 824.46]  drones and you know they're flying around these drones actually have sensors on them or they're talking
[824.46 --> 829.04]  a sensors on the ground pulling back data and sort of pulling that back to a you know a main
[829.04 --> 834.30]  repository of data and collecting big data for farming and for industrial camps and just all sorts
[834.30 --> 840.12]  of crazy stuff does this potentially tie into those types of uh i guess other hardware yeah absolutely
[840.12 --> 845.00]  i mean i think that like the internet of things is a big buzzword um and i think there's a lot of
[845.00 --> 850.38]  questions uh in people's minds is like well what is what exactly does that mean right do i really need
[850.38 --> 855.26]  does this does is the internet of things about my fitbit talking to my microwave like yeah you know
[855.26 --> 860.28]  that's that it's all that stuff sounds gimmicky but a lot of the um i think a lot of the applications
[860.28 --> 865.98]  we see this very common thread that it's about closing a feedback loop um so like a good example is
[865.98 --> 872.02]  uh you know you're let's say you're farming or you've or even gardening right um and you have uh
[872.02 --> 877.50]  so you have an input which is how moist is the soil and you have an output which is like running a
[877.50 --> 882.98]  sprinkler and these two things like you know they're next to each other uh like maybe you can
[882.98 --> 887.32]  have some sort of closed loop that can um automate that but what if you have a big farm and you and
[887.32 --> 891.46]  everything's sort of further away and you don't necessarily want to like run a bunch of wires
[891.46 --> 896.04]  underground so you need everything to be wireless well these tools make it possible to close that
[896.04 --> 901.26]  feedback loop so that your input can drive your output and uh like i think comfort in your home is
[901.26 --> 906.46]  another example of well you've got let's say you have a nest thermostat and that's that's trying to
[906.46 --> 910.92]  get the temperature right in your home make you comfortable save you energy and you also might
[910.92 --> 916.58]  have ceiling fans and they also have a role to play in in in that and separately you might have
[916.58 --> 920.66]  sensors for well what's the temperature and what's it obviously the the thermostat knows what the
[920.66 --> 926.64]  temperature is at the thermostat but what about in 30 other places in your home and what if you could
[926.64 --> 931.38]  also have moisture or motion sensors all over your home that could detect whether you're there or not
[931.38 --> 936.02]  um so you can sort of take all that pool of knowledge that all these sensors are collecting
[936.02 --> 943.64]  and and use that to drive uh the um you know your radiator or uh hvac system whatever it might be
[943.64 --> 947.78]  and those are much more efficient system could be built around that kind of knowledge yeah exactly but
[947.78 --> 951.52]  a lot of times the people who are building all these products are different so like what you're
[951.52 --> 955.22]  trying to do is pull all these things to get all these things together to close these feedback loops
[955.22 --> 961.52]  yeah let me just hover on kickstarter for a second because it seems like there's a there's a trend
[961.52 --> 966.08]  recently i think gears would be an interesting perspective to get on it um and some criticism
[966.08 --> 972.72]  that kickstarter has come under as as kind of turning into pre-order starter um where it's not let's
[972.72 --> 979.08]  start this new thing that may or may not even be successful i think pebble is a interesting other
[979.08 --> 984.14]  example of course where we have a huge you know uh surplus of money according to the goal
[984.14 --> 989.32]  um what's your take on that do you think that's fair and if so do you think that's a bad thing for
[989.32 --> 995.08]  kickstarter kind of this change of pace um or a good thing i mean it's i think that it is fair to
[995.08 --> 999.24]  some extent you know we're we're a very different company now than we were when we first went on
[999.24 --> 1004.24]  kickstarter for the first time like we um at that point we didn't know what we were going to become
[1004.24 --> 1011.20]  now we're we're a um you know we're going concern right we we exist um and so our our interaction
[1011.20 --> 1016.10]  with kickstarter and with backers is very different but i think that um it's still what's what's great
[1016.10 --> 1020.54]  is that it still provides an opportunity for people for people to do things a little differently so
[1020.54 --> 1025.68]  pebble is obviously like i mean they were going to make that watch um the the the time and they
[1025.68 --> 1031.24]  raised 20 million dollars i mean it's it's crazy um but that if they didn't have that platform
[1031.24 --> 1039.72]  they'd be falling way behind uh apple and uh and you know uh android wear so it gives it gives a
[1039.72 --> 1044.28]  company like them the ability to actually compete with these behemoths that they're that they're going
[1044.28 --> 1049.02]  up against and and for us the story with the electron is kind of interesting because you know like i said
[1049.02 --> 1052.60]  we knew we were going to make this thing um and when we went into the kickstarter campaign
[1052.60 --> 1060.36]  we've we've been we've spent like close to a year probably trying to negotiate uh telco deals uh to be
[1060.36 --> 1066.92]  able to provide the back end the sim cards and the data platform for our cellular product and this is i mean
[1066.92 --> 1073.46]  you could imagine what it's like to negotiate with with carriers it's not it's uh it's long and and uh
[1073.46 --> 1077.18]  opaque and you've no idea what's going on you don't know who the right people are to talk to but so we
[1077.18 --> 1081.62]  talked to a couple carriers and sort of ongoing relationships and we found a deal that we were
[1081.62 --> 1088.16]  excited about that that gave us just u.s and u.s canada um to start off with and then when the
[1088.16 --> 1092.78]  kickstarter campaign went live we knew this was going to happen is that it was very visible and all of a
[1092.78 --> 1099.02]  sudden every major carrier emailed us within the first month of the of the campaign and we were
[1099.02 --> 1104.18]  very public about this on the campaign that like well we have a deal um in front of us but you know
[1104.18 --> 1110.60]  part of why we were going on kickstarter was to create this visible platform to tell carriers hey this
[1110.60 --> 1115.84]  is important pay attention to us and it worked and all these carriers came to us and we were able to
[1115.84 --> 1124.14]  uh work out a deal with uh telephonica where we're building with them uh global mbno uh which is a
[1124.14 --> 1130.66]  sort of a virtual carrier that covers 100 countries um and that was only possible because we went on
[1130.66 --> 1135.22]  kickstarter i don't think we ever would have been able to do that if it weren't um if it weren't for
[1135.22 --> 1141.38]  the visibility that we got during the campaign so you know it's it's it's definitely it's different
[1141.38 --> 1146.16]  second second third time around but i think kickstarter is totally game changing um regardless
[1146.16 --> 1152.16]  of what your status is going into it on that note you said this is your second successful kickstarter
[1152.16 --> 1157.58]  and jared you know kind of teach you about having a 30 000 goal but going to half a million in actual
[1157.58 --> 1164.32]  i don't know funding starting i don't know what you call that yeah pledges yeah pledges um you know so i
[1164.32 --> 1170.66]  guess for someone who's done it successfully do you go back because that's a good place to go or
[1170.66 --> 1175.46]  you don't mind giving them the 25 or 30 percent that it is or what's the percentage like 10 percent
[1175.46 --> 1179.16]  no it's actually less it's just five percent five percent yeah so you don't mind giving it a five
[1179.16 --> 1184.34]  percent to go back to the kickstarter model and reuse that platform right i mean they're um the
[1184.34 --> 1192.52]  kickstarter they're the people who are on kickstarter are a unique set get it they're really engaged uh
[1192.52 --> 1197.24]  they're the best customers you could have uh because they they're really really engaged they really
[1197.24 --> 1200.48]  want you to be successful they invest in you especially as an open source project they're
[1200.48 --> 1206.56]  people who um want to participate and want to be involved and want to provide feedback and uh you
[1206.56 --> 1211.04]  know if you treat them poorly um they're an angry mob uh because they're so engaged right if you don't
[1211.04 --> 1216.24]  give them an outlet for that uh and you're just silent and you know they'll come after you um but
[1216.24 --> 1222.38]  if you're good at managing them then uh it's an amazing set of customers to have and so that's that's
[1222.38 --> 1226.40]  really powerful kickstarter like the people who work at kickstarter we've gotten to know their team well
[1226.40 --> 1232.28]  they're awesome um they really just want to help people do new things and they're really really
[1232.28 --> 1236.90]  excited when people are trying to you know do something different um they love open source stuff
[1236.90 --> 1241.80]  uh anything open source they they just get way behind because they see it as you know their mission is to
[1241.80 --> 1247.34]  um is to empower people to do new things and and that's all that's what open source is about right so
[1247.34 --> 1252.84]  um yeah i think everything about the experience is just it's phenomenal for us like we we just love
[1252.84 --> 1259.72]  uh uh working with them well uh now that we're on the note of open source let's take a quick break
[1259.72 --> 1264.26]  we got to hear a word from an awesome sponsor that makes you so possible but when we come back we're
[1264.26 --> 1270.70]  going to talk about open source so give us a second we'll be right back i want to share a more personal
[1270.70 --> 1276.18]  note today with you about our awesome sponsor top towel you've heard us talk about top towel several
[1276.18 --> 1281.04]  times for long-time listeners you know that top towel has been supporting the show for the better part
[1281.04 --> 1285.24]  of a year to a year and a half now uh if you want to go to their website while i'm talking here it's
[1285.24 --> 1292.22]  top tal.com it's one of the best places to work as a freelance software developer uh we've been
[1292.22 --> 1296.56]  working with top towel like i said for about a year year and a half now and over this year and a half
[1296.56 --> 1302.32]  i've gotten to know their co-founder brendan very very well i love what they're doing for the
[1302.32 --> 1307.18]  software development community they care deeply about software developers having awesome engagements to
[1307.18 --> 1311.08]  work on and they also care about awesome engagements having really awesome software
[1311.08 --> 1316.40]  engineers to work with them so they really make the marriage between a business with great opportunities
[1316.40 --> 1323.02]  and an engineer needing great opportunities to work on they make that marriage possible well we took
[1323.02 --> 1327.60]  our relationship to the next level and went there ourselves we're building something very cool behind
[1327.60 --> 1331.82]  the scenes here to change law to power the future of what we're becoming you're gonna love what we're
[1331.82 --> 1337.38]  doing we hired a software engineer through top towel his name's jaffael so if you're a member and
[1337.38 --> 1342.48]  you're in the members of the slack room say hi to jaffael he's in there but i wanted to tell you just how
[1342.48 --> 1347.62]  deeply we care about our relationship with top towel and how much we trust who they are and if you're
[1347.62 --> 1352.44]  freelancing right now as a software developer and you're looking for a way to work with top clients
[1352.44 --> 1358.36]  maybe even us on projects that are interesting to you challenging and using the technologies you want to
[1358.36 --> 1366.64]  use i will go as far to say that top towel is the place for you head to top tal.com slash developers
[1366.64 --> 1371.28]  that's top towel.com slash developers learn more and tell them the change law sent you
[1371.28 --> 1379.54]  all right zach we're back uh let's talk about open source i know we got several several open topics
[1379.54 --> 1383.66]  that we can sort of go down when it comes to open source but i guess the first question would be
[1383.66 --> 1389.60]  i guess why open source which you kind of teased on but in what way are you engaging open source yeah
[1389.60 --> 1395.12]  yeah it's a good question so you know open source for us is um like we're you know we're building a
[1395.12 --> 1401.82]  business we hope to build a viable business and and and you know profit as a company and and so
[1401.82 --> 1406.34]  you know building open source businesses is challenging because in a lot of ways you're giving
[1406.34 --> 1410.76]  away a lot of what you do um so the question is well how do you how do you build a viable business
[1410.76 --> 1416.30]  that way and for us the reason that we're open source is because um what we're trying to do is
[1416.30 --> 1420.98]  build a platform for other people to to build products uh on top of it i think a lot of those
[1420.98 --> 1428.72]  customers those people are very wary of platforms like us because um they're worried that uh we are
[1428.72 --> 1436.50]  trying to take all the value that that the products might generate right that like you know if if you
[1436.50 --> 1440.72]  have someone who makes hardware and they sort of feel like commoditized right like they're just one
[1440.72 --> 1444.32]  thing of many on the shelf and they're trying to escape that by building connected products
[1444.32 --> 1448.90]  that if we come in and we say well we're you know keeping all the data like everything you learn is
[1448.90 --> 1453.52]  is is ours and all the money that you make is coming to us then i think people are worried about that
[1453.52 --> 1458.74]  um they're worried about uh you know an itunes kind of thing where like you know apple sort of
[1458.74 --> 1463.12]  like collects a lot of the value that used to be distributed to other companies in the music
[1463.12 --> 1467.78]  industry um and they're and they're very cautious of that for us open source is a way for us to say
[1467.78 --> 1472.68]  look we're really not here to screw you over like we're actually just right we're just trying to help
[1472.68 --> 1476.76]  um and provide an infrastructure uh provide a valuable infrastructure and you know we hope to
[1476.76 --> 1481.16]  be paid for the work that we do um it's a good value statement there we're not trying to screw you
[1481.16 --> 1486.16]  over right yeah exactly and and the way that we that we you know that we prove that is by saying it's
[1486.16 --> 1490.98]  open source and basically we say well look there's you know some of our a lot of what we do is open
[1490.98 --> 1496.22]  source our hardware is open source our firmware is open source the the basic functionality of the cloud
[1496.22 --> 1502.92]  platform is open source our sdks and our ide and everything they're all open source and there are
[1502.92 --> 1507.22]  parts of our platform that are closed source that are proprietary um higher level parts sort of like
[1507.22 --> 1512.90]  you know github versus git uh like the the tools that you use to oversee and manage your connected
[1512.90 --> 1517.64]  products those are those are those tools are proprietary and our thought is well you know if we're if
[1517.64 --> 1522.16]  we're doing a good job with those tools then you'll stick around you'll pay us money and and uh for the
[1522.16 --> 1527.62]  services that we're providing and we'll build a viable business and if not um then you can take
[1527.62 --> 1533.70]  our open source stuff and and go you can leave at any time um and that means that we're only we're
[1533.70 --> 1537.84]  only there if we're if we're valuable we're not we don't create any lock-in we're not you know we
[1537.84 --> 1542.54]  don't force you to stick around if we're not providing value in the long term so it's for us it's a
[1542.54 --> 1547.28]  way to keep ourselves on our toes it's a way to mitigate risk for our customers startup risk too like
[1547.28 --> 1553.54]  you know what happens if we exit uh we get acquired or we go out of business or startup so um you know
[1553.54 --> 1559.50]  being open source uh i think helps solve a lot of those problems and and so yeah it's it's you know
[1559.50 --> 1565.76]  it's very important to us um open source hardware is is relatively young compared to software it's
[1565.76 --> 1572.54]  still something that's being figured out on that hardware front um when you share the hardware piece
[1572.54 --> 1577.06]  of open source what is that like like when you build a software program it makes sense that you
[1577.06 --> 1583.72]  see javascript or eagle language you know or eagle man yeah my eagle question what's eagle
[1583.72 --> 1590.70]  you guys on spark cores let me just set that up a little bit yeah on spark cores get up page you
[1590.70 --> 1598.16]  know you check out the what's on there in the repo and the language is 99.8 eagle which is the first
[1598.16 --> 1602.84]  time i've ever even heard that in the context of anything open source so with that being said go ahead
[1602.84 --> 1607.04]  so hardware and open source is really interesting it's totally different um because uh
[1607.04 --> 1613.18]  uh software the whole premise behind um the reason that you can open source software is because
[1613.18 --> 1621.30]  uh software is managed under the same ip laws as novels right copyright it's a it's copyrighted and
[1621.30 --> 1627.02]  so you can provide a license to use your copyright and that's what every open source license is um
[1627.02 --> 1635.14]  hardware is different uh hardware is not you can't copyright hardware um you can patent hardware
[1635.14 --> 1639.38]  it's it's treated under a different set of laws so it's funny because like when we say open source
[1639.38 --> 1642.98]  hardware what we're basically saying is well we make hardware designs like circuit designs
[1642.98 --> 1647.92]  um and we give them away and we allow people to use them however they want the funny thing about
[1647.92 --> 1652.90]  hardware is that's true so long as you don't patent it that's always true like if i give you a circuit
[1652.90 --> 1656.88]  board and you take an x-ray and you look at it and you reverse engineer it and like build the same
[1656.88 --> 1662.90]  circuit like that's that's legal so uh for us it's you know it's almost more of a statement than
[1662.90 --> 1668.52]  anything else it's like we we we really want people to feel free to use these design files
[1668.52 --> 1675.26]  um if they so if they so choose eagle is a cad software so computer aided design um so if you want
[1675.26 --> 1680.26]  to design a circuit board and uh basically like draw all the little copper traces that are going to
[1680.26 --> 1684.94]  connect this bit to that bit there's a bunch of software tools out there that you can use
[1684.94 --> 1690.22]  most of them are really expensive um you know five thousand dollars plus cad software is not cheap
[1690.22 --> 1698.12]  um and uh eagle is one where it's not open source uh but it is uh free to use um for sort of smaller
[1698.12 --> 1704.72]  projects and and uh non-commercial projects so it means that we can give people these tools and say
[1704.72 --> 1708.68]  well you can go download eagle and you have access to it you don't have to go buy a five thousand
[1708.68 --> 1715.48]  dollar program to open our design files um and eagle has become sort of the de facto standard for
[1715.48 --> 1723.10]  open source hardware so when arduino and companies like that uh deliver their hardware design files
[1723.10 --> 1728.96]  um uh on github they typically use eagle i'm just excited that i guessed it right you think i would
[1728.96 --> 1732.90]  just go google it figure it out but it didn't i was like i bet that's cad stuff and i'm just gonna
[1732.90 --> 1737.80]  that's as close as i got to figuring that out so well i'm glad it says eagle now because like when we
[1737.80 --> 1743.18]  it's funny actually the last time i checked github didn't know what eagle was and so it said uh that
[1743.18 --> 1749.88]  if you looked at my github page like like a year or two ago it said that i was a i was like a prologue
[1749.88 --> 1754.82]  developer i was like what i am not a prologue developer but it's because the i think the file
[1754.82 --> 1759.30]  type or something of the of the eagle files was like very similar to the prologue one so it just
[1759.30 --> 1764.22]  thought everything eagle was prologue so i'm glad that they've that they've uh added eagle as a language
[1764.22 --> 1769.70]  you don't want to be a prologue developer come on i mean you know if somebody asked me a prologue
[1769.70 --> 1775.24]  question i would be uh i would be lost well now you know how i feel about eagle
[1775.24 --> 1783.56]  um so spark core out there open source um it's not the only thing you have out there you guys got a
[1783.56 --> 1791.06]  lot of repos yeah um the firmware itself i assume that's firmware for the spark core yeah that's in
[1791.06 --> 1798.16]  c plus plus um and then you do kind of hop higher up pretty quickly you have a spark js maybe you can
[1798.16 --> 1803.70]  take these in order you get spark js spark cli spark dev and these are all kind of in javascripty
[1803.70 --> 1811.82]  coffee scripty languages so maybe uh maybe tell us about spark js yeah yeah so basically like we um
[1811.82 --> 1816.56]  when you build a connected product you're often building a couple things you're building the hardware
[1816.56 --> 1821.98]  um and then you're building the app to interact with the hardware and the cloud acts as a gateway in
[1821.98 --> 1828.22]  between so the app it might be a mobile app might be web app whatever whatever we started with uh
[1828.22 --> 1834.32]  javascript because you know javascript's pretty popular so uh spark js lets you write an application
[1834.32 --> 1839.76]  that interacts with your hardware either from uh on the server side uh using node or in a or in a
[1839.76 --> 1844.98]  browser uh and so it makes it easy to interact with the hardware without without getting digging in
[1844.98 --> 1850.00]  too deep also you know it's all going through this rest api so it's sort of a wrapper for the rest api
[1850.00 --> 1855.08]  to interact with the hardware and uh and then the same concepts are baked into the command line
[1855.08 --> 1860.52]  interface which is our cli so you can uh use the cli to like sort of poke at the hardware and ask it
[1860.52 --> 1868.48]  questions and and call functions um monitor monitor data um coming off of the device and and uh yeah
[1868.48 --> 1877.68]  so you have uh this js library to talk to to spark core and it says spark cloud so it seems like
[1877.68 --> 1884.48]  both interfaces what what does spark cloud add i'm assuming that's your proprietary side maybe you
[1884.48 --> 1888.94]  can talk about if that costs extra or how you do you know all that stuff but yeah spark cloud add
[1888.94 --> 1895.46]  feature-wise right so actually there isn't there's an open source uh if you uh spark server is our the
[1895.46 --> 1900.30]  open source implementation of our cloud platform but basically um there's a few things that are
[1900.30 --> 1906.58]  challenging about talking to hardware directly one is that often that the hardware is in uh it's on a
[1906.58 --> 1910.64]  local network um so let's say you have a you know the thing at home and you're at work and you want to
[1910.64 --> 1916.68]  you want to preheat your oven your connected oven right so it's on your home network so now you're
[1916.68 --> 1922.54]  talking about doing nat traversals uh dealing with firewalls right all this nasty stuff that you really
[1922.54 --> 1929.64]  don't want to deal with the device uh the hardware holds open a long connection a tcp socket to the cloud
[1929.64 --> 1933.60]  and that means that it's always available so you can communicate with it from anywhere
[1933.60 --> 1939.44]  another thing that's really hard on the hardware is authentication so like i want to basically say
[1939.44 --> 1945.66]  well i want to be able to talk to my oven i want to be able to tell my my oven to preheat but i won't
[1945.66 --> 1949.58]  don't want anyone else to be able to tell my oven to preheat because that would be a fire hazard
[1949.58 --> 1955.16]  among other things right a lot a lot of issues there um and i might not even want people on my
[1955.16 --> 1959.38]  wi-fi network right like if i tell my friends they have access to my wi-fi password should they have
[1959.38 --> 1963.60]  access to it uh what about my kids like if they have an if they download an app should should they
[1963.60 --> 1969.78]  have access to it so um we can by using the cloud as a gateway we can we can put in place authentication
[1969.78 --> 1976.02]  that you wouldn't be able to do on the hardware so we use oauth to you can log in and and have access
[1976.02 --> 1981.04]  and an access token that you can use for api calls but also you can integrate with third-party
[1981.04 --> 1986.34]  services so you could provide access to somebody else uh to an app um that could interact with
[1986.34 --> 1992.14]  your hardware thing and so like you could never do that just on the hardware that you need this
[1992.14 --> 1997.44]  you need the cloud platform to um sort of stand in the middle and so the so those are the reasons
[1997.44 --> 2003.30]  that people there's value in a cloud platform um and also like it's a lot of sense because i mean
[2003.30 --> 2009.28]  you're you you bake all that smartness into the cloud right into your cloud you know user
[2009.28 --> 2014.78]  authentication things like that and interruptibility um you know we use slack a lot so it's easy to think
[2014.78 --> 2018.50]  about integrations and stuff like that so it's easy to sort of pull in other web platforms or
[2018.50 --> 2023.92]  other web clouds yeah exactly exactly um to sort of add on without really having to do much and just
[2023.92 --> 2028.60]  provide access to this open source api like you've done right exactly exactly and and it's it's it makes
[2028.60 --> 2033.48]  it much easier to integrate with other web services and and you know also like encryption and like you
[2033.48 --> 2038.42]  have so little memory on this thing it's hard to do sort of full like you know full implementation of
[2038.42 --> 2044.52]  like web web protocols so instead we use a protocol called co-app constrained application protocol
[2044.52 --> 2050.10]  it's like a super byte efficient version of http that's designed for hardware for embedded systems
[2050.10 --> 2055.54]  and so we use that to talk to the cloud and then the cloud can do https so the stuff that's a little
[2055.54 --> 2060.96]  bit heavier um that requires more overhead you don't have to do from the hardware directly um and we can
[2060.96 --> 2067.50]  also do stuff like we you know you can send code you can send a code snippet to the cloud through the api
[2067.50 --> 2072.66]  and we have a compile service that will compile that code into a binary that can then be
[2072.66 --> 2078.14]  uh dropped over the air onto the hardware so you can reprogram your hardware wirelessly
[2078.14 --> 2085.04]  that's amazing and uh the compile service is what makes that possible so like stuff like that you
[2085.04 --> 2089.24]  couldn't do without any was that something in the middle so and then and then you know again we don't
[2089.24 --> 2094.42]  we it's open source so we're not trying to like be the ecosystem right we're trying to open it up so uh
[2095.02 --> 2100.42]  um so you can use our uh our proprietary one and then you know our platform there's some differences
[2100.42 --> 2104.94]  between ours and the open source one um ours has a bunch of scaling infrastructure in place so that
[2104.94 --> 2109.74]  we can do like really really large deployments whereas the uh the open source platform is really
[2109.74 --> 2116.12]  just a single javascript application so it can handle as you know as much traffic as as the application
[2116.12 --> 2122.78]  can as your as your system can so our so our proprietary platform scales better um but yeah that's that's uh
[2122.78 --> 2128.98]  that's pretty much what the cloud does you mentioned authorization and um getting a little timely
[2128.98 --> 2134.28]  here i'm sure you saw amazon dash button oh yeah launched today talk about the internet of things
[2134.28 --> 2139.64]  here we have a new thing from amazon which is basically a button that is locked it seems like to a
[2139.64 --> 2147.02]  specific vendor or a specific product and you stick it on some device i think their canonical example is
[2147.02 --> 2151.62]  your dishwasher or excuse me your laundry machine right and you got your tide button there basically
[2151.62 --> 2157.10]  and uh when you're getting low on tide you know instead of having to do whatever it is you
[2157.10 --> 2163.60]  previously had to do now you just hit hit your tide button and it fires off a you know a purchase
[2163.60 --> 2168.64]  order to amazon and it magically shows up at your door authorization i think is an issue with the
[2168.64 --> 2173.10]  tide button as you're you know i have four kids i don't know about you but uh that would be their
[2173.10 --> 2180.08]  favorite button in the world i'm sure but that's the kind of goes broke by buying too yeah just a huge
[2180.08 --> 2187.52]  you know a pallet shows up one day um so authorization and everything but is this the kind of thing that
[2187.52 --> 2192.48]  you could easily build on top of spark yeah absolutely and and it's actually a great example
[2192.48 --> 2196.84]  of closing the feedback loop right yeah and i think that when it's a button you still have a human
[2196.84 --> 2201.10]  element right and which which creates in some ways it makes it easier because you can just tap the
[2201.10 --> 2206.68]  button but it also creates problems because like your kids can tap the button um and uh whereas i think
[2206.68 --> 2213.82]  the end goal is like anything anything that has a consumable element should be able to recognize
[2213.82 --> 2220.36]  when it's running out of the consumable and reorder it right so like and that so okay like dishwashers
[2220.36 --> 2227.18]  great and laundry machines great and they you know um or what about oil for your car or anything that
[2227.18 --> 2233.32]  uses oil right or food uh you know if if and this is like the connected fridge is always just like
[2233.32 --> 2235.96]  people get really annoyed at it because they make these connected fridges
[2235.96 --> 2240.98]  and they're really just like ipads duct taped to the front of a fridge like it's not really a
[2240.98 --> 2245.98]  connected fridge right um but what if you actually did a connected fridge right which is like it had
[2245.98 --> 2250.00]  a camera in and it can sense what's in there and how long it's been in there and it could reorder
[2250.00 --> 2254.98]  stuff when like it knows that your milk's been in there for like four weeks and you yeah okay it's full
[2254.98 --> 2260.92]  but it's definitely expired so it could reorder your milk or maybe if you're not drinking your milk you
[2260.92 --> 2266.30]  should reorder milk but you know like right like it's it's always it's very often the same story of
[2266.30 --> 2270.36]  like closing the feedback loop um and consumables are a huge part of it i think what amazon's doing
[2270.36 --> 2277.70]  is really smart um and uh and actually there in addition to the button they opened up an api so that
[2277.70 --> 2282.92]  you can use their reordering system without the button so we looked at that and we're like oh we
[2282.92 --> 2286.68]  totally have to integrate that into our web service because what if our customers want to build products
[2286.68 --> 2292.20]  that can hit this api to reorder the consumable from amazon so that's like a huge we're super
[2292.20 --> 2297.50]  jazzed about that yeah instead of everybody having to do it themselves you could do it once and then
[2297.50 --> 2304.06]  your customers could all just use that exactly exactly yeah i just remember like i don't know what
[2304.06 --> 2310.90]  episode adam do we have uh chris mccord on with elixir i was just 148 yeah 148 i was just speaking
[2310.90 --> 2318.54]  skeptically of the internet of things and kind of noting how it's all very kind of novelty and and
[2318.54 --> 2326.64]  vague and not there's not like real value propositions yet um but i think it's just a matter of time i
[2326.64 --> 2330.48]  mean even just when i saw the amazon button i was just like okay that's that's actually a really good
[2330.48 --> 2336.50]  use you know right and you start to be like okay you know soon we're gonna start to see things we're
[2336.50 --> 2341.68]  like wow that that's life-changing in a very small way right and i think you're you're right on par with
[2341.68 --> 2346.34]  the closing the feedback loop and that's why things like spark are exciting because you don't have to
[2346.34 --> 2351.36]  be amazon to put something together anymore exactly you have these open source options and you have
[2351.36 --> 2359.04]  these small cheap entry ways to to building stuff which is why i think this hackster site is so cool
[2359.04 --> 2363.56]  because here you have people just basically having fun and building things that i would never imagined
[2363.56 --> 2368.52]  just because what the capabilities well and that's where i think like the hardware world still has a
[2368.52 --> 2374.20]  lot to learn from the web world where like you know here if you're if you're you know building web
[2374.20 --> 2379.60]  tools um or web software the tools that you use in a production environment are the same tools that
[2379.60 --> 2384.62]  you use as an individual like building a hobby weekend project right so like it's the same programming
[2384.62 --> 2388.88]  languages it's the same frameworks right it's not like there's some like set of tools that are hidden to
[2388.88 --> 2394.70]  you as a as an amateur and in the hardware world there's still there's still generally a pretty big
[2394.70 --> 2400.18]  gap between the professional tools and the and sort of the hobbyist tools so like you've got kind of
[2400.18 --> 2406.36]  arduino and raspberry pi um for these hobbyist projects and then professionals are using like you know
[2406.36 --> 2411.62]  like ide like keel it costs like 10 grand and and uh you know they're using a different set of
[2411.62 --> 2416.70]  microcontrollers they're purchasing components from like qualcomm and broadcom who won't sell them
[2416.70 --> 2421.40]  they will not sell you anything if you're not buying a million units right so like you don't
[2421.40 --> 2427.58]  have access to them as an individual and so there's this rift in tooling between professionals and
[2427.58 --> 2431.54]  and amateurs and that's one of the problems that we're trying to solve is say well look if we could
[2431.54 --> 2437.18]  take the best stuff that the professionals have give access to everybody then it could close the gap
[2437.18 --> 2441.70]  and the and the world would start to look a little bit more like the web where i think it's fascinating
[2441.70 --> 2447.62]  in hardware um you have the concept of a hobbyist right like what's a what about a hobbyist software
[2447.62 --> 2452.06]  developer like well you don't really have a hobbyist software developer because they're just
[2452.06 --> 2456.96]  software developers on weekends right it's the same people as the professionals and i i think that's kind
[2456.96 --> 2462.18]  of true of of the hardware world too um there's a perception that you have these two different groups
[2462.18 --> 2466.48]  hobbyists and professionals but i think that they're mostly the same people it's just whether you're
[2466.48 --> 2472.42]  talking to them on saturday or on tuesday good point let's loop back to some more open source
[2472.42 --> 2479.92]  projects you guys have here um spark dev which you term is a professional hackable ide for spark
[2479.92 --> 2487.50]  based on github's atom yeah interestingly uh facebook just released nuclide or nuclide de
[2487.50 --> 2491.96]  yeah i don't know how they pronounce that but it's a unified ide for react and react native
[2491.96 --> 2497.66]  based on github's atom and so uh seems like you guys beat him to the punch on this tell us about it
[2497.66 --> 2506.56]  yeah so like we um so when we launched the spark core uh we we had a web ide um which people could
[2506.56 --> 2509.68]  use which is great because you don't have to have a tool chain or anything installed locally you can
[2509.68 --> 2514.34]  just um like go to a website write some code hit the flash button and it reprograms it wirelessly
[2514.34 --> 2521.12]  super awesome for getting started but it's hard to build a web ide that's as sort of complete and as
[2521.12 --> 2526.16]  comprehensive as you as uh as a professional would want and so we'd been looking for a while to figure
[2526.16 --> 2530.20]  out like well we want to do something that you can download on your local machine and really have
[2530.20 --> 2534.68]  like a professional experience with and you know when people are doing embedded code usually the
[2534.68 --> 2540.78]  common tools are like the expensive proprietary ides are like eclipse and eclipse is great and you know
[2540.78 --> 2545.18]  it solves a lot of problems but it's it's cumbersome and there's a big rift but there's a big gap between
[2545.18 --> 2550.80]  eclipse i think and like you know the simpler tools and so when adam came out we thought oh this is
[2550.80 --> 2555.46]  perfect this is a great platform for us to use github is clearly investing a lot and making this
[2555.46 --> 2559.48]  thing awesome they've they've done so much development on it and it's evolved so quickly
[2559.48 --> 2567.08]  and it's also web connected so we could do stuff like hit our uh you know cloud apis um from the same
[2567.08 --> 2573.64]  ide where you can also like you know deploy firmware locally using a local tool chain so so we took adam
[2573.64 --> 2580.42]  and sort of added a couple layers of of uh specifically for our hardware to turn it into a standalone
[2580.42 --> 2586.84]  ide um which i don't know if that was what um github was intending that people would do with adam um
[2586.84 --> 2593.06]  but it's really well suited for it and uh and so yeah i think we were the i think we were the first
[2593.06 --> 2598.16]  people to do it uh and then uh when facebook i mean i was not surprised to see facebook do something
[2598.16 --> 2602.76]  like that because it's you know it felt somewhat obvious to us like somebody needs to be using somebody
[2602.76 --> 2607.08]  else needs to be using it in the same way um but yeah it's a great they've they've built a pretty
[2607.08 --> 2613.06]  great tool there i like it a lot question for me i guess on this note is when we look at adam or we
[2613.06 --> 2619.80]  look at sublime text or other text editors out there why fork adam create your own version that
[2619.80 --> 2625.36]  sort of adds you know ability specifically for your infrastructure why do that versus sort of a
[2625.36 --> 2632.34]  a plug-in or a bundle as textmate does or yeah or sublime text why go and actually create the own
[2632.34 --> 2637.34]  what what's the value add there for facebook or for you well that's a good question and here's the
[2637.34 --> 2643.62]  here's the trick really we just did create a plug-in so like actually you can just go install the spark
[2643.62 --> 2649.50]  core plug-in and add them and you end up with the same thing but for a lot of our customers like um
[2649.50 --> 2656.20]  you know we don't our customers aren't typically web folks like we have a lot i shouldn't say that
[2656.20 --> 2662.08]  there are a ton of web developers who use uh who use spark but i would say the majority of our
[2662.08 --> 2667.70]  customers are um like more of sort of embedded developers and they come from a different place
[2667.70 --> 2674.18]  and are used to a different set of tools so github is not necessarily a brand name that they recognize
[2674.18 --> 2680.82]  uh um it's just a little bit of a different world so you know for them for us to say we'll go
[2680.82 --> 2685.28]  download this adam thing and then install this it feels like wait who's whose website am i going to
[2685.28 --> 2692.22]  i don't trust these github people uh like and of course we think that's silly but whatever so we
[2692.22 --> 2696.48]  we package it up and say look here's a downloadable thing it's just an it's it's an application that you
[2696.48 --> 2702.24]  can download and double click on it'll work um but if you are uh you know if you're familiar with
[2702.24 --> 2709.04]  adam you can just install the plug-in and it'll work the same that's cool yeah i'm looking here i'm
[2709.04 --> 2713.12]  looking for the adam uh license i'm assuming it's pretty liberally licensed i think you know that
[2713.12 --> 2718.00]  that's some of the value of open sources it's okay you can take that you can put your name on it as
[2718.00 --> 2722.56]  long as it you know adheres to their license and their copyright and all that and you can make your
[2722.56 --> 2729.32]  company it bolsters your company um and to your customers who may or may not be uh interested in
[2729.32 --> 2734.28]  adam here it is it's spark dev it's all included and then you can you know you don't have to just
[2734.28 --> 2739.08]  maintain a little plug-in and fit inside of that box if you have more kind of deep ingrained things
[2739.08 --> 2743.28]  that you want to change you can go ahead and do that yeah yeah exactly and we you know we didn't
[2743.28 --> 2748.40]  uh we weren't sure because we did it pretty early in adam's life so we didn't know how github
[2748.40 --> 2752.70]  felt about we didn't know what really really they wanted to do with adam so we had a couple friends
[2752.70 --> 2758.26]  there and we're like hey so we're building this ide with adam like is that is that cool like you
[2758.26 --> 2761.84]  know i know it's open source but like we don't want to you know i don't want to piss anybody off and
[2761.84 --> 2768.20]  um they're great they loved it they're like oh yeah that's great it's awesome go for it so that's i love it
[2768.20 --> 2771.92]  i don't know if you found it jared or not but it's under the mit license and when they announced
[2771.92 --> 2777.58]  it they actually said adam free and open source for everyone so i guess the mit license does afford
[2777.58 --> 2782.04]  you the ability to fork it kind of repackage it so long as you're not doing things that are against
[2782.04 --> 2787.54]  the mit license you're good to go yeah right yeah exactly well this is probably a good place to
[2787.54 --> 2792.28]  pause and hear a word from our sponsor when we get back i want to talk to you about getting into the
[2792.28 --> 2797.56]  hardware scene as a web developer as a software developer and get some tips from you but we'll be right back
[2797.56 --> 2805.54]  sure over 400 000 developers have deployed to digital oceans cloud digital ocean is simple cloud hosting
[2805.54 --> 2811.50]  built for developers in 55 seconds you'll have full root access to a cloud server and it just doesn't get
[2811.50 --> 2816.94]  any easier than that pricing plans start out affordably at five dollars a month for half gig of ram
[2816.94 --> 2824.14]  20 gigs of ssd drive space one cpu and one terabyte of transfer all digital ocean servers run on blazing
[2824.14 --> 2831.98]  fast ssds with tier one bandwidth and come with private networking use the promo code changelog april
[2831.98 --> 2838.30]  to get a 10 hosting credit when you sign up again changelog april 10 bucks when you sign up
[2838.30 --> 2843.46]  new accounts only head to digitalocean.com to get started and now back to the show
[2843.46 --> 2851.20]  all right we're back zach i'm a web developer adam's web developer a lot of our listeners are
[2851.20 --> 2856.32]  web developers of course we do have the crispy champs in the audience who are probably sitting
[2856.32 --> 2861.36]  there wishing we're asking more hardware-y hackery questions but we just don't have that in our
[2861.36 --> 2866.66]  arsenal right now if i'm interested maybe in spark maybe just in like making my own thing
[2866.66 --> 2873.52]  what's a break-in point how do i get involved in open source hardware yeah great question so you know i
[2873.52 --> 2881.14]  think that um i think the best uh the best way to get into hardware is is by having something you
[2881.14 --> 2887.48]  want to build right like having an example a project in mind because i think you learn better um you
[2887.48 --> 2891.72]  learn a new area better if you if you if you have some intent right it's it's more important to you
[2891.72 --> 2897.22]  um so like when i started the first thing i built was uh i had a i had a little garden and i was trying
[2897.22 --> 2903.84]  to make it um use an arduino which is so an arduino is a platform very similar to ours uh um but it's
[2903.84 --> 2907.78]  just a microcontroller so it's really just the brain and not the connectivity you can get shields
[2907.78 --> 2914.86]  accessories that um bring it online um but so i got an arduino and i i built a little moisture sensor for
[2914.86 --> 2919.26]  for my little garden um and had it connected to a pump and was trying to pump the water when it got dry
[2919.26 --> 2928.16]  um actually i never got that to work but uh but you know right let's be let's be honest um but you
[2928.16 --> 2933.02]  know having some project like that and then i think that um like a lot of the concepts platforms
[2933.02 --> 2938.68]  like ours so i think spark is a great tool for web developers because um we've tried we've tried to
[2938.68 --> 2943.56]  abstract everything so you don't have to you don't have to go sort of too deep um there's definitely
[2943.56 --> 2950.20]  some level of knowledge you have to pick up along the way of circuit design but i think one of the
[2950.20 --> 2954.24]  things that's important to know and it's like you almost don't know this if nobody tells you it's
[2954.24 --> 2957.52]  really hard to hurt yourself with hardware so like i think a lot of people are a little nervous
[2957.52 --> 2961.20]  because they're going to like electrocute themselves like this stuff is all super low voltage
[2961.20 --> 2968.36]  you're unless you're plugging into the wall um uh like you are it's basically impossible to hurt
[2968.36 --> 2973.54]  yourself and the worst thing that you're going to do is uh there's a there's a term of art
[2973.54 --> 2979.00]  in the hardware world called letting out the magic smoke which basically is like you know you have a
[2979.00 --> 2985.26]  a chip that is expecting 3.3 volts and you give it 10 and you see this little like this little
[2985.26 --> 2991.00]  right and then like the this little black smoke comes out of it and you're like oh i just destroyed
[2991.00 --> 2997.90]  that but you know it's like so that you don't do that sound effect was awesome too i like that
[2997.90 --> 3004.98]  it does make that sound uh and uh it's like well that's okay as long as your hardware is cheap right
[3004.98 --> 3010.82]  like if you know the photon's 20 bucks so i would typically say especially to someone who doesn't
[3010.82 --> 3015.44]  have any hardware background buy two because you'll probably let the magic smoke out of one of them
[3015.44 --> 3023.08]  consummate salesman yeah um go for the upsell buy two yeah buy two but like you know it's cheap so it's
[3023.08 --> 3028.80]  so it so it's it's not that big of a deal and and if you put something in backwards and like you know
[3028.80 --> 3033.96]  whatever happens like it's fine you just you just buy a couple of everything um so you have extras and
[3033.96 --> 3040.32]  you have to learn some basic concepts of like you know adding resistors so that you can limit current
[3040.32 --> 3045.10]  to things as some sort of basic basic stuff like that but a lot of it's available online youtube is
[3045.10 --> 3051.08]  youtube's your friend uh there's websites spark fun and adafruit are both retailers that sell like um
[3051.08 --> 3056.92]  uh diy kind of hobbyist electronics um and they've got tons of tutorials that walk you through stuff
[3056.92 --> 3063.68]  if you google anything like sort of plus arduino you'll get like great tutorials on how to do
[3063.68 --> 3069.48]  something so if you google for instance like moisture sensor arduino you'll find an unbelievable wealth
[3069.48 --> 3075.10]  of knowledge um and our platform is arduino compatible so that all the code like basically everything
[3075.10 --> 3080.02]  that you do in arduino works exactly the same on spark um so all that stuff will work but then with
[3080.02 --> 3085.56]  our platform you can also bring it online if you want to add sort of web stuff to it so i think that
[3085.56 --> 3091.62]  the best thing to do is like you know buy a dev kit like a spark core a photon or uh if you're doing
[3091.62 --> 3097.82]  embedded stuff in arduino uh you know if you're doing stuff that you don't need to be online or or a kit
[3097.82 --> 3104.10]  where like a lot of the companies like spark fun and adafruit have these kits that have the dev board and
[3104.10 --> 3109.36]  like other stuff so like a bunch of jumper wires and a bunch of extra sensors and actuators like little
[3109.36 --> 3113.50]  motors and stuff so that you you have everything you need in the box to to get started so those are
[3113.50 --> 3118.82]  really great um spark fun has one called the spark fun inventors kit that's really what i started with
[3118.82 --> 3125.30]  it's awesome um we sell something called the spark uh the spark maker kit which is very similar uh same
[3125.30 --> 3130.58]  kinds of things but again designed for something that's connected and so that stuff is great for for
[3130.58 --> 3135.88]  getting started and then you can go buy more components online or i was about to say radio shack but
[3135.88 --> 3142.00]  actually i guess that's not true anymore yeah don't do that that face um but online you can
[3142.00 --> 3148.24]  you can still get it and yeah it's just you know find a project get started google around same learning
[3148.24 --> 3152.72]  process is learning a new programming language i think um but you know i think to anyone who's done
[3152.72 --> 3156.30]  software development a lot of this stuff it'll come naturally because it is it's most of the same
[3156.30 --> 3162.30]  concepts it's just a little bit lower level i think i'm kind of inspired by this this sparks dot
[3162.30 --> 3168.68]  hackster spark dot hackster dot io site because the stuff on here is so freaking cool like what i
[3168.68 --> 3174.04]  picture of myself getting into hardware i imagine you know the first couple of weeks or the first
[3174.04 --> 3179.66]  month it's like i get this little led light to like go back between you know yellow and red and to me
[3179.66 --> 3183.68]  like that just that like that doesn't really do it for me like i don't want to invest time and money
[3183.68 --> 3190.70]  and you know frustration into a led light going yellow and red right but if i can see some end goals
[3190.70 --> 3195.12]  like this and maybe you know maybe these are way outside my league or something but uh it seems like
[3195.12 --> 3201.26]  there's just some really cool actual useful things and some just silly like war kitty yeah um that might
[3201.26 --> 3206.10]  be within the realm of possibility nowadays for for a starter oh totally so i'll give you one actually
[3206.10 --> 3211.30]  that's a good like a really good starter project uh which is one that we did um at the end of last
[3211.30 --> 3218.10]  year so when the when the last hobbit movie came out um we uh we were inspired to create and actually
[3218.10 --> 3223.86]  this was also inspired by war kidde which is one of our favorite uh community projects so we built
[3223.86 --> 3230.08]  something called war sting and uh so i assume you guys are familiar with the hobbit and lord of the
[3230.08 --> 3236.12]  rings um of course you know uh the the sword sting that turns blue when there's orcs nearby
[3236.12 --> 3244.36]  so uh they sell you can buy on like amazon or wherever these 30 dollar like toy swords that turn blue
[3244.36 --> 3248.56]  like they've got a little blue led in them that you can flip a switch and then it makes hacking and
[3248.56 --> 3253.28]  slashing noises so we bought one of these and we opened it up and realized that the circuit's really
[3253.28 --> 3260.08]  simple and there was room for a spark core inside the hilt of the sword so we published a project so
[3260.08 --> 3266.22]  if you go to our blog which is blog.spark.io um and scroll down a bit you'll find uh instructions for
[3266.22 --> 3273.60]  building your own war sting so this is a uh hobbit sword that will turn blue near any unsecured wi-fi network
[3273.60 --> 3280.52]  and if you swing the sword it will hop on the network and publish a message that says this
[3280.52 --> 3286.40]  network has been vanquished uh and that project publish it too like well like publishes we have
[3286.40 --> 3290.96]  like an event stream that comes out of our cloud so like it's it's available globally through the cloud
[3290.96 --> 3297.74]  um as a public message but so and then you could you could very easily you could do a webhook uh we
[3297.74 --> 3302.78]  have this really simple webhook command we're using our cli so you could pipe that over to like you
[3302.78 --> 3308.42]  know someone else's api like twitter or twilio or whatever but it's like it's a cool project and
[3308.42 --> 3315.72]  it's really easy because all you do is you like literally snip a wire in the um uh in the hilt
[3315.72 --> 3320.36]  and then like solder uh you do have to use a soldering iron but it's good learning experience
[3320.36 --> 3328.18]  uh you can you solder i'm out you lost me yeah me too you solder the wire to like two of the pins on
[3328.18 --> 3333.16]  on the spark core and then you and then you copy paste the code uh and like you know put it in
[3333.16 --> 3340.50]  your the web id and and flash it over the air and now you've got this connected sword nice new new
[3340.50 --> 3347.16]  talents yeah that sounds so awesome that sounds so awesome yeah the soldering part does a little
[3347.16 --> 3353.66]  lose me because yeah i have a hard time plugging usb uh cords yeah i got these fat fingers who doesn't
[3353.66 --> 3358.12]  right try it twice i'm looking i'm we'll we'll link this up in the show notes by the way i'm looking
[3358.12 --> 3363.60]  at this blog post right now and i'm thinking my kids would think i was so cool with this thing oh
[3363.60 --> 3370.66]  yeah my wife not so much but my kids they would love it right yeah so we actually got i was we were
[3370.66 --> 3374.40]  super excited about this because we were i mean it was totally like a gag right a stunt that we were
[3374.40 --> 3380.22]  just like maybe we'll get some attention online and we posted it and no love like the first three days
[3380.22 --> 3385.38]  like you know like a thousand people saw a blog post and were like oh this sucks and then uh like a
[3385.38 --> 3390.90]  week later it got put up on reddit and it got up to number 26 on reddit which is the one away from
[3390.90 --> 3396.20]  the front page so i'm like so close but now i think the youtube videos got like uh something like 300 000
[3396.20 --> 3402.00]  views so a lot a lot of people have have checked out are very ridiculous also the youtube video is like
[3402.00 --> 3405.68]  silly one of the guys on the team is dressed up like gandalf and another one's dressed up like
[3405.68 --> 3413.10]  frodo it's it's or bilbo i guess um so it's silly but it's fun well let's switch gears here and let's
[3413.10 --> 3419.46]  ask a question from chris himself the requester of the show and the hard work guy chris b champ
[3419.46 --> 3424.94]  who told me that uh what an interesting conversation would be and this will probably be a one-sided
[3424.94 --> 3428.90]  conversation because i'm not i got i got nothing to bring to it but i'm gonna ask it and you can speak
[3428.90 --> 3434.56]  to it all right all right he says what would be interesting is the process that they meaning you
[3434.56 --> 3440.90]  guys and other board makers follow to get their boards manufactured and to market he says something
[3440.90 --> 3445.32]  tells me that they're not fulfilling orders by soldering surface mounts all day in their garage
[3445.32 --> 3453.98]  can you speak to that so we did start in a garage like making them by hand uh i made i'm very proud
[3453.98 --> 3459.24]  because when we did our first so so basically yeah i'll go i'll go through the process so um
[3459.24 --> 3464.92]  uh circuit boards are in some ways it's you know it's a little challenging to figure out how they're
[3464.92 --> 3469.02]  made but it's there there's a million places that do it right it's it's there's a lot of expertise out
[3469.02 --> 3473.78]  there so um in a lot of ways you're just kind of finding a factory and letting them solve a lot of
[3473.78 --> 3481.00]  the problems um but basically the way that it works is um when you design a board that you're going to use
[3481.00 --> 3487.66]  in a mass manufactured product um you use eagle to design the board and sort of find all the
[3487.66 --> 3491.72]  components that you need the sensors and the you know the microcontroller everything like that
[3491.72 --> 3495.56]  you lay them out on the board and the layout on the board is like you know it's an optimization
[3495.56 --> 3501.48]  problem it's like what's the smallest surface area that i can get all of these things on and also draw
[3501.48 --> 3506.66]  little copper lines between each of them and not have any of the copper lines cross so it's you know
[3506.66 --> 3513.00]  it's just a good old-fashioned engineering problem so you lay out the board you usually go it takes a
[3513.00 --> 3519.40]  couple iterations to to get something that that you like and then you send them to uh pcb uh pcb
[3519.40 --> 3523.26]  manufacturers uh printed circuit board manufacturers so these are the guys who actually give you the
[3523.26 --> 3529.30]  circuit board and in the u.s this costs it can cost a lot of money um the best for prototyping there's
[3529.30 --> 3536.16]  a company called osh park osh open source hardware uh osh park.com uh i think is their i think is
[3536.16 --> 3540.22]  their website and they make these purple boards that have become very well known uh you see a
[3540.22 --> 3545.02]  purple board you know exactly where it came from um but you can send them a a design file and you
[3545.02 --> 3549.92]  export from eagle and something called a gerber file so a gerber file is like the output that all of
[3549.92 --> 3558.50]  these pcb manufacturers know how to speak um uh so you send them a gerber file and then depending on
[3558.50 --> 3564.30]  how much money you pay and who you use like sometime between two days and three weeks later a circuit board
[3564.30 --> 3570.20]  arrives and now so you buy the components you go somewhere like digi key is a is a is a common one
[3570.20 --> 3575.84]  uh or mauser there's companies that sell all these components um and then if you're overseas you use
[3575.84 --> 3580.98]  someone else and they'll send you the components uh you take solder paste so in low volume what you do
[3580.98 --> 3589.72]  is you take solder paste which is like a a liquid form of um solder and you you put little drops of it
[3589.72 --> 3594.90]  on all of the pads on your board and then you take a pair of tweezers and you put all the components
[3594.90 --> 3599.98]  on the pads and you put it in a in an oven and there's particular ovens that you use for this
[3599.98 --> 3606.84]  that are called reflow ovens um that are designed to make the solder paste flow but uh uh actually you
[3606.84 --> 3611.86]  can use like there's tons of stuff online about how you can use a convection like a little toaster oven
[3611.86 --> 3617.40]  or a or a little frying pan um to do this so that you can do it with anything you don't need it you
[3617.40 --> 3621.86]  don't need fancy equipment and then that's so that's like how you design it in low volume when
[3621.86 --> 3626.56]  you go high volume you go to a manufacturer so you find some manufacturing partner the places that do
[3626.56 --> 3633.30]  this are called pcba so uh printed circuit board assembly um and typically they will then order the
[3633.30 --> 3637.74]  circuit boards for you and they'll order the components for you so they build they get all the
[3637.74 --> 3643.08]  inventory and then they have machines um that are called pick and place machines that are basically
[3643.08 --> 3649.42]  like you know us using tweezers except on steroids so they have these little like arms robotic arms
[3649.42 --> 3655.06]  that will like you know take these little tiny components like less than a millimeter squared and
[3655.06 --> 3660.40]  pick it up with a little vacuum and drop it on the thing they can do thousands of components per minute
[3660.40 --> 3666.84]  super fast like unbelievably fast and then it'll be this like sort of uh conveyor belt that brings
[3666.84 --> 3671.74]  something down through the oven or sort of through the pick and place machine and then into the oven and
[3671.74 --> 3678.02]  it comes out baked and and ready um and then you and then you program them so you'll have like a
[3678.02 --> 3683.42]  programmer which is usually just like a pc with like a port that you can hook up to this thing and
[3683.42 --> 3690.66]  program the the board like the microcontroller um with your software and then and usually these will
[3690.66 --> 3694.92]  be done in panels so you'd have like 10 boards on a panel and so somebody will snap all of them off
[3694.92 --> 3700.42]  and then put it in a box or a bag or whatever and that's then that's the the process so you know to go
[3700.42 --> 3705.60]  through all this and figure it out like a lot of it is finding the right partner and uh you know
[3705.60 --> 3709.72]  finding a manufacturing partner who's like willing to work with a startup getting them on board going
[3709.72 --> 3713.88]  through these iterations with them there's a lot of work that's called dfm which is designed for
[3713.88 --> 3718.84]  manufacturer so like optimizing things so that they're more manufacturable and a lot of times that's
[3718.84 --> 3723.00]  like make sure to label which direction the led is supposed to be pointing so that somebody doesn't
[3723.00 --> 3727.94]  actually put accidentally put it on backwards or or like make these two components for their part so
[3727.94 --> 3733.56]  they don't accidentally like bump into each other so it's you know it's in comparison to software
[3733.56 --> 3737.68]  development i think one of the things that makes running a hardware startup hard is that
[3737.68 --> 3743.92]  you can't just do like you know it can't be two guys in a garage can't build a billion dollar business
[3743.92 --> 3748.14]  um in the same way that you can with software like you have to partner with other people
[3748.14 --> 3754.70]  um you it's it's messy it's dirty you know it's not like like software you write the right software it
[3754.70 --> 3760.74]  works uh like manufacturing even if you design the circuit board right you still have yield like
[3760.74 --> 3765.80]  one percent of your boards aren't going to work for some reason that has to do with the physical world
[3765.80 --> 3771.00]  and all of its imperfections um and so you have to test everything because you have to throw that one
[3771.00 --> 3776.60]  percent away you don't want to ship that to a customer so it's way messier than software um but in
[3776.60 --> 3780.84]  the end like you know it's engineering a lot of the same concepts apply and and it's hard but it's
[3780.84 --> 3787.46]  rewarding and the fact that it's hard means that fewer people are doing it so it's not like
[3787.46 --> 3793.04]  software development where like if you're making a mobile app there's probably 20 other people making
[3793.04 --> 3797.30]  the same mobile app that are that you're going to be competing with hardware like you do something
[3797.30 --> 3802.98]  cool probably nobody else is doing it and and gadget will probably write about it because
[3802.98 --> 3808.80]  you know there's just not that many things they need more and more content on that side for sure
[3808.80 --> 3812.96]  yeah there's because there's just not it's a smaller market right yeah exactly let's be willing
[3812.96 --> 3816.84]  to do that right it's messy and that's a nice barrier around your business you know you figure
[3816.84 --> 3821.98]  it out and you figure out how to make something and then you know that like it's not like somebody
[3821.98 --> 3826.28]  can just come rip you off because it's actually pretty hard to do this stuff well one way to be
[3826.28 --> 3831.32]  successful is to do something that no one else is willing to do right right yeah that's how you get
[3831.32 --> 3837.58]  there yeah as if uh if i'm willing to do it and you're not guess what i win right that's how
[3837.58 --> 3844.42]  you're winning exactly that was a nice crash course into the hardware side of this i mean that i mean
[3844.42 --> 3851.04]  it seems like we could probably have an entire other show on just that with you uh schooling us
[3851.04 --> 3856.64]  on all facets of of the the hardware side of it because like you said there's a huge barrier there
[3856.64 --> 3862.14]  because no one's really willing to do that hard work yeah not saying no one but it's less enticing
[3862.14 --> 3867.02]  right so so it's easy to there's a lot more there's a lot more moving parts a lot more fail
[3867.02 --> 3871.60]  and even costs right now so we actually just recently launched a blog because we're trying to
[3871.60 --> 3876.70]  explain all this stuff so that more people can do it um and so we launched a blog a couple weeks ago
[3876.70 --> 3885.84]  it's called uh prototype to production so the website is proto to prod uh p-r-o-t-o-2-p-r-o-d.com
[3885.84 --> 3894.38]  um number two or spelled out number two yeah so uh and the goal with proto to prod is um like to
[3894.38 --> 3898.86]  answer all these questions and and to show people the path that they can follow and teach each of
[3898.86 --> 3905.92]  these steps like uh our supply chain our head of supply chain will wrote a blog post on uh like
[3905.92 --> 3910.52]  selecting your bill of materials and like finding all these components and it's this it's a massive blog
[3910.52 --> 3915.76]  post but he's an incredible writer um and so it's i think actually pretty easy to follow like you can
[3915.76 --> 3920.18]  read it and you you come out of it and you're like oh i get that now like that sounds like totally
[3920.18 --> 3926.92]  crazy and like you know like so far from anything you've done before and you read the blog post and
[3926.92 --> 3933.02]  you're like oh this makes sense um so um we're trying to we've we've got a couple posts up now
[3933.02 --> 3936.44]  but over the next couple months we're trying to tell that whole story of like literally
[3936.44 --> 3941.78]  you know from from a single prototype to making 100,000 products
[3941.78 --> 3948.68]  well zach we would love to keep you on the line for much longer but our our listeners tend to be
[3948.68 --> 3953.82]  commuters so they love commuter friendly shows tend to be around an hour a few minutes after but
[3953.82 --> 3958.86]  we have a few awesome closing questions we love to ask that uh sort of let us know a bit more about
[3958.86 --> 3962.62]  who you are so the first question that we like to ask is who's your programming hero
[3962.62 --> 3970.12]  so or even your hardware hero i guess in this case for you oh yeah so uh my my hero is a guy
[3970.12 --> 3976.24]  named bunny huang bunny is uh uh he's he's well known for do you guys remember a product called
[3976.24 --> 3981.66]  chumbie doesn't ring a bell for me it's like i don't know what it is it's this little like alarm
[3981.66 --> 3987.82]  clock kind of thing that sat on your nightstand like pre it was like apps before the iphone had apps
[3987.82 --> 3992.78]  it was like like uh you know six months they had an app store before uh the iphone did like by six
[3992.78 --> 3998.84]  months um so uh bunny was the hardware lead on chumbie and and chumbie wasn't was like one of the
[3998.84 --> 4006.18]  big open source hardware projects um and he's one of our advisors and the guy is like so smart like
[4006.18 --> 4013.16]  unbelievably smart you guys should actually have him on the show um he uh so he's basically the
[4013.16 --> 4017.58]  godfather of open source hardware um he also wrote a book called i don't know if i'll get the title
[4017.58 --> 4023.48]  right but like reverse engineering the xbox where he literally like you know walks through the process
[4023.48 --> 4029.84]  of reverse engineering an xbox um he since leaving chumbie he's been he advises a lot of hardware
[4029.84 --> 4036.66]  startups like us uh he launched a product called novena which is a an open source laptop uh uh that
[4036.66 --> 4045.68]  has like a fbga it's like got all sorts of crazy stuff in it um he uh recently did a talk on reverse
[4045.68 --> 4053.34]  engineering a 3g baseband uh to so that you could take these like really cheap chips that you can find in
[4053.34 --> 4062.22]  china um and use that are like cellular chips and use them for uh like basically like without
[4062.22 --> 4067.50]  like you can basically build up the same baseband and not pay like massive licensing fees to them or
[4067.50 --> 4072.12]  they probably won't let you do it anyway but like just basically build it as an open rebuild it open
[4072.12 --> 4080.04]  source um and so he is an he's an epic guy and we ask him questions like you know we say oh we're
[4080.04 --> 4084.98]  trying to figure out how to like get good rf performance on the wi-fi chip like can you give
[4084.98 --> 4089.78]  us some advice and he he he always sends us an email that says well i'm not an expert in this
[4089.78 --> 4095.52]  but and then there's this like three page response with every detail that you could possibly need to
[4095.52 --> 4102.04]  solve the problem right so it's like i wish like i hope that i can be as knowledgeable as that one day
[4102.04 --> 4107.84]  um and also be as willing to teach other people and to help other people succeed as he is uh he writes a
[4107.84 --> 4114.46]  great blog bunny's blog and um he's he's a huge mentor of mine so your hero is the founder of chubby
[4114.46 --> 4119.40]  uh i don't actually know if he was the founder maker uh the the hardware lead at chubby okay
[4119.40 --> 4124.76]  cool we'll put uh we'll try and find that link if not we'll work with you to get a link on that
[4124.76 --> 4129.18]  put in the show notes for anybody who wants to follow up on that for sure um next question i'd like
[4129.18 --> 4133.22]  to ask is it is more or less i think you might have answered a little bit during the call but
[4133.22 --> 4138.86]  if you were speaking to the world of open source to a degree what's a call to arms to some of the
[4138.86 --> 4142.34]  projects that are open source for you how can people step in and get involved where are the
[4142.34 --> 4149.60]  most immediate needs today for you yeah so so for us like um you know our firmware libraries are
[4149.60 --> 4156.78]  the area where we're most we're really we'd love to have more people participating um firmware is unique
[4156.78 --> 4161.84]  it's different you know it's it's c and c plus plus it's low level stuff um but what we're trying
[4161.84 --> 4168.26]  to do is make doing low level embedded development easier by taking all of the nasty low level bits and
[4168.26 --> 4175.20]  providing that layer of abstraction and so we'd love help so github.com slash spark slash firmware
[4175.20 --> 4181.92]  is our main firmware repo um and uh would love help from anyone who's interested in participating
[4181.92 --> 4190.16]  and i guess if you weren't doing what you're doing today like hardware software what would
[4190.16 --> 4193.38]  you be doing if you weren't doing x which is today what you're doing what would you be doing
[4193.38 --> 4197.72]  uh that's a good question i don't know it's hard to imagine doing anything different now um i really
[4197.72 --> 4204.72]  like i like being an entrepreneur i like running a company i like making new things i think if i
[4204.72 --> 4209.52]  weren't doing this i'd still want to make something i like i like hardware i like gadgets that's what got
[4209.52 --> 4215.08]  me into this in the first place um so if i you know if spark disappeared overnight and i had to
[4215.08 --> 4220.68]  do something again i'd want to start another hardware startup and and like build something else and maybe
[4220.68 --> 4225.90]  it would be a consumer product which is where we started and it didn't pan out for us uh but you
[4225.90 --> 4231.70]  know i could i would i would try that again and find something like you know to your point earlier like
[4231.70 --> 4237.20]  internet of things is super gimmicky and it doesn't have to be like i think that oh i'll give you one okay
[4237.20 --> 4240.16]  here's what thing that i think somebody should build and if i weren't doing spark this is what
[4240.16 --> 4246.46]  i would build i want a two-factor authentication safe i want a safe that as a code just like every
[4246.46 --> 4252.24]  safe does and i type in the code and i want that safe to send me a text message with a second code
[4252.24 --> 4258.28]  and then i type that code in also using the same two-factor authentication principles that we use
[4258.28 --> 4263.52]  on all these web services with physical security that's my like if i weren't doing spark i would love
[4263.52 --> 4269.82]  somebody that idea is for free if anybody wants to make that we'll give you dev boards uh tools to
[4269.82 --> 4274.82]  get started so someone steals so someone steals your safe or tries to break into it they gotta have
[4274.82 --> 4278.70]  your phone too yeah they have to have your password but also they have to have your phone just like
[4278.70 --> 4283.68]  you know the you the same way you'd use that for security for your web service so i'm waiting for
[4283.68 --> 4292.56]  somebody to to build that to a face safe dot com yeah kickstarter that thing oh yeah that's an awesome
[4292.56 --> 4298.08]  one um and i guess the last cool question we have and this one is is sometimes fun because it could
[4298.08 --> 4302.24]  be your own your own stuff it could be something that you hack on that's not your stuff but what's
[4302.24 --> 4306.58]  in your open source radar what are projects that if you had a weekend and you weren't potentially
[4306.58 --> 4311.62]  hacking on on spark what would you hack on what would you play with that's a good question so you
[4311.62 --> 4315.98]  know i've i'm you know despite the fact that we're talking all about hardware i'm actually more of
[4315.98 --> 4321.78]  like i'm really a front-end guy um like i do a lot of our web design um and so a lot of the the stuff that
[4321.78 --> 4327.20]  i'm uh that i'm involved with is uh from a tech perspective is is on the front-end web development
[4327.20 --> 4333.76]  and so like i've been playing around especially the last couple weeks with uh like using like we're
[4333.76 --> 4340.80]  building express apps and doing a lot of stuff like i uh i think that we were originally using
[4340.80 --> 4347.22]  jackal for some things from like some static sites um ruby library and and uh um and then switched over
[4347.22 --> 4352.06]  to doing stuff in node and um there's some uh a project called metalsmith that i think comes from
[4352.06 --> 4358.76]  a segment uh segment.com um that's sort of a javascript version of of jackal that we were
[4358.76 --> 4364.32]  playing around with and i think it's awesome i love like tool chain stuff like working like playing
[4364.32 --> 4370.42]  with gulp and and projects like um uh metalsmith i love developer tools so things that are making it
[4370.42 --> 4375.22]  easier for other people to do other things so um i'd love to be participating in projects like those
[4375.22 --> 4380.98]  well zach it's definitely been fun having you on the call today i know we can uh learn a lot from
[4380.98 --> 4388.62]  you even though you may not say you're uh an expert in everything like your mentor says you seem to have
[4388.62 --> 4395.24]  quite the expertise in this internet thing software hardware space that you're you're operating in
[4395.24 --> 4399.70]  um for the listeners if they want to catch up with you what's the best way to to reach out like via
[4399.70 --> 4404.86]  twitter github what's some of the common social URLs you share to to for people to get in touch yeah so
[4404.86 --> 4413.96]  on twitter i'm zsupala z s-u-p-a-l-l-a and on github i'm zsup uh z-s-u-p um and uh and also are we so
[4413.96 --> 4420.64]  we have we have forums for spark uh that we love very much community.spark.io uh and my username
[4420.64 --> 4427.78]  there is just zach z-a-c-h so um all those places always happy to chat um and uh happy to help if you
[4427.78 --> 4432.42]  know in particular if people are building stuff and they and they need some advice um always always happy
[4432.42 --> 4438.44]  to uh to offer some help good deal we'll make sure we link up those profiles and places you mentioned
[4438.44 --> 4442.48]  uh in our show notes so if you're a listener head to the show notes for this show which is
[4442.48 --> 4448.48]  actually the changelaw.com slash 150 because this is episode 150 congrats um yeah thank you it's it's
[4448.48 --> 4453.78]  been uh it's been an adventure that's for sure uh and speaking of adventures we have awesome sponsors
[4453.78 --> 4459.48]  that make this adventure possible code ship top town digital ocean love those guys they're so
[4459.48 --> 4465.52]  awesome to us they you know they've supported us to to make this show possible and we're just so
[4465.52 --> 4470.52]  thankful for all the ways that they they support not only us but also the community themselves so
[4470.52 --> 4478.26]  uh those people uh awesome just awesome uh we do have another show coming up episode 151
[4478.26 --> 4483.28]  is featuring steve klabnick and yehuda cats talking about rust jared are you excited about that call
[4483.28 --> 4488.76]  you know i am man you know it what you got uh get the show notes ready already they're ready
[4488.76 --> 4496.74]  already already already we'll be ready we've yeah we've been dying for this show so i i hope
[4496.74 --> 4503.58]  everyone tunes in episode 151 again deep klabnick yehuda cats talking about rust can't wait for that
[4503.58 --> 4507.76]  show but uh until we get there let's say goodbye for now so goodbye everybody bye
[4518.76 --> 4523.74]  you
[4523.74 --> 4526.74]  you
[4526.74 --> 4528.74]  you
[4528.74 --> 4530.74]  you
[4530.74 --> 4532.74]  you
[4532.74 --> 4535.74]  you
[4535.74 --> 4537.74]  you
[4537.74 --> 4539.74]  you
