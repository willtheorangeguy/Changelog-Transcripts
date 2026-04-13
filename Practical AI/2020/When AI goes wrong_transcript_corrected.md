[0.00 → 3.58] I love machine learning. I made a career of it. I don't bring these things up just to make data
[3.58 → 8.60] scientists feel bad. I've been sort of studying different failures in machine learning and AI
[8.60 → 14.14] and algorithmic systems. And if you watch, you know, I see one or two every week now,
[14.32 → 21.12] and that's been going on for almost two years. And so I study these things to learn about how
[21.12 → 25.62] these systems fail so that we can help our clients and help other people not have the same failures.
[25.62 → 31.62] But surely governments must be taking notice of the same level of AI incidents.
[55.62 → 60.68] $5 a month, just five bucks. That gets you a gig of RAM, a blazing fast 25 gig SSD,
[61.04 → 65.50] and one terabyte of transfer. Let's be honest, you can go a long ways on that five bucks.
[65.98 → 70.06] When you do need to scale up, their prices are predictable. So you can put your calculator down,
[70.14 → 74.64] you won't need it. We've been running changelog.com on Linde for years, and we've always impressed
[74.64 → 79.44] by their award-winning support team. Check them out at linode.com slash changelog.
[79.44 → 82.82] Once again, that's linode.com slash changelog.
[85.62 → 97.24] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[97.56 → 102.56] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[102.66 → 107.26] and data science happen. Join the community and Slack with us around various topics of the show
[107.26 → 111.80] at changelog.com slash community and follow us on Twitter. We're at Practical AI FM.
[115.62 → 125.78] Welcome to another episode of Practical AI. This is Daniel Whiten ack. I am a data scientist with
[125.78 → 131.68] SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal
[131.68 → 136.22] emerging technology strategist at Lockheed Martin. How are you doing, Chris?
[136.56 → 138.54] I am doing fine. How are you today, Daniel?
[138.54 → 145.60] Doing well. As we're recording this, it was in the U.S. the day after a long holiday weekend,
[145.84 → 150.96] Labour Day. Did you get to spend some time with your family and relax a little bit, Chris?
[151.30 → 156.40] We did. We had good family times, vegan hot dogs and such as that. Excellent stuff.
[156.54 → 163.30] Yeah, yeah, yeah. We have a specific brand of veggie dog we like. Afterwards, we'll have to sidebar and
[163.30 → 168.52] discuss that. My wife's come up with a special recipe and stuff. Oh, wow.
[168.52 → 170.20] So we can share that. Yeah, it's good. Okay.
[170.66 → 175.42] Definitely, yeah. And I spent some of the weekend talking to my brother-in-law. If you've been
[175.42 → 181.24] listening, listeners might know that my brother-in-law lives with us. And we were talking about
[181.24 → 187.38] the new NVIDIA cards that were announced. And he's already specced out a machine. Of course,
[187.38 → 192.62] he's building a gaming machine. But we were talking about the price points and everything. And he was
[192.62 → 199.70] saying for how much lower of a price you could get the level of the previous generation, which was
[199.70 → 206.18] way more expensive. And I was looking a little bit at the 3090 and what they're doing and everything.
[206.30 → 209.10] It's pretty exciting stuff, I have to say. Are you following that at all, Chris?
[209.36 → 213.84] I am some. Absolutely. As you're talking there, I got to ask. So is your machine,
[213.84 → 216.10] the one you built, all working and happy and everything?
[216.10 → 223.08] Yeah, it's all working. I did a few different models on there. I trained those for a project
[223.08 → 229.00] we're doing at SIL. And that worked really well. It's no problems yet. I kind of kept,
[229.80 → 233.78] you know, there's not much installed on it. I basically have Docker installed. And that's how
[233.78 → 241.02] I'm running all everything. So just using like the published TensorFlow images and NVIDIA images,
[241.02 → 244.84] and then, you know, training from there. So it's worked out pretty good so far.
[245.38 → 247.44] At some point, you need to share your specs and stuff.
[247.70 → 252.78] Yeah, I will. I shared them in our Slack channel. So listeners know we have a community Slack channel.
[253.10 → 259.06] And that's, you can find that at changelog.com slash community. And, and we discussed it a little
[259.06 → 263.80] bit there. But I'm definitely going to have to do a legitimate, you know, blog post. I just haven't
[263.80 → 267.38] haven't done it yet. Shame on me. But it's good. Waiting for it.
[267.38 → 272.98] Yeah, definitely. I'm pretty excited. If you remember, Chris, way back in the day,
[273.38 → 280.20] actually, episode four, we had Andrew Burt on talking about at that point, we were talking
[280.20 → 285.82] about, I think, GDPR and regulation and some other things as they relate to AI. And we're
[285.82 → 291.54] really excited to have Andrew Burt, and also Patrick Hall with us today. They're both from
[291.54 → 296.72] bnh.ai. Andrew's a managing partner there. Patrick is a principal scientist.
[296.72 → 303.44] And this is a pretty interesting and new law firm focused on AI and analytics and other
[303.44 → 308.98] things, which is pretty cool. We'll talk about that a bit. But maybe first, let's just get
[308.98 → 312.72] some introductions. Andrew, do you want to start us out and tell us a little bit about
[312.72 → 316.54] your background? Remind us about your background and how you ended up where you're at now?
[316.54 → 324.76] Yeah, happily. And thanks both for having me and us on. And yeah, it's fun to be back and see how
[324.76 → 328.70] many things have changed in the last couple of years. Yeah, yeah. We're still going. I know.
[328.70 → 333.50] It's been crazy. Yeah, still going. Yeah. Well, despite all the fame, the fame and the fortune.
[334.26 → 340.68] Right. What to do, how to find podcasting set up in your mansion. Yeah. I mean, it's just really nice
[340.68 → 346.58] to see how you got to your guys' heads, you know? Well, anyway, so my background, so I'm a lawyer
[346.58 → 352.40] and also a technologist. I spent many years kind of working at the intersection of law and risk and
[352.40 → 359.38] technology. I spent a few years for the FBI cyber division since 2016. Furthermore, I've also been with the MTA.
[359.82 → 365.00] I was on last time in my capacity with the MTA. And basically throughout all of this time,
[365.00 → 370.74] I have been really the only lawyer in a room full of data scientists and technologists and people
[370.74 → 375.74] wanting to do really cool stuff with data, oftentimes sensitive data or data in regulated environments.
[376.64 → 381.86] And it has brought me to this conclusion, which I've seen over and over, which is that the biggest
[381.86 → 388.20] problems with AI and machine learning, in my view, are no longer technical. And in fact, a lot of it
[388.20 → 393.76] to me seems like it's been productized. The biggest challenges, and I've seen this in practice,
[393.76 → 399.54] like being the only lawyer in these rooms, is legal, it's ethical, it's policy related. And so
[399.54 → 404.80] I've started to see these really, really, huge challenges stand in the way of really exciting
[404.80 → 413.20] technology projects. And so all of that kind of led Patrick and me to start B&H.ai, which is a
[413.20 → 419.54] boutique law firm based in Washington, D.C. It's the only place in the country where lawyers and non-lawyers
[419.54 → 425.48] can actually jointly run law firms. And so we can talk about why that is and why that exemption
[425.48 → 430.82] exists. But really, we're the first to do this with data science. And our core thesis is that the
[430.82 → 436.84] only way to do data science right, the only way to really kind of get all the value and minimize all
[436.84 → 442.26] the risks is by really commingling these types of expertise, the legal and the policy really,
[442.26 → 447.84] really closely with the technical and the data science. So that's the 50,000-foot nutshell. And
[447.84 → 452.48] we're just about we launched right at the end of March. So we're just about five months into
[452.48 → 457.24] our journey. And it's been a lot of fun. Awesome. Yeah, that's that's super great. We're also really
[457.24 → 462.30] excited. Patrick, thank you for joining as well. It's great to meet you and get the connection
[462.30 → 467.08] through Andrew. Could you tell us a little bit about your background and how you ended up
[467.08 → 475.34] working together with Andrew on this? Yeah, of course. I'm happy to be here. And my journey was
[475.34 → 482.64] machine learning. I don't you know, started many moons ago at SAS Institute in North Carolina. And I
[482.64 → 488.68] think that that was really formative for me. It seems like some data scientists don't even know about
[488.68 → 495.78] SAS anymore. But it's, you know, roughly $3 billion company that's been making billions of dollars off
[495.78 → 502.94] analytics and machine learning and AI for decades. And just being a part of that organization,
[502.94 → 508.62] which largely lives sort of outside the ML hype sphere, but makes more money than almost any
[508.62 → 514.62] other ML company. And just this awareness that there was a right way to do things that's decades old is
[514.62 → 521.16] was really formative for me. And after that, I joined the sort of topsy-turvy ML startup world with
[521.16 → 529.62] at H2O, where I, you know, I kind of led their efforts in responsible machine learning for
[529.62 → 536.14] for three to four years. And, and we came up with a decent product. And I think like Andrew, you know,
[536.14 → 541.52] I came to the same conclusion, but I saw, like Andrew said, you know, not only does the technology
[541.52 → 548.20] exist to sort of make machine learning more transparent and more trustworthy, hopefully more fair,
[548.20 → 552.44] but it's already being productized. So it's so it's reaching a certain level of maturity.
[552.86 → 558.28] And really, what I see, you know, like Andrew said, I think the next round of challenges for
[558.28 → 562.56] machine learning are not going to be technical, they're going to be policy and regulation and
[562.56 → 569.08] legal and human interactions with AI and machine learning. And, and that's why I joined Andrew on
[569.08 → 573.42] this journey, because I saw a lot of the same things he did. And it was an easy pitch,
[573.42 → 577.98] actually, once he explained it to me. So happy to be here on the podcast and happy to be here with
[577.98 → 578.72] BNH.ai.
[579.54 → 584.64] Thank you very much for joining us. And it's nice to meet you. Andrew, having Andrew back is like
[584.64 → 589.72] having an old friend back from our very beginning, as you mentioned. So, you know, Andrew, you touched
[589.72 → 595.42] on it already a little bit in your intro. And Patrick, you did as well. But can you, you know,
[595.44 → 601.68] you're at this unique position of you have the entire landscape of law with the entire landscape
[601.68 → 609.86] of AI, at this juxtaposition, where they are starting to merge. And, you know, last time, you came, you gave us the
[609.86 → 616.74] general data protection, regulation, deep dive as part of that. And we talked about the fact that there wasn't a
[616.74 → 623.02] lot in terms of laws and regulations out there. And then, you know, on top of that, since then,
[623.08 → 629.78] we've really gotten deep into AI ethics. I know, like, in my own case, I was leading AI ethics for
[629.78 → 634.50] Lockheed Martin for a while, I just stepped out of that position, but learned a lot. So much has
[634.50 → 641.54] happened since we had you on last in this space. Can you together, guys, can you all kind of describe
[641.54 → 646.80] what the space looks like and what some of the complexity with the landscapes at large,
[646.90 → 653.60] given so many things touching ethics, all of these together? Yeah, happily, I'll start and then
[653.60 → 659.12] there's a danger of me going on too long. So Patrick can jump in, please do so. I think from my
[659.12 → 664.30] perspective, I guess, from a very high level, what I have seen is I think the prospect of AI and machine
[664.30 → 669.60] learning, and I'm really for now, I'm just using those two terms interchangeably, we can dive more
[669.60 → 675.56] into why we might want to use one term versus the other. I'm very happy with that. As Chris probably
[675.56 → 681.50] knows from previous of my discussions, other people might not be so much, but you're in a safe space.
[681.98 → 687.64] Okay, cool. That means a lot. That means a lot to me. So I think the prospect of what AI can do,
[688.08 → 692.30] the value, I think has only begun to increase over time. And I think there's a wide recognition,
[692.68 → 698.62] both in industry and by governments and regulators. And the way that I think about the value is that what AI
[698.62 → 705.56] does really, really well is it scales decision-making in volume and speed. And so if you just
[705.56 → 709.18] think about that, so we have this tool, I mean, it's been around for a while, but let's say in the
[709.18 → 714.22] last five years, the value has become more clear, and it's become used more and more, you have this
[714.22 → 719.58] thing that can make huge amounts of decisions at really high speeds. So the progression is almost
[719.58 → 724.48] natural. So as that type of tool starts to be used more and more in the real world, there are a huge
[724.48 → 730.70] amount of concerns that are associated with it. The slightest bias in something like that ends up
[730.70 → 736.74] being magnified. The slightest security bug can be magnified. What you have is, I think, really the
[736.74 → 741.22] same things that make this technology so powerful, which is it can do so much in such little times
[741.22 → 748.00] so efficiently, also mean that really any of the risks end up being greatly magnified. So I think over
[748.00 → 753.82] the last few years, there has been this recognition that if we don't get this right, if we really don't
[753.82 → 758.72] refine what it means to manage all of these different liabilities, we're going to be in a
[758.72 → 764.70] world of trouble. And so that's what I have seen. There's a really wonderful paper from Algorithm Watch
[764.70 → 771.14] called Paper Tigers, which I can't remember the number, but it actually studied something like 120,
[771.38 → 777.12] maybe more ethical AI frameworks released in the last couple of years. And the title is called Paper
[777.12 → 783.46] Tigers because these frameworks don't really have teeth. And so I think it's a to me,
[783.46 → 788.16] the rise of like the corporate ethical AI framework, I think is a perfect sign that
[788.16 → 793.92] we have an issue, like something is wrong. On the other hand, studies like that from Algorithm Watch,
[794.02 → 799.72] I think are also kind of indicative of the fact that we are nowhere close to solving it. And so
[799.72 → 803.60] anyway, that's what this landscape kind of looks like from my perspective.
[803.92 → 809.28] I'll jump in real quickly. First, I want to echo Andrew's last statement, you know,
[809.28 → 813.64] and because I think that some of them as a technologist, right, when I say things, I think,
[814.08 → 818.24] like, I think the technology exists to help with some of these problems. I want to be very clear that,
[818.34 → 823.38] you know, technology alone will never solve these problems, right? Technology is one of many
[823.38 → 829.36] necessary pieces. But to add on to what Andrew was saying, you know, and, and I need to be also need
[829.36 → 833.82] to be very clear, like, I, I love machine learning, I've made a career of it, I don't bring these things
[833.82 → 839.64] up just to make data scientists feel bad. I've been sort of studying different failures in machine
[839.64 → 846.20] learning and AI and algorithmic systems. And if you watch, you know, I see one or two every week now,
[846.34 → 853.64] and that's been going on for almost two years. And so, you know, I study these things to learn about
[853.64 → 858.56] how these systems fail so that we can help our clients and help other people not have the same
[858.56 → 866.78] failures. But surely governments must be taking notice of the same level of AI incidents. And so I think
[866.78 → 872.20] that's another reason why we see companies and governments. So just this year, organizations like the
[872.20 → 880.20] Federal Trade Commission, and FINRA, the Financial Industry Regulatory Authority, have issued this sort of
[880.20 → 886.80] long treatises on the use of AI that Andrew and I think is sort of forecasting or telegraphing future
[886.80 → 892.30] regulation. So, so I think there's, you know, Andrew sort of focused or brought up the idea that the
[892.30 → 896.36] corporations are waking up to this. And I certainly agree with that. And I think that governments are
[896.36 → 899.80] also starting to notice the way that AI fails and react to that.
[900.44 → 905.60] Yeah, I want to ask kind of a follow-up a little bit to that. And that is, you know, when you talk
[905.60 → 909.86] about the failure of ethical frameworks for AI, they're very limited, you know, they're, they're
[909.86 → 916.06] aspirational, they kind of talk about these ideas that you want to constrain your operations with.
[916.06 → 920.38] But as you pointed out, I think the phrase used was they have no teeth. And I, I certainly agree
[920.38 → 926.44] with that. I think one of the challenges that I'm expecting over the next couple of years is as
[926.44 → 933.56] organizations either create or adopt frameworks to utilize for that, the devil is going to be in
[933.56 → 938.76] the details. The devil is in how do you integrate that in with your legal structure at your, at your
[938.76 → 943.72] organization? How do you integrate that in with your operations and how you serve your customers?
[943.72 → 951.10] Um, and so there's a great deal of, of work to do in terms of figuring out how you customize that
[951.10 → 958.36] framework down to your organization specifics. Do you have any kind of guidance on that at large? I
[958.36 → 963.88] mean, would you agree that that is the case? And how would you advise organizations to think about
[963.88 → 967.14] it? You know, so I've adopted a framework. What's next?
[967.14 → 973.06] Honestly, that's exactly why we exist. We just see this huge gap between the people thinking about the
[973.06 → 978.20] laws and the policies. And then, you know, the data scientists and the engineers who actually have to
[978.20 → 983.22] go operationalize it. And what we've seen in practice time and time again, is these big frameworks,
[983.42 → 988.96] usually called ethical AI, sometimes, you know, trustworthy or responsible AI. And it makes everyone feel
[988.96 → 992.60] good. And they're aspirational. It's great. And then it gets to the, you know, the folks in the
[992.60 → 998.48] trenches and the business units, and they say, this is great, but I can't do this. Like there's a chasm
[998.48 → 999.48] that we need to cross.
[999.88 → 1000.28] It's hard.
[1000.96 → 1007.02] Yeah, it's very hard. And so that is why we exist. I think one of our big things is that AI has been
[1007.02 → 1013.92] around for a while. We don't need to start from scratch. There is a host of regulatory, actual
[1013.92 → 1019.22] oversight documents, and then also guidance documents that actually are tried and tested. Some are five
[1019.22 → 1024.26] decades old, dealing with discrimination. Some are about 15 years old, just dealing with model risk.
[1024.78 → 1030.10] So there are actually lots of places that we can start with. And as a law firm, that's what we start
[1030.10 → 1035.02] with. How have regulators, especially in finance and anti-discrimination, like what have they done?
[1035.08 → 1040.42] What does the case law say? And it turns out like there is a lot that we can work with. So that gap,
[1040.54 → 1045.72] that chasm, what it looks like is this huge gap is actually not that deep, and it's not that wide.
[1045.72 → 1050.40] I don't want to minimize how hard this can be, but there are a number of practical things that
[1050.40 → 1056.20] organizations like have been doing and can do for whatever reason. I think largely because the
[1056.20 → 1061.30] lawyers and the technical folks just don't talk enough to each other. I think a lot of these methods
[1061.30 → 1062.80] are underappreciated.
[1075.72 → 1086.88] Hi, I'm Matt, and I'd love to tell you about Pace.dev. Pace.dev is a minimalist task management
[1086.88 → 1091.86] and async by default communication tool. Our screen recording feature is actually very popular.
[1092.30 → 1097.30] Wherever you can leave a comment, just like how easy it is to upload a file, you can record your
[1097.30 → 1103.62] window or the entire screen and upload it as a video to the team. Sometimes a screen recording
[1103.62 → 1109.08] is the perfect way to explain something. You know, whether it's a bug that only happens for you
[1109.08 → 1115.06] or maybe more optimistically, a new feature that you can't wait to show off. And the showcase feature
[1115.06 → 1119.88] takes that a step further and lets you highlight progress, which is a much more positive experience
[1119.88 → 1125.46] than trying to make up estimations out of thin air. So please learn more and start your free trial
[1125.46 → 1126.52] at Pace.dev.
[1142.30 → 1149.04] I'm really interested. I know that you came out with some things recently around like an AI incident
[1149.04 → 1155.00] response checklist, which I'm super interested to dive into the details a little bit. But before we do
[1155.00 → 1162.78] that, I'm just kind of curious to kind of talk generally about AI incidents. So where my mind
[1162.78 → 1167.66] is going with this is like we have some experience with software incidents, right? And there's certainly
[1167.66 → 1174.48] software that drives things that, you know, can make a huge impact on people like, you know, software
[1174.48 → 1180.68] in a medical setting or in a medical device or something that's not AI. But if it malfunctions,
[1180.68 → 1187.56] you know, someone's health could be at risk or, you know, you could expose private information or
[1187.56 → 1193.00] something like that. Right. And there's there are those things that definitely do exist out there.
[1193.00 → 1200.30] What are the sort of liabilities about AI applications in particular that might differentiate
[1200.30 → 1205.88] them from some of these things that maybe we've been dealing with for some time? Patrick,
[1205.88 → 1211.12] do you have any opinion on that? Yeah, yeah. And, and, you know, I'm, I'm not a lawyer. So I'm gonna
[1211.12 → 1219.02] have to let Andrew comment on the legal liability side. But I can say, you know, we see, let's say
[1219.02 → 1226.94] in the tech media and sort of broader media, we see a big focus on discrimination. And of course, you know,
[1226.98 → 1235.10] discriminatory algorithms, AI is, is not something that, that we want out there in the world at all. But we,
[1235.10 → 1242.02] we also try to, to sort of direct people to other problems, like privacy, you know, you mentioned
[1242.02 → 1247.66] data security, you mentioned, and, and so, you know, when, when I look at some of these AI incidents
[1247.66 → 1254.88] I've been tracking, I'd say they mostly break down into maybe four categories. So discrimination
[1254.88 → 1261.16] probably being the biggest one, and we've seen some very troubling things there. But also, you know,
[1261.16 → 1267.18] consumer privacy, data privacy, security, people essentially being kind of sloppy with sensitive
[1267.18 → 1272.42] data that's used to train AI systems, or data that's generated by AI systems. And then a final
[1272.42 → 1279.36] one that I see fairly often, too, is this idea of no interoperability in a machine learning system,
[1279.36 → 1285.24] or sometimes it's called computer says no, where the main failure of the algorithm was just that
[1285.24 → 1290.48] it's a black box, right? It's making decisions that impact people's lives that may or may not be
[1290.48 → 1295.10] correct. But the consumer of the decision has absolutely no ability to appeal the decision.
[1295.34 → 1300.30] And I think that's a huge mistake and another type of AI incident that I see fairly often. So
[1300.30 → 1304.40] I'll leave it at those four sort of categories that I observed, and maybe let Andrew sort of chime
[1304.40 → 1306.88] in on the legal liabilities. Is that okay?
[1307.10 → 1311.16] Yeah, that's good. I'm curious on that last one, actually, because it's an interesting
[1311.16 → 1317.76] category. And of course, we've talked about the sort of interpretability issues and other things
[1317.76 → 1324.42] on the podcast before. In that last category, in terms of the incident itself, is the problem mostly
[1324.42 → 1330.64] more weighted on the side of like interpretability and not kind of digging into the model? Or is it more
[1330.64 → 1336.24] on the like, the computer has made the decision, and there's no way to sort of back out that decision,
[1336.24 → 1341.80] like it just happens. And like, you know, like a person is denied insurance, because they're deemed
[1341.80 → 1347.30] high risk, and there's no way for them to like, you know, like you say, appeal that or something,
[1347.54 → 1349.62] which side of those is it more weighted on?
[1350.04 → 1355.02] I think what I see in practice is it ends up being the latter, right? Right. And this goes back to the
[1355.02 → 1360.42] comment of technology can't really solve these problems. So the sort of two biggest incidents in
[1360.42 → 1366.22] my mind when I hear computer says no, or no interoperability, no appeal or override capability,
[1366.22 → 1374.22] is compass, which is a risk assessment instrument that's used to help in pretrial and parole decisions.
[1374.56 → 1380.84] And then the recent A-levels scandal in the UK, where hundreds of 1000s of students had their
[1380.84 → 1386.80] grades adjusted by an algorithm. And in both these cases, it seems that the algorithm itself was
[1386.80 → 1392.36] at least well tested and well understood by its operators. But the way it was presented to its
[1392.36 → 1398.98] consumers was as this sort of unappealable voice of God that's going to ruin your life. And so I spent
[1398.98 → 1404.62] three years deep, deep, deep and explainable machine learning and interpretable models. I sadly don't
[1404.62 → 1409.60] think that that's the problem here. I think that, of course, that can be a problem that the algorithm
[1409.60 → 1415.74] isn't interpretable. And that's something that I object to in almost all cases. But the big incidents
[1415.74 → 1419.72] that are coming to my mind are more process problems or more human problems.
[1419.72 → 1425.58] I would also just to add to that, I think there's certainly this like kind of the problem
[1425.58 → 1429.86] where there's an algorithm that's deployed, you know, in a public setting where there really is
[1429.86 → 1436.06] this like it's, it's just there's almost like this tension between the authority of the algorithm
[1436.06 → 1441.00] and then everyone who, you know, whose subject to it. And that certainly there is a problem there.
[1441.00 → 1446.64] But just to get more operational in terms of day to day, one of the things that we see in practice
[1446.64 → 1453.28] involved in an incident response is that that same dynamic can also happen between the developers
[1453.28 → 1459.36] of an algorithm or a model and the model itself once it's deployed. And so if something wrong,
[1459.60 → 1464.82] so it's not just consumer decision to model. Perfect point. Really. It's also if something
[1464.82 → 1470.26] bad is happening, if there is an incident, if there is some instance of discrimination or potential
[1470.26 → 1476.50] hacking or data breach, then we have this problem where Patrick calls this debugging. And I think
[1476.50 → 1481.62] it might be worth giving Patrick a proverbial soapbox and let him talk about debugging shortly.
[1481.62 → 1488.58] But if there is a situation where we have potential liability and the data scientists actually need
[1488.58 → 1494.10] to fix it, we have the same type of clash. And what we've seen in practice is it can take an
[1494.10 → 1499.50] extraordinarily long period of time for the data scientists to one, make the decision in the business units.
[1499.94 → 1504.58] Do we pull this from production? Is the liability greater than the business value? So should it be pulled
[1504.58 → 1511.14] from production? What do we do? How do we debug it? I think once a model goes live, so to speak,
[1511.54 → 1518.18] there ends up being this kind of very similar dynamic. And so we see on a practical basis,
[1518.18 → 1524.26] in terms of thinking about risk and liability, we see a huge number of organizations doing things that
[1524.26 → 1528.82] are much smaller, you know, decisions of much smaller scales struggling with this when something goes
[1528.82 → 1534.82] wrong. And just really quickly, building out that AI incident response plan, just like you'd build out
[1534.82 → 1539.86] a response plan for other mission-critical computer systems can help address a lot of those questions
[1539.86 → 1543.78] that Andrew's bringing up, right? A lot of these questions that we see teams struggling with internally,
[1543.78 → 1549.86] if you actually spend the time to generate that checklist, then you'll have better answers for
[1549.86 → 1555.86] this when the time comes. Yeah. And you mentioned the debugging thing, which I definitely I resonate
[1555.86 → 1562.42] with that a lot. So I don't want to lose that, for sure. I know, like, a lot of times when I talk to teams,
[1562.42 → 1568.98] I do some advising and training and stuff. And a lot of times, I think people have in their mind, like, oh, we train
[1568.98 → 1577.30] this model, like we kind of wrap it in our API or whatever, or embed it in our API. And like it operates and
[1577.30 → 1584.90] like the unit tests are like around like the API and like, oh, can I process this, you know, JSON payload,
[1584.90 → 1591.06] right? It's not around the model itself. So apparently, that's something that you're passionate about as Andrew
[1591.06 → 1596.50] alluded to Patrick. So Patrick, do you want to say anything about that in terms of debugging? And like, you know, the
[1596.50 → 1603.70] state of debugging, especially around incidents when something goes wrong with an AI model or something unexpected happens?
[1603.70 → 1610.26] Yeah. So if you guys will permit me when I'm done chatting, I'll put two links in the Zoom chat.
[1610.26 → 1614.10] Yeah. Yeah, we'll include those in the show notes as well for the episode.
[1614.10 → 1617.46] That'd be great. Yeah, I hope they're useful. We've gotten some positive feedback on them.
[1617.46 → 1624.34] So yeah, I think there are two levels of debugging, right? Two major categories of debugging. And you
[1624.34 → 1631.30] brought up one where you said unit test of the API. Great, please, God, do that. I'd include that and sort of just sort of
[1632.02 → 1638.02] normal IT system debugging, right? Unit testing. Yeah, something that people have been doing for
[1638.02 → 1645.14] quite some time. But, and I can't explain this, you know, aside from sort of sad level of hype and
[1645.14 → 1652.26] exceptionalism and data science culture, people in general, in my experience, are failing to apply
[1652.90 → 1660.42] general software based best practices to their machine learning. And I, like I said, I can't explain this
[1660.42 → 1666.50] except for sort of sad and regrettable cultural phenomenon. So that's one main issue I see.
[1666.50 → 1672.58] Patrick, I'll say, I deal with that every day trying to get our, our DevOps folks and our developers
[1672.58 → 1673.46] working with ML.
[1673.46 → 1678.18] Makes no sense. Makes no sense to me. So machine learning is essentially, you know,
[1678.18 → 1686.02] given its complexity, given its drift characteristics, right? It's likely even more volatile than,
[1686.02 → 1691.94] than say, some other mission-critical software assets. And so why data scientists are given a pass
[1691.94 → 1696.66] on basic software quality, I'll never understand. Okay. And so that would be one thing to remit,
[1697.30 → 1703.62] remedy, just, just ASAP. And of course we debug our other mission-critical software assets,
[1703.62 → 1707.94] right? So, so we should be debugging our machine learning systems, just, just using basic software
[1707.94 → 1714.18] best practices. So, so that's part one of, of model debugging. And I, I truly believe that there's no
[1714.18 → 1720.26] such thing as responsible AI or trustworthy AI without basic software best practices. Then we get into
[1720.26 → 1724.74] actually testing the machine learning itself, right? And, and that's more difficult and, and much more of
[1724.74 → 1730.10] sort of new field. And I've got some ideas around that. I'm certainly not the only one.
[1730.10 → 1737.30] There was a conference workshop at ICML, must've been last year when we could still fly, maybe two
[1737.30 → 1740.98] years ago, I'll put the link in the chat where, where some of the world's leading academics got
[1740.98 → 1746.10] together and discussed this. So I would say that just in general debugging of the machine learning
[1746.10 → 1752.10] system itself comes down to, at least from a practical standpoint, sort of sensitivity analysis,
[1752.10 → 1757.86] right? Where is my system unstable? Residual analysis, where, where is my system making
[1757.86 → 1763.46] errors? And can I, can I try to understand those and reduce those security audits, right? We're,
[1763.46 → 1769.30] we're well aware that there are now attacks that directly affect machine learning systems. So,
[1769.30 → 1774.18] so doing red teaming and bug bounties and security audits on those known security vulnerabilities of
[1774.18 → 1780.34] ML, of course, discrimination testing and discrimination remediation is a big one here.
[1780.34 → 1786.18] Yeah, this is all super, it's, it's resonating with me so much. I know Chris and I have talked
[1786.18 → 1791.30] and I have conversations every day with like, you know, you're talking about probing the sensitivities
[1791.30 → 1797.14] and all that. It's so, it's so important. And it's actually like in a lot of cases, it doesn't require
[1797.94 → 1802.58] that much extra work. And I think something that people don't realize as well as to some degree,
[1802.58 → 1809.70] a major component of this is doing this sort of tests actually allows you to be a better data
[1809.70 → 1814.50] scientist or produce better work, right? Because you're actually, you understand the behaviour of
[1814.50 → 1820.02] your model more, and you're finding those places where it misbehaves, and you're able to deal with
[1820.02 → 1826.42] those in a sort of confined test space where you actually, the end product becomes actually better.
[1826.42 → 1829.38] Your model is actually better in the end and more robust.
[1829.38 → 1834.26] Thanks for allowing me time to pause and Google my, my sort of last model debugging practical thing,
[1834.26 → 1838.98] which is, which is benchmark models, right? Like having a simple, trustworthy, interpretable model
[1838.98 → 1843.14] to compare your more complex model against, I think is another super important thing there.
[1843.14 → 1847.54] Just to echo your comments. Sometimes it's a lot more work. Sometimes it's not a lot more work.
[1847.54 → 1852.74] It will make your work better. But, but seriously, when we're talking about data scientists who
[1852.74 → 1858.26] are on average paid very, very well, even if it's a lot of work, you know, with great power comes
[1858.26 → 1863.54] great responsibility. And we just need to start taking more responsibility for the systems that
[1863.54 → 1870.26] we're making. So I actually want to swing things back over to Andrew for just a moment. And Andrew,
[1870.26 → 1874.34] I've been sitting here as we've been talking, pondering something that you said a few minutes ago,
[1874.34 → 1879.94] you were talking about, you know, case law, and I guess that's opposed to statutory law,
[1879.94 → 1883.14] things that I don't normally think about on a day-to-day basis, but I know you do.
[1883.14 → 1887.22] Andrew Can we just define those terms too? Because I think there's probably a lot of people
[1887.22 → 1891.14] that are like maybe confused a little bit. And then I'll ask after that. Go ahead.
[1891.14 → 1895.86] Andrew Okay. Happily. Yes. So, so especially in the U S which is a common law system,
[1895.86 → 1901.62] the way that laws work and the places that laws come from vary. And so there can be a regulatory agency,
[1901.62 → 1905.78] which will promulgate rules that you can think of like the FDA, which has like, you know,
[1905.78 → 1910.58] they are in charge of food and drug. You can have Congresses and state legislatures,
[1910.58 → 1916.74] which will say pass a law that is like doing X is a crime. So like, don't do X or bad things will
[1916.74 → 1922.90] happen. And then there's also case law and case law kind of evolves over time from the courts and case
[1922.90 → 1929.30] law is basically arising on a decision by decision basis. So there'll be, you know, there'll be a case,
[1929.30 → 1936.10] someone, you know, there'll be a controversy that that lends some party in court. And then the decision
[1936.10 → 1942.58] that's made as, as that issue is being resolved comes from just a larger body of case law. And so
[1943.22 → 1948.10] one of the things I think I was thinking about in the world of anti-discrimination is we have all of
[1948.10 → 1953.78] these regulations, both from regulatory agencies. And we have statutes from, from Congress saying,
[1953.78 → 1958.58] basically don't discriminate and don't discriminate in these environments. But it turns out it's really,
[1958.58 → 1964.26] really difficult to figure out exactly what counts as discrimination in a society that's really just
[1964.26 → 1970.50] like marked by profound inequities. And so a lot of the give and take and a lot of figuring out what
[1970.50 → 1975.54] exactly does this mean and how do you balance the usefulness of a model with its potential
[1975.54 → 1981.14] discriminatory impact, like that way comes from case law, and it comes from courts. And so we can look
[1981.14 → 1986.58] at the guidance that comes from government agencies as we try to figure out what the right way to approach
[1986.58 → 1991.38] these issues are. And then we can also look from like specific cases and say, okay, at this one
[1991.38 → 1997.70] specific time, you know, this group ran into an issue and here, here's how the judiciary solved it.
[1997.70 → 2003.22] So hopefully that was a we can get the like schoolhouse rocks, the bill, we can feature that
[2003.22 → 2004.26] also in the show notes.
[2004.26 → 2006.02] You get to sing that at the end of the show, right?
[2006.02 → 2006.74] Yes, exactly.
[2006.74 → 2007.30] Exactly.
[2007.30 → 2011.14] Yeah. Anytime I talk to anyone, that's, that's like, I put on a paint in the top hat.
[2012.02 → 2017.30] Perfect. Okay. So you'll have to get pictures of that to fit out. Anyway, so you've already covered
[2017.30 → 2022.10] part of what I was going to ask. And that is, you know, we've talked about the fact that there's not
[2022.10 → 2029.94] a lot of AI specific statutory law, you know, and so it sounds like you really start with regulation
[2029.94 → 2037.62] and case law and kind of connect that in with the kind of AI data context. Is that a fair way in
[2037.62 → 2039.22] terms of how you would operate in the space?
[2039.22 → 2044.58] So just like Patrick can't explain why data scientists hold themselves to different like
[2044.58 → 2050.58] security standards than, you know, traditional software developers. I can't explain why there isn't
[2050.58 → 2056.90] more awareness of just the liabilities that existing laws place on AI. So it's true. There's
[2056.90 → 2063.94] no national AI law. There are very few laws that say, you know, those creating artificial intelligence
[2063.94 → 2070.98] shall not do this. So you're right that it's not that direct. But there are a huge number of ways
[2070.98 → 2078.18] that existing laws impact AI systems. And so on of the things that, that I kind of feel like I say
[2078.18 → 2082.98] over and over again, is that the liabilities are not new. And we've been dealing with a lot of these
[2082.98 → 2089.62] for a while. So I'm happy to list some, but so there are, I think the three most obvious are security
[2089.62 → 2096.50] and privacy and discrimination. If an AI model discriminates, serious liability can ensue if there
[2096.50 → 2103.86] are privacy violations. So basically those can happen all sorts of ways, but just as simple as using data
[2103.86 → 2108.82] for the wrong reason, when it was collected for one reason, but then used to train a model for
[2108.82 → 2114.74] another, that's a privacy violation. Security violations. I think it's fairly intuitive how
[2114.74 → 2120.98] you can, I think at a high level, the attack service for AI is just very much different than
[2120.98 → 2127.06] traditional software. So an adversary might be able to manipulate the model or steal data or gain access.
[2127.06 → 2130.82] So those are kind of the intuitive things. And there are laws governing all of that.
[2130.82 → 2138.02] At the same time, there are things as basic as negligence standards. So if you create an AI model
[2138.02 → 2143.86] and it goes and someone is harmed either physically or emotionally, or something breaks, we have all
[2143.86 → 2151.30] sorts of negligence and product liability laws. And just because they don't say AI doesn't mean that
[2151.30 → 2156.98] they're any less applicable. So there are a whole host. And I should say, new laws are clearly coming.
[2156.98 → 2162.34] Like Patrick said, the FTC in particular, the commissioner gave a speech. I actually have it
[2162.34 → 2167.22] somewhere on my desk. I can pull it up. But she gave a speech in January and the FTC has been doing
[2167.22 → 2173.22] every couple months, something similar. And she basically said, we're coming for AI. AI is responsible
[2173.22 → 2179.46] for a huge and growing amount of harms. And the FTC is going to regulate it even more. So new laws are
[2179.46 → 2184.58] definitely coming. And I think that that is not kind of controversial to say, but the laws on the
[2184.58 → 2189.46] books right now already do impact AI quite significantly.
[2189.46 → 2197.86] And I think I can add that some of the work in just the very first months of our law firm has been
[2197.86 → 2206.90] AI violating sort of local laws, right? Not these big federal ALCOA or FICA, Equal Credit Opportunity
[2206.90 → 2213.14] Act or Fair Credit Reporting Act, but concerns about AI violating more local laws that I never would have
[2213.14 → 2216.18] thought. I mean, Andrew probably thought about it, but I never would have thought about it.
[2219.46 → 2221.46] So
[2231.70 → 2239.38] Changelog++ is the best way for you to directly support practical AI. Join today and unlock access
[2239.38 → 2245.46] to a private feed that makes the ads disappear, gets you closer to the metal and help sustain our
[2245.46 → 2252.74] production of practical AI into the future. Simply follow the Changelog++ link in your show notes,
[2252.74 → 2261.22] or point your favourite web browser to changelog.com slash plus. Once again, that's changelog.com slash plus.
[2262.66 → 2264.98] Changelog++ is better.
[2275.46 → 2281.62] We've got into a little bit of the sorts of liabilities and incidents that can happen.
[2282.18 → 2287.30] And I'd love to kind of switch gears a little bit and talk about this incident response
[2287.30 → 2293.22] checklist that you've developed. I think that's a pretty cool thing. And maybe we could start out by
[2293.22 → 2299.22] just asking, you know, how this came about? Was this something that you envisioned even, you know, even before
[2299.22 → 2306.26] starting the law firm? Or did it come out of your sort of initial conversations with clients? Or how did this develop as something useful?
[2306.26 → 2311.46] So I think this was not the first thing we had in mind, you know, when we launched the law firm.
[2311.46 → 2319.86] I think we assumed that we would be kind of involved in a lot, lots of preventative work, you know, way before something bad happens.
[2319.86 → 2326.10] And frankly, coming out of the gate, we started to see that people were reaching out to us once something bad happened.
[2326.10 → 2326.42] Interesting.
[2326.42 → 2334.90] You know, frequently, it's not a good, we don't recommend it, you know, call lawyers, call risk folks before you're in trouble.
[2334.90 → 2341.06] When you start building a critical machine learning product, that's when to call legal oversight ethics people in.
[2341.06 → 2368.10] Yeah, so we very much want to help. For us, as an example, we want to help folks way before we're actually needed. What we've learned is sadly, that's not how things work in practice. And very frequently, it takes something bad happening for, you know, data scientists and lawyers to say, kind of, oh, crap, there, you know, we have a gap. And so I used to work at the FBI cyber division, I actually got certified as a traditional cyber incident response handler.
[2368.10 → 2381.30] And so I was very familiar with the six stages of incident response. And one of the things Patrick and I did very early on, is we went through the traditional, you know, textbooks that I've been trained on the traditional incident response.
[2381.30 → 2402.72] And we said, we're going to look at all the bad things we're being exposed to, you know, we're seeing clients struggle with, and all the other liabilities that could happen with AI. And we're just going to go through and see how does current incident response practices measure up. And also in our experience, you know, the answer is they don't. AI is shiny, new and different. And there's this hype cycle.
[2402.72 → 2424.92] And as a result, the incident responders, just kind of, it's just out of their purview. And so we went through, and we realized that there could be a very severe AI incident creating huge amounts of liabilities. In fact, one that we are involved in now is for like a fortune 100. The board is deeply involved, the CEO's butt is on the line.
[2424.92 → 2449.34] And we went through the traditional incident response. And you could go through that, you know, checkmark by checkmark, and everything would be okay, wouldn't have even known anything was wrong with, with the AI in question. And so that kind of, I think, woke us up to the fact that this is something different, this is something new. And also, there's really no guidance on how do you respond when there's an incident. And so we put this together.
[2449.34 → 2479.28] And we love model risk management practices that are mostly in financial services and highly related to this guidance from the Federal Reserve called SR 11-7, which is a masterful treatise on model risk management. Neither did model risk management as it exists today. I'm sure it will mature to include this, but model risk management as it exists today also did not include, you know, exact ways to,
[2479.28 → 2492.60] to react to AI incidents, right? So there was nothing in traditional cybersecurity response. And there were things in model risk management that would help, but nothing that actually, you know, told you how to respond or to prepare to respond.
[2492.60 → 2512.72] Yeah, I'm curious, what were, as you went through those things that are existing and best practices that had already been developed? What are a couple examples of where maybe, you know, existing incident response plans just wouldn't cut it or would leave something out in terms of AI and machine learning?
[2512.72 → 2535.72] So there are many ways that there could be AI incidents. And I actually, I'm getting a little concerned that I think people are just only assuming that the worst that AI can do is discriminate, because there's so much in the news. And frankly, about 15 years ago, there weren't mandatory breach reporting guidelines. So there are legal requirements now that say, if there's a breach or a hack, you need to report it. So now we know all the bad stuff that's happening. Before those, no one really did. And we're in an analogous situation with AI, where all the bad stuff that's happening.
[2535.72 → 2564.52] But there's no incentive for anyone to share it. So the public is in the dark. But anyway, so at the risk of doubling down on discrimination, let's say you have an Apple Goldman situation, which, you know, their credit model was reportedly discriminating. Females, there are many different ways that AI can discriminate. But let's just say you have something that's discriminating.
[2564.52 → 2594.38] Let's say it has been deployed and exposed to, you know, I don't know, many hundreds of thousands, a million, whatever consumers. The question is, how do you know that that model is discriminating? And how do you know the depth of that discrimination? And you could go and so that would be an incident. Let's say you have a model that's been deployed against a million people. And let's say 20% of those decisions have been in some shape or form discriminatory. That's bad. There's lots of liability. It's a huge
[2594.38 → 2619.38] incident. 200,000 people. I mean, in practice, we're seeing that the numbers are even higher. But huge amounts of people can be impacted. And a traditional incident response would say, okay, well, is the model available? Has its integrity been broken? Has anyone breached confidentiality? Is the data being used in line with privacy policies, like all the traditional questions, just don't get at this really, really huge liability.
[2619.38 → 2647.38] And so what can happen in practice is an organization will deploy a model like this. And then frequently, like the media will discover that there's something wrong, or there'll be like a Twitter posting saying like, what, wait a minute, you know, you know, I'm a member of a disadvantaged community. And you know, my spouse is not and the model treated us differently. And then suddenly, the sky is falling on these organizations. So anyway, so that model, I think, in itself, is a signal that something's broken.
[2647.38 → 2677.36] I can summarize my comments really quickly. Typical in computer incident response doesn't address machine learning security yet. And what we saw, it may soon in the future, but it doesn't yet. And then model risk management, typically not in all cases, typically doesn't address security and privacy, and in some cases, discrimination issues, like Andrew mentioned. And so there's just kind of a gap
[2677.36 → 2694.56] gap in the two main practices, which are both great, you know, we're not saying anything negative about these, they're both great, but they just have a little bit of a gap when it comes to AI. And so, you know, I think that that's where the AI incident response checklist comes in, because we tried to fill in those gaps.
[2694.56 → 2722.70] So we've kind of talked about the checklist itself. But one of the comments you made a little while ago was the time to connect with us is really before that happens. So if you're a company out there, and you have, you know, limited resources, limited budget, and you're trying to justify why they should engage you before an incident happens, to try to, you know, you know, work through their operations ahead of time,
[2722.70 → 2733.30] what are some good justifications? What are things that you've seen where you're like, if you come in ahead of time, you're going to save money, you're going to save a lot of heartache? How do you approach that?
[2733.84 → 2745.70] I'll try on this one. And Andrew can kind of jump in and correct me. So one, you know, all models are wrong, some models are useful, right? Your machine learning model is going to be wrong.
[2745.70 → 2772.68] Okay. And so when it's wrong, something bad can happen, right? And so the question is really, how prepared are you for that bad thing to happen? And what will the cost in terms of human value or monetary value be when that bad thing happens? So we try to sort of gauge AI incidents by the organization's preparedness, and by the materiality of the incident.
[2772.68 → 2801.96] And so your machine learning model will be wrong, right? So you just have to get ready for that. That's where I'll leave it, except to say that, in our experience, it's much cheaper and much easier to deal with it before you're on the front page of the New York Times before you have letters from senators, you know, it's a very reasonable expense. And companies are probably already budgeting for in their traditional sort of software budgets, whereas it can explode on the other side of the incident. As Andrew likes to say, on the right side of boom, the cost can explode, right?
[2801.96 → 2811.88] Because then you're talking about reputational problems, potential regulatory problems, potential litigation problems. So I'll let Andrew chime in and correct me if I'm wrong on the news.
[2811.88 → 2813.00] The right side of boom.
[2813.30 → 2813.48] Yeah.
[2813.58 → 2822.14] Yeah. Yeah. So we have, in the national security world, there's a left of boom, right of boom. Boom is the bad thing, and left is before, and right is after.
[2822.14 → 2843.58] And so, I mean, so your question, I think is one of the most frustrating parts of some of what we do. And I think in terms of folks in information security and data protection writ large, which is, there's kind of this intuition, well, if something bad hasn't happened already, why should I be spending time and money on it?
[2843.58 → 2861.12] And I think that is even worse in the world of AI, because AI is subject to so much hype. And we still see people who have this kind of belief, well, my AI could never be wrong. My data scientists are so expensive. They could never do. And honestly, it's just, it's a real problem.
[2861.12 → 2886.44] So what we typically say in practice to our clients who haven't yet had a bad thing happen, they're a precious few, is basically we say, well, there are two answers. One is you need to, like Patrick said, you need to at least be prepared for the bad thing to happen. You need to know what the bad thing is so that when it happens, it doesn't occur for a year until someone tweets about it, and then there's an investigation.
[2886.44 → 2908.58] So you need to be able to know what it is you want to avoid, how are you going to be looking for it and measuring it, and then what are you going to do when you measure it? And so those are kind of typically, that's like the starter package, you know, that's like really kind of like the baby steps and anyone, any organization deploying AI needs to have those things worked out.
[2908.58 → 2917.30] One, it's the right thing to do. And it's just like responsible. But two, it will save them from a world of hurt, if and when something goes wrong.
[2917.80 → 2930.72] The second thing that we say is that, honestly, just in terms of the financial resources, it just does not cost a lot of money to prepare, and it costs a huge amount of money to respond.
[2930.72 → 2938.54] And so on of the things that we'll do is we'll say, you know, you're investing in AI because you believe it's transformational, because you believe it has so much value.
[2939.04 → 2948.58] And the liability is directly tied to the value. You would not, you know, like the greater the value, the higher the chances that if something goes wrong, it's going to be big.
[2948.78 → 2959.58] And so you really can't separate the two. So if you believe that AI is worth investing in, and you believe it's going to change your business, it is just, one, I would say irresponsible.
[2959.58 → 2971.20] We don't tell that to clients. We typically don't, unless it's terrible. But it's just really misadvised and ill-advised to be putting, making such a big bet on something and kind of doing that blind.
[2971.48 → 2978.78] There's a quote that I love that I keep stealing from Patrick, which is that even microwaves have troubleshooting manuals.
[2978.78 → 2989.30] Something as small and as simple as a microwave. And yet AI is deployed in practice all over without troubleshooting manuals, without plans for what happens when something goes wrong.
[2989.82 → 2996.38] And so I think at minimum, there's just kind of this basic level of preparedness that organizations should be willing to invest in.
[2996.76 → 3002.36] And then hopefully they never have to pour money, you know, into a response. But it's a real issue.
[3002.36 → 3012.92] Yeah. And there's definitely, like, I can see, like, in this topic, people could also argue, well, like, I don't really know, I can't anticipate all the bad things that could happen.
[3012.92 → 3017.64] But at the same time, there are some, like, simple things that, like, you can't anticipate, right?
[3017.82 → 3023.92] Like, you can create adversarial examples pretty easily to, like, test the sensitivity and robustness of your model.
[3023.92 → 3031.90] Also, like, I think it was Andrew, you were talking about, like, when your model goes wrong and then, like, which users were impacted by this.
[3032.58 → 3038.06] Like, a lot of people just, like, throw their model up, like, model.PB on S3.
[3038.32 → 3043.16] And that's the name of it. And then when they update it, they just, like, overwrite that file, right?
[3043.28 → 3051.82] And, like, of course, that's going to create all sorts of amazingly terrible issues when you have to figure out something like what you were talking about.
[3051.82 → 3061.34] So even just, like, a simple thing like, hey, could it be conceivable that I would need to know which model operated on which data from users?
[3061.52 → 3063.98] Yeah, that's probably fairly conceivable.
[3064.20 → 3067.12] That's something I've seen, like, people tend to make that excuse, too.
[3067.58 → 3070.90] I'd really like to jump in here, and I'll try not to be too negative.
[3071.26 → 3076.30] You know, having spent four years in Silicon Valley, data scientists are paid a lot, okay?
[3076.44 → 3078.78] A lot more than, like, a general practitioner physician.
[3078.78 → 3091.48] And I'm starting to have sort of personal emotional problems with this idea of someone who makes 200, 300 grand a year saying, I can't think about how the system's going to fail, okay?
[3091.82 → 3097.90] Well, one, you know, just take some time and Google about it and see how systems like yours have failed, right?
[3097.94 → 3100.08] And just open the newspaper, right?
[3100.16 → 3104.88] There's evidence of discriminatory machine learning all over the news, right?
[3104.88 → 3113.18] So, again, I'll bring up this idea of studying AI incidents, much like people study airplane crashes and continue to study airplane crashes, right?
[3113.30 → 3120.02] And so I use the analogy of nuclear power plants or nuclear reactors and airplanes, and I know those aren't exactly right.
[3120.24 → 3122.08] The barrier to entry is a lot higher.
[3122.68 → 3124.54] The impact of a failure is a lot more immediate.
[3124.82 → 3126.38] But there are things to be learned there.
[3126.38 → 3132.10] And so, you know, we studied the ways that airplanes crash in an effort to make them safer.
[3132.40 → 3135.62] And that was just part of the profession of aviation.
[3136.46 → 3143.46] And I'm really personally becoming tired of sort of why data scientists would not have some kind of out for this.
[3143.58 → 3145.16] Like, oh, I get paid too much to do this.
[3145.28 → 3146.82] Like, that doesn't make any sense.
[3146.82 → 3160.34] So, I guess as we come to the conclusion today, I was wondering if you could kind of tell us as insiders at this juxtaposition of law and AI what you're expecting to see over the next few years.
[3160.60 → 3162.26] You know, clearly this is a new field.
[3162.48 → 3163.58] It's growing rapidly.
[3164.46 → 3170.04] What are you seeing, and what do you expect to grow into as you move forward with your new firm?
[3170.04 → 3179.62] Yeah, so I would say, and it's been interesting because we also kind of coming out of the gate have been in discussions with a whole host of regulators.
[3180.06 → 3186.32] I think, you know, there's a direct connection between the headlines about things happening when AI goes wrong.
[3186.62 → 3189.76] And those are only a fraction of what's actually happening out there.
[3190.10 → 3194.18] Then kind of public concern about this and then regulatory reaction.
[3194.18 → 3201.72] And so regulators are going to kind of up the ante, so to speak, in terms of what the liabilities are.
[3202.22 → 3204.76] And so I really see two futures.
[3205.26 → 3208.08] And they're both probably better than the one, you know, the present.
[3208.32 → 3215.54] I think the one that I'm gunning for and why Patrick and me, you know, launched this, the BNH.ai, this we keep offer,
[3215.54 → 3223.42] is because I think there's an opportunity for data scientists to work together with policy folks and legal folks and get this right
[3223.42 → 3226.10] and kind of be proactive rather than reactive.
[3226.36 → 3228.12] Our aim is to help that happen.
[3228.76 → 3235.84] So I think that's one future where before there's any really major incident, we kind of have this, I'm going to say community,
[3236.00 → 3236.86] but it's not really a community.
[3237.00 → 3241.44] It's not like a legal, but as a group can start to build out best practices.
[3241.44 → 3247.86] And even, Dan, what you were saying about just like documentation and like not overriding models when they're updated,
[3247.86 → 3255.24] or at least, you know, like just some basic best practices, I can see a future that is frankly a lot less bumpy
[3255.24 → 3259.52] and where maybe like the hype of AI can actually be, you know, be met in practice.
[3259.52 → 3267.22] I also see another future, which is probably most likely, and I think what kind of Patrick's like frustration is indicative of,
[3267.52 → 3273.06] is where regulators just say, this is not good enough and kind of slap down some much more stringent standards.
[3273.24 → 3277.16] That's where things appear to be heading, although it's not inevitable.
[3277.16 → 3282.58] But if I had to guess, I would say kind of just like we were with, you know, frankly, I was going to say GDPR,
[3282.66 → 3284.70] but I think CCPA is a little bit more stringent.
[3284.70 → 3294.62] And CCPA is this very overbearing privacy regulation that came through California that now basically affects almost any big organization using data in the U.S.
[3294.74 → 3300.28] I think the likelihood, if we're not careful, is that there is going to be the same type of thing.
[3300.28 → 3305.68] And then every single data scientist is going to have, you know, specific additional trainings,
[3305.68 → 3310.84] and they're going to have specific additional forms, and they're going to have kind of lawyers breathing down their neck
[3310.84 → 3315.48] who might not necessarily kind of fully understand all the nuances of their day-to-day.
[3315.62 → 3319.68] So I think no matter what, the life of a data scientist is going to change.
[3320.30 → 3321.24] Risks are increasing.
[3321.58 → 3326.52] It's going to be harder just to deploy models without illustrating how those risks have been reduced.
[3326.64 → 3330.40] And I think how that happens is really kind of up to us.
[3330.40 → 3334.32] And I think smart companies, you know, I'm obviously biased, but I think smart companies and organizations,
[3334.32 → 3340.68] I think will start to think about this stuff now so that they're not surprised when all this happens.
[3340.84 → 3341.32] For sure.
[3341.68 → 3345.48] Yeah, sadly, I think I'm more aligned with Andrew's sort of second scenario.
[3345.82 → 3355.24] I think we're in for a bumpy road where AI and ML are on a collision course with the law over the next, I don't know, decade or two.
[3355.24 → 3361.36] I think it's important to mention, you know, in this topic that we see government agencies internationally, of course,
[3361.52 → 3366.22] Singapore, UK, all over Europe issuing very detailed AI guidance.
[3366.22 → 3378.28] But we also in the U.S. just this year and end of last year saw FTC, CFTC, CFPB, FDA, and probably several more that I can't remember off the top of my head,
[3378.38 → 3383.08] sort of releasing draft guidance or other sort of steps towards regulation.
[3383.28 → 3387.16] So I do think sort of regulation is imminent.
[3387.56 → 3390.10] And sadly, I expected to kind of be a bumpy road.
[3390.20 → 3393.02] But I hope Andrew's first scenario is what actually happens.
[3393.10 → 3395.12] That's certainly, that would be a more pleasant scenario.
[3395.12 → 3402.98] Yeah, hopefully we've got a good number of listeners on this episode who are interested in the practicalities of this.
[3403.06 → 3409.08] And I think this is super practical in the sense that, you know, hey, this is a call to our listeners.
[3409.08 → 3416.10] Before we go down that second path, let's take stock of what we're doing and institute some responsible practices in our own workflows.
[3416.48 → 3419.58] You know, there's simple things like we were talking about that you can do.
[3419.58 → 3426.62] I've taken down the links that we've been chatting about, you know, super practical things that we'll link in the show notes.
[3426.62 → 3436.48] Specifically, there's a great page that BNH.ai has put together with a lot of links contained in that page and the AI incident response checklist.
[3436.48 → 3438.74] We'll include that right at the top of our show notes.
[3438.90 → 3443.58] So definitely check that out and take stock of, you know, how your organization is approaching this.
[3443.66 → 3448.06] And hopefully we can follow that former happier path as practitioners.
[3448.06 → 3450.10] So, yeah, definitely check that out.
[3450.24 → 3452.64] Thank you both, Patrick and Andrew, for joining us.
[3452.68 → 3455.52] This has been fascinating and really important discussion.
[3455.78 → 3460.22] So we appreciate that and wish you luck with the new firm and all the great things you're doing.
[3460.46 → 3461.20] Well, thank you so much.
[3461.26 → 3463.88] It's been fun as always, and I hope it's been helpful for your discussion.
[3464.12 → 3465.10] Yeah, thanks for having me.
[3465.24 → 3466.14] This was a fun discussion.
[3466.14 → 3474.58] Do you have questions, praise, or constructive criticism about the conversation you just heard?
[3475.12 → 3479.90] Comment on this and every episode of Practical AI on changelog.com.
[3480.42 → 3486.04] Just open your show notes, follow to discuss on changelog news link, and let your voice be heard.
[3488.08 → 3491.30] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3491.76 → 3493.18] It's produced by Jared Santo.
[3493.52 → 3494.00] That's me.
[3494.00 → 3497.04] And our music is provided by the mysterious Break master Cylinder.
[3497.92 → 3500.12] We're brought to you by some amazing sponsors.
[3500.34 → 3502.84] Special thanks to Vastly, Linde, and Rollbar.
[3503.16 → 3507.24] And a special shout out to those listening on our ad-free changelog++ feed.
[3507.72 → 3509.28] If that's you, you're awesome.
[3509.62 → 3511.74] If that's not you, well, you're awesome too.
[3512.04 → 3515.24] But you can learn all about it at changelog.com slash plus.
[3516.26 → 3517.32] That's all for now.
[3517.60 → 3518.98] We'll talk to you again next week.
[3524.00 → 3525.16] Take care.
[3525.16 → 3525.60] Critic.
[3527.72 → 3528.08] Bye.
[3528.10 → 3528.48] Bye.
[3528.48 → 3528.56] Bye.
[3530.20 → 3531.52] Bye.
[3533.96 → 3534.30] Bye.
[3534.30 → 3534.40] Bye.
[3534.40 → 3534.74] Bye.
[3535.50 → 3536.06] Bye.
[3536.22 → 3537.02] Bye.
[3537.46 → 3538.36] Bye.
[3538.42 → 3538.44] Bye.
[3538.44 → 3538.46] Bye.
[3538.84 → 3538.88] Bye.
[3538.94 → 3539.54] Bye.
[3539.78 → 3539.98] Bye.
[3540.06 → 3540.58] Bye.
[3541.88 → 3542.50] Bye.
[3542.50 → 3542.66] Bye.
[3542.76 → 3543.26] Bye.
[3543.42 → 3544.66] Bye.
[3544.66 → 3544.82] Bye.
[3551.74 → 3552.40] Bye.
