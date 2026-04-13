[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.38]  Learn how at Fly.io.
[44.50 --> 49.92]  Welcome to another fully connected episode of the Practical AI podcast.
[50.40 --> 55.98]  In these episodes where it's just Chris and I, no guests, we try to keep you updated with
[55.98 --> 59.08]  some of the things happening in the AI world.
[59.30 --> 64.36]  Talk through some things that might help you level up your machine learning and AI game.
[64.58 --> 67.18]  So excited to dig in with you today, Chris.
[67.24 --> 74.02]  I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed
[74.02 --> 74.32]  Martin.
[74.54 --> 77.52]  And I'm Daniel Whitenack, CEO of Prediction Guard.
[78.02 --> 78.70]  How are you doing, Chris?
[79.02 --> 79.94]  I'm doing good.
[79.94 --> 83.30]  It's a, I'm looking forward to our conversation today.
[83.48 --> 88.96]  It's a, it's a snowy day in Georgia and we can, we can talk a little generative AI and
[88.96 --> 93.86]  talk about you, you wouldn't want to use it unless it was snowing in Georgia kind of things.
[93.98 --> 100.52]  In the theme of coldness on today, which is also cold where I'm at, talk about the cold
[100.52 --> 107.02]  side of, of Gen AI or actually, you know, the, what we had talked about thinking through
[107.02 --> 111.92]  were the bad use cases for Gen AI or where you shouldn't use Gen AI.
[112.16 --> 114.88]  Five or more bad use cases.
[115.20 --> 115.36]  Yeah.
[115.52 --> 119.78]  And you know, the funny thing about it is this is a topic that we have casually talked about
[119.78 --> 124.80]  a whole bunch of times and we had not previously said, let's make it an episode.
[124.80 --> 130.06]  But you know, one of the, one of our, I think it may be a little bit of a pet peeve for not
[130.06 --> 136.20]  only us, but other people I talked to in the AI space is there are so many, you know, we're
[136.20 --> 140.66]  at this, you know, huge hype within Gen AI and people just want to use it for everything
[140.66 --> 143.54]  that there could possibly be an AI application for.
[144.52 --> 150.26]  And you know, there's so many places where it doesn't necessarily produce the best outcome
[150.26 --> 150.72]  for you.
[150.78 --> 152.92]  And we talk about this casually all the time.
[152.92 --> 156.14]  So glad that we're actually doing this in the show today.
[156.62 --> 156.66]  Yeah.
[156.72 --> 163.76]  I was creating some, some docs for a, for a customer of ours and some training materials.
[163.76 --> 167.48]  And I have this section just labeled here be dragons.
[169.60 --> 172.40]  So yeah, there might be some hot takes in here.
[172.44 --> 174.94]  I'm interested to hear what, what your takes are.
[175.24 --> 176.66]  My first one.
[176.80 --> 182.90]  So number one, bad use of Gen AI, or maybe one that you want to avoid at least for now,
[182.90 --> 185.22]  is maybe a hot take.
[185.32 --> 192.86]  But I would say from my perspective, completely autonomous agents of any type are currently,
[193.46 --> 199.32]  you know, well, who knows how long this will be the case, but currently and for some time,
[199.96 --> 204.60]  generally a source of sadness for people when they, when they try to create them.
[204.60 --> 212.96]  So what I mean by autonomous agent would be an agent or an automation that, that has no
[212.96 --> 215.90]  human in the loop, just sort of is running in the background.
[216.26 --> 220.18]  And you kind of hope that it does something for you.
[220.18 --> 222.90]  So it could be on the sales side, right?
[223.10 --> 226.40]  Oh, I'm going to have an agent do my whole sales process for me.
[226.46 --> 229.52]  And I'm just going to kind of sit back and work on my product.
[229.70 --> 233.14]  And the agent's going to make all of the sales for me.
[233.14 --> 243.04]  Or maybe it's, you know, some sort of internal admin process that you're automating or, you
[243.04 --> 250.44]  know, even all the way, you know, into manufacturing with automation and implants or, you know,
[250.44 --> 252.98]  more industrial case, whatever you're thinking of.
[253.26 --> 256.28]  My first one is completely autonomous agents.
[256.44 --> 257.72]  What's your, what's your thought, Chris?
[257.72 --> 263.38]  Not only do I think that's right, I'm smiling in a big way because I'm going to throw in
[263.38 --> 265.26]  something from the side just to support that.
[265.48 --> 271.02]  Apparently there is a new show on Netflix and I just read about it last night in a news box.
[271.12 --> 273.16]  Netflix AI is tough for me.
[273.56 --> 277.90]  And, and, and it's, the show is called Cassandra and it's about this.
[277.98 --> 282.86]  It's like a home assistant robot with, you know, with agency in terms of doing lots of tasks,
[282.86 --> 286.44]  but it goes, apparently I have not seen the show yet because I just heard about it,
[286.44 --> 289.16]  but apparently it gets very, very dark.
[289.36 --> 294.38]  And I'm just like, when you were talking about that just now, you know, in, in more of a
[294.38 --> 298.08]  real world scenario, obviously it made me think of that.
[298.18 --> 299.50]  And so, yeah, I, I agree.
[299.60 --> 305.50]  A completely autonomous agent in this day and age with no guardrails around it.
[305.50 --> 311.26]  And you're just saying, go at it, uh, generative AI, uh, especially, especially if it's, uh,
[311.26 --> 318.02]  dealing with anything that has any sort of sensitivity or, uh, requires a little bit of
[318.02 --> 319.02]  thoughtfulness to it.
[319.08 --> 321.02]  I, yeah, not, not going there.
[321.14 --> 321.26]  Yeah.
[321.64 --> 330.36]  Well, and I think even beyond the kind of security, privacy related things, a lot of times I just
[330.36 --> 333.76]  see people trying to do this and it just doesn't really work that well.
[334.34 --> 335.86]  Early days, early days.
[335.98 --> 336.06]  Yeah.
[336.10 --> 337.28]  It's, it's early days.
[337.42 --> 342.70]  So like when you have, and for those that, you know, maybe have or haven't listened to
[342.70 --> 347.40]  previous episodes, when, when we're talking about an agent, we mean, you know, you give
[347.40 --> 350.64]  a task to some sort of system.
[350.64 --> 358.02]  Um, it has the ability then to generate queries maybe into other systems like APIs or databases
[358.02 --> 361.58]  or data stores or other things to accomplish a certain task.
[361.58 --> 366.02]  And it kind of loops over that task until it reaches, reaches an objective.
[366.44 --> 367.02]  Right.
[367.14 --> 373.56]  And in the autonomous, fully kind of autonomous case, you would have, you know, just using the
[373.56 --> 376.20]  sales example, cause it's easy.
[376.20 --> 382.60]  You know, you want an agent to decide how to find prospects for you on LinkedIn.
[383.34 --> 387.90]  And then you want to gather, you know, a dossier about all of those prospects.
[388.40 --> 391.26]  And then you want to initiate the contact.
[391.26 --> 395.32]  And then you want to pull off some type of demo or call.
[395.52 --> 399.68]  And then you want to, you know, close the deal and do the contract arrangement.
[399.68 --> 400.20]  Right.
[400.20 --> 406.56]  And just sort of like determine how to do every step of that process, basically relate, replacing
[406.56 --> 410.92]  a human and their agency with the autonomous agent.
[411.48 --> 420.20]  Now, I think in that case, we could say certain portions of that can be very interestingly addressed
[420.20 --> 421.86]  with AI functionality.
[421.86 --> 425.04]  So doing the prospecting, generating the dossiers, right.
[425.04 --> 432.26]  Those are, I would consider those good use cases if they're tied to a, you know, maybe
[432.26 --> 436.46]  a sales professional that's deciding how and when to do those things.
[436.82 --> 442.94]  In the imagination, it would be great to think of just kind of letting that run in the background
[442.94 --> 445.30]  and you getting sales all the time.
[445.30 --> 448.50]  But it just doesn't really work very well.
[448.50 --> 453.20]  There's a lot of fragility in that type of system when there's a lot of that determination
[453.20 --> 458.68]  of objectives and determining how to interact with systems and all of these things that produces
[458.68 --> 460.66]  a lot of errors, a lot of fragility.
[461.32 --> 468.74]  It's much, much more productive, at least currently for you to have a tool that can help your sales
[468.74 --> 474.72]  professionals prospect or a tool that can help them create these, you know, dossiers and
[474.72 --> 475.48]  that sort of thing.
[475.48 --> 483.12]  And certainly tie in AI to that, but not kind of this end to end, completely autonomous automation.
[483.74 --> 485.02]  I totally agree with you.
[485.18 --> 489.12]  And I certainly, by the way, just as a clarification from what I said earlier, I was not meaning
[489.12 --> 492.10]  to imply agents would typically have a robotic body.
[492.44 --> 494.88]  Just should I have confused anybody?
[495.08 --> 496.74]  There's a lot of people exploring that.
[496.96 --> 503.30]  There are, there are, you know, just one of the things to note in terms of, you know, we're
[503.30 --> 505.34]  in this, the rise of agents right now.
[505.44 --> 509.56]  It's the hottest thing out there, but there are, you know, it's interesting.
[509.66 --> 513.54]  There are a lot of guardrail mechanisms that are out there.
[513.68 --> 518.98]  I know in the industry I work in and defense, there are, especially in things like, you know,
[519.00 --> 520.80]  weapon systems and stuff like that.
[520.84 --> 523.24]  The DOD has guardrails around such things.
[523.34 --> 526.36]  So if you're listening and aren't familiar with that, but are a little bit worried about
[526.36 --> 530.20]  the world, it's fortunately there are people thinking along these lines.
[530.78 --> 530.86]  Yeah.
[531.04 --> 537.72]  And, and there are, I would say useful agents at this point, just not kind of in that fully
[537.72 --> 538.44]  autonomous.
[538.82 --> 539.22]  Correct.
[539.36 --> 539.94]  Kind of setting.
[539.94 --> 546.48]  So AI systems that can connect to multiple things and maybe are used, triggered by a human
[546.48 --> 547.76]  to do certain things.
[547.76 --> 550.40]  Those are the most successful that, that I've seen.
[550.70 --> 551.08]  Absolutely.
[551.64 --> 553.52]  Number two from me, Chris.
[553.52 --> 554.90]  So we've got autonomous agents.
[555.06 --> 564.00]  Number two for me was time series forecasting or really any sort of prediction mechanism.
[564.46 --> 573.22]  So whether that's predicting, you know, future stock prices or reasoning over series of data,
[573.78 --> 580.30]  making predictions sort of, there's some level of prediction that these models can do somewhat
[580.30 --> 586.06]  well in terms of maybe it's things like general text classification, right?
[586.12 --> 589.42]  Is this, is this message spam or not spam?
[589.42 --> 594.80]  And you can give some examples and you could get some reasonable output from a model like that.
[595.18 --> 600.22]  That's why I kind of honed in on time series forecasting specifically, because at least as
[600.22 --> 605.22]  far as I know, and I know that there's research in this area, kind of using transformer models for
[605.22 --> 606.34]  time series forecasting.
[606.68 --> 612.98]  But when I think of Gen AI, I think of, I'm going to log into chat GPT, or I'm going to
[612.98 --> 615.04]  use DeepSeq or one of these models.
[615.84 --> 621.12]  And, you know, if you paste in a bunch of time series data and try to create a forecast
[621.12 --> 629.60]  just with the Gen AI model and nothing else, then I think that's going to end again in sadness
[629.60 --> 630.14]  for you.
[630.14 --> 632.00]  It's not going to work so well.
[632.50 --> 633.24]  Yeah, I think so.
[633.46 --> 639.24]  I actually had that on my list too, in the form of high stakes financial trading, you
[639.24 --> 639.46]  know.
[639.90 --> 641.12]  High stakes financial trading.
[641.24 --> 646.22]  Where do you want to put your million dollars today, you know, and see where it goes.
[646.50 --> 652.16]  So maybe explore some of the possibilities there, but I don't think I would leave it to
[652.16 --> 656.32]  an agent to forecast or make that prediction on its own.
[656.32 --> 662.92]  Yeah, I think people have shown basically that these models definitely don't have the kind
[662.92 --> 671.26]  of world understanding, real world grounding to make certain reasoning or take certain steps
[671.26 --> 673.80]  in reasoning to make reasonable predictions.
[673.80 --> 678.38]  But also they're really bad, generally really bad with numbers.
[678.38 --> 685.86]  And so you may be able to, even with a vision model, paste in a graph of a time series, right?
[685.90 --> 690.42]  And say, you know, what month was my highest sales if it's a graph of sales, right?
[690.50 --> 695.12]  And a vision model could reasonably return that value to you, right?
[695.18 --> 701.24]  But then if you say, well, now model out my sales for the next four quarters or something
[701.24 --> 706.30]  like that, I think generally that's not going to work so well.
[706.30 --> 715.42]  I guess you could argue that a model could generate code that might use packages, you
[715.42 --> 722.80]  know, forecasting packages to actually make a reasonable forecast over certain data.
[723.60 --> 728.74]  Then, you know, my general question then would be, well, that might be useful to generate your
[728.74 --> 729.56]  code to do it.
[729.62 --> 731.82]  But really, it's not Gen.AI that's doing that.
[731.82 --> 740.66]  It's the stats models in Python or, you know, profit from meta and that sort of thing.
[741.20 --> 741.22]  Yeah.
[741.40 --> 746.38]  I mean, and just in case that confuses anyone, you know, there's the generative AI portion,
[746.60 --> 750.54]  you know, which can, you know, is trained on a general data set.
[750.62 --> 754.66]  And then there's these models that it might be generating code to access,
[754.88 --> 757.76]  which are designed specifically for that function.
[757.90 --> 759.16]  So then those are two different things.
[759.16 --> 759.64]  Yeah.
[759.76 --> 765.22]  The code that ends up being executed is not having anything to do with Gen.AI, basically.
[766.22 --> 766.30]  Yeah.
[766.40 --> 770.84]  And maybe it would be worth highlighting in each of these cases that we talk about, Chris,
[771.16 --> 774.22]  some interesting tooling for some of these things.
[774.74 --> 780.62]  You know, in the autonomous agents case, certainly workflows and automations can be created and
[780.62 --> 781.06]  executed.
[781.24 --> 786.14]  You know, we had Prefect on the show, which is a workflow orchestrator that can be monitored
[786.14 --> 788.16]  and handle retries and all of that.
[788.16 --> 792.80]  That's a great thing if you're looking at kind of workflows and orchestration.
[793.62 --> 801.34]  Time series forecasting, my go-to has usually been Facebook or Meta's profit package, which,
[801.56 --> 803.48]  you know, makes certain things pretty easy.
[803.60 --> 807.08]  But there's also many choices for that as well.
[807.26 --> 812.00]  So take a look through those things if you're interested in the non-Gen.AI side.
[812.00 --> 828.52]  Well, friends, AI is transforming how we do business, but we need AI solutions that are
[828.52 --> 831.72]  not only ambitious, but practical and adaptable too.
[831.98 --> 835.34]  That's where Domo's AI and data products platform comes into play.
[835.34 --> 838.62]  It's built for the challenges of today's AI landscape.
[839.04 --> 843.30]  With Domo, you and your team can channel AI and data into innovative uses that deliver
[843.30 --> 844.46]  measurable impact.
[844.84 --> 848.22]  While many companies focus on narrow applications or single model solutions,
[848.78 --> 854.60]  Domo's all-in-one platform is more robust with trustworthy AI results without having to
[854.60 --> 856.18]  overhaul your entire data infrastructure.
[856.18 --> 862.32]  secure AI agents that connect, prepare, and automate your workflows, helping you and your
[862.32 --> 868.28]  team to gain insights, receive alerts, and act with ease through guided apps tailored to your role.
[868.44 --> 871.20]  And the flexibility to choose which AI models you want to use.
[871.58 --> 873.24]  So Domo goes beyond productivity.
[873.54 --> 877.78]  It's designed to transform your processes, helping you make smarter and faster decisions
[877.78 --> 879.10]  that drive real growth.
[879.24 --> 885.98]  And it's all powered by Domo's trust, flexibility, and years of expertise in data and AI innovation.
[886.18 --> 889.30]  And of course, the best companies rely on Domo to make smarter decisions.
[889.86 --> 891.94]  See how Domo can unlock your data's full potential.
[892.50 --> 896.02]  Learn more at ai.domo.com.
[896.10 --> 899.52]  That's ai.domo.com.
[903.96 --> 906.98]  All right, Chris, on to number three.
[907.60 --> 915.88]  My third one was do not use Gen AI to do complete code rewrites or the complete
[915.88 --> 920.00]  development of your applications, your software applications.
[920.56 --> 920.96]  Thoughts?
[920.96 --> 924.28]  Oh, I've tried that just playing around.
[924.92 --> 929.42]  And I definitely don't think that that's ready for prime time, despite the fact that,
[929.64 --> 936.82]  you know, as we sit here and say this, there have been quite a few CEO luminaries out there
[936.82 --> 940.36]  who have been advocating that over the last year or so.
[940.36 --> 947.44]  And I, I, when I sit down and try to do that, uh, in, you know, I get varying results.
[947.52 --> 953.88]  Uh, and it depends largely on how mainstream a language is, for instance, uh, on how good
[953.88 --> 954.16]  it is.
[954.16 --> 960.50]  But, uh, I haven't gotten anything that I would say is a production grade program, fully functional
[960.50 --> 963.42]  through nothing but generative AI, just toy programs.
[963.58 --> 963.76]  Yeah.
[963.82 --> 964.96]  Without interaction.
[965.22 --> 965.60]  Right.
[965.60 --> 966.40]  Yeah.
[966.94 --> 967.50]  Yeah.
[967.82 --> 974.88]  I, I know this is advancing quickly, so who knows how dated this conversation will be
[974.88 --> 980.34]  in a few months, but I think we've been talking about this for, for some time now and we've
[980.34 --> 985.08]  seen things like Devin and cursor and these sorts of things come out, which are pretty
[985.08 --> 989.34]  amazing and do a lot of really interesting things.
[989.34 --> 995.80]  But often don't kind of provide that full, like I'm going to prompt and get a software
[995.80 --> 997.30]  application out of it.
[997.38 --> 999.82]  There is, there's more to it than that.
[999.98 --> 1006.94]  So I think sometimes people are maybe a bit disillusioned and, you know, a better way to
[1006.94 --> 1013.06]  think about this or there are amazing kind of agents and toolings come out like the Devin
[1013.06 --> 1021.06]  cursor, all hands, when surf, et cetera, that can provide a huge acceleration in your code
[1021.06 --> 1021.58]  development.
[1021.58 --> 1030.42]  I think if you treat them like code assistance and, you know, maybe even junior developers
[1030.42 --> 1032.24]  that you are pairing with.
[1032.24 --> 1032.72]  Right.
[1032.86 --> 1038.12]  So it's not so much that I'm just now a not complete non-developer.
[1038.30 --> 1038.58]  Right.
[1038.58 --> 1044.16]  I have no technical skills and I just say, I want this application and it is generated
[1044.16 --> 1044.58]  for me.
[1044.68 --> 1048.40]  That's really what I'm meaning when I say kind of complete app development.
[1048.58 --> 1053.80]  So Gen AI, from my perspective, is not capable of that right now, or you should not rely on
[1053.80 --> 1055.08]  it for that right now.
[1055.22 --> 1060.48]  There may be interesting demos and cases where some form of that is shown.
[1060.48 --> 1067.02]  But for the most part, I think thinking of the technology integrated into your code, code
[1067.02 --> 1075.42]  and programming as a assistant and even a highly functioning agent that you compare with is
[1075.42 --> 1076.18]  a good model.
[1076.72 --> 1082.78]  Just not the kind of, I guess it's a, maybe it's a specialization of the autonomous agent
[1082.78 --> 1084.04]  thing that I mentioned before.
[1084.32 --> 1084.78]  Sort of.
[1084.88 --> 1089.80]  I think, and I think you're making really good points in that it's, you can't just toss it
[1089.80 --> 1097.10]  over the wall and just say, here's an instruction, do it all and generate kind of a complex set
[1097.10 --> 1098.38]  of programs and stuff.
[1098.48 --> 1103.98]  You know, I have done tasking small things very successfully, but the scope of what they
[1103.98 --> 1106.24]  were addressing was, was constrained.
[1106.54 --> 1111.04]  And, and I think we are, we are there for things like that and doing small bits.
[1111.04 --> 1116.42]  It's, it's not uncommon for me to, you know, generate it's, I, many years ago, I would write
[1116.42 --> 1120.92]  a VBA code, a visual basic for applications for Microsoft stuff.
[1121.26 --> 1122.46]  I don't much anymore.
[1122.46 --> 1125.54]  And so now I'll, I can do something like that.
[1125.54 --> 1130.44]  If I happen to be working for something in office to do something, you know, put, put something
[1130.44 --> 1131.78]  together at work.
[1132.02 --> 1136.22]  But when I'm actually coding up a large project, I've not been sick.
[1136.22 --> 1142.42]  I've, it's very helpful to have different tools on this, but I've not found one yet
[1142.42 --> 1147.46]  that I was able to successfully do a significant coding effort by itself, just tossing it over
[1147.46 --> 1147.76]  the wall.
[1147.84 --> 1148.92]  So I agree with you completely.
[1148.92 --> 1152.88]  It will be interesting to see where we are a year from now, two years from now.
[1153.24 --> 1154.16]  Yeah, well, definitely.
[1154.40 --> 1160.18]  I would encourage people to check out things like Windsurf and Devin and All Hands and Cursor
[1160.18 --> 1161.24]  and all of these things.
[1161.60 --> 1162.32]  Super cool.
[1162.58 --> 1163.50]  Try them out.
[1163.50 --> 1169.16]  But don't expect that if you're, if you're not a programmer or have at least some minimal
[1169.16 --> 1175.42]  level of skill that you're going to create a, a huge application or project with all of
[1175.42 --> 1179.06]  its intricacies and have that work and scale well.
[1179.64 --> 1179.94]  Fair enough.
[1180.26 --> 1180.92]  All right, Chris.
[1181.06 --> 1181.88]  What are we on?
[1182.00 --> 1190.44]  Number four for me on the list of don't do this with Gen AI or bad Gen AI use cases for me
[1190.44 --> 1194.74]  is anything extremely high throughput, low latency.
[1195.50 --> 1204.00]  So of course, small models and very high throughput advances have taken place with Gen AI models,
[1204.00 --> 1213.44]  but still, you know, if you're doing quality assessment of products coming off of a actual
[1213.44 --> 1220.60]  scaled up manufacturing line where you have to do maybe the assessment of each of those
[1220.60 --> 1223.22]  products in a fraction of a second.
[1224.04 --> 1231.74]  Really, you don't want to be reasoning over that data with the Gen AI model and take, you
[1231.74 --> 1236.20]  know, 10 seconds to generate your quality assessment for the product.
[1236.20 --> 1237.82]  It's just not, not feasible.
[1238.30 --> 1239.34]  Yeah, I would agree with that.
[1239.34 --> 1243.42]  And I actually have a subset that I'll throw in on that, that I think kind of fits in there,
[1243.48 --> 1248.94]  which would be kind of like real time applications with critical outcomes.
[1249.28 --> 1249.48]  Yep.
[1249.64 --> 1251.42]  You know, that's a great way to phrase it.
[1251.54 --> 1256.34]  I think that that's, I think that that's a, an area that you would, you know, you may,
[1256.90 --> 1261.82]  you may have generative AI as a component in that mix, but you're going to have to have
[1261.82 --> 1265.50]  some guardrails around it and you're going to have to have some specialized models to keep
[1265.50 --> 1271.04]  things on track because in a real time app where, where things matter on the, on the
[1271.04 --> 1275.84]  tail end, you're, you know, great to use, but you don't want to rely entirely on that
[1275.84 --> 1277.90]  when it goes off the rails, you need some way to catch it.
[1278.02 --> 1279.28]  It doesn't take any time.
[1279.50 --> 1279.52]  So.
[1280.16 --> 1282.96]  And I think you make a couple of great points.
[1283.12 --> 1285.78]  Part of it is around the latency, which I kind of highlighted.
[1285.78 --> 1290.92]  These models just don't operate fast enough and they don't operate in the types of environments
[1290.92 --> 1296.78]  necessarily that you need them to operate in for these type of maybe edge use cases as
[1296.78 --> 1306.08]  well in, in many cases, but also these models perform or they do what they are supposed to
[1306.08 --> 1307.24]  do most of the time.
[1307.36 --> 1307.96]  Right.
[1307.96 --> 1314.82]  But still, if you, if you train a, a computer vision model, for example, to do that manufacturing
[1314.82 --> 1324.14]  task that could run on CPU, extremely high throughput and have a much higher accuracy than any, you
[1324.14 --> 1329.22]  know, generalized vision model out there, even that wouldn't need a GPU to, to run.
[1329.54 --> 1329.64]  Right.
[1329.72 --> 1330.92]  I agree with that.
[1331.26 --> 1331.46]  Yeah.
[1331.56 --> 1333.76]  So it's, it's just not, uh, what is that?
[1333.76 --> 1339.74]  The separation between those two cases is still just really, really high in terms of those,
[1340.02 --> 1342.34]  those kind of use cases merging.
[1342.34 --> 1350.58]  Now, I, I do think that in a manufacturing scenario, right, there's a great, or any of
[1350.58 --> 1355.04]  these sort of other cases that you might think of high throughput critical type of scenarios.
[1355.30 --> 1361.02]  Gen AI is, is very useful, maybe just not for that high throughput, low latency piece,
[1361.04 --> 1369.84]  but certainly for, uh, staff at the manufacturing facility that want to look at and analyze the
[1369.84 --> 1375.52]  data coming off of the quality assessment system and ask questions about, Hey, you know, I see this
[1375.52 --> 1380.56]  alert, pull this data for me to help me understand what's going on.
[1380.92 --> 1386.38]  Or are there any of these types of events that have happened in the past X time?
[1386.38 --> 1392.00]  And that query level side via natural language can be very powerful, for example.
[1392.00 --> 1395.98]  And there's many other things that you could do in those scenarios, but there, there is,
[1396.14 --> 1398.64]  I'm, I'll extend this just a little bit.
[1398.74 --> 1405.12]  Um, as, as you know, I, my personal passion is in autonomous platforms, especially at massive
[1405.12 --> 1407.06]  scale swarming, things like that.
[1407.06 --> 1413.58]  And when you talk about that, one of the areas where I think Gen AI does play is exactly the
[1413.58 --> 1415.60]  equivalent of what you just said on the manufacturing.
[1415.60 --> 1421.52]  And that's, um, having a human in the loop or on the loop that's able to interact.
[1421.52 --> 1427.92]  And so you're using Gen AI to actually be able to, uh, enhance the communication between the
[1427.92 --> 1433.96]  human who is in control or on the loop and able to step in and not, but, but not so much in the
[1433.96 --> 1438.44]  other areas, especially considering that when you have lots of vehicles and this could apply
[1438.44 --> 1443.22]  for lots of different use cases, both in the commercial space and the military space where
[1443.22 --> 1447.66]  you have a lot of, a lot of different platforms or vehicles in communication, which requires
[1447.66 --> 1448.18]  high throughput.
[1448.18 --> 1454.44]  But yeah, I think that the only space there, uh, that is a big one is, is in those interactions
[1454.44 --> 1456.94]  with the humans that are involved in that for, for safety.
[1457.58 --> 1458.14]  Yeah, for sure.
[1458.86 --> 1463.88]  Well, I have one more, Chris, a last interesting bad use case for Gen AI.
[1463.96 --> 1471.90]  The one on my list was anything outside of the major languages of the world.
[1472.32 --> 1478.90]  So anything with any sort of, uh, linguistic diversity or cultural diversity, essentially
[1478.90 --> 1489.40]  the models of the modern Gen AI era maybe work well in the kind of top five to 10 languages
[1489.40 --> 1490.40]  of the world.
[1490.40 --> 1495.42]  But there's 7,000 spoken languages in the world, which means they basically don't work
[1495.42 --> 1499.48]  for any of the languages of the world, except for, for a couple.
[1500.34 --> 1509.74]  And moreover, the kind of cultural context of the models is driven by mostly what has been
[1509.74 --> 1518.56]  gathered either from the internet or by Western tech companies, maybe, you know, Chinese tech
[1518.56 --> 1519.16]  companies.
[1519.40 --> 1527.32]  But there's certainly a bias against kind of search, certain cultural contexts and languages.
[1527.76 --> 1533.12]  And, you know, even if you think about vision or video models, I'm sure the same is true,
[1533.22 --> 1533.42]  right?
[1533.42 --> 1536.00]  Because just certain things aren't represented there.
[1536.24 --> 1543.98]  So the reality is that it would be great if you could, you know, land anywhere in the
[1543.98 --> 1553.92]  world and change your, your chat GPT or whatever to help you interact in, you know, X country
[1553.92 --> 1560.36]  in Africa or Y country in Asia and have that work really well with whatever languages you might
[1560.36 --> 1560.82]  encounter.
[1561.24 --> 1565.62]  But I would say generally, that's not, not the case as of now.
[1566.02 --> 1566.60]  I think so.
[1566.64 --> 1571.40]  I think, and, and I know, I know you haven't mentioned it yourself, but longtime listeners
[1571.40 --> 1576.62]  who have been with us for years will know that, that you used to be in that space in a former
[1576.62 --> 1583.02]  professional life and know quite a bit about, about this topic that you've just brought up.
[1583.18 --> 1585.56]  So yeah, yeah, it's, I agree.
[1585.56 --> 1590.98]  It's, it's definitely, uh, I don't think that's changed substantially, uh, over the last few
[1590.98 --> 1591.24]  years.
[1591.72 --> 1591.80]  Yeah.
[1591.84 --> 1597.00]  And even simple things that don't have a lot to do with, I mean, it has to do with Gen
[1597.00 --> 1600.20]  AI, but also has to do with the tooling around it, right.
[1600.20 --> 1608.00]  In terms of even other scripts in particular Arabic, you know, for example, which of course
[1608.00 --> 1614.80]  is a major language of the world, which to some degrees, you know, models can do reasonably
[1614.80 --> 1619.98]  well at at least some models, the tooling around the Gen AI ecosystem, right?
[1619.98 --> 1628.10]  Like, oh, I want to download this chat SDK or this UI that I can plug in a custom model
[1628.10 --> 1628.44]  to.
[1628.62 --> 1631.86]  This is likely not going to support kind of right to left.
[1632.36 --> 1636.96]  Potentially there's going to be some issues, you know, with the script and other things.
[1636.96 --> 1643.82]  So it's just a kind of another highlight of this disparity that exists and it exists.
[1643.82 --> 1648.30]  And I think is worth highlighting because mostly what we're talking about here is language models
[1648.30 --> 1654.88]  and really language models that support a very small amount of the languages on, on the planet.
[1655.36 --> 1655.46]  Yeah.
[1656.16 --> 1656.38]  Yeah.
[1656.98 --> 1662.64]  But that's what I had, Chris, any thoughts after going through, through the list of bad?
[1662.64 --> 1666.82]  Uh, I think, you know, there, I do have a few thoughts there.
[1667.04 --> 1674.10]  I think one of the things that I've noticed there is that there are kind of high risk and
[1674.10 --> 1679.96]  high and, and, and like where you have significant outcomes that can affect people in a, in a
[1679.96 --> 1680.68]  major way.
[1680.68 --> 1688.24]  And whether it be financial or manufacturing or my industry with defense or whatever, you
[1688.24 --> 1695.90]  know, you don't want to put a general, a general generative AI model in charge of doing things
[1695.90 --> 1697.44]  for which there are no guardrails.
[1697.56 --> 1701.60]  I've, I think that that is a thing that I have noticed across a lot.
[1701.60 --> 1706.06]  And, and I could, I could throw out a couple of other areas where I think that applies like
[1706.06 --> 1708.78]  things like, uh, high stakes legal advice.
[1708.78 --> 1714.90]  Do you have a great tooling within things like, uh, chat GPT and the other big language models
[1714.90 --> 1715.88]  for legal advice?
[1716.54 --> 1716.74]  Yeah.
[1716.80 --> 1722.44]  But would you really want to, uh, you know, literally put your life savings, uh, at risk
[1722.44 --> 1723.40]  with things like that?
[1723.80 --> 1725.52]  Maybe not, maybe not today.
[1725.52 --> 1731.64]  At least you see a lot of this, you see a lot of, uh, uh, AI pervading, uh, medical diagnosis.
[1731.64 --> 1738.14]  And once again, I think there's a, a very good use for those, but probably not by itself,
[1738.14 --> 1739.12]  you know, in isolation.
[1739.12 --> 1739.50]  Yeah.
[1739.50 --> 1746.40]  So any of these areas where you have a substantial, uh, risk in the outcome in terms of good and
[1746.40 --> 1751.08]  bad, uh, you probably want to have guardrails around it across many, many different industries.
[1751.08 --> 1752.86]  And that's, I think that's my takeaway.
[1752.86 --> 1757.74]  And, you know, I think that things are continuing to improve at a really, really rapid pace.
[1757.74 --> 1761.94]  And we've said things and had, you know, two months later had the world change out from
[1761.94 --> 1762.34]  under us.
[1762.34 --> 1766.60]  And that may happen again here, uh, with some of these, but yeah, it's, we're on a learning
[1766.60 --> 1770.36]  curve for these things and they're getting better, but they're not all the way there
[1770.36 --> 1770.62]  yet.
[1771.08 --> 1771.20]  Yeah.
[1771.46 --> 1773.52]  I think that's a great way to summarize, Chris.
[1773.64 --> 1778.40]  Thanks for, thanks for chatting through the things with me and we'll look forward to carrying
[1778.40 --> 1780.80]  on the conversation, uh, very soon with you.
[1780.80 --> 1781.52]  Sounds good.
[1787.74 --> 1789.58]  All right.
[1789.86 --> 1791.68]  That is our show for this week.
[1792.06 --> 1798.00]  If you haven't checked out our changelog newsletter, head to changelog.com slash news.
[1798.20 --> 1800.46]  There you'll find 29 reasons.
[1800.70 --> 1801.02]  Yes.
[1801.32 --> 1804.04]  29 reasons why you should subscribe.
[1804.44 --> 1805.88]  I'll tell you reason number 17.
[1806.24 --> 1809.24]  You might actually start looking forward to Mondays.
[1809.24 --> 1812.10]  Sounds like somebody's got a case of the Mondays.
[1812.52 --> 1817.04]  28 more reasons are waiting for you at changelog.com slash news.
[1817.04 --> 1822.66]  Thanks again to our partners at fly.io to break master cylinder for the beats and to you for
[1822.66 --> 1822.98]  listening.
[1823.18 --> 1826.08]  That is all for now, but we'll talk to you again next time.
