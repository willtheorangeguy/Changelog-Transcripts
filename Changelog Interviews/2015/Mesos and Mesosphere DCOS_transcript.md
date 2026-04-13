[0.00 --> 13.52]  welcome back everyone this is the change log and i'm your host adam stuchowiak
[13.52 --> 22.16]  this is episode 167 and on today's show we're talking to toby kanal the cto of mesosphere
[22.16 --> 29.72]  toby was the tech lead at airbnb and ultimately left back in 2013 to start mesosphere a company
[29.72 --> 34.12]  that is building a data center operating system for the next generation of internet scale
[34.12 --> 41.38]  applications we talked about mesosphere mesosphere dcos and all the open source around it apache mesos
[41.38 --> 50.00]  docker containerization linux kubernetes core os all the in-betweens chronos great show today with
[50.00 --> 56.96]  toby we have three awesome sponsors for this show code chip top towel and digital ocean
[56.96 --> 63.00]  our first sponsor is code chip they've launched a brand new feature called organizations
[63.00 --> 69.68]  and now you can create teams set permissions for specific team members and improve collaboration
[69.68 --> 75.28]  in your continuous delivery workflows maintain centralized control over your organization's
[75.28 --> 82.46]  projects and teams with code chips new organizations plans you can save 20 off any plan you choose for
[82.46 --> 89.02]  three months by using this code the changelog podcast again that code is the changelog podcast
[89.02 --> 96.32]  and you'll save 20 off any premium plan for three months by using that code head to codechip.com
[96.32 --> 99.42]  slash the changelog to get started and now on to the show
[99.42 --> 113.18]  all right we're back and this is actually take number two with toby canal he is the cto of mesosphere
[113.18 --> 121.12]  uh often mesosphere and mesos and apache mesos these are all sort of like mixed and intertwined so
[121.12 --> 126.40]  hopefully during the show we'll talk to toby a bit about all that and get it settled out but toby this
[126.40 --> 131.30]  is this is take two man what do you think well let's let's let's try this again let's hope we
[131.30 --> 137.20]  have we have better luck this time so just uh jared's also on the call too but just to explain uh what
[137.20 --> 141.80]  happened here we had a little glitch and we had to reschedule and today's that rescheduled day and
[141.80 --> 148.82]  toby's back so if we didn't tell you you wouldn't know so i i let the cow the bag it's a nice object
[148.82 --> 153.46]  lesson though because uh as i said last week when we had our glitch is that if toby had had
[153.46 --> 160.02]  a recording machine a data data center operating system if he had if his recording machine was
[160.02 --> 164.98]  spread out across a cluster of thousands that little hardware failure would have been no big deal right
[164.98 --> 171.68]  no big deal at all yeah it's all about high availability high availability well let's um
[171.68 --> 176.42]  let's go back in the past a bit so maybe let's set the tone for what the call is about so
[176.42 --> 180.12]  obviously you're the cto at mesosphere you got a lot of cool stuff you're doing there
[180.12 --> 185.32]  a lot of operating around open source a lot of stuff out there that's really uh picked up in
[185.32 --> 190.76]  the last year that's just got all sorts of things happening uh but you were also the tech lead at
[190.76 --> 196.16]  airbnb you've done lots of cool stuff in your past so let's get to know you a bit and learn a bit
[196.16 --> 204.32]  about what your past is and kind of who you are sure yeah so um so yeah i'm toby i i grew up in in
[204.32 --> 212.86]  beautiful bavaria in germany and um moved to silicon valley um about six years ago and um you
[212.86 --> 217.42]  know i went to school in germany did some some work in uh you know machine learning and sentiment
[217.42 --> 222.60]  analysis and then um you know when you grow up in germany and you work in tech um you always have
[222.60 --> 227.76]  these like these ideas these romantic ideas about what silicon valley is like and you know and it's
[227.76 --> 233.18]  everybody lives in the future there and stuff and so i always you know wanted to wanted to check it out
[233.18 --> 239.02]  and so uh you know did an internship at a small startup in silicon valley um you know a couple
[239.02 --> 244.16]  years ago and then um you know through a friend actually um got connected to the airbnb founders a
[244.16 --> 250.10]  little later and uh so i joined those guys um pretty early on i was engineer four at airbnb
[250.10 --> 255.52]  and um so yeah you know when you join that early you wear many hats so it did a lot of different
[255.52 --> 261.16]  things i i helped them scale their infrastructure um you know helped hire a lot of the engineering team
[261.16 --> 266.94]  um built some of the back-end services there like search and um and the fraud detection service
[266.94 --> 271.54]  i built some features in the product too um so lots and lots of different things
[271.54 --> 279.02]  and um you know a couple a couple years into airbnb um brought my best friend on board flow
[279.02 --> 284.48]  who's a co-founder of mesosphere too um so i brought him into airbnb
[284.48 --> 291.84]  um to build out the data infrastructure team and um so there you know we worked uh with apache mesos
[291.84 --> 296.94]  uh which you know ultimately uh was the reason for starting mesosphere because we uh you know we
[296.94 --> 302.98]  were pretty successful with mesos at airbnb flow had used it at uh at twitter before as well and so uh
[302.98 --> 308.52]  you know that that led us to to start the company so maybe since you mentioned apache mesos i mentioned
[308.52 --> 315.34]  as well and mesosphere can we knock down some hurdles in terms of terms and terminology apache mesos
[315.34 --> 323.00]  mesosphere mesos dcos um let's let's let's help us out and explain to the audience the differences
[323.00 --> 329.04]  between all these names totally yeah so let's um so the first thing that was out there was was mesos
[329.04 --> 335.08]  it was actually called nexus before it was called mesos but there was another product called nexus so
[335.08 --> 341.24]  they changed the name so um it was um it started as a project at uc berkeley at the amp lab
[341.24 --> 347.52]  uh and in fact uh ben heinman who's the third founder of mesosphere um you know was one of the
[347.52 --> 353.98]  co-curators of the project um so it started there uh the idea was to build um a cluster management system
[353.98 --> 359.84]  so sort of this layer that manages all the machines in a in a data center in a large cluster
[359.84 --> 365.94]  and that provides apis for building um large-scale systems on top and making that process really
[365.94 --> 372.06]  easy um it um it became an apache project a little later so it was called apache mesos then
[372.06 --> 380.50]  um and uh you know twitter was one of the largest backers initially now so that's apache mesos um you
[380.50 --> 387.24]  know been an apache top level apache project uh for a couple years now um mesosphere is the company
[387.24 --> 394.44]  that uh flow and ben and i created um to commercialize apache mesos and to build a product
[394.44 --> 400.24]  around it um you know the way to think about apache mesos or the way we like to think about it is
[400.24 --> 407.06]  um it's kind of like the linux kernel so it's a fairly it sits fairly low in the stack um it does a lot
[407.06 --> 413.60]  of cool stuff it's very um you know very sophisticated piece of technology um it's uh it's very high
[413.60 --> 418.74]  performance a lot of really smart people working on it um but if you look at the linux kernel you
[418.74 --> 423.52]  know the linux kernel is not linux right there's a lot of things around the kernel that you need to
[423.52 --> 429.48]  um to run your applications and um you know to make the whole thing useful so that's basically what uh
[429.48 --> 435.40]  what dcos is uh the data center operating system uh which is the main product that we're building at
[435.40 --> 441.40]  mesosphere so it has apache mesos at its core um but it has all the pieces around it too that that make
[441.40 --> 449.34]  it you know a full operating system experience so we got lots of different names there mesosphere apache
[449.34 --> 456.98]  mesos the kernel itself basically um let's go back to airbnb where i didn't want to derail us too far
[456.98 --> 461.44]  off the conversation there but i did want to set some tone in terms of the the terms and things like
[461.44 --> 465.92]  that people just sort of stumble over like and part of this conversation is to demystify a bit of
[465.92 --> 471.94]  what's happening in the cloud um and so hopefully you can help us do that but take us back to to when
[471.94 --> 477.02]  you guys were originally starting uh mesosphere what what inspirations were happening what was
[477.02 --> 482.70]  happening at airbnb in terms of the technology that made you guys eventually leave and start this uh this
[482.70 --> 489.02]  new company yeah so it was really our experiences from both airbnb and twitter that that led to it
[489.02 --> 495.94]  because we um you know ben and flo at twitter and then flo and i at airbnb we used the used mesos for
[495.94 --> 500.86]  completely different use cases actually and um and the environment was completely different too you
[500.86 --> 508.22]  know twitter runs their own data centers uh airbnb is entirely on on amazon web services so cloud and
[508.22 --> 513.80]  on-premise um and twitter was was running um you know they're running pretty much all of their production
[513.80 --> 519.00]  services on on top of mesos so you know it's things like search and the ad server and a lot
[519.00 --> 524.62]  of user facing kind of request response type things and uh at airbnb we were running big data
[524.62 --> 533.52]  stuff so we ran hadoop on top of it cassandra spark um so big data analytics um and uh you know that
[533.52 --> 538.64]  that was kind of where the idea for uh calling it a data center operating system came from uh because
[538.64 --> 542.40]  we looked at this and we're like you know this can really run all the workloads you can run in a
[542.40 --> 547.18]  data center the whole range of applications kind of the same way that you know your desktop operating
[547.18 --> 551.98]  system is general purpose you know there's not one operating system that's great for doing
[551.98 --> 555.78]  development and then there's another one that's great for doing graphic design and a third one for
[555.78 --> 563.02]  doing like word and excel uh you know operating systems are mostly general purpose um so that's
[563.02 --> 570.36]  kind of what drove this um and you know pre mesos um at those two companies um there were really a bunch
[570.36 --> 576.98]  of big challenges that we were able to solve with mesos um one thing that was uh that both airbnb and
[576.98 --> 583.20]  twitter uh struggled with was kind of scaling um scaling up and being able to to handle the user
[583.20 --> 589.50]  growth um so twitter if you if you remember the fail whale that was kind of like 2009 right right you
[589.50 --> 593.98]  saw that a lot and you know and i think there's even like it's twitterdown.com and like all that
[593.98 --> 598.30]  stuff it was on hacker news all the time the whole internet got got angry and took out the pitchforks
[598.30 --> 604.26]  when twitter was down so um you know what happened behind the scenes is they um you know they started
[604.26 --> 610.42]  twitter started as a ruby and rails application and um they they had to you know millions of people
[610.42 --> 615.84]  showed up um hundreds of millions tweeted a lot um the infrastructure couldn't scale with this
[615.84 --> 622.78]  um so they really needed to rethink uh stuff and one thing they did is they they took this monolithic
[622.78 --> 627.92]  ruby and rails application and broke it down into pieces uh into like microservices micro backend
[627.92 --> 633.52]  services so you know there's like a different service for um you know your timeline maybe your
[633.52 --> 638.88]  search your ads those are all different uh different code bases different services and so one thing they
[638.88 --> 643.08]  needed is really a platform to run all these things because that's you know a lot of stuff to manage
[643.08 --> 651.64]  um and um and that's what they used mesos for um and uh you know at airbnb um it was a slightly different
[651.64 --> 657.80]  scenario we we wanted to use um hadoop and we wanted to use it in sort of a self-serve way
[657.80 --> 663.18]  where we could start to do clusters very quickly and then shut them down again uh and we also wanted
[663.18 --> 669.74]  to be able to try out uh new data analytics tools as they come out um you know data analytics stack is
[669.74 --> 674.84]  never just a dup it's always a combination of things and you know we were using kafka also at the time
[674.84 --> 681.54]  so it's just a bunch of different tools and we really wanted um a platform to run all this stuff on
[681.54 --> 685.80]  to make it really easy to install these things instead of you know spending a month or even
[685.80 --> 691.92]  multiple months to you know trying to figure out how to install hadoop or kafka um so it was one
[691.92 --> 697.90]  use case at airbnb the other one um which was pretty interesting and probably the most uh advanced one
[697.90 --> 705.28]  um so what we were doing at the time is we um we had one machine that had um a crontab on it and that
[705.28 --> 712.36]  basically ran the whole um etl and analytics pipeline so it would do things like um you know step one
[712.36 --> 717.52]  dump the sql database to a text file and then maybe merge it with the web server logs and pull
[717.52 --> 722.10]  some other data from a key value store and you know build a data set from all that and then
[722.10 --> 727.36]  another step would be you know take that and count the revenue count you know other things number of
[727.36 --> 730.74]  visitors uh what have you so there's always these multiple steps that depend on each other
[730.74 --> 737.14]  and um we were doing that at the time with uh with cron so you had to be you know be like okay the
[737.14 --> 742.50]  first step um should probably take like 30 minutes so you know let's give it an hour and then run the
[742.50 --> 747.98]  next step um and uh so obviously like if that first step would would take longer than an hour
[747.98 --> 753.06]  um for whatever reason then everything would fall over and you had to like manually debug things and
[753.06 --> 758.24]  you know folks weren't happy because the reports weren't there and so it was it was kind of a struggle
[758.24 --> 762.76]  um and the other thing too is um you know the business was growing fast and so
[762.76 --> 768.74]  these jobs would uh would take longer to run over time and this one single box that we had would
[768.74 --> 774.38]  just get overloaded and so and so what we what we wanted to do to solve that problem is we wanted to
[774.38 --> 781.04]  build a system that could dynamically scale with um the workload with the etl workload that's coming
[781.04 --> 787.36]  in that's what became chronos which we open sourced um at airbnb so you were you a part of that then
[787.36 --> 792.52]  chronos yes it was mostly flows team um i contributed a little bit to it um
[792.52 --> 797.70]  but the flow was running the data infrastructure team and they they built that um and we built it
[797.70 --> 801.12]  so we looked at this you know we looked at the requirements that we had you know being able to
[801.12 --> 808.62]  scale dynamically elastically um being able to populate new machines um as needed um and we were like
[808.62 --> 812.64]  you know this is a lot of this is really hard you know this is you know those are not trivial
[812.64 --> 817.40]  problems but um but then we looked at mesos and we're like hey wait a minute you know mesos
[817.40 --> 822.14]  solves a lot of these things already like it has it has those things built in as primitives and we can
[822.14 --> 828.38]  just build on top of that and you know spend a lot a lot less time to um to build this thing and and
[828.38 --> 834.70]  in fact it took only three months to build the whole thing and it had it had just like three
[834.70 --> 839.18]  thousand lines of code i think somewhere around there um which you know given that it's a distributed
[839.18 --> 844.68]  and fault distributed system that is fault tolerant and can scale elastically um can survive machine
[844.68 --> 849.72]  crashes and so on that's that's pretty awesome that's not a lot of code for that so you guys got
[849.72 --> 857.90]  excited about mesos and so excited that you decided to start mesosphere a company um kind of built on top
[857.90 --> 865.82]  of mesos so i'm interested a little bit in the the social and economic kind of background with the
[865.82 --> 871.38]  project because you have it started at uc berkeley um all of a sudden huge players such as airbnb
[871.38 --> 877.48]  twitter more recently apple and many others hopping in and saying this is something that we want that
[877.48 --> 883.54]  we need and we'd like to build upon um and then it became an apache foundation project so maybe just
[883.54 --> 889.58]  kind of explain that whole milieu a little bit and the corporate interests the open source interests and
[889.58 --> 898.26]  break that down for us sure yeah so um it became an apache project um pretty early on basically when um
[898.26 --> 905.28]  when twitter decided to really invest invest in it and um and make it their production um the platform
[905.28 --> 909.90]  for running production um before that you know because it came out of the amp lab in berkeley
[909.90 --> 918.08]  um berkeley had the rights and had the ip and um so twitter you know because it the plan was to make it
[918.08 --> 924.42]  such a central piece of their stack of the infrastructure um they wanted the ip be owned by
[924.42 --> 930.48]  the apache foundation um just so they could contribute to it as well and and to have sort of this neutral
[930.48 --> 936.68]  entity um so it's not the lab it's not twitter or any other um company that that owns it but it's owned
[936.68 --> 943.02]  by the by the foundation um so that was um that was you know a decision that they made pretty early on and
[943.02 --> 950.96]  uh and then uh you know uc berkeley donated all the ip to the apache foundation um ben heineman became the
[950.96 --> 959.08]  um the chair for the project um and uh and then it sort of went the way that uh that most apache projects
[959.08 --> 966.10]  uh go so um you know every apache project actually has a lot of freedom over how they want to manage
[966.10 --> 974.32]  it uh but um you know every every apache project has this has this idea of um of committers and um
[974.32 --> 979.92]  you know the way it works is when when you set up an apache project um and it gets accepted there's an
[979.92 --> 984.40]  initial set of committers so at the time it was you know the folks from berkeley that that have worked
[984.40 --> 991.36]  on it uh in the past and uh and then the project set up a process for you know how do we how do we
[991.36 --> 998.98]  accept new committers and the goal there was really because it is such a you know central such an
[998.98 --> 1004.36]  important piece of the stack um it had the project has a really high bar for people becoming committers
[1004.36 --> 1010.14]  so this you know it typically takes at least six months for someone to you know write enough code fix
[1010.14 --> 1015.56]  enough bugs get enough credibility into the community to be accepted as a committer and um
[1015.56 --> 1021.56]  and so usually what happens is um there is a vote that gets done you know among among the existing
[1021.56 --> 1027.40]  committers so someone will propose a new person uh as a new committer and then the existing committers
[1027.40 --> 1032.24]  make a vote and if there's enough votes then um that that goes through and that person becomes a
[1032.24 --> 1039.12]  committer so being an apache project i assume it's the apache license right that's right yeah it's
[1039.12 --> 1043.98]  apache 2 licensed which is one of the you know more free as far as you are free to build proprietary
[1043.98 --> 1053.40]  systems around it um that being said you're building a company a vc funded company around mesos and um
[1053.40 --> 1060.82]  curious your thoughts on you know building a product or a service around software that ultimately is out of
[1060.82 --> 1068.74]  your control yeah so um this actually works you know the model works really great for us um and
[1068.74 --> 1074.96]  you know we do have some control over the software because we are you know we are an active participant
[1074.96 --> 1083.06]  in in the project in fact we have the most committers of any company on on the apache mesos project and so
[1083.06 --> 1089.54]  you know even though we don't own the ip or we don't own the project um we can uh we have you know a big
[1089.54 --> 1097.88]  seat at the table um and you know what we really wanted to do is um build build substantial product
[1097.88 --> 1102.50]  around the open source project as well uh so we really think that you know there's there's a lot
[1102.50 --> 1110.44]  we can add in terms of management tools and um you know applications around mesos and uh and sort of
[1110.44 --> 1116.10]  you know the the whole um how do you operationalize this thing and really make it work in enterprise
[1116.10 --> 1121.94]  data centers that's really where where we think we we add a lot of value as a company um and so
[1121.94 --> 1127.04]  you know if a lot of these open source projects you know they're built by you know they're built by
[1127.04 --> 1135.08]  hackers and and we kind of built these things for um for ourselves um and um that that works great
[1135.08 --> 1139.38]  you know they they those things those tools work they do the job but they're not really built for
[1139.38 --> 1144.74]  enterprise environments and so in mesos's case for example when you set up a cluster and you use
[1144.74 --> 1149.66]  open source mesos um out of the box it's kind of open you know anybody can do anything
[1149.66 --> 1156.28]  um it does have some controls but it's not enough for um to satisfy you know enterprise requirements
[1156.28 --> 1162.48]  where folks have you know really strict policies and um auditing requirements um you know especially
[1162.48 --> 1168.04]  when it's a bank they have all sorts of regulations that they need to um make sure they they meet
[1168.04 --> 1174.02]  so um so what we're really doing there is building all these tools and apis around mesos to to make
[1174.02 --> 1180.84]  work in those environments too yeah so it sounds like because mesos is kind of the kernel of a
[1180.84 --> 1186.54]  distributed clustering system there's a you know there's a lot of other pieces to the operating system
[1186.54 --> 1193.64]  puzzle and um everybody at least the large players appear to be building their own so um apple has
[1193.64 --> 1198.10]  something i think proprietary called jarvis not sure if that's open source proprietary there's marathon
[1198.10 --> 1203.24]  you mentioned chronos that was built at airbnb some of these are open source some of these are not
[1203.24 --> 1208.48]  apache aurora can you kind of explain all you you mentioned chronos and you mentioned there's other
[1208.48 --> 1214.82]  services and things that need to be built around it um is there a comprehensive list of missing things
[1214.82 --> 1219.78]  that you need to have a data center operating system if all you start with is apache mesos
[1219.78 --> 1225.76]  yeah so um you know the best way to do this is uh is really you know dcos the data center operating
[1225.76 --> 1232.46]  system has a free community edition that uh you know you can just go to our website um you know launch a
[1232.46 --> 1238.60]  cluster on aws um in other clouds and just you know get started with it it doesn't cost anything
[1238.60 --> 1244.68]  besides you know paying for the machines um in in the cloud um so that's really the best way to get
[1244.68 --> 1249.76]  started and and you know you get all the pieces uh you get the cli to interact with your cluster you get
[1249.76 --> 1255.66]  the gui to see what's going on you get a package manager so it's really um you know really all the all
[1255.66 --> 1260.94]  the things you you know from linux or other operating systems there's an equivalent of that in in the dcos
[1260.94 --> 1268.46]  um so our package repository so you can really easily say install hadoop kafka cassandra all these
[1268.46 --> 1273.42]  systems with one single command the same way you know on linux you would do apt get install
[1273.42 --> 1281.32]  um you know we have dcos package install um and you know in terms of the applications that run on top
[1281.32 --> 1287.36]  um you know you mentioned a bunch of them i think i think the operating system analogy works really
[1287.36 --> 1294.28]  well there um so if you think of um you know let's let's pick mac os um you when you install mac os it
[1294.28 --> 1300.06]  comes with a few applications pre-installed right so you fire it up for the first time you already have
[1300.06 --> 1304.34]  finder on there and you have a browser right sort of the basics are there the killer apps are there
[1304.34 --> 1310.34]  right um but there's many other browsers you can run on mac os right you can use chrome you can use
[1310.34 --> 1317.54]  firefox or you can use opera um and i think it works kind of the same way in the dcos you know
[1317.54 --> 1323.36]  when we ship dcos it comes with marathon which is another open source project that we maintain at
[1323.36 --> 1331.32]  mesosphere which is kind of the equivalent of an init system that you know from linux so it starts you
[1331.32 --> 1337.12]  know long-lived processes in your data center so for example your ruby and rails application or no js app
[1337.12 --> 1343.34]  so anything you want to keep running forever um it does that but you know it that's just that's just
[1343.34 --> 1348.54]  the safari equivalent right that's the one that we ship um and we believe it's awesome but if you if
[1348.54 --> 1353.14]  you want to use a different one you can do that and uh you know like you said apple built their own
[1353.14 --> 1360.76]  it's jarvis um hopspot built one called singularity twitter built one called aurora um netflix is working
[1360.76 --> 1366.48]  on one so it's you know i think this really shows that the the data center operating system model works
[1366.48 --> 1371.20]  right because you get this foundation and it allows developers out there at all these companies
[1371.20 --> 1377.08]  to build their own applications on top to use the api and build something that's custom for the
[1377.08 --> 1383.34]  environment that works well for their needs that works well with their workflow and in fact i'd argue
[1383.34 --> 1390.76]  you know if um those things are kind of like platform as a service equivalents passes and uh we've seen a lot
[1390.76 --> 1396.28]  of passes in in the past um and i would argue that none of them have really been that successful
[1396.28 --> 1401.96]  and i think it's because they're generally pretty opinionated they have one specific workflow
[1401.96 --> 1408.30]  and that you know usually just works for a handful of people it's that same workflow does not work for
[1408.30 --> 1414.70]  every company and so one thing uh that the dcos allows you to do is really you know either take one
[1414.70 --> 1419.14]  of those existing things and modify them or just build your own completely if you want to have your own
[1419.14 --> 1425.14]  workflow um and in fact there's uh i think there's more than a dozen in total that are you know paths
[1425.14 --> 1431.94]  like systems that run on top of the dcos um another example is actually docker swarm which uh which
[1431.94 --> 1439.94]  they're also building on top of mesos so as developers we always try to point out patterns and what's the
[1439.94 --> 1446.18]  same and what's different and it seems like uh the mesos makes a lot of sense to have that that cluster
[1446.18 --> 1452.20]  management and scheduler shared and but everybody seems to be agreeing that the platform the marathon
[1452.20 --> 1458.30]  the jarvis this is where the concerns break out and you can't actually that's not shared infrastructure
[1458.30 --> 1465.02]  huh could it be could those all be shared like there's one pass and we all you know just like
[1465.02 --> 1470.28]  apache mesos uh i noticed aurora which you said with twitter started is an apache project well how come
[1470.28 --> 1474.60]  how come it's not everybody's working on apache aurora and then you guys are adding value at an even
[1474.60 --> 1479.76]  higher level it's just because there's different needs at a low level right yeah it's it's for that
[1479.76 --> 1484.72]  reason uh that i mentioned i think um they all all of these things take slightly different approaches
[1484.72 --> 1491.60]  and um you know aurora and jarvis and singularity they're all they all have something that is you
[1491.60 --> 1498.18]  know fills a specific need um inside the company that built it and and that makes it less you know
[1498.18 --> 1502.94]  generalizable and so um you know and i don't think that's a bad thing i think it's i think it's
[1502.94 --> 1509.18]  actually awesome that there's that there's choice and um and you know that if you're new to the space
[1509.18 --> 1514.24]  you can you can look at the patterns that each one of those systems um use and and just pick the one
[1514.24 --> 1519.26]  that works best for you kubernetes is another another example which you know came out of google and has
[1519.26 --> 1523.74]  sort of their workflow and their abstractions built in you can run that on the dcos as well
[1523.74 --> 1528.78]  yeah i was just going to ask about google because they seem to be the the missing entity in the large
[1528.78 --> 1536.00]  uh players here amazon as well i mentioned them a little bit but google has a thing called borg
[1536.00 --> 1541.38]  could you explain how borg fits into this or doesn't fit into this it absolutely fits in yeah so
[1541.38 --> 1549.98]  actually borg was probably the first system ever um in in this space um and um you know google uses it
[1549.98 --> 1555.74]  internally it's not open source um they don't sell it um they wrote a paper about it and uh in fact
[1555.74 --> 1561.48]  um mesos takes some inspiration from borg um you know google is a sponsor of the lab where it came
[1561.48 --> 1566.34]  from so there was you know a good exchange of ideas back then uh it also does a few things
[1566.34 --> 1573.36]  differently than borg but um definitely you know took a lot of inspiration um so yeah borg is the
[1573.36 --> 1581.06]  cluster manager um and that that google uses internally for for pretty much everything so if you're using
[1581.06 --> 1585.90]  gmail that runs on borg if you're using google search it runs on borg they run all the databases
[1585.90 --> 1591.74]  i think even google file system runs on top of borg so uh it's really their one stack that they use
[1591.74 --> 1597.72]  internally to um to run all the things awesome well i want to ask a few more questions about kubernetes
[1597.72 --> 1602.46]  and uh clear up exactly how that fits into everything because it seems like it does play nice
[1602.46 --> 1608.92]  uh in this uh ecosystem but we'll take a quick break here from a sponsor and when we get back we will
[1608.92 --> 1614.68]  ask toby about kubernetes you've heard me talk about top towel several times in this podcast
[1614.68 --> 1621.02]  but today is different i've got a special treat for you i went out and spoke with a listener who
[1621.02 --> 1626.94]  a year ago had never heard of top towel he listened to the show just like you're doing right here right
[1626.94 --> 1631.48]  now today and heard us talk about top towel and what they're all about and he decided to get in
[1631.48 --> 1636.86]  touch and now he's living the dream as a freelance software developer with top towel his name is
[1636.86 --> 1642.76]  daniel alzahn and i sat down and i talked with him i said hey what is it that you love most about top
[1642.76 --> 1650.06]  towel take a listen well for me the the thing about top towel which i thought would be very hard for me
[1650.06 --> 1656.76]  personally as i transitioned to a more consulting role uh was the way i would have access to new
[1656.76 --> 1662.96]  clients and what quality of those would be so i found that i've had access to awesome clients
[1662.96 --> 1667.54]  through top towel and it hasn't been that hard to find because they have a lot of choice and even
[1667.54 --> 1674.42]  more than that uh there's enough choice and i i can actually be a little selective about what kinds of
[1674.42 --> 1680.40]  things i want to be working on so i use that as a way to sort of hone my skills and you know go towards
[1680.40 --> 1685.24]  the technology that i think are are worth investing in for the future so whether it's you know including
[1685.24 --> 1691.68]  new front-end frameworks or doing a little devops work on the side i i usually am able to find clients
[1691.68 --> 1698.26]  who are have the needs of the things i want to get better at so that's been that's been truly useful
[1698.26 --> 1704.50]  all right that was daniel lazon a listener of the change log and also a freelance software developer
[1704.50 --> 1712.10]  with top towel if you want to follow in daniel's footsteps go to top towel.com slash developers
[1712.10 --> 1719.52]  that's t-o-p-t-a-l.com slash developers to learn more about what top towels all about
[1719.52 --> 1721.68]  and tell them the cheese log sent you
[1721.68 --> 1731.70]  all right we're back talking about apache mesos mesosphere uh the cloud digital digital distributed
[1731.70 --> 1738.90]  systems um curious about kubernetes you mentioned it uh previous to the break but i'd kind of like you
[1738.90 --> 1745.34]  just explain it in more detail for us yeah so kubernetes is an open source project that google
[1745.34 --> 1753.72]  kicked off last year uh 2014 um they announced it uh i think in around june last year after working
[1753.72 --> 1760.40]  on it for a couple months um so it's really it's um it's a container manager container orchestrator
[1760.40 --> 1767.18]  um that is um that uses a lot of the same abstractions and learnings uh from google internally
[1767.18 --> 1772.72]  that you know the things that google learned over the years building borg and uh you know it's
[1772.72 --> 1778.82]  multiple iterations um and so they took all those learnings um and you know put it into a new open
[1778.82 --> 1785.74]  source project that they built from scratch um and that is what kubernetes is so uh it's you know
[1785.74 --> 1794.36]  it's a really nice tool it's really um simple and easy to use um they have um it has kind of two main
[1794.36 --> 1799.80]  abstractions that you know google um found very useful for managing large numbers of containers one of
[1799.80 --> 1806.28]  them is uh the idea of a pod which is basically a group of containers that get launched together
[1806.28 --> 1812.94]  on the same physical machine that um you know share the same network address and share the same
[1812.94 --> 1819.98]  volumes um so a use case would be for example if you're running a web application in one container
[1819.98 --> 1826.86]  and you want to run some monitoring system right next to it or some logging agent um right next to that
[1826.86 --> 1831.56]  web application you can run that in another container but they get launched together so
[1831.56 --> 1837.18]  um and they share the volumes share the disk so so they have access to each other um so that's the
[1837.18 --> 1842.74]  idea of a pod it's one of the you know things that are unique about kubernetes uh the other one is this
[1842.74 --> 1849.84]  idea of um labels and using labels to model dependencies in the system and discover other pieces in the
[1849.84 --> 1854.82]  system um so you know when you're running lots and lots of containers at scale um one problem
[1854.82 --> 1859.42]  is is really how do you discover things you know how do you figure out where things are running and
[1859.42 --> 1865.30]  how do you say um you know this web application depends on that database and traditionally how we
[1865.30 --> 1871.66]  did that um once you know in in the past is with dns right we would just say you know my rails
[1871.66 --> 1877.76]  application you know go talk to database.company.com and you know that that doesn't really work in
[1877.76 --> 1882.50]  very dynamic and elasting environments where containers can move around and um and you don't really have
[1882.50 --> 1888.06]  this model of you know pinning an application to a specific machine and and you know making sure
[1888.06 --> 1894.26]  it lives there forever so so yeah what kubernetes does instead is it gives you labels um so you can
[1894.26 --> 1901.28]  basically just say um you know my web app depends on the thing that is labeled um you know type database
[1901.28 --> 1906.34]  and environment production something like that um so those are kind of the two main abstractions
[1906.34 --> 1913.36]  and kubernetes plots and labels um and uh you know we like those um a lot and kubernetes you know is a
[1913.36 --> 1918.28]  really popular open source project it's getting a lot of traction um it's really great for running
[1918.28 --> 1925.78]  containers um in you know sort of um a microservices environment and um so that's why we decided to become
[1925.78 --> 1933.02]  part of the project too and um and i think you know the where we can really add value there is um we can
[1933.02 --> 1940.54]  make it run really well um in you know any environment where the dcos runs um so you don't
[1940.54 --> 1944.64]  have you know the same way you don't have to go through the setup of the other distributed systems
[1944.64 --> 1949.14]  that we support um we make that really easy for kubernetes as well so you can literally say you know
[1949.14 --> 1954.58]  dcos package install kubernetes and you're up and running you have a kubernetes cluster configured and
[1954.58 --> 1960.86]  you can start running containers so because it's operating at the level of orchestrating
[1960.86 --> 1968.46]  linux containers it can actually sit on top of mesos and on top of the dcos that mesosphere adds to
[1968.46 --> 1973.88]  mesos is that right that's right yeah so it it sits sort of at the same level where all of our other
[1973.88 --> 1982.46]  services sit um so right next to you know spark hadoop marathon all these other things so i'm just
[1982.46 --> 1986.42]  going to try to lay out my understanding of this whole stack and i just want you to tell me where it
[1986.42 --> 1991.72]  falls down or if i'm if i'm tracking you because i feel like i am but then i turn around and i can't
[1991.72 --> 1997.08]  and i realize i have no idea what's going on so you have and maybe adam this will help you as well
[1997.08 --> 2002.64]  it'll definitely help me okay so you have your hardware right yep and then on that you have an
[2002.64 --> 2010.24]  operating system like linux um and then on top of that you have mesos which turns many linuxes you
[2010.24 --> 2018.08]  know thousands are scalable up and down into one clustered thing and then on top of that now you
[2018.08 --> 2024.10]  add on top of your your app it's not really application layer but now you can start adding
[2024.10 --> 2028.58]  your this is where your kubernetes we call it services your services so maybe you have a hadoop
[2028.58 --> 2035.42]  service um or you have kubernetes which allows you then to manage linux containers so now you have a
[2035.42 --> 2043.16]  second layer of linux um but abstracted away from the hardware now uh yeah which then inside of those
[2043.16 --> 2049.78]  containers you could run your adobe right exactly so so i think you described it uh really well so you
[2049.78 --> 2056.18]  have the hardware you the next layer up um well linux is there um right the next layer up is um
[2056.18 --> 2063.06]  mesos that's the layer that abstracts um not really abstracts but manages the resources manages the
[2063.06 --> 2068.78]  hardware resources so it knows how big your cluster is it knows how many cores are available how much
[2068.78 --> 2074.92]  memory is available and it uses those resources from that one big pool which is your whole data
[2074.92 --> 2081.08]  center or your whole cloud and and offers them to the services that run on top so the services on top
[2081.08 --> 2085.56]  are kind of your building blocks they're kind of your legos that you use to build your business
[2085.56 --> 2091.48]  application right so if you're building a web app you need a database so you know launch a database
[2091.48 --> 2097.96]  on the dcos if you're if you're building a web app you need a way to run containers so use you know
[2097.96 --> 2103.96]  one of the container orchestrator orchestrator services like kubernetes like marathon like docker
[2103.96 --> 2109.76]  swarm and so on um so those are the building blocks and then you use those building blocks to manage
[2109.76 --> 2115.80]  your application so your application code um goes into a linux container you give that linux container
[2115.80 --> 2121.40]  to one of those orchestrators they run it in the cluster you get the tools um you know the
[2121.40 --> 2124.96]  service discovery for example to let your application talk to the database that you
[2124.96 --> 2130.56]  launched earlier that's how it all fits together gotcha i think i follow that adam yeah i'm definitely
[2130.56 --> 2136.18]  tracking on that i mean it gets a lot it's definitely still complicated but i'm tracking for sure it's
[2136.18 --> 2140.16]  a whole new world everything's different yeah it is and i think when one of kubernetes pitch was
[2140.16 --> 2146.18]  like google's infrastructure for everybody um and you know a data center operating system is kind of
[2146.18 --> 2151.26]  the same idea it's like you could have access to this kind of scale without having to manage all
[2151.26 --> 2157.16]  those you know tricky pieces below where you care about and um you know we've been talking about big
[2157.16 --> 2164.70]  players apple google twitter airbnb um and so the question that pops up because i'm just a little guy
[2164.70 --> 2171.16]  you know like uh and as a lot of developers are out there a lot of our listeners are developers
[2171.16 --> 2175.40]  wondering like is this something i even need to be caring about right somebody who maybe runs
[2175.40 --> 2182.62]  a couple servers that maybe i have a web server and a database server um should we be paying
[2182.62 --> 2188.18]  attention to this stuff or is it really the world of twitters and airbnbs i think everybody should be
[2188.18 --> 2193.18]  paying attention to this um and and here's the reason so i think when we build things today
[2193.18 --> 2200.98]  um we sort of have to we always have to choose between you know building things quickly or building
[2200.98 --> 2205.06]  things for scale i've definitely been in that situation if you look at you know airbnb and
[2205.06 --> 2209.52]  twitter in the early days um they were just you know a simple ruby and rails application that talked
[2209.52 --> 2215.50]  to a database right that's that's how they both started um and uh and they sort of had to choose
[2215.50 --> 2221.04]  to you know build build things quickly for build for a time to market um and then when they when they
[2221.04 --> 2227.48]  started growing um you know it became really hard to scale those things so i think you know for all the
[2227.48 --> 2231.54]  developers out there that are working on something that you know they hope that one day will will be
[2231.54 --> 2240.14]  big um i would say build it on top of the dcos from from day one because um you know when when it
[2240.14 --> 2245.56]  when it comes time to scale that thing um you'll have a lot less things to worry about and you know i
[2245.56 --> 2251.20]  think uh even if you just have two servers and um the dcos can already add value you know if one of
[2251.20 --> 2256.04]  those two servers fails um it can move your applications to the other one so i think that's already pretty
[2256.04 --> 2262.18]  awesome um i think you know the reason why we're seeing mostly big companies using this stuff right
[2262.18 --> 2267.48]  now is because you know for them there's no alternative like their pain in managing those
[2267.48 --> 2273.34]  many many servers that they have is so big there's just no alternative to automating the whole thing
[2273.34 --> 2279.34]  um and so you know their um their bleeding is bigger that's why we're seeing a lot more of those
[2279.34 --> 2286.32]  guys using it but um you know if i were to start a company today um and you know build some uh say
[2286.32 --> 2291.52]  build a mobile app with with a back end um i would definitely build it on the dcos from day one
[2291.52 --> 2297.56]  you don't think things are moving too quickly for those who don't touch it quite off quite as often as
[2297.56 --> 2302.68]  say daily like a large ops team might it's not moving so quickly that they'll just spend most of their
[2302.68 --> 2308.90]  time kind of playing catch up to this new tech uh no i don't think so and and you know really that's
[2308.90 --> 2316.04]  our our mission at mesosphere is to really make this um kind of an easy to use product um so you don't
[2316.04 --> 2321.72]  have to be a you know cluster management expert or distributed systems phd to to run that thing
[2321.72 --> 2327.86]  we want to make that really really easy you know as easy as as linux you know and get get to that
[2327.86 --> 2334.26]  same level of um of sort of turnkey experience maybe we should uh take some time now to break
[2334.26 --> 2339.50]  down mesosphere then so now we've talked about mesos marathon chronos and the whole slew of things
[2339.50 --> 2347.92]  kubernetes borg even um let's talk about what this does to to bring it to a dcos so dcos is
[2347.92 --> 2357.28]  mesosphere is the company dcos or mesosphere dcos is a product where is is this a shipping is it uh
[2357.28 --> 2364.92]  i guess do you download it do you is it a cloud service how does this work right so it um there's
[2364.92 --> 2372.82]  basically you know two ways to run it um which is on one of the public clouds like aws and google
[2372.82 --> 2378.88]  cloud and azure um or you can run it on your own machines if you have you know a bunch of machines
[2378.88 --> 2384.76]  in a data center somewhere or you or you own a whole data center um you can go to the mesosphere
[2384.76 --> 2392.20]  website today um basically click a button and launch a fully configured cluster in in one of the
[2392.20 --> 2397.98]  clouds so all the you know it just uses the standard provisioning tools that the cloud providers have
[2397.98 --> 2404.26]  like cloud formation on aws and you know brings up all the machines it's fully configured you know it
[2404.26 --> 2410.82]  takes about 10 minutes and and you're up and running and um so it's not you know hosted by mesosphere
[2410.82 --> 2417.22]  but um you know you kind of um we just give you a template we redirect you to aws you log in with
[2417.22 --> 2422.70]  your own account and um you know you use that template to bring everything up but you know it's
[2422.70 --> 2429.06]  your machines in your aws account so you manage the whole thing um if you want to run it in uh in a
[2429.06 --> 2435.32]  data center in your own data center on your own machines um we have sort of an early access version
[2435.32 --> 2441.88]  of that product um and um we're giving that to um you know a handful of design partners right now and
[2441.88 --> 2449.14]  and early customers um that are helping us you know sort of polish it up um so it's kind of you know
[2449.14 --> 2454.04]  call us and uh and we'll get back to you and help you install it at the moment so when we go to the
[2454.04 --> 2458.82]  product page we see community edition free and we see enterprise edition let's talk is that the
[2458.82 --> 2462.44]  dividing line there the community edition is what you can go and launch today and the enterprise version
[2462.44 --> 2468.50]  is what you can take to your own data center exactly yep okay so i guess since there's so
[2468.50 --> 2475.96]  much underlying tech under this and we all know what open source is the the most easy way to ask is is uh
[2475.96 --> 2481.60]  why isn't community edition free or i guess it is free but why isn't it open source is there a reason
[2481.60 --> 2486.20]  why you went the way you went with it or do you do you plan on having that as a paid version at some
[2486.20 --> 2492.70]  point so we're um you know we're evaluating our options there right now um you know we love open
[2492.70 --> 2498.04]  source we're a big contributor to mesos in fact uh and to marathon and chronos and other open source
[2498.04 --> 2505.14]  projects um uh so you know today the majority of code that we write is open source and um we've
[2505.14 --> 2508.76]  definitely had to you know we're having the conversation right now about dcs you know what
[2508.76 --> 2513.26]  should we do there should we make it entirely open source should we open and parts of it are already
[2513.26 --> 2520.50]  open source um so um so yeah we'll we'll make um we'll probably have some news there um sometime
[2520.50 --> 2526.36]  soon which which parts are open source right now um so so kind of the parts that i mentioned so mesos
[2526.36 --> 2533.30]  marathon and chronos and all the other uh frameworks that we're running like cassandra um you know the
[2533.30 --> 2538.14]  integration between cassandra and dcs for example kafka and dcs all that stuff is open source
[2538.14 --> 2544.40]  so the so earlier when we talked about terms and try to divide the lines a bit so apache mesos
[2544.40 --> 2551.60]  is different from mesos no that's the same thing okay apache mesos mesos same thing trying to make
[2551.60 --> 2557.96]  sure because i see it's a fork and i wasn't sure if it was is it your own flavor of the fork or is it uh
[2557.96 --> 2563.24]  the the real thing itself yeah so we work we work with apache mesos that's what we contribute to
[2563.24 --> 2570.48]  and and that's what that's the the version that goes into dcs also so what's uh so do you have any
[2570.48 --> 2575.08]  thoughts on the future of this then in terms of how it plays back in open source i know you got
[2575.08 --> 2580.42]  components in there but is it something where you know for example the one that comes to mind right
[2580.42 --> 2585.58]  now is just because the naming is so similar to is git lab right git lab has an enterprise version
[2585.58 --> 2590.06]  and has a community version and community is the open source free version and then enterprise is
[2590.06 --> 2596.78]  something you can buy and install or they even have hosted somewhere to github right yeah you know
[2596.78 --> 2603.82]  for us we we really think that um this is you know this makes operating infrastructure so much easier
[2603.82 --> 2608.74]  and we really want to give it to everybody you know we don't want to we don't want to hold those
[2608.74 --> 2615.30]  things back um and so that's why we have we already have a free community edition that you know
[2615.30 --> 2621.02]  there's no charge for it um the you know and and we're you know we're thinking hard about open
[2621.02 --> 2625.82]  sourcing it as well um you know has some implications of course but um you know we're
[2625.82 --> 2630.46]  we're thinking through that process right now yeah just curious because uh it seems like that would be
[2630.46 --> 2634.50]  the place to start if you were going to and i figured that was the question on every listener's
[2634.50 --> 2638.46]  mind is hey why isn't community free then or why isn't it open source if it's if it's free why not
[2638.46 --> 2644.88]  make it open source too right do you guys feel any pressure from because you are vc funded
[2644.88 --> 2650.50]  and investors uh on the open source front like do they push you away from it do they push you toward
[2650.50 --> 2658.82]  it is it a complete non-factor um so our our investors are really awesome you know it's um
[2658.82 --> 2665.06]  someone told me at some point it's like um well besides besides looking for money you know really
[2665.06 --> 2670.48]  look for a business partner and um you know our two biggest investors are our coastal adventures
[2670.48 --> 2676.36]  and uh and recent horvitz and they've been really great uh to work with and you know they really want
[2676.36 --> 2682.38]  to see this they want to see this uh be successful in the in the long run and um and they give us a lot
[2682.38 --> 2690.34]  of freedom to run the company so um it's you know it's really in a large part it's it's our decision
[2690.34 --> 2695.72]  you know how much we want to do open source and and how much we want to do closed um you know not
[2695.72 --> 2700.60]  really getting getting pressure from from the vcs on that and they see the value of the open source
[2700.60 --> 2705.80]  too and you know they've invested in other uh open source companies before um so you know they
[2705.80 --> 2712.00]  understand the model they see the benefits cool switching gears a little bit here i'm thinking
[2712.00 --> 2718.40]  about languages and um apache mesos itself a c plus plus project it seems like a lot of the
[2718.40 --> 2725.24]  projects built on top of it such as marathon are scala or is it scala i call it scala scala
[2725.24 --> 2731.84]  thank you scala so i'm right or at least according to a couple of us i'm right uh according to to me
[2731.84 --> 2738.62]  which you are yeah we'll let you have the final say so scala um yeah i'm just you know i'm a big
[2738.62 --> 2743.76]  fan of right tool for the right job and learning why tools are the right for particular jobs it seems
[2743.76 --> 2750.10]  like scala is well fitted for this space i'm wondering if you could speak to that yeah so
[2750.10 --> 2754.88]  actually we have um we're working in a lot of different languages in that in that layer and
[2754.88 --> 2760.98]  sort of the the dcos services layer um so yeah chronos and marathon are in scala um there's a bunch
[2760.98 --> 2765.48]  that are in java just you know because the project started that way for example cassandra
[2765.48 --> 2772.10]  and hadoop and hdfs and they're all uh they're all java and then there's go also um kubernetes
[2772.10 --> 2779.54]  is written in go um we're really language agnostic there so you can mesos has an api for a lot of
[2779.54 --> 2784.82]  languages um python in addition to those that we just mentioned i think someone wrote haskell bindings
[2784.82 --> 2790.20]  too so it's uh you know you can really use pretty much anything and it's it's pretty easy to write
[2790.20 --> 2795.72]  your own language bindings um mesos is right now getting a new hdp based api which will which will
[2795.72 --> 2801.58]  ship fairly soon so it'll be you know even easier to build language bindings um we picked scala
[2801.58 --> 2811.38]  originally um trying to think uh why why we picked that um you know at the time um so this was
[2811.38 --> 2818.26]  three years ago i think at this point uh when we started building chronos um you know java was still
[2818.26 --> 2826.06]  very it was a very popular language for systems engineering and um scala is also a jvm language
[2826.06 --> 2833.48]  and we found it to be you know more expressive than java um you know you had to write fewer lines
[2833.48 --> 2840.14]  of code um it allowed us to do functional programming which was really interesting um and so uh you know
[2840.14 --> 2844.18]  that's that's why we went with it it just seemed you know more modern more more effective and more
[2844.18 --> 2851.48]  efficient than uh in terms of you know uh the time it takes to write software um and uh so that's
[2851.48 --> 2857.54]  why we went with it at the time um but you know i completely agree with you i think it's all about
[2857.54 --> 2863.10]  you know finding the right tool for the job and um i think there's right now you know new exciting
[2863.10 --> 2868.04]  languages and systems engineering go is definitely getting a lot of um you know picking about a lot a lot
[2868.04 --> 2873.94]  of steam scala is getting more popular too there's a few new ones like rust um so we're really you know
[2873.94 --> 2878.96]  we're really language agnostic there so if you want to develop for the dcos um you're not tied to a
[2878.96 --> 2884.02]  specific language yeah but with a few years of experience looking back now on that decision
[2884.02 --> 2890.18]  uh do you feel like it was a good decision are you are you still bullish on scala are you uh you
[2890.18 --> 2895.78]  personally even because i noticed you've been writing some as well uh just curious your thoughts on it
[2895.78 --> 2901.00]  and then if you are personally looking at go or looking at these other things rust or if that's
[2901.00 --> 2908.86]  more as a company right so so personally i think um you know it looks like um the go community is
[2908.86 --> 2913.68]  really you know growing and and a lot of the newer tools that we're seeing in the systems engineering
[2913.68 --> 2921.92]  space are written in go so um you know today i would probably um build the thing in go um you know
[2921.92 --> 2928.84]  for that for that reason um i personally still like scala a lot um and i prefer it over over go
[2928.84 --> 2934.86]  actually it's um you know it it has go is a very simple language uh which is great you know it has a
[2934.86 --> 2941.22]  low barrier of entry um it's um you know the code that you write is very consistent because there's
[2941.22 --> 2946.92]  usually only you know only one way to do things or a few ways to do things um so those are huge
[2946.92 --> 2956.04]  benefits um scala you know is lets you do functional programming really well um and so you know they
[2956.04 --> 2962.04]  both have their strengths and weaknesses um for for a type of for a project like um you know a systems
[2962.04 --> 2967.92]  uh systems engineering project a cluster manager i would probably go with uh with go today probably
[2967.92 --> 2974.40]  still use scala for um say if i was doing something in data analytics you know spark based that's using
[2974.40 --> 2979.78]  scala or um you know wet backends and things like that i would probably still go with scala
[2979.78 --> 2985.66]  so all the uh all the folks who we've gotten recently as listeners to the show jared are
[2985.66 --> 2989.50]  pretty excited because we just came back from gopher con and most of those guys are
[2989.50 --> 2993.82]  either writing go or interested in writing go so they're their hands in the air except for when you
[2993.82 --> 3001.60]  said scala anyways well uh tell me we're gonna take a quick break i'll come back and ask you some
[3001.60 --> 3005.66]  really awesome closing questions but uh we're gonna take a break we'll be right back
[3005.66 --> 3012.86]  i have yet to meet a single person who doesn't love digital ocean if you've tried digital ocean
[3012.86 --> 3019.06]  you know how awesome it is and here at the changelog everything we have runs on blazing fast
[3019.06 --> 3025.26]  ssd cloud servers from digital ocean and i want you to use the code changelog when you sign up today
[3025.26 --> 3032.20]  to get a free month run a server with one gig of ram and 30 gigs of ssd drive space totally for free
[3032.20 --> 3039.22]  on digital ocean use the code changelog again that code is changelog use that when you sign up for a
[3039.22 --> 3043.92]  new account head to digitalocean.com to sign up and tell them the changelog sent you
[3043.92 --> 3051.18]  all right we're back uh great break there and we got some awesome closing questions that many many
[3051.18 --> 3057.06]  listeners are always just like i love when they ask those questions and the and the first question
[3057.06 --> 3064.06]  i think is is maybe a call to arms to be so of the projects you have out there from the cli to um
[3064.06 --> 3070.46]  to marathon to all the different projects you mentioned uh what are some call to arms some ways
[3070.46 --> 3073.96]  that the open source community can help rally around what you're working on or what you're doing
[3073.96 --> 3081.06]  to amplify what you're doing or to just step in and help out right yeah so you know i think
[3081.06 --> 3089.04]  the goal of things like marathon and and or you know the whole dcs is really to automate everything
[3089.04 --> 3097.96]  um so you know it's it's making uh making ops people's lives better sres um so if you're working
[3097.96 --> 3103.66]  in that field and uh you know you hate doing the same thing over and over again and um you hate
[3103.66 --> 3108.00]  you know getting working up in the middle of the night um because some random machine in your
[3108.00 --> 3115.00]  data center failed or in your cloud um you know may want to check out marathon and the dcs and um
[3115.00 --> 3122.30]  you know see if it works for your use case um and you know try it out and you know help us help us
[3122.30 --> 3129.32]  fix some bugs in there and help us make it work for even more use cases and the the github org that
[3129.32 --> 3134.56]  you guys operate off of is just slash mesosphere right that's right yeah github slash mesosphere
[3134.56 --> 3139.66]  tons of stuff on there you know from little weekend projects that some of our guys are working on um
[3139.66 --> 3144.16]  there's some really cool stuff there actually so uh you know i don't know if you guys have any uh
[3144.16 --> 3149.64]  hpc high performance computing listeners but um we have a couple guys on the team that are playing
[3149.64 --> 3156.24]  with stuff there like mpi um so so yeah some some really cool things there also you know if you want to
[3156.24 --> 3161.66]  get started um developing for the dcs or building a distributed system if you've never done that
[3161.66 --> 3167.44]  um there's a really cool example project on our github called rendler uh it's a rendering web crawler
[3167.44 --> 3172.98]  so you you know it crawls the web renders all the pages shows them in a big graph um and it's basically
[3172.98 --> 3178.82]  example code for developing a distributed system on on top of the dcs very cool um it's in a lot of
[3178.82 --> 3183.78]  different languages i think we have scala java python you know bunch of others so it's a really good
[3183.78 --> 3188.58]  place to get started it's called wrangler is that right rendler rendler okay i just found it yeah
[3188.58 --> 3195.18]  it's a couple pages back in the we'll link to some of the show notes but it's it's uh r-e-n-d-l-e-r
[3195.18 --> 3203.30]  rendler right and it seems like it's uh you know based on the the guy here on the read me it looks
[3203.30 --> 3210.40]  like joker is it the joker it's the um what is that you know what's the guy i think it's riddler
[3210.40 --> 3215.52]  riddler okay yeah riddler i know there was something like that it looked like joker for a
[3215.52 --> 3219.76]  second but it was riddler but anyway yeah well you're not kidding when you say you have a lot of
[3219.76 --> 3224.90]  open source stuff out there because six pages on there uh slash mesosphere and i think there's a
[3224.90 --> 3230.56]  lot i think it's 20 per page some of those are forks obviously um but still lots of lots of cool
[3230.56 --> 3236.26]  repos out there for those who want to go digging yep next question one we cannot skip everyone's
[3236.26 --> 3243.28]  favorite is who is your programming hero my programming hero i think is mark andreessen
[3243.28 --> 3249.88]  because um you know the guy did so much he wrote um really the first usable web browser
[3249.88 --> 3257.84]  um back in the day and um you know he did he did so much for um making the internet uh what it is you
[3257.84 --> 3263.90]  know went on to start netscape which um you know at the time they came up with javascript um the
[3263.90 --> 3269.40]  netscape browser of course um the netscape application server which you know back then
[3269.40 --> 3275.54]  was basically the way to build web applications you know the equivalent of node.js and and ruby
[3275.54 --> 3283.42]  and rails and all of those tools that we have today um so yeah he's my hero very cool and uh
[3283.42 --> 3287.50]  a question we don't ask every single show but i love asking this question which is what's on your
[3287.50 --> 3293.04]  open source radar so if you've got a weekend or even a week where you could just like take a
[3293.04 --> 3297.02]  vacation that's not really like traditional vacation where you just go and travel and have
[3297.02 --> 3302.50]  fun you actually like maybe you know go travel have fun and hack too it's a hackation or something
[3302.50 --> 3306.92]  like that i don't know but if you had some time where you weren't forced to work on what you work
[3306.92 --> 3312.38]  on daily uh either by your own passions or your own commitments if you just could take a weekend or a
[3312.38 --> 3318.00]  week what would you play with what would you work on yeah um so yeah you know obviously our open
[3318.00 --> 3322.94]  source projects there's there's a ton of them that's um i would definitely work on those but
[3322.94 --> 3329.84]  you know things things that we aren't working on as a company um i can think of two um there's a
[3329.84 --> 3336.50]  really cool um deep learning framework um also uh managed by uc berkeley it's called cafe
[3336.50 --> 3342.82]  um so lets you do you know deep learning neural networks um that's kind of a you know machine
[3342.82 --> 3349.90]  learning is kind of a passion of mine um so i'd probably check that out um cafe and the other
[3349.90 --> 3355.00]  one i'd take a look at uh it's it's a monitoring tool uh built by soundcloud it's called prometheus
[3355.00 --> 3360.80]  um that looks really cool too oh wow adam that's probably check those out that's a good t-up because
[3360.80 --> 3364.98]  that's our next episode isn't the next episode it's definitely in the close pipeline i can't remember
[3364.98 --> 3369.64]  if it's next or second to next but yeah we're having the prometheus team on uh i think it is next week
[3369.64 --> 3375.48]  actually yeah it is it's after this show right on it's like julius holtz and uh is it just julius
[3375.48 --> 3379.16]  coming on the show or who else was coming on the show probably just julius but possibly bjorn as well
[3379.16 --> 3385.08]  bjorn would be awesome those guys were so awesome cool yeah we hired um we have we have a few
[3385.08 --> 3391.04]  soundcloud people here and they're all they're all raving about it yeah we'll be talking to prometheus
[3391.04 --> 3397.94]  soon so then you can tune into that episode so so you got uh cafe which is a deep learning uh don't
[3397.94 --> 3402.22]  know what you describe that as deep learning framework yeah or a toolkit for for deep learning
[3402.22 --> 3410.40]  so why prometheus so i think um you know i'm i did a lot of ops in my career a lot of you know a lot
[3410.40 --> 3417.84]  of sre and so monitoring tools is always um it's always a hot topic um there's just so many shitty
[3417.84 --> 3423.76]  tools out there um so you know prometheus really looks like like something fresh something something
[3423.76 --> 3430.64]  different um i haven't really you know taken it uh tried it out yet so um that would be that would
[3430.64 --> 3435.30]  be my first thing to do is just get it up and running and fire some data at it and and see what
[3435.30 --> 3440.84]  it does just play with it very cool well uh toby it was really awesome having you on the show for
[3440.84 --> 3445.26]  those who don't know how to reach out to you what's the best ways to get in touch twitter github
[3445.26 --> 3453.36]  twitter works um my twitter handle is uh is super gunter so that's how you can find me we'll link to
[3453.36 --> 3461.80]  that one super gunter that's awesome uh cool man so any of the any of the closing thoughts before
[3461.80 --> 3467.76]  we close out the show for yourself this was fun this is fun all right that's a good closing thought
[3467.76 --> 3473.28]  all right well i want to say a huge thanks to everyone who listens to this show and specifically
[3473.28 --> 3479.14]  uh those members out there that support this show we're member supported we're also sponsored so
[3479.14 --> 3484.08]  the sponsors we have for the show are code ship top towel and digital ocean for this show
[3484.08 --> 3489.18]  uh we love those guys to make this show possible jared you're awesome and toby you're awesome for
[3489.18 --> 3494.10]  joining us as well today uh until next week when we talk about prometheus let's say goodbye guys
[3494.10 --> 3496.70]  see ya see ya goodbye
[3496.70 --> 3512.30]  it'snt team
[3512.30 --> 3516.76]  you
[3516.76 --> 3519.84]  you
[3519.84 --> 3549.82]  Thank you.
