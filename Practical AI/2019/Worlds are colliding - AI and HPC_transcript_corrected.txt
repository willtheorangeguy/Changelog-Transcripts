[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.86] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.54] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.42 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.48 → 102.28] And now onto the show.
[106.64 → 111.20] Welcome to another fully connected episode of Practical AI.
[111.54 → 117.70] In these episodes, Chris and I keep you fully connected with everything that's happening in the AI community.
[117.70 → 126.24] We'll take some time to discuss some of the latest AI news and dig into learning resources to help you level up your machine learning game.
[126.56 → 127.92] I'm Daniel Whiten ack.
[128.04 → 130.72] I'm a data scientist working with SIL.
[131.34 → 134.78] And today's a special episode, a fully connected episode.
[134.78 → 139.46] It's always Chris Benson, my co-host, and I that do these episodes together.
[139.62 → 141.38] We kind of chat back and forth.
[141.56 → 146.62] But we're talking about kind of what's going on in the AI news and some of the things we're seeing.
[146.76 → 156.28] And one of the things that I was kind of seeing was some mentioning, more mentioning of HPC or high performance computing clusters in the AI context.
[156.28 → 166.06] And it turns out that Chris Benson, my co-host, is somewhat of an expert in this area and working very closely in this area with Lockheed Martin.
[166.20 → 172.60] So I thought today we could just take some time and I could interview Chris a little bit about HPC clusters.
[172.60 → 177.82] And we could discuss, you know, what they are, how they're being used, what the future is and all that.
[178.02 → 179.50] So you ready for that, Chris?
[179.92 → 180.56] I sure am.
[181.24 → 182.68] I'm looking forward to this episode.
[182.84 → 185.38] It's turning things on its head just a little bit here.
[185.38 → 191.76] Yeah, you get to have some empathy for our guests and figure out what that's like.
[191.90 → 196.90] You can let me give me some pointers about my interview skills after afterwards.
[197.36 → 200.06] OK, I'm nervous for the first time in forever, Daniel.
[200.98 → 201.64] All right.
[201.66 → 202.60] We'll see how it goes.
[202.68 → 207.82] See if is either one of us crashes and burns in as we're doing something slightly different.
[207.98 → 209.44] But I think we'll be all right.
[209.44 → 218.40] Maybe just to start things out, could you kind of remind maybe new listeners or those that haven't kind of listened to the intro episodes?
[218.96 → 226.14] Remind us what you're doing, where you're working and kind of how you ended up crossing ways with the HPC world.
[226.14 → 238.32] OK, so I'm a principal artificial intelligence strategist at Lockheed Martin, and I work directly for the chief data and analytics officer, whose name is Matt Thrasio.
[238.32 → 245.52] And we do a lot of things for the company at a corporate level supporting the four big business units.
[245.74 → 248.36] And they each are entities unto themselves.
[248.60 → 250.92] You can go out on Wikipedia and check Lockheed Martin.
[251.10 → 252.38] We have missiles and fire control.
[252.54 → 253.44] We have aeronautics.
[253.56 → 254.80] We have space.
[255.06 → 257.28] And we have rotary and mission systems.
[257.34 → 258.56] And those are the four business units.
[258.72 → 261.08] And they're all doing incredibly cool things.
[261.22 → 262.38] And I'm not trying to sell them.
[262.38 → 265.56] It's a fascinating environment in which to work.
[265.68 → 268.04] And so our team tries to support that.
[268.24 → 278.26] And one of the things of many that we are doing on our team is supporting the high-performance computing efforts along with other teams.
[278.38 → 279.68] It's not just us doing that.
[279.90 → 286.40] But we are very involved in high-performance computing strategy on how to support all the different people.
[286.52 → 290.36] And Lockheed has something on the order of 110,000 people, give or take.
[290.48 → 292.18] And so it's a large company.
[292.38 → 297.24] And a diverse set of things that different teams do throughout the company.
[297.46 → 302.32] And so what we're trying to do is we have lots of HPC capability already within the company.
[302.32 → 307.34] But we are reassessing in terms of how we're doing it and providing support.
[307.58 → 312.90] And so what I can talk to is certainly about kind of all the types of decisions that have to be made.
[313.16 → 319.54] I obviously won't be talking about Lockheed-specific decisions and how we're implementing because it's proprietary knowledge.
[319.54 → 322.52] But we are kind of neck deep in all the different decisions.
[322.52 → 325.36] And how do you do this in 2019?
[325.62 → 327.52] And this is a changing space.
[327.52 → 329.64] So I'll turn it back over to you.
[329.64 → 331.42] And then we can dive forward.
[331.82 → 332.42] Yeah, sounds good.
[332.48 → 334.04] I'm not sure if you knew this.
[334.04 → 339.30] But I had a very brief interaction with the HPC community back after.
[339.68 → 341.18] Well, I mean, I started out in academia.
[341.18 → 349.34] So in academia, if you're in any sort of computing research field, oftentimes you'll interact with HPC clusters.
[349.34 → 356.40] But then after my undergrad, I did an internship with the National Centre for Atmospheric Research in Boulder, Colorado.
[357.12 → 358.28] They operate several.
[358.52 → 360.94] I'm not sure actually at the moment what they operate.
[361.02 → 363.92] But at the time, they operated several big supercomputers.
[364.46 → 372.34] And, you know, I was doing some like benchmarking of vector computing on a new IBM Power 6 computer.
[372.58 → 374.58] So it's been a while for me.
[374.58 → 382.76] So I'm interested to kind of like I have some concept back in my head of like my interactions with the cluster at that time and what people are doing.
[382.76 → 385.34] But I'm sure it's just like vastly different now.
[385.46 → 390.66] So I'm really interested to hear how things have progressed and how that intersects with AI.
[391.10 → 398.48] Maybe to begin with on that subject, could we just kind of define what is high performance computing or HPC?
[398.48 → 405.80] Like how is it different from, let's say, some things that might also be in people's mind like cloud computing or something like that?
[406.42 → 406.50] Yeah.
[406.62 → 412.96] So just like defining AI can be harder than one might expect because of all the diversity of opinions on what it is.
[413.36 → 418.62] High performance computing is also undergoing quite a transformation at this point in time.
[418.76 → 426.20] And so I would suggest that I will offer my take on what it is and that there will certainly be people out there in the audience that will disagree with me on this.
[426.20 → 428.80] But just as if we were defining AI.
[429.02 → 441.92] So really, there are applications in the world that need a tremendous amount of computing resource, more so than you're typically finding from either on-prem or traditional kind of cloud resources.
[441.92 → 453.98] And you need to be able to scale up with a processing capability that is often done massively in parallel to be able to tackle a computationally intense problem.
[453.98 → 464.88] And so when I talk to people that have been in this space for a long time, and I've only been in it for several years now, not only Lockheed, but at previous employers, but the nature of the field has changed a lot.
[465.02 → 478.06] And so like if I talk to people that have been doing things like simulation, you know, obviously, you know, Lockheed builds platforms for our customers that, you know, in various environments, space and underwater and whatever.
[478.06 → 480.56] And so that requires a lot of simulation.
[480.78 → 489.20] And so if you talk to people that have been running high-performance computing clusters for a period of time, what they're trying to do is say,
[489.42 → 500.00] I need to take maybe a new vehicle or something and try it out in a simulated environment to solve problems and figure out, you know, while it's still in this state,
[500.36 → 506.60] what it needs to be able to do and what the problems are and stuff like that before you get in the real world with a real device and have it not working the way you're expecting.
[506.60 → 516.34] And so the traditional way has been having these massive clusters of CPUs, and it's been incredibly expensive to do that historically.
[516.60 → 523.18] And you often saw that in, you know, government-sponsored laboratories that, you know, were associated with government programs.
[523.28 → 530.50] I mean, like off the top of my head, things like the Livermore Computing Centre, the Lawrence Livermore National Laboratory they maintain, and there are others out there.
[530.50 → 543.94] But that's kind of what I think people traditionally think of is being able to say, I need to apply, you know, 10,000 or 20,000 CPU cores to a problem in massive parallel to work through it.
[544.24 → 548.40] And so that's how I see it historically, but it's not really how I engage it personally.
[549.26 → 553.66] So maybe we can just kind of dig into a couple of these jargon things that you mentioned.
[553.66 → 568.52] So when you're talking about a cluster, I mean, we're talking about a certain number of compute instances, whether those be virtual machines or physical nodes that are working in concert to do something.
[568.70 → 573.66] Now, I'm sure people are also maybe thinking like, oh, well, in the cloud, I can have like a Kubernetes cluster.
[573.66 → 575.70] I can have a bunch of instances, right?
[575.72 → 579.04] Or on-prem, I can buy a bunch of servers and hook them together.
[579.04 → 600.96] But am I right in like one of the elements of an HPC cluster is really that the nodes are tied together in a specific way, like even hardware wise, that makes them, for example, communicate very differently, maybe than a standard kind of on-prem infrastructure for running web servers or something like that.
[600.96 → 607.38] Like they can communicate in a sort of very efficient way and also handle kind of very large amounts of data.
[607.38 → 615.96] Is that like one of the differentiators between like, let's say, a bunch of on-prem servers running websites and a high-performance computing cluster?
[616.64 → 617.62] Yeah, I think so.
[617.74 → 625.52] And as I try to answer this, I want to acknowledge that the CPU cluster side and the software stacks that go into is not my area of expertise.
[626.12 → 628.42] And so I kind of want to go into that.
[628.42 → 635.46] I'm bringing kind of the AI ML perspective where I'm much stronger talking about the things that you and I often do, Kubernetes and stuff.
[635.46 → 638.78] But part of it I've discovered is really cultural.
[639.00 → 643.16] There are software stacks that are applied to tie these clusters together.
[643.68 → 645.90] They tend to be closer to the hardware.
[646.16 → 656.34] In a lot of cases that I've seen kind of generalizing some of the use cases I've seen where people have put together different architectures, you'll sit down at a terminal and do like a virtual desktop.
[656.34 → 662.24] But the virtualization across clusters is very, very close to the hardware to pull that together.
[662.44 → 668.26] And so the traditional view of that is very different from how we look at it in the AI world these days.
[668.48 → 676.18] And so it brings some challenges into the case that as AI ML is becoming part of this, and we'll talk about that obviously in a few minutes.
[676.18 → 685.06] But as it's becoming part of that, you have very different paradigms on how these clusters are constructed and how you interface with them.
[685.32 → 688.46] And so there's really – I've learned the hard way.
[688.60 → 692.54] There's really not a great one-size-fits-all across all the use cases.
[693.06 → 697.16] And so if you have all those use cases, maybe lucky people don't.
[697.24 → 703.24] Maybe they're fortunate that they have a particular specialty they're addressing, which reduces the total scope of what they have to do.
[703.24 → 710.64] But if you're addressing many, many different types of use cases, then it can be a struggle to do that, to be able to do that.
[710.70 → 719.48] But like we were talking about Kubernetes, and if you look at more of the traditional CPU side and kind of what I just described about being able to get close to the hardware,
[720.02 → 730.98] there is a technology called Singularity, which is kind of Kubernetes-like, but it's kind of – and I'm going to give a completely non-technical, squishy definition.
[730.98 → 737.68] It's containerization, but it's not in the – quite to the extent you think of, like when you think of Docker and Kubernetes,
[738.20 → 746.94] it would be – it's an open-source project that is a lot more like – it's containerization, but it's a lot closer to what we traditionally think of as VMs.
[747.38 → 752.44] And that's one of the most popular technologies I've seen in this space that people are looking at.
[752.48 → 754.60] And it's not the only one, but it's being open-source.
[754.60 → 760.14] It's a good one to talk about since we tend to advocate for open-source solutions on the show here.
[760.54 → 765.20] And so that's one where that community is culturally trying to take advantage of containerization,
[765.44 → 772.00] but probably not the way some of us who have come from traditional Docker or Kubernetes over in recent years would think of.
[772.04 → 773.34] It's not quite to that point.
[773.34 → 781.52] So kind of what I'm hearing a little bit is that – and I'm just kind of trying to break it down for my simple mind, I guess.
[781.64 → 786.44] Like if I think about – let's say I have instances in the cloud, right?
[786.54 → 793.50] There would be ways for me to spin up a huge number of instances, run some like Python thing on all of them
[793.50 → 796.34] that communicates all between all the nodes and all of that.
[796.34 → 804.38] But really what I'm doing is I'm spinning up these sorts of generic environments that are really geared towards a wide set of applications
[804.38 → 811.32] from web servers to data processing to databases to whatever it is I can run on those instances.
[811.32 → 812.80] They're meant to be generic, right?
[813.24 → 818.22] Whereas kind of what I'm hearing is that an HPC cluster, like from the start, you say,
[818.22 → 827.46] well, this cluster, I'm going to build this so that it can run massively parallel data-intensive applications at scale.
[827.70 → 831.46] What do I need to put into this cluster to make that happen?
[831.56 → 836.04] And I guess that could include things like specialized connections between the nodes.
[836.14 → 838.10] It could include specialized hardware.
[838.42 → 843.42] It could include specialized software setups, specialized like queuing systems and job scheduling,
[843.96 → 847.06] specialized ways of dealing with containers and virtualization.
[847.06 → 856.34] So it's really kind of the amalgamation of all of those things together that are really geared towards the specific use of the cluster, I guess.
[856.50 → 857.40] Would that be accurate?
[857.94 → 858.94] It would be.
[859.14 → 865.70] And most of that is going to be outside my area of expertise because we have other amazing people on the team that know that stuff inside out.
[865.88 → 867.48] And so I am learning that.
[867.60 → 871.00] And when I say that, I'm talking about the kind of the CPU side of the equation.
[871.00 → 876.04] And so there are schedulers, like I mentioned Singularity, and it does schedule, and it does containerization.
[876.36 → 880.74] And it's designed to take advantage of all those processors across the cluster.
[881.22 → 887.06] And so in that way, it's similar to the world that you and I more often operate within.
[887.06 → 889.56] But it's not exactly the same.
[889.74 → 902.30] And currently, if you try to apply more of a traditional CPU-based simulation paradigm, it doesn't work well in a Kubernetes cluster because that was one of the first things I learned as I explored this thing.
[902.40 → 903.42] Why aren't we using that?
[903.56 → 905.08] Or why wouldn't somebody use that?
[905.20 → 909.34] And so there are reasons that are largely beyond my expertise that I was given.
[909.34 → 911.42] And I trust those experts at that.
[911.52 → 913.22] I have learned that they really know their stuff.
[913.30 → 915.76] And so we have that represented on our team.
[915.90 → 917.36] And I kind of leave that alone.
[917.46 → 931.08] And so on of the things that I have really been focusing on myself is more on the AI ML side, which looks a lot more like the environment that we're used to in terms of largely, you know, not even specific to our company.
[931.08 → 940.36] But in general, there is an expectation in high-performance computing now that AI ML use cases are now requiring that level of computation.
[940.68 → 950.84] And so we're seeing this kind of rapid race up the curve where, you know, originally people would say, I have a GPU to run things on.
[950.92 → 956.18] And then they said, I have a small cluster that's either on-prem or, you know, now cloud providers that are providing that.
[956.18 → 970.60] And as our industry on the AI side and machine learning side becomes more sophisticated and our models are becoming more complex and stuff, the need to drive that computation for highly complex use cases is really shooting up.
[970.66 → 981.52] And also it's interesting that a lot of the traditional simulation side that would traditionally have been done on a CPU-based cluster, you're seeing some of that come over into a GPU world at this point.
[981.52 → 988.48] So the AI ML workload perspective was really not part of high-performance computing until fairly recently.
[989.04 → 991.90] And now you're seeing those two worlds merge right now.
[992.08 → 993.82] So it's a very fast-moving field.
[1004.52 → 1010.10] This episode is brought to you by Brave.
[1010.10 → 1018.18] The Brave team is on a mission to fix the web by building an open source, privacy-focused, and performance-oriented browser.
[1018.76 → 1021.68] Browse the web up to eight times faster than Chrome and Safari.
[1022.20 → 1024.22] Block ads and trackers by default.
[1024.56 → 1028.30] And reward your favourite creators with the built-in basic attention token.
[1028.90 → 1030.16] Yes, you heard that right.
[1030.26 → 1032.34] A real-world use case for blockchain.
[1032.74 → 1038.34] Download Brave for free using the link in the show notes and give tipping a try on changelog.com.
[1040.10 → 1040.58] Okay.
[1040.58 → 1040.60] Okay.
[1040.60 → 1058.80] So when we say something is going to run on an HPC cluster, and it's massively parallel and processing massive amounts of data,
[1058.80 → 1065.92] could you give us kind of perspective on what approximately the scales we're talking about are?
[1066.12 → 1067.98] I know you mentioned a certain number of CPUs.
[1068.02 → 1073.88] Could you kind of just give us a perspective on how big are these clusters that we're talking about?
[1074.42 → 1074.62] Sure.
[1074.62 → 1089.62] So on the CPU side, a large use case can consume tens of thousands of cores to run simulations, you know, in tremendous detail and be able to do all the parallel computation that's required of that.
[1090.00 → 1096.02] That is not just people from our side with our bias tend to think, oh, well, that's going to be eclipsed, and the world goes GPU.
[1096.02 → 1100.84] But there are many use cases that are not necessarily specifically optimized for GPU.
[1101.06 → 1102.44] You're seeing some crossover there.
[1102.84 → 1113.92] And there are companies out there, you know, that are in the GPU space, NVIDIA being one of them, that are basically trying to pull traditional CPU-based use cases over into the GPU world.
[1114.30 → 1120.24] And you have to kind of do that assessment of what that means to your organization and the projects that you're involved in.
[1120.24 → 1125.34] But, you know, it's kind of funny on so you can get to that level on the CPU side.
[1125.38 → 1138.60] But on the GPU side, it's interesting that as HPC is really addressing the artificial intelligence machine learning space at this point, then you get into a situation where you can almost consume for really sophisticated training techniques.
[1138.60 → 1141.56] You can consume a tremendous amount of computation.
[1141.56 → 1146.94] So it's really not always about just I have X number of GPUs.
[1146.98 → 1148.28] OK, that's my requirement.
[1148.28 → 1159.02] Going forward, we have, you know, the concepts, you know, in training of like, you know, mass hyperparameter exploration where you're trying to find optimal sets of hyperparameters for your AI model.
[1159.56 → 1167.88] And you're training them in parallel varying hyperparameters so that you can find the various, you know, performance gains and optimizations to do that.
[1167.98 → 1173.84] And that's one way where you essentially can kind of absorb all to compute that's currently available to you.
[1173.84 → 1176.58] And then there are other things like deep reinforcement learning.
[1176.70 → 1186.28] We'll get into things like large scale self-play where you are allowing the agents to run and going through that training cycle of deep reinforcement learning.
[1186.28 → 1191.32] Also in parallel to speed up and to also find different avenues through that.
[1191.54 → 1195.12] And then at the end of the day, those are kind of served by autoscaling anyway.
[1195.34 → 1201.10] So it's less of, well, I have X number of GPUs, and I'm going to run with that over a given period of time.
[1201.16 → 1202.00] That meets my requirement.
[1202.14 → 1206.14] More like if we're going to do something like this, how much capacity do I have right now?
[1206.14 → 1212.76] It may be that in my prior effort with a slightly different approach, I only needed a certain number of GPUs.
[1212.80 → 1217.78] But if I'm, for instance, going to jump into doing this mass scale hyperparameter exploration,
[1218.10 → 1227.08] I might try to suck in every GPU I can to get through that so that I can get through it in minutes or hours instead of days or weeks or months.
[1227.52 → 1234.82] And so there's this, I guess, the elasticity necessary in your high performance computing cluster becomes very important.
[1234.82 → 1239.50] And so you have to have strategies that can accommodate those types of use cases.
[1240.10 → 1242.44] I'll definitely say that it's impressive.
[1242.96 → 1247.82] Like you said, the amount of compute that's needed even to train like a single model in certain cases.
[1247.82 → 1250.10] And it certainly explores hyperparameter spaces.
[1250.38 → 1255.26] So for those that might not kind of understand this whole idea of hyperparameter optimization,
[1255.26 → 1262.48] like if I'm going to train my neural network, I have to make decisions and put in user defined parameters, right?
[1262.48 → 1266.82] These parameters that are not set through the training process that are things like, you know,
[1266.88 → 1274.22] the number of nodes in this layer or my learning rate or like a dropout or something like that.
[1274.32 → 1275.98] So there's all these parameters.
[1276.24 → 1282.30] And one way of figuring out how to best set those parameters to get the best model is to just try a bunch of them, right?
[1282.34 → 1288.22] Which obviously takes a lot of computational power, but you are kind of exploring that whole space.
[1288.22 → 1292.32] I just read some people probably say you might have seen this too, Chris.
[1292.50 → 1299.00] There was an article recently that kind of showed how some of the large scale language models that are being trained now,
[1299.08 → 1308.50] like training one model took about or contributed as much carbon input to the atmosphere as running like five cars for their entire lifetime of use,
[1308.88 → 1313.24] which is just like, I don't know, like putting it in terms of something that like hits home real,
[1313.24 → 1317.88] real world like that you interact with daily rather than like petalous or something like that.
[1317.88 → 1328.38] It just really hits you that this is significant in very technically interesting ways, very impactful ways and in a positive sense,
[1328.50 → 1331.80] but also potentially there's side effects there as well.
[1332.30 → 1332.68] There sure are.
[1332.76 → 1337.98] I mean, anyone who's been with his listening to the show for long knows that you and I are both incredibly social conscious people
[1337.98 → 1342.56] in terms of, you know, how we perceive the world and the kinds of choices that we make.
[1343.08 → 1352.34] And so this is definitely a weak spot in dealing with providing massive amounts of computation within a reasonable time period that needs to be addressed.
[1352.54 → 1360.88] And so, yeah, I remember when that came out about the, you know, running five cars or whatever it was for a year, and I was a little bit stunned.
[1361.16 → 1363.66] And so it's one of those things that we need to figure out.
[1363.66 → 1364.62] Yeah, definitely.
[1365.16 → 1374.84] So let's kind of jump back to and maybe turn a little bit towards the HPC for AI and how these worlds are colliding.
[1374.94 → 1383.64] Because I remember, for example, when I did that internship that I mentioned, the primary applications that I was working with were climate modelling applications.
[1383.64 → 1389.28] So I know people have kind of used these sorts of clusters for quite a while for these sorts of climate models.
[1389.28 → 1404.96] I know also in grad school when I was doing like computational chemistry calculations where you're basically trying to calculate properties of materials based on what you know about how the physics work for atoms and molecules.
[1405.46 → 1412.14] So we were kind of submitting jobs to HPC clusters at that time in a couple of different places around the country.
[1412.14 → 1425.12] And so I know that there's been kind of this history of HPC clusters being used for this large scale, like you said, simulations and scientific computations and those sorts of jobs.
[1425.66 → 1435.22] But I also know, you know, recently I was talking to, so I live in the same town where Purdue University is, and I was talking to one of the data scientists that works for Purdue University.
[1435.22 → 1445.40] And he was saying that now they have a set of nodes, and they're continually buying more that are specifically geared towards AI applications.
[1445.60 → 1448.90] So I know that this is happening, and obviously you're working in this area.
[1449.06 → 1464.06] So could you kind of describe maybe why HPC is relevant for AI, and maybe when would I want an HPC cluster for doing AI versus maybe just spinning up some stuff in the cloud and vice versa?
[1464.06 → 1477.90] So, yeah, it's a level of really where a use case requires the horizontal scale of what a cluster provides because you're still using the same GPUs, you know, for that.
[1478.20 → 1489.32] But the question is, you know, the cluster gives you the advantage of saying, like, I can go get the latest NVIDIA GPU or any of their competitors and be able to say, OK, I'm going to go do this for my project.
[1489.32 → 1498.32] You can be a student and go do that and run it on one or go to these cloud services where you say, OK, I'm going to I'm going to lock into a, you know, a perfect GPU there and use it.
[1498.74 → 1503.18] In industry, though, there are use cases and I haven't only run into this at Lockheed.
[1503.22 → 1504.62] I've run into it previously as well.
[1504.62 → 1525.80] You'll be dealing with a solution that may not only have challenging models to train, but in many cases you have many, many models that are working together, that are collaborating, where each model is narrowly performing a particular task, you know, in terms of its inference, that it's performing it with great accuracy.
[1525.80 → 1537.48] But because of the scope of what you're tackling in the problem set, there may be many of those type tasks, and you have different models that are applied to each one, but they have dependencies across them.
[1537.62 → 1548.34] You know, they're not standalone in the sense of each model may be only attending to its own input and inference and output, but some of those inputs may be from other model outputs and stuff.
[1548.34 → 1559.24] And so you may have to manage quite a few models that are interrelated and those relationships matter as much as just the construction and training of the model itself.
[1559.24 → 1573.92] And so on of the advantages about having a cluster is if you're dealing with a complex use case like that, where you have this kind of tight dependencies between different models, then it may not be just retraining one.
[1573.92 → 1582.90] And it may be that one model and how it's performing and what it's doing and the choices you make there affect other models that are highly dependent on it.
[1582.98 → 1589.86] And you may change what kind of parameters, hyperparameters you're using and stuff like that that can alter the inference itself.
[1589.86 → 1594.40] But you're having to look at it from a system perspective instead of just a model perspective.
[1594.40 → 1598.50] And so clusters can be really effective when you're iterating on those types of things.
[1598.50 → 1603.92] And you're having to get a lot of training done for every iteration and then be able to go back.
[1604.06 → 1607.32] And you don't want to wait weeks or months because it's not realistic in the real world.
[1607.56 → 1614.60] Without the cluster, the problem that you're trying to solve would not be practically doable in the real world.
[1615.10 → 1615.80] It's fascinating.
[1615.92 → 1617.44] And I definitely see the advantage there.
[1617.88 → 1622.92] But maybe it's like my cheapness or the fact that I work for a nonprofit or something.
[1622.92 → 1627.00] But I'm thinking like, oh, like it seems like there's so much risk.
[1627.00 → 1640.26] Like you're saying, no matter what comes out from NVIDIA, like the latest GPUs, the latest accelerators, types of software that you can run on certain architectures, all of that's pretty much available very quickly in the cloud.
[1640.26 → 1644.32] And so you can have access to that sort of thing very quickly in a flexible way.
[1644.32 → 1658.90] And it is just like it kind of brings about a little bit of fear in me if I think about, oh, like we're going to choose to invest in a specific like architecture and build out this huge cluster, which I'm guessing like takes a ton of time.
[1658.90 → 1661.00] It obviously takes a ton of money.
[1661.00 → 1670.92] And then like technology is progressing so quickly that like how are you not scared that like you build this thing and then like it's obsolete in a year?
[1671.12 → 1677.30] How does that like how does that sort of work in a company or in your strategy?
[1677.94 → 1679.68] No, that's a great question.
[1679.68 → 1691.70] And the HPC strategy has to accommodate that natural refresh, that natural progress, because you don't want to buy into a technology and expect to just to leave it there.
[1691.86 → 1695.70] So it's not something that you just go do and walk away from.
[1695.80 → 1701.38] You're going to do it in many phases that accommodate changes in what's available to you.
[1701.38 → 1705.56] And you try to you try to look ahead and structure that automatically.
[1705.76 → 1709.76] And then you try to take advantage of what you're trying to accomplish.
[1709.76 → 1718.38] For instance, some of the kind of more typical principles that you're going to find in HPC strategy that you're trying to accommodate is you're trying to remove barriers to innovation.
[1718.38 → 1730.14] And you're trying to allow with one of these clusters the ability to kind of develop anywhere with a consistent user experience and deploy wherever you need based on your different use cases.
[1730.14 → 1746.62] You need a solution stack that is kind of consistent with what people would expect to find, whether it's inside your own organization or external to that as you bring a new talent and be able to allow that stack to evolve over time and refresh.
[1746.84 → 1751.58] And it needs to support things like agile development and iterations and such as that.
[1751.58 → 1762.56] And then kind of what I just alluded to is that user experience is really, really crucial because you can put a huge, amazing cluster that you're investing many, many millions of dollars into.
[1762.70 → 1777.96] But if your user experience is a very bad one, either you drive users away, and they seek out other alternatives, or you reduce their productivity, and you reduce their ability to rapidly work on the problem set that they're trying to.
[1777.96 → 1790.34] And all those things hurt your organization. And so with all of those into account, taking those into account, you have to think about, you know, some of the more obvious things are like on prem versus cloud in terms of how you're structuring.
[1790.48 → 1793.98] And hybrid is another popular thing that people are talking about.
[1793.98 → 1799.30] And so how does your population of data scientists, how do they use it?
[1799.32 → 1807.82] Are they tending to do it just here in certain hours, or maybe will they have a week of intense usage, and then they're not doing much model training in the weeks to follow?
[1808.04 → 1815.28] Or do you have a consistent level of training requirement available kind of round the clock, seven days a week that you're doing?
[1815.42 → 1817.82] How do those moments spike over time?
[1817.82 → 1822.08] Yeah, so I'd love to dig into that user experience.
[1822.42 → 1828.44] So I should clarify that the main reference I have for this is like back when I was doing this stuff in my internship and other things.
[1828.48 → 1834.52] And just for reference, like the user experience with that was like, OK, here's what I'm going to do.
[1834.56 → 1838.44] I'm going to log in to my home space in the cluster.
[1838.44 → 1848.90] The first thing I've got to do is install or actually compile this Fortran code against whatever sorts of things are on the cluster, which I'm not totally sure what's there.
[1849.46 → 1854.22] And like basically it would take me days to get things like configured correctly.
[1854.22 → 1861.02] And then I'd have to submit a job to a job queue and wait for that job to get queued on the cluster.
[1861.30 → 1871.42] And then like it would get queued, whatever, however many hours later I would get a notification that I had oversubscribed memory and like my job crashed or something.
[1871.42 → 1874.50] And then I'd like kind of queue it again and go again.
[1874.50 → 1881.58] If I compare that to sort of my workflow now where I'm thinking about, oh, well, I'm going to write some Python.
[1881.76 → 1885.82] I'm going to push it up to a node in the cloud.
[1886.04 → 1892.00] And I'm just going to use like a S3 client to pull down some data from an object store.
[1892.50 → 1893.90] And then I run my job.
[1893.98 → 1894.96] There's a GPU on there.
[1895.06 → 1900.36] Like that workflow is just so vastly different from what I remember from the HPC world.
[1900.36 → 1907.40] Like even the data side of things in the HPC world, I remember like there was literally a tape silo.
[1907.50 → 1914.10] For those that don't know what a tape silo is, it's like a data store where things are written to these physical tapes.
[1914.28 → 1925.60] And there's a little robot arm in there that like when you submit a job, and you say, I want to attach this storage, the robot arm goes over and grabs the tape and like puts it in to something.
[1925.60 → 1926.78] I don't know exactly.
[1926.94 → 1931.76] I still don't know exactly how it works and then connects that to your node so you can have access to it.
[1931.80 → 1941.56] So it's just like these two worlds are like the workflow side of things, user experience side of things, at least in the back of my mind and how I think about it seems so vastly different.
[1941.78 → 1947.32] Are there ways to bridge that gap now to where like, oh, I can spin up a Jupyter notebook and run a job on a cluster?
[1947.44 → 1949.42] I don't actually know what's possible.
[1949.42 → 1968.08] Yeah, so I mean, probably a good place to start for that answer is looking at the cloud providers that we already are familiar with and creating that user experience for the best possible workflow for a typical user is something they are spending an enormous amount of time on.
[1968.08 → 1976.22] And so, you know, all of them, you know, Microsoft and Amazon and Google and NVIDIA with their cloud and stuff, they all have approaches.
[1976.22 → 1983.88] Speaking only for myself, I think my favourite of all those having used multiple of them is probably Google Collaborator.
[1984.32 → 1995.28] And so where it gives you kind of free Jupyter notebook environment that you can use within cost, like if you're doing something as a project on your own time and not necessarily working with clusters and stuff.
[1995.28 → 2003.24] But the ability to just get into a notebook and do that with just individual GPUs, they've really, I think, done a good job of making that seamless.
[2003.38 → 2011.84] And I think so one of the challenges right now that there are, you know, companies that are doing like one of them is a proprietary solution by Domino Data Lab.
[2011.92 → 2024.14] I know they're out there and there are others as well that are trying to take that kind of simplicity in your workflow and apply it to large scale clustered environments.
[2024.14 → 2027.86] In my view, I don't, I haven't seen anyone that I thought was perfectly there yet.
[2027.98 → 2036.14] There's nobody that I'm seeing do that so far that I think is doing it with the simplicity that I love, like I said, in Google Collaborator.
[2036.88 → 2038.68] And so I'm hoping to see that.
[2038.98 → 2043.40] Particularly, I would love to see open source solutions that will allow us to get there.
[2043.50 → 2049.34] But I really think if you don't support your users well in that way, you're just going to reduce your productivity and increase your cost.
[2049.34 → 2060.08] Okay, so we've talked a lot about like what an HPC cluster is, how the experience kind of differs, what the scale of these things are.
[2060.24 → 2063.74] Could you describe some of the AI use cases?
[2063.82 → 2067.28] So you mentioned like reinforcement, learning, self-play, these other things.
[2067.68 → 2073.06] I'm curious if there's like particular, I guess you mentioned hyperparameter tuning as well.
[2073.06 → 2080.30] If there are particular types of AI problems or parallelism that fits really well in an HPC setting.
[2080.44 → 2087.02] And maybe also if there are types of AI workflows that would not fit well in an HPC setting.
[2087.96 → 2088.12] Sure.
[2088.30 → 2093.02] I think it's less about the specific application.
[2093.02 → 2098.42] And it's more about how you're combining different models across.
[2098.42 → 2103.00] So you may have a problem where you're building a model, and it can be any of the things.
[2103.10 → 2108.92] It can be a CNN convolutional neural network, or it can be a generative adversarial network or whatever.
[2109.24 → 2111.34] And you can do those without clusters.
[2111.76 → 2118.92] I think the place where the cluster becomes very advantageous is when you are combining a bunch of those together.
[2118.92 → 2122.32] You could almost think about it as like using Legos.
[2122.50 → 2126.72] And you have different Lego parts that are each representing a different building block.
[2126.80 → 2131.54] And you put those together to build your little Lego house or whatever you care about.
[2131.90 → 2137.92] And when you're trying to iterate on those issues where you're combining a bunch of different models.
[2138.04 → 2141.24] And there are a lot of dependencies between those models.
[2141.44 → 2143.12] I guess in that way as I'm hearing myself talk.
[2143.20 → 2146.72] It's not so different from enterprise scale software development in general.
[2147.04 → 2148.44] It's not even specific to AI.
[2148.44 → 2151.92] You develop a model architecture to solve the problems.
[2152.26 → 2154.86] And so it's not one at a time.
[2155.04 → 2159.48] It's that massive horizontal parallelism that you need to iterate.
[2159.96 → 2167.72] And when you find a use case that needs that massive horizontal scale to iterate effectively in a timely manner.
[2167.90 → 2169.44] That's where the cluster really helps.
[2169.44 → 2180.88] The other place would be the fact that if you're a large organization or a cloud provider that is serving many, many different teams of people working on problems.
[2180.88 → 2184.36] And you have, you know, they all are using a certain amount of capacity.
[2184.36 → 2191.82] And you're trying to accommodate many different use cases with many different characteristics in how they're using the resource.
[2191.82 → 2196.42] Then that's where a cluster and being able to provide it in a form of a cloud.
[2196.52 → 2200.22] I don't necessarily mean a cloud provider like Amazon, Google, Microsoft.
[2200.42 → 2201.44] It can be an internal cloud.
[2201.64 → 2213.62] But you need to be able to handle those and make sure that all the people, all the teams in your organization are able to be productive when they need to be productive without you being the single point of constraint on them.
[2213.62 → 2230.00] And so, you know, that certainly has a lot to do with why any large organization is going to invest in this is being able to ensure that that all of their business units are never constrained by compute resources that, you know, they may be constrained by their problem set or whatever, but that to compute is not the issue.
[2230.00 → 2247.52] So I guess, I mean, there are cases where companies will have a sort of on-prem infrastructure that's more generic, like kind of a cloud-like environment, their own infrastructure where they're trying to enable generic workloads.
[2247.52 → 2262.78] But it sounds like a lot of the things that you're talking about, or at least there are a good number of organizations like Lockheed or others that are specifically building clusters that are geared specifically towards AI, right?
[2262.88 → 2268.84] I'm guessing that like you're not going to build out a whole like a thousand GPUs or whatever.
[2269.00 → 2276.20] I don't know what the scale of the GPUs are in these sorts of clusters, but you're not going to build out that sort of thing for just generic workloads.
[2276.20 → 2283.72] Like you're making a commitment for the long term to really invest in AI applications with this cluster, right?
[2284.20 → 2293.54] What sort of pressure does that create in terms of, I'm assuming once you have that cluster in place and, you know, I don't know what the scale of the investment is, but I'm sure it's amazing.
[2293.98 → 2301.08] What sort of pressure does that create to really be squeezing everything you can out of that cluster?
[2301.08 → 2306.52] How do you kind of make sure that your AI is so dynamic, and it's changing so quickly, right?
[2306.58 → 2321.06] How do you kind of guess, you know, oh, I'm going to need this scale of cluster for all of these AI sorts of problems that we're solving when AI itself is changing so rapidly and the types of models are changing so rapidly and all of that?
[2321.06 → 2334.10] Well, I think, first, we have a lot of great strategic partnerships out there with other organizations that have similar interests and in some cases similar scale in terms of what they're trying to address.
[2334.10 → 2343.46] So it's not only building out the infrastructure, you have to buy the hardware, and you have to kind of make an estimation on what you think your GPU utilization might be.
[2343.66 → 2347.46] If you don't have a lot of history in that, that can be a real challenge.
[2347.54 → 2354.10] And I think every organization I've ever been a part of over the last few years or talked with has had to tackle that.
[2354.20 → 2357.18] And I don't think, I don't know that there is a great way of doing it.
[2357.18 → 2368.60] But I think part of it, part of the challenge in answering that question is that to some degree, if you do a good job of it, then if you build it, they will come, you know, to use the field of dreams quotes there.
[2368.82 → 2383.96] If you have a great infrastructure that suddenly increases people's productivity, then whatever your historical thing has been in terms of utilization and uptake on your systems, you're very much likely to have an uptick on that when you provide a great way of engaging on that.
[2383.96 → 2392.20] So you kind of have to accommodate that your success factor of, wow, I'm meeting everyone's expectations, and now it's almost getting the better of me if I'm not careful.
[2392.76 → 2398.38] And then you have to make sure that not only is the hardware refreshable, but that the software is extendable too.
[2398.48 → 2412.14] If you think how fast any one of the things that go into this, you know, if we talk about a Docker Kubernetes stack, and you think about all the advances in Docker and Kubernetes and that they are constantly evolving because they're in such widespread use.
[2412.14 → 2415.78] And then those are not specific to an AI workload.
[2416.02 → 2429.08] So I know that like because they have public stuff out there, you know, NVIDIA has a production grade AI platform that they use internally on their own massive, massive stack that they have for their self-driving car stuff, which is called Maglev.
[2429.28 → 2433.24] And you can Google Maglev and there's some information out there on it.
[2433.32 → 2435.58] Not a lot because it's not a product that they sell.
[2435.58 → 2441.92] It's an internal thing, but they, I know that's how they approach within the context of being inside a Kubernetes cluster.
[2442.08 → 2449.82] It's how they approach all the AI specific workflow tasking that has to happen to make something work well.
[2450.18 → 2454.94] And Google has their approach and Amazon and Microsoft, they all have their approach.
[2454.94 → 2459.76] And we may eventually see some good open source solutions to be able to do that.
[2460.08 → 2461.88] But it's not just a hardware thing.
[2462.04 → 2470.32] We tend to get locked up into when you think of HPC as just the hardware, but you have to have a stack, which is enabling all the things you have to do in your workflow to get it done.
[2470.44 → 2476.92] So it's quite a lot to think about and especially allow being growing at varying paces throughout the stack.
[2477.58 → 2479.30] Yeah, that's a great explanation.
[2479.30 → 2488.72] I guess maybe to turn to a more forward-looking question, what excites you about the future of AI on HPC?
[2488.98 → 2496.16] Or what trends are you seeing in terms of HPC usage for AI applications?
[2496.54 → 2501.96] And what of those are the things that you're most excited to follow and be part of?
[2501.96 → 2514.66] I think it's really tied into how I see AI itself going forward because the AI side of HPC, the HPC is the enabler for what you're trying to do with AI models.
[2515.24 → 2526.78] And so what we're seeing an explosion of over the last few years is just in the time we've been doing this podcast, it used to be people talked about building a great model to solve their problems.
[2526.78 → 2540.00] And now you're seeing production cases where you might have many models working in a solution, and you're seeing the commoditization and democratization due to these oftentimes open source software driving it that is really driving the cost down.
[2540.00 → 2556.58] So just as people's desire to solve more and more complex problems with a variety of neural network solutions working collaboratively together is increasing very rapidly, I think you're going to see that the providers are doing that.
[2556.58 → 2573.52] You're going to see all the major cloud providers certainly moving from let me grab a GPU to clustering as a service and being kind of the way you think of it to where you may have service agreements that accommodate a baseline of a number of different GPUs with different types of elasticity models in there.
[2574.02 → 2580.58] If I go and look right now, I'm not up-to-date on the latest offerings in all cases, and I need to see if some of them may already be starting to do that at this point.
[2580.58 → 2590.58] But that's going to become really common, I think, because certainly all the large organizations like the one I belong to are, this is becoming a standard part of many things.
[2590.58 → 2608.84] A year or two ago, doing neural network development was still a bit of a specialization, and I think what we're seeing is that it is now becoming part of system and software development in general and becoming a very standard skill that's expected to be part of any solution going forward.
[2608.84 → 2618.94] And so I just think the HPC space is rapidly expanding and advancing to be able to accommodate this exponential AI growth that we're all experiencing.
[2618.94 → 2638.62] Given that, I know there's probably people out there thinking maybe that are excited by this, and they would eventually love to be working with Lockheed or other larger organizations, maybe even government organizations that actually have the ability to build out these large scale clusters, right?
[2638.62 → 2641.60] Or maybe there's people working in academic research.
[2641.74 → 2647.06] A lot of times academics use HPC clusters that they get grants for and that sort of thing.
[2647.06 → 2656.38] Assuming people don't have the funds to set up their own HPC cluster in their basement or something, which I'm guessing there's very few of those people out there.
[2656.38 → 2667.66] Are there any ways to kind of learn at least a little bit about some of the ideas around HPC that people could dig into in terms of a learning resource?
[2668.44 → 2676.18] Yeah, I think we're just getting to where this kind of updated version of HPC is starting to develop now that AI is now part of that story.
[2676.18 → 2682.26] And I know that I ran across an Udacity course that is being done.
[2682.46 → 2684.50] It's high-performance computing by Georgia Tech.
[2684.84 → 2688.90] And I have not taken the course myself, but it's one of their NATO degree programs.
[2689.16 → 2692.50] And I think that would probably be a good place to start.
[2692.80 → 2696.98] And not everything, just to point out, I mean, you can have a smaller cluster that you can build.
[2696.98 → 2705.38] And, you know, you can get several HPC servers or something or put that, you know, your own solution and network them and try out with some of the software that's becoming available.
[2705.38 → 2712.62] And then, like I said, especially to a handle, that makes more sense if you're going to be running models kind of around the clock.
[2712.86 → 2719.00] If you're very occasional, like I need a lot once in a while, then cloud providers are probably a more economical way to go.
[2719.10 → 2723.48] Or some hybrid of in-between, about a baseline of training that you're looking at.
[2723.48 → 2730.00] And you can set up a much smaller version in your organization than what a Fortune 100 company might be doing.
[2730.22 → 2736.08] And so it doesn't all have to be at massive tens of millions of dollars or more scale to be able to do that.
[2736.20 → 2741.64] As the cost of hardware has driven down, try something small, mess around with it, take these courses.
[2741.88 → 2744.82] There's new information coming online all the time if you're Googling.
[2745.22 → 2747.68] And see what the various vendors are offering.
[2747.78 → 2750.92] Because a lot of great information comes by looking through the various vendor sites.
[2750.92 → 2754.78] Yeah, I'd also like to advertise a little bit.
[2754.84 → 2764.06] If there's anyone listening to the podcast who is in college or studying computer science, studying sciences or AI in college.
[2764.26 → 2767.22] And you're looking for an internship after college.
[2767.22 → 2770.24] And you're kind of interested in this high performance computing space.
[2770.40 → 2772.74] I mentioned that I did that internship at NCAR.
[2772.74 → 2783.08] And that was just like, yeah, it was such an amazing time for me to be able to be hands-on with these just amazing supercomputers.
[2783.48 → 2789.08] And getting to like really be hands-on with some of the latest technology on that front.
[2789.28 → 2794.36] Even getting to participate in a high performance computing conference and other things.
[2794.54 → 2797.96] So that internship program, it's called the Sci Parks Internship.
[2798.40 → 2799.98] And they have it every summer.
[2800.08 → 2800.88] It's still going on.
[2800.88 → 2807.14] So if any of you university students out there are looking for something to do, I'd highly recommend that.
[2807.50 → 2809.64] And I'll link that in the show notes as well.
[2809.90 → 2813.26] But it was really great to have this conversation, Chris.
[2813.36 → 2814.94] Things are changing so much.
[2815.20 → 2819.74] And it's really nice to kind of orient myself with a little bit of this technology.
[2820.14 → 2826.02] And I'm excited to see where it goes and how you're involved with it over time.
[2826.44 → 2830.18] So thanks for indulging me and letting me interview you a bit today.
[2830.18 → 2831.40] I appreciate it.
[2831.44 → 2838.08] I'm going to take this awkward guest hat off and put my co-host hat back on, which is a much more comfortable hat for me.
[2838.22 → 2839.82] So thanks for doing this, Dan.
[2840.10 → 2840.92] Yeah, definitely.
[2841.20 → 2842.48] We'll talk to you soon.
[2843.02 → 2843.52] Thanks a lot.
[2843.62 → 2843.78] Bye.
[2843.78 → 2846.80] All right.
[2846.84 → 2849.48] Thank you for tuning into this episode of Practical AI.
[2849.74 → 2851.20] If you enjoyed the show, do us a favour.
[2851.32 → 2851.90] Go on iTunes.
[2852.04 → 2852.70] Give us a rating.
[2853.00 → 2854.84] Go in your podcast app and favourite it.
[2854.92 → 2857.66] If you are on Twitter or social network, share a link with a friend.
[2857.74 → 2860.10] Whatever you got to do, share the show with a friend if you enjoyed it.
[2860.40 → 2863.06] And bandwidth for Changelog is provided by Vastly.
[2863.18 → 2864.62] Learn more at Fastly.com.
[2864.62 → 2868.02] And we catch our errors before our users do here at Changelog because of Rollbar.
[2868.24 → 2870.62] Check them out at Rollbar.com slash Changelog.
[2870.94 → 2873.46] And we're hosted on Linde Cloud Servers.
[2873.80 → 2875.40] Head to Linode.com slash Changelog.
[2875.48 → 2875.94] Check them out.
[2876.02 → 2876.86] Support this show.
[2877.26 → 2880.44] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2880.90 → 2882.96] The music is by Break master Cylinder.
[2882.96 → 2886.80] And you can find more shows just like this at ChangeLog.com.
[2886.88 → 2888.92] When you go there, pop in your email address.
[2889.22 → 2895.24] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2895.62 → 2896.42] Thanks for tuning in.
[2896.56 → 2897.28] We'll see you next week.
