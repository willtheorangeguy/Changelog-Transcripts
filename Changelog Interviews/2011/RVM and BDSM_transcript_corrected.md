[0.00 → 1.96] This week's episode is brought to you by Harvest.
[2.10 → 4.42] Harvest is a web-based time tracking application
[4.42 → 8.24] relied on by creative teams and freelancers in over 100 countries.
[8.64 → 12.14] With Harvest, you can easily track your billable time and invoice for it too.
[12.52 → 16.12] If you're on the go, Harvest has native iPhone and Android companion apps
[16.12 → 19.76] that make it easy to track time and expenses from anywhere in the world.
[20.30 → 24.18] Try Harvest today with a 30-day free trial at GetHarvest.com
[24.18 → 29.20] and use coupon code LIFESAVER at checkout to get 50% off your first month billing.
[30.00 → 48.78] Welcome to the Changelog episode 0.6.6. I'm Adam Stachowiak.
[48.78 → 52.32] And I'm Won Netherlands. This is the Changelog. We cover what's fresh and new in open source.
[52.80 → 56.76] If you found us on iTunes, we're also on the web at thechangelog.com. We're also up on GitHub.
[56.76 → 61.56] Head to gethub.com. You'll find some trending repos, some feature repos from our blog,
[61.66 → 66.58] as well as the audio podcasts. And if you're on Twitter, follow Changelog Show and me, Adam Stack.
[67.18 → 69.56] And I'm Penguin, P-E-N-G-W-Y-N-N.
[70.10 → 75.76] Fun episode this week, talked to Wayne Seguin from, I guess, Engine Yard fame as of late.
[76.06 → 78.16] Probably know him from RVM.
[78.86 → 79.86] Definitely using RVM.
[79.86 → 90.08] RVM is the bomb. Also talked about BDSM, not what you're thinking about, but a Ruby scripting environment that's on the show.
[90.14 → 95.14] I kind of asked if it was part homebrew, part chef, part RVM.
[95.24 → 100.00] And he answered indirectly, yes. So it's kind of all those things kind of mismatched together. It's really fun.
[100.24 → 103.42] Is this the same BDSM that Steve posted about two days ago?
[103.66 → 105.32] It is. One and the same.
[105.32 → 109.64] Steve's played with it a bit, so he did a quick post on the blog last week.
[109.84 → 119.42] But it's fun if you like to have your own scripting environment that's the same on your local machine and all of your Unisexes as you deploy your codes.
[119.80 → 120.02] Gotcha.
[120.26 → 121.72] A couple of quick programming notes.
[121.88 → 125.40] So we'll be in Austin, Texas for Lone Star Rubicon.
[125.46 → 132.24] We'll be doing our Design Eye for the Dev Guy slash Gal all-day training on Tuesday, August 11th.
[132.24 → 136.32] And I'll be giving a TI talk on the 12th, so look us up if you're there.
[137.50 → 142.34] Madison Rubicon, August 18th through the 20th up in Madison, Wisconsin.
[142.46 → 149.42] Our buddy Steve Planck is going to be giving a talk up there, contributor to the show, co-host actually on this episode as well.
[150.26 → 155.34] Also featuring Scott Charon and some other friends of the show up in Madison.
[155.98 → 156.56] Good stuff.
[157.62 → 158.02] Absolutely.
[158.92 → 160.12] Fun show this week. Should we get to it?
[160.28 → 160.84] Let's do it.
[160.84 → 173.88] Charting today with Wayne Seguin from RVM fame.
[174.14 → 177.60] Wayne, for those that don't know, why don't you introduce yourself and a little bit about who you are.
[178.20 → 188.32] My name is Wayne Seguin, and I wrote a small 8,000 line or so shell scripting framework for managing Ruby environments.
[188.32 → 191.18] You can find it at RVM.beginrescuin.com.
[192.06 → 198.80] And in addition to that, I've also written a new framework for system-level shell scripting called BDSM.
[199.60 → 203.10] And that you can find at BDSM.beginrescuin.com.
[203.10 → 213.76] I also currently work for Engine Yard under the auspicious personality of Dr. Nick, who has been known to wear fairy costumes.
[213.76 → 218.24] We've had Dr. Nick on the show.
[218.56 → 219.94] Lively personality, to say the least.
[220.26 → 223.32] So what was the driver behind RVM?
[223.44 → 225.02] Some pain that you were trying to relieve?
[225.68 → 226.40] Yes, actually.
[226.40 → 232.20] Basically, I left Engine Yard during my – I had an initial run at Engine Yard.
[232.40 → 235.40] I left Engine Yard, and then I went to work for another company.
[235.76 → 243.80] And they were trying to – what they hired me for was to help with their infrastructure setup and deployments and all that stuff.
[243.86 → 244.66] So I came in there.
[245.12 → 248.18] And what they needed originally was they had three projects.
[248.18 → 254.00] One was on Ruby, one was on 1.8, and then their new project they were starting out was on 1.9.
[254.84 → 266.52] And we had to run all three of those Ruby's, and there was really no nice and clean way to be able to bootstrap those three Ruby's and to be able to manage their applications.
[266.52 → 285.36] They needed a way to be able to have their development environment and their CI, QA, production, demo, staging, all those environments identical without having to go through too much pain or time.
[285.58 → 290.34] So I wanted to learn more about shell scripting, get better at it.
[290.34 → 306.84] So I basically sat down and taught myself shell scripting, found the best sources for it that I could find, and started learning the do's and the don'tTS, all the different techniques and what it can provide, what it is.
[306.84 → 320.42] And then I took that and started iterating over what was primordial RVM at the time, and I got an initial Ruby environment manager up and running.
[321.02 → 326.80] Back then I called it Ruby version manager, but that's not quite as an apt description as Ruby environment manager.
[326.80 → 341.30] So I started using it, and a week after I wrote it over the initial version over one evening, and then I iterated over it for a week.
[341.62 → 342.94] I had it working pretty decently.
[343.22 → 349.94] It would basically download, compile, install Ruby's, and keep them semi-isolated as a user install.
[350.88 → 353.28] And then I showed it to this guy named Peter Cooper.
[354.10 → 354.40] Who?
[354.40 → 356.82] Some guy named Peter Cooper.
[357.34 → 357.98] Friend of the show.
[358.98 → 360.70] Yeah, kind of goofy, you know.
[361.28 → 362.58] But anyway, I digress.
[363.02 → 373.74] So, yeah, he did a blog post about it, and then next thing I know I had like this IRC channel, and people were asking me left and right to add features to it.
[374.18 → 376.48] Actually, what they were really asking is, hey, can I do this?
[376.56 → 378.84] And I would be like, no, hold on a minute.
[378.98 → 381.98] And then I'd go, and five minutes later I'd be like, hey, get ahead and check this out.
[381.98 → 385.46] And then it just kind of snowballed and iterated.
[385.46 → 392.02] So was it the move to 1.9 that prompted it, or was it Ruby and RE and some of the other flavours?
[392.70 → 394.90] Actually, it was both 1.9 and Ruby.
[395.44 → 398.06] Basically, they had a massive legacy.
[398.46 → 403.84] Well, not exactly a legacy, but they had an application they had written, and it was using MRI 1.8.
[403.84 → 409.42] And they were embarking on a new application.
[409.86 → 422.56] That is, they were going to write it with Ruby 1.9, and a piece of it was supposed to be an ETL processor and needed to use JDBC to connect to SQL servers at the time.
[422.90 → 428.46] And that was a Ruby piece, and that's where that came in.
[428.46 → 433.40] So it was a new project that they were starting out, which is now turning into their main business project.
[434.08 → 438.56] And it used Ruby 1.9 and Ruby from the start.
[439.76 → 444.42] One of the big things that always lets me recommend RVM to people is that IRC channel.
[445.04 → 453.36] And from personal experience and just hearing from other people, you're perfect at being available and helping people out.
[453.36 → 459.68] So how do you manage to stay up for 20 hours a day and hang out on IRC and push new features out to RVM so fast?
[460.90 → 462.90] I'm not sure if I could answer that question if I tried.
[464.94 → 472.50] For the last couple of weeks, I've kind of been dealing with some family things and personal things, so I haven't been quite as available.
[473.02 → 478.46] However, overall, yeah, for the past two years, I've been overly available.
[478.46 → 483.98] Yeah, I don't think anybody can begrudge you for spending time with your family after this, like, you know, I don't know.
[485.02 → 497.24] Yeah, I think I basically burned myself out a bit, but much to my happiness, the community has started to step in and help out.
[497.38 → 499.92] And there's a lot of people on the IRC channel now that help out.
[499.92 → 510.50] And even more phenomenal to me is I now have a co-conspirator, Michael Pappies, who is out of Poland, has stepped in.
[510.70 → 519.08] And he basically took the ball and started running with it and let me take a mental sanity slash family break.
[519.28 → 527.10] And he's been helping support and drive RVM forward for the past two, three, four, three or four weeks now.
[527.10 → 541.48] And so now that I'm kind of getting back into it again, I can't iterate it enough that having someone helping on a project of this that everybody is using like this is just unbelievable.
[541.96 → 550.80] Before that, I had a few quick helps here and there, a few random pull requests and stuff like that.
[550.80 → 565.20] But nobody that could actually know the code base inside out since last year, Ruby Summer of Code, where I had dedicated Darcy Haycock for that entire stint of the Ruby Summer of Code.
[566.06 → 569.90] Since then, I haven't really had anybody that, you know, stepped up and helped out.
[570.32 → 574.34] And Michael now is stepping up and helping out with both RVM and BDSM.
[574.34 → 581.14] And it's just amazing how much more energetic I am able to get about it now.
[583.04 → 586.30] You know, one of the powerful features of RVM are gem sets.
[586.76 → 595.36] There's a post by Ryan McGarry, I guess is the name, talking about how as a community we're probably abusing gem sets for application development.
[595.64 → 598.66] And we should be using the vendor everything approach.
[598.72 → 601.64] What's your take on gem sets and when they're useful?
[601.64 → 607.06] Well, personally, I use gem sets on every project.
[607.42 → 608.72] I bundle, I vendor nothing.
[609.42 → 616.80] I tend to, I do firmly believe in complete and utter isolation of an application.
[618.30 → 622.36] What I do is I do use gem sets to do that.
[622.36 → 631.04] And basically, I obliterate, if I'm deploying to a server, you know, you can just start clean or obliterate a gem set.
[631.28 → 637.10] And, you know, if you're using Bundler or Isolate or something like that, you can, or RVM gem sets themselves.
[637.28 → 640.18] I have a gem set import feature, an export feature.
[640.18 → 647.36] And you can use any of those things to bootstrap exactly the gems you need for your application.
[647.36 → 650.92] And, yeah.
[651.14 → 671.62] The one exception I take to the vendor nothing is I do vendor things when I have to deploy to a system that's insanely locked down behind firewalls such that, you know, there is no actual good reason for them to be that locked down, however they do it anyway.
[671.62 → 678.22] So anytime I deal with people like that, I tend to actually bundle things, but I don't actually bundle them in the application.
[678.92 → 682.44] I like to keep my application's code bases lean and clean.
[682.88 → 690.18] So I have another way that I propagate bundled gem set directories and stuff like that.
[690.42 → 694.08] A big piece of the workflow is how Bundler works together with RVM.
[694.24 → 700.38] How much integration have you done with Yehuda and how he designed Bundler to get those two to play nice?
[700.38 → 714.82] Originally, there was a lot of back and forth with Yehuda and me, and we got a lot of the kinks worked out right around Bundler 1.0 and shortly thereafter 1.0 point, you know, a lot of iterations.
[715.74 → 718.62] And they started to play nice together.
[719.20 → 725.14] And then sometime recently, things started to diverge a little bit again.
[725.14 → 734.38] So what I've requested, well, actually, I talked with Indirect about, and apologies, I don't know, I don't remember his actual name.
[734.52 → 736.34] I deal with him mostly on IRC and Twitter, so.
[737.00 → 738.00] I do that all the time.
[738.48 → 738.70] So.
[738.90 → 739.10] Yeah.
[740.22 → 743.88] If Steve Flank's Twitter handle wasn't Steve Flank, I wouldn't know who he was.
[744.10 → 744.44] Yeah.
[746.44 → 748.72] People have trouble remembering my name as well.
[748.72 → 755.34] So, basically, we went back and forth for the brief discussion, and we figured out a way to do it.
[756.20 → 764.92] And actually, just yesterday or the day before, Yehuda popped in my channel and asked me about my references to that discussion.
[764.92 → 773.78] And what it is, is what we're going to do is I'm going to have RVM basically say, hey, I just entered a project directory.
[774.06 → 775.62] Is there a gem file?
[775.78 → 776.04] Yes.
[776.62 → 776.98] Okay.
[777.22 → 778.44] It looks like we're using Bundler's.
[778.72 → 785.66] So, basically, what it's going to do is Bundler's going to have its own special binary path, the bin directory, right?
[785.66 → 794.80] I'm going to add that to the beginning of path and the beginning of gem path, and that's where everything will be preloaded.
[794.90 → 804.88] Now, the only Bundler change that they need to make is to have Bundler respect loading from gem path instead of only respecting gem home like it does now.
[805.44 → 807.70] So, in other words, full Ruby Gems support.
[808.84 → 813.60] So, loading can come from anywhere in the gem path, whereas installing only goes to gem home.
[813.60 → 825.50] And also their special bin directory so that they can inject loading of Bundler into their binaries in this special bin directory, but not interfere with Ruby Gems proper.
[826.60 → 842.48] And what that will accomplish is people will be able to use Bundler and have it respect all of their environment and not have to type B, E, bundle, exec, anything like that in front of their commands, which is, frankly, it's an abomination.
[842.48 → 849.80] It goes against everything that RVM stands for with cleaning up and keeping a central unified API for everything.
[850.14 → 855.98] With RVM, you don't have to type Mac Ruby, Ruby, Iron Ruby.
[856.04 → 857.76] You don't have to type all these different binary names.
[857.90 → 862.82] You simply specify which one you want to use, and then you type Ruby, Gem, IRB.
[863.02 → 863.94] It's all the same.
[863.94 → 870.22] I had to go through flaming hoops to get it that way, but once it was that way, then everybody else benefits.
[870.36 → 873.68] They have this same workflow no matter which Ruby they're using.
[874.04 → 882.30] I want to come back to the unified thing in a second, but before that, there's sort of two ways that Bundler has these binary stubs and wrappers.
[882.30 → 891.14] So we're talking, in this case, this is about the bin stubs feature of Bundler, not the wrapped-up special Ruby bin stubs thing that RVM has.
[892.34 → 893.54] And what is that used for?
[893.60 → 895.42] I've never actually seen anybody use that feature.
[895.54 → 901.50] I noticed it was there one time when you can sort of generate a Ruby with its own special name, but I haven't actually seen anyone use that.
[901.62 → 904.28] So what was the impetus for that, and what's it good for?
[904.28 → 912.80] Well, that's something completely different from the idea of bin stubs with those, but you can actually name your rubies anything you want.
[912.88 → 931.88] You can alias them, which basically records into an alias file that the – when you alias a Ruby, it basically allows you to, like, say, alias, you know, 19 and then 192 or patch level 280 or whatever.
[931.88 → 945.20] And then you can say just from then on, anywhere you would put a Ruby string specifier in our VM's command line, you can literally just type 19 or something short and convenient for you.
[946.22 → 956.72] And then there's also a wrappers concept where you can generate a wrapper for a Ruby and a command.
[956.72 → 965.24] So using these wrappers feature, you could actually say – for example, Engine Yard, Heroku, they have their own gems.
[965.52 → 974.58] And it would be nice to be able to use those gems anywhere in your system without having to worry about switching to the gems that you installed them in to use and stuff like that, right?
[974.92 → 975.10] Yeah.
[975.10 → 986.88] Well, you can use the wrapper feature in order to wrap those CLI tools and peg them into – and what it does is it pegs the environment to whatever environment they were installed in.
[987.38 → 1001.12] So you can actually – then since you're using RVM, the RVM bin directory gets into your path, and you can now type Heroku EY – you know, Heroku deploy or whatever it is, EY deploy, all those things.
[1001.12 → 1008.74] And anywhere in your system, no matter what Ruby or gem set you're using, and it works as expected.
[1009.66 → 1010.74] Yeah, that's awesome.
[1011.28 → 1020.06] The unified approach thing definitely helps when getting people acquainted with – or just in general, not having to remember how to do things 12 different ways is really nice.
[1020.50 → 1026.28] But sometimes things – since you're sort of the gateway into Ruby, you have to know a lot about a lot of things.
[1026.28 → 1036.70] Like you said, you sort of went through a ton of effort to make this happen, and sometimes there's a little bit of back and forth, like what just happened over the last couple of days with the Nail gun situation that I talked to you about.
[1037.62 → 1048.08] So Michael, if everybody who isn't obsessively using Ruby and paying attention to RVMs, like had – Michael added a thing that starts Ruby with Nail gun.
[1048.08 → 1054.10] So when you do that, type Ruby to start Ruby, you get Nail gun, and Nail gun can change the way your application works.
[1054.64 → 1057.42] Usually it's faster, but sometimes it breaks and sometimes it's slower.
[1057.68 → 1062.86] So how do you keep on top of 12 different versions of Ruby and their patch levels?
[1063.00 → 1068.62] Do you sort of take a more of a pull approach and assume that people will just say, hey, Wayne, this is broken?
[1068.80 → 1071.54] Or do you actively pay attention to all these different projects?
[1071.64 → 1073.22] How does that sort of work out?
[1073.22 → 1079.82] So I do not actively pay attention to all the projects because when I change something in our VM, I will know within five minutes.
[1080.44 → 1081.64] No, I'm serious.
[1081.78 → 1085.48] I guarantee I will know within five minutes whether it broke anything.
[1086.26 → 1087.80] That's awesome and terrible.
[1088.80 → 1089.56] Well, it is.
[1089.68 → 1094.06] So basically anytime I make a change, I literally make sure I'm just waiting around for the next half an hour.
[1094.06 → 1101.08] And if anything broke for anybody, I can fix it right away because I know exactly what it was.
[1101.46 → 1106.56] And, yeah, it's so easy to change things that way because I get feedback.
[1106.72 → 1108.90] And that feedback is absolutely priceless.
[1109.34 → 1110.68] It's like having an army of QA.
[1111.08 → 1111.88] I checked it out.
[1111.88 → 1125.18] And the RVM website and the BDSM website, between the two of them, they're serving – just for the website documentation and everything like that, it's serving well over – I think it was like two million requests a month.
[1127.20 → 1127.78] That's amazing.
[1128.10 → 1131.10] And then you add into that all the downloads and stuff like that.
[1131.20 → 1132.20] It's like, wow.
[1133.62 → 1134.34] That's awesome.
[1134.34 → 1144.04] But, yeah, so what happens is I change – usually I don't really just – I don't any more change things just to change them.
[1145.92 → 1149.52] So I will change things to refactor to clean up the code base.
[1149.94 → 1159.20] However, as far as like adding new features, I really at this point only do that if there's a user who says, hey, does it do this?
[1159.26 → 1159.84] Can it do this?
[1159.84 → 1168.84] And if it sounds like a good suggestion, sounds like a useful feature, it has a use case, I will just add it and push it and then have them test it.
[1168.92 → 1169.46] They test it.
[1169.48 → 1170.12] It will be good or bad.
[1170.54 → 1171.90] And I'll fix it real quick.
[1172.02 → 1177.92] And then once they've got it and tested working, I'll just wait and see if anybody else screams or squeals.
[1177.92 → 1185.40] And if it all looks good, then I'll push a release out either that same day or the next day or whatever.
[1187.50 → 1188.50] Switch gears for a minute.
[1188.50 → 1189.92] Talk to us about BDSM.
[1190.90 → 1203.80] Yeah, BDSM is – originally it was the Bash deployment and server manager because that's actually what I built it for originally was to manage all of my various –
[1203.80 → 1208.10] I was managing like 82 or more servers for different people.
[1208.90 → 1212.66] And, you know, I wanted to do something that would keep them all the same.
[1212.66 → 1225.42] And they were among many different operating systems ranging in age from anywhere from like, oh, my God, why is this thing still chugging along to, Wooloo, it's Arch Linux, the latest and greatest.
[1226.20 → 1227.06] That kind of stuff.
[1227.06 → 1231.06] So, yeah.
[1231.12 → 1237.74] So, originally it was meant for setting up and deploying applications on servers and managing that.
[1237.74 → 1254.24] And then I started thinking and dealing with more – as a systems administrator, I had literally an accumulation of random scripts and things that just kind of started collecting on all the systems.
[1254.24 → 1256.28] And I would go, and I'd need one.
[1256.38 → 1256.94] I'd need a script.
[1257.06 → 1257.98] And I'd be like, oh, crap.
[1258.32 → 1260.00] Where is – which system – okay, okay.
[1260.28 → 1263.00] Oh, this friend of mine had it for his systems.
[1263.54 → 1265.34] And, okay, I'm going to go to one of his servers.
[1265.46 → 1265.62] All right.
[1265.96 → 1267.58] Now, where did I store that script?
[1269.14 → 1269.86] Let's do which.
[1270.00 → 1270.90] Oh, no, it's not there.
[1271.02 → 1271.26] Crap.
[1271.26 → 1272.08] I know it's on here.
[1272.54 → 1279.94] So, you know, trying to figure out where it is and not only that, but then you also have the issue of revision control and all this other stuff of these scripts, right?
[1281.04 → 1283.92] So, it became a little bit painful for that.
[1284.74 → 1293.54] And here I had this great little system, this BDSM, and I had this fledgling modules concept in it.
[1293.90 → 1296.92] And now this was like a year and a half or so ago.
[1296.92 → 1304.98] So, I started adding into it the concept of modules and loadable modules and extensions.
[1305.90 → 1310.12] And so, let me briefly give you a rundown of what those really are.
[1311.02 → 1320.20] So, it changed from this, you know, server setup and deployment script into a full-fledged system-level scripting framework.
[1320.20 → 1328.40] You can actually now put BDSM in the shebang line and start using its modules and extensions inside your scripts,
[1328.84 → 1334.98] which gives you nice things like stack traces that print out such that, based on your editor setting, you can, you know,
[1335.08 → 1342.00] as long as your terminal supports it, you can command-click on the line, and it brings you, opens up to that source line and file.
[1342.00 → 1353.24] And lots of other stack tracing and application tracing and debugging, like goodies, as well as a lot of DSL constructs.
[1353.32 → 1360.64] Like, instead of having to remember the bracket, you know, dash, S, you know, file name, and, and, this kind of stuff.
[1360.64 → 1367.10] You can, you can literally do if space file underscore exists and then the file name or the path to the file with the file name.
[1367.84 → 1374.32] If space file is executable, you know, there are all kinds of DSL methods that are provided by the modules,
[1374.44 → 1378.16] the core modules and the file system modules now by default.
[1378.80 → 1387.00] And using these, these modules, these, so the modules can, are contained basically namespace sets of functions for doing different things.
[1387.00 → 1395.90] Like, there's a file system, a system, a user, a blogging trace, all kinds of different modules.
[1396.80 → 1402.72] And so they're basically, like, equivalent to, in Ruby, the standard library.
[1403.54 → 1407.46] So that they're along the same idea as, like, the Ruby standard library, but for, like, shell scripting.
[1407.58 → 1410.08] Yeah, like, active support is sort of almost what it sounds like.
[1410.14 → 1412.70] Just like, these are all useful things that you might like to use.
[1413.46 → 1414.18] Something like that, yeah.
[1414.18 → 1416.62] Yeah, and it does two things.
[1416.72 → 1423.64] It extends the features of shell scripting so that you get very clean-looking shell scripts
[1423.64 → 1429.94] and also makes them, gives them all these enhanced features like, yeah, sure, the active support concept.
[1430.74 → 1433.08] And also there's a lot of extra error checking.
[1433.24 → 1440.98] So if you use the DSL functions, they, literally any and every error situation that I could think of when I'm writing those functions,
[1440.98 → 1442.22] I account for in them.
[1442.38 → 1450.94] And if there is an error scenario in them, I will, I have it spit out a backtrack as well as the exact message.
[1451.82 → 1456.94] So if it's clear that it's a coding error, like, you say, if file exists, then blah, blah, blah.
[1457.08 → 1458.78] Well, clearly you didn't specify the file.
[1458.90 → 1463.16] Well, it'll actually spit back out a stack trace showing you where, how it got to there.
[1463.16 → 1466.32] So you can see what line of your code was calling if file exists.
[1467.12 → 1473.44] And you can, it'll say, error, you didn't specify the file name to the function or something like that, right?
[1474.02 → 1478.52] So it gives you a lot of sanity checks and helpful stuff when you're scripting in shell.
[1478.52 → 1488.42] So now, using that as a basis, the BDSM extensions are basically a whole other level of nicety.
[1489.02 → 1495.52] Extensions are to be thought of as namespace sets of actions.
[1496.24 → 1499.28] And actions are basically either shell functions or scripts.
[1499.28 → 1516.18] So if you have, like, scripts to manage your, let's say, Regis, for example, you know, you probably have a script to install Regis on a server, a script to start it, stop it, maybe check the status of it, that kind of stuff.
[1517.86 → 1521.88] So what you would do is you would actually write a Regis extension.
[1521.88 → 1526.36] And in the Regis extension, basically, you have an actions' directory.
[1526.54 → 1530.62] And inside that actions directory, you can have as many subdirectory, nested subdirectory as you want.
[1531.08 → 1546.96] And in each one of them, you can either put executable script files or a.actions file, which lists a, you know, how a command line action like, say, BDSM Regis package installation.
[1546.96 → 1559.62] So I'll have a Regis, the Regis extension will be a directory, Regis slash actions slash package slash, say, I do the executable script way, it'll be the script there called installation.
[1560.16 → 1569.76] And then BDSM, once the extension is installed, it will just, as long as it's executable in that directory, it will just call that script file, the installation.
[1570.18 → 1574.80] And that install script can be any language as long as it's an executable script file.
[1574.80 → 1581.00] So you can write it in compiled C, you can write it in Python, Perl, Ruby, Shell.
[1581.42 → 1589.56] Now, BDSM, if you do write your stuff in Shell, then you have the edit bonus of all the standard modules that BDSM provides.
[1590.24 → 1591.88] However, you're not restricted to do that.
[1591.88 → 1603.08] And so then what it does is BDSM encapsulate, you encapsulate your sets of scripts, your namespace sets of scripts in extensions.
[1603.42 → 1610.46] So you can have one for, like, say, Regis, you can have one for deploying, which these are actually examples that I have.
[1610.46 → 1613.86] One for, say, Unicorn to control it.
[1614.08 → 1622.68] And then you install BDSM, you just say BDSM, and then the extension name package installation for, like, Regis.
[1622.86 → 1625.68] Like, so BDSM Regis package installation installs Regis.
[1626.08 → 1632.26] BDSM Regis service start, stop, restart, that kind of stuff does start, stop, restart on Regis.
[1632.26 → 1637.70] And those are implemented as system-level shell scripts or Ruby scripts or whatever you want.
[1638.82 → 1647.56] And one of the things, if you go to RVM's website, you have slash deployment slash best dash practices.
[1648.54 → 1652.20] And I need to update that with a new API.
[1652.46 → 1659.56] But essentially that details how you would go about deploying, say, Redline as an example application.
[1659.56 → 1669.32] And the idea is that you can use BDSM to bootstrap your application stack and control everything application-related on the system.
[1669.90 → 1673.38] And then separate from, like, Package Manager and everything like that.
[1673.78 → 1682.40] So what this affords me is, if you recall, with RVM, we have this isolated system where we can specify the environment,
[1682.90 → 1686.74] which is like the Ruby and the gem set and the list of gems and that kind of stuff.
[1686.74 → 1691.18] And so for your application, that becomes the application's environment.
[1691.46 → 1696.38] Well, this is taking that one step further to the entire application's environment and system.
[1696.80 → 1706.54] So given any Linux-type operating system or BSD, including OSX, you can install BDSM as root
[1706.54 → 1718.80] and then start managing your application stacks with BDSM as well as all of your writing extensions for your sets of scripts and stuff like that.
[1719.34 → 1721.42] So there's just so many things that you can do with it.
[1721.46 → 1722.00] It's ridiculous.
[1723.04 → 1728.92] So this is sort of part chef, part homebrew, part OMIT shell for Bash?
[1728.92 → 1729.32] Bash?
[1729.50 → 1729.94] Yeah.
[1730.62 → 1733.00] So it's not just Bash, though.
[1733.06 → 1735.58] It's more of a system-level framework.
[1736.48 → 1738.94] It happens to be written in Bash at the moment.
[1740.14 → 1746.00] So the fundamental idea that you can think of is, and the reason why I made it the way I did is,
[1746.52 → 1749.92] so I was trying to extend the RVM concept to my entire application stack.
[1749.92 → 1753.32] Since I had so many different servers that I was helping people manage,
[1754.12 → 1759.80] then they were on all kinds of different operating systems while trying to account for differences in package managers
[1759.80 → 1765.58] and package versions and names on them and everything just became a living hellish nightmare for me.
[1766.22 → 1772.80] So instead of doing that, what I do is we have some base libraries that, you know, we have the system,
[1773.28 → 1777.32] we have the system and the systems package manager install and manage the system itself.
[1777.32 → 1787.72] And then each application between BDSM and RVM, we manage the entire application stack specifically using those two tools.
[1788.44 → 1791.54] And it's cross-system the same.
[1791.74 → 1796.32] It's also completely isolated inside itself, just like RVM is.
[1796.54 → 1797.60] Where are you installing these to?
[1797.74 → 1798.82] What sort of paths?
[1799.34 → 1804.36] So for BDSM, you can do user or root installations.
[1804.36 → 1808.16] I only have one person doing user installs, so it's not heavily tested.
[1809.30 → 1814.98] It's an enterprise-type shop where they have the full barrier between sysadmins and developers,
[1815.10 → 1817.76] and developers only can get in as users and stuff like that.
[1817.98 → 1819.90] So, you know, they are doing that.
[1819.94 → 1820.78] So it does work that way.
[1821.00 → 1827.14] But the way I have it done on all the systems is it's installed as root, BDSM is,
[1827.14 → 1834.02] and then every application gets its own system user and its own RVM install.
[1834.16 → 1837.34] The only user thing tripped me up the first time I ever used BDSM.
[1837.46 → 1841.96] Now, I have a server that I've been deploying two applications to with it, and it's been awesome.
[1842.20 → 1848.20] But one of them is called Deployed as far as BDSM goes because I didn't realize that that was the way that it worked.
[1848.20 → 1851.50] And I really like the way that it works, but just hilarious.
[1851.90 → 1855.40] I've been meaning to move it over to a real name, and I haven't gotten around to it yet
[1855.40 → 1858.88] because it confuses me every time I try to configure that particular application.
[1861.36 → 1862.28] It works well.
[1862.32 → 1862.72] It's awesome.
[1863.56 → 1867.52] It's so much simpler than Cristiano was to manage everything.
[1867.62 → 1872.66] One of them is a Sinatra app, and one's a Rails app, and one's using MongoDB, and one's using Postgres.
[1872.92 → 1875.38] And so all that kind of stuff is way easier to manage so far.
[1875.38 → 1878.50] So it's been a reading of best practices page.
[1878.66 → 1879.90] That's exactly the plan.
[1880.66 → 1888.46] So for application developers, like web application developers or people like that,
[1888.76 → 1893.48] the idea is that you need to manage your application stack specifically.
[1894.14 → 1897.02] And you want to be able, in my opinion, and at least the way I do things,
[1897.08 → 1903.42] is I want to be able to go on my laptop, on my desktop, on my CI server, my staging server, my production server,
[1903.42 → 1904.68] all of these, right, the QA.
[1904.68 → 1906.72] And I want to have them identical.
[1906.98 → 1917.16] I don't really give a woo-hoo whether it's on OSX or this one's on CentOS or this one's on Arch Linux or this one's on Redshift.
[1917.30 → 1920.76] I mean, basically, I really don't want to care.
[1921.00 → 1922.36] I really don't want to care.
[1922.46 → 1923.90] I want it to work the same on all of them.
[1923.90 → 1928.60] And also, if it's set up and run and works the same on all of them,
[1928.74 → 1941.30] that also enables me to kind of test exactly that application stack as I go from development to QA to CI and staging, right,
[1941.56 → 1942.48] all the way to production.
[1942.48 → 1947.70] If it's identical, the entire application stack the whole way, then, you know,
[1947.76 → 1951.92] you're more confident that it's going to work the same as you bring it on.
[1952.64 → 1957.48] You run into any problems supporting cross-platform scripts like this?
[1957.48 → 1958.04] Okay.
[1958.92 → 1963.20] So, basically, supporting cross-platform scripts is a living nightmare.
[1964.20 → 1973.26] But the nice thing is if you use the BDSM underlying core DSL functions to write everything,
[1973.26 → 1981.92] then those I've been ensuring when I write them that they're cross-platform as far as cross, like, you know,
[1982.04 → 1982.96] star and X distributions.
[1984.32 → 1988.56] And so as long as you're using them when you're scripting,
[1988.56 → 1994.76] then you automatically have these extensions and scripts that work correctly,
[1994.98 → 2001.26] no matter whether you're deploying to Fedora or, you know, CentOS or Debian or any of those things.
[2003.26 → 2004.98] I'm not sure if I answered the question.
[2005.34 → 2006.32] Oh, absolutely, yeah.
[2006.44 → 2008.12] It just seems like a tall order.
[2008.24 → 2010.28] You know, Homebrew is OS X only, right?
[2010.42 → 2010.70] Yes.
[2011.38 → 2016.52] So, you know, stretching across any star and X platform just seems infinitely more hard.
[2016.68 → 2017.16] Oh, it is.
[2017.50 → 2020.16] And I'm just tackling it one piece at a time.
[2020.64 → 2030.36] As I find and need new – so there's two big – so there's, like, core modules.
[2030.36 → 2034.44] There's, like, base level modules, like file system and user and, you know,
[2034.56 → 2037.14] they're basically dealing with one single small concept.
[2037.46 → 2040.72] But then there's also complex or compound modules.
[2041.40 → 2046.66] And two examples of that are package and service.
[2046.66 → 2053.04] So the package module encapsulates the idea of packaging, right?
[2053.90 → 2060.58] And the service module encapsulates the idea of services, things you run on a system,
[2060.74 → 2064.26] start, stop, restart, you know, status, that kind of stuff.
[2064.26 → 2074.48] And as I need new things for applications, like, okay, I need Regis, I need Elasticsearch,
[2074.58 → 2076.42] I need Postgres, whatever.
[2077.26 → 2081.48] You know, I'll sit down, and I'll write an extension, and I'll make it – test it out,
[2081.56 → 2087.66] make it sure that the extension is using the core modules and package module and service module
[2087.66 → 2093.62] so that I get all the maximum benefits of a generalized framework for package managing,
[2094.20 → 2095.78] for service managing.
[2096.80 → 2100.58] And in doing that, you've got a common command line interface for all these different services, right?
[2100.96 → 2102.42] Actually, that is exactly correct.
[2102.66 → 2108.30] That's another thing that I'm not stressing enough is also it's a common command line interface to it.
[2108.30 → 2116.02] So, yes, so if you're using the service module, all your commands can be managed based on, like,
[2116.48 → 2121.02] BDSM, your extension name, service, start, stop, restart, status, et cetera.
[2121.54 → 2125.80] Similarly for package, install, uninstall, update, whatever.
[2126.48 → 2134.62] And what's nice about this is it's a common command line interface to – and you can make scripts that do this.
[2134.62 → 2141.42] So what's even neater is BDSM is a single systems scripting framework, really.
[2141.58 → 2142.56] That's its focus.
[2143.10 → 2150.28] I'm not trying to conquer anything broader than a single system scope with this framework.
[2150.56 → 2154.82] So the idea, however, is with this framework and its extensions,
[2155.06 → 2160.92] you are able to provide a very succinct common command line interface to your extensions
[2160.92 → 2164.10] to be able to control and update and install your entire system.
[2164.62 → 2171.90] And then you can now use distributed tools such as Puppet, Chef, whatever you're going to use,
[2172.62 → 2178.28] SSH in parallel from a shell script, to call out to all your servers and services
[2178.28 → 2182.76] and do all the logic of managing what should be done on each one of them.
[2183.24 → 2187.68] And they will say, okay, BDSM, blah, blah, blah, BDSM, blah, blah, blah, BDSM, blah, blah, blah.
[2187.68 → 2196.80] And the idea is that you're isolating so that BDSM worries and manages specific aspects of the single systems.
[2197.12 → 2204.54] And then your Chef or Puppet, whatever you're using, will manage your overall infrastructure and coordinate it by –
[2204.54 → 2210.74] and then also all of your recipes and stuff like that for Chef become much simpler
[2210.74 → 2214.26] because you're literally calling out to the BDSM command line interface.
[2214.82 → 2225.64] That's one issue I've always had with Chef and Puppet is trying to manage system level things in Ruby and in these scripts
[2225.64 → 2230.68] has been, for me, a nightmare as it's just so unnatural.
[2231.20 → 2232.36] It just doesn't make sense to me.
[2232.78 → 2238.32] Whereas in shell scripting, what you're doing is you're just stringing together commands
[2238.32 → 2241.54] with a little bit of logic around them
[2241.54 → 2246.68] and piping their inputs and outputs together to manage your system.
[2246.68 → 2254.42] And every single binary on your system is a command available natively inside your shell script.
[2255.14 → 2260.30] It just makes a lot more sense to be doing system level management inside shell scripts.
[2260.84 → 2264.62] Now, another thing that I'm trying to do with BDSM is through these DSLs and everything.
[2264.72 → 2269.76] I'm trying to clean up shell scripting, show that it can be very clean, readable, and debuggable.
[2269.76 → 2275.94] Whereas if you look, just go SSH into your favourite Linux distro and look through the ETC directory
[2275.94 → 2278.92] of the shell scripts in there, and basically it'll make you want to claw your eyes out.
[2281.22 → 2283.22] Do you provide man support for these?
[2284.08 → 2284.60] For which?
[2285.24 → 2286.66] For any of your scripts.
[2286.78 → 2289.54] Do you have like a default documentation man files or anything?
[2289.54 → 2292.26] There's a BDSM help feature for now.
[2292.26 → 2302.46] However, we have currently planned providing hooks into man pages for BDSM extensions and everything itself right now.
[2303.36 → 2304.16] Very cool.
[2304.24 → 2306.74] You know, you're talking about being able to stitch these together.
[2306.90 → 2313.16] When I got into web development, it was back in the day, ESP Classic on the Windows platform.
[2313.46 → 2317.90] I couldn't do anything that didn't involve a right-click property pane somewhere.
[2317.90 → 2323.64] And having gotten into Ruby and Rails and the command line interface, I just could never go back to something
[2323.64 → 2326.70] that I couldn't just stitch together something that I wanted to do in a script, you know?
[2326.94 → 2327.84] Yes, I do know.
[2328.48 → 2329.36] That's exactly it.
[2329.42 → 2334.10] It's insanely powerful and flexible and nerd on.
[2335.46 → 2336.42] So, yeah.
[2337.64 → 2338.18] Go ahead.
[2338.58 → 2344.30] I was just going to say, so there's actually sort of two related things about setting all this up.
[2344.30 → 2349.68] So, obviously, if you want to have one system control your entire application stack and all these things,
[2350.28 → 2353.46] installing BDSM, I mean, I did it, so I sort of know.
[2353.58 → 2356.52] But if you're going to talk about how relatively easy it is to actually get started
[2356.52 → 2362.06] and how much work do you actually have to do to get a new blank, you know, I spin up a new VPS.
[2362.26 → 2364.46] How long is it until I'm deploying my code?
[2365.24 → 2370.84] And then a sort of little follow-up question about the whole get piped sh install method
[2370.84 → 2372.46] that people have been complaining about a little bit.
[2372.46 → 2380.04] So, I guess, yeah, so first thing, how quickly is it to get a new VPS actually set up with all this stuff to get going?
[2380.60 → 2384.20] Depends on the size and the computation power of the VPS.
[2385.16 → 2389.96] I have been focusing on to compile and install for the specific system.
[2390.10 → 2393.24] This allows me to hit a broader range of systems out of the gate
[2393.24 → 2398.20] without having to worry about whether what I built would be compatible.
[2398.58 → 2406.06] And if the dependent libraries or the dependency libraries like, you know, NGINX,
[2406.14 → 2409.48] okay, well, that requires PURE and Lib and OpenSSL.
[2409.48 → 2415.82] Oh, I'm using this extra patch to it, so I need this other library on my system.
[2417.12 → 2430.84] So, all the extensions that I've written so far take on a compiling by default approach.
[2430.84 → 2436.04] Now, you can write extensions that don't do that, and there actually is one extension that doesn't do that.
[2436.10 → 2438.50] For example, I think it's MongoDB, if I remember correctly.
[2439.92 → 2446.34] It's basically downloaded the executable for your platform, extract, and copy the files in the proper locations, and you're done.
[2447.82 → 2450.30] So, you know, it's possible to do anything you want with that.
[2450.30 → 2456.52] Now, that said, on an RVM test server that I have, it's not a particularly beefy server,
[2456.64 → 2461.66] but it's got, you know, like two gigs of RAM, and I don't know how much processing power.
[2461.82 → 2467.40] But within, I don't know, 10 or 15 minutes, I have a Redline instance deployed.
[2467.76 → 2472.26] And most of that time is literally just waiting for the compiling on it.
[2472.26 → 2481.90] So, if you use Gen too, you'll be right at home, as an Arch person, not to crack jokes at Gen too all the time.
[2482.78 → 2485.34] I'm actually a fan of both Arch and Gen too, so I don't know.
[2485.34 → 2485.82] It's so similar.
[2486.08 → 2489.10] It's like Ruby Python, is what it reminds me of.
[2489.16 → 2493.10] They're, like, almost identical, and there's no reason the two should hate each other, but they seem like they do.
[2493.10 → 2495.12] It's even more fundamental than that.
[2495.26 → 2499.54] It's like Ruinous and J. Ruby.
[2500.74 → 2500.88] Yeah.
[2500.88 → 2505.32] So, to the second piece, I guess, of that poorly worded question from earlier.
[2505.78 → 2512.92] So, RVM definitely has the ability to install through, like, curl this shell script and pipe it to SH.
[2513.80 → 2514.98] POW does this.
[2515.16 → 2516.24] NPM does this.
[2516.36 → 2521.96] And I see complaints on the Twitters all the time about how this is a terrible idea for installing software.
[2521.96 → 2523.08] Yeah, let me put it to you this way.
[2524.48 → 2525.50] It's a shell script.
[2527.20 → 2527.58] Shell.
[2527.58 → 2540.98] Your shells are capable of reading streams of files, whether it be from curling, whether it be from catting, whether it be from reading a file, and executing those files in there.
[2540.98 → 2548.74] So, this is literally quite equivalent to downloading the file, making it executable, and doing.slash install.
[2549.94 → 2550.96] There is no difference.
[2550.96 → 2558.64] Now, there was a possibility for a man in the middle attack, which is why I bought the SSL cert for RVM, thanks to the donations.
[2558.64 → 2569.02] And so, then I set up the SSL and then had lots of lovely little nightmares with CA certificates not being updated on people's systems.
[2569.56 → 2569.86] Whee!
[2570.86 → 2571.22] Hold on.
[2571.22 → 2571.38] Yeah.
[2571.80 → 2572.60] Tapping my thing.
[2572.82 → 2573.10] Hold on.
[2573.74 → 2574.78] So, yeah.
[2574.78 → 2578.24] So, that preempts the man in the middle thing.
[2578.82 → 2583.96] But if they're still going to complain, then they're just quite literally being pompous jackasses.
[2584.60 → 2592.06] And the reason for that is you shouldn't be running anything on your system that you don't trust for any number of reasons.
[2592.62 → 2599.36] And so, if you have a problem with that, download the script, read the code, see exactly what it does.
[2599.48 → 2600.24] Oh, my God.
[2600.30 → 2601.14] What a concept.
[2601.52 → 2601.72] Whoa!
[2602.18 → 2603.92] You just blew my mind!
[2603.92 → 2605.08] And...
[2605.08 → 2605.62] Uh-huh.
[2605.74 → 2606.26] Uh-huh.
[2606.52 → 2607.36] So, anyway.
[2608.56 → 2610.12] I don't know what else to say about that.
[2610.20 → 2610.86] It's like, why?
[2611.08 → 2611.96] You know, go ahead.
[2612.06 → 2612.46] Complain.
[2612.66 → 2612.88] You know?
[2613.04 → 2615.70] It's like you're just showing how much of an ass you are, really.
[2617.48 → 2620.78] So, Wayne, how long does it take you to bootstrap your own personal setup?
[2620.88 → 2623.36] So, Lion comes out, you want to install from scratch.
[2623.64 → 2625.48] How much of your own setup do you have automated?
[2628.80 → 2631.12] I'm a very bad monkey as far as that's concerned.
[2631.12 → 2634.40] I sync over my project directory.
[2634.40 → 2643.56] And then I basically just do the curl and cat and pipe and smoke it.
[2643.56 → 2646.26] Um, RBM and BDSM installs.
[2646.58 → 2649.30] And then I just take it from there.
[2649.30 → 2654.06] I basically will install, you know, the rubies as I can.
[2654.38 → 2661.48] I'll literally open up, like, ten shells and ten different terminals and install, you know, as many as I can in parallel.
[2661.62 → 2665.90] Usually I have to install, like, one eight or something first and then do all the rest.
[2665.90 → 2671.20] And for BDSM, I have that down to a little bit more of a science.
[2671.38 → 2674.66] I could actually, at this point in time, I could script the whole thing.
[2674.84 → 2679.90] Just open up a file, make it shebang line, you know, user local bin BDSM.
[2679.90 → 2684.48] BDSM, and then just start calling, you know, commands in there.
[2684.68 → 2692.24] And or just have a normal shell script where you do BDSM NGINX package install, BDSM Regis package installation.
[2692.46 → 2696.52] Or there's actually a new thing that I just introduced, which is an alternative syntax to that.
[2696.52 → 2701.88] And in literally one command, you can have it install all of your package things.
[2702.60 → 2704.62] It's kind of fun to use, too.
[2705.32 → 2724.20] But basically, what it, there's a you can do, like, you know, for example, BDSM Lib, comma, PURE, comma, OpenSSL, dot NGINX, comma, Regis, space, package installation.
[2724.20 → 2742.12] And what that will actually do is that will, in parallel, at the same time, install, what did I say, Lib, PURE, and OpenSSL.
[2742.70 → 2750.62] And then as soon as all three of those finish, then it will launch an installation of NGINX and Regis in parallel.
[2751.18 → 2751.50] Ah.
[2751.50 → 2751.68] Ah.
[2752.76 → 2761.74] And the reason for doing that, well, hopefully it's obvious, is because before you can build NGINX, you need those dependency libraries to be built.
[2762.06 → 2769.98] So I've got this compact command line syntax that I introduced today that allows you to quickly, in one line, install a dependency tree.
[2769.98 → 2773.76] And it also respects the number of CPUs on your system.
[2774.12 → 2787.94] So if you have two CPUs, it will only, so in my example, let's say you have two cores or two CPUs, using my example of PURE, Lib, and OpenSSL as the first set in sequence,
[2787.94 → 2798.06] it will install Lib and PURE, and it won't continue to OpenSSL until one of the two of this finish.
[2799.18 → 2799.88] That's awesome.
[2799.88 → 2807.88] And then once all three in the set of parallels finish, then it will install a, you know, NGINX and OpenSSL.
[2808.66 → 2817.32] And so, like, on my, on the RVM's test, this main test workbench that Engineer donated, it's a 24-core Mac Pro.
[2817.32 → 2827.44] And so on that one, I can make a massive string and watch everything light up, and it's, it's, grab some popcorn, and it's awesome.
[2828.10 → 2833.36] I mean, it seriously gives me the biggest nerd on ever, which keeps me, you know, building more and more packages so I can see it.
[2833.80 → 2834.20] Anyway.
[2834.88 → 2836.56] Another RVM question for you.
[2837.10 → 2844.00] So, any way to have it automatically create a gem set that it hasn't seen before when I click on it?
[2844.00 → 2854.94] In the documentation, if you actually read it, or in the example slash RVMRC, there is an RVM gem set create on use, or something like that.
[2855.04 → 2856.02] There's actually a flag for it.
[2856.02 → 2857.44] Dash create is the flag.
[2857.86 → 2861.06] Okay, so from the command line, you can say dash create, and it will create it.
[2861.50 → 2861.64] Right.
[2861.64 → 2866.68] Or you can make it so that any time it sees a gem set, it doesn't exist yet, it will automatically create it.
[2866.78 → 2872.92] That you can put in your.RVMRC file in your user home directory or your etcRVMRC file.
[2872.92 → 2884.96] And you're going to have to look in the documentation or in example slash RVMRC, but it's something like RVM gem set create flag or something like that.
[2885.26 → 2885.58] Awesome.
[2885.86 → 2892.76] That's pretty much the first thing I do on every project is make an RVMRC with a gem set as the name of the project and shove it in Git.
[2892.90 → 2894.34] I actually do that as well.
[2894.34 → 2910.00] When I create a new project, the first thing I do is I make the directory go to it and I do RVM space, you know, dash RVMRC dash space dash create space, I don't know, 1.9.2 at my project name.
[2910.62 → 2912.76] And that will generate the.RV MRC.
[2912.94 → 2915.70] I do get unit, get to add.RVMRC, and then I continue.
[2915.70 → 2924.72] So while we have you here, I know this is in the RVM best practices website, but let's get it straight from the horse's mouth.
[2926.06 → 2933.14] RVMRCs, always check them into your repositories and have a project gem set with the same name as your project, right?
[2933.48 → 2935.34] Yeah, completely correct.
[2935.34 → 2944.16] If you're, if you, the RVMRC is the bond, is the specification of this is the project's environment.
[2944.40 → 2950.18] When you're in this project, when you're running this project, it should be in this environment by default.
[2950.70 → 2959.28] So that when you go into the project, whether it's five months down the road, whether, whatever, whether you, you know, you're all crap, I lost my system.
[2959.28 → 2961.06] I just clone the repo CD into it.
[2961.14 → 2964.82] RVM sets up your environment and everything's kosher, and you get going.
[2965.34 → 2970.42] And additionally, keep in mind, the RVMRC file is actually a shell script.
[2971.08 → 2979.12] So it's not just setting the RVMRC string and environment ID, which is the ruby string at gem set name.
[2979.60 → 2980.56] It's more than that.
[2981.00 → 2985.14] You should do in the RVMRC with proper error handling.
[2985.64 → 2992.50] Anything that you need to do to set up this application's environment to be ready to work on it or run it.
[2992.50 → 2999.44] You know, when I see anybody complaining about RVM or Bundler on Twitter, I just want to remind them where we've come since 2005.
[3000.28 → 3006.36] Go on to the days when it was just like a picture puzzle game of dependencies trying to get a Rails project to run back then.
[3006.90 → 3007.20] Yeah.
[3007.20 → 3009.16] Thanks for that.
[3010.60 → 3011.60] Thanks for those memories.
[3012.16 → 3019.40] So basically, with that, yeah, so it's basically a contract between all developers on that application.
[3020.04 → 3025.10] And since it's a shell script, you can actually put checks in there that will do things like check the git branch.
[3025.10 → 3031.14] And based on the git branch, so if I'm on production, then we're using this ruby.
[3031.32 → 3040.56] But for the master branch or development branch, then you would use this environment identifier instead because we're to bat it.
[3040.60 → 3041.52] So we were on 1.8.
[3041.70 → 3042.48] That's production.
[3043.06 → 3052.40] But if the git branch is development or master, then we want to be on 1.9 because we're working on upgrading on the master branch or something like that.
[3052.82 → 3054.20] That is the proper way.
[3054.20 → 3054.48] Awesome.
[3054.96 → 3058.76] Or if you've got a special ruby for Heroku, you know, that's different from your local too.
[3058.96 → 3059.26] That's cool.
[3059.32 → 3061.60] Yes, that is the proper way to be using your RVMRCs.
[3061.94 → 3073.44] And if you're a Bundler user, then if you look in the generated RVMRC file towards the bottom, what you will notice is that it has examples of what I –
[3073.44 → 3074.72] Okay, so let me back up.
[3075.30 → 3076.26] It has examples on there.
[3076.26 → 3084.74] What I actually do is if I'm using Bundler on a project, I will have the top of the – the very top selects the environment ID.
[3085.38 → 3088.24] The middle is what – this is already in there generated.
[3088.24 → 3090.90] The middle loads that environment.
[3091.58 → 3096.00] And then down below, I use a .gems file with RVM gem sets.
[3096.44 → 3100.40] And what I do is RVM gem set – it will – RVM gem set import .gems.
[3100.68 → 3103.60] In that file, I have just one word, Bundler.
[3103.72 → 3107.28] Or you could do Bundler space dash V 1.0.15, whatever.
[3107.28 → 3116.38] And what that does is when I CD into the directory, not only does it load the RVM environment, it makes sure that Bundler is – and the proper version is installed in that gem set.
[3117.14 → 3130.82] Taking that further, a little bit down more in the generated file, you can actually see that it has a – you know if Bundler is found, then call bundle when you CD in there so that it also bundles for you.
[3130.82 → 3131.98] But now that's optional.
[3132.48 → 3137.72] But so, yeah, so that's RVMRC files and proper usage of them.
[3138.32 → 3138.62] Cool.
[3138.72 → 3140.18] We know you had a hard stop at five.
[3140.22 → 3141.72] So one last question before we let you go.
[3141.72 → 3149.44] So when you're not hacking on RVM or BDSM, what open source project out there are you excited that you want to tell the world about?
[3150.16 → 3152.54] And by world, I mean like our 200 users or listeners.
[3153.34 → 3154.56] 200 listeners.
[3154.56 → 3168.60] So basically, I'm actually currently working on a specification for a new open source project which does not have a name yet.
[3168.84 → 3170.56] I am working on this with Michael.
[3170.56 → 3187.96] And the idea is that it is the system which allows you to write plug-ins for it for processing arbitrary data streams or – which have the idea of like identities and relationships.
[3188.84 → 3191.34] And like so in other words, identities and interactions between identities.
[3192.04 → 3194.90] And it's a generic framework for this kind of thing.
[3194.90 → 3209.50] So applications for it could be like monitoring systems could have a plug-in which basically maps this data and calculates and computes relationships on aggregated monitoring things that come into it.
[3209.92 → 3215.90] Or you could actually do neat things like business metrics.
[3215.90 → 3226.98] Metrics like if you can pull in metrics from your ticketing system, pull in metrics from your sales department, pull in metrics from your Nagios as well at the same time.
[3227.12 → 3230.54] Pull in any and all kinds of different metrics.
[3230.96 → 3236.00] And basically, you write plug-ins which know how to parse these metrics into the format required by the system.
[3236.00 → 3252.34] And then what happens is when it's in the system, the system itself has a bunch of default – it has a graph database inside of it as well as a document data store as well as a relational data store.
[3252.68 → 3257.44] All three of which work together so that basically the entry into the system is the document data store.
[3257.56 → 3260.34] And that's where all the raw information is stored.
[3260.34 → 3273.70] And then the plug-ins are expected to have processors written in them which extract that and store the – load the – extract data into the IDR, the relationship, the graph database.
[3274.06 → 3281.64] And then inside the graph database, your processor will look at that and extract statistics.
[3281.88 → 3289.54] The system will actually extract statistics based on what it sees in the giant graph relationship database and store them into the tables.
[3289.54 → 3302.42] And then what you can do is you can actually use these things for alerting, for reporting, like business reporting and reflecting on your business and determining directions and stuff like that.
[3302.48 → 3305.64] So that's one kind of thing I'm looking at and thinking about.
[3306.18 → 3310.72] And as well, there's something called event stream processing and workflow engines.
[3310.72 → 3318.76] And combining the two of those together and putting them on top of this system as well will end up with this extremely flexible system.
[3318.76 → 3325.86] It's going to be generic, and the plug-ins are what actually are business-specific or application-specific.
[3326.56 → 3331.42] And the applications of this are – I've just seen this need in so many different areas.
[3333.58 → 3336.02] Could you do social network activity streams, for instance?
[3336.54 → 3338.10] That is exactly correct, yes.
[3338.24 → 3344.48] You could do – let's say you want to have a BDSM relationship dating site and you –
[3344.48 → 3345.56] I don't know.
[3345.58 → 3346.10] Theoretically.
[3346.10 → 3346.64] Theoretically.
[3347.22 → 3352.26] The canonical example is like if everybody uses Twitter as a canonical example.
[3352.54 → 3361.12] The idea is that you would write a Twitter processor which is able to import Twitter relationships.
[3361.74 → 3371.12] So you have these Twitter IDs, and then you have different kind of interaction types between these IDs like follow or retweet or mention, that kind of stuff.
[3371.12 → 3373.58] And then put that in the system and then it will compute.
[3373.80 → 3393.40] Based on the data types that are labelled on the – in the graph database, there are processors which will extract statistical information and store those into relational database as statistics storage, which can be used for reporting and extracting and whatever the heck you want to do, really.
[3393.40 → 3394.40] Very interesting.
[3394.40 → 3394.42] Very interesting.
[3394.50 → 3395.94] Yeah, I've seen that pattern a lot.
[3396.02 → 3402.62] It seems to be kind of the pattern behind a lot of web applications and even business applications like you mentioned now.
[3402.96 → 3403.08] Yep.
[3403.38 → 3407.80] Well, Wayne, surely appreciate it, taking the time to tell us about RVM and BDSM.
[3408.40 → 3411.78] And look forward to this yet unnamed project.
[3412.34 → 3412.58] Cool.
[3412.68 → 3413.44] Yeah, thanks a lot, Wayne.
[3413.46 → 3413.74] Cool.
[3414.82 → 3415.70] All right, guys.
[3415.70 → 3422.96] recipients Hay, being wait, a little bit on my screen.
[3423.36 → 3423.68] Thanks.
[3430.68 → 3433.36] Thanks a lot.
[3443.82 → 3444.96] Thanks a lot.
[3444.96 → 3474.94] Thank you.
