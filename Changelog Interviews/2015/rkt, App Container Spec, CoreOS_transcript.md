[0.00 --> 15.86]  welcome back everyone this is the change log and i'm your host adam stekowiak this is episode 138
[15.86 --> 23.14]  jared and i talked to alex pulvey the ceo of core os great conversation today talking about
[23.14 --> 28.78]  containerization specifically their awesome new open source product called rocket a competitor
[28.78 --> 34.56]  to docker specifically to standardize the app container spec great conversation around that as
[34.56 --> 41.04]  well um alex great guy today going to have this conversation we have some awesome sponsors making
[41.04 --> 46.12]  the show possible code ship top towel and for those who do not know what i'm saying when i say top towel
[46.12 --> 54.24]  i'm saying t-o-p-t-a-l.com i'm assuming their their name i have never asked brendan this so this is
[54.24 --> 58.62]  going off the script a little bit whether or not their name is based on top talent i'm going to
[58.62 --> 65.32]  assume that but it's t-o-p-t-a-l.com top towel great support for the show and not to mention we also
[65.32 --> 70.36]  have the support of rack space we'll tell you a bit about those guys later in the show but code ship
[70.36 --> 75.64]  is an awesome sponsor of ours uh in fact one cool thing i want to mention about code ship recently
[75.64 --> 81.02]  they just listened to all sorts of feedback they got from their users uh and recently redesigned
[81.02 --> 85.48]  their entire application not only does the new design look better but it also has tons of new
[85.48 --> 90.24]  usability improvements to make things even easier than before you can set up continuous integration
[90.24 --> 95.06]  for your app in just a few steps and to pull your code with all your tests to pass no matter what
[95.06 --> 98.00]  language you use no matter what framework you use they have great support for lots of languages
[98.00 --> 103.84]  and frameworks they integrate with github or bitbucket uh you can deploy to cloud services like
[103.84 --> 110.40]  roku and aws setup takes just three minutes you can find code ship at code ship.com
[110.40 --> 117.04]  slash the changelog make sure you go to that url use the offer code the changelog podcast to get a
[117.04 --> 124.26]  20 discount on any plan you choose for three months also you want to check out their blog at blog.coachship.com
[124.26 --> 130.66]  to get updates again the offer code to use is the changelog podcast and get 20 off on any plan you
[130.66 --> 138.98]  choose for three months and now on to the show all right today we're back hey the changelog here adam
[138.98 --> 146.92]  jared and alex alex pulvey from core os the ceo of core os uh we're here to talk about core os
[146.92 --> 155.00]  linux containers rocket specifically um maybe a little bit about docker who knows but alex welcome
[155.00 --> 160.24]  to the show how are you thank you for having me doing great doing great happy to share the story
[160.24 --> 168.98]  yeah i think um we've been watching docker closely um and obviously we're excited to see a new
[168.98 --> 176.42]  opportunity for you know not just docker but what rocket offers and you seem to have a unique way you
[176.42 --> 182.44]  brought it uh out i guess into the ecosystem of open source but before we go there maybe give an
[182.44 --> 189.46]  introduction to you know who you are and what you do at core os maybe maybe uh from that we'll blend
[189.46 --> 196.80]  into more a little bit more of like what chorus is just for the audience who may not know sure um so
[196.80 --> 203.72]  i am the ceo of core os i'm one of the co-founders with brandon phillips uh we started working on core
[203.72 --> 210.60]  os about two years ago now um before core os i was at rackspace uh which i joined through the
[210.60 --> 216.42]  acquisition of my previous company cloud kick um cloud kick built tools for cloud server monitoring
[216.42 --> 224.02]  management um and before coros brandon was um at novelle uh working on susi as a as a linux kernel
[224.02 --> 230.10]  developer so you know when you put a kernel guy and a cloud guy together you get a caudios
[230.10 --> 239.78]  there you go um and this is actually this is episode 138 right jared right and so since you
[239.78 --> 244.04]  mentioned rack space rack space is actually a sponsor of this show so it's kind of funny that
[244.04 --> 252.40]  you have some rack space in your blood yeah i bleed red yeah austin texas well the you know those who
[252.40 --> 258.02]  listen to the show forever but you may not know this alex um the changelog's born in texas right so
[258.02 --> 264.38]  we're not very far from your your your previous mothership so to speak got it got it so maybe a bit
[264.38 --> 272.84]  a back uh story on on core os itself age you know what is it what is it for that kind of thing
[272.84 --> 281.52]  sure so uh we shipped our first release of core os in august of 2013 um and and at the time you know
[281.52 --> 287.30]  core os is a lightweight linux os that updates itself um and i can get into why that's important
[287.30 --> 293.74]  um but you know it's a it's a kind of a rethink on what a server linux operating system should be
[293.74 --> 299.80]  um and we felt that you know the time was right uh to build something like that and and with containers
[299.80 --> 305.48]  emerging as a thing right around the same time you know we've really kind of you know grown into this
[305.48 --> 311.30]  this um you know this set of tools for helping companies build their next generation of of
[311.30 --> 315.72]  infrastructure kind of centered around containers and distributed systems and and and really getting
[315.72 --> 320.48]  security right as well that's one of the things we care a lot about so you guys have a ton of open
[320.48 --> 327.06]  source projects up there at uh github.com slash core os uh at cd i think being the biggest one but is
[327.06 --> 332.74]  is core os itself open source or do you guys have like a proprietary core and then open source
[332.74 --> 340.96]  kind of in the in the ecosystem sure so the way we work um first our team is all open source um
[340.96 --> 347.12]  i'd say zealots because there's really a better word for it uh but our our team is all uh you know
[347.12 --> 351.44]  very strong open source folks i was before my previous company i was at mozilla i was the 12th
[351.44 --> 355.38]  employee at the mozilla foundation and bernan and i actually started working together at this thing
[355.38 --> 361.48]  called the open source lab which ran the servers for apache.org kernel.org mozilla.org kind of all the
[361.48 --> 367.46]  big open source projects so open source is is definitely in our dna and um the way that we
[367.46 --> 373.34]  go to market with all of this stuff is we build open source components which are open source through
[373.34 --> 378.44]  and through we want them to be like the apache 2 web server of whatever they're trying to solve
[378.44 --> 383.40]  and that just ubiquitously used and no company really directly monetizing them um and then to
[383.40 --> 388.50]  have a business to make our efforts sustainable we sell commercial products and those products are
[388.50 --> 394.24]  more full solutions they're end-to-end things that have dashboards and and you know easy to set up and
[394.24 --> 399.58]  it's a full-on product solution and so there's kind of two you know two types of software that
[399.58 --> 403.44]  we build there's all the open source components which are individually useful and reusable and
[403.44 --> 407.66]  vendor neutral and use them however you want and then there's software commercial products that you
[407.66 --> 412.58]  can buy from us um that you know take advantage of of the components that we're building but they are
[412.58 --> 417.68]  they are at the end of the day products that companies go and buy you mentioned brandon uh in there
[417.68 --> 422.80]  brandon phillips uh can you i know he can't be here he i think we might have him on a different show i'm not
[422.80 --> 426.28]  really sure kelly what we she's not really on the call she's listening behind the scenes maybe you
[426.28 --> 432.02]  can say hi kelly hello hey so there's kelly so kelly helped us set up this call uh little funny story
[432.02 --> 437.40]  there she put her phone number in the email i needed to talk to her right away a funny little side chat i
[437.40 --> 441.92]  called her right away and i said hey we got to have alex on the show uh we couldn't wait until like
[441.92 --> 447.84]  late february and we had to have it happen in january so kelly is is uh is awesome she made magic happen
[447.84 --> 452.40]  for us so that's that's good there but brandon was supposed to be on the call at some point but
[452.40 --> 457.56]  can you give like a brief intro of who brandon is and sort of what role he plays uh for the team
[457.56 --> 466.16]  sure brandon is our co-founder and cto um he really is the kind of technical mind behind all this you
[466.16 --> 471.32]  know i'm a pretty technical guy um but but brandon is is what's driving kind of the architecture and
[471.32 --> 476.58]  overall decision making on the on you know on the day-to-day uh technical details of everything
[476.58 --> 481.22]  you do so when you look at for instance and we'll get into this but in rocket if you look at app
[481.22 --> 486.48]  container which is a specification it's almost like an rfc for what a container should be you know
[486.48 --> 491.26]  that's brandon's design kind of coming through and really shining and and uh you know he owns the
[491.26 --> 497.18]  the deep technical side of of the company i guess maybe um to to sort of give some premise to what
[497.18 --> 505.20]  this call is about um you know we like i said we've been watching docker fairly closely we've um
[505.20 --> 510.78]  we've had them on the show to talk about things and stuff like that so we really wanted to to sort
[510.78 --> 516.00]  of just kind of dig into talking about core west talking about containerization you've got your own
[516.00 --> 520.82]  philosophy on it which is where rocket came from and just really drive into that so what's the easiest
[520.82 --> 529.14]  way to open up that conversation sure i mean maybe we can we can talk about um i think first i'd like
[529.14 --> 532.62]  to give a little bit of background on core west overall and why we started building it and i think
[532.62 --> 538.14]  it'll help kind of paint the picture of why rocket is what it is and and why uh you know why we built
[538.14 --> 542.42]  it as an alternative to docker um so maybe we just start with that a little bit of background on core
[542.42 --> 550.80]  west sounds good all right so go for it alex go for it all right go for it
[550.80 --> 558.54]  and so core west um you know after after the acquisition with rack space and you know helping
[558.54 --> 563.22]  rack space build out some different cloud products um you know took a little bit of time off to figure
[563.22 --> 568.64]  out what to work on next and when brandon freed up um you know we we've known each other for a very
[568.64 --> 574.14]  long time and and we looked at sort of you know what do we know best and what what is something we
[574.14 --> 578.94]  could do you know that has good social value as well as could be a good commercial value uh you know
[578.94 --> 584.32]  have good commercial value down the road and and what we looked at was security and we we asked
[584.32 --> 589.14]  ourselves what could we do to fundamentally improve the security of the internet okay kind of a big
[589.14 --> 593.90]  lofty goal yeah you know um but we thought hey if we could build something that could do that then you
[593.90 --> 598.08]  know there's probably some commercial value there and also it's something that you know like us and
[598.08 --> 603.24]  our friends are are well positioned to actually go and sort out too so might as well go for it um and
[603.24 --> 610.22]  and so the key insight uh that that we had is that security at the end of the day is all about
[610.22 --> 616.48]  updates there will always be another vulnerability another patch another issue um you can't harden
[616.48 --> 622.42]  software to be perfect but you can make it easy to update it when there is an issue um and on servers
[622.42 --> 627.84]  i mean servers are like notoriously you know get it running and don't touch it i mean some of the
[627.84 --> 632.72]  most fragile environments out there are these old server infrastructures that you know people um just just
[632.72 --> 637.08]  don't pay attention to anymore but yet that's where all the family jewels are that's where like all of
[637.08 --> 641.88]  our data is it's our social security numbers you know everything is on the server and so we thought
[641.88 --> 648.26]  hey let's build a server that automatically updates and if you talk to any sysadmin this is like a crazy
[648.26 --> 652.42]  idea okay like any any system may be like wait a minute you can't automatically update my server
[652.42 --> 657.40]  you're gonna break everything right um and so we felt this is a perfect thing for a startup to go
[657.40 --> 661.72]  and try to do everybody thinks it's not possible and if it works it unlocks a lot of value
[661.72 --> 666.82]  all right and that value is not just security it's it's you know reliability it's performance
[666.82 --> 671.88]  it's like everything you get by running the latest version of software okay um and so that's really
[671.88 --> 676.96]  where we started um and and and uh that's that's why you know you might have if you read anything
[676.96 --> 681.20]  about core os you you see us message on the updates quite a bit um because we think that that's kind
[681.20 --> 687.86]  of a basic requirement for good security i was gonna say that sounds like a when i heard you say you
[687.86 --> 692.86]  know automatic updating system i just think it sounds awesome and terrible at the exact same time
[692.86 --> 697.76]  so let's talk about how we do it all right it's not uh it's not trivial and it requires a lot of
[697.76 --> 702.32]  changes and that's why core os is quite a bit different than than the existing server os is out
[702.32 --> 707.98]  there today so one of the first things you we need to solve when we want to go update a server is
[707.98 --> 712.62]  is how you package and deploy your applications and one of the main things that breaks when you update
[712.62 --> 718.58]  a server is inter-application dependencies so you go do your patch to heart bleed and fix open ssl
[718.58 --> 724.36]  and it works for your java app but it breaks your other thing that's running on the server um and so
[724.36 --> 729.96]  our our solution to that is every application is packaged with all of its dependencies well what is
[729.96 --> 736.88]  that hey that's a container right and and so core os by design will only run applications inside
[736.88 --> 743.34]  containers containers are our package manager effectively um and so we got very lucky in that
[743.34 --> 748.18]  um you know docker came out around april of 2013 and and when that's we were in the middle of hacking
[748.18 --> 753.22]  on our first versions of core os then and we needed a container runtime that we either built ourselves
[753.22 --> 757.94]  because of you know just filling in the white space or um you know or use something off the shelf
[757.94 --> 762.56]  that that appears to be exactly what we would have built you know if we if we were left to our own
[762.56 --> 767.98]  devices and so that was docker and we released um you know core os with docker in our very first
[767.98 --> 774.72]  release we were the first like kind of docker native operating system uh to come out uh the first
[774.72 --> 779.96]  kind of container native um thing uh to come out and and we did it we did our updates from the very
[779.96 --> 784.00]  beginning so the very first release that we shipped was the one that we could update because we could
[784.00 --> 787.84]  just make the os better over time it's it's kind of like a software as a service but for a whole
[787.84 --> 792.42]  a whole os um and that's still what we do today when you know when heart bleed and shell shock
[792.42 --> 797.16]  came out our little sliver of the internet uh we had patched and fixed you know hours after the
[797.16 --> 802.92]  patches were available and not just like packages available for download like the running servers
[802.92 --> 809.38]  out there on the internet were upgraded and no longer vulnerable to the issue wow so it it's working
[809.38 --> 814.66]  the system's working containers are one of the things that that really enables that um and and that's
[814.66 --> 820.44]  how we got started with docker so early on so help me out with this infrastructure so core os is a
[820.44 --> 827.06]  linux distribution which is a kernel and some supporting software that only runs containers
[827.06 --> 833.40]  and as long as i have a container that you can run you're going to keep that that underlying
[833.40 --> 838.96]  infrastructure updated for me right my goal for core os is for you to not have to think about your
[838.96 --> 845.76]  os anymore um i want i just think that when you know a patch for shell shock comes out and we have
[845.76 --> 850.08]  all these individual ops teams around the world scrambling patching their servers that's just like
[850.08 --> 856.14]  a redundant effort that the world doesn't need to do that my team of of os guys can centrally patch
[856.14 --> 862.36]  the kernel and patch your open ssl vulnerability and deploy it to every server um that is sort of opted
[862.36 --> 867.78]  into our platform um and and we can take care of it for you centrally and and the tools that we've
[867.78 --> 873.50]  designed allow us to do it that way and do it you know kind of ultimately scalably as well uh we can you
[873.50 --> 879.92]  know you we can run millions of servers this way um you know and i can have my my small team of
[879.92 --> 885.08]  engineers developing the patches to do that so so what if i'm a user of the core os distribution but
[885.08 --> 891.84]  not necessarily a customer of your guys's ongoing update service how would i go about uh managing the
[891.84 --> 899.32]  the upgrades so just like you know the way ubuntu and red hat or fedora work um so our gift to the
[899.32 --> 904.40]  world is that steady stream of updates so we don't commercialize the updates themselves in fact all of
[904.40 --> 909.10]  our open source projects core os rocket fleet we don't directly commercialize it all um so like our
[909.10 --> 914.72]  our gift is that we give you that steady stream of updates um you know free of charge it's almost a
[914.72 --> 919.10]  community service um now again that's why we care a lot about our sustainability and why we sell
[919.10 --> 922.86]  commercial products is to you know keep keep those efforts going nice
[922.86 --> 930.40]  so of course you needed docker because you did not have the container environment when you guys
[930.40 --> 936.40]  wanted to launch um is that fair to say yeah i mean if you think about docker sort of originally
[936.40 --> 943.30]  it's it's a tool to download and run a container it's it's very much like apt-get or yum but instead of
[943.30 --> 950.12]  an rpm or a .deb file you're you're downloading uh you know a container image and executing it uh and
[950.12 --> 954.54]  that's it was our package manager effectively and still is our package manager today um but that
[954.54 --> 959.36]  that's how we were using it another another component towards how you build a system that
[959.36 --> 964.52]  you can automatically update another property that you want is you want any individual server to not
[964.52 --> 969.44]  matter so you want to be able to pull the plug on any server and and your environment keeps running
[969.44 --> 974.26]  now if you talk to your ops buddies they'll probably all agree that that's what they want too
[974.26 --> 978.94]  um but if if you ask them if they can do it they'll probably say no and that's because it's too
[978.94 --> 984.90]  difficult and and so that's why we started building kind of again at the lowest level a tool called etcd
[984.90 --> 990.14]  which is a distributed key value store primarily intended for shared configuration among servers
[990.14 --> 995.90]  as soon as you have more than one server you need to start sharing configuration um across those machines
[995.90 --> 1000.64]  and we built that because we want to make it easier for people to build these distributed platforms
[1000.64 --> 1007.14]  so you could run run things in this way um such that we can pull the plug on any machine and update it
[1007.14 --> 1012.72]  any time without you taking a down time um and and uh really filling in the white space and etcd was
[1012.72 --> 1018.08]  one of the first sort of areas of white space that that we saw uh needing to exist and etcd itself has
[1018.08 --> 1025.52]  been adopted by i mean kubernetes mesos cloud foundry kind of like every cloud platform ish thing
[1025.52 --> 1032.44]  that's emerging right now is chosen etcd is there an under underlying key value store nice yeah i'm looking
[1032.44 --> 1039.16]  at the etcd github page now looks like you have 134 contributors over 4 000 commits uh this looks
[1039.16 --> 1045.22]  like a really mature uh product so that's it's really awesome that's all open source and available
[1045.22 --> 1053.98]  um and looks like it's pretty popular as well yep so you started off with docker and you're still you
[1053.98 --> 1061.06]  still use docker to this day in your guys's core product um but there came a point in time where
[1061.06 --> 1067.08]  the docker philosophy and perhaps the core os philosophy about how to do containerization
[1067.08 --> 1075.36]  apparently those diverged can you tell us about that sure so docker originally came out it stopped it
[1075.36 --> 1081.22]  talked a lot about this this standard container this idea that we could have a unit that's an
[1081.22 --> 1087.08]  application that could be ran in many systems um and that you know what was decoupled from you know
[1087.08 --> 1091.46]  particular implementation it was about like package in a container and you know stick the container on
[1091.46 --> 1095.56]  a boat or stick it on a train and it all kind of works you know like using the shipping container
[1095.56 --> 1101.84]  analogy um what's happened over time is docker is clearly on a path to be its own platform now
[1101.84 --> 1108.24]  so while while docker started as a great tool for building a platform with and that's why we saw it
[1108.24 --> 1113.20]  inside of kubernetes inside of amazon's cloud product inside of vmware's products because these are
[1113.20 --> 1118.72]  existing platforms that wanted to add a container to it it's becoming a platform like those things i
[1118.72 --> 1123.42]  just listed off now by adding its own clustering and everything and i get the product decision
[1123.42 --> 1127.84]  there that's fine and i have no objections to it they should go and build their their platform that's
[1127.84 --> 1132.36]  great i mean we'll probably build a platform at some time too you know um so it's a it's a fine
[1132.36 --> 1138.76]  business idea um the the issue is we still want that standalone component that is not directly
[1138.76 --> 1143.38]  commercialized at all that allows you to download and run a container essentially like a package
[1143.38 --> 1150.08]  manager for containers to exist and so uh when it was clear that that you know docker was not investing
[1150.08 --> 1156.20]  in things like standards around what a container is for interoperability or you know just getting some
[1156.20 --> 1162.28]  basic security and composability issues right in the architecture of a unix tool um you know we said
[1162.28 --> 1167.76]  hey it's easier for us to go build uh build a new thing that sort of serves the needs of what we want
[1167.76 --> 1172.82]  uh you know versus you know send some pull request to docker that rewrites the project
[1172.82 --> 1183.68]  and this uh culminated in a launch of a new tool along with um some specifications that you're trying
[1183.68 --> 1192.22]  to get i guess formalized and community uh driven around uh containerization uh the tool we've
[1192.22 --> 1197.74]  mentioned called rocket um the announcement for that came back early december and it seems to be
[1197.74 --> 1203.52]  it caused a bit of a stir is that fair to say yeah you know that one got away from us a little bit
[1203.52 --> 1209.26]  um if you look back on the whole thing the only messaging we've put out on rocket at all so far
[1209.26 --> 1215.58]  is a blog post stating a couple technical reasons of why we built rocket all the press and all the
[1215.58 --> 1219.70]  excitement and all the hacker news threads and everything was just fallout you know that the blog
[1219.70 --> 1224.92]  post is is what stands there and if you read it from it with a technical lens you'll you'll see some
[1224.92 --> 1229.92]  you know some very specific technical issues being addressed you know this is not politics nothing
[1229.92 --> 1235.58]  we're just fixing some some technical issues and uh and all the fallout and docker's response and all
[1235.58 --> 1241.48]  that stuff was just kind of extra extra uh stuff that got away from us uh and kind of our lesson learned
[1241.48 --> 1247.62]  in all this is is uh you know people are watching people people people do are paying attention
[1247.62 --> 1252.18]  putting words in your mouth too yeah i mean nobody can put words in my mouth because it's just written
[1252.18 --> 1257.18]  on the blog post and if somebody is saying something that is not what's in the blog post then they're
[1257.18 --> 1262.68]  just i guess you know making things up so it's probably an important point to say too that we're
[1262.68 --> 1267.58]  not here to throw stones at anybody we're you know like i said before we got on this call like
[1267.58 --> 1273.58]  and everyone who listens to the changelog knows that you know open source is hard right open source is
[1273.58 --> 1279.06]  hard enough as it is without trying to call your buddy or your competitor or whomever you know to
[1279.06 --> 1284.18]  a degree opposes whatever you're building bad or not right or whatever we're not here to do anything
[1284.18 --> 1289.24]  like that whatsoever right um and i and i don't think you you definitely aren't because that's not
[1289.24 --> 1294.78]  what you wrote and that's not the point um maybe to put a timeline on what's happened like this is
[1294.78 --> 1301.88]  transposed over the last let's say i'd say 45 days december 1st was that original blog post and
[1301.88 --> 1307.40]  uh the tech crunch article that put words in your mouth like fundamentally flawed was posted later
[1307.40 --> 1314.72]  that same day so um what exactly happened inside of core west inside of the team when you released
[1314.72 --> 1321.16]  rocket put out this blog post and what was sort of the i guess the press frenzy how did that impact
[1321.16 --> 1326.84]  internally and did did anybody get how did the team react to it i guess is more or less what i'm trying
[1326.84 --> 1331.72]  to ask i'm really proud of the team and how they reacted i mean there wasn't a lot for us to do
[1331.72 --> 1336.60]  um you know we did get a lot of calls from press and such and we essentially just read the blog post
[1336.60 --> 1345.68]  back to them um but did you read the post by the way yeah exactly so so we um that that the team didn't
[1345.68 --> 1351.66]  really react or do anything there was a lot of sort of you know drama in air quotes on you know hacker
[1351.66 --> 1357.54]  news and tech crunch and things like that but the team um you know even internally us deciding to ship
[1357.54 --> 1363.06]  it um something that we had been working on for three weeks by the way um uh you know was a go
[1363.06 --> 1368.68]  no-go based in technical merit you know my the engineers are not at all they're you know hardcore
[1368.68 --> 1374.76]  open source developers and and we we don't want to create redundant efforts or or anything so we saw
[1374.76 --> 1381.14]  a clear kind of white space and that white space was you know a a tool that was secure and composable and
[1381.14 --> 1387.60]  and had an open standard um for running a container and and so we built the thing we wanted to exist
[1387.60 --> 1392.14]  um for that and the team i think is stuck by it and we're continuing to invest in it and it's coming
[1392.14 --> 1400.56]  along quite nicely actually and now a word from our sponsor top towel is the best place to work as a
[1400.56 --> 1405.22]  freelance software developer if you're freelancing right now as a software developer and you're looking
[1405.22 --> 1410.22]  for a ways to work with clients on projects that are interesting challenging and using the technologies
[1410.22 --> 1415.54]  you want to use top towel might just be the place for you working as a freelance software engineer
[1415.54 --> 1420.86]  with top towel your days of searching for high quality long-term work and getting people your
[1420.86 --> 1425.54]  worth will be over let's face it you're an awesome developer and you deserve to be compensated like
[1425.54 --> 1430.74]  one joining top top means you'll have the opportunity to travel the world as an elite freelancer
[1430.74 --> 1436.92]  on top of that top talk and help provide the support for software hardware and all the support you need
[1436.92 --> 1444.76]  to work effectively no matter where you are head to top towel.com slash developers that's t-o-p-t-a-l.com
[1444.76 --> 1451.46]  slash developers to learn more and tell them the changelog sent you so was the lack of that open
[1451.46 --> 1456.90]  standard was that kind of the crux of the matter that made you guys finally decide to do this as
[1456.90 --> 1466.46]  opposed to trying to contribute to docker or steer docker yeah i mean there's we've we've contributed
[1466.46 --> 1471.76]  and tried to steer the project you know for a while because we've been involved with the community for
[1471.76 --> 1478.66]  quite a while um and and so you know it's not that we aren't in fact i think we are steering the project
[1478.66 --> 1485.40]  the most we ever have now it's just a very heavy-handed way to do it yeah and so um i think
[1485.40 --> 1491.24]  look nobody argues with we want a more secure tool we want a more unixy tool and you follow the unix
[1491.24 --> 1495.30]  philosophy right and we want open standards and shared open standards across projects right like
[1495.30 --> 1502.70]  who doesn't want that right so so um so it's kind of a you know obvious thing to put out there and it
[1502.70 --> 1508.20]  was those three things in combination you know i wouldn't say it's any one of them again if our goal
[1508.20 --> 1514.20]  is to secure the internet and in a 1.0 product you know they don't even do signature validation yet
[1514.20 --> 1518.38]  on the thing that was downloaded it's kind of like well at some point we have to do something
[1518.38 --> 1523.90]  about that um and if you know we are building a system that we want to add containers to we're
[1523.90 --> 1529.04]  not trying to just build a you know we're not trying to help users download and run the docker
[1529.04 --> 1535.16]  platform as is we just want we want to add containers to the stuff we're building um then uh then we need
[1535.16 --> 1540.44]  the composability and the unixy kind of philosophy there and then on the standards front for me as like
[1540.44 --> 1545.78]  an open source guy it's like we have a shot at like cross cloud interoperability for the first time
[1545.78 --> 1549.62]  and it's about packaging an application in a container like we actually have a shot at it
[1549.62 --> 1557.12]  amazon and google and folks are sharing a standard around the container as a unit that is actually
[1557.12 --> 1562.74]  movable and in order for that to be actually widely adopted we need it to be written down so other tools
[1562.74 --> 1568.68]  can interop with it like and and so we just wrote it down we wrote down the ideal thing um that that we
[1568.68 --> 1574.12]  wanted and again i i believe what what this will cause over time is i hope a shared standard between
[1574.12 --> 1581.48]  rocket and docker essentially the firefox and chrome you know of of containers and and uh yeah
[1581.48 --> 1587.44]  and the firefox and chrome created a better internet it it made javascript way faster it made open
[1587.44 --> 1592.38]  standards stronger you know on all these things so even if they share a standard it's still good for
[1592.38 --> 1598.40]  for everybody if if you know multiple implementations of a standard exist it's funny the way
[1598.40 --> 1603.40]  your perspective because it reminds me jared a little bit about our call with uh tom del
[1603.40 --> 1607.34]  new huda cats with ember like they they weren't playing the short term they were playing the long
[1607.34 --> 1611.56]  term when it came to the tech they were building so completely different animals in terms of the tech
[1611.56 --> 1618.86]  but similar philosophies in the way they approached it um alex for you when whenever it said that um
[1618.86 --> 1625.28]  you're contributing back or in a more heavier hand obviously with rocket out there now um kind of
[1625.28 --> 1629.58]  guiding or steering the docker ship what is the relationship between what was the relationship
[1629.58 --> 1635.82]  i guess between core os and docker prior to and then post rocket release and how is that ship being
[1635.82 --> 1643.68]  uh steered collectively yeah i mean i hope that just the like technical stuff shines through again
[1643.68 --> 1652.16]  there's been a lot of like not non-technical focused fallouts from this um but i just hope that the
[1652.16 --> 1659.00]  technical merit shines through i think that rocket will create a better docker just in the same way
[1659.00 --> 1665.22]  that chrome created a better firefox um and and that's what i want best i just want i want containers
[1665.22 --> 1672.04]  to win and to be successful okay and and for a certain class of customers to adopt containers they they
[1672.04 --> 1677.40]  need security to be taken seriously they need to integrate it with existing environments and then
[1677.40 --> 1680.62]  they don't want to be locked in and so they want to have the ability to like build their own
[1680.62 --> 1685.50]  implementation of the thing that runs a container if they need to and so that's why we addressed you
[1685.50 --> 1690.74]  know those three things and i think containers overall are better for this in the long run and
[1690.74 --> 1696.44]  and while there is a path of like doing it by collaborating around one project we tried that
[1696.44 --> 1701.90]  around a year and a half maybe almost two years uh ineffectively to be able to guide the project in
[1701.90 --> 1707.36]  a way that that we thought mattered um and so we we just built the thing we wanted to build to solve
[1707.36 --> 1712.52]  the needs we wanted to solve you know so do you all have like collaboration do you have sort of
[1712.52 --> 1717.64]  channels open up between core os and docker to to sort of talk about the direction of containerization
[1717.64 --> 1725.02]  um you know brandon is on the docker governance board um so that's good and then you know as ceo i
[1725.02 --> 1730.82]  talked to the ceo of docker around ways to collaborate um you know but it's it's a little bit
[1730.82 --> 1736.54]  difficult given the current circumstances of how everything sort of played out but again that's
[1736.54 --> 1741.48]  just why i hope that the uh the technical merit of everything shines through and containers are
[1741.48 --> 1746.02]  better overall that's that's really what i want from this one more question for you on that note um
[1746.02 --> 1752.92]  and hopefully the way i ask it and the way you get to answer it is the best possible way i don't
[1752.92 --> 1758.50]  think it's i guess what i'm trying to ask sometimes i hem and haul over certain questions i don't want
[1758.50 --> 1763.52]  because i don't i never want to seem like we're trying to position a guest or this show in a way
[1763.52 --> 1771.94]  to throw stones and and i guess what i mean by that is is that um crap man i totally forgot my question
[1771.94 --> 1777.54]  now trying to explain it jared ask the question real quick i'll come back to it well i just i totally
[1777.54 --> 1783.70]  lost it no problem i want to just kind of uh talk about this this issue of redundant efforts versus
[1783.70 --> 1789.66]  competition and i think uh you know as engineers and developers like we're trying to squeeze like
[1789.66 --> 1794.70]  as much efficiency out of everything we do as possible and we see redundant efforts and it's like
[1794.70 --> 1801.56]  oh why you know why can't we all just work on one thing and and put all of our efforts together but
[1801.56 --> 1807.68]  um i think chrome and firefox is a great example time after time we see a competition in a marketplace
[1807.68 --> 1814.50]  whether you know uh any kind of marketplace even an open source actually just makes all the projects
[1814.50 --> 1820.56]  better and so you see the redundancy and you're like why can't we have a a single effort but
[1820.56 --> 1827.16]  historically every time we have competition amongst a diverse ecosystem like it raises the tide
[1827.16 --> 1834.62]  and everybody has to get better so so first off i in my lens of the world i see rocket and docker
[1834.62 --> 1841.36]  filling different things like docker when you think about it as a platform is much more like a mesos or
[1841.36 --> 1847.10]  cloud foundry or or something like that they use containers but they also like have all this clustering
[1847.10 --> 1853.76]  and sort of other stuff built around it okay and in my eyes rocket is just the container runtime
[1853.76 --> 1858.04]  essentially what people originally thought of docker as the thing that downloads and runs a container
[1858.04 --> 1864.92]  and that's it so the companies that will use rocket are the ones that have existing platforms like some
[1864.92 --> 1869.72]  internal environment that they want to add a container to or the platform product companies themselves
[1869.72 --> 1874.70]  these are things like cloud foundry and mesos or even you know amazon and google like that want to add a
[1874.70 --> 1880.04]  container to an existing thing they already have clustering they already have other stuff in the
[1880.04 --> 1885.98]  environment that they want to integrate with um and docker is in my eyes and just like how i see it
[1885.98 --> 1891.56]  going and this could have changed because of rocket but when we made these decisions um the way it was
[1891.56 --> 1896.24]  going is more of a soup to nuts platform in and of itself something you could take off the shelf to run
[1896.24 --> 1901.86]  your infrastructure which is meant for companies that want like they need in a platform of some sort
[1901.86 --> 1906.18]  to run which is fine and again a lot of companies need that so it makes a lot of sense okay
[1906.18 --> 1911.26]  but the container piece that we want is to have containers interoperable between a bunch of
[1911.26 --> 1914.92]  different platforms you know not just have like there's the one container thing and the one
[1914.92 --> 1920.18]  container thing you can do with it um and so that's the i i guess my point in this is i see them as
[1920.18 --> 1926.46]  actually distinctly different things um you know the firefox and chrome analogy i think applies for like
[1926.46 --> 1930.96]  let's just step up security on the way that you download an image and validate it before you run it
[1930.96 --> 1937.16]  um and so on and and those things apply but but rocket is a component docker is a product
[1937.16 --> 1942.96]  and that's like the core kind of difference is aren't there two pieces i mean isn't docker
[1942.96 --> 1950.02]  um both isn't there still that idea of a container and yet then there's services around it it seems like
[1950.02 --> 1957.96]  in my mind i see the two and maybe they're merging or becoming one um do you see it as just the
[1957.96 --> 1964.80]  platform there's no such thing as a docker uh single container that can be used there's the
[1964.80 --> 1972.08]  docker single container in there but it's it's a again there's a component in there so like the way
[1972.08 --> 1978.30]  we can get technical right it's okay to kind of get into the weeds a little bit okay so the way that
[1978.30 --> 1985.04]  docker is architected today is there's a central daemon that runs on every server okay running is root on
[1985.04 --> 1990.86]  your server and then when you type docker run it's actually an http client talking to this this daemon
[1990.86 --> 1996.02]  locally over http or the daemon can be remote too and that's one of the like more clever things of
[1996.02 --> 2001.76]  docker is you can easily like have your osx go binary push over to a docker daemon that's on a
[2001.76 --> 2006.90]  remote host or on a virtual machine on your laptop okay so that's clever and that's nice from a
[2006.90 --> 2011.90]  ease of use perspective but the problem is is when you have a daemon running as root on your server
[2011.90 --> 2017.72]  that one has an http interface like i think again sysadmin 101 here is do we run our web servers
[2017.72 --> 2023.42]  as root on a server you know like no okay and then the second piece is anything that talks to the
[2023.42 --> 2027.80]  internet should we run that as root so something that like downloads an image and runs and you know
[2027.80 --> 2032.00]  downloads an image or uploads an image so that thing be running as root no and kind of the whole
[2032.00 --> 2036.10]  architecture of the way docker is built is around the central daemon that kind of has all the
[2036.10 --> 2041.02]  functions of docker in it so yes part of that daemon that's running has something that
[2041.02 --> 2048.42]  the downloads and or that runs a container and that's great um we just being like unix guys that
[2048.42 --> 2053.04]  care about security need it to be refactored such that those are individual actual applications
[2053.04 --> 2058.34]  that run so we can invoke them with like different privileges and different users uh to get the
[2058.34 --> 2063.78]  security model more correct okay and and uh and to do that you'd effectively have to rewrite docker
[2063.78 --> 2068.86]  because you have to break apart this whole http client to like daemon thing um that's going on
[2068.86 --> 2074.56]  uh and so that's that's why we're like hey let's just start from from scratch uh because it it's
[2074.56 --> 2078.92]  just it's actually like the model is totally different in our world what you would do if you
[2078.92 --> 2084.72]  wanted an http interface is you'd write a little service that's like a http kind of uh it's an
[2084.72 --> 2091.38]  alternative to ssh on your server that speaks http uh and json and when you hit that it probably talks
[2091.38 --> 2098.16]  to like d bus and tell systemd the init system to invoke a container and run it um or if you want it
[2098.16 --> 2102.56]  to download an image it would tell systemd to to download you know to run a process as an
[2102.56 --> 2107.68]  unprivileged user uh and and download an image maybe it just uses curl to download you know it doesn't
[2107.68 --> 2113.78]  need to have a fancy go binary something you know it it's like your composability is what is the way we
[2113.78 --> 2119.44]  architected rocket to be so you can use it to build systems but anyway yes if docker was for instance
[2119.44 --> 2125.72]  to clean up their security issues refactor docker into a bunch of individual components that could
[2125.72 --> 2131.20]  be used differently and then have an open standard that was interoperable with projects outside of
[2131.20 --> 2136.22]  docker itself well now it starts to become a lot more like chrome and firefox because they're you
[2136.22 --> 2142.06]  know they're they're roughly the same uh then in that case yeah and hopefully you know bringing up
[2142.06 --> 2147.68]  issues uh like you are here allows them to uh bring those problems to light and then address them
[2147.68 --> 2151.88]  uh in their software right and i think they got the message loud and clear with rocket and we've
[2151.88 --> 2157.24]  seen them um like kind of start going down the right path and again what we feel is the right path
[2157.24 --> 2163.54]  is all just an objective you know opinion right um but the um you know they i think they're they're
[2163.54 --> 2168.04]  going down the path of making it more composable and really fixing their security thing and i i do find
[2168.04 --> 2174.70]  it unfortunate that like we weren't able to do this sort of as a as an effort together we you know that's not
[2174.70 --> 2179.00]  without trying it's not like we never tried we tried for you know multiple years actually and
[2179.00 --> 2183.36]  then eventually decided well we just need to go our own way to get it get it the way we need it which
[2183.36 --> 2189.82]  you know i think um i think is also a very hacker way to go yeah well in the hacker world we would we
[2189.82 --> 2195.34]  would tend to fork but it sounds like forking in itself was another decision you guys didn't want to
[2195.34 --> 2201.40]  make again because the model is so yeah different we would have had to essentially rewrite the fork
[2201.40 --> 2206.24]  at which point it's like uh but i just write a new thing and might as well get some of the
[2206.24 --> 2212.72]  security primitives right because that's also pretty core to the architecture too um so we just we we
[2212.72 --> 2217.74]  built it like from scratch because it was easier than forking gotcha i guess it's kind of where my
[2217.74 --> 2224.22]  question that i lost by the way uh on there was more like you know docker was is sort of synonymous
[2224.22 --> 2229.90]  with containerization they sort of you know coined the term or coined the name not so much the term but
[2229.90 --> 2236.16]  you know kind of made it popular they popularized it for sure right and and so you've got this you
[2236.16 --> 2242.08]  know non-standard way to make a container and core west sort of being built around this container
[2242.08 --> 2247.64]  world you know not running anything that's not a container basically um and i was just wondering
[2247.64 --> 2254.26]  i guess what your thoughts were and this may be sort of awkwardly placed in the conversation but
[2254.26 --> 2259.40]  what your thoughts were on their change of business model when they went from doc cloud
[2259.40 --> 2265.62]  to docker and sort of built their new business model around it whereas with core os you know you
[2265.62 --> 2271.38]  started off with the idea of how you were going to build core os from a monetization standpoint how
[2271.38 --> 2276.02]  you were actually going to build a company around it and as you mentioned before providing you know
[2276.02 --> 2280.78]  free update services and community service as part of your business model like sort of buffered in
[2280.78 --> 2285.14]  what what the difference was their model versus the way you went and how that might have could have
[2285.14 --> 2292.98]  played differently to to containers as a whole i'm really not sure how to answer that i mean their
[2292.98 --> 2296.76]  business model is their business model i don't think it's even that's why i had a hard time phrasing
[2296.76 --> 2301.36]  the question yeah i don't think i don't think it's played out yet on what their business model is it's not
[2301.36 --> 2307.88]  that clear right now it appears to be kind of a github like thing for hosting containers um i assume
[2307.88 --> 2313.44]  there'll be more um you know down the road on that um so i don't know i can't really comment on their
[2313.44 --> 2319.54]  business model all i know is the way like our company wants to build open source software is we want to
[2319.54 --> 2324.42]  build open source components that are freely reusable and that helps companies sort of run their
[2324.42 --> 2329.14]  infrastructure in this this new way and that we intend to build commercial products that take advantage
[2329.14 --> 2334.02]  of this transition to this new way of running infrastructure and help companies get there faster by buying our
[2334.02 --> 2342.42]  commercial solutions so let's change focus over to this uh app container specification um this is
[2342.42 --> 2348.48]  seems like a call to arms uh for the community anybody who's interested and invested into containers
[2348.48 --> 2357.02]  and rocket of course is the command line tool that implements um the specification can you speak more
[2357.02 --> 2363.26]  about specification what's in there what's not in there um who owns it that kind of stuff app container
[2363.26 --> 2369.52]  is an awesome piece of tech if if you're into in all this container stuff and want to get really
[2369.52 --> 2374.14]  nerdy with it definitely go read the specification it's really cool it's a really really cool piece
[2374.14 --> 2380.60]  of tech um and uh and so what we did is we talked to kind of everybody that's in the container space
[2380.60 --> 2385.46]  and got their feedback on what would be ideal and then brandon who's a very talented engineer you know
[2385.46 --> 2392.00]  spent a lot of time refining it um but there's three components to it there's an image format
[2392.00 --> 2398.18]  itself which is essentially a gpg signed tarball with some metadata i mean simplifying it but but
[2398.18 --> 2404.28]  that's that's what it is um and then there's a the the runtime itself so you can't just define the
[2404.28 --> 2409.04]  image you have to define the environment that the image runs in uh in order to have real you know
[2409.04 --> 2414.88]  consistency and portability um some of the things that i think are really cool in the in the runtime
[2414.88 --> 2420.66]  are um you know one problem with containers is how do you give them state like to start up how do you
[2420.66 --> 2424.20]  essentially give your containers arguments and there's kind of three different ways to do that
[2424.20 --> 2428.78]  there's environment variables or a config drive where you like have a directory that has config
[2428.78 --> 2435.30]  variables written down to disk or the the third way is a metadata service and that's what like amazon
[2435.30 --> 2441.06]  and and kind of the cloud providers use app containers runtime specifies a metadata service
[2441.06 --> 2447.14]  um for for doing that which is again how the cloud providers kind of done it and then the thing
[2447.14 --> 2452.70]  where we moved everybody forward that no cloud has done at all today is we give every uh every
[2452.70 --> 2457.84]  container that runs an identity uh which means on the metadata service there's an endpoint that you
[2457.84 --> 2463.02]  can post data to and get a signed version back so it's like every container has a little mini hsm
[2463.02 --> 2468.46]  uh built into it um and again from a security perspective the key to good security is giving
[2468.46 --> 2474.10]  everything running in your environment a strong cryptographic identity um and and just like etcd we want to
[2474.10 --> 2480.48]  make these more complicated topics easy you know we we essentially built a tiny little hsm into the
[2480.48 --> 2485.14]  metadata service uh for the runtime and things like this it's like yes let's just move state-of-the-art
[2485.14 --> 2492.54]  forward um and help people more easily build secure systems um so there's the image format the runtime and
[2492.54 --> 2498.98]  then the image discovery specification so one of the novel things of docker is how tightly integrated
[2498.98 --> 2505.10]  it is with the hub which is the place where you host and share your docker containers um and that's a
[2505.10 --> 2513.76]  docker inc ran service the way we did the um the image discovery and download for a rocket and an app
[2513.76 --> 2519.64]  container is it borrow some concepts from the go programming language where essentially you can
[2519.64 --> 2527.86]  federate it across the dns namespace um where the image is hosted so if i went if i said rocket run
[2527.86 --> 2536.58]  coreos.com slash etcd there's a convention for for discovering using dns um how how to find and
[2536.58 --> 2542.58]  download and run that um that uh image which means it's truly distributed and federated because you
[2542.58 --> 2548.20]  know everybody can do dns however they want um and that that we think is also a pretty kind of
[2548.20 --> 2553.62]  clever novel piece of tech in there um borrowed from the from the go world so definitely check it out
[2553.62 --> 2559.46]  if if you haven't already um and you're interested in these sorts of things and now a word from our
[2559.46 --> 2567.10]  sponsor rack space rack space rack space you know i thought about actually saying nothing but rack space
[2567.10 --> 2572.08]  for the whole spot but i didn't think that would be cool and i don't think you would either and when i
[2572.08 --> 2577.16]  told rack space about it they were like nah you can't do that but what they did want me to do is tell
[2577.16 --> 2581.22]  you about how much they love open source and how much they appreciate you listening to the change log
[2581.22 --> 2586.44]  and they want to give you and everyone else who wants it fifty dollars a month in credit for 12
[2586.44 --> 2591.76]  months to explore their open cloud all you need is a free developer plus account to get started
[2591.76 --> 2595.96]  go to the change law.com slash rack space and enjoy the open cloud
[2595.96 --> 2604.10]  i really like that identity piece i've i've enjoyed that uh and go as well i think that's a great addition
[2604.10 --> 2610.64]  to containers um what's the state of the specification is it like pretty much written are you looking for
[2610.64 --> 2618.72]  feedback um how do people get involved so right now we are we're between a so the very first thing
[2618.72 --> 2624.02]  we released was a 0.1.0 which is like essentially prototype here's ideas we wanted to put enough
[2624.02 --> 2629.02]  rails on it that like the conversation you know could move forward but we didn't want to define
[2629.02 --> 2637.80]  everything i think we cut yesterday 0.2.0 which is it's getting pretty good um but still moving um and
[2637.80 --> 2642.78]  we've been keeping rocket kind of in track of the spec the whole time so we we are forced to think
[2642.78 --> 2650.04]  through the spec with an implementation um and then our next major one is around a kind of we think
[2650.04 --> 2655.88]  it's good so i'll you know outside implementations like go for it let's start doing the interoperability
[2655.88 --> 2661.44]  thing folks that want to help kind of show that the standard works and then once we have a number of
[2661.44 --> 2666.92]  sort of outside implementations then we'll call it 1.0 because that should just prove that the
[2666.92 --> 2672.12]  the spec is pretty solid if we're able to get outside folks to contribute to it and and uh and
[2672.12 --> 2676.86]  build their own things and we're starting to see it happen uh you know there was a c++ version that
[2676.86 --> 2682.30]  was released of the app container spec um there's another one i can't recall off the top of my head
[2682.30 --> 2688.08]  um but even that before we have a stable spec is pretty solid you know for a project that has been
[2688.08 --> 2694.86]  out for about 45 days minus like 15 days of holidays in the middle there you know um so it's it's moving
[2694.86 --> 2701.42]  moving along pretty quickly so no doubt you're eventually want to get rocket um in involved in
[2701.42 --> 2707.14]  the core os product uh got a timeline on on that transition and will you continue to support docker
[2707.14 --> 2713.02]  into the future so we'll definitely continue to support docker the rocket timeline depends on
[2713.02 --> 2720.52]  how quickly rocket is production ready um and and so um you know it's a little bit tbd just because
[2720.52 --> 2726.16]  we know like we don't even try to set timelines on our open source projects it's just kind of like
[2726.16 --> 2733.22]  when it's ready it's ready um so uh it'll take a little bit of time to get 1.0 but um but it's moving
[2733.22 --> 2740.20]  along very quickly we will you know at some point have a core os with rocket in it how those all
[2740.20 --> 2745.30]  kind of play together uh you know we haven't really talked too much about i will say though
[2745.30 --> 2751.30]  the original motivation of rocket and our use of containers is to treat it like a package manager
[2751.30 --> 2756.18]  but our packages are different in that our packages are always up to date for you so you
[2756.18 --> 2762.06]  could imagine building a package manager hint hint wink wink that also does auto updating you know
[2762.06 --> 2767.74]  and and that's something that we would want to do for the docker platform itself you know as they
[2767.74 --> 2773.20]  ship new features like constantly and ship uh you know security fixes and everything we would love to
[2773.20 --> 2778.54]  deliver those extremely quickly to the user as an entire platform not just as treating it as our
[2778.54 --> 2783.46]  package manager you know just like how we would love to help the mesos community run mesos on top of
[2783.46 --> 2788.42]  core os um but to do that we would package it you know we would package those things we wouldn't make
[2788.42 --> 2794.68]  it the primitive on core os for how you download and run the package if that makes sense yeah
[2794.68 --> 2802.00]  cool sounds really cool um let me ask you this say i'm interested in core os because actually i am
[2802.00 --> 2810.08]  kind of interested in core os say i am uh hypothetically um can it run pretty much anywhere
[2810.08 --> 2816.14]  these days like amazon digital ocean is it just like any other linux distro that i can go install
[2816.14 --> 2825.70]  onto a vps yep so we're on amazon digital ocean google open stack eucalyptus you know um on-prem
[2825.70 --> 2834.16]  bare metal iso usb stick like vmware you name it um and you can run core os there um and the really
[2834.16 --> 2842.52]  cool thing about core os is we when we when you run us on a bare metal server or you run us on a cloud
[2842.52 --> 2848.80]  server the root file system is bit for bit identical we can pass a signature validation
[2848.80 --> 2854.58]  on the on the entire root block device uh that says they're cryptographically identical which is
[2854.58 --> 2860.60]  great from a security perspective like forget about ids it just doesn't matter anymore um and it's also
[2860.60 --> 2865.58]  great from if you're at you know a developer and you want to target a consistent platform in different
[2865.58 --> 2872.02]  environments we are we are 100 consistent so if you want to use abuntu on digital ocean and
[2872.02 --> 2876.46]  amazon that's cool you can do that and they're pretty close but they're not like bit for bit
[2876.46 --> 2881.26]  identical which is a kind of a requirement if you want actual portability uh between these things
[2881.26 --> 2886.92]  um and so we we put a big emphasis on on core os to really nail some of these things home as we
[2886.92 --> 2889.72]  as we get distributed across all the different cloud environments
[2889.72 --> 2899.16]  i guess uh one closing question before we tail off to our super awesome end of show questions um
[2899.16 --> 2904.44]  what what role does does quay play into if that's the way you said canadians say it k
[2904.44 --> 2911.42]  maybe the french canadians key um what role does that play i guess into the future of core os and
[2911.42 --> 2917.74]  uh this this open standard for the app container sure so first that's a great example of our commercial
[2917.74 --> 2923.76]  offerings you could go and use an open source docker registry or you could use docker's hosted registry
[2923.76 --> 2932.58]  um but we build a enterprise ready on-prem version of docker registry um that companies can go and buy
[2932.58 --> 2936.76]  if they don't want to piece it together themselves and there's no alternative to that right now on the
[2936.76 --> 2942.86]  market we have a complete monopoly on an on-prem kind of commercial ready version of of um of a docker
[2942.86 --> 2948.68]  registry um so that's a perfect example of it's like hey you could go replace it with open source by
[2948.68 --> 2952.62]  your teams piecing it together if they want or you could buy it off the shelf from us and you choose
[2952.62 --> 2958.02]  and it incentivizes us to be interoperable with standards but also just do a great job of piecing
[2958.02 --> 2963.42]  those things together for our customers now features of quay that we might add as they relate
[2963.42 --> 2967.22]  to rocket and app container i think it's only natural to assume that we will support app container
[2967.22 --> 2972.44]  and um docker you know just like all these other projects that are trying to target app container
[2972.44 --> 2976.92]  it's moving right now so so we can't just ship it overnight we have to like get the spec firmed up
[2976.92 --> 2982.08]  before we can have our tools support it as well um so that i think will only be another value prop
[2982.08 --> 2987.86]  of of uh enterprise registry is you could choose the best container technology for you if you want
[2987.86 --> 2995.10]  if you want the one that docker has put together that's fine if you want um you know ours uh you
[2995.10 --> 2998.72]  could do it and we'll make sure they're all interoperable um and you can kind of choose which
[2998.72 --> 3005.20]  one is best best tool for the job and having core os power all that's got to help the development team
[3005.20 --> 3013.26]  sort of bug fix across the spectrum too exactly exactly well um alex it's definitely been fun
[3013.26 --> 3021.04]  talking about uh app containers the standard uh rocket docker core os uh i think jared's excited
[3021.04 --> 3029.42]  about it i've uh those who know the show well know i'm a front-end designer person who plays hacker
[3029.42 --> 3034.92]  for fun on the radio as win used to say when he was co-host of the show he used to say that a lot
[3034.92 --> 3039.70]  so it's kind of funny but i've actually done several server builds over the last couple years
[3039.70 --> 3045.46]  and i've gotten more and more into my dev ops space but uh if jared's excited about core os i'm
[3045.46 --> 3049.96]  excited about core os i hope it i hope you're excited about it because you don't want to care
[3049.96 --> 3054.90]  about it i want you to say like i want to use core os because i don't ever want to have to worry
[3054.90 --> 3058.80]  about a security patch i'll just let the core os guys take care of it for me because i think they
[3058.80 --> 3063.10]  can do a better job than i see and that's exactly probably what you want right that's exactly what
[3063.10 --> 3068.82]  exactly when harpley was around i was like oh man what do i gotta do and i'm not obviously as the
[3068.82 --> 3075.88]  non-devops non-server builder person but does it part-time when he needs to sort of person um i was
[3075.88 --> 3080.50]  thinking what the heck do i do i don't even know what the problem is exactly at the moment and then
[3080.50 --> 3085.26]  you know i'm sort of playing ketchup because i'm less in the fringes on that stuff and you know while
[3085.26 --> 3090.44]  we pay attention to open source and keep our finger on the pulse open source is big technology is big
[3090.44 --> 3095.58]  you can't you know grasp it all and you know i was like what the heck do i gotta do and it would
[3095.58 --> 3100.68]  have been nice to have a core os like thing where i can trust that you're going to auto update it on
[3100.68 --> 3105.50]  my behalf with security but then you do have the fear side which jared pointed out earlier so you
[3105.50 --> 3110.36]  sort of have this double-edged sword that so long as you keep doing your job right on security and
[3110.36 --> 3114.28]  non-breaking i guess the containers sort of take care of that right well i can tell you what i did
[3114.28 --> 3119.86]  on heart bleed is i went out and patched double-digit servers for my customers spent the whole day
[3119.86 --> 3126.22]  patching servers so i could definitely uh get on board with somebody else pushing those security
[3126.22 --> 3131.34]  patches onto my os that would be awesome we patched tens of thousands or hundreds of thousands of
[3131.34 --> 3138.26]  servers is it like the uh the u2 song for apple you you push it out to five million or 50 million
[3138.26 --> 3144.18]  or 100 million people at once that's right right into their into their music right exactly our users
[3144.18 --> 3150.60]  opted into it i was gonna say that backfired a little bit that did um well alex we have a couple
[3150.60 --> 3155.98]  questions we'd like to close with i know that uh kelly probably helped out by uh feeding those
[3155.98 --> 3162.88]  questions to you um jared which which one should we ask we ask them all we got a few minutes we got
[3162.88 --> 3167.86]  some time we got to do programming hero yeah okay so let's start there who's your programming hero
[3167.86 --> 3173.44]  uh that's a great question um you know there's a number of them i think the one that takes the
[3173.44 --> 3182.00]  hat though is john gilmore do you guys know john gilmore i do not so john um the early unix guy um he
[3182.00 --> 3190.46]  did the original public domain implementation of of tar um he also founded a group of cypherpunks he was
[3190.46 --> 3197.28]  the oh yeah the electronic frontier foundation uh one of the coolest moments um i met him really
[3197.28 --> 3202.56]  early in my career when i was in high school actually a mentor of mine in high school um said
[3202.56 --> 3207.42]  hey you should write a paper on the digital millennium copyright act uh that would be a
[3207.42 --> 3212.06]  great senior paper to write and i'm like okay having no clue what that was about and then my friend was
[3212.06 --> 3217.76]  like and i have a buddy coming over that can help review it for you i'm like okay so i write i write a
[3217.76 --> 3222.44]  paper on the digital millennium copyright i could john gilmore founder of the eff reviews my senior
[3222.44 --> 3230.26]  paper on the dfca it's like uh and then what do you have to say about it i mean the the conversation
[3230.26 --> 3234.82]  was fine i mean i was so green and had no idea about any of this stuff uh i didn't even know like
[3234.82 --> 3240.44]  yeah you know this was pre-mozilla and pre-everything um and you know i think it was just a nice you know
[3240.44 --> 3246.20]  conversation he wasn't too hard on me um but it uh that he definitely has a lot of respect of mine
[3246.20 --> 3251.14]  because of his stance on you know online civil liberties as well as um you know he's directly
[3251.14 --> 3255.98]  contributed to really core technology in the unix world you know tar it doesn't get much better
[3255.98 --> 3265.38]  than that right um so i would have to say john gilmore awesome well um for core os the app
[3265.38 --> 3271.46]  apps uh the uh app container standard uh anything that you're working on what is a call to arms what
[3271.46 --> 3276.90]  is a way that the listeners of the show they're either professional open source developers enthusiasts
[3276.90 --> 3282.84]  hackers whatever you want to call them um you know how can they step in where could you best use
[3282.84 --> 3289.12]  um the help i guess from from the listeners of the show and the crowd that uh collects around open
[3289.12 --> 3295.24]  source sure i mean i'd say overall it's like hey all of this from the core os perspective is about our
[3295.24 --> 3300.16]  goal to secure the internet uh and so there are a number of different ways you can contribute to that
[3300.16 --> 3305.30]  one key part of that that's very timely right now is about application interoperability
[3305.30 --> 3311.68]  between platforms and that's app container and rocket we could use help on rocket itself as a
[3311.68 --> 3317.42]  tool but also and more importantly we need third-party implementations of app container to exist in
[3317.42 --> 3322.16]  different languages um so that means let's say you're running uh existing configuration management
[3322.16 --> 3327.26]  system and and you want that to output a container instead of you know manipulate a running host that
[3327.26 --> 3331.46]  would be a great way to to like build an app container image or maybe you are working with
[3331.46 --> 3337.22]  a language specific stuff you're a node.js guy we should be able to build tools that that in the
[3337.22 --> 3343.36]  native node.js tool set output a container image um to allow portability um you know and and things
[3343.36 --> 3349.04]  like that so i would say today we use the most help on is is our third-party implementations of
[3349.04 --> 3354.62]  of the specification to know that we truly have built an interoperable spec that works well for people
[3354.62 --> 3360.48]  um and the spec is just getting to the point right now where we're about ready for that um so i would
[3360.48 --> 3364.44]  say that's the most timely one but hey if you're up for securing the internet we got systems
[3364.44 --> 3369.50]  programming for you with the operating system we have rocket container stuff we have etcd distributed
[3369.50 --> 3373.50]  database i mean all of these things are components toward this bigger vision and we can use help on
[3373.50 --> 3380.16]  all fronts any chance you got a link to third-party spec for what you mentioned there um yeah sharing
[3380.16 --> 3388.82]  the show notes it's on yeah it's github slash app c a p p c uh for app container so uh okay github slash app c
[3388.82 --> 3393.30]  we'll uh we'll trudge through there and figure out where it's at and throw the link in the show
[3393.30 --> 3399.30]  so if you're listening check out the show notes for that link um and i guess the the last question
[3399.30 --> 3405.20]  is kind of fun since we do have uh we do have oh we're past time 21 seconds i'm just kidding um
[3405.20 --> 3410.12]  the last question is sort of fun so have fun with this one what would you be doing if you weren't
[3410.12 --> 3416.78]  doing x and that x being whatever you're doing now so right now you are a ceo of of uh core os and
[3416.78 --> 3421.68]  what you're doing now but if you weren't doing that what would you be doing well the short answer
[3421.68 --> 3427.30]  is what i'm doing a lot of ceo core os is not able to actually hack on the products directly and
[3427.30 --> 3431.34]  doing a lot of other things and so i would not be doing those other things and just working on the
[3431.34 --> 3436.28]  product um but that's the more short-term thing i think overall you know i spent a lot of time
[3436.28 --> 3441.82]  after rack space and the acquisition trying to figure out what to what to work on next and this
[3441.82 --> 3446.42]  mission and what we're on right now is where we ended up and i couldn't be happier than than what
[3446.42 --> 3450.78]  we're doing right now in the work that that this team is doing so i'm right where i want to be which
[3450.78 --> 3456.24]  is you know that makes us pretty defensible towards ever being like you know acquired or being killed
[3456.24 --> 3460.46]  or something because we're building the exact things we we want to build and getting good traction
[3460.46 --> 3465.72]  on it um so really happy but in in the micro sense i would i would die if i could work a little bit
[3465.72 --> 3470.92]  more on the actual products and tech and red code and that kind of stuff uh because that's really what i
[3470.92 --> 3479.08]  really what i love any fun hobbies come to mind that aren't exactly job or tech related um yeah i
[3479.08 --> 3484.52]  there's kind of we've gotten windsurfing and things like that in the past by the way yeah i have these
[3484.52 --> 3490.30]  uh these little inflatable kayaks that i take out everywhere um and so they're these little
[3490.30 --> 3496.18]  kayaks they're actually for like white water rafting in alaska when you need to hike up a big you
[3496.18 --> 3500.70]  know you're hiking somewhere that requires a river crossing um and i take those things out
[3500.70 --> 3505.14]  uh even last night i was out on the bay uh with my little kayaks but they're so small you can put
[3505.14 --> 3508.82]  them uh like in your carry-on luggage and just take them with you wherever you want to go
[3508.82 --> 3513.88]  uh so i really uh i have fun playing out in the water and those things you know on the surf or out
[3513.88 --> 3519.86]  in lakes or in rivers and that kind of stuff so i don't know i enjoy the outdoors yeah well good deal
[3519.86 --> 3525.36]  alex again thanks uh for coming on and kelly in the background i know you're still there thank you for
[3525.36 --> 3532.46]  making this uh time possible for alex um i also want to thank we mentioned rackspace already as one
[3532.46 --> 3537.56]  of the sponsors for this show but we got two other sponsors fantastic sponsors by the way code ship
[3537.56 --> 3544.02]  top towel people have emailed me and said they cannot understand when i say top towel i can't help it i'm
[3544.02 --> 3551.60]  sorry their business is called top towel t-o-p-t-a-l i'm assuming they they named the business name
[3551.60 --> 3558.76]  short after top talent so uh t-o-p-t-a-l.com by the way if you're that person or those several people
[3558.76 --> 3565.46]  who have emailed me and said dude what are you saying um that's what i'm saying top top um and
[3565.46 --> 3569.52]  still it's it's still unrecognizable and of course rackspace we thank them for
[3569.52 --> 3576.86]  uh their support for uh for this show and whatnot so let's uh let's say goodbye fellas great show
[3576.86 --> 3578.94]  goodbye all right thanks bye
[3599.52 --> 3600.02]  you
