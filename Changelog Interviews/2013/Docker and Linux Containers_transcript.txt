[0.00 --> 14.28]  welcome back everybody this is the change log we're a member supported blog and podcast that
[14.28 --> 19.12]  covers what's fresh and what's new and open source this show is hosted by myself adam
[19.12 --> 24.70]  stakovic and andrew thorpe andrew say hello hey how's it going man today's a good day man
[24.70 --> 31.80]  it's a very very good day very exciting day big day yeah big big day big day uh you can tune into
[31.80 --> 37.26]  this show live every tuesday that's right every tuesday at 5 p.m central standard time right here
[37.26 --> 43.50]  on five by five you can check out our past shows at five by five dot tv slash change log and this
[43.50 --> 50.44]  episode is number 89 not 0.8.9 can you believe that no it's hash 89 hash 89
[50.44 --> 57.60]  inside joke yeah and for those who've been listening to the change log forever and forever
[57.60 --> 64.30]  and forever and for those who went and listened or uh or read today's announcement um you know we
[64.30 --> 71.00]  don't we don't sem version our our uh cementally version our podcast so we dropped that moved the
[71.00 --> 79.10]  five by five and now this is just episode 89 so and today we're joined by solomon hikes a hacker of
[79.10 --> 87.34]  course and entrepreneur at dot cloud hey guys it's great to be here it is great so solomon where do
[87.34 --> 91.04]  we where do we begin to tell the story of dot cloud and what you're doing with uh with docker
[91.04 --> 97.90]  where do we begin yeah well we start with you maybe maybe get an intro to maybe start with you give
[97.90 --> 105.10]  an intro of who you are and kind of what you do at dot cloud sure uh so i'm the founder and uh dot
[105.10 --> 111.70]  cloud is my baby it's been my baby for the last five years so about five years ago i quit my job
[111.70 --> 120.88]  and uh set out to work on all things devops and uh deployment automation in cloud and that kind of
[120.88 --> 129.22]  stuff um and i guess i could give you the long version of that but um you know fast forward to 2010
[129.22 --> 136.70]  after two about two years of tinkering and and uh running a bootstrapped consulting business
[136.70 --> 144.24]  um toying with interesting technology and experimenting eventually um we we launched a
[144.24 --> 151.86]  product uh we launched a platform as a service so uh you know for the if you know uh products like
[151.86 --> 158.38]  heroku or google app engine or microsoft du jour uh we launched a platform that um
[158.38 --> 164.94]  lets developers upload their their web application very easily and the platform takes care of
[164.94 --> 171.40]  deploying it configuring the servers scaling it and and all that fun stuff freeing the developer
[171.40 --> 177.16]  uh that burden so that the developer can do what he does best which is write awesome code
[177.16 --> 184.76]  uh so we've launched that in 2010 and our claim to fame at the time was that we were the first
[184.76 --> 190.06]  platform as a service to support multiple languages so you know at the time heroku was really big in
[190.06 --> 196.72]  the ruby community uh google app engine was doing interesting stuff with with python but you had to
[196.72 --> 202.28]  you know heavily modify your app you had to use their custom apis etc um and there were a lot of
[202.28 --> 207.48]  developers out there who were eager to you know get their hands on something similar uh something that
[207.48 --> 212.92]  made their lives super easy uh with their respective languages and we we delivered that and there was a lot
[212.92 --> 221.20]  of buzz around that and uh you know fast forward to um late 2012 and early 2013 and we're you know we're
[221.20 --> 228.88]  doing that now we're growing the business growing the the you know the user base etc uh and all this time
[228.88 --> 238.60]  uh we're we're kind of we're getting more and more uh requests for some very specific we're getting a lot of
[238.60 --> 246.18]  people interested in the secret sauce the the not the platform itself but the the ingredients to build
[246.18 --> 253.50]  your own platform uh and you know sometimes because you know people wouldn't you know would not agree
[253.50 --> 258.64]  with the way we did pricing or usually they had custom needs you know you can't you can't be the
[258.64 --> 263.86]  provider for every applicant you know every developer out there every every company that needs to deploy an
[263.86 --> 272.54]  app that's a little bit ambitious um but um anyway you started getting requests for um the ingredients
[272.54 --> 280.72]  to building your own platform and uh eventually we we decided that that wasn't you know a smart move to
[280.72 --> 288.88]  make and we started open sourcing stuff and um one of the you know one of the components we open
[288.88 --> 295.12]  sourced is a is a is a project called docker which is basically you could call it our secret sauce
[295.12 --> 300.74]  but you know it's it's from a technology point of view you know you could argue it's not that big of a
[300.74 --> 308.36]  deal but there's a lot of uh work that goes into taking at you know a kind of arcane and complicated
[308.36 --> 314.44]  technology and delivering it in a simple way to developers so anyway the the that was kind of like
[314.44 --> 322.62]  the super fast forward version uh from super fast forward versions yeah uh you know the the we can
[322.62 --> 326.42]  go in like a thousand different directions here but you kind of glossed over you kind of glossed over
[326.42 --> 333.08]  the fact though that like for those who may not have caught up with dot cloud and and with what they're
[333.08 --> 337.60]  doing with docker i mean you gave a talk at pi call not long ago which is kind of when a lot of this buzz
[337.60 --> 342.70]  began to really hype up for you i wouldn't say it's the start of of your story but you know you had this
[342.70 --> 347.12]  talk called the future of linux containers and you wowed everybody like everybody was for with
[347.12 --> 351.70]  what you delivered and if kenneth was on this show right now he'd be saying the same thing as i'm sure
[351.70 --> 356.98]  that he was there at pi con so um you know tell tell us about that what is what do you mean by the
[356.98 --> 363.66]  future of linux containers so what i mean by the future of linux containers is well i guess i should
[363.66 --> 368.76]  start with by describing what linux containers are um there was this thing called virtualization
[368.76 --> 379.74]  and you know that the it lets you basically create a virtual computer and um that that had a lot of
[379.74 --> 385.08]  benefits for um companies that operated a lot of computers because you could consolidate hardware
[385.08 --> 392.72]  and you know instead of spending uh tens of thousands for uh dozens of servers all of a sudden
[392.72 --> 398.80]  you can spend much less for a smaller number of of actual computers and pretend you had more right
[398.80 --> 407.74]  um and on top of that the promise of virtual machines was that developers um could package their
[407.74 --> 413.34]  application along with all the dependencies uh everything from you know the libraries you use
[413.34 --> 420.12]  uh the app sure that that runs your app the exact version of the exact system library that your
[420.12 --> 425.02]  your application depends on all the way down to the to the distro in the underlying system
[425.02 --> 431.72]  the whole thing packaged in uh you know a single object something that you can hand to someone else
[431.72 --> 440.44]  and say here run this and it's reusable and that's kind of the key to um reliable testing um you know
[440.44 --> 445.90]  it's the key to component reuse between projects it's the key to making money with your software because
[445.90 --> 451.26]  all of a sudden other people can pay you to use it to reuse it uh there was a lot of excitement
[451.26 --> 457.36]  initially around what you could do with vms and that part of of using vms never really materialized
[457.36 --> 464.60]  because um vms aren't really that you know that's not really the point of vms from a technology point
[464.60 --> 471.82]  of view uh they have a few downsides they're they're big uh you know they take a lot of disk disk space
[471.82 --> 477.34]  uh running them uses up a lot of memory a lot of cpu there's a lot of overhead if you've ever
[477.34 --> 482.64]  you know simulated a complex system you know using vmware virtual box your laptop you know what i'm
[482.64 --> 490.00]  talking about the battery goes away really fast um they're not really portable anyway so um it never
[490.00 --> 496.40]  really took off as the the way developers share their work you know i don't i don't ever remember
[496.40 --> 500.82]  putting my code into a vm and like handing it to a lot of people and saying hey here's the official
[500.82 --> 507.88]  way to use my my my code right so we're still in this world of um fragmented ways to package
[507.88 --> 515.52]  and and share and reuse code uh and we're still in dependency hell and and these kinds of problems
[515.52 --> 522.14]  you know python developers have python packages ruby developers have ruby packages uh everyone has
[522.14 --> 527.52]  to deal with ubuntu packages or debit packages or red hat or etc uh and then you have to compile stuff
[527.52 --> 537.66]  by hand sometimes just a mess um and enter linux containers so what linux containers are uh they are um
[537.66 --> 545.66]  the linux kernels answer um to this problem or you know more specifically to the problem of um
[545.66 --> 557.34]  subdividing uh a single uh system system a single os into multiple uh areas that are
[557.34 --> 563.68]  completely sandboxed from each other so that you can run you know uh multiple applications side by
[563.68 --> 572.80]  side inside the same os right running on top of the same kernel um without application a messing with
[572.80 --> 579.48]  application b in any way and if you think you know if you think about uh iphone or android apps that's
[579.48 --> 584.86]  kind of how they work right you you your apps never interact with each other they don't touch each other's files
[584.86 --> 591.72]  uh you can remove you know you can add any combination of apps um they don't interact with each other they just
[591.72 --> 598.38]  don't mess with each other um and that's what linux containers enable and i would add that every modern
[598.38 --> 605.06]  operating system at least every modern unix operating system has a facility like linux containers you know
[605.06 --> 615.12]  the bsd systems have a similar mechanism called jails uh in fact uh you know bsd fans will tell you
[615.12 --> 623.84]  they've had jails for way longer than the linux head uh and linux containers um solaris has zones
[623.84 --> 630.94]  um and is this like taking all those different metaphors for different platforms and creating like
[630.94 --> 637.62]  one homogeneous like uh api to all that is that is that what the the point of doctor is that's what
[637.62 --> 645.04]  the point of doctor is um like so i guess like my where i was getting was um there is now the
[645.04 --> 653.50]  possibility of creating such an api basically a unified format for packaging your entire app um
[653.50 --> 660.84]  with all its dependencies regardless of what language you used what libraries or framework you use
[660.84 --> 669.56]  as long as it runs on linux basically the only dependency is the linux kernel uh as long as as
[669.56 --> 674.28]  you can run in the linux kernel basically you there is the possibility now of packaging your app in this
[674.28 --> 683.26]  unified standard format and then be able to run it with strong guarantees that uh wherever you run it
[683.26 --> 688.28]  it will run in the same way and that's very powerful because now again you can hand it to someone else and
[688.28 --> 693.06]  say here run it and then that this other person will run it and something predictable will happen
[693.06 --> 699.18]  right and that's that's the key to automation that's the key again to reliable testing to things like
[699.18 --> 705.06]  hey here's an upgrade now i can send you this upgrade and and it works right uh and and so again
[705.06 --> 711.86]  linux containers makes that possible because now the linux the linux kernel effectively can be split up in
[711.86 --> 719.78]  little uh sandboxed areas uh but it's the raw material and what was missing was a tool to kind of glue
[719.78 --> 725.34]  all these raw capabilities together and deliver it to developers in a package that that that is usable
[725.34 --> 731.68]  that makes sense right so dot cloud originally was taking advantage of linux containers to kind of do this
[731.68 --> 736.56]  for everyone yeah and you decided with all the requests that are coming out to to go ahead and build
[736.56 --> 741.78]  you know did you extract docker from dot cloud or did you kind of build a new so it was actually
[741.78 --> 748.12]  extracted from dot cloud so uh a combination of both sorry go ahead i'll answer after well i'll have
[748.12 --> 752.30]  i'll have more for you but go ahead and kind of explain that like how did docker separate itself from
[752.30 --> 758.40]  dot cloud so yeah so first of all to i guess to answer your preliminary question yes that's definitely
[758.40 --> 763.90]  what we've been doing at dot cloud essentially forever i mean all the way back to 2008 when when dot cloud
[763.90 --> 772.38]  was started way before we even launched our first mass you know mass um consumption product um our thing
[772.38 --> 778.68]  was always taking advantage of linux containers for fun and profit that's basically what dot cloud is
[778.68 --> 787.64]  and uh back in 2008 it was just a really really weird thing to do uh in fact that the the at the time
[787.64 --> 795.72]  the lxc project which is today the the the flagship product uh project sorry within the linux kernel
[795.72 --> 802.80]  um for all things containers that project didn't exist or maybe barely existed i forget it was in any
[802.80 --> 809.72]  case highly experimental and definitely not usable uh what what what the linux community had at the time
[809.72 --> 817.36]  was uh various patches so there was one patch called v server which you know was was supposed to
[817.36 --> 822.38]  emulate bsd jails another one called open vz which was maintained by a company called parallels which
[822.38 --> 829.32]  you may have heard of yep um and so back in the day it was highly uh experimental territory to to use
[829.32 --> 834.80]  containers anyway but we did and we had a lot of fun and eventually we became good at it and you know
[834.80 --> 840.16]  figured out ways to plug the components together and then we launched dot cloud on top of it so yes
[840.16 --> 845.78]  definitely dot cloud was our way of taking advantage of these capabilities make you know turning them into
[845.78 --> 851.12]  our kind of secret ingredient and using that for our advantage which was basically come out with a
[851.12 --> 855.90]  heroku competitor that could do 10 times what heroku could do right because hey it was completely
[855.90 --> 860.52]  agnostic to any language of course because it was containers under the hood and then we started doing
[860.52 --> 865.86]  things like launching database services right uh you know dot cloud today has 15 different cloud
[865.86 --> 871.22]  services we have a redis service of a mongodb service of a mysql service and all of those services
[871.22 --> 879.44]  as diverse as diverse as they are are actually under the hood um powered and operated by a single
[879.44 --> 888.52]  layer built on on on linux containers so it's actually the same code um that automates the deployment of
[888.52 --> 895.98]  your mysql database or your rails or python app when you're using dot cloud and and and behind that
[895.98 --> 902.36]  there's an ops team that is ridiculously small you know it's like uh you know five guys basically power
[902.36 --> 909.08]  these 15 cloud services um and this is all thanks to you know what we're able to extract out of this
[909.08 --> 914.16]  awesome technology that has links containers i'm you know i'm simplifying it just a bit because there are
[914.16 --> 919.68]  other components that gravitate around it but really that's really kind of the the starting point that you have
[919.68 --> 926.56]  this this unit of deployment this thing that once you've bundled it you know what's in it and you can
[926.56 --> 931.34]  run it in a repeatable way that's the key to everything right so fast forward four years and
[931.34 --> 937.06]  now based on a lot of you know consumer feedback or people not liking the the pricing or you know
[937.06 --> 941.72]  different reasons you said you guys decided to pull docker out of it and yeah so why was that decision
[941.72 --> 948.76]  finally made our our our reasoning was basically well there's a there was a combination of factors the
[948.76 --> 959.28]  first was clearly the market has evolved people are you know um are are the market in general is
[959.28 --> 964.48]  getting more sophisticated uh it's not like we're the only people in the world who know about linux
[964.48 --> 970.24]  containers understand a lot of very yeah there are very lots lots of very smart systems engineers who are
[970.24 --> 977.78]  taking advantage of them and we started seeing popping up popping up on the radar starting in in 2012
[977.78 --> 986.56]  um a bunch of kind of a new generation of cloud services that started kind of catching on and and
[986.56 --> 992.44]  doing things that clearly um made it you know that made it very obvious that under the hood they were
[992.44 --> 996.98]  playing with containers as well and we thought okay this was our differentiating advantage uh but you
[996.98 --> 1003.16]  know no differentiating advantage lasts forever right um and you know realistically we're a startup we're not a
[1003.16 --> 1008.14]  giant company with with deep pockets we can't possibly compete with everyone on every front right
[1008.14 --> 1015.40]  um and so let's let's let's specialize right let's let's adapt to this new world where a lot of players
[1015.40 --> 1022.30]  know about containers what do we know best right should we specialize on the um on the sql database uh
[1022.30 --> 1026.60]  should we be you know a mongo db provider and go after the mongo db players should be specialized in
[1026.60 --> 1033.64]  rails and python and javascript and you know we realize in the end our true core our true specialty
[1033.64 --> 1040.56]  is the underlying containers layer it's the it's the it's the it's the underlying it's the underlying
[1040.56 --> 1048.84]  layer itself it's doing incredible things with containers uh and how do we um take advantage of that
[1048.84 --> 1054.68]  that uh experience the fact that we're we've been using and taking advantage of containers
[1054.68 --> 1063.76]  for many years we have more production and you know real world experience with them than most
[1063.76 --> 1070.30]  companies in the world um as a business how do we take advantage of that um and the answer is um
[1070.30 --> 1075.06]  open source it to get the credit for the the work we've done right so that's the business answer
[1075.06 --> 1084.56]  right and then um i would say the the the engineer's answer uh is that hey that stuff's going to be
[1084.56 --> 1090.08]  open anyway like it's just too awesome not to become an open standard something that everybody
[1090.08 --> 1095.24]  uses and benefits from that's just the awesome world we live in through things like open source
[1095.24 --> 1103.70]  in the end people will get um a really easy to use incredibly powerful uh open source implementation
[1103.70 --> 1108.34]  of that stuff eventually it will become a standard there will be foundations around it it'll be awesome
[1108.34 --> 1114.68]  for everyone uh so that's if you believe that's going to happen no matter what um do you want to
[1114.68 --> 1119.00]  be part of and and and if you can contribute to that like you've got something to bring to the table
[1119.00 --> 1125.66]  because you happen to know that stuff um then do you want to be part of that awesome movement that is
[1125.66 --> 1129.98]  about to start or do you want to say stay on the silent and say no i've got this closed implementation
[1129.98 --> 1136.12]  mine's better but you'll never know exactly how much better show you the code you know maybe you can do
[1136.12 --> 1140.92]  that if you're a big company and even if you're a big company i think it's stupid but uh for startup
[1140.92 --> 1145.40]  it's it's you just well i mean this shows on open source i mean it makes sense right that's that's uh
[1145.40 --> 1152.70]  it's open source all the things man i i you know right and and then the burdens on us um to prove that
[1152.70 --> 1158.66]  we can bring value as a business and uh i think that's a great that's a great approach to business
[1158.66 --> 1164.40]  it's it's win-win all the way and i think we you know as a business i'm not worried at all we've we've
[1164.40 --> 1170.18]  first of all we know how to run them in production which is very hard uh i mean you know it's the i'm
[1170.18 --> 1175.86]  not going to preach to you uh that open source is good for business but anyway um that that i have
[1175.86 --> 1179.32]  a question though can i can i ask a question on this because this is where this is where i'm trying to
[1179.32 --> 1186.04]  find the line and uh for those listening you definitely know i'm not a devops guy so i come to
[1186.04 --> 1191.00]  this table and talk to solomon and andrew about this with asking for grace because i don't know
[1191.00 --> 1197.14]  uh all the details here but um when we look at linux containers so lxc containers out there and
[1197.14 --> 1201.46]  then we look at docker what is docker to lxc containers what that's where i'm trying to
[1201.46 --> 1207.30]  paint the picture from yeah good question and a question i get a lot so you're not alone um so i
[1207.30 --> 1213.48]  think there was there is there was an early answer and then there's a now there there's a kind of a
[1213.48 --> 1222.40]  larger answer um the early answer is lxc is the raw stuff and and docker is what makes it palatable
[1222.40 --> 1232.88]  what makes it usable um someone someone uh there's a cool blog post um describing docker and and the
[1232.88 --> 1239.18]  guy who wrote the blog post uh compares it to git like using lxc is kind of like using those underlying
[1239.18 --> 1244.14]  obscure commands that actually power git but no one understands how they work unless you know
[1244.14 --> 1249.14]  unless you've read like 10 pages of documentation and you know you got people telling you like oh
[1249.14 --> 1254.22]  you can build like you can build a file system and you know you could rebuild dropbox until on top of
[1254.22 --> 1258.50]  that stuff you know and then there are people who just want to check in source code and see diffs
[1258.50 --> 1263.72]  and merge you know and and uh for that stuff to be possible you need a new set of commands that
[1263.72 --> 1270.74]  actually you know um offer that level of of interface so it's it's it's a it's an api that
[1270.74 --> 1276.36]  makes sense it's a higher level api it's a higher level ui so that's one way to look at it you've you've
[1276.36 --> 1280.96]  you've i've heard uh people describe it as and this probably is good for you too adam like
[1280.96 --> 1287.16]  docker has the potential to be for you know a platform as a service as chef did for infrastructure
[1287.16 --> 1292.44]  as a service so it's just like a high level api to make it easier less barrier of entry to get in
[1292.44 --> 1299.80]  there and be able to do what lxc allows you to do gotcha i uh yeah i that's definitely true i i you
[1299.80 --> 1306.00]  know uh it makes it accessible i think we're whatever platform as a service exactly means let
[1306.00 --> 1312.00]  let's let's say it's whatever offers an api uh you know hosted api for developers to do something
[1312.00 --> 1317.74]  something like that uh whether it's storing data in a database or deploying your code um
[1317.74 --> 1325.16]  i think we're we're at the end of an era where it was there was a very high barrier to entry to
[1325.16 --> 1332.62]  actually building a pass you know whether you were going to build a database service or build some
[1332.62 --> 1341.82]  sort of api powered service like twilio uh or you know stripe or mailgun or whether you were going to
[1341.82 --> 1348.18]  deploy web apps like you know dot cloud or heroku uh etc there was a that was a very high bar you
[1348.18 --> 1355.76]  had you know that that's like very very very specific expertise uh you have to be kind of that
[1355.76 --> 1362.70]  perfect combo of low-level systems engineering ops you know uh and at the same time you know
[1362.70 --> 1369.12]  understanding the needs of a specific um group of developers uh and that's kind of a hard combo
[1369.12 --> 1373.76]  and i think now we're entering a phase where that all that stuff is being democratized
[1373.76 --> 1384.60]  um thanks to things like docker it's actually easier to build a pass that um answers a very
[1384.60 --> 1390.38]  specialized need in the developer community uh without having to reinvent the wheel and become
[1390.38 --> 1397.32]  you know a world-renowned expert in uh you know load balancing between multiple
[1397.32 --> 1406.00]  ec2 regions and you know 24 7 monitoring and uh you know change management and log collection
[1406.00 --> 1413.72]  and metrics collection and all that stuff right so yeah i want to interject so you said that kind
[1413.72 --> 1418.58]  of your claim to fame early on at dot cloud was you know because you were leveraging the linux containers
[1418.58 --> 1424.20]  you were able to basically be you know framework independent language independent like none of that
[1424.20 --> 1428.54]  mattered right so i remember early on there was i don't maybe not early on but i remember you know
[1428.54 --> 1433.06]  the heroku and engine yard for ruby and then node jitsu came out for node.js and it was all these
[1433.06 --> 1440.08]  specialized services came out for these you know one uh framework or one language you know one
[1440.08 --> 1445.42]  environment and then so you came out so now you know fast forward a few years and most of those guys
[1445.42 --> 1453.22]  are supporting multiple um environments so does that mean that would you consider y'all yourself kind of a
[1453.22 --> 1457.22]  trendsetter in a way where now a lot of those guys are probably doing the same thing right using
[1457.22 --> 1465.08]  leveraging linux containers to do this yep i i that that's definitely true i think the you know
[1465.08 --> 1470.32]  pass is a really young market no no one really knows how it works or how to make huge money with
[1470.32 --> 1475.24]  it because no one has like no one's won in pass there's no giant success story in pass yet
[1475.24 --> 1481.46]  everyone's figuring it out so that including us so that's that's a you know a warning before i say
[1481.46 --> 1489.34]  anything that gets me in trouble um but yeah i think that you know there was a trend where uh you
[1489.34 --> 1494.24]  started from the needs of a group of developers that you knew really well so you focused you you
[1494.24 --> 1499.72]  attacked the vertical and that's kind of you know startup 101 so you're heroku you're you know you're
[1499.72 --> 1504.90]  part of the ruby community i mean these guys were you know a rails development shop and they they knew
[1504.90 --> 1508.98]  the needs of the rails community better than anyone and they built a product for the rails community and it
[1508.98 --> 1515.08]  worked right and no jitsu did the same thing for the no j's community etc etc and and you know um as
[1515.08 --> 1521.34]  as that evolved um people started realizing hey actually all these people all these developers who are
[1521.34 --> 1528.28]  part of different communities actually if all have jobs or eventually will get jobs in companies that
[1528.28 --> 1535.34]  are not actually uh organized as highly verticalized tribes like there are very few companies that define
[1535.34 --> 1543.06]  themselves as no j's companies or ruby companies right um including maybe a few fringe you know
[1543.06 --> 1548.48]  startups that are not actually not actually the the reality of the rest of the world right most companies
[1548.48 --> 1555.62]  have you know a real complicated horrible mix of lots of different stuff running on lots of different
[1555.62 --> 1562.18]  technologies um with really really overworked people trying to kind of plug it all together right and
[1562.18 --> 1568.36]  and every time that these guys hear about a new language you're like oh shit you know so on the
[1568.36 --> 1573.22]  one hand you got developers you said you got like five people running your uh your devops team right i
[1573.22 --> 1578.24]  mean yeah but we so what i'm talking about is the companies that that we run applications for
[1578.24 --> 1585.02]  oh these guys have developers writing apps in all sorts of crazy languages and using crazy databases and
[1585.02 --> 1591.34]  they've got you know the old the they've got the you know the the they've got the the cold fusion stuff
[1591.34 --> 1596.06]  uh running on a server under a desk somewhere then they got the java enterprise apps then they got the
[1596.06 --> 1601.78]  ruby and rails uh you know apps now they got the the mobile apps with the no j's back in and god knows what
[1601.78 --> 1606.44]  else and they're trying to like make sense of all that and so these guys are very interested in a
[1606.44 --> 1612.30]  platform that is agnostic that that can run whatever they actually you know happen to need to run
[1612.30 --> 1618.86]  uh and and give them a freaking unified view of what of what's going on you know they want the
[1618.86 --> 1625.30]  logs for the node.js app and the ruby app and the mongo db database all in one freaking place so they
[1625.30 --> 1629.16]  can you know know what's going on and and and they'll pay good money for that and that's basically
[1629.16 --> 1633.68]  that was our premise as a business for going so it's bringing all these different components of
[1633.68 --> 1639.10]  somebody's app or infrastructure under one roof yeah so i mean that's the holy grail right you want to be
[1639.10 --> 1646.30]  the place that runs all the stuff you want to be the provider of the unified provider uh and and so
[1646.30 --> 1652.60]  the i think that's kind of phase two of past where people realized um you can get you can get a lot
[1652.60 --> 1657.92]  of developers to start playing with you by being very specialized and simple for a specific use case
[1657.92 --> 1663.10]  a specific you know language or framework or whatever but then eventually if you want to keep that guy
[1663.10 --> 1672.24]  or at least you know keep keep his business as his app grows um as his business grows etc uh or has you
[1672.24 --> 1677.36]  know as as he brings his colleagues in and tries to convince his boss to to use you you're going to
[1677.36 --> 1681.56]  need to be more flexible more customizable you're going to need to support more things so you're going to
[1681.56 --> 1689.86]  need um basically linux containers uh and and so i think now people are realizing that i mean by people i mean
[1689.86 --> 1699.14]  the past providers and and now you're seeing more multi-language um yeah so you've and maybe this
[1699.14 --> 1704.22]  is an obvious question but or maybe not i don't know maybe i'm not seeing it but by open sourcing
[1704.22 --> 1710.48]  docker uh i mean that must have taken a lot of thought because you're in a way enabling your
[1710.48 --> 1716.22]  competitors to do things that you're doing privately so so how how did that decision come about
[1716.22 --> 1720.46]  so you know this saying like it's it's probably i don't even know i think no one knows who actually
[1720.46 --> 1724.98]  said it but the whole thing about uh when there's a goal you know a gold rush you want to be selling
[1724.98 --> 1732.66]  the the shovels yeah the whole point of paths was that while you know while the the web the web
[1732.66 --> 1738.70]  startup gold miners are mining you you the past provider want to be selling them the shovels right
[1738.70 --> 1747.04]  and then now all of a sudden the the the shovel shops are realizing hey we need to expand our
[1747.04 --> 1753.78]  technology uh really really fast so that we can support cross language and we can kind of expand our
[1753.78 --> 1758.50]  our offering and in these in these organizations we can sell more stuff to these companies we need to
[1758.50 --> 1763.84]  sell more shovels fast and and actually by the way it's getting real easy to make shovels because
[1763.84 --> 1769.34]  there's more there's a lot of money in shovels so uh what do we do how do we differentiate oh that guy
[1769.34 --> 1775.92]  over there is making you know i don't know shovel making machines and so that's us right we're like
[1775.92 --> 1780.90]  we're we're the best at making shovels um here we'll help you make your own shovels because we're
[1780.90 --> 1785.54]  transitioning to the business of selling the machines while you make the shovels so you're you're
[1785.54 --> 1793.00]  becoming platformer as a service as a service i i hope that doesn't become a word but you know in a way
[1793.00 --> 1799.82]  you know we just that was the key that's the key bet it is the key bet uh is that this is a transition
[1799.82 --> 1806.30]  and you know the this is a real economy now it's a real market selling stuff to developers
[1806.30 --> 1814.54]  uh is becoming a real economy you know it's a new market uh and and when there's a market there is
[1814.54 --> 1820.72]  there is now a space for specialized vendors that address that market so i think increasingly you're
[1820.72 --> 1825.92]  going to see that people that used to be our competitors are are now more natural partners
[1825.92 --> 1833.80]  uh or natural you know customers right so the the popularity of docker just took off i mean like it
[1833.80 --> 1839.38]  was kind of mind-boggling to see it just explode and i don't know if the your lightning talk at pycon
[1839.38 --> 1844.62]  was kind of the you know the impetus that but it was just crazy to see this just blow up and then
[1844.62 --> 1852.42]  but i i guess what you really benefited from was you know i saw docker from dot cloud was blowing up
[1852.42 --> 1858.98]  so did you see like the did you see actual boost in dot clouds you know like that was my next question
[1858.98 --> 1864.36]  is like how does this impact business yeah was dot cloud business booming from this too yeah so it
[1864.36 --> 1870.44]  definitely benefits directly i mean it's it's um was it like a hockey stick or was it like a 90 degree
[1870.44 --> 1876.98]  turn i guess 90 degree is it's like super up versus yeah 90 degree is a pretty nice hockey stick
[1876.98 --> 1884.00]  already it's not it's it's so it's kind of a two-step process like step one is obviously it's it's it's
[1884.00 --> 1889.80]  exposure for dot cloud as a company and as a result we're selling more of our stuff and that's great and
[1889.80 --> 1897.74]  and and in fact i don't know if you guys caught this but as part of this crazy um buzz which we didn't
[1897.74 --> 1902.84]  really see coming and actually it started before we were ready if you remember the the it was the
[1902.84 --> 1908.08]  whole thing was leaked uh and we had to rush to actually ship the source code ahead of schedule
[1908.08 --> 1914.82]  because it wasn't ready and fired the developer that leaked it oh boy i don't know i i mean we and and
[1914.82 --> 1919.60]  here's a funny story i mean the the on the one hand i'm saying oh it was leaked and the other hand
[1919.60 --> 1927.60]  here i was giving a talk at pycon but the thing you have to understand is um we were
[1927.60 --> 1933.36]  kind of cautiously one step at a time showing docker to a select group of people that we knew
[1933.36 --> 1941.10]  or would be interested you know and so by the time we we gave that talk at pycon uh about 40 companies
[1941.10 --> 1947.48]  had seen docker played with docker were actively you know checking the repository looking at the
[1947.48 --> 1953.98]  progress so we kind of had this kind of miniature like closed closed but open source at the same time
[1953.98 --> 1961.04]  if that makes sense and you know we were at you know maybe i won't name names but a lot of companies
[1961.04 --> 1966.70]  played with it and are still playing with it um and you know along the way we thought hey there's there's
[1966.70 --> 1972.84]  pycon and we know we know a lot of the guys there surely there are people that are interested in in
[1972.84 --> 1978.12]  oldix containers let's just you know get together with a few of them let's just give this obscure
[1978.12 --> 1983.74]  talk that no one will be interested in except the the uber container geeks uh plus it's a it's a
[1983.74 --> 1990.08]  it's a lightning talk it'll be in a back room there'll be like 15 people 12 of which will
[1990.08 --> 1995.16]  actually not care and you know we'll have we'll meet two really you know interested people and then
[1995.16 --> 2001.60]  we'll add them to the private beta that was kind of the idea and and in fact you know with the you
[2001.60 --> 2007.94]  got a standing ovation from everybody well no the thing is lightning talks at pycon happen to be a
[2007.94 --> 2012.38]  really big deal and there it's like it's in the main room with 800 people in it or something
[2012.38 --> 2017.68]  and i had nothing i didn't have slides i mean you've seen the video right it was like hello world
[2017.68 --> 2023.24]  it was the least prepared talk i know i loved watching you in the video when you were like
[2023.24 --> 2026.86]  typing the commands and you would have to like delete to because you forgot part of the command
[2026.86 --> 2031.56]  and it was just like real so stressed out i was i was like oh 800 people are watching me
[2031.56 --> 2038.26]  type hello world great but you know it it you know they liked it so that was great um but so
[2038.26 --> 2042.80]  the result is of course you know someone in there said hey i'm gonna put this on hacker news and then
[2042.80 --> 2048.04]  you know there was buzz um but there was a point all this i kind of forgot where i was going
[2048.04 --> 2053.24]  uh oh that's okay about the impact back to your business i was kind of surprised i only gave you
[2053.24 --> 2058.98]  five minutes though yeah i wasn't done they're like they're like uh you're everyone is like
[2058.98 --> 2062.48]  at the edge of their seat as you're wrapping up your talk and they're kicking you off the stage
[2062.48 --> 2066.32]  because they literally gave you like four and a half maybe maybe four minutes and 15 seconds that
[2066.32 --> 2070.44]  they're being generous and then they're booting you off the stage not because you weren't talking
[2070.44 --> 2076.02]  about something cool but they were just so adamant about their their timeline they're running a tight
[2076.02 --> 2081.38]  ship i mean those guys are are well organized yeah anyway it was it was you know there was a lot of
[2081.38 --> 2087.14]  cool conversation afterwards or you know it was python is really nice it's a really cool you know chill
[2087.14 --> 2092.68]  uh conference it was a it was a nice place i'm glad i'm glad it happened there and not you know
[2092.68 --> 2097.10]  in a trade you know like a more formal trade show or something that would have been boring
[2097.10 --> 2105.06]  yeah so one thing that's really interesting about uh docker and i guess dot cloud in general is that
[2105.06 --> 2109.62]  you're using go uh for some reason that that's just very interesting to me so where where did the
[2109.62 --> 2115.18]  thought from why did you guys pick go instead of something else so and it actually gets even more
[2115.18 --> 2121.18]  interesting when you know that 90 of the code we've written at at dot cloud since the very
[2121.18 --> 2127.50]  beginning it has been python we're a store python shop we've but at the same time you know we've
[2127.50 --> 2134.40]  written code in various languages i mean we do advocate you know polyglot deployment or whatever you
[2134.40 --> 2139.80]  know the the possibility of using multiple languages so we we have to at least use more than one
[2139.80 --> 2146.18]  you know to be credible so we have a few pieces in node.js um and we started dabbling in go but
[2146.18 --> 2150.46]  nothing crazy but you know we liked it because we're we're systems guys so we've written a lot of c
[2150.46 --> 2157.54]  and you know it's kind of it's like c but nicer uh and so what really decided it is you know the the
[2157.54 --> 2163.88]  very very first versions of docker were written python because they were basically a rewrite a
[2163.88 --> 2172.14]  gradual you know standard pragmatic refactoring of the dot cloud the core dot cloud platform which
[2172.14 --> 2179.52]  you know has been at this point in in production for over two years so you know that's what happens
[2179.52 --> 2186.20]  to production systems used by real customers over many years they you know they tend to things tend
[2186.20 --> 2191.22]  to pile up and at some point you need to kind of just clean things up and refactor and you know take
[2191.22 --> 2196.20]  advantage of the lessons learned yada yada yada and so we you know we started this project and at some
[2196.20 --> 2202.56]  point we kind of had this discussion internally about um hey this this this refactoring is actually
[2202.56 --> 2207.62]  going to be limited in scope because you know we got to drop it in and it has to be completely
[2207.62 --> 2211.98]  reverse compatible we can't just you know break people's applications i mean you know there's a whole
[2211.98 --> 2219.14]  process to running people's apps in production and so we were faced with this decision do we continue
[2219.14 --> 2226.08]  with a kind of a conservative gradual rewrite i mean refactor uh or do we do we do something more
[2226.08 --> 2231.60]  radical and and kind of widen the loop if that makes sense kind of go off and make it a separate
[2231.60 --> 2237.80]  component uh and and say hey you know what it's okay if it doesn't benefit the platform right away
[2237.80 --> 2244.76]  um but then we'll have kind of free reign to to really take advantage of all the lessons learned do
[2244.76 --> 2251.66]  something clean something nice you know something less frustrating um because one of the problems when
[2251.66 --> 2257.46]  you when you cover so many languages and technologies is you know you say yes to too many feature requests
[2257.46 --> 2265.26]  and then you have to support those features forever yeah so we wanted to kind of um the result is you get a
[2265.26 --> 2271.08]  lot of baggage so anyway the um we were really tempted by the second option right clean rewrite but
[2271.08 --> 2277.84]  then how do you how do you avoid the the death trap of you know the the rewrite that never ends
[2277.84 --> 2282.54]  you know and two years later you've never shipped you haven't shipped anything all the customers are gone
[2282.54 --> 2288.58]  because nothing's moving you know just all right that kind of stuff so the the answer was let's let's
[2288.58 --> 2293.46]  make it an open source component let's make it really really small and concise so that can be used
[2293.46 --> 2300.12]  on its own like the first iteration can be used on its own by other people and then let's later
[2300.12 --> 2308.16]  circle back and and plug it back into dot cloud so have you gotten to that point so in some places not
[2308.16 --> 2314.98]  not not on the core production platform no i mean they are very very direct relatives obviously uh i mean
[2314.98 --> 2321.74]  it is still a rewrite of the dot cloud platform so in a way it's kind of v2 of the of the the the the
[2321.74 --> 2330.02]  core of dot cloud right uh and and new stuff is now 100 built on on docker um you know existing
[2330.02 --> 2336.00]  stuff will be you know is being transitions uh you know in a in a on a following a pace that makes
[2336.00 --> 2342.40]  sense i mean a lot of our customers you know they they're they're you know they're glad that we
[2342.40 --> 2346.54]  were getting buzz and they're happy for us but you know they just want their app to run right now so
[2346.54 --> 2353.66]  right um anyway so the back to the question about go uh so we made that decision of making it a rewrite
[2353.66 --> 2362.78]  and and open sourcing it etc and one thing we wanted to avoid was um cutting corners you know if it was
[2362.78 --> 2368.16]  going to be a clean rewrite it had to be a real clean rewrite with no cheating and it's really tempting
[2368.16 --> 2374.36]  to cheat you know you're like oh uh we've solved this problem a year ago it was really a pain in the
[2374.36 --> 2379.24]  s to solve the first time do we really need to write it a second time i'll just copy paste that
[2379.24 --> 2385.76]  over there you know and so you know i wanted to avoid that um and there were two other reasons
[2385.76 --> 2393.68]  for using go the second reason was that it's it's it has this really nice property of compiling to a
[2393.68 --> 2401.36]  static binary which you just drop somewhere and it runs and that is just awesome uh and it you know
[2401.36 --> 2405.62]  it's awesome because it's just really practical from an ops point of view when you got a lot of
[2405.62 --> 2411.06]  servers to run you know you have other shit to do uh you don't want to deal with like dragging all
[2411.06 --> 2415.66]  sorts of dependencies and following like a 50 page tutorial and setting it up you just want you know
[2415.66 --> 2421.66]  drop the binary run it good let's you know moving on and uh it has the added benefit of being really
[2421.66 --> 2429.20]  easy to use by you know regardless of what your language of choice is and you know the devops community
[2429.20 --> 2432.86]  the community of people who you know automate the deployment of servers and deal with
[2432.86 --> 2438.00]  that kind of stuff the kind of people who are naturally attracted to to docker who are the
[2438.00 --> 2445.30]  target of docker um are are fragmented bunch of people there are people who do everything in ruby
[2445.30 --> 2451.40]  obviously there is chef you know puppet uh there's a lot of tools around that um there's a big python
[2451.40 --> 2456.70]  community and then there's a big java community and those are kind of the three main groups and then
[2456.70 --> 2462.16]  there's closure there's cool stuff in closure there's all sorts of cool stuff uh none of these
[2462.16 --> 2468.08]  guys as a general rule will use a tool if it's written and you know if it if it's written in the
[2468.08 --> 2473.06]  opposite language uh and not really because they don't like the language but because uh it comes
[2473.06 --> 2480.16]  with strings attached like if if you're a ruby shop and you're you're evaluating a python tool uh it
[2480.16 --> 2484.32]  can be a real pain in the ass to actually run that python tool because now you got to deal with
[2484.32 --> 2488.64]  python packages and dependencies and virtual end and all these things that you're not familiar with
[2488.64 --> 2492.92]  and if you know if they break how do you go ahead and hack with them and so go is a nice kind of
[2492.92 --> 2497.80]  middle ground it's a binary you drop it everyone can use it and if you want to hack on it it looks a lot
[2497.80 --> 2503.36]  like c so it's kind of neutral and the third the third reason is really just you know it's trendy
[2503.36 --> 2509.30]  and it was you want you want your project to be adopted so if you can give people one more excuse
[2509.30 --> 2515.28]  to play with it then hey you know why not and it's just a really cool language so the the biggest
[2515.28 --> 2519.18]  communities on dot cloud would you say are would you say they're ruby python and java
[2519.18 --> 2528.10]  yeah i mean that would be my guess i mean i didn't really run a uh although maybe i should but yeah
[2528.10 --> 2533.28]  that would be my guess just from experience yeah it's really cool then to see i mean if you look at
[2533.28 --> 2538.26]  the github repository you got you know almost 2 000 stars and almost 200 forks and it's cool to see
[2538.26 --> 2544.74]  that you know a lot of a lot of people maybe don't know more than just the language that they work in
[2544.74 --> 2550.26]  but obviously docker is a cool enough project where i mean people are probably even willing to learn go
[2550.26 --> 2555.22]  and it's a good opportunity to learn go if they don't know it so yeah it's cool to see this growing
[2555.22 --> 2562.42]  up so you have plans then to uh bring docker back into dot cloud and do you have any kind of time
[2562.42 --> 2569.44]  frame and where you would see that happening um well i mean the the what is already happening is
[2569.44 --> 2577.16]  that 100 of everything we're doing as a company is built on docker going forward it's 100 we've just
[2577.16 --> 2583.84]  made as soon i mean it started as an experiment we hope that people would like it then we realize oh
[2583.84 --> 2590.72]  shit people like it and then we realize wow this is not stopping um you know not only are people using
[2590.72 --> 2595.58]  it but people are actually actively contributing to it there's a real community that basically
[2595.58 --> 2601.18]  you know you mentioned the forks the forks to me are even more interesting than the stars because it
[2601.18 --> 2605.54]  means people are actually playing with it and contributing back i think we've got you know
[2605.54 --> 2610.50]  over 20 people now who are authors in the broad sense of the term maybe they only you know they
[2610.50 --> 2615.84]  contributed to fix the readme but there are i mean there are really impressive people in the docker
[2615.84 --> 2621.24]  community i'm like i i look at the irc channel like wow where where these guys come from they're
[2621.24 --> 2626.68]  awesome i don't know them and so as soon as we saw that we're like we you know this is bigger than
[2626.68 --> 2632.58]  we than even we planned you know this this is what dot cloud is going to be about now and so we've been
[2632.58 --> 2637.16]  we've made it very clear that this is not just a side project we're building you know we're going
[2637.16 --> 2642.66]  forward dot cloud's going to be built on docker and then part of that is is you know bring it back
[2642.66 --> 2647.50]  into the existing product but you know also it's going to be building extensions to that product
[2647.50 --> 2656.42]  and you maybe you products you know natively on top of docker from day one yeah so is it a nice
[2656.42 --> 2661.04]  feeling like you know when you were a closed shop you know for lack of a better term and people would
[2661.04 --> 2665.60]  come to you with feature requests and you'd have to either you know go through the process of you
[2665.60 --> 2670.02]  know debating internally if this is acceptable and then who's going to work on it and all that but now
[2670.02 --> 2673.74]  somebody comes to you about docker with a feature request and you can tell them hey fork it and start
[2673.74 --> 2679.10]  to work on it yeah that is a nice feeling uh although then they do it and then you have to
[2679.10 --> 2683.80]  review the code and but it's it's a good problem to have yeah well and that and you bring up a good
[2683.80 --> 2689.08]  point and that's something that you know open source is great right because more often than not the
[2689.08 --> 2693.26]  community will kind of gather around it and and contribute to something that they find useful
[2693.26 --> 2698.94]  for a company like you guys how have you handled the problem of you know roles in the company you get
[2698.94 --> 2704.48]  used to doing things a certain way but now you have to kind of manage this you know and one thing
[2704.48 --> 2708.34]  we like to talk about on the changelog a lot is open source sustainability so now you have to kind
[2708.34 --> 2713.44]  of manage this open source project right and and what that means is you know standards code reviews
[2713.44 --> 2719.66]  um you know handling issues you know all that stuff so in general being a leader yeah yeah leading the
[2719.66 --> 2723.82]  project so internally does the whole team kind of take responsibility for that or how is that what does
[2723.82 --> 2728.68]  that look like for you guys yeah it's been it's been uh i mean when i say we've reorganized around
[2728.68 --> 2734.72]  docker i mean we have truly reorganized in a very significant way it's been a big change uh
[2734.72 --> 2741.30]  for everyone in the team for the company you know even in terms of strategy and also i mean for me
[2741.30 --> 2746.50]  personally i'm you know i'm the founder and ceo i've been kind of gradually transitioning
[2746.50 --> 2752.84]  over the last couple years from the guy who wrote the code to the guy who wrote the code with other
[2752.84 --> 2757.86]  dudes to the guy who wrote less and less code to the guy who raised money and you know hired people
[2757.86 --> 2762.92]  and you know ran meetings and all that stuff which is very interesting uh but you know i ended up in
[2762.92 --> 2768.04]  this kind of product focused ceo right i would kind of make calls when needed but mostly you know they
[2768.04 --> 2773.90]  you know the smart people have a tendency to do smart things on their own so uh and all of a sudden by by
[2773.90 --> 2781.66]  half by chance uh ended up actually being the guy um pushing docker forward as a side project
[2781.66 --> 2786.76]  mostly because the the rest of the doc lab team didn't have time they had more serious things to
[2786.76 --> 2794.52]  do with you know actually running the real product and um and then suddenly docker was no longer a side
[2794.52 --> 2801.16]  project so for me personally it's been a huge transition because um i'm the maintainer right i i review
[2801.16 --> 2806.92]  all the pull requests now thank god i have uh you know guillaume join as a as a maintainer so he
[2806.92 --> 2814.66]  reviews and merges things and you know that the the the the pool is is growing uh and i'll get to
[2814.66 --> 2819.22]  what that means as a process but so you know starting with my experience personally uh it's been a big
[2819.22 --> 2824.94]  change and it's really fun like it's it's it's good to be back to to coding every day uh you know i i maybe
[2824.94 --> 2831.22]  for for another time i'll i'll talk about what it means uh as a ceo mostly means just twice as much
[2831.22 --> 2835.42]  work because and you don't yeah and you didn't love the whole process of raising funds and dealing
[2835.42 --> 2842.62]  with board members and all that it's fun and i still do it um you know i mean it's one way or the
[2842.62 --> 2846.90]  other that that's that's a transition that has to be finished like at some point in the future
[2846.90 --> 2851.92]  it's fun to do both you know at some point in the future i'll have to end up being you know doing
[2851.92 --> 2859.38]  only one so does that mean uh handing over again the whole you know technical sides once that you
[2859.38 --> 2864.74]  know the the the the training process of other maintainers is completed then i go back to being
[2864.74 --> 2870.22]  a ceo or maybe i hire another you know ceo who knows but uh right now it's it's both and it's fun
[2870.22 --> 2875.74]  uh for the rest of the team what we've done is basically we've said okay there's the we've split
[2875.74 --> 2882.06]  the team in two as a start um it and i hope this is on topic but i think it is it's you know it's
[2882.06 --> 2887.66]  about the sustainable open source right so go for it yeah we've we've split the team into half of the
[2887.66 --> 2894.88]  team keeping the lights on uh on like okay we got this we got this existing product uh got production
[2894.88 --> 2901.14]  apps we got customers no matter what you know in this crazy period of one or two months where people
[2901.14 --> 2906.46]  are going crazy and we don't know what to what to do with all this all these pull requests basically
[2906.46 --> 2913.68]  falling in from this falling from the sky um let's let's split the team into two and you know half of
[2913.68 --> 2919.06]  the team um keeps doing things as usual uh and the other team uh you know works with solomon and we
[2919.06 --> 2923.20]  kind of build this open source process and so what we've done and this is on the open source side the
[2923.20 --> 2928.70]  big decision we've made which uh is very important and i think it's the best it's the best decision
[2928.70 --> 2934.16]  we've made in this whole thing is that we've opened the the the process to contributing to docker
[2934.16 --> 2941.82]  completely and i mean 100 percent uh there is no difference uh in how you contribute to docker
[2941.82 --> 2949.62]  uh based on where you work in other words the process that a dot cloud employee goes through to
[2949.62 --> 2956.88]  check code into docker or to influence or discuss the priorities of docker the you know design decision
[2956.88 --> 2964.00]  all that stuff is 100 percent the same as if you're not a dot cloud employee uh which means that
[2964.00 --> 2973.04]  um if you're willing and able and you got the time and you're interested the the prospects for um for
[2973.04 --> 2979.92]  implication and um and credit and influence over the project are exactly the same you can be a core
[2979.92 --> 2984.80]  committer if you want to and you can if you pass the standards and if you involve yourself enough
[2984.80 --> 2989.46]  and you know we don't yet have a core committer i mean it's only two of us who can actually merge
[2989.46 --> 2995.30]  pull requests um and you know guillem works at dot cloud but you know soon enough there's going to
[2995.30 --> 3000.78]  be a core committer that doesn't work at dot cloud i'm sure of it and i mean i can see very smart people
[3000.78 --> 3005.18]  putting a lot of energy and that that's going to be an awesome moment and i think it's really important
[3005.18 --> 3010.24]  what was the process to come up with that idea though to have that um the same process for me if i
[3010.24 --> 3014.64]  forked it and wanted to contribute was that your idea was it the team's idea how did you come up with that idea
[3014.64 --> 3022.52]  that was that was me um basically me right here that was me that was me yeah i mean i don't know
[3022.52 --> 3028.80]  you asked i like that i like the way you responded that was me um uh you know basically here here's
[3028.80 --> 3034.74]  the thing it was kind of unusual territory because here i was kind of uh the maintainer of an open
[3034.74 --> 3040.38]  source project uh and not the guy supposed to be writing code you know as a day job anymore
[3040.38 --> 3047.48]  um and and you know we have this whole engineering team and and uh sam is our director of engineering
[3047.48 --> 3052.64]  he's got this whole process in place i mean we're you know we're a highly organized company you have
[3052.64 --> 3057.48]  to when you're running you know again you're running apps in production and there was this problem of
[3057.48 --> 3064.46]  steering um steering resources away from the core platform i mentioned before we split the team in
[3064.46 --> 3071.12]  two in fact you know we split it in two but you know we didn't split in two equal equal parts uh
[3071.12 --> 3080.40]  you know most of the resources uh have to you know had to stay allocated to the the main product
[3080.40 --> 3085.70]  and at the same time if we're really betting the the farm on docker it needs to move fast and we've been
[3085.70 --> 3091.72]  really really bent on making docker move as fast as possible we've shipped a lot of stuff
[3091.72 --> 3099.22]  the only way to keep shipping fast is to get a lot of people working on it uh and the only way to get
[3099.22 --> 3104.96]  a lot of people working on it if you can't afford to hire hundreds of people is to you know set up a
[3104.96 --> 3110.48]  process that actually makes it possible potentially for hundreds of people to contribute and you know
[3110.48 --> 3116.06]  we're a long way from hundreds of people checking in code but i mean that's the trajectory where we're
[3116.06 --> 3120.82]  we're being aggressive about it you also said that you're going to build dot cloud on top of docker and
[3120.82 --> 3124.98]  right now you have a disclaimer saying docker is still under heavy development so it seems like
[3124.98 --> 3130.74]  it's stable but maybe not as much as it possibly could be to actually build dot cloud on top of it
[3130.74 --> 3136.08]  is that right yeah so i mean so obviously you would want to put a lot of energy into it if you're
[3136.08 --> 3141.62]  gonna you know build dot cloud on top of docker you kind of want to get to a point where it's
[3141.62 --> 3146.44]  even more stable and we are and we're gradually i mean every day there's a little more of our
[3146.44 --> 3150.92]  resources going as a company going towards docker than the the the core product because it feeds
[3150.92 --> 3157.76]  back right so it's an investment uh but the way the way this can the only way this can possibly work
[3157.76 --> 3164.54]  is by really you know building a real community of people who are outside of the company and actually
[3164.54 --> 3173.82]  own the project with us if that makes sense um and about um production readiness you're definitely
[3173.82 --> 3177.46]  right it's not you know you can't run an application production in on docker actually
[3177.46 --> 3184.92]  it turns out you can because i found out that at least one company does but you know hey if it works
[3184.92 --> 3192.00]  for them uh it will be production ready soon and the other thing also is that um docker is a great
[3192.00 --> 3197.92]  development and testing tool so a lot of people actually use docker to develop and test in an
[3197.92 --> 3203.42]  automated way and then there are ways to you know you can you can you can still still take the result
[3203.42 --> 3211.60]  of your work you know take your docker containers and export them into any environment that you actually
[3211.60 --> 3219.30]  use in production so there's a bridge there uh docker doesn't actually need to to be entirely
[3219.30 --> 3225.44]  production ready all you know across the entire life cycle of your app to be useful you can use it on a
[3225.44 --> 3232.66]  segment of that life cycle does that make sense so uh you can start using it as a dev and build uh
[3232.66 --> 3237.30]  tool and if if you're you get more comfortable and you feel like it's it's it's getting it's it's
[3237.30 --> 3241.28]  ready you can you know get a good feel for it you can start using in the next stage which is usually
[3241.28 --> 3248.88]  usually qa you know this um continuous delivery um things like that and then if you're even more
[3248.88 --> 3253.04]  comfortable then eventually you can say hey you know what i'm going to run this in in in production or
[3253.04 --> 3257.72]  you know production for the small app and not for the big app yet right uh it's a very it's a gradual
[3257.72 --> 3263.98]  process right it's it's it starts with the with the you know day one of development and then it moves
[3263.98 --> 3272.22]  it moves it moves along the it matures along with the application so the only supported uh distros are
[3272.22 --> 3280.70]  looks like the latest ubuntu's is that right officially supported yeah so um i guess there are two answers
[3280.70 --> 3287.48]  yeah the the the the only officially supported distro today uh where you can drop that docker binary and
[3287.48 --> 3298.78]  run it is ubuntu but uh there are officially supported uh install instructions for uh going from
[3298.78 --> 3308.70]  a mac laptop to a running uh docker setup a windows machine to running um docker setup and
[3308.70 --> 3315.82]  any other linux distro to running docker setup uh and usually that that means going through you know
[3315.82 --> 3321.20]  deploying a vm right so you you add a vm to your machine and then on top of that vm you run docker
[3321.20 --> 3329.02]  so we hit last week on the show we had uh mitchell from vagrant and looks like i got docker up and
[3329.02 --> 3334.50]  run pretty easily uh using vagrant on my machine yeah that's that's the way we recommend it if you've got a
[3334.50 --> 3342.98]  mac or a or a windows machine just use vagrant and vagrant will you know in our from in our in our
[3342.98 --> 3350.44]  case what vagrant does that is really really awesome is you know if you've got an os that's
[3350.44 --> 3355.10]  not supported it's a nice and automated way to stand up a virtual box vm and boom install something
[3355.10 --> 3360.76]  on it and in our case docker so that's really nice so it's funny because um you know and one of the
[3360.76 --> 3365.50]  things that mitchell says so obviously i'm a mac guy um you know and so i'm on a laptop i'm on a
[3365.50 --> 3372.62]  macbook so early on in vagrant's lifetime they decided um we need to support windows like that's
[3372.62 --> 3377.72]  a you know that was one of not mitchell but um i think his name is john uh said you know we need to
[3377.72 --> 3383.14]  have windows support baked in and so they did right and you know now fast forward again number of years
[3383.14 --> 3390.26]  and are you guys thankful that you're able to use vagrant on windows to get docker up and running
[3390.26 --> 3398.70]  um yeah i mean the the vagrant's a really cool project um they're actually they're right now they're
[3398.70 --> 3405.12]  there are more people definitely using docker from max than from windows machines but there definitely are
[3405.12 --> 3412.98]  um windows machines and from experience on the developer base on you know on doc cloud in general
[3412.98 --> 3419.82]  a lot obviously a lot of people use windows i think there's kind of this san francisco bubble
[3419.82 --> 3425.04]  we're a san francisco based company there's this kind of san francisco silicon valley bubble world of
[3425.04 --> 3432.16]  ah no one uses you know windows anymore but yeah actually a lot of people do and if you want to be
[3432.16 --> 3437.70]  taken seriously you gotta you know your tool has to support it so yeah we're we're in general i will
[3437.70 --> 3444.70]  say this that we have a philosophy of not reinventing the wheel that sounds kind of obvious but we will
[3444.70 --> 3451.80]  we will take every opportunity to reuse uh other people's work if it makes sense and if it allows
[3451.80 --> 3458.78]  us to focus on the hard parts that never no one got to uh and i mean there are lots of examples of that
[3458.78 --> 3465.40]  one example is using vagrant because hey we could start by writing code that automatically spins up vms
[3465.40 --> 3472.30]  from windows and installs docker on it uh but that would be time we wouldn't be spending on
[3472.30 --> 3479.08]  more interesting parts of docker right so we're using vagrant and hey everyone's happy uh it's easier
[3479.08 --> 3485.32]  to use docker and a lot of people uh discover vagrant actually through docker i i saw a lot of tweets
[3485.32 --> 3491.08]  saying hey uh i got you know two projects for the price of one i discovered vagrant so that's awesome
[3491.08 --> 3497.68]  you know another example would be um i mean lxc itself the the when you there is an ambiguity
[3497.68 --> 3505.12]  actually when in the word lxc it stands for linux containers but actually it can mean two things
[3505.12 --> 3512.70]  it can mean um the the the component inside the linux kernel that makes containers possible
[3512.70 --> 3523.02]  um and it can mean the the the higher level tools uh the binaries that you you know that the command
[3523.02 --> 3530.56]  that you run on your linux box to make calls to the to those kernel facilities and both are called lxc
[3530.56 --> 3537.34]  so there's lxc the current the kernel component that you never see uh as a user and then there's lxc the
[3537.34 --> 3546.20]  the command line tool um and you know one one thing that we could have done was uh bypass
[3546.20 --> 3554.90]  the lxc command line tool and make calls to the kernel functions directly because really we you know
[3554.90 --> 3559.32]  what we're really going after is the kernel's capabilities that's where the heavy lifting's
[3559.32 --> 3566.10]  done right in a way the lxc command line tools are themselves convenience wrappers higher level tools
[3566.10 --> 3575.58]  for using the kernels features right so um you know we we could bypass them uh but bypassing them is
[3575.58 --> 3581.80]  work and you know they've you know the the developers of the lxc tools have actually done good work
[3581.80 --> 3591.96]  they've tested it they've uh you know they've these added these nice conveniences uh so that's another
[3591.96 --> 3597.68]  example just like we use vagrant we we actually make calls of the lxc command line tools uh so we
[3597.68 --> 3605.20]  don't waste time reinventing the wheel right yeah i mean it's like where docker is at right now it's
[3605.20 --> 3611.86]  so young it's you know so early in the process it's very exciting i mean to see where this is going to
[3611.86 --> 3618.18]  go uh so for you right now where docker is at where would you like to see it kind of go over the next you
[3618.18 --> 3627.98]  know six months to a year so there's there's kind of two key there's two main things um over the last
[3627.98 --> 3636.38]  few weeks we've realized that people are using docker as a build tool so initially the job of docker was
[3636.38 --> 3643.02]  specifically um given a container in the right format run it in a guaranteed repeatable way
[3643.02 --> 3651.78]  uh and and define the format the executable format right write the spec standardize what what it means
[3651.78 --> 3657.68]  to run a container and and share that standard with the world uh and show an implementation of it so
[3657.68 --> 3662.96]  in other words the run part running things uh and that that was you know that's that's the core of
[3662.96 --> 3669.30]  docker and you can run things in a very reasonable way in a very portable way and etc etc uh and then
[3669.30 --> 3677.72]  um on top of that we saw people using building on top of that functionality to build their software
[3677.72 --> 3684.60]  um uh because you know running a container is is is one thing but how did you get that container in
[3684.60 --> 3690.68]  the first place like who built it like who put it together and it turns out docker itself can be used
[3690.68 --> 3698.42]  to put together your container step by step layer by layer uh in a really cool and convenient way
[3698.42 --> 3705.48]  and and it solves that problem of defining dependencies um and so that became a pattern
[3705.48 --> 3712.74]  people started using docker like that um installing a base image and then um installing a debian package
[3712.74 --> 3718.78]  they were interested in then downloading a library and dropping it in the right place installing i don't
[3718.78 --> 3724.98]  know uh you know uh unicorn then installing the version of ruby they're interested in the gems they're
[3724.98 --> 3732.70]  interested in and and all that layer by layer using our our container versioning system and you
[3732.70 --> 3737.40]  know i don't want to go in crazy details but uh so that use case kind of evolved and as a result
[3737.40 --> 3743.28]  you can use docker for build and for run and so these are the two directions we're pushing we want
[3743.28 --> 3751.24]  docker to be a better build tool and so literally you can dockerize your app i've realized that's a term
[3751.24 --> 3757.54]  now is it really cool yeah so dockerizing your app means well i heard you say containerize uh at least
[3757.54 --> 3762.38]  in your documentation somewhere too yeah you containerize things but dockerize is shorter
[3762.38 --> 3769.82]  and i don't know i it's funny because the the i was i did not come up with the the the the name docker
[3769.82 --> 3776.22]  i initially thought it was really bad and sounded terrible and i i actually was i had the secret plan of
[3776.22 --> 3781.84]  convincing everyone to change it before we we launched but then it got leaked and i never got
[3781.84 --> 3788.42]  the chance and yeah and i kind of it kind of grew on me i kind of like it so you know uh anyway the the
[3788.42 --> 3796.32]  so dockerize um dockerizing your app means uh adding to your to your git repository or you know to
[3796.32 --> 3803.44]  your source code a file called a docker file um with instructions on how to trend you know how to go
[3803.44 --> 3810.88]  from naked source code to to full-blown container ready to run uh and usually that file is like
[3810.88 --> 3818.66]  five lines it's really simple it's basically like shell commands to run it's like ap to get install
[3818.66 --> 3826.64]  that uh you know pip install that gem install that whatever um and it's dead simple but at the same
[3826.64 --> 3834.28]  time it goes from you know source code to freaking full-blown container ready to run and you can hand
[3834.28 --> 3839.64]  it to someone and they can run it on ec2 machine they can run it on their vm they can run it you know
[3839.64 --> 3845.74]  anywhere they want and you don't have to give them any off-band information you just say here it is
[3845.74 --> 3851.60]  you can run it and that is really awesome so you know i want that to be easier because i think it's just a
[3851.60 --> 3858.48]  really cool way to use docker and then obviously i want um you know once you've produced that docker
[3858.48 --> 3864.56]  container you know i want it to be more useful in more places so there are people today saying you
[3864.56 --> 3869.96]  know obviously hey i use red hat or i use you know this or that distro or i got this version of the
[3869.96 --> 3875.56]  kernel and today i can't use docker containers i can't run them because docker doesn't support this
[3875.56 --> 3880.54]  distro or doesn't support this version of the kernel so we want to you know widen the scope
[3880.54 --> 3888.86]  make running docker containers possible in more places and and that also means part of of you know
[3888.86 --> 3894.74]  making it possible to run in more places involves things like allowing for more customizations
[3894.74 --> 3901.54]  like there are a lot of requests especially for ops or shops like ops engineers that already have a
[3901.54 --> 3907.54]  setup they have a storage system they have a networking system in place and they kind of they have a
[3907.54 --> 3912.68]  process manager and they kind of they they like docker but they would like to bend it to fit into
[3912.68 --> 3918.94]  their existing system and i say you know obviously we we want that to be possible so there are a lot of
[3918.94 --> 3926.42]  integration projects uh and for integrations you need nice clean apis so i guess that was a long
[3926.42 --> 3932.16]  answer but a i want docker to be to make it easier to build your source code into a container that can run
[3932.16 --> 3941.06]  anywhere and and b i want it to be easier to run that container any on any server yeah this whole time
[3941.06 --> 3945.14]  you we kind of got through this most of this call we haven't mentioned docker registry yet i'm just
[3945.14 --> 3951.26]  wondering if i missed it or if we didn't cover that and and it seems like it's you know it fits nicely
[3951.26 --> 3955.98]  into that feature just painted definitely yeah it's it's kind of the link between the two that the
[3955.98 --> 3962.18]  the the when you build your source code into a container the logical step after that is you want
[3962.18 --> 3968.18]  to make that container accessible right you want to share it uh and if it's open source software
[3968.18 --> 3974.42]  um sharing it means hey you want every person on earth and to to be able to download it and run it if
[3974.42 --> 3981.56]  they want uh if it's um if if it's private and it's your own code it has credentials in it it's not open
[3981.56 --> 3989.30]  source um sharing might just mean hey i wanted to get from get it from the build server to the
[3989.30 --> 3993.90]  production server you know or on a scale out to 10 servers that's also sharing you know it's moving
[3993.90 --> 3999.12]  bytes around um to share you need you know some sort of infrastructure to move things around and
[3999.12 --> 4005.98]  discover the right container and download it it's what the registry is so the registry is what does that
[4005.98 --> 4011.52]  live at now where can you see that we've put together at dot cloud it's uh well i mean
[4011.52 --> 4018.44]  the the primary way you interact with it is by typing the command docker pull right or docker push
[4018.44 --> 4024.92]  um so right now like if you install docker from scratch fresh the first command you'll probably run
[4024.92 --> 4033.44]  is something like docker run uh ubuntu bash which means hey run run the shell in a in a in an ubuntu
[4033.44 --> 4040.90]  system or docker run centos uh ls you know like run show me the files in my in my in a new centos
[4040.90 --> 4047.32]  container when you type that command docker you know figures out that you want you want to run an
[4047.32 --> 4052.84]  ubuntu container an ubuntu call sorry a container called ubuntu it doesn't have it so it will
[4052.84 --> 4058.12]  automatically connect to the registry which is this publicly accessible place uh think of it like
[4058.12 --> 4066.72]  github for containers ready to run right uh and um it will download it and it has a very efficient way
[4066.72 --> 4071.78]  of downloading like you know um it's just like a git pull actually it will only download the parts that
[4071.78 --> 4076.66]  it needs so if it's only already downloaded the prior version it'll only download the diff
[4076.66 --> 4083.10]  which is really nice and and then it will run it and so the registry is this place this api that we've
[4083.10 --> 4088.88]  you know put up for free to make docker more useful where you can download other people's containers
[4088.88 --> 4094.56]  or upload your own right since once you've built your code into a container you just then you upload it
[4094.56 --> 4100.68]  to the registry and other people can share it uh to can use it so that i guess it's it's the link
[4100.68 --> 4109.52]  between build and run yeah that's awesome man i feel like we could talk about that for a few months
[4109.52 --> 4114.38]  as this thing grows again to talk about you know where it's gone it's very exciting yeah we'll definitely
[4114.38 --> 4118.46]  have to check back in with you because we want to we want to hear your six month year goal and see if
[4118.46 --> 4123.10]  it comes to fruition and we'll obviously be uh there helping you along so in between now and then
[4123.10 --> 4127.52]  anything we can do at the changelog to help you spread the word about the awesomeness of docker
[4127.52 --> 4132.80]  you know please do not hesitate to reach out to us we'll do whatever we can to help thanks i appreciate
[4132.80 --> 4138.98]  that so the for people who have listened to the changelog regularly they'll know this but for anyone
[4138.98 --> 4143.80]  who's new we kind of have two questions that we like to ask at the end of all of them and um just to
[4143.80 --> 4150.28]  get a little give you a chance to kind of um participate so first one uh solomon is we kind of look for
[4150.28 --> 4154.74]  what would be a call to arms or somewhere where that you would like to see the open source community
[4154.74 --> 4162.58]  get involved in docker uh well i mean i guess there's a general answer besides the the the obvious
[4162.58 --> 4168.86]  uh you know try it use it report bugs come hang out on the rc channel kind of get involved in any way
[4168.86 --> 4178.02]  possible we are extremely uh welcoming of any interaction like we will never uh we'll never uh you know
[4178.02 --> 4183.72]  make fun of someone for making a really small fix like every fix counts every question there was no
[4183.72 --> 4190.62]  stupid question you know the the so you know we're we're we're very grateful of any interaction you
[4190.62 --> 4196.90]  know it means you you're interested so check it out ask questions and then more specifically i talked
[4196.90 --> 4203.96]  about that really cool word dockerize yeah um i i'm just really excited about that concept i think it's
[4203.96 --> 4211.24]  really powerful it solves a lot of problems that i've ran into as a developer um there are a lot of
[4211.24 --> 4217.56]  people dockerizing their their apps you know dockerizing famous open source software you know
[4217.56 --> 4226.26]  dockerizing databases frameworks uh libraries um so my call to arms would be try and dockerize something
[4226.26 --> 4233.32]  and tell us how it went you know share it with us right now we're you know every time some someone
[4233.32 --> 4239.80]  sends us a cool example of software they've packaged to run in docker we're really excited we tell everyone
[4239.80 --> 4247.92]  about it um you know just tell us and we'll we'll we'll we'll share with the whole world um and probably
[4247.92 --> 4256.00]  you'll hit a bug too and then you should report that cool so our last question who would you like to
[4256.00 --> 4262.92]  kind of give a shout out to as your programming hero you know i i'm glad you allowed me to prepare
[4262.92 --> 4275.80]  for that one um you know i realize i i i'm not a very um learned person when it comes to the the giants
[4275.80 --> 4282.84]  on who on you know on whose shoulders we stand on but um there is one guy that i that i've always
[4282.84 --> 4287.24]  been super impressed with i guess it's kind of a classic but i don't know if you know this guy
[4287.24 --> 4296.70]  fabrice bellard he's this french dude um also known as the author of qmu okay what's his uh what's
[4296.70 --> 4306.26]  his github handle uh or we can we can link that up in the show notes basically he i mean he he has
[4306.26 --> 4316.16]  written at least half a dozen um pieces of software that each individually um would easily
[4316.16 --> 4323.02]  get him a place in the pantheon of coders but he wrote like six of them and he's just kind of he's
[4323.02 --> 4327.38]  incredibly productive he's the guy i don't know the most recent thing i i saw by him is he's the guy
[4327.38 --> 4332.12]  who got a linux kernel to actually boot in a browser in javascript you guys remember that
[4332.12 --> 4339.22]  vaguely i mean anyway so it's it's like just one example he's just kind of he never stops uh and
[4339.22 --> 4348.68]  it's kind of refreshing um to to see someone that productive i mean ffmpeg is um i mean it's the it's
[4348.68 --> 4354.86]  the it's the foundation of video processing right it's the video processing open source software that's
[4354.86 --> 4365.90]  that's him um qmu is like a uh really um a really effective and very helpful piece of virtualization
[4365.90 --> 4370.56]  software so it was kind of a stepping stone to virtualization i missed it though what is his what
[4370.56 --> 4377.14]  is his name uh fabrice bellard fabrice bellard okay billards i feel like i'm butchering his name we'll
[4377.14 --> 4381.60]  definitely have to put that in the show notes yeah he's he's awesome and and you know that's the
[4381.60 --> 4389.12]  thing i've never i've never seen tweets by him uh probably tweets i don't know but he he's not like
[4389.12 --> 4396.62]  a uh you know like a doesn't seem to be someone who's cultivating his his personal brand or whatever
[4396.62 --> 4401.56]  he's just writing awesome code and seems to enjoy it and we're all benefiting from it i mean he's yeah
[4401.56 --> 4407.46]  he's the he's the like the good side of open source incarnate he's behind the tiny c compiler i know that
[4407.46 --> 4414.32]  nice yeah he's he's anyway i never met him but i just picture him as this really cool guy well
[4414.32 --> 4422.44]  that's that's awesome thanks for plugging him and and uh yeah we always uh enjoy um i guess the the
[4422.44 --> 4427.70]  surprises sometimes even not so much surprises that you choose somebody who may not have gotten all the
[4427.70 --> 4433.50]  limelight that uh some developers get uh when it comes to open source contributions and what they
[4433.50 --> 4439.78]  contribute and what they create so it's always good and it also helps our audience to um you know
[4439.78 --> 4444.98]  and those who are enthusiasts of software and the intersection of you know software development
[4444.98 --> 4450.12]  and this open source world that we're kind of crafting away at so it's it's really fun to to
[4450.12 --> 4456.08]  share that but uh solomon thank you so much for for joining us andrew thanks for asking so many great
[4456.08 --> 4462.08]  questions i definitely lean upon you today when it comes to the devops side i i uh sit back and listen
[4462.08 --> 4468.58]  very closely and hope one day that i can uh be such a such a hacker but uh and this you guys were
[4468.58 --> 4474.16]  right thanks thanks so much for this is really a cool conversation yeah man and this is our first
[4474.16 --> 4480.64]  time here on five by five so for those of you who are long time five by five listeners and first time
[4480.64 --> 4486.70]  changelog listeners uh we're here to stay five by five dot tv slash changelog live every tuesday at five
[4486.70 --> 4491.74]  o'clock you can tune in as you normally do if you got the app uh watch out for push notification and if
[4491.74 --> 4497.90]  you didn't get it you need to go into your settings and uh and turn that on for the changelog as well
[4497.90 --> 4503.90]  as finder's talk because i uh i host finder's talk so that'll be left tomorrow uh same time on wednesday
[4503.90 --> 4509.68]  but uh thanks again for tuning in uh let's say goodbye guys all right thanks so much solomon i really
[4509.68 --> 4512.56]  enjoyed the conversation thanks thanks to you guys
[4512.56 --> 4515.84]  you
