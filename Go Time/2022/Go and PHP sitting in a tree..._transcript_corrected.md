[0.00 → 3.76] But if you also know Golang, you can do even crazier stuff.
[3.98 → 8.30] Like you can take, for example, machine learning model from Keras, compress it, put it into
[8.30 → 12.44] the Golang SDK, and then invoke from PHP, and tandem, you now have machine learning
[12.44 → 14.68] embedded directly into PHP via Golang Bridge.
[15.12 → 19.14] So you can do these crazy things if you know multiple languages, specifically Golang.
[19.28 → 22.02] Golang is beautiful because it's quite easy to learn it, right?
[22.04 → 26.18] It doesn't have many of this legacy overhead and nuances you have to remember.
[26.18 → 31.00] So it's not required, but if you do, well, you're essentially a superhero in PHP world.
[35.08 → 38.70] This episode is brought to you by our friends at Source graph.
[38.80 → 41.38] They recently launched a new feature called Code Insights.
[41.70 → 45.12] Now you can track what really matters to you and your team in your code base, transform
[45.12 → 49.38] your code into a durable database to create customizable visual dashboards in seconds.
[49.78 → 52.66] Here's how engineering teams are using Code Insights.
[52.66 → 56.88] They can track migrations, adoption, and deprecation across the code base.
[57.14 → 60.36] They can detect and track versions of languages or packages.
[60.78 → 64.18] They can ensure the removal of security vulnerabilities like Log4j.
[64.46 → 69.74] They can understand code by team, track code smells and health, and visualize configurations
[69.74 → 70.72] and services.
[71.30 → 73.88] Here's what the engineering manager at Prezi has to say about this new feature.
[74.30 → 74.40] Quote,
[74.40 → 99.24] The next step is to see how other teams are using this awesome feature.
[99.24 → 104.38] Head to about.sourcegraph.com slash code dash insights.
[104.62 → 106.12] This link will be in the show notes.
[106.24 → 110.98] Again, about.sourcegraph.com slash code dash insights.
[125.62 → 126.60] Let's do it.
[127.16 → 128.22] It's go time.
[128.22 → 130.52] Welcome to go time.
[130.78 → 133.74] Your source for diverse discussions from around the go community.
[134.14 → 136.60] We record live on Tuesdays at 3 p.m.
[136.68 → 137.00] U.S.
[137.02 → 137.68] Eastern time.
[137.96 → 141.72] Subscribe at YouTube.com slash changelog so you don't miss it.
[141.92 → 144.62] And don't forget to follow the show on Twitter at go time FM.
[144.94 → 149.44] Special thanks to our partners at Vastly for shipping our shows superfast to wherever you
[149.44 → 149.76] listen.
[150.02 → 151.94] Check them out at fastly.com.
[152.18 → 153.38] Okay, here we go.
[158.22 → 163.18] Welcome to this episode of go time everyone.
[163.18 → 165.12] Glad to have you back.
[165.62 → 170.64] So, go and PHP sitting in a tree.
[171.36 → 175.70] I don't know there's, you know, kissing going on, but we're going to figure out why go and
[175.70 → 179.32] PHP are together on this particular episode.
[179.32 → 183.24] Because last time I touched PHP was many years ago.
[183.24 → 187.66] And although it has it had its charms, it did have some quirks as well.
[187.66 → 190.12] And we may touch on those during this episode.
[190.12 → 197.68] But joining me today are two folks who actually work with go and PHP on a regular basis.
[197.68 → 199.64] And that got us curious.
[199.90 → 202.30] Actually, someone actually suggested this episode.
[202.54 → 203.56] I believe.
[203.68 → 204.86] Let me, let me look up there.
[204.86 → 210.34] Oh, I will find who it was and give them a shout-out for suggesting this episode.
[210.34 → 219.74] Shout out to listener SEB for requesting this episode and putting Roadrunner and PHP on our
[219.74 → 220.04] radar.
[220.56 → 221.08] Thanks, SEB.
[223.84 → 227.64] And they actually recommended Roadrunner, which is a project we'll definitely be touching on
[227.64 → 231.56] by name as an example of go and PHP working well together.
[231.84 → 239.92] So, joining me today are two guests, Mr. Valerie, and I'm going to butcher your last name, Piacchansky
[239.92 → 241.14] Did I get that right?
[241.88 → 242.38] Close enough.
[244.18 → 247.00] And then also Anton Tito.
[247.10 → 248.10] Hopefully I got that right.
[248.20 → 248.88] Yeah, that's correct.
[249.18 → 249.72] Nice to meet you.
[249.94 → 250.16] Okay.
[250.80 → 256.18] So, Valerie is a software developer at Spiral Scout, the team that works on Roadrunner,
[256.26 → 258.12] the particular project that we'll be touching on.
[258.34 → 263.34] He enjoys working on algorithms, writing his own operating system for learning purposes in
[263.34 → 267.48] C++, and helping folks get into programming, which is pretty awesome.
[267.48 → 272.56] He also streams on Twitch, mostly open source Go stuff.
[273.20 → 278.66] Anton is actually the CTO and co-founder at Spiral Scout, also on the same team that actively
[278.66 → 280.70] works behind Roadrunner.
[281.24 → 282.86] He loves software and hardware.
[283.12 → 287.12] We were just talking before the show about some of the hardware stuff he's working on
[287.12 → 293.58] with Go, rather than going the traditional route of the embedded stuff with C or Python
[293.58 → 293.92] and whatnot.
[294.32 → 295.60] I got a chance to take a peek at that.
[295.70 → 296.64] Very interesting stuff.
[296.64 → 300.30] He also enjoys some DIY robotics and machine learning.
[300.88 → 302.26] Welcome to you both, gents.
[302.78 → 303.32] Yeah, thank you.
[303.74 → 306.82] I was saying I do not try to pronounce my surname.
[307.82 → 310.16] So it's like rather complicated.
[311.22 → 312.68] But you're almost correct.
[313.62 → 314.38] It's all good.
[314.44 → 314.94] It's all good.
[315.04 → 315.36] Yeah, yeah.
[315.68 → 317.42] So Go and PHP.
[317.80 → 320.76] Let's start with what brought you to PHP.
[320.98 → 324.10] Like why are you working on PHP this day and age?
[324.10 → 326.78] Well, not that there's anything wrong with working on PHP this day and age.
[326.78 → 330.48] I'm saying like, you know, out of all the languages one could pick, PHP has been around
[330.48 → 332.10] a long, long, long time.
[332.28 → 334.06] Like back in the infancy of the web.
[334.16 → 339.40] It was like at some point, PHP was like it language to actually write, you know, dynamic
[339.40 → 340.18] websites and whatnot.
[340.40 → 343.78] Competing with the like of ASP, you know, classic, as we refer to it now.
[343.78 → 348.68] So in the likes of Cold Fusion, I mean, these things are like granddaddies or grand mommies
[348.68 → 349.92] of the early web.
[350.08 → 351.06] What led you to PHP?
[351.48 → 353.90] Well, as you mentioned, it's a very old language.
[354.16 → 358.40] I was young and naive, and I wanted to have my own forum or my own CMS board.
[358.58 → 364.02] And if you're trying to build a forum back in like 05, the only option would be for you
[364.02 → 364.52] is PHP.
[364.92 → 369.86] It's like I remember trying to download the source code of like the website and trying
[369.86 → 371.08] to figure out why it doesn't work.
[371.08 → 375.10] Well, apparently you had to install a bunch of instruments to also make it work.
[375.26 → 378.84] But it's just been the beginning of kind of this long, long journey.
[379.46 → 380.58] And I'm still sticking to that.
[380.88 → 383.38] So it's a beautiful language these days, and it changed a lot.
[383.70 → 384.14] Yeah, yeah.
[384.24 → 384.72] Very nice.
[385.38 → 389.08] So surprisingly, I'm not a PHP developer.
[389.34 → 394.60] So I'm a good developer and working on a whole part of the ecosystem.
[394.96 → 396.86] We're trying to connect into PHP parts.
[396.86 → 402.12] So Anton for me, it's like a light at the end of the tunnel connected to me from the
[402.12 → 402.80] PHP side.
[403.28 → 403.34] Okay.
[403.48 → 407.32] So then you've got the PHP as part of your background.
[407.32 → 409.68] And then here comes a long go.
[409.82 → 414.32] Like when did you get into it, and what led you to actually combining those two things?
[414.88 → 417.96] I can probably talk from kind of combine part.
[418.10 → 421.44] I mean, the goal been around when I was kind of started studying it.
[421.48 → 424.48] It was around for a few years and I only hear like a good thing about it.
[424.48 → 430.52] It's like performance, fast, concurrent, all this kind of terms which now, well, we all
[430.52 → 431.34] know about Golang.
[431.76 → 434.72] Well, I mean, I actually just tried to just play with that.
[434.98 → 437.26] And I played, I made a couple interesting applications.
[437.64 → 443.32] And since PHP was the main kind of production stack, I was just trying to see how I can kind
[443.32 → 444.68] of use it within this practice.
[444.82 → 449.14] Because all the examples on Golang was kind of like small and easy, right?
[449.14 → 454.16] And on PHP, we have frameworks, like 10 layers of abstractions, Ores, and et cetera.
[454.26 → 456.50] So it's kind of very different worlds.
[457.18 → 458.48] So, I mean, it was just curious.
[458.64 → 462.56] It was kind of very curious language for someone who didn't work in this, like this type of
[462.56 → 463.82] language for a very long time.
[464.56 → 467.28] And, well, that has been an idea.
[467.82 → 469.72] Can we actually make them work together?
[469.84 → 472.20] Can we get benefits of PHP and benefits on Go?
[472.20 → 477.12] And can improve the developer experience or our own experience?
[477.58 → 485.60] I came to Spiral Scout, like, in 2018 as just a regular developer on one of the projects,
[485.86 → 486.90] like Golang developer.
[487.46 → 490.38] Previously, I was programming in .NET.
[490.50 → 495.32] So I was heavily involved into .NET ecosystem, like C Sharp.
[495.32 → 501.28] I've got some, like, I guess, 40, 70, 483 exam paths.
[501.44 → 504.28] It's like C Sharp, something like C Sharp Professional.
[504.62 → 511.36] So, and I saw a guy who worked on a very famous taxi company based in New York.
[512.00 → 519.82] So he's rewriting old Ruby on Rails system into some interesting language.
[519.82 → 526.22] So it was, like, 2015, maybe in early days of the Golang.
[526.52 → 528.82] So I, like, what is language?
[529.04 → 533.04] So could you please explain me about what is...
[533.04 → 537.24] So I was really impressed about first web server written in Golang.
[537.34 → 544.92] So it was so little lines of code, and it brings you to, like, a web server that can
[544.92 → 547.78] respond to, like, just hello world, but it just works.
[547.78 → 553.76] After that, I came into, like, SpiralScal was involved into, like, internal projects.
[554.08 → 559.58] And one time, I started to write a test in the error genre.
[560.02 → 561.36] So it was, like, a mess.
[561.78 → 567.16] Because entering from the PHP expertise, like, forgot to turn errors from the functions.
[568.08 → 571.02] Like, there are no errors if you don't return them.
[571.02 → 577.28] Of course, I fixed it, and it was, like, a lot of errors in the tests.
[577.94 → 584.46] And I sent this PR to Anton, and Anton was, like, oh, my God, why you did this?
[585.26 → 586.74] And we, like, okay.
[586.98 → 592.40] We started fixing it, and we eventually, and we finally fixed all these, like, errors.
[592.40 → 598.24] And after that, I was, like, involved into the Golang part of the road genre.
[598.50 → 603.76] And we started working with Anton together to improve the quality, too.
[604.72 → 610.16] Well, he pretty much rewrote most of the parts of it, but that was for the good.
[611.72 → 612.68] Yeah, might be.
[612.68 → 620.40] Obviously, you saw a need, and you decided to fill in and started meeting, doing some of the things that you saw that needed to be done.
[620.98 → 621.66] And that's always awesome.
[621.78 → 625.74] That's how, you know, the majority of open source contributions happen, right?
[625.84 → 630.52] You know, you find something that you enjoy working on, and you contribute code to it, and that's a beautiful thing.
[630.52 → 643.52] Obviously, when I think about my experience with PHP and all sort of the hoops we had to jump through to sort of, to, quote, unquote, make it scale and sort of using today's terminology and whatnot.
[644.04 → 655.34] When I sort of read the description of the project, and I'm like, okay, this is a load balancer rolled into some sort of application server rolled into some sort of, I mean, it's trying to do a lot of things.
[655.34 → 665.96] So why don't we start with what the difference is between plainchant PHP application server, like the last one I was used to was like Zen or something like that.
[666.12 → 667.20] It was a very long time ago.
[667.44 → 668.46] Yeah, exactly.
[668.90 → 670.14] I'm dating myself here.
[670.46 → 680.48] But what's the difference between sort of those, I guess, for lack of a better terminology, those traditional application servers that are designed to run PHP versus this new approach?
[680.48 → 688.48] To answer this question, it's actually important to understand how PHP actually become like this type of language and bottleneck, which is hard to scale.
[688.72 → 694.86] So, like, imagine every time you write that golden-link application, which say, let's say, doing some endpoint on HTTP.
[695.32 → 705.20] Every time you've been getting an HTTP request, imagine that you have to boatload your application from the disk, start it, answer this request, and then kill this application.
[705.32 → 707.46] And do it over and over and over for every request.
[707.88 → 709.54] This sounds super expensive, right?
[709.54 → 714.62] Well, that's how PHP has been working for 26 plus years.
[715.00 → 720.16] And it's quite amazing that you have the tag, which quite literally restarts on every request.
[720.64 → 724.70] And it still kind of powers, like, the pretty much majority of backend on internet.
[725.20 → 726.98] Well, I mean, public backend, let's say.
[727.10 → 727.20] Right.
[727.54 → 731.06] So the idea was actually quite simple.
[731.14 → 732.40] Let's just remove this overhead.
[732.40 → 739.90] I mean, when I started working with Roadrunner, I started working with actually a protocol just making communication between two languages.
[740.02 → 741.74] And the first example was quite simple.
[741.88 → 748.02] Okay, we have, let's say, a function in Holland to do, let's say, some heavy math, which on PHP might be not optimal.
[748.02 → 752.90] And I have this, like, highly OP-strict code in PHP.
[752.90 → 759.82] And by the way, like, modern PHP is all about, like, OP, strict types, annotations, attributes.
[760.06 → 765.94] Like, it's all very, very similar to Java these days, except it's free, open, and very easy to learn, let's say.
[765.94 → 774.12] So then I just tried to make a call from PHP to Holland using this, like, internal socket or Unix socket RPC call.
[774.42 → 775.50] And it did work.
[775.98 → 778.74] And then I tried to make a very stupid experiment, actually.
[778.82 → 783.34] I tried the native PHP library for RabbitMQ to push message.
[783.88 → 787.04] And I used the Holland library for RabbitMQ to push message.
[787.34 → 790.56] But with additional this RPC overhead from PHP.
[790.56 → 802.06] And we ran some tests, and we found out that the PHP to Holland bridge to RabbitMQ works, like, not, like, margin much, but, like, few percent farther than a native solution.
[802.36 → 804.08] And it was, like, that's weird.
[804.76 → 806.32] This shouldn't be happening, right?
[806.78 → 812.30] And this kind of led to the idea that, like, PHP is, like, a very beautiful language to model business processes.
[812.64 → 817.94] Not, like, high-scale I.O. operations, like traffic management or, well, ingresses.
[818.46 → 819.40] It's single-threaded.
[819.40 → 824.32] And it's very dummy, like, in terms of, like, you can go left, you can go right in some cases.
[824.66 → 828.18] You still can shoot yourself to the foot, but these days it's much harder.
[828.56 → 834.26] But it's very good to have good libraries to explain, like, permission models, document mapping, data mapping.
[834.44 → 843.02] If you'll see how to work with mapping JSON in Holland and PHP, you'll definitely see a major difference in favour of PHP because it's, well, dynamic language.
[843.02 → 855.58] And the goal, like, on the other side is beautiful to manage, like, all of these long-porting connections, sockets, like, retries, restarts, delays, all of this fun stuff with PHP just by the definition by model can't.
[855.58 → 861.76] So then we just tried to create the method which has been invoking code from PHP and worker pools.
[861.76 → 867.96] So you have, like, hot processes of PHP, which are already in memory, like, let's say, one per your CPU core.
[868.18 → 872.24] And then you just ask one of them, just do this payload, do this work for me.
[872.40 → 873.74] You don't kill your application.
[873.90 → 874.88] You don't restart it.
[874.96 → 876.04] Like, you have no overhead.
[876.04 → 881.48] And when we did this code, well, it was working, like, 11 times faster than native approach.
[881.66 → 884.96] So we created HTTP layer at top called Roadrunner.
[885.36 → 888.14] And it's been, well, kind of with us since then.
[888.18 → 892.94] And we haven't written a single application without this model probably, like, since 2019.
[893.82 → 893.96] Wow.
[894.50 → 895.40] Yeah, pretty amazing.
[895.90 → 899.04] So who is this for?
[899.68 → 903.80] Is it the Go developer who has to work with PHP or the PHP developer who has to work with Go?
[903.80 → 906.68] Or who are you targeting with this approach?
[906.98 → 907.78] I guess both.
[908.44 → 909.04] Both of them.
[909.62 → 911.78] Well, it's actually a very good question.
[911.94 → 914.20] I mean, the main auditor is obviously PHP people.
[914.38 → 926.24] Because what the main idea of Roadrunner is, like, you can take these complex aspects of, like, queue load balancing, HTTPS traffic, temporal gRPC, and you're going to make them boring for these developers.
[926.66 → 927.56] But just out of the box.
[927.64 → 928.62] You want gRPC, sure.
[928.78 → 929.72] Just plug and play.
[929.80 → 931.58] You want a temporal, sure.
[931.70 → 932.82] Like, it's already here.
[932.88 → 933.60] Just make it work.
[933.60 → 934.64] You don't need to install anything.
[935.04 → 937.78] It basically manages the complex stuff for you.
[937.78 → 945.34] But at the same time, it's kind of for the Go link engineers who typically work in pair or on the same team as PHP engineers.
[945.84 → 953.10] Because this is application server, like, it's very easy to intercept and modify the requests and calls which you do with PHP.
[953.10 → 957.28] So, like, you can add your own validations, like, author indications.
[957.28 → 964.16] And all obviously going to work much faster and possibly, like, with much deeper integration with modern, like, cloud native tools.
[964.26 → 969.06] You have metrics, you know, readiness, healthy endpoints.
[969.06 → 974.10] Like, all the stuff you need to make application, basically, like, native to the current environments.
[974.10 → 980.64] But obviously, the first target auditorium, well, it's just engineers and companies who are just trying to write scalable code.
[981.16 → 985.08] But at the same time, don't necessarily want to hire, like, 10 Rust engineers.
[985.42 → 994.40] Like, it's more like a balance between price for the engineer and how fast you can find them and the performance and quality of the software you create.
[994.40 → 998.16] Okay, so this is as much a technical decision as it is a business one.
[998.32 → 1005.40] Well, in a long term, yes, because how many startups you've seen which come to the point we're going to scrap out PHP and move to something else?
[1005.52 → 1006.28] It's been a bunch.
[1006.70 → 1006.80] Right.
[1007.16 → 1009.20] Facebook invented their own language, you know.
[1009.30 → 1009.52] Right.
[1009.88 → 1010.26] Hack.
[1010.66 → 1015.30] And we've contacted their, there are some Russian competitors who did the same thing, you know.
[1015.30 → 1017.64] So it's kind of, like, become so expensive.
[1017.64 → 1021.64] So you even have to jump in and make your own compiler for this stuff.
[1021.64 → 1028.66] And we can just move this line when you have to move from one tag to another, ideally up to infinity.
[1028.96 → 1032.06] Just if you need something fast, do it in other language.
[1032.20 → 1035.18] I mean, it's all about microservices these days and C-Bit applications.
[1035.46 → 1037.44] So, like, you're no longer stuck to one language.
[1038.02 → 1040.64] But at the same time, well, you're a startup.
[1040.86 → 1048.02] You're trying to integrate with a few providers, and you need to create 12, 15 API endpoints.
[1048.70 → 1050.64] Like, who are you going to be using for that?
[1050.64 → 1053.62] Do you really want to hire senior engineers who's going to be doing that?
[1053.68 → 1060.20] Or you can just use senior PHP engineers, which is much higher, like, availability since it's so old language.
[1060.58 → 1064.04] We're going to do the same thing, which is going to work the same on the same performance.
[1064.26 → 1067.50] Well, it's just going to be done easy because you can source people easier.
[1068.34 → 1068.74] Yeah.
[1068.74 → 1085.92] And at the same time, if you wanted to do some pretty hard work or some low-level stuff, you can easily write a simple plugin and plug it into Roadrunner, compile it, and solve your needs with that.
[1085.92 → 1089.38] So, we also write our own plugin system.
[1089.60 → 1094.58] Because, so, initially, we wanted to use, like, Golang native plugin system.
[1094.68 → 1097.14] You know, it works only on Linux at the moment.
[1097.14 → 1103.82] So, we waited a little for the Windows support, but I guess it doesn't seem to happen.
[1104.16 → 1107.16] So, the Windows support for Golang native plugins.
[1107.16 → 1121.86] But we wrote our own plugin system called Endure, which is suitable for, like, plugging all the pieces of Golang, combining into one part, like, initializing it, starting to serve it, stopping.
[1122.18 → 1125.26] So, building a tree with all of those plugins.
[1125.26 → 1141.84] So, you can, for example, if you write once a configuration parser, for example, if you write, like, a parser from the YAML, for example, you don't need to write or copy or create some SDK to bring this part into every plugin.
[1141.84 → 1145.00] So, you can just request this unit function.
[1145.72 → 1155.80] And Roadrunner will take care about finding this dependency, initializing it, topologically sorting the graph, and providing this initialized dependency for you.
[1156.04 → 1162.48] You only need to just, okay, configuration, please give me the gRPC section or give me some other section.
[1162.48 → 1178.52] So, if something goes wrong, Roadrunner will take care about this, of course, and, like, provide you, like, nice but unreadable for PHP users message about, like, going to some panic or some errors, something like this.
[1178.90 → 1187.46] And for the PHP, all complexity for the PHP user is to properly define what do you need in the configuration.
[1187.46 → 1197.50] Like, you have a configuration, you need HTTP, so you just enable HTTP section, put your configuration, and Roadrunner will remove all other plugins from the tree.
[1198.02 → 1199.86] Like, it won't even start.
[1200.50 → 1204.02] It just runs your section for your needs, like HTTP.
[1204.56 → 1205.30] Or gRPC.
[1205.46 → 1211.46] Or you can write your own plugin, put your section in the configuration, build with our tool called Velum.
[1211.46 → 1218.30] Velum is a tool which helps you to build Roadrunner with your own custom plugins based on GitHub.
[1219.38 → 1232.20] So, it's all of this heavy, complex stuff was moved to the Golang part, and the open, nice things moved to, like, PHP.
[1232.20 → 1240.82] That's actually quite an exchange of knowledge, because this first container actually came, like, as architectural pattern in most of the PHP applications.
[1241.40 → 1246.56] Because if you've seen .NET, Java, PHP applications, you have a ton of classes, interfaces that inherit each other.
[1246.94 → 1249.78] They, like, use class declarations etc.
[1249.90 → 1251.98] So, like, you can't work without container.
[1252.20 → 1254.80] And it being dependencies, you need to manage all of this stuff.
[1254.80 → 1260.80] So, like, essentially, we use this idea inside of Roadrunner, but obviously, it's the Golang favour tool.
[1260.92 → 1263.46] Initiate it, lays it all correctly in the correct order.
[1264.10 → 1267.30] And answering the question, like, how, like, it's a large tool already.
[1267.70 → 1273.04] Well, it's kind of not, because it's just a container with a bunch of, like, CLI tools and instruments.
[1273.52 → 1276.80] And the rest is just kind of, like, independent projects and plugins.
[1277.08 → 1282.80] So, we can add them without kind of influencing on each other or worrying to break the tool.
[1282.80 → 1284.76] Do you want Roadrunner with HTTP layer? Sure.
[1284.92 → 1287.48] If you don't, well, disable the plugin and build it.
[1287.58 → 1290.98] It's going to be exactly the same thing, just less memory to manage.
[1303.92 → 1307.74] This episode is brought to you by our friends at Fire Hydrant.
[1308.04 → 1310.80] Fire Hydrant is the reliability platform for every developer.
[1310.80 → 1315.02] For incidents, they impact everyone, not just Sees.
[1315.26 → 1322.90] They give teams the tools to maintain service catalogues, respond to incidents, communicate through status pages, and learn with retrospectives.
[1323.26 → 1328.68] What would normally be manual, error-prone tasks across the entire spectrum of responding to an incident,
[1328.94 → 1332.18] they can all be automated in every way with Fire Hydrant.
[1332.18 → 1337.52] They have incident tooling to manage incidents of any type with any severity with consistency.
[1338.04 → 1341.18] Declare and mitigate incidents all from inside Slack.
[1341.56 → 1347.90] Service catalogues allow service owners to improve operational maturity and document all your deployments in your service catalogue.
[1348.48 → 1355.86] Incident analytics allow you to extract meaningful insights about your reliability over any facet of your incident or the people who respond to them.
[1355.86 → 1360.18] And at the heart of it all, incident run books, they let you create custom automation rules,
[1360.40 → 1365.64] convert manual tasks into automated, reliable, repeatable sequences that run when you want.
[1366.02 → 1370.02] You can create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1370.50 → 1373.08] Now your processes can be consistent and automatic.
[1373.08 → 1375.22] The next step is to try it free.
[1375.36 → 1379.74] Small teams, up to 10 people, can get started for free with all Fire Hydrant features included.
[1380.06 → 1381.48] No credit card is required.
[1381.92 → 1384.10] Get started at FireHydrant.io.
[1384.42 → 1386.38] Again, FireHydrant.io.
[1403.08 → 1406.02] Let's dive in a little bit into the weeds, if we will.
[1406.36 → 1408.66] Are you shipping a binary?
[1409.04 → 1410.88] Are you interpreting PHP?
[1411.40 → 1415.92] If I'm a developer, what does my experience look like?
[1416.06 → 1420.66] So from a PHP perspective, we're trying to do the less invasive work possible.
[1420.86 → 1424.08] You literally don't need to do anything to make it work from a PHP side.
[1424.44 → 1425.22] There are no extensions.
[1425.58 → 1428.20] There's no special CLI's, interpreters, nothing.
[1428.20 → 1435.84] What we actually do, we do the 20, 30 years old approach, which still drives all the applications.
[1436.38 → 1437.62] We manage the worker pool.
[1437.90 → 1443.38] So what Word Runner does, it actually uses the default PHP interpreter, which is a binary,
[1443.94 → 1449.08] invokes it with your application, and then keeps it in memory in a pre-warmed state.
[1449.08 → 1457.48] And when the request payload comes, which can come for HTTP endpoint, task queue, temporal workflow,
[1458.04 → 1463.14] gRPC, whatever, you name it, you just send this payload to PHP and wait for it to complete.
[1463.46 → 1468.76] But over the lifetime, the only main difference for the engineer, which is, well, for some engineers,
[1468.86 → 1474.38] it's quite hard, is to realize that your application leaves longer than just a single request.
[1474.38 → 1481.24] And you can't just have a global variable counter, which is going to plus and expect it's going to be zero on the next request.
[1481.84 → 1482.80] That's the only difference.
[1482.88 → 1489.22] But besides that, it's just the same exact PHP, same exact extensions, configurations as you typically use.
[1489.54 → 1491.56] It's just managed in a bit of different flavour.
[1491.90 → 1495.98] But surprisingly, Word Runner knows nothing about the PHP.
[1496.66 → 1500.04] So Word Runner is not bound especially to a PHP.
[1500.04 → 1504.80] It just runs some command you specify in your configuration.
[1505.02 → 1506.64] So you can do it in Python.
[1507.22 → 1513.16] You can even run Golang inside the Golang, like Golang inside the Golang workers.
[1513.50 → 1517.48] So the main purpose for the Word Runner is to manage the process.
[1518.06 → 1519.52] Who will be in this process?
[1519.80 → 1522.40] So for the Word Runner, it doesn't care about it.
[1522.54 → 1524.30] It cares about the protocol.
[1524.74 → 1526.84] So protocol is language agnostic.
[1526.84 → 1532.60] So I saw a project, some guy wrote this, implemented this protocol in Python.
[1533.04 → 1536.02] Anton showed me like some time ago.
[1536.22 → 1539.08] So it's like Python running inside the Word Runner.
[1539.36 → 1544.42] So because it's the same, pretty the same model, like the one-threaded model in the Python.
[1544.60 → 1548.16] So some guy wrote this in and yeah, so it works.
[1548.62 → 1551.30] This sounds like a process manager, if you will.
[1551.30 → 1561.74] So if you wanted to, you could have Python, obviously, as you just mentioned, Ruby, obviously, PHP natively, and whatever else other sort of interpreted languages you want.
[1561.88 → 1567.00] Like even like pre-compiled things, it sounds like you can just have in there and then basically just invoke it.
[1567.26 → 1571.42] In theory, you can take 20 years old Perl file and run it in the Word Runner.
[1571.42 → 1574.96] But if you want to do it, obviously, that's a good question.
[1575.34 → 1580.36] But yes, I mean, I think the only mention, main mention of PHP is actually the title of Word Runner.
[1580.46 → 1582.02] It's a PHP application management server.
[1582.24 → 1586.42] But besides that, there's nothing which actually ties it specifically to single language.
[1586.78 → 1592.24] Except that the single language has the largest SDK code base to communicate with all the features from Word Runner.
[1592.50 → 1594.58] But they're just a nuance, quite frankly.
[1594.58 → 1607.08] Okay, so if I'm used to working with single process PHP style application, I think you touched on this earlier, where it's like I'm restarting the world traditionally when I'm dealing with PHP.
[1607.32 → 1611.46] One request just restarts the world, and basically it's like everything is like a new, right?
[1611.46 → 1625.22] In this world where instead there's a worker pool, there's a process management happening, do you find that developers have to sort of have a mindset shift to basically to think, okay, there's not just one process here, there's multiple.
[1625.54 → 1629.58] So does that change sort of the nature of how they program?
[1629.70 → 1634.60] Do they switch from programming, I guess, a single process to now having multiple processes to contend with?
[1634.94 → 1638.06] Well, I mean, when PHP runs on scale, you still have multiple processes.
[1638.06 → 1644.06] They just create it on demand, but you still have like 500 PHP processes running the request.
[1644.42 → 1648.26] But there is definitely the kind of conception shift in people.
[1649.06 → 1651.38] It's been much harder earlier, like even a year ago.
[1651.56 → 1657.68] But now, like the main reason why it's easy these days is that very minimal amount of people write on pure PHP.
[1658.26 → 1661.52] Unlike Golang, where most of the time you write on pure Golang because you can.
[1661.52 → 1669.48] Like you may be like using some small HTTP overlay framework, but mostly you're going to be using SPL functions, let's say, to do most of your business stuff.
[1670.04 → 1671.26] In PHP, it's completely different.
[1671.58 → 1677.78] You have Symfony or Laravel or our infrastructure framework, Spiral, and they're all managed for you.
[1677.78 → 1692.60] So the beautiful thing is that all of these frameworks over the time, well, we created our own specifically for this purpose, but all other frameworks, they actually do upgrades and patches, which solves all of this kind of thinking nuances for the engineer.
[1692.98 → 1696.40] They reboot some parts of the services, like clean up the caches and et cetera.
[1696.40 → 1705.16] So if you're using modern framework and if you're using Roadrunner, you most likely won't even notice a difference in like 90% of your activities.
[1705.44 → 1710.86] It's still going to be some nuances, but most of them are already known and have already been solved.
[1711.08 → 1716.60] If you're using framework which specifically built for Roadrunner like ours, nothing is different for you.
[1716.66 → 1723.10] Just write code, and it's all been managed and like status managed in memory and all completely reset it.
[1723.10 → 1729.60] So would a PHP developer ever even need to know what's under the hood, what's running their processes?
[1729.92 → 1734.00] I assume they'll never really come in contact, unless they want to, like to come in contact with any go whatsoever.
[1734.26 → 1737.80] Well, it's like owning a car and being able to drive a car, right?
[1737.90 → 1744.30] If you have Roadrunner on PHP and default PHP SDK, you can do many, many like wonderful things.
[1744.30 → 1753.52] You can make PHP respond in like 50 microseconds, like run on the all realms and all the queries, use your PC and like use and all of this stuff.
[1753.78 → 1757.92] But if you also know Golang, you can do even crazier stuff.
[1758.12 → 1765.20] Like you can take, for example, machine learning model from Keras, compress it, put it into the Golang SDK and then invoke from PHP.
[1765.38 → 1769.46] And to the end, you now have machine learning compared to PHP via Golang Bridge.
[1769.46 → 1774.06] So like you can do these crazy things if you know multiple languages, specifically Golang.
[1774.26 → 1778.50] And Golang is beautiful because it's so, I mean, it's quite easy to learn it, right?
[1778.56 → 1783.46] It doesn't have many of this legacy overhead and nuances you have to remember.
[1783.90 → 1788.98] So it's not required, but if you do, well, you essentially are a superhero in PHP world.
[1789.88 → 1791.94] Yeah, and also your Hardware project, Anthony.
[1792.20 → 1794.48] Well, yeah, that's another example how you can use it.
[1794.52 → 1797.46] It's also written here in Roadrunner and PHP combination.
[1797.46 → 1801.78] I can show it when it's going to be the right time up to you, Johnny.
[1802.62 → 1809.88] Well, you know, given that most of our users are going to be listening, not viewing this, we may not be able to show them much.
[1810.00 → 1811.32] I'll try to walk it through, yeah.
[1811.52 → 1817.40] I do want to sort of understand, obviously this is an open source project and folks are contributing to it.
[1817.76 → 1826.02] I do want to understand sort of what are some of the hardest challenges that you encountered, like while sort of coming up with this model.
[1826.02 → 1833.90] Obviously, you're running a process manager, you have to worry about inter-process communication, you have to worry about sort of how to keep things in memory efficiently and all that stuff.
[1834.02 → 1839.20] You know, I'm curious as to sort of what are some of those biggest challenges and perhaps that you're still facing.
[1839.20 → 1844.50] I think, I mean, about the current challenges, what I can speak, I don't think we're facing like a lot of them now.
[1844.64 → 1849.82] But when we started working on this tool, it's been a number of interesting things to solve.
[1849.90 → 1854.42] Well, number one, we had to create a protocol to communicate within two different languages.
[1854.42 → 1858.28] And I had to work over pipes, over Unix sockets and TCP sockets.
[1858.28 → 1867.64] So it's been like, okay, how are we going to create a low-level IPC protocol if you don't want to jump to like shared memory or all of these things?
[1868.24 → 1874.82] This being not like a hard conceptual problem because you can always like, default protocol is like net string.
[1874.94 → 1881.12] You have the lengths of the message with like in a fixed head size, and then you have the payload board.
[1881.12 → 1884.66] So it's quite easy to just read the package between languages.
[1885.08 → 1893.68] Then obviously it was a problem with doing process manager because PHP sometimes tends not to start if you don't send it right parameters, or it might crash.
[1893.84 → 1897.28] If again, you send an invalid payload, I mean, doesn't do it anymore.
[1897.40 → 1902.22] It's been like a demo builds and obviously raise conditions on Goal inside.
[1902.70 → 1906.20] Oh, that was horrible because you can't just write a process manager.
[1906.36 → 1908.16] No one just writes a process manager.
[1909.36 → 1910.50] Sorry for the reference.
[1910.50 → 1912.36] You also need to collect the stats.
[1912.52 → 1914.64] You also need to watch for the process to restart.
[1914.86 → 1917.80] You need to collect the SDR, right?
[1917.84 → 1922.48] You need to understand how many times you invoked it, when it was started.
[1923.02 → 1925.84] It thinks like, okay, let's check how long this process exists.
[1926.42 → 1930.14] And you call, let's say, time now and you immediately kill your performance, right?
[1930.16 → 1934.10] Because it's doing a miscall, well, back in the day, something like that.
[1934.38 → 1939.40] Or, for example, you have a request coming, but at the same time, the PHP process runs out of the memory.
[1939.40 → 1943.08] So what's going to happen is going to fail.
[1943.54 → 1944.56] How are you going to start?
[1944.56 → 1952.28] It's going to be, it's been so many like little international hell and edge cases for this type of work.
[1952.44 → 1957.92] But like, eventually, like once we jumped from this part, what we managed is another part of the hell.
[1958.30 → 1963.10] When you have a single server, which has HTTP endpoint, everything is quite easy, right?
[1963.14 → 1968.38] You have request, pack it into the binary form, send to PHP, and well, Bob's your uncle.
[1968.38 → 1975.76] But when you're doing HTTP, and then you also want to manage the queue process manager, like cooperate with RabbitMQ.
[1976.30 → 1983.42] But what happens, what if you have HTTP, which runs a PHP worker, which sends data to queue?
[1983.42 → 1994.88] So now you have two plugins, which not only have to work, they also have to be created in a correct order, wait for each of them to properly connect, and only then make it work.
[1995.06 → 2000.08] So like, that was a part of like scratching the head a lot, because it was so hard to solve.
[2000.48 → 2007.22] With all these dependencies and plugins and hidden dependencies, because like PHP worker can theoretically do anything which it wants.
[2007.22 → 2017.24] It's like, it can call to queue, and it can invoke HTTP endpoint through the roadrunner to itself, which is, well, I'm not even sure what's going to happen in this case.
[2017.88 → 2020.02] But that's why we created the container.
[2020.22 → 2023.46] That's what we contributed to eventually Endure, which solves all these problems.
[2023.72 → 2029.38] And now, like, there is barely no international hell between like plugins and Roadrunner.
[2029.50 → 2033.10] They all like have interfaces, very easy to connect them together.
[2033.38 → 2036.54] It's basically become a framework for the application server.
[2036.54 → 2050.56] So if you have this deployed, is it recommended basically that you have basically a single tenant kind of situation whereby you don't want sort of processes from multiple parties that are not really associated with the same, say, the same company, right?
[2050.56 → 2062.54] You don't want to run this as some sort of, you know, open to all multi-tenant sort of system, because you could have one process sort of peeking in into what's happening with another process within this sort of, within this world.
[2062.54 → 2066.58] Or is it isolation between these things running all in the same system?
[2066.88 → 2067.96] Well, it could be.
[2068.30 → 2071.36] We can isolate it by many different ways.
[2071.46 → 2075.38] We can isolate them by running with different permission models in PHP.
[2075.50 → 2081.26] You can literally forbid most of the functions, which, well, some engineers and hackers will still be able to bypass.
[2081.88 → 2085.30] You can run them in different user groups and user in different memory spaces.
[2085.30 → 2091.28] I mean, right now we don't run it in like shared fashion, like old-fashioned shared hostings.
[2091.50 → 2094.52] It's mostly suitable for the most classic approach now.
[2094.62 → 2095.38] You have a container.
[2095.86 → 2102.10] Within this container, you have your application, your APIs, or like other service functions of this application.
[2102.46 → 2105.30] And it's fully self-contained inside this container.
[2105.30 → 2110.80] If you work on a multi-tenant model, you don't run 10 different PHP scripts with different users.
[2110.98 → 2116.50] You solve the multi-tenancy on the, well, application design level within your application domain.
[2117.12 → 2117.90] I hope it makes sense.
[2119.00 → 2121.14] But I've been thinking about this problem for a while.
[2121.72 → 2125.54] Basically, in short, if you want to do the multi-tenancy, you're doing it in your application code.
[2125.78 → 2132.40] Roadrunner is designed to actually work the best in modern, like, Docker environment or container-based environment.
[2132.40 → 2135.84] It's a single application per application instance, let's say.
[2136.08 → 2139.14] Single instance of Roadrunner per or single instance of application, sorry.
[2139.34 → 2139.78] Gotcha.
[2140.20 → 2140.40] Yeah.
[2140.56 → 2146.72] And I guess, as for me, it was a lot of challenges in, like, to write all these things.
[2147.10 → 2154.40] Because basically, Roadrunner, as you can see in, like, Roadrunner repository, is just a CLI interface.
[2154.40 → 2158.44] So it's just a Roadrunner server, Roadrunner workers command.
[2158.80 → 2163.62] But everything is hidden under the main, I guess, three parts.
[2164.20 → 2167.14] Those parts are, it's Azure, as Anton mentioned.
[2167.42 → 2169.72] It's like, it was a surprise for me.
[2169.84 → 2172.70] Because, you know, in Golang, we don't have any containers.
[2172.70 → 2184.60] So we, because we just don't need them to get something dependency or, so I heard about some project in Uber, like Uber FX or Google Wire, I guess.
[2185.04 → 2187.70] But I don't think it's many popular solutions.
[2188.72 → 2192.22] So in my project, I never, I worked with a container.
[2192.22 → 2198.42] But BHP is everything about containers and everything about dependency injection and so on.
[2198.44 → 2205.44] So we have to write such algorithmic container, which, like, mutate based on the configuration.
[2206.04 → 2209.04] So it's not like, please give me some dependency.
[2209.66 → 2212.60] It's about, I have a configuration.
[2213.18 → 2217.36] I have a set of, I guess, at the moment we have 20 plugins or more, I guess.
[2217.50 → 2219.96] I don't know how much exactly.
[2219.96 → 2227.26] But you provide a bunch of plugins, like provide a configuration and say, okay, now build this.
[2227.76 → 2231.44] Build this properly, managing the connection, as Anton says.
[2231.84 → 2239.08] Like, if you provide, for example, initialize, like, a logger and logger needs a configuration.
[2239.56 → 2246.84] So you have to properly topologically sort all the things to provide first, to initialize first, like, configuration.
[2246.84 → 2250.22] Then provide this pointer to logger.
[2250.86 → 2258.52] So the Golang race flag won't help us here because it's so distributed all over the plugins.
[2258.52 → 2264.08] So you have to manage and see every, like, race condition by yourself.
[2264.40 → 2269.16] So you have to be very careful with writing all the things.
[2269.50 → 2273.02] But we hide all this complexity inside the Endure.
[2273.36 → 2278.74] And you have to be sure that provided dependency is, like, concurrent free.
[2278.96 → 2279.12] Yeah.
[2279.12 → 2282.48] So you can't, like, use it from the different threads.
[2283.18 → 2285.64] But the second part is also Go rich.
[2286.08 → 2287.10] It's a protocol.
[2287.58 → 2290.02] It's in Go rich version 1 and version 2.
[2290.14 → 2293.12] It was, like Anton said, it's a very basic protocol.
[2293.50 → 2297.24] Like, I guess, 14 bytes of, correct me if I am wrong, Anton.
[2298.02 → 2299.68] 14 bytes or 18 bytes.
[2299.68 → 2303.18] So the first person had 17 bytes heaters for whatever reason.
[2303.38 → 2304.66] 17 bytes, yeah.
[2305.08 → 2311.66] It's, like, a few flags, like, payloads in Big Indian, Little Indian, and payload.
[2312.26 → 2317.02] But imagine the situation if you pass your payload over the pipes, for example.
[2317.46 → 2326.26] You don't have any mechanism to CRC or to check if this payload is correct, passing it from the one side of the wire to another.
[2326.26 → 2334.14] But Roadrunner and Go rich version 3 has a protocol based on IP protocol.
[2334.28 → 2347.38] So I've written, recently, a few protocols, like TCP IP, IP protocol, and combined them all together to have a proper protocol for communicating with PHP parts.
[2347.52 → 2349.56] So we have, like, a synchronic support.
[2349.86 → 2352.88] We have a header length, like in IP protocol.
[2353.04 → 2354.94] We have variable length options.
[2354.94 → 2361.94] So we have all this funny stuff to extend it and not to break it from version to version.
[2362.84 → 2368.74] And I guess the third part is decay, which contains all these worker pools.
[2369.08 → 2375.56] And this is complicating stuff because, you know, you have to, for example, imagine you have an HTTP plugin enabled.
[2375.92 → 2378.48] The user want to get a statistic about the workers.
[2378.48 → 2382.08] So the one approach is to stop the world.
[2382.70 → 2390.76] Okay, stop all the HTTP requests and get all the statistics about, like, get all the pointers to workers.
[2391.22 → 2395.02] Get the stat, print it with some format and show to the user.
[2395.02 → 2406.50] And another approach is to have some shared place where you can safely get at any time, like, without logs, even, this pointer and to provide to user.
[2406.72 → 2412.32] But when the restart happens or some issue happens, it will log only in this case.
[2413.20 → 2415.34] So it's like statistics in the Roadrunner.
[2415.34 → 2417.02] It's basically free for users.
[2417.02 → 2419.80] It's not interrupt the actual request.
[2420.26 → 2422.64] I mean, not HTTP, not jobs.
[2422.94 → 2424.76] So it's none of them.
[2425.02 → 2428.36] It's quite funny how it actually, how we jump into this edge cases.
[2428.54 → 2434.92] Because most of our users are actually, like, already mature PHP applications and, like, large, large startups.
[2435.20 → 2437.38] And, like, they don't play with, like, 10 requests.
[2437.50 → 2439.80] Like, okay, I mean, we just bump a few millions a day.
[2439.80 → 2441.12] And we see this bug.
[2441.22 → 2442.08] So what is bug about?
[2442.20 → 2442.90] Oh, you know what?
[2443.10 → 2447.98] Over time, it's, like, things which you could never imagine while developing the thing.
[2448.26 → 2452.34] But when they catch them, thankfully, the user reports them.
[2452.84 → 2456.46] It's just easy to, like, it's kind of very easy to see how it works on scale.
[2456.74 → 2456.92] Yeah.
[2457.34 → 2462.42] And basically, imagine a situation when you have a completely fresh scheduler in Go link.
[2462.60 → 2465.18] So I guess you saw this ticket recently.
[2465.64 → 2469.00] It's about to write a completely fresh scheduler.
[2469.00 → 2480.40] So we started working with that, I guess, a year before to provide a completely fresh scheduler to schedule jobs inside the Roadrunner.
[2480.62 → 2484.36] So we don't finish it yet, but we're continuously working on it.
[2484.88 → 2490.12] So to provide, like, a binary Hips algorithm to sort by priorities all of these jobs.
[2490.12 → 2500.58] Like, for example, if you have an urgent job to execute, you have to set the priority one, and it will be sorted and scheduled properly.
[2500.58 → 2512.02] So there are a lot of such things, very complicated things, which you should work inside the Roadrunner and hide all of this complexity for users just to specify a few values in the configuration.
[2512.26 → 2514.94] Just, okay, I don't need a gRPC, so it's removed.
[2515.08 → 2517.96] But all of this complexity hidden under the hood.
[2517.96 → 2522.32] That's why it's hard to create very nice user-friendly APIs.
[2522.74 → 2527.36] You know, there's a lot going on under the hood, but, you know, like, you're making it easy for people to actually use.
[2527.44 → 2527.98] That's the beauty.
[2528.28 → 2531.32] What can be easier to make just a Hello World endpoint?
[2531.56 → 2532.36] Because it's so true.
[2532.36 → 2537.66] Yeah, well, the loan balancer, Kubernetes cluster, control plane, and a few other things.
[2538.06 → 2538.70] That's easy.
[2539.54 → 2539.90] I know.
[2540.08 → 2543.66] Man, things have changed over the last decade or two.
[2544.22 → 2554.44] So I do want to switch gears a little bit here, sort of to understand, like, if someone wanted to contribute, because it sounds like there's still a lot of awesome ideas sort of at play and coming to the project.
[2554.44 → 2560.46] If someone wanted to contribute to that, like, what would basically be sort of a safe expectation of them?
[2560.54 → 2562.68] Should they know how to work in PHP?
[2562.98 → 2564.96] Should they know how to do Go?
[2565.42 → 2567.18] Is there work for both sides of the fence?
[2567.32 → 2569.08] Like, what do you need to contribute to this project?
[2569.50 → 2571.48] Basically, I don't know PHP at all.
[2572.00 → 2578.10] I started Googling, like, okay, Anthony, I need some test script.
[2578.64 → 2581.04] Could you please write it for me?
[2581.04 → 2586.18] Or I need to, like, a for loop to write or some variable.
[2586.38 → 2589.60] So I need to Google how to write a for loop in PHP.
[2589.78 → 2590.06] For loop.
[2590.20 → 2594.76] And this is great, because I don't need to involve in the like, PHP part.
[2595.00 → 2599.78] I can concentrate only to improve the Golang user experience.
[2599.78 → 2606.02] And, like, to contribute to the roadrunner, it depends on who are you as a developer.
[2606.18 → 2608.94] You are a PHP developer, or you are, like, Golang developer.
[2608.94 → 2612.32] If you're, like, a Golang developer, it's very easy.
[2612.42 → 2622.84] You just need to go into the root runner issues, find an issue marked, like, help needed or easy to resolve, like, some entry-level issues.
[2622.84 → 2634.70] Or if you want to, like, contribute to PHP part, I guess it's a spiral framework, which you can, like, also have a lot of tickets to improve our PHP part.
[2634.80 → 2638.68] And you don't need to know both sides of this at the same time.
[2638.76 → 2640.96] You only need to know, like, PHP or Go.
[2641.12 → 2645.42] Or if you want to contribute both, usually, yeah, you need to know both.
[2645.68 → 2646.58] But, yeah, it's...
[2646.58 → 2648.58] Sounds like there's room for either side.
[2648.58 → 2648.98] Yeah.
[2649.36 → 2651.08] We're pretty friendly to contribution.
[2651.36 → 2654.38] Like, on PHP, you can help us to improve SDKs and Golang.
[2654.82 → 2661.64] You can go as deep into the weeds as, like, SSL wish, like, dump little ALGOL to run some crazy stuff.
[2661.72 → 2668.00] Even Python developers can write a protocol version 3 and, like, or Ruby on Rails developer.
[2668.24 → 2668.52] Yeah.
[2668.78 → 2673.36] If you want, we will definitely accept the contributions to make it work for other languages.
[2673.36 → 2688.90] This episode is brought to you by Launch Darkly.
[2689.34 → 2691.34] Fundamentally change how you deliver software.
[2691.80 → 2692.68] Innovate faster.
[2693.04 → 2693.64] Deploy fearlessly.
[2694.18 → 2698.46] And take control of your software so you can ship value to customers faster and get feedback sooner.
[2698.92 → 2701.96] Launch Darkly is built for developers but empowers the entire organization.
[2701.96 → 2705.28] Get started for free and get a demo at LaunchDarkly.com.
[2705.64 → 2707.44] Again, LaunchDarkly.com.
[2707.80 → 2713.90] And by our friends at Flat File, the leading data onboarding platform for teams who don't want to build yet another CSV uploader.
[2714.30 → 2718.32] Flat File's powerful, out-of-the-box solution takes the import burden off of your shoulders,
[2718.60 → 2722.04] freeing you to solve bigger business problems and build products that people love.
[2722.30 → 2726.34] Get to usable data faster so you can focus on what matters most to you and your business.
[2726.34 → 2728.36] It is incredibly fast to set up.
[2728.40 → 2732.16] Just write a few lines of code and get up and running in hours, not days or weeks.
[2732.50 → 2733.64] It is framework-agnostic.
[2733.78 → 2739.30] Use the SDK to integrate Flat File into any JavaScript application with support for all major frameworks.
[2739.68 → 2741.64] Learn more and get started at FlatFile.com.
[2741.64 → 2743.94] Again, FlatFile.com.
[2758.02 → 2767.86] All right.
[2767.86 → 2770.34] So, let's start with you, Anton.
[2770.60 → 2771.30] What did you bring?
[2771.64 → 2774.00] You only need 64 kilobytes of RAM.
[2774.32 → 2774.74] For what?
[2775.20 → 2775.88] Just for everything.
[2776.02 → 2776.20] Ever?
[2776.74 → 2777.60] Well...
[2777.60 → 2779.04] Okay.
[2779.72 → 2780.36] Prove it.
[2784.86 → 2793.66] For the most of the stuff, I mean, I would just say, like, people have to, like, try to work on kind of more memory-efficient applications.
[2793.66 → 2797.72] Because when you work with hardware, 64 kilobytes of RAM is a ton.
[2798.06 → 2802.92] You know, you can make robot moves, blink eyes, go on the stairs, and do some other stuff.
[2803.48 → 2806.56] And what can you do with 64 kilobytes of JavaScript application?
[2806.74 → 2807.26] Tell me, please.
[2808.70 → 2809.44] Maybe nothing.
[2809.84 → 2810.42] Not much.
[2811.86 → 2814.54] I have 64 gigs and even can't run a stream.
[2814.54 → 2820.54] I mean, I will say that over the years, we've gotten more...
[2822.14 → 2823.52] Well, let me put it nicely.
[2823.66 → 2828.58] We don't worry very much about sort of CPU and memory and disk, right?
[2828.66 → 2833.20] Things that used to be expensive, you know, like, you know, even like 20, 30 years ago, right?
[2833.36 → 2834.44] Not so much now.
[2834.74 → 2835.78] We take these things for bringing it down.
[2836.04 → 2836.24] Yeah.
[2836.24 → 2842.00] Yeah, but, like, if you know how to pack it down to this level, you can create much larger scalable applications.
[2842.22 → 2848.42] Because when you create, let's say, the traffic filtering software or, like, VPN cores, right?
[2848.54 → 2853.22] The things which actually, like, well, real IP, let's say, not just API endpoints.
[2853.78 → 2855.70] That's where you have to optimize it.
[2855.76 → 2861.34] And, like, knowing these basics and knowing that, yes, 64 kilobytes sound like a small amount.
[2861.34 → 2867.28] And it's a joke, which Bill Gates said back in the day, if someone don't remember, like, obviously he's wrong.
[2867.48 → 2883.54] But if you realize how actually huge this amount, like, 64 kilobytes of stack on, like, some hardware chip can let you, well, to stream a ton of traffic, you know, and build something like a Netflix, build something like Starlink.
[2883.94 → 2887.72] Because all these things which are doing great, great things, they have to be optimized.
[2887.72 → 2891.96] You can't put, you know, 10 CPU server in space.
[2892.14 → 2893.26] It's still going to work.
[2894.50 → 2895.94] All right, all right, all right.
[2896.08 → 2896.96] Valerie, what did you bring?
[2897.20 → 2901.02] So my popular opinion is open source is a hard work.
[2901.54 → 2905.26] In my opinion, it's much harder than some enterprise development.
[2905.82 → 2908.90] Because I was involved in, like, in different enterprise projects.
[2909.24 → 2912.70] And the flow is pretty much defined.
[2912.70 → 2922.76] Like, if customer support has some ticket, it, like, can process it, send to specialists, like, quality assurance.
[2922.98 → 2927.38] It, like, can test it, write, like, test cases it brings to you.
[2927.82 → 2932.56] You can, like, see this ticket, fix the problem, run the tests, and so on.
[2932.56 → 2941.70] But in open source, a lot of people think that they should not bother themselves to write a proper description of the issue.
[2942.04 → 2944.90] It's like, I have a problem, please fix it.
[2945.16 → 2950.08] Or one of my favourite issues is, like, nuts and question mark.
[2951.46 → 2952.84] What does it mean?
[2953.40 → 2955.12] So a lot of people...
[2955.12 → 2957.84] Are they offering nuts or are they asking you if you want not?
[2957.84 → 2969.72] But when I say, please describe what do you want, like, you want to not support or something else and close this ticket, the guy asked me, why are you so rude?
[2970.04 → 2971.50] Why are you closing my ticket?
[2971.80 → 2975.90] So, and there are a lot of such things in the open source development.
[2976.08 → 2978.08] So you should handle a lot of things.
[2978.08 → 2990.68] You should have various types of virtual machines to run on Ubuntu previous versions, Ubuntu current versions, Debian, FreeBSD, macOS, and Windows different versions.
[2990.94 → 2999.12] So if someone send you a ticket, I guess some people think this is a joke, like open source development is like a joke for us.
[2999.12 → 3000.14] So I don't know.
[3000.14 → 3008.74] So it's like, write three, two or three, like lines of the description or do not provide like test cases.
[3009.16 → 3013.68] So it's very complicated to figure out what do you really want.
[3014.70 → 3019.68] So one guy asks me, like, the docker doesn't work on my machine.
[3020.34 → 3021.36] Like, what?
[3021.68 → 3023.82] So I have to fix the docker on the machine.
[3023.82 → 3031.68] So, but you see, in CI, everything like brings from the scratch, like a docker installs from the scratch.
[3031.80 → 3033.56] So you see everything works inside the docker.
[3033.96 → 3035.46] It's something inside your machine.
[3035.64 → 3038.54] But the guy said, no, it's a problem in your code.
[3038.82 → 3040.22] So it's because I can't get around.
[3040.38 → 3047.78] So it was so long and so boring, like communications with a lot of people to prove that this is not a joke.
[3048.20 → 3050.66] It's a hard work, really hard work.
[3050.94 → 3051.14] Yeah.
[3051.30 → 3051.62] Yeah.
[3051.62 → 3054.88] So, and actually all the court to write is public.
[3055.08 → 3058.22] So like, because people are going to see it and going to blame you.
[3058.32 → 3061.60] I mean, they're going to blame you anyway, but now they're going to have a reason.
[3062.22 → 3062.60] Right.
[3062.72 → 3063.16] Exactly.
[3063.58 → 3063.90] Okay.
[3064.02 → 3069.94] You have a squirt, like N squirt algorithm, or you can N factorial algorithm.
[3070.22 → 3073.92] So you shouldn't do it.
[3074.96 → 3075.44] Awesome.
[3075.62 → 3076.08] Awesome.
[3076.08 → 3089.04] Thank you guys so much for coming on the show and talking about really what piqued my curiosity when it showed up on my desk, my virtual desk, you know, PHP and go and how these two things sort of complement each other.
[3089.18 → 3090.50] It's been awesome having you all.
[3091.12 → 3094.28] And I will now play our outro song.
[3094.28 → 3097.44] And we will try to wrap this up.
[3097.60 → 3098.58] Right on time too.
[3106.10 → 3107.64] That is our show for this week.
[3108.04 → 3110.92] Thanks again to SEB for requesting this episode.
[3110.92 → 3111.88] We hope you enjoyed it.
[3112.10 → 3113.34] Yes, we take requests.
[3113.68 → 3119.14] Head to gotime.fm slash request and let us know what you want to hear about on the pod.
[3119.66 → 3123.14] Special thanks again to Vastly for delivering our shows all around the world.
[3123.40 → 3127.22] To Break master Cylinder for hooking us up with all the excellent beats you hear on the show.
[3127.46 → 3128.42] And to you for listening.
[3128.88 → 3130.46] We appreciate you spending time with us.
[3130.92 → 3135.06] If you have a couple more minutes, enjoy this clip from the changelog 486.
[3135.06 → 3140.12] We invited Frank Kruger on to discuss his practical guide to solving hard problems.
[3140.38 → 3141.96] And he shared so much wisdom with us.
[3142.36 → 3142.76] Listen in.
[3143.14 → 3147.64] And I was reading Wikipedia page after Wikipedia page, modern treatment after modern treatment.
[3147.86 → 3150.88] What I was trying to do was synthesize these V nodes.
[3151.00 → 3153.38] It's a complicated thing of data management.
[3153.38 → 3159.60] And I couldn't understand any of the algorithms until I opened the Dragon Book and saw in the 1970s,
[3159.60 → 3165.36] their pseudocode implementation of the algorithm, which threw away all the details,
[3165.86 → 3169.18] ignored all these modern advances that aren't actually advancements.
[3169.24 → 3170.28] You don't actually need them.
[3170.74 → 3175.36] And written out in this very clear style and all capital letters.
[3175.52 → 3178.36] I don't even know what language they were pretending to be in that book.
[3178.56 → 3183.40] But just finally getting it from this old, old resource and realizing,
[3183.62 → 3186.62] oh my God, in the 1970s, there's chapter five, section four,
[3186.62 → 3188.64] and they describe exactly the problem I'm having.
[3188.88 → 3191.58] And they, oh my God, even better, have a solution to it.
[3191.82 → 3191.92] Wow.
[3192.00 → 3195.76] And then you can transcribe that solution from their crazy,
[3195.86 → 3198.82] whatever language that was, into whatever you want to be using.
[3199.22 → 3201.30] And you learn a lot during that process.
[3201.44 → 3203.90] That felt so good to me when I finally found that.
[3204.56 → 3207.76] It's like coming across hidden treasure somewhere.
[3207.96 → 3209.38] You're like, look at this.
[3209.52 → 3210.12] Look what I found.
[3210.40 → 3211.38] I knew they were smart.
[3211.46 → 3211.88] That's crazy.
[3212.54 → 3214.34] You want to tell somebody at that moment, but nobody,
[3214.34 → 3216.14] not that they don't care, they just can't care.
[3216.14 → 3218.40] It's like, they just can't care.
[3218.52 → 3219.10] They can't care.
[3219.20 → 3220.88] It's like, I have no idea what you're talking about, Frank.
[3220.98 → 3221.34] Okay.
[3221.60 → 3223.12] But congratulations on something with the problem.
[3223.56 → 3225.24] Well, there's a little street cred too.
[3225.48 → 3230.32] Like just knowing about the book shows that you're semi-interested in compiler technology.
[3230.56 → 3232.06] Actually having a use for the book.
[3232.22 → 3234.24] I feel like I became a computer scientist that day.
[3234.30 → 3236.96] I actually applied something from the Dragon book.
[3237.12 → 3237.34] Yeah.
[3237.42 → 3239.90] It was a real high point in my career, to be thoroughly honest.
[3239.94 → 3242.74] And that's where you're standing on the shoulder of giants.
[3243.18 → 3245.08] It's like you graduated from Hogwarts that day.
[3245.08 → 3245.86] You became a wizard.
[3246.14 → 3247.00] You became a real wizard.
[3247.08 → 3248.28] By copying a wizard's spell.
[3248.48 → 3248.68] But yeah.
[3249.44 → 3251.80] But I realized the wizard's spell worked.
[3252.06 → 3252.20] Yeah.
[3252.24 → 3253.78] I was very Harry or Hermione there.
[3256.02 → 3262.14] Continue listening and subscribe to the changelog at changelog.fm slash 486.
[3262.80 → 3266.16] Hey, are you ready for our next instalment in the maintenance series?
[3266.66 → 3272.22] Chris assembled an awesome panel to discuss what to do when Go projects get big and messy.
[3272.22 → 3277.54] Johnny joined him, as did Ian Lop shire and Sam Boyer for an excellent conversation.
[3278.00 → 3280.96] That's something to look forward to next time on Go Time.
[3281.24 → 3281.74] Go.
[3281.74 → 3282.86] Go Zen 3 fucking 3 at 9!
[3282.90 → 3284.78] Stop talking here!
[3285.22 → 3287.20] Ciao!
[3287.44 → 3287.54] Bye!
[3287.68 → 3288.22] No!
[3288.70 → 3288.72] No!
[3288.72 → 3289.04] No!
[3289.04 → 3289.08] No!
[3289.10 → 3289.28] No!
[3289.28 → 3289.32] Oh!
[3289.32 → 3289.38] No!
[3289.38 → 3290.22] I know you have enough.
[3290.56 → 3293.42] No!
[3293.42 → 3299.24] Game on.
