[0.00 --> 6.94]  The Change Log is brought to you by Pusher, and they're looking for a system engineer who specializes in evented systems.
[7.52 --> 15.08]  If that's you, send your GitHub profile, a cover letter, and your CV to jobs at pusher.com.
[15.08 --> 22.36]  And also use the coupon code THECHANGELOG to save 15% off your first month billing.
[22.76 --> 25.98]  Join the real-time web today at pusher.com.
[30.00 --> 44.64]  Welcome to The Change Log episode 0.7.8.
[44.86 --> 46.06]  I'm Adam Stachowiak.
[46.26 --> 47.28]  And I'm Wyn Netherland.
[47.42 --> 48.44]  This is The Change Log.
[48.50 --> 50.06]  We cover what's fresh and new in open source.
[50.52 --> 53.06]  If you found us on iTunes, we're also on the web at thechangelog.com.
[53.14 --> 54.14]  We're also up on GitHub.
[54.26 --> 56.44]  Head to github.com slash explore.
[56.44 --> 61.22]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[62.10 --> 65.76]  And if you're on Twitter, follow The Change Log and me, Adam Stach.
[66.08 --> 68.28]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[68.86 --> 69.58]  Fun episode this week.
[69.64 --> 76.08]  Talk to Eloy Duran of the Cocoa Pods Project, which is basically bundler meets homebrew,
[76.24 --> 81.80]  except for, I guess not binaries, libraries for your Objective-C projects, your Cocoa projects.
[81.80 --> 86.82]  So no more downloading tarballs from blog posts to drag into Xcode.
[86.92 --> 91.62]  You now can install all those frameworks that you want to use directly from your command line.
[92.14 --> 95.88]  How about that pulling down and dragging over was a pain in the butt, huh?
[96.40 --> 96.84]  Yeah.
[97.16 --> 102.16]  I think GitHub has changed the way we all work in the Ruby space.
[102.36 --> 106.20]  And we're getting, I guess, penetration into other communities.
[106.20 --> 113.62]  So hopefully this will just further the way we share Objective-C libraries across those projects.
[113.88 --> 116.66]  And I hear you also talked a little bit about Passenger pane.
[117.46 --> 122.62]  Yeah, he's the developer of the preference pane for Passenger that I know you and I both used.
[123.36 --> 131.30]  You either have the choice of editing the big config file in Apache, or if you're on the Mac and you want to install Passenger, which used to be ModRails,
[131.30 --> 137.78]  there's a nice little pref pane you can snap into the Mac to configure all of that.
[137.88 --> 139.62]  He's the author of said utility.
[140.62 --> 146.24]  And if you're around, I guess, this August and you're into Ruby, since we just mentioned Ruby,
[147.26 --> 150.78]  MadisonRuby.org, we're actually going to be there.
[150.86 --> 155.38]  Wyn and I are going to be there doing our famous design eye for the dev guy, Orgal.
[155.86 --> 156.32]  Orgal.
[156.64 --> 157.00]  Orgal.
[157.00 --> 162.12]  So if you go there and you go to slash register, you'll see that we're actually one of the workshop choices.
[162.32 --> 169.52]  So if you want to learn how to do the HTML5, the CSS3, and throw a little sass and compass in there, we'll teach how.
[170.20 --> 177.92]  Well, color theory, a little typography, just basically the science of design as you and I have bloodied our nose on it along the way.
[178.36 --> 178.72]  Absolutely.
[179.48 --> 180.78]  Well, this sounds like a fun episode.
[180.88 --> 181.52]  You want to get to it?
[181.72 --> 182.24]  Let's do it.
[182.24 --> 182.30]  Let's do it.
[187.00 --> 216.98]  Let's do it.
[217.00 --> 246.98]  Let's do it.
[246.98 --> 253.30]  It's basically a package manager built on Ruby, but for Cocoa frameworks, right?
[254.06 --> 254.38]  Correct.
[256.14 --> 261.36]  So at Fingertips, we've been doing Objective-C applications for clients for a while.
[261.36 --> 277.54]  And as I'm spoiled by the Ruby development environments, like RubyGems and Bundler and whatever, I was starting to get a bit frustrated by the process of integrating open source libraries into a project.
[277.54 --> 284.94]  And since I don't want to spend too much time on getting something to run and then afterwards find out that it might not be what I needed.
[284.94 --> 287.94]  I found that I found that I didn't use that many libraries.
[287.94 --> 290.76]  Also, because it's very hard to find them, I found.
[290.76 --> 296.94]  And so every time I would find a library that would do what I needed after the fact.
[296.94 --> 304.02]  And at some point, I think it was they released the, what do they call it?
[304.18 --> 306.14]  The iOS template, something like that.
[306.26 --> 307.54]  The boilerplate template.
[307.54 --> 319.74]  And so by that time, I figured if the solution in the community is going to be like templates, then what I wanted, like a package manager, wasn't going to happen anytime soon.
[320.30 --> 325.32]  So yeah, then you need to stop complaining and start implementing is my motto.
[325.32 --> 325.76]  Absolutely.
[326.72 --> 334.80]  So outside of CocoaPods, the normal procedures, you find a bit of open source on GitHub if you're lucky and it's well done.
[334.80 --> 338.28]  And then the instructions say, hey, drag this to your frameworks folder, right?
[338.92 --> 339.12]  Yeah.
[339.40 --> 347.26]  It tells you to clone and then add it to your project and then add the required build settings, add the required frameworks to link against.
[347.40 --> 354.62]  And then usually it will miss one or two steps because the author forgot to update the readme while developing on it, et cetera, et cetera.
[354.62 --> 354.78]  Right.
[354.88 --> 357.88]  It can take you like an afternoon that's just lost.
[358.78 --> 361.56]  So how much of this does CocoaPods automate?
[362.20 --> 362.56]  Everything.
[363.58 --> 366.62]  So what's the workflow turn into?
[368.06 --> 370.60]  So it's comparable to a bundler.
[371.00 --> 375.36]  You have a file where you specify which dependencies you want to use.
[375.36 --> 387.84]  And as long as there are specifications for that library, it will automate, it will create a separate Xcode project where it will include all the dependencies.
[388.58 --> 391.64]  And that Xcode project will then produce a static library.
[392.24 --> 398.08]  And the static library is then your application probably is linked against that static library.
[398.08 --> 401.82]  And that's all done in a workspace which was introduced in Xcode 4.
[402.62 --> 405.86]  And that's all set up automatically by the tool.
[406.56 --> 408.26]  How are you persisting settings?
[408.78 --> 411.90]  I know NPM has its JSON file and there's a gem file for a bundler.
[411.98 --> 412.76]  What's CocoaPods use?
[414.78 --> 417.70]  So in your user project, you will use a pod file.
[417.88 --> 419.52]  That's what it's called, just like a gem file.
[419.70 --> 420.32]  It's very similar.
[420.32 --> 426.08]  And the specifications for the libraries themselves are probably more what you meant by NPM.
[426.68 --> 429.06]  It's a pod spec, like a gem spec.
[429.40 --> 432.86]  I mean, I try to reuse a lot of RubyGems code as well.
[433.02 --> 437.78]  So things like the version class is already very well done in RubyGems.
[437.90 --> 439.18]  So I'm just using those things.
[439.42 --> 441.88]  They're very similar if you're used to RubyGems and bundler.
[442.24 --> 448.56]  Have you developed a newfound appreciation for YCats and the bundler team for what they've done with bundler?
[449.04 --> 450.16]  Oh, yeah, definitely.
[450.88 --> 458.04]  Well, I mean, I think like a lot of people that are passionate about their environment and have seen the whole environment grow from,
[458.96 --> 465.76]  I think we were, at least fingertips was using Rails since a month after the first release.
[465.98 --> 469.00]  So we've seen that environment grow.
[469.00 --> 473.74]  And then at some point, you start to feel like things like bundler make things more difficult,
[474.08 --> 476.96]  especially because we're actually, and that might be a bit weird,
[477.32 --> 479.52]  we're people that don't like a lot of dependencies.
[479.52 --> 482.78]  So it might be weird for me to implement something like CocoaPods.
[482.96 --> 487.02]  But it got a bit frustrated.
[487.24 --> 493.60]  And obviously, you have Twitter and the bar is very low and you start hating on stuff, in quotes,
[493.80 --> 494.82]  because it's not really hating.
[494.82 --> 497.48]  But yeah, definitely.
[497.66 --> 506.02]  The way I see it now is that once people start hating, between quotes, passionately about CocoaPods the same way they do about bundler,
[506.14 --> 507.10]  then I'm satisfied.
[507.10 --> 518.92]  Have you found any barriers to adoption of it being a Ruby runtime and having to reach outside the Ruby community to pull people in that might not have the Ruby stack?
[518.92 --> 522.58]  So you mean users, right?
[522.58 --> 523.24]  Not collaborators.
[523.24 --> 523.72]  Right, yeah.
[523.84 --> 532.26]  Users that just want to use the CocoaPods to pull down frameworks and install, but may not be Ruby savvy.
[532.26 --> 548.40]  Well, in the beginning, it was way more because by that time I was using MacRuby because a Xcode project is a plist and I just wanted to read it and write it without having to do anything difficult.
[548.40 --> 557.90]  And MacRuby, since it interfaces already with the Cocoa frameworks, that already supported everything I needed to just go ahead and build the core code.
[558.58 --> 562.02]  I already knew, of course, that that was going to be a hassle for a lot of people.
[563.12 --> 567.58]  People just don't feel they want to install something extra, an installer or whatever.
[568.28 --> 571.86]  So right now, we've switched to MRI.
[572.68 --> 573.40]  It works on MRI.
[573.58 --> 576.90]  That has brought a lot of more people in because it will just work.
[576.90 --> 585.62]  Well, nowadays, again, it won't because with the new Xcode 4.3, you have to go through all these hoops to install the right compilers and things like that.
[586.14 --> 589.48]  But in general, it will just work and people will use it.
[589.82 --> 596.72]  On the collaboration side, however, that's obviously a lot more difficult because a lot of people have never written any Ruby or seen it.
[598.92 --> 601.46]  But yeah, I mean, that was to be expected.
[601.82 --> 606.72]  I'm seeing a lot of collaboration, though, so I don't want to put that down.
[606.90 --> 614.74]  There's a lot of people, especially like one guy that never wrote any Ruby and had a feature request and we started talking.
[615.02 --> 617.42]  And then a week later, he was implementing everything.
[617.68 --> 618.84]  So that's cool to see.
[618.84 --> 630.72]  As an open source project lead, I mean, it's fun to watch people come into the community and dip their toe and ask for something and then better yet, come back with a patch for it.
[631.20 --> 631.98]  Definitely, definitely.
[632.22 --> 634.26]  Well, I try to steer it that way, of course.
[635.20 --> 636.28]  You can't do everything.
[636.28 --> 642.38]  And sometimes you see the benefit of a feature, but you have to prioritize.
[642.62 --> 646.72]  And there's so much still to be done that I can't get to all the fun features yet.
[647.70 --> 650.28]  And so I try to steer people to...
[650.84 --> 655.70]  I like to discuss code, not so much just bike shedding.
[656.14 --> 657.94]  I want to prevent bike shedding.
[657.94 --> 664.26]  So asking for patches and helping them out to get that patch done really helps.
[664.54 --> 674.64]  And then once somebody has something merged in, they'll feel much more invited to work on other patches and tickets.
[674.84 --> 675.96]  And that's worked out great for me.
[676.66 --> 681.38]  So speaking of features and patches, what do you see the roadmap for CocoaPods being?
[681.38 --> 685.22]  So that's...
[685.22 --> 693.38]  I'm not thinking too much about version 1.0 yet because that's where, for me, the big transition will be between...
[693.98 --> 701.90]  One of the big things that will have to change at some point, I think, is the way we distribute all the specifications.
[703.20 --> 705.66]  Currently, that's done as a...
[705.66 --> 707.00]  It's similar to Homebrew.
[707.00 --> 713.50]  So the specifications are all in a Git repository on the CocoaPods organization on GitHub.
[715.08 --> 726.04]  And that works great while we're still actively developing stuff because it's very easy to change the API of the specifications and go back and update them all.
[726.20 --> 731.98]  Or even have a branch of the specifications while we're working on a new API changes.
[731.98 --> 741.56]  And that would be very hard if I would have started out with some kind of real server or whatever that accepts JSON, talks back in JSON.
[741.70 --> 749.46]  I mean, this works much easier for me, especially because I need to embrace the community as it already existed.
[749.62 --> 751.88]  And the Objective-C community already existed for a long time.
[751.90 --> 754.34]  And there's a lot of people doing private stuff internally.
[754.34 --> 763.56]  So having them just create a Git repository for internal private specifications is the easiest thing that I could come up with.
[763.70 --> 773.44]  And I want as less friction as possible for everyone until we can converge into the final way it will work.
[773.72 --> 777.02]  And that will most probably be a server like RubyGems has as well.
[777.02 --> 783.32]  So does CocoaPods require a formula, to use homebrew terminology, to be in the specs repo under your org?
[783.38 --> 786.08]  Or can you install from someone else's repo?
[787.48 --> 788.26]  Specifications, you mean?
[788.84 --> 789.26]  Right.
[789.76 --> 789.92]  Yeah.
[790.10 --> 802.06]  So what CocoaPods does is it just checks in your home folder under a .cocoaPods directory for any directories which are expected to be specification repositories.
[802.06 --> 807.02]  And so you can just add a directory, add your specification, and it will be usable.
[807.60 --> 812.20]  And there are many other ways to inline in your pod file.
[812.32 --> 818.90]  You can define a specification if there isn't any specification yet or if you need some, if you have a fork or whatever.
[819.50 --> 829.02]  There are many ways to add specifications and use them without having them in the public specifications repository.
[829.02 --> 832.22]  I wanted to switch gears and talk about MacRuby for a moment.
[832.32 --> 839.58]  It seems like a couple of years ago it was red hot and then everybody that was in the Ruby community was excited about MacRuby.
[839.68 --> 841.18]  What's the state of that project?
[843.48 --> 854.62]  The state of the project is currently, I think there are a lot of people still, if you watch it in the mailing list, there are a lot of people still working with it.
[854.62 --> 860.16]  But I personally haven't had the time to work on it as much as I used to.
[861.02 --> 864.58]  So I can't speak for the community as it is right now.
[865.68 --> 876.44]  But one thing that's definitely for sure is that the main developer, the lead developer, Laurent Sanzonetti, isn't working at Apple anymore.
[876.44 --> 880.50]  And he has had to move and things like that from the US back to Europe.
[880.76 --> 885.10]  And I mean, it has stalled a bit for now.
[885.24 --> 888.64]  But as far as I know, he will pick that up again.
[888.90 --> 893.42]  And then I'm sure he has all kinds of ideas, but we haven't catched up about that yet.
[893.42 --> 897.06]  But the way I use it, I mean, I still use it.
[897.30 --> 909.52]  And we have a client, for instance, where we just recently implemented a specification runner, a test runner in MacRuby for their Objective-C iOS classes,
[909.88 --> 913.56]  where they wanted a visual representation of the state of the game.
[914.50 --> 916.02]  And for that, it works great.
[916.02 --> 923.98]  So, yeah, I'm not sure what to say about where it's heading or going, because I can't speak for that.
[924.24 --> 926.54]  I haven't been that active the last few months.
[926.84 --> 929.52]  One of your more popular projects is Passenger Pain.
[929.86 --> 933.04]  It's a pref manager for Fusion Passenger.
[933.16 --> 934.74]  Was that a MacRuby project as well?
[935.54 --> 937.04]  It was Ruby Cocoa, actually.
[937.12 --> 938.66]  By that time, there was no MacRuby yet.
[941.40 --> 943.78]  Yeah, the difference is marginal.
[943.94 --> 944.48]  It was Ruby.
[944.48 --> 949.08]  You can see it on our repository and browse it.
[949.42 --> 953.04]  But we've rewritten it to be Objective-C.
[954.78 --> 959.00]  But unfortunately, my colleague hasn't had the time to finish that up and release it yet.
[960.06 --> 964.16]  What was the motivation behind that project, just scratching your own itch?
[964.58 --> 966.62]  Yeah, everything I do is scratching my own itch.
[967.66 --> 972.18]  I have so many itches, and that's not because I don't shower and stuff.
[972.18 --> 976.34]  But just, I mean, I feel the need for stuff when I'm doing it.
[976.56 --> 983.96]  I don't think I ever really had, like, it would be fun to do this or nice to do whatever.
[984.06 --> 985.16]  I don't even have the time for that.
[985.16 --> 991.16]  I just, I come up with things that have to be solved while I'm working at work, at my job.
[991.16 --> 994.94]  And that tends to take up most of my time already.
[994.94 --> 998.14]  So, yeah, it's all just scratch itch.
[998.26 --> 1002.82]  And the passenger pain, I'm not sure what the specific...
[1002.82 --> 1009.68]  I think because we're a consultancy, we just have so many applications at any given time on our hard disk.
[1010.54 --> 1017.88]  Yeah, so passenger pain was mainly, I think, because we're a consultancy and we have so many applications at any given time.
[1018.10 --> 1025.18]  And we just want to easily add them, see which one have been added or what are the configured domains, things like that.
[1025.18 --> 1027.76]  And that's basically everything it does.
[1027.96 --> 1028.58]  It doesn't show.
[1028.80 --> 1034.58]  And there have been a lot of requests for thingies like, I don't know, tail-specific logs or whatever.
[1034.70 --> 1036.10]  But that's just not the goal.
[1036.14 --> 1041.30]  The goal was just setting up applications, having a quick overview of which applications you have set up,
[1041.30 --> 1045.52]  and add aliases for their server names, things like that.
[1046.26 --> 1048.00]  So what are you scratching these days?
[1048.00 --> 1055.98]  Oh, I really, really, really, really have to not scratch anything else at the moment.
[1056.58 --> 1058.30]  CocoaPods is so much work.
[1059.50 --> 1068.74]  And I really have to even find the time to get to coding on CocoaPods because their last few weeks at least, let's say last month,
[1069.28 --> 1075.12]  I've been doing so much project management because people are starting to do a lot of contribution,
[1075.92 --> 1077.40]  which is nice for a change.
[1078.00 --> 1084.04]  But I'm sure that if I would try to think of it, I would actually.
[1085.12 --> 1088.90]  Just yesterday, I came up with something that I'm just...
[1088.90 --> 1093.48]  Now, whenever I come up with something, I'll just put it on Twitter as my wish list.
[1093.48 --> 1098.46]  And if somebody knows of something that does it or wants to implement it, then I'll be very happy.
[1098.46 --> 1109.02]  That thing was a Ruby library that will give you divs of arrays and hashes and strings, but a unified div,
[1109.52 --> 1112.62]  and preferably with red and green colors.
[1113.08 --> 1118.12]  Because, yeah, I still find that in many testing frameworks that I work with,
[1118.12 --> 1122.12]  I still have to manually compare huge hashes or whatever.
[1122.26 --> 1123.50]  And that just takes up time.
[1124.12 --> 1127.94]  So that's something I would normally tackle right away.
[1128.20 --> 1133.10]  But I really have to refrain from doing those things because otherwise I wouldn't have any time for other things left.
[1133.10 --> 1135.08]  Hey, Adam here.
[1135.14 --> 1139.38]  Just wanted to take a moment and thank our sponsor, Hover.com, for supporting the show.
[1139.64 --> 1141.86]  We certainly appreciate their support.
[1142.30 --> 1145.40]  Hover is by far the best place to register your domains.
[1146.00 --> 1151.22]  We recently took advantage of their domain concierge service, which is completely free, by the way.
[1151.22 --> 1158.18]  We had over 30 domains that needed to move over from GoDaddy because, you know, for obvious reasons why we didn't want to use them anymore.
[1158.82 --> 1160.72]  And Hover took care of everything.
[1160.86 --> 1162.22]  They took care of all the heavy lifting.
[1162.36 --> 1163.76]  It's this special service they have.
[1164.34 --> 1169.14]  It's called their domain concierge service, which basically means you don't worry.
[1169.30 --> 1170.44]  They do all the work.
[1170.54 --> 1171.94]  They move over all your domains.
[1172.38 --> 1179.00]  They take care of recreating your CNAME, your A records, your MX records for your email, everything.
[1179.00 --> 1181.84]  All you do is sit back and relax, and it's completely free.
[1182.44 --> 1184.52]  You actually talk to a human being to set it all up.
[1184.60 --> 1186.10]  It takes about five or ten minutes.
[1186.76 --> 1191.42]  You call this 800 number, 866-731-6556.
[1192.30 --> 1193.82]  And like I said, you talk to a human.
[1193.92 --> 1194.66]  They take care of you.
[1194.72 --> 1197.64]  They make sure that you're good to go.
[1197.88 --> 1199.82]  And just tell them what the changelog sends you.
[1199.88 --> 1206.02]  Use the coupon code THECHANGELOG to save 10% on all the services that apply us to.
[1206.02 --> 1209.18]  We certainly appreciate their support, and thank you for trying them out.
[1209.24 --> 1210.24]  Hover.com
[1210.24 --> 1217.44]  So digging into the pod spec format, I first thought this was closer to a gem file, but it's actually closer to a gem spec.
[1218.14 --> 1218.38]  Yeah.
[1219.02 --> 1220.66]  Yeah, so there are two things.
[1220.80 --> 1231.28]  So like with Bundler, because pods, as we call them, CocoaPods, aren't installed into the system like RubyGems normally does.
[1231.28 --> 1233.76]  But they're only used in a project.
[1234.18 --> 1236.86]  So that's more like a combination of RubyGems and Bundler.
[1237.22 --> 1238.78]  So you have two things.
[1238.88 --> 1241.78]  You have the pod file, which is like the gem file with Bundler.
[1242.02 --> 1245.96]  And you have the pod spec, which is like the gem spec in RubyGems.
[1245.96 --> 1259.40]  So Jonah Williams from Twitter asks, how do you push for greater adoption of pods, and what advice do you have for getting sourceless pods?
[1261.92 --> 1262.76]  Sourceless pods.
[1264.74 --> 1266.14]  I'm not sure what that means.
[1266.32 --> 1266.96]  Are we talking about...
[1266.96 --> 1268.18]  I'm not sure if that means binaries or what?
[1268.52 --> 1269.76]  It's the problem with 140 characters.
[1269.76 --> 1274.20]  There are things like TestFlight, for instance.
[1274.34 --> 1274.82]  Do you know TestFlight?
[1275.12 --> 1275.64]  TestFlight, yeah.
[1275.68 --> 1276.38]  I use that all the time.
[1276.72 --> 1277.18]  Okay, cool.
[1278.22 --> 1282.04]  So they don't provide the source for their SDK.
[1282.58 --> 1285.04]  They only provide a pre-compiled static library.
[1286.08 --> 1287.44]  Maybe that's what he meant.
[1289.96 --> 1293.50]  Well, first of all, I would say to the TestFlight team, open source it.
[1293.50 --> 1296.26]  But obviously, they have their reasons.
[1296.26 --> 1313.36]  And it already works because the pod spec can indicate libraries that the user's project should link in, which is normally used for things like if a pod requires lib.xml or whatever.
[1313.76 --> 1317.02]  But it works just as well for any other static libraries.
[1317.02 --> 1325.32]  So it can already be done, and there are people discussing this on the CocoaPods issue tracker.
[1326.26 --> 1330.84]  I guess if that's what he meant, then it works.
[1331.18 --> 1335.14]  But I would still prefer, of course, an open source version.
[1336.94 --> 1340.10]  But what can we do further to push for greater adoption?
[1340.10 --> 1346.16]  I think I haven't done any big announcement yet on CocoaDev.
[1346.30 --> 1348.12]  That's the big Cocoa mailing list.
[1348.12 --> 1356.34]  Because there are a lot of things that I first want to have done before I open the floodgates.
[1356.72 --> 1361.10]  Because I think these are things that a lot of people will ask about.
[1361.84 --> 1363.38]  So I don't know.
[1363.44 --> 1364.92]  That's not the way I work.
[1365.04 --> 1370.58]  I want to have a reasonable assumption of what people are going to need, implement that, and then announce it.
[1370.64 --> 1372.66]  In the meantime, it's open for everybody to discover.
[1372.66 --> 1376.42]  But I'm not going to announce it and then say, oh, yeah, that doesn't work yet.
[1376.48 --> 1377.24]  That doesn't work yet.
[1377.30 --> 1378.06]  That doesn't work yet.
[1378.50 --> 1383.06]  So that will probably push a lot of adoption once I finally do that.
[1383.72 --> 1395.00]  Until that time, what we really need is people that use libraries to migrate them to using them through CocoaPods.
[1395.00 --> 1408.88]  So creating specifications for that, even if they do it only locally, like in their pod file in line, then please also take the time at some point to extract that and push it to public repository.
[1408.88 --> 1419.44]  And I think the faster we get to the point where it's like the big 1.0 and where that's also the time that we'll do like big announcements.
[1420.56 --> 1423.86]  Well, that will definitely help if people want to help out.
[1424.00 --> 1432.72]  So just go onto our mailing list or the issue tracker and ask what you're good at, if you want to help out with certain areas or whatever.
[1432.92 --> 1434.62]  And there's plenty of work to do.
[1434.62 --> 1444.78]  I think that's really the biggest important thing right now is to get some of the important features done so that we can really, really start driving it.
[1445.64 --> 1453.92]  One big thing, and I'm sure you have listeners that are very good at that, is things like the Rails guide.
[1455.14 --> 1461.66]  Guide for if you're a user of CocoaPods, how to set it up initially.
[1461.86 --> 1462.62]  That's obvious.
[1462.62 --> 1466.00]  But also guides for library authors.
[1466.30 --> 1467.22]  Why should they care?
[1467.72 --> 1471.14]  How do we handle versioning, semantic versioning?
[1471.64 --> 1472.84]  Why do we do that?
[1473.00 --> 1474.66]  Why not just git hashes?
[1474.80 --> 1477.76]  These are questions that we get all the time from library authors.
[1479.22 --> 1481.74]  And right now that's scattered over.
[1482.14 --> 1484.74]  We do have wiki pages describing these things.
[1484.74 --> 1494.42]  But having a good set of coherent guides about these things would definitely help authors understand how we do things and why we do them that way.
[1494.64 --> 1497.86]  And then contribute specifications for the libraries.
[1498.38 --> 1499.08]  But it's picking up.
[1499.08 --> 1504.60]  In the meantime, I'm very glad the way it goes in the way that I haven't announced anything.
[1504.76 --> 1506.36]  But people are discovering it by themselves.
[1507.14 --> 1511.06]  And adoption is definitely every day more.
[1511.06 --> 1514.00]  So I guess we'll get there.
[1514.44 --> 1516.68]  What we really need is time.
[1516.88 --> 1518.84]  If anybody has some lying around.
[1518.84 --> 1522.96]  You play in a few different communities, namely Ruby and Objective-C.
[1523.14 --> 1528.32]  And I think in the Ruby community, GitHub by far is the center of gravity for our open source work.
[1528.72 --> 1530.64]  But it's not true of every community.
[1530.80 --> 1539.68]  There's other repositories and other community sites that house the bulk of open source or shared source projects in those languages.
[1539.68 --> 1545.34]  According to GitHub Explorer, Objective-C is the 10th most popular language on GitHub.
[1545.60 --> 1551.60]  Have you found that the bulk of Objective-C and Cocoa open source that you found is on GitHub?
[1551.78 --> 1555.42]  Or are there other places where they're playing?
[1556.96 --> 1568.86]  Before I started on CocoaPods, I found that the majority of the libraries that are being released since the inception of GitHub have been on GitHub.
[1568.86 --> 1574.78]  But the Objective-C community goes back way before GitHub.
[1575.66 --> 1580.78]  So there's a lot of people just posting tarballs on their blog, things like that.
[1580.78 --> 1588.04]  Or they use SourceForge or what have you, Bitbucket, I guess.
[1590.62 --> 1597.02]  Yeah, I think a lot of the people, since we have iOS, there's a whole new community.
[1597.02 --> 1600.48]  You have the older Objective-C community and you have the new Objective-C community.
[1600.64 --> 1603.42]  And the newer ones tend to use GitHub, I think.
[1603.56 --> 1605.80]  I haven't seen many that don't use GitHub.
[1606.20 --> 1612.42]  But some of the older libraries, the older authors, yeah, that's not that easy.
[1612.60 --> 1614.30]  They tend to be all over the place.
[1614.68 --> 1617.04]  So GitSupport and Xcode is relatively new.
[1617.14 --> 1619.44]  I'm trying to remember which version introduced that.
[1619.46 --> 1623.26]  But have you seen a spike in GitHub adoption as that feature rolled out into Xcode?
[1623.26 --> 1623.66]  No.
[1625.74 --> 1631.94]  And I think they already had GitSupport before I started on CocoaPods.
[1632.08 --> 1633.54]  But I'm not entirely sure.
[1633.80 --> 1637.54]  I'm not a big Xcode.app user, personally.
[1637.98 --> 1638.64]  That's interesting.
[1638.76 --> 1639.62]  What are you using?
[1640.10 --> 1645.16]  I guess are you still using MacRuby and RubyCoco more than straight Objective-C?
[1645.16 --> 1645.28]  No.
[1647.78 --> 1648.18]  No.
[1648.52 --> 1650.88]  I mean, it could be anything, any given day.
[1651.22 --> 1652.54]  So I use MacFim.
[1653.12 --> 1654.96]  That's why I wrote the file browser for it.
[1655.30 --> 1656.72]  I used TextMate before that.
[1657.00 --> 1660.82]  But TextMate was just getting too slow for big files for me.
[1661.30 --> 1662.72]  And that's the reason I switched to Fim.
[1662.86 --> 1667.02]  And I still feel like a huge Fim noob.
[1667.02 --> 1671.56]  I mean, people look at me weird why I would even want a file browser.
[1671.86 --> 1679.34]  So I do everything there so that I know just the set of commands and editing tools that I tend to use.
[1680.24 --> 1681.26]  Xcode, Editor.
[1681.78 --> 1685.24]  I'm not a real big fan of Xcode.app at all.
[1686.06 --> 1690.94]  It just does things the way my brain doesn't work, I guess.
[1690.94 --> 1695.56]  And obviously, there's still a lot of issues with Xcode 4.
[1696.44 --> 1697.42]  That's no secret.
[1697.56 --> 1698.76]  Everybody complains about that.
[1700.38 --> 1704.72]  Listeners of this podcast won't blame you for using Vim by far.
[1704.84 --> 1708.80]  We've had a few episodes now where we talk about everybody's favorite text editor.
[1709.06 --> 1710.28]  But you're using MacVim.
[1710.36 --> 1710.84]  That's interesting.
[1710.98 --> 1715.42]  What draws you to the GUI shell around Vim that you don't get from the terminal?
[1718.10 --> 1719.60]  I'm a GUI guy.
[1719.60 --> 1722.62]  I think that's the simplest solution.
[1724.34 --> 1728.68]  I'm not particularly interested in computers, actually.
[1728.84 --> 1730.40]  I just want things that work.
[1731.18 --> 1733.50]  And I love the terminal.
[1733.68 --> 1734.52]  That's not the reason.
[1734.62 --> 1743.90]  But I find that the GUI and the set of key bindings that I know for any other application on the platform,
[1743.90 --> 1750.32]  or in this case, OS X, I find it more intuitive to seamlessly switch those things.
[1751.30 --> 1755.92]  And I like a visual file browser that has a contextual menu for thingies.
[1756.04 --> 1759.54]  And that's not the way people work in the terminal, I find.
[1759.54 --> 1763.46]  And that would mean I would have to really more master Vim.
[1763.60 --> 1765.94]  And I don't really care about that.
[1766.00 --> 1768.42]  I just want to get the things done that I want to get done.
[1768.54 --> 1778.74]  And I feel I'm more productive in an environment that allows me to use the GUI instead of looking at a beautiful terminal.
[1778.74 --> 1782.78]  But, yeah, the only way to really interact with it is the keyboard.
[1782.78 --> 1786.50]  It seems a lot of folks go one way or the other.
[1786.64 --> 1791.88]  They're in a full-blown IDE like Xcode, and everything's in really one window or one app at least.
[1792.04 --> 1795.88]  Or they'll go to the terminal, and they'll multiplex with Tmux or something like that.
[1795.96 --> 1801.12]  If you're in this in-between world, how are you managing your test suite run loop,
[1801.16 --> 1804.50]  and what other tools do you use other than MacBurn to work?
[1808.48 --> 1809.22]  Not much.
[1809.22 --> 1815.42]  I use Xcode just to build, and if possible, I'll just use Xcode build on the terminal,
[1815.96 --> 1820.16]  because I really do love the terminal and navigating through source that way.
[1821.94 --> 1824.52]  But I'm fairly simple.
[1824.80 --> 1830.46]  I just use MacVim, but it could have just as well been text edit, I guess.
[1832.34 --> 1836.80]  So I'm not really the right person to give any information, I think,
[1836.80 --> 1843.08]  on certain speed editing tips or whatever.
[1844.90 --> 1850.96]  By the way, regarding Xcode, I recently heard about AppCode, I think.
[1851.12 --> 1855.58]  I haven't used it myself, but it seems to be that there is an alternative for Xcode.app
[1855.58 --> 1859.74]  if people are feeling that Xcode 4 isn't helping them out.
[1859.74 --> 1861.64]  So that might be a tip.
[1862.26 --> 1868.30]  But I just run tests, things from the terminal like most people in the Ruby community do.
[1869.88 --> 1872.26]  And that's basically it.
[1872.28 --> 1875.32]  I'm not sure if there's anything specific you would want to hear.
[1875.32 --> 1881.34]  So as manager, maintainer of this project, I'm sure that as specs are added,
[1881.50 --> 1887.04]  you're constantly discovering new open source in the Cocoa world.
[1887.26 --> 1890.68]  What are some of the most interesting projects that you've seen come across your radar?
[1892.36 --> 1895.42]  I've seen so many nowadays that I have to really think about that.
[1895.42 --> 1901.28]  Definitely one, because we're so spoiled in the Ruby community with blocks,
[1901.64 --> 1905.42]  is called BlockKit by...
[1906.86 --> 1910.98]  I'm not going to butcher his name.
[1911.24 --> 1911.68]  Let's see.
[1912.30 --> 1913.42]  What is...
[1913.78 --> 1914.98]  We'll add that to the show notes.
[1916.14 --> 1919.46]  Yeah, it's Zachary Waldowski.
[1920.18 --> 1922.78]  BlockKit, that's a very good one.
[1922.78 --> 1928.40]  I use QuincyKit, which is a crash reporter.
[1929.66 --> 1932.22]  So a bit like TestFlight, but another one.
[1934.84 --> 1937.62]  JSONKit, obviously very fast at JSON handling.
[1938.76 --> 1942.12]  It's amazing that we have these naming conventions in our different communities.
[1942.32 --> 1946.56]  So Kit and the Cocoa world is what in Ruby we would at one time
[1946.56 --> 1950.58]  Axaz or Foo or any of these other trendy names.
[1950.58 --> 1957.40]  Yeah, well, I think Kit was originally more like a framework.
[1957.74 --> 1957.94]  I did.
[1958.56 --> 1964.14]  So Kit implies it's a framework, not just one problem solution.
[1964.88 --> 1965.86]  But I'm not sure.
[1966.28 --> 1970.66]  Yeah, but it's definitely an Objective-C Cocoa naming convention.
[1970.66 --> 1975.50]  I wasn't a big fan of the whole XS naming convention, by the way.
[1976.06 --> 1976.66]  It didn't...
[1977.28 --> 1983.02]  It felt like at some point people were just trying to mingle the names into that
[1983.02 --> 1984.30]  and it didn't really...
[1984.30 --> 1986.26]  It wasn't declarative anymore at some point.
[1986.68 --> 1989.28]  But I forgot a few specific names, so maybe just cut that out.
[1989.76 --> 1993.88]  We mentioned TestFlight a number of times, and I'm a big fan of TestFlight.
[1993.88 --> 2001.08]  So for those that don't know, I've used it for iOS applications to do over-the-air betas
[2001.08 --> 2003.20]  to beta users before we put them in the App Store.
[2003.76 --> 2004.20]  What...
[2004.20 --> 2006.56]  I guess that's how you're using it as well.
[2008.08 --> 2008.26]  Yeah.
[2008.64 --> 2010.62]  Well, I used TestFlight.
[2010.74 --> 2014.44]  I used to use TestFlight, but I don't use it anymore.
[2014.66 --> 2016.80]  I've switched personally to a hockey app.
[2017.94 --> 2018.68]  I've seen that one too.
[2018.80 --> 2020.96]  So why do you like hockey over TestFlight?
[2020.96 --> 2025.68]  First of all, I pay hockey apps, so I know I'm the customer.
[2027.58 --> 2028.74]  That might be...
[2028.74 --> 2029.22]  I don't know.
[2029.34 --> 2033.02]  That's my ideological way of how I look at products.
[2033.10 --> 2035.34]  Pay for apps that you use so that you know they'll hang around?
[2036.30 --> 2039.90]  Well, I mean, the more the way...
[2039.90 --> 2042.70]  If you're not paying for the app, then you are the product.
[2042.80 --> 2044.36]  It's more the feeling I get with it.
[2044.36 --> 2052.44]  Also, I wasn't able to upload small binaries stably last time with TestFlight.
[2052.58 --> 2054.84]  So I started to get a bit annoyed about that.
[2055.50 --> 2059.44]  And hockey app is a bit simpler, especially in the way it looks.
[2059.56 --> 2062.76]  It isn't that lickable UI that you have with TestFlight.
[2062.76 --> 2065.60]  But it works for me.
[2065.72 --> 2069.04]  And I just want to be able to upload a binary and have it work.
[2070.08 --> 2078.80]  And they have their crash reporter and also their other beta update SDK.
[2079.18 --> 2080.32]  That's all open source.
[2080.70 --> 2085.08]  I also really like that because I can just dig in and see what it's doing or change something.
[2086.22 --> 2086.34]  Yeah.
[2087.20 --> 2089.54]  But obviously, if TestFlight is working for you, it's working.
[2089.78 --> 2090.22]  I just...
[2090.22 --> 2096.42]  I don't really like the whole, if you're not paying for it, then you're the product type of feeling.
[2097.10 --> 2097.56]  So true.
[2098.28 --> 2100.56]  So who's your open source hero?
[2101.84 --> 2103.96]  I don't have like a real hero hero.
[2103.96 --> 2107.96]  But the one that really taught me a lot of the...
[2107.96 --> 2113.84]  Well, just basic programming stuff as well is definitely Laurent Sanzonetti of Ruby Coco and McRuby fame.
[2113.84 --> 2116.92]  I mean, he's a Belgian, but he does awesome stuff.
[2117.12 --> 2118.06]  You want to hold that against him?
[2119.24 --> 2119.68]  No.
[2120.56 --> 2121.20]  We'll...
[2121.20 --> 2125.26]  I mean, he promised me a lot of good beer.
[2125.56 --> 2127.40]  So we'll figure it out.
[2128.06 --> 2128.68]  Well, thanks, Aloy.
[2128.96 --> 2133.38]  Certainly appreciate your insight into CocoaPods and Objective-C and Ruby.
[2133.46 --> 2134.44]  This is an exciting project.
[2134.62 --> 2138.58]  So we'll help spread the word and hopefully get an influx of new specs into this thing.
[2139.12 --> 2139.84]  Yeah, definitely.
[2140.02 --> 2140.46]  Thank you.
[2140.46 --> 2145.54]  And even if there's just Ruby developers that feel like they want to work on some side project thing,
[2145.60 --> 2147.68]  but don't have a real itch at that time,
[2147.80 --> 2156.28]  I can use any Ruby developer to just give a shout on the mailing list and we'll get you something to do.
[2157.28 --> 2157.60]  Absolutely.
[2158.02 --> 2158.52]  Thanks, Aloy.
[2159.18 --> 2159.66]  Yeah.
[2159.92 --> 2162.44]  Thank you to Wyn and Adam by proxy.
[2162.44 --> 2162.94]  Bye.
[2162.94 --> 2163.02]  Bye.
[2163.02 --> 2163.08]  Bye.
[2163.08 --> 2163.52]  Bye.
[2163.52 --> 2164.02]  Bye.
[2164.02 --> 2164.52]  Bye.
[2164.52 --> 2165.02]  Bye.
[2165.02 --> 2165.08]  Bye.
[2165.08 --> 2165.52]  Bye.
[2165.52 --> 2166.08]  Bye.
[2166.08 --> 2166.52]  Bye.
[2166.52 --> 2167.02]  Bye.
[2167.02 --> 2167.08]  Bye.
[2167.08 --> 2167.14]  Bye.
[2167.14 --> 2167.16]  Bye.
[2167.16 --> 2168.08]  Bye.
[2168.08 --> 2169.08]  Bye.
[2169.08 --> 2169.14]  Bye.
[2169.14 --> 2169.16]  Bye.
[2169.18 --> 2169.20]  Bye.
[2170.46 --> 2171.08]  Bye.
