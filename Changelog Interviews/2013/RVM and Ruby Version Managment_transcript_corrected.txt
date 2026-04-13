[0.00 → 13.50] welcome back everyone this is the changelog where our member supported blog and podcast
[13.50 → 17.78] that covers all fresh and what's new in open source you can check out the blog at the changelog.com
[17.78 → 23.46] our past shows at 5by5.tv slash changelog and something new you can subscribe to the changelog
[23.46 → 28.40] weekly our weekly email covering everything that hits our radar in open source you can subscribe
[28.40 → 33.36] at the changelog.com slash weekly this show is hosted by myself and our co-host today
[33.36 → 39.68] our managing editor as a matter of fact is jarred Santa jarred say hello hey how you're doing good to
[39.68 → 44.54] have you on the show my friends here yeah it's uh yeah I think the last time you were on the show
[44.54 → 50.20] was the very first live show roundup when we kind of came back from our hiatus yeah that's right
[50.20 → 54.64] that was a fun show that was a fun show we have to do more of those so if you're a fan of that show
[54.64 → 59.98] give us a shout on Twitter we like that but uh this is episode number one zero two one oh two
[59.98 → 65.70] and we're joined by Michael Paris he's the maintainer of RVM, and he's also the release manager
[65.70 → 71.52] for RVM at engine art so Michael welcome to the show my friend hello everybody from Poland
[71.52 → 76.08] you are from yeah you're from Poland aren't you what's how do you pronounce your city name
[76.08 → 86.26] oh no it's uh good, but it's tiny city so uh it's more close to Berlin if anybody looks
[86.26 → 91.42] on the map gotcha yeah I did look on the map I was like where's he at so it's uh because you know
[91.42 → 98.22] us westerners right here in the U.S. we tend to be oblivious to this thing called a map and uh
[98.22 → 102.72] and we sometimes forget our geography, and you have to look it up I mean even if even Poland like I've
[102.72 → 109.18] got you know my last name right my last name is Kodiak and so my uh my grandfather and a lot of
[109.18 → 113.40] my uh you know my lineage comes from that area so you'd think I'd be a bit more familiar and if you
[113.40 → 120.88] ask me if I speak Russian or Poland I'd say no it's its quite easy yeah uh before we kick off the
[120.88 → 127.64] show I want to give a shout-out to our sponsor app sketchbook um if you do uh if you do any sort of
[127.64 → 132.50] app design which I imagine a lot of our audience do I don't know about you but whenever I have an idea
[132.50 → 137.78] I have to get it on paper before it comes to life and that's exactly what app sketchbook lets you do
[137.78 → 144.12] they make sketchbooks for designers and developers so you can get your interface ideas onto paper before
[144.12 → 151.00] actually designing your next idea they're available in UX responsive iPhone and iPad blueprints they're
[151.00 → 155.14] on every page so if you're designing an iPhone app obviously you want to kind of sketch against that
[155.14 → 158.34] or even collaborate with one of your designers to kind of get some of your ideas out
[158.34 → 165.72] um you can go to app sketchbook.com the coupon code to use is Dan sent me that's Dan sent me to
[165.72 → 170.22] get five dollars off your next order this will be in the show notes so head to five by five dot TV
[170.22 → 175.74] slash changelog slash 102 which is this episode number two learn more and click through to app
[175.74 → 181.26] sketchbook.com but lets uh let's learn a bit more about Michael so Michael you're the took over
[181.26 → 189.82] uh I guess the helm of Rb RVM not long ago about uh almost two years ago I bet now yeah, yeah so it's
[189.82 → 199.66] uh almost two and a half years since I started contributing to RVM and I guess the first
[199.66 → 209.48] bigger time with RVM was during summer when went for vacation with kids and needed some time off
[209.48 → 219.34] and I proposed to do the maintenance and keeping users uh up to date with everything
[219.34 → 227.82] what's going on so uh so yeah it's two years now what was your experience I guess before uh before
[227.82 → 233.22] that uh that time period like what got you into even hacking or even making some suggestions to
[233.22 → 238.50] uh to wane on uh the the the creator of maintainer original maintainer of RVM
[238.50 → 247.50] uh yes so i I've started uh I needed RVM for my work I was installing servers, and it was really a
[247.50 → 257.10] pain and uh i I tried RVM, and it was quite easy uh but I found some patches were missing for
[257.10 → 265.08] ruby enterprise edition or ruby 187 I don't remember exactly, but it was the old one so I've added the
[265.08 → 271.46] patches and that that was my first contribution and from that I really fast started to contribute to
[271.46 → 281.38] RVM and a few months it was like March and during the summer July already was contributing almost
[281.38 → 289.14] full-time nice how mature was it at that point was it at 1.0 back than already, or it's uh I've started
[289.14 → 302.76] at 1.2 and when the summer it was like 1.5 1.6 1.6 yes it was 1.6 during the summer so i I become
[302.76 → 311.36] real-time contributor and during the 1.6 you mentioned you were doing it for your work where
[311.36 → 314.72] and I think before the call actually kicked off before we actually started recording
[314.72 → 320.22] uh you kind of mentioned that it was you're starting to work with RVM and maintaining it
[320.22 → 324.56] I'm not sure if that coincided exactly the same time you started engineering is that who you were
[324.56 → 329.78] working with and why you needed to kind of hit the lower levels and kind of hit these break
[329.78 → 338.72] points at patch levels and as you mentioned ruby enterprise edition so i was needing
[338.72 → 346.46] RVM for my work and I really liked the code and what it does so it was something what i always
[346.46 → 354.76] wanted to do some open source contribute make people happy and during my work time and my free
[354.76 → 363.84] time I started to contribute a lot and I basically spent almost all my free time contributing to RVM
[363.84 → 373.74] and at one point i I got exhausted of my day job so i and I found a chance with Wayne to do some
[373.74 → 384.38] small Wayne the original author of RVM I found some more time to do projects with Wayne and I quit
[384.38 → 391.98] my job to take care of RVM and to do the smaller projects which allowed me to work even more on RVM
[391.98 → 398.54] wow so was uh when you said you quit your job were you being compensated by RVM because I know that
[398.54 → 403.04] RMS had a pledge on their home page for a while and I think they've maybe raised twenty thousand
[403.04 → 410.34] dollars is which probably doesn't pay the bills but um were you unemployed getting paid what was the
[410.34 → 420.38] scenario there yes so uh at this time it was uh a lot of uh contributions thanks to
[420.38 → 431.34] Ryan bates who started action let's let's show when some appreciation for RVM uh because of the
[431.34 → 441.58] uh bad comments from RVM and uh then thanks to from to the contributions Wayne had uh quite
[441.58 → 449.80] quite a good funding for short time which allowed him to fund me uh to do the job for
[449.80 → 458.14] minimal money, but it was really something refreshing for me to just quit all the standard tasks and
[458.14 → 466.04] uh do the good job to community so that that's interesting I didn't know so besides Ryan who else
[466.04 → 475.18] was uh was Ryan the main benefactor of some of that injection or was it others no so actually it's it
[475.18 → 482.86] wasn't just Ryan he only started the action he just asked on Twitter people to contribute and
[482.86 → 490.58] I think it was like two-thirds of the twenty thousand was contributed in really short time like
[490.58 → 496.30] two months or three months jarred I know you're a bit closer to the maybe the drama I guess between
[496.30 → 502.86] RBM and RVM and I guess even cherub if is that uh comes into play in this conversation you want to
[502.86 → 508.86] speak to some of those some of that uh time frame sure I mean I wasn't too close to it, you know I read
[508.86 → 514.14] some of the blog posts but I wasn't I'm sure Michael was intimately involved in that situation and
[514.14 → 521.86] and uh mostly i I was aware of it because um as a RVM user and by the way thank you for all the
[521.86 → 530.44] work you've done long time RVM user and uh saved me a lot of time in my work but I felt the pain of
[530.44 → 538.16] the uh of the r of RVM basically overriding the CD function and your shell uh personally because i also
[538.16 → 544.02] override the CD function in my shell, but my solution was to simply just modify my uh
[544.02 → 550.22] my own monkey patch to just work with RVM's uh monkey patches and just keep on working but
[550.22 → 558.56] I think that that type of thing was uh what originally spawned run you know uh the writing
[558.56 → 564.32] of run and then these other tools and I'm not sure of all the drama that happened, but there was
[564.32 → 569.84] many blog posts I'm sure there were many tweets, and you know uh maybe Michael can speak to it a
[569.84 → 575.46] little bit more but I think it got personal at a certain point um unfortunately and great glad to
[575.46 → 580.18] hear that out of all that came actually this funding and these people supporting the project
[580.18 → 586.18] which it allowed you to move in and do the work you've been able to do yeah yeah it was
[586.18 → 595.46] yeah if it was touching us personally and when and uh, uh for a short time if we've felt really
[595.46 → 603.48] terrible but yeah it passes with time and you you can see good points uh it's what it is ended
[603.48 → 613.20] up uh perfect for users so we get we got new functions new options to run RVM, and we have
[613.20 → 621.42] like new files to uh so you know you don't need to use RVM SC you can use ruby version
[621.42 → 631.56] which is now a common file for uh for major uh tools that do to the switching now yeah I think
[631.56 → 639.78] uh it's become commonplace to see a ruby version file more so than you see uh a RVM RC file or even
[639.78 → 644.72] I don't know I never use RVM, but they have a have a special file that they kind of watch for to
[644.72 → 653.28] to switch to ruby so they finally switched in some time to uh to ruby version but for a long
[653.28 → 660.16] time they use RVM version that's a and in fact now I mean you can put the ruby version right in
[660.16 → 667.10] your gem file now correct with newer versions of bundler and um RVM will recognize that as well
[667.10 → 674.12] to switch to that ruby yes, yes first we had implemented before bundler implemented
[674.12 → 684.00] the ruby uh directive we got a comment support so you could write it in comment and later on bundler
[684.00 → 690.98] introduced the ruby directive, and we still support the comment because in the ruby directive you can
[690.98 → 699.78] write any ruby code so you can do some magic to load ruby version file in this place and
[699.78 → 706.32] to avoid any problems with reading ruby from shell code because all the tools are shell code
[706.32 → 715.82] and we just allow the comment which is just a string which is ruby version so if is you have
[715.82 → 721.52] something else than a string in the ruby directive you can use comment to overwrite it for RVM
[721.52 → 728.70] so now you guys are pretty much supporting four different ways just over time huh so you can get
[728.70 → 736.72] that done do you still support the RVM RC I'm sure you do at least in version one yes so in version
[736.72 → 745.92] one it's still the number one format that is right so if you have ruby version and RVM RC then RVM RC will be
[745.92 → 755.48] read and there is no problem with some magic versions interpreted by other tools which should be not
[755.48 → 763.48] recognized in RVM because you can add extra logic in RVM RC so what's the preferred way going forward
[763.48 → 773.48] is it to use the gem file or to use the ruby version file so if you just want to use ruby and
[773.48 → 782.74] nothing else then ruby version is great but during the initial discussion for ruby version which was
[782.74 → 791.22] introduced by fletcher mike Nicole and I will, I propose another format which allows you
[791.22 → 799.76] list of settings something key equals value and where you can set ruby equals 193, and you can set
[799.76 → 809.10] java equals one seven I don't know java version so good so you can specify more than just ruby
[809.10 → 815.46] version you can describe your project because you never depend on just ruby you always use
[815.46 → 822.34] something else and more you use database so you might want to specify which database to use which
[822.34 → 831.60] python version with JavaScript version and for that I would see like the future of
[831.60 → 838.90] switching environment just one file versions.cone in which you can set everything not just ruby version
[838.90 → 846.32] because ruby version was really convenient just for ruby when you had tools to switch ruby version but for
[846.32 → 853.40] for the future what we will end up it's one file configuring everything in your project
[853.40 → 858.88] I like that so it's kind of like a middle ground between you know executing arbitrary shell commands
[858.88 → 865.36] and simply specifying a ruby version it allows you to specify versions for all the different dependencies
[865.36 → 873.48] you have yes, yes yes that that's that's the that's the plan and that file is already supported but
[873.48 → 881.46] because in rvm1 we switch only ruby versions it only allows you to switch ruby versions you can
[881.46 → 890.48] write anything inside, but you would need other tools to read it and in rvm2 we plan to introduce
[890.48 → 898.02] support for switching almost everything so we want to introduce support from other tools like
[898.02 → 907.36] virtual env I think it's virtual env for python NVM for node.js so everything else that's already
[907.36 → 913.76] working on the market we want in the end it merges in one tool that will be able to switch
[913.76 → 919.36] so you don't you don't need 10 tools to switch to your environment just one tool, and it's ready
[919.36 → 928.02] yeah it seems like from app to app or project to project it's gonna really get uh diverse so
[928.02 → 933.52] probably managing this gets tougher uh over time and that's where pull requests and issues on get
[933.52 → 939.10] up really come into play to help you keep my keep a heartbeat on what uh what's new out there what's
[939.10 → 945.76] different for someone else and be able to report that back and whatnot can you talk a bit about
[945.76 → 952.46] um what it's like to take over a project like this I know that uh you'd mentioned it's been
[952.46 → 957.30] almost two and a half years now since you started and we kind of talked a little bit about the
[957.30 → 964.00] intros of this where uh it kind of spawned from some of the drama but also turned into some uh financial
[964.00 → 970.44] injection through donations to RVM and Wayne being able to being able to bring you on board full
[970.44 → 975.50] time and you being in a place in your life to be able to take it on but what's it like taking over a
[975.50 → 981.66] project like RVM so from the standpoint that it's really important to the developers that use it
[981.66 → 985.82] like it becomes the centre point at which they pivot what is it like taking over a project like that
[985.82 → 993.56] so you don't really get to think about it when you start to do something, and you get passionate
[993.56 → 1003.96] about it, and you just do the work and because it's used by almost everybody you get so many tickets
[1003.96 → 1011.38] all the time that you don't have time to think so you just do the tickets do the tickets do the tickets
[1011.38 → 1017.88] and right now sometimes I get uh moments because everything it's fixed is fixed I get the moments
[1017.88 → 1024.86] like three days of silence so I don't have any tickets but then I get 10 tickets again and
[1024.86 → 1035.44] working on it working on it so I planned rvm2 for over a year now but every time i I'm I'm thinking
[1035.44 → 1044.36] it's ready I can start working on it everything is finished for rvm1 and then I get 10 new tickets
[1044.36 → 1051.14] and spend three next days working on the tickets and helping people to solve their problems and fixing
[1051.14 → 1058.70] the small things and every time it's something smaller and smaller, but people find these things
[1058.70 → 1066.88] with the quality when it increases overall then in the end people start complaining about smaller
[1066.88 → 1075.16] smaller things to make it fine-tuned for everything they need now see on your RVM plan uh you got a
[1075.16 → 1080.72] couple other contributors mentioned are they involved at all in helping kind of manage the
[1080.72 → 1088.74] influx of tickets or kind of doing some pre-validations I know like at pure charity I'm the product manager
[1088.74 → 1093.86] at pure charity and we know one of the things that we always try to protect our developers against
[1093.86 → 1100.48] is you know their focus on future product and improvements, and it seems like you know being
[1100.48 → 1106.66] able to validate those early and then maybe even earmark them as critical would help you save some
[1106.66 → 1110.24] time on the front end are they involved in that or is there any way the community can kind of step up
[1110.24 → 1118.48] to help you do something like that so I get few contributors from time to time that help and
[1118.48 → 1128.66] that's really help but because RVM is quite big it's over 20 20 lines 20 000 lines of shell code
[1128.66 → 1136.74] and the biggest problem is a shell code it's really it's really hard and there will is no good
[1136.74 → 1144.60] standards for coding in shell so I had to develop good standards over the years I worked on RVM
[1144.60 → 1154.88] and even I get contributions it I spent still quite a lot of time doing reviews so nothing breaks for the
[1154.88 → 1162.44] users because if is you don't check it even if there are tests because we got tests like last year
[1162.44 → 1170.54] and even there are tests the tests don't catch everything because there is uh over I don't know 20
[1170.54 → 1177.52] platforms supported right now so you can use RVM almost on every Unix like system and
[1177.52 → 1186.04] to get every contribution every code to work I have to still look on it to just from the experience
[1186.04 → 1193.80] point and to coach the catch the small things that are that need to be
[1193.80 → 1201.46] that can't be tested right now so you mentioned that it has 20 000 lines of shell code is that
[1201.46 → 1208.42] what you said yes so I have that's a lot uh that's huge on your and your plan for 2.0 one of the biggest
[1208.42 → 1214.32] changes is that you'd be switching to writing it not in shell but in ruby can you speak to that
[1214.32 → 1222.70] yes so the biggest problem with shell scripting is nobody knows it anybody knows how to write good
[1222.70 → 1232.02] shell code, and we write a tool for rubies so if a ruby developer wants to check something in the shell
[1232.02 → 1240.24] code he can understand mostly most of it but to write a good code that will be uh that will not slow down
[1240.24 → 1247.94] because that's quite hard thing to not slow down the shell code and that that will not produce side
[1247.94 → 1256.42] effects in random environments because uh supporting both bash and ash and in few flavours in few
[1256.42 → 1265.54] versions that's quite complicated and yes so we want to switch to ruby because everybody knows ruby and
[1265.54 → 1273.88] they're already good practice so you will not have to check every commit for code quality if it's
[1273.88 → 1282.28] even good formatted it's already something people know how to do it, and we only will have to
[1283.08 → 1292.60] do minimal review for security for bugs, but nothing like now to to to search all the special cases
[1292.60 → 1300.20] where experience really counts so RVM installs ruby for you, and you're switching ruby to a
[1300.20 → 1306.04] dependency surely you have a solution for getting RVM onto the machine or excuse me getting ruby onto
[1306.04 → 1315.08] the machine that you're going to use RVM to install ruby on yes so I was it was proposed to me for a
[1315.08 → 1325.24] few times to switch to ruby because everybody knows ruby, and it was before uh we got binary rubies
[1325.24 → 1333.12] binary rubies in RVM so right now we got binary rubies which basically is a ruby that's already
[1333.12 → 1340.30] compiled you can just take it on your system unpack it, and it's working if it's provided for your system
[1340.30 → 1348.54] and if there is no binary ruby for your system second option will be Ruby which is really
[1348.54 → 1356.56] stable now, and you get java for almost every platform in the world so if there is no binary ruby
[1356.56 → 1365.70] you can still get it working with Ruby and in the worst case a small thing that will be planned also for
[1365.70 → 1378.04] rvm2 maybe 2.5 is remote execution where you can run RVM locally on your system and install ruby on
[1378.04 → 1385.06] remote machine so you don't have to work you don't have to install RVM on every computer you will
[1385.06 → 1393.66] use rubies you only install it locally and can use the local version to install rubies on remote servers
[1393.66 → 1403.86] so in the end it will be possible to just install ruby without installing RVM or even prepare packages
[1403.86 → 1409.98] so that's another option, so the plan is to is that you'll have a little bit of shell scripting or
[1409.98 → 1417.40] non-ruby code that will download the binary ruby, and we use that to bootstrap and install other rubies
[1417.40 → 1422.84] does it then discard that initial binary or does is it resident on the machine or have you not
[1422.84 → 1430.32] even figured that kind of stuff out yet yes so for the initial setup there will be
[1430.32 → 1437.16] shell script that's always needed because you can either write shell code or python code
[1437.16 → 1444.04] it depends on what it's available on this remote system, but shell is something the limited
[1444.04 → 1452.26] limited shell sh shell is available everywhere and like base box you can right get it working on
[1452.26 → 1460.70] every device that supports Linux, so minimal shell code will be available everywhere, and you can use it
[1460.70 → 1467.54] too just to bootstrap if there is binary ruby use it downloads if it's not available show instructions
[1467.54 → 1480.66] for Ruby or how to do the remote installation cool so besides switching to ruby what are the other big plans for 2.0
[1480.66 → 1491.10] for 2.0 the biggest plan is to stop being just ruby version manager start managing everything it's
[1491.10 → 1502.62] it's another project from Wayne sig win SM framework which also was in share and did manage installation of
[1502.62 → 1511.06] software and managing software but not switching so all the installation part, and it's rvm2 will be like
[1511.06 → 1521.90] putting the ideas of SM framework to manage everything and the environment switching from RVM but in the end
[1521.90 → 1532.34] uh I'm still thinking about the switching part because I also helped with ch ruby and something small like ch ruby would be as a possible
[1532.34 → 1549.90] and maybe even we could integrate with ch ruby where RVM will be more for installation and uh for managing uh the internals of ruby like gem sets and so on but uh to switch the environment in your local shell you could be a good thing to do with the
[1549.90 → 1556.90] in your local shell you could use ch ruby you talked a little bit about this in your talk at uh
[1556.90 → 1561.62] at Ruby you mentioned uh python version manager as part of it I didn't get a chance to
[1561.62 → 1570.98] to watch the entire talk but um so it sounds like not just ruby versioning but python and others
[1570.98 → 1583.42] yes, yes so basic the initial process for uh for the version 2.0 will be to get ruby and JavaScript
[1583.42 → 1593.82] binaries available so you can get your race applications really fast because right now when you get ruby and want to start
[1593.82 → 1604.34] race project you still need JavaScript executable and that will be the first step that's the basic requirement for race project so
[1604.34 → 1610.40] that will be the first thing that will be working just to make sure we get compatibility
[1610.40 → 1617.34] with race project and second step will be integration with ruby gems
[1617.34 → 1625.38] uh because right now when you install gems you don't know which dependencies of the gems are needed it's
[1625.38 → 1633.40] not anything automated and uh in ruby gems I think it was in 2.0 uh there is made metadata
[1633.40 → 1641.34] which you can use to describe your dependencies of your gem and then uh with simple ruby gems plugin
[1641.34 → 1650.12] you can uh connect RVM and ruby gems where when you install a gem that has a dependency like
[1650.12 → 1659.78] nokogiri has lib XML you can say require lib XML lib XSLT and RVM will know how to install them for
[1659.78 → 1667.82] your system so uh it will be automatic, and the experience should be a lot better for final users
[1667.82 → 1673.90] so I'm just kind of thinking about uh this change and what this means and then I'm always a person
[1673.90 → 1680.66] that kind of kicks back to name so does RVM become something that becomes shaky ground meaning does the
[1680.66 → 1687.78] name change or does it change or morph to a different acronym like real version manager versus uh and I guess
[1687.78 → 1691.24] when Wayne was on the show so for those who've listened to the change level for a while you can go back to
[1691.24 → 1700.44] uh I think it's episode yeah episode 66 um we had wain on, and he talked about it, and it wasn't actually
[1700.44 → 1707.36] called ruby version manager it's environment manager right ruby environment manager yes so
[1707.36 → 1718.70] we got a page for RVM and alternative implementations and it is says ruby is not the only ruby version
[1718.70 → 1726.28] manager and ruby is not the only one ruby environment manager because uh RVM does both right now and
[1726.28 → 1738.60] and in uh rvm2 and the code name for it is SM framework SMF and because it's, it will be more
[1738.60 → 1746.44] based on SM framework the current implementation which I think wain mentioned it back then as BDSM
[1746.44 → 1753.56] yeah and since then we changed the name first to SM and then SM framework okay cool
[1753.56 → 1759.98] I was wondering because I know that Wayne uh kind of that was an unexpected I guess topic
[1759.98 → 1767.12] um for episode 66 when we talked about BDSM I know Steve was really happy to talk about it as well
[1767.12 → 1771.08] on that show so if you go back and listen to that it's definitely be a good primer for you to come back
[1771.08 → 1778.96] into this conversation here but uh it was pretty neat and quite low level and uh way over my head
[1778.96 → 1790.40] but it's still fun to listen to yes so uh rvm2 will be like a mix of SM framework of BDSM and RVM
[1790.40 → 1796.94] so does it uh I guess coming back to that then does the name RVM become stale at that point or
[1796.94 → 1801.60] do I mean I know you said codename is the plan potentially to change that have you talked to
[1801.60 → 1806.34] anybody about that as the community kind of put their two cents in about the the the name change
[1806.34 → 1814.80] or even a potential of yeah so I will not change the name stays rvm2 because uh RVM has its
[1814.80 → 1822.90] brand and people know it and if it's really easy to identify the product with the name so
[1822.90 → 1830.44] if anybody hears a new name it will be something totally new and the change might be harder and
[1830.44 → 1836.94] when you know it's the same product, and it's compatible because that's as one of the aims
[1836.94 → 1844.74] to get the code that's already out there and rvm1 is supporting it is should be
[1844.74 → 1855.62] also working with rvm2 so we do testing outside testing where no internals of RVM are tested only
[1855.62 → 1864.94] the API what's CLI what's available to the user it's tested and we plan to pass the tests
[1864.94 → 1874.72] for rvm2 so no we don't change the name it will stay we have some internal sometimes internal
[1874.72 → 1883.32] we refer it like a same framework but uh in the end it will be rvm2 gotcha i was during uh the
[1883.32 → 1888.10] conversation between you and jarred a bit there i was also taking note that right now you're in the
[1888.10 → 1894.40] clear too in terms of issues i was quite surprised to see that you have zero open issues right now
[1894.40 → 1899.60] on getup I'm not sure if you track issues anywhere else, but that's a that's a pretty
[1899.60 → 1906.84] you might be at zero issues you might be watching on the wrong repository I'm still I'm still using
[1906.84 → 1915.32] whencgwin slash RVM repository yeah and there are 12 open issues at least there were 12 before we
[1915.32 → 1923.98] started and i used a flag feedback needed which means i did everything i could need more information
[1923.98 → 1932.70] from the user and 10 10 10 10 10 issues are feedback needed, so there are two issues i know i have to work
[1932.70 → 1943.58] on and the rest 10 issues uh possibly uh could be something RVM has to do but in most cases that's
[1943.58 → 1952.42] happens to be that it's only just clarifying how things work and asking for more information and
[1952.42 → 1960.56] in the end it's often tiny change that's weird every time i go to uh issues it for some
[1960.56 → 1966.92] reason kicks me to milestone 17 which has no issues so weird because like I'm sitting there in issues
[1966.92 → 1972.50] I'm like there's no issues but i go back to the nav and i see issues in the cyborgs that's a that's an
[1972.50 → 1981.80] aside you need to click uh clean the milestone filter that's either a GitHub bug or a feature
[1981.80 → 1989.38] yeah I'm not sure which it is it's like yay no issues i was like that's cool let's mention that um
[1989.38 → 2000.92] yeah i i got uh two weeks ago i got uh two open issues only and there were different from
[2000.92 → 2008.58] the two that i have right now and yeah i was really happy, and it was before uh conference
[2008.58 → 2017.72] a camp a j ruby cone EU and during the conference i don't know i handle a lot of
[2017.72 → 2027.04] tickets it's like some months i got over hundreds of tickets handled per month wow so yeah and must be
[2027.04 → 2032.48] a a lot of pressure i guess just kind of having to potentially wake up the next morning like
[2032.48 → 2036.68] you go to bed the night before pretty happy, and then you go to sleep, and you wake up, and you're like
[2036.68 → 2045.90] oh what happened you know yes so if it's so you mentioned um i guess i mentioned this actually
[2045.90 → 2051.36] earlier in the show that uh that you're the release manager of RVM at engine yard so back when you very
[2051.36 → 2058.12] first started with RVM kind of serendipitously was able to step away from your current job take on
[2058.12 → 2064.58] responsibilities RVM we talked about the details around that, but now you're um when you kind of
[2064.58 → 2068.94] stepped in to be the full maintainer of it was around the same time you started at engine r2 right
[2068.94 → 2079.66] uh so it was like i work on it uh just as a maintainer for uh two or three months and then
[2079.66 → 2091.34] i got uh half-time as a release manager for RVM, but it was only half-time and only year after
[2091.34 → 2099.20] or one and a half year after i got the offer to get full-time on RVM and so what is it uh you
[2099.20 → 2102.92] know i guess what does engine yards play here i mean obviously we understand what engine yard is and
[2102.92 → 2108.80] the importance that they've played in the ruby community over the years um but what's what uh
[2108.80 → 2113.42] what's it like i guess being at engine yard and what does your role mean at engine yard being the
[2113.42 → 2122.46] release manager for RVM so i don't have a lot of contact with engine yard i get to the team
[2122.46 → 2131.88] meetings with Wayne and his team and i don't do much work for engineering yard i do mostly i do all
[2131.88 → 2142.70] the time uh RVM and only sometimes i get support questions for RVM products and i work maybe two
[2142.70 → 2150.58] months part-time on the small project to integrate RVM with one of the clients but in the end
[2150.58 → 2160.24] i do most of the things like i did before so i take care i take care mostly of making sure that
[2160.24 → 2168.40] releases uh working properly so i check all the tickets and make sure the version released will be
[2168.40 → 2176.06] stable that's that's the thing that i was contacted by engine yard hey we got some bugs uh you uh
[2176.06 → 2183.28] when was not uh not having much time at this point and i was the only other maintainer
[2183.28 → 2190.86] active maintainer at the time, and so i was contacted by engine yard because users got bugs and because
[2190.86 → 2196.76] of the bugs with RVM they were locked, and they couldn't continue work so they couldn't deploy
[2196.76 → 2203.00] applications to engine yard so if they couldn't deploy they couldn't pay that's so engine yard
[2203.00 → 2212.44] needed somebody to provide uh working RVM, so the clients can continue deploying applications
[2212.44 → 2219.58] and do they really work instead of fighting backs that's pretty neat the way that uh that works
[2219.58 → 2225.36] out though that they have such need for RVM that they're capable and willing to support open source
[2225.36 → 2230.02] in a way where you know not only do me and jarred and the rest of the listeners listen to this show get
[2230.02 → 2236.86] to enjoy the benefits of your work on RVM and the other contributors to that effort but at the
[2236.86 → 2244.48] same time you're full-time employed by engine yard to manage essentially the development of RVM how
[2244.48 → 2250.70] much can you talk a bit about how much um i guess feedback you get from the deployment teams or the support
[2250.70 → 2258.94] teams at engine yard and how that feeds back into uh making RVM better by you know identifying uh
[2258.94 → 2263.36] different issues that might come up that otherwise may never be really found unless you're kind of in an
[2263.36 → 2268.80] enterprise scenario, and you have to really support a large-scale application with uh with ruby is
[2268.80 → 2278.40] managed by RVM so yeah so it's uh the fun part is that engineer itself doesn't use RVM internally
[2278.40 → 2287.00] and okay and something ago like i don't know half year ago maybe a bit longer i was helping with
[2287.00 → 2294.86] one of the managed clients to get RVM working because they wanted uh the switching part
[2294.86 → 2302.98] automatic and not to not do everything manually they wanted just to say we are switching ruby RVM switch
[2302.98 → 2309.32] ruby and ready not to ask the staff hey switch a ruby for us make the application working move everything
[2309.32 → 2318.92] and they wanted to make that thing automated with RVM and uh it's there and I'm helping with that
[2318.92 → 2326.10] application but that so far it's just one application so not a lot of not a lot of feedback
[2326.10 → 2332.84] then from the support team yeah not a lot, but it's its the application is quite big
[2332.84 → 2342.90] that they are one of the biggest customers and i don't get any questions because everything is
[2342.90 → 2347.46] working it works well you were going to say something jarred i was going to say that the
[2347.46 → 2351.82] engine yard employs you full-time to work on RVM, and they largely just leave you alone is that
[2351.82 → 2359.50] what you're saying because that'd be awesome yeah mostly mostly mostly, but it's its uh you would say
[2359.50 → 2366.68] it's really great situation to be in because you get paid, and you don't have to answer
[2366.68 → 2375.78] before anybody, and it's not true because i answer before the whole community and when i do something
[2375.78 → 2386.42] wrong i get like in one hour i get tickets and stack overflow questions and very often somebody
[2386.42 → 2392.28] in five minutes somebody locks into ears and complains hey this is broken yeah I'm not saying
[2392.28 → 2396.62] there's no pressure on you, I'm saying that it's awesome that you get to work on that which you are
[2396.62 → 2401.28] already doing in your free time like your passion the thing you're passionate about now you get to
[2401.28 → 2410.18] work on that you know and yes, yes kind of the open source dream it's its it's really great but
[2410.18 → 2416.94] on the other hand on the other hand it's like it takes all your free time it's its really hard
[2416.94 → 2424.68] to find some time for something else i needed really to learn from beginning how to
[2424.68 → 2433.48] take my free time to just have some sports to spend some time with kids it's not nothing like you
[2433.48 → 2440.20] get in real jobs like eight hours, and you go because something always happens, and it's not like
[2440.20 → 2449.56] you do it in eight hours, and you quit uh you get questions you get support issues all the time all
[2449.56 → 2456.18] the day because everybody around the globe uses RVM so you get the need to do the support almost
[2456.18 → 2462.70] 24 7 yeah it seems like fair it seems like a nice lifestyle job too jerry doesn't I mean like
[2462.70 → 2467.04] to be employed full-time and hack on open source code and kind of improve the lives of
[2467.04 → 2475.80] at the same time they'll be the main uh burden bearer if that's uh if that's the case um to have to
[2475.80 → 2481.30] deal with the fact that but like you've said Michael time and time again that it works
[2481.30 → 2491.58] right yes so uh I think yeah maybe now two years two years ago when i uh started
[2491.58 → 2497.92] contributing it was like there was a lot of job a lot job of supporting people and
[2497.92 → 2506.00] at every issue i I got some small ideas how to improve things how to make the less support so
[2506.00 → 2514.58] I added warnings automation and things like autolips which was added half a year ago and the all the
[2514.58 → 2522.56] small things all the small messages make everything working smooth so I stopped getting like 10 requests
[2522.56 → 2530.60] daily why bundler doesn't work because right now RVM comes with ruby gems bundler which integrates
[2530.60 → 2538.16] bundler really with ruby gems that's the missing point of integration and I was it was really hard
[2538.16 → 2546.50] to get it working because ruby gems didn't want that integration bundler was afraid that it will break
[2546.50 → 2553.90] things and I still hear from some sources that's terrible thing, but there are over two millions
[2553.90 → 2562.56] downloads for the jam and everybody is happy and immediately when the support for ruby gems bundler
[2562.56 → 2572.44] was introduced in RVM the amount of issues with not bundler not working dropped from 10 daily to zero
[2572.44 → 2579.56] wow well just to give you some props I mean I've been a RVM user daily since I don't remember how far back
[2579.56 → 2587.58] years and um I would say it's stabilized to a point where I barely have to think about it anymore and
[2587.58 → 2593.08] I'm always you know RVM gets stable whenever there are new rubies out there and everything so far for me
[2593.08 → 2597.02] at least has been very smooth especially in the last year so you're doing you're doing a good job man
[2597.02 → 2604.06] thank you and just to kind of key out that one last point there too is that ruby gems bundler was
[2604.06 → 2614.28] merged into bundler 1.3 right it was planned but uh finally I was not able to do this oh I see so it's still
[2614.28 → 2622.98] an independent gem by itself then yes it's still independent gem but uh ruby gems 2.0 is already doing
[2622.98 → 2633.22] parts of bundler work and the plan for ruby gems 2.1 is to take over everything so I'm not sure about the
[2633.22 → 2643.12] gem uh JIT gems, but it probably will be a plugin for ruby gems 2.1 so you could uh quit using
[2643.12 → 2650.80] bundler and have all the functionalities in ruby gems and ruby gems has already supported for for the
[2650.80 → 2660.02] automatic loading of uh of the binaries with proper environment so you that that gem will be
[2660.02 → 2665.68] then useless if people start switching to just pure ruby gems yeah I don't know if we got a chance to
[2665.68 → 2671.14] really talk about it much, but we're close to being out of time but do we really talk much about autolibs
[2671.14 → 2679.56] and what that means is that that's what you're kind of keen off of their right yeah so autolibs I was I
[2679.56 → 2687.38] had it planned for a long time and I was really holding back with implementation because I wanted to
[2687.38 → 2695.54] make it for rvm2 I wanted it to be the major difference because it's something really it's
[2695.54 → 2702.68] planned for something bigger what's implemented right now it's just the minimal possible uh possible
[2702.68 → 2709.98] thing to make it working and for rvm2 it's still a lot of things like integration with ruby gems
[2709.98 → 2717.12] which are which is missing and I was forced to get it implemented in rvm1 because of
[2717.12 → 2729.18] uh the switched in ruby gems to SSL uh HTTPS URL forgetting gems because of security yeah and this one
[2729.18 → 2738.14] requires open SSL and open SSL on every system installs in different way, and it was quite easy to get
[2738.14 → 2745.80] lib yum which is needed for gems to work because it's tiny library you can compile it and it
[2745.80 → 2755.62] it works everywhere really simple but for open SSL I needed integration with the system because you can't
[2755.62 → 2762.40] compile open SSL if it's already there it will be taking more time than compiling ruby itself
[2762.40 → 2772.52] so then I had to implement autolibs in the minimal version which is just suitable for the shell coding
[2772.52 → 2781.04] because now it's in shell it's its huge project to get it working in ruby it would be
[2781.04 → 2787.08] something quite simple and shell it was really challenging
[2787.08 → 2796.14] well i uh I don't know uh jarred if you have any more you wanted to mention before we tail off we
[2796.14 → 2799.42] have a couple common questions we asked but if is you got anything else you want to mention jarred
[2799.42 → 2805.30] wait uh cool with that too well I was just hoping to nail Michael down on a guaranteed release date for rvm2
[2805.30 → 2814.88] come on Michael what you got yeah if is people stop opening issues for rvm1
[2814.88 → 2826.12] then Christmas will be something really possible, but it's not that easy to stop getting tickets
[2826.12 → 2834.30] because with every handled thing there happens to be something tiny that still needs to be
[2834.30 → 2843.10] handled and rvm1 is feature free for already a year, and we still got small things that need to be
[2843.10 → 2852.50] included like fusing matching when you want to match a one nine anyone nine free ruby and
[2852.50 → 2860.76] that that was needed for Travis for full support and because Travis is right now the biggest customer of RVM
[2860.76 → 2865.48] yeah we got that feature implemented even we are we had feature freeze
[2865.48 → 2870.68] so no more issues to 1.0 and 2.0 becomes a Christmas present
[2870.68 → 2879.82] yes, yes but I'm not sure about that no, no more no yeah crush your fingers probably won't have it but
[2879.82 → 2885.42] all right well maybe uh it might be a chance for someone to maybe uh step up and help you out though
[2885.42 → 2891.08] so I guess that kind of tells into our one of our common questions which is your know for you Michael
[2891.08 → 2897.16] what is a call to arm so to speak for the community the ruby community and I guess these other communities
[2897.16 → 2902.52] that might be stepping up that will eventually begin to use RVM as well python and others
[2902.52 → 2906.90] uh what's a call to arms for RVM how can the community step up and help you out to
[2906.90 → 2911.30] make uh our Christmases bright and beautiful with uh RVM 2.0
[2911.30 → 2923.30] yes so the plan is uh to get the issues handled and to stop uh handling new features
[2923.30 → 2932.70] and if is users could help with limiting the amount of issues if is it's nothing really, really big
[2932.70 → 2945.14] uh just uh help with documentation and help with handling issues then that should allow
[2945.14 → 2951.34] better start for rvm2 what's the best place to go for somebody interested in getting involved
[2951.34 → 2961.04] where should they start so we got quite good readies for uh tests for documentation and for
[2961.04 → 2973.62] uh RVM quite good it's lacking and if somebody wants to help and sees uh problems with uh documentation
[2973.62 → 2984.22] that's not really what should happen then we got everything on GitHub uh fork the documentation
[2984.22 → 2994.32] RVM side and just improve it just improve it that's a good tagline right there so uh yeah Michael one
[2994.32 → 3000.80] thing we like to ask our guests um and feel free to mention whomever uh means most to you but who
[3000.80 → 3003.74] might be a programming hero for you
[3003.74 → 3017.12] uh it's hard to say i I really love the work of Wayne yeah Wayne shagreen he he he did great job
[3017.12 → 3027.68] with RVM with SM framework and I'm really missing him in open source yes uh well I guess we mentioned
[3027.68 → 3033.96] to that Wayne has been on the changelog before episode uh we used to call it 0.6.6 but since we
[3033.96 → 3039.60] moved the five by five we started calling them uh by their real name so back in the 60s as we'd like
[3039.60 → 3046.24] to say episode 66 um you can kind of go back to kind of pickup you know Michael you mentioned uh SM
[3046.24 → 3053.60] framework uh Wayne touches on BDSM back in that day so it might be a good primer for you to go back
[3053.60 → 3059.08] and listen and even another friend of the show is uh Sam Stevenson's we mentioned RVM on here as
[3059.08 → 3067.36] well uh episode 64 is uh is that show he touches a little bit on uh how pow supported RVM back in
[3067.36 → 3075.02] those days and I think that was back that episode was uh 2011 so it's kind of dated but still neat for
[3075.02 → 3082.28] a primer on some of these topics if you want to go back in time a bit um, but you are Michael Paris
[3082.28 → 3089.46] on Twitter and GitHub that's m Paris p-a-p-i-s on Twitter so I guess people want to follow you or
[3089.46 → 3095.08] kind of reach out to you to say hello or even just a thank you that's uh where they should go right
[3095.08 → 3100.06] but is there anywhere else that people can kind of find you and kind of keep up with what you're up to
[3100.06 → 3110.12] yes so I'm all the time available on ears and all the time I mean if it's uh 16 hours a day
[3110.12 → 3119.74] and seven days a week and I'm available at each channel hash RVM, and you can find me there you can
[3119.74 → 3128.58] talk to me and I help everybody as long as it's ruby and RVM related that's yeah and we definitely
[3128.58 → 3135.52] want to uh thank our sponsor for the show uh for supporting the show app sketchbook you can use the
[3135.52 → 3143.48] code Dan sent me go to app sketchbook.com save five bucks uh neat I actually use this myself as
[3143.48 → 3148.80] or really neat whenever I sketch iPhone or iPad stuff I'm always using that actually i I even used
[3148.80 → 3156.38] it whenever I was working on the responsive version of the uh change law weeklies change design so it's
[3156.38 → 3161.20] kind of neat to map that out but Michael I want to thank you for joining us on this show today jarred for
[3161.20 → 3166.08] you being the co-host and Andrew who is missed today because he's not feeling so well he had uh
[3166.08 → 3173.30] some sinus snafu, but he did tee up this conversation with Michael and the update on RVM so thanks to you
[3173.30 → 3180.40] Michael Andrew and for you the listeners for listening so lets uh take this moment and say goodbye
[3180.40 → 3186.18] see ya goodbye everybody, and thanks for having me
[3186.18 → 3190.50] you
[3210.40 → 3220.50] you
[3220.50 → 3223.50] you
[3223.50 → 3225.50] you
[3225.50 → 3227.50] you
[3227.50 → 3229.50] you
[3229.50 → 3231.50] you
[3231.50 → 3233.50] you
