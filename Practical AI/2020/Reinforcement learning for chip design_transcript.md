[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.38 --> 22.30]  Do not underestimate the power of the independent open cloud for developers.
[22.30 --> 24.58]  Yes, I'm talking about Linode.
[25.04 --> 29.38]  Linode is our cloud of choice and it's the home of Changelog.com.
[29.38 --> 34.32]  What we love most about Linode is their independence and their commitment to open cloud.
[34.74 --> 39.92]  Open cloud means being unencumbered by outside investment and maximizing value for the community,
[40.28 --> 41.12]  not shareholders.
[41.52 --> 43.16]  And that's exactly what Linode represents.
[43.54 --> 44.56]  No vendor lock-in.
[44.92 --> 46.32]  Open at every layer.
[46.72 --> 49.24]  If you want to learn more, head to linode.com slash open.
[49.24 --> 51.88]  Again, linode.com slash open.
[59.38 --> 66.08]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[66.38 --> 68.16]  productive, and accessible to everyone.
[68.60 --> 72.54]  This is where conversations around AI, machine learning, and data science happen.
[72.98 --> 77.26]  Join the community and Slack with us around various topics of the show at Changelog.com slash
[77.26 --> 78.92]  community and follow us on Twitter.
[79.06 --> 80.70]  We're at Practical AI FM.
[80.94 --> 82.42]  Okay, take it away, guys.
[82.42 --> 90.16]  Welcome to another episode of Practical AI.
[90.52 --> 92.20]  This is Daniel Whitenack.
[92.32 --> 98.50]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris,
[98.66 --> 102.08]  who is the principal AI strategist at Lockheed Martin.
[102.60 --> 103.34]  How are you doing, Chris?
[103.70 --> 104.70]  I am doing very well.
[104.76 --> 105.58]  How's it going today, Daniel?
[105.96 --> 107.14]  It's going very well.
[107.14 --> 113.32]  Well, staying very busy, as we were talking before the episode, it seems like after the
[113.32 --> 119.80]  crisis and after being everyone at home right now, so for future listeners, this is still
[119.80 --> 121.68]  during the COVID-19 crisis.
[121.90 --> 126.72]  It seems like I'm more busy work-wise now than even before.
[126.98 --> 127.54]  What about you?
[127.80 --> 130.80]  I think it's the same, and we're just trying to not be paranoid.
[131.14 --> 136.40]  We're right in the middle of pollen season, and everyone in my family suffers, so you get
[136.40 --> 140.92]  sore throats, and you're coughing, and you're like, oh my God, that's not symptomatic of
[140.92 --> 142.14]  COVID or something.
[142.26 --> 147.42]  So we're just trying to maintain our calm, get through this, and all is well.
[147.52 --> 150.22]  Other than that, it is a lovely day here in Atlanta, Georgia.
[150.68 --> 155.98]  Yeah, it's a beautiful time to get outside as well, of course, maintaining distance from
[155.98 --> 156.34]  others.
[156.82 --> 161.22]  But we've got something, I think, pretty interesting to chat about today.
[161.22 --> 169.34]  In the midst of all of the COVID-19 and coronavirus tweets and articles that I've been seeing and
[169.34 --> 174.16]  reading and all of that stuff, I was able to pick out this one story that seemed really
[174.16 --> 177.92]  interesting to me that was not related to COVID-19.
[178.24 --> 185.20]  And that was this story about a team at Google who was using reinforcement learning to somehow
[185.20 --> 189.98]  design chips like hardware computing chips.
[190.38 --> 198.30]  And we were joined today by Anna Goldie and Azalea Mir-Saini.
[198.62 --> 201.14]  You can correct me here in a second on that one.
[201.22 --> 201.86]  Sorry, Azalea.
[202.42 --> 203.62]  Welcome to the show.
[204.14 --> 205.78]  Thank you so much for having us.
[206.04 --> 207.08]  Yeah, thanks for having us.
[207.48 --> 211.88]  Yeah, excited to have you both and excited to chat about this amazing project.
[211.88 --> 213.86]  It was really interesting when I read it.
[214.26 --> 219.06]  But before we jump into the project itself, I would love to hear a little bit about both
[219.06 --> 222.78]  of your backgrounds and how you ended up doing what you're doing now.
[223.24 --> 225.36]  So maybe we could start with Azalea.
[225.50 --> 228.28]  Could you give us a little bit of information about your background?
[229.14 --> 229.50]  Yes.
[229.66 --> 233.70]  My PhD from Rice University in computer engineering.
[233.70 --> 242.18]  My thesis was focused on co-design of hardware software systems for machine learning applications.
[243.00 --> 247.58]  And then when I joined Google, I joined Google Brain to the residency program.
[247.86 --> 250.40]  I stayed at Google Brain as a resident for a year.
[250.94 --> 255.82]  And that was the time that they developed passion for the work at the intersection of
[255.82 --> 257.28]  ML for system.
[257.28 --> 263.20]  Like how do we develop new machine learning algorithm and deep learning algorithms for
[263.20 --> 263.74]  system?
[264.50 --> 271.94]  And ever since then, I've been at Google Brain for like almost four years now and enjoy doing
[271.94 --> 275.90]  research and work on impactful projects.
[276.78 --> 277.38]  Awesome.
[277.58 --> 280.74]  And now you're a senior research scientist at Google Brain.
[280.82 --> 281.28]  Is that correct?
[281.66 --> 282.52]  That's correct.
[282.62 --> 282.84]  Yes.
[283.42 --> 283.84]  Awesome.
[284.22 --> 285.54]  Well, thank you for the background.
[285.54 --> 290.22]  Anna, do you want to give us a little bit of information about your background as well?
[291.14 --> 291.72]  Yeah, sure.
[292.32 --> 296.38]  So I studied computer science and linguistics actually at MIT.
[296.90 --> 301.06]  And I did my master's basically building a Mandarin speaking dialogue system.
[301.50 --> 305.42]  I joined Google about eight years ago, Google Research.
[306.04 --> 311.60]  And I've been working mostly before this on like natural language processing applications.
[311.60 --> 315.58]  And about like two and a half, three years ago, I started working with Azalea.
[316.24 --> 320.72]  I actually saw some parallels to natural language processing in some of these systems problems,
[320.72 --> 324.84]  because a lot of them can be formulated as sequential decision making problems.
[325.48 --> 328.20]  And it's been just wonderful working with Azalea.
[328.38 --> 334.50]  And we have such an awesome team solving, basically trying to use machine learning to optimize and automate
[334.50 --> 336.18]  various problems in computer systems.
[336.18 --> 341.92]  So could you give us a little bit more of an idea about this team and how big it is?
[342.00 --> 347.48]  I know you both work closely together, but what's the sort of team like that you're working on?
[347.96 --> 350.70]  Actually, when we first started, it was basically just me and Azalea.
[351.08 --> 353.00]  And then we've been gradually growing.
[353.50 --> 358.26]  I think we have something like maybe eight, ten people on the research side.
[358.30 --> 362.68]  And then we also partner with chip designers who are building the next generation of TPUs.
[362.68 --> 365.30]  And maybe there's about eight, ten people on that side as well.
[365.42 --> 367.80]  So it's, you know, pretty substantial effort at this point.
[368.38 --> 371.90]  So kind of wondering, you know, I come from a software only background.
[372.36 --> 375.88]  And as we kind of dive in, you know, I'll probably be more comfortable in the reinforcement learning
[375.88 --> 379.32]  part, but I know nothing about creating chips and stuff.
[379.42 --> 385.50]  And I guess if you could just kind of lay out the context of what that means, what does it mean?
[385.62 --> 390.04]  I've heard the phrase chip placement and I've heard chip floor planning and stuff like that.
[390.04 --> 394.06]  Could you talk a little bit about the baseline, about what it is you're trying to do and how
[394.06 --> 398.26]  that is, what the context of it from the hardware side, which I know nothing about?
[400.02 --> 400.42]  Sure.
[400.72 --> 402.26]  Maybe I can take a stab at that.
[403.08 --> 405.84]  So basically, this is just one of the stages of chip design.
[406.74 --> 412.00]  There's already been a bunch, basically computer architecture stage and synthesis occurs first.
[412.00 --> 417.14]  But the problem that we were solving in our research was taking a graph of chip components,
[417.36 --> 418.38]  which is called a net list.
[418.86 --> 423.38]  So it's basically a bunch of SRAMs, which are memory components, macros, and standard
[423.38 --> 425.68]  cells, which are logic gates like NANDs and NORs.
[426.06 --> 427.48]  All of these are connected by wires.
[427.62 --> 428.26]  And so it's a graph.
[428.62 --> 434.74]  And we want to place that graph onto this two-dimensional grid such that we minimize various costs like
[434.74 --> 439.78]  latency of computation, power consumption, wire length area, while adhering to hard constraints
[439.78 --> 441.52]  on density and congestion.
[442.18 --> 445.26]  So that's sort of the core problem that we're trying to solve.
[445.96 --> 446.74]  So do I have it right?
[446.94 --> 452.24]  Like when you say that this is kind of graph structured, you're meaning like there's this
[452.24 --> 456.10]  component, like something physical that has to go on the chip.
[456.24 --> 458.54]  And then there's this other components.
[459.04 --> 463.92]  And they need to be linked by an electrical connection, I guess.
[464.06 --> 464.32]  Exactly.
[464.32 --> 465.34]  Is that like a way of saying it?
[465.34 --> 469.38]  So like the graph is formed of these components and the electrical connections between them.
[469.38 --> 470.58]  Is that kind of...
[470.58 --> 471.00]  Exactly.
[471.22 --> 471.42]  Yeah.
[471.48 --> 474.96]  There's all these like sort of logic and memory components connected by wires or like
[474.96 --> 476.12]  electrical connections.
[476.50 --> 480.72]  And then we physically need to decide where to place them so that we get better performance
[480.72 --> 481.86]  for that chip.
[482.54 --> 482.78]  Gotcha.
[483.42 --> 487.24]  And can you talk a little bit about what that means when you talk about why does physical
[487.24 --> 492.26]  placement have an impact on performance and what it is about that placement which affects
[492.26 --> 492.80]  performance?
[492.80 --> 499.22]  So one way you could think about it is the timing of computation or the amount of time
[499.22 --> 504.30]  it takes to compute with this circuit is affected by like the lengths of critical paths in this
[504.30 --> 505.60]  graph, this placed graph.
[506.00 --> 510.60]  So if the total wirelines connecting these components is larger, then it's going to tend to be slower.
[510.84 --> 512.18]  It's going to consume more power.
[512.96 --> 514.00]  That sort of thing.
[514.84 --> 515.16]  Gotcha.
[515.16 --> 524.38]  And how big of a graph, like how many things are we needing to like place and optimize in
[524.38 --> 525.12]  general?
[526.46 --> 529.02]  So it's millions, like millions of standard cells.
[529.24 --> 532.68]  And then in a chip, there's typically many, many blocks.
[532.68 --> 536.00]  So hundreds of millions in total of components that you're placing.
[537.08 --> 537.34]  Gotcha.
[537.34 --> 537.38]  Gotcha.
[537.90 --> 544.46]  So Azalea, I'd love to get some context in terms of like, how has this kind of been this
[544.46 --> 549.04]  problem of figuring out the placement of all of these components of the graph?
[549.28 --> 552.00]  How has this been approached in the past?
[552.00 --> 557.46]  And what are the bottlenecks or problems in terms of creating a solution to this?
[558.50 --> 562.10]  Well, there are several approaches to this problem in the past.
[562.10 --> 570.90]  In fact, since 1960s, research in both academic community and industry started on doing the
[570.90 --> 573.64]  physical design or placement optimization.
[574.26 --> 575.42]  There are various approaches.
[575.66 --> 577.84]  For example, there are quantitative approaches.
[578.60 --> 585.22]  There are approaches based on greedy methods or simulated annealing or hill climbing approaches,
[585.40 --> 587.00]  genetic algorithms and such.
[587.00 --> 595.48]  I would say the way we came in and the way we basically deep learning and reinforcement learning
[595.48 --> 602.48]  is helping us taking a new stab at this problem is that for the first time, we can like learn
[602.48 --> 607.32]  the context of the problem and learn from experience.
[607.48 --> 614.54]  Meaning we think, unlike all of the previous approaches, what we are doing is training agents
[614.54 --> 616.64]  that can accumulate experience.
[616.64 --> 623.06]  And as they're optimizing more chips, they become better at placing new chips.
[623.58 --> 627.70]  This is an approach that's different from all the previous existing methods.
[628.30 --> 628.38]  Gotcha.
[628.52 --> 633.80]  And for those who may not be very familiar with reinforcement learning as a technique, before
[633.80 --> 638.74]  we kind of dive into how you're using it in this, could you take a moment and kind of give
[638.74 --> 643.14]  listeners, either one of you, whoever would be, or both of you, kind of what is reinforcement
[643.14 --> 650.16]  learning and why is that in particular a technique which lends itself, but even kind of starting
[650.16 --> 654.36]  with just the quick run through the fundamentals of what is it if you're not familiar with it?
[654.82 --> 660.36]  So basically, it's a way in normal, like machine learning or supervised learning, you're
[660.36 --> 662.72]  trying to fit labels to input examples.
[663.48 --> 666.52]  In this case, you have this additional power, I guess.
[666.60 --> 670.68]  You can take actions in the world and then you receive feedback from your environment.
[670.68 --> 676.76]  And then you use that information to try to optimize the parameters of your own policy,
[676.86 --> 679.18]  which is generating these decisions to do better over time.
[679.62 --> 683.28]  So basically, it's composed of states, which is sort of the state of the world at a given
[683.28 --> 684.58]  moment in time.
[684.68 --> 689.80]  So for us, replacing these chips, the nodes of this graph one at a time onto the chip.
[690.14 --> 693.06]  So the state is kind of what is the placement so far?
[693.06 --> 699.36]  And then actions are decisions that you make at each point in time, which is for us, like
[699.36 --> 700.70]  where to place the next node.
[701.00 --> 705.70]  And then reward is the sort of final key component for reinforcement learning.
[706.28 --> 708.06]  It's the feedback that we get from our environment.
[708.32 --> 716.20]  So in our case, after we place all the nodes, we have approximate signals on wire length congestion
[716.20 --> 717.70]  and now timing.
[718.30 --> 723.38]  And we use a weighted average of these to tell our policy how well it did.
[723.98 --> 727.08]  And so it can update itself and generate better placements over time.
[728.52 --> 733.44]  So I know a lot of people might have kind of heard about reinforcement learning, maybe with
[733.44 --> 738.94]  like agents that play Atari games or maybe more so in like robotics.
[738.94 --> 746.40]  In those types of scenarios, you have this agent, which, you know, may be composed of one or
[746.40 --> 746.96]  more models.
[747.54 --> 753.84]  And it's trying to take actions like, you know, people like tend to maybe associate that with
[753.84 --> 759.10]  like taking actions in the video game or like moving the arm of your robot or something like
[759.10 --> 759.36]  that.
[759.50 --> 765.56]  In this case, like the quote unquote game you're playing is really the placement of these components,
[765.78 --> 765.98]  right?
[765.98 --> 774.24]  So you're kind of your agent is placing components and then getting feedback about how well it's
[774.24 --> 775.56]  placing those components.
[775.94 --> 777.70]  Is that a good way to put it?
[777.96 --> 778.66]  Yeah, that's great.
[778.72 --> 779.40]  Yes, exactly.
[780.30 --> 781.28]  Okay, great.
[781.72 --> 787.68]  So in doing this, I'm kind of curious, like, I don't know if anyone's tried to do this before.
[787.82 --> 791.82]  I assume maybe not in terms of reinforcement learning for this problem.
[791.82 --> 798.32]  How did you come to decide that reinforcement learning might be a good approach in this scenario
[798.32 --> 801.84]  versus maybe some other methodologies?
[802.30 --> 806.42]  How did you kind of come to the point where you say, oh, those things that people are doing
[806.42 --> 810.52]  in robotics or in these games or something else?
[810.64 --> 816.16]  How did you come to think that those methods, specifically reinforcement learning, might be
[816.16 --> 817.18]  suitable here?
[817.18 --> 823.20]  So before we started this project, we have been working on another project, which was doing
[823.20 --> 827.56]  device placement optimization with reinforcement learning.
[827.56 --> 835.48]  So that project had to do with taking a computational graph, such as a machine learning, like TensorFlow
[835.48 --> 842.92]  graph, and mapping it optimally to the hardware devices, such as GPUs or TPUs, such that the
[842.92 --> 848.08]  runtime or performance of the underlying ML algorithm becomes as fast as possible.
[848.58 --> 854.06]  So that problem was a combinatorial optimization problem and a very complex task.
[854.06 --> 861.68]  And started thinking about how ML and this context of our learning can help doing that optimization
[861.68 --> 863.96]  problem better than existing ones.
[864.76 --> 871.56]  And reinforcement learning is really like a natural thing to come in mind if we think about
[871.56 --> 874.24]  ML because this task is not a supervised task.
[874.32 --> 875.58]  We don't have labels for it.
[876.00 --> 881.70]  We want to optimize this problem by doing several rounds of exploration, exploitations.
[881.70 --> 886.30]  So we did reinforcement learning for that, and we got a lot of interesting, very encouraging
[886.30 --> 889.30]  results on the device placement tasks.
[889.70 --> 896.44]  So then we came to a natural next step for us to try, okay, now what if we tried the same
[896.44 --> 904.68]  kind of approaches for the chip placement problem, which is a much more complex problem than device
[904.68 --> 905.10]  placement.
[905.10 --> 909.54]  So that was the transition for us from devices to chips.
[909.70 --> 914.64]  But the interesting thing was that chip placement, when we came to it, we realized it's a way,
[914.80 --> 918.64]  like orders of magnitude, more complex problem than device placement.
[919.22 --> 925.50]  So it was very unclear to us in the beginning that we are going to get gains with reinforcement
[925.50 --> 926.10]  learning.
[926.10 --> 933.44]  For this problem that has been, there's so much research on it already, but after some trial and error and
[933.44 --> 940.74]  several rounds of improving our algorithms, it seems like it actually is helping a lot in this problem as well.
[940.74 --> 947.86]  What's up?
[947.94 --> 953.18]  This is Daniel Whitenack, one of your Practical AI co-hosts, and I hope you're enjoying this episode
[953.18 --> 955.68]  and staying healthy during these crazy times.
[956.18 --> 961.84]  I'm working on some pretty cool AI stuff here from my home office, but I've also found that I'm having
[961.84 --> 967.86]  to get a bit creative and be intentional when it comes to honing my AI skills and virtually connecting
[967.86 --> 973.50]  with the AI community. If you're in a similar situation or you've been inspired by the practical AI
[973.50 --> 980.02]  we talk about on this show, I want to invite you to a live online AI training event I'm hosting this May
[980.02 --> 981.48]  called AI Classroom.
[982.06 --> 987.42]  In AI Classroom, I'm going to teach you the practical skills I've learned over the years using the latest
[987.42 --> 989.30]  open source AI technology.
[989.90 --> 995.46]  You'll learn AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[995.46 --> 1002.46]  And after the training, you'll be able to understand the latest AI models, implement your own models in code,
[1002.92 --> 1009.26]  train computer vision and NLP models, create model inference servers, and experiment with state-of-the-art
[1009.26 --> 1011.06]  methods like reinforcement learning.
[1011.74 --> 1014.12]  AI Classroom is taking place this May.
[1014.50 --> 1021.10]  It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[1021.10 --> 1026.32]  There'll also be two cohorts with convenient time zones for eastern and western hemispheres.
[1026.86 --> 1032.06]  Don't miss out. Tickets and more information are available at datadan.io.
[1032.58 --> 1034.34]  That's datadan.io.
[1034.84 --> 1040.38]  And practical AI listeners can use the code practicalAI10 for 10% off.
[1040.64 --> 1042.70]  See you online in AI Classroom.
[1042.70 --> 1054.48]  So I am curious.
[1054.60 --> 1058.94]  You mentioned a moment ago that there was, you know, like the data itself wasn't labeled,
[1059.08 --> 1065.04]  lack of labels, and, you know, that reinforcement learning seemed like a very good technique to lend.
[1065.04 --> 1071.36]  And I am curious, if you had not gone down this route, or maybe, you know, you know, not machine learning at all,
[1071.42 --> 1074.98]  what some of the other options, whether they be in the realm of machine learning or not,
[1075.00 --> 1080.60]  might have been just to have a sense of what kind of the technique opportunity cost would have been.
[1080.80 --> 1084.12]  You know, how might others have done it had you not gone down this path?
[1085.18 --> 1087.38]  So we did experiment with some other techniques.
[1087.50 --> 1089.08]  They say evolutionary strategies.
[1089.08 --> 1091.06]  They tend to be less sample efficient.
[1091.34 --> 1095.84]  So it didn't really seem like too promising a path to go farther down.
[1096.64 --> 1103.94]  We also experiment with, like, using supervised learning as a way to basically ground our architecture search.
[1104.54 --> 1112.68]  The policy that architecture that we were able to achieve generalization with was tuned using a supervised learning objective.
[1112.68 --> 1121.76]  And then we use that as sort of the encoding stage of our full policy value net and achieve better generalization results.
[1122.56 --> 1126.14]  Yeah, I would love to follow up on a couple of those things.
[1126.44 --> 1131.32]  So, like, maybe digging into a couple of those pieces just to break it down for listeners.
[1131.62 --> 1138.78]  So when you're talking about this encoding piece and the supervised stage that you did complete,
[1138.78 --> 1146.54]  does that have to do with getting the graph structure data into, like, into another form,
[1146.66 --> 1151.40]  like a sort of embedding or representation that you would use in other things?
[1151.54 --> 1153.18]  Could you kind of describe that a little bit more?
[1153.94 --> 1154.56]  Yeah, sure.
[1155.16 --> 1160.50]  So I think basically in order to achieve generalization, it really, really is about the representation.
[1160.82 --> 1164.88]  Like, as you said, what is the correct embedding for a given input graph?
[1164.88 --> 1173.10]  So basically, we created this very large data set of different placements generated by different placement techniques,
[1173.44 --> 1180.70]  including reinforcement learning policies, but also, like, force-directed methods, simulated annealing, greedy methods.
[1181.26 --> 1190.50]  And we used that to try different architectures on the task of predicting the approximate wire lanes and congestion for those placements.
[1190.50 --> 1203.38]  And the architectures that were better at this prediction task did a much better job of creating policies that were able to generalize across different chip netlists,
[1203.50 --> 1205.92]  because they presumably had a better representation.
[1206.46 --> 1207.02]  I am curious.
[1207.20 --> 1215.30]  You mentioned a little while ago that the thing that inspired you guys to kind of go down this particular path was device placement optimization.
[1215.30 --> 1226.46]  I would imagine, and correct me if I'm wrong, I would imagine that this is like a completely different scale in the sense of, you know, working in very, very small spaces, I would imagine,
[1226.54 --> 1230.00]  compared to the original device placement optimization you were doing.
[1230.36 --> 1236.30]  If that's accurate, did the scale, you know, moving down to such small spaces make a difference?
[1236.30 --> 1238.48]  Or was it fundamentally the same?
[1238.82 --> 1242.80]  Did the approach hold up the same as you had experienced in the prior project?
[1243.08 --> 1244.82]  Azalea, do you have any thoughts on that one?
[1245.30 --> 1246.30]  Azalea, do you have any thoughts on that one?
[1246.30 --> 1246.80]  Yes.
[1246.80 --> 1247.30]  Yes.
[1247.30 --> 1251.80]  So, in both projects, we are still like doing reinforcement learning.
[1251.80 --> 1256.38]  So, the meta approach still remains the same.
[1256.38 --> 1260.64]  But, like you said, the scale of these two problems are very different.
[1260.64 --> 1263.46]  For example, in device placement, we have like a dozen.
[1263.46 --> 1271.60]  Our action space is like tens of devices or less or a few devices, a few GPUs, CPUs.
[1271.60 --> 1279.70]  But here, our action space is the placement or cells of the canvas onto which we are placing the chip.
[1280.40 --> 1285.36]  And this canvas can have thousands or even more of locations.
[1285.36 --> 1290.38]  So, our action space is orders of magnitude larger than the previous problem.
[1290.38 --> 1299.52]  At the same time, our input state, which is the graph that we are processing, a chip graph, like Anna mentioned, can have millions of nodes.
[1299.78 --> 1304.22]  Whereas a computational graph could have like tens of thousands or so.
[1304.22 --> 1311.12]  So, here in this problem, we were dealing with a much more complex state and action space.
[1311.12 --> 1322.74]  And to enable RL agents that can optimize this problem, we had to do several changes to the way that we present the environment to the agent.
[1322.74 --> 1329.92]  For example, we had to kind of take a hierarchical approach to the way we represent the input graph.
[1329.92 --> 1334.00]  So, for example, we grouped certain standard cells.
[1334.18 --> 1340.98]  We break down the complexity of the input state to a graph with like thousands of nodes that we were later on placing.
[1341.48 --> 1345.68]  And on the representation learning, we had to do a lot more work.
[1345.80 --> 1350.18]  Because in this problem, not only were we interested in placing one chip,
[1350.18 --> 1356.20]  we were also interested in creating agents that become better at placing unseen chips.
[1356.20 --> 1360.38]  Because that opens new opportunities for chip design optimization.
[1360.38 --> 1367.62]  If we can quickly, given a chip block, can place it, optimize it, and see how well we are doing in it.
[1367.92 --> 1377.60]  So, this generalization property that we wanted from this problem led us to really heavily focus on representation learning of the graph.
[1377.60 --> 1386.16]  And we created a lot of new techniques for creating these generalized representations that we are hoping in future problems,
[1386.38 --> 1396.56]  better in other stacks of chip design or other kind of hard ML for combinator optimization that we are dealing with can help us do better in those problems as well.
[1397.12 --> 1398.56]  So, I'm really curious.
[1399.28 --> 1400.66]  I have a follow-up from that.
[1400.66 --> 1414.58]  And as you were talking, I was thinking about how essentially you have all of these different possible arrangements of the graph onto the physical canvas, like you said.
[1414.80 --> 1420.78]  But also in this problem, as you're placing components, there is this like sequential nature to it.
[1420.84 --> 1427.56]  And maybe this is where I think it was mentioned earlier that there were kind of even some parallels with natural language processing.
[1427.56 --> 1436.22]  And I was wondering how you deal with this situation where you're really not just taking like a one, at least in my understanding,
[1436.34 --> 1443.82]  you're not taking a one-step approach of like, here's all my components and then here's my prediction for the placement of all of those components.
[1443.82 --> 1450.96]  You're kind of placing one component and then placing another and then placing another kind of in a more iterative sort of way.
[1450.96 --> 1456.02]  So, is that the, how do you deal with that sequential nature of this process?
[1456.36 --> 1471.00]  And does it involve kind of like subgraphs within the graph and then adding a component to that and kind of taking the last so many components and then trying to figure out how the next component comes in?
[1471.06 --> 1474.80]  Kind of like placing characters or placing words when you're doing text generation.
[1474.98 --> 1477.96]  How does that sort of sequential thing come in?
[1477.96 --> 1486.08]  So, the first architecture that we had that worked well, like we would actually pass images of the placement so far.
[1486.64 --> 1490.50]  And so, the model is kind of like a human designer as they're maybe placing a graph.
[1490.58 --> 1494.10]  They could see, you know, what space is left on the canvas and such.
[1494.54 --> 1498.48]  And we had basically an LSTM model for the policy head.
[1499.02 --> 1507.68]  Basically, that sort of stores information about the full like sequence of placement decisions that have been made up to that point.
[1508.50 --> 1517.00]  But in the end, actually, I think our current policy head is a deconvolutional neural net that predicts a policy decision over this two-dimensional grid.
[1517.72 --> 1518.44]  And I'm kind of curious.
[1518.72 --> 1520.90]  I'm also following up on the same thing, actually.
[1521.44 --> 1523.96]  And you may be starting to address that there.
[1523.96 --> 1524.68]  But I was kind of curious.
[1524.74 --> 1530.78]  You mentioned when you were talking about representation learning of the graph that there were some new techniques that you got into.
[1530.96 --> 1532.18]  And you made the comment.
[1532.34 --> 1537.10]  And then I was wondering, is there anything else that you kind of learned to apply to this?
[1537.20 --> 1538.64]  Or did you just cover it right there?
[1538.64 --> 1546.12]  So I think Azalia was getting at this graph embeddings that were developed for this project.
[1546.12 --> 1556.16]  And I think at a high level, the insight there was that for most like sort of graph convolutional neural net type applications, it's really about the features of the nodes themselves.
[1556.80 --> 1561.96]  And so you kind of represent nodes as some kind of average or other aggregation of their neighbor's features.
[1562.34 --> 1566.36]  But in our case, what really matters is the connections between these nodes.
[1566.72 --> 1567.76]  Yet it's about the past.
[1568.30 --> 1571.76]  And so our graph embeddings are much more focused on edge features.
[1571.76 --> 1577.42]  And kind of diving a little bit more into those embeddings.
[1577.80 --> 1582.22]  Again, I'm trying to make connections with maybe things that I've seen or heard about before.
[1582.36 --> 1587.78]  I know in like the NLP world with like, you know, these newer language models that are coming out.
[1588.02 --> 1591.24]  And the word embeddings that they're generating.
[1591.50 --> 1599.98]  The thought is like, oh, we're going to train this model or learn this representation based on one or more tasks.
[1599.98 --> 1603.98]  Like, you know, replacing missing words or something like that.
[1603.98 --> 1612.14]  And then you learn this embedding and then kind of apply maybe some new layers onto the network to do a particular task.
[1612.14 --> 1614.48]  Like question answering or whatever it is.
[1614.88 --> 1627.08]  Here is it similar in that you were talking about how you use some supervised learning to train the embeddings in my understanding.
[1627.08 --> 1633.14]  So you have these certain tasks that are supervised and you learn the graph embeddings.
[1633.34 --> 1637.36]  And then you were able to apply those in a new scenario.
[1637.78 --> 1640.72]  Is that the strategy or do I have that wrong?
[1641.44 --> 1642.56]  Yeah, that's very much right.
[1642.72 --> 1643.72]  Yes, that's correct.
[1643.72 --> 1661.22]  So I think the way we can describe this is that we trained architectures to capture the representation or encode the embedding of the input by having a supervised model that with very easy to produce labels.
[1661.42 --> 1662.92]  We call them pseudo labels, right?
[1663.16 --> 1670.80]  Those labels were our proxy costs for the optimization that were very fast and not at all expensive to generate.
[1670.80 --> 1689.80]  So the motivation for us to train architecture this way was if our agent, our policy is to generalize to unseen graphs, it should also have a good understanding of predicting what the actual reward is for a given state.
[1689.80 --> 1691.80]  Like unless it can.
[1692.66 --> 1701.80]  So that's like a prerequisite for generalizing policies to unseen graph is to have an idea of how good a current state is.
[1701.80 --> 1710.26]  And that's what made us do the supervised approach first, where we predict these pseudo labels for a given graph.
[1710.56 --> 1726.38]  And once the architecture is tuned in a way that this prediction task is done at a high accuracy for the test set, then we take that and use that as the encoder part of the policy for further optimization of placement.
[1726.38 --> 1726.82]  Awesome.
[1726.82 --> 1727.18]  Awesome.
[1727.18 --> 1727.74]  Awesome.
[1727.74 --> 1727.86]  Awesome.
[1727.86 --> 1727.98]  Awesome.
[1727.98 --> 1738.46]  This is really interesting because we've brought up graph neural networks a couple times on the show, but maybe not in the sort of applied way that we're talking about them here.
[1738.46 --> 1752.00]  I was wondering if you could just before we get too much further, just mention like what makes like a graph neural network, a graph neural network instead of just like a normal neural network, I guess.
[1752.00 --> 1763.14]  And maybe like help clarify for people, because even in this episode in our conversation, we mentioned like computational graph, which people might, that might come to people's mind.
[1763.28 --> 1767.92]  If they're thinking about TensorFlow, there's like this computational graph in the background.
[1767.92 --> 1775.32]  But here, like for a graph neural network, we're not talking necessarily about the computational graph.
[1775.42 --> 1778.08]  What makes the graph neural network a graph neural network?
[1778.16 --> 1783.28]  Is it just the input data and this sort of way of representing graph data?
[1783.86 --> 1791.18]  So what makes graph neural nets graph neural nets is what the way they encode information.
[1791.18 --> 1807.68]  So in a typical graph neural nets, we are learning representations of the nodes of a graph with respect to the properties of this node and the properties of its neighbor nodes and the neighbor of the neighbors and so on.
[1808.22 --> 1818.40]  So graph neural nets have this property that they can encode information about the one hub, two hub, like K hub adjacency information of a node.
[1818.40 --> 1826.72]  And you can also, on top of this adjacency information, like the connectivity graph, you can also add features per node.
[1827.24 --> 1833.58]  And you can also, in our case, you can add features per edge of the graph.
[1834.20 --> 1846.84]  So basically, graph neurons are allowing us to capture all of this information about the graph structure of an input data and generate embeddings of the nodes and edges
[1846.84 --> 1852.60]  that kind of relate and can capture those graph structure and graph information.
[1853.54 --> 1858.24]  So, you know, having gone through this, which is fascinating, it's entirely new to me.
[1858.44 --> 1862.68]  I'm curious what the results were like and as, you know, kind of where did you arrive?
[1862.96 --> 1866.04]  What surprised you along the way in the process?
[1866.28 --> 1868.40]  You know, what was not what you were expecting to see?
[1868.40 --> 1873.82]  And also, how did the larger organization at Google take the results?
[1874.02 --> 1880.02]  Is it something that is now becoming kind of standard at Google or was it just a test or an experiment?
[1880.40 --> 1885.54]  Or how did it affect the larger organization in terms of designing chips going forward?
[1885.54 --> 1901.88]  So we have definitely tested this method on chips that Google makes and have gotten superhuman results on a good portion of the complex chips that we tried placing them.
[1902.54 --> 1908.78]  But in terms of other questions you asked, I'm not sure if we can answer that at this point.
[1909.24 --> 1909.46]  Okay.
[1910.02 --> 1912.92]  But nothing jumped out from a surprise standpoint?
[1913.20 --> 1914.86]  Just kind of like you got something?
[1914.86 --> 1915.60]  I was curious.
[1915.76 --> 1916.12]  Yeah, sure.
[1916.22 --> 1917.72]  I have something to offer on that.
[1918.06 --> 1919.76]  I don't know, surprising, maybe just exciting.
[1920.42 --> 1930.60]  In terms of those generalization results, we would say take a policy and pre-train it on a larger number of chip netlists and then, you know, apply it to a new chip.
[1931.26 --> 1944.84]  So sort of surprised and excited us was that a pre-trained policy that was fine-tuned for, say, only 12 hours would outperform a policy that was trained from scratch on this netlist for 24 hours or more.
[1944.86 --> 1953.74]  So I think it was exciting to us that this new policy architecture generalized so well that it actually does better and it takes less time.
[1954.52 --> 1955.26]  That's pretty amazing.
[1955.26 --> 1956.00]  Yeah.
[1956.00 --> 1956.04]  Yeah.
[1956.12 --> 1968.22]  Was that having to do, I know when I was looking at the paper, you talked about like domain adaptation, which I remember we talked about with the OpenAI team.
[1968.22 --> 1973.02]  And also we've talked about in relation to like robotics and moving hands.
[1973.54 --> 1983.04]  So is that key to that sort of generalizability is adapting the domain or the environment during this training?
[1983.04 --> 1992.60]  If so, did you have to like create a bunch of simulated data for various environment changes and that sort of thing?
[1992.70 --> 1993.66]  What was your approach there?
[1993.66 --> 1999.14]  So we actually just used real chip netlists for all of the pre-training.
[1999.58 --> 2006.96]  But so we'd stay trained on 20 real chip netlists and then we were able to achieve those results where we have much better and faster results.
[2007.10 --> 2017.70]  But we probably could do some kind of data augmentation where we could maybe turn those 20 into many more or, you know, source more netlists in some other way and we would do much better.
[2017.70 --> 2035.50]  And what is your feeling in terms of, you know, how specific this pre-trained policy is for the sorts of chips that are included in the set of chip nets, I think you called them, that you use during pre-training?
[2035.80 --> 2045.88]  How specific do you think the pre-trained version of the policy is for that kind of family of chips or do you think it's generalizable beyond that?
[2045.88 --> 2049.72]  I think it's definitely affected.
[2050.14 --> 2056.14]  The policy's performance on a new netlist is definitely affected by the types of netlists that it's trained on in the past.
[2056.62 --> 2059.56]  At the same time, it's a pretty general problem.
[2060.02 --> 2065.40]  So, yeah, I think as long as you train on a representative set of netlists, you could do well on a new one.
[2066.14 --> 2066.36]  Gotcha.
[2066.36 --> 2076.40]  And what are some of the challenges that maybe you faced during this project that you maybe didn't have time to address in the initial version of this project?
[2076.58 --> 2079.82]  What are some of the things that you want to explore more going forward?
[2080.24 --> 2083.96]  I mean, there's just so many other stages of this process.
[2083.96 --> 2099.52]  And kind of what's exciting about, you know, developing policies that can more quickly generate high-quality placements is that we can kind of explore feedback or interactions between, say, previous stages, like upstream choices, like this choice of SRAM.
[2100.22 --> 2103.02]  Basically, there's a certain amount of memory that needs to be in this chip.
[2103.02 --> 2107.14]  But the choice of how to slice it up into these macros is somewhat arbitrary.
[2108.06 --> 2122.48]  And if you can, say, try one, like slice up the macros a particular way and then see what kind of placement, what level of quality you can get in terms of timing and other properties from that quickly, you could do all sorts of explorations upstream.
[2122.48 --> 2127.70]  So I want to follow up on something that you were saying before.
[2128.04 --> 2140.70]  And just to make sure I understand, when you're looking at these different types of chips that you want to apply this to, and going back, I know we had someone talk about some chips from a previous company earlier.
[2140.70 --> 2146.56]  But, you know, they were talking about basically different types, you know, from GPU, TPU, FPGAs, and such as that.
[2146.98 --> 2151.98]  Do those different architectures dramatically change the problem for you?
[2152.04 --> 2155.66]  I know that we were talking about the domain adaptation a moment ago.
[2155.66 --> 2179.62]  But, I mean, in a practical sense, do you have a substantially different RL approach every time you change out the chips, given that, like, I believe, like, a GPU will have a whole bunch of things beyond what a TPU might have on it, you know, because it's being able to address problems, whereas a TPU is very specific to the matrix multiplication.
[2180.22 --> 2182.38]  How does that affect your approach on that?
[2182.38 --> 2188.06]  I personally wasn't clear enough on it because of trying to learn this as we go.
[2189.26 --> 2189.78]  Yes.
[2190.06 --> 2201.02]  So we have tried our method on a bunch of different types of chips that were available inside of Google, and also chips that were available open source.
[2201.72 --> 2207.62]  And the way we did our RL approach didn't need to change going from one set of chips to the other.
[2207.62 --> 2220.04]  But definitely, like Anna was mentioning, the larger, if you have a chip that is drastically different from anything you have seen before, then it could affect the performance of the agent.
[2220.44 --> 2224.16]  But at the same time, the input space of our problem is very abstract.
[2224.72 --> 2227.98]  We don't deal with the specifics of a chip.
[2227.98 --> 2245.42]  Rather, we are dealing with a generic, like, netlist representation of a chip with these nodes that have certain connectivities, and the nodes have different sizes and different shapes, and we are placing them, optimizing for the cost that we have developed.
[2245.42 --> 2257.00]  So the problem, if we don't think about what chips they are, is very abstract in a sense that it can really handle different sorts of input from different chips.
[2257.90 --> 2266.14]  And so far, we didn't have a chip that was drastically different from our training set that we had to change the RL algorithm for.
[2266.14 --> 2270.82]  There's always a modification of the algorithm for improving it overall.
[2271.32 --> 2276.04]  But like I said, the input state is pretty standard among different types of chips.
[2277.36 --> 2292.68]  So I'm kind of curious, the more I think about this problem, it seems kind of like we're using an AI method to help design a chip on which AI will hopefully operate,
[2292.68 --> 2297.32]  or be trained or run inference on or that sort of thing.
[2297.52 --> 2309.48]  I'm kind of curious on a more general sense, how you see, you know, AI as we move into the future and AI development continues to accelerate.
[2309.48 --> 2320.62]  Are we going to kind of need these sorts of methods more and more because more specialized chips are going to be needed for these types of AI problems moving forward?
[2320.62 --> 2328.00]  How do you see kind of AI influencing the hardware that AI runs on, I guess, is my question?
[2329.30 --> 2333.00]  So chip design is a really complicated task.
[2333.42 --> 2338.40]  And making customized chips is definitely also very complicated.
[2338.40 --> 2350.76]  We are witnessing the more that we are going to need more and more of these customized chips because of various computational demands of especially AI algorithms.
[2351.42 --> 2360.40]  And our vision is AI can help the design of these chips because of its ability to learn and improve over time.
[2360.40 --> 2379.68]  For example, if we look into the chip design process, there are various stages of optimization from architecture design to logic design to verification and physical design and placement.
[2380.48 --> 2384.20]  Each of these stages are very complicated, are combinatorially hard.
[2384.20 --> 2394.20]  And so our goal or our vision is AI can help us finding globally optimized solutions across all of these stages.
[2394.58 --> 2403.70]  Then we are going to have hopefully a lot more performance improvement over what we have right now where we optimize each stage separately and then just cascade them together.
[2403.70 --> 2412.74]  And the reason we think AI can help with it, we mentioned this a couple of times in this conversation, was that AI can improve over time.
[2413.08 --> 2419.88]  And this property is something that's very different from what we have seen in any other existing methods.
[2420.24 --> 2426.82]  So the policy, the agents can become better, more experienced at doing newer tasks.
[2426.82 --> 2442.96]  So if we accumulate this experience over time, then we are dealing with these agents that become much better than any single person or single algorithm that has ever optimized the chip.
[2443.50 --> 2453.80]  Yeah, and that way it almost seems like so many other areas that we're applying AI techniques to and that you take it to that superhuman level and just continue on.
[2453.80 --> 2473.52]  It makes me wonder, as you guys, and I don't know, this may be almost an organizational question to some degree, but I'm curious whether having pioneered this, you know, being able to apply reinforcement learning to this particular problem, is this something that the two of you are expecting to continue working on for some time?
[2473.62 --> 2478.88]  Or have you kind of done your experiment and, you know, you got your results and you're going to move on to other problems?
[2478.88 --> 2481.42]  If it's the latter, what might those other problems be?
[2481.54 --> 2484.64]  Or if it's staying on this, what are you looking to next?
[2484.72 --> 2488.30]  What's the next step, whether it be on this problem or doing something else for each of you?
[2488.52 --> 2489.30]  Anna, you want to go first?
[2489.92 --> 2496.26]  I think that there are definitely other stages of the chip design process that, you know, have a lot of impact.
[2496.38 --> 2502.62]  I think getting to your last question a little bit in terms of, like, how can this affect kind of AI for AI chips?
[2502.62 --> 2506.70]  The current chip design process takes nearly two years.
[2507.22 --> 2513.62]  And so there could be certain types of machine learning architectures that just aren't computationally feasible on today's hardware.
[2514.14 --> 2518.76]  But if we could more quickly design chips for them, they might become more viable approaches.
[2519.48 --> 2522.44]  But the problem is that, say, chip floor planning is just one of these stages.
[2522.84 --> 2531.54]  So if we wanted to, say, dramatically accelerate this process, we would have to tackle these other stages, say, like architectural exploration or design verification.
[2531.54 --> 2531.98]  Awesome.
[2532.62 --> 2532.94]  Awesome.
[2533.12 --> 2540.28]  And you've built one of the building blocks of that process, but you could be exploring some of those other building blocks as well.
[2540.44 --> 2541.02]  Is that right?
[2541.92 --> 2542.56]  That's right.
[2543.20 --> 2543.56]  Awesome.
[2543.80 --> 2544.84]  What about you, Azalea?
[2545.56 --> 2548.76]  Yeah, I think I'm in a similar boat.
[2549.02 --> 2556.68]  I think I'm very excited about the research on RL and ML for optimization tasks in general.
[2556.68 --> 2563.96]  And I think chip design is a very critical and important application of optimization.
[2564.74 --> 2576.72]  Something that's going to enable, like, if you have better chips, we're going to have better next generation AI algorithms as well, because chips are key enablers of those algorithms.
[2576.72 --> 2588.38]  So I would say both research on RL for optimization and with applications in chip designs is something I'm very excited about and look forward to continue working on.
[2589.08 --> 2589.64]  Awesome.
[2589.92 --> 2592.78]  Well, thank you both for taking time to join us.
[2592.94 --> 2594.56]  This has been super fascinating.
[2594.56 --> 2604.26]  And it's been great to dive into some of these subjects like graph neural networks and chip design and these things that we haven't talked a lot about on the show.
[2604.40 --> 2608.62]  So I really appreciate both of you taking time and joining us for the conversation.
[2608.86 --> 2609.64]  It was great to talk.
[2610.36 --> 2611.18]  Thanks for having us.
[2611.28 --> 2612.62]  Thank you so much for having us.
[2615.80 --> 2618.58]  Thank you for listening to this episode of Practical AI.
[2619.18 --> 2623.00]  More like this at changelog.com slash practical AI.
[2623.00 --> 2628.64]  There you'll find our latest as well as lists of our most popular episodes and the ones we recommend.
[2629.14 --> 2633.00]  If this show has helped you on your AI journey, please leave us a five star review on Apple Podcasts.
[2633.84 --> 2635.04]  Part us on Spotify.
[2635.40 --> 2638.46]  Star us on Overcast and tell a friend what they're missing out on.
[2638.72 --> 2641.56]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2641.82 --> 2643.20]  It's produced by me, Jared Santo.
[2643.44 --> 2645.92]  And our music is brought to you by the Beat Freak, Breakmaster Cylinder.
[2646.50 --> 2647.64]  We have awesome sponsors.
[2647.78 --> 2648.48]  Please support them.
[2648.54 --> 2649.20]  They support us.
[2649.38 --> 2651.50]  Thanks again to Fastly, Linode, and Rollbar.
[2651.50 --> 2659.34]  If you and your organization could benefit from speaking directly to all the AI practitioners out there, you should sponsor the show.
[2659.76 --> 2664.60]  Podcast advertising is one of the most effective ways to spread your message in an authentic way.
[2664.88 --> 2667.42]  Plus, you get the added bonus of supporting something you love.
[2667.66 --> 2668.38]  That's all for now.
[2668.74 --> 2669.72]  We'll talk to you next time.
[2670.14 --> 2683.40]  We'll see you next time.
[2685.56 --> 2687.10]  We'll see you next time.
