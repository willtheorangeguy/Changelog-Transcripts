[0.00 --> 13.50]  welcome back everybody this is the change log where members support a blog and podcast
[13.50 --> 18.06]  that covers what's fresh and what's new in open source this show is hosted by myself
[18.06 --> 23.84]  adam stakovic as well as andrew thorpe say hello hey how's it going and we're also joined by our
[23.84 --> 29.42]  fellow changelogger steve klavnik hey everybody and you can tune in live to this show
[29.42 --> 34.38]  like like you can today it's tuesday at 5 p.m central standard time right here on five by five
[34.38 --> 39.60]  you can check out the past shows we've recorded at five by five dot tv slash changelog and this
[39.60 --> 46.58]  is episode 90 and we're joined by avdi grim maker of pair program with me and ruby extraordinaire
[46.58 --> 51.46]  welcome to the show avdi how are you i'm doing great thanks for having me so where do we where
[51.46 --> 56.08]  do we kick off this call i mean i know we got kind of a huge docket of things to talk about um maybe
[56.08 --> 62.58]  for the uninitiated somewhat introduce yourself you're a podcast yourself a writer and all sorts
[62.58 --> 71.76]  of stuff where do we begin with you uh well i'm i'm a hacker um i'm a hacker that's me yeah uh i'm a
[71.76 --> 79.32]  hacker i've been uh working a lot with ruby for the past several years many years um but uh
[79.32 --> 85.34]  i don't know what else you want to know i'm a family guy i've got lots of kids and why don't
[85.34 --> 90.10]  you give us a little bit of insight into some of the work you've done uh with wide teams and ruby
[90.10 --> 95.50]  rogues and that kind of stuff okay so um yeah that's the uh i guess the broadcaster side of my
[95.50 --> 103.74]  my life um i have been doing a podcast of my own for the past few years uh it's called wide teams
[103.74 --> 112.06]  it's at wide teams.com and it is dedicated to disperse teams uh remote workers people that are
[112.06 --> 115.76]  working geographically removed from the other people that they're working with
[115.76 --> 123.86]  and the goal there has just been to kind of collect stories from people find out how people are working
[123.86 --> 128.88]  on dispersed teams and you know what special strategies they have to make it work and what
[128.88 --> 132.54]  tools they're using and what they like about it what they don't like about it all that stuff mainly
[132.54 --> 138.22]  just to sort of um you know connect people like that and and uh you know help us learn from each
[138.22 --> 143.06]  other because i was working remotely and and there just didn't seem to be a lot of resources when i got
[143.06 --> 153.20]  started yeah those resources um are kind of plentiful now and i remember you know two years ago ish when i
[153.20 --> 159.76]  started my full-time remote job it was it was difficult to find any kind of um you know resources out there to
[159.76 --> 165.06]  help me just know like what would make my life easier right so looking at some of the stuff you've
[165.06 --> 171.86]  done um you know with wide teams specifically um and now you know even a little bit more with
[171.86 --> 177.70]  with the idea of pairing and and remote pairing and things like that man it would be nice to uh
[177.70 --> 184.28]  to have these resources at my disposal when i first got started a few years ago um i love the name
[184.28 --> 188.58]  man wide teams is such a perfect name for distributed teams i mean where did you come up with that
[188.58 --> 195.32]  thanks uh same way i come up with with anything else all the all my name naming ideas i go for a long
[195.32 --> 201.44]  walk go for a long walk what about uh what about your your your twitter bio how many questions you ever
[201.44 --> 210.10]  get about that i mean do people think you're a demon or a daemon um yeah so that's uh uh 80 angel 10
[210.10 --> 215.90]  demon and the rest is is hard to explain um that actually i don't know if anybody's ever asked me
[215.90 --> 223.64]  about that but um it is a reference to an over the rhine song um first year and uh i stuck in the
[223.64 --> 229.10]  sort of the unix spelling of demon just you know because nerd see i was i was thinking you were really
[229.10 --> 233.18]  just playing on the fact that you know what a daemon is but then you were hoping that maybe nobody else
[233.18 --> 240.22]  did but anyways so the the resources on why team so you started this podcast how long ago
[240.22 --> 246.30]  uh i you know i'm not even sure i'd have to i'd have to look but it was a couple years ago
[246.30 --> 252.38]  um actually probably more than a couple now yeah we're on you're on episode 81 now so
[252.38 --> 258.16]  however long ago it was you've definitely uh you've definitely gone into the depths of distributed
[258.16 --> 262.42]  teams with some of these people here i see here on the front page front page you have ernie miller
[262.42 --> 271.38]  of living social um heard i got a chance to hear him talk at uh i want to say it was ruby oh
[271.38 --> 278.74]  it was big ruby conference in grapevine texas and he talked about this he talked about the idea of um
[278.74 --> 286.54]  you know what it what does it mean to be happy in your job and you know it's not money it's not uh
[286.54 --> 290.00]  you know he even he even went as far to say it's not the people you're working with because
[290.00 --> 294.98]  you'll find people that that you love to work with at a lot of places and right to him what he said
[294.98 --> 300.88]  that the the absolute most important thing about being happy your job is is being happy at your job
[300.88 --> 304.72]  wherever that might be whether you're driving working from home you know whatever it is and he's
[304.72 --> 310.30]  obviously you know a remote worker for living social and so he was saying you know kind of what
[310.30 --> 315.36]  we're going to echo here today which is that like if possible the idea the ability to work from the
[315.36 --> 320.60]  comfort of your own home is is tremendous and you you kind of hit on it uh when we chatted a little
[320.60 --> 325.26]  bit earlier avdi with you know you love that you can work from because you that means unlike the
[325.26 --> 332.02]  traditional you know business mindset that comes out of the great depression and on in america we as
[332.02 --> 337.44]  you know as as workers as people that are in the workforce get to spend more time with our family
[337.44 --> 344.02]  and that to me that's something that makes up for any level of you know financial compensation that you
[344.02 --> 350.74]  can find yeah yeah it's a huge deal and it's exactly you can't really um you know you can't
[350.74 --> 355.26]  really count it up in in monetary terms but here's a question for you maybe to kick off this conversation
[355.26 --> 363.24]  are you a are you part of a distributed team right now uh i can't really say that i am so i mean i was
[363.24 --> 370.42]  part of many different distributed teams for years but uh my job has recently changed um kind of
[370.42 --> 378.40]  dramatically my job description is now i guess uh screen screencaster uh primarily uh because i i
[378.40 --> 384.12]  launched ruby tapas which is my my screencast service and that's awesome um and it became popular
[384.12 --> 390.82]  enough that i was able to devote myself to it full time so um that's kind of a a one-man gig
[390.82 --> 398.22]  so i'm not i'm no longer you know working with other freelancers on a job or you know working as part of a
[398.22 --> 403.42]  distributed startup or you know any of the other things that i've done yeah so for those of you
[403.42 --> 410.02]  that don't know ruby tapas and you can go to it at rubytapas.com um the description of it like many
[410.02 --> 417.14]  of your projects is just perfect and it's short screencasts of gourmet ruby um and yeah it's awesome
[417.14 --> 423.20]  and so these are some you know some great resources it's very very affordable i highly recommend them
[423.20 --> 428.96]  uh my question is how much of an influence did ryan bates and uh railscasts have on you when you
[428.96 --> 434.74]  were starting this well i mean uh people like ryan bates you know i mean well particularly ryan bates
[434.74 --> 441.60]  really broke ground um i mean he's a pioneer yeah i mean i i think the the influence there is
[441.60 --> 449.48]  is the fact that he could you know that he was there and um just made it clear that it's possible to
[449.48 --> 455.80]  to do a professional screencast you know and to do that as your job uh you know him and and um
[455.80 --> 463.76]  and others uh i suddenly had a brain fart but uh somebody help me out here um well ryan i think he
[463.76 --> 468.18]  was a pioneer in terms of like just leading the way i mean he was one of the very first at least in
[468.18 --> 473.42]  the ruby spectrum doing screencasts and he did it very simply right like he was just breaking ground on
[473.42 --> 479.18]  how simple it was he had this de facto template for all of his you know all of his screencasts and i think
[479.18 --> 485.50]  he'd even gotten uh ruby hero in 2009 not so much for that but just his impact to the community
[485.50 --> 491.30]  right yeah to kind of hit on a few other ones that you may have heard of you got peep code um yeah
[491.30 --> 498.82]  absolutely rails best practices and rails tutorial.org those guys so and gary's destroy all software
[498.82 --> 506.72]  existed as well exactly my short my short-lived project uh watch.steve which no one forget no one
[506.72 --> 510.48]  knows about which is amazing that's what i always tell people is like if you're gonna try something
[510.48 --> 516.10]  try it because if you fail no one will ever know or remember anyway so like i totally did this a
[516.10 --> 520.52]  couple years ago and no one cared and so it disappeared off the face of the internet and now
[520.52 --> 524.16]  no one knows so gary bernhardt was a big inspiration for me as well
[524.16 --> 533.62]  cool cool yeah this is it's cool i mean to see so you're not i don't know how what's the best way
[533.62 --> 540.44]  to say this the to to do screencasts to get to some level of um you know credibility credibility is the
[540.44 --> 545.64]  right word but but at some point you have to prove to people that like the the code you're writing is
[545.64 --> 551.42]  is good code you know what you're doing is quality stuff and you call it gourmet ruby so what do you
[551.42 --> 556.78]  think it was that because for me i think the first time that i ever heard of uh avdi grim was probably
[556.78 --> 565.08]  when i read um exceptional ruby which is a tremendous book um thank you how how do you think what do you
[565.08 --> 569.38]  think kind of gave you a little bit of that credibility the the the i don't know if notoriety
[569.38 --> 576.04]  is the best word but just the ability to go out and um start to sell your what ultimately isn't even
[576.04 --> 580.80]  necessarily a product it's a you're sharing knowledge so what do you think got you to that point
[580.80 --> 584.82]  it's just an incremental process really i mean i think it's probably similar for anyone you know
[584.82 --> 591.18]  you start to write things here and there i started to blog um you know a while back long around 2006
[591.18 --> 596.66]  or 7 and um you know i found that that people seem to like some of the stuff that i wrote and
[596.66 --> 602.10]  eventually i got around to to doing a talk or two uh and that's where exceptional ruby came from
[602.10 --> 606.20]  was i did a talk and then i was like wow i've done all this research about exceptions uh it'd be cool
[606.20 --> 612.64]  if i could kind of you know recoup some of the time somehow uh so i turned it into a book um and
[612.64 --> 616.38]  people like that too you know so it's really just like you know the confirmation of the market you
[616.38 --> 620.38]  know people buy something people don't seem to hate it people don't like you know ask for their money
[620.38 --> 625.56]  back and they actually say say nice things about it and eventually um eventually it kind of
[625.56 --> 631.28]  breaks through my assumption of of i'm just another dumb programmer that maybe you know some of the
[631.28 --> 637.38]  stuff that i have to say not everybody knows before we get into the uh what i think the the
[637.38 --> 641.30]  meat of the show is going to be with pairing uh i have a question for you what do you think about
[641.30 --> 648.20]  what are your thoughts on being a uh exceptional master what are your thoughts on exceptions as control flow
[648.20 --> 657.42]  i'm not a fan when you when you so you would you do exceptional ruby as a talk before you actually
[657.42 --> 663.34]  wrote the book or no yeah i did yeah okay so would you get that question often when you would talk on
[663.34 --> 669.50]  exceptions uh i think a few people probably ran that by me um i think um i did make a point if i
[669.50 --> 675.06]  recall correctly i think i made a point of including catch and throw even in that talk um and i was
[675.06 --> 680.12]  actually i got to uh i got to use that that transformation just the other day i was working
[680.12 --> 686.36]  on the discourse code base and i submitted a pull request converting um an exception used as a as
[686.36 --> 692.54]  as control flow into a throw and catch uh which is sort of the approved ruby way of doing that
[692.54 --> 699.42]  right right cool yeah that's i think that i don't i think that might come out of my java days back in
[699.42 --> 705.52]  college but that's a question that i i think i've had many long arguments with a non-local so for a
[705.52 --> 709.66]  non-local return in a language that doesn't have you know something like throw throw and catch or
[709.66 --> 714.28]  continuations or anything like that um sometimes it's the only thing you can do
[714.28 --> 719.70]  yeah do we need to give some background to some of this context just for those who may not be
[720.58 --> 724.12]  uber ruby developers but want to kind of catch up with what this means
[724.12 --> 731.50]  yeah go ahead avdi why don't you explain um uh which part so you got exceptions what's what's this
[731.50 --> 736.56]  method of catching and throwing okay so uh a catch and throw in ruby is a construct that's actually
[736.56 --> 741.96]  very similar in implementation to exceptions it's it's another way of sort of tossing something up the
[741.96 --> 748.12]  call chain and it unwinds the call stack until it it gets to something uh that can catch it uh so it
[748.12 --> 752.64]  actually you know describing it it sounds a lot like exceptions and it is but it's specifically
[752.64 --> 758.50]  intended for non-exceptional cases it's specifically intended for the case where you want to you know
[758.50 --> 763.66]  just do an early termination but you need to kind of do it non-locally um the the circumstance that i
[763.66 --> 770.26]  saw this in most recently was a sax parser uh which of course is is hand you hand the parser off to
[770.26 --> 775.70]  or you you hand an event handler class that you write off to a parser and the parser then calls
[775.70 --> 782.34]  event methods on that event handler that you wrote um and at some point uh in this the one i was
[782.34 --> 788.04]  looking at they realized realized okay we're done now we don't need any more xml um but how are you
[788.04 --> 793.50]  going to tell the parser that uh there wasn't any way to tell the parser yet parser okay stop stop
[793.50 --> 798.52]  pulling data stop going through we don't need any more just end it here um and so they were using
[798.52 --> 802.68]  an exception they were raising an exception of the call stack and then catching it higher up
[802.68 --> 810.32]  um and uh using throw and catch is a bit nicer in ruby for that it's a it's it's cleaner it looks it
[810.32 --> 815.04]  actually looks better there's less code on the page you don't need to define a special exception just
[815.04 --> 820.00]  for for it because you're throwing a symbol instead of an exception it's just generally um better
[820.00 --> 828.68]  looking down into the rabbit hole adam yeah no i i'm i'm there with you i'm so right there with you
[828.68 --> 833.82]  honestly it's kind of neat though i mean because it seems like um it might have came about as like a
[833.82 --> 837.38]  hack but it's a good technique a good method and it's you don't really have any other way to get
[837.38 --> 843.20]  around it but it's a good way to use contracts and ruby to achieve your goal yeah well it's one of
[843.20 --> 847.44]  those cases that you you almost never need i mean i would hate to see a code base that was using them
[847.44 --> 850.40]  all over the place because that would be really scary it doesn't seem like it's the the most
[850.40 --> 855.32]  reliable way but every now and then you need to break through a layer of somebody from your software
[855.32 --> 859.50]  through a layer of somebody else's software back to your software again and that's where those you
[859.50 --> 864.70]  know sort of non-local terminations come in gotcha gotcha right and the the notion or the concept of an
[864.70 --> 870.44]  exception is very old it's not it's not anything new to ruby or anything so um but that that's an
[870.44 --> 875.34]  argument that's a debate that has been had for years amongst developers so i think i think throw
[875.34 --> 882.84]  and catch uh specifically i think they may have originated in like um a lisp uh like um scheme
[882.84 --> 891.50]  or something i'm not certain yeah cool so okay so to kind of get to the topic du jour um to keep up
[891.50 --> 897.72]  with the gourmet ruby oh yeah i caught that i'm with you uh okay so one thing we want to the thing we
[897.72 --> 902.76]  kind of want to get to is is pair program with me um and why don't you give us an introduction
[902.76 --> 909.54]  it's a like i i think the best way to describe it um abdi instead of calling it a product necessarily
[909.54 --> 914.46]  it's more of a movement or more of an idea yeah it is kind of building a community so why don't you
[914.46 --> 919.90]  give us some insight into what it is where we can find it and where you'd like to see it go okay well
[919.90 --> 926.12]  let me let me start off with a little bit of history um i've i'm a big fan of pair programming uh i'm
[926.12 --> 930.34]  gonna uh should i assume that most listeners are familiar with pair programming or should i introduce
[930.34 --> 934.50]  that uh why don't you go ahead and introduce it i would definitely say introduce it pair programming
[934.50 --> 940.60]  is the very simple idea of programming um right not programming so solo instead sitting down with
[940.60 --> 947.88]  somebody else and programming um so it's it's not exactly groundbreaking but uh uh it's part of it
[947.88 --> 955.74]  was part of the original extreme programming practices um and probably one of the most controversial of them
[955.74 --> 961.12]  uh you know partly i think because programmers like a lot of programmers like to think of them
[961.12 --> 968.24]  themselves as solitary beasts and uh partly because there was a perception that well if you take two
[968.24 --> 973.80]  programmers and you put them in front of one screen then you're going to have have your uh your project
[973.80 --> 982.62]  speed um and uh but it turns out that it's an incredibly effective technique uh for for many many
[982.62 --> 989.40]  reasons um you know number one it's kind of constant code review i mean code review has been found to be
[989.40 --> 995.46]  one of the most effective ways of avoiding bugs that we know of and pair programming is a way to always be
[995.46 --> 1003.10]  be code reviewing um it's a great way to retain focus i found that in when i'm pairing with someone
[1003.10 --> 1010.90]  i stay focused and you know i don't get distracted nearly as much um because you know who who no your pair
[1010.90 --> 1016.78]  probably doesn't want to pair with you on twitter right so you kind of feel like you know i should
[1016.78 --> 1020.76]  probably stay focused on the task at hand you don't know the kind of developers i pair with
[1020.76 --> 1026.32]  do you like you know pair every other word on careful and they could be listening
[1026.32 --> 1029.76]  write this
[1029.76 --> 1039.84]  um yeah uh you know so um it's uh one of the big benefits that i like about it is the effect on morale
[1039.84 --> 1045.84]  um you know i found that sometimes sometimes i'm having a bad day sometimes i'm working on a piece
[1045.84 --> 1050.50]  of code that just bums me out and i really don't want to touch it and i don't want to deal with it
[1050.50 --> 1059.30]  but i have to um and having uh somebody to deal to go through that with you can be a huge pick me up
[1059.30 --> 1068.52]  um and uh gosh there are so many good things about pairing pairing keeps you pairing makes you smarter
[1068.52 --> 1077.26]  um programming alone you can do some really dumb stuff i've found like um let me give you an example
[1077.26 --> 1086.98]  uh recently i was writing some working on some back-end code for ruby tapas and um i was basically
[1086.98 --> 1092.36]  trying to pull some data out of the shopfront service that i use a third third-party shop shopfront service
[1092.36 --> 1103.00]  uh called dbd and um earlier i had actually worked with them to to define and like um to get a a
[1103.00 --> 1110.12]  feature rolled out which was uh that you can sign up to the the ruby tapas videos as an rss feed in
[1110.12 --> 1115.64]  like itunes uh or miro or a bunch of other programs and i'd actually like worked with them on that i'd
[1115.64 --> 1122.18]  sort of laid down what the rss format should look like for it and all this stuff and and then i'd
[1122.18 --> 1127.34]  moved on so later on i was working on some back-end code and i was you know working alone not pairing
[1127.34 --> 1132.34]  with anyone and i was working on pulling data out of their website and it was just basically
[1132.34 --> 1138.92]  screen scraping because they don't have an api for this stuff yet and i had finished all this really
[1138.92 --> 1146.06]  complicated screen scraping code when i got into a conversation with somebody on twitter and about
[1146.06 --> 1151.50]  this the screen scraping code and they said something about well it can't be that hard parsing the rss feed
[1151.50 --> 1157.82]  to get that data back out and this huge light bulb sort of crashed down onto my head
[1157.82 --> 1168.10]  um as i realized that i had been sort of blindly screen scraping information that was in this rss feed
[1168.10 --> 1176.98]  that i had helped define that is the kind of stuff that happens when you program alone or at least when
[1176.98 --> 1182.44]  i program alone so it's not and it's it's not just that either i mean if you think like if you're a
[1182.44 --> 1187.38]  developer and think about you know oh i've solved this problem before and and i it's might not be the
[1187.38 --> 1191.26]  best most efficient way to do this but here let me just copy and paste this code well you're not going
[1191.26 --> 1196.94]  to do that if you have your colleague watching over your shoulder you know like and and just to kind of
[1196.94 --> 1201.22]  real quick in case to fill in a gap in case anybody doesn't understand the concept i don't think we
[1201.22 --> 1206.06]  actually said it but when you have two people in the same room pairing together typically there's
[1206.06 --> 1211.14]  one person that is actually sitting at the keyboard doing the typing right another person that's watching
[1211.14 --> 1216.22]  that's like you know looking over your shoulder you're talking about what you're doing he's watching
[1216.22 --> 1220.40]  what you're doing pointing out things as you do them if they're incorrect kind of a idea yeah and
[1220.40 --> 1224.16]  there are a couple of different i mean there are different models of it um you have sort of classic
[1224.16 --> 1229.54]  uh navigator driver pairing where basically the navigator is sitting back hands off the keyboard
[1229.54 --> 1233.18]  but they're actually doing most of the thinking they're telling the driver what to do what to code
[1233.18 --> 1238.32]  um driver is responsible for actually getting it onto the page making sure that you know they don't make
[1238.32 --> 1244.28]  too many typos and um you know hitting hitting the the button to run the tests and all that stuff
[1244.28 --> 1249.28]  um and the the navigator is kind of freed up to sort of wave their hands and think
[1249.28 --> 1257.14]  and maybe look up documentation stuff like that um and they may they may well switch off
[1257.14 --> 1262.74]  periodically um you know traditionally if if like the navigator ran out of steam they might
[1262.74 --> 1267.18]  switch around switch around and you know maybe the driver says oh i think i know i think i know what to
[1267.18 --> 1274.00]  do here and so they switch off uh and then there are other things like um ping pong pairing uh which is a
[1274.00 --> 1280.30]  a method of pairing that uh works well with test-driven development where uh basically one right
[1280.30 --> 1284.90]  one person will write a test and then the other person has to has to make it pass and then they
[1284.90 --> 1292.62]  they keep going back and forth like that um and um and sometimes it's it's you know less defined it's
[1292.62 --> 1299.28]  more organic it's just you know two people sitting there and and uh trading the keyboard off as as they
[1299.28 --> 1303.42]  see fit um some people actually set up desks if you're co-located they actually set up desks where
[1303.42 --> 1310.60]  there are two keyboards plugged into the um into the same machine and i've noticed that with remote
[1310.60 --> 1315.96]  pairing specifically the more organic style is what kind of seems to to fit and that we're we're
[1315.96 --> 1319.94]  talking to each other as we're looking at you know we're sharing it a screen with we mux or something
[1319.94 --> 1325.56]  and right as we're looking at that we're talking to each other and um you know we you kind of just
[1325.56 --> 1330.94]  have to get a feel for the other person and how the other person works and you know so me and some
[1330.94 --> 1336.30]  of my co-workers that as we do it uh if i if i notice something and and you know i know how this
[1336.30 --> 1341.28]  person works i know when it's appropriate for me to jump in and type something and to back out and
[1341.28 --> 1346.18]  it just kind of happens naturally for us so i think that tends to be what do you think that i think that
[1346.18 --> 1351.72]  tends to be more common with remote pairing i don't know it's hard i think it depends on the
[1351.72 --> 1357.92]  technology you're using and the kind of connection you have um i mean so i've actually done a fair
[1357.92 --> 1366.08]  amount of uh quite a bit of remote pairing with using screen sharing and um that tends to be less
[1366.08 --> 1371.94]  of a of an organic handing the keyboard back and forth kind of thing just because uh most screen
[1371.94 --> 1377.50]  sharing software has latency that's high enough that it's really impractical to type if you are on
[1377.50 --> 1385.98]  the remote end right um so it partly depends on what kind of technology you're using so what happens
[1385.98 --> 1390.90]  whenever i mean it's it's great if you're in that situation when you're sitting in the same room
[1390.90 --> 1394.88]  but what happens and i i mean i know some of the answers to these questions but i'm just kind of
[1394.88 --> 1398.24]  curious from your perspective and the reason why we're having you on the show is to talk about this
[1398.24 --> 1403.20]  this deep pair programming topic but you know what happens when you're not and obviously you've got
[1403.20 --> 1407.30]  answers for that because you do the podcast why teams and you've talked about this heavily so i mean
[1407.30 --> 1412.84]  how does the situation change when you're not face to face you're not in the same room yeah i think the
[1412.84 --> 1418.08]  truth is that it doesn't change a huge amount um obviously there are some technical hurdles
[1418.08 --> 1423.40]  uh there are various technologies to to bridge that gap you know like like we said there's screen
[1423.40 --> 1433.18]  sharing uh another very popular um technique is to use some form of tmux uh to share a terminal and the
[1433.18 --> 1440.78]  nice thing about sharing a terminal is that it's very low bandwidth and so uh it actually becomes practical
[1440.78 --> 1445.38]  for somebody remote to to type on your screen because the they don't have to send that very
[1445.38 --> 1450.82]  many you know that many bytes um and there are various yeah i mean there are sub categories of
[1450.82 --> 1456.18]  that there's hosting it on a like a shared machine in the cloud versus hosting it on somebody's own
[1456.18 --> 1461.06]  machine stuff like that so you mentioned the tmux and tmux i mean how much andrew do you think we
[1461.06 --> 1466.40]  should explain some of these things because i don't want people to assume oh we can link to that
[1466.40 --> 1471.00]  kind of stuff in the yeah we can but i i want to say that i don't i don't i actually don't find the
[1471.00 --> 1475.74]  the technology all that interesting it you know we're at the point where it's it's totally possible
[1475.74 --> 1480.62]  and that's kind of all i care about right i mean it's it's constantly progressing we keep having new
[1480.62 --> 1485.40]  stuff um there's a new there's a new screen sharing service called screen hero which is kind of cool
[1485.40 --> 1489.78]  because it's really really fast and you get you each get your own cursor your own mouse cursor on the
[1489.78 --> 1496.06]  screen um you know and there will be more you know interesting tools in this space but you know in the end
[1496.06 --> 1502.18]  um it's more about what you do with the tools right and and real quick the technical hurdles
[1502.18 --> 1507.64]  involved are typically hurdles you have to jump over once and once you get over those hurdles
[1507.64 --> 1512.06]  you don't really have to deal with them anymore so yeah pretty much we don't need to focus too much
[1512.06 --> 1517.64]  on the tools because you know that can be different for everybody um so to kind of move on you know
[1517.64 --> 1522.18]  again we'll share all that stuff in the show notes but to move on from this to pair program with me so
[1522.18 --> 1526.44]  now we kind of have an idea of what pairing is and so yeah some of the reasons why it's beneficial
[1526.44 --> 1532.74]  um so go ahead yeah i mean so i i'm a big fan of for all those reasons i'm a big fan of pair programming
[1532.74 --> 1538.96]  uh and then i did something kind of crazy last year for like the latter half of last year uh i stopped
[1538.96 --> 1543.76]  i kind of stopped doing traditional consulting work which is what i've been doing for a while
[1543.76 --> 1550.94]  and i became what i think of as a consulting pair programmer uh and basically what i did was i took
[1550.94 --> 1555.92]  appointments with people to pair program remotely for two hours at a time that's what i did for my
[1555.92 --> 1563.40]  job for uh probably like six or eight months um and it was awesome uh i really enjoyed it and um
[1563.40 --> 1570.78]  and you know a lot of people seem to get really get a lot out of it and i at the end of that i the it
[1570.78 --> 1574.74]  sort of that sort of came to an end i still do that i still do open source pairing sessions
[1574.74 --> 1578.94]  uh but i'm not doing that as my job anymore because like i mentioned before uh ruby tapas
[1578.94 --> 1585.08]  really took took off and so i made that my my main focus but um you know coming out of that i just
[1585.08 --> 1592.24]  felt like i wanted more people to have that experience um you know especially more people who
[1592.24 --> 1599.80]  maybe are not part of a team a co-located team where they get to pair program every day
[1599.80 --> 1607.60]  um i wanted i really wanted to see more people who are isolated or who are you know living maybe
[1607.60 --> 1612.36]  they're in a city but it's not a big tech hub city so they're they're not um around a lot of other
[1612.36 --> 1619.22]  programmers or they're like the only programmer on their team or for whatever reason um are not
[1619.22 --> 1625.56]  getting a chance to pair program uh i want to i just i want to see more programmers benefit from the
[1625.56 --> 1632.20]  experience of pair programming and uh so i decided that i kind of wanted to just basically start a
[1632.20 --> 1641.70]  movement and that's kind of where so the url is is pair program with dot me yeah there's a couple of uh
[1641.70 --> 1647.30]  there's a couple of these out there but it seems to be that and and maybe this is because of people
[1647.30 --> 1652.08]  like steve klabnik who i don't think you've said a word yet steve i've said one or two very briefly
[1652.08 --> 1658.06]  but yeah i'm staying out of it but steve has kind of you know embraced this um and i think you know
[1658.06 --> 1664.74]  we have some of the more without trying to sound like a you know suck up some of the more uh well
[1664.74 --> 1669.06]  known rubius in the community that are starting to embrace this concept and i think that that that
[1669.06 --> 1677.06]  will help this to move forward so um pair program with dot me again is the url and the idea is that
[1677.06 --> 1682.58]  you can basically you're just there's nothing special that's necessarily happening with this
[1682.58 --> 1689.90]  project this is just making it this is helping you to get an idea to share with the world that you are
[1689.90 --> 1695.78]  available to pair yeah i mean the website is almost incidental um you know i wanted some sort of focal
[1695.78 --> 1701.12]  point um but when i launched it it had a badge and nothing else so it had a badge you could put on your
[1701.12 --> 1707.44]  site and that's you know the badge says pair with this says pair program with me um or maybe it says
[1707.44 --> 1712.04]  pair with me i need to check but anyway pair with me um but you know it's it's kind of like the it's
[1712.04 --> 1715.48]  kind of like the badges that you see on some websites that say fork me on github that's that was kind of
[1715.48 --> 1722.72]  my inspiration um and and that was really all i launched with and and that's that's when i kind of
[1722.72 --> 1731.10]  kicked things off with a talk um at ancient city ruby um a couple months ago and yeah i mean
[1731.10 --> 1736.70]  it's it's really it's an idea the idea is uh you know number one pairing is awesome number two you
[1736.70 --> 1741.58]  don't need to be in the same room to do it um and number three all you really need to do is ask
[1741.58 --> 1748.92]  um i i guess that you know for me the biggest thing is sort of inspiring a culture where we ask each
[1748.92 --> 1756.70]  other hey do you want to pair on this and half of that is the asking and half of that is having
[1756.70 --> 1761.42]  having having an environment where it's okay to say that you know having an environment where it feels
[1761.42 --> 1767.60]  natural to say that um and so i kind of wanted to get people to start uh putting this badge up
[1767.60 --> 1773.98]  be just you know to kind of put a welcome mat out to to make it um feel like yeah it's okay
[1773.98 --> 1781.42]  to to say hey would would you pair with me on this and i think that the one thing that you find in
[1781.42 --> 1786.44]  especially in the ruby community and and i've spoken to some python guys and this is i think in
[1786.44 --> 1791.12]  every community but in the ruby community one thing that you find and when we had our uh a few
[1791.12 --> 1797.90]  a few episodes ago we talked about get tip and one of my concerns for a project like that is that you
[1797.90 --> 1802.10]  have all these rockstar ruby developers that get together and this is just a way for them to to
[1802.10 --> 1807.18]  to make each other feel like even more of rockstars right and so the whole idea behind pair
[1807.18 --> 1813.06]  pair program with me we need to say ppwm we need to say what you can just say pair with me
[1813.06 --> 1818.92]  the whole idea behind pair with me is kind of taking that barrier away right so this is like
[1818.92 --> 1823.62]  if if you're a i don't know ruby rockstar i don't know what to call yourself but if you know you kind
[1823.62 --> 1828.76]  of know like hey i i have some clout like i i work on some bigger projects you know like like steve
[1828.76 --> 1832.72]  you work on a bunch of stuff you're on the you know do rails contributions you do a lot of stuff
[1832.72 --> 1837.82]  um if you make this known to the general public then you're bringing that barrier down a little
[1837.82 --> 1844.12]  bit and you're saying hey like you might kind of you might look at me as a ruby rockstar but but i'm
[1844.12 --> 1849.00]  available to help you to help you learn to help you solve a problem to help you do whatever it is
[1849.00 --> 1853.88]  that you need to do right that doesn't necessarily even mean that you know every single like you know
[1853.88 --> 1858.42]  steve klabnick is not my co-worker who i'm gonna reach out to every time i have a problem to fix my
[1858.42 --> 1864.12]  problems for me but but it does say that you are making yourself available in cases where you're
[1864.12 --> 1869.56]  needed and if you have the time and if you have right you know whatever i mean like i said i i do
[1869.56 --> 1876.24]  open source pairing sessions um and um and those have been those have been really neat for me and and
[1876.24 --> 1882.82]  what i really like about them is you know those are free sessions obviously and and uh they've they've
[1882.82 --> 1888.44]  often been the case they've often been been times when i get to work with someone who's really
[1888.44 --> 1896.46]  new to programming or new to ruby or new to whatever you know technology we're working on um
[1896.46 --> 1905.06]  and that's a it's a fantastic experience um you know i i highly recommend it to anybody who's
[1905.06 --> 1913.62]  kind of advanced at what they do because um it's just you get to experience that you know vicariously
[1913.62 --> 1919.00]  experience that thrill of you know learning something new uh you know that that oh my you
[1919.00 --> 1923.64]  know wow i didn't know you could do that that's amazing you you get to experience those those moments
[1923.64 --> 1929.90]  all over again it's like we forget that uh there was a time where you had to learn what it meant to
[1929.90 --> 1934.90]  assign a variable yeah i mean i i feel i fear that that maybe sometimes people might look at the
[1934.90 --> 1939.34]  idea of pairing with a newbie and think wow that's going to be tedious but the the truth is it makes
[1939.34 --> 1946.40]  you feel amazing um and and so i guess really like my biggest call is is out to people who are kind of
[1946.40 --> 1951.92]  in that position of you know knowing knowing whatever whatever language they work in knowing it pretty
[1951.92 --> 1958.74]  well being pretty good at it you know maybe being seen as as a a guru or a master or whatever um i would
[1958.74 --> 1963.48]  love to see more people in that position uh kind of put up the the welcome mat and say yeah come on pair
[1963.48 --> 1970.40]  with me it'll be fun um i think it there's a lot i've seen a lot of people you know who are who are
[1970.40 --> 1978.56]  newbies who feel like um you know these people are unapproachable you know their their programming
[1978.56 --> 1986.22]  heroes are unapproachable and um you know i think we all know i i well i guess the newbies don't know
[1986.22 --> 1991.86]  but you know i you know i we're not unapproachable i i'm not i try not to be unapproachable i don't
[1991.86 --> 1997.40]  really think any of the the people that i um you know see it a lot of the ruby conferences are
[1997.40 --> 2004.12]  remotely unapproachable um and uh and you know we're all just programmers if people still think
[2004.12 --> 2008.08]  there's like secret sauce like i so i've done a couple of these sessions a lot of these sessions
[2008.08 --> 2011.50]  now i wasn't actually even an avdi's talk i just saw him tweet about it and i was like sounds good
[2011.50 --> 2015.84]  tweeting and then i was like oh i have like 15 appointments this week now which is awesome looks
[2015.84 --> 2020.16]  like i'm pairing and it went we're well and i actually did yesterday and today as well um random
[2020.16 --> 2025.24]  pair with me stuff as well but um i had somebody literally say to me like hey i'm real sorry that
[2025.24 --> 2028.70]  we keep writing this code and this test fails and then like it's taking a while to get it to pass
[2028.70 --> 2033.56]  and i was like i don't know what you think i do all day but like i run my tests and they fail and i
[2033.56 --> 2037.88]  try to fix them and they don't work and then i run them again and then they fail and so like you
[2037.88 --> 2042.26]  know it's all we're all just programmers it's not it's not a big deal um but you're steve klatnik
[2042.26 --> 2045.78]  you don't have to write tests everything works that comes out of your fingers stupid so this is
[2045.78 --> 2049.44]  actually what happened today avdi said earlier like you know when you feel really bad about code
[2049.44 --> 2055.54]  it's great to pair with things um and so actually that's what i did today um assuming it passes a
[2055.54 --> 2060.00]  little bit of review i'm going to commit this to rails later today but like um so i found a regression
[2060.00 --> 2064.12]  in rails because of the readers of the rails foreign action book found a discrepancy between
[2064.12 --> 2069.58]  like beta 1 and rc1 and so i figured out what it was and i got a failing test and i tried to fix it
[2069.58 --> 2075.18]  and it didn't work and uh i was like wow this feels really stupid like basically just when the
[2075.18 --> 2081.10]  password confirmation is nil or empty string don't worry about it which like is super trivial
[2081.10 --> 2085.68]  and not complicated but i couldn't get my freaking test to pass and so i ended up like tweeting
[2085.68 --> 2089.70]  finally like hey i'm feeling really dumb could somebody pair with me on this and we paired and
[2089.70 --> 2093.10]  i thought we got it working but it turns out we didn't so today i did the same thing i was like
[2093.10 --> 2097.56]  hey is anybody interested in like working on this bug and so finally after two pair with me sessions
[2097.56 --> 2101.54]  i've managed to like the the diff is like a three-line diff or something it's not even
[2101.54 --> 2106.16]  complicated it's just that like talking with someone is so helpful um you know and what's
[2106.16 --> 2111.52]  hard is different based on time to how you're feeling and all that other stuff too so so how how
[2111.52 --> 2116.68]  concise do you think the topic needs to be so if you if somebody reaches out to you and says hey can
[2116.68 --> 2123.66]  you pair with me on this how exact does that topic need to be before if the topic is too broad right
[2123.66 --> 2127.30]  there's too big of a learning curve for somebody that you don't know to maybe want to get
[2127.30 --> 2132.82]  involved so like how exact on a you know that specific instance for you steve you were like
[2132.82 --> 2136.96]  here's the test this is failing and i can't figure out how to get it passed that's pretty specific like
[2136.96 --> 2141.82]  you don't need to understand anything else other than what you're doing but if somebody comes to
[2141.82 --> 2147.44]  you and says like you know hey um i need to i need a shopping cart like that you know what i mean like
[2147.44 --> 2151.68]  that that's too broad to to be able to really sit down at one time and say let's work on that
[2151.68 --> 2156.58]  together so where do you at avdi and steve maybe where do you consider the kind of the sweet spot with
[2156.58 --> 2161.54]  like how precise do you need to be with the with the thing that you're trying to work on
[2161.54 --> 2171.30]  um i don't know i haven't really thought that hard about it um you know i try to avoid i try to if
[2171.30 --> 2178.12]  somebody approaches me and is like uh you know i want to make a new facebook then you know then i'm
[2178.12 --> 2184.94]  going to say hey can we you know sort of contract the scope a little bit um but it's kind of i don't
[2184.94 --> 2190.26]  know it's one of those organic things that it's it's each i think each each pairing session kind
[2190.26 --> 2194.82]  of works out its own parameters i don't have anything specific on scope but i just like limit
[2194.82 --> 2200.52]  it to time so i'm like oh i only have one hour i only have two hours and then you know if if the
[2200.52 --> 2205.10]  goal is to learn then you can get two hours worth of learning regardless of whether the scope is
[2205.10 --> 2209.80]  huge or small so i find that's much easier in terms of also with people's scheduling and
[2209.80 --> 2214.24]  expectations you know that it's not going to last like longer than a particular amount of time so
[2214.24 --> 2218.16]  that was one of the things yeah the other day was like hey i have a call in an hour and a half so
[2218.16 --> 2223.76]  we can work on this up to that amount but like you know i have this other hard boundary um so yeah
[2223.76 --> 2228.76]  with your interests and some of your skill sets that means that typically i'll get an hour to two to
[2228.76 --> 2233.88]  to build a hypermedia api with you yeah basically i haven't done that with anybody yet but you know
[2233.88 --> 2238.18]  that would be that would be fun um mostly it's been rails and rescue so far is what i've done most of
[2238.18 --> 2242.12]  my pairing on because people are very interested in like how to work on rails and then like it's
[2242.12 --> 2246.16]  the same as any other ruby project you clone it you run some tests you write a new one you make a pass
[2246.16 --> 2251.84]  but i mean obviously it's a big project so um you know that can be complicated to be perfectly honest
[2251.84 --> 2257.58]  and maybe i shouldn't it shouldn't let this on but i've had um i mean i've had pairing sessions that
[2257.58 --> 2263.46]  kind of just devolved into answering questions uh or having a conversation so and that's good i mean
[2263.46 --> 2269.82]  because what so kenneth writes on a show a few weeks ago talked about um in python and we have
[2269.82 --> 2274.54]  this in ruby too like you can read all the books you want but there's this there's this set of tribal
[2274.54 --> 2279.34]  knowledge that you pick up as you go and as you do things wrong and as you read other people's blog
[2279.34 --> 2284.50]  posts and you watch ruby tapas and you you know there's this tribal knowledge that isn't necessarily
[2284.50 --> 2290.28]  in any book right it's hard to just teach all of ruby in one book so for newbies to come to you and
[2290.28 --> 2295.54]  you know you might they might have a very specific problem but if it if it kind of breaks down into
[2295.54 --> 2300.44]  just like a question and answer and education session that's good because that's a that's an
[2300.44 --> 2305.72]  opportunity for you to share that that tribal knowledge to share you know like this is best
[2305.72 --> 2311.00]  practice this is what we tend to do in this world so here's some insight and and i mean who knows if
[2311.00 --> 2317.88]  that's if that gets the the ruby newbie the uh most confidence that they can have to to continue on
[2317.88 --> 2323.54]  that's probably the the best use of that time is it not yeah absolutely and and that's one of the
[2323.54 --> 2332.90]  biggest reasons that um i kind of got this started was um the idea of just spreading spreading ideas
[2332.90 --> 2339.34]  spreading knowledge um uh what i think of as kind of mimetic diversity you know a diversity of ideas
[2339.34 --> 2346.12]  and i think that pairing does that better than anything else um and it's good for us as programmers i mean
[2346.12 --> 2352.98]  having a wider getting to learn from from a wide variety of other programmers experience
[2352.98 --> 2358.66]  i think you know makes us well-rounded makes us better at what we do gives us more more tools in
[2358.66 --> 2364.96]  our toolbox when we're confronted with a problem um it's just all around good if i could jump in here
[2364.96 --> 2372.98]  real quick on the on the notion of approachability and some of the i guess potential of like having
[2372.98 --> 2376.10]  you know and we have this question here at the end of the show and i'm excited to hear what your
[2376.10 --> 2380.48]  answer is obviously but like you know you have your programming hero and you want to maybe you know
[2380.48 --> 2384.70]  for some you might just have a problem you want to solve like for example what steve and andrew were
[2384.70 --> 2389.86]  mentioning earlier but how do you how is this breaking down the barrier breaking down the wall of
[2389.86 --> 2396.72]  actually getting to pair with your programming hero um well i think you know the ideal scenario for me is
[2396.72 --> 2404.34]  is maybe that programming programming hero um puts out a pair with me badge um or puts you know tweets pair with me
[2404.34 --> 2412.86]  and and you say hey can i do it and they're like sure um you know i think that's kind of the ideal scenario
[2412.86 --> 2418.18]  because it's it's the lowest barrier to entry for somebody who might feel a little nervous about asking
[2418.18 --> 2425.66]  um but um you know in general like i'm sorry go ahead well i was gonna say it's a lot easier when
[2425.66 --> 2430.64]  you're invited than if you're trying to you know come knock on the door of a stranger kind of thing
[2430.64 --> 2437.32]  yeah but i mean something else that i'm trying to encourage yeah it you know something else i'm trying
[2437.32 --> 2444.96]  to encourage is just to is that i think i mean i could be wrong in this um one of the questions that
[2444.96 --> 2451.32]  i've asked people when i've talked about this is you know basically if somebody came to you and said
[2451.32 --> 2457.44]  hey i really like what you're doing i love what you're doing with project x um could we pair sometime
[2457.44 --> 2464.76]  um i ask that question and i usually see a lot of uh or i ask if you know what would you say to that
[2464.76 --> 2471.00]  would you say yes to that and i usually see a lot of hands go up when i ask that question um you know i
[2471.00 --> 2475.36]  think that that most people are pretty open to this kind of thing and so i think that if you have
[2475.36 --> 2481.40]  some way of reaching that programming a hero of yours uh if you know if they put their their contact
[2481.40 --> 2487.10]  form up somewhere or if they make their email address available uh or uh if they're just out there on
[2487.10 --> 2495.36]  twitter or something if i think you know if you politely say hey i i really like what you're doing
[2495.36 --> 2500.26]  with such and so um do you think we could uh you know do you think i could pair with you sometime
[2500.26 --> 2506.58]  you know the worst thing that can happen is they ignore you yeah it's true though because i think
[2506.58 --> 2511.22]  that the fear of your you know people are afraid of the program they're you know whoever they would
[2511.22 --> 2515.96]  consider to be one of their heroes and it's probably this self-made you know delusion that you
[2515.96 --> 2520.66]  have that they're gonna you know treat you like you're an idiot and it's kind of the whole crux of
[2520.66 --> 2526.16]  open source and it's kind of what we preach to people is you know just ask because the community
[2526.16 --> 2533.94]  while there is you know and again i've seen this far too often where somebody will commit a um
[2533.94 --> 2539.28]  pull request to some you know repository and say hey this is something that i would like to do what
[2539.28 --> 2542.64]  do you think and and they just get a response like this is stupid you're doing it wrong and it
[2542.64 --> 2547.42]  gets closed that does happen obviously it's unfortunate but it does happen but that's not the
[2547.42 --> 2552.86]  norm right normally normally when you submit something even if it is something that's pretty
[2552.86 --> 2558.74]  you know questionable the the responses you'll get typically will be more like okay well did you
[2558.74 --> 2563.98]  think about trying this way this is what we tend to you know to say is a better solution to that
[2563.98 --> 2569.02]  problem and that's the norm right so people are afraid of submitting their code people are afraid of
[2569.02 --> 2572.02]  the world seeing their code because they're afraid of the response they're going to get
[2572.02 --> 2577.02]  typically that response is a lot more positive than what they expected and it's more
[2577.02 --> 2582.64]  encouraging than anything to get you to contribute more code so when people finally break the wall
[2582.64 --> 2587.22]  down and start contributing to open source you find that their contributions jump because they
[2587.22 --> 2591.94]  they get encouraged about the response they're getting rather than fear of being treated poorly you
[2591.94 --> 2598.26]  know right yeah and something that that i kind of want to get into doing more is um you know if if i
[2598.26 --> 2603.48]  just don't have time or if i've got a huge backlog um i'd like to actually do more sort of referring
[2603.48 --> 2610.00]  people out you know i'd like to if nothing else be kind of a nexus where people can say hey can i
[2610.00 --> 2614.56]  pair with you and i'll be like uh well i i really can't right now and i've got a huge backlog of pairing
[2614.56 --> 2620.32]  requests but here's somebody else that you might you might enjoy pairing with so i guess that kind of
[2620.32 --> 2625.92]  brings us to a good place then pair program with that me so it's a rails app which you know for what it
[2625.92 --> 2633.22]  is might be a little heavy handed but um yeah does is that is there a future is there would you like
[2633.22 --> 2637.44]  to see something like that maybe like a i don't know like a queuing system or something where you
[2637.44 --> 2644.08]  can maybe say hey i'm available right now and um then somebody else can come and say okay this person's
[2644.08 --> 2648.36]  available let me ask them like is there anything like that you would like to see there there are a
[2648.36 --> 2653.88]  bunch of young sites out there um along those lines and i've tried to list most of them on pair
[2653.88 --> 2663.44]  program pair program with dot me see i have trouble saying it too um uh and i don't know like
[2663.44 --> 2668.96]  so the idea i mean the idea with the site is basically to be kind of a community-owned thing i
[2668.96 --> 2673.10]  mean i most of the stuff that's happened since i put it up has been uh pull requests that people
[2673.10 --> 2680.68]  submitted to me um and i think um you know i've definitely talked to some of the people that are
[2680.68 --> 2688.48]  involved with it about something along those lines uh i have some concerns about uh that that it would
[2688.48 --> 2692.44]  be easy to make something that actually wasn't that you wasn't as useful as it seemed like it would be
[2692.44 --> 2701.36]  um i know that i don't want to get into the the rabbit hole of like scheduling because that's a huge mess
[2701.36 --> 2708.54]  um and i'm a little concerned like i wouldn't what i don't want to do is build a system that winds up
[2708.54 --> 2715.18]  sort of reinforcing um circles like you know you were talking earlier about sort of the like the
[2715.18 --> 2720.40]  circles of experts you know all pairing with each other um and you know i wouldn't want to sort of
[2720.40 --> 2728.24]  reinforcing that um or kind of leaving people out in the cold if they if they put just the wrong tags
[2728.24 --> 2734.16]  in their in their post or something like that so i think it it requires a lot of thought um to be
[2734.16 --> 2741.76]  genuinely useful but um i certainly you know i i do expect that site to kind of expand and offer
[2741.76 --> 2746.94]  more features for you know more more ways of finding people to pair with as time goes by
[2746.94 --> 2753.18]  so then you're kind of leaving it open right yeah it's a true open source project you very very open
[2753.18 --> 2757.54]  it's not it's not like i have a master plan for that site i have a you know milestones or anything
[2757.54 --> 2764.30]  like that um you know the idea was i wanted to get the idea out there first and i wanted to then you
[2764.30 --> 2769.48]  know and attract some people to the cause and you know see see what you know what other people felt
[2769.48 --> 2773.92]  like would be the most useful things to have there like i think pretty soon um uh there's going to be
[2773.92 --> 2779.76]  it's a small thing but i'm gonna put like a little widget on there that that um shows all the people
[2779.76 --> 2785.96]  tweeting with hashtag pair with me um so at least you can go there and see like who's available right now
[2785.96 --> 2792.12]  yeah i think that's good i think we you know while the trend in open source has been to kind of have
[2792.12 --> 2796.88]  that you know bdfl on each project and that's that's neat and all for somebody to have this master
[2796.88 --> 2800.56]  vision and this is where the project's going to go and i'm just using the open source community to
[2800.56 --> 2805.70]  leverage other people to help me get it in that direction that's that's cool you know that that's
[2805.70 --> 2810.66]  definitely a useful you know one of the many applications of open source but i think what's what's even
[2810.66 --> 2817.82]  more uh unique and and what i think should what i would like to see grow is the idea that i'm just
[2817.82 --> 2822.06]  starting this ball moving and i want to see the community get behind it and take it wherever it
[2822.06 --> 2828.56]  wants right and and for me for me the idea the idea is i want the idea to always be paramount i mean the
[2828.56 --> 2835.92]  the site is incidental uh the site exists you know it exists to support the idea but ultimately it's i
[2835.92 --> 2839.74]  don't want this to become like a technological problem to solve it's not a technological problem to
[2839.74 --> 2845.90]  solve it's a cultural problem right it's a cultural opportunity it's a cultural opportunity
[2845.90 --> 2851.62]  to enable technical problems being solved yes you know you said the word culture there and i'm we
[2851.62 --> 2857.48]  andrew mentioned this might have mentioned this earlier but uh so we he and i work in a distributed
[2857.48 --> 2863.02]  team at pure charity and we have a back channel it's also known as our hip chat so our our actual
[2863.02 --> 2869.38]  water cooler at pure charity serves as a water cooler here for this show for those that work with us
[2869.38 --> 2873.26]  actually listen to the show but uh beverly nelson i think you you might know her but she mentioned
[2873.26 --> 2879.52]  in our chat room she said 80 of her friends at ruby friends uh is is about bringing them into the
[2879.52 --> 2883.12]  culture not so much the code and i think there's a lot of magic to what you know she said and you
[2883.12 --> 2888.24]  guys are talking about culture there i think it it becomes not so much uh oh i know ruby well you
[2888.24 --> 2893.76]  know more better than you or you know i've got more experiences it's really about just getting
[2893.76 --> 2900.64]  involved you know regardless of your of your level of activity and whatnot but just jumping in and
[2900.64 --> 2905.62]  that's probably the hardest part too about open source is you there's this this huge intimidation
[2905.62 --> 2910.50]  that you have a bunch of assumptions before you're involved that this is how it's going to be and it's
[2910.50 --> 2916.22]  not at all really how it is and we're a lot more uh friendlier than people might think but you know i
[2916.22 --> 2921.24]  think that's the hardest part is just you know breaking the ice something something that i'm i've started
[2921.24 --> 2929.72]  uh doing uh which i hope will help with that um is i started putting some of my pairing sessions up on
[2929.72 --> 2937.14]  uh google hangout uh google hangout on air yeah so um and i didn't really like announce it or anything
[2937.14 --> 2941.46]  i just i would be working with someone i'd be like hey do you mind putting this make putting this up as
[2941.46 --> 2946.86]  a hangout on air and then whoever happened to be around could like tune in and watch us and i recently
[2946.86 --> 2955.12]  did one of these um actually with one of my co ruby rogues just josh susser um and put it out there
[2955.12 --> 2960.22]  and got a lot of really good feedback from it and i i think some of the feedback that i think that was
[2960.22 --> 2970.32]  most interesting for me was kind of the like um the the way watching it kind of took the the magic
[2970.32 --> 2977.64]  out of it like you know took the that aura of you know the thing that those coders do is different
[2977.64 --> 2986.06]  from what i do um and you know i think that if we maybe if if if i and maybe others put some more of
[2986.06 --> 2992.42]  our pairing sessions up like that um other program programmers can look at it and say oh wow that you
[2992.42 --> 2997.34]  know basically the stuff they do is the same stuff that i do and and they make the same boneheaded
[2997.34 --> 3002.82]  mistakes and they sit waiting for their tests to pass and and you know and sometimes sometimes
[3002.82 --> 3010.24]  they spend an hour and write three lines of code and um and it's not you know there's nothing magical
[3010.24 --> 3015.98]  about it there's nothing unique about it um we're you know we're all just doing the same stuff
[3015.98 --> 3022.08]  i think that's kind of something that steve said uh not so much said with his words but
[3022.08 --> 3026.02]  that we're all doing the same stuff steve didn't you um for a while there weren't you
[3026.02 --> 3031.90]  vimeoing if that's the word um like basically just you hack him by yourself but you were just
[3031.90 --> 3036.56]  hacking on hackity i believe and you were sharing that on vimeo and people are watching like oh yeah
[3036.56 --> 3040.36]  he does the same thing i do or you would actually have your own commentary in there and you were just
[3040.36 --> 3045.96]  talking to yourself yeah it was with hilarious results so i didn't i didn't fully appreciate how
[3045.96 --> 3051.34]  to properly mix my audio or i didn't notice that the audio was mixed poorly and so there's there's
[3051.34 --> 3058.32]  one of me fixing a bug in ruby gems um with like kesha louder than my voice so i didn't provide
[3058.32 --> 3064.48]  commentary but instead it's just blasting i wasn't sure i thought it was something hilarious too but
[3064.48 --> 3069.72]  i was yeah it was pretty good so i i would like to get back to doing a little bit of that but um
[3069.72 --> 3073.46]  you know i just it's just one of those things where i did it a couple times and it was fun and
[3073.46 --> 3077.40]  people liked it and i just haven't done it since because i haven't done it since not because of any
[3077.40 --> 3082.14]  specific reason so sometimes you gotta break the mold man you know just do them a little
[3082.14 --> 3086.48]  different you know don't follow the same rhythm in the rhyme it's also just funny because you're
[3086.48 --> 3090.42]  like when you're like recording your screen you're always like terrified that something is going to
[3090.42 --> 3095.22]  happen like what am i going to type or am i going to get like an im message that should be private or
[3095.22 --> 3101.38]  like you know how is this going to work out so that's also real fun too um but uh yeah you know i
[3101.38 --> 3104.88]  mean i think it's good uh just in general that was what i was trying to show with ruby gems is that
[3104.88 --> 3110.92]  like you know ruby gems is a particularly terrible code base due to its history and etc and so uh you
[3110.92 --> 3114.38]  know watching like here's how i tackle this kind of bug you know you could totally do it too was
[3114.38 --> 3118.68]  definitely like the point of that i was like i don't do anything but just run the tests and cuss
[3118.68 --> 3124.92]  over and over and over again i can't imagine if i'm pairing with somebody and and i am from my wife
[3124.92 --> 3129.34]  pops up reminding me to get the rash cream or something that would probably be the worst thing ever
[3129.34 --> 3134.64]  seems bad i just noticed somebody might think that you're human or something
[3134.64 --> 3139.26]  yeah yeah i don't want that man they are supposed to like i'm supposed to be a demigod of programming
[3139.26 --> 3145.44]  or something to them uh just kidding hopefully everyone knew that uh on pair program with dot
[3145.44 --> 3151.76]  me i just noticed the header you say pair widely pair often is that a uh shout out to the idea of
[3151.76 --> 3157.90]  wide teams a little reference to wide teams there that's the second uh last week we had docker on and
[3157.90 --> 3162.66]  they had a number they had their on their frequently asked questions they went numbers one two three four
[3162.66 --> 3168.80]  five and then to 42 so this is the second little uh nugget i found in the uh products you're so
[3168.80 --> 3171.38]  you're so keen man you know that's right
[3171.38 --> 3180.40]  so confident ruby another book that you are writing still i mean it's in betas i mean you're
[3180.40 --> 3187.02]  still writing it's in beta which means that i've pronounced it content complete um after taking
[3187.02 --> 3194.38]  kent beck's advice to get it to 150 pages and then just stop um and so it's i'm still editing the
[3194.38 --> 3202.88]  crap out of it but um but it's content complete and this book um again stemmed from a talk that
[3202.88 --> 3209.88]  you've been giving yeah um actually i think it was the first talk i wrote um which i called confident
[3209.88 --> 3221.18]  code and uh it's it's all about writing methods that tell a coherent story uh sort of a narrative
[3221.18 --> 3228.90]  style of of writing methods is how i think of it and and a lot of that involves uh writing code that
[3228.90 --> 3235.62]  uh sort of confidently progresses forward without a lot of tangents and diversions and provisos because
[3235.62 --> 3241.66]  of uncertainties about input or uncertainties about errors that might occur um and just uh it's
[3241.66 --> 3247.32]  basically a patterns book and it's a book of patterns um that are strategies for making your
[3247.32 --> 3253.36]  code more confident for you know telling those stories uh more coherently uh and you know isolating
[3253.36 --> 3260.30]  isolating the error handling and and dealing with with input in such a way that you don't have to be
[3260.30 --> 3265.46]  uncertain about it in the midst of the method and stuff like that yeah it's a uh where can you
[3265.46 --> 3270.00]  where i couldn't find it anywhere other than on your uh on your store is there anywhere that if you
[3270.00 --> 3275.36]  go if you go to confident i think if you go to confident ruby.com you'll actually actually i think
[3275.36 --> 3282.06]  that'll redirect you to the blog post where i first introduced it um and so that's probably the easiest
[3282.06 --> 3289.16]  way to get to it uh you can also find announcements about it on my blog which is devblog.avdi.org yeah
[3289.16 --> 3292.68]  we'll uh we'll have this i found the link we'll have the link in the show notes for those of you
[3292.68 --> 3298.66]  listen to the podcast head to five by five dot tv slash changelog slash 90 to see all the show notes
[3298.66 --> 3306.90]  and links and everything else so don't be lost so um avdi what are your speaking uh engagements
[3306.90 --> 3311.00]  planned for the future that you already have set up i keep meaning to put together like a
[3311.00 --> 3317.68]  an actual list of them um let's see uh next one up i know is going to be um
[3317.68 --> 3333.12]  um uh yeah name god uh the one in in dc arlington not not yeah uh yeah the one oh gosh it's uh
[3333.12 --> 3338.88]  oh uh ruby nation ruby nation thank you thank you funny my mind wanted to be like nation ruby and
[3338.88 --> 3349.26]  then i was like no that's not right um yes ruby nation um and uh in just like a couple of weeks
[3349.26 --> 3356.08]  and speaking of ruby nation you gave this confident code talk there too yeah i guess i did um i i'm
[3356.08 --> 3364.14]  doing a i believe i'm going to be doing a talk on uh uh coding and joy basically uh little little
[3364.14 --> 3370.70]  bits of ruby that just make me happy uh this time around so um yeah that'll be fun and then uh after
[3370.70 --> 3377.82]  that um several others i think uh well i'm going to be going to pittsburgh steel city ruby um love
[3377.82 --> 3384.22]  pittsburgh woo stack adam is from pittsburgh yeah originally born and raised in the pittsburgh area
[3384.22 --> 3391.18]  so that's uh steve where are you at i mean i live in santa monica now but um i i lived in pittsburgh
[3391.18 --> 3396.46]  my entire life before moving to los angeles so there you go i thought so so everyone everyone
[3396.46 --> 3401.64]  on this chat has some connections to pennsylvania that that has happened in pretty much every chat
[3401.64 --> 3408.72]  that i've ever had i found it's weird it's six degrees of pennsylvania yeah so you'll be a steel
[3408.72 --> 3417.68]  city ruby um when is that on the date that it is on yes yeah august middle august sometime awesome
[3417.68 --> 3426.12]  so for those of you who are uh new to the show and those of you that have listened you'll know
[3426.12 --> 3433.38]  uh we ask all of our guests these two questions um the first one abdi is for a call to arms and i
[3433.38 --> 3439.16]  guess in this case you could give us a specific call to arms for pair program without me if you want
[3439.16 --> 3445.12]  yeah or uh just kind of what you would like to see the community do around this i i don't think it's
[3445.12 --> 3450.30]  going to come as any surprises at all it's it's just go out there and pair with each other go you
[3450.30 --> 3457.20]  know go ask um if you have somebody that you've always wanted to you know learn from go ask them
[3457.20 --> 3463.80]  if you have some time in your day uh you know that you would be working on open source or something
[3463.80 --> 3469.32]  anyway put that welcome that out there put that badge on your blog put the you know hashtag pair with
[3469.32 --> 3475.26]  me on your twitter feed if you do the twitters um make yourself available i think you'll find it
[3475.26 --> 3483.98]  incredibly rewarding to to pair widely pair diversely um pair more often how do you feel about pairing on
[3483.98 --> 3489.42]  more conceptual like if somebody's a python developer and you don't have python experience
[3489.42 --> 3495.34]  pairing conceptually on an idea how do you feel about that i think it still totally works uh just the
[3495.34 --> 3502.44]  other day uh i paired with somebody on some dot net code some c sharp code and granted um i have
[3502.44 --> 3508.44]  done c sharp before but it was years and years ago and i was totally rusty uh and it didn't matter i
[3508.44 --> 3513.56]  just basically i had i had them be the driver uh that could have worked either way but it worked
[3513.56 --> 3517.58]  that was nice just because they already had their whole environment set up and they had their ide and
[3517.58 --> 3522.86]  they knew the key bindings and you know how to make the test go and stuff like that um but it was fun
[3522.86 --> 3529.12]  because i actually got to teach them something about uh something about c sharp um not because i knew it
[3529.12 --> 3540.46]  but because i i just sort of like basically um figured that a particular um the library call had to exist
[3540.46 --> 3547.66]  and looked it up until we found it and basically it was using a more functional functional approach to
[3547.66 --> 3552.54]  solving a problem than they were used to maybe as an attachment to your call of arms i have a
[3552.54 --> 3557.30]  couple ideas and i can share with you on the fly maybe um start a wiki page for those who
[3557.30 --> 3564.38]  on uh the ppwm repo you have on your offer user maybe a wiki page that says hey i'm open for pairing
[3564.38 --> 3571.72]  and or moving this to an org and maybe having just a project for issues where you can kind of allow
[3571.72 --> 3578.60]  issues to coordinate the community potentially just an idea yeah yeah that's a good thought actually we've
[3578.60 --> 3584.82]  we we have started using the the wiki a little bit uh on the the github page for it gotcha it says
[3584.82 --> 3593.70]  welcome to ppwm i'm just messing with you man just uh one thing i did want to give a shout out this is a
[3593.70 --> 3600.46]  community project but um at the bottom i noticed you said the design was done by chris radford and the
[3600.46 --> 3606.08]  badge was done by uh david browning so kind of wanted to give them a little bit of yes a shout out for
[3606.08 --> 3612.08]  getting in on this thing early with you yeah yeah um and they totally deserve it um much uh gratitude
[3612.08 --> 3618.82]  to both of them and to everybody who's submitted a pull request all right and our last question if you
[3618.82 --> 3625.54]  could name a programming hero or again somebody in the idea of distributed workplaces or wherever you
[3625.54 --> 3635.46]  might think what would who would you say your hero would be um so i could obviously name any number of
[3635.46 --> 3642.64]  amazing programmers that have influenced me and that i look up to uh but i think i want to give a shout
[3642.64 --> 3651.96]  out to angela harms um because she's she's been doing some talks in the ruby community lately well
[3651.96 --> 3657.24]  in the programming community lately not specifically the ruby community she's she's uh i guess maybe more
[3657.24 --> 3664.32]  um part of the agile community you could say um that's i think that would be her background but
[3664.32 --> 3672.10]  seems right yeah um and she has been she she talks to to programmers about compassion
[3672.10 --> 3681.90]  and she does it in a way that's that's effective and um you know really uh is eye-opening and um i think
[3681.90 --> 3689.08]  heart opening and i think that's wonderful and i think it's much needed uh so so yeah i'm gonna say
[3689.08 --> 3696.58]  angela harms uh did she i want to like i remember there was something like a radical something that
[3696.58 --> 3702.12]  she did or that i remember seeing her name on i'm actually not sure of like any of the i don't recall
[3702.12 --> 3707.18]  any of the specific titles of her talks radical love or something like that but yeah no i definitely
[3707.18 --> 3714.66]  have um well it's not radical love.org it's that org it's something that she did but yeah uh or at least
[3714.66 --> 3720.84]  i remember hearing her name with but i i agree with you i think that there's something inherent
[3720.84 --> 3729.44]  that we need to see in this community and it's it's it's the idea of like i don't know just acceptance
[3729.44 --> 3735.76]  of people in this community and you can get bogged down and what you know the ruby drama or whatever we
[3735.76 --> 3741.04]  we call it where um you just you get on and you follow some of the big names in the ruby community
[3741.04 --> 3746.50]  and is there can be a lot of name calling and a lot of just trash going back and forth and i don't
[3746.50 --> 3750.76]  know if maybe that's what you're hinting at but i would like to see less of that and more of just
[3750.76 --> 3755.78]  people generally respecting each other in the in the community well you know not just a ruby thing
[3755.78 --> 3761.78]  it's just a programmer thing in general i think um we we have a culture that's very very rationality
[3761.78 --> 3768.04]  centric uh very logic centric um you know very often i think yeah in theory we believe it to be
[3768.04 --> 3774.22]  um and of course we also believe ourselves to be very logical um and i think a lot of you know a lot
[3774.22 --> 3779.76]  of times uh you know we think that solving a problem boils down to being the most rational
[3779.76 --> 3786.08]  person in the room uh and i think the stuff that she's talking about will challenge that and i think
[3786.08 --> 3792.68]  it'll challenge that in in a good and important way yeah that is true i mean i think it begins with uh
[3792.68 --> 3798.68]  it begins with you right it begins with us uh as an individual to to be different and to act
[3798.68 --> 3808.88]  differently so um don't be a hater repeat after me we are all different somebody's gotta we're all
[3808.88 --> 3815.64]  yeah somebody's got uh nobody uh the response the response is i'm not
[3815.64 --> 3823.50]  that'll be some some python fans in the audience at least and hopefully somebody will get it i don't
[3823.50 --> 3823.64]  know
[3823.64 --> 3833.08]  this has certainly been a definitely been a fun chat avi i definitely appreciate you taking the
[3833.08 --> 3837.64]  time to come on the show it's it's a fun conversation uh you're always invited back
[3837.64 --> 3841.64]  certainly appreciate all that you're doing in the community and what you've done with uh
[3841.64 --> 3847.22]  pair programming and just lifting that up and sharing what that can be and just starting the
[3847.22 --> 3852.84]  movement as as andrew mentioned before and uh definitely thanks to andrew and steve for coming
[3852.84 --> 3857.84]  on the show what a what a great show you guys uh put on today and thanks to you for the listeners
[3857.84 --> 3863.40]  out there listening live this show does broadcast live every tuesday at uh at 5 p.m central standard
[3863.40 --> 3869.20]  time here on five by five if you want to check out back our backlog you can go to five by five dot tv
[3869.20 --> 3874.98]  slash changelog this is episode number 90 so uh you you definitely enjoyed it but let's close this
[3874.98 --> 3880.48]  out and say goodbye see y'all later bye bye
[3899.20 --> 3899.70]  you
