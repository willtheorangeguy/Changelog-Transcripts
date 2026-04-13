[0.00 --> 18.54]  Welcome to the ChangeLog episode 0.4.8.
[18.78 --> 19.80]  I'm Adam Stachowiak.
[20.00 --> 20.96]  And I'm Wynne Netherlump.
[21.22 --> 22.20]  This is the ChangeLog.
[22.24 --> 23.94]  We cover what's fresh and new in open source.
[24.40 --> 27.32]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.62 --> 28.40]  We're also up on GitHub.
[28.40 --> 28.52]  Yep.
[29.02 --> 30.64]  Head to github.com slash explore.
[30.72 --> 34.88]  You'll find some training repos, some feature repos from the blog, as well as our audio podcast.
[35.14 --> 38.04]  And if you're on Twitter, follow ChangeLog Show and me, Adam Stach.
[38.40 --> 40.88]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.28 --> 43.00]  This episode is sponsored by GitHub Jobs.
[43.10 --> 45.88]  Head to thechangelog.com slash jobs to get started.
[46.20 --> 50.76]  If you'd like us to feature your job on the show, select advertise on the ChangeLog and we'll take care of the rest.
[50.96 --> 57.08]  The folks at PandaStream need a special dev who's at ease with Ruby Redis, MongoDB, and Beanstalk in production.
[57.08 --> 62.06]  Preferably in the U.S. as a remote worker, but also in London, if you happen to be there.
[62.38 --> 65.30]  If you're interested, lg.gd slash 6z.
[65.30 --> 73.40]  And if you're an Objective-C, Coco, or iOS dev that likes working with really smart people, check out Mutual Mobile based in Austin, Texas.
[73.52 --> 74.26]  They want to talk to you.
[74.58 --> 76.86]  Check out lg.gd slash 82.
[77.68 --> 85.08]  And Store Envy, a.k.a. the Tumblr for e-commerce, is looking for a senior Rails dev with JavaScript, Redis, M-Cache-D, and MySQL chops.
[85.08 --> 88.86]  If you're interested, lg.gd slash 6l.
[89.38 --> 92.56]  Store Envy made those awesome ChangeLog tees we handed out at South By last year.
[92.76 --> 93.86]  Those are awesome tees, man.
[94.08 --> 97.20]  Now we're eagerly awaiting our stickers from Sticker Mule.
[97.80 --> 98.58]  Die-cut stickers.
[99.24 --> 100.84]  Can't wait to put one of those on my Mac.
[101.44 --> 105.66]  I've got my recent sticker, my Hubcap sticker.
[105.94 --> 107.28]  I got my Hubcap sticker, too.
[107.50 --> 107.90]  Yeah.
[108.40 --> 109.44]  From our buddy SF Eric.
[109.94 --> 110.92]  Eric, Michael's over.
[111.86 --> 113.56]  So who did we talk to this week, when?
[113.56 --> 120.16]  I talked to Koskay and Andrew from the Jenkins Project, formerly Hudson, about their continuous integration server.
[120.80 --> 121.34]  Very cool.
[121.86 --> 124.38]  One of those great tools lets you know who broke the build.
[124.74 --> 125.52]  Who broke the build?
[125.62 --> 128.64]  Almost a little like C.I. Joe with GitHub's project.
[129.00 --> 129.32]  Yeah.
[129.76 --> 130.68]  Cool name of that one.
[131.10 --> 131.34]  Yeah.
[131.82 --> 132.62]  Knowing is half the battle.
[133.02 --> 133.78]  Knowing is half the battle.
[133.88 --> 136.46]  So Jenkins, they went through a rebrand recently, a rename?
[136.76 --> 137.06]  Yeah.
[137.06 --> 146.76]  So we talked a little bit about the controversy there and how they kind of parted ways with Oracle and the corporate backing they had when the project was named Hudson.
[146.92 --> 151.12]  And now pretty much the whole core team has moved on as the name Jenkins.
[151.48 --> 156.06]  So we talked about that and a little bit about what you would use Jenkins for.
[156.58 --> 156.96]  Sweet.
[157.82 --> 158.34]  Fun episode.
[158.42 --> 158.94]  Should we get to it?
[159.12 --> 159.78]  Let's do it.
[159.78 --> 172.20]  We're chatting today with Kosky and Andrew from the Jenkins team.
[172.38 --> 176.48]  So I'm going to let you guys introduce yourselves and a little bit about what you do with the project.
[176.60 --> 177.66]  So Kosky, why don't you go first?
[178.20 --> 178.52]  Okay.
[178.52 --> 184.20]  So I guess I'm the creator of the original Hudson slash Jenkins project.
[184.80 --> 187.16]  And I've been involved with it ever since.
[188.04 --> 188.60]  Andrew?
[188.60 --> 188.68]  Andrew?
[190.20 --> 195.08]  I'm a dope guy here at Cloudera and a contributor to Hudson.
[195.38 --> 196.02]  Sorry, no.
[196.22 --> 198.24]  Jenkins, core, and plugins.
[198.52 --> 200.74]  And I've been for almost two years now.
[201.44 --> 203.16]  So I bet you we do that a lot on this call.
[203.64 --> 204.56]  Hudson to Jenkins.
[204.88 --> 215.28]  So for those that might be confused, who wants to give a little backstory before we jump into what Jenkins actually is around its history as Hudson?
[216.26 --> 216.54]  Right.
[216.64 --> 216.92]  Okay.
[216.92 --> 219.24]  So I think I can take that.
[220.08 --> 223.76]  So, well, I was working for some microsystems for quite some time.
[223.84 --> 224.84]  I think nine years now.
[225.12 --> 226.30]  Well, nine years or so.
[227.14 --> 231.14]  And, well, I'm a guy who just enjoy writing programs.
[231.14 --> 234.04]  So my day job didn't keep me busy enough.
[234.04 --> 237.18]  So I have all these projects that I'm doing for hobby.
[238.10 --> 241.70]  And the Hudson was one of those that I started around 2004.
[241.70 --> 245.42]  And, well, like I said, I have many other projects.
[245.42 --> 251.62]  But this one, for some reason, got traction, I guess, both inside the company and outside.
[252.62 --> 255.04]  And so I sort of gradually grow from there.
[255.18 --> 260.48]  And I think over the years, it attracted a lot of users as well as the developers.
[260.48 --> 264.68]  And then so we are now, you know, a very modest size project now.
[265.44 --> 268.40]  So I think that's sort of the brief history of the project.
[268.40 --> 270.78]  How many users do you think you have?
[272.06 --> 272.54]  Yeah.
[272.62 --> 274.46]  So we actually have some means.
[274.70 --> 284.22]  So the Hudson or Jenkins now has a mechanism to sort of ping back our server because that's how they get updates.
[284.78 --> 286.72]  And then we also collect anonymous usage statistics.
[287.52 --> 291.38]  And so that gives us some sense of how much the project is used out there.
[291.38 --> 294.74]  So I think we haven't tallied the number for a while.
[294.82 --> 304.70]  But the last time we checked, which was around, I think, the last summer, I think we are estimating about 26K to 30K installations worldwide.
[305.16 --> 305.98]  That's fantastic.
[306.28 --> 307.00]  Yeah.
[307.06 --> 312.16]  So given that each one is a server app, I think we have probably like about half a million users right there.
[314.02 --> 314.46]  Yeah.
[314.46 --> 319.80]  Those were real installations that we saw multiple times that had actual projects on them,
[319.80 --> 323.36]  and not just somebody spinning it up locally to take a look at it.
[323.42 --> 325.14]  Those were real production instances.
[326.34 --> 329.30]  So this podcast covers a wide range of listeners.
[329.50 --> 333.30]  For the uninitiated, explain a little bit about what continuous integration is.
[333.88 --> 339.80]  To me, I guess the ultimate summary of the CI is like, well, we want to be, we, the human beings, want to be lazy.
[340.68 --> 348.32]  And so everything, so the program like CI is really just doing everything that the machines can do.
[348.32 --> 353.02]  And they free us up for, you know, the kind of things that only we can do.
[353.96 --> 356.52]  But, so that's like the ultimate long-term goal.
[357.30 --> 370.62]  And I guess, but in the meantime, at the more short term, what the most of the users are using Jenkins for is basically having the servers build your program and test them.
[370.62 --> 379.82]  And also perhaps like deploy to your, you know, the target environment or do some other peripheral automations.
[379.82 --> 383.86]  I think reporting on the builds and tests.
[384.28 --> 384.64]  Oh, yeah.
[384.78 --> 384.98]  Yeah.
[384.98 --> 392.20]  Is probably the biggest visibility thing for Jenkins.
[392.52 --> 394.32]  Just that you can see what happens with the builds.
[394.44 --> 396.34]  You can see what happened in previous builds.
[396.58 --> 401.06]  You can see how many tests failed this build versus previous build, et cetera.
[401.06 --> 402.06]  Right.
[403.74 --> 407.16]  It sort of gives more visibility into the current state of the project.
[407.34 --> 414.38]  I think what used to happen in some a lot is, you know, there are people who occasionally, well, if you take vacations and so on.
[414.88 --> 422.52]  And then often those are the only people who knows, like, which branch you're supposed to be committing or, like, whether the tests are supposed to be passing or failing.
[422.52 --> 430.20]  So when we didn't have Jenkins before, those information are basically hardcoded into people's brain.
[430.86 --> 444.74]  And now with applications like the CI service in general, but Jenkins in particular, when you have those data available on the web application, it's much easier for the managers and so on to get some sense of what's going on.
[445.96 --> 450.88]  Jenkins also offers a lot of features that are useful for management type of people, too.
[450.88 --> 456.02]  Like, you have the clouds that you display if a project isn't building well.
[456.58 --> 456.82]  Yeah.
[458.14 --> 458.62]  Yeah.
[458.72 --> 462.22]  We actually took some heat for some of the more visibility stuff.
[462.34 --> 466.76]  I guess the managers back then didn't really know how horrible our state of the programs are.
[467.78 --> 480.86]  The engineers kind of got away with that, that there is this stuff that, you know, so when I put, I actually built the, at one point, so one of the things that Jenkins has is this color org that represents, like, the latest.
[480.88 --> 482.88]  So if it's blue, it's good.
[482.88 --> 484.42]  And if it's red, it's bad.
[484.98 --> 489.48]  So at one point, this physical device that actually shows it and put that in the coffee room.
[490.28 --> 494.30]  And so what happened was that the manager got scared that it's red all the time.
[495.58 --> 502.46]  My fellow engineers, they didn't like the idea because, you know, the managers aren't supposed to see that.
[502.46 --> 510.68]  So can you go over some of the things that makes Jenkins stand out versus the other continuous integration servers that are available?
[510.98 --> 518.78]  For example, it's written in Java, and so you can deploy it anywhere, but people use it for projects that have nothing to do with Java.
[519.16 --> 521.70]  And can you, like, go over the plug-in system?
[522.16 --> 524.32]  I think that's one of your biggest features right there.
[524.32 --> 524.60]  Yeah.
[526.00 --> 527.22]  Andrew, do you want to take that?
[527.34 --> 531.14]  Because I think he's been deploying Jenkins in pretty interesting ways.
[531.32 --> 531.86]  I think he can.
[532.64 --> 538.72]  Because out of the box, with the plug-ins you install, you can pretty much do anything that you could ever need 85% of the time, right?
[539.40 --> 544.50]  Yeah, I think the plug-in architecture and ecosystem is really what sets Jenkins apart.
[544.50 --> 548.34]  It's so easy to get going writing a plug-in.
[548.56 --> 551.14]  If you know any Java, you can figure it out pretty quickly.
[551.82 --> 553.20]  And you can also write them in Groovy.
[554.24 --> 559.04]  And now there's work on writing them in JRuby as well.
[561.18 --> 568.14]  So there's so many extension points to build off of so that if you've got a test tool you want to do reports on,
[568.14 --> 576.42]  a coverage tool, static analysis, there's easy ways to integrate that, either using existing plug-ins,
[576.48 --> 580.68]  or if you've got something new that's not out there, you can write something yourself very easily
[580.68 --> 587.00]  and then publish it through the Jenkins Update Center to get to all the other Jenkins users out there.
[589.24 --> 594.98]  So that's what pulled me in originally, was that I started playing with Jenkins
[594.98 --> 600.74]  and needed a change to the ClearCase plug-in, and next thing I know I'm the ClearCase plug-in maintainer.
[601.42 --> 606.88]  And then writing more plug-ins any time there's something else I know that's not there that I'd like to have there.
[607.48 --> 617.34]  And that ease of use and that ease of extensibility is really great as a build hacker, as a tools guy.
[618.50 --> 622.82]  Being able to improve your tools on the fly is fantastic,
[622.82 --> 628.78]  especially compared to a large commercial build management server that doesn't really expose its data,
[628.88 --> 631.02]  that doesn't really encourage you to improve it.
[632.04 --> 633.06]  It's night and day.
[634.42 --> 638.70]  Yeah, it's really helped us that our users are also developers.
[638.96 --> 645.52]  So when they find some missing things, as long as we provide a means for them to scratch their own, which they do.
[645.52 --> 652.74]  I think that's really the part of the success of the Jenkins is that this plug-in system that allows people to, you know,
[652.78 --> 654.60]  just scratch their own little itch.
[655.50 --> 658.00]  And so all the time, I think people have...
[658.00 --> 662.00]  Well, so I had to spend a lot of time, actually, to get that infrastructure in place.
[662.08 --> 665.78]  But once that's in place, the people showed up in mass and then wrote the plug-in.
[665.78 --> 676.90]  I think we have today about, like, 300 plug-ins that's covering not just Java, but PHP, Ruby, Python, .NET, C++, and what have you.
[677.40 --> 679.12]  Did we actually have, like, a COBOL plugin?
[680.42 --> 685.10]  Somebody was talking about a COBOL plugin, but that kind of terrified me as a concept.
[687.04 --> 691.88]  I'm just blown away continuously when I'm using it, how easy it is to set anything up.
[691.88 --> 694.74]  Like, I was discussing internally.
[695.06 --> 699.24]  I was on an IRC channel that we created for my organization, and they were just like,
[699.32 --> 702.42]  yeah, some people use this for, you know, reporting builds.
[702.60 --> 703.22]  And, like, within...
[703.22 --> 708.20]  I think it took me, like, two minutes from start to finish to get it to push every test up, you know,
[708.30 --> 709.74]  report it into the IRC channel.
[709.82 --> 710.52]  It's just amazing.
[710.94 --> 711.10]  Yep.
[712.18 --> 712.52]  I love it.
[712.52 --> 717.76]  The barrier to get going with pretty much anything is almost nil.
[717.76 --> 725.76]  When you compare that to some of the other CI tools out there, you know, the older ones with it have...
[725.76 --> 727.84]  You've got to go edit files from the server, et cetera.
[728.02 --> 728.54]  I love it.
[728.82 --> 734.48]  I think if you just run the war file and then everything's pretty obvious and pretty right there.
[735.50 --> 739.56]  And it supports every version control system there is ever, right?
[740.34 --> 742.72]  It supports ones that it really shouldn't, yeah.
[742.84 --> 743.62]  We support...
[743.62 --> 745.50]  There is a plugin for visual sources.
[746.10 --> 747.14]  I don't know why.
[747.14 --> 753.66]  Last I checked in the last few steps we looked at, I think there were, like, 10 people who had it installed.
[753.92 --> 754.56]  That's amazing.
[754.70 --> 755.06]  I don't know why.
[755.50 --> 757.78]  I still get, like, the bug reports on that one.
[758.00 --> 759.52]  So I know people are using it.
[760.42 --> 763.00]  Well, the biggest bug on that one, of course, is that it's visual sourcing.
[763.22 --> 763.74]  But, yeah.
[766.86 --> 769.96]  And so people use it for other things other than just writing tests, right?
[770.04 --> 774.02]  You can push, you know, deploys and everything else with it.
[774.04 --> 775.12]  You have parameterized builds.
[775.94 --> 776.12]  Yep.
[776.12 --> 786.42]  Back in my previous job at DIG, we used it for pre-testing commits, you know, when they get submitted for review.
[786.42 --> 797.74]  And then an automated deployment, you know, continuous deployment process such that anytime anything changed and passed the test, it would keep going through to be tested against other things until it ended up live.
[798.24 --> 803.00]  So that theoretically the only human intervention you needed was writing the code and reviewing the code.
[803.00 --> 807.24]  Yeah, anything you can script, you can do through Jenkins.
[808.18 --> 808.54]  Right.
[808.62 --> 813.56]  So, in fact, one of the ways that Jenkins is described is, like, as a glorified Chrome.
[813.56 --> 816.96]  So, anything that you can do, you know, you can do that.
[816.96 --> 820.00]  You can do that at certain point or scriptable.
[820.40 --> 821.86]  You can run it from Jenkins.
[822.12 --> 824.56]  And it's normally better to do so than doing it from Chrome.
[825.44 --> 826.70]  You get the notifications.
[827.02 --> 829.36]  You can retry at your own choosing if you want to.
[829.70 --> 834.68]  You know, you can script the choreograph multiple things, emails, et cetera, et cetera.
[834.68 --> 839.74]  So, Jenkins predates GitHub, right?
[843.04 --> 844.14]  I'm not sure, honestly.
[844.26 --> 845.96]  I don't know exactly when GitHub came along.
[846.08 --> 848.40]  So, when did you start the Hudson project?
[849.18 --> 850.02]  That's 2004.
[850.86 --> 851.14]  Yeah.
[851.38 --> 852.98]  So, I think GitHub came along.
[853.18 --> 854.22]  It lapsed it a couple times.
[854.66 --> 854.96]  Yeah.
[855.54 --> 857.06]  So, what does GitHub meant?
[857.28 --> 859.88]  So, I'm assuming you added source control prior to GitHub.
[859.88 --> 864.62]  What does GitHub meant as far as building community and getting community buy-in?
[864.84 --> 866.38]  Around Hudson, now Jenkins.
[868.14 --> 870.84]  Well, pull requests, obviously, are fantastic.
[873.90 --> 881.80]  It's so easy to take fixes from somebody else rather than having to worry about getting them to put a patch on Jira
[881.80 --> 887.10]  and then having to apply it and make sure that we've got the right versions against it, et cetera.
[887.10 --> 895.82]  Well, with pull requests, somebody can just go fork it, make their change, submit, commit it, push it, and then send it a pull request.
[896.26 --> 897.86]  And we've got what we need.
[897.86 --> 909.44]  So, to me, one of the most important aspects of the project was how to make it easier for other people to come join the development of the project.
[910.30 --> 919.16]  So, even when we were using Subversion, we had this interesting committer policy that everyone can just become a committer just by asking.
[919.16 --> 930.06]  Whereas in normal, more mainstream open source project, you normally have to first prove yourself, you know, hanging around long enough and sending in patches before you are accepted.
[930.06 --> 934.88]  So, we tried various things in an attempt to lower the barrier to entry.
[935.04 --> 940.28]  And then, to me, the Git or the GitHub is like, you know, the natural next step to that end.
[940.54 --> 943.64]  Because then people could just fork a repository and then make some changes.
[944.12 --> 947.60]  And it makes it easier for us to see those and integrate them back.
[947.60 --> 956.60]  So, you know, when we saw GitHub, initially, I have to say, I wasn't quite ready to move the code.
[956.74 --> 961.04]  But over the time, I think we sort of saw the light.
[961.26 --> 964.70]  And then we became an integral part in my mind.
[965.40 --> 968.58]  So, we need you guys to tell your buddies about GitHub.
[968.84 --> 970.34]  We love GitHub.
[970.48 --> 972.48]  And we would like to cover more Java on the show.
[972.48 --> 980.92]  The problem is a lot of these code repositories that are popular outside of the GitHub community just make it difficult to peer into the community and see what's hot and not.
[981.00 --> 984.44]  I'm looking at the top languages on GitHub right now, github.com slash languages.
[985.06 --> 988.22]  And Java weighs in at 6% of the projects.
[989.18 --> 990.62]  So, why do you think that is?
[995.02 --> 995.70]  Yeah, okay.
[995.84 --> 996.40]  Andrew, go ahead.
[996.40 --> 1008.68]  I think part of that is you've got the really big Apache Java projects all already, you know, have their own repositories outside of GitHub historically.
[1009.76 --> 1021.26]  So, that's some factor considering how much of the Java open source ecosystem consists of Apache tools and libraries, et cetera.
[1024.00 --> 1025.98]  But I'm not entirely sure, honestly.
[1025.98 --> 1030.46]  It may just be that Ruby and Python people write too much code.
[1033.00 --> 1034.20]  I can attest to that.
[1035.16 --> 1038.88]  So, speaking of, I'm going to drop a – you guys are still online.
[1039.24 --> 1043.22]  I'm going to drop a graphic that you've probably seen in our chat here.
[1044.70 --> 1050.14]  How language programmers view programmers from different languages.
[1051.10 --> 1052.28]  I'll drop this in for you, Andy.
[1052.30 --> 1053.34]  Paste that into the show notes.
[1054.10 --> 1055.66]  You'll have to paste this into the show notes.
[1055.98 --> 1058.56]  Do you guys remember seeing this?
[1059.70 --> 1060.68]  If it's the same thing.
[1063.00 --> 1063.90]  Let me take a look.
[1070.38 --> 1071.28]  That's kind of funny.
[1071.28 --> 1075.06]  So, is that how you see us?
[1075.14 --> 1076.50]  Do you see us as the –
[1076.50 --> 1077.96]  Well, which one are you, Ruby?
[1078.70 --> 1079.68]  Yeah, I'm Ruby.
[1079.92 --> 1080.54]  Kenneth's Python.
[1081.30 --> 1082.24]  At least you're not PHP.
[1082.78 --> 1085.20]  Yeah, Kenneth, I guess you're not represented here.
[1085.26 --> 1086.42]  Probably closer to Ruby.
[1087.84 --> 1088.38]  So, I'm a super fray.
[1088.38 --> 1089.32]  No, Python isn't even on there.
[1089.48 --> 1089.76]  That's –
[1089.76 --> 1091.72]  That's because it doesn't need to be mentioned.
[1091.92 --> 1093.54]  It's just on the whole other plane.
[1093.54 --> 1094.50]  Above the fray, as it were, huh?
[1094.50 --> 1095.32]  Yes, exactly.
[1096.98 --> 1099.88]  Hey, by choice, I'll take closure over anything else.
[1099.96 --> 1101.20]  Give me my lists, and I'm fine.
[1102.26 --> 1105.92]  You know, we want to give more closure and Scala on the show as well.
[1106.16 --> 1106.82]  So, we need –
[1106.82 --> 1108.96]  Don't those both fall underneath the Java realm, though?
[1109.16 --> 1109.64]  They do.
[1109.80 --> 1110.12]  They do.
[1110.22 --> 1111.98]  So, we need you guys to hook us up with –
[1111.98 --> 1113.58]  Oh, okay.
[1114.12 --> 1116.92]  Well, I mean, I guess you could call JRuby in that regard as well.
[1117.06 --> 1122.60]  But I need you guys to hook us up with the cool projects in these communities so that we can showcase them on the changelog.
[1123.18 --> 1123.52]  Sure.
[1124.36 --> 1125.68]  So, this whole –
[1125.68 --> 1130.00]  You're talking about how Git is fostering the community, or GitHub and Git.
[1130.48 --> 1132.60]  Isn't that what triggered this whole Oracle debacle?
[1135.08 --> 1136.20]  Yeah, it's one of the things.
[1136.52 --> 1138.70]  It's one of the triggers, yeah.
[1138.70 --> 1146.52]  The community deciding to migrate off of Oracle's infrastructure onto GitHub?
[1147.72 --> 1156.88]  That probably wasn't the underlying cause, but definitely the straw that broke the camel's back, probably.
[1158.88 --> 1168.68]  Yeah, back in November, we'd had some very preliminary talks before that point about our infrastructure situation.
[1168.70 --> 1173.54]  About eventually wanting to move more to GitHub.
[1174.32 --> 1180.42]  I'd already started doing my plug-in development with any new plug-ins in GitHub as of the spring.
[1180.42 --> 1187.04]  So, you know, we'd have some talks about that, like, you know, why change was not broken, that sort of thing.
[1187.04 --> 1205.44]  And then the Java.net repositories, mailing lists, and the rest of the infrastructure went down while they were moving it all over to new infrastructure and a new framework, Oracle, moving it.
[1205.44 --> 1209.72]  And then, you know, without really communicating well with us, that that was happening.
[1209.86 --> 1212.58]  And so we weren't sure what that meant.
[1212.68 --> 1218.10]  And we started, you know, trying to make sure we had the source on GitHub so we could keep working.
[1218.24 --> 1222.78]  Tried to make sure we had Google Groups so that we had a communication mechanism, et cetera.
[1222.78 --> 1227.46]  And then there were conflicts stemming from that.
[1229.10 --> 1229.28]  Yeah.
[1230.18 --> 1231.84]  So then – oh, go ahead, sorry.
[1232.74 --> 1234.26]  No, go ahead.
[1234.88 --> 1236.38]  So what's the current status?
[1236.48 --> 1241.36]  I feel like a lot of people are confused because they're calling Jenkins a fork of Hudson.
[1241.58 --> 1246.50]  When really the Oracle's continued Hudson development is actually a fork of Jenkins, right?
[1246.50 --> 1249.02]  That's what I feel.
[1250.34 --> 1262.66]  As I've said in a couple posts and emails, that whichever project it is – whatever project it is that Cosgate is working on, that's the real project to me.
[1262.78 --> 1268.50]  I mean, he's too modest to say this himself, but seriously, he's the project.
[1268.60 --> 1271.90]  He's written like 85% of the code of core.
[1271.90 --> 1290.32]  I mean, he's done remarkable work here, and I can't see a situation where the majority of the community says we want to go rename Jenkins and Cosgate as part of that, where I can't see that being the fork versus the one that's kept the name, but that's about it.
[1290.32 --> 1303.64]  And I should also point out that we spit for – I guess we did the voting to get the feeling and get to see where the community – how the community feels.
[1304.70 --> 1310.54]  And so the result of that was likely more than 90% of people were favorable.
[1310.54 --> 1319.80]  214 voters, available voters, people who had been on the mailing list before the vote started, voted to – renamed to Jenkins.
[1320.04 --> 1325.24]  14 voted to stay with the status quo under Oracle Central.
[1326.24 --> 1326.60]  Right.
[1326.60 --> 1340.66]  So I guess my argument is that, well, if the 93% of, well, let's say, well, the people are moving us to Jenkins, well, and they call that a fork, I don't know.
[1340.94 --> 1344.38]  I don't know how you – I think that's not a fair description.
[1345.02 --> 1347.12]  Is there going to be any code sharing between the two projects?
[1347.96 --> 1348.52]  We'll see.
[1348.52 --> 1358.56]  I don't – I honestly – I mean, we – in our talks with Oracle, again, when this actually ended up happening,
[1359.12 --> 1364.62]  they made it very clear that renaming was not saying we want nothing to do with Oracle.
[1364.86 --> 1374.26]  It was just saying that because Oracle claims a trademark on the name Hudson, there were restrictions that that put on the project.
[1374.26 --> 1379.40]  We didn't have a guarantee that we'd be able to use the name regardless.
[1379.64 --> 1388.12]  You know, we weren't an independent – we weren't able to be a truly independent project while we were beholding to Oracle for the rights to our name.
[1388.58 --> 1398.60]  So I felt that – and Kofsky agreed, and apparently most of the community agreed – that we needed to change the name so that we could be an independent project.
[1398.80 --> 1401.16]  That was not saying that Oracle shouldn't be involved.
[1401.16 --> 1408.04]  We still offered the third seat on the interim board, governance board, to Oracle.
[1408.84 --> 1419.94]  I really wish Oracle had wanted to and been willing to work with the Jenkins community, but that's not what they opted for.
[1420.02 --> 1424.16]  They opted to – I guess.
[1426.04 --> 1428.72]  Let's see if there's – you know, what code is shared.
[1428.72 --> 1432.68]  I mean, I don't know what all they'll end up doing.
[1432.84 --> 1442.80]  I don't know what all they'll be able to take from us and vice versa based on licenses or copyright or community, you know, licensing agreements, et cetera.
[1446.38 --> 1452.54]  Hopefully we can stay compatible as long as possible.
[1452.54 --> 1458.84]  Hopefully they – you know, never know, maybe they'll be willing to play ball eventually.
[1459.22 --> 1461.04]  We're not trying to push them away.
[1462.36 --> 1467.82]  We're trying to just make sure that it's a healthy, stable, vibrant, independent project.
[1468.62 --> 1478.54]  So Matthew McCullough on Twitter, you've answered part of his question, wants to know if there will be any effort to migrate existing plug-ins from using the Hudson name to the Jenkins name.
[1478.54 --> 1478.98]  Yes.
[1478.98 --> 1479.58]  Yes.
[1479.58 --> 1479.74]  Yes.
[1480.68 --> 1483.72]  But it's probably going to be piecemeal.
[1484.14 --> 1494.52]  It'll probably be when there's a reason to release a new version of the project, of that plug-in, besides just changing the name, then do a new release.
[1494.52 --> 1508.20]  I know that for my plug-ins, I'm at least looking into that, but it's not – functionality matters more than cosmetics on a plug-in level, I think.
[1508.64 --> 1514.02]  As long as it says Jenkins, you know, at the top banner, you can tell that you're on Jenkins.
[1514.02 --> 1521.40]  I think that it's permissible if one plug-in doesn't quite get all the names exactly right, right away.
[1522.64 --> 1529.90]  And we don't want to make everybody have to reinstall new versions of their plug-ins just to get a purely cosmetic name change.
[1529.90 --> 1545.86]  But over time, I'm sure that will – that more and more of the – as plug-ins get modified, as new releases come out, that the Hudson name will fade out from the plug-ins.
[1546.60 --> 1551.02]  Is that going to affect – or do you know how that's going to affect the Ubuntu package by any chance?
[1551.38 --> 1552.68]  Or the Debian packages, I should say?
[1552.68 --> 1553.12]  Okay.
[1554.44 --> 1555.04]  Okay.
[1555.54 --> 1557.38]  So I believe – so let's see.
[1557.48 --> 1562.14]  So I believe we only have – the packages we produce are already, you know, properly renamed.
[1562.86 --> 1567.56]  And I don't think we are in any other sort of official Wintu repositories.
[1568.02 --> 1568.58]  Oh, yeah.
[1568.66 --> 1569.02]  Oh, sorry.
[1569.16 --> 1574.96]  Well, I have the app source pointed to the Hudson URL.
[1575.20 --> 1577.88]  Is that automatically over at Jenkins now?
[1578.00 --> 1578.92]  Or do I need to update that?
[1578.92 --> 1588.02]  I believe that Kosuke and others have written up a wiki entry on upgrading Hudson to Jenkins.
[1588.44 --> 1590.00]  We can send that to you guys if you'd like.
[1590.62 --> 1597.00]  So you think that the migration for everyone should be painless and really wouldn't make any difference at all, right?
[1597.84 --> 1598.28]  It shouldn't.
[1598.38 --> 1598.52]  Yeah.
[1598.90 --> 1604.10]  So far, the reports we got from people are very positive that they were able to smoothly migrate to a newer version.
[1604.10 --> 1610.32]  So you just have to say – if you're using the Ubuntu, I guess you just have to say sudo apt-get install Jenkins.
[1610.70 --> 1611.40]  And then that's it.
[1612.20 --> 1612.82]  Sounds good.
[1613.72 --> 1621.48]  So this whole debacle kind of, you know, brings forth the two-edged sword of corporations backing open source software.
[1621.68 --> 1630.26]  Do you have any other comments or opinions on, you know, what people should be doing or shouldn't be doing in terms of that and how to handle certain situations?
[1630.26 --> 1633.54]  Because this has got a lot of press and a lot of coverage.
[1634.20 --> 1636.66]  It's kind of a hot topic at the moment.
[1638.14 --> 1638.50]  Yeah.
[1638.56 --> 1640.04]  I don't know what the lesson should be.
[1642.20 --> 1645.02]  Like, is there anything that you guys would have done differently from the start?
[1646.02 --> 1655.12]  Or you wish that – obviously you wish Oracle would have been a little more willing to discuss things and, you know, be part of the board now that you've changed the name, right?
[1655.12 --> 1669.00]  For instance, on jQuery, John Resick, you know, made efforts at some point in the project to move trademarks and licenses and things into – outside of his personal control, into a foundation control, as I understand it.
[1669.74 --> 1682.36]  Is that important to do once a project hits a certain critical mass to make sure that no single organization other than that organization that really, you know, is looking after the community can gain control of it?
[1683.42 --> 1684.22]  I think that's true.
[1684.22 --> 1689.00]  I mean, I think it's different depending on the situation.
[1689.14 --> 1696.26]  There's plenty of open source projects that are 90% developed at one company, but they share it with the world.
[1697.20 --> 1704.60]  And in those cases, I mean, that's, you know, the choice of the developers, the choice of the development and user community.
[1704.60 --> 1733.10]  But if it's a project that's not just tied to one corporation, not just tied to one entity, I think it is important to make sure that it is truly independent, that it's not – that you don't have one figure playing a bigger – having more – a disproportionate power because of trademarks and copyrights over the rest of the community.
[1733.10 --> 1734.10]  Assuming that's the direction you want your project.
[1734.10 --> 1735.14]  Assuming that's the direction you want your project to go.
[1735.24 --> 1739.46]  Again, this is – it's entirely up to the project what they want to do.
[1740.32 --> 1745.72]  What works for Jenkins doesn't necessarily work for a different project.
[1745.72 --> 1748.70]  There's no one-size-fits-all solution.
[1750.56 --> 1751.00]  Yeah.
[1751.14 --> 1753.74]  But I think we've come out stronger from this than before.
[1753.94 --> 1767.58]  I think it was actually a good thing that, you know, this gave us the motivation to sort of look more into more structures and the governance and making sure that the various companies are involved.
[1767.58 --> 1772.18]  And so that sort of helps make the project more independent.
[1772.60 --> 1774.50]  And I think in the long term, that helps.
[1775.86 --> 1778.84]  So even though in the short term, it might take some hit.
[1779.10 --> 1782.58]  I think it's in the long term, I think we've come out stronger from this than before.
[1782.58 --> 1797.84]  And we've definitely seen an increase in users and developers wanting to help, wanting to contribute bug fixes, help with the rename process, infrastructural matters.
[1798.56 --> 1799.82]  It's been hardening.
[1799.82 --> 1806.86]  It's been really nice to get that support, to get more people playing bigger roles.
[1809.10 --> 1816.58]  And so that everybody's got more of a sense of ownership of the project because it is the communities.
[1817.62 --> 1819.82]  So my wife and I are considering baby names.
[1819.94 --> 1824.14]  And I've got to tell you, Hudson was on the list, but I can't say that Jenkins will make the cut.
[1825.68 --> 1827.20]  Where did that name come from?
[1827.24 --> 1828.54]  And was this also a community vote?
[1829.82 --> 1839.44]  So Hudson, the name Hudson was for Butler from Upstairs, Downstairs, if I remember correctly.
[1840.22 --> 1841.30]  The BBC TV show.
[1841.40 --> 1841.62]  Is that right?
[1841.70 --> 1842.06]  That's right.
[1842.22 --> 1842.58]  Isn't it?
[1843.20 --> 1843.46]  Okay.
[1844.06 --> 1844.84]  No, that's not.
[1845.08 --> 1855.70]  So I guess the origin of the name is that, as I mentioned, I think of this software as really as one more person to your development team.
[1855.70 --> 1863.46]  So I liked very much the idea of giving it the name of the person so that you can say, well, let's have Hudson look at this.
[1863.62 --> 1867.02]  So let's have Jenkins already did that or something like that.
[1867.02 --> 1872.22]  So, you know, so I thought, well, this is a program that helps other people.
[1872.42 --> 1875.52]  So, well, what kind of people help other people?
[1875.96 --> 1876.76]  Well, butlers do.
[1876.76 --> 1880.68]  And so hence the logo of that little gentleman.
[1880.82 --> 1881.62]  So he's a butler.
[1882.44 --> 1886.10]  And then the Hudson just sounded like a British butler name to me.
[1886.10 --> 1891.12]  It sounds like, you know, when I ask the people here, it apparently isn't.
[1891.24 --> 1895.04]  But somehow I got the impression that the Hudson was like a British sounding name.
[1895.04 --> 1898.18]  So then, you know, so that was like 2004.
[1898.48 --> 1901.96]  And then recently we had to come up with something else.
[1902.02 --> 1904.40]  So we actually had, you know, we looked at a few other names.
[1904.56 --> 1910.02]  I think our primary choice was actually Alfred, you know, the famous butler.
[1911.30 --> 1911.74]  Yeah.
[1911.74 --> 1920.30]  But we fairly late into the game on that one, we discovered an application for the Mac.
[1920.74 --> 1921.92]  Yeah, I was going to mention that.
[1922.14 --> 1922.92]  Called Alfred.
[1923.46 --> 1926.28]  How we didn't notice that until then, I'm not entirely sure.
[1927.82 --> 1935.78]  But, yeah, so then we had to come up with something else that would still evoke the butler feel.
[1935.78 --> 1943.56]  Something that would still fit with, yeah, the theme and the conception.
[1944.38 --> 1946.96]  And Jenkins, I think, is a pretty good option.
[1947.32 --> 1955.98]  I think it's a – we didn't put the specific vote up, the name up for a vote just because then we'd end up with 70,000 suggestions.
[1957.20 --> 1958.66]  Was Niles up for a vote?
[1960.96 --> 1963.02]  The community has embraced it.
[1963.02 --> 1967.96]  Yeah, people had all kinds of suggestions when this whole thing had started.
[1968.40 --> 1968.92]  I can imagine.
[1969.02 --> 1973.18]  Someone suggested that we call it Rari, you know, in honor of the CEO.
[1977.44 --> 1980.90]  So this is where we turn the show upside down a little bit.
[1980.98 --> 1985.86]  We've added another question or two to this kind of ending salvo.
[1986.20 --> 1987.74]  So I'll put you guys on the spot.
[1987.74 --> 1990.72]  First question, and I'll hit you up first, Koski.
[1991.60 --> 1992.98]  Who's your programming hero?
[1993.88 --> 1994.48]  Ah, okay.
[1994.64 --> 1995.82]  So that's an easy question.
[1995.96 --> 1997.70]  So there's a guy called James Clark.
[1998.34 --> 2000.96]  He's – I think he now lives in Thailand.
[2001.90 --> 2008.06]  But, yeah, I think he's in a very unbelievable position of being very rich and very smart.
[2008.74 --> 2010.28]  So, like, he doesn't have to do work.
[2010.40 --> 2012.80]  He just wants to do things that he wants to do.
[2012.80 --> 2017.90]  And he's been – so he's, like, so smart that I actually met him a few times.
[2018.00 --> 2019.42]  And his brain is actually bigger.
[2019.80 --> 2026.64]  You can see that, like, his head, you know, above the eyes is, like, actually swelling to accommodate his brain size.
[2026.64 --> 2030.00]  And so he's been my hero ever since.
[2031.58 --> 2034.78]  When I looked at his color, it's just amazing.
[2035.42 --> 2038.10]  And so that's the height that I'm trying to get to.
[2039.08 --> 2046.12]  But, you know, sometimes you just see someone that's so good that you kind of get depressing because you see the chasm that you can't cross.
[2046.86 --> 2047.54]  You'll see.
[2047.54 --> 2049.70]  At least I'm younger than him.
[2049.80 --> 2053.50]  So if I survive him longer, that might be a way.
[2054.36 --> 2054.92]  Andrew?
[2056.92 --> 2070.52]  Honestly, I have a hard time imagining anybody that much better than Kosuke, who is definitely one of my programming heroes, just for the sheer volume of amazing code that he's written.
[2070.52 --> 2080.26]  And also Guy Steele and other Lisp hackers, just aesthetically I love Lisp and I love thinking about Lisp.
[2080.42 --> 2084.38]  And so guys have done really great work in that area and in language design.
[2085.42 --> 2086.48]  Impressed the hell out of me.
[2087.08 --> 2089.80]  Yeah, you have the thing with Lisp that I've been always curious about.
[2090.98 --> 2097.50]  My dad was an MIT grad, so I grew up with the little Lisper in the room with the computer.
[2097.50 --> 2103.80]  And then in college we did our second year of CS courses in Scheme.
[2104.14 --> 2112.96]  And there's just something elegant about Lisp languages and about thinking about programming in that functional way.
[2113.32 --> 2115.54]  And about, you know, where code is data and data is code.
[2115.80 --> 2124.86]  And I'm not very good at it, but it really helps me when I run into a programming challenge to think about the problem and how one would solve it from that perspective.
[2124.86 --> 2130.82]  And it tends to help me come up with less buggy solutions, if nothing else.
[2131.62 --> 2135.78]  So you grew up within an environment surrounded with a sea of parentheses?
[2137.30 --> 2138.26]  Yeah, basically.
[2140.96 --> 2143.28]  And I've been on Emacs for 14 years.
[2143.96 --> 2145.30]  Oh, so Lisp Emacs?
[2145.46 --> 2150.00]  Which Lisp is the Kosher implementation?
[2150.00 --> 2158.34]  Most of the Lisp I've done in the last year or so have been just programming challenge stuff and Clojure.
[2160.34 --> 2161.82]  I like to dabble in MZ.
[2162.26 --> 2163.42]  Oh, go ahead, sorry.
[2164.02 --> 2164.68]  Sorry, go ahead.
[2165.06 --> 2167.80]  I like to dabble in MZ scheme every once in a while, but I can't.
[2168.26 --> 2170.60]  I still haven't wrapped my head completely around the concept.
[2170.76 --> 2172.28]  It's like an exercise for me.
[2172.74 --> 2175.20]  I can't actually, could never be productive in that environment.
[2175.20 --> 2182.08]  Definitely take a look at Structured Interpretation of Computer Programs, the old intro textbook from MIT.
[2184.06 --> 2191.00]  It's a brilliant resource for, A, understanding programming, and B, understanding scheme and Lisp languages.
[2191.78 --> 2194.12]  I treasure my copy.
[2194.12 --> 2205.52]  So, outside of Jenkins, what software gets you guys excited that you really want to play with in the future of the whole programming landscape?
[2209.24 --> 2210.34]  Interesting question.
[2214.08 --> 2216.02]  Well, I'm a build guy.
[2216.62 --> 2221.16]  So, build tools really fascinate me.
[2221.16 --> 2223.02]  I love Maven for Java builds.
[2224.34 --> 2227.62]  I think Selenium is absolutely fantastic.
[2230.50 --> 2241.14]  And I really enjoy seeing this sprawl of languages running on JPM besides Java.
[2241.78 --> 2250.70]  I think that's the ability to write in so many different languages, but share code between them, I think, is really great.
[2252.12 --> 2260.34]  So, if you had a completely open weekend this weekend and you weren't allowed to touch anything related to build servers, what project would you play with?
[2262.48 --> 2264.30]  I have absolutely no idea.
[2264.30 --> 2269.18]  I've been trying to set up this, I guess, the home audio automation.
[2269.40 --> 2271.72]  So, I bought the Airport Express.
[2271.96 --> 2275.42]  I guess that's how they call their wireless router at Apple.
[2275.42 --> 2282.28]  They got some DRM to protect it down, but you got the streaming protocol that can send audio over there.
[2282.86 --> 2291.94]  So, I was wondering if I could hack that a little bit so that I can get my speaker hooked up there to receive audio from my computers.
[2291.94 --> 2293.74]  That would be very cool.
[2293.74 --> 2297.04]  The problem is that everything like that eventually comes back to Jenkins for me.
[2297.16 --> 2300.90]  That I had these lots of holy projects, but one way or the other, they come back to Jenkins.
[2301.00 --> 2306.92]  So, in the context of Jenkins, it would be like if the build would break, you know, this is sort of a fact.
[2306.92 --> 2316.22]  You don't normally have a speaker, but with this audio over the internet, you could actually send the audio over that and then you get.
[2317.08 --> 2318.26]  So, I thought that would be funny.
[2319.72 --> 2321.00]  I haven't actually done that, but.
[2323.26 --> 2324.88]  Well, thanks for taking the time, guys.
[2324.96 --> 2329.58]  We really appreciate you telling us the backstory of Jenkins and A Hudson.
[2330.38 --> 2336.08]  And hopefully, it'll just keep on going as far as the momentum that you've seen so far.
[2336.08 --> 2336.90]  Yep.
[2337.36 --> 2337.82]  Thank you.
[2337.82 --> 2337.84]  Thank you.
[2366.08 --> 2367.20]  Thank you.
[2367.20 --> 2370.68]  Thank you.
[2370.74 --> 2371.92]  Okay.
[2375.86 --> 2377.10]  Bye.
[2377.10 --> 2379.02]  Bye.
[2379.26 --> 2379.70]  Bye.
[2387.80 --> 2389.84]  Bye.
[2389.86 --> 2392.34]  Bye.
[2392.54 --> 2392.86]  Bye.
