[0.00 --> 13.78]  welcome back everyone this is the changelog we're a member supported blog and podcast
[13.78 --> 18.36]  that covers fresh and what's new in open source you can check out the blog at the changelog.com
[18.36 --> 23.10]  and our past shows at five by five dot tv slash changelog the show shows by myself adam
[23.10 --> 28.38]  and also andrew thorpe hey what's going on i didn't ask you to say hello this week did i
[28.38 --> 33.34]  no winging it kind of threw you off a little bit yeah we're always winging it around here so
[33.34 --> 37.54]  to to wing it even further you can tune in live every tuesday at five central standard time here
[37.54 --> 44.60]  on five by five and this is episode 101 and we're joined by ajak schluder he's the maker of npm
[44.60 --> 50.82]  he's the core maintainer of node and he's also a javascript hacker obviously at uh at joy in welcome
[50.82 --> 57.00]  to the show isaac thanks happy to be here it is uh it's been a while since we had uh this topic
[57.00 --> 64.32]  on the show but before we uh dive deep into this conversation we have a sponsor yeah so real quick
[64.32 --> 69.08]  i want to give a shout out to pete keen for sponsoring our show today he has a new ebook
[69.08 --> 74.36]  out there called mastering modern payments using stripe with rails we use stripe at the changelog
[74.36 --> 79.72]  who doesn't right and his book aims to help you with topics like why a simple 10 minute integration
[79.72 --> 86.76]  isn't enough dealing with security including pci dss stripe js checkout js subscriptions marketplaces
[86.76 --> 91.18]  testing and more it's a great resource for rails developers that want to get started with stripe
[91.18 --> 99.64]  for 29 you get the guide which includes 116 pages and a 100 code samples for 59 you get the source code as
[99.64 --> 105.86]  well and for 299 you get a team license so you can share it all with up to 50 team members
[105.86 --> 113.06]  check it out at petekeen.net slash mastering hyphen modern hyphen payments thanks a ton to pete for
[113.06 --> 117.94]  sponsoring today's show absolutely man that's uh we we love stripe man i absolutely love stripe
[117.94 --> 123.80]  yeah i think a lot of developers are kind of heading that way so so yeah it's so easy to use and it
[123.80 --> 130.22]  integrates with everything man and geez well cool so we got isaac on the show uh isaac i i hear you know
[130.22 --> 137.30]  something about node um yeah so i've been uh been working on node pretty much since there's been node
[137.30 --> 142.98]  not quite as long as a couple of other people but i think as far as people who are actually involved in
[142.98 --> 150.74]  the project still uh i'm one of the oldest why don't you give us an introduction to to uh who you are and
[150.74 --> 159.34]  maybe who joint is and you know what node is sure so um i actually was kind of involved with uh doing
[159.34 --> 164.84]  some stuff with server side js i was a php developer prior to that and got more and more annoyed that i
[164.84 --> 171.16]  had to write uh one language on the client and another on the server and um even more annoyed that
[171.16 --> 179.88]  the server language was not javascript um so i got started kind of messing around with uh you know
[179.88 --> 185.42]  spider monkey and and web core and um jscore and kind of like trying to figure out how to do something
[185.42 --> 192.86]  on the server and then um uh but i didn't actually know what i was doing and uh around that time then um
[192.86 --> 201.06]  google open sourced v8 and so i started playing with that and you know lo and behold this like new
[201.06 --> 208.00]  thing showed up on the scene called node uh so i you know the website looked really nice and it seemed
[208.00 --> 213.42]  like it had a really nice api so i i you know downloaded the source code and tried to build it checked it
[213.42 --> 219.04]  out from git or whatever and it didn't compile so i was like okay well this is obviously not real and
[219.04 --> 226.30]  never gonna go anywhere um and so i kept i kept playing around i got got kind of into uh narwhal
[226.30 --> 233.50]  and the common js stuff and then somebody at a i gave a talk at a meetup at yahoo about um
[233.50 --> 240.04]  about using javascript on the server and and you know some of these ideas of of common js and the
[240.04 --> 245.10]  module pattern and this kind of stuff and um somebody in the audience asked me if i'd ever heard of
[245.10 --> 251.94]  node and you know kind of nudged me to go take a look at it again um i don't remember who that person
[251.94 --> 259.52]  was but uh i'm i'm sure it's uh it'd be it'd be nice to know who that who that actually was i wonder
[259.52 --> 264.12]  if they're still involved with node but um so if they're listening to this podcast now
[264.12 --> 273.30]  it's at izz on twitter yeah yeah i i think it was um i think it was also one of the first projects
[273.30 --> 276.48]  he pointed me at something that was one of the first projects that ever used a dot io
[276.48 --> 283.06]  domain i don't think it was socket io i think it was some other like io thing uh and it was built
[283.06 --> 287.98]  on node and so i took a look at it and i downloaded it that was version like 0.0.6 and so that was the
[287.98 --> 294.86]  first one i tried that actually compiled on my mac and you know i i immediately basically stopped what
[294.86 --> 299.32]  i was doing and said like okay this is this is the right way to do it um this is the one that i'm
[299.32 --> 307.26]  gonna actually focus on and and play with and so um yeah i was kind of hooked and i mean there was this
[307.26 --> 314.62]  this dude in germany had written it this like ryan doll guy and then a couple months later this uh
[314.62 --> 319.98]  video came out from him giving a talk at node confi you i knew he was going to be at node confi you i
[319.98 --> 325.16]  knew that he was uh you know i knew him from the irc channel and stuff and we'd been sort of chatting
[325.16 --> 331.58]  and and whatnot and then when he when i saw his talk the video i was like oh wow like he's he's not
[331.58 --> 338.30]  german he's he's american um so that was kind of like the big a big shock for me early on um everybody
[338.30 --> 342.18]  else was shocked by that video because that was when most people i think found out about node that's
[342.18 --> 347.90]  kind of the uh the the big coming out of node as a project and being presented to the world
[347.90 --> 355.60]  so uh yeah you know i was really active in the the mailing list and stuff and um just it was very
[355.60 --> 363.96]  very small community very tightly knit and um i got kind of sick of uh working at at yahoo and and
[363.96 --> 368.94]  just being at a big company got kind of fed up with it so i quit my job and spent two months just
[368.94 --> 372.56]  messing around with i was like i'm just gonna like take a few months off and see what happens
[372.56 --> 377.00]  and what i found was it was really frustrating on the mailing list because people would post these
[377.00 --> 380.80]  things where they like they would post this announcement that they wrote some new project
[380.80 --> 386.64]  in node some like new reusable module in node and oh god it was always such a pain it's always like
[386.64 --> 391.26]  okay so here's what you do you download this thing and you run make and then you copy this file
[391.26 --> 396.02]  into your into this folder and you also have to copy this other file because it depends on this
[396.02 --> 399.26]  thing and it has to be this certain version and it's always a get sub module so you have to get
[399.26 --> 405.14]  sub module update and i was like oh god this is just this is a nightmare um and in the four years
[405.14 --> 408.42]  that i'd worked at yahoo you know there's this really cool tool called wyants so you just type
[408.42 --> 416.04]  wyants install whatever it fetches all the down all the uh the dependencies um and it has like it's a
[416.04 --> 421.82]  really nice sort of platform to actually build your your programs as well as distribute and install
[421.82 --> 429.50]  them and it's very low bandwidth low um barrier to entry um so i kind of took some of those ideas
[429.50 --> 436.10]  and and set about writing a package manager for node there was a couple of other options at the
[436.10 --> 443.74]  time um tj holloway chuck actually wrote one called kiwi uh which was written in bash and had a very very
[443.74 --> 449.92]  pretty interface um you know this sort of like stereotype of of tj holloway chuck stuff it's
[449.92 --> 455.14]  always like you know extremely extremely polished and and pretty the thing that bugged me about about
[455.14 --> 459.80]  it um and there there was a couple others too there was a few that were based on git there was two
[459.80 --> 466.08]  actually that i remember that were based on git um and use that as the transport mechanism uh
[466.08 --> 472.48]  and a couple of others and the thing that that kind of bugged me about all of them was that the um
[472.48 --> 480.16]  the path to publishing something was much much too difficult and usually relied on uh either you
[480.16 --> 488.44]  telling everybody the the you know the git repo that they need to go and install or you have to um
[488.44 --> 493.24]  you know you had to have somebody merge in a a patch to add your thing to the to the registry of
[493.24 --> 499.78]  published modules and i thought this is just this is too hard so i said about basically take i took a
[499.78 --> 509.52]  couple months and basically wrote what ended up being npm um and the the premise of it was to
[509.52 --> 517.16]  basically not require any um any unnecessary ceremony from writing your project to actually
[517.16 --> 521.68]  having somebody install it and because i had no job at the time and nothing really to do
[521.68 --> 526.34]  i went around and sent pull requests to every node project to add a package.json to them
[526.34 --> 534.28]  that's a good way to do it yeah i think i wrote an option exactly um and i think the main reason
[534.28 --> 538.52]  why npm ended up being the package manager everyone uses is that i didn't have a job then and everybody
[538.52 --> 545.16]  else did um and so you know it just had somebody kind of through force of will sort of pushing on it
[545.16 --> 551.14]  to to get the community to use it and um you know it's it's a very easy as you know like if you've
[551.14 --> 557.72]  ever gotten a pull request to add like a um travis ci or something like it's very easy to just say
[557.72 --> 562.00]  like here's one file you know it's not going to be in your way it's like one file you got to put in
[562.00 --> 567.78]  there it's short it's easy to read you know just accept this pull request and i and the world will
[567.78 --> 574.28]  be better um and and people very for the most part were very accepting of that because there wasn't a lot
[574.28 --> 580.22]  of things doing that i mean nowadays now that you have package.json and component.json and some yml
[580.22 --> 586.20]  travis yml and like some other thing it it's you know it's starting to along with like your license
[586.20 --> 591.42]  your readme your git ignore yeah so now people are a little bit more uh resistant to this sort of thing
[591.42 --> 595.92]  but at the time it was it was a very easy sell so you know let me interject here real quick the yeah
[595.92 --> 600.80]  we'll talk more about you know all this stuff npm and all that but it's it's kind of striking the
[600.80 --> 606.28]  similarity that node and and with npm has had like with you know my experience in in the ruby
[606.28 --> 613.68]  community with ruby gems coming up and uh how much of npm would you say was influenced by you know
[613.68 --> 621.20]  ruby gems and just that whole environment uh roughly zero and that's not to say i mean that's not to say
[621.20 --> 625.20]  that they're not similar because like the similarities have been pointed out to me a lot of times but i
[625.20 --> 630.42]  i have almost no experience with ruby i've you know i've edited a few ruby programs just because
[630.42 --> 636.20]  they're kind of out there and you can't it's kind of inescapable right such a very popular platform
[636.20 --> 647.00]  but uh no i i think it was mostly influenced by wanting to not be pair right and wanting to kind
[647.00 --> 654.30]  of emulate what worked what i saw work for wyantst yeah i mean it's it's it's cool i've heard i actually
[654.30 --> 660.58]  listened to um i want to say it was the the node podcast that you did with two other guys and i was
[660.58 --> 665.26]  listening to the first episode i think you know this was months ago and i remember you guys were
[665.26 --> 671.42]  just kind of talking about how you know node is it's obviously very young and it's kind of following
[671.42 --> 676.52]  in similar tracks as other you know modern technologies have gone and it's it's always been
[676.52 --> 681.50]  kind of shocking to me that you know it's not exactly the same and the pitfalls you know don't look
[681.50 --> 686.22]  exactly the same but but you kind of have to go through the same growth uh problems as you know
[686.22 --> 690.28]  just package management in general is a common growth problem that these young frameworks have
[690.28 --> 693.86]  to go through and i don't know it's kind of striking that they all go through the same ones
[693.86 --> 700.10]  yeah yeah absolutely and i mean the big question is like can you evolve past those problems or not
[700.10 --> 707.18]  yeah i think as far as like you know if you look at i hate to pick on pair but at the same time i
[707.18 --> 712.22]  obviously don't hate it that much because i do it a lot right um but pair is basically i think the
[712.22 --> 716.76]  object example of what happens when you try to have too much ceremony in a in a package ecosystem
[716.76 --> 723.78]  um that that module ecosystem is effectively dead now thankfully for the php community like the php
[723.78 --> 729.20]  community as a whole wasn't really too dependent on it and you have stuff like packages and composer
[729.20 --> 735.58]  coming up from with more of like a ruby gems mtm kind of model so it's very low um
[735.58 --> 743.24]  low barrier to entry and a small amount of ceremony to get started right so you talked a little
[743.24 --> 749.84]  bit about just you know how you came about with mpm so how did the uh i i kind of stopped you so if
[749.84 --> 753.78]  you want to keep going about just kind of how that that brought you into the the node js community
[753.78 --> 760.88]  as a whole and then where joint came about and all that sure so um so i'd been uh jobless for a
[760.88 --> 767.56]  while and uh got this job working for this company doing this stuff that wasn't really related to node
[767.56 --> 773.40]  and kind of disappeared off the map a little bit off of that group and you know it was frustrated i
[773.40 --> 778.22]  wanted to get more into node and and do something that's more node specific and and i was thinking
[778.22 --> 784.62]  about starting this uh some kind of little startup or whatever with a couple of guys and and i mentioned
[784.62 --> 790.70]  this to ryan and he said no no no no don't do that come work at joint you'll have you'll have
[790.70 --> 800.26]  health benefits and like a salary today and i was like oh well yeah okay um yeah and and that was
[800.26 --> 807.78]  basically my job interview and uh then i came here and started working on on node and npm um at joint
[807.78 --> 812.96]  you kind of have the dream job though i mean because i mean how many people are listening to the show
[812.96 --> 817.74]  right now hacking on open source that would love to hack on open source and get paid to do it
[817.74 --> 823.90]  yeah well that's i mean that's a fascinating subject actually i think i think a lot of people get a lot
[823.90 --> 829.74]  of people really really like working on open source i think there's a lot of um intrinsic motivation that
[829.74 --> 835.84]  really drives us to write software and write really good software and focus a lot of uh care and time
[835.84 --> 841.08]  and attention and feel very rewarded by this however like the financial incentives often just aren't there
[841.08 --> 848.08]  and so yeah i do have a dream job and it would be really nice if there was you know ways for other
[848.08 --> 855.14]  people to be more to do this as their job you know it's um it's definitely a passion of mine and
[855.14 --> 861.32]  something i hope to maybe one day figure out some way out of but um so you know some just to paint
[861.32 --> 866.00]  this picture a little bit for the listeners so you quit your job to work on open source then got a job
[866.00 --> 871.84]  to work on open source yes which is good because i i mean which is good because i i couldn't do that
[871.84 --> 879.66]  forever um you know at some point i was going to have to do something to to make money and uh sending
[879.66 --> 883.96]  people pull requests to add package.json files to their projects wasn't really paying the bills
[883.96 --> 891.04]  well in a sense it was though because would you say that the success of npm is kind of well i guess a
[891.04 --> 896.50]  better way to put it is when you came on to joint full-time to work on node full-time was it was npm
[896.50 --> 902.24]  mature at that point to where it was the primary adoption for package management in node oh yeah
[902.24 --> 906.90]  yeah that that was that was well established at that point yeah so if you think about it like all
[906.90 --> 912.72]  those long you know nights of submitting package.json uh pull requests probably was paying the bills in
[912.72 --> 919.42]  a sense maybe yeah i mean i i think it's i think it is a good case checks yeah it is a good example of
[919.42 --> 924.88]  you know if you if you do something that you're really passionate about it i think it's a misnomer
[924.88 --> 928.94]  to say that if you know it's it's not exactly true to say that if you do what you're passionate
[928.94 --> 935.94]  about the money will come right but if you do almost anything really diligently then the money will
[935.94 --> 942.82]  come and it takes passion to have that kind of diligence you know so if if um and a lot of things
[942.82 --> 947.00]  like if you do almost anything really diligently you'll figure out what parts of it you like and what parts
[947.00 --> 951.40]  of it you don't and that'll help inform your choices when it comes to you know choosing a job
[951.40 --> 958.10]  or or doing another thing right so why don't you kind of give us a uh an overview of just you know
[958.10 --> 965.48]  what node is i don't we haven't really talked about that yet so oh yeah sorry so node is uh a platform
[965.48 --> 974.56]  for writing asynchronous io based servers in javascript um it's a i think the the tagline is
[974.56 --> 982.76]  invented io for v8 javascript which basically means um so v8 javascript is pretty straightforward it uses
[982.76 --> 990.66]  the v8 um javascript virtual machine as its its way of you know running your program but the uh the
[990.66 --> 995.24]  nice thing about javascript is it doesn't actually have a built-in io mechanism as part of the language
[995.24 --> 1002.08]  so whereas in ruby or python you have this you know standard library which has you know predefined
[1002.08 --> 1008.60]  mechanisms for reading files and stuff in node um or in any javascript program right there's there's a
[1008.60 --> 1014.56]  lot of stuff for doing like you know loops and functions and what have you but there's no um there's
[1014.56 --> 1021.44]  no way to write a file in javascript right so node also links to a program called a library called lib uv
[1021.44 --> 1031.32]  which is um it it's a an abstraction for doing um asynchronous io or non-blocking io
[1031.32 --> 1038.24]  in um across different operating systems so for example in um
[1038.24 --> 1045.90]  i always get wrong like which ones have which but there's so there's uh in the unix land there's stuff like
[1045.90 --> 1058.58]  kq and in e-pole and so forth in um in windows there is uh cp um iocp i o completion ports and
[1058.58 --> 1066.46]  so lib uv is like a bridge across these two um or three or actually four like very different worlds
[1066.46 --> 1074.18]  um of of ways of doing io in a in a non-blocking way so what non-block let's explain what non-blocking
[1074.18 --> 1083.18]  means um in uh in a you know like any any old random program like a you know c program or shell
[1083.18 --> 1088.80]  script or what have you you open a file and you call you know var you know int fd equals
[1088.80 --> 1097.58]  fopen and you give it a path name right right um and that that open call that open method will
[1097.58 --> 1103.42]  return the the file descriptor then you pass that file descriptor to a read operation and that read
[1103.42 --> 1108.92]  operation returns you know the um well and see it returns a number of bytes read but let's say if
[1108.92 --> 1112.40]  in like a higher level language it would just return you a string or a buffer of some sort
[1112.40 --> 1117.70]  indicating representing the the memory that it read well the problem with that
[1117.70 --> 1124.96]  is that if you have a um if you have a server like an http server its job is to be serving requests
[1124.96 --> 1130.36]  right now most of the time when you're doing a read operation you're just kind of sitting there
[1130.36 --> 1137.12]  waiting for the hard drive controller to respond um or if you you know if you make an http request
[1137.12 --> 1143.16]  right you you send the request out and then you like sit there and wait for the um for the response
[1143.16 --> 1147.22]  for the packets to get sent over the network and then for the response to get sent back and
[1147.22 --> 1150.98]  there might actually be multiple packets you have to receive before you can parse out the full http
[1150.98 --> 1157.78]  response so if your program is sitting there doing nothing right you're not serving new requests and
[1157.78 --> 1162.22]  you're you're not actually you're just kind of blocking on cpu you're not actually doing anything
[1162.22 --> 1170.38]  so nodes approach to this is a little bit different you um in the case of where you you know make an http
[1170.38 --> 1177.36]  request what you do is you get back a request object went from from that http request and every
[1177.36 --> 1182.30]  time there's new data available you know then when the response comes back you pass it a function that
[1182.30 --> 1188.26]  function gets the response object now every time the response object gets another chunk of data it and
[1188.26 --> 1193.72]  it's a data event and so you attach functions to these things in order to handle this stuff at some
[1193.72 --> 1199.46]  future time right in the simple in the simplest case if you do like you know fs.read file you pass
[1199.46 --> 1204.12]  it the name of the file and a callback to get um which will get an error or the data
[1204.12 --> 1210.34]  at some future time and so then this is like the callback callback hell that you've heard people talk
[1210.34 --> 1214.08]  about where you have you know one thing that calls another thing that calls another thing that calls
[1214.08 --> 1220.06]  another thing and your code keeps indenting because you keep defining new right um it's kind of a
[1220.06 --> 1227.66]  it's kind of a novice novice uh problem but um it does make it does need require you to kind of
[1227.66 --> 1234.44]  invert your thinking about how you do io right um the the blessing and or curse of node is that you
[1234.44 --> 1242.46]  you can't just ignore things that take a long time to do so let me ask you the early on in node i
[1242.46 --> 1248.60]  kind of got it well no not early on but early on for me in node i was on the uh and on the mailing list
[1248.60 --> 1252.96]  and and i i would start to see these arguments and and you just like i hear buzzwords and i start to
[1252.96 --> 1256.72]  see these arguments about callbacks come up and i can't remember i think it was like pipes and streams
[1256.72 --> 1263.48]  and callbacks and all that uh so you obviously know what i'm talking about um so elaborate on that a
[1263.48 --> 1268.30]  little bit when you talk about callbacks is that i guess just elaborate on what what's the i don't know
[1268.30 --> 1275.26]  the the you know the um standard way the right way the uh you know how do you handle this stuff
[1275.26 --> 1285.26]  so this is a trap um there's we'll we can edit it out later
[1285.26 --> 1294.78]  no no it's okay it's okay it's it's a trap i'm familiar with um so there's there's two answers
[1294.78 --> 1299.34]  to this um there's there's isaac the person the programmer and what do i prefer and then there's
[1299.34 --> 1303.46]  like what is the official stance of the node project right and they're not exactly the same
[1303.46 --> 1310.58]  so um basically a callback is just a function um it's a function that you pass to some other method
[1310.58 --> 1318.84]  that will be called with the results of that operation in um you know in in scheme this would
[1318.84 --> 1324.06]  be called a continuation and actually in scheme the semantics are completely different so calling
[1324.06 --> 1329.00]  called if you call callbacks continuations then certain people get really upset yeah they get
[1329.00 --> 1335.72]  beards on their necks parentheses all over the place and uh oh goodness i'm getting an email
[1335.72 --> 1342.08]  so um anyway a callback is just like a thing to say okay here i want you to go read this file and once
[1342.08 --> 1346.94]  you're done reading that file put the data in here and then go do this other stuff in the meantime i'm
[1346.94 --> 1353.66]  gonna go do these three other things um so you get that you get into the situation where like
[1353.66 --> 1357.68]  okay i don't actually just want to read a file usually i want to read a file then i want to upload
[1357.68 --> 1362.86]  it somewhere and then depending on the status result of the upload whether it gave me a you know
[1362.86 --> 1368.14]  two or whatever or a 409 i want to go do this other thing and read this third file and parse it and
[1368.14 --> 1373.04]  then send the results over here right so if you're doing this all with a callback based system there's
[1373.04 --> 1378.92]  a tendency to well you in general there's a tendency to put too much code in one place right that's
[1378.92 --> 1385.52]  kind of a universal thing like factoring out programs is hard right so in node this hard this
[1385.52 --> 1391.80]  difficulty is readily apparent because you end up six levels indented and suddenly your your code is
[1391.80 --> 1395.90]  like all the way off the right hand corner of your right hand side of your screen so
[1395.90 --> 1404.92]  there's a couple of ways to deal with this the way that isaac the person uh you know my my personal
[1404.92 --> 1413.12]  preference is just factor your damn program like break it up into chunks create named functions that have
[1413.12 --> 1419.72]  like meaningful names and do one like really well defined thing and make those functions take a
[1419.72 --> 1424.84]  callback and just use it and just pass that callback around it's not actually all that hard um
[1424.84 --> 1436.30]  the the some alternative uh ways of looking at that are that you can use things like coroutines where
[1436.30 --> 1441.40]  what you actually do is you tell the you tell the interpreter okay i want you to pause my
[1441.40 --> 1446.70]  my program's execution at this point because i'm going to go and i'm going to wait for this thing
[1446.70 --> 1450.88]  to happen but in the meantime you can go run other stuff just don't keep running the rest of this one
[1450.88 --> 1455.76]  function and then when it comes back with the results right so you you flip it so that it looks
[1455.76 --> 1465.12]  like the imperative style of programming so you do var data equals fs.read file um that's actually kind
[1465.12 --> 1471.24]  of so there's there's an implementation of this that is a little bit uh kludgy and dangerous um
[1471.24 --> 1482.06]  in uh uh which uses long jump in in the uh as a compile that on there's also some ways to implement
[1482.06 --> 1492.08]  this using um yield and generators in uh in later versions of v8 newer versions of v8 um you do have
[1492.08 --> 1495.68]  to pass a flag into the binary because they're not enabled by default yet it's a new experimental
[1495.68 --> 1501.74]  feature in ecma scripts uh six but you know it's it's there it's one way you can structure your code
[1501.74 --> 1507.66]  and it's not really a node thing it's just a javascript thing the other a third option for this
[1507.66 --> 1514.64]  is to use something called promises and so the promise promises don't require any additions to the
[1514.64 --> 1520.58]  language what they do is you say instead of instead of receiving a callback this function will
[1520.58 --> 1527.78]  instead return you a promise object that promise object then gives you an api to say once this
[1527.78 --> 1533.40]  promise once this promise resolves do this other thing but you can write your your programs in a
[1533.40 --> 1538.92]  more you know top to bottom kind of manner rather than a left to right kind of manner right the the
[1538.92 --> 1543.96]  promises is kind of just in all of javascript not node that's kind of a growing trend that you see
[1543.96 --> 1549.22]  with a lot of different environments i think yeah yeah exactly and i think that there are um
[1549.22 --> 1557.40]  it's unlikely that anytime soon node will make promises a default thing right in core uh a lot
[1557.40 --> 1562.54]  of people use it in their apps and that's perfectly fine it's basically just another flow control um
[1562.54 --> 1567.30]  mechanism so then that brings me to the fourth possible way to manage this which is something
[1567.30 --> 1573.80]  like the uh the async module and basically what that gives you is just some helper methods to thread
[1573.80 --> 1579.04]  callbacks together so you can say here's like here's 10 functions i want you to run them uh one
[1579.04 --> 1584.76]  after the other and each one receives a callback and so that's kind of the de facto way to go about
[1584.76 --> 1592.04]  uh managing callback taking functions and putting them in par running multiples in parallel excuse me
[1592.04 --> 1597.14]  in parallel or synchronous or you know one after the other or so and so forth again adds nothing to
[1597.14 --> 1602.20]  the language it's just a it's somewhat lighter weight than promises because it doesn't require any kind
[1602.20 --> 1608.22]  of like paradigm shift with how you think about your program right so so streams are something that
[1608.22 --> 1614.96]  that people talk about too what what is what are streams and node and how are they handled streams are um
[1614.96 --> 1625.00]  streams represent a flow of data so you have a thing like a um let's say uh
[1625.00 --> 1630.32]  uh and a network connection like a tcp connection right tcp socket
[1630.32 --> 1636.60]  every time the other guy on the other side of that socket every time they write some data into
[1636.60 --> 1642.72]  their end some data is going to pop out on my end so i need some weight some abstraction to say
[1642.72 --> 1648.86]  look every time there's data available give me a an indication of that and you know have some
[1648.86 --> 1655.20]  mechanism for pulling that data out of that stream every time it it shows up then um on the
[1655.20 --> 1660.30]  writable side a stream represents a place where you're sending a flow of data and then you call an
[1660.30 --> 1667.90]  end method when you're done with it so what this gives you then is another abstraction on top of
[1667.90 --> 1672.64]  those two things where you can take a readable stream and just plug it directly into a writable
[1672.64 --> 1679.34]  stream with a pipe method so you can do my readable dot pipe and then paren's my writable uh and all the
[1679.34 --> 1684.34]  data that comes out will just immediately be sent into this writable stream right so that's particularly
[1684.34 --> 1690.26]  handy if you want to send like this the contents of a file to an http response or vice versa or you know
[1690.26 --> 1697.08]  do things like that some of this stuff might be a little uh i don't know complicated for like a
[1697.08 --> 1702.62]  newcomer so let's say especially hearing in a podcast rather than like reading on a yeah totally
[1702.62 --> 1708.92]  so go go there's plenty there's a archive of a lot of debate on that subject if you have interest in it
[1708.92 --> 1714.70]  on the node mailing list so you can go there for more information um there's also pretty extensive docs on
[1714.70 --> 1721.26]  this now in the uh in the node api docs uh if you look up the the streams api doc for the latest
[1721.26 --> 1727.24]  um stable release there is a pretty good discussion of like what streams are and how to use them
[1727.24 --> 1733.66]  broken into three different sections so this was this is pretty recent um prior to this it was all kind
[1733.66 --> 1739.34]  of a mishmash and i think there was just a lot of confusion and and fud around it so we've broken it
[1739.34 --> 1744.70]  into three different sections so there's um you know streams for a youth for users like you're
[1744.70 --> 1750.96]  consuming a stream here's how to do it then there's streams for people implementing streaming apis
[1750.96 --> 1756.38]  for instance if you are you know creating a new module that's going to like send data somewhere or
[1756.38 --> 1761.22]  do some transform on it or what have you and then there is a third section which is like how it
[1761.22 --> 1765.02]  actually works and the history of it and how it used to work and how it's changed and so on
[1765.02 --> 1770.64]  so most people really only need the first you know third of that document and you can find that
[1770.64 --> 1777.86]  at nodejs.org slash api is that right yep slash stream.html yep so for so i i kind of talked about
[1777.86 --> 1783.60]  it but for a newcomer um well i guess let me preface this by by saying are your target is your target
[1783.60 --> 1788.78]  audience or are your target developers seasoned or you know entry-level developers or people that
[1788.78 --> 1793.30]  are in other environments and frustrated with it or you know who does node target to kind of for
[1793.30 --> 1798.92]  for new developers yes yes all the developers we target all the developers if you're a developer
[1798.92 --> 1804.90]  we are targeting you we want you developing with node um maybe not as your only platform but as
[1804.90 --> 1811.48]  certainly as one of them i mean it's it's kind of nice it's kind of nice to develop in um javascript
[1811.48 --> 1819.00]  is not a very bad language and i think that node hits a pretty good um you know a useful
[1819.00 --> 1825.54]  a useful kind of niche between really low-level systems programming and super high-level like
[1825.54 --> 1835.84]  you know railsy type stuff um the the paradigms are very c-ish and very unixy and um you know i
[1835.84 --> 1842.08]  obviously here so here at joint i mean most of the engineering staff at joint are like super low-level
[1842.08 --> 1849.02]  like kernel hackers and os people um and people who have been doing systems engineering for you
[1849.02 --> 1855.02]  know for years and years and node has really caught on in this crowd i think in large part because
[1855.02 --> 1861.24]  it's very um you know it's very it follows a lot of very standard unix paradigms
[1861.24 --> 1869.64]  yeah people you know there's a reason why i think is node still the most popular repository on github i
[1869.64 --> 1876.96]  believe it is right oh i'm not sure um it's the most popular repository in my list of
[1876.96 --> 1882.96]  tabs that i have open on chrome yeah i know it's it's up there and i remember there was like a day
[1882.96 --> 1888.50]  where it kind of passed uh ruby or sorry rails and that was kind of like a big day for node um you
[1888.50 --> 1892.18]  know i don't you know maybe not specifically for like the node core team but just the community in
[1892.18 --> 1897.80]  general um so but that kind of gets back to my question so for a newcomer you know let's say
[1897.80 --> 1902.88]  somebody that's like new to well let's say somebody that's new to just node like they're they're a
[1902.88 --> 1907.30]  developer they know you know maybe they've worked with java or ruby or something else and they want
[1907.30 --> 1913.56]  to try out node you know with ruby there's try ruby.org there's like all the code schools and uh
[1913.56 --> 1917.98]  treehouse and all those they have a lot of you know tutorials and lessons and how to learn you know
[1917.98 --> 1923.64]  ruby there's for python things like that what is there for node you know for a newcomer to kind of
[1923.64 --> 1930.98]  get started and kind of play around with it um for a newcomer to kind of get started with node i
[1930.98 --> 1937.10]  think i mean i don't know i guess the i guess just kind of download it and install it and start
[1937.10 --> 1942.22]  messing around with some of the examples and and docs and stuff like we don't have as nice an
[1942.22 --> 1949.68]  onboarding system as i would like but um you know and i mean there's nothing like uh like pythonista
[1949.68 --> 1955.16]  for instance with python where you can like where you literally like download an ipad app and install
[1955.16 --> 1962.96]  it and you're like making games in you know 20 minutes like wow i'm super jealous but you know
[1962.96 --> 1968.22]  there's nothing quite like that for node but i think the actual platform itself is seems to be
[1968.22 --> 1973.58]  approachable enough um because we keep getting more people using it i will say that uh if you
[1973.58 --> 1978.70]  don't mind me stepping here for a second on the on the getting started part i had a hard time finding
[1978.70 --> 1984.72]  because i actually wanted to hack on uh i wanted to mess with bauer a couple like i guess four or
[1984.72 --> 1991.86]  five months ago and to get bauer on to my system i had to use npm which required me to kind of get
[1991.86 --> 1995.72]  started with node for lack of better terms you know i needed to have this installer to do that
[1995.72 --> 2002.60]  and i found it very hard to find out how to get it on my system in an easy way and i ended up finding
[2002.60 --> 2010.48]  uh a tutorial from robert bennett on uh installing node with with homebrew on on the mac so that worked
[2010.48 --> 2017.40]  okay but it was still like had to search yeah yeah so on nodejs.org we actually have a big green
[2017.40 --> 2025.40]  install button now yeah which will um detect whether you're on mac or windows or some other os if you're
[2025.40 --> 2029.10]  on some other os it doesn't show a big green install button it just kind of has you download
[2029.10 --> 2033.98]  the source code because whatever you're on linux you got to figure it out you're smart enough not on
[2033.98 --> 2041.62]  those exactly you're you're used to being abused yeah but for uh for windows and and osx we have
[2041.62 --> 2047.48]  pretty straightforward downloaders now that'll kind of put things in the right place so i should undo
[2047.48 --> 2052.70]  what i've done and use that i mean if what you've done is working for you that's fine i think uh
[2052.70 --> 2057.94]  i think homebrew is is you know it seems like people are succeeding that way and and a lot of
[2057.94 --> 2065.64]  people seem to get it relatively in a relatively good state on their machine i mean i don't know
[2065.64 --> 2070.08]  i'm probably not the best person to ask about getting started guys with node because honestly
[2070.08 --> 2073.36]  like i read those things and i just can't see the forest for the trees a lot of the time
[2073.36 --> 2078.02]  um yeah and for me i mean the you know the getting started is like you will just clone the
[2078.02 --> 2084.32]  github and make install like you know it's hard about that yeah right right yeah but i mean we're
[2084.32 --> 2091.06]  seeing really interesting things but actually i mean bauer stuff like uh like uh not just bauer but
[2091.06 --> 2097.54]  what's the other one um grunt actually is is driving a lot of node adoption i've found because
[2097.54 --> 2102.74]  people need to use grunt in order to use some you know contribute to some open source
[2102.74 --> 2110.94]  um uh front-end project and then they end up discovering npm and java and and node and the
[2110.94 --> 2116.58]  process and kind of find oh like oh i can i can write like command line scripts in javascript and i
[2116.58 --> 2120.46]  know javascript like hey isn't this great you know this person who might not have ever considered that
[2120.46 --> 2129.00]  they could do server-side programming yeah so for somebody that that does kind of want to get started
[2129.00 --> 2133.12]  with node what kind of like let's say they're they're you know sitting down they have applications
[2133.12 --> 2136.56]  to build and you know or they have a specific application they want to build and they're
[2136.56 --> 2140.68]  they're making the decision between let's say they they're comfortable with getting started with node
[2140.68 --> 2144.54]  or you know any other environment what kind of applications would you say you know thrive
[2144.54 --> 2150.50]  in node or where would you where would you say node flourishes over you know ruby python php
[2150.50 --> 2162.90]  you know etc i think um node really seems to do best as a uh like middleware api tier um particularly
[2162.90 --> 2170.94]  if you have to talk to multiple different um back-end sources and provide you know a web and or you
[2170.94 --> 2177.48]  know tcp or some other kind of front end for those api sources um another place where node does really
[2177.48 --> 2185.34]  well actually is in uh writing command line tools because of the portability to um to windows and
[2185.34 --> 2189.70]  and unix so i i mean i think that's a big part of the reason why grunt is so successful because
[2189.70 --> 2198.86]  windows developers can actually use it pretty easily uh for writing i mean you know if you're going to
[2198.86 --> 2206.90]  write a relatively low uh you know if you don't have really high uh scaling concerns and you need to
[2206.90 --> 2212.44]  write a crud app like you know what rails is probably really good at that like especially
[2212.44 --> 2217.18]  if you're already familiar with rails especially if you're already good with ruby and and happy using
[2217.18 --> 2223.60]  it then like by all means like it's it's got a lot of really nice uh tools to to make that successful
[2223.60 --> 2228.88]  um for but if you're doing stuff that has a lot of requirements for doing a lot of streaming
[2228.88 --> 2234.22]  type of data um you know if you're very comfortable with javascript if you're comfortable writing
[2234.22 --> 2238.66]  things in javascript then i think you know then then node really starts to make a lot of sense
[2238.66 --> 2246.32]  gotcha so if you're doing you know event-driven non-blocking io in other words right in v8 javascript
[2246.32 --> 2254.32]  yeah i i mean it's also actually so at joint um joint's a huge user i'll talk about a few of the
[2254.32 --> 2263.14]  really big users of node um joint itself they they use node as um basically the the orchestration tier
[2263.14 --> 2271.66]  of their entire data center system so you know everything between um when you sign up for for a uh
[2271.66 --> 2279.02]  for a host on joint all the way through you know all the way down to like the actual operating system
[2279.02 --> 2285.70]  um is is running entirely on node now obviously the operating system as a whole is not entirely
[2285.70 --> 2290.16]  running on node like that's got a lot of stuff that's written in c there's you know zfs and zones
[2290.16 --> 2296.76]  and dtrace and so forth but like you know all of those little kind of orchestration demons and
[2296.76 --> 2302.74]  things that all need to talk to each other um you know this is this is all a big collection of node
[2302.74 --> 2307.78]  programs and and the nice thing about it is it's like you can be writing a little demon and be like
[2307.78 --> 2312.86]  ah god i really wish i had some like easy way to see what this thing is doing like oh i know i'll
[2312.86 --> 2319.16]  just have it spin up an http server because that's easy right like um and so it opens a lot of doors
[2319.16 --> 2323.38]  and kind of having all of these different things all in one place makes you kind of think about
[2323.38 --> 2329.52]  things in a little bit different way um another example is uh voxer is using it has been using it
[2329.52 --> 2335.74]  for a long time actually to run their um uh their routing and their whole system so that you can
[2335.74 --> 2343.16]  so they're basically sending uh json payloads with binary chunks of of sound data of audio data
[2343.16 --> 2349.22]  and a little bit of metadata to know who to send it to and that's i mean that's the the core of
[2349.22 --> 2355.58]  their system so they've got all of these different um proxies and and and demons and stuff taking this
[2355.58 --> 2359.88]  data in and stuffing it in a database and sending it to some other thing that like broadcast it out to
[2359.88 --> 2365.42]  these other servers and you know it's all this this big telephony network um and they've they've
[2365.42 --> 2371.04]  written this thing entirely in node yeah so i so little side note i wonder how exactly how many
[2371.04 --> 2374.96]  callbacks it takes for my softball team to tell me which field we're playing on in boxer
[2374.96 --> 2380.66]  i have no idea it's probably a shocking shocking number i'm sure
[2380.66 --> 2389.90]  yeah and and it it is pretty good for writing websites i i kind of like it um because i like
[2389.90 --> 2394.42]  having a lot of very explicit control over that kind of stuff and i like it just because i'm
[2394.42 --> 2399.64]  obviously extremely familiar with node so you know the first the hammer that i grab when everything
[2399.64 --> 2405.50]  looks like a nail is is node um you know there's there's other things for building websites it's
[2405.50 --> 2411.66]  it's something that we humans have gotten pretty good at doing but um you know i i like node for it
[2411.66 --> 2419.06]  cool so i want to roll back a little bit um the the original the creator of node ryan doll who is he's
[2419.06 --> 2424.84]  i think he's still at joint is that correct that is not correct okay he is not at joint or anywhere
[2424.84 --> 2433.10]  on the internet he's he's basically retired from public life and oh we got a uh another uh why or
[2433.10 --> 2441.12]  yeah he's he seems to be doing well uh for 10 gone no i i don't know if it's a 410 i think it's just um
[2441.12 --> 2443.90]  you know temporarily unavailable it's a right three
[2443.90 --> 2451.44]  the uh the way he put it to me he doesn't like creating permanent things on the internet anymore so he
[2451.44 --> 2456.22]  you know removed his github and his uh twitter and i don't know if he removed his github but he
[2456.22 --> 2462.68]  definitely removed his twitter and and blog and facebook and everything um it's it was why ish but
[2462.68 --> 2470.64]  not completely yeah so uh basically i mean you know i he got kind of tired of working on node
[2470.64 --> 2476.72]  day in and day out for three years yeah and uh you know as as one would i'm sure if you you know
[2476.72 --> 2480.94]  got into this by hacking on new things and always wanting to try out the latest new thing
[2480.94 --> 2490.14]  and suddenly tripped and fell and ended up a success and uh next thing he knew he was doing the same job
[2490.14 --> 2498.58]  for three years and went a little stir crazy yeah so how long so okay so up to speed the transition
[2498.58 --> 2503.04]  from ryan doll to yourself as kind of the maintainer of the project what did that go like
[2503.04 --> 2513.64]  so um yeah so he was kind of uh he was kind of feeling burnt out and over a couple of months um
[2513.64 --> 2520.48]  i took over making the builds every you know couple weeks when we would release a new version
[2520.48 --> 2529.14]  and um gradually more and more took over more you know over about a six month or so period took
[2529.14 --> 2535.36]  over more and more of the duties of of running the project and kind of um keeping things going and
[2535.36 --> 2540.24]  then and he had talked about the other core committers about this about me taking over his role in the
[2540.24 --> 2552.62]  project um and then uh he posted a a message on the mailing list saying he's you know taking off to work on
[2552.62 --> 2559.82]  research projects and that i am the new uh forget how he phrased it lead gatekeeper um of node and
[2559.82 --> 2565.72]  that all feature requests need to you know if you want any new features or have any bugs to complain
[2565.72 --> 2571.72]  to me about them and that i'll be the one saying no to people from now on so how's this transition
[2571.72 --> 2578.10]  been then i guess taking over that space considering his departure maybe it's just from being stir crazy on
[2578.10 --> 2583.72]  the project three years has it been the have you been happy i guess is the way to ask that question
[2583.72 --> 2591.34]  i have been very happy um you know i it's it's extremely rewarding and it's it's extremely
[2591.34 --> 2597.30]  challenging and um running a running a project and and a community i think is um
[2597.30 --> 2605.12]  it's i i feel very very lucky to be able to have found myself in a position where this is my job and
[2605.12 --> 2614.50]  this is what i'm doing um it's a ton of work and it's can certainly be exhausting but um you know i
[2614.50 --> 2621.58]  care a lot about the success of this project and and the people who are uh who are pouring time and
[2621.58 --> 2628.50]  energy into it and um i i think it's also really uh you know it's it's a good group of people like it's
[2628.50 --> 2632.60]  a good um it's a friendly community and i think we've done a pretty good job of trying to kind of keep
[2632.60 --> 2641.02]  some sense of positivity um and not kind of devolve into too much of like you know turf wars or you
[2641.02 --> 2651.40]  know bad exclusionary you know sexist heteronormative ableist you know yeah behavior or whatever um
[2651.40 --> 2655.76]  which is which kind of happens a lot of times in communities i mean you know it doesn't take too
[2655.76 --> 2662.12]  many people to make a community a lot less welcoming to newcomers right how much of your
[2662.12 --> 2666.68]  time now would you say is actually writing you know contributing to the node project itself and
[2666.68 --> 2675.06]  versus community engagement and you know kind of the maintainer role i think um i don't know i mean
[2675.06 --> 2681.76]  it's it's probably about 50 50 uh i i'm certainly a lot better at writing code than i am at being a
[2681.76 --> 2686.80]  community maintainer and i i sort of always feel like i'm i'm feeling my way out on that one um
[2686.80 --> 2694.46]  basically one or two days a week is just completely burned up by meetings uh that's that's actually
[2694.46 --> 2699.32]  what you know what today is that's why i opted to schedule this call on it on a tuesday was because
[2699.32 --> 2708.30]  of uh because this day is gone anyway yeah but uh no i mean it's it's ironic though i think um
[2708.30 --> 2713.74]  you know as a programmer and and as a as a person engaging with community or and with people like
[2713.74 --> 2720.18]  the more the more of your time and the more of yourself that you kind of like keep heaping like
[2720.18 --> 2727.42]  just throwing at this project or throwing out a at a particular um bit of work the less sometimes the
[2727.42 --> 2733.50]  less creative and the less insightful you can be so i i do try to carve out of a large amount of my time
[2733.50 --> 2740.74]  for um you know doing yoga and biking and just kind of like watching cartoons and doing like
[2740.74 --> 2748.08]  completely other random things um you know because that's sort of like that's sort of like what keeps
[2748.08 --> 2753.04]  you sane you know it keeps you much more grounded and i find that i actually am much more productive
[2753.04 --> 2758.98]  writing code when i write less of it um which is yeah like i said i mean it's completely counterintuitive
[2758.98 --> 2764.44]  but it's funny because i you know a few years ago i kind of felt the same way and i started running
[2764.44 --> 2771.40]  every day so you know whereas you would do yoga and biking i run every day and um i heard i think it was
[2771.40 --> 2776.08]  a guy at the i can't remember now what it was called but it was a ruby conference in grapevine texas and he
[2776.08 --> 2781.56]  was talking about like the importance of you know staying fit and you know just being active and for
[2781.56 --> 2786.96]  your happiness and this last week we were traveling and you know we were i was doing some flying and
[2786.96 --> 2791.60]  driving and i and i realized i hadn't run for like a week and i just felt like i was going crazy like
[2791.60 --> 2796.26]  i just felt like i you know sitting at a desk and having this you know working on a computer all day
[2796.26 --> 2800.68]  every day and not really getting the energy out anywhere kind of kind of took me back to where i
[2800.68 --> 2807.86]  felt like i'd gotten you know before i started doing it yeah yeah so i wanted to ask uh how long have
[2807.86 --> 2810.40]  you been the maintainer of the project when did that happen
[2810.40 --> 2821.56]  so when did that happen um was it at the start of 2012 i think if i'm remembering correctly so it's
[2821.56 --> 2827.06]  been about a year and a half now okay so burnout is the thing that we like to kind of talk about and
[2827.06 --> 2832.18]  if we could you know package up how to solve burnout and sell it to everyone we'd be bajillionaires but
[2832.18 --> 2840.08]  uh it took ryan about three years to to burn out and and would you say that i think it took him i
[2840.08 --> 2843.62]  think arguably it took him two and a half years to burn out it took him about six months to recognize
[2843.62 --> 2849.14]  it to actually accept it yeah what uh what are you doing to to kind of prevent that from happening
[2849.14 --> 2854.44]  obviously you said you know the the yoga and and uh cycling but what else would you say is a you
[2854.44 --> 2858.68]  know you're you're kind of doing to to help prevent you know that burnout from coming upon yourself
[2858.68 --> 2869.30]  i think um you know i think also a big part of it is to to try and like work on things that aren't
[2869.30 --> 2877.40]  your main job but are maybe more of you know but are still in line with your craft so you know node
[2877.40 --> 2882.62]  core is not the only thing i'm writing code for um and npm is not the only thing i'm writing code for
[2882.62 --> 2889.72]  and i think you know just other than that like just being more than a programmer i think is a is a
[2889.72 --> 2896.02]  really important thing you know we we start to it's very easy and typical for us to kind of identify
[2896.02 --> 2902.48]  ourselves with our job or with whatever it is we do to make money and kind of forget that we're also
[2902.48 --> 2906.38]  supposed to be whole people you know and so um
[2906.38 --> 2913.06]  obviously you know if you spend a lot of your time on your craft or your job like a lot of your
[2913.06 --> 2916.96]  friends are going to be friends you've met through work or through you know open source projects or
[2916.96 --> 2923.04]  what have you and certainly most of my best friends are all node people at this point in my life but um
[2923.04 --> 2930.66]  you know i i try to i try to have a little bit of a sense of a community outside of work or outside of
[2930.66 --> 2937.64]  just you know node um and i think that you know doing yoga regularly has made a huge impact on my
[2937.64 --> 2944.40]  life and my health but also just you know hacking on things occasionally that are not you know as
[2944.40 --> 2952.22]  obviously uh node-ish like even though even if they it is a node program it's like if i i have a lot of
[2952.22 --> 2956.50]  like random little node modules that i've written that people like and they use and it's it's kind of
[2956.50 --> 2960.90]  nice every once in a while to spend a day just kind of like fixing bugs in those or like you know
[2960.90 --> 2966.04]  accepting pull requests or whatever just because like like that's that's what i'm actually passionate
[2966.04 --> 2970.28]  about that's how i got into this and so it's important to not forget you know not get too caught
[2970.28 --> 2974.58]  up in where you're at now that you forget why it was you started out wanting to do this in the first
[2974.58 --> 2982.48]  place you might have said it i guess in there in a in a winded way but um if you were talking to
[2982.48 --> 2986.84]  people which might quite quite possibly be the the thing happening here but if you're talking to a
[2986.84 --> 2993.24]  bunch of people that were maintaining i guess semi or you know highly adopted uh open source projects
[2993.24 --> 3001.20]  what advice would you give them i guess to not um over over i guess commit themselves and get
[3001.20 --> 3008.02]  themselves into a position where they do burn out um so a good first step is to trick a company into
[3008.02 --> 3013.80]  paying you to do it there you go because no and i mean i'm i'm really really serious like
[3013.80 --> 3020.02]  if i if i had a job doing something other than node and i was also doing all this stuff like oh my
[3020.02 --> 3026.24]  goodness forget about it like i would have no life um you know if you can't if you can't kind of make it
[3026.24 --> 3033.08]  your job then you can't expect to keep devoting a fair amount of your waking hours on it and and
[3033.08 --> 3039.00]  continue to feel rewarded by that um and i see this happen a lot you know where people have a job
[3039.00 --> 3042.72]  with some random company and they also have some open source thing and their company says well
[3042.72 --> 3049.88]  we'll let you work on this like in your free time uh or you know we'll give you like you know 20
[3049.88 --> 3059.22]  time which is really 120 time and um you know and that's just really not sustainable so if you have a
[3059.22 --> 3063.52]  at some point you know with the success of an open source with an open source project that's
[3063.52 --> 3068.70]  successful you have to either accept that it's never going to be much more than a hobby
[3068.70 --> 3076.94]  and that that's going to you know necessarily limit how far the project can go or and that ends in some
[3076.94 --> 3080.74]  in the cases of some projects like that's perfectly fine i have some projects that are just purely
[3080.74 --> 3085.40]  like hobbies and labors of love and i i don't get as much time to work on them as i'd like but that's
[3085.40 --> 3092.06]  just how the cookie crumbles uh or find some way to make that thing be your job so that you know you
[3092.06 --> 3097.42]  can actually have time and energy to uh to devote to it and not have to be stealing it from somewhere
[3097.42 --> 3103.32]  else are you a fan of potentially i guess in some cases we've had people on the show injure where
[3103.32 --> 3108.72]  they've turned their project into some sort of commercial way of of making money i guess if you
[3108.72 --> 3113.38]  can't trick a company like no or uh joined into paying you full-time to do your your thing like
[3113.38 --> 3118.68]  you're doing you know have you would you have considered i guess maybe i guess you didn't
[3118.68 --> 3124.30]  create node but i guess would you advise to find a way to monetize it in some sort of way that that
[3124.30 --> 3129.20]  makes sense for the community yes i mean if if you can do that in such a way that it actually
[3129.20 --> 3135.18]  doesn't destroy the goodwill that you've created um and this is i mean there's another huge pitfall
[3135.18 --> 3142.38]  right if you a lot of a lot of paths to monetization and um you know just to pick one example of of um
[3142.38 --> 3149.14]  of my sequel uh if you try to go kind of the the dual licensing route where you have this
[3149.14 --> 3158.02]  you know crippled for commercial use license a gpl license and then you have a um you know
[3158.02 --> 3164.68]  proprietary but not crippled for corporate use license uh that's one way that you can monetize
[3164.68 --> 3169.48]  because anybody in the community can use the gpl one but if you need to use it for you know closed
[3169.48 --> 3176.24]  source stuff or you know proprietary stuff you have to purchase this other license uh in the long run
[3176.24 --> 3181.24]  i think that that obviously doesn't really work as well because what what can very easily end up
[3181.24 --> 3185.12]  happening is you get purchased by a company like oracle that says you know what actually we don't
[3185.12 --> 3189.38]  want to do this gpl stupid thing anymore so we're just going to do the proprietary one
[3189.38 --> 3195.54]  and now your users are over a barrel you know another way to go about this is with like you
[3195.54 --> 3202.28]  know heavy-handed marketing type stuff and and um nobody really likes nobody likes being sold
[3202.28 --> 3205.06]  something they don't want right so um
[3205.06 --> 3214.38]  if if there's some way to go about monetizing your your project perhaps by uh by providing some
[3214.38 --> 3222.18]  additional service or you know whatever like you know services or products around it
[3222.18 --> 3225.04]  um that can often be very very successful
[3225.04 --> 3232.18]  i wanted to ask you you know uh kind of running short on time but one of the things i wanted to
[3232.18 --> 3238.22]  kind of get to is node has some pretty cool branding and i just wanted to ask who controls the brand of
[3238.22 --> 3247.28]  node oh so uh um when he i don't know exactly when it was but at some point ryan sold the trademark
[3247.28 --> 3256.84]  to the uh the node mark and and name to joint and so joint actually owns the ip of node um they own
[3256.84 --> 3265.02]  the copyright on the code and the the trademark and uh word mark of node.js so the uh the logo and
[3265.02 --> 3270.50]  stuff that was all commissioned by uh by joint gotcha and basically all the all the branding
[3270.50 --> 3276.08]  and everything there that's uh that's joint's thing there was a uh there was a logo before this
[3276.08 --> 3281.84]  one that was contributed by the community with the little cloud and the like bubbly letters but um
[3281.84 --> 3288.62]  it didn't work out so well for joint because there had it had i guess rather dubious um intellectual
[3288.62 --> 3294.86]  property ownership we weren't sure like who actually owned it or like you know what the rights
[3294.86 --> 3299.30]  were or under what conditions it was given to the node project and it was ryan at the time and not
[3299.30 --> 3303.22]  joint so it was tricky to kind of work that all out and so they just kind of went back to the drawing
[3303.22 --> 3309.46]  board create a brand new logo which was like hated at the time let me tell you like people people could
[3309.46 --> 3314.66]  not i i am not joking people threatened to like fork the project and rename it just so that they
[3314.66 --> 3320.00]  wouldn't have to look at that logo you know which is a total like it's a total like well if the if
[3320.00 --> 3324.34]  the republicans get elected i'm moving to canada like no you're not gonna do that you're not gonna uproot
[3324.34 --> 3330.78]  your family and move to another country because of who got elected come on right uh so yeah and so
[3330.78 --> 3334.76]  some time passed and now it's like now everybody loves the logo now everybody wants to put everything
[3334.76 --> 3340.18]  in a hexagon and hexagons are great and it's it's kind of funny that's how that's worked out
[3340.18 --> 3345.98]  cool so we'd definitely uh i feel like we could talk about this forever kind of happens with most of
[3345.98 --> 3351.30]  the things we talk about because well we bring interesting topics on the show mostly but for those
[3351.30 --> 3355.98]  you that are kind of sorry go ahead i said it seems that way from your from your past topics i'm i'm
[3355.98 --> 3361.14]  very very honored to be here oh no we've had definitely had demand to have you guys on here so
[3361.14 --> 3367.26]  it goes both ways doors are being beaten down so to those of you that are kind of new to the show we
[3367.26 --> 3372.82]  ask our our guests uh kind of a set of three questions at the end um and the first question
[3372.82 --> 3378.28]  is for kind of a call to arms so you know for the community to get involved and what you would
[3378.28 --> 3385.18]  like to see them kind of contribute or you know work on i think um i think the main thing that we
[3385.18 --> 3391.58]  need right now is just more people using node advocating for it and helping new users in the uh
[3391.58 --> 3399.64]  in the various channels like in the irc channels and in uh github and um and the mailing list uh
[3399.64 --> 3404.70]  you know we are we're growing fast and if you look at all the numbers i mean it's like we're still
[3404.70 --> 3412.28]  hockey sticking but we're still quite a small community and um you know it really the more
[3412.28 --> 3417.42]  positivity that everybody brings to it the more successful newcomers will be and and the more
[3417.42 --> 3423.58]  it'll keep kind of compounding this this growing system right maybe something like a try node.org or
[3423.58 --> 3428.82]  something yeah yeah sure i mean that would be that would be lovely i think there's something like
[3428.82 --> 3434.32]  that there's a learn you a node uh i i don't remember uh like i think it's kind of like a play
[3434.32 --> 3440.58]  on the learn you a haskell for great good yep but uh yeah i mean there's some there's some resources
[3440.58 --> 3449.22]  out there i think just uh continuing to um help new people be successful and uh guide them towards
[3449.22 --> 3455.06]  success is is extremely useful gotcha if you are doing what you're doing now um whether it be
[3455.06 --> 3460.90]  a different environment programming language or you know just personally something different what
[3460.90 --> 3466.42]  would you like to do i would really like to take and this is this is probably going to happen
[3466.42 --> 3471.38]  eventually but i i would really like to take a good couple years off from from software in general
[3471.38 --> 3476.52]  um and just kind of see what happens i i did a few months and npm happened and that has been
[3476.52 --> 3484.92]  extremely uh beneficial for myself and i think a lot of other people and uh yeah i don't know i i there's
[3484.92 --> 3489.48]  this uh co-op bakery near my house that i every time i go in there i fantasize about just like
[3489.48 --> 3497.30]  being like ah screw technology i'm just gonna like i'm just gonna like do yoga and bake and
[3497.30 --> 3503.20]  sell pizza and that's gonna be my whole life it just seems so simple it's funny because i think
[3503.20 --> 3508.10]  that the common you know i don't know why but for some reason like the trendy things that that you hear
[3508.10 --> 3514.66]  a lot about are some in the in the you know developer world are woodworking uh you know cooking
[3514.66 --> 3519.24]  or baking of some sort and music like those are kind of the three things that people seem to to
[3519.24 --> 3525.62]  gravitate towards and i think it just kind of speaks to uh creating something physical with your hands
[3525.62 --> 3531.82]  you know what i mean yeah yeah i mean there's a real um when you when you make like a perfect pastry i mean
[3531.82 --> 3538.02]  that is like so so satisfying um and it's it's difficult you know you can't do it at home because
[3538.02 --> 3543.44]  you need like the chilled table and and massive amounts i mean you need in order to make a really
[3543.44 --> 3550.14]  good croissant you have to make a hundred of them yeah so kind of opportunity to give you a shout out to
[3550.14 --> 3556.22]  a hero of yours um we call it a programmer hero who's somebody that's kind of impacted you in your life
[3556.22 --> 3562.76]  um i you know i you told me that you were going to ask me this question and i all i could think of
[3562.76 --> 3571.80]  is a lot of people who i would want to uh to shout out to but i i think um if i had to pick one i mean
[3571.80 --> 3579.42]  honestly i'd have to say ryan uh and it might sound kind of cheesy but uh you know like i said is um
[3579.42 --> 3587.92]  his aesthetic with node really um called out to me and i think that he has a really good um
[3587.92 --> 3594.02]  really good view of what's important when it comes to writing software that it needs to be fast it
[3594.02 --> 3599.66]  needs to delight the user and it just needs to you know work really well and um as much as i find
[3599.66 --> 3605.60]  myself cursing him because i've inherited a bunch of his code and frequently find bugs in it um
[3605.60 --> 3613.68]  you know i i think that in a in any in any platform or any like significantly sized programming project
[3613.68 --> 3619.52]  you see a lot of the um a lot of the aesthetic of the original creator in in everything it kind of
[3619.52 --> 3627.02]  permeates the entire thing and i think um you know npm is very much my aesthetic and and node still is
[3627.02 --> 3634.36]  very much ryan's i think that a lot of that has uh has been maintained and so i think um it's it's
[3634.36 --> 3640.16]  definitely been an inspiration to keep working on node i really like it a lot awesome well yeah like
[3640.16 --> 3644.96]  i said i you know we could talk about this forever but we're coming up on that that uh hour time limit
[3644.96 --> 3649.12]  so i just wanted to yeah i just wanted to say thanks so much for coming on the show man i mean
[3649.12 --> 3655.10]  hearing about you know i don't know just node and and the community that's coming up under it is it's
[3655.10 --> 3659.56]  really kind of exciting so i just wanted to say thanks for uh you know all the hard work and
[3659.56 --> 3664.52]  and the work you put into yourself to to prevent burnout so you can keep this train going man
[3664.52 --> 3668.66]  all right thanks real quick before we go i want to mention that we are
[3668.66 --> 3674.76]  member supported so you can head to the changelog.com slash membership to show some love um if you'd like
[3674.76 --> 3678.94]  to get if you would like to get updates every thursday in your inbox from the changelog you can
[3678.94 --> 3684.38]  sign up for our newsletter at the changelog.com slash weekly that's right
[3684.38 --> 3692.54]  um and now you can hack in style with your very own changelog t-shirt you can get yours at the
[3692.54 --> 3699.38]  changelog.com slash store if you're a member you get 20 off uh once again you can check out pete keen's
[3699.38 --> 3706.96]  ebook at pete keen.net slash mastering dash modern dash payments that's it for today's show how do you
[3706.96 --> 3715.60]  spell pete keen pete keen it's p-e-t-e-k-e-e-n dot net it's a lot of e's pete keen that's what i would
[3715.60 --> 3721.52]  have guessed yeah so that's it for today's show thanks again to isaac schluter for joining us
[3721.52 --> 3726.24]  and until next week guys let's say goodbye later bye
[3726.24 --> 3743.58]  you
[3743.58 --> 3744.58]  you
[3744.58 --> 3746.44]  you
[3746.44 --> 3750.92]  you
[3750.92 --> 3780.90]  Thank you.
