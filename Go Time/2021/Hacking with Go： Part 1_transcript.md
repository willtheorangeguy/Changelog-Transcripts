[0.00 --> 9.46]  The stakes have been ratcheting up. We don't want to make it like too dark or too heady, but now this is the playground of also a lot of nation states and a lot of criminals.
[9.72 --> 14.58]  And, you know, if you're in the US, it's kind of like the ransomware epidemic is sort of unavoidable, right?
[14.60 --> 18.70]  Like you have to talk about it every day. And that's where things get less pretty, right?
[18.74 --> 27.42]  Like if you're at a hospital that can't help folks because all their tragically outdated Windows XP systems are in a flat network and all of them got popped at the same time.
[27.42 --> 36.86]  That's where you go. Well, yeah, that code was fun. I love the idea of just having these, you know, kind of hacking superpowers, but there's a side to it that isn't quite so cute.
[37.16 --> 39.48]  And I think we're kind of walking that line all the time.
[41.82 --> 48.02]  Big thanks to our partners, Linode, Fastly and LaunchDarkly. We love Linode. They keep it fast and simple.
[48.32 --> 55.62]  Get $100 in credit at linode.com slash changelog. Our bandwidth is provided by Fastly. Learn more at Fastly.com.
[55.62 --> 60.36]  And get your feature flags powered by LaunchDarkly. Get a demo at LaunchDarkly.com.
[61.44 --> 64.02]  This episode is brought to you by Teleport.
[64.24 --> 69.60]  Teleport lets engineers operate as if all cloud computing resources they have access to are in the same room with them.
[69.96 --> 77.28]  SSO allows discovery and instant access to all layers of your tech stack behind NAT, across clouds, data centers, or on the edge.
[77.64 --> 80.88]  I have Ev Consovoy here with me, co-founder and CEO of Teleport.
[80.88 --> 88.30]  Ev, help me understand industry best practices and how Teleport Access Plan gives engineers unified access in the most secure way possible.
[88.50 --> 94.96]  So the industry best practice for remote access means that the access needs to be identity-based,
[95.22 --> 99.18]  which means that you're logging in as yourself. You're not sharing credentials from anybody.
[99.44 --> 101.94]  And the best way to implement this is certificates.
[102.38 --> 106.44]  It also means that you need to have unified audit for all the different actions.
[106.44 --> 112.18]  With all these difficulties that you would experience configuring everything you have, every server, every cluster,
[112.42 --> 117.46]  with certificate-based authentication and authorization, that's the state of the world today that you have to do it.
[117.66 --> 121.86]  But if you are using Teleport, that creates a single endpoint.
[122.20 --> 127.30]  It's a multi-protocol proxy that natively speaks all of these different protocols that you're using.
[127.30 --> 136.68]  It makes you to go through SSO single sign-on, and then it transparently allows you to receive certificates for all of your cloud resources.
[137.10 --> 141.30]  And the beauty of certificates is that they have your identity encoded, and they also expire.
[142.04 --> 146.30]  So when the day is over, you go home, your access is automatically revoked.
[147.20 --> 149.30]  And that's what Teleport allows you to do.
[149.30 --> 157.86]  So it allows engineers to enjoy the superpowers of accessing all of cloud computing resources as if they were in the same room with them.
[157.96 --> 159.08]  That's why it's called Teleport.
[159.28 --> 162.64]  And at the same time, when the day is over, the access is automatically revoked.
[162.94 --> 164.10]  That's the beauty of Teleport.
[164.42 --> 168.34]  All right, you can try Teleport today in the cloud, self-hosted or open source.
[168.70 --> 170.90]  Head to goteleport.com to learn more and get started.
[171.26 --> 173.30]  Again, goteleport.com.
[179.30 --> 191.72]  Let's do it.
[192.28 --> 193.34]  It's go time.
[193.90 --> 198.66]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[199.36 --> 205.16]  Subscribe if you're new at gotime.fm and follow the show on Twitter for the unpopped polls,
[205.16 --> 211.32]  notifications of when we go live, and other solid tweets like interesting repos from your fellow gophers.
[211.68 --> 213.08]  We are at gotime.fm.
[213.36 --> 214.48]  All right, that's all for me.
[214.72 --> 215.32]  Here we go.
[225.30 --> 226.14]  Hi, everyone.
[226.30 --> 229.50]  Welcome to our episode about hacking with Go.
[229.56 --> 234.86]  So this time we're not talking about Go and security or things like that,
[234.86 --> 238.46]  that we have two hackers who are occasional members of the Go community,
[238.46 --> 244.46]  and we'll be learning about how Go is used for things like hacking, whatever that means.
[244.78 --> 250.82]  So we are joined today by Joakim, who is a researcher.
[251.38 --> 255.82]  You're a security researcher at Intensa, and you became a gopher in 2016
[255.82 --> 258.48]  and have been hunting bad gophers since 2018.
[258.84 --> 259.44]  That's right.
[259.60 --> 260.18]  Great to have you.
[260.44 --> 260.80]  Thank you.
[260.80 --> 263.16]  We also have Jags.
[263.36 --> 263.80]  That's easy.
[264.00 --> 270.72]  Who is a principal threat researcher at SentinelOne and professor at the Johns Hopkins AIS
[270.72 --> 272.24]  Altarovich Institute.
[272.56 --> 273.38]  What is that place?
[273.48 --> 274.56]  What is that wonderful place?
[274.82 --> 275.78]  Oh, that wonderful place.
[275.92 --> 277.82]  So it's Johns Hopkins.
[278.58 --> 282.54]  We just started a new institute under Dmitry Altarovich, you know, with his blessing.
[282.80 --> 285.92]  So just trying to do cyber research, cybersecurity stuff.
[285.92 --> 286.36]  Super.
[286.94 --> 288.60]  It's very great to have you today.
[288.78 --> 292.60]  And I am joined by my co-host, Matt.
[292.76 --> 293.04]  Hello.
[293.48 --> 294.24]  You all know Matt.
[294.36 --> 297.44]  You will hear him every episode, even when he's not around,
[297.52 --> 299.96]  because he has the song of Unpopular Opinion.
[300.46 --> 300.80]  Hello.
[301.30 --> 302.96]  Matt, it's great to have you here.
[303.26 --> 304.72]  So what was the name of your first pet?
[304.98 --> 305.74]  My first pet.
[307.34 --> 307.82]  LB.
[308.80 --> 310.40]  And your mother's maiden name?
[310.42 --> 311.28]  And how do you spell that?
[311.66 --> 311.88]  Yeah.
[311.88 --> 312.94]  Oh, I see what's happening.
[314.10 --> 315.28]  I've fallen for it.
[316.20 --> 318.02]  What's your favorite security question, Natalie?
[318.54 --> 318.78]  Other.
[319.34 --> 319.62]  Other.
[319.80 --> 320.62]  Yeah, it's a good one, that.
[321.94 --> 323.66]  That's a race to the bottom at this point.
[325.16 --> 332.88]  So, gentlemen, please tell us what programming languages do you commonly use for hacking?
[333.20 --> 335.06]  Well, just to kind of put things in context, right?
[335.14 --> 338.82]  Like we are, it's sort of charitable to put us in the context of hackers.
[338.82 --> 342.74]  We are very much in the security research side of the house.
[342.96 --> 347.92]  So as much as we're kind of interacting with hackers or their byproducts all day long,
[348.04 --> 350.34]  we are more on the receiving end, right?
[350.36 --> 354.16]  So you want to try to reverse engineer whatever malware you find,
[354.26 --> 356.94]  figure out what it is that they're doing, do a little bit of threat hunting.
[356.94 --> 364.08]  And at least in my case, where I'm focused on targeted attacks and cyber espionage and kind of nation state sponsored stuff,
[364.52 --> 372.42]  it really becomes more about going from hacks and malware to try and understand campaigns and like, you know, who's doing what and where.
[372.42 --> 378.60]  So at least in my case, like, yeah, I do a little bit of coding in Golang.
[378.84 --> 387.04]  But for the most part, Go became this kind of interesting challenge of new language looks very, very different under the hood,
[387.12 --> 389.08]  looks very different once you get past the linker.
[389.40 --> 395.32]  What the hell are we looking at and how do we reverse engineer this very sort of strange set of constructs in assembly?
[395.32 --> 403.40]  So we could give you some answers about hacking, but I think it might be disappointing in comparison to kind of our side of the house, right?
[403.82 --> 404.00]  Yeah.
[404.48 --> 412.82]  I think it can add also sort of comparing binaries produced by the Go compiler versus like other languages.
[413.20 --> 418.40]  It is a goldmine when it comes to miscellaneous data that's in it,
[418.40 --> 427.08]  which makes sometimes our work maybe slightly easier because it doesn't sometimes include like information on the host where it was compiled.
[427.28 --> 430.08]  Like you get file paths and things like that.
[430.10 --> 436.60]  So you can then start sort of track between maybe families that have nothing else in common in terms of the code,
[436.68 --> 441.20]  but you can see from unique folder names and things like that.
[441.20 --> 445.54]  I guess we're kind of putting like the cart before the horse, right?
[445.54 --> 446.12]  Like, yeah.
[446.52 --> 446.82]  All right.
[446.90 --> 451.38]  So in an attempt to address Natalie's question and hopefully bring everybody along with us,
[451.46 --> 456.04]  for the most part, when you're dealing with malware and just hacks in general,
[456.38 --> 462.86]  C tends to be the most popular language, maybe some C++ if you're looking at some more kind of professional grade malware,
[463.20 --> 465.82]  but you'll see malware of just about every stripe, right?
[465.82 --> 470.84]  Like if you're looking at Brazilian banking trojans, they almost always write them in Delphi.
[471.04 --> 473.58]  Like there's people who like doing compiled Python.
[473.58 --> 475.14]  You can find just about everything.
[475.86 --> 479.92]  What we end up doing is, you know, you get a binary that's usually stripped.
[480.24 --> 481.28]  There's no context.
[481.38 --> 482.12]  There's no source code.
[482.22 --> 483.24]  There's no debug symbols.
[483.84 --> 486.74]  And you have to, you basically work backwards.
[486.74 --> 491.02]  Like we want to take that compiled binary and reverse engineer it and figure out the functionality,
[491.26 --> 496.06]  figure out what it was the programmers intended to do and kind of take it from there.
[496.14 --> 498.40]  And it's a little bit of a Rubik's cube, right?
[498.40 --> 502.78]  Every time you come at a different binary, you're trying to figure out, you know, how do they build it?
[503.06 --> 504.02]  What programming language?
[504.20 --> 506.14]  What linker compiler version?
[506.14 --> 511.62]  And, you know, just start sort of building an understanding of layers and layers of abstraction until you can go,
[512.06 --> 519.38]  okay, yeah, this, you know, two megabyte binary in reality is just trying to hijack your browser so that it can take your bank account.
[519.52 --> 521.28]  And these folks can try to steal your money.
[521.48 --> 523.46]  It's like, okay, that's your ultimate understanding.
[523.70 --> 529.58]  But between getting a binary and getting to that, it's just many layers of confusion that you're just kind of working your way through.
[529.58 --> 529.98]  Yeah.
[530.14 --> 542.90]  And also add all of the sort of things that malware authors do to make that job even harder with regards to obfuscating stuff and encrypting payloads and decrypting it in memory.
[543.18 --> 549.42]  And so it's like when you first like look at it, you don't see the original sort of behavior.
[549.80 --> 551.36]  You have to start working.
[551.36 --> 560.06]  And it's almost like these, well, sometimes it can be like those Russian dolls where you just have to, you open it up and open it up and you just get smaller and smaller and smaller.
[560.14 --> 562.02]  And eventually you get to the piece that you need.
[562.40 --> 567.60]  You mentioned that Go has a lot of extra data in there that makes it easier.
[567.68 --> 569.24]  It's like a goldmine of data in there.
[569.30 --> 570.94]  But how does that make it easier then?
[571.04 --> 577.68]  Is it about that that you're able to kind of unpick it in some way and learn more as you dig into it?
[577.68 --> 578.12]  Yeah.
[578.48 --> 589.78]  I mean, so what Juan was talking about first was most of the times when we get like binaries that are written in C and compiled, like they strip out all the symbols and everything.
[589.90 --> 592.52]  So you don't have any names of the functions or anything like that.
[593.18 --> 597.78]  And you can do the same for like gold binaries with the compiler flags.
[597.92 --> 600.02]  But that information is still there.
[600.12 --> 601.92]  It's available in other data structures.
[601.98 --> 603.02]  It's not in the symbols.
[603.02 --> 613.32]  So a lot of the tooling that we have and we use, we pull that information and we kind of recreate what would be the symbols so we can get the function names and stuff like that.
[613.90 --> 616.44]  And it was like some of us have looked into this more in detail.
[616.70 --> 621.66]  But, you know, you're using some of the data that's not intended for what it's supposed to be.
[621.72 --> 624.10]  And we're sort of using it because it's available.
[624.10 --> 630.74]  I mean, the nice panic functionality, but you get the nice stack traces, which means it has that information.
[631.02 --> 633.44]  So just about knowing where to find it.
[633.50 --> 637.46]  And then you work your way backwards and you sort of can align it.
[637.90 --> 642.02]  So recently we released a little project called Alpha Golang.
[642.44 --> 649.26]  It's kind of a nod at AlphaGo and sort of DeepMind's attempt to master Go the game rather than Go the programming language.
[649.26 --> 653.02]  So compiling is kind of an entropic process, right?
[653.10 --> 660.68]  You're losing all this added flavor and syntactic sugar that makes programming understandable to human beings.
[660.98 --> 668.38]  All of that gets taken away and you can't really get it back unless, you know, you have all this extraneous information that comes with having built the project yourself.
[668.38 --> 680.94]  And I think when folks first approached reverse engineering Go, you had that absence of information and you had a lack of understanding of the Go paradigm, right?
[680.98 --> 688.76]  Like how different the programming was, a lack of understanding of all the magic that the linker is doing along the way to make even simple things work.
[688.76 --> 709.36]  Like, you know, in order to have multiple return values, which is a, you know, fantastic thing that Go enables, the way the linker manages that is that it adds, it peppers extra functions every time there's a function call that creates a runtime stack in order to allow you to have somewhere to put those values when you're going to come back, when you're going to return from the function.
[709.36 --> 719.46]  But when you don't have an understanding of how the linker works, how Go works, what you're really just looking at is why the hell is it calling another function every time we're going into and it's returning?
[719.62 --> 721.74]  Like, I can't find the arguments anymore.
[721.86 --> 722.72]  Like, where did all this go?
[722.76 --> 726.98]  You're just kind of in this hurricane of information and you have no idea what's happening.
[727.56 --> 738.50]  I think the myth that we wanted to dispel, and this comes years after the fact, is that in reality, Go might be one of the easiest programming languages to reverse engineer.
[738.50 --> 748.38]  Just by the way that the linker was designed, it'll actually break if you try to remove all of the information, all of the debug information out of the binary.
[748.66 --> 760.14]  So it turns out that if we get really clever with our reversing tools, you can actually get a pretty comprehensive understanding of what the binary is doing without having to spend a whole ton of analyst time.
[760.50 --> 761.80]  Yeah, I agree with you there.
[761.80 --> 767.86]  I've looked at so many Go binaries at this point, but I find it easier than other languages.
[768.50 --> 769.26]  So what they spit out.
[769.54 --> 772.64]  You said that the linker needs that information to do its job.
[772.82 --> 779.32]  Could you not do all that, get the final binary, and then go and do some work to obfuscate more?
[779.84 --> 784.28]  So what we use is, for example, the type information is still there.
[784.42 --> 788.10]  And we can utilize that to actually reconstruct all the type definitions.
[788.66 --> 789.80]  With the names as well?
[790.02 --> 791.36]  Yes, the names is there.
[791.36 --> 792.56]  It's used by the runtime.
[792.56 --> 802.70]  So there is a shared structure, both in the reflect package and the runtime and also in the linker that is sort of just copied by text.
[803.40 --> 806.30]  And that's how all the type information is stored.
[806.30 --> 816.10]  And you walk that table and you can reconstruct all the types that goes from a struct type to all its subfields and everything.
[816.22 --> 821.92]  And you get that back to remove that because every time when you're allocating memory for it.
[822.00 --> 827.58]  So when you create a new object, there is a function in the runtime that essentially just called malloc.
[827.84 --> 832.80]  But that size of that struct or whatever it needs to allocate is stored in that data structure.
[832.94 --> 833.82]  So you can't wipe it.
[833.82 --> 835.88]  Right. So it needs it in order to work.
[836.10 --> 836.82]  Yeah. Yeah.
[837.14 --> 840.52]  I feel like we have to be kind of careful not to set up a challenge, right?
[840.56 --> 844.12]  Like it's not to say that someone couldn't get super, super clever.
[844.66 --> 846.72]  And because this happens on Windows too, right?
[846.72 --> 852.94]  Like the folks that write packers and obfuscators, like there have been some really, really clever packers along the way.
[853.12 --> 857.82]  And that's kind of the way that polymorphism sort of grew into the antivirus and virus community.
[857.82 --> 860.28]  It's like, well, you know, you guys think you're so clever.
[860.28 --> 865.10]  Let's see what happens if this thing basically reshifts itself every time that you execute it.
[865.18 --> 866.78]  And you're like, okay, well, this isn't going to be nice.
[867.36 --> 875.74]  However, I think you kind of have to weigh that against the value of writing malware in Golang, which is, well, I just wrote this piece of ransomware once.
[875.74 --> 881.16]  And now I can cross compile it and it has all these nice efficiencies and like concurrency is easy.
[881.52 --> 887.56]  Like all the features that we like as programmers are suddenly a boon for folks that are doing not so great things.
[887.86 --> 887.96]  Yeah.
[888.08 --> 890.90]  So do you prefer rubbish programming languages for that reason?
[892.74 --> 893.60]  I don't know.
[893.60 --> 898.26]  I mean, I'm learning to love reversing Go because it's drastically easier.
[898.64 --> 900.36]  Like first, I like writing Go.
[900.84 --> 902.22]  It makes a little more sense to me.
[902.36 --> 917.70]  And then also we've written some scripts that allow us to like undo the debug stripping that you can do with the compiler that allow us to put all of the function names back into all the functions that we're sort of discovering through our reverse engineering tools.
[918.02 --> 922.04]  Then like we can sort all of those function names by package.
[922.04 --> 925.86]  So since Go, like I wish Ivan was here.
[925.96 --> 927.36]  I know Ivan was supposed to join us.
[927.86 --> 931.48]  And he has this great expression that like Go is fascist Python.
[932.18 --> 937.50]  That fascism, sorry to put it that way, but that fascism kind of allows us to do a lot, right?
[937.54 --> 944.26]  You can go, hey, we can essentially separate everything that we know is part of the standard library.
[944.26 --> 946.94]  That's part of like GitHub repositories.
[946.94 --> 956.84]  And unlike any other programming language that you might want to reverse engineer, in this case, we can literally sift down to what are the user written functions.
[956.84 --> 966.18]  So, you know, we were looking at malware like Sunburst, which is part of this really famous SolarWinds attack that happened a few months ago.
[966.46 --> 973.94]  When you look at one of those binaries, they're like, I want to say like 40,000 functions that get discovered post compilation, right?
[973.94 --> 978.28]  Because there's a lot of stuff that gets added by the linker and things that you don't think about.
[978.78 --> 983.64]  So if you're looking at it blindly, it's like, oh, my God, 40,000 functions and I have to figure out what the hell I'm looking at.
[983.80 --> 993.00]  If you run it through all of those processing scripts that we were talking about, you can actually get it down to like, here's 22 functions that the malware developers actually wrote.
[993.00 --> 1003.42]  Instead of like getting trapped in the runtime and sort of losing your way and, you know, phoomped and like all these other like packages that you don't really want to spend your time reversing, right?
[1003.58 --> 1004.74]  You also have to add to that.
[1005.10 --> 1017.96]  I think last time that I checked might have been like go 1.16, like the hello world had about 1700 functions and then one main function that just printed a line.
[1017.96 --> 1029.60]  You start with basically nothing like you get at the entry point, which is the small pieces of the ghost in a library or the gold code that is actually written in assembly.
[1030.08 --> 1031.52]  That's where you land.
[1031.94 --> 1038.70]  And then there's this bootstrapping of the runtime and the scheduler and all that stuff, which you don't need.
[1039.00 --> 1046.68]  And then somewhere in that, all of those functions, you need to find where does it call main dot main?
[1046.68 --> 1051.44]  Because until you get to that point, you haven't even started your work yet.
[1051.80 --> 1052.66]  That does make sense.
[1052.80 --> 1059.68]  Could you not just like compare like a simple go binary and do like a diff on two to see what's different?
[1059.78 --> 1062.24]  Like, could you make a simple hello world and diff it with?
[1062.48 --> 1070.18]  That's kind of like some of the sort of the initial techniques that was used when people started to sort of analyzing go binaries.
[1070.18 --> 1079.10]  You would basically use the information that you could get from the strings to kind of figure out which version of the compiler is this.
[1079.40 --> 1080.20]  Oh, it's this.
[1080.34 --> 1081.86]  And it's using these imports.
[1082.30 --> 1086.18]  Let me just build a binary that imports all of those packages.
[1086.18 --> 1089.18]  And then I'll generate like signatures for those functions.
[1089.18 --> 1092.18]  And then I put those signatures on top of what I have.
[1092.32 --> 1095.44]  And what is not detected, that's what I'm looking at.
[1095.62 --> 1097.26]  Yeah, that's so clever.
[1097.68 --> 1099.38]  That's one way to try to go about it.
[1099.48 --> 1104.38]  And frankly, I think that's still part of the phase where we're kind of knocking about in the dark room.
[1104.46 --> 1105.48]  We don't know where the walls are.
[1105.56 --> 1106.78]  We don't know where the light switches are.
[1107.20 --> 1109.64]  Because if you think about it, it sounds simple.
[1109.76 --> 1114.18]  Like, okay, we're going to write something with the same packages and compile it and so on.
[1114.18 --> 1116.94]  But then you start getting into the flavors of things, right?
[1117.00 --> 1118.70]  Like, what versions of this were they using?
[1119.06 --> 1121.10]  What version of the compiler were they using?
[1121.36 --> 1122.42]  What did they link against?
[1122.62 --> 1124.04]  What was it built for?
[1124.38 --> 1125.56]  Target architectures.
[1125.66 --> 1131.32]  Like, the linker actually works slightly differently if you're on Elf versus MacGo versus Windows.
[1131.52 --> 1138.16]  So, like, that's when you start to get into this world of infinite variations that kind of takes the wind out of your sails.
[1138.72 --> 1143.80]  And normally, it would just be kind of this slightly disastrous situation, right?
[1143.80 --> 1147.40]  Like, when you look at C++, there really aren't that many shortcuts for C++.
[1147.70 --> 1154.24]  There's flirt signatures and other little tools that we can use to try to get some of the functionality out of the way.
[1154.52 --> 1162.06]  But that entropy that gets involved in the compilation process means, for example, like, classes are gone.
[1162.52 --> 1163.82]  Like, class definitions are gone.
[1164.12 --> 1165.60]  You have these virtual tables.
[1166.22 --> 1168.10]  We have no idea what reference is what.
[1168.18 --> 1172.30]  So, you don't even have a perfect control flow unless you're dynamically executing the samples.
[1172.30 --> 1177.20]  So, like, there's a lot of ways that you don't really have a clear path forward.
[1177.20 --> 1181.82]  And it takes a lot of work to try to reverse engineer complex C++ binaries.
[1182.22 --> 1184.42]  And that's how it felt when you first get to Go.
[1185.00 --> 1188.96]  Eventually, we figured out that there are actually wonderful ways to rebuild Go binaries.
[1188.96 --> 1192.40]  Now, we're looking at other things that are not so nice, right?
[1192.46 --> 1195.18]  Like, now that it feels like Go is...
[1195.18 --> 1199.00]  I won't say that we've, like, you know, bested Go and reversing is super easy.
[1199.16 --> 1201.58]  But it's so much more approachable.
[1201.72 --> 1203.42]  And now we're looking at things like Rust.
[1203.48 --> 1206.18]  And it's like, oh, my God, reversing Rust is awful, right?
[1206.18 --> 1208.30]  Like, it's so much closer to C++.
[1208.48 --> 1211.10]  And now we don't, you know, we don't really know what to do once again, right?
[1211.10 --> 1214.70]  Hmm, that's interesting, because I probably wouldn't have guessed that.
[1215.00 --> 1219.82]  I would have thought Rust would be, in some ways, more deterministic.
[1220.48 --> 1221.20]  But that's interesting.
[1221.62 --> 1225.94]  The problem where this stemmed from is, like, these new languages,
[1226.12 --> 1230.98]  they kind of shifted from the dynamic linking to statically linking libraries.
[1231.44 --> 1235.52]  So that's where the major hurdle comes from.
[1235.52 --> 1240.74]  And analyzing a dynamic linked whatever, it's relatively easy,
[1240.78 --> 1243.96]  because you know it imports those specific functions.
[1244.34 --> 1246.76]  So you know what it's going to call at that point.
[1247.40 --> 1251.34]  But when you get a binary, and it just suddenly...
[1251.34 --> 1256.98]  It has SQLite, it has OpenSSL, and all these other libraries inside it,
[1257.20 --> 1258.86]  and you just see a function call.
[1259.28 --> 1260.66]  You have no clue where you're at.
[1261.66 --> 1265.10]  So you can run into those two with, like, C and C++.
[1265.10 --> 1269.98]  But obviously, with Go and Rust, that's the default.
[1270.18 --> 1272.98]  So every Rust binary, in general, will be like that.
[1273.62 --> 1276.82]  Yeah, it might be a little bit unfair to Rust, which is probably fine, too.
[1277.76 --> 1278.66]  Fine on this podcast.
[1278.96 --> 1280.82]  In this podcast, it's perfectly fine.
[1280.98 --> 1284.56]  You know, there are no Rust stations that are going to come beat my door down.
[1284.74 --> 1286.90]  But I'll say we're probably being a little bit unfair,
[1287.00 --> 1290.54]  in the sense that if we had had this conversation about Go four years ago,
[1290.74 --> 1292.68]  we would have probably said the same thing, right?
[1292.72 --> 1294.52]  Like, oh my god, it's awful reverse engineer.
[1294.52 --> 1296.04]  We have no idea where we are.
[1296.16 --> 1302.48]  There's all this cruft of, like, statically linked code that has nothing to do with the program itself.
[1302.80 --> 1304.82]  That's kind of what it feels like in Rust right now.
[1305.04 --> 1310.10]  I'm hoping that as we get more familiar with that paradigm and our tools improve,
[1310.20 --> 1312.72]  that we'll also get into a better place with Rust.
[1312.72 --> 1315.32]  But there's nothing to say that that's going to be the case, right?
[1315.38 --> 1319.28]  Like, C++ has been C++ for the past, you know, however many years.
[1319.80 --> 1320.68]  And there's still...
[1320.68 --> 1326.38]  I can probably count on one hand the folks that are, like, genuinely proficient at reversing C++.
[1326.74 --> 1330.52]  Like, there's, like, stars of reverse engineering, like, rough roles.
[1330.52 --> 1336.40]  But it's definitely not me or many of the folks that I, like, get to reverse with.
[1336.96 --> 1340.32]  So there's nothing saying that that's going to get better.
[1340.48 --> 1342.06]  We just have high hopes that we might.
[1342.06 --> 1359.06]  This episode is brought to you by our friends at Incident.io.
[1359.46 --> 1361.94]  Every software team on the planet has to manage incidents,
[1362.12 --> 1365.66]  and a very large percentage of those teams are using Slack to communicate.
[1365.66 --> 1366.84]  That includes us.
[1367.30 --> 1372.04]  With Incident.io, you can create, manage, and resolve incidents directly inside Slack.
[1372.38 --> 1373.28]  Here's how it works.
[1373.54 --> 1375.62]  Head to Incident.io and sign up for free.
[1375.84 --> 1377.24]  Then add it to your Slack.
[1377.42 --> 1381.28]  From there, you have a brand new Incidents channel where all incidents get announced.
[1381.64 --> 1384.22]  Use the slash incident command to create and manage incidents.
[1384.64 --> 1389.02]  This command lets you share updates, assign roles, set important links, and more,
[1389.36 --> 1391.22]  all without ever leaving the Incident channel.
[1391.40 --> 1396.62]  Each incident gets their own Slack channel plus a high-res dashboard at Incident.io
[1396.62 --> 1399.10]  with the entire timeline from report to resolution.
[1399.64 --> 1401.78]  Get everyone on the same page from the moment they join the incident.
[1402.06 --> 1403.68]  and help stakeholders stay in the loop.
[1404.04 --> 1407.20]  Add Incident, ILG, or Slack today and prove to yourself and your team
[1407.20 --> 1409.78]  that they have everything you need to streamline your incident management.
[1410.26 --> 1412.68]  Learn more and sign up for free at Incident.io.
[1412.96 --> 1414.04]  No credit card required.
[1414.54 --> 1415.98]  Again, Incident.io.
[1415.98 --> 1434.86]  So when you reverse engineering things,
[1434.86 --> 1439.36]  you mentioned that you can get the names of functions and the names of types.
[1439.36 --> 1441.96]  But I mean, how useful is that?
[1442.06 --> 1446.48]  Are hackers, like, are they writing code and they've got, like, a function called steal credit card?
[1447.06 --> 1449.58]  Like, it can't be as simple as that.
[1449.70 --> 1450.00]  Yes.
[1451.76 --> 1452.68]  Sometimes, yeah.
[1452.92 --> 1453.10]  Yeah.
[1453.10 --> 1454.62]  So I wrote a tool.
[1455.08 --> 1455.90]  I open sources.
[1456.10 --> 1457.62]  I think it was about two years ago.
[1458.12 --> 1461.44]  And what it does is, like, you throw it in a Go binary.
[1461.62 --> 1463.06]  It will extract that information.
[1463.88 --> 1468.40]  And it will print out, like, a source code projection.
[1468.58 --> 1475.40]  So you get the folder, file, and then functions, and then the line numbers where the functions start and ends.
[1475.40 --> 1478.68]  You print that out, and you can look at samples.
[1479.60 --> 1488.02]  And many times, like, I'll just throw a bunch of Go binaries and just go through it and go loader, rat, ransomware.
[1488.60 --> 1489.72]  Oh, that's a new backdoor.
[1490.22 --> 1491.90]  You know, because you see the function names.
[1492.12 --> 1498.14]  Like, there are these encrypt, get key, drop note, walk file system.
[1498.44 --> 1500.22]  You know, I see only encrypt.
[1500.28 --> 1501.80]  I never see a decrypt function.
[1502.08 --> 1504.96]  Like, you know, it's pretty clear what this is doing.
[1505.86 --> 1506.76]  Just from, like, the name.
[1506.84 --> 1509.88]  It's nice to know that hackers use good practices in software.
[1510.02 --> 1510.22]  Yeah.
[1510.46 --> 1510.62]  Yeah.
[1511.04 --> 1512.02]  Well, more or less.
[1512.76 --> 1514.90]  Then you get into, like, obfuscators, right?
[1515.14 --> 1515.40]  Yeah.
[1515.50 --> 1517.28]  So there are some obfuscators.
[1517.36 --> 1523.86]  But I can tell you, like, I so far haven't seen a legitimate application or anything like that using an obfuscator.
[1524.20 --> 1527.08]  So, like, you see just garble letters.
[1527.08 --> 1532.88]  And also the interesting part with sort of all the UTF-8 characters being allowed.
[1532.88 --> 1543.76]  But if you see a function name that is just a mixture between Cyrillic and Korean character set and Chinese character set just mixed together, you go, well, that's not.
[1544.02 --> 1546.04]  It's like, that's obvious.
[1546.32 --> 1546.36]  Right.
[1546.76 --> 1550.64]  Or it's a really smart person like Natalie who speaks many, many languages.
[1551.04 --> 1551.34]  Right.
[1552.00 --> 1552.48]  Yeah.
[1552.48 --> 1559.76]  When you have to start installing font just to be able to print out the characters, you know, like, this is because, like, every other character is missing.
[1560.10 --> 1560.26]  Yeah.
[1560.98 --> 1561.42]  Yeah.
[1561.48 --> 1563.80]  But I think I'd throw you off the scent.
[1563.96 --> 1567.88]  I'd call the function, like, don't steal the credit card information.
[1567.88 --> 1573.38]  Just that reverse psychology in the binaries, right?
[1573.56 --> 1573.98]  Exactly.
[1574.20 --> 1576.52]  It's reversing the reverses, essentially.
[1576.88 --> 1577.04]  Yeah.
[1577.36 --> 1585.96]  One of the most interesting, from, like, a reverse engineer's perspective, like, one of the weirdest thing I've seen is this binary.
[1585.96 --> 1592.20]  All the strings is sort of hidden, but they are hidden as the function name of a function.
[1592.98 --> 1596.14]  And then what it does is it executes the function.
[1596.24 --> 1600.00]  It uses reflect to figure out where it is to get its own function name.
[1600.22 --> 1604.16]  And then that is an XOR with a key to get the string back up.
[1605.04 --> 1609.04]  That's one of the most interesting kind of obfuscation techniques I've seen.
[1609.66 --> 1609.98]  Yeah.
[1609.98 --> 1611.72]  You start to get into a lot of cleverness.
[1611.72 --> 1617.22]  Like, there's certain packers that are just, like, you open a binary and it's full of passages from Shakespeare.
[1617.92 --> 1623.40]  And what the packer is supposed to do is, you know, go through that passage, cherry pick things, and rebuild dynamically.
[1623.82 --> 1630.88]  There's this big cat and mouse game, particularly in the Windows world, between malware developers and security researchers.
[1631.28 --> 1633.96]  And, you know, you've got these strange metrics, right?
[1634.00 --> 1638.18]  Because we've been talking about reverse engineering for understanding.
[1638.38 --> 1640.38]  Like, we want to know what the sample does.
[1640.38 --> 1646.42]  But from the perspective of a malware developer, their biggest initial concern is just not getting detected.
[1646.92 --> 1658.02]  So you have to, as a malware dev, you kind of have to walk a fine line between how difficult do I want to make it for Joakim or for me to understand what the binary is doing?
[1658.44 --> 1665.58]  But also, how can I fly under the radar so that an antivirus doesn't go, hey, this looks super weird, detect, right?
[1665.70 --> 1667.82]  Like, it's a touchy balance.
[1667.82 --> 1671.40]  I see Matt is trying to think of smarter ways for the functions.
[1671.54 --> 1673.40]  I'm also wondering what can be good.
[1673.40 --> 1680.92]  Well, that's what I realized as I was falling into that trap of trying to now, like, turning it into a game.
[1681.02 --> 1681.62]  Yeah, yeah.
[1681.70 --> 1683.72]  And it is kind of fun, isn't it?
[1683.76 --> 1688.40]  You know, in some situations, it's a very serious impact that these things can have.
[1688.90 --> 1691.50]  But it does have that, we can't deny it.
[1691.50 --> 1695.98]  It's the kind of cool area of coding, you know, hacking.
[1696.18 --> 1700.70]  It's kind of, a lot of people grew up with popular culture was around hacking.
[1700.96 --> 1704.78]  And I think some people probably get into programming for that reason.
[1705.44 --> 1711.38]  And, you know, mischief at a distance was definitely a motivator for me when I started writing scripts.
[1711.38 --> 1713.38]  And I'd do things like little pranks.
[1713.52 --> 1714.68]  Mine would always be pranks.
[1715.04 --> 1723.66]  So I would, like, on the auto-exec bat on a floppy disk, I would change, overwrite the wallpaper on the school computers or something like that.
[1723.72 --> 1725.86]  And so all I had to do is put a floppy disk in.
[1725.94 --> 1731.16]  And the next time the machine booted up, it would, the wallpaper would then change, you know.
[1731.24 --> 1733.96]  So, and it would always be just prank things like that.
[1734.28 --> 1734.38]  Right.
[1734.38 --> 1738.14]  But it is something that is very kind of enticing.
[1738.52 --> 1740.12]  The stakes have been ratcheting up.
[1740.40 --> 1742.42]  It's really easy to kind of look at it that way.
[1742.60 --> 1745.50]  And we don't want to make it, like, too dark or too heady.
[1745.78 --> 1751.72]  But now this is the playground of also a lot of nation states and a lot of criminals.
[1751.72 --> 1757.24]  And, you know, if you're in the U.S., it's kind of like the ransomware epidemic is sort of unavoidable, right?
[1757.26 --> 1759.12]  Like, you have to talk about it every day.
[1759.34 --> 1761.92]  And that's where things get less pretty, right?
[1761.92 --> 1769.12]  Like, if you're at a hospital that can't help folks because all of their, you know, tragically outdated Windows XP systems are in a flat network.
[1769.12 --> 1771.10]  And all of them got popped at the same time.
[1771.40 --> 1773.84]  That's where you go, well, yeah, that code was fun.
[1774.28 --> 1778.00]  I love the idea of just having these, you know, kind of hacking superpowers.
[1778.26 --> 1781.20]  But there's a side to it that isn't quite so cute.
[1781.62 --> 1784.40]  And I think we're kind of walking that line all the time, right?
[1784.42 --> 1786.48]  Where you go, oh, this is fascinating.
[1786.56 --> 1790.80]  And you just get wrapped up in the functionality and what someone has been able to accomplish.
[1790.80 --> 1797.26]  And it's easy to forget, like, oh, well, this is actually a part of a much, much heavier game.
[1797.52 --> 1797.62]  Yeah.
[1797.76 --> 1798.50]  No, absolutely.
[1798.78 --> 1799.90]  I think that's a very good point.
[1800.28 --> 1802.50]  By the way, I'd just change all the hospital wallpaper.
[1802.86 --> 1805.78]  Like, if I ever broke it and that's all that's happened.
[1805.90 --> 1806.96]  That's how you'll know it's me.
[1807.18 --> 1807.42]  Right.
[1807.50 --> 1809.12]  It'd just be my face smiling as well.
[1809.36 --> 1810.08]  Such an idiot.
[1811.28 --> 1812.22]  Hope you feel better.
[1812.56 --> 1812.74]  Yeah.
[1813.14 --> 1814.12]  Oh, exactly.
[1814.46 --> 1814.78]  Yeah.
[1814.78 --> 1816.94]  But how often do you even reach the desktop?
[1817.66 --> 1822.68]  I can imagine that if you have a computer at the reception of some hospital department.
[1822.94 --> 1826.02]  Like, how often do you really close everything and reach the desktop?
[1826.28 --> 1827.22]  You'll never see that, Matt.
[1827.24 --> 1828.68]  You're going to have to come up with something better.
[1828.84 --> 1829.92]  You think they just wouldn't notice?
[1830.16 --> 1830.26]  Yeah.
[1830.38 --> 1831.06]  That's a fair point.
[1831.36 --> 1833.50]  Maybe Matt already did that and nobody ever knew.
[1833.60 --> 1834.34]  Nobody noticed.
[1834.52 --> 1835.04]  Oh, yeah.
[1835.88 --> 1836.90]  A bit disappointing.
[1836.90 --> 1842.62]  I mean, a fun thing to do with hacking, if you want to play with that more, is go and do CTFs, right?
[1843.00 --> 1843.26]  Right.
[1843.76 --> 1844.10]  All right.
[1844.18 --> 1846.44]  Getting away from the dark side of the house, right?
[1846.54 --> 1852.42]  Like, there's a good community of red teamers and pen testers who like Go.
[1852.60 --> 1857.70]  So, for those who are new completely to this terminology, what are all those fancy words?
[1857.92 --> 1860.08]  We would be on the blue team side, right?
[1860.12 --> 1861.60]  Like, we're on the defender side.
[1861.68 --> 1863.76]  We're just trying to make sure that bad things don't happen.
[1863.76 --> 1869.58]  There is the red team side, which is more folks that are emulating attackers, right?
[1869.66 --> 1879.90]  Like, we're going to get paid to come to one of these hospitals and hack them on purpose within certain constrained boundaries to say, look, here are the weak spots of your network.
[1880.14 --> 1882.24]  These are the things that you should be fixing now.
[1882.46 --> 1886.10]  So, it tends to be kind of opposing sides of the house, but, you know, we're all friends.
[1886.10 --> 1894.80]  And there is actually a community, a strong community of folks who like doing that sort of development and red teaming tools on Go.
[1894.88 --> 1895.96]  Hold on just one second.
[1896.14 --> 1896.24]  Right.
[1896.52 --> 1899.86]  So, red team are the people who do pen testing.
[1900.26 --> 1900.40]  Yeah.
[1900.70 --> 1900.88]  Yeah.
[1901.04 --> 1907.38]  And blue team is the people who go get hired to fix whatever the red team people pointed out.
[1907.56 --> 1908.00]  Sort of.
[1908.08 --> 1908.94]  Call it the defenders.
[1909.58 --> 1909.82]  Yeah.
[1910.18 --> 1911.56]  Broadly speaking, defenders.
[1911.92 --> 1914.62]  And where does white hat, black hat fit in all this?
[1914.62 --> 1917.62]  All of those would theoretically be white hats, right?
[1917.74 --> 1929.20]  You get some cross sections, but if you're working towards improving the general defensive stance of a company or an organization, the government, whatever, all of that technically puts you under white hat, right?
[1929.40 --> 1930.18]  Yeah, that would be me.
[1930.42 --> 1931.14]  I'd be one of those.
[1931.38 --> 1932.32]  Just gentle.
[1932.72 --> 1937.78]  I've proven your wallpaper is up for grabs to anyone who wishes to do it.
[1938.16 --> 1939.18]  Advertisers could do it.
[1939.30 --> 1941.90]  If you want to promote something, pop that on all the hospitals.
[1942.04 --> 1942.34]  Do you know what I mean?
[1942.34 --> 1945.34]  But yeah, so definitely that would be the side I'm on.
[1945.42 --> 1947.10]  I just want to get that out there on the record.
[1947.76 --> 1949.88]  This can also make a really good security question.
[1950.42 --> 1951.62]  What is your wallpaper?
[1952.04 --> 1952.22]  Yeah.
[1952.40 --> 1954.00]  What color hat have you got on?
[1954.34 --> 1955.12]  I thought that's what you meant.
[1955.20 --> 1955.88]  That's a good one too.
[1956.44 --> 1957.64]  So, what's CTF?
[1957.74 --> 1958.64]  What's CTF mean?
[1958.90 --> 1959.18]  Oh, wait.
[1959.26 --> 1961.32]  We were talking about the red and the white hat.
[1961.56 --> 1962.26]  And the blue.
[1963.00 --> 1963.98]  All colored hats.
[1964.24 --> 1964.74]  All the topics.
[1964.74 --> 1973.24]  Yeah, I think for the most part, we're just in the business of tracking and trying to defend against black hats, right?
[1973.40 --> 1979.72]  Like the black hats standard definition would be folks that are getting access to networks are not supposed to.
[1979.82 --> 1985.34]  Nowadays, doing that for effects that are obviously undesirable, if not straight up illegal.
[1985.34 --> 1988.10]  So, there's the espionage side of the house.
[1988.18 --> 1989.68]  There's the sabotage side of the house.
[1990.06 --> 1995.42]  Obviously, ransomware falls well within a long established tradition of like cybercrime.
[1995.64 --> 2000.40]  So, before they used to just want to get access to bank accounts or steal credit card numbers.
[2000.50 --> 2007.32]  Nowadays, instead, you infect an entire enterprise network and then demand $30 million to release it once again.
[2007.32 --> 2010.08]  All those folks fall under the black hat category.
[2010.82 --> 2016.76]  And then, ideally, all your blue teamers, red teamers, pen testers, whatever, are squarely in the white hat side.
[2016.88 --> 2018.46]  Though, you know, some folks dabble.
[2018.90 --> 2019.38]  Not me.
[2019.58 --> 2020.80]  I don't have those skills, sadly.
[2021.12 --> 2023.64]  But it can be a really interesting space, right?
[2023.72 --> 2026.06]  You would probably say that, though, even if you were, wouldn't you?
[2026.24 --> 2030.42]  I'm learning your reverse psychology as far as hacking goes, right?
[2031.08 --> 2034.10]  Definitely not malware is the name of my package.
[2034.46 --> 2035.22]  Exactly, yeah.
[2035.84 --> 2036.78]  That'd work on me.
[2036.78 --> 2038.02]  Yes, exactly.
[2038.14 --> 2044.04]  For those who do want to play a little bit with hacking, there are those competitions of CTF, right?
[2044.18 --> 2044.42]  Yeah.
[2044.62 --> 2045.84]  Of capturing the flag.
[2045.96 --> 2047.52]  So, what is the flag we're capturing?
[2047.88 --> 2048.82]  There's different kinds.
[2048.82 --> 2055.62]  So, you have sort of those kind of capture the flags that would kind of fall more into the red teaming,
[2055.72 --> 2061.74]  which usually involves maybe like compromise a machine that has some vulnerability,
[2062.02 --> 2064.68]  or it can also be a binary that has a vulnerability.
[2064.68 --> 2076.42]  And your goal is to then actually exploit and write an exploit that actually will kind of fetch a flag to prove that you sort of managed to do that.
[2076.42 --> 2081.80]  But then you also have sort of in the CTF, the type of like, that's called like a crack me,
[2081.80 --> 2088.90]  which essentially is a binary that you have to reverse engineer to maybe get it to run properly.
[2088.90 --> 2090.46]  And it's probably not written in Go.
[2090.94 --> 2099.36]  Well, usually with CTFs, they usually would write them in, sometimes you get the very esoteric languages because no one would know it.
[2099.46 --> 2102.58]  And it's, you know, it increases sort of like the challenge.
[2102.84 --> 2103.52]  Like NIMH.
[2103.52 --> 2104.72]  Yeah, it's like NIMH.
[2104.94 --> 2105.08]  Yeah.
[2105.54 --> 2114.00]  This year, so there's a pretty famous, well, famous within our space, reversing capture the flag called the Flare-on challenge.
[2114.22 --> 2117.12]  And that's, you know, Mandiant puts it on every year.
[2117.12 --> 2124.52]  And this year, the like last level, like if you made it all the way through the competition, it was actually a Go binary.
[2124.94 --> 2126.88]  So, you know, I didn't make it all the way.
[2126.98 --> 2128.72]  I had somebody be like, hey, look at this thing.
[2128.76 --> 2134.90]  And like, I'm trying to like rebuild this binary for, you know, much smarter folks to try to finish the competition.
[2135.56 --> 2139.76]  But yeah, I mean, Go is getting up there as far as what reversers you're thinking of.
[2140.18 --> 2140.54]  Yeah.
[2140.80 --> 2142.48]  Is that a good thing for us?
[2142.52 --> 2142.86]  I don't know.
[2142.86 --> 2146.86]  I think DEF CON last year had part of their qualifications.
[2147.06 --> 2148.16]  They had a Rust binary.
[2148.34 --> 2150.06]  That was, I think it was part of that.
[2150.36 --> 2150.64]  Boo.
[2150.74 --> 2152.04]  You get the mixture, you know.
[2152.82 --> 2154.32]  We'll see when we get a NIMH one.
[2155.16 --> 2155.40]  Yeah.
[2155.56 --> 2159.46]  I think it's more speaking to kind of the new paradigm of programming languages.
[2159.62 --> 2162.12]  Like there weren't, it's a cross-section of two things.
[2162.20 --> 2166.06]  First of all, the VXers, the virus riders, you know, they're aging out.
[2166.14 --> 2168.24]  There's a new generation of folks coming along.
[2168.24 --> 2178.44]  So you don't have as many people that like learned assembly in school and like were doing, were cracking software in Eastern Europe back in the day when they couldn't get their hands on legitimate software.
[2178.68 --> 2182.24]  Like that was the old school of VXers and virus riders.
[2182.24 --> 2195.24]  Now, I think this new generation is kind of kicking up and starting to get more involved and they are spending more time with Go and Rust and, you know, trying to learn these new paradigms.
[2195.36 --> 2199.40]  And it doesn't seem that many of them are going back to just learn hard assembly or C.
[2199.40 --> 2208.66]  So it's inevitable that we're going to see this sort of like increasingly popular and more accessible languages start to become more prevalent as far as malware goes.
[2209.20 --> 2209.28]  Yeah.
[2209.32 --> 2222.86]  It's very interesting when you think of the different languages and the different capabilities that we have and how that then turns into like when you come to reverse engineering, like I'm thinking defer statement.
[2222.86 --> 2236.60]  For example, in Go, where a function runs after this function exits, obviously there's something in the binary that's just normal looking code, I guess, or assembly that describes that in some way.
[2236.86 --> 2242.68]  Can you look at a binary and tell where something's using defer or there's concurrency or Go routines?
[2242.86 --> 2244.10]  It's a different return call.
[2244.68 --> 2244.98]  Do you remember?
[2245.24 --> 2246.10]  It's a defer return.
[2246.42 --> 2247.16]  I think it's what it's called.
[2247.34 --> 2251.48]  It's a function call on runtime that just has a pointer to the function that we'll call.
[2251.48 --> 2251.74]  Hmm.
[2251.94 --> 2253.02]  It's a lot easier.
[2253.38 --> 2256.78]  I would say it's easier when you're familiar with the paradigm, right?
[2256.86 --> 2263.58]  Like it's, it's, if Go has been as accessible as it was to me, it was, you know, working at Google for a short stint.
[2263.92 --> 2268.78]  One of my better friends there, mentor there, Mike Wysek is a huge fan of Go.
[2268.94 --> 2271.52]  And, you know, I walk into Google within the first two weeks.
[2271.52 --> 2274.28]  It's like, you know, here's, here's the Go programming language book.
[2274.34 --> 2275.16]  Like figure this out.
[2275.68 --> 2277.30]  I learned to love it.
[2277.30 --> 2285.36]  And then when it came time to reverse it, things made sense that otherwise might not have like channels and defer statement, things like that.
[2285.48 --> 2289.26]  It was easy to kind of map those concepts because they were already familiar to me.
[2289.26 --> 2303.48]  The biggest, sort of the steepest challenge getting into reverse engineering is usually training yourself to recognize what are C level constructs by staring at assembly.
[2303.48 --> 2312.56]  You're basically just trying to like get familiar with how different compilers are going to represent some C concept that might not be that complicated.
[2312.68 --> 2313.52]  Oh, it's a switch statement.
[2313.70 --> 2315.04]  But how does that look in assembly?
[2315.46 --> 2315.64]  Right.
[2315.72 --> 2317.72]  And sort of like learning to go back and forth.
[2317.72 --> 2329.96]  And it helps to have those concepts, which is why I say maybe Rust will get easier for folks that understand Rust to come in and, you know, write some scripts and write some tools.
[2330.18 --> 2333.14]  I don't find Rust very familiar right now.
[2333.22 --> 2336.52]  So when I try to reverse something in Rust, it's like being lost.
[2336.52 --> 2337.78]  Like you don't have any coordinates.
[2338.00 --> 2340.08]  You have thousands of functions with no names.
[2340.12 --> 2340.92]  You have no types.
[2341.04 --> 2343.04]  You have sometimes the strings are mangled.
[2343.04 --> 2346.54]  It's just you're dropped in the middle of a large binary with no map.
[2346.54 --> 2354.42]  So when you think of those features, and by the way, it's very interesting because I don't basically never look at the assembly that gets generated.
[2354.42 --> 2360.94]  So I kind of only really think of those features at the level of the language itself.
[2361.40 --> 2369.88]  It's very interesting to imagine because, of course, like they feel quite magical in some ways, like channels, when they work right, they work kind of brilliantly.
[2369.88 --> 2374.94]  And you sort of forget, I think, that there's just it's just doing boring things underneath.
[2374.94 --> 2382.04]  So but what about like when new language features come out into Go, like Go 118, we're going to get generics.
[2382.22 --> 2385.76]  Is that going to be a bit of a headache for you when that lands?
[2386.12 --> 2386.48]  Probably.
[2388.44 --> 2390.96]  The biggest question is going to be how many of the tooling will break.
[2391.36 --> 2397.28]  One of the problems we face is that we parse internal data structures that are not exported.
[2397.28 --> 2399.24]  So they changes all the time.
[2399.54 --> 2402.54]  I can't remember how many times the internal map structure have changed.
[2402.92 --> 2409.42]  And when you parsing that, you need to have the exact right structure that you read in the binary.
[2409.70 --> 2412.50]  Otherwise, your whole offset goes off afterwards.
[2412.70 --> 2415.94]  You know, you go off and read somewhere else and then you're lost.
[2416.70 --> 2419.66]  And it's not announced when things like that changes.
[2420.06 --> 2420.46]  Right.
[2420.46 --> 2426.14]  This is like the interface to those things stay the same, like the language is the same.
[2426.38 --> 2426.44]  Yeah.
[2426.54 --> 2431.58]  But of course, the compiler is free to really do whatever it needs to do.
[2432.04 --> 2442.68]  And this is one of the advantages really of using a language like Go is that people are doing work under the hood, making changes that we don't have to even think about.
[2443.06 --> 2445.26]  But of course, you do have to think about those things.
[2445.26 --> 2450.00]  But do you just not have the tooling tagged to each version of Go?
[2450.06 --> 2451.40]  Is that essentially what you end up with?
[2451.40 --> 2452.80]  You kind of can.
[2453.00 --> 2457.68]  And to some extent, we do just out of necessity in the way things have built up.
[2457.78 --> 2469.74]  It's more that no one is calling us up and saying, hey, you remember that magic header that you're relying on to figure out where the PCLN symbol table is?
[2469.84 --> 2470.42]  We changed it.
[2470.62 --> 2473.64]  Yeah, we changed it in 1.16, which they did.
[2473.64 --> 2475.20]  We changed it in 1.16.
[2475.32 --> 2475.86]  Good luck.
[2476.38 --> 2483.82]  You know, it's part of the very nature of reverse engineering that like you're kind of stealing bits of information out of the air.
[2484.34 --> 2487.98]  And there's nothing to say that that won't change the next time around.
[2488.02 --> 2489.48]  And there's usually good reasons for it.
[2489.50 --> 2489.62]  Right.
[2489.62 --> 2495.40]  Like if you figure out a more efficient way to get through a certain algorithm, of course, you're going to want to implement that.
[2495.40 --> 2500.88]  Nobody's sitting there thinking, well, how do we help the reverse engineers like sort of get their bearings again?
[2501.34 --> 2505.50]  It is sort of living on a series of heuristics that can and will change over time.
[2505.50 --> 2516.92]  And it's really hard to maintain the tooling and make it able to continue to do what it does for different versions, but also recognize the new things, new conventions.
[2517.18 --> 2522.92]  There are different variations across different compiler settings and different target platforms and so on.
[2522.92 --> 2527.18]  One of my most sort of like the bugs initially sort of stumped me.
[2528.14 --> 2533.08]  The Go 1.7 beta 1, the data structure.
[2533.30 --> 2538.70]  I know this because it's only one version that was released that has this data structure in this format.
[2539.24 --> 2542.98]  This data structure for the methods, the methods for types.
[2542.98 --> 2548.26]  There's a couple of fields that tells you the offset from where it would locate it.
[2548.94 --> 2555.74]  And in this version, the size of that int is a 32.
[2556.20 --> 2557.26]  I think it's an int 32.
[2557.70 --> 2559.62]  The beta 2 switches to a 16.
[2560.02 --> 2561.34]  And after that, it sort of changed.
[2561.48 --> 2565.72]  So there's one beta version where the size is completely different than any other version.
[2565.72 --> 2574.68]  And yes, I came across that in a malware that was compiled with a beta version and it threw off the complete, you know, just ran through it.
[2575.04 --> 2575.24]  Wow.
[2575.44 --> 2576.54]  That is so interesting.
[2576.66 --> 2577.10]  Is there not?
[2577.16 --> 2579.86]  Does the fact that Go is open source not help?
[2579.96 --> 2588.68]  I mean, could you not like literally build some tool that looks at the code and alerts you if something's committed and something's changed there?
[2588.80 --> 2590.58]  Anything you could do there?
[2590.58 --> 2599.08]  In theory, you could, in theory, but that's where you start to get into over-optimizing, right?
[2599.18 --> 2605.66]  Like we see a lot of Go malware now, but it's still not the majority of what we're dealing with.
[2605.66 --> 2625.04]  So you get into the situation where if Go were the ultimate malware writing language and we knew we were going to see Go malware indefinitely in its majority, then it's absolutely worth it to like maybe even go like kick up a startup and just dedicate yourself to reverse engineering Go.
[2625.26 --> 2634.48]  But these days, there's Russian threat actors that will just rewrite their code in a different language every other week in the hopes of evading detection.
[2634.48 --> 2642.88]  So there's a group called Cyberacy that first they wrote their malware in Delphi and then they ported it to Python and they ported it to Go.
[2643.00 --> 2643.92]  They ported it to Rust.
[2644.00 --> 2644.86]  They ported it to Nim.
[2645.10 --> 2645.26]  Yeah.
[2645.38 --> 2647.92]  They've done it in basically every other language.
[2648.12 --> 2650.00]  And for them, it's just kind of a joke, right?
[2650.02 --> 2653.10]  Like you just want to get your first stage loader by undetected.
[2653.60 --> 2660.16]  For us, it's like if you sat and tried to build tooling for every possible variation, like you're just never going to get ahead of the curve, right?
[2660.16 --> 2660.60]  Yeah.
[2661.32 --> 2665.74]  Some companies do that as well, by the way, have just to keep rewriting things in different languages and stuff.
[2665.84 --> 2668.88]  They're not trying to evade anyone apart from themselves.
[2669.60 --> 2670.88]  But yeah.
[2670.88 --> 2692.48]  This episode is brought to you by Honeycomb.
[2692.48 --> 2699.64]  Honeycomb is built on the belief that there's a more efficient way to understand exactly what is happening in production right now.
[2699.94 --> 2703.74]  When production is running slow, it's hard to know exactly where problems originate.
[2704.04 --> 2708.06]  Is it your application code, your users, or the underlying systems?
[2708.42 --> 2712.76]  Teams who don't use Honeycomb scroll through endless dashboards guessing at what they mean.
[2712.76 --> 2719.52]  They deal with alert floods, guessing which ones matter, and go from tool to tool to tool, guessing at how the puzzle pieces all fit together.
[2719.78 --> 2723.94]  It's this context switching and tool sprawl that are slowly killing your teams and your business.
[2724.34 --> 2729.50]  With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business.
[2729.78 --> 2730.18]  Production.
[2730.62 --> 2739.04]  Honeycomb quickly shows you the correct source of issues, discover hidden problems, even in the most complex stacks, understand why you're at Feel Slow to own some users.
[2739.46 --> 2741.90]  With Honeycomb, you guess less and know more.
[2741.90 --> 2746.82]  Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[2747.08 --> 2749.82]  Again, honeycomb.io slash changelog.
[2750.16 --> 2754.40]  And by our friends at Linode, cut your cloud bills in half with Linode's Linux virtual machines.
[2754.70 --> 2757.84]  Develop, deploy, and scale your modern app faster and easier.
[2758.22 --> 2764.98]  Whether you're developing a personal project or managing larger workloads, you deserve simple, affordable, and accessible cloud computing solutions.
[2765.50 --> 2769.52]  You can get started today for free with the huddles and credit at linode.com slash go time.
[2769.52 --> 2775.46]  Linode has data centers all around the world with the same simple and consistent pricing regardless of location.
[2775.90 --> 2778.80]  Choose a data center that makes the most sense to you, close to you, whatever.
[2779.22 --> 2784.02]  You have access to 24-7, 365 human support with no tiers or handoffs.
[2784.24 --> 2788.10]  Regardless of your plan size, you can choose shared or dedicated compute instances.
[2788.10 --> 2793.76]  Or you can use that credit on S3-compatible object storage, managed Kubernetes, and so much more.
[2794.12 --> 2796.38]  If it runs on Linux, it runs on Linode.
[2796.70 --> 2798.50]  Head to linode.com slash go time.
[2798.62 --> 2800.66]  Again, click on the free account button.
[2801.02 --> 2801.72]  Get that credit.
[2801.84 --> 2802.60]  Get started today.
[2803.06 --> 2805.56]  Once again, linode.com slash go time.
[2805.56 --> 2824.36]  You mentioned that there's an increasing number of malware written in Go.
[2824.36 --> 2833.28]  Is there some special malware that you liked something that they did because they utilized a special feature in Go and did something interesting?
[2833.28 --> 2835.08]  I've seen a lot of them.
[2835.40 --> 2843.32]  The majority of the stuff that I see, I've seen, is sort of like something that is sort of either designed to load shell code.
[2843.46 --> 2846.84]  So it loads another malware or it sort of encrypts stuff.
[2847.36 --> 2851.22]  It's a lot of stuff that's targeting Linux and servers and stuff like that.
[2851.22 --> 2854.30]  It's used to drop miners and stuff like that.
[2854.30 --> 2863.60]  One of the more interesting ones I've seen, if you're familiar with the IPFS project, was an interplanetary file system.
[2863.98 --> 2868.88]  So it's a startup that tries to do like distributed, they distribute the internet.
[2869.64 --> 2871.88]  Like IPFS.io is a website.
[2871.88 --> 2879.36]  So they've released their peer-to-peer library for Go and found a botnet.
[2879.46 --> 2880.02]  They used it.
[2880.22 --> 2886.26]  So the botnet sits on top of this, the IPFS botnet, so to speak.
[2886.34 --> 2887.98]  It's like their peer-to-peer network.
[2890.06 --> 2894.90]  And mainly it was using it then eventually to sell a proxy service.
[2894.90 --> 2902.72]  But I think the interesting part there is sort of laying a botnet on top of a legitimate peer-to-peer network.
[2903.26 --> 2907.12]  I thought IPFS was an internet protocol file system.
[2907.32 --> 2908.56]  But you're right, it's interplanetary.
[2908.72 --> 2910.90]  How many planets are they on at the moment?
[2910.90 --> 2924.88]  I think it's sort of interesting to realize that the standard proficiency of Go developers probably listening to this podcast is pound for pound much higher.
[2924.90 --> 2928.50]  than what we tend to see for Go malware devs.
[2929.04 --> 2931.22]  I think it's still, like I said, it's still a new paradigm.
[2932.06 --> 2938.72]  In some cases, you get the sense that the authors are just not that familiar with Go yet.
[2938.82 --> 2939.54]  Like they're trying.
[2940.16 --> 2944.48]  Especially like, you know, the cybersecurity side, like I said, you know, they're trying to master a bunch of different languages.
[2944.72 --> 2945.98]  And obviously they never do.
[2946.44 --> 2952.22]  But you also get interesting situations like a lot of ransomware is trying to embrace Go.
[2952.22 --> 2957.42]  Because concurrency is a fantastic feature for speeding up, you know, encrypting a bunch of files.
[2957.84 --> 2959.50]  And also the encryption libraries are good.
[2959.54 --> 2959.78]  Right.
[2959.96 --> 2960.74]  And easy to use.
[2961.02 --> 2963.52]  So you've got good, strong encryption, crypto libraries.
[2963.66 --> 2969.26]  You're not going to accidentally, you're not going to roll your own crypto and then somebody can recover the keys or whatever.
[2969.62 --> 2971.56]  And concurrency is relatively easy.
[2971.56 --> 2977.76]  So you see them starting to play with channels and you see them trying to kind of build these lists on the fly and trying to do all this quick crypto.
[2978.36 --> 2987.36]  But then they'll do other stupid things like they interface with Windows using OS specific libraries off of GitHub.
[2987.64 --> 2992.30]  So it's like, well, you spent all this effort and you went for an easy to cross compile language.
[2992.30 --> 2994.70]  And now you've made it impossible to cross compile.
[2995.46 --> 2998.06]  And you're like, OK, well, thankfully, you're not that good.
[2998.06 --> 3000.44]  But there's kind of a missed opportunity sense to it.
[3000.52 --> 3000.62]  Right.
[3000.64 --> 3006.32]  Like if you were if you were a slightly better dev, like, you know, your revenue stream would be much more expanded.
[3007.96 --> 3008.88]  It's so difficult.
[3009.06 --> 3014.72]  How do you not antagonize people and make them like by saying things like this, even having this conversation?
[3014.92 --> 3015.40]  Oh, we do.
[3015.74 --> 3016.14]  Oh, you do.
[3016.14 --> 3016.54]  Yeah.
[3017.44 --> 3023.94]  InfoSec Twitter is just, you know, a cesspool of hot takes and insults and, you know, people sort of going at each other.
[3024.08 --> 3027.82]  It's a great community in some ways and in others it can be very spiteful.
[3028.84 --> 3030.18]  Doesn't sound like Twitter.
[3030.98 --> 3031.46]  Right.
[3031.72 --> 3034.04]  It's modern community.
[3034.40 --> 3034.58]  Yeah.
[3034.90 --> 3037.46]  Modern community with anonymous accounts.
[3037.76 --> 3037.92]  Yeah.
[3037.96 --> 3038.40]  There you go.
[3038.94 --> 3039.38]  Civility.
[3039.62 --> 3041.22]  Your name comes up as Jagess.
[3041.52 --> 3041.72]  Right.
[3041.92 --> 3042.38]  On this.
[3042.80 --> 3042.88]  So.
[3043.88 --> 3045.22]  But you've been so polite.
[3045.22 --> 3047.10]  Like, I'm even being helpful with that.
[3047.16 --> 3047.30]  Right.
[3047.32 --> 3051.06]  I don't want you to have to struggle through my two double barrel names.
[3051.26 --> 3052.04]  I see.
[3052.16 --> 3053.06]  Thank you so much.
[3053.14 --> 3056.20]  I wish Natalie Pistinovich had the same sort of.
[3056.42 --> 3060.14]  We might have talked about this when we started without you.
[3060.52 --> 3062.48]  Oh, well, that was before the show, wasn't it?
[3062.80 --> 3063.08]  Yes.
[3063.42 --> 3063.70]  Okay.
[3064.78 --> 3065.62]  Say it again then.
[3067.14 --> 3067.58]  Sorry.
[3067.84 --> 3068.80]  You talked about my name.
[3068.80 --> 3070.50]  Oh, I am interested now.
[3070.60 --> 3071.98]  We've mentioned it, what your name is.
[3072.30 --> 3074.94]  But if you'd rather not, that's totally fine as well.
[3074.94 --> 3075.54]  No, it's fine.
[3075.64 --> 3077.42]  My name is Juan Andres Guerrero Saade.
[3077.86 --> 3080.56]  I just figure it's a lot easier for folks to just.
[3080.70 --> 3082.28]  That is amazing, by the way.
[3082.58 --> 3083.86]  Can you just do it one more time?
[3084.64 --> 3087.38]  Juan Andres Guerrero Saade.
[3087.58 --> 3087.78]  Oh.
[3088.30 --> 3088.70]  Again.
[3088.80 --> 3089.06]  Amazing.
[3089.30 --> 3090.06]  Jags is fine.
[3090.24 --> 3090.94]  Juan is fine.
[3091.72 --> 3093.02]  No one's got the time for it.
[3093.02 --> 3093.16]  Yeah.
[3093.54 --> 3095.24]  I've got my new password sorted anyway.
[3095.34 --> 3095.86]  There you go.
[3095.94 --> 3096.08]  Right.
[3096.08 --> 3096.30]  Yeah.
[3099.18 --> 3100.16]  No one's going to get that.
[3100.28 --> 3101.24]  I wouldn't even try.
[3101.44 --> 3104.14]  I knew I would somehow mispronounce something.
[3104.14 --> 3106.20]  That is such an interesting conversation.
[3106.40 --> 3110.92]  That's like all the things that you always look at when you think of Goal, like cross-compilation.
[3111.10 --> 3111.58]  Oh, wonderful.
[3111.80 --> 3116.28]  And then suddenly when you said that this is so useful for hackers, that was completely mind-blowing for me.
[3116.44 --> 3117.28]  You see a lot.
[3117.40 --> 3130.18]  I mean, there's, especially when you're targeting like Unix systems, you know, if you found one in that's for x86, you're guaranteed to kind of almost find ARM and MIPS and all the other ones eventually too.
[3130.18 --> 3130.70]  Yeah.
[3130.76 --> 3134.72]  I think the big test is, you know, are you going to see a whole lot of Sego in it?
[3135.12 --> 3139.26]  And if not, then chances are you're going to be comfortable sort of porting back and forth.
[3139.50 --> 3139.58]  Yeah.
[3139.98 --> 3149.28]  I will say this, and, you know, I try not to talk about this publicly too much, but the malware dev community in Go is not that good.
[3149.28 --> 3151.70]  But the red teaming community is.
[3151.96 --> 3161.90]  So it's kind of surprising that they haven't, the actual bad guys haven't just been picking up the tooling that the pretend bad guys are building.
[3162.06 --> 3162.54]  Right?
[3162.60 --> 3165.90]  Like those dudes actually understand Go fairly well.
[3166.14 --> 3170.96]  They're doing quite a bit of trickery that, you know, I don't want to give anybody ideas, but they're developing good stuff.
[3170.96 --> 3178.14]  But the actual black hats haven't taken the time to kind of study the ecosystem and see what's out there to our benefit.
[3178.34 --> 3178.46]  Right?
[3178.54 --> 3178.98]  Thank you.
[3179.06 --> 3180.74]  It's not like we really want them to get that much better.
[3181.14 --> 3181.28]  Yeah.
[3181.72 --> 3185.18]  I don't know how many of our audience falls into that description.
[3185.58 --> 3189.42]  Like, I can't imagine people like hackers.
[3189.74 --> 3194.70]  I can't imagine like a cool hacker person popping a podcast on.
[3195.04 --> 3195.72]  Can you?
[3196.48 --> 3197.34]  Maybe they do.
[3197.56 --> 3198.38]  Well, you're welcome to live.
[3198.44 --> 3198.82]  Welcome.
[3199.04 --> 3199.74]  Welcome to go to.
[3199.74 --> 3200.56]  You never know.
[3200.70 --> 3200.86]  Right?
[3200.96 --> 3202.06]  Like, well, that's the other thing.
[3202.12 --> 3207.00]  Are they, are these like full-time hackers or are we talking about folks moonlighting?
[3207.04 --> 3207.20]  Right?
[3207.22 --> 3216.50]  Like every once in a while you get some interesting tidbit where it's like, this is a Kubernetes dev, someone who like has a full on like real dev job.
[3216.50 --> 3220.12]  And then they just so happen to decide to try something.
[3220.28 --> 3223.18]  Like, I think it's the, the psychology of white collar crime.
[3223.18 --> 3223.42]  Right?
[3223.44 --> 3227.60]  Like you think you can get away with things because you're, you're clever and it doesn't feel like real crime.
[3227.88 --> 3228.84]  And it happens.
[3228.84 --> 3230.84]  It happens sometimes if folks think that.
[3230.96 --> 3234.48]  That they dip their toe in that it's not really going to come back to bite them.
[3234.68 --> 3235.08]  And yeah.
[3235.32 --> 3236.14]  Sometimes it doesn't.
[3236.22 --> 3237.00]  And sometimes it does.
[3237.00 --> 3241.54]  Sometimes they leave breadcrumbs and you find, you'll find their LinkedIn profile.
[3241.68 --> 3242.56]  You go, great.
[3242.84 --> 3243.36]  Hi friend.
[3244.96 --> 3245.40]  Interesting.
[3245.40 --> 3246.46]  It happens.
[3246.46 --> 3246.86]  Yep.
[3246.86 --> 3248.80]  We'll post a link to those in the show notes.
[3249.20 --> 3249.40]  Right.
[3250.12 --> 3251.48]  One bit of advice.
[3251.62 --> 3270.48]  If you decide to go down the malware route with Go, if you have great coding practices and you are using Git to write your malware incrementally with nice version control, maybe don't leave your name in the, like, maybe don't have it all built under your actual name in like your own GitHub repo.
[3270.48 --> 3270.92]  Yeah.
[3270.92 --> 3282.44]  Like, it's amazing how much people don't realize that like standard strong coding practices are also in many ways kind of violate that principle of trying to anonymize this thing.
[3282.54 --> 3290.88]  So you'll get some like really clever malware, but you're like, man, it's the same handle for this GitHub repo as this, you know, as the account you've been using for the past 10 years.
[3290.88 --> 3297.38]  I'm reading like your live journal, like trying to understand all your feelings because I ran into one of your samples.
[3297.56 --> 3298.14]  Oh, wow.
[3298.24 --> 3312.78]  One of my favorite finds is the path where the project was located was slash users slash first name of the person slash go project slash source slash key base slash a key base team.
[3312.78 --> 3316.74]  And like, God, just one line got everything.
[3317.38 --> 3317.70]  Wow.
[3318.44 --> 3319.74]  It's nice when they're organized.
[3319.96 --> 3320.10]  Yeah.
[3320.20 --> 3320.50]  Yes.
[3321.26 --> 3327.00]  Good structure of the source code and things like that, but you may not want to keep that in the binary.
[3327.52 --> 3328.72]  Are we helping them really?
[3328.88 --> 3333.46]  Do you think by having these conversations in public, it does help?
[3333.60 --> 3334.36]  It's pretty obvious.
[3334.70 --> 3337.30]  Like those kind of things kind of get published.
[3337.80 --> 3338.72]  I mean, yeah.
[3338.80 --> 3340.80]  Obviously somebody on Reddit already said that.
[3340.80 --> 3345.00]  The info is out there and it will be out there and folks are going to figure stuff out.
[3345.24 --> 3346.16]  I'll be honest with you.
[3346.18 --> 3350.86]  I'm not that stressed about like sort of two bit criminals figuring out how to better use Go.
[3351.40 --> 3364.78]  I am very curious for when we're going to see the nation state sponsored attackers start to pick up and productize Go and Rust for malware properly.
[3364.78 --> 3365.34]  Right.
[3365.42 --> 3374.54]  Because like the, you know, C++ is usually what we see, like, let's say with US or Five Eyes malware, like the best stuff you can find tends to be C++.
[3374.54 --> 3377.90]  Plus very highly quality assured code.
[3378.02 --> 3383.36]  You can tell that there's a certain amount of infrastructure and tooling that's built around producing these things.
[3383.36 --> 3400.28]  And what you're dealing with is layers upon layers of really good engineering that have gone into producing implants that are hard to track, that, you know, might do a lot of those relocations that are having custom packers that have encrypted payloads, like all the stuff that's going into it.
[3400.28 --> 3405.88]  And that's all productized in a way that's sort of repeatable and avoids mistakes like what we're talking about.
[3406.16 --> 3408.98]  So far, that's not the malware that we're seeing.
[3409.28 --> 3409.50]  Right.
[3409.58 --> 3413.72]  Like it's still kind of the early days of people going, oh, how do we play with this?
[3413.92 --> 3415.18]  And maybe it's out there.
[3415.18 --> 3415.44]  Right.
[3415.46 --> 3417.56]  Like maybe we just haven't found it yet.
[3418.08 --> 3423.36]  But I'm kind of on the lookout to say, you know, when are we going to see some government quality?
[3423.68 --> 3429.24]  You know, Raytheon wrote this kind of malware versus, you know, somebody just sort of moonlighting.
[3429.24 --> 3431.14]  This opens so many questions.
[3431.46 --> 3436.16]  Like, do expect the next episode about AI generated malware.
[3436.46 --> 3437.02]  Right.
[3437.26 --> 3444.04]  There's been a pickup of like nation states using Go, especially the last year and a half.
[3444.36 --> 3446.18]  Prior to that, it was really rare.
[3446.56 --> 3446.68]  Yeah.
[3446.80 --> 3448.38]  Do you know which states they are?
[3448.62 --> 3450.34]  Definitely the Russians and the Chinese.
[3450.60 --> 3450.72]  Yeah.
[3450.72 --> 3453.94]  I mean, there's a proliferation of groups for both countries.
[3454.14 --> 3457.68]  And our attribution is always, you know, take it with a grain of salt.
[3457.68 --> 3474.42]  So something that happened without getting too inside baseball and like threat intelligence, but something that happened over the past couple of years is particularly on the Russian side, there was so much attention paid to these different Russian state sponsored groups, particularly with the summer of election hacks in 2016.
[3474.42 --> 3483.16]  And everything that followed from there, they got so much attention that these groups kind of were forced to do a lot of retooling, like major, major retooling and reorganizing.
[3483.16 --> 3489.50]  And they dumped most of the toolkits that we were used to using, a lot of which were written in C and C++.
[3490.06 --> 3497.34]  And interestingly, now we're seeing, you know, Russian state sponsored groups who like Go and who, you know, actually rely on Kubernetes.
[3497.78 --> 3501.48]  And, you know, you see malware that now includes like gRPC.
[3501.80 --> 3506.46]  And you're like, oh, my God, like you guys are kind of getting you're getting a little more professional with this.
[3506.46 --> 3507.90]  So it's interesting.
[3508.12 --> 3509.16]  It's actually cool.
[3509.60 --> 3512.86]  At the same time, it's daunting, right?
[3512.96 --> 3516.22]  Like the kind of resources that start to go into that are quite daunting.
[3516.68 --> 3516.88]  Yeah.
[3517.46 --> 3519.04]  Is there any written in JavaScript?
[3519.62 --> 3520.18]  Yeah, of course.
[3520.38 --> 3520.50]  Yeah.
[3520.70 --> 3527.96]  A lot of the malware on the web, like the crypto miners and even landing pages, like JavaScript is really useful.
[3527.96 --> 3537.36]  When you think about an attack chain, if somebody is going to use an exploit or they're using something very specialized, they actually really need to know a lot about you before they can use that.
[3537.52 --> 3537.62]  Right.
[3537.66 --> 3547.12]  Like I need to know what Matt's computer is running, what browser, what, you know, what sort of software stack I'm dealing with before I can try any kind of fancy exploitation.
[3547.82 --> 3551.34]  And JavaScript tends to be the go to first stage.
[3551.34 --> 3553.10]  Like let's land here.
[3553.10 --> 3561.08]  Maybe we don't even serve you anything, but we take a moment to profile your system and then the next step will be giving you something very specialized.
[3561.38 --> 3565.48]  So like JavaScript tends to fuel a lot of the early stages of malware ops.
[3565.70 --> 3565.80]  Yeah.
[3565.86 --> 3569.28]  I remember the love bug, which is probably one of my favorites.
[3569.80 --> 3570.60]  It was VBScript.
[3570.98 --> 3571.12]  Yeah.
[3571.52 --> 3575.28]  Microsoft has, was it JScript, which is kind of a flavor of JavaScript.
[3575.86 --> 3578.02]  So you have malware written data.
[3578.16 --> 3578.28]  Yeah.
[3578.30 --> 3580.14]  But that runs on the system properly, doesn't it?
[3580.18 --> 3581.46]  That's not just in the browser, that one.
[3581.54 --> 3581.62]  Yeah.
[3581.62 --> 3583.84]  VBScript, the love bug was VBScript.
[3584.02 --> 3591.64]  I remember this was where it would use the Outlook automation APIs essentially to email itself to all of your contacts.
[3591.90 --> 3593.72]  And then I think that's all it was doing actually.
[3593.88 --> 3596.22]  And then it sends an email saying, oh, I love you.
[3596.34 --> 3597.06]  Check out this file.
[3597.14 --> 3601.22]  And it was iloveyou.vb or something, which people would just happily double click.
[3601.42 --> 3605.78]  And it would then send it, you know, it was sort of this literally virus kind of.
[3605.78 --> 3612.26]  I mean, if you can, if you would really want to write a malware in JavaScript, you could just package this with Node.js.
[3612.44 --> 3615.64]  It has a bunch of packages that will spit out a single binary.
[3615.86 --> 3616.50]  You can send it.
[3616.50 --> 3623.02]  But if you're okay with the user downloading 20 to 40 megabyte file and run it, you know, it works.
[3623.38 --> 3623.58]  Yeah.
[3624.00 --> 3626.98]  You get V8 and everything else.
[3627.22 --> 3627.50]  Yeah.
[3627.90 --> 3628.44]  Mind-blowing.
[3628.44 --> 3631.08]  This is such a fascinating episode.
[3631.36 --> 3636.34]  Really, thank you for sharing all the insights with the community and hopefully inspiring only the right people.
[3636.56 --> 3640.92]  The other side of this, right, is Gophers are by and large great devs.
[3641.36 --> 3648.04]  And our space, the larger InfoSec community could really use much better engineers getting involved.
[3648.40 --> 3657.28]  Like we, reversers and threat hunters, we have a certain set of skills, but we don't usually come from strong engineering backgrounds.
[3657.28 --> 3660.28]  Like some of us do, but some of us don't.
[3660.42 --> 3665.50]  Like myself included, we come from international relations space, philosophy, physics, whatever.
[3665.64 --> 3670.12]  If you just have a mind for like solving puzzles, you kind of get into it and learn to reverse engineer.
[3670.44 --> 3674.96]  And it tends to mean that a lot of our tooling is just like cobbled together Python scripts.
[3674.96 --> 3687.24]  So if this serves to do anything, hopefully not inspire more malware authors, but rather to say, you know, if more Go developers, robust Go developers want to get into the security space.
[3687.24 --> 3698.90]  There's a lot of opportunity for startups, a lot of opportunity for just coming in and kind of revolutionizing a whole software stack that is horribly aged and in disrepair.
[3699.14 --> 3705.58]  And that a lot of the well-being of the internet and the general ecosystem sort of relies on.
[3706.06 --> 3711.52]  So it would be great to get more Gophers kind of coming our way instead of, I don't know, working on ads or whatever it is Google.
[3711.52 --> 3714.84]  And where should they go to if they are interested?
[3715.40 --> 3716.78]  So a couple of different places.
[3716.94 --> 3727.44]  If you're particularly in the trying to get into like the threat intel side of the house, I know Ninja Jobs is a good place to like kind of try to find jobs in the security space in particular.
[3728.30 --> 3733.06]  Honestly, if you have the right mind for it, you might really just want to kick off a startup.
[3733.34 --> 3738.28]  Like not to make it sound so simple, but a lot of the tooling that we rely on is just old school.
[3738.40 --> 3739.42]  It's way too old school.
[3739.42 --> 3742.56]  So I think security is the land of opportunity.
[3742.72 --> 3745.06]  There's a ton of investment and a ton of need.
[3745.74 --> 3748.66]  And none of us really seem to know what the solution is.
[3748.92 --> 3760.36]  So even if you make incremental improvements for things that people really need, like understanding DNS, understand even like, you know, nobody wants to touch operational transforms ever.
[3760.58 --> 3768.06]  Like Google Drive, Google Docs might be the only operational transforms project anyone ever wants to take on and never again.
[3768.06 --> 3772.48]  But like that means we have no collaborative platforms to use and things like that.
[3772.74 --> 3774.94]  Would open source work for that kind of tooling?
[3775.14 --> 3775.94]  Would that be okay?
[3775.94 --> 3779.26]  Or would that give the hackers an advantage?
[3779.80 --> 3780.72]  I think it's okay.
[3780.90 --> 3785.72]  I mean, we rely on things like a lot of security detection relies on OS query, for example.
[3785.72 --> 3786.96]  And that's open source.
[3786.96 --> 3791.38]  And you've got a lot of open source stuff that goes into our stack.
[3791.48 --> 3796.22]  And if anything, you have a healthy services industry that's risen around it, right?
[3796.30 --> 3803.70]  Like OS query is free, but a lot of people will pay other companies like Uptix and so on to set that stack up for them and maintain it.
[3803.70 --> 3808.48]  So I'm sort of speaking more to the business side of the house, but it's just to say, you know, there's incentives.
[3808.66 --> 3810.02]  Like come our way, come work with us.
[3810.22 --> 3811.16]  Yeah, definitely.
[3811.78 --> 3815.18]  That sounds like a popular opinion.
[3816.68 --> 3824.58]  It may seem like magic to some of this stuff, but a lot of it is just fundamentals of computer science in the end.
[3824.58 --> 3832.74]  You know, it's kind of take back to if you took, you know, computer science in school and as Jax was talking about, you know, DNS and stuff like that.
[3833.78 --> 3840.66]  I've looked at a lot of RFCs in my days and I'm not a developer, but it's all about, you know, looking and understanding how protocols work.
[3840.98 --> 3846.02]  There's a lot of stuff sort of shared between developers and what we do.
[3846.02 --> 3856.24]  Great tips. Thank you for this new perspective and for like a sneak peek into this wonderful industry and for also the tips for those who do want to jump into the water.
[3857.08 --> 3860.78]  And I guess the last question to you would be, are you ready for unpopular opinions?
[3862.36 --> 3862.84]  Sure.
[3868.22 --> 3870.94]  I actually think she'd probably leave.
[3876.02 --> 3882.94]  I heard you have two.
[3883.36 --> 3888.10]  Yeah, I'm trying to pick which one's worse, like which one is going to be more incendiary to this crowd.
[3889.78 --> 3890.90]  We'll test them both.
[3891.04 --> 3892.36]  So please feel free.
[3892.72 --> 3893.96]  Particularly this crowd.
[3894.62 --> 3903.42]  I actually think that software developers might have some of the worst security posture of all like internet users.
[3903.86 --> 3904.32]  Really?
[3904.32 --> 3914.40]  Nobody likes that idea, particularly like any of the really persnickety Linux devs who think like, oh, they've got their stuff like locked down.
[3914.60 --> 3917.44]  But none of them run any kind of endpoint security.
[3918.30 --> 3922.40]  Nobody believes in like any security solutions working on that space.
[3922.40 --> 3934.36]  And we tend to use a lot of shoddy package managers that just shove code into our environments all day long that isn't audited.
[3934.46 --> 3935.72]  Nobody knows what's going in there.
[3936.08 --> 3938.58]  There's a lot of like name typo squatting for packages.
[3938.58 --> 3948.02]  So, you know, brew and NPM and pip, like all these things are actually quite scary mechanisms that we all rely on that are being targeted.
[3948.02 --> 3956.22]  And we don't really realize that sort of like the substrate of what software developers tend to rely on is actually quite porous.
[3956.54 --> 3965.10]  That's so interesting because you genuinely would not think that you think most software developers at least have an idea of security.
[3965.10 --> 3968.12]  And, you know, they'll use one password and things like this.
[3968.42 --> 3971.42]  But yeah, I mean, that's very interesting.
[3971.70 --> 3971.86]  Sorry.
[3973.36 --> 3974.20]  Sorry, guys.
[3974.32 --> 3975.10]  That one hit deep.
[3975.56 --> 3975.80]  Yeah.
[3976.80 --> 3977.72]  It burns.
[3978.28 --> 3979.60]  Which would you say are better though?
[3979.70 --> 3981.10]  Software developers or grandmothers?
[3981.10 --> 3981.72]  Grandmothers.
[3982.32 --> 3984.20]  If you had to pick, what would you do?
[3984.48 --> 3986.66]  It just depends on the effects, right?
[3986.72 --> 3990.28]  Like it's easy to look down on the grandmas.
[3991.36 --> 3992.14]  Because they're little?
[3992.56 --> 3998.54]  No, you know, because it's like, well, you know, you're talking about a different generation and, you know, they're not necessarily the most savvy.
[3998.54 --> 3999.42]  And it's easy.
[3999.60 --> 4001.66]  It might be easier to kind of scam these folks.
[4001.74 --> 4002.72]  And a lot of that happens.
[4003.32 --> 4008.66]  But I think that the difference there is they tend to be very casual Internet users, right?
[4008.66 --> 4015.30]  So at most what you're defending is a few passwords and maybe some pictures of your family and things that are emotionally impactful.
[4015.60 --> 4019.12]  But that aren't that important in the grand scheme of things.
[4019.38 --> 4025.02]  Whereas like software devs, like sure, it might be easier to scam a software dev or social engineer them.
[4025.02 --> 4030.66]  But if you do get on their box, they have like SSH keys for all these different services.
[4030.66 --> 4037.30]  And they've got like full privileges for like this whole source code repo that an entire company relies on.
[4037.30 --> 4041.42]  So the impact tends to be drastically different.
[4041.98 --> 4044.34]  I'm pleased I said that silly comment now.
[4044.54 --> 4045.52]  That was very interesting.
[4046.52 --> 4048.44]  Got to defend the grandmothers here.
[4048.72 --> 4048.84]  Yeah.
[4049.10 --> 4051.18]  Note to self, say more silly things.
[4052.14 --> 4053.78]  Yoakim, did you have an unpopular opinion?
[4054.54 --> 4054.96]  Yeah.
[4055.70 --> 4058.94]  I'm just going to hit a little bit on the community that's writing Slack.
[4059.28 --> 4059.82]  Get them.
[4059.82 --> 4060.26]  Yeah.
[4061.32 --> 4069.58]  I don't think that a community, like an open source community should be hanging in a commercial product.
[4069.76 --> 4074.10]  And instead should embrace sort of like the open source projects that are around that are similar.
[4075.06 --> 4076.20]  That's a very good point.
[4076.54 --> 4077.68]  Do you want to elaborate a bit more?
[4077.98 --> 4078.58]  Do I need to?
[4079.26 --> 4080.50]  Because it's free to use.
[4080.50 --> 4080.90]  Yes.
[4081.30 --> 4083.12]  It's free to use, but it also is.
[4083.68 --> 4090.00]  You do end up in that sort of like the lock in kind of scenario that you are dependent on a commercial entity.
[4090.68 --> 4091.78]  Sorry, just to interrupt you there.
[4091.84 --> 4093.22]  We'll be back after these messages.
[4093.74 --> 4095.28]  Sorry, we just didn't need to add a break.
[4095.44 --> 4096.06]  What were you saying?
[4097.46 --> 4103.42]  And especially now, I mean, there's some really good open source projects just trying to kind of break that apart.
[4103.42 --> 4108.76]  I mean, Matrix is a really nice thing in the sense of that it is decentralized and they can go away.
[4109.26 --> 4110.94]  It doesn't take the community with it.
[4111.10 --> 4111.18]  Yeah.
[4111.20 --> 4115.52]  But the problem with Matrix is you have to have that thing installed in your skull to plug it in.
[4115.66 --> 4115.82]  Yeah.
[4115.96 --> 4117.84]  And a lot of people are against that.
[4118.10 --> 4120.48]  I had it done very early when it was still floppy disks.
[4120.80 --> 4122.44]  That's a very early adopter.
[4122.86 --> 4123.26]  Yeah.
[4123.36 --> 4124.44]  Which I regret now.
[4124.82 --> 4126.16]  But at the time it was.
[4126.44 --> 4128.28]  But it does teach you Kung Fu pretty quickly though.
[4128.78 --> 4128.98]  Yeah.
[4129.06 --> 4131.24]  Well, that comes on eight floppy disks.
[4131.24 --> 4132.44]  So it does take a bit of time.
[4132.44 --> 4135.22]  And it's quite difficult to reach around to do it.
[4135.32 --> 4138.36]  You need a friend to help Morpheus or whoever, Trinity.
[4138.94 --> 4141.18]  But no, that is a very good point actually.
[4141.46 --> 4145.98]  And yeah, that one will be very interesting to find out if that is unpopular actually.
[4146.38 --> 4150.42]  We test these of course on Twitter, another commercial platform,
[4150.94 --> 4155.64]  by doing a Twitter poll and asking people whether these are indeed unpopular or not.
[4155.72 --> 4156.60]  So we'll find out.
[4156.60 --> 4162.00]  I guess that community just isn't quite so cypherpunk as before, right?
[4162.00 --> 4166.00]  Like if you think about most common software development environments,
[4166.00 --> 4169.86]  like you are saving all your stuff on a Microsoft-owned product.
[4169.86 --> 4172.58]  You're looking for your new job on a Microsoft-owned product.
[4172.58 --> 4179.72]  You're communicating about it on like Slack and putting all your stuff up in like Google Docs.
[4179.72 --> 4187.22]  Like you're basically trusting like the biggest corporations on earth to fuel and support your newfound endeavors.
[4187.58 --> 4192.86]  It's just a different, a very different community than what it might have been in like the 90s, right?
[4193.10 --> 4193.38]  Yeah.
[4193.80 --> 4194.26]  Yeah.
[4194.44 --> 4195.34]  That is very true.
[4196.50 --> 4198.98]  Did you have another unpopular opinion though?
[4199.20 --> 4200.12]  You mentioned you had two.
[4200.12 --> 4200.86]  I do.
[4200.96 --> 4208.02]  I think it's more incendiary to especially the European audiences than it is to sort of the Go community in particular.
[4208.26 --> 4210.38]  Is it just going to be like America's great?
[4210.74 --> 4211.62]  America's the best.
[4212.10 --> 4212.20]  Yeah.
[4212.42 --> 4212.56]  Yeah.
[4212.68 --> 4213.18]  USA.
[4213.52 --> 4214.58]  That's your unpopular opinion.
[4214.66 --> 4215.42]  Full jingoism.
[4215.62 --> 4216.64]  USA number one.
[4216.90 --> 4222.32]  No, it's actually something really that, you know, we're quite touchy about on the security space, which is GDPR.
[4222.32 --> 4225.80]  So I don't know how familiar folks are with GDPR.
[4225.90 --> 4233.80]  I imagine anybody who's, anybody who's handling any kind of like PII is having a sort of nightmare go with GDPR.
[4234.00 --> 4241.02]  But what's likely to be a very unpopular opinion is that GDPR is just feel good security posturing.
[4241.28 --> 4249.06]  Like it has next to no genuine value as a stance other than to make people feel warm and fuzzy.
[4249.36 --> 4251.42]  It's a nightmare for folks to maintain.
[4251.42 --> 4253.28]  It's impossible to be compliant.
[4253.76 --> 4261.50]  And on the security space, it's actually made it really hard to maintain really important telemetry that we tend to rely on.
[4261.68 --> 4264.34]  So, yeah, I'm very opinionated about GDPR.
[4264.54 --> 4265.12]  Oh, wow.
[4265.22 --> 4265.38]  Yeah.
[4265.42 --> 4267.40]  You just said you lost who is information.
[4267.68 --> 4270.08]  I am upset that I lost who is information.
[4270.72 --> 4274.86]  It's like the whole argument was like, oh, we're going to save people from spam.
[4274.96 --> 4277.10]  It's like they're not saving us from spam at all.
[4277.20 --> 4279.48]  And now I can't tell who owns this server.
[4280.20 --> 4280.58]  Yeah.
[4280.58 --> 4282.72]  I think this is going to win.
[4283.08 --> 4287.60]  This is my bet for unpopular opinion for this, for the next Twitter poll.
[4287.84 --> 4292.46]  It manifests by every website asking you to accept the cookies.
[4292.68 --> 4293.62]  Over and over.
[4293.88 --> 4297.64]  There's another button which is to, you can go and like configure it.
[4297.64 --> 4300.04]  And then you enter this big preference.
[4300.04 --> 4302.60]  And then it's loads and loads and loads.
[4302.92 --> 4304.66]  Or enormous settings.
[4305.44 --> 4311.54]  And yeah, it's just, you can't even like tell the browser whether you want cookies or not.
[4311.70 --> 4313.42]  And then it just answers for you.
[4313.52 --> 4317.04]  You literally have to tap the button every time.
[4317.04 --> 4322.16]  And basically people just go, yeah, accept cookies just to get past this annoying screen.
[4322.58 --> 4325.36]  Well, well, that was fascinating.
[4325.60 --> 4326.34]  That was very interesting.
[4326.46 --> 4330.18]  I hope that all the people who joined learned new things and got inspired.
[4330.54 --> 4334.52]  I'm going to say, first of all, thank you very much, Jags and Joaquin for joining.
[4334.86 --> 4336.48]  And thanks, Matt, for co-hosting.
[4336.48 --> 4341.48]  And definitely see you all in an episode about AI-generated malware.
[4342.44 --> 4343.54]  AI-generated malware.
[4344.10 --> 4344.50]  Someday.
[4345.28 --> 4346.10]  Thank you both.
[4366.48 --> 4377.82]  Next up on the pod, Matt Reier, Golang Johnny, and John Calhoun are joined by special guest
[4377.82 --> 4381.04]  Tiago Mendez to discuss managing data at scale.
[4381.50 --> 4384.00]  Subscribe if you're new at gotime.fm.
[4384.24 --> 4387.54]  That'll give you something to look forward to next time on Gotime.
[4396.48 --> 4397.18] einsă!
