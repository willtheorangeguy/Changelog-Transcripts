[0.00 --> 8.68]  Welcome to Practical AI.
[9.36 --> 17.14]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing
[17.14 --> 19.58]  the world, this is the show for you.
[20.26 --> 24.96]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.96 --> 30.98]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.98 --> 35.46]  on six continents, so you can launch your app near your users.
[35.86 --> 37.86]  Learn more at fly.io.
[42.74 --> 49.94]  Hello, Jared Santo here, Practical AI's producer and managing editor of all the shows here at
[49.94 --> 50.52]  Changelog.
[50.52 --> 55.22]  Daniel and Chris took this week off, but we didn't want to leave you hanging without
[55.22 --> 59.62]  anything to listen to, so today's episode is going to be a little different than our
[59.62 --> 60.26]  usual fare.
[60.86 --> 66.10]  AI is permeating the entire software industry, so we found ourselves talking about its impact,
[66.34 --> 71.12]  sometimes in practical ways, other times in less practical ways, on many of our pods.
[71.54 --> 74.96]  So today, we are serving you a sampler platter.
[75.08 --> 80.40]  You'll hear a segment from this week's JS Party Podcast, where me and my two co-hosts,
[80.40 --> 86.00]  K-Ball and Nick Neesey, discuss the recently announced Devon project, which is making waves
[86.00 --> 86.96]  in developer land.
[87.14 --> 91.82]  You'll hear a segment from a recent GoTime episode called, How Long Until I Lose My Job
[91.82 --> 98.84]  to AI, where Johnny Borsico and his experienced panel of friends discuss using CodeGen AI to
[98.84 --> 101.54]  augment your dev skills instead of replacing you.
[101.54 --> 106.36]  And finally, you'll hear a segment from the Changelog, where my co-host, Adam Stokowiak,
[106.48 --> 108.30]  and I talk to José Valim.
[108.62 --> 113.58]  José is the creator of the Elixir programming language, and he's been a guest here on Practical
[113.58 --> 116.30]  AI in the Past, talking about Elixir AI tooling.
[116.64 --> 121.66]  Today, you'll hear us question him regarding Elixir's place in a world increasingly influenced
[121.66 --> 126.58]  by large language models and how he thinks about it as a language author and promoter.
[126.58 --> 131.10]  Hopefully, there's a little something for everyone on this episode, and if it's not
[131.10 --> 134.54]  approaching AI from a perspective that's compelling to you, don't worry.
[134.92 --> 138.88]  Your regularly scheduled programming with Chris and Daniel will be back next week.
[139.28 --> 141.60]  Okay, first up, it's JS Party and Devon.
[141.60 --> 141.62]  Let's go.
[161.08 --> 162.68]  There's some news that's good.
[162.78 --> 165.70]  There's also some news that's maybe bad, maybe good.
[166.00 --> 166.60]  I don't know.
[166.60 --> 171.94]  The thing that everybody's talking about this week, at least as we record, and last week
[171.94 --> 173.94]  as well, is Devon.
[174.22 --> 176.86]  Devon, D-E-V-I-N.
[177.34 --> 185.82]  The first AI software engineer, according to the makers of Devon, which is Cognition Labs,
[186.68 --> 193.38]  a new company which raised a Series A led by Founders Fund, headed up by Scott Wu, who seems
[193.38 --> 197.64]  to be a very intelligent person, even from a young age, if you watch that video of him
[197.64 --> 201.96]  doing math very quickly at ages when it seems like you shouldn't know math very quickly.
[202.80 --> 207.92]  And they got a demo out there of this new AI software engineer.
[208.20 --> 209.68]  So I could say more.
[209.80 --> 210.78]  I'll stop right there.
[211.00 --> 216.30]  You all have probably seen the demo, Cable and Nick, or at least heard about what's going
[216.30 --> 216.54]  on.
[216.54 --> 223.50]  This is a new tool which can start from scratch and do some cool stuff.
[223.60 --> 224.52]  I'll just leave it there for now.
[224.70 --> 226.50]  We can talk about the details.
[226.72 --> 231.58]  If you're excited, you too can pay for the right to have a software engineer that can only
[231.58 --> 237.78]  fix one in seven of your tickets and spin up lots of new ways for AWS to charge you money
[237.78 --> 238.82]  without your oversight.
[239.20 --> 240.60]  Sounds like an intern.
[240.78 --> 241.12]  No, just kidding.
[242.34 --> 243.26]  Sounds nice.
[243.26 --> 244.72]  What are you referring to?
[244.84 --> 247.56]  Or is this some specific things that Devin's been up to?
[248.34 --> 250.84]  So high level, there's a couple of things that I'm referring to here.
[250.94 --> 253.86]  So one is they're pumping up the marketing on that.
[253.90 --> 255.22]  This is a standalone software.
[255.36 --> 256.56]  Why get a coding assistant?
[256.68 --> 258.36]  Get something that can go and do your software.
[258.98 --> 261.18]  And they publish some data on it.
[261.38 --> 268.10]  And it does do better than the state of the art in terms of tackling going from a GitHub
[268.10 --> 272.66]  issue to, OK, I'm going to actually solve this implemented change and get it to happen.
[272.66 --> 280.10]  But the number they published, I think, was 13.86% of issues unresolved.
[280.20 --> 281.38]  So that's about one in seven.
[281.98 --> 286.62]  So you pointed at a list of issues and it can independently go and solve one in seven.
[287.62 --> 292.40]  And first off, to me, I'm like, that is not an independent software developer.
[292.40 --> 299.74]  Like that's and furthermore, I find myself asking if its success rate is one in seven.
[299.84 --> 301.58]  How do you know which one?
[302.00 --> 302.42]  Right.
[302.44 --> 307.12]  Like are the other six those it just got stuck or is it submitted something broken?
[307.36 --> 307.80]  Right.
[307.84 --> 312.24]  Because if it sets up something broken that doesn't actually solve the issue, not only do
[312.24 --> 316.28]  you have it only actually solving one in seven, but you've added load because you have to go
[316.28 --> 321.18]  and debug and figure out which things are broken and like like you have a whole bunch of additional
[321.18 --> 321.50]  load.
[321.62 --> 327.26]  So like I think the marketing stance there is a little over the top relative to what's
[327.26 --> 327.84]  being delivered.
[328.20 --> 332.88]  The other thing and this is around, I think, a part of what they do is, oh, it can spin
[332.88 --> 333.88]  up resources for you.
[333.88 --> 334.22]  Right.
[334.26 --> 337.98]  And they show this cool demo of like you pointed at this thing and it allocates a bunch of
[337.98 --> 340.30]  different production resources for you.
[340.30 --> 348.64]  And the person who's handled DevOps in me before and now the, you know, engineering leader who
[348.64 --> 355.36]  has to sign up off on our DigitalOcean or AWS or Google Cloud or whatever expenditures you
[355.36 --> 361.04]  might have looks at that and is terrified by I'm going to give an LLM, which is known for
[361.04 --> 366.02]  hallucination, which is, you know, these things are not you have to design application and
[366.02 --> 369.98]  I'm building applications, but you have to design around their unpredictability and their
[369.98 --> 370.82]  willingness to lie.
[371.42 --> 375.18]  And I'm going to give that raw access to spinning up resources in my cloud.
[375.64 --> 379.10]  Like that sounds, well, it sounds like something I would not sign up for.
[379.22 --> 379.74]  I'll say that.
[380.08 --> 380.18]  Okay.
[380.44 --> 380.64]  Okay.
[380.64 --> 387.56]  Well, let he whose success rate at issues that is greater than one in seven cast the first
[387.56 --> 387.84]  stone.
[388.00 --> 392.62]  I was wondering how, what Nick's ratio is over there, you know, like one in seven sounds
[392.62 --> 394.02]  about the way I would do.
[394.10 --> 395.42]  I'd pull off the easiest one first.
[395.52 --> 399.54]  Does Devin know what the easy tickets look like, you know, cause that's the skill right there.
[399.98 --> 402.78]  I'm over here counting on my fingers trying to see if I'm within that ratio.
[404.18 --> 408.84]  But do you know when you fail or do you just throw out broken code and you're like, eh,
[408.98 --> 409.70]  here you go.
[410.18 --> 413.38]  It's, it's more of a question of, do I know when I succeed?
[413.54 --> 414.14]  I guess.
[414.50 --> 414.86]  Right.
[414.96 --> 416.00]  Which is, yeah, same thing.
[416.48 --> 419.82]  You think you succeeded until you find out later that actually you failed.
[419.82 --> 422.00]  You know, that's, that's been my experience.
[422.64 --> 426.10]  Or you succeeded under the constraints that you put yourself under, right?
[426.12 --> 430.26]  Or that was actually specified in the ticket itself, but you actually failed at some other
[430.26 --> 435.22]  unnamed, unlisted constraints that were unknown at the time, but are obviously clearly there
[435.22 --> 435.92]  in production.
[435.92 --> 437.62]  And so in that context, you failed.
[437.62 --> 439.90]  So it's not easy.
[440.24 --> 442.14]  It's not easy to succeed in this world.
[442.48 --> 443.48]  Well, what about a cable?
[443.66 --> 449.06]  What if you, can't you point Devin at like a $5 a month digital ocean and say, you know,
[449.06 --> 451.98]  deploy to this and like, can't you cap your risk?
[451.98 --> 454.06]  I guess on the, on the DevOps side.
[454.16 --> 454.44]  Probably.
[454.64 --> 455.76]  You probably can.
[455.76 --> 461.88]  And like, I do want, so I'm taking a hard skeptic stance on particularly the claim that
[461.88 --> 463.66]  this is an AI software engineer.
[463.84 --> 466.62]  Like don't hire a person, use this thing.
[466.74 --> 467.76]  And this is their claim.
[467.84 --> 473.30]  So I think it's fair for you to be that harsh on them because they say, meet Devin, the world's
[473.30 --> 477.48]  first fully autonomous AI software engineer.
[477.92 --> 479.24]  That's a very bold claim.
[479.40 --> 481.66]  So I think it's fair that you're being that harsh.
[481.78 --> 482.04]  Go ahead.
[482.24 --> 483.52]  They're showing some cool stuff.
[483.52 --> 486.96]  It looks like a pretty interesting tool to put in the hands of someone who knows what
[486.96 --> 491.04]  they're doing and is able to validate it and is able to say, okay, go and solve this,
[491.04 --> 497.62]  you know, relatively well-constrained problem where I can easily validate the correctness
[497.62 --> 498.28]  of your output.
[498.58 --> 502.52]  Go at the sandbox where I know that you're not spinning up massive amounts of resources
[502.52 --> 507.26]  in a way that I'm going to regret, or even go at this non-sandbox situation.
[507.42 --> 511.98]  But I can, I have the knowledge to check what you did, look at the logs and be like,
[512.04 --> 512.82]  yeah, that's okay.
[512.82 --> 514.76]  Those are really cool things.
[514.86 --> 516.00]  That could be really valuable.
[516.28 --> 518.42]  That could dramatically increase somebody's productivity.
[519.48 --> 524.28]  And those are so far from being something that I would trust independently to replace
[524.28 --> 527.12]  a software developer that they're not even in the same country.
[527.58 --> 529.84]  Like maybe not even in the same world.
[530.12 --> 532.52]  Like these are just completely different claims.
[533.04 --> 533.16]  Yeah.
[533.16 --> 540.64]  I think that the sensationalism of this comes from not what it can do now, but what it represents
[540.64 --> 546.04]  and the progress that it's made when comparing to other things like whatever it was comparing
[546.04 --> 550.74]  that, you know, 13% to, to other AI chat things that can do things.
[551.14 --> 552.92]  It's way better than all of those.
[553.02 --> 558.86]  It still sucks compared to a human, but it's made like monumental progress in terms of AI.
[558.86 --> 562.36]  And I guess the question is, does that continue?
[562.82 --> 564.06]  Can it get further than that?
[564.22 --> 566.10]  Or will it reach some kind of limit?
[566.60 --> 570.12]  And then the other piece of it, I think just from a marketing thing, and I'll be honest,
[570.18 --> 574.80]  the only thing I've seen on it really is a, uh, a fire ship video is that it's, it's already
[574.80 --> 576.14]  doing some work on Upwork.
[576.14 --> 580.84]  So in a way, like that's a marketing claim that they, it competes against real humans
[580.84 --> 581.68]  for jobs.
[582.06 --> 582.46]  Truth.
[583.10 --> 587.12]  According to them, I haven't confirmed, but what you said is true that they say that.
[587.24 --> 587.40]  Yes.
[587.58 --> 591.78]  So this is a struggle with it, with all of the LLM world right now and all of the AI world.
[591.78 --> 594.16]  Cause on the one hand you get it.
[594.24 --> 597.08]  We, we have been in a place where we're in the rapid part of an S curve.
[597.36 --> 603.08]  There have been some very rapid advancements in the core capabilities of these things.
[603.08 --> 608.32]  And they are super freaking cool, like really cool.
[608.60 --> 611.32]  And also they have a lot of limitations.
[611.62 --> 615.70]  A lot of those limitations are baked into the architecture that's being used.
[615.96 --> 621.62]  And so you get kind of a situation where like, there's a bunch of people doing really cool
[621.62 --> 626.84]  stuff with this and like figuring, trying to figure out what it's good for, but it demos
[626.84 --> 632.00]  way better than it does anything reliably in production because you can get a really cool
[632.00 --> 637.94]  outcome, you know, 40% of the time, some situations, 70% of the time.
[638.06 --> 641.92]  And like you show that and people like, Oh my gosh, this is going to take over the world.
[642.60 --> 649.70]  And I would not trust a, for example, AI software engineer that even that they could handle 70%
[649.70 --> 653.84]  of my tickets, but 30% of the time spins up millions of dollars of costs for me.
[654.24 --> 654.64]  Right.
[654.64 --> 655.66]  Or like other things.
[656.12 --> 662.50]  And once again, like, I'm not trying to take away from the technology, but I don't think
[662.50 --> 666.82]  these hyperbolic claims actually serve anyone except for getting attention.
[667.06 --> 668.06]  They get attention.
[668.28 --> 668.90]  Okay, great.
[669.00 --> 672.40]  And you're going to get a whole bunch of people who buy this thing are disappointed.
[672.58 --> 674.92]  If it costs them a bunch of money, they'll sue your ass off.
[674.92 --> 677.36]  And like, why would you do that to yourself?
[678.16 --> 683.48]  It's somewhat similar to generative AI in the image.
[683.68 --> 690.96]  Let's just stick with like static image world where everywhere you see is impressive results.
[691.46 --> 695.62]  And they'll be like this new, like mid journey seven is off the charts.
[695.78 --> 696.10]  Amazing.
[696.30 --> 698.56]  Here's nine examples that'll blow your mind.
[698.66 --> 698.96]  Right.
[699.40 --> 702.28]  And if you click through on that, they're all going to be very impressive.
[702.28 --> 707.38]  Like those are amazing things, but then you have to stop and think, well, mid journey
[707.38 --> 708.70]  didn't create nine examples.
[709.26 --> 710.30]  That blew my mind.
[710.42 --> 713.64]  Mid journey probably created 40, 50, maybe 500 examples.
[713.92 --> 717.36]  And then you human decided which ones were amazing.
[717.80 --> 720.06]  And you cherry pick those out as the examples.
[720.06 --> 724.46]  And like, that's a great team work guys, right?
[724.52 --> 727.20]  Computers plus humans equals better results.
[728.00 --> 729.92]  And so there's the cherry pick.
[729.92 --> 733.02]  And that's what code review on these things will be.
[733.14 --> 736.52]  That's what happens when you tell Copilot, no, I did not want that function.
[736.86 --> 736.98]  Right.
[737.30 --> 741.32]  It's all as Hipster Brown calls it in the chat room, human in the loop.
[741.74 --> 744.18]  And that's exactly what is necessary.
[744.44 --> 751.10]  And I think the reason why you call them hyperbolic claims, K-Ball, is because they're saying it's
[751.10 --> 754.86]  a fully autonomous AI software engineer, human out of the loop, let it rip.
[754.86 --> 759.26]  And maybe fans of the bear will like to say, let it rip.
[759.34 --> 763.96]  But those of us who aren't fans of Devin are thinking, let's not let it rip too much because
[763.96 --> 765.92]  it might just tear the whole thing down.
[766.02 --> 766.96]  Now I'm being hyperbolic.
[767.16 --> 767.94]  Nick, you're nodding along.
[768.00 --> 768.58]  Do you agree with me?
[769.06 --> 769.30]  Somewhat.
[769.40 --> 769.62]  Yeah.
[769.80 --> 775.26]  I think like, yeah, it's humans who are deciding what is good out of that and kind of helping
[775.26 --> 777.12]  to train that going forward.
[777.12 --> 780.60]  But in a way, like I was trying to think and trying to relate this to another article I
[780.60 --> 785.72]  saw that wasn't about Devin specifically, but was about like prompt engineering as a
[785.72 --> 792.08]  quote unquote profession being taken over already by AI because an AI can iterate and more quickly
[792.08 --> 798.18]  come up with a way to answer the questions that you want by appending exactly what it wants
[798.18 --> 799.56]  to hear at the end of a string.
[799.62 --> 804.02]  And I think the example that I heard from that was like, we want you to answer this question
[804.02 --> 810.42]  and it, the AI is quote unquote incentivized to answer it a little bit better if you put
[810.42 --> 811.86]  it into a scenario that it likes.
[812.02 --> 816.92]  So the AI is Captain Kirk on the Enterprise and it has to answer this question to save
[816.92 --> 818.24]  a planet from whatever.
[818.24 --> 821.82]  And the question could be what's two plus two or something like something really simple.
[822.36 --> 827.56]  And by putting in all of these extra prompt words that the AI is coming up with on its
[827.56 --> 831.34]  own, it's making better results overall.
[831.34 --> 836.66]  And I'm just wondering how that marries to the idea of humans being the ones who curate
[836.66 --> 838.84]  the, the good ideas that come out of it.
[839.30 --> 843.52]  Well, prompt engineering, I've been convinced by Swix that it's a code smell.
[843.68 --> 844.16]  Yeah.
[844.50 --> 849.06]  Like we, I was, at first I was convinced like this is the new thing that everybody needs
[849.06 --> 849.54]  to learn.
[849.70 --> 855.12]  And I think it's just the, a leaky abstraction that's we're currently dealing with as humans
[855.12 --> 859.30]  because the tooling is not good enough so that we have to engineer the prompts.
[859.30 --> 863.34]  I mean, Google's search box is prompt engineering, right?
[863.36 --> 865.62]  Like knowing how to Google is, it's the exact same thing.
[865.62 --> 866.78]  It's just way harder.
[867.02 --> 871.38]  And it's like way more magical now to like tell it the magical incantations to get the
[871.38 --> 872.28]  best results back out.
[872.52 --> 877.24]  And so the fact that it knows what results are better to me is not intelligence or anything.
[877.24 --> 879.74]  It's just like, we just need that to go away.
[879.74 --> 884.44]  And I think that's, I think Devin's actually an example of where they've productized and
[884.44 --> 889.60]  hidden a lot of the innards that we've currently been exposed to in order to make the tool work
[889.60 --> 892.38]  better than it would for an inexperienced user to use it.
[892.42 --> 894.10]  Like they've actually turned it into a product.
[894.28 --> 895.28]  And I think that's great.
[895.50 --> 901.22]  I think it's one step on a long line of iterative improvements that will make it so that prompt
[901.22 --> 907.40]  engineering, I mean, you're just going to basically talk to it in layman's terms and it will know
[907.40 --> 912.14]  how to feed itself the correct prompt, so to speak, in order to get the, to get the goodness
[912.14 --> 912.44]  out.
[912.54 --> 913.92]  But I don't know.
[914.68 --> 914.82]  Okay.
[914.82 --> 915.86]  Well, back to you.
[916.34 --> 916.46]  Yeah.
[916.52 --> 921.76]  I mean, I think so the high level on all of this AI stuff is there's really cool stuff
[921.76 --> 922.04]  there.
[922.46 --> 924.06]  We're figuring out how to use it.
[924.52 --> 927.50]  And the current state is, is clearly intermediate.
[928.18 --> 933.66]  However, the thing I want to keep coming back to with this is like, there are things that
[933.66 --> 937.28]  it's like, okay, this technology is immature and we're going to evolve around it.
[937.28 --> 940.82]  And, you know, figuring out how we handle prompts and managing prompts and what's generating
[940.82 --> 943.56]  them and whatever, like that, that fits well in that bucket.
[943.86 --> 948.34]  And there are things that are fundamental pieces of the way the technology is designed,
[948.48 --> 948.68]  right?
[949.70 --> 955.66]  LLMs, machine learning models in general are statistical, probabilistic.
[955.96 --> 959.88]  They, they're very different than most things you think about in software where you're trying
[959.88 --> 962.58]  to make something that is logical, consistent.
[962.58 --> 965.16]  Like you could put a in, you get B out.
[965.28 --> 967.50]  And that is not there with these things.
[967.86 --> 971.28]  And so you can design applications around that.
[971.60 --> 978.52]  And there were things that you can do to, to sort of pin that down, to add validation
[978.52 --> 980.80]  that is outside of the LLM and do other things.
[980.80 --> 982.68]  And maybe Devin is doing that.
[982.68 --> 988.24]  But I think the more we start looking at these sort of, you know, places that require judgment,
[988.40 --> 993.58]  places that require precision, places that like, if you just make some random up, it can
[993.58 --> 994.76]  cause a lot of problems.
[995.02 --> 999.80]  Like those are not actually like, there's a fundamental thing about what the technology
[999.80 --> 1000.38]  does.
[1000.38 --> 1003.46]  That means it's not necessarily going to be a good building block for that.
[1003.46 --> 1009.48]  And so making hyperbolic promises about where it's going to develop that depend on it being
[1009.48 --> 1013.88]  a fundamentally different technology than what it is, feel like they are setting yourself
[1013.88 --> 1015.10]  up for a lot of heartbreak.
[1015.68 --> 1016.48]  What about the job market?
[1016.58 --> 1022.16]  Do you think it's fundamentally affected by tools like Devin as they progress over the
[1022.16 --> 1023.22]  next three to five years?
[1023.40 --> 1025.60]  Because we're not talking about humans out of the loop.
[1025.66 --> 1031.28]  I think we're all in agreement here that that's not feasible or smart, at least in today's
[1031.28 --> 1036.08]  technology plateau of LLMs, but less humans in the loop.
[1036.80 --> 1041.48]  You know, that seems like it's very feasible if these tools continue to iterate and even
[1041.48 --> 1046.06]  just not have revolution, but evolutionary advancements from here.
[1046.90 --> 1046.92]  Yeah.
[1047.02 --> 1050.96]  If it makes me three to five times faster, do we need three to five times fewer engineers?
[1051.28 --> 1051.44]  Yeah.
[1051.76 --> 1057.62]  I mean, I think there is, so this is a technology that has the potential to dramatically impact
[1057.62 --> 1059.18]  the productivity of software engineers.
[1059.18 --> 1064.26]  And I think there's a couple of different things around that as we think.
[1064.38 --> 1067.24]  So short term, that can create some disruption, right?
[1067.68 --> 1072.70]  Short term, that means that a company that had been running on, say, five engineers and
[1072.70 --> 1076.62]  might have needed to hire and expand to 15, now they don't have to expand nearly as soon
[1076.62 --> 1077.64]  and things like that.
[1078.38 --> 1082.16]  So I think there is the potential for relatively short term disruption.
[1082.72 --> 1088.12]  I will say both the history of economics broadly and software in particular is that every
[1088.12 --> 1093.68]  time we make it easier to code, we discover there are whole worlds now that we can address
[1093.68 --> 1095.58]  and build software around that we couldn't before.
[1096.22 --> 1100.46]  So if, for example, and this actually, there's a particular example of this that I think is
[1100.46 --> 1101.36]  interesting to dive into.
[1101.54 --> 1108.24]  So one of the big economic challenges in the tech industry in the last four or five years
[1108.24 --> 1113.10]  is that we had these massive tech companies with incredibly high revenue per employee.
[1113.72 --> 1118.42]  Google, Meta, Netflix, like the Fangs mostly, right?
[1118.60 --> 1122.50]  And so they were able to set the salary bar that was super high.
[1122.74 --> 1124.94]  They were paying ridiculous amounts of money.
[1125.32 --> 1126.44]  That's a technical term.
[1126.76 --> 1127.24]  Ridiculous.
[1127.48 --> 1128.70]  For software engineers.
[1128.70 --> 1135.50]  And then when we had very low interest rates and a ton of VC money flowing in to the industry,
[1135.50 --> 1142.96]  there were lots of companies whose fundamental business economics do not support that level
[1142.96 --> 1149.18]  of salary per software engineer who were nevertheless paying that amount of salary per software engineer
[1149.18 --> 1150.24]  based on VC capital.
[1150.62 --> 1154.48]  And sort of this thesis that, okay, we'll be able to scale out of this and we'll get whatever.
[1154.48 --> 1158.62]  And I think that caused a lot of distortions and problems in the field.
[1159.28 --> 1162.88]  Now, if suddenly software engineers are three to five times more productive,
[1163.46 --> 1172.50]  the range of businesses that could use software but previously could not afford to compete with the Fangs,
[1172.58 --> 1177.24]  et cetera, of the world, there's a whole set of business models in there that become viable
[1177.24 --> 1180.18]  because it's that much cheaper to develop software.
[1180.18 --> 1188.06]  And so I could imagine this actually dramatically expanding the number of viable either software businesses
[1188.06 --> 1193.66]  or businesses that are non-tech but would like to include software or could have custom software
[1193.66 --> 1196.64]  and dramatically expanding the number of those that happen.
[1196.76 --> 1202.44]  So I think long term, I don't think it's a negative impact on the software engineering career path.
[1202.58 --> 1206.38]  I think that what it means to be a software engineer looks a little bit different
[1206.38 --> 1208.24]  when you have different types of tooling.
[1208.24 --> 1211.74]  That has been true as long as I've been around.
[1212.00 --> 1214.76]  Like I've just JavaScript land, right?
[1214.78 --> 1216.64]  I remember when jQuery was a revelation.
[1217.28 --> 1218.62]  Oh my gosh.
[1218.96 --> 1221.20]  This is going to make me so much more productive.
[1221.50 --> 1223.28]  It did make me so much more productive.
[1223.48 --> 1224.56]  All these other different things.
[1225.02 --> 1228.06]  And now the level of tooling that we have there that supports our productivity,
[1228.22 --> 1230.10]  building things in the front end is astronomical.
[1230.44 --> 1232.62]  And has that taken away from the number of people writing JavaScript?
[1232.62 --> 1238.28]  Speaking of astronomical, Astro has a new database.
[1238.38 --> 1239.20]  Moving on.
[1251.38 --> 1252.54]  What's up, friends?
[1252.70 --> 1256.58]  Is your code getting dragged down by joins and long query times?
[1257.04 --> 1259.20]  The problem might be your database.
[1259.20 --> 1262.22]  Try simplifying the complex with graphs.
[1262.70 --> 1266.28]  A graph database lets you model data the way it looks in the real world,
[1266.42 --> 1268.90]  instead of forcing it into rows and columns.
[1269.32 --> 1272.76]  Stop asking relational databases to do more than what they were made for.
[1273.26 --> 1277.34]  Graphs work well for use cases with lots of data connections like supply chain,
[1277.62 --> 1280.90]  fraud detection, real-time analytics, and generative AI.
[1281.46 --> 1285.68]  With Neo4j, you can code in your favorite programming language and against any driver.
[1285.92 --> 1288.50]  Plus, it's easy to integrate into your tech stack.
[1288.50 --> 1291.16]  People are solving some of the world's biggest problems with graphs.
[1291.52 --> 1292.26]  And now it's your turn.
[1292.54 --> 1295.62]  Visit neo4j.com slash developer to get started.
[1296.02 --> 1299.48]  Again, neo4j.com slash developer.
[1299.80 --> 1304.36]  That's n-e-o-4-j dot com slash developer.
[1304.36 --> 1314.66]  Up next, we have a GoTime podcast fireside chat between longtime programmers Kent Quirk,
[1314.96 --> 1318.60]  Sharon Diorio, Stephen Pyle, and host Johnny Borsico.
[1318.60 --> 1320.60]  GoTime.com slash developer.
[1320.60 --> 1321.60]  GoTime.com slash developer.
[1321.60 --> 1322.10]  GoTime.com slash developer.
[1322.10 --> 1329.16]  It's one thing to have Jan AI, you know, pump out snippets of code that is part of a larger whole, right?
[1329.20 --> 1330.52]  Whereby I'm the engineer.
[1330.78 --> 1332.76]  I am engineering a solution.
[1332.76 --> 1337.62]  I'm not just a code monkey just clacking out, you know, syntax.
[1338.00 --> 1339.64]  I'm trying to fix a problem.
[1339.84 --> 1342.22]  I'm engineering a solution to a business problem.
[1342.80 --> 1345.90]  Now, I could go, you know, as high level as I can.
[1345.98 --> 1350.34]  I can just open up, you know, Copilot in chat mode and say, hey, this is what I'm trying to accomplish.
[1350.68 --> 1352.62]  Start spitting out, you know, files, right?
[1353.04 --> 1357.66]  Now, maybe today, right, it can build somewhat trivial apps.
[1357.66 --> 1362.84]  I've seen YouTube videos and clips and things of it spitting out entire working React apps and all these things.
[1362.88 --> 1363.78]  And that's great.
[1364.30 --> 1367.24]  And I think over time, it's going to come even better at doing those things.
[1367.24 --> 1374.70]  But I have a hard time trying to sort of correlate that or trying to replace solution building.
[1374.88 --> 1378.72]  Because to me, solutions aren't static, right?
[1378.80 --> 1383.86]  When a business comes to me and says, hey, I need you to build a solution to this problem.
[1384.62 --> 1385.70]  I build it.
[1386.16 --> 1387.98]  They take it into production.
[1388.12 --> 1388.96]  They do stuff with it.
[1389.00 --> 1390.58]  And they come back and says, hey, you know what?
[1390.60 --> 1391.40]  This is great.
[1391.80 --> 1394.04]  Now, I need to change it in this way.
[1394.40 --> 1397.04]  Or I need to account for this exception.
[1397.24 --> 1400.52]  I need to account for this particular use case or this specific customer.
[1400.66 --> 1403.52]  Where 90% of the time, it works like this way for every customer of this type.
[1403.84 --> 1405.26]  But for this customer of that type.
[1405.34 --> 1409.80]  But on Ultimate Thursdays during the phone, it does this completely different thing.
[1410.10 --> 1410.36]  Exactly.
[1410.98 --> 1417.66]  So now, how are we supposed to treat those entirely made-up solutions?
[1418.22 --> 1425.48]  Am I just feeding that back into the system and saying, hey, so now I account for these alternative approaches?
[1425.48 --> 1432.24]  Is it going to be like it was when the first generated code frameworks started hitting the scene?
[1432.60 --> 1434.54]  And you'd go in and there'd be all this code.
[1434.64 --> 1436.12]  It was like, yes, super fast.
[1436.14 --> 1439.54]  If you had to do an ORM, it'd ruin all the code for you, et cetera.
[1439.64 --> 1441.14]  And then you needed to change something.
[1441.68 --> 1447.18]  And all of a sudden, it was like, you know, change management in some of those days was...
[1447.18 --> 1449.44]  Yeah, or regenerate the whole thing from scratch.
[1449.60 --> 1451.30]  And oh, sorry about all your customization.
[1453.52 --> 1453.92]  Yeah.
[1454.14 --> 1459.12]  So that'll be another big test that AI has not yet proven it can do.
[1459.28 --> 1461.78]  Well, so let's talk about art for a second, though.
[1461.84 --> 1463.54]  Because this is, again, a similar thing.
[1463.62 --> 1464.52]  Like, everybody's real excited.
[1464.62 --> 1467.90]  Look at the images I can generate with, you know, Mid Journey or whatever.
[1468.30 --> 1469.14]  It's stolen art.
[1469.14 --> 1470.08]  Well, right.
[1470.24 --> 1473.74]  But the point is, again, it's going out and giving you the average solution.
[1474.02 --> 1478.14]  It's going out and going, here are the things that look most like what you described that
[1478.14 --> 1479.68]  somebody else has created already.
[1480.12 --> 1482.50]  And we're kind of going to cobble pieces of that together.
[1482.90 --> 1488.14]  Or here's an opinion formed by the loudest voices out there that I sucked up as source data.
[1488.44 --> 1489.50]  Hell yeah.
[1489.50 --> 1499.20]  But, like, I sat in a meeting today where an artist went over her design, basically her design process for a big design project.
[1499.74 --> 1502.82]  Like, here's the resources I looked at.
[1502.96 --> 1506.10]  Here's the, you know, the feeling I was going for.
[1506.18 --> 1507.18]  Here are the things I considered.
[1507.34 --> 1508.42]  I looked at these typefaces.
[1508.54 --> 1513.98]  This typeface reminded me of this, you know, building architecture, which is relevant to the site.
[1513.98 --> 1524.92]  You know, and then that artist proceeded to churn out, over the course of a couple of months, 200 pieces of support art for an event.
[1525.48 --> 1539.72]  That was a brilliant design exercise by somebody deeply steeped in art and creation who then studied the event and what the event needed and integrated all that.
[1539.72 --> 1545.34]  And, yes, some random person could have sat down with Mid Journey and said, make me this stuff.
[1545.96 --> 1548.84]  And it would have been much less good.
[1550.48 --> 1554.30]  But people who don't know the difference would have been, sure, it looks fine.
[1554.62 --> 1556.32]  You know, I mean, we've all seen that, right?
[1556.42 --> 1561.80]  You know, my document has 37 fonts and 12 colors, but it looks fine to me.
[1561.80 --> 1568.66]  But, like, there's a big difference between, you know, something crafted and something just slapped together.
[1569.14 --> 1573.64]  And, yeah, I guess I think that AI is going to make it easier to slap together.
[1574.72 --> 1576.94]  But for most people, though, would you argue?
[1577.16 --> 1578.58]  So here's what I'm not saying.
[1578.62 --> 1582.34]  I'm not saying that these things generated by AI.
[1582.34 --> 1596.50]  Like, if you're a connoisseur of a particular art, you know, you're an architect of a particular kind of application or solution or, you know, or thing, whatever it is, you can critique, right, the output of Gen AI as it stands today.
[1596.64 --> 1599.22]  Again, arguably, it's going to get better at what it does, right?
[1599.48 --> 1603.02]  But you can critique the output today and be like, this is subpar, right?
[1603.04 --> 1605.76]  This is not as good as what I could have come up with.
[1606.04 --> 1609.56]  But for most people, it's good enough.
[1610.10 --> 1611.26]  It depends on what they're using it for.
[1611.26 --> 1615.72]  And so, again, if you're just doing something for yourself, who the hell cares?
[1615.90 --> 1619.20]  I mean, yeah, I'll slap something together out of two by fours if I'm building it for my garage.
[1619.34 --> 1619.84]  I don't care.
[1620.68 --> 1627.74]  But if I'm going to sell it, if I'm going to make a business around it, that's the part where I'm saying I don't think the AI stuff is there.
[1627.90 --> 1638.68]  If you're just doing a hacky project for personal use, yeah, I mean, maybe you would have had to pay somebody to come in and slap that shelf together in your garage if you didn't have the skills to do it yourself.
[1638.68 --> 1644.74]  And so now there's this kind of, you know, yes, there's a few things that I couldn't do before that now I can do today for myself.
[1645.24 --> 1648.26]  Design that invitation for my kid's birthday party.
[1648.76 --> 1649.18]  Hell yeah.
[1651.24 --> 1653.10]  I can't draw, but I can use an AI.
[1653.76 --> 1655.00]  There's nothing wrong with that.
[1655.00 --> 1660.62]  And, you know, so, yeah, there's probably some, you know, the kid next door, you're not paying 20 bucks to do that for you.
[1660.86 --> 1661.62]  But that's now.
[1661.84 --> 1665.00]  What happens in, you know, in the future as AI evolves and improves?
[1665.82 --> 1671.12]  So, you know, do we get to this uncanny valley level of like, oh, now it's not just good enough.
[1671.22 --> 1671.54]  It's like.
[1671.62 --> 1672.70]  It's like the standard.
[1672.96 --> 1674.24]  Now it's building your whole kitchen.
[1674.60 --> 1674.88]  Right.
[1675.56 --> 1676.92]  Do we need to worry about that?
[1676.92 --> 1684.28]  And how much coding out there is most of what's out, you know, how many cruds have we ever created in our lives?
[1684.86 --> 1686.68]  How many cruds are still being created every day?
[1687.28 --> 1687.50]  Yeah.
[1687.58 --> 1687.90]  Okay.
[1688.02 --> 1691.90]  So that's a problem that's largely been solved greater or lesser degree.
[1692.22 --> 1692.32]  But.
[1692.58 --> 1692.68]  Yeah.
[1692.70 --> 1693.94]  I mean, it's white box, right?
[1693.96 --> 1695.42]  You make white box easy to do.
[1695.42 --> 1695.90]  Yeah.
[1696.16 --> 1708.64]  And tech has always been making things that had gates around them or real or created limited availability or and making them more available.
[1708.64 --> 1712.86]  Like artisan things that used to be only certain artisans could do that.
[1712.86 --> 1716.28]  Only musical artists had a studio and an audio engineer.
[1716.90 --> 1722.58]  And now they can go and, you know, create their own tracks with one app at home.
[1722.58 --> 1725.74]  For me, that's the part that's like, oh, I can't complain.
[1725.84 --> 1734.22]  I can't be the curmudgeon complaining about this latest thing that might make something that I do more accessible to other people.
[1734.42 --> 1737.42]  Like I've benefited from these other things that came along.
[1737.82 --> 1738.96]  It's time to share the wealth.
[1739.48 --> 1740.18]  I don't want to.
[1740.40 --> 1741.90]  I'm really rooting against it.
[1744.06 --> 1744.54]  Yeah.
[1744.82 --> 1746.58]  I don't think it's about gatekeeping.
[1746.58 --> 1753.38]  I mean, I'm not like I feel like a big chunk of my career has been spent trying to help people learn to program.
[1753.98 --> 1760.64]  And so I'm not thinking that the reason I'm skeptical is because I don't want other people to do what I do.
[1760.78 --> 1767.52]  I think it's more because I feel like the hype and the reality are distinct.
[1767.52 --> 1773.58]  I think that what the reality is producing is mostly devoid of creativity.
[1774.02 --> 1778.80]  People are confusing knowing what to look up with being creative.
[1779.44 --> 1783.62]  And I think knowing what to look up is a skill and a lot of us have it.
[1783.86 --> 1785.70]  And the better engineers, I think, are better at it.
[1785.84 --> 1789.32]  And so, yes, AI helps to ease that problem.
[1789.32 --> 1809.62]  But knowing what to even ask about, you know, like or looking at a new solution to a problem, that's something that I think is well beyond what AI is capable of now or in the reasonably like the LLM model, I think, is fundamentally non-creative.
[1809.70 --> 1811.08]  That's my take on it.
[1811.60 --> 1812.20]  Spicy.
[1813.02 --> 1817.16]  We're not at the unpopular opinions yet.
[1817.16 --> 1829.08]  So one thing you mentioned, like the whole teaching, like y'all remember when maybe it was during maybe first or second Obama term or something, but there was this giant push to teach everybody how to code.
[1829.52 --> 1829.70]  Right.
[1829.98 --> 1831.10]  Like it was it was everywhere.
[1831.20 --> 1832.02]  It was in the media.
[1832.18 --> 1833.02]  It was in newspapers.
[1833.16 --> 1836.72]  It was like, you know, we need to teach our young how to program.
[1837.14 --> 1846.86]  Now I'm looking at a clip from, you know, NVIDIA CEO like three or four days ago or something saying, hey, people shouldn't learn how to program.
[1847.16 --> 1850.62]  You should now let, you know, the new programming language is a human language.
[1850.84 --> 1852.88]  I'm thinking, man, you are sitting here.
[1853.14 --> 1856.80]  You stand to gain billions of bajillion dollars.
[1856.80 --> 1857.12]  Right.
[1857.38 --> 1861.76]  If your wish comes to it, because you're producing, you know, chips and stuff for these things.
[1861.80 --> 1862.98]  Of course, you're going to say that.
[1863.02 --> 1863.20]  Right.
[1863.26 --> 1863.62]  So this.
[1863.98 --> 1865.32]  So I mean, what?
[1865.38 --> 1868.06]  I'm definitely not on the don't teach people how to program camp.
[1868.30 --> 1868.88]  No, no.
[1869.42 --> 1871.92]  I'm going to I'm going to take a slightly spicy take here.
[1871.92 --> 1877.98]  I don't think he's completely off now in the time we've all been engineers.
[1878.10 --> 1885.70]  We've seen waves of different things that are going to come and take our jobs, you know, offshoring and, you know, code generation now AI.
[1886.20 --> 1887.36]  And they haven't.
[1887.36 --> 1893.96]  And my theory is that the key thing that an engineer has is the ability to communicate.
[1893.96 --> 1905.60]  And even when you're supposed to be communicating to people on the other side, product, the business, whatever affectionate term you use for them, aren't always as good at that.
[1905.98 --> 1907.44]  Although it should be part of their job.
[1907.44 --> 1918.26]  But having somebody who can think back and forth, there will, I think, always be a need for those people because every every CEO thinks they have the answer to every question.
[1920.06 --> 1921.12]  That's what they need to do.
[1922.18 --> 1922.58]  Right.
[1922.58 --> 1924.30]  But they really shouldn't.
[1924.36 --> 1929.24]  If they have a business that's big enough to grow, their biggest skill is finding the people and put in the right place.
[1930.00 --> 1940.72]  So if your job right now is like doing creds for a company that can't even explain what they want, I wouldn't worry because they're not going to be able to explain what they want to AI.
[1941.16 --> 1941.30]  Right.
[1941.60 --> 1941.72]  Yeah.
[1941.76 --> 1942.82]  No, it's the thinking logic.
[1943.04 --> 1943.36]  It's yeah.
[1943.44 --> 1946.80]  There's the think about break something down into steps and think logically.
[1946.80 --> 1956.64]  Like I once did have a client very early in my career who was a pretty good business person who really wanted to automate his business.
[1956.64 --> 1959.54]  And he was able to sit down and explain it to me.
[1959.54 --> 1966.08]  Like if he had had the tools to program, he could have written his own code because he thought about it really logically.
[1966.08 --> 1973.26]  And it was just my job to basically take dictation and turn it into Pascal for him back in the day.
[1973.26 --> 1977.56]  But that's few and far between.
[1978.24 --> 1983.50]  You know, quite honestly, most people who specialize in business aren't specializing in thinking logically.
[1983.96 --> 1987.36]  They specialize in thinking about people and like you said about communications.
[1988.08 --> 1990.78]  So does AI then make you more what you already are?
[1991.12 --> 1992.64]  If you're a logical thinker, you'll benefit.
[1993.06 --> 1994.86]  And if you're not, you still struggle?
[1996.38 --> 1998.22]  And who gets to train the agent?
[1998.22 --> 2002.56]  I want to be in the training side.
[2002.80 --> 2006.68]  I want to be the one doing the building of the things that you use.
[2007.38 --> 2007.52]  Right.
[2007.76 --> 2008.16]  Fascinating.
[2008.16 --> 2009.80]  That's a good question.
[2010.34 --> 2014.96]  I think at the point where it comes to like a personal AI, where it's just like, it's tuned to you.
[2015.62 --> 2017.02]  Your data doesn't get shared.
[2017.84 --> 2021.00]  It's just, you know, then it becomes like a superpower, right?
[2021.08 --> 2023.34]  You can just, it's like you're co-pilot.
[2023.34 --> 2027.10]  But how would that work if it's only got your data?
[2027.50 --> 2030.40]  It's basically replicating to a point you.
[2030.76 --> 2034.18]  There's a generic, it's trained on the universe.
[2034.76 --> 2035.08]  Right.
[2035.20 --> 2036.64]  And then specialized for you.
[2036.66 --> 2036.90]  Right.
[2037.12 --> 2039.14]  Is the way that we're seeing all of this.
[2039.74 --> 2044.00]  It's like creating your own GPT, but it's based on the larger model, right?
[2044.48 --> 2045.00]  Yeah, exactly.
[2045.00 --> 2051.00]  So, I mean, like my company, we built, we have a query engine that looks like SQL.
[2051.74 --> 2066.38]  And then we built an AI where we train that AI, like as part of a prompt, we basically can go out and get your data and all the names of your fields and the data types of your fields.
[2066.38 --> 2078.32]  And we can plug them into the AI query so that when you say, show me my slowest service, it can go, all right, what are the fields that are named according to, you know, time, duration?
[2078.60 --> 2080.54]  And what are the things that look like a service name?
[2081.02 --> 2085.82]  And now I can write a query for you so it knows how to query Honeycomb.
[2085.82 --> 2095.82]  And then it can write that query for you from your inept prompt because it's been specialized for that particular type of application.
[2096.08 --> 2097.68]  And I think that's a really cool use of AI.
[2098.26 --> 2101.88]  That is a productivity boost for people who are already technical.
[2102.20 --> 2105.88]  Like, you know, full disclosure, my startup is a Honeycomb customer.
[2106.40 --> 2111.26]  So, you know, I will go in the dashboard and I can formulate those queries.
[2111.26 --> 2122.06]  But I'm already a highly technical user who knows how to use these kinds of tools to get and know exactly what kind of data I'm looking for and when I've found it.
[2122.54 --> 2139.46]  Now, for the layperson, right, who doesn't know, like the layperson, like the more I think about it, the more I'm thinking, okay, if I'm a, on one end of the spectrum, you have the complete layperson who is using perhaps, you know, chat GPT or something like it.
[2139.46 --> 2148.18]  To maybe generate copy and not hiring a copyright person like you might traditionally do back in the day, right?
[2148.32 --> 2158.82]  I'm sure the copywriters of the world are suffering right now because content creators, you know, like content is like, yeah, content creators are suffering because this stuff is now being generated.
[2159.04 --> 2160.36]  So are all our Google searches.
[2160.84 --> 2161.04]  Right.
[2161.04 --> 2161.52]  Right.
[2161.66 --> 2165.96]  So if that was your job, absolutely you're impacted.
[2166.24 --> 2166.40]  Right.
[2166.42 --> 2175.06]  And the layperson can now bypass you and get to something that, again, the good enough, right, they can get something good enough to achieve some means.
[2175.06 --> 2175.30]  Right.
[2176.00 --> 2180.62]  On the complete opposite end of the spectrum, you have people who engineer software.
[2180.98 --> 2181.46]  Right.
[2181.46 --> 2186.92]  That, again, given the context of the conversation, we're talking about like how safe is our jobs.
[2187.00 --> 2187.20]  Right.
[2187.36 --> 2198.36]  And so when I'm asking this question, I'm not asking, is the layperson going to find ways of reducing, right, their reliance on sort of, I don't want to say lower skill, just the different kind of skill.
[2198.66 --> 2199.02]  Right.
[2199.02 --> 2199.06]  Right.
[2199.14 --> 2207.52]  I'm thinking like for people like us, as software engineers who presumably will be impacted by this to some degree.
[2207.74 --> 2207.92]  Right.
[2208.26 --> 2208.98]  And we already are.
[2209.02 --> 2209.16]  Right.
[2209.26 --> 2220.86]  For us, there's also the micro spectrum whereby if you're on the sort of the lower end of that spectrum and if the only thing we are doing is generating crud, well, I'm sorry, your job is indeed in jeopardy.
[2220.86 --> 2222.36]  If that's the only thing you've been doing.
[2222.36 --> 2222.78]  Right.
[2222.88 --> 2223.58]  With your career.
[2223.58 --> 2235.72]  On the opposite side of it is the highly specialized person who understands a business problem has to debug and troubleshoot and talk to people and integrate different things.
[2235.86 --> 2237.14]  And institutional knowledge.
[2237.30 --> 2237.60]  Right.
[2237.70 --> 2238.22]  All that stuff.
[2238.32 --> 2240.48]  I mean, I don't see that skill.
[2240.72 --> 2241.02]  Right.
[2241.56 --> 2244.50]  I don't see that being replaced by AI anytime soon.
[2244.88 --> 2246.24]  Am I wrong here?
[2246.84 --> 2248.16]  I don't think so.
[2248.42 --> 2248.94]  Personally.
[2248.94 --> 2250.86]  How many of those people do we need?
[2251.20 --> 2252.50]  And that's the thing, right?
[2252.50 --> 2254.46]  I mean, is it a game of musical chairs?
[2254.56 --> 2256.00]  We should be looking for our chair now.
[2256.46 --> 2256.76]  No.
[2256.86 --> 2261.96]  Any business is thinking, do I need a thousand engineers, right, when 500 will do?
[2262.26 --> 2266.04]  I mean, I think, as we've all said, right, it makes us more productive today.
[2266.20 --> 2271.76]  So I'm writing more lines of code per day than I was five years ago.
[2272.02 --> 2272.42]  Right.
[2272.54 --> 2272.88]  Right.
[2273.08 --> 2273.34]  Right.
[2273.34 --> 2273.52]  Right.
[2273.52 --> 2274.40]  So that's good.
[2274.88 --> 2278.86]  You know, but we all kind of expect productivity to continue to rise.
[2278.96 --> 2280.50]  So this is a productivity tool.
[2281.12 --> 2281.42]  Mm-hmm.
[2281.42 --> 2283.16]  Not a replacement tool.
[2283.26 --> 2287.78]  You know, we're also using languages that are more expressive than they were.
[2288.22 --> 2298.60]  You know, like the code I write in Go is probably one third the length of the same code I write in C++ or used to write in C++ back in the day.
[2299.08 --> 2301.44]  So that's also a productivity boost at some level.
[2301.44 --> 2307.94]  At least if you believe the old metrics that it's basically you can write the same number of lines of code per day no matter what language you write it in.
[2307.94 --> 2316.60]  But I think actually knowing how to use it is a skill to put on your resume, but not before too long, or if not now.
[2316.94 --> 2327.74]  I mean, even if I didn't want to use it, I would because it's becoming of like, it's going to be a point where like, oh, you know, I use Copilot all the time.
[2327.74 --> 2328.32]  Oh, good.
[2328.62 --> 2331.36]  You have a point for you to get the job.
[2331.56 --> 2333.90]  Is prompt engineering I know already in your Lincoln profile?
[2335.06 --> 2336.02]  It's going to be soon.
[2337.56 --> 2342.64]  No, but if you put it in your interests as AI, it shows up in the keyword searches.
[2342.64 --> 2343.22]  Oh, there you go.
[2343.42 --> 2343.66]  Right?
[2343.66 --> 2345.72]  Nice.
[2346.20 --> 2347.22]  I mean, that's a good point.
[2347.36 --> 2349.84]  But to me, it's like back to my woodworking thing.
[2349.94 --> 2352.40]  It's like, I know how to use a power saw.
[2352.56 --> 2353.62]  I know how to use a drill press.
[2353.70 --> 2354.62]  I know how to use a lathe.
[2354.94 --> 2358.04]  You know, those are kind of expected.
[2358.72 --> 2364.60]  Today, if I'm going to do woodworking and say I only use hand tools, people are going to look at me like, I don't have time for you.
[2364.72 --> 2365.14]  Same thing.
[2365.14 --> 2369.54]  And the same is true of like, if you're not using Copilot, what am I paying you per hour?
[2369.54 --> 2369.90]  What are you doing?
[2370.18 --> 2373.72]  You know, why are you not as productive as you could be?
[2373.98 --> 2374.12]  Yeah.
[2374.32 --> 2383.40]  I think at this point, the only people who really aren't using it are people who are doing like very arcane languages or people who their businesses, they don't allow it.
[2383.42 --> 2384.48]  Their company doesn't allow it.
[2384.94 --> 2386.18]  I think everybody else has at least tried it.
[2386.18 --> 2398.76]  I mean, if you're a company that doesn't allow such things, like I understand not bringing sort of open source code into your organization that might be the wrong licensing model for you or something like that.
[2398.80 --> 2398.94]  Right.
[2399.28 --> 2400.72]  You don't want to be in some hot water.
[2401.12 --> 2404.86]  All you have to do is look at, you know, Oracle and Google over the whole Java thing.
[2405.02 --> 2406.48]  I think those are the companies involved.
[2406.48 --> 2422.08]  But if you allow your engineers to use a model where you can control the kinds of things that were used in the model, right, for the training, and you can have maybe you can run your own internal, right, Gen AI for code generation, whatever it is.
[2422.50 --> 2422.78]  Right.
[2423.00 --> 2432.06]  I think if you're an organization that is afraid of these things, you should at least follow that route as opposed to saying, hey, nobody can use any Gen AI coding tools whatsoever.
[2432.06 --> 2434.90]  Because I think you're going to lose people if you do that.
[2435.04 --> 2442.06]  Because I'm going to look at my peers that get to use these things and they're learning those skills, right?
[2442.28 --> 2448.08]  And then now I'm falling behind because everybody's using, you know, some sort of code generation tool and I'm not, right?
[2448.38 --> 2448.70]  I mean.
[2449.10 --> 2461.24]  This is where I hope somebody reaches out to somebody who hears this and reaches out and can answer that question of like, can you have a copy of Copilot that you train on a specified set of repos?
[2461.24 --> 2463.16]  And only those repos.
[2463.50 --> 2464.12]  Private repos.
[2464.64 --> 2470.98]  Well, I mean, I would, you know, as we joked, I mean, if I'm a Go developer, I'm training it on Johnny's code.
[2472.00 --> 2473.78]  Because if I don't like it, I can yell at Johnny.
[2474.72 --> 2474.74]  But.
[2475.72 --> 2476.04]  Nice.
[2476.44 --> 2477.26]  I don't know what I mean.
[2477.30 --> 2478.18]  There's people out there.
[2478.44 --> 2479.42]  One neck to choke.
[2479.50 --> 2479.90]  I get it.
[2479.96 --> 2480.42]  I get it.
[2480.52 --> 2482.62]  It doesn't matter what language it is.
[2482.64 --> 2487.12]  There's people out there that you respect their code and you'd be like, yes, I would like my code to be more like this.
[2487.12 --> 2491.62]  I wish it would learn that that's what I was thinking or that's the way this problem should be thought about.
[2492.28 --> 2496.08]  I mean, yes, there's precious few of those people and those people will probably never lose their jobs.
[2496.54 --> 2501.06]  But for the rest of them, you're mortals that are going to have to work with the tools that are out there.
[2501.18 --> 2508.22]  And I would love to, if this is a possibility now that you could train Copilot on what you'd say to train it on and not all of GitHub.
[2508.68 --> 2511.10]  I think there are companies that are working on that product.
[2511.10 --> 2514.48]  I feel like I've even seen a product announcement like it.
[2514.94 --> 2524.50]  But yeah, I mean, you know, the thing about it is you can take one of these LLMs and you can essentially subset it and you can make a tiny compact LLM that will run in a box that you can actually stand on your desktop.
[2525.06 --> 2528.02]  And then you can further train that with new information.
[2528.52 --> 2530.78]  So that's exactly what you want to do here.
[2530.84 --> 2539.06]  You want to take a coding-centric LLM, like a Copilot, and create the mini version of it and then train it on your repositories.
[2539.06 --> 2543.18]  And now it knows how to write your code and it's also not talking out to the cloud while you're doing it.
[2543.46 --> 2545.84]  So there's got to be businesses like that if there are.
[2545.84 --> 2549.28]  And this is where we redact all of this and put it into our business plan.
[2558.90 --> 2559.80]  What's up, friends?
[2559.92 --> 2562.54]  There's a new book out there called The Hacker Mindset.
[2562.54 --> 2572.60]  This is a productivity cheat code to unlock new levels of success in your career, in your creative pursuits, and in your personal growth.
[2573.00 --> 2579.40]  This book is about leveraging the principles of white hat hacking and applying those skills to the broader world.
[2579.82 --> 2583.76]  It's available for pre-order right now and is not your typical productivity guide.
[2584.02 --> 2590.22]  This is written by Garrett G., a seasoned white hat hacker with over 20 years of experience.
[2590.22 --> 2597.06]  This book reveals the secrets of hacking and how you can apply those skills to overcome obstacles and achieve your goals.
[2597.50 --> 2601.20]  So don't miss your chance to get ahead and get this book, The Hacker Mindset.
[2601.58 --> 2605.90]  You can pre-order your copy today at thehackermindset.com.
[2606.16 --> 2610.84]  Be among the first of many to tap into this power of hacking for your success.
[2611.26 --> 2614.00]  Join the movement and embrace a new way of thinking.
[2614.40 --> 2617.80]  Again, that's thehackermindset.com.
[2617.80 --> 2632.70]  Last up, we have José Valim, creator of the Elixir programming language on Changelog and Friends.
[2633.00 --> 2636.66]  That is our talk show flavor of the Changelog podcast.
[2636.66 --> 2648.18]  To Jared's point earlier, AI, as it's known today, GPT, ChatGPT, and others are not that good with assisting with Elixir programming.
[2649.30 --> 2652.34]  And so I guess the question is, what does it take to make it good?
[2652.56 --> 2653.88]  You mentioned embeddings earlier.
[2654.06 --> 2657.32]  You mentioned documentation being more readily available.
[2657.68 --> 2663.70]  What does it take from a, I guess, a leader in the Elixir world to enable LLMs to be better?
[2663.70 --> 2677.84]  Like, what role do you play in that journey for them to better consume the documentation and better know how to programming in Elixir to help folks like Jared and myself or our team or others to really become better and more proficient at Elixir?
[2678.16 --> 2685.02]  Versus just like anytime Jared asks ChatGPT for assistance, it's just like, no, it's not good.
[2685.08 --> 2685.92]  So just quit.
[2685.92 --> 2699.66]  You know, so I think if I got the question right, I think we did our work correctly in the sense that at least from the language point of view, in the sense that like documentation was always first class.
[2700.40 --> 2703.10]  So documentation is very easy to access.
[2703.10 --> 2713.46]  So if what you want to do is to like configure an LLM, it's actually very easy to access that programmatically, send that, extract information.
[2714.36 --> 2721.52]  And we talked about like one of the things that you also have to do is like try to get understanding from the source code.
[2721.74 --> 2726.96]  So you can find, oh, this code is using those modules, is importing those things.
[2727.14 --> 2730.18]  And those are things that you can do relatively easily in Elixir.
[2730.66 --> 2732.36]  We can most likely improve that.
[2732.36 --> 2736.28]  So I feel like we have the knife and the cheese.
[2737.38 --> 2743.68]  It's just a matter of somebody going and like cutting the cheese, you know, it's yeah.
[2743.80 --> 2749.68]  I feel like the foundation is there in terms of like having this information structured, but somebody needs to feed it somewhere.
[2750.10 --> 2758.40]  But again, we can go back like maybe it's a corporate size, like maybe ChatGPT like indexed HexPM already.
[2758.84 --> 2759.62]  Not sure.
[2759.86 --> 2760.10]  Right.
[2760.28 --> 2761.18]  Maybe it has done that.
[2761.18 --> 2761.64]  But I don't know.
[2761.70 --> 2764.34]  I don't know if I can send a letter to somebody.
[2764.46 --> 2766.62]  Hey, please index my website.
[2767.28 --> 2768.64]  Or maybe it's a matter of.
[2768.94 --> 2779.02]  So one of the things is that Redmonk, they have, they release twice a year, like kind of a graph plotting GitHub against Stack Overflow.
[2779.02 --> 2784.02]  And I think they're having like the most popular languages according to GitHub and Stack Overflow.
[2784.40 --> 2788.06]  And then there's like a, you know, a linear thing in the middle.
[2788.28 --> 2793.68]  And it's very funny because Elixir is high on the GitHub side, but quite low on the Stack Overflow side.
[2793.68 --> 2799.82]  And one of the reasons for that is because we have always had the Elixir forum.
[2799.82 --> 2803.40]  So that may be one of the things.
[2803.76 --> 2804.62]  Where's the knowledge?
[2805.04 --> 2806.38]  Where's the back and forth in the community?
[2806.38 --> 2806.60]  Yeah.
[2806.66 --> 2807.88]  The knowledge is in the forum.
[2808.04 --> 2809.52]  Is that thing being indexed?
[2809.60 --> 2811.26]  Because we know Stack Overflow is.
[2812.00 --> 2812.22]  Right?
[2812.32 --> 2812.52]  Yeah.
[2812.52 --> 2827.56]  And so, and ironically, that's one of the reasons I think I may be misquoting that Redmonk, they are considering removing Stack Overflow from their plots because it's prone, like I think it has been losing relevance in the last years.
[2828.00 --> 2828.34]  Right?
[2828.72 --> 2840.24]  But, you know, maybe in the effort of trying to have a closer community where everybody can engage with each other, when I'm active in the forum, and I'll probably not have this patience if I was dealing with Stack Overflow.
[2840.86 --> 2841.18]  Right?
[2841.18 --> 2845.38]  We created our community at a special place, but it's not known.
[2845.88 --> 2846.78]  So, yeah.
[2846.88 --> 2862.28]  So I think it's still like too many unknowns, but I think at the core, we unwillingly did a good job because we were worried about documentation being accessible, documentation being first class.
[2862.80 --> 2868.72]  So we did that, and that can be, and we promote people to write documentation, lots of documentation.
[2869.36 --> 2869.62]  Right?
[2869.62 --> 2871.70]  So there is a lot there.
[2872.26 --> 2876.76]  And yeah, and maybe the RAG is going to be the thing that is going to be enough.
[2877.20 --> 2878.38]  That's one of the hopes, right?
[2878.44 --> 2881.38]  Going back to, oh, we want everybody to be able to use this.
[2881.52 --> 2888.44]  If RAG is good enough, then a lot of people would be able to augment their ecosystems without depending on OpenAI or whatever.
[2888.44 --> 2890.44]  But we are still evaluating.
[2890.44 --> 2903.20]  When we talked about sort of the long-term future of Elixir, artificial intelligence, and that sort of larger topic of how long will we be relevant and can AI generate it well, that whole conversation.
[2903.20 --> 2910.94]  This makes me think of this necessity to not have a black box that is whatever AI is.
[2910.94 --> 2928.06]  Because just like you said, who do I send a letter to to index my stuff so that my very relevant language today remains relevant tomorrow because tomorrow says AI will continue to be more and more relevant to developers in their journey to develop.
[2928.30 --> 2928.52]  Right?
[2928.52 --> 2928.56]  Right.
[2929.12 --> 2930.72]  So who do we send a letter to?
[2930.78 --> 2931.26]  How do we know?
[2931.34 --> 2936.08]  Well, currently, the status quo of AI is for the most part a black box.
[2936.08 --> 2942.40]  Obviously, open source LLMs and indexes have become more and more pushed because of this challenge.
[2942.40 --> 2953.92]  But I think this illustrates and highlights really the long-term challenge because even you can't say for sure why what wasn't indexed was indexed for the Elixir corpus.
[2954.12 --> 2970.82]  Whether that's the forums, whether that's the documentation through hex documentation or whatever, it's unclear to someone like you how to enable chat GPT or the likes to better support Elixir assistance for developers using those things to use as tooling.
[2971.10 --> 2972.18]  And that's just not cool.
[2972.40 --> 2981.78]  Because long-term, we need to have inroads into those places so that we can be part of the future if AI is predicting how we'll get to the future.
[2982.26 --> 2982.40]  Yeah.
[2982.48 --> 2984.70]  And I think, yeah, it's too early.
[2984.78 --> 2986.00]  I think we're going to improve a lot.
[2986.00 --> 2999.30]  I was listening to a podcast today where Sam Altman, he was saying like, they improved chat GPT 3 about 40 in the orders of magnitude in terms of size, performance and things like that since they started.
[2999.30 --> 3002.94]  I think 10 times for chat GPT 3 and a half.
[3003.58 --> 3008.74]  And I think open source is going to catch up, I think.
[3008.82 --> 3010.50]  And I think that's the hope.
[3010.96 --> 3017.62]  But yeah, it's also like we go back to this when we are thinking about Livebook because what I want is for open source to win.
[3017.62 --> 3025.16]  But when I'm building a feature for Livebook, I need to build the best feature for the users.
[3025.16 --> 3034.98]  And when I can use chat GPT 4 and I can immediately see the results and they're really, really good.
[3035.52 --> 3037.52]  I can use other tools off the shelf.
[3037.86 --> 3038.72]  They're not as good.
[3039.32 --> 3041.64]  So we are a small company.
[3041.74 --> 3042.68]  We are doing open source.
[3042.68 --> 3052.66]  So my options, if I have to choose for my users, is going to be chat GPT 4 because it gives me the best result for the least amount of effort.
[3052.90 --> 3053.04]  Right.
[3053.12 --> 3054.16]  I just it's there.
[3054.62 --> 3060.38]  And this is like so we were back and like about my indecision about investing this stuff is that because I want open source.
[3060.54 --> 3060.72]  Right.
[3060.78 --> 3062.08]  I want things to be open source.
[3062.58 --> 3067.50]  But right now, the quickest return of investment is GPT.
[3067.50 --> 3069.50]  And then I am in this contradiction space.
[3070.68 --> 3070.88]  Right.
[3070.88 --> 3074.48]  But yeah, and it's just I think it's just patience.
[3074.62 --> 3075.60]  We have to be patient.
[3076.38 --> 3082.78]  And, you know, I think probably in one year and the whole thing is like it's crazy to think about is that this thing has been happening for a year only.
[3083.00 --> 3083.18]  Right.
[3083.22 --> 3088.48]  It appears that this thing has been out for so long, but it's a year.
[3088.56 --> 3093.66]  And I think like if I'm back on the show in a year, we may potentially be having a very different conversation.
[3094.06 --> 3095.20]  So, yeah, we'll see.
[3095.68 --> 3097.02]  Do you have any fear about this?
[3097.02 --> 3102.44]  It's like even as you respond to that, you sort of had some I wouldn't say like trepidation in your voice, but you sort of had some uncertainty.
[3102.56 --> 3106.90]  Do you have any like fear and uncertainty and doubt the FUD that people sort of pass around?
[3106.94 --> 3108.00]  Do you have any fear about this?
[3108.00 --> 3118.18]  No, not really in the sense that I consider myself like very lucky, very fortunate or whatever or blessed, whatever you want to say it.
[3118.52 --> 3126.58]  I think maybe it's a I'm not being overconfident here, but more like thankful that I think whatever happens to me, it's going to be fine.
[3126.58 --> 3135.44]  I truly believe that what's going to make Alexer survive is the community more, you know, than whatever technological changes.
[3135.52 --> 3138.06]  Unless there is something very drastic.
[3138.20 --> 3140.90]  I talked to my father about this, about investments.
[3141.18 --> 3141.30]  Right.
[3141.40 --> 3143.88]  So like when Bitcoin wasn't crazy.
[3144.26 --> 3144.48]  Right.
[3144.62 --> 3152.08]  And then my father is like, oh, have you heard like about this thing that if you put your money there, like people got this huge return.
[3152.08 --> 3158.10]  And then I always told him, father, if we got to know about it, it's because it's too late.
[3158.72 --> 3161.88]  You know, it's like or if something happens.
[3161.88 --> 3162.18]  Right.
[3162.20 --> 3169.62]  It's like, oh, father, like if something happens is because like if something goes this bad, it's because it's going to be bad for everybody.
[3169.88 --> 3171.60]  So like don't try to fight it.
[3171.60 --> 3171.76]  Right.
[3172.04 --> 3175.70]  So again, like unless there is a very major change, I think I will be fine.
[3176.24 --> 3176.58]  Right.
[3176.70 --> 3182.06]  So I'm not worried about me in the sense I always think more about it's more about ideals.
[3182.40 --> 3187.74]  You know, again, like I like to say, well, me 10 years ago, that's where my trepidation is.
[3187.86 --> 3194.60]  If things go like close source, you know, and those things, they happen by we don't see the results.
[3194.60 --> 3199.80]  Like I think another polemic topic about this, it's like, hey, I use Chrome.
[3199.80 --> 3203.32]  As soon as Chrome came out, I today I don't use Chrome anymore.
[3203.74 --> 3207.16]  But as soon as Chrome came out, I immediately swapped to Chrome.
[3207.56 --> 3207.74]  Right.
[3207.74 --> 3207.78]  Right.
[3208.50 --> 3218.58]  And if I had known that this would lead to a point where, you know, Google is in this position where it has a lot of control over the browser, over the web.
[3218.58 --> 3218.96]  Right.
[3218.96 --> 3226.78]  And over how we use the internet, like 10 years ago, I would probably not have used Chrome if I could have seen it.
[3227.12 --> 3227.36]  Right.
[3227.52 --> 3234.56]  Or so I think I think that's where my trepidation comes from of like things being close source, like the developer experience.
[3234.56 --> 3247.10]  So today, another example today, like Elixir was the first programming language that GitHub had like the new navigation code navigation things that were provided by the community.
[3247.40 --> 3247.92]  Right.
[3247.92 --> 3254.98]  So there were some programming languages, and there still are, where they have very good navigation and exploration on GitHub UI.
[3255.88 --> 3267.34]  And the path for that, to get that feature, to get that behavior was, and I'm very welcome that, I'm very thankful that the GitHub team, they, you know, they discuss with us and allow us to do that.
[3267.48 --> 3268.58]  But that's close source.
[3269.00 --> 3269.22]  Right.
[3269.22 --> 3273.78]  And GitHub plays a major role over, you know, how developers use.
[3274.18 --> 3274.30]  Right.
[3274.36 --> 3284.34]  So it all comes back to this idea of like, if you want to provide a good experience for your users, how much of that is behind something closed source that you have no control?
[3284.58 --> 3298.62]  And you are depending on somebody, you know, paying attention to you, like, or you having a contact or, you know, me having a name because I was very active in the Rails community that GitHub uses like 10 years ago.
[3298.62 --> 3299.22]  Right.
[3299.26 --> 3304.92]  Those are the things that, but I, like, I feel lucky, you know, but it worries me.
[3305.00 --> 3305.20]  Right.
[3305.26 --> 3307.36]  Like, how much is being closed?
[3307.76 --> 3308.10]  Right.
[3308.14 --> 3310.90]  How much is going to be out of our control?
[3311.12 --> 3317.96]  And then the trepidation, I guess, is like, what does that matter for the small Jose out there?
[3318.02 --> 3318.28]  Right.
[3318.40 --> 3322.60]  That wants to start building his thing today and they won't be able to.
[3324.14 --> 3326.24]  Well, you killed the vibe there, Jose.
[3326.68 --> 3327.52]  Oh, thank you.
[3327.52 --> 3332.84]  Well, you just, that's me at parties, you know, so you killed me at parties.
[3333.92 --> 3334.52]  Not invited.
[3335.50 --> 3336.04]  Just kidding.
[3336.22 --> 3336.92]  Oh, funny.
[3337.46 --> 3337.84]  All right.
[3337.92 --> 3342.52]  Well, let's, should we try to close on an up note, on a high note?
[3343.50 --> 3344.36]  On an upper.
[3345.80 --> 3346.36]  What's that?
[3348.00 --> 3348.36]  Wow.
[3349.08 --> 3349.78]  I had no idea.
[3349.92 --> 3351.80]  I think we should end it right there, Adam, don't you think?
[3351.94 --> 3352.88]  We ended on a high note.
[3352.90 --> 3354.14]  This cheese and knife tactic there.
[3354.24 --> 3354.60]  I love it.
[3354.60 --> 3354.96]  It was.
[3355.36 --> 3356.26]  Do you want higher?
[3356.42 --> 3357.92]  I don't think it would be good for the listeners.
[3358.36 --> 3360.30]  I think that was plenty high enough for me.
[3360.42 --> 3361.56]  Adam, were you satisfied with that?
[3361.58 --> 3363.22]  That was a high note, literally.
[3363.70 --> 3364.04]  Yes.
[3364.04 --> 3365.62]  And I dig it.
[3365.62 --> 3376.80]  Thanks for listening to this very special episode of Practical AI.
[3377.30 --> 3380.38]  These were just extracted segments of much longer conversations.
[3380.98 --> 3386.20]  If you want to hear more, there's a link in your show notes to each of the episodes featured here.
[3386.20 --> 3392.76]  Thanks again to our partners, Fly.io, to our Beat Freakin' Residence, Breakmaster Cylinder, and to our friends at Sentry.
[3393.02 --> 3398.36]  Save yourself 100 bucks on the team plan when you use code CHANGELOG while signing up.
[3398.66 --> 3399.70]  That's all for now.
[3400.02 --> 3402.12]  Chris and Daniel return on the next one.
[3402.12 --> 3425.68]  Take care.
