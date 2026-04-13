[0.00 → 14.50] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 188
[14.50 → 22.72] and today is a special show it's a combo show we have two shows in one just for you for Christmas
[22.72 → 27.52] holiday hope you enjoy it the first part of the call we're talking to Andrew despite about 24
[27.52 → 33.44] pull requests and also libraries.io and in part two we're catching back up with Jonathan Rosenberg
[33.44 → 39.52] the creator of Flynn a next generation application platform we had four awesome sponsors for the show
[39.52 → 48.12] code ship top towel digital ocean and also harvest our first sponsor is code ship in the new year
[48.12 → 54.06] January 12th they have a free webinar you have to check out code ships engineer Laura frank is going
[54.06 → 59.44] to give an overview of docker's ecosystem docker composed docker machine she'll talk about
[59.44 → 64.26] containers, and you'll learn about docker images why they're so powerful and how you can start running
[64.26 → 69.48] services in containers and when it comes to web apps and docker you'll understand how to develop
[69.48 → 75.76] your web apps using docker working with images registries and running services in containers
[75.76 → 81.62] the link to this webinar is rather long so I'm going to put it in the show notes, but you can also go to
[81.62 → 87.92] resources.codeship.com and look for webinars in that list, and it's going to link to the same webinar I'm
[87.92 → 94.18] talking about or head to the show notes and click the link there again totally free January 12th 2016
[94.18 → 101.62] from noon Eastern Standard Time to 1 p.m Eastern Standard Time that's one hour and now on to the show
[101.62 → 113.86] hey everyone we're here with Andrew despite Andrew is an open source software developer has done lots
[113.86 → 119.68] of cool stuff 24 pull requests libraries Io and Andrew you got a longer list than I can even say here
[119.68 → 124.02] right now, but we'll talk about some of these things but uh when you come on a show like this
[124.02 → 132.04] how do you introduce yourself uh as I guess like an open source enthusiast okay I've been
[132.04 → 138.52] i kind of built my career on the back of lots of other people's open source work so
[138.52 → 144.30] kind of the kickstart for the whole thing was WordPress and teaching myself some Ruby on Rails
[144.30 → 149.44] so it feels like I've been kind of standing on the shoulders of giants for a long time
[149.44 → 156.50] and I've got to the point where I feel like I can now start to really contribute back and kind of
[156.50 → 163.04] give back based on the things that I've been using for years uh to the point where I try and do that
[163.04 → 168.78] all the time now if I can let's get a little history of you then I guess you know sometimes what we do on
[168.78 → 174.94] this show is figure out where someone came from to kind of make sense of and even establish more
[174.94 → 180.20] credibility to what they're doing now so where did things begin for you as a programmer
[180.20 → 188.22] so I originally didn't get into programming I went down the robotics route okay at university
[188.22 → 195.16] I thought I'll try and do something slightly different from just computing and robotics turned
[195.16 → 202.12] out to be basically just advanced math all the way through every part of it uh is just comes down to math
[202.12 → 208.76] which at the time I didn't find particularly interesting and ended up actually uh kind of
[208.76 → 216.02] setting up a blog and then wanting to customize a blog and basically self-taught myself uh
[216.02 → 222.32] enough kind of web programming on the side of doing my robotics course when I finished the university
[222.32 → 230.24] degree I was so kind of involved in the web stuff that I was doing just getting into Ruby on Rails about
[230.24 → 237.90] nine years ago and it kind of went from there like I was able to pick that up much easier than the
[237.90 → 246.72] robotics kind of very industrial very uh hard to get into which it's definitely changed now but back
[246.72 → 254.06] kind of nine years ago was very difficult to really get your teeth into and learn like in this way that
[254.06 → 260.86] open source helps programmers to pick stuff up uh really easily just because so much code is available
[260.86 → 267.54] uh in the robotics world it's really not like that at all yeah it seems like robotics might be a little
[267.54 → 273.48] bit easier nowadays and some might even call that internet of things or what have you there's
[273.48 → 280.98] probably robotics is obviously one term for it and then attachment to that might be IOT or whatever
[280.98 → 286.78] what uh what do you think about it now do you think man I can, you know I've got all this other
[286.78 → 291.96] skills now considering your path with Ruby on Rails and ruby and the things you've been involved with
[291.96 → 299.12] have you had some second thoughts about going back to robotics so uh over the last couple of years I've
[299.12 → 304.98] definitely dipped back into um especially around the node copter movement where you can get a
[304.98 → 314.86] power AR drone, and essentially it runs a little busy box Linux uh install on board, and it's a Wi-Fi hotspot you
[314.86 → 323.04] can load like connect it with your macBook turn it into it uh and there's a nice uh kind of API that you can
[323.04 → 334.78] talk to over UDP there's a little node module for essentially telling it like take off land do flip uh, and you can even stream the video back to a web browser
[334.78 → 342.06] all of this stuff is open source, and it's really easy to get into obviously you still run into like
[342.06 → 349.52] the fact that physics isn't very easy to program against and the real world has a lot of things that
[349.52 → 356.04] are much harder to program for than like in a browser environment if you run out of range and your drone
[356.04 → 363.22] hasn't been told to stop it just carries on until it hits something yeah I see the core team here on
[363.22 → 367.86] nodecopter.com and Felix geissendorfer has been on this show before way back in the day it's been
[367.86 → 374.18] probably 130 shows since we've seen the likes of phoenix uh Felix around here but I also see you as
[374.18 → 380.24] the core team so you're part of that yeah so I started I managed to get a number of drones uh
[380.24 → 388.18] basically by getting companies to sponsor a drone for an event right and I ran a number of events around
[388.18 → 394.02] the UK the UK being much smaller than like the US I could drive from one end of it to the other in a
[394.02 → 401.86] day and I would kind of lug 10 drones around take them to a big space like a sports hall and then say
[401.86 → 408.10] like okay 30 programmers a day see what you can do with them uh fix them up at the end of the day and
[408.10 → 412.88] then drive them off somewhere else, so part of this big this give back mentality you have
[412.88 → 418.34] just kind of thinking is this something when they sponsored did it is it something that you were
[418.34 → 423.50] doing as like a paid thing or was this because you were just in love with robotics in the community
[423.50 → 430.32] it's just a brilliant uh kind of small community of lots of people who had never really had that
[430.32 → 436.44] experience before and to enable that we did a number of things with coded dojo as well right which
[436.44 → 442.86] was basically like kids who had just enough JavaScript to be dangerous uh just unleashed them on
[442.86 → 448.20] the drones give them some example code and then let them change and copy and paste bits so that
[448.20 → 453.78] they can actually start the drones doing kind of like manoeuvres and trying to fly them around in a
[453.78 → 458.90] square in the room you can imagine how crazy it starts to get when you've got like 30 kids flying
[458.90 → 465.38] 10 drones in one room yeah with JavaScript well especially when you think about things like you'd
[465.38 → 472.00] mentioned before where you know you can, I'm familiar with uh node copter the project and you
[472.00 → 476.72] know the syntax and whatnot like if you're just telling it to you know to do a clockwise turn or
[476.72 → 482.12] to go forward you know 10 feet you know you don't know if there's another kid there or another cop or
[482.12 → 488.14] a wall there so it could be kind of dangerous yeah so that's where the kind of yeah the robotics
[488.14 → 491.92] aspect starts to come back into it once you've got the basics then you're like okay well I need to
[491.92 → 498.20] learn about feedback and then I need to learn about control algorithms, and you get quickly back into
[498.20 → 504.92] that math uh I was talking about earlier uh the initial kind of your first time at a node copter
[504.92 → 509.60] event is great because you can do you can start to do the simple things but when you really start to
[509.60 → 515.72] get into it your kind of progress slows down you hit a wall of like oh actually some of this is really
[515.72 → 522.56] hard, so the open source side comes back and kind of saves you where people have with more experience
[522.56 → 527.76] to build things that you can then go and like read the source and go oh okay I understand a little
[527.76 → 533.12] bit how this works now based on what someone else has actually already done and shared whereas in the
[533.12 → 538.72] traditional robotics community it's all kind of proprietary enterprise software that is written
[538.72 → 546.40] in c++ and not particularly user-friendly so when I'm at your home page which is your lastname.io
[546.40 → 552.36] and look down you're the at least the code you have listed here I'm not on your GitHub repo or your GitHub
[552.36 → 559.78] profile, but libraries like Io is on their split node SAS 24 pull requests uh contributor first pull
[559.78 → 565.84] request which is kind of interesting first pull request uh brooder Xbox controller hipster news and
[565.84 → 572.32] lanyard an unofficial wrapper for the lanyard API I don't see anything in there for uh node copter
[572.32 → 577.92] or anything on the robotics side is there any plans for anything on that front for you um so
[577.92 → 584.00] I've done different pieces a lot of the uh the code that I wrote for that is on my GitHub account and
[584.48 → 593.20] it's quite experimental it's like the uh the basics to get you started with say plugging uh a con an Xbox
[593.20 → 602.24] controller into node and then using the output from that to control the drone so rather than uh contributing
[602.24 → 607.28] directly to the node copter code I did a lot more essentially working with other people pairing
[607.28 → 613.84] with them to get them started which doesn't really show up on my GitHub account so much right what uh
[613.84 → 619.36] what is your current situation now with node copter anything happening there any new events coming up
[620.16 → 625.36] uh there isn't much happening right now that the core team has kind of disbanded off in different
[625.36 → 631.92] directions Felix is doing a lot of go yes and lots of this there's still a lot of good
[631.92 → 638.96] node copter related things going on uh Chris Williams of JS cone has got the new parrot
[638.96 → 643.76] drones I forget what they're called it's like I think it's the rolling spider much smaller more
[643.76 → 650.16] affordable drone I was thinking bebop or the bimbo or something like that yeah well those that
[650.16 → 658.64] work on the same protocol so yeah that's it with the uh kind of wide view camera on the front of it
[658.64 → 666.40] uh they all work over this new protocol and the rolling spiders are a Bluetooth which
[666.96 → 673.12] is much harder to reverse engineer than uh than the Wi-Fi kind of UDP protocol that you could just listen
[673.12 → 680.64] to right that's interesting to hear your take and uh background and robotics and node copter it's a
[680.64 → 686.32] shame that uh the core teams kind of disbanded as you mentioned uh because I was always a fan of that
[686.32 → 692.96] project and uh several times on this show the hero of people has been Jim lyrics, and he's had a lot
[692.96 → 699.20] of influence in that front too, and it's just a really fun project and I didn't know about the coder dojo
[699.20 → 703.36] piece where you're actually working with children and kids doing this stuff I think it's just like a
[703.36 → 708.72] fun way like you said before of having that heart of giving back yeah um you know whether it's just
[708.72 → 715.20] open source but also to people too you know and for a kid rather than like a console log as your output
[715.20 → 721.36] to actually get like a robot to take off and hover in the air even if it's almost identical code right
[721.36 → 726.24] it's just the most engaging way to get someone involved interested in program absolutely I mean it's
[726.24 → 732.32] you know you talk about real world response you know an actual thing they can touch and throw or play
[732.32 → 736.08] with or whatever that they can, you know later on when they're actually programming it they can
[736.08 → 741.28] actually still hover it in their own hand like they would any toy but to be able to actually write a
[741.28 → 746.88] few you know characters on a screen and or new words they're learning and bam it starts working
[746.88 → 755.44] that's cool yeah well lets uh let's tail off to that and uh talk about your project 24 pull requests
[755.44 → 760.96] that's 24pullrequests.com and this show is coming out in the Christmas holiday season so I thought it
[760.96 → 765.44] would make sense even though we're kind of late to the ball so to speak because the basic idea of this
[765.44 → 773.28] is to send 24 pull requests between December 1st and December 24th um right and that's such an
[773.28 → 776.80] such an interesting idea I think it's been around for at least three or four years if I can remember so
[776.80 → 783.60] what's what is this project to you yeah, so this is I think it's the fourth year it's been running and
[783.60 → 792.96] it started out as not even really like it was more of a idea and a challenge just as like why don't
[792.96 → 798.88] you try and do this it didn't have any kind of code behind if it was just the original web page you go
[798.88 → 804.24] back and look at like the first commit on the repo there's a single HTML page that just says like try
[804.24 → 813.04] and do 24 pull requests between like on the 24 days up to Christmas uh and that came from an uh a blog
[813.04 → 820.88] that only runs uh in those same days for 24 ways yes I thought that might be influenced by that yeah
[820.88 → 826.88] absolutely loved it uh but uh as a developer which they've they've got a lot more developer articles
[826.88 → 833.20] now but back four years ago is very much design focus and as a developer i kind of felt like oh I'd
[833.20 → 838.16] I'd love to do something like this but maybe a bit more code related and I thought well why not
[838.72 → 845.12] 24 pro requests has a nice ring to it and I get people to send 24 requests like that's quite an ask
[845.12 → 850.40] but if we can get lots of people doing it then you're more likely to go like yeah let me try
[850.40 → 856.16] and do this as well like everyone else seems to be contributing back um, and it's kind of every year
[856.16 → 862.56] doubled the amount of people and the amount of poor requests uh since it first started
[862.56 → 868.08] which is blowing me away I didn't expect it to have that kind of response well so I mean I guess
[868.08 → 875.28] if you did it on a whim so to speak uh in a way to pay some homage to 24 ways what was your initial
[875.28 → 880.56] request you know your just your initial expectation what were you thinking at first really just wanted
[880.56 → 887.12] to see what other people thought of it is this crazy idea or is it something reasonable like to actually
[887.12 → 893.60] give uh if you're you've been using all of this open source code throughout the year to actually
[893.60 → 899.60] try and go okay well I'm going to try and contribute back a patch to all the kind of maintainers who
[899.60 → 908.32] have been supporting my work throughout the year can I help them by fixing a bug or making an improvement to
[908.32 → 914.00] one of the libraries that I use which then will in turn help me by improving the quality of the code that i
[914.00 → 919.12] depend upon, and you make it pretty easy too because you have logging with GitHub so uh pretty easy
[919.12 → 926.32] credentials there and I think you asked for some very, very sparse um I guess what do you call that
[926.32 → 931.76] authentication back to GitHub yeah asking for like your basic public profile it's not even asking for
[931.76 → 937.92] much really in terms of you know clicking one button using your existing GitHub profile and getting
[937.92 → 943.60] access to this dashboard which shows off various languages and ways that uh I'm assuming that you're
[944.24 → 950.80] probing the community based on what they prefer you're saying hey these are projects out there
[950.80 → 958.40] that are that could use some help exactly so when you really the GitHub login is something that came
[958.40 → 964.16] along, and it's like after a little while when people said well we're already doing this all the
[964.16 → 969.60] work is happening on GitHub like if can we start tracking and kind of showing this as some kind of
[969.60 → 974.88] advent calendar so you get like on your profile page a little calendar that shows the pull requests that
[974.88 → 980.72] you've sent on different days, and we detect the languages that you've used on the repos that you
[980.72 → 987.20] have or that you've contributed to on GitHub and automatically suggest projects that match with the
[987.20 → 993.60] languages that you're you have some experience with and the projects are submitted by the community or the
[993.60 → 999.44] maintainers themselves so it's you can do a pull request to any uh GitHub repo and that will that
[999.44 → 1006.16] will count but the ones that we email you to go oh would you like it there are so many days
[1006.16 → 1010.88] left till Christmas here are three projects that match languages that you've said you're interested in
[1011.44 → 1015.36] why don't you try and send a pull request to one of these today I think it's fascinating too
[1015.36 → 1021.52] especially the fact that you were fetching stuff I've already contributed to and saying well hey because i
[1021.52 → 1027.12] I didn't even notice that, but you'd selected uh I'm more of a front-end developer than a back-end
[1027.12 → 1033.04] developer so you got things like you know sass and CSS related JavaScript related and I didn't even
[1033.04 → 1037.76] quite notice that those I thought they might just be smart defaults, but they're actually based on my
[1037.76 → 1044.56] behaviours on public activity and GitHub yeah, yeah so I used to work at GitHub uh worked there for a
[1044.56 → 1050.88] almost a year and kind of had a good it was actually how it kind of got me the job uh because I'd
[1050.88 → 1058.00] been doing all this good stuff with 24 pro requests and the so it hooks nicely into the
[1058.00 → 1062.88] the bits of information you have without being too kind of over the top and going right oh I know all
[1062.88 → 1068.40] about you, and we're not going to pull way too much information in I think what's interesting too is
[1068.40 → 1073.28] you've got some at least now it seems you've got some sponsors to help make this possible so what
[1073.28 → 1078.24] what kind of sponsors do you have and what uh what roles do they play in making 24 pull requests
[1078.24 → 1085.12] possibly cheer the uh the majority of the thing of the sponsorship comes around the services third
[1085.12 → 1093.12] party services that we use to keep the site running so Heroku uh specifically Heroku Postgres
[1093.12 → 1099.20] has sponsored it every year to cover the um the bill during December outside December the site
[1099.20 → 1105.52] basically shuts down it stops tracking for requests it stops uh kind of running any background tasks so I can
[1105.52 → 1113.04] scale it down to one free Dino and a small database, and it doesn't cost any money but over the past few
[1113.04 → 1119.12] years it shows up on hacker news and suddenly the traffic goes wild uh had to scale it up to a couple
[1119.12 → 1125.44] dynes or add in a little bit of uh caching and Heroku Postgres covers most of the cost of those things
[1126.08 → 1132.40] DN simple jumped straight in on the first kind of week and said do you want like to use our DNS will
[1132.40 → 1140.32] cover the cost for I think they've covered the cost for like 20 years or something wow of DNS uh and
[1140.32 → 1149.04] domain name, and then we send a lot of emails uh I think last year we sent kind of close to 100 000 emails
[1149.04 → 1157.52] during the 24 days so uh got in touch with SendGrid last year, and they sponsored they basically
[1157.52 → 1162.48] covered the cost of the of sending those emails through SendGrid, and they've come back and uh
[1162.48 → 1170.00] covered it again this year that's awesome so it covers the costs aren't huge, but it means that
[1170.00 → 1176.64] no one has to worry that there's like any kind of financial pain that could happen from the site
[1176.64 → 1182.00] getting too popular right well I mean most importantly you know this is something that you've started as a
[1182.00 → 1188.16] as a part of your love for giving back to open source, and you know just finding more and more
[1188.16 → 1194.80] ways to include people and share, and it would suck to have you know a 500 bill every December to
[1194.80 → 1199.84] to make this possible while you may or may not be able to afford it you know it's its very interesting
[1199.84 → 1208.96] to see DNS simple bug snag SendGrid ROK Postgres and uh and uh the last one here is sci-fi JS just to
[1208.96 → 1215.44] see them step in and say hey we care enough too to get these services for free yeah yeah loads of
[1215.44 → 1222.72] uh support and not necessarily always financial support but having uh people from each year there's
[1222.72 → 1228.56] a few people who step up to kind of help triage the issues and the pull requests that come in
[1228.56 → 1236.80] we've had so far looking on the GitHub page 175 contributors to the 24 pull requests uh repository the main
[1236.80 → 1244.64] uh project which is kind of overwhelming during the period of December the amount of activity that
[1244.64 → 1251.68] happens on the repo for uh but what is essentially a side project yeah well it's uh it's certainly an
[1251.68 → 1255.44] interesting project to us and like I said I've been watching it for a couple of years now and every year
[1255.44 → 1262.32] I'm thinking you know i I don't think about it until um December, and then it comes around it's like oh i
[1262.32 → 1267.36] would love to talk to this guy and so finally we were able to you know four years later sync up
[1267.36 → 1272.24] with you and sort of cover this so it's great I've been listening I remember listening to the change
[1272.24 → 1280.24] log back way back when uh win was on it as well yeah uh good times yeah we miss when
[1280.24 → 1287.20] around here he's uh he's a GitHub doing his awesome stuff on the API being uh an API junkie as he likes to
[1287.20 → 1296.64] say so we uh we miss yeah exactly he's fixed a few bugs for 24 progress where we try and get the
[1296.64 → 1303.28] the best way to pull in the 20 like the pull request for a user like over a given time period which uh
[1303.28 → 1309.44] there are different ways of doing it but now we're using the like the GitHub firehouse the event feed
[1310.16 → 1316.40] to try and pull in 20 like your request as soon as you open it which is pretty neat as soon as within a
[1316.40 → 1322.08] maybe like 10 seconds of you opening your progress on GitHub it shows up on 24 requests
[1322.64 → 1326.48] well cool lets uh let's take a break real quick when we come back we're going to talk a little bit
[1326.48 → 1333.12] more about contributing what that means in 24 pull requests you know how that kind of works we'll come
[1333.12 → 1339.12] back we'll talk a bit more about 24 pull requests, and then we'll move on to libraries.io and all that
[1339.12 → 1344.80] that's going on with package management so we'll be right back our friends at top town launched a
[1344.80 → 1349.84] scholarship program for female developers to support aspiring female computer scientists
[1349.84 → 1354.32] developers and software engineers to help achieve their goals through financial support and also
[1354.32 → 1359.92] mentorship each scholarship winner will receive a five thousand dollar scholarship that can be used
[1359.92 → 1364.80] towards education and professional development goals you can spend this money on anything you want
[1364.80 → 1371.44] from coding boot camps to online programming courses textbooks you name it you also get one-on-one
[1371.44 → 1377.60] mentoring an entire year of weekly one-on-one mentoring with a top tile senior developer and
[1377.60 → 1383.52] this person is going to help you with topics like project guidance choosing an academic or career path
[1383.52 → 1389.12] and also preparing for interviews head to toptown.com scholarships to learn more and also to apply
[1392.08 → 1397.68] all right we're back again from the break with Andrew despite, and we've been talking about 24 pull
[1397.68 → 1403.28] requests an interesting way to give back to open source during the holiday season here at Christmas
[1403.28 → 1409.68] so between December 1st and December 24th Andrew and the rest of the gang that's a part of this is uh
[1409.68 → 1415.76] is asking everyone to find ways to give back to open source that matters to them so Andrew the
[1415.76 → 1422.96] next part I like to talk about on this is ways people can contribute on your contributing page you have
[1422.96 → 1428.16] guides and things like that like where did this come from and how do you guide people into
[1428.72 → 1433.92] contributing is it like people who are new to GitHub or new to open source you know who are you trying
[1433.92 → 1440.72] to reach when it comes to this um so initially it was aimed at people who use a lot of open source
[1440.72 → 1446.00] and i kind of felt like as someone who's a lot of open source myself that I should be
[1446.00 → 1454.16] actively trying to contribute to some of these projects um, but it's kind of moved towards much
[1454.16 → 1461.76] more of a way of making it kind of okay for to get into open source because so many people are doing
[1461.76 → 1468.48] it at the same time and sending their first pull request as part of 24 pull requests right that this
[1468.48 → 1475.84] move towards like okay well you can get started here and then continue, and we've got um we've got a
[1475.84 → 1482.80] get a chat room which is full of really friendly people, so people will hop in and go like uh I'm
[1483.44 → 1488.72] I'm not sure where to send my first pull request like can you give me some tips here are like some
[1488.72 → 1493.20] things that I'm interested in and other people will be able to point them in the right direction
[1493.20 → 1498.64] help them rebase their branches uh and do all the kind of the different learn about all the different
[1498.64 → 1504.32] pieces involved in contributing to a project I see also has some other ways to find projects so not only
[1504.32 → 1511.84] just ways that uh 24 pull requests is using that GitHub login to you know kind of get to know who's
[1511.84 → 1515.28] logging in and allowing them also to choose their own ways, but you also mentioned several of the
[1515.28 → 1521.28] places like code montage code triage and a couple others um where how do you find this list and if
[1521.28 → 1525.84] someone out there is like hey I have a similar site how do they go about uh getting in touch with
[1525.84 → 1531.52] you are the site uh workable can someone update the site themselves and send a pull request for this
[1531.52 → 1538.24] absolutely the uh all the pages are part of it's its a Ruby on Rails application and there's kind
[1538.24 → 1547.20] of a static um controllers section that has all of this content in it so you can if you have some kind of
[1547.20 → 1554.08] uh site that will help people to be able to get into uh sending poor request contributing to open
[1554.08 → 1561.28] source definitely open up request um or even just an issue and say like can you add this to the
[1561.28 → 1566.72] contributing page uh all the projects that are listed on the contributing page also get shown on the
[1566.72 → 1574.72] home page when it's not December so because 24 progress doesn't really do anything for you outside
[1574.72 → 1579.12] Christmas it goes here are some other different ways of getting involved or finding out about
[1579.12 → 1585.44] projects that might be uh useful for you, you mentioned that uh another way this is kind of
[1585.44 → 1591.12] morphed over the years or change of the years is originally it was sort of focus on those who use a lot of
[1591.12 → 1597.20] open source and encouraging them to give back during the season and now kind of transitioning into a way
[1597.20 → 1603.04] to help people get involved in open source, and you have another project called first PR which i actually
[1603.04 → 1607.36] uh used about a month ago when i first kind of picked up this conversation internally here
[1608.00 → 1611.60] and I was like that's pretty interesting and I went and looked at my first pull request and I was like
[1611.60 → 1617.12] that's embarrassing so I don't know about you, but my first pull request is kind of embarrassing
[1617.12 → 1623.68] it's a good way of seeing what uh kind of your heroes how they got started uh sending their
[1623.68 → 1629.52] first request and that may not be their first ever open source contribution it only works from the
[1629.52 → 1636.40] introduction of pro request 2.0 on GitHub which is I guess kind of like five years ago or so but for
[1636.40 → 1643.52] a lot of people it will be their first time that they've contributed code to a project uh or documentation
[1643.52 → 1650.64] if it's part of their GitHub repo which I think a lot of projects have started to move their documentation
[1650.64 → 1656.40] out of wikis and into right repositories so that they have a good way of managing and encouraging
[1656.40 → 1662.96] that same kind of collaboration and review yeah I don't uh i never really cared for wikis not being
[1663.92 → 1669.44] well I don't care for how the wikis are actually set up I actually prefer an actual repo for it and
[1669.44 → 1675.28] that whole method to me is just seeming a bit better for docs yeah definitely and the lines of all the
[1675.28 → 1680.72] similar kind of things you could set up uh essentially Travis tests to check the typos
[1680.72 → 1685.60] and different things if you wanted to or have those docs automatically published to GitHub pages when
[1685.60 → 1692.64] you merge the pull request so before we transition this conversation to libraries.io is there anything
[1692.64 → 1697.44] else about 24 pull requests that the community needs to know about that uh that we didn't cover so i
[1697.44 → 1704.32] think we covered uh most of it the if you're interested in actually helping move the site forwards or
[1705.12 → 1711.28] implementing like other functionality I'm always open for that most of the code now is kind of
[1711.28 → 1717.20] being written by someone else for the project I've I like to say that I've lost control of it and if
[1717.20 → 1724.56] you're interested in either helping triage issues or uh kind of make improvements across the site especially
[1725.20 → 1731.84] for translation the site has been translated into like 16 different languages completely done by open
[1731.84 → 1739.20] source contributors uh and if you want it in your language then dive in there's its using standard
[1739.20 → 1746.72] rails like i18n translation so it's easy to pick up that one file and translate it into another language
[1746.72 → 1752.88] and enable that for everyone else in uh who speaks that language to have a better experience with
[1752.88 → 1758.64] contributing to open source very cool and that's uh that's on its own org too so it's GitHub.com
[1758.64 → 1765.12] slash 24 pull requests slash 24 pull requests that's where the actual uh rails app repo is at
[1765.12 → 1769.68] all right let's let's talk about uh well obviously there's some pricing here so I can't tell if this is
[1769.68 → 1775.04] your startup what is libraries.io to you the libraries is I've been working on it for about eight
[1775.04 → 1784.40] months as another side project which is kind of like how can I have given a incredible range of open source
[1784.40 → 1791.76] libraries if I want to compare a load of them uh to work out what is the best Regis client if I'm writing
[1791.76 → 1800.24] some node uh that was kind of how it initially started I wanted to index every open source library
[1800.24 → 1806.32] into one place in a standard format so that I could have a good quality search that bubbled the best
[1806.32 → 1811.52] project to the top so that I could be sure that I was making the right decisions when picking a
[1811.52 → 1818.64] dependency um and from there it's kind of wildly expanded uh and gone off in lots of different
[1818.64 → 1825.92] directions now pulling out the dependencies for every library as well and essentially building out
[1825.92 → 1834.88] a graph of the dependency network for each package manager and I think it supports about 29 different
[1834.88 → 1842.00] package managers at this point about 1.1 million different libraries that's quite a bit yeah so it's
[1842.96 → 1850.88] slightly grown beyond my behind a side project uh, but it currently doesn't really make any money to
[1850.88 → 1856.80] support itself so I've just started to look into ways of making it be able to support itself so that
[1856.80 → 1865.20] I can spend more time on it with some uh private repository tracking how that works, and it works exactly
[1865.20 → 1871.12] the same for open source and is completely free you can log in with your GitHub account, and it will
[1871.12 → 1877.60] given any repository it will pluck out all the dependencies across every different package manager that it
[1877.60 → 1885.76] supports so you might have a package Jason and a gem file and maybe even a bower dot Jason it will find
[1885.76 → 1890.80] all the dependencies in that repo, and it will tell you whenever there's a new version of one of those
[1890.80 → 1897.44] things that's released but rather than just doing it at that snapshot it will also hook into GitHub and go
[1898.08 → 1905.52] whenever you add a dependency or remove a dependency I'll automatically start watching that as well so you've
[1905.52 → 1912.40] got this kind of real-time view of everything that your application depends upon, and then you can be
[1912.40 → 1920.64] notified about anything that happens related to those dependencies so say that one is marked as deprecated
[1920.64 → 1929.68] or it has a license change or potentially even removed from the package manager, so there's like a good 7 000
[1929.68 → 1937.44] libraries that have been removed from NPM since I started tracking NPM about seven months ago which is
[1937.44 → 1944.24] crazy you think I'm just going to do a NPM install and something is gone you imagine if that happens
[1944.24 → 1953.28] whilst your machine is auto-scaling say it's making a new version of another server in your cluster
[1953.28 → 1961.84] if it does a NPM install during that process that is just going to be a huge pain yeah libraries just
[1961.84 → 1968.40] tries to give you that total view of everything that you use in a way that is essentially only going
[1968.40 → 1974.32] to tell you about things when they change rather than you having to remember to go and review your
[1974.32 → 1980.48] dependencies on a regular basis can you talk about the uh real world example I'm assuming there is some
[1980.48 → 1984.88] sort of pain you personally felt you know you mentioned the original version of the idea and
[1984.88 → 1989.60] how it's scaled since then, but you know when you started to get towards more of the model it's in now
[1989.60 → 1995.92] which is your know tracking all these different package managers and dependencies and all that you
[1995.92 → 2000.64] mentioned that it does what are some of the real world problems that you faced yourself that led you to
[2000.64 → 2009.76] build this well so running a number of open source projects like uh like 24 per request and um a number of rails
[2009.76 → 2019.60] apps as well having either internally or as private repos or open source projects the amount of times
[2019.60 → 2025.60] like oh there's a new version of rails which applications do I need to go and update to make
[2025.60 → 2032.32] sure that I pick up whatever changes are made or potentially there may be performance fixes
[2032.80 → 2039.28] that unless I'm actively going to look for all of these changes like there's no good way for me to know
[2039.28 → 2047.52] when something moves in the transitive dependency tree of that application and over time especially
[2047.52 → 2053.04] working in node projects the size of that dependency tree is getting bigger and bigger and bigger as
[2053.60 → 2059.28] people depend on more and more libraries and those libraries depend on more and more libraries that
[2059.28 → 2066.40] I just didn't feel like I had good visibility on all the code that I depend upon so if one of those
[2066.40 → 2073.36] things breaks I really may not even realize for a good few weeks before I'm actually go back and
[2073.36 → 2080.32] review those things so I felt like I had no idea of all the code that I was depending on and I wanted to
[2080.32 → 2086.32] be able to kind of get a hold of that and then start to automate it because otherwise it just becomes
[2086.88 → 2093.20] kind of collection of scripts which are useful to me, but they should be useful to everyone else as well
[2093.20 → 2099.76] right at the same time picking all that data up and using it for the search engine so it feeds in
[2099.76 → 2107.92] things like the number of projects that depend upon a particular project so it will highlight the projects
[2107.92 → 2116.00] that are highly depended upon in a community for example imagine you're looking for libraries to convert
[2116.00 → 2124.32] XML to Jason in uh in node that there could be 10 different options to do that probably the one you
[2124.32 → 2129.84] want is the one that is dependent upon the most by the community which works basically the same as
[2129.84 → 2136.96] the Google page rank where the site that gets the most links to it is essentially being kind of crowdsources
[2137.52 → 2143.92] the source of it's a trusted website yeah that makes a lot of sense and then that passes down as
[2143.92 → 2151.84] well so if Ruby on Rails depends upon a small library like mime types then you can pass a lot of that
[2151.84 → 2158.88] authority that Ruby on Rails is a trusted high quality project therefore if it depends upon mime types
[2159.52 → 2167.44] that must be pretty good as well even if people don't depend on it directly as much interesting and so
[2167.44 → 2174.08] with it being a discovery service you know I'm just going through the UI itself it seems like it's a
[2174.08 → 2180.32] lot of manual drilling, or you can actually search what uh how do you feel about where it's at right now
[2180.32 → 2185.92] what is the utility of going to the site and searching or poking around what is the know the
[2185.92 → 2191.36] true value there for those that are listening going there and checking it out the real valuable bits that i
[2191.36 → 2198.32] see people using is given any application you can see a snapshot straight away of all the dependencies
[2198.32 → 2204.40] without having to go poke around in different files and uh work out which versions of what thing I'm
[2204.40 → 2212.24] currently using uh and potentially any warning so you can go to if you're logged in uh, or we can look at
[2212.24 → 2220.56] the 24 pro request repo okay and basically the URL structure is libraries.io slash GitHub and then
[2220.56 → 2228.48] the name slash sorry the owner slash name so it mirrors the GitHub uh URL structure after that like
[2228.48 → 2235.84] first segment and that will show you the list of dependencies for that repo along with any potential
[2235.84 → 2243.04] warnings the licenses of those things the current latest version so you can get a good view of if
[2243.04 → 2248.56] you've got anything that's out of date or potentially has a conflicting license which is a whole area that
[2248.56 → 2256.88] I've only just started to touch on but say MIT projects that depend upon GPL uh libraries which
[2256.88 → 2264.72] is a gray area potentially means that that project needs to be re-licensed as GPL considered like a
[2264.72 → 2271.12] derivative work or that it needs to swap out that dependency with something else and for companies they
[2271.12 → 2278.64] they're kind of like license and licensing compliance stuff can cost a lot of money to have that reviewed
[2278.64 → 2285.36] manually or even get like a lawyer involved that if you can get a good view of like oh we seem to
[2285.36 → 2291.20] have like a conflicting license here let's just swap that out soon before we become really dependent
[2291.20 → 2297.60] upon that particular library I'm also noticing in the explorer area in your footer you have a buzz factor
[2297.60 → 2304.40] oh yes that's a fun term to throw around anyway it's you know so for those of you listening what
[2304.40 → 2311.12] is a buzz factor at least the way I know it is if you're the only person that has onus of something
[2311.12 → 2316.16] that if for some reason you got hit by a bus, and you couldn't come into work today how would we pick
[2316.16 → 2321.12] up and carry on is that pretty much what you mean by this exactly yeah how many people in your team
[2321.12 → 2327.12] need to get hit by a bus before the project is essentially disabled for can't move any longer
[2327.76 → 2332.00] so when you pull back this list of improve the bus factors that mean that there's
[2332.56 → 2338.48] not enough contributors not enough uh yeah so it looks at the number of contributors to that library
[2338.48 → 2345.52] which basically connects through to GitHub uh and will go, and it'll order by the projects that are
[2345.52 → 2353.76] depended upon by the most uh either other libraries or applications uh and then ordered by the number of
[2353.76 → 2359.36] the like the lowest number of contributors so most of the time it will show like here's a project that's
[2359.36 → 2368.48] depended upon by 200 uh projects and has one guy who's done all the commit which basically means if he
[2368.48 → 2378.24] stops working on it or if he decides to uh to delete it yeah because he's burnt out then that's 200 projects
[2378.24 → 2386.00] that could potentially just be made unusable so it's a good way to kind of go like ah well here are some
[2386.00 → 2394.00] places that essentially are a weak spot in your dependency tree maybe you should like to offer a helping hand
[2394.00 → 2400.40] or try and get him to share the commit bit with a few other people just to make sure that this is like a
[2401.04 → 2406.88] a key piece of infrastructure essentially in the open source world that we need to make sure continues
[2406.88 → 2412.56] to work even if uh that guy is not interested in looking after it that someone else can come along and
[2413.44 → 2418.40] make sure that continues to work okay lets uh let's take one more break uh when we come back I want to
[2418.40 → 2422.72] talk a bit about the API and the docs you have for that because it kind of dovetails from that
[2422.72 → 2428.00] conversation we just had into this because I'm thinking if you can pull back searches for bus
[2428.00 → 2433.60] factors for example you know there must be the sky's the limit so to speak if you've got you know
[2433.60 → 2439.28] enough creativity in your mind on how you can actually use libraries Io to kind of pull all
[2439.28 → 2444.88] these different dependencies and package managers to really have some fun with it so I'm imagining
[2444.88 → 2448.72] that the API is going to power a lot of that so let's take a quick break we'll come back we'll dive
[2448.72 → 2456.80] deeper into this cool project and the API of it we'll be back I have yet to meet a single person
[2456.80 → 2462.00] who doesn't love digital ocean if you've tried digital ocean you know how awesome it is and here
[2462.00 → 2469.28] at the changelog everything we have runs on blazing fast SSD cloud servers from digital ocean and I want
[2469.28 → 2476.16] you to use the code changelog when you sign up today to get a free month run a server with one gig of ram
[2476.16 → 2483.28] and 30 gigs of SSD drive space totally for free on digital ocean use the code changelog again that
[2483.28 → 2489.44] code is changelog use that when you sign up for a new account head to digitalocean.com to sign up
[2489.44 → 2490.88] and tell them the changelog sent you
[2494.00 → 2499.52] all right we're back with Andrew talking about libraries.io, and we talked a bit about the bus factor
[2499.52 → 2506.72] and what that is and interesting ways you can probe and kind of fine tooth comb what's available out
[2506.72 → 2511.92] there in the open source world, and you have this pretty awesome API can we talk a bit about
[2511.92 → 2517.44] the API what how does it work what do you expect to happen with this yeah, so there's a few different
[2517.44 → 2524.24] kind of APIs going on at the moment there's for all the searches there's a RSS feed version of the
[2524.24 → 2532.40] so you can keep track of say any new libraries that work with Twilio that are written in coffee
[2532.40 → 2540.00] script and that you could plug into your RSS feeder or programmatically consume that to find out about
[2540.00 → 2545.68] new things that happen or there's the more traditional rest API which is pretty new and if
[2545.68 → 2551.76] anyone has any feedback then or any feature requests things it's missing please do let me know because
[2551.76 → 2556.72] it's really only existed for a couple of weeks and love to get more people kicking the tires on
[2557.28 → 2561.92] that would let you potentially pull out all the information about every different library across
[2561.92 → 2567.84] every different package around here in a very standard way which is exactly how I envisioned like
[2567.84 → 2574.64] if I wanted to work on an API that worked with all these different kinds of libraries that I'd need
[2574.64 → 2580.08] some standard way of talking about them so it tries to normalize out the differences between
[2580.08 → 2585.20] different package branches and there may be some information missing for some package managers like
[2585.20 → 2593.76] Bauer doesn't really have a good concept of versioning in that everything is in git tags in GitHub
[2594.48 → 2601.52] there's no real like active publishing a new version of a Bauer library but I've tried as hard as
[2601.52 → 2607.04] possible to make it completely standard so you can essentially look at the same use the same tools
[2607.04 → 2611.20] again different package managers so if someone builds something for one
[2612.32 → 2618.64] language then it can be useful to everyone rather than kind of siloed effect of people building say
[2618.64 → 2624.32] things just for NPM all the other communities can also benefit from this kind of things
[2624.80 → 2629.04] and during the break we had a kind of interesting conversation to about uh I guess
[2629.92 → 2635.04] ways this API can be extended in just different fun things and we talked a bit about in a way
[2635.04 → 2640.06] way kind of linting a repository or a pull request whenever someone contributes back we talk a bit
[2640.06 → 2646.00] about some hypothesis some future ideas something that maybe it's not even quite there yet where
[2646.00 → 2652.84] where do you see this going yeah so the nexus of the of where I'm moving towards the kind of
[2652.84 → 2657.38] other pieces I'm trying to put into place with the deprecation warnings and the license
[2657.38 → 2661.52] conflicting warnings and the security vulnerabilities which are pretty close to getting
[2661.52 → 2669.42] shipped is to be able to do that on a snapshot of a branch or the difference between a branch and
[2669.42 → 2675.86] master so you can imagine a service kind of like Travis that hooks into your pull request and goes
[2675.86 → 2681.36] okay you've opened a new pull request to this repo you've added a dependency and let me review that
[2681.36 → 2687.14] new dependency and see if it matches the different options that your organization has
[2687.14 → 2691.62] decided like we're going to follow these so that might be we're not going to let you merge any
[2691.62 → 2698.54] new dependencies that have security vulnerabilities that match that particular version that you've
[2698.54 → 2706.66] included or that have no license uh that we can find for them or say have a really high bus factor
[2706.66 → 2711.80] like there's only one contributor to this project that's not necessarily a good thing to depend upon
[2711.80 → 2718.28] because there's no one else there to support it, and you can imagine actually having like the red green
[2718.28 → 2725.14] come out of that where it goes yes your dependencies that you're adding look fine or no they don't you
[2725.14 → 2731.48] can't merge this PR because it's red and I can see that being a really helpful thing for open source as
[2731.48 → 2740.84] well to kind of it you would at least I personally don't review every dependency that I add to an
[2740.84 → 2746.98] application manually or to look at its transitive dependencies and see like is there something that
[2746.98 → 2751.28] I should be worried about in any of these things we should be able to do that fairly automatically
[2751.28 → 2757.52] and then warn you kind of proactively don't add this thing to your application because it might cause
[2757.52 → 2763.54] you pain further down the line do you have any ideas for how someone might list or manage that
[2763.54 → 2768.40] will be there will there be like a libraries file for example almost listing somewhat, somewhat similar
[2768.40 → 2775.06] to like a gem file for example kind of saying this is what you want to keep, or we want to avoid you
[2775.06 → 2780.50] know gpl3 for example because we're MIT you know whatever it might be yeah character code or whatever
[2780.50 → 2786.18] you know however you can kind of like throw in there how is that going to work so I imagined it
[2786.18 → 2791.90] working by essentially an org level that you'd configure it inside the libraries Io dashboard
[2791.90 → 2798.62] but you could also do it on a per-repo basis with like a dot libraries Io dot YAML file very similar to
[2798.62 → 2804.18] the way traffic works where you can go like for this repo actually it's all running inside a firewall
[2804.18 → 2812.10] we don't need to worry about security related things because we this is running completely internally
[2812.10 → 2817.24] and not a problem then let's skip all the security warnings we don't need to worry about that
[2817.24 → 2825.12] or for this project it's public domain open source project it doesn't matter if there's del things here
[2825.12 → 2831.00] or whatever the white list of licensing things here as a little config file that you could overwrite
[2831.00 → 2837.04] the like the org wide setting I think it's a fascinating take towards it too I mean i really
[2837.04 → 2842.36] and I was you know I have to I have to admit I was slightly skeptical at first like okay this is a
[2842.36 → 2848.14] this is a pretty useful thing but I wasn't really sure how many people out there would actually
[2848.14 → 2852.30] you know maybe go to the site and check dependencies and then I was also going to ask questions about
[2852.30 → 2859.20] the notification process but I really see the utility in having it you know at the developer level
[2859.20 → 2863.86] where you're you know in the command line you're already you know doing pull requests you're already
[2863.86 → 2869.70] pushing to your CI server or whatever it might be and having that real-time feedback whenever you
[2869.70 → 2874.08] might be even be doing a pull request I really see a lot of usefulness in that utility part of it
[2874.08 → 2881.22] yeah you could imagine hooking that into say even into atom where it could glint the gem file as soon as
[2881.22 → 2887.80] you saved it i I haven't quite worked out if that is a feasible thing but the API would allow you to
[2887.80 → 2893.30] to do that anywhere that you would run any other kind of linter it just might take a little bit longer
[2893.30 → 2899.22] uh because it's got to go past but depending on the language some programming languages have
[2899.22 → 2907.30] really nice uh formats like all they're the manifest files are written in Jason or TOML or YAML
[2907.30 → 2915.46] other ones need like to actually run the code in the language that was written in things like Lua and
[2915.46 → 2923.14] closure all of their manifest files are written in Lua or closure which is difficult to regex out of all
[2923.14 → 2928.82] the dependencies we've been talking about a couple of these features and some of them some of them
[2928.82 → 2934.74] are there and some of them seem like they may be dreams of yours how far are we away from
[2935.22 → 2941.46] this linting world as we've been talking about it uh the linting is working internally and so
[2941.46 → 2946.18] libraries tracks its own dependencies which is pretty neat to get the project to be able to kind of eat
[2946.18 → 2954.26] his own dog food uh, and it will, it uses a lot of the webhook API uh as well so it will open an issue
[2954.26 → 2961.06] on GitHub and the webhook API is pretty poorly documented on the site at the moment, but there's a
[2961.06 → 2969.54] lot of little uh open source GitHub project on the libraries Io GitHub uh org that show you different ways
[2969.54 → 2974.90] of doing things so it will rerun its test uh automatically every time there's a dependency
[2974.90 → 2982.74] updated it will open an issue if there's a dependency that's not a pre-release that's been uh the version
[2982.74 → 2989.06] has been bumped um, and it will even potentially you could have that tweet or post to your slack room to
[2989.06 → 2994.90] say hey there's a new version of this thing I've got it tracking and kind of reviewing the dependencies
[2994.90 → 3001.06] that I add to the project itself, but it needs work mostly around the configuration of the options
[3001.06 → 3007.94] as you say like there needs to be that YAML file be able to say uh here are the things I care about which
[3007.94 → 3015.62] may not be the same as other people and I reckon it's probably another a month away before that live
[3015.62 → 3024.02] on the site so this is an open source focus, but it's not an open source project right not at the moment no
[3024.02 → 3030.34] I'm trying to work out exactly what to do with that I'm kind of halfway between the two I haven't
[3030.34 → 3038.66] landed on do I open source it all as say like a GPL or do I continue to run it as a proprietary bit
[3038.66 → 3044.82] of software a lot of the pieces of it are open source but the main rails app is currently private
[3045.70 → 3051.62] it's certainly interesting especially whenever you start talking about um I know so many developers
[3051.62 → 3057.46] and teams are using slack and obviously using Twitter so those two mentions of like tweeting to
[3057.94 → 3062.98] you know that seems somewhat okay to me but I think you know maybe a lot of ears perked up when
[3062.98 → 3069.06] you said slack integration potentially so I know for us, you know anytime we have you know here at the
[3069.06 → 3074.50] changelog we have a private kind of activity area where if things happen things get triggered and
[3074.50 → 3078.82] it's an area where jarred and i and the rest of the team we kind of keep an eye on it and those are
[3078.82 → 3083.54] like critical things happening so if those things is something gets posted there we know it's not a
[3083.54 → 3088.42] good thing it's somewhat of a bad thing, and we get on it right away so I can kind of see some utility in
[3088.42 → 3092.98] that too because you know it removes the bus factor so to speak whenever something bad happens and if
[3092.98 → 3098.98] you've got a team, and you're kind of triggering notifications back into slack or via email I'm kind
[3098.98 → 3102.82] of less interested in email because I think people get a lot of that but I think slack seems to be
[3102.82 → 3110.02] like the next better thing to an email response on a notification yeah i I haven't written a slack
[3110.02 → 3116.42] box for it yet mostly because I'm working on this on my own most of the time and I didn't feel the
[3116.42 → 3122.58] need to hang out in my own little slack room uh so i I have it open issues on GitHub for me instead
[3122.58 → 3129.06] but that's definitely something that can be built on the webhook API that's there already i just really
[3129.06 → 3135.30] need to write some documentation for the thing, and then you can have that either only post me like
[3135.30 → 3144.02] major versions or like new big versions updates or maybe even only go like I just want to post
[3144.02 → 3150.34] about any potential security vulnerabilities that are um that are announced on the things that
[3150.34 → 3156.34] any application across the whole GitHub org uh depends upon well I'm not sure if you heard about it
[3156.34 → 3161.46] yet but uh there is a brand-new repo as of yesterday when Slack made that announcement about
[3162.10 → 3167.14] um you know the app store they're having and stuff like that and this ecosystem and whatnot they also
[3167.14 → 3171.94] uh released a thing called bot kit actually I don't think it was them directly releasing it
[3172.50 → 3184.58] it was uh a team or I think it's an org on uh on GitHub and I think it's just howdy, but it's h-o-w-d-y-a-i
[3184.58 → 3192.26] and uh so on that user so it's you know that name slash bot kit is the repo, so there's a bot kit out
[3192.26 → 3197.86] there for you know a toolkit for building bot applications for slack so they may have just
[3197.86 → 3203.30] made it so much easier for you okay so maybe by the time that this podcast goes out there may be a
[3204.10 → 3211.46] libraries iOS lack bot available there you go well we love that so I mean it's also available via NPM so
[3211.46 → 3214.98] you're already familiar with that so it seems like it's you know we're actually thinking about
[3214.98 → 3219.06] doing something like that ourselves around here at the change like I was telling jerry this the other
[3219.06 → 3224.18] day I was like it would be pretty interesting that uh if we can have something where it integrated into
[3224.18 → 3230.02] slack and rather than just subscribe to what we do here at the change law between our podcast our email
[3230.02 → 3233.62] things we tweet and different stuff that we plan to do in the future I was like it'd be kind of
[3233.62 → 3238.02] interesting to be able to pipe that into some sort of slack bot and allow people to subscribe to it
[3238.02 → 3242.66] yeah, and so I think that's a fascinating way that teams are hopefully it doesn't get too
[3242.66 → 3247.86] spammy that's my only concern honestly with that if it becomes too noisy you just fuzz it out in the
[3247.86 → 3254.98] background yeah exactly so I think there's a happy medium that we have to all be mindful of and that was
[3254.98 → 3259.62] my only worry with it was like should we do this are we like just enabling you know not that we're
[3259.62 → 3266.50] spammers but are we enabling us to become known as maybe spammers because somebody integrated us and
[3266.50 → 3270.18] another person's like well I'm tired of the change log you know I don't know who knows what but
[3270.18 → 3276.10] just always got a toe line of you know too much noise not enough signal, and we always focus on
[3276.10 → 3282.58] signal around here yeah maybe having the ability to vote to have the slack button and tell you about
[3282.58 → 3289.54] episodes of the change log that are about a particular language see so I could just go i I'm not interested in
[3289.54 → 3297.54] any java uh related change log episodes um so don't tell me about that to try and reduce the amount of
[3297.54 → 3305.22] noise yeah well lets uh what else could we cover that we may not have covered well enough for libraries
[3305.22 → 3311.54] before we tail off the call um I think we've covered things pretty well so they I've not got to the point
[3311.54 → 3318.82] of I'm I'm balancing on whether to actually turn it into a real business or to turn it into kind of
[3318.82 → 3324.26] it because it's built on so much open source and the data should all be open source should it be an
[3324.26 → 3330.74] open source project uh how can I make it like continue to support itself because it gets quite
[3330.74 → 3338.10] a lot of traffic now I think yeah like 50 000 visitors a week um from Google which ends up costing
[3338.10 → 3344.02] money so I need to have some way of running it but do you have any ideas about how I could
[3344.02 → 3350.58] potentially support that a couple ideas might be to potentially find somewhere I guess not so much
[3350.58 → 3356.18] to be employed but somewhat where it's almost a partnership, so this would benefit someone
[3356.18 → 3362.02] else really greatly you know, and they may essentially foot the bill of you being the developer of it and
[3362.02 → 3365.86] kind of bankrolling, and you essentially become an employee that can have its own pros and cons
[3366.50 → 3371.14] um you might even do other ways where you have sponsored things where you're not really
[3371.14 → 3375.78] but it really kind of depends on your motives right like if is I don't know what you do for
[3375.78 → 3381.54] your day job or what you're doing for freelance or how you know earn your living so I'm an I do
[3381.54 → 3388.82] freelance um application development and performance tuning and things like that uh which is fine but
[3388.82 → 3394.98] I'd really like to spend more time on libraries uh especially that around the side kind of the area of the
[3394.98 → 3402.50] bus factor and there's also a like an unlicensed library uh page ways of producing calls to action
[3402.50 → 3409.86] for in a similar age 24 pro requests with more focus like here's some pain points in a community that
[3409.86 → 3416.26] would be solved or helped with or here are some maintainers who might need some help because they're
[3416.26 → 3423.46] completely overwhelmed by the amount of people using their project uh be able to use the harvest the data
[3423.46 → 3430.10] inside of libraries for ways kind of as a force multiplier for open source given these projects
[3430.10 → 3437.30] we know are dependent on by a lot of people can we what ways can we support that project or think like
[3437.30 → 3443.14] expose it to people so they're more aware that this project might need some help yeah it's uh it's
[3443.14 → 3450.18] borderline public service borderline you know utility for enterprise or commercial, so there's a several
[3450.18 → 3457.38] different angles for it for sure yeah yeah there's definitely that of uh of enterprises seeing those
[3457.38 → 3463.94] projects potentially as a centre of risk, and so they could if we can encourage enterprises that
[3463.94 → 3471.14] really heavily depend on those projects to maybe give some financial support or some developer support
[3471.14 → 3477.94] if they have a team of say 200 developers like and one of those developers help to maintain that
[3477.94 → 3484.26] library for a certain amount of time right would be a great way to potentially help solve this current
[3484.26 → 3490.50] and I'm pretty sure it's going to get worse the problem of open source maintainers kind of burning
[3490.50 → 3498.02] out from essentially giving out all their time for free and getting very little support back it is a tough
[3498.02 → 3504.58] problem to solve and I've heard before that if it's a hard problem to solve uh, and you're already trying
[3504.58 → 3508.26] to solve if it's good that you're trying to solve it that's also meaning that you could be heading in
[3508.26 → 3514.18] the right direction because anything that's easy isn't worth doing yeah which isn't exactly a perfect
[3514.18 → 3519.86] saying but what I mean by that is if it was easy everyone else would do it too so it could be something
[3519.86 → 3526.66] that's very profitable to you, it could be something that's um not but uh you got to put in the work to
[3526.66 → 3531.78] do it, and it seems like you're doing you're heading down the right path that's for sure so i I think that uh
[3531.78 → 3536.66] uh I don't have any particular exact advice I can give you here but what I can say is that if
[3536.66 → 3541.30] there are listeners out there that have some ideas uh how can they get in touch with you is it an
[3541.30 → 3548.42] issue they should open up or uh yes it is an open source uh GitHub repo on the libraries Io
[3548.42 → 3553.86] GitHub called support which is essentially just an issue tracker probably the best way to
[3554.66 → 3560.98] to kind of publicly put out those ideas, or you can get hold of me on Twitter cool we'll put the link to
[3560.98 → 3565.78] that repo and issues in the show notes so if you're listening now head to the show notes you'll
[3565.78 → 3570.82] see a link there to get in touch if you got some ideas I mean I think it's really, really interesting
[3570.82 → 3575.70] I'm I'm sure there's people listening to the show now thinking that's fascinating um how you
[3575.70 → 3580.42] can turn into a business that's the hard part well here's a here's a chance for you to highlight
[3580.42 → 3585.06] somebody that's been really influential to you, we asked this question on the show it's who is your
[3585.06 → 3590.90] programming hero and uh so who's been really influential to you, I was pondering this today uh
[3591.46 → 3599.78] and there are a few people, but one person stands out in my mind it who's a yes um she's a developer
[3600.66 → 3609.46] based in London, and she also helped a lot with 24 progress um a couple of years ago, and she started a
[3609.46 → 3618.66] project called code bar which is essentially a movement to help diversity and kind of underprivileged
[3618.66 → 3625.38] groups to get into programming uh focused on the UK, but she picked it off and kind of completely open
[3625.38 → 3631.62] sourced everything she was doing and has turned it into like this movement which is sweeping across
[3631.62 → 3639.06] the UK as a way of saying like how can we get more women and more uh kind of underrepresented
[3640.02 → 3650.42] groups into programming by producing lots of free um courses and tutorials and everything has been
[3650.42 → 3657.38] done and kind of she set herself up as a way that it wasn't dependent on her so it's spread, and it's
[3657.38 → 3663.06] I think she's got like five or six groups now running around the UK on a regular basis they're introducing
[3663.06 → 3668.90] more and more people into programming and I think it's just amazing if I can have that kind of
[3668.90 → 3674.74] impact yeah so I didn't catch her name exactly, but it's codebar.io if you're listening what was her
[3674.74 → 3682.66] name again a despot how do you say like spell that for me d-e-s-p-o she's on Twitter and
[3682.66 → 3689.14] GitHub as despot as well all right we're going to put a link to her Twitter account and her GitHub account
[3689.78 → 3694.82] in the show notes so if you want to check out despot I'm curious to know her full name her real name maybe
[3694.82 → 3700.18] she's being anonymous for a reason i like real names but uh if you're curious about her and
[3700.18 → 3705.78] what she's doing you can go to codebar.io, or you can check out the show notes and find her twitter
[3705.78 → 3711.22] links it's also despot so well today we're actually doing a little bit different, so this is our
[3712.26 → 3720.82] unusual holiday episode we wanted to team up two shows we did so we talked to Jonathan Rosenberg about
[3720.82 → 3726.74] Flynn uh about three or four weeks back, and it wasn't quite long enough of a conversation to have
[3726.74 → 3734.18] as a full episode so what we're doing is we're combining this 60 minute show with that 35 minute
[3734.18 → 3740.34] show so it's roughly an hour and a half, but that gives us our full length show so we've combined 24
[3740.34 → 3747.86] pull requests libraries.io and Flynn into one single awesome Christmas holiday episode so hopefully
[3747.86 → 3753.30] everybody listens to it and really enjoys it and uh at this time I'm going to take another break but
[3753.30 → 3758.02] it's just the goodbye for Andrew, but it's not the goodbye for the show so we'll take a break
[3758.82 → 3764.74] uh and when we come back we're going to be talking to Jonathan Rosenberg, but before we go on that break
[3764.74 → 3768.10] Andrew do you have anything else to say to the audience any more advice you want to share back to
[3768.10 → 3773.38] the open source community uh no just have a great uh Christmas holiday well thank you for coming on the
[3773.38 → 3777.86] call we're going to go into the break when we come back we're talking to Jonathan about Flynn very
[3777.86 → 3784.10] back if you thought harvest was only about time tracking check again fast invoicing and payments
[3784.10 → 3789.78] you can easily create and send invoices and accept payments with PayPal stripe and many more you got
[3789.78 → 3795.22] expense tracking without the mess you got an iPhone or an android app to go on the go with you snap
[3795.22 → 3800.02] photos or receipts and store them in the harvest app you can also connect favourite tools like slack and
[3800.02 → 3805.70] use chat commands to start and stop your timers head to getharvest.com and start your free trial
[3805.70 → 3810.90] and once that trial is over use our code changelog to save 50 off your first month
[3813.62 → 3818.10] all right we're back from our break here in this special Christmas holiday episode part two
[3818.10 → 3823.94] talking to Jonathan Rosenberg the creator of Flynn a next generation application platform now Jonathan the
[3823.94 → 3829.46] last time you were on the show was December 20th 2013 nearly two years ago you were on episode
[3829.46 → 3835.78] 115 most recently and then once before that again on episode 99 so it's been about two years since we
[3835.78 → 3842.74] caught up with you caught up with Flynn so kind of catch us up with the last couple of years of Flynn
[3842.74 → 3850.10] yeah so we've had several major releases uh the most recent uh was our stable channel which was a week
[3850.10 → 3858.02] and a half ago, and it is the first release of Flynn that has an updater that can just update Flynn in
[3858.02 → 3864.34] place with near zero downtime, and it's basically good to go, and you don't have to use the nightly
[3864.34 → 3869.06] like bleeding edge release anymore so what is this what is a channel when you say channel what does that
[3869.06 → 3875.14] mean think of it like uh browser release channels so like Firefox has uh several release channels
[3875.14 → 3880.58] there's a release channel there's an um like a beta channel there's a developer channel and there's a
[3880.58 → 3885.70] nightly channel we currently just have two channels we have a nightly channel and a stable channel, and we may
[3885.70 → 3891.46] like adjust that uh, but we're doing this kind of browser style rolling release model where um
[3891.46 → 3896.66] it's like release trains so you end up with a new release every um every so often currently we're
[3896.66 → 3901.78] doing it every week or two, and we're just rolling out a new update, and we're not like we're really
[3901.78 → 3907.14] concerned about version numbers we're just um just rolling stuff out, so working is all that really
[3907.14 → 3912.58] matters you're not caring about you know breaking changes in the past um yeah, so the goal here is to have
[3912.58 → 3919.22] uh backwards compatibility with the past um for now like quite a ways back so the command line tool
[3919.22 → 3923.94] will work with uh forwards and backwards, and you know like the dashboard won't break when you update
[3924.50 → 3930.82] but any API integrations that you built won't break, but we'll be adding new APIs in a backwards
[3930.82 → 3936.34] compatible fashion interesting so lets uh before we go a little bit further let's kind of break it down
[3936.34 → 3942.82] for those who didn't catch episode 115 or episode 99 which were awesome episodes uh, and you weren't
[3942.82 → 3949.86] alone you had uh Jeff Lindsey with you um is Jeff still part of the picture i I think he moved on
[3949.86 → 3957.54] like beginning of 2014 um he's been doing all sorts of other stuff with docker and so on, and we've just
[3957.54 → 3964.90] been like hyper focused on building a platform that helps you deploy your applications and is super easy to
[3964.90 → 3974.50] deploy anywhere so the um the idea is that you write code as a developer um and getting that code
[3974.50 → 3979.22] into production currently is really painful you end up having to duct tape together a bunch
[3979.22 → 3985.14] of components um that you might like want to use containers, and now you've got a whole like new set of
[3985.14 → 3990.58] challenges, and we found that a lot of people were spending a ton of time just working on the deployment
[3990.58 → 3995.38] and orchestration of their applications and so our goal is to make it as easy as possible
[3995.38 → 4002.66] to deploy your applications in a highly available fault-tolerant way and um not just stateless web
[4002.66 → 4008.58] applications, but also things like your backing stores so we have what we call a Postgres appliance which um
[4008.58 → 4013.14] it is fully highly available and if you're running across three nodes and one of those nodes fails
[4013.14 → 4018.98] it'll just keep on working, and it won't eat your data and um it's safe to use kind of reminds me a little
[4018.98 → 4023.14] bit of the conversation we had with Mitchell recently I'm sure that auto was kind of interesting for you
[4023.14 → 4027.86] to see, and it's promising a better deployment process how does something like auto-fit into
[4027.86 → 4033.70] this world is it a competing thing is that a competing ideology I'd say it's a competing ideology so
[4034.42 → 4041.70] what we have is we have this um this idea that you should not have to worry about how things are
[4041.70 → 4045.86] deployed on your servers and I know auto is doing some of that, but it's doing it slightly differently in
[4045.86 → 4050.74] that um there's a bunch of like underlying stuff that you're going to need to know about
[4051.22 → 4057.78] like um are you using nginx and how does that hook up to PHP and so on um with Flynn you may need to
[4057.78 → 4063.94] worry about that but probably not it's just going to work out of the box, and we've got uh it set up in
[4063.94 → 4068.42] such a way that you can just go to production right away, and you don't need to worry about um the
[4068.42 → 4074.82] difference between development and staging and production and so on I think auto is not concerned about
[4074.82 → 4079.86] where you're putting your stuff whereas uh it seems like Flynn is more of the platform you're
[4079.86 → 4085.22] deploying to and part of that platform you're deploying to you have the ability to deploy as
[4085.22 → 4091.94] part of this platform is that maybe a layman's version of describing it i yeah I find the whole
[4091.94 → 4096.58] space just really confusing, and we're trying to unconfused that's part of the show is to demystify some of
[4096.58 → 4103.94] this stuff yeah um so my I really don't like I haven't actually used auto I've looked at it a bit
[4103.94 → 4109.54] um if you think of something like Heroku where you're just like git pushing your app, and you don't
[4109.54 → 4114.10] need anything running on your local machine except for git in that case, but you can also use our web
[4114.10 → 4119.86] dashboard which will clone from GitHub, and you don't need to have any local development tools installed
[4119.86 → 4126.10] on your local machine in order to use Flynn um if you want you can install the Flynn command
[4126.10 → 4130.10] line tool and manage your Flynn cluster using that, but you don't have to you could just like edit your
[4130.10 → 4135.14] code on GitHub and then go to the Flynn dashboard and click deploy so if you rewind back in time a
[4135.14 → 4144.10] little bit uh since you're back uh December 30th sorry December 20th 2013 episode 115 at that time
[4144.10 → 4151.78] your page title on uh flynn.io was open source platform as a service powered by docker uh your
[4151.78 → 4156.02] page title now which to me that's just like a little quick description of like a snapshot of whom
[4156.02 → 4161.54] you are yeah, and now it says the product that ops provides the developers but then on your GitHub
[4161.54 → 4166.98] it says next generation application platform a lot of buzzwords in there a lot of confusion if you
[4166.98 → 4172.82] kind of just trace back a bit right what does all that mean okay so originally we were very much
[4172.82 → 4178.98] designed as a platform that was built around docker, and it was designed to be a bunch of components
[4178.98 → 4185.06] that were like easily composable, and you could like to use a single component without using the whole thing
[4185.06 → 4190.26] and what we found is that well a few people were interested in the idea of that very few people use
[4190.26 → 4197.30] that in practice and what people actually want we talked to many potential users and um
[4197.30 → 4202.26] people that were using what we are like prototypes and our MVPs and so on and what we found is that
[4202.26 → 4206.42] everyone just wanted something that let them deploy their apps, and they didn't really care how it worked
[4206.42 → 4212.02] um, so this is very much for if you don't actually like want to think about individual
[4212.02 → 4217.62] components flint is for you, you it's absolutely all open source and all the components are really easy
[4217.62 → 4222.90] to get wrap your head around, and you can totally modify it if you want, but you don't need to it's just
[4222.90 → 4229.94] it just works that's the idea I know before we talked a bit about fundraising and uh that line gets a
[4229.94 → 4235.14] a little bit blurred when you talk about where money's coming from was it VC funding that it was
[4235.14 → 4240.18] this private investment from the community with no obligation for return what can you talk to us a
[4240.18 → 4245.06] bit about the fundraising version that you've done and what that looks like as your company is it
[4245.06 → 4251.46] a company what is uh what is flint behind the actual software yeah sure so when we started uh we
[4251.46 → 4256.50] were not a company we were just a project that had a single web page that said we would like to build a
[4256.50 → 4262.98] platform long lines of Heroku but open source um, and you can deploy it anywhere and that really
[4262.98 → 4269.38] resonated with especially the hacker news community, and we ended up raising close to 120 000 just in like
[4269.38 → 4276.74] kind of kickstarter type thing uh in order to build that and so then we took that money, and we built our
[4276.74 → 4283.14] uh a MVP of the platform and um we actually got the whole thing working you could boot it up in a VM and
[4283.14 → 4289.30] deploy, and we decided that we wanted to like to take it much further than that to be like actually
[4289.30 → 4296.50] production ready and um and like much more full-featured so we evaluated a few options we talked to
[4296.50 → 4302.34] a lot of the original contributors and some new ones, and we found that there wasn't a lot of
[4302.34 → 4309.14] interest in putting like more kickstarter style money into it so uh around that time that was uh in uh
[4309.14 → 4316.10] uh 2014 the beginning of 2014 we applied to Y Combinator which is a startup accelerator uh in
[4316.10 → 4324.50] Silicon Valley, and we got in and so uh we took we did a seed round in the summer of uh 2014 and we
[4324.50 → 4331.78] hired a team and so Flynn is actually prime directive incorporated and we um we make Flynn which is entirely
[4331.78 → 4337.30] open source, and we will uh it's not open core it's just an open source product that you can run anywhere
[4337.30 → 4341.38] you want you don't need to pay us anything for it, and we continue to develop that and in the
[4341.38 → 4348.26] future we'll have mostly sassed products that integrate with Flynn uh in a way that doesn't
[4348.26 → 4353.86] compromise the open source nature of it I'm really interested in the process of applying to Y Combinator
[4353.86 → 4359.54] can you talk a bit about as much as you want honestly I mean from the process of actually pitching to
[4359.54 → 4364.74] you know what was the real idea they bought into because as you said it's sort of morphed over time so
[4364.74 → 4371.14] what was the pitch then yeah uh applying to Y Combinator is I guess strange is one way of
[4371.14 → 4377.54] describing it there's just a application with basically infinite questions on it and um it's
[4377.54 → 4380.74] really a flip of the coin whether you get an interview or not just because there's so many
[4380.74 → 4386.42] applications, and after you do you apply there's like an interview process where you do this rapid
[4386.42 → 4392.74] fire 10 minute interview with like three or four partners at YC um and I think what uh what they
[4392.74 → 4399.62] really liked was that we had a like a working thing that allowed you to deploy apps from GitHub
[4399.62 → 4406.74] with basically near zero friction and um that is something that they got and so that's why we got it
[4407.62 → 4413.30] is this unique to you, I mean being what you just said like is there anything else out there like
[4413.30 → 4420.10] you um there are other platforms uh I'd say the vast majority of them are limited in some way they're
[4420.10 → 4426.82] either very hard to install or like not easy to install or they most of them only run stateless
[4426.82 → 4432.58] web applications they don't have stateful services built in like our Postgres appliance I'd say just i
[4432.58 → 4436.34] don't think there's any other platform out there that is trying to do the same thing that we're doing
[4436.34 → 4442.74] which is to be that like super easy to use super easy to deploy and manage and does everything you
[4442.74 → 4448.66] need out of a platform you don't need additional tools or components uh to use with it so maybe give
[4448.66 → 4456.50] me an example of a typical Flynn production setup like uh be agnostic if you'd like to I mean I'd imagine
[4456.50 → 4463.14] people are thinking about AWS or even uh our friends at digital ocean who sponsored the changelog so we have
[4463.14 → 4466.74] an affinity towards them, but you know give me an idea of what it looks like to have Flynn in
[4466.74 → 4472.98] production what servers are actually bare metal hardware needs to be in place um what languages
[4472.98 → 4477.62] people are dealing with what are some of the things that requires Flynn to be in production what's it
[4477.62 → 4484.74] like yeah sure okay so we have a super easy installer um that basically you install the Flynn command line
[4484.74 → 4488.50] tool, but you don't actually have to use the command line to install you just type Flynn install
[4488.50 → 4492.98] and it opens up in your web browser uh from a local web server that's uh in the command
[4492.98 → 4499.06] line tool and there's an installation wizard that is very easy you can point it at AWS you can point
[4499.06 → 4505.46] it at digital ocean azure or even um give it sh credentials to a few of your own hosts so you
[4505.46 → 4511.78] if you wanted a highly available cluster you'd tell it to boot up three instances on say digital ocean
[4511.78 → 4518.34] and it would tell the digital ocean API to boot those instances up and deploy Flynn to them and
[4518.34 → 4522.18] configure it, and you'd be ready to go it would take probably about 10 minutes and most of that is just
[4522.18 → 4528.58] waiting for the instances to start and install packages and so on so how much of that is kind
[4528.58 → 4533.94] of like magic inside of it to start it off easy and how much does the developer have I guess control
[4533.94 → 4539.78] over changing that um there's absolutely control over you don't have to use the installer you can use
[4539.78 → 4545.22] that we have a script that um is much more minimal in that you can just run it on existing hosts
[4545.78 → 4550.98] um there isn't that much to configure in Flynn uh we've designed that intentionally just so that you
[4550.98 → 4556.02] don't have to think about too much it's just configured to work out of the box, and we're
[4556.02 → 4561.22] just shipping best practices with it so you get stuff like for instance uh like I mentioned Postgres
[4561.22 → 4564.98] that's just highly available out of the box you don't have to do any configuration whatsoever
[4564.98 → 4570.74] is there a reason why it's Postgres and not my sequel or something else like maybe even rethink or
[4570.74 → 4578.10] yes you know insert database name here right um so we started with Postgres because uh we wanted to
[4578.10 → 4584.10] keep uh Heroku compatibility and Heroku has Postgres as a first-class citizen so we're using Heroku build
[4584.10 → 4590.42] packs to deploy apps as well, but we'll be adding more data appliances in the future so um stuff like
[4590.42 → 4597.70] rethink dB and Regis and manga dB and all these things that um are used quite extensively uh will be
[4597.70 → 4602.82] becoming to Flynn in a way that is just as easy as our existing Postgres appliance in that you just
[4602.82 → 4609.62] say hey I need a Congo database for my app, and it sets that up for you so in your own words what is
[4609.62 → 4616.82] the problem and then the dream of the developer that is like man Flynn is awesome I love it okay so
[4616.82 → 4622.10] the problem uh i I assume you're asking like why would someone choose right like what problem is it
[4622.10 → 4628.98] solving for them yeah um I'd say that this is the um currently it is the hardest that it's ever been
[4628.98 → 4634.10] to deploy an application like think back to when you could just ftp PHP files up to a shared host
[4634.10 → 4639.30] somewhere and that worked right, and it's actually the easiest it's ever going to be to deploy apps so
[4639.30 → 4644.34] there's more and more tools you have to worry way more about security you have to worry way more about
[4644.34 → 4651.46] high availability and backups and disaster recovery and so on just because people expect way more out of
[4651.46 → 4656.58] the products that you're selling them on the internet as sass and so on even just a like static
[4656.58 → 4662.18] website needs to stay up the whole time so I'd say that is the problem that we're solving this problem
[4662.18 → 4668.82] of how do I get stuff into production and keep it up and running so when flint solves a problem that was
[4668.82 → 4675.06] designed to solve what's the dream of the developer what's that look like yeah and so that is a single
[4675.06 → 4681.30] cluster where you can just run everything whether that be a stateful app that is legacy
[4681.30 → 4686.50] in some way or you wrote internally like there are many companies out there that have um they have
[4686.50 → 4691.06] special databases that they wrote like a graph database that's specific to their use case and so
[4691.06 → 4697.22] on you can run that on flint as well as um all of their apps whether they be from like open source
[4697.22 → 4703.78] from GitHub or developed internally as internal apps or developed as customer facing stuff all of that
[4703.78 → 4709.62] can be deployed in on a single platform, and you don't need any other tools to manage that in production
[4709.62 → 4714.82] so all you have to do then is just pick where you want to host your stuff and have fun I guess is that
[4714.82 → 4721.30] right yeah absolutely um and I should mention that like there are definitely some areas where we're
[4721.30 → 4727.38] like still working on it so we're I'm currently working a lot on the security parts of flint we um
[4727.38 → 4733.78] we basically have no internal authentication and um there's uh there's a bunch of there's no user
[4733.78 → 4739.14] management and so on so we're we're working really rapidly to fill out these gaps that we see as
[4739.14 → 4745.38] barriers to adoption I was reminded when you said that of your twitter handle uh not so much your
[4745.38 → 4750.82] handle but uh your bio in your twitter, and it's like security focused computer hater I've never
[4750.82 → 4757.62] really heard anybody say that, but that's that's interesting yeah um I really think that where we are with
[4757.62 → 4764.26] computing is um it's not great it's just computers are very unreliable they don't do what you want them
[4764.26 → 4774.74] to do they're very insecure, and so I'm working on fixing that gotcha so Flynn uh in the past when you
[4774.74 → 4781.14] were on with uh with Jeff we um we talked about Dou which was something he had written, and then you got
[4781.14 → 4789.22] uh dais out there and for those out there listening now, and they're thinking okay Flynn Dou dais and xyz
[4789.22 → 4794.42] that I may not have even covered that we haven't heard of yet where does Flynn fit in what is
[4794.42 → 4801.38] the future of what Flynn is in comparison to the other options out there that promise the same or
[4801.38 → 4807.62] similar thing like platform as a service it really depends on what we're talking about here I think for
[4807.62 → 4813.46] the most part we can generalize and say that there are um there are many platforms that are
[4814.02 → 4819.38] like successors to Heroku in that they have basically the same functionality except they are open
[4819.38 → 4825.94] source or not there's some non-open source platforms that are Heroku clones that you can run elsewhere and
[4825.94 → 4832.02] so like I think of some of the ones that you mentioned as being in that bucket Dou is the one
[4832.02 → 4836.34] case where it's even more limited in that it's only designed to run on a single host, and it's very
[4836.34 → 4841.86] very minimal, but most of the other existing platforms are they're just direct copies of
[4841.86 → 4849.14] Heroku in that they run stateless web applications that serve http traffic okay, and so I guess maybe
[4849.14 → 4854.66] that makes me think about what your inspiration was then so if those seem to be successors or inspired by
[4855.30 → 4862.90] a Heroku situation what was the beginning of Flynn like for you definitely inspired by Heroku um but we
[4862.90 → 4868.90] really wanted to take it further and say hey i I got you know apps that I can deploy on Heroku or Heroku
[4868.90 → 4874.82] like platform but what about all the other stuff like my databases and like an IRC server or a mail
[4874.82 → 4880.26] server like where do I deploy those and the answer at the time was oh you spend a while writing some
[4880.26 → 4885.86] configuration management scripts that are like very specific to the host you're deploying on and you
[4885.86 → 4891.54] manage those separately and our goal is to make it so that you don't have to do that you can just deploy all of
[4891.54 → 4898.74] your stuff on Flynn when you look at the platform as a service I guess landscape if dare I even say
[4898.74 → 4902.98] that like what does it make you think of like does it encourage you more to what you're doing with
[4902.98 → 4908.18] Flin or are you like wow we've really got a know a blue ocean here because they're not thinking
[4908.18 → 4914.74] the way we're thinking what does the landscape look like to you yeah so I think I'd rather expand that
[4914.74 → 4919.06] to not just platform as a service but like there's a whole there's this whole like new infrastructure
[4919.06 → 4925.06] space um and the focus seems to be a lot on very specific tools so you have you know a service
[4925.06 → 4929.78] discovery tool or a container management tool or an overlay networking tool all these things are
[4929.78 → 4937.22] components of a well-built platform there are very few well-built platforms and if you don't have one
[4937.22 → 4941.62] of those then you're stuck kind of gluing these tools together and ends up being a lot of work and
[4941.62 → 4948.02] it's a lot of time, and it's just not as resilient as it could be we already talked about getting
[4948.02 → 4952.66] started to a degree we talked about being production ready so when you say stable channel that means that
[4952.66 → 4957.06] it is stable it does work, and you are suggesting that it should be used in production is that correct
[4957.86 → 4963.62] yeah with a few caveats so yeah we definitely have people that are using it in production um there are
[4963.62 → 4969.14] like we're certainly not bug free in that there are um people are finding issues now and then, and we do fix
[4969.14 → 4976.02] those pretty fast but um the main thing right now is that uh we don't have like multi-user support or
[4976.02 → 4981.30] the ability to run even like close to untrusted code on the platform, so there's a bunch of like
[4981.30 → 4986.18] internal APIs that are exposed that we need to lock down more um that is the main thing we're focused on
[4986.18 → 4991.86] right now is making sure that it's secure enough to be able to deploy anything that you found on GitHub
[4991.86 → 4997.62] without worrying too much about it this is sort of a slight tangent to a degree but I had it down here
[4997.62 → 5002.90] here and I can't leave this conversation without asking it which is what's a typical day in the
[5002.90 → 5006.98] life of Jonathan like you know what do you what do you do what's what's money through Friday for you
[5006.98 → 5011.54] or is it Monday through Monday I don't know is it seven days a week for you yeah no it would that
[5011.54 → 5019.46] would definitely be like Monday through Sunday okay um yeah uh so typical day looks like I have a bunch of
[5019.46 → 5025.54] GitHub emails in my inbox uh various pull requests and issues and so on, and so I do a bunch of code review
[5025.54 → 5032.50] and respond to issues um catch up with people in IRC um and then get to work on my list for the day of
[5032.50 → 5039.62] software that I'm developing um whether that be actually software writing documentation um and
[5039.62 → 5045.54] all the while like watch IRC and our internal chat for issues that come up so um we try to be super
[5045.54 → 5050.98] helpful in IRC if you have any issues with Flynn you can get a hold of us really easily um and we actually
[5050.98 → 5055.54] uh have people in different time zones, so the coverage tends to be pretty good we haven't really
[5055.54 → 5060.58] talked about the size of your team really what's the size of Flynn like these days uh we're about
[5060.58 → 5067.46] half a dozen people wow okay yeah so I guess being through Y Combinator coming out what is the
[5067.46 → 5072.42] state I guess of dare I say runway I mean that's really what it is I mean somebody's got to pay for
[5072.42 → 5077.78] your time you're worth a lot and so is the rest of your team, so there's funding there's money there uh
[5077.78 → 5084.18] what is it like on the funding side do you have a long-term partner who's like hey I'm just interested
[5084.18 → 5091.70] in the long-term future this pay me back when you get a chance or um I'd say the answer is that the
[5091.70 → 5097.86] funding ecosystem is complicated um and I don't really want to get too deep too much into the weeds
[5097.86 → 5106.74] here but uh we have no uh concerns about our runway um and hopefully with yeah we have absolutely
[5106.74 → 5111.14] no concerns about the runway we'll keep del alpine Finn for the foreseeable future some
[5111.14 → 5116.10] backstory on that uh that question to you wasn't loaded I promise, but we had a conversation with
[5116.10 → 5122.02] as I mentioned before with slave attached talking about rethink dB and jarred and I were both surprised
[5122.02 → 5128.10] by the um patience that it not so much they're not doing what they should be doing, but he just seemed
[5128.10 → 5133.54] to have investors who were like just more flexible I don't know how to describe it and then obviously
[5133.54 → 5139.46] Mickey he took a little bit of funding recently with uh hash corp, and then we also had
[5139.46 → 5145.54] the guys behind metabases on recently which was also VC funded and uh so we're seeing a trend here and i
[5145.54 → 5150.90] can't help but ask questions of like okay if you're taking investment, and you're building a company but
[5150.90 → 5156.50] you're also completely focused on open source like you are you know just not so much like a devil's
[5156.50 → 5161.94] advocate kind of thing but like how do you as a software developer navigate that world and how can
[5161.94 → 5168.02] you share or encourage other developers out there that have just as many dreams and ideas as you do
[5168.02 → 5174.26] accomplish some of their goals yeah um and okay so I think there 's's a few things that we should
[5174.26 → 5181.14] unpack here um the first one is uh VC funded open source which I think the jury is still out on there's um
[5181.14 → 5186.42] there are a lot of new companies that have been funded recently that are working
[5186.42 → 5192.42] on open source either full-time or part-time um whether they have commercial products or not
[5192.42 → 5196.50] there's also there's a whole gamut of stuff and I think the interesting question and I don't think
[5196.50 → 5201.46] it's been answered yet is what how does that play out like what are the business models that end
[5201.46 → 5208.10] up being successful because the there are very few like successful open source companies that you can
[5208.10 → 5212.74] point to that have been around for a while and I think the big one you can think of is red hat
[5212.74 → 5218.42] and they have a very like relatively enterprise centric support contract business model which
[5218.42 → 5224.34] works well for them but I'm curious to see how that that scales and whether um these new companies
[5224.34 → 5230.82] are in that that same position um we're very focused on not compromising the open source nature of the
[5230.82 → 5234.74] project so as I mentioned before we really don't want to do open core which is where you have like
[5234.74 → 5238.98] enterprise features that you're selling and you're actually selling binary software to run on
[5239.54 → 5246.26] servers and we're just not in like interested in doing that so we're we're really focused on um how can we
[5246.26 → 5253.30] uh you know be successful as a company without having to compromise the open source nature of the project
[5253.30 → 5259.62] and so far we think the answer to that is uh SAS products that are like really a huge value add
[5259.62 → 5269.06] uh to Flynn without having to um install any binary proprietary software on your computer and um
[5269.70 → 5275.38] the other thing that is worth discussing is um this like if I have an open source project how do i
[5275.38 → 5282.34] you know take it to the next level and I don't I don't know the answer to that uh I know that one answer
[5282.34 → 5290.10] is absolutely raising venture capital um it is complicated and it really depends on your
[5290.10 → 5296.66] situation like that's a very person specific thing there's yeah yeah i kind of figured that because
[5297.46 → 5302.90] it's um you know I figured with Y Combinator it would just make sense the process of going
[5302.90 → 5308.50] through that and you obviously get exposed to a lot of uh people who are willing to invest so through
[5308.50 → 5312.50] that you might come out with new connections maybe no particular ties with well I see they
[5312.50 → 5315.78] I don't know what the terms are but I think usually it's like five percent or ten percent they take some
[5315.78 → 5324.10] sort of equity, and they take uh seven percent they give you 120 000 um and the uh the big deal with
[5324.10 → 5329.14] Y Combinator is you get to go to demo day which they have a bunch of uh like early stage
[5329.14 → 5334.82] investors right and so you ends up being relatively easy compared to not going through Y Combinator to
[5334.82 → 5341.78] raise a seed round of you know a million or two or three million dollars any other particular insights
[5341.78 → 5349.54] or advice that you if you had the ear of the open source world on accepting money taking VC what
[5349.54 → 5354.50] this process is like for you anything you want to share I think that if it's important to think
[5354.50 → 5361.54] really carefully about the um the goals of the project before you're considering funding and how the
[5361.54 → 5367.78] funding will impact that so whether you can find uh investors who are willing to like to go with the
[5367.78 → 5372.66] open source nature or whether they will pull you towards selling proprietary project uh products
[5372.66 → 5380.02] which that's definitely happened so you'd mentioned that uh some particular SAS models that you have uh
[5380.02 → 5386.50] ideas for is very I'm not asking for product names or whatnot but is there anything in particular you can
[5386.50 → 5396.26] share about what the future of I guess revenue generating things will be for Flynn um is it i
[5396.26 → 5402.82] don't really I think it's I think it's too early we're like super focused right now on getting people
[5402.82 → 5409.38] happy with Flynn so if you are an um if you are like have the problem that we're trying to solve which is
[5409.38 → 5415.30] deploying stuff is too hard and takes too long, and you need something like Flynn then we're really
[5415.30 → 5423.54] interested in getting you using Flynn and that is our focus 100 and our investors understand that
[5423.54 → 5429.54] and are totally up for that, and so I think that the um the monetization will come a bit later after
[5429.54 → 5435.06] we have this really great core of community of, and we already have over 90 contributors to the open
[5435.06 → 5441.86] source project and our IRC is pretty active we're we're super interested in building out uh the user base and
[5441.86 → 5446.74] community of Flynn as we were talking a bit earlier about the day in the life of Jonathan I was thinking
[5446.74 → 5453.22] okay you got 237 open issues right now on the Flynn repo uh, so your day must be pretty busy just
[5453.22 → 5458.74] considering the traffic of issues on the project alone uh I think you mentioned the popularity
[5458.74 → 5467.06] a bit so 400 or sorry 4,025 stars uh so it's its definitely popular if you have the ear of the open source
[5467.06 → 5472.74] world to step in and help out how could you know how could uh our listeners step in and say okay
[5473.30 → 5478.58] I'm I'm interested in Flynn how can I be of service what can I do from an open source perspective to
[5478.98 → 5484.34] move things along with you yeah there's lots of cool stuff to do so um the very easiest is absolutely
[5484.34 → 5491.54] just installing Flynn and trying it out with your apps at work or your side projects and so on and um
[5492.18 → 5496.98] seeing if it works for you and if it doesn't tell us why it's not working and we really
[5496.98 → 5502.58] want to fix that uh if you actually want to commit some code or docs there's lots of stuff to do there's
[5502.58 → 5507.78] um the reason why there are so many issues is we actually uh track feature requests on GitHub too so
[5507.78 → 5512.74] there's uh we've got an easy tag on GitHub and if you just click on the easy tag you should see a bunch of
[5513.14 → 5517.70] like things that you could get done in an hour or less and um Flynn is really easy to contribute to
[5517.70 → 5522.98] is written in go, and we have a development environment that um spins up in a VM using
[5522.98 → 5528.34] vagrant so you can just um have like one command and be ready to go and work like develop then
[5528.34 → 5534.42] locally I love this easy tag it's so cool you got 52 open issues yeah I don't like that they call
[5534.42 → 5539.14] them issues either because it not doesn't mean like you got you know 230 whatever bugs out there
[5539.14 → 5545.46] it's you know the legitimate community focused conversations basically yeah absolutely this
[5545.46 → 5551.70] easy tag is fascinating though I don't know if you connected a little bit there
[5551.70 → 5556.18] or had a bit of a lag the I was just talking about the easy tag I think it's fascinating I don't
[5556.18 → 5560.82] know if I've seen that before where did you get that idea from for an easy tag um to be honest i
[5560.82 → 5564.90] don't really remember I think I've seen it in a few repos I couldn't name one off the top of my head
[5564.90 → 5571.14] um the idea though of having these like relatively small chunks of work that don't require a ton of
[5571.14 → 5577.94] knowledge and um and get you started contributing to the pro uh the project I'm I'm really excited to
[5577.94 → 5585.38] help new contributors um work on Flynn because um it's really neat to see the new perspectives and um
[5585.38 → 5590.02] there's its always nice having someone else write code for you yeah whenever you can get the community
[5590.02 → 5593.86] to step in and help out with the well the actual mission of the project is always going to be
[5593.86 → 5601.94] a good thing so yeah absolutely okay uh I guess we really haven't talked too much about language but
[5601.94 → 5607.46] I know Flynn's been written in go since the beginning am i right on saying that that's absolutely
[5607.46 → 5614.10] correct okay so having been what's about four three or four years old now the project uh yeah we started
[5614.10 → 5622.58] in um like July end of July like August uh 2013 okay so two and a half years so that's about two years
[5622.58 → 5627.78] after go was actually written maybe three years after it went public yeah I want to say we started
[5627.78 → 5633.22] with like go 1.2 or so okay and the reason why I'm asking is I'm just kind of getting a
[5633.94 → 5640.34] heartbeat on like your happiness level with go quite happy um yeah i have no meaningful
[5640.34 → 5645.46] complaints go is really great because it allows our new contributors to get up and running really
[5645.46 → 5650.66] quickly it's not a hard language to pick up um, and you can come to it from any other language so
[5650.66 → 5656.74] whether you used to program and you know you're a c kernel hacker or you wrote rails apps you can
[5656.74 → 5662.50] contribute to Flynn using the go language really easily has there been any other attraction for you
[5662.50 → 5667.78] to other languages like rust or crystal or anything else you can think of that might have drawn your
[5667.78 → 5672.02] attention not that go isn't good enough but has there been any other attraction to other languages that
[5672.02 → 5678.50] make you think man if is Flynn had been written in that it might be better I keep trying to find an
[5678.50 → 5684.82] an excuse to do something in rust um and I have like i I've been uh reading some rust projects
[5684.82 → 5690.50] recently I haven't actually written any uh that is the only like language that I think i I would be
[5690.50 → 5697.38] um that I think has a future currently in Flynn I'm always excited to see new languages that people
[5697.38 → 5701.38] are targeting at production because there 's's kind of a few different classes of programming
[5701.38 → 5707.94] languages that people develop and uh only a few of them seem to be like really like laser focused on
[5707.94 → 5713.06] use in production and I think that that is something that the go community has gotten sorted out
[5713.78 → 5718.18] if you have the ear of the go community which I'm sure you do on your own anyway not just with our help
[5718.18 → 5723.46] but uh any sort of congratulations anything in particular you want to say back to the go community
[5723.46 → 5729.46] that uh that you're excited about with go I think that just in general the quality of the community is
[5729.46 → 5736.98] great uh there's a really strong focus on just um on writing code and doing stuff with code as opposed
[5736.98 → 5744.58] to um like kind of rehashing the language um which I think is some people get upset about you know oh the
[5744.58 → 5748.66] go people aren't super interested in changing language but from the perspective of someone who's
[5748.66 → 5755.94] like using this all day every day it's an it's a solid language it has you know everyone I think there are
[5755.94 → 5761.14] like reasonable complaints about some of it, but it's um it's overall really really really easy to
[5761.14 → 5767.86] get started with and um and the quality of the tooling is pretty great I think the last thing
[5768.42 → 5775.46] that uh that is problematic and go is the whole like rendering and package management situation but
[5775.46 → 5780.66] they are finally sorting that out so in the next few releases we should have that like totally fixed
[5780.66 → 5784.82] did you happen to make it to go for con this past year I did not unfortunately
[5784.82 → 5790.42] do you have done you make it to any go for con I know I've never been to go for con I haven't
[5790.42 → 5795.06] I've mostly been holed up working on fly and I haven't too busy right yeah I haven't really been
[5795.06 → 5801.78] out to any conferences uh the first conference i uh I'm going to um this year is uh at the end of
[5801.78 → 5807.38] the year 32 c3 I'd be really interested to uh because we plan to be a part of go for con next year
[5807.38 → 5812.82] I'd be really interested to see um a talk submitted from you on just a lot of the stuff you've done
[5812.82 → 5816.18] because I mean it seems like you're solving fascinating high level problems that
[5816.98 → 5821.54] that uh you can share a lot back to the community and when we were there it was really
[5821.54 → 5825.06] interesting, and you know a lot of the things you're saying about the go community we saw that
[5825.06 → 5830.58] firsthand so you know you have that perspective without going to the go conference you know
[5831.14 → 5836.66] yeah absolutely I'm definitely going to consider what conferences to submit talks to this upcoming year
[5836.66 → 5843.54] cool well all right let's let's tell the show then so GitHub.com slash Flynn is the org on Flynn
[5843.54 → 5852.58] you got flynn.io so that's f l y n so two n's dot i o and i never even mentioned this but your
[5852.58 → 5857.14] your tagline on the home page is just stunning throw away the duct tape say hello to Flynn
[5858.02 → 5863.70] yeah just in retrospective of our conversation here it's its fitting very fitting thanks and then
[5863.70 → 5872.18] you're also available on Twitter at titanous that's t-i-t-a-n-o-u-s twitter.com of course
[5872.98 → 5876.74] so Jonathan thanks so much for taking the time to come back on and just catch us up with what you're
[5876.74 → 5881.86] doing I'm super encouraged what's going on is there anything else you want to cover before we close out
[5882.50 → 5885.78] no, thanks for having me oh you're welcome it's uh it's a pleasure to have you back on the show
[5885.78 → 5889.46] uh in that case let's go ahead and say goodbye then bye everyone bye
[5894.66 → 5902.10] Te her
[5902.58 → 5908.08] выш
[5911.36 → 5915.30] TWO
[5920.74 → 5921.32] 2
