[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 --> 24.36]  on Linode servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[24.36 --> 29.28]  podcast about making artificial intelligence practical, productive, and accessible to everyone.
[29.28 --> 34.86]  This is where conversations around AI, machine learning, and data science happen. Join the
[34.86 --> 38.92]  community and snag with us around various topics of the show at Changelog.com slash community.
[39.44 --> 43.00]  Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[47.32 --> 52.42]  So Wojcik, thanks for joining us in Practical AI. I know you've got a busy schedule today at
[52.42 --> 58.48]  O'Reilly AI. So thanks for taking time. Thank you for the invite. Yeah. And you probably don't need
[58.48 --> 63.48]  much introduction. But for those that don't know, Wojcik is one of the co-founders of OpenAI.
[64.02 --> 69.24]  And he's going to be talking today at O'Reilly AI about robotics and deep learning. Is that right?
[69.62 --> 74.26]  That's correct. Yeah. Awesome. It'd be great if you could give the audience just a little bit of an
[74.26 --> 80.78]  idea of your background and what you're working on now. Cool. So I mean, I spent some time at Google
[80.78 --> 86.84]  Brain. I spent some time at Facebook. I researched, have finished PhD in the topic of deep learning.
[87.36 --> 93.72]  Even I spent many years ago some time at NVIDIA before actually deep learning was the thing.
[95.08 --> 99.72]  So it's kind of somewhat coincidental that all these things turn out to be extremely relevant.
[100.18 --> 106.46]  As you have said, Daniel, I'm one of the co-founders of OpenAI. And goal of OpenAI,
[106.46 --> 114.08]  it's quite ambitious is to figure out the way to build general's artificial intelligence or to be
[114.08 --> 122.22]  more exact, like how to build it in the way that say it's safe. In a sense, we can control it or let's
[122.22 --> 127.22]  say figure out, let's say from political perspective, how to deploy it in the way that it is beneficial
[127.22 --> 136.12]  to humanities as a whole. Our approach is more or less as follows. We see
[136.12 --> 143.28]  various limitations of current systems. And we think what's the best way to, what are the
[143.28 --> 149.62]  goals that we should attempt such that if we solve them, it becomes clear that we lift
[149.62 --> 156.86]  these limitations. And particularly, so, I mean, there are, let's say, somewhat several kind of
[156.86 --> 163.66]  internal approaches, how we go about the problems. But in case of what I'm doing, the motivation is as
[163.66 --> 170.48]  follows. So we know as of today that you can take extremely complicated computer games and
[170.82 --> 176.66]  machine can become superhuman in it. But the main criticism is, yeah, but that's just a game.
[177.16 --> 183.74]  It is kind of, let's say, unrelated to reality, confined into, let's say, the realm of the computer.
[184.32 --> 190.82]  And kind of sounds straightforward that we should be able to pull it off and apply it into real world.
[190.82 --> 197.30]  But it turns out that many people tried and haven't succeeded for a while when it comes to very,
[197.78 --> 203.88]  let's say, more complicated robots and so on. Yeah, I mean, I will let you ask me more questions and
[203.88 --> 204.86]  then I can tell you more.
[205.08 --> 209.28]  Sounds great. Yeah, I appreciate that. I was wondering before going forward, if you could just
[209.28 --> 216.04]  maybe, I know you mentioned, you know, open AI kind of going after general AI or general intelligence.
[216.04 --> 220.48]  I was wondering if you could kind of break that down for the listeners in terms of how
[220.48 --> 226.18]  that might be different from the research or the methods that other people are going after.
[227.00 --> 234.22]  So it's clear to me that AI, AGI consists of more or less three components.
[234.94 --> 241.02]  So, I mean, you have to be able to inject gigantic amount of compute, most likely.
[241.02 --> 250.36]  You need to invent some new algorithms and AI needs some kind of a data or environment in which it lives.
[251.56 --> 259.12]  So there are three main components that you have to, let's say, attack if you want just the capabilities of AGI.
[259.92 --> 268.72]  So I think that open AI is extremely well suited to pursue this goal because of a few reasons.
[268.72 --> 272.34]  One, we are not bounded by a product.
[273.00 --> 288.84]  And so often when we are building a product, actually quite a huge fraction of the work has to do with figuring out the niche or let's say target, marketing, let's say packaging and so on.
[288.84 --> 300.42]  And it's clear that there are various problems that you can attempt that have very small economical value, but it's actually very clear that they are making actual progress.
[300.72 --> 306.14]  I mean, if you would, for instance, be able to train the system that can solve Riemann hypothesis.
[307.12 --> 311.62]  And could you just give a quick explanation of what that is?
[311.62 --> 312.56]  Okay, yeah.
[312.64 --> 317.68]  So let's say, I just mentioned Riemann hypothesis is like an unresolved mathematical problem.
[318.36 --> 328.46]  So if system would be able to, you know, have such an incredible reasoning, that would indicate that you lifted one more restriction.
[328.46 --> 331.66]  Maybe, you know, the restriction that the neural networks do not reason much.
[332.40 --> 335.56]  It has not that much of an economical value.
[336.14 --> 339.18]  I mean, maybe people doing math would get upset.
[339.18 --> 341.56]  You would employ another group of people.
[342.36 --> 345.70]  But in a sense, that's not the product out of which you are making tons of money.
[346.16 --> 347.04]  So I'm just saying that.
[347.36 --> 352.52]  So I just compared, let's say, our approach to the building conventional product.
[352.80 --> 356.50]  I can also compare it to, let's say, academic labs.
[357.02 --> 367.94]  So in a sense, most of the academic labs, they are, they construed of the, it's like an endeavor of small number of individuals.
[367.94 --> 378.36]  And I would say, among these three components that I mentioned, let's say, compute algorithms and environment data, it actually focuses mostly on the algorithm, which is completely fine.
[378.40 --> 379.44]  That's one of the components.
[379.82 --> 383.44]  That's the one that they are well suited to actually pursue.
[383.44 --> 389.64]  But it seems to me that you have to be able to pursue actually all three components to make a progress.
[389.84 --> 406.94]  You need to be able to, you know, to focus the entire data center 10 miles by 10 miles that, you know, consumes millions of watts with some number of algorithms and, let's say, environments to actually achieve it.
[406.94 --> 411.72]  So in a sense, you need resources beyond actually, let's say, researchers.
[411.72 --> 418.00]  You need also all sorts of the talented engineers, infrastructure engineers, and so on and so forth.
[418.52 --> 420.70]  So I guess that's the main difference.
[421.24 --> 422.70]  Yeah, that helps a lot.
[422.70 --> 434.60]  And you kind of alluded to the fact that, you know, in your background, you had experience with these different technologies that kind of coincidentally converged in this new hype around AI.
[434.88 --> 437.08]  And you co-founded OpenAI.
[437.08 --> 459.90]  And I want to get into the content of your talk a little bit later, but I'm wondering if you could just comment on what you see as some of the advantages and disadvantages of kind of founding a company that is really at the center of this hype around AI and what your thoughts on that are and how you see the field moving forward in the midst of all this hype.
[459.90 --> 463.98]  I think, you know, NIPS, the NIPS conference sold out in like 15 minutes.
[464.14 --> 467.84]  It's like faster than a Taylor Swift conference or something.
[468.24 --> 473.14]  People are comparing the sales of tickets for NIPS to sales of tickets to Burning Man.
[473.44 --> 474.12]  Yeah, exactly.
[474.42 --> 474.58]  Yeah.
[474.74 --> 478.68]  So and OpenAI is really at the kind of center of that hype.
[478.76 --> 485.64]  Have you seen that kind of advantages and disadvantages to that or in terms of the progress that you're going after?
[485.64 --> 491.96]  So, I mean, this is extremely important to, let's say, not overpromise, deliver and so on.
[492.30 --> 496.64]  I mean, otherwise, over some period of time, it's going to bite you in the ass.
[496.98 --> 497.88]  Simple as that.
[498.28 --> 506.54]  The fact of being well-recognized organization definitely helps to hire incredibly brilliant people.
[506.54 --> 518.46]  I would say I'm feeling pretty much like I'm feeling extremely honored that say people around, they are on, you know, various axes, pretty much everybody.
[518.96 --> 520.64]  It's on some axis better than me.
[521.02 --> 523.98]  I'm feeling honored that these folks want to work with me.
[524.24 --> 524.76]  Awesome.
[525.12 --> 527.06]  Well, yeah, thank you for that.
[527.14 --> 530.92]  And I definitely respect a lot of a lot of the things you're doing.
[531.18 --> 534.32]  And so looking forward to seeing seeing what happens from here.
[534.32 --> 536.36]  But now I want to kind of talk a little bit.
[536.50 --> 540.98]  You're going to be talking about deep reinforcement learning for robotics at OpenAI.
[541.30 --> 543.94]  Give us just a brief sketch of what you'll be talking about.
[544.24 --> 544.48]  Cool.
[544.82 --> 553.76]  So as I mentioned at first, it's actually the case that, you know, reinforcement learning, it's a quite generic, incredible paradigm.
[553.76 --> 566.04]  It's effectively saying that you can take any quantity that you can measure and you can, if you can even remotely influence this quantity, you can learn how to, let's say, maximize it.
[566.52 --> 569.78]  And the quantity can measure, you know, success on the task or so.
[569.78 --> 576.64]  So this paradigm was used to use in various computer games, was used to beat humans in Go.
[576.84 --> 583.18]  It was used to in the game of Dota to get to the professional level.
[583.68 --> 586.80]  The paradigm has several shortcomings.
[586.80 --> 591.92]  So in a sense, as of today, it requires insane amount of data.
[592.60 --> 600.16]  So the rates are of tens of thousands of years of experience, virtual experience.
[600.32 --> 608.26]  So let's say in case of Go or in case of Dota, agent is playing for so long for millennia.
[608.26 --> 613.80]  Yes, that's the requirement if you really want to get top raw or superhuman performance.
[613.80 --> 620.84]  In case of robotics, it seems to be very hard to apply the same paradigm to the physical robots.
[621.36 --> 628.80]  I mean, it is possible you can try also to, you know, go through the path of decreasing number of interactions.
[628.80 --> 640.54]  So I would say that's one of the meaningful directions to just minimize the, try to improve algorithms to minimize number of interactions.
[641.12 --> 650.18]  And one of the approaches was, let's say, done at Google to, let's say, build form of arms to pick an object.
[650.60 --> 653.52]  But still, there are a few fundamental issues.
[653.52 --> 661.36]  So as long as once you are moving to the real world, it's actually not that easy to even get diversity of data.
[661.72 --> 664.62]  I mean, you cannot take your arm and go to a waterfall.
[665.12 --> 673.66]  Other part of the assumption is that you have to be able to reset and tapping from scratch.
[674.10 --> 677.38]  And it's also, say, once you are moving some objects, it can fall over.
[677.48 --> 681.60]  And then you have to build some contraption mechanism to bring it back.
[681.60 --> 694.46]  So I started myself to think that maybe the paradigm of reinforcement learning, instead of being close to actually what is happening when the human is learning,
[694.76 --> 699.34]  is actually closer to what is happening during evolution-like learning.
[699.54 --> 701.60]  That you have a really gigantic population.
[702.20 --> 705.18]  It has a huge number of the interactions.
[705.18 --> 711.68]  Rather than like a human kind of thinking through what truly happened and what should be the outcomes.
[712.44 --> 725.16]  So then it is also kind of natural to me that in case of evolution-like learning, you have, or let's say, in case of human learning, there are essentially two stages.
[725.32 --> 729.78]  There is a stage that takes this gigantic, gigantic amount of data, which is evolution.
[729.78 --> 734.16]  It actually, it is, evolution is reinforcement learning.
[734.30 --> 736.44]  It's like, you're going to survive or die.
[737.02 --> 743.04]  And this stage is powerful enough to create our brains that can then rapidly learn.
[743.48 --> 757.58]  So I was thinking, you know, it's actually not such a bad thing if we can learn in simulation to slightly add to, okay, almost majority of the task.
[757.58 --> 761.74]  And then in reality, there is quite rapid adaptation.
[762.22 --> 763.40]  So that's what we did.
[763.62 --> 771.04]  The interesting thing is when we, so the task is, we took robotics hand and we are reorienting objects.
[771.34 --> 774.38]  And let's say, speak in a second about the difficulty of this task.
[774.82 --> 780.50]  But solving the task itself takes something maybe like three years of virtual experience.
[780.50 --> 787.72]  But then to get to the capabilities that allow you for the transfer, that takes another 97 years.
[787.88 --> 788.24]  Oh, wow.
[788.38 --> 788.52]  Yeah.
[788.64 --> 798.04]  So the generalization to create a model that creates this kind of, or response to adaptations takes the longest amount of time.
[798.26 --> 798.52]  Correct.
[798.66 --> 798.80]  Yeah.
[798.96 --> 799.44]  Awesome.
[799.44 --> 801.98]  And just to kind of clarify a few things.
[802.12 --> 811.86]  So like when you're doing this virtual simulation, we've talked already on the podcast about where deep learning fits into the spectrum of AI techniques.
[811.86 --> 822.12]  And we've talked about even like masks, our CNN for in robotics context, but we haven't really dove into reinforcement learning yet.
[822.20 --> 830.68]  So I was wondering if you could just kind of give us a brief introduction to when you're doing the virtual learning and these kind of two stages.
[830.78 --> 836.64]  So you mentioned the first stage where it's kind of learning a task and then the second stage where you're attempting to make it more adaptive.
[837.16 --> 839.96]  What is the process that you're actually doing there?
[839.96 --> 843.82]  So let me first describe what reinforcement learning is.
[844.04 --> 844.44]  That'd be great.
[844.62 --> 852.80]  So reinforcement learning is a framework of teaching an agent to maximize amount of reward.
[853.36 --> 857.16]  You can think about it a little bit like training a dog with a treats.
[858.04 --> 865.36]  So when the dog is doing good stuff, you're giving the dog treats and then it does more of the stuff that you want.
[865.36 --> 872.10]  And that's the way more or less how you train the computer to become best in all these games.
[872.26 --> 876.12]  So it's completely up to you when you define that you're going to give a treat.
[876.70 --> 877.18]  Yeah.
[877.26 --> 879.64]  So there's a feedback that happens.
[880.44 --> 881.04]  Correct.
[881.04 --> 889.28]  So agent itself effectively some network that consumes observations.
[889.48 --> 892.58]  You can think as of an analogy to a human.
[892.80 --> 898.14]  It's like input to eyes, ears, nose, touch and so on.
[898.14 --> 902.58]  And the network is supposed to produce actions.
[903.00 --> 905.62]  So in our case, it would be electric signal.
[906.14 --> 910.06]  The nerves to decide how to move, let's say, limbs or so.
[910.50 --> 913.90]  And the network itself attempts to maximize reward.
[914.30 --> 919.88]  The system has a chance only to be successful if from time to time it gets a reward.
[919.88 --> 924.44]  So that's a kind of, let's say, let me a little bit downplay reinforcement learning.
[924.62 --> 930.76]  So the situations that wouldn't work is if you give a treat to a dog after it lands on Mars.
[931.18 --> 931.30]  Okay.
[931.54 --> 933.16]  It's like, it will just never happen.
[933.26 --> 939.14]  It has to, from time to time, it starts with, it starts at first with very random strategy.
[939.40 --> 943.54]  And then gradually it attempts to get more and more of the treats.
[943.74 --> 947.62]  So that's pretty much the paradigm of reinforcement learning.
[947.62 --> 953.80]  And that's what you would be doing kind of in that first stage where you're teaching a specific task.
[953.98 --> 954.46]  Is that right?
[954.64 --> 954.92]  Correct.
[955.18 --> 957.70]  So let me briefly describe the task.
[958.16 --> 961.82]  So we haven't knew much about the robotics of a year ago.
[962.52 --> 964.02]  We went to a robotics conference.
[964.18 --> 969.64]  We asked people what are the things that are impossible or very hard to do in the classical robotics.
[970.42 --> 974.28]  And people are saying anytime when you have a large number of degrees of freedom,
[974.36 --> 977.38]  it's very hard to control when there is a lot of interactions,
[977.38 --> 981.46]  when you touch many things simultaneously, in many places simultaneously.
[981.82 --> 983.46]  That's also very hard to model.
[984.56 --> 990.82]  And there is, when, it is way easier when you are in the open space and you are not touching anything.
[991.22 --> 991.46]  Okay.
[992.14 --> 997.10]  Or if the problem somehow can be simplified to one or two dimensional problems,
[997.22 --> 999.46]  then there are some, let's say, closed form solutions.
[999.46 --> 1007.20]  But in case of robotics hand, robotics hand has, let's say, the one that we bought has 24 degrees of freedom.
[1007.56 --> 1011.00]  We also kind of knew that the task is solvable because human can solve it.
[1011.28 --> 1014.96]  So we wanted to have a hope for the success.
[1014.96 --> 1015.96]  Yeah.
[1015.96 --> 1018.26]  And task is, you take an object.
[1018.44 --> 1023.44]  In our case, we demonstrated it on two different objects, which is, one is a block.
[1023.74 --> 1026.28]  One is some octagonal prism.
[1026.58 --> 1030.76]  And task is move it around to the new desired position.
[1031.12 --> 1032.32]  Like in a robotic hand.
[1032.52 --> 1033.54]  In the robotic hand.
[1033.54 --> 1043.58]  So, as I said, we were able to train it actually a while ago already in the simulation to achieve it.
[1043.82 --> 1046.96]  But then during deployment, it didn't work at all.
[1047.18 --> 1049.16]  Like literally, it's not at all.
[1049.24 --> 1054.54]  Despite easily being able to solve it in the simulation.
[1055.08 --> 1059.18]  Typical response of, or let's say, the typical approach is,
[1059.18 --> 1063.50]  let's just get the simulation closer and closer and closer and closer to reality.
[1063.84 --> 1065.24]  And I would say that helps.
[1065.38 --> 1070.80]  But the problem is that with sufficiently complicated systems like the hand,
[1071.16 --> 1073.90]  it is actually impossible to model everything.
[1074.22 --> 1077.06]  So, in a sense, hand has tendons, tendons stretch.
[1077.68 --> 1079.78]  It has a rubber, rubber deforms.
[1080.10 --> 1085.26]  Also, the shape that you have in the simulation actually doesn't even correspond exactly to the real shape.
[1085.40 --> 1087.60]  And when there is a lot of interactions,
[1088.20 --> 1091.76]  the difference in the given place you are touching versus not touching
[1091.76 --> 1095.84]  might cause the object to pivot, let's say, slip over and so on.
[1096.30 --> 1099.68]  So, that's why things do not want to transfer.
[1099.68 --> 1100.08]  Yeah.
[1100.24 --> 1105.68]  So, it's like a lot of very small kind of differences in how things are touched or moved
[1105.68 --> 1107.80]  can create a whole different outcome.
[1108.24 --> 1108.80]  Correct.
[1108.80 --> 1108.96]  Correct.
[1108.96 --> 1116.22]  In a sense, the fundamental idea that allows us for, let's say, adaptation to reality,
[1116.84 --> 1120.04]  say, is actually extremely simple what we did.
[1120.68 --> 1127.34]  So, in a sense, the initial approach is, you have this single simulation.
[1127.50 --> 1130.36]  You can think about it like a single universe in which you are training.
[1130.36 --> 1135.62]  And then you are asking, here is an alternative universe in which you want to actually verify the performance.
[1136.16 --> 1141.48]  And we are just instead saying, if you will have entire distribution, many universes,
[1142.02 --> 1149.04]  and network has a capability to encode, let's say, try to distinguish them,
[1149.04 --> 1155.56]  then it essentially might force the network to try to discover what are the underlying properties.
[1155.56 --> 1160.74]  So, let's say, if we don't know exactly what's the weight of the cube,
[1161.12 --> 1163.76]  or, I mean, more or less, maybe we know, but it might be off.
[1163.90 --> 1169.10]  If we have a network that just has a capability to, let's say,
[1169.48 --> 1171.94]  through interaction past the information,
[1172.22 --> 1175.36]  and these are like very common networks, recurrent neural networks,
[1175.36 --> 1181.60]  then, as we vary these parameters, and it tries in the simulation on all of these instances,
[1182.16 --> 1185.84]  maximize the score, it implicitly actually does,
[1186.10 --> 1190.34]  it has to try to, based on the initial few seconds,
[1190.76 --> 1192.82]  try to find out what are these values.
[1193.26 --> 1195.84]  I mean, it's like a combination of two things.
[1196.10 --> 1198.80]  On one side, it tries to be robust to some components,
[1198.80 --> 1203.14]  and on one side, it tries to adapt to various things.
[1203.14 --> 1209.30]  And, in essence, this is in the core of the idea to actually achieve the transfer to the reality.
[1209.74 --> 1211.04]  Yeah, that's really interesting.
[1211.42 --> 1217.16]  So, how long have you been kind of working towards this type of adaptation,
[1217.40 --> 1219.64]  and how has the process gone?
[1219.78 --> 1224.78]  Have you made other attempts to make this transfer to reality that haven't worked as well?
[1224.78 --> 1228.50]  Yes, so, and that project more or less took us one year.
[1229.60 --> 1233.22]  I would say, I mean, earlier on, there was, let's say, maybe five people.
[1233.36 --> 1237.32]  Later on in the project, there is maybe closer to, let's say, 15 or so.
[1237.54 --> 1239.70]  So, I would say average 10 human years.
[1240.12 --> 1243.04]  There were many, many attempts internally,
[1243.72 --> 1248.64]  and many of the things that we tried, they partially worked and so on.
[1248.64 --> 1253.86]  But, so, I mean, the way how the team is more or less organized is,
[1254.38 --> 1255.80]  once we agree on the goal,
[1256.20 --> 1259.48]  like I try to, let's say, engage people,
[1259.76 --> 1263.30]  and ask what do you think is the best way to solve the problem.
[1263.48 --> 1264.80]  And, in that sense, as I said,
[1264.98 --> 1268.44]  people to some extent are on many axes,
[1268.58 --> 1270.16]  they are smarter than me,
[1270.16 --> 1275.46]  and they might sometimes better know than me what's the best approach.
[1275.96 --> 1279.88]  When you're in the situation that there are multiple competitive approaches,
[1280.36 --> 1283.52]  they are also becoming closer to the truth, what really works.
[1283.72 --> 1286.00]  So, I mean, it's often the case that idea,
[1286.20 --> 1287.80]  as long as it is, let's say, sound,
[1288.04 --> 1289.96]  it will show signs of life,
[1290.16 --> 1293.80]  but it doesn't mean that this is the really ultimate solution.
[1294.14 --> 1296.42]  It might be sufficient for, you know,
[1296.48 --> 1299.04]  to present the conference or so,
[1299.04 --> 1302.90]  but our goal is truly to solve the problem
[1302.90 --> 1307.42]  and actually get to the solutions that we think we can push forward.
[1308.02 --> 1310.76]  So, when I was looking through the OpenAI website
[1310.76 --> 1314.26]  and kind of looking into some of what you're trying to achieve,
[1314.40 --> 1317.74]  I kept coming across this statement about, you know,
[1317.84 --> 1319.46]  safe applications of AI.
[1319.70 --> 1322.82]  And I know we've talked in the past about AI ethics and other things.
[1323.14 --> 1325.40]  I was wondering if you could briefly talk about, you know,
[1325.80 --> 1328.18]  safe AI, how you see that,
[1328.18 --> 1332.28]  and, you know, maybe what counter examples to safe AI would be.
[1332.78 --> 1335.28]  So, there are several problems into it.
[1335.70 --> 1337.56]  One problem is the question,
[1337.90 --> 1340.56]  how to ensure that the system will be achieving the goal
[1340.56 --> 1343.16]  in the way that we intended it to achieve.
[1343.16 --> 1348.18]  So, I mean, I see, I gather many kind of philosophical examples and so on,
[1348.22 --> 1349.78]  and I want to go through some of them.
[1350.32 --> 1351.98]  It sounds somewhat foreign,
[1352.10 --> 1356.02]  but simultaneously, we are starting to see that actually,
[1356.18 --> 1359.76]  it is not as trivial to tell actually system what to do,
[1359.80 --> 1364.10]  because it is completely abstracted from our values, ethics, and so on.
[1364.50 --> 1367.12]  So, in essence, you tell someone, make money.
[1367.12 --> 1373.38]  It's like the best way to make money is steal a car, sell drugs,
[1373.50 --> 1378.04]  like all the stuff that is really that you wouldn't intend the system to do.
[1378.46 --> 1379.56]  It's actually the best way.
[1379.56 --> 1380.92]  Things we probably don't want robots doing.
[1381.32 --> 1385.30]  Yeah, I mean, even you don't need robots for it to give you some example.
[1385.30 --> 1390.38]  Let's say if you are really insanely clever about stock market,
[1390.88 --> 1393.70]  you can, I'm saying insanely clever,
[1393.92 --> 1396.32]  and you know, you have superhuman capabilities,
[1396.82 --> 1400.38]  and what you truly care about is to maximize profit,
[1400.84 --> 1404.70]  you can, you know, cause a war in the country and short the stocks.
[1405.26 --> 1409.76]  And it is completely valid strategy if that's the quantity that you...
[1409.76 --> 1410.36]  To reach an objective.
[1410.64 --> 1411.54]  To reach the objective.
[1411.54 --> 1416.54]  And in some sense, you can say that the systems that we are training,
[1417.52 --> 1420.44]  you can say it has a little bit like a profile of psychopathy.
[1420.66 --> 1424.10]  It only cares about the one thing and one thing only.
[1424.44 --> 1426.56]  That's literally how we optimize them.
[1426.64 --> 1429.64]  They are completely abstracted away from everything else.
[1430.16 --> 1433.32]  And they want just these treats, treats, treats.
[1433.88 --> 1438.92]  And they actually don't know even about the things that are really important to us.
[1438.92 --> 1445.44]  So the question is, what's the way even to inject what we want?
[1445.80 --> 1447.06]  What is our ethics?
[1447.64 --> 1453.88]  And I mean, I would say there are multiple axes into safety.
[1454.04 --> 1458.92]  So just told you about one which is more or less called misspecification.
[1459.86 --> 1462.40]  I mean, so specify something, but it's actually something,
[1462.52 --> 1464.90]  something slightly different that you really wanted.
[1464.90 --> 1467.96]  And we can see it, like even in some computer games,
[1468.04 --> 1470.62]  that it has the system to maximize score in the game.
[1470.90 --> 1474.50]  But truly, you would like to ask the system to finish the game.
[1474.80 --> 1478.82]  And then it finds some back on some level of the game
[1478.82 --> 1481.64]  and keeps on staying there, let's say generating a lot of points.
[1482.04 --> 1484.62]  But actually it doesn't progress anymore in the game.
[1484.62 --> 1492.62]  I mean, there are other axes, which is how to make the systems robust to adversaries.
[1493.14 --> 1495.34]  And to give some concrete examples.
[1496.14 --> 1502.20]  So let's say there was a Twitter bot released by Microsoft, Tanya.
[1502.96 --> 1506.60]  And this folks from Microsoft, there is no doubt,
[1506.72 --> 1510.02]  there's like a lot of very clever researchers and so on.
[1510.02 --> 1514.38]  So I can say that it's like they thought through various scenarios.
[1514.70 --> 1517.08]  But despite, let's say, thinking it through,
[1517.40 --> 1524.42]  turns out that the bot within several hours was hijacked and repurposed.
[1524.88 --> 1528.58]  As it started saying very offensive things on Twitter.
[1529.32 --> 1531.10]  So as you might ask,
[1531.46 --> 1535.10]  is it the case that as the systems will become smarter,
[1535.36 --> 1537.98]  will they be less prone to it?
[1537.98 --> 1543.34]  I actually think that it might be due to the overall increased complexity.
[1543.50 --> 1545.36]  The surface area will just increase.
[1545.86 --> 1549.98]  Yeah, it's almost, even if you're trying to misspecify an objective,
[1550.38 --> 1552.96]  the space of objectives is larger.
[1553.18 --> 1554.02]  It's more complex.
[1554.76 --> 1558.42]  And so I would say from perspective of pursuing SAV-AGI,
[1558.96 --> 1561.64]  there are also per se three main things.
[1561.64 --> 1564.20]  So one, in order to achieve it,
[1564.26 --> 1568.70]  I mean, you have to, let's say, work toward capabilities.
[1569.20 --> 1572.52]  Second one is you have to work toward safety.
[1572.64 --> 1573.94]  So what we just discussed.
[1574.36 --> 1575.94]  And the third one is a question,
[1576.36 --> 1578.58]  let's say, even if we would have it today,
[1578.94 --> 1582.58]  what are the, what's the step in terms of a policy?
[1582.74 --> 1584.80]  What should we do with it?
[1584.80 --> 1589.62]  And I would say also all these three components actually fit into each other.
[1589.82 --> 1595.90]  So capabilities indicate actually maybe what the shape of AGI will be there for,
[1596.26 --> 1599.74]  what are the ways to actually inject our ethics and so on,
[1600.24 --> 1601.62]  the safety work.
[1601.98 --> 1604.52]  And also it helps the policy people.
[1605.16 --> 1609.20]  So I'm saying like all these topics, they fit into each other.
[1609.58 --> 1610.46]  Yeah, that makes sense.
[1610.46 --> 1616.08]  So I'd love to switch directions here for the last bit of the show
[1616.08 --> 1617.74]  and kind of get your perspective.
[1618.20 --> 1620.82]  So you mentioned a lot of really exciting things around robotics
[1620.82 --> 1624.22]  and a lot of that involved kind of large scale computing
[1624.22 --> 1627.16]  and lots of large simulations.
[1627.72 --> 1629.74]  I was wondering for people that are out there,
[1629.82 --> 1632.88]  like trying to get their hands dirty with some of these techniques,
[1633.00 --> 1634.96]  maybe it's reinforcement learning or other things.
[1635.26 --> 1638.52]  What are some good ways for people to kind of get their hands dirty
[1638.52 --> 1642.06]  and start working on problems that are interesting,
[1642.26 --> 1644.86]  but maybe they aren't able to run these, you know,
[1644.92 --> 1646.94]  large scale simulations and that sort of thing?
[1647.30 --> 1650.68]  Yeah, I mean, there are incredible materials online.
[1650.88 --> 1654.26]  So I would just go first through all Coursera, Udacity,
[1655.08 --> 1659.40]  lectures from Berkeley, Stanford, follow all the homeworks.
[1659.62 --> 1661.18]  So I would say that's step one.
[1662.26 --> 1663.74]  There's also great books.
[1663.92 --> 1666.50]  I mean, there is a book by Ian, deep learning book.
[1666.50 --> 1670.22]  There is reinforcement learning book by Richard Sutton.
[1670.74 --> 1673.58]  Yeah, and so I would say that would be my starting point.
[1673.94 --> 1678.12]  And I think it's actually quite important to get very strong fundamentals,
[1678.56 --> 1681.48]  for fundaments, because in the sense, by default,
[1682.06 --> 1686.44]  when you run your models, first, they do not work at all.
[1687.16 --> 1687.26]  Yeah.
[1687.50 --> 1690.44]  And then the question is, so what do you do?
[1690.44 --> 1696.84]  And the simpler models, the fewer tricks or steps you have to do,
[1697.12 --> 1699.40]  and you have to familiarize yourself with them.
[1699.58 --> 1702.46]  The harder models, the larger number of these steps.
[1702.84 --> 1706.32]  So it's very likely that at first you don't know any of them.
[1706.52 --> 1710.50]  If you need to do 10 things, you are less likely to succeed
[1710.50 --> 1712.86]  versus if you need to do two things.
[1712.86 --> 1716.26]  I would really recommend to go through fundamentals
[1716.26 --> 1720.92]  instead of jumping right away to the most difficult architectures.
[1721.08 --> 1723.90]  And I would really recommend to as much as you can
[1723.90 --> 1725.92]  to implement things from scratch.
[1726.40 --> 1727.96]  Yeah, that's a great point.
[1728.08 --> 1731.08]  I know I've had some experience in the past where, you know,
[1731.16 --> 1732.40]  some research comes out.
[1732.46 --> 1733.14]  It's really interesting.
[1733.38 --> 1737.24]  And, you know, you can go to a GitHub repo within a number of days
[1737.24 --> 1740.34]  and there's open source architecture there.
[1740.34 --> 1744.34]  But you try to run it and you see all these weird behavior
[1744.34 --> 1746.46]  and maybe it behaves differently than you would expect.
[1746.60 --> 1748.66]  But it's really hard if you don't know the fundamentals
[1748.66 --> 1752.30]  to dive into the debug and advance.
[1752.50 --> 1753.88]  So, yeah, that's great.
[1754.12 --> 1757.64]  I know I've appreciated what you've said about any one person,
[1757.86 --> 1761.00]  even yourself who's advanced a lot in this field,
[1761.10 --> 1764.12]  doesn't have all of the pieces of knowledge to, you know,
[1764.24 --> 1768.92]  perform successful research or to advance a project.
[1768.92 --> 1773.48]  I was wondering at OpenAI, how do you kind of structure your teams
[1773.48 --> 1776.66]  and what do you look for when you're kind of putting together a team
[1776.66 --> 1779.88]  so that you have a variety of experience and perspectives
[1779.88 --> 1782.52]  to actually give a good result?
[1782.98 --> 1788.00]  So, different teams, they have a little bit different values
[1788.00 --> 1789.68]  and they are differently organized.
[1789.94 --> 1791.76]  I can speak about robotics.
[1791.94 --> 1795.92]  It's extremely important to have people who are good team players.
[1795.92 --> 1798.66]  I would say also when we hire people,
[1799.26 --> 1803.32]  we hire it based on being incredible in something.
[1803.74 --> 1808.26]  It doesn't need to be exactly what they will be working on.
[1808.42 --> 1811.90]  Or so, it's like more or less you want to verify brilliancy
[1811.90 --> 1817.78]  and that's a sign that a person can adapt whatever is needed.
[1818.18 --> 1820.64]  And also, let's say, so in a sense,
[1821.06 --> 1824.02]  I want people to be able from day zero to contribute.
[1824.02 --> 1828.00]  Still, let's say, I encourage to spend one day per week on,
[1828.46 --> 1830.44]  let's say, do arbitrary learning.
[1830.58 --> 1833.10]  We have, let's say, internally curriculum with simple stuff.
[1833.32 --> 1836.74]  I like people who are excited about their resolving problems.
[1836.88 --> 1839.38]  So, in a sense, when it comes to difficult problems,
[1839.52 --> 1841.66]  as for instance, as the last project,
[1841.80 --> 1845.58]  it is very common that the time in the middle
[1845.58 --> 1848.44]  is when everything is extremely difficult.
[1848.44 --> 1851.04]  And you need that people who have this, let's say,
[1851.30 --> 1853.88]  internal energy that they can, you know,
[1854.00 --> 1856.34]  still push it through and get it through.
[1856.60 --> 1860.36]  Yeah, so persistence and motivation and passion for the problem.
[1860.54 --> 1860.78]  Correct.
[1861.10 --> 1861.68]  Yeah, awesome.
[1862.30 --> 1863.90]  Well, I'd love to take time.
[1863.98 --> 1864.66]  If there's anything,
[1865.14 --> 1868.68]  where can people find out, you know, more about OpenAI?
[1868.68 --> 1871.04]  And are there any kind of open source projects
[1871.04 --> 1874.08]  or papers or efforts that you'd like to kind of share?
[1874.22 --> 1877.32]  And we can, we'll for sure post those in the show links and everything.
[1877.68 --> 1880.00]  We are quite frequently releasing
[1880.00 --> 1882.68]  what we are able to build on our blog.
[1882.68 --> 1886.62]  So, that's at the openai.com website.
[1886.98 --> 1889.54]  We are also quite active on Twitter.
[1889.92 --> 1891.96]  So, it's twitter.com slash openai.
[1892.46 --> 1896.20]  Third word, you asked about the research proposals or so.
[1896.48 --> 1898.40]  We posted, I think, even twice,
[1898.78 --> 1903.78]  let's say, a bunch of ideas for projects for people
[1903.78 --> 1905.90]  if they want to pursue it.
[1906.10 --> 1908.88]  There's even indication of the level of difficulty.
[1909.32 --> 1910.66]  That might be a place to start.
[1910.94 --> 1911.34]  Awesome.
[1911.54 --> 1912.50]  And where can we find that?
[1912.92 --> 1915.12]  That's also on our website.
[1915.60 --> 1915.90]  Awesome.
[1916.32 --> 1918.48]  Well, I really appreciate you taking time.
[1918.62 --> 1919.94]  I know that you must be busy
[1919.94 --> 1921.20]  and you're getting ready for your talk.
[1921.30 --> 1923.20]  So, I'll let you get back to that.
[1923.28 --> 1924.96]  But thank you so much for joining us.
[1924.98 --> 1926.08]  It was a really great conversation.
[1926.28 --> 1926.86]  Thank you, Daniel.
[1929.74 --> 1930.26]  All right.
[1930.30 --> 1932.92]  Thank you for tuning into this episode of Practical AI.
[1932.92 --> 1934.66]  If you enjoyed this show, do us a favor.
[1934.78 --> 1936.14]  Go on iTunes, give us a rating.
[1936.46 --> 1938.30]  Go in your podcast app and favorite it.
[1938.38 --> 1940.10]  If you are on Twitter or social network,
[1940.22 --> 1941.12]  share a link with a friend.
[1941.18 --> 1941.86]  Whatever you got to do,
[1941.86 --> 1943.54]  share the show with a friend if you enjoyed it.
[1943.82 --> 1946.52]  And bandwidth for ChangeLog is provided by Fastly.
[1946.64 --> 1948.06]  Learn more at Fastly.com.
[1948.16 --> 1951.48]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[1951.68 --> 1954.06]  Check them out at Rollbar.com slash ChangeLog.
[1954.06 --> 1956.88]  And we're hosted on Linode cloud servers.
[1957.16 --> 1958.84]  Head to Linode.com slash ChangeLog.
[1958.92 --> 1959.40]  Check them out.
[1959.48 --> 1960.30]  Support this show.
[1960.62 --> 1963.88]  This episode is hosted by Daniel Whitenack and Chris Benson.
[1964.38 --> 1965.82]  Editing is done by Tim Smith.
[1966.06 --> 1968.10]  The music is by Breakmaster Cylinder.
[1968.44 --> 1971.94]  And you can find more shows just like this at ChangeLog.com.
[1971.94 --> 1974.08]  When you go there, pop in your email address.
[1974.36 --> 1978.20]  Get our weekly email keeping you up to date with the news and podcasts for developers
[1978.20 --> 1980.40]  in your inbox every single week.
[1980.76 --> 1981.56]  Thanks for tuning in.
[1981.56 --> 1982.48]  We'll see you next week.
