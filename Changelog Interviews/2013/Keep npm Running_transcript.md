[0.00 --> 14.02]  welcome back everyone this is the changelog we're a member supported blog podcast and
[14.02 --> 19.74]  weekly email that covers what's fresh and what's new in open source check out the blog
[19.74 --> 25.74]  at the changelog.com our past shows at 5by5.tv slash changelog and subscribe to the changelog
[25.74 --> 29.98]  weekly it's our weekly email covering everything that hits our open source radar we ship it
[29.98 --> 36.46]  on saturdays you don't want to miss it subscribe at the changelog.com slash weekly and this is
[36.46 --> 42.34]  episode 113 and today's show is sponsored by digital ocean and top towel we'll tell you a bit
[42.34 --> 48.38]  more about top towel here in just a bit later in the show but top towel connects startups businesses
[48.38 --> 55.46]  and organizations to a growing network of elite engineers around the world check them out at
[55.46 --> 61.58]  top towel t-o-p-t-a-l.com and digital ocean has been supporting us for quite a while we love
[61.58 --> 66.54]  digital ocean we're actually hosted on digital ocean right now which i have to say is fantastic
[66.54 --> 74.10]  and we want you to get hosted on blazing fast digital ssd cloud servers today they're a simple
[74.10 --> 79.02]  cloud hosting provider built for developers you can easily create a new droplet which is basically a
[79.02 --> 85.76]  server and you can get root access in 55 seconds literally in 55 seconds you will be shelled into
[85.76 --> 91.40]  your new machine you get a choice of size you know so you you want a large server a small server
[91.40 --> 97.64]  a lot of ram not a lot of ram choose the region whether it's new york or amsterdam or one of their
[97.64 --> 102.56]  other locations where they have data centers at and also the flavor of os so no matter what it is
[102.56 --> 108.96]  arch linux ubuntu whatever your choice is within 55 seconds you'll have all that set up and you'll
[108.96 --> 114.66]  literally be ssh into that machine all through an easy to use dashboard you can enable backups take
[114.66 --> 121.54]  snapshots to your server resize up or down as needed and they are and when i say they digital ocean is
[121.54 --> 128.82]  optimized for developer user experience that i cannot stretch that enough that it is so easy and so
[128.82 --> 133.62]  pleasant to use you've got to try it try digital ocean today for free use the promo code we have
[133.62 --> 139.50]  changelog sent me that's changelog sent me when you sign up you're gonna enter your credit card
[139.50 --> 144.16]  information and and near that spot there there's a spot where you can add that coupon code go ahead
[144.16 --> 148.30]  and pop it in there which will give you a ten dollar hosting credit or two months free if you're going
[148.30 --> 153.48]  with their lowest plan head to digitalocean.com right now to get started telling the changelog sent you
[153.48 --> 159.00]  and we're joined by charlie robbins and isaac schluter charlie is the co-founder and ceo of
[159.00 --> 164.32]  nodejitsu and isaac you're back again you're the creator of npm and the maintainer of node.js and
[164.32 --> 168.94]  i gotta welcome charlie you're the first time on the show but uh isaac you're back again you were
[168.94 --> 175.00]  recently on i think was 101 i believe is what it was sounds about right sounds about right yeah we had
[175.00 --> 180.66]  you talking about i guess a little bit of burnout a little bit of npm history some origins and i guess
[180.66 --> 187.28]  part of this call here is kind of going deeper into the origins of of npm and mostly around the
[187.28 --> 193.40]  registry but uh before we dive deep into the show let's do a quick round of introductions charlie why
[193.40 --> 199.36]  you uh introduce yourself real quick bud how's it going everyone i'm charlie robbins i'm the co-founder
[199.36 --> 206.20]  and ceo of nodejitsu um in addition to running a platform as a service for node.js we also host
[206.20 --> 211.64]  the public npm registry which is why i'm here today to talk to you about that and we also have a
[211.64 --> 216.22]  enterprise private npm product to help your organization work better with npm and node.
[217.46 --> 221.98]  Awesome and isaac i guess do we have to announce who you are everybody might know right?
[223.02 --> 226.44]  Well just to be on the safe side yeah and because my head is big you know it keeps keeps me
[226.44 --> 234.66]  keeps my ego inflated um i'm isaac i i wrote npm and i work on node i am currently a joint employee and
[234.66 --> 241.02]  um been on the internet since there was an internet and if you want to for the listeners of this show
[241.02 --> 247.42]  who may not have listened to episode 101 uh isaac was on that show we talked about the origins of npm
[247.42 --> 254.46]  and and some different details around that and great show and stuff yeah yeah exactly so i would
[254.46 --> 259.38]  definitely encourage you either before or after this show i'm not sure what matters really to you but
[259.38 --> 264.80]  uh go back and listen to that show for sure but this is episode 113 so we're you know we're 12
[264.80 --> 270.86]  episodes past that so and and i guess a bit has gone on since then too i mean that was let me check my
[270.86 --> 276.66]  uh details here so this the date we did that show isaac may be around the time that you guys have
[276.66 --> 281.80]  started to hear uh some of the details of what we're going to discuss on this show and the the main
[281.80 --> 286.76]  premise of this show i guess it was kind of going to be for lack of better terms like a public service
[286.76 --> 290.24]  announcement like you know something's going on with the with the registry y'all got something
[290.24 --> 293.94]  cool happening you're announcing some news tomorrow today's monday by the way if you're listening to
[293.94 --> 298.12]  this on tuesday you probably heard some you know some big news and you're jumping on board to help
[298.12 --> 305.32]  out so i guess which one of you want to tee off what's going on i guess i'll take the lead there
[305.32 --> 310.38]  um because that has been what's keeping me up at night the last few weeks charlie right because you
[310.38 --> 316.10]  guys sound a little similar uh yeah yeah this is charlie okay cool charlie you should um just just
[316.10 --> 320.12]  just to help distinguish you should talk in an exaggerated new yorker accent there you go hey
[320.12 --> 324.12]  i'm walking here i'm going to talk about programming that's right because you're from the east coast
[324.12 --> 330.70]  right yeah that's right well so is isaac yeah um from connecticut you know so it's a little different
[330.70 --> 336.92]  not very though basically the same place for all you california people absolutely it kind of you
[336.92 --> 342.18]  know new jersey and connecticut are the armpits to new york's brain uh apologies to everyone from
[342.18 --> 345.84]  new jersey and connecticut but i'm from new york it's my obligation to make fun of you
[345.84 --> 347.36]  we're we're in a fight now
[347.36 --> 355.48]  um yeah so getting to the serious things um yeah the the registry has been having some stability
[355.48 --> 362.30]  issues over the last month and again if this is monday but um tuesday there will be a postmortem
[362.30 --> 366.68]  and so at this point if you're listening you've probably already read it and we've put a lot of time
[366.68 --> 373.08]  and effort into figuring out what root cause was and we haven't quite gotten there but we do know
[373.08 --> 380.80]  the solution which is it needs more resources and uh we actually have been uh hosting the registry for
[380.80 --> 386.22]  about the last six months since we acquired iris couch and they've been hosting it forever um and
[386.22 --> 390.96]  isaac will probably talk a little bit more about that later but what we need right now is more
[390.96 --> 397.34]  resources and we do this completely as a community service uh we don't take any money from anyone for
[397.34 --> 402.84]  it and what we're looking to do today is we're starting a crowdfunding campaign for npm so that
[402.84 --> 407.38]  we can keep it running and keep it awesome and so we're asking individuals and organizations to reach
[407.38 --> 414.60]  out uh the website is scale npm.org you can check it out now and i think that's officially the end of my
[414.60 --> 420.82]  um shtick so i'll i'll pass it back to you adam well i want to touch on one thing i mean
[420.82 --> 425.80]  we can go deeper into this but uh you mentioned organizations as well as people can kind of play
[425.80 --> 431.28]  a part in this so i'd notice that i've got early access to this you know i guess non-public version
[431.28 --> 436.68]  yet since it's monday not tuesday yet so i see some some logos are those real logos or those fake for now
[436.68 --> 442.46]  uh no those are those are real logos um those those people have committed and uh we're excited to have
[442.46 --> 448.72]  them as launch partners um we are we are waiting to get the final axe from one of them so i'm going to
[448.72 --> 455.16]  hold off the talk site tomorrow so anybody hearing uh will be like oh what are they talking about
[455.16 --> 463.06]  that's on the website right and when we talk about this crowdfunding um this isn't new right i mean
[463.06 --> 468.50]  this is something that i mean there's kickstarter so this isn't like new things but when andrew and i
[468.50 --> 472.22]  talked a little bit earlier about this because you know andrew if y'all noticed that andrew's not on the
[472.22 --> 477.88]  show uh he couldn't make it today so i had to fly a solo myself but um we talked quickly about this
[477.88 --> 482.08]  and he was like this is really neat i mean doing this i mean getting the community behind
[482.08 --> 486.82]  npm and even like you're branding around like you are npm and that's the community right like
[486.82 --> 492.10]  you're doing this as a public service you know you charlie and no jitsu and the service you're doing
[492.10 --> 497.74]  there and isaac obviously you wrote it and have been working really hard to lift up the community but
[497.74 --> 502.80]  you know it's really a community thing like there's so much new stuff happening that's distributed
[502.80 --> 510.24]  through npm it's crazy i mean and that's kind of why you're in this boat today yeah file this under
[510.24 --> 516.34]  good problems right isaac i i i don't actually think there are any such thing as good problems
[516.34 --> 521.36]  um it's it's a problem that has that indicates that we're doing something right but it it's a
[521.36 --> 527.50]  problem because we're not doing everything right right and uh you know the bottom line is we need more
[527.50 --> 535.70]  resources to get the uh to to make the npm registry stay up and stay good so um that has to come from
[535.70 --> 544.18]  somewhere so we're asking people to uh to help out can we rewind a bit though and and maybe kind of
[544.18 --> 550.02]  talk about the early days of of the npm registry and what that liked and kind of how we got to maybe a
[550.02 --> 561.82]  year ago so um the the original the first pass at the registry which was um very very a very simple
[561.82 --> 567.46]  version of what's up there right now was actually written by um by michael rogers when he worked at
[567.46 --> 573.24]  couch io which later became couch one and then merged with membase and became couch base when that
[573.24 --> 581.70]  happened um and so when they were couch one i believe um they took on hosting of the npm registry
[581.70 --> 591.54]  without uh just as a as a community service and that was um when when iris couch spun off from uh couch one
[591.54 --> 600.20]  under uh jason smith being run by jason smith and jeff jackson um they continued to run the npm registry
[600.20 --> 609.06]  uh and actually developed a um iris npm product and kind of the the the handshake agreement was
[609.06 --> 614.82]  you know you keep running the registry and keep not charging me and you know selling npm registries is
[614.82 --> 622.90]  the you know way that can potentially fund this um and you know that's kind of where we left it uh
[622.90 --> 629.08]  after uh after a bit of time uh they they merged with uh with nojitsu or uh
[629.08 --> 635.78]  purchased by nojitsu iris couch is purchased by nojitsu and um so now nojitsu is selling
[635.78 --> 647.16]  on-prem npm registry clones and um also providing hosting for the uh the public npm registry as a
[647.16 --> 654.70]  community service the interesting thing is that this year in 2013 we've experienced 10x growth
[654.70 --> 662.16]  in most metrics and in fact more than that in some uh the the number of downloads per per month just
[662.16 --> 667.04]  is one rough metric of um of activity and size the number of downloads per month has gone from
[667.04 --> 676.54]  about 13 million per month to you know well over 100 million per month so basically we're at this
[676.54 --> 682.90]  point where the you know the money to continue providing this hosting is not growing quite as
[682.90 --> 689.92]  quickly as the costs of providing this hosting and so the the thought then i mean if i'm reading
[689.92 --> 694.88]  through the details right it sounds like uh charlie on your side to i mean obviously you want to do
[694.88 --> 699.06]  something good you're part of the you're obviously invested in node right i mean that's clear with the
[699.06 --> 705.86]  business name and what you do is is that's evident right but to fund that you've got uh like a
[705.86 --> 712.14]  private enterprise on-premise npm that's one thing and then you've also got npm registry that you can
[712.14 --> 717.92]  installs out is that right so it is an enterprise product that provides some features that you don't
[717.92 --> 725.74]  really get with um even a vanilla clone of the public registry so one of the things that we get as the
[725.74 --> 732.44]  host of the public registry is we have all of the hashed passwords obviously we're never going to
[732.44 --> 736.80]  release those and they're kept in a very secure manner but one thing we can do is replicate
[736.80 --> 744.32]  specific ones of those to our customers private npm so that means that your company when you tell
[744.32 --> 748.62]  someone to point to a new registry they don't have to sign up again they don't have to go through that
[748.62 --> 753.48]  experience they can use the same npm credentials that they have for the public registry on their
[753.48 --> 760.46]  private registry smart yeah um and in addition to that there's some additional policy-based things
[760.46 --> 765.66]  where you only want to have a subset of the registry or you want to know which packages are yours that
[765.66 --> 772.24]  are private um those sorts of higher level large organization problems and so i guess if i'm
[772.24 --> 777.48]  understanding this right uh isaac you'd mentioned that that part of it isn't quite moving as fast
[777.48 --> 784.26]  enough to keep up with the demands to one labor servers just in general the resources necessary to
[784.26 --> 790.36]  keep the npm registry to its you know maximum potential keeping up time right and that's we've kind of
[790.36 --> 794.94]  gotten to this point now where we don't have enough man hours and enough servers to kind of
[794.94 --> 804.02]  go around to make it as uh as responsive as it needs to be right exactly and in addition to that um
[804.02 --> 810.18]  you know what also comes along with 10x growth in addition to you know additional uh resource
[810.18 --> 816.78]  utilization and so on is that there's more people depending on it so you know a smaller hiccup of
[816.78 --> 822.66]  of service has a much bigger impact on a much bigger number of people whereas previously you
[822.66 --> 826.84]  know if the npm registry did go down for a few minutes chances are nobody would get bothered with
[826.84 --> 833.48]  it because you know that's just like statistics um whereas now i mean even even relatively minor
[833.48 --> 837.54]  outages end up impacting a lot of people calling they're causing their builds to break and you you
[837.54 --> 843.72]  know there's a lot of uh a lot of impact from that now yeah i've been noticing on the npm js twitter
[843.72 --> 849.76]  handle too is it the you that run that or is it you charlie you isaac and one other person isn't
[849.76 --> 858.20]  that right npm the npm twitter handle um is npm yeah i mean didn't it's self-aware i mean we just
[858.20 --> 864.70]  service it yeah we're just helping it out i mean that's i don't really know i don't really understand
[864.70 --> 869.36]  your question oh like who is behind it because what i was going to say was that i've seen lately
[869.36 --> 874.92]  you know kind of responding back to so you know certain people and saying okay you've got an issue
[874.92 --> 879.22]  here there's a package here we're working on that and there's issues being obviously filed against the
[879.22 --> 885.64]  the github issue uh database and so you're playing i guess triage and support to the community through
[885.64 --> 889.90]  twitter and there's you know over the last few weeks you've had some some scenarios where you've
[889.90 --> 895.60]  had to you know kind of look at what's going on and apply some fixes i was trying to figure out who
[895.60 --> 900.66]  who runs it i was trying to key off that basically oh yeah yeah um i i guess the uh
[900.66 --> 906.42]  wasn't sure who's doing the talking i was being slightly tongue-in-cheek the the npm uh twitter
[906.42 --> 912.48]  account is the the the character of npm and um npm loves you
[912.48 --> 922.36]  npm more so much more than any of us do that's for for damn sure i see i see uh i'm not really sure to
[922.36 --> 927.42]  go where to go with that one but so we got we got a it's kind of like it's kind of like when my mom
[927.42 --> 933.62]  was santa claus like she right you know she asserted that santa claus really existed because
[933.62 --> 940.66]  he's an important part of her psyche right right gotcha gotcha um so we've got a crowdfunding
[940.66 --> 948.36]  goal of two hundred thousand dollars um i guess you probably expect this question but what does the
[948.36 --> 954.18]  money get used for since we're talking about resources so we expect um the the server bills
[954.18 --> 959.62]  for npm right now are about 10 grand a month um and that's actually probably going to grow a little bit
[959.62 --> 967.62]  as we start to move off some additional things um because on those servers we just really can't do
[967.62 --> 975.70]  anything that's io intensive anymore um for example uh when we tweet out the statistics of npm every month
[975.70 --> 981.40]  those used to be crunched from log files that sit on those servers on those servers can't do that
[981.40 --> 986.86]  anymore we need to have a separate log server that all that io gets done on we need to have a hot spare
[986.86 --> 993.72]  that's in continuous replication not just in case there's a crash but in case um the disk size continues
[993.72 --> 997.78]  to grow the way that it's been growing over the last few weeks uh so we have to regularly start
[997.78 --> 1004.64]  running compaction on couchdb to keep that disk size down because from a couchdb
[1004.64 --> 1011.12]  uh perspective and that this is sort of an interesting story um the outage on november 13th
[1011.12 --> 1016.98]  where we actually switched over to multi-master jason and i were in vancouver to go to couch comp
[1016.98 --> 1023.84]  so so we woke up to go to a couchdb conference with couchdb falling over and with a room of couchdb
[1023.84 --> 1031.48]  core committers nobody really knew what was going on because the attachments were never really meant to be
[1031.48 --> 1039.90]  99.97 percent of all bytes in the database which is basically what you get in npm so we just run
[1039.90 --> 1046.74]  into these really strange scenarios that um you just don't see anywhere else so we we can throw more
[1046.74 --> 1052.20]  hardware at it for now and it works just fine um and then you know isaac is leading the charge on
[1052.20 --> 1057.40]  uh refactoring things to get those out of the out of the registry and into a cdn somewhere
[1057.40 --> 1065.18]  and you mentioned i guess a bit earlier that your your hope is that this fundraiser is more of like
[1065.18 --> 1069.36]  a shim for now it's not a long-term solution it's more of like a here's how the community can help
[1069.36 --> 1075.44]  give back to keeping npm up uh or keeping the registry up and and things going smoothly or at
[1075.44 --> 1080.78]  least having a a plan to do that at least monetarily and then the hope is that the private enterprise
[1080.78 --> 1087.06]  npm product later on will help facilitate that through you know node being able to or node just
[1087.06 --> 1093.56]  to being able to um get that product out there and be sustainable to supply the needed funds to run it
[1093.56 --> 1100.34]  absolutely we've done some sales of our private npm products so far um that's really starting to scale
[1100.34 --> 1104.96]  up and i think by this time next year it's going to be a completely sustainable business
[1104.96 --> 1109.76]  um and we'll be able to provide this you know service to the community uh the way that we've
[1109.76 --> 1117.92]  been doing uh up until now what type of um i guess who is it that uses what kind of scenario is
[1117.92 --> 1124.82]  is can you best paint that would use this private enterprise npm registry i like to paint it in the way
[1124.82 --> 1134.48]  that we used it at nojitsu because we've had um the most all of the npm use cases we've had them so
[1134.48 --> 1141.74]  all of our stack is node so we want to encourage this same idea of modularity and innovation through
[1141.74 --> 1148.04]  modularity in the organization so that um one of our engineers can say i want to write a module to do x
[1148.04 --> 1152.68]  that's sort of internal something that wraps our api in some unique way they can name it publish it to
[1152.68 --> 1158.86]  the private npm and feel that same sense of ownership that they have in their open source code
[1158.86 --> 1165.02]  at the same time we also run a platform as a service product that runs uh in a different data
[1165.02 --> 1170.44]  center than the npm registry i would say that basically all uh platform as a service products
[1170.44 --> 1177.70]  run in a different data center than the npm registry which is soft layer us east and so we run a full
[1177.70 --> 1185.70]  replica of the public registry in joyance us east data center to remove downtime in case the public
[1185.70 --> 1192.84]  registry does go down and then also to reduce latency because all of those package gets are going
[1192.84 --> 1200.04]  over the local intranet and not going out to the public internet so any gamut of of those things there
[1200.04 --> 1208.78]  um could be helpful so if you're having use node um bu rackspace or joint or heroku or any of those
[1208.78 --> 1214.98]  types of companies running a public replica in the same way that they run apt or yum replicas is super
[1214.98 --> 1221.56]  valuable and for private organizations it's a way to scale and distribute the workload of your node
[1221.56 --> 1225.76]  js code base in an organic way throughout your organization the same way that it's distributed
[1225.76 --> 1231.10]  organically throughout the node community itself so i guess with the enterprise piece of this is
[1231.10 --> 1234.76]  assuming that a lot more people are in the enterprise are picking up node and using it in
[1234.76 --> 1239.34]  in ways that their their organizations are going to use this and want to publish private
[1239.34 --> 1245.76]  packages to be able to serve and and that's kind of hinged on that fact too is that growth still
[1245.76 --> 1250.62]  going the direction you guys want to see it go um yeah i mean that's that's definitely the way that
[1250.62 --> 1256.30]  things are going i think that uh if you look at how npm is being picked up and how node is being picked
[1256.30 --> 1260.82]  up at companies like yahoo and walmart um you know they are using it internally to manage their
[1260.82 --> 1267.38]  dependencies and um this kind of a enterprise product makes it a lot easier and more accessible
[1267.38 --> 1273.36]  for more companies to do that you know like a yahoo will probably just hire the the people that they
[1273.36 --> 1279.08]  need to manage that in-house but they're gigantic and there's a lot of companies that are a little
[1279.08 --> 1285.18]  bit smaller or um you know even if they are of the same size they have you know a little bit less of a
[1285.18 --> 1291.46]  a you know devops culture right and i think you know for example uh walmart is is a perfect example
[1291.46 --> 1297.54]  of that they have um a lot of technical work that they're doing in node they have a big you know
[1297.54 --> 1302.88]  several teams that want to share code and interoperate and npm makes that extremely easy to do
[1302.88 --> 1310.56]  so as long as they can remove themselves from the um you know from any impact of the public registry
[1310.56 --> 1315.12]  having any problems it makes a lot of sense for them on that you know from like a safety
[1315.12 --> 1320.10]  net point of view but also they want to be able to publish code that you know just publish to other
[1320.10 --> 1327.70]  teams inside their own firewall and be very strict about which programs they allow their developers to
[1327.70 --> 1333.76]  to pull in so for example they can have license auditing or you know even security reviews and so
[1333.76 --> 1339.96]  forth and that's not something that we're likely to add anytime soon to the public registry so having
[1339.96 --> 1345.24]  that uh but but it's a big feature for um for enterprises who are using npm internally
[1345.24 --> 1352.84]  you know we uh we have this weekly email we send out and just talking about walmart we linked out to
[1352.84 --> 1358.92]  something on the joint uh i think it's their i think it's the blob it was a video and it was this
[1358.92 --> 1366.98]  fellow named uh a ray hammer yeah how do you say it erin erin okay erin yeah yeah and uh i was like
[1366.98 --> 1371.16]  you know my eyes are glazing over it and obviously at some points but i'm like you know the billion
[1371.16 --> 1376.36]  dollar question which is how you how more how walmart's using um how walmart's using node and
[1376.36 --> 1383.52]  the node platform i mean those are big companies and but how are the i guess not walmart's and not
[1383.52 --> 1388.64]  yahoo's or are there just a lot more walmart's and yahoo's we don't know about that that uh will
[1388.64 --> 1394.06]  utilize an enterprise system that will pick this up and use it the way we think they should be using it
[1394.06 --> 1399.60]  well i mean what we're seeing is that node is becoming kind of the the de facto place for the
[1399.60 --> 1405.50]  de facto platform for doing a lot of these kinds of uh kinds of tasks um that are extremely data
[1405.50 --> 1411.80]  intensive and and you know need to do a lot of io and kind of be this this sort of central hub middle
[1411.80 --> 1421.26]  layer um and you know condi nast is uh is using it the wall street journal the uh new york times um
[1421.26 --> 1427.22]  you know lots and lots of them if you go to uh nodejs.org slash industry that's actually that's
[1427.22 --> 1433.26]  a pretty small subset in fact of the the companies that are using node in a in a really big way and
[1433.26 --> 1439.78]  there's some really well uh well-known names there on that list basically those are just the subset
[1439.78 --> 1445.48]  that have noticed this page and decided to send me a poll rec to uh to put them on it so you know it's
[1445.48 --> 1452.52]  there's a step to get on this page and we have honestly no clue um how many people are using
[1452.52 --> 1456.04]  node or exactly what they're using it for just because that's you know the nature of open source
[1456.04 --> 1463.84]  but uh being at joint and uh you know getting involved in in some production issues and uh
[1463.84 --> 1471.18]  things that come up with our customers i mean yeah node is node is very big at a lot of companies that
[1471.18 --> 1476.00]  are of the similar size to uh to walmart i think walmart's probably one of the biggest they're one
[1476.00 --> 1481.08]  of the biggest companies period right yeah but there's a lot of companies that that have a need
[1481.08 --> 1490.78]  for um for you know internal npm services and and have the money to pay for it so i guess this has been
[1490.78 --> 1497.86]  a kind of maybe a 12 minute rant or so on whether or not i guess the the core crux of the question was
[1497.86 --> 1503.00]  you know do you guys both truly believe that and obviously you know no jitsu and charlie you do
[1503.00 --> 1507.78]  because you've you're building this product but you know is is the private side of this going to be
[1507.78 --> 1512.88]  able in the future to sustain it i mean so that's that's the goal and how you think it's a year away
[1512.88 --> 1518.70]  from that or what is the what are the challenges to get there i think we actually could be as close
[1518.70 --> 1525.50]  as six months away from that um the challenge for us is really streamlining the the process here
[1525.50 --> 1532.58]  and right now the the big blocker for us is that um the registry is quite large and so moving that
[1532.58 --> 1540.56]  around for customers is something that can't be done in a please enter your your login um and your
[1540.56 --> 1547.36]  credit card and here's an npm registry for you without expending um a large amount of resources
[1547.36 --> 1555.48]  because we need to copy over uh roughly 100 gigabytes to a new server when that happens and so that's a
[1555.48 --> 1563.60]  a function of um really the the disk io that couch db needs we can't put that on say an ebs volume uh
[1563.60 --> 1569.66]  or a uh some sort of network storage of some kind uh because that is just not fast enough couch sort of
[1569.66 --> 1576.16]  tends to get behind itself or ahead of itself with these reads and writes um when the disk io is not fast
[1576.16 --> 1582.50]  enough so we have a process now where someone can sign up and we can get something provisioned within
[1582.50 --> 1590.00]  48 generally 24 hours but making that easier and getting those those sales done faster is our main
[1590.00 --> 1597.24]  focus right now on that product well let's pause for a minute and give a shout out to our sponsor top
[1597.24 --> 1603.26]  towel there'll be sponsoring the show for another month so good news there and certainly appreciate the
[1603.26 --> 1608.98]  support of top towel to the show uh i've been talking to brendan uh their co-founder and cto and
[1608.98 --> 1614.42]  i kind of mentioned before that i wasn't quite sure what to expect but you know since then brendan and
[1614.42 --> 1618.50]  i've had a number of conversations and he's kind of really helped me understand what their mission is and
[1618.50 --> 1623.00]  i gotta say these guys are the real deal they're they're engineers themselves you know they built the
[1623.00 --> 1628.70]  entire company around engineering from top to bottom they're not non-technical recruiters trying to
[1628.70 --> 1633.64]  pimp developers for lack of better terms they're a network of elite engineers from all around the
[1633.64 --> 1638.42]  world who work with some really awesome clients and for those of you out there who are freelancing
[1638.42 --> 1643.24]  or like to test out freelancing you gotta check out top towel you can work on special projects with
[1643.24 --> 1650.66]  companies like airbnb rc ideo and many others you can work remotely or on a beach which is uh which is
[1650.66 --> 1654.84]  always fun or anywhere in the world and to get started you just gotta go to top towel.com
[1654.84 --> 1660.34]  slash developer and click join the best and because they want to work with only the best
[1660.34 --> 1666.44]  team engineers out there you've got uh they've got a well thought out four stage screening process that
[1666.44 --> 1671.62]  they that they use that begins with a personal skype conversation they get to know who you are
[1671.62 --> 1675.78]  they introduce you to top towel and kind of help you understand what their mission is and see if you're
[1675.78 --> 1681.58]  a fit and from end to end the entire screening process includes an english speaking test a timed
[1681.58 --> 1688.16]  algorithm test technical interviews with core top towel engineers as well as a test project and once
[1688.16 --> 1692.28]  you've made it through the screening process the sky is the limit and if you think you have what it
[1692.28 --> 1697.18]  takes head to top towel.com slash developer to get started tell them the changelog sent you
[1697.18 --> 1703.58]  isaac i know you kind of touched a little bit earlier on like the early versions of it but uh you know
[1703.58 --> 1709.38]  can you kind of give me for those out there who would totally be interested in this part i certainly am
[1709.38 --> 1715.40]  but uh how does npm currently work like what is the current setup and when we get these funds and
[1715.40 --> 1719.78]  this crowdfunding is successful which it's going to be because i know you guys are awesome so this is
[1719.78 --> 1723.60]  community is going to love this but totally going to support it but you know when we get to the next
[1723.60 --> 1727.74]  version of it how how's it work now and how's it going to work when when we get fully funded for
[1727.74 --> 1739.12]  this uh this fundraiser so um in a nutshell the npm registry is a couch db um with a little bit of uh
[1739.12 --> 1743.92]  little bit of rewrite action you know kind of pointing at certain like shows and views and such
[1743.92 --> 1752.84]  um when you uh when you publish a package that's doing a put into the couch db and uh there's a
[1752.84 --> 1759.04]  bunch of rules that you know make sure that it's following a few basic guidelines and and whatnot and
[1759.04 --> 1767.48]  not doing anything uh insecure set up in the validate doc update function there's also um the actual
[1767.48 --> 1771.74]  tarball which contains the contents of the package and then that's added as an attachment on the
[1771.74 --> 1778.12]  document so there's one document per package which has like little like a versions um versions object
[1778.12 --> 1784.16]  that has the individual package.json data for each published version and then also has a uh
[1784.16 --> 1792.92]  a tarball as an attachment so the problem is that couch db is good at handling attachments but it's not
[1792.92 --> 1801.46]  great at handling as much attachment load as we've put into it um and we we've kind of reached well
[1801.46 --> 1806.62]  past the breaking point of of what this database is actually good for what it's great for is storing
[1806.62 --> 1815.16]  um json blobs and doing map reduce over them like couch db actually totally totally is great for that and
[1815.16 --> 1820.44]  you know they also have like really nice restful apis really which is obviously a big win when you're um
[1820.44 --> 1826.88]  you know when you're when you're doing stuff with node which you know npm is a just a node program
[1826.88 --> 1834.70]  so what the plan is is um one thing that i've been kind of working on as a a sort of side project
[1834.70 --> 1840.54]  thinking about and not really gotten too serious about until relatively recently um is this project of
[1840.54 --> 1848.72]  taking all of the attachments out excuse me and putting them into uh joyance uh cloud hosting service
[1848.72 --> 1856.30]  called manta so this gives us a number of benefits um first and foremost if we can uh if we have all
[1856.30 --> 1864.26]  the attachments in one place it's very easy to make that the origin server for a cdn network um we have a
[1864.26 --> 1873.06]  i have an offer from max cdn to um provide free cdn services uh in exchange for you know a little bit of
[1873.06 --> 1879.34]  like link love and and so on and so that's that's going to be really awesome but in order to do that we need
[1879.34 --> 1886.90]  to get everything in as as the uh you know with behind the the area at a single origin server url so we can
[1886.90 --> 1894.94]  say okay map this path to this path in the cdn so i've been working on um the process to make sure that we can
[1894.94 --> 1900.04]  get things out of there but what we can't do is we can't go through and replace everybody's npm client overnight
[1900.04 --> 1906.32]  so any changes that we make to the actual client application have to be done and then published
[1906.32 --> 1912.32]  with a uh with a node release and then you know we need to sit on it for like six months wait for the
[1912.32 --> 1918.68]  request to the old url to kind of taper off it's just like very very long process right so uh what i've
[1918.68 --> 1923.68]  been trying to figure out how to do is basically how to move forward with this without um without
[1923.68 --> 1932.36]  breaking backwards compatibility at our our api layer so um what we've done is or what i'm planning
[1932.36 --> 1936.84]  on doing is once i get everything moved into manta there's already kind of a first pass of this when we
[1936.84 --> 1943.64]  uh banged on it a little bit and found a few problems and kind of circling back and and updating some of
[1943.64 --> 1952.76]  that stuff um once uh once that's in place the uh uh the url that tells the url in the metadata of
[1952.76 --> 1959.30]  the couch db that uh that tells the npm client where to go download the uh the tarball from basically
[1959.30 --> 1964.86]  each time it gets an update from couch it's going to take that tarball put it into manta where it's
[1964.86 --> 1971.76]  behind the cdn and then change the the url to point to the cdn url rather than the the direct
[1971.76 --> 1979.04]  couch db url once we do that then there's a couple of options that we have um newer npm
[1979.04 --> 1983.30]  clients already know how to interpret this there's a i don't know if you want to call it a bug it was
[1983.30 --> 1988.30]  actually an early workaround for a bug that no longer exists but like you know that's how it goes
[1988.30 --> 1996.28]  with code um there is a shortcoming of the previous versions of npm client where it will always try to
[1996.28 --> 2004.38]  fetch the tarball from the same um from the same registry host no matter what so we need to do some
[2004.38 --> 2009.62]  other magic and we've kind of explored different ways that we can either modify couch db or uh take
[2009.62 --> 2015.94]  some uh liberties with the way that the npm registry couch app works such that it will still pull those
[2015.94 --> 2023.44]  attachments from um from the cdn rather than from an attachment url on the couch db once we're at that
[2023.44 --> 2028.44]  point we can actually remove start removing those attachments altogether and now um and even before
[2028.44 --> 2032.44]  we remove them altogether as long as those requests aren't coming in for them it'll be a lot easier
[2032.44 --> 2037.62]  because um there won't be as much disk io and it seems like it's a lot of orchestration around this i
[2037.62 --> 2042.28]  know that i mean there's nothing to compare to but just when you move a site from one server to another
[2042.28 --> 2045.98]  there's a lot of orchestration around that and this is like that times a million right like it's
[2046.70 --> 2052.56]  you know everybody banging on npm you know either installing or deploying or or you know pushing up
[2052.56 --> 2059.30]  their own packages so how does the community i guess how i mean is this something that you
[2059.30 --> 2064.94]  need to orchestrate in some sort of like syncopated manner does how do how does the world fall in place
[2064.94 --> 2071.98]  to your plan here well i i think basically everything that we're planning on doing we can do with um
[2071.98 --> 2078.06]  with little or no downtime i mean with something like npm if we do need to have some kind of downtime to
[2078.06 --> 2082.46]  restart a server or or you know change the way things operate you really need to make sure that
[2082.46 --> 2087.30]  that counts and so you kind of want to plan everything that you need to do and get it ready
[2087.30 --> 2091.76]  and then like minimize the downtime so you can be back up and serving requests right away in this case
[2091.76 --> 2096.50]  i don't think we'll even need that um because of just the nature of the way that couch operates we
[2096.50 --> 2104.16]  already have two um two replicas that are in continual um uh peer-to-peer replication with one another
[2104.16 --> 2110.82]  and then a load balancer in front of them so you know we can start operating on one of them either
[2110.82 --> 2115.64]  take it out of rotation and then do the thing and put it back in and and so on i mean there shouldn't
[2115.64 --> 2120.22]  be any interruption of service throughout the way throughout all of this and in fact most npm users
[2120.22 --> 2125.66]  won't even notice that anything happens once the cdn starts being the target for all of those tarball
[2125.66 --> 2132.04]  downloads um users in you know especially users in southeast asia and australia will notice that things get
[2132.04 --> 2140.74]  quite a bit faster but um you know otherwise for the most part it should be it should be only increases
[2140.74 --> 2147.50]  in stability as we move forward just because i'm trying to really stay on on point with this one but
[2147.50 --> 2153.90]  when you say clients what you mean by that is like me at my computer either installing or pulling from
[2153.90 --> 2161.12]  npm right yep okay just i mean any anytime you type npm whatever on your command line and it has to go
[2161.12 --> 2164.96]  to the registry so that's i mean that's a lot of application that's a lot of uh different commands
[2164.96 --> 2168.96]  but mostly you're either you're either downloading metadata and looking at it you're downloading
[2168.96 --> 2175.68]  tarballs and installing them or you're pushing stuff up to the registry so um yeah all of those
[2175.68 --> 2180.82]  operations whenever i say npm client i mean like the the program called npm right right and so with
[2180.82 --> 2187.16]  that you mentioned an update that has to happen for the client so i guess uh those who may not go and
[2187.16 --> 2191.40]  pull down the latest version of it whenever you kind of start to orchestrate this this plan here i
[2191.40 --> 2198.64]  mean is it uh how do you you know i guess if i don't upgrade or update my npm what happens to me
[2198.64 --> 2208.86]  well i mean for at least you know until everybody else also moves on you should be fine uh i i have a
[2208.86 --> 2214.12]  very strong feeling that like you know it's when people are using your program in production it's
[2214.12 --> 2221.88]  kind of a dick move to to break it so um and that that dramatically slows us down sometimes um
[2221.88 --> 2227.20]  but on the plus side you know it means that things keep working for people and that they don't ever
[2227.20 --> 2232.54]  really notice so what we do is we we make whatever change we need to make in the client i i usually set
[2232.54 --> 2239.40]  like a six month reminder on my calendar to revisit the the issue and then uh you know we we take a look
[2239.40 --> 2244.34]  at it and and see if we're still getting requests to that old url or or what have you and if we can
[2244.34 --> 2248.60]  tell that it's uh you know very very small percentage of users who won't be impacted we might just go
[2248.60 --> 2254.76]  ahead and make the change and you know okay a couple people have to upgrade um but as long as they're at
[2254.76 --> 2260.10]  that point they they have had ample opportunity so it's it's not such a their own fault right move on
[2260.10 --> 2266.54]  right yeah gotcha well i wouldn't say it's their fault but um but it's reasonable to expect that if
[2266.54 --> 2270.30]  they haven't upgraded at least it's easy enough for them to upgrade by this point you know there's
[2270.30 --> 2274.94]  there is a version of npm that works with their version of no that has access to this new thing
[2274.94 --> 2279.68]  and and so it's not an issue man we obviously see some of the reasons why it's important but i want
[2279.68 --> 2283.68]  to hear from you guys you know what what is it that's important why the community steps up to
[2283.68 --> 2288.24]  support it's like you got this branding around like it's your npm you know you want to keep it up
[2288.24 --> 2293.28]  you want to keep it fast you know what is what is the the importance i guess of the community
[2293.28 --> 2300.18]  stepping up to help support this effort of keeping npm running um i'll jump in on there on that um
[2300.18 --> 2306.58]  isaac and i have actually talked about this a lot because the you know he has obviously very excited
[2306.58 --> 2315.74]  about this migration to mansa as am i but from a like standpoint as us as a company um that's actually
[2315.74 --> 2322.50]  a lot of like long ball labor costs that are hard to to ballpark and it turns out actually the person
[2322.50 --> 2329.70]  who's most suited to do this work on the couch db side is jason our cto and so from our perspective
[2329.70 --> 2334.72]  we have this thing that we run which we're really happy to run but we also have this product that
[2334.72 --> 2341.76]  we're building that also needs jason's time and so if we're going to prioritize his time to you know
[2341.76 --> 2348.26]  make that the thing that needs to get done and takes priority over our product um we you know need
[2348.26 --> 2352.54]  to subsidize that in some way going forward and that's where we say our costs are doubling not
[2352.54 --> 2356.20]  just servers but labor to take us to the next order of magnitude
[2356.20 --> 2364.00]  so let's talk about uh let's talk about the the actual fundraiser itself we talked a little bit
[2364.00 --> 2369.24]  earlier about the the goal that you have said and like any crowdfunding you've got many levels and
[2369.24 --> 2373.72]  you've got the opportunity for not only individuals but also companies to take part in this and you've
[2373.72 --> 2378.16]  got a couple that are on the site now which we can't mention because we're not really sure if at
[2378.16 --> 2383.68]  least one of them is so i'll just leave them both out the gate but um you know talk about how i guess
[2383.68 --> 2390.08]  maybe the last when did this idea come about to to do a fundraiser to make this effort possible not
[2390.08 --> 2395.14]  just much acid the asking the community for their support but you know actually turning into a crowd
[2395.14 --> 2401.22]  funding with these levels and what you guys are doing with it um so the the person who actually
[2401.22 --> 2409.86]  suggested this to me was it was actually at couchdbconf um what was that 10 days ago and it was i was on a
[2409.86 --> 2417.50]  call with uh with nuno job uh who is uh congratulations nuno and paula they just had a baby um he was
[2417.50 --> 2422.12]  talking with me and we were talking about how the downtime was just taking up it literally sapped our
[2422.12 --> 2427.70]  whole week and he had just said look you know um you should do something like what travis did
[2427.70 --> 2434.58]  for their uh crowdfunding campaign so travisci ran a successful crowdfunding campaign in 2012 and
[2434.58 --> 2444.54]  12 i believe um or maybe it was through 2013 called the love.travisci.org and the parallels were
[2444.54 --> 2450.12]  were really obvious there um you have this thing that is deeply integrated into the community that
[2450.12 --> 2458.32]  people rely on and is also on its way to becoming a sustainable product but uh you know we need help
[2458.32 --> 2463.32]  to get there uh just like they did and i think they've done a lot with uh the money that they
[2463.32 --> 2468.58]  raised last year and so with those parallels in place it just became obvious that this is what we
[2468.58 --> 2474.60]  need to do and so we moved very very quickly to get this out the door because we didn't want to lose
[2474.60 --> 2481.00]  the or didn't want people to forget the pain that they felt when this happened because it's very easy
[2481.00 --> 2487.88]  um with a service that you depend on to be mad at it when it's down and then just forget about that
[2487.88 --> 2493.54]  later on and then just be mad again later uh when it goes down again without really thinking about
[2493.54 --> 2499.52]  okay well why did it go down in the first place you know is that a symptom of a greater problem can that
[2499.52 --> 2505.10]  be prevented and not in the way that um you generally probably read post-mortems for the services that
[2505.10 --> 2511.84]  you use but in a holistic community way because this service again is is not um for profit in any way
[2511.84 --> 2521.50]  i'm going to read a tweet i saw actually from sven lito he's a a hacker on uh at at uh at hoodie which
[2521.50 --> 2525.96]  was recently on the show and also on bauer and uh something he had tweeted i don't know if it was
[2525.96 --> 2531.52]  actually from him or not maybe it was an overheard who knows but he said uh as a developer i want super
[2531.52 --> 2537.76]  fast npm everyone always so everyone wants it fast right they want they want it fast they want it now
[2537.76 --> 2543.14]  so that's that tends to be that and i think you know charlie you and i talked a couple days ago
[2543.14 --> 2548.80]  kind of prepping for this call and i was just thinking like you know as somebody in open source
[2548.80 --> 2554.52]  right you you know you just expect the service to be there but you forget you know what's behind it
[2554.52 --> 2559.90]  all like you guys just talked about this entire re-architecture that involves you know brand new
[2559.90 --> 2565.44]  cool blazing awesome stuff from joint and max cdn giving their support and all these different
[2565.44 --> 2570.80]  things you have to do to orchestrate this stuff and you know those who are using grunt or bauer all
[2570.80 --> 2576.30]  these newer things that are kind of front-end tools that uh you know maybe they're not they're not used
[2576.30 --> 2581.04]  to what a registry might be because some front-end developers are kind of getting into using you know
[2581.04 --> 2585.06]  something like ruby gems would be like that's that might be newer to them and they just think oh
[2585.06 --> 2590.26]  it's a service it'll be there but you know all the while you guys as a business have to support this
[2590.26 --> 2595.88]  thing and you isaac have to you know work really hard to you know deviate and kind of coordinate
[2595.88 --> 2604.22]  things for the community to keep npm running well and fast and it's it's tough i mean this is probably
[2604.22 --> 2613.38]  proof of that right well you know big things are fun too um yeah yeah right i mean if you're gonna
[2613.38 --> 2623.02]  have a hard problem make it a fun hard problem right um so i guess maybe some details quickly
[2623.02 --> 2628.20]  about i don't know how important it is to mention some of the different goals you guys have but the
[2628.20 --> 2633.78]  the entire overall goal is two hundred thousand dollars you're trying to raise the campaign is
[2633.78 --> 2639.18]  in 30 days what happens i guess with the traditional crowdfunding like let's say you don't fund the full
[2639.18 --> 2645.26]  230 days what what are some of the takeaways or changes that you know is there is is it all or nothing
[2645.26 --> 2650.82]  what's what how is this crowdfunding uh goal a little different than maybe others might have been
[2650.82 --> 2659.44]  so we opted to go outside of say um kickstarter or indiegogo because um if we got 180 or 100 you
[2659.44 --> 2664.56]  know that's still going to get us further along than we are now and this is such an important public
[2664.56 --> 2669.78]  utility that we didn't want to be an all or nothing place which is why this actually runs through this
[2669.78 --> 2676.94]  is totally custom uh site that we've built at nojitsa over the last week um sort of coincided with a new
[2676.94 --> 2682.48]  version of our billing system which makes doing this very very easy uh and considering that we're
[2682.48 --> 2688.44]  you know going to launch with a pretty significant um portion of this already committed from companies
[2688.44 --> 2694.44]  i'm feeling confident that we'll hit the goal but that is obviously always a concern and from our
[2694.44 --> 2698.16]  perspective if we don't get there we're going to do as much as we can with the money that we get
[2698.16 --> 2706.76]  so you know the registry costs will be subsidized that way um the other important thing to to realize is
[2706.76 --> 2712.12]  that we're also a company and that this uh when you play that and this probably doesn't often get
[2712.12 --> 2718.20]  talked about in a show about open source you talk about signaling um when you when you do run a
[2718.20 --> 2723.06]  company and this even just the support that we've gotten now is a very positive signal for what we're
[2723.06 --> 2729.00]  doing and i think that that's going to be reflected in uh how our business operates and you know raises
[2729.00 --> 2734.68]  capital over the next six months and that's the a big impetus for this is to really demonstrate to
[2734.68 --> 2739.10]  the community the larger community the larger investment community the larger software community
[2739.10 --> 2745.50]  that there is something special going on here and it's not just a lot of um hand waving and um
[2745.50 --> 2751.26]  china market internet scale words getting thrown around since we're throwing around a couple words i
[2751.26 --> 2755.34]  was thinking about something as i was driving around thinking about this call earlier in my day today and
[2755.34 --> 2760.12]  i was thinking if i had to tell somebody something i'd just say put your money where you put your
[2760.12 --> 2763.98]  packages i'm not sure if that's accurate or not you didn't say it's not your marketing thing but
[2763.98 --> 2769.42]  i was thinking that's pretty accurate what do you think put your money where you put your packages
[2769.42 --> 2777.64]  yeah that's that's a that's a good uh good slogan all right cool uh awesome you know please please
[2777.64 --> 2783.30]  please don't put your money in npm literally like don't don't publish bitcoins yeah don't do that
[2783.30 --> 2790.16]  it is not secure for that we are not a bank uh you know one thing that was on this page too and i want
[2790.16 --> 2794.80]  to just point this out to those that are maybe at the page right now just to kind of recap on the
[2794.80 --> 2799.72]  on the url this is going to be and i want to ask you one question about this too once i mention this
[2799.72 --> 2807.70]  but the url is scale npm.org but on that page uh about halfway down where it says why is this important
[2807.70 --> 2815.12]  um i've been on this page i don't know how long maybe a half hour i think or a couple hours i don't know
[2815.12 --> 2819.54]  maybe i've had it sitting here that's i think it's like an hour and since that hour's passed there's
[2819.54 --> 2829.52]  been over a quarter million uh packages downloaded like this thing is like it's on fire it's crazy yeah
[2829.52 --> 2836.16]  it's um and that's one of the things that you know is really nice about the the data statistics that we
[2836.16 --> 2842.96]  get um is that we can go out and crunch that data and infer it um that way so what's behind the i mean
[2842.96 --> 2850.78]  obviously url is url but what's the the significance of scale npm i mean obviously you're scaling it but
[2850.78 --> 2857.94]  why not just opt for a subdomain or something like that like uh like love.travisci.org.com i think
[2857.94 --> 2868.20]  it's .org for their their open source uh no comment okay gotcha uh let's see uh that's i think that's
[2868.20 --> 2873.42]  pretty much all i wanted to ask you guys i guess about about what uh what's happening here i think
[2873.42 --> 2878.42]  it's just pretty neat that um that you're doing this i think it's i mean anytime you get a chance
[2878.42 --> 2884.20]  to involve the community i know they the community always ends up uh you know one being excited about
[2884.20 --> 2889.18]  what you're doing for but then also just appreciating um you know just appreciating the
[2889.18 --> 2893.84]  fact that you let them take part so i mean even if it's five bucks or a hundred bucks or whatever it is
[2893.84 --> 2898.86]  whatever you can afford to uh to support this we definitely would love you to do that that's why
[2898.86 --> 2901.82]  isaac's on the show that's why charlie's on the show that's why they're working really hard for this
[2901.82 --> 2911.02]  so go to scale npm uh dot org to to check that out and uh and give your support but you know a couple
[2911.02 --> 2916.22]  traditional questions we ask on the show which i don't think it's uh a problem here and isaac i know
[2916.22 --> 2921.24]  you asked or answered a couple before but if you weren't charlie i guess i'll ask this question for you
[2921.24 --> 2928.28]  which is if you weren't uh i guess on this call with me right now and isaac talking about this and
[2928.28 --> 2934.34]  you weren't building no jitsu what would you be doing uh if i wasn't building no jitsu that's that's
[2934.34 --> 2940.14]  that's a big one um because i've been doing that for more than three years um i would probably still
[2940.14 --> 2945.02]  be writing node software somewhere i would probably still be working on open source things that's what
[2945.02 --> 2952.02]  drew me to node and to start not just you in the first place and i guess isaac if you weren't in
[2952.02 --> 2956.08]  in the middle of this crowd fundraiser and doing what you're doing with node i think you answered
[2956.08 --> 2961.90]  this a couple shows back but has your answer changed what else would you be doing what was my answer last
[2961.90 --> 2966.80]  time i don't i don't remember even uh i think you said you were going to be sailing that's been a popular
[2966.80 --> 2973.80]  answer no no no no i wouldn't have i wouldn't have said that i'm sure i'm terrified of being out in the
[2973.80 --> 2977.20]  ocean it will kill you it's full of monsters well make a new one up what would you be doing
[2977.20 --> 2985.98]  uh what would i be doing um i don't know i would probably be uh going to yoga practice more and um
[2985.98 --> 2993.22]  i don't know maybe living somewhere warmer i think in 101 you were talking about how it was kind of
[2993.22 --> 2997.74]  happenstance that you didn't have a job and it was kind of like you had this extra two or three months
[2997.74 --> 3003.60]  just kind of sitting there and you're like ah i'll build something so i guess maybe it'd be around that
[3003.60 --> 3009.62]  like if you'd never actually built npm and never got into uh node and took over the maintainership
[3009.62 --> 3014.94]  of it yeah i don't know how long i would have gone without a job maybe a year or so um and then i would
[3014.94 --> 3023.00]  have run out of savings and um i don't know probably gone back to yahoo or something back to yahoo and uh
[3023.00 --> 3027.50]  i mean we're pretty lucky as programmers right you could just go get a job whenever you want one
[3027.50 --> 3032.96]  uh not not a lot of people have that luxury yeah that's that's that is absolutely true i mean
[3032.96 --> 3039.26]  yeah that's totally true the the bad part about that is there's lots of jobs not always lots of
[3039.26 --> 3044.76]  jobs you'd actually want to do sometimes there is and you know maybe if you're you you have you know
[3044.76 --> 3052.62]  better pick of the litter but not everybody has that uh that luxury but um how about programmer hero
[3052.62 --> 3058.42]  uh charlie we'll let you go first who is your who would be somebody that was very impactful to you
[3058.42 --> 3065.24]  uh over the course of your career programmer hero um people have asked me this before i don't have
[3065.24 --> 3071.38]  programming heroes um yeah maybe just somebody that's been important on another show i do called
[3071.38 --> 3076.16]  founders talk i'd ask somebody you know who's your founder hero who's been like a hero to you to help
[3076.16 --> 3082.52]  you get to where you are today um i like scientists i'm i'm big into that whole thing
[3082.52 --> 3087.98]  um the sort of mountain of work that needs to be done to inch society forward just a little bit
[3087.98 --> 3096.80]  and uh in in that sense um i don't know that's that's a tough question i'm you know the the big
[3096.80 --> 3101.56]  ones newton uh einstein those sorts of things but people living living heroes i've never really
[3101.56 --> 3108.24]  identified with with many um newton was kind of a dick he was kind of a dick he and liebnitz really
[3108.24 --> 3112.46]  went into it yeah but i mean he had the oh yeah way before way before liebnitz i
[3112.46 --> 3117.10]  mean he even um you know he wrote more about the bible than he did about physics or math or
[3117.10 --> 3122.82]  anything yeah he was he was searching for bible codes to try and like tell the future that's see
[3122.82 --> 3128.52]  i mean that's uh these are the things i learned when i hang out with isaac there you go um and
[3128.52 --> 3131.92]  yeah i don't know isaac what about you uh
[3131.92 --> 3139.50]  uh i don't know i don't think we in our show notes we didn't have one for you last time so i'm not
[3139.50 --> 3144.78]  sure if you didn't answer we didn't ask you but there's nothing in the show notes my programmer hero
[3144.78 --> 3150.52]  today because um i i just recently had to patch his code and and i i really liked the experience
[3150.52 --> 3156.78]  is uh trent mick trent mick who is uh he's an employee here at joint he wrote dash dash which is
[3156.78 --> 3165.56]  my new favorite uh options parser for the command line i'm about to check that out yeah dash dash is
[3165.56 --> 3172.78]  super neat cool is it spelt out or is it literally like like underscore type thing dude come on like
[3172.78 --> 3177.54]  you can't publish hyphen hyphen as an npm package name you can't i don't know i thought maybe you
[3177.54 --> 3184.42]  could no way it's got to start with a letter or number uh but uh no it's spelled out d-a-s-h-d-a-s-h
[3184.42 --> 3194.32]  got it and is that trent mick or nick trent mick with a m as in movember gotcha and it's it is
[3194.32 --> 3202.52]  movember isn't it are you are you guys movembering it no um i i don't like mustaches i think that you
[3202.52 --> 3206.48]  should just give money to prostate cancer research if that's what you want to do don't grow a
[3206.48 --> 3210.56]  mustache it's disgusting i'll pay 10 bucks to not grow a mustache and you can give that to prostate
[3210.56 --> 3215.48]  cancer research oh boy wow i don't i no i'm just kidding i won't do that i was gonna say now everybody
[3215.48 --> 3219.60]  knows how to get an extra 10 bucks yeah there's a lot of people out there um and a lot of them
[3219.60 --> 3228.76]  have mustaches but no um i i am i am not i i shave my face like a gentleman gotcha cool well guys i want
[3228.76 --> 3233.52]  to thank you for joining us today on the show definitely um you know we as the change i'll definitely
[3233.52 --> 3237.84]  want to support you however we can uh it it's not quite the future yet but tomorrow morning we
[3237.84 --> 3243.62]  have a post plan to help um you know obviously we'll post this uh this podcast everyone's listening
[3243.62 --> 3248.94]  to as well but we you know we want to support you however we can and we think that uh you should
[3248.94 --> 3258.32]  too and you can go to scale npm.org to um uh to to show your support uh they said don't do it but i
[3258.32 --> 3261.66]  say put your money where you put your packages i mean don't put your actual bitcoin in there but
[3261.66 --> 3268.46]  definitely help support this for sure and for all of you uh you know companies corporations out
[3268.46 --> 3273.04]  there that are using node that are listening to this or someone who works there um you know share
[3273.04 --> 3278.06]  share the uh share the information up line to get get corporate sponsorship in there and uh and make
[3278.06 --> 3282.22]  this thing happen so isaac and charlie different want to thank you for coming on the show today i want
[3282.22 --> 3289.92]  to also shout out to our sponsors digital ocean and top towel um something cool today um that digital
[3289.92 --> 3296.64]  ocean just mentioned was a one click uh application for doku we had uh we had jeff lindsey on the show
[3296.64 --> 3301.04]  a couple back uh if you haven't listened i'll put that in the show notes but super cool there's a
[3301.04 --> 3306.56]  one click install application you can like boom in one second have a droplet with uh with doku on it
[3306.56 --> 3311.76]  already and you can take advantage of our ten dollar hosting credit use the coupon code changelog
[3311.76 --> 3318.96]  sent me that's changelog sent me uh to use that you'll get a ten dollar hosting credit uh and if
[3318.96 --> 3325.94]  you like to write tutorials and you uh i just saw jeff actually released a a community tutorial that went
[3325.94 --> 3330.80]  along with this but if you're like jeff and you want to write a tutorial for digital ocean you can get
[3330.80 --> 3335.22]  paid 50 bucks to do that we'll have links in the show note for that as well and it doesn't matter where
[3335.22 --> 3341.58]  you live if you want to email barry at digital ocean.com he will send you stickers digital
[3341.58 --> 3346.70]  ocean stickers so to take advantage of that but uh you know isaac you mentioned earlier about having
[3346.70 --> 3353.08]  the opportunity to work pretty much anywhere and and our partner and and uh sponsor top towel uh is
[3353.08 --> 3358.78]  is uh able to make that happen as well you can join their team in a network of awesome people from
[3358.78 --> 3365.48]  anywhere in the world and uh and work anywhere basically uh with top towel we we mentioned how
[3365.48 --> 3369.44]  they do some pretty cool freelancing but you can go to top towel.com slash developer to apply
[3369.44 --> 3375.36]  and if you haven't yet check out their top towel uh engineering blog which has been featured on the
[3375.36 --> 3382.62]  show before as well as in our newsletter but uh top towel.com slash blog for that but guys anything
[3382.62 --> 3388.26]  else you want to say before we make this a wrap no i'm i'm really just looking forward to see uh how
[3388.26 --> 3394.62]  this thing uh plays out you know we've been it's been a sort of uh whirlwind uh since uh couch conf
[3394.62 --> 3400.74]  when this whole thing happened and it's uh exciting to see it wrap up this way yeah it's i like when
[3400.74 --> 3404.92]  you kind of get a problem and you kind of figure out how to solve it and then you release it then it's
[3404.92 --> 3409.94]  solved and it's like wow yeah we did it you know it's that moment or at least tomorrow's the beginning
[3409.94 --> 3416.24]  of that moment for you guys right so we're getting that's the idea that is the idea well fellas thanks for
[3416.24 --> 3422.04]  uh joining us on the show today we certainly support you however we can uh let's say goodbye take care
[3422.04 --> 3423.38]  thanks for having us
[3423.38 --> 3427.38]  you
[3446.24 --> 3457.38]  you
[3457.38 --> 3459.38]  you
[3459.38 --> 3461.38]  you
[3461.38 --> 3463.38]  you
[3463.38 --> 3465.38]  you
[3465.38 --> 3467.38]  you
