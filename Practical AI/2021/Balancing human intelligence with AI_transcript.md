[0.00 --> 4.06]  With the podcast that we have here, we have the privilege of meeting and talking with
[4.06 --> 5.92]  lots and lots of amazing people.
[6.34 --> 11.52]  I find myself very interested when people reach out in conversation where they have
[11.52 --> 16.42]  a really meaningful need and they're solving it with AI because it's the right solution.
[17.20 --> 22.76]  And conversely, the conversations that I don't find myself really gravitating to are when
[22.76 --> 25.52]  people are trying to sell their stuff based on AI.
[26.16 --> 31.28]  And rather than talk about the problem they're solving and why that matters to people out
[31.28 --> 32.80]  there, it's all about the AI.
[32.96 --> 33.94]  Hey, we have AI now.
[34.06 --> 37.66]  And I think that goes back to the fact that no matter what your job is, no matter what
[37.66 --> 41.68]  your role in the world is, we're all productively trying to solve things that need solving.
[41.68 --> 47.32]  I think AI is fantastic, but it also needs to be the right thing to solve your particular
[47.32 --> 47.90]  problem.
[48.14 --> 53.50]  Whereas if it's just doing it because the marketing people say you need to do it, that's a good
[53.50 --> 55.22]  warning sign that you may be off track.
[55.52 --> 60.60]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[60.82 --> 61.56]  We love Linode.
[61.64 --> 63.04]  They keep it fast and simple.
[63.18 --> 65.54]  Check them out at linode.com slash changelog.
[65.76 --> 67.84]  Our bandwidth is provided by Fastly.
[68.18 --> 71.74]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[72.00 --> 73.72]  Get a demo at LaunchDarkly.com.
[73.72 --> 81.34]  SignalWire is real-time video tech to help you create interactive video experiences previously
[81.34 --> 82.00]  not possible.
[82.00 --> 88.32]  It gives you access to broadcast quality, ultra low latency video that's proven and trusted
[88.32 --> 91.48]  by Amazon, Ring Doorbell, Zoom, and others.
[91.82 --> 95.86]  See why the future of video communication is being built on SignalWire.
[95.86 --> 102.02]  They have easy to deploy APIs, SDKs for the most popular programming languages, and expert
[102.02 --> 105.48]  support from the OGs of software-defined telecom tech.
[105.90 --> 111.48]  Try it today at SignalWire.com and use code AI for $25 in developer credit.
[112.06 --> 114.10]  Just visit SignalWire.com.
[114.10 --> 118.48]  That's SignalWire.com and use code AI to receive that $25.
[119.06 --> 122.72]  Once again, that's SignalWire.com, code AI.
[132.10 --> 137.96]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[138.38 --> 139.30]  and accessible to everyone.
[139.62 --> 143.70]  This is where conversations around AI, machine learning, and data science happen.
[143.70 --> 148.44]  Join the community and Slack with us around various topics of the show at CaneJog.com slash
[148.44 --> 150.08]  community and follow us on Twitter.
[150.20 --> 151.80]  We're at Practical AI FM.
[157.70 --> 162.42]  Well, welcome to another fully connected episode of Practical AI.
[162.86 --> 168.94]  This is where we will keep you fully connected with everything that's happening in the AI community.
[168.94 --> 173.58]  We'll take some time to discuss some of the latest AI news and topics,
[173.84 --> 179.02]  and we'll dig into some learning resources to help you level up your machine learning game.
[179.58 --> 180.54]  I'm Daniel Whitenack.
[180.64 --> 183.64]  I'm a data scientist with SIL International,
[183.94 --> 187.02]  and I'm joined as always by my co-host, Chris Benson,
[187.28 --> 189.56]  who is a strategist at Lockheed Martin.
[189.82 --> 190.44]  How are you doing, Chris?
[190.64 --> 191.90]  Doing very well, Daniel.
[192.14 --> 194.46]  It's a nice fall weather has arrived.
[194.72 --> 196.54]  Yeah, it's rainy and gloomy here.
[196.54 --> 197.78]  Oh, I'm sorry, man.
[197.84 --> 199.26]  We've had a week of that.
[199.34 --> 200.00]  But it is cool.
[200.10 --> 200.54]  It's nice.
[200.86 --> 202.90]  It's not like an oven outside, which is good.
[203.10 --> 203.30]  True.
[203.64 --> 205.30]  So I'm enjoying the weather at this point.
[205.38 --> 207.22]  We've had a week of rain, and now it's...
[207.22 --> 212.22]  So we get to jump into some AI and sunshine, and we'll see how it goes.
[212.34 --> 213.22]  Yeah, that's good.
[213.90 --> 218.52]  You know, every week I introduce you as a strategist,
[218.78 --> 220.48]  and sometimes I'm thinking,
[221.10 --> 224.50]  what does a strategist do day to day?
[224.50 --> 226.80]  Maybe my question is more like,
[227.04 --> 230.58]  how is strategy developed at a large organization?
[230.74 --> 232.96]  And this is related to what we'll talk about today.
[233.10 --> 234.34]  But I'm just sort of curious,
[234.72 --> 239.88]  like how a large organization thinks about developing their strategy,
[239.88 --> 244.32]  maybe related to something like AI or a new advanced technology.
[244.54 --> 249.00]  What does the development of strategy look like at an organization?
[249.00 --> 256.30]  So I would say the short version of an answer is that organizations have needs,
[256.50 --> 259.18]  and those needs have to get solved.
[259.62 --> 263.04]  And most, as simple as that sounds,
[263.30 --> 267.24]  it is very common for people not to start and say,
[267.38 --> 268.68]  what is the need I have to solve?
[269.06 --> 272.48]  They say, I have this cool new technology, man.
[272.54 --> 273.38]  It's incredible.
[273.50 --> 274.26]  It's called AI.
[274.26 --> 276.84]  And it's, you know, all these awesome things.
[276.94 --> 279.02]  And we just need this in our product or service.
[279.16 --> 279.82]  It's amazing.
[280.14 --> 282.80]  And we call that an approach in the strategy world.
[282.90 --> 286.48]  It's, in other words, it is a solution in search of a problem.
[286.74 --> 290.68]  Yeah, it's something that could enable something, but it might just...
[290.68 --> 290.92]  Yeah.
[291.32 --> 292.46]  And here's the funny thing.
[292.48 --> 293.96]  If you think back through your career,
[294.10 --> 297.70]  I'll bet that 99% of your technology conversations
[297.70 --> 300.72]  where people are excited about the way forward
[300.72 --> 303.84]  start with them saying, I have this amazing thing.
[303.88 --> 304.92]  I'm so thrilled with it.
[305.16 --> 306.66]  And everyone will need one.
[306.66 --> 308.96]  If anyone tells you everyone will need this,
[309.22 --> 312.62]  that's a sure sign that you're starting in the wrong place.
[313.30 --> 314.20]  Everyone will need this.
[314.26 --> 316.96]  So you start with a need and you solve it with an approach.
[317.12 --> 318.64]  And that's how you get to a good answer
[318.64 --> 319.74]  instead of the other way around.
[319.82 --> 320.68]  So that's the short version.
[320.98 --> 325.92]  So are there tools or frameworks that you use?
[326.10 --> 329.54]  Maybe certain of these can't be revealed from your proprietary work,
[329.54 --> 331.74]  but are there like general tools or frameworks
[331.74 --> 335.74]  that you use in developing strategy?
[335.94 --> 339.14]  I know, for example, you gave a talk last week
[339.14 --> 341.00]  at an event that I was helping organize,
[341.14 --> 342.26]  which thank you for doing that.
[342.32 --> 343.28]  It was a wonderful talk.
[343.74 --> 345.72]  I think you mentioned some sort of frameworks
[345.72 --> 346.94]  that you think about.
[347.08 --> 349.18]  I'm always intrigued by the different ways
[349.18 --> 351.80]  people frame their strategy.
[352.02 --> 354.14]  What are some of those tools that you use?
[354.24 --> 355.38]  It's actually going to follow through
[355.38 --> 356.72]  on what I was just talking about
[356.72 --> 359.20]  is that a lot of approaches to strategy
[359.20 --> 360.94]  are incredibly complex.
[361.60 --> 364.12]  And because of that, no one sticks with it.
[364.22 --> 367.06]  There's a lot of, you know, mundane documentation and stuff.
[367.46 --> 370.14]  There's a really simple framework that I use as baseline.
[370.28 --> 371.56]  And we'll build around that
[371.56 --> 373.50]  as we need for specific business cases.
[373.78 --> 375.36]  It's called NABC,
[375.62 --> 378.58]  which is need approach benefit competition,
[378.58 --> 380.12]  where you start with a need
[380.12 --> 382.44]  and you're looking at what are all the possible approaches.
[382.68 --> 384.34]  In this case, they may be AI approaches.
[384.34 --> 388.64]  And then you figure out how those benefit a solution.
[388.94 --> 390.58]  And there may be a lot of options there
[390.58 --> 392.00]  and what the competition is between them.
[392.04 --> 393.74]  And you try to get to an honest answer.
[394.44 --> 396.52]  And that very, very simple framework
[396.52 --> 398.30]  is how I start my thinking around it.
[398.68 --> 400.88]  And then we do have various proprietary,
[401.08 --> 402.46]  you know, business specific frameworks.
[402.46 --> 404.38]  But I always come back to that
[404.38 --> 406.66]  because it's so simple that it's hard to go wrong
[406.66 --> 407.52]  if you keep it in your brain.
[407.84 --> 407.96]  Yeah.
[408.12 --> 409.44]  And this gets, I mean,
[409.44 --> 410.74]  on these fully connected episodes,
[410.74 --> 413.60]  we're always talking about maybe the latest AI news
[413.60 --> 415.96]  or a new capability that comes out
[415.96 --> 419.84]  or a new type of method or new data.
[420.34 --> 423.08]  And definitely those things
[423.08 --> 426.18]  separate from like a strategic mindset.
[426.18 --> 427.68]  I mean, in the very least,
[427.70 --> 429.88]  they could not bring value, right?
[429.92 --> 431.88]  In the very most, maybe they bring harm
[431.88 --> 434.06]  if they're sort of misapplied.
[434.38 --> 434.46]  Yeah.
[434.96 --> 437.08]  Suboptimal outcomes are incredibly common.
[437.38 --> 439.10]  And so even if it's a simple framework,
[439.10 --> 440.48]  it takes a lot of discipline.
[441.00 --> 442.80]  You'll put something like that out there
[442.80 --> 444.66]  and people will kind of nod and go,
[444.74 --> 446.64]  yeah, yeah, nice, simple four-letter acronym.
[446.74 --> 447.16]  I got it.
[447.18 --> 447.92]  And they move on.
[448.26 --> 450.50]  But then they go do the wrong thing right after that.
[450.76 --> 450.92]  Yeah.
[450.96 --> 451.88]  And you're like, no, no,
[452.18 --> 453.78]  we're going to come back and solve the need
[453.78 --> 456.36]  that we actually have identified and is validated.
[456.58 --> 456.80]  Yeah.
[456.90 --> 457.84]  And that's hard to do.
[457.84 --> 460.32]  It's deceptively simple in speaking it.
[460.66 --> 460.78]  Yeah.
[460.94 --> 465.20]  And I think that maybe a lot of the conversation
[465.20 --> 467.88]  and blog posts or like conversations I've had
[467.88 --> 469.12]  have been centered around,
[469.46 --> 471.94]  can we justify the use of AI here?
[471.94 --> 475.86]  Or is AI the strategic choice for this application
[475.86 --> 477.76]  for X, Y, Z reason?
[478.02 --> 478.88]  But I think that,
[479.08 --> 482.34]  so something happened actually earlier today
[482.34 --> 483.80]  in my own work,
[483.80 --> 487.26]  where someone asked me to do a bit of analysis
[487.26 --> 492.28]  of the polarity or the balancing of two things,
[492.48 --> 494.70]  human intelligence and artificial intelligence.
[494.70 --> 497.50]  And I thought this was an interesting question
[497.50 --> 500.46]  that maybe I hadn't fully thought through yet,
[500.58 --> 502.64]  which is not so much like,
[502.92 --> 506.36]  is AI going to bring value for a particular solution?
[506.80 --> 511.60]  But how do you weave together human intelligence
[511.60 --> 514.80]  and human expertise with artificial intelligence
[514.80 --> 518.28]  and balance those two in a good way
[518.28 --> 519.98]  for your organization
[519.98 --> 522.78]  or for your particular problem that you're looking at?
[522.78 --> 525.32]  So that's what I was maybe going to bring up today.
[525.44 --> 527.70]  Would you be interested in kind of going through
[527.70 --> 528.82]  that exercise with me,
[528.90 --> 530.64]  helping me in my homework assignment?
[531.00 --> 531.30]  Absolutely.
[531.56 --> 534.24]  But I feel since you have taken me down this path,
[534.28 --> 535.86]  I feel obligated to point out
[535.86 --> 538.70]  that we're kind of starting with an approach there.
[538.82 --> 540.60]  So maybe we pick a use case
[540.60 --> 543.50]  and we kind of talk our way through that use case
[543.50 --> 544.98]  because then we have a validated need
[544.98 --> 546.14]  to have context for it.
[546.30 --> 546.40]  Sure.
[546.74 --> 547.84]  So, yeah, I mean,
[547.88 --> 548.88]  I think in general,
[548.88 --> 550.72]  we could use the use case,
[550.84 --> 552.62]  which is definitely the case in,
[553.04 --> 553.78]  although we're talking
[553.78 --> 555.24]  in a little bit more specifics
[555.24 --> 557.62]  on the project that I work on,
[558.08 --> 561.76]  we're generally talking about the application of AI
[561.76 --> 564.00]  in local language context.
[564.66 --> 567.22]  So let's say there's languages
[567.22 --> 571.52]  where something like chat, dialogue technology,
[571.98 --> 573.68]  sort of like named entity recognition,
[573.90 --> 574.58]  sentiment analysis,
[574.58 --> 576.50]  that sort of stuff isn't being applied yet.
[576.50 --> 578.40]  Maybe it's machine translation,
[578.66 --> 581.06]  which doesn't support these local languages yet.
[581.52 --> 582.66]  Maybe it's speech recognition.
[583.16 --> 586.84]  The premise is that the local language community
[586.84 --> 591.48]  would benefit from these types of technologies
[591.48 --> 594.38]  being extended to support their languages,
[594.38 --> 598.48]  but also that the AI community at large
[598.48 --> 601.88]  would benefit from local language communities
[601.88 --> 604.56]  actually being part of that
[604.56 --> 606.68]  natural language processing conversation
[606.68 --> 607.92]  in a wider way.
[608.04 --> 609.26]  So that's the sort of context
[609.26 --> 609.88]  that we're working in
[609.88 --> 611.94]  is this sort of AI technology.
[611.94 --> 614.88]  Should it be applied to do things?
[614.98 --> 616.10]  We can kind of scope it down.
[616.20 --> 618.24]  Should AI technology be applied
[618.24 --> 620.86]  to support machine translation
[620.86 --> 623.52]  for all these local languages
[623.52 --> 624.90]  or speech recognition
[624.90 --> 626.22]  for all these local languages
[626.22 --> 627.86]  where it's not currently supported?
[628.04 --> 628.76]  How does that work?
[628.88 --> 630.32]  Putting your strategist hat on.
[630.64 --> 631.84]  So I think it really depends
[631.84 --> 633.38]  on the stakeholder up front
[633.38 --> 635.58]  in that if you're an organization,
[636.00 --> 637.76]  either a commercial or a nonprofit,
[637.98 --> 639.52]  a not-for-profit organization,
[639.52 --> 640.00]  either way,
[640.44 --> 642.32]  then there is a mission,
[642.56 --> 643.26]  there's an objective
[643.26 --> 644.48]  that your organization has,
[644.58 --> 645.84]  and you have to figure out
[645.84 --> 647.52]  whether that use case is going to fit in.
[647.72 --> 651.20]  If you are a large internet-based company,
[651.34 --> 651.60]  you know,
[651.68 --> 653.36]  and without getting into specific names,
[653.86 --> 655.28]  and those in us,
[655.48 --> 657.22]  a significant proportion of your users
[657.22 --> 658.30]  are in those local languages,
[658.66 --> 659.78]  it would make sense for you,
[659.84 --> 661.02]  but it would not make sense
[661.02 --> 661.92]  for you necessarily,
[661.92 --> 662.92]  but it might make sense
[662.92 --> 664.28]  for another organization
[664.28 --> 666.12]  that is trying to help that.
[666.22 --> 667.16]  So what I'm saying is
[667.16 --> 668.24]  there's a cost to be born,
[668.36 --> 669.22]  and you have to figure out
[669.22 --> 670.40]  where the cost should be born
[670.40 --> 672.40]  so that you can serve all users well.
[672.66 --> 673.96]  And so I think there's room
[673.96 --> 676.30]  for everyone in getting in on that.
[676.58 --> 677.40]  You just have to figure out
[677.40 --> 678.14]  where that goes.
[678.50 --> 679.44]  Yeah, and I mean,
[679.46 --> 680.66]  you could think of a scenario
[680.66 --> 682.30]  like the most glaring one
[682.30 --> 684.40]  that we had recently with COVID
[684.40 --> 686.74]  and this sort of massive need
[686.74 --> 688.38]  for around the world,
[689.38 --> 690.70]  rapid translation
[690.70 --> 692.68]  of COVID-related information
[692.68 --> 694.32]  into as many languages
[694.32 --> 696.76]  as we could get it into.
[697.04 --> 697.24]  Yep.
[697.34 --> 700.36]  Because there was an immediate need.
[700.62 --> 701.86]  Now the question comes up,
[701.98 --> 705.16]  well, what role does AI play in that?
[705.32 --> 706.72]  And how is it balanced
[706.72 --> 708.26]  with human intelligence
[708.26 --> 711.12]  in the solution to that problem?
[711.52 --> 713.14]  What are the advantages of one
[713.14 --> 715.14]  and the disadvantages of the other
[715.14 --> 716.94]  and how should they be balanced together?
[717.48 --> 719.06]  The specific thing
[719.06 --> 721.66]  that came across my desk today
[721.66 --> 725.08]  was this idea of a polarity mapping,
[725.62 --> 726.42]  which I kind of like
[726.42 --> 727.64]  because my background's in physics.
[727.64 --> 729.54]  So anything with polarity
[729.54 --> 730.82]  is probably okay.
[731.36 --> 733.40]  I just chatted you a link to that
[733.40 --> 735.14]  and we'll link it in our show notes.
[735.32 --> 737.02]  But there's this sort of
[737.02 --> 737.98]  what I would consider
[737.98 --> 739.36]  a goofy looking picture.
[739.74 --> 740.94]  But there's this framework,
[741.04 --> 742.68]  a framework for tracking
[742.68 --> 743.78]  this sort of problem.
[744.12 --> 746.36]  I guess according to this wiki article,
[746.36 --> 748.38]  it was created by Barry Johnson,
[748.60 --> 749.90]  who I don't know who that is.
[750.06 --> 750.44]  I don't either.
[750.66 --> 751.24]  Barry Johnson.
[751.46 --> 753.14]  There's probably a million Barry Johnsons.
[753.38 --> 754.34]  But Barry Johnson.
[754.98 --> 757.54]  And it was created to help problems
[757.54 --> 758.62]  be solved in a realistic
[758.62 --> 760.32]  and multidimensional manner.
[761.02 --> 761.48]  Now, normally,
[761.64 --> 763.02]  because I'm a practical person
[763.02 --> 764.80]  and I like to spend most of my time
[764.80 --> 766.68]  in VIM and, you know,
[766.76 --> 768.50]  in a collab notebook or something,
[768.50 --> 770.60]  I really sort of cringe
[770.60 --> 772.00]  when I see these kind of
[772.00 --> 773.54]  like innovation frameworks
[773.54 --> 775.44]  or innovation map type things.
[775.56 --> 776.50]  They sort of like,
[776.60 --> 777.02]  I don't know,
[777.22 --> 778.70]  they give me a bad feeling right away.
[778.94 --> 779.80]  Hey, I'm a strategist
[779.80 --> 781.10]  and they give me a bad feeling too.
[781.24 --> 782.00]  So I'm right there with you.
[782.22 --> 783.18]  They're also like,
[783.26 --> 784.64]  I mean, it's kind of a goofy picture.
[784.80 --> 785.84]  It almost looks like
[785.84 --> 789.20]  maybe what Prince would have
[789.20 --> 791.34]  on some of his like stage art
[791.34 --> 792.60]  at a show or something.
[792.72 --> 793.18]  I don't know.
[793.40 --> 794.06]  With lasers.
[794.16 --> 795.10]  You have to have lasers.
[795.10 --> 796.26]  Yeah, maybe.
[797.20 --> 799.72]  So the idea of the picture,
[800.00 --> 800.68]  I think,
[800.82 --> 802.78]  is there's like these four quadrants
[802.78 --> 803.82]  and you can follow up
[803.82 --> 804.68]  in the show notes.
[804.80 --> 806.74]  But the idea is that
[806.74 --> 808.56]  sort of on one side,
[809.00 --> 810.40]  you've got human intelligence.
[810.84 --> 811.96]  It's really a framework
[811.96 --> 813.16]  for comparing two things.
[813.18 --> 813.82]  But on one side,
[813.88 --> 815.44]  you've got maybe human intelligence.
[815.90 --> 816.82]  And then on the other side,
[816.86 --> 818.16]  you've got artificial intelligence.
[818.52 --> 820.70]  And then what you would want to do
[820.70 --> 824.44]  is think about the positive results
[824.44 --> 826.70]  and the negative results from each
[826.70 --> 828.68]  or like the pros and cons of each.
[828.82 --> 831.44]  And then in looking at the pros and cons
[831.44 --> 832.36]  of each of those,
[832.80 --> 834.60]  think about the action steps
[834.60 --> 835.76]  and warning signs
[835.76 --> 837.88]  when they aren't in balance
[837.88 --> 840.96]  or how you can keep them in balance.
[840.96 --> 841.98]  Because we're assuming
[841.98 --> 843.70]  that both will play a role.
[844.24 --> 845.28]  So in our context,
[845.38 --> 846.60]  like in the machine translation
[846.60 --> 847.92]  of COVID information
[847.92 --> 848.90]  into local languages,
[849.60 --> 851.80]  how does human intelligence play a role?
[852.04 --> 854.04]  How does artificial intelligence play a role?
[854.44 --> 856.38]  And when and how would we know
[856.38 --> 858.34]  if one is out of balance
[858.34 --> 860.10]  in comparison to the other one?
[860.32 --> 861.44]  So does the premise make sense?
[861.70 --> 862.66]  The premise makes sense.
[862.80 --> 864.72]  And I think it's an interesting topic
[864.72 --> 866.46]  that I think is very relevant to our future.
[866.60 --> 867.38]  Yeah, definitely.
[867.68 --> 868.00]  Definitely.
[868.58 --> 870.38]  So maybe we'll talk about,
[870.58 --> 873.06]  let's think about the values
[873.06 --> 874.82]  of each of these first.
[875.24 --> 877.66]  So on the top of these quadrants,
[878.22 --> 880.50]  what they have the user of this framework do
[880.50 --> 882.28]  is think about the values,
[882.28 --> 883.08]  which they've labeled
[883.08 --> 884.62]  as the positive results
[884.62 --> 886.20]  from focusing on,
[886.64 --> 887.98]  and then you fill in the blank
[887.98 --> 889.40]  with whichever one you're thinking about,
[889.46 --> 890.14]  human intelligence
[890.14 --> 891.14]  or artificial intelligence.
[891.26 --> 893.54]  So what are some positive results
[893.54 --> 895.36]  from focusing on human intelligence
[895.36 --> 897.72]  when you're trying to solve this problem
[897.72 --> 899.20]  of machine translation
[899.20 --> 900.32]  into a local language?
[900.90 --> 901.46]  What do you think?
[901.74 --> 902.30]  Any ideas?
[902.72 --> 904.12]  The target, if you will,
[904.22 --> 905.70]  of what you're trying to accomplish
[905.70 --> 906.40]  is a human.
[906.40 --> 909.10]  And so having a human involved
[909.10 --> 911.74]  automatically allows you to connect.
[912.04 --> 913.64]  There's a whole bunch of problems
[913.64 --> 915.22]  that just don't exist.
[915.94 --> 917.96]  And you get the benefit of us
[917.96 --> 919.06]  complicated humans
[919.06 --> 920.54]  in terms of not only do you get
[920.54 --> 921.62]  the benefit of communication
[921.62 --> 922.46]  and understanding,
[922.72 --> 923.90]  but things like empathy.
[924.42 --> 926.76]  And there's huge value in that.
[927.20 --> 927.38]  Yeah.
[927.58 --> 930.28]  So a human is the target
[930.28 --> 931.46]  of this technology.
[931.46 --> 932.96]  So that's definitely good
[932.96 --> 934.82]  to keep in mind.
[934.82 --> 937.06]  I think like you were talking about earlier,
[937.82 --> 940.52]  we can get enamored by the tech, right?
[940.64 --> 940.82]  Yes.
[940.86 --> 941.64]  And think about like,
[941.90 --> 943.84]  this is a cool solution to a thing,
[943.96 --> 946.00]  but ultimately a human's
[946.00 --> 948.36]  going to interact with it, right?
[948.46 --> 948.78]  Absolutely.
[948.98 --> 949.72]  So I don't know.
[949.82 --> 951.12]  Do you think about that
[951.12 --> 953.06]  like term of like empathy
[953.06 --> 955.12]  when you're thinking about strategy?
[955.28 --> 956.80]  I've heard that term thrown around.
[957.06 --> 957.46]  I do.
[957.46 --> 959.66]  So not everyone does think that way,
[959.76 --> 961.02]  but it is value.
[961.64 --> 962.58]  And the older I get,
[962.64 --> 964.04]  the more I care about that.
[964.04 --> 965.16]  Most problems,
[965.30 --> 966.28]  there's the basic problem
[966.28 --> 967.20]  and there's a whole bunch
[967.20 --> 969.66]  of surrounding concerns around that.
[969.90 --> 971.30]  And you have to figure out
[971.30 --> 972.04]  what you're going to address.
[972.16 --> 973.04]  So for me,
[973.16 --> 974.96]  I see benefit to there.
[974.96 --> 991.48]  ChangeLog News is the best way
[991.48 --> 994.14]  to keep up with the fast moving software world.
[994.14 --> 995.22]  We track,
[995.56 --> 995.96]  log,
[996.08 --> 997.30]  and contextualize
[997.30 --> 998.52]  the coolest projects,
[998.82 --> 999.72]  the best practices,
[1000.10 --> 1001.18]  and the biggest stories
[1001.18 --> 1002.50]  each and every week.
[1002.50 --> 1004.20]  Make ChangeLog.com
[1004.20 --> 1005.30]  your daily destination
[1005.30 --> 1006.66]  or hit the snooze button
[1006.66 --> 1008.46]  and subscribe to our weekly newsletter
[1008.46 --> 1009.62]  that hits inboxes
[1009.62 --> 1010.64]  on Sunday mornings.
[1011.24 --> 1012.92]  Join more than 15,000
[1012.92 --> 1014.18]  enthusiastic readers.
[1014.46 --> 1016.16]  It'll cost you exactly $0
[1016.16 --> 1018.34]  and you can subscribe right now
[1018.34 --> 1019.66]  at ChangeLog.com
[1019.66 --> 1020.60]  slash weekly.
[1020.60 --> 1034.26]  So Chris,
[1034.32 --> 1035.28]  I think you brought up
[1035.28 --> 1037.76]  a couple of interesting things
[1037.76 --> 1040.44]  related to the positive results
[1040.44 --> 1043.00]  from focusing on human intelligence
[1043.00 --> 1045.28]  to solve the hypothetical problem
[1045.28 --> 1045.86]  we're considering.
[1046.18 --> 1047.84]  So humans being the target,
[1047.84 --> 1050.90]  it sort of breeds trust maybe.
[1051.06 --> 1051.62]  So I'm going to bring up
[1051.62 --> 1052.28]  the word trust.
[1052.42 --> 1053.40]  It maybe brings trust
[1053.40 --> 1056.18]  when a human does the thing.
[1056.30 --> 1058.28]  So like if I'm translating material
[1058.28 --> 1059.24]  about COVID
[1059.24 --> 1060.96]  into a local language,
[1060.96 --> 1062.16]  if I have a human
[1062.16 --> 1063.92]  that does that translation,
[1064.40 --> 1066.46]  maybe there's more trust there.
[1066.60 --> 1066.96]  I don't know.
[1067.02 --> 1067.54]  Would you agree?
[1067.92 --> 1068.76]  I think it would be
[1068.76 --> 1070.10]  a fair statement to say
[1070.10 --> 1072.24]  most people are able
[1072.24 --> 1073.66]  to connect with other humans
[1073.66 --> 1075.18]  long before they connect
[1075.18 --> 1076.34]  with a particular technology.
[1076.34 --> 1078.00]  There's an adjustment period
[1078.00 --> 1080.04]  to new technologies being accepted.
[1080.50 --> 1081.08]  We've seen that
[1081.08 --> 1082.68]  in many, many cases
[1082.68 --> 1084.74]  of technology release
[1084.74 --> 1086.08]  and development over the years.
[1086.30 --> 1088.04]  And so that's a big concern.
[1088.32 --> 1089.14]  You can look back
[1089.14 --> 1090.32]  and say kind of the classical
[1090.32 --> 1092.04]  my grandmother doesn't know
[1092.04 --> 1092.90]  how to use a cell phone
[1092.90 --> 1093.70]  kind of context.
[1093.88 --> 1096.12]  So yes, you are circumventing
[1096.12 --> 1097.30]  a whole set of issues
[1097.30 --> 1099.70]  and by taking advantage
[1099.70 --> 1101.04]  of the fact that you inherently
[1101.04 --> 1102.44]  will probably have trust
[1102.44 --> 1103.82]  with the human to human contact.
[1103.82 --> 1106.18]  And the other thing you mentioned,
[1106.42 --> 1108.72]  I think is maybe related
[1108.72 --> 1110.64]  to like flexibility
[1110.64 --> 1112.30]  or adaptation.
[1112.30 --> 1113.70]  So like a human,
[1114.14 --> 1115.20]  we're used to adapting
[1115.20 --> 1117.30]  to all sorts of situations, right?
[1117.42 --> 1118.02]  But generally,
[1118.58 --> 1119.68]  like an AI model
[1119.68 --> 1121.04]  for machine translation,
[1121.52 --> 1122.18]  there are good
[1122.18 --> 1123.46]  general purpose models,
[1123.66 --> 1124.56]  but oftentimes
[1124.56 --> 1126.02]  there are certain domains.
[1126.02 --> 1126.82]  Like if we think about
[1126.82 --> 1128.14]  this domain of translation
[1128.14 --> 1129.28]  of COVID material,
[1129.78 --> 1131.26]  there's really not that much
[1131.26 --> 1134.00]  in public corpora out there,
[1134.12 --> 1134.80]  public data
[1134.80 --> 1136.14]  that is representative
[1136.14 --> 1138.68]  of COVID type of information.
[1138.88 --> 1140.80]  And so machine translation model
[1140.80 --> 1142.42]  might just simply not know
[1142.42 --> 1144.38]  that domain of translation,
[1144.68 --> 1146.36]  whereas it's maybe fairly easy
[1146.36 --> 1148.64]  for a human to adapt
[1148.64 --> 1150.42]  to translating COVID information
[1150.42 --> 1153.60]  in a very quick period of time.
[1153.74 --> 1155.36]  So we're adaptable, I guess.
[1155.76 --> 1156.12]  Absolutely.
[1156.32 --> 1156.62]  I agree.
[1156.92 --> 1158.04]  Now, depending on,
[1158.24 --> 1158.74]  and this is,
[1158.94 --> 1159.20]  of course,
[1159.20 --> 1160.42]  there's a whole range
[1160.42 --> 1161.22]  of philosophical
[1161.22 --> 1164.06]  and religious positions on this,
[1164.12 --> 1165.30]  but at least I would argue
[1165.30 --> 1166.62]  that humans,
[1166.74 --> 1168.22]  as opposed to machines,
[1168.46 --> 1169.30]  like there's a difference
[1169.30 --> 1170.94]  between humans and machines.
[1171.38 --> 1172.68]  Now, like I say,
[1172.76 --> 1173.92]  depending on your worldview,
[1173.92 --> 1175.34]  you might think of that
[1175.34 --> 1177.08]  in different ways,
[1177.08 --> 1179.10]  but I think we could probably
[1179.10 --> 1180.68]  all agree on the fact
[1180.68 --> 1183.08]  that at least today's machines
[1183.08 --> 1185.94]  have a very task-focused
[1185.94 --> 1188.80]  way of solving problems
[1188.80 --> 1193.62]  and humans have a natural creativity,
[1194.36 --> 1196.32]  productivity, adaptation.
[1197.08 --> 1198.20]  There's a different element
[1198.20 --> 1200.74]  about how they solve a problem
[1200.74 --> 1202.90]  as opposed to a machine.
[1203.06 --> 1203.50]  So I don't know
[1203.50 --> 1204.36]  if that's creativity
[1204.36 --> 1205.64]  in addition to adaptation.
[1205.94 --> 1206.30]  I don't know
[1206.30 --> 1207.16]  if you have thoughts there.
[1207.40 --> 1208.44]  I think that's right on
[1208.44 --> 1209.74]  is it's the complexity
[1209.74 --> 1211.28]  inherent in the human mind
[1211.28 --> 1213.04]  that allows for the adaptation
[1213.04 --> 1215.08]  and in many cases for those,
[1215.34 --> 1217.02]  it makes those interactions interesting.
[1217.62 --> 1219.08]  I mean, a good example of that
[1219.08 --> 1220.84]  is if you look at humor
[1220.84 --> 1222.16]  that's machine-generated
[1222.16 --> 1223.66]  as of today in 2021,
[1224.18 --> 1225.46]  I've yet to find a source
[1225.46 --> 1226.14]  that I find funny,
[1226.22 --> 1226.84]  and yet you and I
[1226.84 --> 1227.80]  can have a conversation.
[1228.46 --> 1229.14]  Neither one of us
[1229.14 --> 1230.30]  is a professional comedian,
[1230.54 --> 1231.82]  despite evidence possibly
[1231.82 --> 1233.04]  to the contrary at times,
[1233.44 --> 1234.64]  but we have a good time.
[1234.72 --> 1235.52]  I'm definitely not.
[1235.54 --> 1237.70]  We can laugh at each other's jokes,
[1237.70 --> 1238.88]  and that's something
[1238.88 --> 1240.06]  that's uniquely human
[1240.06 --> 1241.32]  at the moment at least.
[1241.62 --> 1243.06]  And yet on the other side,
[1243.22 --> 1244.32]  as you certainly know,
[1244.34 --> 1245.20]  and maybe some of our listeners,
[1245.30 --> 1245.92]  I recently got
[1245.92 --> 1247.12]  my private pilot's license,
[1247.40 --> 1248.60]  and I would argue
[1248.60 --> 1251.40]  that it's an incredibly manual,
[1251.56 --> 1253.28]  procedural thing to learn.
[1253.62 --> 1254.54]  And most pilots
[1254.54 --> 1255.80]  would probably disagree with me,
[1255.90 --> 1257.04]  but I actually think
[1257.04 --> 1258.90]  that technology can fly
[1258.90 --> 1260.58]  a lot better than we can.
[1260.64 --> 1261.82]  I know that I am prone
[1261.82 --> 1262.74]  to make small mistakes.
[1262.90 --> 1263.78]  Thankfully, they are small,
[1263.78 --> 1265.48]  but there's ways that
[1265.48 --> 1267.46]  by doing it very procedural,
[1267.58 --> 1268.26]  very task-oriented,
[1268.36 --> 1270.24]  that you have superior capabilities
[1270.24 --> 1271.30]  from technology.
[1271.70 --> 1273.28]  So I guess getting to that
[1273.28 --> 1274.42]  and thinking about
[1274.42 --> 1276.12]  the positive results
[1276.12 --> 1278.86]  from focusing on an AI approach
[1278.86 --> 1280.70]  to solving this
[1280.70 --> 1282.14]  machine translation problem,
[1282.40 --> 1283.76]  what comes to mind first?
[1283.94 --> 1284.54]  You'll have to give me
[1284.54 --> 1285.86]  an example to go for that.
[1286.00 --> 1287.94]  So like if we didn't have
[1287.94 --> 1289.46]  a human in the loop at all,
[1289.64 --> 1291.26]  and we had a great AI
[1291.26 --> 1293.06]  that could or we thought
[1293.06 --> 1294.40]  could solve this problem
[1294.40 --> 1295.46]  of machine translation
[1295.46 --> 1296.80]  of COVID information,
[1297.20 --> 1298.24]  what are the benefits
[1298.24 --> 1299.82]  of that AI solution
[1299.82 --> 1301.14]  in isolation
[1301.14 --> 1303.94]  with no sort of human expertise
[1303.94 --> 1305.36]  or intelligence infused?
[1305.64 --> 1306.68]  Once you've absorbed
[1306.68 --> 1307.88]  the cost of that,
[1308.16 --> 1309.12]  assuming for a moment,
[1309.24 --> 1310.06]  constant, you know,
[1310.12 --> 1311.40]  static model based on
[1311.40 --> 1311.80]  where you,
[1312.02 --> 1313.04]  what your development was,
[1313.48 --> 1315.42]  then you can deploy it at scale
[1315.42 --> 1317.36]  without incurring additional cost.
[1318.02 --> 1318.94]  And not only that,
[1319.02 --> 1319.52]  but you can,
[1319.68 --> 1320.40]  because of that,
[1320.46 --> 1321.98]  you can deploy it
[1321.98 --> 1323.02]  much more widespread.
[1323.34 --> 1324.50]  There's a very limited number
[1324.50 --> 1326.14]  of human translators out there.
[1326.34 --> 1327.90]  And so there are costs
[1327.90 --> 1329.04]  associated with that.
[1329.26 --> 1329.78]  And so,
[1330.18 --> 1331.14]  so long as you're willing
[1331.14 --> 1332.52]  to take the cost
[1332.52 --> 1333.54]  of the development
[1333.54 --> 1334.38]  into account
[1334.38 --> 1335.50]  and the cost of deployment
[1335.50 --> 1336.32]  into account,
[1336.82 --> 1337.98]  then you can scale
[1337.98 --> 1339.20]  a certain capability
[1339.20 --> 1340.74]  across a very wide
[1340.74 --> 1341.66]  group of users.
[1341.92 --> 1343.30]  And that's a huge benefit.
[1343.40 --> 1344.50]  I mean, that we see that
[1344.50 --> 1346.14]  in all sorts of business use cases.
[1346.40 --> 1346.48]  Yeah.
[1346.60 --> 1348.24]  And when I teach classes
[1348.24 --> 1348.82]  or workshops,
[1348.82 --> 1350.46]  normally the question comes up,
[1350.46 --> 1352.16]  like when is an AI solution
[1352.16 --> 1353.12]  appropriate
[1353.12 --> 1354.56]  or under what conditions?
[1354.56 --> 1355.26]  And generally,
[1355.26 --> 1356.50]  I do think about that
[1356.50 --> 1358.60]  in terms of two things.
[1358.66 --> 1359.58]  One is scale.
[1359.82 --> 1360.68]  Even if a human,
[1360.92 --> 1362.42]  which I think a human would
[1362.42 --> 1363.26]  in most cases,
[1363.56 --> 1364.72]  if they knew both languages,
[1364.72 --> 1366.44]  create a better translation.
[1366.66 --> 1368.52]  But if we have to translate
[1368.52 --> 1370.52]  four million sentences,
[1370.86 --> 1372.26]  the fact is that it just,
[1372.42 --> 1373.38]  it's going to take a human
[1373.38 --> 1374.92]  an incredible amount of time.
[1374.92 --> 1376.96]  And so there's a scale factor
[1376.96 --> 1379.40]  and then there's also a complexity
[1379.40 --> 1380.62]  of the problem factor.
[1380.80 --> 1382.42]  So like some problems
[1382.42 --> 1383.60]  just by their very nature,
[1383.70 --> 1384.96]  even if they're not at scale,
[1385.38 --> 1387.78]  are hard for a human to visualize.
[1388.10 --> 1389.62]  And maybe it's combining
[1389.62 --> 1391.00]  a bunch of sensor data
[1391.00 --> 1392.44]  from IoT devices
[1392.44 --> 1394.12]  to determine when anomalies
[1394.12 --> 1396.14]  are happening in a network
[1396.14 --> 1398.28]  or in a manufacturing system
[1398.28 --> 1398.60]  or something.
[1398.68 --> 1400.56]  Those are like really complex problems.
[1401.02 --> 1401.78]  It's hard for a human
[1401.78 --> 1403.76]  to actually parse
[1403.76 --> 1404.76]  all of that information
[1404.76 --> 1405.76]  and make a decision.
[1405.76 --> 1407.18]  Maybe they could retroactively,
[1407.36 --> 1407.96]  but in the moment,
[1408.08 --> 1408.58]  it's difficult.
[1408.82 --> 1410.40]  So there's the scale of complexity,
[1410.40 --> 1412.86]  but then also the scale of scale.
[1413.18 --> 1413.88]  I get what you're saying.
[1414.00 --> 1416.74]  I'll offer an alternative point
[1416.74 --> 1419.20]  on that one is in translation,
[1419.70 --> 1420.92]  if you're looking at
[1420.92 --> 1423.10]  that you have a string of words
[1423.10 --> 1424.12]  that you're trying to translate,
[1424.60 --> 1425.74]  there may be context
[1425.74 --> 1426.78]  around those words, though,
[1426.84 --> 1427.82]  that is not captured
[1427.82 --> 1428.68]  by the technology.
[1429.40 --> 1430.64]  If you're, you may be in a,
[1430.92 --> 1432.10]  we've all lived this pandemic
[1432.10 --> 1433.32]  the last couple of years.
[1433.32 --> 1434.10]  And, you know,
[1434.10 --> 1434.96]  there are all sorts
[1434.96 --> 1437.12]  of challenging situations
[1437.12 --> 1438.48]  that humans have to go through.
[1438.60 --> 1440.06]  And sometimes the human
[1440.06 --> 1441.20]  can take into account
[1441.20 --> 1442.08]  things outside
[1442.08 --> 1443.70]  the direct task at hand,
[1443.70 --> 1444.84]  which shape the world
[1444.84 --> 1445.90]  the entire interaction
[1445.90 --> 1446.76]  is happening within.
[1447.10 --> 1448.08]  You know, there's a trade-off
[1448.08 --> 1448.62]  either way.
[1448.92 --> 1449.48]  In this case,
[1449.58 --> 1450.50]  you just identified
[1450.50 --> 1452.24]  an excellent reason
[1452.24 --> 1453.42]  to apply technology.
[1453.42 --> 1454.72]  And then we also can turn around
[1454.72 --> 1455.62]  and say there's a great reason
[1455.62 --> 1456.66]  to have a human in the loop.
[1456.92 --> 1457.90]  So it kind of depends
[1457.90 --> 1458.84]  on how you want to value
[1458.84 --> 1459.78]  those different attributes.
[1459.78 --> 1460.14]  Yeah.
[1460.26 --> 1461.70]  I also think that
[1461.70 --> 1463.06]  if we think about
[1463.06 --> 1464.12]  the combination
[1464.12 --> 1466.12]  and maybe this is the,
[1466.32 --> 1468.54]  I don't know if it's a pure AI value,
[1468.74 --> 1470.54]  but there one feature
[1470.54 --> 1473.22]  of the AI side of things
[1473.22 --> 1475.36]  is that there are many processes
[1475.36 --> 1476.52]  where the combination
[1476.52 --> 1478.56]  of the AI model
[1478.56 --> 1479.54]  plus a human,
[1479.84 --> 1481.16]  so the human plus computer,
[1481.36 --> 1483.00]  is actually both faster
[1483.00 --> 1484.16]  and higher quality
[1484.16 --> 1485.16]  in its task
[1485.16 --> 1487.06]  than either one in isolation.
[1487.32 --> 1488.14]  And this has been true
[1488.14 --> 1489.52]  in like healthcare applications,
[1489.52 --> 1490.84]  where doctors
[1490.84 --> 1492.18]  are recognizing tumors
[1492.18 --> 1493.14]  or whatever it is.
[1493.66 --> 1495.08]  So there is this element
[1495.08 --> 1496.44]  of the two together
[1496.44 --> 1497.88]  can produce actually
[1497.88 --> 1499.48]  higher quality results
[1499.48 --> 1500.68]  than either one
[1500.68 --> 1501.50]  by themselves.
[1502.58 --> 1503.40]  In my industry,
[1503.40 --> 1504.40]  we have, I think,
[1504.42 --> 1505.48]  a unique term for that
[1505.48 --> 1505.96]  and that is
[1505.96 --> 1507.46]  manned-unmanned teaming
[1507.46 --> 1508.82]  is what we call it.
[1509.12 --> 1510.38]  We call it MOM-T.
[1510.64 --> 1512.44]  So there's a new acronym for you.
[1512.84 --> 1513.14]  Okay.
[1513.26 --> 1513.44]  Yeah.
[1513.44 --> 1513.90]  I'll make sure
[1513.90 --> 1514.98]  and fit that in
[1514.98 --> 1516.96]  at a few points.
[1517.02 --> 1517.74]  There are great outcomes
[1517.74 --> 1518.34]  that can be had
[1518.34 --> 1519.10]  by taking advantage
[1519.10 --> 1520.10]  of the strengths
[1520.10 --> 1520.76]  of both sides.
[1520.96 --> 1521.16]  Yeah.
[1521.30 --> 1522.04]  So actually,
[1522.10 --> 1523.20]  I think we've already
[1523.20 --> 1524.90]  sort of got into
[1524.90 --> 1526.56]  some of the downsides,
[1526.68 --> 1528.02]  but I think it is interesting
[1528.02 --> 1529.18]  to think about
[1529.18 --> 1531.32]  on both sides of things
[1531.32 --> 1532.60]  because a lot of times
[1532.60 --> 1533.68]  people think about
[1533.68 --> 1535.34]  the downsides of AI,
[1535.82 --> 1537.08]  like whether that be bias
[1537.08 --> 1537.54]  or whatever.
[1537.68 --> 1537.78]  Yeah.
[1537.78 --> 1541.12]  But what are the negative results
[1541.12 --> 1542.78]  from over-focusing
[1542.78 --> 1543.98]  on human intelligence
[1543.98 --> 1546.36]  rather than bringing in any AI?
[1546.68 --> 1547.40]  Right off the bat,
[1547.52 --> 1548.92]  the same thing you just mentioned
[1548.92 --> 1550.34]  applies to both sides
[1550.34 --> 1551.08]  and that's bias.
[1551.68 --> 1551.80]  Yeah.
[1551.90 --> 1553.08]  And we in data science
[1553.08 --> 1555.56]  tend to focus on bias
[1555.56 --> 1557.62]  in data and data processing,
[1557.84 --> 1558.20]  you know,
[1558.26 --> 1559.38]  when we're building models.
[1559.54 --> 1560.70]  But, oh boy,
[1560.82 --> 1561.48]  all you have to do
[1561.48 --> 1563.36]  is look at the last election cycle
[1563.36 --> 1564.54]  with humans
[1564.54 --> 1565.42]  and you see that
[1565.42 --> 1566.78]  we have the same faults
[1566.78 --> 1567.46]  in that way.
[1567.78 --> 1569.46]  So that's one right off the bat.
[1569.60 --> 1571.20]  Another one that you mentioned earlier
[1571.20 --> 1572.36]  was the fact that
[1572.36 --> 1573.40]  humans don't necessarily
[1573.40 --> 1575.56]  take all of the data in
[1575.56 --> 1577.54]  and give it all processing time
[1577.54 --> 1578.46]  before an output
[1578.46 --> 1579.30]  if you're looking at
[1579.30 --> 1579.96]  all these sensors
[1579.96 --> 1581.32]  that you mentioned earlier.
[1581.86 --> 1581.92]  Yeah.
[1582.02 --> 1582.72]  Some of the things
[1582.72 --> 1584.44]  that make us so strong
[1584.44 --> 1585.12]  in some areas
[1585.12 --> 1587.12]  make us terribly weak in others.
[1587.40 --> 1587.60]  Yeah.
[1587.80 --> 1588.64]  A human inference
[1588.64 --> 1589.58]  is very different
[1589.58 --> 1590.64]  from a computer inference
[1590.64 --> 1591.60]  and they both have
[1591.60 --> 1592.28]  strengths and weaknesses.
[1592.60 --> 1594.20]  One of the interesting thing
[1594.20 --> 1595.24]  about bias
[1595.24 --> 1596.46]  on the human side
[1596.46 --> 1597.24]  which someone
[1597.24 --> 1598.72]  my co-worker
[1598.72 --> 1600.46]  brought up to me today
[1600.46 --> 1601.58]  is he said
[1601.58 --> 1603.26]  on the human side
[1603.26 --> 1605.20]  biases are covered by shame.
[1605.74 --> 1606.36]  And I was like
[1606.36 --> 1607.58]  okay, well
[1607.58 --> 1608.54]  like unpack that
[1608.54 --> 1609.22]  a little bit for me.
[1609.32 --> 1610.40]  What do you mean by that?
[1610.76 --> 1613.02]  And he was basically saying
[1613.02 --> 1615.82]  people hide their mistakes, right?
[1616.12 --> 1617.84]  If you have a test set
[1617.84 --> 1619.08]  on the AI side
[1619.08 --> 1621.00]  like you can just count up
[1621.00 --> 1622.28]  how many you got wrong.
[1622.38 --> 1623.26]  Now there could be
[1623.26 --> 1624.42]  bias in that
[1624.42 --> 1625.42]  and you can actually
[1625.42 --> 1626.32]  measure it, right?
[1626.76 --> 1627.54]  But a human
[1627.54 --> 1628.70]  oftentimes
[1628.70 --> 1631.20]  either they subconsciously
[1631.20 --> 1632.22]  have a bias
[1632.22 --> 1633.32]  and it's hidden
[1633.32 --> 1634.16]  because they just
[1634.16 --> 1634.78]  don't even know
[1634.78 --> 1635.58]  that they have it
[1635.58 --> 1636.40]  or
[1636.40 --> 1638.06]  they do know
[1638.06 --> 1639.18]  that they have a bias
[1639.18 --> 1640.66]  and they intentionally
[1640.66 --> 1642.74]  try to hide it, right?
[1642.80 --> 1643.04]  Yes.
[1643.04 --> 1643.58]  Which is maybe
[1643.58 --> 1645.60]  a more interesting situation.
[1645.84 --> 1646.58]  So when a human
[1646.58 --> 1647.42]  makes a mistake
[1647.42 --> 1648.50]  they generally like people
[1648.50 --> 1649.02]  to know
[1649.02 --> 1650.12]  that they didn't
[1650.12 --> 1650.80]  make the mistake.
[1650.80 --> 1651.80]  So it's really hard
[1651.80 --> 1653.24]  to measure sometimes
[1653.24 --> 1655.20]  when people are making mistakes
[1655.20 --> 1657.56]  and what their actual perception is
[1657.56 --> 1659.84]  and how a situation went down.
[1659.96 --> 1661.00]  And so there is this
[1661.00 --> 1662.42]  in addition to
[1662.42 --> 1663.38]  there being bias
[1663.38 --> 1664.20]  on the AI side
[1664.20 --> 1665.22]  there's this interesting
[1665.22 --> 1666.00]  kind of bias
[1666.00 --> 1667.22]  on the human side
[1667.22 --> 1668.06]  that's really hard
[1668.06 --> 1669.22]  to measure and deal with.
[1669.46 --> 1669.90]  Yeah, you know
[1669.90 --> 1670.88]  a few minutes ago
[1670.88 --> 1671.82]  we were talking about
[1671.82 --> 1673.16]  these external concerns
[1673.16 --> 1674.38]  for whatever your primary
[1674.38 --> 1676.28]  task or motivation is.
[1676.28 --> 1678.26]  and when we talk about
[1678.26 --> 1679.32]  on the model side
[1679.32 --> 1679.86]  we say well
[1679.86 --> 1681.34]  a model is creating
[1681.34 --> 1681.92]  an inference
[1681.92 --> 1684.04]  to solve a particular task
[1684.04 --> 1685.30]  and you know
[1685.30 --> 1685.82]  unfortunately
[1685.82 --> 1687.10]  it didn't take into account
[1687.10 --> 1688.20]  the external environment
[1688.20 --> 1689.34]  that it was operating in
[1689.34 --> 1690.74]  and so it didn't have empathy
[1690.74 --> 1691.58]  it didn't have other
[1691.58 --> 1692.54]  other attributes
[1692.54 --> 1693.30]  that we might
[1693.30 --> 1694.54]  we might have value for
[1694.54 --> 1696.34]  but at the same time
[1696.34 --> 1697.90]  that's also the strength of it
[1697.90 --> 1698.90]  as you just pointed out
[1698.90 --> 1699.26]  in that
[1699.26 --> 1700.84]  you are getting the benefit
[1700.84 --> 1701.80]  of that inference
[1701.80 --> 1702.54]  as it should be
[1702.54 --> 1703.60]  whereas we humans
[1703.60 --> 1704.98]  we want to look good
[1704.98 --> 1705.92]  we want to sound good
[1705.92 --> 1707.06]  we don't want to make mistakes
[1707.06 --> 1708.42]  we want our peers to like us
[1708.42 --> 1709.78]  and that creates
[1709.78 --> 1710.94]  a whole set of concerns
[1710.94 --> 1712.26]  that change the way
[1712.26 --> 1713.02]  that we're both
[1713.02 --> 1713.86]  in the interactions
[1713.86 --> 1714.54]  and the way that
[1714.54 --> 1715.50]  we're communicating those.
[1715.50 --> 1716.60]  So we have
[1716.60 --> 1717.28]  I think
[1717.28 --> 1718.78]  on many episodes
[1718.78 --> 1719.44]  highlighted
[1719.44 --> 1721.06]  some of the
[1721.06 --> 1722.34]  downsides
[1722.34 --> 1723.48]  of an over
[1723.48 --> 1724.24]  focus
[1724.24 --> 1725.76]  on AI solutions
[1725.76 --> 1726.80]  so I don't know
[1726.80 --> 1727.66]  that we need to go
[1727.66 --> 1729.34]  into incredible detail
[1729.34 --> 1729.82]  on that
[1729.82 --> 1730.12]  I mean
[1730.12 --> 1730.84]  some of those
[1730.84 --> 1731.62]  are this sort of
[1731.62 --> 1732.88]  black box
[1732.88 --> 1733.82]  side of things
[1733.82 --> 1734.44]  where you have
[1734.44 --> 1735.72]  a lack of interpretability
[1735.72 --> 1736.86]  which causes
[1736.86 --> 1738.20]  problems with trust
[1738.20 --> 1739.14]  and debugging
[1739.14 --> 1740.26]  and all of those
[1740.26 --> 1741.02]  sorts of things
[1741.02 --> 1742.10]  you've got
[1742.10 --> 1743.58]  sort of disillusionment
[1743.58 --> 1744.14]  of people
[1744.14 --> 1745.02]  where they
[1745.02 --> 1746.12]  hype up AI
[1746.12 --> 1747.08]  and you know
[1747.08 --> 1747.82]  it's actually
[1747.82 --> 1748.74]  not as great
[1748.74 --> 1749.60]  as they think
[1749.60 --> 1750.04]  of course
[1750.04 --> 1750.80]  AI systems
[1750.80 --> 1751.84]  depend on data
[1751.84 --> 1753.10]  generated by humans
[1753.10 --> 1753.82]  and humans
[1753.82 --> 1754.52]  have bias
[1754.52 --> 1755.46]  and so that data
[1755.46 --> 1756.16]  has bias
[1756.16 --> 1757.28]  and humans
[1757.28 --> 1758.34]  kind of infuse
[1758.34 --> 1759.14]  that sometimes
[1759.14 --> 1759.98]  into models
[1759.98 --> 1761.26]  and you know
[1761.26 --> 1761.96]  in general
[1761.96 --> 1762.90]  it's just hard
[1762.90 --> 1763.44]  to
[1763.44 --> 1764.72]  because AI
[1764.72 --> 1765.12]  is hard
[1765.12 --> 1765.84]  to explain
[1765.84 --> 1766.28]  it's hard
[1766.28 --> 1767.00]  to trust
[1767.00 --> 1768.50]  and it's hard
[1768.50 --> 1769.30]  maybe also
[1769.30 --> 1770.76]  in this context
[1770.76 --> 1771.24]  we're talking
[1771.24 --> 1772.00]  about translation
[1772.00 --> 1773.04]  into local languages
[1773.04 --> 1774.42]  where this sort
[1774.42 --> 1774.88]  of power
[1774.88 --> 1775.52]  to create
[1775.52 --> 1776.16]  these AI
[1776.16 --> 1776.74]  systems
[1776.74 --> 1777.94]  might be
[1777.94 --> 1778.58]  centralized
[1778.58 --> 1779.72]  in large
[1779.72 --> 1780.48]  tech companies
[1780.48 --> 1781.78]  in big
[1781.78 --> 1782.98]  GPU clusters
[1782.98 --> 1784.34]  and not
[1784.34 --> 1784.94]  accessible
[1784.94 --> 1785.98]  to local
[1785.98 --> 1786.72]  language communities
[1786.72 --> 1787.30]  although I think
[1787.30 --> 1788.04]  that is rapidly
[1788.04 --> 1788.58]  changing
[1788.58 --> 1789.74]  there's evidence
[1789.74 --> 1790.52]  throughout
[1790.52 --> 1791.30]  like efforts
[1791.30 --> 1792.20]  like Masakane
[1792.20 --> 1793.46]  in Africa
[1793.46 --> 1794.20]  where people
[1794.20 --> 1794.66]  are doing
[1794.66 --> 1796.22]  amazing AI research
[1796.22 --> 1797.00]  people from
[1797.00 --> 1797.58]  local language
[1797.58 --> 1798.04]  communities
[1798.04 --> 1798.60]  are doing
[1798.60 --> 1800.40]  amazing AI research
[1800.40 --> 1801.00]  with things
[1801.00 --> 1801.52]  like Google
[1801.52 --> 1802.04]  CoLab
[1802.04 --> 1803.46]  so I think
[1803.46 --> 1804.16]  there's a balance
[1804.16 --> 1804.50]  of course
[1804.50 --> 1805.02]  to all these
[1805.02 --> 1805.34]  things
[1805.34 --> 1805.90]  but anything
[1805.90 --> 1806.34]  else you'd
[1806.34 --> 1807.00]  like to highlight
[1807.00 --> 1807.60]  on that
[1807.60 --> 1808.36]  sort of over
[1808.36 --> 1809.18]  focus on AI
[1809.18 --> 1810.02]  side of things
[1810.02 --> 1810.54]  I think
[1810.54 --> 1811.26]  for me
[1811.26 --> 1811.70]  at least
[1811.70 --> 1812.78]  having spent
[1812.78 --> 1813.68]  several years
[1813.68 --> 1814.34]  thinking about
[1814.34 --> 1814.82]  this stuff
[1814.82 --> 1815.24]  with you
[1815.24 --> 1815.66]  and others
[1815.66 --> 1817.04]  I am now
[1817.04 --> 1817.60]  in the habit
[1817.60 --> 1818.40]  of trusting
[1818.40 --> 1819.02]  AI
[1819.02 --> 1820.68]  that solves
[1820.68 --> 1821.70]  procedural
[1821.70 --> 1822.54]  and very
[1822.54 --> 1823.32]  task oriented
[1823.32 --> 1823.88]  things
[1823.88 --> 1824.54]  and I've
[1824.54 --> 1825.34]  seen so many
[1825.34 --> 1825.86]  cases
[1825.86 --> 1826.68]  where it's
[1826.68 --> 1827.18]  doing it
[1827.18 --> 1827.58]  better
[1827.58 --> 1828.58]  than humans
[1828.58 --> 1829.38]  even if it's
[1829.38 --> 1829.88]  a series
[1829.88 --> 1830.76]  of tasks
[1830.76 --> 1831.50]  that together
[1831.50 --> 1832.58]  create a complex
[1832.58 --> 1833.22]  task like
[1833.22 --> 1833.80]  flying an
[1833.80 --> 1834.18]  airplane
[1834.18 --> 1835.18]  but you know
[1835.18 --> 1835.72]  I think
[1835.72 --> 1836.30]  I'm probably
[1836.30 --> 1836.74]  in the
[1836.74 --> 1837.22]  very much
[1837.22 --> 1837.74]  in the minority
[1837.74 --> 1838.30]  but I would
[1838.30 --> 1838.72]  actually be
[1838.72 --> 1839.32]  very comfortable
[1839.32 --> 1840.56]  in an aircraft
[1840.56 --> 1842.14]  that was
[1842.14 --> 1843.24]  mostly modeled
[1843.24 --> 1844.08]  maybe entirely
[1844.08 --> 1844.82]  model driven
[1844.82 --> 1845.46]  without a human
[1845.46 --> 1846.04]  at the wheel
[1846.04 --> 1846.98]  so to speak
[1846.98 --> 1848.22]  and I don't
[1848.22 --> 1848.56]  think most
[1848.56 --> 1848.98]  people are
[1848.98 --> 1849.46]  there yet
[1849.46 --> 1850.36]  I don't
[1850.36 --> 1851.10]  trust AI
[1851.10 --> 1852.20]  to handle
[1852.20 --> 1852.74]  things that
[1852.74 --> 1853.48]  are complex
[1853.48 --> 1854.22]  and nonlinear
[1854.22 --> 1855.24]  and where
[1855.24 --> 1855.56]  there are
[1855.56 --> 1856.22]  many external
[1856.22 --> 1857.10]  concerns that
[1857.10 --> 1857.64]  can influence
[1857.64 --> 1858.24]  a situation
[1858.24 --> 1859.36]  and that's
[1859.36 --> 1859.98]  kind of where
[1859.98 --> 1860.74]  I've arrived
[1860.74 --> 1861.40]  after several
[1861.40 --> 1861.88]  years of
[1861.88 --> 1862.48]  thinking about
[1862.48 --> 1862.64]  it
[1862.64 --> 1863.16]  that's kind
[1863.16 --> 1863.38]  of how
[1863.38 --> 1864.26]  I'm looking
[1864.26 --> 1864.54]  at the
[1864.54 --> 1865.16]  trust issues
[1865.16 --> 1866.00]  so what
[1866.00 --> 1866.24]  what do
[1866.24 --> 1866.98]  you think
[1866.98 --> 1867.58]  would be
[1867.58 --> 1868.38]  a symptom
[1868.38 --> 1869.34]  or an
[1869.34 --> 1870.32]  early warning
[1870.32 --> 1871.24]  sign maybe
[1871.24 --> 1872.24]  that you
[1872.24 --> 1873.28]  are over
[1873.28 --> 1873.90]  focusing
[1873.90 --> 1875.06]  on human
[1875.06 --> 1875.62]  intelligence
[1875.62 --> 1876.52]  or that
[1876.52 --> 1877.10]  you're over
[1877.10 --> 1878.24]  focusing on
[1878.24 --> 1878.96]  artificial
[1878.96 --> 1879.88]  intelligence
[1879.88 --> 1880.40]  what would
[1880.40 --> 1881.34]  be a
[1881.34 --> 1881.64]  symptom
[1881.64 --> 1882.28]  of either
[1882.28 --> 1882.84]  one of
[1882.84 --> 1883.36]  those
[1883.36 --> 1883.96]  conditions
[1883.96 --> 1884.30]  that's
[1884.30 --> 1884.52]  another
[1884.52 --> 1884.98]  part of
[1884.98 --> 1885.26]  this
[1885.26 --> 1885.76]  kind of
[1885.76 --> 1886.08]  framework
[1886.08 --> 1886.38]  is
[1886.38 --> 1886.98]  hey
[1886.98 --> 1887.16]  how
[1887.16 --> 1887.30]  would
[1887.30 --> 1887.42]  I
[1887.42 --> 1887.72]  actually
[1887.72 --> 1888.08]  know
[1888.08 --> 1888.74]  if
[1888.74 --> 1888.96]  I'm
[1888.96 --> 1889.22]  over
[1889.22 --> 1889.60]  focusing
[1889.60 --> 1890.48]  in one
[1890.48 --> 1890.60]  of
[1890.60 --> 1890.78]  these
[1890.78 --> 1891.12]  areas
[1891.12 --> 1891.94]  so the
[1891.94 --> 1892.30]  way I
[1892.30 --> 1892.72]  would arrive
[1892.72 --> 1893.14]  at that
[1893.14 --> 1893.54]  is I
[1893.54 --> 1893.98]  would not
[1893.98 --> 1894.48]  start with
[1894.48 --> 1895.14]  those things
[1895.14 --> 1895.58]  I would
[1895.58 --> 1896.04]  not start
[1896.04 --> 1896.42]  with the
[1896.42 --> 1896.68]  human
[1896.68 --> 1897.18]  intelligence
[1897.18 --> 1897.70]  and what
[1897.70 --> 1898.04]  I think
[1898.04 --> 1898.34]  of it
[1898.34 --> 1898.66]  versus
[1898.66 --> 1899.38]  machine
[1899.38 --> 1899.84]  intelligence
[1899.84 --> 1900.86]  I would
[1900.86 --> 1901.36]  start with
[1901.36 --> 1901.68]  what I'm
[1901.68 --> 1902.18]  trying to
[1902.18 --> 1902.56]  solve
[1902.56 --> 1903.10]  and I
[1903.10 --> 1903.22]  would
[1903.22 --> 1903.40]  think
[1903.40 --> 1903.72]  what are
[1903.72 --> 1904.34]  the kinds
[1904.34 --> 1904.90]  of things
[1904.90 --> 1905.34]  in the
[1905.34 --> 1905.64]  abstract
[1905.64 --> 1906.34]  that will
[1906.34 --> 1906.68]  solve
[1906.68 --> 1907.04]  this
[1907.04 --> 1908.12]  and then
[1908.12 --> 1908.64]  we've
[1908.64 --> 1909.16]  called out
[1909.16 --> 1909.68]  some fairly
[1909.68 --> 1910.24]  substantial
[1910.24 --> 1910.76]  differences
[1910.76 --> 1911.54]  in those
[1911.54 --> 1911.94]  two
[1911.94 --> 1912.50]  sides
[1912.50 --> 1913.38]  the human
[1913.38 --> 1913.72]  side
[1913.72 --> 1914.18]  versus the
[1914.18 --> 1914.42]  machine
[1914.42 --> 1914.66]  learning
[1914.66 --> 1914.98]  side
[1914.98 --> 1916.24]  and I
[1916.24 --> 1916.48]  think
[1916.48 --> 1917.00]  that there
[1917.00 --> 1917.24]  are
[1917.24 --> 1917.78]  characteristics
[1917.78 --> 1918.38]  that kind
[1918.38 --> 1919.08]  of automatically
[1919.08 --> 1919.40]  lend
[1919.40 --> 1920.22]  themselves to one
[1920.22 --> 1920.52]  way or
[1920.52 --> 1920.74]  another
[1921.12 --> 1921.28]  I think
[1921.28 --> 1921.52]  I would
[1921.52 --> 1921.82]  arrive
[1921.82 --> 1922.32]  that way
[1922.32 --> 1922.96]  I think
[1922.96 --> 1923.40]  the biggest
[1923.40 --> 1924.16]  warning sign
[1924.16 --> 1924.68]  going back
[1924.68 --> 1925.08]  to the
[1925.08 --> 1925.58]  very beginning
[1925.58 --> 1925.86]  of our
[1925.86 --> 1926.42]  conversation
[1926.42 --> 1927.68]  is starting
[1927.68 --> 1928.02]  with an
[1928.02 --> 1928.40]  agenda
[1928.40 --> 1929.00]  which we
[1929.00 --> 1929.32]  call an
[1929.32 --> 1929.78]  approach
[1929.78 --> 1930.34]  starting
[1930.34 --> 1930.66]  with an
[1930.66 --> 1931.08]  approach
[1931.08 --> 1932.18]  and trying
[1932.18 --> 1933.56]  to hammer
[1933.56 --> 1934.34]  that into
[1934.34 --> 1934.90]  whatever it
[1934.90 --> 1935.30]  is that you're
[1935.30 --> 1935.74]  trying to
[1935.74 --> 1936.06]  solve
[1936.06 --> 1936.86]  you go to
[1936.86 --> 1937.16]  the other
[1937.16 --> 1937.44]  end
[1937.44 --> 1938.00]  and so
[1938.00 --> 1938.36]  if you
[1938.36 --> 1938.72]  feel like
[1938.72 --> 1938.88]  you're
[1938.88 --> 1939.28]  hammering
[1939.28 --> 1939.52]  something
[1939.52 --> 1939.90]  in it
[1939.90 --> 1940.24]  doesn't
[1940.24 --> 1940.48]  quite
[1940.48 --> 1940.78]  fit
[1940.78 --> 1941.44]  it
[1941.44 --> 1942.16]  probably
[1942.16 --> 1942.58]  means
[1942.58 --> 1942.84]  that's
[1942.84 --> 1943.20]  exactly
[1943.20 --> 1943.48]  what
[1943.48 --> 1943.64]  you're
[1943.64 --> 1943.92]  doing
[1943.92 --> 1944.64]  and you
[1944.64 --> 1944.80]  should
[1944.80 --> 1945.38]  reassess
[1945.38 --> 1945.84]  and go
[1945.84 --> 1946.16]  back to
[1946.16 --> 1946.40]  what you're
[1946.40 --> 1946.56]  trying
[1946.56 --> 1946.98]  to solve
[1946.98 --> 1947.74]  and figure
[1947.74 --> 1947.90]  the
[1947.90 --> 1948.38]  characteristics
[1948.38 --> 1948.70]  out
[1948.70 --> 1948.92]  and then
[1948.92 --> 1949.20]  which way
[1949.20 --> 1949.40]  do you
[1949.40 --> 1949.74]  go with
[1949.74 --> 1949.96]  that
[1949.96 --> 1950.48]  it leads
[1950.48 --> 1950.70]  to a
[1950.70 --> 1951.00]  natural
[1951.00 --> 1951.50]  solution
[1951.50 --> 1951.72]  quite
[1951.72 --> 1952.04]  honestly
[1952.04 --> 1952.70]  yeah
[1952.70 --> 1953.04]  maybe
[1953.04 --> 1953.56]  that's
[1953.56 --> 1953.88]  part
[1953.88 --> 1954.30]  of
[1954.30 --> 1955.12]  on the
[1955.12 --> 1955.94]  over
[1955.94 --> 1956.50]  emphasis
[1956.50 --> 1957.14]  on the
[1957.14 --> 1957.86]  AI side
[1957.86 --> 1958.40]  maybe that's
[1958.40 --> 1958.78]  part of
[1958.78 --> 1958.96]  it
[1958.96 --> 1959.36]  that
[1959.36 --> 1960.18]  is
[1960.18 --> 1960.80]  where
[1960.80 --> 1961.24]  you
[1961.24 --> 1961.92]  have
[1961.92 --> 1962.68]  this
[1962.68 --> 1963.94]  inclination
[1963.94 --> 1964.88]  to love
[1964.88 --> 1965.64]  your AI
[1965.64 --> 1966.04]  tech
[1966.04 --> 1966.58]  solution
[1966.58 --> 1968.02]  and you
[1968.02 --> 1968.40]  are the
[1968.40 --> 1968.74]  one that
[1968.74 --> 1969.04]  has
[1969.04 --> 1969.54]  created
[1969.54 --> 1969.86]  it
[1969.86 --> 1970.48]  apart
[1970.48 --> 1970.80]  from
[1970.80 --> 1971.12]  these
[1971.12 --> 1971.44]  end
[1971.44 --> 1971.94]  users
[1971.94 --> 1973.00]  you know
[1973.00 --> 1973.20]  these
[1973.20 --> 1973.54]  people
[1973.54 --> 1973.76]  you're
[1973.76 --> 1973.98]  doing
[1973.98 --> 1974.16]  the
[1974.16 --> 1974.62]  translation
[1974.62 --> 1975.02]  for
[1975.02 --> 1975.32]  and
[1975.32 --> 1975.52]  you're
[1975.52 --> 1975.72]  just
[1975.72 --> 1976.00]  sort
[1976.00 --> 1976.20]  of
[1976.20 --> 1976.86]  giving
[1976.86 --> 1977.36]  the
[1977.36 --> 1977.70]  output
[1977.70 --> 1977.96]  to
[1977.96 --> 1978.24]  them
[1978.24 --> 1979.04]  and
[1979.04 --> 1979.42]  they're
[1979.42 --> 1979.62]  not
[1979.62 --> 1979.92]  using
[1979.92 --> 1980.06]  it
[1980.06 --> 1980.20]  they're
[1980.20 --> 1980.38]  not
[1980.38 --> 1980.78]  consuming
[1980.78 --> 1981.00]  it
[1981.00 --> 1981.18]  it's
[1981.18 --> 1981.44]  not
[1981.44 --> 1981.76]  being
[1981.76 --> 1982.20]  adopted
[1982.20 --> 1982.88]  well
[1982.88 --> 1983.10]  that's
[1983.10 --> 1983.46]  probably
[1983.46 --> 1984.04]  a sign
[1984.04 --> 1984.38]  that
[1984.38 --> 1985.10]  hey
[1985.10 --> 1985.62]  you
[1985.62 --> 1986.04]  haven't
[1986.04 --> 1986.56]  involved
[1986.56 --> 1986.90]  them
[1986.90 --> 1987.32]  maybe
[1987.32 --> 1988.42]  maybe
[1988.42 --> 1988.82]  what
[1988.82 --> 1989.00]  you're
[1989.00 --> 1989.34]  doing
[1989.34 --> 1989.70]  isn't
[1989.70 --> 1989.88]  as
[1989.88 --> 1990.18]  great
[1990.18 --> 1990.38]  as
[1990.38 --> 1990.54]  you
[1990.54 --> 1990.88]  think
[1990.88 --> 1991.02]  it
[1991.02 --> 1991.44]  is
[1991.44 --> 1991.84]  like
[1991.84 --> 1991.94]  you
[1991.94 --> 1992.06]  were
[1992.06 --> 1992.24]  saying
[1992.24 --> 1992.40]  you're
[1992.40 --> 1992.62]  trying
[1992.62 --> 1992.82]  to
[1992.82 --> 1993.08]  sort
[1993.08 --> 1993.30]  of
[1993.30 --> 1994.14]  force
[1994.14 --> 1994.62]  a
[1994.62 --> 1995.08]  solution
[1995.08 --> 1995.78]  on
[1995.78 --> 1996.36]  another
[1996.36 --> 1997.06]  target
[1997.06 --> 1998.14]  audience
[1998.14 --> 1998.58]  that
[1998.58 --> 1998.88]  maybe
[1998.88 --> 1999.12]  you
[1999.12 --> 1999.46]  don't
[1999.46 --> 1999.90]  haven't
[1999.90 --> 2000.14]  really
[2000.14 --> 2000.76]  involved
[2000.76 --> 2001.42]  from
[2001.42 --> 2001.60]  the
[2001.60 --> 2002.02]  beginning
[2002.02 --> 2002.92]  of course
[2002.92 --> 2003.18]  if
[2003.18 --> 2003.50]  there
[2006.20 --> 2006.42]  is
[2006.42 --> 2006.86]  involving
[2006.86 --> 2007.44]  everybody
[2007.44 --> 2007.78]  from
[2007.78 --> 2007.96]  the
[2007.96 --> 2008.26]  start
[2008.26 --> 2008.50]  right
[2008.50 --> 2008.64]  it
[2008.64 --> 2008.86]  makes
[2008.86 --> 2009.06]  things
[2009.06 --> 2009.50]  slower
[2009.50 --> 2010.34]  right
[2010.34 --> 2010.48]  it
[2010.48 --> 2010.72]  makes
[2010.72 --> 2010.88]  things
[2010.88 --> 2011.30]  slower
[2011.30 --> 2011.68]  more
[2011.68 --> 2012.14]  costly
[2012.14 --> 2012.82]  and
[2012.82 --> 2013.06]  so
[2013.06 --> 2013.34]  it
[2013.34 --> 2013.50]  is
[2013.50 --> 2013.64]  a
[2013.64 --> 2014.06]  balance
[2014.06 --> 2014.40]  there
[2014.40 --> 2014.58]  I
[2014.58 --> 2014.92]  realize
[2014.92 --> 2015.34]  that
[2015.34 --> 2015.98]  but
[2015.98 --> 2016.30]  maybe
[2016.30 --> 2016.54]  that
[2016.54 --> 2016.72]  is
[2016.72 --> 2016.92]  one
[2016.92 --> 2017.04]  of
[2017.04 --> 2017.32]  the
[2017.32 --> 2017.70]  early
[2017.70 --> 2018.00]  warning
[2018.00 --> 2018.40]  signs
[2018.40 --> 2018.76]  I'll
[2018.76 --> 2018.90]  give
[2018.90 --> 2019.06]  you
[2019.06 --> 2019.20]  an
[2019.20 --> 2019.60]  ironic
[2019.60 --> 2020.24]  answer
[2020.24 --> 2020.44]  for
[2020.44 --> 2020.66]  that
[2020.66 --> 2021.18]  it's
[2021.18 --> 2021.62]  with
[2021.62 --> 2021.78]  the
[2021.78 --> 2022.24]  podcast
[2022.24 --> 2022.42]  that
[2022.42 --> 2022.54]  we
[2022.54 --> 2022.78]  have
[2022.78 --> 2022.98]  here
[2022.98 --> 2023.18]  we
[2023.18 --> 2023.36]  have
[2023.36 --> 2023.50]  the
[2023.50 --> 2023.84]  privilege
[2023.84 --> 2024.24]  of
[2024.24 --> 2024.64]  meeting
[2024.64 --> 2024.84]  and
[2024.84 --> 2025.08]  talking
[2025.08 --> 2025.30]  with
[2025.30 --> 2025.68]  lots
[2025.68 --> 2025.86]  and
[2025.86 --> 2026.18]  lots
[2026.18 --> 2026.36]  of
[2026.36 --> 2026.74]  amazing
[2026.74 --> 2027.16]  people
[2027.16 --> 2027.72]  but
[2027.72 --> 2027.92]  there
[2027.92 --> 2028.02]  are
[2028.02 --> 2028.24]  also
[2028.24 --> 2028.56]  people
[2028.56 --> 2028.72]  out
[2028.72 --> 2028.84]  there
[2028.84 --> 2029.00]  with
[2029.00 --> 2029.38]  agendas
[2029.38 --> 2029.60]  that
[2029.60 --> 2029.70]  will
[2029.70 --> 2029.86]  reach
[2029.86 --> 2030.06]  out
[2030.06 --> 2030.26]  and
[2030.26 --> 2030.40]  in
[2030.40 --> 2030.56]  my
[2030.56 --> 2030.76]  day
[2030.76 --> 2031.00]  job
[2031.00 --> 2031.16]  I
[2031.16 --> 2031.36]  also
[2031.36 --> 2031.54]  have
[2031.54 --> 2031.66]  the
[2031.66 --> 2031.84]  same
[2031.84 --> 2032.12]  thing
[2032.12 --> 2032.40]  about
[2032.40 --> 2032.78]  people
[2032.78 --> 2033.06]  trying
[2033.06 --> 2033.20]  to
[2033.20 --> 2033.38]  reach
[2033.38 --> 2033.62]  out
[2033.62 --> 2034.12]  I
[2034.12 --> 2034.46]  find
[2034.46 --> 2034.88]  myself
[2034.88 --> 2035.46]  very
[2035.46 --> 2035.92]  interested
[2035.92 --> 2036.38]  when
[2036.38 --> 2036.60]  people
[2036.60 --> 2036.84]  reach
[2036.84 --> 2037.00]  out
[2037.00 --> 2037.12]  in
[2037.12 --> 2037.70]  conversation
[2037.70 --> 2038.52]  where
[2038.52 --> 2038.78]  they
[2038.78 --> 2039.30]  have
[2039.30 --> 2039.78]  a
[2039.78 --> 2039.98]  really
[2039.98 --> 2040.48]  meaningful
[2040.48 --> 2041.04]  need
[2041.04 --> 2041.26]  and
[2041.26 --> 2041.44]  they're
[2041.44 --> 2041.84]  solving
[2041.84 --> 2042.04]  it
[2042.04 --> 2042.20]  with
[2042.20 --> 2042.48]  AI
[2042.48 --> 2043.00]  because
[2043.00 --> 2043.32]  it's
[2043.32 --> 2043.48]  the
[2043.48 --> 2043.68]  right
[2043.68 --> 2044.20]  solution
[2044.20 --> 2045.08]  and
[2045.08 --> 2045.80]  conversely
[2045.80 --> 2045.98]  the
[2045.98 --> 2046.56]  conversations
[2046.56 --> 2047.10]  that I
[2047.10 --> 2047.76]  don't
[2047.76 --> 2048.00]  find
[2048.00 --> 2048.42]  myself
[2048.42 --> 2048.78]  really
[2048.78 --> 2049.30]  gravitating
[2049.30 --> 2049.62]  to
[2049.62 --> 2050.36]  are
[2050.36 --> 2050.54]  when
[2050.54 --> 2050.78]  people
[2050.78 --> 2050.96]  are
[2050.96 --> 2051.16]  trying
[2051.16 --> 2051.38]  to
[2051.38 --> 2051.68]  sell
[2051.68 --> 2051.96]  their
[2051.96 --> 2052.32]  stuff
[2052.32 --> 2052.74]  based
[2052.74 --> 2052.96]  on
[2052.96 --> 2053.26]  AI
[2053.26 --> 2054.02]  and
[2054.02 --> 2054.28]  rather
[2054.28 --> 2054.48]  than
[2054.48 --> 2054.74]  talk
[2054.74 --> 2055.00]  about
[2055.00 --> 2055.26]  the
[2055.26 --> 2055.64]  problem
[2055.64 --> 2055.86]  they're
[2055.86 --> 2056.24]  solving
[2056.24 --> 2056.96]  and
[2056.96 --> 2057.18]  why
[2057.18 --> 2057.40]  that
[2057.40 --> 2057.84]  matters
[2057.84 --> 2058.34]  to
[2058.34 --> 2058.74]  people
[2058.74 --> 2059.06]  out
[2059.06 --> 2059.32]  there
[2059.32 --> 2059.56]  they
[2059.56 --> 2059.84]  just
[2059.84 --> 2060.16]  it's
[2060.16 --> 2060.30]  all
[2060.30 --> 2060.52]  about
[2060.52 --> 2060.68]  the
[2060.68 --> 2061.02]  AI
[2061.02 --> 2061.34]  hey
[2061.34 --> 2061.48]  we
[2061.48 --> 2061.62]  have
[2061.62 --> 2061.86]  AI
[2061.86 --> 2062.18]  now
[2062.18 --> 2062.44]  and
[2062.44 --> 2063.00]  frankly
[2063.00 --> 2063.58]  ironically
[2063.58 --> 2063.96]  on an
[2063.96 --> 2064.14]  AI
[2064.14 --> 2064.50]  podcast
[2064.50 --> 2064.90]  I
[2064.90 --> 2065.24]  find
[2065.24 --> 2065.56]  myself
[2065.56 --> 2065.78]  getting
[2065.78 --> 2066.06]  very
[2066.06 --> 2066.32]  bored
[2066.32 --> 2066.54]  with
[2066.54 --> 2066.76]  that
[2066.76 --> 2067.38]  conversation
[2067.38 --> 2067.64]  very
[2067.64 --> 2067.92]  quickly
[2067.92 --> 2068.64]  so
[2068.64 --> 2069.12]  I
[2069.12 --> 2069.24]  think
[2069.24 --> 2069.38]  that
[2069.38 --> 2069.56]  goes
[2069.56 --> 2069.80]  back
[2069.80 --> 2069.92]  to
[2069.92 --> 2070.04]  the
[2070.04 --> 2070.24]  fact
[2070.24 --> 2070.48]  that
[2070.48 --> 2070.80]  no
[2070.80 --> 2070.94]  matter
[2070.94 --> 2071.22]  what
[2071.22 --> 2071.36]  your
[2071.36 --> 2071.70]  job
[2071.70 --> 2071.88]  is
[2071.88 --> 2072.00]  no
[2072.00 --> 2072.14]  matter
[2072.14 --> 2072.40]  what
[2072.40 --> 2072.54]  your
[2081.16 --> 2081.94]  right
[2081.94 --> 2082.44]  thing
[2082.44 --> 2082.72]  to
[2082.72 --> 2083.08]  solve
[2083.08 --> 2083.36]  your
[2083.36 --> 2083.80]  particular
[2083.80 --> 2084.30]  problem
[2084.30 --> 2084.82]  and
[2084.82 --> 2084.98]  that
[2084.98 --> 2085.22]  makes
[2085.22 --> 2085.32]  it
[2085.32 --> 2085.44]  a
[2085.44 --> 2085.82]  fascinating
[2085.82 --> 2086.48]  conversation
[2086.48 --> 2087.24]  whereas
[2087.24 --> 2087.76]  if
[2087.76 --> 2088.06]  it's
[2088.06 --> 2088.32]  just
[2088.32 --> 2088.66]  doing
[2088.66 --> 2088.88]  it
[2088.88 --> 2089.20]  because
[2089.20 --> 2089.52]  the
[2089.52 --> 2089.82]  marketing
[2089.82 --> 2090.16]  people
[2090.16 --> 2090.42]  say
[2090.42 --> 2090.56]  you
[2090.56 --> 2090.74]  need
[2090.74 --> 2090.86]  to
[2090.86 --> 2091.06]  do
[2091.06 --> 2091.24]  it
[2091.24 --> 2091.92]  that's
[2091.92 --> 2092.06]  a
[2092.06 --> 2092.32]  good
[2092.32 --> 2092.58]  warning
[2092.58 --> 2092.94]  sign
[2092.94 --> 2093.12]  that
[2093.12 --> 2093.24]  you
[2093.24 --> 2093.42]  may
[2093.42 --> 2093.56]  be
[2093.56 --> 2093.72]  off
[2093.72 --> 2094.04]  track
[2094.04 --> 2094.52]  and
[2094.52 --> 2094.90]  the
[2094.90 --> 2095.30]  other
[2095.30 --> 2096.28]  question
[2096.28 --> 2096.72]  here
[2096.72 --> 2097.00]  in
[2097.00 --> 2097.22]  this
[2097.22 --> 2097.84]  framework
[2097.84 --> 2098.20]  in
[2098.20 --> 2098.52]  addition
[2098.52 --> 2098.88]  to
[2098.88 --> 2099.18]  those
[2099.18 --> 2099.50]  early
[2099.50 --> 2099.86]  warning
[2099.86 --> 2100.38]  signs
[2100.38 --> 2100.68]  they're
[2100.68 --> 2101.16]  asking
[2101.16 --> 2101.74]  how
[2101.74 --> 2102.02]  will
[2102.02 --> 2102.24]  we
[2102.24 --> 2102.74]  gain
[2102.74 --> 2103.00]  or
[2103.00 --> 2103.72]  maintain
[2103.72 --> 2104.52]  the
[2104.52 --> 2105.06]  positive
[2105.06 --> 2105.74]  results
[2105.74 --> 2106.30]  from
[2106.30 --> 2107.12]  AI
[2107.12 --> 2108.24]  without
[2108.24 --> 2109.42]  sort
[2109.42 --> 2109.58]  of
[2109.58 --> 2110.04]  over
[2111.16 --> 2111.60]  AI
[2111.60 --> 2112.20]  and
[2112.20 --> 2113.02]  maintaining
[2113.02 --> 2113.48]  some
[2113.48 --> 2113.90]  balance
[2113.90 --> 2114.16]  with
[2114.16 --> 2114.46]  human
[2114.46 --> 2115.10]  intelligence
[2115.10 --> 2115.50]  any
[2115.50 --> 2115.84]  thoughts
[2115.84 --> 2116.12]  there
[2116.12 --> 2116.56]  kind
[2116.56 --> 2116.68]  of
[2116.68 --> 2116.88]  what
[2116.88 --> 2117.02]  we
[2117.02 --> 2117.20]  already
[2117.20 --> 2117.46]  said
[2117.46 --> 2117.54]  I
[2117.54 --> 2117.66]  mean
[2117.66 --> 2118.48]  humans
[2118.48 --> 2118.72]  are
[2118.72 --> 2119.26]  amazing
[2119.26 --> 2119.66]  and
[2119.66 --> 2119.82]  as
[2119.82 --> 2120.04]  much
[2120.04 --> 2120.16]  as
[2120.16 --> 2120.28]  we
[2120.28 --> 2120.54]  talk
[2120.54 --> 2120.74]  about
[2120.74 --> 2120.92]  how
[2120.92 --> 2121.46]  amazing
[2121.46 --> 2122.34]  current
[2122.34 --> 2122.60]  deep
[2122.60 --> 2122.94]  learning
[2122.94 --> 2123.72]  technologies
[2123.72 --> 2124.06]  are
[2124.06 --> 2124.20]  in
[2124.20 --> 2124.32]  the
[2124.32 --> 2124.56]  AI
[2124.56 --> 2125.02]  space
[2125.02 --> 2125.90]  humans
[2125.90 --> 2126.12]  are
[2126.12 --> 2126.52]  amazing
[2126.52 --> 2126.90]  too
[2126.90 --> 2127.78]  and
[2127.78 --> 2128.20]  if
[2128.20 --> 2128.36]  you
[2128.36 --> 2128.58]  can
[2128.58 --> 2129.12]  optimize
[2129.12 --> 2129.60]  both
[2129.60 --> 2130.08]  sides
[2130.08 --> 2130.30]  and
[2130.30 --> 2130.42]  you
[2130.42 --> 2130.58]  can
[2130.58 --> 2131.02]  find
[2131.02 --> 2131.36]  that
[2131.36 --> 2132.02]  teaming
[2132.02 --> 2132.38]  between
[2132.38 --> 2132.60]  the
[2132.60 --> 2132.96]  manned
[2132.96 --> 2133.04]  and
[2133.04 --> 2133.16]  the
[2133.16 --> 2133.50]  unmanned
[2133.50 --> 2133.90]  side
[2133.90 --> 2134.74]  and
[2134.74 --> 2135.20]  find
[2135.20 --> 2135.34]  a
[2135.34 --> 2135.44]  way
[2135.44 --> 2135.60]  for
[2135.60 --> 2135.76]  them
[2135.76 --> 2135.92]  to
[2135.92 --> 2136.14]  fit
[2136.14 --> 2136.50]  together
[2141.16 --> 2141.88]  if
[2141.88 --> 2142.06]  you
[2142.06 --> 2142.60]  over
[2142.60 --> 2142.94]  focus
[2142.94 --> 2143.18]  on
[2143.18 --> 2143.38]  one
[2143.38 --> 2143.50]  or
[2143.50 --> 2143.64]  the
[2143.64 --> 2143.84]  other
[2143.84 --> 2144.04]  for
[2144.04 --> 2144.34]  whatever
[2144.34 --> 2144.58]  your
[2144.58 --> 2145.02]  alternative
[2145.02 --> 2145.64]  reasons
[2145.64 --> 2145.94]  then
[2145.94 --> 2146.36]  that
[2146.36 --> 2146.58]  tends
[2146.58 --> 2146.74]  to
[2146.74 --> 2146.90]  send
[2146.90 --> 2147.02]  you
[2147.02 --> 2147.24]  off
[2147.24 --> 2147.82]  yeah
[2147.82 --> 2148.00]  and
[2148.00 --> 2148.30]  maybe
[2148.30 --> 2148.90]  the
[2148.90 --> 2149.42]  way
[2149.42 --> 2149.92]  or
[2149.92 --> 2150.26]  a
[2150.26 --> 2150.68]  way
[2150.68 --> 2151.16]  to
[2151.16 --> 2152.00]  shift
[2152.00 --> 2152.32]  our
[2152.32 --> 2152.64]  thinking
[2152.64 --> 2152.92]  in
[2152.92 --> 2153.50]  this
[2153.50 --> 2154.04]  respect
[2154.04 --> 2154.36]  is
[2154.36 --> 2154.70]  to
[2154.70 --> 2155.26]  when
[2155.26 --> 2155.40]  we
[2155.40 --> 2155.58]  think
[2155.58 --> 2155.78]  about
[2155.78 --> 2155.96]  one
[2155.96 --> 2156.06]  of
[2156.06 --> 2156.22]  these
[2156.22 --> 2156.70]  solutions
[2156.70 --> 2157.00]  like
[2157.00 --> 2157.30]  machine
[2157.30 --> 2157.88]  translation
[2157.88 --> 2158.62]  for
[2158.62 --> 2159.06]  COVID
[2159.06 --> 2159.74]  information
[2159.74 --> 2160.42]  we
[2160.42 --> 2160.64]  should
[2160.64 --> 2160.82]  be
[2160.82 --> 2161.16]  thinking
[2161.16 --> 2161.58]  from
[2161.58 --> 2161.82]  the
[2161.82 --> 2162.16]  start
[2162.16 --> 2162.54]  maybe
[2162.54 --> 2163.24]  about
[2163.24 --> 2163.96]  who
[2163.96 --> 2164.32]  is
[2164.32 --> 2164.54]  the
[2164.54 --> 2164.86]  human
[2164.86 --> 2165.10]  that
[2165.10 --> 2165.36]  needs
[2165.36 --> 2165.52]  to
[2165.52 --> 2165.70]  be
[2165.70 --> 2165.88]  in
[2165.88 --> 2166.04]  the
[2166.04 --> 2166.32]  loop
[2166.32 --> 2166.54]  in
[2166.54 --> 2166.74]  this
[2171.16 --> 2171.68]  model
[2171.68 --> 2172.04]  rather
[2172.04 --> 2172.34]  than
[2172.34 --> 2172.68]  simply
[2172.68 --> 2173.20]  saying
[2173.20 --> 2173.54]  how
[2173.54 --> 2173.72]  can
[2173.72 --> 2173.88]  I
[2173.88 --> 2174.40]  create
[2174.40 --> 2174.72]  the
[2174.72 --> 2175.10]  best
[2175.10 --> 2175.42]  AI
[2175.42 --> 2175.84]  model
[2175.84 --> 2176.72]  which
[2176.72 --> 2176.86]  is
[2176.86 --> 2177.14]  normally
[2177.14 --> 2177.38]  where
[2177.38 --> 2177.54]  we
[2177.54 --> 2177.84]  start
[2177.84 --> 2178.08]  and
[2178.08 --> 2178.20]  to
[2178.20 --> 2178.32]  be
[2178.32 --> 2178.54]  honest
[2178.54 --> 2178.90]  that's
[2178.90 --> 2179.26]  normally
[2179.26 --> 2179.52]  where
[2179.52 --> 2179.74]  I
[2179.74 --> 2180.12]  start
[2180.12 --> 2181.22]  just
[2181.22 --> 2181.62]  out
[2181.62 --> 2181.82]  of
[2181.82 --> 2182.24]  habit
[2182.24 --> 2182.64]  but
[2182.64 --> 2183.42]  I
[2183.42 --> 2183.94]  definitely
[2183.94 --> 2184.60]  know
[2184.60 --> 2184.82]  that
[2184.82 --> 2185.02]  I
[2185.02 --> 2185.64]  need
[2185.64 --> 2185.92]  to
[2185.92 --> 2186.20]  be
[2186.20 --> 2186.46]  more
[2186.46 --> 2186.98]  focused
[2186.98 --> 2187.34]  on
[2187.34 --> 2187.60]  that
[2187.60 --> 2187.96]  human
[2187.96 --> 2188.24]  in
[2188.24 --> 2188.38]  the
[2188.38 --> 2188.62]  loop
[2188.62 --> 2189.04]  element
[2189.04 --> 2189.40]  and
[2189.40 --> 2189.58]  it
[2189.58 --> 2189.98]  definitely
[2189.98 --> 2190.30]  is
[2190.30 --> 2190.72]  important
[2190.72 --> 2191.16]  and
[2191.16 --> 2191.44]  I
[2191.44 --> 2191.64]  think
[2191.64 --> 2191.88]  can
[2191.88 --> 2192.10]  help
[2192.10 --> 2192.58]  maintain
[2192.58 --> 2192.92]  that
[2192.92 --> 2193.38]  balance
[2193.38 --> 2193.60]  I
[2193.60 --> 2193.82]  agree
[2193.82 --> 2194.00]  with
[2194.00 --> 2194.10]  you
[2194.10 --> 2194.30]  and
[2194.30 --> 2194.42]  I
[2194.42 --> 2194.60]  think
[2194.60 --> 2195.00]  COVID
[2195.00 --> 2195.26]  is
[2195.26 --> 2195.42]  a
[2195.42 --> 2195.84]  great
[2195.84 --> 2196.26]  since
[2196.26 --> 2196.40]  we're
[2196.40 --> 2196.68]  talking
[2196.68 --> 2196.92]  about
[2196.92 --> 2197.10]  that
[2197.10 --> 2197.22]  as
[2197.22 --> 2197.34]  our
[2197.34 --> 2197.54]  use
[2197.54 --> 2197.80]  case
[2197.80 --> 2198.20]  it
[2198.20 --> 2198.38]  is
[2198.38 --> 2198.60]  such
[2198.60 --> 2198.76]  a
[2198.76 --> 2199.12]  strong
[2199.12 --> 2199.52]  reason
[2199.52 --> 2199.96]  to
[2199.96 --> 2200.14]  have
[2200.14 --> 2200.70]  language
[2200.70 --> 2201.20]  models
[2201.20 --> 2201.50]  in
[2201.50 --> 2201.88]  many
[2201.88 --> 2202.56]  languages
[2202.56 --> 2203.04]  and
[2203.04 --> 2203.30]  what
[2203.30 --> 2203.50]  that
[2203.50 --> 2203.86]  does
[2203.86 --> 2204.06]  is
[2204.06 --> 2204.64]  you
[2204.64 --> 2204.80]  can
[2204.80 --> 2205.00]  let
[2205.00 --> 2205.26]  those
[2205.26 --> 2205.76]  models
[2205.76 --> 2206.62]  do
[2206.62 --> 2206.92]  that
[2206.92 --> 2207.24]  work
[2207.24 --> 2207.54]  because
[2207.54 --> 2207.76]  they
[2207.76 --> 2208.02]  can
[2208.02 --> 2208.30]  because
[2208.30 --> 2208.48]  it
[2208.48 --> 2208.58]  can
[2208.58 --> 2208.68]  be
[2208.68 --> 2208.88]  very
[2208.88 --> 2209.30]  procedural
[2209.30 --> 2209.54]  to
[2209.54 --> 2209.66]  do
[2209.66 --> 2209.90]  that
[2209.90 --> 2210.26]  but
[2210.26 --> 2210.50]  there's
[2210.50 --> 2210.74]  also
[2210.74 --> 2211.00]  a
[2211.00 --> 2211.14]  role
[2211.14 --> 2211.34]  for
[2211.34 --> 2211.72]  humans
[2211.72 --> 2212.10]  there
[2212.10 --> 2212.68]  and
[2212.68 --> 2212.96]  that
[2212.96 --> 2213.34]  all
[2213.34 --> 2213.46]  of
[2213.46 --> 2213.60]  that
[2213.60 --> 2214.10]  communication
[2214.10 --> 2214.48]  is
[2214.48 --> 2214.92]  happening
[2214.92 --> 2215.22]  inside
[2215.22 --> 2215.38]  a
[2215.38 --> 2215.90]  context
[2215.90 --> 2216.60]  it's
[2216.60 --> 2216.92]  happening
[2216.92 --> 2217.28]  inside
[2217.28 --> 2217.48]  an
[2217.48 --> 2217.98]  environment
[2217.98 --> 2218.70]  that
[2225.42 --> 2225.66]  you
[2225.66 --> 2225.84]  can
[2225.84 --> 2226.28]  scale
[2226.28 --> 2227.30]  language
[2227.30 --> 2228.04]  across
[2228.04 --> 2228.52]  many
[2228.52 --> 2228.74]  many
[2228.74 --> 2229.06]  user
[2229.06 --> 2229.50]  groups
[2229.50 --> 2230.16]  effectively
[2230.16 --> 2231.02]  and
[2231.02 --> 2231.16]  yet
[2231.16 --> 2231.38]  there's
[2231.38 --> 2231.56]  still
[2231.56 --> 2231.92]  room
[2231.92 --> 2232.16]  for
[2232.16 --> 2232.48]  people
[2232.48 --> 2232.68]  to
[2232.68 --> 2232.84]  be
[2232.84 --> 2233.12]  there
[2233.12 --> 2233.36]  to
[2233.36 --> 2233.58]  add
[2233.58 --> 2233.76]  that
[2233.76 --> 2234.12]  human
[2234.12 --> 2234.66]  element
[2234.66 --> 2234.96]  that
[2234.96 --> 2235.08]  is
[2235.08 --> 2235.24]  so
[2235.24 --> 2235.70]  necessary
[2235.70 --> 2236.20]  especially
[2236.20 --> 2236.58]  in
[2236.58 --> 2237.04]  times
[2237.04 --> 2237.24]  like
[2237.24 --> 2237.48]  this
[2237.48 --> 2237.92]  yeah
[2237.92 --> 2238.26]  for
[2238.26 --> 2238.52]  sure
[2238.52 --> 2239.18]  well
[2239.18 --> 2239.66]  we
[2239.66 --> 2240.02]  will
[2240.02 --> 2240.66]  link
[2240.66 --> 2241.14]  this
[2241.14 --> 2241.96]  polarity
[2241.96 --> 2242.50]  map
[2242.50 --> 2243.02]  into
[2243.02 --> 2243.56]  our
[2243.56 --> 2243.86]  show
[2243.86 --> 2244.20]  notes
[2244.20 --> 2244.72]  in case
[2244.72 --> 2244.88]  you
[2244.88 --> 2245.04]  want
[2245.04 --> 2245.14]  to
[2245.14 --> 2245.32]  go
[2245.32 --> 2245.62]  through
[2245.62 --> 2246.02]  this
[2246.02 --> 2246.58]  exercise
[2246.58 --> 2247.48]  with
[2247.48 --> 2247.66]  your
[2247.66 --> 2247.90]  own
[2247.90 --> 2248.28]  team
[2248.28 --> 2248.58]  or
[2248.58 --> 2249.00]  thinking
[2249.00 --> 2249.40]  through
[2249.40 --> 2250.04]  various
[2250.04 --> 2250.62]  other
[2250.62 --> 2251.32]  balances
[2251.32 --> 2251.82]  that
[2251.82 --> 2252.04]  need
[2252.04 --> 2252.22]  to
[2252.22 --> 2252.58]  be
[2252.58 --> 2253.28]  had
[2253.28 --> 2253.66]  in
[2253.66 --> 2254.38]  technology
[2255.42 --> 2257.18]  we
[2257.18 --> 2257.46]  do
[2257.46 --> 2257.98]  normally
[2257.98 --> 2258.92]  share
[2258.92 --> 2259.34]  some
[2259.34 --> 2259.74]  learning
[2259.74 --> 2260.28]  resources
[2260.28 --> 2260.64]  at
[2260.64 --> 2260.82]  the
[2260.82 --> 2261.10]  end
[2261.10 --> 2261.50]  of
[2261.50 --> 2262.12]  our
[2262.12 --> 2263.08]  episodes
[2263.08 --> 2263.52]  I've
[2263.52 --> 2263.70]  got
[2263.70 --> 2263.92]  one
[2263.92 --> 2264.24]  I wanted
[2264.24 --> 2264.44]  to
[2264.44 --> 2264.68]  share
[2264.68 --> 2264.98]  which
[2264.98 --> 2265.38]  I don't
[2265.38 --> 2265.50]  know
[2265.50 --> 2265.64]  how
[2265.64 --> 2266.08]  popular
[2266.08 --> 2266.40]  it would
[2266.40 --> 2266.54]  be
[2266.54 --> 2266.68]  but
[2266.68 --> 2267.00]  I hope
[2267.00 --> 2267.18]  it's
[2267.18 --> 2267.56]  popular
[2267.56 --> 2268.32]  so
[2268.32 --> 2268.74]  normally
[2268.74 --> 2269.18]  we share
[2269.18 --> 2269.72]  machine
[2269.72 --> 2270.04]  learning
[2270.04 --> 2270.40]  courses
[2270.40 --> 2270.60]  or
[2270.60 --> 2270.84]  something
[2270.84 --> 2271.10]  like
[2271.10 --> 2271.32]  that
[2271.32 --> 2271.46]  but
[2271.46 --> 2271.60]  I
[2271.60 --> 2271.86]  think
[2271.86 --> 2272.62]  I
[2272.62 --> 2273.06]  have
[2273.06 --> 2273.50]  someone
[2273.50 --> 2274.30]  early
[2274.30 --> 2274.70]  on
[2274.70 --> 2275.02]  in
[2275.02 --> 2275.48]  my
[2275.48 --> 2277.60]  shout
[2277.60 --> 2277.84]  out
[2277.84 --> 2278.22]  to
[2278.22 --> 2279.18]  Manish
[2279.18 --> 2279.48]  who
[2279.48 --> 2280.54]  is
[2280.54 --> 2280.76]  the
[2280.76 --> 2281.14]  CEO
[2281.14 --> 2281.44]  over
[2281.44 --> 2281.64]  at
[2281.64 --> 2282.18]  DGraph
[2282.18 --> 2282.96]  in one
[2282.96 --> 2283.28]  of our
[2283.28 --> 2283.60]  early
[2283.60 --> 2284.22]  conversations
[2284.22 --> 2284.72]  this was
[2284.72 --> 2285.16]  quite a
[2285.16 --> 2285.34]  while
[2285.34 --> 2285.64]  ago
[2285.64 --> 2285.86]  he
[2285.86 --> 2286.16]  told
[2286.16 --> 2286.46]  me
[2286.46 --> 2287.26]  that
[2287.26 --> 2287.56]  one
[2287.56 --> 2287.72]  of
[2287.72 --> 2287.98]  the
[2287.98 --> 2288.44]  biggest
[2288.44 --> 2289.46]  improvements
[2289.46 --> 2290.16]  in his
[2290.16 --> 2290.48]  own
[2290.48 --> 2291.28]  development
[2291.28 --> 2291.86]  professional
[2291.86 --> 2292.36]  development
[2292.36 --> 2292.74]  as a
[2292.74 --> 2293.00]  software
[2293.00 --> 2293.40]  engineer
[2293.40 --> 2294.36]  was
[2294.36 --> 2294.86]  someone
[2294.86 --> 2295.28]  helping
[2295.28 --> 2295.54]  him
[2295.54 --> 2296.12]  understand
[2296.12 --> 2296.36]  that
[2296.36 --> 2296.66]  putting
[2296.66 --> 2297.12]  time
[2297.12 --> 2297.70]  and focus
[2297.70 --> 2298.28]  onto
[2298.28 --> 2298.80]  his
[2298.80 --> 2299.38]  code
[2299.38 --> 2299.76]  editor
[2299.76 --> 2300.04]  his
[2300.04 --> 2300.42]  IDE
[2300.42 --> 2301.30]  and
[2301.30 --> 2301.64]  really
[2301.64 --> 2302.30]  understanding
[2302.30 --> 2302.52]  that
[2302.52 --> 2302.78]  very
[2302.78 --> 2303.22]  deeply
[2303.22 --> 2304.04]  was
[2304.04 --> 2304.36]  an
[2304.36 --> 2304.76]  extremely
[2304.76 --> 2305.40]  important
[2305.40 --> 2306.02]  element
[2306.02 --> 2306.78]  of
[2306.78 --> 2307.44]  development
[2307.44 --> 2307.82]  and
[2307.82 --> 2308.02]  can
[2308.02 --> 2308.40]  really
[2308.40 --> 2308.74]  give
[2308.74 --> 2308.90]  you
[2308.90 --> 2309.06]  a
[2309.06 --> 2309.44]  huge
[2309.44 --> 2309.94]  boost
[2309.94 --> 2310.66]  in
[2310.66 --> 2311.06]  terms
[2311.06 --> 2311.66]  of
[2311.66 --> 2312.06]  your
[2312.06 --> 2312.50]  work
[2312.50 --> 2312.98]  and
[2312.98 --> 2313.08]  I
[2313.08 --> 2313.20]  don't
[2313.20 --> 2313.32]  know
[2313.32 --> 2313.46]  if
[2313.46 --> 2313.72]  you've
[2313.72 --> 2314.04]  found
[2314.04 --> 2314.26]  that
[2314.26 --> 2314.48]  to
[2314.48 --> 2314.64]  be
[2314.64 --> 2314.86]  true
[2314.86 --> 2315.06]  but
[2315.06 --> 2315.20]  I
[2315.20 --> 2315.66]  definitely
[2315.66 --> 2315.94]  have
[2315.94 --> 2316.16]  found
[2316.16 --> 2316.34]  that
[2316.34 --> 2316.48]  to
[2316.48 --> 2316.64]  be
[2316.64 --> 2316.82]  true
[2316.82 --> 2317.02]  over
[2317.02 --> 2317.34]  time
[2317.34 --> 2317.86]  so
[2317.86 --> 2318.46]  my
[2318.46 --> 2318.72]  code
[2318.72 --> 2319.02]  editor
[2319.02 --> 2319.50]  is
[2319.50 --> 2319.88]  Vem
[2319.88 --> 2320.24]  I know
[2320.24 --> 2320.42]  it's
[2320.42 --> 2320.56]  not
[2320.56 --> 2320.76]  very
[2320.76 --> 2321.06]  cool
[2321.06 --> 2321.60]  I
[2321.60 --> 2321.76]  don't
[2321.76 --> 2321.98]  use
[2321.98 --> 2322.42]  VS
[2322.42 --> 2322.68]  code
[2322.68 --> 2322.80]  or
[2322.80 --> 2323.06]  anything
[2323.06 --> 2323.80]  but
[2323.80 --> 2324.14]  there's
[2324.14 --> 2324.36]  a
[2324.36 --> 2325.02]  website
[2325.02 --> 2325.34]  called
[2325.34 --> 2325.90]  Vemcast
[2325.90 --> 2326.46]  org
[2326.46 --> 2326.76]  I
[2326.76 --> 2327.04]  learned
[2327.04 --> 2327.54]  about
[2327.54 --> 2327.98]  this
[2327.98 --> 2328.34]  from
[2328.34 --> 2328.58]  a
[2328.58 --> 2328.90]  recent
[2328.90 --> 2329.44]  couple
[2329.44 --> 2329.58]  of
[2329.58 --> 2329.90]  episodes
[2329.90 --> 2330.16]  on
[2330.16 --> 2330.30]  the
[2330.30 --> 2330.82]  changelog
[2330.82 --> 2331.28]  podcast
[2331.28 --> 2332.58]  and
[2332.58 --> 2333.02]  this
[2333.02 --> 2333.14]  is
[2333.14 --> 2333.34]  just
[2333.34 --> 2333.58]  like
[2333.58 --> 2333.70]  a
[2333.70 --> 2333.96]  great
[2333.96 --> 2334.34]  wealth
[2334.34 --> 2334.60]  of
[2334.60 --> 2335.00]  info
[2335.00 --> 2335.62]  but
[2335.62 --> 2336.02]  also
[2336.02 --> 2336.54]  that
[2336.54 --> 2337.36]  Vemcast
[2337.36 --> 2337.76]  the
[2337.76 --> 2338.36]  guy
[2338.36 --> 2338.74]  who
[2338.74 --> 2339.30]  runs
[2339.30 --> 2339.70]  that
[2339.70 --> 2340.30]  podcast
[2340.30 --> 2340.74]  he
[2340.74 --> 2340.98]  also
[2340.98 --> 2341.32]  has
[2341.32 --> 2341.60]  a
[2341.60 --> 2342.16]  course
[2342.16 --> 2343.18]  about
[2343.18 --> 2343.78]  Vem
[2343.78 --> 2344.38]  and
[2344.38 --> 2344.70]  the
[2344.70 --> 2345.10]  core
[2345.10 --> 2345.46]  Vem
[2345.46 --> 2345.98]  course
[2345.98 --> 2346.70]  and
[2346.70 --> 2346.92]  I've
[2346.92 --> 2347.04]  been
[2347.04 --> 2347.24]  going
[2347.24 --> 2347.44]  through
[2347.44 --> 2347.68]  that
[2347.68 --> 2347.86]  and
[2347.86 --> 2348.06]  I've
[2348.06 --> 2348.40]  really
[2348.40 --> 2348.60]  been
[2348.60 --> 2348.94]  enjoying
[2348.94 --> 2349.16]  it
[2349.16 --> 2349.32]  so
[2349.32 --> 2349.46]  I
[2349.46 --> 2349.62]  wanted
[2349.62 --> 2349.82]  to
[2349.82 --> 2350.04]  mention
[2350.04 --> 2350.32]  that
[2350.32 --> 2350.44]  on
[2350.44 --> 2350.56]  the
[2350.56 --> 2351.10]  podcast
[2351.10 --> 2351.38]  thank
[2351.38 --> 2351.54]  you
[2351.54 --> 2351.78]  so
[2351.78 --> 2352.10]  much
[2352.10 --> 2352.88]  Drew
[2352.88 --> 2353.28]  at
[2353.28 --> 2353.96]  Vemcast
[2353.96 --> 2354.18]  for
[2354.18 --> 2354.44]  putting
[2354.44 --> 2354.80]  together
[2354.80 --> 2355.04]  this
[2355.04 --> 2355.28]  great
[2355.28 --> 2355.62]  course
[2355.62 --> 2355.90]  that
[2355.90 --> 2356.16]  is
[2356.16 --> 2356.92]  benefiting
[2356.92 --> 2357.34]  me
[2357.34 --> 2357.52]  a
[2357.52 --> 2357.72]  lot
[2357.72 --> 2357.92]  but
[2357.92 --> 2358.28]  also
[2358.28 --> 2359.24]  another
[2359.24 --> 2359.72]  podcast
[2359.72 --> 2360.22]  that
[2360.22 --> 2360.34]  I
[2360.34 --> 2360.54]  love
[2360.54 --> 2360.84]  listening
[2360.84 --> 2361.12]  to
[2361.12 --> 2361.38]  and
[2361.38 --> 2361.92]  learning
[2361.92 --> 2362.28]  from
[2362.28 --> 2362.66]  so
[2362.66 --> 2363.28]  yeah
[2363.28 --> 2363.36]  I
[2363.36 --> 2363.48]  just
[2363.48 --> 2363.64]  wanted
[2363.64 --> 2363.80]  to
[2363.80 --> 2363.92]  give
[2363.92 --> 2364.04]  a
[2364.04 --> 2364.26]  shout
[2364.26 --> 2364.44]  out
[2364.44 --> 2364.72]  there
[2364.72 --> 2365.20]  I
[2365.20 --> 2365.32]  don't
[2365.32 --> 2365.42]  know
[2365.42 --> 2365.52]  if
[2365.52 --> 2365.60]  you
[2365.60 --> 2365.78]  found
[2365.78 --> 2365.94]  that
[2365.94 --> 2366.04]  to
[2366.04 --> 2366.16]  be
[2366.16 --> 2366.38]  true
[2366.38 --> 2366.72]  as well
[2366.72 --> 2366.82]  in
[2366.82 --> 2366.92]  your
[2366.92 --> 2367.06]  own
[2367.06 --> 2367.36]  work
[2367.36 --> 2367.90]  with
[2367.90 --> 2368.06]  your
[2368.06 --> 2368.30]  code
[2368.30 --> 2368.58]  editor
[2368.58 --> 2368.92]  yep
[2368.92 --> 2369.14]  I
[2389.24 --> 2389.64]  person
[2389.64 --> 2389.82]  would
[2389.82 --> 2390.04]  tell
[2390.04 --> 2390.24]  you
[2390.24 --> 2390.60]  like
[2390.60 --> 2391.02]  if
[2391.02 --> 2391.14]  you
[2391.14 --> 2391.32]  go
[2391.32 --> 2391.52]  to
[2391.52 --> 2391.64]  a
[2391.64 --> 2391.86]  Linux
[2391.86 --> 2392.18]  server
[2392.18 --> 2392.46]  Vem
[2392.46 --> 2392.60]  will
[2392.60 --> 2392.78]  be
[2392.78 --> 2393.02]  there
[2393.02 --> 2393.16]  and
[2393.16 --> 2393.30]  then
[2393.30 --> 2393.46]  you're
[2393.46 --> 2393.70]  not
[2393.70 --> 2394.10]  crippled
[2394.10 --> 2394.58]  anymore
[2394.58 --> 2395.48]  but
[2395.48 --> 2395.96]  you know
[2395.96 --> 2396.26]  that's
[2396.26 --> 2396.60]  also
[2396.60 --> 2397.08]  sort
[2397.08 --> 2397.20]  of
[2397.20 --> 2397.44]  like
[2397.44 --> 2397.98]  VS code
[2397.98 --> 2398.16]  is
[2398.16 --> 2398.36]  pretty
[2398.36 --> 2398.80]  amazing
[2398.80 --> 2399.22]  it
[2399.22 --> 2399.50]  is
[2399.50 --> 2399.70]  I
[2399.70 --> 2399.88]  agree
[2399.88 --> 2400.08]  with
[2400.08 --> 2400.20]  you
[2400.20 --> 2400.62]  I'll
[2400.62 --> 2400.84]  offer
[2400.84 --> 2401.02]  up
[2401.02 --> 2401.20]  one
[2401.20 --> 2401.36]  as
[2401.36 --> 2401.58]  well
[2401.58 --> 2401.82]  I'll
[2401.82 --> 2401.90]  go
[2401.90 --> 2402.08]  back
[2402.08 --> 2402.20]  to
[2402.20 --> 2402.32]  what
[2402.32 --> 2402.46]  I
[2402.46 --> 2402.68]  was
[2402.68 --> 2402.92]  talking
[2402.92 --> 2403.12]  about
[2403.12 --> 2403.26]  the
[2403.26 --> 2403.44]  very
[2403.44 --> 2403.84]  beginning
[2403.84 --> 2404.28]  of
[2404.28 --> 2404.46]  the
[2404.46 --> 2404.96]  conversation
[2404.96 --> 2405.58]  the
[2405.58 --> 2406.40]  NABC
[2406.40 --> 2406.88]  value
[2406.88 --> 2407.46]  proposition
[2407.46 --> 2408.32]  framework
[2408.32 --> 2408.80]  which
[2408.80 --> 2409.16]  is
[2409.16 --> 2409.76]  beautiful
[2409.76 --> 2410.06]  in
[2410.06 --> 2410.24]  its
[2410.24 --> 2410.80]  simplicity
[2419.24 --> 2425.88]  and
[2425.88 --> 2426.00]  we
[2426.00 --> 2426.16]  will
[2426.16 --> 2426.34]  link
[2426.34 --> 2426.50]  to
[2426.50 --> 2426.64]  it
[2426.64 --> 2426.78]  in
[2426.78 --> 2426.88]  the
[2426.88 --> 2427.06]  show
[2427.06 --> 2427.34]  notes
[2427.34 --> 2427.98]  but
[2427.98 --> 2428.14]  that
[2428.14 --> 2428.26]  is
[2428.26 --> 2428.38]  a
[2428.38 --> 2428.50]  good
[2428.50 --> 2428.80]  place
[2428.80 --> 2428.94]  to
[2428.94 --> 2429.14]  go
[2429.14 --> 2429.32]  and
[2429.32 --> 2429.48]  learn
[2429.48 --> 2429.60]  a
[2429.60 --> 2429.72]  little
[2429.72 --> 2429.88]  bit
[2429.88 --> 2430.16]  about
[2430.16 --> 2430.44]  it
[2430.44 --> 2430.86]  and
[2430.86 --> 2431.16]  I
[2431.16 --> 2431.34]  think
[2431.34 --> 2431.60]  that's
[2431.60 --> 2431.88]  why
[2431.88 --> 2432.38]  it
[2432.38 --> 2432.80]  keeps
[2432.80 --> 2433.02]  it
[2433.02 --> 2433.86]  straight
[2433.86 --> 2434.10]  and
[2434.10 --> 2434.42]  simple
[2434.42 --> 2434.92]  and
[2434.92 --> 2435.14]  that
[2435.14 --> 2435.52]  means
[2435.52 --> 2435.78]  that
[2435.78 --> 2436.12]  when
[2436.12 --> 2436.26]  you're
[2436.26 --> 2436.34]  in
[2436.34 --> 2436.44]  the
[2436.44 --> 2436.62]  middle
[2436.62 --> 2436.76]  of
[2436.76 --> 2436.84]  a
[2436.84 --> 2437.40]  conversation
[2437.40 --> 2438.30]  it
[2438.30 --> 2438.60]  allows
[2438.60 --> 2438.74]  you
[2438.74 --> 2438.86]  to
[2438.86 --> 2439.02]  stay
[2439.02 --> 2439.16]  on
[2439.16 --> 2439.44]  target
[2439.44 --> 2439.76]  so
[2439.76 --> 2440.00]  that's
[2440.00 --> 2440.10]  what
[2440.10 --> 2440.28]  I'll
[2440.28 --> 2440.50]  offer
[2440.50 --> 2440.70]  up
[2440.70 --> 2440.86]  for
[2440.86 --> 2440.98]  a
[2440.98 --> 2441.30]  strategy
[2441.30 --> 2441.90]  awesome
[2441.90 --> 2442.58]  thanks
[2442.58 --> 2442.90]  Chris
[2442.90 --> 2443.38]  I
[2443.38 --> 2443.78]  appreciate
[2443.78 --> 2444.42]  you
[2444.42 --> 2444.82]  letting
[2444.82 --> 2445.00]  a
[2445.00 --> 2445.38]  novice
[2445.38 --> 2445.64]  like
[2445.64 --> 2445.98]  me
[2445.98 --> 2446.48]  enter
[2446.48 --> 2446.72]  into
[2446.72 --> 2446.98]  the
[2446.98 --> 2447.34]  strategy
[2447.34 --> 2447.82]  world
[2447.82 --> 2448.60]  and
[2448.60 --> 2450.18]  operate
[2450.18 --> 2450.44]  where
[2450.44 --> 2450.58]  I'm
[2450.58 --> 2450.78]  not
[2450.78 --> 2451.20]  qualified
[2451.20 --> 2451.46]  to
[2451.46 --> 2451.90]  operate
[2451.90 --> 2452.36]  oh
[2452.36 --> 2452.76]  boy
[2452.76 --> 2453.26]  oh
[2453.26 --> 2453.80]  gosh
[2453.80 --> 2454.28]  so
[2454.28 --> 2454.68]  thanks
[2454.68 --> 2454.84]  so
[2454.84 --> 2455.02]  much
[2455.02 --> 2455.38]  Chris
[2455.38 --> 2455.66]  hope
[2455.66 --> 2455.78]  you
[2455.78 --> 2455.96]  have
[2455.96 --> 2456.14]  a
[2456.14 --> 2456.48]  good
[2456.48 --> 2456.90]  week
[2456.90 --> 2457.12]  and
[2457.12 --> 2457.30]  we'll
[2457.30 --> 2457.52]  talk
[2457.52 --> 2457.62]  to
[2457.62 --> 2457.74]  you
[2457.74 --> 2458.00]  soon
[2458.00 --> 2458.46]  sounds
[2458.46 --> 2458.72]  good
[2458.72 --> 2458.96]  thanks
[2458.96 --> 2459.20]  Daniel
[2475.00 --> 2475.44]  to
[2475.44 --> 2475.66]  the
[2475.66 --> 2476.02]  world
[2476.02 --> 2476.42]  and
[2476.42 --> 2476.68]  seeing
[2476.68 --> 2476.86]  what
[2476.86 --> 2477.26]  happens
[2477.26 --> 2477.84]  it's
[2477.84 --> 2478.02]  about
[2478.02 --> 2478.20]  the
[2478.20 --> 2478.62]  code
[2478.62 --> 2478.92]  the
[2478.92 --> 2479.36]  ops
[2479.36 --> 2479.60]  the
[2479.60 --> 2479.98]  infra
[2479.98 --> 2480.38]  and
[2480.38 --> 2480.54]  the
[2480.54 --> 2480.74]  people
[2480.74 --> 2480.90]  that
[2480.90 --> 2481.08]  make
[2481.08 --> 2481.18]  it
[2481.18 --> 2481.52]  happen
[2481.52 --> 2482.04]  yes
[2482.04 --> 2482.24]  we
[2482.24 --> 2482.52]  focus
[2482.52 --> 2482.66]  on
[2482.66 --> 2482.78]  the
[2482.78 --> 2483.06]  people
[2483.06 --> 2483.52]  because
[2483.52 --> 2483.78]  everything
[2483.78 --> 2484.16]  else
[2484.16 --> 2484.60]  is an
[2484.60 --> 2484.98]  implementation
[2484.98 --> 2485.56]  detail
[2485.56 --> 2486.12]  subscribe
[2486.12 --> 2486.52]  now
[2486.52 --> 2486.78]  at
[2486.78 --> 2487.66]  changelog.com
[2487.66 --> 2488.00]  slash
[2488.00 --> 2488.48]  ship it
[2488.48 --> 2489.16]  or simply
[2489.16 --> 2489.48]  search
[2489.48 --> 2489.70]  for
[2489.70 --> 2490.12]  ship it
[2490.12 --> 2490.42]  in your
[2490.42 --> 2490.58]  favorite
[2490.58 --> 2490.98]  podcast
[2490.98 --> 2491.24]  app
[2491.24 --> 2491.44]  you'll
[2491.44 --> 2491.64]  find
[2491.64 --> 2491.82]  it
[2491.82 --> 2492.06]  of
[2492.06 --> 2492.24]  course
[2492.24 --> 2492.40]  the
[2492.40 --> 2492.72]  galaxy
[2492.72 --> 2493.06]  brain
[2493.06 --> 2493.34]  move
[2493.34 --> 2493.56]  is
[2493.56 --> 2493.70]  to
[2493.70 --> 2494.06]  subscribe
[2494.06 --> 2494.30]  to
[2494.30 --> 2494.54]  our
[2494.54 --> 2494.88]  master
[2494.88 --> 2495.20]  feed
[2495.20 --> 2495.56]  it's
[2495.56 --> 2495.84]  all
[2495.84 --> 2496.30]  changelog
[2496.30 --> 2496.94]  podcasts
[2496.94 --> 2497.62]  including
[2497.62 --> 2498.18]  practical
[2498.18 --> 2498.52]  ai
[2498.52 --> 2498.90]  and
[2498.90 --> 2499.14]  ship
[2499.14 --> 2499.32]  it
[2499.32 --> 2499.54]  in
[2499.54 --> 2499.90]  one
[2499.90 --> 2500.60]  place
[2500.60 --> 2501.20]  search
[2501.20 --> 2501.70]  changelog
[2501.70 --> 2501.98]  master
[2501.98 --> 2502.36]  feed
[2502.36 --> 2502.66]  or
[2502.66 --> 2502.84]  head
[2502.84 --> 2503.02]  to
[2503.02 --> 2503.86]  changelog.com
[2503.86 --> 2504.10]  slash
[2504.10 --> 2504.50]  master
[2504.50 --> 2504.98]  and
[2504.98 --> 2505.34]  subscribe
[2505.34 --> 2505.70]  today
[2505.70 --> 2506.50]  practical
[2506.50 --> 2506.88]  ai
[2506.88 --> 2507.12]  is
[2507.12 --> 2507.36]  hosted
[2507.36 --> 2507.54]  by
[2507.54 --> 2507.86]  daniel
[2507.86 --> 2508.28]  whitenack
[2508.28 --> 2508.54]  and
[2508.54 --> 2508.74]  chris
[2508.74 --> 2509.04]  benson
[2509.04 --> 2509.40]  with
[2509.40 --> 2509.76]  music
[2509.76 --> 2510.00]  by
[2510.00 --> 2510.20]  break
[2510.20 --> 2510.44]  master
[2510.44 --> 2510.84]  cylinder
[2510.84 --> 2511.18]  we're
[2511.18 --> 2511.38]  brought
[2511.38 --> 2511.54]  to you
[2511.54 --> 2511.64]  by
[2511.64 --> 2512.12]  fastly
[2512.12 --> 2512.50]  launch
[2512.50 --> 2512.92]  darkly
[2512.92 --> 2513.28]  and
[2513.28 --> 2513.60]  linode
[2513.60 --> 2514.14]  that's
[2514.14 --> 2514.24]  all
[2514.24 --> 2514.36]  for
[2514.36 --> 2514.60]  now
[2514.60 --> 2514.96]  we'll
[2514.96 --> 2515.10]  talk
[2515.10 --> 2515.18]  to
[2515.18 --> 2515.24]  you
[2515.24 --> 2515.52]  next
[2515.52 --> 2515.78]  week
[2527.62 --> 2545.15] 
