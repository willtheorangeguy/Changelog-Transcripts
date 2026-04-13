[0.00 → 11.34] I'm going to say something slightly controversial, I think, and that is that I think of AI development as a component of software development, which a lot of data scientists will say, no, it's not.
[11.42 → 11.96] No, it's not.
[11.96 → 21.78] But when I'm looking at it in production, and I'm looking at us actually managing that, I see it in that larger context because all of those other activities are happening around it.
[24.00 → 26.90] Bandwidth for Change Log is provided by Vastly.
[27.22 → 29.18] Learn more at Fastly.com.
[29.18 → 32.48] We move fast and fix things here at Change Log because of Rollbar.
[32.62 → 34.28] Check them out at Rollbar.com.
[34.54 → 36.18] And we're hosted on Linde cloud servers.
[37.06 → 39.04] Head to linode.com slash Change Log.
[41.76 → 44.36] This episode is brought to you by DigitalOcean.
[44.68 → 49.46] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[49.46 → 61.14] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[61.38 → 66.80] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[67.20 → 70.66] Head to do.co slash Change Log to get started with a $100 credit.
[70.66 → 73.12] Again, do.co slash Change Log.
[73.12 → 89.84] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[90.14 → 94.24] This is where conversations around AI, machine learning, and data science happen.
[94.24 → 100.60] Join the community and Slack with us around various topics of the show at ChangeLog.com slash community and follow us on Twitter.
[100.74 → 102.40] We're at Practical AI FM.
[108.66 → 114.16] Welcome to another fully connected episode of the Practical AI podcast.
[114.68 → 120.30] This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[120.30 → 129.60] We'll take some time to discuss some of the latest AI news, and we'll dig into a few learning resources to help you level up your machine learning game.
[130.12 → 131.12] I'm Daniel Whiten ack.
[131.20 → 140.70] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[141.30 → 144.06] It's been quite a season in our lives, Chris.
[144.26 → 147.62] Oh boy, 2020 has definitely had an impact on my life.
[148.22 → 149.24] Yeah, definitely.
[149.24 → 158.26] I think we would not be right to just ignore everything that's happening in our world as we enter into these conversations.
[158.26 → 175.32] Of course, we've got the unrest that's really happening in our country, but around the world as a result of injustices and police brutality and sort of systematic racism that's happened in our country, but also around the world.
[175.32 → 181.50] And then that kind of piled on top of COVID virus related things.
[181.50 → 187.54] And then that piled on top of the economic impact and fallout of that and unemployment.
[187.84 → 192.66] And of course, these things are not separate from AI things.
[192.66 → 200.62] And I think probably over the course of these coming years, I think it'll be years of fallout from everything that's happening.
[200.84 → 201.28] Totally.
[201.52 → 203.12] You know, it'll impact our conversations.
[203.68 → 204.28] It will.
[204.36 → 204.56] Yeah.
[204.56 → 205.70] It's all real life.
[206.06 → 208.16] And a couple of thoughts there.
[208.36 → 219.98] You know, you talked about the injustice of what's happening in terms of, you know, in Black Lives Matter, being able to come back out and be meaningful in this discussion, which I think is fantastic.
[220.50 → 222.00] It's a time of change right now.
[222.08 → 223.54] It's a time of massive shift.
[223.54 → 225.68] And I know it impacts everybody in the audience.
[225.88 → 231.52] I know for me, you mentioned COVID and you and I had talked a little bit about before the show.
[231.68 → 236.14] And so I'll share very briefly with the audience what's happened recently to me.
[236.42 → 237.92] I'm actually choking up a little bit.
[238.36 → 241.42] So my mother-in-law recently died of COVID.
[241.82 → 246.56] So it's impacted my family and just wanted to share that with the audience.
[246.66 → 248.56] I've been kind of missing in action for a little while.
[248.64 → 252.58] I know you did an episode with Darwin AI recently, and I thank you for doing that.
[252.58 → 257.22] And I know with the unrest, we paused to show briefly, but I've been kind of out of action.
[257.70 → 265.78] Just wanted to let folks know, I know so many people that say they hear about COVID in the news, but it hasn't touched their lives in a direct way.
[266.30 → 272.54] And speaking as someone who has had it touched directly, it is a serious disease.
[272.72 → 276.70] And so I just hope everybody will follow the safety guidelines and be aware.
[277.38 → 280.02] When you lose someone that you love, it changes how you see it.
[280.02 → 284.70] When you have other family members that have it, then you're working on them.
[284.82 → 288.50] And when you have a whole family in isolation, it makes a difference.
[288.76 → 290.14] So stay safe, people.
[290.38 → 291.38] I appreciate it.
[291.54 → 294.96] And just wanted to let you know, it's real and it's touched my life.
[295.08 → 296.46] And thank you for letting me say that.
[296.52 → 297.36] It was important to me.
[297.58 → 297.78] Yeah.
[297.90 → 299.14] Thank you for sharing, Chris.
[299.14 → 301.86] I know it takes a lot to share that as well.
[301.86 → 306.76] And I know my thoughts and prayers have been with you and your family.
[307.00 → 315.34] And yeah, I think it's just another data point to motivate people to, like you say, take things seriously.
[315.34 → 328.00] But also, I mean, I think the AI community, a lot of the people that listen to this podcast, there are many meaningful ways that people can contribute.
[328.00 → 339.50] Whether it's on the COVID and virus related front, whether it's on the racial injustice side of things or the economic side of things.
[339.56 → 341.76] Of course, there's community things that we can all do.
[342.00 → 345.48] Being good neighbours, being, you know, caring for people.
[345.48 → 354.18] But then also being tech people, being AI people, I mean, there are some real intersections with AI technology.
[354.44 → 367.06] I mean, of course, on the policing front and that side of things, we've seen, you know, increased usage of things like facial recognition and other things that are concerning for certain groups.
[367.30 → 370.68] Algorithmic decisions that are impacting certain groups.
[370.68 → 380.40] On the virus side of things, there's a bunch of AI people that are trying to come up with beneficial applications to help that scenario.
[380.52 → 387.06] Not necessarily all, you know, predicting COVID outcomes, but, you know, helping people get the right information.
[387.30 → 391.52] We had the episode with the COVID QA group that was working on that.
[391.62 → 397.08] We also talked to, had an episode about the CORD-19 data set as related to COVID.
[397.08 → 407.10] And there are ways that AI people can contribute both in terms of data annotation, in terms of coding, in terms of jumping into open source projects.
[407.58 → 419.06] So I think I'd really encourage people, if you're interested in those things or wanting to know how to contribute to those things or wanting to know how to make your voice heard in terms of good AI ethics related things.
[419.06 → 423.38] And reach out to us on our Slack channel, our Slack team.
[423.48 → 429.66] You can find us at changelock.com slash community or on our LinkedIn page or on Twitter.
[429.66 → 435.54] We really are wanting to have some discussions about these topics and point people to good resources.
[435.54 → 440.64] So I'm really hoping that people reach out and find some of those ways to contribute.
[440.64 → 450.04] You know, I'm so glad that not only did you bring up the practitioner side of being an AI professional or an enthusiast, but also the AI ethics side.
[450.16 → 453.08] And as we've talked about before, I'm very involved in AI ethics.
[453.08 → 467.60] And so, you know, as we talk about injustice, both the technical skills that you have there and the incredibly deep, rich thinking that we hear from people in this community, you have a voice and you can shape the future.
[467.94 → 471.24] This is really something that we have a role to play in.
[471.54 → 474.76] So I am asking our listenership to engage.
[474.88 → 479.72] Engage with these issues in real life and bring your expertise and your skills to bear on this.
[479.72 → 480.16] Yeah.
[480.28 → 480.76] Yeah.
[480.90 → 487.54] And later on, normally in these fully connected episodes, we take some time at the end to share some learning resources.
[487.90 → 494.34] I've pulled in a few that I've run into over the years as related to bias and fairness in AI.
[494.86 → 501.64] And so we'll talk about those later on in the episode and maybe some places where you can find out about some of those things.
[501.64 → 516.72] But before we get there, we do want to kind of acknowledge that there are a lot of, you know, encouraging and exciting things coming out in the AI community in terms of advancing various efforts and various toolkits.
[516.72 → 521.46] And that's one of the things that we wanted to do in this episode was highlight a couple of those.
[521.46 → 535.82] The first of those that I saw, which really excited me, was the announcement from Streamlet that they finished a Series A of funding for actually $21 million, which is kind of crazy.
[536.14 → 538.82] If you remember, we had Streamlet on the podcast.
[539.72 → 541.14] That was episode 66.
[541.64 → 544.58] And we talked all about the Streamlet project and everything.
[544.72 → 547.54] So we definitely recommend you go back and listen to that.
[547.54 → 552.20] But in general, I think Streamlet is an incredible project.
[552.44 → 554.20] I don't know if you've been following it at all, Chris.
[554.58 → 558.86] Certainly after we had the conversation with the team, I found it incredibly inspirational.
[559.30 → 565.06] And, you know, they are, Streamlet is an open source framework to turn Python scripts into interactive apps.
[565.22 → 568.90] And I know prior to us engaging them, I wasn't really aware of that.
[568.90 → 572.78] But it's a super cool approach, and it's showing the creativity.
[573.16 → 573.78] So, yeah.
[574.30 → 574.64] Yeah.
[574.64 → 591.76] So I know for me, I have no, well, I don't know if I want to say absolutely zero, but I don't have much exposure and experience in terms of like front end engineering or building actual graphical interfaces or web apps or anything like that.
[591.76 → 617.48] At the same time, often when you're trying to integrate a machine learning application into a business process, there's a very human side of that that becomes very difficult if you aren't able to let people interact with what you're building in a visual way.
[617.48 → 626.38] So I'm thinking right now, I attended a couple workshops recently on active learning and sort of human in the loop methods.
[627.44 → 637.60] And so you could have this scenario where, you know, maybe you're working on like the workshops we were talking about, like translation applications, machine translation applications.
[637.60 → 656.18] And sometimes when you deploy that, you might want to have a model in the loop that tries to identify like, you know, bad translations or something that your machine translation application is producing and then have a user actually review and look at those and correct them.
[656.18 → 664.52] And so you've got this kind of graphical piece, but also the user piece, the non-technical user piece potentially that's interacting with that.
[665.00 → 681.64] And so, yeah, I see that scenario, I think, popping up all the time and Streamlet, I think, fits right in there, which is why it seems like to me that it's getting a lot of attention is that there's an often seen pain point that isn't really well dealt with.
[681.64 → 711.62] I agree.
[711.64 → 712.64] In AI.
[712.90 → 721.56] If you don't either yourself or people you work with have those skill sets, you can lose the value in something that would otherwise be great very, very quickly.
[721.90 → 726.74] And as I've worked in a professional context, that point has been driven home to me over and over again.
[726.82 → 732.28] So I tend to approach AI from a user perspective, even if I'm the developer doing the work.
[733.14 → 736.86] And Streamlet is talking about the ways they'll use this money.
[737.00 → 739.18] They want to extend the application.
[739.18 → 743.32] And I should mention, too, this is an open source application that you can use.
[743.56 → 745.08] So you kind of just pip install.
[745.20 → 749.08] I think you pip install, if I remember right, back to Streamlet.
[749.28 → 751.08] And then run it locally.
[751.32 → 760.40] And they have a bunch of different customizations that you can add, like little sliders and text input and file upload and plotting and all sorts of ways you can configure it.
[760.40 → 768.58] And so I think that when they're talking about extending, of course, extending that and the customizability of it and customized layouts.
[769.04 → 771.88] They also talk about building in programmable state.
[771.88 → 781.50] One of the things I was curious about, of course, because I've always used Streamlet just as an open source application is if they're raising money, they're obviously a business.
[781.50 → 807.66] And so I think the other thing that they're going to devote that effort into is the Streamlet for Teams, which in my understanding is some sort of sharing and a combination of like sharing and deploying securely Streamlet apps that are actually sort of production applications and not just like demos or proof of concept sort of things or little tools and that sort of thing.
[807.66 → 812.52] Yeah, I'm looking forward to seeing some of the other things they choose to do as they go into this new phase.
[812.68 → 819.76] So we may have to revisit with them at some point as they get some of this work done, and they're able to use that capital well.
[830.64 → 835.66] Changelog News is the best way to keep up with the ever-changing world of software.
[835.66 → 844.42] We track, log, and contextualize the coolest projects, the best practices, and the biggest stories each and every week.
[844.94 → 852.56] Make changelog.com your daily destination or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[853.24 → 856.10] Join more than 15,000 enthusiastic readers.
[856.38 → 862.54] It'll cost you exactly zero dollars, and you can subscribe right now at changelog.com slash weekly.
[865.66 → 883.80] So I know you had a topic that you wanted to go into, which I think is a good one.
[883.80 → 892.28] But before we do that, I just wanted to mention one other thing that actually just before recording today I saw as I was scrolling through Twitter,
[892.48 → 901.78] which is GPU accelerated training now supported in Windows subsystem for Linux.
[901.78 → 908.86] And I have to admit, I have not been a Windows user for quite some time.
[909.06 → 913.36] But in my understanding, there are quite a few of them out there.
[913.90 → 914.28] There are.
[914.46 → 915.88] Yes, there are a few.
[916.42 → 917.68] Yeah, quite a number.
[917.68 → 931.66] And I know, for example, like when I taught a couple courses at Purdue over the last few years, of course, the lab machines there, Windows machines, or at least some of them.
[932.12 → 942.30] And so it was always a struggle for me to kind of figure out the best ways of like doing sort of AI experiments and programming in that environment.
[942.30 → 947.10] And mostly that's just my unfamiliarity with that whole world.
[947.36 → 948.86] But yeah, this is pretty cool.
[948.98 → 966.28] So I guess Windows subsystem for Linux or WSL enables the users of Windows to run a native unmodified Linux kernel or Linux command line directly on Windows.
[966.28 → 969.16] So that's pretty cool in and of itself.
[969.32 → 979.24] But now I guess the step is that they're adding the GPU acceleration to that and, you know, connecting up things nicely to CUBA and those sorts of things.
[979.54 → 980.70] Yeah, and I think that's great.
[980.88 → 983.68] And like you, I have not recently been a Windows.
[983.76 → 986.58] Once upon a time, I was on Windows, moved away.
[986.80 → 990.08] But I've been hearing they're really embracing open source in recent years.
[990.08 → 998.46] And that's definitely brought me back around to being very, you know, I would consider them for a while before they kind of hit that approach.
[998.80 → 1003.44] But so total kudos to Microsoft for making that very hard.
[1003.54 → 1006.44] It's hard to steer a big organization in a very different direction.
[1006.68 → 1007.94] So I've been very impressed.
[1008.24 → 1011.96] I think it's a fantastic step forward to have the GPU support in that.
[1012.32 → 1019.24] And the funny thing is I keep running across Windows subsystem for Linux being incredibly usable from people that are using it.
[1019.24 → 1022.02] And I work in an organization that has a lot of Windows users.
[1022.36 → 1027.58] And so I'm getting really, perfect feedback on the work they've done and being able to utilize that Linux kernel.
[1028.04 → 1030.30] It's not a second class citizen, as I understand it.
[1030.48 → 1031.58] It really does a good job.
[1031.68 → 1037.38] So now seeing that they have that support may change the landscape a little bit as that gets adopted over the next couple of years.
[1038.12 → 1048.94] Yeah, I think that the like the sort of ability to run unmodified Linux things on Windows, that part sort of rings trues right away for me.
[1049.24 → 1052.76] And it's cool that you could do the GPU accelerated stuff.
[1052.94 → 1067.84] I guess in terms of my own workflows, often, you know, I don't have the GPU like in my laptop or sitting on my desk, but I'm using it on either a remote computer or in the cloud.
[1067.84 → 1078.68] So in that case, if I was on Windows, I think the important thing would be this sort of command line stuff and scripting things and all that sort of things that I could do in the way that I'm used to.
[1079.04 → 1090.58] But I know also that people build a lot of great systems for also, you know, like gaming computers, for example, that are Windows based.
[1090.58 → 1100.36] This is where my mind's kind of going with this, I guess, is that there's all of these like gaming computers out there with GPUs and games for the most part.
[1100.50 → 1106.88] And I'm also not a gamer, so I'm really speaking outside my domain, but for the most part running on a Windows system.
[1106.88 → 1119.84] So it seems like now this would make it maybe easier to buy a sort of off the shelf gaming computer or gaming laptop that's Windows and then use the GPU on that for AI purposes.
[1120.38 → 1128.40] Whereas before, maybe you have to like to buy that and then install Linux and figure out all the drivers and blah, blah, blah, blah.
[1128.70 → 1131.14] Maybe that makes that process easier.
[1131.26 → 1131.98] I'm not sure.
[1132.46 → 1133.66] So I would agree.
[1133.66 → 1136.40] I'm not much of a gamer, but I think that makes a lot of sense.
[1136.54 → 1140.64] I actually think I'm probably going to try a Windows subsystem for Linux out in this context.
[1141.46 → 1152.02] So like yesterday, I didn't have a chance today, but yesterday I was logging into a dedicated DGX2 and I got all 16 GPUs for myself.
[1152.70 → 1154.88] And that was a lot of fun doing some work on there.
[1154.98 → 1155.50] That sounds like a lot of fun.
[1155.58 → 1156.62] It was a lot of fun.
[1156.80 → 1160.12] And so I might have to pull out a Windows laptop and do the same thing.
[1160.18 → 1161.74] I did it from my Mac going in.
[1161.74 → 1164.10] But yeah, I think I'm going to give it a whirl.
[1164.60 → 1169.34] You could write a blog post about Windows laptop versus DGX2.
[1169.68 → 1170.18] There you go.
[1170.48 → 1171.04] There you go.
[1171.38 → 1175.96] I figure there will be a clear winner, but it would be interesting to do the comparison.
[1176.48 → 1181.28] Well, I can start on the Windows side and use that as a client and then log into the DGX.
[1181.48 → 1183.14] And we'll use both systems.
[1183.26 → 1184.28] We can make that work.
[1184.88 → 1185.84] Yeah, yeah, sure.
[1185.84 → 1186.24] Cool.
[1186.24 → 1186.80] Cool.
[1187.08 → 1188.16] Well, let us know.
[1188.28 → 1194.80] I'll be interested to hear from people if and when they start getting into this Windows mix of things.
[1195.26 → 1203.74] But moving on, I think you were mentioning a topic to me that I think is pretty interesting and oftentimes very confusing for people.
[1203.84 → 1205.66] And I know that we've touched on it before.
[1206.20 → 1208.46] You want to mention what you were thinking there?
[1208.46 → 1208.90] Sure.
[1209.64 → 1216.50] So I do quite a bit of mentoring for people, not only at my employer, but just in general.
[1216.84 → 1218.88] And people will reach out and ask for advice.
[1219.14 → 1228.82] And probably the thing that people ask about most often is they're trying to figure out how to orient their own careers on AI, ML, focus.
[1229.36 → 1235.66] I've been pretty open that I came from the software development world and reoriented my own career some years back on this.
[1235.96 → 1236.94] And it's completely doable.
[1236.94 → 1241.00] I think it's a myth that everybody in AI is a data scientist.
[1241.52 → 1250.92] I think it's a myth that you have to have a PhD or some other university-based experience to get into this field.
[1251.28 → 1252.26] It's certainly not the case.
[1252.36 → 1255.12] None of those are the case for me and a lot of people that I've worked with.
[1255.58 → 1265.52] And I think in a previous episode, I don't recall which one, but I mentioned the fact that because I've been in my career now for, I don't know, 25 bearish in that frame,
[1265.52 → 1268.96] I was around when the web was taking off.
[1269.32 → 1278.22] And that was the early part of my career was when the web went from the internet with no web into the web that was initially just academic and then took off.
[1278.30 → 1287.10] And I have observed as we've gone through this AI revolution that it follows many of the same trends of a brand-new field that is exploding outward.
[1287.10 → 1290.88] And in the beginning, people thought computer science was the thing.
[1291.04 → 1293.44] You had to have a computer science degree to do that.
[1293.54 → 1298.16] But we rapidly, one role changed into many roles very rapidly.
[1298.48 → 1304.68] And there was a lot of diversity that got introduced as well as the skills you needed, the level of experience to do different roles.
[1304.82 → 1306.04] It got complicated.
[1306.04 → 1307.32] And that's good.
[1307.44 → 1308.98] It's a sign of maturity.
[1309.16 → 1311.40] And we're definitely seeing that in this field.
[1311.86 → 1315.54] And so a lot of people, when they're trying to figure out, how do I do this?
[1315.66 → 1318.96] How do I fit into this new exciting AI world?
[1319.20 → 1321.56] That's where I really want to be in the years to come.
[1321.90 → 1323.64] But that's not where my education has been.
[1323.74 → 1325.98] That's not where my previous experience has been.
[1325.98 → 1335.66] And one of those things that I start with people that I wanted to address today is there's not one role out there that you have to find your way into.
[1335.88 → 1337.06] There are many ways.
[1337.26 → 1341.58] And actually, it might be a role that you're already playing in a slightly different context.
[1341.80 → 1345.06] It may be that you can kind of evolve your way into this.
[1345.06 → 1359.32] And so if you're already working with databases and other data sources, data lakes, that's one area that's now very involved in the big data input that goes into these AI models and stuff.
[1359.36 → 1368.50] So I really wanted to talk in a practical sense and have a conversation about what are different avenues people might be able to take to get into this fun field.
[1368.50 → 1386.42] Yeah, and I think along with that, of course, there's, like you say, there's a lot of kind of jargon and job titles out there that people hear and might be confusing as to how they fit in, like data scientist versus machine learning engineer or research scientist or data engineer.
[1386.42 → 1400.98] But maybe it would be good to kind of talk about the various pieces of the AI workflow and where certain people might fit in terms of a team of people working on these sorts of solutions.
[1401.32 → 1402.36] That's a great idea.
[1402.36 → 1422.04] From my perspective, when you're thinking about the workflow that often happens here, there is sort of an initial phase, which involves a lot of kinds of problem defining and scoping in terms of what may or may not be possible and what might be good to experiment with or try.
[1422.04 → 1437.52] And also an exploratory kind of phase of data gathering and pre-processing and in an exploratory and interactive way, doing some model training and sort of proof of concept evaluation and validation of a certain process.
[1437.52 → 1454.62] So, you know, for example, if you're a manufacturing company, and you say, oh, we've got this problem on our manufacturing line, and we think maybe we could stick a camera, you know, in this location and detect this problem or something like that.
[1455.18 → 1460.30] You have to figure out, OK, well, what would I want as my input and output data?
[1460.42 → 1461.86] What's actually going to be fed in?
[1462.18 → 1463.88] Could this camera be placed?
[1463.88 → 1466.94] What would be the appropriate output that would actually make it useful?
[1467.52 → 1476.30] And then in an exploratory way, like, could I actually gather some of the data which would allow me to train that sort of model?
[1476.42 → 1481.12] And if I could gather that data, what sort of model might I go after?
[1481.30 → 1485.00] And all of this stuff is very iterative and fuzzy.
[1485.30 → 1487.00] I guess this is the fuzzy phase.
[1487.42 → 1488.86] I don't know if you'd agree with me.
[1488.96 → 1492.22] I think a lot of these projects start out that sort of way.
[1492.22 → 1492.90] It does.
[1493.02 → 1495.44] There is expertise required on the front end.
[1495.44 → 1498.70] In real life, you don't jump in to model development.
[1499.02 → 1507.20] I think there's this kind of perception of, you know, come join us, hop on, you know, pick an environment, whatever you care about and build a model.
[1507.34 → 1510.10] But there's a lot of work that goes into it on the front end.
[1510.42 → 1517.22] Before you even get to exploring in the data context, you've got to figure out what is it that you think you want to build and why?
[1517.22 → 1521.58] And why on earth would this particular approach be the right approach?
[1522.46 → 1527.14] And why would AI bring value in versus some other solution?
[1527.40 → 1527.60] Yeah.
[1527.76 → 1533.58] I mean, that's a great point in that there might be five different ways of approaching a solution to the problem.
[1533.58 → 1545.44] And if building a neural network is the most expensive approach to doing that, and when I say expensive, I mean the amount of effort and time and resources necessary to do it.
[1545.80 → 1553.12] Why would you do that if you can get a result that's just as good from, you know, from some other algorithmic approach?
[1553.12 → 1560.76] And you need whatever problem you're going to solve, you need expertise as far as being a domain, you know, expert on that problem area.
[1560.90 → 1567.22] And that might mean working with the business side of your company on what it is that they're trying to provide for customers.
[1567.22 → 1570.04] Because at the end of the day, that's what a company is there to do.
[1570.24 → 1570.34] Yeah.
[1570.44 → 1572.84] And we're just barely touching on the front end of this process.
[1572.84 → 1589.46] So there are so many ways to engage in this AI process that we're talking about that don't require that you have a PhD, you know, in data science from a, you know, from a top university and have 30 years of data behind your belt, you know, under your belt.
[1589.46 → 1589.52] Yeah.
[1589.52 → 1599.68] I think actually there's like in this sort of category of contribution, I guess we could call it.
[1599.68 → 1603.86] Um, this problem defining, scoping, exploratory stuff.
[1604.30 → 1628.88] Um, in fact, I think there is a sort of solution architect sort of role here where you do need some type of knowledge about AI systems and what is possible and what is feasible and what isn't feasible and what's sort of overkill and what's not overkill and appropriate usage and like scoping in terms of how long this is going to take or how much data we might need.
[1628.88 → 1635.92] But those are skills that you can pick up without knowing like the difference between LSTM and grew, right?
[1636.22 → 1636.36] Yeah.
[1636.46 → 1640.38] That level of detail is not required, I think, for this sort of thing.
[1640.38 → 1664.62] Although I may not be one of them, there are people out there that I think really enjoy that, like going into a situation or a problem, maybe dealing with a client on a shorter timescale, like, you know, a few months and scoping out a potential solution and then passing that off to another team to actually do some more implementation and production related things.
[1664.62 → 1684.28] Absolutely. I'm one of those people sometimes. Yeah. It's one of the things that I do in my own job. And I'll tell you, having built up some expertise in the field, if you can go talk to people on the front end and help them figure out what it is they should be thinking about, what's going to serve the need, it can be quite fulfilling.
[1684.28 → 1702.90] And it does take some understanding and expertise of the field to be able to do that successfully. If you go in and only do the kind of be a business analyst without any background at all, and no interest in developing the background, you won't be as effective at being able to decide that. So strategy is a key part of the front end of this process.
[1702.90 → 1727.58] Yep. I think once the problem starts shaping up, like this seems like it's going to be a valuable thing to do. There's still that exploratory phase of like getting an initial proof of concept data set together, you know, proving out that this will actually work and produce the type of value that we want.
[1727.58 → 1740.20] And oftentimes in this stage of things, I think like getting a kind of brute force solution is kind of how I think about it in terms of this thing might not be optimized in every way.
[1740.34 → 1749.48] It might not have the exact, you know, accuracy or performance that we want, but all the right things are sort of plumbed together.
[1749.48 → 1755.40] And like the right type of data is coming in, the right type of pre-processing is happening.
[1755.60 → 1763.12] The right type of model is producing, you know, some result, which is then being used to create something of value.
[1763.12 → 1779.28] That kind of rough plumbing of those things together requires now some technical skill, but this doesn't have to be a fine-tuned C++ application that, you know, runs with super high performance on an embedded device out in the field.
[1779.28 → 1784.84] This is like proving out that the thing works and developing the right type of solution.
[1785.58 → 1794.56] So I think it's a more technical level, but it's not as hardcore software engineering or data engineering as it could be.
[1795.08 → 1797.48] When you say that, I agree with everything you just said.
[1797.48 → 1812.58] And the way I would express that is that AI development fits very well into an agile software development process where you're having to iterate, and you learn from that iteration, and you make those adjustments and you go back.
[1812.64 → 1822.46] And that happens both at the model level, and it also happens in terms of how you're going to choose to deploy and do the engineering you need to accomplish that.
[1822.46 → 1836.14] I very much, and I know that I'm going to say something slightly controversial, I think, and that is that I think of AI development as a component of software development, which a lot of data scientists will say, no, it's not.
[1836.22 → 1836.76] No, it's not.
[1836.76 → 1847.70] But when I'm looking at it in production, and I'm looking at us actually managing that, I see it in that larger context because all of those other activities are happening around it.
[1847.92 → 1848.70] So definitely.
[1852.46 → 1861.86] We deserve a better internet and the brave team has the recipe for bringing it to us.
[1861.98 → 1863.00] Start with Google Chrome.
[1863.22 → 1866.96] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1867.16 → 1868.02] Rip out the Google bits.
[1868.14 → 1868.80] We don't need them.
[1869.16 → 1871.66] Mix in ad and tracker blocking by default.
[1871.94 → 1879.34] Quick access to the Tor network for true private browsing and an opt-in reward system so you can get paid to view privacy respecting ads.
[1879.34 → 1883.30] Then turn around and use those rewards to support your favourite web creators like us.
[1883.66 → 1888.22] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1888.22 → 1911.70] I really liked where you were headed with what you're saying, Chris, in terms of AI development being viewed as a sort of subcategory of software development.
[1911.70 → 1918.44] I think this fits very well into the mindset of another person we had on the show.
[1918.58 → 1923.82] Joel Ruse will link to his episode from the Allen Institute for AI.
[1924.18 → 1927.80] I think he's mainly working on the Allen NLP project.
[1928.16 → 1933.04] And I think he had a lot more things to say about that and why it's useful.
[1933.04 → 1946.16] I definitely think that we kind of started talking about the more technical exploratory stuff where you're trying to figure out what you're going to do and start plumbing the right pieces together and validate a solution.
[1946.16 → 1964.92] You will see some difference in industry, at least from my perspective, in terms of sometimes at an organization, the people that are doing that are not the same people that are at the end of the day involved in producing the production system that's actually implemented.
[1964.92 → 1978.86] And then you'll see other organizations where at least there is some overlap between the team that does this sort of exploratory work and the team that actually produces production systems.
[1978.86 → 2001.88] From my perspective, the latter has a big advantage because if you have total separation between those groups, then when something goes wrong in production, basically, the production team will, maybe in a non-confrontational way, but basically at the end of the day, they'll say, well, this is a problem with the solution and the model and the way it was developed.
[2001.88 → 2003.44] Not a problem with our implementation.
[2003.44 → 2009.38] And then the people that did the exploratory work and validated the solution will say, no, our solution's great.
[2009.62 → 2011.66] You know, there must be something in the implementation.
[2011.88 → 2020.22] No one's taking ownership of it and no one's taking ownership of the robustness of it in particular, like in how robust the solution is.
[2020.30 → 2026.92] So I think in a perfect world, there is some overlap between the group that does those things.
[2027.02 → 2028.76] No, I agree with you completely.
[2028.76 → 2038.16] And I think the reason, to state it, the reason that that second group has the advantage is because they are able to learn from those earlier processes.
[2038.42 → 2043.52] So if you have one group doing a prototype, they've gone through that process, and they've learned what they need to know.
[2043.58 → 2050.40] And if they're going to hand it off to a production-only group, well, they're starting from zero again or from whatever documentation came out of that first thing.
[2050.40 → 2060.28] So there's certainly an advantage to the learning process, which is why AIMS development is best served in a larger agile development process.
[2060.28 → 2066.14] And if you're in that software development world, and you're hearing this, these should be familiar terms to you.
[2066.46 → 2080.16] And those are all potential inroads for you and your career and your particular interest in this to translate existing skills and existing interest into this AI world and be able to do that.
[2080.32 → 2082.98] And there's no point where you're ever done.
[2082.98 → 2090.06] You can continue to migrate across that space by always learning and always deciding where you want to go next and doing that.
[2090.44 → 2090.56] Yeah.
[2091.22 → 2094.48] I think that's crucial for career development in general, but especially in this one.
[2094.88 → 2095.12] Yeah.
[2095.12 → 2113.42] And even in the phase of this that's exploratory, I often use this analogy, which listeners will be familiar with, that a lot of AI development is more akin to cooking according to a recipe than it is some intense research and development.
[2113.42 → 2126.20] And so even in that exploratory phase, it's taking pieces of things that have been done before and putting them together in a unique solution, which is very similar to software engineering.
[2126.20 → 2137.72] And if you were to produce a proof of concept in software engineering, the difference, I think, you know, there is a sort of tool set difference, maybe that some software engineers might be a little bit uncomfortable with.
[2137.72 → 2151.10] Like in this exploratory phase, you might have a, you know, a Jupyter notebook that shows here's how I ingress data and then here's how I pre-process the data and then here's how I train my model and then here's how I do inference.
[2151.10 → 2163.98] And then when you move into the production side of things, maybe it gets a little bit more comfortable in terms of the tooling for software engineers where you would take that notebook and then say, well, I'm not going to run my notebook in production.
[2163.98 → 2172.62] I've got to take out this data gathering piece and make it a Docker container that's going to run, you know, in Kubernetes on AWS.
[2172.92 → 2180.44] And then I've got to take out this pre-processing container and figure out how to run it in parallel over a large data set in the cloud.
[2180.58 → 2189.46] And then I've got to take my training piece and pull that out and Voucherized it and figure out how to run it on some GPU accelerated infrastructure.
[2189.46 → 2195.38] And those pieces still carry through, but the tool set and the way you go about it definitely changes.
[2195.60 → 2197.32] Yeah, that's a great point there.
[2197.44 → 2205.56] And that is that at different points, you may have different people involved in the maturation, the maturity aspect of this process.
[2206.08 → 2216.84] And so, you know, it's really common for software developers to look at a Jupyter notebook for the first time and scoff at it and say, no, I grew up in software development best practices.
[2216.84 → 2221.16] I'm looking at this Jupyter notebook, and it's, you know, why would you do that?
[2221.24 → 2228.64] But, you know, if you were the data scientist that's trying to put the model together, it's a fantastic way of iterating rapidly.
[2228.90 → 2232.48] And your job at that point is not to produce production software.
[2232.66 → 2234.84] It's to test and try different things out.
[2235.32 → 2243.62] You may be implementing a transfer learning approach where you're then trying to customize that transfer learning into the specific solution you need.
[2243.62 → 2248.62] And likewise, the data scientist needs to recognize when you deploy it, you're not deploying that notebook.
[2248.94 → 2252.52] You were using the notebook for what it's good for, but it has to be a software component.
[2252.96 → 2258.78] It's a model that's wrapped in a software component that's being deployed out into a larger software system at the end.
[2259.26 → 2261.86] And so there's a role for all of these things.
[2262.06 → 2264.12] And so leave your biases at the door.
[2264.36 → 2265.02] Leave them there.
[2265.42 → 2270.16] Look for why each tool or each role is so important and recognize that.
[2270.16 → 2273.90] Because I've seen people fall down in that way many times.
[2274.54 → 2274.64] Yep.
[2274.92 → 2286.94] I know, for example, we had a question in our Slack recently in a discussion about, hey, I, you know, I hear all of this stuff about training, and I'm able to run these examples.
[2287.24 → 2293.02] But then when I try to do this inference in production, the performance is so terrible.
[2293.02 → 2297.82] Why is no one talking about this or how, why is it hard to find resources about this?
[2298.00 → 2298.62] Great question.
[2298.62 → 2302.14] There definitely are resources out there.
[2302.24 → 2311.48] And I think like the commenter said, it would be great to have a even a full episode about that side of things and model optimization.
[2311.48 → 2325.30] That is another piece of the puzzle that changes when you kind of move later on into a project is I, if I'm running this an edge device in a manufacturing plant, it's going to have concerns.
[2325.30 → 2330.82] If I'm doing it on a mobile device, it'll have different challenges.
[2330.82 → 2336.16] If I'm doing it on a beefy cloud instance, then you have maybe more flexibility.
[2336.76 → 2341.50] But you may have like latency issues you want to deal with or something in responding to people.
[2341.50 → 2344.68] So that's a great question from the listener.
[2344.68 → 2346.60] And I love how you led into that.
[2346.70 → 2352.98] And really, I, I, I'm not sure if it's an official term or not at this point, but we have conversations.
[2352.98 → 2356.82] I know in my own collection of colleagues about this all the time.
[2356.82 → 2358.76] We refer to it as AI engineering.
[2358.76 → 2372.76] And I think the thing that is so crucial about that is to recognize that two years ago, we were talking about the edge as kind of exception case because people really deploying most often into servers and, you know, or locally or whatever.
[2372.76 → 2375.96] And it was more of a kind of standard, well-known environment.
[2375.96 → 2380.02] But going forward, most things will be at the edge.
[2380.16 → 2391.46] As you make models and the utility of models pervasive in our society, in our culture, you're going to see edge devices being the targets of that deployment in so many different ways.
[2391.60 → 2395.80] And so that requires that you rethink your engineering to accommodate that.
[2395.92 → 2403.78] Once upon a time, you know, deploying software was really, you know, it was kind of code-centric, and you'd think about just processors and stuff like that.
[2403.82 → 2404.84] But now it's all about data.
[2404.84 → 2412.34] If you are deploying to some sort of mobile platform, maybe it's an autonomous vehicle, you have telemetry from that vehicle.
[2412.50 → 2414.06] You have sensors in that vehicle.
[2414.18 → 2415.66] You have cameras in that vehicle.
[2416.32 → 2431.10] And to provide the level of performance you need to be able to do real-time inference on that requires special knowledge of engineering on getting the right data in the right way to the right place at the right time so that it can be acted upon.
[2431.10 → 2435.78] And you no longer are doing static data that you're running through a server or something.
[2436.26 → 2440.48] So AI engineering is crucial for making this stuff actually work.
[2440.56 → 2442.82] It's later in the process than what we were talking about.
[2442.82 → 2449.24] But, you know, after that data scientist has been working in the Jupyter notebook, you got to either put it out there in the world or it's useless.
[2449.42 → 2450.84] It doesn't do anything for you.
[2451.44 → 2451.64] Yep.
[2451.64 → 2471.24] Another piece of this puzzle is actually, I think, so there's like the AI workflow and the different, you know, phases along a project all the way from kind of solution architecting or consulting to, you know, the very technical side of AI engineering things.
[2471.24 → 2482.02] But then there's also, I think, you know, you could look at that workflow in different domains or verticals and that's going to look very different.
[2482.22 → 2497.90] Of course, you know, in maybe the manufacturing world, you're going to be thinking a lot about computer vision and running things and edge devices and potentially hazardous conditions where they might have to be, you know, you have a lot of device issues.
[2497.90 → 2509.50] In other cases, like in webspace, if you have a web app that you're dealing with or software as a service company, then you might be running your models a lot of time, you know, in the cloud.
[2509.76 → 2517.10] And maybe you're dealing with a lot of natural language processing issues and dialogue related issues with customer service and all of that.
[2517.16 → 2526.26] And each of those sets of problems has its own tooling and its own methods and its own community and its own way of going about things.
[2526.26 → 2534.38] And so I think another thing to think about when you're thinking about the lay of the land is also the domain.
[2535.16 → 2538.76] And I think, like you said, this happens in software engineering, too.
[2539.30 → 2547.86] And, you know, people have specialized in certain areas of software engineering and AI, I think, will be no different.
[2548.06 → 2550.22] There's a lot of specialization that can happen.
[2550.40 → 2553.30] Yeah, I think in my own experience, it definitely bears that out.
[2553.30 → 2562.48] If I look at counting my current employment, my last three organizations that I've been a part of, and all three had an AI role.
[2562.88 → 2567.42] In the first one, we were working with clients, and it was server-based.
[2567.50 → 2569.74] It was kind of what I think of as a little bit old school now.
[2570.24 → 2575.10] You know, it's funny that it doesn't take very long for something to become old school because it evolved so fast.
[2575.10 → 2580.86] But, yes, we were deploying models into big servers that were resource-rich.
[2581.50 → 2593.02] And then in the next organization I went to, we were focused on warehouse spaces and introducing robotics and cameras and different things that make logistics work.
[2593.02 → 2597.52] And that presented a different set of challenges that were specific to the domain.
[2597.90 → 2605.42] And then now I've moved into the defence industry, and I focus on autonomous platforms and other adjacent technologies.
[2606.02 → 2615.14] And some of the previous things certainly had an effect, but this is a new domain that has its own specific constraints and challenges, and that's the case.
[2615.14 → 2623.18] So we are definitely seeing diversity in how AI is conceived and implemented depending on the context that you're using it in.
[2623.50 → 2624.10] Yep.
[2624.60 → 2635.42] Well, one thing that's true across all of these workflows and domains is that definitely you're going to have to deal with bias in your data and model fairness.
[2635.42 → 2652.32] And this kind of brings us to the end of our conversation where we're going to share some learning resources with you and think in light of our current climate and things going on in our world, it's only natural to share some resources about bias in your data and model fairness.
[2652.32 → 2665.72] I think that one of those resources, which maybe is a good jumping off point, there's a nice write-up in Google's machine learning crash course about fairness and types of bias.
[2666.34 → 2667.84] And I thought this was pretty interesting.
[2668.10 → 2682.22] And maybe certain branches of science have similar terminology around this sort of thing and think about like, you know, survey science, for example, thinks about bias a lot and populations and those sorts of things.
[2682.32 → 2687.32] So this was really helpful for me to kind of pickup some of this terminology and examples.
[2687.32 → 2704.42] They actually go through with talking about reporting bias, automation bias, selection bias, group attribution bias, and others, and give examples of those types of biases and how they can creep into your data, which I thought was incredibly useful.
[2704.42 → 2714.48] I don't know how familiar you are with some of these things, Chris, but it was really helpful for me because I was not familiar with the sort of categories that you could think about bias in.
[2714.84 → 2715.30] Yeah, totally.
[2715.60 → 2721.54] And bias in the involvement I have in the AI ethics space, bias is a huge part of it.
[2722.02 → 2728.24] It's probably the concern that most people associate most with AI ethics.
[2728.40 → 2730.60] It's the thing that people think about the first.
[2730.60 → 2741.76] And so understanding those different types of bias and how they impact an outcome and how they can result in unexpected outcomes, which can be incredibly common, is pretty important.
[2741.76 → 2745.14] So it's a first good way to get into that.
[2745.44 → 2765.12] And kind of going back, I think it's particularly applicable as we have this episode at this particular time, given the large public response to injustice, to think about some of these tools I've already heard are being used in unexpected ways against protesters, for instance, even ones that are not breaking the law in any way.
[2765.12 → 2775.36] And just as we think about different types of bias here, think about how do you want the application of these tools to be used?
[2775.68 → 2784.52] Facial recognition can occur long before or after a protest event by following people through cameras and having to do an automatic tracking.
[2784.74 → 2787.32] There's a lot of impact on how we may want to think about this.
[2787.32 → 2794.76] I'd also encourage people, just a couple more quick mentions here, to take a look at IBM's Fairness 360 website.
[2795.40 → 2811.46] It just includes a really great sort of breakdown about various ways that people are dealing with fairness, both sort of pre-processing of data, in-processing or model change, actual changes to your model that you can make.
[2811.46 → 2815.48] Also, like post-processing monitoring of your predictions.
[2815.84 → 2818.74] They talk about a whole variety of things with great examples.
[2819.06 → 2820.08] So check that out.
[2820.20 → 2827.48] Also, Google's Responsible AI Practices, they have a great write-up and discussion of fairness and bias.
[2828.16 → 2841.44] There's also a good project from Driven Data called Dean, which includes a nice checklist, if you like checklists, that you can sort of start with a default checklist and update it to make sure that your checklists are not going to be used.
[2841.44 → 2850.02] You can also check for certain things like bias and fairness in a project, and that can be embedded within your repository or within a Jupyter notebook or other things.
[2850.22 → 2852.58] So we'll link to all of those in our show notes.
[2852.86 → 2861.94] I think it's well worth people's time to take a look at those things and make sure and educate themselves about how that can creep into your process.
[2862.24 → 2862.44] Totally.
[2862.44 → 2875.00] There's one other one that I'll throw out that is, it has been useful beyond the industry that it started in, is that is the because of the process that the U.S. Department of Defence entered into on their AI ethical principles.
[2875.00 → 2878.00] And we had a show where we addressed that in depth previously.
[2878.20 → 2886.18] They went out into industry and academia and solicited feedback from many, many different people in the space.
[2886.28 → 2888.50] Many of them were luminaries whose names you would recognize.
[2888.96 → 2898.46] And you can actually go and do like, if you Google DOD AI principles, you'll find that they have their five, just like Google and Microsoft and all the other players do.
[2898.46 → 2907.26] But I've noticed recently that they're being adopted in completely different use cases because they're not specific necessarily to the industry that they were formed in.
[2907.40 → 2910.60] So that's a perfect one that I end up interacting with quite a lot.
[2911.74 → 2915.44] Well, it's been great to have a conversation with you again, Chris.
[2915.52 → 2916.48] Great to have you back.
[2916.62 → 2923.70] And I'm looking forward to our future conversations and how those will be shaped with our ever-changing world in the future.
[2923.70 → 2934.60] But I appreciate our listeners hanging through us this spring with changes in our schedule and also changes in your life and being in different places than you normally would be.
[2934.90 → 2939.60] I'm glad that you've continued to stick with us and looking forward to more conversations.
[2940.04 → 2940.40] Absolutely.
[2940.66 → 2948.14] And for my part, I just want to thank the listeners for bearing with us as we started the show and having my sharing what had happened to me.
[2948.14 → 2954.36] In the show notes, I'm also going to include a link to kind of my experience of COVID in a way.
[2954.48 → 2962.20] So if it's something you're interested in and want to know somebody that's actually dealt with it in a firsthand way, you can check that out in addition to the normal notes for the show.
[2962.30 → 2963.44] Thank you so much for listening.
[2967.04 → 2970.24] Thank you for listening to this episode of Practical AI.
[2970.64 → 2971.84] People ask us all the time.
[2971.92 → 2973.54] They say, hey, how can I support your work?
[2973.54 → 2978.46] One easy way is to leave a five-star review on Apple Podcasts.
[2978.46 → 2980.98] Tell folks why you listen and why they should, too.
[2981.12 → 2982.40] It only takes about 30 seconds.
[2982.60 → 2987.90] And believe it or not, those ratings and reviews really do help us rank higher in AI-related search results.
[2988.48 → 2991.36] Practical AI is hosted by Daniel White neck and Chris Benson.
[2991.82 → 2993.02] It's produced by Jared Santo.
[2993.26 → 2993.78] That's me.
[2994.18 → 2997.18] And our music is brought to you by the one and only Break master Cylinder.
[2997.70 → 3000.80] We are sponsored by amazing people at companies who get it.
[3001.04 → 3002.96] Thanks again to Vastly, Linde, and Rollbar.
[3002.96 → 3006.02] Did you know we have a master feed of all Changelog podcasts?
[3006.36 → 3006.86] We do.
[3007.30 → 3009.16] It's your one-stop shop for everything we produce.
[3009.42 → 3012.62] If you like this show, you'll love the Changelog, Brain Science, and Go Time.
[3012.82 → 3017.80] Check it out at changelog.com slash master or search for Changelog Master in your favourite podcast app.
[3018.06 → 3018.72] You'll find us.
[3019.10 → 3019.90] That's it for now.
[3020.10 → 3021.30] We'll talk to you again next week.
