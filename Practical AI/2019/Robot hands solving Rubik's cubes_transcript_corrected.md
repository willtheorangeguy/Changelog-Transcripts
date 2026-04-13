[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.42] This is where conversations around AI, machine learning, and data science happen.
[93.42 → 98.20] Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.42 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.16 → 102.28] And now onto the show.
[107.14 → 112.00] Welcome to another fully connected episode of Practical AI.
[112.34 → 117.36] In these fully connected episodes, my co-host Chris and I keep you fully connected
[117.36 → 120.32] with everything that's happening in the AI community.
[120.32 → 124.34] We'll take some time to discuss some of the latest AI news,
[124.56 → 130.36] and we'll dig into some learning resources to help you level up your machine learning and AI game.
[130.74 → 134.52] I'm joined today, as always, by my co-host Chris Benson,
[134.90 → 138.22] who is a principal AI strategist at Lockheed Martin.
[138.66 → 142.38] And I'm Daniel Whiten ack, a data scientist at SIL International.
[142.62 → 143.26] How are you doing, Chris?
[143.38 → 144.18] I'm doing great.
[144.24 → 145.12] How's it going today, Daniel?
[145.60 → 146.76] It is going great.
[146.76 → 156.64] It is a nice fall day here and enjoying the like, two weeks of perfect weather before it's bitterly cold in the Midwest.
[157.34 → 157.52] Yeah.
[157.60 → 159.26] Trying to enjoy that while I can.
[159.54 → 162.08] See, when it gets bitterly cold, you can come down here.
[162.18 → 164.50] I think we're actually going to see each other in Chattanooga.
[165.02 → 166.42] Yeah, I'm excited about that.
[167.10 → 173.34] Yeah, we'll both be at the Project Voice Conference, which is happening in Chattanooga in January.
[173.34 → 176.44] So come by and say hi to us if you're around.
[176.96 → 177.32] Absolutely.
[177.32 → 180.60] We'd love to talk to you about AI and voice and all of those things.
[180.92 → 184.00] And we can talk about our nice, mild southern winters here.
[185.14 → 186.10] Sounds good.
[186.82 → 192.40] Now on to, I guess, some AI news, as this is a fully connected episode.
[192.40 → 208.42] I don't know about you, Chris, but for, like, the past week or however long it's been, about half of my Twitter feed has been, like, jiffies and videos of robot hands manipulating Rubik's Cubes.
[208.56 → 209.90] Has it been the same for you?
[210.04 → 210.46] It has.
[210.54 → 213.92] It's been kind of the big topic as we're recording this over the last couple of weeks.
[213.92 → 221.04] It's been a fascinating thing, and diving into it, as we have both done in anticipation of this talk, has been a lot of fun.
[221.16 → 222.30] So looking forward to today.
[222.90 → 227.70] Yeah, well, maybe to start out with, we should probably get a baseline.
[228.00 → 230.82] How good are you at solving Rubik's Cubes, Chris?
[231.40 → 233.66] So not so good by myself.
[233.66 → 238.88] So if I was going to do it, like, for my daughter, I would cheat and look at one of those algorithms.
[239.08 → 241.36] You know, you can see these manual algorithms.
[241.74 → 242.82] Your daughter might beat you.
[243.06 → 244.98] Yeah, she probably would, actually.
[245.18 → 250.10] I would have to, Daddy would have to go and cheat and look up, because there are solutions out there, you know.
[250.70 → 252.14] Right, methods and such.
[252.20 → 255.28] Yeah, but no, no, for real, I tried it when I was younger.
[255.40 → 256.28] I haven't tried it recently.
[256.72 → 258.00] And utterly failed.
[258.16 → 258.94] So, pathetic.
[259.30 → 261.24] I'm not good at solving Rubik's Cubes.
[261.24 → 262.30] I will admit that.
[262.30 → 264.82] I've had some friends try to teach me various things.
[265.28 → 267.02] I remember one in particular in college.
[267.28 → 271.16] He was one of those just brilliant, naturally brilliant guys.
[271.44 → 274.44] He was one of my friends in the physics program.
[274.78 → 280.90] And when I would ride with him from his house to school, he would always try to solve.
[281.44 → 288.60] So he would drive with one hand and solve a Rubik's Cube with the other hand one-handed while he drove, which I'm not recommending at all.
[288.90 → 290.58] Ooh, doesn't sound like a good idea.
[290.58 → 300.40] Yeah, it was about like a five-minute drive, and he could solve the Rubik's Cube with his one hand, which kind of disgusted me a little bit and was probably not safe in any way.
[300.62 → 305.76] So my question to you is, had he looked at one of those algorithms that you can manually do it?
[305.76 → 307.90] Because I know there's one that I have seen before.
[308.04 → 309.38] I have not memorized it or anything.
[309.38 → 314.50] But you can solve any Rubik's Cube in a certain number of very small steps.
[314.58 → 316.60] I mean, it's less than 20 that you would do.
[317.28 → 319.06] Yeah, I mean, it must have been something like that.
[319.18 → 322.30] Eventually, he went on to like the five by five.
[322.40 → 323.62] So there's like three by threes.
[323.70 → 328.30] And then he went on to like the five by fives, which I can't even comprehend working on.
[328.30 → 331.52] But yeah, that's a little bit too much for me.
[331.52 → 340.62] But maybe not so for OpenAI's Rubik's Cube solving robot hand, which is going to be what we're going to talk about today.
[340.82 → 342.64] They solved the three by three.
[342.76 → 344.44] Maybe they'll go on to the five by five.
[344.60 → 350.94] But yeah, just to clarify, you know, what we're talking about in terms of the robot hand solving the Rubik's Cube.
[350.94 → 365.42] If you weren't aware, OpenAI, a research team there, just published a blog post and a paper, at least a preprint of a paper about using a robotic hand to solve a Rubik's Cube.
[366.16 → 367.88] And it's pretty impressive.
[368.32 → 369.94] What were your initial reactions, Chris?
[370.16 → 371.20] Correct me if I'm wrong.
[371.28 → 376.68] If I recall, they did use one of the standard algorithms for the Rubik's Cube itself, I think.
[376.68 → 383.02] But I believe that most of the training was focused on the articulation of the hand itself.
[383.18 → 384.56] Am I right or am I wrong?
[384.68 → 384.88] Yeah.
[385.02 → 391.82] So there was definitely some pushback against the results, in particular, maybe as related to that.
[391.94 → 393.58] And we can get into that in a bit.
[393.92 → 405.10] But yeah, I think the main point was, like, if you just imagine manipulating a Rubik's Cube with one of your hands and solving it, even for a human, like that manipulation is not trivial.
[405.10 → 425.32] And so the idea that they could get a robotic hand to manipulate this Rubik's Cube towards the solution, even if they are using this sort of other algorithm for the solution, is pretty astounding because it's a really hard manipulation problem, I guess, is the idea.
[425.52 → 425.90] I agree.
[425.90 → 431.04] And I think, I mean, it's almost, whether you're solving the Rubik's Cube is almost an aside in this.
[431.18 → 438.66] I think the fascinating thing, for me at least, was seeing this robotic hand, and there's just one, so you can't, you know, you don't have both hands to put it in.
[438.66 → 446.98] But the robot is both manipulating the Cube in the appropriate directions and using the robotic fingers to pivot the Cube.
[447.20 → 455.86] And the dexterity required to do that is something that I certainly would be challenged myself to try to recreate with my human hand at all.
[456.00 → 464.14] So it was just the ability for the robot to be able to act with that kind of dexterity was just impressive to watch the video that they had on the site.
[464.14 → 471.14] Not only that they kind of solved it once, but they did a bunch of different interesting things with perturbations, too.
[471.24 → 485.08] So this is kind of similar, maybe, to those Boston Dynamics videos and, like, the memes that are also, like, associated with these Boston Dynamics videos where they kind of, like, hit robots with hockey sticks and things.
[485.08 → 495.24] But they hit the robotic hand with, like, a stuffed giraffe and pushed it with a pen and threw a blanket over the hand and other things.
[495.80 → 514.08] And we're testing the adaptation of the hand to be able to continue towards the solution and continue manipulating the Rubik's Cube in light of these things that weren't part of the training data, but were perturbations that it had not been exposed to before.
[514.08 → 521.42] And I think that also is part of the big story here is that the adaptability of the solution, I guess.
[521.76 → 522.00] I agree.
[522.12 → 526.22] They added a lot of variability, which I know we're about to talk toward in this conversation.
[526.22 → 530.14] And there's an entire algorithm that's designed around that, which we'll discuss in a moment.
[530.54 → 535.48] But it was just it was an impressive bit of engineering, both from a data science standpoint.
[535.48 → 543.44] But also, as I watched that video, I just kept thinking of all the applications and not even necessarily robotic hands.
[543.44 → 550.92] But if you start thinking of other manipulation tools that you might have on a robot and applying the same principles, I'm pretty excited about it.
[551.48 → 553.84] So congrats to the OpenAI team.
[553.90 → 558.78] If any of you are listening, I hope maybe one or two of you will come across this podcast.
[559.26 → 560.50] Congrats and great work.
[560.50 → 572.40] So maybe what we could do now, Chris, I think would be good for me and probably the listeners, too, is to just kind of break down how OpenAI went about this solution.
[572.62 → 583.46] What they used in terms of neural networks and setting up the solution and training and simulation and all of those things to just kind of break down the main parts of this study.
[583.54 → 584.14] Does that sound OK?
[584.28 → 585.30] That sounds like a good idea.
[585.30 → 593.56] So I went to the OpenAI blog post about this research, which we'll, of course, link in our show notes.
[594.30 → 603.84] And kind of the first sentence that they have there is we've trained a pair of neural networks to solve the Rubik's Cube with a human like robot hand.
[603.84 → 616.96] The neural networks are trained entirely in simulation using the same reinforcement learning code as OpenAI 5 paired with a new technique called automatic domain randomization.
[617.34 → 624.18] The system can handle situations it never saw during training, such as being prodded by a stuffed giraffe.
[624.68 → 631.58] That summarization there is just like packed full of all sorts of things that I would love to break down.
[631.58 → 636.76] Maybe not so much the stuffed giraffe, although I was intrigued by that as well.
[637.14 → 639.54] And later on down, they also have another good summarization.
[639.70 → 646.82] They say we train neural networks to solve the Rubik's Cube and simulation using reinforcement learning and Combat's algorithm.
[647.00 → 648.42] I'm probably butchering that name.
[648.52 → 648.72] I'm sorry.
[648.96 → 649.76] That's how I would have said it.
[649.92 → 651.58] And then they also talk about domain randomization.
[652.32 → 655.26] So some of these things I'm more familiar with than others.
[655.46 → 658.06] And there are some new things here as well.
[658.06 → 665.32] So maybe we can start by just digging into these pair of neural networks that they're talking about.
[665.52 → 672.28] Were you able to kind of deduce from their blog post or their paper anything about this pair of neural networks?
[672.62 → 674.24] What pair of neural networks are these?
[674.48 → 674.60] Yeah.
[674.76 → 681.48] For the computer vision side, they use three cameras to address the aspects of the Rubik's Cube.
[681.48 → 685.48] And then for the manipulation, they had a reinforcement learning policy.
[686.22 → 690.20] And so they had the control policy network that was addressing that.
[690.32 → 700.82] And so both of those networks had to be trained to be able to work together to be able to manipulate the Rubik's Cube and understand where they were statewise at any given moment.
[700.82 → 714.84] So the two networks, I guess, then would be this control policy network and then the convolutional neural network, which has to do with estimating the position of the cube in the hand.
[714.84 → 730.38] So the control policy network, in terms of input and output, what I was getting from the paper is basically the input of this control policy network would be the positioning, kind of noisy positioning of the Rubik's Cube and the robot hand.
[730.38 → 742.16] So they were actually, you know, either from the convolutional neural network or from sensors in the cube and the hand, they had these positioning of the cube and the robot hand.
[742.26 → 747.20] So you have these positioning, basically the state of how the cube is in the hand as input.
[747.38 → 753.04] And then the output would be what action does the robot hand need to take?
[753.04 → 759.24] In particular, that brings the state of those things closer to solving the cube.
[759.24 → 764.94] So in comes these what they're calling observations, outcomes, actions.
[765.20 → 771.36] Now, I guess for those observations, they need some way to estimate the positioning of the cube.
[771.44 → 774.64] And is that where the convolutional neural network comes in?
[774.64 → 783.54] Yeah, I think they were using the convolutional neural network for the three cameras that were observing from different positions, the various aspects of the Rubik's Cube.
[783.54 → 793.52] And then I do recall also that they mentioned that the robot's hand was also tied to 3D positioning capability that they had.
[793.58 → 803.12] So they'd understand where the robot was at any given moment in relation to how the cube was to combine those two so that it could do the policy based manipulation.
[803.12 → 819.04] Yeah, it was a combination of, you know, the detected position of the cube, the tracked position of the robot hand fingers or hand in general.
[819.04 → 827.24] And then they also were able to kind of track the faces of the cube by instrumenting the cube as well.
[827.32 → 830.04] So there's definitely a lot of instrumentation going on here.
[830.16 → 841.66] But essentially all of that is considered observations, which is passed into this control policy network to produce what action should the hand do.
[841.66 → 853.70] And my understanding is that these actions are essentially the sort of desired angles that they want to manipulate the cube into or the faces into.
[853.82 → 859.38] I'm not sure what the dimensionality of that is because there are a lot of these faces of the Rubik's Cube.
[859.94 → 864.30] So all the observations come in and the outcomes, the actions.
[864.30 → 869.74] You mentioned that like the control policy had to do with reinforcement learning.
[870.18 → 874.58] The convolutional neural network for the position detection was separate.
[874.92 → 885.28] As a reminder, kind of what's the difference in training the control policy via reinforcement learning versus the convolutional neural network in another way?
[886.04 → 892.24] So the convolutional neural network is when you're training it, you're trying to recognize certain patterns.
[892.24 → 901.86] And so obviously the patterns here are the various faces of the Rubik's Cube and the different coloured faces on each of those cubes and how they're working together.
[902.02 → 904.96] And so recognizing what that is at any given moment.
[905.08 → 909.20] So for cube state is what the CNN, the convolutional neural network would have been doing.
[909.58 → 917.36] Reinforcement learning, though, is the other side, the control policy side, where the network has to figure out with this articulated hand.
[917.36 → 922.08] And so it has many different joints and motors that are driving it at different angles.
[922.08 → 929.80] And they have to work in unison to be able to work with what is determined to be the state of the Rubik's Cube at any moment in time.
[929.80 → 931.82] So it's not just one motion.
[931.82 → 933.38] It's a whole collection of motions.
[933.38 → 940.10] And it does that through essentially trial and error that the algorithm puts it through to learn the process.
[940.10 → 943.42] And so you could think of the CNN as perception oriented.
[943.42 → 952.92] And you could think of the reinforcement learning as what do I do next with my articulated hand to achieve the next state that I'm trying to get to.
[953.06 → 954.28] So it takes them both.
[954.28 → 973.04] If I also recall, just to throw out one extra thing, they had a type of recurrent neural network called an LSTM, long short term memory, which takes into account time, the time sequence between the different observations and the policy based movements it's doing.
[973.04 → 981.06] You have to have a sequence for that to make any sense, because obviously a robotic hand that's trying to do a task has a series of moves it has to do.
[981.06 → 986.96] So it actually takes all three of those to work together to be able to apply itself to this problem.
[987.62 → 988.84] The reinforcement learning.
[989.14 → 995.46] We won't do a huge deep dive into that because we actually have a couple of other episodes on that already.
[995.46 → 1002.68] I would recommend first off taking a look at episode 14 from Wojtek Marimba actually at OpenAI.
[1002.90 → 1007.54] So he was on the team that helped do this research or did this research.
[1007.54 → 1016.52] And he goes a little bit more into reinforcement learning in that episode and kind of compares reinforcement learning to like semi supervision.
[1016.52 → 1029.78] So giving the network a sort of treat, like giving a dog a treat or a reward as it performs actions that get closer to a solution versus the convolutional neural network, which is just supervised.
[1029.78 → 1039.20] So you have input images that have a labelled position, and you're trying to predict that position in a sort of supervised manner.
[1039.36 → 1043.50] So we'll link our other episodes about reinforcement learning in the show notes.
[1043.76 → 1043.96] Correct.
[1044.22 → 1055.02] I guess to summarize that up, the algorithm has what's called an agent, which takes actions to act upon the environment it's in and is rewarded or not, depending on the outcome of that.
[1055.02 → 1060.36] And then adjustments are made based on what happened, and it goes around and around in that process.
[1071.88 → 1073.62] What is up, Practically I listeners?
[1073.84 → 1077.14] We're working with Infinite Red to promote their free AI mini course.
[1077.38 → 1078.82] It's called AI Demystified.
[1079.18 → 1082.38] Learn more and enrol at learn ai.infinite.red.
[1082.38 → 1090.66] This free five day mini course is a great introduction to the most important concepts, types and business applications for AI and machine learning.
[1091.00 → 1096.34] Each day of the course includes a lesson, a quiz and an assignment to submit your learning.
[1096.82 → 1103.02] And after you've completed the course, you'll also get a certificate of completion for your LinkedIn profile or for your portfolio.
[1103.02 → 1113.90] If you've been feeling lost in the world of AI and hearing lots of buzzwords, then by the end of this mini course, you'll be able to speak intelligently about AI and machine learning and their practical business applications.
[1114.54 → 1116.48] Again, this course is completely free.
[1116.86 → 1119.90] Learn more and enrol at learn ai.infinite.red.
[1120.10 → 1122.98] Again, learn ai.infinite.red.
[1122.98 → 1134.90] All right.
[1134.90 → 1143.60] So they show some great pictures of their experimental setup, like in the physical world and also in simulation.
[1143.60 → 1152.32] And particularly in that summarization that we talked about initially when we got into this, they talk about training in simulation.
[1152.94 → 1160.80] And I know that you've had some experience in the robotics world before and have run across different scenarios.
[1161.04 → 1164.08] Why is simulation important, particularly in robotics?
[1164.08 → 1175.18] Because probably the biggest reason, and it's really, really, really common in robotics to start in simulation to the point where it's probably that's the case in almost all cases.
[1175.50 → 1181.74] So in simulation, you can essentially create the circumstances that you're operating in.
[1181.84 → 1187.14] You're essentially able to simulate the data that applies to the situation, and you can have the environment created.
[1187.14 → 1204.74] And so if you don't have a bunch of the ability to apply real world data up front that may not have been created yet, and you don't have an environment that lends itself to testing, you know, just as a kind of obvious example, in my own job at Lockheed Martin, one of the things we build are airplanes.
[1204.74 → 1219.30] And so if you're trying to figure out how an airplane will fly around, and you haven't yet built the airplane, it's a real problem because, you know, you have to do it in a simulated world where you can try different things out and that lends itself to the engineering.
[1219.60 → 1225.78] And so if you kind of take that example, and you push it out in the world, you can apply that in a lot of different ways.
[1225.78 → 1229.96] So it's a much more inexpensive way to start your training out.
[1230.26 → 1236.60] And depending on your situation, you may be able to do almost all of your training and simulation, which it sounds like they did in this case.
[1237.14 → 1237.58] Yeah.
[1237.68 → 1251.82] And in your example, like the airplane example, like it's inexpensive, I guess, because you don't have to manufacture 2000 aircraft with different variations and then see, you know, which 10 of them don't crash.
[1251.82 → 1255.18] And then you utilize those as what you design off of, right?
[1255.18 → 1261.50] You're able to kind of go through a lot of different scenarios, a lot of different configurations and in a simulated sense.
[1261.62 → 1274.48] In the same way, I think OpenAI, like they don't need a thousand robot hands to be manipulating cubes and getting the data off of those to create a kind of vast training data set.
[1274.48 → 1285.18] What they do is, you know, they create the simulated world using, I think, a lot of technology from like gaming and image rendering and all of that.
[1285.26 → 1286.96] So like Unity 3D.
[1286.96 → 1316.94] So they create this virtual hand, virtual cube and position it in various ways to recreate as real of imagery and as real as position data as they can without actually having to position a real robot hand into those positions and gather the data off of the hand, which I imagine would take an enormous amount of time and effort.
[1317.26 → 1321.38] So, yeah, I mean, you were kind of getting at the engineering side of things.
[1321.88 → 1331.32] And even though they aren't engineering a bunch of different hands to collect this data, it seems like this simulation task in itself is actually a pretty big engineering burden.
[1331.32 → 1335.28] It is, but simulation has been around for a long time.
[1335.40 → 1336.80] And I know we talked about it.
[1336.88 → 1341.32] We had our episode where we discussed high performance computing, HPC.
[1342.14 → 1346.82] And we talked a bit about in that conversation about the simulation world and the requirements.
[1347.12 → 1348.48] And it's been around for decades.
[1348.78 → 1352.38] And so, you know, gaming, as you pointed out, also does that.
[1352.50 → 1354.50] There are a lot of industries that utilize it, automotive.
[1354.50 → 1366.44] And so trying to get the physics of what you're working on and all the environmental considerations and, you know, is at least something it is complex, but it's something that is somewhat known.
[1366.44 → 1380.10] And it's much less expensive to do it in that simulated world than to do what you just described, the kind of the ludicrous, you know, create a bunch of versions of the same thing and figure out which one works and which one doesn't, which would be prohibitively expensive.
[1380.10 → 1385.24] Right. And could be dangerous, depending on what you're trying to simulate, I guess.
[1385.24 → 1385.60] Absolutely.
[1385.82 → 1386.78] In the airplane case.
[1386.98 → 1393.52] But going back to the Rubik's Cube, I'm thinking back to my friend in my physics class who was brilliant.
[1393.66 → 1401.52] And I was in a mechanics class with him where we had to do these simulations of real life mechanics.
[1401.52 → 1413.00] So classical mechanics like pendulums and all this stuff and more complicated things that are fairly chaotic, like, you know, multi weight pendulums with bends in them and all of these things.
[1413.64 → 1416.24] And I remember that that was extremely challenging.
[1416.24 → 1422.16] And one of the things that they note in the paper is that it is challenging.
[1422.16 → 1437.84] So you have to, in some sense, use simulated data for these types of problems and robotics, but it is challenging to create simulated environments that capture all the physics of the real world.
[1437.84 → 1443.26] And this is where this sort of domain randomization stuff comes in.
[1443.26 → 1467.82] So they bring up this idea of domain randomization, which is actually a previously introduced idea where in a created environment for a simulation, you introduce some amount of randomness in the renderings of that simulator or some variability in the simulator based on randomness that you're basically trying to simulate.
[1467.84 → 1480.88] That there's going to be variations in the environment that there's going to be variations in the environment that it sees when you transfer the model that you're training from the simulated world into the real world, because that transfer can be rather difficult.
[1481.46 → 1483.72] But OpenAI took this a step further.
[1483.84 → 1484.60] That's my understanding.
[1485.28 → 1495.92] Yeah, they created this approach, which they called automatic domain randomization, where they systematically created that randomization as part of their training process.
[1495.92 → 1499.38] And, you know, it was done in simulation, as we've been discussing.
[1499.86 → 1512.60] And it was interesting in that it was a technique that could increase the ability for the control policy to be able to generalize to the environment that it's in.
[1512.60 → 1530.34] And if they had not done that, for instance, and the articulated hand, robotic hand had been manoeuvring the Rubik's Cube around and any kind of interference was introduced, you know, going back to your stuffed giraffe comment a little while ago, you know, that could completely throw it off.
[1530.34 → 1538.36] But if as part of the training process, you are constantly introducing different types of interference in all sorts of different ways.
[1538.68 → 1546.98] And as part of its reinforcement learning process for its control policy, it has to learn to cope with each of those forms of interference.
[1546.98 → 1551.90] Then it is better able to generalize once you've completed learning down the road.
[1552.06 → 1556.06] I was fascinated reading through their white paper on how they approach that.
[1556.20 → 1557.34] I think it's a great next step.
[1557.92 → 1558.00] Yeah.
[1558.12 → 1566.44] And one of the things I think that they were interested in is this idea of handling situations that weren't seen during training.
[1566.44 → 1588.34] So the idea is, OK, how do we extend domain randomization in a way that creates an even more robust model that will be able to adapt quickly and return to a sort of baseline performance, even when things happen that we don't anticipate.
[1588.34 → 1601.06] And so on of the key pieces of how they extended the domain randomization was that they didn't just randomize the simulation, they randomized it in increasingly difficult ways.
[1601.70 → 1614.64] So one of the things that they mentioned in their blog post is like they would increase the size or decrease the size of the simulated Rubik's Cube more and more or less and less as the training went on.
[1614.64 → 1631.64] So whenever the neural network achieved a certain level of performance, then they would throw something at it even harder, like they would change the size of the Rubik's Cube even more and kind of continually push it to have to adapt more and more to harder and harder things.
[1631.88 → 1644.42] And in this way, it kind of they created what they're kind of calling or what they're theorizing is something that leads to what they're calling emergent meta learning.
[1644.64 → 1653.76] So if you remember, we had this episode with Cheryl Chen from Google where we talked about AutoML and meta learning, which are kind of related.
[1653.94 → 1658.62] Maybe those were in we talked about them in a slightly different context with Cheryl.
[1658.88 → 1666.28] But here they're talking about emergent meta learning, which sounds like this really weird term to me.
[1667.28 → 1670.16] And it's almost like a term that doesn't mean anything.
[1670.16 → 1671.74] It's like emergent, and it's meta.
[1672.12 → 1673.88] Very new age sounding there.
[1673.88 → 1674.32] Yeah.
[1674.36 → 1675.56] What does that even mean?
[1675.60 → 1676.32] I'm not sure.
[1676.44 → 1679.28] So what do you get, if anything, from that?
[1679.68 → 1693.96] Well, I actually drew an analogy between what they were doing with that and kind of what we as humans do in the sense of as they kept cranking up the difficulty by changing the parameters into something more difficult.
[1693.96 → 1704.46] It reminded me as I read that about, for instance, teaching my daughter to ride a bike and, you know, first just learning how to sit on it and pedal with training wheels on and start steering it.
[1704.46 → 1713.30] And then she got comfortable with that and, you know, going over curbs and then taking the training wheels off and, you know, having to learn how to do balance and all that.
[1713.30 → 1716.60] Or even myself, I would like to learn how to juggle just for fun.
[1716.60 → 1720.00] And recently I picked up some balls and I started with just one.
[1720.00 → 1725.74] And as I started mastering that, I ramped up the difficulty into two, and I'm not to three yet.
[1725.96 → 1732.50] So, but I think their approach really reminded me of how humans learn along the way.
[1732.50 → 1743.04] And I thought that was striking since that doesn't always, as much as we like to draw analogy between different AI approaches and humans and brain and such, that doesn't always reflect the reality.
[1743.90 → 1745.28] It's fascinating.
[1745.48 → 1747.52] First off, a little piece of trivia.
[1747.76 → 1752.32] I was the unpopular kid in high school who was a juggling troop.
[1752.98 → 1756.58] Next time we're together, we'll have to experiment with that.
[1756.58 → 1771.22] But I do like the analogy that that gives because in juggling or some activity like that, that a human learns each time you add, like, let's say you add an element that you're juggling, like a new ring or ball or club or whatever it is.
[1771.22 → 1778.90] It doesn't necessarily take you an exponentially longer time to adapt to that new situation.
[1779.16 → 1784.18] But you've kind of learned how to, you've learned how to learn a new juggling trick.
[1784.18 → 1788.40] And so you kind of just kind of bolt it on to your juggling toolkit.
[1788.40 → 1790.90] It doesn't always carry through like that.
[1791.02 → 1796.98] But here with meta learning, you know, meta learning itself just means kind of learning to learn.
[1797.18 → 1797.78] Right.
[1797.82 → 1808.68] And so what they're saying is that by introducing this element of increasingly difficult domain randomization into the training,
[1808.68 → 1821.96] then what's emerging from that process is a network that is able to learn as new perturbations come in like the stuffed giraffe or whatever it is.
[1821.96 → 1824.62] So I like your illustration very much.
[1825.08 → 1833.30] The last thing that they mentioned, we can just mention really quickly in their paper that maybe needs some definition is this Coimbra algorithm.
[1833.30 → 1845.30] As you mentioned, the solving of the Rubik's Cube, in other words, how do I need to move the faces of the cube to move towards a solution of the cube?
[1845.64 → 1853.40] That was actually not a neural network that was deciding those operations.
[1853.40 → 1861.56] So like the raw operations, like move this block to this position, move this face, rotate it one direction.
[1861.56 → 1864.92] That that was not a neural net that was deciding that, right?
[1865.32 → 1865.52] Correct.
[1865.72 → 1867.44] Yeah, that was they're using an algorithm.
[1867.44 → 1879.98] And this is one of several that I believe exist that where you follow a known sequence of moves and rotations, and it will eventually get you where you're trying to get to.
[1879.98 → 1895.86] So kind of going back to what we said in the very beginning, they were really focused on understanding the state that they were in and articulating the robotic hand to achieve the next state, which this algorithm, which was an already known thing based on this algorithm.
[1895.86 → 1919.10] Well, talking about the fact that they use the AI models to manipulate the robot hand, but not actually, quote unquote, solve the Rubik's Cube, that and a few other things created a bit of pushback in terms of the community's reception to that and various people saying strong things.
[1919.10 → 1931.34] I saw a couple of tweets in this regard about, you know, how like this algorithm that they're using to solve the Rubik's Cube, it's been around for 17 years and it's symbolic.
[1931.64 → 1932.98] It's not like a neural network.
[1933.20 → 1935.78] So they were missing the point in my view.
[1935.94 → 1936.24] Yeah.
[1936.40 → 1946.42] And they also talked about, oh, well, like the Rubik's Cube is all instrumented with LEDs and sensors and all of these things.
[1946.42 → 1961.24] It's not just like I threw, for example, I couldn't go into the store and buy a Rubik's Cube and put it in the hand of this robot and then have it do the manipulation because their cube was a special cube or these sorts of things.
[1961.24 → 1965.58] So this was kind of the pushback was that in their blog posts.
[1965.72 → 1972.88] So if I go back to the blog post here, their kind of headline is solving Rubik's Cube with a robotic hand.
[1973.04 → 1977.20] And they say trained a pair of neural networks to solve the Rubik's Cube.
[1977.40 → 1982.30] So the pushback was like, well, did they really do that?
[1982.30 → 1989.12] So in my view, OpenAI's mistake here was no in what they actually did.
[1989.22 → 1992.54] It was in the marketing of the blog post and how they titled it.
[1992.90 → 1995.82] I think what they did was awesome and a lot more important.
[1995.94 → 2000.36] If you used a neural network to solve a Rubik's Cube, that might be a cool little project to do.
[2000.58 → 2002.72] But it's very, very specific.
[2002.72 → 2009.30] And it's not maybe I'm wrong, but I don't see the applicability off the top of my head to generalize on that.
[2009.30 → 2018.88] And so what they were focusing on was how do you create the control policy for that articulated hand and learning how to do that better?
[2019.04 → 2027.24] Because in my view, that is much, much more valuable because you can use that all in so many different use cases out there.
[2027.24 → 2035.58] And if OpenAI's purpose is to kind of help the rest of us get to the next level, I think that they did exactly the right thing.
[2035.66 → 2037.14] I think they focused on the right thing.
[2037.14 → 2040.44] So they should have worded the blog post better, probably.
[2040.72 → 2044.36] But other than that, I personally am very happy to see them do this work.
[2044.94 → 2055.38] And I think that even the strongest critics, at least in looking through Twitter, the Twitter verse and internet on various things that I found,
[2055.38 → 2066.44] even the strongest critics, I don't think characterized what they did as not impressive, but maybe that it was mischaracterized, as you're saying.
[2066.44 → 2068.50] So, yeah, I think that there is.
[2068.64 → 2072.48] And that kind of got me going down a train of thought.
[2072.98 → 2079.84] You know, why did people react in such a way, like this sort of way to this article with such vigour?
[2080.18 → 2088.14] I started thinking like, you know, back a few years ago or whenever it would be, would people have reacted the same way?
[2088.20 → 2093.58] And why are people so sensitive to AI hype?
[2093.64 → 2095.62] Do you have any thoughts on that?
[2095.62 → 2100.14] Well, I think we're all subjected to quite a lot of AI hype.
[2100.32 → 2109.24] And I know we've discussed that on numerous episodes in the past, which is one of the reasons, as an aside, that you and I decided to make this practical AI,
[2109.76 → 2114.34] practical, productive, and accessible to everyone, because we were, to some extent, even at the very start,
[2114.60 → 2122.04] recognizing the overwhelming amount of hype that was then and continues to this day and probably will for a long time to come.
[2122.04 → 2129.38] So, I get that people, that the message needs to be more specific to the actual amazing work that was done.
[2129.88 → 2138.58] And so, you know, they need to be careful how they're putting their work out there in terms of what the actual impressive thing is that we should focus on.
[2138.58 → 2145.06] But I get that people feel a little bit burned by the hype, but also, you know, sometimes recognize we're all human, we all make mistakes.
[2145.70 → 2148.32] And, you know, focus on where the good is on this.
[2148.40 → 2151.78] I would ask people to take a glass half full approach.
[2152.20 → 2152.56] Yeah.
[2152.82 → 2155.22] And, you know, let's look at this and go, wow.
[2155.22 → 2161.44] And now this is something that we can all use going forward and not focus on whether somebody could have done a better job on a title.
[2162.02 → 2162.12] Yeah.
[2162.24 → 2165.00] It is kind of the situation where we're in.
[2165.14 → 2173.96] I guess, you know, this probably relates to some of the discussion around, like, cancel culture and all of that stuff.
[2173.96 → 2178.86] And I don't really want to get into the politics and views on that in this episode.
[2179.00 → 2191.36] But we, I think, have been burned quite a bit by people just, you know, saying all this stuff about AI or blockchain or quantum this or whatever when it hasn't really proved true.
[2192.08 → 2196.36] And I think we do need to be careful about this in particular as related to certain things.
[2196.60 → 2199.70] There's a lot of talk about bias now in AI.
[2199.70 → 2209.46] And I think that's probably a point that, you know, is not being hyped enough that we're not concerned about that enough.
[2209.54 → 2211.08] At least that's my personal opinion.
[2211.26 → 2221.32] I saw some tweets saying that Eric Schmidt of Google, the chairman, was saying some things about, oh, we don't need to yell that much about bias now in AI.
[2221.58 → 2225.80] And I think, you know, we need to be practical in how we approach these things.
[2225.80 → 2231.98] But there's a lot to sift throughout there when you start looking up terms like AI and quantum and other things.
[2232.50 → 2239.64] Even, you know, just this last week, I don't know if you were following, Google made the announcement about, you know, finally achieving quantum supremacy.
[2240.06 → 2240.28] Oh, yeah.
[2240.28 → 2241.14] That made me cringe.
[2241.28 → 2241.44] Yeah.
[2241.62 → 2241.84] Yeah.
[2242.16 → 2247.98] They said this thing would have taken, you know, a classical computer 10,000 years to solve.
[2248.10 → 2253.46] And then IBM kind of worked on it a bit and solved it in two and a half days with a classical computer.
[2253.46 → 2255.80] So in some sense, I don't know.
[2256.00 → 2266.96] This is part of the scientific process in the sense that, like, if you claim something, people should be able to, you know, test it and see if you're really what you're claiming is true or false.
[2267.08 → 2271.82] It's maybe the difference now is that that testing is like it's so much more public now.
[2271.92 → 2275.88] Used to that would happen in like private peer review and all of that.
[2276.04 → 2279.82] Now it's kind of happening on Twitter and all over the Internet.
[2279.82 → 2285.14] So I'm not sure if I'm still kind of parsing through whether parts of that are all good or bad.
[2285.36 → 2293.06] And I think the fundamental issue there is with the acceleration process that you just described and the fact that you don't have something.
[2293.06 → 2301.12] You don't produce a result that gets peer reviewed over a period of weeks or months and then kind of eventually goes out to the larger world at this point.
[2301.12 → 2318.40] You know, AI and these other fields that we're talking about are happening so fast that you kind of have to get your stuff out there as an organization before somebody is likely to, you know, steal your thunder and maybe reveal their results that were very similar to yours before you get there.
[2318.40 → 2325.66] And so especially with so much of this work being done by industry, I think what I'm about to say holds true even for academia.
[2326.04 → 2331.94] There's a marketing desire to say, hey, look at this great work we did because people are looking for customers.
[2332.04 → 2333.30] People are looking for funding.
[2333.30 → 2340.00] And so there is definitely a marketing consideration in doing this advanced scientific work.
[2340.12 → 2350.02] But the marketing and the science, you need to find the best balance you can and not let your marketing overreach your science, or you're going to get a lot of backlash on that.
[2350.02 → 2363.12] So I think it's tough to be in an organization these days when you're trying to do amazing work and have it validated, but also get the benefit of that work in other domains such as continued funding and continued customers.
[2364.22 → 2364.32] Yeah.
[2364.32 → 2379.20] So I guess one of the best responses to some of the criticism that I saw in the open AI stuff was like, hey, look, you know, we shouldn't be solving Rubik's cubes with neural networks because we don't have to.
[2379.62 → 2382.58] And we've had the solution for a long time and it works fine.
[2382.58 → 2394.30] But we don't have the solution to this sort of robotic manipulation, which is actually maybe easier for humans, but really hard for computers and AI systems.
[2394.52 → 2399.10] And so what they tackled was the harder of the problems.
[2399.10 → 2412.16] And there's certainly other cases of this that, you know, are present in AI, like, you know, detecting and working with sarcasm in text is extremely difficult, like, or even just sentiment.
[2412.58 → 2429.14] It's still a hard problem just because it's easy for humans to maybe detect that and like even like combine text with facial or voice with facial expressions and all of that to detect sarcasm or volume or tone or all of those things.
[2429.32 → 2432.50] And that's really, really tough for a computer to solve.
[2433.04 → 2442.48] If you think about not having facial expression, you know, the way we type our emails or texts, for instance, we humans also have a hard time detecting sarcasm when it's there.
[2442.58 → 2446.62] And it's not if we don't have other sources other than the text alone.
[2447.12 → 2466.44] Yeah, which is why I think a lot of people in that space are talking about this sort of multimodal learning where you have maybe text and video or imagery and that sort of thing, too, where these people solving those types of problems, maybe sentiment analysis is something where we're like, oh, well, humans can do that easily.
[2466.44 → 2470.36] Why do we need to work on computer algorithms to solve this sort of thing?
[2470.36 → 2485.80] It's part of this effort to really tackle the hard problems that are hard for computers and advance AI more generally versus just kind of solving already solved things just quicker or faster, that sort of train.
[2485.80 → 2490.90] If you have an option that is less expensive to do it, then take that option.
[2491.02 → 2492.10] Don't take the AI route.
[2492.34 → 2495.92] It's, you know, apply AI where it makes sense to apply AI.
[2496.38 → 2496.98] Amen.
[2497.48 → 2498.12] All right.
[2498.18 → 2504.76] Well, on this front, we always like to end these fully connected episodes with some learning resources.
[2504.76 → 2515.74] And in particular, if you're wanting to learn more about reinforcement learning, that was a confusing statement, very meta learning, learning about reinforcement learning.
[2515.94 → 2521.52] Again, episodes 40 and 14 of this podcast, you might want to take a listen to.
[2521.72 → 2528.56] But OpenAI use this OpenAI gem to train their reinforcement learning algorithm.
[2528.56 → 2532.00] And that is something that you can get your hands on.
[2532.00 → 2537.90] There's a tutorial that we'll link in our show notes that kind of shows how to use this OpenAI gem.
[2538.02 → 2542.76] So if that's something you're interested in exploring, then we'll certainly link it in the notes.
[2543.36 → 2549.26] And there's PyTorch and TensorFlow tutorials as well that deal with reinforcement learning.
[2549.74 → 2557.22] So there are a bunch of ways that you can get hands on with this sort of thing, even if you don't have a robotic hand handy.
[2557.66 → 2558.60] There's my pun.
[2558.92 → 2559.76] Your hand handy?
[2560.00 → 2560.80] Yeah, and I don't.
[2560.80 → 2562.70] I don't either.
[2563.18 → 2563.50] Cool.
[2563.70 → 2566.76] Well, thanks for going through this discussion with me, Chris.
[2566.82 → 2567.64] It was a lot of fun.
[2567.78 → 2568.12] It was.
[2568.20 → 2568.92] Interesting article.
[2569.40 → 2577.50] Very interesting in all sorts of different ways, technically, culturally, and reception-wise, and all of those things.
[2577.70 → 2583.16] So yeah, definitely go take a look at the blog post and the paper if you haven't yet.
[2583.16 → 2585.18] And let us know what you think.
[2585.18 → 2595.02] You can reach out to us in our Slack channel, which you can find if you go to changelog.com slash community, or reach out to us on our LinkedIn page.
[2595.42 → 2605.56] We're happy to get good feedback, whether that's positive or negative things, but also to hear what your thoughts are on potentially controversial and interesting topics like this.
[2605.56 → 2606.60] So reach out.
[2607.10 → 2609.72] And yeah, I think that's all we've got for today.
[2609.90 → 2610.96] It's great to talk to you, Chris.
[2611.08 → 2611.66] It was a good one.
[2611.76 → 2612.56] Talk to you soon, Daniel.
[2612.56 → 2615.68] All right.
[2615.74 → 2618.34] Thank you for tuning into this episode of Practical AI.
[2618.60 → 2620.06] If you enjoyed this show, do us a favour.
[2620.18 → 2620.78] Go on iTunes.
[2620.90 → 2621.56] Give us a rating.
[2621.84 → 2623.70] Go in your podcast app and favourite it.
[2623.78 → 2626.52] If you are on Twitter or a social network, share a link with a friend.
[2626.60 → 2628.98] Whatever you got to do, share the show with a friend if you enjoyed it.
[2629.24 → 2631.94] And bandwidth for changelog is provided by Vastly.
[2632.04 → 2633.48] Learn more at fastly.com.
[2633.48 → 2636.88] And we catch our errors before our users do here at changelog because of Rollbar.
[2637.08 → 2639.50] Check them out at rollbar.com slash changelog.
[2639.62 → 2642.12] And we're hosted on Linde cloud servers.
[2642.56 → 2644.26] Head to leno.com slash changelog.
[2644.36 → 2644.82] Check them out.
[2644.90 → 2645.72] Support this show.
[2646.14 → 2649.30] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2649.76 → 2651.82] The music is by Break master Cylinder.
[2652.16 → 2655.66] And you can find more shows just like this at changelog.com.
[2655.74 → 2657.78] When you go there, pop in your email address.
[2658.08 → 2662.00] Get our weekly email keeping you up to date with the news and podcasts for developers
[2662.00 → 2664.10] in your inbox every single week.
[2664.48 → 2665.28] Thanks for tuning in.
[2665.42 → 2666.16] We'll see you next week.
[2672.56 → 2683.32] Thank you.
[2683.40 → 2684.30] Novena people.
[2684.30 → 2685.08] The music is by Meeting.
[2685.14 → 2685.68] All right.
[2685.74 → 2686.44] We'll see you next week.
[2686.44 → 2696.78] Good evening.
