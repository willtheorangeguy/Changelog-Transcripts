[0.00 --> 14.70]  welcome back everyone this is the changelog where our member supported blog podcast and
[14.70 --> 20.24]  weekly email come with fresh and what's new and open source check out the blog at the changelog.com
[20.24 --> 27.04]  our past shows at five by five dot tv slash changelog and you're listening to episode 124
[27.04 --> 33.16]  jared and i talked to tim caswell about getting started in open source exploring new frontiers
[33.16 --> 38.78]  and his project t edit a git based development environment today's show is sponsored by
[38.78 --> 44.54]  digital ocean top tile and snap ci we'll talk to you a bit more about top tile and snap ci later in
[44.54 --> 50.14]  the show but our friends at digital ocean are a simple cloud hosting provider built for developers
[50.14 --> 57.02]  in just 55 seconds you can join over 150 000 developers who deploy to digital ocean's ssd
[57.02 --> 62.30]  cloud digital ocean offers a fantastic user experience handcrafted by developers
[62.30 --> 69.92]  enjoy the ease of use and speed of an ssd only cloud create droplets manage your dns build a new
[69.92 --> 74.76]  server from a snapshot save a ton of time installing rails docker git lab and more with one click
[74.76 --> 80.68]  installs you can even scale your infrastructure with the intuitive api sign up today and use the
[80.68 --> 86.98]  code changelog july to get a ten dollar credit when you sign up head to digitalocean.com to get started
[86.98 --> 88.70]  and now on to the show
[88.70 --> 97.96]  we're joined today with uh with tim caswell also have the managing editor my sidekick in crime
[97.96 --> 107.22]  jared santo on the call too so tim and jared say hello hey hello so tim you are uh you're no stranger
[107.22 --> 111.84]  to the changelog you used to be uh a contributor to the changelog back in the day when we're still on
[111.84 --> 117.26]  tumblr and as a different changelog probably but still the same mission but uh you've been on the
[117.26 --> 123.42]  show before uh you started uh how to node and several other things you're prolific and open
[123.42 --> 128.64]  source you speak at many conferences so you're not a stranger to the world but for those who may be
[128.64 --> 134.14]  come to this podcast brand new that don't know who you are can you kind of tee up whom tim caswell is
[134.14 --> 143.46]  okay so i i guess the best way to describe me is i like to invent things i love open source and i love
[143.46 --> 150.58]  enabling other programmers the a quick background is i programmed in commodores and q basic for a long
[150.58 --> 156.38]  time without internet without help and i was blocked by limitations of the platform nowadays we have
[156.38 --> 161.18]  incredible amounts of technology and ability and the main thing blocking people is just they think
[161.18 --> 166.52]  things aren't possible so i basically spend every free moment i have finding something that is
[166.52 --> 172.54]  impossible and making it possible so i i author a lot of libraries a lot of infrastructure code
[172.54 --> 178.72]  and a lot of educational content so pretty much anything related to that i've i've worked a ton with
[178.72 --> 186.18]  the node.js project since the very beginning in 2009 um i've worked on web os i worked at cloud 9 ide
[186.18 --> 192.82]  of course we're going to talk about my recent work on the show i've i mean basically i've done web development
[192.82 --> 198.62]  since there was a web and i like enabling people what do you just i guess pausing on that for a second
[198.62 --> 202.80]  considering that you've been developing for the web since there has been a web what do you think
[202.80 --> 208.48]  um what kind of i guess quick advice would you give about open source to some of the newer people
[208.48 --> 212.86]  that are coming to open source let's say in the last five to six years that's that's still kind of
[212.86 --> 218.24]  older but new in comparison to your time frame what what do you think has changed i guess to the
[218.24 --> 225.48]  degree of access to information so yeah i mean first of all there was the internet which made a world of
[225.48 --> 232.10]  difference and then for a long time it was central systems like w3 schools was actually where i learned
[232.10 --> 240.16]  a lot of web tech and as much as we make fun of them it was the content i had and so it worked but
[240.16 --> 248.82]  nowadays we have all sorts of blogs and podcasts and videos and we have better documentation sites
[248.82 --> 252.58]  microsoft has a good one mozilla has a good one there's lots of stuff out there
[252.58 --> 256.84]  i mean you can learn from anywhere from individuals to large companies and
[256.84 --> 263.00]  there's just a ton of stuff as far as learning goes yeah now as far as the community involvement
[263.00 --> 269.42]  that's where it really gets interesting what i what i tell people is i'm just a guy from a small
[269.42 --> 277.00]  town in texas i was nobody until i started writing a blog and once i started writing a blog and people
[277.00 --> 280.46]  found out what i was writing was interesting suddenly i started getting these job offers i
[280.46 --> 286.92]  ended up in california working for hp and and all sorts of things happened anybody can be successful
[286.92 --> 291.38]  in web development if they have passion and if they're willing to volunteer a lot of free time
[291.38 --> 298.66]  into helping open source it pays it pays back hugely i'd like to is and help us navigate that
[298.66 --> 306.00]  conversation because the you know i guess the word free can scare some people but open source is maybe
[306.00 --> 311.84]  an easy way to say free um and make it cool i guess at least today like open source is becoming more
[311.84 --> 317.38]  and more cool uh to be a part of and obviously it has its own gains and benefits which you can definitely
[317.38 --> 323.52]  allude to but um you know it can be a scary word to say free so open source time definitely giving
[323.52 --> 328.90]  back to the community plus a lot of what people are jumping into these days are frameworks or platforms
[328.90 --> 334.92]  that have been you know getting the tires kicked for years by the community and and it's freely
[334.92 --> 340.54]  accessible to them so why not give back right right yeah i mean some people like to work on frameworks
[340.54 --> 345.50]  some people are more like me and just want to make things from scratch i mean there there's a place
[345.50 --> 350.86]  for all types of people in open source communities at which point did you feel like you had like
[350.86 --> 355.96]  quality content to give back because i think a lot of the the lack of confidence for people just
[355.96 --> 360.36]  getting started is i have a lot to learn maybe it's a little bit of the imposter syndrome like what
[360.36 --> 367.68]  could my blog possibly provide to the community that's of value did you have a certain point where
[367.68 --> 371.86]  you're like you just hit a confidence bump and you're like all right i'm just gonna start writing
[371.86 --> 377.66]  online and willing to put yourself out there or you know did you do it too late too early what's
[377.66 --> 385.04]  what's advice for people getting getting to that point um i think i'm i'm not normal in that regard
[385.04 --> 391.16]  i i mean i started out programming when i was i don't know seven and so by the time i graduated high
[391.16 --> 396.10]  school i'd already tried and failed at a web startup and i i was pretty i was pretty confident in my
[396.10 --> 401.48]  abilities probably too confident i look back at that code and i'm like oh my gosh did i actually think
[401.86 --> 410.50]  code so i didn't have that problem i thought i was really good okay and now as far as the the
[410.50 --> 417.46]  social aspect i i mean i have mild asperger's and when i was in high school like i would literally be
[417.46 --> 421.04]  the kid who runs to the front of the school line with my long sleeve winter coat and shorts
[421.04 --> 425.58]  eat my lunch and then run to the library and read books about building catapults like that was me
[425.58 --> 432.72]  and then somewhere in there i i changed from that to i joined a sports team got good at swim
[432.72 --> 438.50]  and then what really helped is i went on a mission for my church where you spend all day going door to
[438.50 --> 442.72]  door asking people questions about their life and religion now if that won't break you out of your
[442.72 --> 449.34]  bubble i don't know what will yeah so i mean i don't know so at that point right and your thoughts
[449.34 --> 455.94]  online was nothing yeah yeah in context i mean i i still get a little stage fright my my first
[455.94 --> 461.12]  conference talk was in this movie theater in stokholm sweden and i just remember being on stage with
[461.12 --> 465.38]  spotlights in this room of hundreds of people and i can't see them and it was a little nerve-wracking
[465.38 --> 474.06]  wow but what what helped me a lot actually was meeting with the dallas rb user group and doing lightning
[474.06 --> 480.36]  talks and just starting there like that that did wonders i've been to that uh that group once or
[480.36 --> 487.22]  twice we uh i work at a non-profit called pure charity is my very passionate day job and every
[487.22 --> 491.98]  once in a while we'd be in dallas hanging out we'd be there with karthik and win and jesse
[491.98 --> 499.02]  uh whom are probably names you know that go to dallas rb so that's a good meetup too it is they do really
[499.02 --> 503.72]  well and yeah i mean that helped me that helped ease me in because there's a big step between
[503.72 --> 508.08]  i'm giving a lightning talk to 10 guys i know and i'm on a stage with hundreds of people in a foreign
[508.08 --> 516.52]  country so i couldn't imagine that uh stage when i so you know a little confession on my side i i would
[516.52 --> 522.04]  probably not be very happy at all being in front of that many people with stage lights on me i would
[522.04 --> 528.40]  probably just rather be in the crowd uh as odd as it might seem running the podcast that's like yeah
[528.40 --> 532.32]  it's it's easier to be behind the mic in the seclusion of my comfortable office
[532.32 --> 537.64]  than in front of hundreds and hundreds of people it's just not my place you can you can always edit
[537.64 --> 543.72]  it too so yes yeah let's to some degree we try to as best we can we try to put this one down from
[543.72 --> 550.10]  live to tape as as they say in recording but nice so i was gonna say i was doing a lot a lot of
[550.10 --> 554.34]  javascript nowadays could you take us through your language progression through the years just
[554.34 --> 560.32]  um sure yeah i don't want to spend too much time on it but basically i did basic for a long time
[560.32 --> 567.24]  a long long time i did like i said i started on commodore 64 basic which is awesome because that
[567.24 --> 570.42]  thing had no memory management at all you could just poke random spots of memory and things would
[570.42 --> 577.56]  happen and then and then i got a dos computer i had this this lovely little 386 with 16 megahertz
[577.56 --> 584.08]  and 16 megs of ram and i programmed on that thing for about 10 years just that and the q base agreed
[584.08 --> 592.32]  me was my entire world so like age 7 to 17 ish yeah and then the internet came out yeah exactly
[592.32 --> 597.72]  and that changed everything i think it's important to mention too just um just from a
[597.72 --> 603.58]  a passionate standpoint i guess maybe some inspiration or some encouragement is that
[603.58 --> 610.48]  you uh attacked this passion for programming when there was no information so you had no choice
[610.48 --> 615.62]  but to hit the brick walls and hit the hurdles and find ways yourself to get over them we live in a
[615.62 --> 623.20]  world now where if you hit a hurdle you google it you likely land on stack overflow um to some degree
[623.20 --> 628.82]  maybe somebody's blog or a doc somewhere maybe there's a lot of information accessible to people to get
[628.82 --> 635.48]  over those hurdles so it's building that confidence i think uh is a lot harder today because you're
[635.48 --> 641.64]  always second guessing yourself and maybe to some degree could you quickly touch on maybe that for
[641.64 --> 652.04]  you like gaining confidence on your own okay um i think so there are always unsolved problems i i tend
[652.04 --> 657.78]  to do things that haven't been done before because that's what interests me and i hit a lot of roadblocks
[657.78 --> 664.16]  even in today's world i will be for example today i was trying to figure out how to store binary data
[664.16 --> 671.16]  in safari and a few people have tried this the the lawn chair and pouch tb people have worked on this
[671.16 --> 677.66]  like yeah you can't do that you got a base 64 encoded and use web sql and crazy stuff or but sometimes
[677.66 --> 682.32]  i'm on i'm doing things like a chrome packaged app and i'm testing these apis that no one has really
[682.32 --> 689.16]  used before or the hers used much or the github rest api because i can't do real git protocol to
[689.16 --> 695.04]  github and i find bugs everywhere i find bugs in chrome i find bugs in github and there's nothing
[695.04 --> 700.96]  on stack overflow about it because no one's really tried this yet so there's still plenty of frontier
[700.96 --> 706.24]  out there you just have to do things that haven't been done before so i would imagine you're probably on
[706.24 --> 712.62]  the uh the happy but yet sad list oh another support request from tim oh he found he found
[712.62 --> 720.54]  another bug gosh you know i have no idea so since you're an inventor and you like to hit the unknown
[720.54 --> 726.60]  it probably tees up the what i think is the meat of the conversation so um just to quickly touch on
[726.60 --> 733.12]  js git git browser t edit or some might call it teddit which was me prior to listening to your super
[733.12 --> 738.88]  awesome youtube demo of that which blew my mind so i mean how what's the best way to tee up what
[738.88 --> 744.24]  you've what you're doing now with t edit and the kickstarter you did for js git and the like you said
[744.24 --> 749.24]  the infrastructure tools you need to actually pull this project off right i'd like to start with the
[749.24 --> 754.56]  goal and the goal is a very ambitious but but simple goal i want to make programming accessible
[754.56 --> 762.94]  and what i mean by that is we have all these devices in the world that that kids and teenagers
[762.94 --> 768.60]  have access to that are consumption devices we have ipads and android tablets and chromebooks and who
[768.60 --> 773.78]  knows what else maybe you're on a school computer or a library computer or something and it's a
[773.78 --> 781.08]  lockdown environment but they all have javascript they all have a web platform all of them and so my
[781.08 --> 788.00]  goal is to build a full professional developer environment with everything with dependency management
[788.00 --> 793.18]  with build systems with git check-in checkout clone merge all of that to work in this restricted
[793.18 --> 798.84]  environment and i want to do that so that more people can get into programming without having to
[798.84 --> 806.94]  go out and buy a macbook pro or a windows pc or something so that's the goal now with that goal
[806.94 --> 811.46]  there's a whole lot of sub parts i am invented a new language i'm implementing git in javascript i'm making
[811.46 --> 819.64]  a prototype of this developer environment and so that's what all these projects are the one of the
[819.64 --> 825.14]  biggest technical ones was some sort of version control and interacting with the outside world
[825.14 --> 832.96]  and nowadays by far the most popular version control system for open source is git and so i've been
[832.96 --> 838.92]  working on implementing git in javascript because then i can use it anywhere and so yeah well that brings
[838.92 --> 844.64]  us to the i guess the first hurdle you hit was you couldn't do t edit unless you had js git can you
[844.64 --> 850.64]  talk about i guess the exploration the inventor side of you to to know i mean there's obviously a lot
[850.64 --> 855.74]  of wisdom and discernment in your choices too i mean you can see that given your path uh you crowdfunded
[855.74 --> 863.14]  js git twice um so maybe take us back to you know you said you have a goal how did you begin to think
[863.14 --> 866.92]  about that goal and and figure out what you needed to get in place to actually meet it
[866.92 --> 875.10]  well the way you eat an elephant is one bite at a time and it's very easy to get overwhelmed when
[875.10 --> 880.22]  you have large goals like this and so i figured what is a large substantial thing that i need for
[880.22 --> 887.38]  this that just needs to get done and and i decided over a year about a little over a year ago that i
[887.38 --> 893.88]  need to get and if i had git that would enable so many things and so i tried working on my free time
[893.88 --> 898.68]  didn't make any progress i looked for existing code and there was nothing that had what i needed
[898.68 --> 903.30]  i mean there there were several attempts i'm not the first person to try getting javascript there
[903.30 --> 909.54]  were many many attempts but nothing nothing had what i wanted and so one day i just came to the
[909.54 --> 915.04]  conclusion that i have to do this full time and i have to find a way to fund that and kickstarter was
[915.04 --> 918.78]  very was a little new and still pretty exciting back then so i thought i'd give it a try
[918.78 --> 922.12]  and that's that's where that started
[922.12 --> 930.62]  so there were two kickstarters for jskit there was a kick so there was a kickstarter and i didn't ask
[930.62 --> 937.06]  for near enough money because i miss i misunderstood how it works i want to ask you about that goal
[937.06 --> 941.68]  because i've heard some kind of behind the scene horror stories from some people like i didn't ask for
[941.68 --> 948.74]  enough or yeah so so i mean obviously implementing git in javascript is with my skill set roughly
[948.74 --> 956.92]  a year full-time work i mean it's not easy at all and i asked for what i asked for 12 000
[956.92 --> 962.36]  that's not a year of salary i have three kids in a house i mean that's not going to work right
[962.36 --> 969.38]  so what what i did was i calculated okay i have these consulting projects and if i cancel them then
[969.38 --> 974.22]  it'll take me a month or two to get new consulting things if the kickstarter doesn't work out or whatever
[974.22 --> 978.08]  and so in kickstarter they say what's your minimum what's the least you're willing to accept
[978.08 --> 983.92]  to make it worth your time and i said well i'll do 12 000 that'll give me enough that i can live
[983.92 --> 989.48]  on a reduced budget for a few months and that makes it worth it to fire my clients
[989.48 --> 994.98]  and so i put that as my minimum now here's the problem everyone who was funding it thought that
[994.98 --> 1001.46]  was all i needed and so it hit the minimum overnight like overnight it hit it was because
[1001.46 --> 1005.08]  it was very exciting people love the idea but as soon as i hit that it just crawled to a halt
[1005.08 --> 1010.82]  and i set stretch goals i explained to people no that's the minimum if you want all these things
[1010.82 --> 1017.24]  implemented i need a lot more and it didn't work so i worked on that i stretched it for as many months
[1017.24 --> 1021.56]  as i could until it was endangering my family and then bounty source came to me and says hey we're
[1021.56 --> 1027.28]  like kickstarter but specifically for open source projects we will help you and they did they they
[1027.28 --> 1032.30]  went out and helped find funding from corporations they handled all the stickers and t-shirts and everything
[1032.30 --> 1037.10]  wow they just charge a fee for the service which i thought was well worth my time because when i was
[1037.10 --> 1042.54]  doing the kickstarter i spent an entire month and a half full-time fundraising and that was half the
[1042.54 --> 1050.22]  money because i barely hit i barely got enough so that was almost a waste of time so the js get one
[1050.22 --> 1059.30]  in in bounty source raised 34 000 just a little over 34 000 of your 30 000 goal that's that's neat i i knew
[1059.30 --> 1064.82]  about bounty source obviously we've we've um i think we've had uh michael peace on the show before
[1064.82 --> 1070.22]  he had an rvm fundraiser there i'm not really sure you term it uh bounty source there i guess
[1070.22 --> 1076.26]  because you would use the brand name of the platform like a kickstarter i don't know sure um
[1076.26 --> 1081.78]  and then you got your 12 000 goal that you that you even over exceeded to you had four or five backers
[1081.78 --> 1086.98]  on on kickstarter which uh looking at the time frames trying to figure out what the time frames were
[1086.98 --> 1092.34]  between the two was it about five months between or a few months between kickstarter and bounty source
[1092.34 --> 1099.30]  something like that that sounds right so i mean you got twenty thousand dollars so what happened when
[1099.30 --> 1104.50]  you got when you first get your first crowdfunding from kickstarter did you you fired your clients and
[1104.50 --> 1109.94]  and went to work for two months and then what'd you do yeah i worked and spent most of the months
[1109.94 --> 1114.82]  just trying to solve the cross-platform issue which was the first thing because the javascript
[1114.82 --> 1120.42]  module ecosystem is terribly fragmented and the goal of js git was to have this platform that runs
[1120.42 --> 1126.10]  anywhere so i had to run on chrome app platform on the web platform on the firefox app platform on
[1126.10 --> 1130.26]  the windows app platform on cordova on pretty much any javascript platform you can think of
[1131.30 --> 1136.74]  and so i spent the first several months mostly figuring that out i mean i did some get specific
[1136.74 --> 1140.58]  code here and there and a lot of it was finding out what existed and how i could use it
[1140.58 --> 1148.18]  but i'm going to admit a lot of that time was was spent trying to find a flexible way to work with
[1148.18 --> 1153.38]  all these systems what's the i guess what's the biggest hurdle between the two between all of them
[1153.38 --> 1156.74]  just uh the fact that they're just different they make different choices or how they store
[1157.38 --> 1161.78]  data how they deal with databases i mean that kind of stuff you can abstract away
[1163.30 --> 1169.54]  the the trick was how was the best way to abstract that how what kind of dependency injection do i want
[1169.54 --> 1173.78]  to use what kind of module system do i want to invent because i can't use anything existing
[1174.82 --> 1180.02]  a lot of people told me to just use browserify which i understand if you're on a desktop platform
[1180.02 --> 1184.58]  that's a great choice but i'm specifically targeting platforms that don't have a command
[1184.58 --> 1190.74]  line that don't have node right and so i want to be able to develop on these machines not just consume
[1190.74 --> 1195.38]  on these machines that was the entire point and so i can't depend on a tool chains that need a desktop
[1195.38 --> 1202.26]  machine so basically there was nothing existing i could use yeah it's like all these you might be
[1202.26 --> 1206.74]  able to learn something from some of them or at least see what their what their goods and bads are
[1206.74 --> 1211.78]  i guess you know what their fails and successes were to maybe learn from that but otherwise you're kind of
[1211.78 --> 1217.62]  hanging out in uncharted territory right i mean i i use browserify style transforms i write all my code
[1217.62 --> 1222.82]  as common js modules and then they're compiled to whatever i need for the target but all these transforms
[1222.82 --> 1227.46]  run in web workers or if i'm a node they run in something else but they but it's all implemented
[1227.46 --> 1232.90]  in the t edit platform let's pause the show for a minute give a shout out to our sponsor snap snap
[1232.90 --> 1238.58]  is a hosted ci and continuous delivery service that goes far beyond letting you do continuous
[1238.58 --> 1245.22]  deployment don't waste your time set up your own ci box under your desk use snap snap has first-class
[1245.22 --> 1249.94]  support for deployment pipelines with snap you can push any healthy build to multiple environments
[1249.94 --> 1254.26]  automatically or on demand this means with snap you could do things like deploy to your staging
[1254.26 --> 1260.90]  environment today verify it works and later deploy the exact same build to production snap integrates
[1260.90 --> 1265.86]  deep into github has great support for lots of languages databases and testing frameworks snap
[1265.86 --> 1273.22]  deploys your application to cloud services like digital ocean heroku open shift aws and many more
[1273.22 --> 1279.46]  you can also use snap to push your ruby gem to ruby gems and snap is always free for open
[1279.46 --> 1286.18]  source projects try snap for free for 30 days today sign up at snap ci.com slash the changelog
[1287.78 --> 1295.86]  well since you teed up t edit um you know you did js get um i guess out of the box i'm you know i
[1295.86 --> 1300.82]  want you to explain what it is for one and then i guess a follow-up question that would be why no
[1300.82 --> 1305.78]  crowdfunding for t edit but there was crowdfunding for js get okay so on the crowdfunding
[1305.78 --> 1314.18]  it did not go so well the second time the bounty source i set a much higher goal i set a much longer
[1314.18 --> 1321.14]  time frame because i learned that the companies can't get from idea to approval within a couple
[1321.14 --> 1327.06]  weeks they just don't work that fast like brian larue and some other people at adobe were trying to
[1327.06 --> 1331.22]  help me get adobe funding and they're like look if you give us a week of warning we're gonna have a
[1331.22 --> 1336.82]  really hard time getting you that money so i set the goal longer i set the money higher and i traveled
[1336.82 --> 1342.42]  i went to california i talked to people at all the big companies and i was getting nothing
[1344.82 --> 1351.46]  i was several weeks in and i think i just had a few thousand dollars mostly from individuals who
[1351.46 --> 1355.78]  funded me the first time around and just liked me so much they want to do it again yeah that's not
[1355.78 --> 1362.02]  sustainable at the the last second mozilla bailed me out and paid the bulk of it with a grant wow
[1362.66 --> 1368.18]  but i i learned from that that i can't live long term on crowdfunding it helps you get an idea off
[1368.18 --> 1375.06]  the ground it helps you discover if people like it but i don't believe it works long term so what was
[1375.06 --> 1379.30]  the feedback from the individual companies on t edit did it just not align with their particular goals
[1379.30 --> 1385.22]  like js get did or did you have a hard time delivering the vision well i i didn't even try
[1385.22 --> 1391.14]  to fundraise t edit so i don't know oh okay the bounty source was still js get gotcha but the the feedback
[1391.14 --> 1396.74]  i got from several of them and one of them just just bluntly told me he's like look my generation of
[1396.74 --> 1402.98]  managers does not understand giving money to an open source project if we give you money we want a
[1402.98 --> 1409.06]  contract in place and we want exclusive ownership and i was telling them no this code is open this code
[1409.06 --> 1413.54]  this code is freely available to anyone and they're like so you want me to give you money so my
[1413.54 --> 1419.06]  competitors can benefit i'm like yes because if you don't it won't exist and it benefits you too
[1420.26 --> 1426.02]  and they're like nope you think there might just be a generational gap there or maybe it just
[1426.90 --> 1431.94]  case by case i think so i mean mozilla obviously donated the most twice but they're a non-profit whose
[1431.94 --> 1436.26]  goal is the open web right and i'm doing something cool with javascript like they don't actually need
[1436.26 --> 1439.22]  jskit they just thought it was cool that i'm doing something with javascript
[1440.66 --> 1444.74]  i think adobe was the only company who actually had a use for it that donated because they were
[1444.74 --> 1450.42]  thinking of using it in brackets and something with some other stuff that's tough to i mean
[1451.70 --> 1454.66]  you know jared you asked is it a generational gap or something else i think
[1455.70 --> 1459.22]  yeah if you don't have the right person who cares and really understands and i think that's kind
[1459.22 --> 1460.90]  of what we try to do with this show is to
[1460.90 --> 1466.34]  to to not just talk about the projects but also the people behind them and the motivations and
[1466.34 --> 1470.98]  their aspirations and like you had said before the goal behind this project is pretty audacious
[1471.70 --> 1478.18]  and it's uncharted territories and shining a light on that is important because there's a lot of benefit
[1478.18 --> 1483.22]  that can come down the way from all this learning that you're doing and what it gives back but you
[1483.22 --> 1487.38]  know we have a passion for open source we understand the community and it's a lot harder to sell that to
[1487.38 --> 1492.02]  someone who just doesn't get it just doesn't care maybe they maybe they get it they just don't care
[1492.58 --> 1499.46]  and given a lot of money to something and and not seeing in quotes the roi is is really tough we we
[1499.46 --> 1505.38]  face that battle here and there too ourselves yeah it's it's tough i mean there there were companies
[1505.38 --> 1510.10]  which i'm i know benefit a lot from what i'm doing and i couldn't get them to fund because that's just
[1510.10 --> 1515.62]  not their policy that's not how they work and so it's t at a totally nice and weekends and you're just
[1515.62 --> 1523.14]  uh full-time somewhere or at the moment yes so around around new year's the js get money almost
[1523.14 --> 1528.82]  dried up and so i made one last sprint i was going to try to make a product that used js get and i
[1528.82 --> 1533.30]  could sell that product i was going for the business route maybe like maybe i could fund it that way
[1533.86 --> 1538.58]  and so if you look at my github history you'll see i worked insane overtime the first couple months
[1538.58 --> 1544.34]  of this year and i was basically just building t edit from the ground up and i tried a web version i
[1544.34 --> 1549.54]  tried a portable version and i i got stressed and just focused on a chrome app only version
[1549.54 --> 1554.98]  so i just threw away all the all the cross-platform stuff and i got pretty far in the chrome app version
[1554.98 --> 1561.14]  until i finally was really out of money and so right now i'm just i'm doing consulting work
[1562.10 --> 1568.10]  and i work on t edit when i have time but the progress is way slow because i had to stop so i was
[1568.10 --> 1572.50]  going to ask you about the the chrome app piece because you talk about you know open cross-platform and
[1572.50 --> 1576.50]  then i look at it it's a chrome app and i thought this doesn't seem to line up with its goals but it
[1576.50 --> 1584.10]  seems like it's just a just a time and money decision for now well and there's many versions of it this
[1584.10 --> 1592.26]  week actually i i made i made a little time and t edit now runs on chrome and web nice so if you go
[1592.26 --> 1597.38]  to t edit.creationx.com that's the web version and if you look in the source tree it's the exact same code
[1597.38 --> 1602.34]  there's just a few parts where it swaps in some platform primitives and turns off some features
[1603.70 --> 1608.98]  so for example in the chrome app i can access the file system so i can read and write files i can
[1609.70 --> 1616.18]  there's one feature where you can export your t edit build system final files like the built files to
[1616.18 --> 1621.46]  the file system and so you can use a chrome app to make chrome apps or i've used it for node development
[1621.46 --> 1629.46]  before i also say before we dive deep i know that uh t is probably a rough concept for most anyways
[1629.46 --> 1634.50]  maybe you could tee it off by you know you mentioned the goal of you know programming being accessible to
[1634.50 --> 1639.70]  everybody but can you kind of give us what exactly is t edit kind of give us the high level overview
[1639.70 --> 1644.90]  let's let's start diving into some of the details around what it does and how it works and where you see
[1644.90 --> 1651.94]  it going sure so yeah js gets just a library it was just a means to an end and then t edit itself
[1651.94 --> 1658.82]  is the developer environment and the goal there is is i want to i'm thinking of two two main use cases
[1658.82 --> 1664.26]  one is me i like being a random machines like my chromebook pixel for example or who knows what else
[1664.26 --> 1669.78]  maybe my android tablet and i want to be able to do work there and then kids in my programming class or
[1669.78 --> 1675.54]  just anywhere who are learning i want them to be able to use any machine they have i chose chrome
[1675.54 --> 1682.34]  app for now because it's everywhere nearly if the machine has chrome it can run chrome apps
[1683.38 --> 1688.82]  so that's all laptops including chromebooks and desktops and there's a lot of chromebooks in schools
[1689.62 --> 1694.26]  i thought lots of kids had them maybe that's not true i don't know and then two the platform is
[1694.26 --> 1699.14]  very powerful it gives you primitives the web doesn't have i can access the file system i can make a
[1699.14 --> 1704.26]  web server i can get around the cores restriction and talk cross domain you have all these extra
[1704.26 --> 1713.54]  primitives that the browser doesn't have so the the chrome app that's in the the store right now
[1714.26 --> 1721.62]  is basically an ide that edits git repositories directly it does not edit files on disk and this
[1721.62 --> 1724.82]  is a very important distinction between t edit and all the other editors in the world
[1724.82 --> 1731.38]  in everything else git is a tool you use on the side that creates a working directory and then your
[1731.38 --> 1736.10]  editor works with those files on the hard drive and then when you go back to git you pull those files
[1736.10 --> 1743.78]  back into the git database whereas in t edit you never have a working directory ever you always work
[1743.78 --> 1748.74]  directly on the git database so it's a it's a it's a slightly different way of working
[1748.74 --> 1756.10]  does that make for a better user experience or more approachable than than the traditional way
[1756.10 --> 1761.14]  i'm still exploring that one of the things that i found that i like i really like so far is i found
[1761.14 --> 1769.22]  a way to make sub modules not suck really yeah because the concept is not wrong just the ux in the
[1769.22 --> 1775.22]  real git client is terrible it is horribly terrible and this is why people don't use sub modules because
[1775.22 --> 1780.34]  they'll bite you yeah i mean i've personally given up on them a while ago so i don't even know what
[1780.34 --> 1784.66]  the current state of sub modules is because i just nothing's completely just flush them from my brain
[1784.66 --> 1792.50]  no nothing's changed it's okay no one works on it as far as i know okay but like the main issues were
[1794.10 --> 1799.46]  one it doesn't record the branch you're working on like the way it's actually implemented is very
[1799.46 --> 1805.38]  simple in the tree blob for that file listing it's just type commit and then the hash is the
[1805.38 --> 1810.90]  hash in the other repo that's it no other context it just points to the hash in another repo and then
[1810.90 --> 1816.58]  in the root of your project there's a git modules file right that maps that path to a remote url and
[1816.58 --> 1823.22]  that's it so by default in the normal client you're in if you change anything you get thrown in a detached
[1823.22 --> 1827.38]  head state and then if you move some stuff right in the parent repo it'll revert your code without
[1827.38 --> 1832.34]  even warning you and your changes are gone and if right if you forget to push the sub module
[1833.06 --> 1836.90]  and then push the main one it'll point to a commit that doesn't exist on github and like it's a
[1836.90 --> 1845.06]  nightmare so how do you fix it so with t edit everything is one big continuous virtual file system
[1845.94 --> 1852.34]  and sub modules are just mapped in like you do an nfs or samba mount and you can just browse them as
[1852.34 --> 1857.14]  if they were local files and depending on which back end you're using it works really well i have a
[1857.14 --> 1863.38]  github back end that actually mounts the repos using github's rest api and uses github as the
[1863.38 --> 1871.46]  data store instead of a local data store i have a local cache to make it faster but all the real
[1871.46 --> 1878.42]  actions happen directly on github and so suppose i edit a file in a sub module i will then save that
[1878.42 --> 1884.58]  blob to github which gives me back a hash and then i modify the parent tree to say hey it points to this
[1884.58 --> 1888.26]  new hash and then i save that and gets new hash for the parent tree and i do this all the way up to
[1888.26 --> 1894.10]  the root tree and then once the root tree has a new hash i create a temporary commit pointing to that
[1894.10 --> 1900.02]  root tree and then in the parent repository i update the sub module entry to points to that new temporary
[1900.02 --> 1906.74]  commit and then this prop gets all the way up to the root so anytime you change anything in a
[1906.74 --> 1914.42]  t edit tree it's saved all the way up in all the parent repos and so if you knew the the hash to
[1914.42 --> 1918.26]  the temporary commit you could see all these temporary state of your files in github
[1920.34 --> 1924.90]  but that's all in the background like you don't actually see that temporary commit right since i don't
[1924.90 --> 1930.26]  actually move the reference i don't actually move head none of it's visible and in fact if you don't
[1930.26 --> 1933.78]  commit it within two weeks it'll probably get garbage collected by github's back end
[1933.78 --> 1939.46]  hmm so you don't want to be in this state for a long time like i i commit my code every day just
[1939.46 --> 1945.30]  because i don't trust my local machine and not eat my code right is this is this keying off of the
[1946.82 --> 1950.58]  just watching we'll link out to this too so if you're listening we'll we'll have this youtube
[1950.58 --> 1955.94]  video we're going to mention uh we mentioned earlier tim's awesome demo of this which it was
[1955.94 --> 1962.82]  very enlightening and mind-blowing but you said in the video uh it's always committing is that just um
[1962.82 --> 1967.46]  is that kind of like committing to your local git repository and then finally doing a final push
[1967.46 --> 1973.78]  whenever you want to do a commit of that code and is that kind of like a rebase of that or or
[1973.78 --> 1977.62]  whatever to kind of munch it into one commit is that what you're doing or is it something more unique
[1977.62 --> 1985.38]  than that no it's um so like like i said when i'm using the github back end your jsgit instance is a
[1985.38 --> 1990.82]  proxy to github there is no local database there is no clone there is no pool there is no fetch there is no
[1990.82 --> 1997.70]  push you are literally modifying your data on github directly like if you open up the terminal you can
[1997.70 --> 2003.70]  see rest calls just flying back and forth but it actually performs pretty well so how does that
[2003.70 --> 2008.66]  handle offline is it just queue them up and wait it doesn't or it doesn't okay i have a task for that
[2009.30 --> 2014.66]  okay because i want offline though right i mean you got a lot of this it's offline and secure i heard
[2014.66 --> 2018.02]  that a couple times in the video can you talk about that is that a good time to talk about that or
[2018.02 --> 2023.54]  uh sure so the backends there's lots of backends for jsgit there is no one back end the jsgithub
[2023.54 --> 2028.34]  back end is the one that live mounts github repos it's the one i use the most because i don't have
[2028.34 --> 2035.70]  push and pull implemented and so i can't sync and so i just use that one but once i implement the
[2035.70 --> 2040.90]  network protocols the other backends will work great there's an index db back end i was working on a web
[2040.90 --> 2046.90]  sql back end this morning there's i had a local storage one but i don't know if it's still maintained
[2046.90 --> 2053.30]  because there were some issues there mostly with just limited space if you're a node i have a back
[2053.30 --> 2059.46]  end that can that can read and write real git repos off disk so it implements that format that dot get
[2059.46 --> 2065.30]  folder i have the same thing for chrome apps because chrome apps can access the native file system so you
[2065.30 --> 2071.14]  can mount a native git repository using a chrome app edit it and t edit and then push it from the
[2071.14 --> 2077.46]  command line if you have node or if you have git so there's lots of backends and it's very flexible
[2078.26 --> 2084.34]  there was i had people talking to me one company thought about using s3 as a back end and all i
[2084.34 --> 2090.26]  really need is a key value store that's the bulk of what git needs for its storage so it's depends on
[2090.26 --> 2097.54]  what performance you want you can use anything as the back end yeah but yeah i haven't i haven't
[2097.54 --> 2102.58]  implemented push and pull fully yet i haven't implemented merge or diff because and those are
[2102.58 --> 2106.82]  being on the js get side right not on the t edit side yeah they're part of js get but t edit will use
[2106.82 --> 2112.74]  them it'll it'll expose interfaces for them and yeah that's that's where i was when i ran out of money
[2112.74 --> 2118.02]  i was i was implementing that stuff and then i couldn't get done so you mentioned you're you ran out of
[2118.02 --> 2124.74]  money where what is the state of this project right now i guess from uh obviously you're passionate
[2124.74 --> 2129.86]  about it so that that kind of goes without saying but you know are you out of money what's the next
[2129.86 --> 2135.46]  step to giving yourself the necessary time to keep building this and i guess what is your direction
[2136.50 --> 2142.98]  so i've got some consulting work till end of june and after that i'm going to take another run at it
[2142.98 --> 2148.82]  see how much i can get done and see if i can find more novel ways to fund it i don't know yet
[2149.94 --> 2156.34]  how i'm going to do that i'm just trying to survive and get there some some ideas i had was t edit
[2156.34 --> 2162.02]  consulting where people would want to use js get or t edit in their product and they could pay me to
[2162.02 --> 2168.50]  integrate it into their platform and i found some interest there from a few companies i could do
[2168.50 --> 2174.10]  one one thing i really want to do back to my original goal is i want to make games i want to
[2174.10 --> 2179.94]  make simple games make them open source and then write docs about how to write games so these kids
[2179.94 --> 2186.34]  can get into programming and i was thinking about maybe selling podcasts or tutorials because people
[2186.34 --> 2191.06]  seem to want to pay for that what i don't want to do is i don't want to charge for the code
[2192.26 --> 2197.30]  because i'm essentially writing infrastructure and infrastructure should not be for pay it should be freely
[2197.30 --> 2200.50]  available because it's just code it doesn't it's not like it cost me anything to copy it
[2202.02 --> 2207.22]  so i want t edit and js getting all the code itself to stay open sourced mit or apache something very
[2207.22 --> 2213.94]  very liberal and find other ways i've considered another fundraiser but like i said before i don't
[2213.94 --> 2218.90]  think that's sustainable yeah it's well especially if you've been through two and the second one
[2220.02 --> 2226.02]  even had the help of bounty source um still had to be you know the final bit taken care of by mozilla
[2226.02 --> 2231.14]  and big shout out to mozilla too you know i'll give them a thanks i know you already have but on the
[2231.14 --> 2237.86]  show that's that's awesome to support tim like that so yeah they're awesome tim you mentioned um in
[2237.86 --> 2243.54]  that in the video that we keep mentioning your demo uh a pro version what is that on the horizon that's
[2243.54 --> 2247.54]  is that something that you're thinking about you just mentioned free code you know and no charge
[2247.54 --> 2253.86]  for infrastructure so does does a pro version fit into that um i don't know i've sort of scrapped that idea
[2253.86 --> 2258.42]  i do still have a hosting platform i've been developing and that's actually my only private
[2258.42 --> 2266.34]  repo on github and we haven't talked about the t edit build system yet but yes that was pretty neat
[2266.34 --> 2272.74]  too high level it's a build system like grunt or gulp or whatever but it works completely different
[2272.74 --> 2278.98]  and you don't need a command line but this the same build system i've implemented in a node web service
[2278.98 --> 2286.74]  where i can host your t edit based web apps and it's basically github pages but with a bunch of
[2286.74 --> 2294.26]  smarts baked in so one idea is i could charge for that hosting because it's a service i don't mind i
[2294.26 --> 2297.62]  don't mind charging for services i just don't want to charge for the infrastructure code
[2299.86 --> 2305.38]  but hosting is a hard thing to make money from the the build system that you mentioned is that um
[2305.38 --> 2311.38]  is that where you were piping into like app cache and the other tools that are available to to build
[2311.38 --> 2318.66]  something because you use the use t edit to rebuild another version of t edit right right so let me let
[2318.66 --> 2325.70]  me go into that so the original goal was i wanted a full development environment so once i have get done
[2325.70 --> 2331.22]  and i've implemented push and pull and merge and diff and all that fun stuff i have version control i have
[2331.22 --> 2338.18]  sharing and i've done dependencies with the easy sub modules i can add a package manager on top of
[2338.18 --> 2344.26]  that that just eases setting up these sub modules but you still need a way to build files in modern web
[2344.26 --> 2348.74]  development maybe some people use coffee script maybe you like writing common js but you're running
[2348.74 --> 2354.26]  in a browser you need you need build steps and so the t edit build system is kind of unique
[2355.06 --> 2359.62]  the way it works is you create these rule files i think there were some links in the video yeah
[2359.62 --> 2364.90]  but now they're rule files dot rule they're actually written in john which is a subset of jack
[2365.54 --> 2370.74]  like json is a subset of javascript so they look like json they're just a little more flexible
[2371.38 --> 2377.86]  and you basically say all right this so you take the file that you want to exist i need an app cache
[2377.86 --> 2384.10]  manifest or manifest app cache and then you add dot rule to the file name mark it as executable because
[2384.10 --> 2390.10]  you can do that cross-platforming git because i'm not using real files and what the system will do
[2390.10 --> 2396.66]  is when it sees an executable dot rule file when it's serving over the web or exporting to disk or
[2396.66 --> 2402.34]  going through anything that needs the built version of the files it will execute that rule and the rule
[2402.34 --> 2408.50]  itself will be an arbitrary program the user writes and i'm going to maintain a library of some useful
[2408.50 --> 2413.62]  things and so these are the equivalent of your your gulp or grunt plugins and so i have one called app
[2413.62 --> 2419.30]  cache and you give it a listing of files and what it will do is it will search the git tree the built
[2419.30 --> 2425.38]  version find the e-tag of all those files and append them as comments in the app cache and if you've
[2425.38 --> 2429.78]  worked with that cache before you know that the the file needs to change every time any file it depends
[2429.78 --> 2435.30]  on changes and so that way you don't have to constantly go update some timestamp in your app cache
[2435.30 --> 2440.66]  so when you refresh in the browser it automatically grabs the new app cache and you always have the
[2440.66 --> 2447.54]  latest code and there's there's other compilers there's the the one i just built for my cross
[2447.54 --> 2454.50]  platform stuff i called what did i call it js compiler something really really plain but what
[2454.50 --> 2461.14]  it does is it takes a tree of source code that's in common js node style and then builds it as a bunch
[2461.14 --> 2469.22]  of amd modules and then i have a really really minimal amd loader that injects those as script
[2469.22 --> 2475.46]  tags in the web page and loads them on demand and i'm going to add another version that builds a
[2475.46 --> 2481.70]  single concatenated file for websites that want to work offline and so what you'll do is you'll have
[2481.70 --> 2485.86]  all your javascript in the one big concatenated file and then your app cache manifest will point to
[2485.86 --> 2490.50]  that file and then anytime anything changes the e-tag of the big file will change which will then
[2490.50 --> 2496.18]  cause them app cache to change and so you'll have automatic concatenation we can throw in
[2496.18 --> 2500.98]  minification you can have any other filters you want we could do coffee script i have a
[2502.02 --> 2506.98]  i've put facebook's regenerator in there because i really like using generators so now i can use
[2506.98 --> 2513.46]  generators in any web app or chrome app i want and all of this works without a command line without node
[2513.46 --> 2519.62]  without anything let's pause the show for just a minute give a shout out to our sponsor top towel
[2519.62 --> 2524.34]  now we've been working with top towel for about a year now almost a year now and we thought it would
[2524.34 --> 2530.74]  make sense to circle back and talk to some of our listeners who have applied to top towel and have
[2530.74 --> 2535.46]  been accepted because only about two to three percent of the engineers who apply make it past their strict
[2535.46 --> 2541.22]  elite engineering process and daniel lauzon a long-time listener and fan of the changelog
[2542.26 --> 2548.74]  is now living the dream he's an elite engineer top towel and i say living the dream because he's now able to
[2548.74 --> 2554.50]  have 100 control of the types of projects and technologies he's working on as well as the rate
[2554.50 --> 2561.30]  he wants to charge daniel earns 100 of his income as a top towel engineer and he wanted me to pass on
[2561.30 --> 2566.18]  his seal of approval of the top towel experience for those of you out there who are freelancing or
[2566.18 --> 2571.30]  like to test out freelancing you've got to check out top towel if you think you have what it takes head to
[2571.30 --> 2577.94]  top towel.com slash developers that's t-o-p-t-a-l.com slash developers to get started tell them the
[2577.94 --> 2578.74]  changelog sent you
[2581.30 --> 2584.66]  you mentioned in the video too since you're mentioning node and npm i think you mentioned earlier
[2584.66 --> 2592.10]  um you know on a chromebook so you're this is just to kind of recap this is pointed right now it's a
[2592.10 --> 2596.98]  chrome app and i think it seems like if i'm if i'm hearing you correctly it seems like it's a chrome
[2596.98 --> 2600.90]  app now not because you don't want to be cross-platform but because you have limited time
[2600.90 --> 2606.98]  and you need to make progress um is that is that accurate to say well i need i need the extra
[2606.98 --> 2612.74]  primitives the web version has serious limitations right i can't get github or bitbucket to turn on
[2612.74 --> 2617.14]  cores i have asked them multiple times and i don't know if they have security security concerns or what
[2617.14 --> 2624.42]  but a web page cannot clone from github because it's cross domain yeah right now there is the rest api
[2624.42 --> 2628.90]  which i use extensively but it's it's much slower and it's proprietary to them and it's not the same
[2630.50 --> 2635.38]  so with a chrome app i have full access to everything and also i can access the file system
[2635.38 --> 2642.18]  i can create a local http server and so you can write a web app in the chrome app host it start
[2642.18 --> 2646.98]  the web server in the chrome app and then another tab in your chromebook you can then run your web app
[2647.54 --> 2652.34]  and all of the build files will be built by t-edit in the chrome app and everything works end to end
[2652.34 --> 2657.46]  and then like you mentioned you can also self-host the t-edit itself so i can build a chrome app with
[2657.46 --> 2663.46]  a chrome app that's awesome let me just stop you for a second and say you're doing some really cool
[2663.46 --> 2668.58]  stuff when i watched that jared up my i was like i seriously almost fell over i had to catch myself
[2669.86 --> 2674.10]  i feel like there's certain people out there that like everybody should they should just be given a
[2674.10 --> 2678.42]  bunch of money and be like just go do your thing and we're all going to be better off and i got a
[2678.42 --> 2685.94]  feeling you're one of those guys sounds good to me well we're offline i mean what i think uh i think
[2685.94 --> 2691.14]  what jared's trying to say is you have our full support whatever we can ever do to help you we're
[2691.14 --> 2694.90]  going to be there for you and i'd like to talk to you more about some ways we can be a part of that and
[2694.90 --> 2702.34]  just help make your life a little easier if we can so you um you touched on the web server part of it
[2702.34 --> 2707.22]  um is there any more we can mention about that i think it's just kind of unique that it's it's all
[2707.22 --> 2714.50]  encompassing t-edit it's it not only is it it's a full-on ide it's it's uh edit straight from git i
[2714.50 --> 2721.54]  mean this is pretty some pretty amazing stuff um you know you can run the app itself with it um
[2722.74 --> 2727.62]  and i think one other quote you said you're not building an editor you're building a workflow
[2727.62 --> 2734.10]  and it seems like this is you know not only is it it's got all these complex back-end pieces but
[2734.90 --> 2740.10]  you're also able to serve up whatever you've built and then the offline part that i think you touched
[2740.10 --> 2744.74]  on in the video that i'm not sure how accurate it is now because that was in february but you were
[2744.74 --> 2750.50]  able to kill the current web server and still serve up the game from the app cache right so app cache
[2750.50 --> 2755.70]  lets apps work offline and when i get the web version of t-edit done it's going to have its own app cache
[2755.70 --> 2761.78]  so you can you can go on an android tablet go to t-edit.creationx.com it'll run today but you have
[2761.78 --> 2767.86]  to be online but once i get all of that done and i've implemented offline sync then you'll be able
[2767.86 --> 2775.30]  to add this to home screen it'll work offline just like any native app which which i'm very excited about
[2776.26 --> 2781.62]  how has uh mounting a github repo changed it see i couldn't tell from the video how
[2781.62 --> 2787.38]  it seemed like you had to like manually type in you couldn't just like what maybe some users at
[2787.38 --> 2792.90]  least i was thinking that you might just be able to choose um you know from the repo versus like
[2792.90 --> 2799.78]  hand typing in creation x slash t edit i have an app for example to to kind of and then you also had
[2799.78 --> 2804.66]  to point back i think a sha1 code can you talk about mounting a github repo maybe how that's changed
[2804.66 --> 2810.34]  since february if it's changed at all so that that ux hasn't changed much the what that is is it's a
[2810.34 --> 2816.50]  github token and i'm not sure you can github oauth from anything that doesn't have server
[2816.50 --> 2821.54]  assistance because the way they've set up their oauth but you can go to github and request an app
[2821.54 --> 2825.86]  token and then paste that token in and you only have to do it once to set up your machine and it
[2825.86 --> 2831.14]  remembers it okay now the other part that the paste in the url is just me being lazy there's no
[2831.14 --> 2836.66]  reason i couldn't have a smarter ui that using the rest api queries all of your git repos and gives
[2836.66 --> 2841.78]  you a drop down or some smart selector or whatever that's a nice to have not a need to have right
[2841.78 --> 2846.50]  yeah i'm focusing on the things that other people can't do or other people think they can't do there's
[2846.50 --> 2854.18]  nothing i'm doing other people can't do and um just to kind of key off one more thing i i'm not sure
[2854.18 --> 2859.78]  if we touched on it i think slightly but it uses ace editor and it kind of goes back to what i just said
[2860.26 --> 2864.74]  which is what you said actually uh which is i'm not building an editor i'm building a workflow so you
[2864.74 --> 2869.22]  didn't actually build the editor part of it this is from an existing open source project that's out
[2869.22 --> 2873.38]  there i think i was going to ask about your cloud cloud nine experience i'm assuming you had some
[2873.38 --> 2877.94]  part in ace editor as well i didn't actually work on ace a lot while i was there it was pretty much
[2877.94 --> 2885.78]  fabian's work i've at cloud nine i was doing a bunch of infrastructure back-end stuff making the like
[2885.78 --> 2890.26]  the big thing i did there was i made the terminal run in the browser over web socket with the lowest latency
[2890.26 --> 2897.22]  possible okay but yeah ace is amazing i've i used code mirror for a while and then i switched to ace
[2897.22 --> 2902.02]  because i i prefer it personally it's it's a lot more full-featured out of the box but it's also a
[2902.02 --> 2908.34]  lot bigger so it's a trade-off i liked your um your comments too about working late at night near
[2908.34 --> 2914.10]  children in low light levels and being able to easily swap out the various um oh right the various
[2914.10 --> 2919.62]  syntax highlighting colors that was pretty neat too so when you open up t-edit you're going to see a
[2919.62 --> 2924.02]  nice window at a tree view the tree view is all my code and that's all custom code that's the bulk
[2924.02 --> 2931.06]  of the code actually everything's inside that tree and using tj holloway chuck's css parser i parse out
[2931.06 --> 2937.46]  the ace theme when you change themes and then apply the same colors to the tree so your entire screen is
[2937.46 --> 2942.90]  the same color scheme because like you said i am i am all often working in the dark in a bedroom next
[2942.90 --> 2948.10]  to children helping them sleep and i hit having this bright white tree here next to this dark code
[2948.10 --> 2954.10]  here and it's yeah it doesn't work yeah i've kind of i like that too it's just i think those who
[2954.66 --> 2960.26]  primarily work maybe in in vim or something like that are used to it because it's all whatever they
[2960.26 --> 2965.86]  set for their theme in you know in their terminal but for those who maybe work in sublime text or
[2965.86 --> 2970.98]  other i guess ide's you generally have syntax highlighting and colors for your code but then
[2970.98 --> 2975.78]  it doesn't really apply to your sidebar your you know your file system like you just mentioned so it's
[2975.78 --> 2980.02]  it was neat how those played a part too and just even easy to how you can swap
[2980.98 --> 2987.78]  from one color to another i think it makes it a little harder in other editors and for some reason
[2988.34 --> 2994.58]  you just made it so easy right like i said my focus is accessibility yeah and part of accessibility is
[2995.46 --> 3000.66]  uh vision so one of the first things that i did for t-edit was you can change the font size and the
[3000.66 --> 3007.38]  color scheme with keyboard shortcuts there you can change them very easily so if i'm presented at a
[3007.38 --> 3012.50]  conference and i'm live demoing i can change it to a white background if it's not a very good projector
[3012.50 --> 3017.78]  i can bump up the font or shrink it down i want all these things to be extremely easy because i don't
[3017.78 --> 3021.06]  want them to get in the way so those were some of the first things i did
[3021.06 --> 3030.82]  well we didn't talk at all about chrome fs maybe you mentioned it note fs um i'm just looking at some
[3030.82 --> 3036.50]  of our notes we had for this call what before we begin to close out the show what other things can
[3036.50 --> 3041.86]  we mention that you know just you haven't done enough tim so what else is there to mention that's
[3041.86 --> 3047.06]  um really important to close off i guess talking about t-edit and i guess the direction you're taking
[3047.06 --> 3051.62]  with that right we should probably talk about the current state of the project and what people can
[3051.62 --> 3059.06]  use now okay well it's not done and the biggest missing pieces are network and diff and merge but
[3059.06 --> 3066.10]  what is done is a lot the js github backend is quite mature i use you can use it node or web app or chrome
[3066.10 --> 3075.38]  it works anywhere the and that's the js github project there's two new ones there is get chrome fs and
[3075.38 --> 3082.26]  get node fs and what those do is those use the built-in mix in and js get the fsdb and they let
[3082.26 --> 3088.82]  you mount real git repos using js git either from a chrome app or through node and so the the hosting
[3088.82 --> 3095.70]  project i was talking about what it does is it github mounts the projects but then it caches them
[3095.70 --> 3102.10]  locally using a real git repo using the git node fs and when i'm doing my consulting work what i'll do is
[3102.10 --> 3109.06]  using t-edit i will mount my local git repo on my macbook and that way i can edit the git tree in t-edit
[3109.70 --> 3113.62]  and i need the files back on the hard drive for node and so i live export the whole thing to the
[3113.62 --> 3119.86]  hard drive and so anytime i change a file it writes it out first to the git repo and then to the working
[3119.86 --> 3126.90]  directory so i can test my code there there's a there's a few weird things about it because i now have
[3126.90 --> 3134.66]  two copies of everything but some nice reverts or git resets fix that pretty quickly so you can use
[3134.66 --> 3143.06]  js git today for a lot of things you can since you can read and write existing git repos if you're on a
[3143.06 --> 3149.70]  server where you have real git then you can clone using normal git and then using js git you can mount
[3149.70 --> 3156.02]  that repo and use this nice javascript api to walk the tree and walk the commits and do code analysis
[3156.02 --> 3162.50]  or custom builds or whatever you want so this could be used for javascript package managers or build
[3162.50 --> 3168.42]  systems or continuous integration systems i want to be able to eventually use it for mobile apps that
[3168.42 --> 3176.50]  want a syncable offline storage and so i have two tasks there that i'm going to work on soon one is i'm
[3176.50 --> 3180.98]  adding sync to the github back end so it can actually work offline and then sync with github
[3180.98 --> 3185.70]  using the rest api and then another one is i'm going to implement the full pack protocol that
[3185.70 --> 3190.90]  everyone else uses that real git uses for the platforms that actually have that network primitive
[3193.06 --> 3197.70]  since you were talking about the i guess location of where things like mounting from github it seems
[3197.70 --> 3204.26]  like it's got some deep github integrations at one point during your demo you talked about owning your
[3204.26 --> 3209.38]  own code and you feel very passionate about that is it is it where you store your code or what did
[3209.38 --> 3215.46]  you mean by that i couldn't quite understand what you were trying to trying to emphasize with owning
[3215.46 --> 3220.74]  your own code in the editor is that is that keying off of where you mount your repos from like your own
[3220.74 --> 3228.34]  private repos or github or bitbucket is it is it that or is it something else so i i worked with cloud
[3228.34 --> 3233.38]  ids i mean i've worked at cloud nine for a while and the biggest issue i had with them is your entire
[3233.38 --> 3239.46]  workspace lives on some cloud server right which i mean first of all that's a practicality issue you
[3239.46 --> 3244.74]  have to be online and that's that's a non-starter for me i have flaky internet i travel a lot
[3246.10 --> 3249.70]  and then it's on their cloud server they can read it they can write it they have full access to your
[3249.70 --> 3253.70]  code they have your github token they can write to your github i don't think any of these companies
[3253.70 --> 3257.78]  are malicious but just from a security standpoint you don't want anybody with that much power
[3258.58 --> 3261.38]  they could be corrupted they could be hacked they are now a hacking target
[3262.50 --> 3267.94]  whereas if everything lives locally in your device and you just push to github or bitbucket as a
[3267.94 --> 3274.10]  public mirror then it's different you you are now in control of it and you control who has access
[3275.70 --> 3282.50]  so and also with jsgit it's not hard at all to write your own your own services and your own hosting
[3282.50 --> 3286.82]  as soon as i get some of this network syncing stuff done it'll be trivial for people to host
[3286.82 --> 3292.58]  their own git repos and even mount them off their own servers yeah because the light the live mount
[3292.58 --> 3297.14]  is really convenient if you have large repos with lots of sub dependencies you don't have to do
[3297.14 --> 3299.78]  recursive clone you just instantly mount and everything's available
[3302.50 --> 3307.94]  i was gonna say it seems like i mean for the most part github is very popular because of its
[3307.94 --> 3313.06]  collaboration around open source not so much for being a git hosting platform that's how they started
[3313.06 --> 3319.62]  but they popularized social coding so to speak and obviously are responsible for a lot of the big push
[3319.62 --> 3324.34]  and adoption for open source and maybe even some growth uh maybe somebody's gonna punch me in the
[3324.34 --> 3329.70]  face for saying this but like just growth in the developer ecosystem you can't you can't uh not
[3329.70 --> 3336.34]  recognize their power and their um you know their push for this so i just kind of wondering it seems like
[3336.34 --> 3342.26]  uh because t edit is so easy to use in this respect by money a repo it doesn't really have to live
[3342.26 --> 3347.86]  on github it's just that's your means right now right and like you can use the web version today
[3347.86 --> 3351.22]  mount to github repo and edit it so if you just want a quick way to edit your git repos
[3351.86 --> 3358.18]  just go to t edit.creationx.com paste in your token and edit anything at will we got uh several links that
[3358.18 --> 3362.74]  uh this will be a link filled show notes episode so if you're listening to this
[3362.74 --> 3369.46]  uh go back to the change log find the episode i think this is 124 if i remember correctly um
[3370.42 --> 3374.90]  uh and also on five by five the the links will be there or even in your podcast catcher so
[3375.46 --> 3380.42]  we'll we'll share tons of links so if you can't hear us or you weren't sure uh check the links we'll
[3380.42 --> 3385.06]  we'll have a bunch of show notes for this but uh jared is there anything else you want to mention
[3385.06 --> 3390.90]  before we start uh closing off the show well i did want to ask about jack but i'm not sure if we
[3390.90 --> 3394.58]  have time to even you might have to have him back just for a whole entire show maybe you can
[3395.14 --> 3400.74]  maybe do a quick overview and we'll have you back to talk about jack all right um jack is a fun
[3400.74 --> 3407.62]  project my goal there is to make a language that's easy to learn yet powerful it's basically a mix of
[3407.62 --> 3413.62]  javascript and lua and i'm really excited to actually use it someday i haven't had time for it yet
[3415.30 --> 3418.90]  so is it backburnered because of t edit at this point it's way backburnered it's i've
[3418.90 --> 3426.42]  been working on it since before coffee script wow that's a long time yeah uh and then you also
[3426.42 --> 3434.10]  mentioned john which is a i guess a sub brother subsister so i guess right subset subset yeah it's a
[3434.74 --> 3443.22]  it's jack object notation okay so john is to jack as json is to javascript so in t edit all the config
[3443.22 --> 3448.74]  files and that one file that opens up with the instructions those are all basically john format
[3449.46 --> 3454.34]  so it's it's just a subset of jack that's the data format and it's a strict superset of json so you
[3454.34 --> 3458.66]  could write json and that would work but the quotes are optional the commas at the end are optional you
[3458.66 --> 3463.86]  can have comments in line it's a it's a little more flexible than json you decided against jill on that
[3463.86 --> 3473.54]  one huh yeah didn't fit the acronym yeah we can yeah that's that's neat though so i i guess uh yeah for
[3473.54 --> 3478.42]  one i mean i just uh i'm not even kid when i said i almost fell over with uh watching your videos like
[3478.42 --> 3483.38]  wow this is insane what you're doing and you're definitely leading the charge in that that's that's
[3483.38 --> 3489.62]  for sure so um i one way we close the show off is we have a couple questions i don't think we had
[3489.62 --> 3493.22]  these questions whenever you first came on the show back when you're talking about lua i think in the
[3493.22 --> 3498.82]  early 20s of the change log um but one one question we ask and you may have already asked
[3498.82 --> 3504.18]  or answered this during the call but to be blatantly clear what does it call to arms for your projects
[3504.18 --> 3508.74]  you know js get i think that's pretty much complete but um obviously you're probably still accepting
[3508.74 --> 3515.46]  code uh to that but how how can how can the general public listening to this either step up and help you
[3515.46 --> 3521.46]  code wise issues wise how can the community step up and help you so it's it's to the point where other
[3521.46 --> 3527.86]  people can code without getting in the way i have a lot of issues what what i really need is starting
[3527.86 --> 3533.70]  in july if your company is interested in using this you can hire me to integrate it and i promise that
[3533.70 --> 3541.70]  almost every company with that involves data or dev tools can use this in some way so if you can get
[3541.70 --> 3546.58]  your company to hire me to help integrate this to add the features you want i want it to kind of work
[3546.58 --> 3551.54]  like the code mirror or lua jet projects where they have corporate sponsors who add features
[3552.66 --> 3553.86]  and then everyone can use the code
[3556.34 --> 3561.70]  and and the what's the best way to get in touch with you you got creationx.com is your home page
[3561.70 --> 3565.62]  we'll have that in the show notes is that is there a contact button on there or how what's the best way
[3565.62 --> 3572.02]  to reach out to you i hope there's a contact button i don't know i mean my my email is probably
[3572.02 --> 3579.38]  the best my email is public on my github it's tim at creationx.com gotcha you yeah that works and uh
[3579.94 --> 3585.22]  i guess the next question which is is usually a fun question so i mean it doesn't have i'm considering
[3585.22 --> 3590.74]  your background i'm assuming you'll be talking about uh programming to some degree but what would
[3590.74 --> 3603.38]  you be doing if you weren't doing what you're doing good question if i wasn't doing the js get
[3603.38 --> 3608.90]  to edit stuff yeah this mission we're talking about on this show like if you weren't trying to put all
[3608.90 --> 3613.38]  your passion all of your effort and all of your time into that either through your own free time or
[3613.38 --> 3619.86]  supported time you know if you weren't doing that what would you be doing i would probably be
[3620.74 --> 3626.82]  oh i don't know if i wasn't programming i'd be making things that's for sure i i make things
[3626.82 --> 3632.66]  with paper with wood with whatever if it was computer related i'd probably be writing libraries
[3632.66 --> 3639.62]  template engines compilers that's that's still pretty much related to this i i'd be making something
[3639.62 --> 3646.58]  for sure i am always making things i'm always creating that's why my my handle the creationix is
[3646.58 --> 3652.74]  the word creation and then ix from linux from unix i create open things that's what i do i was
[3652.74 --> 3659.78]  thinking that uh the x part kind of gave it away but i was i wasn't sure for sure yep i i create things
[3659.78 --> 3667.22]  and then i open them up that's what i do and i guess uh our last question we ask is uh i don't know if you
[3667.22 --> 3672.50]  answered this your first time around but uh who's your programming hero like who's inspired you who's
[3672.50 --> 3677.46]  help lead you who's encouraged you anybody it can be one person could be a couple people
[3677.46 --> 3683.94]  whomever oh i got i got lots of heroes um name them all that's fine all right there's a couple language
[3683.94 --> 3689.22]  designers i like i like matt's from ruby he's a really cool guy i've met him in person i like brendan
[3689.22 --> 3696.50]  ike from javascript they're they're very different people but i like them both um i'm i'm impressed with
[3696.50 --> 3702.66]  mike paul for the way he gets paid to work on luiget even though i know very little about his
[3702.66 --> 3709.46]  actual person he's quite cryptic oh i'm gonna butcher his name but um the code mirror guy is it
[3709.46 --> 3716.42]  marine how do you say his name i don't know what look it up the the author of code mirror
[3717.30 --> 3722.26]  and turn js and the eloquent javascript book he he is amazing i love what he's done
[3722.26 --> 3726.82]  let me look behind me i have it on my shelf yeah the big yellow book that book is great
[3727.30 --> 3733.06]  let's see i'll try and he's good he's i've been meaning to reach out to him too i'm gonna say
[3733.06 --> 3737.86]  marriage and have her back have her back yeah i'm sure i butchered the name i probably did too
[3737.86 --> 3744.50]  sorry about that i think he's awesome so yeah i i like those people i think they're cool awesome
[3744.50 --> 3747.62]  we'll do our best to to do some digging too and make sure we get some links in the show notes so if
[3747.62 --> 3752.34]  you're i know one reason i like asking that question on the show is just it kind of gives
[3752.34 --> 3757.62]  some insight to who inspires you and they're not always um people that are very public like you'd
[3757.62 --> 3763.38]  mentioned you don't know so much about um one particular person just because they're sort of
[3763.38 --> 3768.74]  just not very public about what they do so but their work is and that's what inspires you
[3770.34 --> 3776.66]  uh yeah i think that's that's this has been a fun show man i know that uh t edit i again i'm glad
[3776.66 --> 3782.50]  you said t edit because i was going to call it ted it um just based on the the the phonetic
[3782.50 --> 3788.34]  sounding of it i suppose i was going to sound it out versus thinking just t edit but uh tim thanks
[3788.34 --> 3793.30]  so much for joining us on today's show i know that um you know we'll definitely help you out if we can we
[3794.26 --> 3798.90]  uh we'll do whatever we can to also in the future now or in the future just promote ways that the
[3798.90 --> 3803.78]  community can support you whether it's through funding or whatever so if ever you need a friend to
[3803.78 --> 3809.30]  to help you out we'll we'll be there for you but um before we close the call i want to give another
[3809.30 --> 3814.98]  shout out to our sponsors digital ocean top towel and snap ci for supporting the show thank you so
[3814.98 --> 3819.94]  much for your support and if you uh if you're a listener and you haven't yet done this subscribe
[3819.94 --> 3824.10]  to the change law weekly it's been on a small hiatus but there's no reason not to sign up because
[3824.10 --> 3830.58]  we are bringing it back uh we get death threats and emails daily about where's this awesome email i've
[3830.58 --> 3834.58]  been getting and why did you stop doing it so we can't stop shipping that so the change
[3834.58 --> 3840.02]  law.com slash weekly to sign up uh jared thanks so much for joining me on the call today and tim you
[3840.02 --> 3844.98]  as well and the listeners for listening so until the next time we speak maybe about jack let's say
[3844.98 --> 3858.10]  goodbye see ya all right see you guys later bye
[3860.58 --> 3872.66]  bye
[3872.90 --> 3877.06]  you
