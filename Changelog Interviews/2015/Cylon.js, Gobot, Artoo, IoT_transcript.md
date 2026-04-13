[0.00 --> 16.46]  welcome back everyone this is the changelog and i'm your host adam stakowiak this is episode 177
[16.46 --> 22.40]  and today jared i'm joined by ron evans and ron is the ringleader of the hybrid group
[22.40 --> 33.30]  and creator of a fleet of open source robot libraries cylon js gobot r2 and we had a blast
[33.30 --> 41.20]  having ron on the show today we had four awesome sponsors for this show code ship opbeat harvest
[41.20 --> 47.86]  and imagix our first sponsor of the show is code ship their hosted continuous delivery service
[47.86 --> 53.48]  focusing on speed security and customizability you can easily set up continuous integration
[53.48 --> 57.10]  for your application in just a few steps and automatically deploy your code when your test
[57.10 --> 63.02]  pass now code ship has great support for lots of languages test frameworks and notification services
[63.02 --> 68.46]  and they even integrate with github and bitbucket and you can deploy to cloud services or even your
[68.46 --> 74.50]  own servers get started today with their free plan when you upgrade to a premium plan use the code
[74.50 --> 81.56]  the changelog podcast and save 20 off any plan you choose for three months head to code ship.com
[81.56 --> 84.56]  slash the changelog to get started and now on to the show
[84.56 --> 97.04]  all right everyone we're back we have ron evans here with us ron is from the hybrid group we met
[97.04 --> 102.98]  jerry we met ron where where we meet him at well i met him a couple years ago at ng conf uh the
[102.98 --> 107.58]  original back further yeah and i remember at the time i said we gotta get you on the changelog
[107.58 --> 113.02]  that's right and you know it's only two years later but uh we got you on and then we met we saw him
[113.02 --> 119.00]  again and you met him at gopher con which is kind of a running theme this fall is a lot of people
[119.00 --> 124.04]  that we met at gopher con on the show but ron it's it's really nice having you thanks for joining us
[124.04 --> 130.80]  hey guys thanks for inviting me uh at long last it's been a long time coming yes it has been and
[130.80 --> 140.12]  yeah it's uh funny at gopher con um i the first gopher con actually i saw a lot of people i hadn't seen
[140.64 --> 148.28]  in a long time from various other open source communities and go really brought them all
[148.28 --> 155.26]  together yeah and the second one most recently same thing but just even more magnified so you
[155.26 --> 161.60]  know kudos to the organizers and also very interesting quality to the go programming world
[161.60 --> 168.54]  that it's attracted people that you know a bunch of old hands and a bunch of cool people who are doing
[168.54 --> 176.52]  new things and you know just lots of enthusiasm absolutely so you're the ringleader of the hybrid group
[176.52 --> 184.64]  and the creator of what i'll just call i guess a fleet of open source robot libraries um why don't
[184.64 --> 188.94]  you go ahead and let us know a little bit about the hybrid group uh what it is and what you do there
[188.94 --> 196.94]  sure so we're a software development consultancy based here in los angeles and we've been called the
[196.94 --> 204.28]  software company that makes hardware companies look good we've done software for a bunch of hardware
[204.28 --> 210.80]  companies such as pebble uh sphero we've worked on a bunch of robotic programming work for them
[210.80 --> 220.94]  particle the wireless micro controller company formerly known as spark oh yeah and um so and intel and a
[220.94 --> 228.08]  bunch of others so so we've been fortunate to have a lot of real world experience with programming
[228.08 --> 236.42]  all of the software around various physical real world devices and so we've taken that knowledge
[236.42 --> 244.16]  you know some people may call it um mistakes lessons learned you know it would be the euphemism
[244.16 --> 252.70]  um we've kind of solidified a lot of that into a series of open source frameworks that basically
[252.70 --> 258.40]  all do the exact same thing in three different programming languages but with the same set of core
[258.40 --> 270.46]  design patterns in javascript it's called cylon.js in ruby we call it r2 ruby on robots and then in the
[270.46 --> 277.92]  go programming language we call it gobot so but they all have the same core set of design patterns
[277.92 --> 283.64]  underneath but then implemented idiomatically in each of the different programming languages
[283.64 --> 291.10]  in a way that programmers in those languages would expect so for example if you're programming in
[291.10 --> 301.04]  javascript it's all callbacks and asynchronous calls if you're programming in go it's uh channels uh
[301.04 --> 309.78]  you know so uh and go routines so we've really said here's a core set of patterns for developing
[309.78 --> 318.14]  physical systems how could we then implement those and provide a set of libraries that work together in
[318.14 --> 326.92]  the form of a framework so that developers can much more easily program the physical world the same way
[326.92 --> 333.82]  as right now web developers program websites yeah you know we really see when we say think outside
[333.82 --> 340.48]  the box you know we're not just speaking metaphorically we literally mean you know out here in the real
[340.48 --> 347.34]  world where stuff happens and it's all very analog and it's you know so there's a lot of interesting
[347.34 --> 354.08]  people who've been working on these sort of things as well and have been contributing um you know when
[354.08 --> 364.00]  when i saw you guys last at gopher con we were just holding the um hardware hack day with a bunch of
[364.00 --> 369.72]  really awesome hardware donated by our friends at intel uh intel has been really really supportive of
[369.72 --> 373.66]  the work that we've been doing in open source they actually are doing a lot of cool open source work
[373.66 --> 382.74]  themselves but we had this massively successful hardware hack day with yeah i mean i don't know how many
[382.74 --> 387.62]  people there was i think there was over 100 people there um i lost count at some point just because
[387.62 --> 394.80]  um you know we basically lost control of the registration i mean it was great you know it was
[394.80 --> 400.62]  fantastic you know we were but we ran out of hardware and yeah i mean i remember i didn't know you had to
[400.62 --> 404.34]  register so i was just kind of we were walking around shooting b-roll and talking to people and i was
[404.34 --> 409.16]  like i'll hop in here and participate and i hopped in and it was like there's no hardware left dude
[409.16 --> 415.84]  it's it's uh it's uh you missed the you missed the ship we got some good footage in that room too with
[415.84 --> 421.92]  um i'm not sure what they were doing but they were doing something with um where you can see gestures
[421.92 --> 429.06]  and like hand motions yes that was using um we've done a lot of work with leap motion yeah that was
[429.06 --> 437.40]  gestural controller company and so we have a whole box full of controllers that we bring with us to
[437.40 --> 444.22]  various hackathons and hack sessions and workshops and kids programming things and just for no apparent
[444.22 --> 449.56]  reason just because they're really cool yeah no wires just wave your hands around i wave my hands
[449.56 --> 453.78]  all the time and nothing happens and you know that's like i'm waving my hands and now something's
[453.78 --> 458.12]  actually happening see i knew it that was exactly it you could see the person's hands on the screen and
[458.12 --> 461.92]  like they were doing different things and interacting and stuff it was pretty interesting
[461.92 --> 470.36]  yeah we've actually had really good support for the leap motion um since they first uh shipped their
[470.36 --> 478.84]  1.0 sdk and uh it's improved quite a lot since then um they have a bone api that actually lets you
[478.84 --> 487.02]  track the different digits within your hands so the sensitivity is quite a lot better um than it ever
[487.02 --> 491.04]  was in the past and you can do some really really cool things i've seen some really awesome demos
[491.04 --> 499.76]  that were done in particular uh my favorite ones were actually done by charlie gerard uh she's a
[499.76 --> 508.26]  developer down under um who's done a bunch of cool things with salon js and leap motion and sphero and
[508.26 --> 514.34]  ar drone you know her demos are always really really fun and she's written a couple of blog posts about
[514.34 --> 521.22]  them so um you know i find that kind of thing really fascinating to see how other people look
[521.22 --> 526.02]  at the stuff that we've made and think of interesting ways to use it you know it's far more interesting
[526.02 --> 530.36]  than the stuff that we do you know at least as far as me personally i'd much rather hear somebody play
[530.36 --> 536.92]  my song than to just play it again myself yeah we definitely want to talk to you about some of the guts
[536.92 --> 542.54]  and the internals and the way that these three libraries work and maybe dive into that but before
[542.54 --> 550.28]  we do that i would like to kind of get your take on the robotics industry at large um you mentioned
[550.28 --> 556.22]  particle and we did have zach is it so paula from spark on back in april i didn't even realize they
[556.22 --> 561.56]  had renamed so we're kind of adam and i are kind of outside our proverbial comfort zone when it comes to
[561.56 --> 566.66]  some of these things we aren't exposed into the you know the hardware community as much as you are so
[566.66 --> 571.64]  um one thing that you and i discussed briefly go for con what i'd like you to elaborate on now is
[571.64 --> 579.66]  the interplay between open source and closed source uh amongst the robotics companies kind of the big
[579.66 --> 585.38]  players that probably our listeners have heard of and that i know of um some of them seem to be all
[585.38 --> 589.48]  about open source some of them seem to be completely closed source can you kind of like lay out the
[589.48 --> 595.14]  landscape for us so we can kind of understand how robotics companies think about open source sure
[595.14 --> 605.40]  well um the drone industry is one really well-known niche within robotics that has gotten a lot more
[605.40 --> 613.16]  attention you know in the last you know year or two in particular uh so there's three companies
[613.16 --> 628.10]  that have been doing extremely well by selling drones to the public the first one is dji so dji many people
[628.10 --> 635.86]  have called them the apple of drones their software is entirely closed source you cannot get any information
[635.86 --> 643.14]  about their sdks unless you register with their developer program you cannot distribute any software
[643.14 --> 651.38]  for their platform without going through their official distribution mechanism so it's you know there are a lot of parallels and also
[651.38 --> 661.30]  they're well known for having a really great consumer out-of-box experience for people so you know they would be at the very closed end of the spectrum
[661.30 --> 667.52]  the opposite end of the spectrum would be 3d robotics which is chris anderson's company
[667.52 --> 680.10]  3d robotics is completely open their hardware is completely open source hardware where they publish the schematics and part listings and bill of materials and
[680.10 --> 689.90]  um in fact the history of the company in brief they were selling a different autopilot that was based on the arduino
[689.90 --> 709.90]  and another company started working on a single board linux um called the pixhawk and they took a look at that it was basically if you can make the hardware better than we can we want to buy your company so you know they basically did exactly that adopted the pixhawk as their official technology
[709.90 --> 716.14]  again still all open source hardware so it's a really classic case of a virtuous circle working
[716.14 --> 724.62]  the software likewise all the apis um for the autopilots are all based on an open source protocol called mavlink
[724.62 --> 733.18]  which is supported by a few hundred different unmanned aerial vehicles unmanned ground vehicles unmanned submersibles
[733.18 --> 762.54]  and uh other things that probably defy description um so they're the opposite end of the spectrum complete openness and they've been doing extremely well in particular agricultural applications that are being built i mean there's a whole ecosystem which has been forming around that for a long time and now it's not just open source cool projects but it's also commercial projects that some of them are fairly substantially funded
[762.54 --> 786.54]  you know and are doing fairly substantial important things as far as work in you know disaster recovery uh bringing medications to remote villages at consistent temperatures you know especially for uh anti-retroviral mechanism uh medications which are highly temperature sensitive and quite costly um agricultural applications of all different kinds
[786.54 --> 800.74]  different kinds so you know there's a lot of really exciting work that's happening and it's not under anybody's control it's all just over the happening so that would be the completely open middle you know side yeah so in the middle
[800.74 --> 814.54]  would be parrot i think would be a great example so with the ar drone best-selling drone ever in history i've heard different stats but you know it's certainly at least uh 250 000
[814.54 --> 843.50]  um ar drone one and ar drone one and ar drone twos um that have been sold so the ar drone uses open source under the hood the um so does the bebop and so does the um their other drones that they're currently selling they're running a busy box linux distro um so but their firmware is not open source
[843.50 --> 858.88]  in fact it's all closed source but their apis are all public they don't require any licensing they're not stopping anybody so you know we might think of them as sort of the semi-open
[858.88 --> 865.14]  or not closed you know depending if you're like a half empty or half full kind of person
[865.14 --> 872.52]  um yeah you know the point being that it's been all sorts of really awesome things that have been created despite
[872.52 --> 878.02]  you know richard stallman lack of complete openness and yet there's a whole ecosystem of
[878.02 --> 884.58]  awesomely fun cool free and open source projects like node copter um you know that have been created
[884.58 --> 892.24]  around this stuff so and they've sold a lot of hardware as well they've been very financially successful so
[892.24 --> 900.38]  three different strategies for how to use open source in the same sector aka drones
[900.38 --> 907.24]  and yet each of them completely viable in their own way so it's really really interesting because you
[907.24 --> 913.30]  know sorry for the extremists out there you know you were expecting a simple answer of course the answer
[913.30 --> 914.84]  is it depends
[914.84 --> 924.64]  reality is always a bummer for the purists out there right yeah i guess you know i'm a purist deep down
[924.64 --> 931.00]  inside somewhere yeah it's the fight between the the romantic purism and the pragmatism that
[931.00 --> 938.38]  tends to take over most of my time as i argue with myself um about which one is the right way so
[938.38 --> 943.44]  so that's interesting somebody has to pay for something somewhere at some point or else the whole thing you
[943.44 --> 948.56]  know comes to a screeching halt especially open source hardware you need some actual hardware and you know
[948.56 --> 955.06]  you burn up parts you brick things while experimenting with them you know you they crash in a very literal
[955.06 --> 962.16]  sense like from the air to the ground in a way that was faster than anticipated or in an angle that was
[962.16 --> 969.72]  you know generally bad for the thing you know in a permanent way um you know so though you know the need
[969.72 --> 978.64]  for companies to support open source and not just sort of coast off of it and you know that's why
[978.64 --> 987.88]  it's great to see like i'm glad um zach from particle you know they're a great example of a company that's
[987.88 --> 994.60]  doing a lot of things right you know sharing a lot of the work that they've done writhing off of a lot
[994.60 --> 1001.20]  of open source and at the same time you know with a good solid value that they provide to other people
[1001.20 --> 1005.22]  so that you know they can actually make some money and still be around for a while because you know
[1005.22 --> 1009.36]  if they're like oh what happened to that awesome company oh yeah they died it was really sad you know
[1009.36 --> 1016.68]  like oh that's terrible you know i've seen a bunch of kickstarters not to pick on crowdsourced companies
[1016.68 --> 1024.20]  not at all quite the opposite really um i feel for a bunch of these companies that i get my weekly
[1024.20 --> 1031.42]  kickstarter apology emails i know you know and and behind each one of them is like a horribly
[1031.42 --> 1037.06]  tormented person that's just feeling all this pain and disappointment and like no that never went down
[1037.06 --> 1042.36]  and you know i couldn't do this thing and you know like you know they're you know not to mention you
[1042.36 --> 1047.42]  know all these people kind of hating on them like hey i thought i pre-ordered my awesome gadget you
[1047.42 --> 1052.76]  know like wait no you actually were betting that we might be able to successfully deliver it and
[1052.76 --> 1059.98]  you know so there's a bunch of companies that they didn't survive to ship and then there's a few
[1059.98 --> 1065.30]  companies that they survived to ship and that effort literally killed them like okay we shipped and like
[1065.30 --> 1072.24]  i'm quitting technology and now going far away from far away from radio signals you know goodbye all
[1072.24 --> 1080.42]  you know and i i really feel sorry for these people because i think wow you know you did not realize
[1080.42 --> 1086.66]  you literally did not realize how bad things were going to be until you got into it and then of course
[1086.66 --> 1090.46]  it was so much worse than you thought and then all these people were expecting you know that's where
[1090.46 --> 1098.32]  you know perhaps a better model for a lot of companies might be you know on the one hand just make some
[1098.32 --> 1105.54]  you know just a handful and then sell them on tindy or something like you got it off your chest and this
[1105.54 --> 1111.84]  way you weren't on the hook for the excessive popularity that may be good and may be bad depending
[1111.84 --> 1117.78]  on whether you could actually you know shipping 50 of a thing might be enough to nearly kill you
[1117.78 --> 1124.24]  shipping 5 000 might be enough to you know you lose all your hair and you lose all your love for
[1124.24 --> 1130.76]  technology and you know of course you lose all your money you know that was sort of a given because
[1130.76 --> 1136.52]  you're like like oh yeah we're going to be able to ship anytime well you also can lose your reputation
[1136.52 --> 1140.48]  because now you're somebody who can't actually come through and you've let down a lot of people
[1140.48 --> 1146.44]  which feels bad but it harms your chances next time around of having you know people supporting your
[1146.44 --> 1153.72]  ideas and your efforts which is difficult too yeah and i think if it was a little bit more
[1153.72 --> 1160.70]  spelled out to the buyer yeah all right sorry let me rephrase that sorry it's clearly spelled out
[1160.70 --> 1165.60]  to the buyer but if people didn't interpret it the way that they're pre-ordering the thing as
[1165.60 --> 1172.74]  opposed to their sort of you know investing in the potential of a dream you know they're giving
[1172.74 --> 1179.66]  somebody a chance to do an experiment you know i wish people looked at it that way because you know
[1179.66 --> 1184.42]  if it was a little less high stakes well i think that's a two-edged sword though i think you know
[1184.42 --> 1189.32]  specific to some kickstarters they actually pitch it as if they're going to get it like they show the demo
[1189.32 --> 1194.02]  they like they do hype some dreams up because they because they do have to actually you know
[1194.02 --> 1199.02]  collect some money to make it happen so they do have to sell a little bit right you know so sometimes
[1199.02 --> 1205.60]  they can be not purposefully but in a way misleading because you think well i'm going to fund this today
[1205.60 --> 1209.48]  and in a year from now just like they said everything's going to go perfectly so i'm expecting
[1209.48 --> 1216.32]  this thing and then you know snag one snag two snag three later it's three years out and you're like
[1216.32 --> 1222.18]  well i'm never going to get this thing yeah exactly um you know and if it all just quietly
[1222.18 --> 1227.24]  go away as you said you know that would be nice for the original people of course it doesn't
[1227.24 --> 1235.04]  it's the internet nothing goes away ever um in some cases too that gap right that in some cases when
[1235.04 --> 1242.42]  you don't ship the technology has been replaced by apple pay i'm thinking for example um this one card
[1242.42 --> 1248.60]  that was like smart i can't remember the name of it right coin coin coin yep so i'm a good example
[1248.60 --> 1255.16]  that i actually bought that thinking like heck yeah man i want that i got myself one i got my wife one
[1255.16 --> 1261.40]  and i was like this is gonna be awesome and then between the time they you know were in deep in their
[1261.40 --> 1267.62]  tech and deep in their r&d they uh they got sideswiped by the bigger people which became much
[1267.62 --> 1274.66]  a bigger play for square apple android they all have their payments platform you know so
[1274.66 --> 1282.42]  well the nfc chip was already in the android phones literally it was just deploying um iphones with that
[1282.42 --> 1290.10]  chip and all of a sudden all the software was ready yeah so it's a classic case of if you only have a
[1290.10 --> 1296.88]  feature then you probably don't have a company yeah if you have a full product you know that's that's a
[1296.88 --> 1302.80]  whole nother story but there's a lot of you know the interesting thing is that there are companies
[1302.80 --> 1310.32]  and individuals who now have some experience with these things and they're a lot more readily able
[1310.32 --> 1318.44]  to successfully help you navigate that space and uh we work with one in particular uh called highway
[1318.44 --> 1328.02]  highway one which is a accelerator based in san francisco um so highway one uh they've been
[1328.02 --> 1337.54]  responsible for some really cool companies like uh navdi and um julie bots which is a really cool
[1337.54 --> 1347.76]  programmable jewelry for young girls um excuse me so there's some really fantastic things that come out
[1347.76 --> 1352.96]  of these you know of an accelerator because they help you navigate you know in their particular case
[1352.96 --> 1358.62]  they're it's specific to hardware companies so these companies you know they they're able to come in
[1358.62 --> 1366.78]  to a program where they have access to mentors of different sorts you know hardware software etc
[1366.78 --> 1372.46]  helping them navigate the process of getting to a thing only once they've gotten through that whole
[1372.46 --> 1378.28]  program only then should they really think about doing the crowdsourcing you know crowdsourcing
[1378.28 --> 1384.34]  you know premature crowdsourcing doesn't really lead to success either just because you fail because
[1384.34 --> 1391.58]  it's so damn hard to succeed there's so many things you can go wrong or you know you hey this is you
[1391.58 --> 1398.04]  know the new you know square i've reinvented the wheel you know when i was a little kid reinventing the
[1398.04 --> 1404.58]  wheel was a pejorative it was like it was considered a bad thing like oh you reinvented the wheel nowadays
[1404.58 --> 1409.42]  like you've reinvented the wheel i want to invest you know how do i get in you know
[1409.42 --> 1418.62]  but the problem is of course is um you know your wheels turned out to be square and made of wood
[1418.62 --> 1423.34]  yeah there was a good reason why the industry had standardized on rubber and round
[1423.34 --> 1430.78]  and you know you and your amazing hubris and success of the cool video that got your crowdfunding
[1430.78 --> 1434.78]  you know everyone's like yeah the square wheels and then you ship the first few square wheels and
[1434.78 --> 1439.88]  people are like you know these wheels suck you people are idiots and you're like oh you know i know
[1439.88 --> 1443.58]  this sounds when we're talking about square wheels it sounds like it's obvious but you know it's
[1443.58 --> 1449.98]  obviously a lot more subtle so the fact that there are some successes and failures we can all go take a
[1449.98 --> 1455.82]  look at now and say all right this worked and this didn't one of the things that's a common
[1455.82 --> 1462.90]  characteristic of successes is they did as little as possible and what i mean what i mean by that
[1462.90 --> 1468.64]  specifically is they used open source well whether it was open source hardware platforms like the
[1468.64 --> 1474.28]  particle whether it's open source software of different kinds you know they did as little as
[1474.28 --> 1482.40]  possible to actually get to some kind of you know demonstrable product ideally a shippable one even
[1482.40 --> 1489.42]  if it was just a 1.0 version because if you spend all the time going off and doing all this work or
[1489.42 --> 1495.32]  starting your own hey we're going to open source it that's not a panacea either you know just saying
[1495.32 --> 1500.36]  okay we're going to slap it on github and make it a public repository does not an open source project make
[1500.36 --> 1506.02]  right so in fact quite the opposite they're like wait you're running your company on this code like
[1506.02 --> 1510.90]  oh my god i kept like first of all the hackers have a field day not that they couldn't already just with
[1510.90 --> 1519.22]  metasploit and other scanners right you know you've already got a whole world of hurt that can come in
[1519.22 --> 1525.72]  you know i don't consider open sourcing your code to be significantly exposing your attack surface
[1525.72 --> 1532.16]  but it does significantly expose your incompetence if you fail to do it you know well yeah that's true
[1532.16 --> 1539.20]  right and the opposite you know we've seen individuals really really smart people come
[1539.20 --> 1547.30]  sort of humbly doing a cool thing that you know quietly like solves a real problem you know i'm talking
[1547.30 --> 1555.40]  about mitch hashimoto right now um actually so mitch um i've known mitch for a long time um his
[1555.40 --> 1564.54]  company hashi corp um they're the people originally you know who now have auto most recently um so i've
[1564.54 --> 1570.08]  known mitch for a really long time um we worked together on a bunch of things um way way way back
[1570.08 --> 1578.12]  in the day um so he he actually was a consultant that uh consultancy based here in los angeles called
[1578.12 --> 1583.28]  citrus bite and citrus bite has had a lot of really interesting people who passed through there just
[1583.28 --> 1591.32]  because los angeles not being known for as a major tech company you know location for a long time
[1591.32 --> 1595.12]  you know so a lot of interesting people sort of have passed through similar fashion the hybrid group
[1595.12 --> 1601.34]  you know so anyway so mitchell you know came up with vagrant just worked on it very humbly super smart
[1601.34 --> 1607.24]  guy solving a real problem doing this thing lots of people paying attention suddenly all of a sudden
[1607.24 --> 1613.32]  you know boom you know boom overnight success years in the making and oh yeah all built on top
[1613.32 --> 1618.44]  of open source and oh yeah all built on top of really good open source that's why people used it
[1618.44 --> 1622.28]  was because they looked at the source and they said this is actually good code that's solving a real
[1622.28 --> 1630.62]  problem and i could improve on it and you know so i'm not at all surprised at the success that they're
[1630.62 --> 1636.04]  experiencing right now because it was earned it was earned over a long period of time it's not just
[1636.04 --> 1641.00]  like a sudden you know boom out of nowhere nothing like that speaking of auto adam you might want to
[1641.00 --> 1646.12]  tease our upcoming show with mitch yeah we actually have an upcoming show with mitchell we saw auto as
[1646.12 --> 1650.46]  well we've been fans of vagrant around here for a long time so when we saw auto we were pretty excited
[1650.46 --> 1658.30]  about uh just seeing you know their constant chipping away at this this problem so even if it supersedes
[1658.30 --> 1662.46]  vagrant or not it's still pretty interesting so oh that's really funny hey mitch how you doing
[1662.46 --> 1668.20]  yeah upcoming show with mitch i say hi i say hello your future self from the past here
[1668.20 --> 1674.00]  and uh while we're doing it let's let's go ahead and take a break and pay some bills have a sponsor
[1674.00 --> 1680.04]  come in and tell some awesome stuff uh one way you can support us is by supporting our sponsors so
[1680.04 --> 1686.84]  have a listen if it intrigues you check it out we'll be right back guess what everyone
[1686.84 --> 1692.16]  opbeat is announcing their no js beta right here right now exclusively to our listeners
[1692.16 --> 1698.62]  opbeat combines performance metrics release tracking and error logging into a single simple service
[1698.62 --> 1704.30]  and with all of your data in the same place they're able to do smart things with it and help you make
[1704.30 --> 1709.88]  wiser choices opbeat integrates with your code base through git and makes monitoring and debugging your
[1709.88 --> 1716.08]  production apps much faster it's free for an unlimited number of users and until now has only been
[1716.08 --> 1722.44]  available for django and flask but now they're launching a private beta for node.js and sharing
[1722.44 --> 1729.08]  it with our listeners first so go check it out and sign up for the beta head to opbeat.com slash changelog
[1729.08 --> 1734.46]  that's opbeat.com slash changelog
[1734.46 --> 1743.06]  all right we're back with ron evans uh ron the self-professed ringleader of the hybrid group
[1743.06 --> 1747.78]  you guys are doing some really interesting things uh some questions jared and i have
[1747.78 --> 1753.88]  are uh the three different projects you have they're in three different languages you got silent js gobot and
[1753.88 --> 1760.96]  r2 so why three different projects and why three different languages well every programming language
[1760.96 --> 1768.40]  does something really well or else nobody would use it at all of course but the inheritance of that
[1768.40 --> 1776.20]  language would often proclaim its superiority in all things as opposed to you know generally being
[1776.20 --> 1781.20]  curious about why is somebody using that other language the one that i don't use myself you know
[1781.20 --> 1787.04]  what's so good about that you know and it falls into these kind of religious debates and wars most much
[1787.04 --> 1794.96]  of the time um unfortunately just because of this sort of technological tribalism um the cool thing
[1794.96 --> 1801.42]  about the early days of language communities is they're usually the polyglots you know the people
[1801.42 --> 1807.18]  who are you know genuinely curious at learning as many programming languages as possible just to try to
[1807.18 --> 1812.30]  grok you know exactly what is it about this that's so cool because somebody must like this thing i mean
[1812.30 --> 1817.42]  there's a bunch of people using it let me understand what that thing is because it could be good for my
[1817.42 --> 1827.00]  brain to expand my own sort of thinking but at the same time each language you know community also has
[1827.00 --> 1835.64]  a human side to it which is sort of the flavor of how you know ruby it's a very test oriented type of
[1835.64 --> 1841.84]  culture if you're talking to a bunch of ruby programmers and you show them your ruby code and there's
[1841.84 --> 1848.80]  you know no tests they'll say in mock horror oh my goodness you have no tests let's sit down and write
[1848.80 --> 1855.04]  some tests together you know we'll get your code tested you know if you're a python programmer and
[1855.68 --> 1861.28]  you don't have any documentation that's other generated they'll be like oh my goodness you need
[1861.28 --> 1868.32]  some documentation let's sit down we'll help you write some docs you know that's just a characteristic
[1868.32 --> 1873.44]  you know the javascript community is a little different it's more trailblazers like let's just
[1873.44 --> 1877.76]  you know blaze a trail and you know if you could follow that trail after me and you know good that's
[1877.76 --> 1883.44]  great but you know i'm sorry i moved on to a new trail you know so it's more exploratory not necessarily
[1883.44 --> 1892.64]  worrying about you know the the you know keeping up with what's already been done uh the go community
[1892.64 --> 1898.96]  on the other hand being a very new community of of much very hardcore programmers from other
[1898.96 --> 1904.40]  disciplines you know has a certain newness to it you know we don't know what it's going to turn into
[1904.40 --> 1910.48]  eventually but one thing is that the discipline that it enforces has brought a really interesting
[1910.48 --> 1915.92]  group of people together so each one of our frameworks you know takes advantage of the strengths
[1915.92 --> 1922.72]  of the particular community as well as the particular language and tools around it you know
[1922.72 --> 1929.92]  Cylon.js has a real has more hardware support than the other frameworks because there's a lot of people
[1929.92 --> 1939.12]  doing cool hardware hacking over in the javascript world you know from the stuff that all of the spin-offs
[1939.12 --> 1944.88]  of node serial port which was uh chris williams project you know to all the stuff that's going on
[1944.88 --> 1950.88]  through johnny5 which is rick waldren's project you know to all the stuff going on with node copter
[1951.52 --> 1957.84]  with the tessel which is the javascript powered microcontroller with all the stuff that intel has done
[1958.48 --> 1966.96]  with all of the stuff that uh marvell's new javascript uh powered microcontroller with samsung with i
[1966.96 --> 1973.76]  think it's called jimmy js or something johnny i forget anyway they have a new stripped down
[1973.76 --> 1981.68]  javascript runtime to specifically to run on their arctic line of microcontrollers and single board
[1981.68 --> 1988.40]  linux computers so there's a lot of people doing hardware hacking in the javascript world so of course
[1988.40 --> 1993.36]  we have more support for more pieces of hardware there because you know our framework it's all about
[1993.36 --> 1998.16]  the design patterns that we apply and if there's already a library that talks to a particular piece
[1998.16 --> 2005.20]  of hardware you know we're we'd much rather be using that especially if we can be using a library
[2005.20 --> 2012.16]  that is also being used by other subcultures within the javascript world you know because javascript is
[2012.16 --> 2021.04]  very very tribal within itself you know case in point being the node.js and io.js schism and subsequent
[2021.04 --> 2027.52]  reunification much to all of their credits you know cooler heads prevailing which i you know i'm not
[2027.52 --> 2032.88]  a member of either one of those communities directly per se so i'm happy to see them you know getting
[2032.88 --> 2038.72]  together i'm kind of doing my own thing and i have been um you know as far as sort of pursuing the design
[2038.72 --> 2047.28]  patterns around physical computing really it started in 2008 with um something in ruby called ruby arduino
[2047.28 --> 2055.68]  development that was a project from greg bornstein who um ended up going back to grad school at uh
[2056.32 --> 2061.36]  nyu's interactive technology program which is where massimo pansi the creator of the arduino is one of
[2061.36 --> 2069.60]  the professors really amazing place um so the work that we've done you know first it started with r2
[2069.60 --> 2074.00]  just because it was natural in ruby it was really about creating frameworks that supported multiple
[2074.00 --> 2079.52]  different hardware platforms even all at the same time it was about using the adapter patterns
[2080.40 --> 2084.16]  in order to communicate with all sorts of different categories of devices and it was really about
[2084.16 --> 2091.52]  identifying interfaces to talking to whole categories of devices and how can we do interface-based
[2091.52 --> 2097.60]  programming you know in ruby well there is nothing in the language that enforces interfaces
[2097.60 --> 2103.20]  and then javascript well there's nothing in the language that enforces interfaces it doesn't mean
[2103.20 --> 2110.72]  you can't do it you can absolutely do it but you do it through customs you know like we agree that
[2111.36 --> 2115.36]  you know when we both come to the door at the same time that one of us is going to stop and let the other
[2115.36 --> 2121.20]  one go through first but there's no rule there's like there's no traffic cop there's no camera there's no
[2121.20 --> 2127.84]  buddy enforcing this custom you know so in dynamic languages interface-based programming is something
[2127.84 --> 2134.48]  that's enforced by custom and not by rule in gobot on the other hand because gobot is able to utilize go
[2135.20 --> 2143.04]  go is all about interface-based programming and by defining certain categories of interfaces
[2144.08 --> 2149.36]  the implementations of which could talk to different completely different hardware platforms you know
[2149.36 --> 2152.88]  could be talking to a beagle bone black could be talking to a raspberry pi can be talking to an
[2152.88 --> 2159.52]  intel edison you know with a minimum of changing of code this is a really really powerful paradigm
[2160.40 --> 2168.80]  for programming of the physical world and so you know each one of the frameworks is it takes advantage of
[2168.80 --> 2176.32]  each of the languages capabilities and also of the community behind it you know go has a really
[2176.32 --> 2182.00]  you know rapidly growing and really active community and they're really interested in hardware hacking
[2182.80 --> 2186.40]  javascript people they've been interested in hardware hacking for a long time and you know the node
[2186.40 --> 2191.52]  bots community and node copter and you know a bunch of some of these communities you know consider
[2191.52 --> 2196.72]  themselves competitive to silon js you know we don't consider ourselves competitive we're more just sort
[2196.72 --> 2202.56]  of like hey we have our band and we're playing our music you know we hope you like it you know you have a
[2202.56 --> 2207.60]  band too that's really cool we'd like to hear it you know your band's music doesn't mean anything
[2207.60 --> 2213.52]  towards our band's music nor vice versa you know and let's hey let's have a music festival you know
[2213.52 --> 2220.16]  that's that's sort of the jamming and code attitude that you know that i've tried to have and you know
[2220.16 --> 2227.04]  certainly hybrid group is also and lots of other people too you know it's interesting perspective to
[2227.04 --> 2231.52]  take it from like a you've got your band i've got my band we play our songs you play your songs
[2231.52 --> 2237.52]  kind of approach towards uh what you said earlier much earlier which was reinventing the wheel you
[2237.52 --> 2242.96]  know to a degree which is why we said you know why three different projects three different languages
[2243.52 --> 2249.68]  you know essentially you recreated the wheel for each camp right well the way it sort of played out
[2250.56 --> 2259.52]  you know um ruby is a great way to learn ideas and to play with ideas you know we've seen a lot of
[2259.52 --> 2267.84]  interesting new concepts come from the ruby world a really good example would be sinatra you know the
[2267.84 --> 2280.48]  sinatra pattern for you know developing web mini applications has been adopted widely you know express js
[2281.20 --> 2289.28]  flask and python noir enclosure you know martini and a couple of other ones and go
[2290.08 --> 2294.88]  i mean there's a lot of people who use express js who have no idea that express took every one of
[2294.88 --> 2302.24]  its ideas in whole cloth from sinatra and you know tj who wrote express never tried to hide that quite
[2302.24 --> 2308.56]  the opposite you know tj's biggest contribution to the node world was he could look at ruby jams
[2308.56 --> 2314.00]  that do the thing and rewrite them in node really quickly that was a huge contribution because it really
[2314.00 --> 2318.56]  accelerated but you know a lot of people in in the node world had no idea where that stuff originally
[2318.56 --> 2323.68]  came from which is you know funny yeah but the reason why they didn't use ruby was because ruby was
[2323.68 --> 2331.68]  great for ideas but you know ultimately ruby's virtual machine is its weak spot you know and it's the
[2331.68 --> 2339.20]  the it's its undoing um you know the kinds of applications that people want to write increasingly
[2339.20 --> 2347.84]  involve some ways to deal with concurrency and you know j ruby is a great project fantastic project
[2347.84 --> 2355.76]  amazing what those guys have done you know its strength is the jvm and its weakness is the jvm
[2356.32 --> 2360.64]  like if you're committed to the jvm then j ruby is for you it's absolutely fantastic but if you
[2360.64 --> 2365.52]  weren't thinking of using the jvm or you know you intentionally weren't using it because you're
[2365.52 --> 2370.88]  running on you know really small or underpowered hardware single board linux computers you know in
[2370.88 --> 2377.84]  in our case you know it's not really something you could take seriously you know you're trying to go
[2377.84 --> 2386.56]  the other way how much can i get rid of right you know rubinius um cool project but splintering off
[2386.56 --> 2391.12]  of the main ruby implementation you know there was already problems with fragmentation i mean look
[2391.12 --> 2397.68]  look what happened with you know node with node and iojs which finally pragmatists there said you
[2397.68 --> 2403.60]  know we better get back together before something bad happens and we lose all of our collective momentum
[2403.60 --> 2412.40]  around this thing you know java's node is a hack all right it's a hack language purists concurrency purists
[2412.40 --> 2420.08]  can you know get into the details about you know but ultimately it's a hack that we all need it
[2420.08 --> 2426.08]  because it solved the biggest problem that most programmers have these days which is not the general
[2426.08 --> 2433.52]  case of concurrency but it's really just about blocking io you know if you're writing programs for the web
[2434.16 --> 2438.24]  your biggest problem is blocking io because you know you've got requests that have to go off and you
[2438.24 --> 2443.68]  know do something and then respond so if you're writing applications that are talking to physical
[2443.68 --> 2450.56]  devices your biggest problem is blocking io you are waiting for the servo to move to the stepping
[2450.56 --> 2455.92]  motor to a particular position so you can then you know do something with this other motor so i mean
[2455.92 --> 2463.92]  you're waiting for io so i'm not at all surprised that a lot of people who are node programmers found out
[2463.92 --> 2470.00]  hey node is actually really cool for device programming only because the hack that they put in is the
[2470.00 --> 2477.04]  hack that we needed you know it doesn't solve the general concurrency case go on the other hand was designed
[2477.04 --> 2485.60]  by very serious people who had spent a long time not succeeding you know and figuring out okay this is
[2485.60 --> 2494.56]  going to work and this is not and over that long period of time really synthesizing down some more
[2494.56 --> 2498.88]  fundamental solutions to the concurrency problem at large and so we could take advantage of that
[2499.68 --> 2507.36]  in gobot to do device programming you know that's something that most people in go hadn't really thought
[2507.36 --> 2513.36]  about but once they start to think about it wow this is a great way to do the kind of concurrent
[2513.36 --> 2518.32]  programming that you need if you're going to program robotics or internet connected devices or drones
[2518.32 --> 2527.44]  or these other things in fact wow it's a multi architecture so i can cross compile it so i can you know compile
[2527.44 --> 2534.00]  it on my computer and you know scp the file over to the drone to execute it you know there's a bunch of
[2534.00 --> 2541.52]  advantages to developing code using go which translate very directly to the kinds of problems
[2541.52 --> 2547.60]  problems that device programmers now not necessarily the ones who are programming on microcontrollers
[2548.24 --> 2555.28]  but that's you know again that's a false argument oh well go doesn't run on arduino so you can't use it
[2556.48 --> 2564.16]  well that is sort of saying you're going to develop all of your complete internet connected
[2564.16 --> 2569.60]  application using nothing but microcontrollers there's just no way they're too underpowered
[2569.60 --> 2574.64]  on the other hand you can't do it all with single board linux computers either because they're too expensive
[2575.28 --> 2580.64]  you know for these small cheap sensors that need to be deployed in mass to all these different places to do all these different things
[2581.76 --> 2589.60]  well the answer is a heterogeneous architecture you know you've got microcontrollers which are connected
[2590.16 --> 2596.32]  possibly through wi-fi possibly through bluetooth or bluetooth low energy you know particle has got a
[2596.32 --> 2602.48]  great option there and you're talking to some type of hub you know some type of single board linux computer
[2603.04 --> 2607.20]  you know whether that's a raspberry pi or beaglebone black or the far more powerful intel edison
[2607.92 --> 2616.32]  you know so now you've got a complete suite of different possible solutions to bring to bear to the problem so
[2616.32 --> 2621.44]  you can push as much intelligence to the edge as possible that way if the internet goes down
[2622.16 --> 2628.08]  you know your home security system doesn't lose all capabilities or what have you you know your home
[2628.08 --> 2635.20]  agricultural system no longer works and so you know your you know your crop dies or you know your industrial
[2635.84 --> 2642.08]  processing plant no longer has the ability to get you know external data so of course it shuts down and
[2642.08 --> 2647.68]  you know you have a fire or something i mean this is we the internet of things needs to be about
[2647.68 --> 2653.04]  the internet of things and not the aol of things and that's where open standards and open source are
[2653.04 --> 2660.24]  so important so each one of these communities you know the ruby world is more about learning how robotics
[2660.24 --> 2669.04]  work i don't see a large adoption in ruby as far as getting excited about device level programming for
[2669.04 --> 2675.12]  various reasons the javascript world is very excited about it and is pursuing all sorts of different
[2675.12 --> 2681.12]  avenues and you know that's the most popular of our frameworks but gobot is coming you know up very
[2681.12 --> 2690.48]  quickly in popularity um it's in one it's in the 99.9th percentile of github stars uh for golang projects
[2691.04 --> 2696.72]  you know and that's competing against you know docker and core os and everything i mean we're at the bottom
[2696.72 --> 2704.24]  on the top okay make no mistake the very bottom like last one's in you know last slot but um that
[2704.24 --> 2708.56]  kind of leads me into my question was you got these three you know let's take your band analogy you've
[2708.56 --> 2713.60]  got these three songs that you've written and if you had to take one of them and and you had to pick
[2713.60 --> 2718.56]  a single that you're going to play on the radio or whatever would it be gobot and would it be
[2718.56 --> 2730.24]  cylon which one would you uh pick to be the the hit cylon js is the popular song right now but gobot is a
[2730.24 --> 2735.44]  whole new genre of music that once people realize what it is they're going to get even more excited
[2735.44 --> 2743.44]  about it because a lot of insiders already are so i was gonna i would say you know salon js this year's
[2743.44 --> 2752.96]  grammy's gobot next year's i don't know okay now my head just exploded from being too large you know
[2752.96 --> 2759.76]  let me remind uh our listeners that all of these projects have a lot of contributors both direct
[2759.76 --> 2764.08]  contributors that you see in the commit logs indirect contributors who paired with those people
[2764.96 --> 2770.72]  indirect contributors who just pointed stuff out through twitter email hey you at the conference
[2770.72 --> 2776.40]  you know these are very much the product of a lot of people thinking about them and really that's
[2776.40 --> 2782.32]  the great thing about open source is you know you play the song once and it turned into a whole nother
[2782.32 --> 2787.92]  song so if you like that sort of thing you're really happy but if you're trying to keep control over my
[2787.92 --> 2794.32]  music then you know you don't like it one bit yeah i personally have found that you know the song that
[2794.32 --> 2800.32]  people thought they heard me play and then they played back to me was way better than the original song i
[2800.32 --> 2804.96]  played which i can't even remember what it was right now because your songs your version of my song was
[2804.96 --> 2810.00]  so much better than mine yeah that's why i like when you said it's like a jam band because it really is
[2810.00 --> 2816.24]  as far as you know there's people riffing off one another yeah the uh those different takes on it
[2816.24 --> 2823.60]  actually improving the overall the overall thing so i want to ask you about the different platforms
[2823.60 --> 2828.80]  supported maybe cylon is the most popular because of the javascript community maybe because it supports the
[2828.80 --> 2834.48]  most platforms but uh before we get into that let's take a quick break here from a sponsor and
[2834.48 --> 2841.36]  we'll be right back all right listeners out there who are working solo or on a team tracking time for
[2841.36 --> 2848.48]  your projects and billing for invoices imagine this scenario you thought you were wrapping up a project and
[2848.48 --> 2852.56]  the client asked for a new feature at the last minute and they got questions about time spent on the
[2852.56 --> 2858.64]  project well do you know how much time you're spending on every feature tweak or bug fix to give
[2858.64 --> 2864.64]  them that feedback well harvest is a time tracking tool built just for that for understanding where
[2864.64 --> 2870.16]  time is going and billing for that time they even have built-in reporting that lets you know how much
[2870.16 --> 2874.88]  time your projects took so you can use that information to make better estimates in the future
[2874.88 --> 2879.60]  not only will you understand how much time you're tracking on your client work you'll also be able to turn
[2879.60 --> 2887.36]  those billable hours into invoices in minutes create a free 30-day trial today at getharvest.com
[2887.36 --> 2892.80]  after your trial's over enter our code changelog to save 50 off your first month
[2896.00 --> 2903.52]  all right we're back talking about robots with ron with a hybrid group ron you've got cylon your most
[2903.52 --> 2911.76]  popular project um you got gobot the up and come or next year's grammy winner and uh they support
[2911.76 --> 2918.88]  different platforms so you mentioned that um the javascript one supports the most play it has 36
[2918.88 --> 2926.64]  different platforms gobots got about 15 maybe speak about the platforms themselves what you know the
[2926.64 --> 2931.92]  interesting ones and then why the discrepancy and and the support from one library to the next
[2933.20 --> 2943.12]  so the different devices and platforms that we support are kind of in a couple different categories
[2943.12 --> 2950.64]  one of them are things like single board linux computers where we're actually talking directly to the
[2950.64 --> 2961.04]  the pins to turn on and off the digital signals to turn on and off leds or motors um my uh friend
[2961.04 --> 2968.64]  julian cheels um who's done a lot of really great talks about dancing drones he pointed out that most of
[2968.64 --> 2974.48]  the internet of things is just turning things on and off you know whether it's turning on and off light
[2974.48 --> 2983.52]  bulbs or motors or leds or you know whatever those happen to be and so a lot of the devices or platforms
[2984.48 --> 2989.92]  the intel edison you know the beaglebone black we actually are able to take advantage of the built-in
[2989.92 --> 2999.04]  linux operating system for the general purpose input output or gpio interfaces as well as the
[2999.04 --> 3008.32]  i square c or i2c which stands for inter inter chip communication a very brief uh inter inter chip
[3008.96 --> 3015.04]  yeah so when board designers it turns out so you think board designers are magic beings who wave
[3015.04 --> 3022.88]  their magic soldering irons aka wands and somehow this mysterious spooky device that you just plug your
[3022.88 --> 3028.80]  cables into that somehow works oh man you really nailed it there that's exactly turns out they're just
[3028.80 --> 3036.08]  as lazy as software programmers perhaps even more so it's just they do it with circuits instead of
[3036.72 --> 3042.48]  with modules and libraries um most electrical engineers never actually get to design a circuit
[3042.48 --> 3047.76]  they take various circuits that do well-known things and combine them together and you know and that's how
[3047.76 --> 3051.92]  they i mean it's very hard work don't get me wrong is it like is that like copy paste kind of
[3051.92 --> 3059.28]  yeah uh yeah similar in fact they have tools like eagle you know another cad programs which actually
[3059.28 --> 3066.48]  enforce a bunch of these rules because turns out that there's rules of physics that are you know quite
[3066.48 --> 3074.72]  well defined and you know quite fixed when it comes to the board level design so um you know you
[3074.72 --> 3079.92]  if you're going to build a drone for example you don't start completely from scratch you say okay what do
[3079.92 --> 3086.24]  i need i need some accelerometer i need a barometer so i know my altitude i know a magnetometer so i can
[3086.24 --> 3092.48]  figure out which way the thing is pointed so you get chips that do each one of these things and you
[3092.48 --> 3098.96]  put them onto your board the way that they communicate with each other is so-called inter inter chip
[3098.96 --> 3107.44]  communication or i2c is how you see it written the old timers call it i square c so if you know you know
[3107.44 --> 3112.56]  which you can go either way depending on how much gray hair is in the room at the time but um
[3114.56 --> 3123.52]  excuse me so um you know we have support for these different devices so all of our frameworks
[3123.52 --> 3128.96]  have kind of the same set of design patterns you have connections connections are how you physically
[3128.96 --> 3135.12]  are going the protocol physically to communicate with a particular piece of hardware it could be a serial
[3135.12 --> 3145.92]  port it could be bluetooth low energy it could be linux gpio and then you have devices devices are
[3145.92 --> 3153.44]  things like leds or buttons so where the connections are the you know physical part of the communication
[3153.44 --> 3160.88]  you know the transport if you will devices are the behaviors leds know how to blink buttons can be
[3160.88 --> 3169.04]  pushed and could be either on or off digital compasses have a heading etc so we can combine these two
[3169.68 --> 3176.16]  patterns together basically a double adapter pattern so the same digital compass will work
[3176.80 --> 3185.28]  regardless of whether it's on an intel edison or a beaglebone black or an arduino so in the case of the arduino
[3185.28 --> 3193.76]  we communicate with a c program that's running on the arduino's firmware itself that supports a
[3194.80 --> 3201.84]  serial protocol called fermata fermata is basically a descendant of the midi protocol which is used for
[3201.84 --> 3210.32]  musical instruments and it is a way for a computer to talk to an arduino and say is your digital pin
[3210.32 --> 3218.88]  you know number one turned on because the button's being pushed or turn on digital pin 6 to flash or 13
[3218.88 --> 3224.00]  to flash an led so it's a way of communicating with the microcontroller from an external computer
[3224.80 --> 3232.24]  that's how we communicate with the particle the the particle is essentially a microcontroller that has an
[3232.24 --> 3240.00]  api on it so you can call this api through particles cloud servers wherever the thing is as long as it's
[3240.00 --> 3247.68]  connected to the local wi-fi network so our frameworks use these different interfaces whether it's a gpio
[3247.68 --> 3253.28]  interface or an i2c interface to communicate with all the different hardware platforms that support that
[3253.28 --> 3263.28]  interface whether it's a particle or an intel edison so it's a great way to apply the same sort of
[3263.28 --> 3269.84]  patterns the database programming in web development has for a long time you know you you switch between
[3270.40 --> 3276.72]  you know mongo and you know couch db or something you switch between mysql and postgres you don't really
[3276.72 --> 3281.76]  think that much about it just because you've got some plumbing under the hood which is handling this
[3281.76 --> 3287.68]  so we're applying those same exact principles but to physical systems development and we're doing
[3287.68 --> 3294.40]  it not just for the gpio and i2c interfaces but also for other interfaces so we there's other devices
[3295.04 --> 3302.16]  which are themselves complete autonomous robotic units like sphero right sphero really great example
[3302.72 --> 3310.08]  so the sphero is the robot toy from sphero of boulder colorado from star wars
[3310.08 --> 3316.96]  um can't talk about the star wars thing what they already announced it i could they could talk about
[3316.96 --> 3324.64]  it but i can't talk about it the one thing i can say the one thing i could say is um there may be very
[3324.64 --> 3330.88]  soon open source support for a sphero that happens to have a head
[3330.88 --> 3340.64]  that's all i'm allowed to say um can't can't name names okay but uh but that's you know you can't say
[3340.64 --> 3347.28]  but if it just so happened to work that would be really cool um anyways but the spheroes that you
[3347.28 --> 3353.68]  have today that we have official support for you know it's really the minimum viable robot it has
[3353.68 --> 3361.28]  output and that you can send it bluetooth so it's a bluetooth device or in the case of the ollie and uh
[3361.76 --> 3369.28]  the sphero with a head it's a bluetooth low energy uh device but they use the same protocol as far as
[3369.28 --> 3377.12]  the same packets that send it commands to roll around and it also has input it has a built-in
[3377.12 --> 3384.72]  accelerometer so it's able to detect collisions for example so it's the simplest possible
[3385.28 --> 3392.16]  input and output you know we joke around we call it the minimum viable robot and it's great for
[3392.80 --> 3397.28]  people who want to learn about robotics but they don't want to get into the whole soldering or plugging
[3397.28 --> 3403.44]  things in you know that's they're more interested in making their robotic device do something that's
[3403.44 --> 3408.08]  the part that interests them as opposed to the you know how do i actually build it up from nuts and
[3408.08 --> 3414.96]  bolts you know and you really need both and a lot of other people too yeah i mean admittedly that'd be
[3414.96 --> 3420.08]  the that'd be the camp that i would be more in is like how do i make this sphero with the head
[3420.72 --> 3426.64]  uh do something you know programmatically as opposed to how do i build my own you know robot from the
[3426.64 --> 3432.48]  ground up or whatever yeah the software wing of the hardware hacker movement if you will
[3432.48 --> 3440.96]  yeah you know the fun part is it really called sphero with a head yes that is not the official
[3440.96 --> 3448.24]  name that's the that's the operative term for avoiding um imperial entanglements let's just say
[3448.24 --> 3455.28]  imperial entanglements good uh good use of the word but um but we have a really really good support
[3455.28 --> 3464.24]  for some of these complete robotic devices through again interfaces you know kind of a rover style
[3464.24 --> 3470.80]  interface you know forward back left and right so you could apply that same concept of coding so if
[3470.80 --> 3477.76]  you're using a sphero or you're using the sphero's uh little brother the ollie you know you're still using
[3477.76 --> 3483.44]  the same style of interface if you're programming a couple of different kinds of drones you know same
[3483.44 --> 3489.76]  idea you know knows it has a takeoff command it has a land command you know it has an interface which
[3489.76 --> 3496.08]  is well understood now we can mix and match our controllers you know you could be using a joystick
[3496.08 --> 3503.12]  you could be using a leap motion and our drones could be using you know a 3d robotics iris could be
[3503.12 --> 3509.52]  using an ar drone could be using a paired bebop you know we're applying these same sorts of principles
[3509.52 --> 3515.52]  that you know i know web developers are going yeah no big deal right you know everyone else is going
[3515.52 --> 3519.36]  wait you're saying you can use the same code and change two lines of code and be running out a
[3519.36 --> 3524.56]  completely different piece of hardware yes that's exactly what i'm saying so that's that thought is
[3524.56 --> 3531.68]  pretty avant-garde in the in the hardware world space yeah that's our contribution that's the reason why we
[3531.68 --> 3535.92]  have our own frameworks as opposed to just jumping in on somebody else's frameworks because there's a
[3535.92 --> 3542.88]  lot of cool work that's been going on you know but you know but we've been doing we boxed ourselves in
[3542.88 --> 3550.80]  we wrote a framework in 2008 2009 specifically for unmanned aerial vehicles using ruby and you know
[3550.80 --> 3555.44]  there's a bunch of youtube videos and my little brother damon and i you know flew around the world
[3556.24 --> 3561.44]  you know carrying tanks of helium on our shoulders through exotic cities you know we could say
[3561.44 --> 3566.96]  we could ask for a tank of helium in like six languages it's amazing but um but it was really
[3566.96 --> 3573.60]  too early and also it was very limited it only worked with arduinos and at the time that seemed
[3573.60 --> 3580.72]  like it was you know really big and open-ended well now we realize there's so much more there's a bunch
[3580.72 --> 3586.32]  of different ecosystems based around different hardware platforms unique capabilities some of which are shared
[3586.32 --> 3593.28]  so if we can apply these same set of design patterns we can really do something important
[3593.84 --> 3600.24]  as far as making it easier for people to program their physical world so it's not just you know the
[3600.24 --> 3607.20]  professional peace priesthood of programming as it's been but it's really for every human
[3607.20 --> 3617.44]  giving this sort of ability to do more you know because eventually this is where everything's going
[3617.44 --> 3623.28]  right the same way mobile is today physical computing you know internet of things and robotics will be in
[3623.28 --> 3629.04]  you know five years you know you'll have app stores you'll have big ipos some gigantic successes some
[3629.04 --> 3635.20]  you know massive failures you know in short all the same sort of stuff that we see today in mobile
[3635.20 --> 3643.28]  so you know we have invested really heavily in terms of our time and also you know paying people
[3643.28 --> 3653.52]  to work on open source to say look let's start doing this now everybody so that we can have the
[3653.52 --> 3658.80]  renaissance that we hope that it can become and it's not just a few big companies dominating the
[3658.80 --> 3664.48]  landscape because the innovation really comes from individuals and small groups
[3664.48 --> 3670.16]  you know that's really where innovation comes from that doesn't mean that can't happen at big
[3670.16 --> 3675.36]  companies but it happens within those companies and it's not the company as a whole and we need to
[3675.36 --> 3683.60]  encourage also non-commercial types of development solving problems that maybe aren't you know highly
[3683.60 --> 3689.60]  renumerative but they're important for the world you know those are the kind of problems we also need to be able to work
[3689.60 --> 3695.68]  on and if we can make it easier and cheaper for people to actually do that then instead of getting
[3695.68 --> 3701.52]  disheartened of saying oh wow i'm trying to boil the ocean saying no no no just just boil this one pot of
[3701.52 --> 3707.04]  water it's all it's all you need to do you know and somebody else will do their part and so on you know
[3707.04 --> 3713.52]  that's how we got to where we are now as opposed to living in a closed source world so ultimately this can win
[3713.52 --> 3720.40]  but it requires a collective commitment to it and you know right now there's a lot of companies
[3720.40 --> 3724.24]  throwing their hats in the ring of saying we want to build the back end for your internet of things
[3724.80 --> 3728.56]  you know i just don't want it to be the aol of things i want it to be the internet of things and
[3728.56 --> 3734.64]  it's the openness and the interoperability it may seem scary like wow you're saying we can make it
[3734.64 --> 3738.72]  possible for our competitors to get right into our systems like yes that's right and that's going to keep
[3738.72 --> 3744.72]  you honest that's going to keep you on edge and actually doing something useful or you won't be
[3744.72 --> 3753.44]  relevant anymore another question for you here what's the coolest thing you've seen somebody make
[3753.44 --> 3759.60]  with one of your libraries either cylon gobot or r2 you know you mentioned you can mix and match all
[3759.60 --> 3764.00]  these things and come up with something amazing has anybody really wowed you with something they've done
[3764.00 --> 3774.24]  with with uh these frameworks well um some of the stuff that i've seen um in particular in education
[3775.04 --> 3780.08]  you know that's the stuff that that excites me personally but i know there's you know important
[3780.08 --> 3786.08]  or highly profitable or you know big money investments in some but the ones that excite me personally
[3786.08 --> 3796.56]  list yeah are the ones that i've seen where it's you know little kids um we we did um a bunch of work
[3796.56 --> 3807.44]  with some visual programming tools in participation with sphero and google for um youth io youth io is a
[3807.44 --> 3814.48]  kids programming event that takes place the last day of the google io event this was the second year
[3814.48 --> 3821.36]  um a couple of months ago and so it was a visual programming environment that ran on chromebooks
[3821.84 --> 3834.64]  specific for a lunar mission where the kids would do visual programming to you know control the spheroes
[3834.64 --> 3841.92]  and their lego mindstorms robots you know to navigate this lunar landscape and they had to get through this tunnel
[3841.92 --> 3850.72]  and then i i just thought this is such an incredible application of so much technology
[3850.72 --> 3855.04]  like the amount of engineering that to do this deceptively simple thing you know it's the
[3855.04 --> 3860.40]  technological equivalent of playing a conga drum right it looks really easy to you actually try to do it
[3860.40 --> 3866.96]  and you're like oh man that's really hard you know i thought it was easy like no no no that to me that was
[3866.96 --> 3876.96]  the most personally exciting is seeing the looks on the kids faces as they grok the concepts of
[3876.96 --> 3883.04]  programming you know because kids are much smarter than adults ever give them credit for right they
[3883.04 --> 3887.04]  don't necessarily have this ability to express themselves in the same ways they don't necessarily
[3887.04 --> 3893.44]  have the same fine motor skills but their ability to comprehend you know researchers are consistently
[3893.44 --> 3898.96]  learning that babies long before they're actually able to vocalize or able to understand a lot more
[3898.96 --> 3906.48]  speech than was ever previously thought you know and that's very consistently true through the entire
[3906.48 --> 3912.64]  developmental cycle if you've ever learned to speak a foreign language um you've probably experienced
[3912.64 --> 3918.40]  that directly right it's much easier to learn to understand than to initiate the things you want to
[3918.40 --> 3924.16]  say outside of a few canned phrases but to actually you know hold a full intellectual conversation
[3924.16 --> 3930.08]  where you don't just understand but you're able to respond and and you know initiate concepts in the
[3930.08 --> 3938.96]  conversation so watching these kids grab these ideas and turn them into variations of these ideas
[3938.96 --> 3943.76]  there in real time and the amount of work that it took to actually get to that but that was unlocking
[3943.76 --> 3948.80]  their creativity in that some of these kids are going to go on themselves and build all these amazing
[3948.80 --> 3955.12]  things you know not necessarily using these tools but that doesn't really matter you know you have to
[3955.12 --> 3961.28]  ask yourself at some point is what you care about the fact that this mission is being accomplished or do
[3961.28 --> 3967.36]  i care about that my name's on the mission you know when it comes to kids and teaching programming
[3967.36 --> 3971.52]  you know you got to take yourself out of the equation to the maximum extent possible while still at the
[3971.52 --> 3978.56]  same time recognizing you know you have a leadership role to play by what you choose to do but ultimately
[3978.56 --> 3983.20]  it's not about you it's about them they're they're going to take these ideas and do something with them
[3983.20 --> 3989.44]  and you know you can't control it all you can really do is sort of inspire it and then you know then it's
[3989.44 --> 3998.00]  up to their parents ha ha ha i have my own kids so i got my own problems so that's a great uh that's a great
[3998.00 --> 4007.12]  one-time opportunity for kids have you seen robotics and in and teaching uh in any sustained ways uh out
[4007.12 --> 4013.28]  there as far as things that just you know and continue to teach as opposed to like just get kids excited and
[4013.28 --> 4028.08]  then kind of move on oh yeah um so i was lucky that um i guess the the virtue of having um of being a
[4028.08 --> 4032.88]  little ahead of people because of life experiences like i happen to have you know my oldest son is a
[4032.88 --> 4037.44]  teenager so you know if i started caring a little bit earlier about kids programming than some younger
[4037.44 --> 4045.52]  people it's because i had a kid so you know sure wow amazing um but i was just the latest of the new
[4045.52 --> 4050.40]  generation i mean it goes back to alan k and it goes back to papert and it goes back to before them
[4051.28 --> 4058.24]  you know of you know how do we teach critical thinking to the next generation and i think it was
[4058.88 --> 4064.24]  you know if we go back i believe it was cicero complaining about you know the youth of the ancient
[4064.24 --> 4071.20]  roman times yes you know so it's like oh yeah okay so so like i i'm sorry i'm gonna vote with the
[4071.20 --> 4080.80]  delinquents on this one um you know but if nothing else they're more fun but um you know the ideas
[4080.80 --> 4088.48]  that we are unleashing through teaching programming you know coming to town and saying hey kids you know
[4088.48 --> 4093.44]  here's this one-time thing we did this kids code camp was what we called it you know we were doing
[4093.44 --> 4099.20]  them in 2011 um you know and it was literally like a programming circus comes to town yeah you know
[4099.20 --> 4107.04]  we would do a one-day thing we brought in experts um the first one actually was we sort of hit the
[4107.76 --> 4116.64]  home run out of the park um so cory haynes who i'm sure you know cory um so cory was supposed to come
[4116.64 --> 4124.24]  and teach the scratch class um but he flaked no he couldn't make it because of some no he he literally
[4124.24 --> 4129.44]  could not make it and he was super bummed because he really wanted to do it and and i was really
[4129.44 --> 4136.56]  bummed too because i really needed him to do it i wanted scratch and uh so um we were introduced to
[4137.20 --> 4145.68]  the one of the teachers at the liberal arts and science academy of austin texas which is a high school
[4146.64 --> 4151.92]  university and one of the teachers there said oh yeah i'd love to come and teach the class then he got
[4151.92 --> 4157.36]  back to us the next day saying oh i got really bad news i can't make it either and we're like oh god
[4157.36 --> 4163.92]  like we can't we can't cut a break then the very next day he contacts back and he says listen
[4164.96 --> 4170.40]  some of my students here at the high school said they would really like to teach this class and i'm like
[4170.40 --> 4175.60]  like my jaw is on the ground okay literally there's tears in my eyes i'm like you know
[4176.64 --> 4184.40]  so they put together a curriculum themselves they came in and taught the elementary age students
[4184.40 --> 4189.60]  these high school kids and their curriculum was so good that when i showed it to cory cory's like oh
[4189.60 --> 4193.68]  this is much better and he adopted their curriculum and started using it as part of the scratch stuff
[4193.68 --> 4200.56]  that he was doing wow okay like that was that was a magical moment because that was sort of
[4201.36 --> 4207.60]  you know that's the holy grail of education the mixed age peer learning you know montessori style
[4208.32 --> 4215.12]  you know re-learning by teaching and the fact that we were actually able to hit that but then the
[4215.12 --> 4223.20]  programming circus rolled away so what now luckily for us collectively when i say us all of us
[4223.68 --> 4228.32]  humanity a bunch of other people started thinking about this problem and started caring about it
[4228.32 --> 4235.92]  enough to do something uh coder dojo fantastic work that they've done you know sort of bringing back
[4235.92 --> 4243.12]  the computer club of your you know weekly you know a place to go hang out and just sort of play around
[4243.12 --> 4251.52]  with stuff you know fantastic uh code.org code.org where where where our team was sort of like hey let's write
[4251.52 --> 4256.00]  some software and we wrote kids ruby code.org you know they were video producers like let's get the
[4256.00 --> 4265.44]  word out that was really important to do that because the more support that the broader community
[4265.44 --> 4269.52]  not just i mean we programmers know that programming is important already we do it every day all the time
[4269.52 --> 4275.68]  right it's the rest of the people you know helping you know share and make it easier for them
[4275.68 --> 4284.32]  to if nothing else understand how a technological world works you know not necessarily from the
[4284.96 --> 4289.60]  everyone become a programmer but to everyone understand that programmers run the world and they make
[4289.60 --> 4294.80]  mistakes due to the program errors and so you know maybe you shouldn't push the red button
[4295.60 --> 4301.68]  you know because that might be an error like are you sure sure sure you know you want to launch the first
[4301.68 --> 4310.88]  strike you know so just having uh well educated well i mean you know it could be law enforcement
[4310.88 --> 4315.52]  realizing oh there was an error with this person had the same name but obviously there was a very
[4315.52 --> 4324.72]  different gender and you know height and age like we're we were looking for an 87 year old woman and this
[4324.72 --> 4331.52]  is a 16 year old guy pretty sure that like this is a computer error you know sort of common sense thinking
[4331.68 --> 4339.28]  that does not necessarily occur when people accept you know the dea ex mechanica what the computer says
[4339.28 --> 4345.52]  is absolutely always infallibly correct when that's absolutely not the case right and so knowing
[4346.80 --> 4352.64]  a little bit of common sense of like well let's just hold up for a minute and verify that that was
[4352.64 --> 4358.00]  indeed the first strike launch order you know it's something that all of us would like to know exists in the
[4358.00 --> 4366.16]  world and so you know it's those are extreme examples but they happen in very minor ways all the time
[4366.16 --> 4373.92]  through minor decisions that are increasingly made by machine we need the general populace to understand
[4373.92 --> 4381.44]  the implications of that so that they can be informed not just how to make good policy on that
[4381.44 --> 4389.28]  you know at the governmental level but also just how do you deal with it on a day in day out like what to do
[4389.28 --> 4396.80]  if the garbage robot malfunctions kind of thing well first of all stay away from it you know kind of idea you know i mean
[4396.80 --> 4404.40]  these are common sense i you know the self-driving car error you know most of those problems are due to the people well most of the
[4404.40 --> 4409.28]  problems in the world are due to the people and programming error is the same so it's not about
[4409.28 --> 4415.44]  creating a generation of entrepreneurial programmers i think that's very much of a red herring i think it's
[4415.44 --> 4421.28]  more about how do we create a better world by acknowledging the place that technology has taken
[4422.96 --> 4431.04]  of importance the same way that we expect our doctors and our lawyers to have certain professional and
[4431.04 --> 4437.84]  ethical standards software and hardware people eventually are going to have to grow up and
[4437.84 --> 4444.56]  recognize we also are going to have to recognize our place in the broader world and what part
[4445.12 --> 4448.96]  that we have in that and how can we be making things better and not worse
[4450.32 --> 4457.52]  well said let's uh let's stop here for another quick break here from another one of our awesome sponsors
[4457.52 --> 4464.32]  when we get back ron i want to ask you about getting started uh with some of these libraries and with
[4464.32 --> 4472.24]  programming robotics and then of course our awesome closing questions so after the break uh we'll do that and we'll be right back
[4474.40 --> 4484.48]  imagex is a real-time image processing proxy in cdn and let me tell you this is way more than image magic running on ec2 this is way better
[4484.48 --> 4493.68]  it's everything your friend and developers have dreamt of output to png jpeg jpeg jpeg 2000 and several other formats
[4494.24 --> 4501.28]  and if you're like me you've ever argued with your boss or a teammate about serving retina images to non-retina devices
[4501.84 --> 4507.68]  you'll appreciate their open source dependency free javascript library that allows you to easily use the
[4507.68 --> 4515.04]  imagex api to make your images responsive to any device now all this takes a platform and the imagex
[4515.04 --> 4522.64]  platform is built on three core values flexibility and quality performance and affordability when it
[4522.64 --> 4530.32]  comes to flexibility and quality imagex has over 90 url parameters that you can mix and match to provide
[4530.32 --> 4537.20]  an unlimited amount of transformations that you need for your images and they take quality very seriously and
[4537.20 --> 4543.84]  because of their commitment to quality several top 1000 websites in the world trust them to serve their
[4543.84 --> 4550.32]  images now when it comes to performance imagex operates out of data centers filled with top of
[4550.32 --> 4556.56]  the line mac pros and mac minis and they're set up for a completely streaming solution this means your
[4556.56 --> 4563.28]  images never hit the disc images are served by the best ssd based cdn for delivery around the world
[4563.28 --> 4569.68]  anywhere extremely fast and while we're talking about speed almost all the image processing happens
[4569.68 --> 4575.84]  on gpus this means transformations are super fast when compared to competing virtualized environments
[4576.64 --> 4581.84]  and lastly it's all about affordability everyone wants to save a buck that's how the world works
[4582.40 --> 4588.80]  because imagex processes close to a billion with a b images per day they're able to make certain
[4588.80 --> 4595.68]  optimizations at scale and pass those savings on to you to learn more about imagex and what they're all
[4595.68 --> 4606.16]  about head to imgix.com slash changelog once again imgix.com slash changelog and tell them adam from the
[4606.16 --> 4615.44]  changelog sent you we're back with ron evans ready to find out ron how do you get started i'm sure there's
[4615.44 --> 4624.08]  plenty of developers out there now excited about the not the aol of things but the internet of things
[4624.64 --> 4632.72]  and specifically how they can use cylon or r2 or gobot to program some hardware um what would you say to
[4632.72 --> 4640.08]  somebody who's just like okay let's let's do this what do i do how do i get started well first of all um
[4640.08 --> 4649.36]  you better get buy-in from your significant other um he or she is going to have to uh deal with your
[4649.36 --> 4655.60]  new electronic habits so uh that's a that's important that you shouldn't hide these types of
[4655.60 --> 4661.60]  addictions there's gonna be a cash investment probably into some hardware i guess oh yeah um but
[4662.16 --> 4670.96]  the beauty of it is there's a lot of really great um kits that combine together sort of the minimum
[4670.96 --> 4684.48]  necessary pieces um seed studio uh spark fun and adafruit are three online um retailers that have put
[4684.48 --> 4693.68]  together various kits that work with um you know the arduino is sort of the gold standard of micro
[4693.68 --> 4700.88]  controllers the minimum viable market controller um of course that's better for people who want to
[4700.88 --> 4709.04]  actually assemble some pieces if you buy something called the grove starter kits then a grove connectors
[4709.04 --> 4715.36]  or little plug-in type connectors uh those are the one the kits that we used uh the gopher con hackathon
[4716.00 --> 4720.88]  that way you can assemble some basic circuits without actually having to solder anything just
[4720.88 --> 4726.96]  by plugging in the connectors you know that makes it a lot easier to get started you know before you
[4727.52 --> 4731.20]  you know not that many people have soldering experience it's great to learn how to solder but
[4731.20 --> 4735.60]  you might want to do that the separate project just a pure electronics project as opposed to the
[4735.60 --> 4740.56]  you know programming soldering together the whole robot and then programming it you know could take
[4740.56 --> 4748.56]  quite a long time um and that this way you can get started a lot more quickly um the intel edison
[4749.20 --> 4755.52]  has a couple of different starter kits that we have really good support for with our frameworks um they
[4755.52 --> 4761.60]  have the base starter kit the same sort of starter kit which is also available for the raspberry pi and the
[4761.60 --> 4770.16]  the arduino with a few basic sensors up then from there if you what you're really more interested in
[4770.16 --> 4777.28]  is how can i have some type of programmable device to then you know make it do things the sphero robots
[4777.28 --> 4786.88]  are really excellent you can get them typically um sphero now has a program called spark sprk where they have
[4786.88 --> 4792.96]  a special educational program with uh heavily discounted so that's a great way to get a hold of a sphero robot
[4794.08 --> 4803.28]  the um we have support for if drones making things fly is is what's getting you excited the parrot it's really
[4803.28 --> 4810.40]  hard to go wrong um to a large extent just because you can get replacement parts as well when you're flying things
[4810.40 --> 4819.68]  around you're probably going to crash um a bunch of times so the um new parrot rolling spider for 99
[4820.48 --> 4826.40]  is a great option for if you want to just have a programmatic control over a flying device
[4828.08 --> 4834.64]  um so those are some of the and then there's lots of really great peripherals of different kinds
[4834.64 --> 4841.68]  you know whether that's the leap motion gestural controller um there's a couple of brain computer
[4841.68 --> 4852.48]  interfaces that we have support for the neuro sky mind wave and also the muse um which are both bluetooth
[4853.92 --> 4861.76]  um electroencephalograms or eegs which are able to read your brain waves so practice meditation or
[4861.76 --> 4867.28]  have the drone fly off when you get really agitated or maybe you should do the opposite maybe it should
[4867.28 --> 4873.20]  land if you get really agitated you know that might be better yeah you know so there's a lot of different
[4873.20 --> 4880.72]  toys you know you might consider them toys in fact a lot of them come from toy stores you know we call it
[4880.72 --> 4890.00]  iot to us means internet of toys and you know to any sufficiently advanced technology starts out in the form of a toy
[4891.76 --> 4897.68]  right if you want to know what the next big thing is go to a really really good toy store
[4898.48 --> 4907.12]  and look around right look around in the so-called science section you know scientific toys you know
[4907.12 --> 4913.84]  so you go over there and you're like let's see hydrogen cell fuel kit oh you know home dna test kit
[4913.84 --> 4919.44]  how about that and of course like a pile of robots pile of robots yeah but these are rock and sock and
[4919.44 --> 4924.48]  robots so they're fully you know bluetooth low energy interface you know api available there's
[4924.48 --> 4929.36]  a real world you know human size or even larger rock and sock and robot thing do you see that where
[4929.36 --> 4937.20]  they're trying to fight japan yeah well on that listen team usa you guys are looking great but you
[4937.20 --> 4943.12]  should be in contact with limor freed she should be the captain of the team if if we put her in charge
[4943.12 --> 4950.00]  i think the possibility of our success is significantly higher really just saying just
[4950.00 --> 4954.64]  saying you should i don't think they may or may not hear this but you could you send them an email
[4954.64 --> 4961.04]  might be more effective yeah well you know she's got the street cred and you know being a new yorker i
[4961.04 --> 4968.72]  think she can she's got the right pit fighter attitude to you know but uh you know when i was in uh tokyo
[4968.72 --> 4979.20]  um speaking at ruby kaigi and um very very nice man was introduced to me by tender love aaron pattishon
[4979.92 --> 4984.88]  and uh this guy turned out to be one of the heads of the japanese national institute of science and
[4984.88 --> 4992.80]  technology who uh told me about his uh permanent installation at the museum that was right down
[4992.80 --> 4998.32]  the street from where the ruby kaigi conference was and i was like oh wow i really want to go see that so
[4998.88 --> 5005.20]  went over there and turned out that's the museum where the asimo is and wow you know so so they're
[5005.20 --> 5012.96]  very far ahead as far as developing robotic technology and also adoption of it culturally but
[5013.68 --> 5018.24]  you know we've seen a lot you know particularly with drones what you know we would have called
[5018.24 --> 5023.76]  unmanned vehicles a few years ago but now you know anything that flies under robotic control is a drone
[5023.76 --> 5028.40]  yeah what's the definition of drone is that it right there anything that flies in a robotic control
[5029.76 --> 5034.80]  well you know like the mainstream definition of drone is similar to the mainstream definition of
[5034.80 --> 5039.60]  hacker yeah just in other words they took our word from us and they ran with it and whatever we
[5039.60 --> 5044.48]  wanted to do something bad do with that word then we tried to take it back and we failed um
[5044.48 --> 5053.92]  drones originally um actually the first drones were airplanes that flew themselves through mechanical
[5053.92 --> 5064.16]  means during world war ii uh during world war ii the average survival rate for fighter pilots was only
[5064.16 --> 5067.68]  you know a few minutes of air combat before they got shot down and killed
[5067.68 --> 5077.12]  so it turned out this was a real problem in the air war um and they developed these airplanes that
[5077.12 --> 5084.72]  they would literally take off by themselves and fly a pre-determined flight pattern and then the human
[5084.72 --> 5090.88]  pilot would take off in another airplane and shoot down this other airplane that was what a drone was
[5090.88 --> 5100.08]  in circa world war ii and so you know drone aircraft meant you know eventually they were remote controlled and
[5100.08 --> 5107.76]  you know it meant any vehicle that was remotely piloted you know became a drone and you know hence the
[5107.76 --> 5112.80]  predator drones which are not you know technically really flying robots but they're actually you know
[5112.80 --> 5120.24]  telepresence flying telepresence with weapons you know as opposed to it you know autonomous
[5120.88 --> 5126.72]  robot robot you know the things that you see for example in the darpa challenge or in the spark
[5126.72 --> 5131.12]  fun autonomous vehicle challenge which is you know slightly more friendly version
[5133.12 --> 5139.36]  you know these are devices where the intelligence to make all the decisions is entirely in the device
[5139.36 --> 5147.04]  itself of course that's a little bit of a false dichotomy right human beings we have the problem of our
[5147.04 --> 5153.12]  brain and our body have to be attached or else bad things happen right you know robotic devices no
[5153.12 --> 5159.20]  such requirement you know that's where swarms or you know the brain is safely on earth while while the
[5159.20 --> 5165.84]  body rolls around the planet mars you know out of curiosity you know and a bunch of those systems
[5166.40 --> 5171.12]  you know so you know there needs to be intelligence in the devices themselves but also
[5171.12 --> 5178.88]  you know there's a distinctly human component whether that's the decision making process you know fire or
[5178.88 --> 5185.68]  do not fire the missiles or you know you know conduct this experiment but i mean it's really really hard
[5185.68 --> 5192.16]  a neighbor of mine um actually works on at the jet propulsion laboratory in pasadena on some curiosity
[5192.16 --> 5200.88]  related work and the latency of communicating with a robotic device on another planet you know it
[5200.88 --> 5208.00]  you think you got problems flying your drones around your backyard have fun with that right yeah
[5210.08 --> 5215.76]  well uh it's definitely been a blast having you uh on the call ron i know that was uh great meeting
[5215.76 --> 5221.12]  you at uh at gopher con loved having you at hack week it was a lot of fun seeing a lot of the people
[5221.12 --> 5226.88]  in your class and then you're in your um in your room they're just kind of doing some really interesting
[5226.88 --> 5233.84]  things and uh what y'all are doing at the hybrid group for it as well on the open source side is is really interesting so we
[5233.84 --> 5239.92]  appreciate your love of everything the one closing question we think we have to ask you though is uh
[5240.48 --> 5246.00]  who your hero is so we ask those who come on the show who's your programming hero so who's that for you
[5246.00 --> 5254.80]  wow i have um a bunch of programming heroes actually um i have to only pick one well i'm gonna give a
[5254.80 --> 5262.40]  shout out to the late great jim weirich uh jim was a the creator of the rake programming language
[5263.20 --> 5271.04]  um and innumerable other open source projects he was the only guy who was a chief scientist who i didn't
[5271.04 --> 5276.56]  laugh at that title by asking them if they had peer-reviewed papers and where the last one was
[5276.56 --> 5283.68]  you know jim was an amazing contributor to a lot of other projects as well um very humble guy a lot
[5283.68 --> 5290.00]  of people felt like he was their best friend uh programming and uh he was definitely is missed
[5290.00 --> 5296.80]  in the ruby community and so um i would have to say of all my programming heroes i miss him the most
[5296.80 --> 5304.32]  yeah well yeah we uh yeah those things same thoughts we have uh who was that recently jared who had a
[5305.04 --> 5313.84]  their hero was uh was jim the karen meyer karen meyer yeah oh karen's amazing okay well you know karen
[5314.72 --> 5322.64]  um she the work that she did with closure drone um which you know i don't know if she's i saw her at
[5322.64 --> 5329.44]  oscon um fairly recently and it was really great because we'd never actually met up in real life
[5330.00 --> 5334.64]  although we had worked together on some stuff so it's really funny all the answer that is crazy
[5334.64 --> 5339.04]  but but the stuff that she's doing with autonomous drones and the closure language is absolutely
[5339.04 --> 5345.36]  fascinating amazing work and you know jim is really missed by both of us because he was one of the few
[5345.36 --> 5350.80]  people who understood you know of the people in the ruby world i felt like jim was one of the few people
[5350.80 --> 5357.04]  who really understood what i was trying to do and how much more it was just than ruby and so he's
[5357.04 --> 5365.20]  missed even more for that vision of seeing right you know and contributing really actively you know
[5365.76 --> 5369.76]  he just got really excited about a lot of projects and you know he'd done some really cool stuff with
[5369.76 --> 5378.24]  drones and i was really excited to um to make him excited and happy when i showed r2 for the first
[5378.24 --> 5384.08]  time at the los angeles ruby conference and it was using the argus gem that he had worked on you know
[5384.08 --> 5388.48]  with a bunch of patches that i didn't submit as a pull request because i wanted to surprise him
[5388.48 --> 5393.68]  so he was in the front row and he he saw the box for the ar drone and then i pulled the whole thing
[5393.68 --> 5398.48]  out and you know did the talk it was just the fact that i was able to make him happy for a minute
[5399.28 --> 5404.64]  that really made me happy like to give back because he was a really humble guy who did a lot of things for a
[5404.64 --> 5413.04]  lot of people and you know everyone who ever used rake still uses it today not realizing you know and
[5413.04 --> 5421.60]  just doing this thing and playing this ukulele yeah i i showed him how to play blues music on ukulele
[5421.60 --> 5428.16]  true story um actually the same day that i showed him that you could use ruby for unmanned aerial vehicles
[5428.16 --> 5435.20]  the fact that i could bring something to a brilliant guy like him like i don't mean like oh i'm so great
[5435.20 --> 5441.28]  i mean like i felt genuinely grateful that i could offer him something back in return because he did so
[5441.28 --> 5446.32]  much for so many people and never thought of himself really he was just doing it so the fact that i could
[5446.32 --> 5453.76]  even bring him anything at all ever as sort of uh you know hey thanks you like you know because we're all very
[5453.76 --> 5460.00]  hungry for new information and that i think that includes everybody and you know some people they're
[5460.00 --> 5464.24]  you know humble enough to acknowledge it and other people they just sort of like sneak around and
[5464.24 --> 5468.40]  quietly look at what everybody else is doing because we're all really hungry for new information and so
[5468.40 --> 5477.04]  jim you know he was overt about it he was like if he didn't know something he would instantly ask you
[5477.04 --> 5482.08]  what's that he didn't pretend like he knew things that he didn't already know that's how he learned so
[5482.08 --> 5487.84]  quickly and he was able to come up with so much was that you met just a curious mind and so you
[5487.84 --> 5493.76]  know let's let's all be like that let's all be curious absolutely stay curious my friends stay
[5493.76 --> 5498.48]  curious well ronald it was definitely a pleasure to have you on the show i know that uh i'm sure our
[5498.48 --> 5505.12]  listeners have appreciated your passion for hardware open source internet of things creating the software
[5505.12 --> 5510.32]  behind some of the best hardware out there as you mentioned earlier in the show and the passion you
[5510.32 --> 5516.88]  have you know for not only ruby but go and also javascript and how it can affect the future of
[5516.88 --> 5522.40]  these uh the directions we've talked about today uh but i want to thank our awesome listeners who
[5522.40 --> 5527.84]  listen to the show each week without you it would be possible because who would listen uh we also have
[5527.84 --> 5535.68]  awesome sponsors that make this show possible code ship opbeat harvest and imagex and uh ron i know this
[5535.68 --> 5540.56]  has been a long time in the making this show here with you uh but it was great meeting you at gopher con
[5540.56 --> 5545.68]  look forward to seeing you further out there in the open source world my friend but for now let's all
[5545.68 --> 5554.08]  say goodbye jared adam thanks so much to all of you listeners out there in internet lands i just want
[5554.08 --> 5562.24]  to say thanks for taking the time and go program something right now boom bye guys that's the way i do it
[5562.24 --> 5584.16]  and
[5584.16 --> 5614.14]  We'll be right back.
