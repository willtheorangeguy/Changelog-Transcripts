[0.00 → 4.14] This episode is brought to you by Type kit, the easiest way to use web fonts.
[4.60 → 7.66] Type kit pioneered the usage of CSS web fonts nearly two years ago
[7.66 → 10.88] and continues to be the leading source for designers and developers today.
[11.48 → 13.82] Sign up at typekit.com for as little as $4 a month
[13.82 → 19.98] and get thousands of high-quality fonts from the likes of Adobe, Font Font, Mark Simpson, and more.
[20.52 → 22.84] The hardest part is deciding which font to use.
[23.58 → 26.84] Try Type kit risk-free for 30 days at typekit.com.
[27.58 → 29.92] And by Tasks from Idea Division.
[30.50 → 34.80] Tasks for iPhone and iPod Touch is a simple yet sophisticated application
[34.80 → 38.34] to keep track of your to-dos, notes, due dates, and priorities.
[39.00 → 41.70] With Cloud Sync out of the box and coming soon to the web too,
[41.70 → 44.94] it's their take on connected task management.
[45.64 → 47.50] Learn more at taskapp.com.
[60.00 → 62.34] Don't push me away!
[62.34 → 65.86] Welcome to the Changelog episode 0.6.2.
[66.06 → 67.22] I'm Adam Stachowiak.
[67.46 → 68.30] And I'm Wynn Netherlands.
[68.48 → 69.42] This is the Changelog.
[69.48 → 71.04] We cover what's fresh and new in open source.
[71.54 → 74.72] If you found us on iTunes, we're also on the web at thechangelog.com.
[74.84 → 75.96] We're also up on GitHub.
[76.58 → 78.48] Head to GitHub.com slash explore.
[78.48 → 81.64] Or you'll find some trending reposts, some feature reposts from our blog,
[81.72 → 82.90] as well as the audio podcast.
[83.48 → 86.22] If you're on the Twitter, follow Changelog Show and me, Adam Stack.
[86.60 → 88.96] And I'm Penguin, P-E-N-G-W-Y-N-N.
[89.72 → 90.54] Fun episode this week.
[90.60 → 94.36] Talked Irons with Frederick Nordstrom, way over in Sweden,
[94.60 → 99.40] about Irons that sits atop F-sharp, which sits atop .NET.
[99.90 → 101.74] Some really cool low-level stuff this week.
[101.94 → 103.84] Nice to see some .NET coming into the stream here.
[104.28 → 105.48] Yeah, hopefully we'll get some more of that.
[105.72 → 108.08] Speaking of JavaScript, we'll be at Texas JavaScript.
[108.94 → 109.70] At least I will.
[109.76 → 110.00] You going?
[110.60 → 111.58] I'm thinking about it.
[111.82 → 112.62] I'm thinking about it.
[113.02 → 116.08] On June 11th in sunny Austin, Texas,
[116.08 → 121.16] Doug Crockford and others will be there at the premier regional JavaScript event.
[121.42 → 122.10] It was fun last year.
[122.16 → 123.10] Wouldn't miss it again this year.
[123.60 → 127.54] Speaking of regional conferences, we'll be at Lone Star Rubicon in August.
[128.36 → 130.74] Calls for proposals are now open.
[130.74 → 134.32] So if you haven't submitted to speak at Lone Star, and you're a Rubbish,
[134.42 → 135.50] then what are you waiting on?
[135.86 → 136.26] That's right.
[136.40 → 140.70] And we'll also be at Rubicon in Argentina, Buenos Aires, at November.
[140.94 → 141.84] Well, we won't be there, actually.
[141.92 → 142.54] We won't be there.
[142.68 → 147.40] Actually, we're trying to get a special correspondent, Ernesto Tag Worker,
[147.54 → 152.06] down in Buenos Aires, is hoping to cover that for us.
[152.28 → 152.80] There you go.
[153.00 → 153.78] Way down there.
[154.20 → 155.62] November 8th and 9th.
[155.62 → 161.42] Check out rubyconf.com slash – that's not a slash, it's a dot – dot com dot AR.
[161.56 → 162.16] It's kind of odd.
[162.54 → 164.22] You know, we love regional conferences.
[164.52 → 167.60] I think that's where the conversation happens in a lot of these communities.
[167.78 → 173.06] So if you're organizing a regional conference and want to promote it on this here podcast,
[173.26 → 176.08] let us know how we can work with you to get the word out about those.
[176.52 → 176.88] Absolutely.
[177.14 → 178.60] Submit at thechangelaw.com.
[179.18 → 179.86] Fun episode this week.
[179.90 → 180.40] Should we get to it?
[180.80 → 181.42] Let's do it.
[181.42 → 194.96] I'm chatting today with Frederick Nordstrom from Irons.
[195.36 → 198.48] So, Frederick, why don't you introduce yourself and a little bit about what you do.
[199.56 → 199.98] Yeah, okay.
[200.14 → 205.96] I'm a software developer at Crispin Porter Borowski at my day job.
[206.66 → 209.12] Just quit today, actually, but that's irrelevant.
[209.12 → 219.50] I work on Irons in my spare time, which is really – I do pretty much only .NET programming nowadays.
[220.00 → 228.10] I've done PHP, Ruby, JavaScript, and all the whole shebang, but I got stuck in .NET a couple of years back, and, well, I like it here.
[228.60 → 232.90] So Irons is a JavaScript runtime for .NET written in F-sharp.
[232.90 → 235.86] So for our listeners, there's a lot to unpack there.
[236.02 → 239.34] So let's start with F-sharp.
[239.64 → 240.96] What exactly is F-sharp?
[241.82 → 250.26] Well, F-sharp is a functional programming language, ported language for Microsoft from Visual Studio 2010, which is, like, last April, I think.
[250.36 → 250.46] Yeah.
[251.72 → 256.28] I mean, it's based on the ML style, like ML OCaml style languages.
[256.28 → 260.40] I would almost call it, like, an OCaml dialect, but not quite.
[261.04 → 266.46] Runs on .NET, interrupts with, like, C-sharp, VS, whatever you can run on .NET, basically.
[267.42 → 273.74] But it's functional, so you have the whole, like, static assignment, like, immutability, stuff like that built in.
[274.38 → 277.74] So Irons is a JavaScript runtime built on top of that.
[277.86 → 282.86] What's the use case for having a different JavaScript runtime on top of .NET?
[282.86 → 289.30] I mean, on top of the net, like, when I started, there wasn't really any JavaScript runtimes available.
[289.48 → 298.54] If you wanted to use JavaScript as a scripting language for your application or a game or whatever, it was, like, there's this JScript thing that Microsoft uses in IE.
[299.14 → 303.74] But it's, I mean, it's pretty bad, and the integration with .NET is very flaky and weird.
[304.08 → 307.78] So I started Irons in December 2010.
[308.40 → 309.60] No, 2009, sorry.
[309.60 → 319.10] Mostly, I mean, the original thing was that I was going to use it for, like, a database, like a, you know, like, NoSQL database I was working on.
[319.80 → 326.30] But then I found the whole JavaScript runtime a lot more fun to work on, so I just, like, scrapped the other project, and I've been working on Irons ever since.
[326.90 → 332.26] So you support the regular .NET framework, but also Mono, what was involved in getting it to run on Mono?
[332.26 → 334.58] Not a lot, actually.
[335.16 → 337.84] Like, changing two references and compiling, basically.
[338.58 → 340.70] It was almost painless.
[341.86 → 346.60] I know you're on Windows as we're recording this podcast, but are you playing around with Mono on Linux at all?
[347.34 → 351.96] Yeah, I mean, I have a what do you call it, a dual boot or whatever, into Ubuntu?
[352.08 → 352.46] Ubuntu?
[352.72 → 355.90] Yeah, Ubuntu, whatever you call it, that I run.
[355.90 → 361.16] And usually, like, just the latest version of everything, I think it's, like, 11.04 or something.
[362.02 → 367.22] And I run, like, Mono develop and stuff like that, so I can make sure RNG is constantly compiling on Mono.
[367.58 → 375.22] So I've got to ask you, the trend in naming ported languages to Microsoft's frameworks as Iron Something, where did that come from?
[375.22 → 378.72] I think it's, what do you say, like a homage, yeah?
[379.06 → 379.30] Right.
[379.48 → 388.82] To the original developer who developed the original implementation of Iron Python, like, way back before the dynamic language runtime existed.
[389.58 → 391.60] I think that's the history of it.
[391.64 → 392.52] I'm not quite sure.
[392.98 → 401.02] But, I mean, you had, like, Iron Ruby and Iron Python, so when I was going to name my old thing, I was just like, okay, RNG is, like, why not?
[401.12 → 402.80] It's the obvious choice.
[402.80 → 407.36] But I don't know exactly where the prefix iron comes from.
[408.52 → 409.82] So what about JavaScript support?
[410.10 → 413.52] What version of JavaScript, or I guess an EMMA standard, are you supporting?
[414.58 → 418.28] Currently, just three, which I'm very sad about.
[418.44 → 421.76] But we're working on the ECMAScript 5 compatibility.
[422.54 → 423.30] Yeah, combat.
[424.64 → 428.20] And it's, I mean, it's trucking.
[428.28 → 431.88] I mean, it's going to be a couple of months before it's fully in place.
[432.80 → 437.10] We got, I mean, I have one guy helping me from the States, John.
[437.46 → 439.26] Thanks, John, by the way, if you're listening to this.
[440.28 → 441.34] He has helped tremendously.
[442.28 → 446.14] So we're working, but we sort of got sidetracked with performance because it's a lot more fun to work on.
[447.30 → 447.68] Sure.
[447.68 → 449.78] The graphs going down and down and down.
[450.06 → 460.36] It sort of more gives you a better gratification than, but we're getting back on the ECMAScript 5 horse right now to get that done.
[460.38 → 463.34] What's the practical impact of supporting through JavaScript 3?
[463.48 → 465.26] What sorts of applications can be ported?
[465.30 → 466.68] Can you run Node on this?
[466.68 → 469.14] Yes, in theory.
[469.30 → 476.84] There's one guy I talked to today, actually, that's working on Node.js for .NET using Iron.js.
[477.22 → 484.26] One of the things that fascinates me about, I guess, the .NET framework is that it's kind of the inverse of a lot of frameworks out there.
[484.42 → 488.30] The Unix community tends to find the best in breed tool for the job.
[488.30 → 492.96] And with the .NET framework, you've got multiple languages that compile down to one framework, right?
[493.74 → 493.84] Yeah.
[493.96 → 499.52] So in theory, you could do the same thing with, I guess, CoffeeScript that you're doing with JavaScript, correct?
[500.30 → 500.54] Yeah.
[500.82 → 502.80] Without having to go through the JavaScript layer at all.
[503.32 → 503.56] Yeah.
[503.96 → 505.46] Have you played around with CoffeeScript at all?
[505.80 → 511.12] You mean basically like getting a native parser for CoffeeScript that would run on top of Iron.js?
[511.84 → 516.56] Or even bypass Iron.js and go directly down to the Sharp .NET.
[516.56 → 520.60] Oh, you mean like just parsing CoffeeScript basically straight off and going straight down.
[521.36 → 528.94] Oh, I mean, I've been playing around with getting a native parser for CoffeeScript because that speeds it up by a lot.
[530.28 → 536.28] But I haven't touched CoffeeScript in the regard of just compiling it straight to .NET.
[536.98 → 541.48] Because that would have to be a completely separate project from Iron.js.
[541.48 → 551.66] So in the previous episode, we covered PyPI, and it has some .NET extensions that can be compiled for Python.
[551.98 → 557.44] Is there any sort of ability to load .NET assemblies using Iron.js?
[557.44 → 558.44] Yeah.
[558.44 → 559.08] Yeah.
[559.08 → 567.14] I mean, since I'm using the dynamic language runtime, you have pretty much access to all of C Sharp inside the JavaScript if you choose to.
[567.48 → 573.44] Like if you're hosting it in an application or a game or something, I mean, you probably want to limit what the user can do.
[573.56 → 576.62] Because otherwise, you could introduce yourself.
[576.74 → 579.74] I mean, you have the security applications of letting the user do whatever they want.
[579.74 → 584.76] But yes, you can access pretty much any functionality from .NET inside of Iron.js.
[584.76 → 592.82] But this would be a great way to expose a scripting interface for your application to third-party developers.
[593.88 → 594.46] Yeah, exactly.
[595.26 → 598.04] And then you want to limit what they can do.
[599.00 → 601.86] But that's a different issue.
[601.98 → 604.54] But yes, you can access all of .NET inside Iron.js.
[605.12 → 606.22] So back to Mono for a second.
[606.28 → 608.14] Have you built anything with Mono?
[609.74 → 611.04] Yeah, small things.
[611.22 → 616.14] You know, like I used to have the C Sharp scripting ability.
[616.36 → 619.94] Like you can use C Sharp as sort of like a shell script language or something like that.
[620.34 → 622.14] I played around with that a bit.
[622.88 → 627.04] You know, but I mean, I haven't really built anything specifically for Mono.
[627.68 → 633.32] I built a lot of stuff that I've made sure that runs both on Mono and on Windows or the canonical .NET implementation.
[634.08 → 636.10] But nothing Mono specific, you know.
[636.38 → 638.52] We need to get Mono on the show.
[638.52 → 640.76] So it's a fascinating little application.
[641.44 → 641.66] Yeah.
[642.24 → 644.54] I mean, I've been speaking to Miguel.
[644.82 → 645.98] You know, Miguel de Castro.
[645.98 → 646.52] Sure, sure.
[646.92 → 648.96] I probably butchered his name to no end there.
[649.44 → 652.76] But I mean, he's a really nice guy.
[652.92 → 654.10] And there's the Mono team also.
[654.48 → 659.90] I mean, Mono product itself is, I mean, it's insane how well they're doing.
[659.90 → 661.74] I mean, yeah, they're backed by Novel.
[661.82 → 666.84] But still, I'm thoroughly impressed by the progress and how good it's coming along.
[666.84 → 677.52] You know, in your introduction email that you tipped me off to this project, it sounded a lot like a lot of the letters I get from folks in the .NET community.
[677.86 → 683.66] And usually it starts out, you guys don't cover .NET much on the podcast, but here's a great project I'd like you to take a look at.
[684.00 → 686.76] The reason we don't is that they're so hard to find.
[686.84 → 688.32] We're trying to make inroads into that community.
[688.32 → 696.64] Talk a minute about the difference in, I guess, open source philosophy between the .NET community and the rest of the web world.
[697.66 → 705.94] I mean, I think the .NET community, and I can see this even when I'm working professionally, is basically based on closed source, on proprietary software.
[707.02 → 714.00] I mean, there are usually like, you know, you can find the occasional open source plug-in to the CMS you're using or whatever.
[714.00 → 718.74] But, I mean, there are a few open source CMSs like Umbra and a couple of others.
[718.96 → 725.12] But, I mean, the community as a whole and like all the products that Microsoft sell that concern .NET, it's all closed source.
[726.36 → 728.24] There's very little open source.
[728.38 → 730.12] I mean, F-sharp is, I would say, is mostly open source.
[730.22 → 732.16] I mean, even F-sharp itself is open source, actually.
[733.22 → 735.36] So you can download the compiler and mess around and everything.
[735.36 → 742.16] But, looking at C-sharp and VS, it's all closed source, straight through, basically.
[743.00 → 748.74] And, I mean, I learned programming through like C and PHP and Perl and Python and stuff.
[749.34 → 757.84] So, I mean, I miss the open source perspective you get in those languages and the like Ruby, JavaScript world and stuff.
[757.84 → 767.46] You know, one of the things that I really enjoyed coming to the Ruby community from the .NET community was just Ruby Gems and the package management.
[767.74 → 772.26] And I know Python has PyPI and PIP rather than an easy installation.
[773.80 → 777.04] Is NuGet this answer for .NET?
[777.78 → 777.98] Yeah.
[778.78 → 780.04] Yeah, I'd say it is.
[780.56 → 782.92] I use it for pretty much everything now.
[782.92 → 789.32] Yeah, it's, I install it, as soon as I install Visual Studio, I install NuGet and use it for pretty much everything.
[789.50 → 791.02] It's, it's been working flawlessly.
[791.26 → 796.68] I mean, and what I like about it is that it's not only for like, you know, like .NET assemblies.
[796.82 → 801.08] It's for like pretty much anything, like JavaScript files, templates, like whatever.
[801.32 → 803.66] It's, it's not only for libraries.
[804.06 → 808.82] Do you know when you install packages via NuGet, does it also put things in the registry?
[809.52 → 809.74] Hmm.
[811.08 → 812.64] Not the foggiest, actually.
[812.64 → 814.26] That's just curiosity.
[814.48 → 819.98] I was, we should have those guys on the show, but it, I guess with Windows, even with the .NET applications,
[820.12 → 822.68] there's still that registry component still on Windows, correct?
[823.66 → 825.34] Yeah, like the global assembly cache.
[825.54 → 825.82] Right.
[825.92 → 827.72] Or like registering it in the GAC.
[828.10 → 828.60] The GAC.
[828.70 → 831.56] The people, yeah, the people in the know, say the GAC.
[832.10 → 834.30] That's a word I haven't heard in quite some time.
[834.92 → 835.22] Yeah.
[836.20 → 841.46] I don't know, I'm like, I've never like gotten used to like how the whole assembly cache thing works.
[841.46 → 842.16] It's just awkward.
[842.70 → 846.40] I think the so the way they present it and the way it's used is really awkward.
[846.52 → 852.42] It's just like, like I want my DLLs in a folder and like, that's the version I use and just be happy with them.
[852.42 → 854.42] But they insist on putting them freaking everywhere.
[854.42 → 854.46] Sure.
[855.24 → 858.30] So Nougat is the package management piece of that.
[858.38 → 861.00] But if you're looking for open source and .NET, where do you go?
[862.58 → 862.94] Complex.
[863.28 → 865.22] I said CodePlex.com or is it .org?
[865.76 → 866.86] Yeah, I think it's .com.
[867.48 → 870.06] And that has most of the open source .NET stuff.
[870.06 → 875.32] There's another place called, oh, I don't remember the name.
[875.44 → 877.58] But I mean, GitHub has a lot of C Sharp properties also.
[877.80 → 879.16] I noticed just a couple of days ago.
[880.72 → 885.86] Sadly, not so much F Sharp, but I suppose the language is sort of like a niche language.
[886.32 → 888.84] But yeah, I take GitHub and Complex, definitely.
[888.84 → 895.80] You know, one aspect of, I guess, .NET, probably the counter or the epicentre of that is C Sharp.
[896.02 → 897.62] You know, it's just the biggest footprint.
[898.26 → 901.58] And it's just unfortunate that there is a special reserve character.
[901.72 → 906.00] So it's just not search engine friendly when you're finding a lot of C Sharp stuff.
[907.18 → 911.40] Yeah, I've had problems because I've been looking for jobs occasionally around Sweden.
[911.40 → 918.96] And you can't search for, like, you can't search for C Sharp because the search input boxes don't accept the pound sign.
[920.02 → 920.52] So it's like...
[920.52 → 921.42] What's the same with .NET?
[921.58 → 924.96] A lot of times you'll see C Sharp spelled C-S-H-A-R-P, right?
[925.02 → 926.54] And .NET spelled D-O-T-N-E-T.
[927.36 → 930.94] Yeah, because you can't search for .NET either because, like, invalid characters.
[931.12 → 934.58] Only alphanumeric plus the Swedish extension characters.
[935.00 → 936.88] So it's like, okay, well...
[936.88 → 938.14] But Java, of course, works.
[938.14 → 943.30] So you mentioned a number of languages that you, I guess, learned on prior to .NET.
[943.38 → 946.52] What sort of perspective has that given you in writing .NET code?
[947.34 → 959.78] I'd say the biggest impact that especially Python had on me, or Linux as a whole, because I did use Linux a lot a couple of years ago, or like five, six years ago,
[959.78 → 970.08] is the whole, like, async and many processes, like, one process compared with one thread compared to, like, monolithic process with, like, 40 threads,
[970.16 → 971.24] which is, like, the Windows model.
[971.52 → 980.12] And sort of the asynchronous style of programming that, well, Node use leverages, but also, like, that's very common, like, with the e-pal and select calls.
[980.12 → 993.18] And that's, I think, is the biggest influence that I prefer to think in, well, async and processes instead of, like, threads and, I don't know, weight handles, I think they call it in .NET, yeah.
[993.82 → 998.42] What sort of advantages do you think a .NET developer has over a Unix developer?
[998.42 → 1007.14] I'd say the like, how, because you get used to handling threads in .NET pretty fast, and I think that's the main thing.
[1007.96 → 1013.84] Like, I mean, multithreading is really freaking hard, and, I mean, no one would ever claim to be good at it, I think.
[1013.96 → 1016.32] But at least I'd say that I'm decent at it.
[1016.54 → 1023.86] And I have friends who are, like, you know, Python or PHP, and PHP might be a bad example, but, you know, Python and stuff like that.
[1023.86 → 1030.90] And there's no real multithreading there in the way you do it in .NET, and you don't learn that because that's not the Unix model, basically.
[1031.88 → 1033.28] Small tools, one process.
[1033.96 → 1036.22] So you mentioned that F-sharp is a functional language.
[1036.54 → 1038.12] Is it compiled or dynamic?
[1039.86 → 1040.56] It's compiled.
[1040.70 → 1042.82] It's statically compiled, but it's type-inferred.
[1043.08 → 1048.56] So you basically don't have to, like, type out the types, if you know what I mean.
[1048.56 → 1057.30] Yeah, so it infers most of the types from the way you use the variables and the constants and stuff.
[1057.68 → 1062.14] So you're writing JavaScript on top of this in Iron.js.
[1062.50 → 1066.54] So you're straddling that line between compiled and dynamic.
[1067.16 → 1070.68] What aspects of both of those worlds do you like?
[1070.68 → 1077.42] I mean, I have to say, like, if I'm using, like, C-sharp, I mean, I grew up with, like, PHP, Python mostly.
[1077.70 → 1081.38] I did some JavaScript, you know, like when the DHTML from 2001.
[1081.54 → 1081.80] Right.
[1083.68 → 1086.66] Which a lot of what we call AJAX is actually just DHTML.
[1086.80 → 1089.20] If you're not making a network call, it's DHTML, right?
[1089.98 → 1090.24] Yeah.
[1090.84 → 1099.50] But, I mean, just, like, everyone remembers, like, and you'd search for this, like, little snippet on the internet to, like, scroll the like, the status bar and the text would scroll and stuff.
[1099.50 → 1100.64] But, sorry.
[1101.66 → 1109.26] Anyway, I mean, I think the main drawback of, like, the statically typed languages, if you look at, like, Java and C-sharp, is that they're so verbose.
[1109.92 → 1121.06] Like, it's the amount of, like, physical code and characters you have to put down, like, link down on the keyboard to be able to produce something is quite staggering if you compared it to, like, JavaScript or something.
[1121.06 → 1127.98] But if you're looking at F-sharp, for example, I mean, it's a statically typed language, and it has to be.
[1128.20 → 1132.80] Like, you can't, like, make it dynamic where you want, like, with the dynamic keyboard and C-sharp or stuff.
[1133.32 → 1135.12] It's statically typed and that's it.
[1135.12 → 1141.94] But, I mean, the amount of code, if you look at lines or, like, amount of characters, it's almost equal to JavaScript because it's so tiers.
[1143.58 → 1153.02] So, if you have a language like that, I mean, that includes, like, Haskell, F-sharp, stuff like that, I see very little benefit of being dynamic.
[1153.02 → 1163.94] But if you're comparing dynamic like JavaScript versus C-sharp, then I see a benefit of being dynamic because of the I mean, the amount of code you don't have to write, basically.
[1164.86 → 1168.80] So, the last time I did .NET professionally, it was ASP.NET.
[1168.90 → 1172.74] It was before the MVC release.
[1173.32 → 1176.38] So, are you doing much on the web with .NET?
[1177.60 → 1178.04] Yeah.
[1178.04 → 1186.86] I mean, my day job is pretty much, I mean, I do the heavy back-end lifting, but, I mean, I plunk some, like, web forms and stuff at times.
[1189.00 → 1191.08] Not a fan at all.
[1191.08 → 1208.08] So, it seems like that when .NET came out, Microsoft tried to take a desktop abstraction or a paradigm and write an abstraction web forms, right, to expose the web to folks that aren't used to writing web applications.
[1208.46 → 1213.06] And it was just a crazy, weird abstraction in hindsight.
[1213.06 → 1217.90] Have you seen a philosophy change at Microsoft over the last 10 years at all?
[1218.02 → 1221.88] Are they really embracing the web or is it still an embrace and extend philosophy?
[1223.36 → 1227.74] I mean, with MVC 3, I didn't use the first one, but the second and third one.
[1228.60 → 1238.88] I just, it's, you know, like, but, I mean, coming from Python and PHP, like, the thing they sell in, like, ASP.NET, MVC 3 and stuff, it's stuff I saw around, like, 2005.
[1238.88 → 1242.06] You know, it's, like, but this isn't really new.
[1242.22 → 1245.44] Like, Ruby and Rails did this six years ago or, like, five years ago or whatever.
[1248.22 → 1256.88] So, I mean, I don't think they embrace and extend as much, but the stuff they release is stuff that everyone else has been using for years currently.
[1258.68 → 1260.08] That's the way I look at it, at least.
[1260.92 → 1268.18] So, at least on the web with Ruby and Python and other frameworks, there seems to be a myriad of server choices that you can deploy to, right?
[1268.18 → 1274.40] There's, even in the Ruby world, there's Thin and Unicorn and Passenger, and we just have a host of different choices.
[1275.08 → 1277.60] On .NET, are you still tied to IIS?
[1278.48 → 1279.34] Yeah, pretty much.
[1279.92 → 1288.22] I mean, but I don't see it as a bad thing, really, because at least when I do stuff for work and, you know, like, you do applications for different companies and stuff,
[1288.78 → 1294.32] they, I mean, they pick .NET because it's a Windows platform, and that's because they have a Windows network, which means they have an Active Directory.
[1294.32 → 1299.84] You know, like, they want everything integrated, you know, like the IIS and .NET and Webforms even.
[1299.98 → 1301.26] It's just like, it just works, you know.
[1301.32 → 1302.58] You don't need to really do anything.
[1302.70 → 1306.26] Like, all the permissions work, like, logins, everything just works.
[1306.70 → 1313.12] So, IIS brings a lot of benefits in terms of integration with other Microsoft systems, like, yeah, AD and stuff.
[1313.12 → 1321.52] The other difference that seems to come up quite a lot between .NET developers and, I guess, open source or Unix developers,
[1321.94 → 1332.50] and a lot of times this is more of a corporate versus, you know, startup type of mentality, is in .NET, a lot of times in Java, you're tied to an IDE,
[1332.74 → 1335.08] whereas in other languages, people prefer text editors.
[1335.34 → 1336.26] Where do you hang out all day?
[1337.06 → 1338.54] I swear by Visual Studio.
[1338.80 → 1340.42] Pride for my cold, dead hands.
[1340.66 → 1340.94] Oh, yeah?
[1340.94 → 1342.22] Oh, yeah.
[1343.04 → 1350.66] It's, I mean, once I got used to it, I will not ever program without an IDE ever again.
[1350.90 → 1357.22] It's, I mean, I started doing .NET fully around 0405, maybe.
[1358.50 → 1361.42] And, I mean, it took a while to get used to Visual Studio.
[1362.22 → 1362.48] Definitely.
[1362.82 → 1368.38] But now it's, I mean, the amount of help it gives, especially when you're writing code like C-sharp code or Java code,
[1368.38 → 1369.76] which is very verbose.
[1369.76 → 1372.54] I mean, it gives you so much assistance.
[1372.68 → 1377.26] And even, like, if you're looking at someone else's library, you can just, like, jump around, you know, like the go-to-definition stuff.
[1377.62 → 1383.52] And that's, and then when I, at times, have to open, like, a PHP project at work, and I'm just completely lost.
[1384.14 → 1388.36] Like, I've lost the skill of navigating code without an IDE, sadly.
[1388.86 → 1393.94] You know, I used to be in that camp where I couldn't do anything without a GUI menu to do it for me.
[1393.94 → 1402.58] But since moving to Ruby and Rails and embracing kind of the Unix philosophy, I found myself writing my own little scripts to automate a lot of what I do on a daily basis.
[1402.58 → 1404.50] To what extent can you automate Visual Studio?
[1405.12 → 1406.76] You can do pretty much whatever you want.
[1406.88 → 1410.34] I mean, Visual Studio has a rich extension gallery nowadays, at least.
[1410.54 → 1413.38] I know it's been building up since 2008.
[1413.54 → 1415.58] And now 2010 has it integrated even.
[1415.58 → 1420.06] And, I mean, there are extensions for pretty much everything you could possibly get.
[1420.14 → 1422.22] There's even a Git extension now that actually works.
[1423.68 → 1426.78] So I'm using that for, like, the small things like committing and updating.
[1427.34 → 1428.08] I'm glad you brought that up.
[1428.20 → 1434.98] So is there any traction for Git and Mercurial and the open source .NET community outside of Team Foundation server?
[1434.98 → 1446.10] I mean, I think Mercurial, so I can't pronounce that being so much, has more traction than Git in the .NET community, I think.
[1446.18 → 1454.66] Because Complex has a HG-like repository option next to the normal Team Foundation, I think.
[1456.86 → 1458.04] But, I mean, I use Git.
[1458.16 → 1460.96] And I know a lot of other .NET projects use Git also.
[1462.48 → 1463.32] I mean, for me, I don't know.
[1463.32 → 1464.58] Git just clicked.
[1464.98 → 1466.10] So I stuck with that.
[1466.84 → 1474.82] So, when you're not hacking on Iron.js, what open source projects just have you dying to play with?
[1475.36 → 1477.12] I've been meaning to get more into Node.
[1478.08 → 1480.14] I love the whole async idea.
[1481.14 → 1484.74] And, I mean, obviously, a lot of other people do also.
[1485.62 → 1491.86] I mean, I've been toying with Node, like, a bit on my Ubuntu dual boot or whatever.
[1491.86 → 1493.70] But, I don't know.
[1493.70 → 1503.54] I haven't had time to fiddle around with open source projects for ages because I've been working, and then I've been doing Iron.js for, like, eight hours every day for the past year.
[1503.54 → 1507.76] So, it's like, well, I don't know.
[1508.00 → 1510.48] I do look at some other C Sharp projects, though.
[1510.82 → 1513.88] Like, the Kayak HTTP server.
[1514.60 → 1522.70] I've been meaning to play around with that because that's, like, an integral part in getting the or important part in getting the Node for .NET running.
[1522.70 → 1525.88] As a .NET developer, who's your programming hero?
[1527.18 → 1529.18] Oh, I don't know.
[1529.26 → 1530.22] I have to say Hedgehog.
[1530.28 → 1530.96] I like that guy.
[1531.36 → 1532.62] He's, like, complete asshole.
[1533.76 → 1535.08] But, like, I like him.
[1535.12 → 1535.52] I'm sorry.
[1537.42 → 1538.48] We're fans of Zed.
[1538.54 → 1540.90] Zed was on an episode, a highly edited episode.
[1541.24 → 1545.96] But he plays in a lot of different, I guess, playgrounds.
[1545.96 → 1554.50] I mean, he's made friends in Enemies and Ruby and Python and, I guess, now at least one friend in the .NET community.
[1554.62 → 1557.68] So, what's got you excited about what Zed does?
[1558.58 → 1560.50] I mean, I just like his, like, brutal honesty.
[1561.16 → 1562.00] I think that's what I mean.
[1562.16 → 1563.80] First, he's a perfect programmer, obviously.
[1564.40 → 1567.62] But, I mean, like, more as a persona, like, I like his brutal honesty.
[1567.88 → 1570.60] I mean, he goes overboard a lot.
[1571.22 → 1574.08] But, at least from my perspective, I mean, I've never met the guy.
[1574.08 → 1576.06] But, yeah.
[1576.36 → 1580.32] But if you're talking, like, programming, it would have to be Miguel from Mono.
[1581.38 → 1583.14] I mean, he's such a nice guy.
[1583.22 → 1585.78] And he's, like, so scary smart.
[1587.06 → 1592.50] It's, you know, I mean, at work, you know, like, you think you're the hot shot.
[1592.58 → 1594.68] And then you talk to someone like him, and he's like, oh, God.
[1595.00 → 1598.04] I need to go back to school for 15 years to catch up with him.
[1598.04 → 1604.56] So, since .NET is backed by Microsoft, are most of the thought leaders in the .NET community at Microsoft?
[1604.78 → 1607.82] Or are there other folks in the community that are bearing the standard?
[1608.46 → 1615.06] When you're talking about, like, I'd say if you talk about the core .NET stuff, of course, Microsoft, like, the community doesn't have that much control.
[1615.06 → 1618.90] But if you're looking at F-Sharp, and F-Sharp really is the oddball here.
[1619.48 → 1626.30] There's, like, Don Some, who's also, that's another programming here, actually, who's also, like, insanely smart, who's the main architect behind F-Sharp.
[1626.52 → 1629.40] I think he's also one of the main architects behind generics in .NET.
[1629.40 → 1633.74] But, I mean, the F-Sharp community is very open.
[1634.52 → 1635.80] And, like, there are a lot of discussions.
[1636.04 → 1638.32] And there are a lot of people from the community who are involved.
[1638.62 → 1642.52] Or F-Sharp, I'd say the community has more influence than the other stuff.
[1642.70 → 1646.82] But, like, C-Sharp, VS, and stuff, I think it's, from my point of view, it's on Microsoft.
[1647.28 → 1648.68] And you just have to live with that.
[1649.20 → 1656.36] You know, a lot of the I guess, sharing that happens in the Ruby and Python and Unix communities happens at user groups.
[1656.36 → 1658.44] Or you're involved in a .NET user group.
[1659.40 → 1662.22] They actually spend my time in Sweden, Gothenburg.
[1663.00 → 1665.04] I've been trying to look them up.
[1665.24 → 1666.60] But, I don't know.
[1666.74 → 1668.40] It's, I don't know.
[1668.56 → 1671.32] The thing is, it's mostly, like, those user groups are mostly, like, C-Sharp and stuff.
[1671.40 → 1673.42] I've been trying to, like, find an F-Sharp user group in Sweden.
[1673.56 → 1676.10] But I think we're, like, three F-Sharp programmers in all of Sweden.
[1676.36 → 1676.54] Yeah.
[1677.16 → 1678.94] So, it's, like, I don't know.
[1679.08 → 1681.96] It's, I mean, those are mostly F-Sharp.
[1681.96 → 1685.26] And they usually, you know, they talk about, like, the CMS systems.
[1685.48 → 1688.68] And, you know, like, the client, you know, like, CRM systems and stuff.
[1688.68 → 1692.42] And that's not really, I mean, what I'm interested in as a person.
[1692.74 → 1694.56] You know, I prefer it sort of, like, the open source.
[1694.70 → 1696.30] More than, like, the tech projects.
[1697.16 → 1699.18] You know, like, hacking on compilers and stuff.
[1699.44 → 1703.30] Compared to discussing the latest CRM system released by some company.
[1703.30 → 1706.18] Do you have a favourite F-Sharp feature you would like to see in another language?
[1708.10 → 1710.86] This is a functional feature, but its pattern matching by far.
[1711.14 → 1712.72] Discriminated units and pattern matching.
[1713.54 → 1716.18] Those things are just amazing.
[1716.44 → 1722.12] It's, I mean, those are the two features that made me choose F-Sharp for Irons, basically.
[1723.18 → 1728.06] Because of how easy they make parsing and, like, building syntax trees and stuff.
[1728.06 → 1731.70] How large is the Irons project, roughly, in lines of code?
[1732.40 → 1733.06] It's tiny.
[1733.22 → 1734.72] It's, like, 11,000 lines.
[1735.86 → 1738.12] This is nothing for a compiler or a runtime.
[1738.40 → 1740.42] I mean, the runtime is .NET, but, like, a compiler.
[1740.96 → 1741.86] How many contributors?
[1743.40 → 1746.20] There's me and this guy named John.
[1746.42 → 1748.28] I can't pronounce his name, though.
[1748.38 → 1750.56] I think it's John Gimson.
[1751.40 → 1755.70] He lives in the States, but he has a really funky last name.
[1755.70 → 1757.50] I'm sorry, John, if you're listening to me.
[1758.18 → 1764.92] He helped a lot on the ECMAScript, three conformance tests.
[1766.02 → 1768.66] He did, I'd say, about half the work there.
[1769.04 → 1773.64] So looking at the Irons website and the benchmarks that you've published,
[1774.40 → 1776.66] you mentioned earlier that these were fun.
[1776.84 → 1779.02] So what makes benchmarking fun?
[1779.74 → 1780.04] I don't know.
[1780.24 → 1783.82] Isn't there something inherently fun over being fast?
[1783.92 → 1784.26] I don't know.
[1784.26 → 1786.12] I don't know.
[1786.34 → 1790.24] I think it's, you know, it sort of gives you sort of, like, a receipt of your efforts.
[1790.34 → 1792.40] You know, like, that you actually made something that works and it's fun.
[1793.14 → 1793.96] Fast, I mean, sorry.
[1795.22 → 1798.40] I mean, it's sort of, like, it's the own validation.
[1798.78 → 1802.08] You know, it's, like, I've actually built something, and it works and it runs fast.
[1802.14 → 1805.90] And it runs fast compared to the competition, you know, competition or whatever you want to call it.
[1805.90 → 1814.64] And seeing that little bar decrease even more, I think we're down to 2,900 milliseconds now for all of Sun spider.
[1815.38 → 1818.58] You know, I think you asked me, you know, isn't that fun?
[1818.70 → 1820.24] For me, no, it would not be.
[1820.32 → 1821.66] But, you know, I'm thankful for guys like you.
[1821.72 → 1822.54] So here's the deal.
[1822.54 → 1825.40] I play where the user meets the machine, right?
[1825.56 → 1831.94] And somebody has to have a business benefit for me to get excited about what computing can do for them, right?
[1831.98 → 1837.22] But I am so thankful that guys play at the lower end or the deeper end of the pool, right?
[1837.22 → 1841.10] And do things like this to make the whole effort faster.
[1841.98 → 1842.82] Yeah, I mean, I don't know.
[1842.90 → 1845.38] I just, I don't even really know why I like it.
[1845.82 → 1849.90] You know, like I said earlier, I drive a motorbike in my spare time.
[1850.02 → 1850.12] Yeah.
[1850.20 → 1851.56] And I suppose that goes fast also.
[1851.72 → 1854.48] So there's some correlation there.
[1854.56 → 1855.78] So you just like speed in general.
[1856.28 → 1857.56] Yeah, just speed in general.
[1858.20 → 1862.12] So, Frederick, where can folks go to learn more about Irons and get involved?
[1864.12 → 1866.76] IronJS.wordpress.com or ironjs.net.
[1867.22 → 1873.60] And, of course, GitHub.com slash fall slash irons, which is the main repository.
[1873.94 → 1876.22] And follow on Twitter at irons.
[1877.04 → 1877.30] Yeah.
[1877.76 → 1880.94] And I am fjhallmstrom at Twitter.
[1881.26 → 1882.82] And we'll put all of that in the show notes.
[1883.04 → 1887.94] So thanks much for joining us and telling us a little bit about Irons and Sharp
[1887.94 → 1893.60] and giving us, I guess, a whole slew of projects that we need to have on the show in the future.
[1894.08 → 1894.80] Yeah, thanks for having me.
[1894.80 → 1895.50] It's been a blast.
[1897.22 → 1897.64] I'm out.
[1897.64 → 1899.08] And we'll be right back.
[1899.08 → 1899.82] Thanks for listening.
[1900.02 → 1900.66] I'll see you next time.
[1902.94 → 1904.86] I'll see you next time.
[1904.86 → 1906.42] Bye-bye.
[1908.86 → 1911.00] Please absolutely.
[1911.00 → 1911.86] Bye-bye.
[1911.98 → 1913.26] Bye-bye.
[1913.26 → 1914.12] Bye-bye.
[1914.66 → 1915.30] Bye-bye.
[1915.54 → 1916.96] Bye-bye.
[1917.06 → 1918.08] Bye-bye.
[1918.08 → 1919.22] Bye-bye.
[1919.22 → 1920.00] Bye-bye.
[1920.00 → 1921.02] Bye-bye.
[1921.02 → 1921.98] Start.
[1921.98 → 1922.02] Bye-bye.
[1922.02 → 1922.60] Bye-bye.
[1922.60 → 1923.04] Bye-bye.
[1923.04 → 1923.12] Bye-bye.
[1923.12 → 1923.44] Bye-bye.
[1923.44 → 1923.96] Bye-bye.
[1923.96 → 1924.14] Bye-bye.
[1924.14 → 1925.10] Bye-bye.
[1925.10 → 1925.18] Bye-bye.
[1925.34 → 1926.24] Bye-bye.
