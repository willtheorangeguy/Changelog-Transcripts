[0.00 → 8.66] Welcome to Practical AI.
[9.14 → 19.56] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.38] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 → 35.44] So you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.50 → 47.54] Welcome to another fully connected episode of the Practical AI podcast.
[47.54 → 54.74] In these fully connected episodes, we try to connect you with various things happening in the AI space.
[54.92 → 61.26] And connect you with maybe some learning resources or talk about some subjects that will level up your machine learning game.
[61.80 → 63.20] My name is Daniel Whiten ack.
[63.32 → 68.48] I am founder and CEO at Prediction Guard, where we're enabling AI accuracy at scale.
[68.70 → 74.98] And I'm joined as always by Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[75.28 → 75.92] How are you doing, Chris?
[75.92 → 77.06] Doing great today.
[77.22 → 79.76] It's dog days of summer here in the U.S.
[79.76 → 82.60] It is really hot and humid.
[83.02 → 83.22] Yeah.
[83.42 → 85.58] Super humid and nasty.
[86.04 → 90.14] I'm looking forward to AI control, you know, like weather control from AI.
[90.32 → 93.38] And it will keep all of us at just the right temperature.
[93.60 → 94.14] Right.
[94.28 → 97.48] I can't see anything possibly going wrong with that.
[97.64 → 98.40] Of course not.
[98.46 → 100.30] Only positives there.
[100.72 → 105.70] And that is, regardless, that is in the distant, distant future of 2025, I'm sure.
[105.70 → 106.84] Yeah, exactly.
[107.08 → 107.54] Exactly.
[107.82 → 110.56] Let's focus on the next two weeks for now.
[110.56 → 111.06] That's right.
[111.36 → 112.48] Which is important.
[113.14 → 121.22] I think one of the things that caught me off guard this last few weeks, which you and I try to stay plugged in to various things.
[121.42 → 129.66] And, you know, maybe people think and listen to this podcast that we're, you know, keeping plugged in with every single thing happening in the AI space.
[129.66 → 132.76] But I was a little bit surprised when I saw the release.
[133.02 → 140.10] I guess I just hadn't really been following along with what the company or research lab Tai was doing.
[140.70 → 146.68] So this is an open research lab that researches AI.
[147.58 → 152.14] And they have funding and some support in terms of infrastructure and all of that.
[152.54 → 156.92] But they're a nonprofit research lab in my understanding.
[156.92 → 163.08] And they actually, so we talked on a previous show, we kind of got fooled a little bit.
[163.24 → 168.20] Or maybe it was, you know, a little bit of a fumbling in terms of marketing.
[168.54 → 176.62] But it seemed like when OpenAI GPT 4.0 came out, you know, people were hyped because a lot of the demos were voice based.
[176.62 → 187.38] But at least, you know, at the time of that recording, I'm not sure all of what everyone has access to in the paid and unpaid and enterprise version.
[188.02 → 191.46] But the actual voice assistant for OpenAI was not out.
[191.46 → 213.68] And at least as far as the release date of Tai's voice assistant, which is called Moshe, they were the first to actually release a version of their voice assistant, which it's similar to, in my understanding, what GPT 4.0 is on the multimodal side in that it is a multimodal model.
[213.68 → 219.34] So it's a real-time multimodal model that supports a voice assistant.
[220.02 → 225.00] And this research lab, I think it's like eight people or something like that.
[225.12 → 228.74] Of course, they have resources that are supporting them, right?
[228.82 → 231.64] Like this, I think it was a thousand GPUs or something.
[232.10 → 233.48] They have resources, obviously.
[233.48 → 252.12] But they were able to beat, you know, what is now the Goliath of the AI space, beat them to market with this real-time voice assistant, which I think took a lot of people maybe by surprise or maybe some people were following it closer and expecting it.
[252.12 → 266.36] But I think in this sort of six-month or whatever time period it was when they were working to get this out and beat the kind of Goliath of what is OpenAI, which I think in and of itself is pretty interesting.
[267.06 → 267.44] It is.
[267.68 → 270.60] I mean, you know, so many try.
[271.58 → 277.58] And some of the other Goliaths, you know, the second-tier Goliaths, if you will, are continually trying to compete.
[277.78 → 279.24] And they may touch it.
[279.32 → 280.18] They may fall short.
[280.18 → 287.68] I always love hearing when a smaller group, especially if they're focusing on open solutions, comes out and is able to do well.
[287.86 → 289.26] And they got a cool name, by the way.
[289.98 → 290.52] Yeah, yeah.
[290.66 → 294.40] And it is interesting because this does run.
[294.78 → 299.38] So when you see the demo, and we can pull it up here in a second and maybe ask a few questions.
[299.38 → 304.18] But when you see the demo or the prototype, it obviously still has some rough edges.
[304.18 → 317.02] So I think you have some rough edges that aren't fully kind of productized version, like maybe what you get with the OpenAI voice assistant in the forms that it's in.
[317.02 → 328.96] But it is very impressive also because this is a model that I believe it's models that are of a size that you, or I could run them on even a single GPU.
[328.96 → 332.64] And they're going to open source these models.
[332.64 → 337.66] I don't know what the time frame is on that, what exactly that will look like, what licensing, all of those things.
[337.66 → 339.72] They do have a few talks online.
[339.94 → 346.40] So if any of the listeners know that information and I just haven't run across it, then they can maybe update us.
[346.58 → 353.08] But yeah, they will be open sourcing this, which I think will drive a lot more experimentation.
[354.06 → 360.20] And of course, as we saw with the first open LLMs that were released with Llama and other things,
[360.20 → 369.18] there was, of course, a huge explosion of innovation and experimentation going along with the release of the open versions of those things.
[369.62 → 379.76] And so I expect that there'll be a similar thing with these models and what I assume will be other versions or other families of these types of models moving forward.
[380.30 → 385.72] Yeah, I noticed, you know, going back to your point about being able to run it locally and potentially on a single GPU.
[385.72 → 390.12] They talk about in their press release, they just say compact.
[390.72 → 395.84] Moshe can also be installed locally and therefore run safely on an unconnected device.
[396.06 → 403.24] To extend that a little bit, I think that, you know, there are a lot of larger organizations that are worried about IP concerns.
[403.74 → 407.00] These are topics that we've covered quite a bit on the show in days past.
[407.00 → 421.18] So Moshe may very well find a home in corporate environments, first, where they don't want to send information out, and they want to get the advantage of that because it can probably be run on a single GPU.
[421.74 → 423.82] A lot of edge devices make it possible.
[424.00 → 426.48] So great thinking there in terms of what's possible.
[426.48 → 442.10] And then finally, thinking of my own industry in the defence space, since it can be run in an unconnected or disconnected environment, there are all sorts of things from a government standpoint that they may be willing to do.
[442.28 → 444.08] So it's a great strategy.
[444.34 → 451.82] I love hearing these small companies that might be able to have a big impact in industry by accommodating those concerns.
[451.82 → 480.54] Well, Chris, I find one piece of this whole Tai Moshe thing very interesting, which is almost like it feels a little bit like déjà vu because we back in whenever it was, I forget, you know, what year OpenAI came about is like there's these big players in the AI space, and they were doing, you know, certain pre-trained models and all of this stuff.
[480.54 → 483.94] And robotic things and all of that.
[484.08 → 496.50] And then OpenAI came along and said, oh, we need an open, transparent, nonprofit driven research lab to really promote innovation going forward.
[496.50 → 512.52] And of course, as we have moved forward through that, we've seen OpenAI kind of get away from that sort of pure nonprofit status with a little bit more of a complicated corporate structure, right?
[512.94 → 515.00] Which we've talked about on different shows.
[515.00 → 526.14] But then also, you know, just their release of their work and their research and their models and their data and those sorts of things, of course, has become very not open.
[526.86 → 533.54] And they, of course, have their own reasoning behind that, which at least publicly they would say is related to...
[533.54 → 533.84] Microsoft.
[533.84 → 534.84] Sort of.
[534.84 → 534.88] Sort of.
[535.04 → 535.26] Yeah.
[535.36 → 540.64] Well, at least publicly they would say is related to safety of the use of these models.
[540.86 → 546.58] Of course, you know, there's various people that might guess certain other motivations.
[547.04 → 547.60] Microsoft.
[548.08 → 548.28] Yeah.
[550.18 → 555.72] But yeah, I do find this whole thing sort of like déjà vu.
[555.96 → 558.94] I don't know if you're having the same feeling here.
[558.94 → 572.46] You and I both have a long history in the more than six years now that we've been doing the podcast of supporting open engagement from different organizations, whether they're corporate entities or nonprofits or whatever.
[573.26 → 574.50] And we've seen that from others.
[574.58 → 585.72] I mean, famously, Jan Begun talks about he works for Meta, you know, which is Facebook's parent and talks about nonetheless having open models and all that.
[585.72 → 592.02] And so we tend to shine a spotlight on those organizations that do that wherever possible.
[592.24 → 603.72] We certainly went through that because we've been doing about just after we started the podcast, which was back in 2019 or 2018, actually 2018.
[605.00 → 607.50] And about a year later, OpenAI closed up.
[607.60 → 609.48] So we actually covered that in the early shows.
[610.04 → 611.24] You know, it is what it is.
[611.46 → 612.58] They've done that.
[612.58 → 615.88] They remain an amazing corporate leader in the space.
[616.00 → 617.58] But yeah, they did close all up.
[617.98 → 621.04] And we tend to turn more spotlights toward others like this.
[621.10 → 628.34] So I'm pretty excited to see what Utah is doing and is able to do going forward here.
[628.36 → 633.56] And I hope this I hope they're able to viably play against that top tier competition.
[633.56 → 635.82] I think that would be wonderful to have multiple.
[635.82 → 636.48] Yeah.
[636.48 → 662.94] Do you think that there's any chance for this sort of like open research in the AI space or in the technology space to survive as a sort of bulwark of open, transparent research and open source within the pressures that come, of course, when you release this sort of technology, and you're a leader in the space.
[662.94 → 670.98] And there are actual dollar signs and corporate concerns and certainly like partnerships that are necessary.
[670.98 → 689.48] So, you know, partnering with companies to do this work is almost a reality, I think, in the space, because we talked about this a little bit with the Stanford AI index, where they found that, you know, the bulk of AI research is still happening from the industry side.
[689.48 → 695.92] So I don't know. What are your thoughts? Do they stand a chance at staying the course with this or?
[696.28 → 712.44] I think there's certainly a chance at it. And I would argue it's the same argument I've made in previous shows where we talked on similar topics is that we're seeing is the AI industry has been maturing these years at an incredibly rapid pace.
[712.44 → 720.88] But we're still seeing many of the things occurring that we saw when the software world was really maturing over several decades.
[720.88 → 732.36] And the place where open source has really, really worked are in common touchpoints where all organizations or many organizations need a common thing.
[732.42 → 737.92] And they might build something differentiated on top of that, you know, for their revenue to drive profitability.
[737.92 → 749.08] But there's so much that is underneath that point of differentiation that they and many other organizations can get the benefit out of a lot of effort, a lot of work.
[749.16 → 751.42] A lot of times they'll pay have paid employees do it.
[751.96 → 758.28] So there's a point where working together and doing open stuff makes sense for business, and it drives profitability.
[758.74 → 763.34] It may not be your single point of differentiation, but if it's anything under that, why not?
[763.34 → 769.34] You know why not share the costs and pull expertise for the best possible foundations?
[769.66 → 774.92] And so what I'm hoping is that we continue to see that play out in the AI space.
[775.48 → 783.18] We're seeing, you know, if you look at Hugging Face, we've already talked about the fact that a couple of months ago they announced that they were hosting a million models.
[783.32 → 784.36] Those are all open sources.
[784.88 → 786.26] Really, really impressive.
[786.26 → 796.66] And so I think that there is a good chance that a vibrant, open community around AI can and will continue, and it will have a lot of corporate players involved in it.
[796.68 → 798.10] So I'm very optimistic in that way.
[798.10 → 815.72] Hey friends, this episode of Practical AI is brought to you by our new friends over at Plum.
[816.00 → 823.00] Plum is a low-code AI pipeline builder that helps you to build complex AI pipelines superfast.
[823.00 → 833.46] You can easily create AI pipelines using their node-based editor, iterate and deploy faster and more reliably than coding by hand without sacrificing control.
[833.82 → 835.20] Deployment is easy.
[835.34 → 838.22] Pipelines are live API endpoints.
[838.54 → 845.98] They eliminate the need for constant code redeployment and debugging by deploying complex AI pipelines as API endpoints.
[846.42 → 848.50] Team collaboration is easy too.
[848.50 → 856.42] Plum's declarative node-based editor enables you to build quickly while empowering non-technical roles to iterate on what you've done without breaking it.
[856.80 → 866.92] You can build advanced AI features, get structured output every time, transform data and leverage validated JSON schema to create reliable, high-quality structured output.
[867.44 → 869.06] So Plum is built for builders.
[869.50 → 874.88] Early stage product teams are using Plum to go from idea to validation in record time.
[874.88 → 877.88] To get started, go to useplum.com.
[878.62 → 882.46] That's Plum with a B as in plumber to request access today.
[882.84 → 886.96] That's U-S-E-P-L-U-M-B.com.
[887.14 → 889.08] Again, useplum.com.
[904.88 → 911.70] All righty.
[911.78 → 918.18] So as we change gears just a little bit, I had noticed a couple of interesting things.
[918.18 → 926.60] So I spend a lot of time talking to different folks in the kind of in the Fortune 500, Fortune 100 world.
[926.84 → 933.66] You know, I work at a big company, but I have a lot of friends and former colleagues at other companies and we chit-chat about these things.
[933.66 → 938.96] So something has really come up in a bunch of conversations lately for me.
[939.08 → 946.54] And I thought, wow, if I'm talking about it this much with different friends of mine, it probably is a good topic to talk about on the show.
[946.62 → 948.92] And that's an interesting observation.
[948.92 → 964.98] And that is, for those of you who are familiar with the organization Gartner, and that organization does a lot of prediction and kind of identifying different technologies and things where businesses can use them effectively.
[964.98 → 969.66] And famously, they put out the Gartner hype cycle.
[970.28 → 974.38] And what that is, is it is a life cycle for technologies.
[974.78 → 984.50] And they basically, across all technologies that they track, which is many, they put them on this hype cycle and track where they are in their life cycle.
[984.50 → 995.24] And the short version of what that is, it has a steep upward curve that looks like an ocean wave sort of that plunges down into a trough behind it.
[995.36 → 1002.48] And then it kind of comes up without so much steepness midway to kind of sustainable plateau.
[1002.48 → 1013.82] And so what they would argue is that for any given technology, there is an innovation trigger, which is this, you know, rocketing up on amount of hype associated with the technology.
[1014.30 → 1022.44] And that it gets to a peak, which they refer to as the peak of inflated expectations, where it's really high.
[1022.68 → 1027.28] Everyone's talking about it, but maybe not a lot of productive work has happened yet.
[1027.74 → 1028.46] Super cool.
[1028.46 → 1035.62] You can probably already recognize how AI might fit into this, how we've, you know, with all the things we've talked about over time.
[1035.84 → 1045.26] But then those expectations have not been met and people become frustrated with the technology, and it plunges down into what they call the trough of disillusionment.
[1045.96 → 1051.88] And that's where they kind of go, wow, I thought that thing was so great, but boy, it really didn't pan out.
[1051.96 → 1053.48] And we wasted a lot of money on it.
[1053.92 → 1057.44] And it's just not, it's just not really worked out well for us.
[1057.44 → 1064.36] But then calmer minds come along, and they say, well, wait a minute, this technology has some perfect uses.
[1064.50 → 1071.56] We just need to be a little bit more practical, pragmatic about it and not lose our heads over the hype.
[1071.68 → 1074.00] And that's called the slope of enlightenment.
[1074.00 → 1080.76] And that reaches a point that's called the plateau of productivity where we're basically for the long term.
[1080.82 → 1087.96] A technology lives out the rest of its life cycle, being a productive technology, but without all the craziness in the early hype days.
[1087.96 → 1106.22] So now that I've introduced everyone to that, that life cycle, going back to the conversation that, that I've been having repeatedly with multiple people that I had noticed that so many organizations, especially large organizations are just plowing money into generative AI with mixed results.
[1106.22 → 1113.56] Some are getting some decent results within, you know, within the context of, of it being early days in the corporate sense.
[1113.56 → 1127.14] But I noticed that after peaking and holding a peak on the hype cycle for quite a long time, generative AI is now beginning to plunge down into the trough of disillusionment.
[1127.14 → 1133.72] And what that would imply, according to Gardner, is that people are beginning to get a bit frustrated.
[1134.06 → 1145.86] And I would say that's panning out because I've noticed many articles and social media posts over the last few weeks that people have been kind of going, this isn't going to lead to generative AI.
[1146.26 → 1148.16] This isn't quite as good as we thought.
[1148.22 → 1149.14] It's not magic.
[1149.70 → 1153.32] It's all the things that you see with people being a bit frustrated with it.
[1153.32 → 1156.64] And those are increasing in the number that I've seen.
[1156.64 → 1169.04] And so it got us talking about what does that mean in a corporate sense, especially when you have a technology plunging down into the trough of disillusionment.
[1169.04 → 1177.30] And not only that, but it's a technology that has received a lion's share of funding relative to other technologies that go through the hype cycle.
[1177.54 → 1184.30] It's the coolest of the AI, you know, over the last couple of years, the coolest of the AI tools in the toolbox.
[1184.30 → 1190.88] And with corporations always lagging, they're now plowing money into it, and yet expectations are falling.
[1191.54 → 1199.68] And so not getting to the point of it will obviously find that slope of enlightenment and that plateau of productivity eventually.
[1199.68 → 1215.04] What does it mean over the next few months as we're looking at organizations that are still plowing money into generative AI, but maybe not in the most productive sense or not as productive as they could have given the dollar value that they're putting in?
[1215.60 → 1218.42] So I've asked a lot of people what they think of this.
[1218.68 → 1220.94] Daniel, what are your impressions of that?
[1221.08 → 1225.46] You know, it's an interesting place to be if you're in corporate America or corporate anywhere these days.
[1225.46 → 1232.94] I do think it's interesting, and I think that in some ways, some of these feelings are healthy.
[1233.26 → 1253.90] In particular, what I mean is I noticed earlier on, so maybe in 2023 or, you know, last fall, still talking to a lot of people with a misconception that, oh, we have somehow what's going to happen is we're going to get access to a large language model.
[1253.90 → 1258.08] Or we're going to get access to a foundation model in our company.
[1258.92 → 1264.00] And somehow that kind of equates to a solution to them.
[1264.12 → 1268.06] Like this will now be a thing that solves problems.
[1268.70 → 1273.80] And I think that, of course, is a bunch of baloney because basically a model does nothing.
[1274.08 → 1279.72] It's how you implement it, how you integrate it, how you use it that actually makes it a solution.
[1279.72 → 1297.04] And so I don't know how else to describe that other than people thinking that AI would provide a different type of solution than other technologies, which are pieces of software that people deploy within their companies.
[1297.04 → 1302.72] Right. And so some of this, I think, is really healthy in that people are realizing, oh, wait a minute.
[1303.24 → 1313.46] There's still a need to think about how we integrate a call to a large language model in the context of a larger engineering project.
[1313.46 → 1325.80] And actually, there is engineering around the edges of the integration of AI in some ways different from traditional software engineering and in a lot of ways the same.
[1325.80 → 1338.44] Whether that be hosting services or testing and evaluating outputs or versioning the way that we call these models or other things.
[1338.72 → 1343.78] There are a lot of those best practices that are still really valid from the software world.
[1343.78 → 1347.50] And so to me, it's not so much.
[1347.78 → 1355.64] And maybe this is just because I, of course, have a vested interest in the technology because I'm building with it every day.
[1355.76 → 1366.02] But I think it's not so much a disillusionment about AI functionality in the context of what people are building over the next year.
[1366.02 → 1380.84] But disillusionment around how that integration happens, whereas before it was sort of this fuzzy thing that we're going to bring AI in and somehow that's going to like to solve a bunch of problems without really an understanding of how you would actually see return around that.
[1380.84 → 1391.74] Now people are saying, well, yes, we're going to bring in LLMs, but that's going to live still in a software stack that we have engineers developing.
[1392.04 → 1395.16] And we're going to develop that on some lifecycle.
[1395.58 → 1405.14] And yeah, there's still going to be, if anything, maybe increased engineering spend because there needs to be extra engineering around these models.
[1405.14 → 1411.26] And so it is enabling efficiencies, it is enabling net new kind of features or net new products.
[1411.52 → 1416.00] But these are still products driven by software that requires engineering.
[1416.60 → 1419.54] And so that realization, I think, is a really healthy one.
[1420.08 → 1428.20] And so maybe that thing that has the disillusionment wasn't really ever a real thing that could have been gained, I guess.
[1428.64 → 1430.38] I think that's a fantastic insight.
[1430.38 → 1445.18] I think in a perfect world, if we can help people along, kind of get through their own trough of disillusionment very quickly to climb back up onto the slope of enlightenment by following that guidance is essentially what I'm getting at.
[1445.58 → 1458.34] Before diving into it, I know that over time, as I've talked to people, it reminded me of Amplified beyond what I've heard before, but of previous technologies that were supposed to solve everything.
[1458.34 → 1461.76] You know, blockchain was going to solve the world, if you recall.
[1462.36 → 1463.54] Blockchain was amazing.
[1463.86 → 1464.92] We were going to have it everywhere.
[1465.04 → 1465.90] It was going to be everything.
[1466.62 → 1475.50] And by, you know, having since reached that plateau of productivity at the end of the lifecycle, blockchain has a fantastic place in the technology world and a vibrant community.
[1475.50 → 1477.46] But it, of course, doesn't solve all things.
[1478.00 → 1483.40] And I think people need to realize that the same with these kinds of models is that they can do that.
[1483.40 → 1495.04] So I know that one of the things that I'm trying to get people to do is to get through their own trough of disillusionment quickly and start recognizing in a really productive sense how to fit it in with larger systems.
[1495.44 → 1502.16] We've always talked about it's really the software system around these models that makes it all work, that makes the value for the user.
[1502.16 → 1506.50] And even extending that, if you're not in the cloud, it's the hardware.
[1506.76 → 1513.42] If you're out on the edge, it's all about what do you have on the hardware, and how does it integrate, and how does it integrate with the systems you already have in place?
[1513.84 → 1521.76] And what special value are you expecting generative AI to bring to bear that you haven't already been trying to design and solve for?
[1521.76 → 1531.88] And so I think as people really stopped and they kind of got out of their New Year's Eve party moment, and they said, OK, I'm an engineer.
[1532.08 → 1534.54] I need to start being an engineer again and thinking about it.
[1534.54 → 1542.96] And they thought, well, maybe it doesn't solve everything like I thought, but I can identify some pretty cool things that it would help on value.
[1542.96 → 1555.86] And I'm hoping that people will start focusing on that and bring engineering, to your point, back to bear on this and solving it, but solving it in that larger ecosystem that includes the overall stack that you're in, the software.
[1556.52 → 1567.66] And since we're moving ever more out onto the edge into all the devices that we use out there beyond just our cell phones that were always ever present, that we can find some good uses.
[1567.66 → 1580.40] So maybe this is a chance for a bit of a resurgence, yes, of engineering, but also this triggers all sorts of data science-y things in my mind.
[1580.50 → 1595.28] Because as a data scientist operating in that industry for however long it was the thing, it was about choosing the right sets of data tools and models to come up with a solution.
[1595.28 → 1598.20] Or at least that's how I think a lot of people viewed it.
[1598.30 → 1614.54] And that may have been a gradient boosting machine plus a SQL database plus some sort of data pipeline and connecting that into infrastructure and eventually into products that get out into the world.
[1615.20 → 1621.90] Now, some people might view data science differently and have different views because it's sort of an ambiguous term in and of itself.
[1621.90 → 1625.88] But I see one interesting thing on the hype cycle that you were mentioning.
[1626.06 → 1640.06] There's a shorter time period that they talk about this composite AI reaching the plateau than, quote, generative AI, which is interesting to me in that I actually had to look up this term because I have no idea what that term means.
[1640.24 → 1646.34] There are actually a number of terms on the Gartner-Height cycle that I have no idea what they mean, which I wonder where they come from.
[1646.60 → 1647.42] And I'm right there with you.
[1647.48 → 1649.70] So neither one of us knows what composite AI is.
[1649.70 → 1654.48] So I'm sure that there are a few people out there that are very familiar with it and are snickering at us.
[1654.60 → 1658.18] And we welcome your education and feedback on such.
[1658.28 → 1658.94] Keep going, though.
[1659.20 → 1659.38] Yeah.
[1659.50 → 1677.56] But I looked up the term and this appears to just be like almost a term describing data science, which is just like using different types of AI or machine learning together to solve issues or create solutions, which is sort of just descriptive of data science and kind of what it was for many years.
[1677.56 → 1681.10] So I don't know that it'll be called data science.
[1681.18 → 1682.46] Maybe it's called AI engineering.
[1682.46 → 1683.10] I don't know.
[1683.10 → 1699.58] But I do think that we'll see kind of a return to this idea of composite solutions and a multifaceted way of looking at doing these things, not just with Gen AI, but that plugged in as an option into the solution mix.
[1699.58 → 1701.52] I couldn't agree more.
[1701.72 → 1708.64] Despite being an AI podcast, I know you and I are always a little bit eyes-only when it comes to all the surrounding hype.
[1708.80 → 1712.86] We try for our listeners to cut through the hype and talk about it.
[1712.96 → 1724.64] So, yeah, a return to engineering and taking advantage of some of these capabilities in a holistic system that is highly productive and gives your end users what they need is the way to the future.
[1724.64 → 1754.62] Thank you.
[1754.64 → 1784.62] Thank you.
[1784.64 → 1786.64] Thank you.
[1786.64 → 1814.62] Thank you.
[1814.64 → 1816.64] Thank you.
[1816.64 → 1817.64] Thank you.
[1817.64 → 1818.64] Thank you.
[1818.64 → 1819.64] Thank you.
[1844.64 → 1869.86] Thank you.
[1869.86 → 1880.58] Well, Chris, I have maybe a related question for you, which it's not exactly related to the hype cycle.
[1880.58 → 1888.86] But I was at my local co-working space for a fundraiser on Friday night.
[1889.36 → 1893.32] And shout out to Matchbox co-working if anyone's listening.
[1894.32 → 1895.98] But yeah, so that was fun.
[1896.08 → 1899.70] But I got into a number of AI-related conversations, as I usually do.
[1899.86 → 1920.84] And one of the things that one of the guys I was talking to mentioned was, you know, there's a lot of people talking about how this sort of wave of generative AI, this wave of AI and what people are referring to AI now as being compared to kind of like the surge of it's like the new Internet, right?
[1920.88 → 1925.28] Like when the Internet was brought about and the type of change that that created.
[1925.28 → 1934.24] And his point was sort of, well, that definitely created a kind of new market, this space that was and is the web.
[1934.74 → 1938.26] And it wasn't just about creating efficiencies.
[1938.26 → 1962.28] And his point was, it seems like most people are using AI to create efficiencies in the enterprise, whether that's, you know, helping write reports or automate certain functionalities that interns were doing before, or analyze a bunch of documents, summarize those, answer questions, get quick access to information.
[1962.28 → 1980.58] And from his standpoint, these are all kind of efficiency gains and not necessarily creating any sort of new market that would be comparable to the huge shift that happened when the web came about.
[1981.08 → 1983.40] So I was curious on your take of that.
[1983.58 → 1987.12] Maybe it's slightly related to the hype cycle stuff.
[1987.12 → 1989.28] But yeah, I think so.
[1989.66 → 1992.00] There are two different qualitative things.
[1992.16 → 1994.30] There are a lot of common traits between them.
[1994.86 → 2001.38] But because I'm slightly on the older side, I was an adult when the Internet became, you know, not when it was invented.
[2001.58 → 2005.28] That was actually was invented the same year that I was born or a year before.
[2005.84 → 2010.80] But at the point where it hit the public in a slight way, I was in college.
[2010.80 → 2014.14] And by the time it became the thing, I was well into the workplace.
[2014.14 → 2025.20] And so, you know, that qualitatively, the advent of the Internet brought about a brand-new ecosystem upon which people could do all sorts of new things.
[2025.40 → 2033.38] I would say it was like putting up is like if you're in a classroom, it was like putting up a chalkboard on the wall that people can then go draw.
[2033.74 → 2035.72] They can draw mathematical equations.
[2035.72 → 2036.66] They can doodle.
[2036.76 → 2038.14] They can do whatever they want.
[2038.14 → 2042.74] But it gave them a new medium upon which to communicate and do stuff and interact together.
[2043.44 → 2045.46] And so it was that baseline.
[2045.94 → 2046.94] AI is a bit different.
[2047.14 → 2050.78] AI is it has a similar revolutionary quality, obviously.
[2051.36 → 2059.40] But it's expanding on that connectivity and saying, how can we get you what you need faster and more intelligently?
[2059.68 → 2061.96] We know with aid along the way.
[2062.08 → 2065.86] And so it's its apples and oranges, but they're they're both in the same fruit bowl.
[2065.86 → 2067.64] A little bit of a strange analogy there.
[2068.38 → 2074.62] Yeah, it's interesting that you bring up the element of sort of creativity and communication.
[2075.18 → 2086.00] So there are probably some parallels in the sense that I would say there are many people treating this sort of AI models and what they're building with it as a very creative new.
[2086.00 → 2098.84] I don't know if you'd call it a new canvas on which they're painting, but definitely they're they're trying things that are new and interesting, maybe that haven't been done before and are very generative.
[2098.84 → 2111.64] And some of those things, even if you think about something very much on the creative side, like the UDO type of thing that is the music generator that we talked about a while back, I think you could make an argument.
[2111.90 → 2122.92] Well, that is an efficiency builder because you could make a bunch of music really quick for your YouTube videos or a bunch of music really quick for your ads or whatever you're running online.
[2122.92 → 2135.92] But I think also some people are using it as a creative element in and of itself and doing maybe new and different things or mixing things in ways that people hadn't done in the past.
[2135.92 → 2144.82] And maybe there are other examples that are better in my mind where kind of it's almost a both and type of situation.
[2145.14 → 2152.52] So I'm I'm always maybe a sucker for the third option where it's not like clear-cut on one side or the other side.
[2152.52 → 2156.80] But this third option of yes, it is about efficiency gains.
[2156.80 → 2174.30] But I think there is an element of net new things that will come out of the AI space with these models that maybe we are hard to predict right now, like they would have been hard to predict in the rise of the Web.
[2174.30 → 2179.34] Right. It was probably hard to predict what an Amazon would become.
[2179.56 → 2179.96] Agreed.
[2180.04 → 2185.78] When people were kind of goofing around and making websites to do this or that.
[2185.88 → 2187.66] Maybe it would have maybe it wouldn't have.
[2187.78 → 2197.92] But like the level at which that sort of company has shaped culture at large, not even just like commerce, but culture at large.
[2198.14 → 2202.02] You know, maybe we just don't know yet is one way to put it.
[2202.02 → 2203.82] I have a couple of thoughts on that.
[2204.30 → 2208.54] First, there is creativity in these AI models.
[2208.66 → 2211.56] And some people argue against that even today, like they may see.
[2211.90 → 2215.22] But they'll say they don't invent wholly new notions and stuff.
[2215.34 → 2219.38] They take things that are already out there and they combine them and stuff like that.
[2219.48 → 2221.18] And there may or may not be merit to that.
[2221.50 → 2226.08] But what I can do is I can compare it to myself and other humans that I know.
[2226.08 → 2235.24] And I'm an extremely creative human, but I'm creative, and I have strengths in certain areas of creativity and big weaknesses and others.
[2235.24 → 2240.92] And I've spent a lot of time trying to compare myself to these tools that I'm using in that way.
[2240.98 → 2254.20] And so I am very good at creating out of nothing a software system in my head and understanding all the right things to put in place to do it, even if it's a fairly new way of doing things.
[2254.20 → 2255.92] And that's a strength that I have.
[2256.14 → 2262.46] I'm terrible at drawing a beautiful picture or painting and getting that out, even if I can envision it in my head.
[2262.50 → 2263.12] I can't do that.
[2263.12 → 2278.12] And what it's made me realize, seeing these tools that I'm using, that is that are producing these capabilities that we're all using, all of us listening to this are using every day these days, is it's made me really question the sanctity of human creativity.
[2278.12 → 2287.22] And I think at the end of the day, I'm a big believer that everything is mathematical, whether you agree or disagree with it, that, you know, we're we're a biology.
[2287.22 → 2290.48] We're based on chemistry, which is based on physics, which is based on math.
[2290.48 → 2301.80] And that kind of science stack that I tend to think of us as whether something is silicon and producing stuff from its capability or is biological in nature.
[2302.16 → 2306.94] I spend a lot of time going, how special is what we as humans create?
[2307.06 → 2320.46] So maybe we just kind of acknowledge that we're bringing things to bear and these new tools that we're all using every day brings things to bear, and we can be more productive and capable by combining our talents and doing stuff.
[2320.48 → 2322.66] So I don't tend to be in either camp.
[2322.72 → 2328.48] I don't tend to be in the is amazing new imagination from computers.
[2328.82 → 2330.12] My God, what's the world coming to?
[2330.32 → 2332.54] And I don't tend to be in the bah humbug.
[2332.66 → 2334.66] This is just more of the same.
[2334.78 → 2338.08] I've seen this before and there's nothing magical about it.
[2338.14 → 2341.94] I'm a little bit in the middle and maybe a little bit more nuanced than that.
[2342.20 → 2343.78] It's a long way around to an answer.
[2343.86 → 2344.24] I apologize.
[2344.24 → 2346.44] Yeah, I definitely understand that.
[2346.44 → 2359.46] And I think from my own worldview and even my faith perspective, I would think of a sort of different special way in which humans exist.
[2359.46 → 2368.98] But at the same time, we have created a lot of creativity with the tools that we create and the technologies that we create.
[2369.14 → 2379.14] And I think there is something beautiful about the fact that we are acting out as creators, creating things that are creative in and of themselves.
[2379.14 → 2379.60] Right.
[2379.60 → 2387.00] And so we're we're kind of acting out the don't know how philosophical we've got on this show up to this point.
[2387.32 → 2389.74] But yeah, we can afford a moment here.
[2389.86 → 2390.48] Yeah, exactly.
[2390.62 → 2391.60] This is the end of the show.
[2391.70 → 2404.32] Yeah, I would say it's kind of a beautiful thing that we as human beings are creative, and we create things that in and of themselves could be conceived to be creative also.
[2404.32 → 2406.58] And we co-create with those things.
[2406.58 → 2408.28] I think that's that's really cool.
[2408.28 → 2412.04] And I think that's an element of what we've done with technology over time.
[2412.26 → 2423.34] And so, yeah, I think my perspective is maybe we just haven't seen what we are to co-create with this technology moving into the future and how that will shape culture.
[2423.50 → 2432.76] I think that's going to be a longer time period than maybe the one to two year Gartner hype cycle time period that we actually see.
[2432.76 → 2436.46] Yeah, this is shaping culture because people know about it now.
[2436.58 → 2444.30] But I think there's like a deeper way like people knew about the Internet at the sort of hype of the Internet coming out.
[2444.44 → 2454.48] But really how the Internet would shape culture and shape, you know, things like what social media and other things have done took a long time to realize.
[2455.22 → 2460.00] So, yeah, I think that we have to wait a little bit for that from my perspective.
[2460.74 → 2462.10] Great perspective you have there.
[2462.10 → 2469.44] And I would encourage our listeners, you know, we had a little bit of moment of finishing the show up with kind of sharing our views on this.
[2469.88 → 2479.92] But I think this is important because we're all going to see an increasing amount of AI capabilities coming into our lives for forever going forward at this point.
[2480.36 → 2481.80] Our children are grandchildren.
[2482.48 → 2484.64] The world is changing faster now than it ever has.
[2484.64 → 2494.04] So these are thoughts that I hope you're having as well, evaluating how you see yourself in this world, sharing a world with these technologies that are increasing.
[2494.04 → 2509.58] And if you haven't already, I hope you will join our Slack community where you can engage Daniel and myself directly and share some of your thoughts on how all this might work going forward with creativity and with these other topics we're having, because we'd love to hear your thoughts.
[2509.58 → 2517.62] And for what it's worth, we build these shows off of a lot of those conversations that happen in the Slack community where people are showing interest.
[2518.12 → 2520.02] So please engage us there.
[2520.46 → 2523.38] Share your thoughts, including the philosophical ones.
[2523.46 → 2524.06] Don't be shy.
[2524.44 → 2528.82] And I'm looking forward to hearing what some of you out there are thinking yourselves.
[2528.82 → 2529.70] Cool.
[2530.22 → 2538.68] Well, thanks for having the discussion, Chris, and hope you can have a good week as you enter into more fun AI work.
[2538.84 → 2539.80] Sounds good, Daniel.
[2540.14 → 2545.30] Stay cool in the hot summer weather since we don't have that AI climate control quite yet.
[2545.38 → 2545.58] Yeah.
[2545.82 → 2546.78] I'll see you next week.
[2547.02 → 2547.44] All right.
[2554.70 → 2555.82] All right.
[2555.82 → 2558.46] That is Practical AI for this week.
[2558.82 → 2560.26] Subscribe now.
[2560.48 → 2565.46] If you haven't already, head to PracticalAI.fm for all the ways.
[2565.92 → 2571.86] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2572.42 → 2577.08] Sign up today at PracticalAI.fm slash community.
[2577.68 → 2584.62] Thanks again to our partners at Fly.io, to our Beat Freakin' Residence, Break master Cylinder, and to you for listening.
[2584.98 → 2586.72] We appreciate you spending time with us.
[2587.06 → 2588.28] That's all for now.
[2588.28 → 2590.20] We'll talk to you again next time.
[2597.48 → 2597.76] Bye.
[2597.76 → 2599.54] Good.
[2601.74 → 2602.66] Bye.
[2602.72 → 2602.78] Bye.
[2602.84 → 2602.90] Bye.
[2603.66 → 2605.14] Bye.
[2605.78 → 2606.32] Bye.
[2614.82 → 2615.38] Bye.
[2615.38 → 2615.46] Bye.
[2615.98 → 2617.38] Bye.
