[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.22 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.22 → 102.28] And now onto the show.
[106.54 → 108.48] Welcome to the Practical AI podcast.
[108.76 → 109.84] This is Chris Benson.
[110.46 → 115.62] We are the podcast that brings AI to you in a practical, productive, and accessible way.
[115.62 → 122.72] I am at NVIDIA's GPU Technology Conference in March 2019.
[123.22 → 128.52] And we have a lot of world-class people in the AI space here.
[129.28 → 134.28] And normally, I would have my co-host, Daniel Whiten ack, joining me.
[134.62 → 136.24] He was not able to make it this time.
[136.24 → 140.86] But I have the pleasure of introducing to you Adam Stuck.
[141.14 → 146.48] Adam is a graduate student who is studying robotics and deep learning at UC Berkeley.
[147.44 → 153.44] And he's really focused on scaling deep reinforcement learning and hierarchical reinforcement learning.
[153.98 → 156.26] And so it's a pleasure to have you on the show, Adam.
[156.56 → 157.08] Welcome.
[157.48 → 157.64] All right.
[157.68 → 158.14] Thank you, Chris.
[158.20 → 158.98] It's a pleasure to be here.
[158.98 → 170.44] So I wanted to note, and we'll dive into it in a few minutes, that you had done a talk called Doing More With More Recent Achievements in Large-Scale Deep Reinforcement Learning.
[170.60 → 181.34] But before we dive into the meat of it, could you tell me a little bit about your background, kind of how you got here, how you discovered deep learning and deep reinforcement learning, and kind of what your story is?
[181.52 → 181.78] Sure.
[181.78 → 181.82] Sure.
[182.12 → 190.34] I've been working and studying deep reinforcement learning for about four years now as a PhD student at UC Berkeley under my professor, Peter Abel.
[190.60 → 194.90] Previous to that, I had studied physics and mathematics in undergrad.
[195.42 → 198.34] I actually did a master's in physics here at UC Berkeley.
[198.88 → 201.04] And then I was in the Air Force at the time.
[201.24 → 202.78] So I was pulled away on active duty.
[203.30 → 209.12] I was very lucky to land a position at the Air Force Research Lab in Albuquerque, New Mexico.
[209.12 → 213.26] So I kept my technical chops up pretty well during this period.
[213.90 → 222.86] And, yeah, about four years ago, my time in the Air Force kind of came to a natural end, and I came back to school and was looking for what's hot, what's next.
[223.18 → 224.98] And, yeah, the robots caught my eye.
[225.20 → 229.00] So I got to start off by saying a couple of things, connections here.
[229.06 → 237.16] First, Daniel is going to be completely jealous that he's not here because he is a physicist who also came into the AI space as well.
[237.16 → 241.00] So he's going to be going, ah, gosh, why did you take it, Chris?
[241.30 → 243.36] So sorry, Daniel, on that.
[243.78 → 251.28] And number two, being in the Air Force, I work for Lockheed Martin in the AI space, and we do a lot of work with the Air Force.
[251.60 → 261.56] So anyway, I guess, so as you started, were you already interested in deep learning, reinforcement learning when you were in the Air Force, or did that come along sometime thereafter?
[261.56 → 266.98] No, this came along after, actually, only once I returned to graduate school.
[267.28 → 271.84] What I did get out of my time in the Air Force was just kind of by accident.
[272.02 → 283.84] It became a first exposure to me to a lot of programming and modelling and simulation in order to make informed decisions about technologies that we were going to invest in and try to fly in space.
[284.06 → 285.58] What kind of tools were you using while you were doing that?
[285.58 → 291.98] In that case, I was programming pretty much entirely in MATLAB and a little bit of Excel.
[292.10 → 292.40] Why not?
[292.64 → 295.62] Yeah, but that's actually a lot of people I know get into it from that.
[295.68 → 297.02] So that's totally valid.
[297.48 → 301.08] And so, yeah, that kind of gave me the first impression of like, wow, this is really powerful.
[301.28 → 309.12] If you can craft a good simulation and run this program in the computer, it can tell you a lot of important things about what's going to happen in the real world.
[309.12 → 317.88] And that was the first thing that kind of turned me on to this idea so that when I came back to school, it was kind of a natural thing to look to a computer science department.
[318.26 → 319.86] Yeah, so tell me a little bit about that process.
[320.08 → 321.00] You're out of the Air Force.
[321.08 → 321.78] You're getting into school.
[321.86 → 322.72] How did you discover it?
[323.62 → 326.26] What, you know, what specifics did you get into?
[326.94 → 329.16] How did you find your way eventually to reinforcement learning?
[329.76 → 337.14] Yeah, so I came back to school and I rejoined the physics department at Berkeley where I'm actually still technically a member.
[337.14 → 348.58] But after about a semester and a summer of kind of floating around to different research groups and finding a lot of really, really deep and interesting projects going on, but not really getting the personal feeling.
[348.76 → 355.38] Like I was finding a place where I wanted to be continuing the work after graduating.
[355.74 → 358.78] You know, doing the PhD in physics still has a really strong draw to me.
[358.78 → 362.02] But I started to look to other things to do after graduation.
[362.02 → 368.80] And then eventually I decided, well, if I'm going to do something different after graduating, why don't I get ready to do something different before graduating?
[369.08 → 376.94] And so I started looking a little broader and found the robotics work happening kind of across the street on the campus there.
[377.06 → 377.32] Okay.
[377.42 → 378.50] And a computer science.
[378.60 → 382.56] Very lucky to be at such a powerhouse research university like Berkeley.
[382.60 → 382.86] Absolutely.
[382.86 → 385.80] With a hand in so many, leading in so many different fields.
[386.72 → 391.46] So, yeah, I just kind of went across the street and knocked on the door and said, hey, can I play?
[392.32 → 402.64] And a year or two of basically reaccomplishing an entire set of graduate coursework and projects later, the professor finally says, yeah, you know what, Adam?
[402.74 → 403.96] Okay, you can stay.
[404.08 → 405.02] You can do this with us.
[405.04 → 406.82] He made you earn your chops there, didn't he?
[406.84 → 410.12] Which is code for I can see you're not going away, so I might as well.
[410.12 → 415.88] So, you know, persistence there, you know, intelligence and all, but you're sticking with it there.
[416.04 → 419.50] So they were a robotic shop at this point that you're moving into?
[419.94 → 420.40] That's correct.
[420.48 → 421.38] Yeah, it's a robotic shop.
[422.26 → 427.08] And at the same time, it's a lot about applying deep learning to robotics.
[427.44 → 427.62] Okay.
[427.62 → 435.28] So kind of my personal path since then has actually been much heavier on the deep learning side, the deep reinforcement learning in particular.
[435.76 → 441.26] And before we even go on, we've mentioned reinforcement learning and deep reinforcement learning several times already.
[441.66 → 446.80] Could you tell us how you would interpret those in terms of what they are for anyone that doesn't know what that is?
[446.80 → 447.28] Sure.
[447.46 → 454.52] Yeah, let's start with reinforcement learning, which has a little bit of a longer history and kind of pedigree behind it.
[454.80 → 459.38] It's basically a kind of formal way of doing learning by trial and error.
[459.90 → 463.28] So you've got some sort of task that you're trying to figure out how to do.
[463.78 → 470.84] You know what are the different possible, you know, small actions that you can do in order to try to achieve that task,
[470.84 → 475.40] but you don't necessarily know ahead of time what the task is or how to do it.
[475.58 → 478.00] So you just explore, you try things.
[478.76 → 482.94] The key thing is that you get a signal back from the task.
[483.42 → 484.76] That's what we call a reward.
[485.26 → 488.42] When you receive a positive reward, it says, oh, you did a good thing.
[488.56 → 489.42] So do that more.
[489.56 → 492.14] When you receive a negative reward, it says, oh, you did a bad thing.
[492.20 → 492.98] So do that less.
[494.28 → 498.74] And yeah, based on queuing off of those signals, basically, again, through trial and error, gradually over time.
[498.74 → 499.26] Make an adjustment.
[499.26 → 505.40] You make an adjustment, you try again, and then eventually you can learn to do some pretty sophisticated tasks through this.
[505.54 → 513.08] So there's a whole mathematical formalism kind of like built up around this that we don't necessarily need to go into the depths of all the terms with that,
[513.14 → 514.18] but it's pretty well established.
[514.72 → 519.08] And a more recent development is deep reinforcement learning,
[519.20 → 523.76] which simply refers to the application of deep learning to reinforcement learning.
[523.76 → 529.42] deep learning, meaning for all practical purposes, using deep neural networks.
[529.90 → 530.02] Sure.
[531.02 → 539.52] And at a high level, without diving too deep on this, can you talk a little bit about how you're applying deep learning to integrate that into reinforcement learning?
[539.78 → 547.12] Is there a high enough level for kind of understanding of what that integration is without diving too far into the math?
[547.12 → 548.44] Sure. Yeah, we can do that.
[548.44 → 548.80] Okay.
[548.80 → 556.92] So one of the key components that you have in a reinforcement learning system is the learning, what you would call the learning agent itself.
[557.18 → 562.36] So the learning agent is interacting with the environment, which contains the task.
[562.36 → 575.04] And the learning agent is where the deep learning comes in, because the learning agent is going to be somehow making use of a deep neural network to express its decision-making.
[575.40 → 575.50] Sure.
[575.92 → 581.22] And so this gives performance advantages over what you could previously do with just reinforcement learning,
[581.38 → 587.02] given the fact that there are so many more options available in terms of adjustments that you can make going forward, I assume.
[587.08 → 588.16] That's exactly right, yes.
[588.16 → 598.50] So in terms of the interfaces between the environment and the agent, so the environment provides some sort of information to the agent that the agent gets to look at and use,
[598.92 → 602.14] and we're making its decision of what to do next.
[602.48 → 611.72] And it turns out that deep neural networks basically open up a whole new class of environments of much more complicated sets of information
[611.72 → 616.18] that the agent is able to digest in order to figure out what to do next.
[616.18 → 623.56] Sure. So I guess, as you got into this environment, they've accepted you into the fold.
[624.26 → 628.58] What did you do? What captured your imagination as you got into some of your first projects with the group?
[629.72 → 640.20] Yeah, I think early on the projects that I kind of cued in on the most were some early work out of DeepMind on learning to play Atari games from scratch,
[640.20 → 645.16] using only the screen image as input to the learning agent.
[645.28 → 650.58] So in a very similar style to a way that a human would actually operate to play the game.
[650.96 → 656.84] So I remember reading about that. Can you tell us a little bit about what that was and how it inspired you to move forward?
[657.72 → 662.76] Sure, yeah. So this was about five or more years ago by now, maybe.
[662.76 → 668.24] Maybe it was the first result of, again, playing Atari from only the screen image.
[668.52 → 670.20] It made a big splash when it came out.
[670.28 → 670.70] It sure did.
[670.78 → 673.82] There was a Nature article about it, cover of Nature even.
[674.06 → 674.20] Yeah.
[674.20 → 683.10] So this published a lot more broadly than the usual learning-only conferences and this sort of thing.
[683.62 → 688.46] And then very shortly after that, after the initial successes there with the first algorithm,
[688.72 → 693.30] then another paper comes out with a second learning algorithm that's a little bit different,
[693.42 → 696.00] but is also getting good results, maybe running a little bit faster.
[696.00 → 701.96] And then over the next several years, kind of in rapid fire, these teams that came out with the original ones
[701.96 → 705.32] are making little enhancements here, little enhancements there, piling them on.
[705.52 → 710.30] And before you know it, these learning algorithms are just completely destroying these Atari games
[710.30 → 713.48] way, way beyond the human level.
[714.94 → 721.36] And it really is just a springboard for lots of more sophisticated and more interesting games, for instance,
[721.46 → 722.68] to come after that.
[722.68 → 731.18] So, you know, obviously that's been a while since the Atari news that came out in Nature and stuff.
[731.44 → 732.72] Where did that take you at that point?
[732.78 → 735.88] As you're getting into this, what captured your interest?
[736.04 → 737.78] What did you choose to do?
[737.88 → 741.12] What activities in terms of research did you want to engage in?
[741.68 → 742.86] What was that journey like?
[742.92 → 747.18] Because a lot of us out here who are very interested may not have had that experience.
[747.18 → 752.62] And I'm just very curious about how that evolved to where you are today with the talks that you're giving at this point.
[752.68 → 759.88] Yeah, I think it actually ended up in combination with a certain course that I was taking on parallel computing.
[760.32 → 765.80] It actually led me down the path of scaling up implementations of deep reinforcement learning.
[766.18 → 770.54] So taking an algorithm, okay, this algorithm is like shown to work and here's how we run it.
[770.60 → 776.62] Maybe we're running it on a small computer, and it takes five or ten days to do one learning run
[776.62 → 780.92] and to see the thing go from losing every point in Pong to winning every point in Pong.
[781.34 → 782.22] Okay, this is exciting.
[782.32 → 782.78] This is working.
[782.94 → 785.58] This is something we've got like something real to go on here.
[785.82 → 795.82] Now let's refine it and scale it up and adjust it to make much better use of the computers that are available today.
[796.38 → 799.70] And I mean, long story short, that has a lot to do with why I'm here at GTC.
[799.70 → 801.92] Yep, we're working our way there.
[803.76 → 808.08] So you mentioned already to compute being a huge limitation.
[808.76 → 814.28] And obviously we are at NVIDIA GTC where it's all about compute and so many things.
[814.98 → 817.46] So I guess, you know, what bridged you?
[817.60 → 823.10] You know, today you did this talk doing more with more recent achievements in large-scale deep reinforcement learning.
[823.10 → 828.68] What kinds of things are you covering in that and, you know, what was the evolution to get to that point?
[829.44 → 833.98] And what were some of the milestones that you went through along the way to get to where you're at now?
[834.60 → 834.78] Sure.
[834.96 → 843.04] I think some of the early steps started out with just taking a kind of in-house algorithm,
[843.32 → 844.88] reinforcement learning algorithm that we had,
[844.88 → 855.56] and identifying kind of the key pieces in a way that the algorithm could be broken down to operate in parallel over more compute resources.
[855.88 → 859.32] So instead of just one CPU core running the computation or whatever,
[859.64 → 869.22] maybe you can use all the CPU cores in the machine, 16 of them running in parallel in a smart way that gets you 16 times faster to the answer.
[869.22 → 877.28] And so this is kind of how I started was just with one example kind of algorithm like this
[877.28 → 880.42] and just a lot of practice of figuring out how to set that up,
[880.44 → 885.04] how to set that up in a computer and get it to run and actually get the efficiency out.
[886.02 → 888.10] And you hadn't even gotten to the GPU world yet.
[888.22 → 889.66] I hadn't even gotten to the GPU world.
[889.78 → 890.66] No, no.
[891.46 → 897.10] And then let's see, with this, I actually took a little, once we had this running up and running smoothly,
[897.10 → 903.62] took a little detour through actually an Intel Knight's Landing development kit that we bought.
[903.82 → 912.14] So a CPU-based architecture, but with maybe 60 or 70 cores that we could successfully parallelize across.
[912.76 → 916.46] But ended up finding in the end that, no, really, the GPU...
[916.46 → 918.68] It wasn't quite up to what you needed, was it?
[918.68 → 921.66] It wasn't quite up to what we needed, and really, there's no way around it.
[921.68 → 923.60] Like, the GPU was the way to go.
[923.60 → 929.72] So at what point, you know, how long ago was that where you realized you needed to go GPUs
[929.72 → 933.80] and you started grabbing those because you realized that you were limiting yourself
[933.80 → 935.52] until you could speed up your training?
[936.00 → 939.86] Yeah, I think by now this was maybe about two years ago or so.
[940.38 → 942.16] So it was a bit of a journey.
[943.00 → 945.18] Yeah, starting on the GPUs about two years ago,
[945.28 → 947.70] and then about one year ago kind of wrapping up the project
[947.70 → 949.98] and more or less having it in shape.
[949.98 → 954.00] Yep. So one of the things I was thinking as you were taking me through this,
[954.26 → 957.00] what were you trying to achieve with some of these projects?
[957.18 → 961.80] As you're doing these experiments and carrying it forward,
[961.88 → 963.10] what was your end goal in mind?
[963.18 → 964.44] What were you trying to get to?
[964.98 → 968.24] Yeah, so the main project that I was working on over this period
[968.24 → 972.44] was really just, man, we had a need for speed.
[972.44 → 977.22] We were just going to explore these deep reinforcement learning algorithms
[977.22 → 981.88] and see how fast can we learn one Atari game
[981.88 → 987.06] and see what kind of records we can't set and otherwise blow out of the water.
[987.70 → 991.04] So it turns out that a lot of the same techniques for parallelism
[991.04 → 993.52] that were useful in the CPU setting,
[993.94 → 996.20] the same principles applied in the GPU setting
[996.20 → 1001.62] for using multiple GPUs inside one computer to run the algorithm.
[1001.62 → 1005.04] So about the same time that I was setting down that path anyway,
[1005.30 → 1010.82] we were very lucky enough to have NVIDIA come by
[1010.82 → 1015.52] and donate actually a DGX1 as part of their university research support.
[1015.52 → 1017.12] That's a great donation, you know?
[1017.14 → 1019.28] That's the kind of donation I want right there.
[1019.72 → 1022.40] So yeah, this is a really fortunate moment for us
[1022.40 → 1023.86] and good timing for me.
[1024.06 → 1025.96] That's about the time I was getting into this anyway,
[1026.08 → 1026.88] and my advisor says,
[1026.98 → 1029.14] hey, Adam, we've got this DGX1,
[1029.38 → 1031.52] and well, here you go.
[1032.62 → 1033.94] Go to it.
[1034.02 → 1034.96] Go to it, exactly.
[1035.04 → 1036.54] Here's the first AI supercomputer.
[1036.98 → 1037.44] Have at it.
[1037.78 → 1038.10] Exactly.
[1038.76 → 1040.62] And so I couldn't say no to that.
[1040.72 → 1041.60] I mean, didn't want to say no to that.
[1041.62 → 1042.20] Of course not.
[1042.28 → 1042.96] Couldn't say no to that.
[1043.04 → 1043.80] That's Christmas right there.
[1043.94 → 1047.08] And then couldn't stop once I started either.
[1047.08 → 1047.12] Sure.
[1048.54 → 1052.44] I'm guessing it was speeding up your process a little bit there,
[1052.52 → 1054.88] you know, to go from CPUs.
[1055.62 → 1057.60] And it sounds like you didn't have an in-between.
[1057.72 → 1061.28] Did you go straight from CPU all the way to using DGX1 just like that,
[1061.28 → 1064.62] or was there any intermediate steps along the way?
[1064.74 → 1065.40] No, that's right.
[1065.44 → 1068.52] We pretty much just went straight to the DGX1.
[1068.70 → 1068.88] Wow.
[1069.94 → 1071.18] That's like stepping out.
[1071.18 → 1073.92] That's like stepping out of this old jalopy car
[1073.92 → 1076.72] and getting right into the Lamborghini and just going.
[1076.98 → 1077.40] That's it.
[1077.62 → 1078.00] That's it.
[1079.62 → 1080.44] I don't, yeah.
[1081.34 → 1082.74] So I'm just curious.
[1083.14 → 1085.80] You know, it's non-trivial to,
[1086.18 → 1089.02] you have to kind of learn how to use a DGX1.
[1089.48 → 1092.52] They suddenly plopped one into your lap and said,
[1092.60 → 1094.08] hey, make use of this thing.
[1094.08 → 1095.88] And, you know, what was the
[1096.16 → 1099.88] were you already familiar with containerization and Kubernetes and things,
[1099.88 → 1103.94] or was there a learning curve for you to get ready to use the box?
[1104.20 → 1106.40] Or what was that like to make that transition?
[1106.66 → 1107.94] There was a little bit of a learning curve.
[1108.24 → 1109.22] And so at this point,
[1109.24 → 1112.04] I was already pretty familiar with the deep learning,
[1112.28 → 1114.32] the particular deep learning library that we were using,
[1114.76 → 1116.28] which at this time was Thea no.
[1117.74 → 1120.20] And luckily enough, about the same time,
[1120.20 → 1123.98] Thea no released support for Nickel,
[1124.24 → 1126.96] so NVIDIA's collective communication library,
[1126.96 → 1132.72] which is for direct interconnects between the GPUs within the DGX1
[1132.72 → 1134.22] for very fast operations,
[1134.92 → 1137.02] very fast communication, sorry.
[1138.08 → 1141.12] And so, yeah, the learning curve was mainly around,
[1141.34 → 1143.32] okay, I already am familiar with this deep learning library,
[1143.48 → 1147.32] but let's see how to plug it into use for multiple GPUs.
[1147.58 → 1150.70] This was a pretty new thing at that time, about two years ago.
[1151.06 → 1156.26] And so there wasn't really built-in support from Thea no for multi-GPU use.
[1156.26 → 1159.04] There was some kind of preliminary stabs at that,
[1159.12 → 1162.84] but what I ended up doing was kind of writing our own libraries
[1162.84 → 1165.02] for the parallel processing aspects.
[1165.10 → 1165.38] Sure.
[1165.78 → 1169.68] And then, yeah, again, luckily having the Thea no guys expose
[1169.68 → 1172.90] an interface to this Nickel, this communications library,
[1172.90 → 1177.26] to tie the multiple GPUs together in the most efficient way possible
[1177.26 → 1179.70] based on the NVIDIA hardware that was inside.
[1179.90 → 1180.14] Gotcha.
[1180.14 → 1180.22] Gotcha.
[1181.18 → 1185.48] And I guess, were you already in the middle of a particular project
[1185.48 → 1187.96] when the DGX1 came into the picture,
[1188.18 → 1190.72] or did you kind of pick it up as you picked up a new project
[1190.72 → 1191.26] to move forward?
[1191.94 → 1193.48] No, I think looking back on it,
[1193.50 → 1194.58] I hadn't really thought about this before,
[1194.66 → 1196.38] but it was just incredibly fortunate timing
[1196.38 → 1199.04] because I was already on this project,
[1199.20 → 1202.14] had already been tinkering around with the night's landing for some time
[1202.14 → 1205.98] and was ready to move on for that and move to GPUs.
[1206.70 → 1209.42] And so, no, it just, like, the timing couldn't have been better
[1209.42 → 1210.56] when this came in.
[1210.62 → 1211.04] It happened.
[1211.18 → 1212.16] Oh, that sounds fantastic.
[1212.40 → 1217.06] So, I guess, as you're making this transition,
[1217.62 → 1219.80] how are you, so you now have this DGX1
[1219.80 → 1222.30] that's been gifted to you,
[1222.38 → 1224.10] and they're saying, go do stuff with it.
[1225.34 → 1226.30] What's going through your head?
[1226.34 → 1227.78] What kind of projects are you thinking about?
[1227.88 → 1229.28] You're now into deep reinforcement learning,
[1229.38 → 1230.30] I assume, at this point,
[1230.38 → 1233.16] and you have the power to drive that forward.
[1233.58 → 1234.50] What were you thinking,
[1234.62 → 1236.22] and what kinds of projects have you taken on
[1236.22 → 1238.84] over the last couple of years to take advantage of that?
[1239.98 → 1241.46] Yeah, so, I mean, again,
[1241.46 → 1242.38] a lot of the work at the beginning
[1242.38 → 1245.38] was just scaling out the reinforcement learning itself,
[1245.46 → 1247.20] taking existing algorithms and showing,
[1247.20 → 1250.56] discovering that they can be scaled up
[1250.56 → 1251.90] to run on the entire system
[1251.90 → 1254.26] so that we could use all eight GPUs
[1254.26 → 1256.78] and all 40 CPU cores within a DGX1
[1256.78 → 1259.06] to learn a single Atari game
[1259.06 → 1261.96] and get, basically, linear speed-ups with that.
[1262.14 → 1266.24] So, instead of taking 10 or 15 hours to Master Pong,
[1266.78 → 1269.24] you know, we're getting it to, like, four minutes.
[1269.42 → 1269.78] Yep.
[1270.24 → 1272.08] Or so, which was...
[1272.08 → 1273.90] That probably helped your productivity a little bit.
[1273.92 → 1274.40] Which helps the productivity, it does.
[1274.40 → 1275.32] Go get a cup of coffee,
[1275.40 → 1276.42] and you come back, and it's done.
[1276.42 → 1277.22] Come back, and it's done.
[1277.30 → 1280.02] And then you can iterate and try the next thing.
[1280.68 → 1282.00] And that was actually, I think,
[1282.20 → 1283.56] a pretty interesting finding
[1283.56 → 1286.78] because one of the key techniques
[1286.78 → 1289.40] to scaling up to using multiple GPUs
[1289.40 → 1292.86] that we also see across a lot of other scaling efforts
[1292.86 → 1295.84] is increasing the training batch size.
[1296.20 → 1298.42] So, how many in this...
[1298.98 → 1300.10] There might be a couple of points
[1300.10 → 1301.16] where we need to stop back here
[1301.16 → 1301.88] and make some definitions,
[1302.12 → 1305.08] but when training these neural networks,
[1305.08 → 1307.76] we often use this algorithm called stochastic gradient descent.
[1307.76 → 1308.08] Mm-hmm.
[1308.34 → 1311.96] And can you define that for the audience loosely?
[1312.34 → 1312.78] Sure can.
[1312.88 → 1313.26] Sure can.
[1313.36 → 1315.26] So, basically, you're going to have
[1315.26 → 1318.76] some way that you want to change the outputs,
[1319.84 → 1321.26] change the behaviour of the neural net,
[1321.34 → 1323.14] which is this decision-making function
[1323.14 → 1324.74] inside your reinforcement learning agent.
[1324.74 → 1327.28] And you're going to change it
[1327.28 → 1329.22] based on experience that you have in the game.
[1329.68 → 1332.28] But instead of making updates
[1332.28 → 1334.56] on all the possible experience that you could gather,
[1335.08 → 1337.24] you'll gather a little bit of experience at a time
[1337.24 → 1338.52] and then make a small adjustment.
[1338.74 → 1340.44] And then gather a little bit of experience at a time
[1340.44 → 1341.54] and make a small adjustment.
[1341.54 → 1350.60] This episode is brought to you
[1350.60 → 1352.08] by O'Reilly Open Source Conference
[1352.08 → 1353.28] in Portland, Oregon,
[1353.66 → 1355.16] July 15th through 18th.
[1355.20 → 1356.10] We'll be there, by the way.
[1356.32 → 1356.92] As you know,
[1357.02 → 1358.72] Oz Con has been ground zero
[1358.72 → 1360.96] for the open source community for 20 years.
[1361.14 → 1361.94] And this year,
[1362.08 → 1363.28] they're expanding to become
[1363.28 → 1365.02] a software development conference
[1365.02 → 1366.08] because in 2019,
[1366.58 → 1368.78] software development is open source.
[1368.78 → 1369.60] At Oz Con,
[1369.64 → 1370.50] you get to see what's shaping
[1370.50 → 1371.78] the future of software development.
[1371.96 → 1373.14] The program covers everything
[1373.14 → 1374.12] from open source,
[1374.34 → 1375.44] AI, infrastructure,
[1375.66 → 1376.06] blockchain,
[1376.62 → 1377.32] edge computing,
[1377.54 → 1378.06] architecture,
[1378.24 → 1379.26] and emerging languages.
[1379.78 → 1380.58] Hear from industry leaders
[1380.58 → 1381.40] like Holden Caro,
[1381.86 → 1382.64] RPA Dmitri,
[1383.06 → 1383.80] Julian Simon,
[1384.28 → 1385.26] and Allison McCauley.
[1385.70 → 1386.74] Learn more and register
[1386.74 → 1387.82] at ozcon.com
[1387.82 → 1389.10] slash changelog prices
[1389.10 → 1390.68] start at just $925
[1390.68 → 1393.72] when you register before April 19th.
[1393.72 → 1394.28] After that,
[1394.32 → 1395.38] the price is going to go up.
[1395.50 → 1396.70] Plus, you can use our code
[1396.70 → 1397.58] changelog20
[1397.58 → 1398.94] to get 20% off
[1398.94 → 1399.48] your bronze,
[1399.64 → 1399.82] silver,
[1399.98 → 1400.60] or gold passes.
[1401.08 → 1401.74] Once again,
[1401.84 → 1403.42] our code is changelog20
[1403.42 → 1404.96] and head to ozcon.com
[1404.96 → 1405.72] slash changelog
[1405.72 → 1407.12] to learn more and register.
[1424.34 → 1426.08] Okay, so having defined
[1426.08 → 1427.42] stochastic gradient descent,
[1427.58 → 1429.78] take us forward on that.
[1429.98 → 1431.20] Okay, so the next step
[1431.20 → 1433.20] into making stochastic gradient descent
[1433.20 → 1434.42] run more efficiently
[1434.42 → 1435.98] on a GPU,
[1436.24 → 1436.84] which is itself
[1436.84 → 1437.86] a highly parallel
[1437.86 → 1438.96] computing platform,
[1439.42 → 1440.82] is one way to do this
[1440.82 → 1441.70] is to increase
[1441.70 → 1443.10] the training batch size.
[1443.44 → 1444.22] So increase the amount
[1444.22 → 1444.72] of experience
[1444.72 → 1445.40] that you gather
[1445.40 → 1446.54] and use together
[1446.54 → 1447.22] each time you're going
[1447.22 → 1448.04] to make a slight adjustment
[1448.04 → 1449.88] to this decision-making function.
[1450.52 → 1451.36] And that gives you
[1451.36 → 1452.36] full utilization
[1452.36 → 1453.20] of this GPU,
[1453.36 → 1453.92] which is kind of like
[1453.92 → 1455.28] a fat and wide
[1455.28 → 1456.26] computing pipe.
[1456.58 → 1456.70] Yep.
[1456.70 → 1457.42] And if you want
[1457.42 → 1458.24] to make full use
[1458.24 → 1459.30] of eight GPUs,
[1459.34 → 1460.18] then you need
[1460.18 → 1461.30] to have eight times
[1461.30 → 1462.60] bigger training batch size
[1462.60 → 1463.68] in your algorithm
[1463.68 → 1465.14] because you need
[1465.14 → 1466.10] to fill up all eight
[1466.10 → 1467.10] of those GPUs
[1467.10 → 1468.30] in order to run them
[1468.30 → 1468.72] efficiently.
[1469.24 → 1469.76] So it was a pretty
[1469.76 → 1470.44] interesting finding
[1470.44 → 1471.28] that we found
[1471.28 → 1472.02] that we were able
[1472.02 → 1473.72] to scale up
[1473.72 → 1474.64] the training batch size
[1474.64 → 1475.44] even in a game
[1475.44 → 1476.68] as simple as Pong
[1476.68 → 1477.86] all the way to the point
[1477.86 → 1478.40] where we're making
[1478.40 → 1479.04] efficient use
[1479.04 → 1480.14] of eight GPUs
[1480.14 → 1480.96] in the full machine
[1480.96 → 1481.54] and we're getting
[1481.54 → 1483.58] good linear scaling
[1483.58 → 1484.22] where you're learning
[1484.22 → 1485.24] the game basically
[1485.24 → 1486.10] eight times as fast
[1486.10 → 1487.84] when using eight GPUs.
[1488.20 → 1489.30] So I know
[1489.30 → 1489.82] at some point
[1489.82 → 1490.50] NVIDIA is working
[1490.50 → 1491.58] on some of the same problems
[1491.58 → 1493.26] as they're learning
[1493.26 → 1495.00] to get the parallelism
[1495.00 → 1496.78] of the capacity out there
[1496.78 → 1497.36] so that you can take
[1497.36 → 1498.82] advantage of all the GPUs.
[1499.72 → 1501.56] Are you still using
[1501.56 → 1503.08] the code that you wrote
[1503.08 → 1504.16] to handle that
[1504.16 → 1505.66] or have you switched over
[1505.66 → 1506.40] to some of the stuff
[1506.40 → 1507.38] that NVIDIA was producing?
[1507.54 → 1508.84] I had the same experience
[1508.84 → 1510.48] working at a prior employer
[1510.48 → 1511.68] where some of the things
[1511.68 → 1512.60] that we needed to do
[1512.60 → 1513.36] was out ahead
[1513.36 → 1514.50] of any release and stuff
[1514.50 → 1515.42] so we had a kind of
[1515.42 → 1516.04] a similar problem.
[1516.32 → 1517.32] Have you just stuck
[1517.32 → 1518.26] with the code
[1518.26 → 1518.64] that you wrote
[1518.64 → 1519.48] to accomplish that?
[1519.66 → 1520.16] Yeah, so far
[1520.16 → 1520.84] for new projects
[1520.84 → 1521.98] that I've been working on
[1521.98 → 1522.86] that aren't focused
[1522.86 → 1523.88] on scaling RL
[1523.88 → 1524.66] but doing other
[1524.66 → 1525.90] learning experiments
[1525.90 → 1526.58] yeah, exactly
[1526.58 → 1528.04] we're using the same code base
[1528.04 → 1529.28] that we established
[1529.28 → 1531.30] before during the scale up
[1531.30 → 1531.68] project
[1531.68 → 1533.08] so far the new projects
[1533.08 → 1533.74] we've been running
[1533.74 → 1535.06] it's interesting
[1535.06 → 1536.24] you end up running
[1536.24 → 1538.58] many different experiments
[1538.58 → 1541.10] in order to see
[1541.10 → 1541.88] what is working
[1541.88 → 1542.82] and what is not working
[1542.82 → 1543.98] so in the end
[1543.98 → 1545.28] an efficient way to run
[1545.28 → 1546.12] is actually to use
[1546.12 → 1547.14] only a single GPU
[1547.14 → 1548.32] but maybe stack
[1548.32 → 1549.42] multiple different experiments
[1549.42 → 1551.10] running on the same computer
[1551.10 → 1552.60] each one on a separate GPU
[1552.60 → 1554.12] and so we had kind of
[1554.12 → 1555.18] baked that into
[1555.18 → 1556.30] our code base anywhere
[1556.30 → 1557.30] where it was flexible
[1557.30 → 1558.02] you could either throw
[1558.02 → 1558.78] all eight GPUs
[1558.78 → 1559.38] at one problem
[1559.38 → 1561.28] or have each of the eight GPUs
[1561.28 → 1562.18] running a separate problem
[1562.18 → 1563.02] and you have like
[1563.02 → 1563.76] many different settings
[1563.76 → 1564.88] that you're trying to test anyway
[1564.88 → 1566.36] and so either way
[1566.36 → 1566.74] in the end
[1566.74 → 1568.54] you get a good turnaround
[1568.54 → 1568.92] of results
[1568.92 → 1569.14] Gotcha
[1569.14 → 1571.12] so now that we've kind of
[1571.12 → 1572.64] gotten up to more or less
[1572.64 → 1573.12] you know
[1573.12 → 1575.16] the more recent past
[1575.16 → 1576.08] and you're now using
[1576.08 → 1577.38] DGX1
[1577.38 → 1579.24] and you have these great tools
[1579.24 → 1580.24] available to you
[1580.24 → 1582.04] and you know
[1582.04 → 1583.48] to kind of come full circle
[1583.48 → 1584.76] back to your talk today
[1584.76 → 1587.42] as you talked about
[1587.42 → 1588.10] and I quote
[1588.10 → 1588.88] recent achievements
[1588.88 → 1589.42] in large scale
[1589.42 → 1590.30] deep reinforcement learning
[1590.30 → 1591.42] what things did you cover
[1591.42 → 1592.04] in your talk
[1592.04 → 1594.00] what kinds of things
[1594.00 → 1595.18] is useful
[1595.18 → 1596.04] so you know
[1596.04 → 1596.66] some of our listeners
[1596.66 → 1597.24] out there
[1597.24 → 1598.96] are using DGX1s
[1598.96 → 1599.82] DGX2s
[1599.82 → 1601.02] and other equipment
[1601.02 → 1601.74] from other companies
[1601.74 → 1602.22] as well
[1602.22 → 1604.56] what are the learnings
[1604.56 → 1605.10] that you found
[1605.10 → 1606.56] that are going to help us
[1606.56 → 1606.96] along there
[1606.96 → 1608.04] in terms of recent achievements
[1608.04 → 1608.82] Sure
[1608.82 → 1609.78] so most of the projects
[1609.78 → 1610.58] that I talked about
[1610.58 → 1611.98] earlier today
[1611.98 → 1614.16] were to do with
[1614.16 → 1617.26] large scale research projects
[1617.26 → 1618.26] happening at
[1618.26 → 1619.28] other organizations
[1619.28 → 1620.20] such as like
[1620.20 → 1621.08] Google DeepMind
[1621.08 → 1622.16] in London
[1622.16 → 1623.28] and OpenAI
[1623.28 → 1624.62] here in San Francisco
[1624.62 → 1625.42] some really
[1625.42 → 1626.00] really impressive
[1626.00 → 1626.70] recent achievements
[1626.70 → 1627.76] coming out of those places
[1627.76 → 1628.86] Can you share some of those
[1628.86 → 1629.64] achievements from each
[1629.64 → 1630.50] that you talked about?
[1630.72 → 1630.98] Certainly can
[1630.98 → 1631.16] yeah
[1631.16 → 1632.10] so kind of building on this
[1632.10 → 1632.72] like foundations
[1632.72 → 1633.68] that happened under
[1633.68 → 1634.92] the Atari experiments
[1634.92 → 1635.96] over the last several years
[1635.96 → 1636.96] now there's
[1636.96 → 1638.50] new results coming out
[1638.50 → 1639.46] in other domains
[1639.46 → 1640.66] to include
[1640.66 → 1641.44] Data 2
[1641.44 → 1643.04] Star Craft 2
[1643.04 → 1644.74] a version of
[1644.74 → 1645.40] Capture the Flag
[1645.40 → 1646.48] that's in an actual
[1646.48 → 1647.64] like first person action
[1647.64 → 1648.32] you know
[1648.32 → 1649.76] 3D game style
[1649.76 → 1650.12] yep
[1650.12 → 1651.56] so it's really exciting
[1651.56 → 1652.34] to see a lot of more
[1652.34 → 1652.96] like sophisticated
[1652.96 → 1654.60] video games
[1654.60 → 1655.16] that are actually
[1655.16 → 1655.60] interesting
[1655.60 → 1657.46] and still maybe
[1657.46 → 1657.94] like addictive
[1657.94 → 1658.80] for humans to play
[1658.80 → 1659.14] today
[1659.14 → 1660.22] that are now
[1660.22 → 1661.20] being tackled
[1661.20 → 1662.24] and solved
[1662.24 → 1663.68] by these learning agents
[1663.68 → 1664.06] yeah
[1664.06 → 1665.64] the Star Craft 2
[1665.64 → 1666.42] work
[1666.42 → 1667.38] really captured
[1667.38 → 1668.46] my imagination
[1668.46 → 1669.38] and those of some
[1669.38 → 1669.94] friends of mine
[1669.94 → 1671.44] we were talking about that
[1671.44 → 1672.44] just in terms of
[1672.44 → 1672.94] the
[1672.94 → 1674.64] just the
[1674.64 → 1675.96] this field
[1675.96 → 1676.16] this field is
[1676.16 → 1676.86] leaping forward
[1676.86 → 1677.42] so fast
[1677.42 → 1678.08] as you talked about
[1678.08 → 1678.36] you know
[1678.36 → 1679.44] going from Pong
[1679.44 → 1680.12] going to
[1680.12 → 1682.20] to managing games
[1682.20 → 1682.78] at that level
[1682.78 → 1684.40] with this technology
[1684.40 → 1685.22] and doing that
[1685.22 → 1686.24] what
[1686.24 → 1686.88] I guess
[1686.88 → 1688.58] tell us a little bit more
[1688.58 → 1689.20] about you know
[1689.20 → 1690.26] DeepMind and OpenAI
[1690.26 → 1691.62] and how that's influenced you
[1691.62 → 1692.90] yeah sure
[1692.90 → 1693.30] so I was
[1693.30 → 1694.38] I was fortunate enough
[1694.38 → 1695.96] to do an internship
[1695.96 → 1696.96] research internship
[1696.96 → 1697.64] at DeepMind
[1697.64 → 1699.10] over the last fall
[1699.10 → 1700.46] so I had some
[1700.46 → 1701.38] first-hand exposure
[1701.38 → 1702.92] to some of their techniques
[1702.92 → 1704.24] and their working methods
[1704.24 → 1705.50] and such
[1705.50 → 1707.36] I'm not going to say
[1707.36 → 1708.06] anything that isn't
[1708.06 → 1708.74] publicly
[1708.74 → 1709.66] of course not
[1709.66 → 1710.94] we would never
[1710.94 → 1711.90] ask you that
[1711.90 → 1713.98] so I got to be careful
[1713.98 → 1714.50] about that
[1714.50 → 1715.62] but yeah
[1715.62 → 1716.22] no it was a wonderful
[1716.22 → 1717.34] experience to see
[1717.34 → 1719.96] the whole organization
[1719.96 → 1721.52] from top to bottom
[1721.52 → 1722.70] amazing resources
[1722.70 → 1723.50] in terms of people
[1723.50 → 1724.30] amazing resources
[1724.30 → 1725.16] in terms of
[1725.16 → 1725.84] compute
[1725.84 → 1727.74] and it's no wonder
[1727.74 → 1729.10] once you're inside the door
[1729.10 → 1729.54] it's no wonder
[1729.54 → 1730.66] the amazing things
[1730.66 → 1731.26] that are coming out
[1731.26 → 1733.26] so of the things
[1733.26 → 1734.98] that are publicly known now
[1734.98 → 1736.28] what was the coolest thing
[1736.28 → 1737.34] that you experienced there
[1737.34 → 1739.36] while you were doing that
[1739.36 → 1739.96] internship
[1739.96 → 1741.62] that you can share with us
[1741.62 → 1742.84] yeah I think the thing
[1742.84 → 1744.38] that was the coolest for me
[1744.38 → 1745.96] again it was kind of
[1745.96 → 1746.74] the combination of these
[1746.74 → 1747.78] two factors I just saw
[1747.78 → 1748.62] the people
[1748.62 → 1750.00] and the compute resources
[1750.00 → 1751.04] and both of those
[1751.04 → 1751.78] organized well
[1751.78 → 1752.40] in the same place
[1752.40 → 1753.74] so I actually was sitting
[1753.74 → 1754.60] next to
[1754.60 → 1756.62] much of the Star Craft 2 team
[1756.62 → 1757.10] really
[1757.10 → 1757.82] when they were in the heat
[1757.82 → 1758.50] of their development
[1758.50 → 1759.92] last fall
[1759.92 → 1760.48] oh that's cool
[1760.48 → 1761.18] in the run-up
[1761.18 → 1763.02] to these professional matches
[1763.02 → 1764.42] and so just like
[1764.42 → 1766.44] I wasn't personally involved
[1766.44 → 1768.00] on that particular project
[1768.00 → 1769.38] but I just heard
[1769.38 → 1770.52] a lot of background chatter
[1770.52 → 1771.20] from ears
[1771.20 → 1772.06] looking over their shoulders
[1772.06 → 1773.34] saw the very intense meetings
[1773.34 → 1773.88] going on
[1773.88 → 1774.64] saw people scrambling
[1774.64 → 1776.04] to get presentations together
[1776.04 → 1776.64] for the meetings
[1776.64 → 1777.70] with their latest developments
[1777.70 → 1778.46] and learning careers
[1778.46 → 1778.82] and everything
[1778.82 → 1779.74] saw people
[1779.74 → 1780.92] debating about
[1780.92 → 1782.92] how much computer
[1782.92 → 1783.64] they were going to use
[1783.64 → 1784.44] whether they were going to
[1784.44 → 1785.36] bring down
[1785.36 → 1786.76] all Google Cloud
[1786.76 → 1787.68] or something like that
[1787.68 → 1788.38] oh wow
[1788.38 → 1791.44] that would be a bad moment
[1791.44 → 1791.70] there
[1791.70 → 1793.10] it would be a bad moment
[1793.10 → 1793.36] yeah
[1793.36 → 1794.88] so it was
[1794.88 → 1795.90] really amazing
[1795.90 → 1796.52] to see this
[1796.52 → 1798.30] great organization
[1798.30 → 1799.26] of really interested
[1799.26 → 1800.86] and generally excited
[1800.86 → 1801.44] researchers
[1801.44 → 1802.60] working together
[1802.60 → 1803.92] in this team
[1803.92 → 1804.80] environment
[1804.80 → 1805.62] that was very
[1805.62 → 1808.32] professional
[1808.32 → 1810.96] and eager
[1810.96 → 1811.40] yeah
[1811.40 → 1813.76] so what about OpenAI
[1813.76 → 1814.50] you mentioned that
[1814.50 → 1815.10] a moment ago
[1815.10 → 1816.56] what are some of the things
[1816.56 → 1817.20] that they have
[1817.20 → 1818.04] been doing
[1818.04 → 1818.86] that have inspired you
[1818.86 → 1820.14] yeah and OpenAI
[1820.14 → 1821.10] also has a very
[1821.10 → 1821.70] exciting project
[1821.70 → 1822.16] going on
[1822.16 → 1822.92] with a slightly
[1822.92 → 1824.04] different game
[1824.04 → 1825.58] Data 2
[1825.58 → 1826.88] which I think
[1826.88 → 1827.86] is even more popular
[1827.86 → 1828.40] and widespread
[1828.40 → 1830.32] than Star Craft 2
[1830.32 → 1831.90] I think I read
[1831.90 → 1832.90] something on their blog
[1832.90 → 1833.40] about maybe
[1833.40 → 1834.70] the annual winnings
[1834.70 → 1836.44] of esports contests
[1836.44 → 1836.90] in Data 2
[1836.90 → 1838.64] is like 40 million dollars
[1838.64 → 1840.20] a year or so
[1840.20 → 1840.54] wow
[1840.54 → 1841.68] yeah so this game
[1841.68 → 1841.88] is happening
[1841.88 → 1842.56] some real money there
[1842.56 → 1843.28] this game is happening
[1843.28 → 1844.06] there's real money
[1844.06 → 1847.38] and yeah
[1847.38 → 1847.90] likewise
[1847.90 → 1848.30] they have like
[1848.30 → 1849.04] a totally independent
[1849.04 → 1849.34] branch
[1849.34 → 1850.24] a very different approach
[1850.24 → 1853.42] and their own run
[1853.42 → 1855.52] to train an agent
[1855.52 → 1855.96] to play
[1855.96 → 1857.02] at a professional level
[1857.02 → 1859.06] in a very complicated
[1859.06 → 1860.18] environment
[1860.18 → 1861.58] such as these games
[1861.58 → 1862.44] so
[1862.44 → 1864.48] it sounds like
[1864.48 → 1865.84] pretty amazing experiences
[1865.84 → 1866.94] to be exposed to that
[1866.94 → 1868.68] where do you see
[1868.68 → 1869.28] yourself going
[1869.28 → 1869.94] is there stuff
[1869.94 → 1870.56] that you're working on
[1870.56 → 1871.34] now that you can share
[1871.34 → 1873.20] or things that you have
[1873.20 → 1874.18] in mind for the future
[1874.18 → 1876.00] and you know
[1876.00 → 1877.00] kind of what you
[1877.00 → 1877.96] want to do specifically
[1877.96 → 1879.50] yeah there's a couple
[1879.50 → 1880.36] of projects that I've
[1880.36 → 1881.24] been working on
[1881.24 → 1881.62] recently
[1881.62 → 1883.14] that are kind of
[1883.14 → 1885.02] I think are interesting
[1885.02 → 1886.50] one of them actually
[1886.50 → 1887.12] is
[1887.12 → 1888.88] working towards
[1888.88 → 1891.20] real world
[1891.20 → 1891.96] applications
[1891.96 → 1893.06] of reinforcement learning
[1893.06 → 1893.82] so it's very exciting
[1893.82 → 1894.44] all this development
[1894.44 → 1895.48] that is happening
[1895.48 → 1896.52] in these video games
[1896.52 → 1897.74] but obviously
[1897.74 → 1898.84] we're not developing
[1898.84 → 1899.62] reinforcement learning
[1899.62 → 1900.76] to play the games
[1900.76 → 1901.02] better
[1901.02 → 1901.40] we're
[1901.40 → 1902.74] we could be
[1902.74 → 1903.32] but we're not
[1903.32 → 1903.76] we could be
[1903.76 → 1904.20] but we're learning
[1904.20 → 1904.76] to play the games
[1904.76 → 1905.70] better to develop
[1905.70 → 1906.54] reinforcement learning
[1906.54 → 1908.20] maybe for other things
[1908.20 → 1909.40] so I think another
[1909.40 → 1910.44] really exciting result
[1910.44 → 1911.34] that came out recently
[1911.34 → 1912.46] is in
[1912.46 → 1913.96] job scheduling
[1913.96 → 1915.28] which is like
[1915.28 → 1916.62] managing parallel
[1916.62 → 1917.64] computing resources
[1917.64 → 1920.42] so I'll give a shout-out
[1920.42 → 1921.94] to another group
[1921.94 → 1922.98] Hung TSE Mao
[1922.98 → 1924.30] from MIT
[1924.30 → 1925.50] is the first author
[1925.50 → 1925.96] on a paper
[1925.96 → 1926.58] that came out
[1926.58 → 1927.14] in the fall
[1927.14 → 1928.72] to do with
[1928.72 → 1929.70] reinforcement learning
[1929.70 → 1931.88] for job scheduling
[1931.88 → 1933.40] on data clusters
[1933.40 → 1935.30] under the Apache
[1935.30 → 1936.86] Spark setup
[1936.86 → 1937.20] so
[1937.20 → 1938.56] and we'll include
[1938.56 → 1939.26] a link to that
[1939.26 → 1939.80] in the show notes
[1939.80 → 1940.16] as well
[1940.16 → 1940.82] for people to go
[1940.82 → 1941.20] reference
[1941.20 → 1941.60] great
[1941.60 → 1943.34] and yeah
[1943.34 → 1943.94] this is really
[1943.94 → 1944.90] really exciting work
[1944.90 → 1945.94] to see reinforcement
[1945.94 → 1946.54] learning applied
[1946.54 → 1947.24] to a real world
[1947.24 → 1947.90] problem like this
[1947.90 → 1948.56] scheduling hundreds
[1948.56 → 1949.12] or thousands
[1949.12 → 1950.02] of CPUs
[1950.02 → 1950.42] basically
[1950.42 → 1952.28] under diverse
[1952.28 → 1952.80] workloads
[1952.80 → 1954.70] from multiple users
[1954.70 → 1955.92] and they did
[1955.92 → 1956.60] a really nice job
[1956.60 → 1957.22] of laying out
[1957.22 → 1957.98] okay here's a couple
[1957.98 → 1959.04] of like heuristic
[1959.04 → 1959.70] job scheduling
[1959.70 → 1960.16] algorithms
[1960.16 → 1960.96] that you might have
[1960.96 → 1961.32] for you know
[1961.32 → 1961.82] for deciding
[1961.82 → 1962.66] which computing
[1962.66 → 1963.80] tasks need to run
[1963.80 → 1964.68] on which system
[1964.68 → 1965.74] which CPU
[1965.74 → 1966.54] and like when
[1966.54 → 1968.68] they have some
[1968.68 → 1970.24] really nice like
[1970.24 → 1970.58] heuristics
[1970.58 → 1971.54] that they use
[1971.54 → 1972.00] and then also
[1972.00 → 1972.86] some more advanced
[1972.86 → 1973.80] but recent
[1973.80 → 1974.58] like handcrafted
[1974.58 → 1975.00] algorithms
[1975.00 → 1976.04] and then they show
[1976.04 → 1976.72] deep reinforcement
[1976.72 → 1977.52] learning of course
[1977.52 → 1978.24] taking the cake
[1978.24 → 1978.86] and blowing them
[1978.86 → 1979.66] all out of the water
[1979.66 → 1980.82] it's a really
[1980.82 → 1981.68] beautiful thing to see
[1981.68 → 1984.90] so where do you
[1984.90 → 1985.36] think we're going
[1985.36 → 1986.76] next in terms
[1986.76 → 1987.88] of applying
[1987.88 → 1989.16] deep reinforcement
[1989.16 → 1990.90] learning to robotics
[1990.90 → 1992.64] you know this field
[1992.64 → 1993.82] both of those
[1993.82 → 1994.86] individually are moving
[1994.86 → 1995.76] so fast now
[1995.76 → 1997.12] what do you
[1997.12 → 1997.78] you know do a little
[1997.78 → 1998.94] fortune-telling for us
[1998.94 → 2000.38] and lay out
[2000.38 → 2000.94] what you think
[2000.94 → 2002.72] we're going to see
[2002.72 → 2003.98] in the near term
[2003.98 → 2005.08] maybe even longer term
[2005.08 → 2006.06] be a little speculative
[2006.06 → 2007.12] okay sure
[2007.12 → 2008.42] I mean I think
[2008.42 → 2009.08] we're already seeing
[2009.08 → 2010.10] interesting robotics
[2010.10 → 2010.98] results coming out
[2010.98 → 2011.72] of like open AI
[2011.72 → 2012.36] for instance
[2012.36 → 2014.82] they had a blog post
[2014.82 → 2015.56] recently on learning
[2015.56 → 2016.12] dexterity
[2016.12 → 2016.54] where they had
[2016.54 → 2017.28] a robotic hand
[2017.28 → 2018.12] which could manipulate
[2018.12 → 2019.68] a cube in very
[2019.68 → 2021.08] very human like
[2021.08 → 2022.66] looking ways
[2022.66 → 2024.34] trained entirely
[2024.34 → 2024.98] on reinforcement
[2024.98 → 2025.66] learning using
[2025.66 → 2026.50] basically the same
[2026.50 → 2027.40] algorithm and setup
[2027.40 → 2027.96] as they used
[2027.96 → 2028.62] for Data 2
[2028.62 → 2029.84] which is really cool
[2029.84 → 2030.40] to see this
[2030.40 → 2032.08] techniques kind of
[2032.08 → 2033.38] crossing into new
[2033.38 → 2033.86] applications
[2033.86 → 2035.46] but I think definitely
[2035.46 → 2037.50] robotics is a very
[2037.50 → 2038.52] very ripe field
[2038.52 → 2039.70] for application
[2039.70 → 2040.92] where obviously
[2040.92 → 2041.50] there's so many
[2041.50 → 2042.62] things that could
[2042.62 → 2043.14] be enabled
[2043.14 → 2044.52] where not only
[2044.52 → 2045.00] is the hardware
[2045.00 → 2045.74] getting there
[2045.74 → 2047.02] and in place
[2047.02 → 2048.14] but man it's
[2048.14 → 2048.94] really hard to
[2048.94 → 2049.90] it's just really
[2049.90 → 2050.64] hard to hand
[2050.64 → 2051.22] program these
[2051.22 → 2052.64] things to do
[2052.64 → 2054.20] interesting activities
[2054.20 → 2055.32] in new environments
[2055.32 → 2055.86] and new places
[2055.86 → 2056.30] that they haven't
[2056.30 → 2056.74] seen before
[2056.74 → 2058.34] and learning is
[2058.34 → 2059.06] definitely going
[2059.06 → 2059.66] to be the way
[2059.66 → 2060.94] to get behaviours
[2060.94 → 2061.48] out of robots
[2061.48 → 2062.28] that generalize
[2062.28 → 2062.98] to new scenarios
[2062.98 → 2063.72] that will let them
[2063.72 → 2064.66] roam free in the
[2064.66 → 2065.50] world and be
[2065.50 → 2067.30] useful and safe
[2067.30 → 2070.84] so do you dare
[2070.84 → 2071.56] to put any
[2071.56 → 2072.80] time frames around
[2072.80 → 2073.58] when we'll see
[2073.58 → 2074.46] different levels
[2074.46 → 2075.26] of that out there
[2075.26 → 2077.14] or am I getting
[2077.14 → 2077.90] too out there
[2077.90 → 2080.48] the look on his
[2080.48 → 2081.12] face by the way
[2081.12 → 2081.76] you can't see it
[2081.76 → 2082.34] listening to this
[2082.34 → 2083.34] but he was like
[2083.34 → 2084.10] oh god I just
[2084.10 → 2085.72] poured gas
[2085.72 → 2086.24] on the fire
[2086.24 → 2086.64] right there
[2086.64 → 2087.76] maybe what we
[2087.76 → 2088.16] can do is
[2088.16 → 2088.82] I'll just record
[2088.82 → 2089.42] 5 years
[2089.42 → 2090.34] 10 years
[2090.34 → 2091.18] 15 years
[2091.18 → 2091.62] and then we can
[2091.62 → 2092.14] go back later
[2092.14 → 2092.60] depending on
[2092.60 → 2093.08] which one was
[2093.08 → 2093.28] right
[2093.28 → 2093.74] there you go
[2093.74 → 2094.74] how about that
[2094.74 → 2095.30] fair enough
[2095.30 → 2096.20] I had to try
[2096.20 → 2096.54] there
[2096.54 → 2097.96] so a lot
[2097.96 → 2098.34] of people
[2098.34 → 2099.20] that listen
[2099.20 → 2100.88] are kind
[2100.88 → 2101.14] of getting
[2101.14 → 2101.68] into it
[2101.68 → 2102.70] we have a lot
[2102.70 → 2102.96] of people
[2102.96 → 2103.20] that are
[2103.20 → 2103.60] practitioners
[2103.60 → 2104.16] but we also
[2104.16 → 2104.46] have a lot
[2104.46 → 2104.78] of people
[2104.78 → 2105.30] out there
[2105.30 → 2106.28] that are
[2106.28 → 2107.22] in the
[2107.22 → 2108.16] technology world
[2108.16 → 2108.92] academic world
[2108.92 → 2109.62] business world
[2109.62 → 2110.52] who are trying
[2110.52 → 2111.20] to figure out
[2111.20 → 2111.56] how they're
[2111.56 → 2112.32] going to move
[2112.32 → 2113.26] into this space
[2113.26 → 2113.94] and someone
[2113.94 → 2115.02] who is
[2115.02 → 2115.94] ramped up
[2115.94 → 2116.60] done that
[2116.60 → 2117.84] understands
[2117.84 → 2118.80] what's necessary
[2118.80 → 2119.62] to be productive
[2119.62 → 2120.16] in the world
[2120.16 → 2120.90] what kind
[2120.90 → 2121.60] of advice
[2121.60 → 2122.10] do you have
[2122.10 → 2122.66] for people
[2122.66 → 2123.70] in a couple
[2123.70 → 2124.10] of different
[2124.10 → 2124.60] scenarios
[2124.60 → 2126.54] if they're
[2126.54 → 2127.72] in a business
[2127.72 → 2129.34] and they may
[2129.34 → 2130.22] have a data
[2130.22 → 2130.90] science team
[2130.90 → 2131.32] or something
[2131.32 → 2132.12] or group
[2132.12 → 2132.68] of developers
[2132.68 → 2133.00] and they're
[2133.00 → 2134.16] wanting to
[2134.16 → 2135.96] kind of
[2135.96 → 2137.14] retrain
[2137.14 → 2138.56] in reinforcement
[2138.56 → 2139.02] learning
[2139.02 → 2139.68] deep reinforcement
[2139.68 → 2140.12] learning
[2140.12 → 2140.64] and maybe
[2140.64 → 2141.26] even robotics
[2141.26 → 2141.64] that might
[2141.64 → 2142.22] be an application
[2142.22 → 2142.94] that they're
[2142.94 → 2143.54] interested in
[2143.54 → 2145.18] what would you
[2145.18 → 2145.70] first
[2145.70 → 2146.02] for that
[2146.02 → 2146.86] kind of
[2146.86 → 2147.40] personality
[2147.40 → 2148.02] out there
[2148.02 → 2148.68] in the real
[2148.68 → 2148.90] world
[2148.90 → 2149.40] so to speak
[2149.40 → 2150.68] what should
[2150.68 → 2151.14] they be thinking
[2151.14 → 2151.38] about
[2151.38 → 2151.76] how should
[2151.76 → 2152.08] they start
[2152.08 → 2152.48] making a
[2152.48 → 2152.94] transition
[2152.94 → 2153.76] to take
[2153.76 → 2154.10] advantage
[2154.10 → 2154.36] of these
[2154.36 → 2154.84] technologies
[2154.84 → 2155.20] at this
[2155.20 → 2155.40] point
[2155.40 → 2156.54] yeah I think
[2156.54 → 2157.68] one possible
[2157.68 → 2158.70] way to
[2158.70 → 2159.74] approach this
[2159.74 → 2160.68] taking on
[2160.68 → 2161.10] a new field
[2161.10 → 2161.62] like this
[2161.62 → 2162.46] that I think
[2162.46 → 2162.74] could be
[2162.74 → 2163.14] productive
[2163.14 → 2164.38] is to
[2164.38 → 2165.66] take the
[2165.66 → 2166.00] time to
[2166.00 → 2166.54] practice it
[2166.54 → 2167.28] and do it
[2167.28 → 2168.30] yourself
[2168.30 → 2168.82] so there's
[2168.82 → 2169.28] starting to be
[2169.28 → 2169.84] more and more
[2169.84 → 2170.62] implementations
[2170.62 → 2171.14] of these deep
[2171.14 → 2171.56] reinforcement
[2171.56 → 2172.56] learning algorithms
[2172.56 → 2173.36] available out
[2173.36 → 2173.98] there on the
[2173.98 → 2174.30] internet
[2174.30 → 2175.96] GitHub for instance
[2175.96 → 2176.94] I'm sure
[2176.94 → 2178.06] is full of them
[2178.06 → 2179.58] I mean I just
[2179.58 → 2180.64] released the
[2180.64 → 2181.32] code for
[2181.32 → 2181.80] Excel
[2181.80 → 2182.46] Excel RL
[2182.46 → 2183.00] my project
[2183.00 → 2183.42] for scaling
[2183.42 → 2183.76] up on the
[2183.76 → 2184.28] DGX one
[2184.28 → 2185.06] is now out
[2185.06 → 2186.30] on GitHub
[2186.30 → 2186.88] and of course
[2186.88 → 2187.74] we'll add a link
[2187.74 → 2188.08] to that
[2188.08 → 2188.60] into the show
[2188.60 → 2189.06] notes there
[2189.06 → 2189.70] okay so this
[2189.70 → 2190.08] is this one
[2190.08 → 2190.76] such example
[2190.76 → 2191.96] but really
[2191.96 → 2192.42] taking the
[2192.42 → 2193.04] time to
[2193.04 → 2194.32] okay you know
[2194.32 → 2195.16] read off of
[2195.16 → 2195.60] those but
[2195.60 → 2196.26] implement it
[2196.26 → 2196.62] yourself
[2196.62 → 2197.60] make yourself
[2197.60 → 2198.12] rewrite it
[2198.12 → 2198.72] from scratch
[2198.72 → 2200.58] and run it
[2200.58 → 2201.42] and get all
[2201.42 → 2201.74] the way to
[2201.74 → 2202.08] the point
[2202.08 → 2202.60] where you're
[2202.60 → 2203.22] recreating the
[2203.22 → 2203.78] learning curve
[2203.78 → 2204.86] that is
[2204.86 → 2206.10] published in
[2206.10 → 2206.50] the literature
[2206.50 → 2207.72] because a lot
[2207.72 → 2208.12] of what happens
[2208.12 → 2208.62] with this work
[2208.62 → 2209.26] is you know
[2209.26 → 2209.70] there's like
[2209.70 → 2210.54] so many
[2210.54 → 2211.52] programming concepts
[2211.52 → 2212.24] that are
[2212.24 → 2214.12] not too difficult
[2214.12 → 2214.72] to understand
[2214.72 → 2215.30] mainly and get
[2215.30 → 2215.62] in place
[2215.62 → 2215.98] but there can
[2215.98 → 2216.44] be lots of
[2216.44 → 2217.10] little bugs
[2217.10 → 2217.54] and lots of
[2217.54 → 2218.10] little gotchas
[2218.10 → 2219.24] and maybe you
[2219.24 → 2219.56] didn't tune
[2219.56 → 2220.24] this hyperparameter
[2220.24 → 2220.82] just right
[2220.82 → 2221.70] or maybe there's
[2221.70 → 2222.96] a detail that's
[2222.96 → 2223.78] a little bit
[2223.78 → 2224.40] obscured in the
[2224.40 → 2225.08] paper and maybe
[2225.08 → 2225.94] isn't revealed
[2225.94 → 2226.52] as clearly
[2226.52 → 2227.16] you know
[2227.16 → 2227.96] as could have
[2227.96 → 2228.20] been
[2228.20 → 2228.90] and so you
[2228.90 → 2229.26] need to go
[2229.26 → 2229.64] back and
[2229.64 → 2230.22] reference someone
[2230.22 → 2230.50] else's
[2230.50 → 2230.98] implementation
[2230.98 → 2231.30] to say
[2231.30 → 2231.76] oh that
[2231.76 → 2232.20] number needs
[2232.20 → 2233.48] to be 0.25
[2233.48 → 2234.14] instead of
[2234.14 → 2234.76] 1.25
[2234.76 → 2235.46] and suddenly
[2235.46 → 2236.38] it works
[2236.38 → 2236.74] now
[2236.74 → 2237.36] oh this is
[2237.36 → 2237.56] new
[2237.56 → 2238.62] so make
[2238.62 → 2239.10] yourself go
[2239.10 → 2239.52] through all
[2239.52 → 2239.96] the stages
[2239.96 → 2240.66] basically from
[2240.66 → 2241.04] scratch
[2241.04 → 2242.14] to reproducing
[2242.14 → 2242.50] the learning
[2242.50 → 2242.96] curve that
[2242.96 → 2243.46] you see
[2243.46 → 2245.04] in the literature
[2245.04 → 2245.90] and then
[2245.90 → 2246.50] you'll know
[2246.50 → 2247.08] that you're
[2247.08 → 2248.02] doing the
[2248.02 → 2248.66] full stack
[2248.66 → 2249.30] gotcha
[2249.30 → 2250.04] and I'm
[2250.04 → 2250.20] going to
[2250.20 → 2250.60] ask for
[2250.60 → 2250.96] one other
[2250.96 → 2251.44] use case
[2251.44 → 2251.82] that's
[2251.82 → 2252.46] probably
[2252.46 → 2253.02] some
[2253.02 → 2254.06] commonality
[2254.06 → 2254.48] between them
[2254.48 → 2255.38] but if
[2255.38 → 2255.98] you are
[2255.98 → 2257.18] a student
[2257.18 → 2258.60] maybe in
[2258.60 → 2259.00] high school
[2259.00 → 2259.38] now
[2259.38 → 2259.72] and you're
[2259.72 → 2260.38] looking at
[2260.38 → 2260.74] trying to
[2260.74 → 2260.98] figure out
[2260.98 → 2261.22] what you're
[2261.22 → 2261.40] going to
[2261.40 → 2261.60] do
[2261.60 → 2261.88] as you
[2261.88 → 2262.38] go into
[2262.38 → 2263.54] your first
[2263.54 → 2264.02] university
[2264.02 → 2264.66] experience
[2264.66 → 2265.12] and
[2265.12 → 2266.36] you know
[2266.36 → 2266.80] what would
[2266.80 → 2267.46] you advise
[2267.46 → 2268.50] that
[2268.50 → 2269.06] you know
[2269.06 → 2269.48] 16
[2269.48 → 2270.06] 17
[2270.06 → 2270.32] 18
[2270.32 → 2271.08] year old
[2271.08 → 2271.44] kid
[2271.44 → 2271.76] who's
[2271.76 → 2272.02] ready
[2272.02 → 2272.46] to
[2272.46 → 2273.36] say
[2273.36 → 2273.60] hey
[2273.60 → 2273.78] I
[2273.78 → 2274.02] think
[2274.02 → 2274.22] this
[2274.22 → 2274.40] might
[2274.40 → 2274.52] be
[2274.52 → 2274.70] what
[2274.70 → 2274.80] I
[2274.80 → 2274.94] want
[2274.94 → 2275.06] to
[2275.06 → 2275.32] do
[2275.32 → 2275.60] and
[2275.60 → 2275.90] they have
[2275.90 → 2276.46] the advantage
[2276.46 → 2277.32] of going
[2277.32 → 2277.60] through
[2277.60 → 2278.08] schooling
[2278.08 → 2278.78] and taking
[2278.78 → 2279.12] advantage
[2279.12 → 2280.14] they're not out there
[2280.14 → 2280.52] in the world
[2280.52 → 2280.76] yet
[2280.76 → 2281.96] what would you advise
[2281.96 → 2282.50] them to do
[2282.50 → 2283.28] what kind of track
[2283.28 → 2283.82] should they be
[2283.82 → 2284.42] thinking about
[2284.42 → 2285.72] yeah
[2285.72 → 2286.12] definitely
[2286.12 → 2286.68] taking
[2286.68 → 2287.70] as many
[2287.70 → 2288.28] of the
[2288.28 → 2289.08] computer science
[2289.08 → 2289.52] and programming
[2289.52 → 2290.24] classes as you
[2290.24 → 2290.52] can
[2290.52 → 2292.18] being a
[2292.18 → 2293.04] good programmer
[2293.04 → 2294.00] is definitely
[2294.00 → 2294.84] a plus
[2294.84 → 2295.62] in this field
[2295.62 → 2296.66] but if you're
[2296.66 → 2297.16] really trying to
[2297.16 → 2297.58] get into
[2297.58 → 2298.62] learning research
[2298.62 → 2300.18] it's
[2300.18 → 2301.04] actually
[2301.04 → 2301.82] not always
[2301.82 → 2303.16] fully necessary
[2303.16 → 2303.86] like there's
[2303.86 → 2304.44] there's a lot
[2304.44 → 2304.66] of
[2304.66 → 2306.56] things to know
[2306.56 → 2307.28] about learning
[2307.28 → 2307.94] theory
[2307.94 → 2308.68] and such
[2308.68 → 2308.96] that you can
[2308.96 → 2309.50] also get involved
[2309.50 → 2309.86] in a lot
[2309.86 → 2310.40] of mathematics
[2310.40 → 2310.80] a lot
[2310.80 → 2311.40] of statistics
[2311.40 → 2313.60] so yeah
[2313.60 → 2314.02] I would say
[2314.02 → 2314.92] try to take
[2314.92 → 2315.62] early on
[2315.62 → 2316.38] take a broad
[2316.38 → 2316.66] approach
[2316.66 → 2317.30] because a
[2317.30 → 2317.60] different
[2317.60 → 2318.48] sub area
[2318.48 → 2318.98] within
[2318.98 → 2319.94] this whole
[2319.94 → 2321.48] field of
[2321.48 → 2321.74] learning
[2321.74 → 2322.62] might grab
[2322.62 → 2323.10] your attention
[2323.10 → 2323.68] and before
[2323.68 → 2324.08] you know it
[2324.08 → 2324.70] you've gone
[2324.70 → 2325.14] a year or two
[2325.14 → 2325.54] deep into
[2325.54 → 2325.84] a certain
[2325.84 → 2326.50] subtopic
[2326.50 → 2326.90] and then you
[2326.90 → 2327.16] realize
[2327.16 → 2327.68] oh this is
[2327.68 → 2327.94] the part
[2327.94 → 2328.18] that I
[2328.18 → 2328.54] really want
[2328.54 → 2328.82] to do
[2328.82 → 2329.56] okay
[2329.56 → 2330.72] well this
[2330.72 → 2331.04] has been
[2331.04 → 2331.76] fascinating
[2331.76 → 2332.84] thank you
[2332.84 → 2333.36] so much
[2333.36 → 2333.64] for coming
[2333.64 → 2333.78] on
[2333.78 → 2334.08] I guess
[2334.08 → 2334.94] as people
[2334.94 → 2335.18] want to
[2335.18 → 2335.56] reach out
[2335.56 → 2335.94] to you
[2335.94 → 2336.82] make contact
[2336.82 → 2337.28] with you
[2337.28 → 2338.34] where are you
[2338.34 → 2338.80] on social
[2338.80 → 2339.18] media
[2339.18 → 2340.42] how do you
[2340.42 → 2340.84] like to
[2340.84 → 2341.28] interact with
[2341.28 → 2341.88] people out
[2341.88 → 2342.08] there in
[2342.08 → 2342.38] the world
[2342.38 → 2343.48] yeah sure
[2343.48 → 2343.88] that's easy
[2343.88 → 2344.40] you can find
[2344.40 → 2345.42] me either
[2345.42 → 2345.92] on Facebook
[2345.92 → 2347.12] or old
[2347.12 → 2347.52] fashioned
[2347.52 → 2348.42] email can
[2348.42 → 2348.68] do the
[2348.68 → 2348.92] trick
[2348.92 → 2349.84] as well
[2349.84 → 2350.74] and we'll
[2350.74 → 2351.30] include those
[2351.30 → 2351.78] as well
[2351.78 → 2353.46] so thank
[2353.46 → 2353.92] you very
[2353.92 → 2354.20] much
[2354.20 → 2354.58] this was
[2354.58 → 2355.02] a great
[2355.02 → 2355.54] conversation
[2355.54 → 2356.06] I really
[2356.06 → 2356.90] enjoyed it
[2356.90 → 2357.92] you really
[2357.92 → 2358.84] made the
[2358.84 → 2360.04] thought of
[2360.04 → 2360.72] getting into
[2360.72 → 2361.48] deep reinforcement
[2361.48 → 2362.24] learning accessible
[2362.24 → 2363.60], and thanks for
[2363.60 → 2363.94] doing that
[2363.94 → 2364.20] and sharing
[2364.20 → 2364.62] with us
[2364.62 → 2365.26] and I
[2365.26 → 2365.74] appreciate the
[2365.74 → 2366.02] time
[2366.02 → 2366.56] good yeah
[2366.56 → 2367.12] invite anyone
[2367.12 → 2367.68] who wants to
[2367.68 → 2368.16] to come in
[2368.16 → 2368.70] and jump
[2368.70 → 2369.06] on the field
[2369.06 → 2369.58] it's exciting
[2369.58 → 2370.00] times
[2370.00 → 2370.52] will do
[2370.52 → 2370.98] thank you
[2370.98 → 2371.40] very much
[2371.40 → 2371.92] thank you
[2371.92 → 2374.68] all right
[2374.68 → 2375.16] thank you for
[2375.16 → 2375.82] tuning into this
[2375.82 → 2376.74] episode of
[2376.74 → 2377.36] Practical AI
[2377.36 → 2378.04] if you enjoyed
[2378.04 → 2378.38] this show
[2378.38 → 2379.08] do us a favour
[2379.08 → 2379.78] go on iTunes
[2379.78 → 2380.58] give us a rating
[2380.58 → 2381.74] go in your podcast
[2381.74 → 2382.72] app and favourite it
[2382.72 → 2383.38] if you are on
[2383.38 → 2384.12] Twitter or social
[2384.12 → 2385.04] network share a link
[2385.04 → 2385.54] with a friend
[2385.54 → 2386.28] whatever you have to do
[2386.28 → 2386.94] share the show
[2386.94 → 2387.26] with a friend
[2387.26 → 2388.00] if you enjoyed it
[2388.00 → 2388.94] and bandwidth for
[2388.94 → 2390.14] changelog is provided
[2390.14 → 2390.94] by Vastly
[2390.94 → 2391.62] learn more at
[2391.62 → 2392.48] fastly.com
[2392.48 → 2393.38] and we catch our
[2393.38 → 2394.08] errors before our
[2394.08 → 2394.74] users do here at
[2394.74 → 2395.48] changelog because of
[2395.48 → 2395.88] Rollbar
[2395.88 → 2396.98] check them out at
[2396.98 → 2397.56] rollbar.com
[2397.56 → 2398.50] slash changelog
[2398.50 → 2399.66] and we're hosted
[2399.66 → 2400.64] on Linde cloud
[2400.64 → 2401.30] servers
[2401.30 → 2401.82] head to
[2401.82 → 2402.44] linode.com
[2402.44 → 2403.28] slash changelog
[2403.28 → 2403.82] check them out
[2403.82 → 2404.74] support this show
[2404.74 → 2406.16] this episode is
[2406.16 → 2407.06] hosted by Daniel
[2407.06 → 2407.76] Whiten ack and
[2407.76 → 2408.30] Chris Benson
[2408.30 → 2409.80] the music is by
[2409.80 → 2410.82] Break master Cylinder
[2410.82 → 2411.82] and you can find
[2411.82 → 2412.82] more shows just like
[2412.82 → 2413.50] this at
[2413.50 → 2414.66] changelog.com
[2414.66 → 2415.50] when you go there
[2415.50 → 2416.30] pop in your email
[2416.30 → 2416.80] address
[2416.80 → 2417.62] get our weekly
[2417.62 → 2418.50] email keeping you
[2418.50 → 2419.04] up to date with
[2419.04 → 2419.86] the news and
[2419.86 → 2420.52] podcasts for
[2420.52 → 2421.62] developers in your
[2421.62 → 2422.78] inbox every single
[2422.78 → 2423.12] week
[2423.12 → 2424.30] thanks for tuning in
[2424.30 → 2424.96] we'll see you next
[2424.96 → 2425.22] week
[2425.22 → 2435.82] winner
[2435.82 → 2436.52] chicken dinner
[2436.52 → 2437.56] you have won
[2437.56 → 2438.62] again yes
[2438.62 → 2439.56] that's why you
[2439.56 → 2440.32] listen all the way
[2440.32 → 2440.82] to the end of the
[2440.82 → 2441.68] shows because we
[2441.68 → 2442.96] give you previews of
[2442.96 → 2444.34] what's coming up and
[2444.34 → 2445.10] as you may have
[2445.10 → 2446.18] guessed we have
[2446.18 → 2447.84] another preview of
[2447.84 → 2448.52] our upcoming show
[2448.52 → 2449.48] called brain science
[2449.48 → 2450.96] this podcast is for
[2450.96 → 2451.68] the curious to
[2451.68 → 2452.52] explore the inner
[2452.52 → 2453.26] workings of the
[2453.26 → 2454.24] human brain to
[2454.24 → 2455.00] understand behaviour
[2455.00 → 2455.82] change how about
[2455.82 → 2456.76] formation mental
[2456.76 → 2457.60] health and the
[2457.60 → 2458.30] human condition
[2458.30 → 2459.38] this show is
[2459.38 → 2460.20] hosted by myself
[2460.20 → 2461.26] Adam Stachowiak
[2461.26 → 2462.00] and my good
[2462.00 → 2463.04] friend Mariel Rees
[2463.04 → 2464.16] a doctor in
[2464.16 → 2465.02] clinical psychology
[2465.02 → 2466.26] it's brain science
[2466.26 → 2466.96] applied not just
[2466.96 → 2467.46] how does the brain
[2467.46 → 2468.44] work but how do we
[2468.44 → 2469.06] apply what we know
[2469.06 → 2469.96] about the brain to
[2469.96 → 2470.82] better our lives
[2470.82 → 2471.96] here we go
[2471.96 → 2474.28] my wife and I
[2474.28 → 2474.98] we've learned this
[2474.98 → 2476.10] this concept of
[2476.10 → 2477.38] goodwill right
[2477.38 → 2478.94] yeah I can take
[2478.94 → 2480.06] your feedback or
[2480.06 → 2481.80] your criticisms in
[2481.80 → 2482.86] a different light
[2482.86 → 2484.74] if is I know
[2484.74 → 2485.32] that you have
[2485.32 → 2486.12] goodwill for me
[2486.12 → 2487.48] meaning that you're
[2487.48 → 2488.18] not trying to harm
[2488.18 → 2489.72] me that you are
[2489.72 → 2490.54] for me not against
[2490.54 → 2491.42] me and sometimes
[2491.42 → 2492.94] change as we all
[2492.94 → 2493.92] know is painful
[2493.92 → 2494.70] and can be painful
[2494.70 → 2496.28] so sometimes the
[2496.28 → 2497.52] necessary feedback
[2497.52 → 2498.30] and or criticism
[2498.30 → 2499.72] that can influence
[2499.72 → 2500.40] that change can
[2500.40 → 2501.08] also be painful
[2501.08 → 2502.26] but I can accept
[2502.26 → 2502.94] it differently if I
[2502.94 → 2504.60] know right that
[2504.60 → 2505.90] she or they or
[2505.90 → 2507.44] whoever is in the
[2507.44 → 2508.30] scenario with me
[2508.30 → 2509.70] has goodwill for me
[2509.70 → 2510.80] you know whereas if
[2510.80 → 2511.62] you know that they're
[2511.62 → 2512.40] not for you then
[2512.40 → 2513.30] you obviously take
[2513.30 → 2513.92] it a whole different
[2513.92 → 2514.66] way and that's
[2514.66 → 2516.22] that's an okay
[2516.22 → 2518.08] thing but we often
[2518.08 → 2519.04] are you know in
[2519.04 → 2519.60] relationship with
[2519.60 → 2520.80] people that are
[2520.80 → 2521.54] giving us crucial
[2521.54 → 2522.44] feedback and we
[2522.44 → 2523.10] need to have that
[2523.10 → 2524.54] kind of that lens
[2524.54 → 2524.98] like it was
[2524.98 → 2525.88] significant in our
[2525.88 → 2526.44] marriage to
[2526.44 → 2528.14] understand hey I
[2528.14 → 2528.56] know there are
[2528.56 → 2529.12] times when you give
[2529.12 → 2530.06] me feedback I am
[2530.06 → 2530.94] not happy about it
[2530.94 → 2532.92] but I know
[2532.92 → 2533.44] you have goodwill
[2533.44 → 2534.38] for me so
[2534.38 → 2536.42] I calm down I
[2536.42 → 2539.08] listen I know I
[2539.08 → 2540.36] take that in and I
[2540.36 → 2541.22] process it whatever
[2541.22 → 2542.68] but I take it in a
[2542.68 → 2543.52] different way because
[2543.52 → 2545.38] I know that she's
[2545.38 → 2545.98] for me and not
[2545.98 → 2547.78] against me yep one
[2547.78 → 2549.02] of the key things
[2549.02 → 2550.12] when it comes to
[2550.12 → 2551.64] change is a sense
[2551.64 → 2552.58] of openness and
[2552.58 → 2553.96] even relationally
[2553.96 → 2556.48] like of going I
[2556.48 → 2557.32] need to be able to
[2557.32 → 2558.98] see somehow
[2558.98 → 2559.58] somebody else
[2559.58 → 2560.40] responds or how
[2560.40 → 2561.20] they're feeling as
[2561.20 → 2562.58] based on their
[2562.58 → 2564.38] perspective of what
[2564.38 → 2564.94] they're going through
[2564.94 → 2566.54] and not just my
[2566.54 → 2567.72] perspective of their
[2567.72 → 2569.06] perspective and
[2569.06 → 2569.62] and so this
[2569.62 → 2571.22] goodwill is like I
[2571.22 → 2572.06] believe that we're
[2572.06 → 2573.76] on the same side
[2573.76 → 2574.98] and that you're not
[2574.98 → 2575.84] trying to make it
[2575.84 → 2576.80] harder for me but so
[2576.80 → 2577.94] I can understand if I
[2577.94 → 2578.72] were sitting where you
[2578.72 → 2579.56] were sitting had the
[2579.56 → 2580.36] background that you
[2580.36 → 2581.66] had why you would
[2581.66 → 2582.42] have taken it in
[2582.42 → 2584.20] that way and then I
[2584.20 → 2584.86] can provide an
[2584.86 → 2586.82] opportunity to clarify
[2586.82 → 2588.02] or create more
[2588.02 → 2589.68] connection even when
[2589.68 → 2590.58] it doesn't feel good
[2590.58 → 2592.56] and I honestly
[2592.56 → 2593.80] think this is so
[2593.80 → 2594.58] much of what's
[2594.58 → 2596.44] missing in people's
[2596.44 → 2598.28] relationships if I
[2598.28 → 2599.32] look at relational
[2599.32 → 2600.58] interactions through
[2600.58 → 2602.24] the notion of
[2602.24 → 2603.84] conditioning wherein I
[2603.84 → 2605.14] get a sort of hit of
[2605.14 → 2606.48] dopamine feel good
[2606.48 → 2607.52] feelings because I
[2607.52 → 2609.28] went to a person I
[2609.28 → 2611.06] had a conversation that
[2611.06 → 2612.42] didn't necessarily feel
[2612.42 → 2614.12] good, but there was
[2614.12 → 2615.52] openness on both
[2615.52 → 2616.74] parties to hear one
[2616.74 → 2617.76] another's perspective
[2617.76 → 2619.64] that it actually then
[2619.64 → 2621.80] reinforces like oh when
[2621.80 → 2623.54] I go, and I have this
[2623.54 → 2625.34] exchange with people I
[2625.34 → 2627.60] feel better, so now I'm
[2627.60 → 2628.68] going to go and engage
[2628.68 → 2629.64] with other people and
[2629.64 → 2631.62] get the feedback even if
[2631.62 → 2632.52] I might not like the
[2632.52 → 2634.22] feedback because now I'm
[2634.22 → 2635.66] buffered, and I'm not
[2635.66 → 2636.94] alone in this and I
[2636.94 → 2638.30] somebody else sees my
[2638.30 → 2638.72] world
[2638.72 → 2641.98] that's a preview of
[2641.98 → 2643.20] brain science if you
[2643.20 → 2643.94] love where we're going
[2643.94 → 2645.34] with this send us an
[2645.34 → 2646.62] email to get on the
[2646.62 → 2648.46] list to be notified the
[2648.46 → 2649.72] very moment this show
[2649.72 → 2651.50] gets released email us
[2651.50 → 2652.80] at editors at
[2652.80 → 2654.28] changelog.com in the
[2654.28 → 2655.14] subject line put in
[2655.14 → 2657.18] all caps brain science
[2657.18 → 2658.76] with a couple bangs if
[2658.76 → 2659.44] you're really excited
[2659.44 → 2661.10] you can also subscribe to
[2661.10 → 2662.06] our master feed to get
[2662.06 → 2663.42] all of our shows in one
[2663.42 → 2664.84] single feed head to
[2664.84 → 2666.68] changelog.com slash master
[2666.68 → 2668.36] or search in your
[2668.36 → 2669.42] podcast app for
[2669.42 → 2670.38] changelog master you'll
[2670.38 → 2671.70] find it subscribe get
[2671.70 → 2672.84] all of our shows and
[2672.84 → 2674.40] even those that only hit
[2674.40 → 2675.90] the master feed again
[2675.90 → 2677.48] changelog.com slash master
[2677.48 → 2682.84] Grindr.
[2707.48 → 2737.46] Thank you.
