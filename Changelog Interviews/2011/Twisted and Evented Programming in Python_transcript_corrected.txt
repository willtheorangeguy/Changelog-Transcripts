[0.00 → 17.58] Welcome to the Changelog episode 0.5.8.
[17.92 → 19.00] I'm Adam Stachowiak.
[19.12 → 19.98] And I'm Wynne Netherlands.
[20.12 → 21.04] This is the Changelog.
[21.06 → 22.94] We cover what's fresh and new in the open source world.
[23.66 → 26.24] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.42 → 27.18] We're also on GitHub.
[27.18 → 34.02] At thegethub.com slash explore, you'll find some trending repos, some feature repos from this blog, as well as our audio podcasts.
[34.20 → 36.94] If you're on Twitter, follow Changelog Show and me, Adam Stack.
[37.16 → 39.54] And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.04 → 41.30] Fun episode this week.
[41.36 → 51.96] Talk to Glyph over at Twisted, the granddaddy of all vented, non-blocking, I don't want to call it a web framework, but a toolkit, as it were.
[52.72 → 56.02] Big in the Python community, so chock-full of white space.
[56.02 → 58.26] So we like Hamelin's eyes and white space, right?
[58.72 → 58.94] Yeah.
[59.66 → 60.70] Get a little of that.
[60.92 → 61.22] Cheers.
[61.50 → 65.14] Every time that we say Hamelin's eyes from now on, Adam's going to mix in the clinking sound.
[65.32 → 66.16] So, bottoms up.
[66.58 → 67.18] There you go.
[68.22 → 69.86] So, no jobs to read this week.
[69.90 → 76.20] We do have some developments around the sponsorship front that we're just so excited about that we will share in coming weeks.
[76.20 → 80.46] Yeah, it's a really exciting thing, actually, for somebody else as well as us.
[80.88 → 81.92] As well as us.
[82.34 → 86.04] Kenneth joined the last minute and helped us out with this Twisted episode.
[86.38 → 87.76] I think you're going to enjoy it.
[88.02 → 97.52] Talked about non-blocking frameworks in general, but also kind of the world of Python and really a rich history of this Twisted project.
[97.62 → 98.36] Ten years old.
[98.36 → 101.88] Anybody using Tornado might also listen in as well.
[102.28 → 109.46] Yeah, I went into that and some of the I guess, distinctions between Twisted and Tornado.
[110.16 → 115.34] I think it's wild how it contains a web server, chat clients, and all this other fun stuff to do all this.
[115.44 → 115.96] It's pretty wild.
[116.38 → 117.90] Did you see the success pages?
[117.90 → 124.70] It powers Hip Chat, which we use every day, and also powers Tweet Deck, which we're big fans of.
[124.80 → 131.10] Some other high-profile sites, but he probably gets the most play out of the fact that Lucasfilm is using it.
[131.36 → 131.92] There you go.
[132.70 → 133.20] Fun episode.
[133.30 → 133.80] Should we get to it?
[134.02 → 134.64] Let's do it.
[134.64 → 148.86] Chatting today with Glyph Lefkowitz from Twisted, Twisted Matrix Labs.
[149.56 → 154.10] So, Glyph, why don't you give a quick introduction to who you are and a bit about Twisted?
[155.64 → 159.12] Well, I'm the original founder of the Twisted project.
[159.98 → 163.32] I write lots of code in Python, pretty much all of it open source.
[164.64 → 169.96] And Twisted is an event-driven framework in Python.
[170.78 → 178.38] It's a networking engine and has tons of utilities for doing event-driven programming of various kinds,
[178.50 → 180.08] lots and lots of protocol implementations.
[181.34 → 183.86] I could do the whole list, but then we'd be here all day.
[184.42 → 189.36] So, yeah, not too much to tell.
[189.72 → 192.48] If you know what it is, you probably have used it.
[192.48 → 196.64] Because it's one of the few things of its kind.
[197.16 → 200.34] A little bit like Event Machine or Node, I guess.
[200.66 → 204.26] Recently, there are more popular hip versions of this thing.
[204.32 → 205.88] But Twisted's been around for 10 years.
[206.74 → 210.96] So, we were not the first, but a pretty early one.
[211.46 → 213.80] What was the impetus for starting Twisted?
[213.80 → 216.62] Oh, I love that question.
[216.80 → 218.48] I actually gave a talk about that question recently.
[218.66 → 222.34] The impetus for starting Twisted was I was making a video game.
[223.62 → 227.38] The story actually starts when I was 8, but the first 10 years or so are not very interesting.
[229.08 → 231.42] Eventually, so I was writing this video game in Java,
[231.54 → 234.72] and I eventually sort of reached the limits of the Java virtual machine,
[234.72 → 239.78] especially because this was around 2000 when there wasn't such a thing as NIO yet.
[239.96 → 241.44] So, I had thread per connection.
[241.82 → 243.78] In fact, four threads per connection.
[245.02 → 247.22] Reader, writer, exceptions, and logic.
[247.72 → 250.86] And as you might imagine, that got to be a big mess pretty fast.
[251.08 → 253.06] So, I rewrote it in Python.
[253.30 → 254.78] Still a thread per connection thing.
[255.22 → 257.22] And then I discovered the select module.
[257.32 → 260.04] I was just kind of going through learning each module in a standard library,
[260.20 → 262.38] and I had no idea what select meant.
[262.38 → 266.22] So, I read the documentation, and it didn't make any sense to me.
[266.38 → 269.68] So, I did a little prototype, and then thought,
[269.80 → 271.94] wow, this is clearly the best way to do I.O.
[272.60 → 274.90] So, it's so much less confusing.
[275.06 → 276.08] Everything just happens in order.
[276.22 → 280.26] And as I was implementing a game, I really wanted things to happen in that kind of way
[280.26 → 285.36] because I wanted to do a simulation loop that had discrete phases and discrete ticks,
[285.52 → 289.02] and every action that a user took was a discrete object.
[289.02 → 295.22] So, I was like, great, I'm going to do this.
[295.42 → 297.32] I'm going to switch everything over to using select.
[297.94 → 301.40] Now, where are all the network protocol implementations?
[301.62 → 302.94] Because there's got to be a bunch of them, right?
[303.18 → 306.32] And I found, you know, Python has all these great libraries,
[306.48 → 311.90] URL lib and HTTP lib and Mime lib and IMAP lib,
[311.90 → 315.60] but none of them work in an asynchronous context.
[315.92 → 320.68] There was Async Core at the time, but Async Core didn't actually do anything.
[320.86 → 322.78] It just let you write your own stuff.
[322.84 → 324.30] So, I wrote my own event-driven core,
[324.60 → 331.80] and I decided that it should be the one true way to write network protocols in an asynchronous way
[331.80 → 336.76] so that there would be a common API that people could get a bunch of different protocol implementations
[336.76 → 342.72] and have them all in the same process because I wanted to make my game accessible to web browsers,
[343.06 → 345.22] which were, at the time, this new hip thing.
[345.32 → 348.52] But, you know, all the other network clients that were popular then,
[348.68 → 352.64] Telnet clients, and I wanted it to be able to deliver you email.
[352.90 → 355.32] I wanted you to be able to check your email on the game server.
[356.00 → 358.18] And now we actually have all that stuff in Twisted.
[358.18 → 363.12] There's an IMAP implementation, POP, SMTP, DNS, HTTP,
[363.42 → 366.30] pretty much all the stuff that I originally wanted to do in that original game.
[366.76 → 368.88] And the game is nowhere to be seen, though.
[369.10 → 374.22] That project has become increasingly research,
[374.54 → 376.98] and it's currently called Diamond Imaginary.
[377.24 → 379.96] And if you Google around enough, you can probably find the code for that.
[380.02 → 383.28] But it's definitely not as mature or interesting as Twisted itself.
[383.48 → 386.06] Speaking of Google, you own Twisted on Google.
[386.38 → 387.06] I was impressed.
[388.00 → 391.74] Yeah, there's a couple of people that are close.
[391.84 → 394.80] There's, I think, a humour site that has Twisted in its name somewhere.
[394.80 → 401.30] But, yeah, we've been relentlessly and shamelessly self-promoting for a really long time,
[401.40 → 402.54] and so Google likes us.
[403.88 → 408.72] So you were mentioning all the different asynchronous libraries that weren't available at the time for HTTP.
[409.58 → 416.86] Do you have any thoughts on event and event let and how those are, you know, their relationship with Twisted?
[416.86 → 417.86] Sure.
[419.26 → 421.74] Well, so first, event let is great.
[421.84 → 424.76] I love it when people bring up event let because they so frequently,
[425.04 → 428.68] I hear it from some programmer who used to use Twisted and is now using event let,
[428.80 → 431.38] and they sheepishly admit the betrayal.
[432.24 → 436.96] But event let actually, the default hub for event let, uses Twisted for network IO.
[436.96 → 441.56] And that's pretty much exactly the situation we want to be in.
[441.64 → 443.62] It's just the default choice for network IO.
[443.80 → 449.58] And then event let presents this API that's different from what Twisted would natively present,
[449.68 → 453.40] but you can still use all the Twisted protocols, presuming that you use that hub,
[453.90 → 458.24] and you don't switch to one of the other event let hubs.
[458.24 → 461.94] Which, you know, I don't really understand the point of some of the other event let hubs
[461.94 → 469.52] because one of the big things that they tell you in their documentation about which hub you should use is,
[469.60 → 473.68] well, you could use the Twisted hub, or you could use the poll hub because it's more scalable.
[474.76 → 479.28] But actually, you can just use Twisted's poll support, and it's equally scalable.
[479.58 → 487.06] So I think that there might be a communication issue there that we might need to talk to their developers more often.
[488.24 → 494.68] And event is like event let, except it's got its own network IO and is totally incompatible with Twisted,
[494.80 → 495.96] so it's not very interesting to me.
[496.90 → 501.74] It kind of seems like just a step-down from what event let offers.
[501.90 → 503.84] I realize that it's a little bit simpler, smaller.
[505.82 → 511.14] But things like event and event let present this API which is sort of semi-synchronous.
[511.14 → 517.38] The code that you write in event let or event is more or less indistinguishable from the code you would write
[517.38 → 520.24] if you were just writing a multithreaded server.
[520.72 → 523.18] You just write a protocol implementation that blocks,
[524.36 → 527.08] and then transparently in the background it's made asynchronous,
[527.36 → 530.88] but you have to do all the same things that you would do.
[531.42 → 533.70] You have to write synchronization logic.
[533.90 → 537.26] You have to make sure that you don't accidentally context switch in the wrong place.
[537.26 → 542.06] So for certain types of applications, and to my mind for most applications,
[542.06 → 544.54] but obviously my taste is a little bit biased here,
[545.28 → 548.72] I think that for most applications something like Twisted is actually simpler
[548.72 → 552.72] because you don't have to kind of unravel the threads in your head
[552.72 → 557.50] and go and inspect and make sure that nothing you're calling eventually calls a socket function
[557.50 → 560.52] because that'll cause a context switch that you might not be expecting.
[561.24 → 562.72] With Twisted it's all very straightforward.
[562.72 → 565.28] You don't context switch until you return.
[566.06 → 568.52] And so it's very easy to figure out when you're returning.
[569.52 → 571.64] I've been wanting to get into Twisted for a long time.
[571.72 → 573.82] I just haven't found the excuse to.
[575.72 → 577.60] So I just wanted to point that out.
[577.70 → 579.12] There's nothing there.
[579.28 → 579.38] Sorry.
[579.86 → 581.00] Deep thoughts by Kenneth.
[581.30 → 581.54] Yes.
[582.32 → 588.12] So is HTTP, I guess, the primary protocol that people are using when they're using Twisted?
[588.12 → 590.78] Oh, well, of course.
[590.94 → 595.32] But I mean, that's just because HTTP is the primary protocol that people are using
[595.32 → 596.26] when they're using the internet.
[597.42 → 598.64] That's twisted.web, right?
[599.34 → 600.64] Yes, that's twisted.web.
[601.78 → 608.28] And people who use Twisted do tend to use HTTP and then something else.
[608.38 → 612.88] I mean, there are obviously a lot of users who will just use HTTP and write a web app,
[612.88 → 621.00] especially in these heady days of Comet and WebSockets where HTTP is an increasingly expanding thing
[621.00 → 623.68] that actually is event-driven and two-way.
[624.46 → 633.62] But HTTP in combination with like DNS or with an email protocol is a very common sort of thing
[633.62 → 634.54] people will do with Twisted.
[636.30 → 638.98] Was that the primary protocol you had out of the box?
[639.10 → 642.18] And how soon did the other protocols trail?
[642.96 → 646.30] Actually, HTTP was not first at all.
[646.88 → 648.36] I think it might have been third or fourth.
[648.52 → 651.34] I can't remember if NNTP beat it out.
[652.50 → 657.86] The idea was originally Twisted's main protocol was really just a remote,
[658.00 → 662.78] a custom remote object access protocol because there was a sort of desktop client for the game.
[663.72 → 667.64] That protocol eventually became what is now Perspective Broker,
[668.50 → 670.98] which is in the twisted. Spread package.
[670.98 → 675.46] And it's twisted.spread.PB.
[675.46 → 683.56] And the idea was you wanted to just publish your objects for access over a network.
[683.72 → 685.76] So PB was the native protocol of Twisted.
[685.86 → 688.48] And then all the other things were this kind of degenerate things like,
[688.62 → 691.66] oh, well, okay, maybe you want to use a web browser, but that's not as good.
[691.66 → 697.46] Obviously, the PB applications marketplace has not taken off to quite the degree that we expected.
[697.62 → 701.20] So HTTP has become a much bigger part of Twisted's life.
[701.52 → 705.12] But that same idiom kind of pervades still,
[705.26 → 710.36] which is that every protocol is just about publishing your objects in the network somehow.
[710.36 → 718.20] So HTTP is a little more popular, but it doesn't occupy a special position in Twisted's hierarchy.
[720.20 → 723.70] Especially because given that Twisted is not a web framework,
[723.84 → 726.20] people often come to it expecting something like Ruby on Rails,
[726.32 → 727.92] but it's really nothing like that at all.
[728.28 → 736.24] It's a lower level thing that's designed that you would build something like a web framework on top of.
[736.24 → 740.92] Because it's not a web framework,
[741.14 → 744.50] people who come to it and expect a web framework are often disappointed and leave.
[744.66 → 749.74] People who come to it expecting a toolkit to do this kind of multiprotocol things are very happy,
[749.86 → 751.88] and that's what our community is largely made up of.
[752.82 → 754.54] So you mentioned it's 10 years old,
[754.58 → 758.28] and I know that we haven't had Mac Intel that long, and you're on a Mac now,
[758.36 → 761.62] so I'm assuming you weren't on a Mac when this project started.
[761.62 → 765.30] So you come from a Linux or a Windows Python background?
[765.30 → 767.92] I'm definitely a polyglot.
[768.06 → 769.94] I like to use every platform.
[770.60 → 773.68] I think probably my history is primarily Linux.
[773.94 → 776.26] A lot of Twisted's development was on Linux.
[776.44 → 780.12] But actually, I believe at the time that I started the project,
[780.26 → 784.58] I was using a public beta of Mac OS X server.
[785.44 → 789.12] That's kind of what I remember having on my workstation at the time.
[789.12 → 795.60] But yeah, I have lots of Linux servers.
[795.84 → 798.16] I have several Macs.
[798.72 → 801.98] I still play video games, so I run Windows on occasion.
[803.24 → 806.38] And that's actually part of Twisted's philosophy as well.
[807.26 → 813.48] It's partially just a random comment on my own desire to be portable and be able to work anywhere.
[813.48 → 820.12] But also, we want you to be able to write asynchronous code for Twisted.
[820.32 → 824.96] The original vision was to be able to write an asynchronous protocol implementation and say,
[825.06 → 825.82] there, I've done it.
[825.88 → 827.66] It's an asynchronous HTTP client.
[828.16 → 830.16] You can use it from any Twisted program.
[830.42 → 835.10] And part of the appeal there is you want to be able to write that on the server and the client, potentially.
[835.10 → 840.36] So we have reactors for GUI toolkits of various kinds.
[840.72 → 844.06] So it runs native in the Mac GUI.
[844.18 → 846.20] It can run native in a Windows GUI.
[846.34 → 852.16] It can run in GTK on Linux or in QT, which I think works cross-platform.
[852.52 → 852.68] Yes.
[853.82 → 855.22] Well, obviously, QT does.
[855.34 → 857.68] I'm trying to remember if all the support actually does.
[859.46 → 862.58] But yeah, so you can use Twisted pretty much wherever.
[862.58 → 872.76] And we try, I think there's a definite bias, especially after many years of trying to fight with the network stack on Windows,
[873.10 → 876.30] that we definitely have a Unix-y bias and do not like Windows very much.
[876.34 → 878.24] But we try not to let that show through too much.
[878.30 → 886.06] We do have support for IOCompletionPorts, which is a Windows-specific asynchronous networking API.
[888.08 → 892.16] So are there any uses for Twisted other than network-driven programming at all?
[893.58 → 899.94] Well, all programming these days is network programming, really.
[900.98 → 902.38] The network is the computer.
[903.10 → 903.30] Yeah.
[904.70 → 909.40] It's sad that even though those guys were right, they didn't really get to benefit too much from being right.
[909.40 → 909.44] Right.
[911.72 → 918.38] So Twisted has a lot of utilities like, for example, deferred.
[918.48 → 920.70] A deferred is a result that doesn't exist yet.
[920.70 → 928.52] That is very useful in a network context where you're going to make a call across the network and the result might come back or might not.
[928.52 → 934.92] It's also useful in a GUI context, though, because it lets you pop up a dialogue and continue processing.
[935.32 → 939.66] You can have a function which asks a user a question.
[940.38 → 943.40] And, of course, if you're writing a web app, that's what you're doing half the time anyway, right?
[943.40 → 947.18] You're just asking the user a question and waiting for their response to come back.
[947.62 → 951.46] And you would make a deferred to say what the response would be.
[951.72 → 954.10] But you can just do that with a dialogue box, too.
[954.14 → 962.60] And that lets you pop up a dialogue box without blocking or having weird re-entrant multi-level main loops or any of the funky stuff that GUIs sometimes have to facilitate that.
[962.64 → 963.60] You can just make a deferred.
[963.82 → 965.64] And then you can pop up five dialogue boxes.
[965.64 → 967.22] The user can answer them in any order.
[968.32 → 970.98] And you can continue processing in the background while they're doing that.
[972.32 → 973.72] So there's that.
[973.80 → 975.28] There are also some timing utilities.
[975.78 → 987.62] One of my favourites is twisted.internet.task.looping call, which was originally designed for a voiceover IP application, so a networking application,
[988.82 → 995.00] in order to do real-time, every 10 milliseconds, sending out an audio sample.
[995.64 → 1001.20] So you can tell people about that the next time you hear that Python's not fast enough for something.
[1001.32 → 1003.20] It can do real-time network audio processing.
[1005.44 → 1007.74] And so that was originally what it was for.
[1007.82 → 1017.52] But then we realized that we really wanted to have it be able to compensate for falling behind.
[1017.52 → 1029.82] So the idea is it obviously can't be hard real-time because even just forget about Python, even just being a user space process, like not a kernel process on a Unix operating system, you can't really do hard real-time.
[1030.46 → 1036.08] So since it's soft real-time, we want to make it so you get called every 10 milliseconds really reliably.
[1036.08 → 1050.02] But then if some other thing is processing and delaying the main loop from executing your call again, you get notified, okay, this is an exact multiple of 10 milliseconds that you're being invoked at, but you've skipped six calls.
[1050.20 → 1051.72] So you've dropped six frames.
[1051.72 → 1054.60] And that's useful for animation.
[1055.24 → 1058.32] You can use it in a Pi game, which I've seen done.
[1060.26 → 1067.72] These are obviously less popular uses for Twisted because it is a pretty big piece of code that contains lots and lots of network protocol implementation.
[1067.72 → 1074.82] So most people who just discover it in the first place come to it because of the networking stuff that's in it.
[1074.96 → 1082.18] But lots of people who learn to work with the event abstractions in Twisted and write other kinds of programs do use it for other stuff.
[1084.32 → 1088.22] So Twisted is extremely performant compared to a lot of other options out there.
[1088.66 → 1094.06] Can you get a little bit into the whole controversy behind when Tornado came out and how they built a whole –
[1094.06 → 1099.22] from my understanding is they built a whole framework that was unnecessary because the Twisted.web was already there, right?
[1100.10 → 1101.90] But it didn't have a web framework built on top of it?
[1102.54 → 1106.06] I suppose it depends on who you ask whether it was necessary or not.
[1106.30 → 1113.84] I think the most definitive answer to this was a couple of – so I did a big angry blog post when Tornado came out,
[1114.32 → 1118.90] largely because – not because they wrote it because people write stuff all the time.
[1118.90 → 1125.34] It was more that the way they announced it was very strange and –
[1125.34 → 1126.06] Revolutionary.
[1127.06 → 1133.18] Well, it included a comment about Twisted, which was misleading and wrong and kind of weirdly passive-aggressive.
[1133.32 → 1136.84] It was – it said something about Twisted not meeting their requirements.
[1137.60 → 1139.94] And I had never heard from them about their requirements.
[1140.08 → 1141.50] I had no idea what their requirements were.
[1141.58 → 1143.16] They didn't say what their requirements were.
[1143.26 → 1148.28] They kind of implied that it wasn't fast enough, but they didn't give any performance numbers or anything.
[1149.14 → 1159.78] So I was a little miffed that they were bad-mouthing Twisted in this way that made it impossible to respond and say,
[1160.20 → 1161.02] no, it's not slow.
[1161.14 → 1162.02] No, it's not whatever.
[1163.04 → 1166.44] Or even just to constructively respond and say, oh, wow, it is slow.
[1166.50 → 1167.38] We should really fix that.
[1170.02 → 1176.64] So Twisted – and I don't like to harp on the performance thing too much because performance is an extremely complex question,
[1176.64 → 1182.10] and especially when you get into a system like Twisted, which allows you to integrate lots of different protocol implementations,
[1182.24 → 1186.70] lots of different event sources all firing in the same main loop, all sharing resources.
[1187.56 → 1192.68] What you're doing depends on very, very heavily on how it's going to perform.
[1195.00 → 1196.14] And – or, well, I'm sorry.
[1196.28 → 1200.30] What – how it's going to perform depends on very, very heavily on what exactly you're doing.
[1200.30 → 1211.24] And one of the things that we have to counsel people over and over again in various support forums for Twisted is written your code,
[1211.40 → 1216.02] run your code, run a profiler, see what the hotspots are.
[1216.02 → 1226.02] Because people get very excited about microbenchmarks, and then they focus to the exclusion of actually useful stuff,
[1226.06 → 1228.54] especially like performance under scalability.
[1228.70 → 1237.04] Like if you have a framework that can do 20 connections really, really fast and process lots of responses and requests over those 20 connections,
[1237.22 → 1239.48] but then when you scale it up to 1,000, it falls over.
[1239.48 → 1244.26] Is that better or worse than a framework that doesn't do those 20 connections terribly fast,
[1244.44 → 1251.24] but maintains that performance on a totally consistent ramp up to however many connections you want?
[1252.42 → 1255.68] Personally, I tend to go for things that are the latter.
[1255.96 → 1259.08] But regardless of what type of performance you're looking for,
[1259.50 → 1265.54] your application will always be 10 times as much CPU than Twisted.
[1265.54 → 1271.06] So when you write a Twisted app, you will typically spend your time optimizing things outside Twisted.
[1271.18 → 1274.50] And I know this because whenever people start talking about performance,
[1274.62 → 1279.36] I really, really want people to contribute performance patches to help us make Twisted faster.
[1279.70 → 1282.80] You can check out Twisted's performance on speed.twistedmatrix.com.
[1283.40 → 1288.20] But it's fast enough for so many things that we get very few contributions in the performance area
[1288.20 → 1293.10] because people come to it, they spend a month complaining about performance
[1293.10 → 1296.94] and doing these tiny little benchmarks and trying to figure out if Twisted's going to be good enough.
[1298.02 → 1300.10] And then they decide to use it.
[1300.58 → 1302.76] And then it turns out that actually that was a huge waste of time
[1302.76 → 1305.82] and all those benchmarks they were doing are not actually measuring their app at all.
[1306.34 → 1312.66] And when they go to Optimize, it turns out, oh, well, Postgres is 99% of the performance bottleneck.
[1312.88 → 1315.68] We don't even notice Twisted. It doesn't show up in any of our profiles.
[1316.22 → 1318.32] So that's a typical performance story.
[1318.32 → 1321.82] And, of course, there are stories where, for example, if you're doing voice over IP
[1321.82 → 1325.76] and you're trying to multiplex a thousand real-time audio streams,
[1325.96 → 1329.26] then you start to notice the low-level networking stuff cropping up.
[1330.34 → 1338.04] As far as Tornado specifically, it seems to perform kind of to within an epsilon of Twisted.
[1338.38 → 1340.10] There are a couple of things it doesn't do.
[1341.54 → 1347.24] It's a little bit faster, so it's not really clear that there's a huge win on one side or the other.
[1347.24 → 1352.46] But the most definitive argument in the whole Tornado thing is after I wrote that big, angry blog post,
[1352.92 → 1357.88] a Twisted user came along and just wrote a patch.
[1358.00 → 1360.72] I think it was a fork on GitHub, if I recall correctly.
[1360.82 → 1361.96] That's where they're hosted.
[1362.72 → 1367.56] And he just took out all the networking stuff from Tornado and replaced it with Twisted.
[1367.68 → 1370.04] And the web framework API remained exactly identical.
[1371.22 → 1374.60] And it was a patch that deleted like 8,000 lines or something.
[1374.60 → 1378.86] And Tornado was functionally equivalent on top of Twisted,
[1378.98 → 1383.60] unless you were writing a hook into their bio loop.
[1384.90 → 1391.10] So quite the success stories on the Twisted website, Tweet Deck, Justin TV, Hip Chat, which I use every day.
[1391.42 → 1397.42] Any of these are you prouder of that you're able to enable someone else's success?
[1397.42 → 1402.02] Well, I'm proud of all of them.
[1402.14 → 1403.42] I'm happy when anyone...
[1404.74 → 1407.72] Well, it's got to be a geek's dream to power Lucas in some way, right?
[1408.32 → 1408.94] Oh, yeah.
[1409.18 → 1413.80] No, I guess if I had to pick one, it would have to be Lucasfilm.
[1414.00 → 1417.46] I got a Christmas card from them once, and I was like, I have arrived.
[1419.88 → 1422.72] And they were really great and super gracious.
[1422.72 → 1431.50] The folks at Lucasfilm who actually did that and got us a success story, obviously they're a big company,
[1431.68 → 1438.66] and it's difficult to get something like that out past the corporate communications people.
[1439.16 → 1444.60] And I really appreciate that Dave Petioles, who's the guy listed there in the success story,
[1445.14 → 1449.10] really worked to get us that success story and to get it on our website.
[1449.10 → 1454.10] So if I had to choose one, that would be it.
[1454.98 → 1458.32] But there are so many projects that have used it in some way.
[1458.48 → 1459.38] And I almost...
[1459.38 → 1462.10] Proud isn't even the right emotion in a way.
[1462.20 → 1462.90] It's honoured.
[1463.26 → 1470.84] I'm honoured that they chose the technology that the Twisted team and I worked on so hard.
[1470.94 → 1473.44] Like, it's just a great validation of our efforts.
[1473.44 → 1479.32] And there are some on there that if you look on...
[1479.32 → 1482.04] We got another wiki page, projects using Twisted.
[1482.96 → 1488.00] Success stories are just the ones where people could actually put together a little narrative
[1488.00 → 1490.22] about why they're using it and what was good about it.
[1490.32 → 1494.24] But another one that I'm really quite happy about was OpenStack,
[1495.14 → 1499.34] which was the collaboration between NASA and Rackspace.
[1499.34 → 1504.48] This is the open source web framework, or I guess cloud framework?
[1505.06 → 1506.52] Yeah, it's a cloud computing thing.
[1506.68 → 1509.30] And to be honest, given that it has the word cloud in the name,
[1509.36 → 1511.54] I'm not even really sure what it does, but...
[1511.54 → 1514.58] It's a set of APIs they build on top of the different virtualization layers.
[1515.16 → 1521.24] So you can control like a VMware stack as well as all the other different ones, I believe.
[1521.58 → 1525.10] And it includes some other things and specs on top of that as well.
[1525.66 → 1527.18] Storage, compute, the whole nine yards?
[1527.18 → 1528.00] Yeah, all of that.
[1528.00 → 1531.40] It's really some other things where I get a little bit fuzzy.
[1531.58 → 1535.68] But regardless of what it is, it's used by NASA to control thousands of computers.
[1535.90 → 1537.02] So that is cool.
[1537.42 → 1540.58] You must be a hit at Christmas and Thanksgiving when you go home and, you know,
[1540.94 → 1543.80] look, Mom, doing Lucas and NASA.
[1544.58 → 1545.58] You know what?
[1546.28 → 1550.48] My family is very diverse and eclectic.
[1551.06 → 1553.36] My sister is an acoustic physicist.
[1554.32 → 1554.66] Wow.
[1554.66 → 1557.60] My other sister is a rock star.
[1558.50 → 1559.46] You just...
[1559.46 → 1561.56] It's hard to impress anybody in that family.
[1561.86 → 1565.96] In fact, my father, I don't know if you've ever heard him speak,
[1566.06 → 1568.82] but he was a keynote speaker at Pylon and Oz Con.
[1568.94 → 1572.38] So even if you just restrict my family's achievements to open source,
[1572.82 → 1576.74] I'm still kind of not necessarily at the top of the heap.
[1576.74 → 1578.54] So, yeah.
[1578.76 → 1580.86] But it's great to be in a family like that.
[1581.52 → 1583.82] So I was going to ask, who's your programming hero?
[1584.00 → 1585.22] Is your dad in the list?
[1586.10 → 1588.20] It might sound a little corny, but yeah.
[1589.98 → 1592.46] I always thought of my dad as my programming hero,
[1592.62 → 1594.56] but I didn't actually know that much about what he did.
[1594.56 → 1598.40] He worked a lot on systems in the finance sector,
[1599.28 → 1603.88] and I was a little kid, so I didn't really understand what he did.
[1604.60 → 1608.60] But I actually worked at a startup a couple of years ago
[1608.60 → 1610.36] with one of his coworkers,
[1610.84 → 1612.38] and that experience was fascinating
[1612.38 → 1614.78] because apparently I write code very much like my father.
[1616.08 → 1620.00] There are similarities between Twisted and some systems that he worked on,
[1620.04 → 1622.64] and the more that I've learned about what his career was like
[1622.64 → 1623.84] and the kind of stuff that he did,
[1624.64 → 1627.48] the more that he's my programming hero.
[1627.82 → 1629.56] The force is strong with this one.
[1632.74 → 1633.66] Yeah, that's a metaphor.
[1634.18 → 1636.22] It's a little uncomfortably close to home.
[1637.16 → 1638.90] If you've ever met my dad, you know what I mean.
[1641.64 → 1643.78] So what's coming up on your open source radar?
[1643.78 → 1646.32] What new projects are you excited about?
[1646.32 → 1654.64] You know, it's very hard to choose something.
[1655.06 → 1656.78] I'm just...
[1656.78 → 1658.36] In the world of open source,
[1658.52 → 1660.02] I think what I'm really glad about
[1660.02 → 1664.20] is that we are experiencing this massive renaissance.
[1665.32 → 1667.56] It's hard to get excited about any single project
[1667.56 → 1669.08] because every time I want to do something,
[1669.38 → 1673.10] I just type a search into my web browser,
[1673.10 → 1676.68] and there's something that does something like what I want
[1676.68 → 1678.88] in the open source space.
[1678.98 → 1683.02] And then even in the relatively small niche of Twisted,
[1683.36 → 1687.02] there are just tons of libraries
[1687.02 → 1689.40] that people are writing every day.
[1691.84 → 1694.80] I'm really kind of excited about
[1694.80 → 1698.44] the minor renaissance that Twisted is enjoying, too.
[1698.50 → 1700.96] The last couple releases, we've gotten out on time.
[1700.96 → 1703.12] We've gotten new features.
[1703.56 → 1707.12] For a while, development was slowing down a bit.
[1707.20 → 1709.92] We had a lot of bugs to fix for a long time.
[1710.66 → 1712.66] We transitioned from that process,
[1713.10 → 1715.56] a process that was a wild west,
[1716.22 → 1719.24] kind of commit anything you want to...
[1719.24 → 1720.48] Everything has to be unit tested.
[1720.58 → 1721.60] Everything had to be documented.
[1721.98 → 1723.88] And for a little while, that slowed us down.
[1723.96 → 1725.46] But now that we're reaping the benefits
[1725.46 → 1726.40] of having done that,
[1726.40 → 1729.98] you can actually see on twistedmatrix.com
[1729.98 → 1731.16] slash high scores,
[1731.92 → 1736.40] the review points that people are accumulating.
[1738.82 → 1741.84] And if you click on that left arrow,
[1742.12 → 1743.12] go back a couple of months.
[1743.14 → 1744.36] I love that 8-bit interface.
[1747.26 → 1748.48] I'm glad you appreciate it.
[1748.52 → 1750.88] The font was the first thing that went into that web app.
[1751.44 → 1752.10] I can see.
[1752.10 → 1755.68] This avatar is 8-bit, so...
[1755.68 → 1756.72] I'm stuck in an 8-bit world.
[1758.00 → 1759.58] So, Glyph, one last question.
[1760.06 → 1761.08] Is this your real name,
[1761.16 → 1763.60] or is your name like a symbol like Prince was,
[1763.70 → 1765.40] where you just had to shorten it to Glyph
[1765.40 → 1766.68] to make it pronounceable, or...?
[1767.24 → 1770.70] No, Glyph, as a handle, predated the symbol.
[1771.50 → 1773.42] When I started using Unix,
[1773.48 → 1775.16] I needed a short handle
[1775.16 → 1777.48] that was easy to type,
[1777.48 → 1779.48] because I had to type...
[1781.10 → 1783.48] As I started off...
[1784.70 → 1786.44] Like, when I started using Unix,
[1786.52 → 1789.30] I was using a macOS 8 machine,
[1789.80 → 1792.22] and so I needed to type my username all the time
[1792.22 → 1793.14] because it wasn't implicit.
[1793.30 → 1794.84] It wasn't part of my environment.
[1795.10 → 1796.66] So every time I connected somewhere,
[1796.72 → 1797.28] I had to type it.
[1797.44 → 1800.12] So five letters was shorter than my real name.
[1801.80 → 1803.24] But it is not my legal name,
[1803.24 → 1806.26] and I don't talk about my legal name
[1806.26 → 1809.44] because it's kind of a little in-joke
[1809.44 → 1810.66] on the open-source community.
[1811.94 → 1815.58] My hypothesis is that nobody really reads licenses
[1815.58 → 1817.36] or knows what license things are under,
[1817.74 → 1820.26] and this is validated by the fact
[1820.26 → 1822.36] that most people don't know my real name,
[1822.78 → 1826.28] but for, I think, 7 out of the 10 years
[1826.28 → 1827.24] that Twisted's been going,
[1827.24 → 1829.36] it was at the top of every single file
[1829.36 → 1830.48] in the Twisted repository
[1830.48 → 1832.32] in the license statement.
[1832.32 → 1834.04] It said copyright, my real name.
[1834.88 → 1836.72] So are you like the why-gawky stiff
[1836.72 → 1837.72] of the Python community?
[1838.82 → 1840.88] I'm not going to randomly disappear
[1840.88 → 1842.38] from the internet one day, I hope.
[1843.80 → 1844.24] Asynchronously.
[1846.04 → 1846.52] Yes.
[1847.24 → 1848.30] He'll promise to be back, right?
[1850.30 → 1851.32] Well, if I did it asynchronously,
[1852.02 → 1855.58] I would be the doctor of the Python community.
[1855.58 → 1859.86] But I can only hope to be
[1859.86 → 1862.00] as witty and prolific as why.
[1863.24 → 1863.60] Indeed.
[1863.92 → 1865.26] Well, thanks so much for joining us,
[1865.38 → 1867.88] telling the world and all of our listeners
[1867.88 → 1868.80] about Twisted.
[1868.90 → 1869.86] It's been out there for a while,
[1870.00 → 1871.82] but definitely good stuff.
[1871.92 → 1875.02] And I wanted to get down with this project
[1875.02 → 1876.22] just because it seems like every time
[1876.22 → 1877.72] we talk about Node.js,
[1877.92 → 1878.58] it comes back to,
[1878.66 → 1879.60] oh, that's just like Twisted.
[1879.60 → 1881.94] Well, thank you for the opportunity.
[1882.16 → 1884.28] And if I might just one last interjection,
[1884.48 → 1888.32] since your co-host mentioned that he had no reason
[1888.32 → 1889.38] to get into Twisted,
[1889.46 → 1890.72] he was looking for a reason to do it.
[1891.12 → 1892.74] I would just like to leave your listeners
[1892.74 → 1894.60] with something that they might do.
[1895.64 → 1898.62] Twisted includes a bunch of command line utilities
[1898.62 → 1900.90] for running all the servers that it includes.
[1900.90 → 1903.54] So if you're the average source,
[1903.62 → 1905.14] sort of open source nerd
[1905.14 → 1906.50] who runs a personal server,
[1907.12 → 1910.68] you can replace all of your personal network infrastructure
[1910.68 → 1912.70] with, instead of bind,
[1912.82 → 1914.62] you can run Twisted DNS.
[1914.96 → 1915.88] Instead of Apache,
[1916.02 → 1917.14] you can run Twisted web.
[1918.20 → 1919.34] And instead of hybrid,
[1919.50 → 1920.90] you can run Twisted words,
[1921.08 → 1922.74] dash IRC port.
[1923.68 → 1924.24] So you can,
[1924.94 → 1927.08] pretty much any network service
[1927.08 → 1928.68] that you're interested in playing around with,
[1928.68 → 1930.62] you can start off by just typing one command line.
[1930.72 → 1932.50] You don't need to write a whole ton of code to get into it.
[1932.96 → 1933.24] Fantastic.
[1933.40 → 1934.42] Even SSH server, right?
[1934.48 → 1935.22] With Twisty Conch?
[1935.48 → 1935.70] Yep.
[1936.04 → 1936.66] Twisty Conch.
[1937.22 → 1938.32] SSH, of course, with the crypto,
[1938.46 → 1940.26] you've got to generate some keys and do a little more.
[1940.34 → 1942.10] So that's the reason I don't open up with that one.
[1942.28 → 1942.96] But yeah,
[1943.10 → 1946.18] it is a functional replacement for OpenSSH.
[1946.32 → 1948.78] It does authorize key authentication and everything.
[1949.02 → 1951.08] Now, does that work well as a client as well?
[1952.16 → 1952.52] Yes.
[1952.52 → 1953.52] You can just run Conch.
[1954.04 → 1955.62] And it's more or less drag and drop,
[1956.04 → 1956.78] or sorry,
[1956.78 → 1960.42] drop-in replacement for the command line SSH,
[1960.50 → 1962.96] except it outputs a couple of log messages every so often.
[1963.30 → 1964.22] So I'm curious,
[1964.30 → 1966.54] how does that compare to Aramco?
[1969.38 → 1970.72] You can run it in any,
[1970.80 → 1973.78] a client in any Twisted server.
[1973.94 → 1975.86] That's the difference between that and Aramco.
[1976.32 → 1977.80] Oh, because it's 100% Python.
[1977.96 → 1979.42] There are no dependencies at all, right?
[1980.04 → 1982.20] Well, there's some C crypto dependencies,
[1982.52 → 1985.14] but the application logic is all Python.
[1985.14 → 1986.72] The network I.O. is all Twisted.
[1986.82 → 1988.20] It doesn't use any special.
[1988.58 → 1988.98] Fantastic.
[1989.06 → 1989.82] Network I.O. stuff.
[1989.90 → 1992.14] It just reads the bytes and does some crypto on them.
[1992.62 → 1993.12] Sounds good.
[1993.52 → 1996.14] Sounds like you claimed Canada's upcoming weekend.
[1996.50 → 1997.10] No, no, no.
[1997.24 → 1997.62] Excellent.
[1998.18 → 1998.94] Next month.
[2000.28 → 2000.68] Cool.
[2000.74 → 2001.40] Well, thanks again, Cliff.
[2001.44 → 2002.42] We surely appreciate it.
[2003.06 → 2004.22] And thanks again for the opportunity.
[2004.22 → 2022.08] We'll be right back.
[2022.10 → 2022.70] Thanks again.
[2022.70 → 2023.22] Bye.
[2023.22 → 2023.54] Bye.
[2023.54 → 2023.72] Bye.
[2023.72 → 2024.18] Bye.
[2024.96 → 2025.68] Bye.
[2025.82 → 2026.36] Bye.
[2026.64 → 2027.14] Bye.
[2027.82 → 2028.82] Bye.
[2029.00 → 2030.08] Bye.
[2030.92 → 2032.12] Bye.
[2032.32 → 2032.94] Bye.
