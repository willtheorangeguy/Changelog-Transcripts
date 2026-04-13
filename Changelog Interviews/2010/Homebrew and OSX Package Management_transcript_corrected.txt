[0.00 → 19.26] Welcome to the Changelog episode 0.3.5.
[19.98 → 20.80] I'm Adam Stokowski.
[21.12 → 22.04] And I'm Wynne Netherlands.
[22.18 → 23.02] This is the Changelog.
[23.06 → 25.02] We cover what's fresh and new in the world of open source.
[25.42 → 28.34] If you found us on iTunes, we're also on the web at thechangelog.com.
[28.34 → 29.38] We're also up on GitHub.
[29.38 → 35.50] At GitHub.com forward slash explore, you'll find some trending repos, some feature repos from our blog, as well as the audio podcasts.
[35.80 → 37.24] And if you're on Twitter, follow Changelog Show.
[37.96 → 38.68] And I'm Adam Stop.
[39.12 → 41.52] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.98 → 44.16] Chatted this week with Max Howell from Homebrew.
[44.58 → 45.56] You're a Homebrew user?
[46.48 → 47.58] Yeah, I aim to be.
[47.64 → 52.36] I think I have it, and I'm using it, and it's made life simpler, but I haven't actually used it in a while.
[52.82 → 57.70] It's let me cut the cord with Mac ports and Fink, some other projects to manage packages on OS X.
[57.70 → 63.42] It's got, I wouldn't say a bad install process, but it's a little beefy for a designer.
[63.70 → 65.82] I was kind of hoping we'd talk against that, but...
[65.82 → 67.76] Training wheels can only come so big.
[68.96 → 69.32] Thanks.
[69.32 → 71.32] I love Homebrew.
[72.16 → 73.52] You know, I especially love the beer theme.
[73.60 → 74.64] We riffed on that quite a bit.
[74.78 → 75.48] Yeah, that was a lot of fun.
[75.74 → 78.24] The notion of kegs and cellars and whatnot?
[78.58 → 83.62] I think it's, you know, we've exposed this in a couple repos we've commented on or had on the podcast in the past,
[83.62 → 90.94] but having fun and humour in the syntax and in the installation processes or the wiki, the documentation.
[91.16 → 91.62] It's kind of fun.
[92.20 → 92.56] Absolutely.
[92.96 → 96.18] You know, one of the things that he said in the interview that I absolutely agree with is,
[96.42 → 100.52] if you're doing an open source project, it's got to be something that, you know, you use yourself,
[100.66 → 102.64] or you won't be motivated to keep it going.
[102.80 → 103.32] Oh, absolutely.
[103.58 → 103.82] Yeah.
[104.26 → 107.24] Mac's built Homebrew to scratch an itch, and it's kind of taken off.
[107.24 → 114.64] So I know that I'm a user, you're a user, and for the folks that are hollering for non-web content, here you go, Homebrew.
[114.96 → 116.52] Yeah, I also want to plug something else as well.
[116.90 → 120.20] We partnered with Jason Heifer of The Ruby Show and The Dev Show fame.
[121.04 → 123.42] He runs a site called GeniusPool.com.
[123.50 → 128.20] It's a job board designed to connect employers and jobseekers in a very targeted manner.
[128.42 → 131.24] It's got this very cool thing called The Genius Pool Network.
[131.90 → 134.80] It gives extra opportunities for promoting your jobs to the right kind of audience.
[134.92 → 135.68] We're a part of it.
[135.68 → 138.02] The Dev Show is obviously in it, and The Ruby Show is in it.
[138.14 → 144.90] So if you're hiring a developer, you can choose the changelog, the dev show, and even the Ruby Show as extra promotion for your job.
[145.06 → 150.56] So head to GeniusPool.com right now, and if you post a job, check the box next to the changelog for an extra $100,
[150.84 → 152.92] and we'll read it on air, GeniusPool.com.
[153.36 → 154.70] Everybody out of the pool.
[156.06 → 156.92] Fun episode this week.
[156.96 → 157.52] Should we get to it?
[157.78 → 158.28] Let's do it.
[165.68 → 174.64] We're joined today by Max Howell, founder of The Homebrew Project, to talk to us about package management on OS X.
[175.06 → 177.56] So Max, why don't you introduce yourself and let the folks know who you are.
[179.02 → 180.12] Well, hi, everyone.
[180.34 → 181.14] I'm Max Howell.
[181.14 → 186.66] I started The Homebrew Project about a year ago, and it's been quite successful.
[187.86 → 191.86] Before that, I started programming when I was six, in fact.
[192.72 → 198.16] My dad came in one day when I was playing Super Mario and insisted I stop, which I wasn't very happy about.
[198.82 → 202.38] But he put me down in front of my computer and started teaching me how to program.
[202.62 → 207.54] And when I realized that I could probably make my own Super Mario, I became more enthusiastic.
[208.72 → 211.04] Since then, I've been doing it on and off.
[211.56 → 214.92] I never really intended to do programming as a career.
[214.92 → 220.52] But having done a chemistry degree, I decided that I didn't like chemistry very much.
[221.28 → 231.10] It wasn't really about changing the world like I expected it to as much as making potions and solutions and small measurements upon them.
[231.96 → 233.72] And I fell back on my programming.
[234.86 → 237.38] So I started working at Lost FM a few years ago.
[237.38 → 250.28] And it was working at Lost FM that made me interested in package management on Mac, because I found the existing solutions to be not exactly to my liking as a developer.
[250.90 → 252.38] But I never got around to doing it.
[253.08 → 255.38] And I was...
[256.90 → 259.48] Well, I was going to say that I work at Tweed Deck now.
[260.52 → 265.32] So I left Lost FM last year, and now I work at Tweed Deck.
[265.32 → 267.56] I work on their mobile and client software.
[267.96 → 268.72] Well, I was the last fan.
[268.80 → 270.92] I worked on their mobile and client software as well.
[271.02 → 271.54] I was a lead developer.
[271.72 → 273.10] I'm a lead developer at Tweed Deck as well.
[274.54 → 275.74] I know Adam's a big Twitter user.
[275.86 → 278.38] Probably has lots of questions on Tweed Deck in a minute.
[278.60 → 279.64] But to talk first...
[279.64 → 280.04] It's pretty great.
[280.86 → 283.20] To talk first about Homebrew.
[283.68 → 287.18] So what led you to kick off the project?
[287.32 → 289.68] Was it just one too many Image Magic installs?
[291.62 → 292.02] Yeah.
[292.44 → 293.36] Stuff like that.
[293.36 → 296.82] I have quite a large Linux background.
[297.54 → 305.84] Before Lost FM, I worked on a project called Amar ok, which was and probably still is one of the bigger music applications on Linux.
[306.66 → 310.00] I joined the project when it was very fresh.
[311.40 → 313.78] But it had potential, I could tell, by looking at it.
[314.72 → 316.60] And I worked on that for two and a half years.
[316.60 → 320.88] And, well, the package management on Linux is mostly great.
[321.34 → 325.56] We always thought there was like a niche area for like a developer package management solution.
[325.72 → 328.08] You don't always want what the system gives you.
[328.08 → 339.40] And while working at Lost FM, I had to do an awful lot of packaging of our software, like the desktop.
[339.60 → 341.52] We did Windows, Mac, and Linux.
[341.52 → 345.38] And I had to manage the packaging of each system.
[345.50 → 346.62] And, God, I hate packaging.
[347.76 → 357.10] C++, which I never really want to have to do again, is a real bitch to package up into a binary or work on all the different systems.
[357.10 → 363.06] And when our client had lots of separate dependencies that were very difficult to manage.
[363.88 → 366.76] And I was using Mac ports, and I was developing on Mac.
[366.90 → 370.70] And I just felt that I couldn't get enough control over what it was producing.
[372.12 → 374.72] And I wanted to have control over it.
[374.82 → 377.34] Quite possibly there's a way to get control over it.
[377.34 → 378.98] But the whole project didn't seem geared around that.
[379.06 → 384.74] It seemed like it was geared around giving people a solution to getting software onto their computers.
[384.74 → 390.58] Well, I wanted a solution for developers that would allow you to get what you needed for the work you were doing.
[391.08 → 399.38] So I would constantly moan about this at the pub every Friday with people there when we were talking about our work for the week.
[399.68 → 401.76] And eventually someone just told me to do it.
[402.52 → 404.36] I was like, well, I guess I could.
[405.80 → 407.86] So one day I just started making it.
[408.12 → 413.20] And within a few hours I had something which was basically great, really.
[413.20 → 414.70] It was the way it really needed.
[414.94 → 420.52] I'd had ideas for a few years about putting things into separate directories and sim linking everything into the main tree.
[420.66 → 424.12] So you could easily manage it without having to use tools.
[424.22 → 430.32] I never understood why you need these elaborate tools for managing small bits of Unix software.
[431.30 → 433.98] These massive black boxes which don't make any sense.
[434.56 → 436.56] Because it's not really that difficult.
[436.64 → 437.30] There's not much to it.
[437.30 → 442.24] So I wanted a system where you could just do it with your own tools if you want.
[442.42 → 447.06] But there is a convenience tool so that you can get things done quickly if you want.
[448.52 → 450.88] So I just started building that.
[451.38 → 457.56] And, well, I put it on GitHub because that's where all the cool people were putting things.
[457.80 → 457.90] Sure.
[457.90 → 462.50] And I chose Ruby because that's what all the cool people were doing, and I wanted to look cool.
[464.24 → 465.84] Although I had done some Ruby.
[466.06 → 470.28] It was admittedly my first big Ruby project.
[470.40 → 472.24] And I liked it a lot, the stuff I'd done before.
[472.32 → 473.38] But it was mostly scripting stuff.
[473.50 → 476.98] As I say, I was really a C++ developer at this point.
[477.04 → 478.20] I hadn't done much Ruby.
[479.72 → 482.40] Which I think you can see in the code base.
[482.82 → 485.06] It does look like a noob wrote it.
[485.06 → 491.92] For the uninitiated, explain a bit about the anatomy of a homebrew package, the formulas.
[494.06 → 494.58] Yeah.
[494.74 → 501.00] So I just wanted something which was as simple as possible that I was going for.
[501.92 → 506.64] So a homebrew formula, a package recipe, is just a Ruby script.
[507.10 → 508.60] It's a class, a Ruby class.
[508.96 → 512.48] And you define some metadata at the top, the minimal amount of metadata.
[512.48 → 516.02] I was like, why do you need all this duplicate metadata for description and stuff?
[516.08 → 519.96] And I've had people say to me at the time since, let's have a description field.
[520.08 → 522.68] And I'm like, well, you know, the web is where the description is.
[522.70 → 523.32] You go to the homepage.
[523.64 → 524.70] So there's a homepage field.
[524.80 → 525.12] That's it.
[525.16 → 525.76] There's no description.
[526.38 → 531.34] So if you want to know what the package is about, you can type broom home and the package name.
[531.58 → 532.28] And then you can see.
[532.28 → 536.52] I didn't want to duplicate all this information and have to keep it up to date.
[536.60 → 540.04] I wanted the minimal amount of work I had to do to keep this project going.
[540.86 → 542.52] I didn't want to have to update description fields.
[543.14 → 549.18] And then there's an installation function, which literally just runs the scripts that are required to install the thing.
[549.64 → 551.72] And it installs it into its own prefix.
[551.72 → 562.18] So if you've installed Homebrew to user local, there's a directory in their called Seller, which is part of the beer theme, which I'm proud of.
[563.64 → 568.44] And inside that, there's like, say, get is what you're installing as a get folder.
[568.54 → 570.60] And inside that, there's another folder, which is the version.
[571.74 → 572.78] And so it installs there.
[572.82 → 574.42] And then it just sim links it into user local.
[574.88 → 577.38] So you have these encapsulated folders.
[577.66 → 579.24] It's the Gov Linux approach.
[579.24 → 580.84] This is where I got the idea from.
[580.88 → 581.44] It's not mine.
[581.84 → 582.30] Gov Linux.
[582.58 → 584.70] And maybe they didn't even invent this.
[584.98 → 587.36] Like, I'm sure they would like to claim they did.
[587.44 → 590.44] But, you know, I've heard of other projects doing similar things before.
[590.78 → 594.62] But it just seemed like a sensible way to do it from an auxiliary package manager for OSX.
[594.62 → 598.02] And Homebrew really tries to complement the system.
[598.36 → 601.66] It's not trying to, like, be its own autarky like Mac Ports does.
[601.74 → 603.44] That's one of the things I didn't like about Mac Ports.
[604.36 → 606.28] But, so yes, the formula has an installation function.
[606.38 → 608.04] It has a few other little bits of things.
[608.04 → 613.96] Like, you can show some caveats in case there's, like, some issues that the person installing the package needs to know.
[614.00 → 616.40] And that's one of the things about Homebrew that is also the case.
[616.84 → 620.22] It's not meant to, like, hold your hand too much.
[620.92 → 623.26] It does the bare minimum, which is installed the software.
[623.36 → 626.34] And then it tells you what the issues are after that.
[626.40 → 627.50] So you can deal with it.
[627.50 → 628.24] Because you're smart.
[628.52 → 629.10] You're a developer.
[629.50 → 630.44] You know what's going on.
[630.44 → 636.36] So I want you to have the power to do what you need with the software you're installing.
[637.88 → 639.86] So let's talk about that a little bit.
[639.92 → 647.36] In the installation, you mentioned to delete these two different directories, user local include and user local lib.
[648.10 → 652.22] Can you talk about that a bit and why and what kind of trouble is sprouted about when you don't do that?
[652.22 → 656.46] Well, you know, this is why I don't like C++ and all that anymore.
[656.72 → 660.74] The entirety of the Unix system is complicated.
[662.76 → 671.86] Basically, user local as a directory will get included when you install C software, whatever, really.
[672.06 → 675.42] There is very little we can do to stop it from using those directories.
[675.42 → 688.26] So if you have libraries or include files or headers in there which conflict with the package you're trying to install, it will cause problems and bugs, which it's very difficult for us to prevent.
[689.58 → 693.04] So really, the best bet is just to start fresh there.
[693.68 → 698.76] And we made this brew doctor command in the end because, you know, we try to minimize the amount of support we have to do.
[698.82 → 703.10] We want to help you to help yourselves when you're using Homebrew.
[703.10 → 708.34] So as you're deleting some of these things, then the next thing you're going to do is you're going to start doing some installation stuff.
[708.50 → 710.92] So the next thing that comes to mind is when to sudo.
[711.06 → 715.24] What's up with the whole solution here with Timbre and sudo?
[715.74 → 721.22] Well, because we're installing from source, sudo is dangerous.
[721.54 → 725.04] There's massive installation scripts that get run, but you can't know what they're doing.
[725.14 → 730.06] And I've seen running a file system watcher to see what stuff goes on.
[730.06 → 735.68] Some of these packages try to edit core system files, and you just don't know what it's going to do.
[736.44 → 737.30] There are ways around that.
[737.38 → 742.80] And Mac Port puts everything in a chown root directory, which is the sort of thing that maybe we should do.
[743.20 → 748.24] But instead, we're making a simple solution here.
[750.76 → 753.84] So no sudo is a very sensible thing to do.
[753.96 → 755.54] And it feels like OSX, doesn't it?
[755.54 → 758.16] You install TextMate without having to sudo.
[758.52 → 764.24] You don't, you know, chown it to root after you've copied it into your applications' directory.
[765.36 → 769.96] Admittedly, some of the packages you can install with Homebrew, it would make sense to root them.
[770.06 → 774.42] But we trust you as the guy installing the software to know what you're doing, basically.
[774.60 → 779.38] That's kind of the distinction between Homebrew and the other options.
[779.38 → 785.84] Homebrew really is for developers, who most of the time probably are just installing a few dependencies.
[786.12 → 790.84] They need to compile the gems or the Python eggs that they need to use.
[791.62 → 798.16] So we trust you to know what you're doing, basically.
[799.56 → 801.20] And sudo is an inconvenience.
[801.20 → 807.74] Once you've not used sudo to install stuff, you realize it was holding you back.
[807.74 → 814.60] Like, it's much easier to edit the packages you're installing and customize them how you want if you're not using sudo the whole time.
[815.12 → 824.80] I've seen people be adamantly against it because, especially if they come from Linux, it's the mentality there that all the packages should be installed with root command.
[825.22 → 827.26] And, like, you know, there's security implications.
[828.02 → 829.74] Let's talk about dependencies for a moment.
[829.74 → 835.36] So how does Homebrew manage dependencies between kegs and packages?
[835.36 → 838.22] In a very basic fashion.
[838.92 → 849.42] It has a depends on piece of metadata for each formula, which is just a name which directly correlates to the file name of the other formula.
[849.58 → 851.56] The formula are just files on the system.
[851.68 → 854.86] That's how we resolve unique naming.
[855.28 → 856.82] The file system is used all over Homebrew.
[856.94 → 859.66] Like, when I designed it, I wanted just a very simple system.
[860.24 → 861.92] Simple systems are the ones that work.
[861.92 → 867.86] They're the ones that succeed without anyone having to do too much work.
[868.04 → 869.64] And also they're the ones with the least bugs.
[869.96 → 872.48] So it just resolves to another file.
[872.74 → 875.62] And the packaging system installs that.
[876.12 → 880.48] There isn't anything particularly advanced that other packaging systems have where you can specify versions and stuff.
[880.54 → 882.06] It's not that we don't plan this sort of stuff.
[882.46 → 884.84] It's just in a very typical open source fashion.
[884.84 → 887.52] We've done what we've needed as we go.
[888.20 → 891.42] And we haven't needed anything more advanced yet.
[891.90 → 896.02] I'm kind of hoping at some point someone will need something more advanced, and they'll submit as a patch.
[896.68 → 898.74] And that's basically happened for the whole project.
[898.90 → 901.80] Because we based it on GitHub, it had amazing uptake.
[902.50 → 905.66] And very, very easy for people to contribute.
[905.90 → 906.70] Like, nothing else.
[906.92 → 908.24] The whole system is based on Git.
[908.24 → 913.86] I don't know if people realize this about Homebrew, but you install it and that's a Git repository you've just put somewhere.
[914.06 → 915.46] You can put it anywhere you like as well.
[915.74 → 917.06] I don't know if people realize that.
[917.58 → 918.56] Put it in your home directory.
[918.90 → 923.66] We recommend user local because it makes it so much easier to install stuff.
[923.94 → 926.02] Especially gems, like Ruby gems.
[926.14 → 929.42] People put it in their home directory because they're like, well, I don't want to mess around with user local.
[929.94 → 931.78] It's in the user directory.
[932.00 → 934.64] I don't know what that is or whatever they're thinking.
[934.64 → 938.14] I'm sure they have excellent reasons for what they choose.
[938.78 → 942.66] And it makes it a lot harder to install gems because this is the problem with C code.
[942.88 → 943.90] It's what people don't realize.
[944.74 → 947.22] It has default directories.
[947.34 → 948.34] It looks for stuff.
[948.98 → 953.26] And this is why installing gems off of Mac ports is always so much of a pain in the bum.
[953.78 → 956.44] It was going to say arse there.
[956.56 → 957.24] I hope you guys realize.
[958.96 → 960.08] Although maybe you want that.
[960.22 → 961.00] So I'll repeat it.
[961.30 → 962.42] Such a pain in the arse.
[964.56 → 966.18] Because it was in local.
[966.56 → 967.64] And you had to tell the gem.
[967.64 → 971.30] And every gem has its own way of knowing where to look for dependencies.
[971.50 → 974.40] And you have to Google and find a blog post where someone's done it before.
[974.82 → 975.82] Install everything to user local.
[975.92 → 976.48] It just works.
[977.56 → 978.84] Anyway, what was I saying?
[980.58 → 982.00] You can install it wherever you like.
[982.58 → 984.82] And it's just a Git repository.
[985.02 → 986.02] So you can edit anything.
[986.12 → 987.76] And that's one of the beauties of Homebrew as well.
[987.76 → 994.18] It's a system that builds from the ground up for you to be able to manipulate exactly how you want.
[994.44 → 996.04] It sort of packages how you want.
[996.36 → 998.24] No messing around with variants and things like that.
[998.32 → 1000.26] Just edit the formula yourself.
[1000.26 → 1003.62] Make it add the extras you need.
[1004.68 → 1005.16] Et cetera.
[1005.24 → 1007.12] And then just commit that to your own fork on GitHub.
[1007.40 → 1008.82] And then you just keep pulling from mine.
[1009.18 → 1011.18] And Git manages all the merging for you.
[1011.56 → 1013.88] And you've got this almost magical system.
[1014.08 → 1016.08] That's what I wanted from this whole system.
[1016.62 → 1022.00] Something where I could manipulate it as I needed for the projects I was working at work and home.
[1022.00 → 1027.26] And it just took the pain out of dealing with these other dependencies and bits of software.
[1028.00 → 1029.88] And that's really the ultimate goal.
[1030.46 → 1033.00] When I started the project, I also had other ridiculous goals.
[1033.26 → 1040.36] Like everything should be highly optimized and ridiculously fast and no universal binaries because we don't need those, et cetera.
[1041.10 → 1047.44] And as the project became more popular, it became apparent that these were ridiculously impractical goals.
[1047.58 → 1050.90] It's kind of stuff that Gen2, you know, Gen2 is one of the Linux distributions.
[1050.90 → 1057.10] Where it's renowned for its users wanting to optimize to 11 for everything.
[1057.46 → 1059.84] And I was kind of going down that route just for the fun of it.
[1059.94 → 1062.76] And I've, you know, since rejected that policy.
[1062.90 → 1064.58] Although not everyone's happy about that.
[1064.62 → 1065.40] They seem to want it.
[1065.46 → 1068.40] But the important thing is the system is practical.
[1068.84 → 1070.18] It's useful to you.
[1070.34 → 1072.42] And that's what I try to maintain.
[1073.82 → 1077.68] So talking about formulas, you're pushing 2,700 watchers right now.
[1077.80 → 1078.00] Yeah.
[1078.00 → 1081.36] How many formulas are out there, and what are some of your favourites?
[1081.82 → 1082.72] I can tell you.
[1082.98 → 1083.82] Because that's the thing.
[1083.98 → 1087.14] Like, you just step into the homebrew directory.
[1087.84 → 1088.58] So let's go there.
[1088.70 → 1090.96] That's what I'm doing right now in my terminal while you wait.
[1091.58 → 1094.22] Except it's not responding to my clicks.
[1094.50 → 1094.64] Okay.
[1094.82 → 1095.04] All right.
[1095.04 → 1097.30] So I go into user local.
[1097.68 → 1098.72] Then I'll go into library.
[1099.02 → 1100.84] Because I chose the library name, incidentally.
[1100.90 → 1104.86] Because it's an OSX thing.
[1104.96 → 1109.48] People think that cellar and library, it's like a room theme that I came up with.
[1109.54 → 1110.78] But no, the theme is beer.
[1110.78 → 1111.42] All right.
[1111.48 → 1111.94] I got to be.
[1113.02 → 1116.14] This is like when I was in the pub, and we were discussing this project.
[1116.26 → 1118.88] I was like, okay, well, what am I going to call it?
[1119.38 → 1120.00] What am I going to do?
[1120.06 → 1121.82] And like someone suggested I have a beer theme.
[1122.08 → 1123.56] I was like, yeah, excellent.
[1124.58 → 1125.50] That will be fun.
[1125.92 → 1135.12] And like as much as now it seems a little unprofessional, it does help with your open source projects to have something fun about it.
[1135.12 → 1138.06] Because it makes people tweet about it, and it makes people blog about it.
[1138.12 → 1140.16] And they're like, oh, I found this project and I thought it was funny.
[1140.28 → 1145.74] They had like a beer theme and there was formula and there was a cellar and things were installed into kegs, et cetera.
[1145.80 → 1149.48] And if you go through the source code, it's kind of full of beer jokes, incidentally.
[1149.62 → 1151.22] I don't know if that's your sort of thing.
[1152.08 → 1152.44] Absolutely.
[1153.60 → 1156.38] It's not a good source code, but it's full of good comments.
[1157.48 → 1158.10] So let's see.
[1158.10 → 1165.48] There's 1167 formulae currently, which is pretty good going.
[1165.64 → 1168.64] Like when I started the project, there was five, and I added them as I needed them.
[1168.94 → 1175.44] And then like after like a month or so, the project turned up on a few people's radars and I got a few contributions here and there.
[1175.52 → 1179.10] And as I was saying about being on GitHub, it's just great.
[1179.42 → 1181.24] It makes it so easy for people to contribute.
[1181.38 → 1183.08] They just throw stuff at me.
[1183.08 → 1188.00] And for the first like few months of the project, I struggled to keep up with contribution.
[1188.26 → 1193.72] After it took off, like it only took off when Josh Peake from 37 Signals tweeted about it.
[1194.06 → 1199.04] He was like, I'm going to install Snow Leopard because it was just before Snow Leopard came out last year.
[1199.42 → 1200.82] The project is like a year old.
[1200.90 → 1201.46] That's about it.
[1201.78 → 1204.60] I started building it after I left Lost FM.
[1205.10 → 1208.54] I started before then, and I just continued at that point.
[1208.54 → 1213.34] And he said, I'm going to source Snow Leopard, and I'm going to use Homebrew to manage my package.
[1213.52 → 1215.20] And it was perfect timing in that respect as well.
[1215.26 → 1218.34] People were installing fresh installations of OSX.
[1218.48 → 1220.38] They were kind of looking for an alternative.
[1221.52 → 1225.20] And after that happened, I got like 50 forks that week.
[1225.26 → 1227.84] And then it went up to like 200 in a couple of months.
[1228.18 → 1230.92] And since then, it's just it's been ridiculous, the amount of forks.
[1230.92 → 1237.64] People kind of fork, contribute, make a pull request, and then they keep their fork around.
[1237.78 → 1241.42] Maybe they do another pull request here and there for like formula.
[1241.84 → 1245.84] I did design the system to be ridiculously simple to contribute to.
[1246.44 → 1249.06] That was one of the things I didn't like about Mac ports.
[1249.18 → 1252.50] I just didn't know how to contribute if I had a contribution.
[1252.50 → 1262.00] So you can type brew create at the command line and then the URL for the tarball for the thing that you're trying to make a formula for.
[1262.30 → 1266.74] And it automatically generates you the formula as best it can.
[1267.02 → 1268.68] So you'll probably have to tweak it a little bit.
[1268.90 → 1272.46] But at that point, you maybe already have a contribution to the project.
[1273.50 → 1275.12] That has really helped.
[1275.12 → 1282.42] So we are the most forked project on GitHub now since Rails disappeared a few weeks ago.
[1282.50 → 1283.12] I don't know what happened.
[1285.00 → 1290.90] But I can't exactly claim that's completely because it's the most exciting project.
[1291.20 → 1293.84] It is really because it's just so easy to contribute to it.
[1294.40 → 1298.32] People feel almost that it would be wrong if them not to because I made it so simple.
[1299.10 → 1302.36] So people, do they buy you beer whenever you meet up with them at Meetup?
[1302.76 → 1304.04] And what's your favourite?
[1304.04 → 1309.28] I've certainly had a few threats of pints.
[1309.52 → 1314.68] But, well, the problem is we're in London and there isn't such a thriving Ruby community here.
[1315.20 → 1317.50] It's certainly here, and I won't deny it.
[1317.56 → 1321.34] But I feel that it's more in the States.
[1321.84 → 1325.62] So, well, if anyone ever wants to invite me over for some of those conferences, I'll certainly come.
[1327.10 → 1328.20] But my favourite beer?
[1328.36 → 1332.28] Well, I'm a big fan of the British Ales as it happens.
[1332.28 → 1334.00] I don't know if you guys ever tried one.
[1334.36 → 1334.90] Favourite brand?
[1336.00 → 1337.34] No, British Ale.
[1337.72 → 1338.92] Oh, is that the actual brand?
[1339.22 → 1339.88] I just thought that was a...
[1339.88 → 1341.34] No, it's a type of beer.
[1341.48 → 1342.40] Oh, yes, yes.
[1342.96 → 1343.86] The type, right?
[1344.40 → 1344.80] Yeah.
[1344.96 → 1349.78] Like you have your microbrews in the States, and they tend to be pale ales and IPAs.
[1349.90 → 1350.48] And they're very nice.
[1350.54 → 1351.30] I really like them, actually.
[1351.78 → 1354.46] But we have, like, the stuff that tastes a bit like pond water.
[1354.84 → 1359.40] But you become, like, used to the taste and there's some really nice stuff.
[1359.96 → 1364.02] My favourite is probably there's a new brewery called Brew Dog, which is a Scottish brewery.
[1364.02 → 1368.94] They're the ones making these crazy beers you might have heard of that, like, 42%.
[1368.94 → 1371.36] And they brew them in a whiskey-type fashion.
[1372.06 → 1373.74] But they do some normal stuff as well.
[1373.82 → 1375.52] And they've got this one that's a hardcore IPA.
[1375.66 → 1375.90] It's cool.
[1375.98 → 1378.82] And it's got, like, an interesting picture on the front.
[1378.82 → 1381.24] They've got a very clear identity of brand.
[1381.36 → 1382.86] But the beer tastes delicious as well.
[1383.10 → 1385.32] 42% alcohol volume as in 80%?
[1385.32 → 1385.62] Yeah.
[1386.02 → 1386.26] Wow.
[1386.26 → 1387.96] It's a beer which is distilled.
[1388.44 → 1390.06] They distill it with ice.
[1391.04 → 1392.28] It almost doesn't count.
[1392.44 → 1395.46] It's not very nice, actually, the Nuclear Penguin.
[1396.78 → 1399.40] It's the Tactical Nuclear Penguin is what they call it.
[1399.94 → 1400.80] I could give a hug to that.
[1401.54 → 1403.30] It's, yeah, interesting.
[1403.30 → 1411.64] But, yeah, the beer thing was kind of, well, you know, I work in Old Street, which is, it
[1411.64 → 1419.94] has been coined the Silicon Roundabout, which we say with some chagrin.
[1420.76 → 1424.98] But there are a lot of startups here, and we do meet up a lot.
[1425.28 → 1430.84] And there are a lot of pubs, and we tend to discuss our work with a few pints.
[1430.84 → 1435.56] So, yeah, the beer has been a part of my life, I guess.
[1435.76 → 1437.30] And that was part of the reason for the theme.
[1438.48 → 1440.58] So you built the Scrabble over at Last.fm, is that right?
[1441.28 → 1442.16] Yeah, exactly.
[1442.46 → 1445.40] I worked on all the client-side software.
[1446.16 → 1447.02] Are you a music guy?
[1448.08 → 1451.72] Yeah, well, you know, worked on Amar ok for three years.
[1452.12 → 1455.20] I've always been into my music, mostly for consumption purposes.
[1455.42 → 1458.64] I got into Amar ok because I was interested in making the perfect music application.
[1458.64 → 1460.22] And to a certain extent, we did.
[1460.28 → 1461.60] At the time, it was revolutionary.
[1461.90 → 1463.02] There was nothing like it.
[1463.30 → 1469.40] And we pioneered concepts like sticking the wiki page for the artist in the app so while
[1469.40 → 1473.94] you were listening to music, you could see what the artist was if you hadn't discovered
[1473.94 → 1474.50] them before.
[1475.56 → 1477.22] There was nothing particularly like it before.
[1477.32 → 1482.20] And we were, like, heavy users of Last.fm metadata and data as well, which is how I got
[1482.20 → 1486.00] the job at Last.fm in the end, which is, like, a testament to working on open source
[1486.00 → 1488.16] can get you jobs at cool companies.
[1489.28 → 1491.80] So now you're over at Tweet Deck working on mobile, right?
[1492.44 → 1492.66] Yeah.
[1492.84 → 1494.26] Slinging Objective-C or?
[1495.16 → 1499.14] Well, I just did the Android app, which is in public beta at the moment, but we're going
[1499.14 → 1502.60] to be releasing, like, to the Android marketplace soon.
[1503.26 → 1504.08] So that's a great app.
[1504.50 → 1506.04] You should try it if you're on Android phone.
[1506.04 → 1511.90] So we decided to try something different with the Android app to what Tweet Deck does currently.
[1512.12 → 1513.24] Like, you might know the iPhone app.
[1513.74 → 1517.60] And we wanted to do new stuff and see what people's reaction was to it.
[1518.18 → 1519.40] And it's a great app.
[1519.50 → 1520.18] Really pleased with it.
[1520.30 → 1521.10] I love making apps.
[1521.36 → 1522.18] That's where all this comes from.
[1522.32 → 1523.28] I love making little things.
[1523.80 → 1527.18] What's your take on the state of open source on OS X?
[1528.00 → 1530.90] That's the best platform for us, open source, in my opinion, currently.
[1531.80 → 1532.98] I came from a Linux background.
[1532.98 → 1539.70] I switched to Mac tentatively because I appreciated the fact that the UI was solid, and I wouldn't
[1539.70 → 1543.78] have to worry about my Wi-Fi drivers anymore and things like that.
[1543.86 → 1547.84] The only amount of times I'd recompile my kernel to make the Wi-Fi work, and I was sitting there
[1547.84 → 1552.92] thinking, I want to be writing my software, not messing around with the kernel.
[1553.36 → 1555.16] And so in the end, I was like, okay, Mac looks pretty good.
[1555.22 → 1555.94] There's Unix underneath.
[1556.10 → 1556.98] I've beenn't Unix.
[1557.48 → 1561.92] I don't know where we'd be right now with OS X being a popular platform like it is with
[1561.92 → 1562.40] developers.
[1562.40 → 1565.02] The Unix underpinning is essential, in my opinion.
[1566.08 → 1569.04] And it had a nice GUI and everything just about works.
[1569.66 → 1574.20] And I started to find that there was a lot of really quality open source stuff on OS X.
[1574.38 → 1583.00] It's funny how Apple's passion for polish and good work comes through in what people expect
[1583.00 → 1584.90] their own apps should be like.
[1584.98 → 1591.74] People aren't happy with it being, I dare not say and offend Linux people, but it is more
[1591.74 → 1592.30] mediocre though.
[1592.36 → 1594.54] I worked on the UI stuff for ages.
[1594.76 → 1598.40] I did two of my own apps there, which I felt I put a lot of time into.
[1598.58 → 1601.10] But it's a bit messy.
[1602.12 → 1605.04] And you see apps like Transmission and VLC on Mac.
[1605.18 → 1608.38] And they're much better than the equivalents of other places.
[1608.42 → 1609.54] And that's the GUI stuff.
[1609.54 → 1615.12] So speaking of OS X, do you have any other plans or any other ideas that you're brewing?
[1615.12 → 1619.92] I got ideas for homebrew.
[1620.06 → 1621.82] I think it should integrate more with the system.
[1623.20 → 1626.82] Initially, I wanted people to use it.
[1627.00 → 1631.96] So I designed it so that it was self-contained in its own directory, so that you could just
[1631.96 → 1632.54] delete it.
[1632.74 → 1634.62] And you know that everything's gone.
[1634.72 → 1635.62] There's no messing around.
[1635.62 → 1638.98] But it's not so useful in that manner.
[1639.22 → 1644.22] Like, you need to be able to have, for instance, jar files for Java developers.
[1644.38 → 1646.14] They need to go in library slash Java.
[1646.90 → 1650.02] Otherwise, you have to mess around with your system some more.
[1650.36 → 1656.42] So I feel that if you install to user local, you're saying that we should put things in
[1656.42 → 1657.62] the places they should go.
[1657.88 → 1660.52] And we do it via symlinks, so you can still delete it.
[1661.02 → 1662.40] That's the kind of thing I'm thinking of.
[1662.40 → 1665.90] I often play around with ideas for tools that I could use.
[1666.26 → 1671.40] I really want an app, which, since my menu train just tells me when people I'm working
[1671.40 → 1675.38] with are committing to projects that they've forked from me.
[1675.90 → 1678.44] And it pops up, et cetera, with growl.
[1679.44 → 1682.98] Things like that, I always almost sit down on Saturdays and do.
[1683.54 → 1685.92] I've got loads of little apps I've built on GitHub.
[1685.92 → 1692.60] My little app that shows you pictures your friends have taken on Flickr and on the dashboard.
[1693.06 → 1695.80] Because otherwise, I never go there, and I never see that stuff.
[1696.66 → 1703.38] And I wrote an app for, a web app for showing you comics that you're interested in.
[1704.24 → 1707.72] So I just wanted a place I could go, and I click next, next, next, next.
[1707.86 → 1709.74] And every day, and it shows me all the comics.
[1709.74 → 1711.78] And so I do these things.
[1712.02 → 1713.58] But on the iOS X itself, I don't know.
[1714.06 → 1717.34] I kind of feel that the future is mobile nowadays, I have to say.
[1717.42 → 1723.30] But that's just a consequence of the industry I'm kind of working in, my job.
[1723.52 → 1725.18] You mentioned the Android app.
[1725.36 → 1727.06] So iPhone or Android?
[1727.06 → 1727.14] Android?
[1729.46 → 1733.88] Honestly, and I think this will cause me some problems.
[1734.12 → 1736.34] I prefer iPhone, I have to say.
[1738.28 → 1740.94] But Android is a very exciting platform.
[1741.08 → 1741.92] It's definitely up and coming.
[1742.12 → 1745.24] And the flexibility and the things you can do with it are very interesting.
[1747.12 → 1753.82] Just right now, I'd rather have an iPhone because it's got the better apps.
[1754.34 → 1755.66] And they're more polished.
[1755.66 → 1760.60] And there isn't a perfect Android handset yet.
[1760.66 → 1762.28] I've heard good things about the Droid X.
[1762.44 → 1766.28] I've heard good things about the G2, which will hopefully come out soon.
[1766.90 → 1768.68] And the Galaxy Tab looks great.
[1768.78 → 1770.52] I've seen Screech on some of my apps running on it.
[1770.62 → 1773.92] I'm like, yes, I'm begging Google to give me one.
[1774.02 → 1775.08] But I don't think they will.
[1777.52 → 1780.24] But, yeah, currently the iPhone is pretty awesome.
[1781.16 → 1782.74] So we're at that point where we kind of wrap up the show.
[1782.74 → 1787.08] But before we go, we always ask what our guests have on their open source radios.
[1787.16 → 1790.46] So what's out there that's in open source that's got you excited and just want to play with it?
[1790.46 → 1797.12] I'm pretty interested in the Mac branch of VLC.
[1797.12 → 1802.66] VLC, the Glasses, is it the Glasses branch?
[1803.12 → 1807.00] I have that on my GitHub radar and I watch it myself and I forget exactly what it's called, I'm afraid.
[1807.74 → 1810.88] But, you know, they're trying to do a proper Mac app for VLC.
[1811.14 → 1818.36] And every other Saturday I sit down and promise everybody that I'm going to make a great Mac music app.
[1818.36 → 1820.96] Like, it's just the sort of thing I'm never going to have time for.
[1821.18 → 1823.02] So I am interested in what they're doing with VLC.
[1823.26 → 1825.88] I almost have contributed to that several times myself.
[1827.64 → 1833.46] It's difficult with open source because there are not many good apps on mobile being done now.
[1833.62 → 1836.96] I think the most exciting area of open source right now is definitely server-side stuff.
[1837.50 → 1842.52] And I don't personally deal with that very much nowadays, apart from through homebrew, of course.
[1842.86 → 1844.88] Like you asked me earlier what my favourite homebrew package was.
[1844.88 → 1846.40] I think it's definitely SL.
[1846.92 → 1851.78] It's the app that when you typo LS, you get a chop-chop train coming across the screen.
[1852.62 → 1853.08] It's great.
[1853.44 → 1854.94] I was like, I'm like, yeah.
[1855.68 → 1857.68] I always committed a typo for brew.
[1857.84 → 1860.38] I don't know what the common one would be, which would do something similar.
[1862.68 → 1863.64] Any more questions, Winn?
[1863.88 → 1864.42] No, that's it.
[1864.46 → 1864.82] You want to wrap?
[1865.44 → 1872.68] The only thing I wanted to riff on really was the I kind of do like your idea for the notification thing for repos and stuff like that.
[1872.68 → 1883.16] It could be a really fun tool to have because I know for me, I hate to sit there and watch my homepage more or less, just watch that stuff.
[1883.26 → 1885.74] But I guess we do have to get tailback up, Winn.
[1886.26 → 1887.46] It's in process.
[1887.46 → 1890.22] Yeah, well, I think it would be really useful.
[1891.40 → 1898.28] Just to see, especially, we use GitHub at Tweed deck at work through my recommendation, as I would, I guess.
[1898.82 → 1901.12] And we have private repos for everything.
[1901.32 → 1909.98] I want us to release some open source, and we probably will at some point just for the sake of looking like one of those brand names like Facebook where they have a GitHub presence.
[1909.98 → 1917.46] But I have some stuff I did with the Android project, which would be useful, just tools I wrote, which facilitated some easier Android development.
[1918.62 → 1925.08] Well, hey, Max, we really appreciate you taking the time to spend some of your afternoon, I guess, what's that, late night for you over there?
[1925.70 → 1926.22] Evening, yeah.
[1926.72 → 1927.24] Yeah, late evening.
[1927.40 → 1930.96] So we appreciate you taking the time to spend with us, and appreciate you coming on the show.
[1931.44 → 1931.80] Pleasure.
[1932.00 → 1932.26] Thanks.
[1932.26 → 1932.32] Thanks.
[1932.32 → 1932.34] Thanks.
[1932.34 → 1932.38] Thanks.
[1932.38 → 1932.40] Thanks.
[1932.40 → 1932.42] Thanks.
[1932.42 → 1932.44] Thanks.
[1932.44 → 1932.52] Thanks.
[1932.52 → 1934.38] Thanks.
[1934.38 → 1936.38] Thanks.
[1936.38 → 1936.44] Thanks.
[1936.44 → 1936.46] Thanks.
[1939.98 → 1940.06] Thanks.
[1959.24 → 1963.74] Thanks.
[1964.38 → 1965.84] Thanks.
[1965.84 → 1966.72] Thanks.
[1968.32 → 1968.88] Thanks.
[1968.88 → 1968.94] Thanks.
[1968.94 → 1969.88] Thanks.
[1969.88 → 1969.94] Thanks.
[1969.94 → 1969.96] Thanks.
