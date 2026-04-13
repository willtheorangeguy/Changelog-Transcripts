[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.02 → 36.08] Learn more at fly.io.
[43.04 → 46.28] Welcome to another episode of Practical AI.
[46.60 → 48.04] This is Daniel Whiten ack.
[48.14 → 51.30] I'm a data scientist building a tool called Prediction Guard.
[51.30 → 56.28] And I'm joined as always by my co-host, Chris Benson, who's a tech strategist at Lockheed
[56.28 → 56.54] Martin.
[56.76 → 57.46] How are you doing, Chris?
[57.60 → 58.64] Doing very well.
[58.80 → 62.66] We're still in 2023, the most exciting year in AI history.
[62.88 → 64.88] It is, you know.
[65.30 → 72.46] It's hard to keep up, but it's also sometimes hard to understand, like, what of these cool
[72.46 → 77.80] demos and models and integrations are, like, actually production ready?
[77.80 → 81.88] And how are people actually taking these things into production?
[81.88 → 87.76] And we're really happy to have with us today Travis Fisher, who is a founder and CEO at
[87.76 → 93.50] a stealth AI startup and is focused 100% on that, delivering products with AI.
[93.72 → 95.06] So we're happy to have you here.
[95.30 → 96.10] Welcome, Travis.
[96.58 → 97.06] Thank you, guys.
[97.12 → 98.08] It's a pleasure to be here.
[98.14 → 99.48] Looking forward to the conversation.
[99.48 → 100.48] Yeah.
[100.48 → 100.58] Yeah.
[100.88 → 106.26] Well, on Twitter, you posted this diagram, which I think maybe you have penned right now,
[106.38 → 110.56] which is how to use large language models effectively.
[110.56 → 114.68] And it's sort of like a start simple to complex scale.
[114.68 → 116.96] And I found that really great.
[117.12 → 121.54] And I've actually shared that diagram with a number of people and various Slack channels
[121.54 → 121.82] and all.
[121.92 → 122.12] Awesome.
[122.36 → 123.56] This is how you should be thinking.
[123.96 → 128.72] How did you, maybe not specifically with that figure, which we can talk about, but like,
[128.80 → 134.56] how did you get into thinking about how to use large language models effectively to,
[134.80 → 137.56] like, actually how to build products with these models?
[138.14 → 138.34] Yeah.
[138.54 → 139.64] It's a great, great question.
[139.64 → 144.02] So I'll give you kind of my quick, what I've been up to in the last six months, which is
[144.02 → 145.08] going to answer some of this stuff.
[145.42 → 147.04] I'm a huge fan of open source.
[147.50 → 154.28] When ChatGPT launched on November 30th, 48 hours later, I released the ChatGPT NPM package,
[154.50 → 156.22] which was using unofficial API.
[156.54 → 160.80] And it just allowed like thousands of developers to go and start building with this cool new
[160.80 → 165.86] thing that, you know, like the GPT series and LLs have been along for a while before that,
[165.86 → 169.78] but it was kind of this step function in terms of just their mainstream adoption and really
[169.78 → 170.92] just caught people's attention.
[171.58 → 176.78] You know, after that, I released the ChatGPT Twitter bot, which now has about 123,000 followers.
[177.56 → 185.60] I run a group called ChatGPT Hackers.dev that has about 9,500 AI developers, just a whole spectrum
[185.60 → 186.14] of people, right?
[186.14 → 189.70] We have like researchers in there, and then we have like prompt engineering script kitties.
[190.08 → 195.12] And because, I mean, my background is computer science and I do have some formal education in
[195.12 → 198.44] machine learning, but it's not like I'm an AI expert, like my any means, right?
[198.94 → 204.42] And what has really captured me really over the past year or so has just been the rate
[204.42 → 207.22] of progress and trying to wrap my head around it and understand it.
[207.72 → 211.68] And because it's been moving so quickly, I've been optimizing for my rate of learning.
[211.92 → 216.00] And I personally learn best by building out in public and building open source and just
[216.00 → 217.08] sharing what I learn as I go.
[217.08 → 223.32] So, you know, I think there's a lot of like complexity and terms in AI, as you guys know,
[223.32 → 226.48] and to some degree, even just having a mental model of like, what are the different approaches
[226.48 → 230.82] that you could start with or how to approach solving a problem is already like a difficult
[230.82 → 231.78] starting place, right?
[232.34 → 240.46] And I know for the how to use LLMs effectively, my inspiration there was Andre Karate recently,
[240.98 → 245.18] maybe a month or two ago, tweeted something about, you know, all these big companies are
[245.18 → 246.36] interested in using AI.
[246.62 → 248.98] They're aware that they should be using it to some extent.
[248.98 → 253.10] And so they're like, well, we need to hire a team of ML engineers and get on this, right?
[253.44 → 258.32] And the huge unlock now is with these foundational models, like for most problems, you don't need
[258.32 → 258.86] to do that.
[259.28 → 262.30] And, you know, yeah, there's the production side, the practical side, and I'm sure we'll
[262.30 → 262.84] get into that.
[262.94 → 268.00] But like in terms of where to start and starting simple and actually validating for your business
[268.00 → 273.20] use case that you can actually solve it with AI, that you understand the problem domain
[273.20 → 277.32] enough that you have, whether it's a training data or that you're actually solving a real
[277.32 → 282.40] customer a problem, like starting as simple as possible with hosted foundational models,
[282.50 → 287.04] a lot of times is a great way to get started and just to validate quickly.
[287.60 → 292.92] You know, as you kind of inevitably find points where your workflow breaks down or where you're
[292.92 → 297.78] not getting a quality or the cost or some hard constraints like security, privacy, you know,
[297.80 → 301.18] of your data, there's kind of this ladder of complexity I like to look at.
[301.28 → 303.52] And, you know, you start with just prompt engineering up at the top.
[303.52 → 308.92] And then it's about like, well, how much can I reduce hallucinations or add domain specific
[308.92 → 312.82] context into my prompt by, you know, doing information retrieval?
[313.16 → 316.72] And then, you know, at some point you're like, well, a single prompt isn't doing it.
[316.76 → 321.68] So maybe I add some iterative process to that where I use another language model to, there's
[321.68 → 324.22] all these techniques for doing kind of multistep prompting.
[324.22 → 329.90] But you can do all of that with a hosted model, and you can get like 95% of the way there for
[329.90 → 334.20] a lot of problems and domains these days in a way that was previously like locked behind,
[334.20 → 336.58] you know, proprietary data providers.
[336.58 → 338.74] And you had to have so many resources to be able to do that.
[338.78 → 345.12] So it's really this like democratizing point in the industry at the applied AI level that
[345.12 → 345.76] we're at right now.
[345.76 → 350.48] And I think from the conversations I've been having with folks who are a lot of them, you
[350.48 → 354.30] know, like, like full stack TypeScript devs for building applications, right.
[354.32 → 355.14] And they want to use AI.
[355.24 → 355.86] They know it's cool.
[356.22 → 358.62] They don't know how to get started, or they're like, oh, I need to learn Python.
[358.72 → 360.30] I need to train these custom models and stuff.
[360.32 → 365.96] And, and like, all of that is super important, and it comes into play at a time or for particular
[365.96 → 366.72] types of problems.
[366.72 → 372.70] But the majority of people for getting started, like start simple is the main takeaway from that.
[372.70 → 374.54] I think that's a great insight.
[374.64 → 380.60] And I think that's a one of the places where so many people go wrong is jumping into too
[380.60 → 381.32] much complexity.
[381.68 → 387.14] They don't find a simple need and potentially even don't look for things that work just
[387.14 → 389.36] as fine that are not AI in that way.
[389.40 → 393.24] So I love, I love the go simple and build from their philosophy.
[393.40 → 394.72] I think that's incredibly practical.
[395.08 → 402.16] I get the sense that a lot of this sort of like chaining and like bringing models together,
[402.16 → 404.04] doing the information retrieval.
[404.28 → 409.86] It's sort of like almost like a hacking culture around this language model prompting, which
[409.86 → 410.68] is really cool.
[410.68 → 413.42] And like that can go so, so far.
[413.92 → 419.24] Maybe there's like you say, there's like privacy or domain specific concerns with like
[419.24 → 420.50] enterprise use cases.
[420.50 → 425.44] But in your, like you mentioned the community that you've kind of built-up, and you're part
[425.44 → 426.66] of on discord.
[426.66 → 433.76] What are some of the things that have maybe like surprised you that you've seen that, Hey,
[433.86 → 440.04] I didn't even think that maybe this was possible with just this layer of like using a hosted
[440.04 → 444.26] model, using pre-training, using retrieval, whatever it is.
[444.26 → 450.94] What are some of those things that you've seen that kind of surprise you or maybe like help
[450.94 → 453.08] develop your thinking around this topic?
[453.08 → 456.14] I have a few examples in one story.
[456.68 → 462.74] Examples would be folks who are taking these models and like applying it to their personal
[462.74 → 463.24] finances.
[463.52 → 464.12] Right.
[464.20 → 467.46] And there's one guy in our discord who's like an ex hedge fund guy.
[467.46 → 471.60] And he created a very basic agent that uses a large language.
[471.60 → 477.36] I think it's probably using GPT-4 to take this unstructured information from his bank's
[477.36 → 481.44] website about his expenses and like, you know, extract structured information about that.
[481.52 → 482.86] And then, you know, he can graph it and whatever.
[483.08 → 486.32] So I think there's a lot of hacking going on around this stuff.
[486.40 → 487.36] It is very, very early.
[487.80 → 491.22] Another story of something that surprised me, and this is just a fun story.
[491.34 → 496.08] But when I released the kind of unofficial API wrapper for ChatGPT, we kind of had this
[496.08 → 498.86] cat and mouse game going back and forth with open AI for a while.
[498.86 → 502.64] Because apparently there was kind of a group within open AI that was like, oh, this is
[502.64 → 502.98] amazing.
[503.06 → 504.82] Look at the open source community is doing.
[504.92 → 505.90] They're building all this cool stuff.
[506.10 → 508.50] And then there was another group that was like, well, we're going to have the official
[508.50 → 508.80] API.
[508.92 → 510.36] Eventually we want to control this stuff.
[510.42 → 510.60] Right.
[510.96 → 512.92] So there was kind of this back and forth.
[512.98 → 513.20] Right.
[513.20 → 520.52] And at one point our community found a public model, but it wasn't like publicly disclosed.
[520.62 → 525.08] It was security through obscurity, but it was a fine-tuned chat model that ChatGPT was actually
[525.08 → 525.86] using at one point.
[526.44 → 529.64] And all the open source projects started to use this thing.
[529.64 → 534.20] And there were tens of thousands of actual real consumers at the end, you know, who were
[534.20 → 535.04] building on top of this.
[535.48 → 537.42] And of course, opening, I knew that we were doing this.
[537.50 → 539.98] I talked with one of our security engineers about this after the fact.
[540.22 → 544.12] And they, instead of like what you would expect, just shutting it off.
[544.38 → 548.66] Instead, they switched it out with what they call Catgut.
[549.36 → 554.30] And just all of a sudden, one day in our discord, we started getting hundreds of messages from
[554.30 → 555.88] users saying, I think I got hacked.
[556.20 → 559.20] I'm seeing all these meows, like in response to my thing.
[559.20 → 561.62] So it goes to show, you know, the moral here.
[561.98 → 566.74] And I ended up hearing from the open AI engineer that they were watching our discord, taking
[566.74 → 570.74] screenshots and laughing their asses up, you know, at this happening.
[570.88 → 577.88] But it goes to show that like one, the kind of level of there's no switching costs to these
[577.88 → 578.40] things, right?
[578.42 → 579.94] It's like text in, text out, fairly basic.
[579.94 → 586.92] And there's like entire new venues of like vulnerabilities of like swapping it out with
[586.92 → 588.48] a, you know, a cat or something.
[588.48 → 593.30] Like what does security look like in this world when it just thought it was an interesting
[593.30 → 594.36] kind of anecdote?
[595.18 → 601.60] Probably that vulnerability of like all of a sudden getting meows like that is a possibility.
[601.60 → 606.08] But I'm wondering, like, as you've spent a lot of time with these models, you've also
[606.08 → 608.96] like you're building products on top of these models.
[608.96 → 618.76] Like from your perspective, taking an LLM integration to that sort of last mile of like integrated
[618.76 → 621.14] into a product, supporting users.
[621.80 → 628.46] What are the things that should be on either developers or data scientists minds as they
[628.46 → 633.70] think about like taking the step from like demo to like product integration?
[633.70 → 635.36] I guess would be the question.
[636.42 → 642.02] So I like to say that absolutely everything in engineering is about trade-offs, and it's
[642.02 → 646.90] about really thoroughly understanding trade-offs and then being able to effectively communicate
[646.90 → 649.00] those trade-offs and the pros and cons and everything.
[649.42 → 651.66] And it really boils down to those two things like over and over.
[651.80 → 655.04] So let's talk about some of the trade-offs that are most important to using language
[655.04 → 655.78] models in practice.
[656.02 → 658.12] You have the most obvious one, which is quality.
[658.12 → 662.18] Like, can I use these language models to actually perform the task that I want?
[662.74 → 667.16] You know, you have oftentimes secondary but equally important trade-offs.
[667.36 → 669.14] Like, how much does this cost to run in production?
[669.50 → 672.10] What is the latency for my use case for the end users?
[672.58 → 674.72] How consistent and reliable is it?
[674.82 → 678.66] Like, can I have actual, is my use case fault-tolerant?
[679.16 → 682.94] Which is a great initial question because we're kind of moving from a world of like very
[682.94 → 687.92] deterministic human driving the program to a world where the more control you give to
[687.92 → 691.54] language models and their reasoning abilities, this is getting more into the agentic side
[691.54 → 697.54] of things, the more that it becomes slightly non-deterministic or very non-deterministic.
[698.10 → 703.60] And so the ability to have guardrails around these things, the ability to have consistency
[703.60 → 706.10] and predictability is extremely important.
[706.28 → 709.96] And one of the first questions that you should ask yourself, are you thinking about like integrating
[709.96 → 714.52] with LLMs is for your particular use case, for your job to be done, for your customers,
[714.52 → 720.60] to what extent, you know, do you need a hundred percent reliability versus like 99% reliability?
[720.90 → 723.60] And that may sound like a little bit for certain domains of problems.
[723.84 → 724.76] It's everything, right?
[725.22 → 727.14] And so that's one fundamental question.
[727.24 → 728.96] There are techniques, and we can talk about them.
[729.08 → 732.44] I'm sure you guys are very aware as well of like going from that 99%, getting close,
[732.70 → 734.08] adding extra nines of reliability.
[734.08 → 739.02] And, you know, that's also a very active area of research where folks are actively figuring
[739.02 → 741.72] out ways to increase the reliability of these models.
[741.72 → 748.38] But the fundamental trade-offs are, you know, quality, cost, latency, and reliability.
[749.02 → 754.14] And using a hosted model is going to be great for quickly, like with minimal resources and
[754.14 → 755.22] validating your use case.
[755.40 → 759.88] For a lot of those types of trade-offs, it may make more sense than to use a local model.
[760.28 → 764.16] And there's kind of been this Cambrian explosion of open source, large language models and other,
[764.32 → 766.20] you know, specialized machine learning models.
[766.48 → 768.94] And we're going to continue to see that proliferate.
[768.94 → 774.34] I like to think of the open source kind of state of the art as, you know, six to 12 months
[774.34 → 776.18] behind the proprietary versions.
[776.56 → 780.54] We'll see if that holds, but, you know, it's kind of because there's like zero switching
[780.54 → 784.54] costs with these models, because there's just so much competition, the price is going to
[784.54 → 786.06] keep going down over time.
[786.22 → 790.22] We're going to see the open source side of these models continue to get more powerful.
[790.74 → 795.06] And so for a lot of use cases where you're dealing with, well, maybe I need ultra low latency
[795.06 → 799.38] on device or maybe, you know, cost is a factor and I need to be running in my own data centres
[799.38 → 803.84] or maybe, you know, you need to, after a certain point, once you validate your use case, you
[803.84 → 809.12] want to fine tune and distill the model down and have a really locked in, like a check pointed,
[809.34 → 811.44] this is like completely unit tested.
[811.60 → 814.20] This is, you know, evaluated version of things.
[814.20 → 818.60] And I think we're at the stage right now where there's so much like hype and so many people
[818.60 → 820.50] building AI applications and demos.
[821.02 → 821.76] And that's great, right?
[821.76 → 825.80] Just getting it out there, proliferating through open source, through Twitter, whatever it is,
[825.84 → 825.98] right?
[826.00 → 826.52] This is awesome.
[826.80 → 831.88] But the version of that last mile and the product ionization concerns really need to dive
[831.88 → 835.50] deep on all of this kind of fundamental trade-offs that I'm talking about in the hosted
[835.50 → 839.00] models versus local models and, and, you know, fine-tuning distillation.
[839.14 → 841.26] They all become really important very quickly.
[844.20 → 858.70] So, uh, before the break, as we were talking about these different characteristics that
[858.70 → 864.72] kind of affect applied AI and affect deployment, I was really taken by the fact that so many
[864.72 → 867.54] of them are not really AI specific.
[867.54 → 872.72] You know if you could almost argue that applied AI in so many ways is about software, it's about
[872.72 → 873.64] the systems.
[873.64 → 874.80] It's now about cloud.
[874.80 → 881.00] It's about all these other things blended together to produce solutions that are productive in
[881.00 → 884.10] the world and, and have value for people and organizations.
[884.44 → 887.10] You know, we talked about unit testing and stuff like that.
[887.18 → 891.74] What is your thinking around kind of the integration of all those things?
[891.74 → 896.42] Cause the model itself, you know, to your point about hype still kind of gets all the attention
[896.42 → 898.14] and the amazing things.
[898.14 → 903.54] And it is amazing what we're doing, but to make this stuff work in life, there's all these
[903.54 → 908.70] other concerns that there are so many cool things in 2023 happening on the model side that the
[908.70 → 912.76] other 99% to make it real, uh, kind of gets.
[912.76 → 919.72] When you're working with people around understanding how all this fits together so that they can do that.
[920.12 → 923.38] How do you frame that so that their attention gets on the right thing?
[923.46 → 926.92] Their budgets are properly allocated to attend to all the things.
[926.92 → 933.32] I've seen organizations really struggle with that because they go into it with hype, focusing on just
[933.32 → 936.80] the model and building skill sets and budgets around the model.
[937.00 → 941.78] And then they try to figure out the whole thing with clouds and deployment and things afterwards.
[941.78 → 943.30] And they have a hard time.
[943.46 → 946.80] How do you navigate that given the hype cycle that we're operating in?
[947.58 → 954.24] My first piece of advice would be that for your particular use case is your job to be done,
[954.38 → 956.20] whatever business use case you're solving.
[956.54 → 961.56] And to keep in mind that AI, like all software is a tool, and it may be a really shiny tool.
[961.68 → 964.26] It may be a tool that is evolving very quickly in front of us right now.
[964.46 → 968.84] It's a very powerful tool, but it is a tool to solve, you know, a business use case in a problem
[968.84 → 969.40] for humans.
[969.40 → 972.92] So rooting, you know, the framing in that I think is very important.
[973.64 → 980.52] The second thing I'll say is a lot of AI right now, and especially the stuff that gets a light
[980.52 → 985.44] shined on it and in the open, because the application layer is so new and there's so much
[985.44 → 990.14] low-ganging fruit, you know, as you said, like we need to have more emphasis on the engineering
[990.14 → 991.42] rigour under the hood.
[991.42 → 999.38] And so on practical piece of advice there is to really focus on an evaluation set for
[999.40 → 1000.60] your particular use case.
[1000.86 → 1002.54] And you might have existing data.
[1002.62 → 1005.78] You might have existing kind of input-output pairs for your particular example.
[1005.96 → 1009.70] You might have, you might not have that, but like starting from there and working backwards
[1009.70 → 1012.78] of like, this is what the end user is going to see.
[1012.78 → 1017.36] And then working backwards from that to think about, well, how can I use language models
[1017.36 → 1020.40] or other expert focused machine learning models to solve that?
[1020.62 → 1025.10] I think is very important because that also gives you a grounded North star.
[1025.10 → 1031.26] Like so much of the prompt engineering and tuning of these models is based around, well, I think
[1031.26 → 1035.46] this is going to work better, or I eyeball it on this one example, and it seems to work for
[1035.46 → 1035.90] this, right?
[1036.00 → 1041.58] But really applying some fundamental engineering rigour at that level where you have an evaluation
[1041.58 → 1046.52] set that you can track, that you can improve over time, that you can, and not just tracking
[1046.52 → 1050.36] the quality of these models, but, you know, attracting the other trade-offs in terms of pricing,
[1050.36 → 1055.44] latency, recall, like there's a whole slew of trade-offs that can matter depending on
[1055.44 → 1057.34] your particular, you know, use case.
[1057.76 → 1063.38] And then the other piece of practical advice I would say is the kind of diagram of this
[1063.38 → 1065.90] ladder of complexity that I was referring to before.
[1066.28 → 1069.94] Like every time you take a step down that ladder of complexity from using a hosted model,
[1070.20 → 1074.92] just using prompting, and then going to, you know, some type of information retrieval embedded
[1074.92 → 1081.70] in the context to having a multiple chains of prompts to going down to fine-tuning, you know,
[1081.72 → 1085.84] a hosted model or fine-tuning a local model that the very, very bottom is building your
[1085.84 → 1086.74] own model, right?
[1086.78 → 1090.70] Like every time you take a step down that ladder of complexity, it adds engineering complexity.
[1091.76 → 1095.02] It's going to make your solution more complex to maintain.
[1095.40 → 1100.30] And so really like having a good handle on how you can start simple and only move down,
[1100.42 → 1103.96] you know, when you need to, or when you hit a constraint, like, okay, this is great.
[1103.96 → 1107.66] And I have a working solution with a hosted API, but now I need to worry about the price
[1107.66 → 1110.92] because I'm going to production and, you know, the unit economics, like maybe at that
[1110.92 → 1114.62] point, then you think about, well, now I have this great solution and I can auto generate
[1114.62 → 1118.22] an evil set for myself and, you know, have a bunch of inputs and outputs and fine tune
[1118.22 → 1121.54] a model that is hyper distilled and efficient and focused.
[1121.82 → 1122.40] That's great.
[1122.48 → 1124.42] Don't start there for most use cases, right?
[1124.60 → 1130.10] The one other thing I would say at the practical level is where language models tend to break down
[1130.10 → 1133.90] or lack reliability is oftentimes when you're trying to give too much to the
[1133.90 → 1134.84] model to do it once.
[1135.12 → 1140.32] And so breaking the problem down into sub problems that are a lot more focused is one
[1140.32 → 1142.12] of the most practical.
[1142.26 → 1145.84] Like I just find myself telling people over and over again, it's like, okay, that's awesome.
[1146.22 → 1147.66] Break your problem up into some problems.
[1147.66 → 1150.26] And you know, how to do that is a whole arc forward in itself.
[1150.26 → 1153.68] And maybe someday in the near future, language models will do that for us.
[1153.80 → 1154.30] I don't know.
[1154.50 → 1154.68] Right.
[1154.72 → 1157.72] That's getting into the more sensational side of things.
[1157.72 → 1162.64] But as a general principle, breaking your problem up into sub problems, thinking about
[1162.64 → 1169.04] how you can articulate your problem as succinctly as possible in a way that is native to the
[1169.04 → 1171.08] language models is a really key practice.
[1171.08 → 1177.42] I love how you talked about like evaluation, forming your evaluation set, getting some ground
[1177.42 → 1182.28] truth, also breaking up your problem, maybe having an evaluation set for each of those
[1182.28 → 1184.48] sub problems would be a good idea.
[1184.70 → 1191.32] I think there's this general perception that large language models are this kind of unique
[1191.32 → 1191.78] thing.
[1191.90 → 1194.38] These chat interfaces are this kind of unique thing.
[1194.38 → 1200.18] Like we can't, how do you like to evaluate that in the way, like, I think what people have
[1200.18 → 1204.94] in their mind is, oh, if I'm doing sentiment analysis, it's either positive or negative or
[1204.94 → 1205.28] neutral.
[1205.40 → 1211.32] And I can like to calculate an accuracy, for example, whereas they might struggle to think about,
[1211.50 → 1214.50] okay, well, there's this output from this language model.
[1214.50 → 1218.18] It seems coherent and fluent.
[1218.46 → 1220.06] Like, how do I evaluate this?
[1220.06 → 1224.54] And so I think there's maybe a bit of confusion around the evaluation side.
[1225.06 → 1230.94] Can you share any tips or thoughts in terms of what you found to be useful in your own
[1230.94 → 1238.84] work in terms of evaluation sets and like how you think about how good the output of a language
[1238.84 → 1239.44] model is?
[1240.44 → 1245.92] My first thought would be the less that it's about me thinking about how good it is and
[1245.92 → 1250.32] the more that it can be objective, like using some constant way of evaluating it, the better.
[1251.00 → 1254.52] There's one project that I really like recently by Lance Martin.
[1254.74 → 1255.74] It's called Auto Evaluator.
[1255.98 → 1260.22] I don't know if you guys have seen it, but it's specifically for the domain of QA.
[1260.50 → 1261.52] So question answering.
[1261.90 → 1265.62] And he recently partnered with Lang chain to create a hosted version of it.
[1265.72 → 1268.36] But the way that I think about this is a little abstract.
[1268.56 → 1271.46] And it's really like starting from your job to be done.
[1271.76 → 1273.98] Oftentimes sentiment analysis isn't the job to be done.
[1273.98 → 1276.20] It's like a piece of a job to be done, right?
[1276.32 → 1280.30] So again, it's like breaking up the problem and understanding how to think about and structure
[1280.30 → 1285.32] those problems as whether it's an expert model that just does sentiment analysis or it's
[1285.32 → 1288.62] using a large language model that like it can do sentiment analysis.
[1288.62 → 1291.68] It's perfect at that, but it's also like it can do a bunch of other things as
[1291.68 → 1291.90] well.
[1292.58 → 1299.12] So the more focused your task is, the more clearly articulated your task is, and the more structured
[1299.12 → 1304.76] of the output that you have at the individual LLM call level, the better and the easier it is to
[1304.76 → 1309.82] create reliability around these things and to actually test them with more traditional
[1309.82 → 1313.44] software engineering practices like writing unit tests or integration tests.
[1313.94 → 1317.98] You know, one thing that I'm actively working on right now for the TypeScript community is
[1317.98 → 1322.82] a way to invoke large language models and have structured guards on them.
[1322.90 → 1325.92] I know like prediction guard, guard wheels, there are a few projects that are doing this,
[1325.92 → 1330.58] but really then having that actually be typed in TypeScript so you can make an LLM call like
[1330.58 → 1335.14] it's a function, but get some JSON that has these fields that has these types and have
[1335.14 → 1340.06] it kind of, you know, there are techniques that you can do under the hood to self-heal if
[1340.06 → 1343.50] the JSON isn't properly formed or, you know, maybe you want to generate some TypeScript code
[1343.50 → 1346.94] and you want to validate that's a correct AST or something like there are techniques that
[1346.94 → 1352.42] you can do to constrain the output of the language model for your particular task.
[1352.42 → 1356.96] But in my view, these techniques are constantly shifting kind of the best practice in the
[1356.96 → 1357.66] state of the art there.
[1358.10 → 1362.56] And so I think libraries like Lane Chain and the open source framework that I'm currently
[1362.56 → 1366.66] working on, you know, I think will do a lot to help developers to abstract out some of
[1366.66 → 1369.12] the complexity of just viewing this as a general purpose tool.
[1369.78 → 1371.08] And again, it's like you start simple.
[1371.38 → 1374.78] One of the great things about language models is they can do just about anything.
[1374.88 → 1376.76] That's also one of the downsides, right?
[1376.80 → 1380.10] Like when it's so unconstrained, how do you even approach the problem?
[1380.10 → 1384.32] So having best practices, having like examples, constraining the problem.
[1384.32 → 1390.22] And really it's like the ability to have a unit test or an assertion in a traditional
[1390.22 → 1394.72] programming language at the large language model call level where it's like, I assert
[1394.72 → 1399.62] that the output should be valid JSON or I assert that the output should conform and be valid
[1399.62 → 1400.58] TypeScript syntax.
[1400.98 → 1405.46] And if not, like actually self-reflect on that and put it back into the large language model
[1405.46 → 1406.34] and regenerate it.
[1406.34 → 1410.08] All of those things I think are foundational primitives at the large language model level
[1410.08 → 1416.98] that will allow developers who want to build real reliable applications to do so more
[1416.98 → 1421.04] reliable because they can focus on their domain specific, you know, business logic or aspects
[1421.04 → 1425.44] that are away from a lot of this kind of implementation details that are also constantly shifting under
[1425.44 → 1426.12] our feet, right?
[1426.80 → 1427.60] Fantastic explanation.
[1427.82 → 1431.70] You keep talking over and over again about how things are shifting and the evolution of the
[1431.70 → 1432.78] engineering around it.
[1433.02 → 1439.36] That puts a burden on these hackers and developers that are trying to go out and implement these
[1439.36 → 1444.64] things at this point, because this year has just been, you know, phenomenal progress, but
[1444.64 → 1450.40] that makes it really hard for mere humans here to kind of track that and keep up with it.
[1450.62 → 1455.80] So you kind of talked about some of the concepts right there, but if you're thinking about like
[1455.80 → 1460.42] you're about to turn to somebody who's a hacker, and they're looking for that guidance, what
[1460.42 → 1468.68] are some really, you know, not necessarily comprehensive, but hey, go do one, two, three or ABC and that
[1468.68 → 1470.50] will help you kind of keep levelling up.
[1470.56 → 1474.76] Like what are some of the things that you're telling people these days to say, if you want
[1474.76 → 1480.88] to keep up this year with what's all with this insane progress and LLMs and all the different
[1480.88 → 1484.38] model types that we're seeing the progress of, what are you going to do in a practical
[1484.38 → 1486.82] side as a hacker to manage that?
[1487.16 → 1489.48] Do you have any tips that you can kind of take us through about?
[1489.70 → 1490.02] Absolutely.
[1490.40 → 1491.44] One is super noisy.
[1491.66 → 1492.78] There's so much happening.
[1493.00 → 1494.66] We're in the middle of this exponential wave.
[1495.14 → 1497.80] And, you know, I think a lot of people are like, oh, I felt well, I want to be on this
[1497.80 → 1498.38] wave, right?
[1498.50 → 1499.42] But where do I start?
[1499.50 → 1504.30] And there's just, just so much noise, which is great on the one hand, but on the practical
[1504.30 → 1506.00] side, like, how do you give advice?
[1506.06 → 1506.56] Where do you start?
[1507.00 → 1509.00] So, you know, there are a couple levels to this.
[1509.00 → 1513.56] Um, I have talked, uh, given some talks to kind of like a chat TVT for beginners type
[1513.56 → 1513.86] crowd.
[1513.96 → 1519.06] And really it's like my main advice is one, just use it, just go and try it.
[1519.06 → 1519.26] Right.
[1519.26 → 1519.76] That's simple.
[1520.06 → 1524.58] But two, more importantly, like the next time you have an actual problem that you think
[1524.58 → 1530.64] like, maybe I could use a chat TVT or a language model for actually try using it to solve your
[1530.64 → 1531.16] own problem.
[1531.24 → 1536.08] Cause what that does is it starts to build up this muscle in your brain around thinking
[1536.08 → 1538.44] about using these new type of tools to solve problems.
[1538.44 → 1540.62] And it's really a different type of tool.
[1540.76 → 1541.54] It's like exercise.
[1541.64 → 1544.30] You need to start exercising that muscle early and often.
[1544.30 → 1545.66] And there's a lot of noise.
[1545.72 → 1546.82] There are a lot of different AI tools.
[1546.96 → 1550.66] The side of things which I'm confident will be just as relevant, you know, a year from
[1550.66 → 1556.62] now, a couple of years from now is building up that muscle to think about using, uh, how
[1556.62 → 1560.20] to actually use AI to solve your own particular problems.
[1560.20 → 1565.14] It's one thing to talk about like, uh, hypotheticals and general like cases of problems where these
[1565.14 → 1569.58] tools excel, but it's another thing entirely to start building your own personal, you know,
[1569.58 → 1570.14] a muscle.
[1570.52 → 1571.60] Totally agree with that.
[1571.70 → 1575.50] I have a, you know, whether it's a personal problem and you want to just go, you know,
[1575.50 → 1579.80] talk to the chat TVT or you have a problem at work, and you're like, well, I think I could
[1579.80 → 1584.82] use a language model, a hosted API to solve this or something like starting simple, starting
[1584.82 → 1589.52] from your own problems will start to build up that muscle, and you'll, you'll naturally
[1589.52 → 1590.98] learn it and take it from there.
[1605.06 → 1611.62] So Travis, you've mentioned a couple of times, like TypeScript node, this community that like
[1611.62 → 1618.34] you're a part of, and I think there's probably a lot of Python people listening to this show,
[1618.48 → 1620.46] maybe data scientists, practitioners.
[1620.88 → 1624.30] To me, it almost seems like there's like two communities.
[1624.44 → 1628.44] There's like all of these data scientists trying to figure out like, oh, large language
[1628.44 → 1633.64] models, generative AI has sort of broken my intuition around like how, what I need to
[1633.64 → 1634.06] be doing.
[1634.18 → 1636.10] Like, do I need to be training models now?
[1636.20 → 1637.98] Like, how do I solve this problem now?
[1638.10 → 1640.06] I was training models last year.
[1640.06 → 1641.58] Do I still need to be doing that?
[1641.66 → 1643.66] So there's like that side of things.
[1643.66 → 1649.24] And then there's like this really vibrant community of front end developers and other
[1649.24 → 1653.94] developers that are building, even like people that are maybe like low code, no code people
[1653.94 → 1658.02] building really cool products around this technology.
[1658.24 → 1663.60] You seem to be sort of like exposed to a lot of those things.
[1663.70 → 1666.42] How do you see these communities developing over time?
[1666.42 → 1673.78] And like, how have you seen the maybe the TypeScript, the Node, JavaScript type crowd kind
[1673.78 → 1679.70] of rise up to meet these technologies, maybe in a way that the sort of traditional data
[1679.70 → 1683.54] scientist crowd has not or has differently, I guess.
[1684.02 → 1688.50] To some degree, a lot of the JavaScript TypeScript world is like jealous of the Python world, right?
[1688.50 → 1693.10] Because it's all the cool new AI stuff is like Python first or, you know, using this machine
[1693.10 → 1694.08] learning framework or whatever.
[1694.46 → 1699.20] And this is where like hosted APIs, whether it's Replicate or Hugging Face, so you got
[1699.20 → 1699.82] a hat on, right?
[1700.04 → 1705.52] Hugging Face or OpenAI or Cover or like all these hosted models are a massive unlock for
[1705.52 → 1706.48] application developers.
[1707.20 → 1710.66] And TypeScript is the largest programming language in the world.
[1711.22 → 1712.22] Python is, it's big.
[1712.28 → 1715.68] It's the largest by far in the data science in machine learning world for sure.
[1715.68 → 1721.08] And so, you know, there's this dynamic between the two where I think we're seeing at the
[1721.08 → 1727.60] application layer, folks who are good at building full stack apps that can easily plug in to
[1727.60 → 1732.72] hosted models and things who really push the envelope in terms of like unlocking people's
[1732.72 → 1735.06] imaginations, building a good UX around these things.
[1735.06 → 1740.70] That's so important, like to make it more approachable for people and to really like show
[1740.70 → 1743.98] people what a lot of the machine learning people have known about for a long time.
[1743.98 → 1746.16] Right. But like you need both sides of that equation.
[1746.34 → 1750.62] So one of the projects I did a couple of months ago was I ported scikit-learn to TypeScript
[1750.62 → 1753.86] and it's not like a full port, you know, it's like auto generates all the TypeScript
[1753.86 → 1755.48] classes, like 260 classes.
[1755.82 → 1760.88] And then under the hood, it creates a sub process, a Python sub process, and then marshals and
[1760.88 → 1762.74] does the interprocess communication between them.
[1762.74 → 1768.78] But it works extremely well, and you can call and do k-means and PCA and just all these fundamental
[1768.78 → 1771.72] things that the Python machine learning world takes for granted.
[1771.72 → 1775.40] There are versions of that exist in the NPM ecosystem.
[1775.40 → 1779.88] It's just they're all over the place in terms of quality, in terms of like there's so many
[1779.88 → 1784.46] just fundamental aspects of machine learning that the TypeScript world is missing out on.
[1784.74 → 1790.16] And one of the primary drivers behind kind of what I'm working on, and I'm, you know,
[1790.16 → 1795.28] happy to share, like I'm building a reliable TypeScript open source framework for building
[1795.28 → 1796.08] reliable agents.
[1796.62 → 1796.92] Very cool.
[1796.92 → 1797.70] Thank you.
[1797.80 → 1802.44] I view agents as this new, like if large language models are CPUs, right?
[1802.50 → 1805.04] And kind of this new compute paradigm, there are these reasoning engines.
[1805.18 → 1808.76] Like, yeah, they're great at generating text, but the real emergent property, the real game
[1808.76 → 1810.80] changing property of them is reasoning.
[1811.16 → 1815.52] If they're kind of the new reasoning engines, and you have like that, that's your CPU layer.
[1815.52 → 1817.14] And then you have like a storage layer.
[1817.24 → 1820.42] That's all these vector databases and kind of overhyped on that side of things.
[1820.42 → 1823.46] On top of that, you have like, how do you actually run programs?
[1823.92 → 1825.38] And that's, you know, agents.
[1825.56 → 1830.38] And I view it as like, there's kind of a spectrum of like traditional programming that might happen
[1830.38 → 1831.64] to use a large language model.
[1831.86 → 1836.00] And then on the other end, you have like full self-driving agents that are making decisions
[1836.00 → 1838.80] and creating tasks and just fully autonomous, right?
[1839.18 → 1844.32] And I'm excited to kind of focus on somewhere in the middle and focus on more reliable like
[1844.32 → 1846.32] use cases that we can actually build reliably today.
[1846.32 → 1851.82] But to your question about kind of the TypeScript Python world, a lot of the frontier, the libraries
[1851.82 → 1855.56] at the framework level that are pushing the edge here are all Python first, right?
[1855.60 → 1860.18] And I really want to take a TypeScript first approach, partially because it's the community
[1860.18 → 1861.04] that I know and love.
[1861.12 → 1863.08] It's my like best tool on my tool belt.
[1863.32 → 1867.54] And partially because I think people building real applications at the application level,
[1867.84 → 1871.00] a lot of those folks are more in the JavaScript TypeScript world.
[1871.38 → 1875.14] So you have hit an area that I have so much passion for.
[1875.14 → 1875.88] Oh, awesome.
[1875.88 → 1879.34] I'm sitting here waiting to ask my next question here.
[1879.72 → 1884.38] And Daniel has heard me whine about this for years, what I'm about to say.
[1884.76 → 1886.20] And so I want to get your take on it.
[1886.36 → 1890.76] So like there is more to the world than just Python.
[1890.76 → 1895.68] And I'm a multi-language person and I don't necessarily go all in on any one language or
[1895.68 → 1895.96] the other.
[1896.12 → 1897.28] I'm a TypeScript user.
[1897.48 → 1900.54] In the last year, I've been doing Rust.
[1900.54 → 1905.44] I had been doing more Go before that outside of the AI and Python stuff.
[1905.50 → 1911.10] But I hit a use case where I was building something and I had to eat every little bit of performance
[1911.10 → 1914.10] out of the available hardware to do what it was.
[1914.18 → 1917.52] It was going to be C++ or Rust when it wasn't going to be C++.
[1917.52 → 1919.76] So I went to learn Rust.
[1919.92 → 1922.04] And then I'm in Rust, and I'm doing that.
[1922.14 → 1926.48] And I'm looking at, as an analogy here for what we're about to go at, I'm looking at WebAssembly
[1926.48 → 1932.90] and the Rust community and other language communities are so into that fact of write it in with the
[1932.90 → 1939.36] thing that you need to be in and yet have access to that in terms of deployment and still having
[1939.36 → 1940.46] great performance and stuff.
[1940.94 → 1947.10] And every time I'm now messing with WebAssembly in Rust, I'm thinking, when is the AI world
[1947.10 → 1955.34] going to catch up on having, you know, multifaceted from a language standpoint, access to the models
[1955.34 → 1957.26] instead of everything being Python first?
[1957.78 → 1962.88] And so asking the pardon of the Python lovers in the audience, when am I going to be,
[1962.90 → 1968.80] in Rust or Go, and you're obviously doing it in TypeScript, but the language of my choice
[1968.80 → 1974.86] and taking advantage of, as you called it, the new CPU of reasoning from that point, instead
[1974.86 → 1980.32] of having to do a context switch, it is an ongoing year after year frustration
[1980.32 → 1982.74] that I have, as you can probably tell by now.
[1983.20 → 1987.88] So I'm hoping that you're about to give me the golden path out of here because I need one.
[1988.66 → 1988.72] Okay.
[1988.88 → 1990.38] Well, first, I love your framing.
[1990.62 → 1991.72] I love your passion for this.
[1991.72 → 1993.22] I also feel very similarly.
[1994.22 → 1999.64] I think the reason why I'm starting with TypeScript is because of the developer experience
[1999.64 → 2003.80] at the application level, I think is really important for the type of framework I'm looking
[2003.80 → 2004.12] to build.
[2004.62 → 2013.74] But I view WebAssembly, or Wasm, as kind of the ultimate compiled language runtime that,
[2013.82 → 2014.70] you know, I want to target.
[2014.70 → 2020.34] Because you could imagine a world not too distant from right now where you have agents that are
[2020.34 → 2023.30] running, you know, in data centres, they're running on edge.
[2023.62 → 2028.42] So anything that's kind of, you know, whether it's a Cloudflare worker or a Va sell edge function
[2028.42 → 2031.68] or within a service worker in your browser, right?
[2031.68 → 2033.40] But the common thread there is Wasm.
[2033.40 → 2038.26] You know, to what extent, starting with developer experience at the TypeScript level and then
[2038.26 → 2043.20] focusing on that at the runtime level, there's still a clear path forwards for a lot of folks
[2043.20 → 2045.30] for just like using hosted APIs.
[2045.60 → 2048.16] You know, that's one area that you can have that multi-language very easily.
[2048.30 → 2049.36] That's a natural point.
[2049.36 → 2053.20] But you got to be kind of in the cloud for most of that in a practical sense, which I'm
[2053.20 → 2053.64] not always.
[2053.84 → 2054.72] Yeah, 100%.
[2054.72 → 2058.84] And then there's like the whole open source models or the practical side of things where
[2058.84 → 2062.66] you're like, well, I need to have full hardware or the latency or something that's like on
[2062.66 → 2063.06] device.
[2063.64 → 2070.30] And I am extremely bullish on WebAssembly as there's a quote that I like, and it was from,
[2070.50 → 2072.84] I forget who it was from, from the Linux Foundation or something.
[2072.92 → 2077.98] It was like, you know, if WebAssembly existed 10 years ago, then Docker would have never needed
[2077.98 → 2078.82] to exist, right?
[2078.82 → 2081.80] And I think it will have that level of impact eventually.
[2082.16 → 2083.06] I think potentially.
[2083.32 → 2083.72] I do too.
[2084.14 → 2084.30] Yeah.
[2084.38 → 2089.70] I think potentially the kind of unlock here that the path that could bring it into the
[2089.70 → 2091.36] more of the mainstream could be AI.
[2091.62 → 2097.50] I don't know at the model level, there's just so much momentum behind Python, you know, and
[2097.50 → 2100.24] all the core kind of researchers in this other Python first.
[2100.52 → 2106.40] So when I did the sci kit learn kind of port to TypeScript, there was, I think, a Python port
[2106.40 → 2107.40] called Pyoid.
[2107.40 → 2111.24] And it's a Python runtime.
[2111.46 → 2115.14] You guys might know better than I do, but it's targeting WebAssembly, and it allows them
[2115.14 → 2120.40] to run subset of sci kit learn in WebAssembly support environments, including Node.js on the
[2120.40 → 2120.70] browser.
[2120.94 → 2122.98] And that's super, super fascinating to me.
[2122.98 → 2126.38] Yeah, I think that there are a couple of related projects.
[2126.58 → 2132.06] I think like Script from Anaconda is like trying certain things like that.
[2132.18 → 2138.62] But I'm really interested in that space as well, because I've seen its sort of like a
[2138.62 → 2141.96] different kind of diversity than we normally talk about.
[2141.96 → 2147.20] But the fact that like more developers from more diverse backgrounds are at the table building
[2147.20 → 2149.70] AI things, I think is an amazing thing.
[2150.08 → 2152.34] And I think a lot of good is going to come from that.
[2152.48 → 2155.34] So I'm really happy to see a lot of that happening.
[2156.04 → 2159.70] Well, if we have time, just one more maybe controversial take on this.
[2159.98 → 2160.12] Sure.
[2160.42 → 2161.76] We like controversial takes.
[2162.10 → 2162.42] Awesome.
[2162.56 → 2162.84] Awesome.
[2163.16 → 2169.50] You know, as we get closer to building reliable agents in the way that I kind of was framing
[2169.50 → 2173.04] it before, it's kind of a fundamental new compute paradigm with large language models
[2173.04 → 2175.64] of CPUs, and you're building these agents on top of them.
[2176.04 → 2180.36] As they eventually get more and more reliable and more autonomous, right now, a lot of them
[2180.36 → 2181.54] are just toys, let's be clear.
[2181.54 → 2187.70] But as that happens, I view it as a new higher level programming language, you know, and we're
[2187.70 → 2188.70] working with natural language.
[2189.18 → 2192.28] The AST of that language is, in my view, a directed graph.
[2192.36 → 2196.76] And the nodes are like specific LLM calls or a call to a tool or a call to an API.
[2196.76 → 2202.22] And, you know, there are massive problems around how to add reliability at that level of kind
[2202.22 → 2205.96] of structured output or guard wheels, like some of these things are clearer than others.
[2206.14 → 2209.72] And then at the whole graph level, you know, that becomes a program or an agent.
[2209.82 → 2214.40] To some degree, we're talking about all of these like Python and Rust and implementation
[2214.40 → 2215.92] details, and that's all very important.
[2215.92 → 2221.50] But I wonder to what extent, you know, 10 years from now, we will even be talking about a lot
[2221.50 → 2226.00] of the current levels of programming abstractions that are hyper relevant to us today as practitioners
[2226.00 → 2231.86] or how quickly we'll move towards this world of a higher level abstraction for solving problems
[2231.86 → 2235.90] that is just significantly more efficient, more approachable, because it's kind of based
[2235.90 → 2236.74] on natural language.
[2237.26 → 2240.48] Anyone in this field that talks to you about timelines, you know, is like just throwing
[2240.48 → 2243.02] a dart, ran it with a blindfold on.
[2243.16 → 2245.90] But that's one thread that I'm really excited about.
[2246.56 → 2251.30] You kind of went already ahead to where I was hoping you would go, which is what's keeping
[2251.30 → 2255.72] you up at night, what's in your mind in terms of like looking forward and all of that.
[2255.82 → 2256.56] And I agree.
[2256.66 → 2260.24] I think this is a really, fascinating direction.
[2260.24 → 2264.24] And I certainly hope that we see that timeline progress rapidly.
[2264.42 → 2265.62] I think we probably will.
[2265.88 → 2269.02] So, yeah, it's been a pleasure to have you on the show, Travis.
[2269.28 → 2274.46] Really looking forward to keeping in contact and seeing all the amazing things you do and
[2274.46 → 2276.48] trying out some things in TypeScript.
[2276.48 → 2281.40] It's an exciting time to be part of this and yeah, looking forward to keeping in contact.
[2281.54 → 2282.56] Thanks for joining us.
[2291.04 → 2293.60] Thank you for listening to Practical AI.
[2294.12 → 2297.94] Your next step is to subscribe now if you haven't already.
[2298.38 → 2303.06] And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2303.06 → 2304.42] AI with your friends and colleagues.
[2304.42 → 2309.80] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2310.38 → 2314.16] Check out what they're up to at Fastly.com and Fly.io.
[2314.56 → 2319.16] And to our Beat Freakin' Residence, Break master Cylinder, for continuously cranking out the best
[2319.16 → 2319.88] beats in the biz.
[2320.18 → 2321.06] That's all for now.
[2321.38 → 2322.48] We'll talk to you again next time.
[2322.48 → 2323.48] Bye.
[2323.48 → 2324.48] Bye.
[2324.48 → 2325.48] Bye.
[2325.48 → 2326.48] Bye.
[2326.48 → 2327.48] Bye.
[2327.48 → 2328.48] Bye.
[2328.48 → 2329.48] Bye.
[2329.48 → 2330.48] Bye.
[2330.48 → 2331.48] Bye.
[2331.48 → 2332.48] Bye.
[2332.48 → 2332.54] Bye.
[2332.54 → 2332.58] Bye.
[2332.58 → 2332.62] Bye.
[2332.62 → 2332.66] Bye.
[2332.66 → 2332.68] Bye.
[2334.42 → 2335.42] Bye.
