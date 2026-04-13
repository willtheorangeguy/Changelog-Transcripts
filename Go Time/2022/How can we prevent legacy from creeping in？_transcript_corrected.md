[0.00 → 4.02] When I hear the term legacy, I think there is this kind of feeling of dread that a lot of us have.
[4.10 → 6.06] But, you know, the term legacy can actually be a good thing, too.
[6.14 → 9.26] Like the legacy that you leave from the life that you lived and things like that.
[9.30 → 13.22] And I kind of take the same view that I take for something like debt.
[13.48 → 16.50] There's good debt. There's bad debt. There's good legacy. There's bad legacy.
[16.80 → 21.40] And I think that really informs the way that I also see legacy when it comes to code.
[21.40 → 24.14] I kind of see it's like anything that's hit production to me is legacy.
[24.52 → 26.06] It's out there. It's something to deal with.
[26.10 → 28.58] It's something that we have to maintain and we have to understand.
[28.58 → 32.20] Even if we don't necessarily like that code at the end of the day.
[35.76 → 38.40] This episode is brought to you by Source graph.
[38.82 → 42.94] Source graph is universal code search that lets you move fast, even in big code bases.
[43.56 → 48.18] Here's CTO and co-founder Bung Liu explaining the problems that Source graph solves for software teams.
[48.18 → 54.08] Yeah, so at a high level, the problems that Source graph solves, it's this problem of for any given developer,
[54.58 → 57.22] there's kind of two types of code in the world, roughly speaking.
[57.22 → 61.66] There's the code that you wrote and understand, like the back of your hand.
[61.78 → 65.26] And then there's the code that some idiot out there wrote.
[65.48 → 72.66] Or, you know, alternatively, if you don't like the term idiot, it's the code that some inscrutable genius wrote and that you're trying to understand.
[72.78 → 76.32] And oftentimes that inscrutable genius is like you from, you know, a year ago.
[76.32 → 80.72] And you're going back and trying to make heads or tails of what's going on.
[80.88 → 91.82] And really, Source graph is about making that code that some idiot or inscrutable genius wrote feel more like the code that you wrote and understand kind of intuitively.
[91.82 → 96.30] It's all about helping you grok all the code that's out there, all the code that's in your organization,
[96.56 → 102.64] all the code that is relevant to you in open source, all the code that you need to understand in order to do your job,
[102.70 → 105.86] which is to build the feature, write the new code, fix the bug, etc.
[106.34 → 106.82] All right.
[106.88 → 111.46] Learn how Source graph can help your team at info.sourcegraph.com slash changelog.
[111.46 → 115.32] Again, info.sourcegraph.com slash changelog.
[128.74 → 129.68] Let's do it.
[130.26 → 131.32] It's go time.
[131.90 → 137.04] Welcome to Go Time, your source for diverse discussions from around the Go community.
[137.04 → 141.58] Subscribe today at go time.fm and follow the show on Twitter.
[141.82 → 143.38] We are at GoTimeFM.
[143.76 → 148.78] Special thanks to our partners at Vastly for delivering Go Time superfast all around the world.
[149.10 → 151.66] Check them out for yourself at fastly.com.
[151.92 → 153.06] That's all for me.
[153.38 → 154.10] Here we go.
[163.40 → 165.36] Welcome to Go Time.
[165.36 → 171.54] Today, we're going to be talking about how to prevent legacy code from creeping in.
[171.82 → 178.02] I'm joined by a wonderful array of guests, as well as my lovely co-host, Chris.
[178.34 → 179.24] Hello, Chris.
[179.52 → 179.86] Hello.
[180.50 → 182.74] And yes, that is my voice you hear out there, listeners.
[182.96 → 185.42] I'm finally back after, what, four months?
[185.96 → 188.40] It's been quite a while, but I am very excited to be back.
[188.70 → 190.60] It's been far too long.
[190.60 → 197.44] And along for the ride with us, talking about how to work with, avoid issues arising from,
[197.90 → 204.76] as well as just how to deal with legacy code on a day-to-day basis, we have, firstly, Dominic
[204.76 → 207.90] St-Pierre, who operates a small consulting company in Montreal.
[208.58 → 214.42] He's the maintainer of an Asks alternative to Firebase called Static Backend, and is the
[214.42 → 216.58] author of Build SaaS Apps in Go.
[217.10 → 218.00] Welcome, Dominic.
[218.08 → 219.50] Welcome back, I should say.
[219.50 → 220.22] Thank you.
[220.38 → 221.34] Pleasure to have you.
[221.46 → 222.14] Happy to be here.
[222.52 → 228.74] Then we've got Misha, who is a first-time Go Time guest, but also, I'm told, a first-time
[228.74 → 229.90] podcaster in general.
[230.08 → 234.16] So very privileged that you decided to grace us as your first podcast.
[234.56 → 235.56] How are you today, Misha?
[235.96 → 236.94] I'm good, thank you.
[237.36 → 241.48] And then we have Jeff, who is an Associate Backend Engineer at the New York Times.
[241.56 → 244.94] I should also say Misha is also at the New York Times and is a software engineer.
[245.34 → 246.38] But welcome, Jeff.
[246.42 → 246.98] How are you?
[247.54 → 247.96] Great.
[247.96 → 249.26] I'm excited to be here.
[249.50 → 251.04] I'm excited to have you.
[251.46 → 253.98] And then, John, we've been here before.
[254.48 → 257.72] John Sab ados, who is also at the New York Times.
[258.10 → 259.40] I promise I'm not biased.
[259.56 → 262.40] They just happen to be people that I spend most of my life with.
[262.88 → 264.44] He was a staff software engineer.
[265.02 → 265.58] Welcome back.
[265.72 → 266.34] How are you today?
[266.58 → 267.90] Doing well and good to be back.
[268.42 → 268.72] Awesome.
[268.72 → 275.30] So before we kind of dive into the nitty-gritty, I wanted to ask the group, what is legacy code?
[275.54 → 279.10] How do we even define what we call legacy?
[279.68 → 282.12] I don't know whether, Dominic, you want to dive in?
[282.18 → 286.32] I know you've been working with something that I'm sure we would all agree is legacy.
[286.32 → 287.76] Yeah, yeah.
[287.80 → 292.42] I think in my case, it's really a passion, quote unquote, because, yeah.
[292.66 → 301.62] So to me, legacy is when a company starts to have difficulties hiring developers to work on their software.
[301.62 → 304.90] You can think of that as legacy, I think.
[305.20 → 309.72] Also, when there's no unit test, not perfect documentation.
[310.26 → 319.20] So very, very old software that nobody other than the original author can maintain anymore.
[319.56 → 322.68] I'm talking about like 20 years old software.
[322.90 → 326.40] So this is one of the things that I do in my consulting.
[326.40 → 327.40] So, yeah.
[327.52 → 334.98] So to me, when the tooling starts to not work for you anymore and things like that.
[335.06 → 335.36] So, yeah.
[335.56 → 339.58] In a nutshell, that's a little bit my definition of what legacy software is.
[339.80 → 341.46] So you said very, very old.
[341.96 → 343.26] So we're on Go time.
[343.72 → 347.14] Go, to me, doesn't feel like a very old language.
[347.82 → 353.22] So I wonder, maybe, John, I know that you've had a little bit of experience working with this,
[353.22 → 356.70] but at what point did Go applications turn into legacy?
[357.44 → 362.92] Well, so that's a good question because you can actually, and again, it depends on how you define legacy.
[363.22 → 370.06] But it's, at least in our scenario, it's very possible to have fairly recent code that is suddenly legacy.
[370.06 → 377.98] And like one example of where you might hit that is if you have a system that was implemented in a fashion that really didn't suit the need.
[378.14 → 382.18] So you're forced into a Greenfield rewrite and supporting two systems.
[382.18 → 384.46] That's an easy definition of legacy code.
[384.58 → 389.02] We've got a new thing that's going to do the stuff, but an old system that we have to support.
[389.28 → 395.34] I might define legacy code as any type of code that your engineers hate to work on.
[395.34 → 399.46] Okay, so any code that I don't want to work on, I can just say, oh, that's legacy.
[399.80 → 401.78] It was written last week, but it was too old.
[401.82 → 402.72] I don't want to work on it.
[404.34 → 404.70] Okay.
[405.36 → 410.90] And then I wonder, Jeff, specifically, I know you've kind of joined the New York Times preferably recently,
[410.90 → 414.38] and I know that you came to a kind of legacy system.
[414.90 → 420.78] Coming in, how do you identify whether something you're working on is legacy or not?
[420.78 → 426.62] Is it that like everyone in the team is saying, oh, this legacy system, but are there indicators when you're kind of joining a new team,
[426.90 → 428.88] you're like, oh, this feels legacy?
[429.42 → 436.22] I feel like part of it is everyone just says that this portion of our services are really difficult to work with.
[436.22 → 437.62] They're kind of considered legacy.
[438.16 → 439.42] But I don't know.
[439.46 → 445.70] I feel like maybe my own definition of what is legacy is kind of more broad than what's been given so far.
[445.70 → 452.96] I think legacy is definitely something that, for me, is something that is already there by the time you joined the team, right?
[453.34 → 455.76] Regardless of whether people like to work with it or not.
[456.30 → 457.88] That's kind of like software itself, right?
[457.88 → 460.24] We're building on top of what has come before us.
[460.98 → 464.40] So I guess that would kind of be my own definition of legacy.
[465.20 → 470.16] But I definitely take into account what other people on the team who have been working with the system have to say about it.
[470.16 → 474.94] But our old stuff or like our old system is very difficult to work with.
[475.04 → 478.92] It definitely informs my opinion on what I consider legacy.
[479.64 → 480.22] Yeah, for sure.
[480.22 → 490.12] And then obviously when we're talking about legacy, I feel like not only are we talking about legacy architecture, legacy infrastructure, but we have legacy dependencies.
[490.62 → 496.32] I mean, a lot of our apps have hundreds possibly of external dependencies.
[496.32 → 502.14] At what point do we, and how do we go about defining our dependencies as legacy?
[502.28 → 509.42] I don't know whether Misha, you wanted to speak a bit on kind of how do you think about dependencies and when they become legacy?
[509.88 → 510.10] Right.
[510.22 → 518.52] Well, so, for example, the project that I work with now, which is written in Go, it's about two years old at this point.
[518.52 → 525.50] So probably not legacy code, strictly speaking, although there are parts of it that are starting to feel like legacy code.
[525.82 → 528.08] We can talk about that separately later.
[528.26 → 534.56] But yeah, as far as external dependencies that are legacy systems, we have a few of those.
[534.56 → 548.94] The way we've dealt with them is by caching as much as possible, caching the data that's returned by the external dependencies to reduce the latency, essentially of dealing with external legacy projects.
[549.54 → 552.38] And is that something that you do for all of your dependencies?
[553.02 → 556.18] Or is that something you kind of have a specific list?
[556.52 → 557.84] Or like, how do you make that decision?
[558.22 → 563.80] So on our team, we made those decisions specifically based on our latency metrics.
[563.80 → 571.40] So it doesn't really matter whether the external dependency was written in Go or Java or what have you.
[571.52 → 576.70] If we feel like we need to optimize for latency, we try to cache it.
[577.10 → 578.22] That's with our approach.
[578.86 → 582.58] So yeah, monitoring and testing for latency in this case.
[583.10 → 583.80] For sure.
[584.24 → 592.94] And then obviously, when we're talking about legacy in its many different definitions, because, you know, as we kind of can tell from even these initial definitions,
[592.94 → 601.50] there is kind of a fluid way of defining, we can't just identify and then say, great, we're going to rebuild, refactor.
[602.12 → 608.14] We have to maintain it, whether it be for a month, a year, many, many years.
[608.14 → 619.80] So I'd love to hear a little bit about what it is like, both from like a day to day, personal, but also from a technical point of view to maintain legacy code.
[620.20 → 625.16] And I know kind of Chris, our wonderful co-host has been kind of spearheading a maintenance series.
[625.16 → 629.80] So I know this really tees into the various different topics you've been exploring.
[630.30 → 639.02] Perhaps for our listeners who aren't fully familiar, I'd love to kind of pass over to you, Chris, before we dive in to talk a little bit about like how we've been exploring and thinking about maintenance.
[639.84 → 649.66] Yeah, I guess I would start with saying my view of maintenance is definitely not, I think, in some ways as maybe negative as everybody else seems to think it is.
[649.66 → 654.38] Like when I hear the term legacy, I think there is this kind of this feeling of dread that a lot of us have.
[654.46 → 659.96] But, you know, the term legacy can actually be a good thing, too, like the legacy that you leave from the life that you lived and things like that.
[660.00 → 663.92] And I kind of take the same view that I take for something like debt.
[664.16 → 667.64] It's like there's good debt, there's bad debt, there's good legacy, there's bad legacy.
[668.14 → 672.72] And I think that really informs the way that I also see legacy when it comes to code.
[672.78 → 675.82] I kind of see it's like anything that's hit production to me is legacy, right?
[675.82 → 679.54] Like it's out there, it's something you have to deal with, it's something that we have to maintain.
[679.66 → 684.48] And we have to understand, even if we don't necessarily like that code at the end of the day.
[684.64 → 692.86] So I think like before it gets to production, when you can still change it and mould it and do what you like with it, I think at that point, yeah, we're still dealing with something that's not legacy.
[692.98 → 694.16] It's not debt yet.
[694.40 → 697.38] It's not something that like we have to necessarily deal with in the future.
[697.58 → 701.68] But once it hits production, once it's out there, it becomes very difficult for us to pull back.
[701.84 → 705.68] Now, of course, we can get into the semantics of what does it mean when something actually gets to production.
[705.96 → 709.16] But I think that's like the way that I at least conceptualize this.
[709.16 → 715.18] So I think pulling it further back than anybody else has and really seeing it as like, well, all of our code is legacy.
[715.46 → 720.66] And it really comes down to like, which code do we think is good legacy and which code do we think is bad legacy?
[721.40 → 724.94] Well, yes, I really like what I'm hearing so far.
[724.94 → 734.08] One thing that jumped to my mind is, to me, a Go code base, even though it might not have been designed the proper way or whatnot, it's still easier to refactor.
[734.26 → 739.10] It's still easier to change the status of the code base.
[739.10 → 741.98] Because there's probably unit tests and whatnot.
[742.10 → 746.92] There are probably lots of tests in a modern code base.
[747.48 → 754.86] So to me, I understand all of this, but I feel it might not be the same thing here.
[754.86 → 763.72] When you're stuck with something and, yeah, you don't have anything, anything, no documentation, no tests to exit yourself out of this situation.
[764.02 → 766.58] Because like you said, I really like what you said.
[766.66 → 767.34] Everything is legacy.
[767.52 → 768.42] Yeah, I understand that.
[768.42 → 775.54] But it seems to be that when the budget is there and when the team is there, you still have option.
[775.86 → 784.66] Whereas I work at small companies that they just cannot invest into any kind of refactor or even a rewrite at that.
[785.14 → 787.98] So you still have to maintain the code base.
[788.30 → 794.10] Yeah, and I think that's definitionally just bad code at the end of the day, like if you can't maintain it in any way.
[794.10 → 799.94] But I would also say I've run into lots of circumstances where we have lots of tests, and they're not good.
[800.06 → 801.48] They give us a false sense of confidence.
[801.70 → 804.40] Or you have lots of tests, and they're written in the wrong way.
[804.46 → 809.04] So whenever you touch something of the code base, you have to go refactor a few hundred lines of tests.
[809.60 → 814.68] So I think even in your example there, it's like, yeah, no, tests definitely can make a code base better.
[815.16 → 817.38] And generally they show the mark of a better code base.
[817.44 → 821.38] But I think there are ways in which even those types of code bases can be a pain to work with.
[821.38 → 830.32] But I would absolutely say like a code base that has zero tests, no documentation, none of that is like the worst kind of legacy code bases that we can deal with.
[830.32 → 835.58] How do you know then if your test suite is going to be good for the long run?
[836.08 → 838.02] Good design of your software.
[838.72 → 844.60] Like I think like if you kind of got to push the boulder up the hill or like kind of really go back to the genesis of the stream, right?
[844.60 → 854.16] It's a lot easier to like if you're going to build a dam, it's a lot easier to build a dam across a stream that's two feet wide than it is to build one across one that's 200 or 2,000 feet wide.
[854.38 → 862.02] So, yeah, it's like if we put a lot of the stuff downstream to know if we've done the right thing, we can through various techniques understand how good it is.
[862.02 → 868.08] But I think it's much better to try and put in ways of knowing how correct your code is upstream.
[868.30 → 872.92] But of course, too, it's like a stream, a dam across two feet of stream is quite useless of a dam.
[873.24 → 876.50] So there's a middle ground here of where we need to find the right place to put things.
[876.54 → 883.38] And I've definitely found that right place to be in good design documentation and good design ideology for the software that we build.
[883.74 → 886.76] But I'm sure other people have different opinions on that.
[886.76 → 891.00] And I think I'd add modern code base does also do not mean tested.
[891.46 → 897.66] There's plenty of fresh code that I see written that like engineers oftentimes don't like to write tests.
[897.96 → 904.88] So that is a pervasive problem that seems to plague all code bases and stuff just isn't tested.
[904.88 → 916.16] Yeah, one thing I can say we've done to kind of mitigate that problem is to keep an eye on the coverage thresholds and actually building the test coverage thresholds
[916.16 → 918.68] into our testing and deployment pipeline.
[919.12 → 924.24] So if someone adds new code without adding tests, the pipeline actually fails.
[925.02 → 927.30] So that is definitely an interesting approach.
[927.36 → 930.06] But I've also seen it backfire horribly in the past.
[930.06 → 941.00] I've seen engineers and this actually got somebody talking to, but like this is in Java land, put an entire class on a single line because they were just annoyed by the test coverage requirements.
[941.00 → 946.18] And so you can kind of get malicious compliance with those code coverage requirements.
[946.38 → 949.60] And also depending on your language, like Go, it's not as bad.
[949.70 → 956.12] But in Java land, there are lots of all sorts of like you've got to catch these exceptions that practically are never going to happen.
[956.12 → 959.46] But you might not even be able to write tests to get there.
[959.88 → 963.32] So I think you do have to be a little bit careful with coverage requirements.
[963.54 → 965.66] I think it's a good metric to have and to track.
[965.98 → 969.98] But there's a danger zone when you start failing builds because of it.
[969.98 → 974.54] I mean, I'm interested to hear a little bit more about your reference kind of Java, Go.
[974.54 → 987.86] Are there aspects of Go as a language that make it easier for you to either avoid quote unquote legacy code or avoid it being a whole huge refactor project?
[988.04 → 993.46] Because in fact, refactoring, you know, bit by bit, you know, backwards compatibility comes to mind.
[993.64 → 998.44] Are there aspects of Go that make it easier for us to avoid legacy creeping in?
[998.44 → 1002.26] So I think there's some in that it's a simpler language.
[1002.38 → 1004.20] Up until recently, it didn't have generics.
[1004.28 → 1010.96] So you're not going to have people going nuts with generics and creating really complex things like trying to deduplicate everything through generics.
[1011.20 → 1012.12] So that helps.
[1012.46 → 1019.44] But I think the biggest thing that Go has going for it with like the lack of legacy and maintainability is that it's a newer language.
[1019.44 → 1021.30] It hasn't been around for that long.
[1021.68 → 1029.86] So you don't have projects that have been sitting under or that, you know, have been that were conceptualized 20 years ago to carry that forward.
[1029.98 → 1034.66] But there are a lot of Java projects out there that have been around for a long period of time.
[1035.08 → 1041.62] And so I think there might be a false sense of security saying, well, Go is going to have less legacy just because, you know, you don't see it as much.
[1041.62 → 1048.62] But that's also a function of the language being newer and therefore not having, you know, just the crap that's been around for a long time.
[1048.98 → 1052.66] And that's also something like we learn every time we write code and every time we develop.
[1053.02 → 1060.46] So there are a lot of patterns that, you know, we might have been doing 20 years ago in Java land that, you know, we've maybe learned better ways for that are being let go.
[1060.86 → 1065.46] But again, that's not so much a function of the language, just of the newness of it.
[1065.46 → 1082.32] I just wanted to add that what John was saying kind of made me think about what this topic of legacy will be like for Go in like 10 or 20 years in terms of when it gets to be old enough to like the same age as Java is currently.
[1082.68 → 1087.04] And we have a lot more Go projects around that need maintenance.
[1087.26 → 1090.90] It's just an interesting thought experiment to be having.
[1090.90 → 1097.96] Well, I can tell you about stories that, you know, with .NET, even though, let's say it started in 2001.
[1098.16 → 1105.24] So in 2005, there were already projects that you could not even migrate to the next version.
[1105.62 → 1113.68] So to me, the tooling that the language provide, which is very solid in Go, in my opinion, and the fact that it's backward compatible,
[1113.68 → 1119.48] if they can maintain that for a long time, it will diminish the effect of that.
[1119.48 → 1120.56] Yes, I'm certain of that.
[1120.64 → 1126.82] Because in my case, at the moment, the tooling of Microsoft is my main issues.
[1127.20 → 1128.26] It's not the code per se.
[1128.44 → 1131.02] I mean, it's not that at all, but the tooling.
[1131.64 → 1136.16] And I guess I'd be interested that because I've never really worked in .NET, always been allergic to Windows.
[1136.16 → 1146.14] But the Java side of things, you do have, like, you know, but they strive for a long time to make the JVM backwards compatible with prior versions of Java.
[1146.38 → 1154.66] And that didn't necessarily stop, like, the need to have complete rewrites or, like, you being stuck on an ancient version of Java because, like, whatever new thing.
[1154.66 → 1165.86] I've actually even seen the new thing with Go where they're seeing projects that were, like, running on old versions of GAE that have pinned their version of Go to, like, 111 or something.
[1166.10 → 1168.20] And, like, upgrading those has become a nightmare.
[1168.20 → 1171.76] So, again, it's less likely in Go.
[1171.88 → 1178.56] And it is, for sure, easier to generally upgrade versions of Go than my experience has been with Java.
[1179.00 → 1187.58] But, again, in Java land, you're also dealing with a ton more dependencies because there's this massive ecosystem that abounds where you're not having to do everything.
[1187.78 → 1191.08] Where in Go, a lot of that ecosystem doesn't exist.
[1191.24 → 1195.04] So you're reimplementing a lot of things and not sucking in as many dependencies.
[1195.04 → 1201.26] So the benefit of that is when you continue to upgrade, you're only worried about your code, not, like, a million different libraries.
[1201.96 → 1208.96] I'd be curious to see if that easy to upgrade continues as the Go ecosystem grows and as it becomes more complete.
[1209.28 → 1211.32] Yeah, but you are talking about the platform.
[1211.48 → 1213.96] So the Google App Engine is a platform.
[1214.14 → 1218.90] It's not really Go's fault or responsibility, in a sense.
[1218.90 → 1225.40] You can still take code bases from, like, early, early days of Go and compile that with the new compiler.
[1225.60 → 1228.56] This is something that you just cannot do in the .NET world.
[1228.76 → 1231.16] So that's mostly what I'm talking about.
[1231.30 → 1242.94] When the tooling is failing you, it's a different ballgame because you have the code, but you have the technologies that were suggested to use.
[1242.94 → 1255.26] When a company makes a choice of going with something and three years later, it's not even supported by Microsoft anymore, then it's a different thing than bad design, I think.
[1255.60 → 1263.54] Yeah, and I guess there's a different user or past user story there and experience because, like, again, coming from Java land, like, everything will compile just fine.
[1263.54 → 1271.68] But the things that I've encountered that I've seen that make, like, upgrading hard isn't so much the compilation, which it sounds like in .NET that might be a thing.
[1272.04 → 1276.78] But it is the platform that is the hard thing to upgrade from my experience.
[1277.20 → 1288.98] And, you know, so that's where I think that Go won't be immune to the platform increasing scope and, like, hardness to upgrade with that as it becomes more robust.
[1289.68 → 1292.34] Or there are more things going to be, like, GAE and whatnot.
[1292.34 → 1295.04] So I think I definitely agree with you.
[1295.12 → 1299.32] Yeah, if your vendor is making stuff that doesn't compile it in three years, oh, my God, that stuff's terrible.
[1299.88 → 1300.38] I'm sorry.
[1301.04 → 1302.38] Yeah, I can give another example.
[1302.38 → 1308.00] So, you know, our TLS 1.1 just vanished recently.
[1308.22 → 1316.88] But there is still an old application that runs under an old version of Windows Server 2008, which is not supported anymore.
[1316.88 → 1323.54] But because their migration path to the next version of .NET is not an easy one.
[1323.80 → 1325.30] I'm not saying it's not possible.
[1325.54 → 1326.36] It's not what I'm saying.
[1326.46 → 1331.64] But there is a lot of investment that the company needs to do to migrate to the next version.
[1332.30 → 1335.30] So that's another aspect of legacy.
[1335.30 → 1344.30] I mean, when the OS and the bare-bones communication system, the protocol starts to fail you, what do you do?
[1344.38 → 1355.20] So I had to start writing some very, very small piece in Go that just do HTTP call because I needed to use TLS 1.2 or 1.3.
[1355.20 → 1358.18] So, yeah, it's a different ballgame, I think.
[1358.64 → 1366.30] That does bring up, like, is working in legacy with closed-source systems different from working in legacy with open-source systems when it comes to those dependencies?
[1366.72 → 1368.28] Because that is one thing.
[1368.32 → 1372.02] That's one thing I've always liked about working in all the various different texts.
[1372.20 → 1373.54] I've been in its open-source scene.
[1374.90 → 1376.16] Oracle buys Java.
[1376.84 → 1380.64] Somebody's going to be like, well, we can take the JVM and run with it still.
[1380.86 → 1381.54] Open JDK.
[1381.78 → 1383.26] It's been a while since I've been to Java land.
[1383.26 → 1387.12] So I'm not sure how successful OpenJDK has been, but that is a possibility, right?
[1387.30 → 1392.74] When you've got open-source, closed-source, you might be forced into complete rewrites.
[1393.40 → 1408.14] So do we feel like that's one of the kind of differentiators of Go in that, you know, we have this vibrant, wonderful community where if there's anything that is detrimental is causing people to feel that it's legacy in some way in terms of the tools provided,
[1408.38 → 1412.98] that there's going to be mass opera in the community be like, hey, can we fix this, please?
[1413.26 → 1414.72] It definitely can help.
[1415.14 → 1419.80] Up until the point that there's enough bifurcation that there's a fork, which hopefully won't happen.
[1420.02 → 1423.62] And it's rare to see languages truly fork like that.
[1423.80 → 1427.50] So I think largely, yes, but that forking is also a potential danger.
[1427.84 → 1429.12] Languages except for JavaScript.
[1431.02 → 1431.92] Oh, God.
[1432.06 → 1432.40] JavaScript.
[1432.74 → 1432.96] Yay!
[1432.96 → 1433.14] Yay!
[1433.14 → 1433.16] Yay!
[1433.16 → 1433.26] Yay!
[1433.26 → 1433.96] Yay!
[1433.96 → 1444.98] This episode is brought to you by our friends at Square.
[1445.28 → 1452.00] Millions of Square sellers use the Square app marketplace to discover and install apps they rely on daily to run their businesses.
[1452.00 → 1456.52] and the way you get your app there is by becoming a Square app partner.
[1457.00 → 1458.12] Let me tell you how this works.
[1458.56 → 1463.42] As a Square app partner, you can offer and monetize your apps directly to Square sellers
[1463.42 → 1466.70] in the app marketplace to millions of sellers.
[1466.70 → 1470.68] You can leverage the Square platform to build robust e-commerce websites,
[1471.10 → 1474.96] smart payment integrations, and custom solutions for millions of businesses.
[1475.50 → 1476.56] And here's the best part.
[1476.88 → 1480.40] You get to keep 100% of revenue while you grow.
[1480.40 → 1486.62] Square collects a 0% cut from your sales for the first year or your first 100 Square referred sellers.
[1487.04 → 1490.70] That way you can focus on building and growing your Square customer base,
[1490.84 → 1493.02] and you get to set your own pricing models.
[1493.56 → 1495.40] You also get a ton of support from Square.
[1495.76 → 1498.06] You get access to Square's technical team using Slack.
[1498.32 → 1501.92] You get insights into the performance of your app on the app marketplace.
[1502.50 → 1505.16] And of course, you get direct access to new product launches.
[1505.74 → 1509.36] And all this begins at changelog.com slash Square.
[1509.36 → 1512.22] Again, changelog.com slash Square.
[1512.22 → 1529.34] So you talked about kind of the pains of maintaining and the need to,
[1529.76 → 1532.94] as you kind of touched upon Dominic, kind of hacking these small solutions
[1532.94 → 1535.82] to make sure your apps continue running.
[1535.82 → 1541.40] But at what point do you kind of throw your hands up and say,
[1541.64 → 1543.44] no, we need to completely rewrite this?
[1543.80 → 1546.32] Like this needs to have, well, one,
[1546.90 → 1549.44] reliant upon having the time and investment to do that,
[1549.48 → 1550.60] but we'll touch on that later.
[1551.20 → 1555.60] But if you feel like there is the time and investment to do a rewrite,
[1555.74 → 1560.68] at what point do you go from maintaining to really advocating for,
[1560.84 → 1563.58] we need to, you know, rip this out and plant a completely new tree?
[1563.58 → 1568.24] One nice thing about legacy software is that at some point,
[1568.34 → 1572.82] they kind of run without any intervention from any developers.
[1573.18 → 1577.28] So that is something that could help with a complete rewrite.
[1577.50 → 1581.44] If the company is able to do that and sees the value in doing that,
[1581.96 → 1584.30] then yes, I think at some point the maintenance,
[1585.04 → 1589.26] because after 20 years, you're not really maintaining any code base.
[1589.40 → 1591.54] You know, you're not changing lots of code base.
[1591.54 → 1595.16] It's everything around the software that is failing.
[1595.62 → 1596.70] So it's not the code.
[1596.76 → 1597.88] The code is battle tested.
[1598.02 → 1599.60] So even though there's no unit test,
[1599.92 → 1603.54] I trust this old software completely.
[1604.10 → 1605.86] You know, they have been fixed.
[1606.10 → 1608.70] There is not really any bugs anymore.
[1609.20 → 1610.20] They are pretty stable,
[1610.20 → 1614.28] but it's a huge investment to decide to rewrite the software,
[1614.78 → 1617.44] especially old application like that.
[1617.86 → 1621.72] So yes, I don't really know how to answer that,
[1621.88 → 1625.96] but maybe someone else has another point.
[1625.96 → 1631.36] I don't know that there is like a hard and fast rule for when to do a green or a Greenfield rewrite,
[1631.36 → 1635.24] other than it should probably be like one of your last resorts,
[1635.24 → 1638.24] because it is an incredibly expensive thing to do.
[1638.76 → 1640.92] Oftentimes you have to do it bug for bug,
[1641.02 → 1642.80] depending on your downstream clients.
[1642.80 → 1645.18] And that can be a nightmare to do.
[1645.18 → 1649.34] So, and you know, different scenarios can offer different reasons.
[1649.54 → 1651.50] Like, you know, if you're doing a cloud migration,
[1651.72 → 1658.12] well, there may very well be a reason to do a Greenfield rewrite of fairly recent stuff in that case,
[1658.12 → 1660.98] because your underlying platform is changing dramatically.
[1661.18 → 1662.90] Based on the projects I've seen,
[1663.08 → 1668.34] there definitely needs to be a close alignment between business and product,
[1668.34 → 1673.32] as it were, business requirements and sort of the tech requirements
[1673.32 → 1676.00] and what needs to be done on the tech side,
[1676.08 → 1679.66] because that's when you start seeing possible solutions like,
[1679.80 → 1682.70] oh, well, maybe I don't need to rewrite the whole thing, right?
[1682.78 → 1686.70] Maybe I need to rewrite just parts of my legacy code,
[1686.70 → 1694.26] and those will work as standalone pieces while the legacy thing continues to kind of chug away in the background.
[1695.12 → 1697.02] And also, of course, the expense part,
[1697.02 → 1702.50] that needs to be kind of understood and underwritten by your business,
[1702.50 → 1707.02] if that is to happen, if any kind of rewrite is to happen.
[1707.48 → 1710.02] I'm kind of curious whether,
[1710.30 → 1714.14] when it is important to be, for business and product to be aligned,
[1714.24 → 1719.24] but also taking into account kind of the engineering quality of life.
[1719.42 → 1723.84] Like, if your engineers are feeling like I'm spending all my time,
[1723.84 → 1727.38] like Dominic said, I'm not like fixing the code itself.
[1727.38 → 1730.92] I'm trying to keep the code standing and keep it running,
[1731.38 → 1733.12] because everything around it is just crumbling.
[1733.80 → 1739.78] Speaking for myself, I don't feel like I would last very long if that's all I was doing at a company.
[1740.32 → 1741.48] Like, yes, I can.
[1741.48 → 1746.82] I'm willing to support legacy systems, but I don't want, that's not all I want to be doing.
[1746.96 → 1749.86] I want to be at least adding, like creating something new,
[1750.22 → 1751.64] or at least extending it or something.
[1752.16 → 1755.48] I don't want to just be maintaining forever.
[1755.94 → 1761.22] And I feel like I won't grow as an engineer if that's all I'm allowed to do.
[1761.22 → 1765.02] Yeah, I can totally relate with what you're saying.
[1765.54 → 1767.16] Yeah, if you're an engineer, I suppose, sorry.
[1767.80 → 1769.82] I'm alone at the company at the moment.
[1769.94 → 1772.94] So they are simply not able to hire anyone else.
[1773.16 → 1774.62] So I'm kind of stuck there.
[1774.88 → 1778.44] I do think there are some engineers who actually do like kind of just
[1778.44 → 1782.34] tinkering on old code bases and not adding new features or anything,
[1782.44 → 1784.66] but just like keeping something running.
[1784.78 → 1789.50] I think there are people that just like get an immense amount of joy out of just doing that.
[1789.50 → 1792.96] But I definitely think like trying to put engineers that don't want to do that sort of thing
[1792.96 → 1795.58] onto a code base that is, that's all the work.
[1795.68 → 1798.20] It's not going to work out very well for anybody involved.
[1798.60 → 1804.10] And do you feel like that is more in keeping with just like personal preference?
[1804.10 → 1808.86] Or is that perhaps to do with like where you are in your progression as a software engineer?
[1809.32 → 1812.58] I mean, purposefully, we have kind of a range of different levels on this call
[1812.58 → 1817.68] because I wanted to really get an understanding of what is it like coming in like at Jeff's level
[1817.68 → 1823.56] and, you know, very early looking to learn, looking to grow at a very rapid pace versus someone
[1823.56 → 1826.48] like Chris, John, et cetera, who are at that.
[1826.96 → 1828.06] I don't want to say end phases.
[1828.20 → 1829.68] You have many more years in you.
[1830.54 → 1831.62] But you see what I'm saying?
[1831.70 → 1836.42] Like you've worked on enough problems to have learned a massive amount and perhaps to find
[1836.42 → 1838.74] a new problem for you to solve is more difficult.
[1839.12 → 1840.82] Or do you think it's just personality?
[1840.96 → 1841.50] Go on, Chris.
[1841.50 → 1845.40] I think it's a different type of engineering rather than a certain level of it, right?
[1845.40 → 1849.20] I think it's like there are people that want to be maintenance engineers in the same way
[1849.20 → 1853.94] there are people that want to just be like pure R&D, pure prototype engineers.
[1854.04 → 1854.94] Like they want to build stuff.
[1855.10 → 1858.48] They never want any of that to be in production because they know that it's like not going
[1858.48 → 1859.08] to survive production.
[1859.18 → 1860.92] And they know that they don't want to have to maintain it.
[1860.96 → 1862.54] They're like, I'm just doing research.
[1862.62 → 1864.06] I'm just proving out an idea.
[1864.54 → 1865.50] That's what I like doing.
[1865.62 → 1870.40] And I think there's levelling within those types of engineering, but I don't think they kind
[1870.40 → 1872.16] of like stack on top of each other or anything.
[1872.16 → 1875.30] I think there's like, okay, maybe you're on one far into the spectrum.
[1875.46 → 1879.20] You really like getting one of those old, nasty code bases.
[1879.30 → 1880.86] You're like, I'm just going to, I'm not going to add anything new.
[1880.88 → 1881.76] I'm just going to like to fix it up.
[1881.84 → 1882.42] I'm going to add tests.
[1882.50 → 1883.30] I'm going to document things.
[1883.34 → 1886.46] I'm going to turn this into like a really nice code base to work within.
[1886.72 → 1889.36] And then there's, you know, the other end of the spectrum is those prototype people
[1889.36 → 1893.16] that are like, I just write code that I just copper together and like make something
[1893.16 → 1893.64] work.
[1893.82 → 1896.36] But like, there's no way this will work for the long term.
[1896.66 → 1899.42] And I think, you know, the majority of engineers fall in the middle.
[1899.42 → 1900.78] Like they like doing some new stuff.
[1900.84 → 1902.26] They like maintaining some old stuff.
[1902.52 → 1903.62] And that's just kind of what it is.
[1903.64 → 1907.22] And I think it's important that we start seeing that as a spectrum instead of trying to see
[1907.22 → 1909.60] that as like, well, who's better than the other?
[1909.68 → 1910.72] It's like, there's no better.
[1910.88 → 1913.06] There's just like, we need a bit of all of them.
[1913.12 → 1914.82] You need to keep your organization balanced.
[1914.82 → 1918.32] And I think that's one of the criticisms I have for a lot of tech companies right now is
[1918.32 → 1923.18] that they are very much focused on that, the other end of that spectrum that is the
[1923.18 → 1926.00] R&D engineers and the people that want to build newer things.
[1926.16 → 1930.06] And the results of that is a lot of code bases that don't wind up getting properly maintained
[1930.06 → 1933.58] because there's no one in the company that wants to do that maintenance.
[1933.78 → 1936.98] So there's no one in the company that's advocating for it, even though everybody in
[1936.98 → 1938.62] the company is aware that it needs to happen.
[1938.72 → 1939.56] And I think that happens.
[1939.62 → 1943.36] A lot of teams sitting there are being like, well, we really want to work on all of this old
[1943.36 → 1945.96] legacy stuff, but where's the time to do it?
[1946.04 → 1947.44] Where, and how are we going to make this happen?
[1948.04 → 1949.48] So I think like getting some of that balance is good.
[1949.54 → 1952.52] But to answer your original question, yes, I think they are different types of engineering,
[1952.72 → 1955.92] not different amounts of time that you've been doing software engineering.
[1956.42 → 1956.92] Yeah, for sure.
[1957.42 → 1963.70] And kind of off the back of that, like people know that a certain platform, a certain part
[1963.70 → 1966.08] of their technology, their stack is legacy.
[1966.28 → 1968.50] And it's all kind of, it's known about like you're slacking about it.
[1968.52 → 1969.74] Oh, this annoying platform.
[1969.92 → 1971.86] Oh, this annoying, like it's all known.
[1971.86 → 1978.40] How do you then advocate for a rewrite or for the time to maintain?
[1978.58 → 1984.06] Like what are from your experiences, the key things that you have to kind of bring up
[1984.06 → 1989.16] to get buy in from kind of product business, et cetera, to actually give you that time?
[1989.22 → 1992.22] Because that is, I know, a challenge that many people face.
[1992.30 → 1993.74] So how do you, how do you overcome that?
[1993.78 → 1994.60] How do you make them care?
[1995.08 → 2000.48] That's a hard problem because it's effectively like that maintenance is a cost centre with
[2000.48 → 2003.58] no, like you don't see the benefits immediately.
[2003.58 → 2008.82] And generally my experience has been everyone is short-sighted and more concerned about getting
[2008.82 → 2013.78] their current feature out than they are about the ability to add another feature six months
[2013.78 → 2014.58] down the line.
[2015.06 → 2019.80] And I think the best argument that I've had is like working with business and explaining,
[2019.96 → 2025.16] you know, that this tech debt is something that actually has a cost down the line and will
[2025.16 → 2027.44] impede future things.
[2027.44 → 2031.10] And most people understand the idea of debt, you know, there's only so much you can have
[2031.10 → 2035.70] and explaining it as teach debt and being like, you know, we will get to the point where all
[2035.70 → 2040.30] we can do is pay our tech debt, and we won't be able to make any new investments.
[2040.80 → 2042.50] And oftentimes that falls on deaf ears.
[2042.76 → 2048.00] So I definitely think structuring it as a conversation around debt and the financial aspect of it can
[2048.00 → 2048.42] help people.
[2048.42 → 2052.90] But also just like, I think a lot of it has to do with process and project management of like,
[2052.90 → 2057.46] okay, like when we said that we could like, when we said that we could deliver this feature,
[2057.52 → 2061.30] we said it would come with this amount of debt, this amount of stuff that we have to do later.
[2061.56 → 2062.88] Well, here's the later part.
[2063.04 → 2064.48] And we have to go do that.
[2064.50 → 2065.70] And you said that we could do it.
[2065.78 → 2070.14] So you're going to have to actually stick to what you said you were going to do and give us
[2070.14 → 2070.86] the time to do this.
[2070.90 → 2073.18] I think it does take a lot of fighting and advocating.
[2073.18 → 2077.86] But I think part of the problem is that in general, the teams I've been on have been
[2077.86 → 2082.48] kind of not great at explaining exactly what that technical debt is.
[2082.54 → 2086.04] It's like we took on some technical debt, but it's just kind of this mysterious thing,
[2086.08 → 2086.18] right?
[2086.38 → 2087.88] It's like, oh, you got to go write some tests.
[2087.92 → 2089.36] You got to go do some other stuff.
[2089.80 → 2093.96] So I think it's less that product and business don't want to pay for it.
[2094.02 → 2098.44] But the cost of it is kind of like not known, not quantifiable.
[2098.44 → 2102.52] It's like if we talked in debt, but you never knew or never found out what the interest rates
[2102.52 → 2102.80] are.
[2102.96 → 2105.60] And it's like, OK, well, you're telling me you have to pay down this debt.
[2105.72 → 2110.56] But is this debt that's at a 0.5% interest rate or at a 25% interest rate?
[2110.66 → 2113.78] Because we're going to deal with that in very, very different ways.
[2113.88 → 2118.10] Like 25% interest rate, we got to pay that down immediately, stop everything else, get
[2118.10 → 2119.64] rid of that 0.5% interest rate.
[2119.66 → 2122.38] I'm just going to let that sit there because it's not going to cost me much in the long
[2122.38 → 2122.62] run.
[2122.68 → 2126.94] And not being able to talk about things in that kind of quantifiable level, I think is what
[2126.94 → 2131.18] holds back a lot of engineering organizations from being able to pay down that technical debt
[2131.18 → 2132.30] and handle that legacy.
[2132.52 → 2137.30] So I think, at least in my experience, the closer that I've gotten to talking in terms
[2137.30 → 2139.70] that are more concrete of like, here's what we need to do.
[2139.80 → 2140.78] Here's the technical project.
[2140.88 → 2141.68] Here's the plan for it.
[2141.74 → 2142.94] Here's how much time it's going to take.
[2143.20 → 2145.58] And here are the benefits that we're going to get out of it at the other end.
[2145.66 → 2147.84] I've been very successful in selling that.
[2147.98 → 2153.28] It's definitely the other side of it when it's more just like you can't get a good grasp
[2153.28 → 2157.46] on it when it's not quantifiable in the terms of the business or in the product team.
[2157.46 → 2160.76] And quantifying it can be interesting, too, because there are some things that can be
[2160.76 → 2163.32] like, yeah, this is a huge thing that's going to bite us hard.
[2163.52 → 2168.78] But when you're trying to quantify exact terms for like, this may or may not be a problem
[2168.78 → 2173.80] depending on what we do, which oftentimes maybe the answer in that is, if it's not a
[2173.80 → 2175.24] problem, don't worry about it.
[2175.46 → 2177.18] I guess quantifying that debt is hard.
[2177.18 → 2182.42] Would it be fair to say that that is exactly the difference between legacy code and technical
[2182.42 → 2187.02] debt, where technical debt is something that needs to be repaid and that will potentially
[2187.02 → 2193.38] grow with time, whereas legacy code, as Dominic said, it might just sit there and work for
[2193.38 → 2195.02] years until anyone notices.
[2195.52 → 2200.22] I feel like legacy code is like the technical debt that we haven't paid down for so long
[2200.22 → 2202.24] that we kind of declare bankruptcy on it.
[2202.44 → 2205.72] Like, and the way that people think about legacy code, it's like that code that's just like,
[2205.72 → 2210.02] whenever you make that declaration of a Greenfield, you're like, okay, we're done with this.
[2210.14 → 2213.22] And since we haven't planned well for our debt in the first place, we haven't planned well
[2213.22 → 2217.38] for how we're going to replace that debt, because we also haven't quantified it for ourselves.
[2217.90 → 2224.04] So I think it starts off as we want to declare bankruptcy, but we don't actually know how to
[2224.04 → 2224.36] do that.
[2224.42 → 2229.06] And so we have this thing that kind of sits there and lives on continuously, but definitely
[2229.06 → 2231.34] open to other people's interpretations of that as well.
[2231.34 → 2239.86] To me, it boils down to once the company is near reaching a point where it will affect
[2239.86 → 2240.74] their bottom line.
[2241.08 → 2247.62] And when you're not able to find any engineers to work at your company, this is terrible.
[2247.86 → 2253.22] I mean, this is, you've already reached a certain point that you should never have passed,
[2253.32 → 2253.86] in my opinion.
[2253.86 → 2261.70] But before, yeah, before going there, the other point from just a minute ago, I think
[2261.70 → 2266.62] we might see a new kind of engineering type evolving.
[2266.62 → 2272.64] Because if you think about it, how much software are we creating these days compared to 25 years,
[2272.76 → 2273.52] 30 years ago?
[2273.68 → 2274.58] It's incredible.
[2274.90 → 2281.30] There will not be enough of us to maintain every single piece of software that is creating
[2281.30 → 2281.76] at the moment.
[2281.76 → 2285.62] I think we will see new kind of job evolved.
[2286.22 → 2287.92] And I'm not talking about AI here.
[2288.04 → 2289.96] And AI cannot maintain software.
[2290.38 → 2292.68] I'm looking at you, GitHub Copilot.
[2292.88 → 2300.00] But yeah, my point is, I mean, there should probably not be a difficult argument to be said
[2300.00 → 2305.14] about if a piece of software should be left as legacy like that, because it will impact
[2305.14 → 2307.20] the bottom line of the company at some point.
[2307.28 → 2311.14] And that should be the metric that every business people should understand.
[2311.14 → 2315.38] I think there was also a question about how we might start quantifying what this debt
[2315.38 → 2316.90] looks like for the business.
[2317.00 → 2319.28] And I think kind of using their own terms would be helpful here.
[2319.42 → 2323.46] Like businesses tend to have perfect, or at least the ones that survive for a long
[2323.46 → 2326.48] time, tend to have perfect risk management apparatuses.
[2326.48 → 2329.74] So they have perfect ways of talking about things probabilistically.
[2329.74 → 2335.10] And we as engineers hate talking about things in probabilistic terms or statistic terms, right?
[2335.14 → 2338.12] We're like, that will absolutely happen or that will never happen.
[2338.18 → 2339.68] And like, those are the only two options.
[2339.90 → 2344.20] But I've also found some success in like talking about things in a more probabilistic way.
[2344.34 → 2349.62] This can go as far as down as like story pointing, kind of changing it to be like, I have 70%
[2349.62 → 2351.54] confidence that this will take this amount of time.
[2351.54 → 2353.70] And just kind of bubbling that all the way up.
[2353.80 → 2358.48] And once we start talking in less of these absolute terms, I think it becomes easier for
[2358.48 → 2362.34] business people to commit for us to communicate with business people and give them something
[2362.34 → 2362.98] quantifiable.
[2362.98 → 2367.98] It's like, okay, well, if we don't do this work, there's an 80% chance we're going to
[2367.98 → 2371.48] run into a problem versus like, if we don't do this work, there's a 20% chance we're going
[2371.48 → 2372.32] to run into this problem.
[2372.48 → 2375.08] And then we can start doing those types of trade-offs.
[2375.12 → 2380.04] And then importantly, that also gives us something to track so we can improve there as well.
[2380.04 → 2383.82] Because once again, if we're trying to like figure out what our interest rates are, figure
[2383.82 → 2387.68] out like how much things are costing, it doesn't matter if we're just making up terms that don't
[2387.68 → 2391.58] actually come back to reality, that's going to degrade the trust from product and business.
[2391.58 → 2394.90] So we have to say, okay, we have an 80% probability of this thing happening.
[2395.40 → 2397.14] Okay, did it actually happen?
[2397.42 → 2399.72] And how many times did it actually wind up happening?
[2400.08 → 2403.06] Just going back and like tracking all of that and tracing all of that.
[2403.12 → 2406.28] So then every time the business asks, we can be like, here's, you know, the pages and
[2406.28 → 2409.92] pages and pages of like how we've discussed this and how we came to these
[2409.92 → 2411.66] numbers, how we came to this probability.
[2411.66 → 2415.98] And here's like the historical aspect of that and how much of the time, how much it has occurred
[2415.98 → 2420.58] historically so that we're actually able to like to give you some basis to believe us and
[2420.58 → 2422.14] kind of build that trust back up.
[2422.14 → 2425.22] And I think that's how you start making it more quantifiable for people.
[2425.72 → 2429.42] But I think to your point of that, like type of engineer that we need to develop, I think
[2429.42 → 2433.20] one of the types of engineers we do need to develop are people that are kind of focused
[2433.20 → 2437.60] on like going into code bases and doing this type of analysis and figuring out how to
[2437.60 → 2441.94] prioritize that debt that we have and come up with like debt consolidation and debt pay
[2441.94 → 2446.64] down plans and help us actually determine, hey, we want to declare bankruptcy and build
[2446.64 → 2447.24] a new thing.
[2447.64 → 2448.94] This is how we're going to do it.
[2449.00 → 2452.44] So we don't wind up with the old thing still being there haunting us forever.
[2452.94 → 2455.22] That is definitely an interesting thought.
[2455.34 → 2459.22] But it is like you mentioned, that is almost like a new type of engineer, a new type of position
[2459.22 → 2465.58] because coming up with all those percentages and whatnot, that's like an FTE almost.
[2465.76 → 2470.72] So it's not something that you can just kind of do on the side, you know, while you're doing
[2470.72 → 2471.52] your feature work.
[2471.76 → 2474.66] You need somebody who's focused and dedicated to that.
[2475.22 → 2475.94] Yeah, yeah, absolutely.
[2476.14 → 2480.90] It's like it's an it's a thing you have to be dedicated to doing and actually want to push
[2480.90 → 2482.90] your organization forward with doing it in the future.
[2483.26 → 2486.64] And it's like a whole process and a whole framework you have to develop as an engineering team.
[2486.64 → 2488.86] Like we're lacking this in most of our engineering organizations.
[2488.94 → 2494.00] Like I have not been to, I think, any companies that have had this type of robust way of talking
[2494.00 → 2497.70] about technical debt or legacy systems or even just feature work.
[2497.70 → 2500.16] Like most of the time, it's just like we got a bunch of story points.
[2500.22 → 2503.54] We got a bunch of sprints, and we're going to take a guess, and we're going to have retrospectives.
[2503.54 → 2507.68] But retrospectives are complaining about things that went wrong, not about did we actually
[2507.68 → 2509.12] meet what we said we were going to meet?
[2509.56 → 2513.00] So I think there's definitely a lot of area here that we could kind of build up something
[2513.00 → 2515.22] better for being able to discuss a lot of this stuff.
[2515.22 → 2519.52] Well, yeah, no wonder if that also calls out there's oftentimes so much ceremony involved
[2519.52 → 2523.76] that at least my experience has been a lot of engineers are like, well, this is kind of
[2523.76 → 2528.50] killing productive time because like, you know, if we spend a bunch of time pointing things
[2528.50 → 2533.82] when we do the work based on scrums, but no one's holding us accountable for our sprints
[2533.82 → 2538.06] and they actually end up devolving into something like business ends up wanting con bond anyway.
[2538.30 → 2540.48] So I'm doing all this ceremony work for nothing.
[2540.96 → 2543.28] Why do I want to add more ceremony onto that?
[2543.28 → 2548.44] Yeah, I think that's the kind of hole we've dug for ourselves in building a system where
[2548.44 → 2552.60] we are supposed to be getting these benefits, but then not actually doing the back half of
[2552.60 → 2553.12] that work, right?
[2553.24 → 2557.84] Not actually figuring out like, are these systems like is this form of agile we're doing?
[2557.92 → 2559.08] Are sprints working for us?
[2559.12 → 2560.40] Are story points working for us?
[2560.58 → 2564.76] Are we able to actually get the benefits out of them that we think we're getting?
[2564.76 → 2567.12] Or is this just kind of in reality?
[2567.24 → 2572.12] Yeah, like you're saying a ceremony, something we just do because we've done it, not because we have
[2572.12 → 2575.12] we're getting any intrinsic value out of it at the end of the day.
[2575.32 → 2579.26] I feel a whole go time episode coming on this exact topic.
[2580.38 → 2584.36] So I kind of I'm interested to hear a little bit more about we've talked about getting to that
[2584.36 → 2589.64] explosion point where it's falling apart, you know, having bugs every day, you know,
[2589.64 → 2594.36] making your on call engineers life hell, that is the point at which you're like, we need to do
[2594.36 → 2594.78] something.
[2595.12 → 2600.18] But going back to our original question, like, how do we stop legacy code creeping in as we're
[2600.18 → 2602.62] talking about accumulating tech debt, etc?
[2603.18 → 2608.86] What are some ways that we can stop getting to that kind of final point of explosion where
[2608.86 → 2610.44] everything's falling to pieces?
[2610.96 → 2616.48] Well, so I think one thing that like, if you want to keep from code becoming legacy, I think
[2616.48 → 2619.12] that testing is a helpful tool for it.
[2619.12 → 2621.44] It's by no means a salve it.
[2621.56 → 2627.28] But you know if you can define your actual problems that you're trying to solve and write
[2627.28 → 2633.20] tests that exercise those problems, that kind of it'll also help, you know, ensure that
[2633.20 → 2638.26] you've got discrete chunks doing those things rather than tangled mess all playing together.
[2638.62 → 2641.10] Sounds like you're advocating for test driven development.
[2642.30 → 2644.02] I just might be.
[2645.48 → 2646.56] It's not the cure all.
[2646.56 → 2649.88] There are oftentimes a lot of places where test driven development doesn't work, especially
[2649.88 → 2652.74] like lab settings or where you don't know what you're going to do.
[2653.12 → 2658.64] But it is a tool that helps in more than just like ensuring that your code functions correctly.
[2658.64 → 2665.58] In my experience, you have to invest in your infrastructure and your monitoring probably before you invest
[2665.58 → 2670.70] in your in actually rewriting your code in the sense that, for example, if your deployment
[2670.70 → 2676.38] pipeline takes hours for your changes to get deployed, you need to rewrite the deployment
[2676.38 → 2678.02] pipeline first, right?
[2678.44 → 2683.50] Add tests, add monitoring to make sure that you know what your system is doing, like what
[2683.50 → 2687.88] queries it's executing on the back end or what external calls it's making or whatever it is.
[2687.88 → 2693.82] And probably do that before you get to that explosion point that Angelica just mentioned.
[2694.06 → 2696.94] And then the explosion point will be a lot less painful.
[2697.36 → 2698.28] Yeah, I like that.
[2698.48 → 2705.56] I like that going small piece by piece and just being in a better way each week probably
[2705.56 → 2707.02] than you were last week.
[2707.18 → 2709.20] It feels like a great, great way to do that.
[2709.20 → 2714.30] And also probably less careful and dangerous, if I can say that.
[2714.56 → 2720.12] Because when you think about that, you know, rewriting as an entire software is, it is scary,
[2720.70 → 2721.14] for sure.
[2721.78 → 2725.84] I think I would say writing documentation or just comments, really.
[2726.28 → 2728.10] Like I think testing is definitely helpful.
[2728.10 → 2734.42] But I think if I were to be given a code base that has perfect tests, but no comments
[2734.42 → 2738.00] and documentation or a code base that has documentation comments, but no tests, I would
[2738.00 → 2738.86] definitely take the latter.
[2739.48 → 2744.06] Because good comments and documentation tell me the intent of what this thing is supposed
[2744.06 → 2747.06] to be doing, which then I can go write the test for myself.
[2747.32 → 2750.84] But when I only have tests and I don't have good documentation or comments, then it's like
[2750.84 → 2755.64] I have to assume that the tests were also written to do the thing that was intended to be done
[2755.64 → 2759.68] or kind of try and make, like derive from those tests what's supposed to be being handled
[2759.68 → 2760.02] here.
[2760.16 → 2763.64] But I think just going through and being like, okay, here's a function with this name.
[2763.70 → 2764.42] Here's a type with this name.
[2764.48 → 2765.64] Here's a method with this name.
[2765.98 → 2767.50] Does this do the thing I think it does?
[2767.52 → 2770.42] And then writing that down and making sure everybody has an understanding of that.
[2770.52 → 2775.28] Real great way to actually like, A, start exploring and understanding a legacy code base, but also
[2775.28 → 2778.00] helps prevent code bases from becoming legacy.
[2778.00 → 2782.48] Because then other people can catch the bugs in what you intended versus what's actually
[2782.48 → 2783.66] written in the code.
[2783.74 → 2785.90] So that clarity of intent is a good one.
[2786.14 → 2791.08] Because that's also like comments, documentation, and even just the coding style as well can go
[2791.08 → 2792.34] a long way towards that.
[2792.78 → 2797.64] Because naming is one of those things that's really hard and people tend to just eventually
[2797.64 → 2800.20] give up on or get frustrated and be like, ah, whatever.
[2800.36 → 2803.08] But it is worth that time to take care of your naming.
[2803.08 → 2807.66] Because if you can structure your code in a way where the code declares its intention,
[2808.00 → 2813.24] that's even better than having to say comments about saying what it's going to do, what it's
[2813.24 → 2813.96] intending to do.
[2814.42 → 2818.76] I think that's another strength of Go, in my opinion, due to the packages and whatnot,
[2818.92 → 2822.78] compared to other frameworks and language that I worked with in the past.
[2822.98 → 2829.66] So you kind of already have a small sense of what something is going to do in terms of
[2829.66 → 2831.44] a business case and whatnot.
[2831.44 → 2836.56] Because they are probably properly placed into the right packages.
[2836.56 → 2839.22] I'm wondering if people have any examples of...
[2839.22 → 2843.50] Because everything so far, it sounds like having good engineering standards and protocols
[2843.50 → 2847.88] for your team and organization is a big help in preventing legacy code.
[2848.02 → 2856.62] I'm curious if others have examples of maybe not just good documentation or good tests and
[2856.62 → 2860.66] stuff like that that could help in preventing legacy code.
[2860.66 → 2866.34] Because a lot of times that comes from the whole team that has to kind of agree upon a set of
[2866.34 → 2869.52] documentation and a kind of coding style.
[2870.20 → 2874.46] But if there's maybe something like you as an individual can kind of take upon yourself to
[2874.46 → 2879.44] kind of improve yourself as an engineer, totally not trying to talk about myself.
[2879.56 → 2884.58] I've definitely found that, at least for me, what the outcome of this is usually writing better
[2884.58 → 2886.12] documentation or tests or whatever.
[2886.12 → 2890.82] But I think just taking some extra time to stop and really think about what you're trying to do
[2890.82 → 2892.96] and what you're trying to implement doesn't have to be a ton of time.
[2893.04 → 2894.64] I'm not saying take hours and hours and hours.
[2894.80 → 2898.62] But just sitting there and looking at the thing and then thinking about the problem you're trying
[2898.62 → 2902.94] to solve for even just a few minutes longer than you would have before, I think can really
[2902.94 → 2905.42] help you perhaps design something a little better.
[2905.90 → 2908.28] And I think also just many iterations of things.
[2908.50 → 2913.24] So if you write something, and you budget your time and plan on being able to write it
[2913.24 → 2917.88] three, four or five times, that gives you the space to write it once, maybe quick and dirty
[2917.88 → 2921.52] and look at it and say, but is this the way that it should be written?
[2921.82 → 2924.58] I kind of get that feeling of if this is the right thing.
[2924.64 → 2929.90] So I think a lot of the times we wind up with legacy code or kind of the bad legacy code
[2929.90 → 2934.02] because we didn't go through enough iterations of thinking about something.
[2934.44 → 2938.94] And I think it can be very difficult to sit down and do that because we do have deadlines
[2938.94 → 2939.62] we're trying to hit.
[2939.62 → 2942.88] But I think that's one of the things that has definitely made me a better engineer is
[2942.88 → 2948.20] pushing back on myself and my team and saying, I'm going to take the extra few minutes here
[2948.20 → 2951.40] to think this through a little bit more because it doesn't feel right.
[2951.74 → 2957.04] And really just listening to your gut and developing your gut instinct over time to know, okay,
[2957.08 → 2957.84] I've written something.
[2957.94 → 2961.72] Okay, this is good versus I've written something and this is rough.
[2962.16 → 2966.16] And listening to that feeling inside you that's like, it's rough, but I don't know why.
[2966.28 → 2968.10] And then following that thread.
[2968.10 → 2971.38] And so I think a lot of times, once again, we kind of ignore that thread because we have
[2971.38 → 2971.90] things to do.
[2971.98 → 2974.60] We have features to develop, and we have something that works.
[2974.64 → 2975.62] So why are we going to follow the thread?
[2975.66 → 2978.82] But I think really just following that thread at the end of the day has definitely helped
[2978.82 → 2982.94] me write code bases that are much more resistant to legacy.
[2982.94 → 2986.44] Even when I'm working with a bunch of people that are just trying to move really fast,
[2986.48 → 2991.14] at least the parts that I'm working on are a little bit more immune to that bad legacy
[2991.14 → 2995.34] at the end of the day, which can help quite a lot because that kind of thing tends to be
[2995.34 → 2999.06] contagious and other people tend to pick up on it because they want, like they're working
[2999.06 → 3000.70] in the code that you wrote, and they're like, this is great.
[3000.76 → 3001.42] This is amazing.
[3001.78 → 3002.88] Like, I want my code.
[3002.96 → 3004.60] I want the whole code base to feel like this, right?
[3004.62 → 3006.22] It's very infectious at the end of the day.
[3006.72 → 3009.80] Do you think that pair programming could also do this effect?
[3010.26 → 3011.02] I think it can.
[3011.02 → 3015.48] If your environment is one that is, I'd say, opportune for pair programming, right?
[3015.54 → 3019.06] So like you're actually in person, you can actually sit at the same desk, you can actually
[3019.06 → 3021.80] work through things together at the same time.
[3021.80 → 3024.38] I think then, yeah, pair programming can be very helpful.
[3025.00 → 3028.54] I think also just group design, group thought processes, like whenever you can get like
[3028.54 → 3032.42] people in the same setting, and you have enough psychological safety where people can just
[3032.42 → 3034.78] like ask those questions that they might think are dumb.
[3035.14 → 3037.70] Because at the end of the day, you know, that thread you have is like the very much a
[3038.32 → 3041.12] I don't know what the problem is, but this doesn't feel right.
[3041.24 → 3044.74] So you have to be in an environment where you can express that and the people you're working
[3044.74 → 3047.68] with will help you work through that and have enough trust in you.
[3047.98 → 3050.88] So yes, I definitely think pair programming can be excellent for this.
[3050.88 → 3054.30] I think whiteboard sessions, if you can be in a space where you can do whiteboarding
[3054.30 → 3054.90] is great.
[3055.00 → 3058.70] But I think also just maybe not doing the pair programming part of programming, but just
[3058.70 → 3061.56] hopping on a call and talking through an idea with people.
[3061.78 → 3066.20] Maybe if we're a Google Doc, that also is, I think, equivalent and a very helpful way
[3066.20 → 3067.46] to kind of execute this.
[3068.16 → 3073.24] So we've talked a little bit about kind of you have this legacy thing and how do you make
[3073.24 → 3077.04] it so that you don't get to that final explosion point.
[3077.04 → 3084.28] But I'm interested to talk a little bit about when you, if you get that buy-in to rewrite
[3084.28 → 3091.22] a legacy code base or to change up a system and, you know, business for whatever reason
[3091.22 → 3092.88] decide they're having a great day.
[3093.00 → 3097.74] They're like, you have a year, you have two years, however long it takes, we need to rebuild
[3097.74 → 3099.10] this thing and make it better.
[3099.38 → 3104.34] When you are architecting that new solution, we are thinking through how do we build this
[3104.34 → 3110.90] new thing, how do you, from day one, from the whiteboarding session, build something that
[3110.90 → 3115.86] is going to avoid being legacy for as long as possible?
[3116.10 → 3116.46] I.e.
[3116.46 → 3120.42] is it always having microservices, making sure nothing is deeply coupled?
[3120.64 → 3123.32] Like what are some things, some questions to be asked?
[3123.80 → 3128.26] How do you go about designing a new system already with legacy in mind?
[3128.26 → 3133.70] I would say from the jump, understand what went wrong with your old system.
[3133.90 → 3140.10] I think people run for microservices or for Kafka or for some new flashy tech at the end
[3140.10 → 3140.48] of the day.
[3140.56 → 3143.46] Like they're like, oh, the problem was we weren't using microservice or something.
[3143.60 → 3148.22] But it's like, sit down and actually think like, why don't you like working this good?
[3148.30 → 3151.18] Why, why have we had to declare bankruptcy on this code base?
[3151.50 → 3156.76] A thing that I have done that has hilariously sometimes wound up with me not actually abandoning
[3156.76 → 3160.62] old code bases when I really wanted to, because like the problems I wanted to fix, I could
[3160.62 → 3161.92] just fix in that old code base.
[3161.96 → 3163.82] So why make a whole new one with all new problems?
[3164.24 → 3168.50] But I think that's definitely where I tend to start is like, what is it about this code
[3168.50 → 3172.14] base I'm working on now that's making it, so I want to build a new one?
[3172.70 → 3174.16] John, what do you think?
[3174.32 → 3177.22] I know this is something that I'm hoping you're thinking about.
[3178.80 → 3182.32] I don't know if I got too much on this one.
[3182.32 → 3188.18] But also off the record, for those who didn't see my cheeky smirk, John and Jeff, in fact,
[3188.24 → 3189.26] are both on my team.
[3189.48 → 3193.84] So when I make any cheeky comments in their direction, it is slightly more layered than
[3193.84 → 3196.66] other people who don't have that context may know.
[3197.16 → 3199.04] And I am their technical product manager.
[3199.52 → 3201.70] So that's also a context that you should know.
[3201.84 → 3205.12] I am speaking off the record as a business person.
[3205.56 → 3206.68] Undercover business person.
[3206.92 → 3207.62] I'm undercover.
[3207.78 → 3208.66] Secret gopher.
[3208.66 → 3210.28] Well, overt gopher.
[3210.44 → 3211.62] Secret product manager.
[3211.62 → 3218.72] I don't know, Jeff, like, what are some questions that you would hope if I was to go to you,
[3218.78 → 3222.92] Jeff, and be like, hey, Jeff, I'm thinking we should completely get rid of our current
[3222.92 → 3224.28] platform and rewrite it.
[3224.62 → 3228.22] What would be things that would pop to your head as things you would need to, you would
[3228.22 → 3233.40] want to be given time to think about before we kind of went, right, this is the new architecture.
[3233.40 → 3234.74] Let's go code.
[3234.74 → 3238.78] Yeah, I'm definitely following what Chris is saying.
[3238.78 → 3242.88] It's definitely you have to understand why you're trying to rewrite everything, right?
[3243.28 → 3247.54] You don't want to rewrite just for the sake of, oh, we have lots of issues with this codebase.
[3247.70 → 3251.74] Maybe we should just declare bankruptcy and start something new.
[3252.04 → 3255.06] It's definitely something I myself have been interested in.
[3255.06 → 3266.42] And I like for our team specifically, we're in the middle of kind of rewriting our two platforms and getting some historical context as to why we went that route.
[3266.66 → 3267.72] It would be interesting.
[3267.82 → 3268.50] But I do not.
[3268.62 → 3269.10] I don't know.
[3269.12 → 3273.74] I don't want to trigger John's PTSD too much because it looks like he's going through something.
[3274.00 → 3274.88] The question came up.
[3274.88 → 3275.52] Yeah.
[3276.52 → 3278.70] And I guess rewrites are tough.
[3278.84 → 3288.32] I feel like everybody at some point in their career needs to go through the let's just do a rewrite because of it and feel the pain and watch it fall flat on its face and waste like six months of their lives.
[3288.72 → 3289.68] Six months if you're lucky.
[3290.18 → 3290.50] Yeah.
[3290.70 → 3294.08] I'm like I've seen like entire years go down the drain.
[3294.08 → 3299.68] So having an understanding of the risk involved is huge.
[3300.28 → 3305.82] And you know if there are scenarios that do warrant it, but they're the exception rather than the rule.
[3305.82 → 3322.64] So am I right in assuming that if your product partner or the business came to you, I'm speaking to all of you here, and said, right, Chris, Misha, Dominic, I know you've been working with this 20 plus year in Dominic's case infrastructure.
[3322.64 → 3327.64] We're going to give you five years maximum to rewrite completely.
[3328.20 → 3334.16] Would there be cases in which you would then, after assessing, be like, no, actually we don't want to rewrite?
[3334.56 → 3337.96] Or would you always, if given the opportunity, want to rewrite?
[3338.06 → 3343.30] If given the buy-in, the money, the time to do it, would you always jump at that opportunity?
[3343.72 → 3350.04] I would only rewrite a software that works if the technology is not going to exist sooner.
[3350.24 → 3352.16] Take like old system like COBOL.
[3352.64 → 3359.46] In Quebec, there are a couple of companies that are still built on top of AS400 and COBOL and whatnot.
[3360.20 → 3362.94] I mean, there's no manpower anymore for that.
[3363.24 → 3364.00] So what do you do?
[3364.36 → 3365.36] You don't have a choice.
[3365.90 → 3375.78] But I would be extremely careful to rewrite the software not built from a long-time software from scratch.
[3375.78 → 3382.12] I would still try to see if there is something that can be done other than a complete rewrite.
[3382.36 → 3383.32] I'm in agreement there.
[3383.54 → 3390.96] I mean, I think when it comes to Greenfield projects or when it comes to rewriting legacy projects, just don't.
[3390.96 → 3393.44] Like, I think that's kind of the hard and fast rule most of the time.
[3393.44 → 3401.02] Because like, sure, there's usually like, usually we get to the point where we wanted to rewrite something when there's like, I would say 20 to 30% of it.
[3401.22 → 3406.02] Like maybe like a fifth to a third of the project is just obnoxious to work within.
[3406.02 → 3411.26] But there is still 70 to 80% of it that is doing things correctly.
[3411.48 → 3419.30] When you do a rewrite, you have to account for all those things that it does correctly and then replicate them and then also fix all those bugs.
[3419.50 → 3428.34] So it's always going to take way, way, way, way, way longer to rewrite the thing than it is to fix the problems in the thing that exists.
[3428.80 → 3430.88] So I think that's the thing that we have to account for.
[3430.88 → 3437.34] And if you go into it, and you do that math, and you say, yep, nope, we want to rewrite because we have X, Y, and Z reasons why.
[3437.74 → 3438.76] Sure, go ahead and go forth.
[3438.90 → 3445.74] But if it's just like, here are some individual pain points that I don't like about this system, and it's causing us to slow down some, let's rewrite the whole thing.
[3445.98 → 3446.70] Like, absolutely not.
[3446.78 → 3452.18] Like, you have to do like in-depth research and understanding of the project that you're dealing with before you can rewrite it.
[3452.22 → 3456.30] Like, you should actually be able to rewrite it before you start rewriting it.
[3456.30 → 3462.60] Which sounds like something that sounds super obvious when said, but is a thing that I have witnessed over and over and over again.
[3462.72 → 3464.88] It's not something that we do as engineers in general.
[3465.62 → 3470.54] Yeah, there's got to be some fundamental problem that requires like a complete Greenfield rewrite.
[3470.74 → 3473.48] It can't just be pain, which I think everyone's getting at.
[3473.74 → 3475.08] But also, it shouldn't come from product.
[3475.20 → 3481.24] It should be tech being like there's this technical roadblock that means, you know, we just cannot do this anymore.
[3481.24 → 3490.66] Because, you know, if you want to, if you've got like this legacy code base, and you just want to make it better and get there, there are ways that you can like to boil things out too.
[3490.82 → 3499.96] So, you know, if you can be like, well, we're going to move this small set of functionality to a new thing and piecemeal things out if you really want an entirely new code base versus improving it.
[3500.22 → 3504.38] But again, that should be, I think, tech driven rather than coming from product.
[3504.38 → 3514.32] If you can't come up with a way of conceivably actually retiring completely the thing that you're rewriting at the beginning of your rewrite, then you shouldn't do it.
[3514.46 → 3519.26] Because you're not going to be able to retire it if you don't already have a plan for how to do it.
[3519.70 → 3521.58] I think that's just like fact at this point.
[3521.66 → 3524.82] Like I've never seen anywhere that's been able to successfully retire something.
[3524.82 → 3540.76] Either it's like you've been able to successfully do it because you had a plan, or you were able to successfully do it because you just threw engineering bodies at the problem and basically said all other work halts until we finished this movement and this migration, which is incredibly difficult.
[3540.76 → 3554.92] And really requires buy-in of, you know, all the way up to the CTO level at the end of the day and probably the CEO level to really say, no, we're actually going to, no matter what, throw as many bodies as is required to get rid of this thing.
[3555.24 → 3558.12] Either you have to do that or you have to have a good plan from the beginning of how you're going to do it.
[3558.38 → 3559.48] And most of the time we don't have plans.
[3559.54 → 3560.90] So we're really saying the latter.
[3561.08 → 3569.06] And if you're not going to go spend that political capital to buy into that, then just don't rewrite the thing and really sit down and think about like what is frustrating you about this code base.
[3569.06 → 3577.34] Because I would say for most of the code bases, except for the ones, you know, once again, written maybe in COBOL or in some other ancient language that we don't want to deal with anymore.
[3577.50 → 3581.54] For the most part, especially if you're like, if it's a Go code base, and you're like, I want to rewrite this.
[3581.64 → 3582.52] Just stop.
[3582.78 → 3584.84] Just stop and be like, what's bothering me about this?
[3584.88 → 3586.02] And then go fix those things.
[3586.48 → 3594.92] That will take tremendously less time, and you will be happier with the results because now you will have the code base you wanted without the code base you didn't.
[3595.02 → 3599.00] You don't have this legacy code base that someone gets stuck maintaining until your new thing.
[3599.06 → 3604.20] It actually does what you promised it would do, which also will take a lot longer than you think it's going to take.
[3604.64 → 3605.86] The rewrite always takes longer.
[3605.94 → 3616.06] And if you can't shut down the new thing, the old thing until the rewrite is done, well, now someone has to keep fixing bugs and keep that old thing operable until the new thing is ready to go in full capacity.
[3616.56 → 3620.68] So if you really don't want to work on the old thing anymore, just fix the old thing in place.
[3620.68 → 3621.74] You know how it is.
[3621.78 → 3627.70] Even if everyone is agreeing to not touch the old thing anymore, there will always have new feature.
[3627.80 → 3631.74] There will always have bug fixes that you will need to replicate on the new system.
[3631.84 → 3632.94] It's extremely difficult.
[3633.38 → 3639.68] Don't assume that you will not have to add something new to the old system until the old system is completely off.
[3639.68 → 3651.48] So if your new thing is I'm going to go build something new, and it's going to take me two and a half years to build it, assume that you have to keep adding stuff to the old thing until that two and a half year mark hits, and you actually get to turn that old thing off.
[3651.86 → 3656.98] Moral of the story is Greenfield rewrites are not always the right direction to go.
[3656.98 → 3663.64] You need to sit, take some time, think it through, identify the core issues, and then get perfect.
[3663.90 → 3668.92] Nod to your wonderful series, Chris, at maintaining your software and your technology.
[3669.58 → 3677.10] Yeah, I think I have participated in one successful Greenfield rewrite in my 20-year career.
[3677.40 → 3678.32] And where was that, John?
[3678.52 → 3679.46] That is with us.
[3680.00 → 3681.40] And who was your product manager?
[3681.50 → 3682.46] That is with the Times.
[3682.46 → 3683.32] Yep, that is.
[3683.32 → 3692.24] I also have a side note about the term Greenfield, which I find hilarious because if you want to have an actual Greenfield, someone has to maintain that.
[3692.52 → 3694.54] Like if you go into nature, you don't find a lot of Greenfield.
[3694.58 → 3698.22] You find a lot of mud pits and stuff and a lot of overgrown grass and stuff.
[3698.28 → 3699.38] But a real Greenfield?
[3699.50 → 3701.90] Now you got to have like good lawn equipment, good agriculture.
[3702.34 → 3705.72] It takes a lot of work, a lot of maintenance to have a Greenfield.
[3705.88 → 3708.72] And people are just like, we're just going to start with a Greenfield.
[3708.72 → 3711.70] It's like you're going to start with something that's well-maintained and well-mannered.
[3711.70 → 3716.60] Okay, so it's like we should really call it like mud pit like development.
[3716.92 → 3718.32] And then people are probably...
[3718.32 → 3721.28] The grass is always greener on the other side.
[3721.40 → 3725.76] Because the other person actually maintains their lawn unlike you, right?
[3725.90 → 3728.62] Their grass is cleaner because they take care of it.
[3728.80 → 3735.34] You go over there, it might be green for a little bit, but then your old grass is going to be greener because that person maintains it now.
[3735.72 → 3736.82] So you're always going to want to...
[3736.82 → 3740.08] It's like, no, no, just learn how to maintain your grass and then you'll have a really green lawn.
[3740.44 → 3741.54] And also don't envy your neighbour.
[3741.54 → 3742.58] There are lots of lessons in here.
[3742.60 → 3744.28] I can take this analogy all day long.
[3744.44 → 3744.88] You know, this is...
[3744.88 → 3747.28] I feel like we're getting into the Canterbury Tales here.
[3747.84 → 3750.58] This is what happens when you have two writers on a podcast, Angelica.
[3750.78 → 3751.18] I know.
[3751.24 → 3752.24] We just feed off each other.
[3752.76 → 3755.42] Don't even get me started on Shakespeare in reference.
[3756.06 → 3757.38] We'll be here all night.
[3758.14 → 3760.54] To rewrite or not to rewrite, that is the question.
[3762.56 → 3764.28] Whether it is greener or the other side.
[3764.34 → 3765.18] Okay, I'm going to stop now.
[3765.70 → 3766.76] I could go on for days.
[3766.76 → 3767.24] Great.
[3767.24 → 3767.48] Great.
[3767.80 → 3769.26] Well, I...
[3769.26 → 3775.16] Regrettably, we have to move on to our next section because I want to hear your unpopular
[3775.16 → 3775.80] opinions.
[3775.80 → 3778.70] But it's been an absolute pleasure chatting about Legacy Code.
[3778.88 → 3781.42] And I'm sure myself and Chris have many an episode.
[3781.80 → 3783.96] As a follow-up, we now will like to do.
[3784.50 → 3787.24] This maintenance miniseries is becoming a maintenance series.
[3787.68 → 3788.68] It's just kind of expanding.
[3788.92 → 3789.20] Yes.
[3789.32 → 3793.30] I feel like we should stop calling it mini and just go with, this is a series.
[3793.86 → 3794.82] Maintenance is important.
[3795.44 → 3795.98] It's a thing.
[3796.30 → 3798.16] We should make its own little theme tune.
[3798.26 → 3799.08] I'm ready, Chris.
[3799.12 → 3800.28] Let's whip out the keyboard.
[3800.46 → 3802.90] I'll do the vocals, and I'll like to rap a little bit.
[3802.94 → 3803.42] It'll be great.
[3803.54 → 3804.08] A new jingle.
[3804.20 → 3805.24] We'll make that a note for Jared.
[3805.46 → 3807.36] Hey, Jared, we need a jingle for the maintenance series.
[3808.16 → 3808.40] Yeah.
[3808.84 → 3812.62] And on the topic of jingles, here's our unpopular opinion one.
[3812.94 → 3813.88] Smooth transition.
[3813.88 → 3819.08] Unpopular opinion.
[3819.34 → 3820.26] You want to.
[3820.30 → 3822.04] I actually think she'd probably leave.
[3825.16 → 3826.92] Unpopular opinion.
[3830.20 → 3837.62] So for all you lovelies who have not heard Go Time Unpopular Opinions before, this is
[3837.62 → 3843.34] where we ask our lovely guests and also Chris, if we have time, for an unpopular opinion.
[3843.34 → 3845.16] It does not need to be about Go.
[3845.28 → 3846.72] It does not need to be about technology.
[3846.90 → 3849.78] It can be about your aunt's favourite sock collection.
[3850.04 → 3851.40] It can be about China dolls.
[3851.68 → 3854.84] It can be about your view on the ethos and life.
[3855.38 → 3856.26] It can be on anything.
[3856.78 → 3862.28] First, I'm going to turn over to you, Jeff, for an unpopular opinion.
[3862.58 → 3867.96] Now, the goal of this is to come up with an opinion that you believe will be unpopular
[3867.96 → 3869.92] because we're going to post this opinion.
[3869.92 → 3874.22] I'm going to tweet about it, have our lovely Gopher community vote on it, and then we're
[3874.22 → 3876.78] going to tell you what percentage unpopular it was.
[3877.36 → 3879.00] And if it's popular, you have to come back.
[3879.26 → 3879.40] Yeah.
[3879.42 → 3883.74] And if it's popular, we're getting you back on Go Time to grill you again to get a better
[3883.74 → 3884.82] unpopular opinion.
[3885.26 → 3889.24] What if I just use that as a way to keep coming back on the show and just keep popular
[3889.24 → 3890.64] opinions because I like it here?
[3891.50 → 3892.84] We'll sniff you out.
[3893.16 → 3895.30] We're savvy individuals on this show.
[3895.30 → 3899.60] So I've been racking my brain with this ever since I agreed to be on Go Time.
[3899.86 → 3906.14] So I don't think I have anything earth-shattering like John's previous unpopular opinion.
[3906.32 → 3913.18] But what I came up with is I do not like any type of yogurt.
[3913.80 → 3917.48] I feel like that's a very popular snack that people like to eat.
[3917.80 → 3919.72] I just do not like yogurt at all.
[3919.90 → 3921.54] I have a story actually about that.
[3921.54 → 3927.52] So I bought Greek yogurt as a substitute for sour cream because I heard that's a good,
[3927.66 → 3929.42] healthy substitute.
[3929.96 → 3932.16] And it was my first time actually trying it.
[3932.42 → 3936.18] I opened up the container, and it just smelled really funky.
[3936.84 → 3941.50] And I told my college roommate at the time, did this go bad?
[3941.78 → 3943.18] And he came over and smelled it.
[3943.18 → 3944.58] He's like, no, that's just how it smells.
[3944.70 → 3946.70] I'm like, oh, definitely not for me.
[3946.70 → 3953.38] Wait, are we talking just like plain or are we talking like mix in with some granola and
[3953.38 → 3953.68] fruit?
[3953.78 → 3955.12] You also don't like it?
[3955.20 → 3955.64] Are we talking?
[3955.96 → 3956.94] I don't like any yogurt.
[3956.98 → 3958.58] I've never been like a yogurt person.
[3958.70 → 3959.70] Like Greek only?
[3960.06 → 3961.14] Are we talking about hope?
[3961.32 → 3962.66] Like drinkable yogurt?
[3963.06 → 3963.80] No yogurt.
[3963.98 → 3964.44] Oh my gosh.
[3964.44 → 3968.34] This is like an umbrella yogurt band in the Jeff Household.
[3968.80 → 3969.58] Basically, yes.
[3970.16 → 3972.62] Fascinatingly, I thought I always hated Greek yogurt.
[3972.84 → 3974.60] And for some reason, I now like Greek yogurt.
[3974.70 → 3975.48] I don't know why.
[3975.48 → 3978.50] So I'm kind of on the opposite end of the spectrum as you, dude.
[3979.04 → 3983.12] Well, Chris, you know, your taste buds do mature as you age.
[3987.46 → 3989.00] That's a good unpopular opinion.
[3989.46 → 3990.22] I love yogurt.
[3990.48 → 3991.30] I love Greek yogurt.
[3991.42 → 3993.70] Also, it's very good for your digestion, I'm told.
[3994.20 → 3997.62] And it has things called active things.
[3998.48 → 3999.48] But I also...
[3999.48 → 3999.50] Active.
[4000.14 → 4000.62] Active.
[4000.88 → 4001.40] What are they called?
[4001.66 → 4002.06] Probiotics.
[4002.28 → 4002.64] Probiotics?
[4003.06 → 4003.46] Yes.
[4003.46 → 4008.98] They have active probiotics that are apparently, I've been told by being brainwashed by the media,
[4009.12 → 4010.36] are very good for my digestion.
[4010.36 → 4013.94] But I have no scientific facts to back up that view.
[4014.36 → 4015.10] Purely from like...
[4015.88 → 4018.82] But I will, after this, Google it and check.
[4019.08 → 4024.06] But maybe as you get older, like Chris, you'll develop a taste.
[4024.06 → 4028.16] I get all my active probiotics from Dipole, if anyone else has had that.
[4028.56 → 4030.50] I don't know what I would describe it as.
[4030.56 → 4032.46] It's like a small little drink.
[4033.02 → 4034.70] It's not yogurt, as far as I know.
[4035.22 → 4039.64] But that's where I receive my active probiotics, since I don't have any yogurt.
[4039.64 → 4048.14] World's leading probiotic beverage created in Japan in 1935 and is now sold in over 40 countries.
[4048.56 → 4050.24] And it's not yogurt, so...
[4050.24 → 4051.06] It's not yogurt.
[4051.22 → 4055.12] I actually felt like it was, and I was going to Google it in the hopes that I would catch you out.
[4055.52 → 4056.50] But it's not.
[4056.66 → 4058.02] I've done my research, so...
[4058.02 → 4058.22] Oh.
[4059.22 → 4060.06] It won't catch me.
[4061.20 → 4063.02] Misha, unpopular opinion.
[4063.02 → 4064.22] Let's see.
[4064.44 → 4064.80] All right.
[4064.96 → 4074.76] So, my unpopular opinion that is not about Go is that CSS is a full-fledged programming language
[4074.76 → 4078.42] that will someday replace all other programming languages.
[4078.96 → 4085.16] Now I just need to figure out how to rewrite all of my backend microservices in CSS.
[4086.10 → 4088.10] I don't even know how to respond to that one.
[4088.62 → 4089.72] You broke my brain, I think.
[4089.72 → 4092.08] That will solve the legacy problem, for sure.
[4092.08 → 4094.24] Yeah, let's just write everything in CSS.
[4095.08 → 4099.88] Does it have to be CSS, or can I write it in Sass and then transpire it to CSS?
[4100.32 → 4101.04] Sass is fine.
[4101.62 → 4103.30] I'm getting snazzy with it here.
[4103.54 → 4109.62] Well, you can't do math in CSS now, so I can kind of see how you could create a virtual machine
[4109.62 → 4113.28] out of CSS, where, like, the byte code is CSS, and then...
[4113.28 → 4113.70] Oh, God.
[4113.86 → 4117.88] Now we're going to wind up with someone writing a C compiler that compiles C into CSS that can
[4117.88 → 4118.38] actually...
[4118.38 → 4119.22] Nah, this is terrible.
[4119.66 → 4120.08] This is...
[4120.08 → 4120.50] Oh, no.
[4120.56 → 4121.60] What have we started?
[4122.08 → 4126.18] I would be surprised if that was not unpopular.
[4126.82 → 4128.44] That's a very good unpopular opinion.
[4129.00 → 4129.36] Thank you.
[4130.04 → 4132.18] But I do now really want someone to do that.
[4132.40 → 4133.52] I want to see this compiler.
[4134.02 → 4134.90] It's a challenge.
[4135.86 → 4136.90] Dominic, over to you.
[4137.38 → 4141.70] In fact, Misha, you can do it, and then come back on the show, and we can talk about it.
[4141.78 → 4142.60] You just got to write it in Go.
[4142.66 → 4143.14] Sounds good.
[4143.42 → 4143.86] I'm ready.
[4144.46 → 4146.12] Wait, I swear that defeats the purpose.
[4146.12 → 4150.70] I swear, if you write it in Go, is it not then fully CSS?
[4151.04 → 4155.62] You can eventually bootstrap it so it's self-hosting on CSS, but you have to write it in some...
[4155.62 → 4156.20] Does that count?
[4156.34 → 4156.58] Yeah.
[4156.98 → 4159.06] Go was written in Go, but it didn't start off being written in Go.
[4159.14 → 4160.16] It started off being written in C.
[4160.58 → 4161.08] Oh, okay.
[4161.70 → 4165.86] Misha, in the definition for your unpopular opinion that you just came up with, does that
[4165.86 → 4166.16] count?
[4166.42 → 4166.74] Yes.
[4166.92 → 4167.62] Yeah, that would count.
[4167.84 → 4168.60] Can we do this?
[4168.94 → 4170.68] Okay, it's official now.
[4172.86 → 4174.00] Dominic, hit me.
[4174.18 → 4174.88] Unpopular opinion.
[4175.40 → 4179.58] Well, last time I thought it was the highest I could go, so let's see.
[4180.24 → 4181.88] Clearly not, because you're back.
[4182.02 → 4182.84] No, clearly not.
[4182.90 → 4183.16] Exactly.
[4183.78 → 4187.30] GitHub Copilot will do more harm than good, I think.
[4187.38 → 4188.58] Oh, that's not going to be unpopular.
[4189.08 → 4189.30] No?
[4189.48 → 4189.74] Yeah.
[4190.66 → 4193.30] It's more of an opinion that needs to be put out there.
[4193.38 → 4194.00] Yeah, I know.
[4194.00 → 4196.20] I was supposed to think about it.
[4196.20 → 4200.62] Maybe I will pass, because like I was saying at the beginning, I caught the COVID yesterday,
[4200.86 → 4206.14] so I was supposed to think about that yesterday, and to be frank, I did not.
[4206.34 → 4208.60] So yeah, let me pass on that.
[4208.84 → 4212.34] Shout out to Dominic for doing Go Time with active COVID.
[4212.60 → 4213.50] Yeah, it was rough.
[4214.18 → 4214.80] Real trooper.
[4215.12 → 4216.36] Yeah, thank you so much.
[4216.60 → 4218.32] Yeah, that's my popular opinion, in fact.
[4219.40 → 4220.90] Doing things with the COVID.
[4221.44 → 4222.12] Powering through.
[4222.12 → 4230.24] All right, John, you are the person who holds one of the most unpopular Go Time opinions ever.
[4231.10 → 4236.32] Shameless plug to a previous Go Time episode where we go through all of our unpopular opinions of the year.
[4236.60 → 4239.84] I don't know exactly what number it is, but if you DM me, I'll let you know.
[4239.88 → 4240.68] It's a great episode.
[4240.68 → 4244.64] Where John said that he hates chocolate.
[4245.16 → 4247.30] So I'm ready for this next one.
[4247.36 → 4248.26] It better be a good one.
[4248.34 → 4250.30] My expectations are sky-high.
[4250.56 → 4255.38] I'm going to swing for the fences on this one and say that I think adding generics to Go was a mistake.
[4255.88 → 4256.36] Ooh.
[4256.36 → 4266.16] So while there are use cases where generics actually are very handy, I think overall I have seen more harm done with generics than in general.
[4266.16 → 4273.48] Because I think that it encourages developers to try and deduplicate things that are not necessarily the same.
[4274.14 → 4285.54] And when you're trying to reuse for the sake of reusability and accomplish different tasks with code, you oftentimes end up with code that is much more of a tangled mess and harder to maintain and harder to understand.
[4285.54 → 4289.20] And I think the generics encourage that.
[4289.68 → 4293.32] I think like everything in life, balance will return at some point.
[4293.72 → 4296.12] But in my opinion, it will be good.
[4296.22 → 4301.40] Just think about all the loops that we are doing that we will not be forced to do.
[4301.56 → 4305.96] Like, you know, removing an item from a slice, for example, or I don't know.
[4305.96 → 4312.86] So I think for the next six months, it will be like very dirty everywhere.
[4313.16 → 4314.24] Everyone will try that.
[4314.36 → 4316.06] But I'm not sure.
[4316.32 → 4317.76] I disagree with that, respectfully.
[4318.70 → 4319.18] Totally.
[4319.30 → 4323.78] And I totally get you where like those loops and whatnot, where there are cases where it totally makes sense.
[4324.08 → 4329.30] But I think that having those cases is a lesser sin from the abuse of generics that's going to follow.
[4329.84 → 4330.10] Yeah.
[4330.24 → 4331.02] Yeah, I see the point.
[4331.44 → 4334.20] I hope we will see a balance at some point because...
[4334.20 → 4336.28] It's going to be channels and good routines all over again.
[4336.40 → 4338.82] People are just going to sprinkle that stuff all over their code bases.
[4339.68 → 4340.00] Yep.
[4340.28 → 4341.78] Oh, can I use a channel here?
[4341.84 → 4343.12] I'll use a channel because I can't.
[4343.14 → 4344.40] Oh, now I need to use seven channels?
[4344.50 → 4346.38] I'll use all seven of those channels just because I can.
[4346.42 → 4347.60] I'll sprinkle good routines everywhere.
[4347.78 → 4349.50] It's just going to be that all over again.
[4349.64 → 4349.82] Yep.
[4350.14 → 4353.90] Need I return to my first app ever that I think, Chris, you've seen,
[4353.90 → 4360.28] where I literally ended up having like 317 channels individually written,
[4360.88 → 4363.34] partly because I didn't know you could send stuff to one channel,
[4363.34 → 4364.92] but also because I just had fun.
[4365.08 → 4366.40] I was like, oh my God, I could create all this...
[4366.40 → 4368.42] And then I had like pointers to channels.
[4368.80 → 4369.46] Oh boy.
[4369.66 → 4372.16] It was all fun, but clearly not the right approach.
[4372.36 → 4373.12] Difficult to maintain.
[4373.30 → 4373.54] Oh yeah.
[4373.60 → 4376.26] And then I added like go routines onto every single one.
[4376.90 → 4378.54] So that was fun.
[4381.10 → 4383.32] Yeah, Chris, I know you loved it when I showed you.
[4383.52 → 4385.10] Like, look how pretty it is.
[4385.30 → 4385.60] No.
[4388.22 → 4391.60] Chris, do you have an unpopular opinion to finish us up with?
[4391.60 → 4393.66] I have many an unpopular opinion.
[4393.66 → 4396.92] I think I hold one of those most like coveted unpopular opinions.
[4396.92 → 4397.88] You absolutely do.
[4397.88 → 4398.58] Unpopular opinions.
[4399.58 → 4400.04] Okay.
[4400.16 → 4402.04] So this one is tech related, not Go related.
[4402.56 → 4410.28] But I think that we should kill off all C-like languages and C-derived languages
[4410.28 → 4414.28] and get rid of the von Neumann architecture and move on as an industry.
[4414.88 → 4416.70] Do you have a beat more as to why?
[4417.24 → 4417.94] Yes, actually.
[4417.94 → 4421.98] So when the von Neumann architecture was created, like we were still using discrete parts.
[4422.08 → 4426.32] But even when we made the first transition in the 70s to transistors, we had on the order
[4426.32 → 4429.48] of thousands of transistors operating at kilohertz.
[4429.74 → 4434.54] And now, as of a couple of weeks ago, you can buy a chip, buy a computer on the market that
[4434.54 → 4439.98] has over 100 billion transistors operating at several gigahertz each.
[4439.98 → 4445.44] So we've had many, many, many, many, many orders of magnitude along two different dimensions
[4445.44 → 4447.74] of improvement in our hardware capabilities.
[4447.74 → 4453.28] But we still use the same fundamental architecture that is the same fundamental bottlenecks attached
[4453.28 → 4459.92] to it, which ironically is turning our systems, our chips into distributed systems just to keep
[4459.92 → 4461.82] pace with the improvements that we've made.
[4462.12 → 4465.96] And I think all of this extra work and all of this strife is caused by the fact that we're
[4465.96 → 4470.00] still using this architecture, and the reason we still use it is because, well, it's the
[4470.00 → 4471.32] architecture of C at the end of the day.
[4471.40 → 4476.86] C very much programs in this mentality that recognizes the von Neumann architecture as being
[4476.86 → 4477.06] there.
[4477.14 → 4482.24] It's very difficult to write truly parallel or good parallel code or concurrent code in
[4482.24 → 4482.48] C.
[4483.04 → 4489.28] So jettison the von Neumann architecture and along with it, C and C-like languages, which
[4489.28 → 4491.22] unfortunately includes Go as of right now.
[4491.22 → 4495.78] Because while you can write some good concurrent code in Go, it's still pretty difficult.
[4496.20 → 4500.48] You know, we want languages that look more like Erlang, or at least have the same underpinnings
[4500.48 → 4505.16] of things like Erlang at the end of the day to really capture the capabilities of the silicon
[4505.16 → 4505.74] that we have.
[4505.96 → 4507.22] Because it is, you know, quite incredible.
[4507.34 → 4511.76] I mean, Apple did just come out with a chip that has 115 billion transistors on it.
[4512.08 → 4516.80] And it's like, yeah, we can't really utilize all of those if we're using them in our CPU
[4516.80 → 4517.56] based architecture.
[4517.56 → 4521.64] So more stuff that looks like graphics cards, too, because they're very good at capturing
[4521.64 → 4524.66] this idea of parallelizable and concurrent workloads.
[4524.92 → 4527.76] But yes, no more C, no more von Neumann.
[4528.16 → 4528.98] Get rid of it.
[4529.12 → 4530.10] Move on as an industry.
[4530.38 → 4530.88] Let's get better.
[4530.98 → 4534.74] Let's stop wasting so many CPU cycles waiting for our main memory to get back to us.
[4535.00 → 4539.10] Yeah, that may be an unpopular one, especially if you add in that like very blasé, like,
[4539.14 → 4540.50] oh, you know, Go is included.
[4541.02 → 4544.76] I mean, it's like, it's all C, like, you know, Java, Go, Rust, C, C++.
[4544.76 → 4548.68] You know, all those popular imperative languages, just goodbye.
[4549.16 → 4549.92] Time for something new.
[4550.16 → 4551.98] Let's rewrite Linux and Erlang.
[4552.30 → 4552.84] It will be fun.
[4553.28 → 4556.14] So on that fine point, let's get rid of Go.
[4556.64 → 4558.82] Regrettably, that is the end of our episode.
[4559.38 → 4560.12] Thank you all.
[4560.18 → 4562.22] It was an absolute pleasure having you on.
[4562.28 → 4565.24] And I hope we'll have you all back very soon.
[4565.36 → 4567.46] Subject, how unpopular your opinions are.
[4567.46 → 4573.80] That is Go Time for this week.
[4574.12 → 4575.30] Thanks for hanging with us.
[4575.74 → 4581.34] Don't forget to follow GoTimeFM on Twitter so you can get in on our unpopular opinion polls.
[4581.78 → 4585.94] And if this is your first time listening, subscribe now at GoTime.fm.
[4586.32 → 4592.10] There you'll also find lists of recommended episodes, listener favourites, and a request form
[4592.10 → 4595.06] so you can let us know what you want to hear about on the pod.
[4595.06 → 4598.34] Special thanks to Vastly for being our CDN partner.
[4598.54 → 4601.00] Our episodes reach you fast because of Vastly.
[4601.28 → 4603.26] And to Break master Cylinder for the fresh beats.
[4603.64 → 4605.16] Finally, thank you for listening.
[4605.36 → 4606.06] We appreciate you.
[4606.54 → 4609.50] Next week, yours truly is guest hosting.
[4609.82 → 4615.36] I've got Ian Lop shire and Chris Brando answering my newbie Go Curious questions.
[4615.86 → 4616.64] Stay tuned.
[4616.78 → 4619.80] We'll have that one ready for your next time on Go Time.
[4619.80 → 4620.10] Go Time.
[4620.10 → 4620.14] Go Time.
[4620.14 → 4622.14] Go Time.
[4622.14 → 4622.58] Go Time.
[4622.58 → 4623.14] Go Time.
[4623.14 → 4623.58] Go Time.
[4625.06 → 4626.12] Go Time.
[4631.40 → 4635.96] Go Time.
[4638.10 → 4638.68] Go Time.
[4638.74 → 4650.66] Go Time.
[4650.66 → 4650.74] Go Time.
[4650.74 → 4650.84] Go Time.
[4651.38 → 4653.40] Go Time.
