[0.00 --> 10.48]  This week on The Change Law, we're sharing the most popular episode of Go Time from last
[10.48 --> 10.80]  year.
[11.12 --> 16.08]  This is episode 196, and we believe it's the most popular episode because it's all
[16.08 --> 19.38]  about building actually maintainable software and what goes into that.
[19.72 --> 23.64]  Chris Brando is joined by Johnny Borsico, Ian Lopshire, and Sam Boyer.
[23.90 --> 28.14]  There is lots of hot takes, disagreements, and of course, unpopular opinions.
[28.14 --> 32.34]  This is part two of a three-part mini-series led by Chris on maintenance.
[32.78 --> 36.70]  Make sure you check out Go Time, 195 and 202, and continue the series.
[37.26 --> 37.84]  And guess what?
[37.92 --> 42.06]  Go Time records live, so join in on the conversation on Tuesdays at 3 p.m.
[42.08 --> 42.78]  U.S. Eastern.
[43.12 --> 48.84]  Hang in the Go Time FM channel on Go for Slack, and watch and listen live at youtube.com slash
[48.84 --> 49.30]  changelog.
[49.82 --> 53.40]  A big, big thanks to our friends and partners at Fastly and Fly.io.
[53.78 --> 57.38]  Our friends at Fastly, make sure our pods are fast to download a little bit because, hey,
[57.38 --> 58.92]  Fastly is fast globally.
[59.40 --> 60.84]  Learn more at Fastly.com.
[61.20 --> 64.66]  And our friends at Fly, let you run your app and your database close to your users all
[64.66 --> 65.20]  over the world.
[65.48 --> 67.26]  It's like a CDM, but for your entire application.
[67.78 --> 69.70]  Try it free at fly.io.
[77.28 --> 82.04]  This episode is brought to you by Influx Data, the creators of InfluxDB.
[82.04 --> 88.54]  InfluxDB is the open source time series platform where developers build IoT, analytics, and cloud
[88.54 --> 89.04]  applications.
[89.66 --> 92.56]  And I'm here with Paul Dix, founder and CTO of Influx Data.
[92.96 --> 97.78]  Paul, all the open source software that Influx Data creates is either MIT licensed or Apache
[97.78 --> 98.38]  2 licensed.
[98.88 --> 100.74]  These are very permissive licenses.
[101.36 --> 103.44]  Why are you all for permissive licensing?
[103.44 --> 108.42]  The thing is, we like permissive licenses because we want people to do whatever they want.
[108.72 --> 112.90]  Because of these three reasons, freedom, evolution, and impact.
[113.36 --> 117.56]  Freedom means being able to create a business and create your livelihood off of this code,
[117.82 --> 119.30]  regardless of what you want to do with it.
[119.50 --> 121.86]  You can modify it, look at it, do whatever.
[122.38 --> 127.80]  Evolution means you can create a derivative project and rename it, put it out there in
[127.80 --> 132.56]  the world, either as an open source project under a permissive license, or you can relicense
[132.56 --> 136.84]  it under a copy left license, or you can create a business off of that.
[137.14 --> 138.78]  And then the last bit is impact.
[139.14 --> 145.00]  We believe more people benefit from open source when that code is permissively licensed, despite
[145.00 --> 147.76]  the changes that the other infrastructure vendors are making.
[148.30 --> 152.12]  Influx remains permissively licensed open source with commercial software.
[152.54 --> 152.90]  Well said.
[153.00 --> 153.42]  Thank you, Paul.
[153.50 --> 156.10]  That truly summarizes the spirit of open source.
[156.10 --> 162.04]  So if you want the option to have freedom, the option to have evolution and impact, use
[162.04 --> 164.76]  InfluxDB for your time series application needs.
[164.90 --> 169.02]  Check it out and start for free, of course, at influxdata.com slash changelog.
[169.12 --> 172.70]  Again, influxdata.com slash changelog.
[186.10 --> 186.72]  Let's do it.
[187.38 --> 188.36]  It's go time.
[189.64 --> 191.10]  Welcome to go time.
[191.44 --> 197.18]  This week, we're going to be doing part two of our multi-part mini series on maintenance
[197.18 --> 199.80]  and the importance of maintaining our software.
[199.80 --> 206.00]  As I said in the first episode in this series, you know, we talk a lot in this industry about
[206.00 --> 211.10]  innovation, about greenfield projects, about prototyping and hackathons, but rarely do we
[211.10 --> 215.44]  talk about the longer side of things when it comes to software, the maintenance and the
[215.44 --> 217.18]  long-term prospects of it.
[217.68 --> 224.06]  This week's episode is going to be focused on building actually maintainable software and
[224.06 --> 225.20]  what goes into that.
[225.82 --> 229.42]  And this week, I am joined by Sam Boyer.
[229.88 --> 230.40]  Hi, Sam.
[230.44 --> 231.04]  How are you doing?
[231.40 --> 231.96]  I'm lovely.
[232.02 --> 232.32]  How are you?
[232.62 --> 233.02]  Great.
[233.34 --> 237.54]  And to give you a little introduction of Sam, Sam is a principal engineer at Grafana Labs,
[237.54 --> 241.44]  where he just switched teams to be responsible for Grafana's Go backend.
[242.18 --> 246.84]  The team is nominally in charge of around 250,000 lines of code.
[247.26 --> 249.22]  Yeah, that's a huge amount of code right there.
[250.00 --> 253.94]  Sam thinks a lot about code evolution and quality, usually under the umbrella of package
[253.94 --> 258.54]  management, an area he's been working in for the better part of a decade, as I'm sure many
[258.54 --> 260.24]  of our listeners are well aware of.
[260.76 --> 263.30]  And I'm also joined today by Ian Lopshire.
[263.50 --> 264.32]  How are you today, Ian?
[264.62 --> 265.26]  I'm doing great.
[265.62 --> 265.86]  Yeah.
[265.94 --> 270.64]  And to give you guys an introduction of Ian, Ian is a senior engineer at TimeHop, where
[270.64 --> 273.96]  he's responsible for keeping TimeHop's Go backend in working order.
[274.62 --> 279.46]  TimeHop integrates with multiple social media platforms to surface millions of user photos
[279.46 --> 280.58]  and posts each day.
[280.88 --> 282.40]  It's like your own little day in history.
[282.40 --> 282.68]  Yeah.
[282.68 --> 283.08]  Yeah.
[283.16 --> 287.02]  I remember TimeHop from back in the day and, you know, still got, you guys are still going
[287.02 --> 287.40]  strong.
[287.48 --> 287.92]  It seems.
[288.38 --> 288.76]  We are.
[289.06 --> 292.20]  And I'm also joined by my fellow host, Johnny Bersico.
[292.46 --> 293.60]  How are you doing today, Johnny?
[294.12 --> 294.66]  Not too bad.
[294.72 --> 295.18]  Not too bad.
[295.24 --> 296.26]  I bring hot takes.
[296.58 --> 296.70]  So.
[297.46 --> 297.86]  Yeah.
[298.26 --> 300.58]  I'm ready for some good Johnny hot takes.
[301.00 --> 304.84]  I thought of a couple unpopular opinions, but if you have extra despair, I mean, maybe I'll just
[304.84 --> 306.92]  lean on you for those.
[308.66 --> 309.64]  Plenty to go around.
[310.04 --> 310.38]  Excellent.
[310.38 --> 313.08]  There's going to be a lot of unpopular opinions in this episode, I feel.
[315.72 --> 316.48]  All right.
[316.74 --> 321.38]  So with that, let's get into talking about maintenance and how to build maintainable software.
[322.00 --> 327.66]  And I want to start with thinking about, you know, how do we build actually maintainable
[327.66 --> 330.28]  code for new code bases, right?
[330.32 --> 334.18]  Because there's, you know, some maintenance you do for old code bases, but then you have,
[334.26 --> 335.14]  you know, new code bases.
[335.14 --> 338.28]  And we always start with these great ideas when we make like a new one.
[338.82 --> 342.80]  But rarely are we thinking about, you know, what's it like when that code base actually
[342.80 --> 343.66]  goes to production?
[344.02 --> 346.04]  What are the steps to get toward it?
[346.42 --> 349.24]  So I guess we can start with, let's start with you, Johnny.
[349.70 --> 353.72]  What are the things that we should be thinking about when we, you know, build a new code base
[353.72 --> 357.88]  and we're aiming to get it to production for more of like, I guess, a maintenance standpoint?
[358.64 --> 359.40]  Well, that's the thing.
[359.46 --> 364.68]  You don't know if whatever it is that you're working on is going to be around for the long
[364.68 --> 365.26]  haul, right?
[365.26 --> 371.58]  So we have this assumption that all the pieces of code that we write sort of is worth sort
[371.58 --> 375.36]  of getting all production ready and everything else like all the time.
[375.36 --> 376.74]  And that's really not true.
[376.86 --> 379.88]  So as you say, like a lot of times you start out with basically doing some prototyping,
[379.96 --> 380.46]  some R&D.
[380.78 --> 386.60]  It is an unfortunate fact that a lot of times, right, due to business pressures or whatever
[386.60 --> 392.16]  timelines, sometimes most of the time manufactured, you know, timeframes for things that the stuff
[392.16 --> 394.84]  you have ends up going into production.
[394.84 --> 398.78]  And you're like, oh man, like we really didn't do all the due diligence necessary or the all
[398.78 --> 402.68]  the prep, all the operationalization, all the production readiness stuff that should have
[402.68 --> 403.48]  gone into this, right?
[403.48 --> 404.68]  It was just a prototype.
[404.94 --> 407.98]  Now, you know, management wants it to be deployed and whatever it is.
[408.06 --> 409.76]  So you're playing catch up now, right?
[409.98 --> 415.46]  But in the ideal scenario, right, you figure out basically what is it that I'm building,
[415.54 --> 416.80]  that I'm tasked with building, right?
[417.10 --> 420.86]  And making sure that everybody understands this is the scope of this work.
[420.96 --> 424.00]  This is really, it's meant to show you something, right?
[424.30 --> 426.14]  Maybe you're trying to determine product market fit.
[426.42 --> 427.68]  Is this thing real?
[427.74 --> 428.38]  Does it have legs?
[428.44 --> 429.34]  Whatever the case may be.
[429.62 --> 433.14]  But with the intention of actually making it ready for production.
[433.14 --> 435.58]  These are very separate steps, right?
[435.62 --> 438.78]  When you're exploring and when you're making something production ready, these are very,
[438.88 --> 439.78]  very different things, right?
[440.12 --> 445.04]  Again, it's unfortunate that a lot of times, you know, the play, the toy ends up going to
[445.04 --> 445.46]  production.
[445.96 --> 450.14]  But yeah, you kind of have to basically ask yourself, start out by saying, hey, do I have
[450.14 --> 452.12]  an agreement with whoever's asking me to build this piece of software?
[452.28 --> 455.58]  Do I have an agreement on where this is actually needs to go, right?
[455.72 --> 459.16]  Is it a toy that I throw away at the end or is this it, right?
[459.16 --> 461.44]  Because there's going to be very different approaches to these things.
[461.84 --> 461.96]  Yeah.
[462.10 --> 462.26]  Yeah.
[462.32 --> 465.36]  I think, and that gives me like a lot to think about, man.
[465.40 --> 467.02]  You just started unwinding.
[467.42 --> 469.18]  I told you, man, I bring, I bring the heat.
[469.28 --> 469.90]  I told you.
[470.04 --> 472.72]  I mean, I've got, you know, opinions about this stuff.
[472.96 --> 474.52]  That's the start of the diverging path though, right?
[474.56 --> 478.08]  Like it's, we can all imagine the best of intentions for making things maintainable over
[478.08 --> 478.62]  the longterm.
[478.80 --> 480.28]  But those pressures exist at all times.
[480.44 --> 482.20]  And certainly I don't disagree at all.
[482.30 --> 486.20]  You know, that, that initial stage, you don't know if the thing that you're making is trash
[486.20 --> 486.56]  or not.
[486.84 --> 489.32]  And the only way to figure out if it's trash is get it to the point where it actually
[489.32 --> 491.78]  runs and see if it's not trash.
[491.98 --> 494.82]  And the faster you get to that point, the faster you figure out whether it's actually
[494.82 --> 495.80]  worth putting the effort in.
[496.10 --> 497.68]  So my only point is to say, no, I agree.
[497.68 --> 503.84]  But I think that the point there is that the diverging tensions between like a sort
[503.84 --> 506.82]  of high quality or maintainable code base.
[507.00 --> 510.40]  And I have a thing to like talk about whether we think those are different things later.
[510.70 --> 513.02]  But I think those paths start diverging right from the beginning.
[513.14 --> 514.36]  Like is it high quality, maintainable code base?
[514.54 --> 515.22]  Or does it do the job?
[516.12 --> 517.44]  And resources are finite.
[517.54 --> 518.02]  Time is finite.
[518.28 --> 519.46]  And I think it's a good point.
[519.54 --> 520.66]  There's pressures that are there right from the beginning.
[521.08 --> 523.58]  Ian, do you have anything you want to say?
[523.98 --> 525.32]  Yeah, it's kind of along those same lines.
[525.32 --> 530.24]  I think an important piece of the beginning there is, does this piece of software actually,
[530.82 --> 533.48]  is this something that we can actually solve with software?
[533.92 --> 537.58]  I've been in the situation where, you know, you got to build a piece of software to automate
[537.58 --> 538.54]  something or do something.
[538.84 --> 542.32]  And it turns out the edge cases and the error cases are just too numerous.
[542.62 --> 546.20]  And it's more of a headache to fix those than it is to actually just manually do the work.
[546.58 --> 551.10]  So I think at the very beginning, you got to kind of start with a actual solvable problem.
[551.10 --> 551.62]  Okay.
[552.02 --> 557.66]  But let's say that we've already figured out that, you know, we have some code, right?
[557.68 --> 558.90]  We wrote some code, we prototyped.
[558.98 --> 563.78]  We're like, okay, this idea is solid and we can go forward with it.
[564.26 --> 568.66]  I guess like at that point, what should we be doing or should we be thinking about to
[568.66 --> 570.18]  like make that code base more maintainable?
[570.24 --> 575.56]  Or are we saying that perhaps we shouldn't be focused on maintenance in these earlier times
[575.56 --> 577.42]  and we should be trying to focus on it later?
[577.42 --> 580.92]  I guess like how do we start to strike that balance there?
[581.52 --> 585.04]  Because I know like a lot of us, you know, go into companies and, you know, whether it's
[585.04 --> 588.76]  moving from monolith to microservices or just, you know, you have microservices and you're
[588.76 --> 589.66]  starting a new one.
[589.82 --> 592.62]  And there's always, as Johnny and Sammy said, there's this hope.
[592.80 --> 595.80]  There's just like green field, this whole new path you can go.
[595.88 --> 597.26]  And there's all these different directions.
[597.84 --> 602.62]  And there always is that trade-off of time, as you also brought up, and constraints.
[602.62 --> 606.08]  But at some point we have to say, there's obviously a trade-off at some point where if
[606.08 --> 609.28]  you don't maintain, then you're going to have to wind up throwing this whole thing out.
[609.40 --> 612.00]  And then all of that time you put into it is now gone.
[612.34 --> 615.50]  And you have to, you know, start all over again and pay those costs all over again.
[616.00 --> 622.90]  So is there a point or is there, I guess, some signal or some way of knowing at what point
[622.90 --> 627.12]  you should start focusing a little bit more on maintenance and stop trying to maybe optimize
[627.12 --> 630.80]  for those time or whatever it is, you know, product features, whatnot.
[630.80 --> 635.24]  I think we need a definition from what maintainable is at that stage, right?
[635.24 --> 640.84]  Because I think if I'm speaking from a developer, like the person writing the code standpoint,
[641.20 --> 645.74]  my idea of maintenance is perhaps different from, say, an operator's viewpoint of maintenance,
[645.92 --> 646.08]  right?
[646.62 --> 648.86]  And again, there's a subtle difference.
[649.06 --> 653.28]  Well, in a lot of cases, not so subtle between sort of operating, right, a piece of software
[653.28 --> 656.98]  that you and other teammates have written, right?
[656.98 --> 660.88]  And making that easy to operate, easy to maintain from an operational standpoint.
[661.08 --> 664.42]  And then there's the aspect of, okay, I'm working on a problem domain.
[664.84 --> 666.26]  I don't know everything there is to know.
[666.26 --> 667.78]  I don't know what business is going to throw at me next.
[668.30 --> 670.00]  I need to structure my code, right?
[670.06 --> 673.88]  And perhaps follow some best practices and design patterns, whatever the case may be,
[674.20 --> 674.36]  right?
[674.36 --> 676.48]  To be able to extend the software easily, right?
[676.76 --> 682.12]  So different kind of views on maintenance and maintainability of long term.
[682.12 --> 688.24]  And interestingly enough, different companies, depending on their stage of sort of technology
[688.24 --> 689.66]  sort of maturity, right?
[689.76 --> 692.26]  Or engineering discipline and maturity, right?
[692.32 --> 696.32]  Are going to have, they're going to be in different sort of positions on that spectrum,
[696.60 --> 696.78]  right?
[696.92 --> 701.10]  So I think really, you can't look at sort of maintainability in a vacuum on its own.
[701.18 --> 704.68]  You kind of have to say, well, for us, what does maintainability mean, right?
[704.70 --> 706.06]  And that's going to vary from team to team.
[706.38 --> 708.16]  I feel like Sam has something he wants to say about that.
[708.16 --> 708.66]  Mm-hmm.
[710.92 --> 711.98]  I'm not sure I can.
[712.58 --> 716.46]  Well, the problem is actually, I think I hung on to something you said earlier, Johnny,
[716.52 --> 719.22]  about the difference between operating and maintaining.
[719.82 --> 723.16]  Certainly there are differences, but I don't know.
[723.24 --> 726.72]  I've had a few thoughts swirling around in my head about what it means to do maintenance.
[726.76 --> 730.24]  Because I do agree, like we need a definition for what that actually is, right?
[730.72 --> 737.70]  My sense is that there are two fundamental ways in which we can think about maintenance.
[737.70 --> 742.38]  One is fixing bugs, and the other is adding features.
[743.12 --> 745.74]  And those two things have tensions involved, right?
[745.86 --> 750.82]  But what I was thinking about when you were talking was how I think there actually is a
[750.82 --> 756.86]  really important commonality between operational characteristics and development time characteristics.
[757.42 --> 759.04]  And to me, that's failure locality.
[759.04 --> 768.56]  It's the idea that I want the computers to tell me as closely as possible how the thing is failing so that I can fix it.
[768.68 --> 771.38]  And that is true whether I am writing tests.
[771.52 --> 775.40]  Because to me, a good test is something where when it fails, I know right where to look.
[775.64 --> 776.62]  I know right what to fix.
[776.88 --> 781.20]  And that's not something that I need to rebuild a ton of context for where somebody else can come in and do, right?
[781.20 --> 790.68]  Similarly, when something is failing in one of its operational characteristics, I want to know as closely as possible where to look, where to go.
[790.88 --> 800.56]  So I think there's a common principle there in terms of the way that we should be approaching making – and that's mostly on the bug fixing side, right?
[800.56 --> 802.30]  Mostly, I think, on the bug fixing side.
[802.78 --> 826.78]  But maybe where the paths meet in the woods of the two approaches, or the bug fixing and then the feature adding, is the extent to which your tests and your telemetry and whatever systems you have set up for consuming your operational information are able to tell you when the thing that you were adding over here broke some stuff over there, right?
[826.78 --> 828.36]  And quickly, guys, do the same thing.
[828.40 --> 833.20]  Because, I mean, ultimately, what we're talking about here is, like, does the software continue to be correct or not?
[833.36 --> 834.18]  And how can you tell?
[834.70 --> 838.76]  So I apologize, though, because, like I said, that it kind of took off like a thing you said at the beginning.
[838.76 --> 842.54]  And I feel like I missed the tail end of it, which is why I was thinking about biting my tongue.
[842.64 --> 844.74]  But then Chris called on me, so I'm sorry.
[847.14 --> 847.42]  Ian?
[847.86 --> 848.98]  Ian's got some thoughts, too.
[849.36 --> 850.26]  He looks deep in thought.
[850.78 --> 855.30]  Yeah, so this idea of, like, locality, I think is important for maintainability as well.
[855.30 --> 864.44]  Like, I feel like if we minimize the amount of, like, unrelated changes that have to happen to make a change, a desirable change that is maintainable, right?
[864.66 --> 869.40]  So because maintainability, right, has all these facets, right?
[869.48 --> 872.76]  Perhaps we can sort of come at it from the other way around.
[872.88 --> 875.54]  What would we call unmaintainable software, right?
[876.00 --> 877.02]  How do we define that?
[877.12 --> 883.44]  I think that's something we perhaps all might agree on as these are the sets of things, right,
[883.44 --> 885.78]  in practice that make a piece of software unmaintainable.
[885.90 --> 890.74]  And I'm sure over the course of our individual careers, we've probably seen a few, right?
[891.16 --> 893.88]  I mean, you can start with anything you can lint for, right?
[894.20 --> 898.04]  Especially in Go, where there isn't a lot of disagreement about, like, what should go into linters.
[898.74 --> 901.12]  That's a lot more common in other languages.
[901.12 --> 908.54]  But, I mean, if you can lint for it, then, yeah, like, you know, put basic docs on your functions and your exported members.
[909.14 --> 914.18]  You know, maybe don't have insanely short variable names for literally everything that you do.
[914.64 --> 916.40]  There's the minimum bar, right?
[916.96 --> 924.74]  And I feel like we can almost just, you know, put a checkmark on the list and say, okay, if you can lint for it, like, maybe just, you know, do that from the start.
[924.74 --> 929.76]  And actually, I would loop back to the early question, right, even in a new code base, like, throw the linters in as soon as you can.
[930.14 --> 933.86]  Maybe you can ignore and just write some dumb, like, you know, one-liners for your function docs, right?
[933.90 --> 935.22]  But, like, don't make things harder for yourself.
[935.42 --> 941.02]  Just start from that and get yourself a nice little, like, foundational baseline going of the basics.
[941.58 --> 950.64]  But I used words to identify the easy part so somebody else can talk about the other things that might be harder to agree on about what makes unmaintainable code.
[950.68 --> 951.68]  Because I think it's a great question.
[951.68 --> 954.82]  I think coming at this from a negative angle is a good way to do this.
[955.48 --> 959.80]  Ian, do you have ideas on what makes unmaintainable code?
[960.60 --> 961.30]  I mean, I do.
[961.80 --> 965.10]  I think fundamentally untestable code is unmaintainable.
[965.42 --> 968.48]  If you can't know if it's correct, you can't make changes to it.
[968.84 --> 977.86]  So some things that make things fundamentally untestable, like heavy use of globals, that sort of thing, I think is probably the biggest thing that sticks out to me.
[977.86 --> 991.26]  I feel like there's something you said earlier, Ian, that I would classify as making software unmaintainable, which is, like, if we don't know what we're building, I feel like that fundamentally makes it very difficult for us to write software that we can maintain.
[991.26 --> 993.18]  I feel like if you don't know the scope, right?
[993.22 --> 1003.56]  If you haven't sat down and written a scope and written a design, then the resulting software, it might do what you as an individual thought the software should do.
[1003.70 --> 1008.54]  But that might be slightly different from what other individuals thought the software would do.
[1008.54 --> 1012.76]  And I think that that's one of those, like, longer term maintainability problems.
[1013.22 --> 1026.08]  If people have different concepts of what a specific code base or a specific package or a specific function even is supposed to be doing, then when multiple people work on it over time, it kind of atrophies and it kind of falls apart.
[1026.18 --> 1033.70]  And I think we've all seen these functions that live in code bases that have just been hijacked to do something completely different from what the original author intended.
[1034.32 --> 1035.86]  And you're like, how did that happen?
[1035.92 --> 1038.12]  And I feel like that's upstream of scoping problem.
[1038.12 --> 1038.66]  That's upstream.
[1038.80 --> 1042.20]  Like, we didn't properly define what this thing was supposed to do.
[1042.62 --> 1047.18]  And I feel like that fits in that category of, like, gnarly things that Sam was just like, you did the easy stuff.
[1047.26 --> 1048.06]  This is a harder thing.
[1049.00 --> 1050.26]  Well, no, I agree.
[1050.32 --> 1057.18]  But I want to ask a maybe annoying question there, which is, so Ian said code is fundamentally untestable, right?
[1057.86 --> 1064.34]  How is code that's untestable different from code where the intent is not clear?
[1064.90 --> 1065.36]  It's not.
[1066.20 --> 1067.38]  Behavior is not defined.
[1067.38 --> 1070.00]  What if you're testing the wrong thing?
[1070.60 --> 1070.74]  Right.
[1071.00 --> 1071.24]  Right.
[1071.44 --> 1072.88]  Like, you have tests, right?
[1073.04 --> 1073.64]  You test that.
[1073.80 --> 1074.20]  Right.
[1074.36 --> 1077.40]  The assumptions you made, though wrong, pass your test.
[1077.78 --> 1078.00]  Right.
[1078.20 --> 1085.04]  I feel like there's that cyclical testing that people tend to get into with unit testing as well, where they test at, like, the wrong level.
[1085.42 --> 1086.90]  And it's like, well, that thing is tested.
[1087.04 --> 1087.72]  You've tested it.
[1087.78 --> 1091.28]  It does the thing that you thought it was supposed to do.
[1091.28 --> 1095.48]  But, like, the thing you thought you were supposed to do is not the thing that you actually wanted to do.
[1095.54 --> 1097.26]  And I think that's the difference there as well.
[1097.26 --> 1108.08]  Like, you as an individual, if you write the function and then you write the test, then obviously, I mean, I hope that the tests that you wrote have now confirmed that that function does what you want.
[1108.08 --> 1115.54]  But if, you know, you, Sam, and I have two completely different ideas about what this function is supposed to be doing, we can both write tests and those tests can both pass.
[1115.86 --> 1118.90]  But that doesn't solve that initial problem of, like, scoping.
[1119.44 --> 1122.42]  Like, this function itself is still not well defined.
[1122.52 --> 1125.52]  So I do think that they are divergent paths.
[1125.54 --> 1126.96]  Or maybe, like, one encapsulates the other.
[1127.08 --> 1127.22]  Right?
[1127.22 --> 1132.66]  Like, if you have untestable code, then you've, like, most definitely probably scoped it wrong.
[1132.80 --> 1136.30]  But scoping it wrong doesn't necessarily mean that it's untestable.
[1136.86 --> 1136.98]  Yeah.
[1137.10 --> 1138.96]  No, that certainly is the case.
[1139.04 --> 1139.32]  I agree.
[1139.38 --> 1140.68]  I do think there's a difference between these things.
[1140.68 --> 1159.58]  But I think that it's worth asking that question because having a clear sense of, like, what it is that this code's supposed to do, the boundaries within which it's supposed to exist, is astonishingly important to, like, actually trying to maintain a code, especially as a code base gets larger.
[1159.80 --> 1162.16]  You know, should this function go in this package?
[1162.38 --> 1164.64]  Should it be a new package?
[1165.04 --> 1165.36]  Why?
[1165.74 --> 1168.20]  What's the logic by which we are grouping these things?
[1168.20 --> 1174.30]  Is there some, like, broader theme that we can use to decide that this is how we actually organize our code?
[1174.40 --> 1176.44]  This is where we ought to look for something.
[1176.60 --> 1184.48]  Like, these, as your code base grows larger, you can't just kind of, you know, oomph your way through, like, finding things inside of it.
[1184.54 --> 1197.48]  Like, having larger patterns for why code gets grouped in different ways, having larger structural patterns, whether those are something, like, formally defined by, like, type-checkable interface contracts, less formally defined in terms of, like, naming convention patterns,
[1197.48 --> 1203.58]  or really informally defined, but still very important in terms of, like, general patterns and responsibilities,
[1203.58 --> 1209.46]  and, like, we're going to put a collection of packages under a single tree that are service-y shaped or something like that, right?
[1209.46 --> 1221.16]  As your code base gets larger, and take note for that intro bit where I'm currently thinking about and mostly learning a 250,000 line code base at the moment,
[1221.38 --> 1233.12]  having patterns and structures like this, I think, do an enormous amount to orienting the maintainer who inevitably, given a large enough code base,
[1233.12 --> 1238.32]  you just have to assume that every maintainer is basically naive at some level about what's in some code.
[1238.32 --> 1246.60]  They do a lot to orient the user, the maintainer, towards intent, which is the first step towards being able to figure out what should be tested,
[1247.50 --> 1253.74]  which is the next step on the path to figuring out whether the thing does what it's supposed to do after, you know, in the first place.
[1254.06 --> 1257.88]  So you don't wake up one day and you have an unmaintainable code base, right?
[1257.98 --> 1258.18]  No.
[1258.46 --> 1260.48]  Going with the same, like, terminology that we established.
[1260.48 --> 1262.18]  So you gradually get there.
[1262.18 --> 1267.72]  So we've already sort of created or at least identified the nuance between correct code and testable code.
[1267.82 --> 1269.28]  The two are not necessarily the same thing, right?
[1269.54 --> 1278.34]  But I think, to me, you start to gradually get towards an unmaintainable code as you start to sort of let your technical debt,
[1278.42 --> 1280.18]  which is, that's not a bad word.
[1280.24 --> 1281.56]  That's not a dirty set of words, right?
[1281.62 --> 1285.62]  Technical debt is absolutely, I think personally, I think that's necessary, right?
[1285.62 --> 1288.52]  When you're evolving software, as long as you pay it back.
[1288.80 --> 1291.38]  If you don't have debt, you haven't done anything great.
[1291.96 --> 1292.74]  Exactly, exactly.
[1293.24 --> 1298.74]  Yeah, literally, you need, technical debt is part of the currency, right, that you have, right?
[1298.74 --> 1304.12]  To trade for things, you know, basically to pay an upfront cost for a certain feature, right?
[1304.12 --> 1309.64]  And then to come back and actually, you know, like fix the things that really make it maintainable in the long term, right?
[1309.74 --> 1313.36]  So when you don't address your technical debt, you start to creep towards that unmaintainability.
[1313.36 --> 1318.18]  So we're to the point where it's like, oh, man, like I'm looking at a code base, which has been around for a couple of years.
[1318.64 --> 1323.28]  And there's three different ways to do the same thing with a slightly different parameterization.
[1323.64 --> 1328.20]  You know, this one accepts, you know, like an empty interface here because somebody wanted to make it super flexible,
[1328.20 --> 1330.62]  but they didn't understand enough about the problem domain.
[1330.62 --> 1333.02]  Now you end up having to create another one with more specific.
[1333.16 --> 1340.12]  You can see those like sprinkles of just different people trying to solve the same problem in different ways and not basically saying,
[1340.12 --> 1343.68]  OK, we've done enough sort of damage, right?
[1343.76 --> 1346.74]  You know, we have an understanding of what it is that this thing's supposed to do now.
[1346.82 --> 1354.42]  Can we just take a minute, take a step back, take all the different ways we would do the same thing, refactor, right, for maintainability, right?
[1354.44 --> 1359.52]  As opposed to somebody coming, you know, next week and says, oh, now I need a slightly different version of this thing.
[1359.58 --> 1361.58]  Now you have four ways of doing the same thing, right?
[1361.58 --> 1366.06]  So you start that march towards, you know, increasingly unmaintainable software.
[1366.50 --> 1368.68]  But is any software truly unmaintainable?
[1368.76 --> 1372.76]  That would mean that you can never do anything else to it unless you're basically on a code freeze.
[1372.90 --> 1374.96]  That's it. It's done. You're never touching it again.
[1375.50 --> 1380.24]  Like as long as software is delivering value for the business, you have to maintain it, right?
[1380.28 --> 1385.96]  So if you don't do the things you're supposed to be doing, right, towards making something maintainable for the long term,
[1386.18 --> 1391.08]  you're going to increasingly creep towards that unmaintainable, like increasingly unmaintainable state.
[1391.58 --> 1417.62]  So this episode is brought to you by our friends at Square.
[1417.62 --> 1419.94]  Develop on the platform that sellers trust.
[1420.26 --> 1424.00]  Support Square sellers by building apps for today's business needs.
[1424.32 --> 1429.60]  As a Square app partner, you can reach millions of business owners searching for trusted software solutions.
[1430.20 --> 1434.00]  As a Square solutions partner, you can get hired by sellers on the Square platform,
[1434.38 --> 1437.26]  find new clients and build apps that meet their needs.
[1437.64 --> 1438.46]  Square loves developers.
[1438.66 --> 1442.00]  They work hard to enable you to launch fast with their developer tools.
[1442.00 --> 1449.18]  You get a full sandbox environment, an interactive API explorer, live event monitoring,
[1449.60 --> 1455.30]  backend SDKs for PHP, Ruby, Java, .NET, Python, and Node.
[1455.64 --> 1460.00]  You get secure payment SDKs for iOS, Android, React Native, and Flutter.
[1460.26 --> 1460.90]  You get it all.
[1461.28 --> 1464.14]  Learn more and get started at changelog.com slash Square.
[1464.14 --> 1467.80]  Again, changelog.com slash Square.
[1467.80 --> 1496.06]  Have you guys heard the rant about the word performance and how it's a made up word that doesn't mean anything?
[1496.06 --> 1498.68]  Like, is the software performant?
[1498.96 --> 1500.36]  What does that mean?
[1500.38 --> 1500.88]  What does that mean?
[1501.20 --> 1503.20]  How fast is performance?
[1503.98 --> 1508.72]  So I ask it here because I think maintainable is the same kind of problem, right?
[1508.98 --> 1510.94]  The point is we're on a sliding scale here.
[1511.32 --> 1517.46]  And whether or not you would call something maintainable or unmaintainable, I mean, realistically, that's a question of how bad your day has been.
[1517.46 --> 1528.78]  But if you're being a little bit more high-minded, it's like, what is the appetite of the organization that I am in for allocating a bunch of time for being able to make changes to this thing?
[1528.78 --> 1534.28]  So it is fundamentally contextual to, like, the environment that you are operating in.
[1534.30 --> 1543.88]  In the same way that, like, is the code performant is actually a question about what the appetite of the organization is for, like, accepting latency, whatever, along this particular path.
[1543.88 --> 1557.28]  There is no objective standard here for it, which is why, as you say, Johnny, it's this risk of the creep towards you can continually add things that might make it more unmaintainable, but maybe would never necessarily reach there.
[1557.28 --> 1568.24]  Or exogenous factors might change, like how many things are relying on that code that will suddenly have it be in an unmaintainable state, whereas before it seemed fine.
[1568.24 --> 1580.94]  And I think you have a good call out there, because I think the business is also on the hook for ensuring that there is enough space, time, resources for keeping the software maintainable.
[1580.94 --> 1601.50]  Because if you don't, and as I'm sure we've all either, you know, experienced or heard, like, if you're never making room for improving your code base, not adding new features, not fixing bugs alone, but really improving the code base to make it easier to work in, eventually your shipment of features is going to come to a crawl.
[1601.50 --> 1609.50]  And everybody's, like, scratching their heads wondering, why does it take, like, three, four sprints of two weeks of pop to add just this one feature?
[1610.04 --> 1614.34]  Everybody ends up scratching their heads asking that same question, and the answer is always the same thing.
[1614.44 --> 1619.60]  Well, we keep wanting to go back and fix these other things, but we never get the time.
[1619.76 --> 1622.48]  You know, there's always a demand for ship this next thing.
[1622.56 --> 1624.82]  This is important, but this is whatever it is, right?
[1624.82 --> 1630.22]  Basically, the business is not caring about what it takes, behind the scenes.
[1630.28 --> 1631.50]  There's things that they can't see, right?
[1631.54 --> 1632.26]  We're the engineers.
[1632.38 --> 1638.26]  We need to make the case for the time, the resources, the space, right, to improve the code base.
[1638.40 --> 1640.88]  If we don't do that, the business is not going to do that for us automatically.
[1641.26 --> 1643.08]  To them, it's like, hey, can I get this?
[1643.14 --> 1643.74]  And you deliver it.
[1643.98 --> 1644.66]  Here's what's next.
[1644.72 --> 1645.26]  Can I get this?
[1645.34 --> 1649.10]  Because they have pressures from customers, from stakeholders, right?
[1649.20 --> 1652.24]  As long as you keep giving them stuff, they're going to keep asking for more stuff, right?
[1652.24 --> 1658.02]  If you don't fight for the space and time to make your code base maintainable, right?
[1658.10 --> 1661.10]  Easier to keep adding things to, that's how you get in trouble.
[1661.50 --> 1662.76]  We had a discussion recently.
[1663.44 --> 1668.04]  We have a thing, Grafana, called gardening week, which I had not heard referred to this
[1668.04 --> 1668.42]  way before.
[1668.50 --> 1669.52]  It's my first time hearing the term.
[1670.02 --> 1673.34]  But, you know, after we do a release, we have like a gardening week, basically.
[1673.96 --> 1677.86]  And there was a discussion about like, well, should we have a gardening week?
[1677.98 --> 1679.34]  Like, is it a bad thing that we have gardening week?
[1679.46 --> 1681.68]  Wouldn't it be great if we didn't like need to have a gardening week?
[1682.42 --> 1685.22]  And my sense is that there are three.
[1685.42 --> 1688.00]  I'm going to try to pre-count the number of universes and then get it wrong.
[1688.08 --> 1690.66]  So I'm going to say there's three universes and then get it wrong.
[1691.00 --> 1695.08]  There is the universe where you don't have a gardening week, but you need one.
[1695.94 --> 1698.16]  You don't have a gardening week and you don't need one.
[1698.76 --> 1702.38]  And you have a gardening week and you need one.
[1702.54 --> 1706.94]  I don't think the like have it and not need it is a super realistic one.
[1706.98 --> 1707.40]  But there you go.
[1707.44 --> 1708.96]  There's my missed count.
[1709.06 --> 1709.98]  There's three, but maybe there's four.
[1709.98 --> 1716.90]  Anyway, point is, like, I had this initial reaction to seeing the existence of gardening week and and seeing, oh, like, come on.
[1716.94 --> 1718.84]  Can't we kind of do that as we go along?
[1719.00 --> 1725.76]  And then I realized, no, like, actually, I would so much rather be in a world where there is two words.
[1725.86 --> 1731.12]  Gardening week that has an understood meaning and understood reason why it's valuable to the business and why it's valuable to the people involved.
[1731.12 --> 1740.98]  And that we have that time in that space allocated in a sort of structured way because it is way better than being in the world where you need a gardening week and don't have it.
[1741.44 --> 1743.20]  I would love to be in a world where we don't need one at all.
[1743.46 --> 1744.58]  I'm not sure that's ever realistic.
[1744.58 --> 1752.54]  But having phrases like this, I think, help to maybe make it less of a fight all the time to have to advocate for this.
[1752.64 --> 1762.10]  But if you don't have one and you need one, you need to advocate because, yeah, otherwise it's not going to you're just going to keep on trying to push that Sisyphean rock up the hill and struggling.
[1762.10 --> 1767.78]  And the business will only see things slowing down and not really understand why.
[1768.28 --> 1777.16]  And I guess I have a sort of question off of that, but I want to preface it with something like the code bases I've worked on that have been unmaintainable.
[1777.26 --> 1780.74]  It feels like unmaintainable where it's like this thing should take a week.
[1780.80 --> 1783.20]  And instead it's taking four months to do.
[1783.60 --> 1784.20]  This is miserable.
[1784.44 --> 1785.26]  I hate everything.
[1785.56 --> 1785.76]  Right.
[1785.76 --> 1790.04]  Whenever I've wound up in one of those situations, it's always like it's not like one big thing.
[1790.04 --> 1790.90]  That's the problem.
[1790.90 --> 1794.92]  It's always like thousands of little tiny things.
[1795.10 --> 1799.38]  And then you look at those in isolation and everybody's like, well, that's a little thing.
[1799.48 --> 1801.52]  So is it really worth it to go and fix it?
[1801.64 --> 1803.10]  There's all this other stuff we need to do.
[1803.30 --> 1810.74]  Like it's always like we know that it's death by a thousand paper cuts, but we never want to like stop any one of those paper cuts from happening.
[1811.52 --> 1815.96]  So the question I have based on that is like, is gardening week enough?
[1815.96 --> 1821.08]  Or should we actually be pushing further and saying we want like a gardening team?
[1821.08 --> 1826.84]  Because I think there's this myth that exists in our industry that like people wouldn't like working on said team.
[1826.90 --> 1837.28]  It'd be like this miserable thing where like, oh, well, that's the team of people that doesn't get to do the fun stuff of building features and building new products and doing all of that.
[1837.56 --> 1839.68]  But I think and I have some friends that are like this.
[1839.74 --> 1841.84]  I was like, no, just give them give them code base.
[1841.94 --> 1846.14]  Let them go and just like clean up some certain parts of code bases.
[1846.14 --> 1847.46]  Scratch that itch.
[1847.86 --> 1853.56]  Yeah, like the garbage men, like every city, like imagine what our cities would be like if there were no garbage people, right?
[1853.64 --> 1856.34]  Not garbage people, but like trash collectors.
[1856.50 --> 1858.30]  That's a better, better.
[1859.52 --> 1861.30]  I mean, it'd be good to have a city that has.
[1861.36 --> 1862.68]  I didn't hear it till you said it.
[1863.68 --> 1866.94]  I mean, it would be a wonderful world if we didn't have garbage people.
[1870.28 --> 1872.74]  Imagine a world that we didn't have trash collectors, right?
[1872.80 --> 1874.50]  Like our streets would be disgusting.
[1874.50 --> 1876.40]  Our cities would be awful.
[1876.98 --> 1882.06]  But like there's no one there that's saying like and there's there's some people that are trash collectors and that they love their life.
[1882.34 --> 1886.50]  Like they are so happy with like what their job is and how they live their life.
[1886.88 --> 1891.22]  And I think there's like a significant portion of software engineers that want to do that sort of thing.
[1891.26 --> 1893.62]  They're like, let me like take this part of the code base.
[1893.66 --> 1896.28]  It has that function that has like 15 parameters.
[1896.28 --> 1900.18]  And that's just like I'm going to think about it and refactor it and just make it better.
[1900.54 --> 1903.58]  So the next time someone comes through, it's like not as bad to be in that space.
[1903.58 --> 1909.62]  But I'm wondering if that's something that we should be pushing for or if there's like another version of that.
[1909.76 --> 1917.32]  Or is it just like, well, let's just start with gardening weeks and then we can figure out what we should be doing after we have this at like most of the organizations.
[1917.32 --> 1920.56]  I don't think that's something that needs to be optioned personally.
[1920.86 --> 1921.00]  Right.
[1921.04 --> 1927.90]  If I'm running a team, if I'm an engineering manager, unless the team is gelling so well that I don't need to formalize the process.
[1928.16 --> 1928.32]  Right.
[1928.34 --> 1929.88]  I'm just making it a formalized process.
[1929.88 --> 1930.28]  Right.
[1930.32 --> 1932.58]  I'm just making it just like, you know, going on call.
[1932.96 --> 1934.28]  There's a rotation schedule.
[1934.50 --> 1936.06]  You go in that squad.
[1936.20 --> 1937.68]  You know, other people call it health squad.
[1937.80 --> 1937.98]  Right.
[1938.04 --> 1939.64]  We can call it gardeners if you want.
[1940.02 --> 1940.20]  Right.
[1940.20 --> 1942.74]  So but you do your time in there.
[1942.74 --> 1942.98]  Right.
[1943.04 --> 1947.30]  And and I say that I don't want it to sound like it's a punishment or chore.
[1947.46 --> 1953.30]  I think every engineer needs to understand what it's like to work on greenfield projects.
[1953.30 --> 1961.48]  And they also need to understand how you maintain existing software that's been around for a while that is making money for the business and paying your salary.
[1961.70 --> 1962.20]  Right.
[1962.24 --> 1964.84]  You need to understand how that software works.
[1964.84 --> 1969.02]  And because when we need to change it, maintain it.
[1969.20 --> 1969.34]  Right.
[1969.68 --> 1972.28]  Add features, fix security holes or whatever it is.
[1972.56 --> 1972.74]  Right.
[1972.92 --> 1975.46]  Everybody should be somewhat well versed.
[1975.46 --> 1975.72]  Right.
[1975.78 --> 1982.16]  And that software and obviously different people, depending on tenure and seniority, whatever, they're going to have a much better.
[1982.16 --> 1987.80]  They're going to have time at sort of holding the whole problem domain in their heads, depending on how large your code base is and all these other factors.
[1987.80 --> 1991.84]  But at least everybody's towards working towards a shared common understanding.
[1991.84 --> 1992.26]  Right.
[1992.62 --> 1998.00]  Of the software so that we can all keep this thing alive that's paying our salaries.
[1998.00 --> 1998.26]  Right.
[1998.26 --> 2001.18]  So I think this is something that every engineer.
[2001.54 --> 2001.70]  Right.
[2002.08 --> 2007.40]  Should feel responsible for basically contributing to the health.
[2007.50 --> 2007.92]  Right.
[2007.92 --> 2012.46]  Of a piece of code base or however many you have in case of microservices or whatever.
[2013.10 --> 2018.16]  I would question, though, if that's actually a good idea, because here's where I'm coming.
[2018.54 --> 2020.36]  Like, I always pull analogies from like other things.
[2020.40 --> 2024.34]  I gave a talk at GopherCon where I basically talked about like how we're similar to the publishing industry.
[2024.34 --> 2031.80]  And when I hear like everybody needs to do like a rotation on this team to help clean up the code base, I hear like everybody needs to become a copy editor.
[2032.34 --> 2033.92]  And I don't like that idea.
[2034.02 --> 2034.12]  Right.
[2034.12 --> 2040.80]  I don't think that this is I feel like this is like a higher form of engineering in a way than even just like product or feature engineering.
[2040.92 --> 2041.00]  Right.
[2041.04 --> 2042.32]  I feel like feature product engineering.
[2042.52 --> 2044.36]  That's like here's the requirements.
[2044.56 --> 2045.44]  It's being done well.
[2045.50 --> 2046.50]  It's like here's the requirements.
[2046.60 --> 2047.16]  Here's this go.
[2047.44 --> 2048.12]  Go make a design.
[2048.12 --> 2054.86]  Like it feels like this more structured thing, whereas when you're trying to like do gardening or doing maintenance of a code base.
[2054.86 --> 2056.86]  I know that's still kind of an endless word right now.
[2056.86 --> 2068.20]  But when you're trying to do this, it's like trying to pull out value when you don't necessarily have that level of structure, especially within organizations, to make that happen.
[2068.40 --> 2075.18]  And I think the thing I worry about is like making bad tradeoffs when it comes to trying to garden your code bases.
[2075.28 --> 2075.42]  Right.
[2075.42 --> 2081.66]  Because just like we have to make, you know, tradeoffs when it comes to product features, we have to make tradeoffs when it comes to gardening.
[2081.76 --> 2081.86]  Right.
[2081.88 --> 2083.96]  There's a thousand paper cuts that are happening here.
[2084.16 --> 2092.28]  We have to decide, you know, which ones are at a part of your body that's just annoying and which ones are like slicing an artery that is going to make you bleed out.
[2092.76 --> 2093.80]  Gosh, Chris.
[2096.68 --> 2098.04]  Your analogies, my friend.
[2098.16 --> 2099.46]  These analogies are escalating, right?
[2101.08 --> 2102.00]  Up and away.
[2102.00 --> 2107.04]  But I feel like that's like a very difficult thing to figure out and to determine.
[2107.18 --> 2112.70]  And I feel like there are people that are really good at like that prototyping, that hackathon style engineering.
[2112.96 --> 2118.14]  I feel like there's people that are really good at this more maintenance mindset engineering.
[2118.66 --> 2124.16]  And just like I don't want to put maintenance people into hackathon style stuff because they burn out, they are miserable.
[2124.16 --> 2129.38]  I don't want to take people that would rather just be doing product features or really rather be like, give me a ticket.
[2129.50 --> 2130.22]  I'll do that ticket.
[2130.40 --> 2134.76]  And then I move on in a situation where now it's just like, here's a code base.
[2135.08 --> 2138.84]  Go make it better or go figure out the things that we need to do to make it better.
[2139.38 --> 2141.18]  So, yeah, I think that's where I fall on that.
[2141.74 --> 2143.08]  I disagree with you on that.
[2143.82 --> 2144.34]  And because.
[2144.84 --> 2145.24]  Disagreement.
[2145.54 --> 2145.78]  Nice.
[2145.78 --> 2149.50]  So, this idea of like greenfield development, right?
[2149.78 --> 2152.52]  Like, I think in a lot of ways it's an easier process.
[2152.72 --> 2153.90]  You know, you're starting from new.
[2153.94 --> 2155.76]  You don't have a lot of things to consider.
[2156.16 --> 2160.86]  But you can only do it well if you have had the experience of having to go back and change things.
[2161.26 --> 2167.76]  So, if all you do is build greenfield stuff, you're going to leave a trail of debt behind you and never realize it.
[2167.76 --> 2176.64]  So, if you have this distinction between a maintenance engineer and a greenfield engineer, I think you're going to kind of end up with bad software.
[2177.18 --> 2180.64]  It's not necessarily saying that you have to be one or the other.
[2181.04 --> 2184.46]  It's more so saying that like we shouldn't make everybody.
[2184.92 --> 2186.92]  That's why I don't like it being a rotation, right?
[2186.94 --> 2188.90]  That's the thing I was more objecting to than anything else.
[2188.90 --> 2199.58]  It's like, if people don't want to do this, that seems like an option that we can have in the same way that I think if people don't want to do product engineering, for example.
[2199.82 --> 2203.72]  Like, we're not like every engineer that works at a company must do product engineering.
[2204.10 --> 2208.10]  So, I don't think that, you know, every engineer should have to do maintenance work.
[2208.24 --> 2211.62]  I think they should have to be aware of the maintenance work that goes on, right?
[2211.64 --> 2213.08]  We can't just like in observability.
[2213.08 --> 2219.08]  We can't just like, or with SREs, we can't just be like the SREs will just take care of all of our reliability things.
[2220.12 --> 2222.48]  Like, the engineers still have to care about this.
[2222.90 --> 2231.66]  But I think it's important to make the distinction of like who winds up working on this like the most and who develops like the ethos of it, right?
[2232.22 --> 2234.82]  So, yeah, I mean, but I don't disagree with you either.
[2234.94 --> 2239.64]  So, I think it is important to get people seeing the repercussions of what they build, right?
[2239.64 --> 2247.84]  We can't have a world where there are just like, I mean, that's kind of the world we live in right now, where there's just a bunch of people running around creating stuff.
[2248.10 --> 2256.62]  And then they're never around to pay for, you know, the repercussions of it, whether that's because, you know, it's kind of built into the organization or because, you know, it's a startup or whatever.
[2257.10 --> 2260.10]  And, oh, well, we built this thing and now we've made an exit.
[2260.10 --> 2263.84]  And now the next group of people can deal with all of our terrible decisions.
[2264.46 --> 2270.48]  You know, whatever form it takes of like cut and run, we don't want people to be doing that sort of thing.
[2270.54 --> 2278.68]  So, I think it is important for people to understand maintenance, which is also why I guess I'm trying to like raise maintenance engineering to a higher level, right?
[2278.74 --> 2286.58]  It's like, you know, maintenance engineering in some ways probably should be above product engineering because you can't do product engineering without maintenance engineering.
[2286.58 --> 2295.50]  But you can definitely do maintenance engineering without product engineering because there's some code bases that have been around for decades that it's just like, no, your job is to keep this going.
[2295.70 --> 2296.98]  We're not adding features to it.
[2297.04 --> 2298.30]  We're not doing anything new with it.
[2298.38 --> 2300.64]  But we have to keep this thing going.
[2301.42 --> 2301.70]  I don't know.
[2301.78 --> 2306.42]  I would point back to, at least on the maintenance engineering is a higher form than product engineering.
[2306.52 --> 2307.46]  I'm not sure I can compare them.
[2307.58 --> 2310.60]  I would go back to John's earlier point about technical debt.
[2311.02 --> 2313.22]  And you borrow money to start a company.
[2313.52 --> 2316.04]  You take on debt for a good reason.
[2316.58 --> 2319.36]  And it's because you're trying to make something on the outside.
[2319.74 --> 2323.00]  But I would say the debt you have to take on needs to be good debt, right?
[2323.02 --> 2324.48]  There's good debt and there's bad debt.
[2324.80 --> 2326.20]  Well, we can push the analogy too far.
[2327.04 --> 2335.72]  But I do feel like this does come up in our code bases, though, because there's some code bases where like this technical debt, like this is acceptable for the tradeoff we got.
[2335.72 --> 2337.14]  And there's other technical debt.
[2337.22 --> 2338.62]  You're like, why?
[2338.78 --> 2343.78]  This was not debt we need to take on or this was debt we were never going to be able to pay down.
[2343.78 --> 2357.92]  I think that's worthy of like making sure we understand the debt that we're taking on, which I feel like is what maintenance engineers would understand a little bit better than people that aren't as focused on like what the repercussions of different types of technical debt we might take on.
[2357.92 --> 2387.08]  This episode is brought to you by Honeycomb.
[2387.08 --> 2389.58]  Don't find your most perplexing application issues.
[2389.86 --> 2396.78]  Honeycomb is a fast analysis tool that reveals the truth about every aspect of your application in production.
[2397.26 --> 2401.24]  Find out how users experience your code in complex and unpredictable environments.
[2401.58 --> 2406.46]  Find patterns and outliers across billions of rows of data and definitively solve your problems.
[2406.86 --> 2408.36]  And we use Honeycomb here at Change.
[2408.40 --> 2412.22]  Well, that's why we welcome the opportunity to add them as one of our infrastructure partners.
[2412.22 --> 2420.06]  In particular, we use Honeycomb to track down CDN issues recently, which we talked about at length on the Kaizen edition of the Ship It podcast.
[2420.30 --> 2420.98]  So check that out.
[2421.22 --> 2421.72]  Here's the thing.
[2421.96 --> 2425.20]  Teams who don't use Honeycomb are forced to find the needle in the haystack.
[2425.34 --> 2428.48]  They scroll through endless dashboards playing whack-a-mole.
[2428.72 --> 2431.74]  They deal with alert floods, trying to guess which one matters.
[2432.08 --> 2437.34]  And they go from tool to tool to tool playing sleuth, trying to figure out how all the puzzle pieces fit together.
[2437.34 --> 2444.00]  It's this context switching and tool sprawl that are slowly killing teams' effectiveness and ultimately hindering their business.
[2444.42 --> 2451.16]  With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business.
[2451.42 --> 2451.84]  Production.
[2452.40 --> 2454.84]  With Honeycomb, you guess less and you know more.
[2455.24 --> 2460.44]  Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[2460.56 --> 2464.06]  Again, honeycomb.io slash changelog.
[2464.06 --> 2466.32]  And by our friends at Retool.
[2466.68 --> 2473.08]  Retool helps teams focus on product development and customer value, not building and maintaining internal tools.
[2473.64 --> 2476.48]  It's a low-code platform built specifically for developers.
[2477.08 --> 2478.18]  No more UI libraries.
[2478.72 --> 2480.20]  No more hacking together data sources.
[2480.76 --> 2482.94]  And no more worrying about access controls.
[2483.46 --> 2491.34]  Start shipping internal apps to move your business forward in minutes with basically zero uptime, reliability, or maintenance burden on your team.
[2491.34 --> 2493.44]  Some of the best teams out there trust Retool.
[2493.56 --> 2500.72]  Brex, Coinbase, Plaid, DoorDash, LegalGenius, Amazon, Allbirds, Peloton, and so many more.
[2501.14 --> 2505.80]  The developers at these teams trust Retool as their platform to build their internal tools.
[2505.96 --> 2507.26]  And that means you can too.
[2507.64 --> 2508.44]  It's free to try.
[2508.56 --> 2510.60]  So head to retool.com slash changelog.
[2510.76 --> 2514.30]  Again, retool.com slash changelog.
[2514.30 --> 2538.66]  Is there a difference between maintainable code and good code in the way that we are talking about it?
[2539.14 --> 2540.46]  Good doesn't tell me anything, though.
[2540.92 --> 2541.16]  Maybe.
[2541.42 --> 2541.64]  Okay.
[2541.64 --> 2545.84]  I mean, actually, very good code that is obfuscated code.
[2546.02 --> 2548.64]  And, you know, it's designed to be short and terse.
[2548.82 --> 2551.74]  And it's good by that definition, right?
[2551.78 --> 2555.42]  So I always feel like we have to sort of provide the criteria.
[2556.04 --> 2556.12]  Sure.
[2556.22 --> 2557.82]  Well, no, but that's why I'm asking the question.
[2557.88 --> 2563.28]  Because when I was thinking about maintainable code, I found myself sliding into thinking about good code.
[2563.64 --> 2569.42]  And the distinction between these, I think it's interesting where it is or isn't different.
[2569.42 --> 2577.76]  Like, one thing that jumps out to me clearly is how I have internalized that belief that the best code is code that is easy to delete.
[2578.26 --> 2579.56]  That is the best code.
[2579.80 --> 2581.16]  It's not easy to extend.
[2581.62 --> 2583.44]  It's not super abstract and great.
[2583.82 --> 2584.06]  Nope.
[2584.64 --> 2585.30]  You can delete that.
[2585.30 --> 2586.66]  That's what makes it great.
[2587.36 --> 2597.16]  So the point there being, certainly, and I agree, like, I do have some of my own internal definitions of good that I think have started to skew towards maintenance.
[2597.16 --> 2606.10]  But I ask the question here because if we're having a discussion about, like, what is the relative value of maintenance versus, like, pushing forward, right?
[2606.16 --> 2613.44]  Then it seems like part of the thing that we're asking is what our values are in terms of what actually makes code good versus not.
[2613.58 --> 2619.70]  So I ask the question kind of to put a spotlight on, I guess, another definitional issue that seems to be at play behind some of this.
[2619.70 --> 2627.58]  I feel like they're different because I feel like there's code that I've seen and code that I've dealt with where I'm like, this is not good for whatever reason.
[2627.74 --> 2630.80]  Maybe it's like a Go code base that's written in, you know, Guava, right?
[2630.82 --> 2633.24]  It's Java, but just happens to have Go syntax.
[2633.82 --> 2634.60]  Wait, that's a thing?
[2635.10 --> 2635.38]  Yeah.
[2636.70 --> 2639.94]  Wow, you never come across an I iterable?
[2639.94 --> 2644.36]  You've never come across some factory factories in your Go code base?
[2644.36 --> 2645.66]  Oh, okay, wait.
[2645.78 --> 2647.54]  I thought this is, like, an actual thing.
[2647.86 --> 2648.90]  Like, no, no, no.
[2649.06 --> 2651.22]  Like a Java person wrote Go.
[2651.32 --> 2653.94]  Like, I was about to Google, like, Guava Go.
[2654.08 --> 2655.10]  No, no, no, no, no, no.
[2655.10 --> 2655.60]  Something.
[2656.16 --> 2657.30]  Okay, okay, all right.
[2657.42 --> 2660.04]  You probably heard of Gooby as well and Gaethan.
[2660.36 --> 2661.68]  Okay, yes, yes, yes.
[2661.76 --> 2665.08]  We're back in a domain that I'm familiar with and slightly less terrifying.
[2665.08 --> 2665.60]  Bye.
[2667.94 --> 2673.82]  So I've worked at some of these code bases before where I'm like, this is bad and this is gross.
[2673.82 --> 2675.10]  And I do not like this.
[2675.16 --> 2679.20]  And it makes me, as a gopher, very mad that someone has done this.
[2679.32 --> 2685.02]  But I wouldn't say that those code bases were unmaintainable or, like, weren't maintainable.
[2685.12 --> 2687.14]  It's like, you're using interfaces everywhere.
[2687.54 --> 2688.78]  I hate you for it.
[2688.90 --> 2691.36]  But, like, there's a logic to them.
[2691.84 --> 2693.74]  They're arranged in a way that makes sense.
[2693.94 --> 2696.54]  And you can see, like, okay, this is where we would add things.
[2696.58 --> 2698.52]  If we wanted to get rid of this, this is where we would delete that, right?
[2698.52 --> 2704.22]  Like, so for that reason, it seems like, yeah, we can have bad code that is still maintainable code.
[2704.38 --> 2706.44]  So I do think they are separate things.
[2706.96 --> 2714.90]  I do think in that case, like, you know, the reason we're saying it's bad code is because you're writing it in a language but not embracing the language you're writing it in.
[2714.90 --> 2723.24]  And I think, you know, to your point, you could say good has to encapsulate both writing the language for the language and also making it maintainable.
[2723.40 --> 2728.98]  In which case, then you can definitely make it so that, yes, good code and maintainable code are the same thing.
[2729.04 --> 2731.86]  But I don't think you necessarily have to do that.
[2732.36 --> 2733.60]  I think they can be distinct.
[2733.60 --> 2737.44]  So, I mean, under that, never mind, it's not even worth doing that.
[2737.56 --> 2745.08]  I'm going to, like, let's go look at, like, you know, a Go implementation of Paxos and see if that's, like, super maintainable by someone, right?
[2745.10 --> 2745.76]  Is it good code?
[2745.82 --> 2746.60]  Is it maintainable code?
[2746.68 --> 2749.30]  I think that it's complicated.
[2749.74 --> 2750.34]  It's personal.
[2750.58 --> 2752.78]  There is certainly a degree of subjectivity to it.
[2752.88 --> 2755.00]  But that's actually, that's part of the thing, too, right?
[2755.04 --> 2756.30]  Like, it is personal.
[2756.54 --> 2757.24]  It is subjective.
[2757.24 --> 2767.10]  So, is a given code base maintainable in the hands of one team, but you swap out different people or a different team dynamic and it's not maintainable anymore?
[2767.48 --> 2772.10]  I think if you're using Go, it's a bit more so than it would be otherwise.
[2772.34 --> 2775.14]  And I'm speaking, like, completely from my own experience here.
[2775.40 --> 2780.02]  Because Go was sort of designed with that in mind, right?
[2780.08 --> 2781.64]  It was designed with the ability.
[2781.84 --> 2786.66]  I mean, our linters, right, they all follow a similar approach.
[2786.66 --> 2791.52]  Our Go thumped, right, to remove, you know, everybody's pet peeves around formatting.
[2791.70 --> 2792.90]  I want my braces on this line.
[2793.02 --> 2794.92]  I want mine on my, these kinds of things, right?
[2795.10 --> 2803.66]  So, our entire sort of ecosystem, like, prides itself on the ability to, of anyone, finding a Go code base.
[2804.14 --> 2811.66]  You might not understand the problem domain that you're reading about, but you could read the Go code and the code itself will be readable to you, right?
[2811.76 --> 2814.42]  As somebody who's completely new to that code base, right?
[2814.42 --> 2819.76]  And since you're going through a 250,000 line code base right now, you can attest to that probably, right?
[2819.92 --> 2820.86]  So, to me, that's the thing.
[2820.94 --> 2827.68]  Like, the technology that we use can help, right, in the maintainability, right, of software, right?
[2827.70 --> 2832.82]  So, if we add that sort of lens to it, I think the technology plays a huge role in that as well.
[2832.98 --> 2833.52]  Not just the people.
[2833.52 --> 2838.92]  I think in that case, too, we have to, like, maybe level up what maintainability means as well.
[2839.00 --> 2852.40]  Because it's like, okay, well, if we want to be able to move this code base between teams, say, like, if we have, say, microservices, and those microservices might be handed off to different teams or reorg to, like, make things make more sense.
[2852.40 --> 2862.66]  I think that's where you have to start building more, I guess, documentation in this case or just processes and practices into your organization that allows that code to be moved between.
[2862.98 --> 2870.08]  And that inability for a code base to move from one team to another team becomes a problem of maintenance, right?
[2870.08 --> 2882.20]  It's like, okay, now this code base that might be maintainable for one team is now classified as unmaintainable because it can't be maintained by two teams or three teams or however many teams that you want it to be maintained by.
[2882.36 --> 2884.70]  And then that's a thing you have to go back in and resolve.
[2885.32 --> 2892.94]  I wonder if that helps us frame maintenance as well to kind of, like, help us answer this various question that exists right now of, like, what is maintenance?
[2892.94 --> 2900.30]  Maybe it is this thing of, like, you know, a sense of the team, so it's, like, a subjective thing, and, like, a comparator over time.
[2900.52 --> 2909.72]  So it's, like, all right, well, this code base is currently maintainable because, like, we can do something that we weren't able to do before.
[2909.82 --> 2914.16]  Now we can do it now, and we continue to sustain the ability to do that into the future.
[2914.24 --> 2922.52]  If we add a new thing to our definition of maintenance, then something that was maintainable becomes unmaintainable, and we have to, like, bring it back to home of maintenance.
[2922.52 --> 2924.60]  It reminds me a lot of simplicity, right?
[2924.66 --> 2930.62]  Like, what is simple and, you know, the famous rich hickey talk of simple made easy and all of that.
[2930.74 --> 2938.04]  It's, like, it's this very difficult concept to, like, pin down, grab down, and you know it when you go into a code base, right?
[2938.06 --> 2945.82]  You know a simple code base when you're in it and you're working in it, and it's hard to figure out when you've lost that simplicity, but you always sense that you've lost it.
[2945.90 --> 2947.14]  I feel like maintenance is the same thing.
[2947.14 --> 2949.62]  It's, like, you know when you're in a maintainable code base.
[2949.62 --> 2953.56]  It has a certain feeling, and then you know when you've lost that.
[2953.64 --> 2960.14]  You know when something has diverged, and it's like, okay, this no longer feels like a maintainable code base anymore.
[2960.24 --> 2963.18]  There's something wrong with the way that we can properly maintain it.
[2963.66 --> 2965.08]  I feel like this is all subjective, though.
[2965.24 --> 2978.60]  I mean, this is all very much our own experiences, and I think naturally, as an engineer grows from, you know, junior, intermediate, you know, senior, super-duper senior, whatever other titles we throw out these days.
[2978.60 --> 2979.04]  Staff.
[2979.04 --> 2979.24]  Staff.
[2979.96 --> 2981.14]  Staff, and you know, whatever.
[2981.28 --> 2982.72]  I prefer super-duper senior.
[2982.90 --> 2983.62]  Thank you very much.
[2985.06 --> 2985.28]  Yeah.
[2986.28 --> 2986.60]  Right.
[2986.72 --> 2990.16]  It's all, I mean, you learn, you get that gut feeling that Chris is talking about, right?
[2990.18 --> 2996.28]  He's like, yes, this is, based on my experience, you know, based on what I've been through, this feels good.
[2996.28 --> 3008.20]  And when you start to lose that grip, and when you can no longer hold in your head all the different strands that you've had to fold to understand one single feature in a code base, once you've lost that, then you kind of, ah, you know, this could be better, right?
[3008.44 --> 3011.92]  But is there a more scientific method, right?
[3011.92 --> 3033.08]  Like, I remember back in my Ruby days, we relied quite a bit on things like code climate and whatnot to measure things like, you know, cyclomatic complexity and sort of repetition, you know, all these kinds of things, like, you know, some heuristics and trying to figure out, okay, based on a common set of agreed-upon don't-dos, in this case, the Ruby community, right?
[3033.08 --> 3035.68]  These are the things you should avoid doing in your code base.
[3035.72 --> 3037.48]  So you get that feedback almost immediately, right?
[3037.54 --> 3042.68]  You open up a PR, and then, boom, you've got some feedback from a machine, right?
[3042.96 --> 3047.50]  Not from another human, from a machine, telling you, hey, we ran some linters, and this is what we found.
[3047.70 --> 3048.64]  Rubocop yelling at you.
[3048.78 --> 3054.20]  I mean, I remember I'd be fighting Rubocop every day on every NPR, because I'd be like, oh, okay, fine.
[3054.28 --> 3055.36]  I have to go and fix that, right?
[3055.56 --> 3056.32]  Oh, okay, fine.
[3056.32 --> 3063.06]  But you're paying that cost, and you have a machine helping you, right, to identify these things, and all in the hope that you will not be able to do that.
[3063.08 --> 3074.60]  And I get to a point where you've got so many of these, the accumulation of these minor paper cuts, right, I recall them, that the code base becomes sort of, ah, every time you're in there, it kind of feels yucky, kind of feels that feeling that you're talking about, Chris.
[3074.68 --> 3079.26]  It's like, oh, man, we have too many, you know, little pinpricks here, kind of thing.
[3079.56 --> 3084.56]  Is there such a thing, and go, obviously, we have all linters, you know, we can have that sort of immediate feedback mechanism.
[3085.02 --> 3090.22]  But do we all agree on patterns and best practices and things?
[3090.22 --> 3095.44]  The stuff that we sort of usually thought of would idiomatic go, is that our common set of patterns?
[3095.60 --> 3097.62]  Is that as scientific as we get?
[3098.10 --> 3101.98]  I feel like for go, we could probably get at least part of the way there.
[3102.18 --> 3106.16]  Like, once again, I'm always thinking about writing, because I'm a writer.
[3106.56 --> 3115.90]  But I'm kind of thinking of, like, you know, manuals of style and how, when you have a manual style, it has a lot of very strong opinions about this is how you do things.
[3115.90 --> 3116.50]  Exactly.
[3119.02 --> 3123.18]  For those wondering what we're laughing about, Sam just pulled up a book on style.
[3124.04 --> 3125.72]  Yeah, Strunk and White's a classic.
[3125.86 --> 3127.72]  The book on style, in fact, yes.
[3127.72 --> 3129.00]  The book, yep, the book.
[3129.02 --> 3129.16]  Indeed.
[3130.32 --> 3132.76]  Chicago manual style sitting on my bookshelf right over there.
[3132.84 --> 3134.20]  Oh, it's a fight.
[3134.52 --> 3135.32]  It's a fight.
[3137.10 --> 3138.90]  Writer's version of tabs versus spaces.
[3139.14 --> 3139.26]  Yeah.
[3139.44 --> 3139.72]  Yep.
[3139.96 --> 3140.68]  Yeah, exactly.
[3140.76 --> 3143.82]  It's like the famous, like, you know, you have closing quotation marks.
[3143.82 --> 3145.66]  Does the comma go inside or outside of them?
[3145.66 --> 3146.02]  Mm-hmm.
[3146.30 --> 3146.62]  Right?
[3146.78 --> 3147.48]  Like, outside.
[3148.32 --> 3153.98]  There are these things that are, like, I don't think there is an objective answer, but we still need an answer.
[3153.98 --> 3162.12]  So I think, like, if we as a community or if we as a group of people can craft something like that, then I think the answer to your question is, like, yes.
[3162.56 --> 3165.96]  I feel like there is a more scientific approach we can take to things.
[3165.96 --> 3174.20]  But I think for us, especially, you know, if we take kind of wider angle of it, not just go, I don't think so.
[3174.32 --> 3176.46]  I think a lot about, like, you know, once again, writing.
[3176.56 --> 3185.52]  It's like what's good in a romance novel or, like, one of those trashy, you know, airport romance novels versus what's good in the New York Times is going to be very different.
[3185.98 --> 3187.64]  And neither is wrong.
[3188.14 --> 3190.44]  And you probably wouldn't want to label either one as wrong.
[3190.44 --> 3192.20]  I feel like code is the same way, right?
[3192.28 --> 3195.80]  What is good in Go is not the same as what is good in Java.
[3196.36 --> 3201.46]  And I think even within Go code bases, what's good in some Go code bases is probably not good in others.
[3201.52 --> 3205.60]  Like, I think of the use of the unsafe package or the use of the sync package.
[3205.80 --> 3210.12]  Like, some teams and some organizations, that's a good decision.
[3210.20 --> 3211.18]  That's a good thing to use.
[3211.24 --> 3212.88]  It's like you have the engineers with the experience.
[3213.52 --> 3216.26]  Other teams probably shouldn't be doing that.
[3216.36 --> 3218.66]  Like, someone's going to, like, blow off their foot with that.
[3218.66 --> 3221.06]  Just, man, gruesome analogies today.
[3221.40 --> 3221.76]  Seriously.
[3222.22 --> 3229.20]  It's just, I mean, and also, I don't know about you, but I start every main package with a compare and swap because that's just how I roll.
[3229.54 --> 3231.54]  Why use mutexes when you can use atomics?
[3231.74 --> 3232.14]  Like, come on.
[3232.22 --> 3232.54]  Seriously.
[3232.84 --> 3234.34]  It's all the cool kids are doing that.
[3234.72 --> 3241.84]  I think it's, like, one of those things that, like, if you define enough components of it, though, you can get toward a more objective thing.
[3241.84 --> 3247.32]  But I think it will always have hefty, hefty amounts of subjectivity that you need to kind of abide by.
[3247.32 --> 3253.60]  And I think we as a Go community, I think this is, like, a thing that we need to do is we need to start writing these things down more, right?
[3253.68 --> 3260.16]  You know, when you look at the Chicago Manual Style or the AP Style book, like, they didn't just appear as thousand page.
[3260.36 --> 3262.38]  Well, the AP Manual Style is shorter.
[3262.62 --> 3265.74]  But they didn't just appear as these, like, huge books.
[3265.96 --> 3266.50]  The important parts.
[3266.60 --> 3268.38]  They appeared over time.
[3268.48 --> 3268.64]  Okay.
[3268.76 --> 3271.02]  I have problems with Strunk and White, but we are not.
[3271.02 --> 3272.02]  Style, the good parts.
[3273.62 --> 3273.98]  85.
[3274.32 --> 3275.06]  The elements of style.
[3275.06 --> 3277.90]  What is this thousand page business you're talking about?
[3278.30 --> 3278.56]  Continue.
[3278.68 --> 3280.48]  There are some antiquated things in that.
[3280.56 --> 3280.78]  Anyway.
[3281.16 --> 3282.08]  Yes, yes, they're wrong.
[3283.44 --> 3286.28]  They didn't just spring out of, like, out of nothing.
[3286.66 --> 3293.24]  They were developed by, like, smaller style sheets for specific books over time and then compounded over time.
[3293.36 --> 3299.22]  So it's, like, I think we as a community need to start just doing that action of, like, more people writing manuals.
[3299.34 --> 3300.52]  And there's some out there, right?
[3300.82 --> 3301.04]  Go.
[3301.18 --> 3302.52]  I think Uber has one for Go.
[3302.62 --> 3303.90]  I think Facebook has one for Go.
[3303.90 --> 3304.52]  You go look.
[3304.78 --> 3305.56]  You find them.
[3306.00 --> 3308.02]  But they're all very, very, very short.
[3308.10 --> 3309.48]  Not even 85 pages, right?
[3309.52 --> 3311.68]  These are, like, five pages.
[3312.28 --> 3317.36]  And I think that's what makes it so hard to understand what maintainability is at the end of the day.
[3317.42 --> 3327.42]  Because, you know, once again, to go back to the paper cuts, those small paper cuts are those small little decisions that aren't being aligned over time.
[3327.42 --> 3333.28]  It's the equivalent of, like, not making a decision about whether the comma goes inside or outside the quotes.
[3333.44 --> 3337.06]  And then it's, like, different for every paragraph in the whole book.
[3337.30 --> 3340.36]  And it's, like, pick a way to do it and then stick with it.
[3340.36 --> 3341.72]  It's one of the reasons we love GoFump.
[3341.80 --> 3343.40]  It's, like, brackets go here.
[3343.88 --> 3346.76]  Like, these things go in these places and that's where they live.
[3346.92 --> 3348.30]  And now we don't have to think about it.
[3348.30 --> 3349.78]  We don't have to care about these things.
[3350.00 --> 3352.12]  That was a very, very long way of answering your question.
[3352.22 --> 3354.80]  I hope I actually, like, captured some of it.
[3355.22 --> 3361.62]  Can I try to sum that up into a pseudoscientific, still subjective, but something that has more numbery bits in it?
[3361.80 --> 3362.34]  Go for it.
[3362.46 --> 3364.84]  I want to loop back on the correctness bit that we were talking about earlier.
[3364.96 --> 3367.44]  I mean, everything you were talking about just now are essentially correctness criteria.
[3367.44 --> 3372.00]  Not formal verification, correctness, but, like, it's correct if it passes linting and not if it doesn't.
[3372.68 --> 3379.06]  I would offer that the maintainability of a code base, starting just accepting the premise, this is subjective.
[3379.06 --> 3380.92]  Because I don't see any way around it.
[3381.30 --> 3391.76]  Is the ratio, you can understand the maintainability of a code base by looking at the ratio of time spent researching what is correct versus making the thing correct.
[3392.24 --> 3395.74]  Whether you're talking about trying to fix a bug and so, you know, failure locality, right?
[3395.80 --> 3398.84]  Like, how long does it take to figure out why the thing is failing?
[3399.52 --> 3408.00]  How long does it take to figure out the rule you should apply in deciding how to fix the thing versus actually fixing the thing?
[3408.00 --> 3415.54]  And that ratio, which, yes, like, will vary from person to person based on the length of their experience, they're familiar with the code base.
[3415.92 --> 3417.68]  But, again, I don't see a way around it.
[3418.04 --> 3421.48]  I think that may be the kind of core of what we're driving at here.
[3421.48 --> 3425.46]  I feel like that sums up what I took, like, 10 minutes to say.
[3427.20 --> 3435.70]  Okay, so speaking about Go, because we're kind of getting toward the end of the episode here, and I feel like we've been very light on the Go content in this episode.
[3435.94 --> 3437.06]  So it's Go time.
[3437.18 --> 3437.90]  We've got to talk about it.
[3438.20 --> 3438.44]  I don't know.
[3438.56 --> 3440.28]  I think it's been implicit in there.
[3440.58 --> 3441.88]  I think it very much applies.
[3441.88 --> 3443.60]  Well, thank you for saving me there.
[3445.04 --> 3455.52]  But is there anything that I guess any of you would give as, you know, what makes Go a good language for building, like, maintainable code bases?
[3455.64 --> 3465.24]  Like, what things do we have that are, like, yes, like, this is why I like and enjoy writing maintainable code for, you know, knowing that we haven't quite defined maintainability that well.
[3465.24 --> 3468.70]  But this is what I like that Go has that makes it so I can write maintainable code.
[3468.74 --> 3473.14]  And then what are some things, if there are any, that make Go a bad language for said maintainability?
[3473.62 --> 3475.88]  If you each want to answer that in turn.
[3476.24 --> 3477.84]  I already gave my reasoning for that.
[3478.16 --> 3487.44]  The fact that I can drop new person in a Go code base, and even though they're still learning about the problem domain, it's not Go to have a problem.
[3488.14 --> 3489.04]  They're not fighting the language.
[3489.18 --> 3490.50]  It's not Go to have a problem understanding.
[3490.70 --> 3492.70]  It's, you know, what is this type doing?
[3492.86 --> 3493.62]  Where is it used?
[3493.62 --> 3496.00]  What business problems it's solving, right?
[3496.36 --> 3506.56]  So that, for me, I've never experienced a language that gives me that sort of room, right, with my engineering team to be able to say, hey, go into this code base.
[3506.60 --> 3509.34]  I know you've never worked on this code base, but this is what it's supposed to do, right?
[3509.84 --> 3513.06]  I have a bug fix or I have a feature, you know, drop in there, see what you can do.
[3513.32 --> 3521.98]  And then relatively speaking to other languages, they come back much more quickly with the fix or the feature or whatever it is because they didn't have to fight the language, right?
[3521.98 --> 3523.92]  They easily understood what they were reading.
[3524.42 --> 3527.60]  Once they understood the problem domain, they were able to execute and get the job done.
[3527.92 --> 3531.78]  Like, to me, there's nothing like Go that does this, in my experience.
[3532.44 --> 3532.66]  Ian.
[3533.16 --> 3534.68]  Yeah, so, I mean, I'll mirror that.
[3534.78 --> 3537.46]  The simplicity of the language just adds to the maintainability.
[3537.46 --> 3542.28]  But on top of that, I think the errors as values really adds to this.
[3542.46 --> 3551.90]  Being able to explicitly see error paths and not worrying about exceptions and trying to trace these all the way back up really adds to, like, glanceability and therefore maintainability.
[3552.34 --> 3557.32]  Wait, so you don't use panic, defer, recover everywhere in your code all over the place all the time?
[3557.96 --> 3558.66]  That's crazy.
[3558.80 --> 3561.00]  I think that's what we all did.
[3561.30 --> 3562.30]  Sam's best practice.
[3562.30 --> 3565.60]  I got to go rewrite a lot of code right now, guys.
[3565.68 --> 3566.92]  That's not good.
[3568.98 --> 3570.22]  Planning-driven development.
[3570.68 --> 3571.20]  Sam?
[3571.64 --> 3572.08]  Yeah.
[3572.36 --> 3574.34]  I mean, I'll go with the definition I just offered, right?
[3574.42 --> 3588.48]  Like, I think that I will mirror these same statements and translate them into the ability to quickly, with very little research time and mostly fixed time, hone in on the basic answers to the questions about structured code.
[3588.48 --> 3599.28]  I remember running face-first into a very large Ruby code base and being gobsmacked about my inability to figure out what felt like basic questions.
[3599.38 --> 3608.98]  I had been really just focusing on Go code for a while and came back and was just like, wow, I can't even, like, I can't even just, like, look up symbol names and find them in places.
[3608.98 --> 3612.60]  There has to be, like, you know, special pseudo-static analysis.
[3613.58 --> 3633.72]  The manner in which the structures and variance rules, whatever the language, make it possible to, even over large code bases, have clear answers to questions about basic things like, what are all the instances of this, you know, references to this type or to this interface?
[3633.72 --> 3638.08]  Or perhaps even find all the implementations of it, a relatively difficult thing to do and yet still very doable.
[3638.56 --> 3640.14]  Like, it goes very innumerable.
[3640.62 --> 3642.30]  It's very analyzable.
[3642.84 --> 3653.22]  And that means that most of my cognitive effort is spent on dealing with the higher order abstractions that people have tried to create because all the boring questions are quickly answerable.
[3653.52 --> 3655.24]  And so I can get right to the heart of the matter.
[3655.24 --> 3656.08]  All right.
[3656.36 --> 3657.68]  And then final question.
[3658.38 --> 3667.52]  What would you add, if you have anything, to make Go more, let's not make Go itself more maintainable, but make the code that we write more maintainable?
[3668.18 --> 3668.62]  Generics.
[3669.32 --> 3669.88]  Hell no.
[3672.40 --> 3673.22]  No, no, no.
[3673.32 --> 3674.64]  I want generics, but just for me.
[3675.22 --> 3676.98]  It's everybody else can screw themselves, right?
[3677.34 --> 3680.78]  Like, because then I know what mine do, and I don't have to deal with any of your garbage.
[3681.32 --> 3682.66]  And we're fine.
[3683.24 --> 3683.68]  Right?
[3683.80 --> 3684.38]  I'm fine.
[3684.38 --> 3685.72]  That's what's important here.
[3686.90 --> 3687.24]  Yeah.
[3688.16 --> 3689.12]  Oh, I would add Rust.
[3689.30 --> 3690.00]  That's what I would add.
[3692.54 --> 3695.36]  I would really like to have, you know, compile time.
[3695.68 --> 3696.00]  Unpopular.
[3696.00 --> 3697.34]  There you go.
[3697.52 --> 3705.18]  I would really like to have compile time guarantees about shared access to global immutable state.
[3705.34 --> 3708.16]  Forget this, like, Go test race garbage.
[3708.38 --> 3708.68]  Come on.
[3709.64 --> 3710.68]  Static or nothing.
[3710.98 --> 3713.36]  That's my, uh, is this a helpful answer?
[3713.36 --> 3714.34]  This isn't a helpful answer.
[3714.50 --> 3714.74]  I'm sorry.
[3714.74 --> 3717.06]  Well, we avoided dependency management, so it's okay.
[3717.24 --> 3718.00]  We did.
[3718.18 --> 3718.54]  We did.
[3718.78 --> 3718.86]  Yes.
[3720.98 --> 3722.28]  Scooted right by it.
[3722.34 --> 3722.82]  Well done.
[3723.24 --> 3724.14]  Uh, okay.
[3724.90 --> 3725.34]  Nice.
[3725.34 --> 3728.44]  It's time for unpopular opinions.
[3732.96 --> 3733.64]  Unpopular opinions.
[3734.04 --> 3734.56]  What?
[3734.82 --> 3736.52]  I actually think she'd probably leave.
[3739.80 --> 3741.44]  Unpopular opinions.
[3741.44 --> 3748.22]  Ian, you're up first.
[3748.22 --> 3749.22]  Unpopular opinion.
[3749.46 --> 3751.16]  I really don't have one this time.
[3751.42 --> 3752.94]  I cannot think of anything.
[3753.40 --> 3754.10]  Oh, man.
[3754.68 --> 3755.20]  It's okay.
[3755.38 --> 3756.72]  Sam has an extra four for you.
[3756.92 --> 3757.50]  Oh, crap.
[3758.16 --> 3761.84]  Let me hear some other ones, and I'll, uh, you know, something pops in my mouth.
[3762.04 --> 3763.14]  Get the wheels turning.
[3763.14 --> 3767.34]  Sam, any unpopular opinions?
[3767.86 --> 3771.60]  I totally had, like, two at the beginning, and then we were talking about all this interesting stuff.
[3772.70 --> 3776.08]  Don't, well, I was going to say don't use gRPC, but I can actually back that one up.
[3777.12 --> 3778.46]  I don't think that's unpopular.
[3778.66 --> 3779.76]  You don't have to back it up.
[3779.80 --> 3781.28]  You can just throw it out there.
[3781.58 --> 3782.94]  Oh, I can just throw it out there?
[3783.14 --> 3784.14]  Jeez, God, that's liberating.
[3784.98 --> 3785.20]  Okay.
[3785.34 --> 3786.08]  Don't use gRPC.
[3786.44 --> 3787.28]  Let the masses interpret.
[3787.64 --> 3788.00]  All right.
[3788.22 --> 3790.32]  Uh, don't use gRPC streams.
[3791.00 --> 3791.32]  Unpopular.
[3791.88 --> 3792.38]  There we go.
[3792.38 --> 3792.98]  Oh, okay.
[3793.40 --> 3794.08]  That's nuanced.
[3794.32 --> 3794.46]  Yeah.
[3795.00 --> 3796.74]  I feel like that's not unpopular, though.
[3796.94 --> 3797.28]  Like, gRPC.
[3798.02 --> 3798.34]  Right.
[3798.50 --> 3802.70]  That's the problem, is that all of my opinions are right and popular, and so how am I supposed to?
[3804.56 --> 3806.16]  There's the unpopular opinion.
[3806.50 --> 3806.88]  There it is.
[3806.90 --> 3807.66]  There it is.
[3808.02 --> 3808.78]  There we go.
[3809.16 --> 3810.10]  There we go.
[3810.58 --> 3811.38]  There we go.
[3811.72 --> 3811.98]  Yeah.
[3812.72 --> 3821.76]  And yet, I also think that that one might be a relatively common one, even if not necessarily unpopular in our industry.
[3821.76 --> 3823.28]  We've done enough meta dancing.
[3823.40 --> 3828.24]  I feel like Johnny gets to go, and then maybe I'll have something more real in a minute, maybe.
[3828.78 --> 3832.20]  Johnny, I know you have many unpopular opinions, so.
[3832.76 --> 3832.94]  Yeah.
[3832.94 --> 3835.44]  Let me formalize it into a natural unpopular opinion.
[3835.82 --> 3846.00]  I don't think you should have separate teams, feature teams, health squads, folks who only work, you know, on greenfield stuff or whatever.
[3846.00 --> 3855.54]  And, like, I don't believe in sort of because what if I was hired and I was put on the bug squash team and then I want to work on some feature stuff?
[3855.64 --> 3857.60]  Like, am I never going to get a chance to do that?
[3857.70 --> 3857.82]  Right?
[3857.90 --> 3858.10]  No.
[3858.56 --> 3862.30]  I think teams should be loose in terms of their memberships.
[3862.30 --> 3868.26]  And people can just, if you want to have formalized rotation to put people in different teams, and that goes for on-call as well.
[3868.56 --> 3878.32]  I firmly believe that if you're on a team writing software that goes into production and it needs to be operated, right, I think you need to be on the hook for when something goes wrong.
[3878.92 --> 3879.64]  You're on the pager.
[3879.98 --> 3881.78]  You get called as a responder, right?
[3881.78 --> 3886.46]  I think that perhaps that is another opinion, but I think you need to be part of that rotation as well.
[3886.86 --> 3899.80]  It all basically falls under this umbrella that, as an engineer, you need to be exposed through basically to all the layers, right, of the stack as it pertains to running the piece of software that helps a business make money.
[3899.98 --> 3908.70]  I think you need to understand each, maybe even spend some time in support, the front lines of customer requests and bug filings or whatever it is, right?
[3908.70 --> 3911.50]  So play a role in each layer of that.
[3911.78 --> 3913.78]  And trust me, this is not a punishment.
[3914.10 --> 3923.32]  This is going to make you exponentially better engineer if you understand the different vectors, right, of things that are coming at your piece of software that you're writing, that your teams are responsible for.
[3923.60 --> 3925.10]  That's going to give you superpowers as an engineer.
[3925.22 --> 3925.82]  That's all I can say.
[3926.08 --> 3926.76]  I think I agree with that.
[3926.80 --> 3930.22]  Not the on-call stuff because I don't wake up for anything when I'm asleep.
[3930.50 --> 3933.80]  So the things are going to be broken until I wake up in the morning.
[3933.90 --> 3935.92]  So if that's okay, then sure.
[3935.92 --> 3938.76]  But I feel like maybe on-call should be for...
[3938.76 --> 3939.76]  You wouldn't do well on my team.
[3939.76 --> 3946.56]  This is also why I purposefully avoid roles that have on-call components to them because I know this about myself.
[3946.82 --> 3947.76]  So I...
[3947.76 --> 3949.14]  It's good to know thyself.
[3949.46 --> 3949.72]  Yes.
[3950.06 --> 3951.40]  Man who understands his constraints.
[3951.52 --> 3952.42]  I mean, respect, right?
[3952.58 --> 3953.04]  Like...
[3953.04 --> 3954.16]  I like high-level stuff.
[3954.16 --> 3955.92]  I like being at 30,000 feet.
[3956.08 --> 3957.78]  I can come down to the ground at some point.
[3957.98 --> 3963.00]  But like on-calls, usually not at 30,000 feet.
[3963.18 --> 3963.88]  That's for the birds.
[3964.76 --> 3965.92]  You're a little bit lower.
[3965.92 --> 3968.10]  But no, I think you're right, though.
[3968.22 --> 3973.00]  I mean, I've been doing a bunch of security engineering-related work at work.
[3973.60 --> 3979.58]  And I'm like, more people need to understand security, not to implement it themselves.
[3979.90 --> 3981.24]  Please don't go roll your own crypto.
[3981.24 --> 3993.06]  But I think from like actually getting in and understanding how, you know, public key infrastructure, how certs work, how public-private key pairs work, how like cryptography in general works.
[3993.22 --> 3998.00]  Like, I think enough people don't get exposed to that because security is like in this specialized area.
[3998.16 --> 4001.96]  I think reliability is the same sort of thing where it's like, you know, there is...
[4001.96 --> 4002.96]  Oh, there's the SRE team.
[4002.96 --> 4004.34]  They tackle stuff.
[4004.80 --> 4007.40]  So I am in general agreement with you.
[4007.96 --> 4013.16]  I think software engineers need to be taking more on as far as like what their remint is.
[4013.46 --> 4015.34]  It shouldn't just be, go build some products.
[4015.46 --> 4016.22]  Go write some code.
[4016.68 --> 4017.06]  Chris is there.
[4017.12 --> 4019.02]  I agree, except when it applies to me.
[4020.04 --> 4024.40]  I can agree with something in general and know that it wouldn't work that well for me.
[4024.72 --> 4028.44]  I mean, like, I could do on-call just during the day hours.
[4028.44 --> 4032.50]  Or more so, I just will write software that doesn't crash at night.
[4033.00 --> 4034.28]  Oh, okay.
[4034.60 --> 4035.74]  Or doesn't crash at all.
[4035.96 --> 4036.92]  There's the...
[4036.92 --> 4037.68]  See, that's the thing.
[4037.68 --> 4038.30]  That's the trick.
[4038.38 --> 4039.38]  Or only crashes.
[4039.84 --> 4042.80]  Crash a little software, which is a real thing.
[4042.98 --> 4043.78]  That's a great thing.
[4044.00 --> 4044.66]  Ian, I have another.
[4044.78 --> 4047.10]  I do have one if you want another minute to think.
[4047.16 --> 4047.60]  Otherwise, go.
[4048.12 --> 4048.72]  You can go ahead.
[4049.58 --> 4058.42]  Do not use semantic versioning for any versioning system that you create unless you can define what backwards compatibility means.
[4058.92 --> 4059.18]  Clearly.
[4059.70 --> 4060.34]  And precisely.
[4060.82 --> 4061.12]  Mm-hmm.
[4061.70 --> 4061.96]  Yeah.
[4062.66 --> 4064.08]  Skating into dependency management.
[4064.38 --> 4064.52]  Just a little bit.
[4064.52 --> 4064.74]  Yeah.
[4064.74 --> 4065.02]  Yeah.
[4066.16 --> 4067.14]  That is...
[4067.14 --> 4067.42]  Yeah.
[4067.52 --> 4069.10]  A little subtweet there, but...
[4069.10 --> 4069.22]  Yeah.
[4069.62 --> 4069.98]  Yeah.
[4070.84 --> 4071.50]  Sneaking in.
[4071.82 --> 4072.00]  Yeah.
[4072.18 --> 4072.44]  You know.
[4072.50 --> 4073.30]  Snuck that one in.
[4073.54 --> 4074.14]  Just...
[4074.14 --> 4074.48]  Yeah.
[4074.92 --> 4075.12]  Yeah.
[4075.26 --> 4075.66]  I gotcha.
[4076.22 --> 4078.78]  I mean, oh, I don't know if that's going to be...
[4078.78 --> 4084.08]  It'll be popular among some people and very unpopular among other people.
[4084.58 --> 4085.06]  So...
[4085.06 --> 4087.12]  The conditionality makes it very interesting.
[4087.12 --> 4092.86]  If I've had previous conversations with you about it, you know that there's a deep troll in that statement, too.
[4092.98 --> 4093.86]  But I'm not going to...
[4093.86 --> 4095.96]  I'm not going to unroll it here.
[4096.76 --> 4097.04]  So...
[4097.04 --> 4100.24]  I was going to say, depending on how...
[4100.24 --> 4105.72]  There's going to be a whole swath of new Go developers who have no idea of the backstory for all this.
[4105.72 --> 4105.88]  So...
[4105.88 --> 4109.60]  There's going to be a bunch of people who are like, yeah, yeah, I get what you mean.
[4109.94 --> 4111.00]  We get what you're putting down.
[4111.32 --> 4112.46]  You know, it's...
[4112.46 --> 4115.74]  I think it's a statement that stands on its own, though, independent of any history.
[4116.14 --> 4116.42]  So...
[4116.42 --> 4116.68]  Right.
[4116.88 --> 4117.06]  Yeah.
[4117.42 --> 4117.66]  Yeah.
[4117.86 --> 4118.04]  Yeah.
[4118.14 --> 4119.70]  There's a lot there to that one.
[4119.86 --> 4122.06]  I think it hooks into, like, the episode, you know?
[4122.30 --> 4123.82]  We started out just talking about maintenance.
[4123.94 --> 4126.26]  And we're like, maybe we should define what maintenance is.
[4126.26 --> 4134.42]  So if there's a specific thing that's at the crux, I feel like when it comes to semantic versioning, the thing at the crux of it is this idea of backwards compatibility.
[4134.82 --> 4138.58]  Because, like, that's what all of the digits in it are about.
[4138.74 --> 4139.74]  It's like, what...
[4139.74 --> 4141.60]  How much have you maintained backwards compatibility?
[4141.90 --> 4144.10]  You don't define what that means.
[4144.64 --> 4144.72]  Well...
[4144.72 --> 4145.56]  You kind of have a problem.
[4146.08 --> 4150.56]  You wind up with that function that is, like, means different things to different people.
[4150.76 --> 4153.64]  And then it has 14 parameters.
[4153.64 --> 4156.62]  And they still don't describe the entire possible space.
[4157.00 --> 4162.28]  Because thus far, we've been talking mostly about maintenance as though it's something which is kind of confined to a single team.
[4163.02 --> 4164.24]  Which kind of isn't true.
[4164.70 --> 4168.22]  When you've got a blast radius that is as large as your depender space.
[4168.42 --> 4170.40]  This is why this is a series and not an episode.
[4172.14 --> 4172.54]  Yeah.
[4173.38 --> 4180.86]  But yeah, I've never, ever run into a code base that I've maintained that has a 14 parameter function that only has three lines of code.
[4180.94 --> 4181.34]  Never.
[4181.34 --> 4181.46]  Never.
[4181.78 --> 4184.04]  I've never felt that situation happen.
[4184.36 --> 4185.12]  Not even one time?
[4185.48 --> 4186.36]  Never have I ever.
[4186.50 --> 4191.64]  The thing about it is, in that situation, too, that code is like, this is actually correct for the state of the code base right now.
[4191.66 --> 4192.60]  And I'm mad about it.
[4193.22 --> 4197.92]  Yeah, just one 14 parameter function calling another 14 parameter function.
[4198.36 --> 4200.98]  Well, I would hope it's at least like a 14 calling a 13.
[4201.14 --> 4203.30]  So you're doing, like, partial function application all the way down.
[4203.38 --> 4205.44]  You're just peeling parameters off, like, one at a time.
[4205.92 --> 4206.70]  Does it not do that?
[4207.04 --> 4208.52]  Now I'm picturing, like, a code pyramid.
[4208.52 --> 4214.30]  It was an unpleasant situation when I had to refactor a lot of code to get rid of that.
[4216.24 --> 4222.84]  I looked at it and I'm like, this looks wrong, but it's not wrong.
[4223.54 --> 4224.48]  All right, merge it.
[4224.48 --> 4228.34]  Yeah, it was a bad situation.
[4228.46 --> 4230.58]  Anyway, Ian, unpopular opinion.
[4230.70 --> 4231.16]  Got anything?
[4231.60 --> 4233.88]  It doesn't have to be related to Go or code.
[4234.14 --> 4236.32]  It is not related, but I do have something.
[4236.58 --> 4236.82]  Okay.
[4236.82 --> 4244.26]  I do not think variables belong in paths of URLs, like, especially in APIs.
[4244.46 --> 4248.90]  I think we have query parameters that are built for this.
[4249.18 --> 4253.44]  So all these APIs that are slash one to get something, I think that was a misstep.
[4253.72 --> 4254.46]  You're old school, huh?
[4254.66 --> 4256.48]  When I started, REST was already a thing.
[4256.56 --> 4258.60]  I think it was just a bad thing, you know, like.
[4258.86 --> 4259.74]  Clean URLs.
[4260.46 --> 4261.84]  Great idea for WordPress.
[4262.14 --> 4263.24]  Bad idea for APIs.
[4264.76 --> 4265.84]  That was what mine went to.
[4266.20 --> 4267.98]  I went to Drupal days, for sure.
[4268.26 --> 4271.02]  I feel like Roy Fielding would be very happy with you right now.
[4272.02 --> 4274.50]  I think he has a couple of rants about that.
[4274.50 --> 4277.22]  About just, your URLs are opaque.
[4277.38 --> 4279.78]  Stop putting stuff in them that you need to parse.
[4280.32 --> 4282.40]  There's other parts of the protocol, but anyway.
[4283.48 --> 4286.68]  Yes, all good, unpopular opinions.
[4287.20 --> 4287.90]  Oh, so we think.
[4287.90 --> 4290.78]  Like, they end up being popular anyways.
[4291.04 --> 4294.18]  Like, I'm not really sure how many of these are going to wind up being popular.
[4294.52 --> 4295.36]  I feel like it could be.
[4295.44 --> 4298.18]  It's like an actual, like, I'm wondering what the poll results will say.
[4298.74 --> 4301.12]  Because we do go and we poll all of these on Twitter.
[4301.58 --> 4303.66]  So, it should be good.
[4303.74 --> 4308.38]  I mean, my summer one really, like, that one gets unpopular when you start suggesting alternatives.
[4308.64 --> 4310.96]  It sounds fine when you're just like, the world's terrible.
[4311.16 --> 4312.40]  Don't do that thing.
[4312.50 --> 4313.24]  And everyone agrees.
[4313.34 --> 4314.60]  And then you, like, try to suggest an alternative.
[4314.76 --> 4316.88]  Everybody's like, go f*** yourself.
[4316.88 --> 4319.76]  And so, it's...
[4319.76 --> 4322.80]  Depends on how far you're walking out, I guess.
[4325.44 --> 4326.74]  I'm going to fall over.
[4329.94 --> 4331.76]  We haven't had a bleep on the show in a while.
[4331.88 --> 4332.92]  So, this is going to be a good one.
[4333.16 --> 4333.48]  Sorry.
[4333.70 --> 4334.02]  Sorry.
[4334.50 --> 4336.06]  I realized I should have inquired at the beginning.
[4336.06 --> 4339.74]  Oh, I mean, Peter, I mean, Peter got his one swear.
[4339.90 --> 4342.86]  So, I feel like you also can get a couple swears in.
[4342.94 --> 4343.18]  Okay.
[4343.60 --> 4343.84]  All right.
[4343.98 --> 4344.08]  Okay.
[4344.62 --> 4346.96]  We're a mostly family-friendly show.
[4347.48 --> 4347.72]  Gotcha.
[4348.12 --> 4348.54]  Noted.
[4348.64 --> 4351.18]  I'll remember for next time.
[4352.30 --> 4352.46]  Yeah.
[4352.46 --> 4355.70]  Thank you, Ian and Sam, for joining us today.
[4355.98 --> 4359.68]  And thank you, Johnny, for being my co-host through this.
[4360.06 --> 4365.22]  And thank you to all the listeners out there for enduring through another episode about maintenance.
[4365.58 --> 4366.52]  There are more to come.
[4366.52 --> 4370.90]  Yes, indeed.
[4371.14 --> 4372.42]  There are more to come.
[4372.54 --> 4376.88]  In fact, there's two more episodes to enjoy on this maintenance series from Chris.
[4377.22 --> 4380.40]  Again, episode 195 and episode 202.
[4380.54 --> 4382.84]  The links for those shows are in the show notes.
[4383.50 --> 4388.34]  Jared and I hope you enjoyed this awesome rebroadcast of GoTime196 as much as we did.
[4388.88 --> 4393.70]  Building actually maintainable software is very hard, as you can tell from all the disagreements,
[4393.70 --> 4396.80]  all the hot takes, and those unpopular opinions.
[4397.36 --> 4401.56]  A big thanks to Chris Brando for kicking off this series, Johnny Borsico for being an awesome
[4401.56 --> 4406.40]  panelist, Ian Lapshire, and Sam Boyer for being awesome guests, and you for listening to
[4406.40 --> 4406.80]  this show.
[4407.06 --> 4407.90]  Thank you so much.
[4407.98 --> 4409.34]  If you enjoyed it, tell a friend.
[4409.48 --> 4411.82]  That helps us reach more people with our podcasts.
[4412.28 --> 4416.28]  Thank you once again to our friends and partners at Fastly and Fly.io.
[4416.74 --> 4419.92]  Also, big thanks to the Beatmaster in residence, Brakemaster Cylinder.
[4420.28 --> 4421.58]  Those beats are banging.
[4421.58 --> 4427.68]  If you haven't yet subscribed to GoTime at GoTime.fm, this show records live on Tuesdays
[4427.68 --> 4428.48]  at 3 p.m.
[4428.50 --> 4429.30]  U.S. Eastern.
[4429.70 --> 4435.22]  Hang and go for slack in the GoTime.fm channel, or watch and listen live at YouTube.com slash
[4435.22 --> 4435.76]  changelog.
[4436.14 --> 4436.56]  That's it.
[4436.60 --> 4437.10]  This show's done.
[4437.18 --> 4438.08]  Thanks again for tuning in.
[4438.40 --> 4439.20]  We'll see you on Monday.
[4439.20 --> 4469.18]  We'll see you on Monday.
[4469.20 --> 4472.70]  findout.
[4472.90 --> 4473.56]  Yeah.
[4473.56 --> 4477.36]  You.
[4477.36 --> 4477.56]  You.
[4477.56 --> 4478.18]  You.
[4478.24 --> 4478.48]  You.
[4478.48 --> 4478.70]  You.
[4478.70 --> 4478.76]  You.
[4478.76 --> 4479.14]  You.
[4480.02 --> 4480.26]  You.
[4480.26 --> 4480.36]  You.
[4480.52 --> 4484.46]  You.
[4484.46 --> 4484.94]  You.
[4484.94 --> 4486.92]  You.
[4487.12 --> 4487.96]  You.
[4487.96 --> 4491.12]  You.
[4491.12 --> 4492.12]  You.
[4492.12 --> 4492.68]  You.
