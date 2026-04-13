[0.00 → 4.88] I think of data sets as sort of, we want them to be living data sets, right?
[4.92 → 6.84] It's sort of like a garden.
[7.02 → 8.94] You know, you've got to prune it, and you've got to water it.
[9.02 → 15.50] And so on of the things that I think ML Commons is uniquely positioned to do is to be that
[15.50 → 19.00] organization that does sort of maintain it for the community.
[19.42 → 24.42] We've got engineers who are, their full-time work is to help maintain and improve this.
[24.42 → 29.16] So, you know, we are looking at new data sets that, again, we think will push the needle forward.
[30.00 → 35.14] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[35.36 → 36.10] We love Linde.
[36.16 → 37.58] They keep it fast and simple.
[37.72 → 40.06] Check them out at linode.com slash changelog.
[40.30 → 42.38] Our bandwidth is provided by Vastly.
[42.72 → 46.28] Learn more at fastly.com and get your feature flags powered by Launch Darkly.
[46.54 → 48.26] Get a demo at launchdarkly.com.
[49.72 → 54.98] Changelog++ is the best way for you to directly support practical AI.
[55.62 → 59.90] Join today and unlock access to a private feed that makes the ads disappear
[59.90 → 65.88] gets you closer to the metal and helps sustain our production of practical AI into the future.
[66.72 → 72.64] Simply follow the Changelog++ link in your show notes or point your favourite web browser
[72.64 → 74.96] to changelog.com slash plus.
[74.96 → 79.16] Once again, that's changelog.com slash plus.
[80.54 → 82.92] Changelog++ is better.
[89.90 → 97.00] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[97.32 → 99.08] productive, and accessible to everyone.
[99.40 → 103.48] This is where conversations around AI, machine learning, and data science happen.
[103.72 → 108.54] Join the community and Slack with us around various topics of the show at changelog.com slash community
[108.54 → 109.84] and follow us on Twitter.
[109.98 → 111.54] We're at Practical AI FM.
[111.54 → 120.94] Welcome to another episode of Practical AI.
[120.94 → 122.82] This is Daniel Whiten ack.
[122.98 → 128.98] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson,
[129.26 → 131.92] who is a tech strategist at Lockheed Martin.
[132.20 → 132.84] How are you doing, Chris?
[133.00 → 133.98] I'm doing very well.
[134.18 → 139.36] Happy New Year as we are in the early winter of 2022 now recording this.
[139.36 → 143.18] Yes, the very cold early winter of 2022.
[143.86 → 148.18] Yeah, I think our listeners will probably have heard another episode this year, but this
[148.18 → 150.44] is the first that we're recording in the new year.
[150.62 → 153.06] So happy New Year to everyone again.
[153.78 → 161.20] But it's always good at the new year to revisit certain things or look forward to things that
[161.20 → 162.24] you thought about last year.
[162.30 → 168.82] And it's cool that we have David Cantor with us, who is the executive director at ML Comments,
[168.82 → 172.36] because we had a great conversation with David last year.
[172.70 → 176.96] It'll be good to catch up on all the amazing stuff that ML Comments is doing.
[177.10 → 177.82] So welcome, David.
[178.20 → 178.68] Thank you.
[178.82 → 180.08] It's great to be back.
[180.34 → 181.58] Happy New Year to everyone.
[181.76 → 186.56] I also have to point out, it is only cold if you aren't in California.
[187.14 → 187.60] Yes.
[187.60 → 195.76] Well, I certainly am not, at least judging by my walk into the co-working space today.
[196.02 → 197.62] Definitely not California.
[198.30 → 203.76] Although our listeners can't see, but you are wearing like a hoodie zip up type of thing.
[203.98 → 204.68] Oh, no, no, no.
[204.68 → 205.24] It's not a hoodie.
[205.38 → 206.18] It's a fleece.
[206.34 → 207.62] But it's also a fleece.
[207.74 → 208.86] I got to have my own logo.
[208.98 → 209.34] Right.
[209.46 → 210.12] It's swag.
[210.26 → 210.46] Yeah.
[210.60 → 211.54] You're looking good, man.
[211.68 → 212.00] Sure.
[212.26 → 212.44] Sure.
[212.44 → 212.88] Yeah.
[213.08 → 215.24] I'm in San Francisco, for those who don't know.
[215.38 → 216.62] And like, we should be clear.
[217.06 → 219.36] San Francisco weather is not LA weather.
[219.56 → 219.70] Yeah.
[219.88 → 220.86] That is true.
[221.16 → 221.30] Yeah.
[221.30 → 223.90] I've been there on occasion when that is apparent.
[224.40 → 225.36] So yeah.
[225.74 → 226.62] Welcome back.
[226.76 → 232.12] I know we had some introduction to ML Commons in our last episode, which we'll link in our
[232.12 → 232.74] show notes.
[232.74 → 238.56] But for those maybe that haven't heard that or maybe want a sort of refresher, could you
[238.56 → 244.22] just give us a little bit of an idea about what ML Commons is, why it exists, and what
[244.22 → 245.96] are some of the things that you're doing?
[246.52 → 247.30] Yeah, absolutely.
[247.54 → 252.86] So the mission of ML Commons is really making machine learning better for everyone.
[253.44 → 258.40] So I think of our goal as being, you know, sort of how do we stimulate innovation in ML
[258.40 → 262.16] in a way that, you know, really benefits society and the whole world.
[262.74 → 268.32] So we were started, you know, it was a very informal collaboration starting in 2018.
[269.02 → 276.00] But we actually formed a nonprofit in 2020 that I am, you know, the founder and executive
[276.00 → 276.64] director of.
[276.72 → 277.86] We've got an amazing team.
[278.04 → 279.44] And it's an industry consortium.
[279.50 → 285.44] So we're bringing together a lot of heavyweights in the ML world from the systems side, from
[285.44 → 289.36] the software side, from the cloud side, you know, who are all focused on this.
[289.36 → 295.64] And we, you know, that mission of making ML better for the whole world, we have sort of
[295.64 → 297.10] three real pillars to that.
[297.24 → 299.82] And one is benchmarks and metrics.
[300.64 → 306.26] And so the first thing that a lot of people know us for is Alpert, which are the industry
[306.26 → 312.74] standard benchmarks for the speed of training neural networks and doing inference.
[313.10 → 316.36] And, you know, actually, one of the things that's been really cool since we've talked is,
[316.36 → 319.86] you know, I think when we first talked, we might have only had two of the benchmarks in
[319.86 → 320.74] our suite up and running.
[321.16 → 325.14] And we're now, what I like to say is covering from microwatts to megawatts.
[325.26 → 329.92] So the smallest systems we've measured performance on are like, you know, maybe tens of microwatts,
[329.98 → 335.50] you know, really deeply embedded IoT devices up to the world's number one supercomputer, which
[335.50 → 336.56] is 20 megawatts.
[337.26 → 339.08] And sort of everything in between.
[339.20 → 341.38] And so, you know, you can see what's really cool.
[341.38 → 345.62] And I have some slides that I use in keynotes saying like, hey, if you look at the two and
[345.62 → 350.66] a half year we've been around, you would expect that just through Moore's law alone,
[350.84 → 353.66] ML solutions would be about two and a half X faster.
[353.92 → 355.12] And that's great, right?
[355.20 → 358.66] You know, we want to make your life easier, Daniel, when you're doing the work.
[358.98 → 365.28] But if you look at the Alpert data that we have, actually, it's more like 16 to 30 X faster.
[365.42 → 369.28] And so it's really cool to see, you know, when you get benchmarks and when you get metrics and
[369.28 → 373.88] everyone starts really rowing in the right direction, the kind of momentum you can get in
[373.88 → 374.22] the industry.
[374.32 → 379.32] So that's one example of ways we can make ML better for everyone is just, you know, being
[379.32 → 384.02] able to train bigger models and do it faster and really bring those capabilities out.
[384.40 → 389.14] Sort of the second pillar is the one that brings me here is our data sets.
[389.96 → 395.02] And, you know, I like to think of data sets as really being the raw ingredient for ML.
[395.02 → 402.38] If the industrial revolution was powered by iron and coal, not the most environmentally
[402.38 → 404.88] stuff, you know, we're really powered by data, right?
[405.02 → 410.26] And it's, you know, I think at SIL, right, you guys understand that just as well as everyone
[410.26 → 410.54] else.
[410.60 → 415.60] You know if you want to start talking in new languages or working with new texts, you can't
[415.60 → 420.42] get from English to Urdu without some new data, right?
[420.42 → 427.90] And bringing large scale, open, nicely curated data is a huge boon for the industry because
[427.90 → 432.78] even at some of the biggest shops in the world, you know, places like Google or Amazon, their
[432.78 → 439.54] researchers want to use public data because the whole point is that you're sharing techniques
[439.54 → 441.94] that everyone can use and driving the industry forward.
[442.28 → 443.28] Yeah, that's fascinating.
[443.54 → 448.46] Sometimes I get the question when I'm working on various data sets, like what the benefit,
[448.46 → 453.78] and like you said, we deal with this at SIL too, like we have a bunch of data in our archive
[453.78 → 458.06] or wherever that linguists have gathered like over very long time.
[458.28 → 463.24] And sometimes the question comes up, well, like, first off, why would anyone in the industry
[463.24 → 467.38] be interested in sort of like this strange data?
[467.60 → 468.70] And we can answer that.
[468.78 → 472.44] But then secondly, like, why would we want to make this open?
[472.44 → 478.76] And like, how would that benefit like our organization to work on open data sets versus
[478.76 → 482.04] like closed and proprietary stuff?
[482.18 → 485.38] When you're having those conversations, how do you express that to people?
[485.38 → 492.98] Like the maybe the business sort of case for contributing to open data sets?
[492.98 → 496.42] Because you do engage with large organizations on the data sets you work with.
[496.42 → 499.26] So how is that phrased to their sort of leadership?
[499.86 → 502.58] Yeah, so I think it depends on the companies, right?
[502.62 → 508.34] So there are some companies where their data really is a critical differentiator, and they
[508.34 → 510.08] probably don't ever want to open it.
[510.54 → 515.22] But even in the case where that is true, so like, I'll give you an example.
[515.56 → 522.08] So there's a company, Writer, in Europe that actually was really fantastically cooperative
[522.08 → 529.00] and opened up one of their data sets for our use, it was an older data set that they weren't
[529.00 → 532.40] super concerned about a competitor having access to, right?
[532.40 → 537.54] And they said like, look, if you use this data set for your benchmarks, systems are going
[537.54 → 539.90] to get faster for what we want to do.
[540.60 → 546.12] So this is a way that you can kind of, in some ways, punch above your weight in getting
[546.12 → 548.04] the attention of the industry, right?
[548.06 → 551.28] And I'm sure you've talked to folks about how, you know, when you start training on a data
[551.28 → 555.10] set, the models begin to specialize a bit for that.
[555.24 → 561.50] And so, you know, if you want your use case to be popular, making it open is a perfect
[561.50 → 561.68] one.
[561.74 → 566.32] And then a lot of our member companies, you know, if you look at someone like Intel or
[566.32 → 571.82] NVIDIA, more open data means more ML, means more people doing cool things with computers,
[571.82 → 572.78] means more sales.
[572.78 → 578.04] So, you know, in a lot of cases, I think you hit the nail on the head, which is as a nonprofit
[578.04 → 581.66] and industry consortium, I can't force people to do what they don't want to do.
[581.86 → 587.80] I can provide persuasion and I can try to help them understand where our interests are aligned.
[587.80 → 590.30] And I think there are a lot of ways where that's great.
[590.46 → 594.32] Or, you know, Chris, you work in the defence and intelligence community.
[594.32 → 598.96] So I had a really cool meeting late last year with some folks there.
[599.20 → 604.34] And one of the things they were saying that they love about open data is certain parts
[604.34 → 608.20] of that community have real difficulty spending money through normal channels.
[608.94 → 614.12] And one of the interesting things specifically about speech is by and large, the intelligence
[614.12 → 620.34] community tends to care about languages that are not very commercially viable for like regular
[620.34 → 621.08] products, right?
[621.16 → 621.28] Sure.
[621.28 → 623.72] There's not as much interest.
[624.04 → 625.62] Let's rewind to 10 years ago.
[625.80 → 630.32] If you asked like, you know, the CIA or whoever, like what language would you love to have like
[630.32 → 631.58] an auto-magical translator?
[631.72 → 633.40] They'd be like, oh, Arabic for sure, right?
[633.88 → 636.92] And they wouldn't have said English or Mandarin, right?
[636.96 → 642.52] Which are, you know, probably the two most popular speech data set flavours out there, right?
[642.52 → 642.68] Sure.
[642.68 → 651.60] And so, yeah, I think just open data is hugely powerful in enabling researchers and everyone
[651.60 → 653.82] to sort of work together on these problems.
[654.00 → 657.86] Do you think there's a cultural aspect to it in terms of people getting used to this idea?
[658.20 → 661.68] Because when you position it like that, you can clearly see the business case for it.
[661.68 → 666.52] I know in my experience, it seems like some years back we went through this with open source
[666.52 → 670.16] software and people struggled to see that business case and understand.
[670.42 → 673.92] And now it has swept almost all aspects of business.
[674.12 → 680.80] Do you envision that use case benefit in terms of being able to influence how things go and
[680.80 → 685.48] participate that in a larger scale that that is going to be more widely adopted over the years
[685.48 → 685.66] ahead?
[685.66 → 686.94] Yeah, I think so.
[687.16 → 691.56] And I mean, I think one of the other things that I'd say is, you know, when you look at
[691.56 → 697.14] open data, in a lot of cases, even where you might be differentiating via your own data,
[697.64 → 699.86] like in a lot of cases, it's going to be additive, right?
[699.94 → 704.16] So let's say you want to do a medical transcription thing.
[704.42 → 711.22] You might not want to donate to the wide world like all of your work on translating and decoding
[711.22 → 714.94] specialized medical terms like tachycardia, right?
[714.94 → 721.18] But if you were going to do train like a natural language model, you know, some version of say
[721.18 → 722.26] BERT, right?
[722.30 → 728.60] You might start with BERT on a large public data set like Wikipedia or a crawl of the web.
[728.76 → 734.30] And then you'd say, well, you know, I'm going to add on my special sauce later to fine tune
[734.30 → 735.92] or supplement or augment that.
[736.02 → 742.86] And so on of the ways I think about this is that getting from zero to product is a really
[742.86 → 744.22] big push.
[744.56 → 747.74] And you need the data to get there, but it's not the only thing you need, right?
[747.76 → 750.74] There's also the whole process of how do I productize it?
[750.76 → 751.70] How do I test it?
[752.00 → 756.08] How do I make sure it's not going to do, you know, wild and crazy things that I don't expect?
[756.08 → 762.16] And if I as an organization can provide some open data and get the whole world a few steps
[762.16 → 766.16] down that path and sort of accelerate things, that's just good for everyone.
[766.34 → 766.72] I'm curious.
[766.88 → 768.26] I got a follow-up for you on that.
[768.34 → 772.12] And that is, I know that there are people listening to this because it's in my head as
[772.12 → 776.24] well that are thinking my organization needs to do better on that.
[776.24 → 783.38] And as we talk about the decision point about how do I make the business case, and what should
[783.38 → 788.22] go open, what should we keep as our secret sauce and all that, any guidelines on how to
[788.22 → 789.02] make such an evaluation?
[789.02 → 795.12] I realize that use cases vary a lot, but I have had conversations with people where they
[795.12 → 798.70] either want to just throw everything open or they want to do everything as their special
[798.70 → 799.14] sauce.
[799.24 → 804.32] But there doesn't seem to be a method to the madness on what constitutes the two.
[804.32 → 810.70] How would an organization do that, recognize that by going open, they selfishly, they get
[810.70 → 814.16] the benefit of being able to steer things, but they still get to keep their secret sauce.
[814.24 → 816.90] Any thoughts about how to make such an evaluation?
[817.56 → 817.74] Yeah.
[818.00 → 821.64] So the other thing I was actually going to mention is, you know, one of the things that
[821.64 → 826.70] our organization is very dedicated to is the maintenance and upkeep of these.
[826.86 → 833.36] And, you know, so if you think of ImageNet, right, that really started this round of innovation
[833.36 → 834.48] in machine learning, right?
[834.50 → 839.94] And then it was ImageNet and then the realization that, hey, Alex Net plus GPUs plus ImageNet
[839.94 → 841.74] beats humans at image recognition.
[841.88 → 842.44] Oh, my gosh.
[842.48 → 842.68] Right.
[842.76 → 845.48] And now ImageNet is fantastic.
[845.48 → 846.16] It's amazing.
[846.40 → 848.24] But, you know, now it's old.
[848.74 → 849.82] It hasn't been updated.
[850.44 → 853.06] There are some legal issues associated with the licensing.
[853.36 → 857.60] And, you know, so imagine we're doing speech to text, and we did that in 2019.
[857.60 → 863.24] That model, that data set would not have anything about COVID or coronavirus or any of these other
[863.24 → 863.48] things.
[863.54 → 865.14] So, you know, you want to keep these things up to date.
[865.26 → 867.22] And that does cost some amount of money.
[867.38 → 871.74] And so by offloading that to the community or, you know, ML Commons, we're curating our
[871.74 → 872.10] stuff.
[872.30 → 874.04] It's part of where our budget goes.
[874.20 → 877.94] That can be very helpful in terms of combining community resources.
[878.12 → 880.88] And so that's another aspect of the business case.
[880.96 → 885.58] But to answer your question, I think it is very easy to slide into these binaries, right?
[885.58 → 887.54] It's just it's a very natural way of thinking.
[887.72 → 897.22] And where we've had a lot of success, I think, is usually where there is some sort of research
[897.22 → 902.54] folks involved or, you know, some sort of specialist who can think about this and reason about it.
[903.10 → 907.48] This kind of endeavours inevitably involve your legal department.
[907.92 → 908.66] That's a great point.
[908.84 → 910.94] And we don't want to get folks in trouble.
[911.50 → 913.76] And so there are all sorts of issues about how is it collected?
[913.92 → 914.96] Do you have the right permissions?
[914.96 → 916.10] Do you have the right permissions, GDPR?
[916.52 → 922.64] And a lawyer is probably not going to be able to give you the insights as to what is
[922.64 → 925.32] commercially valuable, what is commercially threatening?
[925.80 → 927.66] Could it be monetized in other ways?
[927.88 → 929.94] Or no, is this just the thing that makes sense?
[929.98 → 935.52] So you kind of do need some element of the business and potentially technical community.
[935.66 → 938.84] And so we've found that that is oftentimes a very helpful driver.
[938.84 → 946.32] One of the things that is beautiful about the machine learning community is I think there's an openness is in our DNA.
[946.88 → 951.60] And so I think for a lot of researchers, that is sort of a default mode of thinking.
[951.60 → 952.56] And that is helpful.
[952.56 → 972.64] We deserve a better internet.
[972.64 → 975.90] And the Brave team has the recipe for bringing it to us.
[976.10 → 977.04] Start with Google Chrome.
[977.28 → 981.00] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[981.20 → 982.08] Rip out the Google bits.
[982.20 → 982.84] We don't need them.
[983.20 → 985.72] Mix in ad and tracker blocking by default.
[985.98 → 988.68] Quick access to the Tor network for true private browsing.
[988.98 → 993.38] And an opt-in reward system so you can get paid to view privacy-respecting ads.
[993.58 → 997.32] Then turn around and use those rewards to support your favourite web creators like us.
[997.32 → 1002.34] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1017.86 → 1024.96] So David, as ML Commons was thinking about this sort of pillar of data sets.
[1024.96 → 1032.56] And obviously, there are a lot of different data sets that could be valuable to the ML community.
[1032.98 → 1039.24] And all sorts of data, whether that be one type of data or multimodal data or like all sorts of things.
[1039.60 → 1047.20] How did ML Commons sort of settle on an initial maybe focus on speech data?
[1047.30 → 1054.12] Because I know we'll be kind of transitioning to talk about a couple of the very impressive data sets that were recently released.
[1054.12 → 1058.04] But they're both speech data sets or speech-related data sets.
[1058.14 → 1059.66] So how did that come about?
[1060.08 → 1060.24] Yeah.
[1060.46 → 1073.00] So when I think about the data set problems that I want my organization to or the organization I serve to tackle, I sort of think about it as two sides of the equation, return and investment.
[1073.42 → 1076.08] And by return, I really mean what's the impact, right?
[1076.08 → 1085.10] And so I want to be working on problems that will have an impact where we're going to provide some very clearly differentiated, very valuable things that the community doesn't have.
[1085.30 → 1091.92] If all you do is produce something that already exists with a slightly friendlier license, that can have a big impact.
[1092.22 → 1099.64] But, you know, it's not as great as, you know, I'm now one of our data sets, right, is the first in many, many languages, right?
[1099.64 → 1104.26] That's like a qualitative change in the landscape that's like really exciting.
[1104.82 → 1108.78] And then the other side of that is, do we have the right people to do it?
[1108.94 → 1111.68] And what is the investment that's involved there?
[1111.70 → 1113.44] And can we bring that skill set together?
[1113.44 → 1115.12] And are we uniquely positioned to do that?
[1115.34 → 1121.44] And for us, speech was very much ground zero for a couple of reasons.
[1121.44 → 1134.18] So one is we actually want to build up the infrastructure around building these data sets because part of the theory behind our organization is that actually a lot of the plumbing behind the scenes, there's some commonality to it.
[1134.20 → 1135.56] And sharing that can be helpful.
[1136.06 → 1140.34] I mean, obviously, there's greater alignment between two speech data sets than, you know, speech and vision.
[1140.52 → 1143.74] But still, there's a lot of just general wrangling you got to do.
[1143.74 → 1150.84] And also, some of the leads on our project had prior experience building speech data sets.
[1151.52 → 1159.48] And there was a very real desire to have, and all of our data sets are permissively licensed for both research and commercial use.
[1159.96 → 1167.90] And there's a real desire to build something big enough to train an end-to-end speech model on and then begin to tackle diversity.
[1167.90 → 1172.54] And so those things all kind of lined up for us in that there was sort of a gap in what was out there.
[1172.68 → 1176.32] And we had the right expertise, and we thought that the impact would be big.
[1176.78 → 1176.84] Yeah.
[1176.98 → 1184.30] So maybe you could just describe generally there's two large data sets that you've released recently.
[1185.04 → 1188.94] You know, we'll link, of course, to the specific information about those.
[1189.04 → 1192.72] And people can obtain them and download them and start working with them.
[1192.72 → 1197.94] But maybe just give us a picture of each of those and what the goal was with each one.
[1198.54 → 1198.78] Yeah.
[1198.98 → 1202.00] So the first one is called the people speech.
[1202.06 → 1205.44] And I think I talked with you guys about this last year.
[1205.74 → 1211.60] And that is 30,000 hours of labelled speech data.
[1211.78 → 1215.78] And it's sort of intended for speech recognition purposes.
[1215.78 → 1217.40] But you can use it for a lot of other things.
[1217.40 → 1223.60] We've had people who downloaded it to do, like, denoting filters for acoustical applications.
[1224.42 → 1228.24] And it's, like I said, permissively licensed conversational speech.
[1228.32 → 1232.62] So it's not just read audiobooks, as was sort of common before.
[1233.32 → 1235.24] And it's very big.
[1235.36 → 1236.78] It's 30,000 hours.
[1236.78 → 1238.68] It's about, I think, two to three terabytes.
[1238.68 → 1247.70] And part of the point here is we've got, you know, when I think about speech, I sort of think about three dimensions to the data sets.
[1248.12 → 1249.14] One is size.
[1249.50 → 1251.38] One is the languages.
[1251.74 → 1253.68] And then the other is sort of the context.
[1253.84 → 1255.68] And, like, do you have noisy speech?
[1255.70 → 1257.94] Or is it, you know, something really clearly recorded?
[1258.08 → 1260.92] Are there kids playing in the background and other things like that?
[1261.00 → 1264.16] And so this is putting the stake in the ground on the size.
[1264.54 → 1266.34] And, you know, we can work on the other things.
[1266.34 → 1269.10] And, like I said, it's big enough to train an end-to-end model.
[1269.62 → 1273.18] So kind of over the 10,000 to 15,000-hour tipping point.
[1273.62 → 1277.94] So that is sort of going deep and big in the size dimension.
[1278.12 → 1284.92] And then the second one, which is nicely complementary, is the multilingual-spoken words corpus.
[1285.70 → 1292.50] And this is exciting because this is really pushing the boundaries on the diversity angle from the number of languages.
[1292.50 → 1297.54] And so that it's not for speech recognition but for keyword spotting, right?
[1297.64 → 1301.58] So recognizing keywords, a modest number of keywords.
[1301.82 → 1315.60] And it is 23 million clips that are each about one second long covering 340,000 keywords with 115,000 different source speakers in 50 languages.
[1315.60 → 1322.74] And the thing to me that's really cool about that is those 50 languages cover 5 billion human speakers, right?
[1322.80 → 1324.74] So this is the majority of the world's population.
[1325.18 → 1334.20] And most of these languages, this is the first existing data set for keyword spotting in those languages.
[1334.20 → 1337.12] And certainly the first under such a nice permissive license.
[1337.12 → 1342.44] And, you know, we're talking about languages that are not supported by these home assistants, right?
[1342.48 → 1349.68] If you, you know, I don't want to pick on any one company, but if you look at a lot of the home assistants or things like that, they might support a dozen languages.
[1350.30 → 1353.14] But there are a lot of languages where there's not a lot of support.
[1353.24 → 1357.46] And so, you know, bringing that capability to these new communities is really exciting.
[1357.56 → 1364.48] Like it was very cool to see some of the people tweeting about, hey, my language is in here or getting emails about how can I add my language?
[1364.48 → 1368.02] So that's pushing forward in a different dimension.
[1368.20 → 1369.34] But again, also speech.
[1369.72 → 1381.00] So I'm kind of curious, you know, I've worked with data sets from whatever, you know, the task that I'm focused on, but I've never done anything at the scale of having to put the data together.
[1381.40 → 1382.82] What's involved in that?
[1382.92 → 1391.24] You know if you're looking at you have the keyword spotting, and you have the speech recognition use cases, and you have massive amounts of content that you're doing,
[1391.24 → 1402.26] I would imagine that there is a level of organization and effort required way beyond what most of us that are just doing typical day-to-day machine learning models are having to deal with.
[1402.32 → 1403.38] How do you even start that?
[1403.46 → 1405.26] How do you approach such an engagement?
[1405.94 → 1406.20] Hmm.
[1406.48 → 1407.88] That's a perfect question.
[1408.06 → 1412.54] So our team is pretty small in terms of the number of engineers.
[1412.54 → 1419.80] So I'm not sure that, you know, resource wise, it's not like, you know, we're coming in with 10 people or whatever, full-time or anything like that.
[1420.16 → 1427.48] You know, I would say I think the thing that we really wanted to focus on was because we knew, as you said, this is like a big problem.
[1428.24 → 1431.00] I think we had to focus on things that scaled initially.
[1431.00 → 1440.20] And, you know, a perfect example of that is we did a back of the envelope calculation of like, okay, what would it take to label the data manually?
[1441.04 → 1446.66] And, you know, I think we calculated it would be on the order of about $10 million.
[1447.80 → 1449.34] That's a bit of a budget right there.
[1449.56 → 1449.78] Right.
[1449.86 → 1450.12] Yes.
[1450.14 → 1453.12] That's several years of budget for my nonprofit.
[1453.30 → 1454.60] And we've got to keep the lights on.
[1454.64 → 1456.06] We've got to pay the employees, you know.
[1456.36 → 1457.58] So that was out of the question.
[1457.58 → 1468.30] And so we actually I think one of the things we really wanted to focus on was building the tools and leaning into compute rather than manual labour.
[1468.64 → 1479.10] And so, you know, we were able to label the data and generate the labels using computer systems for under about $20,000.
[1479.50 → 1484.68] So I think it's sort of attention to that and building up the tools.
[1484.68 → 1486.78] And all the tools are open source, by the way.
[1486.78 → 1491.04] You know, not only can you go and get the data set, but you can get the tools we use to create it.
[1491.24 → 1499.50] And, you know, we'd love to see people updating them, fixing bugs, whatever it is, and see community adoption of all of those pieces.
[1499.80 → 1504.00] But, you know, it's also, again, yeah, I think it does come down to the right tools, right?
[1504.00 → 1507.34] If you're building one house, you want one set of tools.
[1507.54 → 1513.70] If you are building a 50-story apartment building or a dozen houses, you're going to, you know, have slightly different infrastructure.
[1513.70 → 1525.12] Yeah, I would be kind of curious to maybe dig a little bit into that because when you're creating a labelled data set, people might think, oh, I want gold standard data, right?
[1525.12 → 1530.04] Which necessarily in their mind means human labelled, right?
[1530.58 → 1534.66] Without a sort of machine in the loop of creating the gold standard data.
[1534.66 → 1546.62] So maybe describe a little bit more like why this sort of machine process can create something that's useful to train a machine on, I guess would be the question.
[1547.14 → 1547.24] Right.
[1547.36 → 1548.20] Or put another way.
[1548.30 → 1548.44] Okay.
[1548.48 → 1550.20] So the snake is eating its own tail.
[1550.30 → 1551.38] Does that actually work?
[1551.64 → 1551.82] Right.
[1551.82 → 1552.14] Right.
[1552.14 → 1552.50] Right.
[1552.60 → 1554.94] Or are we left, and we're like, there's no snake anymore.
[1555.62 → 1560.32] So first, I think the technical team had some great instincts here.
[1560.80 → 1567.26] And, you know, one of the big hypotheses is, as you say, like a lot of people will focus on extremely high quality data.
[1567.52 → 1575.90] But it's also pretty common that if you have some bad data in there, it may not really be a huge problem.
[1575.90 → 1582.96] And so I think part of this is accepting that a large amount of modest quality data.
[1583.06 → 1591.96] And actually we did, we can talk about some of the details because we did in generating the labels, we actually did figure out or try to estimate how many of them were good.
[1591.96 → 1595.40] And like a big chunk of it was done, you know, sort of perfectly.
[1595.80 → 1598.16] Some of it was done to sort of human quality.
[1598.66 → 1599.66] Some of it was worse.
[1599.88 → 1606.58] And, you know, I think there was a bit of a gamble there that that would ultimately prove to be useful.
[1606.78 → 1613.98] But we do know that machine learning is very good at handling kind of rough inputs.
[1613.98 → 1618.04] And so it seemed like a pretty good hypothesis there.
[1618.52 → 1626.40] You know, it's also the ways that a machine in the loop for labelling go wrong are going to be probably a lot different from a human.
[1626.92 → 1627.92] I'm just kind of curious.
[1628.24 → 1629.60] I'm sure Daniel already knows this.
[1629.72 → 1636.44] But as you're putting these data sets together, is it kind of one shot, and you're done and it's there?
[1636.52 → 1639.64] Or is there a management of that data set over time?
[1639.64 → 1645.22] Do you go back and relabel with new tools or anything or do you kind of move on to a whole new data set?
[1645.44 → 1647.32] How do you think about producing things?
[1647.82 → 1653.20] I guarantee you, like any engineer, we tried a few things and the first things did not work.
[1654.52 → 1655.84] I'll give you an example.
[1656.06 → 1660.76] I know we evaluated several different forced aligners.
[1660.76 → 1669.42] So we started for people's speech by scraping data where there was a transcript and the audio.
[1669.64 → 1675.04] But they weren't necessarily temporally aligned, which you need to train a speech to text model.
[1675.80 → 1684.76] So we did our own transcription using Cali with an Ngram language model.
[1684.98 → 1688.52] And so we came up with our estimated transcription.
[1688.94 → 1692.60] And then we reinforced alignment on that to get the timestamps right.
[1693.12 → 1695.06] And all of this audio came with subtitles.
[1695.40 → 1698.76] But just as an example, sometimes the subtitles are a little wonky, right?
[1698.76 → 1701.10] Like you might get a subtitle.
[1701.52 → 1704.74] Maybe the language spoken is French and the subtitle is in English.
[1704.82 → 1707.40] Or maybe it's a description of a picture or something like that.
[1707.40 → 1709.68] So you can get all sorts of fascinating problems.
[1710.44 → 1713.62] And so we tried different aligners.
[1713.92 → 1717.34] And we did find one that we thought solved some of these problems.
[1717.44 → 1718.28] Didn't solve all of them.
[1718.28 → 1721.28] But we definitely tried out a bunch of different things.
[1721.96 → 1735.72] And to us, one of the proof in the pudding sort of things was actually training a speech to text model on our data set and seeing how comparable it was to using something like Libra speech, which is much smaller, but it's sort of the gold standard today.
[1735.72 → 1739.86] And, you know, we got in the ballpark of Libra speech, which we're like, that's good enough.
[1739.92 → 1743.20] But I will tell you, we did not start out in the ballpark of Libra speech.
[1743.32 → 1745.02] There's, you know, all sorts of problems.
[1745.18 → 1748.40] You know, you have like mismatched transcripts where things are just, you know.
[1748.94 → 1752.22] But you find the problems, and you hammer them down one by one.
[1752.80 → 1753.74] That's my experience.
[1753.82 → 1754.08] I don't know.
[1754.14 → 1755.00] Daniel, what about you?
[1755.00 → 1759.62] Yeah, I mean, this is a sort of never, never ending process.
[1759.76 → 1759.96] Right.
[1760.02 → 1768.60] And I think like you were talking about ImageNet and others, you know, this is only like things get stale and need to be updated.
[1768.60 → 1774.08] And language especially is like always changing very rapidly.
[1774.08 → 1783.78] And like you say, if something was released like before COVID and you need like COVID health words and stuff after COVID, it needs to be updated.
[1784.08 → 1798.06] As part of your release, do you have a mechanism for people to like make sort of contributions or feedback or sort of human evaluation type of feedback or anything like that?
[1798.42 → 1798.64] Yeah.
[1798.82 → 1800.84] So, you know, again, we're big on community.
[1800.84 → 1806.94] We have an open Discord channel that you can drop in and tell us what's great, tell us what doesn't work.
[1807.44 → 1813.00] When we released it, as you might expect, the initial sets of comments were, this is really amazing, but we, you know, we found this hitch.
[1813.66 → 1815.36] So we're nailing those down.
[1815.48 → 1818.36] And we've got, you know, a Google group and mailing list for this.
[1818.52 → 1820.68] And so, and again, all the code is open source.
[1820.78 → 1822.86] So, you know, folks want to file bugs.
[1823.04 → 1829.28] And I mean, the thing to me that is most exciting is now that it's released, like a year from now, what are people doing with it?
[1829.28 → 1833.46] Like, to me, that's really the sort of thing that's very cool.
[1833.78 → 1842.74] One of the other things I would actually mention just briefly, you said an example of a scale thing that we had to work on is when we were initially doing the forced alignment,
[1842.74 → 1849.00] one of the things we found is that, you know, just using out-of-the-box software was not sufficiently fast.
[1849.62 → 1859.94] And so we actually had to go through and optimize our forced aligner, both the acoustic model and language model, and get them running on an accelerator, on a GPU.
[1860.64 → 1863.86] And at that point, we were able to get 250x real time.
[1863.86 → 1871.36] And so that's an example of paying attention to scaling and sort of systems where it's like, yeah, 30,000 hours is a lot.
[1871.46 → 1876.72] You don't want to be renting an Amazon instance for 30,000 hours because, A, we got to release it.
[1877.00 → 1881.94] But, OK, you cut that down by a factor of 250, and it's like, OK, we can rent a few of those, right?
[1882.02 → 1884.98] So there are all sorts of things that go into this.
[1884.98 → 1906.12] Changelog News is the best way to keep up with the fast-moving software world.
[1906.12 → 1914.48] We track, blog, and contextualize the coolest projects, the best practices, and the biggest stories each and every week.
[1914.48 → 1922.62] Make ChangeLog.com your daily destination or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[1923.22 → 1926.16] Join more than 15,000 enthusiastic readers.
[1926.44 → 1932.58] It'll cost you exactly $0, and you can subscribe right now at ChangeLog.com slash weekly.
[1944.48 → 1967.00] So being with SIL, I think I would probably get fired if I didn't ask a little bit about the particularly the data set with the spoken words.
[1967.00 → 1974.28] And your sort of attempt to, like you say, bring in a bit of diversity into speech data sets that were out there.
[1974.62 → 1986.16] Kind of as you look back on that, how does this data set stack up against maybe, like, what are other examples of data sets out there for spoken words?
[1986.16 → 1990.84] And how does this change the picture in terms of the diversity of languages?
[1991.64 → 1993.36] I know that's a great question.
[1993.56 → 1997.14] And that hits on sort of the things that I'm most proud of in some ways.
[1997.30 → 2002.16] So, you know, I think the gold standard is Google speech commands.
[2002.16 → 2007.92] And I am not as much of an expert on the keyword spotting area as the speech to text.
[2008.60 → 2017.98] But my understanding is that's a data set with about 105,000 one-second utterances covering 35 words in English.
[2018.58 → 2019.16] And it's great.
[2019.30 → 2021.60] You know, again, fantastic community resource.
[2022.28 → 2029.06] You know, and if you go back to what I said, we've got 340,000 keywords in 50 languages with 23 million clips.
[2029.06 → 2031.76] So there are 50 different languages we're covering.
[2031.76 → 2034.36] And, you know, some of them have very good coverage.
[2034.90 → 2041.68] And we sort of bucketed it into three categories, sort of low-resource languages, which is under 10 hours of data.
[2042.02 → 2046.26] So that would be something like Georgian, Tamil, Vietnamese, Arabic.
[2046.82 → 2048.96] And that's about half of the languages.
[2049.54 → 2053.98] And then we have medium-resource languages with between 10 and 100 hours.
[2054.44 → 2055.74] And that's 12 languages.
[2055.74 → 2064.12] And so some examples of that are, like, Czech, Ukrainian, which is actually that's the first Ukrainian data set of its kind for sure.
[2064.60 → 2066.42] Turkish, Portuguese, Indonesian.
[2067.04 → 2070.50] And then we've got high-resource languages, which is over 100 hours.
[2070.56 → 2076.62] And that includes, like, actually some reasonably obscure languages like Basque, Catalan, Persian.
[2076.62 → 2080.52] And then, of course, some standard ones like English, Welsh, et cetera.
[2080.86 → 2086.78] And so, you know, to me, the really exciting thing is that, first, it's a lot of languages.
[2086.98 → 2093.88] And also some of the work in this paper was about, okay, when we say low-resource, does that mean you can't use it?
[2093.88 → 2095.88] Or, you know, what does that really mean?
[2096.22 → 2107.32] And actually what we found is that you can use a lot of the low-resource languages, I think, for, like, few-shot training and fine-tuning examples, right?
[2107.46 → 2113.32] And so that is really powerful in terms of bringing out new capabilities.
[2113.74 → 2120.44] And, you know, I think the blog post I wrote was sort of cheekily, like, giving a voice to 5 billion people, right?
[2120.44 → 2125.24] I think especially with speech, you know, text is a slightly different scenario.
[2125.24 → 2133.46] But especially with speech, you actually, like, we always talk at SIL about the sort of long tail of languages, which is sort of got the top 100.
[2133.46 → 2141.70] And then you drop off sort of very quickly in terms of resources that are out there all the way out to 7,000-something languages.
[2142.02 → 2145.94] So you actually don't have to go very far.
[2145.94 → 2154.38] As soon as you get past, like, the first 10 or so top languages in the world with speech data, it drops off, like, very rapidly.
[2155.14 → 2159.68] And so, yeah, it's really cool to see this effort that pushes that out there.
[2159.94 → 2161.40] And that's really encouraging.
[2161.68 → 2165.04] And my brain's already going with ideas of how to use this.
[2165.12 → 2169.14] I think it's also interesting, you know, looking at it how you've...
[2169.14 → 2180.92] I mean, it's one thing to release data, but also it's very useful, at least in my view, to provide additional metadata and annotations along with those words.
[2180.92 → 2193.64] Like, I see you have parts of speech and semantic categorization, which is fascinating and something that I think will be one of those things that drives maybe surprising uses of the data set.
[2193.64 → 2201.30] So, yeah, I'm not sure when that came up in your planning, but I'm glad you went for that extra kind of metadata information.
[2201.96 → 2202.16] Yeah.
[2202.54 → 2209.74] This is part of sort of the curation process and how can you improve things over time and make it more useful.
[2209.90 → 2217.44] And part of it is, you know, we talked to the member organizations along the way as we were doing this to get some feedback on what would be useful.
[2217.44 → 2223.36] And the other thing I should mention is actually the Multilingual Spoken Words Corp is actually a data set generator.
[2223.64 → 2226.68] So you can sort of dial in your own keywords, right?
[2226.74 → 2235.86] And I think because of that capability, it's useful to know, like, what parts of speech are there and what are sort of the content types in the topics and domains.
[2236.48 → 2244.62] So to me, it's part of making it low friction and usable and also just understanding really what's going on.
[2244.62 → 2250.56] And I think that kind of analysis is super important for large scale data sets.
[2250.70 → 2254.24] Like to jump around a little bit and talk about the people's speech.
[2254.48 → 2260.50] One of the things we did is we sort of randomly sampled about 5,000 hours to find out what kind of background noise we had.
[2261.12 → 2263.48] Because, you know, if you're going to train a model, you want to know.
[2264.04 → 2271.02] And, you know, we found lots of music in the background, conversation, basketball bounces, all sorts of things.
[2271.02 → 2275.36] And ultimately, as a data scientist, just getting this is perfect.
[2275.54 → 2279.84] And I should mention for the Multilingual Spoken Words Corpus, it's built on top of Common Voice.
[2280.42 → 2284.62] So what we have is this really cool pipeline that can pull in a data set.
[2285.14 → 2288.62] And what's cool about Common Voice is its ordinary people.
[2288.72 → 2292.92] So anything that goes into Common Voice will eventually get incorporated into ours.
[2292.92 → 2298.38] And there's going to be good background noise and different kind of recording circumstances.
[2298.72 → 2304.06] But I think it really helps to the extent that we can to try to characterize that.
[2304.48 → 2306.64] Kind of in the spirit of if you build it, they will come.
[2307.20 → 2313.44] What kind of member organizations are you kind of pulling in now that you have these new data sets out there?
[2313.44 → 2318.38] And as you're attracting new participants, how are you organizing them?
[2318.50 → 2325.58] And how are you able to put them all together in such a way that it kind of continues the development forward in a cohesive way?
[2325.66 → 2326.78] How do you manage that process?
[2327.26 → 2327.98] Oh, that's a good one.
[2328.08 → 2331.82] Well, so we released these data sets in the middle of December.
[2331.82 → 2333.80] So it hasn't been that much time.
[2333.94 → 2337.44] So I don't know if we've gotten any new members to join yet.
[2337.44 → 2345.36] Yet, but, you know, it's certainly part of my goals for 2022 is getting new members and getting folks who are excited about contributing and using.
[2345.68 → 2348.46] And look, there are a lot of ways that folks can contribute.
[2348.62 → 2351.58] If you're using the data set, and you give us feedback, that's super helpful.
[2351.80 → 2354.42] I mean, obviously, we have to get funding from somewhere.
[2354.60 → 2356.20] And so we do want new members.
[2356.60 → 2362.36] I would say that as an organization, a lot of our folks are very benchmark centric and focused on ML Perth.
[2362.36 → 2372.22] But, you know, I'm looking at as we evolve the organization, how can we allow for participation from folks who are much more data centric?
[2372.36 → 2374.96] And the motivation there is a little bit different, right?
[2375.36 → 2379.06] It may be that it's not, oh, you know, pay us to join this consortium.
[2379.14 → 2381.18] It may be, do you think this is a great effort?
[2381.34 → 2382.60] Like cut us a check, right?
[2382.66 → 2387.04] Or working with, you know, there are a lot of government and other organizations.
[2387.04 → 2391.16] Daniel, you're at one that are very invested in speech diversity.
[2391.16 → 2394.66] And they might, you know, maybe consider doing grants or something like that.
[2394.72 → 2397.44] So this is something we're just starting to explore.
[2397.64 → 2398.70] I mean, yeah.
[2399.18 → 2407.56] Yeah, I'm, my mind is already like thinking of follow-up conversations that I need to have with you, David.
[2407.84 → 2408.58] But that's great.
[2409.64 → 2412.88] Yeah, I hope others and our listeners will be as well.
[2412.88 → 2431.28] So as you kind of move forward this new year, you know, since this is sort of a first recording for the new year, what is in the kind of future roadmap for ML Commons, both in terms of the data sets, but maybe other things to that you're excited about diving into?
[2431.28 → 2439.84] So the first thing is specifically on these data sets, I think of data sets as sort of, we want them to be living data sets, right?
[2439.90 → 2444.34] It's sort of like a garden, you know, you got to prune it, and you got to water it.
[2444.34 → 2454.16] And so on of the things that I think ML Commons is uniquely positioned to do is to be that organization that does sort of maintain it for the community.
[2454.36 → 2460.74] And so we've got engineers who are, their full-time work is to help maintain and improve this.
[2460.88 → 2465.04] So, you know, that's sort of incremental, get better, you know, maybe add a little bit more data.
[2465.04 → 2470.18] But, you know, we are looking at new data sets that, again, we think will push the needle forward.
[2470.40 → 2480.38] There's some vision data set that we're sort of looking at that should have, you know, some really new, nice sort of diverse aspects to it compared to what's currently out there.
[2480.80 → 2483.66] I think that on the data set side is a big thing for us.
[2483.66 → 2488.24] And then we've got some other projects that actually we sort of announced at the same time.
[2488.24 → 2498.92] You know, there's sort of the data-centric AI movement, right, which is sort of at a high level saying like, look, we have a lot of competitions where people are showing off their models, right?
[2498.98 → 2507.10] You know, I saw on Twitter, Jan Begun was talking about sort of, do we want to use transformers or convolution-based networks for vision, right?
[2507.10 → 2514.18] And with convolutions having been sort of the gold standard for a while, but there's a lot of fascinating research focused on using transformers in that area.
[2514.88 → 2516.36] That's very model-centric.
[2516.36 → 2521.90] And one of the things that we want to do is focus on data-centric AI because we think that is really powerful.
[2522.10 → 2525.38] And so we have an initiative called Data Perf.
[2525.64 → 2541.30] And sort of the idea is to say, hey, let's run a competition where instead of showing off the coolest model, you show off things like data augmentations or different splits that can help get better accuracy, faster time to train, things like that.
[2541.30 → 2550.88] And so I'd also love to see folks doing cool things with multilingual spoken words or people's speech and stuff that we've never even thought about.
[2551.16 → 2554.76] So I think that's some of the stuff ahead that really excites me.
[2554.76 → 2567.54] And we may also, you know, I should mention, one of the motivators around people's speech, it's not the size of a data set that someone like Google or Amazon is going to train on, but it's definitely moving in the right direction.
[2567.68 → 2573.00] And so having that for our benchmarking at ML Perf is actually very nicely synergistic.
[2573.00 → 2582.98] So, you know, maybe we'll start building some bigger benchmarks with that, especially because one of the things we wanted to focus on is making these data sets very legally easy to use, right?
[2583.00 → 2584.02] They're all CCB.
[2584.72 → 2588.76] Tell the world we're awesome because we built the data set and do whatever you want, right?
[2589.38 → 2593.20] Well, David, thank you very much for coming back onto the show a second time.
[2593.56 → 2600.46] These are a little bit special for me because I get to sit here not only with you, but with Daniel also and the expertise that he has in language.
[2600.46 → 2604.92] I kind of feel like a kid in a candy shop every time I talk to you on this, and I learn a lot.
[2605.18 → 2615.98] So really, really, really cool work that you guys are doing after talking in the previous episode, mostly about ML Perf and now getting to learn more about data sets and everything.
[2616.24 → 2618.72] So thank you very much for your time and for coming on the show.
[2619.16 → 2620.78] Looking forward to next year's conversation.
[2621.04 → 2621.40] Absolutely.
[2621.58 → 2621.98] Absolutely.
[2622.16 → 2623.08] No, that'd be great.
[2623.60 → 2624.18] All right.
[2624.22 → 2624.88] We'll see you, David.
[2627.88 → 2628.76] All right.
[2628.76 → 2630.82] That's Practical AI for this week.
[2631.10 → 2631.76] Thanks for listening.
[2632.26 → 2640.30] If this is your first time with us, subscribe now at practicalai.fm or simply search for Practical AI in your favourite podcast app.
[2640.46 → 2640.96] We're in there.
[2641.28 → 2645.38] And if you're a longtime listener, do us a solid by recommending the show to a friend.
[2645.86 → 2649.74] Word of mouth is still the number one way people find new podcasts they love.
[2650.12 → 2652.26] Special thanks to our partners for supporting our work.
[2652.58 → 2654.64] Vastly, Launch Darkly, and Linde.
[2654.82 → 2655.60] We appreciate it.
[2655.60 → 2659.80] And to the mysterious Break master Cylinder for cranking out new beats for us all the time.
[2660.16 → 2660.94] That's all for now.
[2661.38 → 2662.54] We'll talk to you again next week.
[2662.54 → 2692.52] We'll see you again next week.
