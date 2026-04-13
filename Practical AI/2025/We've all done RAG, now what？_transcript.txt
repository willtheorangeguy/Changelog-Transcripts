[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.64 --> 19.16]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.54 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.46 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind the scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.18 --> 37.50]  Now, on to the show.
[48.62 --> 52.16]  Welcome to another episode of the Practical AI Podcast.
[52.60 --> 53.80]  I'm Daniel Whitenak.
[53.80 --> 60.98]  I am CEO at Prediction Guard and not joined by Chris today, but very happy to be joined
[60.98 --> 70.60]  by a longtime friend of the podcast and friend of all things AI and data science online, Rajiv
[70.60 --> 77.92]  Shah from Contextual AI, where he's the chief evangelist and also, of course, a TikToker
[77.92 --> 80.60]  extraordinaire and all things.
[80.84 --> 82.74]  So welcome back to the show, Rajiv.
[82.74 --> 83.56]  It's great to have you.
[83.80 --> 84.70]  It's great to be back.
[85.00 --> 85.68]  Excited to talk.
[85.80 --> 85.98]  Yeah.
[86.06 --> 89.68]  And we're close neighbors around the Midwest as well.
[89.76 --> 95.58]  I'm looking forward to seeing you at the Midwest AI Summit, which if listeners don't know, both
[95.58 --> 102.32]  Chris and I will be at the Midwest AI Summit, which is happening November 13th in Indianapolis.
[102.32 --> 112.42]  So I think as you put it on LinkedIn, Rajiv, if you live anywhere near Korn and you like AI, then this is the place to be.
[112.52 --> 121.06]  And actually, Rajiv will be there giving a great talk about kind of this idea of, I think you're going to be talking about this stat,
[121.18 --> 125.06]  the 95% of pilots that fail, why that might be.
[125.06 --> 125.50]  Yeah.
[125.50 --> 125.68]  Yeah.
[125.82 --> 132.76]  So great to have a fellow Midwest AI Silicon Prairie friend on the show as well.
[132.98 --> 135.60]  No, it's great to have these in-person events here in the Midwest.
[136.10 --> 138.84]  Usually you have to kind of fly out to some large city to get that.
[139.12 --> 141.26]  It's nice to be able to kind of get that right into Indy.
[141.44 --> 141.76]  Yeah.
[141.84 --> 142.06]  Yeah.
[142.06 --> 149.74]  So if you're interested in that, go to midwestaisummit.com and make sure and register for that.
[149.82 --> 151.86]  Hopefully we'll see you there in person.
[152.02 --> 153.76]  It's going to be a fun time.
[153.92 --> 159.60]  But it has been a while since we've had you on the show, Rajiv, and I'm sure there's a lot to catch up on.
[159.60 --> 170.74]  It almost seems like last time we talked, there was kind of, we were all getting into RAG and thinking about, you know, agents and reasoning models.
[170.74 --> 172.36]  We're trying things.
[172.48 --> 181.18]  People were kind of gradually developing maybe what they thought would be a direction for kind of best practices or ways to approach problems.
[181.64 --> 197.86]  It would be interesting to hear kind of from then to now how you've seen that world advance and kind of these archetypal use cases that people are addressing with retrieval and related frameworks.
[198.44 --> 198.54]  Yeah.
[198.64 --> 200.02]  No, it's been amazing, right?
[200.02 --> 205.74]  About two and a half years ago, we were really giddy about the possibility of AI, but there was a lot of different things that we can do.
[205.74 --> 216.94]  And kind of since then, we've seen AI develop in certain ways where, for example, in code completion, code development tools, it's accelerated dramatically even over the last year like that.
[216.98 --> 220.38]  And we're all kind of using those tools on a regular basis.
[220.38 --> 226.10]  And then in other areas, right?
[226.10 --> 230.32]  We've also seen that there's some things that are difficult to do with chatbots as well.
[230.32 --> 247.34]  But I think, you know, it's been incredible to see just the continued development of AI in terms of the capabilities, the smartness, the ability to kind of use tools to find search information that there's still so much for all of us to do in our lives, the kind of those of us that work with AI.
[247.34 --> 247.78]  Yeah.
[247.78 --> 248.10]  Yeah.
[248.10 --> 248.22]  Yeah.
[248.22 --> 248.58]  Yeah.
[248.58 --> 277.46]  And I guess, like, certainly there's a lot of people still, I guess when I interact with customers or hear from other people in the industry, like still a lot of people are wanting as their first things to kind of whatever is build a rag chatbot, which maybe for those listeners out there that are maybe not as familiar with this, they've maybe heard, you know, rag this and raggedy rag that and all of that.
[277.46 --> 286.30]  Maybe just remind listeners, like what rag is and like how retrieval, you know, may fit into some of this AI stuff.
[286.50 --> 286.68]  Yeah.
[286.88 --> 288.36]  And I'll start simply.
[288.64 --> 297.14]  Even a couple of years ago, I was kind of working with the earliest large language models and people would be like, I like chat GPT, but it doesn't know anything about me or my company.
[297.66 --> 300.26]  Like, how can I train it to know all that knowledge?
[300.26 --> 305.60]  And what we figured out is that it's not about really training that model about the knowledge.
[305.72 --> 313.02]  It's instead finding that knowledge, searching that knowledge, passing that on to the model and then be able to use that.
[313.16 --> 322.40]  And that's where kind of this idea of retrieval, finding stuff, and then augmenting the generation, augmenting the written response for that came about.
[322.40 --> 330.50]  And I think rag today is kind of one of the most important or it's one of the most widely used use cases, I'd say, in the generative AI space.
[331.16 --> 331.26]  Yeah.
[331.36 --> 338.84]  Like every company is probably running some type of rag at this point for searching its internal knowledge, right?
[338.88 --> 343.46]  Helping folks figure out through HR documentation, using it for customer support.
[343.58 --> 347.38]  There's a lot of use cases where we have huge amounts of information.
[347.38 --> 353.18]  We want to be able to find things from that, but we also want to use the smarts of AI for that.
[353.32 --> 356.26]  Like we don't want to Google search results of 20 things, right?
[356.28 --> 361.76]  Like we want a nice like AI summary of it, or we want to extract all the information.
[361.88 --> 363.90]  I just want the names and dates out of all this.
[364.00 --> 365.14]  I don't need to read every one.
[365.66 --> 371.08]  And so that's where the AI really comes into it and why rag is so powerful and we see it so widely used.
[371.08 --> 371.56]  Yeah.
[371.70 --> 377.62]  And I love what you were saying, just sort of contrasting this with training or even fine tuning.
[377.88 --> 384.68]  I find this, of course, to be a very widespread misconception about how these tools work.
[384.90 --> 396.60]  Even chat GPT, the application, like it does seem like it kind of quote trains on your information that you put in, your previous chat history, et cetera.
[396.60 --> 401.20]  And then like, it's almost like you have a model of your own, right?
[401.28 --> 411.60]  Which seems like, it almost seems like OpenAI has a separate model for every person on the planet, which is not feasible from the data science training perspective.
[412.30 --> 419.20]  So could you highlight some of those things and just highlight, I know you educate a lot as well.
[419.26 --> 420.70]  So I'm sure you've seen this as well.
[420.70 --> 427.28]  Well, there's kind of this jargon of training thrown around a lot, which is confusing maybe in how it's used.
[427.64 --> 428.02]  So, yeah.
[428.24 --> 428.52]  Yeah.
[428.60 --> 436.72]  And I think partly is a lot of these companies want to make you think that they have like one thing that does everything in the world.
[437.02 --> 441.14]  But if you actually take a look at something like chat GPT, it's a system.
[441.24 --> 443.12]  It actually composes of multiple parts.
[443.64 --> 448.38]  So if you were trying to build your own chat GPT, these are some of the things that you would have to think about.
[448.38 --> 452.20]  So one is I need to be able to retrieve from lots of different sources.
[452.42 --> 456.54]  I have all my knowledge inside my companies inside of Confluence.
[456.74 --> 458.56]  I need to be able to access and retrieve that.
[459.02 --> 459.98]  That could be one thing.
[460.50 --> 464.02]  So one thing is using RAG, being able to access tools.
[465.22 --> 466.26]  Another thing is memory.
[466.60 --> 476.98]  Like I wanted to remember that last conversation I had, whether it was two things I said ago or like one of the nice things about chat GPT is you can come back a conversation or a day later.
[476.98 --> 478.72]  And it remembers a lot about you.
[478.84 --> 483.66]  It may be a little bit scary sometimes how much it remembers about you and how well it can profile you.
[484.40 --> 497.12]  And so this is kind of what we see inside of AI engineering as context engineering, where there's a number of different parts of managing interactions with these models.
[497.12 --> 507.16]  Whether it's RAG, whether it's remembering the memory, when it's knowing how to summarize conversations to do things like multi-turn so we can have those repeated conversations.
[507.44 --> 511.46]  But keep track of what was said earlier in our conversations as well.
[511.80 --> 511.92]  Yeah.
[512.08 --> 514.88]  So I love that idea of context engineering.
[514.88 --> 527.06]  How is that idea of context engineering kind of different from like what we would maybe from the data science, traditional data science side consider like model training, I guess.
[527.06 --> 536.14]  So there's almost like a pipelining mindset versus an actual like GPU model training piece.
[536.14 --> 536.58]  Yeah.
[536.80 --> 544.66]  You know, I think what's what's remarkable nowadays is the amount of information that's stored inside of these large language models.
[545.04 --> 553.38]  I do a thing when I kind of talk about large language models where imagine if you were sitting outside and kind of reading a book and you could read all day, all night.
[553.54 --> 558.44]  If you read for 10 years, I think that's on the order of something like about a billion tokens.
[558.44 --> 562.86]  And these models are trained on the order of like 15 trillion tokens.
[563.52 --> 568.96]  So it's just an inconceivable amount of information that these models hold inside there.
[569.30 --> 579.60]  And I think one of the biggest, biggest improvements we've seen in these models is not only kind of stuffing all that information in there is effectively using all of that information in there.
[579.60 --> 584.40]  That these models really today are untapped in terms of everything they can do.
[584.40 --> 599.58]  And it's one of these things on the technical side is why you see that the capabilities of the models have continued to grow without them necessarily having to grow immensely in size, simply because we're better tapping into all the abilities that they have inside them.
[599.94 --> 600.08]  Yeah.
[600.76 --> 610.78]  And I know you're up for this because we know each other, but I'll present a scenario to you that sometimes comes up for us.
[610.78 --> 617.96]  And, you know, whether I'm teaching a workshop or something and you can help us understand how this retrieval type of thing fits in.
[617.96 --> 629.54]  So I often, maybe I'm talking to folks in healthcare and what's interesting is there's all of this, you know, huge amount of data that these models have been trained on.
[629.74 --> 634.78]  And there is good, let's say, medical information in that data, right?
[634.78 --> 640.02]  Or there's like care guidelines for nurses or medics or whatever it is.
[640.04 --> 641.28]  Let's take that as an example.
[641.28 --> 658.78]  The interesting thing is there's even like if you think about factuality in a situation, it is kind of relative in the sense that if I'm a medic that works for this provider, let's say their care guidelines are different from another provider.
[658.78 --> 669.58]  Or if like I'm treating, you know, maybe children, those guidelines are probably different than if I'm treating adults or senior adults or something like that.
[669.62 --> 673.90]  So there can be these facts out there that are actually conflict with one another.
[674.04 --> 676.50]  And it's really, you know, you talked about the context.
[676.50 --> 680.34]  It's really about the context that you're working in, what it should pull.
[680.34 --> 685.90]  So these models, assuming that all that information is public, right, like you said, it's been scraped off the internet.
[686.46 --> 694.02]  All of that's kind of, you could imagine that maybe somehow that is embedded somewhere in the model, the base model.
[694.18 --> 698.56]  So whether we're talking about, you know, LAMA or GPT or whatever.
[699.56 --> 705.80]  How can, let's say I'm a healthcare company, but I'm interested now in my context.
[705.94 --> 707.50]  Now, how do I make that connection?
[707.50 --> 716.40]  So still use maybe, I'm not going to retrain that model, but how do I use the model then in this context of kind of conflicting facts?
[717.08 --> 717.76]  Yeah, absolutely.
[717.94 --> 722.06]  As much as the models know and been trained so widely, they don't know everything.
[722.38 --> 724.84]  And so sometimes that's, you have your own information.
[725.06 --> 727.12]  You want to pass that into the model.
[727.20 --> 732.20]  And so that's where that retrieval augmented generation comes in, where you want to grab that information.
[732.46 --> 734.58]  And then we want to pass it into the model.
[734.58 --> 750.20]  And this is where, for folks who are in the space for a while, prompt engineering comes into play, where we think about the inputs that go into the model, where we take the facts that we know about our own given situation, along with maybe some instructions for what we want along with it.
[750.20 --> 753.44]  And that all of that is manipulating the context, right?
[753.44 --> 756.22]  The larger world that this model is sitting within there.
[756.34 --> 766.14]  And by manipulating and giving it information, instructions and other facts, we can get outputs that more, that better match kind of what we're looking for like that.
[766.46 --> 766.62]  Yeah.
[766.78 --> 767.76]  Yeah, that's great.
[767.76 --> 773.36]  And I guess, you know, there's another term that's been thrown around the last couple of years.
[773.76 --> 776.92]  One would be this kind of retrieval piece, which you've talked about.
[776.92 --> 785.62]  And this idea that in the context of a certain question or something, I'm able to connect to one of my internal data sources, get that right information.
[786.66 --> 791.06]  There's this other thing that would be related to reasoning.
[791.06 --> 801.18]  Now, some people might kind of just consider that all kind of generative AI models reason in one way or another, but it is kind of now almost like a term of art.
[801.34 --> 805.90]  It means kind of a certain thing when we're talking about these models.
[806.06 --> 809.18]  Could you help highlight that also to put that in context?
[809.18 --> 812.26]  And then maybe we'll circle around and combine some of these things.
[812.66 --> 812.82]  Yeah.
[813.12 --> 818.50]  You know, a lot of times when we talk about models, we want to make it convenient to help people explain things.
[818.50 --> 820.90]  And so we kind of anthropomorphize them, right?
[820.90 --> 824.20]  We give them human-like qualities when they're not actually human-like qualities.
[824.72 --> 827.84]  And so, for example, reasoning is something we say for these models.
[827.92 --> 831.14]  Now, they're not reasoning like a human would through a problem.
[831.60 --> 838.76]  But what we typically mean kind of when we think about reasoning with these models is they're doing lots of extra steps.
[838.98 --> 843.56]  And they're doing these steps in a logical way to better solve a problem.
[843.56 --> 856.40]  So if you take kind of a math word problem, a great way to see this is if you take a word problem like the train is moving east, you know, at 50 miles an hour and another train is moving west another 40 miles an hour.
[856.40 --> 858.50]  And you have to figure out like what point they're going to cross.
[858.96 --> 859.12]  Right?
[859.12 --> 861.04]  There's no kind of quick answer to that.
[861.34 --> 867.28]  You need to kind of calculate the first train, calculate the second train, and then you can figure out the solution.
[867.28 --> 874.00]  And what we've done, and that's what these reasoning models have done, is we've trained them that don't come up with the answer right away.
[874.56 --> 875.22]  Think through it.
[875.28 --> 876.30]  Think about the first thing.
[876.50 --> 877.36]  Think about the second thing.
[877.76 --> 880.70]  Connect all the dots and then put an answer in.
[881.26 --> 884.64]  And the way we've done this is we've literally given the model.
[885.10 --> 886.44]  Well, we've trained it in multiple ways.
[886.52 --> 891.72]  But in some ways, we've literally given the model an example of, hey, this is how I solved this word problem.
[891.78 --> 893.46]  I did this all these steps here.
[893.70 --> 896.30]  I want you to learn how to go through these problems step by step.
[896.30 --> 901.38]  And this is where we differ from two and a half years ago when the first models didn't know how to do that.
[901.88 --> 907.06]  Those first models, all we had trained it up was like, hey, tell me if a movie is a good movie or a bad movie.
[907.14 --> 909.56]  Or tell me if this sentiment is happy or sad.
[910.00 --> 912.90]  But since then, we've had time to develop more training data.
[913.34 --> 914.98]  We've given them more complex training.
[915.42 --> 917.72]  And the cool thing is the models have picked up.
[917.84 --> 920.52]  They've been able to learn this capability for doing this.
[920.52 --> 925.94]  And so now we're able to do this much more complex kind of, I'm doing the air quotes of reasoning.
[926.30 --> 927.98]  To solve these problems.
[928.38 --> 928.58]  Yeah.
[928.86 --> 939.94]  I guess one thing that people, and this is part of why I really enjoy watching your videos online, is you often break down a lot of this jargon and kind of help.
[940.26 --> 949.62]  It's almost like people feel the shock of all of this terminology and a new model coming out every 30 minutes or whatever it is.
[949.62 --> 953.40]  And just not really knowing how to deal with that.
[953.54 --> 956.66]  And there's kind of all of these things that have happened.
[956.76 --> 958.14]  So there's reasoning models.
[958.32 --> 959.76]  There's small language models.
[960.10 --> 961.44]  There's tool calling.
[961.66 --> 962.52]  There's retrieval.
[962.78 --> 966.58]  There's like all of these different kind of mix of things.
[966.58 --> 974.22]  Based on your experience and both what you've implemented personally, also what you've seen and interacted with folks on.
[974.22 --> 988.80]  If people could kind of bring in some focus and maybe imagine a company's kind of getting into, you know, AI, however they view AI transformation within their organization.
[988.80 --> 996.18]  And they're thinking about some of the use cases that are kind of the initial ones on their roadmap.
[996.52 --> 1003.30]  At the time being, like what would you encourage them to kind of like pick the signal out of the noise?
[1003.44 --> 1009.44]  So what would you encourage them to maybe focus on to see some of that time to value up front?
[1009.44 --> 1016.44]  Not that they don't want to explore some of the other topics that are happening or, you know, read about them or whatever that is.
[1016.44 --> 1025.02]  But how would you at least recommend kind of to get that best time to value or maybe just the things that are producing the most value?
[1025.02 --> 1032.10]  And you could maybe flip that as well and say, like, what are some of those things that are cool things?
[1032.22 --> 1034.48]  But maybe let's wait and see what happens.
[1034.62 --> 1038.24]  And maybe just sort of don't get distracted at the moment.
[1038.24 --> 1047.14]  Yeah, I mean, you're taking me away from all the full, all the fun, cool technologies that are the latest like automation things that I can kind of fire up like that.
[1047.14 --> 1061.30]  I think, you know, when you're thinking about this from the perspective of kind of a company, if you're kind of a manager in these situations, you have to figure out what use cases you want to put on a very different hat than just thinking about the technology itself.
[1061.70 --> 1068.06]  And I can tell you this, like I was burned from this from personal experience when I was just starting out in data science.
[1068.06 --> 1071.02]  I was entranced by the latest technology.
[1071.02 --> 1073.86]  So I remember, right, we were talking about code development.
[1074.84 --> 1077.40]  Like 10 years ago, I was working at State Farm.
[1077.72 --> 1085.76]  And I think Andrew Karpathy has written his paper about the, I think, like the unreasonable effectiveness of LSTMs.
[1085.86 --> 1086.68]  It was something like that.
[1086.96 --> 1090.58]  But part of that paper had the idea of you could translate code.
[1090.68 --> 1092.74]  You could complete code from one language to another.
[1092.74 --> 1095.44]  And I was like, hey, come on, guys.
[1095.44 --> 1097.70]  Like, we've got a lot of this code sitting around.
[1097.86 --> 1103.32]  Like, give me some, give me a few GPUs and some data and I'll solve this.
[1103.42 --> 1103.54]  Right.
[1103.58 --> 1104.72]  Like, totally naive.
[1104.82 --> 1107.08]  Like, you know, they didn't fund that project or anything.
[1107.08 --> 1112.22]  But I think, yes, it can be very easy to be kind of seduced by the technologies.
[1112.22 --> 1120.42]  Kind of what a shiny demo is versus when you're in an organization, you really have to think about kind of the problems that you have.
[1120.96 --> 1125.98]  Part of it will be, you know, how complicated is this from a technical point of view to get it up and running?
[1126.18 --> 1127.26]  That's one factor.
[1127.86 --> 1129.36]  But that's not the only factor.
[1129.56 --> 1132.78]  We also need to consider, like, what's the value to this organization?
[1132.78 --> 1143.70]  I talk to lots of enterprises on a regular basis and I see often what I call science experiments where teams like the latest technology, they go out and kind of run this stuff.
[1144.12 --> 1150.00]  But there's no way for them to actually get that implemented inside the company in a useful way.
[1150.32 --> 1154.44]  And they're literally just kind of interesting experiments that people are running like that.
[1154.44 --> 1163.26]  Does that get partially to, like, the 95% of AI pilot failing type of report from MIT?
[1163.68 --> 1164.06]  Absolutely.
[1164.38 --> 1168.84]  Now, the 95%, of course, is like a little bit of a hype number that they like to put out in this.
[1169.52 --> 1178.10]  And, right, for those of us who have been in the space for a while, we remember the fact of 80% of data science projects fail, I think was something that we had.
[1178.56 --> 1180.48]  And to some extent, that's okay.
[1180.48 --> 1186.36]  You can't expect every initiative, every experiment, everything that you start to succeed.
[1186.68 --> 1192.66]  You want things to fail because partly is if something works, that means you have to maintain it.
[1192.72 --> 1193.50]  You have to monitor it.
[1193.50 --> 1195.16]  You have to put up a lot of guards around it.
[1195.28 --> 1197.58]  There's a cost for something that actually succeeds.
[1198.06 --> 1202.16]  But when we talk about AI, it's very easy to build a cool demo.
[1202.78 --> 1204.96]  But it's not only the value to the company.
[1205.30 --> 1209.56]  You have to figure out how to integrate this into people's everyday work life.
[1209.56 --> 1214.72]  And so you can build a very shiny widget that sits and can do something awesome.
[1215.10 --> 1233.12]  But if that's not inside somebody's regular workflow of how they work, the tools that they work in, if they're not properly trained on how to use it, if their leadership isn't supporting you to use it, there's lots of factors like that that go into why people might not actually adopt and use a technology.
[1233.12 --> 1234.90]  And it's really nothing about AI.
[1234.90 --> 1239.90]  It's really about organizational change and introducing technology into companies.
[1240.16 --> 1240.28]  Yeah.
[1240.44 --> 1256.56]  I know from just a founder perspective, it can be, you know, just from a different side of this, it can be frustrating when you see like, oh, there's this, you know, company over here that the technology side is fairly simple.
[1256.56 --> 1263.10]  Like, oh, it's just a simple model that does a simple thing or a browser extension that does this.
[1263.10 --> 1268.36]  And you're like, wow, you know, like I could have vibe coded that in a weekend.
[1268.36 --> 1271.22]  Like, how are they, you know, scaling to the moon?
[1271.22 --> 1273.42]  And we have all this cool technology.
[1273.42 --> 1298.82]  And I think part of it is that that side of it that you talked about, like part of the hard problem is cracking what actually does provide value to your organization, what can be adopted, how you communicate that, how you tell that story and how you deliver on your promises, how you provide customer support.
[1298.82 --> 1304.00]  Like a lot of that is not really related to the technology and that component.
[1304.50 --> 1316.28]  So maybe, I don't know if this would be accurate to say, but maybe the first step people could take is just getting something off the ground that's fairly simple and interacts with an AI model.
[1316.28 --> 1324.54]  Maybe it's just to do a very simple task, but really pushing that through, like you say, to be embedded in a product or be embedded in a process.
[1324.72 --> 1339.36]  That may be the best way for people to kind of start that journey is to, yeah, really start from that simple side and deal with some of, in all honesty, the harder problems around the periphery of the technology.
[1339.36 --> 1357.18]  And, you know, I think a big part of that, like what you're saying is just to get closer to those end users, the stakeholders, because I think once you often cut through that, sometimes you figure out that really they don't necessarily need a fancy kind of GPT-5 model to solve their problems.
[1357.18 --> 1362.90]  Maybe you can solve it with almost a simple if-then rule that you can just implement in some place.
[1363.26 --> 1372.88]  And so this is where kind of looking at the data, spending time talking to those end users like that often gives you a much better result, right?
[1372.90 --> 1376.74]  It's going to give you the biggest bang for your buck than going out and reading some archive paper.
[1377.04 --> 1378.44]  Yeah, yeah, that's true.
[1378.44 --> 1385.82]  And I guess now you should just have the AI model read the paper for you and give you some summary points.
[1385.82 --> 1388.18]  I'm a big fan of that.
[1388.38 --> 1394.68]  On my walks, I often sit and I'll talk to chat GPT and we'll talk through papers and what are the main technical points and stuff.
[1394.96 --> 1395.30]  So, yeah.
[1395.30 --> 1397.44]  Yeah, I'm glad I'm not the only one.
[1397.66 --> 1400.30]  So thanks for validating that.
[1400.80 --> 1406.32]  I guess getting back like more into the development retrieval kind of reasoning stuff.
[1406.46 --> 1409.78]  What are some of that now that we've been working with this technology for a while?
[1409.86 --> 1410.78]  We've got more cycles.
[1410.78 --> 1416.24]  Like someone can spin up a rag pipeline in, you know, whatever, 10 minutes.
[1416.34 --> 1418.90]  I can spin it up and I have something going.
[1419.06 --> 1425.10]  But it's another thing to kind of, of course, scale that, maintain it over time, deal with some of the issues.
[1425.10 --> 1438.60]  You know, what I guess my question is, what pitfalls are people falling into that maybe we didn't know about whatever it was a year ago when we were kind of just getting into these initial kind of naive rag sorts of things?
[1438.88 --> 1444.70]  What challenges or consistent challenges and pitfalls do you see people kind of falling into?
[1444.70 --> 1451.56]  Yeah, I think the consistent thing I see with something like rag is it's fairly easy to build a quick demo.
[1451.82 --> 1455.62]  You can grab an off the shelf embedding model to do that.
[1455.72 --> 1462.52]  You can combine that with a generation model like an open AI model and you can build yourself a quick kind of proof of concepts.
[1462.94 --> 1466.50]  I think the trouble that people get into with it is scaling it up.
[1466.50 --> 1473.52]  It's great on 100 documents, but now all of a sudden I have to go to 100,000 or a million documents.
[1473.64 --> 1475.18]  How am I going to do that?
[1475.72 --> 1482.54]  Or, you know, when I first did my demo, I did a couple of very simple queries, text extraction queries.
[1482.54 --> 1489.36]  But now when I put it out in front of my users, I find out all of a sudden they're not giving nice one sentence queries.
[1489.62 --> 1491.20]  They're just asking two words.
[1491.80 --> 1497.42]  And then I need to add a query reformulation step or something to do that.
[1497.54 --> 1501.50]  Or the accuracy is not kind of what I was looking for.
[1502.10 --> 1503.70]  And so I've added a bunch of pieces in there.
[1503.78 --> 1504.68]  I've added a re-ranker.
[1504.74 --> 1505.62]  I've added other steps.
[1506.28 --> 1508.60]  But now my latency is suffering, right?
[1508.60 --> 1511.72]  There's all these kind of trade-offs as you kind of get to production.
[1511.92 --> 1513.98]  And then you're like, oh, you know, do I go back?
[1514.06 --> 1517.74]  And you go and you look online and you see that, oh, wait a minute.
[1517.82 --> 1518.92]  There's like 15.
[1519.12 --> 1522.28]  I think there's like 25, 30 flavors of rag.
[1522.34 --> 1525.24]  And you're like, oh, did I set up my infrastructure wrong?
[1525.32 --> 1527.76]  Or, oh, do I go back and I change my chunking strategies?
[1527.88 --> 1531.16]  I can see, you know, there's 10 different chunking strategies people are doing that.
[1531.74 --> 1535.02]  And so I think this is the cycle of where it's very easy to get started.
[1535.02 --> 1540.72]  But getting to that final kind of production quality rag can kind of be a little worrisome.
[1540.80 --> 1540.90]  Yeah.
[1540.98 --> 1547.96]  And do you think that that's where the real human engineering piece of this development
[1547.96 --> 1551.06]  still like will be with us for some time?
[1551.16 --> 1556.22]  Because, you know, to some degree, like you can describe, let's say I describe that sort
[1556.22 --> 1559.04]  of problem to my AI coding assistant.
[1559.26 --> 1563.72]  Is it reasonable for me to think that like that kind of debugging and process could help
[1563.72 --> 1569.26]  me or that kind of assistant type of thing could help me get to the bottom of this or
[1569.26 --> 1572.88]  update my, you know, retrieval pipeline and that sort of thing?
[1573.26 --> 1578.52]  So I'm kind of optimistic that the reasoning models that we have now are going to get us
[1578.52 --> 1581.30]  much farther towards helping you solve that problem.
[1581.80 --> 1585.26]  Now, of course, that reasoning model has got to understand like how you're thinking about
[1585.26 --> 1586.46]  how to solve that problem.
[1586.46 --> 1592.26]  But already today, if you take the traditional rag approach, for example, but you pair it
[1592.26 --> 1597.10]  with one of the reasoning models that can make tool calls, that can kind of look at the
[1597.10 --> 1601.78]  results that come back, think about it, decide, hey, I want to requery it in a different way.
[1602.46 --> 1607.76]  You can improve the quality of your results in that way by kind of using that reasoning to
[1607.76 --> 1608.10]  do that.
[1608.10 --> 1612.74]  So I'm pretty optimistic that we're going to keep finding new ways, as long as there are
[1612.74 --> 1617.02]  workflows that we can train these models on that are kind of fairly, fairly, let's say,
[1617.08 --> 1617.34]  logical.
[1617.70 --> 1618.02]  Archetypal.
[1618.42 --> 1619.46]  Yeah, exactly.
[1619.68 --> 1619.88]  Gotcha.
[1620.12 --> 1625.32]  Like a way we can kind of connect the dots and teach the models to do that, that I think
[1625.32 --> 1630.86]  a lot of these things that if we have the, if we give it the budget for spending time
[1630.86 --> 1635.76]  thinking, doing those tokens there, it's going to cost us more latency, but we're going to
[1635.76 --> 1636.54]  see better results.
[1636.54 --> 1640.10]  And I think some of us, we already see that in using some of these tools like deep research,
[1640.10 --> 1644.56]  where we can see that by spending more time on the task, it's able to give us a better
[1644.56 --> 1644.94]  result.
[1645.40 --> 1645.52]  Yeah.
[1646.18 --> 1646.40]  Yeah.
[1646.50 --> 1653.40]  And, you know, one area that we haven't talked about yet is this sort of world of agents,
[1653.40 --> 1658.84]  which I know is a loaded term, and it's probably related to what you were just talking about
[1658.84 --> 1664.80]  in terms of time of compute and steps in the process and the reasoning models and all of
[1664.80 --> 1666.24]  those sorts of things.
[1666.54 --> 1672.96]  Could you help us parse apart, you know, from your perspective, it almost seems to me like
[1672.96 --> 1677.08]  it's one of those, I don't know if you're, oh, I'm sure you remember, you know, when
[1677.08 --> 1682.46]  it seemed like every conversation I got on, like the first part of the presentation was,
[1682.98 --> 1688.86]  what is the difference between data science and AI and machine learning, or the difference
[1688.86 --> 1691.42]  between machine learning and AI or whatever.
[1691.42 --> 1695.74]  And at a certain point, I was like, well, these terms all mean nothing, essentially,
[1695.96 --> 1698.58]  because people use them so interchangeably.
[1698.66 --> 1703.92]  I feel like that's sort of where we're getting with agents and assistants and all of these
[1703.92 --> 1704.96]  sorts of terms.
[1705.10 --> 1710.64]  But from your perspective, I guess, if that word agent kind of has a meaningful difference
[1710.64 --> 1713.50]  to you, what kind of stands out in your mind there?
[1713.50 --> 1713.90]  Yeah.
[1714.06 --> 1716.94]  And I think like we all like the idea of this agent, right?
[1716.98 --> 1721.88]  Like something I can give a problem to and it solves the problem.
[1722.20 --> 1726.86]  And now I think there's where the definitions break down to is how much autonomy is this agent,
[1726.94 --> 1730.46]  how structured is what we do like that.
[1730.76 --> 1734.32]  But if we just think back about the bigger picture of like, I have a problem.
[1734.44 --> 1737.28]  It's not a straightforward problem that I want to give to an agent.
[1737.28 --> 1740.92]  Now, there's at least two different ways that we can kind of tackle this.
[1741.00 --> 1744.56]  One is I can give them a step-by-step list of instructions.
[1745.36 --> 1748.82]  And this is what we call a workflow often, like do this, do this, do this.
[1748.94 --> 1752.64]  And then I can check their work at every step and make sure that they're on the track to
[1752.64 --> 1753.10]  solve it.
[1753.74 --> 1757.98]  Or I can just be like, this is the difference maybe between my kind of five-year-old and
[1757.98 --> 1758.74]  a 13-year-old.
[1758.80 --> 1762.50]  My 13-year-old, like I'll give them the list and I'll cross my fingers and hope that they'll
[1762.50 --> 1763.02]  finish it.
[1763.12 --> 1765.34]  And, you know, usually they do, but not always.
[1765.34 --> 1768.62]  But I'm not involved in every step of the way.
[1768.98 --> 1772.32]  And I think one of the things is we're watching the agents evolve.
[1772.42 --> 1776.78]  And this is one of the big trade-offs that developers have today is how much structure,
[1776.92 --> 1780.00]  how much babysitting am I doing for this agent?
[1780.12 --> 1782.52]  How do I do versus kind of the hands-off?
[1783.40 --> 1788.10]  Now, I think the trend is we're going to be able to do much more hands-off.
[1788.42 --> 1792.62]  Just like we've seen these models be able to gain the reasoning ability over the last
[1792.62 --> 1798.68]  two years or so, I have no doubt that we're going to be able to train them to do more complex
[1798.68 --> 1801.08]  tasks, to be able to follow those steps.
[1801.22 --> 1805.42]  It's just a matter of kind of giving them the training data, having the experience to
[1805.42 --> 1805.84]  do that.
[1805.94 --> 1812.04]  So my bet is in the long term for many of these tasks, we'll be able to be much more hands-off
[1812.04 --> 1816.44]  and the models themselves will strive to be able to solve them themselves.
[1816.44 --> 1822.96]  I just thought it would be good to get your input on a theory I've been having, which
[1822.96 --> 1824.24]  is maybe related.
[1824.78 --> 1831.34]  I mean, maybe it's an offshoot from what we're talking about, which is really maybe the ability
[1831.34 --> 1838.46]  to use these Vibe coding tools or others to, or assistants or agents to update retrieval
[1838.46 --> 1842.82]  processes or kind of architect our AI pipelines, if you will.
[1842.82 --> 1848.22]  Well, I've had this sort of thought and I'm curious about your opinion because you also
[1848.22 --> 1855.18]  have a background kind of pre-generative AI in the data science world that like previously
[1855.18 --> 1860.50]  I kind of had in my mind this mental model of on the one side, you have kind of engineering,
[1860.84 --> 1863.56]  traditional software engineering, DevOps infrastructure.
[1864.40 --> 1870.54]  On the other side, you have business and the product and marketing, all of those things.
[1870.54 --> 1875.44]  And in the middle is kind of data scientists because, you know, you translate the business
[1875.44 --> 1880.28]  problems and understand how to connect it to the data and the tech and produce your predictive
[1880.28 --> 1880.76]  model.
[1880.94 --> 1884.48]  And like, you're kind of living between those two worlds.
[1884.48 --> 1889.82]  And it's almost like I see that middle zone shrinking and shrinking and shrinking because
[1889.82 --> 1898.66]  those domain experts on the business side are actually able to use very sophisticated tools
[1898.66 --> 1904.74]  now to kind of self-serve themselves a lot of the kind of maybe stuff that would normally
[1904.74 --> 1907.26]  fit on the plate of a data scientist.
[1907.54 --> 1914.18]  So part of me is wondering, like me as a, me personally, like Daniel Whitenack as a data scientist,
[1914.18 --> 1919.82]  like what is the future of that data science world when this kind of middle is shrinking?
[1919.96 --> 1924.84]  I'm curious if you also see it that way or see it slightly differently and what your thoughts
[1924.84 --> 1926.50]  are in terms of that view.
[1926.62 --> 1926.82]  Yeah.
[1927.26 --> 1930.12]  So I don't think the data science world is changing at all.
[1930.38 --> 1935.38]  First of all, I'm excited that the bar is kind of dropping in terms of people being able
[1935.38 --> 1937.04]  to use code to build solutions.
[1937.04 --> 1943.38]  Like my nine-year-old can literally like vie code of a game that he can play as well as
[1943.38 --> 1947.12]  my 23-year-old who has a degree in computer science.
[1947.12 --> 1950.78]  And you couldn't tell the difference between like the games that they built like that.
[1951.20 --> 1956.66]  So there's a great ability in just allowing everybody to be able to kind of more participate
[1956.66 --> 1960.62]  and work kind of with code that we're being able to see now.
[1961.08 --> 1964.44]  Now, how does that change something like data science, right?
[1964.44 --> 1967.24]  Like data science, the original triangle was right.
[1967.38 --> 1968.26]  Part of it was coding.
[1969.02 --> 1973.60]  I think data scientists were never thought of as really great coders, which is why, right?
[1973.70 --> 1975.22]  They were kind of put in there.
[1975.82 --> 1978.92]  80% of those projects didn't make it past pilot too.
[1979.06 --> 1979.78]  Exactly, right?
[1979.82 --> 1981.80]  Like they would not write production code.
[1981.98 --> 1985.94]  And right, there was MLE engineers kind of became the offshoot to kind of do the production
[1985.94 --> 1987.42]  piece like that.
[1987.90 --> 1994.26]  Now, for me, it's a similar thing to like, if you think of like journalists in media, right?
[1994.26 --> 1996.48]  Like everybody says, oh, right, everything's going online.
[1996.52 --> 1997.72]  We're not going to have any journalists.
[1997.90 --> 2002.72]  Well, if you think at the end of the day, a journalist is a storyteller telling you about
[2002.72 --> 2004.46]  kind of the facts of what's going on.
[2004.88 --> 2011.50]  For me, the data science is a similar piece where it's still kind of a mission, a work that
[2011.50 --> 2015.90]  we're doing in terms of we're helping a business solve problems by looking at their data.
[2016.76 --> 2022.08]  The tools have changed, but the same problems still exist.
[2022.08 --> 2028.32]  And I think this is the most important thing is you still need a flexible mind as a data
[2028.32 --> 2033.28]  scientist to be able to look at data, to be able to talk to a stakeholder, to be able
[2033.28 --> 2035.26]  to go out and figure out what is the coding?
[2035.72 --> 2041.04]  What is the math, the algorithms to bring to solve that problem where you need a lot of
[2041.04 --> 2042.74]  this kind of left brain, right brain stuff.
[2042.82 --> 2044.72]  And so it's still a fairly unique role.
[2044.72 --> 2052.82]  And you can see this where you start talking to like AI engineers, where you have developers
[2052.82 --> 2056.48]  that are trying to kind of bridge this and solve the business problems.
[2056.82 --> 2060.80]  And we see one of the biggest problems they have is with evaluations.
[2061.26 --> 2065.78]  And for data scientists, they're trained on how to do evaluations coming up.
[2065.84 --> 2067.62]  Like you look at the data, you talk to people.
[2067.62 --> 2071.82]  Like error analysis is something that's built into kind of data scientists.
[2071.96 --> 2076.64]  But I always look over and see like how we have to kind of teach software developers that
[2076.64 --> 2081.04]  skill if they really want to be able to kind of do the same kind of work like that.
[2081.32 --> 2082.46]  Yeah, that's super interesting.
[2082.74 --> 2089.40]  I kind of pose the question in maybe a little bit of a controversial way.
[2089.62 --> 2093.48]  I think I would echo what you're saying.
[2093.48 --> 2100.18]  I mean, there's elements of this in certain cases, like, you know, in certain industries
[2100.18 --> 2108.12]  where like, hey, if you're using computer vision to analyze parts coming off of, you know,
[2108.22 --> 2114.14]  medicine coming off of a pharma manufacturing line and needing to do that, you know, 10,000
[2114.14 --> 2120.06]  times a minute, like this is not a problem that is like, hey, just prompt an LLM.
[2120.06 --> 2127.66]  Like on one side, there's very hard kind of modeling problems that need to be solved there.
[2127.80 --> 2133.34]  I think on the other side to what you're saying, I also see this kind of gap around AI engineering
[2133.34 --> 2136.50]  where it's, okay, we can architect the pipeline.
[2136.86 --> 2141.70]  And where I see a lot of people spinning their wheels is saying, well, it seems like this is
[2141.70 --> 2142.12]  working.
[2142.52 --> 2143.68]  That's kind of where they end.
[2143.68 --> 2150.74]  And like, well, we could also measure if it's working and like construct a test set and,
[2150.88 --> 2152.62]  you know, maybe automate that.
[2152.76 --> 2156.64]  And as we update our pipeline, we could test the retrieval and those sorts of things.
[2156.64 --> 2161.88]  So love, love that perspective around the evaluation, especially.
[2162.28 --> 2169.06]  I guess you see that side being stressed more and more as like in maybe software engineers
[2169.06 --> 2174.34]  see that the future is AI related and really want to push into that.
[2174.34 --> 2182.46]  So I see that there is kind of a growing emphasis for developers and engineers to understand evaluations
[2182.46 --> 2183.36]  and do that.
[2184.26 --> 2188.80]  My thing is that it's always going to be a little bit of a tension for those folks because
[2188.80 --> 2194.36]  often the folks that are really good at software development have a very black and white way
[2194.36 --> 2199.76]  of looking at the world, that they focus on optimization, that there is a best solution,
[2200.18 --> 2204.68]  which necessarily isn't the same type of mindset that you need.
[2204.76 --> 2207.10]  And of course, this is, you know, a graduated spectrum.
[2207.24 --> 2208.10]  Everybody's a little different.
[2208.14 --> 2208.48]  Yeah, yeah.
[2208.56 --> 2208.90]  Fills that.
[2209.26 --> 2213.54]  So this is where I think there's always going to be that gap between just having kind of
[2213.54 --> 2215.90]  software developers fully step into it.
[2216.14 --> 2221.18]  But I want to take up one other thing that you say is a lot of times like the hype we see
[2221.18 --> 2228.24]  around generative AI and NVIDIA and stuff kind of draws out and makes kind of the problems
[2228.24 --> 2233.00]  that we can solve with generative AI kind of much bigger than I think the actual usefulness
[2233.00 --> 2233.34]  of them.
[2234.06 --> 2239.38]  So and what I mean is that there's a lot of problems inside an enterprise that can be solved
[2239.38 --> 2240.82]  without large language models.
[2241.34 --> 2245.54]  And my worry is, is the folks inside them that have been doing data science for 10 years
[2245.54 --> 2245.92]  know that.
[2246.00 --> 2250.54]  They know that I could use operations or optimization to solve this problem.
[2250.54 --> 2253.14]  Or this is a time series problem to do that.
[2253.62 --> 2260.16]  My biggest fear is the people coming into kind of AI and data science nowadays aren't seeing
[2260.16 --> 2264.42]  those types of problems and understanding that there's a whole set of tools to be able
[2264.42 --> 2267.60]  to solve those problems where often kind of everything comes.
[2268.02 --> 2271.90]  We're using generative AI as the hammer for solving every type of problem like that.
[2272.30 --> 2274.72]  Yeah, maybe this exists out there.
[2274.92 --> 2277.34]  And so, you know, I'm already building something.
[2277.34 --> 2280.42]  So someone can totally steal my idea if they want.
[2280.48 --> 2288.42]  But I wonder if there exists out there, you know, this kind of idea of some sort of assistant
[2288.42 --> 2295.24]  that would live at the orchestration level above these kind of traditional data science
[2295.24 --> 2297.94]  tools and help you like towards that analysis.
[2297.94 --> 2305.24]  So just by way of example, like I'm assuming you could put sort of Facebook's profit for
[2305.24 --> 2310.88]  time series forecasting behind an MCP server and be able to have that discovered by this
[2310.88 --> 2313.60]  kind of orchestration level and maybe guide people to that.
[2313.70 --> 2318.40]  Now, that might not be the interface that you want to have for your time series modeling
[2318.40 --> 2319.94]  like in production.
[2319.94 --> 2327.90]  But it could potentially kind of guide folks to some of these kind of traditional data science
[2327.90 --> 2333.80]  tools and kind of help teach them maybe what they need to put in place that's not on the
[2333.80 --> 2338.24]  large language model side and actually have the large language model tell you that,
[2338.62 --> 2343.60]  hey, I'm not the best for this and you should use Facebook profit or whatever.
[2344.12 --> 2347.08]  Yeah, I'm hoping that we'll be able to get to that.
[2347.08 --> 2351.32]  Like I think there's some elements of why these models are great for kind of brainstorming,
[2351.38 --> 2354.18]  thinking through things, solutions through too.
[2354.50 --> 2361.12]  But if the space is too large of possibilities of different ways to slice the problem, different
[2361.12 --> 2366.28]  ways to think about how you could set the predictions or what data to use, then even an
[2366.28 --> 2370.42]  LM, you're not going to be able to feed it all the relevant information to be able to actually
[2370.42 --> 2371.52]  kind of make that decision.
[2371.64 --> 2376.40]  And this is where as humans, we have to kind of often be the piece that takes in a lot of
[2376.40 --> 2380.30]  that disparate information and figure out like, okay, this is what the business really
[2380.30 --> 2380.98]  focuses on.
[2381.24 --> 2382.76]  Let's zoom it down to this piece.
[2382.76 --> 2386.62]  And now I'm going to use my LM to help me think about, hey, there's three different tools
[2386.62 --> 2387.58]  here and strategies.
[2388.00 --> 2388.86]  Like tell me the trade-offs.
[2389.20 --> 2392.52]  Let's figure out which, I was doing this earlier today, like which package should I spend my
[2392.52 --> 2395.00]  time learning how to use to solve this problem?
[2395.14 --> 2395.30]  Yeah.
[2395.48 --> 2395.64]  Yeah.
[2395.66 --> 2396.90]  That makes sense.
[2397.50 --> 2403.28]  Well, Rajiv, I'm sure we'll have many other great conversations at the Midwest AI Summit and
[2403.28 --> 2407.68]  at upcoming or future podcast episodes.
[2408.18 --> 2415.66]  But as we kind of get closer to the end here and you look out towards the future, what is it
[2415.66 --> 2420.92]  that kind of excites you about the next steps of our journey in this space?
[2421.74 --> 2421.86]  Yeah.
[2421.98 --> 2426.76]  No, I mean, it's just been a great time of innovation inside of data science, which is
[2426.76 --> 2427.54]  why I love it.
[2427.54 --> 2433.48]  I mean, everything from kind of going from XGBoost to CNNs to kind of where we are now.
[2434.02 --> 2438.74]  And so I'm looking forward to like more innovation, especially in kind of the area of large language
[2438.74 --> 2439.06]  models.
[2439.38 --> 2443.20]  But I also want to remind people, like we were talking about, there's a great wake of tools
[2443.20 --> 2447.98]  that are out there that I still like to kind of point people to that there's, it might not
[2447.98 --> 2451.30]  get the most attention, but there's a lot of times a more efficient way of solving your
[2451.30 --> 2451.98]  problem as well.
[2451.98 --> 2452.62]  Yeah.
[2452.86 --> 2459.32]  And where would you like from, obviously you produce a lot of content and that sort of
[2459.32 --> 2466.92]  thing, but as just a person that's more intimately familiar with that kind of ecosystem, if folks
[2466.92 --> 2473.46]  are like, hey, you know, I heard, for example, I'm at a Raleigh Innovation Conference here in
[2473.46 --> 2475.78]  Indianapolis today, off in a corner.
[2475.78 --> 2480.50]  And I heard Kevin O'Leary, you know, from Shark Tank this morning, he was saying, you
[2480.50 --> 2487.64]  know, every day you should spend 30% of your mental capacity trying something new, like
[2487.64 --> 2488.92]  keep those juices flowing.
[2489.06 --> 2493.78]  So maybe it's our listeners today, they're, they're taking away, hey, I should try one of
[2493.78 --> 2495.90]  these non-gen AI things.
[2495.90 --> 2499.12]  And like, where would, where would I even go to, to start that?
[2499.18 --> 2500.06]  Any, any suggestions?
[2500.46 --> 2505.36]  Yeah, no, I, I love that idea of like, it's spending a 30 minutes or an hour a day, like
[2505.36 --> 2508.58]  continual learning is, is the, is the future like that.
[2508.80 --> 2513.64]  So I have my own content that I put out at Registics that tries to kind of inspire you
[2513.64 --> 2518.42]  to push you in different ways that kind of AI is doing, give, give people simple kind
[2518.42 --> 2519.52]  of nuggets like that.
[2519.64 --> 2522.14]  So I would, of course, kind of point to myself as well.
[2522.40 --> 2525.36]  I think the other area that I really like are newsletters.
[2525.36 --> 2530.78]  I think newsletters are a nice way to be able to take in all the information that's coming
[2530.78 --> 2536.84]  in, but in a little bit of a slower kind of meditative way, rather than just kind of reacting
[2536.84 --> 2538.66]  to the latest trending post.
[2539.06 --> 2540.26]  Yeah, that's, that's awesome.
[2540.48 --> 2547.26]  And, uh, um, I'm sure we'll include a few links, um, in our, in our show notes to things
[2547.26 --> 2549.02]  that will be useful for people.
[2549.26 --> 2553.76]  Um, but really appreciate you joining us again, uh, Rajiv, looking forward to seeing you in
[2553.76 --> 2557.80]  person and, uh, and yeah, keep up the, keep up the great work.
[2557.80 --> 2562.14]  It's, it's always, it's always good to get to hear your perspective and looking forward
[2562.14 --> 2563.32]  to having you on the show again.
[2563.72 --> 2564.40]  Thanks so much.
[2564.44 --> 2567.22]  I think this is one of the longest running data science podcasts out there.
[2567.22 --> 2568.92]  So it's been great to be part of it.
[2568.98 --> 2569.56]  Thanks so much.
[2569.86 --> 2570.18]  Thanks.
[2577.36 --> 2577.98]  All right.
[2578.20 --> 2579.56]  That's our show for this week.
[2579.56 --> 2584.94]  If you haven't checked out our website, head to practicalai.fm and be sure to connect with
[2584.94 --> 2586.90]  us on LinkedIn X or blue sky.
[2586.90 --> 2591.46]  You'll see us posting insights related to the latest AI developments, and we would love
[2591.46 --> 2592.82]  for you to join the conversation.
[2593.10 --> 2597.10]  Thanks to our partner prediction guard for providing operational support for the show.
[2597.44 --> 2599.42]  Check them out at prediction guard.com.
[2599.78 --> 2603.48]  Also thanks to break master cylinder for the beats and to you for listening.
[2603.72 --> 2606.66]  That's all for now, but you'll hear from us again next week.
[2606.66 --> 2609.00]  We'll see each other time.
[2611.52 --> 2611.60]  Bye.
[2611.60 --> 2611.74]  Bye.
[2611.96 --> 2612.14]  Bye.
[2612.22 --> 2612.38]  Bye.
[2612.78 --> 2613.14]  Bye.
[2613.22 --> 2613.34]  Bye.
[2613.34 --> 2614.18]  Bye.
[2614.18 --> 2614.74]  Bye.
[2615.16 --> 2615.28]  Bye.
[2615.46 --> 2615.60]  Bye.
[2615.72 --> 2615.78]  Bye.
[2615.86 --> 2616.28]  Bye.
[2616.28 --> 2616.54]  Bye.
[2616.58 --> 2616.62]  Bye.
[2616.78 --> 2617.18]  Bye.
[2617.26 --> 2617.32]  Bye.
[2617.44 --> 2617.72]  Bye.
[2617.82 --> 2619.32]  Bye.
[2619.34 --> 2619.88]  Bye.
[2619.94 --> 2620.28]  Bye.
[2620.28 --> 2620.78]  Bye.
[2620.78 --> 2621.10]  Bye.
[2621.26 --> 2621.28]  Bye.
[2621.28 --> 2621.78]  Bye.
[2621.78 --> 2622.38]  Bye.
[2622.54 --> 2623.42]  Bye.
[2623.42 --> 2623.56]  Bye.
[2623.56 --> 2624.38]  Bye.
[2624.38 --> 2624.42]  Bye.
[2624.58 --> 2624.94]  Bye.
[2624.94 --> 2625.14]  Bye.
[2625.14 --> 2626.74]  Bye.
[2626.86 --> 2627.10]  Bye.
[2627.16 --> 2627.44]  Bye.
[2627.44 --> 2627.54]  Bye.
[2627.56 --> 2627.86]  Bye.
[2627.92 --> 2628.22]  Bye.
[2628.22 --> 2628.84]  Bye.
[2628.88 --> 2628.94]  Bye.
[2629.06 --> 2629.60]  Bye.
[2629.72 --> 2630.48]  Bye.
[2630.52 --> 2630.72]  Bye.
[2630.82 --> 2631.86]  Bye.
[2631.96 --> 2632.30]  Bye.
[2632.40 --> 2632.50]  Bye.
[2632.50 --> 2632.84]  Bye.
[2633.00 --> 2633.10]  Bye.
[2633.20 --> 2633.66]  Bye.
[2633.66 --> 2634.32]  Bye.
[2634.48 --> 2634.88]  Bye.
[2634.92 --> 2635.54]  Bye.
