[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[17.46 → 20.04] This episode is brought to you by DigitalOcean.
[20.38 → 25.14] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 → 36.82] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 → 42.54] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 → 46.34] Head to do.co slash Changelog to get started with a $100 credit.
[46.64 → 48.82] Again, do.co slash Changelog.
[55.14 → 66.00] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[66.30 → 70.40] This is where conversations around AI, machine learning, and data science happen.
[70.74 → 75.42] Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[75.42 → 76.76] And follow us on Twitter.
[76.90 → 78.56] We're at Practical AI FM.
[78.86 → 80.24] Okay, here's Daniel and Chris.
[80.24 → 87.54] Welcome to another episode of the Practical AI podcast.
[87.98 → 89.28] My name is Chris Benson.
[89.52 → 92.32] I am a principal AI strategist at Lockheed Martin.
[92.58 → 97.74] And with me, as always, is Daniel Whiten ack, a data scientist with SIL International.
[97.94 → 98.94] Hey, how's it going today, Daniel?
[99.32 → 100.32] It's going great.
[100.50 → 104.92] You know, I don't have the coronavirus yet, so that's always a good thing.
[104.92 → 110.18] And, you know, working on some interesting things.
[110.32 → 111.02] So, it's a good week.
[111.48 → 112.22] What about yourself?
[112.60 → 113.28] About the same.
[113.38 → 117.74] I know both of us travel a lot, so I, too, have my eye on that very carefully.
[118.02 → 123.92] So, trying to listen to good science-based recommendations on the kinds of things we should be doing.
[124.30 → 129.02] And other than that, all is going well down in Atlanta, where it's not too cold today.
[129.14 → 130.16] All the raining just a bit.
[130.48 → 131.72] Yeah, nice, nice.
[131.72 → 134.00] I'm excited about today.
[134.32 → 141.66] I know that one thing that we've kind of interacted with for a while is the quote-unquote data science industry,
[141.94 → 144.36] which the title of the podcast is AI.
[144.90 → 149.76] But, of course, AI and data science are all kind of mixed up in an interesting way.
[150.16 → 151.46] So, who do we have on the show today?
[151.94 → 156.32] So, today we have a guest that can tell us all about how data science is changing
[156.32 → 158.44] and how people are interacting and learning from it.
[158.44 → 163.64] We have Matt Brews, who is the global lead data science instructor for General Assembly.
[163.92 → 168.64] And he is also a managing partner for a data science consulting called Beta Vector.
[168.78 → 169.66] Hey, welcome to the show, Matt.
[170.18 → 171.92] Hey, thank you so much for having me.
[172.50 → 176.84] Well, I guess if you could just give us a little bit of background on kind of, you know,
[176.84 → 181.80] how you got to where you got and a little bit of both from the General Assembly perspective
[181.80 → 184.88] and tell us a little bit about what you do at Beta Vector as well.
[185.82 → 185.96] Yeah.
[186.16 → 190.82] So, I guess the best way to describe it is everything that I do has to do with data science.
[191.08 → 195.58] You know, part of my day is focused on doing data science by teaching it to other people,
[195.66 → 198.66] helping to train the next generation of data scientists.
[198.88 → 199.78] And that's a really cool thing.
[199.86 → 201.30] That's what I'm doing with General Assembly.
[201.30 → 207.12] But also, I get to do a little bit more hands-on work by actually implementing some of the data
[207.12 → 212.16] science solutions by advising and building for a bunch of different clients through my
[212.16 → 213.26] consultancy, Beta Vector.
[213.66 → 218.82] So, just about everything I do is very innately connected to data science.
[219.30 → 222.22] How I got into that is a sort of interesting path.
[222.42 → 227.46] So, I've been with Beta Vector for some form or another for about a year now.
[227.46 → 231.90] It's been something long in the making, even though we formally incorporated back in September.
[232.38 → 235.40] But I've been doing some side data science work for kind of long time.
[235.74 → 239.62] I've also been working for General Assembly for about three and a half years now.
[239.94 → 244.52] Prior to that, though, I was doing data science for a political consulting firm.
[244.74 → 251.24] So, I was based in the Washington, D.C. area and was helping to use data science to advance
[251.24 → 253.78] issues and get people elected and that sort of thing.
[253.78 → 258.50] Building models to, for example, forecast who's likely to show up in the next election or
[258.50 → 262.90] who is likely to care about issue X or candidate Y.
[263.32 → 266.88] So, did some hands-on data science with that consulting firm.
[267.12 → 272.16] And then prior to that, I was in grad school at Ohio State where I did a master's in statistics.
[272.78 → 277.48] But one of the things that I thought was really cool about that was when I was in grad school,
[277.68 → 278.92] I got to teach a lot.
[279.02 → 279.78] I taught a little bit.
[279.78 → 280.32] I tutored.
[280.50 → 285.36] I was a TA for a couple of classes in undergrad at Franklin College in Indiana.
[285.52 → 288.94] But when I went to grad school, that's where I really started to ramp up that teaching.
[288.94 → 294.42] I got to teach for a bunch of very, very different classes.
[295.14 → 299.38] A lot of it was aimed at freshmen, but working with people who were going into the business
[299.38 → 302.12] school versus people who were in social science majors.
[302.12 → 308.60] Working with small groups of about 15 to 20 students, all the way up to lecture halls of
[308.60 → 310.34] 315 students.
[310.72 → 315.40] So, I got a really, perfect understanding of how to try and make statistics and data
[315.40 → 317.48] science, et cetera, exciting to people.
[317.68 → 321.56] And in many cases, who weren't as excited to be there as I was.
[321.90 → 325.32] They actually frequently gave me the 8 a.m. slot to teach.
[325.32 → 328.16] And so, it's a hard sell trying to get a bunch of college freshmen.
[328.40 → 330.02] The dreaded 8 a.m.
[330.62 → 331.14] Right.
[331.28 → 331.66] It is.
[332.04 → 332.38] Right.
[332.74 → 333.02] Yeah.
[333.10 → 338.28] So, I'm kind of curious from that perspective, since you have been speaking about this so
[338.28 → 341.58] long and kind of explaining it to students.
[341.58 → 347.70] Also, something I get frequently asked is, you know, given that we talk about AI a lot,
[347.88 → 351.92] we also, I'm involved in some sort of analytics things.
[351.92 → 355.88] And then my job title is data scientist, actually.
[356.12 → 362.36] But I get asked a lot, what is data science, and how is it different from some of these
[362.36 → 367.80] other things, maybe analytics or business intelligence things that people talk about?
[367.80 → 372.26] And I realize that's a hard question because there are so many different answers to that.
[372.34 → 373.64] And it really depends.
[373.82 → 375.16] And there's a full spectrum.
[375.48 → 380.16] I was wondering, from your perspective, as you talk to students, how do you explain what
[380.16 → 381.86] data science is?
[382.10 → 384.90] How do you view its kind of main components, I guess?
[385.54 → 388.26] So, there are two different ways I like to think about it.
[388.50 → 393.78] On one hand, if you're familiar with Drew Conway's Venn diagram of data science, it's where,
[393.78 → 397.78] you know, one of the circles in the Venn diagram is like math and statistics.
[397.80 → 402.68] One of the circles is computer science or programming skills or hacking skills.
[403.12 → 405.82] And then the third circle is subject expertise.
[406.58 → 411.92] And so, oftentimes, data science is represented as the intersection of those three things,
[412.12 → 416.28] the math stats, the computer programming, and the subject expertise.
[417.12 → 422.06] And I like that, but I do think we need to get beyond that a little bit and think of it
[422.06 → 424.44] more as the union of these three things.
[424.44 → 430.68] And the reason that I say that is, I think that when it comes to data science, depending
[430.68 → 436.96] on why you're doing it or what your purpose is, you may not need to be an expert in programming,
[436.96 → 444.56] or you may not need to be an expert in statistics, or you may be able to not know innately or as
[444.56 → 447.36] intimately the subject expertise that you're working with.
[447.36 → 452.30] As an example, there are plenty of people doing data science related things in Excel,
[452.30 → 456.26] I would call that data science, there's a lot of people who may, you know, kind of turn
[456.26 → 457.22] up their noses at it.
[457.28 → 461.36] And I think it's important to if you want to get into data science as a professional field,
[461.62 → 466.14] that you should be able to have tools in your toolkit that are more sophisticated than Excel.
[466.36 → 471.68] But it's certainly possible to do data science in Excel, if that's where you or your organization
[471.68 → 472.52] are kind of at.
[472.82 → 478.42] That gets me into kind of the second definition or description of data science that I personally
[478.42 → 478.70] use.
[479.22 → 486.36] And it's just that data science, I think, is using data to make a more informed decision
[486.36 → 488.74] than if you were to not use that data.
[489.38 → 491.82] And I like that because I think it's simple.
[491.98 → 493.50] I think it's easy to understand.
[493.60 → 497.42] We're just trying to use data to better inform the decisions and the choices and everything
[497.42 → 497.96] that we make.
[497.96 → 503.04] And I think that that's a very flexible definition that applies to a lot of the things, kind of
[503.04 → 506.58] like you mentioned, analytics and business intelligence and all of that.
[506.94 → 510.84] I think the distinction between those or among those is fairly arbitrary.
[510.84 → 513.34] And it depends on different companies and what they want.
[513.40 → 517.52] There are all sorts of incentives there, largely centred around how much they pay people, you
[517.52 → 522.14] might be able to pay people less if they are analysts or BI analysts than if they were
[522.14 → 523.68] data scientists, for example.
[523.68 → 528.34] But I think that at the end of the day, I just think of data science as let's use data
[528.34 → 533.04] to make a more informed decision than we otherwise would be making if we didn't have that data
[533.04 → 534.12] or if we didn't use it.
[534.70 → 539.52] So, you know, you raise a really great point there when you're talking about kind of the
[539.52 → 544.00] different levels that people are engaging in data science from, you know, kind of starting
[544.00 → 548.82] maybe at that Excel level and moving up to very sophisticated applications.
[548.82 → 555.20] And as we have seen in the last few years, this field just absolutely explode, not only
[555.20 → 558.04] in terms of applications, but in terms of the number of roles.
[558.42 → 563.90] And people are kind of engaging in data science or finding it at different levels.
[564.08 → 571.14] How has that kind of fragmentation of a rapidly expanding field resulted in, you know, in looking
[571.14 → 577.42] at it from different skills in terms of different practitioners needing different levels of expertise
[577.42 → 581.46] and different skill sets to fulfill their own roles with so many roles out there now?
[582.06 → 587.32] I think that a lot of this is driven by just, I mean, you're right, you know, because this
[587.32 → 591.80] field has exploded, because there's such a demand for people who can make sense of numbers
[591.80 → 592.50] and of data.
[592.86 → 597.06] I think that there are so many people kind of aiming to get into this market.
[597.32 → 602.54] And so I know that, for example, colleges and universities are doing their best to better
[602.54 → 606.04] prep people to leave and go out into the workforce.
[606.04 → 610.86] There are organizations like, you know, my company, General Assembly, where, you know,
[610.90 → 613.46] our mission is to empower people to pursue the work they love.
[613.56 → 615.52] We want to focus on 21st century skills.
[615.86 → 618.54] And we recognize that there's a skills gap there that exists.
[618.68 → 623.72] And there's a lot of people who want to be able to fill in that skills gap or be able to
[623.72 → 627.32] close that gap between the skills they have and the employers that people want.
[627.52 → 632.74] And at the same time, there are also employers themselves who say, let's try and figure out
[632.74 → 635.88] how we can get the right people in these roles.
[636.24 → 638.54] Do we hire directly out of a college or a university?
[639.04 → 641.56] Do we hire directly out of a General Assembly?
[641.88 → 646.68] Do we try and train people internally, just train coach and train people to get into those
[646.68 → 646.94] roles?
[647.36 → 652.72] Do we, for example, reach out to General Assembly and say, hey, can you train our team specifically
[652.72 → 653.76] to level them?
[653.76 → 656.70] So there's, I think, a lot of different avenues there.
[657.32 → 662.52] And based on the backgrounds of these different organizations and what people are working with,
[662.64 → 664.88] et cetera, you'll notice that fragmentation exists.
[665.16 → 665.92] Perfect example.
[666.72 → 672.50] People who are trained at colleges and universities in statistics and data science will more frequently
[672.50 → 677.74] come from our backgrounds or maybe State than using Python.
[677.74 → 682.86] And I think that there are a number of things for that, but it largely gets back to the types
[682.86 → 687.48] of problems that people in academia tend to be solving and how those tend to be more formal
[687.48 → 692.46] and statistical in nature than a lot of the other work people are doing in data science.
[692.58 → 697.66] Whereas I think that coming from industry, if people jump into data science from industry,
[697.66 → 699.90] you're often working in Excel.
[700.34 → 701.92] Perhaps you're working in Tableau.
[702.26 → 703.50] Maybe you learn Python.
[703.50 → 708.36] And I think Python is commonly a language of choice for a lot of them because those people,
[708.48 → 711.58] they spend a lot of their day cleaning and mugging data.
[711.98 → 715.00] And so I think that, in my opinion, Python is pretty good at that.
[715.22 → 718.94] You notice this kind of everybody comes in with all of these different perspectives and
[718.94 → 720.78] these different incentives and goals.
[721.34 → 724.92] So everybody is in this big universe of data scientists.
[725.24 → 729.66] However, everybody got there through a very, very different path and has very different skills
[729.66 → 730.36] as a result.
[730.36 → 734.42] So there's so much there that I know I want to follow up and ask about.
[734.54 → 739.56] But before we get too far into the conversation about the skills that people are acquiring,
[739.70 → 744.12] how they're acquiring them and all of that, I was wondering if you could kind of give us
[744.12 → 751.86] a glimpse as to some of the main tasks that data scientists do and how AI fits into that.
[752.30 → 758.78] So because we are a practical AI, I want to make sure and make that connection because it is confusing.
[758.78 → 764.80] Like you said, I know some data scientists who are creating their own neural network architectures
[764.80 → 768.28] and publishing academic research papers from their company.
[768.84 → 774.88] And then others, like you say, who maybe they're not running TensorFlow, they're running Excel or
[774.88 → 775.56] something like that.
[776.02 → 781.24] How does AI fit into the tasks that data scientists are typically approaching?
[781.24 → 781.64] Yeah.
[781.64 → 782.16] Yeah.
[782.40 → 787.22] So I think that to address the first question, when it looks, when you say like, what are
[787.22 → 791.12] the types of tasks and things that the data scientists are doing in their jobs?
[791.16 → 793.68] Those vary quite wildly.
[794.10 → 800.36] And I think that there are a lot of, I mean, again, it depends on the needs of your company
[800.36 → 803.82] or the needs of your organization and the backgrounds that people have, et cetera.
[803.82 → 807.84] But one thing that people are fairly surprised to hear is that as a data scientist, especially
[807.84 → 813.00] at the entry level, a significant portion of your time is spent cleaning and gathering
[813.00 → 816.30] and exploring your data and often thrown out figure.
[816.42 → 821.18] I don't know how rooted this is in like actual evidence, but a lot of people ballpark the amount
[821.18 → 827.58] of their time in a project spent on gathering and cleaning and exploring their data at about 80%.
[827.58 → 829.48] Yeah, I would second that.
[829.74 → 833.68] And I know Chris and I have talked a couple of times on here, and I actually enjoy that
[833.68 → 834.46] part of my job.
[834.68 → 839.10] A lot of people seem to think it's really unenjoyable, but he's kind of sick in that
[839.10 → 839.38] way.
[840.72 → 845.08] It's funny that you bring that up because it's a lot of people don't get into data science
[845.08 → 845.86] to do that.
[846.24 → 850.06] Everybody gets excited by and connecting with the other part of your question, the artificial
[850.06 → 851.06] intelligence part.
[851.06 → 855.98] People get really turned on to the idea of neural networks and saying, I want to learn how
[855.98 → 857.14] to build a neural network.
[857.68 → 858.84] And that's great.
[858.98 → 862.78] I think that neural networks can, and it's not just me thinking this, it's true.
[862.92 → 867.08] Neural networks can be used to solve a great many problems.
[867.74 → 872.94] I also think that in order to be able to build those, you've got to start out with kind of
[872.94 → 874.82] the basics and understanding all of those inputs.
[875.00 → 880.82] Because as you and I know as practitioners of this, if your data isn't good, it doesn't
[880.82 → 886.54] matter if you crafted or if you selected the world's greatest neural network, it's not
[886.54 → 887.90] going to do what you want it to do.
[888.38 → 893.66] And so I think that it is surprising to many people getting into the field how much time
[893.66 → 896.10] it's spent on that exploratory data analysis.
[896.64 → 901.60] But how it's so important to understand how critical that is to everything that comes
[901.60 → 902.16] afterward.
[902.16 → 906.16] That's an interesting misconception that I think people have when they're kind of thinking
[906.16 → 910.32] of the kind of the sexy thing that they're, you know, that they, hey, I'm going to go
[910.32 → 912.50] in and do neural networks and AI and all that.
[912.62 → 917.12] And we know that so much of it is in data cleaning and other kind of mundane tasks.
[917.12 → 922.10] Can you kind of talk about some of the other common misconceptions that we tend to experience
[922.10 → 925.84] as we become practitioners in this versus what maybe our expectations would have been
[925.84 → 926.26] up front?
[927.10 → 927.24] Sure.
[927.36 → 933.08] I think that probably the other biggest misconception, at least what I see from students that have
[933.08 → 937.94] come in on day one and who know sort of the broad idea of data science, but the inner
[937.94 → 938.44] workings.
[938.52 → 941.74] I mean, that's why they're coming to General Assembly to learn a lot of that.
[941.74 → 945.76] And this is certainly not a comes in with this misconception, but something
[945.76 → 950.90] that people are somewhat surprised to learn is how much data science you can do without
[950.90 → 956.08] getting into that artificial intelligence or that neural network kind of level of doing
[956.08 → 956.84] data science.
[957.16 → 961.46] And when I use the term artificial intelligence, what I mean is we're trying to get computers
[961.46 → 965.18] to mimic or to simulate human intelligence.
[965.18 → 971.40] I think that people are surprised when we teach models like a linear regression model for
[971.40 → 973.78] listeners who may not have heard of a linear regression model.
[973.92 → 977.84] You may have heard of the term line of best fit in the past where you've just got kind
[977.84 → 982.94] of a scatter plot of data points, and we need to put a line through that data or thinking
[982.94 → 988.06] about a slightly more complicated model, but a related one, a logistic regression model where
[988.06 → 993.12] you're using a curve of best fit to try and predict a one zero outcome.
[993.30 → 997.76] For example, from my political experience, will this person vote or won't they?
[997.76 → 1002.28] I think that the misconception for a lot of people or a misconception is that people often
[1002.28 → 1008.26] think that neural networks will be the solution to all of their problems when in reality, linear
[1008.26 → 1013.70] regression, logistic regression, much more basic techniques for lack of a better word are really,
[1013.88 → 1017.92] really helpful and are often the solution to the problem that you're trying to solve.
[1018.46 → 1021.44] You make a great point there because I'm always telling people don't start with a neural
[1021.44 → 1026.02] network because there's quite a bit of expense in a variety of ways to doing that.
[1026.02 → 1029.44] Start with the thing that will solve it that is the cheapest mechanism.
[1029.96 → 1032.88] And I think that that gets to the heart of data science.
[1033.08 → 1035.08] Our goal is to be able to solve problems.
[1035.28 → 1039.18] Very few of us are doing data science just for the sake of doing data science.
[1039.32 → 1042.90] We're not building neural networks just because we want to build neural networks.
[1043.16 → 1044.78] Now, I think building neural networks is cool.
[1045.00 → 1045.82] Don't get me wrong.
[1046.18 → 1051.64] But at the same time, when we are paid by an organization, we're paid to solve problems,
[1051.64 → 1053.78] not to do data science just for the fun of it.
[1053.78 → 1057.40] And so it's really important to always keep that in mind.
[1057.46 → 1060.70] And I think that's probably the last misconception that I'll bring up is that
[1060.70 → 1066.78] a lot of times people, maybe it's not a misconception, but people often lose the forest for the trees
[1066.78 → 1071.42] and they focus so much on the modelling technique that they're using.
[1071.60 → 1076.56] And then forget that the reason that they're using that modelling technique is to try and solve
[1076.56 → 1080.28] a problem and get a more complete picture of the world around us.
[1080.28 → 1096.92] If you like this show, and you aren't listening to The Changelog, hey, let's fix that bug.
[1097.30 → 1101.16] The Changelog is our flagship show, and we've been doing it for over a decade.
[1101.82 → 1106.22] Adam and I seek out and interview the people who are pushing the world forward with software.
[1106.22 → 1113.00] We dive deep into the hacks, the innovations and the leadership required to do what these amazing people do.
[1113.30 → 1116.46] One recent example is our conversation with Anders Asgard,
[1116.66 → 1120.30] a climate scientist from Denmark who gave us a peek inside his work
[1120.30 → 1124.86] and how he scratched a common itch he has when gathering academic research from around the web.
[1125.32 → 1126.98] Here's a dorky moment from that episode.
[1127.84 → 1130.78] Are you trying to be right or are you trying to solve the world's problems?
[1131.02 → 1131.40] Exactly.
[1131.76 → 1135.82] If you're a scientist trying to be right, well, then your right may not actually be the right.
[1135.82 → 1137.02] Yeah, exactly.
[1137.36 → 1140.34] There's another saying, all models are wrong, but some are useful.
[1141.14 → 1142.44] I like that one.
[1142.92 → 1145.48] There's another saying, all models are wrong, except for mine.
[1145.64 → 1146.02] Mine's correct.
[1147.86 → 1151.40] We had a lot of fun with Anders.
[1151.58 → 1152.60] He's a fascinating guy.
[1153.30 → 1157.86] Continue listening at changelog.com slash podcast slash 378
[1157.86 → 1161.36] or search for The Changelog on your favourite podcast app
[1161.36 → 1164.86] and find the episode called Open Source Meets Climate Science.
[1165.82 → 1185.82] So, Matt, as we kind of ended up talking about the AI side of things
[1185.82 → 1187.56] and how that's integrating with data science
[1187.56 → 1191.74] and also how, you know, there's been this sort of explosion of roles
[1191.74 → 1193.20] and diversity in data science.
[1193.20 → 1198.20] I was wondering, as you've kind of taught data science over the years,
[1198.34 → 1202.18] how has the toolkit that you're teaching
[1202.18 → 1205.30] and that a lot of people are using for data science,
[1205.38 → 1208.86] how has that kind of shifted or changed over time?
[1208.86 → 1213.24] And I mean, in the sense of, you know, have things become more standardized,
[1213.64 → 1214.42] less standardized?
[1215.06 → 1217.76] Also, as opposed to maybe a few years ago,
[1217.76 → 1221.48] are you having to teach like TensorFlow and GPUs now?
[1221.82 → 1226.06] Or, you know, whereas maybe before it was like Pandas and Scikit-learn?
[1226.32 → 1228.00] Or is it both?
[1228.24 → 1232.10] And also, like, how has the quality of that toolkit changed
[1232.10 → 1235.94] as you've been teaching it in terms of its robustness
[1235.94 → 1237.22] and integrity and all that?
[1238.18 → 1238.38] Yeah.
[1238.56 → 1240.46] So, all perfect questions.
[1240.66 → 1245.08] I think that in terms of the toolkit continues to evolve.
[1245.24 → 1247.64] So, we, I guess, let me lay the groundwork first.
[1247.98 → 1251.74] The program that I teach is a 12-week Monday through Friday,
[1251.92 → 1253.48] 9 a.m. to 5 p.m. class.
[1253.48 → 1256.48] So, it's a full-time 12-week immersive program
[1256.48 → 1261.00] designed to take people from, I'll call it approximately square one,
[1261.20 → 1264.78] where on the first day we're talking about things like data types,
[1264.96 → 1266.76] we're talking about control flow,
[1266.90 → 1269.40] and what's the difference between a for loop and a while loop
[1269.40 → 1270.78] and all of that stuff in Python,
[1271.36 → 1275.38] to at the end of week six, students are presenting a project,
[1275.58 → 1277.20] I like to call it the Reddit project,
[1277.36 → 1280.52] where they choose two Subreddits of their choice.
[1280.52 → 1283.06] They use the Reddit API,
[1283.28 → 1285.54] or they will scrape thousands of postings
[1285.54 → 1287.30] from two different Subreddits,
[1287.50 → 1289.36] and then they will use NLP,
[1289.66 → 1291.66] or natural language processing techniques,
[1291.82 → 1293.54] to parse those out.
[1293.96 → 1296.06] Then they will train a classification model
[1296.06 → 1298.32] to get the computer to understand.
[1298.54 → 1299.96] If you gave it a new post,
[1300.30 → 1301.92] it would be able to tell you,
[1302.18 → 1304.92] does that come from Subreddit A or Subreddit B?
[1305.40 → 1309.00] And it's really cool to see how quickly people grow with that,
[1309.00 → 1311.28] and then that's the halfway point in our class,
[1311.32 → 1314.22] and then people just kind of skyrocket from there.
[1314.72 → 1316.34] So that's a little bit of background
[1316.34 → 1318.04] in terms of the program that we teach.
[1318.20 → 1320.32] In terms of the toolkit that we're using,
[1320.44 → 1322.98] given the Python stack and focused on Pandas
[1322.98 → 1325.40] and Scikit-learn and stats models and all of that,
[1325.66 → 1327.10] those continue to update.
[1327.54 → 1329.88] I think Pandas is at 1.0.0,
[1329.94 → 1331.16] just was released recently.
[1331.60 → 1333.26] Those continue to evolve,
[1333.38 → 1336.48] and so we're staying on top of those changes as they go.
[1336.48 → 1340.20] We have also expanded the amount of content
[1340.20 → 1340.76] that we've had.
[1340.82 → 1342.00] For example, deep learning.
[1342.26 → 1346.04] We used to have one two-hour lesson on neural networks,
[1346.18 → 1348.20] just because three and a half years ago,
[1348.26 → 1350.94] that was something that was not expected to be seen
[1350.94 → 1353.02] in like an intro-level data science role.
[1353.46 → 1354.20] It was just kind of,
[1354.36 → 1356.50] it was good to show people neural networks,
[1356.68 → 1358.16] but it was not reasonable
[1358.16 → 1360.26] that people were going to be fitting neural networks
[1360.26 → 1361.50] in that entry-level role.
[1361.82 → 1364.08] And I will say in most cases,
[1364.08 → 1365.80] certainly not all, but in most cases,
[1366.12 → 1370.08] to now we've extended that to a full week of the class.
[1370.56 → 1373.52] So we are continually changing that
[1373.52 → 1375.84] in response to a couple of things.
[1375.98 → 1378.46] One, what we see as the instructors
[1378.46 → 1380.30] and what we see as our product team
[1380.30 → 1382.92] as the industry changes and develops.
[1383.30 → 1385.66] And two, what we're also seeing from our alumni,
[1385.82 → 1386.84] people graduate, and they say,
[1386.92 → 1388.72] hey, this is what I'm focused on in my job.
[1389.06 → 1391.22] These are the things that were most helpful.
[1391.22 → 1392.62] You know, this is what,
[1393.06 → 1394.90] if you were to change things again in the future,
[1394.90 → 1396.44] these are the things that you should perhaps
[1396.44 → 1398.62] include more of moving forward.
[1399.30 → 1400.90] So Matt, you kind of, a moment ago,
[1401.00 → 1403.30] you talked about the course that you teach,
[1403.36 → 1406.64] the 12-week kind of completely full-time immersive course,
[1406.76 → 1407.96] which raises the question of,
[1408.08 → 1411.16] there are so many different ways these days
[1411.16 → 1414.22] of engaging in education to fit people's needs,
[1414.30 → 1416.02] to fit their lifestyles and such as that.
[1416.14 → 1419.08] So how are you seeing people engage
[1419.08 → 1420.34] in those different ways?
[1420.34 → 1422.88] How does general assembly fit into that?
[1423.30 → 1425.74] And in what, could you just kind of describe
[1425.74 → 1428.14] as you see it, you know, being in that space,
[1428.22 → 1429.92] how you see the options that are available
[1429.92 → 1430.66] for people out there?
[1431.48 → 1432.06] Yeah, of course.
[1432.44 → 1433.78] So I think that when,
[1434.08 → 1436.38] so we were talking before the break
[1436.38 → 1439.12] about people who want to get into the field
[1439.12 → 1440.48] and kind of the options they have.
[1440.58 → 1442.70] Some people may go to a college or a university.
[1443.12 → 1444.82] Some people may go to a general assembly.
[1445.20 → 1447.84] Some people may be trained by their company in some way,
[1447.84 → 1449.28] or they may self-study.
[1449.62 → 1451.74] There are a lot of different options out there.
[1451.74 → 1453.56] And I think that it all comes down
[1453.56 → 1456.02] to a couple of dimensions for most people.
[1456.28 → 1459.46] I think that people think about the time investment.
[1459.78 → 1462.60] People think about the monetary investment.
[1463.08 → 1464.60] I think people also think about,
[1464.80 → 1466.46] related to that monetary investment,
[1466.58 → 1467.78] the opportunity cost.
[1468.08 → 1469.76] For example, if they were to leave work
[1469.76 → 1470.96] and go to general assembly,
[1471.06 → 1472.94] or if they left work to go to grad school,
[1472.98 → 1474.84] or if they went to grad school at night.
[1474.84 → 1477.56] And then also the practicality of the skills
[1477.56 → 1478.64] that they're doing,
[1478.78 → 1480.78] the hands-on nature of the program.
[1481.08 → 1484.24] Where I personally think that general assembly
[1484.24 → 1487.12] sets itself apart is it provides,
[1487.24 → 1489.06] like I said, this three-month program
[1489.06 → 1492.68] to take people from approximately square one
[1492.68 → 1496.88] to be well-qualified for entry-level data science roles.
[1497.18 → 1499.82] And people are often able to get more senior roles
[1499.82 → 1501.88] depending on their backgrounds coming in.
[1501.88 → 1503.98] I think that a great deal of that
[1503.98 → 1506.14] has to do with the applied nature of our program.
[1506.32 → 1509.58] I think when you ask where GA fits into everything,
[1509.96 → 1511.40] I think general assembly fits into it
[1511.40 → 1512.98] just because of its applied nature.
[1513.38 → 1514.42] Like I shared earlier,
[1514.42 → 1516.50] I did a master's degree in statistics,
[1516.50 → 1519.22] and I learned a ton of perfect
[1519.22 → 1521.94] and important things in my master's program.
[1522.84 → 1524.38] And at the same time,
[1524.38 → 1525.46] there were a lot of things
[1525.46 → 1527.24] that were not as applied
[1527.24 → 1528.60] as I would have liked them to be.
[1528.72 → 1529.52] As an example,
[1529.52 → 1532.26] I can't recall working with any data
[1532.26 → 1535.08] that was missing in my grad program.
[1535.40 → 1537.12] I'm sure that you both recognize
[1537.12 → 1539.38] how much missing data we deal with
[1539.38 → 1541.24] on literally a daily basis
[1541.24 → 1542.90] in the practice of data science.
[1543.24 → 1545.06] And how we choose to deal with that is a problem
[1545.06 → 1546.92] and is a challenge for us.
[1547.16 → 1549.42] I think that with minimal exception,
[1549.66 → 1551.22] the largest data set
[1551.22 → 1553.10] that we worked with in grad school
[1553.10 → 1555.38] was probably about 200 rows.
[1555.38 → 1557.74] Whereas that's not the case
[1557.74 → 1560.26] in most data science roles.
[1561.18 → 1562.86] Everything was already sanitized,
[1562.92 → 1564.94] and we just focused on building a model
[1564.94 → 1566.90] instead of thinking about everything else
[1566.90 → 1567.58] that goes into it.
[1567.84 → 1568.70] So all of that is to say,
[1568.82 → 1570.52] I think where GA fits into that
[1570.52 → 1571.96] is for people who say,
[1572.08 → 1575.12] look, I want to commit to learning skills.
[1575.52 → 1577.38] Perhaps I need more of that personal...
[1578.00 → 1579.70] Oversight isn't the right word,
[1579.78 → 1581.06] but maybe somebody says,
[1581.16 → 1582.76] look, I don't have the responsibility
[1582.76 → 1584.30] to do that myself.
[1584.44 → 1586.32] Like, I don't know if I could sit down
[1586.32 → 1588.56] and learn data science on my own,
[1588.66 → 1589.30] start to finish.
[1589.36 → 1591.12] And so I need some support in getting there.
[1591.52 → 1592.74] And for people who are looking
[1592.74 → 1594.98] for specifically practically applied skills,
[1595.32 → 1596.58] I think that that's sort of
[1596.58 → 1598.60] where general assembly fits
[1598.60 → 1600.52] in the broader landscape of things.
[1601.30 → 1603.46] So kind of as a follow-up to that,
[1603.50 → 1604.14] I'm kind of curious,
[1604.70 → 1607.18] and I'm thinking a little bit selfishly myself now,
[1607.38 → 1608.78] you have people obviously
[1608.78 → 1610.50] who are working full-time
[1610.50 → 1612.48] and they're just getting into data science,
[1612.48 → 1613.68] so they're fairly early on,
[1613.72 → 1615.86] and you have people like Daniel and me
[1615.86 → 1617.16] who do this for a living,
[1617.46 → 1619.06] but we're in a fast-moving field
[1619.06 → 1620.76] that's constantly evolving
[1620.76 → 1623.86] and we're constantly levelling ourselves up
[1623.86 → 1625.08] as this continues on.
[1625.24 → 1626.18] What are some of the options
[1626.18 → 1627.84] for people who are working full-time,
[1627.94 → 1629.04] have families to support,
[1629.18 → 1630.16] that they can do?
[1630.28 → 1631.10] What do you recommend?
[1631.48 → 1633.66] And what are those options for us to do?
[1633.98 → 1635.48] I think that if, for example,
[1635.60 → 1637.20] leaving a job as a non-starter,
[1637.28 → 1638.94] which I think it is for many people,
[1638.94 → 1641.22] I think that the best options
[1641.22 → 1642.34] that are out there
[1642.34 → 1644.22] might be either
[1644.22 → 1646.16] looking at a graduate degree
[1646.16 → 1648.44] part-time in the evening
[1648.44 → 1649.20] or on weekends
[1649.20 → 1650.42] or something like that,
[1650.46 → 1652.32] or self-study.
[1652.46 → 1653.36] The biggest challenges
[1653.36 → 1654.88] that I've identified with those,
[1654.96 → 1655.40] for example,
[1655.50 → 1657.86] if somebody goes to grad school at night,
[1658.00 → 1659.22] it just takes way longer.
[1659.36 → 1660.14] Again, it's a trade-off,
[1660.22 → 1661.24] that time and that money.
[1661.64 → 1662.62] We see at GA people
[1662.62 → 1663.64] will be willing to say,
[1663.74 → 1665.20] look, I'll step back from work
[1665.20 → 1666.00] for three months
[1666.00 → 1666.82] and get a job
[1666.82 → 1668.32] toward the goal
[1668.32 → 1669.46] of being able to shorten
[1669.46 → 1671.02] that amount of time
[1671.02 → 1672.56] between now
[1672.56 → 1673.38] and when I would be able
[1673.38 → 1674.74] to get those new skills.
[1675.10 → 1675.60] I also,
[1675.92 → 1676.86] and I think for people
[1676.86 → 1677.84] on the other end
[1677.84 → 1678.14] who say,
[1678.22 → 1679.28] look, I'm just going to study
[1679.28 → 1679.78] on my own.
[1679.84 → 1680.84] I'm not going to commit
[1680.84 → 1681.94] to a graduate program
[1681.94 → 1682.60] that might cost
[1682.60 → 1683.40] however much money.
[1683.56 → 1685.58] I'm going to study on my own.
[1685.94 → 1687.30] It can just be difficult.
[1687.50 → 1687.64] I mean,
[1687.64 → 1689.18] there's so many data science resources
[1689.18 → 1690.40] out there to understand
[1690.40 → 1691.86] what's the right thing
[1691.86 → 1692.96] to try and learn
[1692.96 → 1694.02] and when
[1694.02 → 1694.90] and how it fits
[1694.90 → 1696.00] into the broader picture.
[1696.40 → 1697.78] It can be quite challenging
[1697.78 → 1698.42] to do that.
[1698.50 → 1699.44] Certainly not impossible,
[1699.74 → 1700.78] but I think that
[1700.78 → 1701.72] those are probably
[1701.72 → 1702.52] the two,
[1702.74 → 1703.24] I'll say,
[1703.46 → 1704.56] the easiest options
[1704.56 → 1705.62] or the best options
[1705.62 → 1706.08] for people
[1706.08 → 1706.82] who are currently
[1706.82 → 1708.04] working full-time.
[1708.38 → 1709.12] One caveat
[1709.12 → 1709.82] or one other thing
[1709.82 → 1710.86] that I will share,
[1711.08 → 1711.48] and I promise
[1711.48 → 1712.40] I'm not trying to turn this
[1712.40 → 1713.64] into a general assembly ad
[1713.64 → 1714.56] or anything like that,
[1714.66 → 1715.70] but there are also
[1715.70 → 1716.94] part-time classes
[1716.94 → 1718.30] available in the evenings.
[1718.58 → 1718.88] So there's,
[1718.98 → 1719.34] for example,
[1719.42 → 1721.00] a part-time Python class.
[1721.30 → 1721.90] There's a part-time
[1721.90 → 1722.88] data science class.
[1723.08 → 1723.64] Those certainly
[1723.64 → 1725.10] don't go in as much depth
[1725.10 → 1725.66] as you would see
[1725.66 → 1726.60] in the full-time class,
[1726.80 → 1728.06] but if you say,
[1728.30 → 1729.44] I'm not able to leave a job,
[1729.50 → 1730.18] but I want to get
[1730.18 → 1731.86] that baseline set of skills
[1731.86 → 1733.16] that will give me
[1733.16 → 1734.86] a good enough starting point
[1734.86 → 1735.84] where I can jump off
[1735.84 → 1736.80] and then start
[1736.80 → 1738.48] learning more on my own,
[1738.58 → 1739.12] that's something
[1739.12 → 1739.56] that I think
[1739.56 → 1741.00] is available to you as well.
[1741.52 → 1742.34] So I'm curious,
[1742.50 → 1743.62] after doing
[1743.62 → 1745.04] some teaching myself
[1745.04 → 1746.20] in industry
[1746.20 → 1747.34] and in university
[1747.34 → 1748.36] a bit as well,
[1748.44 → 1749.50] I know one of the challenges
[1749.50 → 1750.52] that I've faced
[1750.52 → 1751.20] in the past
[1751.20 → 1753.90] is standardizing
[1753.90 → 1755.54] a data science
[1755.54 → 1757.18] or AI-related curriculum
[1757.18 → 1758.36] for people
[1758.36 → 1759.98] with varied number
[1759.98 → 1761.32] of backgrounds.
[1761.68 → 1762.32] So I was curious,
[1762.52 → 1763.14] how do you approach
[1763.14 → 1764.34] that in the work
[1764.34 → 1765.18] that you've done
[1765.18 → 1766.08] over the years
[1766.08 → 1767.76] and how have you seen,
[1768.20 → 1768.96] like some people,
[1769.10 → 1769.80] like you said,
[1770.08 → 1770.90] might come into
[1770.90 → 1771.44] the beginning
[1771.44 → 1772.44] of a program
[1772.44 → 1773.38] and they're already
[1773.38 → 1774.80] Python experts, right?
[1774.84 → 1775.66] So learning about
[1775.66 → 1776.44] a for loop
[1776.44 → 1777.06] or a while loop,
[1777.14 → 1777.80] that's going to be,
[1777.92 → 1778.36] they're not going
[1778.36 → 1779.04] to struggle with that.
[1779.12 → 1779.62] They may struggle
[1779.62 → 1780.48] with other bits
[1780.48 → 1781.00] that is,
[1781.18 → 1781.66] on the other hand,
[1781.72 → 1782.62] easy for people
[1782.62 → 1783.64] that already know
[1783.64 → 1784.86] maybe a bunch of math
[1784.86 → 1785.96] or something like that.
[1786.34 → 1787.12] So how do you go
[1787.12 → 1788.50] about standardizing
[1788.50 → 1789.62] that sort of curriculum
[1789.62 → 1791.28] when there's so many people
[1791.28 → 1792.16] coming from so many
[1792.16 → 1792.98] different backgrounds
[1792.98 → 1793.98] into data science?
[1794.48 → 1795.62] Yeah, so one of the things
[1795.62 → 1796.30] that we do
[1796.30 → 1798.02] is there's a certain level
[1798.02 → 1799.72] of pre-work required
[1799.72 → 1801.46] in order to get everyone
[1801.46 → 1803.66] to kind of similar
[1803.66 → 1805.04] starting point on day one.
[1805.16 → 1805.94] For those people
[1805.94 → 1807.04] who are Python experts,
[1807.22 → 1807.40] it's,
[1807.40 → 1808.50] I will broadly say
[1808.50 → 1809.94] that the programming piece
[1809.94 → 1810.44] for them is going
[1810.44 → 1811.48] to be quite easy there
[1811.48 → 1812.12] and they can kind of
[1812.12 → 1812.86] blow through it
[1812.86 → 1814.60] and not need to worry
[1814.60 → 1815.64] about their ability
[1815.64 → 1816.44] on day one.
[1816.88 → 1818.28] We do things quite quickly.
[1818.68 → 1819.86] So by the end of,
[1819.96 → 1820.42] for example,
[1820.66 → 1821.42] day two,
[1821.64 → 1822.56] people are,
[1822.70 → 1823.52] I'm trying to remember
[1823.52 → 1824.00] the exact,
[1824.10 → 1825.46] like the flow of things.
[1825.72 → 1826.40] By the end of day two,
[1826.48 → 1827.76] people are writing functions
[1827.76 → 1829.02] and doing list comprehensions
[1829.02 → 1829.58] in Python,
[1829.78 → 1830.60] which is still going
[1830.60 → 1832.26] to be very basic
[1832.26 → 1833.22] for people who
[1833.22 → 1835.22] know that coming in,
[1835.50 → 1837.22] but we condense it down
[1837.22 → 1838.54] because it is an immersive program.
[1838.62 → 1839.44] We've got 12 weeks
[1839.44 → 1839.80] and we say,
[1839.88 → 1840.04] look,
[1840.08 → 1841.38] let's make the absolute best
[1841.38 → 1842.50] of those 12 weeks.
[1842.88 → 1843.60] So our pre-work is
[1843.60 → 1845.06] an attempt to get folks
[1845.06 → 1846.34] who may not be
[1846.34 → 1847.20] at that level yet
[1847.20 → 1849.32] to prepare before the program
[1849.32 → 1850.98] so that they're at that level.
[1851.48 → 1852.70] Then on day one,
[1852.76 → 1853.00] we say,
[1853.08 → 1853.26] look,
[1853.30 → 1853.82] we're going to talk
[1853.82 → 1854.48] about data types.
[1854.52 → 1855.24] It's going to be quick.
[1855.48 → 1855.70] You know,
[1855.70 → 1857.04] make sure to follow along.
[1857.12 → 1858.00] We're going to work with you.
[1858.20 → 1859.20] We give people support
[1859.20 → 1859.82] along the way,
[1859.86 → 1860.24] of course.
[1860.24 → 1860.72] However,
[1860.98 → 1862.56] we move at a pace
[1862.56 → 1864.06] such that if you do come in
[1864.06 → 1866.06] with that advanced Python background,
[1866.30 → 1867.98] we're getting into statistics
[1867.98 → 1868.92] and distributions
[1868.92 → 1869.76] and all of that
[1869.76 → 1870.82] by like day three
[1870.82 → 1871.60] or day four.
[1872.10 → 1873.66] So it's not a very long time
[1873.66 → 1874.54] that people tend to,
[1874.64 → 1875.22] if you come in
[1875.22 → 1876.56] with that great Python background,
[1876.84 → 1877.56] that people say,
[1877.78 → 1877.92] oh,
[1877.98 → 1878.22] okay,
[1878.34 → 1879.40] like I'm bored
[1879.40 → 1879.70] or I,
[1880.00 → 1880.12] you know,
[1880.14 → 1881.20] this is not as challenging
[1881.20 → 1882.22] as I thought it would be.
[1882.46 → 1883.60] We get through that pretty quickly.
[1884.02 → 1884.50] I'm wondering,
[1884.82 → 1886.04] so one of the questions
[1886.04 → 1887.20] that I get asked
[1887.20 → 1888.32] a good deal
[1888.32 → 1890.12] from companies
[1890.12 → 1891.52] that I'm advising with
[1891.52 → 1892.42] and that sort of thing
[1892.42 → 1893.40] is like,
[1893.50 → 1894.42] what sort of person
[1894.42 → 1895.38] should I hire
[1895.38 → 1897.02] for a data science position
[1897.02 → 1898.76] that maybe isn't
[1898.76 → 1899.80] a data scientist now,
[1899.86 → 1901.58] but they could grow into one
[1901.58 → 1902.16] and,
[1902.44 → 1902.56] you know,
[1902.68 → 1903.38] this is similar
[1903.38 → 1904.26] to what you're talking about.
[1904.30 → 1905.02] There's people that come
[1905.02 → 1906.32] from a lot of different backgrounds
[1906.32 → 1907.32] and maybe they can grow
[1907.32 → 1909.30] into a data science position
[1909.30 → 1910.40] or maybe they can,
[1910.96 → 1912.68] there are a lot of different backgrounds
[1912.68 → 1913.46] that can go into
[1913.46 → 1914.84] your general assembly program
[1914.84 → 1915.60] and that sort of thing.
[1915.90 → 1916.38] I was wondering
[1916.38 → 1917.40] from your perspective
[1917.40 → 1918.54] to kind of help
[1918.54 → 1919.90] my understanding of that,
[1920.16 → 1921.68] are there certain backgrounds
[1921.68 → 1922.66] that you feel like
[1922.66 → 1925.22] lend themselves very well
[1925.22 → 1926.96] to quickly adapting
[1926.96 → 1928.38] to the data science world?
[1928.46 → 1930.10] I guess from my perspective,
[1930.10 → 1931.34] what I've told people
[1931.34 → 1932.24] in the past is,
[1932.62 → 1932.82] you know,
[1932.84 → 1933.56] if you're hiring someone
[1933.56 → 1934.10] in your company,
[1934.20 → 1935.32] maybe it would be best
[1935.32 → 1936.16] to train up,
[1936.36 → 1936.60] you know,
[1936.66 → 1937.70] the sort of engineers
[1937.70 → 1938.96] in your company
[1938.96 → 1940.64] to grow into data scientists
[1940.64 → 1942.60] because they at least know,
[1943.12 → 1943.96] like they're used to
[1943.96 → 1944.98] building things
[1944.98 → 1945.42] and,
[1945.42 → 1945.96] you know,
[1945.96 → 1947.30] thinking about product,
[1947.48 → 1948.62] thinking about testing,
[1948.80 → 1949.98] thinking about robustness
[1949.98 → 1951.10] and a lot of times
[1951.10 → 1952.34] I see people struggling
[1952.34 → 1953.34] with that bit
[1953.34 → 1954.58] in the data science world
[1954.58 → 1955.92] even after becoming
[1955.92 → 1956.70] a data scientist.
[1956.70 → 1957.10] So,
[1957.22 → 1958.32] I see those people
[1958.32 → 1959.36] as having an advantage
[1959.36 → 1960.24] from that perspective
[1960.24 → 1961.08] but I know that
[1961.08 → 1962.64] I've also known people
[1962.64 → 1963.96] with a philosophy background
[1963.96 → 1965.14] that have,
[1965.84 → 1966.08] you know,
[1966.12 → 1966.96] do amazing things
[1966.96 → 1967.94] and still have a level
[1967.94 → 1968.78] of practicality.
[1968.92 → 1969.04] So,
[1969.14 → 1970.12] do you have any insight
[1970.12 → 1970.46] on that?
[1970.46 → 1970.96] Yeah,
[1971.06 → 1971.84] I think you're
[1971.84 → 1972.76] absolutely right.
[1973.12 → 1973.56] Certainly,
[1973.80 → 1974.72] if somebody has
[1974.72 → 1975.76] a computer science
[1975.76 → 1976.26] background,
[1976.68 → 1977.60] I think all else
[1977.60 → 1978.22] held equal,
[1978.52 → 1979.24] they will tend
[1979.24 → 1980.64] to be better
[1980.64 → 1981.86] at adapting
[1981.86 → 1982.52] if they need
[1982.52 → 1983.58] to learn a new language
[1983.58 → 1985.00] or change the way
[1985.00 → 1986.02] that they're using Python
[1986.02 → 1986.94] to focus more
[1986.94 → 1988.04] on a data science thing.
[1988.42 → 1989.20] I think that if somebody
[1989.20 → 1991.22] comes from a math background,
[1991.62 → 1992.52] they will have
[1992.52 → 1993.32] an easier time
[1993.32 → 1994.24] with understanding
[1994.24 → 1994.86] some of those
[1994.86 → 1995.50] statistical
[1995.50 → 1997.12] and probabilistic concepts
[1997.12 → 1999.16] that lay the foundation
[1999.16 → 2000.06] for data science
[2000.06 → 2000.90] and are very important.
[2001.44 → 2002.40] At the same time,
[2002.44 → 2003.34] when you talk about,
[2003.48 → 2003.66] you know,
[2003.68 → 2004.46] the person who has
[2004.46 → 2005.60] a philosophy background
[2005.60 → 2006.72] who does well,
[2006.90 → 2007.96] we see that.
[2008.12 → 2009.04] Some of the strongest
[2009.04 → 2010.32] students we've had
[2010.32 → 2011.24] have come from
[2011.24 → 2012.22] very, very different
[2012.22 → 2012.82] backgrounds.
[2013.12 → 2013.60] Chemistry,
[2014.24 → 2014.70] journalism,
[2015.18 → 2015.62] English,
[2015.90 → 2016.22] law.
[2016.58 → 2017.48] It's certainly
[2017.48 → 2018.38] not limited
[2018.38 → 2019.28] to folks
[2019.28 → 2020.02] who just have
[2020.02 → 2020.86] a math background
[2020.86 → 2021.38] or just have
[2021.38 → 2022.36] a CS background
[2022.36 → 2023.30] or something like that.
[2023.54 → 2024.32] When it comes to
[2024.32 → 2024.90] thinking about
[2024.90 → 2025.76] within your company,
[2025.76 → 2027.90] I would agree
[2027.90 → 2028.34] with you
[2028.34 → 2029.70] that it can be
[2029.70 → 2030.44] better
[2030.44 → 2031.88] and obviously
[2031.88 → 2032.80] your circumstances
[2032.80 → 2033.98] are particular
[2033.98 → 2034.44] to you,
[2034.50 → 2035.20] but in many cases
[2035.20 → 2035.84] it can be better
[2035.84 → 2037.06] to train someone
[2037.06 → 2038.36] up internally
[2038.36 → 2039.92] and upskill them
[2039.92 → 2041.24] or deskill them
[2041.24 → 2041.96] depending on what
[2041.96 → 2042.76] it is you want to do.
[2043.06 → 2043.44] For example,
[2043.44 → 2044.06] you might take
[2044.06 → 2044.72] a programmer
[2044.72 → 2045.72] and you may say,
[2045.80 → 2045.98] look,
[2046.08 → 2046.90] you know Python this,
[2047.00 → 2047.08] well,
[2047.16 → 2048.36] we want to extend
[2048.36 → 2049.34] your knowledge of Python.
[2049.46 → 2050.34] So you might upskill them
[2050.34 → 2050.72] and give them
[2050.72 → 2051.70] that additional skill
[2051.70 → 2052.66] or you might take
[2052.66 → 2053.42] someone who knows
[2053.42 → 2054.44] the business really well.
[2054.54 → 2055.04] Maybe somebody
[2055.04 → 2056.18] is a financial analyst
[2056.18 → 2057.06] within your company,
[2057.22 → 2057.94] works in Excel
[2057.94 → 2058.62] most days,
[2058.76 → 2059.24] doesn't have
[2059.24 → 2060.14] a programming background,
[2060.28 → 2060.84] doesn't really know
[2060.84 → 2061.76] the math or the stats,
[2061.78 → 2062.18] but you say,
[2062.24 → 2062.60] you know what,
[2062.82 → 2063.60] you know the business
[2063.60 → 2064.46] or the organization
[2064.46 → 2065.08] well enough
[2065.08 → 2066.74] that you are
[2066.74 → 2067.66] well-suited
[2067.66 → 2069.04] to shift into this.
[2069.48 → 2071.22] So let's deskill you
[2071.22 → 2071.94] and give you
[2071.94 → 2072.76] a whole new set
[2072.76 → 2073.12] of skills
[2073.12 → 2073.68] that are fairly
[2073.68 → 2074.72] foreign to you,
[2074.92 → 2075.70] but given
[2075.70 → 2076.30] your knowledge
[2076.30 → 2076.92] of the business
[2076.92 → 2077.86] and given your knowledge
[2077.86 → 2078.84] for those problems
[2078.84 → 2079.50] that we're solving,
[2079.80 → 2080.00] again,
[2080.04 → 2080.54] it comes back
[2080.54 → 2081.00] to the fact
[2081.00 → 2081.82] that data science
[2081.82 → 2083.02] is really just us
[2083.02 → 2083.78] using data
[2083.78 → 2084.90] to solve problems.
[2085.34 → 2085.50] You know,
[2085.58 → 2086.58] it can be easier
[2086.58 → 2087.86] to perhaps upskill
[2087.86 → 2088.36] or deskill
[2088.36 → 2089.18] those individuals
[2089.18 → 2091.34] and from a strictly
[2091.34 → 2092.38] financial point of view,
[2092.38 → 2093.28] it tends to be
[2093.28 → 2094.54] more economical
[2094.54 → 2095.48] to do that.
[2095.72 → 2096.16] I don't know
[2096.16 → 2096.96] the statistics
[2096.96 → 2098.10] and I've seen numbers
[2098.10 → 2098.44] on them
[2098.44 → 2098.96] and I'm sure
[2098.96 → 2099.82] that we could find them
[2099.82 → 2100.64] and share them out
[2100.64 → 2101.06] afterward,
[2101.06 → 2102.56] but it is generally
[2102.56 → 2104.08] much more expensive
[2104.08 → 2105.82] to hire someone new
[2105.82 → 2107.06] as well as riskier
[2107.06 → 2108.34] to hire someone new
[2108.34 → 2109.16] from the outside
[2109.16 → 2109.92] for a role
[2109.92 → 2111.02] than to train
[2111.02 → 2112.52] someone up internally.
[2112.52 → 2113.94] And your mileage
[2113.94 → 2114.98] is going to vary there,
[2115.14 → 2115.90] but a lot of it
[2115.90 → 2116.44] is just the
[2116.60 → 2117.26] you take a risk
[2117.26 → 2118.04] when you hire someone
[2118.04 → 2118.84] from the outside
[2118.84 → 2119.86] where they don't know
[2119.86 → 2120.30] the business,
[2120.38 → 2120.72] they don't know
[2120.72 → 2121.16] the problems
[2121.16 → 2122.04] you're trying to solve.
[2122.26 → 2122.84] So bringing this
[2122.84 → 2123.28] back around
[2123.28 → 2124.50] to your original question
[2124.50 → 2125.54] when it comes to,
[2125.66 → 2125.78] you know,
[2125.84 → 2126.60] what are the backgrounds
[2126.60 → 2128.32] that tend to suit
[2128.32 → 2129.16] people the best
[2129.16 → 2129.64] for this?
[2130.00 → 2130.76] I think that
[2130.76 → 2131.70] the biggest traits
[2131.70 → 2132.60] that lend themselves
[2132.60 → 2133.42] to people learning
[2133.42 → 2134.00] data science
[2134.00 → 2134.60] if they do need
[2134.60 → 2135.20] to upskill
[2135.20 → 2135.76] or deskill
[2135.76 → 2136.64] or change direction
[2136.64 → 2137.88] tends to be grit
[2137.88 → 2140.40] and tends to be logic.
[2140.88 → 2141.88] So people being able
[2141.88 → 2142.24] to,
[2142.38 → 2142.56] I mean,
[2142.60 → 2143.30] when you start out
[2143.30 → 2143.84] programming,
[2144.02 → 2144.58] I know this was
[2144.58 → 2145.24] the case for me.
[2145.34 → 2146.22] I imagine this may be
[2146.22 → 2147.10] the case for you as well.
[2147.52 → 2148.34] Programming for me
[2148.34 → 2149.56] was really hard.
[2150.28 → 2150.80] It was something
[2150.80 → 2151.34] where it took
[2151.34 → 2152.32] like three times
[2152.32 → 2152.90] of me learning
[2152.90 → 2153.58] to program
[2153.58 → 2154.98] for that to really click.
[2155.34 → 2155.86] And I'm not sure
[2155.86 → 2156.50] what it was.
[2156.56 → 2156.96] I'm not sure
[2156.96 → 2158.00] what that mental block
[2158.00 → 2158.86] was for me,
[2159.08 → 2160.32] but it was something
[2160.32 → 2161.66] that was really challenging.
[2162.28 → 2163.34] Whenever you start programming,
[2163.46 → 2164.58] especially in a new language,
[2164.58 → 2165.10] you're going to get
[2165.10 → 2166.78] a bunch of unfamiliar errors
[2166.78 → 2167.42] and warnings
[2167.42 → 2168.02] and exceptions
[2168.02 → 2168.78] that tell you,
[2169.06 → 2169.14] hey,
[2169.16 → 2170.58] you're doing these things wrong.
[2170.58 → 2171.86] And it can be very easy
[2171.86 → 2173.28] to just throw your hands up
[2173.28 → 2173.90] and, you know,
[2173.90 → 2174.80] say, screw it.
[2174.84 → 2175.34] I'm done.
[2175.46 → 2175.94] I'm, you know,
[2175.94 → 2177.22] this is not for me.
[2177.34 → 2178.68] But the more you realize
[2178.68 → 2179.42] that that kind of
[2179.42 → 2180.68] is a common experience
[2180.68 → 2181.26] for everybody
[2181.26 → 2182.78] that even experienced
[2182.78 → 2183.26] programmers
[2183.26 → 2184.58] are looking things up
[2184.58 → 2185.08] on Google,
[2185.48 → 2186.82] checking out Stack Overflow
[2186.82 → 2187.92] to see other people
[2187.92 → 2188.50] who have had
[2188.50 → 2189.50] these problems before,
[2189.66 → 2190.52] you realize
[2190.52 → 2191.40] that you are meant
[2191.40 → 2191.98] to be there.
[2192.14 → 2193.10] So just that willingness
[2193.10 → 2193.72] and that grit
[2193.72 → 2195.00] to try and try
[2195.00 → 2195.82] and try again,
[2195.94 → 2196.50] even when it's
[2196.50 → 2197.24] initially tough,
[2197.38 → 2198.02] that logic,
[2198.02 → 2198.28] I mean,
[2198.34 → 2199.34] logic is an integral
[2199.34 → 2200.54] part of the stats
[2200.54 → 2201.42] and the programming
[2201.42 → 2202.14] needed in order
[2202.14 → 2203.42] to be a data scientist.
[2203.94 → 2204.26] So Matt,
[2204.32 → 2205.46] we've kind of focused
[2205.46 → 2206.42] very heavily
[2206.42 → 2207.32] on kind of
[2207.32 → 2208.02] the experience
[2208.02 → 2208.72] of practitioners
[2208.72 → 2209.78] as they're learning
[2209.78 → 2210.96] and going through education
[2210.96 → 2211.74] and seeking out
[2211.74 → 2212.64] what fits them.
[2212.98 → 2214.00] I got another question
[2214.00 → 2214.42] for you
[2214.42 → 2215.22] that is kind of
[2215.22 → 2216.08] adjacent to that
[2216.08 → 2216.54] and that is
[2216.54 → 2218.32] we have lots
[2218.32 → 2219.52] of managers
[2219.52 → 2220.50] and executives
[2220.50 → 2221.12] out there
[2221.12 → 2222.04] in organizations
[2222.04 → 2223.50] that are not
[2223.50 → 2224.58] practitioners themselves.
[2224.82 → 2225.28] They're not going
[2225.28 → 2225.62] to be doing
[2225.62 → 2226.32] the data science
[2226.32 → 2226.76] themselves,
[2226.96 → 2228.44] but they're
[2228.44 → 2229.08] in a position
[2229.08 → 2229.72] where they have
[2229.72 → 2230.16] to make
[2230.16 → 2232.08] lots of decisions
[2232.08 → 2232.68] and they have
[2232.68 → 2234.24] to decide things
[2234.24 → 2234.86] for budgeting
[2234.86 → 2235.90] and for strategic
[2235.90 → 2236.82] path forward
[2236.82 → 2237.68] for the organization.
[2238.18 → 2240.00] For those managers
[2240.00 → 2240.90] and executives
[2240.90 → 2241.80] that are in that
[2241.80 → 2242.76] position of having
[2242.76 → 2243.80] to make those choices
[2243.80 → 2245.04] without the fundamentals
[2245.04 → 2245.98] that the practitioner
[2245.98 → 2246.38] has,
[2246.56 → 2247.24] what are the tools,
[2247.36 → 2248.04] what are the skills
[2248.04 → 2249.44] that those individuals
[2249.44 → 2250.96] need to be able
[2250.96 → 2252.02] to do their job
[2252.02 → 2252.50] effectively
[2252.50 → 2253.62] in this day and age?
[2254.60 → 2255.24] I think that
[2255.24 → 2256.28] it's a perfect point.
[2256.32 → 2257.46] And something that,
[2257.46 → 2257.96] again,
[2258.08 → 2259.32] GA has been working on
[2259.32 → 2260.12] because if you think
[2260.12 → 2261.06] about the skills gap,
[2261.18 → 2262.46] the gap between
[2262.46 → 2264.18] what skills people have
[2264.18 → 2264.74] and the skills
[2264.74 → 2265.74] that their organization
[2265.74 → 2266.86] requires of them,
[2267.22 → 2268.04] that skills gap
[2268.04 → 2269.58] is quite large
[2269.58 → 2270.30] in some cases
[2270.30 → 2271.08] and it's going to differ
[2271.08 → 2272.26] from person to person.
[2272.54 → 2272.70] You know,
[2272.76 → 2273.66] what are these skills
[2273.66 → 2274.54] that somebody needs
[2274.54 → 2275.12] in this role
[2275.12 → 2275.54] versus,
[2275.96 → 2276.08] you know,
[2276.10 → 2276.88] where they are now?
[2277.14 → 2277.72] And that's true
[2277.72 → 2278.84] of executives as well.
[2279.32 → 2279.70] And so,
[2279.78 → 2280.66] when it comes to
[2280.66 → 2281.38] minimizing
[2281.38 → 2282.40] or erasing
[2282.40 → 2283.46] that skills gap
[2283.46 → 2284.12] and figuring out
[2284.12 → 2284.76] what are the skills
[2284.76 → 2285.92] that executives need,
[2285.92 → 2287.12] in my opinion,
[2287.12 → 2287.98] so much of it
[2287.98 → 2288.96] is rooted in
[2288.96 → 2291.08] understanding the
[2291.46 → 2292.50] you certainly don't need
[2292.50 → 2293.64] to be an expert programmer,
[2293.78 → 2294.72] you certainly don't need
[2294.72 → 2297.10] to be a master statistician
[2297.10 → 2298.08] or something like that.
[2298.18 → 2298.70] Instead,
[2298.92 → 2299.48] what I think
[2299.48 → 2300.40] is important
[2300.40 → 2302.20] is people
[2302.20 → 2303.48] need to understand
[2303.48 → 2304.28] the
[2304.44 → 2305.14] I think,
[2305.20 → 2305.82] the provenance
[2305.82 → 2306.62] or the source
[2306.62 → 2307.70] of the data.
[2307.94 → 2309.42] They need to understand
[2309.42 → 2310.26] the biases
[2310.26 → 2311.64] that may go
[2311.64 → 2312.80] into that data.
[2312.80 → 2313.98] and then they need
[2313.98 → 2314.54] to understand
[2314.54 → 2315.26] how that data
[2315.26 → 2316.00] is being used
[2316.00 → 2317.66] to solve that problem.
[2317.96 → 2318.12] So,
[2318.30 → 2319.30] a perfect example,
[2319.82 → 2321.48] if we were to,
[2321.60 → 2322.38] let's say that we wanted
[2322.38 → 2323.00] to understand
[2323.00 → 2323.90] what our customers
[2323.90 → 2324.92] thought of our product.
[2325.32 → 2326.54] There are a number
[2326.54 → 2327.28] of different sources
[2327.28 → 2328.14] that we could check out
[2328.14 → 2328.94] to gather data,
[2329.06 → 2329.80] but let's say somebody,
[2330.06 → 2330.80] a data scientist
[2330.80 → 2331.36] under you
[2331.36 → 2332.28] does an analysis
[2332.28 → 2333.80] and they do this analysis,
[2334.00 → 2335.54] they share their results
[2335.54 → 2335.88] with you
[2335.88 → 2336.42] and it looks like
[2336.42 → 2337.28] people are really
[2337.28 → 2338.66] dissatisfied with you
[2338.66 → 2339.56] and with your company.
[2339.56 → 2342.20] and the executive
[2342.20 → 2342.82] knows to ask,
[2342.92 → 2343.06] okay,
[2343.12 → 2343.36] you know,
[2343.42 → 2344.00] where did we get
[2344.00 → 2344.90] this data from?
[2345.34 → 2346.84] And the person responds,
[2347.04 → 2348.10] we used the data
[2348.10 → 2348.80] from Yelp
[2348.80 → 2349.64] that's available
[2349.64 → 2350.66] about our business.
[2351.44 → 2351.88] Well,
[2352.04 → 2352.78] as a person,
[2352.92 → 2353.70] we recognize
[2353.70 → 2355.20] that people who go
[2355.20 → 2356.56] and they post on Yelp,
[2356.66 → 2357.60] that is not going to be
[2357.60 → 2358.94] a random sample of people.
[2359.16 → 2360.64] People generally post on Yelp
[2360.64 → 2362.08] in one of two situations.
[2362.26 → 2362.50] One,
[2362.78 → 2363.42] they're just kind of
[2363.42 → 2364.78] a constant Helper,
[2364.96 → 2365.42] so to speak.
[2365.52 → 2366.76] They're going to put ratings up
[2366.76 → 2368.16] for everywhere they go.
[2368.58 → 2369.40] Or the other time,
[2369.56 → 2370.30] people are generally
[2370.30 → 2371.24] only going to be driven
[2371.24 → 2371.84] to Yelp
[2371.84 → 2373.04] when they have
[2373.04 → 2374.14] a terrible experience
[2374.14 → 2374.76] and they kind of need
[2374.76 → 2375.80] the world to know about it.
[2376.12 → 2377.64] I'm painting with a very,
[2377.88 → 2379.14] very broad brush here,
[2379.26 → 2380.76] so all sorts of approximations
[2380.76 → 2381.20] are in there.
[2381.48 → 2382.34] But recognizing
[2382.34 → 2384.16] that potential for bias
[2384.16 → 2385.18] is, I think,
[2385.26 → 2386.92] huge in understanding
[2386.92 → 2388.52] how you can make decisions.
[2388.88 → 2389.48] So when it comes
[2389.48 → 2390.26] to the skills
[2390.26 → 2391.46] that an executive can have,
[2391.50 → 2392.04] I think that
[2392.04 → 2393.48] understanding
[2393.48 → 2394.84] what are the right questions
[2394.84 → 2395.52] to ask,
[2395.76 → 2396.90] try and poke holes
[2396.90 → 2397.88] in the analysis.
[2398.26 → 2398.94] I think that,
[2398.94 → 2399.44] certainly,
[2399.62 → 2400.30] if an executive
[2400.30 → 2401.34] knows about something
[2401.34 → 2402.40] called overfitting
[2402.40 → 2403.50] versus underfitting
[2403.50 → 2404.80] and knows how to assess
[2404.80 → 2405.16] for that,
[2405.42 → 2406.36] that is great.
[2406.74 → 2407.08] However,
[2407.20 → 2408.70] I think that in many cases,
[2408.88 → 2410.26] being able to understand
[2410.26 → 2410.98] the decision
[2410.98 → 2411.76] that's being made
[2411.76 → 2412.86] and just ask some questions
[2412.86 → 2413.10] about,
[2413.22 → 2413.34] okay,
[2413.44 → 2414.34] what's the source
[2414.34 → 2414.90] of the data?
[2415.28 → 2415.94] What are the steps
[2415.94 → 2416.68] you took here?
[2417.10 → 2418.28] When you dropped data
[2418.28 → 2419.84] or when you dropped observations,
[2420.34 → 2421.64] why did you choose this?
[2421.96 → 2423.52] What if you had done it differently?
[2423.68 → 2424.52] How does that change
[2424.52 → 2425.04] your results?
[2425.04 → 2426.36] I think just asking
[2426.36 → 2427.26] good questions
[2427.26 → 2428.22] and being generally
[2428.22 → 2429.58] data literate
[2429.58 → 2430.28] and being aware
[2430.28 → 2430.98] of the biases
[2430.98 → 2432.60] that are kind of around us,
[2432.76 → 2433.56] I think that probably
[2433.56 → 2434.62] puts them in a position
[2434.62 → 2435.94] to be successful
[2435.94 → 2436.96] as opposed to saying,
[2437.42 → 2437.96] as an executive,
[2438.14 → 2439.10] you should know Python
[2439.10 → 2440.06] because in reality,
[2440.54 → 2442.16] the chief data officer
[2442.16 → 2443.66] or the chief financial officer
[2443.66 → 2444.04] being,
[2444.32 → 2444.58] you know,
[2444.60 → 2445.28] making decisions
[2445.28 → 2446.14] based on data
[2446.14 → 2447.20] probably doesn't have
[2447.20 → 2447.84] to spend a ton
[2447.84 → 2448.64] of their day
[2448.64 → 2449.44] in Python
[2449.44 → 2450.36] depending on the size
[2450.36 → 2451.28] of your organization.
[2451.28 → 2452.52] So I'm curious,
[2452.78 → 2453.42] this is related,
[2453.56 → 2453.88] I guess,
[2454.00 → 2455.46] to management
[2455.46 → 2456.58] in the sense of hiring,
[2456.80 → 2458.16] but we've talked about
[2458.16 → 2458.96] how there's all
[2458.96 → 2460.02] of these different backgrounds
[2460.02 → 2461.00] that people can come from
[2461.00 → 2462.26] and all of these specializations
[2462.26 → 2463.20] in data science
[2463.20 → 2464.24] and there certainly are
[2464.24 → 2466.72] many and varied specializations,
[2466.98 → 2467.66] but I was wondering
[2467.66 → 2470.40] based on your recent experience
[2470.40 → 2471.76] with General Assembly
[2471.76 → 2472.64] and maybe things
[2472.64 → 2473.78] that you're just monitoring
[2473.78 → 2474.94] in the industry,
[2475.48 → 2476.96] what are the sort of
[2476.96 → 2479.12] top specializations
[2479.12 → 2479.96] or skills
[2479.96 → 2481.70] that are like
[2481.70 → 2482.90] people are hiring
[2482.90 → 2483.64] for immediately
[2483.64 → 2484.82] and very rapidly?
[2485.06 → 2485.38] Is that,
[2485.50 → 2485.98] for example,
[2486.10 → 2487.60] is that NLP
[2487.60 → 2488.90] or is that like
[2488.90 → 2490.78] quantitative finance
[2490.78 → 2491.58] in that industry?
[2491.66 → 2492.58] Maybe it's an industry
[2492.58 → 2493.96] or maybe it's a skill.
[2494.14 → 2495.48] Are there any standouts
[2495.48 → 2496.10] that you've seen?
[2497.10 → 2497.36] Honestly,
[2497.46 → 2499.00] the most common thing
[2499.00 → 2500.40] that I have observed
[2500.40 → 2502.34] in terms of data scientist roles
[2502.34 → 2503.34] is SQL.
[2503.72 → 2504.20] Interesting.
[2504.76 → 2506.28] Knowing how to get data
[2506.28 → 2507.84] out of databases
[2507.84 → 2509.68] I think is something
[2509.68 → 2511.96] that is very highly sought
[2511.96 → 2513.50] after in data science roles
[2513.50 → 2514.94] and it's interesting
[2514.94 → 2516.22] because we were talking earlier
[2516.22 → 2517.78] about kind of the fractured nature
[2517.78 → 2519.48] of the data science industry
[2519.48 → 2521.24] and all the different things
[2521.24 → 2522.16] people are looking for
[2522.16 → 2522.84] in a data science.
[2522.92 → 2523.46] You're really looking
[2523.46 → 2524.16] for a unicorn.
[2524.64 → 2524.74] You know,
[2524.78 → 2526.04] you want someone with,
[2526.14 → 2526.52] you know,
[2526.54 → 2528.56] a bunch of interpersonal skills
[2528.56 → 2529.76] and programming skills
[2529.76 → 2530.54] and stats
[2530.54 → 2531.68] and subject expertise
[2531.68 → 2532.48] and all of this stuff.
[2532.68 → 2534.58] The closely related title
[2534.58 → 2535.68] data engineer
[2535.68 → 2536.82] dealing with more
[2536.82 → 2537.56] the back end
[2537.56 → 2538.42] and figuring out,
[2538.64 → 2538.72] okay,
[2538.76 → 2540.56] how do we take information,
[2541.00 → 2541.12] you know,
[2541.14 → 2542.40] how do we structure databases
[2542.40 → 2543.18] and all of that?
[2543.40 → 2544.82] There's a bit more
[2544.82 → 2546.04] of a melding between them
[2546.04 → 2546.94] because now people
[2546.94 → 2548.00] want data scientists
[2548.00 → 2549.40] to also be
[2549.40 → 2551.06] at least moderately
[2551.06 → 2552.38] well-versed in SQL.
[2552.70 → 2553.56] Different companies
[2553.56 → 2554.64] and different organizations
[2554.64 → 2555.88] will have different perspectives,
[2555.88 → 2557.46] but I think that SQL
[2557.46 → 2559.62] is an important thing
[2559.62 → 2560.88] for everybody to learn.
[2560.88 → 2562.24] I also think
[2562.24 → 2563.38] that in addition to that
[2563.38 → 2565.18] with thinking about SQL,
[2565.18 → 2566.20] for my money,
[2566.32 → 2567.52] it's probably an easier
[2567.52 → 2568.28] skill to learn
[2568.28 → 2569.50] than like the
[2569.72 → 2570.42] than the Python
[2570.42 → 2571.18] or, you know,
[2571.18 → 2572.10] some of the other stuff
[2572.10 → 2572.78] that's out there.
[2572.78 → 2574.16] But that is,
[2574.52 → 2575.58] that almost feels more
[2575.58 → 2577.14] like table stakes
[2577.14 → 2578.04] to know SQL
[2578.04 → 2579.58] than a differentiator
[2579.58 → 2581.04] where to put a bow
[2581.04 → 2581.50] on this.
[2582.16 → 2583.60] People knowing SQL
[2583.60 → 2584.64] is kind of a
[2584.88 → 2586.04] people need that
[2586.04 → 2587.10] in order to be considered
[2587.10 → 2587.74] for the role.
[2587.88 → 2589.68] It's not like knowing SQL
[2589.68 → 2591.78] would immediately qualify
[2591.78 → 2592.96] someone for that role
[2592.96 → 2593.76] or set them apart,
[2593.76 → 2594.64] if that makes sense.
[2594.64 → 2595.54] Table stakes
[2595.54 → 2596.20] is a good way
[2596.20 → 2597.06] when you said that,
[2597.12 → 2597.86] I would agree.
[2598.14 → 2599.68] It's kind of a universal thing
[2599.68 → 2600.50] that almost everyone
[2600.50 → 2601.08] needs to know.
[2601.42 → 2601.62] Yeah.
[2601.78 → 2601.98] Yeah.
[2602.00 → 2602.98] And I think that,
[2603.30 → 2603.74] I don't know,
[2603.80 → 2605.12] I would see as a differentiator
[2605.12 → 2606.46] if I'm thinking about people too,
[2606.56 → 2606.80] like,
[2607.32 → 2607.44] well,
[2607.44 → 2608.48] certainly a lot of people
[2608.48 → 2609.80] that can know SQL
[2609.80 → 2610.88] and there's a lot of people
[2610.88 → 2612.32] that can learn
[2612.32 → 2613.80] and know like the data science
[2613.80 → 2614.96] tooling in,
[2614.96 → 2615.70] in Python
[2615.70 → 2616.32] or,
[2616.70 → 2616.82] you know,
[2616.88 → 2617.72] whether it be TensorFlow
[2617.72 → 2618.42] or,
[2618.76 → 2618.96] you know,
[2618.96 → 2620.00] just Pandas
[2620.00 → 2620.64] and scikit-learn
[2620.64 → 2621.00] or whatever.
[2621.30 → 2622.00] I think it's a very
[2622.00 → 2623.18] unique differentiator
[2623.18 → 2624.70] if you're able to connect
[2624.70 → 2625.76] the SQL world
[2625.76 → 2626.98] and the database world
[2626.98 → 2628.16] with the other world,
[2628.22 → 2628.42] right?
[2628.44 → 2629.96] If you're able to drive models
[2629.96 → 2631.62] out of SQL queries
[2631.62 → 2632.10] in a
[2632.10 → 2633.40] in a sort of reasonable,
[2633.80 → 2634.52] efficient way
[2634.52 → 2635.68] and you're able to connect,
[2635.74 → 2636.08] you know,
[2636.48 → 2637.34] Python services
[2637.34 → 2638.44] that are running
[2638.44 → 2639.82] and doing something fancy
[2639.82 → 2640.86] with a database,
[2640.86 → 2642.46] I think that sort of thing
[2642.46 → 2642.84] is a
[2642.84 → 2643.98] is a real standout
[2643.98 → 2644.76] from my perspective.
[2644.76 → 2645.90] So,
[2646.24 → 2647.20] I guess as we're getting
[2647.20 → 2647.76] toward the end,
[2647.82 → 2648.60] I'm kind of curious,
[2648.80 → 2649.84] what are the things
[2649.84 → 2650.82] that you're excited about,
[2650.94 → 2651.10] Matt,
[2651.16 → 2652.08] in terms of like the
[2652.14 → 2653.80] the topics and problems
[2653.80 → 2654.12] that,
[2654.24 → 2654.96] that we're finding
[2654.96 → 2656.02] in data science now
[2656.02 → 2656.34] and,
[2656.46 → 2656.58] you know,
[2656.60 → 2657.28] what are the things
[2657.28 → 2658.26] that are really making you
[2658.26 → 2659.52] look at it on a day-to-day basis
[2659.52 → 2659.86] and go,
[2659.98 → 2660.14] hmm,
[2660.20 → 2661.74] this is really exciting me
[2661.74 → 2662.86] and where do you think
[2662.86 → 2663.90] this is going to go
[2663.90 → 2664.88] over the next few years?
[2665.02 → 2666.84] What kinds of interesting topics
[2666.84 → 2668.28] and exciting problems
[2668.28 → 2669.48] do you think we'll be contending
[2669.48 → 2670.46] with over the next few years?
[2671.00 → 2673.04] I think that the biggest problem
[2673.04 → 2674.28] that we'll be grappling with
[2674.28 → 2675.94] kind of as a society,
[2676.10 → 2677.08] for lack of a better word,
[2677.42 → 2679.88] is the idea of deep fakes.
[2680.36 → 2681.94] I think that the
[2682.02 → 2683.76] the methods that are out there
[2683.76 → 2685.58] have become very powerful
[2685.58 → 2687.26] and I think that
[2687.26 → 2689.30] what we will see probably
[2689.30 → 2690.94] in the next five years or so,
[2691.24 → 2692.18] maybe sooner,
[2692.54 → 2694.08] just given the political landscape
[2694.08 → 2696.26] is understanding how,
[2696.70 → 2696.96] you know,
[2697.00 → 2698.88] we are able to create images
[2698.88 → 2700.86] that obviously are,
[2701.08 → 2701.64] they're fake,
[2701.72 → 2702.56] they're not real,
[2702.98 → 2704.12] but they look,
[2704.28 → 2704.82] really,
[2704.96 → 2705.64] really real.
[2705.94 → 2706.74] I think that,
[2706.82 → 2706.94] hey,
[2706.94 → 2708.34] we can do the same with video.
[2708.70 → 2710.18] We can do similar things
[2710.18 → 2710.72] with audio.
[2710.96 → 2712.18] It's not just,
[2712.34 → 2712.54] you know,
[2712.60 → 2713.56] still images.
[2713.76 → 2713.94] It's,
[2714.18 → 2714.30] you know,
[2714.32 → 2715.04] we're able to,
[2715.10 → 2716.06] to create audio
[2716.06 → 2716.60] that literally,
[2716.94 → 2717.12] you know,
[2717.16 → 2717.80] audio and video
[2717.80 → 2718.24] and all of that
[2718.24 → 2719.82] that literally doesn't exist
[2719.82 → 2720.72] but can be used
[2720.72 → 2721.38] to make a point.
[2721.38 → 2723.12] I don't mean to sound the alarm
[2723.12 → 2724.64] but I do think that
[2724.64 → 2725.30] that's going to be
[2725.30 → 2726.94] a really important thing
[2726.94 → 2729.36] that we need to reckon with
[2729.36 → 2731.00] as we see how the tools
[2731.00 → 2731.58] of our field
[2731.58 → 2732.62] can be used
[2732.62 → 2734.10] in nefarious ways
[2734.10 → 2735.16] and there are a lot of ways
[2735.16 → 2737.00] that we're more aware of that
[2737.00 → 2738.06] but I think that's only going
[2738.06 → 2739.32] to become more and more
[2739.32 → 2740.90] and more of our conversation.
[2740.90 → 2742.20] It is not enough
[2742.20 → 2743.26] to do kind of like
[2743.26 → 2745.04] a drive-by nod
[2745.04 → 2746.42] to ethical behaviour
[2746.42 → 2747.20] and say,
[2747.32 → 2747.54] hey,
[2747.86 → 2748.16] you know,
[2748.16 → 2749.10] in order to be
[2749.10 → 2750.38] an ethical data scientist
[2750.38 → 2752.16] or an ethical consumer of data,
[2752.46 → 2753.10] this is something
[2753.10 → 2754.16] that you should be aware of
[2754.16 → 2755.08] and then kind of move on
[2755.08 → 2755.68] and forget it
[2755.68 → 2756.54] but instead I think
[2756.54 → 2757.98] we will have to apply
[2757.98 → 2758.98] when we're teaching
[2758.98 → 2759.56] these methods
[2759.56 → 2760.22] and when we're learning
[2760.22 → 2761.06] about these things
[2761.06 → 2761.76] and when we're putting them
[2761.76 → 2762.34] into practice,
[2762.56 → 2763.28] I think we're going to have
[2763.28 → 2764.90] to apply an ethical lens
[2764.90 → 2765.74] to everything
[2765.74 → 2766.88] and I think the best
[2766.88 → 2767.64] data scientists
[2767.64 → 2768.56] already are
[2768.56 → 2769.42] but when it comes
[2769.42 → 2770.48] to the developments
[2770.48 → 2771.08] in the field
[2771.08 → 2772.36] that I'm most,
[2772.46 → 2772.96] I think,
[2773.04 → 2773.86] excited about
[2773.86 → 2774.94] but also most,
[2775.08 → 2775.56] I think,
[2775.60 → 2776.26] are most important
[2776.26 → 2777.70] is that better understanding
[2777.70 → 2778.50] of what are
[2778.50 → 2779.96] our ethical obligations
[2779.96 → 2781.26] as data scientists,
[2781.74 → 2782.82] what are our
[2782.82 → 2784.28] organizational role
[2784.28 → 2785.96] like if I'm a data scientist
[2785.96 → 2786.90] professional,
[2787.16 → 2788.04] what are those obligations
[2788.04 → 2788.62] that I have
[2788.62 → 2789.44] as somebody
[2789.44 → 2790.70] who knows data scientists
[2790.70 → 2791.68] even if I'm not
[2791.68 → 2793.06] working at the moment
[2793.06 → 2793.66] but I'm like
[2793.66 → 2794.92] at home with family
[2794.92 → 2795.98] and stuff comes up
[2795.98 → 2796.58] or you know,
[2796.64 → 2797.70] you see something on TV
[2797.70 → 2798.72] like what are those
[2798.72 → 2799.56] ethical obligations
[2799.56 → 2800.84] to maybe call out
[2800.84 → 2801.42] those biases
[2801.42 → 2802.42] that I were talking about
[2802.42 → 2803.06] that executives
[2803.06 → 2804.06] should be aware of
[2804.06 → 2805.74] or to recognize things
[2805.74 → 2807.20] that aren't exactly right.
[2807.20 → 2808.12] So that's probably
[2808.12 → 2808.80] for my money
[2808.80 → 2810.30] the most important thing
[2810.30 → 2811.22] moving forward
[2811.22 → 2812.22] and understanding
[2812.22 → 2813.28] how we can be
[2813.28 → 2814.18] good stewards
[2814.18 → 2814.68] of the data
[2814.68 → 2815.34] that we collect,
[2815.66 → 2816.52] how we can be
[2816.52 → 2817.94] good and ethical
[2817.94 → 2818.74] practitioners
[2818.74 → 2819.94] of data science
[2819.94 → 2820.80] and making sure
[2820.80 → 2821.98] that we are developing
[2821.98 → 2823.04] things for,
[2823.28 → 2824.28] I will broadly
[2824.28 → 2825.00] wave my hands
[2825.00 → 2825.38] and say,
[2825.56 → 2826.60] for the good
[2826.60 → 2827.46] of all of us
[2827.46 → 2828.60] as opposed to the bad.
[2828.60 → 2829.66] Well, I think
[2829.66 → 2830.40] that's a really
[2830.40 → 2831.12] good place
[2831.12 → 2832.70] to end the conversation
[2832.70 → 2833.74] and we have
[2833.74 → 2834.40] another episode
[2834.40 → 2835.64] that covered
[2835.64 → 2836.78] deep fakes
[2836.78 → 2838.28] in some detail
[2838.28 → 2839.28] and we'll for sure
[2839.28 → 2840.10] link that in our
[2840.10 → 2840.58] show notes
[2840.58 → 2841.36] so check that out
[2841.36 → 2841.96] but definitely
[2841.96 → 2842.70] check out what
[2842.70 → 2843.34] General Assembly
[2843.34 → 2844.04] is doing
[2844.04 → 2844.92] in terms of
[2844.92 → 2845.60] their data science
[2845.60 → 2846.10] education
[2846.10 → 2846.84] and we really
[2846.84 → 2847.58] appreciate you
[2847.58 → 2848.22] joining us
[2848.22 → 2849.00] on the podcast,
[2849.16 → 2849.30] Matt,
[2849.40 → 2849.98] and sharing
[2849.98 → 2850.74] your perspective
[2850.74 → 2851.82] after so much
[2851.82 → 2852.44] experience
[2852.44 → 2853.82] in data science
[2853.82 → 2854.64] and in data science
[2854.64 → 2855.14] education.
[2855.30 → 2856.02] Really appreciate it.
[2856.02 → 2857.52] Yeah, absolutely.
[2857.70 → 2858.34] Thank you so much
[2858.34 → 2858.96] for having me.
[2862.58 → 2863.70] Thank you for listening
[2863.70 → 2864.50] to Practical AI.
[2865.00 → 2865.68] If you're not
[2865.68 → 2867.30] following Practical AI FM
[2867.30 → 2867.80] on Twitter,
[2868.02 → 2868.66] you're missing out
[2868.66 → 2869.76] on clips and highlights
[2869.76 → 2870.68] from past episodes,
[2871.02 → 2872.04] links and repos
[2872.04 → 2873.08] from around the AI
[2873.08 → 2873.86] and data science
[2873.86 → 2874.90] community and more.
[2875.34 → 2875.86] Follow us,
[2876.00 → 2877.24] Practical AI FM.
[2877.44 → 2878.18] You won't regret it.
[2878.60 → 2879.38] Practical AI is hosted
[2879.38 → 2880.44] by Daniel Whiten ack
[2880.44 → 2881.26] and Chris Benson.
[2881.54 → 2882.28] It's produced by me,
[2882.46 → 2883.02] Jared Santo
[2883.02 → 2884.32] and our music is brought
[2884.32 → 2885.30] to you by the Beat Freak,
[2885.44 → 2885.80] Break master,
[2885.80 → 2886.22] Cylinder.
[2886.72 → 2887.88] We have awesome sponsors.
[2888.04 → 2888.62] Support them.
[2888.78 → 2889.56] They support the show.
[2890.04 → 2891.20] Special thanks to Vastly,
[2891.48 → 2891.90] Linde,
[2892.10 → 2892.70] and Rollbar
[2892.70 → 2893.50] for helping us
[2893.50 → 2894.20] do what we do.
[2894.56 → 2895.48] If you aren't receiving
[2895.48 → 2896.24] Change Log Weekly
[2896.24 → 2896.94] every Sunday,
[2897.08 → 2897.92] you are missing out.
[2898.26 → 2899.26] It's our take on
[2899.26 → 2900.00] this week in the world
[2900.00 → 2900.48] of software,
[2900.82 → 2901.48] what's interesting
[2901.48 → 2902.26] and why.
[2902.62 → 2903.20] Head to
[2903.20 → 2904.24] changelog.com
[2904.24 → 2904.86] slash weekly
[2904.86 → 2905.66] to subscribe.
[2906.20 → 2906.96] Get it for the price
[2906.96 → 2907.74] of a free cheeseburger.
[2908.50 → 2909.42] Thanks again for listening.
[2909.74 → 2910.74] We'll talk to you next week.
[2910.74 → 2910.76] We'll talk to you next week.
[2910.76 → 2912.74] We'll talk to you next week.
[2912.74 → 2914.74] We'll talk to you next week.
[2914.74 → 2915.24] We'll talk to you next week.
[2916.20 → 2916.94] We'll talk to you next week.
[2916.94 → 2918.78] Bye.
[2920.06 → 2921.24] We'll talk to you next week.
[2921.24 → 2921.94] Bye.
[2921.94 → 2922.12] Bye.
[2922.64 → 2922.80] Bye.
[2923.20 → 2925.16] Bye.
[2925.16 → 2925.24] Bye.
[2925.32 → 2925.36] Bye.
[2925.40 → 2925.68] Bye.
[2925.76 → 2926.18] Bye.
[2927.66 → 2927.88] Bye.
[2927.88 → 2928.00] Bye.
[2928.12 → 2928.20] Bye.
[2928.46 → 2936.08] Bye-bye.
[2936.14 → 2936.78] Bye.
[2936.80 → 2937.16] K fell.
[2937.36 → 2937.82] Bye.
[2938.00 → 2938.32] Bye.
[2938.56 → 2939.80] Bye.
[2939.86 → 2940.50] Bye.
