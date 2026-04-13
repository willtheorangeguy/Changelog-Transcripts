[0.00 --> 9.64]  Noticing the similarities in the workflow between a quantitative trader and an ML engineer on a recommender system is what kind of gave me the idea for the book.
[9.90 --> 16.34]  I thought, hey, you know, you can describe this all as one instruction book for an engineer and they both could use the same instruction book.
[18.10 --> 20.80]  BAM with for Change Log is provided by Fastly.
[21.12 --> 23.00]  Learn more at Fastly.com.
[23.24 --> 25.52]  Our feature flags are powered by LaunchDarkly.
[25.78 --> 27.60]  Check them out at LaunchDarkly.com.
[27.60 --> 29.70]  And we're hosted on Leno Cloud servers.
[30.00 --> 33.58]  Get $100 in hosting credit at Leno.com slash Change Log.
[34.28 --> 36.88]  This episode is brought to you by our friends at O'Reilly.
[37.26 --> 43.38]  Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform as well.
[43.74 --> 48.18]  The platform has all their books, all their videos, and all their conference talks.
[48.18 --> 59.30]  Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams, and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[59.30 --> 73.26]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security, and even soft skills like business management and presentation skills.
[73.38 --> 75.16]  You name it, it is all in there.
[75.46 --> 80.64]  If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[80.64 --> 84.70]  Learn more and keep your team skills sharp at O'Reilly.com slash Change Log.
[84.86 --> 87.10]  Again, O'Reilly.com slash Change Log.
[87.10 --> 107.60]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[107.84 --> 112.00]  This is where conversations around AI, machine learning, and data science happen.
[112.00 --> 118.36]  Join the community and Slack with us around various topics of the show at change.com slash community, and follow us on Twitter.
[118.50 --> 120.08]  We're at Practical AI FM.
[126.40 --> 129.62]  Welcome to another episode of Practical AI.
[130.00 --> 131.64]  This is Daniel Whitenack.
[131.72 --> 137.72]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson,
[137.72 --> 142.02]  who is a principal emerging technology strategist at Lockheed Martin.
[142.26 --> 142.88]  How are you doing, Chris?
[143.38 --> 144.52]  I am doing very well.
[144.60 --> 145.56]  How's it going today, Daniel?
[145.88 --> 146.58]  It's going great.
[146.68 --> 149.32]  I feel like it's been a productive week.
[150.14 --> 156.84]  I made some progress on some projects and have some new collaborations going, and that's always fun.
[157.08 --> 157.94]  So what about you?
[158.60 --> 159.54]  Same kind of thing.
[160.36 --> 163.16]  Yesterday was like a 15-hour day for work.
[163.20 --> 163.74]  Oh, jeez.
[163.76 --> 166.00]  So there's all sorts of stuff in the air.
[166.00 --> 168.42]  Lots of emerging technologies.
[168.56 --> 169.58]  Emerging technologies.
[169.90 --> 175.86]  And we were talking in the pre-show about something that I have such a deep appreciation for AI right now
[175.86 --> 182.08]  because, as I think I've mentioned before, I'm doing flying lessons, and I'm in this ancient 1973 airplane,
[182.64 --> 186.44]  and every time I'm in it, I'm just like, I'm thinking about us.
[186.54 --> 189.96]  I'm thinking about deep learning and all the things that we're able to do,
[190.38 --> 193.64]  and just wishing that, because I need some help, man.
[193.74 --> 194.46]  I need some help.
[194.46 --> 194.64]  Yeah.
[194.64 --> 195.00]  Okay?
[195.38 --> 196.04]  I'm just saying.
[196.40 --> 201.46]  Did we not have an episode about autonomous flying races and that sort of thing?
[201.48 --> 201.62]  We did.
[201.86 --> 202.58]  Wasn't that a thing?
[202.90 --> 203.16]  Oh, yeah.
[203.22 --> 209.30]  You were like TV host for an autonomous flying thing or something, right?
[209.54 --> 212.78]  We had a fellow named Keith Lynn who was running the show, and he came on.
[212.90 --> 214.62]  It was Alpha Pilot a while back.
[214.76 --> 215.98]  Oh, that's right.
[216.08 --> 216.22]  Yeah.
[216.22 --> 224.66]  So I just want to say I am doing the opposite of Alpha Pilot and really wishing that some of that amazing technology was available to me.
[224.72 --> 232.60]  So I'm just saying I just want to come to the show because we're practical AI and saying there are moments in my life I need a little bit more practical AI to help me out.
[232.66 --> 232.84]  Yeah.
[233.08 --> 233.28]  Yeah.
[233.28 --> 233.96]  There we go.
[234.14 --> 236.94]  Hopefully that technology filters down eventually.
[237.30 --> 237.72]  Absolutely.
[238.08 --> 238.86]  I'm counting on it.
[239.22 --> 239.72]  I'm excited.
[239.88 --> 249.84]  Today, occasionally on the podcast, we get a chance to talk to someone who has authored a new book or updated a book or something like that.
[249.84 --> 256.98]  And, of course, I always love that because, you know, authors have put so much thought into the topics that they're passionate about.
[257.08 --> 261.60]  So it's really good to get their feedback and views on things.
[261.92 --> 270.80]  Today, we have with us David Sweet, who is the author of a new book called Tuning Up from A-B Testing to Bayesian Optimization.
[271.38 --> 271.88]  Welcome, David.
[272.38 --> 272.84]  Thank you.
[272.94 --> 273.64]  It's great to be here.
[273.64 --> 274.20]  Yeah.
[274.20 --> 274.50]  Yeah.
[274.90 --> 285.30]  Maybe before we get into what tuning up means from your perspective, could you just give us a little bit of a background about yourself and how you got into doing what you're doing now?
[285.66 --> 286.00]  Sure.
[286.30 --> 290.20]  I started out getting a PhD in physics.
[290.56 --> 291.96]  It was theoretical and computational.
[292.38 --> 293.20]  So I did a lot of that.
[293.20 --> 293.22]  Yeah.
[293.40 --> 294.48]  Another physics guy.
[294.62 --> 294.94]  I know.
[295.02 --> 295.46]  I love that.
[295.46 --> 300.32]  I don't know what percentage we have on the show, but it is a high percentage.
[300.76 --> 302.18]  And Daniel is a physics guy, too.
[302.42 --> 302.60]  Yeah.
[302.60 --> 304.30]  I'm feeling very left out at this point.
[305.30 --> 307.44]  Physicists get spread far and wide.
[307.62 --> 309.20]  It's a popular subject.
[310.54 --> 314.80]  And I guess the world's only got room for so many professional physicists.
[315.56 --> 315.82]  So, yeah.
[315.86 --> 323.66]  So doing a lot of computer programming kind of lent itself to an industrial job and either in kind of in finance or in technology.
[323.66 --> 326.28]  And I guess I was an East Coaster from New York.
[326.28 --> 330.38]  So that kind of drew me towards finance a little bit.
[330.82 --> 336.70]  But ultimately, I wanted to go into industry because I really wanted to build things that kind of work.
[336.88 --> 339.42]  Like kind of like most engineers kind of have the story.
[339.50 --> 347.74]  They grew up as a little kid working with Legos or something called an erector set or some other kind of building toy like this.
[347.74 --> 353.22]  And the fun of research for me was that I got to do something new.
[353.22 --> 355.26]  But I felt like there was like something missing in it.
[355.34 --> 356.74]  Like the end is you get a paper.
[357.28 --> 360.28]  And it's wonderful because you get to kind of communicate with the world.
[360.28 --> 362.12]  But you don't get to kind of wind it up and watch it go.
[362.34 --> 363.68]  The way like the toys I built in all those.
[363.74 --> 365.14]  So I still had some of that desire.
[365.24 --> 367.64]  And that's kind of what brought me into industry.
[367.92 --> 369.16]  And finance in particular.
[369.16 --> 377.94]  So I'm curious when I was in physics, it was like this urban myth that like, you know, there was a way to go from physics to finance.
[377.94 --> 384.04]  And, you know, there were these like mythical physics people that made that transition.
[384.04 --> 385.90]  But it was very unclear to me at the time.
[385.90 --> 388.04]  Like, how does that happen?
[388.04 --> 391.80]  And like, of course, I as a physics person didn't really know anything about finance.
[391.96 --> 394.18]  And well, I still don't really.
[394.18 --> 398.66]  But yeah, I'm curious, how was that transition for you?
[398.74 --> 402.28]  And was that something that like was on your mind for a while?
[402.70 --> 405.64]  I can say in there are two factors there that mattered.
[405.86 --> 410.78]  One was that there had been people from my group who had gone into finance before.
[411.22 --> 417.64]  And so that kind of set the stage for headhunters to come back to the group or recruiters to come back to the group and look for look for people.
[417.64 --> 429.36]  So I got a call from a recruiter and he talked to me about what, you know, what kind of jobs there were in finance for physicists and what, you know, the one the one in particular he had in mind, but he had kind of others in backup as well.
[429.70 --> 431.86]  And that's what really sparked my interest.
[432.48 --> 438.08]  I had an interest in finance from the perspective of personal finance investing.
[438.08 --> 440.60]  Like I had bought Netscape the day after an IPO.
[440.78 --> 442.50]  That was my first trade.
[442.50 --> 443.70]  And of course, it was Netscape.
[443.70 --> 443.80]  Nice.
[443.94 --> 445.86]  It did really well, but it was like it was very exciting.
[445.98 --> 449.00]  It was, wow, you know, you can buy something and it can go up really quickly.
[449.92 --> 454.10]  And so most investments, most purchases or trades don't go like that.
[454.14 --> 457.22]  But it was, you know, it had the impact that it had.
[457.56 --> 458.62]  So that was the first step.
[458.86 --> 460.42]  The was that there's people in the group.
[460.42 --> 465.46]  But then the second step was just going, I went on an interview just to sort of see what I thought about it.
[465.54 --> 470.34]  And the company was a small company with lots of computing resources.
[470.34 --> 480.58]  And the job was to build a strategy that traded a portfolio autonomously, more or less, you know, almost, you know, almost completely autonomously.
[481.48 --> 482.90]  And and that was very exciting.
[482.98 --> 488.78]  That was that that really was like right up my alley was you'd get to do I get to do coding, which is something I enjoyed for a long time.
[488.78 --> 490.74]  You get to do math, building, building the models.
[490.74 --> 495.24]  But then you get this kind of final piece of satisfaction of just kind of watching it go do its thing.
[495.30 --> 496.68]  And it's pretty cool.
[496.68 --> 500.52]  So did you did you reach that sort of end to end state?
[501.12 --> 504.14]  Well, I was, you know, junior, junior person at the time.
[504.14 --> 506.78]  So the people who had founded the company had built a strategy.
[506.78 --> 507.54]  It was a single strategy.
[507.54 --> 510.36]  So my job was to work on this and improve it and enhance it.
[510.36 --> 514.52]  And, you know, I got to learn how how that kind of thing worked and at the same time make some contribution.
[515.04 --> 516.40]  So what what happened after that?
[516.54 --> 521.92]  Did you end up staying in in finance for some time or how did things kind of progress from there?
[521.92 --> 524.52]  Yeah. So I was in finance for a long time.
[524.66 --> 531.26]  My my next step after that was to go and try to build my own trading strategy.
[531.64 --> 537.32]  And it was at a time when, you know, day trading and intraday trading was something people were doing.
[537.76 --> 542.00]  Lots of people were doing by hand very successfully is right after the Nasdaq dot com boom.
[542.00 --> 547.88]  So I got I partnered up with a buddy from my research group in grad school.
[549.08 --> 550.60]  And we just started building.
[550.70 --> 558.82]  We just went on the Web and went to the Web sites for the exchanges and just figured out how to do this and built a, you know, a small but working trading strategy.
[558.82 --> 563.92]  And it was super exciting in part because we got to build our own thing, but in part or build our own strategy.
[563.92 --> 568.90]  But in part also because we were building our own company at the same time, you know, for the two of us.
[569.10 --> 573.68]  It was interesting that it was a totally different kind of experience from anyone I had up to that point.
[573.76 --> 583.30]  Up to that point, I'd always and I think a lot of people have this experience going through school is you rely on your practice to give you confidence that you can do a particular thing that you've learned.
[583.30 --> 594.04]  When you go to build a business, you have to kind of build this meta confidence that you can figure out how to do new things, which is nerve wracking, but super exhilarating.
[594.16 --> 595.68]  It was a lot of it was a lot of fun.
[596.20 --> 596.30]  Cool.
[596.36 --> 596.96]  That sounds cool.
[597.14 --> 604.90]  So I can't help but ask, you know, being the podcast that we are and having, you know, you tackled the finance side of things.
[605.38 --> 607.44]  You know, what is the state of AI?
[607.68 --> 611.14]  Because I don't think we've had anyone on the show in that specific arena.
[611.14 --> 613.72]  AI and the world of finance and trading.
[614.04 --> 614.76]  How do you see it?
[614.82 --> 616.16]  What do you think of it at this point?
[616.26 --> 616.98]  What's the state?
[617.66 --> 617.88]  Sure.
[618.02 --> 628.38]  What I see from talking to colleagues, you know, from the past that have kind of spread out all over to different companies from like early in my career, people progress and they go different directions.
[628.58 --> 629.38]  But we keep in touch.
[629.38 --> 636.20]  And what I see people doing quite a bit in short term trading strategies.
[636.74 --> 638.68]  Well, I'll back that up.
[638.74 --> 642.34]  Long term, too, but for different reasons, is I see three things.
[642.40 --> 648.88]  One is I see linear models with lots of regressors and automatic feature selection and kind of like pre-deep learning.
[649.86 --> 651.64]  You may call it linear machine learning.
[651.64 --> 652.20]  Right.
[652.28 --> 663.66]  So you're building linear models, but not interactively and carefully building, checking each regressor, but putting in lots of signals and automatically turning them into a compact model.
[663.94 --> 665.46]  I always think of Hastie and Tip Sharani.
[665.58 --> 667.52]  They have this book out in this whole methodology.
[667.68 --> 670.58]  You build a large dictionary of signals and use sparsity and whatnot.
[670.58 --> 690.96]  So I see that I see a deep learning used for interpreting maybe alternative data sets, sometimes, you know, short term trading where you get lots and lots of samples and you need to take something like the order book, which maybe all your listeners are familiar with this, but like it's a complex data structure.
[690.96 --> 700.94]  And so to turn it into something to something you can predict with, you have to do a lot of feature engineering and you can either do it manually or you can use some kind of automated feature representation learning.
[701.56 --> 706.12]  The other thing I see a lot of is optimization of a simulation.
[706.44 --> 707.80]  Now, this is like old school.
[708.02 --> 714.18]  This is like 19, maybe 70s on, maybe even earlier, depending on how you want to call it simulation.
[714.48 --> 717.36]  So optimization of simulation is like an old school engineering technique.
[717.36 --> 724.22]  You build a model, you build a simulator for it, and you want to run a controller and controllers are hard to solve.
[724.36 --> 727.04]  There's no quick and easy solution like a linear regression for a controller.
[727.18 --> 730.70]  So you run lots and lots of simulations and you see which parameters work best.
[730.76 --> 732.30]  And there are all kinds of ways to solve this.
[732.74 --> 735.54]  And so that's a lot of what trading is.
[735.62 --> 741.04]  I mean, that's sort of like the end state of building a trading strategy right before you go and put it online.
[741.18 --> 744.34]  And then, yeah, then there's a whole other state.
[744.34 --> 748.80]  But so I think those are the three big AI related things.
[748.88 --> 763.78]  And in terms of simulation optimization today, you might see evolutionary algorithms where, you know, when I first started out, you might just have like one parameter at a time and sweep through 10 values and make sure it looks pretty good to the eye on the graph and then repeat that process with each new parameter.
[763.78 --> 766.84]  Now, you know, it's more automated black proxy.
[767.72 --> 783.98]  Do you feel like on that front that in the sort of trading space, there's been a sort of a time in which people are considering and trying all sorts of new things as related to these new types of models that are that are coming out?
[783.98 --> 793.58]  Or do you feel like it's been pretty progressive and incremental in terms of the same sort of strategy, but with maybe a different model like you're talking about?
[793.78 --> 804.94]  Or are people trying, you know, like I'm thinking of things like reinforcement learning or other things to, you know, try sort of whole new approaches to the problem?
[805.32 --> 806.24]  This is a good question.
[806.24 --> 809.48]  I have, as you were asking, I came up with four different answers.
[809.58 --> 809.84]  I'm going to go.
[810.50 --> 810.90]  Awesome.
[812.02 --> 812.80]  Talk about them.
[812.92 --> 814.74]  Maybe I'll try to do them most interesting to least.
[814.90 --> 821.36]  But the one thing there's this interesting cultural dynamic in finance, which is in trading.
[821.48 --> 823.10]  I shouldn't say finance, trading specifically.
[823.30 --> 824.42]  I even narrow it down more.
[824.60 --> 836.12]  Quantitative trading where people, especially when they're new to the field, they want to come in and they want to try the latest and greatest algorithms and ideas and everything they've learned, you know, recently in school.
[836.12 --> 841.54]  They're from papers or whatnot and make some money and make, you know, build the magic machine that makes a ton of money.
[841.86 --> 845.48]  And on the other side, you've got people who've been doing it for a while, usually, you know, mentoring.
[845.60 --> 850.16]  There are people who roll their eyes at every new thing and say, ah, I know that's not going to work.
[850.58 --> 851.82]  Neural networks don't work.
[852.18 --> 853.06]  SVMs don't work.
[853.16 --> 854.36]  And, you know, and sometimes they're right.
[854.40 --> 855.08]  Sometimes they're wrong.
[855.34 --> 860.06]  I think if you say something's not going to work, you'll usually be right, but you just won't be productive.
[860.06 --> 867.36]  So it's one of the unfortunate aspects of the distribution of new quality of new ideas in engineering.
[867.84 --> 873.34]  So what I find is that I've seen, you know, I've seen people try or I've been one of the other ones who've tried all kinds of things.
[873.44 --> 879.02]  Basically, you know, everything that you, if you wanted to just randomly throw out ideas, it probably, I've seen somebody try it.
[879.50 --> 880.64]  And some of the things stick.
[880.64 --> 883.38]  And, you know, some people figure out how to get things to work.
[883.52 --> 888.98]  The big problems with financial data are the signal to noise ratio is very low.
[889.82 --> 894.24]  The signals aren't just small, but they're competed away.
[894.66 --> 901.86]  The act of going and trading on signals, which your competitors are seeing as well, is squashing the signals.
[902.64 --> 909.76]  And so it creates this non-stationarity where over time, your strategies become less and less tradable, sometimes very quickly.
[909.76 --> 914.08]  And so you constantly have to adapt and look for new ways, you know, to predict or to trade.
[914.48 --> 916.84]  One other thing that you mentioned, reinforcement learning.
[916.92 --> 925.32]  And that brought to mind, I don't think reinforcement learning is ready to just, you know, turn it on and get a usable answer out of.
[925.58 --> 927.34]  In finance, I haven't seen that.
[927.74 --> 930.56]  And I say that only, you know, I say because it's hard.
[930.64 --> 933.40]  I feel like it's still cutting edge for solving this kind of problem.
[933.82 --> 938.00]  I see a lot of promise in offline reinforcement learning, what's been going on the past year or so.
[938.00 --> 939.32]  It's just amazing.
[940.06 --> 948.66]  And it's very much in line with like a machine learning replacement for the old or an AI replacement, I'll say, for the old school simulation optimization.
[949.00 --> 955.56]  Like, how do you make that more automated or, you know, more autonomous, hyper automated, but get that next level of automation.
[955.80 --> 957.10]  So, yeah, so I see a lot of promise, but I don't see it.
[957.20 --> 960.48]  I haven't, you know, just kind of taking that out of the box, making it work.
[960.48 --> 964.94]  So contextual bandit, on the other hand, which is a limited subset of reinforcement learning problems.
[965.28 --> 973.94]  Not only do I think that that's useful, directly useful, but I think people in finance have been doing it ad hoc for a long time anyway.
[974.44 --> 985.30]  You know, if not the most, you know, super efficient way it could be done, you know, the way people understand it these days, I think since the beginning of my career, people have been doing things that kind of look to me like a contextual bandit.
[985.30 --> 985.66]  Yeah.
[985.76 --> 990.56]  I mean, what makes that easier than a full reinforcement learning problem is that you're only predicting the immediate reward.
[990.78 --> 1000.30]  So you don't have to worry about your decision now affecting the state of the world for your decision later and then have this compounding of state changes based on previous decisions.
[1001.34 --> 1006.20]  That's a more, a more IID sample, so to speak, to build your model with.
[1015.30 --> 1025.12]  This episode is brought to you by our friends at Rudderstack.
[1025.32 --> 1029.84]  And we're calling all data engineers to check out Rudderstack Cloud and start building smart customer data pipelines.
[1030.34 --> 1033.24]  Rudderstack is warehouse first, no more silos.
[1033.70 --> 1042.74]  Rudderstack builds your customer data lake on your data warehouse, not theirs, enabling all functionality of a CDP with more security and retaining full ownership of your data.
[1042.74 --> 1045.54]  It's open source and API first.
[1045.84 --> 1049.28]  Rudderstack can be easily integrated into your existing development processes.
[1049.84 --> 1052.58]  And because they're open source, you can see all their code.
[1052.80 --> 1055.24]  So you don't have to worry about vendor lock in or black boxes.
[1055.76 --> 1057.36]  And best of all, they have transparent pricing.
[1057.56 --> 1059.80]  Stop paying your CDP a premium to store your data.
[1060.26 --> 1065.14]  Rudderstack is free up to 500,000 events and pricing scales transparently from there.
[1065.56 --> 1067.60]  Learn more and get started at Rudderstack.com.
[1067.88 --> 1070.12]  Again, Rudderstack.com.
[1070.12 --> 1073.84]  That's R-U-D-D-E-R-S-T-A-C-K dot com.
[1083.28 --> 1087.60]  So, David, I know once upon a time you were working at Instagram, right?
[1087.72 --> 1089.52]  And you were working on recommender systems.
[1089.72 --> 1093.50]  And so, kind of curious, like, what is your perception of the differences?
[1093.50 --> 1102.30]  You know, we've been talking about finance and applying AI ML techniques in finance versus the social media world, the recommenders that you were doing before.
[1102.54 --> 1105.50]  What are they like in and what differences have you experienced?
[1106.16 --> 1110.70]  You know, even though that you're applying some of the same algorithms potentially in both areas.
[1110.70 --> 1124.38]  Sure. That's actually, well, noticing the similarities in the workflow between a quantitative trader and an ML engineer on working on a recommender system is what kind of gave me the idea for the book.
[1124.66 --> 1125.00]  Oh.
[1125.00 --> 1131.72]  I thought, hey, you know, you can describe this all as, you know, one instruction book for an engineer and they both could use the same instruction book.
[1132.06 --> 1137.78]  So, what the workflow looks like typically is first comes ideation and implementation, right?
[1137.78 --> 1139.68]  So, you get some idea of, like, a hypothesis.
[1139.82 --> 1141.60]  I think if I did this, it'll make their system better.
[1141.78 --> 1142.84]  And you code it up.
[1142.84 --> 1145.52]  And the next thing you do is you check it offline.
[1146.10 --> 1150.52]  Now, in finance and trading, that would be like running a back test or simulation of trading.
[1151.02 --> 1160.80]  In recommender systems, you might do a data science kind of analysis of the data, or you might run a survey or have something kind of like a simulation.
[1161.00 --> 1164.48]  I mean, you can read in papers that there are simulations for these kinds of systems.
[1165.02 --> 1167.88]  And then the final step is you put it online.
[1167.88 --> 1174.06]  Mike Tyson has this saying, something like, everyone has a plan until they get punched in the face.
[1175.64 --> 1179.76]  Someone just quoted that to me in Slack yesterday, by the way.
[1180.32 --> 1187.52]  And so, it's really funny that you're mentioning that because I came up with a plan and that was the quote they gave me in Slack.
[1187.88 --> 1190.10]  So, anyway, not to throw you off.
[1190.40 --> 1192.46]  Everyone has a model until they put it in production.
[1192.72 --> 1194.72]  And then, you know, then things change.
[1194.72 --> 1200.36]  And so, it's this final step of trading means you go and you trade and you say, wow, that doesn't look like the back.
[1200.38 --> 1201.58]  I made so much money in back test.
[1201.64 --> 1202.26]  What's going on?
[1202.66 --> 1203.98]  Or, you know, recommender systems.
[1204.34 --> 1205.56]  And, yeah, let's say recommender systems.
[1205.88 --> 1211.46]  You look like you've made a better prediction of whether someone's going to retweet or click like or do whatever.
[1211.58 --> 1214.04]  And you put it online and it didn't quite pan out the way you thought.
[1214.52 --> 1218.88]  Your predictions might not even be as good as they looked in the model offline.
[1218.96 --> 1219.58]  That can happen, too.
[1219.58 --> 1230.32]  So, this final step, this experimentation or the, you know, either it's A-B testing or it's some other type of experimentation method is, I think, super important.
[1230.52 --> 1232.10]  And it's the common final piece in that.
[1232.40 --> 1237.84]  And for me, I feel like it's the hardest piece in a lot of ways because you have the least amount of data to work with.
[1238.22 --> 1240.92]  But it's the most satisfying piece because it's the most accurate.
[1241.06 --> 1241.96]  It's the real system.
[1242.06 --> 1242.60]  It's not a model.
[1242.72 --> 1243.72]  It's not a simulation.
[1243.84 --> 1244.84]  It's the real thing.
[1244.84 --> 1248.58]  You have this tradeoff between the offline stuff.
[1248.86 --> 1249.76]  It can be precise.
[1249.94 --> 1251.14]  It's very quick to iterate.
[1251.58 --> 1253.68]  But it's got bias, model bias, simulator bias.
[1254.48 --> 1258.98]  The live stuff is noisy, but it's accurate because you're really doing it.
[1259.06 --> 1261.00]  And so, that's what I wanted to write about.
[1261.26 --> 1267.50]  And so, what I'm writing in a way that, you know, can be kind of read by quantitative traders or ML engineers.
[1267.94 --> 1269.04]  Yeah, that's awesome.
[1269.04 --> 1273.48]  So, it's definitely a common scenario that people face.
[1273.60 --> 1285.26]  And I think a lot of people just don't know what to do when they get to that place because they put all their time and reading and focus on the sort of offline testing that is also important, right?
[1285.28 --> 1286.70]  We don't want to, like, get rid of that.
[1286.80 --> 1290.12]  But often people don't necessarily know what to do.
[1290.34 --> 1295.86]  Maybe before we get into, like, the details of some of that, could you clear up maybe just some jargon?
[1295.86 --> 1301.60]  So, you know, I've heard all sorts of, like, hypothesis testing, experimentations.
[1302.04 --> 1303.88]  Like, you use the term system tuning.
[1304.34 --> 1311.34]  Are those sort of all things kind of people use interchangeably to talk about this kind of online testing scenario?
[1312.16 --> 1315.48]  Yeah, I see them all as kind of stitched together as one topic.
[1315.48 --> 1331.46]  So, the idea of tuning, I think, harkens back to, like, an AM or FM radio that had knobs on it from, like, 1965 where, you know, you take the knob and you tune a little bit to the left and you hear static and you go to the right and the signal gets better, but you go too far.
[1331.52 --> 1332.04]  It gets noisy again.
[1332.12 --> 1338.54]  So, you tune your radio into, you know, 88.7, you know, K-Rock or whatever, and you get to listen to your music.
[1338.54 --> 1349.60]  Right. So, if you analogize that and you say your engineered system, be it the recommender system or trading strategy, all the parameters in it are, like, knobs on a radio.
[1349.70 --> 1352.28]  But instead of one knob, you have maybe 10 knobs or 100 knobs.
[1352.32 --> 1355.30]  And you have to tune them all to get the thing to work its best.
[1355.86 --> 1357.36]  Then you're, you know, you're tuning the system.
[1357.52 --> 1360.78]  But, you know, you might also call that experimental optimization, right?
[1360.78 --> 1363.58]  So, you optimize these parameters with experiments.
[1364.00 --> 1373.84]  But it really comes down to more of, like, a complex, focused, and efficient, maybe, way of the experimental optimization is of doing some experiments.
[1373.84 --> 1377.36]  Like, an A-B test would be, like, the most basic form of that.
[1377.42 --> 1381.94]  And you really use the same, a lot of the same techniques and mathematics and analysis, whatever, to do it.
[1381.94 --> 1386.62]  You're making me feel old because, you know, in this context, A-B testing is so old.
[1386.62 --> 1390.50]  And I remember back when I felt it was, you know, new and hot.
[1390.68 --> 1393.36]  And so, I'm just going to sit here quietly at this point.
[1394.36 --> 1401.52]  Well, it hasn't changed that A-B testing is the most, like, robust, reliable, and believable way to do things.
[1401.64 --> 1403.04]  So, it hasn't gone away at all.
[1403.04 --> 1415.14]  So, maybe before we go on, could we just talk about what an A-B test is for those out there that maybe are, you know, wondering about this thing that we're all so hyped about?
[1415.14 --> 1424.72]  Sure. So, the A-B test is, like, the engineer's term for medical research, or might call it randomized controlled trial, which might be a phrase more familiar to people in these pandemic days.
[1425.26 --> 1428.44]  But so, the idea is you have some way of doing things.
[1428.50 --> 1434.78]  Let's say you have some way of recommending new posts to somebody on Twitter, you know, ranking the posts.
[1434.82 --> 1436.60]  And you've got some system that does this.
[1436.90 --> 1439.26]  You come up with an idea to make this system better.
[1439.26 --> 1447.82]  And so, A is what you'll call the original system, and B is what you'll call the system with your change applied to it.
[1448.00 --> 1449.86]  So, now, you have two systems slightly different.
[1450.24 --> 1456.50]  And you go and you run them live, and you see how the audience or the users respond to these two systems.
[1457.02 --> 1462.48]  So, you have some – usually, you'll have some kind of business metric, like, how long does the person spend on Twitter?
[1462.68 --> 1466.40]  You know, how long do people spend on Twitter using version A, and how long do they spend on Twitter using version B?
[1466.40 --> 1469.08]  And you want to compare, and you want to see that they spend more time.
[1469.50 --> 1472.88]  Or, well, maybe you want to see they spend less time in this day and age.
[1473.04 --> 1476.74]  But typically, in a business, you'd want more attention from users.
[1477.18 --> 1477.64]  Yeah, yeah.
[1477.74 --> 1494.62]  And I guess in terms of how this intersects with the AI ML community, I mean, A and B testing could be something like you were talking about that can be done outside of, you know, just changing a user interface or testing a drug or, you know, something like that.
[1494.62 --> 1508.22]  But in terms of, like, the ML AI space, I think something people don't often maybe think about is, like, I have this model, I deploy it, and now I want to work on, like, version 2 of the model.
[1508.56 --> 1513.62]  But how do I actually know that that model is going to perform better?
[1513.86 --> 1519.16]  You know, other than on the test set that I already have, how do I know that that model is going to perform better?
[1519.16 --> 1523.26]  So do you use A-B tests for those sorts of scenarios?
[1523.64 --> 1524.16]  Yes, absolutely.
[1524.32 --> 1527.26]  So what you need, like, A-B tests is sort of like the least you can do.
[1527.40 --> 1530.26]  It's the gatekeeper so that you don't ruin your system, right?
[1530.32 --> 1536.78]  So if your B version doesn't perform better, you want to throw it away and don't let it be the new standard version of your system.
[1536.78 --> 1541.74]  And so what sounds like you're kind of alluding to is this problem people run into.
[1542.20 --> 1552.58]  We've talked about it even before, where you try something offline and by the metrics you use offline, the thing you tried, let's say, to be concrete, a machine learning model, right?
[1552.60 --> 1555.06]  And you've done prediction with, say, cross entropy.
[1555.22 --> 1556.04]  You've got a data set.
[1556.22 --> 1558.20]  And your cross entropy has decreased.
[1558.70 --> 1560.92]  It's looking better than the old model.
[1560.92 --> 1565.18]  But you put this now, this model online, but it's online.
[1565.30 --> 1567.02]  It's part of a larger system.
[1567.70 --> 1577.88]  So this is where I like to differentiate between a prediction and control or supervised learning and we'll call reinforcement learning for a lack of a better term.
[1577.96 --> 1580.16]  But these are kind of different ways of looking at this problem.
[1580.32 --> 1585.56]  So in prediction, that's what you would do offline via supervised learning or classifier regressor.
[1585.82 --> 1588.62]  And maybe you predict a probability someone's going to retweet a tweet.
[1588.62 --> 1598.68]  And when you put that online, you might use that probability along with other probabilities of the probability of liking a tweet or the probability of quote tweeting a tweet or commenting on a tweet.
[1598.76 --> 1608.86]  So you have all these kinds of probabilities and combine them to create an interaction ranking, the probability of engagement, the probability of engaging with the tweet.
[1609.12 --> 1611.94]  And that's going to be the number you use to rank the tweets.
[1612.02 --> 1614.42]  You want to put the most engageable tweets first.
[1614.42 --> 1626.32]  So just to connect the two, like if you're stuck with me back in 2005 doing A-B testing and we're moving forward in time and we're starting to apply that, how do you make that transition?
[1626.42 --> 1627.62]  How do those integrate in?
[1627.70 --> 1634.40]  How do you, what's that path forward in a practical sense for starting to move forward on the calendar closer to the present day?
[1634.42 --> 1636.50]  And we're trying to implement that.
[1636.60 --> 1642.48]  I guess what I'm asking is, is that a direct replacement for A-B testing when you're starting to do recommender?
[1642.48 --> 1643.98]  What's the relationship between the two?
[1644.42 --> 1644.82]  I see.
[1644.94 --> 1645.12]  Okay.
[1645.34 --> 1650.96]  So where the A-B testing would come in is you'd run the recommender system with the old model and compare it to the new, the A to the B.
[1651.42 --> 1654.52]  And so the A-B testing would be an experiment you'd run.
[1654.56 --> 1662.02]  You might run it for a couple of weeks or for a month and then see whether users are engaging more with your old ranking model or your new ranking model.
[1662.02 --> 1662.66]  Gotcha.
[1662.66 --> 1662.72]  Gotcha.
[1663.26 --> 1680.40]  And do you feel like this sort of mindset of experimentation is fairly, is embedded enough in the technology space that, you know, it's not hard to sort of convince the product owners to let you run experiments in production?
[1680.40 --> 1686.48]  And, you know, how do people perceive this sort of idea of experimenting online and in that sort of way?
[1686.74 --> 1687.46]  The risk of it.
[1687.78 --> 1688.02]  Yeah.
[1688.36 --> 1688.54]  Yeah.
[1688.54 --> 1697.06]  So it's my understanding that at the larger companies, this is the standard practice is everything gets tested, you know, into production.
[1697.32 --> 1704.34]  Nothing just gets, or typically things don't just get put into production just on a whim or based on domain knowledge or just based on the offline results.
[1704.34 --> 1706.00]  But they're really experiments.
[1706.08 --> 1708.52]  And now the bigger companies, you know, there's lots of money at stake.
[1708.56 --> 1709.54]  So revenue can be high.
[1709.72 --> 1714.62]  So a small percentage change up or down can be a dollar significant, right?
[1714.66 --> 1716.82]  Or engagement or time spent can be high.
[1716.88 --> 1718.60]  And so a small change up or down can be significant.
[1718.74 --> 1722.78]  So these things are, they're all, they're all tested the way I understand it.
[1722.78 --> 1737.10]  I would think, I think it's not an uncommon, less common these days, but not totally uncommon for people to have a feeling that they, an intuition, that they understand their domain and understand whether something is going to be right or wrong.
[1737.16 --> 1740.52]  Whether it's said that it's obviously going to, something is obviously going to be better.
[1740.94 --> 1743.74]  And it's so common to be proven wrong.
[1743.86 --> 1744.86]  It's, it's humbling.
[1744.86 --> 1748.80]  You know, a person, a person who goes through that, I wouldn't say is strange or arrogant.
[1748.92 --> 1749.56]  I would say they're typical.
[1749.56 --> 1755.82]  So, um, and I've done sort of an informal survey over the past 10 years of, of quant traders.
[1755.96 --> 1764.02]  I always ask them what fraction of the ideas that you come up with after you've tested them, um, actually work and, and, you know, end up in your system is a good idea.
[1764.48 --> 1770.06]  And almost everybody who's that, you know, had some experience says one in 10 and just with kind of like shaking their head.
[1771.68 --> 1774.62]  It's just the nature of the beast that you're with a complex system.
[1774.62 --> 1780.12]  Uh, just because things can seem very reasonable, but simply be wrong.
[1780.26 --> 1783.56]  There are just too many dimensions, too many factors to keep in the human mind.
[1783.56 --> 1785.08]  And you really need to just go and test.
[1785.08 --> 1803.02]  Change Log Plus Plus is the best way for you to directly support practical AI.
[1803.54 --> 1813.94]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal, and help sustain our production of practical AI into the future.
[1813.94 --> 1823.00]  Simply follow the Change Log Plus Plus link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1823.30 --> 1827.18]  Once again, that's changelog.com slash plus plus.
[1828.18 --> 1830.94]  Change Log Plus Plus is better.
[1830.94 --> 1832.94]  Change Log Plus Plus.
[1841.28 --> 1845.98]  So, I'm kind of curious as we kind of started to get into some of the techniques.
[1846.20 --> 1852.70]  I was looking through your table of contents on your book and stuff, and you have all of these techniques, most of which I'm not familiar with.
[1852.70 --> 1863.98]  And I was wondering if you could take a moment and kind of tell us briefly what each is and what that relationship is between those so that I'll understand.
[1864.28 --> 1867.76]  I'm super interested, especially when I see things like multi-armed bandits and stuff.
[1869.14 --> 1875.42]  Sure. So the book is laid out in the order – really it's laid out in the order in which I learned these things.
[1875.68 --> 1879.96]  But that also happens to be the order in which they appeared chronologically in the literature.
[1879.96 --> 1885.96]  So A-B testing has been around – I have 200 years or something, 100 years when it really started to pick up.
[1886.28 --> 1890.02]  The next one is response surface methodologies, maybe from the 50s or 60s.
[1890.10 --> 1897.68]  And so what response surface methodology does is it focuses in the experimentation technique on systems with continuous parameters, right?
[1897.70 --> 1899.88]  So like a knob that you could tune continuously.
[1900.00 --> 1906.52]  And if you had a couple of these, if you tune them simultaneously, you can be more efficient than if you tune them one at a time.
[1906.52 --> 1911.04]  If you go one at a time, you might say – you might tune one and say, well, I've got the right value for this one.
[1911.10 --> 1911.52]  It's seven.
[1911.74 --> 1913.96]  And then you tune the other one, you say, oh, the right value for this is three.
[1914.38 --> 1917.10]  But then if you go back and tune the first one, you might find that six is a little better.
[1917.34 --> 1919.24]  And so you can bounce back and forth.
[1919.28 --> 1922.30]  And there's no guarantee that you'll ever find the single optimum for both.
[1922.34 --> 1924.50]  So if you do them together, you can get the right answer.
[1924.56 --> 1934.02]  So the response surface literally means a picture of the function, the surface of the function of like your business metric, like revenue, let's say, versus those two parameters.
[1934.02 --> 1945.50]  So if you imagine a 3D plot with one of those nice colored or wireframe surfaces, and you're looking for the top of that, the highest peak in that surface, that's what response surface methodology is about.
[1945.86 --> 1946.70]  Gotcha. Thank you.
[1946.92 --> 1949.06]  Yeah. So that kind of limits you in some sense.
[1949.12 --> 1951.34]  There are A-B testing you could apply to any two choices.
[1951.52 --> 1952.84]  Should I use red or green?
[1953.02 --> 1958.14]  And there's no real surface between red and green that would make – well, if you do frequencies, there might be.
[1958.38 --> 1961.56]  But there's – well, think about this categorical, red, green, blue.
[1961.62 --> 1962.70]  There's no surface you'd plot there.
[1962.70 --> 1966.54]  But multi-arm bandits, now, they're interesting.
[1966.76 --> 1973.16]  They go back to instead focus on systems where, again, like A-B testing, you compare any two options.
[1973.52 --> 1979.60]  They don't really take advantage of the continuity of a parameter, but you can pick any finite set of values and compare them.
[1980.14 --> 1989.54]  With multi-arm bandits, the real change from A-B testing is that you're focusing on maximizing whatever your business metric is, let's say revenue.
[1989.54 --> 1992.04]  You want to make money while you're running the experiment.
[1992.32 --> 1997.18]  So with A-B testing, I feel like – I think of it as more you really want the information.
[1997.70 --> 2003.40]  You want a reliable answer whether A is better than B, right, because people are going to die if you get it wrong.
[2003.48 --> 2006.00]  Like with drug testing, the stakes are really high.
[2006.06 --> 2007.00]  You really want to get the right answer.
[2007.00 --> 2014.48]  With multi-arm bandits, you want to make money, and you can afford to be – nobody's going to die if you get it wrong.
[2015.42 --> 2016.02]  It's a good thing.
[2016.20 --> 2020.14]  And you can afford to change back and forth very quickly.
[2020.42 --> 2025.56]  So the typical way it works is you take up your set of – let's take a trading example.
[2025.62 --> 2028.92]  Let's say in trading, you're trading 100 stocks, right?
[2029.62 --> 2035.26]  You might say 50 of them to start out, dedicate them to strategy version A and 50 to strategy version B.
[2035.64 --> 2040.80]  And as time comes in, as the returns come in and you see A doing a little better than B, you increase the number.
[2040.88 --> 2042.70]  Say your 60 of them go to A and 40 to B.
[2042.84 --> 2043.76]  And you just keep scaling.
[2043.84 --> 2045.32]  And then 70 to A and 30 to B.
[2045.36 --> 2048.24]  Rather than waiting until the end of the experiment and keeping it 50-50 the whole time,
[2048.62 --> 2051.42]  you kind of scale it gradually toward the one that seems to be doing better.
[2051.42 --> 2061.84]  And as the data comes in and the error bars go down, you scale back and forth however you need until the probability of being in, let's say, B is low, under 5% or 1%.
[2061.84 --> 2064.00]  And you get to decide that percent as your threshold.
[2064.12 --> 2070.48]  So now you're talking about practical or business significance rather than statistical significance as your threshold, your criteria.
[2070.72 --> 2075.36]  Is it ever the case when you're doing that sort of test and adjusting things on the fly?
[2075.36 --> 2089.74]  Let's say you have, you know, model A and model B and it's sort of a mixed bag where, well, it turns out over that time, like actually the mixture of models was better than either model A by itself or model B by itself.
[2090.10 --> 2091.86]  Does that sort of scenario occur?
[2092.42 --> 2092.74]  Yes.
[2093.14 --> 2100.22]  And it could also be that a model A and B running together can be worse than either A or B running alone.
[2100.54 --> 2104.14]  There can be interactions basically depending on what it is you're testing.
[2104.14 --> 2106.20]  And it doesn't just apply to trading.
[2106.50 --> 2108.56]  So, yeah, that can be complicated.
[2108.80 --> 2111.98]  So that process can be complicated by these interactions.
[2112.10 --> 2115.12]  That being said, it would also be complicated if you're just running an A-B test.
[2115.42 --> 2116.74]  The interactions would interfere.
[2116.96 --> 2126.10]  So you kind of have to have this assumption of IID, independent, identically distributed samples in the analyses through these kinds of algorithms typically.
[2126.56 --> 2130.56]  But in reality, your samples are either I nor I nor D.
[2130.56 --> 2132.58]  So they're either I nor I.
[2132.58 --> 2132.64]  Yeah.
[2133.82 --> 2141.84]  And that, I guess, brings me to my next question, which is, you know, typically we think of A, B test, one thing or the other thing.
[2142.06 --> 2145.92]  Do some of these techniques work when you have more than two options?
[2145.92 --> 2149.06]  Like, let's say I have A, B, C, D, and E.
[2149.36 --> 2154.74]  Or is it better to just always sort of assume you're going to test one thing at a time?
[2154.74 --> 2157.74]  As a general rule, it's better to test.
[2158.22 --> 2163.94]  It's more efficient to test statistically to test everything at once, right?
[2163.94 --> 2167.04]  For the same reasons I was talking about with the alluded to with the two knobs.
[2167.44 --> 2173.56]  You know, it's possible that moving, you know, to the left and moving up in your space, moving to the left in your space is good.
[2173.64 --> 2174.52]  Moving up in your space is good.
[2174.60 --> 2176.66]  But moving left and up at the same time is even better.
[2176.66 --> 2182.54]  If it's that kind of space you're testing, then you should do the same thing with A, B testing and test them all at once.
[2183.08 --> 2191.42]  The virtue in doing only two things at a time is that your test gets done faster as you increase the number of things you're testing, the amount of data you need increases.
[2191.94 --> 2193.02]  So your test gets done faster.
[2193.50 --> 2199.52]  You'll typically have less noise simply because you'll have your patience won't be tried as much.
[2199.64 --> 2202.14]  So you'll get maybe you'll get the data you need.
[2202.52 --> 2203.66]  It'll be easier to make a decision.
[2203.66 --> 2207.18]  It's also easier to decide between two things than it is to decide between more than two.
[2207.86 --> 2211.02]  So you just communicate it to your team or that or other teams.
[2211.22 --> 2214.44]  So there are benefits to doing the simpler thing for sure.
[2214.82 --> 2215.58]  You know, but it's a tradeoff.
[2215.86 --> 2215.96]  Gotcha.
[2216.20 --> 2216.36]  Yeah.
[2216.68 --> 2224.66]  So having asked you about your response service methodology and the contextual bandit, how does Bayesian optimization, you have that in the title.
[2225.06 --> 2228.14]  So, you know, I feel like we're moving up toward that.
[2228.24 --> 2229.44]  How does that fit into the equation?
[2229.58 --> 2230.32]  What does it bring us?
[2230.32 --> 2237.14]  Bayesian optimization takes bits from response service methodology and contextual bandits and multi-armed bandits.
[2237.36 --> 2239.96]  But it makes this super automated by comparison.
[2240.10 --> 2241.64]  Response service methodology is very manual.
[2241.78 --> 2242.40]  You make the surface.
[2242.52 --> 2242.82]  You look.
[2242.86 --> 2244.02]  You make a decision where to go.
[2244.60 --> 2253.16]  And Bayesian optimization does the modeling for you, makes the decision about where to test next, what parameter values to test next for you.
[2253.16 --> 2254.16]  It's nice.
[2254.16 --> 2255.48]  And there's this interesting thing.
[2255.54 --> 2258.84]  You've just probably heard the phrase exploitation versus exploration.
[2259.62 --> 2261.44]  And multi-armed bandits will do this.
[2262.16 --> 2268.80]  That's what they're doing when they're waiting towards the AFA is doing better and they're adding more stocks to A and fewer stocks to B.
[2269.20 --> 2271.68]  They're taking advantage of the information that's come in so far.
[2271.76 --> 2273.88]  They're exploiting the information to make more money.
[2273.88 --> 2278.42]  But they're still testing B because they want to explore to bring the error bars down.
[2278.92 --> 2285.12]  And so Bayesian optimization will do that kind of exploitation modeling and decision making for you as well.
[2285.60 --> 2289.56]  And to top things off, it'll also work with categorical and discrete parameters.
[2289.78 --> 2296.36]  So it really brings kind of the rest of the book together into a single, the ideas from the rest of the book together into a single automated technique.
[2296.36 --> 2296.96]  Awesome.
[2297.56 --> 2302.68]  So I'm kind of curious, I guess, just bringing things way down to a practical level.
[2302.92 --> 2309.72]  What are the sorts of practical tools that you can use to do this sort of testing?
[2309.72 --> 2317.76]  Is it things that are available in familiar tool sets maybe to data science or AI people like the Python ecosystem?
[2318.08 --> 2320.60]  Is there common stuff out there that people use?
[2320.60 --> 2328.88]  And how easy is it to sort of set up these sorts of scenarios online in a reasonable and robust way?
[2329.52 --> 2329.66]  Okay.
[2329.96 --> 2335.18]  So for A-B testing, there are lots of tools, both open source and commercial.
[2335.80 --> 2343.34]  And when I say open source, you'll probably find tools that you can make use of in R or in like the NumPy Python ecosystem.
[2343.76 --> 2349.18]  But there are also commercial products that can help you do this online.
[2349.18 --> 2353.96]  And you can sort of submit results to a web service or other ways of accessing.
[2354.12 --> 2355.92]  So A-B testing is well known.
[2356.04 --> 2357.76]  It's the most commonly used of all these techniques.
[2357.84 --> 2359.28]  And there's lots of support for it out there.
[2359.66 --> 2364.90]  On the other end of the spectrum, Bayesian optimization, there's a tool called, open source tool called Axe.
[2365.00 --> 2366.72]  That's written and supported by Facebook.
[2367.80 --> 2369.82]  And that's very good.
[2369.94 --> 2371.36]  That would be the go-to, I would think.
[2371.36 --> 2375.74]  I suspect Google's got something similar.
[2376.18 --> 2377.90]  Although I'm not as familiar with it.
[2377.94 --> 2383.28]  I'm familiar with their paper where they used their optimizer to make better chocolate chip cookies.
[2383.44 --> 2384.24]  Visier, it's called.
[2385.20 --> 2387.74]  And I don't know for sure if there's an open source version of that.
[2387.74 --> 2393.94]  So I guess as we've kind of gone through some of the things you've covered, what are you anticipating going forward?
[2394.18 --> 2401.12]  So as, you know, clearly from early A-B testing and stuff, as we started the kind of, you know, the progression,
[2401.44 --> 2404.04]  and you've just taken us into Bayesian optimization.
[2404.52 --> 2406.58]  And like, what are you thinking of for the future?
[2407.08 --> 2411.72]  What are you getting excited about working on or utilizing going forward?
[2411.78 --> 2414.62]  Do you have any sense of where the next steps might be?
[2415.00 --> 2415.62]  What might go?
[2415.62 --> 2416.06]  Yes.
[2416.56 --> 2420.30]  What I'm most excited about is offline reinforcement learning.
[2420.48 --> 2422.82]  So doing reinforcement learning from small amounts of data.
[2423.34 --> 2430.04]  And really the key to that, it's not so much the learning of the controller, you know, or the strategy or whatnot,
[2430.42 --> 2432.70]  but it's the learning of the simulator itself.
[2433.36 --> 2434.80]  That's where the real power is, right?
[2434.80 --> 2439.84]  If I had a simulator, a learned simulator that I could believe, I could optimize it in, you know, five different ways.
[2439.84 --> 2445.10]  One of which would be, you know, through a reinforcement learning technique like, you know, PPO or something more, you know,
[2445.10 --> 2445.86]  more recent than that.
[2446.22 --> 2452.88]  But learning the simulator from a small amount of data and understanding, you know, what results you can trust in production,
[2452.96 --> 2458.22]  which ones you can't, and, you know, where to go and maybe explore next to get data built to improve the simulator,
[2458.30 --> 2461.96]  these kinds of questions, being able to do that well could be super valuable.
[2461.96 --> 2469.10]  I mean, I know when you read about these kinds of things, the examples are often from robots, robotics.
[2469.30 --> 2470.76]  They can provide a great visual.
[2470.92 --> 2473.32]  You can kind of get data pretty quickly.
[2473.40 --> 2475.76]  But there are industrial processes, I think, everywhere.
[2477.12 --> 2484.26]  So many things work by optimization of a simulator that I think this would be super valuable throughout society.
[2484.46 --> 2484.58]  Yeah.
[2484.68 --> 2485.50]  I'm very excited about this.
[2485.50 --> 2486.18]  Awesome.
[2486.82 --> 2492.84]  Before we end here, I definitely want to let people know, you know, to check out David's book.
[2492.84 --> 2499.46]  But also we have a discount code through Manning, 40% off, which is pretty spectacular.
[2500.34 --> 2504.18]  So you can use the code PODPRACTICALAI19.
[2504.80 --> 2507.10]  We'll put that in our show notes as well.
[2507.26 --> 2509.16]  But that'll get you 40% off.
[2509.50 --> 2512.44]  And I know I'm really excited to dig more into this book.
[2512.44 --> 2514.60]  But David, it's been super fascinating.
[2514.96 --> 2518.58]  And I really appreciate you taking time and explaining some of this stuff to us.
[2518.74 --> 2520.48]  It's really good and it's important.
[2520.68 --> 2529.42]  And like I say, I think it's something that people need to think about more and often are, you know, perplexed by in many scenarios.
[2529.46 --> 2532.62]  And I'm sure your book shed a lot of light on those situations.
[2532.62 --> 2534.44]  So thank you for your work on it.
[2534.44 --> 2536.12]  And thank you for the discussion.
[2536.76 --> 2537.66]  Thanks a lot for having me.
[2537.66 --> 2538.44]  I really enjoyed this.
[2538.44 --> 2544.32]  Thank you for listening to Practical AI.
[2544.94 --> 2548.66]  If this is your first time, make sure you subscribe so you don't miss a thing.
[2549.18 --> 2556.82]  Head to practicalai.fm to subscribe or find us in Apple Podcasts, Spotify, or wherever you listen to podcasts.
[2557.66 --> 2561.78]  And if you get value from the show, please do share it with a friend or a colleague.
[2561.96 --> 2563.34]  We appreciate you spreading the word.
[2564.22 --> 2567.08]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2567.08 --> 2571.20]  It's produced by Jared Santo and our music is provided by Breakmaster Cylinder.
[2571.72 --> 2573.88]  We are brought to you by some awesome sponsors.
[2574.44 --> 2576.90]  Shout out to Fastly, Linode, and LaunchDarkly.
[2577.68 --> 2578.94]  That is our show.
[2579.14 --> 2581.62]  We hope you enjoyed it and we'll talk to you again next week.
[2581.62 --> 2582.78]  Thank you.
[2582.86 --> 2586.76]  Thank you.
[2586.76 --> 2588.40]  Thank you.
[2589.86 --> 2590.06]  Okay.
[2596.12 --> 2602.22]  Thank you.
[2602.22 --> 2603.28]  Thank you.
[2603.28 --> 2603.76]  Thank you.
[2603.82 --> 2604.20]  Thank you.
[2604.30 --> 2604.60]  Thank you.
