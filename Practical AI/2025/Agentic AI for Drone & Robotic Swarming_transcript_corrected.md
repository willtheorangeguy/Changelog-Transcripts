[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.18 → 37.50] Now, on to the show.
[48.74 → 53.82] Welcome to another fully connected episode of the Practical AI Podcast.
[53.82 → 60.20] In these episodes where we don't have a guest, it's just Chris and me, we take some time to
[60.20 → 66.60] deep dive into some interesting AI topics or explore some things in the news related to
[66.60 → 73.22] AI and hopefully give you a little bit of learning resources or information to help you level
[73.22 → 75.28] up your machine learning or AI game.
[75.88 → 76.78] I'm Daniel Whiten ack.
[76.78 → 82.84] I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[82.84 → 86.42] a principal AI research engineer at Lockheed Martin.
[86.66 → 87.36] How are you doing, Chris?
[87.58 → 88.76] Hey, doing great today, Daniel.
[88.84 → 89.42] How are you today?
[89.80 → 90.92] I'm doing well.
[91.08 → 97.62] Yeah, I just took a tried to take a run before it gets really, really hot here.
[98.24 → 101.70] So hopefully, you know, that worked out well.
[101.76 → 102.98] It was still kind of hot.
[103.10 → 104.78] Hopefully, I don't end up with a sunburn, but...
[104.78 → 106.10] Absolutely.
[106.48 → 111.72] Yeah, it's been hot here in the US, especially in the southern US where we both are right
[111.72 → 112.10] now.
[112.64 → 119.68] And so, yeah, you definitely don't need you collapsing from heat exhaustion right before
[119.68 → 120.78] we get into a show here.
[121.54 → 122.62] Yeah, yeah, for sure.
[122.76 → 125.38] I will definitely say there's fewer people out.
[125.60 → 131.62] There was not in any way a swarm of people running anywhere that I saw.
[131.62 → 138.66] So yeah, I guess that leads a little bit into what you teed me up to talk about today, Chris,
[138.70 → 145.88] which I'm excited about, which is an area of your expertise and interest, which is swarming,
[146.12 → 148.70] which I guess could be related.
[149.08 → 154.88] You know, people might be thinking of animal swarming, robot swarming, other swarming.
[155.10 → 156.54] Maybe just starting there.
[157.10 → 158.58] What do we mean by swarming?
[158.58 → 166.54] So before I get into that from my side, let me set that up a little bit because you actually
[166.54 → 172.98] mentioned several things that knowing me and also just the general topic as we've kind
[172.98 → 176.58] of prepped to do this a little bit, you mentioned animal swarming.
[176.94 → 178.36] And so it's funny.
[178.52 → 185.76] In the AI world, we have been talking about robotics and autonomy and unmanned aerial and
[185.76 → 187.82] ground vehicles for various things.
[188.02 → 193.50] You hear about Amazon drones and Walmart drones are out there now and various other applications.
[193.84 → 199.78] And so even though my background may be in the in kind of military applications, because
[199.78 → 203.18] I'm in the defence industry, we're really talking about it in a general say.
[203.30 → 209.60] And one thing I should say up front just to cover myself is I'm only representing my only
[209.60 → 214.84] my own personal viewpoint and not that of my employer or any other organization.
[215.40 → 215.88] Point taken.
[216.06 → 221.02] Point taken, which is kind of funny because when you talk about swarming, if you put 10
[221.02 → 226.18] people into a room and ask them each to define swarming, you will end up with about 17 different
[226.18 → 228.56] definitions of what swarming is.
[228.72 → 230.70] It's one of those types of terms.
[230.70 → 237.36] Yeah, you mentioned the delivery drones around where I'm at.
[237.46 → 239.84] I'm I live right by Purdue University.
[239.84 → 249.82] And actually, for quite a few years now, we've had these little box robots that will
[249.82 → 251.30] deliver you food.
[251.30 → 256.94] So they like drive along the sidewalks and, you know, go through intersections and deliver
[256.94 → 261.38] food to you through an app and all that stuff.
[261.54 → 265.38] So that one definitely hits a little bit close to home.
[265.66 → 273.70] I think for the most part, I have seen them, you know, successfully navigate the terrain and
[273.70 → 275.44] and intersections and all of that.
[275.44 → 278.84] Although I will say I did see one at one point.
[279.04 → 284.22] I didn't see the collision, but it was definitely run over on the road.
[284.34 → 286.64] It was in pieces at an intersection.
[286.94 → 289.50] Yeah, somebody didn't get their dinner that night.
[289.80 → 290.52] Yeah, exactly.
[290.92 → 292.04] Somebody called up hungry.
[292.24 → 292.98] Where's my food?
[293.16 → 297.78] You know, which, you know, and it was the delivery driver once upon a time.
[297.86 → 299.50] Hopefully that person would not have gotten hit.
[299.56 → 304.40] But yes, having the some sort of automated vehicle bringing the stuff.
[305.34 → 309.72] So wanted to talk a little bit about it and probably before we get into, you know, talking
[309.72 → 314.90] about what swarming is kind of distinguishing it because it's one of those autonomy words.
[314.90 → 317.84] And, you know, autonomy is another one of those words.
[317.84 → 326.00] And we have things like drone and robot and UAV, UGV, UV, X covering kind of all the things.
[326.18 → 328.44] And so I don't know what a lot of those things are.
[328.44 → 332.12] OK, so ground sky.
[332.38 → 334.26] You got a ground air.
[334.44 → 334.66] Yes.
[334.90 → 342.84] So like UV would be unmanned or unscrewed is a little bit more modern term for it.
[342.88 → 347.24] The X signifies kind of what the domain it's operating in, air, ground, whatever.
[347.62 → 348.40] And then vehicle.
[348.40 → 355.28] And if you've seen UX, S, that would be an unmanned or unscrewed whatever system.
[355.78 → 357.68] And so those are really common lingo things.
[357.80 → 359.04] And they're not specific to military.
[359.30 → 362.74] You see those in commercial and industrial applications and stuff.
[362.84 → 371.02] And for the most part, we'll probably for simplicity's sake, mostly talk about drones to in this conversation.
[371.02 → 376.70] We tend to stay away from jargon and maybe robots, you know, for ground stuff.
[376.80 → 382.70] And that way people are not trying to get through acronyms while we're talking and stuff just to simplify things a bit.
[382.94 → 400.10] But we're having that we're definitely living in this age, as you just pointed out from personal experience, where we're we're starting to see these things, which are, you know, physical embodiments of some sort of AI or other algorithmic driven, you know, movement around the physical world for various activities and stuff.
[400.10 → 409.36] And it sounds like, and I don't know the specific technology for the one that's bringing you the food on how they're how they're approaching that, because there are a bunch of different approaches.
[409.36 → 417.98] But that is an either a semi-autonomous, presumably, or fully autonomous, you know, ground vehicle that's bringing you the stuff.
[418.58 → 424.06] Whereas going back to our topic, swarming implies numbers, first.
[424.26 → 426.94] And so, but it doesn't just imply numbers.
[426.94 → 430.66] It implies the way numbers are working together and collaborating.
[431.20 → 435.34] And I think that's where a lot of people get in trouble with all sorts of different definitions.
[435.34 → 438.98] And it's super popular to talk about swarming now.
[439.56 → 441.76] Yeah, it's a crazy buzzword these days.
[442.14 → 445.70] Yeah, I almost wonder, like, there could be some confusion.
[445.70 → 451.12] We hear a lot of talk these days about multi-agent systems.
[451.12 → 459.86] And, of course, we've had episodes where we discuss agents specifically and what that term agents mean.
[460.00 → 466.40] But as soon as you as soon as you bring in that kind of multi-agent side, people might be confused.
[466.62 → 467.98] Is that what we're talking about?
[467.98 → 484.62] So I guess one question would be, like, swarming, does it imply, like, physical, I guess, physical AI or physical autonomy in terms of things that are operating in the physical world, not the digital world?
[484.70 → 488.52] We've talked a lot about drones and robots in the beginning of this.
[488.52 → 492.66] So is that part of that definition or not really?
[492.92 → 493.14] It is.
[493.46 → 493.68] Okay.
[493.86 → 494.36] It is.
[494.36 → 509.52] And we've had, across a lot of our episodes recently, especially our fully connected episodes like this, where it's you and I discussing a topic, we've talked about, we've had over the history of the show, we've seen the evolution of AI.
[509.96 → 512.46] And there tend to be specific topics that get really hot.
[512.46 → 514.44] And right now, agents are really hot.
[514.70 → 526.00] But there's also the notion of agents applying themselves in collaboration with various other AI technologies, whether they be LLMs or reinforcement learning or computer vision.
[526.80 → 535.26] And I think if you take a step farther into this world of autonomy, especially modern autonomy in 2025, agents are a big part of that.
[535.26 → 541.86] And having multiple agents collaborating, and they're using these other models to get these tasks done.
[541.86 → 545.08] So you have agents operating with LLMs for different purposes.
[545.50 → 550.10] And so you're able to go and grab the right model for the right task.
[550.10 → 556.80] And you're putting a bunch of tasks together to go do something which I might call a mission.
[556.80 → 560.08] But I don't necessarily mean that in a military-issue way.
[560.34 → 560.92] Could be.
[561.24 → 567.04] But it could be something that is what the purpose of your company's autonomy is to do.
[567.04 → 570.76] Maybe like a goal or an objective or outcome.
[570.98 → 571.50] That's right.
[571.50 → 572.64] Could be synonyms.
[572.90 → 573.00] Maybe.
[573.12 → 573.38] That's right.
[573.60 → 575.80] I'm not that great at the English language.
[576.10 → 579.60] But those are all loose synonyms that could apply.
[579.96 → 580.08] Yeah.
[580.30 → 582.32] And so we're seeing this.
[582.54 → 590.60] We're seeing these individual drones and robots that are starting to do tasks in the commercial and industrial space.
[590.60 → 594.50] Certainly, it's been that way in the industrial space and warehouses and robots.
[594.50 → 602.64] I guess the first robot I worked on was 2000 that personally I was doing were two of them that were autonomous in 2018.
[602.64 → 604.60] So this is not new in that capacity.
[604.60 → 607.42] How it's doing it has changed over time.
[607.42 → 607.90] Yeah.
[607.90 → 619.68] Maybe just taking a moment kind of looking back a little bit because I remember what year was it that the...
[619.68 → 625.18] I forget the year of the Beijing Olympics when they had the...
[625.18 → 630.28] It was the first one I had seen where they had a kind of...
[630.28 → 631.74] I guess we could call it a swarm.
[631.86 → 632.26] I don't know.
[632.60 → 633.78] You can correct me if I'm wrong.
[634.02 → 639.28] Swarm of drones that were sort of in the sky in the...
[639.28 → 641.34] I guess I think it was the opening ceremony.
[641.50 → 642.66] I'm trying to remember.
[642.66 → 644.46] But that was the first time I had seen that.
[644.56 → 647.92] Of course, I've seen it in other places after that.
[648.66 → 651.58] But yeah, what's kind of the...
[651.58 → 652.72] The definitions, right?
[652.72 → 653.12] Yeah.
[653.26 → 660.72] Well, how would you represent the history of kind of coming to the point where we're at now in these...
[661.46 → 662.72] So I'm getting from you.
[662.84 → 664.72] There's these autonomous...
[664.72 → 679.82] So multiple objects in the physical world that are autonomous or multiple vehicles or robots or whatever in the physical world that are autonomous trying to accomplish a goal or mission.
[680.02 → 683.16] Now, in the Beijing case, I don't know if those were autonomous or not.
[683.52 → 686.72] But yeah, help me kind of parse through maybe a little bit of that.
[687.12 → 691.52] So I should say ahead of time that I don't have any special knowledge of that particular configuration.
[691.52 → 694.88] So I'm making educated guesses on that.
[695.02 → 698.36] And so I would suggest that's not what I...
[698.36 → 700.66] And I'll define a swarm in a moment as a follow-up.
[700.74 → 702.44] But I would not call that a swarm.
[702.54 → 712.12] I would call that many individual aerial platforms that are operating in a predetermined, coordinated manner.
[712.36 → 713.72] Yeah, it's like synchronized droning.
[713.72 → 716.82] They're synchronized from the ground control system.
[716.82 → 724.60] So a notion in flying autonomous vehicles is that you have a ground control station, which might be like a laptop.
[724.92 → 727.38] It might be a bigger thing inside a truck or something.
[727.38 → 730.96] But it has comes, and it has ways of communicating.
[731.28 → 736.84] And so for shows like that, you would use things like GPS.
[736.84 → 744.80] And each drone would have a three-dimensional path that it's following that's a little bit different from all the others.
[744.96 → 749.06] But when you put them all up there at the same time, they look like a big coordinated show.
[749.16 → 751.16] But they're not actually coordinated.
[751.80 → 754.82] It's the human on the ground programming in their path.
[755.26 → 758.80] They are not determining their coordination.
[759.22 → 761.10] There you go, which is really important.
[761.76 → 764.08] So you went right to the heart of it.
[764.08 → 769.62] And so there is that, which is really not intelligent at all.
[769.68 → 771.98] It's pre-programming these drones to do something.
[772.10 → 776.16] And the visual impact is that you have this thing happening among a bunch of things.
[776.22 → 777.58] But it's sort of an illusion.
[777.72 → 780.20] It's really a bunch of individual things on their path.
[780.76 → 785.98] And then there's a whole continuum of how this kind of vehicles can operate.
[785.98 → 803.86] One kind of popular approach today that a lot of people would call swarming, and which I don't, and I'll define it right after I say this, is the notion of giving plays to a group of vehicles that go out and do a task.
[803.86 → 807.12] Sort of like some people, the analogy would be a football play.
[807.54 → 809.84] Go to this location and do this.
[809.98 → 816.68] And there might be some communication with the other platforms in your area that you're doing something with.
[817.04 → 820.10] But I also don't consider that a swarm.
[820.34 → 824.94] Because I think it comes back to the notion of what is swarming.
[825.46 → 828.20] Swarming is not an autonomous thing.
[828.28 → 830.14] It's a type of behaviour exhibited.
[830.14 → 832.80] And we see that in nature.
[833.64 → 836.72] And so I will give the definition.
[837.02 → 843.64] And then I'm actually going to go away from technology for one second and talk about what we see in Mother Nature that's kind of consistent with that.
[843.90 → 849.34] So my definition sounds a little military-like, but don't take it too much that way.
[850.00 → 853.72] It can easily be applied to commercial or industrial.
[854.58 → 857.94] But I think it gets the gist of how I see swarming.
[857.94 → 859.26] Mine is,
[859.44 → 871.28] Swarming occurs when numerous independent, fully autonomous platforms exhibit highly coordinated locomotive behaviours in any domain, be it air, ground, sea, undersea, or space,
[871.28 → 892.60] functioning as a single, independent, logical, distributed, decentralized decisioning entity for purposes of command, control, and communications with human operators on the loop to implement actions that can achieve strategic, tactical, or operational effects in the furtherance of a mission.
[892.60 → 898.58] A little military sounding, but if you translate those words into commercial and industrial, they still apply.
[898.72 → 901.44] You might choose a synonym in some of those areas.
[902.10 → 906.38] But that is a pretty high bar right there.
[906.38 → 918.38] And as we go forward, we can talk a little bit about kind of what in that definition turns something from a collection of autonomous vehicles into a swarm of autonomous vehicles.
[918.38 → 940.02] Well, friends, if you want to build the future of multi-agent software, check out Agency.
[940.20 → 942.78] That's A-G-N-T-C-Y.
[942.94 → 946.46] It's an open source collective building the internet of agents.
[946.46 → 952.90] It is a global collaboration layer where AI agents can discover, connect, and work across frameworks.
[953.34 → 961.76] That means better tools for you, standardized agent discovery, seamless interagent communication, and modular components to scale your multi-agent workflows.
[962.34 → 971.82] And they're teaming up with Crew AI, Lang chain, Cisco, and many more, dropping real code, specs, and services with no strings attached.
[971.82 → 975.72] Start building alongside engineers who care about high-quality multi-agent software.
[976.26 → 977.82] Learn more at agency.org.
[978.58 → 981.80] Again, that's A-G-N-T-C-Y.org.
[981.88 → 983.84] That's agency.org.
[983.84 → 991.32] Well, Chris, I really appreciate your definition.
[991.74 → 999.76] Maybe that's even something we can pull out and put into the show notes for people so that they can read that if they want to.
[999.76 → 1011.54] I'm actually reminded as we're talking about this and as I'm hearing your definition of these things in the animal kingdom.
[1012.04 → 1018.32] Actually, I'm remembering a movie that I watched with my wife, The Murmuring.
[1018.32 → 1033.24] I think it was on Netflix and very interesting movie, but kind of at the core of the movie were these, I don't know if I'm using the right terminology, but murmurations of swarms of birds.
[1033.60 → 1035.24] Starlings, you're famous for it.
[1035.70 → 1036.10] Exactly.
[1036.10 → 1036.50] Yeah.
[1036.58 → 1051.50] So you can see in the sky, I'm sure many people have seen this, swarms of birds that almost form kind of patterns and synchronizations in the sky and move around together.
[1051.50 → 1056.74] Now, according to your definition, each of those birds, right?
[1057.24 → 1079.64] Now, I guess in this sense, there's no connection to obviously a human command and control type of scenario, but certainly they are autonomous, but they're accomplishing something together, which is maybe a little bit mysterious in this case, although I'm sure it's a topic of study.
[1079.64 → 1086.58] But yeah, that's what came to my mind is that movie and that kind of phenomenon.
[1087.24 → 1087.34] Yeah.
[1087.54 → 1099.82] And that formulation, if you will, is literally, it's called flocking in that case, which is obviously a bird term, but that is definitely consistent with what I would consider to be a swarm.
[1100.16 → 1108.20] And if you break that down, and there are other animals we can talk about to that have different types of swarming behaviour, but that are consistent with that.
[1108.20 → 1120.84] If you talk about starlings in particular, you know, they're beautiful when you see those massive, and there could be thousands of starlings moving across, and you see the waves within the system, you know, within the flock as they're doing that.
[1120.84 → 1124.80] And so you kind of go, you know, what's going on there?
[1124.88 → 1131.98] We have thousands of individual beings that are communicating and sensing each other.
[1132.40 → 1134.40] They have a unified purpose.
[1134.56 → 1136.36] They're all going someplace together.
[1136.36 → 1144.22] But there's no one master general or CEO starling that's going, you guys are going to go that way.
[1144.42 → 1146.02] Everyone do what I tell you to do.
[1146.22 → 1148.96] They are all subscribing to the mission, if you will.
[1149.28 → 1155.98] But each one has a position, if you will, or a place in that mission where they are communicating.
[1155.98 → 1165.58] And the way they do their sensing of each other and their communications helps them, A, not collide and, you know, fail through collisions and such.
[1166.04 → 1167.14] It keeps them together.
[1167.50 → 1173.72] But they also have a way of agreeing, if you will, to go do something.
[1174.00 → 1177.60] They're going to move from one place on the Earth to another place on the Earth.
[1177.60 → 1189.78] And that kind of comes down to the crux of it is that swarm behaviour is where you have that a bunch of fully autonomous beings, in this case.
[1190.02 → 1198.72] They're functioning in that formulation as a single, independent, logical, distributed, decentralized decisioning entity.
[1198.94 → 1204.24] It's a long mouthful that I use because all of those have a part in that describing it.
[1204.24 → 1206.04] But they're all working together in that way.
[1206.04 → 1209.00] Do you want to pick apart maybe each of those words?
[1209.26 → 1214.94] So, like, why use those multiple words, kind of distributed, decentralized?
[1215.24 → 1220.32] Some people might kind of not know why each of those is important.
[1221.10 → 1221.24] Sure.
[1221.50 → 1233.96] So, single implies that the joint actions together about how they're communicating and sensing give a rise to one generalized process.
[1233.96 → 1237.00] Kind of emergent or combined process.
[1237.00 → 1238.22] That's a great way of putting it.
[1238.42 → 1244.40] And that's kind of that emergent, you know, we said mission or goal kind of thing is coming out of that.
[1244.76 → 1248.36] And that process is independent of any one bird.
[1248.60 → 1255.96] And it's independent of any controlling authority that's saying, from afar, you all, she'll go do this thing, you know.
[1255.96 → 1258.52] And so, you have that independence.
[1258.92 → 1260.96] You have that single emergent characteristic.
[1262.12 → 1275.10] Logical meaning, it's also kind of, it's kind of think about, it's arising an emergent, intelligent notion or a processing notion that's all happening by the unity.
[1275.10 → 1279.58] It is distributed across the entire flock or formulation.
[1280.18 → 1281.28] It is decentralized.
[1281.70 → 1287.86] There's no one special bird or group of special birds that are the birds that are in charge of everybody else.
[1287.94 → 1289.28] And you guys have to do what we say.
[1289.60 → 1298.18] And finally, it's a decisioning entity that by this emerging thing happening, choices are made collectively for the whole thing.
[1298.28 → 1302.98] And yet, no one bird is saying, everyone's going to go do this thing.
[1302.98 → 1312.72] So, it's all this kind of characteristics about that emergent, I may add the word emergent into the definition that I have there because I think that's really a great way of describing that.
[1313.16 → 1315.86] But it's that unified collection to do this.
[1315.96 → 1324.66] Now, that's a far cry from what we're currently doing in the autonomy space at large.
[1324.66 → 1333.70] I'm not saying that doesn't exist in little pockets, academic pockets and other places, labs, whether they be government labs or university labs and stuff like that.
[1333.70 → 1343.94] But you don't see widespread deployment of drones or robots that are acting in this manner as we sit here recording today.
[1344.40 → 1344.46] Okay.
[1344.64 → 1345.66] That makes sense.
[1345.66 → 1346.06] Yes.
[1346.06 → 1346.10] Yeah.
[1346.68 → 1347.24] Yeah.
[1347.24 → 1363.24] Part of what I'm thinking and my questioning in my mind, which maybe you're going to get to as you kind of get through some of these things is obviously we have a kind of inspiration or a model there from the animal kingdom.
[1363.24 → 1381.68] In the case of, let's say, robots in a warehouse or a manufacturing facility or autonomous vehicles, we have in probably things that people are familiar with, the idea of self-driving things or autonomy.
[1381.68 → 1385.26] So like the Waymo cars or that sort of thing.
[1385.90 → 1397.20] And there's certainly obviously AI at play there in terms of computer vision and maybe reinforcement learning and decision-making.
[1397.20 → 1416.94] So assuming that people might know at least or be exposed to that in terms of the connection to AI specifically, what about this kind of swarming or robots or these entities working together to do a task?
[1416.94 → 1430.90] What is necessary for AI to do in that swarming scenario that's not necessary in just a single self-driving car, like a Waymo car or something like that?
[1431.00 → 1431.80] That's a great question.
[1432.08 → 1433.34] There's a lot of nuance there.
[1433.34 → 1450.22] So the self-driving car is having to navigate an environment in which it's both sensing and to some degree communicating potentially, although that is evolving over time, with other actors in that environment around it.
[1450.50 → 1453.20] And there is emergent behaviour on what to do.
[1453.56 → 1462.70] There's kind of the classic cases of kids playing on the sidewalk and the ball bounces into the street and reacting to various unexpected events like that.
[1462.70 → 1473.70] But at the end of the day, that vehicle is still, which may be fully autonomous, is still only having to decision on its own behalf.
[1473.94 → 1487.86] And so it has an onboard inference system, the onboard computers, the onboard models, or potentially that in combination with some remote that it's doing over some sort of connection, radio connection or cellular connection.
[1488.34 → 1491.00] But it's still decisioning for itself.
[1491.00 → 1507.52] The difference, according to my definition of a swarm, is that the emergent quality of the decisioning is arising from participation in many of the platforms that are participating in that unified mission or activity.
[1507.52 → 1537.50] But it has to decide for all of them.
[1537.50 → 1543.08] The difference, according to the difference, is that the difference, is that the difference that's happening across the swarm to get an activity accomplished?
[1543.58 → 1544.96] Does that clarify a little bit?
[1544.96 → 1546.08] Yeah, that helps.
[1547.08 → 1551.94] And I'm trying, maybe this is the decentralized part of what you're talking about.
[1551.94 → 1570.38] But part of maybe what is a challenge in my mind to think about is how such a thing would happen without a central kind of, so to say like, oh, let's just take a very simple, maybe it's simple.
[1570.38 → 1573.68] In my mind, it seems complex as well.
[1573.76 → 1580.46] But we have 20 robots in a manufacturing facility trying to do something.
[1580.46 → 1595.60] In one model, I could see where each of those robots detects certain things on a number of sensors, maybe cameras or temperature sensors or force sensors or something like that.
[1596.22 → 1600.70] All of that is communicated back to a central processing system.
[1600.70 → 1609.70] And it's really the single entity, the kind of master brain that makes the decision and communicates out a next step to all the robots.
[1610.04 → 1615.66] But in the decentralized way, you talked about how there's not this kind of central.
[1616.06 → 1620.14] There may be a central command where maybe there's oversight or something.
[1620.70 → 1624.68] But things somehow happen in a decentralized way.
[1624.76 → 1627.28] That's what I'm trying to connect in my brain, maybe.
[1627.28 → 1629.54] No, that's a great nuance that you're pointing out there.
[1629.72 → 1634.70] So in the warehouse, that's not really that's definitely a centralized environment.
[1634.70 → 1647.26] And you don't even have to have on board compute for that because your robots can have a highly reliable system of communication over Wi-Fi, you know, with a master server that's there.
[1647.26 → 1654.24] And you're in the distances involved or close enough to where you can have them interact with each other without having to do that.
[1654.24 → 1664.18] And according to the definition of the swarm that we're using here, that would not be a swarm, even though you may have many platforms working collaboratively.
[1664.32 → 1667.62] They're being controlled by a local centralized agent.
[1668.56 → 1676.28] And in swarming generally, according to this definition, you're really looking at an environment where that's not possible.
[1676.28 → 1690.14] You're looking, you know, what we would traditionally call edge or, you know, far edge is another term that will be able to use basically where you can't count on either local or cloud environments to provide to compute.
[1690.30 → 1696.88] And so you have to have to compute on board, including all the activities that will arise from that compute.
[1696.88 → 1726.86] Yeah, I'm almost imagining moving still kind of in my mind, living in the industrial world, if I think more to like oil and gas and like certain of the environments that are part of working in that industry, whether it be deep under the ocean or in very disconnected, remote places where you might not even want to or even could.
[1726.86 → 1729.70] expose humans to those environments.
[1729.70 → 1730.04] That's right.
[1730.14 → 1736.00] But they're also very hard in terms of connectivity and that sort of thing.
[1736.08 → 1739.18] You might want to accomplish tasks in that sort of environment.
[1739.30 → 1741.32] Am I getting to the right kind of scenarios?
[1741.78 → 1756.14] Like one good one that is commonly used is the notion of disaster recovery, where you might go into an area that is geographic, you know, it may be geographically remote or may not be.
[1756.14 → 1761.66] But either way, the infrastructure has likely things have happened with the infrastructure to where things have been torn down.
[1761.78 → 1764.14] You don't have cell towers, things like that.
[1764.14 → 1769.36] And you don't have the level of connectivity necessary for centralized control.
[1769.36 → 1786.82] And so if you're thinking about disaster recovery in a swarm context, you or you do not have that infrastructure in place to guide those, then you could put drones or robots on the ground that have their own inference capability.
[1786.82 → 1799.58] And if you're approaching it with that decisioning entity that is decentralized that I've described, then that could occur where they're actually working collaboratively to save lives.
[1799.58 → 1812.72] You know if it's is there are buildings in rubble, they're, you know, one robot that has that ability as maybe pulling rubble off because it has that capability, while others that specialize in getting down between the rubble and they're smaller.
[1812.72 → 1816.78] It might be in other words, not all robots may be the same.
[1816.86 → 1823.22] You might have a heterogeneous mix of robots with different capabilities, but they're able to dynamically go.
[1823.22 → 1830.86] So here's a rock, and it needs to be moved while you go under the rock, you other platform go under the rock looking for a survivor there.
[1831.38 → 1837.92] And so you can have a collection of robots that each has an optimal function.
[1837.92 → 1838.32] Yeah.
[1838.40 → 1842.82] Where they're working together to do something and ultimately save a life.
[1842.82 → 1851.70] And you don't have, you know, maybe you've had a hurricane come through or tornadoes, and you don't have the normal digital infrastructure that we're all so used to today.
[1851.70 → 1873.88] Well, Chris, that is really helpful to break down maybe some of the use cases or scenarios that maybe compare and contrast multiple agents or robots or systems that are working in an environment that maybe are in a swarm or are not in a swarm.
[1874.84 → 1879.92] Maybe part of so that that's helpful on the use case front.
[1879.92 → 1894.90] My mind is still kind of wondering on this side of the AI side, what unique AI problems are unique to the swarm environment that aren't encountered elsewhere?
[1895.46 → 1905.34] And how do those map to kind of maybe open challenges that are open or kind of maybe known models that are able to handle certain of these things?
[1905.34 → 1910.70] Yeah. So there's I mean, I think you just kind of alluded to the complexity involved.
[1910.86 → 1931.56] And I think the reason we haven't had swarms before now and that they are still something that that is emerging within what is being developed is because not all the technologies and models that you would need have been mature enough up until this point in time to be able to do that.
[1931.56 → 1939.58] So there are a lot of pieces. And some of that is on is operating in a physical environment.
[1939.58 → 1948.50] And so on the AI side, you know, over the years, we've talked about these different architectures, you know, of different models with different purposes.
[1948.50 → 1975.42] And swarming ends up taking quite a few of those and making them available to agents so that you can within a complicated physical environment, different agents on platform are working with each other to accomplish the on platform parts and then be able to communicate and coordinate that with other platforms that also each are multi-agent, multimodal configurations.
[1975.42 → 1978.42] And so and then being able to do swarm of swarms.
[1979.24 → 1998.42] Yeah, sort of like if you think of all the various technologies that go into just a single platform able to do that, we're only now really getting, you know, in the large getting to where these kinds of things are possible and where to compute is powerful enough for edge devices and that the models are being reduced.
[1998.42 → 2003.86] We've talked a lot over the last year or two about how models are getting smaller, and you get a hugging face.
[2004.00 → 2009.70] And, you know, the vast majority of models, they're very small models that are useful in a lot of specific tasks.
[2009.70 → 2025.70] And so you have to match up small models that can run on edge inference or even CPUs to do various tasks for specific agents and coordinate that with sensors and comes to be able to accomplish stuff.
[2025.70 → 2027.70] So it's quite complicated.
[2028.02 → 2033.52] And that kind of, and I use this kind of in air quotes, that kind of miniaturization of the technology.
[2033.64 → 2046.02] I don't mean physical miniaturizations, but kind of getting everything to work and run on a remote edge device that is likely battery powered is a bit of a challenge.
[2046.02 → 2053.86] So I think as we look forward right now, there's you know, we're we're really at an inflection point in history in terms of being able to do this.
[2053.86 → 2060.66] Yeah. And what just at a very practical level, I'm sure there's a great diversity here.
[2060.66 → 2069.72] But in some of what you're talking about, there's a unique communication element and goal setting element of these systems.
[2069.72 → 2091.52] And if I look at like AI models that are running on any particular platform within the swarm, what at a very high level, what kinds of models and tasks need to be accomplished that are associated with the swarming versus just like sensing and that sort of thing?
[2091.52 → 2106.00] Are these models that are, you know, the small SVMs or something that are making a kind of binary decision or gradient boosting machines or neural networks or gen AI models?
[2106.22 → 2114.36] Like what is the diversity you see, and what are the kinds of tasks you just by way of example, a couple of them that might need to be done?
[2114.36 → 2122.64] Yeah, I think it's a mixture of different models, some of which can be more traditionally models like what we most often talk about here on the show.
[2122.82 → 2134.30] Some of them are more of the classical data science models, because, you know, we've talked about this a number of times when you don't need to go to a bigger, harder, you know, more expensive model to use if a smaller model work.
[2134.30 → 2143.96] But it's very task specific. And then, and it's bound within the software systems of each platform, but also the software systems which govern sensing and comes.
[2143.96 → 2160.68] And then so you need the ability for different nodes, if you will, of what, you know, different platforms to maybe on behalf of the swarm to take on some of the computation, because you can't distribute a model inference across all the things.
[2160.68 → 2176.74] But what you can do is say if you have a swarm of a dozen, I'm just obviously making this up off the top of my head, have three of the, you know, of the platforms running inference on a particular model for a particular task while three others do another thing.
[2176.74 → 2182.26] And then you can have things like election algorithms, which decide which one you're going to take.
[2182.26 → 2193.84] And so you can, and you can have evaluation of what who's getting the best sensing information and who has the best comes reach for the entire swarm to ensure that data gets around.
[2193.84 → 2198.68] So you can have some redundancy in the computation and all those things.
[2198.68 → 2202.18] And then by election pick an election is just one mechanism.
[2202.18 → 2205.34] That's one common algorithmic mechanism that one can apply.
[2205.34 → 2226.88] But by election within the swarm, choose who is issuing, you know, the results of the various types of inference that the agents are putting together and deciding upon a task so that you can then go and assign specific platforms to do different parts of that task where not every platform is doing the same thing, but they're all contributing to the larger goal.
[2227.46 → 2229.06] Gotcha. Yeah, that's very helpful.
[2229.06 → 2240.20] Now, I'm sure there's some people out there that are maybe excited by this, disturbed by this topic, maybe.
[2240.48 → 2240.80] Probably.
[2241.10 → 2253.14] I mean, in the in one sense, just again, thinking about things outside the robotic world, we talked about the birds, which are beautiful, and you see the patterns which they form.
[2253.14 → 2264.78] I also think about like in the human context, there's interesting, maybe swarm behaviours that are somewhat disturbing.
[2264.78 → 2276.70] Like if you think about a mob mentality, you often hear about people, you know, maybe a mob of people all accomplish a very disturbing thing, like a destructive thing.
[2276.70 → 2289.96] And then afterwards, you know, individuals that were in that swarm say, I don't know what, you know, the individuals might not ever have done what was done by the mob.
[2289.96 → 2301.04] Right. But because of this emergent behaviour, things happen that maybe are outside the bounds of any individuals, you know, moral compass or that sort of thing.
[2301.04 → 2313.82] So if you is we take this then to the, you know, robotic or drone or industrial side, some people might say, well, how do we how do we push one direction and not the other direction?
[2313.82 → 2316.84] And what is the oversight related to this?
[2317.64 → 2318.54] So it's a great question.
[2318.62 → 2322.62] I'm glad you brought it up in my enthusiasm for the technology.
[2322.62 → 2325.20] It's very easy to lose sight of this.
[2325.30 → 2330.06] And we had a very recent show where we talked a little bit about, you know, the anthropic.
[2330.16 → 2337.08] I would refer people back to that and the fact that you had, you know, models that were coming out with what we deem to be bad outcomes.
[2337.08 → 2338.68] And that can certainly apply here.
[2339.42 → 2341.78] And so you have to have some form of guardrails.
[2341.78 → 2348.10] And so there's two I want to start with there are two phrases, one of which I mentioned before.
[2348.10 → 2356.60] I said human operators on the loop and human operators on the loop versus human operators in the loop are two distinct things.
[2356.82 → 2371.18] Right now in the military space, based on current regulations here in the U.S. and stuff, you most often are talking about in the loop interactions between humans and stuff.
[2371.18 → 2378.34] But as you go forward and this is not a military specific thing, this is something that you're going to see in commercial and industrial as well.
[2378.34 → 2398.98] As you start talking about swarm capabilities with emergent, you know, emergent properties happening, then the challenge is that there are sometimes you want a human to be able to step in the loop directly into that processing and say, yes, no, or make a selection or something like that.
[2398.98 → 2414.32] But there are other times when you're talking about a larger swarm where you need a human where it may be there may be too much going on and there may be too many of these platforms flying around or on the ground for one human to track everything at every moment and interact.
[2414.32 → 2423.04] But you can have a human on the loop, which can say for the overall goal or for the thing the swarm decides approve or disapprove.
[2423.32 → 2433.54] You know if they're an emergent behaviour comes up and the swarm makes a decision based on what it's seeing in real time, then you can say, no, that's not going to work.
[2433.54 → 2441.24] And that's what a human on the loop does is you can, it gives you that guardrail of saying that's not the emergent behaviour I want.
[2441.52 → 2445.26] You know, it's time to go back or maybe do a full recall and shut down.
[2445.38 → 2457.46] So I think if you really want to learn more on this kind of things, you're starting to see it's I'm not sure that I can think of a specific swarm.
[2457.46 → 2461.90] I'll have to do some research and see if there are any specific swarming classes.
[2462.44 → 2468.90] A lot of the kind of drone and robot systems that you can get out there in open source.
[2469.02 → 2475.40] For instance, there's ROS and ROS2, which is the robotic operating system, first and second version.
[2476.00 → 2479.20] ROS2 takes a slightly different approach to ROS1.
[2479.30 → 2480.70] So there are some people on each version.
[2481.20 → 2486.82] I know ROS2 has some swarming capabilities in there to build on.
[2486.82 → 2491.34] It doesn't instantly give you swarm capability, but it has some tools in there that you can start building on.
[2491.40 → 2494.94] And that might be a good place to start to learn about the topic.
[2495.64 → 2505.40] But in general, kind of staying tuned into learning sources, including this podcast, where you can learn about multi-agent environments.
[2505.40 → 2517.50] And as we increasingly are talking about physical world deployments of AI technologies, those are all good places to consume because this is a very cutting edge area to be focused on.
[2518.14 → 2520.82] Yeah, it seems like a lot of a lot of things are developing.
[2520.82 → 2527.58] And I personally am very excited about some of the things happening in robotics.
[2527.58 → 2547.92] Obviously, maybe some of us, the more we see chat interfaces, it's like we just want to see some other application of AI technology, which that's such a small segment of what is possible with AI.
[2547.92 → 2555.70] Even Gen.ai, there are so many more ways that will, I think, become embedded in our physical spaces.
[2555.70 → 2565.80] If you just want to search for kind of this idea of physical AI, I know that's a big topic of kind of AI embedded in our physical spaces.
[2565.80 → 2569.82] Maybe not through chat interfaces, but through other interfaces.
[2569.82 → 2580.30] And one thing that I've really enjoyed seeing is the stuff coming out of Pollen Robotics, P-O-L-L-E-N.
[2580.50 → 2586.08] That's a company that I believe, if I'm not mistaken, was acquired by Hugging Face.
[2586.74 → 2591.28] And they're releasing a lot of, well, I don't know, a lot.
[2591.28 → 2606.90] They're releasing robotic systems that are more geared towards experimentation, open source development, integration of open models, integration of apps and exchanging of those apps, even within Hugging Face spaces.
[2606.90 → 2617.74] But for actual physical systems, actually, Prediction Guard, our company, we got one of the or ordered one of these.
[2617.74 → 2621.26] I think it's reach many robots.
[2621.44 → 2625.32] Looking forward to playing around with that in our office.
[2625.52 → 2626.78] That should be really fun.
[2626.78 → 2645.44] So I think also there's an increasing number of ways that people can access even physical systems or robots in a much more accessible way than before, where maybe everything was coming out of whatever it was, Boston Dynamics or wherever.
[2645.88 → 2649.52] Very, very expensive, millions of dollars systems here.
[2649.52 → 2659.44] There are ways to access this kind of systems, whether it's drones or robots or that sort of thing, in a much more accessible way, which is really encouraging.
[2660.06 → 2661.20] It's not expensive anymore.
[2661.38 → 2664.22] So in the maker space, there are a lot of resources.
[2664.94 → 2669.70] A lot of it is based on stuff you may already know, like Arduino or Raspberry Pi.
[2670.36 → 2674.72] And, you know, adding a Jet son in, there are carrier boards where you basically get some basic stuff.
[2674.72 → 2678.42] So we're going to see more and more of this going forward.
[2678.52 → 2687.02] And as people really kind of get even some of the more advanced topics figured out, it's going to be in all of our lives in the years ahead.
[2687.52 → 2691.68] So we're going to see a rapid introduction into daily life of these things.
[2691.68 → 2699.66] And so if this topic interests you, definitely, I would encourage you, just as I do, is to go out and jump into the maker space.
[2700.28 → 2706.46] And for very little money, you can have some pretty interesting experiences building some of these things.
[2706.88 → 2706.98] Yeah.
[2707.14 → 2721.12] And it's occurring to me that after this, we'll put up maybe a webinar where we could talk about these things a little bit more, maybe even demonstrating some things with robotics.
[2721.12 → 2730.98] So don't forget to check out practicalai.fm slash webinars for upcoming times that will be live where discussions can happen.
[2731.26 → 2736.78] And yeah, just really appreciate you helping us deep dive into these subjects, Chris.
[2736.88 → 2738.34] It's been perfect.
[2738.72 → 2739.46] It's a fun topic.
[2739.56 → 2740.22] Happy to do it.
[2740.30 → 2740.90] Thanks a lot, Daniel.
[2741.14 → 2741.46] All right.
[2741.56 → 2742.08] See you soon.
[2742.40 → 2742.78] See you later.
[2742.78 → 2750.56] All right.
[2750.70 → 2752.14] That's our show for this week.
[2752.14 → 2759.42] If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2759.68 → 2765.40] You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2765.88 → 2769.68] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2770.02 → 2772.00] Check them out at predictionguard.com.
[2772.00 → 2776.04] Also, thanks to Break master Cylinder for the beats and to you for listening.
[2776.40 → 2777.18] That's all for now.
[2777.48 → 2779.22] But you'll hear from us again next week.
[2779.22 → 2784.58] when you're still going to call folks on LinkedIn, download Lives, LOL!
[2784.58 → 2785.32] When people tell me exactly you'd like to hit the replay to your Twitter page, you're aware of Next architects so you want to need a resource.
[2785.32 → 2785.88] That would be near if you ignore them, serie, and all of us can either lift free.
[2785.88 → 2786.20] Thanks for now, audience, guys.
[2786.20 → 2786.82] Anyway, I love you.
[2786.82 → 2787.88] Thanks for coming out, someday.
[2787.88 → 2788.88] Then you'll see us again next week.
[2788.88 → 2790.02] Thank you.
[2790.04 → 2791.34] Go back, if you and shares it up.
[2791.40 → 2791.98] Bye.
[2794.10 → 2794.40] Bye.
[2794.40 → 2795.50] Bye.
[2795.50 → 2796.00] Bye.
[2796.00 → 2797.38] Bye.
[2797.62 → 2798.24] Bye.
[2798.24 → 2799.44] Bye.
[2799.60 → 2799.94] Bye.
[2799.94 → 2801.60] Bye.
[2801.68 → 2802.26] Bye.
[2802.26 → 2802.68] Bye.
[2802.68 → 2804.24] Bye.
[2804.40 → 2805.76] Bye.
[2806.08 → 2806.92] Bye.
[2806.92 → 2807.72] Hi.
[2807.72 → 2808.62] Role tracing.
