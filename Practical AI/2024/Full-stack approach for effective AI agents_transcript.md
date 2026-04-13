[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.44 --> 46.28]  Welcome to another episode of Practical AI.
[46.28 --> 48.54]  This is Daniel Whitenack.
[48.68 --> 52.38]  I am the CEO and founder at Prediction Guard.
[52.38 --> 59.96]  And I'm joined as always by my co-host, Chris Benson, who is a Principal AI Research Engineer at Lockheed Martin.
[60.26 --> 60.92]  How are you doing, Chris?
[61.26 --> 62.62]  I'm doing very well today, Daniel.
[62.76 --> 68.22]  I'm hoping that we can kind of imbue today's show with a sense of wonder and exploration.
[68.88 --> 69.16]  Yes.
[69.26 --> 75.04]  Well, thankfully, we have an agent on the show with us that's going to be very helpful in that.
[75.42 --> 80.86]  Today, we have Josh Albrecht, who is CTO and co-founder at Imbue.
[81.00 --> 81.68]  Welcome, Josh.
[81.68 --> 82.28]  Thanks.
[82.36 --> 83.08]  It's great to be here.
[83.64 --> 83.94]  Yeah.
[84.18 --> 84.34]  Yeah.
[84.40 --> 92.70]  Well, we sort of, in a not very funny way, teed up a couple of things to talk about there as related to agents.
[92.92 --> 94.62]  But could you give us a little bit of background?
[94.78 --> 105.58]  You talk with Imbue about the dream of personal computing, the dream of agents doing work for us in the real world, kind of your approach to that.
[105.58 --> 107.84]  But we'll dig into a lot of those things.
[107.84 --> 124.42]  But could you give us just a little bit of background in terms of how you, as founders of Imbue, came to these problems around agents and accomplishing more kind of complete or complicated tasks with agents?
[124.42 --> 124.90]  Yeah.
[124.90 --> 125.22]  Yeah.
[125.22 --> 128.96]  I mean, AI is definitely something that I've always been interested in and excited by.
[129.06 --> 136.42]  I remember a long time ago, my friend read some book in middle school, I think, like maybe Ray Kurzweil's The Singularity Is Near.
[136.50 --> 137.64]  And it's like, oh, wow, there's AI.
[137.76 --> 138.44]  Wow, so exciting.
[139.04 --> 140.14]  And, you know, did all that come true?
[140.22 --> 141.40]  I don't know necessarily.
[141.40 --> 143.78]  But it seemed like an interesting thing.
[143.98 --> 148.06]  And I've always been interested in thinking and logic and AI and neuroscience.
[148.48 --> 151.38]  And when I went to school, I was originally going to do cognitive neuroscience.
[151.70 --> 153.50]  But the professor was a little bit too boring.
[153.68 --> 154.90]  So I did AI research instead.
[155.48 --> 158.82]  And so ever since then, I've kind of, you know, I published a bunch of papers and things.
[158.82 --> 160.94]  But it felt like it wasn't really going to have a big impact on the world.
[161.12 --> 162.24]  So I went off to do startups.
[162.24 --> 168.52]  But all the time that I was in startups, I was always looking back and looking and saying, like, oh, it's like now the time to get back into like more fundamental AI research.
[168.62 --> 169.50]  Like, does this stuff work yet?
[169.50 --> 172.20]  And eventually it came a point where it's like, yep, this stuff is working.
[172.54 --> 177.84]  Like, what I've always wanted to do with AI systems is, like, make better tools for us.
[177.88 --> 184.70]  Like, there's so much work that we have to do in the real world that is just not that fun, not that interesting, and not really moving things forward.
[185.36 --> 191.80]  And so all my time at startups and the things that I've been working on, they've all been very practical, very applied versions of machine learning.
[192.28 --> 197.24]  And so I've always wanted to, you know, we are an AI research company, but it's not AI research for AI research sake.
[197.24 --> 199.32]  It's AI research to actually make tools that are useful.
[199.90 --> 203.98]  And so what we're doing at MPU is we're trying to make tools, you know, even just starting for ourselves.
[203.98 --> 212.34]  Like, can we make robust coding agents for ourselves that can really help accelerate us and help kind of take over some of the boring tasks that we don't necessarily want to do?
[212.66 --> 214.12]  And that's what sort of gets into agents.
[214.34 --> 216.76]  It's like agents are AI systems that are acting on your behalf.
[217.14 --> 219.44]  Tools like, you know, chatbots, et cetera, are really cool.
[219.74 --> 220.90]  It's great to be able to answer questions.
[221.02 --> 222.08]  It's great to be able to generate text.
[222.08 --> 228.74]  But if I have to copy and paste that text every time over into some other thing and like do all the work myself, it can only save you so much time.
[228.98 --> 233.68]  Right. It's like a better version of Google at the end of the day or a better version of like search engine or something like that or a book.
[233.68 --> 237.82]  And so I think the real promise of AI is in systems that actually take actions.
[238.00 --> 242.80]  But in order to get that to work, we still have a lot of work to do on the capability side.
[243.04 --> 249.36]  Like when you're talking about taking actions in the real world, there's a lot more risks, a lot more kind of downsides that come from that.
[249.36 --> 253.02]  And you need to be careful about like, you know, you don't want to empty the user's bank account.
[253.14 --> 254.80]  Like that's going to be a really bad product experience.
[254.80 --> 259.26]  Right. So how do you make systems that the user can actually trust?
[259.64 --> 265.08]  Systems that are robust systems that you can know are actually correct and that flag for you like, hey, I'm not really sure about this.
[265.54 --> 274.48]  So this is kind of why we always talk about coding and reasoning is we're talking about the ability to kind of like understand the outputs that are actually being created and understand, is this correct?
[274.80 --> 279.16]  Is this actually going to be useful for people and really like thinking it through more like a person instead of just, hey,
[279.16 --> 280.32]  here's a generation, good luck.
[280.80 --> 283.40]  So that's kind of how we got to agents is like we want to make practical systems.
[283.56 --> 287.06]  We care about, you know, making these systems actually robust and useful for people.
[287.28 --> 289.58]  And that's what a lot of our research is focused around.
[290.16 --> 293.32]  When it comes to agents and sort of where we're at with them now.
[293.32 --> 297.24]  So we're recording this in May of 2024.
[297.76 --> 303.04]  For those that are that are listening back, how would you kind of categorize in your mind?
[303.12 --> 305.44]  Because, you know, you can download Blankchain.
[305.44 --> 315.12]  You can like create what is a agent, you know, maybe for this purpose or that purpose that searches the web or does this thing or that thing.
[315.12 --> 321.38]  And there's certainly even in my own experience, a lot of fun to be had in that for sure.
[321.50 --> 336.12]  But there's a lot of challenges in making this sort of at least in the enterprise setting, making this a reality for solving problems, much less than sort of my those random times in my personal life where I need to do things.
[336.12 --> 348.12]  So how do you categorize like as of now, the state that we're now, of course, everything's changing the sort of main sets of challenges that where people are hitting blockers when they're trying to create these agents?
[348.62 --> 352.14]  Yeah, that's something that we actually played around with a lot last year.
[352.14 --> 370.28]  We interviewed a whole bunch of founders of different agent companies, both, you know, like on our podcast and our Thursday nights at AI events and also just in person, kind of off the record, a bunch of friends, friends of friends, people starting companies, really trying to understand, like, what are the problems that people are running into when they're trying to make agents?
[370.28 --> 381.62]  And the thing that we kept coming back to is, you know, there are all these tools like LaneChain and all these other bits of infrastructure out there or ways of testing things like Scorecard AI or all these different libraries.
[382.20 --> 389.16]  But the problem that people really had was like what you really want as a software developer is, but does it actually work?
[389.24 --> 391.18]  Like, does it actually answer the question correctly?
[391.18 --> 400.14]  And can I get these things to do what I want as a product designer or as an engineer without having to specify all of the, like, details myself?
[400.26 --> 401.50]  Like, that's sort of the promise of AI.
[401.80 --> 407.34]  And right now, they're really great for getting, like, a first pass version of this system working where it's like, oh, cool.
[407.40 --> 410.98]  Like, you ask it a thing and, like, 60, 70% of the time it's right.
[411.12 --> 411.68]  That's great.
[411.72 --> 412.28]  That's so amazing.
[412.40 --> 412.56]  Wow.
[412.60 --> 414.88]  It's like getting this really complicated question right some of the time.
[414.88 --> 418.80]  But 60, 70, 80% isn't really enough for, like, deploying this.
[418.80 --> 425.86]  And going from that 80 to 90 to 95 to 99 to 99.99, like, that's actually a lot of work.
[426.40 --> 432.68]  And so people have made all sorts of techniques, you know, for RAG or for kind of other types of ways of conditioning.
[432.80 --> 434.36]  The answer is to kind of make them better and better.
[434.74 --> 442.26]  But the things that work today are kind of the more constrained versions where you're sort of, you know, you're asking, like, a very simple question or you're in a very narrow domain.
[442.26 --> 447.16]  And so the programmers, the product designers can, like, make sure that, like, everything works out within these rails.
[447.16 --> 452.14]  So, like, once you are in the more, like, general assistant kind of category, it's, like, a lot, lot harder.
[452.24 --> 454.24]  I think we've seen a lot less stuff be successful there.
[454.68 --> 463.06]  But I think in terms of categories and, like, in terms of kind of the problems that people are running into, I would say the main one I would summarize as robustness, like, correctness.
[463.12 --> 466.04]  Like, can you actually get these things to be robust all the time?
[466.10 --> 468.00]  I think that's what really distinguishes agents.
[468.00 --> 471.68]  Like, if we think about agents in the real world, like, a dog is an agent.
[471.82 --> 472.32]  I am an agent.
[472.40 --> 473.10]  A robot's an agent.
[473.52 --> 477.68]  Like, a dog is actually extremely good at not dying for a really long time, right?
[477.96 --> 481.38]  It's not that 90% of the time when it walks across the road, it doesn't get hit by a car.
[481.46 --> 483.54]  Like, 100%, well, almost 100%.
[483.54 --> 485.62]  Most of the time, you know, it's, like, pretty safe.
[485.72 --> 491.02]  Like, it's usually, like, as agents, we're being very, very conservative, very cautious so that we take correct actions.
[491.02 --> 501.34]  And there's a lot of, like, heuristics and intelligence that goes into being conservative, being risk-averse, like, being able to take a long chain of actions without going wrong, without something else horribly going wrong.
[501.38 --> 504.42]  And our agents, like, don't have that kind of common sense and that kind of reasoning right now.
[504.84 --> 507.76]  I think if they did, it would make it a lot easier for people that are building agents.
[508.12 --> 518.54]  As we were kind of going through the last couple of questions, talking about kind of the problems that people are run into when they're trying to make agents work and, you know, what can they do to ensure that it has a good outcome?
[518.54 --> 534.34]  I also run into people all the time who I think really struggle to understand, you know, within the context of this, you know, all the hype and the boom of generative AI, what can you use an agent for productively in enterprises in 2024?
[535.02 --> 539.50]  You know, they're used to going to these web interfaces that are, you know, becoming ubiquitous for us all.
[539.62 --> 545.88]  But the notion of saying, okay, I'm going to, going back to what you said earlier on, kind of getting it out of that web interface.
[545.88 --> 560.36]  Can you kind of paint a picture about how people out there who are trying to bring this productively into their organization as an agent versus a web interface, how they might even conceive of what, of how to approach problems that they might want to solve with the technology?
[560.98 --> 566.24]  There's a lot more work to be done today to make agents work for a system.
[566.50 --> 571.68]  I think if you approach it as a more holistic system, then it's more likely to work.
[571.68 --> 574.74]  So if you think like, okay, where are the places that it could go wrong?
[575.10 --> 577.50]  How, like, what's the confidence that I'm getting back from this system?
[577.94 --> 579.84]  Can I flag that for human reviewers?
[580.16 --> 584.96]  Can I have like a bunch of different checks in place that are both like in domain, like for programming?
[585.10 --> 589.58]  Like, does it pass a linter or does it pass this like style guide or like, does it at least type check, right?
[589.64 --> 590.76]  Or is the syntax correct?
[590.84 --> 593.62]  Like there's a lot of checks that you can do kind of in domain that you can help out.
[593.66 --> 595.16]  There's different in different industries as well.
[595.16 --> 599.16]  And then there's sort of, you can use the LLM to score this and ask like, is this particular thing wrong?
[599.24 --> 600.62]  Is that particular thing wrong with it?
[600.92 --> 611.78]  So as you start to build up more kind of like safeguards and guardrails around these, then you can start to get them to a level of robustness where like maybe for the easy cases, it's okay for your application for it to fail.
[612.18 --> 613.60]  And you know where that failure rate is.
[613.66 --> 617.02]  And you've done a lot of work to understand like how much can we tolerate?
[617.56 --> 620.70]  One of the things that we've done a lot internally is working on our own evaluations.
[621.06 --> 624.98]  This is a really critical thing for anyone who's like trying to build real systems.
[624.98 --> 629.32]  You have to get really into the weeds of what does it mean for the system to be right?
[629.76 --> 641.92]  We've actually taken all of the open source NLP benchmarks and made our own internal versions of these systems to make sure that they're not contaminated by the training data and to make sure that the questions are actually correct.
[641.92 --> 652.04]  So one of the things that we'll have coming up and not too distant future actually is I think hopefully being able to contribute back some of that evaluation work that we've done of like cleaning up these existing benchmarks.
[652.26 --> 654.66]  But we also have a bunch of our own internal ones as well.
[654.98 --> 660.58]  And I think it's kind of critical for anyone making these systems to like make them yourself like by hand at least like 100.
[661.08 --> 661.62]  Look at them.
[661.86 --> 662.74]  Is this the right answer?
[663.16 --> 664.02]  Okay, what did it get?
[664.26 --> 665.04]  Okay, is that right?
[665.14 --> 670.02]  Like getting to a place where as humans you agree on this, you're getting a machine system to calibrate well to this.
[670.16 --> 673.82]  Then you're checking like, okay, are the things that we're getting as inputs in production?
[673.82 --> 675.18]  Like, are they from the same distribution?
[675.74 --> 677.68]  Like, does this test actually make sense for this?
[677.74 --> 678.28]  They're not drifting.
[678.66 --> 682.32]  Like if you have adversarial systems like fraud or something much, much more typical.
[682.54 --> 689.56]  If you have something where you're getting the same kind of a query every time, then it can be possible to get something where you can trust it enough to say like, okay, cool.
[690.00 --> 691.38]  This is getting us 99%.
[691.38 --> 692.18]  That's acceptable.
[692.18 --> 694.00]  We have some, you know, guardrails here.
[694.06 --> 695.54]  We can check how well it's doing over time.
[695.64 --> 697.56]  We have people looking at these and auditing some of them.
[698.02 --> 704.46]  That's kind of the way to make this really useful as you have to be like really getting into the weeds and into the details of how do we evaluate this?
[704.74 --> 705.86]  What does success look like?
[706.18 --> 706.44]  Et cetera.
[706.44 --> 717.50]  And for the use cases out there, like the most successful use cases that you've seen, I don't know if you have good examples of those either internally or externally.
[717.70 --> 722.54]  But when you think of those, I like what you're saying about digging into the details.
[722.54 --> 732.62]  I'm wondering also how much sort of specific domain expertise is actually factoring into how you handle those details.
[732.62 --> 746.16]  So if you're building an agent to help people process data in a healthcare scenario or data in a financial services scenario or in a coding assistance scenario, there's kind of this view.
[746.16 --> 755.12]  Like if I just download Langchain, if I go and kind of have the zero shot approach, right, where this agent might be expected to do anything.
[755.12 --> 768.92]  My impression is that the most successful agentic type of workflows out there so far have been very much driven by people with high degrees of domain expertise in an area that are able to work through those details.
[769.02 --> 770.12]  Is that impression correct?
[770.24 --> 771.84]  Do you have any thoughts on that?
[772.20 --> 773.74]  Yeah, that seems pretty much right.
[773.86 --> 779.02]  I think there's this promise of AI that like someday you'll be able to just ask it to do anything.
[779.28 --> 781.48]  And the interface sort of affords that.
[781.48 --> 783.28]  It looks like, oh, like there's this text box.
[783.34 --> 784.32]  I can just ask it to do whatever.
[784.40 --> 785.60]  And it will give me back a response.
[785.66 --> 787.66]  And wow, it even sounds so confident and so correct.
[787.74 --> 788.30]  Wow, that's great.
[788.50 --> 789.26]  This can do anything.
[789.64 --> 791.12]  Maybe it even succeeded at that case.
[791.28 --> 799.92]  One example that I love from a little while ago was we were trying to see how well existing LLMs would do at detecting bugs.
[800.24 --> 805.38]  And so we would ask, like, the first thing that I did was like, I looked, okay, like, is there a bug on this line?
[805.42 --> 806.56]  I found a function that had a bug.
[806.64 --> 808.22]  I was asking, yes, there's a bug on this line.
[808.28 --> 809.68]  It's like, oh, wow, I look so good at this.
[809.68 --> 810.64]  It's like, wait a second.
[811.12 --> 813.00]  How about this other line that definitely does not have a bug?
[813.20 --> 814.44]  Oh, yeah, there's a bug on this line.
[814.58 --> 815.32]  This doesn't work.
[815.40 --> 816.46]  And this is like, wait, wait, wait.
[816.48 --> 817.68]  You're just always saying yes.
[817.82 --> 819.54]  Like, this is not quite right.
[819.70 --> 822.36]  So, yeah, it seems to like promise that.
[822.44 --> 830.22]  But you have to really dig into the detail, use few shot examples and retrieval and all these other kinds of techniques to kind of like get into the weeds.
[830.40 --> 835.44]  And the more domain expertise that you can bring to bear, the dramatically better I think the outcome is going to be.
[835.44 --> 848.40]  So, Josh, I'm really intrigued by sort of the statement on what you put online in terms of imbues thinking about building robust foundation for AI agents as being a full stack approach.
[848.40 --> 856.64]  I like that because it sort of reminds me, I don't know, Chris, if you remember quite a while ago when we were still talking about data science.
[856.96 --> 862.92]  I guess it's data science is still a thing, but you're talking about it a lot more years ago.
[862.92 --> 870.22]  And there was this, I forget, I think it came up a few times like this discussion about being a full stack data scientist.
[870.22 --> 883.14]  And oftentimes those are the most productive where you have an understanding of how data pre-processing happens and building your application, how the model is embedded in software and deployed and all of this stuff.
[883.14 --> 886.28]  And so I love that sort of thinking in that respect.
[886.42 --> 893.06]  And I'm wondering from imbues perspective, how you think about taking a full stack approach when it comes to agents?
[893.60 --> 909.72]  Yeah, we take it, I think, to a slightly more extreme degree than most people in that we do everything from setting up our own hardware, building our own infrastructure, retraining, fine tuning, RL evaluations, data generation, cleaning, like UI, user experience, like the whole thing.
[909.72 --> 917.34]  And the thinking there is that at each one of these places, you can tweak some things to make the overall thing kind of work better together.
[917.78 --> 925.14]  Right. So you can kind of change the training data that you've used in your system in order to make it more like the kind of thing that you actually need for your product.
[925.26 --> 930.34]  And then in RL, you can kind of set objectives that are related to the things your user actually cares about.
[930.42 --> 936.86]  And then on the UI, you can use the capabilities that you have to kind of help highlight places where this particular system fails.
[936.86 --> 944.30]  Right. So I think we're really interested in kind of the full stack approach and the ability to like tweak things at each one of these levels.
[944.46 --> 948.12]  And for us, it comes from our like history as a research company.
[948.24 --> 954.48]  One thing that we've always really focused on is being able to like deeply understand the technologies that we're working with us.
[954.48 --> 959.62]  So for us, you know, pre-training, fine tuning, doing RL, it's not just a black box.
[960.06 --> 963.78]  Like we want to open these things up and understand like what's actually happening inside of there.
[963.78 --> 972.28]  We have a paper club, you know, every Friday where we're looking at like the state of the art stuff that's coming out, reading through this and trying to like really understand what are neural networks really learning?
[972.44 --> 974.90]  Like, how is this language model actually learning? Where does it fail?
[975.34 --> 980.34]  There are really interesting papers, you know, that show particular logic puzzles where this thing doesn't work.
[980.42 --> 984.26]  And it's like, oh, OK, it's not really doing logic. It's not really doing addition. It's doing this other thing.
[984.66 --> 990.14]  But if you, you know, if you tweak it in this way, like, oh, now you can get it to learn like a simpler form of addition that is more general.
[990.34 --> 991.66]  OK, that's really interesting. Right.
[991.66 --> 996.36]  So what is a transformer really good at learning? Like what things in the data actually matter?
[996.82 --> 1000.88]  And how do you evaluate these things as well as another thing that, you know, we've also thought about a lot.
[1000.94 --> 1008.64]  Like one of the things that we set up that has been super useful is looking at the not just the accuracy of our systems,
[1008.64 --> 1013.76]  but the perplexity on multiple choice question answering data sets specifically, not perplexity over all the tokens,
[1013.86 --> 1016.70]  but perplexity specifically for the multiple choice question answering things.
[1016.70 --> 1021.36]  This gives you a much more fine grain understanding of like, is this actually being right or not?
[1021.40 --> 1026.86]  It gives you a really precise metric for this. And this idea came from a paper which was about, you know,
[1027.48 --> 1033.64]  I think something like our emergent properties of language models are mirage or something like that was the title of the paper.
[1034.02 --> 1038.82]  Their point was like, you know, a year or two ago, people were like, oh, look, like these language models have these like emergent behaviors.
[1038.82 --> 1042.70]  Like they're suddenly learning to reason or whatever. It's like, oh, wow, they're like suddenly getting so smart.
[1042.96 --> 1047.92]  But when you really dig into it, it turns out that if you look at the performance on a log scale, it's linear.
[1048.42 --> 1051.86]  So what was really happening is just our metric was not very good, right?
[1051.88 --> 1055.08]  We weren't really asking the right questions. We weren't deeply understanding what was happening.
[1055.46 --> 1059.28]  It was just always in a log scale, just always getting better. And you just couldn't see it in the metric.
[1059.70 --> 1063.18]  And so for us, you know, this is a good example of like you want to deeply understand what's going on here.
[1063.24 --> 1066.54]  We don't want to just treat these as magical entities, but rather they're just technologies.
[1066.54 --> 1072.30]  They're just really bags of features at the end of the day that we can use to do actual work in the real world.
[1072.82 --> 1079.44]  And so I think that that's kind of our approach is to like take the full stack approach, understand everything from like, OK, how does the InfiniBand network work?
[1079.54 --> 1083.52]  Like, how does that fit into our performance optimizations? Like, how does the data work?
[1083.60 --> 1089.48]  Like, how does the network work? Like, how are all these things adding up to give us, you know, some final error, some final user experience?
[1089.48 --> 1090.08]  That's really good.
[1090.40 --> 1093.24]  You're kind of really fascinating me with that statement.
[1093.24 --> 1102.14]  So many people do take kind of that black box approach and they don't necessarily have that kind of research first orientation that you're describing.
[1102.14 --> 1117.68]  As a company, as a business, how does that research orientation where you are rejecting the black box perspective and saying, we're going to open it up, we're going to tinker, we're going to understand the specifics of how small changes, you know, affect that.
[1117.82 --> 1124.50]  How does that affect how you approach this compared to whoever you would perceive as your competition or something?
[1124.62 --> 1125.08]  What is it?
[1125.28 --> 1128.92]  What does it mean for you as a company to take that kind of research first approach?
[1128.92 --> 1138.08]  Yeah, I think there are tradeoffs to it. One tradeoff is that, you know, it takes a little bit more time and effort to do this, to like really deeply understand things rather than just like hack it together and throw it out there.
[1138.40 --> 1148.14]  But I think the benefit is in the long term, like when we do really deeply understand these systems, it makes it a lot easier to make modifications and to make changes and to know how to improve things.
[1148.54 --> 1155.62]  These systems are very expensive to train. Like there's a lot of effort that goes into this and it can be very expensive to like just try a whole bunch of things.
[1155.62 --> 1158.94]  And like, if you don't really know what you're doing, it's easy to waste a lot of time.
[1159.48 --> 1164.10]  And so I think for us, we would rather take a step back, say like, okay, what's actually going on here?
[1164.22 --> 1171.82]  Can we make robust systems? Can we make robust baselines? Can we get this working in a way that like we can trust our results, that we can understand what's going on and build on top of those.
[1171.82 --> 1183.46]  Another thing that we've built internally that has been really useful kind of along these lines is carbs is cost aware Pareto region Bayesian search or something like that.
[1183.72 --> 1186.98]  Basically, it's a hyperparameter tuner that is cost aware.
[1187.50 --> 1194.22]  So we can take any system that we have and say, hey, you have all these, you know, 10 or 20 different hyperparameters, these different knobs you can fiddle.
[1194.36 --> 1197.32]  Like, how do you get, you know, I have a system that works, but how do I make it way better?
[1197.32 --> 1203.70]  We can take this, just throw it in there, come back the next day, and it's tried hundreds of experiments at different scales.
[1203.82 --> 1208.04]  So it tries at a really small scale and it sees like, okay, for a really small scale, like this is the best way to do it.
[1208.08 --> 1215.20]  And then as we get higher and higher and spend more and more time and resources and money on it, like this is kind of how these hyperparameters change, how things change as we scale.
[1215.90 --> 1220.42]  And just understanding that like there are these scaling laws, there are scaling laws for different parameters.
[1220.42 --> 1228.44]  Like, how can we back those out and learn for any given architecture, any given problem, having an automated system to do this allows us to kind of like quickly develop this.
[1228.54 --> 1230.42]  And it took some time to make this system, right?
[1230.42 --> 1235.40]  But it like really pays off to have that kind of deep understanding of the systems that we're working with.
[1235.52 --> 1237.76]  So I think for us, it's kind of like taking a long-term view.
[1238.18 --> 1241.12]  I think in the long term, it's much better to actually understand what's going on.
[1241.40 --> 1243.34]  And it does take a little bit of upfront, you know, work.
[1243.58 --> 1245.38]  That's why, you know, we don't necessarily have a product yet.
[1245.44 --> 1246.20]  We're working on it.
[1246.42 --> 1247.38]  I think we'll get there.
[1247.38 --> 1250.80]  And I have confidence that we'll get something really cool, but it does take a little bit longer.
[1251.22 --> 1252.24]  And that's okay.
[1252.32 --> 1254.18]  I think we'll end up with something much cooler as a result.
[1254.80 --> 1263.68]  As someone who's working both on the, like all the way up the stack, even up to interfaces and all of that.
[1263.68 --> 1267.86]  But you're also training these foundation models.
[1268.66 --> 1277.74]  Certainly the sort of both the market and the technology and the options around foundation models have just sort of blossomed.
[1277.88 --> 1282.38]  And these have proliferated over the past year, especially.
[1283.10 --> 1284.70]  What's it been like internally?
[1284.70 --> 1289.40]  Certainly, you know, we've had a couple people on the show and I find this interesting.
[1289.66 --> 1295.74]  Like from the perspective of someone inside a company that is training their own foundation models.
[1296.54 --> 1307.86]  How do you go about maintaining focus within this sort of environment where eventually you're going to have to spend a significant amount of time, you know, investing in a model.
[1307.86 --> 1311.60]  Our specific model architecture, specific data sets, that sort of thing.
[1311.74 --> 1313.72]  But, you know, things are shifting all the time.
[1314.22 --> 1317.76]  You mentioned reading, you know, papers and trying to keep up.
[1317.98 --> 1320.00]  But, yeah, how do you maintain that focus?
[1320.22 --> 1329.52]  And what's sort of life like in the midst of being a foundation model builder in May of 2024?
[1330.30 --> 1334.88]  Yeah, I would not necessarily characterize us as a foundation model builder.
[1334.88 --> 1337.40]  And that part of what we do is train models.
[1337.86 --> 1339.50]  But that's not the only thing that we do.
[1340.02 --> 1340.10]  Yeah.
[1340.18 --> 1345.92]  And the reason that we do it is not necessarily to make, you know, the biggest, bestest foundation model ever.
[1346.12 --> 1351.42]  Like I think there's, you know, a lot of money going into other companies spending huge amounts on these.
[1351.66 --> 1352.76]  And general purpose.
[1352.96 --> 1354.92]  On general purpose versions of these systems.
[1355.16 --> 1358.98]  And I think for us, the more interesting thing is, can we make them more specialized ones?
[1359.06 --> 1359.76]  Can we take these?
[1359.84 --> 1360.60]  Can we adapt them?
[1360.88 --> 1361.98]  Can we make them more specialized?
[1362.18 --> 1367.70]  Can we find ways to have them work together to pull different things together and make a model that's kind of better at doing?
[1367.86 --> 1374.08]  That, that sort of synthesis and kind of like pulling these things together and better at the particular tasks that we care about.
[1374.40 --> 1376.84]  We've seen really good results from this.
[1376.92 --> 1379.16]  We'll have some blog posts in the next few weeks about this.
[1379.22 --> 1383.72]  But I think we've seen some really good results on much, much smaller models.
[1383.72 --> 1396.26]  And so, you know, I think if you look at like DeepSeq Coder, for example, I think that model still significantly outperforms Lama, a model that's the same size and even of much larger models.
[1396.52 --> 1398.88]  And because this is because like it's really trained on a lot of code.
[1398.94 --> 1403.76]  And so to generate code is like something it's very familiar with, as opposed to being a pretty small part of its distribution.
[1403.76 --> 1404.12]  Right.
[1404.12 --> 1409.82]  So I think, again, this comes back to the fundamental understanding part, like because we know like these are just bags of features.
[1410.14 --> 1412.14]  Yes, having a bigger bag of features is definitely better.
[1412.50 --> 1413.96]  But then your inference time goes up as well.
[1414.40 --> 1417.04]  And if you want better bags of features, like you need to give a good data.
[1417.42 --> 1421.18]  Like the really important thing here is the quality of data that you're giving it.
[1421.48 --> 1426.30]  Less so the like, you know, absolutely massive size, I think, for practical uses.
[1426.30 --> 1432.68]  So our focus is like, can we make these like really specialized and, you know, very useful for ourselves for our own purposes?
[1433.10 --> 1442.56]  I think we're pretty happy to see people out there competing, making better technologies, you know, driving the cost of these things down, making the huge context windows, like giving them away for free in many cases.
[1442.82 --> 1443.42]  You know, that's great.
[1443.52 --> 1450.72]  Like we're happy to see more competition there, because I think the part that we're more interested in is how do we actually use these things at the end of the day and put it all together to be really useful?
[1450.72 --> 1453.10]  I love that you mentioned DeepSeq.
[1453.20 --> 1463.16]  That's a favorite of ours as well at PredictionGuard and generating SQL to do data analysis and code and in our chat interface.
[1463.38 --> 1464.64]  Yeah, we love that.
[1464.98 --> 1466.44]  And so, yeah, I totally agree.
[1466.54 --> 1469.34]  There's a lot that can be done with that sort of thinking.
[1469.82 --> 1473.34]  You also mentioned you're in your work kind of more of that.
[1473.46 --> 1477.34]  And I do want to get to kind of more of the front end interface side.
[1477.34 --> 1490.26]  But before we get there, you mentioned kind of pursuing fundamental laws behind deep learning in order to, again, understand and create this foundation for the agents that you're building.
[1490.50 --> 1501.18]  What have been some of the things that you pursued in that area as kind of the theoretical underpinnings for this progression towards robust agents?
[1501.18 --> 1510.80]  There's a bunch of things that are still in progress that I can't speak to directly, but we're definitely interested in, say, you know, how do you initialize things properly?
[1510.98 --> 1513.74]  Like the MUP work by Greg Gang, et cetera.
[1513.74 --> 1525.88]  We have one of our researchers with a collaborator of his and like working on kind of understanding exactly what the right way is to parameterize these language models in a theoretical sense, but for a practical reason.
[1526.36 --> 1533.80]  So if theoretically like this is the right way to parameterize them, then the practical implication is like you no longer need to tune the learning rate as you scale them up.
[1534.02 --> 1536.70]  This is super helpful because that's like one of the key factors.
[1536.70 --> 1541.16]  And so to remove some of these hyperparameters makes it much more efficient to kind of explore this space.
[1541.56 --> 1547.82]  Right. So that's like an example, a very concrete, simple example of like a place where sort of the theoretical understanding can help you.
[1548.38 --> 1559.20]  Other places where this can help are not as easy to point at like the exact theory and sort of more informed by that or more like physics, like physics didn't start with like perfect theories of everything.
[1559.20 --> 1565.28]  Right. We sort of like kind of did some experiments and had a more experimental understanding of the world before we had perfect theory about why everything worked.
[1565.28 --> 1567.80]  I think we're at that phase with machine learning as well.
[1568.28 --> 1584.94]  And so there's some interesting work by one of our researchers, Jamie Simon, on kind of like what's actually happening in the fundamentals, like when we're when we're learning things like there's this notion from one of his papers about learnability, like a network of a fixed size can only learn so many things.
[1584.94 --> 1593.24]  And it's like very precise. Or we've had another paper about like self-supervised learning where you can see like, oh, there's this sort of like stepwise nature as it learns like each piece of the thing.
[1593.24 --> 1597.36]  So each of these little like theoretical things is telling you something about how they work.
[1597.60 --> 1602.94]  We don't have a full picture and the real ones are like quite complicated and a little bit more complicated than these smaller examples.
[1602.94 --> 1612.40]  But each piece is giving you like a sense for what's going on and allowing you to like operate in this space without having to like guess and check quite so much.
[1612.48 --> 1619.08]  It's not as much of a black box. It's more of like a machine where, you know, you don't know the exact internals, but, you know, like don't make it too hot or it'll explode.
[1619.20 --> 1621.66]  Right. Like don't make your learning rate too high. It's not going to work. Right.
[1621.66 --> 1625.58]  So you can see not just learning rate, but other sorts of precursors earlier.
[1625.58 --> 1632.36]  Like you can look at various like norms or other quantities to understand, like, is this like, you know, getting too large?
[1632.36 --> 1635.18]  Is this growing large over time? Is this something that's actually too small?
[1635.28 --> 1638.76]  And like we want to, you know, we can actually up the learning rate later.
[1638.76 --> 1641.84]  Or do we need to apply more regularization of a particular type?
[1641.94 --> 1646.86]  Like you can kind of get a sense for these things, even if we don't have kind of perfect laws yet.
[1646.86 --> 1651.82]  We also get some laws out of like the CARB hyperparameter optimizer that I mentioned before.
[1652.12 --> 1663.84]  We can see things like how do these parameters change with a scale and understand like, you know, not just how do the learning rate and data and parameters change, but how do very specific hyperparameters change?
[1663.84 --> 1667.00]  Like what is the depth versus width that you should have?
[1667.20 --> 1672.00]  Like for this particular type of regularization, like how much exactly should you have and how is that changing?
[1672.30 --> 1676.32]  And that goes back and kind of informs like, OK, like what is actually happening under here?
[1676.32 --> 1679.40]  Like it's weird that like this particular trend holds over scale.
[1679.40 --> 1681.04]  Like it seems like it needs less and less of this.
[1681.08 --> 1682.14]  Like that's kind of interesting.
[1682.24 --> 1682.86]  Why is that?
[1683.18 --> 1685.50]  And sometimes we'll see a paper that's like, oh, that fits in.
[1685.60 --> 1686.56]  I see what's going on there.
[1686.64 --> 1687.06]  That's nice.
[1687.56 --> 1688.48]  So we're getting more and more.
[1688.66 --> 1693.52]  I think collectively as a machine learning community, we're also starting to understand these things a lot more.
[1693.80 --> 1698.98]  I think when people point at, you know, neural networks or language models as like black boxes, like, oh, nobody understands.
[1699.32 --> 1701.66]  I think that's quite a mischaracterization of it.
[1701.94 --> 1705.44]  There are a lot of people that have a lot of very good ideas about how these things work.
[1705.44 --> 1711.82]  And nobody on this call probably knows exactly how a car works and that, yeah, I don't think you can make a car from scratch.
[1711.90 --> 1712.64]  I certainly couldn't.
[1712.76 --> 1714.92]  There are especially modern cars that are quite complicated.
[1715.28 --> 1716.86]  But we can use cars to go wherever we need.
[1716.94 --> 1718.18]  And we like roughly know how they work.
[1718.26 --> 1720.32]  So it would be weird to say like, oh, we don't know how cars work.
[1720.38 --> 1725.32]  I think machine learning and neural networks are a lot more like that than most people kind of put us credit for.
[1725.32 --> 1736.18]  What's up, friends?
[1736.30 --> 1740.24]  Is your code getting dragged down by joins and long query times?
[1740.50 --> 1742.82]  The problem might be your database.
[1743.20 --> 1745.86]  Try simplifying the complex with graphs.
[1745.86 --> 1752.54]  A graph database lets you model data the way it looks in the real world instead of forcing it into rows and columns.
[1753.02 --> 1756.42]  Stop asking relational databases to do more than what they were made for.
[1756.92 --> 1764.54]  Graphs work well for use cases with lots of data connections like supply chain, fraud detection, real-time analytics, and generative AI.
[1765.10 --> 1769.30]  With Neo4j, you can code in your favorite programming language and against any driver.
[1769.54 --> 1772.14]  Plus, it's easy to integrate into your tech stack.
[1772.14 --> 1774.80]  People are solving some of the world's biggest problems with graphs.
[1775.14 --> 1775.90]  And now it's your turn.
[1776.18 --> 1779.26]  Visit Neo4j.com slash developer to get started.
[1779.64 --> 1783.12]  Again, Neo4j.com slash developer.
[1783.50 --> 1787.98]  That's Neo4j.com slash developer.
[1787.98 --> 1799.98]  Neo4j.com slash developer.
[1799.98 --> 1800.98]  Neo4j.com slash developer.
[1800.98 --> 1801.98]  Neo4j.com slash developer.
[1801.98 --> 1814.70]  So, Josh, going into the break, you had a really good analogy there about the fact that, you know, the sophistication of cars, it means that while we all use them all the time, we may not understand every aspect of them.
[1814.70 --> 1819.74]  And I wanted to go back for a moment because I've been kind of percolating on some of the things that you said earlier.
[1819.92 --> 1823.24]  And you've been talking about kind of the trust and robust systems and all.
[1823.36 --> 1830.18]  But I was wondering, I know in my own life, I'm very involved in the trustworthiness of models.
[1830.18 --> 1835.46]  And you talked a bit about, you know, getting good outcomes and being able to detect that.
[1835.80 --> 1843.32]  Do you have any guidance on what it means to engineer trust into model training?
[1843.68 --> 1851.00]  So many organizations that I've seen kind of tag the trustworthiness of models on at the end as though, oh, yes, we have to do that too.
[1851.00 --> 1859.80]  And with you have such a insightful and deep way of approaching the engineering, you know, rejecting the black box approach.
[1860.06 --> 1874.56]  Any guidance you have on how you engineer trust in it from up front so that as you get through the training life cycle, you come out with something that kind of you have a high degree of confidence is what you're intending it to be.
[1874.56 --> 1881.94]  I think a lot of people are trying to do this and there is good work to be done there and we can do things to improve the models and make them more trustworthy and during training.
[1882.04 --> 1887.22]  And that's great. But I think by far the largest place that we should be focusing is actually after training.
[1887.46 --> 1892.92]  We don't trust people because like, oh, I looked at their schooling and like, you know, they seem real trustworthy up to this point.
[1893.00 --> 1895.16]  Like, I'm going to give them my credit card and I'm going to give them my bank account.
[1895.32 --> 1899.96]  Like, no, you know, we're going to be like looking like, what is this person doing?
[1900.10 --> 1901.84]  You know, OK, we're going to be checking things afterwards.
[1901.84 --> 1908.84]  Like, you know, there's a lot of other stuff that needs to happen post training and in deployment where we can actually trust things.
[1908.94 --> 1921.48]  So I think for me, it's actually a lot more about like what is happening when you're actually using the model, like what kind of auditing or real time verification or user interaction or other sorts of checks or things that you have.
[1921.48 --> 1923.98]  Can you have other systems that are checking the behavior of this?
[1924.12 --> 1930.84]  Like for an agent, you know, maybe you'd want to predict, like, is this action going to have potentially going to have a negative consequences?
[1930.84 --> 1934.62]  Or is this going to be potentially dangerous or will this be something that the user might not want?
[1934.88 --> 1940.76]  And those seem like good things to have as totally separate systems that are completely unrelated to the development of your original model.
[1941.12 --> 1944.84]  You would not want the original model to be responsible or connected to this at all.
[1944.92 --> 1947.54]  You'd want to have a totally separate thing that's looking at this. Right.
[1948.02 --> 1958.70]  And so I think trust is better thought of as like a set of different types of data that can give you confidence that things are going well, that have gone well and will continue to go well.
[1958.70 --> 1964.36]  And so you can only get so much trust up ahead by kind of designing the system in a particular way.
[1964.48 --> 1968.60]  And you have to understand, like, what is that model good at?
[1968.72 --> 1971.72]  What distribution was it trained on? Have we shifted from that distribution?
[1972.18 --> 1975.56]  Have we shifted from the task that it's good at? How well has it done over time?
[1975.92 --> 1978.20]  Is it likely to go wrong in this new example?
[1978.48 --> 1982.20]  So I think it's more of a post training, more of a practical kind of a problem.
[1982.20 --> 1989.96]  And the idea that we could like solve this all by making like safer, trustworthy models is a little bit it's going to be difficult to succeed at that task.
[1990.72 --> 1997.02]  Maybe this ties into the trust element, certainly the kind of collaborative approach with agents.
[1997.02 --> 2004.16]  But you do talk also a lot about some of the thinking that you're doing around interfaces as well.
[2004.62 --> 2012.70]  And it sounds like you've also been utilizing or trying to utilize some of what you're developing internally for coding and other things.
[2012.90 --> 2026.60]  So what are you thinking about in terms of interfaces and kind of how are you dogfooding some of those things internally to kind of learn about interfaces beyond the kind of AI chat interfaces that we're all familiar with?
[2027.02 --> 2036.22]  Yeah. So I think the learning internally from using our own kind of prototypes and internal products and demos has been there's been quite a lot of that.
[2036.68 --> 2042.30]  Like without actually using it, it's hard to kind of get this learning about like, OK, you know, is this trustworthy or not?
[2042.36 --> 2045.32]  Or like, does this actually work? Like what UI do I want to use for this?
[2045.64 --> 2048.96]  I think when I, you know, I made some prototype, it generates a bunch of code.
[2049.06 --> 2052.46]  And very quickly I started to realize like, hmm, that's great.
[2052.58 --> 2055.20]  But like, it's really annoying to review this much code. Right.
[2055.20 --> 2058.66]  I see a lot of products out there that are like, oh, look, it'll like make a PR for you.
[2059.08 --> 2064.00]  Yeah. I mean, how fun is it to review a PR of, you know, a few hundred lines if there's like a few lines that are wrong?
[2064.10 --> 2067.68]  You have to like search through for this bug. It doesn't really tell you anything about where it is.
[2067.72 --> 2070.76]  Like this is just a really awful user experience.
[2071.26 --> 2076.44]  And so I think instead, if we approach it from the perspective of like, OK, what do I want as the user here?
[2076.88 --> 2081.94]  What I want is for this to be pretty interactive and for this to tell me like, OK, maybe there is a bug here.
[2081.94 --> 2087.98]  Or, yeah, you asked me to make this PR, but like your ask was like kind of ambiguous and I needed to make some assumptions.
[2088.10 --> 2090.28]  Here's the assumptions I made. Like, here's how confident I am.
[2090.52 --> 2092.42]  Do you want to change them? Yes, I do.
[2092.64 --> 2101.86]  OK, like once it's more interactive, once you're going back with the back and forth with the user and trying to flag places of ambiguity, uncertainty, risk, etc.
[2101.86 --> 2107.00]  To the extent that you can be correct about those, it can make the user experience feel a lot, lot better.
[2107.52 --> 2117.12]  Any anecdotes from your own sort of internal experiences with these or things that you've tried either on the positive or negative side?
[2117.56 --> 2121.60]  One thing that I really like about Copilot, just as an example, is that it keeps it short, right?
[2121.60 --> 2122.46]  So it's easy to review.
[2122.88 --> 2127.84]  I think when Copilot style things make these huge like generations, that's why they normally don't.
[2127.84 --> 2131.36]  It's because it's kind of hard to review it and to trust it and to like do that.
[2131.40 --> 2136.50]  But I'm imagining that people are probably going to get to a world where they realize like, oh, OK, this is kind of annoying.
[2137.00 --> 2141.12]  Maybe you could point out, you know, places where there are potential bugs.
[2141.12 --> 2144.78]  Like, can you just tell me what lines like seem like the most suspect?
[2144.88 --> 2152.86]  So we, for example, made some, you know, like internal error checkers and linters that will sort of highlight like, oh, OK, yeah, you know, this thing's not even important.
[2153.06 --> 2155.34]  Like your editor does this for you, right?
[2155.34 --> 2160.62]  You can also highlight things like, hey, this spec doesn't look like it was actually properly implemented here.
[2160.70 --> 2165.02]  Or this function specification is like kind of ambiguous for these edge cases.
[2165.18 --> 2166.68]  Like, do you want to take a look at that?
[2166.96 --> 2171.28]  A lot of the work that we've done for our evaluations is related to this as well.
[2171.74 --> 2181.98]  So when we look at evaluation data, most of the time when systems fail, it's actually from like under specification and not from, oh, the model like messing it up fundamentally.
[2181.98 --> 2184.74]  It's more like as a user, I didn't really decide what I wanted.
[2184.74 --> 2193.58]  So I think one thing that's really interesting to me is that coding is not really about like pure correctness in this like abstract mathematical form where there's like a perfectly correct version of this.
[2193.86 --> 2197.22]  The version of the function that you want and that I want are actually subtly different.
[2197.38 --> 2201.58]  And like what I want in the moment might change, you know, from moment to moment as well.
[2202.08 --> 2204.66]  And so the user like really needs to be connected to that.
[2204.66 --> 2211.94]  And as it happens, I also, you know, learn about things where I'm like, hmm, yes, you did exactly what I wanted, but that turned out to be not a good idea.
[2212.46 --> 2217.54]  And so I think the user needs to be there and able to learn and refine like what they even want and what's even possible in the world.
[2217.54 --> 2219.76]  So you peeked my interest in there.
[2219.90 --> 2226.04]  It's with as a coder myself who makes all sorts of errors in my code constantly.
[2226.04 --> 2243.66]  As you're doing that and you're kind of changing the workflow over time of how the coder is spending their time and then ultimately potentially how they're thinking about coding as they adjust to the new approach that your tools are doing.
[2243.66 --> 2250.98]  How does that look for the coder going forward in terms of how does it change their day to day experience of coding?
[2251.18 --> 2259.26]  Are you able to rescue me from spending 90% of my time coding errors and forever trying to get myself back out of that hole?
[2259.52 --> 2273.60]  That's really like the vision for Imbue and for the company and for the work that we're doing is can we get to a place where people, not just coders, but other even non-technical people can effectively write higher level pseudocode or code or
[2273.60 --> 2280.20]  intent and actually have this translated into real code and into something that actually makes your computer do what you want.
[2280.54 --> 2290.12]  That's why when we're talking about making a new personal computer, et cetera, we're really at the end of the day, the thing that is missing is the ability to robustly write this software.
[2291.08 --> 2295.02]  And we can as software engineers get down to the details and get everything there.
[2295.08 --> 2297.28]  We spend a lot of time fixing our own bugs, et cetera.
[2298.00 --> 2303.18]  And our goal is to make it so that as a user, you can keep working at a higher and higher level of abstraction.
[2303.60 --> 2304.88]  And feel confident in that.
[2305.00 --> 2308.44]  Right now, you can work at a super high level of abstraction to say, like, make this whole thing for me.
[2308.82 --> 2309.42]  It doesn't work.
[2309.54 --> 2311.90]  And so that's not very fun because it's busted.
[2312.12 --> 2314.26]  And now you like, how do you get into the details, et cetera?
[2314.26 --> 2325.64]  So how can we make it robust enough so that you can work at a higher level of abstraction and trust that this part was actually correct and be able to have that dialogue back and forth when like, OK, you know, maybe it's not quite working like I want it.
[2325.66 --> 2329.84]  Or maybe it's not possible to do this thing or not as easy to do it in the way that I wanted to do it, et cetera.
[2329.84 --> 2336.80]  So how do you have a dialogue and help educate the person about what is possible, what isn't working, what might not be working, where they should dig in?
[2337.22 --> 2338.86]  So it changes the workflow.
[2339.32 --> 2342.60]  And I think we're interested in how do you change this workflow in a slightly more incremental way.
[2342.98 --> 2348.14]  You could, you know, just say, like, oh, we're going to have the AI system do everything for you and like magically try and figure it out.
[2348.14 --> 2355.80]  But I think from our previous experience, we don't think that these types of products are nearly as good to use as a user experience.
[2356.00 --> 2362.96]  Like trying to fully automate something kind of is disempowering to people and also results in kind of a worse experience and a worse product.
[2362.96 --> 2371.88]  So we're more interested in this like interactive dialogue, like tool that as a person I'm trying, like maybe, you know, you can just write a line of pseudocode.
[2371.98 --> 2372.84]  You get a big block out.
[2372.96 --> 2376.60]  It tells you like one line that is, you know, potentially problematic for you to look at.
[2376.66 --> 2377.52]  Or maybe it just gets it right.
[2377.66 --> 2378.02]  OK, great.
[2378.08 --> 2379.02]  You can move on to the next one.
[2379.42 --> 2380.20]  So that's like one.
[2380.32 --> 2383.58]  Imagine like one way that you can think about writing code is like writing pseudocode.
[2383.66 --> 2384.88]  But there's other ways you could write it.
[2384.94 --> 2388.50]  You might also write a command like, you know, change the file to add lots of log statements.
[2388.50 --> 2392.36]  Or you might also, you know, say like make this function more robust.
[2392.64 --> 2395.56]  Or there's like lots of different ways that you can interact with this.
[2395.64 --> 2403.12]  And how can we give people more tools, more like paintbrushes for being able to change code and ultimately like make their computer do what they want?
[2403.12 --> 2414.88]  I think the thing that's really exciting about this is that when you can robustly write software, what you're really doing is being able to create agents that can do a huge swath of tasks.
[2414.88 --> 2423.60]  If you're not able to write robust software, then the only way your agent can interact with your computer is with things that we have already programmed as actions.
[2423.60 --> 2426.04]  Like, OK, we programmed it to go to a website and like click a button.
[2426.24 --> 2426.60]  That's it.
[2426.92 --> 2433.60]  But if it can write software, now it can do some huge set of things and even things that you never intended or programmed in the first place.
[2434.02 --> 2438.08]  So for us, like agents and writing code and reasoning are all like intimately connected.
[2438.86 --> 2441.18]  I have one more tiny follow up to that.
[2441.34 --> 2443.34]  It's a personal thing I run into all the time.
[2443.34 --> 2446.66]  And having someone with your expertise, I want to throw it at you.
[2447.04 --> 2448.62]  Does it make a difference?
[2449.18 --> 2455.68]  Is most software developers, including people in the AI space doing models and stuff, you know, they write in Python.
[2456.04 --> 2458.78]  They write in usually a variety of different languages.
[2459.18 --> 2470.06]  And as I shift from one to the other, I find that some of the capabilities that are currently out there, they are great on Python because everyone on the planet is writing Python.
[2470.06 --> 2481.76]  But if I'm writing on something that's slightly more obscure, maybe even something big like Rust, it struggles to do the exact same thing that it can do flawlessly on the Python side.
[2481.76 --> 2491.02]  Do you anticipate a time where that context shifting no longer applies very well and that they're all high fidelity in terms of what they can do?
[2491.02 --> 2497.34]  Are we always going to be dogged a bit with the obscurity issue of certain languages?
[2497.84 --> 2499.50]  It might go the other way.
[2499.62 --> 2504.04]  It might be that like because it's so much more robust in Python, we should only ever write in Python.
[2504.54 --> 2510.46]  And so what we do is we just write in Python and we make a Python to Rust converter or we make a thing that assembles Python to assembly or whatever.
[2510.46 --> 2520.60]  It might be that it's sort of better to like double down on like a really small set of things that we've made tons of data for and works really robustly because you get a better kind of user experience.
[2520.88 --> 2528.50]  Like one of the things that, you know, a lot of these models struggle with now is like you have different versions of like NumPy or Python or Ubuntu or whatever.
[2529.14 --> 2529.78]  Things are different.
[2529.98 --> 2531.60]  How is it supposed to know what version you're using?
[2531.74 --> 2531.86]  Right.
[2531.86 --> 2537.48]  And so there's this combinatoric like explosion of like complexity that comes from all these different possibilities.
[2538.18 --> 2542.14]  And so, you know, an alternative way to do this would be to say, you know what, let's not do that.
[2542.28 --> 2544.40]  Let's just say you've got a Ubuntu 22.04.
[2544.64 --> 2545.72]  You've got this library version.
[2545.80 --> 2546.40]  You've got that one.
[2546.46 --> 2548.66]  Like if you do this, I think it might work a lot better.
[2548.68 --> 2550.42]  So it could go actually in the other direction.
[2550.80 --> 2556.22]  Instead of it making it more robust on all these niche things, we might say like, you know what, just all work in that level.
[2556.28 --> 2557.92]  And like, let's not worry about what language it writes.
[2557.98 --> 2559.26]  Maybe we only write at this higher level.
[2559.32 --> 2560.52]  We never even look at that code anymore.
[2560.52 --> 2562.20]  So we don't care if it's in Rust or Python.
[2562.62 --> 2569.00]  I think once that happens, once we sort of abstract it up a level, then you might be able to come back and say, why are we writing this in Python?
[2569.16 --> 2570.70]  Like, this is not a type safe language.
[2570.78 --> 2571.58]  This is really slow.
[2571.70 --> 2576.10]  Like, why don't we change it to like be a language that fits better for language models?
[2577.02 --> 2578.90]  And that might be an even better future thing.
[2578.92 --> 2582.02]  But that will require generating a ton of data to make this actually work.
[2582.54 --> 2586.44]  So I see that as like maybe probably a future thing, not a thing to focus on right now.
[2586.44 --> 2588.52]  But that's my guess as to how it will evolve.
[2588.52 --> 2593.16]  But also an alternative world would be, you know what, it gets really cheap to just generate all this data.
[2593.44 --> 2600.84]  So we just make a converter from all of our Python pre-training data to just make it do it in JavaScript and Rust and Elixir and whatever all the time anyway.
[2601.50 --> 2602.34]  So fine.
[2602.60 --> 2604.22]  We just like train it to be good on all these.
[2604.46 --> 2604.66]  I don't know.
[2604.70 --> 2605.50]  We'll see which way it goes.
[2605.50 --> 2611.32]  Yeah, well, Chris will be happy if anything stays in Rust, I'm sure.
[2611.58 --> 2612.30]  I wasn't saying that.
[2612.30 --> 2612.72]  You'll be happy.
[2612.98 --> 2617.98]  We just started working on our official Rust client for PredictionGuard, Chris.
[2618.24 --> 2619.72]  So you can be a beta user.
[2620.08 --> 2620.56]  There you go.
[2620.56 --> 2622.60]  It's been great to talk through.
[2622.92 --> 2632.30]  Again, I love this concept of this sort of full stack approach that you're taking and triggering things in my own mind to think through in my own work.
[2632.30 --> 2645.82]  But as you look forward, either you personally or you at Imbue look forward to kind of the things that are happening this year, either in the community as a whole or at Imbue.
[2645.82 --> 2665.44]  What's kind of most exciting for you that you see as a possibility kind of coming into the future, whether that be multimodal stuff or new types of agents or products or directions that the community is going or the research is going?
[2665.96 --> 2670.06]  What kind of stands out to you about that as you look to the future?
[2670.06 --> 2684.06]  I think the thing that is going to be most exciting over the next year or two, at least for us internally and probably for other providers externally, is I think we're going to make really good progress on what we have been talking about today on actually reasoning on robustness.
[2684.72 --> 2693.22]  Like, I think once you can get to a place where you ask this question and you get back an answer that is really correct and like robust and grounded, it's not just, oh, it said yes.
[2693.22 --> 2701.42]  But like it has all the right reasons and it kind of like understands the nuance of like, OK, yeah, it's like yes-ish, but like there's like a little bit of complexity here.
[2701.50 --> 2703.94]  You can ask follow up questions and those are also right and robust.
[2704.16 --> 2712.54]  Like that ability to robustly reason and answer questions is going to unlock some huge amount of work that I think people are not really anticipating.
[2713.16 --> 2720.74]  Like once we really have the ability to robustly reason through scenarios, now we're talking about a lot more like labor displacement and disruption than we were before.
[2720.74 --> 2728.32]  There's a lot of jobs that like all of us like can pretty easily put together like, well, first I do this, then I do that, then I think about this.
[2728.46 --> 2732.88]  Like, OK, it only takes like one person to do that when you have these tools that are that powerful.
[2732.88 --> 2738.94]  So I think there's going to be a lot more change in this area than people are really expecting right now.
[2739.56 --> 2746.76]  You know, it's not to say that all jobs disappear or something, but the nature of work might change pretty dramatically and we might have like much more powerful tools than I think people are anticipating.
[2746.76 --> 2760.42]  Right. Yeah. Well, we were really happy that imbue is thinking deeply about those things as we look to the future and at a really practical and useful way as we look forward.
[2760.56 --> 2765.42]  So thank you for doing that. Thank you for your research and for taking time to join us. This has been great.
[2765.80 --> 2767.52]  Yeah, that's been great. Thanks a bunch, guys.
[2767.52 --> 2778.62]  All right. That is Practical AI for this week.
[2779.34 --> 2792.00]  Subscribe now. If you haven't already, head to practicalai.fm for all the ways and join our free Slack team where you can hang out with Daniel, Chris and the entire ChangeLog community.
[2792.00 --> 2797.22]  Sign up today at practicalai.fm slash community.
[2797.52 --> 2810.34]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening. We appreciate you spending time with us. That's all for now. We'll talk to you again next time.
[2810.34 --> 2811.08]  Bye.
[2811.08 --> 2818.64]  Bye.
[2819.92 --> 2821.16]  Hang on.
[2821.22 --> 2821.26]  Bye.
[2821.68 --> 2837.18]  Bye.
