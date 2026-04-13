[0.00 → 3.14] This is really the core about how people build careers now.
[3.30 → 9.72] If you are thinking about how to get there, you have to build in constant lifelong learning
[9.72 → 10.50] into your process.
[10.50 → 13.04] And if you don't do that, you will fall behind.
[13.16 → 17.68] And as things are moving faster and faster forward, the ability to thrive in a digital
[17.68 → 22.50] world is really crucial to having it because anything you're learning right now in more
[22.50 → 26.90] of a formal context, if you're coming out of school, for instance, a lot of that will
[26.90 → 27.52] be obsolete.
[27.52 → 31.34] The basic math will be there, but the algorithms are going to change.
[31.70 → 34.78] How you're achieving problem solutions will change.
[35.02 → 37.02] And so you really have to be able to do that.
[37.02 → 42.82] I think that is a fundamental for being a digitally literate person in the job world these days.
[45.62 → 48.32] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[48.52 → 49.22] We love Linde.
[49.30 → 50.72] They keep it fast and simple.
[50.86 → 53.22] Check them out at linode.com slash changelog.
[53.44 → 55.50] Our bandwidth is provided by Vastly.
[55.86 → 57.20] Learn more at fastly.com.
[57.20 → 59.42] And get your feature flags powered by Launch Darkly.
[59.68 → 61.38] Get a demo at LaunchDarkly.com.
[61.38 → 66.88] This episode is brought to you by our friends at O'Reilly.
[67.24 → 70.90] Many of you know O'Reilly for their animal tech books and their conferences, but you may
[70.90 → 73.36] not know they have an online learning platform as well.
[73.68 → 78.16] The platform has all their books, all their videos, and all their conference talks.
[78.16 → 83.56] Plus, you can learn by doing with live online training courses and virtual conferences, certification
[83.56 → 88.90] practice exams, and interactive sandboxes and scenarios to practice coding alongside what
[88.90 → 89.34] you're learning.
[89.34 → 95.16] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps,
[95.66 → 101.82] data science, cloud, containers, security, and even soft skills like business management
[101.82 → 103.26] and presentation skills.
[103.38 → 105.16] You name it, it is all in there.
[105.50 → 109.22] If you need to keep your team or yourself up to speed on their tech skills, then check out
[109.22 → 110.64] O'Reilly's online learning platform.
[111.18 → 114.74] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[114.74 → 117.14] Again, O'Reilly.com slash changelog.
[125.96 → 131.72] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[132.08 → 133.02] and accessible to everyone.
[133.38 → 137.42] This is where conversations around AI, machine learning, and data science happen.
[137.80 → 142.16] Join the community and Slack with us around various topics of the show at changelog.com slash
[142.16 → 143.80] community and follow us on Twitter.
[143.94 → 145.54] We're at Practical AI FM.
[151.92 → 154.96] Welcome to another episode of Practical AI.
[155.30 → 156.86] This is Daniel Whiten ack.
[157.00 → 163.02] I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[163.02 → 165.70] Benson, who is a strategist with Lockheed Martin.
[165.92 → 166.54] How are you doing, Chris?
[166.86 → 167.84] I am doing very well.
[167.90 → 168.78] How's it going today, Daniel?
[169.12 → 169.98] It's going good.
[169.98 → 174.64] For listeners who are in the U.S., you'll know that this last week was Memorial Day weekend,
[174.84 → 175.74] which is good.
[175.82 → 176.76] It was a nice long weekend.
[176.86 → 180.92] It's beautiful weather here, but I'm feeling the amount of catch-up I need to do in this
[180.92 → 181.44] short week.
[181.50 → 182.46] I don't know about yourself.
[183.18 → 186.50] No, they give us a holiday, but then the amount of work for that week never changes,
[186.70 → 188.28] so you just have to cram it all in.
[188.54 → 189.76] It's always the same, right?
[189.90 → 190.14] Yeah.
[190.38 → 194.16] I'm feeling it this week, but lots of good stuff to work on.
[194.16 → 199.08] But I'll sleep well over the weekend, I'm sure, and have a nice Saturday to sleep in,
[199.14 → 199.40] hopefully.
[200.10 → 200.90] So there you go.
[200.98 → 202.30] Recovery time this weekend.
[203.56 → 204.98] Recovery time this weekend.
[205.58 → 211.40] One thing is there are a lot of news and updates and AI stuff to catch up on.
[211.40 → 214.96] I know both you and I have probably been feeling that.
[215.10 → 217.66] Lots of things have been happening in the AI world.
[218.48 → 223.42] And so today on our episode, what we're going to do is we're just going to kick it back old
[223.42 → 223.74] school.
[223.96 → 228.50] And as our long-term listeners will know, sometimes Chris and I like to do these episodes where
[228.50 → 234.72] we don't really have a specific guest speaking about a topic, but we kind of talk about a
[234.72 → 239.64] variety of topics that we've seen in the AI ecosystem that we think are interesting,
[239.64 → 242.70] maybe of note, and discuss them here live.
[242.88 → 243.98] So you up for that, Chris?
[244.88 → 245.78] I'm totally up for that.
[245.84 → 247.00] We have fun with these episodes.
[247.14 → 247.74] I enjoy them.
[248.26 → 248.58] Yeah.
[248.80 → 250.42] This is a little free-form for us.
[250.70 → 251.14] Exactly.
[251.38 → 251.58] Yeah.
[251.64 → 256.20] And I'm sure it shows to our listeners how ignorant we are in certain cases, but that's
[256.20 → 256.50] okay.
[256.80 → 261.20] Because as everybody who's exploring this space, everybody has their sort of own little
[261.20 → 262.92] niche sphere of knowledge.
[263.10 → 267.80] And it seems like these other people are very knowledgeable in all of AI, but they just have their
[267.80 → 269.38] own little niche of knowledge too.
[269.38 → 272.74] So it's good to sort of dip our toes into different areas.
[272.88 → 274.24] At least it is for me, I think.
[274.72 → 279.04] You know, that is something that we talked about a little bit in the last episode for
[279.04 → 284.16] anybody that might've been listening was just the fact that there is too much stuff for everyone
[284.16 → 285.02] to know all of it.
[285.56 → 289.50] And so you kind of have to pick and choose where you're going to dive in.
[289.62 → 293.74] And that might be something worth talking about today because you have to kind of make
[293.74 → 294.28] some choices.
[294.28 → 299.94] And it's interesting how the different choices people make affects how a team might come together
[299.94 → 302.40] and what the team's capabilities are and stuff.
[302.54 → 304.14] So there are a lot of ramifications here.
[304.94 → 305.12] Yeah.
[305.28 → 309.88] There's definitely the concept as well of like when you're putting together a data science
[309.88 → 312.16] team or an AI team or something like that.
[312.16 → 313.42] Actually, it's funny.
[313.50 → 317.26] We're actually bringing this up because we had one of these discussions internally, actually,
[317.46 → 323.58] even this week is, hey, what are the advantages of having a sort of organizational, the separate,
[323.58 → 328.66] you know, data science and AI unit versus data science and AI people embedded in various
[328.66 → 330.24] teams throughout the organization?
[330.24 → 334.66] And also within those specific people, of course, there's a slant.
[334.78 → 341.00] Sometimes people sort of want to hire in data science people or AI people to just do the sort
[341.00 → 342.78] of modelling and analysis stuff.
[342.84 → 344.68] And like, don't worry about the other things.
[344.68 → 345.92] Just focus on that stuff.
[345.98 → 351.00] And we'll handle the business logic and like pushing that out into products and all of that
[351.00 → 351.58] stuff.
[351.80 → 356.68] In other cases, people sort of very much like to, you know, there's even this term now full
[356.68 → 360.68] stack data science where it's like, hey, I'm going to take care of doing this analysis
[360.68 → 364.32] piece, but I'm also going to figure out how to integrate it into a product.
[364.88 → 369.12] So there's just so many different parameters there, I think, in terms of how people put
[369.12 → 369.90] their teams together.
[369.90 → 373.60] And it makes it hard for a new person to figure out where they fit in that, I think.
[374.78 → 375.32] It sure does.
[375.32 → 381.44] I mean, not only that, but it doesn't stand by itself in that, you know, AI, if you're thinking
[381.44 → 386.54] of AI as deep learning, which we tend to in these last few years, and it has to be
[386.54 → 391.86] you know, you have the algorithms, you have the need to deploy it out to be useful to
[391.86 → 393.52] your user community.
[393.76 → 398.10] It integrates in with other software, it integrates in with the microservices and the APIs.
[398.84 → 404.34] And so you have a huge area of target surface of things that have to get done.
[404.64 → 407.94] And I have never seen two organizations do it the same way.
[408.04 → 412.00] And the organizations that I've worked with, it's like, yeah, everyone has their own way
[412.00 → 416.52] of doing it, which means there's not a normalized or standardized way to achieve that.
[416.54 → 417.10] Yeah.
[417.10 → 417.54] Yeah.
[417.54 → 417.78] Yeah.
[417.78 → 423.08] And of course, this is something because we have a podcast, or we're, you know, interacting
[423.08 → 424.28] with a lot of different groups.
[424.70 → 430.02] Something that I'm asked a lot is, hey, where, you know, I'm wanting to get into this field.
[430.46 → 432.24] Where do I need to focus?
[432.46 → 436.18] And oftentimes my response to that is, well, let me ask you a question.
[436.18 → 441.06] Like, are you more interested in this sort of, you know, more engineering slant, or are you
[441.06 → 446.04] just wanting to do sort of research type things and analysis and that sort of thing?
[446.12 → 448.92] And because those two could take a very different path.
[449.06 → 453.22] And probably if you're focusing on one, you're not going to be well-prepared for the other
[453.22 → 453.48] one.
[453.54 → 457.02] That's very rare that there's someone that sort of operates in both of those spaces.
[457.24 → 458.18] Yeah, totally.
[458.34 → 458.48] Yeah.
[458.48 → 462.84] It's a super hard challenge to figure out for someone new into it because I always ask
[462.84 → 466.64] people what they're already passionate about, or I ask them what kinds of things are they
[466.64 → 472.10] reading and watching videos on that has captured their imagination and then start building on
[472.10 → 472.48] that.
[472.48 → 476.98] And you can ask five different people and get five very, very different answers, which
[476.98 → 478.60] isn't necessarily a bad thing.
[479.08 → 483.26] You know if they're each gravitating toward different areas that have to be addressed, then
[483.26 → 484.84] that's the making is for a team right there.
[484.84 → 489.94] Yeah, maybe one thing I could suggest promoting my own, you know, biased opinion.
[490.48 → 491.82] I was thinking about this recently.
[492.10 → 495.22] I'm kind of involved to some respect over at Purdue University.
[495.44 → 501.20] Sometimes some of their students help my organization with some projects like practicum type projects,
[501.20 → 505.02] or I help their students in working on projects, or occasionally I teach some lectures.
[505.50 → 509.92] And I was putting together some material for a course this time around.
[509.92 → 516.42] My thought process was really like, for these students, if I was hiring them in, what would
[516.42 → 520.96] be the sort of set of things I would want them to go through or be able to go through
[520.96 → 526.88] that would really give me confidence in their abilities to perform, you know, on my data science
[526.88 → 527.48] or AI team?
[527.60 → 530.24] And so the thing, and you know, you could disagree with this.
[530.50 → 531.62] Like you say, every team's different.
[531.62 → 535.54] But what I did was I said, okay, I proposed a certain problem.
[535.62 → 536.94] The problem was question answering.
[537.54 → 542.10] So, you know, a piece of text comes in, there's a question, you have a model that actually extracts
[542.10 → 543.28] the answer out of the text.
[543.50 → 544.98] And this is a well-known problem.
[544.98 → 549.22] And there are models out there that do this because it's a short time that we have the
[549.22 → 549.86] students together.
[549.86 → 553.04] I was basically saying, Hey, well, this model exists.
[553.04 → 554.94] So figure out how to use it for inference.
[554.94 → 560.54] And then I would like to see three different sort of manifestations of that model.
[560.54 → 565.72] One that I can have a REST API and, you know, send a request and get a response.
[566.32 → 571.40] One where there's a user interface where I type in my question and I type in my passage
[571.40 → 572.86] and get the answer.
[573.02 → 576.66] And one where I can use it in a batch way.
[576.66 → 583.54] So if I want to answer, I have a data set of 20,000, you know, 50,000, 100,000 questions
[583.54 → 585.92] and passages, and I want to answer them all at once.
[586.48 → 589.20] What's a way that I can, you know, do that in a batch sense.
[589.54 → 593.80] And I think through those different sort of manifestations of how a model could
[593.80 → 597.58] operate was really, I think it was actually helpful for me in terms of thinking through,
[597.72 → 602.24] you know, how to structure the material, but also it, you know, I thought it was a good
[602.24 → 605.96] way to think about things and maybe something I'd share on the podcast, because as people
[605.96 → 608.72] are getting into things, they want to sort of show a project or something.
[609.18 → 613.14] And I would encourage people, you know, maybe it's worth, you create a model, but then
[613.14 → 617.72] you create this sort of different manifestations of the model and how it actually interacts
[617.72 → 620.14] with users or the end use case, something like that.
[620.86 → 620.94] Yeah.
[621.64 → 621.90] Yeah.
[622.22 → 624.06] So let me ask you a question about that.
[624.06 → 630.42] Was the model itself fundamentally designed differently or was it more of a software input
[630.42 → 631.08] output thing?
[631.72 → 631.88] Yeah.
[632.06 → 638.98] So the model itself was basically the same in the three cases, although in a more batch sense.
[639.20 → 640.34] I had a feeling you were going there.
[640.34 → 646.72] One thing, of course, you can do is operate on, you know, instead of pushing one input
[646.72 → 650.16] into the model and getting one output and doing that over and over, of course, you can
[650.16 → 654.88] push multiple in, and then you can also parallelize across the data set and all those sorts of
[654.88 → 655.14] things.
[655.14 → 657.74] So there is maybe a different inference pattern.
[658.18 → 661.00] The model architecture itself wouldn't be fundamentally different.
[661.54 → 667.14] I think if there was more time, I would have loved to add a kind of upfront component, which
[667.14 → 672.02] would have been like, fine tune the model, take a pre-trained model, fine tune that model
[672.02 → 677.24] with just a little bit of data for a slightly different task or a slightly different domain,
[677.24 → 681.78] and then sort of make it available in these three different ways.
[682.24 → 687.42] I think, I mean, that's almost the sort of bootcamp in and of itself.
[687.42 → 692.12] If you can sort of go through that process, I think you're really, you're well, you're
[692.12 → 697.56] at least well set up to talk the language and understand how people go about their AI
[697.56 → 698.88] and ML development.
[699.16 → 702.20] And, you know, I'm sure there's people out there that disagree with me.
[703.20 → 703.80] Yeah, yeah.
[703.86 → 707.68] I would argue that that's almost more of an engineering thing than it is truly a modelling
[707.68 → 709.86] thing because your model is not fundamentally changing.
[710.12 → 713.84] It's just how you're choosing to deploy it and integrate it in with the larger software
[713.84 → 714.90] environment that you're in.
[714.90 → 715.34] Yeah.
[715.68 → 721.60] And I would probably go more, I'm naturally more on that engineering side, probably in
[721.60 → 727.06] the way that I operate than I am in the sort of pure research or creating new model architecture
[727.06 → 727.92] side of things.
[728.06 → 733.50] So if someone wants to go then and like to be the next team developing the next cool model
[733.50 → 737.54] that is, you know, fundamentally different and that, you know, they spend five years on
[737.54 → 741.84] that to develop that model and really prove it out and probe all the implications and
[741.84 → 744.18] all of that, that is also really needed.
[744.70 → 748.14] But it's the sort of different skill set around research and experimentation.
[749.14 → 754.16] You know, you raise a fascinating kind of, there's a dimension to this I'd like to draw.
[754.40 → 759.28] And tell me if you have a different sensation about this, but is I'm looking at the deep
[759.28 → 765.86] learning world over the last year or two compared to the years prior to that, that it seems like we were
[765.86 → 773.26] seeing lots of completely new architectures coming through, through the late teens, especially,
[773.82 → 775.48] you know, early in and into the late teens.
[775.48 → 780.02] And then we kind of got into the twenties, and we're really in an age of implementation.
[780.02 → 785.04] I don't know if that's because I'm in my bubble, and I'm seeing tons and tons and tons of
[785.04 → 790.36] implementation, but not a lot of truly revolutionary new ideas coming to market.
[790.36 → 791.80] What is your impression?
[792.12 → 793.66] Am I trapped in my little bubble?
[793.84 → 799.02] Or do you think that we're seeing more implementation than we are research right now because so many
[799.02 → 800.40] more people are getting into deep learning?
[801.38 → 802.38] It's a good question.
[802.64 → 810.00] I think part of it is maybe the maturity of the field in the sense that in maybe previous
[810.00 → 814.66] years, everything seemed a little bit more new because nothing was really normalized yet.
[814.66 → 821.10] It was all this sort of storm of ambiguity and new things, whereas there's, you know, really
[821.10 → 826.60] developed workflows around transfer learning and, you know, even, you know, running really
[826.60 → 829.54] large scale jobs and multiple GPUs and other things.
[829.54 → 833.90] And all of that sort of like people have developed workflows around that.
[834.48 → 839.70] So maybe that those pieces of it seem less new, but I don't know.
[839.70 → 844.92] I don't know if I would say that, you know, the progression of new models and architectures
[844.92 → 846.34] has slowed or increased.
[846.46 → 846.82] I don't know.
[846.90 → 850.12] There's definitely still some of that going on, but the perception may be different.
[851.48 → 855.74] It feels evolutionary at the moment to me because I was really wondering this, knowing that we
[855.74 → 858.02] were going to have this conversation among ourselves.
[858.12 → 863.14] I was coming into it, thinking about it and going, when's the last time I saw a completely
[863.14 → 867.96] new architecture sweep through the market and really take hold?
[867.96 → 872.72] You know, like, you know, back when we were looking at, you know, the sweep of convolutional
[872.72 → 878.32] neural networks, and then we hit the age of NLP really hitting a stride, followed immediately
[878.32 → 880.64] by another big jump with transformers.
[880.78 → 885.04] And then we've seen reinforcement learning have some jumps in there as well.
[885.26 → 891.24] And I was thinking, hmm, when's the last time one of those big, big jumps leapt out at
[891.24 → 891.40] us?
[891.46 → 892.96] Can you think of what that might've been?
[893.16 → 896.34] What would you think of as the most recent big jump forward?
[896.34 → 897.86] I don't know.
[897.98 → 901.52] I'm also pretty stuck in my little NLP bubble, maybe.
[902.22 → 906.88] So obviously transformers and large scale language models have been the thing.
[907.06 → 907.54] Your bread and butter.
[907.66 → 908.26] Yeah, definitely.
[908.52 → 911.08] That have really pushed the envelope forward.
[911.24 → 913.80] But that really has happened over the past few years.
[914.00 → 914.26] Yes.
[914.34 → 919.28] There is one thing I'd like to discuss in a bit that I think we can decide if it's new
[919.28 → 920.96] or not in that sense of new.
[921.04 → 922.12] It's new, but yeah.
[922.40 → 922.94] I don't know.
[922.94 → 925.90] I definitely think that there's more people getting into the field.
[926.66 → 931.02] And because of the tooling and the maturity of the tooling, there's more people that are
[931.02 → 936.52] able to do very advanced and sophisticated things, whereas maybe that was restricted to a very
[936.52 → 937.40] elite before.
[937.40 → 945.80] This episode is brought to you by Snowplow Analytics.
[946.32 → 950.14] Snowplow is the behavioural data management platform for data teams.
[950.52 → 956.28] Maximize the value of your behavioural data using Snowplow Insights, a managed data platform
[956.28 → 961.12] that's built on leading open source tech leveraged by tens of thousands of users.
[961.60 → 966.16] Capture and process high quality behavioural data from all your platforms and your products
[966.16 → 968.78] and deliver that data to your cloud destination of choice.
[969.12 → 973.58] When marketing needs to make data-informed decisions, when product needs next-level understanding,
[973.96 → 978.54] and when analytics needs rich and accurate data, Snowplow is the solution for data teams
[978.54 → 983.48] who want to manage the collection, processing, and warehousing of data across all their platforms
[983.48 → 984.10] and products.
[984.44 → 988.52] Get started and experience Snowplow data for yourself at SnowplowAnalytics.com.
[988.86 → 991.42] Again, SnowplowAnalytics.com.
[991.42 → 1010.98] Chris, you were kind of bringing up this topic of like new architectures and like what is
[1010.98 → 1017.58] a big leap in terms of new kind of models and what is like building on the shoulders
[1017.58 → 1018.80] of things before.
[1019.04 → 1021.86] And to some degree, I mean, everything's building on things from before.
[1022.56 → 1029.92] But one of the things that I've really enjoyed sort of watching and have seen kind of have
[1029.92 → 1035.06] a lot of discussion on Twitter and in the circles that I'm in is this new model from Facebook,
[1035.48 → 1036.52] Wave2VecU.
[1036.74 → 1038.46] I don't know if you've seen this.
[1038.60 → 1039.80] It's a pretty interesting model.
[1039.94 → 1041.60] It's a speech recognition model.
[1041.60 → 1046.88] And the interesting thing, well, I guess it sort of stands on the shoulders of Wave2VecU,
[1046.90 → 1048.48] which was a previous model.
[1048.74 → 1052.84] But it is very interesting in that it is unsupervised.
[1052.98 → 1055.00] That's what the U stands for.
[1055.52 → 1061.80] And I think what maybe shocked people or what got them really thinking is that this Wave2VecU
[1061.80 → 1070.54] essentially learns how to create transcriptions of audio or speech using purely unpaired data
[1070.54 → 1072.24] or untranscribed data.
[1072.38 → 1077.82] So just putting audio in, which is kind of a weird thing if you think about it.
[1077.92 → 1080.16] Have you seen this or has it crossed your path at all?
[1080.76 → 1082.58] I had seen the name, but I hadn't dug into it.
[1082.62 → 1084.66] And I've just I'm looking at it while we're talking about it.
[1084.66 → 1086.12] And it came out a couple of weeks ago.
[1086.34 → 1089.02] So it's still very new if I'm reading this correctly.
[1090.16 → 1091.42] It's still fresh.
[1092.16 → 1096.78] You know, of course, speech recognition is very much a problem.
[1096.78 → 1101.48] Or often the problem with speech recognition is the fact that you don't have a lot of data.
[1101.96 → 1105.96] We've talked to people like Jeff Adams or others on this podcast who worked in speech
[1105.96 → 1108.88] technology for some long time.
[1109.02 → 1113.52] And a lot of times the problem there is, you know, you need a good amount of high quality
[1113.52 → 1115.12] transcribed audio.
[1115.12 → 1119.36] Like we're talking about thousands and thousands of hours of transcribed audio.
[1119.36 → 1122.22] And you need it sort of pretty high quality.
[1122.42 → 1124.20] You need a diversity maybe of speakers.
[1124.38 → 1125.90] You need a diversity of accents.
[1126.26 → 1130.58] And gathering and curating all that data is incredibly labour intensive.
[1131.38 → 1137.96] And so this model, basically, it operates in a slightly different way than previous models
[1137.96 → 1145.62] in that what it's trying to do is take in unlabelled speech audio, just audio, and generate the
[1145.62 → 1148.40] phonemes corresponding to that audio.
[1148.40 → 1152.10] So phonemes is a word that I, you know, I'm not a linguist.
[1152.40 → 1157.58] So I learned this after joining with SIL, and they started talking about phones.
[1157.58 → 1162.96] And I was confused about, you know, phones, cell phones, what type of phones are we talking
[1162.96 → 1163.24] about?
[1163.56 → 1165.14] But phonemes are phones.
[1165.28 → 1167.14] Here we're talking about actual sounds.
[1167.42 → 1170.64] So phones are the sounds corresponding to the audio.
[1170.96 → 1176.32] And what you can do is you can actually try to create a model that takes in speech and
[1176.32 → 1179.46] generates phones from that or phonemes.
[1179.62 → 1183.28] And then you could take those phonemes and then map them to text.
[1183.50 → 1188.66] And it's that sort of generating from the audio to the phones that they did in an unsupervised
[1188.66 → 1189.04] way.
[1189.60 → 1193.62] And the way that they did this was actually in a sort of generative adversarial way.
[1193.62 → 1200.08] So they had audio coming in one stream to a generator model that generate, tried to
[1200.08 → 1203.94] generate the phones corresponding to that unlabelled data.
[1204.10 → 1209.52] And then over here, they had actually unlabelled phonemicized text.
[1209.80 → 1212.94] So they took text that was already, you know, it was good text.
[1213.02 → 1216.82] It was like, you know, text that they knew was in the language that they're working with.
[1216.82 → 1219.20] They converted that to phones.
[1219.74 → 1224.80] And then they tried to see if a discriminator could tell the difference between the sort of
[1224.80 → 1230.14] quote, good phones that were actually from actual text versus the phones that were generated
[1230.14 → 1231.36] from the generator model.
[1231.98 → 1235.44] And so it's interesting that they're working in this in two ways.
[1235.44 → 1240.46] They're working in this phone space, but then they're also using this idea of generative
[1240.46 → 1245.42] adversarial networks to allow them to solve this problem in an unsupervised way.
[1245.42 → 1249.62] So I don't know if this fits into, you know, after sort of talking through it, if this fits
[1249.62 → 1255.96] into fundamentally, you know, new, different, or just like incremental, I don't know.
[1256.38 → 1260.40] I would say, I don't know that it's a whole new category, but it's certainly an interesting
[1260.40 → 1266.48] step forward in kind of that spans the natural language processing and generative adversarial
[1266.48 → 1267.98] network world together.
[1268.20 → 1272.02] I'm kind of curious, could you talk about like a use case where you could see this being
[1272.02 → 1274.08] applied just to give context for it?
[1275.42 → 1276.42] Yeah, good question.
[1276.62 → 1284.06] So of course, this also stood out to me because I work with a lot of local languages and oftentimes
[1284.06 → 1291.20] you either have a very small amount of sort of transcribed audio for a language in one
[1291.20 → 1293.86] of these lower resource language, or you may have none.
[1293.86 → 1300.40] But oftentimes in like language survey and documentation and language preservation efforts,
[1300.62 → 1303.86] you do collect audio of the language, right?
[1304.02 → 1305.96] It's just not transcribed.
[1306.56 → 1310.36] And in some cases, maybe it's actually never been written down, right?
[1310.42 → 1314.48] Like there are many languages out there, people might be surprised that are still just oral
[1314.48 → 1314.92] languages.
[1314.92 → 1318.20] They've never even been written down in any type of script.
[1318.20 → 1323.92] So I think that although this might not be applied like out of the box in that scenario,
[1323.92 → 1329.14] I think it works us much closer to where, you know, people working with this sort of
[1329.14 → 1334.48] endangered languages and very extremely low resource languages who are able to gather
[1334.48 → 1339.64] audio, you know, of the language speakers still, they may have an advantage in terms of being
[1339.64 → 1345.24] able to actually work towards transcribing that audio more quickly than they would have before.
[1345.24 → 1346.62] Fair enough.
[1346.82 → 1349.64] I'm really fascinated by the number of use cases.
[1350.04 → 1354.96] You know, we've just seen so many orders of magnitude exploding outward the last two
[1354.96 → 1360.10] or three years in terms of where, you know, when we started this podcast, and we are closing
[1360.10 → 1363.10] in now on three years that we have been doing this.
[1363.20 → 1363.84] That's kind of crazy, right?
[1363.88 → 1366.90] The landscape, it is a little bit crazy, I agree.
[1367.28 → 1374.32] The landscape since we started has changed dramatically in terms of how widespread these technologies and
[1374.32 → 1380.84] specifically these models being deployed has been, it was still a little bit unusual to find
[1380.84 → 1385.64] use cases in the marketplace where you had deployed deep learning models that were actually
[1385.64 → 1386.42] in production.
[1386.96 → 1390.28] They were kind of here and there, whereas now it is everywhere.
[1390.54 → 1394.24] And really it is going back to some conversations that we had some time back.
[1394.38 → 1397.98] We are seeing, you know, it very much just being part of software development.
[1398.22 → 1402.54] The idea of model-based engineering is just what engineering has become.
[1402.54 → 1403.94] It's not a separate thing anymore.
[1404.10 → 1405.14] It's not a call-out.
[1405.62 → 1411.20] And I think it is unlikely these days to build any significant software system without any
[1411.20 → 1416.72] thought into model deployment as a service or microservice that can be utilized in that.
[1416.88 → 1422.96] Which brings us back to all of those folks out there who may either be trying to create a career
[1422.96 → 1428.94] in AI or deep learning or however you want to call it, or even software and trying to figure out
[1428.94 → 1434.90] where exactly they fit in and how they should approach, as well as a lot of organizations.
[1434.90 → 1439.92] It's now that the cost has been driven down so substantially from the early days when you,
[1440.22 → 1444.64] you know, very early when the widespread large things were being done by the big name companies.
[1444.64 → 1447.46] But now it's available to just about anyone.
[1447.56 → 1453.42] And all the major cloud providers have full tooling sets, you know, that cover not only the model
[1453.42 → 1457.94] creation and the model deployment, but the entire software stack with it integrated.
[1458.16 → 1462.56] So if you have somebody coming out of college right now, and maybe they have a computer science
[1462.56 → 1465.94] degree, maybe they don't, maybe they're in another area, but this has captured their imagination.
[1466.42 → 1469.94] How would they help their new employer get into this?
[1470.38 → 1471.42] In what different areas?
[1471.54 → 1475.92] How would you, if you were coming in, it's been a while since we talked about it from a complete
[1475.92 → 1476.80] newbie standpoint.
[1476.98 → 1480.12] And I'm just curious, how has that changed now in the last couple of years?
[1480.12 → 1486.00] So when you say that, do you mean like, I am a data or AI person coming into a company
[1486.00 → 1488.64] that's not doing AI things?
[1488.80 → 1491.20] How do I go about creating that transformation?
[1491.44 → 1496.70] Or are you coming at it more from, I'm coming out of college and I want to step into this
[1496.70 → 1498.88] world of AI type stuff?
[1499.10 → 1499.98] I think we should divide them.
[1500.08 → 1502.00] Let's hit both questions for a few minutes.
[1502.18 → 1505.68] And I think it's worth asking because you and I have been doing this for such a long time
[1505.68 → 1508.00] and it feels like we've been there and done that many times.
[1508.00 → 1514.30] But in my day job, outside the podcast, I'm still having people come to me on a regular,
[1514.58 → 1518.68] you know, day-to-day basis and asking for mentorship, and how do I do this?
[1519.08 → 1523.42] And it makes me realize how many people are still trying to find a path into it.
[1523.48 → 1524.46] That happens a lot.
[1524.94 → 1525.06] Yeah.
[1525.20 → 1531.26] I think there's actually, and maybe we can go in terms of learning resources for those
[1531.26 → 1534.76] actually trying to get into the field as an AI person here in a second.
[1534.76 → 1540.98] But I think that the first of those that you mentioned like, how do you sort of seed
[1540.98 → 1547.78] or spawn AI work within an organization that's maybe not operating in that area currently?
[1547.96 → 1550.86] I think that's actually a very challenging problem.
[1551.50 → 1555.88] I would recommend, I don't know if you remember, we were talking about how long the podcast has
[1555.88 → 1561.68] been going on, but way, way, way back at the beginning in the first few episodes, I forget
[1561.68 → 1565.56] which of the first few episodes we had Mike Regime on the show.
[1566.00 → 1566.30] Oh yeah.
[1566.38 → 1567.30] I do remember that.
[1567.48 → 1567.74] Yeah.
[1568.54 → 1572.62] He's sort of an expert in, I mean, I think, I know he's an expert in this area.
[1572.68 → 1576.54] I don't know how you'd describe himself, but how I sort of think of him as really,
[1576.66 → 1583.42] really having amazing expertise in this sort of behavioural economics of creating this sort
[1583.42 → 1584.96] of change within an organization.
[1585.22 → 1587.22] He has a book called Cracking the Data Code.
[1587.80 → 1592.22] So that's maybe a resource out there for those looking to create more of that organizational
[1592.22 → 1592.88] change.
[1593.38 → 1595.90] But he has a formula that he follows.
[1595.90 → 1603.20] But I think that part of that really comes down to making sure that you have and develop
[1603.20 → 1607.92] more and more empathy for the people in your organization and the sort of pain points
[1607.92 → 1614.18] that they're feeling, the more that I think they can feel truly listened to and that you
[1614.18 → 1618.76] understand their pain points and why they go about the way that they're solving those
[1618.76 → 1623.50] problems now and the challenges that they're having, the better chance you have of sort of
[1623.50 → 1631.08] coming beside them and bringing them in very early into the process and helping them sort
[1631.08 → 1633.76] of shape what a solution looks like.
[1633.76 → 1638.38] Because once you kind of, I think, get through a first cycle of this and if it is successful,
[1638.84 → 1643.02] other people will sort of start asking and momentum will build.
[1643.02 → 1648.74] But if you kind of get that wrong the first time, and you develop a terrible taste in
[1648.74 → 1655.84] people's mouth for like AI predictive things, then that's almost impossible to overcome, I
[1655.84 → 1656.12] think.
[1656.60 → 1657.52] That's a perfect point.
[1657.66 → 1660.94] And that was a perfect answer, actually, to how to address that.
[1660.94 → 1667.34] One of the things that I'm seeing also is organizations trying to figure out how to, kind of what
[1667.34 → 1670.68] we talked about in the very beginning a little bit, but how to address AI.
[1670.88 → 1676.12] Do they do it as a separate organization or do they, you know, they integrate it in with
[1676.12 → 1678.32] their data science or their software teams?
[1678.50 → 1683.24] And that can vary based on the domain expertise they have, what their employees are, what kind
[1683.24 → 1686.34] of business they're in, and also what technologies they're focused on.
[1686.34 → 1693.86] I think early on, I saw a lot of AIs being broken out more and more as its own thing.
[1693.98 → 1698.98] And I think the people that drove that were very savvy on kind of internal marketing and
[1698.98 → 1700.36] getting budget for that.
[1700.50 → 1705.86] And certainly, as we've seen it normalize over time a little bit, you're starting to see it roll
[1705.86 → 1712.52] back into more of the data science and DevOps, you know, side of things as well.
[1712.52 → 1716.62] Since it's, you know, it's just another model type, why, you know, divide up your model types
[1716.62 → 1719.38] into some or the, you know, some happen to use GPUs and some don't.
[1719.80 → 1722.40] It seems a very artificial, an artificial thing.
[1723.54 → 1723.66] Yeah.
[1723.96 → 1729.28] And there's always going to be, I don't think there's any right, you know, perfect solution
[1729.28 → 1731.32] here because there's going to be challenges either way.
[1731.42 → 1738.46] If you try to centralize your data science and AI team within an organization, the challenges
[1738.46 → 1742.40] you're going to face are those where you have to be very intentional about having those
[1742.40 → 1747.16] people, you know, reach out and make sure that they connect with the end user, understand
[1747.16 → 1751.28] their pain points, understand their challenges, and that they really have the tentacles out
[1751.28 → 1752.14] in the organization.
[1752.54 → 1757.14] Whereas if you have everybody distributed everywhere, you're probably going to deal with more like
[1757.14 → 1760.64] duplication type issue, duplication of work.
[1761.02 → 1762.78] How are they going to share resources?
[1763.10 → 1767.68] Maybe it's more efficient to have centralized infrastructure, but now it's more complicated because people are in
[1767.68 → 1771.76] all of these different organizational units and all of that sort of stuff.
[1771.88 → 1775.24] So I don't think any one particular model is perfect.
[1786.08 → 1791.18] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1791.32 → 1796.28] Start with Google Chrome, keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1796.50 → 1797.34] Rip out the Google bits.
[1797.34 → 1798.14] We don't need them.
[1798.48 → 1801.00] Mix in ad and tracker blocking by default.
[1801.26 → 1803.96] Quick access to the Tor network for true private browsing.
[1804.26 → 1808.66] And an opt-in reward system so you can get paid to view privacy respecting ads.
[1808.84 → 1812.62] Then turn around and use those rewards to support your favourite web creators like us.
[1812.94 → 1817.54] Download Brave today using the link in the show notes and give tipping a try on ChangeDog.com.
[1817.54 → 1840.96] Well, as always on these fully connected shows, I think that our conversation has led us exactly to where, you know, we often like to go in these types of episodes.
[1840.96 → 1843.62] And that's learning resources for people.
[1843.62 → 1846.30] Maybe new ones that have come out or things that have been updated.
[1846.96 → 1849.30] And we are talking about two different scenarios.
[1849.30 → 1857.70] One where, you know, the challenge is kind of having an organization be transformed into one that uses AI or data science type techniques.
[1857.70 → 1864.78] And the other where maybe you're an individual, and you're trying to break into an organization that's already using AI.
[1864.78 → 1872.10] Maybe on that latter point, I ran across something that I haven't gone through totally, but I very much want to.
[1872.62 → 1875.20] And I've seen sort of a bit of buzz around.
[1875.86 → 1879.74] And this is this new book that is called Meta Learning.
[1880.14 → 1880.98] Have you seen this?
[1881.22 → 1881.90] I haven't, no.
[1882.24 → 1882.44] Okay.
[1882.56 → 1885.66] So originally when I saw the book, I thought, oh, cool.
[1886.04 → 1887.38] It's a meta learning book.
[1887.38 → 1897.46] And, you know, of course, that's a bit of a loaded term in the deep learning AI type world because meta learning, we even have, I think, an episode with, I'm not sure.
[1897.64 → 1899.98] Well, I know we talked to Cheryl Chen about AutoML.
[1900.32 → 1903.10] We think we talked to a couple of people about meta learning.
[1903.24 → 1903.48] Yep.
[1903.72 → 1906.38] Where this is really learning to learn, right?
[1906.42 → 1913.72] So you have some method that maybe learns an architecture or learns an optimization technique or something like that.
[1913.76 → 1916.20] You're sort of learning to learn in some way.
[1916.20 → 1918.84] Well, that's not the kind of meta.
[1919.04 → 1920.34] Well, maybe that's part of the book.
[1920.38 → 1920.72] I don't know.
[1920.96 → 1925.64] But this sort of learning to learn book is really about how to learn deep learning.
[1925.84 → 1927.38] So it is meta learning.
[1927.50 → 1928.58] It's how to learn deep learning.
[1929.02 → 1931.48] It's the human learning, not the model learning in this case.
[1931.84 → 1937.72] Yeah, the human learning, not a model learning how to do learning, but a human learning how to do deep learning.
[1937.86 → 1938.88] It's a nice title.
[1939.46 → 1939.60] Yeah.
[1939.62 → 1942.76] How to learn deep learning and thrive in the digital world.
[1942.76 → 1946.14] And sorry if I get the name wrong, Made Sapolsky.
[1946.74 → 1948.96] And it looks like a really nice book.
[1949.26 → 1954.90] And I think that the focus here, he talks about, I learned to program and do deep learning using online resources.
[1954.90 → 1959.72] Most of my income over the last two years has come from deep learning roles.
[1960.24 → 1961.24] How did that happen?
[1961.54 → 1964.04] If, you know, and he basically lays it out.
[1964.36 → 1968.86] How did he go from, you know, learning deep learning using online resources?
[1968.86 → 1976.42] And now he sort of makes his career from, or his career is doing deep learning type things.
[1977.04 → 1981.08] So this, you know, and I think both of us sort of ended up in that same path.
[1981.24 → 1983.60] Most of our learning has come from self-learning.
[1983.60 → 1990.24] I mean, certainly I'm grateful for the sort of math foundational things in my past and certain
[1990.24 → 1995.04] programming things, experience with doing experiments and that sort of thing in science.
[1995.20 → 1997.76] But I mean, physics isn't exactly deep learning.
[1997.76 → 2000.76] And I didn't really think about machine learning until I was in industry.
[2001.68 → 2007.08] So, and maybe you can remind people about sort of your status prior to working in AI.
[2007.70 → 2012.30] Well, I was doing lots of software for years, but actually my, even that would be the same
[2012.30 → 2016.34] thing and that I learned how to do software fairly early in my career.
[2016.62 → 2018.56] And my degree is actually in finance.
[2018.90 → 2024.18] So it has nothing to do directly with any of these things that we have been talking about,
[2024.20 → 2027.14] whether it be software or deep learning or the things that come next.
[2027.38 → 2032.42] So I think the beauty of a book like this, as I'm looking through the webpage about it,
[2032.44 → 2036.30] is that this is really the core about how people build careers now.
[2036.52 → 2041.98] If you are thinking about how to get there, you have to build in constant
[2041.98 → 2043.68] lifelong learning into your process.
[2043.68 → 2046.20] And if you don't do that, you will fall behind.
[2046.20 → 2048.74] And I meet people all the time that are doing both.
[2048.82 → 2050.86] I meet people that are constantly learning.
[2050.96 → 2052.86] I know you and I are definitely two examples of that.
[2052.94 → 2057.12] I have some other good friends, good colleagues that are constantly learning as things are moving
[2057.12 → 2062.40] forward and figuring out where and how they're going to dig into those ideas incrementally as
[2062.40 → 2062.76] they go.
[2063.16 → 2066.26] And then you see people that don't do that and they do fall behind.
[2066.36 → 2071.32] And as things are moving faster and faster forward, the ability to thrive in a digital world,
[2071.32 → 2074.88] going back to the book subtitle, is really crucial to having it.
[2074.94 → 2079.10] Because anything you're learning right now in more of a formal context, if you're coming
[2079.10 → 2082.54] out of school, for instance, a lot of that will be obsolete.
[2082.98 → 2086.34] The basic math will be there, but the algorithms are going to change.
[2086.70 → 2089.80] How you're achieving problem solutions will change.
[2090.04 → 2092.02] And so you really have to be able to do that.
[2092.38 → 2097.80] I think that is a fundamental for being a digitally literate person in the job world these days.
[2097.80 → 2098.44] Yeah.
[2099.16 → 2104.74] And there's also a lot of what I've seen as maybe difficulty in parsing through.
[2105.14 → 2106.74] It's kind of a good thing and a bad thing.
[2106.82 → 2112.98] There's so much available online that you can use for your learning, but there's also so
[2112.98 → 2114.20] much available online.
[2114.46 → 2116.18] For free or very inexpensively.
[2116.36 → 2116.50] Yeah.
[2116.56 → 2124.62] So how do you figure out what to focus on when there's so much you could focus on and in what
[2124.62 → 2125.04] order?
[2125.28 → 2125.42] Right.
[2125.42 → 2126.70] That's often the missing piece.
[2126.78 → 2128.40] I feel like something like this.
[2128.44 → 2133.64] And again, I'm expecting that the content of this book at least goes into a little bit
[2133.64 → 2135.62] of this, although I haven't explored it in detail.
[2135.62 → 2142.44] But it sounds like from the purpose of this, that part of it is kind of putting some framing
[2142.44 → 2146.68] around the resources that are online and helping people understand the different things that
[2146.68 → 2152.96] they might need to explore if they want to have this sort of role or be part of this kind
[2152.96 → 2155.58] of world.
[2155.58 → 2156.68] missing piece, right?
[2156.76 → 2160.84] Because someone publishes a course over here on this topic and someone publishes a course
[2160.84 → 2165.46] on this topic and then there's a thousand courses and there's a route through those
[2165.46 → 2166.76] courses that make sense.
[2167.34 → 2171.40] But if you don't know anything about the topic in the first place, it's hard to determine
[2171.40 → 2172.50] what that route is.
[2172.56 → 2175.56] And then you sort of get all confused and maybe discouraged.
[2175.56 → 2181.04] Yeah, I think a perfect tactic, which actually comes straight out of the software world is
[2181.04 → 2185.74] the concept of scratching your own itch, is that if you want to get into deep learning
[2185.74 → 2192.56] and into AI over time as it continues to evolve, having a personally significant use case,
[2192.94 → 2194.58] something that you want to get done.
[2194.72 → 2197.00] And it doesn't have to be a day job thing.
[2197.04 → 2198.64] It can be something you're doing on your own.
[2198.94 → 2200.52] It could be doing something around the house.
[2200.70 → 2202.32] There's an infinite number of possibilities.
[2202.32 → 2208.12] And we've talked about these off and on over the three years of the show so far at various
[2208.12 → 2210.38] times in terms of things that we wanted to do.
[2210.68 → 2215.30] And having a use case and figuring out a path through that, and there can be an infinite
[2215.30 → 2216.62] number of paths through that.
[2216.90 → 2221.64] If your fascination is how do I create the models, then you spend your time and learning
[2221.64 → 2223.58] resources on what are the possibilities.
[2224.08 → 2227.12] Somebody else may be a lot more interested in the engineering side of it.
[2227.12 → 2233.30] And they're really just keen on taking advantage of transfer learning and finding a model that's
[2233.30 → 2237.70] already doing very similar to what you want, if not exactly what you want, and basically
[2237.70 → 2240.26] getting that into your context and deploying it out there.
[2240.38 → 2244.86] And those are very, very different paths that you might take to achieve essentially the same
[2244.86 → 2245.20] thing.
[2245.20 → 2250.12] But doing that also helps you find your own personal golden path on how you're going to
[2250.12 → 2255.26] come in to this AI world and be able to be productive and passionate about what you're
[2255.26 → 2255.54] doing.
[2255.54 → 2259.48] So really scratching your own itch is finding the things you want to do.
[2259.60 → 2263.44] If it seems a little intimidating, just try to dig in a little bit and try to figure out
[2263.44 → 2268.86] what those parts would be before you go, oh, this is too much and break it down and then
[2268.86 → 2272.58] continue to break each piece down and put them in the right order and get there.
[2272.58 → 2277.80] I find that I have a habit of the things that I've gravitated toward have usually been because
[2277.80 → 2281.68] of that, because there was a personal fire I had going on that particular thing.
[2281.68 → 2282.12] Yeah.
[2282.12 → 2282.52] Yeah.
[2283.24 → 2289.36] The other interesting element of this sort of finding your path, and I don't know that
[2289.36 → 2292.28] this is explicitly detailed anywhere.
[2292.48 → 2294.88] Maybe this would be a good resource that could be out there.
[2295.00 → 2299.40] But depending on where you want to end up in your career and who you're wanting to work
[2299.40 → 2305.64] with, the sort of stack that you're working with, and it can be very different as we've
[2305.64 → 2306.30] talked about.
[2307.00 → 2314.20] And certain of these courses online sort of assume just like a single lane because it's
[2314.20 → 2318.44] all from one perspective in terms of the tech stack and the tooling as well.
[2318.44 → 2323.86] I'm thinking of, so I was looking up for some Flops resources recently.
[2324.42 → 2328.40] And just by the way, for people who aren't familiar with that, Flops is kind of the machine
[2328.40 → 2333.46] learning version of DevOps, you know, development operations, getting your stuff out there so
[2333.46 → 2337.28] people can use it in a reproducible and standardized way.
[2337.36 → 2337.72] Keep going.
[2337.80 → 2339.96] I just wanted to throw that out for those who aren't used to it.
[2340.44 → 2340.70] Yep.
[2340.86 → 2341.38] Very good.
[2341.38 → 2341.58] Yeah.
[2341.70 → 2347.62] So I was looking for, you know, some resources on this at different courses out there that
[2347.62 → 2348.68] teach Flops.
[2348.90 → 2352.10] And all of them actually that I was looking at seem perfect.
[2352.30 → 2358.02] But for example, I was looking at the deeplearning.ai new Flops course, and I'm sort of looking
[2358.02 → 2358.56] through there.
[2358.68 → 2363.46] And I think partly because I've been exposed to some of this stuff, I kind of deduced and
[2363.46 → 2367.44] partly from, you know, who's teaching it, you can sort of deduce, hey, this is a very
[2367.44 → 2371.86] TensorFlow extended specific pipeline of tooling, right?
[2372.16 → 2376.86] Like they're working with this framework called TensorFlow extended in terms of how they're
[2376.86 → 2382.66] doing both model serialization, optimization, deployment, sort of from end to end.
[2382.86 → 2388.36] This is like the world that they're living in, which makes sense for a lot of companies.
[2388.36 → 2393.50] But there are a lot of companies that have very drastically different opinions on that
[2393.50 → 2394.78] sort of pipeline.
[2394.78 → 2399.72] And another one I was looking at was from Elvis Sarnia.
[2400.28 → 2402.62] He publishes a lot of great content.
[2403.08 → 2407.42] And he has a site called Machine Learning Ops, a collection of resources on how to facilitate
[2407.42 → 2408.80] machine learning ops with GitHub.
[2409.74 → 2414.72] And so this is like a very different, this is all about like, okay, I have code that does
[2414.72 → 2415.68] machine learning stuff.
[2415.76 → 2420.30] How can I automate the deployment and manage testing and all of those things with things
[2420.30 → 2425.74] like GitHub Actions, which is GitHub's sort of CCD framework, continuous integration,
[2425.94 → 2429.98] continuous deployment, and how to like version things properly and all that stuff.
[2430.14 → 2434.86] And so, but then there's another sort of world where like ML Ops, like if you're in a certain
[2434.86 → 2441.40] organization, they've bought into like a platform like, you know, Domino Data Lab, Data Robot,
[2441.68 → 2446.08] this sort of things that handle a lot of those things as well, but at an enterprise level.
[2446.08 → 2452.50] So yeah, there's just these different, I don't know how to help people navigate through things
[2452.50 → 2453.06] like that.
[2453.10 → 2458.80] Because if they, if they choose any one of those courses, it's that that's good content,
[2458.90 → 2459.18] right?
[2459.30 → 2460.56] That they're going to learn a lot.
[2460.72 → 2464.98] But then if they walk into a company that's doing the other thing, you know, it's not that
[2464.98 → 2469.24] it's not relevant, but it's sort of a lot of it's not going to be the same.
[2469.24 → 2475.68] Yeah, there's that dichotomy that you are almost going to be required to buy in or invest in
[2475.68 → 2480.02] some sort of particular flow, an environment, if you will, an ecosystem.
[2480.36 → 2485.60] You have TensorFlow and PyTorch as two of the giant ecosystems and such.
[2485.70 → 2487.06] And there are others as well.
[2487.24 → 2490.90] And, you know, we've talked, we recently were talking about Apache on the show.
[2490.90 → 2496.52] And so at some point, you have to kind of say, okay, well, I have to pick something.
[2496.72 → 2501.70] And you're going to pick the one that either your company's doing or that appeals to you
[2501.70 → 2502.88] or you read an article, whatever.
[2503.46 → 2508.56] But it really helps to try to abstract back out a little bit about what it is that those
[2508.56 → 2509.60] things are trying to do.
[2509.70 → 2512.58] So you don't lock yourself in and be able to.
[2512.74 → 2516.72] And at some point, you need to go look at some of the other ecosystems and try to map them
[2516.72 → 2518.62] to what you just learned in that first one.
[2518.62 → 2522.34] And that way you have the ability to understand how you're doing ML Ops.
[2522.48 → 2526.72] It's not limited to a single ecosystem or community on how they're doing it.
[2527.24 → 2528.54] Yeah, I think that's a great point.
[2529.00 → 2533.58] I hope that this discussion, this sort of rambling discussion has been useful for people that
[2533.58 → 2535.32] are trying to navigate this road.
[2535.42 → 2538.74] We'll provide links to all the things that we've talked about in the show notes.
[2539.16 → 2544.22] We'd really encourage people to join our Slack community by going to changelog.com slash
[2544.22 → 2548.20] community, where you can share some of your favourite resources and talk about how you've
[2548.20 → 2551.18] been learning deep learning and other things online.
[2551.70 → 2555.56] But yeah, that recording went pretty quick, Chris.
[2555.86 → 2556.88] It was a fast one.
[2557.10 → 2559.66] Yeah, I feel like there's a lot to talk about and catch up on.
[2560.00 → 2562.40] Well, we'll have more fully connected shows coming up.
[2562.52 → 2563.32] More in the future.
[2563.58 → 2563.80] Yeah.
[2563.92 → 2564.88] Thanks for the discussion.
[2565.02 → 2565.46] It was fun.
[2565.98 → 2566.74] Thanks a lot, Daniel.
[2567.24 → 2567.48] Bye.
[2567.48 → 2572.94] Thank you for listening to Practical AI.
[2573.30 → 2575.28] We appreciate your time and your attention.
[2575.94 → 2579.34] If you enjoyed this episode, help us out by spreading the word.
[2579.98 → 2580.68] Think of a friend.
[2580.86 → 2581.64] Think of a colleague.
[2581.84 → 2583.66] Somebody who would benefit from listening to it.
[2583.90 → 2584.64] And send them a link.
[2585.00 → 2586.00] We'd really appreciate it.
[2586.38 → 2589.70] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[2589.92 → 2593.46] It's produced by Jared Santo with music by Break master Cylinder.
[2593.46 → 2597.06] Thanks again to our sponsors, Vastly, Linde, and Launch Darkly.
[2597.34 → 2598.02] That's our show.
[2598.44 → 2601.16] We hope you enjoyed it, and we'll talk to you again next week.
[2601.16 → 2631.14] We'll be right back.
