[0.00 --> 14.16]  welcome back everyone this is the changelog i'm your host adam stekowiak this is episode
[14.16 --> 20.76]  139 today jared and i talked to michael rogers one of the leads behind iojs
[20.76 --> 27.64]  iojs is a recent fork of node.js a lot of good conversation here today about the community
[27.64 --> 36.20]  open governance why the iojs fork exists uh sem version how they're doing it open governance
[36.20 --> 41.64]  a lot of cool conversation today with michael uh we got some awesome sponsors today for the show
[41.64 --> 46.54]  code ship top tile and digital ocean we'll tell you a bit more about code ship and top tile later
[46.54 --> 50.76]  in the show but our friends at code ship they want us to tell you about this awesome free plan they
[50.76 --> 57.50]  have it includes 100 builds a month and five private projects code ship is a hosted continuous
[57.50 --> 62.78]  deployment service that just works you can easily set up continuous integration here in just a few
[62.78 --> 67.98]  steps and automatically deploy all your code when you're just passed the cool thing too about code
[67.98 --> 72.26]  ship is they just released a brand of design not it doesn't look better but it also has a lot of
[72.26 --> 78.28]  great usable functions uh usability improvements to make things even easier than they were before
[78.28 --> 83.84]  they got great support for lots of languages and test frameworks they integrate with github or bitbucket
[83.84 --> 88.94]  and you can deploy to cloud services like heroku aws and the list goes on setup takes just three
[88.94 --> 96.62]  minutes find code ship at code ship.com slash the change log also check out their blog to blog.code
[96.62 --> 104.32]  ship.com to get updates use our special offer code the change law podcast to get 20 off any plan you
[104.32 --> 111.46]  choose for three months again that code is the change log podcast to get a 20 discount on any plan you
[111.46 --> 116.18]  choose for three months code ship.com slash the change log and now on to the show
[116.18 --> 124.84]  all right everybody we're back we're talking with michael rogers he is uh well michael what are you
[124.84 --> 132.08]  what exactly are you to io.js to io.js i think the the best title for me would be janitor janitor okay
[132.08 --> 137.52]  that's the most apt yeah yeah so it's me i generally go around and clean up the messes there you go
[137.52 --> 144.78]  so it's it's me uh jared's on the call jared say hello hey everybody and we got michael um and it's
[144.78 --> 148.04]  funny you know i'm gonna just say this michael because that's the question i asked you prior to
[148.04 --> 152.52]  get on the call which was how to say your first name and i'm sure you get that a lot so uh everyone
[152.52 --> 157.86]  his name is michael he just had hippie parents yeah hippie parents invent spelling which is which
[157.86 --> 162.68]  is cool and uh a little disclaimer here digital ocean does sponsor the show michael works there he's
[162.68 --> 167.28]  not on the show because of digital ocean by any means but they are sponsoring this show it's just
[167.28 --> 174.04]  a fluke it's just timing um you know it works out like that sometimes but uh the the call we want to
[174.04 --> 178.16]  have today is you know in the preamble the call that wasn't in the audio that you're not going to
[178.16 --> 184.72]  listen to was us sort of rehashing the change logs perspective on the node community our coverage of
[184.72 --> 190.58]  it we had aaron hammer on two black fridays ago talking about how node scaled and how their
[190.58 --> 196.58]  servers barely saw a blip on in terms of cpu and everything that was going on there we've had uh
[196.58 --> 201.54]  isaac suit on our show before we've had talking about npm um we've had lots of conversations about
[201.54 --> 207.92]  it we haven't come back to the topic of io.js and what's happening there so maybe the easiest way to
[207.92 --> 213.36]  open up the show would be to sort of introduce deeper than a janitor level um you know kind of who
[213.36 --> 217.92]  you are michael uh you obviously work at digital ocean what their usages of it is and sort of what
[217.92 --> 224.02]  your stake is here we'll kind of begin there yeah yeah so i mean i've been a developer for a long
[224.02 --> 229.44]  time been an open source developer for quite a long time uh been a javascript developer for a long time
[229.44 --> 236.80]  i was at mozilla and i was at couch one the couch db company um and you know right when node uh sort of
[236.80 --> 242.34]  became public and and ryan did his first talk i got really into node and went pretty deep um and you
[242.34 --> 247.56]  know i back in the day i worked a bit on core and haven't really worked uh too much on code and core
[247.56 --> 252.92]  since um but mostly in like the hdp client uh and i wrote a library called request that uh became
[252.92 --> 261.56]  quite popular and is now sort of like the default hdp client that people use um on top of node and uh
[261.56 --> 268.62]  oh i run node conf um and js fest um some pretty big and and really fun uh node and javascript
[268.62 --> 275.60]  conferences um and in digital ocean i'm a js evangelist so um i go out and sort of give back to the
[275.60 --> 281.44]  to the js community on behalf of digital ocean um and you know we we love node and javascript and a
[281.44 --> 287.14]  lot of our customers are running it we just shipped a free bsd support actually um and free bsd for a
[287.14 --> 291.90]  variety of historical and technical reasons is a great place to run node or iojs so that's been
[291.90 --> 300.10]  really cool to see what makes free bsd specifically tailored for that environment um so i'm if you if
[300.10 --> 308.56]  you've gone to a node conference or if you've sort of sat through um any series of speakers about node
[308.56 --> 314.76]  you'll hear about dtrace right like um dtrace is really big in the node community um and you know
[314.76 --> 319.80]  a lot of that is because of joyant um but also it's just a great tool for for looking at what's going
[319.80 --> 325.76]  on uh turns out that not only solaris solaris variants uh have dtrace support but also free bsd
[325.76 --> 331.30]  has pretty fantastic dtrace support um uh to the extent that you know voxer who's you know one of
[331.30 --> 336.32]  the bigger node users they've actually moved um everything over to free bsd and one of the more
[336.32 --> 343.06]  uh prolific uh contributors to iojs uh fiodo uh fiodoran duttony uh who actually was the the person who
[343.06 --> 350.00]  hit the damn fork button um he's responsible right no no he's he's great um and he writes a ton of code
[350.00 --> 355.48]  um but he actually works at voxer um is really dedicated to keeping free bsd support great um and
[355.48 --> 360.06]  is even a free bsd carnal contributor now and has done work to make dtrace better over there
[360.06 --> 368.76]  awesome so let's talk about that fork button um you know node huge project lots of corporate
[368.76 --> 374.94]  interests lots of um uh hobbyist interest plenty of people making a living writing node applications
[374.94 --> 382.20]  you know maybe take us a little bit through um at whatever level you like to get into on the the
[382.20 --> 391.38]  recent history of the node project joyance involvement um why the fork right right um so node
[391.38 --> 397.64]  uh simultaneously uh has become one of the biggest success stories uh and one of the biggest failures
[397.64 --> 404.92]  in open source so um about a year ago um myself and other people started to get
[404.94 --> 409.90]  you know increasingly concerned and organized around doing something about this um and the
[409.90 --> 414.58]  problem is that you know we have the a year ago we had the fastest growing open source ecosystem
[414.58 --> 421.84]  uh today we have by far the largest public open source ecosystem there are over 100 000 modules on npm
[421.84 --> 427.14]  there will probably be around 200 000 by the end of the year um that's just phenomenal it's crazy
[427.14 --> 431.52]  um so a ton of people are using it a ton of people are bringing it into production the usage
[431.52 --> 438.96]  and the ecosystem has grown tremendously at the exact same time actual people contributing to node
[438.96 --> 445.34]  core has gone down precipitously um and an even greater decline we've seen the releases so releases
[445.34 --> 450.84]  just don't happen anymore we just don't ship any software and we can we can argue forever about why
[450.84 --> 456.12]  that is and we can argue forever about the quote-unquote best way to fix it um but the reality of the
[456.12 --> 462.68]  situation is that while there's a company that runs the project and sort of owns the project at this
[462.68 --> 469.60]  level they're the only people that are enabled to fix it and so what myself and and a bunch of other
[469.60 --> 474.42]  companies that were concerned and core contributors were consumed we sort of got organized around
[474.42 --> 480.44]  asking joint you know we want to take over the the actual running of the project um so that we can
[480.44 --> 486.96]  take on these issues and so that we can fix them so we you know started a process uh it was it was rocky
[486.96 --> 492.50]  and a bit up and down and i think isaac has probably talked a bit more about that publicly than than i have
[492.50 --> 500.36]  um uh eventually joint got a new ceo a guy named scott hammond um scott got involved he built out
[500.36 --> 509.98]  uh an advisory board and uh you know he he scott's a great guy um everything that he has said that he
[509.98 --> 515.88]  would do that he has taken on to himself to do as a task has has totally happened and come through um
[515.88 --> 521.72]  but you know he has this really long involved process um where all these companies sort of get
[521.72 --> 527.12]  in a room and they try to figure out what to do to solve these problems and the big problem the thing
[527.12 --> 532.46]  we're talking about is that open source contributors in an open source community isn't participating in
[532.46 --> 537.36]  the project and isn't enabled to fix these problems and having a room full of people from companies
[537.36 --> 542.52]  doesn't really fix that and you know even if they say tomorrow okay here the contributors run the
[542.52 --> 547.96]  project we don't have the momentum and all the people behind that um to actually you know get the
[547.96 --> 553.94]  project moving along so what i did um around the time that the advisory board was sort of spinning up
[553.94 --> 558.42]  is i started this project called node forward the idea was that we would try to organize and
[558.42 --> 562.02]  galvanize the community around solving some of these higher level issues you know some of them
[562.02 --> 569.12]  in core and some of them just around core um and for a time we had um for a very short amount of time
[569.12 --> 574.50]  we had a fork of node where we were just sort of merging stuff and we we didn't have plans at the time
[574.50 --> 579.92]  to even really do releases we just wanted to see what we could do sort of code wise and contributor wise
[579.92 --> 585.74]  um i was informed quite quickly uh over the phone that that is a trademark violation and that i would
[585.74 --> 591.54]  be sued and da da da um and we talked about it with the other contributors and sort of in good faith
[591.54 --> 596.34]  um because scott was putting this good foot forward with the advisory board we decided to make that
[596.34 --> 600.98]  private for an amount of time um and then we kind of kept you know pushing it out and pushing it out
[600.98 --> 606.88]  and uh finally uh fiotr had just kind of had enough um he he wanted to be you know putting his patches
[606.88 --> 612.82]  back into a public uh fork so he created one called iojs um which you know doesn't infringe
[612.82 --> 618.04]  on the trademark um and even if it did i mean he's russian like you can't sue him for trademark um
[618.04 --> 624.92]  and uh that's one way to do it right yeah or at least to get around the the temporal issue yeah yeah
[624.92 --> 632.18]  um so and you know within a day you know basically fiotr just said i'm landing my patches here now and um
[632.18 --> 636.34]  that was enough for all the other contributors and everybody just be like well i guess we're also
[636.34 --> 641.98]  landing our patches there um and we just sort of moved all of the work and the effort over there
[641.98 --> 647.58]  uh and came up with a plan to you know ship a release so and plan to ship sort of purposeful
[647.58 --> 654.04]  but accidental um what do you mean by that well i mean purposeful in the fact that node forward and
[654.04 --> 659.78]  then you know getting a phone call and then having to have alternate plans and then accidental that
[659.78 --> 664.52]  um fedora had had pushed the fork button and wanted to start contributing back publicly
[664.52 --> 670.88]  not back to original node and io.js and so that's sort of the purposeful yet accidental
[670.88 --> 677.42]  approach to this yeah i mean we we had done a lot of governance work already and we had had and we
[677.42 --> 682.68]  were having these regular sort of technical committee calls um but they were they were all private and
[682.68 --> 685.58]  they were about this private fork and there's just a limited amount of things that you can do there
[685.58 --> 693.20]  right um and and we nobody was happy with it being private um but you know trademark law being what
[693.20 --> 697.64]  it was like we just we just didn't want to mess with it um and uh i think it was actually like
[697.64 --> 702.78]  maybe thanksgiving weekend or something um so it was you know like a bunch of the people in the u.s
[702.78 --> 706.94]  just aren't even around when he decided to do it so it was it was not the most opportune time it's a
[706.94 --> 711.82]  good time to do it too to get on the radar you know right right i mean it wasn't even the most
[711.82 --> 716.94]  opportune time to do it you know if we really wanted to message it as this big thing but um we
[716.94 --> 720.80]  all got on board real quick and and you know immediately we saw people get really excited
[720.80 --> 726.06]  about it and you know like when the when the node forward stuff sort of like leaked although i don't
[726.06 --> 730.36]  know how something public can leak but um when people started talking about the node forward stuff
[730.36 --> 737.82]  we made the mistake of you know not talking uh to press and and to people more honestly about it
[737.82 --> 742.32]  because we didn't want to you know make waves with with the stuff going on with joyant but then
[742.32 --> 746.78]  joyant actually did talk to all those press and so um we didn't make that mistake again you know we
[746.78 --> 751.98]  talked about it really openly we we had really clear messaging um so the people didn't get confused and
[751.98 --> 757.30]  there wasn't a lot of fud and then you know if you look at you know all the twitter stuff about iojs
[757.30 --> 761.58]  when it when all the information gets out there you know people were pretty much universally positive so
[761.58 --> 765.66]  that was really good to see it seems like it wasn't necessarily accidental it's just that you guys
[765.66 --> 770.94]  were kind of maybe waiting for someone to take the lead and jump into that you know into that cold water
[770.94 --> 775.88]  and then once the once one buddy somebody's in uh it's easier for everybody else just to make the leap
[775.88 --> 781.40]  yeah and i and i think it has to be somebody like fiotr or you know somebody who is is is
[781.40 --> 787.90]  contributing in an equal amount i mean the reality is like we don't have a fork or a node without fiotr
[787.90 --> 793.46]  so where he goes it's like everybody else is very incentivized also how many of the core team
[793.46 --> 800.34]  uh moved over um everybody except the ones employed by joint okay and just historically
[800.34 --> 805.56]  did joint i know ryan doll started the project and i believe did he work at joint when it was
[805.56 --> 814.40]  conceived and released no no he was living off of savings um uh in germany actually okay when he wrote
[814.40 --> 820.18]  it in cologne and um and then sort of ran out of savings uh and needed a job and was like by the
[820.18 --> 825.66]  way i wrote this node thing uh and then he went to join and worked there and then after some amount
[825.66 --> 830.54]  of time working there um there was an agreement where he he transferred the copyright uh and the
[830.54 --> 836.24]  trademark and all the assets over to joint okay so they own the trademark for node js but the project
[836.24 --> 844.68]  itself what was the open source license on it mit um and in addition to that there was for a while
[844.68 --> 853.80]  there was a cla um that granted joint uh a license to your work um that was essentially the equivalent
[853.80 --> 860.60]  of also sharing the ownership but uh they removed that uh sometime i think in the summer of last year
[860.60 --> 868.08]  so there's no cla and there was no dco and there's you know lots of very concerned people about that for a
[868.08 --> 876.04]  while um iojs uh has always had um it's called the dco um which is a developer certificate of origin
[876.04 --> 882.86]  um essentially some of the uh patent protection stuff and some of like the concerns that people have
[882.86 --> 888.18]  um about just taking contributions under license without anything else they're solved by the dco
[888.18 --> 893.08]  just as a public notice it's not like a thing that you have to sign um and this is used by the
[893.08 --> 898.96]  kernel project it's used by the get project it's you know every company that you would need to buy
[898.96 --> 905.64]  into this idea has bought into this idea so kind of interesting we just last week we had on um
[905.64 --> 913.36]  alex pulvey who was the ceo of core os and they just um did not fork docker but they just released a
[913.36 --> 920.36]  public uh implementation competitor in a certain sense to docker um iojs this is more this is your
[920.36 --> 925.08]  traditional fork right this is not a rewrite this is not an alternate implementation this is literally
[925.08 --> 933.42]  code base taken renamed and just landing patches on on the renamed version is that right well i i don't
[933.42 --> 938.78]  even think it's all that traditional as a fork because i mean for it to be a fork there has to be
[938.78 --> 944.54]  a competing linear line of development okay and that we so far we haven't seen that i mean we
[944.54 --> 950.26]  we basically have the future of node happening over in iojs um and while some patches are still going
[950.26 --> 956.56]  in that we're merging out of node back into iojs uh for 0.12 like they haven't made any public plans
[956.56 --> 961.86]  past 0.12 they haven't shipped 0.12 even though all the other contributors thought that they should
[961.86 --> 968.52]  have um you know it's i i don't know what's going on over there okay and the a lot of the contributors
[968.52 --> 973.70]  that are still you know still feel obligated to to do some work over there to get out 0.12 they're
[973.70 --> 978.82]  also actively involved in io.js and aren't really going to continue i i don't think they'll continue
[978.82 --> 985.58]  much past the the 0.12 release so you're so it sounds like joint is it's stagnated because of
[985.58 --> 990.42]  perhaps lack of interest and that's just going to remain on that side of the fence who knows how long
[990.42 --> 995.88]  i mean i i don't like to speculate like yeah um you know a lot of people have a lot of differing
[995.88 --> 1004.42]  opinions about why um it has sort of died on the vine i mean i don't i don't know joint corporate um
[1004.42 --> 1009.66]  what joint corporate position is on it like you know why they are or are not investing in it or
[1009.66 --> 1016.32]  why they have one opinion or another um i just know that the reason that the project lacks contributors
[1016.32 --> 1021.32]  that there's not a clear way to contribute and then even if you do contribute it's this huge hill
[1021.32 --> 1027.00]  decline to get any recognition for it and then if you even get any recognition for it um there's no way
[1027.00 --> 1031.76]  that you can actually direct the future of the project or be involved in decision making because of
[1031.76 --> 1038.70]  this you know corporate dictator model um so how long has it been like that like it's if this is why
[1038.70 --> 1046.62]  has that been a problem for years or is this like something new that's crept up trying to release the
[1046.62 --> 1052.56]  next version um well no i think that a combination of things happened right so the first project leader
[1052.56 --> 1059.12]  was ryan doll ryan um was sort of done he just didn't really have any interest in in working on
[1059.12 --> 1062.36]  no anymore he has a bunch of other crazy projects i'm having dinner with him tonight actually i'll
[1062.36 --> 1068.64]  find out what his new thing is okay um but uh and and then it went to isaac schluter um who was also a
[1068.64 --> 1074.30]  joint employee but was also just the the most obvious choice to start running the project i mean he
[1074.30 --> 1081.56]  created npm he was a really active contributor um he built out the module system um and and sort of a
[1081.56 --> 1085.32]  lot of the shift in priorities and focus that the project needed to go through basically from
[1085.32 --> 1092.46]  uh focusing on low-level details to enabling more of an ecosystem it was just a natural choice so
[1092.46 --> 1097.78]  um even though ryan made that decision somewhat unilaterally or you could say joint made that
[1097.78 --> 1101.80]  decision somewhat unilaterally um if anybody were to complain about it in the community they would
[1101.80 --> 1105.44]  have had to come up with somebody else and nobody else really had the credibility at the time to do
[1105.44 --> 1111.20]  that um and just for the listeners sake to just to sort of play catch up here if you're going back and
[1111.20 --> 1116.56]  listening to past changelog shows to kind of keep up the pace with what we've talked about around node
[1116.56 --> 1122.88]  and and whatnot npm with isaac on the show that show with isaac isaac was still at joint then and i
[1122.88 --> 1127.16]  remember andrew and i because this is prior to jared coming on as a co-host he was on the team at the
[1127.16 --> 1132.32]  time but um andrew was a was the co-host with me then um shout out to andrew thorpe by the way
[1132.32 --> 1140.24]  awesome dude um on that show we were talking too about how cool it was that isaac was you know getting
[1140.24 --> 1146.80]  paid by joint to hack on open source npm node all that good stuff so just to sort of paint the
[1146.80 --> 1152.44]  picture for those going back and listening but uh go ahead and continue michael yeah yeah so um they
[1152.44 --> 1157.42]  you know they were employed by joint i'm sure that joint um and people at joint had opinions and and it
[1157.42 --> 1161.68]  influenced the direction of the project that's that's entirely possible um i don't know that it
[1161.68 --> 1170.18]  didn't and i don't know that it did um but when tj fontaine's an amazing developer um he's done
[1170.18 --> 1178.02]  an amazing amount of work on node um but just you know i don't think that um some of the contributors
[1178.02 --> 1182.58]  felt like it was the most obvious choice or that we should really continue with this dictator model
[1182.58 --> 1186.54]  like they're at that point people really didn't feel like it was it was the best choice and and even
[1186.54 --> 1191.80]  a lot of the decisions that isaac had made other contributors felt were really not the right decision
[1191.80 --> 1196.30]  and that we should have had like a real conversation about them but you know we just weren't allowed to
[1196.30 --> 1200.74]  have that conversation like it's it's joint's project there's a new dictator it's tj's project
[1200.74 --> 1205.88]  tj's going to go in whatever direction that he wants to go um and then for whatever reason
[1205.88 --> 1211.04]  releases just kind of stopped um and also uh some some really key developers and some developers that
[1211.04 --> 1216.48]  were contributing a lot sort of checked out um and stopped contributing as much um and there
[1216.48 --> 1220.94]  weren't new people to replace them um so the project so so not only i mean this is like a very
[1220.94 --> 1226.28]  hard position for tj to be in right because not only is he is he taking over the project um and
[1226.28 --> 1230.74]  i'm sure that there are people you know at joint telling him this or that or what to do but also
[1230.74 --> 1236.30]  you know he he lacks like people to even implement all this stuff now and you know like me and a bunch
[1236.30 --> 1240.80]  of other people around going like you know take on this contribution model or take on that governance
[1240.80 --> 1246.26]  model um and yeah it's it's an impossible situation i don't think that any of this is tj's fault
[1246.26 --> 1251.26]  like you know tj's done you know as good of a job as i think anybody can in the situation it's just
[1251.26 --> 1259.52]  a terrible situation and now a word from our sponsor top towel is the best place to work as a
[1259.52 --> 1264.18]  freelance software developer if you're freelancing right now as a software developer and you're
[1264.18 --> 1269.58]  looking for a way to work with top clients on projects that are interesting challenging and using
[1269.58 --> 1275.56]  the technologies you want to use top towel might just be the place for you working as a freelance
[1275.56 --> 1279.98]  software developer with top towel your days of searching for high quality long-term work
[1279.98 --> 1284.94]  and getting paid with your worth will be over let's face it you're an awesome developer and
[1284.94 --> 1289.82]  you deserve to be compensated like one joining top top means that you have the opportunity to travel
[1289.82 --> 1296.06]  the world as an elite freelancer on top of that top talk and help provide the software hardware and
[1296.06 --> 1301.26]  support you need to work effectively no matter where you are head to top towel.com slash developers
[1301.26 --> 1308.12]  that's t-o-p-t-a-l.com slash developers to learn more and tell them the changelog sent you
[1308.12 --> 1317.44]  well it sounds like you guys are taking steps with iojs to avoid the dictator situation the biggest
[1317.44 --> 1323.04]  step being this open and open governance model which you guys proclaim right there on the home
[1323.04 --> 1330.68]  page of of iojs can you tell us about that sure i mean the most important thing for the project is
[1330.68 --> 1336.82]  that at every layer of the project literally every part of it there is a way for you to contribute and a
[1336.82 --> 1343.52]  way for the community to contribute and so um you know it starts at if you're just a user and you
[1343.52 --> 1348.68]  want your voice to be heard and you know what your problems are and your concerns are and those to make
[1348.68 --> 1353.76]  it into the future of the project there's a roadmap repo with some issues where you can just comment and
[1353.76 --> 1357.86]  give us your feedback and that will get rolled up into what eventually ends up being the future of
[1357.86 --> 1362.54]  the project if you want to help us with the website there's a website working group it's great
[1362.54 --> 1367.48]  very easy to get involved um we're spinning up work around documentation around translations
[1367.48 --> 1374.20]  um and then core you know the traditional sort of uh what we've you know forked and replaced from
[1374.20 --> 1380.46]  from node um there's a technical committee which you know was was spun up and started with the
[1380.46 --> 1385.98]  uh traditional committers that had come over from from node into the fork um since then two more
[1385.98 --> 1390.76]  people have been added to the technical committee chris dickinson and uh colin i think it's pronounced
[1390.76 --> 1398.48]  erring they're fantastic um we've also separated sort of the technical committee and and from the
[1398.48 --> 1403.30]  idea of contributorship or getting a commit bit so what we want to do is we want to really bring in a
[1403.30 --> 1406.90]  lot of people that have a commitment and a lot of people actively contributing to the project
[1406.90 --> 1413.52]  and really the tc just focuses on really contentious problems and issues and that's something that we
[1413.52 --> 1418.62]  you know move people into um once they have some history with the project and so the technical
[1418.62 --> 1424.18]  community uses this governance model called um consensus seeking so it's not a pure consensus
[1424.18 --> 1431.10]  model like if if something stays contentious long enough we'll just take it to a vote uh and it'll go
[1431.10 --> 1437.58]  majority wins for the voting um this has you know consensus models get criticized a lot for
[1437.58 --> 1444.18]  incentivizing people saying no or incentivizing kind of stalwartism because if in a pure consensus model
[1444.18 --> 1448.54]  i'm one person if i disagree with you i can literally just hold up the entire process right
[1448.54 --> 1455.94]  so they're they don't they have a bias towards not having any kind of change the great thing about
[1455.94 --> 1460.58]  consensus seeking is that um everyone is incentivized to try and convince their peers of their position
[1460.58 --> 1464.84]  and if you can't convince your peers of the position where you don't care enough you just sort of
[1464.84 --> 1469.12]  feel like okay whatever i'll go with whatever everybody else is doing so you know we have this great
[1469.12 --> 1474.42]  process where we essentially just say hey does anybody disagree and if there's just silence then
[1474.42 --> 1478.62]  we just move along um so we don't even really take things to vote very often it's not like everybody
[1478.62 --> 1484.60]  has to say yay or nay you know it's literally just like is it the direction nobody has any problem with
[1484.60 --> 1489.26]  that okay we're going we're moving along and that's allowed the project to go incredibly fast right so
[1489.26 --> 1495.94]  like i said we've added two new contributors to the project um we've also done you know four releases in a
[1495.94 --> 1504.06]  week um we you know got up an entire new build infrastructure um we we're also you know in i think
[1504.06 --> 1511.24]  in the history of the node project we never had more than eight active committers we're onboarding that
[1511.24 --> 1517.76]  many new committers under the new policy i think like next week um so that's that's pretty phenomenal
[1517.76 --> 1523.82]  so all the committers on the the technical committee or is that a subset yeah the subset the
[1523.82 --> 1528.64]  technical committee is a subset um who's how many people are on that and then how do you get on that
[1528.64 --> 1535.10]  well so that's that's really interesting so um anyone at any time on the tc can just say like hey i think
[1535.10 --> 1539.12]  this person should be on there and then it comes up in the next tc meeting and it falls under the regular
[1539.12 --> 1545.54]  kind of rules but we also have uh like people that we want to have participate in the tc meetings
[1545.54 --> 1550.56]  um but don't necessarily need a vote or even want to vote uh so for instance i actually don't have a vote
[1550.56 --> 1556.28]  on the tc i i tend to i i was facilitating the calls until uh rod vegg stepped up and and he's doing
[1556.28 --> 1561.26]  a great job um so really i'm just there sort of like informing them about some of the other working
[1561.26 --> 1566.66]  groups that are going on we've invited dominic danicola um because he's very well connected to
[1566.66 --> 1573.20]  the v8 team and to tc39 um and we really want to like up the amount of collaboration that we're doing
[1573.20 --> 1577.54]  with those groups so it's great to have him involved in those calls also rod vegg who's the new
[1577.54 --> 1582.32]  facilitator um you know he's built out the whole build system he's doing the releases but he's not
[1582.32 --> 1587.52]  actually a voting member of the tc um and and you know if you if you look at the contribution that he
[1587.52 --> 1593.28]  actually does to core there's not that many because he's working on nan which is like the binary build
[1593.28 --> 1596.94]  interface or the binary interface which is a separate project he's working on build which is a separate
[1596.94 --> 1605.06]  project so um you know we've we've upped the collaboration um and uh the the tc we really just
[1605.06 --> 1609.88]  want it to be okay here are the the people that we all trust to make the right technical decisions
[1609.88 --> 1614.62]  at a low level in the project they don't have to be involved in everything and we're breaking a lot
[1614.62 --> 1618.96]  of stuff off into working groups when we know that other people are going to be better at kind of
[1618.96 --> 1623.24]  fixing them and delegating all of that authority and that autonomy to those groups right so you know
[1623.24 --> 1627.52]  the website group is allowed to make decisions without going to the tc it's just its own working group
[1627.52 --> 1634.62]  and that's its own contributorship it just rolls along and the same is true of build the uh the members of the
[1634.62 --> 1640.54]  tc though they do have the final authority over the project though right so they if it doesn't pass
[1640.54 --> 1648.94]  the tc then whatever the concern is whether it's a voting a new member something technical um policy
[1648.94 --> 1654.02]  change whatever it might be it's got to go through the tc to get you know and then that that subsequent
[1654.02 --> 1661.70]  meeting to to sort of get approved is that the right method that you're all uh yes um for iojs kind
[1661.70 --> 1668.54]  of core um there i mean i'm working on the the working group policy right now but um as it stands
[1668.54 --> 1672.56]  i think what will help what will end up happening is that the um the working groups will have a lot
[1672.56 --> 1677.90]  of autonomy and be able to make decisions um totally outside of the tc that's sort of the point of the
[1677.90 --> 1683.86]  working group is to break off this responsibility out of the tc um but also i think that it's it's the
[1683.86 --> 1688.84]  wrong way to look at it um saying that everything goes through them because that makes it seem like
[1688.84 --> 1694.04]  there's a funnel and all the work kind of has to be approved where in reality the work is just going
[1694.04 --> 1698.92]  on and most work that ends up happening and getting merged um you know it goes through review process
[1698.92 --> 1704.48]  it's not contentious ever it just sings along you know we have releases without the entire tc buying
[1704.48 --> 1711.44]  off as well um really the tc only deals with issues of contention where you know we don't agree
[1711.44 --> 1719.32]  about something um so i'm assuming that the reason for this governance uh was this based on anything
[1719.32 --> 1725.62]  prior to that and the reason for implementing this was probably largely because of the stagnation that
[1725.62 --> 1732.04]  happened in node original and then sort of the the break off from there because that wasn't in place
[1732.04 --> 1737.30]  there is is that why this is in place now not so much to provide more red tape or the opportunity for
[1737.30 --> 1742.60]  red tape but just to provide some sort of model where the community in fact does guide this project
[1742.60 --> 1751.82]  yeah i mean so the the the origins of this go all the way back to um last july uh i sort of built out
[1751.82 --> 1758.20]  a proposal that we hoped to get joined on board with um which obviously didn't happen uh and then when we
[1758.20 --> 1764.02]  ended up doing node forward we sort of like revive like revive that um and initially it was actually
[1764.02 --> 1768.64]  called the bootstrap voting model because the the purpose of it is not to define all the governance
[1768.64 --> 1774.24]  rules forever it's actually just to get us some governance rules so that we can iterate on the
[1774.24 --> 1780.16]  governance rules as we go along so if something doesn't work we can just change it um you know
[1780.16 --> 1784.78]  none of this governance is sort of stagnant um a lot of the initial stuff that we put together
[1784.78 --> 1790.10]  um you know we did a lot of research and and had a lot of conversations about what the best approach
[1790.10 --> 1794.56]  was a lot of it's worked out just really well so we haven't felt the need to change it um in fact
[1794.56 --> 1799.22]  mostly what we've done is we've documented it a lot more we we've described the process and the
[1799.22 --> 1805.46]  the way in which um the governance model is actually implemented um a lot better you know so we talked
[1805.46 --> 1809.40]  about you know having this tc governance model and making these decisions but we didn't talk about
[1809.40 --> 1814.80]  like they happen on this tc call that happens every week and you know how do you you know call or not
[1814.80 --> 1820.50]  call for a vote and how do you move along in the agenda and that kind of stuff so i mean man it
[1820.50 --> 1826.58]  feels like uh you've you've broken free from the shackles of a dictator and you're now forming your
[1826.58 --> 1834.26]  brave new world and you and you're you know you got to set up a government uh very much you know it
[1834.26 --> 1839.94]  hearkens at least a little bit to me to the u.s constitution where they built in the ability to amend it
[1839.94 --> 1844.54]  if there's because knowing that they didn't have everything figured out and things would change
[1844.54 --> 1849.56]  sounds like the bootstrap model is very much the we're gonna we're just gonna get us enough
[1849.56 --> 1853.80]  so that we can get going and we're gonna figure everything else out as we go it's very
[1853.80 --> 1860.62]  software-y yeah yeah and it's it's worked better than any of us could have ever imagined i mean when
[1860.62 --> 1865.96]  i said that i'm a janitor right now i was not exaggerating like um we have so many new contributors
[1865.96 --> 1870.76]  coming in and so much stuff happening that um all i'm really trying to do is is keep up with them
[1870.76 --> 1874.54]  um and make sure that everybody is still enabled and it's clear where everybody can contribute
[1874.54 --> 1881.40]  i think uh you know so for the listener's sake listening to all this and trying to figure out
[1881.40 --> 1887.32]  we're probably like 25 minutes into the show ish somewhere around there and you know we've had
[1887.32 --> 1893.02]  conversations like this in the past around the node community and now iojs and what's happening
[1893.02 --> 1898.14]  here and i think the reason for this last 25 minutes was really to sort of paint a picture
[1898.14 --> 1903.52]  of what the history has been and what's gotten us to today uh prior to some sort of technical
[1903.52 --> 1910.38]  conversations um you know just just to sort of get a snapshot of what's happened why the governance
[1910.38 --> 1917.34]  you know why the community had a change of heart why the fork button was you know pushed uh
[1917.34 --> 1924.02]  and sort of why we're why we're at where we're at um trying to think that the next direction here i
[1924.02 --> 1928.54]  think you know maybe let's let's move on to some more highlights i guess for ios i mean one of the
[1928.54 --> 1933.98]  bigger highlights is bringing es6 to the community that was something that you know some members of the
[1933.98 --> 1939.60]  community seem to want and some others could live without um you know in terms of like stagnation and
[1939.60 --> 1947.44]  the next version what uh you know what is in y'all move december um what is in this latest version of
[1947.44 --> 1952.16]  version one which actually is unstable and you've got reasons why you say that what's what's in this
[1952.16 --> 1957.34]  latest version aside from just yet uh es6 and all the greatness that comes with that what's what's new
[1957.34 --> 1963.26]  and happening well so i will say that you know the the first release uh i talked about that roadmap
[1963.26 --> 1967.86]  repo earlier right um which is like a place where you can sort of voice you know what you think is
[1967.86 --> 1973.04]  is wrong with node or where you'd like to see it go so the top things that we saw in there were
[1973.04 --> 1980.64]  uh more releases please i would love to have releases right um es6 was a huge one um and could
[1980.64 --> 1984.28]  you please move to send there and stop with this weird even odd thing that nobody understands
[1984.28 --> 1990.26]  so we did all of those um and it turns out that we actually get the es6 stuff basically for free
[1990.26 --> 1996.34]  uh just by taking a modern v8 so the v8 that ships in the last stable version of node
[1996.34 --> 2002.34]  is so old that they don't fix critical bugs anymore wow and you know even the one that i
[2002.34 --> 2007.26]  the last time i checked was planned for 0.12 is even behind where we are now so one of the decisions
[2007.26 --> 2012.28]  that we actually made in the last tc meeting um is to come up with a way to to track with v8 really
[2012.28 --> 2018.44]  really closely so that you know we have an unstable line that we're working on and in there we're taking
[2018.44 --> 2023.62]  uh the unstable version that v8 is working on for the next chrome release so when we find bugs
[2023.62 --> 2026.96]  they're actively engaged in fixing those bugs and those performance regressions and we can
[2026.96 --> 2032.02]  collaborate more closely together and then once every six weeks those are going to come into those
[2032.02 --> 2035.40]  are going to land in a chrome and they're going to be considered stable and then you know we can say
[2035.40 --> 2041.30]  okay now we know that this v8 is stable it's our stuff stable okay now here's the stable release
[2041.30 --> 2047.02]  so yeah i mean there's a bunch of es6 features as dictated by v8 um you know we're not going to go in
[2047.02 --> 2050.74]  and turn them off just because some people don't like them or whatever we're just we're going to take
[2050.74 --> 2055.78]  v8 as is so that's that's a big win for a lot of people i was gonna say are these features these
[2055.78 --> 2061.02]  es6 features intrusive into existing code bases like if i don't want those features could they
[2061.02 --> 2066.56]  possibly mess up what i'm currently doing it seems like they would be new apis no because well the
[2066.56 --> 2071.02]  thing about uh ecma script right and javascript in general is that you can't break the web so
[2071.02 --> 2075.32]  everything has to be somewhat reverse compatible right you can't break a bunch of existing code that's
[2075.32 --> 2079.90]  out there right um so we don't really need to worry about that um you do have forward
[2079.90 --> 2085.06]  incompatibility though right so if people are now building a bunch of modules and putting them in
[2085.06 --> 2090.62]  npm uh they use these new features um and they're not doing any kind of like you know compile down
[2090.62 --> 2099.24]  steps or anything like that um they're not going to work in node 012 and node 010 um so and you know
[2099.24 --> 2103.82]  potentially as they add more features there may even be versions of iod.js that don't have those
[2103.82 --> 2109.28]  um but we've there's a lot of threads right now on the best way to handle that and you know is it
[2109.28 --> 2114.46]  npm tooling is it cross compilation all that kind of all that goodness and according to your guys is
[2114.46 --> 2119.56]  uh yes six pages sounds like there's a few features that are still behind the flag namely classes um
[2119.56 --> 2125.36]  object literal extensions and symbol to string tag which i'm not familiar with that one um but the
[2125.36 --> 2131.02]  majority of everything else let const generators just the whole kit and caboodle besides those
[2131.02 --> 2137.28]  a few subsets uh are all in there why why classes and object literal extensions didn't make the cut
[2137.28 --> 2142.96]  um i mean that that's the v8 team doesn't feel that they're stable okay so just completely whatever v8
[2142.96 --> 2148.74]  shipping you guys are shipping right right exactly and um you know i think that going forward we're not
[2148.74 --> 2153.96]  actually going to see a lot of people publishing modules that rely on features behind flags um in in the
[2153.96 --> 2160.34]  past we actually did have um a bunch of people uh including a tj holloway chuck you know build a little
[2160.34 --> 2168.78]  ecosystem around generators which um in node 010 uh requires like a recompile and in 011 012 uh is
[2168.78 --> 2173.94]  still behind a flag um or at least in the existing 011 releases i don't know what 012 will take when it
[2173.94 --> 2178.28]  goes out so you know that's a huge barrier to entry for using those features but you know people were
[2178.28 --> 2182.26]  clamoring for them so much and it was just so unclear when the next version of node would come out that
[2182.26 --> 2187.24]  people were were really going the extra mile i think that now that we're you know shipping quickly
[2187.24 --> 2191.62]  and that releases are coming out you know on time and that we're taking new v8 features as best the
[2191.62 --> 2195.74]  v8 team is doing them i really don't think that people are going to you know do more than play
[2195.74 --> 2201.36]  around and test uh stuff behind flags so you guys were it's like you guys were excited to get this
[2201.36 --> 2207.10]  version 1.0 out there but yet on your home page it says that you know the choice to release this as
[2207.10 --> 2213.20]  1.0 was not to signify that io js should be considered production ready but because it was a
[2213.20 --> 2219.74]  significant enough release from node.js to warrant a major version increment now semver means 1.0 is
[2219.74 --> 2224.68]  production ready right and this is specifically not production ready so help help me out here
[2224.68 --> 2230.98]  uh well i mean i think it's in my opinion it's as production ready as any release of python or ruby but
[2230.98 --> 2238.16]  um and and that's really not a dig at them it's just a node is incredibly stable and in huge
[2238.16 --> 2244.78]  production use cases that you like i don't know of any any scale um anything where uh python or ruby
[2244.78 --> 2249.88]  is at that scale and the node that you've been using for a long time has been at 1.0 quality for
[2249.88 --> 2256.76]  you know at least a full major release cycle um i think that the reason why we state really strongly
[2256.76 --> 2262.98]  that it is considered unstable is that we are tracking an unstable version of v8 um and because
[2262.98 --> 2267.70]  you know we have a brand new release process and a brand new build process um so if there are any built
[2267.70 --> 2273.42]  like kinks and stuff in that also you know we've taken a lot of work that was going into 012
[2273.42 --> 2280.96]  um and while a lot of people do follow the 011 lines um this stuff just hasn't shipped and hasn't
[2280.96 --> 2286.36]  been tested that much um because of this you know giant lack of releases and actually getting code out
[2286.36 --> 2292.22]  of the wild so we really want people to to pull down even that work um as well as some of the work
[2292.22 --> 2297.66]  that's only happened in iojs as well as the new v8 um and tell us you know how stable it is and
[2297.66 --> 2303.08]  verify that there's no regressions and you know we have found some performance regressions um i was
[2303.08 --> 2307.28]  seeing them pop up the other day some of them we we fixed uh because they were in our code some of
[2307.28 --> 2311.84]  them are in v8 and now they're logged and luckily they are logged against a version of v8 that the v8
[2311.84 --> 2316.46]  team is actively working on and doesn't like performance regressions in so you know going forward you
[2316.46 --> 2321.78]  know once that v8 is stable very soon after that you'll see a stable release of node um and then
[2321.78 --> 2329.26]  it'll be really clear where the lines of delineation are around stable unstable um also we in the
[2329.26 --> 2334.58]  beginning we really wanted to make it clear that we're moving to semver um and that we we have a
[2334.58 --> 2341.38]  much cleaner more organized way of doing these version numbers um since then we've we've gotten a
[2341.38 --> 2349.22]  little deeper into what it looks like to take um v8 as it's unstable and if we want to do that in
[2349.22 --> 2355.18]  strict semver or if we want to go you know dash pre one dash pre two while we're in that unstable mode
[2355.18 --> 2359.24]  so that may change after the first stabilization phase just to make it a lot clearer to everybody
[2359.24 --> 2367.08]  and now a word from our sponsor digital ocean a simple cloud hosting provider built for developers
[2367.08 --> 2371.98]  we've been working with digital ocean for quite a while we host ourselves on digital ocean we love
[2371.98 --> 2377.98]  digital ocean and we think you'll love digital ocean too in 55 seconds that's how long it takes to
[2377.98 --> 2382.86]  provision a brand new server you'll have a cloud server with forward access and it just doesn't
[2382.86 --> 2388.28]  get any easier than that pricing plans are just five bucks a month for half a year ram 20 gigs of ssd
[2388.28 --> 2396.00]  drive space one cpu and one terabyte of transfer in fact digital ocean is ssd only they're an ssd only
[2396.00 --> 2402.26]  cloud ssd hard drives three one bandwidth kvm virtualization they got an awesome control panel
[2402.26 --> 2410.72]  to use amazing hardware built on the hex core machines with dedicated ecc ram and raid ssd cloud
[2410.72 --> 2416.90]  storage you're gonna love digital ocean use our promo code changelog to get a 10 hosting credit when
[2416.90 --> 2422.74]  you sign up again that code is changelog and you'll get a 10 hosting credit when you sign up and now back
[2422.74 --> 2429.30]  to the show this is sort of send a message then i mean it sounds like i mean obviously note has been
[2429.30 --> 2435.70]  out there and this is you know to a degree a fork as as you've already mentioned how it is or isn't a
[2435.70 --> 2439.82]  fork in the show already but it's really around the new things that are happening build process
[2439.82 --> 2446.28]  and various processes that sort of make it unstable so to speak yeah yeah and and i mean you know like
[2446.28 --> 2453.80]  we're we're very confident um that it's awesome uh but you know nothing is going to make us fully
[2453.80 --> 2458.40]  confident in calling it stable until other people run it in production and tell us that it is and and
[2458.40 --> 2463.06]  they're doing that now that we have releases this is somewhat off topic but i'm kind of curious because
[2463.06 --> 2467.32]  you know jared i'm just sitting here thinking about like we've we've said several times in the past
[2467.32 --> 2472.68]  i don't know how many shows but we've either alluded to or directly said how difficult and how
[2472.68 --> 2478.58]  time consuming and how hard open source is and like i can only imagine how much time aside from
[2478.58 --> 2486.52]  your day job at digital ocean how much time you spend um not just contributing back but i guess
[2486.52 --> 2492.26]  sacrificing for open source sacrificing for you know your life and your time whether you love it or not
[2492.26 --> 2499.08]  um how much time you spend and others spend making this open source possible i mean it's gotta take a ton
[2499.08 --> 2504.92]  of time yeah i mean i i will say that it was um it was a bit of a sacrifice and a little a little bit
[2504.92 --> 2509.64]  hard uh back when we were you know just trying to negotiate with joyant and and these companies like
[2509.64 --> 2514.98]  that took a toll on me much more than anything right now is taking a toll on me um also one of the things
[2514.98 --> 2520.42]  that i figured out and this project kind of continues to prove is that it's not just about what you do
[2520.42 --> 2527.24]  it's about what you don't do and when you step away um so i mean what i've been really doing a lot
[2527.24 --> 2531.86]  of is i'll i'll jump in i'll i'll bring some organization to something have some conversations
[2531.86 --> 2537.28]  get things moving um get things into a state where there's something there and there's a clear way to
[2537.28 --> 2542.96]  contribute to it and a clear way to move it forward um and then take all the people that are now
[2542.96 --> 2546.24]  contributing and make sure that they feel comfortable making decisions that they feel comfortable
[2546.24 --> 2551.22]  you know moving this forward on their own and then i just get the hell out um and a lot of it is a
[2551.22 --> 2556.36]  is just about what i don't do i mean i i actually don't merge a lot of people's pull requests um
[2556.36 --> 2561.50]  i you know make them merge it themselves um you know like this this was happening in the website
[2561.50 --> 2564.74]  because you know we had to spin up this website team really quickly so we gave a bunch of people
[2564.74 --> 2569.78]  commit privileges um but a lot of them were like oh what are the rules around actually putting this
[2569.78 --> 2574.14]  in and like you know do i have the authority to do this just because of a commit bit so it you know
[2574.14 --> 2579.00]  they were looking to me and rather than merge it i just said no you merge it right now and just do
[2579.00 --> 2585.24]  that in the future um and you know coming back to the the node project and some of the problems
[2585.24 --> 2589.66]  that it's had a lot of it has been that there has been a centralization of control around a few
[2589.66 --> 2596.92]  people not just the dictator or the corporate owner but like the even just the committers right and the
[2596.92 --> 2600.72]  the more that you try to control all of that the more that they just become a bottleneck and that
[2600.72 --> 2606.22]  other people check out of the process yeah i think the reason why i also mentioned that too is
[2606.22 --> 2613.24]  is just when you with you know with the proverbial drama or with all the change and new process and
[2613.24 --> 2619.26]  all the motion that's happened from node to iojs and all the traction you guys and the rest of
[2619.26 --> 2623.80]  the community have uh have placed into this you know we've had several guests on the show that talk
[2623.80 --> 2629.48]  about past uh run times of burnout for themselves you know where they sort of no matter how much they
[2629.48 --> 2634.52]  care about something they sort of hit a brick wall and you know i see all of you all you know
[2634.52 --> 2640.32]  contributing so much and you love it i can tell you love it you know we can both jared i can both tell you
[2640.32 --> 2647.26]  love it um but i guess the caution i concern myself with is like um you know how how much of a toll does
[2647.26 --> 2653.70]  this take on um a certain core team a certain core membership of the team or a certain core people
[2653.70 --> 2659.60]  in the committee the tc um on their lives to sort of make it happen to make this you know day-to-day
[2659.60 --> 2667.42]  happen well i i remember we we had a one of the first tc meetings that we had um uh ben nord who was
[2667.42 --> 2672.58]  uh was on it and somebody mentioned something about like okay i'll go through and i'll triage
[2672.58 --> 2676.64]  all of the bugs or i'll go through and i'll review all of the pending pull requests for the last like
[2676.64 --> 2683.44]  six months and in node or whatever and see if we can merge them over and uh and ben cautioned like he
[2683.44 --> 2688.82]  was like you know don't take that on indefinitely it's soul-sucking work like you will burn yourself
[2688.82 --> 2695.38]  out um speaking like you know from experience and um i mean one of the great things about the project
[2695.38 --> 2701.16]  right now is that we've seen so many people flock to it and contribute and now it's it's not it's
[2701.16 --> 2707.18]  not on one person anymore um and i i think for the first time like a lot of people that are on the tc
[2707.18 --> 2716.28]  right now weren't super active uh in node core uh towards the the like within the three to four month
[2716.28 --> 2721.86]  period uh before we we did iojs um they had started to check out quite a bit and they're also really
[2721.86 --> 2726.98]  busy people um and i think that they they probably really don't want to be in these tc meetings
[2726.98 --> 2733.46]  forever um they're looking for a way out you know they're not looking for the door but um you know
[2733.46 --> 2737.76]  they would love it if they just didn't have to worry anymore and they knew that there were a ton of
[2737.76 --> 2742.38]  people um you know qualified and the tc and everything is running and they can just like go and run their
[2742.38 --> 2747.78]  business or whatever you know isaac luter is like the ceo of npm inc right now it's a growing company
[2747.78 --> 2754.04]  like they have this investment i mean he has a lot of things to do that aren't being on these tc calls
[2754.04 --> 2758.52]  i'm sure that he would love to get off of them as soon as we have people step up and and we have
[2758.52 --> 2762.02]  people stepping up and we have people growing into the project so it's looking great so i guess it's
[2762.02 --> 2769.12]  the the the light shining back on the you know as jared mentioned you know kind of um casting light on
[2769.12 --> 2773.52]  the american constitution and the you know ability to amend it and sitting at the government that whole
[2773.52 --> 2781.80]  mindset is is uh sacrificed now but you know it's more of a a long-tail approach to a more uh not
[2781.80 --> 2789.88]  only just a more mature um software release but a a more healthy um team people making it happen day
[2789.88 --> 2796.60]  to day yeah yeah and um also i mean the thing about these working groups that we're spinning up to um
[2796.60 --> 2801.22]  they offer people the opportunity who may not even be programmers to participate in a particular way
[2801.22 --> 2806.80]  and even to become leaders in a particular area you know um like we're spinning up one sort of about
[2806.80 --> 2811.98]  um like evangelism pretty soon um which is like you know helping with the social media stuff and the
[2811.98 --> 2815.80]  messaging and like you know keeping a good list of people that can speak at conferences and all that
[2815.80 --> 2822.72]  um and you know there will be i i really hope to see people contribute there that you know aren't just
[2822.72 --> 2828.54]  programmers and aren't just code contributors additionally though we have um stuff like the roadmap
[2828.54 --> 2835.12]  you know that could be attractive to a tc member and it could you know take time away from their other
[2835.12 --> 2839.60]  technical work but could also be really valuable and could actually be where they want to put more
[2839.60 --> 2844.28]  of their sort of influence i know that like uh bert belder for instance is really wants to help and work on
[2844.28 --> 2850.16]  the roadmap stuff so and is super interested in that so a lot of this is like offering up the
[2850.16 --> 2856.58]  opportunity for people to go and do work that they're well qualified to do and that they'll they'll see a lot
[2856.58 --> 2862.96]  of benefit from but also we as a project see a huge amount of benefit sounds like it's fun again too at
[2862.96 --> 2868.82]  least for the time being there's a renewed enthusiasm you have a lot more people who are diving in who may
[2868.82 --> 2877.14]  have burnt out or lost interest and there's it seems to be a vigor around the program or the project and
[2877.14 --> 2881.68]  yourself i mean you sound very excited about it that usually fights off that burnout are you feeling
[2881.68 --> 2886.34]  more excited are you feeling vigorous are you is it are you feeling good about things oh definitely
[2886.34 --> 2893.42]  yeah oh definitely i can tell yeah yeah uh no it's it's been great i mean i i was very optimistic and
[2893.42 --> 2897.46]  i had really high hopes for what would happen and and you know a vision for like how many people that i
[2897.46 --> 2902.00]  thought would come and uh it turns out that i was actually being quite pessimistic in in my numbers
[2902.00 --> 2906.34]  and what i thought people would show up and do um i mean the other day somebody showed up and was
[2906.34 --> 2911.54]  like hey i registered a soundcloud account and set up like a podcast feed of all of the tc
[2911.54 --> 2916.98]  meetings with just the audio um i was like wow i hadn't even thought of that yeah and it already
[2916.98 --> 2922.66]  exists it's great it's really great there's probably people that want to listen to that too which is
[2922.66 --> 2929.16]  awesome um so let's talk about the transition because obviously it's a transition from one project to the
[2929.16 --> 2936.48]  other um as a user you know if i've been a long time node user what are my steps to get onto the iojs
[2936.48 --> 2946.42]  you know bandwagon um so i mean so i mean if you have stuff in production or even if you have like
[2946.42 --> 2950.90]  a really great local dev environment i mean dip your toe in the water before you just jump in um
[2950.90 --> 2956.40]  so nvm uh which is like the node kind of version manager it's like a set of shell scripts that will
[2956.40 --> 2961.78]  just install and manage the the version of node that you're currently running that supports iojs so
[2961.78 --> 2966.82]  just use nvm install iojs and then you can run and play around with iojs you can see which of your
[2966.82 --> 2973.50]  projects work and which ones don't there's a there's a list of native modules like like modules that bind
[2973.50 --> 2979.68]  in some way to c++ that um need to get fixed um actually that's that's another phenomenal story of
[2979.68 --> 2985.74]  contributors showing up um tim oxley uh just started a thread where he was like let's compile a full list
[2985.74 --> 2990.56]  of all the modules that need to get updated um and you know get people to go and do stuff on each one
[2990.56 --> 2994.58]  so within a day he had like a full list of you know like 40 native modules that needed to go
[2994.58 --> 3000.76]  um and then i think only shortly after that there was a pr link next to every single one of them
[3000.76 --> 3004.96]  and now it's just a matter of those getting tested and actually released by all those projects so
[3004.96 --> 3012.34]  that's awesome um that's going very fast so you know if you if you can run all of your code um on
[3012.34 --> 3018.80]  iojs please do it please tell us about any sort of bench like any benchmarks that might be off um but
[3018.80 --> 3023.82]  it should just run um and you know it should be backwards uh compatible with everything so
[3023.82 --> 3029.58]  it should just be better i mean that's it you know it intends to be a drop-in replacement you
[3029.58 --> 3036.02]  know by default we do also have a node alias to iojs by default you know we're there to sort of
[3036.02 --> 3042.24]  supplant the the prior node that was there um so that i mean and especially once we stabilize like
[3042.24 --> 3047.90]  it should be really easy and really simple um and if there are any sort of gotchas or hang-ups
[3047.90 --> 3053.46]  um you can expect the documentation around that to be pretty fantastic so awesome and as far as
[3053.46 --> 3058.48]  roadmap goes obviously you've you've caught up with v8 you're going to keep up with v8 regular release
[3058.48 --> 3063.10]  cycles it sounds like you guys are getting that figured out um so once that kind of gets in place
[3063.10 --> 3068.82]  i know you have the roadmap repo but that's it seems like a conversation anything that's like
[3068.82 --> 3072.32]  in the roadmap for sure that's going to happen over the next two or three months
[3072.32 --> 3080.66]  um i don't think that there's anything certain um i think um there's definitely some more streams
[3080.66 --> 3087.44]  updates coming in so um a readable stream module was was brought into iojs there's a working group
[3087.44 --> 3093.04]  around streams um that's getting rolled into you know further releases of nodes so that require stream
[3093.04 --> 3098.54]  will just be that readable stream uh there's also work that dominic nicole has been doing um
[3098.54 --> 3103.98]  for working group streams um and we want to make sure that any incompatibilities between these two
[3103.98 --> 3109.82]  apis any functionality that can't be polyfilled um is reconciled now in the standardization phase
[3109.82 --> 3115.14]  once that's done uh i expect that to move in a direction where it's very easy to interoperate
[3115.14 --> 3120.40]  between what wg streams and streams to come out of node in terms of other roadmap stuff i mean
[3120.40 --> 3125.76]  that hasn't been decided yet because you know my my next task really is to jump into the roadmap repo
[3125.76 --> 3131.60]  um and figure out more ways of pulling in feedback from the community um and figuring out what people
[3131.60 --> 3137.20]  want out of node next um and you know that's the direction that i expected to go in awesome we'll
[3137.20 --> 3142.32]  definitely link up that uh roadmap repo in the show notes you can get those show notes at the
[3142.32 --> 3150.88]  changelog.com slash podcast slash 139 uh all the relevant links will be there i do have a i'm about
[3150.88 --> 3155.34]  ready to wrap up here adam but i do have one i guess kind of it's not off topic but it's tangential
[3155.34 --> 3160.40]  and kind of a personal question for you michael uh because you've been running the node conf right
[3160.40 --> 3166.50]  and so i'm starting to wonder what happens with node conf well i mean the community is still
[3166.50 --> 3172.14]  called the node community we still install a binary called node okay um or it's an alias i guess now but
[3172.14 --> 3177.88]  um you know we're not going to rebrand the community we we you know we consider the project
[3177.88 --> 3183.00]  sort of the future direction of core um we don't want to split or bifurcate the community
[3183.00 --> 3187.50]  um and in fact like you know we're we're sort of just waiting for joint to come around and
[3187.50 --> 3193.86]  and just join the project to be honest um and you know lead the way uh in doing some kind of uh
[3193.86 --> 3199.24]  foundation but you know we we have figured out you know a better democratic model for running the
[3199.24 --> 3205.02]  project um we have a huge amount of success now we're sort of done having that conversation because
[3205.02 --> 3210.90]  we've we've solved it and it's going incredibly well um but we you know we would like it to exist
[3210.90 --> 3216.30]  in some kind of a neutral party we would like joint to get back on board so we're sort of still waiting
[3216.30 --> 3221.72]  around for that so ideally would it would io eventually loop back into node and and we'd go
[3221.72 --> 3227.64]  back to node only under the open governance model or yeah yeah i mean as as long as there's not
[3227.64 --> 3231.96]  as long as there's no owner that can kind of pull stuff out from under us like as long as you know
[3231.96 --> 3238.52]  the the website uh you know domain is actually owned by this neutral party and stuff like the
[3238.52 --> 3241.76]  trademark is actually owned by this neutral party so it's not like hey you guys use this for a while
[3241.76 --> 3246.76]  and then later we'll that we might be able to change it yeah um but you know it's it's a pretty
[3246.76 --> 3252.16]  obvious path to that yeah um and we we hope to see them come around yeah what a success story that
[3252.16 --> 3258.16]  would be yeah yes yeah that that would be it would be nice i mean it's good when everybody
[3258.16 --> 3263.68]  plays well anyway so hopefully you know for the betterment of the community there there can be
[3263.68 --> 3272.04]  just eye to eye speak across the across the channels yeah well michael it's definitely been
[3272.04 --> 3278.20]  great having on the call i know that uh we we sort of sort of cut ties with the the call so to speak
[3278.20 --> 3282.00]  and go into some kind of neat questions we have here at the time of the show to sort of
[3282.00 --> 3287.94]  give us a deeper view of the guests we just had on the show and and you're that guest so the the
[3287.94 --> 3293.50]  favorite question that our listeners like to hear about is who is your programming hero and you can
[3293.50 --> 3300.72]  have one you can have several it's up to you um i mean so historically i think um i just don't know
[3300.72 --> 3307.26]  of anyone programming today that does stuff uh as cool or as clever as what i read about was doing
[3307.26 --> 3314.38]  back in the day in the 70s um it's just insane the stuff that he did i've never met anyone or even
[3314.38 --> 3320.68]  heard of anyone uh quite that talented um i think today though like actually active programmers um
[3320.68 --> 3327.40]  probably rod vegg um he's been you know he built out the build system has been has been uh he runs
[3327.40 --> 3332.38]  the tc meetings now as well um i don't do them i don't run them anymore he's a fantastic developer
[3332.38 --> 3340.06]  obviously but he's also played this huge role in leading the community forward so this more
[3340.06 --> 3345.26]  liberalized uh contributor model that we've moved to um that was actually pioneered by him uh called
[3345.26 --> 3350.12]  open open source uh in the level up ecosystem and all the level to be stuff that's going on a node
[3350.12 --> 3355.62]  he also played a really pivotal role in getting uh node school off the ground um and at the same time
[3355.62 --> 3359.78]  you know he's taking on all these like really important leadership roles and code roles in iojs
[3359.78 --> 3364.98]  so yeah he's he's been uh amazing to work with and a real hero lately
[3364.98 --> 3373.38]  awesome um next question is what's the call to arms i think we've talked heavily about the history
[3373.38 --> 3377.90]  obviously it probably dipped in a little bit into the call to arms but i think jerry your question
[3377.90 --> 3382.82]  prior to this was probably the best which is you know if you're currently using node how do you begin
[3382.82 --> 3389.62]  to enjoy the iojs goodness um but aside from that um i think the question is a little bit
[3389.62 --> 3395.90]  let's let's make a little more open-ended not just a call to arms to iojs and how people can
[3395.90 --> 3401.96]  contribute but um also keep up because it's moving so fast changes are happening quickly what's the
[3401.96 --> 3408.22]  easiest way to keep up and what's the best way to step in and start making some impact regardless of
[3408.22 --> 3416.02]  programming depth whether you're a new coder or a seasoned veteran so very soon you'll be able to
[3416.02 --> 3421.18]  sort of go to the iojs github org and look through the repos and have a clear like that's something that
[3421.18 --> 3424.06]  i could work on that's something that i couldn't that's something that i could contribute in some way
[3424.06 --> 3430.10]  to um and in each of those readmeans you should see a very clear way to do that contribution um
[3430.10 --> 3435.46]  but i i'm really interested in sort of what people can do you know in a pure community kind of way
[3435.46 --> 3440.66]  um really like just growing the community teaching people um and so there's a bunch of things that you
[3440.66 --> 3447.58]  can do there you can run a node school uh which is like a free programming uh workshop format there's
[3447.58 --> 3451.84]  a ton of them they're all interactive so you just sort of npm install this workshopper and then
[3451.84 --> 3457.22]  jump jump through it um there's a huge amount of resources on node school.io on how to get those up
[3457.22 --> 3463.00]  and running and and how to you know mentor them there's a great process actually for you know you get a
[3463.00 --> 3468.46]  repo for your upcoming node school and then you should add everybody as an owner to it that comes
[3468.46 --> 3473.48]  to the node school so that um you're actually creating a support network locally for helping
[3473.48 --> 3479.10]  them even after they leave the event and people will ask questions there that they would never ask in any
[3479.10 --> 3483.72]  of the the big forum global forums because they're just too scared but because it's just people that
[3483.72 --> 3489.92]  they just met um they have no problem with it uh and you know in in addition to sort of like the the
[3489.92 --> 3496.30]  local meetup scene um one thing that i've seen be really successful is uh oakland js so oakland js is
[3496.30 --> 3501.68]  uh there's no talks there's no speakers it's just we every week every week at the same time at the
[3501.68 --> 3509.02]  same bar we just hang out um we just and just talk about stuff and it's become this amazing support
[3509.02 --> 3513.42]  system for the community and the culture locally and you know we've had a lot of people brand new to
[3513.42 --> 3517.50]  programming that find out about it and then like that's like the only thing they do for the first
[3517.50 --> 3520.58]  month of their programming is like they come to this thing and they keep talking to everybody and
[3520.58 --> 3526.24]  they get really involved um and that's just been awesome so you can totally run you know your own
[3526.24 --> 3531.00]  of those it's very simple there's literally no setup and and surprisingly it's easier to run something
[3531.00 --> 3536.90]  weekly than monthly um because it's just not this this big production uh people you know don't feel
[3536.90 --> 3541.46]  quite as obligated or quite as stressed out about going so some people go one week they come back the
[3541.46 --> 3547.68]  next week who knows um it just it stays really informal but it's also uh consistent which is
[3547.68 --> 3551.96]  great and now there's going to be a sunset js actually in in san francisco which will be pretty
[3551.96 --> 3557.62]  cool um yeah and also uh if you have a bit more chops if you've been organizing meetups and stuff for
[3557.62 --> 3562.54]  a while um you can run what's called a node conf one shot which is just a one-day conference really
[3562.54 --> 3567.12]  simple really stripped down we have documentation on like here's the best way to do a cfp and the kind
[3567.12 --> 3571.28]  of stuff you need to worry about and how to do the ticketing and um you know we help out with some of
[3571.28 --> 3575.62]  the promotion and we get you on the one shot site so um yeah those are all ways that you can just
[3575.62 --> 3581.96]  kind of do pure community stuff awesome i'm sure i'll have tons of fun uh finding all the links for
[3581.96 --> 3586.44]  the show notes so if you're listening and you're like man like i want to go grab that link go to the
[3586.44 --> 3593.38]  show notes uh assuming i took the time which i will to go and find all these links um yeah we like to
[3593.38 --> 3597.10]  put some awesome show notes in there for the listeners because it really just helps you know you can
[3597.10 --> 3601.82]  listen and sort of be running or working out or gardening whatever people do when they listen
[3601.82 --> 3606.48]  to the change logo i don't know people commute and they listen so they're not always like ready to
[3606.48 --> 3612.84]  take down links or go go to the google and search around and stuff so kind of depends but uh yeah i
[3612.84 --> 3618.58]  think that's pretty much um that's pretty much the show you know i think that uh it's been great
[3618.58 --> 3622.36]  having you on the show is there anything that you want to mention prior to us closing out michael
[3622.36 --> 3626.66]  uh no not that i can think of it's been fantastic thank you awesome
[3626.66 --> 3632.70]  well uh we do have some awesome sponsors for the show that i do uh want to mention
[3632.70 --> 3638.66]  code chip top towel and we did put the asterisk disclaimer on there michael does work at digital
[3638.66 --> 3642.36]  ocean and digital ocean did sponsor the show but digital ocean has been sponsoring the show
[3642.36 --> 3648.38]  uh for a very very long time and uh we love digital ocean so we're hosted on digital ocean we think
[3648.38 --> 3654.84]  you should be hosted on digital ocean uh and if you're not that's just uh that's just a sad state of
[3654.84 --> 3660.30]  affairs there jared one thing i thought we need to keep mentioning uh at the tail of the show is to
[3660.30 --> 3666.84]  remind our listeners that we are listening as well uh go to github.com slash the change log slash ping that is
[3666.84 --> 3672.50]  our open repo i've been calling it our open inbox and you know maybe jared since you've been kind of
[3672.50 --> 3676.80]  triaging that quite a bit maybe you can mention quickly you know how we're using that and some of the
[3676.80 --> 3682.40]  things we're hearing back from the community yeah absolutely um whether it's a project that you love
[3682.40 --> 3687.98]  or a project that you just released and you want to have some coverage too uh an idea for a future show
[3687.98 --> 3693.76]  um a complaint you know you think i talk too much i don't know whatever you got to say to us
[3693.76 --> 3699.96]  uh come say it at ping we're watching that repo we're conversing there and we've had a lot of
[3699.96 --> 3704.64]  interesting projects come through and great show ideas and a lot of those are turning into
[3704.64 --> 3710.36]  real shows so it's been pretty awesome we've been leveraging issues not just there but michael that's
[3710.36 --> 3716.38]  how you got on here we went to the io js uh repo and just dropped the uh an issue in there and said
[3716.38 --> 3720.90]  hey can you guys come on the show and uh that's how this happened that was pretty awesome jared was
[3720.90 --> 3724.66]  like that's that's a neat way to get a hold of people yeah that's how we do pretty much everything
[3724.66 --> 3730.42]  yeah so it worked out so that was good stuff well everybody thanks for listening we'll be back next
[3730.42 --> 3735.30]  week enjoy this i hope you enjoyed this show if you have any questions about some links you mentioned
[3735.30 --> 3742.48]  the show notes are there that's changelog.com slash 139 episode 139 thanks michael thanks jerry let's all
[3742.48 --> 3743.98]  say goodbye bye guys
[3754.66 --> 3758.56]  bye
[3758.56 --> 3770.60]  bye
[3770.60 --> 3771.78]  so
[3771.78 --> 3772.28]  you
[3772.28 --> 3773.30]  yeah
[3773.30 --> 3773.48]  you
[3773.48 --> 3773.54]  you
[3773.54 --> 3773.94]  you
[3773.94 --> 3774.44]  you
[3774.44 --> 3775.68]  you
[3775.68 --> 3775.80]  you
[3775.80 --> 3780.40]  you
