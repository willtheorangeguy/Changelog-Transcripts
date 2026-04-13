[0.00 --> 15.12]  welcome back everyone this is the changelog and i'm your host adam stokowiak we're member
[15.12 --> 21.36]  supportive blog podcast and weekly email covering what's fresh and what's new in open source check
[21.36 --> 26.96]  out the blog at the changelog.com our past shows at five by five dot tv slash changelog
[26.96 --> 31.82]  and subscribe to the changelog weekly it's our weekly email covering everything that hits our
[31.82 --> 36.76]  open source radar you don't want to miss it we ship it on saturdays and you can subscribe at
[36.76 --> 42.66]  the changelog.com slash weekly this show is hosted by myself adam stokowiak as well as our awesome
[42.66 --> 49.30]  awesome host andrew thorpe and this is episode 115 and today's show is sponsored by our good
[49.30 --> 54.42]  friends at digital ocean and our good friends at top towel and we'll tell you a bit more about top
[54.42 --> 59.16]  top here in just a bit but we're huge fans of top towel they connect startups businesses and
[59.16 --> 65.14]  organizations and people like you to a growing network of elite engineers all around the world
[65.14 --> 69.88]  so if you've been wanting to freelance call up top towel tell them we sent you they're gonna love who
[69.88 --> 75.98]  you are but uh huge fans of digital ocean we want you to get hosted on digital ocean today we're on
[75.98 --> 83.06]  digital ocean we absolutely love it uh blazing fast ssd cloud servers you can easily spin up a new
[83.06 --> 91.66]  droplet with root access within 55 seconds with your choice of size ram uh region os it's really
[91.66 --> 96.66]  really easy they got a simple and easy to use dashboard and for our fans across the pond they
[96.66 --> 100.76]  recently announced their brand new data center in amsterdam super awesome stuff going on there
[100.76 --> 106.18]  and they're going to continue to invest heavily into their infrastructure worldwide as more and more
[106.18 --> 110.74]  data centers are added throughout their throughout the world but we want you to try digital ocean today
[110.74 --> 118.56]  for free using our promo code changelog sent me that is changelog sent me with uh which will get you a
[118.56 --> 123.68]  ten dollar hosting credit or basically two months free if you're uh if you're on their base plan but
[123.68 --> 130.76]  head to digitalocean.com to get started and now on to the show we're joined today by jonathan
[130.76 --> 135.54]  rudenberg and jeff lindsey to talk about the flynn project welcome to the show guys it's great to be here
[135.54 --> 142.44]  yeah so we had you guys on the show uh previously but things have changed quite a bit at flynn so
[142.44 --> 148.96]  for the listeners that um maybe either haven't heard the show shame on them or are catching up
[148.96 --> 152.20]  why don't you guys give us an introduction of who you are and what you guys are doing
[152.20 --> 162.60]  uh well i'm mostly a freelance engineer but i've been working on this project um with jonathan uh to
[162.60 --> 171.26]  basically build this sort of ideal platform or uh basically the system that i've i've always wanted
[171.26 --> 179.78]  to work with at every company i've worked at um and so that's sort of me and my involvement yeah um
[179.78 --> 186.44]  i'm uh mainly working on flynn right now i also work on the tent protocol and a few other open source
[186.44 --> 192.92]  projects i basically all of my work is open source at this point uh and so flynn tries to be uh
[192.92 --> 199.94]  essentially a platform for uh developers to deploy their work on and that can be anything from a web
[199.94 --> 207.12]  application to like stuff that anything runs on linux essentially it's runs in containers um so the
[207.12 --> 213.08]  idea is that it's the product that an operations team can provide to an engineering team and i mean that
[213.08 --> 217.60]  could be someone as you know just a single developer who maybe does a little bit of ops on
[217.60 --> 223.40]  the side runs out of vps all the way up to like a startup that um has a full like service-oriented
[223.40 --> 228.96]  architecture with lots of different components exactly just speaking purely about like the the
[228.96 --> 233.80]  growth of the project so we had you guys on the show it was about three or four months ago now
[233.80 --> 238.28]  where do you guys remember like where you were at then and kind of what's changed since august
[238.28 --> 245.32]  yeah so uh at that point we were basically at the end of our fundraising period and we um
[245.32 --> 250.40]  uh we hadn't really written much code yet we'd done a lot of the architecture work uh but there
[250.40 --> 255.84]  was very little code available uh and we were still doing in the planning stages essentially
[255.84 --> 263.52]  um so we're much farther along now um we have uh prototype components of just about everything that
[263.52 --> 269.20]  we plan to build uh and we have some releases coming up this month and next month uh essentially
[269.20 --> 275.54]  like completing the work that uh was funded in august right so the so the layer zero release is set to
[275.54 --> 281.00]  is that coming out this month or is the layer one going to come out yeah so uh flint has two layers uh
[281.00 --> 286.98]  layer zero will be released uh probably around the end of december and then layer one is scheduled for
[286.98 --> 292.86]  the end of january gotcha so what what would you say in the last couple months has been like the
[292.86 --> 297.48]  i don't know not the biggest change but just in you know you guys kind of went out there and you had
[297.48 --> 302.56]  a pretty successful fundraising experience and so since then now you guys obviously have a lot more
[302.56 --> 307.08]  um you know news behind you people know about flint and you guys are actually starting to put some
[307.08 --> 312.60]  some code out there for people to kind of start to consume so since that in that time like what would you
[312.60 --> 317.22]  say has been the biggest struggle with maintaining this open source project but also now you have
[317.22 --> 325.96]  demands and expectations because people have funded this thing well uh i mean putting code out there um
[325.96 --> 334.90]  i'm actually more personally i i uh am not so uh afraid of putting code out i i i uh do a lot of open
[334.90 --> 340.92]  source projects although the the attention that this one has gotten is kind of interesting because i'll build
[340.92 --> 347.24]  a component that's sort of like it's a placeholder component um i'm talking about shelf yeah um which
[347.24 --> 353.94]  is one it's just like a little http um you know file services like the simplest thing and we put it up
[353.94 --> 360.66]  as a placeholder uh um because it kind of serves the job that we need right now and all of a sudden
[360.66 --> 366.76]  people are submitting patches to it and there isn't even a really a readme um and so just the number of
[366.76 --> 375.04]  eyeballs um has made the experience a lot more enjoyable yeah um yeah um i also publish a lot of
[375.04 --> 380.74]  open source code um so i'm used to people looking at stuff and i'm not really afraid to push things
[380.74 --> 385.86]  but uh just the amount of attention is really interesting there's a it's uh it's really nice
[385.86 --> 389.42]  to push something and see that people are already using it the next day just kind of experimenting
[389.42 --> 394.08]  figuring out what's going on and unfortunately our our docs are rather lacking in the readme department
[394.08 --> 398.76]  right now but people are struggle to get things set up um so the one thing that i do want to point
[398.76 --> 404.62]  out uh before i get too far is that we actually have a demo of flynn um available that uh you can
[404.62 --> 410.06]  essentially boot up uh all the prototype components in vagrant and just test out you can do like a sample
[410.06 --> 416.82]  get push deploy scale up scale down look at the logs etc very much like heroku um and so uh we plan to
[416.82 --> 421.00]  obviously develop all these components further and we are doing that currently but uh if you're
[421.00 --> 425.96]  interested in just like experimenting with like the very alpha flynn uh it's available right now
[425.96 --> 431.40]  we released that uh last month so in like a kind of just layman speak what would you guys say is like
[431.40 --> 437.36]  the the roadmap for like a uh production ready version of flynn that people can actually start to use
[437.36 --> 445.18]  like yeah you know so uh at the end of this month we're releasing uh layer zero flynn layer zero is
[445.18 --> 450.96]  essentially everything you need to schedule and run containers on a cluster of nodes um so this is
[450.96 --> 457.66]  much closer to something like mesos than it is to heroku it's very low level and then next month uh
[457.66 --> 465.24]  we are going to release uh layer one uh in a working configuration that is close to heroku it'll
[465.24 --> 470.50]  probably be very bare bones compared to heroku but this is this will be suitable for deploying
[470.50 --> 474.74]  like probably just like internal apps that you have at your company or if you're just like a
[474.74 --> 481.52]  hobbyist experimentation etc uh and then over the coming months we will be working on uh improving
[481.52 --> 489.06]  the stability and fixing bugs and uh adding features etc um to bring it to something hopefully that
[489.06 --> 496.30]  in mid 2014 will be usable to serve production traffic yeah that's crazy so you guys are i mean it's so
[496.30 --> 500.32]  young and when i remember when i when we brought you on the show last time i believe the only actual
[500.32 --> 505.44]  uh repository on github you had was flint spec is that right i that's absolutely true there was
[505.44 --> 510.32]  there wasn't a single line of code written yeah and now i just look at the the you know the uh
[510.32 --> 515.82]  the repositories you guys have and it's crazy like the amount of growth is has been shocking and it's
[515.82 --> 520.74]  only been a few months so i mean how has the other work that you guys have been doing with tent
[520.74 --> 529.42]  and with other things struggled or or has it at all um so i still do work on tent um i've been
[529.42 --> 534.88]  focusing on flint um because i really really needed to get uh tent to the next level because
[534.88 --> 541.42]  we're actually going to be deploying our uh tent server on flint and releasing that uh in a nice
[541.42 --> 546.30]  packaged version i don't know whether you've ever tried to deploy like an open source rails app or
[546.30 --> 552.28]  anything like that deploying complex services currently even open source ones tends to be very
[552.28 --> 558.42]  complicated so i'm excited for what flint can do for deploying open source stuff as well um so that you
[558.42 --> 565.06]  could for instance run a very robust tent server on uh your own server and using flint and the
[565.06 --> 570.16]  management and operations of it would be very simple compared to what you'd be used to deploying
[570.16 --> 574.22]  just about any other open source application uh so that's why i've been focusing on flint lately
[574.22 --> 579.64]  and um but uh tent is definitely bouncing around the back of my mind to be honest it's been great to
[579.64 --> 583.40]  have a break from like thinking about tent full-time and just kind of switching to something else
[583.40 --> 588.36]  because you you you just think of different things when you uh when you have something bouncing around
[588.36 --> 593.22]  in the back of your mind instead of thinking about it full-time right what have you guys thought about
[593.22 --> 598.90]  doing this in go i mean go is still pretty young and and you know it's a i don't know it's it's it's
[598.90 --> 602.56]  definitely a powerful language and it's got a lot of acceptance but have you guys kind of ran into
[602.56 --> 608.56]  any gotchas that have hit you at this point um the only thing is dependency management that's the only
[608.56 --> 614.44]  thing i'm aware of that uh is a problem at all and there's there's some solutions in the works uh
[614.44 --> 620.40]  go dep looks like the best option right now um but that's basically the only thing that's bitten us i
[620.40 --> 626.78]  think jeff yeah no i've i've really loved it i feel like i've also become a better programmer using it
[626.78 --> 631.14]  it's awesome yeah you have to learn a little bit more about like you know lower level stuff and
[631.14 --> 636.08]  stuff that you might have taken for granted if you work more in you know higher level stacks so it's cool
[636.08 --> 640.74]  absolutely so let's talk a little bit i mean the last time we had you on the show it was it was
[640.74 --> 645.94]  flint spec that's all there was you guys now have a a working demo and and you're close to your layer
[645.94 --> 650.84]  zero release let's talk a little bit about um now that we have the ability what flint is and and kind
[650.84 --> 655.58]  of take a deep dive into flint and who it who it might work for and um you know what what it would
[655.58 --> 661.10]  look like for a production application so what what's what would you say is the the elevator pitch for
[661.10 --> 669.74]  flint okay so and i said this before flint is the product that operations provides to engineering
[669.74 --> 675.94]  so what that means is that instead of um doing like one-off deployments of applications where you
[675.94 --> 682.26]  have to write chef or puppet scripts just to deploy a single application you uh as an operations team
[682.26 --> 687.54]  you are managing this platform that engineering can then use to deploy and manage the applications
[687.54 --> 696.02]  themselves it's very self-serve and you also get the uh the consistency of configuration so if you have
[696.02 --> 700.12]  a bunch of applications that all use my sequel they're all using my sequel in the exact same way
[700.12 --> 705.80]  um we have these things called service appliances uh which jeff can explain that make this very simple
[705.80 --> 712.98]  yeah so well service appliances are are kind of neat um they're sort of eat every component of
[712.98 --> 720.98]  flint is is basically a a almost a standalone appliance um and we think of these as basically uh
[722.98 --> 731.06]  so uh software is a service in a box um so each of the components has its own uh api and is actually
[731.06 --> 739.06]  made to be to to work in a cluster um so for example we talk about things like a mysql
[739.06 --> 746.52]  uh appliance um or any other kind of database appliance it has kind of a master slave uh clustering setup
[746.52 --> 754.30]  um the ideal is to basically spin up a couple of these appliances and they would um via our
[754.30 --> 761.56]  service discovery infrastructure be able to self-organize into a master slave um and provide a lot of the
[761.56 --> 767.60]  uh administrative functions that you would normally do by logging into the machine via an api so that
[767.60 --> 775.80]  you could then write um your own uh code or systems to then to manage them in a in a consistent way as
[775.80 --> 784.30]  opposed to um using tools that assume that you ssh into hosts because very very much flint is about
[784.30 --> 791.94]  abstracting away the host um it kind of pushes um you to think more about services and service-oriented
[791.94 --> 799.44]  architecture and for the most part hosts are pretty um kind of homogenous i mean you still the operators
[799.44 --> 806.46]  still have to know you know which hosts um they still actually can manage the hosts but in terms of
[806.46 --> 812.80]  um what goes where that's mostly taken care of by uh the systems that you would be building with flint
[812.80 --> 817.44]  yeah the only decision you're going to really make is just like you're going to pick a few classes of
[817.44 --> 823.32]  nodes that you have uh deployed so maybe you have like high memory nodes for doing caching and uh high
[823.32 --> 829.32]  disk nodes for doing uh like databases that kind of stuff but other than that um you're going to be
[829.32 --> 833.82]  just managing everything through flint and you don't think about the host you just think about what
[833.82 --> 839.88]  you're running uh on your cluster so you say you know i need a highly available my sequel deployment i
[839.88 --> 846.32]  need a highly available postgres deployment and then this application uh needs to connect to that and
[846.32 --> 851.64]  it's just going to keep on working even if one of those nodes goes down you can scale up scale down
[851.64 --> 857.04]  without really thinking about where things are running unless you really need to and you yeah
[857.04 --> 864.02]  no keep going go ahead go ahead okay you always have the um the ability to to kind of drop to a lower
[864.02 --> 868.72]  level and say hey i actually know exactly where this job should be running for instance for like data
[868.72 --> 874.18]  locality if you're doing lots of like map reduce jobs you would want the jobs to run uh near the data on
[874.18 --> 879.30]  the same nodes possibly right you talked a little bit about how like deploying open source applications
[879.30 --> 884.54]  is a pain how does flynn you know i don't know when you're when you're talking about deploying let's
[884.54 --> 888.18]  say you're talking about deploying a rails application and you have all the you know the kind of de facto
[888.18 --> 891.92]  standards for deployment you have whether it's heroku or you're doing you're rolling your own thing
[891.92 --> 896.42]  with capistrano or you know those things how does flynn help to alleviate the deployment issue that you
[896.42 --> 903.38]  you kind of talked about um so in the case of a rails app uh most rails app these days are going to
[903.38 --> 906.16]  work on herokio so it's going to be very similar
[906.16 --> 918.76]  sounds like we had a uh yeah sorry completely forgot to silence my phone i'm sorry no that's okay
[918.76 --> 926.34]  we'll edit this out probably not but it'll be funny in the show okay uh silenced so um
[926.34 --> 932.94]  so the question was uh you know how does how does flynn help to alleviate like the deployment issue that
[932.94 --> 941.38]  you mentioned before yes so rails applications uh typically on heroku you're just going to get
[941.38 --> 946.30]  pushed them you're going to say i need a postgres add-on i need memcache whatever um that's great
[946.30 --> 950.16]  except when you don't want to run your application on heroku when you want to run it on your own
[950.16 --> 954.86]  infrastructure perhaps you have a vpn that you need to have this service behind or you have your
[954.86 --> 959.60]  own hardware or you know there's a variety of situations where you'd have this you could deploy
[959.60 --> 963.68]  those applications in exactly the same way because flynn is compatible with roku applications
[963.68 --> 971.08]  but you perhaps you have an application that consists of multiple services um that are more
[971.08 --> 976.84]  complex to orchestrate uh flynn gives us all the hooks we need to deploy that and the exact way we're
[976.84 --> 980.88]  going to do that is not been completely sorted out yet but the idea is that you have a manifest that
[980.88 --> 988.06]  describes you know exactly what services are required and you can um run those uh on flynn very
[988.06 --> 993.92]  easily and deploy those and running running and deploying those backing services uh is pretty much
[993.92 --> 1001.86]  the exact same uh as you would deploy the application so it actually you know the difference i think when
[1001.86 --> 1007.24]  you when you're working with a rails application uh at first you're worried about deploying the rails
[1007.24 --> 1011.56]  application but you also have to worry about deploying the database server and then later you have
[1011.56 --> 1017.72]  to worry about deploying caching server and then later you have to worry about deploying um you know
[1017.72 --> 1025.26]  some sort of background worker type system and very often a couple people um talk about this quite a
[1025.26 --> 1031.32]  bit most a lot of web application development starts simple but eventually turns into this very
[1031.32 --> 1036.44]  service-oriented type of architecture you have a number of it's more complex than just this sort of
[1036.44 --> 1043.40]  three-tier um architecture and so as an especially larger organizations either as you get bigger
[1043.40 --> 1049.94]  existing large organizations have a fairly service-oriented architecture and they get to a
[1049.94 --> 1055.54]  certain size where even their application is broken down into smaller pieces or services and so that's
[1055.54 --> 1063.34]  the sort of thing that flynn really helps um uh support because you you you can manage and deploy all
[1063.34 --> 1069.00]  these things pretty much the same way you would a heroku application yeah so it's interesting because
[1069.00 --> 1072.86]  when you talk about like service-oriented architectures it it sounds to me like flynn
[1072.86 --> 1079.56]  is a great solution for just the more complex i mean heroku is great right heroku has enabled a lot of
[1079.56 --> 1086.64]  things that are you know it makes a pretty uh what could potentially be a difficult task as long as you're
[1086.64 --> 1091.56]  running a relatively generic setup pretty simple and it sounds like flynn kind of is going to take that
[1091.56 --> 1096.48]  to the next level which is going to make the the more complicated tasks relatively simple is that i mean
[1096.48 --> 1101.96]  would that be accurate to say that's absolutely accurate um and i should point out that we wouldn't
[1101.96 --> 1107.90]  have flynn without heroku because heroku kind of demonstrated a lot of the concepts that were just
[1107.90 --> 1114.06]  kind of taking a bit further in flynn um so flynn absolutely it starts with like something like a
[1114.06 --> 1118.92]  heroku app and probably a lot of people will just use that functionality of just like get pushing your
[1118.92 --> 1125.12]  applications it's very natural right now uh to do that because we're familiar with roku etc but then you
[1125.12 --> 1130.56]  can kind of dive in and say i actually have more complicated application for instance i could build
[1130.56 --> 1137.40]  a tool that does continuous integration and then continuous deployment so i run my tests using flynn
[1137.40 --> 1144.64]  and then uh the output of those tests is a a build artifact that literally is a container image and then i am
[1144.64 --> 1150.20]  going to perhaps manually or automatically deploy that image the exact same image that came out of the
[1150.20 --> 1157.72]  tests and deploy that to production on flynn yeah so i mean so just to just to be clear like this is
[1157.72 --> 1163.48]  built on top of docker right and and docker is one of the things that has kind of helped to enable some
[1163.48 --> 1170.88]  of these like what's the best way to put it these like box development or you're deploying the i think
[1170.88 --> 1178.10]  docker's really um pioneered this model of like a high level container that's what container i was
[1178.10 --> 1183.36]  couldn't think of the word yeah thank you um because i containers have been around for a long
[1183.36 --> 1189.04]  time or things like containers but docker really introduced sort of this um you know slightly more
[1189.04 --> 1196.54]  vm like model for containers um that i think uh is actually a bunch of people are kind of pushing that
[1196.54 --> 1203.02]  to be an open standard so there will be docker competitors and stuff um but uh but yeah right now
[1203.02 --> 1208.18]  it's all based on a lot of the amazing work that um the the docker guys have done so one of the
[1208.18 --> 1212.56]  questions i kind of have for you is like docker in the last couple months has changed a bunch too i
[1212.56 --> 1217.68]  mean and it's continued to evolve and grow and get and become a full-time project and essentially like
[1217.68 --> 1222.52]  take over the company and so have you guys had any issues with that or is it has it pretty much been
[1222.52 --> 1227.68]  in lockstep with what you guys are doing um they're taking docker in various directions adding
[1227.68 --> 1233.02]  features mostly focusing on like single host use cases whereas we're very much focused on the the
[1233.02 --> 1240.88]  multi-host use cases of containers um so a lot of their uh their features are not currently being
[1240.88 --> 1247.48]  used by flint yeah but i i think um i mean they've gotten a lot of attention and so they've also gotten
[1247.48 --> 1254.30]  a lot of contributors and a lot of people pulling it in a lot of different directions um which is great
[1254.30 --> 1262.06]  to kind of get all those ideas out um and but uh i think you know at the core there's a really simple
[1262.06 --> 1270.92]  idea in there um so but the other thing is a lot of people are still trying to catch up to thinking
[1270.92 --> 1282.58]  in terms of containers um and so that's um you know kind of uh it's it's great for us because we're
[1282.58 --> 1292.48]  based on this concept of of containers um and uh but it's sort of like we're still docker's doing an
[1292.48 --> 1299.42]  amazing job it's basically prepping everybody for flint yeah yeah yeah um it's it's great to see
[1299.42 --> 1303.92]  people thinking about the different ways that you can deploy applications because for a long time it
[1303.92 --> 1311.56]  was it was you know standardized on things like capistrano and uh fabric which um are great and they've
[1311.56 --> 1315.52]  they've gotten us a really long way but there's there's lots of new and exciting ideas that we can
[1315.52 --> 1320.32]  have about how to do this yeah how much of your like day is spent not not day but how much of your
[1320.32 --> 1324.68]  you know time is spent like defending hey how does this compare to heroku what is this as compared
[1324.68 --> 1328.48]  to heroku or docker you know how how does this relate like how much do y'all have to clarify that
[1328.48 --> 1335.12]  when you're explaining flint to somebody um not much i mean to be honest it's uh mostly comparing
[1335.12 --> 1342.96]  to perhaps other open source passes um cloud foundry yeah cloud foundry um mostly uh most
[1342.96 --> 1347.82]  people get it like it's uh at a very simple level it's heroku that you can run on your own hardware
[1347.82 --> 1352.94]  we don't compete with heroku really the the people that want to use heroku aren't people that want to
[1352.94 --> 1358.96]  use flint because you need to have some operations support in order to run flint you don't need that
[1358.96 --> 1366.78]  with heroku that's the feature that heroku provides is operations yeah and it's kind of nice um when
[1366.78 --> 1371.48]  you're we were talking about earlier if you when you start with a simple application you can run it
[1371.48 --> 1378.08]  on heroku um you get to a certain point where uh people kind of need to need slightly more than
[1378.08 --> 1384.40]  heroku and really their only choice after that is to redo everything or sometimes they'll be afraid
[1384.40 --> 1389.80]  to use heroku um because they know that at some point they'll outgrow it and have to go basically
[1389.80 --> 1396.32]  back to um you know host-oriented architecture cloud you know like ec2 or something and all that
[1396.32 --> 1403.74]  infrastructure that heroku provided is gone um and so hopefully flint will kind of fill in the gap
[1403.74 --> 1412.48]  between ec2 um and heroku but kind of in a way i i it's sort of like um in terms of uh in terms of
[1412.48 --> 1417.70]  operations but in in a way flint is more than heroku i almost think of it like heroku plus plus
[1417.70 --> 1424.20]  in terms of the software because it gives you so much more power um because it's basically heroku
[1424.20 --> 1430.16]  given to you inside out you have control over you know how it works you know it's really interesting
[1430.16 --> 1434.66]  that you say that because i wonder if like the the future for flint and maybe you can kind of speak
[1434.66 --> 1440.18]  to this is somebody you you want to encourage people hey start out with heroku it's it's painless it
[1440.18 --> 1444.44]  doesn't take much configuration you don't have to know much about operations at all and then as you
[1444.44 --> 1450.72]  start to grow and and your your demands grow flint kind of steps in as the next evolution for the apps
[1450.72 --> 1457.44]  that are on heroku how would you feel about that kind of like a flow for people i mean that's great
[1457.44 --> 1464.60]  you can also start out with flint um but because a lot of people i think um are a little hesitant
[1464.60 --> 1470.58]  like if it's something really a really simple application um you know pretty standard uh heroku
[1470.58 --> 1477.04]  a lot of the time just um you know does the trick um but there's so many times when people don't think
[1477.04 --> 1483.44]  that heroku will do the trick and i think in those cases people might want to start with flint um and
[1483.44 --> 1492.56]  and you know even if your app is really simple um hopefully flint is um so extremely simple to set up
[1492.56 --> 1500.40]  that the uh you know kind of overall you know it is a kind of a complex system um but overall it
[1500.40 --> 1505.00]  should be easy to set up and that it's worth it because you're going to grow with it uh as opposed
[1505.00 --> 1510.90]  to trying to and and it sort of has a path for you right as you uh as your system gets larger as
[1510.90 --> 1516.70]  opposed to you kind of doing your own thing and having to relearn everything and try out a lot of
[1516.70 --> 1524.94]  different um approaches um to to scaling your application in terms of both complexity as well
[1524.94 --> 1531.10]  as handling load and stuff um so i think with flint we're kind of baking in all these kinds of
[1531.10 --> 1538.46]  best practices right um and ideas from you know google and twitter and basically every every everything
[1538.46 --> 1544.32]  we've learned from from all that stuff and and putting it into a package for you right so you talk
[1544.32 --> 1548.98]  about getting started with flint so and and one of the things you mentioned was you're you're behind
[1548.98 --> 1554.62]  on like the docs um thing so how will somebody get started with flint i mean just plain and simple
[1554.62 --> 1561.66]  um i mean if you're using amazon web services you're probably just going to boot an ami that contains
[1561.66 --> 1567.04]  flint in the case of um running it on your own hardware you're going to start with a base os
[1567.04 --> 1572.82]  and currently you would just install docker and then probably run one or more docker containers which
[1572.82 --> 1577.86]  would then uh talk to docker and get everything else set up uh it'll be very simple but as far as
[1577.86 --> 1582.62]  like education on flint and and so obviously like getting up and running with flint is going to be
[1582.62 --> 1587.70]  pretty painless but as far as like how to take flint to the next level and configuration and all that
[1587.70 --> 1594.08]  stuff where will that exist for you guys i think so that that spec that we had last time we talked
[1594.08 --> 1600.20]  is actually kind of want to turn that into like a guide um that's sort of you know we would have our
[1600.20 --> 1605.74]  normal sort of getting started and here's the basic usage stuff but um i kind of envision a guide
[1605.74 --> 1612.30]  that is sort of um a really great sort of user's manual both for operators as well as engineers
[1612.30 --> 1619.36]  um to sort of understand how the system works and how they can make it work for them um and so that's
[1620.04 --> 1626.42]  you know i guess kind of kind of the vision yeah um obviously we'll have documentation on the website
[1626.42 --> 1633.00]  um at varying levels of detail um depending on what you're interested in right so you guys were
[1633.00 --> 1639.30]  hosted a meetup uh i guess last month is that right yes what was it yeah we had a meetup in san francisco
[1639.30 --> 1647.34]  so what was that experience like for you guys it was really interesting um there i really wasn't
[1647.34 --> 1652.92]  expecting so many people to show up we had like i think 40 or 50 people show up and um and then to
[1652.92 --> 1658.38]  have most of them pretty much all of them get it yeah a lot of people got it it was good you guys
[1658.38 --> 1665.78]  were in the twilio offices yeah twilio um i i'd have i'd been there a couple of times since they moved
[1665.78 --> 1670.80]  but you know they're pretty nice setup awesome yeah really nice space for meetups it's really cool to
[1670.80 --> 1675.74]  see i mean you know i'm just kind of trying to not harp on it but i just it's cool to me that that we
[1675.74 --> 1680.40]  had you guys on the show at such a young you know a young part in flynn's future and obviously
[1680.40 --> 1684.38]  we were talking about fundraising at that point and and trying to help you guys get off the ground
[1684.38 --> 1690.34]  and it's it's really cool to me to see a project like this just take off and you know from the
[1690.34 --> 1695.16]  ground floor it's two guys sitting you know working on this thing and well two guys in the open source
[1695.16 --> 1701.04]  community working on this thing and you know just to see it like take off like you guys have been able
[1701.04 --> 1708.20]  to to do this so you know i just want to get into that what has the experience given you know in terms
[1708.20 --> 1713.24]  of flynn and and the future of flynn and and what has the experience been like for other people who
[1713.24 --> 1718.64]  you know potentially could get into something that would take off like this what what what should they
[1718.64 --> 1723.64]  expect what should be something to look out for and you know the thing that i hear a lot of is demands
[1723.64 --> 1728.48]  from the community and you you start off with just this idea it's just you and your friend and
[1728.48 --> 1734.86]  you know you start off and it becomes a bigger deal because people have invested money and i and i'm
[1734.86 --> 1740.14]  curious to know and and i want to kind of tie this into the the fundraising goals you you have for the
[1740.14 --> 1745.74]  project in in the coming year but i'm curious to know was there any added pressure once that happened
[1745.74 --> 1754.94]  maybe the approach of our fundraising kind of helped uh you know we we talked about how we focus more on
[1754.94 --> 1761.56]  on companies um that were willing to to work with us and understood um how it worked i think if we took a
[1761.56 --> 1769.26]  more traditional uh you know kickstarter ask anybody can can put in a little bit of money
[1769.26 --> 1775.92]  we would get a lot more people kind of feeling more entitled you know that we have to listen to
[1775.92 --> 1780.40]  their opinion i mean we listen to everything and just you know go into the irc channel but most of
[1780.40 --> 1787.20]  i think i haven't felt a whole lot of pressure um it's mostly been personal pressure of like because
[1787.20 --> 1792.02]  there is this very clear vision for what it is and it seems like everybody understands it so it's more
[1792.02 --> 1800.34]  about kind of meeting um for me my own uh my own expectations um yeah it's a it's a very positive
[1800.34 --> 1807.52]  thing to have a bunch of people that that get it um contribute uh money and so far there has been very
[1807.52 --> 1814.20]  little if any uh pressure from sponsors about specific features um or demands it's been really great we've
[1814.20 --> 1819.10]  been we've been very uh upfront about what we're building and people seem to get that and are on
[1819.10 --> 1823.36]  board with it um and now it's just a matter of delivering that which we're we're rapidly working
[1823.36 --> 1830.54]  towards i think we're a little lucky just in the the choice of the project because it's very much a
[1830.54 --> 1835.38]  problem that you know it's infrastructure right and everybody has to deal with these problems
[1835.38 --> 1844.52]  systems and we are you know using a lot of existing landmarks things like um heroku and existing systems
[1844.52 --> 1849.92]  like amazos or just schedulers in general and a lot of these kinds of best practices so i think
[1849.92 --> 1854.76]  building a system that's based on those means a lot of people already understand we're not
[1854.76 --> 1862.76]  really introducing completely new crazy stuff we're really just aggregating a lot of um existing best
[1862.76 --> 1869.14]  ideas into a single system and that makes it easier for people to to understand um as well as
[1869.14 --> 1875.90]  and and um and get behind what's the team look like now is it is it still just the two of you or or
[1875.90 --> 1881.72]  would you does that there's actually like three of us yeah um we also have daniel who also works on
[1881.72 --> 1886.48]  the tent protocol and he's doing kind of community management type stuff but um he doesn't work full-time
[1886.48 --> 1891.36]  on it gotcha so you have a fundraising goal for 2014 once you talk about that a little bit
[1891.36 --> 1900.52]  yeah so our goal for uh 2014 is 350 000 and that is entirely going towards development that will pay
[1900.52 --> 1907.04]  for myself and jeff and we're also looking to bring on uh at least one more person to work on the project
[1907.04 --> 1912.70]  full-time and we're uh looking for uh monthly contributions from companies that are interested
[1912.70 --> 1919.66]  in working with us to deploy flynn into production essentially um and so we've just kind of started
[1919.66 --> 1927.62]  on this goal and we expect to uh to hear more uh about it in january so you have your layer zero
[1927.62 --> 1931.64]  release coming up pretty soon layer one release is coming a few months after that and then the
[1931.64 --> 1937.20]  fundraising goal will go towards what layer two or you know what would be the next step well i we've
[1937.20 --> 1944.32]  taken a really kind of broad strokes um approach to this so you know just because we have the these
[1944.32 --> 1950.82]  releases out doesn't mean that they're you know really ready for for production use um and so it's
[1950.82 --> 1957.54]  really about filling in uh a lot of the gaps and building out some of the extra stuff because it
[1957.54 --> 1965.44]  there's there's uh there's just tons of nice to haves um and the system is so open-ended that it's sort
[1965.44 --> 1970.06]  of like at some point you can't really tell the difference between this system and your system
[1970.06 --> 1976.86]  right um because in a way you start building your system in this uh and so there's a lot of things
[1976.86 --> 1984.78]  that we can get into um that are kind of designed for you know the architecture of flynn things like
[1984.78 --> 1989.76]  uh i mean log aggregation is coming up pretty soon but things like metrics and stuff like that
[1989.76 --> 1996.04]  auto scaling some a lot of people are interested in like scaling up down on various public and private
[1996.04 --> 2002.32]  clouds um and so yeah we the funding we raised initially covered uh six months of development
[2002.32 --> 2010.60]  which will uh end at the end of january and culminate in our uh kind of initial like i guess beta release
[2010.60 --> 2016.72]  um and then uh what we're raising money for is to cover development in 2014 because we want to
[2016.72 --> 2023.00]  fix bugs and make new features and make cool new stuff that runs on flynn that just makes everyone's
[2023.00 --> 2029.12]  lives easier so after that what are you guys thinking about for as far as you know uh i don't
[2029.12 --> 2035.60]  know if sustainability is the right word but after the you know 2014 i guess my question is would it would
[2035.60 --> 2040.08]  you guys consider just continuing fundraising efforts or is there some plan to monetize flynn in the future
[2040.08 --> 2048.36]  currently no plans to monetize um things change rapidly uh i expect that late in 2014 flynn will be
[2048.36 --> 2055.40]  quite stable and um that there'll be a strong community around it developing add-ons etc um
[2055.40 --> 2064.04]  so i i don't foresee needing to to fundraise past 2014 but who knows it's interesting i mean it's a
[2064.04 --> 2068.94]  different definitely a different take on uh how to how to do open source well i mean sort of a
[2068.94 --> 2072.88]  different right it's fundraising and developing open source but it's a really neat way to you know how to
[2072.88 --> 2077.70]  how to do that so you've had you you have some competitors that um you know you mentioned cloud
[2077.70 --> 2082.48]  foundry and and things how many of these kind of got this started around the same time as you and and
[2082.48 --> 2088.48]  how would you you know talk about the experience of kind of entering a new space you know i i say new
[2088.48 --> 2093.54]  in quotes because this isn't new but it's a potentially new solution that's different way of
[2093.54 --> 2098.54]  thinking about it so what has it been like with your competitors or is there any any relationship there to
[2098.54 --> 2104.56]  to kind of speak of um so cloud foundry has been around for a while a few of the others have been
[2104.56 --> 2110.62]  around for a while uh there's at least uh one other one that kind of is started around the time that we
[2110.62 --> 2115.48]  did uh as far as publicly goes but they've been working on it for a while named dais and they actually
[2115.48 --> 2122.42]  share some components that jeff built for flynn um so it's everyone is kind of working towards what
[2122.42 --> 2128.36]  they their model of uh what they think you know life should be like deploying applications etc
[2128.36 --> 2135.46]  and so it's it's very healthy i think gotcha yeah we're gonna pause the show for just a minute
[2135.46 --> 2139.94]  and give a shout out to our awesome sponsor top towel they've been sponsoring the show for a little
[2139.94 --> 2143.58]  bit we've had a chance to tell you about some really awesome stuff they're doing i've been working with
[2143.58 --> 2149.24]  brendan their co-founder and cto and i mentioned that you know i wasn't quite sure what to expect from
[2149.24 --> 2154.20]  them and i was but i was excited about what they're doing they're helping developers who want to
[2154.20 --> 2159.02]  freelance with some really awesome companies find ways to do that and it's their mission these guys
[2159.02 --> 2163.60]  are the real deal they're engineers themselves from top to bottom they're not technical recruiters
[2163.60 --> 2167.68]  trying to pimp developers so if that's what you think then you've got you've got them completely
[2167.68 --> 2172.06]  pegged wrong they're a network of elite engineers all around the world who work with some really
[2172.06 --> 2177.04]  awesome clients and for those of you out there who are freelancing or or would like to freelance
[2177.04 --> 2181.22]  you've got to check out top tie you can work on special projects with companies like airbnb
[2181.22 --> 2187.00]  artsy audio and many others you can work remotely you can go to andrew's favorite place which is on
[2187.00 --> 2193.18]  a beach or anywhere in the world it's there there no office is required and to get started head to
[2193.18 --> 2198.16]  top tie.com slash developer click join the best and because they want to work with only the best
[2198.16 --> 2202.74]  senior engineers out there they've got a well thought out four-stage screening process that begins
[2202.74 --> 2207.86]  with a personal phone call via skype to kind of get to know who you are and introduce you to who
[2207.86 --> 2212.42]  they are and what their mission is and see if you're a fit and from end to end the screening process
[2212.42 --> 2217.96]  includes an english speaking test a timed algorithm test technical interviews with core top top
[2217.96 --> 2223.88]  engineers as well as a test project and once you've made it past the screening process the sky is the
[2223.88 --> 2228.36]  limit and if you think you have what it takes head to top.com slash developer right now to get started
[2228.36 --> 2231.92]  tell them the changelog sent you and enjoy now back to the show
[2231.92 --> 2242.56]  so this is a unique way this is the first show we've done where we want to bring bring the the uh
[2242.56 --> 2246.16]  previous guest back on the show to talk about progress you guys have been tremendously successful
[2246.16 --> 2251.02]  up to this point with this project and and we hope that it continues to go into the future um is there
[2251.02 --> 2256.52]  anything specifically that you guys want to talk about on the show and i want to kind of get give you
[2256.52 --> 2262.32]  guys a part up a moment before we wrap the thing up um anything you specifically wanted to hit on
[2262.32 --> 2264.20]  about flynn for the listeners to hear
[2264.20 --> 2273.58]  i don't think so i think we we covered um everything um i mean not everything but uh everything that we
[2273.58 --> 2278.94]  want to talk about here yeah so let me ask you one i think we might not have uh uh mentioned this
[2278.94 --> 2282.88]  actually how can let's say somebody's listening and they want to contribute as a company or you know
[2282.88 --> 2287.00]  whether it's recurring or not how can they contribute to flynn um so you just go to flynn.io
[2287.00 --> 2294.28]  um there is a sponsorship form which you can fill out um and drop your credit card number into and
[2294.28 --> 2301.00]  that'll set up a one-time or a recurring sponsorship you can also email us the email address is on the
[2301.00 --> 2305.40]  site and we're happy to work out alternative arrangements gotcha yeah actually if anybody's
[2305.40 --> 2310.12]  interested in using it as well it would be really great if you got in touch with us um
[2310.12 --> 2315.70]  because uh you know at a certain point we're gonna probably want to start working with some
[2315.70 --> 2321.18]  companies whether they're sponsors or not just in trying to get them set up uh with flynn and
[2321.18 --> 2326.30]  getting their feedback and stuff so we typically ask the same questions at the end of every show
[2326.30 --> 2331.28]  but being that we've already asked you guys we will have we will ask you kind of just one question
[2331.28 --> 2336.68]  now to see where it's changed and the question is what can the open source community do to contribute
[2336.68 --> 2341.80]  to flynn and and obviously start using flynn as a big point now but but in just in general what
[2341.80 --> 2345.06]  would be something you guys would like to see the open source community kind of pitch in with
[2345.06 --> 2357.48]  uh support i guess uh in not just financial but i mean really just um you know dig into what we've got
[2357.48 --> 2364.92]  and and and play with it and um uh you know talk to you know if it's something that you you think
[2364.92 --> 2372.52]  that you would uh love to see your whatever organization you're working at um have uh you know start
[2372.52 --> 2380.44]  you know maybe talking about it internally about you know this great possibility um and uh and we'll see
[2380.44 --> 2387.10]  what happens but i think it would be great to just have um you know even more uh love and support
[2387.10 --> 2394.26]  because it kind of makes uh our job easier in terms of fundraising and continuing to exist in that
[2394.26 --> 2401.68]  regard yeah and um in the meantime um absolutely play with our prototype components uh we have it all
[2401.68 --> 2408.42]  packaged up into a vm and hang out in the irc um feel free to you know raise issues on any of the repos
[2408.42 --> 2413.68]  send us email if you're you have any questions at all what's what's the irc channel that people can
[2413.68 --> 2420.42]  come to it's uh flynn on freenode and how will people email you is the you said the email address
[2420.42 --> 2427.84]  is on the website which is at flynn f-l-y-n-n.io that's correct awesome well i guess we have nothing
[2427.84 --> 2434.64]  else nothing left to talk about because flynn is something that is ever growing and uh it's still
[2434.64 --> 2439.62]  you know you launched or you launched your i don't you said probably the best way to say it is you're
[2439.62 --> 2445.82]  like super alpha version of the product um it's it's gonna be cool again you know and i said this
[2445.82 --> 2450.52]  last time but i mean it again this time it's you got a big couple of months ahead of you and i'm
[2450.52 --> 2454.32]  excited to see you know what the next few months bring and hopefully you guys don't you know burn
[2454.32 --> 2458.90]  out i think one of the things that i read on your blog was everybody has been working on flynn
[2458.90 --> 2463.54]  um everybody meaning the three of you have been working on flynn much more than you expected
[2463.54 --> 2469.04]  which is a good and a bad thing right and the good is that you've i mean it's crazy it's only been a
[2469.04 --> 2473.84]  few months and it's already to this point but the the fear is burnout so you know hopefully the next
[2473.84 --> 2478.20]  few months will be pivotal and you guys will uh these be very successful with it but but not get
[2478.20 --> 2483.66]  burnt out on it so you can continue to deliver great things with flynn thanks we hope so too yeah well
[2483.66 --> 2488.62]  once again i wanted to say thanks to jonathan and jeff for joining us on today's show i also wanted to give
[2488.62 --> 2492.98]  another shout out to our sponsors digital ocean and top towel for supporting the show you can head
[2492.98 --> 2498.08]  to digitalocean.com to set up your cloud server today and make sure you use our promo code changelog
[2498.08 --> 2503.58]  sent me that's changelog sent me to get a ten dollar hosting credit if you want to freelance with
[2503.58 --> 2510.06]  companies like airbnb artsy or ideo you can head to toptow.com slash developer and click join the best
[2510.06 --> 2514.42]  to see if you have what it takes to join top towels network of elite engineers again the url is
[2514.42 --> 2519.76]  toptow.com slash developer and that's it for this week thanks again to jonathan and jeff for joining
[2519.76 --> 2523.66]  us and also thanks to the listeners for tuning in and for your support if you haven't yet subscribe
[2523.66 --> 2528.16]  to the changelog weekly it's our weekly email where we share everything that hits our open source radar
[2528.16 --> 2533.82]  you can subscribe at the changelog.com slash weekly so for now guys let's say goodbye bye
[2533.82 --> 2538.80]  you
[2538.80 --> 2568.78]  We'll see you next time.
