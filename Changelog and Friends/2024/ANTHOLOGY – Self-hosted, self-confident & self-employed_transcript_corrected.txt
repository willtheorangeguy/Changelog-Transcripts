[0.00 → 22.14] welcome to changelog and friends a weekly talk show about ATO hallway vibes thanks to our
[22.14 → 28.88] partners at fly.io the home of changelog.com launch your app in five minutes or less learn how
[28.88 → 32.18] at fly.io okay let's talk
[32.18 → 43.90] what's up friends I'm here with Dave Rosenthal CTO of century so Dave when I look at century I see you
[43.90 → 49.54] driving towards full application health error monitoring where things began session replay
[49.54 → 55.30] being able to replay a view of the interface a user had going on when they experienced an issue
[55.30 → 60.68] with full tracing full data the advancements you're making with tracing and profiling chrome
[60.68 → 67.84] monitoring co-coverage user feedback and just tons of integrations give me a glimpse into the inevitable
[67.84 → 73.26] future what are you driving towards yeah one of the things that we're seeing is that in the past
[73.26 → 78.94] people had separate systems where they had like logs on servers written files they were maybe sending
[78.94 → 83.90] some metrics to Datadog or something like that or some other system they were monitoring for errors
[83.90 → 88.60] with some product maybe with century but more and more what we see is people want all of these
[88.60 → 95.62] sources of telemetry logically tied together somehow and that's really what we're pursuing at century now
[95.62 → 101.78] we have this concept of a trace ID which is kind of a key that ties together all the pieces of data
[101.78 → 107.34] that are associated with the user action so if user loads a web page we want to tie together all the
[107.34 → 113.36] server requests that happened any errors that happened any metrics that were collected and what that allows
[113.36 → 118.20] on the back end you don't just have to look at like three different graphs and sort of line them up in
[118.20 → 123.42] time, and you know try to draw your own conclusions you can actually like to analyze and slice and dice the
[123.42 → 128.34] data and say hey what did this metric look like for people with this operating system versus this metric
[128.34 → 133.32] looked like for people with this operating system and actually get into those details so this kind of
[133.32 → 140.80] idea of tying all the telemetry data together using this concept of a trace ID or basically some key
[140.80 → 147.54] I think is uh is a big win for developers trying to diagnose and debug real world systems and something
[147.54 → 153.14] that is uh we're kind of charge the path for that for everybody okay let's see you get there let's see you get
[153.14 → 159.40] there tomorrow yeah perfectly how will systems be different how will teams be different as a result yeah I mean I
[159.40 → 163.40] I guess again I just keep saying and maybe, but I think it kind of goes back to this
[163.40 → 168.84] debuggability experience when you are digging into an issue you know having a sort of richer data
[168.84 → 173.16] model that's you know your logs are structured they're sort of this hierarchical structure with
[173.16 → 177.82] spans and not only is it just the spans that are structured they're tied to errors they're tied to
[177.82 → 183.38] other things so when you have the data model that's kind of interconnected it opens up all different
[183.38 → 189.80] kinds of analysis that were just kind of either very manual before kind of guessing that maybe this
[189.80 → 194.94] log was you know happened at the same time as this other thing, or we're just impossible we get excited
[194.94 → 199.76] not only about the new kinds of issues that we can detect with that interconnected data model but also
[199.76 → 205.00] just for every issue that we do detect how easy it is to get to the bottom of it I love it okay so they
[205.00 → 210.82] mean it when they say code breaks fix it faster with century more than 100,000 growing teams use century to
[210.82 → 221.44] find problems fast, and you can to learn more at century dot Io that's s e n t r y dot Io and use our code
[221.44 → 228.36] change law get $100 off the team plan that's almost four months free for you to try out century once again
[228.36 → 230.38] century dot Io
[230.38 → 244.34] we are taking you back to the all things open hallway track one more time to talk with some friends new and old
[244.34 → 253.18] first up Alex kretschmar who you may remember from earlier this year when he was on the episode called self-hosted media server goodness
[253.18 → 261.88] well have you met jarred before no, no this is jarred well I've heard you many times yes and I've heard you many times
[261.88 → 270.94] oh yeah awesome yeah happy to meet you yeah mutual fans Alex runs is it self-hosted dot FM uh dot show
[270.94 → 278.20] dot show what happened to dot FM somebody else had it no you wanted a show I don't know I just feel
[278.20 → 283.66] figured that dot show was it's self-hosted show so self-hosted dot show seemed to be there it works
[283.66 → 288.76] okay I'm not I'm not a hater we have shipped it dot show we do, but that's because we could not get ship
[288.76 → 295.26] it dot FM yeah somebody owns that whoever you are give it up give it up it's ours somebody owns
[295.26 → 300.00] self-hosted dot com and I'd love to know who that is yeah that's probably expensive yeah that's a nice
[300.00 → 307.50] domain question for you is this could you do like similar to a commercial open source company forms around
[307.50 → 313.64] forms a company around open source could you form a company around the podcast like a service
[313.64 → 318.38] business around self-hosted yeah could you do that it's an interesting one because I think
[318.38 → 324.28] because you got the the the media what is it called again collection the media collection apps
[324.28 → 329.10] no that guide you have what was the name of the ultimate media server okay thank you
[329.10 → 333.08] it's an interesting one because you look at the routes people come into self-hosting through
[333.08 → 339.54] and it's its typically things like Plex and collecting media through nefarious means
[339.54 → 345.40] but I think these days there are a whole new subset of people coming in through home assistant and home
[345.40 → 350.72] automation yeah this mythical new Linux user that we talk about in the Linux world for years and years
[350.72 → 356.54] it's happening through those platforms because they enable things to run on like Raspberry Pi's
[356.54 → 361.68] that you couldn't do full fat windows right you just couldn't do it that way so like a gateway drug
[361.68 → 368.50] but one of the big appeals of self-hosting is yes data sovereignty is important, but it's free as in
[368.50 → 373.58] cost for a lot of people too so they can ditch subscriptions with a lot of these apps and so in
[373.58 → 378.78] terms of like a services company I've thought about it quite a bit, but you'd have to charge more than
[378.78 → 386.26] most commercial services standalone services for just one thing which is like a well I could go and do
[386.26 → 391.16] it for free on unpaid I can go do it for free on Linux or docker or like whatever, and it's tricky
[391.16 → 397.28] you know yeah yeah have you thought about writing a book or a guide to like to capitalize on your you know
[397.28 → 401.74] because you're putting a lot of information out there and the consolidation of information enables what
[401.74 → 407.60] value exchange what happens when value exchanges yeah money yeah it's a little education for you
[407.60 → 412.32] jarred thank you I do put a lot of stuff out on YouTube these days yeah on the tail scale
[412.32 → 417.58] channel also kHz systems self-hosted podcast perfect media server.com like it's all over
[417.58 → 424.90] but maybe i should write a book I'm just curious did you know that Alex started Linux server Io
[424.90 → 429.96] yes because I listened to your guy's episode right did you know I didn't know that before that
[429.96 → 434.26] it's proof you were listening then neither did i I mean I prepped for that show you found out on
[434.26 → 438.38] the show I discovered it on the show I think you thought I was making it up I was like I had to
[438.38 → 444.00] check this guy he's like no you don't I paginated back to like page one of the blog sure enough boom
[444.00 → 450.90] yeah sure enough right there so for me like a lot of this stuff started just by I was trying to compile
[450.90 → 455.56] a kernel to put PCI pass through in it because I was cheap I couldn't afford a second computer
[455.56 → 461.26] I could afford a GPU though so I threw that in my server my unpaid server did the pass through in
[461.26 → 464.74] there and I'm like everyone else needs to know how to do this because this is awesome so I started
[464.74 → 469.80] writing blogs about it and yeah sharing information and that's how it's how many times have we heard
[469.80 → 476.92] something like that story in a different space is the beginning for so many people it's
[476.92 → 482.30] really rinse and repeat in your little niche and there's like not guaranteed success but if you do
[482.30 → 486.38] it longs enough I mean you're going to bring so much value to so many people I hope so I mean
[486.38 → 491.94] sometimes I wonder who's actually listening after a while sure because I feel like I mean for me the
[491.94 → 497.40] message has been the same for as eight years now but there's always new people coming in and want to
[497.40 → 504.98] hear new stuff so yeah well you might become jaded, but your audience might not even like it's not so
[504.98 → 510.52] much jaded because I mean I still get a lot of utility out of it myself like i I run home assistant at
[510.52 → 516.16] home I run Jellyfin I've promo like everything that I can self-host pretty much is self-hosted
[516.16 → 520.62] and tail scale obviously helps with that because I don't need to open ports in my firewall and all
[520.62 → 525.76] that kind of stuff but I mean from my perspective it's its weird to see my episode
[525.76 → 532.96] your episode's right there did you plant that no we sure did that's random we have a TV to uh Alex's
[532.96 → 539.18] left my right, and we have clips playing there for the audience and there's Alex and me talking about
[539.18 → 545.36] jellyfish great lighting too yeah very nice well you were actually shooting a log right and then you
[545.36 → 550.16] changed yeah yeah I actually figured out after our episode how to get my ninja five to output
[550.16 → 555.94] the log profile straight out of HDMI into obs so yeah now it's fixed but for that episode that was
[555.94 → 561.62] it's good lighting for sure yeah what's got your interest these days whether it's
[561.62 → 568.30] tail scale or personal like what's got your attention Linux nix os yeah oh like the
[568.30 → 574.76] man the package manager or the actual operating system yes, yes yeah because it's really so nix is
[574.76 → 579.56] talking about the language and the package manager and the OS as you say yeah it completes but i
[579.56 → 584.30] started managing all my macBooks using nix Darwin and then trying to build a single flake that can
[584.30 → 589.72] configure all my different Mac systems using home manager and then I've started trying to get
[589.72 → 595.94] involved in neo vim as well and mechanical keyboard like I'm going down the rabbit hole pretty hard of
[595.94 → 602.92] being like a chicken jet no factor also that's been that's been that came out this week and that's
[602.92 → 608.72] been a big time sink okay Victoria metrics factor oh factories oh that's the game right
[608.72 → 614.64] yeah like a some sort of builder game yeah I haven't played it so I'm I'm literally ignorant
[614.64 → 618.76] right here I'm like telling you how much I know about it, you play like a thousand hours in this game
[618.76 → 624.30] okay I don't play video games but that one what's different about that one it's basically software
[624.30 → 629.62] development but in game form okay like inputs outputs API interfaces all that kind of stuff so Chris
[629.62 → 634.82] killer on JS party is big into that game yeah, and he was trying to tell me that about it and I was
[634.82 → 639.54] like I don't want to try playing that because I'll probably never stop it kind of feels like work
[639.54 → 645.78] sometimes I'm not gonna lie like a grind are you grinding no in just so much as the fact it's exactly
[645.78 → 652.20] like software development wow like I am building this entity, and it's got to interface with these other
[652.20 → 657.70] entities and like before you realize it you've built basically a modular piece of code that you can reuse
[657.70 → 662.16] different, and then you spend most of your time refactoring the base to make it more efficient and
[662.16 → 667.58] the analogies to writing code are very strong okay very strong and the joy I guess would be similar
[667.58 → 675.66] joys the joy is there's no boss there's no but there is this kind of guilty pleasure in it of
[675.66 → 681.22] I must be productive I don't know if you guys feel that too but like I feel like I'm wasting my time
[681.22 → 686.50] playing video games and yet sometimes I just need to right whereas the rest of the time I'm busy making
[686.50 → 692.08] content probably like you guys like thinking on it in the shower and just you know right the grind
[692.08 → 698.22] never stops in that regard yeah for sure yeah I use video games now as like a decompression from work
[698.22 → 704.28] you know 45 minutes to an hour after I'm done working yeah put everything else away and just play
[704.28 → 710.58] for an hour and then I can be done and move on have you played geometry dash yet oh yeah I played
[710.58 → 716.20] geometry dash way back in the day I mean like I've moved on from it because I was kind of addicted
[716.20 → 721.54] to it do you ever move on from it well maybe not I mean it changes you yeah but yeah I love geometry
[721.54 → 726.10] dash I just don't play it anymore my son got me into it because he's got into it great music too
[726.10 → 732.14] yeah, and he loves he's he wants to be a DJ we should give BMC some geometry dash just side note
[732.14 → 737.58] yeah I remember the first time I got heavily into transport tycoon I was about 14 or 15 yeah
[737.58 → 743.08] it was open TTD when that started we took a holiday very much lived in England at the time
[743.08 → 747.98] in case you couldn't guess yeah we took a holiday in Florida and Orlando you've got all those
[747.98 → 754.08] interchanges flying around and I'm like looking at designs thinking I could implement this in the game
[754.08 → 762.64] yeah I got big into roller coaster tycoon and sim city oh yeah after that i kind of moved away from
[762.64 → 769.12] builders myself yeah, but now it's rocket league my kids like rocket league and now I like it and so
[769.12 → 774.84] we play it together which is a great co-op can relate I'm a somewhat of a bluey fanboy these days
[774.84 → 780.78] myself yeah there you go so you're talking about things you try to self-host everything you can
[780.78 → 789.14] what services do you not self-host and why great question my password manager I pay Bitwarden the ten
[789.14 → 796.64] dollars a year to host that because if I get locked out of my vault I can't get back into anything
[796.64 → 802.22] to unlock the vaults, and it's like this catch 22 yeah, and so I'd much rather pay Bitwarden it's
[802.22 → 806.62] because it's only ten dollars a year or twelve dollars or something for them to do it, and it's
[806.62 → 814.40] like that trade-off is worth it for me, I still pay for Google photos as well for right now at least
[814.40 → 820.22] but image is coming up real good which is like a self-hosted Google photos clone it's got things
[820.22 → 824.32] like machine learning face detection and duplicate detection and all that kind of stuff in
[824.32 → 832.12] it too it uses it needs a good GPU to do that so like it's properly doing Cuba library stuff oh wow
[832.12 → 835.98] but yeah I think really password managers is the only one where I'm like
[835.98 → 841.62] nah cloud even though you could Bitwarden you can totally self-host yeah yeah yeah you could
[841.62 → 847.36] absolutely well can't you just like literally host Bitwarden itself because it's open source
[847.36 → 854.46] well they're changing things are they Bitwarden yeah Bitwarden relicensed uh a SDK
[854.46 → 858.82] I thought I saw they reversed that though because they might have since this was like last week though
[858.82 → 863.22] so there's news since then yeah because they pushed there was pushback they got to the top of
[863.22 → 867.96] hacking news a couple of times yeah nobody wants that right so they reverse course that's cool I'm glad
[867.96 → 873.98] to hear that I recall years ago probably like at least two years ago I was standing up my own
[873.98 → 879.18] Bitwarden just to play yeah I wasn't I'm with you, i I don't know I want to host my own password
[879.18 → 886.50] manager because it's just it's too much of an I suppose if the tech is already you know secure
[886.50 → 890.70] I don't have to worry about it and like whoever gets access to you have to authenticate so if that's
[890.70 → 895.48] good to go whatever, but it's like if it's down and then I have to access from everywhere
[895.48 → 901.62] i I wasn't that good at poking holes in my firewall at the time you know so I was like nah I don't know
[901.62 → 907.88] if I want to do that what else would you not host you obviously host your data right like you, you host
[907.88 → 913.20] a ton of data, and you're cool with that next cloud is what I use to host something like Google Drive
[913.20 → 920.08] replacement Dropbox replacement are you happy with that mostly okay it's a big fat PHP app
[920.08 → 925.72] it's kind of slow it's kind of clunky it breaks a lot but i I have it now as a nix module and i
[925.72 → 930.32] just don't touch it now it's stable I just leave it alone it just does its thing in the corner
[930.32 → 938.24] yeah, but it's trying to be a platform for small to medium businesses I think it's like you can install
[938.24 → 946.40] office suites on it, you can install calendars contacts email file syncing there's a million
[946.40 → 951.04] different like add-ons you can get for it, and it's like once you start getting beyond the core product
[951.04 → 958.16] it starts to get pretty crufty pretty quickly really gotcha brittle I think would be the word
[958.16 → 963.70] brittle yeah photos is interesting because we've debated photos recently we did that's kind of a
[963.70 → 969.56] hard line of like the one thing you don't want to mess up right mainly my point is like know what
[969.56 → 973.30] you're getting into if you're going to self-host your own photos, and you're the arbiter of the
[973.30 → 979.56] final copy know what you're getting into yeah have a backup plan the only reason I trust myself to
[979.56 → 984.16] self-host photos is because I have an off-site server back in England that I replicate everything
[984.16 → 990.40] to that's right with ZFS every night, and it's done yeah exactly yeah does it snapshot too yeah
[990.40 → 996.92] ZFS is cool like that so like copy on write all that kind of stuff it will only sync the blocks that
[996.92 → 1003.16] have changed or the delta so yeah send receive is pretty cool but I recently got fibre as well so
[1003.16 → 1008.62] I've got like five gig uploads now which is wow I've gone from 30 Meg to 5 000 Meg, and it's like
[1008.62 → 1014.56] for you, I upload stuff to YouTube like every day nearly, and it's like amazing yeah that's awesome
[1014.56 → 1021.10] what's with tail scale these days what's new and fresh there is its you still uh what's the latest
[1021.10 → 1027.66] still developing relations with developers I guess yeah yeah uh it's pretty good we just had our
[1027.66 → 1032.54] company off-site in Mexico uh a whole company gets together once a year because we're fully remote
[1032.54 → 1038.54] so everybody looks at tail scale being like head office in Toronto, and they're like order a Canadian
[1038.54 → 1043.74] company in reality there's four people in a work in Toronto yeah and everyone else is just
[1043.74 → 1046.74] geographically spread like I'm here in Raleigh there's people in San Francisco
[1046.74 → 1053.24] all over the place yeah so there's a there's a lot of excitement at the moment in the company
[1053.24 → 1057.38] about where things are going over the next year or so we've made a bunch of new hires and new blood
[1057.38 → 1061.78] and stuff like that, and you know just changing the structure and growing into that next phase
[1061.78 → 1067.02] sounds fun I think it will be yeah I like tail scale still, yet you know I'm not a hater
[1067.02 → 1073.96] I'm a lover my use case is pretty simple though you know that's it how do you connect to your stuff
[1073.96 → 1080.52] it's at home from here uh just about tail scale exactly that's it right this is so easy like that's
[1080.52 → 1084.58] fine, and it is it on is it connected okay cool, and it's free for you because you're just one person
[1084.58 → 1091.64] right that's right and I love that and I do run an exit node at home on a dedicated VM I guess could
[1091.64 → 1096.30] you say a VM is dedicated it's not an Apple TV let's just say you know it's a yeah a VM that's
[1096.30 → 1101.74] dedicated to being that Ubuntu server is a VM, and it's meant to be the exit node that's it
[1101.74 → 1107.38] tail scale makes my life simple if it's kind of boring because it's so easy and that's kind of
[1107.38 → 1113.98] good right I often say it's wire guard on easy mode, and it sounds super cheese ball, but it's true right
[1113.98 → 1119.92] yeah I mean like once you're there's not really a lot of setup you do all the heavy lifting and it
[1119.92 → 1124.80] just blends in I don't have to think about it and worry about whether it is working or not
[1124.80 → 1130.88] working I remember the first time that I went to set tail scale up this is like probably three
[1130.88 → 1136.08] years ago before I worked there I set aside the whole weekend to retool my wire guard around
[1136.08 → 1140.90] tail scale and I was done in like 10 minutes and I'm like well i what am I going to do with my
[1140.90 → 1144.94] weekend I was expecting that to be really difficult, and it was yeah it's not hard at all it was just
[1144.94 → 1150.42] really easy tail scale is really easy dig it mans jarred doesn't tail scale though do you
[1150.42 → 1155.64] you don't need to right you have no need for tail scale what about if you need to control a mixer
[1155.64 → 1163.12] back in Texas from here don't do it jarred lives a simple life I do very simple it's not that he
[1163.12 → 1168.92] tries to not be complex he tries to be simple I do which is a different thing really and he
[1168.92 → 1172.42] feature though not a bug it is a feature yeah I've designed my life around it, I mean
[1172.42 → 1179.10] we are home bodies we are home schoolers I work from home I have one laptop I take it with me when I go
[1179.10 → 1185.40] somewhere I got nothing to connect to back home yeah I mean the Mac mini has some old movies on it
[1185.40 → 1189.60] but like I'm not going to watch those if I'm on the road I'm gonna watch whatever's on you're gonna
[1189.60 → 1195.42] watch the world go by the window yeah right exactly so young jarred would be all about tail scale
[1195.42 → 1201.64] but old jarred I'm just like I'm not a self-hosted yeah I still think it's cool tech I remember the
[1201.64 → 1207.94] battle days of Karachi VPN I think it was called which was I think open source, but it's definitely free
[1207.94 → 1214.74] is my closest analog to tail scale before tail scale, and it was cool because you could do a lot
[1214.74 → 1219.74] of the same stuff but it was that's pre-wire guard even I'm not sure how it worked I know it's
[1219.74 → 1225.28] a VPN, but you know we had Nazi in different people's houses right, and we were seeking we were
[1225.28 → 1229.94] like sharing backups with each other like I back up your stuff you back up mine I did all that stuff
[1229.94 → 1237.24] the hard way you know probably 15 years ago and so now just not interested now no yeah I just don't I
[1237.24 → 1241.22] just have different interests I like to talk about the stuff I like to hear what people are up to
[1241.22 → 1248.02] but I just don't have that that hacker mindset with that kind of stuff I just don't yeah I think for me
[1248.02 → 1254.14] it's when companies like Disney just jack the price up yeah to be double in the years space of a year or
[1254.14 → 1260.06] you're beholden to business models, and it's a trade-off that you're making of convenience versus
[1260.06 → 1267.60] time versus sovereignty of that data and information and stuff like that your choice is time and money
[1267.60 → 1275.58] right my choice is invested a lot of time and a lot of money in hardware yeah and then I also get the
[1275.58 → 1280.86] sovereignty of the data as well yeah i 100 understand that and I understand it would be
[1280.86 → 1285.18] cool to have a Plex library with like all the movies and all that kind of stuff that I own
[1285.18 → 1289.94] but my choice when Disney does that I just cancel Disney plus I'm like peace out guys
[1289.94 → 1294.28] I don't need you know yeah I'll live the simpler life it's gonna the kids are like where's
[1294.28 → 1301.54] bluey and then I tell them bluey's no longer with us bluey's no longer with us, you know so yeah I mean
[1301.54 → 1305.82] that's another trade-off right it's like okay now i have to deal with that situation yeah yeah you can't
[1305.82 → 1311.34] do that to all your to everything in your life but so you make choices yeah, but then you end up spending
[1311.34 → 1316.36] thousands on hardware and for me, it's also an educational piece too like the skills that I've
[1316.36 → 1320.72] learned through building my home lab have gotten me the jobs that I've had over the last decade
[1320.72 → 1327.56] and by staying true to my passions and just doing what I find interesting and talking about it that
[1327.56 → 1332.86] comes across in everything that i yeah all the content that I make and things like that and I think
[1332.86 → 1336.54] ultimately it makes for better content people can relate to you better and all that kind of stuff
[1336.54 → 1341.14] as opposed to scratching around for ideas for content the whole time it's like no this is what
[1341.14 → 1346.96] I'm doing anyway if I find it interesting probably at least a couple of other people will yeah I had
[1346.96 → 1353.58] the chance to and I still might actually uh do you know techno Tim by any chance Tim Stewart yeah so
[1353.58 → 1359.12] when he was on the pod a couple of times I was like dude you really need to like to spin off like and do a
[1359.12 → 1364.28] podcast that's adjacent from your news your YouTube channel because you're sort of like diving
[1364.28 → 1369.46] deep into certain things I think there's a room there for it and he and I were like skunk working
[1369.46 → 1375.20] the idea but then I felt like I was like Tim I don't know if I could be your co-host man I like
[1375.20 → 1379.96] the idea one I don't know if there's a time for it and then two I'm like i kind of feel like even
[1379.96 → 1384.20] though I'm a home lubber i kind of feel like I'm an imposter in a way because I'm not like
[1384.20 → 1389.98] every day every weekend every possible moment am I thinking about like tinkering in my home lab
[1389.98 → 1394.04] it's a problem and whereas Tim is you know where that's Tim's like that's his style I'm like
[1394.04 → 1399.24] i kind of even felt like imposter there I was like Tim I think I don't know if I could be your co-host
[1399.24 → 1402.68] man for this thing I like the idea of you doing it and I think he's spun up a couple other channels
[1402.68 → 1407.84] now that's like gone from his single channel to like giving him more freedom and I think he's
[1407.84 → 1415.92] kind of doing that now but I even feel like there are times I'm like I'm not even sure I am home lab
[1415.92 → 1420.18] enough for home lab and so like for you and your job and what you do with tail scale and other things
[1420.18 → 1425.68] like YouTube's a whole beast though and it's turned somewhat in I'm going to get on my soapbox for
[1425.68 → 1430.04] a second please do get on it it's its turned somewhat into a bit of a shopping channel where
[1430.04 → 1436.32] there are these guys like and I mean there's no disrespect to Tim to Jeff killing to craft
[1436.32 → 1442.32] computing to random to all these guys right those are four great channels they do a lot of really
[1442.32 → 1448.18] good stuff but they've got to pay the bills, and so they take a lot of sponsored videos and a
[1448.18 → 1453.32] lot of hardware and woodworking YouTube suffers from the exact same problem totally where you think
[1453.32 → 1457.92] I need this massive garage what's the latest planer right you know who's the wall what's the
[1457.92 → 1462.66] watch leper now full of a bandsaw and a jointer and like to right the reality is a track saw and a
[1462.66 → 1466.64] table saw and a couple of sanders, and you can get most things done with that yeah and the same is
[1466.64 → 1470.38] true in home lab you don't need to be home lab enough to be home lab like well I feel like it's
[1470.38 → 1476.46] even gone beyond home lab it's like well now it's literally a data centre in your home lab right and
[1476.46 → 1482.24] it's almost and I'm not hating either I love Tim and Jeff and all those guys negative it's just
[1482.24 → 1487.20] precisely I think it's its the nature of the content beast in a way where there's not there's
[1487.20 → 1492.74] not good enough you almost have to like almost give it your soul or feel compelled to and I'm not
[1492.74 → 1497.98] going to do that like a 30 000 view video gets you a hundred dollars I can't pay my bills with that
[1497.98 → 1503.06] right you know just get more views is the answer but there are only so many home lab views around
[1503.06 → 1507.30] and you see these big guys, and they're getting one two three hundred thousand maybe
[1507.30 → 1512.50] so let's just take the 30k and extrapolate to it right it's a thousand dollars for one video that
[1512.50 → 1518.52] does really well I'm doing four of those a month that's still pretty tight if you've got a mortgage
[1518.52 → 1523.42] and a kid's to pay for and like so you have to take these third-party deals and sponsorships and
[1523.42 → 1528.06] I know you're not immune to that in the podcasting yeah world as well and yeah it's trying to strike
[1528.06 → 1533.34] that balance between finding sponsors people find interesting versus, and we have this on self-hosted
[1533.34 → 1540.32] too like it's its just at what point does a hobby become a business, and it's easy to turn a hobby into
[1540.32 → 1545.78] a business and then learn to hate it because you're doing it all day every day like I was a classically
[1545.78 → 1551.78] trained musician I hate music now because it's just too I love listening to it but I don't play
[1551.78 → 1561.54] anymore because it was too competitive too real too yeah too much yeah it does it demand something
[1561.54 → 1569.88] from you and I think that's uh that's what separates those who go beyond all that and in quotes make it
[1569.88 → 1576.88] and those who don't, and it's not the ability it's the desire to go through the slog of what's required
[1576.88 → 1582.64] to get the greatness right perceive greatness not literally greatness because it takes a lot out of
[1582.64 → 1589.04] you to produce a podcast for 15 years or to do all the things you've done like it's it takes a lot
[1589.04 → 1594.72] and I don't think people realize the content grind of i mentioned the shower earlier like I'm thinking
[1594.72 → 1599.02] about how I'm making a tail scale YouTube video today I'm in the shower thinking about how I present
[1599.02 → 1603.96] that idea how I make it interesting who's watching what do they find interesting like trying to
[1603.96 → 1610.08] trying to second guess every little detail that you can, it's a lifestyle it's not a job it's its a
[1610.08 → 1615.44] lot to be good at it, I think it's a lifestyle precisely I hadn't appreciated that before taking
[1615.44 → 1620.08] this derail job at tail scales and like going full-time you know it is it a lifestyle that is
[1620.08 → 1627.52] worth living I think so I mean if it's sustainably so if you tell 15-year-old Alex he would get paid a
[1627.52 → 1634.92] salary to make tech videos I think he'd be pretty happy yeah I dig it mans so I was wrong it's not a
[1634.92 → 1643.00] dot FM it's self-hosted dot show and I think one of the things you talked about recently was uh
[1643.00 → 1650.16] no google November is that right or no google October no Goober yeah no goober okay so we've
[1650.16 → 1654.96] been looking at a bunch of stuff self-hosted search right there's an app called searching its
[1654.96 → 1662.38] spelt sear like you sear a steak and then CNG okay it creates an anonymous Google search profile for
[1662.38 → 1668.30] every query you make so there's no tracking cookies I mean they know you rip address that's originating
[1668.30 → 1674.86] from but beyond that it's a d it's a brand-new empty search profile every single time there are no ads
[1674.86 → 1680.40] there's no tracking there's no spyware like all of that stuff, and it presents the results do you
[1680.40 → 1684.60] remember how google used to look 10 years ago yeah, and now it's got this AI nonsense at the top and
[1684.60 → 1689.70] pictures and I've trained myself to scroll to about a third of the way down the page before anything
[1689.70 → 1696.02] interesting actually happens with searching it's right there at the top every time, and it can self
[1696.02 → 1701.24] host it and I connect to my instance through tail scale of course running in my basement what I didn't
[1701.24 → 1706.64] expect though was to start looking at other things like AI search like perplexity have you come across
[1706.64 → 1712.96] perplexity yet a little bit yeah amazing google must be quaking in their boots because you can self-host
[1712.96 → 1719.50] perplexity with something called perplexing, and then you can use searching to perplexity goes out
[1719.50 → 1724.74] to the internet and does those searches on real content because chat TPT is based on two years ago
[1724.74 → 1730.04] right the data they scraped two years ago it'll say sorry I have no record before October 2022 or
[1730.04 → 1736.08] whatever whereas perplexity is searching YouTube videos constantly right now yeah, and it's summarizing
[1736.08 → 1741.74] videos from like right now so you're like real time that's dope is the AMD 9950x the best CPU right now and
[1741.74 → 1747.00] it will go out, and it will transcribe a bunch of videos figure out the answer and kind of and then
[1747.00 → 1752.98] you can ask it questions and Google's done in my opinion and until like a proper chat style comes out
[1752.98 → 1760.48] like perplexity is so good and so you're self-hosting perplexity is that right perplexing yeah perplexing
[1760.48 → 1765.20] it's perplexing isn't quite ready for prime time it crashes quite a bit at the minute
[1765.20 → 1771.16] and you need a GPU to do the machine learning like the AI like oh because it plugs into Obama
[1771.16 → 1775.58] is there it plugs into Obama underneath to do the could you run it on like a m4 mac or something like
[1775.58 → 1781.28] that yeah so maybe uh anywhere Obama will run you can throw like a Mac mini on your network and just
[1781.28 → 1787.90] let that be the workhorse couple of docker containers Obama, and you're good to go dope that's uh a couple
[1787.90 → 1794.40] down in your most recent episodes so self-hosted. Show full length go deep I'm sure right you
[1794.40 → 1799.88] and your Chris is your co-host yeah so you guys go deep on that what else you got jarred anything else
[1799.88 → 1806.68] I'm just now realizing that I've been without Google for a long time but I've just been suffering with
[1806.68 → 1811.64] duck.go, and it's like I should just replace that with perplexity and I won't be suffering it I've just
[1811.64 → 1818.42] I've just lived without and I've learned how to use dot go to the best of its abilities example I was
[1818.42 → 1824.08] doing some messing about for my talk here and I wanted to know the file path that the nginx docker
[1824.08 → 1830.74] uses for its default volume mapping and I literally said perplexity what is the default docker nginx
[1830.74 → 1838.28] mapping for the HTML directory it came back with the slash user slash share whatever boom right there i
[1838.28 → 1843.18] didn't have to go to look at the actual docker hub page nothing it was like right there, and it was
[1843.18 → 1850.48] so non-self-hosted what's their what's their model what's their business perplexity you can that you
[1850.48 → 1855.76] get a certain amount of searches for free, and then you can pay 20 bucks a month for pro searches whatever
[1855.76 → 1863.96] that means okay I haven't looked at that cool so are you said it perplexing yeah is not ready for
[1863.96 → 1868.60] usage it's necessarily mine's been unstable I mean I don't know if that's just an Alex problem or what
[1868.60 → 1874.88] but right what are you writing on uh an epic 48 core thing with like and it should be how much it's not
[1874.88 → 1879.74] a hardware problem it could just be a problem yeah yeah it could just be that revision has an I don't
[1879.74 → 1885.42] know that'd be dope I would that's cool I mean to especially if you're on the LAN I suppose you can
[1885.42 → 1891.70] always expose that via a tail scale URL yeah, thank you very much tail scale to be able to match your own
[1891.70 → 1899.92] search that's self-hosted I can get down with that I mean we've given so much to google so much
[1899.92 → 1905.16] it's time to take it back it's time to like just stop giving it all back you're not going to get it
[1905.16 → 1908.70] back, but you can stop giving it to him at least I can hear tom morello warming up somewhere over
[1908.70 → 1913.94] there you know there you go good reference I was trying to go for a goodies reference, but it was
[1913.94 → 1920.74] probably too deep of a cut do it I want to hear it he's like those dreams up there those are other
[1920.74 → 1926.46] people's dreams he's like down here these are our dreams and I'm taking them back I'm taking them
[1926.46 → 1936.20] all back I remember that yes, but you know what this one right here this was my dream my wish
[1936.20 → 1943.32] and it didn't come true so I'm taking it back taking them all back that was my that was good
[1943.32 → 1950.04] that was Sean Austin we love you man yeah all right well thanks Alex yep thank you thanks man
[1950.04 → 1957.92] what's up friends I'm hearing the breaks with kyle barberry co-founder and CTO over at coder.com
[1957.92 → 1963.90] coder is an open source cloud development environment a CDE you can host this in your
[1963.90 → 1970.08] cloud or on premise, so kyle walk me through the process a CDE lets developers put their development
[1970.08 → 1974.22] environment in the cloud walk me through the process they get an invitation from their platform
[1974.22 → 1980.48] team to join their coder instance they have to sign in set up their keys set up their code editor
[1980.48 → 1986.46] how's it work step one for them, we try to make it remarkably easy for the dev we never gate any
[1986.46 → 1991.98] features ever for the developer they'll click that link that their platform team sends out they'll sign
[1991.98 → 1997.42] in with OIDC or google, and they'll really just press one button to create a development environment
[1997.42 → 2003.38] now that might provision like a Kubernetes pod or an AWS VM you know we'll show the user what's
[2003.38 → 2007.36] provisioned, but they don't really have to care from that point you'll see a couple buttons appear
[2007.36 → 2012.28] to open the editors that you're used to liking VS Code desktop, or you know VS Code through the web
[2012.28 → 2017.68] or you can install our CLI through our CLI you really just log into coder, and we take care of
[2017.68 → 2022.30] everything for you when you ssh into a workspace you don't have to worry about keys it really just kind
[2022.30 → 2026.24] of like beautifully magically works in the background for you and connects you to your workspace
[2026.24 → 2030.90] we actually connect peer-to-peer as well you know if the coder server goes down for a second because
[2030.90 → 2033.90] of an upgrade you don't have to worry about disconnects, and we always get you the lowest
[2033.90 → 2039.14] latency possible one of our core values is we'll never be slower than ssh period full stop and so
[2039.14 → 2043.18] we connect you peer-to-peer directly to the workspace so it feels just as native as it possibly could
[2043.18 → 2048.84] very cool thank you kyle well friends it might be time to consider a cloud development environment
[2048.84 → 2055.56] a CDE and open source is awesome and coder is fully open source you can go to coder.com right
[2055.56 → 2063.44] now install coder open source start a premium trial or get a demo for me my first step I installed it on
[2063.44 → 2070.28] my Dropbox box and play with if it was so cool I loved it again coder.com that's c-o-d-e-r.com
[2070.28 → 2076.34] and also by our friends over at eight sleep check them out eight sleep.com I love my eight sleep I've
[2076.34 → 2083.12] never slept better, and you know I love biohacking I love sleep science and this is all about sleep
[2083.12 → 2090.30] science mixed with AI to keep you at your best while you sleep this technology is pushing the
[2090.30 → 2094.92] boundaries of what's possible in our bedrooms let me tell you about eight sleep and their cutting edge
[2094.92 → 2102.78] pod for ultra so what exactly is the pod imagine a high-tech mattress cover that you can easily add
[2102.78 → 2110.76] to any bed, but this isn't just any cover it's packed with sensors heating and cooling elements and
[2110.76 → 2117.56] it's all controlled by sophisticated AI algorithms it's like having a sleep lab a smart thermostat and
[2117.56 → 2124.00] a personal sleep coach all rolled into one single device and the pod uses a network of sensors to track
[2124.00 → 2131.44] a wide array of biometrics while you sleep it tracks sleep stages heart rate variability respiratory rate
[2131.44 → 2137.30] temperature and more and the really cool part is this it does all this without you having to wear
[2137.30 → 2144.16] any devices the accuracy of this thing rivals what you would get in a professional sleep lab now let me
[2144.16 → 2149.46] tell you about my personal favourite thing autopilot recap every day my eight sleep tells me what my
[2149.46 → 2153.90] autopilot did for me to help me sleep better at night here's what it said last night last
[2153.90 → 2161.22] night autopilot made adjustments to boost your REM sleep by 62 percent wow 62 percent that means that
[2161.22 → 2169.44] it updated and changed my temperature to cool to warm and helped me fine tune exactly where I wanted to be
[2169.44 → 2175.90] with precision temperature control to get to that maximum REM sleep and sleep is the most important
[2175.90 → 2181.12] function we do every single day as you can probably tell I'm a massive fan of my eight sleep and I think you
[2181.12 → 2187.56] should get one so go to eight sleep.com slash changelog and use our code changelog, and you'll get
[2187.56 → 2195.46] 350 off your very own pod for ultra you can try it free for 30 days but I am confident I sleep on this
[2195.46 → 2201.52] thing every night I'm confident you will not want to return it trust me once you experience this AI
[2201.52 → 2207.70] optimized sleep you'll wonder how you ever slept without it how do I know because that's exactly how I feel
[2207.70 → 2213.22] they're currently shipping to the U.S. Canada United Kingdom Europe and Australia once again
[2213.22 → 2221.08] eightsleep.com slash changelog and use our code changelog and get 350 off your very own pod for ultra
[2221.08 → 2233.40] next up we are joined by IRA taxa a senior software engineer with over 12 years of experience
[2233.40 → 2239.02] IRA is as legit as they come, yet she still struggles with self-confidence sound familiar
[2239.02 → 2244.00] we kind of hounded her to get her on the mic I even felt bad for a minute, but it all worked out
[2244.00 → 2248.68] in the end because she decided to do it, and we had a great conversation here it is
[2248.68 → 2258.32] IRA IRA IRA yes here we go how close do I have to be is that good depends on how loud you're going to be
[2258.32 → 2267.64] you're golden you're golden sweet so we asked you to come on the show yesterday morning yeah now it's
[2267.64 → 2273.56] this afternoon, but you made it I did I almost didn't make it you're stepping outside your comfort
[2273.56 → 2280.30] zone I am do you find that hard to do it is but I gave my first conference talk this year, and it was
[2280.30 → 2285.88] because somebody pushed me to do it and so if I don't start to take more of those chances myself
[2285.88 → 2290.32] yeah I'll never step out of my comfort zone and I can't rely on other people pushing me to do
[2290.32 → 2295.38] something right uh until I do it myself we kind of pushed you into this one didn't we yeah well a
[2295.38 → 2300.00] gentle nudge is what I like to call it we gave her a nudge yeah we didn't require it of her but we
[2300.00 → 2304.70] constant gentle pressure we just wanted her to come on the show so we're happy to have you first time
[2304.70 → 2312.36] at all things open it is impressions it's great i every day I walk through and I find more booths
[2312.36 → 2317.76] and more floors lots of booths yeah yeah it's a lot bigger than I thought it was going to be
[2317.76 → 2324.22] I'm used to more smaller conferences capped at a thousand people so it can be a little bit
[2324.22 → 2329.24] intimidating but I think going to more conferences made me a little bit more comfortable uh speaking
[2329.24 → 2334.58] to people kind of whether at the booths or at the hallway track just kind of finding people that you
[2334.58 → 2340.12] have things in common with whether you went to the same sessions or just at lunch yeah yeah
[2340.12 → 2345.92] we're hallway trackers ourselves aren't we Adam that's right yeah it's where all the fun is
[2345.92 → 2351.28] it's where we belong you know it is where the people are yeah I've had more conversations with
[2351.28 → 2356.48] people than I have been to sessions yeah and i I think I like that a lot better because you can find
[2356.48 → 2361.78] a lot of the content online whether it's on YouTube or a blog yeah or things like that but the thing that
[2361.78 → 2367.90] I miss most is that interaction with people because I do work remote yeah, and so I go to conferences
[2367.90 → 2374.28] for those connections for those interactions and not really for the sessions right what if we just
[2374.28 → 2380.96] had a conference that was only the hallway track that would be incredible hallway I would go to that
[2380.96 → 2388.06] that's right yeah coming to a hallway near you yeah don't go in there there are no talks
[2388.06 → 2393.12] the nice thing about that is you don't really even need a place to gather you just need a hallway
[2393.12 → 2398.10] yeah like we don't need an auditorium would you have vendors and stuff too it'd be like this
[2398.10 → 2402.34] everything would be in the hallway, but it would get pretty crowded though yeah you would need a pretty
[2402.34 → 2409.36] big hallway would there be a revolt attempting to organize which would be cool would be to put it in
[2409.36 → 2415.28] like an arena but just in the hall you know in the hallway of the arena the circular yeah and so
[2415.28 → 2421.24] you would just walk in circles you call it circles figure eight yeah well that's not how they're
[2421.24 → 2427.58] designed oh you want to cut through the middle just think out loud you know cool shape this is
[2427.58 → 2431.66] what we do welcome to the podcast yeah we think out loud yeah what do you think would you go to
[2431.66 → 2437.90] that conference I would if we just made you walk in a square circle or a figure eight circles or
[2437.90 → 2443.22] kind of like a speed networking kind of thing yeah yeah what would attract you to that
[2443.22 → 2448.80] conference the hallway because you come here for the people that come here to hang out in the
[2448.80 → 2453.98] hallway yeah I think it's a hard sell like especially if you have like the company paying
[2453.98 → 2459.24] for if it's hard to sell your employer on I'm just going to go talk to a bunch of people
[2459.24 → 2465.38] like where's the business value in that is what a lot of them would probably have a little apprehension
[2465.38 → 2472.32] with right, but it's its kind of like a meetup just on a larger scale yeah yeah or like an Union
[2472.32 → 2478.80] you know like base camp style base camp bar camp food camp no not food camp bar camp bar
[2478.80 → 2485.26] camp was a response to food camp you know food camp I don't you know bar camp no okay so food camp
[2485.26 → 2492.86] stood for friends of o'Reilly okay and that's Tim o'Reilly Tim o'Reilly the creator of the o'Reilly
[2492.86 → 2502.74] yeah empire media empire, and he had an event that was I think on his property or somewhere near where
[2502.74 → 2510.20] he lives it was very exclusive invite only you had to be a friend of o'Reilly to go okay, and it was a
[2510.20 → 2516.70] camp food camp I think they camped out okay that part might be gray area, but the rest is true at least
[2516.70 → 2521.76] and cool for everybody who gets invited but not cool for anybody who doesn't get invited right
[2521.76 → 2530.20] so bar camp was a response to food camp because food bar right and so bar camp became a conference
[2530.20 → 2537.14] where anybody can come you don't have to be a friend of o'Reilly you can be anybody and because
[2537.14 → 2543.34] it was an conference there was no pre-planned schedule so you show up on a Saturday morning
[2543.34 → 2548.74] for instance right everybody gets together and there are whiteboards or even just construction
[2548.74 → 2553.70] paper and there's a schedule like here's slots yeah, and you just show up a lot like lightning
[2553.70 → 2558.84] talks you just show up and like sign up for a slot yeah, and then you just have your you're putting
[2558.84 → 2565.34] together the conference as it's going yep they actually did that they did that on uh Sunday at all
[2565.34 → 2570.22] things open oh yeah that first day there were two uh tracks there was the community track and then
[2570.22 → 2574.90] there was a diversity track and the community track was essentially um a bunch of people writing
[2574.90 → 2581.54] down talk ideas or session ideas, and they just get around in a room in a circle and kind of talk about
[2581.54 → 2587.34] that one topic yeah another uh that conference also does a similar concept that's right uh open spaces
[2587.34 → 2593.02] open spaces so we went to that conference yeah in Austin in January yeah were you at that one
[2593.02 → 2597.42] not in Austin but I went to Wisconsin one we wanted to go to Wisconsin we didn't quite make it
[2597.42 → 2604.44] yeah, but you did I did a space what was that called birds of a feather is it called spaces
[2604.44 → 2609.54] I don't know like there were tables it was called come to my table and hang out, and you would sign up
[2609.54 → 2614.20] the tables were lettered or numbered they were, and you would sign up what we're going to be talking
[2614.20 → 2619.86] about at this table and Adam you did home lab or something i did home lab and I did uh
[2619.86 → 2626.48] podcasting yep was that cool that was cool did you get a lot of people come to it
[2626.48 → 2633.36] describe a lot uh more or more oh yes a lot okay yeah it was good we had some good conversations
[2633.36 → 2639.82] about both home lab and podcasting I think a lot of people are probably interested in podcasting
[2639.82 → 2643.90] in some way shape or form yeah I did a perfect job of my placard though because like you
[2643.90 → 2649.06] could put it up on the board and I decorated it oh like I made it look flashy you know you think
[2649.06 → 2653.24] that's how you got such big numbers like more than four I think it was a great topic, but it was
[2653.24 → 2659.88] also like oh look at me yeah I was pea cocking you know I guess you have to do what you have to do yeah
[2659.88 → 2665.16] you know get your attention bro you know right get your attention so that's cool I like the idea of
[2665.16 → 2672.04] I like improvisation I like spontaneous things yep, and so I really have I've gone to a lot of bar
[2672.04 → 2675.76] camps over the years yeah it used to be a bar camp Omaha every year for a long time
[2675.76 → 2679.68] and they were just fun because you never know what to you're going to get right you don't know who
[2679.68 → 2684.28] you're getting me, or you're gonna talk about oh that's pretty Adam is showing her a picture I like
[2684.28 → 2690.96] that what he put on the that conference it was the main thing and I put a little sub talk
[2690.96 → 2698.60] it let me see it I'll describe it good it says all caps in blue across the top home lab exclamation
[2698.60 → 2705.84] mark that's it oh no I thought those are names I thought people signed up it also says now in kind of
[2705.84 → 2714.80] cloudy kind of mix match uh unified promo oh yeah it's a tag cloud plans ultimate
[2714.80 → 2716.00] Ubuntu
[2716.00 → 2725.16] Texas docker oh no true Nazi you're Texas can you read your handwriting leaves a lot to be desired
[2725.16 → 2730.82] Wi-Fi six pi hold now did you talk about all these yes so that's not even false advertising now the other
[2730.82 → 2737.38] one says podcast in all caps and then in lower caps because I think you probably forgot to put that
[2737.38 → 2746.94] in there exclamation mark Mike's software sales editing questions community clips gear that's good
[2746.94 → 2752.14] that's good advertising I like that because a lot of times you have like a topic, but you don't really
[2752.14 → 2757.36] know like what they're going to be talking about almost too open-ended it's too generic or I know about
[2757.36 → 2763.98] you know, or you want to something or other yeah switching ports and stuff yeah come on now
[2763.98 → 2770.76] yeah you know Wi-Fi six right it'll get you I don't know what that is seen, but you would want to
[2770.76 → 2778.00] you might show up and find out about Wi-Fi generally right yeah what is Wi-Fi uh wireless uh something
[2778.00 → 2784.50] yeah I think it stands for fidelity, but that's right but yeah wireless networks right and six is a good
[2784.50 → 2789.32] number and six is just better than five you know yeah it's the next version than four too it's here
[2789.32 → 2795.98] though right Wi-Fi six it's here many devices are Wi-Fi six enabled but not all of them yeah it's uh
[2795.98 → 2804.76] it's not faster it can do more concurrent bandwidth right than Wi-Fi five it's a wider pipe but not a
[2804.76 → 2811.60] faster pipe yeah cool interesting I learned something today if you were to command a space
[2811.60 → 2818.48] and advertise it did you do that at that conference did you start one I did not but I attended my first
[2818.48 → 2825.76] open space um this year which is surprising because like we've done open spaces at that conference for
[2825.76 → 2832.64] 11 12 years but I was always interested in the sessions and I didn't realize that the interesting
[2832.64 → 2838.60] conversations usually happen in those open spaces or in the hallway but I went to my first one this year
[2838.60 → 2847.16] and uh it was on meetups and how to get people to show up to meetups how to organize meetups because
[2847.16 → 2853.06] a lot of them have died down since covid a lot of them are pretty much gone so how do we bring those
[2853.06 → 2859.34] communities back how do we in a sense resurrect those meetups and get people more involved in those
[2859.34 → 2865.04] things yeah yeah that's cool so if you're going to start a space though like you're going to step outside
[2865.04 → 2871.74] your comfort zone and next year at that conference I'm gonna I'm going to run a space I would probably do
[2871.74 → 2878.96] it on React Native okay i I've been a React Native developer for two years now but I'm a solo dev for
[2878.96 → 2885.34] the most part and I don't know a lot of others in the community at least immediate community that do
[2885.34 → 2890.28] React Native development so it would just kind of be interesting to see if there are people doing
[2890.28 → 2895.02] mobile development what are they using if they're interested in React Native I could maybe talk about
[2895.02 → 2901.48] that a little bit yeah but yeah how do you keep up in the React Native world I listen to the React
[2901.48 → 2908.08] native radio podcast uh that's hosted by infinite red who is one of the leading uh consultancies um
[2908.08 → 2914.10] actually one of the biggest consultancies in the U.S. for React Native development I also read their
[2914.10 → 2919.76] newsletter they have a newsletter that they publish with some of the latest news I keep up with uh the
[2919.76 → 2926.84] React Native releases uh they just released 0.76 recently and then just kind of keeping up on Twitter
[2926.84 → 2933.02] just reading up on you know new libraries and framework frameworks with expo brand-new architecture
[2933.02 → 2939.60] right yeah yeah do you have a take on that by default I haven't used it yet, but it's supposed to be
[2939.60 → 2946.64] faster and then obviously the old architecture yeah, so there's a lot of push for React Native packages
[2946.64 → 2952.14] to switch to the new architecture because there are ones that are still not compatible with it
[2952.14 → 2956.48] so if you do switch your project to new architecture there might be some packages that
[2956.48 → 2962.18] kind of have issues with that I know there's a there's a big movement to get those packages
[2962.18 → 2973.12] compatible so yeah what else man anything else is it getable React Native like how do you level up and
[2973.12 → 2982.80] learn where do you get your new skills by doing it is getable but some of the like some of the stuff
[2982.80 → 2988.68] is a little bit older or like outdated right so you kind of have to keep up with documentation
[2988.68 → 2993.44] kind of have to try it out for yourself and play around with it but yeah that's kind of been one
[2993.44 → 2998.42] of my biggest struggles is where do I find those resources when I have questions yeah on how do i
[2998.42 → 3004.84] do this or this isn't quite working the way that I expect it to where do I go and so twitter infinite
[3004.84 → 3009.76] red also has a slack community of a lot of React Native developers so if you have questioned a lot of
[3009.76 → 3015.94] times you can go into their slack ask a question and somebody will be able to either answer or point you
[3015.94 → 3022.16] in the right direction to figure out where to go from there nice what are you doing you said learn
[3022.16 → 3030.76] by doing so what are you doing I'm building a React Native template so I am using React Native CLI
[3030.76 → 3042.54] to build a template with React Native hook form and God for forms and validation and integrating
[3042.54 → 3050.02] authentication with the idea that if I wanted to build a mobile app with React Native these are the
[3050.02 → 3055.94] things that just kind of come with it so I don't have to rebuild it from scratch, so these are things
[3055.94 → 3061.52] that I like to use or would make a development easier yeah and just kind of learning by doing so
[3061.52 → 3068.30] how does validation work with God and react hook form how does authentication work with auth zero how do
[3068.30 → 3072.88] you implement state management with all of these you know technologies and what's the best way to do
[3072.88 → 3078.98] it so it kind of helps me learn about the technologies that I'm using but also how to integrate them with
[3078.98 → 3085.80] other technologies and have something that I can then take and used to build a real world app awesome
[3085.80 → 3096.00] if you had a magic wand to change React Native an angst or just something you haven't learned quite
[3096.00 → 3101.26] as well as you'd like to yeah what would it be how would you change it debugging yeah
[3101.26 → 3107.88] so the problem there I think the tools that we have today aren't like the tools that we're used to in web development
[3107.88 → 3116.46] there is I know there's a debugger that's coming out with React Native 0.76 I heard about it in React Native
[3116.46 → 3122.32] universe or react universe I can't remember the name of that conference, but it was held in Poland
[3122.32 → 3128.98] earlier this year most of my logging and debugging in React Native is console logs and I'm sure a lot
[3128.98 → 3133.66] of people kind of do that yeah it's just not a lot of good tooling around debugging and React Native
[3133.66 → 3140.54] there is reaction it was also built by the folks at infinite red I haven't had a chance to try that out
[3140.54 → 3146.42] yet, but it's one of those things where if I could know more about debugging in React Native I'd probably try
[3146.42 → 3152.92] reaction uh try out the new debugger in 0.76 and kind of figure out how best to do that
[3152.92 → 3161.80] awesome dope good job thank you yeah, thanks for sharing you're a podcaster awesome you did it we did
[3161.80 → 3168.08] it we all did if it's done it's not as scary as I thought it was going to be told you yeah it's fun you
[3168.08 → 3173.96] just talk to each other what's up friends I'm here with a new friend of ours over at assembly AI
[3173.96 → 3181.10] founder and CEO Dylan fox assembly AI is where you can turn voice data into insights chapters
[3181.10 → 3188.52] transcripts summaries and so much more with their leading speech AI models so Dylan give me a glimpse
[3188.52 → 3194.42] into what you're doing with speech AI models at assembly AI so at assembly we're building industry
[3194.42 → 3200.68] leading speech AI models for various tasks like speech to text streaming speech to text speech
[3200.68 → 3206.28] understanding to help developers easily convert voice data whether it's live or pre-recorded into
[3206.28 → 3211.92] super accurate text and then to help developers extract a ton of information and metadata around
[3211.92 → 3216.90] voice data or even around the text that they just were able to convert from that audio data so these
[3216.90 → 3224.34] are things like picking out entities or PII that was spoken in voice files or summarizing
[3224.34 → 3231.12] voice and audio data down into custom summaries it's things like being able to detect how many
[3231.12 → 3236.08] speakers spoke and who said what and what the names of different speakers were so we bundle all those
[3236.08 → 3242.66] things into a super simple API with really great docs that developers can just sign up to for free
[3242.66 → 3248.40] to start use the API build into their apps and then build these really cool AI apps and products and
[3248.40 → 3253.92] workflows and automations on top of voice data with I dig it okay can you take me a little deeper
[3253.92 → 3258.94] into the opportunity for developers because it seems like there's a lot of voice data out there and
[3258.94 → 3264.80] there's a lot of trapped value in that voice data there's so much voice data being created on the
[3264.80 → 3272.74] internet now podcasts videos phone calls voice messages audiobooks virtual meetings it's crazy and
[3272.74 → 3278.56] you can now transform and understand all this voice and audio data in ways that were not even possible
[3278.56 → 3284.58] a year 18 months ago so what we're seeing with the help of these new AI models that we're creating
[3284.58 → 3290.64] at assembly developers and organizations are just racing to build all these new applications workflows
[3290.64 → 3296.40] automations that leverage the voice data they have either within their organization or within their
[3296.40 → 3301.68] product build really cool new products and services workflows that are just like taking off in the
[3301.68 → 3307.52] market so at assembly we're building the industry-leading models for all those different apps and workflows
[3307.52 → 3313.04] whether it's speech to text or speaker dimerization or speech understanding capabilities to summarize voice
[3313.04 → 3319.84] data or extract entities voice data or mask PII from phone calls for various types of automations that
[3319.84 → 3324.88] might be built, and we're exposing that through a super simple super scalable API that's just constantly
[3324.88 → 3330.24] being updated and constantly getting better, and so we're seeing a crazy amount of developers and
[3330.24 → 3336.48] companies just build really cool apps and services on top of our API every day uh it's really only just getting
[3336.48 → 3340.96] started especially with the model updates that we have planned over the second half of the year
[3340.96 → 3346.96] that are coming out they're really excited to launch to the developers on our API okay constantly updated
[3346.96 → 3353.76] speech AI models at your fingertips well at your API fingertips that is a good next step is to go to
[3353.76 → 3358.56] their playground you can test out their models for free right there in the browser, or you can get
[3358.56 → 3368.24] started with a 50 credit at assemblyai.com practical AI again that's assemblyai.com practical AI
[3373.28 → 3379.44] our final two conversations are with a husband and wife pair, but we speak to each of them separately
[3379.44 → 3383.92] because they had their son and daughter with them at the event which is awesome but means they had to
[3383.92 → 3391.36] take turns on kid duty first up Ravindra Fernando an independent software consultant after AVI we speak
[3391.36 → 3397.60] with his wife adit Ramachandra adit is an independent software consultant is there an echo in
[3397.60 → 3406.40] here now is there a power couple in here I think so well we're here with AVI Fernando Fernando Fernando
[3406.40 → 3413.36] we're here with I was about to call you Abby yeah I just changed the sound Abby I'm Abby now you all
[3413.36 → 3421.28] Abby Fernando that's right from kansas kansas city born and raised uh not born and raised
[3421.28 → 3426.72] born in Sri Lanka okay Sri Lanka how did you get to Kansas how did you get to Kansas are you the
[3426.72 → 3431.60] Missouri side or the Kansas side oh I live on the Kansas side okay yeah so I got here when I was 19.
[3431.60 → 3439.28] wanted to pursue a degree yeah so that's k you rock chalk jayhawk oh rock chalk yeah absolutely
[3439.28 → 3443.28] sorry we speak a different language here in the Midwest what did you say it louder I said rock
[3443.28 → 3450.00] chalk jayhawk yeah rock chalk that's their saying rock chalk jayhawk that's our chant yeah the k-u
[3450.00 → 3456.24] jayhawks uh jock motto they're the jayhawks the mascot that's rock jock jayhawk rock chalk jayhawk rock
[3456.24 → 3460.56] chalk jayhawk that's right yes you're saying it right that's what they all say to each other it's kind
[3460.56 → 3466.08] of like saying keep going temper phi you'll be chanting it yeah it's a chant give me a demonstration
[3466.08 → 3471.04] give me a demonstration rock chalk jayhawk
[3471.04 → 3478.08] yeah that's it I did not go to k-u all right but I've been there many a time
[3478.72 → 3486.24] and I know the chance because I live nearby um all right so you're 19 move from Sri Lanka to Kansas of
[3486.24 → 3492.96] all places that's right yeah and then you never go back no yeah yeah I stuck around in
[3492.96 → 3498.40] Lawrence uh finished my bachelor's in computer science nice and then decided right after like
[3498.40 → 3503.04] let me do a master's as well so I pursued my master's right afterwards and then stuck around
[3503.04 → 3510.08] in Kansas City yeah since yeah got married started a family started a business yes in that order eventually
[3510.08 → 3516.08] yeah eventually sure probably skipping over a lot of life there but so my wife and i we uh we met at
[3516.08 → 3522.00] Ku okay we were both teaching assistants so we started dating right around the time of
[3522.00 → 3527.68] graduation so we both started at corner which is a large healthcare it company okay in the
[3527.68 → 3533.28] Kansas City area on the same day wow so we've had we've had a great journey from the very beginning
[3533.28 → 3543.20] yeah yeah in lockstep yep that's good stuff yeah, and you are a React guy oh one of my
[3543.20 → 3547.60] specialties yes okay yeah what would you what's your list of specialties why don't you list our
[3547.60 → 3553.52] specialties for you uh mostly front end yeah I would say react Next.js uh do a lot of playwright tests
[3553.52 → 3561.04] cypress for my clients yeah yeah, and you are uh running your own business yeah since 2021
[3561.04 → 3567.36] how'd you get there great story so back when I was working at sonar you know I got to meet a lot
[3567.36 → 3573.44] of architects and senior engineers which I had learned a lot of knowledge from and then this journey goes
[3573.44 → 3580.24] along at one point I decided to join another big company at that point you know I started to feel
[3580.24 → 3584.80] like I was attending a lot of meetups locally because I wanted to spread the knowledge that I was gaining
[3584.80 → 3592.24] from the other people and I spoke to a couple of directors at RSA at the time, and then they were
[3592.24 → 3597.12] like yeah you bring the meetup in-house, and we'll let you host it we'll let you have people in it
[3597.12 → 3603.12] so it was awesome right so I was really motivated by all of that but then I realized like what I'm
[3603.12 → 3608.96] missing is you know I'm I'm seeing how big companies run right how they operate but let me see how the
[3608.96 → 3613.84] small companies run so I took the risk and I said okay let me just go join a startup right
[3613.84 → 3619.36] product startup so that was my journey into seeing how a product works yeah and from a startup
[3619.36 → 3624.72] level there was only like five people at the startup and everyone was wearing different hats sure getting
[3624.72 → 3632.32] started with it learned a ton there right constant innovation constantly like grinding uh great
[3632.32 → 3638.16] great time there what I was like thinking to myself at that time was okay now I got the product
[3638.16 → 3644.72] startup perspective what if how does services or consulting work right let me go experiment that
[3644.72 → 3651.68] so I joined a services' startup which their motto was consulting a couple of guys amazing dudes
[3652.40 → 3656.88] got to work with them see how they negotiate contracts you know bring in different contracts
[3657.44 → 3663.36] one of the contracts was so interesting to me, I was working on an app for someone that was his hobby he
[3663.36 → 3670.16] wanted this idea of a virtual bar so he was mapping out all the bars in the cities that they go to
[3670.16 → 3677.68] and would give the ability for someone to purchase a seat in the virtual world which is a fascinating
[3677.68 → 3682.56] idea I was like people pay for this stuff it's like yeah this is cool stuff right so I got really
[3682.56 → 3687.92] motivated by that and then eventually decided okay I'm just gonna I'm just going to start this journey on my
[3687.92 → 3695.84] own and see how things go so that's fast-forward to 2021 sure and I work with a client and at that
[3695.84 → 3701.60] point I decided okay the project's going really well and I think I can pull the plug on my full-time job
[3701.60 → 3707.44] and took that leap and never looked back gotcha so you were kind of a weekend warrior at that
[3707.44 → 3713.76] point yes you had a job yep nights and nights and weekends I was wondering because for a lot of people
[3713.76 → 3718.96] going into their own business yeah especially a services business like a consultancy the question
[3718.96 → 3726.80] is how do I get that flywheel going you know do I just quit my job and take the leap or do i
[3727.44 → 3732.24] weekend warrior it for a while so what did you have a plan from the start or was it just kind
[3732.24 → 3737.60] of like opportunistic yeah I think I jumped into the opportunity maybe in hindsight I probably jumped
[3737.60 → 3743.52] into early but again I have no regrets right uh if I were a good time man yeah absolutely right
[3743.52 → 3747.36] yeah there really isn't you can't tell that stuff it's like the market you can't tell the entrance
[3747.36 → 3753.28] into a stock oh yeah I mean you can but yeah it's hard right it's basically impossible yeah just get
[3753.28 → 3758.72] in yeah absolutely yeah the best time is now yeah oh yeah that's why you've been doing that for three
[3758.72 → 3766.48] years yes what's the hardest part is managing the different clients and keep the pipeline
[3766.48 → 3773.12] full all the time right so now wearing different hats not only consulting not only coding not only
[3773.12 → 3780.40] mentoring selling yeah closing that's invoicing collecting money contracts
[3780.40 → 3784.24] are tough too because you want to scrutinize those contracts are obviously like
[3784.24 → 3789.92] words of bond oh yeah so it's got to be clear yeah, and you don't want your client relationship to go
[3789.92 → 3794.32] haywire because yeah absolutely you did not word your contract well enough yeah there's always little
[3794.32 → 3798.96] details between each contract that changes yep and there are a lot of details in that process and
[3798.96 → 3803.36] finding the right people who actually write the check you know some companies it's the CTO who
[3803.36 → 3808.80] does that some companies it's not right the CTO still has to talk to the CFO or the senior engineer
[3808.80 → 3812.88] will have to go talk to someone else right so getting everyone on board time hunting down a check
[3813.92 → 3817.20] uh what's what's that do you have to spend a lot of time hunting down this check like
[3817.84 → 3821.84] once you've delivered your invoice is there sometimes like hey you know uh
[3821.84 → 3828.48] uh you all owe us the money the invoice said to pay us you know I've been fortunate so far okay so
[3828.48 → 3832.56] knock on wood you'll hit it yeah eventually especially larger I still haven't had to larger
[3832.56 → 3837.44] the org yeah the less they care yeah what's your TTP what's that mean I'm making this up right now
[3838.48 → 3846.72] time to payment yeah do you have like a 30 or sorry uh mostly net 30 uh right that's that's my standard
[3846.72 → 3853.68] uh but a couple of months too it's great it's good but that's I learned a new word today yeah i just
[3853.68 → 3859.60] paid up just now meantime to payment here's a here's a pro tip on your terms uh-huh take that
[3859.60 → 3864.96] net 30 and turn it into due upon receipt yep because if they're big enough they're not going to care
[3864.96 → 3868.56] anyway they're going to pay you when they want to yeah if they're small they'll take that net 30 very
[3868.56 → 3873.28] seriously, and they'll pay on the 30th day yeah so if you just change that to do upon receipt
[3873.28 → 3876.64] if they're serious they'll just pay you as fast as they can yeah, but the other ones will ignore
[3876.64 → 3881.28] you anyway so they're not going to pay attention to your net 30. yeah, it won't really matter that much
[3881.28 → 3885.44] but you might as well make try to get paid as fast as possible gotcha you know that's what I do with
[3885.44 → 3890.08] one of my clients, and they're perfect about yeah good about it yeah but yeah the larger ones
[3890.08 → 3895.92] you know it's like a whole like you're a vendor in a system and there's like some they don't even care
[3895.92 → 3900.24] what your net anything is it's like net whatever I want to pay you yeah if you're lucky the nice thing
[3900.24 → 3904.88] is though on the larger ones is once you get that deal set up, and you're in the system yes, and you're
[3904.88 → 3909.76] on those terms they will actually pay you reliably that's right as the smaller customers you know
[3909.76 → 3913.28] they might run out of money in the meantime or something yeah and just not have the money to pay
[3913.28 → 3919.04] you I certainly hit that as well with my time yeah it's interesting i I worked with a foreign client
[3919.04 → 3924.88] too and sometimes you have tax concerns too right you got to get the right documents before they can pay
[3924.88 → 3930.64] you so I had to go obtain uh tax certificates saying that I pay taxes in the United States
[3930.64 → 3934.56] really so that I don't get double taxed in the other country, so yeah there's a lot of
[3934.56 → 3938.40] hoops you have to jump through when you're when you actually customers are from outside the US
[3939.68 → 3945.68] so when I first started I thought to myself if I want to work 40 hours a week and I can bill x dollars
[3945.68 → 3953.28] per hour yeah you know I think it was like 75 when I started and I can get that 80 of the time
[3954.00 → 3958.88] then I'll make this much money does that dog hunt you now and then you look at that number
[3958.88 → 3963.68] and you're like yeah that that makes a lot of sense like I can live off of that what I didn't realize is
[3963.68 → 3969.84] is that working 40 hours a week if that's what you want to do which is what I wanted to do and billing
[3969.84 → 3974.80] anywhere close to 40 hours a week like those two things don't happen right no very rarely it's a dream
[3974.80 → 3982.40] yes so how many what's what percentage of your working hours are you billing is it 50 80 like
[3982.40 → 3987.44] what because you're a solo consultant right so you don't have any help on anything maybe some
[3987.44 → 3991.84] software doing some stuff that's right yeah but like everything that has to happen in your business
[3991.84 → 3995.92] you're doing it or software is doing it how much of your time are you billing on a weekly
[3995.92 → 4001.68] percentage wise don't need hours yeah I would say about 80 80 that's a good estimate, and you have a
[4001.68 → 4009.20] a large customer which helps yes absolutely yeah how many hours we do work about 35 to 40 right now
[4009.20 → 4016.40] what yeah nice yeah self-employed yes working 35 maybe 40 yeah which is pretty good
[4017.68 → 4023.52] what are you looking at me for well because i just I want a response yeah okay for me well I was telling
[4023.52 → 4029.44] jarred earlier that I do have capacity right I'm always constantly looking to keep right a couple of
[4029.44 → 4036.64] clients at the same time so I can agree to some more contracts and get those hours in, but you got
[4036.64 → 4042.80] an 80 20 rule on your customers like currently you have an 80 customer yeah and everything else yes, yes
[4042.80 → 4049.12] so that helps you get to that 80 billable yes if you had three smaller customers at the same time and
[4049.12 → 4054.40] no larger one yeah you would spend more of your time trying to fill that pipeline yeah yeah and if that
[4054.40 → 4059.92] 80 turns into zero now you're like flip-flopped, so there are risks on either side going like on a big
[4059.92 → 4064.00] hunt there's no perfect way to set it up yeah I think it depends on the year it depends on the month
[4064.00 → 4067.92] all of these formulas would change, and you're going to constantly keep adapting to right the newer
[4067.92 → 4074.32] newer world yeah I'm just surprised what are you surprised about that you only work 40 hours yeah
[4075.20 → 4079.76] not a lot of people do that yeah well there's a primary reason for that so we have a little one at home
[4079.76 → 4084.96] and i I deliberately want to spend as much as time with that's the way to do it heck yeah with
[4084.96 → 4089.44] the kids you know just because you have that principle doesn't mean you get to yeah always do
[4089.44 → 4094.96] it that's good for you that you do yeah because you know I'm I'm surprised not because I think you
[4094.96 → 4100.96] should but because you don't yes which is a good thing yeah, and you know you're talking to two people
[4100.96 → 4107.20] who power has their family yeah deeply you know is there a better way to say that deeply yeah it's
[4107.20 → 4112.80] just um I thought about it, you know massively bigly yeah yeah bigly is the right word bigly is
[4112.80 → 4117.84] the word yeah yeah I thought about it's like those years of my son and my daughter is like
[4117.84 → 4121.84] they're not coming back yeah the time once it's gone it's gone right it's the most valuable thing yeah
[4122.96 → 4128.40] and I have a bunch of them so the way I look at it is I got six kids and I look at it like every
[4128.40 → 4133.44] year I lose six years yeah you know because all six of them get one year older that's right so that's
[4133.44 → 4137.52] six years they've actually gained on a single year and so how precious is each one of those
[4137.52 → 4141.12] oh absolutely you know yeah once they're all adults those years won't matter quite as much but right
[4141.12 → 4147.20] now they're not coming back I'm about to start crying man yeah look at the three of us here it's
[4147.20 → 4152.48] hitting me hard although Bobby's got us beat because his kids are literally with him yes last year I had
[4152.48 → 4157.44] a son with me in the year before but yeah I consider bringing my son and I really wanted to bring him
[4157.44 → 4162.48] I was just thinking how old I'm just not sure eight he's a little young yeah yeah I think he
[4162.48 → 4168.64] needs like one more year before he can, I would not be able to concentrate yeah I think, and it's not his
[4168.64 → 4173.20] fault it's that i I want to you know I would actually probably want to experience it with him yeah so it'd be
[4173.20 → 4181.20] hard I would be distracted as a dad you know whereas you know otherwise I can totally focus yeah right
[4181.20 → 4186.16] you know yeah so we pick and choose, so this is the second conference so my wife she's speaking here too
[4186.16 → 4191.60] and she gave a keynote earlier so that's why everyone's here on us right now yeah he's flexing
[4191.60 → 4194.08] he did he literally flexed his body when he said that he's like
[4196.08 → 4200.88] he's flexing all right we get it you're cool and I continue no wife is cool oh you're both
[4200.88 → 4205.12] cool yeah that's right yeah you're both cool that is nice though okay he's cool by proxy okay
[4205.12 → 4208.72] that's what I'm trying to say hey the truth is we couldn't find a babysitter you're still in lockstep
[4208.72 → 4213.92] that's true they're still in lockstep yeah after all these years so you're doing the
[4213.92 → 4220.40] consultancy what does she do then uh she does uh very similar okay consult as well she does mobile
[4220.40 → 4225.52] so okay yeah that's that's her specialty as well all right so you're both kind of doing everything
[4225.52 → 4230.80] yes same now is one of you better than the other there are talks about merging the companies because
[4230.80 → 4236.96] we don't want to yeah we don't want to pay yeah same accountant yeah exactly you might as well minimize
[4236.96 → 4242.48] your costs we started at different times yeah and different specialties going forward yeah why
[4242.48 → 4247.60] let's merge yeah totally yeah even brand-new company name maybe even like I don't know what
[4247.60 → 4252.64] what's the company's names, so my company is ta proving consulting okay and hers is Syria consulting
[4253.20 → 4258.08] so we can hyphen it maybe the old hyphen we'll just sit down and talk about that one
[4259.84 → 4263.68] well she's not here to speak for herself so we need to decide right now before she gets here
[4263.68 → 4268.64] that's right yeah see if she agrees and if she do you both are eyewitnesses right yeah yeah we
[4268.64 → 4275.36] signed it in yeah exactly we're good that's good man I mean that's very cool power couple yeah it's
[4275.36 → 4282.08] a power couple right there man yeah so much potential and possibility yeah it's cool man good for you
[4282.08 → 4288.80] thank you yeah, and you get to have your kids with you too I mean what a what a blessing yeah oh yeah
[4288.80 → 4293.84] that's where it's at man yeah I'm hoping uh my daughter uh you know she came to my wife's talk
[4293.84 → 4300.40] she's inspired so hopefully you know she wants to be a speaker one day yeah yeah that's that's
[4300.40 → 4305.60] where dreams begin right there man that's right but uh jarred I mean i have to tell you six kids
[4306.48 → 4312.96] you're you're a power dad well for sure yeah my wife's pretty amazing too yeah or very smart
[4313.84 → 4318.00] you know I think it's a little bit of both yeah a little bit of both there's a fine line between a
[4318.00 → 4324.24] a crazy person and a wise person isn't there any twins in their nope okay all organic power dad
[4324.24 → 4329.84] that's right organic like it's a non-twin or twins are non-organic
[4331.68 → 4337.12] that's right yes well thanks for chatting with us obi it's fun oh absolutely yeah well thanks for
[4337.12 → 4338.64] having me it was a blast it was the best
[4341.44 → 4344.96] so what are these people these are people that have been on the show those are not you
[4344.96 → 4351.84] oh okay oh this is video oh we're not doing video here oh okay good we have a drone
[4354.64 → 4358.56] so this will be audio only but what did you have for breakfast uh is it started
[4359.20 → 4366.48] we're just sound checking yeah gotcha yeah I had uh scrambled eggs coffee you ate scrambled eggs
[4368.08 → 4373.76] and coffee yeah lots of coffee lots of coffee yeah very standard yep
[4373.76 → 4382.96] what did you have for breakfast I had two eggs over easy yeah no toast I had some hash browns
[4382.96 → 4390.56] yeah light fruit and one strawberry and one slice of orange wow yeah very detailed
[4390.56 → 4395.36] the breakfast of champions I remember it like it was just this morning usually my breakfast is just
[4395.36 → 4400.64] leftovers from my kids so yeah I know how that goes too yep leftovers huh uh-huh
[4400.64 → 4407.92] so you're you're a leader eat last kind of person sort of yeah yeah I have a couple kids and just
[4408.72 → 4411.84] look at them like waste all their food and then I know they're not going to finish it
[4411.84 → 4417.04] right and then I just eat off their plate muffin you didn't eat yep there's a half a bagel I wanted
[4418.00 → 4422.16] right yeah my daughter is good at loading up the plate, but she's not going to eat any of that so yeah
[4422.16 → 4427.76] for sure my mom used to do that constantly we call her like the garbage disposal because she would not
[4427.76 → 4432.96] let anything get thrown away yeah whatever was left over she's like just give it to me, she's never
[4432.96 → 4439.28] happy about it yeah she's like I'll eat that like my mom did the same I'm going to eat it now yeah like just
[4439.28 → 4444.16] we're not throwing anything away yeah which I appreciate that sentiment, but it's like well you're just
[4444.16 → 4449.36] taking in empty calories on our behalf mom yeah it's got pros and cons you don't want to overeat
[4449.36 → 4455.60] for sure yeah totally so we spoke with AVI got yesterday yeah, and so we got his side of the story
[4455.60 → 4457.76] okay uh let's hear the real story
[4460.48 → 4467.28] uh he told us that you guys met at Ku yeah, and you're still together seems like he's telling the
[4467.28 → 4474.24] truth yeah two kids yeah two businesses yeah and so you're you're doing very similar things yeah
[4474.24 → 4484.00] how did you get into it so I grew up in India and my dad had a small business he was buying and selling
[4484.00 → 4490.64] cleaning products to hospitals and local companies, and he's a very ambitious person but of course he
[4490.64 → 4495.52] didn't scale up to a large company or anything it was just two people my mom and dad, and he would
[4495.52 → 4501.04] always go meet these customers and uh basically it was more for the flexibility, and he loved being
[4501.04 → 4506.48] an entrepreneur so i just kind of grew up watching that and I knew that was a possibility and I knew
[4506.48 → 4511.68] that he didn't have a boss, but he had like many bosses always like after all these customers and all of
[4511.68 → 4518.16] that so I guess that's where I draw my inspiration from okay and so when you graduated from Ku uh-huh
[4518.16 → 4524.32] you had an engineering degree yeah so I did self I did computer science uh undergrad in India actually okay
[4524.32 → 4530.64] and then I came for my master's to Ku and right after that I was a good economy it was 2012 uh so
[4530.64 → 4536.80] I got a job right out of college moved to Kansas City went to a big corporation so yeah that's that's
[4536.80 → 4541.52] kind of how my journey began one step in front of the other huh uh-huh, and now you're doing mobile
[4541.52 → 4548.16] apps or something I did do that for a while uh but now I'm more into like the web apps as well okay so
[4548.16 → 4552.40] I was doing React Native for a long time once in a while I do get customers who do React Native
[4552.40 → 4557.68] um so I do both yeah yeah react and React Native and between you and your husband who's the better
[4557.68 → 4564.88] software engineer you had to go scan our code to find out okay yeah so she's not going to answer that
[4564.88 → 4571.76] one you know we try not to work together honestly on projects yeah it kind of we have similar you know
[4571.76 → 4578.32] we have similar personalities and uh we kind of take lead a lot so leaders it could be, but it could be
[4578.32 → 4583.44] conflicting so we try to have our own customers have our own clients once in a while we would like
[4583.44 → 4589.20] maybe review our code or something like that we talk about problems in our day-to-day work yeah but
[4589.20 → 4594.24] I don't think I've ever worked with him yeah I work with him in like conference talks and stuff we would
[4594.24 → 4599.76] sometimes give a workshop together but like actual coding and architecture work we don't we don't work
[4599.76 → 4604.32] together because you've tried, and it didn't work, or you never tried it I just think there's too much
[4604.32 → 4610.96] like we're too much other too much that's too much yeah we need that space yeah I think that sounds
[4610.96 → 4616.88] healthy what do you think Adam it's not bad yeah I don't disagree but I enjoy working with my wife so
[4616.88 → 4623.44] yeah yeah I can't, you might be missing out on something you didn't realize yeah I said to him, I said
[4623.44 → 4630.72] to AVI power couple, and he's like yeah yeah but separate you're not unified in the powering of the couple
[4630.72 → 4635.52] just in the end the business side obviously yeah I agree with you so what happened was I started out
[4635.52 → 4641.20] first while he was having a full-time job yeah and I didn't have any ideas of scaling or anything like
[4641.20 → 4645.60] that I just wanted out and wanted to be an entrepreneur but I didn't know what that really
[4645.60 → 4651.84] meant and at that time my goal was mostly I want to spend more time with my baby and I want to earn what
[4651.84 → 4657.04] I was earning in my full-time and that's that was my goal I didn't have like a large scale goal
[4657.04 → 4662.16] so I was like I need flexibility I want to spend time with the baby and I want to make as much as
[4662.16 → 4667.52] I made in my full-time job so I wasn't looking to like so I just needed a company yeah, and you know
[4667.52 → 4673.12] that that was the goal so i just that's how it started and then when AVI started it was a year later
[4673.12 → 4678.88] and he had uh he probably had a different mindset so by then I was doing React Native app so we were
[4678.88 → 4684.88] unsure if we needed different brands or how it went so he started his own, but technically we're just two
[4684.88 → 4690.80] people so we need to like merge together our future now like I think we have more clarity now over the
[4690.80 → 4696.88] years, and we see our son growing up oh so we had a second baby right so maybe once he goes to daycare
[4696.88 → 4702.40] and has a more stable routine I think we want to scale and that's when we want to like merge we have
[4702.40 → 4708.96] no reason to have two different companies right yeah yeah economies of scale yeah and different baskets
[4708.96 → 4717.20] too yeah for sure yeah yeah two eggs yeah two baskets yeah not two eggs one basket yeah absolutely
[4717.20 → 4722.56] yeah basket dies yeah we don't even actually like now that you guys are talking about it, we haven't
[4722.56 → 4727.36] even talked about it or thought about it that way oh we're just no we're doing basically the same thing
[4727.36 → 4732.56] right in different names that's that's that's it that's okay times you know when I might be fully
[4732.56 → 4738.40] booked, or he's fully booked if customers come away we just kind of like send them to the other person so
[4738.40 → 4742.80] it's not like that's nice we don't really view it as two different businesses do you charge a referral
[4742.80 → 4750.08] fee no not at all dinner out or anything you know dinner's on him, you should do it you guys are giving
[4750.08 → 4754.96] me ideas you should do it in like marital favours that's what we do and there are lots of ways you
[4754.96 → 4762.88] can take that obviously yeah but I should yeah I would leverage it yeah I would send you a referral I get
[4763.44 → 4767.68] a manicure and a pedicure or something yeah if you're into that kind of thing the joker's
[4767.68 → 4772.24] said it best he said if you're good at something don't do it for free yeah yeah you're referring
[4772.24 → 4777.28] something to somebody yeah husband or not yeah you have to be careful because you know the sword
[4777.28 → 4783.20] cuts two times he said he sent people my way too right so he gets his referral fee I guess it could
[4783.20 → 4787.60] be like hey you're doing dinner tonight you know you're in charge of sides that's how we are in my
[4787.60 → 4792.40] house it's like my wife is like you're in charge of sides or I'm in charge of the main course and you
[4792.40 → 4798.16] know we'll collaborate and come together, or you know I need you to put away the dishes in the
[4798.16 → 4804.08] dishwasher sure thank you very much you know whatever it takes you know yeah, and he's been
[4804.08 → 4809.28] super supportive a lot of the risks I was able to take was also because he was in a stable full-time
[4809.28 → 4813.60] job with health insurance and everything so I was like all right I'm going part-time now that we have
[4813.60 → 4818.16] the baby and then I was like now I'm going to go to a startup, or you know I was able to do all of that
[4818.16 → 4825.20] stuff because I knew I had like a support system and then once I got the stability in that business
[4825.20 → 4832.80] he was able to take a risk too and start yeah what is it that drives you personally I think uh
[4832.80 → 4840.24] personally ever since I got my kid my first kid i kind of found more purpose in life and I wanted to do
[4840.24 → 4847.92] something out of the box um and kind of be a role model to her as well so i just don't want to
[4847.92 → 4854.80] do a nine to five for 30 years and then realize that I missed out on something so I wanted to try
[4854.80 → 4860.48] out being an entrepreneur, and you know see how that journey goes and I think the flexibility was my
[4860.48 → 4866.64] first motivator uh with the time as a new mom that was my primary goal yeah but eventually obviously it's
[4866.64 → 4873.84] the money the flexibility the happiness um to be able to see success and failure quickly and then iterate
[4873.84 → 4880.88] upon that and have control I just don't want a boss controlling my career I want to control my
[4880.88 → 4887.92] career on my own yeah for sure it's been so long since I've had a boss that I can't imagine having a
[4887.92 → 4894.24] boss I guess you know I just can't imagine the not that it's a bad thing or a good thing, but it's
[4894.24 → 4900.64] definitely different from being your own yeah controller of your schedule and what happens
[4900.64 → 4905.76] and what you're optimizing for the things that matter to you the way you schedule your day yeah
[4905.76 → 4912.96] you know I can't imagine the opposite of that yeah I'm sort of in that space right now too yeah
[4913.76 → 4920.48] do you see yourself scaling beyond what your parents did with your business because right now you're kind
[4920.48 → 4928.16] of I do emulating that because I want to I think right now are um we're kind of capped out at a certain
[4928.16 → 4934.72] extent, and we don't have to be that way so um the goal is I think in a year or so we're going to have
[4934.72 → 4941.60] to try to scale by bringing in people who right now the brand unfortunately is just me and him so we
[4941.60 → 4947.28] need to build that trust uh with our customers and be able to train people um so it might have it might
[4947.28 → 4951.12] be a journey so we don't know what that is or what it looks like so we'd have to train people
[4951.84 → 4955.60] and bring them to the level where like hey these are these software engineers we trust
[4955.60 → 4962.48] and um slowly start scaling that way so it might take some time and money to train these people
[4962.48 → 4967.60] who we trust and be like hey they are part of our brand right as well yeah I definitely see myself
[4967.60 → 4976.48] scaling for sure what about family what's that scaling your family no, no the family's done it's just two
[4976.48 → 4982.00] kids it's a lot that was a quick I know you have five you mentioned six technically, but you know we
[4982.00 → 4987.68] don't count Ezra my wife is the same she's like nope no more kids it's over yeah if is I even like
[4988.24 → 4993.60] if for some reason there's even mention of the possibility yeah I can see her recoil
[4995.36 → 5002.08] in like physical and mental I can see it in her yeah because she's like no yeah no, no I think we're in
[5002.08 → 5007.76] a good two is a great number I think the national average is probably two or 2.5 that's good yeah
[5007.76 → 5015.12] yeah I got 2.5 you got 2.5 yeah well that's exciting yeah good luck to you thanks for stopping
[5015.12 → 5019.20] by and talking with us yeah appreciate that any other questions Adam that's it yeah, thank you
[5019.20 → 5021.04] appreciate that thank-you me too yeah awesome
[5027.52 → 5034.40] that's all and that's it our all things open 2024 hallway track coverage ends right here well that's
[5034.40 → 5041.76] not 100 true I guess because we do have a changelog plus members only episode coming soon so stay
[5041.76 → 5047.44] tuned for that if you are a plus supporter otherwise yeah this is it until next year at least
[5047.44 → 5054.40] one more shout out to all of our guests on this anthology episode thank you to Alex IRA AVI and adit
[5054.40 → 5061.52] for the great combos and a big thanks once again to our partners at fly.io you know we love to fly and to
[5061.52 → 5067.28] break master cylinder our beat freaking residents keep the beats coming BMC thank you have a great
[5067.28 → 5081.60] weekend leave us a five-star review if you dig the changelog and let's talk again real soon
[5091.52 → 5102.00] butter is the key to great eggs right the edge is nice and crispy oh yeah yeah do you like a small
[5102.00 → 5109.92] bit or a big dollop uh just a little bit yeah you have to go dollop you were doing so well you do right
[5109.92 → 5117.60] you were doing so well yeah you have to go dollop all right dollop is the way awesome are you an uh a butter
[5117.60 → 5126.32] snob no I wouldn't say, so no yeah do you like uh grass-fed butter you're a butter snob then okay
[5126.32 → 5131.44] you're a butter snob then yeah you gotta check the ingredients right yeah I'm conscious
[5131.44 → 5136.16] about what I put in my body grass only yeah carry gold is the one it's like a brand of choice for a
[5136.16 → 5144.08] lot of people yeah but it's cows I believe it's uh New Zealand not New Zealand it's like Irish
[5144.08 → 5149.84] where's that Irish Irish Irish yeah yeah carry gold yes yeah carry gold's Irish yeah but I was
[5149.84 → 5155.28] thinking it was like Greenland potentially like one of those but not was it like literally an island
[5155.28 → 5160.16] it's Ireland yeah yeah it's Ireland yeah that's what they that's what they call it yeah okay so it's
[5160.16 → 5168.80] cows that graze grass only yep in the fields of Ireland then cows make butter and cows carry gold carry
[5168.80 → 5174.88] gold carry gold yeah it's a with a k pretty cool brand you've never had it I mean maybe I have I'm
[5174.88 → 5181.04] just not a butter snob so I don't know if I'm headed or not I think my wife is the worst of the butter if
[5181.04 → 5189.04] you're achieving the perfect egg uh you know over easy over medium scrambled you pick your style of eggs
[5189.60 → 5195.28] butter grass-fed butter that's right sorry when I make my hamburgers on my griddle
[5195.28 → 5202.32] butter it up yeah when i you know obviously you guys toast my buns for my burgers you
[5202.32 → 5208.48] guessed it butters okay TMI man you can't go wrong with butter right it's vodka I would tend to agree
[5208.48 → 5213.84] that butter is hard to go wrong with its just perfect butter's dope man yeah butters away
[5213.84 → 5218.48] especially grass-fed Irish cows that's right man what do you mean you don't do butter tasting
[5218.48 → 5230.80] I have butter taste all the time man daily pretty much daily I taste some butter's good butter's good
