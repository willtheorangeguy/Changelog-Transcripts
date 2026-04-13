[0.00 --> 10.64]  Welcome back everyone.
[10.84 --> 13.80]  This is The Change Log and I'm your host Adam Stachowiak.
[13.80 --> 19.70]  We're a member-supported blog, podcast, and weekly email covering what's fresh and what's new in open source.
[19.92 --> 26.88]  Check out the blog at thechangelog.com, our past shows at 5x5.tv slash changelog, and subscribe to The Change Log Weekly.
[26.88 --> 30.04]  It's our weekly email covering everything that hits our open source radar.
[30.56 --> 35.20]  You don't want to miss it. It ships on Saturdays. Subscribe at thechangelog.com slash weekly.
[35.64 --> 42.20]  This show is hosted by Andrew Thorpe. It's episode 114 and is sponsored by DigitalOcean and TopTile.
[42.62 --> 46.44]  We'll tell you a bit more about TopTile later in the show, but they're awesome sponsors of ours.
[46.52 --> 54.98]  We absolutely love them, and they connect startups, businesses, and organizations to a growing network of elite engineers all around the world.
[54.98 --> 61.52]  Head to TopTile.com slash developer. That's T-O-P-T-A-L dot com slash developer.
[62.24 --> 67.88]  And DigitalOcean. We love DigitalOcean. We're hosted on DigitalOcean, and we want you to be hosted on DigitalOcean.
[68.48 --> 73.06]  Today, get hosted on a blazing fast DigitalOcean SSD cloud server.
[73.42 --> 78.20]  You can easily create a brand new droplet with root access in 55 seconds.
[78.20 --> 82.68]  Literally, in 55 seconds, you'll be at your prompt setting up your new machine.
[83.06 --> 89.88]  You get your choice of size, region, operating system, all through a simple and easy-to-use dashboard or via the command line if you want to.
[89.90 --> 90.44]  They've got an API.
[91.10 --> 96.44]  And as for our fans who cross the pond, DigitalOcean just announced their brand new second Amsterdam data center.
[96.44 --> 109.98]  AMS2 just opened up on December 2nd and now offers expanded server capacity to Europe, as well as shared private networking, which is only a feature we had here in the States at their NYC2 data center.
[110.36 --> 113.20]  We want you to try DigitalOcean today for free using our promo code.
[113.74 --> 114.54]  Try them out today.
[115.02 --> 117.34]  ChangelogSent is the promo code to use.
[117.58 --> 120.28]  You'll want to use that when you enter your billing code information.
[120.28 --> 123.02]  There's a spot there asking for your promo code.
[123.42 --> 126.86]  Or if you miss it and you sign up, just email support.
[126.96 --> 128.20]  Let them know that ChangelogSent you.
[128.32 --> 132.28]  Use ChangelogSentMe as your promo code and they'll hook you up.
[132.34 --> 133.62]  It's a $10 hosting credit you'll get.
[133.80 --> 136.40]  So we want you to enjoy DigitalOcean.
[136.56 --> 139.54]  Head to DigitalOcean.com today to get started.
[140.02 --> 141.32]  And now, on to the show.
[142.08 --> 145.50]  We're joined today by Slava Akmachet to talk about RethinkDB.
[145.80 --> 146.58]  Welcome to the show, Slava.
[147.22 --> 147.72]  Hi, Andrew.
[148.06 --> 148.82]  It's good to be here.
[148.82 --> 156.64]  Yeah, so RethinkDB is a – I love your catch or your tagline on the website.
[156.86 --> 158.52]  I do this often.
[158.66 --> 159.64]  I say built with love.
[159.96 --> 163.92]  But RethinkDB is an open source distributed database built with love.
[164.82 --> 167.80]  Why don't you give us a little introduction?
[168.00 --> 170.86]  First, who is Slava Akmachet and what is RethinkDB?
[171.76 --> 176.60]  Yeah, well, I was born in Ukraine and I moved to New York City when I was 13.
[176.80 --> 178.40]  I now live in California.
[179.80 --> 181.68]  You know, I did my undergrad in computer science.
[181.80 --> 183.84]  I worked for the financial industry for a while.
[184.60 --> 186.44]  And then I sort of didn't fit in.
[186.52 --> 187.48]  So I went to grad school.
[187.48 --> 198.62]  And, you know, we looked around and we saw that there are a lot of changes in how people access databases and sort of a lot of changes of how things get deployed, how applications get built.
[198.62 --> 201.64]  So we thought it was me and my co-founder, Michael.
[201.64 --> 205.36]  And I'll tell you more about these details, you know, as we get deeper in.
[205.36 --> 215.60]  And we thought we're going to start a project to take some of these ideas and some of these thoughts and sort of implement them into a product, an open source product that people could use.
[215.60 --> 220.86]  So we moved from – I was in grad school at the time doing something totally different.
[221.02 --> 225.40]  We were doing computational neuroscience and supercomputers.
[225.40 --> 235.86]  And it sounds kind of fancy, but really it was just trying to figure out how to simulate big things with a lot of interconnections on IBM BlueJune, which turns out to be really difficult.
[235.86 --> 240.16]  So we were doing that and then started Rethink, moved to California.
[241.44 --> 245.82]  And we've just been working on this project ever since about 2009.
[247.80 --> 248.20]  Gotcha.
[248.38 --> 249.62]  So you guys moved out.
[249.74 --> 251.36]  I think – did you go through the Y Combinator?
[251.48 --> 251.86]  Is that right?
[252.50 --> 253.12]  Yes, we did.
[253.20 --> 256.10]  That was actually the catalyst for moving to California.
[256.28 --> 257.34]  And then we never went back.
[258.28 --> 258.66]  Gotcha.
[259.72 --> 262.40]  Yeah, so it's a relatively new project.
[262.40 --> 269.52]  I mean, NoSQL is – I wouldn't say new, but just the – it started to really gain in popularity in the last couple of years.
[270.48 --> 273.78]  What is it that made you want to do your own thing?
[274.30 --> 276.90]  Were the current solutions not good enough?
[277.02 --> 279.52]  Were there no solutions that you were aware of to solve the problem?
[279.76 --> 284.14]  What really made you kind of rethink the NoSQL for a cheesy pun?
[284.84 --> 291.26]  Well, there really – I think the really major – there were a lot of factors going into it, but there is one thing that I think is a really big deal.
[291.26 --> 301.22]  If you look at traditional databases and even NoSQL databases, there are databases that just happen to have a programmer interface, like an API.
[302.20 --> 304.10]  And we saw this trend.
[304.26 --> 312.06]  Like, if you look at programming languages, people understand that, you know, developers spend many, many hours a day building their programs.
[312.18 --> 314.72]  And these things don't just have to be, like, easy or pragmatic.
[314.88 --> 318.48]  They also have to be pleasant because pleasant programming languages win.
[318.48 --> 326.22]  And so we thought that we're going to start a database that is a developer tool first and a database second.
[327.04 --> 334.52]  And what that really means – I mean, there's a lot of details that go into it, but every time we design a feature or sort of make any kind of a decision,
[334.64 --> 338.98]  we first think of developers and what it feels like to develop in the system.
[338.98 --> 345.52]  And then after that, we think of all the implications in the database – to, like, the database world and the operations world.
[345.86 --> 354.72]  And what comes out of that is what we think and a lot of our users think a really, really pleasant database to develop in because many times people,
[355.24 --> 364.24]  when they build web applications, right, like, back-end is a huge, huge deal, and they spend many hours a day just working through a lot of these things.
[364.24 --> 376.84]  So it's stuff like, you know, a really pleasant administration UI that takes a lot of cues from many of the consumer projects or consumer products.
[377.02 --> 380.98]  Like, why do consumers have to get better UIs than the programmers?
[381.32 --> 385.14]  It's something that didn't sit well with us, so we thought we're going to make that part really good.
[385.88 --> 391.88]  It's things like a query language that's designed to be just a really unique, pleasant, and pragmatic query language.
[392.38 --> 393.28]  We wanted to do that.
[393.28 --> 401.78]  So if you take this core premise that it's a developer tool first and a database second, a lot of very interesting things come out of it,
[402.38 --> 407.74]  and you get something that looks quite different and feels quite different from anything else out there.
[408.64 --> 409.94]  I'm not sure. Does that make sense?
[410.46 --> 410.96]  Yeah, it does.
[411.06 --> 416.30]  I mean, actually, on some of your docs, you kind of say, like, you like to call it the best of both worlds.
[416.30 --> 424.24]  And so you say that there are – like, when I first saw the RethinkDB kind of, like, interfaced, it reminded me a little bit of CouchDB, right?
[424.26 --> 425.18]  The same kind of idea.
[425.18 --> 425.26]  Yeah.
[426.70 --> 432.94]  So you say there's, like, the more developer-oriented products, which would include CouchDB, MongoDB, and things like that.
[432.98 --> 439.90]  And then there's the more, you know, ops-oriented solutions like Cassandra and React, which are a little bit more difficult to get started with.
[439.96 --> 442.68]  And, you know, they are designed for kind of a different purpose.
[442.68 --> 447.36]  Would it be appropriate to say that Rethink is more of, like, a DevOps solution?
[447.64 --> 449.64]  You know, it's like the mixture of the two?
[449.64 --> 452.52]  Yes, we always wanted to do that.
[452.66 --> 468.42]  We wanted – so I think, and actually in a lot of the NoSQL projects, and really databases in general, this tension between developers and operations and how the team behind the project manages that tension is really what pretty much defines the project.
[468.42 --> 485.10]  So, for example, in the case of Cassandra and React to a large extent, you know, this tension between developers and operations and how they make decisions definitely falls closer to the operations side, far closer to the operations side.
[485.16 --> 490.08]  Because in Cassandra's case, it was really important to maintain write availability.
[490.08 --> 493.06]  So they designed, you know, a Dynamo-type system.
[493.26 --> 498.80]  And then if you're writing an application, you have to deal with conflicts and things like that.
[498.82 --> 499.96]  So it's just by design.
[500.20 --> 506.16]  It makes writing applications a little bit more difficult and running a large system a little easier.
[506.72 --> 515.16]  And then MongoDB was kind of the opposite, where they made really pleasant decisions for designing applications.
[515.82 --> 519.16]  You know, it was just JSON in, JSON out, really simple.
[519.16 --> 521.44]  You couldn't do joins, couldn't do many things.
[521.60 --> 525.14]  So it was just that simple system that people really, really loved.
[525.24 --> 532.78]  But then on the operations side, things got tougher because of failover and things like that that weren't as nice as Cassandra or React were.
[533.18 --> 538.74]  So Rethink is just our own take on this tension between developers and apps.
[539.50 --> 544.26]  And we thought that a lot of these systems are very nuanced.
[544.26 --> 554.12]  So if you start looking at the details and looking at the nuances, we thought that we could design a much more balanced, much more pleasant experience.
[554.58 --> 558.82]  But the product is definitely developers first.
[558.82 --> 569.86]  We sort of look at what it's like to develop applications, what it feels like just from, you know, landing on the page to downloading the product to doing the first five minutes and so on.
[570.14 --> 575.98]  And then we, of course, have to make sure that operations, like that it works, that it's good, that it's pleasant for people.
[575.98 --> 586.26]  But whenever there is a decision like a tradeoff and we can't do the best of both worlds, we usually fall closer towards the developers.
[586.56 --> 587.56]  Not always, but usually.
[588.12 --> 588.26]  Yeah.
[588.46 --> 591.74]  So like one of the things that you tout is the query language.
[591.88 --> 597.52]  And I read very popular, or not popular, I read very positive responses to Requel.
[597.52 --> 604.82]  What, I guess, like what was the decision behind Requel?
[605.04 --> 609.14]  Like give me some information about when you guys sat down to talk about your query language.
[609.34 --> 611.42]  You know, what do those talks sound like?
[611.44 --> 613.98]  Because that's pretty low level stuff to talk about.
[614.88 --> 615.06]  Yeah.
[615.22 --> 618.00]  So I'll sort of start with an anecdote.
[618.86 --> 623.72]  I don't know if you remember, there was an operating system a long time ago called BOS.
[624.54 --> 625.54]  Do you remember that at all?
[625.54 --> 628.58]  Well, this was like maybe in the 90s, it was a media operating system.
[629.08 --> 630.88]  Sounds vaguely, vaguely familiar.
[630.88 --> 631.46]  I was very young.
[631.58 --> 631.80]  Okay.
[631.94 --> 632.26]  So.
[632.88 --> 633.14]  Yeah.
[633.96 --> 636.14]  Well, so BOS was this really pleasant.
[636.70 --> 638.92]  It was an operating system, was a really pleasant UI.
[638.92 --> 647.72]  And I think someone asked like the lead developer or an architect of BOS, you know, how did you guys get a UI that is so snappy?
[648.46 --> 650.00]  And the guy said, oh, it's easy.
[650.12 --> 655.18]  The UI guy was sitting in a queue very close to the kernel guy or right next to the kernel guy.
[655.54 --> 659.40]  And, you know, that interaction just resulted in a snappy UI.
[659.88 --> 668.32]  So I think the way what happened was Requel at Rethink is that we, I'm originally, you know, I'm a programming language person.
[668.44 --> 670.34]  I absolutely love programming languages.
[670.34 --> 678.22]  I used to just build interpreters for fun for different languages and learn like every language I could get my hands on.
[678.22 --> 690.42]  And then when we started Rethink and we started building the team around it, part of what I did is this was completely unconscious, but the people that joined also happened to be programming language people.
[690.42 --> 693.26]  Not because I was looking for that or anything.
[693.26 --> 700.38]  It's just because, you know, people just tend to unconsciously sort of attract people and work with people that are similar to them.
[700.74 --> 702.70]  And then my co-founder, Mike, was a UI person.
[702.90 --> 709.96]  So he got, you know, people to join that were really interested in user interfaces.
[709.96 --> 717.28]  So a lot of us are programming language people and we thought, okay, we have to design an interface and it has to be really pleasant.
[717.54 --> 718.76]  It has to be easy to use.
[718.84 --> 720.30]  It has to be familiar to people.
[721.02 --> 733.02]  So just starting with these premises, we built a query language that's sort of like the domain specific language that integrates into whatever language you use.
[733.02 --> 738.64]  So if you're using Python, for example, everything to be query language is just a library for Python.
[738.78 --> 741.02]  Or if you're using Ruby, it's just a library for Ruby.
[741.44 --> 743.34]  So some of these things were pretty easy.
[744.02 --> 751.86]  But once you get into like the esoteric parts of it and how lots of pieces fit in, a lot of the discussions get pretty contentious.
[751.98 --> 753.96]  People have different ideas, different opinions.
[753.96 --> 760.60]  So we've created almost like, I mean, to some degree, it's like the U.S. judicial system, right?
[760.60 --> 761.98]  It's very adversarial.
[762.60 --> 767.26]  And this adversarial process, I think, results in something quite good.
[767.64 --> 768.72]  Sometimes it's stressful.
[769.08 --> 770.14]  There's a lot of tension.
[770.62 --> 773.24]  Sometimes, you know, people don't often agree.
[773.72 --> 778.76]  But I think at the end, it results in a really pleasant experience for people.
[779.58 --> 781.92]  Yeah, I mean, you're ultimately working toward the same goal, right?
[781.96 --> 786.36]  So if you guys have different opinions, you can, you know, be adults and sit down and talk about it.
[786.82 --> 787.86]  Oh, yeah, yeah, absolutely.
[787.86 --> 791.72]  So the way, I mean, the way the process works, it's actually completely open online.
[791.84 --> 795.82]  So if you go to GitHub and search for RethinkDB and look at the issue tracker.
[796.68 --> 799.68]  So when we started, we actually, we couldn't do that online.
[799.80 --> 801.00]  So we sat down in a room.
[801.24 --> 808.28]  And the first version of Requel was just completely banged out, you know, in a room with five people sitting around.
[808.28 --> 818.88]  Right now, because the core of the language already exists and most of the changes are smaller, all of the discussions are happening online and on GitHub.
[819.10 --> 823.92]  So if you look at the issue tracker and look at, like, Requel issues, you'll see exactly what the process looks like.
[823.98 --> 827.68]  And typically, we have a discussion process where anybody could participate.
[827.92 --> 831.88]  You know, it's anyone who's working on Rethink or users or really anybody at all.
[831.88 --> 838.88]  And we have a, we time box it, so it takes about, I believe it's a week to settle on an issue.
[839.18 --> 841.88]  And then if we still can't settle, there is a tiebreaker.
[842.48 --> 848.30]  And it's just the person, you know, we think is, has a really good sense for programming languages.
[848.30 --> 849.86]  So we try to arrive at a consensus.
[849.86 --> 852.20]  And if we can't, that person breaks ties.
[852.20 --> 855.50]  And that's how the process works right now.
[857.62 --> 858.02]  Gotcha.
[858.20 --> 859.72]  So, yeah, it's an open.
[859.82 --> 868.64]  We've had guests on the show, I think, that we've had, like, Chad Whitaker from GitHub that would love to hear that the community and everyone kind of plays a part in the decisions that are made.
[868.70 --> 869.98]  That's a pretty cool thing.
[871.52 --> 872.50]  How often do you have to...
[872.50 --> 873.46]  Go ahead.
[874.46 --> 879.08]  So, actually, the community playing a part in design discussions has been a huge deal for us.
[879.08 --> 884.10]  I think it's incredibly important because what often happens, and actually, it's not just Rethink.
[884.20 --> 885.82]  I think it's open source in general.
[886.20 --> 892.02]  But what used to happen with, you know, commercial projects is people would release a feature and then they'd get the feedback afterwards.
[892.20 --> 893.70]  And you could do all sorts of stuff before.
[893.86 --> 898.08]  Like, you could do, you know, studies and you can do betas and demos and things like that.
[898.08 --> 907.58]  But it's just not the same as having users, you know, jump in on a GitHub issue during the technical discussion and comment on what you're doing.
[907.58 --> 918.44]  And so far, I mean, I wouldn't say every single recall design decision benefited from this, but, like, the majority probably did.
[918.44 --> 918.58]  Yeah.
[920.86 --> 931.74]  How often do you have to, you know, I feel like a year, two years ago, maybe a little longer than that, the question that I always read was, you know, NoSQL versus SQL, right?
[931.82 --> 932.94]  What's the right solution?
[933.04 --> 939.26]  Should I use, like, a Mongo or should I use, like, a Postgres or, you know, what's the solution for my application?
[939.26 --> 946.30]  How often now – it seems like that question has shifted now to people kind of know what they want to use for their solution.
[946.44 --> 951.56]  And now it's, like, it's gone back to if you're going to use SQL, like, is it MySQL or is it Postgres?
[951.64 --> 954.98]  If you're going to use NoSQL, is it, you know, which one?
[955.02 --> 962.52]  So how often do you have to answer or kind of defend the decision to whether to go with, you know, Postgres or Rethink kind of a thing?
[962.52 --> 975.02]  Well, I think we're – so Rethink is a young product and a young project, and a lot of people that start using Rethink already have a very good idea of what's going on.
[975.10 --> 981.02]  So we very rarely have to talk about Rethink versus Postgres or Mongo versus Postgres or anything like that.
[981.08 --> 984.92]  I think most people pretty much know who use RethinkDB.
[984.92 --> 1000.48]  But if you zoom out a little bit and look at, like, programmers in the world in general, I think there is still a lot of education to do and a lot of work to do for people to understand the differences between these two approaches and what fits when.
[1000.88 --> 1007.82]  Because people have – I mean, we've studied, you know, relational systems and taught relational systems to people for the past 40 years.
[1007.82 --> 1013.78]  And I don't think a change like that, a very fundamental change like that can happen within a couple of years.
[1013.88 --> 1019.14]  I think it's going to take a while for, like, the programming world at large to really understand the difference.
[1019.68 --> 1027.00]  And I actually think, you know, young people building these things, like, we're learning every day how RethinkDB is and isn't useful to people.
[1027.00 --> 1042.08]  So even for the vendors and the people that are building these projects, it takes a while to understand, like, what their project actually means and what it does for people and when it's a good idea and when it's not such a good idea.
[1042.72 --> 1042.92]  Yeah.
[1043.16 --> 1051.16]  I mean, I think I, like – I would say most people, and myself included, tend to still just think relationally in terms of, you know, our system design.
[1051.16 --> 1065.92]  And so I would wonder and I'd probably imagine that a lot of people who are just doing – like, going to Rethink or going to Mongo are just kind of doing it at this point because it's, like, the new thing to do and still trying to slam relational models into it and use it that way.
[1066.58 --> 1069.50]  And so I wonder at what point will we – you know, you said it.
[1069.66 --> 1074.38]  Like you said, I mean, just object-oriented in general kind of lends itself to relational ideas.
[1074.38 --> 1084.82]  So, you know, at what point – how many years will it take before we, like, are able to actually kind of free our minds of that and think in different ways that really enable this, you know, this mindset?
[1086.00 --> 1088.12]  Well, so we sometimes talk about this.
[1088.70 --> 1092.68]  So when you – when people first built cars, right, they used to not be called cars.
[1092.76 --> 1094.40]  They used to be called horseless carriages.
[1095.38 --> 1103.74]  And NoSQL kind of reminds me of that because when you define a whole field by an absence of something, that means the field is pretty young, right?
[1103.74 --> 1106.00]  It's going to take a while for it to really settle.
[1106.56 --> 1117.08]  I think if you jump a little bit into the details, when people first start using Rethink in particular, they maybe start with preconceptions of relational design.
[1117.08 --> 1125.70]  But then they very quickly learn not to necessarily do that because the project just sort of guides them towards the thing that makes sense.
[1126.68 --> 1130.24]  You know, these things are often not about what's possible because you could build anything and anything.
[1130.24 --> 1134.48]  It's more about what's easy and what is, like, the path of least resistance.
[1134.60 --> 1140.02]  So people learn pretty quickly on an individual basis the moment they start using Rethink.
[1140.08 --> 1142.70]  And I'm sure that's true about other NoSQL projects too.
[1143.46 --> 1150.26]  But the world at large, I think it will probably take, you know, another five to ten years for this to really become old news.
[1151.12 --> 1154.56]  And everyone just understands what everything is and what it means.
[1154.56 --> 1158.66]  So let me ask you then just kind of for an answer.
[1158.78 --> 1160.72]  What makes NoSQL a good choice?
[1160.82 --> 1164.82]  And then more specific, what makes Rethink a good choice once you've gotten to that point?
[1165.12 --> 1168.84]  So I think NoSQL as a field is still definitely young.
[1169.52 --> 1172.28]  But what makes NoSQL a good choice is two things.
[1172.36 --> 1182.30]  The first is that a lot of data that people work with now, it's not relational in nature, at least not as relational as it used to be.
[1182.30 --> 1184.14]  It's much more hierarchical.
[1185.30 --> 1192.04]  And, you know, pragmatically what it means is if you just do a relational design, you're going to have a lot of missing columns.
[1192.84 --> 1196.98]  You just have, you know, a thousand columns and in most rows, most of them are null.
[1197.34 --> 1199.98]  And it's very unpleasant to work that way.
[1200.52 --> 1202.22]  And NoSQL makes that very pleasant.
[1202.40 --> 1204.04]  You don't have to worry about that very much.
[1204.42 --> 1209.84]  That's the first thing that makes NoSQL easier for that kind of problem.
[1209.94 --> 1211.26]  The second thing is scale-out.
[1211.26 --> 1214.34]  So there was a big promise of that.
[1214.94 --> 1221.28]  And it's still, I think, quite debatable whether NoSQL makes things easier to scale out in practice today.
[1221.84 --> 1225.72]  But I think when the field matures, it's definitely going to be the case.
[1226.12 --> 1230.50]  Because the thing is fundamentally more scalable than relational systems just because it does less.
[1230.98 --> 1238.78]  And when these systems mature, I think scale-out is going to be a no-brainer in NoSQL, but it's still going to be hard in SQL.
[1238.78 --> 1240.56]  So that's the field in general.
[1240.76 --> 1248.40]  As far as rethink, we make it really, really, really easy to build applications that have to deal with JSON.
[1248.40 --> 1258.72]  Specifically, if you want to do things other than sets and gets and basic aggregations in a single table, the moment you start doing cross-table stuff or cross-collection stuff,
[1259.54 --> 1261.06]  Rethink just makes that really easy.
[1261.16 --> 1262.82]  The programming language is really easy.
[1262.82 --> 1271.32]  And then you build your app, and then we make deploying and scaling out just a very pleasant and easy experience.
[1271.82 --> 1278.88]  And you could go to rethinkdb.com and watch the video, and we sort of show like a one-minute video of how easy it is to scale things out.
[1278.92 --> 1280.02]  It's just a press of a button.
[1280.02 --> 1284.70]  So we make building applications and then scaling them out really simple.
[1285.04 --> 1290.34]  Now, I would point out that Rethink is still in beta, and we said it on the front page.
[1291.14 --> 1300.16]  We're getting very close to making it be a production release that people can start using in real production products, and a lot of people have already.
[1300.16 --> 1306.20]  But we've been very careful about making promises to people because these systems are hard.
[1306.30 --> 1307.68]  They take a long time to design.
[1308.06 --> 1311.50]  They take a long time to iron out the bugs so they work well.
[1312.20 --> 1317.90]  So Rethink is new, and we certainly encourage everyone to try it and play with it and start building applications.
[1319.70 --> 1325.76]  But it's always a disclaimer that I kind of use before we start offering commercial versions of the product.
[1325.76 --> 1327.82]  Yeah.
[1328.26 --> 1336.18]  Being in beta, I mean, so just to kind of be transparent, you guys are – so there's a 13-minute video I watch, right?
[1336.32 --> 1340.02]  The first thing I did with Rethink, I was like, let me watch this video.
[1340.20 --> 1344.44]  13-minute video, and you guys kind of explained Rethink, what it is.
[1344.88 --> 1350.24]  You showed me sharding replication failover, all in 13 minutes.
[1350.24 --> 1356.24]  And I just think back to a couple years ago, like somebody trying to explain sharding to me.
[1356.74 --> 1361.86]  And a couple years ago, somebody trying to explain what their replication strategy is to me.
[1362.02 --> 1365.56]  And it's just shocking to me that you guys can do all that in a 13-minute video.
[1366.08 --> 1374.52]  Well, so it's 13 minutes to demo the product, but it's about three years to make all of that possible, right?
[1375.92 --> 1376.36]  Exactly.
[1376.36 --> 1381.08]  Yeah, it's really cool.
[1381.16 --> 1381.94]  So let me ask you this.
[1382.04 --> 1388.22]  What is your – you guys officially support, I guess, three languages, the best way to put it, right?
[1388.26 --> 1389.32]  Python, Ruby, and JavaScript.
[1390.36 --> 1394.60]  What is your favorite – like, what's your favorite implementation and why?
[1394.98 --> 1398.58]  So I am personally a Python fan.
[1399.02 --> 1400.86]  But I think – and I love Python.
[1401.08 --> 1402.48]  I love the programming language.
[1402.48 --> 1406.04]  And I love the Python driver, RethinkDB driver.
[1406.18 --> 1406.84]  I use it a lot.
[1406.94 --> 1411.20]  I also use JavaScript a lot, both because I like the language and I like the driver.
[1411.76 --> 1413.70]  I'm not a fan of Ruby myself.
[1413.86 --> 1421.28]  But if I had to be honest with myself and with everyone listening, I'd say that the Ruby driver for RethinkDB is probably best.
[1421.28 --> 1436.58]  Just because Ruby, with their blocks and in general how the language is designed and how easy it is to hack in and do anything you want, is the most pliable if you want to build a domain-specific language.
[1437.14 --> 1437.18]  Right?
[1437.18 --> 1441.04]  So Python – you know, the Python driver for Rethink and the JavaScript drivers are great.
[1441.44 --> 1444.18]  But Ruby, the language, makes some things easier.
[1446.30 --> 1448.78]  Specifically, I think blocks are the most important.
[1449.32 --> 1452.80]  And it's a little bit difficult to describe without, you know, just actually typing.
[1452.94 --> 1454.32]  So I can't do that verbally.
[1454.32 --> 1462.78]  But if you look at RethinkDB.com and see just a basic example of what it looks like in Ruby and Python and JavaScript, Ruby just is a little bit nicer.
[1464.24 --> 1464.68]  Yeah.
[1464.84 --> 1467.74]  Well, I mean, it's just the idea of chaining in general.
[1468.00 --> 1474.62]  Like JavaScript chaining is great, but there's some parts of it that anyone who's worked in JavaScript has – you kind of – it feels weird sometimes.
[1474.98 --> 1478.26]  And Ruby lends itself to that, I think, just in a real elegant way.
[1478.40 --> 1481.28]  Just, yeah, it's a great language for DSLs and stuff like that.
[1481.28 --> 1482.28]  So –
[1482.28 --> 1485.48]  Yeah, well, the fact that – oh, sorry.
[1485.50 --> 1485.78]  Go ahead.
[1486.24 --> 1486.68]  No, you got it.
[1487.14 --> 1491.52]  I was just going to say the fact that blocks have a really nice syntax make it easier.
[1491.62 --> 1494.96]  Because in JavaScript, you have to type, like, the word function, right?
[1495.00 --> 1496.36]  And that's a lot of typing to do.
[1496.80 --> 1499.88]  Whereas in Ruby, you just put brackets, and that makes things a lot easier.
[1501.02 --> 1502.12]  Yeah, definitely.
[1502.42 --> 1505.34]  Let's go ahead and pause for a minute, give a shout-out to our sponsor, TopTal.
[1505.98 --> 1510.02]  Yes, let's give a shout-out to our awesome sponsor, TopTal.
[1510.02 --> 1510.10]  Wow.
[1510.30 --> 1513.66]  They've been sponsoring the show for a bit now, and they're going to sponsor, I think, one more month.
[1513.86 --> 1516.58]  But I've been working with their CTO, Brendan.
[1517.10 --> 1521.90]  And I mentioned before I wasn't quite sure what to expect from them when we first started working out with them.
[1521.92 --> 1523.32]  But I got to say, these guys are the real deal.
[1523.44 --> 1525.70]  They're engineers themselves from top to bottom.
[1525.86 --> 1528.38]  They built the company around engineers.
[1528.96 --> 1532.28]  They're not non-technical recruiters trying to pimp developers.
[1532.28 --> 1537.84]  They're a network of engineers from all around the world who work with some really awesome clients.
[1538.04 --> 1547.56]  And for those of you out there who are freelancing, or maybe you'd like to freelance, or maybe you're in a full-time position, kind of doing one thing by day, and you like to do another thing by night.
[1547.62 --> 1553.34]  Let's say Node or something in JavaScript or Ruby, just as an example.
[1553.34 --> 1556.64]  And you like to try kind of testing out freelancing.
[1556.82 --> 1564.26]  You've got to check out TopTal because they're doing some really awesome stuff with companies like Airbnb, Artsy, IDEO, and many others.
[1564.66 --> 1568.00]  You can work remotely, on a beach, or anywhere in the world.
[1568.08 --> 1568.96]  No office required.
[1568.96 --> 1573.44]  To get started, head to toptal.com slash developer and click join the best.
[1573.86 --> 1588.60]  Because they want to work with only the best senior engineers out there, they've got a well-thought-out four-stage screening process that begins with a personal call via Skype to kind of get to know who you are and what you're up to and introduce you to TopTal and what their mission is and see if you're a fit.
[1588.60 --> 1600.12]  And from end to end, the process includes an English-speaking test, a timed algorithm test, technical interviews with core TopTal engineers, and a test project.
[1600.50 --> 1604.42]  But once you've got through that screening process, the sky is the limit.
[1604.82 --> 1608.76]  And if you think you have what it takes, head to toptal.com slash developer to get started.
[1609.20 --> 1613.38]  Tell them the changelog sent you, toptal.com slash developer.
[1613.38 --> 1621.90]  All right, so we were talking about which languages and Ruby versus Python, and we don't want to get too much into that right now.
[1622.00 --> 1629.82]  But what I do want to kind of get into is just a little bit more specific, deep dive into Rethink itself and less of the theory behind it.
[1630.16 --> 1632.88]  And let's talk a little bit about how it works.
[1632.98 --> 1638.44]  So what do you guys recommend for the kind of the best way for somebody to get started working with Rethink?
[1638.44 --> 1643.20]  So we wanted the way we created getting started.
[1643.34 --> 1644.46]  It's almost like a game, right?
[1644.54 --> 1646.62]  So it's got to be really easy when you start out.
[1647.02 --> 1653.42]  And then as you start doing more advanced things, it should keep being easy and the learning curve shouldn't jump too much.
[1654.32 --> 1655.96]  So getting started is really easy.
[1656.04 --> 1657.24]  Go to RethinkDB.com.
[1657.30 --> 1660.06]  You can download it on Linux or OSX.
[1660.06 --> 1668.56]  And then there is a tutorial for any pretty much, you know, Ruby, Python, JavaScript, but you could really use this with any programming language.
[1669.16 --> 1670.60]  The tutorial is just 10 seconds.
[1670.74 --> 1677.90]  And then if you like that, you can move on to a 10-minute tutorial and start inserting documents and querying and doing more advanced things.
[1679.80 --> 1680.20]  Gotcha.
[1680.30 --> 1681.74]  So let's talk a little bit about the querying.
[1681.84 --> 1684.32]  I think it's a neat way, the way that you guys do the chaining.
[1684.32 --> 1689.50]  And so every, basically, every, let's specifically talk in JavaScript.
[1689.78 --> 1697.70]  Every, I don't know, operation is essentially a chain of, you know, different, this is what we're talking about with Requel, the query language, right?
[1697.94 --> 1702.20]  So you would basically say, you know, R.database.
[1702.30 --> 1705.56]  And I guess that's probably optional if you're only dealing with one database.
[1705.70 --> 1706.12]  I'm not sure.
[1706.40 --> 1708.70]  But, you know, you would say R.database.
[1708.74 --> 1711.92]  And then you'd pass the name of your database into that function.
[1711.92 --> 1714.94]  And then you would say .table, pass the name of the table into that function.
[1715.06 --> 1717.44]  And then you would start talking about your operations and what you want to do.
[1717.50 --> 1719.18]  And then you end it with a run.
[1720.12 --> 1720.28]  Yes.
[1720.76 --> 1724.40]  So the query language is designed in a way where you start.
[1724.64 --> 1726.90]  So the data sort of flows left or right.
[1727.30 --> 1730.70]  So on the very left of your query, you specify where the data comes from.
[1730.80 --> 1731.88]  Usually it's a table, right?
[1731.92 --> 1733.54]  So you say table, you know, users.
[1733.88 --> 1735.62]  And then after that, you say ..
[1736.10 --> 1737.48]  And you can put any command you want.
[1737.56 --> 1740.68]  So, for example, you want to filter users in a specific city.
[1740.68 --> 1744.40]  So you say .filter and then, you know, the city that you want.
[1744.60 --> 1745.82]  And then you can say .again.
[1746.56 --> 1748.24]  And let's say you want to group things.
[1748.32 --> 1750.64]  So you say, you know, group by, da-da-da-da-da.
[1750.72 --> 1751.84]  And then you can say .again.
[1751.94 --> 1753.34]  And you can just do this indefinitely.
[1753.34 --> 1760.98]  So it's very similar to how you do chaining in jQuery, if people are familiar with that.
[1761.06 --> 1767.26]  It's also very similar with how you do it on the Unix command line in Bash, right, where data just flows left to right.
[1767.32 --> 1768.88]  And you can keep adding pipes.
[1769.40 --> 1772.74]  And each pipe is just an operation on that data.
[1772.74 --> 1781.16]  So then once you actually execute it, you just – once it hits run, it actually executes everything from before, right?
[1781.74 --> 1782.16]  Yeah.
[1782.24 --> 1788.38]  So the important subtlety here is as you write that query in JavaScript, all of that is on the client.
[1788.68 --> 1790.02]  It's all written in JavaScript.
[1790.82 --> 1794.04]  And you say, you know, table, filter, group by.
[1794.14 --> 1795.12]  You can count things.
[1795.20 --> 1796.50]  You could do whatever you want.
[1796.78 --> 1798.46]  You know, you could do joins across tables.
[1798.46 --> 1801.14]  But all of that is still just a program in JavaScript.
[1801.40 --> 1814.38]  And then when you type .run and you give it the connection to the database, what happens is the client takes that query, packages it into a binary format, into protocol buffers, actually, Google protocol buffers.
[1814.72 --> 1817.80]  And that gets shipped over to the database server.
[1818.62 --> 1826.56]  And then RethinkDB clusters, basically, the machine on the other side, the server machine, takes that query, compiles it down to a distributed program,
[1826.56 --> 1829.52]  and sends it out to all the nodes in the cluster.
[1830.08 --> 1833.14]  It knows where everything is, so you can send the query to any machine.
[1833.72 --> 1837.08]  And it gets the data, and then as a user, you just get the result, right?
[1837.12 --> 1839.06]  So none of this gets executed in the client.
[1839.48 --> 1843.20]  The client side is just a convenient way to write the query.
[1843.32 --> 1845.72]  The whole thing runs on the server in the cluster.
[1845.72 --> 1847.96]  One little thing I wanted to point out.
[1848.02 --> 1855.82]  I was looking at your FAQs, and at the top of the site, I see a little example on inserting into students.
[1856.00 --> 1859.64]  And it looks like you guys are kind of taking a shot at SQL with the SQL injection.
[1860.62 --> 1862.32]  Bobby drop tables.
[1862.72 --> 1863.74]  Yeah, Bobby drop tables.
[1863.80 --> 1864.22]  That's funny.
[1864.22 --> 1873.30]  But that does kind of give me a – I mean, is that just because – do you guys deal with just only this SQL in this format,
[1873.40 --> 1876.82]  or can you actually write actual – not SQL, but something similar?
[1877.54 --> 1879.82]  So right now, we only deal with this format.
[1880.16 --> 1885.12]  But if you look at – if you actually dive into the details of how the protocol is designed,
[1885.20 --> 1889.92]  there is no reason this has to be a DSL in Python, Ruby, JavaScript, or any other language.
[1890.00 --> 1891.22]  This could be a text language.
[1891.58 --> 1893.30]  We just haven't designed one yet.
[1893.30 --> 1898.44]  I think this is going to be important for people like business analysts who later, you know,
[1898.48 --> 1900.88]  they have a running database, and they want to analyze the data.
[1901.52 --> 1904.44]  And I don't think – well, I'm not sure, but, you know,
[1904.48 --> 1910.90]  I think it's nicer for people to be able to do it in a language closer to English rather than Python.
[1911.48 --> 1913.22]  So we're thinking about this a little bit.
[1913.30 --> 1915.08]  But, yes, there is no language like that now, right?
[1915.12 --> 1916.22]  Now it's just a DSL.
[1916.62 --> 1921.26]  And as you pointed out, an interesting property of that is you can't really get injection attacks
[1921.26 --> 1923.26]  in the way you can with SQL.
[1924.80 --> 1928.60]  So do you think that you'll ever – do you think it would be SQL that you would support,
[1928.68 --> 1932.60]  or would you write your own mapping, or how would you – what kind of decisions would you make?
[1932.60 --> 1936.30]  I don't think it would ever be SQL for a couple of reasons.
[1936.44 --> 1939.70]  I think SQL isn't very good for hierarchical data.
[1939.70 --> 1945.98]  And people have tried extensions to it, in particular, like Postgres has extensions to SQL to work with JSON.
[1946.54 --> 1947.96]  And, you know, it's okay.
[1948.22 --> 1953.12]  It's not nearly as nice as a language designed from scratch to work with hierarchical data.
[1953.40 --> 1954.76]  So I don't think it will ever be SQL.
[1954.88 --> 1959.96]  I just think it's going to be designed – if we ever do this, it's going to be more for non-programmers,
[1960.02 --> 1960.82]  if that makes sense.
[1961.54 --> 1966.04]  SQL sort of has this interesting property where it was designed for non-programmers, right?
[1966.04 --> 1969.78]  And then programmers were kind of forced to use it, but it was really designed for business people.
[1970.36 --> 1974.86]  So we designed the first version of the language as DSLs for programmers.
[1974.86 --> 1980.66]  And then if we ever do a SQL-like language for business people, it's not going to necessarily look like SQL.
[1981.04 --> 1983.08]  It's just going to be closer to a natural language.
[1983.26 --> 1988.88]  So you don't have to put, like, quotes and dots and things like that, which non-programmers probably don't understand.
[1989.56 --> 1990.00]  Right.
[1990.00 --> 1990.04]  Right.
[1990.38 --> 1996.86]  So one thing that's interesting that kind of – I don't know, just to me personally it jumped out was watching the tutorials on Rethink,
[1997.02 --> 2000.04]  the join part of the language.
[2000.36 --> 2006.68]  And I think that being a non-relational, I think that you don't see that a lot with NoSQL because they want to –
[2006.68 --> 2013.66]  I mean the word join kind of implies that these two different databases are – I'm sorry, two different tables are related in some way.
[2013.66 --> 2017.56]  And so that's some sort of relationship.
[2017.98 --> 2026.94]  But the truth is, like, even when it's hierarchical data, they oftentimes do have things that are relatable or you want to –
[2026.94 --> 2031.64]  maybe they're not necessarily related to each other, but you want to compare with each other, things like that.
[2031.72 --> 2035.02]  So what was the decision behind supporting a join like that?
[2035.10 --> 2040.94]  And why do you think other NoSQL solutions – and I don't know which ones do and don't support that, but what do you think goes behind that?
[2040.94 --> 2048.52]  Well, it's actually really interesting because when people talk about relational databases, the – I mean, when this thing was designed in, like, the 70s and 80s,
[2048.56 --> 2055.78]  the word relational really came from mathematical relations, which has almost nothing to do with relationships,
[2056.02 --> 2058.94]  but because the word sounds so similar, it has the same root.
[2059.34 --> 2063.10]  People talk about relational databases in terms of relationships between data.
[2063.30 --> 2065.12]  And this was completely unintended, right?
[2065.16 --> 2068.24]  This was not, you know, the original intention at all.
[2068.24 --> 2073.18]  And with NoSQL, you just can't escape the fact that data has relationships.
[2073.90 --> 2082.22]  I mean, every hierarchical data, graph data, any data, it's all about encoding relationships, whether it's SQL databases or NoSQL databases.
[2082.92 --> 2093.64]  And to us, a join operation was really a no-brainer because if you look at what people do with a database like MongoDB, for example,
[2093.64 --> 2101.18]  that doesn't have a join operation, what they'll do is they'll have a table where they'll often get the data out into the client
[2101.18 --> 2105.06]  and then loop through every record and then go to the database again.
[2105.58 --> 2109.74]  And you can, of course, you can get around that by storing documents in line,
[2110.46 --> 2114.94]  but you can only do that to a point because that's not necessarily very scalable.
[2114.94 --> 2123.26]  And we thought that, hey, Rethink has to support both because it's just a matter of time until every NoSQL database supports a join operation.
[2124.06 --> 2130.80]  It was sort of a no-brainer to us, so we just went ahead and did it because we designed the architecture on day one
[2130.80 --> 2134.80]  to support commands that work across tables.
[2134.80 --> 2140.44]  And you could do this, so pretty much anything you could do in SQL, you could do in Rethink,
[2140.54 --> 2142.40]  so you could do subqueries and things like that.
[2142.50 --> 2147.64]  If you're running a map reduce command or something, you can put a join inside there,
[2147.74 --> 2153.70]  you could do subqueries inside there, and it never made sense to us that a query should just be on a single table.
[2154.24 --> 2158.44]  We always thought it should be able to support dealing with relationships.
[2158.44 --> 2161.30]  Yeah. That's kind of a big decision, though, right?
[2161.38 --> 2163.58]  I mean, do you guys have to kind of answer for that a lot?
[2163.84 --> 2167.42]  It seems like that would be a pretty big selling point of Rethink.
[2168.14 --> 2169.40]  Yes, it's a big selling point.
[2169.96 --> 2174.58]  So the downside to this, of course, is that a system like this is much, much harder to develop
[2174.58 --> 2180.20]  because there's a lot that goes on in the back end to make this work,
[2180.44 --> 2184.50]  and it almost makes the complexity exponential, right?
[2184.52 --> 2187.56]  It's just so much harder to develop a system like this.
[2187.56 --> 2189.88]  It's so much harder to design an architecture,
[2190.18 --> 2193.68]  and then every feature you have to think about how it fits in.
[2194.08 --> 2197.00]  So we have to pay for that in just development time.
[2198.16 --> 2200.76]  Every time we do something, we have to make sure everything fits.
[2200.90 --> 2205.84]  But now that we understand that really well, it became a lot easier.
[2205.94 --> 2209.64]  I think early on, we just had to pay a lot in development time.
[2209.74 --> 2214.16]  But we think about this in terms of just what's better for users,
[2214.16 --> 2215.96]  and we thought it's totally worth it.
[2215.96 --> 2216.70]  Mm-hmm.
[2217.24 --> 2221.78]  So talking about what's better for users, can you kind of give me a practical application
[2221.78 --> 2224.90]  of Rethink, the real-world scenario where it would make sense?
[2225.60 --> 2229.48]  Oh, we originally designed it for web applications and mobile applications,
[2229.62 --> 2232.62]  but we just find people use it in a lot of different places.
[2232.80 --> 2236.90]  Like people use it in municipalities to record police events.
[2237.06 --> 2240.42]  People use it in biotech to store gene sequence data.
[2240.42 --> 2242.40]  It just shows up all over the place.
[2243.30 --> 2248.26]  But I think, and, you know, it was very exciting and sort of makes me personally very happy
[2248.26 --> 2253.30]  to see that a lot of people like, just like what we've built and find it useful.
[2253.76 --> 2258.20]  But I still think that every time you're dealing with, so Rethink is really useful
[2258.20 --> 2259.58]  every time you're dealing with JSON.
[2259.58 --> 2265.68]  So, you know, stuff like log data, any kind of middleware where you're dealing with different
[2265.68 --> 2271.00]  APIs, any time you're doing things like product catalogs where you can't, you know, you have
[2271.00 --> 2273.20]  different products and they all have different structure.
[2273.50 --> 2278.38]  Just really any time you're dealing with JSON or hierarchical data, Rethink is really useful.
[2278.48 --> 2282.44]  And I still think most of the time that's building things for the web.
[2283.30 --> 2283.86]  Gotcha.
[2283.86 --> 2288.04]  Do you have any plans of releasing a Windows support for Rethink?
[2289.12 --> 2290.04]  I'd love to do this.
[2290.12 --> 2291.26]  I actually grew up in Windows.
[2291.62 --> 2297.10]  I think one of my first, like, development environments was Visual Studio.
[2297.78 --> 2299.82]  So I'm still in love with that platform.
[2299.94 --> 2302.36]  I think it's just a matter of time until we do it.
[2302.42 --> 2307.98]  We don't have plans for this right now because we don't want to increase the surface area of
[2307.98 --> 2308.82]  the project, right?
[2308.88 --> 2312.28]  Because the moment we port the Windows, we have to support it and everything gets a little
[2312.28 --> 2312.74]  bit harder.
[2312.74 --> 2314.38]  So sooner or later, we're going to do it.
[2314.44 --> 2316.38]  I don't have an ETA for this right now.
[2316.96 --> 2317.02]  Gotcha.
[2317.14 --> 2318.98]  So you talk about having to support it.
[2319.12 --> 2321.20]  And you mentioned earlier that you guys are still in beta.
[2322.80 --> 2326.72]  Although you're in beta, do you see people using this in production like anyone, you know,
[2326.76 --> 2330.92]  any companies that are, you know, big companies or anything using this in production?
[2331.50 --> 2331.88]  Yeah.
[2331.92 --> 2336.90]  So one thing we quickly learned is people don't listen when you say it's in beta, right?
[2337.02 --> 2340.78]  Like, Gmail was in beta for a very long time, you know, up to a point where, like, the
[2340.78 --> 2341.68]  whole world was using.
[2341.68 --> 2343.32]  So the same is true as we think.
[2343.44 --> 2345.62]  I can't speak to specific companies right now.
[2345.74 --> 2349.62]  We're definitely going to, you know, post it on the site and talk about it and do case
[2349.62 --> 2352.50]  studies and sort of showcase a lot of interesting use cases.
[2352.98 --> 2358.44]  But yeah, people definitely have been, you know, starting to build production software on
[2358.44 --> 2363.62]  Rethink like from day one, which really surprised us because, you know, we expected people would
[2363.62 --> 2364.68]  be a little bit more careful.
[2364.68 --> 2365.64]  All right.
[2366.24 --> 2373.50]  So like with traditional solutions, you have, you know, I mean, sharding and replication.
[2373.82 --> 2375.64]  Those aren't, I mean, those are common things, right?
[2375.68 --> 2378.70]  And pretty much every database solution has to handle that in some way.
[2378.70 --> 2381.90]  It's so easy with Rethink though.
[2382.10 --> 2386.22]  But so part of that is, and I think a lot of, you know, developers and ops people, and
[2386.22 --> 2389.30]  I think they like to kind of have fine control and fine tune.
[2389.42 --> 2393.14]  But when I'm watching this video and I see, I don't know who it was that was doing the
[2393.14 --> 2393.34]  video.
[2393.42 --> 2398.50]  But when I see him, you know, shard the one of the servers and replication was so easy.
[2398.50 --> 2400.82]  But is there fine tuning?
[2401.10 --> 2406.50]  Like, can somebody get in there and really tune like, you know, I don't know, like to
[2406.50 --> 2408.98]  speed up queries or can they do stuff like that in Rethink?
[2409.50 --> 2410.02]  Oh, yeah.
[2410.08 --> 2415.04]  So there's a command line interface that allows you to really deep down, dive deep down into
[2415.04 --> 2418.76]  the details and take complete control over the system.
[2419.14 --> 2422.84]  We designed it with the idea that, well, there are a couple of ideas there.
[2422.92 --> 2427.46]  The first is we learned that when you automate too much, it works and it works, let's say,
[2427.46 --> 2431.56]  95% of the time, but 5% of the time it breaks down.
[2431.94 --> 2434.36]  Well, that's great, but it's not very useful to people, right?
[2434.38 --> 2437.06]  Because they don't know what to do when there is an actual error.
[2437.50 --> 2442.28]  So we didn't want to automate too much and we wanted to build it in a way where administrators
[2442.28 --> 2445.46]  could do, you know, could be very explicit about what they want.
[2445.56 --> 2448.20]  And we built that first and that's available in the command line.
[2448.58 --> 2452.18]  And then after that, we thought, you know, to get started with the system, that's got to
[2452.18 --> 2452.90]  be really easy.
[2452.90 --> 2457.44]  So we built tools on top of that that use the lower level tools to automate.
[2457.46 --> 2459.30]  And that's what you see in the web UI.
[2460.98 --> 2462.88]  And it turned out to work really well.
[2463.20 --> 2469.56]  So, you know, 95% of the time, people just do not have to look at the deeper thing because
[2469.56 --> 2471.88]  the high level interface will work.
[2472.36 --> 2473.98]  But if you want to, you totally can.
[2474.42 --> 2478.38]  You just type everything to be admin on the command line, point it at the cluster, and you
[2478.38 --> 2480.76]  can administer and change pretty much anything you want.
[2480.76 --> 2481.32]  Awesome.
[2483.74 --> 2483.96]  Yeah.
[2483.98 --> 2486.16]  So you guys have a page, SQL to Requel.
[2486.54 --> 2493.34]  And I think it's neat to see how these projects are vastly different and, you know, just in
[2493.34 --> 2497.72]  general, but how easy it is to kind of map terminology and stuff like that.
[2497.80 --> 2498.80]  It's pretty cool to see.
[2498.88 --> 2503.10]  I think it's going to be, you know, it really helps to enable people who've been in a traditional
[2503.10 --> 2507.24]  environment to kind of move into the next era of databases and really learn.
[2507.24 --> 2510.70]  And it's not like learning from, you know, the bottom.
[2510.92 --> 2512.86]  It's you kind of have a foundation already.
[2513.98 --> 2514.10]  Yeah.
[2514.32 --> 2514.56]  Yeah.
[2514.62 --> 2519.48]  It's actually amazing how similar they look, but how different they feel when you actually
[2519.48 --> 2520.80]  start using the two things.
[2521.60 --> 2522.08]  Yeah.
[2522.96 --> 2524.82]  Let's talk a little bit about the business.
[2525.10 --> 2530.46]  And Rethink is a, we talked a little bit, you guys were in Y Combinator and this is public
[2530.46 --> 2530.88]  information.
[2531.02 --> 2535.06]  You guys put this, I think it's on your website or somewhere, but you guys have raised funding.
[2535.06 --> 2539.60]  But at some point, you guys have monetization at some point and making money.
[2539.70 --> 2542.50]  So what's the goal look like for Rethink as a business?
[2543.72 --> 2547.36]  So we really want the product to be open source forever.
[2548.26 --> 2549.56]  It's sort of at the core of what we do.
[2549.66 --> 2551.70]  Every developer here really cares about that.
[2551.76 --> 2554.94]  And we think it results in better software for people.
[2555.04 --> 2556.74]  So Rethink will always be open source.
[2558.30 --> 2561.26]  Well, always is a long time, but I mean, I really believe that.
[2561.40 --> 2563.62]  I can't see a world where it wouldn't be.
[2563.62 --> 2564.64]  Let's put it that way.
[2565.12 --> 2570.08]  But commercially, I mean, we wouldn't do anything very different from other companies
[2570.08 --> 2570.48]  like this.
[2570.62 --> 2576.00]  We plan to offer support versions, supported versions of RethinkDB, so support packages.
[2576.40 --> 2579.56]  And we found that what happens is developers pick up Rethink.
[2580.04 --> 2584.10]  They start building an application on it and then they hand it off to operations people.
[2584.22 --> 2588.50]  And operations people usually want to make sure that if something goes wrong, they can pick
[2588.50 --> 2590.76]  up the phone and call someone on the other end of the line.
[2590.76 --> 2593.38]  So that's the model for Rethink.
[2593.46 --> 2596.02]  We're going to offer support versions and announce them pretty soon.
[2596.10 --> 2597.76]  I can't talk about the details right now.
[2599.88 --> 2603.92]  And that's going to be the immediate monetization.
[2604.36 --> 2609.54]  And we have a lot of ideas on what to do after that, specifically with services and platforms
[2609.54 --> 2610.12]  as services.
[2610.12 --> 2611.84]  But I don't want to get into that too much.
[2612.22 --> 2614.00]  It's just it's a little bit early for that.
[2614.00 --> 2616.36]  Yeah, that's fine.
[2616.46 --> 2619.96]  So you guys, though, obviously are thinking about things like that.
[2620.20 --> 2625.16]  And part of what comes with that is, you know, you guys have started to really, well, I don't
[2625.16 --> 2628.36]  know if started is the right word, but some, you know, you guys have gotten some a lot of
[2628.36 --> 2628.74]  popularity.
[2628.74 --> 2633.34]  So when you first started working on this project and you guys kind of started the business and
[2633.34 --> 2638.48]  all that, there were other viable options to NoSQL and just databases in general.
[2638.48 --> 2644.64]  Were you expecting the kind of, you know, popularity that you guys have now and or has this kind
[2644.64 --> 2649.14]  of taken you by surprise, like as far as, you know, just your day to day goes?
[2650.30 --> 2655.24]  Oh, it's definitely taken us by surprise, at least was the very first release of everything
[2655.24 --> 2656.28]  to be as it is now.
[2657.06 --> 2659.64]  We worked, you know, these systems take a while to build.
[2659.74 --> 2662.52]  It's not like it took three months and then we released it.
[2662.52 --> 2669.60]  We were working on it pretty much in isolation for about, I want to say two and a half or
[2669.60 --> 2674.10]  three years because it took a really long time to design the architecture, make everything
[2674.10 --> 2679.44]  work and make like the first sort of quantum of utility, right, that we could release.
[2680.22 --> 2683.98]  And that's a really long time, like very few projects take that long.
[2684.08 --> 2690.50]  So when we released it and people were just absolutely blown away by the UI and the query
[2690.50 --> 2695.46]  language, how easy it is to use and how pleasant and how all these things feel, that, I mean,
[2695.52 --> 2696.76]  that felt amazing.
[2696.92 --> 2706.08]  We would never expect that kind of popularity early on because every time we'd make a decision,
[2706.24 --> 2708.76]  it sort of felt as the right thing, you know, at the time.
[2708.86 --> 2712.24]  But you never really know how people are going to perceive it or they're going to understand
[2712.24 --> 2712.44]  it.
[2712.48 --> 2714.86]  Is it going to be useful to people?
[2714.86 --> 2722.42]  And the fact that the unbalance, most of these decisions came out, I don't want to say right,
[2722.56 --> 2724.18]  but at least useful to a lot of people.
[2724.28 --> 2728.50]  I think that's definitely not something we expected to this degree.
[2729.98 --> 2731.64]  So when you guys started, who was the team?
[2731.96 --> 2733.66]  Like it was you and one other person, is that right?
[2734.14 --> 2735.88]  It was me and my co-founder, Michael.
[2735.88 --> 2741.64]  And we had the third co-founder, a guy named Leif from Stony Brook University, Leif Walsh.
[2741.90 --> 2744.06]  He has long, long flowing red hair.
[2744.32 --> 2745.52]  I still remember that.
[2746.14 --> 2747.48]  We're still, I mean, we're still friends.
[2747.84 --> 2753.90]  Leif now works at TokoTech, which is not a NoSQL company, but also in the database world,
[2753.98 --> 2755.02]  in the database industry.
[2755.60 --> 2761.24]  And then right now we're a team of 11, but it started with just the three of us.
[2761.24 --> 2761.68]  Right.
[2762.34 --> 2767.26]  I love looking at the people on RethinkDB and your title is raising the bar.
[2767.40 --> 2767.84]  What does that mean?
[2769.66 --> 2770.68]  Well, I'm the CEO.
[2770.84 --> 2772.50]  Officially, I'm the CEO of the company.
[2772.66 --> 2780.18]  But if you look at what I do on a daily basis, it's really anything from, you know, just basic services.
[2780.34 --> 2786.48]  Make sure, you know, the fridge is stocked and the engineers here have what they need to get their jobs done.
[2786.48 --> 2792.76]  All the way to feature design and architecture and project management and, you know, talking to people and things like that.
[2793.06 --> 2800.90]  But I think if you boil it down to one thing, it's about getting the product to be so good that people just can't ignore it.
[2801.38 --> 2805.50]  It's got to be so pleasant and so helpful and so nice for people.
[2805.50 --> 2814.14]  And they have to find it so valuable that they just can't, you know, not talk about it, not pick it up, not download it, not find it useful.
[2814.40 --> 2817.20]  And that, I think, is the main thing that I do.
[2817.36 --> 2818.62]  Or I'd like to think I do that.
[2818.90 --> 2820.26]  You know, the jury is still out.
[2820.48 --> 2822.58]  But that's how I think of my job.
[2823.22 --> 2823.44]  Awesome.
[2823.60 --> 2829.90]  So you guys got a bunch of contributors that you've kind of specifically noted just probably because of the amount that they've given to the project.
[2829.90 --> 2831.26]  But it looks like you're also hiring.
[2831.40 --> 2832.42]  Is that accurate?
[2833.26 --> 2834.12]  Yes, that's right.
[2834.12 --> 2839.88]  We actually – so I can't talk about this too much about the financing, but we're going to announce this pretty soon.
[2840.20 --> 2843.26]  And, yes, we're hiring people all over the board.
[2843.54 --> 2845.22]  I can talk about that a little bit.
[2845.38 --> 2849.30]  You know, I don't know if the audience is interested in this kind of thing.
[2849.36 --> 2856.12]  But, yes, we are hiring and we're looking to make the project hopefully even better than it is now.
[2856.86 --> 2857.22]  Awesome.
[2857.52 --> 2861.56]  If you're interested, just head over to their website and click on people and you can get some more information.
[2861.56 --> 2863.94]  Again, we won't belabor the point here.
[2865.04 --> 2868.14]  But, yeah, I mean, Rethink, it's really cool to see you guys growing.
[2868.28 --> 2871.50]  I want to kind of just in general thank you for being so flexible with me.
[2871.70 --> 2873.38]  This has been a crazy couple weeks.
[2873.38 --> 2880.24]  But it's been really cool to see Rethink growing and, you know, the company and the product and the community around it.
[2880.42 --> 2883.26]  And to me, any time that you can – I don't know.
[2883.36 --> 2885.64]  I look at – again, looking at your people page.
[2885.68 --> 2895.06]  And any time you can kind of distinguish the core team from the notable contributors and the contributors list is just as long, if not longer, than the core team, means that you've got something.
[2895.06 --> 2895.24]  Right?
[2895.28 --> 2900.20]  It means that the community is interested and it means that there's something here.
[2900.40 --> 2904.00]  And we just kind of hope that we can watch you guys succeed in the future with it.
[2904.28 --> 2913.34]  And, you know, it's definitely a really awesome product that when you – during the show today, you said that there was a bunch of things that are coming soon and announcements that are going to be made.
[2913.34 --> 2914.92]  And you didn't want to talk too much about them.
[2915.02 --> 2920.62]  So it sounds like there's going to be some news to follow to kind of keep up with Rethink.
[2920.70 --> 2921.92]  So how can people do that?
[2922.04 --> 2923.22]  How can people keep up with you guys?
[2923.78 --> 2925.96]  Yeah, there's definitely a lot of energy actually.
[2926.20 --> 2926.98]  So it's interesting.
[2927.08 --> 2930.74]  You started the show with Built With Love and why that is.
[2931.48 --> 2938.52]  And, you know, we think of ourselves, the people that work for Rethink, we just think of ourselves as contributors that happen to get paid.
[2938.58 --> 2941.52]  And there are a lot of contributors that, you know, just from the community.
[2941.52 --> 2944.84]  But so we try to get rid of that divide.
[2945.94 --> 2955.30]  And, you know, anybody who contributes RethinkDB and even the user is just sort of part of this group, part of the team, and everybody cares about the project and what it means.
[2955.64 --> 2959.66]  So to answer your question, you could follow at RethinkDB.com slash blog.
[2959.82 --> 2960.92]  We always announce things.
[2961.00 --> 2961.80]  You could look at GitHub.
[2962.46 --> 2967.94]  Or you could follow us on Twitter, just at RethinkDB, and all the announcements happen there.
[2968.08 --> 2970.02]  So any one of these three channels.
[2970.02 --> 2975.12]  You could hop onto IRC, and you'll know what's going on.
[2975.18 --> 2978.08]  And you can follow some of the energy and some of the things that are happening.
[2979.90 --> 2984.24]  So for our listeners that are new, we ask the same three questions at the end of every show.
[2984.46 --> 2985.12]  So we'll go ahead and ask them.
[2985.26 --> 2992.82]  The first question for you, Slava, is for a call to arms, for the community to help out with RethinkDB.
[2992.96 --> 2993.68]  What would you like to see?
[2993.68 --> 3004.72]  So what we're trying to do right now, a big push, is making the experience more unique for people who use Django, people who use Ruby and Rails, and people who use Node.js.
[3004.96 --> 3014.06]  So we already have the three drivers in the languages, but we want to make it unique and a nicer experience for people building specific, you know, using specific web frameworks.
[3014.06 --> 3026.46]  So for anybody who's a core contributor to Django or Rails or Node, we are hiring right now, and we're looking for people to contribute to the drivers and make RethinkDB just a better experience for those environments.
[3026.66 --> 3032.00]  Please shoot me an email, jobs at RethinkDB.com, and we'd love to talk about it.
[3032.56 --> 3035.78]  Other than that, download the product, you know, play with it, send us your feedback.
[3035.78 --> 3037.12]  Like, that's the most valuable thing.
[3038.08 --> 3038.48]  Awesome.
[3038.82 --> 3044.58]  If you weren't doing this, whether it was working at Rethink or just, you know, programming in general, what would you be doing instead?
[3045.78 --> 3051.00]  I'd try to pick another problem in software that I think would make a big difference in the world.
[3051.96 --> 3056.12]  The thing, I think, that really excites me is 3D printing.
[3056.72 --> 3061.14]  It reminds me of StartRec replicators, and I think it's going to be a huge deal.
[3061.50 --> 3063.68]  So if I weren't doing Rethink, I'd probably work on that.
[3063.68 --> 3066.40]  Nice. You'd be doing Rethink printing.
[3067.88 --> 3071.00]  Yes. I'd have to be useful. I'm not sure I know very much about the field.
[3071.46 --> 3075.42]  Well, you could at least, maybe you wouldn't be working on it, but you would be playing with the prototypes.
[3076.18 --> 3079.72]  Yes. We actually are building a 3D printer from a kit at Rethink.
[3082.10 --> 3087.32]  Awesome. And the last one is for a programmer hero, so somebody that's kind of influenced you up to this point in your career.
[3088.98 --> 3092.16]  I'd say it's, I mean, John Carmack comes to mind.
[3092.16 --> 3105.02]  I grew up with his games. I'm just absolutely amazed with his ability to marry research and pragmatism and getting people something amazing that they're just amazed by.
[3105.20 --> 3109.48]  And he really inspired me just as a kid when I started programming, and he still does.
[3109.48 --> 3117.68]  Yeah, that's a pretty, I was going to say, I remember his name from Quake and stuff, but looking at it, that's a pretty crazy chain.
[3118.00 --> 3123.64]  Wolfenstein 3D, Doom, Quake, Rage. That's crazy that he's kind of been the lead on so many successful projects.
[3124.08 --> 3130.42]  Yeah, the guy is amazing. I mean, he should be an inspiration, I think, to the whole generation of programmers. He probably is, right?
[3130.42 --> 3141.10]  Yeah. Awesome. I want to say thanks again for joining us, and I was, once again, to reiterate, we kept tossing your day around to which day you would join us,
[3141.16 --> 3148.72]  and every time you came back with a no problem, that'll work great, and you've been really flexible, and I just want to say I appreciate that for joining with us.
[3149.58 --> 3156.40]  Thank you, Andrew. I'm happy to be here. I'm always excited to talk about Rethink and talk about open source and technology in general,
[3156.40 --> 3159.98]  so it's no problem at all. I'm happy to be here. Awesome.
[3160.66 --> 3165.64]  I also wanted to give another shout-out to our sponsors, DigitalOcean and TopTal for supporting the show.
[3165.92 --> 3171.44]  Head to DigitalOcean.com to set up your cloud server today, and make sure you use our promo code CHANGELOGSENTME,
[3171.54 --> 3175.90]  that's CHANGELOGSENTME, all caps, to get a $10 hosting credit.
[3176.20 --> 3180.78]  And if you want to do freelance with companies like Airbnb, Artsy, or IDO,
[3180.78 --> 3188.60]  head to TopTal.com slash developer, and click Join the Best to see if you have what it takes to join TopTal's network of elite engineers.
[3189.14 --> 3192.48]  Again, that URL is TopTal.com slash developer.
[3192.78 --> 3195.58]  And that's it for this week. Thanks again to Slava for joining us,
[3195.62 --> 3198.36]  and also thanks to the listeners for tuning in and for your support.
[3198.88 --> 3200.88]  If you haven't yet, subscribe to the Changelog Weekly.
[3200.88 --> 3204.06]  It's our weekly email where we share everything that hits our open source radar.
[3204.44 --> 3207.80]  You can subscribe at thechangelog.com slash weekly.
[3208.28 --> 3209.48]  So for now, let's say goodbye.
[3210.78 --> 3240.76]  We'll see you next time.
