[0.00 → 3.08] I'm a Microsoft guy. So I remember Biz Talk. I don't know if you remember that product.
[3.18 → 8.30] It was supposed to do away with all coders. And then you encounter it, and one asymmetry
[8.30 → 12.74] in the data or one irregular use case blows the whole system up. So we have enough experience
[12.74 → 17.48] to know, look, we're giving you a tool that takes away the arduous elements of deep learning. But
[17.48 → 22.72] you still apply your creativity and understanding that gets you there a lot faster. And I think
[22.72 → 29.56] that's going to be with us for some time. Bandwidth for Changelog is provided by Vastly.
[29.56 → 35.14] Learn more at Fastly.com. We move fast and fix things here at Changelog because of Rollbar.
[35.28 → 40.70] Check them out at Rollbar.com. And we're hosted on Linde cloud servers. Head to linode.com
[40.70 → 48.16] slash Changelog. Linde makes cloud computing simple, affordable, and accessible. Whether
[48.16 → 52.40] you're working on a personal project or managing your enterprise's infrastructure, Linde has
[52.40 → 56.64] the pricing, support, and skill you need to take your ideas to the next level. We trust
[56.64 → 60.94] Linde because they keep it fast, and they keep it simple. Check them out at linode.com
[60.94 → 61.84] slash Changelog.
[69.84 → 75.56] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[75.86 → 80.96] and accessible to everyone. This is where conversations around AI, machine learning, and data science
[80.96 → 85.78] happen. Join the community and Slack with us around various topics of the show at ChangeLog.com
[85.78 → 89.48] slash community and follow us on Twitter. We're at Practical AI FM.
[95.08 → 102.34] Well, welcome to another episode of Practical AI. My name is Daniel Whiten ack. I'm a data scientist
[102.34 → 109.18] with SIL International. And normally I'm joined by my co-host Chris Benson, who is principal AI
[109.18 → 115.48] strategist at Lockheed Martin. But this week is kind of weird in a couple of respects. So Chris
[115.48 → 121.32] is out dealing with a personal thing, which I totally understand, and he'll be back next
[121.32 → 126.70] week. But also we're all just kind of, at least if you're in the US or watching on from afar,
[126.82 → 133.74] it's kind of a crazy time right now. Yeah, there's a lot of people struggling and suffering and
[133.74 → 140.08] experiencing a lot of hardship, whether that be from the sort of police brutality that's happened,
[140.08 → 147.10] or the looting, or even just the ongoing struggle from COVID. It's definitely a hard time right now.
[147.50 → 154.04] But there are important issues to talk about are actually not unrelated to this. We know as AI
[154.04 → 160.90] practitioners that a lot of how our models behave is driven by the data that we put in. And because
[160.90 → 167.78] we're often gathering data from a biased world, then often our models end up being biased and not fair.
[167.78 → 175.72] And so this is a real problem. So people like to talk about the sort of sentient problem or
[175.72 → 181.06] singularity that they're afraid of AI taking over the world in that way. But I think in our immediate
[181.06 → 187.78] terms, you know, these sorts of problems of bias and fairness and understanding why that happens,
[187.84 → 194.98] the explainability around our AI models is even more so important because of the things that are
[194.98 → 200.32] happening in our world and because of all of these things that are driving the data that we're using.
[200.56 → 206.56] So today, I'm really excited to have an expert on this topic with us. And not only an expert on the
[206.56 → 212.94] topic of explainability and building things related to explainability, but also the CEO of a really
[212.94 → 218.96] innovative company doing a bunch of great things. The company is Darwin AI. And today I have with me
[218.96 → 222.98] Sheldon Fernandez, who's CEO of Darwin AI. Welcome, Sheldon.
[222.98 → 225.68] Thank you for having me today. Appreciate it.
[225.68 → 230.72] Yeah, definitely. So as we get started into this topic, I'd love to just hear a little bit about
[230.72 → 237.78] your background and how you got into the AI world and eventually found your way into Darwin AI.
[238.18 → 243.30] Yeah, it's quite the interesting story. So I went to the University of Waterloo here in Canada. So I'm
[243.30 → 248.46] right now speaking to you from Toronto, Canada, home of the NBA champion Toronto Raptors, and will be
[248.46 → 250.14] champions for a little bit longer, it looks like.
[250.14 → 253.88] And Waterloo is kind of a tech hub, right?
[254.06 → 254.30] Correct.
[254.50 → 260.66] So for Americans who might not be like, a little ignorant of Canadian things, that's like a big
[260.66 → 261.30] tech hub, right?
[261.56 → 266.04] Correct. It's kind of like the MIT of the United States. So it's a very engineering focused,
[266.16 → 270.74] heavy school. And a lot of our tech innovation comes from Waterloo. There's U of T, there's Montreal,
[270.74 → 273.76] but like, of course, I'm going to be biased and say Waterloo is by far the best.
[273.88 → 274.28] Of course.
[274.28 → 280.38] So I went to Waterloo, did computer engineering, started a consulting company, enterprise software
[280.38 → 287.04] consulting company in 2001, and grew that to a size of 700. And we were acquired in 2017 by a
[287.04 → 292.94] company called Average. They're co-owned by Microsoft and Accenture. So my job, and I was the CTO of that
[292.94 → 298.50] company, was to bring emerging technologies to the enterprise about two or three years before the
[298.50 → 304.46] enterprise was ready to use them. And so when DeepMind accomplished what they did with Alfaro,
[304.58 → 309.80] you might remember that in 2016, I remember really paying attention to that and thinking this was
[309.80 → 315.00] significant. I had followed computer chess, if you remember, for many years. And, you know,
[315.02 → 320.60] it was a very sad day for me when Deep Blue beat Kasparov. I was very downcast and my mom thought it
[320.60 → 325.70] was a girl. And when she found out it was that Deep Blue beat Kasparov, I think she was half proud,
[325.70 → 330.40] but also half worried that she'd never get grandkids, right? Right, right. But the thing with Go,
[330.58 → 336.52] the game of Go wasn't supposed to be conquered by machines till 2030 or even 2050. So when DeepMind
[336.52 → 340.50] did that, I remember thinking, this is significant, and how did they do this? And then really getting
[340.50 → 345.76] into deep learning and doing the Jeffrey Hinton deep learning course. And then when we got acquired,
[345.98 → 350.78] I had been speaking about deep learning. A mutual friend said, go have a conversation with this
[350.78 → 355.36] academic team at Waterloo. It's a special team, and you'll have just a wonderful
[355.36 → 360.64] conversation. And I did. And, you know, they just had incredible technology. And I was just
[360.64 → 365.16] supposed to advise them. I wasn't supposed to start another venture. I had just finished a 17-year
[365.16 → 369.84] journey and was going to take time off and drive my wife to work and watch The Price is Right and all
[369.84 → 373.68] the wonderful things you do when you're retired. But this team was just too special.
[374.02 → 374.56] Not to be.
[374.88 → 375.48] Yeah, right?
[375.74 → 376.08] Yeah.
[376.36 → 380.58] So I started advising them, and then the talks got more serious. And I'm like, okay, I have to do this.
[380.58 → 385.94] And so, you know, we formalized the company in 2017 and got our venture funding in 2018.
[386.28 → 389.30] And four months after that, my wife got pregnant with our first child.
[389.62 → 390.30] Oh, wow.
[390.42 → 393.10] So actually, I have two startups. I've got an artificial intelligence startup and a
[393.10 → 394.40] biological intelligence startup.
[394.72 → 396.96] Right. Both on the same sort of timeline.
[397.14 → 401.04] Exactly. And they're both magical and exhausting in equal measure, but in different ways.
[401.66 → 401.92] Yeah.
[401.92 → 406.58] And so, yeah, it's just been an incredible ride. And, you know, our chief scientist, Professor
[406.58 → 411.26] Alexander Wong, is Canada's research chair in artificial intelligence. So this team just has
[411.26 → 417.18] an incredible amount of scholarship and innovation behind them. And so to work with them to take the
[417.18 → 423.36] product to market has just been incredibly exciting, especially given the use cases around AI and so
[423.36 → 428.38] forth. So that's a quick journey. And then very quickly, although I did an engineering degree, I took
[428.38 → 431.82] some time off in my previous venture. I did a master's degree in theology.
[432.22 → 433.16] Oh, awesome.
[433.26 → 436.98] Which was just out of interest. And somehow that's significant now because of the ethics
[436.98 → 441.40] and the way we think about AI. So just a fascinating combination of things.
[441.68 → 447.10] Well, there is a number of interesting groups kind of exploring that connection. I know there's a group
[447.10 → 453.16] in Seattle. Also, I work for a faith-based non-value of human life or whether it's like the sort of
[453.16 → 457.24] things that we started talking about with bias and fairness and all. Yeah.
[457.24 → 462.14] Yeah. It's interesting to have those conversations. So interesting to hear that background as well.
[462.66 → 463.38] Yeah, for sure.
[463.74 → 470.06] As I was looking through the Darwin AI website and some of your work, I'll link to your website
[470.06 → 474.62] in our show notes. But I was looking specifically through the information about the platform,
[474.62 → 479.80] but also this page you have about research. And it seemed like there were a few kind of themes
[479.80 → 488.66] popping out that were really focus areas. One of those being kind of edge computing and running AI at the edge.
[488.74 → 497.98] So I see things like edge signet, which is a compact network for segmentation, edge speech net for speech recognition at the edge.
[497.98 → 506.66] I also saw a theme of generative machines and generating networks in some way. And then, of course,
[506.78 → 512.10] what we talked about a little bit at the beginning, which was related to explainability. So I was wondering
[512.10 → 518.06] if you could kind of give a little background on how those themes came up and maybe starting with the
[518.06 → 519.76] edge case. Yeah.
[520.08 → 526.64] Why are people concerned about AI at the edge now? Why did that seem like a sort of direction you wanted
[526.64 → 531.54] to put some focus into? Yeah. So let me bring this together and talk about how the core IP was formed,
[531.60 → 534.86] because it kind of informs those three areas, right? Yeah, that'd be great.
[535.14 → 541.30] So our academics have been working with deep learning for about a decade, right? So well before it even
[541.30 → 545.90] entered the consciousness of the enterprise, our academics knew what this was. They were familiar
[545.90 → 551.38] with the machinery, and they were actually doing it for their own research. And they found it to be
[551.38 → 558.38] terribly difficult to develop deep learning neural networks. And they said, look, as academics,
[558.38 → 564.12] this is difficult. We can only imagine how hard this is going to be when non-academics encounter this.
[564.80 → 571.70] And was that difficulty mostly related to like computational infrastructure difficulty? Or was it
[571.70 → 579.92] like the sort of complication around the tooling or sort of the theory behind like what's best to do when?
[579.92 → 585.16] Or what was the difficulty mainly focused around? So there were three difficulties, right? Yeah.
[585.36 → 591.02] The first was they said you need an incredible level of skill to develop these things. The tool sets
[591.02 → 596.86] are immature, but the mathematical background you need is significant and a barrier. The second, as you say,
[596.92 → 603.32] is the computational overhead in running these networks. So our professor often jokes, he originally did
[603.32 → 610.32] this work for some of his scholarship and he didn't have the funding to pay for hundreds of thousands
[610.32 → 616.66] of dollars in Azure or GCP. So he had to invent a technique to make it quicker. And then the third
[616.66 → 622.74] was it was so painstaking to do this because you had no understanding of how these networks came to
[622.74 → 626.58] this conclusion. So it was like debugging a program without the source code, right? Right, right.
[626.58 → 631.32] So those were the three problems they encountered. So they invented scholarship initially for their
[631.32 → 638.80] own purposes to address those problems. To scratch their own itch, essentially. Exactly. And so they
[638.80 → 646.82] termed it generative synthesis. And the way it works is they use other machine learning techniques to probe
[646.82 → 651.78] and understand a neural net. They develop a very sophisticated mathematical understanding of the neural
[651.78 → 657.24] network. And then they use a generative approach to generate an entirely new family of neural nets
[657.24 → 662.16] that is a lot more compact than the original, as good as the original and can be explained, right?
[662.82 → 668.90] Yeah. So as you're kind of describing that, I'm starting to get like vibes of like some of the
[668.90 → 674.82] meta learning, auto ML sort of things. And I know there's a lot of people interested in this. This seems like
[674.82 → 680.94] a sort of unique flavour of it, I guess, at least. Do you see those as kind of these generative
[680.94 → 687.58] techniques that you're talking about and like stuff that people might call auto ML or meta learning?
[687.82 → 691.74] Do you see those as in the same family or? I'd say they're in the same family. They're
[691.74 → 697.88] analogous to what we do, but different, right? So auto ML does a, you know, a search across a vast
[697.88 → 703.66] search space and gives you something that it thinks is appropriate. Which in itself is computationally
[703.66 → 707.98] difficult. Exactly, right? So Google will give it to you for free, but you got to do it in GCP and
[707.98 → 713.10] that's where they get you, right? Yeah. It's not free. Whereas we will look at your data and then
[713.10 → 717.68] synthesize a new network from scratch. It's a lot more granular in terms of how we do it, but it is
[717.68 → 722.88] like conceptually similar. And so, yeah, that's the process that these guys invented. And then of course,
[722.88 → 728.72] we asked when we started the business, okay, what's the commercial potential? Like,
[728.76 → 732.46] what do you do with this? And one of the first ones, and this addresses your first question,
[732.46 → 738.82] was the edge-based scenario, right? What do you do when you need to deploy deep learning to a GPU or
[738.82 → 743.56] CPU? You don't have, you know, three or four servers to run it. And so that was kind of the
[743.56 → 749.30] first place and crevice that we found when we started thinking about this tech. Yeah. And what
[749.30 → 756.18] have you seen now that you've kind of explored that space a bit, are working with clients and people
[756.18 → 762.04] that are doing things at the edge, what do you see as the sort of real world driving factor of
[762.04 → 767.04] people wanting to deploy AI at the edge? Because from my perspective, I hear different things. I hear
[767.04 → 772.32] like on the one side, like privacy is the main issue, which I could definitely, you know, see that if
[772.32 → 779.88] data is not leaving the device. Yeah. But then there's also like, you know, your device and maybe
[779.88 → 784.24] you're running at a farm, or maybe you're running at a factory where the connectivity is not that great.
[784.24 → 789.56] So it's a connectivity to the cloud thing or maybe, and then I hear like a third set of things,
[789.60 → 794.80] which is like latency, right? So you got like your, your algorithm at the edge, and it's really fast
[794.80 → 799.00] and you don't have to like to wait for things to come back from the cloud or wherever. So from your
[799.00 → 804.58] perspective with clients, what are you seeing as sort of the driving factor there? So it depends on the
[804.58 → 811.68] vertical is what I would say, right? So when you're talking autonomous vehicles or aerospace or defence,
[811.68 → 817.46] they can't afford a trip to the round server. One, because of latency reasons. If a car needs to
[817.46 → 822.02] make a decision or a drone needs to make a decision in milliseconds, you can't depend on that round trip.
[822.16 → 827.08] And they, so they have to do things at the edge. So that's the predominant, you know, motivation that
[827.08 → 833.66] I see in those verticals. In consumer electronics and health, privacy is probably the more predominant
[833.66 → 838.62] factor, right? If you have a watch and that watch is using deep learning to do some kind of analysis
[838.62 → 845.16] on your heartbeat or detect COVID or whatever it is, you know, you as a consumer don't want that
[845.16 → 850.50] data shared with some central location that is going to aggregate and monetize that data. And so
[850.50 → 855.52] in that situation, privacy is the motivating factor to do it entirely on the edge. So it does differ
[855.52 → 861.28] depending on the vertical that you're dealing with. Yeah. Interesting. And just to get a sense,
[861.94 → 867.14] if we're talking, and this is another, maybe a point of confusion that I see a lot of times is like,
[867.14 → 872.22] when we're talking about AI at the edge, what is the edge? Is the edge, you know, a mobile device?
[872.22 → 879.50] Is it a Raspberry Pi with a camera in your house? Is it like a legit computer, but it's like at the
[879.50 → 885.34] edge in a manufacturing place? So what are you seeing trends that way? I know there's a lot of,
[885.64 → 892.60] even Nvidia came out with their new architecture. They have like the edge specific card that they're
[892.60 → 897.86] talking about. So yeah. And maybe what do you see as the trend of the focus in the future? Or maybe
[897.86 → 903.34] it depends on the vertical again. Yeah, it's a great question. I mean, now I think we use the edge
[903.34 → 910.62] colloquially to describe a scenario where all the processing is done on device, whatever that might
[910.62 → 917.10] mean, with no processing done in the cloud, right? And so that could be a super powerful GPU
[917.10 → 922.48] in a car. One of the autonomous trucking companies, I know they have eight GPUs in the truck,
[922.70 → 927.28] right? And so it's that edge. I mean, there's more compute power there than Deep Blue had in 1997.
[927.70 → 931.30] Yeah. Or that I ever use for training. Or that you ever use for whatever, right?
[931.82 → 938.84] So it is an evolving term. I do think we generally mean on some kind of device or something that is
[938.84 → 945.34] autonomous and self-contained and is not being done on the server, right? So a satellite,
[945.34 → 950.34] a drone, your hand, not a computer in the traditional sense is the way we think of it.
[951.10 → 957.70] Gotcha. And in these cases, what is the biggest concern or hurdle when you're getting to the edge?
[957.74 → 964.74] So you talk about like compact networks, you know, obviously for a thing that is like lower power,
[965.22 → 971.38] you know if we're thinking about like a small computer or like a small, like smart camera or
[971.38 → 975.10] something like that, that's going to be low power. It's not going to have that much power in storage
[975.10 → 981.48] space and RAM and all of that stuff. So is the compactness, is it dual purpose, both for the
[981.76 → 987.52] like getting it on the device and the efficiency, or what's the blocker there?
[988.14 → 989.70] So again, it depends on vertical.
[989.70 → 990.46] Yeah.
[990.86 → 998.28] In the case of, for example, defence, they have pretty powerful, you know, devices already that
[998.28 → 1003.16] are outfitted on, on whatever it is they're trying to do. So it's efficiency on those devices. How
[1003.16 → 1008.08] many concurrent systems can I run with this hardware that I've already agreed is going to be on the
[1008.08 → 1014.06] device in autonomous vehicles? It's, I need my perception network to recognize the scene in front of
[1014.06 → 1022.10] me in 10 milliseconds. And I therefore needed to be really fast on this hardware, right? With
[1022.10 → 1027.14] consumer electronics, it's a bit different. It's look, accuracy is important, but it's not as
[1027.14 → 1033.28] mission-critical as, you know, finding a child in a, in a scene when a car is driving, right? You know,
[1033.30 → 1038.64] when you're talking to Siri, Hey, you get your last name wrong. Okay. Just re-say it again. In that case,
[1038.64 → 1044.44] its performance accuracy on the device is, is usually the predominant factor. So again,
[1044.48 → 1046.72] it differs, right? Depending on your use case.
[1053.98 → 1060.12] I'm Jared Santo, Go Times producer and a loyal listener of the show. This is the podcast for
[1060.12 → 1066.08] diverse discussions from around the Go community. Go Times panel hosts special guests like Kelsey
[1066.08 → 1072.78] Hightower. And sometimes you can leverage a cloud provider and make margins on top. That's just
[1072.78 → 1077.70] good business. But when we're at the helm making the decision, we're like, yo, forget good business.
[1078.30 → 1082.50] I'm about to deploy Kafka to process 25 messages a year.
[1083.58 → 1085.24] It's nerd pride, right?
[1085.98 → 1088.50] Picks the brains of the Go team at Google.
[1089.04 → 1092.80] You don't get a good design by just grabbing features from other languages and gluing them
[1092.80 → 1097.90] together. Instead, we tried to build a coherent model for the language where all the pieces worked
[1097.90 → 1098.62] in concert.
[1099.50 → 1102.26] Shares their expertise from years in the industry.
[1102.80 → 1106.26] Don't expect to get it right from the start. You'll almost definitely get it wrong. You'll
[1106.26 → 1109.74] almost definitely have to go back and change some things. So yeah, I think it goes back to what
[1109.74 → 1113.38] Peter said at the start, which is just made your code, write your code in a way that is easy to
[1113.38 → 1115.92] change. And then just don't be afraid to change it.
[1116.18 → 1118.86] And has an absolute riot along the way.
[1118.86 → 1123.22] Yeah, you know that little small voice in your head that tells you not to say things?
[1123.92 → 1126.70] What is that? How do you get one?
[1128.34 → 1129.24] You want one of those?
[1129.26 → 1130.52] Is it like an in-app purchase?
[1131.20 → 1136.84] It is go time. Please select a recent episode, give it a listen and subscribe today.
[1137.28 → 1138.48] We'd love to have you with us.
[1148.86 → 1156.80] Okay, so I would love to maybe dive into this generative model technology a little bit more.
[1156.88 → 1161.80] You mentioned that there's this sort of, I think what you call an inquisitor model that
[1161.80 → 1168.00] kind of studies something. I'm not sure if I'm clear, you know, exactly the process that
[1168.00 → 1173.06] that goes through. So I guess from a practical perspective, when we're talking about this,
[1173.06 → 1181.24] is this a case where like, I still am using like the same types of models, like I have a
[1181.24 → 1186.82] convolutional net, or I have a recurrent neural network or whatever it is. And I have another
[1186.82 → 1191.28] model that's performing this function? Or is everything happening together in the same sort
[1191.28 → 1193.02] of different model of some type?
[1193.84 → 1198.34] Right. So I mean, it's happening underneath the hood with this technology that uses this
[1198.34 → 1204.00] inquisitor generator pair. You're giving it a neural network, and you're getting a number
[1204.00 → 1209.78] of neural networks generated that are more compact and work against your data with usually
[1209.78 → 1211.52] the same accuracy and are faster.
[1211.80 → 1211.98] Gotcha.
[1212.16 → 1216.30] So like the internals of how it works, it's interesting to academics. And we've issued papers
[1216.30 → 1221.22] on this without giving away the core IP. But really, you're giving me a neural network,
[1221.22 → 1226.08] which is a graph, and you're getting a much more compact graph as an output. And then our platform
[1226.08 → 1228.20] will provide the explainability and so forth. Yeah.
[1228.70 → 1233.72] Gotcha. It would still be up to, let's say if I'm an AI practitioner, I'm using this type of
[1233.72 → 1240.22] technology, it may still be up to me to determine like, hey, here's a computer vision problem.
[1240.66 → 1247.52] I'm going to train a convolutional neural network on this data. But then afterwards, I'm going to
[1247.52 → 1253.12] provide it to the system and get a better architecture out. Is it kind of two stage like
[1253.12 → 1254.94] that? Or can you do like everything in one shot?
[1254.94 → 1261.82] So you can do it in one shot. You can choose a popular public reference model. We're adding this
[1261.82 → 1265.54] feature to the platform. You can say, look, I have a computer vision problem. I don't know what
[1265.54 → 1270.28] the best thing is. Is it Inception? Is it Reset? And we will take a public model and produce a really
[1270.28 → 1275.50] optimized version for you against your data. Or if you're a more intermediate or advanced user,
[1275.62 → 1279.36] you might already have a network. You might have already trained it, done all that pre-work.
[1279.36 → 1282.38] And you're just going to give that to the platform and say, give me the best version
[1282.38 → 1286.14] of this against my data. So it can work in either way, depending on where you are
[1286.14 → 1287.58] in the process. Yeah.
[1288.08 → 1294.02] Yeah. Personally, I kind of like this way of thinking about it. Because oftentimes when I talk to people
[1294.02 → 1300.32] about auto ML or meta learning or something like that, it seems like the end goal of where people
[1300.32 → 1306.94] want to get is like, I just have data and then like whatever sophisticated system I have figures
[1306.94 → 1308.76] out everything for me. Yeah.
[1309.18 → 1315.96] Maybe a possibility in certain cases that have been very well studied. But I also know just from my own
[1315.96 → 1322.92] experience that every use case I come up with, it's like weird in some way that just doesn't match
[1322.92 → 1323.74] like something.
[1323.74 → 1327.98] That's our big thing. Like we are proponents of human machine collaboration.
[1328.38 → 1328.54] Yeah.
[1328.70 → 1337.58] Right. You need a human in the loop to couple the laborious intelligence of AI with your own
[1337.58 → 1342.16] intuition as a human being. And that's not going away anytime soon. Right. I mean, how often
[1342.16 → 1348.50] I've been in the technology field for 25 years. So many times I've heard you, you don't ever have to
[1348.50 → 1352.48] code again. Right. There's all these two. And then like software engineers are going to automate
[1352.48 → 1357.52] away software engineers. Right. And like you hear that, and you roll your eyes because you've seen
[1357.52 → 1361.88] it so many times. You know, I'm a Microsoft guy. So I remember Biz Talk. I don't know if you remember
[1361.88 → 1367.30] that product was supposed to do away with all coders. And like, you know, then you encounter it and like
[1367.30 → 1372.22] one asymmetry in the data or one irregular use case blows the whole system up. So we have enough
[1372.22 → 1377.02] experience to know, look, we're giving you a tool that takes away the arduous elements of deep
[1377.02 → 1382.38] learning, but you still apply your creativity and understanding that gets you there a lot faster.
[1382.48 → 1387.60] And like, I think that's going to be with us for some time. Yeah. Do you think that I know one of
[1387.60 → 1392.66] the things I forget where I saw this, I think maybe it was at a TensorFlow dev summit when they're
[1392.66 → 1400.24] talking about AutoML? Okay. That one of the things that they saw as interesting in this process is not
[1400.24 → 1406.20] so much automating away everything, but just learning new architectures that they wouldn't have guessed
[1406.20 → 1411.16] prior. Right. Is that something that you found in doing this different? It's a different approach,
[1411.16 → 1417.16] but you are still generating sort of new graphs. Like you say, in looking at those new graphs and
[1417.16 → 1422.62] those new architectures have surprising things come out from that in terms of like what's actually
[1422.62 → 1428.36] needed for to solve certain problems or? That's a great question. And one I would have to ask are
[1428.36 → 1433.58] like deep researchers. Yeah. Do they look at the new architecture and does that give them an idea?
[1433.58 → 1438.92] The fact of the matter is like very few people are designing networks from the ground up.
[1439.36 → 1442.98] Yeah. Right. It's like, you know, like the big five basically do it because they've got the
[1442.98 → 1447.78] intellectual horsepower to do it. Now where we do have insights though, and maybe we'll get to this,
[1447.80 → 1451.90] is the explainability piece of why certain things are being made. Like that is intriguing.
[1452.14 → 1455.70] And that teaches you think that just never would have occurred to you before.
[1455.70 → 1463.06] Yeah. So, um, I totally agree with you. I, I often, when I teach classes, I say like most of
[1463.06 → 1469.98] AI and practice is not sort of like drawing networks on the chalkboard and like starting
[1469.98 → 1475.68] with a blank chalkboard and then going, it's more like cooking in the sense that you get a recipe
[1475.68 → 1481.08] and then you have to bring your ingredients to it, your data to it. And you might have to change the
[1481.08 → 1485.42] recipe a bit because you don't have these ingredients or those. That's a great analogy. I'm going to steal that.
[1485.92 → 1489.36] Okay. Please do. I like that a lot, but I will give you credit when I use it. Yeah.
[1489.44 → 1494.02] It sounds good. Yeah. I, I, at least, uh, I can contribute something to the AI community.
[1494.36 → 1498.66] Exactly. Since we've kind of got there naturally, let's talk a bit more about the
[1498.66 → 1504.58] explainability piece, and maybe we can actually start at a, at a higher level there as well and talk about
[1504.58 → 1510.56] like, um, let's say in the absence of the things that, that you're doing and your team is doing,
[1510.56 → 1514.44] and actually, you know, many other teams are exploring explainability things.
[1514.44 → 1521.72] For those that are maybe newer to AI or are in a company and exploring AI and are concerned about
[1521.72 → 1530.80] it, what are the main sort of reasons why we need explainability? And then at what level do we need
[1530.80 → 1535.64] explainability? Like, you know, cause like, for example, with GDPR, when people are talking about,
[1535.72 → 1539.84] Oh, you give an explanation for how, how you process people's data. Well,
[1539.84 → 1545.52] like, I don't always know why my network did something and I think it would be infinitely
[1545.52 → 1552.22] hard to describe everything. So what are the main challenges and what expectations can we have
[1552.22 → 1558.62] for explaining? Okay. So great question. So first, the fundamental problem with machine learning
[1558.62 → 1562.70] and deep learning is you are essentially saying to these systems, here's a bunch of data,
[1562.70 → 1568.50] data, you infer your own rules as to how you're going to make a decision against this data.
[1568.88 → 1573.10] And all I care about is the results, right? And the reason machine learning and, you know,
[1573.10 → 1578.66] this is so powerful is it is great at, you know, characterizing situations where the rules cannot be
[1578.66 → 1583.74] codified in human terms. And that's why it's great. And the example I often give is, you know,
[1584.06 → 1589.00] giving a neural network, a picture of something of a lion or a tiger and saying, Hey, classify this,
[1589.00 → 1593.94] you know, and this was a profoundly difficult problem in computer graphics before neural networks,
[1594.12 → 1599.98] something my son can do now at 18 months was impossible. Right. So it's wonderful that we can
[1599.98 → 1604.08] do that. But the explainability problem exists because we don't know how the neural network
[1604.08 → 1610.64] is orienting itself internally with its weights and so forth to reach that conclusion. Right. Yeah.
[1611.02 → 1617.52] And so the problem with explainability is if you don't understand how a decision is being made,
[1617.52 → 1622.22] you don't understand where it will fail. And if you don't understand where it'll fail,
[1622.34 → 1626.48] there are all these edge cases that are lurking in the network with potentially catastrophic
[1626.48 → 1630.72] consequences. So very practical example I can give you in the early days of Darwin,
[1631.04 → 1636.24] we worked with an autonomous vehicle company. And I've used this example in my writing a little bit
[1636.24 → 1644.08] where their car, the perception network in their car or the AI in their car would turn left with
[1644.08 → 1648.50] increasing statistical frequency when the colour of the sky was a certain shade of purple.
[1649.90 → 1655.46] Right. So just pause on that. Like you and I know that the colour of the sky never influences the
[1655.46 → 1659.04] way you turn. I mean, maybe there's a volcano in the right or something. Right. Yeah. But that was
[1659.04 → 1663.16] mystifying to them. And so without explainability, they couldn't understand what are the drivers
[1663.16 → 1669.18] here? It's what we call a nonsensical correlation. And so we were able to help them debug that they had
[1669.18 → 1674.84] done the training for the turning scenario in the Nevada desert when the colour of the sky was the
[1674.84 → 1679.48] shade of purple. And that was the correlation the car had made. Right. But in order to understand
[1679.48 → 1686.06] those nonsensical correlations, in order to identify the edge cases, you need to have some
[1686.06 → 1691.90] insight into why the neural network is doing what it's doing. And so that is why explainability is
[1691.90 → 1698.08] so important, is to make more robust networks and give the data scientist and the deep learning
[1698.08 → 1705.12] developer tools to make those more robust networks. Yeah, I think you really, uh, summarize that well.
[1705.16 → 1712.98] And I think some of this is like, it's beginning to be on my mind so much more as I develop. I know
[1712.98 → 1719.42] just last week, just to shout out one of my favourite podcasts, which is the NLP highlights podcast from
[1719.42 → 1726.64] Allen Institute of AI. His name's Marco Rubio on there talking, he's from Microsoft. And he was talking
[1726.64 → 1732.74] about behavioural testing of NLP models. And he basically used a bunch of commercially available
[1732.74 → 1738.50] systems in his paper, like from Microsoft and Google and Amazon that they sell, for example,
[1738.50 → 1745.30] for like sentiment analysis. And he did some very kind of like, so what he called minimum functionality
[1745.30 → 1750.48] tests that were not based on like a training set that they use to train the model, but just were like
[1750.48 → 1756.14] the minimum functionality you'd expect from a sentiment analysis. Like, can it get, I don't like food.
[1756.14 → 1762.22] Right. The sentiment of that. Yeah. But then what he did is he made perturbations on that, like
[1762.22 → 1769.12] changing, you know, I don't like burritos to, I don't like oranges. So like simple perturbations
[1769.12 → 1774.80] that should not change the sentiment from like negative to positive. Right. Or changing like,
[1775.12 → 1781.74] I like the U S to, I like Turkey. Right. And then seeing if it changed. And he actually found that these
[1781.74 → 1786.54] like huge percentage of failures in these commercially available systems for these
[1786.54 → 1792.58] kind of minimum functionality tests. Right. And some of those things were tied to the way things
[1792.58 → 1798.86] are represented in the data. Like Turkey was represented in a very negative light in a lot of
[1798.86 → 1804.62] the data that was trained on this model. So I totally agree with you in that case, like this thing's
[1804.62 → 1810.06] already deployed. Right. And you have this existing problem in the system. Yeah. And you don't know it
[1810.06 → 1814.70] until you hit it. Yeah. Whereas you're saying like, if you're developing, you should ideally
[1814.70 → 1820.30] know where you're going to maybe hit some of those pitfalls, or at least understand why you hit those.
[1820.36 → 1825.84] So you can make the system better. And so sometimes the system will get it right, but for the wrong
[1825.84 → 1831.68] reasons. Right. So a very popular example I've heard is there was a neural network that was trained to
[1831.68 → 1837.90] detect horses, recognize horses, and it performed admirably well. But what they didn't realize was
[1837.90 → 1843.74] apparently, this was news to me, many professional pictures of horses are copyrighted. So it was
[1843.74 → 1848.24] actually looking at the copyright symbol at the bottom of the picture, and that was a tell it.
[1848.36 → 1854.70] But of course, so what you do then is you say, oh, okay, let's remove the copyright from the picture
[1854.70 → 1860.16] and let it organically or naturally look at the features of a horse to detect things. So that is what
[1860.16 → 1868.08] you're trying to do is align how it's triggering on data for decision-making with your own intuition
[1868.08 → 1875.92] that yes, this makes sense. Right. Now, sometimes you will actually learn from explainability. The
[1875.92 → 1880.58] neural network will teach you something about explainability. So our professor does a lot of
[1880.58 → 1885.16] work with neural network and detection of disease. And so actually, we've been in the news because when
[1885.16 → 1889.42] when corona became a serious thing here in Canada, we released an open source network called COVID net
[1889.42 → 1896.02] that detects corona using chest x-rays. But his previous work was detecting lung cancer with CT scans.
[1896.72 → 1901.12] And we show this example where the neural network was looking at the walls of the lung,
[1901.62 → 1905.50] which had never occurred to radiologists, apparently. I'm probably oversimplifying a little.
[1906.18 → 1911.88] But they actually started looking at them thinking, huh, what maybe here can we learn from what the
[1911.88 → 1915.34] neural network is looking at? So explainability. That's fascinating. Yeah. So there's a
[1915.34 → 1919.82] second benefit in that sometimes, not often, but occasionally, it will actually teach the subject
[1919.82 → 1923.64] matter expert about a new way of thinking about the domain.
[1931.64 → 1937.32] We deserve a better internet and the Brave team has the recipe for bringing it to us. Start with
[1937.32 → 1941.86] Google Chrome, keep the extensions, the dev tools, and the rendering engine that make Chrome great,
[1941.86 → 1946.64] rip out the Google bits, we don't need them, mix in ad and tracker blocking by default,
[1946.90 → 1951.92] quick access to the Tor network for true private browsing, and an opt-in reward system so you can
[1951.92 → 1956.94] get paid to view privacy-respecting ads. Then turn around and use those rewards to support your
[1956.94 → 1961.30] favourite web creators like us. Download Brave today using the link in the show notes and give
[1961.30 → 1963.20] tipping a try on changelog.com.
[1971.86 → 1980.04] So as we're thinking about this explainability piece, I'm kind of curious, we've kind of motivated,
[1980.20 → 1985.32] I guess, why explainability and some of the pitfalls that people can fall into, and also this sort of
[1985.32 → 1991.88] dual benefit of also learning in some cases from explainability. But I'm curious, like, from a
[1991.88 → 1996.86] practical perspective, as I'm using this system, and I'm learning about my network, what is this sort of
[1996.86 → 2004.62] range of things that I can learn since, you know, there could be so many different types of, like,
[2004.78 → 2011.40] features that could be contributing to something. So, like, when I'm using this system, what sort of
[2011.40 → 2016.88] feedback am I getting? Is it like, you know, these portions of the network are doing something weird
[2016.88 → 2021.74] or interesting, or is it more having to do with the data? Like this, like you say, the segment of the
[2021.74 → 2026.22] data is important for this prediction, or what's the sort of range of things?
[2026.66 → 2032.44] Yeah, it's a great question. So we really asked, how do we surface explainable insights
[2032.44 → 2039.54] that are most useful to developers? And what we saw was very few of them really go down to the
[2039.54 → 2045.26] architectural level and tweak individual weights and so forth. It happens, but, like, in a very small
[2045.26 → 2050.86] minority of cases, most of them want explainability against data. Why is the network doing what it's doing
[2050.86 → 2055.40] against this data set or this family of data? So that's what we surface in the platform, right?
[2055.70 → 2059.44] You know, when we detected a lion being a lion, what were we looking at predominantly?
[2059.88 → 2063.94] When the network got it wrong and different from the human labeler, what did it get wrong?
[2064.44 → 2071.08] When you remove the predominant, you know, inputs that the our explainability algorithm detects
[2071.08 → 2075.28] are important, when you remove those, how does the prediction change? So that's kind of the
[2075.28 → 2080.70] data that we surface that we find really accelerates the deep learning development process.
[2080.86 → 2087.82] Gotcha. How do you balance the sort of range of data that people are dealing with? Is it a matter of
[2087.82 → 2094.52] kind of starting to specialize in a few different types of data, like text and images, and then like
[2094.52 → 2100.48] moving on past that, it just in terms of product development, I mean, it's got to be a burden to
[2100.48 → 2106.48] sort of think about all of these weird scenarios. Yeah, so it's a great question. So right now we've,
[2106.48 → 2111.16] our explainability focuses on things you can represent visually, object detection, object
[2111.16 → 2118.38] classification. Your question's a good one. How do you surface explainability for natural language
[2118.38 → 2122.84] translation or something that's inherently non-visual? So we're doing the visual stuff first
[2122.84 → 2126.60] because it's easier to surface. And then eventually we'll get to some of the other stuff. Yeah.
[2126.60 → 2134.54] Yeah. I know that there are some interesting attempts out there. Actually, we had a guy on the podcast who
[2134.54 → 2142.46] was talking about recurrent units in a neural network and how those behave in terms of the memory or what
[2142.46 → 2148.54] they pay attention to previously or forward in a text sequence and visualizing that sort of thing.
[2148.74 → 2153.46] And that was fascinating. I'll link that one in the show notes. So maybe there are some things that
[2153.46 → 2160.76] are possible there. I could definitely see it's, um, that in itself is a research topic almost.
[2160.90 → 2168.64] Yeah. Yeah. Yeah. That's interesting. So in terms of the system, how do you make decisions about,
[2168.64 → 2175.08] like, do you provide, and I'm kind of curious about this just from like an AI startup perspective,
[2175.08 → 2180.24] because there's a lot of people out there trying to do different things and some kind of like, well,
[2180.24 → 2186.48] you know, our system bolts onto TensorFlow or has a TensorFlow backend or PyTorch or whatever.
[2187.00 → 2187.10] Yeah.
[2187.44 → 2193.48] Are you kind of providing a self-service portal for people to do things where like the frameworks and
[2193.48 → 2198.20] that sort of thing are transparent, and they're really just kind of importing models and that
[2198.20 → 2203.60] sort of thing? Or is it a kind of augmentation to their existing workflow?
[2203.84 → 2208.90] Yeah, it's the latter. So we build on top of TensorFlow right now. You give us a TensorFlow model
[2208.90 → 2214.62] and the data. We do what we do, and then you'll get a TensorFlow output. It's not SaaS. Yeah.
[2214.84 → 2218.68] And so that was a big learning for us when we started Darwin. We wanted it to be SaaS because then
[2218.68 → 2223.40] we wouldn't have to expose anything. But the enterprise was quickly saying, we're not sharing
[2223.40 → 2228.86] our models, number one, and we're not sharing our data. So like, you know, disabuse yourself of that
[2228.86 → 2234.52] fantasy right now. So yeah. So we provide an enterprise platform that sits on top of TensorFlow.
[2234.52 → 2239.06] We're adding support for PyTorch later this year. Then, you know, that way your workflow doesn't
[2239.06 → 2243.02] have to change considerably. You just use the parts of the tool that you find are useful.
[2243.32 → 2247.98] Awesome. And how big is the team now? Is it quickly growing or what's the...
[2247.98 → 2248.96] It's about 25.
[2249.44 → 2249.66] Okay.
[2249.78 → 2254.70] So we're, you know, smaller team in Waterloo. I live in Toronto and was commuting before COVID.
[2255.22 → 2259.58] But as the commercial traction increases and people start doing it, I imagine we'll be growing in the
[2259.58 → 2265.86] months ahead. Yeah. Yeah. And I'm always curious for organizations like yours, you know, if I go to
[2265.86 → 2271.62] your research page and look at all the great things that you've submitted, or if you look at company
[2271.62 → 2277.64] like Hugging Face or others where it's still a relatively small team, but it's like there's a product
[2277.64 → 2283.78] and there's also like this great research coming out. Like, I don't know how you do it all. Is that
[2283.78 → 2290.20] like strategic partnership with the university as well or? Yeah, great question. So two of our
[2290.20 → 2294.94] co-founders are professors at Waterloo. Okay. We're in the unique position of having an organic
[2294.94 → 2301.86] academic connection with the university. And part of their university responsibility is to publish
[2301.86 → 2307.96] scholarship and to publish, you know, academic papers and so forth. It's a natural part of our identity.
[2307.96 → 2314.42] It requires discipline to get the balance right. Because research is good. And academics love to
[2314.42 → 2319.78] research things. But if you're a startup, you also need to channel that research into your product.
[2320.46 → 2325.70] Right. While at the same time, giving your academics the latitude to explore things for the next,
[2326.12 → 2331.32] you know, the next gen stuff. So requires discipline. We're hopefully getting it right. But it's something
[2331.32 → 2337.94] you're constantly thinking about. Yeah, yeah, for sure. I mean, we're doing great work. I'm really happy to
[2337.94 → 2344.44] see a lot of it. From your perspective, maybe whether that's with edge computing, AI at the edge,
[2344.44 → 2350.78] or maybe it's with explainability. What are you excited about for the future in terms of like
[2350.78 → 2355.86] things coming down the road or things that you want to explore that seem like fascinating areas?
[2356.16 → 2358.48] What are some of those things that excite you personally?
[2359.28 → 2366.44] Yeah, I think one of the big things is really seeing significant deep learning use cases realized
[2366.44 → 2372.52] in the next, you know, couple years. You know, there's this concept of the adjacent possible that you may have
[2372.52 → 2377.58] heard about, which is, what can you do with your technology given where the world is at?
[2378.16 → 2382.88] And sometimes at Darwin, you know, we were maybe a year too early when we started, you know,
[2383.10 → 2388.30] and so the industry is now catching up and grappling with the problems that our academics knew they would have
[2388.30 → 2394.00] 10 years ago. And so what excites me is now that they're actually doing it, now that, you know,
[2394.10 → 2401.52] Lockheed is trying to do AI and implement robust AI at the edge, the problems we foresaw are ones our tool set
[2401.52 → 2408.38] helps with. So it's seeing how, you know, those use cases play out and just knowing what deep learning
[2408.38 → 2413.90] can do and the number of different areas where it can be used. I mean, healthcare, to cite an obvious
[2413.90 → 2419.70] example, you know, the amount of interest we've gotten because that vertical is really looking
[2419.70 → 2425.10] seriously at experimental technology to create a vaccine is incredible, right? Digital learning,
[2425.20 → 2430.64] like so many things. I think just the general applicability of it is what fascinates me. I say
[2430.64 → 2437.18] sometimes it sort of reminds me of the internet in the early 90s. And I don't know if you remember
[2437.18 → 2443.70] that, but like I was, you know, a teenager in high school and like we didn't think in 1992 or 93
[2443.70 → 2449.46] that these little signals going over telephone wires with modems would reimagine the world and
[2449.46 → 2453.52] reimagine industries. And to me, it's the same thing with artificial intelligence, only greater.
[2454.18 → 2459.12] So the potential there is incredible for me. Yeah, that's perfect to hear. And I could
[2459.12 → 2467.08] definitely see what you're saying, even looking at conferences that I attended like three, four years
[2467.08 → 2473.74] ago, and kind of leading up until now. Yeah, it seemed like, of course, there was a lot of focus
[2473.74 → 2479.10] on like, you know, we did this cool thing with a model, we process this much data with our big data
[2479.10 → 2486.14] platform or whatever. And now I think, you know, I see kind of two huge things, almost in some cases,
[2486.26 → 2493.58] dominating discussion at conferences now, which is like the explainability and fairness and bias piece.
[2493.58 → 2500.60] And then there's the like, how am I going to manage this now? Like, it's a legit piece of our
[2500.60 → 2508.40] software stack. Yeah. And we've decided to buy in. So like, how do we actually like integrate AI?
[2508.70 → 2515.38] And so you see a bunch of, you know, platforms and tools and deployment systems and all of those
[2515.38 → 2521.70] things out there. So, yeah, I think, you know, that's really exciting for sure, from my perspective,
[2521.70 → 2527.68] because, of course, this is practical AI. So, you know, think about the first days when the very
[2527.68 → 2533.90] first developers wrote in notepad or the text editor, and they just wrote program code and compiled
[2533.90 → 2539.48] and that was it. And then as it got more sophisticated, we had IDEs and source control and QA. And like,
[2539.54 → 2544.56] you know, we're speaking at ML ops, DevOps, you know, virtual event later. And like, yeah,
[2544.56 → 2549.00] the enterprise is now like, oh, how do we manage this? How do you version models? How do you version
[2549.00 → 2554.00] data? Like, you know, so it shows you the seriousness with which organizations are taking
[2554.00 → 2558.76] this, right? And the tooling needs to be there for it. Yeah. And that it's, it's not going anywhere,
[2558.76 → 2564.30] for sure. Yeah. I don't know. I feel like, and I've heard people refer to this, that there's kind of
[2564.30 → 2571.40] going to be this AI layer in the software stack now. Right. And just like if you're a software engineer,
[2571.40 → 2578.88] and you don't know anything at all about CCD, probably you need to learn a little bit about
[2578.88 → 2582.78] at least to where you can interact with that system. Not that you have to like to spin up your
[2582.78 → 2587.20] own or whatever, but like you're going to be interacting with this. Yeah. It's a similar way,
[2587.34 → 2592.50] like, okay, maybe you don't need to be an AI expert, but you're going to need to interact
[2592.50 → 2596.44] with these systems, and they're going to be part of our lives. So exactly. Yeah. Yeah,
[2596.44 → 2602.62] for sure. Well, it's been a perfect to chat with you. Where can people find out more about
[2602.62 → 2608.98] Darwin AI and what sort of tips would you give people if maybe they're convinced now that the
[2608.98 → 2616.76] explainability is important? What kind of tips would you give them for maybe either getting started
[2616.76 → 2622.48] with it, with your system, or maybe just learning about explainability in general and the topic out
[2622.48 → 2629.36] there? Any suggestions? Yeah. So we actually wrote a pretty lengthy explainability primer on Medium,
[2629.86 → 2635.20] which goes over the problem, which goes over traditional techniques. And so if you follow us
[2635.20 → 2641.26] on our Twitter, Darwin AI, or our LinkedIn page, we post this all. And so that's a perfect place
[2641.26 → 2646.38] to start because we go over, you know, why the problem exists, what the common techniques are,
[2646.50 → 2650.66] what our technique is, our scholarship around this. So I think that that's a perfect,
[2650.66 → 2653.68] you know, starting point for people that are grappling with this and thinking about,
[2654.06 → 2659.34] you know, addressing the problem. Yeah. Yeah, great. And in light of, you know, a lot of the
[2659.34 → 2663.74] things going on in our nation and otherwise, too, I definitely recommend one thing that I've found
[2663.74 → 2670.40] really useful out there in terms of the sort of exposing maybe on the data side, like the biases
[2670.40 → 2676.34] and the fairness in your data. There's a great toolkit from IBM, IBM Fairness 360. Okay. Even if you
[2676.34 → 2682.42] don't use their toolkit, you can learn a lot about like the various ways people are looking at bias
[2682.42 → 2687.00] and data and other things like that. So just for our listeners who might be interested on that topic,
[2687.00 → 2692.54] but really appreciate you joining us today, Sheldon. It's been a really great and timely
[2692.54 → 2698.62] conversation and really excited to see what comes out of Darwin AI and how the platform progresses.
[2698.62 → 2705.00] And I hope we can meet and chat at either a virtual or real conference or something sometime.
[2705.00 → 2709.16] Yeah. No, thank you for having me. And, you know, as you alluded to at the beginning of the program,
[2709.16 → 2715.00] there's we're in a period of real challenge as a species. So, you know, Godspeed to everybody
[2715.00 → 2719.80] who's listening. And, you know, there's a there's a phrase I told my team this morning that I'm fond of
[2719.80 → 2724.46] in Martin Luther King, you know, the arc of the moral universe is long, but it bends towards
[2724.46 → 2729.64] justice. I believe that, and it's sometimes hard to see. Yeah. And we regress a little bit,
[2729.64 → 2734.32] but I do believe that's true. So, you know, let's just all stay strong and united.
[2735.00 → 2738.00] Yeah. Thank you for that. And thank you for joining. Thank you so much.
[2742.00 → 2746.64] Thank you for listening to Practical AI. We appreciate your time and your attention.
[2747.36 → 2752.70] Word of mouth is the number one way people find new podcasts. If Practical AI has helped you on
[2752.70 → 2758.12] your AI journey, please do tell a friend, hey, they'll thank you later. Special thanks to Break master
[2758.12 → 2763.20] Cylinder for the beats and to our awesome partners for their support. Shout out to Vastly, Linde,
[2763.20 → 2769.72] and Rollbar. If you and your organization would benefit by speaking directly to the AI community,
[2769.94 → 2775.62] you should sponsor Practical AI. Podcast advertising is highly effective, and we would love to work with
[2775.62 → 2781.22] you. Head to changelog.com slash sponsor to learn more. That's all for now. We'll talk to you again next
[2781.22 → 2781.50] week.
[2788.44 → 2788.96] so
[2788.96 → 2818.94] Thank you.
