[0.00 --> 12.64]  welcome back everyone this is the change log and i'm your host
[12.64 --> 18.16]  adams dakowiak this is episode 129 jared and i talked to sarah goldman about her
[18.16 --> 25.02]  awesome work at facebook and making php fast awesome and specced this entire conversation
[25.02 --> 30.64]  is about getting the php spec out there facebook leading the way but more importantly sarah
[30.64 --> 36.94]  leading the way on that front this show is significantly delayed sarah you're awesome
[36.94 --> 44.22]  i'm really sorry please accept my apology this show is sponsored by digital ocean code ship and
[44.22 --> 50.04]  top tile we'll tell you a bit more about code ship and top tile later in the show but our friends at
[50.04 --> 56.38]  digital ocean simple cloud hosting built for developers in 55 seconds you can have a cloud
[56.38 --> 62.72]  server with full root access and it just doesn't get any easier than that pricing plans started only
[62.72 --> 69.66]  five bucks a month for half a gig of ram 20 gigs of ssd drive space one cpu and one terabyte of
[69.66 --> 75.88]  transfer they got locations all over the world new york san francisco amsterdam singapore and now their
[75.88 --> 81.72]  newest location london and you can easily migrate your data in between any of those regions making
[81.72 --> 87.98]  sure that your data is always closest to your users use the promo code changelog november in all
[87.98 --> 94.56]  lowercase again changelog november all lowercase very important to get a ten dollar hosting credit
[94.56 --> 99.56]  when you sign up head to digital ocean.com right now to get started and now on to the show
[99.56 --> 106.92]  we're joined today by sarah goldman she is man sarah i'm so impressed with what you're doing you work
[106.92 --> 112.58]  at facebook so that's kind of a big deal but not only do you work there but you also make facebook
[112.58 --> 118.38]  fast which i think that that's been like the mantra of facebook to be fast since the beginning so
[118.38 --> 126.18]  today we're joined by my managing editor jared santo and also sarah goldman from facebook to talk about
[126.18 --> 132.14]  some cool stuff happening in the php world specifically the php spec that's brand new so
[132.14 --> 139.62]  sarah welcome to the show thanks for having me so i guess the best way to start navigating this
[139.62 --> 146.28]  conversation might be to tee up the post that you shared on the php mailing list which was sort of
[146.28 --> 152.02]  the announcement it was kind of at oscon and um and i'm not sure if it's oscon or oscon i kind of
[152.02 --> 156.42]  wasn't sure i've never been there so i've never heard anybody actually say it until just now so
[156.42 --> 161.74]  is it oscon or is it oscon you know i always say oscon but that doesn't mean that i'm right
[161.74 --> 168.02]  what do you think jared i'm gonna go with oscon so i think oscon too okay so i wish i didn't say
[168.02 --> 171.80]  that at all then now because i feel like an idiot for thinking it's oscon why would it be os now that
[171.80 --> 176.54]  you actually say it out loud it does seem like it should be os it's open source con so that would
[176.54 --> 181.64]  yeah i don't know gotta just that's what i was thinking who says i should write some os software
[181.64 --> 190.18]  yeah right good point that's true this is a heated debate so this post was on tuesday july 22nd which
[190.18 --> 194.38]  wasn't too long ago but long enough ago that's a lot of stuff's happening between now and then so
[194.38 --> 200.10]  help us uh and jared i don't want to speak for you but i know that i'm pretty much a php novice like i've
[200.10 --> 206.24]  done some stuff with wordpress i've never written anything uh any of any extent that sarah's been to so
[206.24 --> 211.12]  i'm totally a novice in the room just asking questions so um i would consider myself an
[211.12 --> 217.90]  intermediate so intermediate yeah okay not a pro but i have some experience so hold our hands along
[217.90 --> 223.54]  the way yes please do please do but tee this up what what what happened what is what does this mean
[223.54 --> 230.58]  for the php community well i mean so php has been around for like 18 years now and just sort of
[230.58 --> 236.68]  grasp that in your mind for a second um and in that 18 years it's gone completely as an organic
[236.68 --> 242.48]  growth right it's sort of rasmus wanted something to display his resume better so he put together some
[242.48 --> 250.20]  scripts and to do that and then that kind of turned into a more of a compiled program to turn some html
[250.20 --> 255.02]  with a few little bits of code and into something real and it's all been organic ever since then even
[255.02 --> 261.86]  when andy and zev got involved to uh build php3 with more like real engine like you would find in
[261.86 --> 268.52]  a any kind of sensible language it was still organic because they were just trying to scratch their itch
[268.52 --> 273.94]  um and it's been a whole bunch of it scratching and what you wind up with is what got popularly
[273.94 --> 279.78]  described as a fractal of bad design um and you know a lot of us kind of take that tongue in cheek
[279.78 --> 283.68]  because well all right it might be a fractal of bad design but it runs most of the internet so
[283.68 --> 290.48]  whatever yeah um but it's done all this without really having a clear picture of itself it doesn't
[290.48 --> 299.36]  know um how do you define what is proper php all of the uh the the really serious languages like c c
[299.36 --> 305.42]  plus plus they have these massive documents that describe um what syntax should look like what's
[305.42 --> 309.94]  valid grammar that sort of thing and we've been talking about it i'm i'm sorry i'm going to say we
[309.94 --> 313.54]  and us in a lot of different contexts today i'm going to try and keep track of which context that
[313.54 --> 319.90]  is um we the php community um have been talking for a lot of years about how we kind of need to
[319.90 --> 327.00]  formalize what the language is you know we need to say all right these are the behaviors you should
[327.00 --> 334.26]  expect from the parser and and what uh a script a well-written script actually looks like as opposed
[334.26 --> 339.18]  to having two different ways of doing if statements that look completely different or whatever it happens
[339.18 --> 344.72]  to be um so it's always been like yeah we should do that we should do that we should do that but who
[344.72 --> 349.14]  wants to write documentation right none of the programmers i don't want to write documentation
[349.14 --> 356.68]  so fast forward years and years and years facebook's got this hhvm thing that we've built for
[356.68 --> 362.46]  uh running face learning facebook code very fast and hopefully other people's php code very fast
[362.46 --> 369.54]  um and we're thinking well what can we do to give back really because like facebook was built on php it
[369.54 --> 375.08]  was built on the public version of php you know zuck sitting in his dorm room putting together the first
[375.08 --> 382.72]  facebook.net or whatever um was just running regular php um funnily enough probably some code that i wrote in
[382.72 --> 390.64]  there um that's kind of cool yeah no he's my boss go figure um so what can we do to to give back and show
[390.64 --> 396.48]  that we're serious about taking the php language seriously you know we want php to be seen as a
[396.48 --> 403.30]  better language instead of the fractal of bad design so we said well here's something that not
[403.30 --> 408.44]  only has the community sort of been asking for this and hoping that they can put together a spec properly
[408.44 --> 414.84]  but this will actually help hhvm at the same time because we want to be able to write a parser that is
[414.84 --> 421.20]  fully compliant with php but how do we do that if we don't know what php is apart from looking at the
[421.20 --> 427.04]  source code so it's not a completely selfless gesture either so let's so we pause there for just a second
[427.04 --> 434.68]  maybe um for those listening and kind of catching up um real quick mention what is hhvm oh of course
[434.68 --> 442.00]  i'm sorry um hhvm stands for hip-hop virtual machine um it's the basically third generation of
[442.00 --> 450.76]  a compiler that facebook's been working on to uh to run php code it's um ostensibly uh php syntax
[450.76 --> 458.50]  compatible um the the problem we ran into about five years ago or so at this point is that um php's
[458.50 --> 465.50]  code base is massive and we have a couple of users so we need to be able to run that php as fast as
[465.50 --> 473.60]  possible uh changing to another language is possible but it is obviously a large task we have
[473.60 --> 480.08]  something like 10 to the seventh lines of code um that's not a small project very big wow uh yeah
[480.08 --> 484.18]  very big i remember reading about your choice of mercurial versus get to and it was you know the
[484.18 --> 489.54]  choice between those two version controls was also based on how larger larger code base was and how many
[489.54 --> 496.80]  developers have committing to it on a daily basis too yeah no so our our main code base of php um i
[496.80 --> 501.46]  don't touch it often i'm mostly touching c plus plus code but sometimes i go ahead and touch the the php
[501.46 --> 508.22]  repo and if i'm doing the checkout on git because we we're still supporting both modes at the moment
[508.22 --> 516.76]  um i can say git pull and then i'll walk away you know go down have lunch uh check myself in the
[516.76 --> 522.28]  america all the time right come back but a long time is the point yeah um i do it on mercurial and
[522.28 --> 530.48]  i just say hg update and done and now it's done it is blazingly faster we might need to earmark that
[530.48 --> 535.50]  topic just just for the listeners sake because i know we covered that on the changelog um i know it's
[535.50 --> 540.08]  a big deal anytime facebook makes choices and it sort of provides this rift for others to follow in the
[540.08 --> 545.38]  community because because of your sheer size and also because of your engineering team and the talent you
[545.38 --> 550.64]  have you know you obviously tend to have a pretty good opinion any pretty definitive opinion that
[550.64 --> 556.90]  sort of provides this divide to the community and we covered uh just quickly your your um your choice
[556.90 --> 561.40]  of mercurial over git and i thought it was just enlightening the reasons why you chose it
[561.40 --> 566.58]  yeah and there's more reasons than just speed um and i'm not going to go into all those because
[566.58 --> 571.84]  that's actually not my area of expertise and i'll probably get some things wrong um i do just want
[571.84 --> 576.54]  to say that i have a lot of love for git i don't want to poop on git about saying it's slower than
[576.54 --> 582.50]  mercurial in all cases it's it was a decision that facebook made because our code base particularly
[582.50 --> 590.08]  needed um uh speed to get developer efficiency up um and that's developer efficiency is one of our
[590.08 --> 597.02]  watch words when it comes to what we want to focus on um focus on 10 to the 7th lines of code that is
[597.02 --> 602.50]  just astounding yeah yeah you know you have a lot you know you have a large app when you consider
[602.50 --> 607.58]  you know reworking the underpinnings less work than actually you're rewriting in a separate language
[607.58 --> 612.18]  well really i mean that that's what it comes down to it's like what's what's going to be easier
[612.18 --> 617.76]  rewriting in another language or making the language better right can you give us maybe a snapshot too of
[617.76 --> 624.66]  the importance of hhvm to facebook because i remember reading uh um and help me piece this together
[624.66 --> 629.86]  this is totally up um you know off the cuff here but i remember reading a blog post about and i can't
[629.86 --> 633.70]  remember the names of who's involved so you could probably even name them if you'd like to but it was
[633.70 --> 637.64]  basically like down to the wire of getting this done or you'd have to like do something massive to
[637.64 --> 643.20]  get this just-in-time virtual machine in place to kind of read php code and from what i can understand
[643.20 --> 648.96]  basically decompile that down to binary or something other way some other way of doing it was like this
[648.96 --> 653.54]  big deal and it was like down to the minute and a five-year-long project and finally you had cracked it
[653.54 --> 660.08]  can you kind of give a snapshot of that of that moment um that might be slightly dramatic dramatized
[660.08 --> 665.80]  for internet effect i'm not sure okay because it seemed dramatic to me i i will certainly say that
[665.80 --> 671.04]  you know when we when we started building the hip-hop project um which initially by the way was not a
[671.04 --> 677.88]  virtual machine or or a just-in-time compiler it was actually a a php to c++ transpiler um when we
[677.88 --> 684.00]  first got that project going we actually were sort of hitting the limits of how much blood we could
[684.00 --> 690.10]  squeeze out of the php turnip for our code base and the number of users we had um we literally could
[690.10 --> 696.18]  not buy hardware fast enough to be able to serve up every user that wanted to hit the site um so
[696.18 --> 702.68]  in in that sense it was probably a bit of a crunch time it was it was a bit of um god what are we going
[702.68 --> 709.62]  to do do we need to train everybody to write c++ code and get this thing uh running at at real speeds
[709.62 --> 715.36]  are we going to pick up i don't know compiled python or something like that i don't know um
[715.36 --> 721.18]  consider the undertaking when you have that many engineers working on that much code
[721.18 --> 730.26]  um how long is that going to take um turned out the uh the process of transpiling php to p to c++ code
[730.26 --> 736.94]  at the very base of it wasn't all that difficult um i don't want to take it away from him from uh
[736.94 --> 744.50]  high ping who wrote the first version of of hip-hop but um the the basic of of just doing that bits of
[744.50 --> 750.72]  transpiling uh got us a huge performance win i think it was like an 80 win right off the bat and it came
[750.72 --> 757.02]  to like a two and a half times win within like a year or something like that um that's a huge gain
[757.02 --> 763.38]  when you can run um two and a half times fewer servers right absolutely um and that just gives
[763.38 --> 772.88]  you that breathing room to say oh thank god oh you know um that ultimately uh led to the vm project
[772.88 --> 777.52]  because we looked at this transpiler option and we said well this has got a bunch of problems with it
[777.52 --> 782.88]  number one our developer environment now looks nothing like a production environment and it can't
[782.88 --> 787.42]  because you can you imagine as a developer if you make one tiny change to a little php file
[787.42 --> 794.24]  you then have to recompile all of these millions of lines of code just to see what difference comes
[794.24 --> 799.48]  out on your web page you would run screaming from that yes what what was the compile time do you
[799.48 --> 810.66]  recall like um so uh i i yeah i can say that number sorry i was trying to decide if i could say that
[810.66 --> 817.80]  number um at the time that we switched off of the transpiler onto the vm um i want to say it took
[817.80 --> 823.86]  about 20 minutes to build the entire site but that's not on a single machine that's actually on a fleet of
[823.86 --> 828.68]  machines because we're using just cc to do this wow i think if you tried to do this on a single machine
[828.68 --> 835.42]  um it would be like you know a day's process or something like that it was definitely not something
[835.42 --> 841.62]  that developers could do so developers uh for a while wound up doing just regular php because it's
[841.62 --> 847.88]  close enough but then we started adding functionality to the language like generators for example we've had
[847.88 --> 856.72]  for years and php just got them uh in version 5.5 so uh we had these sort of hacks in place like hphpi
[856.72 --> 861.18]  which was uh slower than regular php but it worked for development purposes
[861.18 --> 866.70]  and and things like that and it was it was just kind of messy it led to some weird inconsistencies
[866.70 --> 875.36]  between dev and production excuse me um so that led off the the vm project um and we we had a bunch
[875.36 --> 881.76]  of guys who who came from microsoft uh at that time uh they've worked on the clr um so they've built
[881.76 --> 888.02]  you know just in time compilers before recently in fact um so they brought a lot of that uh information
[888.02 --> 895.18]  to bear and that um i think i think that kicked off somewhere around like 09 something like that
[895.18 --> 901.36]  slightly before we actually released hip-hop to the world in 2010 um but it didn't really
[901.36 --> 911.12]  hit the point of running production code until uh january of 2013 so it took a while to get that one right
[911.12 --> 918.40]  if i can maybe do a call back to our last show too jared um i want to make a note i guess to kind
[918.40 --> 922.92]  of i guess go from where we are to talking about the php spec and what it's actually written and it's
[922.92 --> 929.14]  kind of a an aside but a throwback to our most recent show which was uh just released today episode
[929.14 --> 936.20]  127 talking about uh keeping a change log or the project keep a change log from olive oil account uh which
[936.20 --> 941.84]  i could not say correctly on the show but uh yeah it's just whatever that's i can't get over it
[941.84 --> 946.52]  anyways um what you say though sarah is that the first thing you'll notice is that it's written in
[946.52 --> 953.32]  markdown um and that there's this slight lean towards um something called restructured text and
[953.32 --> 957.92]  it's something that i have an interface with can you kind of talk a bit about you know your choice
[957.92 --> 966.04]  of what to write the spec in well the original spec was actually written in ms word um we the the
[966.04 --> 972.00]  contractor that we hired to work on the spec um he's got like a lot of spec chops um he's worked on
[972.00 --> 978.72]  the c spec before um zim's rex and i'm gonna butcher his last name jash j-a-s-c-h-e something like
[978.72 --> 983.84]  that that's hard to say i can't pronounce last names either um he's worked on on specs before but his tool
[983.84 --> 991.00]  of choice is ms word so god bless him let him do what he needs to do um we're not gonna put that into
[991.00 --> 996.12]  any kind of open source uh collaborative uh editing system because that just doesn't work for that
[996.12 --> 1001.72]  um so we had to pick something um we look at github we say oh okay markdown is natively supported
[1001.72 --> 1007.68]  like by github it seems like it's probably expressive enough for what we need to do so let's just use that
[1007.68 --> 1013.62]  as a starting point and we can switch off after that um when i made the original announcement at
[1013.62 --> 1020.34]  ofcon and released that sort of pdf of the sample chapter uh i asked for people's opinions you know
[1020.34 --> 1026.66]  what makes sense to you guys you know what formats do we want to be uh editing it in um and
[1026.66 --> 1033.90]  in those responses from the php mailing list not from internally at facebook um there were
[1033.90 --> 1038.94]  there were of course some bike shedding about oh maybe we should go this direction well this one
[1038.94 --> 1044.72]  has this advantage that one has that advantage maybe ascii docs the right way to go um as to as
[1044.72 --> 1047.82]  is pretty typical with with those kind of forms you know there were a lot of answers
[1047.82 --> 1051.90]  slightly towards restructured text from what i could see but nothing really definitive
[1051.90 --> 1058.08]  um at the end of the day um the guy who was actually doing the transformation from
[1058.08 --> 1062.78]  uh word doc to something sensible joel marcy who i was hoping was going to be on this podcast
[1062.78 --> 1069.36]  but he didn't make it bummer joel you couldn't make it man i miss you where are you joel um at at the
[1069.36 --> 1073.28]  end of the day he had already started migrate uh migrating things into word doc and they were looking
[1073.28 --> 1079.58]  great so i just said you know what finish the word doc and we will fix that later there's always
[1079.58 --> 1086.66]  time for pull requests um and sure enough um one of the first big uh commits that was done by somebody
[1086.66 --> 1092.56]  outside of facebook was to take this big monolithic markdown file and split it up into chapters which
[1092.56 --> 1096.58]  was something i was initially asking joel for and he's like i got so much going on i can't even think
[1096.58 --> 1103.76]  about that much so it's great to see the php community have been so well receptive of this
[1103.76 --> 1109.02]  like like i was i was worried that there was going to be some sort of like oh facebook's trying to take
[1109.02 --> 1114.58]  over the language by imposing the spec on us right but it's it's really just been sort of like oh gosh
[1114.58 --> 1121.48]  thanks guys we we were looking for this where'd you find it um so how long has this project been in
[1121.48 --> 1126.06]  the making is it i mean i know 20 years the language the kind of story we've kind of painted here but
[1126.06 --> 1131.78]  you know how long has it been on your particular mind to sort of start lifting this up and actually
[1131.78 --> 1137.18]  making it happen even from your perspective or facebook's um i want to say that we made the
[1137.18 --> 1142.32]  decision that we were going to write a spec and publish one somewhere around last february um i think
[1142.32 --> 1147.14]  we actually started like properly working on it you know sorting out rex's contract things like that
[1147.14 --> 1153.24]  um i want to say we properly started working on it around march or possibly april i can't say for sure
[1153.24 --> 1160.66]  um so just this year not very long so it seems like specs are far more important when you have
[1160.66 --> 1165.00]  many implementations you know you look at something like javascript you know you have all these browser
[1165.00 --> 1173.08]  implementers um and they all need a spec to conform to was it is hhvm the second major php implementation
[1173.08 --> 1180.10]  um or are there is there a more diverse ecosystems i'm not aware of um it depends on what you mean by
[1180.10 --> 1186.68]  um i consider it the second major um but a lot of people who have worked on other implementations
[1186.68 --> 1194.74]  would certainly disagree with me um there's uh implementations like phalinger uh phc um what's
[1194.74 --> 1200.12]  the other one i'm thinking of hippie vm uh which was released very recently and uh has spent a lot of
[1200.12 --> 1207.12]  time comparing themselves to us so i'm not going to say they they picked their name as a as a bit of a
[1207.12 --> 1213.80]  gesture but maybe um so there's there's a number of php implementations out there i haven't seen
[1213.80 --> 1218.52]  a lot of chatter about many of them oh roads and i forgot to mention them they're another
[1218.52 --> 1225.50]  implementation but i'm pretty sure they're gone um so having having a spec is definitely important
[1225.50 --> 1231.86]  to bringing all of these different implementations together um but i think i think that's not the only
[1231.86 --> 1238.04]  benefit that we get out of it because um if you look actually at php itself um it goes through these
[1238.04 --> 1244.34]  you know version cycles four to five was a big jump um five to seven now is going to be a big jump by
[1244.34 --> 1251.84]  the way we're skipping six um why uh there's history behind six um i don't think you want me to get in
[1251.84 --> 1257.34]  there is that very much like fertile six yeah this is like you know certain hotels they they don't have
[1257.34 --> 1262.22]  a 13th floor you know you go from the 12th straight to the 14th but come on those people
[1262.22 --> 1267.22]  on the 14th know what floor they're really on that's right oh that's a that's a laugh that's a
[1267.22 --> 1272.74]  mitch head for joke but you laugh but in the discussion about what version to call it seven was actually
[1272.74 --> 1279.48]  highlighted as a lucky number oh is it yeah uh humans and our numbers uh no we were going to
[1279.48 --> 1285.60]  make unicode into the language for php6 um like four years ago or something like that and the project
[1285.60 --> 1290.18]  got really far along to the point that even books were published about it um those of us who worked
[1290.18 --> 1296.28]  on the unicode implementation felt sort of a you know a connection to that um and then the project
[1296.28 --> 1303.24]  kind of died because of a number of reasons and so there was never a six um so a discussion came up
[1303.24 --> 1308.84]  about what if it picks six or seven i don't want to belabor it bottom line we pick seven um
[1308.84 --> 1313.98]  gosh what was i talking about before we went off on a tangent spec and the next version kind of
[1313.98 --> 1323.38]  uh oh yes so yeah so the usefulness yes uh the usefulness of the spec is um partially to give
[1323.38 --> 1328.26]  the php project something to make sure that you know we don't break things accidentally along the
[1328.26 --> 1333.58]  way and we have broken things accidentally on a number of occasions um remind me to explain to you
[1333.58 --> 1342.78]  why zero x zero plus two equals four sometimes um it's also important for some of the uh revisions
[1342.78 --> 1348.88]  we're making to the language right now um there are two uh rfcs up on the php list one for unif some
[1348.88 --> 1355.34]  what's called uniform variable syntax um this is to make it sort of consistent when you say something
[1355.34 --> 1362.60]  like uh dollar a square brackets some subscript uh parentheses some function call arrow some method
[1362.60 --> 1367.30]  call whatever you happen to do piling these things together what's the right evaluation order
[1367.30 --> 1372.98]  left to right right to left um middle outwards which is actually um sort of like what it currently
[1372.98 --> 1379.94]  does and makes no sense um unifying that and making it make sense um another guy nikita popov um who's
[1379.94 --> 1386.90]  been really um uh a big contributor in the php circles in the past few years um he's working on an abstract
[1386.90 --> 1394.10]  abstract syntax tree for php which is also another huge thing um php's compiler doesn't have an ast it
[1394.10 --> 1399.98]  says here here are my parse uh uh expressions coming through let's just compile those straight
[1399.98 --> 1406.02]  to byte code and don't look at the overall program at all um so he's introducing an ast which is
[1406.02 --> 1411.92]  obviously a big opportunity to screw up the language um having again a conformance suite and a spec
[1411.92 --> 1413.76]  helps to make sure that that doesn't happen
[1413.76 --> 1420.12]  all right let's pause the show for just a minute give a shout out to our sponsor code ship
[1420.12 --> 1425.48]  code ship is a hosted continuous deployment service that just works we've been working with
[1425.48 --> 1430.44]  code ship for quite a while now we really really enjoy not only the product they built but the
[1430.44 --> 1436.14]  people behind it you can easily set up continuous integration for your app today in just a few steps
[1436.14 --> 1441.54]  and code ship has great support for lots of languages all the test frameworks as well as
[1441.54 --> 1447.28]  notification services they easily integrate with everything you can think of github bitbucket you can
[1447.28 --> 1454.96]  deploy to cloud services like heroku aws nojitsu google app engine or even your own service because
[1454.96 --> 1459.84]  that's the way you want to do it sometimes too uh setup only takes three minutes it's it's so quick
[1459.84 --> 1464.14]  it really is just so quick get started today with their free plan and make sure you use the code
[1464.14 --> 1470.20]  the changelog podcast that's really important use the changelog podcast and when you do that you can
[1470.20 --> 1477.08]  get 20 off for three months on any plan you choose head to code ship.io and tell them the
[1477.08 --> 1484.98]  changelog sent you well let's let's talk about this you know this uh backlash that didn't happen
[1484.98 --> 1489.62]  you know that what you maybe perhaps feared is that the community would say okay this is facebook
[1489.62 --> 1495.06]  trying to you know grab a stranglehold around php the language by introducing the spec
[1495.06 --> 1500.16]  can you and i don't necessarily believe that but could you still speak to those fears perhaps
[1500.16 --> 1505.04]  um maybe from facebook's perspective and then maybe you know you you like you said we have all
[1505.04 --> 1508.68]  these different we's you know you represent facebook a little bit and then you also represent
[1508.68 --> 1515.06]  just the php community and how you balance those two as well would be interesting um well yeah i
[1515.06 --> 1518.28]  mean i'll start i'll speak to the second part of that first because i've actually been working
[1518.28 --> 1524.94]  on php for about the past dozen years or so um so i've got a lot of skin in the game in terms of
[1524.94 --> 1531.30]  code contributed to uh the php source code and and involvement with the community of i i wrote
[1531.30 --> 1537.22]  pretty much the book on writing extensions for php um but at the same time i'm also working here for
[1537.22 --> 1544.86]  for a for facebook on hhvm largely because of that php work um i wrote i'm doing things like writing the
[1544.86 --> 1550.92]  actual extension api itself on the hhvm side so i have interests on both sides of the fence and
[1550.92 --> 1558.40]  um when i come to the list you know it's it's on the one hand it's coming with the uh history of
[1558.40 --> 1564.08]  of like having time and skin in the game with php but it's also coming in with this yeah but she's
[1564.08 --> 1571.30]  working on that other php thing and um how how much of what she's requesting in this rfc or whatever
[1571.30 --> 1578.70]  is to improve hhvm so it can take over the world um i i don't think i have to tell you that there
[1578.70 --> 1584.80]  there is um there is some degree of sort of distrust about facebook and facebook's intentions
[1584.80 --> 1591.24]  um i mean do any google search and you'll get funny of those conspiracy theories um and some
[1591.24 --> 1596.24]  of those come through because we're all people and we you know we we want to protect what we see is
[1596.24 --> 1603.44]  good and you know php's open source uh philosophy i think is actually really good it's a really open
[1603.44 --> 1610.38]  project it's got no bdfl it's got nobody saying no this is how the project must go forward and that's
[1610.38 --> 1615.40]  why there's been no forks because what goes into the language is what the people who are actively
[1615.40 --> 1621.86]  working on it at the time say is right for the language um so when you've got something like um
[1621.86 --> 1628.50]  facebook suddenly making this big push on its open source uh on its uh implementation of php
[1628.50 --> 1633.68]  saying oh we're we're making this really open source now we're making this really uh friendly to
[1633.68 --> 1643.38]  to developers out there um and uh hey here's a spec for it you can look at that as uh gosh php's
[1643.38 --> 1652.20]  seeing a resurgence or you can look at it as hmm embrace extend and extinguish right um so so i i have
[1652.20 --> 1659.12]  personally gotten some of that that kickback on other um uh posts that i've put on the the mailing list
[1659.12 --> 1665.12]  but that did not happen at all here i think everybody sort of saw the way we released this
[1665.12 --> 1671.50]  um and the way that we you know tried to make sure that we focused on php as the source of truth and
[1671.50 --> 1680.50]  said how can i fault this you know it's it's this is just a thing that now belongs to the php community
[1680.50 --> 1686.76]  like um we with facebook hat on didn't maintain any control over this we said here it is public domain
[1686.76 --> 1693.22]  license cc0 we're putting it into php's git repository so they completely control the documents
[1693.22 --> 1699.52]  um it's it's completely out of facebook's hands at this point maybe that's where we can dig in just
[1699.52 --> 1704.22]  a quick bit because i know we talk about licensing on the show here and there but maybe to catch up
[1704.22 --> 1710.84]  why you chose cc0 it's it's in quotes no rights reserved can you talk about maybe the choice of that
[1710.84 --> 1715.74]  license versus say gpl or some other license you may have chose for other uh open source that facebook
[1715.74 --> 1722.26]  has out there um well i can only speak to it so much because i didn't specifically pick the cc0 license
[1722.26 --> 1727.50]  um my personal favorite um for my projects is bsc license because i just like the little bits of
[1727.50 --> 1735.08]  attribution um but like it comes down to to what your your philosophy about this sort of information
[1735.08 --> 1738.68]  is like we're just talking about a document at the end of the day we're not even talking about software
[1738.68 --> 1747.46]  right um you know what is going to be most useful to a project like php and like i said php is a
[1747.46 --> 1753.42]  really open project and for something like php it makes sense to just say you know what here's some
[1753.42 --> 1759.64]  information for the world um what what do we have to gain by putting a more restrictive license on it
[1759.64 --> 1769.28]  very little um you mentioned gpl um i could i could see the advantage of wanting to say that if
[1769.28 --> 1775.44]  somebody else grabs this and you know adds to it and and extends it you know we would want to make
[1775.44 --> 1781.76]  sure that that's open and visible to everyone um i personally don't like the gpl license um
[1781.76 --> 1787.64]  well i'm not holding you to the fence you're trying to figure out why you chose this place i
[1787.64 --> 1793.74]  just wanted to kind of get a snapshot because mostly from the the vantage point of uh it will
[1793.74 --> 1798.96]  right when somebody does something in the world you you want to um you know depending upon the person
[1798.96 --> 1805.68]  obviously you want to say that person has goodwill for me so or that entity or that organization or
[1805.68 --> 1809.72]  you know so your reputation does precede you in a way that you've done a lot for open source
[1809.72 --> 1814.54]  and i just want to make sure that you have a chance here clearly to to say we chose this license for
[1814.54 --> 1819.30]  this reason for the reasons it's open it's you know it's not ours it's the communities and that
[1819.30 --> 1825.62]  kind of thing so i i didn't want to uh dang all that too far but get the point across yeah i mean the
[1825.62 --> 1830.98]  only thing i could say about that is just like that's the beautiful thing about cc0 it's literally no
[1830.98 --> 1837.60]  strings attached you know yeah and it's just it's a simple license it's about three lines you don't need uh
[1837.60 --> 1842.92]  you don't need a lot of greed to understand a license like that so maybe this is just a
[1842.92 --> 1850.46]  a left-wing question but it seems kind of an obvious one to to me but you know it's just a
[1850.46 --> 1857.46]  document you just said that um it's not like it's code it's not like it's changing php really but what
[1857.46 --> 1865.36]  does this spec what does having it written out um fleshed out open source uh cco uh cc0 license
[1865.36 --> 1872.86]  attached to it what does that do what how does this how do you expect or desire for the community to
[1872.86 --> 1879.74]  change because of this document now being there to specify how php should be it's interesting you
[1879.74 --> 1884.24]  weren't used the phrase it's not changing the language because as it turns out it actually is okay
[1884.24 --> 1890.78]  um one of the first payoffs that we've seen from this is um as you know people are looking through
[1890.78 --> 1895.30]  the document a lot of pull requests coming through for simple things like grammar fixes and things
[1895.30 --> 1900.22]  like that whatever um a few bugs have come up uh one of them that i just worked on the other day
[1900.22 --> 1906.84]  uh noted that the spec says switch statements may only have one default block which i mean i think we
[1906.84 --> 1914.06]  can all agree makes sense um and this user hadn't had noticed at some point in his code that he
[1914.06 --> 1918.40]  wrote a switch statement with two default blocks and it caused a weird bug for him because he
[1918.40 --> 1924.02]  doesn't understand why that first default block wasn't getting executed um and so he filed a bug
[1924.02 --> 1928.34]  report he said this doesn't match php allows multiple default statements and when you have
[1928.34 --> 1931.80]  multiple it'll execute the last one which i think we can all agree is a bit clowny
[1931.80 --> 1938.44]  um so what should we do with that should we fix the spec to say multiple are allowed because that's
[1938.44 --> 1944.96]  what php does well no we shouldn't actually because that's really silly code um and i put it exactly
[1944.96 --> 1952.00]  that way to the list i said this is this is silly behavior that php supports probably by accident let's
[1952.00 --> 1958.80]  fix the language so it matches the spec so that's what we're doing and and that's the benefit of having
[1958.80 --> 1963.48]  that spec you've got a lot of eyes looking at it this and you've got that lived experience of these
[1963.48 --> 1967.96]  developers out in the wild who are saying that doesn't jive with what i know
[1967.96 --> 1974.96]  so facebook has another uh language that they're very interested in their very own hack language
[1974.96 --> 1979.80]  which i think they announced was it this year i think it was 2014 it was a few months yeah i think
[1979.80 --> 1986.32]  it was in april yeah april ish we know hhbm compiles to hack and php um how does hack fit into
[1986.32 --> 1990.08]  this landscape with facebook obviously it's not going to affect the php spec or will it
[1990.08 --> 1997.76]  um so hack um we are writing a second spec actually um rex is already busy back at work
[1997.76 --> 2003.84]  writing a spec for the second word document open huh a second word document yes command or was that
[2003.84 --> 2010.28]  control new never mind uh when that's done um we're most likely going to publish that as well of course
[2010.28 --> 2015.54]  that will be under the the facebook namespace on on github or uh possibly the hhbm namespace i'm not sure
[2015.54 --> 2023.12]  um because it does make sense for us to own that document at least for now um hack is sort of it's
[2023.12 --> 2028.70]  you could describe it as its own language but i think if you know any php you can look at a hack
[2028.70 --> 2033.56]  document and immediately understand what it does because it's it's really more like php plus plus
[2033.56 --> 2039.36]  um which for those of you keeping track of php's rules uh if you have a string that you post
[2039.36 --> 2044.68]  uh increment that would turn out phq try and pronounce that in your head i'll leave that to you
[2044.68 --> 2054.76]  um so hack is uh as i said php plus plus uh it's a different open tag it drops a whole bunch of
[2054.76 --> 2060.96]  some of the clownier bits of php the things that we look at and we say why is that even in the language
[2060.96 --> 2065.56]  um and it can do so safely because obviously if you're writing hack code this is not something
[2065.56 --> 2071.44]  that was written in 1989 and still needs to function right sorry i meant 1999 89 is a bit too far back
[2071.44 --> 2078.76]  um it also adds a number of things that um we noticed sort of developing our own code base
[2078.76 --> 2082.94]  it would have been really nice to have and we're not really sure why php didn't add them
[2082.94 --> 2089.96]  um i know why but that's another story um things like uh scalar type hinting um php only allows type
[2089.96 --> 2094.06]  hinting for arrays and objects so we add type hinting for everything we even go beyond that
[2094.06 --> 2100.20]  parameterized type hinting um the sort of workhorse of php the array that can be a vector or a map or a
[2100.20 --> 2105.74]  set or whatever um we actually define these specifically as a vector a map a set a pair
[2105.74 --> 2112.26]  whatever else um so you can define more uh specialized structures that can behave more sensibly under the
[2112.26 --> 2117.86]  hood if i've got a vector event that should literally be in memory int int int int in in a nice
[2117.86 --> 2122.74]  type packed array um so there's there's a performance gain to be had there but there's
[2122.74 --> 2127.98]  also a readability gain to be had you don't have to look at you know dollar foo as an array and wonder
[2127.98 --> 2132.24]  what kind of array that is you can look at dollar foo as a vector event and know exactly what you're
[2132.24 --> 2137.74]  dealing with um that helps the static analysis type checker and it also helps you as a human
[2137.74 --> 2143.40]  understand what the code's doing um so i mentioned static analysis type checker that's sort of the
[2143.40 --> 2148.64]  workhorse of hack um this is a extra program that runs in the background on a developer workstation
[2148.64 --> 2155.62]  and it reads all of your code base constantly watches for updates on the file system and it looks
[2155.62 --> 2160.54]  at all of the code paths for data moving through your system so it says okay this is coming from
[2160.54 --> 2164.06]  dollar underscore request obviously it's a string because that's what comes from the user
[2164.06 --> 2170.72]  it's going into this function so this function apparently accepts strings does it accept other types
[2170.72 --> 2176.10]  elsewhere no okay we'll say this type this function accepts strings it's going from there into some
[2176.10 --> 2181.90]  function elsewhere and it goes down to other paths it gets concatenated whatever else if you've got any
[2181.90 --> 2186.84]  sort of type error in that system it's going to let you know that hey you should probably check this
[2186.84 --> 2193.46]  bit of code over here we've converted 98 or something percent like that of our code base of our you know
[2193.46 --> 2199.50]  10 to the 7th lines of code to using hack by running a program that automatically goes through and makes all
[2199.50 --> 2204.76]  those changes so now when somebody works on facebook code they see this code that's fully type annotated
[2204.76 --> 2212.72]  has all these parameterized expressions to let them know what's moving through and we have a lot fewer
[2212.72 --> 2218.08]  problems of people saying oh i would refactor my little helper class that surely nobody else is using
[2218.08 --> 2222.62]  and then finding out that the site breaks because somebody was passing the wrong kind of data and it
[2222.62 --> 2229.26]  happened to work before so you know there's an old saying a servant you know can't serve two masters
[2229.26 --> 2237.12]  it seems like php's it generated themselves a nice or php facebook has this new uh maybe not a master
[2237.12 --> 2243.90]  but maybe a new toy and you said that 98 of your code base is now over onto it um being a subset or a
[2243.90 --> 2251.10]  maybe a superset of php is a superset is that fair to say well it's it's both a sub and a superset yeah
[2251.10 --> 2257.28]  it's like a side set i gotcha it's it's in a venn diagram or something right right so just your
[2257.28 --> 2261.44]  personal opinion where do you see you know facebook's interest lied long term but at the same
[2261.44 --> 2268.26]  time your facebook is investing into an open source public domain php spec so it seems like they have
[2268.26 --> 2275.14]  interest in both things where do you see that moving into the future um so there's a there's a
[2275.14 --> 2280.12]  few pieces of that answer so um as you see you can't serve two masters and that's a very fair
[2280.12 --> 2285.74]  statement on it how much attention are we really paying to the regular php side of things well a
[2285.74 --> 2290.54]  language is more than just its syntax right it's also the whole runtime that comes behind it and php
[2290.54 --> 2296.20]  has a massive runtime library um those are completely shared in common so you know we're obviously taking
[2296.20 --> 2303.32]  good care of those uh in common the other half of that is um a lot of the extra features that go into
[2303.32 --> 2309.60]  hack are actually just development time features um they're not necessarily used in the runtime
[2309.60 --> 2316.22]  some pieces of them are but not all of them so what works for hack works equally well for php
[2316.22 --> 2321.08]  um we want to make sure that we still pass the conformance suite and we're still behaving the way
[2321.08 --> 2330.20]  php expects but we can we can work on hack without losing sight of php um modulo those those sort of
[2330.20 --> 2340.32]  missing things gotcha um you know we we kind of rely on external users to tell us when we're doing php
[2340.32 --> 2346.10]  wrong at this point because we are all hack um but we do have you know tens of thousands of tests that
[2346.10 --> 2351.50]  run on every single diff so hopefully we're finding most of those things ourselves and what was the
[2351.50 --> 2360.18]  other half of your question i've already paged out so did i forget about it oh i think it's i think
[2360.18 --> 2365.12]  the the kind of maybe the the leave behind on that one might be just that you've got kind of these
[2365.12 --> 2371.68]  two parallels you're running and to some it seems like maybe it's a competitor and to some um they
[2371.68 --> 2376.42]  can clearly see what you just described there which was this sort of parallel effort and it's sort of
[2376.42 --> 2382.70]  like sugar on top instead of like a competitor and the squashing well i mean hack is not meant to be
[2382.70 --> 2389.48]  a completely new language it's meant it's meant to be um something that can live alongside php and in fact
[2389.48 --> 2394.12]  in most cases it kind of has to uh one of the things hacks doesn't let you do is have any top
[2394.12 --> 2400.78]  level code well your entry point can't actually launch without top level code so there has to be
[2400.78 --> 2408.14]  a php file in there somewhere um and it's it's about giving the developer the opportunity to use
[2408.14 --> 2414.28]  as much or as little of that functionality as they want to and one other thing i think that's kind of
[2414.28 --> 2422.22]  neat about hack is just i think the the hacker hack culture that facebook has propped up and just how
[2422.22 --> 2430.48]  how um i guess how awesome it is i guess in a sense to say that you you get not only to do some
[2430.48 --> 2436.88]  really awesome stuff um for developers across the world worldwide um but you also get to come up with
[2436.88 --> 2441.68]  a language that's kind of named after your mantra which to me is just like completes the world you know
[2441.68 --> 2446.86]  yeah at the end of the day that's that's pretty much um so so the length the name of the language
[2446.86 --> 2453.28]  that's another story um it's a it's in a lot of our opinions like and even internally it's a horrible
[2453.28 --> 2459.22]  name for a language because how do you google that right yeah i was thinking well that's great now the
[2459.22 --> 2463.96]  NSA is watching me because i've talked about hacking something um they're already watching so
[2463.96 --> 2470.64]  well they're watching us certainly um oh god somebody's gonna read something into that no i
[2470.64 --> 2476.66]  did not mean anything by that tell us more i already started just kidding i just i just created that out
[2476.66 --> 2484.32]  anytime you and i think this natural addition of lang after whatever it is so foo lang hack lang
[2484.32 --> 2488.22]  php lang that makes sense you've got sas lang you know all these other different
[2488.22 --> 2493.30]  ruby langs so the the addition of lang kind of helps maybe keep the NSA at bay
[2493.30 --> 2498.72]  well i mean it certainly is the same same problem that go ran into how generic is the word go right
[2498.72 --> 2504.34]  right yeah it's a movie it's a drug it's a verb it's a game whoa there's a drug called go
[2504.34 --> 2508.40]  yeah i think i don't know i'm not on the kids these days
[2508.40 --> 2516.24]  if you're gonna read into that yes we're definitely catching echelon's attention at this point
[2516.24 --> 2520.82]  well sarah you know the the one other thing i wanted to mention and you kind of did it a little
[2520.82 --> 2525.16]  tiny bit and i think i have to give you a little bit of applause because you seem to be pretty humble
[2525.16 --> 2531.50]  about um maybe either the fact that we didn't allow you to give you yourself a proper intro in
[2531.50 --> 2535.50]  the front of the show but um i think it's awesome that you've written this really awesome book
[2535.50 --> 2541.06]  extending and embedding php uh you've been involved in the php community for a very long time so you
[2541.06 --> 2546.14]  you definitely have uh the battle scars to to prove you are where you are for a reason
[2546.14 --> 2552.10]  and obviously facebook saw something in you because they hired you to work on making it fast
[2552.10 --> 2558.24]  which is pretty much what everybody wants facebook to be right uh it's what everybody wants all their
[2558.24 --> 2565.42]  sites yes um yeah that's that's a true statement just as well um i think you you mentioned a couple
[2565.42 --> 2569.40]  tangential conversations we could probably have i'm not sure if you want to bring them out or
[2569.40 --> 2573.18]  maybe take a minute or two just to touch on a couple of them you're welcome to but
[2573.18 --> 2578.36]  um yeah i think you mentioned uniform variable syntax and a couple others so feel free to refer
[2578.36 --> 2584.02]  for a minute or so um i'm not sure how much more i can say about uniform variable syntax as an example
[2584.02 --> 2590.66]  because i mean that that's just sort of um it was an rfc put forward as a guys we're doing this
[2590.66 --> 2596.52]  kind of clowny how can we fix this without breaking all the code out there um which is really what the
[2596.52 --> 2602.22]  the consternation on that particular subject has come down to you know um people are expecting
[2602.22 --> 2606.44]  their expressions to work a certain way because they've always worked a certain way they maybe
[2606.44 --> 2611.32]  even be muttering about it and saying why do i have to put extra parentheses or why do i have to
[2611.32 --> 2618.46]  do weird things for this language that doesn't understand order of precedence um at the same time that
[2618.46 --> 2624.18]  could exist and if we just like introduce that in like 5.7 or something like that there would be
[2624.18 --> 2629.66]  uproar because stuff would break um not my stuff i put ridiculous numbers of parentheses and braces
[2629.66 --> 2637.88]  everywhere um i've been told off for using too many parentheses in fact um but you know we there
[2637.88 --> 2643.80]  are there are warts on the language and everyone on the php internals list knows what those warts are
[2643.80 --> 2649.50]  because we get you know pelted with them on a regular basis php is a fractal of bad design it's a
[2649.50 --> 2655.30]  double claw hammer it's a silly language whatever it happens to be it tends to get a bad rap honestly i
[2655.30 --> 2661.72]  mean especially as uh i dare to say even like this but more modern ways or more modern things just
[2661.72 --> 2666.88]  meaning that they're newer a lot of things happening in the javascript space with node just with all
[2666.88 --> 2672.08]  sorts of other areas ruby is around 10 years i think it's just just turned 10 or just turned 15 or so
[2672.08 --> 2678.00]  now what rails is growing up and rails has turned 10 that's what it was um you know so like people kind
[2678.00 --> 2682.26]  of cling to these new things but there's been php for quite a while and it and it tends to kind of get
[2682.26 --> 2686.64]  this bad rap because it's been around for so long yeah and people almost look down upon it in some
[2686.64 --> 2689.92]  ways not that's why i really thought it would be important to have you on the show just to talk about
[2689.92 --> 2694.48]  the spec its importance and what you've been doing for the language and the community itself and then
[2694.48 --> 2700.44]  also kind of how that ties into facebook's approach to to making itself fast hhvm and everything
[2700.44 --> 2704.68]  else we've talked about so kind of neat there's a couple others do you want to mention abstract
[2704.68 --> 2711.36]  syntax tree or or the other two that you've mentioned that were uh side conversations um yeah i mean i i i i
[2711.36 --> 2716.54]  sort of touched on both of them already but um yeah the absent abstract syntax tree is something
[2716.54 --> 2723.24]  like i said nikita's working on um this like this never this used to never matter to me when i was
[2723.24 --> 2729.18]  working on uh regular php's engine um because i'd look at the compiler and i'd say well you know it
[2729.18 --> 2734.16]  gets the job done it probably makes it faster not to have this intermediate representation it's fine
[2734.16 --> 2740.14]  we can just compile an expression here's a ternary statement okay make emit the off codes for a ternary
[2740.14 --> 2744.60]  statement why do you need an extra abstract representation and then i started working on
[2744.60 --> 2751.12]  hhvm and i saw people who really understood how to write compilers and i saw the the way this abstract
[2751.12 --> 2758.30]  syntax tree got used in the process of compilation i'm like oh that's why that makes a lot of sense
[2758.30 --> 2764.70]  we can do a lot more optimization we can do we can do a lot fewer hacks to make these expressions work
[2764.70 --> 2771.78]  we can make things just function right without being inscrutable and i look back at the the the
[2771.78 --> 2777.90]  zen engine and i say you know there are some parts in here that are kind of kind of messed up um and and
[2777.90 --> 2782.28]  the ast is going to help us fix that it's not going to be anything visible to end users nobody's going
[2782.28 --> 2788.92]  to know what's gone in uh but it's going to make uh our life as as php engine developers a lot simpler
[2788.92 --> 2794.40]  all right let's pause the show for a minute give a shout out to a sponsor we've been working with
[2794.40 --> 2800.48]  top top for a very long time these guys are super awesome and i kind of wanted to take a moment and
[2800.48 --> 2805.24]  pause this for a bit and rather than just kind of give you an ad about what they're doing and what
[2805.24 --> 2810.04]  they're about i kind of wanted to tell you a personal story and part of that personal story is
[2810.04 --> 2815.12]  telling you a little bit about my day job so beyond just the change log and what we do here
[2815.12 --> 2824.12]  i have a full-time job at a non-profit called pure charity and uh we have a rail stack and earlier
[2824.12 --> 2830.60]  this year we had some uh developers leave the company and we had a big push coming for the
[2830.60 --> 2838.46]  summertime for for a a uh a new feature we were working on and uh it hit me that that we should
[2838.46 --> 2844.36]  call upon our awesome friends at top towel um and just to kind of give you a snapshot top towel
[2844.36 --> 2852.04]  is a matchmaking service for really awesome developer opportunities and developers to get
[2852.04 --> 2859.48]  started so we had a need for some really great ruby and rails developers and top towel helped us
[2859.48 --> 2867.84]  find developers that fit not only our budget but also our culture our coding style all sorts of things
[2867.84 --> 2873.62]  and long story short they basically perform magic because these people we work with i'm gonna give a
[2873.62 --> 2879.72]  shout out to them real quick if you don't mind guillermes uh andre and jafael all listeners of the
[2879.72 --> 2888.44]  changelot too by the way these guys are phenomenal good people good coders and just great all around
[2888.44 --> 2894.28]  great and i have to say thanks to top top because they made this possible and if you've been thinking
[2894.28 --> 2900.30]  about freelancing if you're thinking about uh trying out a new technology or you wanted some flexibility
[2900.30 --> 2907.58]  in your work life balance and doing some travel top towel is a great place to be an elite engineer
[2907.58 --> 2913.40]  go to top towel.com slash developer to get started and tell them the changelog sent you
[2913.40 --> 2923.20]  and um totally i think it might be completely left wing here but you also wrote lib ssh2 do you want
[2923.20 --> 2928.46]  to touch on that real quick before we start to tell the call um yeah i mean that's really nothing
[2928.46 --> 2933.26]  nothing particularly php related except in that um at the time i was working on a lot of streams
[2933.26 --> 2939.68]  work in php um streams are sort of this abstraction layer we have underneath all the fopen fread fwrite
[2939.68 --> 2945.06]  those sort of calls um so that you can work with different sorts of resources so you can do something
[2945.06 --> 2950.86]  like fopen an http url and that'll talk http to the remote server and you can fread off of that
[2950.86 --> 2956.46]  remote network resource and it's great um i thought gosh how cool would that be if i could do that with
[2956.46 --> 2964.94]  like scp um s s ftp no f yeah sftp files sorry it's been a while since i even touched this library
[2964.94 --> 2973.26]  um sftp files or scp resources or just even be able to ssh into a system and send a command to it
[2973.26 --> 2979.86]  you know how cool would that be um well i looked at uh open ssl and said can i actually you know pull
[2979.86 --> 2988.94]  a library out of this oh god oh god no oh god look away um open ssl is a lovely uh piece of software
[2988.94 --> 2998.88]  um but it's it's also got a very interesting code base um so i i ended up just going to uh ietf and
[2998.88 --> 3004.48]  i said where's the rfcs for secure shell oh here they are let's start implementing a transport let's
[3004.48 --> 3010.36]  start implementing a few channels let's start implementing this um next thing i know i've got
[3010.36 --> 3016.00]  this entire you know client side library for connecting to ssh servers um so that i can
[3016.00 --> 3021.26]  shove it into php and then promptly not use it because while it's cool it's actually not that
[3021.26 --> 3027.98]  um you know practically useful for anything that i'm working on um it was just sort of i was working
[3027.98 --> 3032.60]  for the university at the time and the thing about working for uh public institutions is that you have
[3032.60 --> 3041.76]  um very relaxed goals and extra time on your hands um which is actually how i own getting
[3041.76 --> 3047.46]  involved in php in the first place it sure seems like uh you enjoy diving in deep and getting into
[3047.46 --> 3053.60]  the nitty-gritty is that fair to say well i like understanding what i'm working with um you know i i
[3053.60 --> 3060.88]  i will search google for how to's and documentations with the best of them but if i'm really going to do
[3060.88 --> 3065.50]  something with something i really want to understand how it works underneath um on the hhvm project right
[3065.50 --> 3072.78]  now my main job is to make php a good open source project which really means i don't have to look at
[3072.78 --> 3078.96]  much of the code at all theoretically um i can work on the build system some of the runtime library apis
[3078.96 --> 3084.18]  things like that but i don't need to get down into the jit and start issuing machine code instructions
[3084.18 --> 3090.46]  uh to do what i need to do for my job but gosh i'd actually like to understand how that stuff
[3090.46 --> 3097.76]  actually operates wouldn't i so um so i have so i've i've got uh commits down in there and i now
[3097.76 --> 3108.66]  for no further use in my life probably uh have the abis for uh intel x8 x64 architectures and arm v8
[3108.66 --> 3117.54]  uh i know that the first six integer arguments of a function call go to rdi rsi rdx rcx r8 and r9
[3117.54 --> 3123.98]  the first eight simd registers go into xmm0 through xmm7 and then everything else goes on the stack
[3123.98 --> 3130.40]  um will i use that again probably not uh but it was fun to write the code that actually used it and it
[3130.40 --> 3136.66]  shortened our uh the compile time of one of our files from 100 seconds down to 10 so wow that was good
[3136.66 --> 3142.94]  that was good that was good that was really good yeah that was really good yeah we were using these
[3142.94 --> 3148.48]  recursive variadic templates which you know god bless c++11 it's a it's a beautiful extension to
[3148.48 --> 3155.58]  the c++ language but oh it hurt my head to read that thing like reading assembly was easier than reading
[3155.58 --> 3162.98]  this so that's saying a lot well after after listening to you talk for a while i'm sure uh you know there
[3162.98 --> 3168.20]  might be people out there to whom you're becoming their programming hero because you seem to have a
[3168.20 --> 3173.80]  lot of skills and a lot of knowledge i want to turn that on you and ask uh as we wrap up here uh
[3173.80 --> 3177.88]  who's a programmer that you look up to and that you would consider your programming hero
[3177.88 --> 3183.52]  oh well i'm glad you said look up to because the word hero is a really heavily loaded term for me okay
[3183.52 --> 3189.16]  um and i i'm not going to say i have programming heroes i definitely have people that i admire
[3189.16 --> 3195.38]  um a couple of people on my team that i just want to give shout outs to um mark williams um he's been
[3195.38 --> 3200.40]  on the project for a very long time he understands everything about um repo authoritative mode in our
[3200.40 --> 3207.22]  system and a bunch of the um the the weirdly arcane bits of our system when somebody has a question
[3207.22 --> 3212.22]  they go to mark because mark knows it top to bottom he's a really good compiler designer
[3212.22 --> 3216.52]  um and he's actually really friendly in his responses he's very generous with his information
[3216.52 --> 3223.88]  um similarly jordan delong i want to call out uh because this man knows the c++ spec by heart
[3223.88 --> 3233.12]  um he probably listens to it on tape every night um and and he like when when i when i come to him
[3233.12 --> 3237.72]  and i say you know i'm trying to solve this particular problem and um i i need to achieve
[3237.72 --> 3242.84]  these two things but i just don't see how they fit together he'll just be like oh well here and he'll
[3242.84 --> 3248.00]  scribble something on a piece of paper and he'll hand it to me and say try something like that i
[3248.00 --> 3251.16]  mean he'll explain it as well it's not as though he's just you know throwing a piece of paper at me
[3251.16 --> 3257.06]  but like he'll actually sketch out an implementation while we're sitting there and and and and say you
[3257.06 --> 3260.48]  could try something like this this will probably do what you want you may have to you know check the
[3260.48 --> 3265.48]  other thing over there um he smiles a lot he's a really friendly guy um so i definitely want to
[3265.48 --> 3275.74]  call those guys out um heroes gosh you know honestly anyone who who looks at a piece of open
[3275.74 --> 3281.76]  source software that they use that they make their living on that they that they uh that they care
[3281.76 --> 3288.06]  about at all and says i want to make this better i want to give back i want to do something that's not
[3288.06 --> 3293.14]  going to profit me immediately at all those are my heroes man like just open source developers in
[3293.14 --> 3300.94]  general like i love that there is this community out there and i i i had a conversation on the last
[3300.94 --> 3306.66]  night of oscon with with a guy i've known for a long time john kagashal um he's he's very concerned
[3306.66 --> 3314.36]  that some of our culture is getting lost um and some of some of our uh like collectively our uh commitment
[3314.36 --> 3321.36]  to to open source and and uh real open source is is getting sort of sucked up by the corporate
[3321.36 --> 3325.46]  machine um he actually made a bet with me that night we were standing out in an intersection in
[3325.46 --> 3330.04]  portland at like two o'clock in the morning shouting at each other um he made a bet with me he said i'll
[3330.04 --> 3335.72]  bet you 20 bucks facebook never actually lets go with the spec and never actually makes it you know a
[3335.72 --> 3341.96]  properly community open source thing and he emailed me after the uh the spec actually got released on
[3341.96 --> 3349.14]  php's git server he says all right i'll owe you 20 bucks that's fast so that's a conversation i think
[3349.14 --> 3354.54]  we've uh we've kind of had here and there on this show too just this um this sort of descent towards
[3354.54 --> 3359.72]  corporations and their takeover of open source and what true open source is we've had um to kind
[3359.72 --> 3365.40]  of call it a corporate source right yeah uh we had chad whittaker on who's uh runs get up and he's
[3365.40 --> 3370.64]  obviously pretty uh prolific in that he's open company kind of person we had some deep conversations
[3370.64 --> 3375.30]  both on the show and then after the show as well with them on that so we've kind of danced around
[3375.30 --> 3381.66]  that quite a bit i think that's just a natural fear when it comes to like profit and and uh and
[3381.66 --> 3386.64]  source code you know they just then you got things like bounty source and people want and there's
[3386.64 --> 3393.26]  legitimate reasons for people wanting to raise money to build something um i'm thinking like tim
[3393.26 --> 3396.52]  caswell i don't know if you listen to that show or not but he did some pretty cool stuff and
[3396.52 --> 3401.14]  um he's just really interested in building infrastructure code not really building products
[3401.14 --> 3408.06]  on it and he's trying to find ways to do that full time and make it completely open source and
[3408.06 --> 3413.22]  i think that's just naturally it's something we want to support but it's it's neat to see the
[3413.22 --> 3418.82]  contrast of like corporates taking over and uh what you call real open source i'm curious to know what
[3418.82 --> 3426.08]  he meant by that but uh one last question we have is uh is it called arms it's a call to arms to like
[3426.08 --> 3432.76]  uh the php spec you know whatever you can think of really that that you're um you know spending your
[3432.76 --> 3437.32]  days on how can the community wrap themselves around whatever um you think is most important
[3437.32 --> 3443.08]  what's some good guidance to the php community as it as it is to what you're working on well i mean
[3443.08 --> 3448.38]  the first piece of guidance i would give no matter what project we're talking about whether it's php or
[3448.38 --> 3455.38]  anything else you know don't feel afraid to get involved in an open source project just because
[3455.38 --> 3460.36]  you don't think your coding skills are up to par or because you think that um you know somebody's
[3460.36 --> 3465.70]  not going to like your ideas you might get yelled at a couple of times because people are kind of jerks
[3465.70 --> 3471.08]  but sometimes not everyone's a jerk and not everyone's not most people aren't jerks all the time
[3471.08 --> 3477.20]  um and you can also pick something that you feel comfortable with if that means documentation
[3477.20 --> 3482.02]  god you will get loved for writing documentation you want to build you want to keep people from
[3482.02 --> 3488.62]  yelling at you write documentation and they will love you for life um something like the spec you know
[3488.62 --> 3495.42]  we we knew there were grammatical and spelling mistakes in the spec when we released it and we're
[3495.42 --> 3499.84]  like you know we're okay with that because that's a nice low-hanging fruit that somebody can come along
[3499.84 --> 3504.28]  and just say hey here's a pull request and the next thing you know you've got somebody who's involved
[3504.28 --> 3510.38]  in the project who has this feeling of stakeholdership over it even if it's just i got them to use
[3510.38 --> 3516.30]  the right spelling of the word too you know that i've done that before that's something yeah i mean
[3516.30 --> 3521.58]  and the next thing that person's going to do is they're going to actually start writing some
[3521.58 --> 3525.62]  real documentation in there and then the next thing they're going to do is they're going to fix
[3525.62 --> 3533.02]  some little runtime uh function that is a nice easy little tweak of code my first patch to php um i should
[3533.02 --> 3538.58]  say by the way i did i did not go to school uh well not to college anyway um i don't have any formal
[3538.58 --> 3547.76]  training in any language um i've learned uh c just kind of by jumping in and trying it out my first
[3547.76 --> 3553.30]  patch to php with very little c experience was just to take the log function and give it a second
[3553.30 --> 3558.72]  parameter so you can get logs in an arbitrary base it was a really easy patch to do it was a very tiny one
[3558.72 --> 3564.92]  i sent it to the mailing list they said this is formatted wrong do it again oh okay and then i
[3564.92 --> 3568.84]  reformatted it i sent it and they said oh this looks lovely thank you here would you like some
[3568.84 --> 3573.96]  karma to commit some more patches in the future like that's and that's how it started all it takes
[3573.96 --> 3579.36]  to get involved in open source and if if you're sitting there and if you're thinking gosh i'd like
[3579.36 --> 3586.60]  to to work on some project but i'm just not up to it you're wrong just do it just do it yeah we uh
[3586.60 --> 3591.16]  you're not going to get fired i think the barriers are even lower now with the way that coding has
[3591.16 --> 3594.52]  become social with github i think back when you know in the karma days it might have been a little
[3594.52 --> 3600.60]  different and higher barriers and now it's even lower barriers oh github has done wonderful things
[3600.60 --> 3606.72]  for just bringing everybody out of the word woodwork because you can find your project so fast you can
[3606.72 --> 3611.96]  fork it with a single button press you can make a little branch publish it to your own version of
[3611.96 --> 3615.62]  it you don't have to find some place to host your code it's just right there next to the project
[3615.62 --> 3622.54]  people can even discover your fork of it through the the the uh the ui it's fantastic love github
[3622.54 --> 3629.72]  love github well sarah it definitely has been quite a blast having this chat with you thank you so much
[3629.72 --> 3634.96]  for taking the time you have taken to to step away from what you do at eight in the morning your time
[3634.96 --> 3639.38]  to have this chat with us i'm sorry for making you get up maybe a little bit earlier at least
[3639.38 --> 3644.00]  talking for this long and this excitedly about what you do at eight in the morning it's just probably
[3644.00 --> 3648.74]  not your maybe it's your norm i don't know but i usually wake up about an hour and a half from now
[3648.74 --> 3654.34]  okay so you she woke up earlier just to have the conversation so um we really appreciate you taking
[3654.34 --> 3661.04]  the time and just um your passion for you know for open source and and even you know your hero
[3661.04 --> 3665.30]  statement there was like anybody who commits to open source with a generous heart and just really
[3665.30 --> 3670.18]  wants to see it grow and not so much gain profit from it and i really appreciate you sharing all the
[3670.18 --> 3675.24]  all that you have shared today on the show and you know as best you can keep in touch with us we'll
[3675.24 --> 3680.90]  do whatever we can to help uh you know help mention whatever you do in the future and maybe we can get
[3680.90 --> 3684.70]  uh someone back on the show again i like the the conversation we had there at the end so i'll ping
[3684.70 --> 3689.86]  you via email and see if we can't extend some conversations we had here today but i do want to
[3689.86 --> 3694.98]  mention three of our sponsors digital ocean coachip and top top for helping make this show possible
[3694.98 --> 3701.00]  they are awesome five by five is awesome if you don't listen uh to any other shows on five by five
[3701.00 --> 3705.34]  go to five by five dot tv uh right now and check some other shows out the changelog's on there at
[3705.34 --> 3712.44]  slash changelog we broadcast every week live myself jared and awesome guests like sarah so at this time
[3712.44 --> 3717.84]  everyone let's let's say goodbye bye goodbye
[3717.84 --> 3731.28]  you
