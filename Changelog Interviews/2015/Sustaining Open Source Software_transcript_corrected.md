[0.00 → 16.56] welcome back everyone this is the changelog and I'm your host Adam stekowiak this is episode 159
[16.56 → 23.52] and on today's show we're talking to mike parameter the maker of sidekick pro inspector
[23.52 → 30.44] and inspector pro and this is more of a conversation show than we might normally have
[30.44 → 36.70] jarred myself mike all talking about sustaining open source we teetered off the subject a little
[36.70 → 42.90] bit here and there but for the most part we were focused on what it takes to sustain open source
[42.90 → 51.00] avoid burnout, and hopefully you love this show we have three awesome sponsors code chip top towels
[51.00 → 58.44] and dream host our first sponsor is code ship very hosted continuous delivery service focused on speed
[58.44 → 65.30] security and customizability you can set up continuous integration in a matter of seconds
[65.30 → 72.30] and automatically deploy your code when your tests have passed code ship supports your GitHub and your
[72.30 → 78.60] Bitbucket projects, and you can get started today with code ships free plan should you decide to go
[78.60 → 84.46] with a premium plan you can save 20 off any plan you choose for three months by using our code
[84.46 → 93.14] the changelog podcast again that code is the changelog podcast that gets you access to a 20 off discount
[93.14 → 99.62] on any plan you choose for three months head to code ship.com slash the changelog to get started
[99.62 → 102.64] tell them we sent you and now on to the show
[102.64 → 110.88] all right everybody we're back got a great show lineup today we got mike parameter here today
[110.88 → 118.76] jarred Santa of course jarred what's up man I'm here I'm excited uh I'm ready to do this you don't
[118.76 → 124.04] sound excited you have to sound excited I'm here I'm excited I'm ready to do this mike you excited
[124.04 → 130.52] I am pumped guys this is the best part of my day right now right awesome, and it's Friday
[130.52 → 136.90] you know it's TGIF the best day ever the best day ever so the conversation today this is so for the
[136.90 → 143.16] listeners sake this is a lot more of a round table than I think some of our other shows might be uh a
[143.16 → 148.32] pretty near and dear topic to any of our hearts here uh sustaining open source not just sustaining
[148.32 → 153.18] open source but just sustainable lifestyles sustaining anything the changelog open source
[153.18 → 159.06] projects a business and uh some recent events brought this to Mike's attention mike tweeted out
[159.06 → 165.10] uh that he wanted to talk, and we said hey let's talk and here we are so what do you think mike
[165.10 → 173.34] uh that's a very accurate summary yeah so yeah sustainable open source where what is it that
[173.34 → 181.14] prompted you to tweet what you tweeted so uh I tweeted what I tweeted because Steve flank uh recently
[181.14 → 187.24] sort of rage-quit twitter and uh this made me profoundly sad I mean I've met Steve before
[187.24 → 194.82] a really nice guy really smart guy uh, and he's one of the one of the good guys in open source that is
[194.82 → 202.46] not only incredibly productive, but he is I think a good role model for other people who are looking
[202.46 → 210.40] to get into uh into open source and so for him to sort of quit uh open source in first in frustration
[210.40 → 219.98] um really worried me and uh I think it is I'm assuming that he i yeah I can't really speak to why he quit
[219.98 → 225.90] per se um but I know that open source has a serious problem with sustainability
[225.90 → 233.52] in people working on open source projects for months or years and then giving up on them because
[233.52 → 239.00] they simply don't want to put any more time into it because it's so frustrating, and so I wanted to
[239.00 → 245.08] have that discussion about uh things that you can do to minimize that frustration and things that you
[245.08 → 252.10] can do to uh ensure that not only are you treated with the most respect, but your users are treated with
[252.10 → 258.74] respect and everyone everybody tries to be uh as respectful to each other as possible well i
[258.74 → 264.70] was going to say let's let's maybe as a group try to reflect on those we can remember or moments
[264.70 → 269.12] we can remember where burnout happened besides Steve here this is the most recent one, but you got things
[269.12 → 276.24] like I'm not sure if why I ever left ruby because of burnout or not um i i I think it's sort of up in
[276.24 → 281.12] the air if you it's an opinion maybe not so much a fact unless anybody has
[281.12 → 287.74] proof, and he said so behind the scenes um lee humbly with Cristiano we had a conversation on that
[287.74 → 292.96] um just recently just yesterday we released a show, or recently we released a show with uh
[292.96 → 298.94] uh I had a conversation with the CEO of joint Scott Hammond, and we talked about Ryan doll having
[298.94 → 303.30] uh issues with burnout and then stepping away from node back in the day and that sort of
[303.30 → 310.28] helped begin some long-term fracturing not so much uh you know he himself but just his departure and
[310.28 → 317.10] you know removing himself as the BNFL, and then you know what got what uh examples can you guys come
[317.10 → 326.50] up with the one that i uh can think of offhand was um jams tucker who is also known as rage
[326.50 → 335.90] he used to maintain rack and he sort of he joined google I think a year or two ago, and he's sort of
[335.90 → 341.00] minimized his open source work over the last two years because he's been so frustrated
[341.00 → 348.22] and um and feels like he's just putting in a lot of work uh for maintenance you know and drudgery
[348.22 → 354.92] um without any sort of reward or recognition so uh i I don't know that he is like tweeted out
[354.92 → 357.76] enraged things but I know he has in the past
[357.76 → 364.20] I don't necessarily have someone else to add to the list one fine point I wanted to make
[364.20 → 370.66] about uh Steve's recent departure um as many listeners know Steve's kind of been involved in
[370.66 → 375.30] the changelog over the years, and so he is in our slack room, and he didn't want to make a point
[375.30 → 381.98] um he asked us to say this if we were going to talk about it is that um he says he had a second he
[381.98 → 386.54] had a follow-up tweet which he says I feel the need to say that this has been a few years coming if you're
[386.54 → 390.84] just reading my timeline you probably don't get it, and then he said to us this is me needing to
[390.84 → 397.28] chill out after years of stuff it's not any particular thing so yeah just wanted to throw
[397.28 → 402.72] that in there when you go to when you get the pedal to the metal and your car goes 120, and you're going 120
[402.72 → 410.78] I love analogies yeah I mean you don't you don't you don't burn out overnight right you burn out right
[410.78 → 418.38] day after day for months and years um your sort of frustration level grows every single day
[418.38 → 422.08] there's um the burn-out doesn't happen overnight
[422.08 → 428.72] so maybe we could talk about some things that attribute to it, so there are a couple factors you got
[428.72 → 435.00] one self-inflicting uh things that you can do right the ways you live your lifestyle the choices you make
[435.00 → 439.88] and then there's the other side which is the way the world perceives what you work on whether it's
[439.88 → 447.34] in recognition or adoration um or put downs or requiring too much from you and treating like
[447.34 → 452.76] a god and expecting more from you than you can actually you know put out sustainably for long
[452.76 → 457.56] periods of time so maybe let's start with the ones you do self-inflicting what are some
[457.56 → 463.32] examples I think of that you can think of that are self-inflicting towards moving you towards burnout
[463.32 → 471.32] well the easiest thing to do is just over overwhelm yourself with work is to just keep
[471.32 → 479.26] saying yes to uh to new features yes to the growth of your own project that you may be working
[479.26 → 485.92] on if you want to build start building your own language and interpreter that might be a fun weekend
[485.92 → 492.62] project but if people start using it if you want to start using it at your work uh maybe for some
[492.62 → 497.40] you know custom business purpose now all of a sudden you've got users you've got something to
[497.40 → 504.22] maintain people start adding ask asking for more features now that weekend project has gone from
[504.22 → 510.12] something that you can throw away to something that other people start to depend on and
[510.12 → 515.88] that brings up a question of how long how are you going to support this thing
[515.88 → 524.70] and sometimes that um those responsibilities can even surprise and overwhelm somebody who never
[524.70 → 532.38] expected their little project to go so far um and all of a sudden now you have all these users at first
[532.38 → 537.82] it's fun um somebody's paying attention to something you built of course that joy of having something you
[537.82 → 542.36] made being used in the real world uh we've all probably felt that, and it feels pretty good
[542.36 → 549.60] and you start to have a certain sense of responsibility that you probably weren't prepared for
[549.60 → 555.70] and how you react at that moment or maybe like you said it is over time but how you react to those
[555.70 → 562.16] type of pressures I think can lead you know one way or the other right people start seeing you as
[562.16 → 567.82] an expert in that space whatever that space might be, and you don't want to lose that respect and so
[567.82 → 575.12] by telling people no you might be worried that you're going to start losing that respect and so
[575.12 → 582.20] a lot of people tend to just start saying yes to everything they don't want to turn down PRS they
[582.20 → 590.22] want to answer every support question as fast as possible um yeah it's an it's a tough it's a tough
[590.22 → 594.68] once you have that ball rolling it's going to roll on its own that inertia is going to keep going on its own
[594.68 → 605.22] and it's hard to stop that as a I guess an experiment in preparation for this call I went on
[605.22 → 610.36] hacker news and searched for burnout just the word burnout uh not a ton of results but enough to you
[610.36 → 617.16] know alarm anybody 331 results I don't know if uh somebody's go back a couple of years and then I went to
[617.16 → 623.28] the next place somebody might rant about burnout or talk about burnout which is medium and uh the list is
[623.28 → 629.08] just way too long to even go through like it's just creative burnout uh all angles of burnout
[629.08 → 639.18] talked about on medium, so clearly this happens every day clearly people are having this issue and
[639.18 → 643.62] clearly it's its going to keep happening because that's what the past says in the future predict you
[643.62 → 650.22] know the past predicts the future so right if is some of these things are self-inflicting what are some
[650.22 → 655.64] of the things that are not self-inflicting where I guess it's the thing where you know we
[655.64 → 660.12] have pride we're like okay great people love what I've done I'm thinking you know when you guys were
[660.12 → 665.42] talking I was thinking about flappy birds like he didn't expect that game to get crazy right and then
[665.42 → 669.08] what happened to him, he was like I'm not making games anymore I don't I didn't follow the drama but
[669.08 → 676.18] it is it broke down to some real serious drama where this game took off, and then he got a lot of hate for
[676.18 → 680.08] the game being too close to Mario brothers, and then it was just the coolest game ever because no one
[680.08 → 685.04] could win it and so then it was about trying to win this game and all he was trying to do is just
[685.04 → 689.32] have fun and release something silly to you know the app store
[689.32 → 697.36] neither that was responsible for the game you know that was one of the fastest forms of burnout I've ever
[697.36 → 703.16] seen I think it was uh yeah what did he last uh three days it was not very long he pulled the game
[703.16 → 707.52] from the app store and then that's nobody got really mad right well he couldn't take the attention
[707.52 → 712.92] right I was telling jarred this too like that's one of the concerns I've had with the change
[712.92 → 718.34] log is like I'm not I'm an I'm a pretty private person I like to share what I do in my life but
[718.34 → 723.46] there are certain lines I don't cross not because nobody deserves to know or I'm I got some secrets
[723.46 → 727.92] it's just that there are things that are private there are things that are public and I didn't want the
[727.92 → 734.20] success required of the change log to sustain it require me to become more and more of a celebrity
[734.20 → 738.70] which I don't desire or jarred to become more and more of a celebrity so that when we go places people
[738.70 → 744.88] know us that's nice but I don't want it to be like well the change log is going to exist forever you
[744.88 → 749.32] know it's going to be the greatest show every time we do it, and then you got like this mountain that
[749.32 → 755.46] sort of like starts mount you know mounting up against you, and you're like I can't live up against that so
[755.46 → 759.80] do you have that problem mike with your work
[759.80 → 765.58] celebrity status people expecting like the greatest thing ever from you
[765.58 → 773.24] I don't I don't think I have that too much and I try not to I try not to lead people into thinking
[773.24 → 780.66] that you know my way is the best way ever i i I try to make it clear that what I build here's what
[780.66 → 788.96] it's designed to do um you know it may suit your purpose, or it may not um i I do have a little bit
[788.96 → 795.50] of the celebrity thing in that when I get like when I went to rails cone last month um it was ridiculous
[795.50 → 804.40] because a lot of people knew me and I know nobody right so um for instance i you know I'd just be
[804.40 → 810.02] talking to a bunch of a bunch of people at the happy hour or whatever, and they'd say hey what do you
[810.02 → 814.68] do and I say well i I wrote sidekick I maintain sidekick is my full-time job now and all of a
[814.68 → 820.30] sudden these guys want to get a photo with me because they do sidekick they love sidekick and
[820.30 → 826.94] they can't believe that they just met me, and you know i so i I don't know any of these guys like but
[826.94 → 833.36] they all know me right so that's kind of the definition of a celebrity where people um people
[833.36 → 839.14] just already know who you are there's no introduction sort of necessary aside from just acknowledging
[839.14 → 847.38] yeah that's me right um but uh what was I going to say we were talking about flappy bird and i
[847.38 → 851.92] had something to mention and I lost track I'll throw one thing in there, and you can think about
[851.92 → 857.72] that for a second i I've gotten it where I was standing in line for a drink at a pre-party or
[857.72 → 862.32] after party to conference and I'm talking to somebody and somebody turns around their like hey are you
[862.32 → 866.96] Adam stack you know they don't even call me by my name they call me by my internet hand or whatever
[866.96 → 870.76] and they didn't know me but about what I was talking about they knew me by my voice
[870.76 → 877.10] and I was like that's me you know like what am I going to say no it's somebody you know but yeah
[877.10 → 883.12] I've had something similar, and my wife was with me, and she was sort of freaked out by it not in a
[883.12 → 888.72] bad way she was like he really is googleable that's that's a long story short jarred you might be able to
[888.72 → 892.96] laugh that because we told you the story before but when I'm a longer version yeah I'll embarrass myself by
[892.96 → 900.14] saying when I first met my wife um one of the things I said to her and depending on how you take
[900.14 → 905.50] it is could be it could be thinking like I was trying to like say I was cool but I wasn't I meant
[905.50 → 910.66] that I was trustworthy that anything you want to find out about me is on Google so I said I'm highly
[910.66 → 916.32] googleable go on Google you can find out pretty much the kind of person I am by the links that link
[916.32 → 922.92] back to what the internet says I am you know so you can realize that I'm not this jerk right anyway
[922.92 → 928.48] sidetrack now I'll just say one more point around the celebrity thing, and then we can put this
[928.48 → 933.22] to bed and talk about sustainability I think Mike has some good ideas around it but uh internet
[933.22 → 938.44] celebrity is different right and I think it's better in the terms of overall celebrity of
[938.44 → 942.58] course you're not on the network news or actually usually if you're on the network news you're in
[942.58 → 949.92] trouble uh you're not on uh yeah entertainment tonight and whatnot but those celebrities they can't
[949.92 → 955.84] escape it like you can't like when you reach a certain level of people knowing you and you're
[955.84 → 960.60] not knowing them there's no privacy for you any more you can't actually get away from it
[960.60 → 968.82] and uh internet famous uh you can always just you're always normal in the real world like you know
[968.82 → 973.28] when you unless you're at hailstone right like I assume when you go to your local Apple Store or
[973.28 → 980.60] target people aren't saying hey it's mike parameter I use sidekick right um so it's nice in the sense of
[980.60 → 985.28] you know hailstone perhaps it'll even more enjoyable for you because you meet people who
[985.28 → 992.52] enjoy your work um that can become overwhelming and then what we do in response to that because we can
[992.52 → 998.74] is we just leave the internet because that's where the pressure is right, and it's a nice it's
[998.74 → 1003.50] actually grace for us that we can't, we can just leave the internet, and we're okay but that
[1003.50 → 1010.56] being said you leave all of us behind whom uh who adore the work that you do on the internet and so
[1010.56 → 1017.86] it's all abandoned being a loss for the community but necessary for the person who uh is leaving very
[1017.86 → 1025.74] true um but to move to something mike did you think about your thing mike uh no, no I didn't
[1025.74 → 1029.60] get your point it's long you want to do the sponsor break real quick jerry then come back
[1029.60 → 1035.26] sure what's uh what's the next topic what do you want to bring up well uh something mike said earlier
[1035.26 → 1040.96] of a pre-call which I think we should talk about is goals right and I think that's a major linchpin for
[1040.96 → 1046.56] um gauging success and failure, and you know whether you can sustain something good deal all right
[1046.56 → 1051.80] let's let's take a break we'll come back and talk about what jerry just said and uh we'll be right back
[1051.80 → 1058.62] you've heard me talk about top towel several times in this podcast but today is different I've got a
[1058.62 → 1064.64] special treat for you, I went out and spoke with a listener who a year ago had never heard of top
[1064.64 → 1070.24] towel he listened to the show just like you're doing right here right now today and heard us talk
[1070.24 → 1075.30] about top towel and what they're all about, and he decided to get in touch, and now he's living the dream
[1075.30 → 1080.86] as a freelance software developer with top towel his name is Daniel Alton and I sat down and I talked
[1080.86 → 1087.46] with him, I said hey what is it that you love most about top towel take a listen well for me the
[1087.46 → 1093.56] thing about top towel which I thought would be very hard for me personally as I transitioned to a more
[1093.56 → 1100.52] consulting role uh was the way I would have access to new clients and what quality of those would be
[1100.52 → 1106.98] so I found that I've had access to awesome clients through top towel, and it hasn't been that hard to
[1106.98 → 1112.70] find because they have a lot of choice and even more than that uh there's enough choice and i I can
[1112.70 → 1118.58] actually be a little selective about what kinds of things I want to be working on so I use that as a
[1118.58 → 1124.58] way to sort of hone my skills, and you know go towards the technology that I think are worth investing in
[1124.58 → 1130.38] for the future so whether it's you know including new front-end frameworks or doing a little DevOps work
[1130.38 → 1136.20] on the site i I usually am able to find clients who are had the needs of the things I want to get
[1136.20 → 1142.70] better at so that's been that's been truly useful all right that was Daniel Alton a listener of the
[1142.70 → 1149.60] change log and also a freelance software developer with top towel if you want to follow in Daniel's
[1149.60 → 1159.34] footsteps go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn
[1159.34 → 1163.32] more about what top towel is all about and tell them the change log sent you
[1163.32 → 1170.68] all right we're back we're talking about how can you sustain open source projects we're here with
[1170.68 → 1179.24] mike para mike has a few ideas and one of those is around goals can you speak to that mike sure I think
[1179.24 → 1186.64] a lot of burnout comes from the fact that uh you as a developer or as an engineer just don't see
[1186.64 → 1194.08] the light at the end of the tunnel for your project uh you don't necessarily see where you're going and
[1194.08 → 1200.32] when you're going to achieve that goal and so setting some realistic goals for your project
[1200.32 → 1207.26] like what you want to happen uh based on all the input and all the work that you're doing on the project
[1207.26 → 1214.98] can really help uh because you're not you don't see it as an endless time sock any more you see it as
[1214.98 → 1219.98] the work that you need to do to get to some point at the end, but you see the light at the end of the
[1219.98 → 1227.20] tunnel so um a lot of people when they create an open source project they just say um I want to create
[1227.20 → 1232.58] this thing and then I want people to use it uh but the problem with that is that that becomes an
[1232.58 → 1238.18] endless time sink where people may be using this thing for the next for five years from now are you
[1238.18 → 1243.74] going to be around five years from now to support it and uh if you acknowledge that yes I'm
[1243.74 → 1248.56] going to be around five years from now that's fine that actually helps your mental attitude so that you
[1248.56 → 1255.38] understand that uh I'm going to do what I need to do to reach that goal of supporting it five years
[1255.38 → 1261.46] from now but if you don't have those goals in mind you can easily be overwhelmed psychologically
[1261.46 → 1268.24] and just all that you have to do, and it just keeps piling up um, and you're not really seeing any uh
[1268.24 → 1274.44] positive outcome uh for all the input that you're putting into the project so the thing I think is
[1274.44 → 1281.10] what you get by doing that is something Matt Vasquez taught me when I started working at pure charity with
[1281.10 → 1289.40] mat tum jarred you know Matt that any of you guys know Matt by any chance I don't think so um super
[1289.40 → 1296.24] smart guy um I think he's its called scrummage is the app he's making get scrummage I believe
[1296.24 → 1302.54] is the URL if it's not scrummage might lead you to his actual project, but he worked with me at pure
[1302.54 → 1307.88] charity lead dev uh turned CTO I think at some point I'm not sure if he was actually CTO or not but
[1307.88 → 1312.02] nonetheless he was the person in charge of the development team but I learned so much from Matt
[1312.02 → 1317.90] about setting expectations I used to get angry at people for not delivering what I thought
[1317.90 → 1323.04] they should deliver, and he would say well did you set some goals for them right so what you just said
[1323.04 → 1330.62] like setting goals for yourself or for other people it is sets expectations if I do this I can expect
[1330.62 → 1335.48] you know to come close to this result or not but that's what I'm expecting to do
[1335.48 → 1342.66] and because you set the expectation clearly enough it's easy to have a waypoint, or you know like a
[1342.66 → 1349.34] positive or negative emotional response to where you're actually trying to go and for me that was
[1349.34 → 1356.24] everything was like setting expectations for me and for others has been huge so anytime I feel angry
[1356.24 → 1361.74] at somebody I'm like i internally before I get mad at them and say lash back which I never lash back
[1361.74 → 1367.84] anybody but lets you know my own version of lashing back I ask myself did you set expectations well
[1367.84 → 1376.26] enough for them if not you're wrong right so how how how explicitly do you set expectations that i
[1376.26 → 1384.92] mean you like make a list or you I mean you know use your own judgment but like for example I'll
[1384.92 → 1389.88] use this example and not because it's a real issue whatsoever but only because it's the most
[1389.88 → 1394.90] relevant issue or the most relevant point I can make today we release the show every Friday we release
[1394.90 → 1402.96] the show right now if is is it had gotten to you know end of Thursday night and end of Friday morning
[1402.96 → 1411.22] and Aaron hadn't finished the file or finished the edit then right then I would say to myself well
[1411.22 → 1416.66] it's in Aaron's court he's the last person to touch the next step for this project to go out
[1416.66 → 1423.14] and I would say to myself if it isn't completed or done did I tell him what needed to be done is it
[1423.14 → 1428.46] clear what his next step should be and if that were the case then I have reason to say well he's got an
[1428.46 → 1433.78] issue but if the ball's in my court and I didn't set expectations clearly enough then it's my fault right
[1433.78 → 1439.56] so that's what I mean by that so like if is it's clear that what the next step should be and they
[1439.56 → 1447.34] have onus of it then that to me is clear enough expectations' gotcha but Aaron you're awesome
[1447.34 → 1452.78] dude there's your just a good example to share and I'm just saying that that's all it's a
[1452.78 → 1456.56] good we shipped the first thing this morning yeah I mean it was awesome everybody loves
[1456.56 → 1462.98] the show it's great and expectations are something that uh you're gonna I think that that's a great
[1462.98 → 1468.44] point Adam you're going to use it anytime you interact with people on your open source project
[1468.44 → 1474.82] even a pr feedback is setting expectation right yeah here 's's the three things that I don't
[1474.82 → 1480.18] like about this PR that need to get worked uh get worked on you're setting the expectation that I'm
[1480.18 → 1485.90] I'm not going to accept this PR until this uh these issues are dealt with yeah and that just makes
[1485.90 → 1492.66] everybody happier that way the PR is not sitting there in limbo uh and the person who sent the
[1492.66 → 1496.70] PR understands that they're going to have to put a little more work into it right uh if they want it to
[1496.70 → 1501.94] to be accepted right if the code review is required for a PR to be accepted which is pretty much every
[1501.94 → 1507.74] PR, and it has been done and the PR isn't accepted, yet it's clear why it's not accepted
[1507.74 → 1514.28] somebody hasn't reviewed the code nobody plus one did the community hasn't approved it and that's why
[1514.28 → 1521.34] it's where it's at, and then you flipped you flip that to someone setting their goals now since Steve is
[1521.34 → 1526.98] is your example we use him like if he set his expectations which he has with this recent uh, uh
[1526.98 → 1532.04] rage tweet that he's he's put out to step away for a bit he's made it clear like hey this is what
[1532.04 → 1536.08] you expect from me, I'm going to be on GitHub I'm going to be here I'll be there but I'm not going to be on Twitter
[1536.08 → 1541.78] I'm not going to be on hacker news so if you call I'm not answering now the expectation is set clearly
[1541.78 → 1548.06] now later on when he comes back, and he's revived himself he's got clarity on his next steps, and he can set
[1548.06 → 1554.08] some more expectations saying hey I'm back um, or it's not a good example Ryan bates right we engaged
[1554.08 → 1559.76] Ryan bates we said hey dude so glad you're back we sent him a dm we were trying our best to be
[1559.76 → 1567.88] not too excited that he was back to push him back into the corner again we want to say hey we missed
[1567.88 → 1572.90] you we appreciate the work you've done whenever you're ready the door's open give us a shout we'll be
[1572.90 → 1578.88] here we'd love to talk to you on the show whatever, and he set up expectations I'm only on Twitter for
[1578.88 → 1584.06] now I'm just kind of lurking here and there I'll engage as I can but for the most part this is what
[1584.06 → 1591.36] you can expect from me and I think that expectation is both for people um you know engaging you as well
[1591.36 → 1599.36] as what you expect from yourself right yeah actually that's that's a that's an another good point the uh
[1599.36 → 1604.44] when you start an open source project not only do you set your own expectations about what the project
[1604.44 → 1612.92] is going to do, but you will, you should also list in your README what users should expect from you
[1612.92 → 1620.54] you know uh the MIT and the BSD license says this code is not fit for any purpose don't expect it to be
[1620.54 → 1628.14] that's setting expectations legally that you cannot hold the developer uh legally liable for any issues
[1628.14 → 1632.88] in the same way you should set saying you read me I'm not going to support this thing
[1632.88 → 1640.00] you know period yeah or if you want support you have to buy an enterprise license at this URL that's
[1640.00 → 1645.82] it or say not accepting pull requests exactly yeah exactly that's a legitimate thing to say in your
[1645.82 → 1652.90] README yeah right I mean and as long as you set expectations and uh before people start using it
[1652.90 → 1658.38] they're gonna they're going to be happy about that because then they can decide do I want to use
[1658.38 → 1663.44] this thing based on these expectations I should have you know if you say I'm not going to support this
[1663.44 → 1669.72] maybe a business would say then we're not going to use it that's fine it's a perfectly acceptable uh
[1669.72 → 1675.82] you know thing to do uh, but it also means that you don't have to be supporting it for years to come
[1675.82 → 1686.84] well we talked about sustainability uh goal setting expectation um mike you mentioned in the pre-call
[1686.84 → 1694.70] the care factor can you talk a bit about what you meant by that sure uh I think to some amount more or
[1694.70 → 1703.70] less all engineers who work on open source uh take pride in what they've built, and they see sort of any
[1703.70 → 1714.66] uh any positive uh feedback on it as a point of pride but any negative feedback as um you know
[1714.66 → 1719.90] like you're taking one on the chin you know you take it a little bit personal when somebody says
[1719.90 → 1727.36] this thing is junk or this thing is broken it just doesn't work um when you spend a lot
[1727.36 → 1738.74] of time building something for free uh you that's a that's altruism that you're giving to the world
[1738.74 → 1745.76] and then to be lashed for it to be lashed out or to be maligned because of a mistake or
[1745.76 → 1750.38] something like that it hurts a lot I wish people were more kind period i just really do wish
[1750.38 → 1755.16] people were more kind people feel so much entitlement sometimes especially when it comes to open source
[1755.16 → 1761.42] like hey you put this out there you should expect to support this thing what are you thinking I think
[1761.42 → 1767.72] a lot I think everyone wants to be a nice guy or everyone wants to be a nice person everyone wants to be
[1767.72 → 1775.14] seen as uh a positive, but a lot of people get frustrated, and they lash out without thinking
[1775.14 → 1782.14] um they don't have that internet skill of writing something deleting it walking away and then
[1782.14 → 1787.84] writing it again 24 hours later yes you know they'll, they'll tweet because they're enraged, or they'll
[1787.84 → 1793.76] they'll write a GitHub comment uh on an issue that they just discovered that cost them three hours this
[1793.76 → 1799.50] weekend, and they'll say this just cost me three hours and such a huge pain in the butt why you know
[1799.50 → 1805.62] kill yourself yeah and they're they're super frustrated yeah um, but you're right that there
[1805.62 → 1811.12] is a sense of entitlement to uh to insulting somebody like that, but again it's its faceless
[1811.12 → 1817.46] communication we're not talking to each other face to face so it's so easy to uh to let up to get a
[1817.46 → 1824.68] flame worse oh yeah I mean text is I will just downright say if it's okay I'll say if it's impossible
[1824.68 → 1831.86] to understand whether you're trying to be nice or try to be mean or even malicious because
[1831.86 → 1837.96] you can't see body language you can't see you can't hear tone in the voice all the things we use as
[1837.96 → 1844.04] waypoints to determine whether Mike's trying to be a jerk to me are gone when it's in text the
[1844.04 → 1848.36] only thing that sort of adds it back lately is an emoji but the other day I got a thumbs up after
[1848.36 → 1854.04] something and I was like is that like shoving it up my or is it like is it like really a thumbs up man
[1854.04 → 1858.70] like and I had to like back away from it and not, and it was a little thing and I should like a
[1858.70 → 1863.72] sarcastic smiley face yeah legitimate smiley face or is that a sarcastic smiley face and I share my
[1863.72 → 1869.14] negative concern with my wife, and she's like Adam chill out it's not that big of a deal yeah that's
[1869.14 → 1874.80] the way to burn out man you have to think you gotta think the best of people right if
[1874.80 → 1880.60] it's unclear which one it is just assumed the best yes one thing that we don't think about is
[1880.60 → 1885.26] sorry mike the one thing we don't think about uh oftentimes when we're on the receiving end of
[1885.26 → 1891.22] a flame right is what's going on in that other person's life yes like what brought them to that
[1891.22 → 1896.92] point right uh to where they say something that's incredibly offensive to me or attacking me and you
[1896.92 → 1902.32] know we don't know about uh that pressure they have at work or uh their spouse who's in the hospital
[1902.32 → 1907.54] right or that bill that's you know three months late yeah whatever it is that's like bringing them to a
[1907.54 → 1916.74] point of uh lashing out you know we assume that they're just a jerk right and uh maybe
[1916.74 → 1921.60] legitimately so in certain cases um, but we tend to give ourselves the benefit of the doubt and nobody
[1921.60 → 1930.40] else and on both sides of that on the internet it's just bad news that is absolutely right i always
[1930.40 → 1936.22] think of it like um I don't know when it changed for me but I can remember clearly that
[1936.22 → 1941.94] something in me changed that whenever I would go to let's say a convenience store to get gas
[1941.94 → 1948.44] and it's before the days we can pay at the pump right, so this is back in the day um you know and i
[1948.44 → 1952.38] go into the convenience store and I go to pay, and maybe I get some gum and I get a Snickers I love
[1952.38 → 1958.22] snickers who don't love snickers right always satisfies that's right this is not an advertisement
[1958.22 → 1961.66] this is not an advertisement for snickers but I love snickers that's a free ad
[1961.66 → 1965.46] snickers if you would like to sponsor the changelog we'll definitely consider folks please
[1965.46 → 1969.36] pause the podcast right now and go buy a Snickers that's right that's right get yourself a Snickers
[1969.36 → 1974.84] and when you buy the Snickers be nice to the person behind the uh the counter you know you
[1974.84 → 1980.24] never have any idea like uh I always like to say hello to the person they wear their name tag for
[1980.24 → 1986.78] a reason if their name is Ben, and it says ben on their name tag hey Ben how are you
[1986.78 → 1993.18] be polite to people and I always think of it like the point I'm trying to make here is that
[1993.18 → 1998.60] you know I don't know that person they don't know me but I get you know 30 seconds of their life
[1998.60 → 2004.18] and they're working, and they got to deal with the public say polite things like hello how are
[2004.18 → 2009.74] you are good to see you know whatever it is because you never know that person may be dealing with what
[2009.74 → 2014.46] jerry was just saying like maybe a bad bill, or you know their boss is going to fire him this is their last
[2014.46 → 2020.26] shift who knows, and you may not be the reason they do it, but you may help enforce their negative
[2020.26 → 2026.06] attitude to go home and kill their wife for their you know or do something crazy that just shouldn't
[2026.06 → 2031.54] be done because you could have controlled yourself better or been a more polite social human being
[2031.54 → 2037.60] and just said hello and use their real name not just like uh sticky gum snickers here's my card bye
[2037.60 → 2044.12] you know be right be a little generous with your love and give some love to people
[2044.12 → 2048.70] yeah, and you just got to try extra hard on the internet because like you said we don't have
[2048.70 → 2053.80] yeah those other forms of communication that you have in real life right with the eyes and the body
[2053.80 → 2060.20] language and so we have to be extra you have to take special care with how we craft our sentences
[2060.20 → 2065.74] and like mike said you know take that that one you put together sometimes I'll just stop and reread a few
[2065.74 → 2071.90] times and say how could this possibly be misconstrued right like could this which is either a joke
[2071.90 → 2079.26] or uh just constructive criticism or feedback which is something that is valuable how could this be
[2079.26 → 2086.70] taken wrongly and try to try your best to you know improve your communications um there's a lot of
[2086.70 → 2092.40] really heated debates though on the internet too and those get going real fast like I don't want to
[2092.40 → 2098.04] bring up any particular topic but some that have been there lately in the news has been
[2098.04 → 2106.68] inclusivity gender bias uh, uh feminism where men aren't treating women well a lot of these issues
[2106.68 → 2113.16] and they escalate so quickly because there's some inherent pain and inherent hurt from previous
[2113.16 → 2120.06] engagements around the scenario around the topic yeah and somebody might indirectly take all the pressure
[2120.06 → 2124.42] and all the pain that someone's built up not saying it's wrong or right not saying that
[2124.42 → 2131.94] that they're not deserving of that feeling, but sometimes we also get you know just like i just
[2131.94 → 2138.34] lay it all mike hey Mike you're taking it all you know because you're here today right and that's not
[2138.34 → 2143.96] right either that's interesting talking about the flame wars that come in people are so
[2143.96 → 2148.70] passionate about certain topics, and it's because they identify one way or the other they identify
[2148.70 → 2154.98] themselves with I'm this or I'm that right it's a tribal response it is and in software we identify
[2154.98 → 2159.08] with our code and I know there's even been conversations back and forth about whether or
[2159.08 → 2166.92] not you are your code and these types of things um one kind of shining anti-example to burnout is
[2166.92 → 2174.18] a recent guest Daniel Steinberg yes that's true the show we did on 17 years of curl uh which everybody
[2174.18 → 2178.88] enjoyed I actually went back and re-listened to that show and he's just a very interesting person
[2178.88 → 2188.20] um he said some things like I enjoy working on curl now more than I did when I started and uh you know
[2188.20 → 2194.14] he's been doing it at least two hours a day roughly for 17 years so I started thinking like why
[2194.14 → 2201.36] how did Daniel uh make it so far and one of the things he said is he said this is my life's hobby
[2201.36 → 2210.76] like curl is me, and he identifies like curl is like his life's hobby, and so he has a level of
[2210.76 → 2218.10] dedication and identity wrapped up in that project that I think um you know you could say maybe is or
[2218.10 → 2224.36] is not healthy at certain times but uh has allowed him to sustain through all the pressure and all the
[2224.36 → 2228.76] times when he doesn't want to be coding and what have you and I think that's just an interesting
[2228.76 → 2233.96] data point what do you guys think about that I like the fact that he calls it his hobby
[2233.96 → 2242.56] yeah and not his life's work yeah um that that is a sort of implicit sort of end goal that he's
[2242.56 → 2249.92] setting there which is that I'm not going to support myself through this um it is a hobby and I'm gonna
[2249.92 → 2255.74] treat it as such which you know sort of implies a level of support and a level of activity that can
[2255.74 → 2263.68] fit into an hour or two a day and not uh eight hours a day one other thing he did too um just
[2263.68 → 2271.98] indirectly um is or not explicitly is focused right he doesn't have curl plus 10 other things
[2271.98 → 2277.70] he's known for curl and I guess subsequently lib curl, but it's sort of the same camp you know
[2277.70 → 2282.08] right so he's he's got a level of focus too where he hasn't spread himself too thin
[2282.08 → 2287.48] and then maybe that's some self-identification of like where his strengths and weaknesses are maybe
[2287.48 → 2292.98] he's not okay with multitasking and working on 10 things at once maybe he's okay with full-time
[2292.98 → 2299.12] employment that's enjoyable and his lifetime hobby and so something I learned from doing founders talk
[2299.12 → 2304.76] for years that like if anybody asked me hey Adam you interviewed all these founders of these companies
[2304.76 → 2310.48] that you know do great things what's the what's like some things you took away the number one thing
[2310.48 → 2317.02] I took away was focus every one of them focused on their goals they set some goals, and they focused
[2317.02 → 2322.28] they didn't do 10 things at once they didn't do 15 things at once they set some goals and
[2322.28 → 2329.10] expectations and ran towards those expectations and as they got closer and closer to them self-analyzed
[2329.10 → 2334.50] am I closer or further away what's bringing me closer further away and took the necessary steps to
[2334.50 → 2339.44] correct their course towards their goals and focused and I think Daniel probably has done that
[2339.44 → 2347.10] based on 17 years of girl it's crazy yeah mike interesting to hear um maybe your thoughts on
[2347.10 → 2353.06] that in light of inspector and the fact that you know you had sidekick, and it's not just your life's
[2353.06 → 2357.74] hobby right this is actually how you make a living you had sidekick you added inspector I think it was
[2357.74 → 2362.76] maybe six or eight months ago um has that changed your focus have you been able to handle
[2362.76 → 2369.66] two projects at once or how's that going right so yeah I mean once I started sidekick full-time
[2369.66 → 2375.62] then you know when I was supporting sidekick in my spare time it was taking a lot of my spare time
[2375.62 → 2381.28] once I had once I was doing it full-time then I realized well this isn't taking eight hours a day
[2381.28 → 2387.04] maybe it's only taking four hours a day so I did have a little bit of bandwidth to support a second
[2387.04 → 2395.20] product so I started building inspector and um, and you're you're absolutely right it was six or eight
[2395.20 → 2401.20] months ago something like that October is when I released it um but just I also did it as a way
[2401.20 → 2407.28] of diversifying I didn't want to put all my eggs in one basket um you know who knows how sidekick will
[2407.28 → 2412.60] do in the future uh so I thought uh well let's build a second product and see what happens
[2412.60 → 2419.02] so I've done that um in practice though inspector has not taken a lot of support time it's still
[2419.02 → 2425.90] sidekick that that dominates my time so and sidekick also dominates my income so I've refocused
[2425.90 → 2437.18] on sidekick and I am working on prototyping uh some new functionality in the sidekick space that I will be
[2437.18 → 2444.04] hopefully releasing sometime this summer hmm we'll see just to get a little bit technical for a little
[2444.04 → 2451.22] minute for a minute here uh interested why you think sidekick uh dominates your time is it
[2451.22 → 2457.06] the threading is it uh you know where reverses go or just because you have so many more people using it
[2457.06 → 2464.28] uh I think there's a lot more people using it I think inspector will uh slowly rise in users
[2464.28 → 2470.82] over time uh, but it's not a's not a grand slam hit like sort of sidekick just sort of took off
[2470.82 → 2478.56] um and also uh sidekick is just inherently a lot more complex it's a framework, so your code is running
[2478.56 → 2483.78] within sidekick whereas inspector is kind of like this black box you configure it set it up on your
[2483.78 → 2490.44] machine, and it just runs right so uh sidekick is just inherently a lot more complex and doing a
[2490.44 → 2495.74] lot more things so when you started sidekick did you follow the advice that you now have
[2495.74 → 2504.10] did you have set goals and did you have expectations that you followed that well I had one explicit goal
[2504.10 → 2511.42] and that was I did not want to work for free for the rest of my life supporting this thing I wanted to
[2511.42 → 2518.68] come up with a way of supporting myself and paying myself for the hours that I was spending on it
[2518.68 → 2523.16] now what that pay was going to be I wasn't sure I didn't know if I was going to make a dollar an
[2523.16 → 2533.62] hour or uh you know a thousand dollars an hour so uh i started sidekick with the aim of
[2533.62 → 2538.98] trying to figure out some sort of business model for it because I knew it was an it was a valuable
[2538.98 → 2546.34] thing it was uh it was going to be my plan was to make the best background job system bar none and
[2546.34 → 2549.86] make it a lot more efficient than the current systems that were out there, so there's inherent
[2549.86 → 2554.22] value in that instead of needing to run 10 machines now you only need to run one machine
[2554.22 → 2558.66] that saves that actually saves the business a lot of money, so there 's's some value right there
[2558.66 → 2567.48] so i I had to play with the various business models for you know the first year of sidekick's
[2567.48 → 2576.62] existence but uh once I hit upon sidekick pro and released it um the sales immediately took off
[2576.62 → 2585.44] and I wasn't self-sufficient in the first year but within I think two years after I released sidekick
[2585.44 → 2593.86] pro I was making more off of it than I was making off of my full-time job and so there was no point in
[2593.86 → 2600.50] working for somebody else to build their dream when I've got my own dream which is scaling up in
[2600.50 → 2606.06] sales over time why not work on that full-time and do my own thing and so that's what I've been
[2606.06 → 2613.24] doing for the last year but uh, but it does go back to having an end goal which is if I'm going to put a
[2613.24 → 2618.40] lot of time into this thing I want it to support me if I'm going to support you need to support me
[2618.40 → 2627.06] so to speak right so that's why i I offer the free version and the paid version and a lot of
[2627.06 → 2632.14] businesses have said yeah this makes perfect sense let's buy this thing we want to guarantee support
[2632.14 → 2639.38] years from now and uh and this is a very easy way to just bring out a credit card and do it
[2639.38 → 2648.00] and in the past mike you talked about um in the past show I'm trying to remember what uh what you
[2648.00 → 2653.82] mentioned that was basically determining what you would allow in the pro version to come
[2653.82 → 2658.10] back into the open source version so if is you're a listener right now, and you're thinking I got that
[2658.10 → 2662.62] question go back and listen to the last show jarred did you have the episode number that mike was on last
[2662.62 → 2670.26] time I'll grab it can you find that because one thing that mike what you said was um was you kind
[2670.26 → 2675.98] of drew the line where pro would overlap with uh the open source version and what you would allow
[2675.98 → 2681.06] coming back in because obviously someone could fork it and add the same feature that you had in the pro
[2681.06 → 2685.70] version to the open source version, but we talked about you know whether you'd accept that pull
[2685.70 → 2690.36] request and what did you write that so you know realistically the features that I've put into pro
[2690.36 → 2699.12] with maybe one or two exceptions are so complicated that i would seriously doubt that someone
[2699.12 → 2705.26] would just be just sort of randomly build an open source version of it just pay mike to to to
[2705.26 → 2713.10] build it and support it I mean right it really is that simple um it really is that simple I know it's
[2713.10 → 2717.72] that simple I know it sounds dumb that's good but remember with the with open source people are
[2717.72 → 2722.50] terrible at estimating how long this is going to take them to build, and so I was talking with a guy
[2722.50 → 2728.20] just today just this morning on stack overflow who said how do I know when my set of jobs are all
[2728.20 → 2734.24] done and I said well that's sidekick pro's batches option, and he was like well can I just implement some
[2734.24 → 2740.46] counters and Regis and uh and just sort of build it myself and I'm thinking and i and I told him up front I was
[2740.46 → 2751.08] like you can absolutely do that it will work 90 of the time and um the other 10 of the time the other
[2751.08 → 2758.12] five percent of the time you'll have no way of figuring out what's going wrong um it will just it'll
[2758.12 → 2764.02] be a time suck, and you know if you're a business you're trying to solve a business problem why are you
[2764.02 → 2770.44] building sidekicks pros batches feature again right that's the expectations back to that
[2770.44 → 2777.44] same thing we did like hey you can do that but if you just support me and support me through buying
[2777.44 → 2782.82] the pro version you can have a happy life not the time suck and there's the expectation so that's
[2782.82 → 2789.30] back to the sustainability of that's how you make your money to I'm sure you got family right mike you got
[2789.30 → 2794.44] wife kids yep a wife and a kid right so you got things to take care of and you're doing work
[2794.44 → 2797.86] and you're being altruistic and putting things out there in the open source world, but you're also
[2797.86 → 2802.26] putting a pro version out there that says hey here's an I've thought of the feature it's really
[2802.26 → 2808.28] complex you don't want to deal with it and if you support me you can get that here and support with
[2808.28 → 2815.00] it I think that's historically a hard sell for developers because we build solutions you know every
[2815.00 → 2819.28] day yeah, and it's like I'll build my own yeah I mean that's just it's in there right
[2819.28 → 2824.40] like i I think that I have to stop myself often I love how as developers I think we're becoming more
[2824.40 → 2830.70] business savvy uh just as an industry over time and uh, and yet I still have to stop myself and say
[2830.70 → 2837.62] why am I handing rolling this solution you know which may take me 10 hours at you know this cost to my
[2837.62 → 2843.34] customer what have you when I know that the solution I saw it, it was 20 bucks a month right or whatever
[2843.34 → 2848.26] it is right, and yet I'm like well that's too much I'll just spend a thousand dollars building it
[2848.26 → 2854.20] that's going to work 90 90 percent of the time all I want is a folder of files on all my machines
[2854.20 → 2859.26] how hard could that possibly be and yet you've got people paying Dropbox billions of dollars
[2859.26 → 2866.16] to provide that same functionality you know your nerds will buy a network attached storage system
[2866.16 → 2873.44] they'll set up a NFS mount they'll do all this complex complexity opens up an IP back to their house
[2873.44 → 2879.64] yeah just provide a folder all that files port yeah, but the reality is that 99 of businesses don't
[2879.64 → 2885.58] want to deal with that so they will pay for the pro version so if somebody wants to build the batch
[2885.58 → 2890.62] or reliability or whatever the different pro features are someone wants to build that and
[2890.62 → 2896.10] release it themselves they can totally do that I don't I don't care it's you are free to write
[2896.10 → 2902.28] whatever code you want um the question though is are you going to be around three years from now
[2902.28 → 2909.82] to support that code are you going to support it as sidekick changes over time that's true so you know
[2909.82 → 2915.02] businesses aren't just paying for a feature they're also paying so that they can, they know that someone
[2915.02 → 2920.18] is going to be there to answer questions to deal with migration and businesses and people though I mean
[2920.18 → 2925.66] because businesses pay for things, but people pay for things with their choices right sure so when they
[2925.66 → 2932.74] choose to use sidekick they're choosing to you know follow you in a trusted way you're not going to
[2932.74 → 2937.76] go anywhere, and they can even trust you more because you do have a business model that is sustainable to
[2937.76 → 2943.84] the point where you can long-term support the open source version you know I mean in terms of not so
[2943.84 → 2948.48] much hey you got a problem here's how you fix it, but you know you're making sure that if things break
[2948.48 → 2952.44] or if there's something that goes wrong with it, you're there to fix the open source version of it and
[2952.44 → 2957.56] re-release it because you've got a sustainable model right so to bring the conversation back
[2957.56 → 2964.64] to the topic at hand which is burnout yes um I knew that when I started sidekick that this was a big
[2964.64 → 2971.96] enough project and my aim was to make it successful enough to where if I didn't have some way of paying
[2971.96 → 2979.22] myself to support myself in doing the project that I was going to burn out there's no way I could
[2979.22 → 2985.70] support sidekick as well as I do today without having it be sort of a job that is paying me money
[2985.70 → 2991.34] and so that's how I dealt with burnout is I turned it into a job and now I'm happy to devote
[2991.34 → 2996.98] eight hours a day to supporting sidekick because I know that it's my full-time job, and it's supporting
[2996.98 → 3005.20] my life so that that goes back to those setting expectations of hey my goal here is to not just
[3005.20 → 3010.50] develop another open source project it's also to develop a business and possibly a life around
[3010.50 → 3017.16] this work yeah so that's I guess where I deviated from what Daniel did with curl he made it his life's
[3017.16 → 3026.08] hobby I want to make it my I want to make sidekick my life's work hmm I wonder if he could make curl uh
[3026.08 → 3031.18] some sort of paint model I imagine right jerry because he says he's got Facebook and all these
[3031.18 → 3036.90] checking companies using it he's gotta they have to have features that uh they need to pay for
[3036.90 → 3042.22] think about that Daniel get back to us well I know he has that I know he has had paid opportunities to
[3042.22 → 3046.96] work on it which gets him very excited um like to add right now he's adding some stuff to http2
[3046.96 → 3054.04] some additional http2 support like on a contract type of deal so he has had opportunities where it
[3054.04 → 3059.38] has made him some money but because he's in his mind it was still that hobby it's not all of a sudden
[3059.38 → 3063.50] now he expects it to make money because if he did you know he may be down at that one dollar an hour
[3063.50 → 3068.70] rate, or you know, and he can make a lot more than that working full-time for Mozilla um for those
[3068.70 → 3074.94] of you who are interested in the full story on uh inspector and sidekick uh check out changelog.com
[3074.94 → 3082.82] slash 130 where mike and us go deep into those topics let's take a break hear from a sponsor, and we'll be
[3082.82 → 3091.70] back in a bit dream host now has managed VPS hosting built for speed and scalability including
[3091.70 → 3097.96] solid state drives and that's awesome these VPS's are built for open source developers and now include
[3097.96 → 3105.22] one-click installations of node.js custom ruby and RVM support speed and more speed is what it's all
[3105.22 → 3112.00] about their VPS servers use SSD hard drives and are 20 faster than traditional SATA drives
[3112.00 → 3120.24] all virtual private servers from dream host include SSD storage Ubuntu 1204 LTS web-based control panel
[3120.24 → 3125.34] scalable ram which is super awesome you can go from one gig of ram and easily scale up to eight
[3125.34 → 3131.50] gigs if you need it node.js one-click install ruby version manager unlimited bandwidth unlimited
[3131.50 → 3138.74] hosted domains unlimited 24 7 support go check them out and learn more at dreamhost.com slash the
[3138.74 → 3152.02] changelog all right we're back it was a fun break um the funnest yeah that was the best break ever
[3152.02 → 3158.68] the best break ever no it really was a good break, and now we're here to talk about moderation so
[3158.68 → 3163.96] we've talked about lots of different things and moderation could have been in some of that
[3163.96 → 3168.62] conversation but directly speaking like what kind of what kind of things have you done personally to
[3168.62 → 3176.06] like practice moderation in your work uh well moderation we all know that burnout happens faster
[3176.06 → 3183.64] the more you the more you push yourself into something right um if you spend 12 hours a day
[3183.64 → 3189.08] working on something it's its very easy to get burnt out very quickly uh so I tend to think of
[3189.08 → 3197.18] moderation as a way of pushing back burnout um of easing up on the gas so to speak to use that
[3197.18 → 3204.22] car analogy so that um you're not going 100 miles an hour uh, but you get a chance to
[3204.22 → 3211.88] to do other things in your life and sort of you know change mental gears that always uh helps
[3211.88 → 3217.26] with the burnout so moderation uh is all about you know spending an hour or two a day and not
[3217.26 → 3224.82] four six eight hours a day especially if you're got a full-time job working in software where then
[3224.82 → 3229.36] you go home, and then you work with software for another four or six hours uh you know that's a
[3229.36 → 3234.26] recipe for burning out really quick lord and many people do that lord yeah lord knows computers can
[3234.26 → 3240.38] be frustrating so um you know also the city position too like you think about the moderation on the brain but
[3240.38 → 3247.00] on your body you know if you study sure jarred I know you stand might you sit or stand I sit
[3247.00 → 3253.10] um but i I also exercise a fair amount um so i I run you're a runner that's right I know you were
[3253.10 → 3262.38] I climb um i uh what else do I do push-ups so yeah I'm generally throughout the day or at the
[3262.38 → 3268.16] weekends and stuff like that like throughout your day I usually do one of those a day so uh before the
[3268.16 → 3273.96] call here I ran for 30 minutes cool um and then yesterday I was at the climbing gym climbing so
[3273.96 → 3279.22] and then the day before that I was out racing my motorcycle around the racetrack so right weren't
[3279.22 → 3283.84] you worked at the climb right that was okay I'm we had so many guests on I'm trying to remember
[3283.84 → 3290.44] who was it so and that was all about being active and outdoors and stuff like that so exactly, exactly
[3290.44 → 3296.18] so I definitely fit into the brand there yeah yeah that's that's another thing I mean I think you
[3296.18 → 3302.10] can try to stand you can minimize some things to step into moderating what it is you do with your
[3302.10 → 3306.38] body but yeah if you are the person who's working 10-hour days and then going home and working on
[3306.38 → 3310.22] open source, and you're sitting 14 hours a day, and then you're sleeping you never really give your
[3310.22 → 3317.78] back or body a chance to sort of stretch out and just be a more healthy body human being like
[3317.78 → 3322.94] people think their mind I'm probably hijacking what you're trying to talk about mike but I'm just
[3322.94 → 3327.92] thinking out loud here like people only think about especially intellectual people they think oh I got a
[3327.92 → 3333.20] good mind they forget about their body they forget to eat right they forget to your know go to the gym
[3333.20 → 3339.74] or just not so much to be like a fitness nut but just to move your freaking body and I'm actually going
[3339.74 → 3346.04] through this myself because I'm I was in that space where i you know probably was a bit you know too into
[3346.04 → 3350.76] the intellectual side of you know moderating my lifestyle and now I've realized that I've got to
[3350.76 → 3355.92] balance things out I've got to make time to go to the gym you know several times a week I've got to
[3355.92 → 3361.92] make time to do these different things and I got to eat right because if not Geez I mean I can get
[3361.92 → 3368.08] sick and I don't know if you guys know this fellow but um IAN war shack and does that name ring about
[3368.08 → 3374.70] either view yeah he's a friend of mine okay so you know his story IAN uh you know love the guy but uh
[3374.70 → 3379.84] a real quick snapshot he was probably living a good lifestyle and I'm not sure what the situation was
[3379.84 → 3386.56] that that made him get so ill, but he'd gotten so quickly he'd gotten a cold and went to the hospital
[3386.56 → 3394.10] and before you knew if it was severe it was serious, and he was um just like you and i all of our limbs
[3394.10 → 3399.62] all of our fingers, and he came down with a sickness I'm not sure if it was because of moderation so I'm not
[3399.62 → 3404.70] trying to place that on him, but it's its uh it's something that can happen to every one of us where
[3404.70 → 3411.36] in a moment's notice your body can turn on you your body cannot react the way and even your
[3411.36 → 3417.28] brain too with Alzheimer's and different diseases so I think moderation isn't just in what we do with
[3417.28 → 3422.12] our lives you know or what we do with our day-to-day coding habits but also just how we play out our
[3422.12 → 3430.70] lives and just to wrap up uh IAN's story uh he ended up losing his hands and his he was his amputee uh
[3430.70 → 3436.90] amputated from his knees down and not that he's not living a good life because dude is
[3436.90 → 3443.66] strong he's he's he's uh he's got a great family he's got a great support system around him, he's happy
[3443.66 → 3449.62] he's doing great things, and he's not down in life, but easily he could have been easily he could have
[3449.62 → 3455.50] had these things that were so precious to every one of us taken away from him and just went into a
[3455.50 → 3460.52] hole, but he's strong, and he didn't do that but I'm sure he's learned some things he can share with
[3460.52 → 3464.56] the rest of us about moderation about living a healthier lifestyle that doesn't let your body
[3464.56 → 3471.94] turn on you like that you know he's an amazing person uh he actually just opened up an uh GoFundMe
[3471.94 → 3479.74] uh thing because he wants to hike, or he wants to climb Kilimanjaro I hadn't heard about this so i uh
[3479.74 → 3484.94] I actually donated to his cause there but I'm sure we can put a link at the bottom of the show page
[3484.94 → 3489.92] or whatever you guys do with the links absolutely we can put a link to IAN's uh thing
[3489.92 → 3497.10] because he's uh one of the nicest guys I've I've ever met um completely like totally humble person
[3497.10 → 3504.26] and um just yeah you're right he got this illness out of the blue for no reason it could
[3504.26 → 3507.50] happen it's one of those things where it could have happened to any of us, and it just happened to
[3507.50 → 3515.08] happened to him yeah and uh, and so he's made an amazing recovery um and yeah I guess he
[3515.08 → 3521.52] owns his own business he still codes ruby still codes iOS ruby I don't know how I mean yeah
[3521.52 → 3526.14] I'd love to hear we actually know what i I just said this the other day to Daniel Luzon who
[3526.14 → 3531.88] uh just to plug a sponsor real quick uh listen to the show got interested in top towel now he freelances
[3531.88 → 3536.42] through top towel which is one of our sponsors but I was talking to him yesterday telling him
[3536.42 → 3543.28] IAN's story and I was like we need to have you know the show so we'll make that happen and of course we
[3543.28 → 3548.54] have to let him accept our invitation, but we'll invite him and if he comes on we'll, we'll help tell
[3548.54 → 3554.72] his story but yeah strong dude and much love for IAN, and it could happen to any of us if we don't live
[3554.72 → 3561.18] healthy for sure but yeah I mean like so to get back to the subject at hand um you know we've all
[3561.18 → 3566.68] had those incidents where we take a shower and all of a sudden a problem that has vexed us for hours
[3566.68 → 3572.54] all of a sudden the way to fix it becomes clear and that's because you're you're you're sort of you're
[3572.54 → 3577.66] changing your pace right you're letting your mind go to a different place than rather than just code
[3577.66 → 3584.48] 24 hours a day it's always in the shower isn't it yeah or overnight right you go to sleep and you
[3584.48 → 3590.56] wake up, and you just have the answer um I've dreamt honestly I've dreamt about sometimes uh solutions to
[3590.56 → 3595.58] things yeah, and it's like what how did I dream that like that was my dream that's crazy that's
[3595.58 → 3599.90] that's the moderation right you've got to let you got to change gears all the time eight hours
[3599.90 → 3608.26] of sleep man work eight play eight sleep eight yeah but um, so moderation is not just uh your own
[3608.26 → 3615.04] habits uh or how much work you do, but it's also how you relate to others uh because open source
[3615.04 → 3622.98] is sort of an infinite uh time suck and if people are just constantly peppering you with requests
[3622.98 → 3630.44] and questions you will find yourself spending all of your time dealing with that and so that's where
[3630.44 → 3637.16] part of moderation is being able to say no to people it's being able to say I don't have the
[3637.16 → 3644.84] time to implement that feature um or no this PR is uh is not something that I want to maintain
[3644.84 → 3650.74] because I have to I have to consider the support costs of this change and I don't want to support
[3650.74 → 3658.86] it for the next you know five in years right for the length of the project um and so there's a large
[3658.86 → 3665.56] number of reasons why you might say no to people, and you need to consider um that as part of
[3665.56 → 3673.20] moderation you need to moderate your own time as part of a project so we uh we'll say this you are
[3673.20 → 3678.66] you are all here on the air because uh jarred is so awesome, and he googles well jarred you're good at
[3678.66 → 3688.04] that right thank you that's I do it for a living some would say some would say uh so it's gofundme.com
[3688.04 → 3697.44] slash IAN hikes i an n h i k e s IAN hikes right now his goal is six thousand dollars the amount
[3697.44 → 3702.58] raised is 725 we need to push that up we need to push that up to make this dream come true this is
[3702.58 → 3709.62] you know I can't wait to have him on the show now I'm excited but uh Geez man what a goal to have
[3709.62 → 3717.88] moderation what a good conversation IAN is not moderating his goals there no, no he is he's leaning
[3717.88 → 3723.62] far into them hiking the trail behind my house that's a moderate goal yes hiking Kilimanjaro that
[3723.62 → 3730.10] is not a moderate goal no that's that's extreme yeah sometimes though you know and that's the thing
[3730.10 → 3737.72] too right is part of moderation comes wise choices' wisdom I think i I think wisdom is probably the thing
[3737.72 → 3742.52] that sits beneath everything we've talked about today because you can have moderation that
[3742.52 → 3747.14] doesn't mean always playing it safe there are times to take risks and I'm sure you can attribute that
[3747.14 → 3752.42] mike and you as well jarred and there are times you go above and go to the extremes like climbing uh
[3752.42 → 3758.14] climbing Mount Kilimanjaro there are times you do that, but then there are times when you
[3758.14 → 3762.68] moderate your life a little bit more, and you do things that uh allow you to have more flexibility and
[3762.68 → 3767.54] more focus in certain areas' goal setting I think is super, super important to all these
[3767.54 → 3774.34] things yeah but the wisdom to know when to go to the extremes or hang out in goal land
[3774.34 → 3781.24] and uh and keep keeping doing what you're doing there so any closing thoughts mike jarred
[3781.24 → 3790.96] uh say no to drugs kids of course say no to pull requests no say no to pull requests
[3790.96 → 3799.78] indeed the world's most dangerous drug yes no I mean uh you know i I think moderation and learning
[3799.78 → 3805.56] to say no and being realistic with what you want to do and what you want to achieve is that part of
[3805.56 → 3812.80] that wisdom uh it's part of the experience you get uh over being in being an open source developer
[3812.80 → 3818.22] for a number of years you start to learn this stuff I got something that I think might be and you guys
[3818.22 → 3827.10] might like is uh sometimes we're our own worst enemies right, and you got your buddy to your right
[3827.10 → 3832.38] and you got your buddy to your left and I learned this in the army right you got those people around
[3832.38 → 3837.36] you that you can trust and if you're someone trusts so and this is an example let's say
[3837.36 → 3842.56] uh the three of us here right I'm someone you guys trust and if I think jarred is doing something that
[3842.56 → 3849.52] is abusing his moderation abusing his goals if I know his goals and I'm there as a support person
[3849.52 → 3855.62] in his life because I'm close enough to him and I see him stepping out of line help I would say help
[3855.62 → 3861.30] people that either you look up to or you know, and you're close enough, and you can say this to them
[3861.30 → 3866.46] help them moderate their life help them not go too crazy help them realize you know hey you said
[3866.46 → 3870.88] you're going to focus on these goals and I see you doing this and this is not saying you're doing
[3870.88 → 3875.62] anything wrong you might want to just double-check back to your goal list are you actually going towards
[3875.62 → 3880.88] where you're trying to go because sometimes I'm my worst enemy and my wife man if I didn't have
[3880.88 → 3886.90] my wife had this sometimes I know for sure I'd be on the ground and I just would not be who I am
[3886.90 → 3891.62] because she knows me so well she knows what my goals are she knows who I'm trying to be
[3891.62 → 3897.58] she knows what kind of man I'm trying to be, and you know if I didn't have her as a support system
[3897.58 → 3906.38] if I didn't have her as her advice I would make unwise choices all the time every day yeah so
[3906.38 → 3912.46] maybe as a call to arms for people is to watch out for our fellow developers out there our
[3912.46 → 3917.50] fellow friends out there whether you know how close you are to them is your choice but
[3917.50 → 3922.46] help others not go towards burnout don't push them to burnout yeah
[3922.46 → 3929.62] see if I have a closing remark it would be uh back to the point about a hobby versus a living
[3929.62 → 3936.56] and uh the goal setting uh can be simplified down to is am I doing this as a hobby or am I doing this
[3936.56 → 3942.20] as a means of making a living and I think determining that and holding strong to it of course you can
[3942.20 → 3947.38] switch at a certain point if you want to but knowing what it is helps you moderate because
[3947.38 → 3953.02] a hobby has got to be fun it's got to be fun it's got to be interesting, and it can't consume your life
[3953.02 → 3959.74] um now a job sometimes you just got to do the job right it's work and that's why we call it that
[3959.74 → 3966.44] um so I think that's a good way to judge you know this idea you have or this project you just started
[3966.44 → 3970.14] and what you're getting yourself into is how do I approach this is it a hobby
[3970.14 → 3974.94] or is it a job and I'm gonna you know approach it um appropriately for each one
[3974.94 → 3981.68] that's a good way of thinking about it, I think from a technical engineer's standpoint
[3981.68 → 3988.72] what's fun to me is writing the code what's not what's never fun is supporting uh users
[3988.72 → 3995.30] just because you know I don't have that problem and so when they come to me and they that I'm solving
[3995.30 → 4001.30] their problem that's work I'm working for them to solve their problem and so you have to be very
[4001.30 → 4006.74] clear uh yeah with open source especially around support how long are you going to support this
[4006.74 → 4011.62] thing how much of an effort are you going to make support supporting it what channels are you going
[4011.62 → 4016.32] to support it through otherwise it'll just it'll, it'll suck all the fun out of the project
[4016.32 → 4020.62] for example not Twitter I saw you tweet just yesterday as I was kind of like
[4020.62 → 4026.54] coming back to your timeline to prepare to see if there's anything else you any recent um you know
[4026.54 → 4030.52] sustainability nuggets you've shared that we should pull into the conversation, and you were like hey
[4030.52 → 4035.64] I don't do support on Twitter go here right you know, and you said it in a polite way you know you
[4035.64 → 4040.66] didn't say it as mean as I just said it but uh you know you were you know you made it clear you set
[4040.66 → 4047.92] expectations that support doesn't happen on Twitter don't ask for it it's its a nightmare right 140
[4047.92 → 4054.56] characters come on that's not realistic that's no half of support is getting the user to define
[4054.56 → 4059.04] their problem oftentimes when you force somebody to write out what the problem they're having is
[4059.04 → 4064.72] they can solve it themselves yeah like it's its almost like rubber duck debugging right yeah um but
[4064.72 → 4070.06] you know someone asking a question 140 characters I'm going to give you 140 character answers which is
[4070.06 → 4076.06] not going to be very useful so yeah i I try to make it clear to people uh and I don't I don't
[4076.06 → 4081.24] I'm not mean about it but I just be matter of fact I don't use Twitter for support twitter's here for
[4081.24 → 4087.18] you know retweeting stupid stuff and cat pictures and that sort of thing change all posts or change
[4087.18 → 4091.14] blog posts yeah that's that's the stuff you have to retweet right there well that was the stupid stuff
[4091.14 → 4096.52] I'm just kidding that was well cool any of the closing thoughts before we trail I don't know this
[4096.52 → 4100.76] has been a has been a fun show for me to have a discussion it's not often I even get to talk this
[4100.76 → 4106.96] much, but it's been fun I liked it thank you for jumping on the subject and and and allowing
[4106.96 → 4111.38] me to come on uh you know actually let me uh let me open up twitter real quick because there's another
[4111.38 → 4118.94] person we should thank uh here on the show because they are the reason I even saw your tweet which uh
[4118.94 → 4127.22] it was Marcello and I don't know how you say a last name because you're from my favourite country
[4127.22 → 4135.82] uh Brazil um but Marcello I'm going to say that, and you're m-a-r-c-e-l-o-c-g on Twitter
[4135.82 → 4144.14] Marcelo Gonçalves Marcello Gonçalves uh that's probably not right but yeah without the
[4144.14 → 4150.34] proper accent you can't say that name so I won't attempt it and I'm already uh known to be a bad last
[4150.34 → 4156.60] name butcher i just there are times I can't say my own last name let's just say his last name is utf-8
[4156.60 → 4162.78] compatible because it's got some that c's got some crazy there you go yeah he uh he retweeted
[4162.78 → 4168.22] your tweet mike and then I was going back through at mentions for our old twitter handle so if you're
[4168.22 → 4173.00] listening to this, and you're still tweeting at the change log on Twitter we've moved to at
[4173.00 → 4178.42] change log because uh it's you know it's shorter saving three characters saving three characters
[4178.42 → 4184.52] that's right so we did that and we check uh at the change log mentions from time to time and
[4184.52 → 4188.76] Marcelo retweeted yours and I was like what is this and I was like oh okay cool and I was like
[4188.76 → 4193.64] no one's responded to mike hey we've got time no more you want to come on the show you're like yeah
[4193.64 → 4199.24] sure yeah johnny on the spot johnny on the spot I like it that's the that's the best show is the
[4199.24 → 4204.82] is uh is the impromptu unexpected great shows and mike you're always a great guest this is what your
[4204.82 → 4210.14] third time being on the show third time's a charm yeah well we'll have to make you uh
[4210.14 → 4217.34] I just love the gab you know you do I'm going to get you that smoking jacket you've earned it
[4217.34 → 4223.70] yeah that's the truth we'll have to send a t-shirt do you have a t-shirt i i I'm wearing a t-shirt you
[4223.70 → 4228.34] are but do you have a change log on it no I don't have a change log we're going to correct that we're
[4228.34 → 4232.24] going to send you a t-shirt fair enough when we're done here we'll get your address we'll, we'll ship
[4232.24 → 4238.68] you out an awesome comfy tea and if you don't have a change log tea not to Sony, but you could go buy
[4238.68 → 4243.84] one if you wanted to change.com slash store they're only 20 bucks I think they're 20 bucks
[4243.84 → 4251.00] as worn by local ruby celebrities that's right look that's good, and they're super comfy American
[4251.00 → 4257.98] apparel uh some of the best shirts out there uh but anyway let's let's tail this off great i really
[4257.98 → 4262.02] did enjoy this is so much fun so if you were listening to this you'd like to see us do more
[4262.02 → 4268.30] discussions like this encourage us tweet at us not negatively positively right be nice
[4268.30 → 4275.82] share your love um but with that let's say goodbye fellas bye see ya
[4275.82 → 4277.76] you
[4277.76 → 4291.76] you
[4291.76 → 4301.22] you
[4301.22 → 4302.22] you
[4302.22 → 4303.22] you
