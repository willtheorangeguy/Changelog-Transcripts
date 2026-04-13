[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind the scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.18 --> 37.50]  Now, on to the show.
[48.26 --> 51.66]  This is Chris Benson, co-host of the Practical AI Podcast.
[51.66 --> 57.62]  I was recently invited by my good friends, Jared Santo and Adam Stachowiak, to be their
[57.62 --> 62.82]  guest on the Changelog Podcast, which is one of the most popular open source and software
[62.82 --> 64.30]  development podcasts in the world.
[64.84 --> 69.98]  Though independent now, Practical AI used to be part of the Changelog family of podcasts,
[70.12 --> 71.48]  and we remain very close.
[72.06 --> 77.10]  We have reproduced that Changelog episode to be this Practical AI episode.
[77.10 --> 80.80]  And in this episode, we're going to cover a wide variety of topics.
[80.80 --> 96.24]  Today, we have Chris Benson, Practical AI co-host and longtime friend.
[96.64 --> 97.72]  Welcome to the show, Chris.
[98.16 --> 99.04]  Hey, thanks a lot.
[99.18 --> 102.00]  It's great to be on the guest side of the equation here.
[102.28 --> 106.50]  Yeah, you've been interviewing folks for a long time, but now you, sir, are being interviewed,
[106.62 --> 107.12]  so to speak.
[108.08 --> 108.48]  Indeed.
[108.48 --> 108.76]  Indeed.
[108.92 --> 109.66]  Does that make you nervous?
[110.08 --> 110.72]  Well, I got it.
[110.76 --> 112.38]  You know, you guys taught me everything I know.
[112.52 --> 113.98]  So like, yeah, a little bit.
[114.12 --> 114.82]  It's kind of like.
[115.32 --> 116.40]  We got back a few tricks.
[116.48 --> 118.02]  We're going to unleash them on you on this show.
[118.12 --> 118.98]  Oh, my God.
[119.08 --> 119.36]  OK.
[119.74 --> 125.30]  So, but, but, but yeah, like, you know, you guys were the, you guys were the, the OG originals.
[125.64 --> 129.32]  So Daniel Whitenack and I learned everything we know from you guys.
[129.48 --> 129.58]  So.
[130.10 --> 131.06]  Well, you guys are good at what you do.
[131.12 --> 132.20]  So I'll take that as a compliment.
[132.54 --> 132.74]  Yeah.
[133.42 --> 134.16]  Well, thank you.
[134.16 --> 137.54]  What's funny is how back, well, how far back we go.
[137.60 --> 138.98]  I think there's some context to give here.
[139.06 --> 143.56]  And Jared, just for an exercise here, I went and searched the name Benson because Chris's
[143.56 --> 144.60]  last name is Benson.
[144.94 --> 145.24]  Correct.
[145.34 --> 146.04]  In my calendar.
[146.04 --> 148.84]  Just to see if the history was there.
[149.00 --> 155.70]  And literally April 3rd at 1030 AM, Chris Benson on Skype.
[155.70 --> 156.70]  Hmm.
[157.66 --> 158.82]  That's how far, that's how far back.
[158.82 --> 158.98]  What year?
[159.26 --> 159.90]  What's the year?
[160.20 --> 160.52]  2018.
[160.98 --> 161.58]  Did I not say the year?
[161.58 --> 161.84]  Yeah.
[161.96 --> 162.28]  My bad.
[162.38 --> 162.74]  No, you didn't.
[162.84 --> 164.12]  April 3rd, 2018.
[164.38 --> 166.66]  Chris Benson, 1030 AM Skype.
[166.74 --> 167.26]  That's what you're doing.
[167.76 --> 170.12]  That was way back when we used Skype, you know?
[170.30 --> 170.74]  That's right.
[170.80 --> 171.40]  We had to.
[171.80 --> 172.54]  That was so wild.
[172.74 --> 173.54]  That was our only option.
[173.84 --> 178.68]  And that's what the, that was the original conversation that started the host, co-host,
[178.84 --> 179.48]  Practical AI.
[179.48 --> 181.40]  I think it was a data show back then, even.
[181.52 --> 182.54]  I'm not even sure if it had a name.
[183.02 --> 184.16]  It didn't have a name yet.
[184.16 --> 188.78]  The beginnings of Practical AI and this long history of relationship.
[189.28 --> 191.64]  It was funny because I know I had reached out to you guys.
[191.94 --> 198.40]  And then like, so, you know, there was, you guys had go time and, you know, there was this
[198.40 --> 201.22]  kind of changelog, you know, family that was already there.
[201.38 --> 209.16]  And I wasn't part of it yet, but Daniel and I were, Daniel Whitenack and I were both kind
[209.16 --> 212.42]  of the data AI people in the go community at the time.
[212.42 --> 217.36]  And, and so like, I was thinking, you know, I was listening to changelog and stuff and
[217.36 --> 222.50]  thinking, boy, you know, maybe it's, maybe these guys need to start an AI, you know,
[222.50 --> 224.78]  focused podcast or something.
[225.04 --> 229.56]  And I was thinking, but like, I'd like to do that, but I was thinking, but I need, I need
[229.56 --> 230.68]  somebody to do it with.
[230.72 --> 232.84]  And I was thinking, I got to reach out to Daniel.
[232.98 --> 234.26]  You know, he's the other AI data.
[234.40 --> 239.22]  So I reached out to Daniel and he's like, oh, by the way, I just started talking to Jared
[239.22 --> 241.02]  and Adam about this.
[241.18 --> 242.26]  And like, I was like, perfect.
[242.36 --> 243.30]  I just sent them a message.
[243.60 --> 245.88]  So the timing, yeah, it all just came together.
[246.04 --> 246.92]  The timing was perfect.
[247.40 --> 248.88]  You guys were so far ahead of the curve.
[249.52 --> 249.76]  Yeah.
[249.92 --> 252.46]  Well, it was like, it was very clear.
[253.16 --> 257.38]  If you were really plugged into the AI world at that point, it was very clear that this was
[257.38 --> 262.08]  going like, you know, like where it was going, you know, things change all the time, but like,
[262.08 --> 268.24]  it was very clear by that time that the gas pedal was on and, you know, sky was the limit
[268.24 --> 270.72]  and there was some kind of journey ahead.
[271.04 --> 276.28]  And at that point, Daniel and I wanted, we wanted to be steering that, that journey for
[276.28 --> 276.68]  everybody.
[276.68 --> 281.22]  And that was how, you know, and you guys were awesome in terms of saying, this would be
[281.22 --> 282.82]  fantastic and we'd love to do it.
[282.82 --> 287.90]  And, you know, that was back in 2018 and here we are in 2025, late 2025.
[288.46 --> 288.64]  Yeah.
[288.76 --> 291.96]  Things have changed, but have stayed the same as well.
[292.08 --> 295.86]  Here's a funny story that you might not know, Chris, I've given you credit for this before,
[295.94 --> 300.18]  but I don't think I've ever told you this, which is at some point the four of us were
[300.18 --> 305.86]  on a call and this is like post launching practical AI, but pre chat GPT moment.
[306.62 --> 311.76]  And you were lamenting that we like missed NVIDIA or something like you, you, we were talking
[311.76 --> 313.24]  about the run up.
[313.40 --> 317.78]  I think NVIDIA had just had a huge run up with regards to first it was gaming, but then
[317.78 --> 321.12]  also, you know, machine learning was kind of starting to take off.
[321.12 --> 324.26]  And you were like, man, I can't believe like, look at NVIDIA.
[324.42 --> 324.82]  It's crazy.
[324.90 --> 326.50]  The hockey stick growth on that stock.
[326.90 --> 328.36]  You're like, but we're too late now.
[328.40 --> 328.94]  We're too late.
[329.58 --> 330.42]  And this is like 29.
[330.58 --> 331.36]  This is like 2019.
[331.82 --> 332.64]  I was so wrong.
[332.86 --> 333.02]  Yeah.
[333.36 --> 334.44]  Here's the funny part, Chris.
[334.48 --> 336.32]  I thought to myself, are we though?
[336.62 --> 337.82]  I said, I was like, are we?
[337.86 --> 341.10]  And I actually left that call and I went, I bought a little bit of NVIDIA stock thinking,
[341.22 --> 344.32]  you know, if Chris thinks we're too late, this guy's always ahead of everything.
[344.32 --> 346.06]  So I think he's ahead.
[346.18 --> 349.84]  So I, I have to thank you for a stock tip that has paid off.
[350.18 --> 352.40]  Well, you're welcome.
[352.54 --> 357.08]  You buy contrary to my advice, but that's maybe that's, that's probably, uh, yeah, that's
[357.08 --> 357.80]  probably right.
[357.92 --> 360.42]  So I need to talk to you more often and kind of do the opposite thing.
[360.62 --> 360.78]  Yeah.
[360.84 --> 361.34]  There you go.
[361.76 --> 362.74]  So yeah, thanks for that.
[362.80 --> 363.36]  That was cool.
[364.24 --> 368.46]  Unfortunately, I didn't buy enough to like just quit everything else and, and retire,
[368.62 --> 371.82]  but I'm still, I'm happy that you thought we missed it.
[371.82 --> 373.36]  I'm glad I was wrong on that.
[373.42 --> 375.14]  They've done amazing things.
[375.14 --> 380.16]  And like, you know, I think it's kind of funny, you know, just in AI in general, you
[380.16 --> 384.74]  know, AI has been around at some level, even, even the modern form of AI has been around
[384.74 --> 385.64]  for decades.
[385.90 --> 392.38]  You know, it's not a recent thing, uh, because like I got introduced to it by my, my parents
[392.38 --> 398.76]  who were actually, who are technical, technical people, um, Georgia tech and Lockheed and things
[398.76 --> 399.20]  like that.
[399.20 --> 403.76]  And they were doing stuff back in the late eighties and early nineties and stuff.
[403.76 --> 408.92]  And my dad introduced me to neural networks, which is still the basis of all this stuff
[408.92 --> 409.98]  in 1992.
[410.82 --> 416.24]  And I think like, it was funny, you know, the tie in here to Nvidia is like, we went through
[416.24 --> 417.10]  another AI winter.
[417.34 --> 421.08]  There's been a series of kind of like where everyone gave up on AI for a little while and
[421.08 --> 422.12]  then circled back around.
[422.22 --> 423.02]  They're called AI winters.
[423.02 --> 428.74]  And so the last AI winter kind of happened at the end of the nineties going into the
[428.74 --> 433.82]  two thousands there for a few years before the modern era, if you will, picked up.
[434.32 --> 441.98]  But I think the difference is that the notion of modeling and the software basis of AI was,
[442.06 --> 442.72]  was there.
[442.88 --> 447.10]  And there were a lot of great ideas and a lot of the stuff we're doing today originated back
[447.10 --> 449.66]  then conceptually, but we didn't have the hardware.
[449.66 --> 455.18]  We couldn't actually do the thing, you know, we, we didn't have these GPUs and, and now
[455.18 --> 458.54]  other types of chips that enabled all this to happen.
[458.54 --> 463.98]  And so it was really like the hardware side of things had to catch up so that the software
[463.98 --> 466.84]  that, and I, like when people say, well, why did we have an AI winter?
[466.84 --> 472.82]  And I think to a large degree, it wasn't the lack of amazing brain power, you know, to solve
[472.82 --> 474.02]  these problems and create the models.
[474.02 --> 478.10]  It was the fact that you didn't have the hardware infrastructure to do the things that people
[478.10 --> 479.52]  were envisioning were possible.
[479.66 --> 484.72]  And it wasn't until Nvidia came along and became the AI, you know, really the AI hardware
[484.72 --> 485.10]  company.
[485.20 --> 490.10]  I mean, I know they do a lot of software stuff, but, but, you know, that, that made the difference.
[490.10 --> 495.22]  And, you know, Google came along eventually with TPUs and lots of other players jumped in,
[495.32 --> 496.72]  but both sides had to be there.
[496.72 --> 500.64]  So a little, little, uh, little journey down memory lane there.
[500.88 --> 501.14]  Yeah.
[501.56 --> 502.04]  It's the bet.
[502.06 --> 503.22]  It's the benefit of being old.
[503.60 --> 504.58]  You've seen it all, Chris.
[504.62 --> 505.64]  You have seen it all.
[505.80 --> 506.46]  I've been around.
[506.54 --> 507.42]  I'm, I'm old as dirt.
[507.42 --> 508.94]  So, so from your purview,
[508.94 --> 515.96]  this is not stock advice, but from your purview, um, here at the end of 2025, and you have Nvidia,
[516.24 --> 522.24]  you have AMD, you have Google, you have meta, you have these large players making huge investments,
[522.84 --> 523.78]  opening AI, of course.
[523.82 --> 525.54]  I mean, the list goes on and on and on.
[525.54 --> 531.00]  Which single entity do you think is best positioned to like succeed over the next 10 years?
[531.52 --> 534.88]  If you had to pick one of the top contenders, like, is it Google?
[535.00 --> 539.94]  They seem like they've really turned the corner, but I'm not sure if their capital investment on
[539.94 --> 542.82]  their own infrastructure is going to be the big win that some people are saying it is.
[542.84 --> 543.18]  I don't know.
[543.28 --> 543.74]  What do you think?
[543.74 --> 544.78]  I think there are.
[544.94 --> 547.90]  So I, I don't, I, I'm, I'm going to cheat a little bit.
[547.98 --> 549.70]  I don't really have a one.
[549.98 --> 552.86]  Um, you know, for a long time, people would say open AI.
[553.26 --> 558.74]  And before that they were saying Google, there, there is a, there's a, a top group and they
[558.74 --> 560.30]  are certainly doing well.
[560.30 --> 566.36]  And I think kind of the, at the risk of getting slightly, uh, in terms of social issues, you
[566.36 --> 571.58]  know, there's growing inequality between kind of those group of haves and kind of a lot of
[571.58 --> 573.40]  others that are have knots in that way.
[573.80 --> 582.60]  But, um, I know one of the things I think is that I, I really think that open models are
[582.60 --> 587.46]  becoming increasingly important because the difference, if you go back a few years and like
[587.46 --> 592.10]  it wasn't coming out of open AI, you know, it, there was a big performance difference
[592.10 --> 593.84]  in what you were able to do.
[594.12 --> 600.44]  And if you look at, at the, the closing of the gap between what's possible, I mean, there
[600.44 --> 607.36]  are millions of open models out there and there are hundreds of them that are in kind of like
[607.36 --> 610.66]  they are nipping at the heels of the, of the leading ones.
[610.78 --> 616.60]  And that gap between the latest, greatest thing from one of these big name companies and what's
[616.60 --> 619.48]  possible in the open world has narrowed dramatically.
[619.48 --> 625.64]  And what that's really doing is pushing, pushing model creation into something of a commodity,
[625.64 --> 626.88]  you know, area.
[626.88 --> 632.16]  And so like, I'm a, while I, and I think you've seen that in terms of what some of these big
[632.16 --> 635.72]  companies, you know, they've built services and they're building separate businesses and
[635.72 --> 638.68]  they're going into verticals and things like that.
[638.76 --> 643.44]  But that's because the, just the model generation is not going to be the profitable thing, you know,
[643.44 --> 645.06]  for years and years going forward.
[645.06 --> 651.02]  And so they're, they're, they're turning, they're turning from being AI providers explicitly
[651.02 --> 656.26]  into AI service providers now that are specific to different types of businesses.
[656.76 --> 659.64]  And, and I think they'll, I think they'll do quite well.
[659.64 --> 665.44]  I think kind of, I don't know, I I'm afraid, especially after pointing out my horrendous last
[665.44 --> 665.74]  time.
[665.86 --> 666.22]  Yeah.
[666.22 --> 671.06]  I was going to say after my horrendous NVIDIA prediction, you know, the last thing I'm going
[671.06 --> 672.58]  to go do is pick a winner here.
[672.92 --> 673.28]  Okay.
[673.38 --> 678.08]  So, but yeah, I mean, they're making a lot of money by, by pivoting, you know, within
[678.08 --> 681.02]  the scope of what they do and they have that, the expertise.
[681.24 --> 686.74]  And I mean, like meta, as we're talking now, meta is just like, just purely buying the AI
[686.74 --> 689.86]  talent, you know, like, I don't care if Google is going to pay you, I'm going to pay you 10
[689.86 --> 690.46]  times more.
[690.54 --> 694.34]  And there's no way you're going to go anyplace but us and trying to kind of catch up to that,
[694.58 --> 700.00]  that open AI, you know, which is still, as we speak, probably still the, you know, kind of
[700.00 --> 705.44]  the gold standard there, but with a few others such as, you know, such as Google, as you
[705.44 --> 709.30]  mentioned and, and other, and several others that are kind of nipping at the heels there.
[709.50 --> 711.68]  So yeah, it's interesting times.
[712.12 --> 714.12]  So a long winded answer is open AI.
[714.38 --> 715.00]  Is that what you're saying?
[716.28 --> 720.38]  You have to go back and analyze what Chris said and tease out the truth of it.
[720.62 --> 723.24]  Oh, I tried to escape that, you know, Adam, that was not fair.
[723.38 --> 727.82]  You know, I worked really hard for five minutes to kind of squirm my way out of your question
[727.82 --> 728.06]  in there.
[728.22 --> 728.50]  Yes.
[728.60 --> 729.90]  So very close.
[729.96 --> 731.46]  Oh, when you say open AI, very close.
[731.54 --> 732.48]  You got the word open, right?
[732.60 --> 732.92]  How's that?
[733.26 --> 733.44]  Okay.
[733.52 --> 733.74]  Sorry.
[733.86 --> 740.02]  Chris's answer is the open models will catch, will commoditize the frontier models, so to
[740.02 --> 740.24]  speak.
[740.24 --> 744.62]  And these people that are just, yeah, just buying all the GPUs and just training and
[744.62 --> 745.24]  training and training.
[745.34 --> 746.76]  And then of course, inference as well.
[746.88 --> 749.08]  But I mean, what you can do, it's requiring you.
[749.08 --> 754.74]  We're seeing, we're seeing this progression where we're building out frontier models is costing
[754.74 --> 755.46]  less money.
[755.66 --> 760.02]  Like there's a ton of money in some of them, but the efficiencies that are now built into
[760.02 --> 764.24]  training from some of the latest research has made it to where you can build some amazing
[764.24 --> 769.90]  stuff with not quite as much as you might've expected a year or two ago in terms of relative,
[770.24 --> 773.42]  you know, for performance against the hardware that you need to support that.
[773.42 --> 777.04]  So it might be, who knows, I mean, where the research is taking.
[777.46 --> 779.02]  Is there such thing as peak parameter?
[779.02 --> 785.58]  I mean, I think I read that XAI is next model coming out whenever is going to have a trillion
[785.58 --> 786.72]  parameters or something.
[787.04 --> 790.66]  And it's like, how large is large too large?
[790.84 --> 792.02]  Or is there no such thing?
[792.46 --> 792.70]  So, yeah.
[792.72 --> 796.12]  Well, I mean, one of the things that we've, that we've been talking about for a while now
[796.12 --> 801.64]  is the fact that like, it used to be in the early days of the, of the GBT series from
[801.64 --> 807.68]  OpenAI that, you know, you saw distinct capability differences as you went from three to three,
[807.78 --> 809.54]  five and a four and that kind of stuff.
[809.54 --> 811.96]  But there's also been, you know, we've seen kind of plateau.
[812.12 --> 817.98]  It's almost like you're seeing that a lot of the, it's not just a model thing, but also
[817.98 --> 822.22]  some of the infrastructure that's being built around it has given it a much, has made it
[822.22 --> 825.84]  much more accessible in terms of its productivity and its usefulness.
[825.84 --> 829.72]  And there's less of a friction when we're trying to use models at this point.
[829.72 --> 835.12]  So I do think that there, that like, there is no infinite rise on terms of the number
[835.12 --> 836.40]  of parameters you have to do.
[836.46 --> 839.04]  I think, I think that that does level out.
[839.48 --> 844.48]  And also like, if you're going to have that many parameters, being able to, to use that
[844.48 --> 849.72]  productively from an inference standpoint, the world is turning out to be a mini model world
[849.72 --> 852.12]  instead of a giant model world, you know?
[852.20 --> 857.00]  And so, yeah, and I'm not sure that a lot of people in the general public, you know, that
[857.00 --> 860.20]  aren't people like us that follow this closely really realize that.
[860.30 --> 864.24]  I think when they think AI, they're thinking chat GPT because it's what they know.
[864.24 --> 867.08]  And, you know, one model to rule them all, one model to bind us.
[867.20 --> 871.22]  And like, I'm not at all, like, that's not what I think is the world.
[871.22 --> 878.12]  I think the world is, is many, many models contribute to solving a problem in various ways.
[878.12 --> 885.56]  And, you know, we're, here we are in 2025, deeply into the, the, the agent, the age of agents.
[886.36 --> 891.66]  And, and so it's no longer just models, but now agents with models that are, that they're
[891.66 --> 892.90]  acting on your behalf.
[892.90 --> 897.18]  And, and I think it's, the reality is it's a mini, it's a mini agent future that we're
[897.18 --> 898.04]  talking about here.
[898.56 --> 902.14]  Before we go there, I got to ask you, cause we're talking about companies and predictions
[902.14 --> 903.76]  and potential here.
[903.84 --> 909.60]  Have you tapped into or heard of the next Jeff Bezos thing, Prometheus and the startup
[909.60 --> 912.56]  he's chairing, co-founding, et cetera.
[912.70 --> 913.96]  Are you, are you tapped into that?
[914.08 --> 915.70]  I'm not, I'm not up to date on the details.
[915.88 --> 917.18]  That's like half the press, isn't it?
[917.22 --> 917.88]  They announced that.
[918.00 --> 921.02]  It's like yesterday's news, basically today, today's news.
[921.40 --> 925.68]  I think there's like a perpetual Bezos Musk pissing contest that goes on.
[925.68 --> 927.04]  And this seems like the next one.
[927.10 --> 929.06]  He's like, you have XAI, I've got this thing.
[929.06 --> 935.44]  According to TechCrunch, Jeff Bezos reportedly returns to the trenches as co-CEO of new AI
[935.44 --> 938.12]  startup Prometheus, Project Prometheus.
[938.98 --> 946.94]  So he hasn't done anything from a CEO aside from shareholder, you know, chairman, et cetera,
[946.94 --> 948.22]  behind Amazon.
[949.22 --> 952.18]  He's been just, you know, getting swole essentially.
[952.42 --> 954.68]  Just getting swole and going to space.
[954.84 --> 955.32]  On his yacht.
[955.52 --> 955.68]  Yeah.
[955.80 --> 956.06]  Yeah.
[956.16 --> 957.30]  As you would, if you were.
[957.30 --> 958.46]  He's been doing the space stuff.
[958.46 --> 959.66]  He's been doing Blue Origin.
[959.84 --> 960.32]  That's what I said.
[960.38 --> 961.78]  Like you're getting swole and going to space.
[961.90 --> 962.78]  Oh, that's what he's been doing.
[962.88 --> 963.02]  Yeah.
[963.14 --> 963.28]  Yeah.
[963.78 --> 968.62]  So this is kind of cool that I suppose the next big thing could be from him.
[968.76 --> 973.32]  So maybe the next time we talk, Chris, you can give us your non-prediction prediction.
[975.00 --> 976.58]  I can slide out of that one too.
[976.76 --> 977.00]  Yeah.
[977.08 --> 979.04]  Like do we go by Amazon right now?
[979.10 --> 979.98]  That's what we want to know, Chris.
[980.42 --> 985.10]  So, so I, you know, I, I'm probably the wrong person to talk to about this.
[985.10 --> 989.22]  Not only because of the prediction that we just talked about, but also I want to point
[989.22 --> 995.38]  out, like, I, I am honestly, like this may sound really counterproductive as, you know,
[995.46 --> 1000.28]  practically I co-host on this, but I'm, and I think Daniel's the same way.
[1000.36 --> 1004.44]  We're less interested in kind of the big, big names coming out with their latest big
[1004.44 --> 1010.98]  things because there's so much amazing work being done by like real people out there.
[1010.98 --> 1014.40]  You know, like, like, there's the, there's the chat there.
[1014.52 --> 1014.68]  Yeah.
[1014.92 --> 1019.30]  Plastic Jeff Bezos is like, hi, I'm Jeff Bezos is kind of, you know, like in, in, in Elon
[1019.30 --> 1020.66]  Musk and all these guys.
[1020.66 --> 1025.10]  And I'm just like, yeah, they're always one upping each other and they do some big things.
[1025.10 --> 1032.88]  But like, like, I think like 99% of the press is going to this, these, these people, but
[1032.88 --> 1039.06]  I think 99% of the real productive work in AI is going to all these invisible masses of
[1039.06 --> 1042.34]  amazing people that are doing the stuff every day.
[1042.34 --> 1048.22]  And like, I, I'd like, you know, if I could, if, if I could get the mainstream press to
[1048.22 --> 1054.16]  kind of like refocus, I'd be like, I'd lay like, like look around, like there's just,
[1054.44 --> 1059.04]  there's just astounding, amazing things that are happening, but they're not happening by
[1059.04 --> 1060.32]  these like famous figures.
[1060.32 --> 1064.28]  And these guys, I guess they have tons of money and they're super, super ultra wealthy
[1064.28 --> 1069.32]  beyond imagination and, and they can throw their money around and stuff.
[1069.32 --> 1073.36]  But you kind of mentioned, it's kind of the pissing contest, for instance, between some
[1073.36 --> 1073.74]  of them.
[1073.92 --> 1077.06]  And I just like, there's so much cool stuff out there.
[1077.52 --> 1084.08]  That's not, that's not the latest, you know, the latest Bezos, you know, Elon Musk.
[1084.66 --> 1084.78]  Yeah.
[1084.98 --> 1085.68]  Massive thing.
[1086.06 --> 1091.64]  I mean, $6.2 billion behind this thing is quite like crazy, quite a, an investment in there
[1091.64 --> 1092.68]  that he's raised for it.
[1092.70 --> 1094.00]  $6.2 billion.
[1094.66 --> 1095.18]  What are they doing?
[1095.30 --> 1095.92]  What's their deal?
[1096.62 --> 1098.06]  It's only speculative at this point.
[1098.06 --> 1104.60]  It's only got a name, Project Prometheus, Jeff Bezos, co-founder, I believe is, is Vic.
[1105.26 --> 1107.44]  I would only mess up the last name.
[1107.54 --> 1110.78]  B-A-J-A-J is the last name of Vic.
[1111.84 --> 1116.58]  Can you imagine being able to throw $6.2 billion at something that you don't really know what
[1116.58 --> 1117.08]  it is yet?
[1117.44 --> 1117.80]  Right.
[1118.10 --> 1118.68]  Well, I think he knows.
[1118.68 --> 1119.14]  I'm just saying.
[1119.32 --> 1120.14]  I don't know if we know.
[1120.14 --> 1125.54]  I think you've already checked for $6.2 billion or you even raised those funds.
[1125.88 --> 1126.10]  You guys.
[1126.34 --> 1128.06]  The reason he announced it is to get better raises.
[1128.28 --> 1128.40]  Yeah.
[1128.56 --> 1129.02]  That's right.
[1129.32 --> 1130.96]  Some version of more money.
[1131.06 --> 1131.82]  Get people interested.
[1131.94 --> 1137.38]  So, Chris, you probably can't convince the mainstream media to ignore, you know, the 800-pound
[1137.38 --> 1139.00]  gorillas, but you can convince us.
[1139.10 --> 1139.94]  So, here we are.
[1140.00 --> 1140.38]  We're ready.
[1141.08 --> 1141.72]  What's cool?
[1141.84 --> 1143.00]  What's underneath the covers?
[1143.00 --> 1148.26]  Or, like, what's the invisible stuff that people are doing that you and Dan and we should
[1148.26 --> 1149.06]  be interested in?
[1149.82 --> 1153.76]  So, I think, like, it's funny.
[1153.94 --> 1158.50]  We just, I'm going to say something that I said the other day, and I'm starting to say
[1158.50 --> 1159.06]  it more and more.
[1159.20 --> 1164.08]  But, like, I think people easily look around wherever they are in the world and whatever
[1164.08 --> 1167.76]  their politics are, and it feels like a difficult moment.
[1167.76 --> 1173.18]  And it feels like, you know, there's all these things you can point at and say, we're going
[1173.18 --> 1177.46]  through a really tough time, and it's tough, and everyone's trying to figure out.
[1177.60 --> 1180.48]  But I want to offer a counter-narrative to that.
[1181.22 --> 1187.72]  We're also at this moment where this stuff is, you know, the AI, and there's a hardware
[1187.72 --> 1193.02]  revolution going on, and there's a robotics revolution going on all together, and they're
[1193.02 --> 1195.50]  all, you know, connected, and they're powering each other.
[1195.50 --> 1201.08]  And I think we live in the coolest moment in human history right now.
[1201.14 --> 1203.34]  Like, we are sitting in it as we speak today.
[1204.28 --> 1211.14]  And so, what's happening right now is with all of these different relevant, you know,
[1211.18 --> 1216.12]  capabilities, you know, and the robot people, and the AI people, and the software people,
[1216.12 --> 1218.08]  and the hardware people, it's all coming together.
[1218.48 --> 1223.58]  And you can do amazing stuff today that even a year ago, we couldn't do.
[1223.58 --> 1229.10]  I mean, it's like, if you think about before now, we would, we'd had kind of have several
[1229.10 --> 1234.40]  years of little software eras, you know, and we were, we were getting into certain ecosystems
[1234.40 --> 1237.66]  with a language or whatever, and they kind of run for a few years.
[1237.92 --> 1243.14]  But right now, it's changing so fast, and the capability is coming so fast, that, like,
[1243.68 --> 1249.62]  aside from the big 800-pound gorilla types and stuff, like, everybody can get into this stuff.
[1249.62 --> 1257.18]  And so, I think we're at a moment right now where, like, it's really going to start being
[1257.18 --> 1260.94]  pervasive in everyone's life in a bigger way than it has been.
[1261.02 --> 1264.86]  Not just, like, I'm going to open my phone up and talk to chat GPT kind of way.
[1265.18 --> 1269.60]  Because, yeah, I mean, that was unimaginable if you think about it just a few years ago.
[1269.76 --> 1273.64]  It wasn't, it hasn't been long since that was an unimaginably amazing thing to do.
[1274.04 --> 1276.76]  But that's, like, we don't even think about that now.
[1276.76 --> 1278.82]  You know, we do it all the time, don't even think about it now.
[1279.10 --> 1285.96]  But, like, physical AI and the fact that robotics have come so far in the last few years and
[1285.96 --> 1291.62]  that you're, and that now there are, in addition to NVIDIA, there are many other chip makers
[1291.62 --> 1293.46]  that are coming on scene to support AI.
[1293.70 --> 1298.62]  And some of them are doing more of the dedicated AI chips, and others are doing more like, you
[1298.62 --> 1301.74]  know, combining different types of chips so that you have that.
[1301.74 --> 1307.08]  And some are great for data centers, you know, big cloud data centers, and others are great
[1307.08 --> 1309.92]  for edge devices and tiny little constructs.
[1309.92 --> 1316.16]  And I think, like, you're going to see so much happening in the marketplace right now that
[1316.16 --> 1317.14]  are coming from startups.
[1317.14 --> 1319.44]  They're not coming from the 800-pound gorillas.
[1320.20 --> 1322.52]  They'll have their fair share at 6.2 billion.
[1322.64 --> 1322.94]  They better.
[1324.30 --> 1325.40]  Or do something with that.
[1325.40 --> 1330.80]  Yeah, you're going to see amazing capabilities coming out of fairly small companies.
[1331.16 --> 1337.20]  And, like, and to, speaking back again to Daniel Whitenack, my co-host and part of our
[1337.20 --> 1341.80]  family in this, he, you know, he started his own company, which is kind of supporting that.
[1342.26 --> 1344.08]  And that's what I like seeing.
[1344.16 --> 1347.26]  He has PredictionGuard, which is kind of supporting open model approach.
[1347.60 --> 1353.44]  And I think that, in general, that approach of anybody can go, whether you're using a cloud
[1353.44 --> 1360.06]  environment or startup like Daniel's or something like that, you can go productively pull down
[1360.06 --> 1366.40]  models from Hugging Face, you know, which I liken to GitHub for AI, you know, the way GitHub
[1366.40 --> 1371.26]  has always been for software, combine a bunch of different, fairly sophisticated open source
[1371.26 --> 1375.60]  software packages, and do some amazing things without 6.2 million.
[1375.78 --> 1379.72]  You can do it as a college student in the dorm, figuratively speaking.
[1379.72 --> 1385.22]  Um, and that's, that's like what that's the thing that really excites me is that is the
[1385.22 --> 1391.12]  ability to everyone becomes a maker, if you will, everyone out there can become it once
[1391.12 --> 1394.52]  upon a time, we were kind of like, you know, hey, we have the internet, everyone can be
[1394.52 --> 1398.24]  a software developer, you know, all the stuff you need to learn is online.
[1398.46 --> 1401.40]  And there's all these resources, a lot of it can be done for free.
[1401.58 --> 1403.40]  It doesn't matter where in the world you are.
[1403.40 --> 1405.54]  Well, now everybody can become a maker.
[1406.08 --> 1410.62]  Everybody can take, it can, can access these different things and go do something great.
[1410.62 --> 1416.30]  And I think that's that the fact that like, we all have these like Roomba type things,
[1416.40 --> 1421.06]  you know, rope, these, these vacuums in our houses and, and everybody is now completely
[1421.06 --> 1421.78]  used to that.
[1421.88 --> 1426.68]  But I think we're right on the cusp of having lots of little devices like that in our houses
[1426.68 --> 1431.58]  and our businesses that are doing all these things, which eventually will get us into
[1431.58 --> 1434.58]  this, this notion of swarming that we're, that we're going to talk about.
[1435.04 --> 1436.36]  I'm ready for the little robots.
[1436.60 --> 1440.12]  I don't want the big scary robots, but I like the little robots that help you do things.
[1441.28 --> 1442.58]  The Neo thing is weird.
[1442.66 --> 1444.60]  We don't have to talk about that, but that was kind of strange.
[1444.96 --> 1445.44]  Was it Neo?
[1445.62 --> 1446.08]  It wasn't Neo.
[1446.24 --> 1446.90]  John Mnemonics.
[1447.08 --> 1447.96]  You think Johnny Mnemonics?
[1448.36 --> 1448.54]  Yeah.
[1448.56 --> 1449.34]  What's Johnny Mnemonics?
[1449.76 --> 1453.24]  Well, Johnny Mnemonics was like, he had, man, I can't remember this one, but it was same
[1453.24 --> 1454.54]  actor Keanu Reeves.
[1454.54 --> 1459.66]  And I believe he had like, oh, he had something in him and he was carrying data.
[1460.50 --> 1461.56]  And it was vaguely.
[1461.70 --> 1462.28]  I recall this.
[1462.36 --> 1462.48]  Yeah.
[1462.48 --> 1465.98]  It was like the idea of a mule, but not drugs.
[1466.30 --> 1466.46]  Yeah.
[1466.54 --> 1468.02]  It was, that was back when he was young.
[1468.60 --> 1469.00]  Yes.
[1469.22 --> 1469.58]  Yes.
[1470.00 --> 1471.52]  I thought you were talking about Johnny Mnemonics.
[1471.52 --> 1475.18]  You jumped right to the matrix, which makes sense, Adam, because most of my references
[1475.18 --> 1479.64]  are the matrix, but I was actually talking about this new robot in your house that costs
[1479.64 --> 1481.80]  20 grand and it's controlled by a human currently.
[1481.80 --> 1485.20]  I saw that, but I still don't think that's going to be the thing.
[1485.32 --> 1485.86]  No, I don't think so.
[1485.88 --> 1487.22]  I would say that's kind of weird at this phase.
[1487.26 --> 1488.90]  Like that's, it's a general purpose.
[1488.90 --> 1490.22]  Like it does laundry.
[1490.22 --> 1491.58]  It does your dishes.
[1492.12 --> 1496.54]  And it's like a humanoid full size, similar to what the optimists, you know, think that
[1496.54 --> 1496.92]  they're building.
[1497.78 --> 1501.52]  And yet it's at this point because they need data to train these models better.
[1501.56 --> 1502.78]  It's not at all autonomous.
[1502.78 --> 1507.58]  It's controlled by a human with what I imagine is like a sophisticated joystick, you know, probably
[1507.58 --> 1508.22]  overseas.
[1508.24 --> 1510.12]  It's kind of creepy when you think about it, isn't it?
[1510.12 --> 1510.90]  It's super creepy.
[1510.90 --> 1514.60]  Your grandma's in there with a stranger in the form of a robot.
[1514.76 --> 1516.64]  The Wall Street Journal did a great video about it.
[1517.36 --> 1521.54]  Like, you know, Joanna Stern told it to do the dishes or something.
[1521.64 --> 1525.80]  And it took like three minutes to load a cup into the, you know, into the dishwasher, which
[1525.80 --> 1527.30]  is a 15 second task.
[1527.36 --> 1527.50]  Anyway.
[1527.70 --> 1528.10]  Let's not do that.
[1528.16 --> 1528.34]  Yeah.
[1528.42 --> 1529.34]  It's not there yet.
[1529.38 --> 1531.80]  I feel like that's being too big in general purpose.
[1531.88 --> 1536.38]  I feel like more specific, small, like sink, like the Roomba, you know, it's going to vacuum.
[1536.38 --> 1541.16]  The Roomba is the future is that like that, that was an early, you know, thing, but like
[1541.16 --> 1544.40]  it's, it's purpose built for a very specific thing.
[1544.90 --> 1548.82]  And it's, and there's a whole bunch of them on the market, you know, a bunch of different
[1548.82 --> 1551.40]  makes and manufacturers and stuff on the market.
[1551.40 --> 1555.98]  And you can, we can go through and debate what's better and all that kind of stuff.
[1556.04 --> 1561.62]  But I think you're seeing that times many, many, many things across all sorts of tasks
[1561.62 --> 1567.28]  and like they're cheap and like even Roomba type, you know, the vacuums are too expensive
[1567.28 --> 1567.82]  right now.
[1567.88 --> 1573.48]  I think as I think with the cost of robotics coming down and accessibility, then it's like
[1573.48 --> 1579.82]  the, if you think, you know, outside this and just walking into a retail store or getting
[1579.82 --> 1584.62]  online to Amazon or whatever, and just buying something, you know, that once upon a time
[1584.62 --> 1587.04]  might've been expensive and now it's 30 bucks, you know?
[1587.36 --> 1592.08]  And I think that like, you know, in this day and age, that 30 buck purchase, I think that,
[1592.08 --> 1596.44]  you know, getting a robot that'll do this and that and the other, and the fact that they
[1596.44 --> 1602.26]  have eventually, uh, you know, you have families of robots that can do different things and you
[1602.26 --> 1606.72]  can put it in swarming mode and just say auto my house and swarming mode as we'll get into.
[1606.72 --> 1609.38]  And they just like coordinate and do all the stuff.
[1609.50 --> 1611.86]  They're sensing you, they're moving around you, you're doing the thing.
[1612.50 --> 1614.24]  And, and that's, that's real life.
[1614.32 --> 1620.42]  You know, you have, you know, you know, aside from just the vacuum, your, your lawn and garden
[1620.42 --> 1626.76]  care is getting taken care of your security around your house, your roof and gutter inspections,
[1626.76 --> 1630.84]  you know, it's integrated into your smart home stuff.
[1630.94 --> 1635.66]  You're like, you know, you don't have to worry anymore about where your packages were left
[1635.66 --> 1640.88]  by the delivery driver because the, the, those robots or the swarms that are managing
[1640.88 --> 1642.46]  your house are just doing that.
[1642.60 --> 1644.62]  And it's not insanely expensive.
[1644.74 --> 1645.52]  People are like, yeah, yeah.
[1645.54 --> 1649.88]  Where am I going to get the 6.2 billion from Bezos to buy my swarm for my house?
[1649.92 --> 1651.86]  And I'm like, no, no, it's not.
[1651.92 --> 1653.42]  You're going to have the Christmas deal.
[1653.50 --> 1658.04]  You know, we're coming up on the holiday time and you're going to get online and you'll
[1658.04 --> 1661.60]  have all the different packages about what level of swarming do you want?
[1661.60 --> 1665.64]  This one is an 18 accessory swarm package that you can come.
[1665.74 --> 1667.12]  It's going to handle your outside.
[1667.24 --> 1668.02]  It's going to do this.
[1668.08 --> 1669.56]  And you're like, you're trying to choose.
[1669.64 --> 1670.54]  You're like, well, I don't know.
[1670.84 --> 1676.20]  You know, I'm going to spend more, I'm going to spend more for my kids, you know, on that.
[1676.30 --> 1681.40]  But, you know, there's, there's, there's great aunt, you know, Louise, and we only talk
[1681.40 --> 1684.54]  to her once every five years and I send her kind of a token thing.
[1684.62 --> 1689.56]  So I'll send her the four items swarm package, you know, that she can add into whatever she's
[1689.56 --> 1691.48]  already using because it's all open stuff.
[1691.48 --> 1695.50]  And like, that's not like, that's going to be normal.
[1695.50 --> 1698.38]  And we're not that far from the opportunity.
[1698.38 --> 1701.64]  And it's not the 800 pound gorillas that are going to bring that.
[1701.74 --> 1704.16]  It's going to be the billions of startups out there.
[1704.54 --> 1709.32]  They're each doing a little piece of it and they're, and they're swarm components and stuff
[1709.32 --> 1710.16]  are able to communicate.
[1710.68 --> 1712.28]  That's the future that we're going to build.
[1712.42 --> 1713.18]  Well, I'll tell you one thing.
[1714.02 --> 1716.68]  You've definitely put a lot more pressure on the idea of home lab.
[1716.68 --> 1719.22]  That's for sure, because that's all home lab.
[1720.02 --> 1723.30]  Those are a ton of DNS queries out there.
[1723.42 --> 1725.40]  Probably a ton of telemetry being tracked.
[1725.62 --> 1729.00]  A lot of, yeah, a lot of things you may or may not be concerned.
[1729.06 --> 1732.64]  Those are things I think about when I think about adding more and more devices to my home.
[1734.02 --> 1734.88]  Gosh, man.
[1735.40 --> 1739.46]  So separate, I got to, I have a slight side story, but it contributes to that.
[1739.72 --> 1744.92]  So about a year ago now, almost exactly a year ago, we bought and moved into the house
[1744.92 --> 1745.64]  that I'm in now.
[1746.26 --> 1752.82]  And the guy that we bought it from, he and his wife, he was a fanatical home automation
[1752.82 --> 1754.00]  person.
[1754.42 --> 1760.44]  And so like, um, we moved in, um, not because of the automation that was incidental, but
[1760.44 --> 1766.84]  like it's had, it's helped me move from just like thinking like more of a professional kind
[1766.84 --> 1767.18]  of thing.
[1767.18 --> 1771.12]  Like, you know, we're talking AI and a professional kind of to thinking about stuff around the
[1771.12 --> 1774.86]  house, um, with all the sensors and the cameras and stuff.
[1774.86 --> 1780.06]  And, um, we have all the, you know, the, the various types of home automation stuff that
[1780.06 --> 1782.44]  you see out there combined costs is here.
[1782.52 --> 1787.40]  Every, like we have many, many, many dozens of costs devices all over the place.
[1787.58 --> 1789.24]  And costs is the brand that from Lutron.
[1789.32 --> 1789.64]  Is that right?
[1789.66 --> 1790.34]  Am I picking that right?
[1790.34 --> 1792.90]  Uh, it's from a TP link actually.
[1793.04 --> 1793.24]  TP.
[1793.42 --> 1797.66]  Um, but that's just one, there's a whole bunch of them and, you know, Apple home and Google
[1797.66 --> 1797.88]  home.
[1797.98 --> 1798.58]  I was thinking Casita.
[1798.72 --> 1799.62]  Casita is from Lutron.
[1799.78 --> 1800.72]  Those are the light switches.
[1800.94 --> 1801.12]  Yeah.
[1801.20 --> 1801.40]  Yeah.
[1801.54 --> 1807.36]  The Lutron does the light, it does light switches, but like they all, there's some common, um,
[1807.44 --> 1808.72]  protocols that they all work on.
[1808.76 --> 1813.10]  And I'm starting to see like, I move, like, because I didn't have to go start it from scratch
[1813.10 --> 1817.10]  and because I inherited what this guy had already kind of put together and then had to figure
[1817.10 --> 1822.02]  it out and make it work. And suddenly I'm like, well, gosh, it would be really easy to add this.
[1822.18 --> 1827.22]  Like, and we're, we're talking about this robotic future, even in our homes, not just a commercial
[1827.22 --> 1832.72]  or industrial or whatever thing, but in our homes, like it's so easy for me to see that now.
[1833.28 --> 1838.74]  Because like, I realized I already have a good bit of infrastructure here and it's not expensive
[1838.74 --> 1842.94]  and it's not, it just takes a little bit of effort. And if they can make that easier for people to
[1842.94 --> 1846.84]  get into, it's a done deal. Like, you know, we already have what we, we,
[1846.84 --> 1850.96]  we already have wifi and all the other things. And then you start, start adding things to plug
[1850.96 --> 1854.78]  in. It's, it's like Legos. It's like home automation Legos in your home.
[1854.78 --> 1877.06]  Well, friends, you know, that feeling your team has solid ideas. You got some good stuff in there,
[1877.06 --> 1882.04]  but there's this gap between these brainstorm sessions and actually shipping the stuff.
[1882.04 --> 1888.58]  weeks of back and forth, scattered feedback. You're in chat GPT friends and colleagues are
[1888.58 --> 1894.66]  in clod and somebody else is in clod code. And it's just everywhere, right? You're throwing AI at
[1894.66 --> 1898.62]  it. It's not solving the problem. It just gets messier. Well, Miro, they flip the script.
[1899.12 --> 1904.64]  Miro's innovation workspace. It is powered by AI and it turns work that normally takes weeks
[1904.64 --> 1911.12]  in today's. Here's the magic. Miro AI sidekicks aren't there to replace your thinking. They're
[1911.12 --> 1916.50]  there to extend it. And custom sidekicks that think like product leaders, agile coaches, or
[1916.50 --> 1920.86]  product marketers, they review your materials. They highlight what to double down on and they
[1920.86 --> 1926.14]  catch gaps for you. So you're not spending weeks, hours, days, months, whatever, going down the wrong
[1926.14 --> 1931.84]  road without details. It integrates directly into your workflow as an extension of your team's
[1931.84 --> 1936.70]  capabilities, not a replacement. You can generate insights faster without tool switching.
[1937.10 --> 1943.78]  Miro AI sorts through everything. Sticky notes, research, ideas, different formats, and combines
[1943.78 --> 1950.30]  them into structured research summaries, product briefs, sentiment analysis, you name it. Test 20
[1950.30 --> 1955.48]  concepts rapidly with Miro prototypes, generating instant prototypes right from your board so you can
[1955.48 --> 1961.04]  iterate on variations and feel confident about feasibility before you get into the heavy builds.
[1961.04 --> 1967.40]  And this opens the door for teams to move at a brand new speed, the speed of their ideas, the speed
[1967.40 --> 1975.18]  of enhanced thinking, spend time building the right things, not digging for information, get great done.
[1975.62 --> 1982.66]  If you're ready to move faster, check out our friends over at Miro, rhymes with hero, M-I-R-O.com.
[1982.94 --> 1984.90]  Once again, Miro.com.
[1984.90 --> 1995.26]  Speaking of Legos and home automation, IKEA just announced a whole new set of like 27 smart home
[1995.26 --> 2000.26]  things coming from IKEA. I saw that. Talk about bringing it to the masses. Like that's the kind
[2000.26 --> 2005.00]  of thing that IKEA brings to the masses now is they make it very simple and straightforward and Lego
[2005.00 --> 2010.16]  esque in order to, and it all runs on Matter, which is like, I think the open standard for
[2010.16 --> 2011.30]  communication between these things.
[2011.36 --> 2016.02]  And so like Matter's in an interesting place and that like, I only buy things that, that are
[2016.02 --> 2021.62]  Matter, that have Matter integrated in. And for, for listeners and viewers, the Matter is a protocol
[2021.62 --> 2027.20]  that allows different makes and models of automation to work together over a common protocol. And it's
[2027.20 --> 2032.94]  local based instead of cloud based. And so like, but not everything does it yet. So it's still kind of
[2032.94 --> 2038.98]  working. It's been very slow. It took a long time to kind of come into, into play, but it seems to be
[2038.98 --> 2044.52]  having a second wind right now because of all this new capability that's coming about. And so like
[2044.52 --> 2050.46]  every new thing I buy, whether I'm using Matter yet on that or not, I have to have Matter so that as I
[2050.46 --> 2056.02]  go forward, I can integrate into that. But like, yeah, you know, everything is, it's local, it's Matter.
[2056.02 --> 2062.56]  Matter. And I'm finding with today's craziness out there that I'm moving more local and a little
[2062.56 --> 2066.32]  bit more out of the cloud. And so Matter is becoming increasingly important from my standpoint.
[2066.78 --> 2071.50]  Well, from the startup perspective and the swarming, perhaps at least the droning perspective,
[2071.94 --> 2077.94]  you'll be happy to hear Chris, that we do have a startup coming on soon, Zipline, who are now moving
[2077.94 --> 2084.82]  delivery drones into production. They actually have a delivery drone system that is started off
[2084.82 --> 2089.94]  delivering medical needs in Africa, vaccines and stuff like that. And now they're moving into the
[2089.94 --> 2095.64]  States and they're doing a food delivery, small item delivery, small package. So you think your
[2095.64 --> 2100.16]  Chipotle burrito, that kind of thing. Yeah. You're, you know, eight pounds or less. Yeah. Eight pounds or
[2100.16 --> 2103.50]  less. It's super cool stuff. And they've got it to where they're actually rolling out into,
[2103.64 --> 2108.64]  into commercialization now. So startups are making moves in this direction. And now there's our,
[2108.64 --> 2116.40]  I'm assuming in each city, they have a fleet of these delivery drones. Obviously each drone is
[2116.40 --> 2122.22]  is operated on its own. I assume eventually autonomously. It actually seems like a simpler
[2122.22 --> 2127.86]  problem than autonomous cars because the airspace is just pretty open, right? Like you got problems like
[2127.86 --> 2134.02]  wind and snow and stuff like that birds, but it's gotta be easier than cars.
[2134.02 --> 2139.78]  Yeah. Generally. And so it's a different problem. So it's easier. There's easier.
[2140.56 --> 2145.60]  It's a little bit of both. It kind of depends on how you're looking at it with cars. Uh, and,
[2145.70 --> 2150.28]  and like we were just talking to Waymo again, uh, a few weeks ago in practical AI about this. So this
[2150.28 --> 2155.20]  is very top of mind for me, um, with cars. Yeah, there are a lot of challenges and you have the,
[2155.20 --> 2158.80]  the notion of the, you know, the child running out or the ball bouncing out and then, you know,
[2158.80 --> 2164.28]  there's a lot of stuff that's right there, but also you're, you know, what you're, how you're
[2164.28 --> 2169.88]  navigating is very well defined in terms of the streets and stuff like that. Uh, air becomes more
[2169.88 --> 2175.58]  three-dimensional. And so the challenges are different, but so long as it's not highly congested,
[2175.64 --> 2179.46]  your, I would agree with you that it is generally easier that you can kind of move from here to there.
[2179.46 --> 2184.24]  And so long as you have good collision avoidance, uh, and some other, you know, capabilities for
[2184.24 --> 2190.04]  navigation there, then you're probably doing okay. Um, though that changes with swarming because
[2190.04 --> 2195.86]  swarming brings in close collaboration. Yeah. So define swarming then, because I think of killer
[2195.86 --> 2200.98]  bees when I hear swarming and I assume with drones, you're talking about a bunch of drones nearby each
[2200.98 --> 2207.08]  other then. You are. And, and it's in whether, and it's not just a physical distance thing because
[2207.08 --> 2212.22]  what distance, what is physical distance is a relative thing, depending on what it is you're trying to do.
[2212.22 --> 2216.54]  Um, but it also, it's really more about behavior. And so we can dive into that.
[2216.54 --> 2221.74]  But before you say that we can, we, I think that's a, a line of thought we should go down is that
[2221.74 --> 2226.18]  as, uh, as you guys know, I'm really into animals. We were making jokes earlier about
[2226.18 --> 2231.42]  bazillion dogs and stuff like that. Uh, I'm a licensed wildlife rehabber and I study animals.
[2231.42 --> 2236.58]  And in the context of swarming, mother nature has perfected, not just swarming, but there are many
[2236.58 --> 2244.04]  different types of swarming from different species. And so I, I have a set of species that I tend to
[2244.04 --> 2250.54]  look to for swarming purposes and say, if I want to swarm with this type of technology or this type
[2250.54 --> 2257.88]  of platform, like how do we get started on that? You know, how do we get inspiration or, or look for
[2257.88 --> 2263.88]  some insights on the technology where you can look to certain species that are, that are similar to the
[2263.88 --> 2268.38]  technology platforms you're interested in terms of how they move around and do stuff and say, well,
[2268.38 --> 2273.52]  how, how has nature solved it there? And I definitely do that a lot. I, I, it's not uncommon for me to go
[2273.52 --> 2278.96]  into tech, um, meetings and start off with lots of pictures of animals and stuff and people like,
[2279.00 --> 2285.30]  what's, what's going on with this business guy. Are you thinking like fungus bees and bees bat? Like I do a
[2285.30 --> 2291.38]  lot of bees, bats, birds, uh, starlings, you know, the, those huge, what are called murmurations of
[2291.38 --> 2298.30]  starlings? Answer. Awesome. Answer. Awesome. When, when, uh, when I'm thinking about robotics on the
[2298.30 --> 2306.62]  ground, uh, meaning, uh, what we would call, uh, a UGV, which is an unmanned or uncrewed ground vehicle.
[2307.02 --> 2312.56]  Um, ants are amazing in what they can do. Uh, and so they're, they're an awesome thing to look at,
[2312.56 --> 2318.80]  but for the, I'll start with the definition that I use. Um, given the fact that I work in the, uh,
[2318.80 --> 2325.38]  in the military intelligence space, uh, my definition sounds kind of, it uses that jargon,
[2325.38 --> 2332.68]  but it really don't get caught up in that. It can be applied to residential. It can be applied to
[2332.68 --> 2336.32]  commercial. It can be applied to industrial. So don't get caught up in this specific wording.
[2336.44 --> 2339.82]  So I'm going to, I'm going to read it in front of me. It's one really long run on sentence.
[2339.82 --> 2346.24]  It's very specific in what it's trying to imply. Um, it is swarming occurs when numerous
[2346.24 --> 2354.06]  independent, fully autonomous, multi-agentic platforms exhibit highly coordinated locomotive
[2354.06 --> 2359.96]  and emergent behaviors with agency and self-governance in any domain, which could be air,
[2360.38 --> 2367.32]  ground, sea, undersea, or space functioning as a single independent, logical distributed,
[2367.32 --> 2374.20]  decentralized decisioning entity for purposes of C3, which is command control and communications
[2374.20 --> 2380.84]  with human operators on the loop to implement actions that achieve strategic, tactical,
[2380.84 --> 2386.88]  or operational effects in the furtherance of a mission. So long, long, long sentence,
[2386.88 --> 2392.00]  but it hits a bunch of very precise concepts and integrates them in together.
[2392.36 --> 2394.18]  I can tell each word was selected there.
[2394.18 --> 2399.84]  Yeah. A mission might be, instead of thinking military, a mission might be, uh, getting a package
[2399.84 --> 2405.04]  to your house. That might be the mission. And that does have command control and communications
[2405.04 --> 2410.74]  involved. So like you can put the, you can, it doesn't have to be the, the military-esque,
[2410.74 --> 2415.68]  uh, jargon that we're talking about. Yeah. Yeah. It applies to any of these, to any of these,
[2415.68 --> 2419.48]  you know, commercial, industrial, residential, military, whatever.
[2421.48 --> 2423.92]  So, so that's a lot.
[2423.92 --> 2429.18]  Yeah. It's a lot. It's a lot. And if you want, I can kind of break down high level what some of those
[2429.18 --> 2432.32]  mean. Yeah. I think my broad takeaway, we can talk about the individual words because I know
[2432.32 --> 2438.58]  they're very specifically chosen, like independent, logical, distributed, decentralized decisioning
[2438.58 --> 2444.02]  entity, like stuff like that. I can tell each word was selected for a reason. But I think my grand
[2444.02 --> 2451.50]  takeaway of a swarm is kind of the e pluribus unum. Like it's like, okay, all these things are individual
[2451.50 --> 2456.20]  and autonomous, but they're all acting as one. They're acting with one purpose.
[2456.54 --> 2462.52]  That's a fantastic insight that you have. And that, that is the key to it is like swarm is such
[2462.52 --> 2467.08]  a buzzword. You know, we, we always have buzzwords in, in this AI and software spaces. There's always
[2467.08 --> 2474.66]  the buzzwords of the year and swarm is certainly a huge buzzword right now. And, and almost without
[2474.66 --> 2480.26]  exception, I will turn around and tell it, I can go back to my definition, assuming that you want to
[2480.26 --> 2484.16]  accept that as the definition of swarming. And I can defend that fiercely.
[2484.76 --> 2486.48]  I cannot attack it. Can you attack it, Adam?
[2489.04 --> 2490.24]  You're the expert here, Chris.
[2490.68 --> 2494.20]  But I would say like all you people who are talking swarming, no, you're not,
[2494.34 --> 2499.28]  it's not swarming. What you're describing is all sorts of things that lead to swarming.
[2499.62 --> 2505.52]  There's a whole bunch of incremental capabilities that, that would eventually, as you add all those
[2505.52 --> 2512.58]  capabilities together, they culminate in swarming. Right. But, but the chances of somebody saying that
[2512.58 --> 2519.04]  what they're doing out there is, is consistent with Chris Benson's definition of swarming. Right.
[2519.12 --> 2526.62]  It's pretty low. So you, what you said was right on. And that is that, that just as you see in nature,
[2526.62 --> 2532.96]  with those ants, all, every little ant has its, you know, neural capability, shall we call it,
[2532.96 --> 2540.16]  you know, and what it's doing. But at the end of the day, they're functioning to get a mission done,
[2540.24 --> 2547.84]  a job done, something productive for the colony. And they are all lending themselves to that greater
[2547.84 --> 2554.00]  good. Even if some of them may not survive that kind of thing there, they are, they are functioning
[2554.00 --> 2559.54]  as a single entity. And it is the entity that's trying to get the thing done, not the individual
[2559.54 --> 2565.42]  ants. The individual ant may be like, we have a crack in the ground and we have to get from this
[2565.42 --> 2570.08]  side to that side. And they build an ant bridge. You know, we've seen pictures of that. And like, you
[2570.08 --> 2576.76]  know, that one job, one little ant may have the job of, I'm holding onto the ant on this side and the
[2576.76 --> 2581.24]  ant below me is holding on there. And then they have that going on as well. And they, we're all
[2581.24 --> 2589.02]  creating this ant bridge over a chasm that none of us individually could span. But by working
[2589.02 --> 2596.32]  together for that swarm approach, which is make that accessible, they are doing something well
[2596.32 --> 2601.62]  beyond what any of the individuals can do. It's, they are super ants in that way. Yeah. And that's
[2601.62 --> 2608.48]  what I'm getting at is that, that ability to, to give up your individual identity as a member of a swarm
[2608.48 --> 2616.56]  for the purpose of the overall swarm's intent. And that swarm itself has an intent that is a swarm
[2616.56 --> 2622.26]  level thing. Kind of to your point, Jared is, is like, you know, it's not, that's not the thing on
[2622.26 --> 2628.20]  any one brain, but when you put all those brains together or technology that represents that there
[2628.20 --> 2632.54]  is a, there's a thing that the overall thing is, is trying to do as a single entity.
[2632.54 --> 2639.86]  It's, it's powers in number. It's like, uh, I saw my kids love ants, animals, you know,
[2640.08 --> 2645.90]  all the things essentially, uh, venomous plants that kill things. Like, you know,
[2646.18 --> 2651.70]  that stuff entertains them dramatically, uh, Venus fly traps, things like that. And we watched this
[2651.70 --> 2658.90]  show. It's kind of a documentary, but it's also kind of dramatic. And John Cusack, uh, was the narrator
[2658.90 --> 2665.62]  and it's a movie called the besieged fortress from 2006. And there's an ant type that I want to
[2665.62 --> 2670.06]  mention to you. It was actually, I ruined the plot a little bit, but it was ants versus termites
[2670.06 --> 2675.80]  essentially. And it was very, very well done. If you've seen it, Chris, obviously say so. I have
[2675.80 --> 2680.58]  not, but I'm going to check it out now. It's, it's a hundred percent worth it. Uh, it is phenomenal.
[2680.72 --> 2685.24]  It's probably going to visualize for our entire, entire audience, the things you're talking about,
[2685.24 --> 2690.52]  because the particular ant, I guess you would call it the name of the ant, I suppose is how you
[2690.52 --> 2699.02]  describe it. We're driver ants. And these driver ants are, are so swarm-like, you know, they don't
[2699.02 --> 2703.80]  think little, they, they, they create rafts for themselves. The entire colony can, can float.
[2704.24 --> 2708.78]  I mean, you can put them underwater and they won't die. They will like create this bubble. They are just
[2708.78 --> 2715.46]  basically resilient to the nth degree. And if you're in their path, you're dead. Like no matter
[2715.46 --> 2720.60]  what you are, a snake, a rat, a bug. They're going to overwhelm you. Oh yeah. They, they drive in
[2720.60 --> 2725.78]  numbers. They're called driver ants and they are truly, truly incredible. And this whole entire
[2725.78 --> 2732.26]  dramatic documentary narrated by John Cusack is phenomenal. The Besiege Fortress. I would highly
[2732.26 --> 2739.14]  recommend it. 2006. Amazing. But these driver ants probably elicited a lot of the, a lot of the
[2739.14 --> 2744.04]  qualities and, and characteristics that you're mentioning, because they act like if you're in
[2744.04 --> 2748.54]  their path, it's not as if they're one, it's their many and they act together and it's wild.
[2749.34 --> 2754.64]  Yeah. I mean, it brings a whole capability, like whether you're talking to ant or whether we're
[2754.64 --> 2760.76]  humans with our technology doing this, you're, you're basically inventing a whole new category
[2760.76 --> 2768.64]  of what's possible by, by, by, by introducing this. And like, you know, um, while, because I,
[2769.08 --> 2773.84]  because the conflict of interest and I stay away from, uh, my employer Lockheed Martin and, and
[2773.84 --> 2778.42]  generally I'm delicate on defense and intelligence stuff anyway, when we're talking in public,
[2778.42 --> 2785.34]  but the notion of, uh, if you were to look, uh, on the military side for just a second at a high level,
[2785.34 --> 2790.70]  there's the notion of, of mass, you know, and if you go back and work on a million people would say,
[2790.70 --> 2797.36]  okay, let's build up mass to win against, uh, an enemy. And then, um, as things progress forward,
[2797.36 --> 2803.18]  we learned that maneuver could, could kind of out, you know, you could go around mass and you
[2803.18 --> 2808.24]  could hit it from different ways. And so maneuver as a capability started trumping what was possible
[2808.24 --> 2813.94]  with mass, but swarming becomes like a whole new thing is that you're, you're kind of getting the best
[2813.94 --> 2820.52]  of mass at individual small scale, but you're getting mass and you're getting hyper maneuverability.
[2820.72 --> 2826.28]  And so it's able to trump that, you know, so when that domain and that kind of military world,
[2826.28 --> 2833.72]  it brings about a whole new capability that it never existed before. And you're in similarly,
[2833.72 --> 2838.12]  when you move into commercial and industrial, and, you know, we talked about this, this,
[2838.12 --> 2843.60]  this super automated house a few minutes ago, you're bringing about things that just were not
[2843.60 --> 2850.50]  possible before you could have little pieces of it that were possible discreetly from a, from a source.
[2850.60 --> 2856.54]  But the notion of this integrated solution that would just kind of go attack a real world problem
[2856.54 --> 2862.86]  and, and overcome it, you know, kind of going back to your driver ants is, is a new capability that,
[2862.86 --> 2867.02]  that, that the world will enjoy going forward across all different types of domains.
[2867.32 --> 2871.96]  And so I think that's, I mean, that's the magic of swarming right there is it's not,
[2872.58 --> 2877.20]  it's different from a fleet. I think a lot of the times where people throw up a whole bunch of things
[2877.20 --> 2881.78]  like drones, so that's the thing everyone knows we'll throw up a whole bunch of drones in the air,
[2881.78 --> 2887.20]  but it's not really a swarm. It's a fleet of drones. That's what it is. And each one requires
[2887.20 --> 2892.28]  individual programming to go do this or do that. There may be some communication between them
[2892.28 --> 2897.02]  potentially, depending on what they're doing, but they're not thinking almost like a brain,
[2897.26 --> 2903.04]  like an abstract brain themselves. They're not looking and dynamically handling what's happening
[2903.04 --> 2909.60]  in the real world in real time and saying, this is changing right here, right now as a swarm,
[2909.60 --> 2914.30]  I'm going to go do that. They can't do that. They're fleets. They can respond, but it's going to take
[2914.30 --> 2919.08]  inputs. It's going to take some collaboration between them, but it's going to take a lot of guidance,
[2919.08 --> 2925.80]  you know, from afar to make that happen. And that that's the difference in mass numbers in a fleet
[2925.80 --> 2933.12]  versus what a true swarm would be, uh, is that, that, that capability and that intent and, and that
[2933.12 --> 2940.24]  emergent behavior is, is really key to identifying a swarm. And you do see that in mother nature.
[2941.24 --> 2946.54]  So let's take a recent phenomenon, which is the drone light shows, you know, where they go out and
[2946.54 --> 2951.68]  let's say they're making a dragon. This is not a swarm, but yes. Well, I was going to ask,
[2951.76 --> 2955.56]  depends on the, depends on how it's implemented, right? See how I did that. Just say I did that.
[2955.94 --> 2959.20]  Not a swarm. Well, I was going to ask, it depends on how it's implemented. Isn't it? Couldn't you
[2959.20 --> 2965.10]  swarm to accomplish a dragon? Absolutely could, but nobody has. So what, like these days, what they're
[2965.10 --> 2971.00]  doing is, you know, you may see these, these light shows, uh, that, you know, where they have thousands
[2971.00 --> 2976.60]  of drones in the air, but each one of those is following a pre-programmed path. There might be
[2976.60 --> 2981.56]  some limited communication when they're very close in case of their winds and things like that in terms
[2981.56 --> 2987.82]  of, uh, anti-collision. But, but the, but what I would say is like, if you were to do the big dragon
[2987.82 --> 2994.44]  that you talked about as a swarm, the swarm would figure out how to do it in real time. Um, it's
[2994.44 --> 3000.62]  actually using that, that, that decisioning entity that we talked about in the definition and saying,
[3000.74 --> 3007.08]  my mission is to produce a dragon over this area for people to watch. And it would go do that.
[3007.08 --> 3012.08]  Like it would go figure out where all the pieces need to be for that dragon to come about.
[3012.08 --> 3018.06]  That's true swarm behavior. Like, because you, if you think about, um, animals that are getting out
[3018.06 --> 3021.60]  and doing something, they're not producing dragons, but they're going out and doing something in a
[3021.60 --> 3028.26]  swarm. They're not, there's no external thing saying, you know, swarm of bees, uh, I'm telling
[3028.26 --> 3034.12]  you to go do this and you need to make an adjustment there and all they figure it out in real time in the
[3034.12 --> 3040.32]  swarm and make whatever it is that those species are trying to achieve. It happens. It's emergent behavior
[3040.32 --> 3045.56]  that's real and in real time that supersedes the individuals. And that's what I'm saying. The light
[3045.56 --> 3052.44]  shows fleets of drones that are being, that are being, uh, provided instructions often, you know,
[3052.66 --> 3058.16]  essentially a three dimensional, uh, vectoring trajectory on what me as an individual drone
[3058.16 --> 3065.30]  would do regardless of what all these others are doing. Okay. So even inside of emergent behavior,
[3065.30 --> 3071.76]  let's say in an ant colony, you have roles, you have leadership. There's some sort of like,
[3072.32 --> 3078.60]  there's some sort of mission that comes from somewhere. There is. And I assume now we're
[3078.60 --> 3081.96]  getting, we're getting to the part where it's like, okay, how do you make these things? Because
[3081.96 --> 3086.40]  as a guy who's makes fancy websites his entire life for a living, like this sounds really hard.
[3086.48 --> 3091.74]  I just feel like if I had a new day, Jared, your new job is like build a swarming technology of
[3091.74 --> 3096.80]  autonomous, whatever is, I'd be like, no, not going to even try that. Cause, uh, that just
[3096.80 --> 3103.62]  sounds very, very, very difficult. Where do you start? Like, how do you, how do you, how do you do
[3103.62 --> 3108.68]  it? That's a great question. And not only that, but you've identified the thing that you just said,
[3108.68 --> 3114.66]  uh, in your, in your vulnerable moment there, uh, in terms of like, I don't even know where to go.
[3114.66 --> 3120.52]  So that's what almost everybody, that is why it is a problem yet to be solved. And there are many,
[3120.62 --> 3127.02]  there are many groups, companies, individuals out there working on it, uh, including me. And, um,
[3127.08 --> 3133.38]  and, and, you know, that this is my passion and, um, all of us at some point start, some of us might
[3133.38 --> 3137.78]  have had the benefit of coming from robotics, but just like many other skills that also carries some
[3137.78 --> 3143.12]  baggage with it that you have to unlearn, uh, to do it. Um, and that's, that's one of the pros.
[3143.12 --> 3147.06]  So when I talk to people, like I've been doing drones for 20 years, I know everything. And I'm
[3147.06 --> 3153.52]  like, well, I'm like, that's good in some ways, but, um, not a swarm. Yeah. Not a swarm. And not
[3153.52 --> 3158.28]  only that, but sometimes it's the, it's the t-shirt says not a swarm, that's not a swarm. Yeah. Ask me
[3158.28 --> 3165.40]  anything, not a swarm. That fresh, that fresh learner's mind though, often does it. And so it's a
[3165.40 --> 3170.80]  complex problem and you have to break it down into its constituent parts. And there's a whole bunch of
[3170.80 --> 3175.32]  layers because there's like, there's things that have to happen at the member. Like if you talk
[3175.32 --> 3180.38]  about the individual ant, you know, at the member level, there's a whole bunch of things it's got to
[3180.38 --> 3185.84]  navigate. And that's kind of like where we are on like drones today, you know, in the sense of like,
[3185.90 --> 3189.32]  if you go buy one, you know, we're going to go out, you go out to the toy store and you buy a drone
[3189.32 --> 3194.98]  today, um, or order one online these days because toy stores are not, not so common anymore. So we ordered
[3194.98 --> 3201.00]  the drone online and like that has basic navigation and there's a whole bunch of tasks associated with
[3201.00 --> 3207.50]  that. And that's where most of the robotics world has been obviously over the years. But as you move
[3207.50 --> 3212.40]  into communication between them and what kind of tasks happen, you kind of move up to a lever.
[3212.50 --> 3218.94]  There's a local, there's a local drone level in a larger swarm. And then there is the, how do all
[3218.94 --> 3225.72]  those locals, uh, operate together. So you're, you kind of steadily move up in abstraction till you
[3225.72 --> 3233.06]  have that, that notion of, uh, this emergent thing, which is really, it's really quite a challenge
[3233.06 --> 3241.58]  of like, cause there's not a master member. There's not the boss. Um, some, some, you may have a queen.
[3241.58 --> 3243.20]  Wouldn't it be easier if there was a boss though?
[3243.56 --> 3248.22]  It would. So it depends on what you're trying to do. I would say that's like the step below. If you're
[3248.22 --> 3253.26]  doing almost everything a swarm can do, but you still have some centralized control. Um, there's
[3253.26 --> 3259.34]  a couple of levels below that. And I, and while I can't, I can't share it today. I'm going to try.
[3259.50 --> 3267.24]  I invented, I created a document that allows that, that helps people at my company evaluate these
[3267.24 --> 3272.62]  technologies at different levels. Um, it's called a maturity, a maturity model towards swarming.
[3272.78 --> 3278.16]  And, and they can look at anyone else. Somebody has put something out there and we can evaluate
[3278.16 --> 3282.54]  it based on that criteria about what exactly it does. Um, and I need to see if they'll let me
[3282.54 --> 3284.56]  release it publicly. Cause I think it would be useful.
[3284.56 --> 3289.84]  Let me see if I can maybe break down an idea and I don't have your depth, but if I were thinking
[3289.84 --> 3295.82]  about this problem and, and obviously when we compare ants, so in the case of the driver ants,
[3295.82 --> 3301.10]  just cause that's my example that I have some clarity on, at least they do have a queen and the
[3301.10 --> 3307.62]  job is to protect the queen. It's like if the queen disappears, they will elect or attempt to elect a new
[3307.62 --> 3314.22]  queen, but there's always somebody in charge essentially. But if that's not, if that's not a swarm,
[3314.64 --> 3323.18]  then the way I might try to, uh, create a boss would be through consensus. Because if you're a
[3323.18 --> 3328.58]  controlling entity that's connected, and so, you know, all your parties in this connected mesh
[3328.58 --> 3334.98]  network or whatever you want to call this, this one, then, you know, player B versus Z over here
[3334.98 --> 3341.70]  has new information. The swarm needs to know to consensus Lee, that's even a word to have consensus
[3341.70 --> 3349.30]  on the next decision. And so we may as a swarm elect a new, not so much boss, but a primary
[3349.30 --> 3354.60]  information source that changes the way the swarm acts as an entity. And so it's sort of self
[3354.60 --> 3355.16]  evolutionary.
[3355.82 --> 3358.26]  You're hired cause you're on the right track. That's it.
[3358.26 --> 3360.58]  So aren't they just making their own boss then basically?
[3361.06 --> 3367.38]  So, so that's the thing. Like, so the queen, like in the case of the queen, the, yes, there's a
[3367.38 --> 3373.64]  queen who is the, you know, the, the general, the, the one in charge, but at the same time, she's
[3373.64 --> 3378.82]  actually not making all the decisions. You know, a lot of it is instinct, you know, that is, that is
[3378.82 --> 3379.58]  being played out.
[3379.66 --> 3384.22]  It's preservation at that case, right? The queen is not the boss in terms of leadership and knowledge
[3384.22 --> 3387.78]  because the drones have the knowledge, right? The drone ants out there doing the work.
[3388.10 --> 3388.34]  That's right.
[3388.36 --> 3393.76]  She is the, the preservation system for the entity. It's a necessary component of many.
[3393.92 --> 3400.24]  So she's not a master, like a master direction giver, you know, that's not her, her role is,
[3400.32 --> 3407.24]  is as you said, perpetuation of the colony versus she's not driving the specific actions of the,
[3407.34 --> 3412.72]  of the drones. Those are built in, you know, mother nature has imbued the members with that and
[3412.72 --> 3419.00]  they understand how to do that. But, but to your point, Adam, that notion of kind of consensus,
[3420.00 --> 3423.40]  you know, there are different approaches to it. We can use some different words because there are
[3423.40 --> 3429.46]  different algorithmic approaches of consensus, election, things like that in terms of saying,
[3429.64 --> 3437.56]  well, we have, we have a distributed compute grid that is our swarm that, you know, that is imbued in
[3437.56 --> 3446.80]  our swarm. And, and how do we arrive at a single overarching directives that perpetuate themselves
[3446.80 --> 3452.30]  downward through the swarm and which change as they go down? Cause this is the overall, this is our,
[3452.66 --> 3458.66]  what we need to do. There's a mission. There is a high level sense of abstraction about, well,
[3458.66 --> 3464.10]  to accomplish the mission, you must do A, B and C, but A has 10 steps to it, you know?
[3464.10 --> 3470.22]  And some of the swarm members are going to be, are going to take the assignment of doing those and
[3470.22 --> 3474.74]  others are going to say, well, I'm going to go off and do these other things that are, that are part
[3474.74 --> 3480.42]  of that, that might've been part of the B category. And so they have to self-organize in the way to do
[3480.42 --> 3486.44]  that in real time, because this is a physical technology. So it's, it's one of those, and there
[3486.44 --> 3491.64]  are sensors coming in, things are changing, you know, constantly without, without, and so you're,
[3491.64 --> 3496.98]  you're, you're a knowledge, you are with your sensors, whether you're a biological being
[3496.98 --> 3501.88]  or whether you're technology, you're having to take all that new information in, you're having
[3501.88 --> 3508.24]  to do distributed computing and decisioning through algorithm, algorithmic approaches and,
[3508.24 --> 3516.10]  and, and select members to accomplish all the things as part of that overall mission that you're
[3516.10 --> 3521.18]  doing. And it's quite complicated. I mean, it's a very complicated thing as we sit here in 2025.
[3521.64 --> 3526.18]  I think we'll nail it gradually. I think we'll nail it in iterations. And I think it won't,
[3526.56 --> 3531.46]  I think somebody a century from now will be like, yeah, well, of course we did that, you know, but
[3531.46 --> 3533.80]  today it's, it's a tough problem to solve.
[3534.40 --> 3538.34]  So at what level do the humans interact? So let's imagine that you've created a
[3538.34 --> 3545.08]  swarm of vehicles and it's, it's, it's a legit swarm. It's not a, not a swarm swarm.
[3545.46 --> 3546.58]  A legit swarm.
[3546.58 --> 3550.50]  Yeah. I was thinking about that. As you said that, you remember the old Jeff Fox where you're
[3550.50 --> 3554.22]  saying you like, you might be a redneck. We could do a four line of like, you might not be a swarm.
[3554.30 --> 3557.98]  Like if you've got a boss, you might not be a swarm. You know, if you've got a path that gave
[3557.98 --> 3562.96]  you to fly, you might not be a swarm, but let's say you have one and this is like, you know, Chris
[3562.96 --> 3570.26]  approves and it's a bunch of drones. Let's just do that. At what level does the drones receive their
[3570.26 --> 3574.94]  mission from the humans? Like, is it very generic or is it very specific?
[3574.94 --> 3579.28]  It can be either. It depends on what you're, what you're building toward and swarms have
[3579.28 --> 3583.96]  different purposes. So remember a swarm is not a generic thing. They're a purpose built,
[3584.04 --> 3590.76]  you know, for certain capabilities. And so you, and you do have that C3, which is command control
[3590.76 --> 3597.36]  and communications that's inherent to that. And one of the other phrases I use, which people
[3597.36 --> 3600.74]  outside of the military context may not be as familiar with is human on the loop.
[3601.12 --> 3602.26]  Not in the loop, but on the loop.
[3602.26 --> 3607.18]  Not in the loop, but on the loop, those are two different things. So an in the loop is where
[3607.18 --> 3613.68]  you're a human is controlling a technology directly or, and, and they are, they're making
[3613.68 --> 3621.66]  it. So like a human in the loop may say, make a choice for a task. So they may say, yes, I'm
[3621.66 --> 3627.32]  going to now have you drop that package on that person's front door. And, you know, yeah, it's
[3627.32 --> 3631.96]  clear. We've looked at it. It's safe. There's nobody in the way, and we're going to have
[3631.96 --> 3636.40]  you put the package on the front door because it's safe. And we did not want the drone to
[3636.40 --> 3641.92]  do that until me as a human verified that that was okay for us to do so that we didn't hit
[3641.92 --> 3642.92]  people or hit things.
[3643.30 --> 3651.26]  On the loop, you are essentially tasking that it's, it's kind of a, the human has a supervisory
[3651.26 --> 3656.86]  role and maybe a mission giving role. Like your mission swarm is to deliver the package
[3656.86 --> 3663.76]  to that, or maybe more, more, it might be, here's a bunch of packages and to the swarm.
[3664.20 --> 3668.48]  And I want you to go to this neighborhood and deliver all these packages to the right houses.
[3668.48 --> 3674.88]  And that is the mission. And then the swarm understands that geographic layout. It understands
[3674.88 --> 3679.84]  the real world environment it's in. And it figures out which member they each pick up
[3679.84 --> 3683.60]  a package and it figures out how are they going to do that. Some of the packages are more than
[3683.60 --> 3689.68]  the eight pounds that Adam talked about. Some of them are 60 pounds and it takes multiple swarm
[3689.68 --> 3694.44]  members to get that package airborne and to collaborate. And so as they go, as they go into
[3694.44 --> 3698.70]  that environment and they're looking, I got to get this package to that address. And oh, by the way,
[3698.70 --> 3705.32]  that address might've been reachable by a four pound package on one swarm member acting alone,
[3705.32 --> 3710.28]  but we, it's now 60 pounds. We have multiple swarm members. And even with all those swarm members,
[3710.28 --> 3715.64]  it's outside of our range. So how do we address getting it outside the range, given the fact that
[3715.64 --> 3722.02]  we have other concerns that may be limiting that the swarm would work that out through its distributed
[3722.02 --> 3727.92]  computing and collaboration that we just talked about that, you know, where, where it kind of comes
[3727.92 --> 3732.52]  to that consensus on how it's going to collectively solve the problem. Does that make sense?
[3733.04 --> 3739.24]  Yes. I think that it does. I'm wondering if maybe I'm sniffing danger eventually because.
[3740.02 --> 3741.02]  Oh, go for it.
[3741.30 --> 3747.76]  Well, because at a certain point you give a directive and maybe that directive is completely benign.
[3747.76 --> 3752.78]  Like you, you have a swarm of cleaning bots, you know, in your house and you say, okay, bots,
[3752.94 --> 3757.42]  you know, clean the bathroom. And that's as far as you get into it, you're on the loop,
[3757.42 --> 3763.90]  but you're not in the loop. And so they go about doing that. And we've accomplished Chris Benson level
[3763.90 --> 3770.48]  swarming. So I now have a, I have now have numerous independent, fully autonomous,
[3771.48 --> 3778.88]  multi-agentic platforms in my bathroom, exhibiting highly coordinated locomotive and emergent behaviors
[3778.88 --> 3784.06]  with agency and self-governance. Right. So at a certain point, couldn't they just say,
[3784.16 --> 3790.00]  man, this toilet's really dirty. What if we just removed it? Wouldn't that be the bathroom
[3790.00 --> 3794.26]  would be even cleaner. And then they all decide that, yes, that's a great idea. I come back,
[3794.32 --> 3794.82]  I don't have a toilet.
[3794.82 --> 3800.40]  That, that is just, Adam had a great moment a moment ago and you just had a great moment.
[3801.30 --> 3803.96]  That was most of my great moments in those toilets.
[3807.44 --> 3813.34]  Cleaning up your act, man. But yeah, so like that, that's a great thing. And that comes down to,
[3813.34 --> 3820.76]  you're not giving what you're really telling about in swarms is when you get down to the task level,
[3820.76 --> 3826.00]  then you're talking maybe not about the whole swarm making a decision. It might be a few of them
[3826.00 --> 3832.32]  that are, that are addressing a task and figuring out at a more logistical level, like how am I going
[3832.32 --> 3837.92]  to, you know, operational level, how am I going to do this? And, and, and that is one of the things
[3837.92 --> 3842.62]  is that when you're doing, you know, we're back to AI safety and AI training on this is that you're,
[3842.62 --> 3850.14]  is that maybe removing the toilet in most cases is not an acceptable thing. So, so we need,
[3850.14 --> 3855.88]  we need some technology based guardrails there, but that's also where depending on the circumstance
[3855.88 --> 3860.60]  that you're looking at, that human on the loop needs to be able to go. No, yeah. There's kind
[3860.60 --> 3866.06]  of a kill button, if you will, you know, figuratively speaking, um, and meaning killing of the swarm,
[3866.06 --> 3870.38]  not killing a person just to be very clear so that nobody misunderstands me. Super clear,
[3870.52 --> 3874.66]  no killing here. No, we're not talking about killing people here. That's why I use a bathroom
[3874.66 --> 3879.90]  and a toilet as my example. In this context, it might be, don't kill the toilet. Um, you know,
[3879.90 --> 3885.56]  kind of thing. And that's where the human on the loop as, as an oversight where we still have these
[3885.56 --> 3893.34]  amazing capable human brains that have, they can't do everything that digital technology can do, but,
[3893.46 --> 3898.10]  you know, digital still hasn't yet arrived. It will, but it hasn't yet arrived at what our
[3898.10 --> 3903.32]  capabilities are. And we can look at it and go, taking the toilet out is not acceptable to the
[3903.32 --> 3907.72]  homeowner. We're not doing that. Maybe if you're Jeff Bezos, maybe instead of cleaning the toilet,
[3907.72 --> 3914.00]  you just remove it every time. Maybe Jeff Bezos will have the toilet removal every day.
[3914.60 --> 3919.98]  The drone swarm goes into Jeff Bezos bathroom and it just takes the toilet out and it puts the new
[3919.98 --> 3924.04]  one in. The back is just a sea of toilets back there. It's like a pile of them.
[3924.16 --> 3928.10]  There you go. Well, it cleans it all up because you know what, when you can throw,
[3928.30 --> 3933.26]  when you can throw $8 billion at something you haven't really identified yet, you can probably
[3933.26 --> 3940.14]  afford to have your toilet. 6.2. Oh, 6.2. That made such a big difference in my mind.
[3940.32 --> 3943.38]  Yeah. Sorry about that. 8 billion is close. Let's just round up to 8 billion.
[3943.38 --> 3947.90]  Let's just round down to 6. Okay. We're there. But yes. So other than Jeff,
[3947.96 --> 3951.98]  I don't want the drone swarm taking my toilet away. That would get rather...
[3951.98 --> 3952.54]  I'm with you.
[3952.54 --> 3954.24]  Yeah. It's a, it's a little bit too much.
[3954.24 --> 3975.40]  Well, friends, when you're building and shipping AI products at scale, there's one
[3975.40 --> 3981.58]  constant complexity. Yes. You're wrangling models, data pipelines, deployment infrastructure.
[3981.58 --> 3988.06]  And then someone says, let's turn this into a business. Cue the chaos. That's where Shopify
[3988.06 --> 3994.02]  steps in. Whether you're spinning up a storefront for your AI powered app or launching a brand around
[3994.02 --> 3999.32]  the tools you've built. Shopify is the commerce platform trusted by millions of businesses and 10%
[3999.32 --> 4007.38]  of all US e-commerce from names like Mattel, Gymshark to founders just like you. With literally hundreds
[4007.38 --> 4012.50]  of ready to use templates, powerful built in marketing tools and AI that writes product
[4012.50 --> 4017.80]  descriptions for you, headlines, even polishes your product photography. Shopify doesn't just
[4017.80 --> 4022.88]  get you selling. It makes you look good doing it. And we love it. We use it here at ChangeLog.
[4023.02 --> 4029.34]  Check us out. Merch.ChangeLog.com. That's our storefront. And it handles the heavy lifting too.
[4029.34 --> 4036.90]  Payments, inventory, returns, shipping, even global logistics. It's like having an ops team built into
[4036.90 --> 4042.84]  your stack to help you sell. So if you're ready to sell, you are ready for Shopify. Sign up now for
[4042.84 --> 4050.78]  your $1 per month trial and start selling today at Shopify.com slash practical AI. Again, that is
[4050.78 --> 4054.54]  Shopify.com slash practical AI.
[4059.48 --> 4066.26]  Can we get into this scenario where it's like Aladdin and the genie and he's like, Hey, you know,
[4066.28 --> 4071.86]  I want, make me a prince. Right. I think it was the first, no, the first one was to, he tricked the
[4071.86 --> 4076.02]  genie to get him out of the cave. We'll, we'll skip that one. And then the second one, technically
[4076.02 --> 4081.30]  the second wish was make me a prince. And he didn't really make him a prince.
[4081.54 --> 4085.50]  That's a great memory. Gosh, I'm like, I've seen the movie, but like, you're really bringing it back
[4085.50 --> 4091.22]  to me. Well, I got a good brain, you know, over here. My brain is solid. That's a second great
[4091.22 --> 4095.60]  moment, right? That's right. Two in one show. I've seen your moments here with me. So, okay. Keep going.
[4096.02 --> 4101.24]  He doesn't really make him a prince. He just clothes him as a prince. He mimics a prince. He doesn't
[4101.24 --> 4105.84]  really give him royalty. He doesn't really give him lineage. And I guess I'm sort of sidetracking
[4105.84 --> 4109.74]  to some degree just to be accurate about my Aladdin reference. But point is, is there's times
[4109.74 --> 4115.52]  when he adds it, or I guess in all of the lore around the Aladdin figure and a genie figure,
[4115.56 --> 4119.32]  where you ask the genie for something, but you have to be careful. That's where this term comes
[4119.32 --> 4124.90]  from. Be careful what you wish for, because you wish for something without the full awareness of
[4124.90 --> 4131.72]  the agency behind the genie, behind the swarm. And so you might get your toilet removed. Is that a
[4131.72 --> 4135.88]  concern? Like how, totally, how are you guarding against that? How do you guard against that without
[4135.88 --> 4141.94]  the human on loop or the kill switch? Is there an OS? Like, I don't know. How do you, how do you guard
[4141.94 --> 4146.16]  against this genie issue? I know. I think there's a lot, and I think it's at many different levels.
[4146.36 --> 4153.30]  And it's a, it's a real thing that we talk about in real life today without having achieved full Chris
[4153.30 --> 4158.68]  Benson level drone swarming. And that, you know, we talk about that in terms of AI safety all the time.
[4158.68 --> 4164.50]  Now, you know, that's a huge part of the AI world is what is AI safety? How do you keep unintended
[4164.50 --> 4170.60]  consequences from coming to pass? I think anyone who's reasonable recognize that some of those will
[4170.60 --> 4177.58]  still come to pass out there. You can put guardrails around things, but, and you can even ask AI to put
[4177.58 --> 4181.68]  guardrails around other AIs as we're doing, you know, because we're using the tool to build the tool,
[4181.82 --> 4188.52]  but we will have that outcomes across the board just as we always have with software and always will.
[4188.68 --> 4197.72]  Um, and so I, I don't have the magic bullet, uh, on that, but, um, there, there is, there is, uh,
[4197.72 --> 4204.90]  training the distributed swarm brain, you know, this abstraction of computing of grid computing,
[4204.90 --> 4208.34]  where they're all doing this and using their algorithms you'll, and that will,
[4208.86 --> 4213.46]  where it goes wrong may happen different places. You know, we often talk about today's LLMs
[4213.46 --> 4219.52]  coming out with, with inferences that are, that are suboptimal, uh, sometimes, uh, quite funny,
[4219.62 --> 4225.96]  sometimes quite tragic actually. Um, but that will continue to happen. We have, uh, we have software
[4225.96 --> 4231.58]  issues. We're also moving into the physical world where, you know, you know, if you have, uh, these
[4231.58 --> 4237.06]  physical agents that are imbued with a whole bunch of AI agents that are doing stuff and they're acting
[4237.06 --> 4243.12]  as a member of a larger swarm, there's a lot of places where things can go wrong. So it's going
[4243.12 --> 4247.02]  to be, it's, there's going to be a learning curve on that. And we're going to have, we're going to
[4247.02 --> 4252.26]  have problems along the way. So I don't want to, I certainly wouldn't want, um, I know for a lot of
[4252.26 --> 4257.30]  listeners and viewers, they probably think of a little, you know, a little bit pie in the sky.
[4257.44 --> 4262.30]  Not everyone's going to believe that this is probably sooner than they would otherwise expect,
[4262.30 --> 4267.08]  but, um, we'll get through it and stuff and we'll, we'll try it. We'll do the best we can.
[4267.08 --> 4272.22]  And the responsible people will put a lot of safety, uh, around it in, in the best they can,
[4272.30 --> 4278.24]  but we'll, we'll make mistakes. Where do we stand? Where are we in this initiative to create
[4278.24 --> 4285.50]  this thing or these things? So I think like many things, you'll see it coming from specialists.
[4285.78 --> 4291.10]  Uh, you know, it, there's, there's a whole area of expertise, you know, that, that you develop around
[4291.10 --> 4296.88]  trying to solve these problems and some companies are specializing that. And just like other things,
[4296.88 --> 4301.38]  you'll see that. But I think over time, especially given the fact that it's not one industry,
[4301.38 --> 4306.24]  it's many industries, there'll be many players. I think one of the things to make this happen
[4306.24 --> 4310.58]  isn't just, can we get there? Cause if you think about it, once you can get there,
[4310.90 --> 4316.04]  almost everybody kind of does a close, close copies of that, you know, once we had our first,
[4316.04 --> 4321.48]  you know, chat GPT, it wasn't long before that we had competitors and other models that were,
[4321.82 --> 4325.64]  that were nipping at its heels. And I think you'll see that here as well, but it'll,
[4325.88 --> 4332.74]  I think it really comes down to getting organizations and, and motivated individuals into it so that they
[4332.74 --> 4338.24]  are producing some level of whatever's productive in what they're doing in their industry and their,
[4338.40 --> 4343.30]  in their world, what's productive and costs will drive down. And I think as those costs drive down,
[4343.30 --> 4348.38]  that's where you see it really pushing out into lots of different places in life.
[4348.50 --> 4353.34]  So a lot of it is, isn't just a technology question. It's an economics question.
[4354.18 --> 4356.80]  But I think the pervasiveness of it will drive that.
[4357.30 --> 4361.96]  Let's get, since we, you know, helped create a show called Practical AI, let's get practical.
[4362.58 --> 4362.84]  Yes.
[4362.88 --> 4367.42]  You'd mentioned this is obviously burgeoning. You're coining this. I kind of feel like swarming is the
[4367.42 --> 4371.52]  protocol. Maybe there's a specification there somewhere and the implementation is more of a product
[4371.52 --> 4375.96]  potentially, but take us into the practical nature of let's just say of the next three years.
[4376.04 --> 4384.98]  Well, we see swarming of any sorts in a consumer level home lab, put it my home level. And if we do
[4384.98 --> 4389.66]  like be realistic, practical, if you can, like, what will it be?
[4389.66 --> 4395.92]  At the level of the definition that I provided, which is a very high bar, I think you'll see lots
[4395.92 --> 4400.68]  of things that are calling themselves swarming things developing within that two to three year
[4400.68 --> 4409.12]  horizon. I don't think many of them will rise to that level. There'll be kind of quasi swarming
[4409.12 --> 4413.84]  capabilities that you're starting to see in consumer and commercial products and stuff.
[4413.84 --> 4420.86]  I do think, however, there are so many really smart minds around the world working on swarming
[4420.86 --> 4429.80]  because by opening up an entire new category of capabilities that don't exist today, that
[4429.80 --> 4434.90]  people already have productive use cases in mind for, there's a lot of money to be made
[4434.90 --> 4441.54]  there. So you have not only commercial entities and motivated makers, but you have nation states
[4441.54 --> 4447.34]  that are highly motivated to do that. And it's a big scientific topic of research.
[4447.66 --> 4452.18]  I think you'll see it probably first in areas where people can throw lots of money at it.
[4452.32 --> 4457.28]  And so, you know, if we do talk about in the commercial space, our 800 pound gorillas,
[4457.54 --> 4464.76]  you're more likely to see it in a narrower case of use cases there. I think in the military space,
[4465.28 --> 4469.98]  an intelligence space, you're likely to see it there because you have the, you know,
[4469.98 --> 4474.88]  the economies of nation states that are, that don't want to be left behind. You know, it's,
[4474.96 --> 4480.52]  it's, if we don't, if we're not able to produce a swarm first or are very closely following whoever
[4480.52 --> 4487.20]  is first, then we have a national security issue here in terms of what's possible. And so I think
[4487.20 --> 4493.44]  you'll see nation states prioritizing that probably in very close collaboration with commercial entities,
[4493.44 --> 4498.50]  which is really common today. I mean, if you look at certainly how both the U S government
[4498.50 --> 4505.42]  and most of our allies as well as, you know, the Chinese government, you know, there's a lot of,
[4505.42 --> 4511.26]  of overlap between nation state resources and commercial entities that have special
[4511.26 --> 4515.78]  knowledge and skills working together to produce that stuff. So I think that's,
[4516.26 --> 4521.30]  I think those types of collaborations are likely to be the first ones largely because they can throw
[4521.30 --> 4526.04]  resources at the problem until you get there. I think the key is, is thinking about the problem
[4526.04 --> 4530.66]  the right way. And I think that's where people struggle is breaking down that complexity that we
[4530.66 --> 4536.46]  were talking about earlier, you know, that Jared pointed out and saying, how can we discreetly address
[4536.46 --> 4542.90]  those points of complexity in a way that you can then pull those, those, those many solutions
[4542.90 --> 4548.32]  together to achieve the grandiosity of the definition that I provided.
[4548.32 --> 4553.12]  Let me see if I can not predict, but this is where I would.
[4553.32 --> 4556.38]  Cause I'm not going to predict anything. Yeah. Yeah. We both, we know that.
[4557.38 --> 4562.08]  I think the two of you, I think we'll agree with what I'm going to say here. I think the area where
[4562.08 --> 4569.58]  I'd like to see this type of swarming is in energy conservation. And so I think there's multiple
[4569.58 --> 4576.58]  devices in my house that consumes energy from a HVAC system above me that both heats and cools my home
[4576.58 --> 4584.92]  to the lights that power my house to let's say a kettle that is electrified, all the things I want
[4584.92 --> 4591.90]  to give my home, the task of being energy conservative, right? This, this swarm, I want to have a swarm of
[4591.90 --> 4599.48]  devices that help me be that. And it can, it, Hey, Adam and the family are not here. It makes sense as an
[4599.48 --> 4603.68]  agency to be, to be conservative with our energy use because there's no one here to do it.
[4604.56 --> 4610.82]  And that's where the, you can do like individual device level smart home automation, which is
[4610.82 --> 4615.26]  here today. Yeah. But it's not matter. Matter supports that. It's not a swarm though. Right.
[4615.26 --> 4621.84]  It's not a swarm. That's right. So I would like energy conservation to be my first swarm tactic.
[4621.84 --> 4627.44]  The next would be, I live in Dripping Springs, Texas, uh, just outside of Austin, Texas. And we
[4627.44 --> 4632.40]  always have water challenges right now. We're always in some version of a drought. There's actually
[4632.40 --> 4638.16]  a big bet on the wall on wall street against Texas running out of water. Like there's a bet
[4638.16 --> 4643.86]  essentially shorting Texas running out of water at some point. I just heard this headline. That's a
[4643.86 --> 4646.98]  headline only. I don't even know what the truth is behind that, but I heard it. So it must be true.
[4646.98 --> 4653.54]  Okay. So the next thing is water conservation helped me as a household, maybe even helped me
[4653.54 --> 4658.56]  as a neighborhood, a swarm neighborhood, be conservative when it comes to water conservation.
[4659.04 --> 4664.90]  So my child goes to, uh, flush the toilet or yeah, I don't know, some sort of action tries to take
[4664.90 --> 4669.02]  place, but the swarm is like, hang on a second. We're in a conservative nature. We're going to use
[4669.02 --> 4675.72]  the one or the 0.5 gallon version flush versus the 1.2. Cause it's a, you know, it's number two,
[4675.72 --> 4681.16]  you know, some reason, right. But for whatever reason, like we now have new tech in my house.
[4681.16 --> 4685.92]  So that gives me things that really matter, energy, water. And I think the last one for me
[4685.92 --> 4692.80]  is food. There is so much food waste in America, tremendous amount. I know I for sure buy some
[4692.80 --> 4696.92]  chicken once, twice a month, and I'm killing chickens constantly because I'm wasting my chicken,
[4697.02 --> 4700.98]  not making it. So I don't know if that's a problem. That's me, but at some point, my tech,
[4700.98 --> 4706.40]  my swarm tech can help me solve those three key things, energy, water, and food.
[4706.72 --> 4710.48]  And I think you start there because that's what matters. My laundry kind of a me problem.
[4710.88 --> 4716.06]  Maybe my washer can say, Hey, you put a white in with a darks, probably not smart, eject it or
[4716.06 --> 4721.14]  alert me. You know what I'm saying? But like, I don't need help with laundry. I don't need,
[4721.24 --> 4725.38]  I mean, I like my iRobot and vacuuming. That's cool. But I think that the thing I would want to
[4725.38 --> 4728.02]  conserve on is those three things. That'd be helpful.
[4728.02 --> 4732.08]  I think you'll see that. I don't think it'll just be the swarm doing that though,
[4732.12 --> 4737.20]  because like even today, you know, if you start with where we're at right now and talk about the
[4737.20 --> 4742.34]  fact that energy monitoring is really common within a lot of these existing devices.
[4742.34 --> 4743.48]  Not a swarm though. Not a swarm.
[4743.50 --> 4745.58]  Not swarm yet, but we're getting there.
[4745.82 --> 4746.30]  We're getting there.
[4746.32 --> 4746.82]  Keep saying it, sorry.
[4746.96 --> 4752.84]  So bear with me for a second. So we have what we can already do at the individual device level.
[4752.84 --> 4759.86]  And then as we really started viewing our homes with AI agents, which is going to happen even
[4759.86 --> 4761.22]  before the swarms are hitting.
[4761.48 --> 4762.60]  So soon. Yeah, that's next.
[4762.74 --> 4766.82]  You're going to have AI agents doing lots of different things, including the monitoring and
[4766.82 --> 4772.64]  and they will be in those AI agents will be monitoring your matter driven devices and thinking,
[4772.86 --> 4776.32]  Oh, we need to make some adjustments. They'll be communicating with the devices that
[4776.32 --> 4781.58]  that are being governed by that. And so they're able to get you a great deal of the way down that
[4781.58 --> 4787.12]  use case that you just talked about. But there are also going to be things in your home that,
[4787.12 --> 4792.04]  you know, where things like for energy, the energy conservation thing, you mentioned things like,
[4792.04 --> 4799.48]  you know, airflow and temperature where it's not an explicit device that's matter enabled and has
[4799.48 --> 4804.86]  the, you know, energy monitoring built in, but it may be like that corner of the room is cold.
[4805.30 --> 4810.28]  And in that case, that swarm that's monitoring the house and maybe has other functions that aren't
[4810.28 --> 4814.60]  just monitoring. Maybe it's doing a cleanup, you know, it's doing the cleaning job, but it also
[4814.60 --> 4819.70]  notes that, Hey, this corner is not getting good airflow. It's the temperature is changing
[4819.70 --> 4827.50]  to your vision, Adam, that you just talked about. That's where the swarming capabilities of having
[4827.50 --> 4832.88]  different devices work together. We'll do it. Now, an individual robot could also detect that device.
[4832.98 --> 4836.86]  It doesn't have to be a swarm. So you're really good at it for a swarm to be effective there.
[4836.86 --> 4843.98]  You're really going to be looking for how does a cluster of members working dynamically together,
[4843.98 --> 4847.66]  get me something I don't already have. And I think that's the question to answer
[4847.66 --> 4851.48]  in that use case, if you're actually wanting to introduce the swarm to it.
[4852.84 --> 4857.50]  Well, we humans have our own form of swarming. It's called open source software. And I'm curious
[4857.50 --> 4864.28]  if there's a place where people who are as passionate or maybe even just potentially interested in this
[4864.28 --> 4868.20]  initiative, this movement, this, I don't know, this next big thing of swarming tech,
[4868.72 --> 4873.64]  is there a place they can gather? Is there like a, is there a framework? Is there a conversation?
[4873.84 --> 4877.34]  Is there anything in the world of open that people could gather around?
[4878.10 --> 4883.34]  There are. And I probably should have brought a list maybe in the show notes. We can add some stuff in.
[4884.40 --> 4889.76]  Some of the things that I often tell people to start off on is, you know, robotics has been a big
[4889.76 --> 4897.38]  part of this kind of robotics role, you know, being a part of developing to the swarm is ROS2 exists.
[4897.58 --> 4903.84]  ROS stands for ROS2. ROS is the robotic operating system, which is open source.
[4904.58 --> 4910.78]  And it is the most widely used robotic software technology out there. It's not the only one.
[4910.92 --> 4916.16]  There are many, and some of them are closed and some of them are open, but there's tons of books now on ROS.
[4916.16 --> 4921.48]  And so I often, when people are interested in this and they're like, but how do you do, like,
[4921.72 --> 4926.20]  aside from the swarm, I can't even make a single robot or like, what do I do? Well, there's tons
[4926.20 --> 4932.74]  of information about that. Start off, maybe not solving the overall swarming problem that we,
[4932.86 --> 4937.68]  that we were describing as being, as remaining a hard challenge, but start with something more
[4937.68 --> 4943.92]  accessible. You can buy, you can get on to, you know, you know, we, we mentioned Bezos so much,
[4943.92 --> 4950.04]  Amazon and, and others. And, and there are a lot of maker kits that you can get that are open maker
[4950.04 --> 4956.92]  kits. You have ROS, they're very similar in terms of, but if you want to not do robots and you will do
[4956.92 --> 4962.12]  drones, there's a whole bunch of open source drone stuff. And then the thing that I love doing, I do this
[4962.12 --> 4968.78]  all the time, is diving in on GitHub at different software communities that support, you know, open
[4968.78 --> 4974.80]  specs and stuff. There's tons of repositories on GitHub that are designed to do this, that just
[4974.80 --> 4979.06]  interested people said, I want to go scratch and itch. I want to solve a problem. And I go there
[4979.06 --> 4985.14]  and I'll then also go to hugging face and look for small models that may, if I need AI in the mix that
[4985.14 --> 4990.66]  can contribute because really, you know, small models are where the future is. You know, it's not,
[4990.78 --> 4994.28]  we talked at the very beginning of the conversation about the giant versus the small,
[4994.28 --> 5001.78]  go for small stuff. You have, you, there's very likely that you have a GPU and at home, it may be
[5001.78 --> 5007.10]  in your laptop or something that you can buy for a couple of hundred bucks that, that can do all sorts
[5007.10 --> 5012.96]  of cool inferencing with an existing model that you can then go do some of the stuff with. So with open
[5012.96 --> 5017.46]  source, that's the place to go. That's where I think, that's where I think the majority of innovation
[5017.46 --> 5023.46]  is really driving from. And it's a good place to start and figure out what is interesting to you.
[5023.46 --> 5030.94]  And, and even that area I'm, I'm really into, I I'm going to, I'm going to also pitch a language
[5030.94 --> 5037.74]  that I'm into, which is Rust. I mentioned Go beginning of the show, love Go. I, and I use that
[5037.74 --> 5044.54]  in a, in a lot of environments, but I've been using Rust because as a replacement for C, C++ because,
[5044.76 --> 5050.64]  and it's great for embedded. You can use it with no operating system at all. And it's fast as can be.
[5050.64 --> 5056.92]  And so I've been, that's been like, when I go play on my own, aside from like work, work stuff in this
[5056.92 --> 5063.42]  area, I'm always, I'm, I'm every day, I'm looking at all the innovation in the Rust community to do
[5063.42 --> 5069.24]  small little projects that I can do for fun that drives my own passion forward. So it doesn't have
[5069.24 --> 5076.30]  to be a giant 800 pound gorilla or defense industry or whatever kind of thing. It can be, it can be
[5076.30 --> 5081.88]  something that you're, that the kid in you, or maybe the kid in your house can go do on their own.
[5082.26 --> 5086.52]  Give some shout outs to, I guess, some crates or some projects out there in the Rust world. I think
[5086.52 --> 5091.12]  probably Tokyo or Tokyo probably is one of them. Saturday is probably one of them. Yep. What else
[5091.12 --> 5098.22]  you, you, you plan with? Tokyo is really good because it, it allows you to, to, you know, kind of
[5098.22 --> 5102.90]  that, the multi-threaded things, many things happening at once, which is really important in robotics.
[5102.90 --> 5108.40]  And so that's really taken off. There is, I'm trying to remember the name, Embassy is the name
[5108.40 --> 5115.06]  of it. I was trying to remember for embedded. It is a runtime in Rust that allows you to do a whole
[5115.06 --> 5120.28]  bunch of embedded capabilities without writing everything from scratch. It kind of gives you
[5120.28 --> 5126.20]  this framework. And so you can go get a Raspberry Pi, even one of the, the small ones, I think in the
[5126.20 --> 5132.28]  nano and stuff that doesn't have, that isn't, they're supporting the OS and use Embassy to create
[5132.28 --> 5138.34]  an executable that runs on something that's too small for an OS. And so I, I like exploring all
[5138.34 --> 5144.36]  these different possibilities in terms of how you're going to, and I, and when I said Tokyo being
[5144.36 --> 5150.00]  multi-threaded, it wasn't multi-threaded. It was a big concurrency. I said the wrong thing. So I just
[5150.00 --> 5155.82]  want to correct that before we got too far, but being able to do a highly performant concurrent
[5155.82 --> 5162.00]  things on very small pieces of hardware out on the edge is a real thing. Like five years ago,
[5162.12 --> 5166.62]  it just wasn't possible to do anything like what we're doing now. But we're, you know, this,
[5166.98 --> 5170.42]  in the beginning of the show, we talked about the revolution of all these different areas coming
[5170.42 --> 5176.88]  together. Well, now anybody can go use several different, several different languages, but in
[5176.88 --> 5184.88]  my case, rust and, and find small bits that cost me 10 bucks, you know, out there and put some unique
[5184.88 --> 5189.26]  software and do something that scratches my itch that no one in the world has done. And it's no
[5189.26 --> 5194.72]  longer out in the cloud or out on some computer. It's, it can be a, something that I'm carrying
[5194.72 --> 5202.36]  around on my body or is, is literally a robot. This is all reachable now. And so that would, that's
[5202.36 --> 5206.46]  really what I would encourage people to do is the future with people. I get asked all the time about
[5206.46 --> 5212.78]  the future of AI. And I really think the next big revolution in AI is going to be physical AI is,
[5212.78 --> 5219.52]  is AI imbued in all these things in our life that we've been talking about, um, that we refer to as
[5219.52 --> 5224.72]  on the edge in the software world, but that's going to be the new normal. And now you can do that,
[5224.72 --> 5232.22]  uh, without any real budget on your own, anytime from any place in the world. So this, if you want to
[5232.22 --> 5237.28]  go create the future and I said, this is the coolest time we've ever lived in, well, you can
[5237.28 --> 5241.50]  go create that right now, no matter where you're living and no matter what your budget is. So
[5241.50 --> 5245.62]  that's what I said, go do it. If you're tinkering with Russ right now. So let's say you're done with
[5245.62 --> 5250.36]  this podcast, you're off for the day. Let's just say magically you have nothing to do. You're going to
[5250.36 --> 5256.34]  go pick up your next or your current Russ project. Maybe you've got a new model you want to play with.
[5256.46 --> 5260.76]  Where, where are the places you're going? You mentioned hanging face. What are some of the stack
[5260.76 --> 5265.82]  that you're, that you're tapping into? So, uh, there's, there's the swarming stuff that we've
[5265.82 --> 5270.30]  talked about and trying to, and trying to figure out robotics and all that. And we've talked about
[5270.30 --> 5274.56]  home automation. And I think that, that feels for answering this question, that's an accessible
[5274.56 --> 5279.42]  thing that I like to do now. So as I've picked up this kind of home automation stuff, I'm trying to
[5279.42 --> 5285.30]  figure out like, what can I do? I go get some raspberry pies, uh, or I can use a slightly larger,
[5285.46 --> 5290.28]  you know, like a mini PC to do something in the house. None of this costs much. And
[5290.28 --> 5296.08]  I'm now on my day to day when I'm just at home and I'm not thinking about the day job, if you will,
[5296.22 --> 5301.84]  I'm looking at all the things that I do with my family and thinking, wow, you know, like I,
[5301.92 --> 5308.28]  I can go pick something to, to, to handle that. So like almost all the lights in our house are
[5308.28 --> 5315.08]  automated. A lot of the appliances are automated. Uh, we have voice command, you know, from anywhere in
[5315.08 --> 5320.54]  the house where we can, we can, you know, tell a particular assistant, go do this. And it happens.
[5320.98 --> 5326.12]  Uh, I've been starting to integrate AI agents into that workflow. Now that that is becoming,
[5326.12 --> 5333.20]  uh, super accessible with all the, there's so much open source that have made, uh, agents very easy to
[5333.20 --> 5338.42]  do. And you can get small models off hugging face and run it off, off compute that you have in your
[5338.42 --> 5343.88]  house already. Um, and so that's, that's the kind of thing that I like to do. And I think it's amazing
[5343.88 --> 5348.74]  because it's gotten people in my family who are like, oh my God, Chris is doing technology again.
[5348.74 --> 5351.94]  You know, like you have the family members that are like, yeah, yeah. I don't want to hear it.
[5351.94 --> 5355.90]  Cause you're talking about that with everyone else all the time, but now they're like, they're using
[5355.90 --> 5360.18]  that and they're getting interested in like, yeah, they're like, tell me more, Chris. Yeah.
[5360.18 --> 5367.50]  They'll start like, but my wife will say, you know, how could we make this, this, you know,
[5367.50 --> 5371.52]  how can we automate this to make it better? And like, I couldn't get her to, to care.
[5371.52 --> 5375.94]  Yeah. She didn't want to care. Like that was my thing. And just stop talking about it, Chris.
[5376.32 --> 5382.10]  So, um, yeah. And, and, and my daughter, uh, is starting to get really, she's 13 and she's really
[5382.10 --> 5387.04]  starting to think about what can we do? And like, it's just sparks the imagination because it's real
[5387.04 --> 5392.40]  and it's tangible. And so that's like, that's why I get to like, go do something. Just decide
[5392.40 --> 5398.42]  today. You're a maker, go get some cheap stuff, have a vision, recognize that every part of it
[5398.42 --> 5404.80]  is either free or only a few bucks and just go do something in your imagination. If you can't think
[5404.80 --> 5409.44]  of anything, there's tons of websites with maker projects out there and find something that you go,
[5409.50 --> 5414.36]  Oh God, that's cool. And just go do it. And like, even if it, it doesn't have to be the greatest
[5414.36 --> 5418.50]  thing in the world, just go do it. And then you're helping push all this stuff forward.
[5418.60 --> 5423.04]  You are diving into the future and making this stuff happen. And that's why this is the greatest
[5423.04 --> 5427.72]  moment in the history of the world. It really is. I mean, we're, we went from photography or from
[5427.72 --> 5433.00]  painting photos to photography and a blink of an eye. And now we're thinking, gosh, I just wouldn't
[5433.00 --> 5436.92]  like paint the picture that way ever again. I would just take the photo because that's the way.
[5437.34 --> 5443.34]  Yeah. It's a cool moment in life. Um, I'm super curious about one, uh, one particular area that you
[5443.34 --> 5450.32]  mentioned, you mentioned voice. Are you leveraging Alexa or leveraging the behemoths or are you home
[5450.32 --> 5454.86]  assisting in it and you're doing something with home assistance? So I am moving. We have been,
[5454.98 --> 5462.62]  we have been for a while Alexa'd all over the place. And, um, given the fact that, uh, I am,
[5462.86 --> 5470.12]  I am increasingly concerned about privacy just in, you know, in terms of it, like surveillance is so
[5470.12 --> 5478.70]  built into everything now that I am generally moving from, um, cloud-based systems into more
[5478.70 --> 5483.78]  private systems that are completely under my control and local and stuff. And, um, I realize
[5483.78 --> 5489.86]  that may not be for everybody. Um, I think part of that is cause I, I work in a world that is obviously
[5489.86 --> 5494.90]  touching on intelligence and I'm more aware of what's possible from a surveillance standpoint than
[5494.90 --> 5502.24]  probably most people are, um, and how pervasive it is. And that makes me, uh, obviously wanting to
[5502.24 --> 5506.58]  kind of protect our own privacy a little bit. So I'm, I'm keenly interested in automation.
[5507.06 --> 5509.88]  That's not specifically commercial cloud dependent.
[5510.54 --> 5513.86]  We should circle back in the new year for a deeper conversation because I'm sure you'll have
[5513.86 --> 5520.26]  some time away, maybe new progress, new projects and new insights. Cause these are things I'm about to
[5520.26 --> 5527.74]  go into in my curiosity is I haven't automated anything in my house. They're like, Adam,
[5527.76 --> 5530.76]  you're such a nerd. You care about home lab. I'm like, yeah, I don't care about that part of the
[5530.76 --> 5533.88]  home lab. It's, it's a different area of the home lab that I'm trying to conquer.
[5534.30 --> 5539.52]  I didn't either. It really took me for me, the kick in the butt was moving into a house,
[5539.60 --> 5545.08]  buying a house that already came with a lot of automation in it. And it's not, it's not just
[5545.08 --> 5548.80]  catching up on that and learning. There was a certain like ramp, like I had to level up,
[5548.80 --> 5553.58]  but then there was also the, it starts getting your imagination going. Like you didn't like,
[5553.66 --> 5556.80]  you knew in the back of your mind, you could do this, but now you're like, you're living it.
[5557.02 --> 5561.60]  And then you're thinking about the next five things after that. And I think that's it. Once you do a
[5561.60 --> 5567.80]  little bit, you, it wets your appetite and you start seeing all the possibilities. And that's what
[5567.80 --> 5571.72]  it took for me, you know, professional technologist, but I wasn't really doing it until a year ago.
[5571.72 --> 5574.56]  And now this last year is just take off.
[5574.56 --> 5580.70]  Being able to host models locally, have that privacy. The fact that Home Assistant is so
[5580.70 --> 5587.36]  pervasive and so massive as an open source project that they have, you can tap into via the API,
[5587.76 --> 5593.44]  you know, whatever local, you know, models you have running for inference, they have voice
[5593.44 --> 5599.30]  capabilities. There's just so much happening there. Why give that data to, you know, to Amazon? It's not
[5599.30 --> 5603.90]  that they're bad. It's just that I have preferences and the preferences don't involve me telling you
[5603.90 --> 5609.02]  what I want. And then now I get hit with ads for X, Y, and Z as I scroll the internet.
[5609.50 --> 5613.72]  People often complain about how creepy it is that you're almost just thinking about something and
[5613.72 --> 5618.72]  then it shows up in your Amazon cart kind of thing, you know, or Google or whatever. And, and like,
[5618.80 --> 5624.48]  but you're doing, you're doing that. You're giving them that power over you. And so to some degree,
[5624.48 --> 5629.64]  and it's not happened all at once, but I'm, I'm taking responsibility for the fact that that's been
[5629.64 --> 5635.58]  my choice because it was the easy way to go because they were, they were providing this ecosystem. I
[5635.58 --> 5641.22]  didn't have to do much. It just happened. All I had to do was let them was say yes. Every time they send
[5641.22 --> 5646.70]  the updated terms and conditions and, and they would take my data and do whatever they wanted. And there
[5646.70 --> 5653.64]  they are. And I've kind of gotten to that point where I'm done with that and to some degree and,
[5653.64 --> 5654.26]  and turning around.
[5654.26 --> 5659.16]  Just gave me an idea, Chris, they, you know, somebody should, I don't know if this is actually
[5659.16 --> 5664.42]  a good thing or not, but like AI is great at scanning an entire document, like in terms of
[5664.42 --> 5669.76]  conditions, there was a documentary, I think on Netflix about this, that if you tried to read
[5669.76 --> 5675.54]  all the terms and conditions you would agree to in modern society, you would spend more than your
[5675.54 --> 5681.04]  entire life just reading terms and conditions. So to keep up with the updates and, or literally
[5681.04 --> 5687.72]  scrolling them to say, yes, I accept is not, it's not possible. It's not realistic of a request from
[5687.72 --> 5692.58]  the people. So we're agreeing to a lot of things just out of the nature that we don't have the time
[5692.58 --> 5693.14]  to do it.
[5693.54 --> 5696.98]  And you're not going to, if you're trying to get something done and now you have to do through
[5696.98 --> 5701.84]  terms and conditions to get something done, they do it at that moment because they have you,
[5701.92 --> 5705.46]  they know you have to get something done. And what are you going to do? Go, well,
[5705.46 --> 5709.02]  I had to do that thing. It was really important, but now I can't do it because I'm not going to do
[5709.02 --> 5709.82]  terms and conditions.
[5710.04 --> 5711.30]  Bricked. You're bricked now.
[5711.60 --> 5714.10]  Yeah. So I'm, I'm starting to invent my own world.
[5714.10 --> 5715.58]  Or as the kids say cooked, you're cooked.
[5715.88 --> 5721.06]  Yeah. I'm starting to invent my own world where I, I, I'm not bound in that little prison,
[5721.52 --> 5721.98]  if you will.
[5722.98 --> 5729.80]  Well, that was cool. Thanks for deep diving on the swarm, not a swarm, rust, uh, all the things.
[5729.80 --> 5735.38]  Make sure if you don't mind some of the things that you can link us to in the, in the show notes,
[5735.42 --> 5739.44]  I'm sure you got lots of links, just spam us with all your links. We'll put them in the show notes
[5739.44 --> 5740.06]  for everybody.
[5740.72 --> 5745.28]  Fantastic. Thanks for, thanks for having me in guys. It's been great catching up with you and a
[5745.28 --> 5746.34]  fun conversation.
[5746.64 --> 5751.02]  Tons of fun. Go listen to practical AI, practical AI.fm. If you want more, Chris,
[5751.08 --> 5751.82]  that's where you find it.
[5751.98 --> 5756.58]  Thank you, Jared. I'm so glad you did that. Cause I, we would love for people to join the conversation
[5756.58 --> 5762.62]  and we all, it's one big happy family as people can, can see here. And that, uh, uh, I love
[5762.62 --> 5766.70]  changelog and I hope some, some of the changelog people who haven't given us a shot will, will
[5766.70 --> 5768.26]  give us a shot and join our conversations.
[5768.60 --> 5768.96]  There you go.
[5769.20 --> 5771.58]  Practical AI.fm.
[5771.80 --> 5772.28]  That's it.
[5772.46 --> 5776.70]  Go there and be square as they would say in the eighties or nineties.
[5777.16 --> 5778.16]  Which is cool now.
[5778.44 --> 5779.34]  It is cool now.
[5779.52 --> 5780.80]  Yeah. The eighties and nineties are cool again.
[5781.16 --> 5782.28]  Good stuff, Chris. Bye friends.
[5782.72 --> 5783.76]  Bye Chris. Bye friends.
[5783.94 --> 5784.46]  Thanks guys.
[5786.58 --> 5795.74]  All right. That's our show for this week. If you haven't checked out our website,
[5796.14 --> 5801.94]  head to practical AI.fm and be sure to connect with us on LinkedIn X or blue sky. You'll see
[5801.94 --> 5806.18]  us posting insights related to the latest AI developments, and we would love for you to
[5806.18 --> 5810.90]  join the conversation. Thanks to our partner prediction guard for providing operational support
[5810.90 --> 5816.46]  for the show. Check them out at prediction guard.com. Also thanks to break master cylinder for the
[5816.46 --> 5820.98]  beats and to you for listening. That's all for now, but you'll hear from us again next week.
