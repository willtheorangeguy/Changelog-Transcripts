[0.00 → 13.50] welcome back everybody this is the change log where members support a blog and podcast
[13.50 → 18.06] that covers what's fresh and what's new in open source this show is hosted by myself
[18.06 → 23.84] Adam static as well as Andrew Thorpe say hello hey how's it going, and we're also joined by our
[23.84 → 29.42] fellow change logger Steve flank hey everybody, and you can tune in live to this show
[29.42 → 34.38] like you can today it's Tuesday at 5 p.m Central Standard Time right here on five by five
[34.38 → 39.60] you can check out the past shows we've recorded at five by five dot TV slash changelog and this
[39.60 → 46.58] is episode 90, and we're joined by avid grim maker of pair program with me and ruby extraordinaire
[46.58 → 51.46] welcome to the show avid how are you I'm doing great thanks for having me so where do we where
[51.46 → 56.08] do we kick off this call I mean I know we got kind of a huge docket of things to talk about um maybe
[56.08 → 62.58] for the uninitiated somewhat introduce yourself you're a podcast yourself a writer and all sorts
[62.58 → 71.76] of stuff where do we begin with you uh well I'm I'm a hacker um I'm a hacker that's me yeah uh I'm a
[71.76 → 79.32] hacker I've been uh working a lot with ruby for the past several years many years um but uh
[79.32 → 85.34] I don't know what else you want to know I'm a family guy I've got lots of kids and why don't
[85.34 → 90.10] you give us a little bit of insight into some of the work you've done uh with wide teams and ruby
[90.10 → 95.50] rogues and that kind of stuff okay so um yeah that's the uh I guess the broadcaster side of my
[95.50 → 103.74] my life um I have been doing a podcast of my own for the past few years uh it's called wide teams
[103.74 → 112.06] it's at wide teams.com, and it is dedicated to disperse teams uh remote workers people that are
[112.06 → 115.76] working geographically removed from the other people that they're working with
[115.76 → 123.86] and the goal there has just been to kind of collect stories from people find out how people are working
[123.86 → 128.88] on dispersed teams, and you know what special strategies they have to make it work and what
[128.88 → 132.54] tools they're using and what they like about it what they don't like about it all that stuff mainly
[132.54 → 138.22] just to sort of um you know connect people like that and uh you know help us learn from each
[138.22 → 143.06] other because I was working remotely and there just didn't seem to be a lot of resources when I got
[143.06 → 153.20] started yeah those resources um are kind of plentiful now and I remember you know two years ago is when i
[153.20 → 159.76] started my full-time remote job it was difficult to find any kind of um you know resources out there to
[159.76 → 165.06] help me just know like what would make my life easier right so looking at some of the stuff you've
[165.06 → 171.86] done um you know with wide teams specifically um, and now you know even a little bit more with
[171.86 → 177.70] with the idea of pairing and remote pairing and things like that man it would be nice to uh
[177.70 → 184.28] to have these resources at my disposal when I first got started a few years ago um I love the name
[184.28 → 188.58] man wide teams is such a perfect name for distributed teams I mean where did you come up with that
[188.58 → 195.32] thanks uh same way I come up with anything else all the all my name naming ideas I go for a long
[195.32 → 201.44] walk go for a long walk what about uh what about your your your twitter bio how many questions you ever
[201.44 → 210.10] get about that I mean do people think you're a demon or a daemon um yeah so that's uh, uh 80 angel 10
[210.10 → 215.90] demon and the rest is hard to explain um that actually I don't know if anybody's ever asked me
[215.90 → 223.64] about that but um it is a reference to an over the Rhine song um first year and uh I stuck in the
[223.64 → 229.10] sort of the Unix spelling of demon just you know because nerd see i was thinking you were really
[229.10 → 233.18] just playing on the fact that you know what a daemon is, but then you were hoping that maybe nobody else
[233.18 → 240.22] did but anyway so the resources on why team so you started this podcast how long ago
[240.22 → 246.30] uh i you know I'm not even sure I'd have to I'd have to look, but it was a couple of years ago
[246.30 → 252.38] um actually probably more than a couple now yeah we're on you're on episode 81 now so
[252.38 → 258.16] however long ago it was you've definitely uh you've definitely gone into the depths of distributed
[258.16 → 262.42] teams with some of these people here I see here on the front page you have Ernie miller
[262.42 → 271.38] of living social um heard I got a chance to hear him talk at uh I want to say it was ruby oh
[271.38 → 278.74] it was big ruby conference in grapevine Texas, and he talked about this he talked about the idea of um
[278.74 → 286.54] you know what it what does it mean to be happy in your job, and you know it's not money it's not uh
[286.54 → 290.00] you know he even went as far to say it's not the people you're working with because
[290.00 → 294.98] you'll find people that you love to work with at a lot of places and right to him what he said
[294.98 → 300.88] that the absolute most important thing about being happy your job is being happy at your job
[300.88 → 304.72] wherever that might be whether you're driving working from home you know whatever it is and he's
[304.72 → 310.30] obviously you know a remote worker for living social, and so he was saying you know kind of what
[310.30 → 315.36] we're going to echo here today which is that like if possible the idea the ability to work from the
[315.36 → 320.60] comfort of your own home is tremendous and you kind of hit on it uh when we chatted a little
[320.60 → 325.26] bit earlier avid with you know you love that you can work from because you that means unlike the
[325.26 → 332.02] traditional you know business mindset that comes out of the great depression and on in America we as
[332.02 → 337.44] you know as workers as people that are in the workforce get to spend more time with our family
[337.44 → 344.02] and that to me that's something that makes up for any level of you know financial compensation that you
[344.02 → 350.74] can find yeah yeah it's a huge deal and it's exactly you can't really um you know you can't
[350.74 → 355.26] really count it up in monetary terms but here's a question for you maybe to kick off this conversation
[355.26 → 363.24] are you an are you part of a distributed team right now uh I can't really say that I am so I mean I was
[363.24 → 370.42] part of many different distributed teams for years but uh my job has recently changed um kind of
[370.42 → 378.40] dramatically my job description is now I guess uh screen screencasted uh primarily uh because i
[378.40 → 384.12] launched ruby tapas which is my screencast service and that's awesome um and it became popular
[384.12 → 390.82] enough that I was able to devote myself to it full-time so um that's kind of a one-man gig
[390.82 → 398.22] so I'm not I'm no longer you know working with other freelancers on a job or you know working as part of a
[398.22 → 403.42] distributed startup, or you know any of the other things that I've done yeah so for those of you
[403.42 → 410.02] that don't know ruby tapas, and you can go to it at rubytapas.com um the description of it like many
[410.02 → 417.14] of your projects is just perfect, and it's short screencasts of gourmet ruby um and yeah it's awesome
[417.14 → 423.20] and so these are some you know some great resources it's very, very affordable I highly recommend them
[423.20 → 428.96] uh my question is how much of an influence did Ryan bates and uh rails casts have on you when you
[428.96 → 434.74] were starting this well I mean uh people like Ryan bates you know I mean well particularly Ryan bates
[434.74 → 441.60] really broke ground um I mean he's a pioneer yeah I mean i I think the influence there is
[441.60 → 449.48] is the fact that he could, you know that he was there and um just made it clear that it's possible to
[449.48 → 455.80] to do a professional screencast you know and to do that as your job uh you know him and um
[455.80 → 463.76] and others uh I suddenly had a brain fart but uh somebody help me out here um well Ryan I think he
[463.76 → 468.18] was a pioneer in terms of like just leading the way I mean he was one of the very first at least in
[468.18 → 473.42] the ruby spectrum doing screencasts, and he did it very simply right like he was just breaking ground on
[473.42 → 479.18] how simple it was he had this de facto template for all of his you know all of his screencasts and I think
[479.18 → 485.50] he'd even gotten uh ruby hero in 2009 not so much for that but just his impact to the community
[485.50 → 491.30] right yeah to kind of hit on a few other ones that you may have heard of you got peep code um yeah
[491.30 → 498.82] absolutely rails best practices and rails tutorial.org those guys so and Gary's destroy all software
[498.82 → 506.72] existed as well exactly my short my short-lived project uh watch.Steve which no one forget no one
[506.72 → 510.48] knows about which is amazing that's what I always tell people is like if you're going to try something
[510.48 → 516.10] try it because if you fail no one will ever know or remember anyway so like I totally did this a
[516.10 → 520.52] couple years ago and no one cared and so it disappeared off the face of the internet and now
[520.52 → 524.16] no one knows so Gary Bernhardt was a big inspiration for me as well
[524.16 → 533.62] cool yeah this is its cool I mean to see so you're not I don't know how what's the best way
[533.62 → 540.44] to say this the to do screencasts to get to some level of um you know credibility is the
[540.44 → 545.64] right word but at some point you have to prove to people that like the code you're writing is
[545.64 → 551.42] is good code you know what you're doing is quality stuff, and you call it gourmet ruby so what do you
[551.42 → 556.78] think it was that because for me, I think the first time that I ever heard of uh avid grim was probably
[556.78 → 565.08] when I read um exceptional ruby which is a tremendous book um thank you how do you think what do you
[565.08 → 569.38] think kind of gave you a little bit of that credibility the the the I don't know if notoriety
[569.38 → 576.04] is the best word but just the ability to go out and um start to sell your what ultimately isn't even
[576.04 → 580.80] necessarily a product it's a're sharing knowledge so what do you think got you to that point
[580.80 → 584.82] it's just an incremental process really I mean I think it's probably similar for anyone you know
[584.82 → 591.18] you start to write things here and there I started to blog um you know a while back long around 2006
[591.18 → 596.66] or 7 and um you know I found that that people seem to like some of the stuff that I wrote and
[596.66 → 602.10] eventually I got around to doing a talk or two uh and that's where exceptional ruby came from
[602.10 → 606.20] was I did a talk and then I was like wow I've done all this research about exceptions uh it'd be cool
[606.20 → 612.64] if I could kind of you know recoup some of the time somehow uh so I turned it into a book um and
[612.64 → 616.38] people like that to you know so it's really just like you know the confirmation of the market you
[616.38 → 620.38] know people buy something people don't seem to hate it people don't like you know ask for their money
[620.38 → 625.56] back, and they actually say nice things about it and eventually um eventually it kind of
[625.56 → 631.28] breaks through my assumption of I'm just another dumb programmer that maybe you know some of the
[631.28 → 637.38] stuff that I have to say not everybody knows before we get into the uh what I think the
[637.38 → 641.30] meat of the show is going to be with pairing uh I have a question for you what do you think about
[641.30 → 648.20] what are your thoughts on being an uh exceptional master what are your thoughts on exceptions as control flow
[648.20 → 657.42] I'm not a fan when you so you would, you do exceptional ruby as a talk before you actually
[657.42 → 663.34] wrote the book or no yeah I did yeah okay so would you get that question often when you would talk on
[663.34 → 669.50] exceptions uh I think a few people probably ran that by me um I think um I did make a point if i
[669.50 → 675.06] recall correctly I think I made a point of including catch and throw even in that talk um and I was
[675.06 → 680.12] actually I got to uh I got to use that that transformation just the other day I was working
[680.12 → 686.36] on the discourse code base and I submitted a pull request converting um an exception used as an as
[686.36 → 692.54] as control flow into a throw and catch uh which is sort of the approved ruby way of doing that
[692.54 → 699.42] right, right cool yeah that's I think that I don't I think that might come out of my java days back in
[699.42 → 705.52] college, but that's a question that i I think I've had many long arguments with a non-local so for a
[705.52 → 709.66] non-local return in a language that doesn't have you know something like throw and catch or
[709.66 → 714.28] continuations or anything like that um sometimes it's the only thing you can do
[714.28 → 719.70] yeah do we need to give some background to some of this context just for those who may not be
[720.58 → 724.12] Uber ruby developers but want to kind of catch up with what this means
[724.12 → 731.50] yeah go ahead avid why don't you explain um uh which part so you got exceptions what's what's this
[731.50 → 736.56] method of catching and throwing okay so uh a catch and throw in ruby is a construct that's actually
[736.56 → 741.96] very similar in implementation to exceptions it's its another way of sort of tossing something up the
[741.96 → 748.12] call chain, and it unwinds the call stack until it is gets to something uh that can catch it uh so it
[748.12 → 752.64] actually you know describing it is sounds a lot like exceptions, and it is, but it's specifically
[752.64 → 758.50] intended for non-exceptional cases it's specifically intended for the case where you want to you know
[758.50 → 763.66] just do an early termination, but you need to kind of do it non-locally um the circumstance that i
[763.66 → 770.26] saw this in most recently was a sax parser uh which of course is hand you hand the parser off to
[770.26 → 775.70] or you hand an event handler class that you write off to a parser and the parser then calls
[775.70 → 782.34] event methods on that event handler that you wrote um and at some point uh in this the one I was
[782.34 → 788.04] looking at they realized okay we're done now we don't need any more XML um but how are you
[788.04 → 793.50] going to tell the parser that uh there wasn't any way to tell the parser yet parser okay stop
[793.50 → 798.52] pulling data stop going through we don't need any more just end it here um, and so they were using
[798.52 → 802.68] an exception they were raising an exception to the call stack and then catching it higher up
[802.68 → 810.32] um and uh using throw and catch is a bit nicer in ruby for that it's an it's its cleaner it looks it
[810.32 → 815.04] actually looks better there's less code on the page you don't need to define a special exception just
[815.04 → 820.00] for it because you're throwing a symbol instead of an exception it's just generally um better
[820.00 → 828.68] looking down into the rabbit hole Adam yeah no i I'm I'm there with you, I'm so right there with you
[828.68 → 833.82] honestly it's kind of neat though I mean because it seems like um it might have come about as like a
[833.82 → 837.38] hack, but it's a good technique a good method, and it's you don't really have any other way to get
[837.38 → 843.20] around it, but it's a good way to use contracts and ruby to achieve your goal yeah well it's one of
[843.20 → 847.44] those cases that you almost never need I mean I would hate to see a code base that was using them
[847.44 → 850.40] all over the place because that would be terrifying it doesn't seem like it's the most
[850.40 → 855.32] reliable way but every now, and then you need to break through a layer of somebody from your software
[855.32 → 859.50] through a layer of somebody else's software back to your software again and that's where those you
[859.50 → 864.70] know sort of non-local terminations come in gotcha right and the notion or the concept of an
[864.70 → 870.44] exception is very old it's not it's not anything new to ruby or anything so um but that that's an
[870.44 → 875.34] argument that's a debate that has been had for years amongst developers so i think throw
[875.34 → 882.84] and catch uh specifically I think they may have originated in like um a lisp uh like um scheme
[882.84 → 891.50] or something I'm not certain yeah cool so okay to kind of get to the topic du jour um to keep up
[891.50 → 897.72] with the gourmet ruby oh yeah I caught that I'm with you uh okay so one thing we want to the thing we
[897.72 → 902.76] kind of want to get to is pair program with me um and why don't you give us an introduction
[902.76 → 909.54] it's a like i I think the best way to describe it um Audi instead of calling it a product necessarily
[909.54 → 914.46] it's more of a movement or more of an idea yeah it is kind of building a community so why don't you
[914.46 → 919.90] give us some insight into what it is where we can find it and where you'd like to see it go okay well
[919.90 → 926.12] let me start off with a little bit of history um I've I'm a big fan of pair programming uh I'm
[926.12 → 930.34] gonna uh should I assume that most listeners are familiar with pair programming or should I introduce
[930.34 → 934.50] that uh why don't you go ahead and introduce it I would definitely say introduce it pair programming
[934.50 → 940.60] is the very simple idea of programming um right not programming so solo instead sitting down with
[940.60 → 947.88] somebody else and programming um so it's its not exactly groundbreaking but uh, uh it's part of it
[947.88 → 955.74] was part of the original extreme programming practices um and probably one of the most controversial of them
[955.74 → 961.12] uh you know partly I think because programmers like a lot of programmers like to think of them
[961.12 → 968.24] themselves as solitary beasts and uh partly because there was a perception that well if you take two
[968.24 → 973.80] programmers, and you put them in front of one screen then you're going to have your uh your project
[973.80 → 982.62] speed um and uh, but it turns out that it's an incredibly effective technique uh for many
[982.62 → 989.40] reasons um you know number one it's kind of constant code review I mean code review has been found to be
[989.40 → 995.46] one of the most effective ways of avoiding bugs that we know of and pair programming is a way to always be
[995.46 → 1003.10] be code reviewing um it's a great way to retain focus I found that in when I'm pairing with someone
[1003.10 → 1010.90] I stay focused, and you know I don't get distracted nearly as much um because you know who no pair
[1010.90 → 1016.78] probably doesn't want to pair with you on Twitter right so you kind of feel like you know I should
[1016.78 → 1020.76] probably stay focused on the task at hand you don't know the kind of developers I pair with
[1020.76 → 1026.32] do you like you know pair every other word on careful, and they could be listening
[1026.32 → 1029.76] write this
[1029.76 → 1039.84] um yeah uh you know so um it's uh one of the big benefits that I like about it is the effect on morale
[1039.84 → 1045.84] um you know I found that sometimes I'm having a bad day sometimes I'm working on a piece
[1045.84 → 1050.50] of code that just bums me out and I really don't want to touch it and I don't want to deal with it
[1050.50 → 1059.30] but I have to um and having uh somebody to deal to go through that with you can be a huge pick me up
[1059.30 → 1068.52] um and uh gosh there are so many good things about pairing keeps you pairing makes you smarter
[1068.52 → 1077.26] um programming alone you can do some really dumb stuff I've found like um let me give you an example
[1077.26 → 1086.98] uh recently I was writing some working on some back-end code for ruby tapas and um I was basically
[1086.98 → 1092.36] trying to pull some data out of the shopfront service that I use a third third-party shop shopfront service
[1092.36 → 1103.00] uh called DBD and um earlier I had actually worked with them to define and like um to get a
[1103.00 → 1110.12] feature rolled out which was uh that you can sign up to the ruby tapas videos as a RSS feed in
[1110.12 → 1115.64] like iTunes uh or Miró or a bunch of other programs and I'd actually like worked with them on that I'd
[1115.64 → 1122.18] sort of laid down what the RSS format should look like for it and all this stuff and then I'd
[1122.18 → 1127.34] moved on so later on I was working on some back-end code and I was you know working alone not pairing
[1127.34 → 1132.34] with anyone and I was working on pulling data out of their website, and it was just basically
[1132.34 → 1138.92] screen scraping because they don't have an API for this stuff yet and I had finished all this really
[1138.92 → 1146.06] complicated screen scraping code when I got into a conversation with somebody on Twitter and about
[1146.06 → 1151.50] this the screen scraping code, and they said something about well it can't be that hard parsing the RSS feed
[1151.50 → 1157.82] to get that data back out and this huge light bulb sort of crashed down onto my head
[1157.82 → 1168.10] um as I realized that I had been sort of blindly screen scraping information that was in this RSS feed
[1168.10 → 1176.98] that I had helped define that is the kind of stuff that happens when you program alone or at least when
[1176.98 → 1182.44] I program alone so it's not, and it's its not just that either I mean if you think like if you're a
[1182.44 → 1187.38] developer and think about you know oh I've solved this problem before and i it's might not be the
[1187.38 → 1191.26] the best most efficient way to do this but here let me just copy and paste this code well you're not going
[1191.26 → 1196.94] to do that if you have your colleague watching over your shoulder you know like and just to kind of
[1196.94 → 1201.22] real quick in case to fill in a gap in case anybody doesn't understand the concept I don't think we
[1201.22 → 1206.06] actually said it but when you have two people in the same room pairing together typically there's
[1206.06 → 1211.14] one person that is actually sitting at the keyboard doing the typing right another person that's watching
[1211.14 → 1216.22] that's like you know looking over your shoulder you're talking about what you're doing he's watching
[1216.22 → 1220.40] what you're doing pointing out things as you do them if they're an incorrect kind of idea yeah and
[1220.40 → 1224.16] there are a couple of different I mean there are different models of its um you have sort of classic
[1224.16 → 1229.54] uh navigator driver pairing where basically the navigator is sitting backhands off the keyboard
[1229.54 → 1233.18] but they're actually doing most of the thinking they're telling the driver what to do what to code
[1233.18 → 1238.32] um driver is responsible for actually getting it onto the page making sure that you know they don't make
[1238.32 → 1244.28] too many typos and um you know hitting the button to run the tests and all that stuff
[1244.28 → 1249.28] um and the navigator is kind of freed up to sort of wave their hands and think
[1249.28 → 1257.14] and maybe look up documentation stuff like that um, and they may well switch off
[1257.14 → 1262.74] periodically um you know traditionally if is like the navigator ran out of steam they might
[1262.74 → 1267.18] switch around, and you know maybe the driver says oh I think I know I think I know what to
[1267.18 → 1274.00] do here, and so they switch off uh and then there are other things like um ping pong pairing uh which is a
[1274.00 → 1280.30] a method of pairing that uh works well with test-driven development where uh basically one right
[1280.30 → 1284.90] one person will write a test and then the other person has to make it pass and then they
[1284.90 → 1292.62] they keep going back and forth like that um and um, and sometimes it's its you know less defined it's
[1292.62 → 1299.28] more organic it's just you know two people sitting there and uh trading the keyboard off as they
[1299.28 → 1303.42] see fit um some people actually set up desks if you're co-located they actually set up desks where
[1303.42 → 1310.60] there are two keyboards plugged into the um into the same machine and I've noticed that with remote
[1310.60 → 1315.96] pairing specifically the more organic style is what kind of seems to fit and that we're we're
[1315.96 → 1319.94] talking to each other as we're looking at you know we're sharing it a screen with we mix or something
[1319.94 → 1325.56] and right as we're looking at that we're talking to each other and um you know we you kind of just
[1325.56 → 1330.94] have to get a feel for the other person and how the other person works, and you know so me and some
[1330.94 → 1336.30] of my co-workers that as we do it uh if i notice something and you know I know how this
[1336.30 → 1341.28] person works I know when it's appropriate for me to jump in and type something and to back out and
[1341.28 → 1346.18] it just kind of happens naturally for us so I think that tends to be what do you think that I think that
[1346.18 → 1351.72] tends to be more common with remote pairing I don't know it's hard I think it depends on the
[1351.72 → 1357.92] technology you're using and the kind of connection you have um I mean so I've actually done a fair
[1357.92 → 1366.08] amount of uh quite a bit of remote pairing with using screen sharing and um that tends to be less
[1366.08 → 1371.94] of an of an organic handing the keyboard back and forth kind of thing just because uh most screen
[1371.94 → 1377.50] sharing software has latency that's high enough that it's really impractical to type if you are on
[1377.50 → 1385.98] the remote end right um so it partly depends on what kind of technology you're using so what happens
[1385.98 → 1390.90] whenever I mean it's its great if you're in that situation when you're sitting in the same room
[1390.90 → 1394.88] but what happens and i I mean I know some of the answers to these questions but I'm just kind of
[1394.88 → 1398.24] curious from your perspective and the reason why we're having you on the show is to talk about this
[1398.24 → 1403.20] this deep pair programming topic, but you know what happens when you're not, and obviously you've got
[1403.20 → 1407.30] answers for that because you do the podcast why teams, and you've talked about this heavily so I mean
[1407.30 → 1412.84] how does the situation change when you're not face to face you're not in the same room yeah I think the
[1412.84 → 1418.08] truth is that it doesn't change a huge amount um obviously there are some technical hurdles
[1418.08 → 1423.40] uh there are various technologies to bridge that gap you know like we said there's screen
[1423.40 → 1433.18] sharing uh another very popular um technique is to use some form of tmux uh to share a terminal and the
[1433.18 → 1440.78] nice thing about sharing a terminal is that it's very low bandwidth and so uh it actually becomes practical
[1440.78 → 1445.38] for somebody remote to type on your screen because the don't have to send that very
[1445.38 → 1450.82] many you know that many bytes um and there are various yeahs I mean there are sub categories of
[1450.82 → 1456.18] that there's hosting it on a like a shared machine in the cloud versus hosting it on somebody's own
[1456.18 → 1461.06] machine stuff like that so you mentioned the tmux and tmux I mean how much Andrew do you think we
[1461.06 → 1466.40] should explain some of these things because I don't want people to assume oh we can link to that
[1466.40 → 1471.00] kind of stuff in the yeah we can but i I want to say that I don't I don't I actually don't find the
[1471.00 → 1475.74] the technology all that interesting it you know we're at the point where it's its totally possible
[1475.74 → 1480.62] and that's kind of all I care about right I mean it's its constantly progressing we keep having new
[1480.62 → 1485.40] stuff um there's a new there's a new screen sharing service called screen hero which is kind of cool
[1485.40 → 1489.78] because it's really, really fast, and you get you each get your own cursor your own mouse cursor on the
[1489.78 → 1496.06] screen um you know and there will be more you know interesting tools in this space, but you know in the end
[1496.06 → 1502.18] um it's more about what you do with the tools right and real quick the technical hurdles
[1502.18 → 1507.64] involved are typically hurdles you have to jump over once and once you get over those hurdles
[1507.64 → 1512.06] you don't really have to deal with them any more so yeah pretty much we don't need to focus too much
[1512.06 → 1517.64] on the tools because you know that can be different for everybody um so to kind of move on you know
[1517.64 → 1522.18] again we'll share all that stuff in the show notes but to move on from this to pair program with me so
[1522.18 → 1526.44] now we kind of have an idea of what pairing is and so yeah some of the reasons why it's beneficial
[1526.44 → 1532.74] um so go ahead yeah I mean so i I'm a big fan of for all those reasons I'm a big fan of pair programming
[1532.74 → 1538.96] uh and then I did something kind of crazy last year for like the latter half of last year uh I stopped
[1538.96 → 1543.76] i kind of stopped doing traditional consulting work which is what I've been doing for a while
[1543.76 → 1550.94] and I became what I think of as a consulting pair programmer uh and basically what I did was I took
[1550.94 → 1555.92] appointments with people to pair program remotely for two hours at a time that's what I did for my
[1555.92 → 1563.40] job for uh probably like six or eight months um, and it was awesome uh I really enjoyed it and um
[1563.40 → 1570.78] and you know a lot of people seem to get really get a lot out of it and i at the end of that i it
[1570.78 → 1574.74] sort of that sort of came to an end I still do that I still do open source pairing sessions
[1574.74 → 1578.94] uh but I'm not doing that as my job anymore because like I mentioned before uh ruby tapas
[1578.94 → 1585.08] really took off, and so I made that my main focus but um you know coming out of that i just
[1585.08 → 1592.24] felt like I wanted more people to have that experience um you know especially more people who
[1592.24 → 1599.80] maybe are not part of a team a co-located team where they get to pair program every day
[1599.80 → 1607.60] um I wanted I really wanted to see more people who are isolated or who are you knowing living maybe
[1607.60 → 1612.36] they're in a city, but it's not a big tech hub city so they're they're not um around a lot of other
[1612.36 → 1619.22] programmers, or they're like the only programmer on their team or for whatever reason um are not
[1619.22 → 1625.56] getting a chance to pair program uh I want to i just I want to see more programmers benefit from the
[1625.56 → 1632.20] experience of pair programming and uh so I decided that i kind of wanted to just basically start a
[1632.20 → 1641.70] movement and that's kind of where so the URL is pair program with dot me yeah there's a couple of uh
[1641.70 → 1647.30] there's a couple of these out there, but it seems to be that and maybe this is because of people
[1647.30 → 1652.08] like Steve flank who I don't think you've said a word yet steve I've said one or two very briefly
[1652.08 → 1658.06] but yeah I'm staying out of it but Steve has kind of you know embraced this um and I think you know
[1658.06 → 1664.74] we have some of the more without trying to sound like a know suck up some of the more uh well
[1664.74 → 1669.06] known rubies in the community that are starting to embrace this concept and I think that that that
[1669.06 → 1677.06] will help this to move forward so um pair program with dot me again is the URL and the idea is that
[1677.06 → 1682.58] you can basically you're just there's nothing special that's necessarily happening with this
[1682.58 → 1689.90] project this is just making it this is helping you to get an idea to share with the world that you are
[1689.90 → 1695.78] available to pair yeah I mean the website is almost incidental um you know I wanted some sort of focal
[1695.78 → 1701.12] point um but when I launched it, it had a badge and nothing else so it had a badge you could put on your
[1701.12 → 1707.44] site and that's you know the badge says pair with this says pair program with me um, or maybe it says
[1707.44 → 1712.04] pair with me, I need to check but anyway pair with me um, but you know it's its kind of like it's
[1712.04 → 1715.48] kind of like the badges that you see on some websites that say fork me on GitHub that's that was kind of
[1715.48 → 1722.72] my inspiration um and that was really all I launched with and that's that's when i kind of
[1722.72 → 1731.10] kicked things off with a talk um at ancient city ruby um a couple of months ago and yeah I mean
[1731.10 → 1736.70] it's its really it's an idea the idea is uh you know number one pairing is awesome number two you
[1736.70 → 1741.58] don't need to be in the same room to do it um and number three all you really need to do is ask
[1741.58 → 1748.92] um i I guess that you know for me the biggest thing is sort of inspiring a culture where we ask each
[1748.92 → 1756.70] other hey do you want to pair on this and half of that is the asking and half of that is having
[1756.70 → 1761.42] having an environment where it's okay to say that you know having an environment where it feels
[1761.42 → 1767.60] natural to say that um, and so i kind of wanted to get people to start uh putting this badge up
[1767.60 → 1773.98] be just you know to kind of put a welcome mat out to make it um feel like yeah it's okay
[1773.98 → 1781.42] to say hey would you pair with me on this and I think that the one thing that you find in
[1781.42 → 1786.44] especially in the ruby community and I've spoken to some python guys and this is I think in
[1786.44 → 1791.12] every community but in the ruby community one thing that you find and when we had our uh a few
[1791.12 → 1797.90] a few episodes ago we talked about get tip and one of my concerns for a project like that is that you
[1797.90 → 1802.10] have all these rock star ruby developers that get-together and this is just a way for them to
[1802.10 → 1807.18] to make each other feel like even more of rock stars right and so the whole idea behind pair
[1807.18 → 1813.06] pair program with me, we need to say ppm we need to say what you can just say pair with me
[1813.06 → 1818.92] the whole idea behind pair with me is kind of taking that barrier away right, so this is like
[1818.92 → 1823.62] if is you're an I don't know ruby rock star I don't know what to call yourself but if you know you kind
[1823.62 → 1828.76] of know like hey i I have some clout like i I work on some bigger projects you know like Steve
[1828.76 → 1832.72] you work on a bunch of stuff you're on the know do rails contributions you do a lot of stuff
[1832.72 → 1837.82] um if you make this known to the public then you're bringing that barrier down a little
[1837.82 → 1844.12] bit, and you're saying hey like you might kind of you might look at me as a ruby rock star but I'm
[1844.12 → 1849.00] available to help you to help you learn to help you solve a problem to help you do whatever it is
[1849.00 → 1853.88] that you need to do right that doesn't necessarily even mean that you know every single like you know
[1853.88 → 1858.42] Steve Planck is not my co-worker who I'm gonna reach out to every time I have a problem to fix my
[1858.42 → 1864.12] problems for me but it does say that you are making yourself available in cases where you're
[1864.12 → 1869.56] needed and if you have the time and if you have righted you know whatever I mean like I said i I do
[1869.56 → 1876.24] open source pairing sessions um and um and those have been those have been really neat for me and
[1876.24 → 1882.82] what I really like about them is you know those are free sessions obviously and uh they've they've
[1882.82 → 1888.44] often been the case they've often been times when I get to work with someone who's really
[1888.44 → 1896.46] new to programming or new to ruby or new to whatever you know technology we're working on um
[1896.46 → 1905.06] and that's an it's a fantastic experience um you know i I highly recommend it to anybody who's
[1905.06 → 1913.62] kind of advanced at what they do because um it's just you get to experience that you know vicariously
[1913.62 → 1919.00] experience that thrill of you know learning something new uh you know that that oh my you
[1919.00 → 1923.64] know wow I didn't know you could do that that's amazing you get to experience those moments
[1923.64 → 1929.90] all over again it's like we forget that uh there was a time when you had to learn what it meant to
[1929.90 → 1934.90] assign a variable yeah I mean i I feel I fear that that maybe sometimes people might look at the
[1934.90 → 1939.34] idea of pairing with a newbie and think wow that's going to be tedious but the truth is it makes
[1939.34 → 1946.40] you feel amazing um and so I guess really like my biggest call is out to people who are kind of
[1946.40 → 1951.92] in that position of you know knowing whatever language they work in knowing it pretty
[1951.92 → 1958.74] well-being pretty good at it, you know maybe being seen as a guru or a master or whatever um I would
[1958.74 → 1963.48] love to see more people in that position uh kind of put up the welcome mat and say yeah come on pair
[1963.48 → 1970.40] with me, it'll be fun um I think it there's a lot I've seen a lot of people you know who are
[1970.40 → 1978.56] newbies who feel like um you know these people are unapproachable you know their programming
[1978.56 → 1986.22] heroes are unapproachable and um you know I think we all know i I well I guess the newbies don't know
[1986.22 → 1991.86] but you know i you know i we're not unapproachable i I'm not I try not to be unapproachable I don't
[1991.86 → 1997.40] really think any of the people that i um you know see it a lot of the ruby conferences are
[1997.40 → 2004.12] remotely unapproachable um and uh, and you know we're all just programmers if people still think
[2004.12 → 2008.08] there's like secret sauce like i so I've done a couple of these sessions a lot of these sessions
[2008.08 → 2011.50] now I wasn't actually even an avid's talk I just saw him tweet about it and I was like sounds good
[2011.50 → 2015.84] tweeting and then I was like oh I have like 15 appointments this week now which is awesome looks
[2015.84 → 2020.16] like I'm pairing, and it went we're well and I actually did yesterday and today as well um random
[2020.16 → 2025.24] pair with me stuff as well but um I had somebody literally say to me like hey I'm real sorry that
[2025.24 → 2028.70] we keep writing this code and this test fails and then like it's taking a while to get it to pass
[2028.70 → 2033.56] and I was like I don't know what you think I do all day but like I run my tests, and they fail and i
[2033.56 → 2037.88] try to fix them, and they don't work and then I run them again, and then they fail and so like you
[2037.88 → 2042.26] know it's all we're all just programmers it's not it's not a big deal um, but you're Steve beatnik
[2042.26 → 2045.78] you don't have to write tests everything works that comes out of your fingers stupid, so this is
[2045.78 → 2049.44] actually what happened today avid said earlier like you know when you feel terrible about code
[2049.44 → 2055.54] it's great to pair with things um and so actually that's what I did today um assuming it passes a
[2055.54 → 2060.00] little bit of review I'm going to commit this to rails later today but like um so I found a regression
[2060.00 → 2064.12] in rails because of the readers of the rails foreign action book found a discrepancy between
[2064.12 → 2069.58] like beta 1 and rc1, and so I figured out what it was and I got a failing test and I tried to fix it
[2069.58 → 2075.18] and it didn't work and uh I was like wow this feels really stupid like basically just when the
[2075.18 → 2081.10] password confirmation is nil or empty string don't worry about it which like is super trivial
[2081.10 → 2085.68] and not complicated but I couldn't get my freaking test to pass, and so I ended up like tweeting
[2085.68 → 2089.70] finally like hey I'm feeling really dumb could somebody pair with me on this, and we paired and
[2089.70 → 2093.10] I thought we got it working, but it turns out we didn't so today I did the same thing I was like
[2093.10 → 2097.56] hey is anybody interested in like working on this bug and so finally after two pair with me sessions
[2097.56 → 2101.54] I've managed to like the diff is like a three-line diff or something it's not even
[2101.54 → 2106.16] complicated it's just that like talking with someone is so helpful um you know and what's
[2106.16 → 2111.52] hard is different based on time to how you're feeling and all that other stuff too so how
[2111.52 → 2116.68] concise do you think the topic needs to be so if you is somebody reaches out to you and says hey can
[2116.68 → 2123.66] you pair with me on this how exact does that topic need to be before if the topic is too broad right
[2123.66 → 2127.30] there's too big of a learning curve for somebody that you don't know to maybe want to get
[2127.30 → 2132.82] involved so like how exact on a know that specific instance for you Steve you were like
[2132.82 → 2136.96] here's the test this is failing and I can't figure out how to get it passed that's pretty specific like
[2136.96 → 2141.82] you don't need to understand anything else other than what you're doing but if somebody comes to
[2141.82 → 2147.44] you and says like you know hey um I need to i need a shopping cart like that you know what I mean like
[2147.44 → 2151.68] that that's too broad to be able to really sit down at one time and say let's work on that
[2151.68 → 2156.58] together so where do you at avid and Steve maybe where do you consider the kind of the sweet spot with
[2156.58 → 2161.54] like how precise do you need to be with the thing that you're trying to work on
[2161.54 → 2171.30] um I don't know I haven't really thought that hard about it um you know I try to avoid I try to if
[2171.30 → 2178.12] somebody approaches me and is like uh you know I want to make a new Facebook then you know then I'm
[2178.12 → 2184.94] going to say hey can we know sort of contract the scope a little bit um, but it's kind of I don't
[2184.94 → 2190.26] know it's one of those organic things that it's its each I think each pairing session kind
[2190.26 → 2194.82] of works out its own parameters I don't have anything specific on scope but I just like limit
[2194.82 → 2200.52] it to time so I'm like oh I only have one hour I only have two hours, and then you know if is the
[2200.52 → 2205.10] goal is to learn then you can get two hours worth of learning regardless of whether the scope is
[2205.10 → 2209.80] huge or small so I find that's much easier in terms of also with people's scheduling and
[2209.80 → 2214.24] expectations you know that it's not going to last like longer than a particular amount of time so
[2214.24 → 2218.16] that was one of the things yeah the other day was like hey I have a call in an hour and a half so
[2218.16 → 2223.76] we can work on this up to that amount but like you know I have this other hard boundary um so yeah
[2223.76 → 2228.76] with your interests and some of your skill sets that means that typically I'll get an hour to two to
[2228.76 → 2233.88] to build a hypermedia API with you yeah basically I haven't done that with anybody yet, but you know
[2233.88 → 2238.18] that would be that would be fun um mostly it's been rails and rescue so far is what I've done most of
[2238.18 → 2242.12] my pairing on because people are very interested in like how to work on rails and then like it's
[2242.12 → 2246.16] the same as any other ruby project you clone it you run some tests you write a new one you make a pass
[2246.16 → 2251.84] but I mean obviously it's a big project so um you know that can be complicated to be perfectly honest
[2251.84 → 2257.58] and maybe I shouldn't, it shouldn't let this on but I've had um I mean I've had pairing sessions that
[2257.58 → 2263.46] kind of just devolved into answering questions uh or having a conversation so and that's good I mean
[2263.46 → 2269.82] because what so Kenneth writes on a show a few weeks ago talked about um in python, and we have
[2269.82 → 2274.54] this in ruby too like you can read all the books you want, but there's this there's this set of tribal
[2274.54 → 2279.34] knowledge that you pick up as you go and as you do things wrong and as you read other people's blog
[2279.34 → 2284.50] posts, and you watch ruby tapas and you know there's this tribal knowledge that isn't necessarily
[2284.50 → 2290.28] in any book right it's hard to just teach all ruby in one book so for newbies to come to you and
[2290.28 → 2295.54] you know you might, they might have a very specific problem but if it kind of breaks down into
[2295.54 → 2300.44] just like a question and answer and education session that's good because that's a that's an
[2300.44 → 2305.72] opportunity for you to share that that tribal knowledge to share you know like this is best
[2305.72 → 2311.00] practice this is what we tend to do in this world so here's some insight and I mean who knows if
[2311.00 → 2317.88] that's if that gets the ruby newbie the uh most confidence that they can have to continue on
[2317.88 → 2323.54] that's probably the best use of that time is it not yeah absolutely and that's one of the
[2323.54 → 2332.90] the biggest reasons that um i kind of got this started was um the idea of just spreading ideas
[2332.90 → 2339.34] spreading knowledge um uh what I think of as kind of mimetic diversity you know a diversity of ideas
[2339.34 → 2346.12] and I think that pairing does that better than anything else um, and it's good for us as programmers I mean
[2346.12 → 2352.98] having a wider getting to learn from a wide variety of other programmers experience
[2352.98 → 2358.66] I think you know makes us well-rounded makes us better at what we do gives us more tools in
[2358.66 → 2364.96] our toolbox when we're confronted with a problem um it's just all around good if I could jump in here
[2364.96 → 2372.98] real quick on the notion of approachability and some of the I guess potential of like having
[2372.98 → 2376.10] you know, and we have this question here at the end of the show and I'm excited to hear what your
[2376.10 → 2380.48] answer is obviously but like you know you have your programming hero, and you want to maybe you know
[2380.48 → 2384.70] for some you might just have a problem you want to solve like for example what Steve and Andrew were
[2384.70 → 2389.86] mentioning earlier but how do you how is this breaking down the barrier breaking down the wall of
[2389.86 → 2396.72] actually getting to pair with your programming hero um well I think you know the ideal scenario for me is
[2396.72 → 2404.34] is maybe that programming hero um puts out a pair with me badge um or puts you know tweets pair with me
[2404.34 → 2412.86] and you say hey can I do it, and they're like sure um you know I think that's kind of the ideal scenario
[2412.86 → 2418.18] because it's its the lowest barrier to entry for somebody who might feel a little nervous about asking
[2418.18 → 2425.66] um but um you know in general like I'm sorry go ahead well I was going to say it's a lot easier when
[2425.66 → 2430.64] you're invited than if you're trying to you know come knock on the door of a stranger kind of thing
[2430.64 → 2437.32] yeah but I mean something else that I'm trying to encourage yeah if you know something else I'm trying
[2437.32 → 2444.96] to encourage is just to is that I think I mean I could be wrong in this um one of the questions that
[2444.96 → 2451.32] I've asked people when I've talked about this is you know basically if somebody came to you and said
[2451.32 → 2457.44] hey I really like what you're doing I love what you're doing with project x um could we pair sometime
[2457.44 → 2464.76] um I ask that question and I usually see a lot of uh or I ask if you know what would you say to that
[2464.76 → 2471.00] would you say yes to that and I usually see a lot of hands go up when I ask that question um you know i
[2471.00 → 2475.36] think that that most people are pretty open to this kind of thing, and so I think that if you have
[2475.36 → 2481.40] some way of reaching that programming a hero of yours uh if you know is they put their contact
[2481.40 → 2487.10] form up somewhere or if they make their email address available uh or uh if they're just out there on
[2487.10 → 2495.36] twitter or something if I think you know if you politely say hey i I really like what you're doing
[2495.36 → 2500.26] with such and so um do you think we could uh you know do you think I could pair with you sometime
[2500.26 → 2506.58] you know the worst thing that can happen is they ignore you yeah it's true though because I think
[2506.58 → 2511.22] that the fear of your you know people are afraid of the program they're you know whoever they would
[2511.22 → 2515.96] consider to be one of their heroes, and it's probably this self-made you know delusion that you
[2515.96 → 2520.66] have that they're gonna you know treat you like you're an idiot, and it's kind of the whole crux of
[2520.66 → 2526.16] open source, and it's kind of what we preach to people is you know just ask because the community
[2526.16 → 2533.94] while there is you know and again I've seen this far too often where somebody will commit an um
[2533.94 → 2539.28] pull request to some you know repository and say hey this is something that I would like to do what
[2539.28 → 2542.64] do you think and they just get a response like this is stupid you're doing it wrong and it
[2542.64 → 2547.42] gets closed that does happen obviously it's unfortunate, but it does happen, but that's not the
[2547.42 → 2552.86] norm right normally when you submit something even if it is something that's pretty
[2552.86 → 2558.74] you know questionable the responses you'll get typically will be more like okay well did you
[2558.74 → 2563.98] think about trying this way this is what we tend to your know to say is a better solution to that
[2563.98 → 2569.02] problem and that's the norm right, so people are afraid of submitting their code people are afraid of
[2569.02 → 2572.02] the world seeing their code because they're afraid of the response they're going to get
[2572.02 → 2577.02] typically that response is a lot more positive than what they expected, and it's more
[2577.02 → 2582.64] encouraging than anything to get you to contribute more code so when people finally break the wall
[2582.64 → 2587.22] down and start contributing to open source you find that their contributions jump because they
[2587.22 → 2591.94] they get encouraged about the response they're getting rather than fear of being treated poorly you
[2591.94 → 2598.26] know right yeah and something that i kind of want to get into doing more is um you know if is i
[2598.26 → 2603.48] just don't have time or if I've got a huge backlog um I'd like to actually do more sort of referring
[2603.48 → 2610.00] people out you know I'd like to if nothing else be kind of a nexus where people can say hey can I
[2610.00 → 2614.56] pair with you and I'll be like uh well i I really can't right now and I've got a huge backlog of pairing
[2614.56 → 2620.32] requests but here's somebody else that you might enjoy pairing with so I guess that kind of
[2620.32 → 2625.92] brings us to a good place then pair program with that me so it's a rails' app which you know for what it
[2625.92 → 2633.22] is might be a little heavy-handed but um yeah does is that is there a future is there would you like
[2633.22 → 2637.44] to see something like that maybe like an I don't know like a queuing system or something where you
[2637.44 → 2644.08] can maybe say hey I'm available right now and um then somebody else can come and say okay this person's
[2644.08 → 2648.36] available let me ask them like is there anything like that you would like to see there are a
[2648.36 → 2653.88] bunch of young sites out there um along those lines and I've tried to list most of them on pair
[2653.88 → 2663.44] program pair program with dot me see I have trouble saying it too um uh and I don't know like
[2663.44 → 2668.96] so the idea I mean the idea with the site is basically to be kind of a community-owned thing i
[2668.96 → 2673.10] mean i most of the stuff that's happened since I put it up has been uh pull requests that people
[2673.10 → 2680.68] submitted to me um and I think um you know I've definitely talked to some of the people that are
[2680.68 → 2688.48] involved with it about something along those lines uh I have some concerns about uh that it would
[2688.48 → 2692.44] be easy to make something that actually wasn't that you wasn't as useful as it seemed like it would be
[2692.44 → 2701.36] um I know that I don't want to get into the rabbit hole of like scheduling because that's a huge mess
[2701.36 → 2708.54] um and I'm a little concerned like I wouldn't what I don't want to do is build a system that winds up
[2708.54 → 2715.18] sort of reinforcing um circles like you know you were talking earlier about sort of the like the
[2715.18 → 2720.40] circles of experts you know all pairing with each other um, and you know I wouldn't want to sort of
[2720.40 → 2728.24] reinforcing that um or kind of leaving people out in the cold if they put just the wrong tags
[2728.24 → 2734.16] in their post or something like that so I think it is requires a lot of thought um to be
[2734.16 → 2741.76] genuinely useful but um i certainly you know i I do expect that site to kind of expand and offer
[2741.76 → 2746.94] more features for you know more ways of finding people to pair with as time goes by
[2746.94 → 2753.18] so then you're kind of leaving it open right yeah it's a true open source project you very, very open
[2753.18 → 2757.54] it's not it's not like I have a master plan for that site I have a know milestones or anything
[2757.54 → 2764.30] like that um you know the idea was I wanted to get the idea out there first and I wanted to then you
[2764.30 → 2769.48] know and attract some people to the cause, and you know see what you know what other people felt
[2769.48 → 2773.92] like would be the most useful things to have there like I think pretty soon um uh there's going to be
[2773.92 → 2779.76] it's a small thing but I'm going to put like a little widget on there that um shows all the people
[2779.76 → 2785.96] tweeting with hashtag pair with me um so at least you can go there and see like who's available right now
[2785.96 → 2792.12] yeah I think that's good I think we know while the trend in open source has been to kind of have
[2792.12 → 2796.88] that you know BNFL on each project and that's that's neat and all for somebody to have this master
[2796.88 → 2800.56] vision and this is where the project's going to go and I'm just using the open source community to
[2800.56 → 2805.70] leverage other people to help me get it in that direction that's that's cool you know that that's
[2805.70 → 2810.66] definitely a useful you know one of the many applications of open source but I think what's what's even
[2810.66 → 2817.82] more uh unique and what I think should what I would like to see grow is the idea that I'm just
[2817.82 → 2822.06] starting this ball moving and I want to see the community get behind it and take it wherever it
[2822.06 → 2828.56] wants right and for me the idea is I want the idea to always be paramount I mean the
[2828.56 → 2835.92] the site is incidental uh the site exists you know it exists to support the idea, but ultimately it's i
[2835.92 → 2839.74] don't want this to become like a technological problem to solve it's not a technological problem to
[2839.74 → 2845.90] solve it's a cultural problem right it's a cultural opportunity it's a cultural opportunity
[2845.90 → 2851.62] to enable technical problems being solved yes you know you said the word culture there and I'm we
[2851.62 → 2857.48] Andrew mentioned this might have mentioned this earlier but uh so we he and I work in a distributed
[2857.48 → 2863.02] team at pure charity, and we have a back channel it's also known as our hip chat so our actual
[2863.02 → 2869.38] water cooler at pure charity serves as a water cooler here for this show for those that work with us
[2869.38 → 2873.26] actually listen to the show but uh Beverly nelson I think you might know her, but she mentioned
[2873.26 → 2879.52] in our chat room she said 80 of her friends at ruby friends uh is about bringing them into the
[2879.52 → 2883.12] culture not so much the code and I think there's a lot of magic to what you know she said and you
[2883.12 → 2888.24] guys are talking about culture there I think it is becomes not so much uh oh I know ruby well you
[2888.24 → 2893.76] know better than you, or you know I've got more experiences it's really about just getting
[2893.76 → 2900.64] involved you know regardless of your level of activity and whatnot but just jumping in and
[2900.64 → 2905.62] that's probably the hardest part too about open source is you there's this huge intimidation
[2905.62 → 2910.50] that you have a bunch of assumptions before you're involved that this is how it's going to be, and it's
[2910.50 → 2916.22] not at all really how it is, and we're a lot more uh friendlier than people might think, but you know i
[2916.22 → 2921.24] think that's the hardest part is just you know breaking the ice something that I'm I've started
[2921.24 → 2929.72] uh doing uh which I hope will help with that um is I started putting some of my pairing sessions up on
[2929.72 → 2937.14] uh google hangout uh google hangout on air yeah so um and I didn't really like to announce it or anything
[2937.14 → 2941.46] i just I would be working with someone I'd be like hey do you mind putting this make putting this up as
[2941.46 → 2946.86] a hangout on air and then whoever happened to be around could like tune in and watch us and i recently
[2946.86 → 2955.12] did one of these um actually with one of my co ruby rogues just josh Sussex um and put it out there
[2955.12 → 2960.22] and got a lot of perfect feedback from it and i I think some of the feedback that I think that was
[2960.22 → 2970.32] most interesting for me was kind of the like um the way watching it kind of took the magic
[2970.32 → 2977.64] out of it like you know took the that aura of you know the thing that those coders do is different
[2977.64 → 2986.06] from what I do um, and you know I think that if we maybe is is is i and maybe others put some more of
[2986.06 → 2992.42] our pairing sessions up like that um other program programmers can look at it and say oh wow that you
[2992.42 → 2997.34] know basically the stuff they do is the same stuff that I do and they make the same boneheaded
[2997.34 → 3002.82] mistakes, and they sit waiting for their tests to pass and you know and sometimes
[3002.82 → 3010.24] they spend an hour and write three lines of code and um, and it's not you know there's nothing magical
[3010.24 → 3015.98] about it there's nothing unique about it um we're you know we're all just doing the same stuff
[3015.98 → 3022.08] I think that's kind of something that Steve said uh not so much said with his words but
[3022.08 → 3026.02] that we're all doing the same stuff Steve didn't you um for a while there weren't you
[3026.02 → 3031.90] viewing if that's the word um like basically just you hack him by yourself, but you were just
[3031.90 → 3036.56] hacking on hacking I believe, and you were sharing that on Vimeo and people are watching like oh yeah
[3036.56 → 3040.36] he does the same thing I do, or you would actually have your own commentary in there, and you were just
[3040.36 → 3045.96] talking to yourself yeah it was with hilarious results so I didn't I didn't fully appreciate how
[3045.96 → 3051.34] to properly mix my audio or I didn't notice that the audio was mixed poorly and so there 's's
[3051.34 → 3058.32] one of me fixing a bug in ruby gems um with like Kesha louder than my voice so I didn't provide
[3058.32 → 3064.48] commentary, but instead it's just blasting I wasn't sure I thought it was something hilarious too but
[3064.48 → 3069.72] I was yeah it was pretty good so i I would like to get back to doing a little bit of that but um
[3069.72 → 3073.46] you know i just it's just one of those things where I did it a couple of times, and it was fun and
[3073.46 → 3077.40] people liked it and I just haven't done it since because I haven't done it since not because of any
[3077.40 → 3082.14] specific reason so sometimes you have to break the mould man you know just do them a little
[3082.14 → 3086.48] different you know don't follow the same rhythm in the rhyme it's also just funny because you're
[3086.48 → 3090.42] like when you're like recording your screen you're always like terrified that something is going to
[3090.42 → 3095.22] happen like what am I going to type or am I going to get like an I'm message that should be private or
[3095.22 → 3101.38] like you know how is this going to work out so that's also real fun too um but uh yeah you know i
[3101.38 → 3104.88] mean I think it's good uh just in general that was what I was trying to show with ruby gems is that
[3104.88 → 3110.92] like you know ruby gems is a particularly terrible code base due to its history etc and so uh you
[3110.92 → 3114.38] know watching like here's how I tackle this kind of bug you know you could totally do it too was
[3114.38 → 3118.68] definitely like the point of that I was like I don't do anything but just run the tests and cuss
[3118.68 → 3124.92] over and over and over again I can't imagine if I'm pairing with somebody and I am from my wife
[3124.92 → 3129.34] pops up reminding me to get the rash cream or something that would probably be the worst thing ever
[3129.34 → 3134.64] seems bad I just noticed somebody might think that you're human or something
[3134.64 → 3139.26] yeah yeah I don't want that man they are supposed to like I'm supposed to be a demigod of programming
[3139.26 → 3145.44] or something to them uh just kidding hopefully everyone knew that uh on pair program with dot
[3145.44 → 3151.76] me I just noticed the header you say pair widely pair often is that an uh shout out to the idea of
[3151.76 → 3157.90] wide teams a little reference to wide teams there that's the second uh last week we had docker on and
[3157.90 → 3162.66] they had a number they had their on their frequently asked questions they went numbers one two three four
[3162.66 → 3168.80] five and then to 42, so this is the second little uh nugget I found in the uh products you're so
[3168.80 → 3171.38] you're so keen man you know that's right
[3171.38 → 3180.40] so confident ruby another book that you are writing still I mean it's in betas I mean you're
[3180.40 → 3187.02] still writing it's in beta which means that I've pronounced it content complete um after taking
[3187.02 → 3194.38] Kent beck's advice to get it to 150 pages and then just stop um and so it's I'm still editing the
[3194.38 → 3202.88] crap out of it but um, but it's content complete and this book um again stemmed from a talk that
[3202.88 → 3209.88] you've been giving yeah um actually I think it was the first talk I wrote um which I called confident
[3209.88 → 3221.18] code and uh it's its all about writing methods that tell a coherent story uh sort of narrative
[3221.18 → 3228.90] style of writing methods is how I think of it and a lot of that involves uh writing code that
[3228.90 → 3235.62] uh sort of confidently progresses forward without a lot of tangents and diversions and provisos because
[3235.62 → 3241.66] of uncertainties about input or uncertainties about errors that might occur um and just uh it's
[3241.66 → 3247.32] basically a patterns book, and it's a book of patterns um that are strategies for making your
[3247.32 → 3253.36] code more confident for you know telling those stories uh more coherently uh, and you know isolating
[3253.36 → 3260.30] isolating the error handling and dealing with input in such a way that you don't have to be
[3260.30 → 3265.46] uncertain about it in the midst of the method and stuff like that yeah it's an uh where can you
[3265.46 → 3270.00] where I couldn't find it anywhere other than on your uh on your store is there anywhere that if you
[3270.00 → 3275.36] go if you go to confident I think if you go to confident ruby.com you'll actually I think
[3275.36 → 3282.06] that'll redirect you to the blog post where I first introduced it um and so that's probably the easiest
[3282.06 → 3289.16] way to get to it uh you can also find announcements about it on my blog which is devblog.avdi.org yeah
[3289.16 → 3292.68] we'll uh we'll have this I found the link we'll have the link in the show notes for those of you
[3292.68 → 3298.66] listen to the podcast head to five by five dot TV slash changelog slash 90 to see all the show notes
[3298.66 → 3306.90] and links and everything else so don't be lost so um avid what are your speaking uh engagements
[3306.90 → 3311.00] planned for the future that you already have set up I keep meaning to put together like a
[3311.00 → 3317.68] an actual list of them um let's see uh next one up I know is going to be um
[3317.68 → 3333.12] um uh yeah name god uh the one in DC Arlington not, not yeah uh yeah the one oh gosh it's uh
[3333.12 → 3338.88] oh uh ruby nation thank you funny my mind wanted to be like nation ruby and
[3338.88 → 3349.26] then I was like no that's not right um yes ruby nation um and uh in just like a couple of weeks
[3349.26 → 3356.08] and speaking of ruby nation you gave this confident code talk there too yeah I guess I did um i I'm
[3356.08 → 3364.14] doing an I believe I'm going to be doing a talk on uh, uh coding and joy basically uh little
[3364.14 → 3370.70] bits of ruby that just make me happy uh this time around so um yeah that'll be fun and then uh after
[3370.70 → 3377.82] that um several others I think uh well I'm going to be going to Pittsburgh steel city ruby um love
[3377.82 → 3384.22] Pittsburgh woo stack Adam is from Pittsburgh yeah originally born and raised in the Pittsburgh area
[3384.22 → 3391.18] so that's uh Steve where are you at I mean I live in Santa Monica now but um i I lived in Pittsburgh
[3391.18 → 3396.46] my entire life before moving to Los Angeles so there you go I thought so everyone
[3396.46 → 3401.64] on this chat has some connections to Pennsylvania that that has happened in pretty much every chat
[3401.64 → 3408.72] that I've ever had I found it's weird it's six degrees of Pennsylvania yeah so you'll be a steel
[3408.72 → 3417.68] city ruby um when is that on the date that it is on yes yeah august middle august sometime awesome
[3417.68 → 3426.12] so for those of you who are uh new to the show and those of you that have listened you'll know
[3426.12 → 3433.38] uh we ask all of our guests these two questions um the first one Audi is for a call to arms and i
[3433.38 → 3439.16] guess in this case you could give us a specific call to arms for pair program without me if you want
[3439.16 → 3445.12] yeah or uh just kind of what you would like to see the community do around this i I don't think it's
[3445.12 → 3450.30] going to come as any surprises at all it's its just gone out there and pair with each other go you
[3450.30 → 3457.20] know go ask um if you have somebody that you've always wanted to you know learn from go ask them
[3457.20 → 3463.80] if you have some time in your day uh you know that you would be working on open source or something
[3463.80 → 3469.32] anyway put that welcome that out there put that badge on your blog put the know hashtag pair with
[3469.32 → 3475.26] me on your Twitter feed if you do the twitters um make yourself available I think you'll find it
[3475.26 → 3483.98] incredibly rewarding to pair widely pair diversely um pair more often how do you feel about pairing on
[3483.98 → 3489.42] more conceptual like if somebody's a python developer, and you don't have python experience
[3489.42 → 3495.34] pairing conceptually on an idea how do you feel about that I think it still totally works uh just the
[3495.34 → 3502.44] other day uh I paired with somebody on some dot net code some c sharp code and granted um I have
[3502.44 → 3508.44] done c sharp before, but it was years and years ago and I was totally rusty uh, and it didn't matter i
[3508.44 → 3513.56] just basically i had them be the driver uh that could have worked either way, but it worked
[3513.56 → 3517.58] that was nice just because they already had their whole environment set up, and they had their IDE and
[3517.58 → 3522.86] they knew the key bindings, and you know how to make the test go and stuff like that um, but it was fun
[3522.86 → 3529.12] because I actually got to teach them something about uh something about c sharp um not because I knew it
[3529.12 → 3540.46] but because i just sort of like basically um figured that a particular um the library call had to exist
[3540.46 → 3547.66] and looked it up until we found it, and basically it was using a more functional approach to
[3547.66 → 3552.54] solving a problem than they were used to maybe as an attachment to your call of arms I have a
[3552.54 → 3557.30] couple ideas and I can share with you on the fly maybe um start a wiki page for those who
[3557.30 → 3564.38] on uh the ppm repo you have on your offer user maybe a wiki page that says hey I'm open for pairing
[3564.38 → 3571.72] and or moving this to an org and maybe having just a project for issues where you can kind of allow
[3571.72 → 3578.60] issues to coordinate the community potentially just an idea yeah yeah that's a good thought actually we've
[3578.60 → 3584.82] we have started using the wiki a little bit uh on the GitHub page for it got you it says
[3584.82 → 3593.70] welcome to ppm I'm just messing with you man just uh one thing I did want to give a shout-out this is a
[3593.70 → 3600.46] community project but um at the bottom I noticed you said the design was done by Chris Radford and the
[3600.46 → 3606.08] badge was done by uh David browning so kind of wanted to give them a little bit of yes a shout-out for
[3606.08 → 3612.08] getting in on this thing early with you yeah yeah um, and they totally deserve it um much uh gratitude
[3612.08 → 3618.82] to both of them and to everybody who's submitted a pull request all right and our last question if you
[3618.82 → 3625.54] could name a programming hero or again somebody in the idea of distributed workplaces or wherever you
[3625.54 → 3635.46] might think what would who would you say your hero would be um so I could obviously name any number of
[3635.46 → 3642.64] amazing programmers that have influenced me and that I look up to uh but I think I want to give a shout
[3642.64 → 3651.96] out to Angela harms um because she's she's been doing some talks in the ruby community lately well
[3651.96 → 3657.24] in the programming community lately not specifically the ruby community she's she's uh I guess maybe more
[3657.24 → 3664.32] um part of the agile community you could say um that's I think that would be her background but
[3664.32 → 3672.10] seems right yeah um, and she has been she talks to programmers about compassion
[3672.10 → 3681.90] and she does it in a way that's that's effective and um you know really uh is eye-opening and um I think
[3681.90 → 3689.08] heart opening and I think that's wonderful and I think it's much needed uh so, so yeah I'm going to say
[3689.08 → 3696.58] Angela harms uh did she I want to like I remember there was something like a radical something that
[3696.58 → 3702.12] she did or that I remember seeing her name on I'm actually not sure of like any of the I don't recall
[3702.12 → 3707.18] any of the specific titles of her talks radical love or something like that but yeah no i definitely
[3707.18 → 3714.66] have um well it's not radical love.org it's that org it's something that she did but yeah uh or at least
[3714.66 → 3720.84] I remember hearing her name with but i I agree with you, I think that there's something inherent
[3720.84 → 3729.44] that we need to see in this community, and it's its it's the idea of like I don't know just acceptance
[3729.44 → 3735.76] of people in this community, and you can get bogged down and what you know the ruby drama or whatever we
[3735.76 → 3741.04] we call it where um you just you get on, and you follow some of the big names in the ruby community
[3741.04 → 3746.50] and is there can be a lot of name-calling and a lot of just trash going back and forth and I don't
[3746.50 → 3750.76] know if maybe that's what you're hinting at but I would like to see less of that and more of just
[3750.76 → 3755.78] people generally respecting each other in the community well you know not just a ruby thing
[3755.78 → 3761.78] it's just a programmer thing in general I think um we have a culture that's very rationality
[3761.78 → 3768.04] centric uh very logic centric um you know very often I think yeah in theory we believe it to be
[3768.04 → 3774.22] um and of course we also believe ourselves to be very logical um and I think a lot of you know a lot
[3774.22 → 3779.76] of times uh you know we think that solving a problem boils down to being the most rational
[3779.76 → 3786.08] person in the room uh and I think the stuff that she's talking about will challenge that and I think
[3786.08 → 3792.68] it'll challenge that in a good and important way yeah that is true I mean I think it begins with uh
[3792.68 → 3798.68] it begins with you right it begins with us uh as an individual to be different and to act
[3798.68 → 3808.88] differently so um don't be a hater repeat after me, we are all different somebody's gotta we're all
[3808.88 → 3815.64] yeah somebody's got uh nobody uh the response is I'm not
[3815.64 → 3823.50] that'll be some python fans in the audience at least and hopefully somebody will get it I don't
[3823.50 → 3823.64] know
[3823.64 → 3833.08] this has certainly been a definitely been a fun chat AVI I definitely appreciate you taking the
[3833.08 → 3837.64] time to come on the show it's its a fun conversation uh you're always invited back
[3837.64 → 3841.64] certainly appreciate all that you're doing in the community and what you've done with uh
[3841.64 → 3847.22] pair programming and just lifting that up and sharing what that can be and just starting the
[3847.22 → 3852.84] movement as Andrew mentioned before and uh definitely thanks to Andrew and Steve for coming
[3852.84 → 3857.84] on the show what a great show you guys uh put on today, and thanks to you for the listeners
[3857.84 → 3863.40] out there listening live this show does broadcast live every Tuesday at uh at 5 p.m central standard
[3863.40 → 3869.20] time here on five by five if you want to check out back our backlog you can go to five by five dot TV
[3869.20 → 3874.98] slash changelog this is episode number 90 so uh you definitely enjoyed it but let's close this
[3874.98 → 3880.48] out and say goodbye see you all later bye bye
[3899.20 → 3899.70] you
