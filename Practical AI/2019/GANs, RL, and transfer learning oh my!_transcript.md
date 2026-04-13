[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.02]  And unlike standard droplets, which use shared virtual CPU threads,
[29.02 --> 32.86]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.40 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.20 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.54]  productive, and accessible to everyone.
[88.94 --> 93.42]  This is where conversations around AI, machine learning, and data science happen.
[93.42 --> 98.20]  Join the community and snag with us around various topics of the show at changelog.com slash community.
[98.44 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.48 --> 102.28]  And now onto the show.
[106.88 --> 111.40]  Welcome to another fully connected episode where Daniel and I will keep you fully connected
[111.40 --> 113.74]  with everything that's happening in the AI community.
[114.22 --> 116.60]  We'll take some time to discuss the latest AI news,
[116.76 --> 120.44]  and we'll dig into learning resources to help you level up your machine learning game.
[120.44 --> 121.88]  My name is Chris Benson.
[122.06 --> 125.48]  I am the chief strategist for artificial intelligence, high performance computing,
[125.60 --> 127.16]  and AI ethics at Lockheed Martin.
[127.58 --> 132.54]  And with me is my co-host, Daniel Whitenack, who is a data scientist at SIL International.
[132.70 --> 133.50]  How's it going today, Daniel?
[133.88 --> 135.40]  It's going pretty good.
[135.74 --> 136.82]  It's been a good week.
[136.92 --> 137.94]  How about with you, Chris?
[138.26 --> 139.08]  It's been good.
[139.26 --> 141.20]  Just the usual busy stuff.
[141.90 --> 144.42]  I am excited about today's episode.
[144.42 --> 151.42]  This was, we were talking about it prior to getting on air, and you had some great ideas.
[151.56 --> 154.20]  You want to go ahead and talk about why we're doing what we're doing?
[154.84 --> 155.46]  Yeah, sure.
[155.64 --> 164.08]  So some of the listeners might know that I do industry trainings in AI and other things
[164.08 --> 167.42]  for companies and sometimes at conferences and that sort of thing.
[167.42 --> 173.16]  And one of the frequent questions that comes up during those trainings and just kind of
[173.16 --> 178.92]  conversations about AI in general are questions about kind of the difference between like
[178.92 --> 180.18]  an AI model.
[180.34 --> 186.18]  So you might think about having like a convolutional neural net, you know, model or image detection
[186.18 --> 188.20]  model, like something like that, like a model.
[188.32 --> 195.50]  Is that the same or different from like things like reinforcement learning, GANs, transfer learning
[195.50 --> 198.86]  are like GANs and reinforcement learning and transfer learning.
[199.00 --> 200.70]  Are those like types of models?
[200.70 --> 205.78]  Like you have a transfer learning model or are they like different sorts of things than
[205.78 --> 211.70]  models that, you know, like then specific architectures that might be associated with like specific
[211.70 --> 216.10]  neural units like recurrent neural networks or convolutional neural networks.
[216.22 --> 222.06]  So my thought today is that maybe we could just kind of go through a few of these like
[222.06 --> 230.14]  methodologies or approaches, maybe we can call them that aren't maybe like models themselves,
[230.14 --> 233.38]  but are connected to the AI world in some way.
[233.50 --> 238.40]  So I'm suggesting that maybe we kind of talk through what what reinforcement learning is,
[238.40 --> 242.00]  what GANs are and what transfer learning is.
[242.14 --> 242.96]  How does that sound?
[243.40 --> 245.36]  That was that's a great idea as far as I'm concerned.
[245.52 --> 250.42]  And it's the kind of thing that that we hear in feedback a lot, because as people come into
[250.42 --> 254.58]  the podcast, they're coming from, you know, some people are already experts in the field.
[254.72 --> 259.06]  A lot of people coming in are brand new and they're trying to understand what the field
[259.06 --> 259.42]  is about.
[259.42 --> 262.02]  And there's so much to learn these days.
[262.02 --> 267.16]  And it's evolving so, so rapidly that I thought this was a great idea to just kind of go through
[267.16 --> 274.38]  each of these and just identify or define what each one is and basically how it works and
[274.38 --> 278.06]  allow people to kind of get up to speed on those a little bit faster.
[278.06 --> 278.70]  Yeah.
[278.70 --> 278.78]  Yeah.
[278.94 --> 283.90]  And as we go through these, we can maybe just give a little bit of a sense of what they
[283.90 --> 289.92]  are, but also give some places that they've shown up in the news recently and in the AI
[289.92 --> 291.76]  news or news in general.
[291.96 --> 294.84]  And then some learning resources for each one.
[294.98 --> 300.04]  If you want to kind of get started in reinforcement learning or one of these other things, some some
[300.04 --> 305.12]  some links that will for sure put in our show notes so that you can follow up on those
[305.12 --> 307.36]  things and start learning them practically.
[307.36 --> 311.40]  Remember, we're all about practicality here at this podcast.
[311.40 --> 314.94]  So I want to make sure and include those links as well.
[315.50 --> 318.08]  So which which one of these you want to get started with, Chris?
[318.54 --> 320.82]  You want to dive into reinforcement learning up front?
[321.72 --> 322.02]  Sure.
[322.32 --> 331.84]  So again, we're kind of thinking about approaches or methodologies that involve AI models, but might
[331.84 --> 337.24]  be kind of slightly different than a single one end to end model.
[337.46 --> 340.62]  So with reinforcement learning, where have you seen?
[340.86 --> 344.56]  First of all, where have you seen reinforcement learning being applied, Chris?
[344.96 --> 350.64]  I think the thing that made reinforcement learning big was its application to simulation and to
[350.64 --> 351.14]  robotics.
[351.14 --> 357.62]  And it's it's, you know, reinforcement learning has been kind of a core technique for for doing
[357.62 --> 359.44]  simulation robotics for a long time.
[359.44 --> 364.30]  And then in recent years, deep reinforcement learning, which we'll dive into in a few minutes
[364.30 --> 368.56]  here, has really come in and revolutionize that process itself.
[368.56 --> 376.14]  But in real life, at a previous employer, I we were working on a large multi skilled team
[376.14 --> 377.54]  with different people specializing.
[377.74 --> 382.42]  And we had reinforcement learning specialists on the team that were focused on doing robotics.
[382.42 --> 385.00]  So, I mean, it's definitely real world stuff.
[385.10 --> 387.62]  It's not just academic and and it works.
[387.72 --> 388.92]  And that's why they're doing that.
[389.62 --> 389.78]  Cool.
[389.92 --> 390.12]  Yeah.
[390.16 --> 394.56]  So you mentioned that there's kind of this thing reinforcement learning and then there's
[394.56 --> 396.84]  like deep reinforcement learning.
[396.84 --> 401.74]  And that's kind of where part of this AI or neural network stuff gets plugged in.
[401.74 --> 408.54]  But in reinforcement learning, one of the main pieces of reinforcement learning is this
[408.54 --> 410.22]  thing called an agent.
[410.22 --> 412.68]  And this agent takes action.
[412.94 --> 420.20]  So like in your case, Chris, with the with the robots, you know, what what do you remember
[420.20 --> 425.34]  kind of what this sort of agent or these actions were that the agent was taking?
[426.00 --> 426.14]  Sure.
[426.32 --> 431.62]  So you'll have different software components within the robot and they may be integrated
[431.62 --> 436.30]  with different types of models and they each have a particular job.
[436.30 --> 441.82]  And and for simplicity's sake, let's just say it's about moving the robot around its environment.
[441.82 --> 449.76]  And so initially you have to have an algorithm where that the agent is going to use to make
[449.76 --> 453.58]  decisions based on what's happening to it in the environment that it's operating in.
[453.66 --> 460.56]  And the way you do that is every time the agent actually takes an action that changes the
[460.56 --> 463.46]  relationship it has within the environment, which is called state.
[463.66 --> 468.60]  And so that might have been it could have been a good action that's kind of going toward
[468.60 --> 471.58]  what you're trying to train it for or maybe not such a good action.
[471.82 --> 478.22]  And the way that is determined by the person that's training the model is by offering a
[478.22 --> 482.20]  reward for for the appropriate actions being taken.
[482.20 --> 488.24]  So you're essentially you you can kind of think of it as since, you know, we're always
[488.24 --> 492.12]  talking about pets and stuff like that, treating a dog for doing the right thing with positive
[492.12 --> 495.20]  reinforcement training for those of us who have pets.
[495.92 --> 496.94]  Same kind of ideas.
[497.12 --> 498.90]  You want to let the agent know, hey, that was good.
[498.90 --> 503.38]  You get bonus points for this, you know, for doing the right thing or we're going to pull
[503.38 --> 504.60]  back something if you don't.
[504.74 --> 506.78]  And so that's kind of the basic idea.
[506.90 --> 512.52]  You go through that iteration many, many times to try to get your robot or your simulation
[512.52 --> 517.84]  could be a video game, could be whatever to start behaving in the way that it has been
[517.84 --> 519.42]  most rewarded along the way.
[520.10 --> 520.50]  All right, cool.
[520.50 --> 525.50]  So let me let me try to I'm kind of trying to parse through in my mind some of the things
[525.50 --> 527.30]  that you said, which was really good.
[527.84 --> 534.20]  So there's this first thing that's called an agent and that agent can take action.
[534.20 --> 539.22]  So let's say in a very simple scenario with a robot, maybe the robot can only do two things.
[539.22 --> 540.60]  It can move left or it can move right.
[540.60 --> 549.26]  So that agent has to determine if based on some external factors, so the environment
[549.26 --> 554.84]  and its current state or maybe where it's at or which way it's facing, if it's to move
[554.84 --> 556.14]  left or if it's to move right.
[556.24 --> 560.50]  So it takes in some inputs from that environment and it's supposed to determine if it moves
[560.50 --> 561.78]  right or left.
[561.78 --> 571.14]  Now, I think what what this so the agent employs what's called a policy to determine that next
[571.14 --> 571.60]  action.
[571.60 --> 576.82]  So let's say that the robot is in this place with these coordinates and maybe there's
[576.82 --> 578.62]  other external factors or something.
[579.50 --> 580.96]  And so it's got a current state.
[581.08 --> 582.80]  It's somewhere in its environment.
[582.80 --> 590.30]  And that policy is is to determine that that next action based on the current state, whether
[590.30 --> 594.06]  it's maybe move left, move right, do this, do that.
[594.22 --> 600.26]  So, yeah, I think that there's so I think so far I'm kind of trying to count up the things
[600.26 --> 603.10]  that reinforcement learning involves in my mind.
[603.12 --> 604.02]  And we've got the agent.
[604.24 --> 605.48]  We've got the policy.
[605.66 --> 607.00]  We've got the state.
[607.24 --> 608.84]  And then we've got the environment.
[608.84 --> 611.58]  Now, you mentioned you mentioned the reward.
[611.98 --> 617.86]  So so the reward also is kind of how the model gets feedback.
[617.86 --> 618.48]  Is that right?
[618.92 --> 620.16]  Yeah, it's the feedback loop.
[620.30 --> 623.86]  And the purpose of the reward is to shape the policy.
[623.86 --> 631.26]  So your policy is is being evolved so that at the end of your training, the policy hopefully
[631.26 --> 633.88]  always does the right thing that you're training towards.
[633.88 --> 638.14]  And you're essentially giving it little bumps with the reward to get it there.
[638.22 --> 642.78]  And so you're trying to shape the policy, which is the strategy that the robot is using
[642.78 --> 643.40]  to move around.
[643.78 --> 647.04]  And so there are many different ways of doing that.
[647.04 --> 650.00]  There are lots of different algorithms that have been used over the years.
[650.00 --> 655.40]  And, you know, when one of those that which we'll talk about has moved into what's called
[655.40 --> 656.48]  deep reinforcement learning.
[657.12 --> 657.20]  Yeah.
[657.20 --> 657.24]  Yeah.
[657.32 --> 662.84]  So in my mind, if I if I'm thinking about this, I kind of see this loop where the agent takes
[662.84 --> 663.48]  actions.
[664.16 --> 670.40]  And then at some point in the feedback loop, the the environment or so the environment
[670.40 --> 674.54]  infuses a reward or feedback into the into the agent.
[674.54 --> 680.60]  Now, you know, one of the things that people ask me kind of is when they're trying to figure
[680.60 --> 684.66]  out this reinforcement learning thing, they kind of get the idea of, OK, you know, you
[684.66 --> 688.28]  can give a dog treats and kind of help train it.
[688.40 --> 690.60]  So this idea of training kind of makes sense.
[691.70 --> 697.78]  But but they have a hard time picturing kind of where the neural network fits in this in
[697.78 --> 701.20]  this scenario or where the model fits in this scenario.
[701.20 --> 705.96]  So one example of that might be like if if our robot has a camera.
[706.50 --> 706.98]  Right.
[707.48 --> 711.78]  And it's looking at its environment or maybe it's looking at a at a simulation.
[712.20 --> 715.04]  One thing it could do is like image recognition.
[715.04 --> 715.48]  Right.
[715.54 --> 721.26]  And then based on that image recognition, it could determine whether to move left or or
[721.26 --> 723.20]  move right or or something like that.
[723.20 --> 731.06]  So instead of like the image coming in and then the output just being like this object
[731.06 --> 738.22]  is in this image or not, then in this scenario, the image would come into the model and the
[738.22 --> 743.50]  output of the model would be like the action like left or right or something, something like
[743.50 --> 743.66]  that.
[743.70 --> 747.84]  So there's still this kind of neural network model there, but it's tied into this feedback
[747.84 --> 751.50]  loop where the the output is is that is the action is.
[751.50 --> 754.20]  Am I am I representing that correctly, Chris?
[754.64 --> 756.82]  I think that's a very good explanation.
[756.82 --> 765.26]  So a lot of times what the reinforcement learning is acting on, maybe, you know, so maybe a camera,
[765.50 --> 767.20]  the camera images coming in.
[767.20 --> 772.98]  And so the type and is a little side note, the type of neural network that is most often
[772.98 --> 775.90]  used for that is called a convolutional neural network or a CNN.
[776.18 --> 779.66]  And we've had several episodes where we've talked about that, including one that was a
[779.66 --> 781.96]  deep dive on the technology early on.
[781.96 --> 788.14]  And so typically when we've talked about those, we'll we'll talk about the convolutional neural
[788.14 --> 794.18]  network basically classifying what it sees, essentially putting a label on it with a
[794.18 --> 797.56]  percentage of, you know, I'm I'm looking at something.
[797.56 --> 798.86]  Is that a horse?
[798.94 --> 799.64]  Is it a cow?
[799.72 --> 800.36]  Is it a dog?
[800.38 --> 804.84]  And there's some level of a percentage of confidence that is being assigned to those
[804.84 --> 806.44]  traditionally with CNNs.
[806.44 --> 810.88]  The difference when you put it in with this particular approach, with reinforcement learning
[810.88 --> 814.36]  is you're you're talking about influencing the policy.
[814.50 --> 819.20]  So what you really need is the output of that convolutional neural network is what action
[819.20 --> 821.12]  should I take for my next action?
[821.28 --> 827.04]  And that's that way it feeds into how the the reinforcement learning algorithm is trying
[827.04 --> 833.74]  to do that reward to change the policy over time on how the model is acting on the environment.
[834.36 --> 835.34]  That's a great point.
[835.34 --> 840.68]  So, you know, you mentioned the convolutional neural network, but, you know, people could
[840.68 --> 847.34]  see that this reinforcement learning algorithm or approach is is really just that it's a
[847.34 --> 853.82]  it's algorithm or approach where within that approach, you could apply a convolutional neural
[853.82 --> 860.92]  network in your agent to kind of learn a certain policy to take in images and output actions.
[860.92 --> 864.68]  But people use reinforcement learning for all sorts of other things.
[865.08 --> 870.90]  And, you know, the that approach is kind of independent of the specific kind of model
[870.90 --> 871.48]  that comes in.
[871.58 --> 877.92]  So, you know, you could perfectly well use other type other architectures of neural networks,
[878.02 --> 881.78]  you know, recurrent and other things within your agent.
[881.78 --> 888.28]  But this reinforcement learning loop or approach would kind of still still be there.
[888.38 --> 891.90]  That would still be kind of an RL approach to maybe a different sort of problem.
[892.62 --> 892.72]  Yeah.
[892.80 --> 894.96]  And you raise a really great point there.
[894.96 --> 897.12]  And we've kind of alluded to it several times.
[897.12 --> 903.74]  And that is and just to kind of back out of the specific RL reinforcement learning focus
[903.74 --> 910.00]  conversation, we're talking about different approaches that have different algorithms or
[910.00 --> 910.88]  architectures.
[910.88 --> 915.42]  And in, you know, when you set aside all these buzzwords, they are there.
[915.52 --> 920.98]  Each one is trying to solve a particular class of problem, whether it's whether, you know,
[920.98 --> 925.34]  we were talking about CNNs looking at images and and trying to solve that and reinforcement
[925.34 --> 930.90]  learning, being able to have an agent take actions that are rewarded to get to the right
[930.90 --> 933.06]  policy to to act in your environment.
[933.56 --> 935.28]  We've talked about several others.
[935.28 --> 938.40]  And the point is, you can use a lot of these together.
[938.40 --> 943.10]  And so to avoid confusion is if you're working on a particular problem and you might be in
[943.10 --> 947.18]  reinforcement learning and say, well, it's it's images that I'm active that I need to act
[947.18 --> 949.82]  on in this case, you would stick a CNN there.
[949.82 --> 957.64]  And that is just one possibility of of of how you would combine different types of of
[957.64 --> 961.46]  architectures or algorithms in deep learning to get where you want to go.
[961.46 --> 966.68]  So it's not always the case that one architecture, one algorithm gets you where you want to go.
[966.80 --> 968.44]  You may a little bit like Legos.
[968.54 --> 969.72]  You may plug some of these together.
[969.84 --> 972.28]  I just wanted to clarify that in case there was any confusion.
[972.94 --> 974.32]  Yeah, I appreciate that.
[974.32 --> 980.42]  Um, so maybe, um, before we move on to the next thing, let's, uh, maybe just think about,
[980.56 --> 985.36]  okay, where, where's reinforcement learning showing up in, in kind of AI news?
[985.36 --> 991.36]  And, um, what are some learning resources that people can, can, uh, look into if they're trying
[991.36 --> 994.76]  to learn reinforcement learning, if this has piqued their interest?
[994.76 --> 1000.60]  So one of the things that I've seen in the news recently, um, so very recently are, you know,
[1000.60 --> 1006.44]  and people have probably seen related things, uh, on Twitter or wherever is deep mind released,
[1006.44 --> 1013.20]  a reinforcement learning approach to, uh, that resulted in human level performance in a video
[1013.20 --> 1014.16]  game quake three.
[1014.68 --> 1019.44]  Um, and so this is pretty cool where, uh, you know, a lot of these reinforcement learning
[1019.44 --> 1024.98]  techniques have been applied to kind of fun things like, uh, like video games and, and,
[1024.98 --> 1026.02]  uh, things like that.
[1026.14 --> 1030.48]  If you're, if you're more interested in reinforcement learning, uh, we've actually had a
[1030.48 --> 1037.46]  couple episodes, so episode 14 and episode 40 of, uh, practical AI, um, that talk about
[1037.46 --> 1042.16]  certain applications of, of reinforcement learning with a little bit more explanation.
[1042.84 --> 1047.62]  Um, and as well, one of the learning resources that I found that, that looked, uh, really good,
[1047.62 --> 1053.04]  um, on this front is there's actually, uh, an official PyTorch tutorial on reinforcement
[1053.04 --> 1053.52]  learning.
[1053.88 --> 1056.70]  Um, and we'll make sure and link that in our show notes.
[1056.70 --> 1061.60]  Um, if you want to, uh, to go ahead and dig a little bit deeper into reinforcement learning
[1061.60 --> 1063.64]  and actually try some things out on your own.
[1071.68 --> 1074.00]  This episode is brought to you by discover.bot.
[1074.22 --> 1078.38]  Learn everything there is to know about bots at discover.bot slash practical AI.
[1078.38 --> 1083.30]  Discover.bot was built by Amazon registry services as an online community for bot creators and
[1083.30 --> 1086.62]  makers of all skill levels to learn from one another, to share stories.
[1086.62 --> 1090.74]  And they regularly publish guides and resources to answer questions like how to set up payments
[1090.74 --> 1095.16]  to your bot, how to stop shopping cart abandonment, what KPIs are worth measuring, how to write
[1095.16 --> 1097.02]  an engaging chat bot dialogue.
[1097.34 --> 1099.22]  You can even register .bot domains there.
[1099.54 --> 1104.26]  Learn more and explore this huge library of bot resources at discover.bot slash practical AI.
[1104.58 --> 1107.08]  Again, discover.bot slash practical AI.
[1108.38 --> 1124.76]  So Daniel, now that we've covered reinforcement learning, uh, what do you say we dive into
[1124.76 --> 1127.60]  GAN, generative adversarial networks?
[1128.32 --> 1129.76]  Yeah, that sounds, sounds good.
[1129.88 --> 1135.90]  So, um, this sounds kind of, kind of scary adversarial, uh, things, Chris.
[1135.90 --> 1138.40]  Are you going to talk about Terminators now?
[1138.70 --> 1140.64]  Are we, are we, are we about to all die?
[1141.28 --> 1141.50]  Yeah.
[1141.60 --> 1144.06]  Is it, uh, uh, yeah, I don't know.
[1144.16 --> 1148.00]  Is, how adversarial are these, uh, are these networks, Chris?
[1148.44 --> 1152.32]  Well, I'd say that, uh, that they're adversarial with each other, which is the whole point,
[1152.38 --> 1154.20]  which is why they're calling it that.
[1154.20 --> 1179.02]  Um, it, it is, uh, it is a really, really interesting innovation that came about in 2014, um, where a, uh, one of the, the, uh, very famous, uh, figures in this space, whose name is, uh, Ian Goodfellow, uh, was, uh, put out a research paper with several of his colleagues and about generative adversarial networks.
[1179.02 --> 1194.72]  And what that is, is basically you have two different types of neural network architectures designed to work together, um, or, or more specifically against each other to try to get where you, where you want to go.
[1194.82 --> 1204.32]  Um, it, it, it's, it's a way of, uh, of often creating, uh, uh, outputs that are creative, uh, from this type of technology.
[1204.32 --> 1206.56]  Um, pretty, pretty interesting stuff.
[1206.56 --> 1208.96]  I've seen it used for lots of different use cases too.
[1209.12 --> 1212.24]  And I, yeah, you mentioned kind of the creative element of this.
[1212.34 --> 1223.48]  Um, you know, one of the places I think this has received a lot of attention for, for good and bad and in some ways is, um, like in generating images.
[1223.66 --> 1233.44]  So, uh, you know, there's kind of examples of creative uses, like generating specific artwork or generating things in the style of, of certain other things.
[1233.44 --> 1239.88]  There's, um, also examples of generating kind of, uh, pictures of, of fake people and, and all of these things.
[1239.88 --> 1246.34]  So this all involves this kind of generative element of GANs or generative adversarial networks.
[1246.34 --> 1252.68]  So you mentioned that there's kind of two elements of this, uh, of this methodology, Chris.
[1252.68 --> 1261.34]  So there's obviously some sort of generative element of this, which is what people call the generator of the, um, of this approach.
[1261.58 --> 1263.92]  What's, what's the other thing that's involved here?
[1264.38 --> 1271.18]  So you have the generator and then you have, which is the, the one part of, of this combined architecture.
[1271.18 --> 1274.62]  And then the other side, the other algorithm, uh, is the discriminator.
[1275.12 --> 1285.94]  And so essentially the generative architecture or model in this case that's being trained is, is creating outputs that are inputs for the discriminator.
[1285.94 --> 1296.20]  And the input on the discriminator side, it's essentially trying to, uh, to classify which ones are real and which ones are fake.
[1296.22 --> 1307.74]  And it has those mixed in with the ground truth data set so that, um, if you're trying to create, uh, images and you're, and, and this might be something that's completely new.
[1307.74 --> 1315.50]  The discriminator has access to a data set that has a bunch of real images that are the, the ground truth that you're training against.
[1315.62 --> 1317.80]  It is, it is that baseline data set.
[1318.12 --> 1328.78]  And the generator is, is also looking at those, but it's creating images that are meant to look like whatever it is that the, that the data set is representing.
[1328.90 --> 1335.14]  And so, um, it might be, I'm just making this up, might be cats since we like to talk about cats on the internet.
[1335.14 --> 1341.14]  And, um, so you might have a bunch of images in the actual data set of cats.
[1341.28 --> 1348.06]  And then the generator is trying to create new images of cats and slide that in with the ground truth data sets.
[1348.06 --> 1353.96]  And it's up to the discriminator to determine which ones are real and which ones are not and put a percentage on that.
[1354.40 --> 1362.30]  And so there's this feedback loop between the two to where the discriminator is constant, is making its choices and giving that feedback to the generator.
[1362.30 --> 1370.24]  And in turn, the generator is, is learning from what the discriminator is able to do right or wrong and produce more and better images.
[1370.24 --> 1378.52]  So, uh, it's a neat thing where this, the, the adversarial side is that these two models are literally trying to beat each other.
[1378.52 --> 1388.22]  Uh, one analogy could be, um, uh, a policeman against a counterfeiter with the generator being the counterfeiter and the discriminator being the policeman.
[1388.22 --> 1391.30]  And they're each trying to do their thing and get better and better at it.
[1391.32 --> 1393.16]  And by doing that, they, they both get better.
[1393.72 --> 1393.82]  Yeah.
[1393.86 --> 1401.18]  I've, I've also heard the analogy kind of being, uh, the, the generator is the artist and the discriminator is the art critic.
[1401.18 --> 1406.52]  Um, trying to, trying to examine the, the output of output of the generator.
[1406.76 --> 1420.30]  Um, so similar to, so in some ways, similar to reinforcement learning, there's this kind of overall scaffolding in which, um, in this case, two models are, are interacting.
[1420.30 --> 1425.88]  So there's, there's, uh, there's more going on here than just kind of one end to end model.
[1425.98 --> 1431.26]  There's, there's a couple of things happening here and there's this loop between the generator and the discriminator.
[1431.26 --> 1443.24]  Now, each of these, uh, pieces, so the generator itself and the discriminator, each of them, um, could be, uh, a single neural network.
[1443.24 --> 1455.34]  So the generator might be a neural network that takes in, for example, some, uh, random inputs and generates a, an image on the output, like a art image or something like that.
[1455.34 --> 1462.34]  So it's, it's input, um, might be, uh, you know, uh, some, some kind of random input like that.
[1462.34 --> 1473.00]  And the output might be what you're trying to generate, uh, the discriminator on the other hand, um, it's taking in a whole bunch of images and it's kind of like a classifier.
[1473.00 --> 1490.60]  So it may just be another, um, type of neural network, uh, that is trained to be a classifier to classify as like, you know, human generated or, or computer generated or, um, good art or bad art or, you know, something like that.
[1490.60 --> 1494.68]  So it's a, it's a classifier that classifies that, that set of images.
[1494.68 --> 1499.00]  So you kind of got two, two quote unquote models here.
[1499.00 --> 1503.86]  Um, and that's where the, that's where the neural networks are, are fitting in here.
[1503.96 --> 1510.98]  Of course, there's specific types of generative models that, uh, that work particularly well in this framework.
[1510.98 --> 1518.16]  Um, for, for the image case, um, DCGAN is, is, uh, uh, fairly popular.
[1518.16 --> 1530.66]  There's a, um, open AI article that we'll for sure link in our, in our, uh, show notes that kind of describes some of the generative models that are used in, in, uh, in GANs.
[1530.66 --> 1540.48]  But, uh, maybe, uh, as we kind of look, uh, a little bit more at GANs, maybe we can talk about where they've been showing up in the, in the news.
[1540.48 --> 1546.72]  So where, where have you been seeing, uh, GANs show up recently in, uh, in AI news or news in general, Chris?
[1547.20 --> 1561.54]  Well, one of the things that we have talked about, uh, on a couple of previous episodes was that, um, there was a portrait that was created by a GAN that Christie's auction house sold, uh, at auction, uh, for $432,000.
[1561.54 --> 1566.64]  And, and it really, nobody, including the people selling it were expecting that.
[1567.06 --> 1573.54]  Um, and that was, uh, it was for a, a, a, a unique, uh, an original piece of artwork that a GAN created.
[1573.84 --> 1582.06]  But, um, you know, and, and that really suddenly, it really shook that industry, you know, because it was, it was one of those instances that nobody saw coming.
[1582.46 --> 1586.16]  Um, but we're also seeing it in all sorts of other places, creating original music.
[1586.16 --> 1587.56]  We've talked about that in the past.
[1588.00 --> 1591.34]  Um, it's, uh, I know that, uh, Ian Goodfellow uses it.
[1591.34 --> 1593.60]  In the security industry, which is completely different.
[1594.06 --> 1603.48]  Um, and so there are, there are so many different use cases where you want some sense of originality or creativity to, to play into it.
[1603.76 --> 1612.84]  Um, and, and using GANs to actually generate the stuff is, uh, regardless of what the medium is, is, is becoming a better and better option for doing that.
[1613.08 --> 1613.52]  Yeah.
[1613.64 --> 1620.86]  I, I know one thing that I've seen, um, but kind of even people that have, so like my, my brother-in-law,
[1620.86 --> 1624.38]  uh, who isn't involved in the, in the AI industry at all.
[1624.38 --> 1629.36]  I mean, he's kind of interested in, in tech things, but not really a programmer or anything like that.
[1629.84 --> 1632.60]  Um, he even showed me this one website.
[1632.78 --> 1637.62]  So people are probably familiar with this, that, uh, it's, this person does not exist.com.
[1637.62 --> 1638.64]  Have you seen this, Chris?
[1638.84 --> 1639.22]  I have.
[1639.32 --> 1641.30]  I, and it's gotten better and better over time.
[1641.60 --> 1643.32]  Yeah, it has gotten better over time.
[1643.32 --> 1655.66]  And, uh, and this website, if you're not familiar with it, um, you can go there and basically all it shows you is a, is a picture of a person, but, um, and it looks, you know, exactly like a real person.
[1655.66 --> 1662.56]  So it's kind of, um, uh, you know, it takes you off guard when you realize that this person does not exist.
[1662.56 --> 1671.46]  In other words, this picture of this person, which looks, you know, real in every way is a picture of someone that is completely generated.
[1671.46 --> 1677.62]  So, uh, everything about that, that picture is generated using this, this type of methodology.
[1677.62 --> 1682.34]  And of course, that's, uh, really interesting and kind of amusing in certain ways.
[1682.86 --> 1689.04]  Um, but also it, it's kind of, uh, you know, concerning in, in other ways.
[1689.04 --> 1695.96]  Like, uh, of course, you know, everyone is concerned with, with fake news and, and fake, uh, content on the internet now.
[1695.96 --> 1704.78]  So, uh, there's definitely a concern with these around, uh, if what you're looking at is actually, is actually real or not.
[1704.78 --> 1720.04]  I remember talking on one episode, I forget which one about, um, you know, there's actually people out there that will create a, a fake persona, a fake picture for you for Instagram to be kind of your company's influencer, um, you know, on, on the internet.
[1720.04 --> 1724.70]  So there's a, there's a question here of like, you know, how real are the things that we're interacting with?
[1724.70 --> 1725.22]  Yeah.
[1725.40 --> 1726.62]  So it's interesting.
[1726.88 --> 1734.70]  Um, one of the responsibilities I've taken on at Lockheed Martin, uh, is, uh, is contributing to developing, uh,
[1734.70 --> 1741.38]  AI ethics and, and, and figure out, you know, not just about what we do, but about how we react to what's happening in the world.
[1741.38 --> 1743.96]  And there are obviously bad actors out there.
[1743.96 --> 1747.80]  And so one of the, the things, you know, GANS are so powerful.
[1747.80 --> 1754.34]  Um, and, and as a quote, Facebook's, uh, AI research director is, is very well known in the industry, Jan LeCun.
[1754.34 --> 1761.22]  And he, uh, he referred to the GANS famously as the most interesting idea in the last 10 years in machine learning.
[1761.22 --> 1769.52]  Um, and, and obviously Ian Goodfellow and, and, and his, his, uh, partners that were working on this are among the brightest minds in the field.
[1769.52 --> 1779.02]  So there, there's so much potential for, for the use of GANS, uh, both wonderful, interesting, and, and some bad use cases as well.
[1779.02 --> 1791.38]  So it's, it's, it's, it's the, the advent of GANS has changed the conversation in terms of AI safety and AI ethics and, and how these technologies, uh, can and should be used.
[1791.66 --> 1800.38]  Yep. Um, so if, if people are interested in diving a little bit more into GANS, there's definitely some good resources out there.
[1800.38 --> 1813.82]  So for, um, for reinforcement learning, we, we mentioned there's a PyTorch tutorial and there's a bunch of other tutorials out there for that, but there's a really great, uh, TensorFlow tutorial for, um, GANS.
[1813.82 --> 1817.04]  So we'll make sure and link that in the, in the show notes.
[1817.04 --> 1828.90]  Actually, if you, if you go to that tutorial, they have some nice, um, some nice pictures as well, talking about the generator and the discriminator and cat images and, and all of those good things.
[1828.90 --> 1836.98]  But then they walk you through all of the code, um, with Keras and TensorFlow to, um, to actually, uh, create this, this GAN.
[1836.98 --> 1845.82]  And they have a link to kind of pop that up in a Google Colab, uh, notebook so that you can go ahead and, uh, and get started, uh, with GANS.
[1853.54 --> 1857.40]  Well, hello there listeners of Practically I. How are you? This is Adam Stachowiak.
[1857.40 --> 1861.16]  If you haven't heard yet, we're launching a new show called Brain Science.
[1861.42 --> 1864.30]  It's a podcast for the curious. Are you curious?
[1864.86 --> 1874.84]  Because if so, we're exploring the inner workings of the human brain to understand things like behavior change, habit formation, mental health, and what it means to be human.
[1875.32 --> 1877.16]  It's brain science applied.
[1877.62 --> 1883.74]  Not just how does the brain work, but how do we apply what we know about the brain that can transform our lives.
[1883.74 --> 1888.62]  Learn more about the show and subscribe at changelog.com slash brain science.
[1888.80 --> 1893.88]  Until then, here's a preview of episode one where we talk about the fundamentals of being human.
[1894.14 --> 1897.06]  We're also all designed to be in relationship.
[1897.82 --> 1903.80]  We are fundamentally hardwired to have social groups and, and this sense of attachment.
[1903.80 --> 1916.52]  And because I'm sort of a geek when it comes to research, what researchers have found is that attachment, which that's what we label, how we relate and connect with others.
[1916.74 --> 1925.66]  Attachment is a hundred percent learned, which means our genetics don't actually contribute to how we learn to stay in proximity with other people.
[1925.66 --> 1933.56]  And with that, that we all develop ways to manage the threat of the loss of a relationship.
[1934.20 --> 1939.00]  But nobody gets to opt out of going, I need to be in relationship with others.
[1939.22 --> 1943.02]  I mean, think about it within the context of the prison system.
[1943.22 --> 1949.52]  Like, why is it that the punishment for prisoners when they don't fall in line is isolation?
[1950.04 --> 1951.02]  Yeah, that's true.
[1951.02 --> 1951.30]  Right.
[1951.94 --> 1955.88]  That wouldn't be significant if in some way that doesn't actually harm our brain.
[1956.20 --> 1960.20]  It's almost like we need to have that echo from another human being to let us know that we.
[1960.62 --> 1961.10]  Yeah.
[1961.30 --> 1964.94]  We're, we're there or we're alive or just some sort of feedback loop.
[1965.00 --> 1966.36]  I'm not really sure how to describe that.
[1966.72 --> 1969.84]  Well, it really is this sense of being with, right?
[1969.84 --> 1975.86]  Like I can't fight battles on my friend's behalf or on my kid's behalf, right?
[1975.86 --> 1985.82]  But the simple fact that I know of what's going on makes a difference because I would contend it sort of like I help them hold that weight emotionally.
[1986.72 --> 1989.04]  And so that actually leads me into the third thing.
[1989.04 --> 1996.16]  And the third thing that I would say in regards to the fundamentals of being human is that we all struggle.
[1996.30 --> 1997.24]  Oh, yes.
[1997.72 --> 1998.28]  Right?
[1998.80 --> 1999.46]  Big time.
[1999.46 --> 2005.44]  And that, you know, we don't always get to pick the way in which we struggle, but we all struggle.
[2006.58 --> 2010.90]  Well, if you like what you hear, you should go to changelog.com slash brainscience.
[2010.98 --> 2013.56]  The show is not out yet, so don't get too excited.
[2013.56 --> 2018.58]  But you can subscribe and be notified as soon as the show launches.
[2019.12 --> 2021.56]  Once again, changelog.com slash brainscience.
[2029.46 --> 2029.90]  Okay.
[2040.16 --> 2043.66]  Lastly, so we talked about reinforcement learning.
[2043.74 --> 2044.76]  We've talked about GANs.
[2045.18 --> 2050.72]  Let's go ahead and jump into this last thing that I hear people asking about, which is transfer learning.
[2050.72 --> 2060.74]  And we've certainly touched on this in previous episodes, but we haven't kind of put it in context like we're putting in context these other things.
[2060.74 --> 2074.12]  So transfer learning is another one of these kind of methodologies or approaches that's used in AI by AI practitioners to do a bunch of different things.
[2074.12 --> 2077.82]  But transfer learning isn't kind of a model in and of itself.
[2078.10 --> 2080.58]  It's another one of these approaches.
[2081.18 --> 2090.86]  And I would say in comparison to GANs and reinforcement learning, it's actually one that I've leveraged pretty heavily in my own work.
[2091.00 --> 2100.06]  I haven't touched as much or reinforcement learning and GANs haven't touched my life as much as transfer learning has.
[2100.06 --> 2107.44]  I think transfer learning is something that pretty much all AI practitioners should be familiar with and utilize heavily.
[2107.56 --> 2108.20]  What do you think, Chris?
[2108.48 --> 2114.32]  I would say that pretty much all AI practitioners have utilized it, whether they realized it or not.
[2114.36 --> 2115.30]  Yeah, that's probably true.
[2115.50 --> 2123.36]  If not before, certainly when they were learning how to do this and they were initially going through and creating their first models,
[2123.48 --> 2126.52]  they were almost certainly using transfer learning, even if they didn't realize it.
[2126.52 --> 2132.48]  It's kind of the secret weapon of kind of getting yourself going.
[2132.88 --> 2137.68]  And it's probably almost always used in certain types of use cases, such as computer vision.
[2138.56 --> 2142.58]  And as we get into defining what it is, it'll become apparent why.
[2143.18 --> 2150.58]  Yeah, and it's definitely impacted the natural language processing or NLP community very heavily.
[2151.24 --> 2154.66]  And there's been a lot of efforts in that direction recently.
[2154.66 --> 2163.52]  I know on one of our very first episodes, we had the guys from Machine Box on the episode.
[2164.02 --> 2165.00]  Yeah, that was episode two.
[2165.00 --> 2165.72]  Was that the first?
[2165.90 --> 2167.08]  Oh, it was episode two.
[2167.16 --> 2168.18]  The first one with guests.
[2168.44 --> 2169.44]  It was the first one with guests.
[2169.54 --> 2169.92]  That's correct.
[2170.22 --> 2170.40]  Yeah.
[2170.54 --> 2177.14]  So Machine Box has this really great service that you can spin up that will do facial recognition.
[2177.14 --> 2183.08]  And really, all you have to give it is like one or two images of a person's face.
[2183.20 --> 2188.94]  And it automatically kind of updates the model and does really great facial recognition.
[2189.74 --> 2196.14]  And of course, it's not just utilizing one or two images and training a whole neural network on two images.
[2196.54 --> 2198.46]  That just wouldn't work.
[2198.46 --> 2201.72]  So there's something else being leveraged under the hood.
[2202.30 --> 2211.64]  And as Chris mentioned, in that computer vision context or NLP, a lot of times that thing is transfer learning.
[2211.86 --> 2216.46]  So at a high level, how do you think about transfer learning, Chris?
[2216.46 --> 2226.70]  So the way I think about it is when you're creating a model, you don't just go and do it and it's done.
[2226.92 --> 2228.70]  It is an iterative process.
[2228.98 --> 2236.50]  And so kind of going back to the basics of what deep learning is, what a deep neural network is, is you have a series of layers.
[2236.50 --> 2243.04]  And each of those layers is responsible for generalizing something, understanding something.
[2243.64 --> 2245.58]  And they tend to build on themselves.
[2245.58 --> 2254.34]  So in the context, to make it real, of computer vision, you may have a deep neural network.
[2254.60 --> 2263.32]  And the early layers are there to recognize just simple things like lines or corners and things like that.
[2263.38 --> 2271.28]  And you tend to build those features up to where now it recognizes, after it combines some of those together, what lips look like or what an eye looks like.
[2271.28 --> 2279.38]  And then, you know, you go up a little bit and it starts to recognize how you put those different features together and make it a face and, you know, and then a full head.
[2279.78 --> 2282.34]  And so each one builds upon the other.
[2282.34 --> 2295.68]  So the really cool thing about this is, let's say that you need to go recognize something and maybe some of those baseline features, like recognizing at the lowest level, recognizing lines and curves and such.
[2295.90 --> 2298.14]  Obviously, in every image, you're going to do that.
[2298.14 --> 2308.24]  So if you have a model that's really good at doing that already, taking that, and if it's getting close to human recognition or maybe animals or certain common objects, you can move higher up the stack.
[2308.24 --> 2320.04]  And then at whatever point the purpose of that preexisting model might diverge from yours, you can take those layers that were consistent with what you're trying to achieve and build upon those.
[2320.42 --> 2337.64]  And since they were built with a general data set that is different from the data that you're about to train it on, your new model is more likely to generalize better as well, since you have a more diverse data set by definition, since you have pulled in a partially trained model from somebody else's data set.
[2337.64 --> 2342.16]  And so it's kind of like we're all standing on the shoulders of giants.
[2342.36 --> 2349.82]  You build upon what other people have built and you can take that preexisting model that might work really well up to a point.
[2350.02 --> 2357.94]  And then you take your specific data with your specific data set, a set of images about something that you care about, and then fill that out.
[2357.94 --> 2365.66]  And you end up being able to get a very robust model that does something very useful with much, much less training.
[2365.96 --> 2369.92]  And it's a lot less brittle since it has a broader data set to base it on.
[2369.92 --> 2381.44]  It's kind of like, you know, most programmers don't write every single line of code from scratch when they're creating a new application.
[2381.70 --> 2386.10]  There's a lot of copy and paste that goes on because they've done this before.
[2386.22 --> 2387.40]  They've done that before.
[2387.40 --> 2392.70]  They've created this sort of service, and it just needs to be kind of slightly different this time around.
[2392.84 --> 2395.08]  And so they never start from scratch.
[2395.08 --> 2397.44]  They kind of copy a bunch of things over.
[2397.68 --> 2410.44]  It's very similar here in the sense that, like, yes, you can in many cases take a model that has not been trained on any data yet and train it to do a certain task.
[2410.44 --> 2414.78]  Let's say that we want to translate text from English to Hindi.
[2415.28 --> 2418.00]  So what we do is we get a parallel corpus.
[2418.00 --> 2425.30]  So we've got a bunch of examples of English phrases and then a bunch of examples of the corresponding Hindi translation of that.
[2425.82 --> 2433.90]  And we train a model on English to Hindi so that when we put in an English phrase, what we get out is the corresponding Hindi translation.
[2434.12 --> 2436.28]  So that's kind of like training from scratch.
[2436.40 --> 2443.08]  That would be like, you know, creating every in my in my analogy, creating every line of code from scratch.
[2443.08 --> 2449.90]  We're we're initializing all of the weights and the biases of our model of the parameters of our model from scratch.
[2449.90 --> 2455.30]  So from some random seed or all starting at zero or whatever that initialization is.
[2455.30 --> 2462.68]  But we're we're using that English to Hindi corpus to train all of those parameters of the model from scratch.
[2462.68 --> 2474.02]  Whereas now, let's say after we've done that, we don't want later on in our work, we don't want a model that is trained to translate English to Hindi.
[2474.02 --> 2477.28]  But we want English to Urdu, which is a related language.
[2478.10 --> 2482.32]  And, you know, this means that we could do one of two things.
[2482.32 --> 2497.02]  We could either get another huge corpus of like English to Urdu data and train from scratch again, or we could leverage the knowledge that we already that we already created in that English to Hindi model.
[2497.02 --> 2501.56]  So we could take that model and all of the weights and parameters that we trained for English to Hindi.
[2501.56 --> 2513.96]  And then we could just kind of slightly modify it or fine tune it by retraining those on the new data set, maybe a smaller amount of English to Urdu language.
[2514.08 --> 2523.14]  So this has been widely used in NLP because in a lot of cases, maybe you want to take a pre-trained model that's very general.
[2523.14 --> 2528.30]  So it's applied to maybe do translation for all domains.
[2528.46 --> 2537.84]  And you want to really fine tune that for a specific domain of text or of some content.
[2538.30 --> 2542.82]  And so what you'll do is you'll fine tune or slightly modify that on this new data set.
[2542.82 --> 2545.76]  So there's kind of this initial pre-trained model.
[2545.88 --> 2552.74]  And then there's the fine tuning of that pre-trained model on a new data set.
[2553.14 --> 2558.28]  So it could be on a new data set or you might fine tune it by kind of adding additional layers to it as well.
[2559.10 --> 2573.20]  So to kind of bring this back full circle on that, if any of our listeners have taken classes from, you know, maybe NVIDIA's Deep Learning Institute or maybe Coursera or whatever on specific things like NLP or computer vision or something,
[2573.20 --> 2584.04]  chances are in that class, one of the things you did when you started creating the models for your class was they would have you go in and select an architecture to base that on.
[2584.14 --> 2585.74]  And that itself is transfer learning.
[2585.74 --> 2594.46]  And you're going to find libraries of these models that are pre-trained that you can build upon in all the common frameworks out there.
[2594.58 --> 2595.58]  TensorFlow has them.
[2595.72 --> 2596.60]  PyTorch has them.
[2597.40 --> 2603.68]  It is truly the most common way, certainly to get started or to build upon.
[2603.68 --> 2615.38]  And I have, in my experience, I have more often than not seen people use transfer learning in their work than start from scratch and try to build things completely for the ground up.
[2615.42 --> 2619.16]  You would have to do that if there is not the right type of model that you can build upon.
[2619.66 --> 2621.78]  But this is normal stuff.
[2621.92 --> 2622.58]  This is what we do.
[2622.58 --> 2632.04]  And I thought your analogy, Daniel, in terms of using libraries, if you're a programmer, is, you know, you're truly using lots and lots of code that other people have built.
[2632.46 --> 2633.84]  Maybe a lot of that's open source.
[2634.02 --> 2635.02]  Maybe some of it's proprietary.
[2635.58 --> 2640.40]  But you're still using those APIs to build whatever thing you're building, whatever application you're building.
[2640.74 --> 2646.66]  And that's a fantastic analogy you gave on matching it up to transfer learning in ML.
[2646.66 --> 2653.78]  And another thing is, like, in a lot of cases, you may just not have access to the data that you need.
[2654.38 --> 2665.12]  So, for example, you know, you may not have access to the huge number of face images that someone else has trained a model, a facial recognition model on.
[2665.12 --> 2673.50]  So they might have, you know, 200 gigabytes of images that they trained their model on and you only have a handful.
[2673.50 --> 2677.98]  But that doesn't mean that you're kind of totally out of luck, right?
[2678.00 --> 2693.48]  Because a lot of people have released these sort of pre-trained models for facial recognition and other things to where, like we were talking earlier with Machine Box, you might just be able to utilize that pre-trained model and update it with a couple new images or a handful of new images.
[2693.48 --> 2709.52]  And, you know, that kind of removes the burden on you to gather all of these large sets of data, maintain them, update them over time, run really long jobs to train these models using GPUs, which is really expensive.
[2709.98 --> 2716.34]  And so it can also be kind of operational and cost saving strategy as well.
[2717.16 --> 2717.58]  Absolutely.
[2717.58 --> 2725.06]  So I've seen transfer learning in the news recently in a few different places.
[2725.40 --> 2735.84]  One of the places, as I was searching around in preparation for this episode, I saw a recent article from Forbes about Google's AutoML.
[2736.24 --> 2743.52]  It mentions actually transfer learning in that article, which, you know, I thought was reasonably technical for Forbes.
[2743.52 --> 2763.98]  But yeah, they talk about how Google's AutoML services are using transfer learning, leveraging transfer learning to allow people to create these sort of customized models, maybe for translation for their specific domain, like for law or for medicine or for, you know, customer service or something like that.
[2763.98 --> 2767.98]  So it's definitely being utilized in a lot of production services.
[2768.98 --> 2779.90]  Where else have you seen transfer learning kind of come into, you know, recent news or recent releases of things, Chris?
[2780.30 --> 2783.40]  Well, we've had several episodes that made reference.
[2783.40 --> 2789.16]  Some of the algorithms that we've talked about were BERT in episode 22.
[2789.48 --> 2793.76]  We talked about GPT-2 in episode 32.
[2794.58 --> 2798.54]  And those are models that you can build upon as well.
[2798.96 --> 2811.76]  And that's really, I think it's really important to note that this is kind of the standard way you start thinking about a problem is you go out and look and see if there is something out there that makes sense to build upon.
[2811.76 --> 2815.18]  And it's almost the route into machine learning today.
[2815.74 --> 2826.70]  And so a lot of these great institutions are, in fact, building things that all of us can then take it thereafter in the tool of whichever one we want to use and apply that.
[2827.16 --> 2833.28]  Yeah, I think the sort of BERT and GPT-2 and other large scale language models are good examples.
[2833.28 --> 2842.50]  So, for example, as we talked about BERT or GPT-2 and other episodes, you can basically take that pre-trained model.
[2842.68 --> 2852.82]  And in a lot of cases, how you would quote unquote fine tune it is by adding a layer that would do named entity recognition or adding a layer that would do text classification or something.
[2852.82 --> 2860.26]  And keeping all of that knowledge from the BERT or GPT-2 embeddings on the front end of your model.
[2860.38 --> 2869.64]  So you're kind of only adding or changing it a little bit, but you're kind of leveraging all of that knowledge that Google or OpenAI has already built into it for you.
[2869.64 --> 2884.74]  So a couple of things that I've seen even over the past couple of days, if you're looking to get hands on with transfer learning, there have been a couple of resources that have been published that I think are really great.
[2885.38 --> 2890.86]  So one of those is blog posts from the Hugging Face team.
[2890.86 --> 2895.46]  So if you remember on episode 35, we had Clem from Hugging Face on.
[2895.78 --> 2900.00]  He had some really interesting and fun stuff to talk about.
[2900.32 --> 2908.04]  But their team has released this tutorial on how to build a state-of-the-art conversational AI with transfer learning.
[2908.22 --> 2912.92]  And I think that builds on some of these large scale language models.
[2913.68 --> 2920.00]  And then even today, I just saw there was a NAACL workshop on transfer learning.
[2920.00 --> 2928.02]  So that's the computational linguistics conference that's happening, I think, even right now up in Minnesota.
[2929.28 --> 2942.12]  And there was a workshop there and they released all of the code and collab notebooks and information, I think, slides from that tutorial.
[2942.12 --> 2949.10]  So we'll make sure and link that in the show notes as well if you want to get hands on with transfer learning.
[2950.00 --> 2961.06]  But yeah, I think that so talking through these things with you, Chris, has definitely helped categorize some of these major components of AI methodologies.
[2961.06 --> 2964.30]  And in my mind, I hope it has for you as well.
[2964.80 --> 2965.46]  It definitely has.
[2965.56 --> 2968.66]  I hope that we get feedback from our listeners.
[2968.66 --> 2979.18]  That certainly, I know when we were talking about doing this before recording this episode, we were hoping that there might be some of the confusion out there that we could alleviate.
[2979.74 --> 2991.06]  And we would love to hear back from people through changelog.com slash community or on our LinkedIn group, which we invite people to join as well.
[2991.06 --> 2994.78]  You can find it out. You can search for Practical AI Podcast on LinkedIn and do that.
[2995.20 --> 2999.74]  But we'd love your feedback to know, you know, if these were helpful.
[3000.42 --> 3002.72]  Are there other specific questions we left unanswered?
[3002.80 --> 3005.60]  And are there other topics that you would like us to cover in future shows?
[3006.64 --> 3009.74]  Awesome. Well, thanks for thanks for talking through these things with me, Chris.
[3009.74 --> 3014.38]  And I'll look forward to hearing from our listeners out there of how they're using these techniques.
[3014.38 --> 3024.42]  And if we messed anything up or misspoke or if there's additional great resources that you know about on this front, please reach out.
[3024.60 --> 3028.54]  And we will talk with you again soon.
[3030.62 --> 3033.92]  All right. Thank you for tuning into this episode of Practical AI.
[3034.16 --> 3035.66]  If you enjoyed the show, do us a favor.
[3035.78 --> 3037.18]  Go on iTunes, give us a rating.
[3037.18 --> 3039.32]  Go in your podcast app and favorite it.
[3039.44 --> 3042.12]  If you are on Twitter or social network, share a link with a friend.
[3042.20 --> 3044.56]  Whatever you got to do, share the show with a friend if you enjoyed it.
[3044.86 --> 3047.52]  And bandwidth for changelog is provided by Fastly.
[3047.64 --> 3049.08]  Learn more at fastly.com.
[3049.26 --> 3052.46]  And we catch our errors before our users do here at changelog because of Rollbar.
[3052.70 --> 3055.10]  Check them out at rollbar.com slash changelog.
[3055.42 --> 3057.88]  And we're hosted on Linode cloud servers.
[3058.24 --> 3059.86]  Head to linode.com slash changelog.
[3059.96 --> 3061.30]  Check them out. Support this show.
[3061.68 --> 3064.92]  This episode is hosted by Daniel Whitenack and Chris Benson.
[3064.92 --> 3067.42]  The music is by Breakmaster Cylinder.
[3067.86 --> 3071.26]  And you can find more shows just like this at changelog.com.
[3071.46 --> 3073.38]  When you go there, pop in your email address.
[3073.68 --> 3079.70]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[3080.06 --> 3080.86]  Thanks for tuning in.
[3081.02 --> 3081.78]  We'll see you next week.
[3081.78 --> 3081.82]  We'll see you next week.
[3081.82 --> 3085.78]  We'll see you next week.
[3085.78 --> 3090.78]  We'll see you next week.
[3090.78 --> 3092.16]  We'll see you next week.
[3092.16 --> 3092.88]  We'll see you next week.
[3092.88 --> 3093.84]  We'll see you next week.
[3093.84 --> 3094.90]  We'll see you next week.
