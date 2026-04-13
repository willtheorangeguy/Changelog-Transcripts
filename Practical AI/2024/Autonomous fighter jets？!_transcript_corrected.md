[0.00 → 8.66] Welcome to Practical AI.
[9.14 → 19.56] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.38] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 → 35.44] So you can launch your app near your users.
[35.84 → 37.86] Learn more at Fly.io.
[42.44 → 47.88] Welcome to another fully connected episode of the Practical AI podcast.
[47.88 → 56.08] This is a fully connected episode where we keep you connected with everything that's happening in the AI community.
[56.38 → 63.78] All the interesting and crazy news out there and hopefully a few things that will help you level up your machine learning game.
[64.22 → 65.84] My name is Daniel Whiten ack.
[66.00 → 69.50] I am the founder and CEO at Prediction Guard.
[69.74 → 76.84] And I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[76.84 → 77.90] How are you doing, Chris?
[78.14 → 79.42] Doing great today, Daniel.
[79.54 → 80.24] How are you doing?
[80.84 → 86.84] I am doing well mentally, a little bit less physically.
[87.10 → 92.00] I ran a half-marathon yesterday, which was really exciting.
[92.48 → 97.70] And the first sort of running type event that I've done personally.
[98.08 → 102.32] And I have to say my training was going good for a while.
[102.32 → 106.56] I would say the last couple of months was not going as well.
[106.56 → 110.30] And so let's just say that I'm in a good amount of pain today.
[111.26 → 113.16] But self-inflicted, I guess.
[113.66 → 114.14] It is.
[114.26 → 115.00] I'm sorry.
[115.14 → 115.76] I sympathize.
[115.88 → 120.48] I have done a couple of half-marathons, but it has been a while since I've done them.
[120.98 → 123.56] And I know that at the end of those, I was definitely...
[124.32 → 126.00] You sound much better than I did afterwards.
[126.04 → 126.74] I got to tell you.
[127.02 → 128.66] Well, I've been in bed most of the day.
[128.66 → 136.50] Since you and I can see each other, but listeners can't, I will report that you look very well for someone who just did a half-marathon.
[136.82 → 138.50] I look terrible at the time.
[138.86 → 140.84] I am sitting in a chair, not moving.
[141.08 → 142.88] So, yeah, that's key.
[143.16 → 143.54] Excellent.
[143.54 → 154.42] Well, I guess someday we'll be doing half-marathons and there'll be things like robots running along beside us, maybe powered by artificial general intelligence.
[154.84 → 156.60] And, you know, they'll have their own.
[156.74 → 159.26] I'm presuming we don't have to compete against the robots.
[159.44 → 162.94] I'm hoping because, you know, I don't think I would do very well.
[162.94 → 173.54] Or maybe I'll just have some sort of automated or augmented knees or legs put in, and I can cyborg the marathon.
[174.30 → 178.54] You know, they've long had meniscus is the cushioning in your knees.
[178.74 → 189.52] They've long had meniscus transplants, but maybe they'll have like robotic, you know, intelligent meniscus and like it springs you up, you know, pushes off or something like that.
[189.52 → 195.70] Nobody, you'll have that edge, and they'll have to detect it then, you know, the competition, you know, for everything being equal.
[195.96 → 197.76] Who knows where we're going on that.
[197.84 → 211.66] But, you know, speaking of autonomous systems and, you know, in the spirit of robots and stuff, I thought I would kick us off by talking about the've been keeping track of kind of ongoing news story.
[211.66 → 224.64] But it popped up in the last week or so, which is the X62A Vista, which is it being a project that the Air Force has been leading with a number of companies.
[224.64 → 232.12] And for full disclosure, Lockheed Martin, my employer is involved, though I personally have absolutely nothing to do with this.
[232.12 → 235.28] And my information is only what's available publicly.
[235.44 → 238.92] So I just wanted to give my disclosure there before we got into it.
[238.94 → 242.92] But I've been following the news stories on this because it is super cool.
[243.08 → 249.38] It is an F-16 Fighting Falcon fighter plane, which are they've been around for a long time.
[249.44 → 254.30] They're actually 50 years old this year, but it's gone through multiple ownership.
[254.30 → 256.68] Lockheed Martin is the owner of the F-16 now.
[256.68 → 263.40] And it's kind of one of those for NATO countries kind of standard baseline fighter planes.
[263.40 → 275.86] But the reason it's an X-62A versus an F-16 in this case is it has been enabled with a fully autonomous AI autopilot.
[276.04 → 281.06] It's not only designed to fly the plane, but flies the plane in combat.
[281.06 → 286.92] And they have been doing simulated tests for the past about roughly the past year.
[287.04 → 288.60] I don't have all the dates in front of me and stuff.
[288.98 → 300.52] But this last week, it made a new splash because in addition to the usual human test pilot, which sits in the cockpit but does nothing, they have manual controls to override the AI.
[300.78 → 307.18] But on all the tests, they have not needed the test pilot to do anything because the AI autopilot is so darn good.
[307.18 → 313.38] And this past week, the Secretary of the United States Air Force also flew in the cockpit.
[313.38 → 317.12] It has two seats and flew in the front seat with the test pilot in the back seat.
[317.50 → 330.14] Neither human touching any controls while they did a simulated combat scenario in the sky with other airplanes flying against, you know, in a human controlled airplane.
[330.26 → 334.46] Human controlled airplanes against other test pilots flying combat scenarios.
[334.46 → 340.92] And rumour, according to what the news reports are, everything has just gone flawlessly.
[341.18 → 343.58] It performs exceptionally well.
[343.78 → 349.60] And it's just, you know, it's one of those moments in time where you realize this stuff.
[349.74 → 357.48] It's, you know, we talk about models and often our models are, you know, just in the cloud, and we're using them on apps and things like that.
[357.48 → 362.30] But this is a type where you have a model that is, you know, in the lingo out on the edge.
[362.54 → 368.04] It is controlling an advanced piece of machinery to a very high degree of performance.
[368.44 → 373.10] And, you know, we kind of had the moment with Tesla cars doing full auto.
[373.10 → 387.38] But now we're talking about some of the most sophisticated aircraft in the world, not just little drones, but big full on fighter planes being flown as well as any human or better than any human fighter pilot in the world.
[387.48 → 389.22] So what do you think of that?
[389.28 → 393.60] I've talked to him for a while, but I'm rather taken with the with just the moment.
[393.84 → 395.78] It's fascinating in a number of ways.
[395.78 → 406.26] I was thinking back to I guess it was in last month when I was in Boston and I got to stop by the MIT Media Lab for an event.
[406.48 → 409.78] And they were a panel with some various luminaries.
[410.20 → 415.14] One of the panels was an investor panel, and they were all talking.
[415.14 → 420.00] Some of the questions were, of course, related to various things about AI.
[420.10 → 421.40] It was an AI focused event.
[421.88 → 428.32] But I was struck by one of the comments about kind of this next wave of innovation and AI.
[428.32 → 443.66] And the panellist was basically saying that the days of just being kind of an innovator in AI as a model builder, as a foundation model builder, are in some ways over.
[444.22 → 450.68] What's fascinating now is embedding AI everywhere in the physical world.
[450.68 → 455.90] And at the edge, you know, here's an example of that happening in an airplane, of course.
[456.26 → 464.62] But there's certainly other things happening in the civilian space as well with AI assistance in the retail environment.
[464.62 → 468.74] Also, of course, in cars and that sort of thing.
[469.28 → 482.18] But yeah, retail environments or manufacturing environments, agriculture, machinery, all of these sorts of things where AI is going to be embedded in all of these physical spaces.
[482.18 → 486.04] That brought up that in my mind as I was thinking back to that event.
[486.18 → 499.36] But then also thinking here, I know you've made some comments before being a pilot yourself, just a civilian aircraft pilot, about the AI systems that already exist.
[499.36 → 509.52] For example, for commercial airliners and other systems that actually can even now do better in many ways than human pilots.
[510.06 → 521.84] But then there's always that, I guess, fear on people's parts where, you know, it's acceptable for a human to make a mistake in such a scenario because, you know, they could potentially be punished.
[521.84 → 527.40] Of course, in air flight, maybe they wouldn't survive if they made a mistake, which would be really unfortunate.
[527.40 → 534.22] But for a machine to make a mistake in such a scenario is sort of unforgivable because the machine shouldn't make a mistake.
[534.34 → 536.68] So there's kind of this double standard that's happening.
[537.12 → 541.24] Do you see that shifting or changing at all with some of these recent developments?
[541.70 → 544.22] I think it'll take longer in the commercial airspace.
[544.38 → 554.04] And just to address one quick thing, to the best of my knowledge at this moment, there are no AI systems authorized by the FAA in the United States to fly commercial airliners.
[554.04 → 558.98] But there's a lot of interest in testing about those kinds of systems that are out there.
[559.42 → 568.00] There's even, I may be wrong about this, but I believe it was MIT that has a system that is designed for that, that's not been deployed in production.
[568.36 → 572.86] That's kind of an open system for airliner navigation and such.
[572.86 → 575.02] But there's a lot of work in this area.
[575.06 → 579.48] And certainly on the military side, there is not, there's lots and lots of constraints.
[579.48 → 583.92] So I don't want to, I don't want to represent it as like, oh, you can do whatever you want.
[583.98 → 588.96] There are tons and tons of gateways you have to, you have to earn your way through in the testing.
[588.96 → 606.06] But there is definitely a full on interest in military circles and defence circles about using AI and just about every conceivable use case that you might want to come up with on the ground, in the air, undersea, in space, you name it, everything.
[606.74 → 608.56] And that's without getting sidetracked.
[608.66 → 612.82] I spend a lot of time in those scenarios in my day job away from the podcast.
[612.82 → 618.66] But many things in the military world are classified, and you can't really talk about it.
[618.66 → 624.42] And one of the really cool things about the X62A program is it's being done in the light of day.
[624.70 → 632.34] It's a news story every time something news happens, and you can go and search it and find all sorts of information about it.
[632.74 → 633.48] It's interesting.
[633.48 → 640.96] Over time, if you, over the last few years, I am one of those people because I've seen this a lot.
[641.16 → 651.94] As a pilot and as just a non-pilot, I will trust myself to AI autopilots and trust my family's lives if it were to come to that because they're so darn good.
[652.30 → 657.46] I've seen them back as far back as a DARPA event that was public on YouTube in 2020.
[657.46 → 670.06] It was a simulator, but the AI pilot beat one of the best fighter pilot instructors in the world, an Air Force instructor, the equivalent of what people would know as Top Gun in the Navy, and just demolished the poor guy.
[670.64 → 673.90] And that was four years ago now, over four years ago.
[674.14 → 679.36] And so we've come, you know, that's the prehistoric times in AI, you know, in the way we think of AI.
[679.36 → 685.00] So I really do think that we're crossing some thresholds now.
[685.18 → 694.26] And really the thing that will hold us back is the public becoming comfortable enough to really, you know, embrace the technology as that.
[694.32 → 704.52] And I think one of the before I draw to an end, and I'm not picking on Boeing, but the Boeing, you know, problems with the 737 MAX, which is not an AI system.
[704.52 → 713.08] They are automated systems, but they're not AI systems, has really shaken the public's trust in automation in aircraft and airliners.
[713.58 → 716.62] And so there's that will slow things down.
[716.76 → 730.74] But, you know, someday when we do have FAA approved systems in the airliners that we're all flying every day, I think that we will be orders of magnitude safer than we are with even seasoned airline pilots today.
[730.82 → 733.72] I'm so sorry as a pilot to say that to you pilots out there.
[733.72 → 734.36] I don't mean that.
[734.42 → 739.16] I have many good friends who are in that occupation, but that's just the way AI is.
[739.20 → 739.92] It's quite amazing.
[751.78 → 758.76] If you're anything like me, you have a certain tendency to put things off until the very last minute.
[758.76 → 765.36] Seeing the dentist, going to the doctor, home improvements, that never ending chore list of yours.
[765.88 → 774.16] And while most of the time it works out just fine, the one thing in life that you really cannot afford to wait on is setting up term coverage life insurance.
[774.80 → 779.66] You've probably seen life insurance commercials on TV and thought, yeah, I'll look into that later.
[780.16 → 781.58] No, later doesn't come.
[781.86 → 783.20] This really isn't something you can wait on.
[783.50 → 786.12] Choose life insurance through a ladder today.
[786.12 → 789.90] Here's what we love about ladder and why we allow them as a sponsor.
[790.40 → 791.58] They are 100% digital.
[792.02 → 794.44] No doctors, no needles, no paperwork.
[794.84 → 800.20] When you apply for $3 million in coverage or less, just answer a few questions about your health in an application.
[800.76 → 804.88] Ladder's customers rate them 4.8 out of 5 stars on Trustpilot.
[805.18 → 808.06] And they made Forbes best life insurance 2021 list.
[808.06 → 811.26] You just need a few minutes and a phone or laptop to apply.
[811.62 → 816.10] Ladder's smart algorithm works in real time so you'll find out if you're instantly approved.
[816.24 → 817.18] No hidden fees.
[817.38 → 818.34] You can cancel anytime.
[818.74 → 823.02] Get a full refund if you change your mind in the first 30 days.
[823.36 → 828.96] Ladder policies are issued by insurers with long proven histories of paying claims.
[829.36 → 833.12] They're rated A and A plus by A and best.
[833.12 → 840.06] Finally, since life insurance costs more as you age now, yeah, right now, now's the time to cross it off your list.
[840.58 → 847.40] So go to ladderlife.com slash practical AI today to see if you're instantly approved.
[847.68 → 852.12] Again, that's ladder.com slash practical AI.
[852.26 → 857.64] L-A-D-D-E-R life.com slash practical AI.
[857.64 → 887.46] Well, Chris, one of the things that I was thinking about when you were bringing up the story about the X62 autonomous testing was one of the comments you talked about was the sort of regulations.
[887.64 → 892.76] And guardrails around the testing that it's also happening in open.
[892.76 → 899.22] There are regulations, especially in the airspace, about testing these vehicles and that sort of thing.
[899.90 → 910.84] I was remembering back I had a conversation with breakfast with a group that just came out here to Purdue University where I'm located.
[910.84 → 913.32] The company is called Wind Racers.
[913.88 → 929.04] And they have sort of commercial autonomous drones that are really kind of mid-sized drones that do like mail remote or rural mail routes or something like that.
[929.14 → 930.62] Like they send mail in the UK.
[930.62 → 938.58] They have drones that take mail out to all of these different islands in the UK that need mail deliveries and that sort of thing.
[938.70 → 946.24] But then also there's the chance to use these for disaster relief or humanitarian aid and that sort of thing.
[946.24 → 963.06] And I know one of the things that they talked about was just the struggle in finding ways to test autonomous drones, especially in the airspace, to actually make significant progress in the R&D and testing and all of that.
[963.18 → 968.84] You actually have to be able to take flights over significant distances and that sort of thing.
[968.84 → 973.60] And here you see, you know, these tests happening on the military side.
[973.76 → 982.94] I know there's differences kind of civilian and government with the ability to test things and availability of airspace and all of that.
[983.08 → 991.08] But how do you as a pilot, maybe you're maybe more familiar with some of these regulations than the rest of us are.
[991.08 → 1000.12] How do you see this technology being able to develop over time with such restrictions around testing?
[1000.30 → 1008.66] And how could that be eased up reasonably without undue, you know, issues and danger and that sort of thing?
[1008.70 → 1015.16] Because obviously, if you have drones flying over populated areas, that is definitely an issue.
[1015.42 → 1020.42] But at some point, there's going to have to be a drone fly over a populated area.
[1020.42 → 1020.86] Indeed.
[1021.50 → 1024.98] And so to start off with, I certainly am not an expert in that.
[1025.12 → 1028.12] I have some very loose familiarity with the process.
[1028.46 → 1031.24] Military, they have their own dedicated airspaces.
[1031.34 → 1043.80] There's military airspace, and especially it's all over, but especially out west, places like Edwards Air Force Base and a number of others where you have literally, you know, hundreds of square miles that you can do testing in.
[1043.92 → 1047.80] And obviously, there's a long history of that since the dawn of flight.
[1047.80 → 1053.20] The FAA is very aware, you know, of the need to innovate on this.
[1053.36 → 1064.32] And so they basically you have to apply for what you're trying to do and show them that you've done due diligence from the engineering safety, you know, all the concerns about that.
[1064.32 → 1067.42] And basically, I follow a lot of aviation news.
[1067.52 → 1071.44] So I've kind of read about a number of these programs that have come into being.
[1071.44 → 1085.90] And then they give you a little bit of a leash, and you can kind of you have to kind of earn your way through a number of gateways, you know, where you successfully do something in very small scale, very small scope and increase your way into it.
[1085.90 → 1089.58] But it seems to me that that is happening more and more.
[1089.58 → 1102.42] And in some cases, if there is a military utility to doing that, then there can be coordination also with military and taking advantage of military airspace to have more room, things like that.
[1102.84 → 1116.60] So it seems, though, though, obviously, government agencies are not the speediest things typically that there are opportunities for even private businesses and stuff to get some support in that way.
[1116.86 → 1117.56] They know it's coming.
[1117.56 → 1128.20] Yeah, this is probably something we could refer people back to our previous episodes with Jake and others.
[1128.78 → 1136.10] It's unlikely that we'll be seeing the skies filled with weaponized autonomous drones doing whatever they want.
[1136.20 → 1141.94] There's a lot of there's a lot of hopefully responsible people thinking about these things.
[1141.94 → 1153.60] But the main interesting piece here is both on the commercial side and on the military side, the ability to increase safety and decrease people.
[1154.28 → 1157.60] Human pilots being in dangerous situations.
[1157.60 → 1161.86] I think it seems to be the focus of a lot of this.
[1162.38 → 1170.26] Now, you know, there's probably all of those out there that can imagine all sorts of scenarios of misuse and all of those sorts of things.
[1170.26 → 1182.26] But there's also in our previous conversations with people, at least I have some hope that there's some reasonable people and thoughtful people that are part of these programs.
[1182.26 → 1186.44] Yeah, it just at risk of sounding like an apologist.
[1186.44 → 1191.04] I point out to people, there are a lot of safeguards to that point.
[1191.18 → 1192.32] I work in defence.
[1192.50 → 1193.48] I come home.
[1193.58 → 1195.38] I mostly work from home.
[1195.38 → 1202.42] But I have my family and my dog and everybody else who's doing this, whether they're in the military or whether they're civilians supporting that.
[1202.62 → 1205.00] They have their family and their kids and all that.
[1205.14 → 1212.62] So the notion that there's like the dark military minds behind the closed doors is, in my experience, a fiction.
[1213.16 → 1221.64] We all, you know, when we get on the phone or even for a business thing, we're talking about the same things that everybody else talks about, you know, the weekend.
[1221.64 → 1226.60] And, you know, my dog wasn't feeling well, and my kid was staying home from school or whatever.
[1226.84 → 1229.44] And so I'm very encouraged in that way.
[1229.54 → 1231.46] It's normal people running these.
[1231.66 → 1237.28] And they have different motivations, obviously, depending on where they're at and what organization they're with.
[1237.58 → 1241.16] But it's one of their things that I get worried about with AI going forward.
[1241.20 → 1242.18] But that's not one of them.
[1242.18 → 1251.14] Yeah, I might refer people back to our episode leading the charge on AI and national security with General Jack Shanahan.
[1251.14 → 1252.78] Perfect episode, too.
[1253.14 → 1255.24] Yeah, retired U.S. Air Force.
[1255.84 → 1269.02] So if you want to get a sense of someone that was sort of leading the charge on the inside for a good long time, then I would recommend that episode from being a civilian myself.
[1269.20 → 1271.02] It was good to have a chat with him.
[1271.02 → 1274.34] Yeah, General Shanahan, who is now retired, is both.
[1274.52 → 1283.38] That was a recent episode as we record this and was also the original hard charger for AI in the military and is in a unique.
[1283.50 → 1287.16] He's still considered, even though he's retired, to be one of the top experts and influencers.
[1287.46 → 1289.14] So I hope people check that out.
[1289.14 → 1296.88] Yeah, well, I don't know if this was widespread news, but I thought it would be a cool thing to highlight for people.
[1296.88 → 1300.06] You know, you're talking about kind of this further testing.
[1300.82 → 1308.38] And I'm sure some of that testing on the autonomous vehicle side involves standards and best practices and frameworks.
[1308.38 → 1316.08] All of that's necessary to really advance a technology from R&D to prototype and otherwise.
[1317.00 → 1325.50] And I think that we're seeing also some of that on the enterprise AI, generative AI side of things.
[1325.50 → 1335.38] So this last couple of weeks, I was informed about this project, which is now a project at the Linux Foundation.
[1335.84 → 1347.78] And the project is called the Open Platform for Enterprise AI, just abbreviated to OPEN, which seems like an unfortunate and awkward acronym.
[1348.76 → 1351.52] I don't I was trying to think, like, how do I?
[1351.94 → 1352.06] Yeah.
[1352.20 → 1352.88] OPEN.
[1353.24 → 1353.92] I don't know.
[1353.92 → 1360.18] I see you avoiding the obvious high school way of doing it.
[1360.64 → 1362.74] Yeah, I mean, not the greatest of acronyms.
[1363.00 → 1367.92] But yeah, the Linux Foundation has this AI and data foundation.
[1367.92 → 1371.06] So if you're not familiar with the Linux Foundation, you can look it up.
[1371.30 → 1379.48] But this enterprise open platform for enterprise AI is a very collaborative initiative, it seems.
[1379.48 → 1382.36] And just some of the companies involved.
[1382.36 → 1383.36] I'll kind of list them out.
[1383.36 → 1383.96] I'll kind of list them out.
[1384.30 → 1386.50] Not all of them, but just to give you a sense.
[1386.88 → 1396.38] Includes Intel and Any Scale, Cloudera, Batista, Domino Data Lab, Hugging Face, Mini, Willie.
[1396.74 → 1402.12] A bunch of different companies that probably you're familiar with.
[1402.12 → 1405.60] Certainly ones that we've talked about on this show.
[1405.94 → 1414.56] And there are a few interesting elements of this open platform for enterprise AI.
[1414.56 → 1435.72] But the general goal, I think, is to enable and facilitate, or the way that they frame it is, aims to facilitate and enable the development of flexible, scalable Gen AI systems that harness the best open source innovation from across the ecosystem.
[1435.72 → 1441.82] And that's kind of vague in terms of where they're going with this.
[1441.90 → 1447.98] But I think if you look sort of a little bit deeper, I think there's some fascinating things of where this could lead.
[1447.98 → 1459.08] One is they recognize certain common and developing archetypes or main use cases where people are using generative AI.
[1459.26 → 1463.32] For example, the RAG workflow, Retrieval Augmented Generation Workflow.
[1463.32 → 1477.70] And they're kind of take that RAG workflow and are creating blueprints for the various pieces that are involved in an industry standard kind of advanced RAG workflow.
[1477.84 → 1486.42] Not just a naive RAG workflow that you might play around with on your laptop, but something that could be deployed in the enterprise.
[1486.74 → 1489.96] And so they have some blueprints or kind of architecture type of things.
[1490.02 → 1492.30] I think there'll be more of that that will be developed.
[1492.30 → 1497.26] And then those architectures or blueprints have certain components within them.
[1497.68 → 1507.84] For example, a retrieval or ranking system or an embedding model or guardrails for models or fine-tuning systems or a vector database.
[1508.56 → 1519.30] And then if you follow the link to the GitHub related to the OPEN project, OPEN project, whatever you want to call it.
[1519.30 → 1527.70] I noticed some fascinating kind of a few categories of some things that aren't quite complete there yet, but that they're building in public.
[1527.70 → 1537.02] And those are both examples of implementing this sort of reference implementations of industry standard ways of going about doing certain things.
[1537.24 → 1547.08] So like chat with your docs, code generation assistance that you can plug into Visual Studio Code, document summary, visual question answer.
[1547.08 → 1556.08] And those reference implementations include open source ways of doing these different things in a kind of industry standard way.
[1556.64 → 1565.66] Another one is they have it seems like they're developing a series of micro open microservices that could be plugged in to do various of these components.
[1565.66 → 1568.96] And then finally, a set of evaluations.
[1569.48 → 1581.78] So they have a repo evaluation benchmark and scorecard targeting performance on throughput and latency accuracy on popular evaluation harnesses for safety, hallucination, other things like that.
[1581.90 → 1584.52] So there seems to all of that put together.
[1584.68 → 1594.60] I know that was a little bit ramble, but it seems like their kind of focused here on these blueprints, reference implementations of things represented in those blueprints.
[1594.60 → 1604.02] And then industry kind of enterprise level evaluations for performance and issues within these systems, that sort of thing.
[1604.14 → 1611.40] So this definitely seems encouraging to see a lot of collaboration on this and see the support from the Linux Foundation.
[1611.94 → 1619.78] Yeah, I mean, with the Linux Foundation being, you know, one of the most reputable open source organizations in the world, certainly the top few.
[1619.96 → 1623.98] It's really important that initiatives like this come into being.
[1623.98 → 1638.30] And the reason is that in the business world, I know you in your company, and I certainly as I'm talking to people in different companies, everyone out there is trying to find their own way into implementing generative AI solutions.
[1638.30 → 1639.56] And how do you put it together?
[1639.64 → 1640.54] How do you architect it?
[1640.92 → 1642.66] I have my own thoughts around that.
[1642.66 → 1645.78] And I know the company I work at has its own thoughts around that.
[1645.78 → 1657.16] And I end up talking to people at different organizations, and they're struggling with many of the same problems, but they come to their own solutions, you know, based on however their team wants to approach it.
[1657.16 → 1672.78] And as we know from other, you know, before generative AI, and even before AI came along, it's an early point in every growth, you know, development of every, you know, whether in software or anything else, where you have everyone kind of going off and doing their own thing.
[1672.78 → 1681.80] But they realize that itself will, while it might solve the immediate itch they need, it creates a whole new set of problems, as they have to grow and integrate with other organizations.
[1681.80 → 1688.18] So seeing what the open platform for enterprise AI has to offer, it looks very promising.
[1688.52 → 1693.50] And I would encourage organizations out there to take a look at it.
[1693.62 → 1705.30] And whether you adopt it or not, maybe it helps frame how you're choosing to solve problems in a way that might make situations you're in down the road that you're not thinking about yet a little bit easier to cope with.
[1705.30 → 1720.56] Well, Chris, as we kind of look back to the last sets of newsworthy AI stuff happening in all over the place, both in terms of large language models, gen AI and not gen AI.
[1720.56 → 1732.16] One of the themes recently that it seems like has been happening and kind of in getting into its prime is video generation.
[1732.16 → 1741.28] I don't know if you've been following this sort of stuff, but I know that there was I saw something from Microsoft.
[1741.28 → 1744.62] I saw something from Alibaba, I think.
[1744.80 → 1748.96] Of course, there was the open AI video generation stuff.
[1749.18 → 1753.04] There's been things from Runway, ML.
[1753.38 → 1760.74] And yeah, so what are your general thoughts on where all of this video generation stuff is happening or is going?
[1760.74 → 1762.52] A couple of thoughts there.
[1762.70 → 1767.16] I don't think it should surprise anyone at this point who's following the industry.
[1767.54 → 1776.82] You know, when we were doing our thoughts for 2024 last year, we were talking about this would surely come next, you know, because we were well into still imagery and stuff.
[1777.14 → 1784.08] And the rate that we're seeing things progress from a quality standpoint, you know, when is going so fast.
[1784.08 → 1788.38] You know, it was not long ago that open AI released Soros.
[1788.80 → 1790.28] That wasn't long ago at all.
[1790.52 → 1794.58] And we were kind of going, oh, wow, look at, you know, it's here and look at this first thing.
[1794.62 → 1798.06] And now there are many options available after just a few weeks.
[1798.06 → 1814.84] And I think I've been somewhat amused to look at the reactions in public about people and the concerns about AI safety and, you know, deep fakes being so much better now in 2024 than they were a year ago right now.
[1814.84 → 1821.54] So we're going to have to adjust and take it in and recognize the utility and come up with some safeguards for it.
[1822.06 → 1828.18] I guess it was kind of obvious to us and those of us who are following this weekend and week out that we'd be here.
[1828.44 → 1829.30] And so now we're here.
[1829.68 → 1834.10] I'm waiting to see some of the more interesting, creative, productive things that people are going to put this to.
[1834.10 → 1840.28] I'm really looking forward at this point to seeing some utility coming from it that's meaningful.
[1841.74 → 1845.78] And yeah, just so people can go out there and look at these things.
[1845.96 → 1852.72] One is called Vast One, which is the one from Microsoft Research.
[1853.62 → 1859.78] And the kind of tagline there is lifelike audio driven talking faces generated in real time.
[1860.14 → 1861.52] This was an interesting one.
[1861.52 → 1876.94] It kind of almost reminded me of the sort of videos that I've seen from Synthesia and these other companies that kind of help create talking heads essentially for marketing videos or training videos, this sort of thing.
[1877.58 → 1880.38] And very impressive stuff there.
[1880.70 → 1888.84] You might have seen something going through on Twitter or LinkedIn with, you know, people always try to make the Mona Lisa face talk.
[1888.84 → 1891.20] And I saw that was one of their examples.
[1891.52 → 1897.98] That they had, which, you know, that seems to be a sort of given that you try that if you're working in this space.
[1898.38 → 1901.62] And the most recent one wasn't actually anywhere close to being the best stuff.
[1901.74 → 1902.84] It was, it was rich.
[1902.92 → 1906.74] I saw that maybe a week ago, and it was pretty cheesy.
[1907.28 → 1910.34] But I mean, we're truly arrived in 2024.
[1910.34 → 1916.86] If you can have video now, certainly at least talking head video that is indistinguishable from a person.
[1916.86 → 1925.88] You would be very, if you were to put, you know, compare it, have two or three people and have two or three AI generated ones, mix them up and have people choose which ones are which.
[1926.48 → 1930.22] I know that I probably could not do that successfully.
[1930.48 → 1933.94] I might get lucky and pick one or two, but we're getting there.
[1933.94 → 1946.06] And so it's, I really am curious to see how these are put it like beyond the novelty of it, of seeing them finally arriving after talking about this stuff for a while.
[1946.06 → 1951.86] I really am curious to see how people use them for, you know, we like to talk about AI for good.
[1952.10 → 1957.44] I really want to see, instead of people worrying about this, strictly about the security concern, which is legit.
[1957.70 → 1964.64] I'd like to see some people do some amazing things for it that is going to benefit people and humanity at large.
[1964.64 → 1966.64] And I'm excited to see those use cases.
[1966.64 → 1972.32] And if anybody out there has something, please point us to it because those are the use cases I'm waiting to see.
[1972.32 → 1981.00] Yeah. And the one, if people are searching from Alibaba is just called Emo, or I guess it's E-M-O.
[1981.28 → 1990.58] I assume Emo. Alibaba is Emo and Vast from Microsoft, if you want to take a closer look.
[1990.58 → 2001.22] It kind of seems to me, Chris, like a time when, you know, when Dali came out, the first one, and then there was, it was like Dali Stable Diffusion.
[2001.22 → 2006.86] And there just seemed to be this snowball really quickly of image generation things.
[2007.02 → 2011.90] It seems like we're in a similar cycle right now with the video generation stuff.
[2011.90 → 2018.46] And then eventually, you know, it'll be integrated into our chat interfaces and other things that.
[2018.68 → 2020.98] I don't think it's going to be long at all to get to that point.
[2021.06 → 2023.72] I think we're going to be amazed at how fast those get integrated.
[2023.72 → 2024.08] Yeah.
[2024.32 → 2031.80] Because every time they keep building on themselves and, you know, we, the one thing we've noticed over the last two years is the acceleration in the development.
[2032.06 → 2036.52] And we will say something will come out in the next year, and then it comes out two months later.
[2036.92 → 2041.02] And, you know, a couple of times we said, well, we predicted it, but we were wrong on the timing on that.
[2041.02 → 2043.74] I think it's going to happen pretty darn quick.
[2043.94 → 2052.50] And to illustrate that, though, it's not specific to this use case, Hugging Face announced this past week that they had crossed over the 1 million mark.
[2052.62 → 2056.72] There's 1 million AI models hosted, Hugging Face.
[2057.12 → 2057.28] Yes.
[2057.38 → 2061.56] Congratulations to Hugging Face and the team there.
[2061.72 → 2062.32] That's amazing.
[2062.66 → 2068.02] All those, you know, it wasn't that long ago where they were nowhere close to a million, but it keeps accelerating.
[2068.02 → 2070.70] And so they'll hit 10 million in no time, I'm sure.
[2071.34 → 2079.60] But to your point earlier that I think it's not just going to be seeing these new technologies coming out where we're looking at the demo.
[2080.18 → 2091.24] But I think for like the second half of 2024 and into 2025, there'll be such a huge push at getting models integrated into real world scenarios.
[2091.52 → 2096.02] You know what we would like to say is at the edge in all sorts of different contexts.
[2096.02 → 2110.96] And that's really, quite honestly, what I'm excited to see is if instead of just a talking head with the audio that's indiscernible, I want to see that in some good contexts that are in places that we're not used to seeing them that make a big difference.
[2111.20 → 2112.36] And so that'll be a pretty cool.
[2112.70 → 2116.34] For me, that'll be a cooler milestone than just seeing the demo up front.
[2116.34 → 2143.70] Yeah, it does seem like that there are some big possibilities in even spaces like education and other places where, hey, you have some text content, you have some sort of curation in place, but creating very much appealing and realistic looking educational content that would fit certain scenarios.
[2143.70 → 2147.28] Because there are tons of sort of self-study stuff online.
[2147.80 → 2152.38] Some of it has better video quality than others.
[2152.70 → 2169.22] But also some of it's at a certain level that's, you know, if you have one set of content, a professor records maybe a video course or something that lasts, you'd have to watch it for an hour every day for many weeks, maybe.
[2169.22 → 2183.04] But if you can repurpose some of that content to answer questions and create engaging courses in different shorter forms or for different age levels and that sort of thing.
[2183.04 → 2194.78] And some of that was able to still be video, still be engaging, but not take a huge amount of video production to create, which is very expensive and time-consuming.
[2195.20 → 2196.60] I could see a lot of possibilities there.
[2196.68 → 2197.60] There are probably many others.
[2197.70 → 2199.74] I'd love to hear from our listeners.
[2199.74 → 2206.16] If they have ideas about this, we'd love to hear about them in our Slack channel if you want to join or elsewhere.
[2206.16 → 2218.74] Just to illustrate that for a moment, and we've talked about education use cases many times, both in how it intersects with traditional education, you know, like I have a daughter in middle school.
[2219.24 → 2228.12] And also, you know, things like continuing education for grownups, you know, that are continuing through this ever-changing world that constitutes our careers.
[2228.12 → 2249.86] But it's very easy to leap from, you know, the VAST example that we're talking about with the talking faces being generated in real time, as they know, and thinking every kid in school, in addition, you know, potentially as things are transitioning forward, and we still have traditional educational paradigms that most kids are involved in.
[2249.86 → 2263.06] But maybe every kid has their own personal teacher in addition to a classroom teacher, and that personal teacher explains the math in a way that that student understands compared to the student next to them.
[2263.44 → 2266.18] And you get a lot of personalization and support that way.
[2266.48 → 2268.66] That would be wonderful to see that.
[2268.78 → 2270.08] And so kids aren't left behind.
[2270.22 → 2275.64] And if you don't understand it the way the teacher is explaining it, you don't have to struggle because you already have your personal assistant.
[2275.64 → 2279.68] So there's many, many thousands of use cases along those lines.
[2280.14 → 2283.28] So that's the kind of thing that I'm pretty excited about for the future.
[2283.82 → 2283.86] Cool.
[2284.02 → 2284.20] Yeah.
[2284.56 → 2294.12] Well, as we kind of draw things to a bit of a close here, we normally try to provide a learning resource for people in these fully connected episodes.
[2294.78 → 2296.78] And I want to share one today.
[2296.78 → 2302.48] We've been doing a bit of experimentation of our own, Chris, with these practical AI webinars.
[2302.48 → 2306.52] These, I think what we've been calling them, Gen AI Mastery.
[2306.64 → 2308.12] So we've done two at this point.
[2308.76 → 2315.64] One related to text to SQL and one related to private chat UIs.
[2316.28 → 2322.40] And I think it's been a good experience so far, at least to motivate us to do it a bit more.
[2322.40 → 2331.16] And we're really trying to make these webinars a live, good learning experience for people.
[2331.96 → 2341.28] And something where we have some hands-on, you know, a visual component with some hands-on that you don't kind of get in just the audio podcast scenario.
[2341.28 → 2344.60] So we do have another one of these planned.
[2345.26 → 2354.44] And I would highly recommend that you go to tinyurl.com slash genai-mastery3.
[2355.32 → 2359.32] tinyurl.com slash genai-mastery3.
[2359.58 → 2361.40] And we'll put that in the show notes as well.
[2361.48 → 2362.70] And sign up for this next one.
[2362.78 → 2365.62] It's going to be about multimodal AI.
[2365.62 → 2371.08] And we're finalizing the guests, but I already, I think I know who they're going to be.
[2371.18 → 2381.32] And it's going to be a sort of rock star there helping us learn about multimodal AI, doing cool things with video, as we've been talking here, but also imagery.
[2381.78 → 2388.90] And kind of tying together text prompts in there as well for kind of multimodal rag sort of systems.
[2389.12 → 2392.22] So if you're interested in that, definitely sign up.
[2392.26 → 2394.26] It's going to be a great experience.
[2394.26 → 2398.06] So we'll have that link in the show notes and look forward to seeing everyone there.
[2398.42 → 2404.54] Yeah, it's a lot of fun to do those sessions because it's live real time and everybody can see everybody else in the chat.
[2404.78 → 2408.58] And those real time communications as we're doing them make it pretty special.
[2408.98 → 2409.16] Yep.
[2409.56 → 2410.28] All right, Chris.
[2410.38 → 2411.26] Well, it's been fun.
[2411.40 → 2415.94] I hope you can enjoy the rest of your weekend, and we'll talk to you soon.
[2416.26 → 2417.08] Take it easy, Daniel.
[2424.26 → 2428.06] All right, that is Practical AI for this week.
[2428.86 → 2429.90] Subscribe now.
[2430.06 → 2435.06] If you haven't already, head to practicalai.fm for all the ways.
[2435.46 → 2441.44] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2442.04 → 2446.66] Sign up today at practicalai.fm slash community.
[2446.66 → 2454.20] Thanks again to our partners at fly.io, to our beat freaking residents, Break master Cylinder, and to you for listening.
[2454.56 → 2456.32] We appreciate you spending time with us.
[2456.68 → 2457.86] That's all for now.
[2458.10 → 2459.78] We'll talk to you again next time.
[2459.78 → 2489.76] We'll talk to you again next time.
