[0.00 --> 3.42]  Greetings Gophers, this is Adam Stachowiak, Editor-in-Chief here at Changelog.
[3.44 --> 6.36]  We're doing something a little different today in the podcast feed.
[6.64 --> 10.24]  We partnered with Red Hat to promote Season 3 of the Command Line Heroes podcast.
[10.88 --> 13.92]  And today we're bringing Episode 5 to our feed.
[14.18 --> 18.78]  It's titled The Infrastructure Effect, Kobol and Go, A Tale of Two Languages.
[19.08 --> 21.10]  This is an original podcast from Red Hat.
[21.26 --> 23.14]  It's hosted by Surmanya Bark of CodeNewbie.
[23.46 --> 27.18]  And to learn more and subscribe, head to redhat.com slash commandlineheroes
[27.18 --> 28.50]  or check the show notes for a link.
[29.02 --> 29.38]  Here we go.
[30.00 --> 44.42]  When the New York City subway first started running in 1904, it was a marvel of the modern age.
[47.24 --> 47.84]  But...
[47.84 --> 54.24]  What happens when today's commuter depends on infrastructure that was designed more than a century ago?
[55.14 --> 57.54]  Trains are packed and often late.
[57.54 --> 62.32]  Two billion subway rides take place each year in New York.
[62.66 --> 64.32]  And nobody's marveling anymore.
[64.90 --> 68.04]  We're tied to yesterday's crumbling infrastructure.
[68.46 --> 71.64]  And we have to find smart new ways to make it work.
[71.64 --> 80.18]  It used to be that infrastructure projects were these big concrete things we could see.
[80.70 --> 81.98]  That subway, for example.
[82.60 --> 88.02]  And because of that physical presence, it was also pretty obvious when they broke down.
[88.80 --> 89.96]  Highways crack.
[90.48 --> 91.74]  Telephone poles fall over.
[92.34 --> 94.52]  We know when those things need fixing.
[94.52 --> 100.66]  Big efforts are necessary to get our lives in sync with aging infrastructure.
[101.30 --> 103.80]  But things aren't always so obvious.
[104.52 --> 107.12]  Today, we also have IT infrastructure.
[107.74 --> 110.30]  Server farms humming in isolated fields.
[110.86 --> 113.06]  Fiber optic cables spanning oceans.
[113.06 --> 115.60]  And software infrastructure, too.
[116.12 --> 117.84]  Like legacy operating systems.
[118.24 --> 120.74]  Or shell scripts that nobody dares to replace.
[121.24 --> 126.48]  When all that IT infrastructure gets old and creaky, we can't see it for ourselves.
[127.26 --> 132.58]  And yet, the infrastructure that makes today's development work possible is aging.
[132.58 --> 134.86]  Just like an old subway track.
[135.30 --> 137.18]  And that can mess with our modern lives.
[137.88 --> 146.24]  Massive new challenges emerge as today's command line heroes work to make sure we're not being boxed in by the past.
[151.98 --> 157.96]  This is episode 5 of our season-long journey into the world of programming languages.
[157.96 --> 164.00]  We're looking at two languages that have intimate ties to the infrastructure they were first designed for.
[164.68 --> 167.64]  COBOL is a language native to mainframe computing.
[168.32 --> 170.00]  And Go is native to the cloud.
[170.58 --> 173.34]  They're both deeply influenced by their origins.
[174.24 --> 180.98]  Understanding that might save tomorrow's developers from ending up like a New Yorker crammed into Penn Station.
[183.14 --> 184.72]  I'm Sarangat Barak.
[184.72 --> 188.04]  And this is season 3 of Command Line Heroes.
[188.30 --> 190.24]  An original podcast from Red Hat.
[192.56 --> 194.98]  So many things ahead that we have to do.
[195.22 --> 197.74]  Well, we need tremendous amounts of information.
[198.18 --> 198.70]  Paraloted.
[199.16 --> 200.16]  Easy to access.
[201.10 --> 202.00]  We're only at the beginning.
[203.56 --> 210.02]  Admiral Grace Hopper pioneered high-level programming languages in the 1940s and 50s.
[210.02 --> 215.32]  And she was able to make that great leap forward because of the infrastructure of her time.
[215.90 --> 217.10]  Mainframe computers.
[217.92 --> 218.78]  Hi, my name's Chris Short.
[219.88 --> 223.96]  Chris is a principal product marketing manager at Red Hat.
[224.28 --> 226.32]  And he's a bit of a history buff, too.
[227.42 --> 230.00]  Admiral Hopper in the 40s made Flomatic.
[230.00 --> 235.30]  And she's widely considered the grandmother of COBOL, which was revolutionary at the time.
[235.58 --> 240.52]  So being able to sit there and say, hey, just put it on the mainframe or, hey, just store it on the mainframe.
[240.92 --> 242.74]  It was a major game changer.
[243.46 --> 249.94]  Suddenly, you've got this machine-independent language, COBOL, that's native to the mainframe environment.
[250.90 --> 252.46]  Possibilities started opening up.
[252.46 --> 263.06]  COBOL with mainframes really gave every organization the capability to say, instead of having a room full of people with pencils and paper and calculators and slide rules,
[263.18 --> 266.14]  they could just have half a room with a mainframe in it.
[266.24 --> 274.26]  And then they could have a few people write some applications in COBOL to do all the math and logic and ledgering that their entire finance team could do.
[274.26 --> 286.60]  So the team of people that you needed to do your finances became a lot less just because a lot more of the input could be digital as opposed to all hand jam in manually.
[287.76 --> 293.30]  If you were one of those new COBOL programmers, it would have felt like you had a job for life.
[293.88 --> 299.74]  Because the infrastructure that your work was based on, all those mainframes, they weren't going anywhere.
[299.74 --> 307.64]  Moore's Law wasn't around back then, so you could go an entire decade working on the same mainframe potentially, right?
[307.74 --> 317.42]  You didn't have to worry about the next operating system or the next type of container orchestrator or the next thing that comes along in AI or whatever.
[317.96 --> 324.48]  You could probably spend your whole career working on COBOL, and you knew you were going to be pretty safe.
[325.36 --> 328.64]  But Moore's Law did arrive eventually.
[328.64 --> 331.50]  New infrastructures showed up too.
[332.10 --> 336.92]  And these days, programmers are less likely to learn a half-century-old language.
[337.62 --> 338.76]  But here's the thing.
[339.40 --> 342.18]  Those old mainframes aren't actually gone.
[342.74 --> 346.82]  And that means our need for COBOL developers hasn't vanished either.
[347.20 --> 350.52]  It's getting a lot harder to find COBOL developers.
[351.00 --> 354.38]  What ends up happening is these mainframes have been here for 50 years potentially.
[354.38 --> 367.24]  And these COBOL developers that still can write good COBOL will get paid exorbitant amount of monies to help with projects and reorganization of data within mainframes.
[367.24 --> 378.90]  And that skill set is definitely dying off and becoming a highly lucrative career field if you can definitely make a lot of money writing COBOL nowadays.
[378.90 --> 387.48]  Especially in the manufacturing and finance industries, you can't outrun all that infrastructure that was laid down decades ago.
[388.14 --> 391.78]  Legacy code permeates work all around the world.
[392.24 --> 397.54]  It'd be a huge mistake to ignore that old infrastructure and the languages tied to it.
[397.54 --> 402.86]  With 200 billion lines of code laying around, it's going to be really hard to refactor all that.
[403.22 --> 407.42]  No, I don't think we'll ever see it disappear in our lifetimes for sure.
[410.86 --> 414.82]  Chris Short is a principal product marketing manager at Red Hat.
[418.26 --> 420.98]  I want to drive Chris's point home for a sec.
[420.98 --> 423.14]  Consider this.
[423.80 --> 428.62]  COBOL is baked into 95% of all ATM transactions.
[429.26 --> 431.14]  That's how tied we are to this language.
[431.90 --> 437.08]  And yet, the average COBOL programmer isn't much younger than the language itself.
[437.72 --> 440.36]  They're 45, maybe 55 years old.
[440.96 --> 442.68]  The newbies aren't interested.
[443.48 --> 445.88]  Which is why I want to introduce you to someone.
[446.60 --> 448.38]  Hi, my name is Rithika Trika.
[449.14 --> 450.86]  Rithika's a technology writer.
[451.38 --> 452.60]  Formerly with HackerRank.
[452.96 --> 455.86]  And she's fascinated by this question of COBOL.
[456.28 --> 461.32]  And the assumption people make that it's a kind of pointless leftover from the mainframe days.
[462.42 --> 465.22]  Developers today are really not thinking about COBOL.
[465.44 --> 466.88]  It's out of sight, out of mind.
[467.70 --> 470.22]  But that could be a recipe for disaster.
[470.84 --> 477.32]  There's a huge volume of COBOL lines of code that are still powering businesses today.
[477.32 --> 482.34]  At least 1.5 billion new lines of code in COBOL every single year.
[482.34 --> 486.78]  And I think when you look at the specific industries, it's really interesting.
[486.78 --> 490.08]  Like, there's 50 million lines of code at the IRS.
[491.40 --> 496.66]  There's 60 million lines of code at the Social Security Administration.
[496.66 --> 504.80]  And so these businesses and entities are handling some of the most sensitive, important information today.
[505.28 --> 512.48]  And if we don't continue to power and maintain these mainframes, it could be really disruptive.
[512.48 --> 522.78]  So if we can't escape our old infrastructure, and we can't wave a magic wand to rebuild the whole mainframe universe, what do we do?
[522.78 --> 529.92]  How do coders, who sometimes only think about the future, start coming to terms with the past?
[530.54 --> 534.06]  We need to start by facing the problem head on.
[535.00 --> 537.88]  You know, younger generations are going to have to pick up these skills.
[538.18 --> 541.46]  Or there has to be some sort of modernization of these mainframes.
[541.64 --> 543.42]  Either way, this problem isn't going to go away.
[543.58 --> 544.84]  That's why COBOL is relevant.
[545.64 --> 547.14]  It's not going to be easy.
[547.94 --> 551.38]  Rithika figures we've ignored the problem for too long already.
[551.38 --> 559.82]  It's incredibly expensive, hard, and the risk is incredibly high to replace billions of lines of COBOL.
[560.24 --> 564.68]  It's mission-critical code like Social Security and financial information.
[565.36 --> 571.48]  And COBOL was specifically designed for these types of large volumes of transactions.
[572.02 --> 577.60]  So it was designed for business transactions by Grace Hopper in the 60s.
[577.60 --> 583.82]  And if it's not broken, why try to fix it has been the mentality since the 60s.
[583.90 --> 591.62]  And now we're at a point where we just have decades of very valuable, high volumes of data running on COBOL.
[591.62 --> 596.34]  In a way, Rithika's calling for a cultural shift.
[596.86 --> 600.02]  A change in attitude about what's in and what's out.
[600.64 --> 605.60]  As the world of development starts to actually gain a deeper and deeper past,
[605.88 --> 609.20]  we have to become more in touch with our own history.
[609.80 --> 611.98]  You can't escape the aging infrastructure.
[611.98 --> 616.80]  And that means you can't ignore the history of languages either.
[617.24 --> 618.40]  Something has to be done.
[619.04 --> 628.68]  You know, when I was at HackerRank, I saw firsthand how many banks and financial institutions are hurting and desperate almost for COBOL developers.
[629.34 --> 631.16]  It's not a problem that's going to go away.
[631.16 --> 639.90]  And I think either there has to be some sort of modernization of the systems or we need to keep training folks and incentivizing it.
[640.02 --> 643.50]  I personally think there's going to be a day where COBOL is actually in again.
[643.96 --> 651.82]  Really, what's going to happen when all of the developers with COBOL knowledge retire and no new younger generations of developers are learning COBOL?
[652.32 --> 653.80]  Something has to give, right?
[653.80 --> 665.26]  So there needs to be more of a systematic and institutionalized change when it comes to shifting away from COBOL and into the new cloud-based infrastructures.
[667.02 --> 671.02]  Rithika Trika is a technology writer based in San Francisco.
[679.16 --> 683.44]  So what about those cloud-based infrastructures Rithika mentioned?
[683.80 --> 692.16]  Are the infrastructures we're building today going to chain future generations to particular languages the way we're still tied to COBOL?
[693.26 --> 699.44]  Amazon Web Services, maybe the biggest single piece of cloud infrastructure, launched in 2006.
[700.10 --> 702.54]  Google Cloud Platform arrived in 2008.
[702.98 --> 705.42]  And Microsoft Azure started in 2010.
[705.68 --> 713.32]  The Go language, with its focus on concurrency, was made to thrive inside all that new cloud infrastructure.
[713.80 --> 715.20]  It's a language of its time.
[715.20 --> 722.68]  Hi, my name is Carmen Ando, and I am a program manager for the Go team at Google.
[723.88 --> 729.52]  Carmen has an insider's understanding of how Go is tied to today's infrastructure.
[730.16 --> 735.78]  It starts with the creators of Go having some strong ties to the history of languages.
[735.78 --> 740.94]  Robert Pike, Robert Griesemer, and Ken Thompson.
[741.40 --> 744.98]  Those names have kind of come through ever since the 1960s.
[744.98 --> 752.98]  So Ken Thompson invented the programming language B, and then he would go on to invent the Unix operating system on a summer off.
[753.62 --> 757.04]  And Rob Pike invented UTF-8, which is a string encoding.
[757.82 --> 759.90]  He also invented ASCII.
[759.90 --> 763.44]  He helped co-author the Unix programming environment.
[763.66 --> 776.94]  So these two had been co-workers for a very, very long time, and they had been looking at and inventing operating systems in previous programming languages, including C, which Ken Thompson would eventually help write with Dennis Ritchie.
[776.94 --> 784.30]  Once Pike, Griesemer, and Thompson were all working at Google, they discovered a serious problem.
[785.10 --> 788.40]  Getting concurrency at scale just wasn't happening.
[789.12 --> 791.94]  People were waiting hours for a bill to compile.
[792.62 --> 797.82]  They were working in C++ and had to write all these callbacks and event dispatchers.
[798.46 --> 802.24]  It was 2009, and our infrastructure was changing again.
[802.24 --> 808.54]  Languages like C++ were becoming less and less in tune with that new reality.
[809.32 --> 818.80]  The problems were being introduced by things like multicore processors and networked systems and massive computation clusters and the web programming model.
[819.28 --> 826.94]  And then also just the growth of the industry and the number of programmers which were going into the thousands and the tens of thousands by 2010.
[826.94 --> 833.88]  And so all the programming languages up until that point were being worked around rather than addressing things head on.
[834.80 --> 838.98]  Eventually, you reach a breaking point, and something's got to give.
[840.12 --> 845.78]  Hey, we hated C++, and they said, well, let's see if we could invent something new.
[846.90 --> 852.40]  That new language would need to be exquisitely adapted to our latest infrastructure.
[852.40 --> 861.88]  What happened with the cloud, which was starting to come of age in 2005, was that you now no longer had to handle your own compute.
[862.12 --> 865.60]  You're sort of renting it elsewhere, and you get a distributed system.
[866.16 --> 873.38]  But what happens in a distributed system and in a cloud is that you have problems of concurrent messaging between distributed systems.
[873.70 --> 878.90]  You need to make sure that you have no problems with asynchronously.
[878.90 --> 883.00]  Go is a programming language that is asynchronous by default.
[883.46 --> 890.66]  Basically, this means that every operation you perform, like sending all these different messages to another in the system,
[890.66 --> 894.76]  it's done without waiting for the other system to respond back to you.
[895.14 --> 898.50]  So it can handle multiple messages at any given time.
[899.08 --> 902.64]  And that said, cloud computing is distributed.
[903.18 --> 906.52]  And so Go was developed to address this exact need.
[906.52 --> 911.84]  Go became, early on, one of the standard ways of doing this kind of distributed computing.
[912.54 --> 917.98]  And that's why I think that it picked up a lot of the developer mindshare immediately.
[918.72 --> 923.70]  Go absolutely is the language of cloud infrastructure, both in its design,
[923.94 --> 934.90]  but also in the ecosystem of all the cloud infrastructure tooling and building blocks that have sprung up in the last decade.
[934.90 --> 940.40]  Soon, major applications like Kubernetes were being written in Go.
[940.80 --> 948.14]  Google also created Go Cloud, an open source library and set of tools that made Go even more attractive.
[948.72 --> 953.10]  It became clear this was the language of a brand new ecosystem.
[953.68 --> 955.20]  It was the language of the cloud.
[955.60 --> 962.08]  And it definitely didn't hurt that the creators had reputations for developing languages that lasted.
[962.08 --> 968.28]  I think that the rest of the industry said, hey, I don't think that this is going to be going away anytime soon.
[968.40 --> 974.98]  And the inventors of the language also happen to invent languages that are now in their 50th year or 60th year.
[976.88 --> 980.78]  Carmen Ondo is a program manager for the Go team at Google.
[980.78 --> 991.88]  So we have a new language, Go, designed to deliver the concurrency that cloud infrastructure makes necessary.
[992.42 --> 993.16]  Sounds great.
[993.66 --> 998.66]  And Go's designers tend to create languages that last for a good half century.
[999.22 --> 999.90]  Also great.
[999.90 --> 1008.06]  But my question is, what will that really mean 50 years from now when Go is more like COBOL?
[1008.66 --> 1015.38]  What will it mean when the world is teeming with legacy Go code that only older developers understand?
[1016.10 --> 1021.34]  Are we going to be prepared for a time when today's cloud infrastructure is aging?
[1021.34 --> 1030.06]  Are we learning lessons from COBOL and the world of mainframe that could help us design a better future for Go and the cloud?
[1030.70 --> 1034.94]  Luckily, I found exactly the right person to ask all these questions.
[1035.44 --> 1036.48]  And that's next.
[1041.48 --> 1043.90]  How do we future-proof our languages?
[1043.90 --> 1047.18]  We know they're tied to the infrastructure of their day.
[1047.62 --> 1054.28]  And we know that new infrastructures are bound to replace the old ones as decades roll by.
[1054.88 --> 1059.30]  So what are we doing today to keep things running smoothly tomorrow?
[1059.96 --> 1061.24]  I'm Kelsey Hightower.
[1061.42 --> 1062.04]  I'm at Google.
[1062.22 --> 1063.30]  I'm a developer advocate.
[1063.90 --> 1068.06]  And I work on bringing open technologies and turning them to products on Google Cloud.
[1068.74 --> 1072.86]  Kelsey spends a lot of time thinking about the future of programming.
[1072.86 --> 1081.70]  I was curious whether one day we're going to end up with another aging group of programmers with these wizard-like skills around Go.
[1082.04 --> 1085.40]  The same way we have a shortage of COBOL wizards today.
[1085.98 --> 1089.22]  Are we even planning for that long-range future?
[1089.94 --> 1092.56]  So Kelsey and I sat down to hash it out.
[1092.90 --> 1093.54]  And so forth.
[1093.90 --> 1098.02]  But if you think about some of the new challenges today, things like dealing with the internet, the network.
[1098.70 --> 1102.56]  You got multiple users, hundreds of thousands of concurrent users.
[1102.86 --> 1106.48]  Different collections of machines and architecture types.
[1107.14 --> 1110.30]  So given those new use cases, typically you want to have a new language.
[1110.42 --> 1112.20]  For example, JavaScript is for the web.
[1112.32 --> 1116.62]  You don't want to retrofit COBOL so that we can start doing web programming with it.
[1116.70 --> 1121.72]  So we have hundreds of languages that are out and pretty well established today.
[1121.88 --> 1124.44]  And they're all kind of hyper-focused on their sweet spots.
[1124.44 --> 1136.98]  So in that case then, do we need to actively push people towards COBOL if we're developing these new languages for these new problems and they're highly specialized and COBOL is still sticking around?
[1137.12 --> 1141.66]  Do we need to encourage folks to pick it up so we can maintain our legacy code?
[1141.66 --> 1144.44]  Well, I think that's going to be a challenge for the enterprise, right?
[1144.52 --> 1152.86]  So you've invested 10, 20 years in COBOL and there is no one actively thinking about learning some new COBOL.
[1153.02 --> 1157.94]  You don't come out of college and it's like, I'm going to double down on this language that's older than my parents.
[1158.60 --> 1164.92]  So in that world, you have to ask yourself, what is the risk of continuing on with COBOL, right?
[1164.94 --> 1166.42]  Is it still relevant going forward?
[1166.42 --> 1173.26]  I think it is still relevant for certain types of workloads, but we have to ask ourselves a question is that, is it time to progress?
[1173.54 --> 1175.44]  Is it time to evolve a little bit?
[1175.54 --> 1185.30]  So if you still have billions of lines of COBOL, yeah, you're in the situation where you're going to have to try to find all the COBOL talent that's remaining and bring them in-house.
[1185.44 --> 1194.50]  But maybe we start to think about what can other languages learn from COBOL and incorporate some of that functionality and libraries into other languages.
[1194.50 --> 1197.24]  Life after COBOL.
[1197.68 --> 1201.58]  That would be an enormous infrastructure project all on its own.
[1202.20 --> 1207.94]  To use my New York subway analogy, it'd be like replacing every underground tunnel.
[1208.76 --> 1216.44]  So going forward, I wanted to know whether we could anticipate those issues and even do our future selves some favors.
[1216.44 --> 1235.22]  If we compare the cloud today to mainframes, are we going to end up in the same boat where we have these legacy code bases that are using kind of old but very stable languages and we have to kind of reach this new point of figuring out if we should move on or stay the same?
[1235.22 --> 1240.18]  So the thing that makes the cloud a bit different, it's not from one manufacturer, right?
[1240.22 --> 1253.92]  A lot of cloud providers typically bundle up collections of technology so you have your choice of programming language, you have your choice of programming paradigm where you want to do event-driven or it's all web services based on, you know, HTTP.
[1253.92 --> 1261.06]  So what that means is you get to choose what you want to program in and just kind of focus on what gets solved.
[1261.14 --> 1265.00]  So data will come in, data will come out, but you choose how you want to process that data.
[1265.86 --> 1268.92]  The mainframe typically just kind of had one main interface, right?
[1268.98 --> 1274.26]  Like you write this job and this is how you submit the job, here's how you monitor the job and here's where it comes out.
[1274.42 --> 1276.22]  So that's very limiting in of itself.
[1276.48 --> 1281.32]  So if you think about some of the newer mainframes, they also support some of the newer technology.
[1281.32 --> 1288.02]  So even in the world of mainframe, you start to see the expansion of programming languages you can use to run your jobs.
[1288.76 --> 1296.60]  So then we start to ask ourselves, okay, given that I have my new choice, when is it time to move on from this particular programming paradigm?
[1296.78 --> 1303.92]  So I think we don't get stuck, but I think it is going to be nice that there's going to be a new machine that's going to be distributed.
[1304.20 --> 1305.78]  Maybe there's a lower cost of entry.
[1305.88 --> 1307.88]  You don't have to buy the whole mainframe to get started.
[1307.88 --> 1313.88]  But we still want that ease of use of, here's my job, you run it for me, tell me when it's done.
[1314.20 --> 1314.52]  Absolutely.
[1315.30 --> 1321.74]  Do you see what's happening or what's happened to COBOL happening to any of today's languages?
[1322.00 --> 1322.84]  Like, for example, Go.
[1322.94 --> 1327.96]  Do you see us struggling to maintain Go and getting folks who want to write Go in 30 years?
[1328.46 --> 1330.50]  I think all languages can suffer that fate, right?
[1330.54 --> 1334.64]  So if you think about it, Python's been around for a very long time, right?
[1334.64 --> 1336.70]  I think it's close to 20 years, if not more.
[1337.84 --> 1341.16]  So I think what happens, and Python's had a resurgence in its usage, right?
[1341.20 --> 1345.64]  It's kind of the foundational language for machine learning, for libraries like TensorFlow.
[1346.04 --> 1351.24]  So if we use just time alone, I think that's probably not the right way to look at it.
[1351.28 --> 1352.98]  It's like, how relevant is that community?
[1353.92 --> 1355.96]  How relevant is that language willing to adapt?
[1355.96 --> 1363.42]  And I think what Python did really, really well, that community saw the ability to make other languages easier to use.
[1363.50 --> 1366.42]  For example, TensorFlow has a lot of C++ underneath it.
[1366.98 --> 1371.42]  So programming in such a language is probably not as user-friendly as something like Python.
[1371.76 --> 1377.70]  And you can take Python and use it to generate some of the stuff that people are using, for example, TensorFlow.
[1377.70 --> 1384.14]  So now that machine learning is hot, people have brung Python into that new space.
[1384.30 --> 1384.90]  So guess what?
[1385.30 --> 1388.54]  Python continues to be relevant and will be relevant for some time to come.
[1388.76 --> 1390.40]  And the same thing is going to be true for Go.
[1390.46 --> 1392.86]  If Go can continue to be relevant, right?
[1392.90 --> 1399.68]  It's like at the foundation of many of our infrastructure tools, many of the cloud libraries, it too will remain relevant.
[1399.88 --> 1404.96]  So I think it's all about those communities ensuring that they have a place in the future.
[1404.96 --> 1407.96]  And when the future shows up, making sure that they have a story there.
[1408.92 --> 1412.32]  So how do we future-proof our languages?
[1412.56 --> 1419.28]  Meaning how do we intentionally design a language to make it last and make it relevant 20, 30 years from now?
[1419.68 --> 1424.34]  The people that use the language, so this is something that's really unique, I think, in the open source space.
[1424.90 --> 1427.64]  Now that we've moved away from commercial languages, right?
[1427.88 --> 1433.04]  Languages used to come from Microsoft or Sun Microsystems in the case of Java.
[1433.04 --> 1442.52]  And at that point, everyone relied on the vendor to do all the heavy lifting about what the language will be able to do, any new improvements in the runtime.
[1443.36 --> 1451.54]  Now what we see with things like Go, Node.js, Ruby, all of these are community-backed and focused runtimes and languages.
[1451.92 --> 1454.36]  So anyone can add new libraries, right?
[1454.40 --> 1456.52]  There was a new HTTP spec, right?
[1456.52 --> 1464.20]  Like HTTP2 came out a few years ago, and each of the respective communities just had contributors at those particular libraries.
[1464.60 --> 1465.36]  And now, guess what?
[1465.44 --> 1470.46]  All of those languages are now compatible with the future of the web for the most part.
[1470.88 --> 1482.16]  So I think it's really now that individuals have more control if they want their language to be relevant for new use cases by just contributing that functionality themselves.
[1482.16 --> 1484.96]  So we're not restricted to one or two companies.
[1485.04 --> 1488.46]  If the company goes out of business, then maybe the runtime dies with it.
[1488.68 --> 1490.88]  We don't have that problem as much anymore.
[1492.76 --> 1494.84]  We've said it on this podcast before.
[1495.28 --> 1496.82]  The future is open.
[1497.48 --> 1503.36]  But it's fascinating to consider how, in another couple decades, the past will be open too.
[1504.14 --> 1508.94]  They'll be inheriting infrastructure and languages that are able to morph and evolve.
[1508.94 --> 1510.78]  Awesome. Thanks for having me.
[1510.98 --> 1512.56]  And I look forward to what people do.
[1512.66 --> 1513.88]  And Mainframe is still relevant.
[1514.22 --> 1515.96]  So we don't call it legacy.
[1516.12 --> 1517.32]  These are classic technologies.
[1517.60 --> 1519.52]  Ooh, I like that. Classic. Very nice.
[1521.44 --> 1524.74]  Kelsey Hightower is a developer advocate at Google.
[1526.82 --> 1531.54]  I'm imagining a future that's rich with classic programming languages,
[1531.92 --> 1535.08]  along with new languages that haven't even been born yet.
[1535.54 --> 1537.44]  That's a future I'm excited for.
[1537.44 --> 1539.44]  And clear of the closing doors, please.
[1541.56 --> 1548.62]  You know, in 2017, Governor Andrew Cuomo declared a state of emergency about the New York City subway.
[1549.46 --> 1554.66]  His government set aside $9 billion to invest in the aging infrastructure.
[1555.28 --> 1560.26]  And that should remind us, sooner or later, we have to take care of the systems we inherit.
[1560.82 --> 1563.36]  You don't just race onward to whatever comes next.
[1563.36 --> 1565.62]  You bring the past with you.
[1567.44 --> 1571.94]  In the world of development, we tend to have a bias towards the future.
[1572.58 --> 1576.86]  We think our languages are only useful in the moment when they're the hot new thing.
[1577.54 --> 1585.24]  But as informational infrastructure continues to age, the history of development becomes more and more real.
[1585.24 --> 1588.74]  The past, it turns out, isn't past at all.
[1589.26 --> 1591.54]  And it's our job to remember that.
[1591.54 --> 1600.04]  You can learn more about COBOL or Go, or any of the languages we're covering this season,
[1600.32 --> 1604.72]  by heading over to redhat.com slash commandlineheroes.
[1604.84 --> 1607.64]  There's a bunch of great bonus material waiting for you.
[1607.64 --> 1611.90]  Next episode is all about Bash.
[1612.14 --> 1616.48]  We're exploring the origins of shell scripts and the key to automation.
[1620.48 --> 1623.94]  Command Line Heroes is an original podcast from Red Hat.
[1625.10 --> 1626.64]  I'm Saran Yitbarek.
[1626.82 --> 1628.92]  Until next time, keep on coding.
[1628.92 --> 1632.28]  rHIndoVant.com
[1632.28 --> 1632.62]  3
[1632.62 --> 1634.14]  5
[1634.14 --> 1634.30]  6
[1634.30 --> 1634.92]  6
[1634.92 --> 1636.30]  7
[1636.30 --> 1637.08]  8
[1637.08 --> 1638.24]  9
[1638.24 --> 1639.42]  10
[1639.42 --> 1639.98]  10
[1639.98 --> 1644.08]  11
[1644.08 --> 1645.48]  11
[1646.10 --> 1646.30]  10
[1646.30 --> 1647.10]  11
[1647.10 --> 1647.68]  12
[1647.68 --> 1647.76]  11
[1647.76 --> 1648.54]  10
[1648.54 --> 1649.98]  12
[1649.98 --> 1650.08]  11
[1650.08 --> 1650.34]  12
[1650.34 --> 1650.80]  13
[1650.80 --> 1651.90]  12
[1651.90 --> 1651.96]  12
[1651.96 --> 1653.20]  13
[1653.20 --> 1653.58]  14
[1653.58 --> 1654.58]  15
[1654.58 --> 1654.64]  16
[1654.64 --> 1655.46]  16
[1655.46 --> 1656.08]  21
[1656.08 --> 1656.14]  18
[1656.14 --> 1656.22]  14
[1656.22 --> 1656.58]  16
[1656.58 --> 1656.80]  18
[1656.80 --> 1657.76]  17
[1657.76 --> 1658.04]  17
[1658.04 --> 1658.82]  15
