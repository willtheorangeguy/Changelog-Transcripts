[0.00 --> 10.86]  This episode of The Change Log is brought to you by Hacker Newsletter, a weekly newsletter delivered every Friday that shares some of the best articles on startups, technology, programming, and more.
[11.36 --> 15.24]  All links are curated by hand from the ever-popular Hacker News.
[15.96 --> 21.84]  Well, two big events are almost here, the 100th issue of Hacker Newsletter and 10,000 subscribers.
[22.58 --> 28.74]  To celebrate, 10 lucky subscribers who opened the 100th issue will win some very cool prizes.
[28.74 --> 33.72]  For full details, subscribe today at HackerNewsletter.com.
[48.20 --> 53.40]  Welcome to The Change Log, episode 0.8.080.
[53.90 --> 55.28]  I'm Adam Stachowiak.
[55.52 --> 56.52]  And I'm Wynne Nethelen.
[56.52 --> 57.72]  This is The Change Log.
[57.80 --> 59.54]  We cover what's fresh and new and open source.
[59.80 --> 63.04]  If you found us on iTunes, we're also up on the web at TheChangeLog.com.
[63.20 --> 64.00]  We're also up on GitHub.
[64.42 --> 70.34]  At TheGithub.com slash explore, you'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[70.76 --> 74.84]  And if you are on Twitter, follow The Change Log and me, Adam Stach.
[75.20 --> 77.34]  And I'm Penguin, P-E-N-G-W-I-N-N.
[77.80 --> 79.10]  We have some news to announce.
[79.16 --> 80.14]  You're recently hitched.
[80.28 --> 82.42]  Yes, I'm married.
[82.56 --> 83.30]  Heather Stachowiak.
[83.30 --> 84.92]  She is my bride.
[85.58 --> 87.84]  Congratulations to you and your lovely bride, Heather.
[87.90 --> 90.96]  Is she going to be changing it to MRS Adam Stach on Twitter?
[91.06 --> 92.56]  Is she going to keep her maiden Twitter handle?
[92.72 --> 94.16]  She's actually already moved over.
[94.26 --> 95.12]  She's Heather Stach.
[95.82 --> 96.92]  She's taking the brand.
[97.52 --> 97.88]  Nice.
[98.00 --> 98.48]  Stack attack.
[98.70 --> 98.94]  Yep.
[99.12 --> 99.58]  That's true.
[99.82 --> 101.76]  Heather Stach on Dribble as well.
[102.46 --> 103.98]  She's a talented designer in her own right.
[104.16 --> 105.04]  Yeah, she is.
[105.04 --> 106.40]  Fun episode this week.
[106.46 --> 108.56]  We talked to Tim Caswell, a.k.a. Creationix.
[108.60 --> 116.46]  He's been a contributor for The Change Log back in the early days when Node was the new hotness, but now it's the old stodgy.
[116.62 --> 124.78]  So if Node's not cutting edge enough for you, he's got Lovett, which is basically V8 with Lua bindings, if you're so inclined.
[125.44 --> 127.44]  That sounds like some madness.
[128.12 --> 128.76]  It is madness.
[128.76 --> 130.54]  Lua looks like a nice little language.
[130.78 --> 140.26]  I was exposed to it in Adobe Lightroom, which my wife uses for photography all the time, but it's making its way into every aspect of development now.
[140.32 --> 147.52]  So we talked about Lua and just what makes it nice, and then got into WebOS a bit since Tim was previously at Palm and HP.
[148.06 --> 149.26]  Wow, you guys covered a lot.
[149.70 --> 150.06]  That's true.
[150.54 --> 151.30]  Fun episode this week.
[151.34 --> 151.88]  Should we get to it?
[152.40 --> 153.06]  Let's do it.
[158.76 --> 166.38]  I'm chatting today with Tim Caswell, a former contributor to The Change Log.
[166.46 --> 170.32]  Big in Node circles, but today we're going to be talking about Lua and Lovett.
[170.48 --> 173.86]  So, Tim, for folks that might not know you, why don't you introduce yourself?
[175.54 --> 176.18]  All right.
[176.32 --> 184.40]  So, as Wyn said, my name is Tim, and I've worked on Node and open source software and web development for a very long time.
[184.40 --> 194.72]  I even, even going back to the 90s, I had a small startup making DHTML-based games that you could market in your .com website to bring in traffic.
[195.02 --> 196.12]  And everyone said I was crazy.
[196.22 --> 197.12]  They used to be Java applets.
[197.62 --> 199.22]  But, well, we saw how that turned out.
[200.34 --> 202.64]  And since then, I've done everything.
[202.86 --> 203.88]  I work a lot in Node.
[203.92 --> 205.14]  I wrote the HowToNode blog.
[205.90 --> 211.18]  And recently, I've been experimenting, taking Node's core library, porting it to all sorts of other runtimes.
[211.18 --> 214.22]  Fresh coat of paint on the HowToNode blog.
[214.30 --> 215.10]  I've just noticed that.
[215.66 --> 215.94]  Well done.
[216.12 --> 216.28]  Yes.
[216.72 --> 217.06]  Yes.
[217.14 --> 217.66]  I didn't do it.
[217.72 --> 220.28]  It was community contributed and looked good, so I took it.
[220.50 --> 221.68]  That's the best way to do it.
[221.84 --> 223.94]  So, let's talk about Lua and Lovett.
[224.04 --> 226.08]  So, how did you get tangled up into Lua?
[227.36 --> 235.20]  So, working on Node on webOS, I realized that V8 is not as lightweight as you would think.
[235.20 --> 238.74]  I mean, sure, compared to, like, Rhino, it's a pretty fast engine.
[239.80 --> 241.56]  Because Rhino starts up the JVM.
[242.28 --> 246.52]  But running V8 on a mobile phone, you realize that it's actually pretty heavy.
[246.94 --> 249.76]  Just starting up a Node process is a minimum 10 megs of RAM.
[250.66 --> 253.62]  And on the phone, over 1,000 milliseconds of startup time.
[254.28 --> 255.48]  I mean, that's just, that's crazy.
[257.16 --> 260.52]  And so, I was looking for something like JavaScript, but faster.
[260.52 --> 264.90]  And I heard a lot of people saying Lua is a good language and the VM is really clean.
[265.90 --> 272.16]  And so, just for fun, I wrote LibUV bindings to Lua to see what Node would be like in a different language.
[273.40 --> 276.22]  So, Lovett is essentially bindings for LibUV.
[276.78 --> 279.86]  What attracted you to Lua as a language, if anything?
[280.98 --> 287.34]  I mean, mainly, I just, I heard good suggestions from other people.
[287.46 --> 288.36]  TJ liked it.
[288.36 --> 291.82]  And looking at the language, it's a very clean language.
[292.10 --> 294.74]  It's, it was developed independently from JavaScript.
[295.58 --> 297.44]  Yet, they're extremely similar.
[297.82 --> 299.10]  Both have closures.
[299.28 --> 300.54]  Both have first class functions.
[301.20 --> 303.26]  Both have these things like objects.
[303.36 --> 304.28]  In Lua, they're called tables.
[304.50 --> 305.48]  They hold arbitrary values.
[305.60 --> 308.76]  They even both have the same annoying number type where it's always a double.
[310.40 --> 313.08]  I mean, the languages are surprisingly similar.
[313.62 --> 315.54]  There's, there's a few core things where they diverge.
[315.54 --> 320.18]  But, as far as power and flexibility, they're almost identical.
[320.70 --> 321.26]  So, is it typed?
[322.20 --> 322.54]  Nope.
[323.76 --> 325.68]  The type system is the same as JavaScript.
[325.96 --> 329.12]  It has coercion and all that timing.
[329.12 --> 334.58]  Basically, you take JavaScript, remove the braces, and put an end keyword, and you're pretty much there.
[334.58 --> 341.38]  So, the first time I came across Lua, I guess, was with the Adobe Lightroom product that my wife uses for photography.
[342.54 --> 343.86]  Plugins were written in Lua.
[344.00 --> 345.70]  I guess the main app is written in Lua as well.
[345.96 --> 348.72]  What other main installations have you seen for Lua?
[349.80 --> 352.70]  So, Lua is primarily an embedded system.
[352.82 --> 353.92]  Its goal is to be embedded.
[353.92 --> 357.08]  So, the game industry has really picked up on it.
[357.20 --> 359.18]  Like, it's the scripted engine to World of Warcraft.
[360.22 --> 366.00]  And, most, like most first-person shooters will use it.
[366.10 --> 369.26]  I mean, lots of game engines use it because it's trivial to embed.
[369.40 --> 374.08]  And, let's use the scripting language for your logic and your plugins.
[374.32 --> 376.44]  And, then you can use C or C++ for the rest of your game.
[376.94 --> 378.06]  So, where do you see Lovett going?
[378.24 --> 379.26]  Any practical applications?
[379.44 --> 381.66]  Or, is it still just a research tool right now?
[381.66 --> 385.80]  So, it's actually used in production by the people at Rackspace.
[387.12 --> 392.04]  And, the reason they went with it is because it has a much lower memory overhead than Node.
[392.50 --> 395.32]  But, it has more or less the same API and power of Node.
[396.72 --> 401.70]  So, if you're not just diehard in love with JavaScript, but you want something like Node, you can use Lovett.
[402.10 --> 403.66]  It's much more efficient on the system.
[404.84 --> 408.74]  And, also, I was thinking that it would be great for making games.
[408.74 --> 413.44]  One thing that LuaJet has that's really amazing is it has built-in FFI.
[414.12 --> 419.52]  This means you can call out to shared libraries, DLLs, SOs, without writing bindings for them.
[420.48 --> 422.82]  So, I can just write a pure Lua script.
[423.42 --> 426.42]  And, I can make OpenGL calls if the system has OpenGL installed.
[428.12 --> 430.20]  And, so, distributing that game is just a script.
[430.44 --> 433.42]  You don't have to send any binaries for all the various platforms.
[433.42 --> 436.92]  And, it's really fast the way that it's embedded into the VM.
[437.84 --> 439.50]  So, what libraries are available out there already?
[439.62 --> 447.22]  I know, in Node early on, that was kind of the bottleneck of getting support for other libraries out there.
[448.18 --> 452.40]  So, I changed the module system to be slightly different than Lua.
[452.66 --> 454.52]  Because, I mean, Lua already exists on the server.
[454.74 --> 456.62]  People use it for web servers.
[456.62 --> 459.56]  But, they're very not Node-like systems.
[460.78 --> 462.38]  And, so, I actually changed the module system.
[462.48 --> 464.96]  But, most Lua modules can be ported trivially.
[465.12 --> 466.76]  You just change how they export.
[467.34 --> 469.10]  As long as they don't use any blocking I.O.
[470.02 --> 472.60]  As far as things written specifically for Lovett,
[473.26 --> 475.38]  I know there's a few database drivers.
[475.56 --> 476.16]  There's Redis.
[477.18 --> 479.12]  There's some basic web frameworks.
[480.38 --> 483.20]  It has built in all the stuff Node has.
[483.20 --> 485.22]  So, we have OpenSSL, Zlib, JSON.
[485.80 --> 487.98]  Because, JSON is actually not part of the Lua language.
[488.14 --> 488.72]  Like, it is JavaScript.
[489.40 --> 491.70]  So, we had to bind in Yagile as part of Lovett.
[492.24 --> 493.34]  How far have you gotten?
[493.44 --> 499.12]  I know with Node, you start seeing these second-level frameworks crop up like Connect and Express.
[499.44 --> 503.96]  And, now there's dozens of these web frameworks that are built on top of it.
[504.34 --> 505.98]  Have you gotten that far with Lovett yet?
[506.92 --> 507.70]  Not much.
[509.00 --> 510.68]  Rackspace doesn't actually use the HTTP.
[511.28 --> 512.64]  They just use TCP and JSON.
[512.64 --> 514.44]  And, they're the biggest user of Lovett.
[515.96 --> 522.18]  They, I mean, their stuff is they've contributed OpenSSL and Zlib and all these libraries that they need.
[522.94 --> 526.50]  There are a few people who play with Lovett for web frameworks.
[526.62 --> 528.30]  I don't know of any actual website using it.
[528.42 --> 530.02]  So, there's not a lot of demand there yet.
[531.00 --> 535.22]  There's, I think, two or three mini frameworks for HTTP.
[535.22 --> 542.92]  What has developing Lovett taught you about Node or JavaScript or V8 that perhaps seeing it from a different angle?
[543.84 --> 544.54]  So, right.
[544.92 --> 552.26]  One of the reasons I did this experiment was there was this raging argument about how callbacks are difficult.
[552.26 --> 555.52]  And, this argument comes back regularly, I've noticed.
[556.78 --> 560.16]  And, Lua has coroutines built in.
[560.46 --> 561.38]  They're part of the language.
[561.38 --> 569.42]  And, using these coroutines, you can make code where you call an async function and then suspend your stack.
[569.74 --> 571.78]  And, you get resumed when the async function calls back.
[571.82 --> 572.64]  So, you don't have to nest.
[572.78 --> 573.58]  It'll look blocking.
[573.58 --> 577.34]  And, I experimented with this.
[577.48 --> 578.80]  And, yes, you can do that and love it.
[578.94 --> 580.30]  And, I still prefer callbacks.
[582.42 --> 582.96]  Why is that?
[583.00 --> 584.30]  I mean, I don't know.
[584.38 --> 587.18]  I just, maybe it's because I have so much more experience with them.
[587.32 --> 593.16]  Or, I like explicitly knowing when I'm between stacks.
[593.82 --> 596.28]  And, technically, you're not between stacks with coroutines.
[596.34 --> 597.26]  You're just pausing stacks.
[597.40 --> 600.42]  But, either way, these are the points where you can get preempted.
[600.88 --> 603.36]  Or, not preempted, but things can change out from under you.
[603.36 --> 604.28]  You have concurrency.
[605.86 --> 606.76]  And, I don't know.
[606.88 --> 607.46]  I like callbacks.
[607.82 --> 615.36]  The biggest dig I have on callbacks, you know, in the JavaScript community, it's almost a four, sometimes an eight space tab set.
[616.18 --> 616.32]  Right?
[616.34 --> 618.44]  And, you start doing these deep nested callbacks.
[618.60 --> 625.80]  You almost get to where you're doing nothing but indentation if you want to put a code snippet in a blog post just because you can't see the actual line that's doing the work.
[626.46 --> 626.66]  Yeah.
[626.80 --> 630.26]  And, there's a lot of techniques to make that better.
[630.36 --> 631.34]  You don't have to nest.
[631.34 --> 640.16]  I need to write a how-to-node blog article about that because that comes up all the time on the node list and starts all sorts of flame wars.
[641.46 --> 643.98]  Also, I use two space indents, so that helps.
[643.98 --> 660.06]  Are we seeing a backlash in the node community that perhaps Rails enjoyed after it peaked in popularity that, you know, this is just a healthy means you have arrived when you hit that Gartner lifecycle spot where people are starting to write articles against node?
[660.06 --> 664.56]  There's definitely been negative articles for at least a couple years.
[664.74 --> 666.78]  I mean, that started happening pretty early on.
[667.44 --> 669.64]  The community has definitely grown a lot, though.
[669.76 --> 672.96]  There's a lot more people who just use node because they want to get their job done.
[673.50 --> 676.98]  I've seen people who say, my employer says I have to use node and I don't like it.
[677.06 --> 677.76]  Help me out.
[677.76 --> 680.76]  I mean, you don't see that when a project is early on.
[683.40 --> 690.72]  Not too much of that, though, but there's definitely a lot more people using it who just want to get work done and not people who want to play with the technology.
[691.22 --> 693.48]  So, beyond V8, you're also playing around with SpiderMonkey.
[693.56 --> 694.46]  You've got LoveMonkey.
[695.22 --> 696.36]  How similar are these projects?
[696.36 --> 700.62]  So, LoveMonkey is LibUV bindings for SpiderMonkey.
[701.14 --> 704.92]  And for those that don't know, LibUV is the C library that powers node.
[705.66 --> 710.06]  It was written for node 8 and it has full Windows support built in.
[711.04 --> 714.04]  And that means that most of node's logic got ported into the C library.
[714.62 --> 720.72]  And so that's why I'm able to rebind node's core to all these other VMs so easily.
[720.72 --> 730.88]  And so basically, SpiderMonkey, the goal there, or the LoveMonkey port, the goal there is to be an API-compatible version of node using SpiderMonkey.
[731.94 --> 735.38]  Since it's the same language, why not expose the same API in the end?
[736.44 --> 745.08]  And that way we can have some of this browser, or not browser engine, but JavaScript engine competition that's good for node and good for the community.
[745.08 --> 751.14]  And also people can experiment with some of the JavaScript features that are upcoming in Harmony because SpiderMonkey already has them.
[751.56 --> 756.00]  What features of SpiderMonkey do you like over V8 and vice versa?
[757.84 --> 761.28]  The V8C API is definitely easier, or at least cleaner.
[762.66 --> 766.04]  The SpiderMonkey code, you can tell that it's been around a long time.
[766.04 --> 776.16]  But as far as the JavaScript side, I mean, ECMAScript versus JavaScript 185, if you looked at them, you wouldn't even know they were the same language.
[776.30 --> 784.78]  Because in SpiderMonkey, you have let, you have argument destructuring, you have these expressions, generator expressions, you have generators.
[785.02 --> 788.74]  I mean, it's code written for SpiderMonkey that knows it's SpiderMonkey.
[788.90 --> 793.26]  It almost doesn't look like JavaScript to me because I'm used to ECMAScript from being cross-browser compatible.
[793.26 --> 800.90]  What's your take on some of the recommendations for the next versions of JavaScript and some of the new features that have been proposed?
[801.56 --> 803.68]  I like most of the things going into ES6.
[805.46 --> 811.34]  I'm trying to remember, I think generators are going to be there, destructuring is going to be there, let should be there.
[812.42 --> 821.20]  I'm not too keen on some of the more heavy abstractions like a module system for JavaScript itself or a class system.
[821.20 --> 824.00]  I don't think the language needs these things.
[825.36 --> 827.84]  But some of the smaller things I like.
[828.24 --> 833.88]  Some of the things that maybe Lou already has or JavaScript 185 already has.
[834.46 --> 835.42]  What's your take on AMD?
[836.30 --> 837.36]  I don't like it.
[837.84 --> 840.18]  I mean, it's useful, I guess.
[840.18 --> 853.88]  When I want to package a node program for the browser, I will just pre-compile my scripts and add the proper wrappers around them in my generator.
[854.90 --> 856.18]  And if I want to...
[856.18 --> 860.56]  If I only want to write it in the browser, I just write it for the browser.
[860.56 --> 863.66]  I mean, I don't see what the use case for AMD is.
[863.82 --> 871.14]  If you're going to involve a node server anyway, why not write it in the simpler style and have your server generate the right code for the browser?
[871.44 --> 875.54]  Because anything in production, you're going to want compressed and concatenated scripts anyway.
[876.14 --> 882.82]  So many folks don't know that you were involved early on with CoffeeScript when you were working at Document Cloud with Jeremy Ashkena.
[883.04 --> 888.42]  So talk about candor and perhaps maybe how CoffeeScript influenced candor.
[888.42 --> 892.68]  So, yeah, I worked at Document Cloud with Jeremy.
[892.82 --> 893.88]  That was great.
[894.44 --> 900.96]  And I was making this language called Jack, which was basically a simplified JavaScript with a few things added.
[901.22 --> 903.74]  And then he was making this language called CoffeeScript.
[904.56 --> 906.40]  And I said, hey, we're working on the same thing.
[906.46 --> 907.16]  Let's join forces.
[908.18 --> 911.96]  And so I wrote the first version of the CoffeeScript compiler written in Node.
[913.04 --> 915.82]  And there were a lot of things I liked about the language.
[915.82 --> 919.82]  But since then, the language has gotten a lot of features.
[920.18 --> 922.04]  It's kind of suffered from its own success.
[922.32 --> 924.14]  And I feel it's a rather bloated language now.
[925.78 --> 937.20]  Candor, the goal there is to take JavaScript, remove the warts, and make a very bare bones, very simple language that's very easy to optimize.
[938.36 --> 939.48]  Candor has its own VM.
[939.96 --> 941.20]  It's all written in C++.
[941.20 --> 947.22]  And the goal is to make a faster VM by making it easier to optimize language.
[948.04 --> 950.18]  For example, in candor, there's no prototypes.
[951.52 --> 953.16]  There's no new keyword.
[954.30 --> 956.26]  You can't put properties on functions.
[956.36 --> 957.52]  Only objects can have properties.
[958.02 --> 959.46]  It's a very simple language.
[960.46 --> 962.32]  There's no this magic property.
[962.92 --> 965.80]  When you call a function, the arguments you pass in are the arguments you get.
[965.80 --> 970.54]  So if you're distributing your own VM, you're definitely not targeting this for browser apps then?
[971.46 --> 971.54]  Right.
[971.64 --> 977.16]  Well, I did start a project called Candor.js, where the goal is to make it a transpiler to JavaScript.
[977.68 --> 979.92]  I just haven't had time to actually work on that.
[980.96 --> 982.42]  You played around Go at all?
[983.40 --> 983.98]  A little.
[985.34 --> 986.22]  It's interesting.
[986.44 --> 987.68]  I think I like Rust better.
[988.96 --> 989.44]  I don't know.
[989.66 --> 994.46]  These new systems languages, I just want to see where they go after a little while.
[994.46 --> 997.78]  I definitely agree with a lot of the concepts.
[998.26 --> 1000.98]  The nice thing about Candor is it's the same syntax as JavaScript.
[1001.18 --> 1002.86]  It almost looks like a strict subset of it.
[1003.18 --> 1005.74]  And I'm assuming it's untyped the same way that JavaScript.
[1006.60 --> 1007.00]  Right.
[1007.28 --> 1007.60]  All right.
[1008.60 --> 1010.88]  So you're working at Cloud9 these days.
[1011.56 --> 1011.82]  Yeah.
[1012.00 --> 1014.48]  What's going on at Cloud9?
[1014.56 --> 1015.42]  What's exciting over there?
[1015.42 --> 1018.02]  All sorts of stuff.
[1018.10 --> 1025.92]  Trying to get the cloud-based IDE to be faster and more stable and better features.
[1026.32 --> 1029.24]  And a lot of that is refactoring the back end.
[1029.40 --> 1037.44]  So what I'm doing right now is I'm writing these node plug-in systems so that their massive code base can be stable and modular and testable.
[1037.44 --> 1040.22]  And we should be rolling that out fairly soon.
[1040.62 --> 1046.08]  So for those that don't know, Cloud9 at C9.io is basically a text editor in the sky.
[1047.00 --> 1050.38]  But it doesn't suck like you think it might just hearing that.
[1051.60 --> 1052.04]  Right.
[1052.40 --> 1055.34]  It actually took me a while to get the vision of it.
[1055.34 --> 1062.14]  If you look at it as just an editor in your browser for editing your local files, that doesn't make sense.
[1062.40 --> 1063.12]  Why would you do that?
[1064.36 --> 1067.46]  But what if you didn't have a local system?
[1067.84 --> 1070.06]  What if your files lived in the cloud as well?
[1070.60 --> 1073.24]  Because, I mean, GitHub already hosts your Git repos in the cloud.
[1073.88 --> 1078.24]  Why not clone them to another place in the cloud, edit them from there, and then push them back to GitHub?
[1080.14 --> 1082.70]  And when you look at it that way, it makes a lot more sense.
[1082.70 --> 1086.76]  Because it has a console, you can run Git commands from the browser.
[1087.64 --> 1089.32]  You can push to GitHub from the browser.
[1089.48 --> 1094.40]  You can run a server from the browser and point at it from another browser and see you're running a web server.
[1095.36 --> 1096.90]  And so you don't need a local machine at all.
[1097.98 --> 1103.52]  And once you look at it as moving my dev machine to the cloud, not just moving my editor, then it makes a lot more sense.
[1104.90 --> 1111.22]  So the ace editor that powers Cloud9 IDE is the same editor you get on GitHub when you edit this file.
[1111.22 --> 1113.18]  I believe so.
[1114.26 --> 1116.14]  If it's syntax highlighted, it's the same one.
[1116.88 --> 1119.10]  Reading the blog post here on GitHub.
[1119.38 --> 1129.98]  So if you've ever done fork and edit this file, which folks have done all the time with correcting spelling errors on a lot of the apps that I've got, then you've used that feature.
[1131.42 --> 1132.90]  So how big is the team at Cloud9 now?
[1136.32 --> 1136.86]  I'm remote.
[1136.94 --> 1137.54]  It's hard to tell.
[1137.66 --> 1140.08]  I think, I don't know, roughly 20.
[1140.08 --> 1142.38]  And how many of those are in Red Lake, Texas?
[1144.22 --> 1146.66]  I am the only JavaScript developer within 100 miles.
[1146.86 --> 1147.44]  Just the one.
[1147.66 --> 1153.12]  I told Tim before we started recording to watch our accents as we text and start talking to each other.
[1153.28 --> 1154.44]  The draws come out.
[1156.24 --> 1157.84]  So what's next for you at Node?
[1158.82 --> 1159.68]  Have you moved on?
[1159.74 --> 1160.80]  Are you still flinging Node?
[1161.30 --> 1162.44]  No, I still work on Node.
[1162.44 --> 1166.96]  I have a new blog that I do as part of my Cloud9 job called NodeBits.
[1168.02 --> 1171.86]  And initially it seemed to overlap heavily with HowToNode.
[1172.60 --> 1174.30]  But actually they are different sites.
[1174.84 --> 1177.06]  HowToNode teaches you the theory behind Node.
[1177.14 --> 1181.52]  It teaches you what objects mean in JavaScript, how to do callbacks, how to do async.
[1181.52 --> 1187.92]  And then NodeBits is sample projects, innovative examples.
[1188.60 --> 1196.30]  My most recent article, for example, is how to read the Linux joystick kernel device from Node
[1196.30 --> 1201.16]  and parse the joystick events so that you can interface a joystick with your Node server.
[1202.86 --> 1206.02]  So really things that get people thinking outside the box.
[1206.02 --> 1212.92]  So the purpose of NodeBits is to keep the innovation flowing, keep people having fun with Node.
[1213.34 --> 1216.96]  Have we boxed in Node as primarily a web framework?
[1217.14 --> 1219.42]  Is it suited for command line apps?
[1220.72 --> 1222.32]  It certainly works for command line.
[1222.46 --> 1227.68]  Desktop GUI apps are still hard because all the GUI frameworks have their own event loop
[1227.68 --> 1229.64]  and those don't meld well with Node's event loop.
[1230.04 --> 1232.46]  That may change in a future version of LibUV.
[1232.46 --> 1237.34]  The one nice thing about working at Cloud9 is that's where Bert and Ben work.
[1237.58 --> 1239.42]  And they're basically the LibUV guys.
[1239.90 --> 1242.40]  So I get to find out the inside scoop of where it's going.
[1243.50 --> 1249.76]  And hopefully with some future reflectors, you'll be able to have better bindings with like Qt or Coco
[1249.76 --> 1252.00]  and make desktop apps in JavaScript.
[1252.00 --> 1258.88]  So some folks might not know that we're both prior HP folk,
[1258.88 --> 1265.24]  and you were over in the former Palm team and working on, I guess you weren't working on WebOS,
[1265.38 --> 1266.74]  but you were involved in that group.
[1266.82 --> 1272.06]  What's your thoughts on how that was handled and what future, if any, WebOS has?
[1274.54 --> 1275.24]  I don't know.
[1275.34 --> 1278.34]  I mean, when I joined WebOS, they were already dying.
[1278.78 --> 1279.58]  And I knew this.
[1279.58 --> 1280.90]  I knew this going in.
[1280.96 --> 1284.96]  I believed in the idea of HTML as the platform,
[1285.44 --> 1288.10]  and so I joined the team anyway as an effort to try to help them.
[1289.56 --> 1292.80]  And I did a lot of work optimizing things, optimizing WebKit,
[1293.10 --> 1296.92]  and in the end it just died anyway for silly business decisions.
[1297.52 --> 1300.08]  The perception on the outside is it's this wonderful operating system
[1300.08 --> 1305.20]  that really suffered from the lack of industrial design and the hardware on which to run it.
[1305.34 --> 1306.72]  Is that fair?
[1306.72 --> 1307.20]  No.
[1307.20 --> 1307.60]  No.
[1308.60 --> 1311.66]  There was a lot of technical debt.
[1312.60 --> 1318.60]  There were a lot of issues in the code that the people left in the engineering team could just not handle.
[1319.24 --> 1322.62]  When Palm went under and got bought by HP, most of the good people quit.
[1324.12 --> 1325.84]  I mean, there were certainly good people left,
[1326.00 --> 1328.18]  but there was way more work than they could do on their own.
[1328.18 --> 1332.48]  And we just missed deadline after deadline.
[1332.94 --> 1336.50]  I mean, it doesn't help that the CEO does crazy stuff like he did,
[1336.64 --> 1339.58]  but on top of that, there were lots of technical issues too.
[1340.62 --> 1341.28]  So what's next?
[1341.48 --> 1345.68]  What's got you excited that's on your radar other than LibUV that you just want to play with?
[1346.32 --> 1350.58]  Speaking of HTML and mobile devices, Boot to Gecko is really interesting,
[1350.58 --> 1355.46]  and WebOS is now open source, so maybe that'll get a second life.
[1356.92 --> 1358.94]  But I've been playing with Boot to Gecko,
[1359.06 --> 1363.54]  and one very important difference between the two is with Boot to Gecko,
[1363.68 --> 1365.76]  there is no such thing as a local app.
[1365.76 --> 1372.22]  Even your dialer and your home screen are just web pages hosted on gecko-mobile.org.
[1373.30 --> 1377.54]  And the way this works offline is they just pre-fill the cache on the phone,
[1378.08 --> 1382.86]  the HTML5 cache with the files for these particular apps.
[1383.64 --> 1388.52]  But everything on the phone is a web app, and even your phone dialer.
[1388.52 --> 1391.46]  So perhaps a really bad metaphor,
[1391.46 --> 1399.10]  this would be like Chrome OS except replace Chrome with Mozilla for your phone.
[1399.98 --> 1400.96]  Similar, yeah.
[1401.84 --> 1403.92]  Except Chrome OS is basically a browser,
[1404.94 --> 1407.06]  whereas these look like native apps.
[1407.94 --> 1410.36]  It has a lock screen that you swipe away,
[1410.56 --> 1414.42]  and I mean the interface can look like any other phone,
[1414.70 --> 1417.24]  but the technology behind them is, yes, they're all just web pages.
[1419.84 --> 1421.28]  So there's some similarities.
[1421.90 --> 1423.00]  It's kind of like Chrome OS.
[1423.10 --> 1424.14]  It's kind of like web OS.
[1425.08 --> 1426.26]  But it's different, too.
[1427.30 --> 1428.78]  Well, thanks, Tim, for joining us
[1428.78 --> 1432.04]  and keeping us up to date on the Node community and what you're doing,
[1432.16 --> 1433.68]  and I hope you'll stop back by soon.
[1434.20 --> 1434.80]  All righty, thank you.
[1434.80 --> 1434.82]  Thank you.
[1451.46 --> 1461.00]  The Medicare
[1463.94 --> 1464.70]  music
[1464.70 --> 1466.64]  in your arms
[1466.64 --> 1468.80]  as a dark fashion
