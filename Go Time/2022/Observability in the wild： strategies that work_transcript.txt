[0.00 --> 2.78]  Hey everyone, Jared Santo here, GoTime's producer.
[3.24 --> 8.40]  This episode is a bit different than what you're used to, but hopefully it feels familiar as well.
[8.74 --> 13.44]  We are helping our friends at Grafana Labs produce a podcast all about observability.
[13.76 --> 19.56]  It's called Big Tent and it's hosted by Matt Toback, Tom Wilkie, and GoTime's very own Matt Reier.
[20.16 --> 24.64]  So, today on GoTime we're featuring episode 6 of Grafana's Big Tent,
[24.64 --> 27.64]  where both the Matts talk with Nayana Shetty from Lego Group
[27.64 --> 30.18]  all about observability strategies that work.
[30.78 --> 33.94]  GoTime returns to its regularly scheduled programming next week
[33.94 --> 39.36]  when Ron Evans travels back from 2053 to warn Matt and Natalie all about Go's future.
[39.98 --> 42.18]  Okay, Grafana's Big Tent. Here we go.
[46.76 --> 49.50]  This episode is brought to you by Chronosphere.
[49.50 --> 54.86]  When it comes to observability, teams need a reliable, scalable, and efficient solution
[54.86 --> 57.46]  so they can know about issues well before their customers do.
[57.64 --> 61.08]  They need a solution that helps them move faster than the competition.
[61.64 --> 65.14]  And companies born in the cloud-native era often start with Prometheus for monitoring,
[65.42 --> 67.16]  which is obviously an amazing piece of software,
[67.54 --> 70.30]  but they quickly push it to its limits and often outgrow it.
[70.50 --> 74.08]  They run into issues with siloed data, missing long-term storage,
[74.38 --> 77.34]  and wasted engineering time firefighting the monitoring system
[77.34 --> 79.64]  versus delivering their application with confidence.
[79.64 --> 82.62]  They describe the system as a house of cards,
[82.62 --> 87.50]  where a single developer's seemingly benign change can overload the whole monitoring system,
[87.60 --> 91.80]  or they say they're flying blind because they pride themselves on making data-driven decisions,
[92.24 --> 95.46]  but losing visibility means they lose this competitive edge.
[95.78 --> 99.40]  Ryan Sokol, VP of Engineering at DoorDash, has this to say about Chronosphere.
[99.76 --> 100.00]  Quote,
[100.00 --> 108.20]  Quote,
[108.20 --> 109.36]  End quote.
[109.74 --> 114.06]  Chronosphere is the observability platform for cloud-native teams operating at scale.
[114.50 --> 117.06]  Learn more and get a demo at chronosphere.io.
[117.06 --> 118.06]  Again,
[118.40 --> 119.86]  chronosphere.io.
[128.26 --> 129.42]  Let's do it.
[129.92 --> 130.72]  It's go time.
[142.14 --> 142.86]  Hello,
[143.34 --> 146.00]  and welcome to Grafana's Big Tent,
[146.00 --> 151.92]  the podcast all about the people, community, tools, and tech around observability.
[152.68 --> 156.18]  I'm joined today by, it's only Matt Toback.
[156.24 --> 156.76]  Hello, Matt.
[157.12 --> 157.60]  Hi, Matt.
[157.82 --> 158.46]  What do you mean, only?
[158.80 --> 160.50]  Yeah, no, it's just understated, isn't it?
[160.60 --> 163.16]  Just, I can't believe it's you, really, in a lot of ways.
[163.38 --> 165.00]  You could say, it's how you say it.
[165.02 --> 165.64]  It's not what you say it.
[165.68 --> 166.76]  You say, I can't believe it's you.
[166.96 --> 167.58]  You're here.
[167.72 --> 168.08]  Oh, right.
[168.14 --> 168.34]  Okay.
[168.40 --> 170.26]  I can't believe it's, I can't believe it's you.
[170.40 --> 171.34]  And you're like, you're here.
[171.80 --> 172.46]  You're here.
[173.02 --> 173.24]  Yeah.
[173.24 --> 173.92]  Well, don't worry.
[174.00 --> 175.06]  It's not just me and you.
[175.06 --> 177.44]  That would be obviously tiresome for both of us.
[177.58 --> 180.94]  We have a special guest joining us today.
[181.12 --> 182.92]  That would be tiresome for both of us.
[183.12 --> 183.46]  Thank you.
[183.52 --> 184.14]  It's how you say it.
[184.14 --> 184.48]  You're right.
[186.56 --> 190.30]  Today, we're joined by Nayana Shetty from Lego.
[190.44 --> 191.00]  Hello, Nayana.
[191.38 --> 192.00]  Hi, Matt.
[192.18 --> 192.64]  I'm mad.
[194.24 --> 196.06]  Yes, just one would suffice.
[196.14 --> 196.66]  We'll share it.
[196.74 --> 197.38]  Happy to share.
[197.38 --> 203.64]  And you are a principal engineer who loves talking about SRE in microservices, right?
[204.42 --> 204.68]  Yes.
[204.78 --> 205.02]  Yeah.
[205.44 --> 209.36]  I think over the years, I've been in teams where we've built microservices.
[210.02 --> 218.22]  And it's when you scale up and have hundreds of microservices, how do you then make them reliable and keep them reliable?
[218.22 --> 220.54]  That's what I'm interested in.
[220.54 --> 228.02]  And yeah, it's been so I was working in the financial times where we had all of these hundreds of microservices.
[228.48 --> 229.78]  And how do we manage it there?
[229.78 --> 233.54]  And now I've moved to the Lego group where we're going through massive digital transformation.
[233.54 --> 238.02]  And here it's like, we want to build these hundreds of microservices.
[238.40 --> 241.00]  So should we care about reliability now?
[241.08 --> 245.46]  Or can we think about it in like 10 years time when we have these microservices?
[245.90 --> 251.26]  So yeah, that is my context to how site reliability, microservices, all of this fit together.
[251.78 --> 254.38]  Yeah, because it did used to be a kind of afterthought, really, didn't it?
[254.42 --> 257.66]  Which is why I think SRE, I think it's short for sorry, right?
[257.66 --> 260.32]  That's one way of looking at it.
[260.38 --> 267.42]  Or like, I always think of it like, sorry, I don't understand why people don't think about site reliability in the first instance.
[267.42 --> 273.66]  Or sorry, I don't understand why people would build this in such a way that it is like half broken.
[273.66 --> 276.96]  Or like, you don't think about the future of this product.
[277.10 --> 283.22]  And you are very close to reinventing the wheel every few months if you went in that direction.
[283.34 --> 286.56]  So yeah, SRE is probably one of the ways of looking at it.
[287.66 --> 297.32]  Just even on a personal note, I'm excited that Naina is here and joining us because we met in 2018 for the first time in an attic in Amsterdam.
[297.90 --> 300.12]  Which when said that way, doesn't feel weird at all, right?
[301.00 --> 307.76]  I mean, we were talking loads of monitoring Grafana and graphite and all of those things.
[307.88 --> 309.74]  So yeah, attic didn't make a difference then.
[309.74 --> 315.70]  But it was wild because we did, we planned GrafanaCon EU in 2018,
[315.70 --> 325.06]  which was technically our third GrafanaCon, but was kind of our biggest up to that point and the most what felt well produced.
[325.20 --> 326.56]  And it was the middle of an Arctic chill.
[326.70 --> 327.30]  Do you remember that?
[327.52 --> 328.84]  That the canals had frozen over?
[329.50 --> 329.72]  Yes.
[329.82 --> 330.00]  Yeah.
[330.06 --> 332.68]  I had struggles getting back home.
[332.94 --> 337.78]  And like, it took me two hours where it should have probably taken me only like half an hour to get home.
[338.02 --> 339.70]  So yeah, I completely remember that.
[339.70 --> 344.26]  And we were in this stage where Tom had just joined the company.
[344.42 --> 346.42]  We announced it on stage, the acquisition of Causal.
[346.60 --> 348.00]  The entire company fit on stage.
[348.08 --> 348.92]  It was 25 people.
[349.34 --> 352.56]  Like when we said kind of goodbye at the end, there's still this photo that circulates here,
[352.64 --> 354.56]  where everyone is just kind of shoulder to shoulder.
[354.94 --> 357.30]  And the stage is the whole company.
[357.78 --> 362.66]  But I do remember, you stand out to me, us being up there kind of in that breakout room,
[362.90 --> 365.14]  talking about what you were trying to do at the Financial Times.
[365.14 --> 370.72]  And it does, it feels like you kind of continue in this natural progression, in this natural journey.
[371.42 --> 374.82]  And like when you think back to you then, how did you see the world?
[375.64 --> 382.42]  At that point, we were investigating, like we had quite a lot of monitoring tools at the Financial Times.
[382.68 --> 387.86]  And I was like, and I was working in the team that provided monitoring as a service to other teams.
[387.86 --> 400.58]  And my head was going mad thinking, okay, how do I as a team with like four or five engineers be able to support like these 20, 30 odd engineering teams who all want monitoring?
[401.36 --> 412.40]  And they're using from Nagios to Zabig, some Graphite, some started, I think there were very few installations of Permitius at that point.
[412.40 --> 416.06]  And I was like, how do we get all of these different use cases together?
[416.06 --> 419.44]  And how do we get them on a platform which could work together?
[419.60 --> 422.64]  And it made me, like I was worried at that point.
[422.64 --> 426.62]  And like three years later or four years later, looking at it, it's like-
[426.62 --> 427.48]  You're still worried.
[427.64 --> 427.74]  No.
[428.06 --> 430.60]  I mean, I have moved on from the Financial Times.
[430.70 --> 434.58]  So I'm less worried about the Financial Times monitoring systems.
[434.58 --> 436.86]  But I still worry about like the same use case.
[436.86 --> 442.74]  I see it here as well in the Lego group where there's different monitoring tools that we've got across the organization.
[442.74 --> 444.62]  And it's how do we get them all together?
[444.62 --> 451.86]  And like, how do we say a single story that everyone could understand rather than every single team trying to solve the same problem?
[451.98 --> 458.92]  So it's still very similar, but probably we have better tools and like processes in place that can help us.
[459.00 --> 459.78]  So that's how I see it.
[460.12 --> 460.60]  Yeah.
[460.78 --> 465.80]  Something you said earlier stood out, this idea that you're like, why did you build it like this?
[465.80 --> 469.98]  If only you'd built it differently, we'd be in a much better position now.
[470.26 --> 471.84]  So it kind of like-
[471.84 --> 473.64]  If you only did it right, is that what you're saying?
[474.90 --> 475.34]  Yeah.
[475.38 --> 476.34]  But that's the question.
[476.34 --> 479.50]  Like, when should we start caring about this stuff?
[479.64 --> 482.98]  When should we start worrying about how are we going to operate this?
[484.02 --> 489.82]  I think this kind of relates to like how I've moved in the journey in my career and stuff.
[489.82 --> 500.64]  So I started off as a test engineer, just doing some manual testing, then moved on to doing more QA, like more quality related things rather than just testing.
[500.64 --> 517.02]  And over the years, I've seen the transition in a lot of organization as well, where they've moved to this shift left and test early, like release as small as possible and continuous iterations and stuff.
[517.02 --> 523.44]  So all of this, I think, kind of leads to that point of like, how do you make your future better?
[523.84 --> 528.42]  And one of the quotes I have often used is being kind to your future self.
[528.56 --> 531.96]  Like, how can you make your life easy in the future?
[532.08 --> 535.32]  So think about that today when you're building whatever you're building.
[535.32 --> 546.22]  And that comes with if you're building a new product, think about do you even have to build it or like can you just look at what's in the market and reuse it?
[546.30 --> 549.82]  If it's a non-differentiating thing, then why build it?
[549.94 --> 553.14]  If it is a differentiating thing, yes, put your heart and soul into it.
[553.14 --> 562.68]  But then when you're doing it, make sure you think about the sustainability aspects of your product and not just today what the customer would get.
[562.68 --> 575.80]  Yeah. And it's like I've often used this carrot and stick kind of approach in teams to show the benefits of what you could get out of thinking about monitoring observability from the front.
[575.80 --> 579.46]  And usually the carrots are like you build it in the right way.
[579.56 --> 584.30]  Then you don't have you can actually forget about your systems because they will take care of themselves.
[584.30 --> 598.96]  And the stick approach is often if you didn't do it, then you have to go into the rotors or like all of those other things that comes with like making your systems more observable and keeping it sustained once it's up and running and stuff.
[598.96 --> 604.82]  So, yeah, I think that's what I've used in the past to actually help teams nudge in that direction and stuff.
[605.00 --> 605.24]  So, yeah.
[605.24 --> 613.16]  Yeah. Yeah. I mean, you know, I would be kind to my future self, but I'm too busy dealing with all the stuff that my past self left me to do.
[613.68 --> 617.50]  So I don't know. But yeah, I think so that's the thing.
[617.58 --> 626.54]  If you think about how it's going to be, where it's going to be running, like the realities of that, if you think about that, the earlier, the better almost, isn't it?
[626.54 --> 639.68]  So, yeah, it is that. And it's also that, yes, you are fixing things from yesterday, but if you don't fix it and leave some goodies along with it, then you're fixing tomorrow.
[639.68 --> 642.90]  You're fixing today's problem. So you're still in that vicious cycle.
[643.34 --> 649.90]  So to get away from that vicious cycle, I think you need to actually step back sometimes and put that extra effort.
[649.90 --> 657.90]  I remember one of the tech principles we had in the Financial Times for FD.com was...
[657.90 --> 659.98]  I've forgotten this.
[661.04 --> 662.32]  It's okay. No, it's okay.
[662.70 --> 670.10]  As we're talking about, you know, like the past self and future self, is it okay that I've completely forgotten about observability and now I'm just on a personal journey?
[671.46 --> 677.86]  I'm thinking about all the decisions made and yet to make and how to provide goodies for everyone.
[677.86 --> 681.44]  So, Naina, or for me, I don't know. I forget that part.
[681.66 --> 690.86]  But, Naina, the carrot and stick, can I ask you, right, is there been a stick that you've seen people try to use that just didn't work, right?
[690.92 --> 700.10]  Or not didn't work, but either was too harsh or like just kind of like ill, you know, not ill-intentioned, but ill-executed?
[700.10 --> 706.48]  I think it's about the motivations and the motivation factor behind doing something.
[707.10 --> 708.84]  And that's how I saw the carrot and stick.
[709.22 --> 717.90]  So, the carrots were the motivation factors that we were providing to teams saying, if you did something right and if you thought about like how do you monitor something,
[717.90 --> 726.70]  how do you add alerts in place and how do you make sure it's auto-recoverable where possible and stuff, then you don't have to worry about it, right?
[726.80 --> 734.80]  So, that is more of the motivation for the team to be like, I don't, like I can be really proud about what I build and I don't have to think about it again.
[735.08 --> 744.92]  But at the same time, we know that every team has these deadlines to meet and like there are product owners who would have their own feature sets to build.
[744.92 --> 756.50]  So, it's that kind of scenarios where you actually still need the stick to help the teams be like, look, I mean, yes, we understand your pressures, but this is more important as well.
[756.88 --> 763.76]  And I did remember the quote and it was slow down to speed up, which actually like that was one of the tech principles we worked with.
[763.76 --> 776.74]  So, basically, yes, you can go at 100 miles per hour today, but then if you don't build it in such a way that you have put those measures in place, then tomorrow you have to break and stop.
[776.92 --> 783.46]  But if you slow down and went at, say, 60 miles per hour, you're there for the long run and you would go on longer.
[783.58 --> 786.60]  So, that's how I would see some of this now.
[786.60 --> 788.32]  Yeah, that is so true.
[788.58 --> 790.90]  We actually built a little project before Grafana.
[791.04 --> 803.74]  We built a project management tool called Pace and it was trying to get across that exact thing, which is that you feel great going at a thousand miles an hour, but you do have, you know, there's important things to do along the way.
[803.90 --> 806.42]  And it's hard to retrofit a lot of this stuff.
[806.72 --> 809.52]  So, it's, you know, thinking about it up front sometimes can save you.
[809.52 --> 812.98]  It's a bit like how you design for failure as well.
[813.28 --> 819.20]  Like, you know, in the perfect world, your system, all the messages flow perfectly and there's no problems.
[819.38 --> 821.94]  But in reality, it's way more messy.
[822.10 --> 822.86]  Things fail.
[823.32 --> 829.78]  And so, that idempotency and things come into play where you may design expecting this is going to fail.
[830.88 --> 836.70]  I write Go code and Go has error handling as a kind of explicit feature.
[836.70 --> 840.54]  They're values that are just returned as the second argument to functions and things like this.
[841.14 --> 845.96]  And that frustrates a lot of people because, you know, they're used to exceptions or something that's just sort of automatic.
[846.40 --> 851.24]  But it forces you to think about what's going to happen if this thing fails.
[851.70 --> 853.98]  And that's great discipline to get into.
[854.68 --> 858.10]  And I think it's a myth to think that your system won't fail.
[858.54 --> 858.76]  Yeah.
[858.92 --> 862.42]  Like, always build your system in such a way that it will fail.
[862.72 --> 864.66]  If it doesn't, then you have a problem.
[864.66 --> 865.30]  Yeah.
[866.10 --> 869.32]  So, make sure you add those checks in place.
[869.52 --> 872.98]  So, when it fails, it can smoothly recover and all of those.
[873.80 --> 874.04]  Yeah.
[874.36 --> 874.56]  Yeah.
[874.56 --> 882.40]  And I know some companies that have that as part of the proper sort of testing approach is they'll literally things will break on purpose.
[882.60 --> 885.32]  And, you know, it's a first class concern that they have.
[885.32 --> 890.20]  And it is that thing of, yeah, don't, you know, of course, like, I don't know.
[890.26 --> 894.40]  Is it just ego that people think I'm so good, I'll write this, it's going to be great?
[894.60 --> 895.22]  What's going on?
[895.32 --> 896.20]  It can't be.
[896.52 --> 897.68]  Honestly, it can't be, right?
[897.70 --> 901.10]  Like, we've all known and experienced it enough.
[901.34 --> 901.60]  Yeah.
[901.72 --> 902.16]  Do you think?
[902.16 --> 902.68]  I don't know.
[902.72 --> 911.40]  But the thing is, when I'm writing code and it doesn't work, it's shocking how quickly I'm like, there's something wrong with the processor.
[912.32 --> 914.92]  The processor is not working.
[915.06 --> 916.12]  Or physics has changed.
[916.56 --> 919.58]  That's why I'll go to physics has changed before it's my fault.
[920.06 --> 922.68]  But it turns out I just did a capital letter where I shouldn't have.
[922.68 --> 929.64]  I think, like, I've been in teams where they do pairing and, like, those mobbing sessions and stuff.
[929.88 --> 938.20]  And, like, they have kind of helped in, like, sense-checking people's egos a bit and be like, I'm not the best.
[939.00 --> 944.70]  And when two people talk about it, I think it does help think, okay, there is a reality that we live in.
[944.86 --> 946.84]  And this is what you need to consider.
[946.84 --> 962.72]  Is there anything that you would, like, even in that, like you were saying before, that progression between, like, being in, you know, manual testing and then QA and then moving to SRE, was there any, was there, like, a moment where it clicked, where people started, I mean, they just started incorporating testing into the code, right?
[962.76 --> 971.88]  Do you see the same progression happening in observability to where there'll be some moment and some kind of click where it just becomes part of it as opposed to the separate thing that happens afterwards?
[971.88 --> 974.34]  I have seen it work in some teams.
[974.54 --> 978.02]  And, like, a lot of teams I've worked in are all autonomous teams.
[978.16 --> 982.68]  So, they can basically build however they want using whatever technologies they want.
[983.12 --> 995.58]  What is often have teams like that is having some sort of guardrails, which actually says, and, like, also being aware that not all applications need the same level of checks and monitoring and all of these.
[995.58 --> 999.36]  So, being aware that, okay, there is a level of criticality of my app.
[999.54 --> 1003.44]  And if it is a highly critical app, then let me put all of the things in.
[1003.84 --> 1010.60]  And if it is a less critical app, in that case, you would just have, like, maybe just a simple health check.
[1010.70 --> 1011.60]  That would be good enough.
[1011.68 --> 1013.50]  You don't need to go all board.
[1013.50 --> 1022.90]  And one thing that we had when I was working for FT was you always have at least a basic check on all your apps.
[1023.24 --> 1028.56]  Otherwise, like, we used to get this service operability score for our applications.
[1028.88 --> 1033.72]  And the score used to go down as in when we didn't have some of these things in place.
[1034.08 --> 1040.96]  And that was, like, a nice measure where people thought about it from the beginning rather than as an afterthought about some of these.
[1040.96 --> 1049.94]  But what could happen in this kind of scenarios is people go all in and they just say, oh, I'm going to monitor everything, have all my logs go in.
[1050.10 --> 1052.46]  Like, you don't need to go all board on this.
[1052.56 --> 1055.14]  There's a limit to how much you need to monitor as well.
[1055.30 --> 1063.00]  And understanding the criticality of your app and then building your observability around that is probably something that teams should think about.
[1063.00 --> 1073.86]  How would you, if a team was listening to this, right, and they were trying to understand the criticality of the app and make decisions around it, like, how would you, if you had them sitting in the room, how would you explain it and say, here, start here, do this?
[1073.86 --> 1076.56]  I think it depends on the business criticality.
[1076.84 --> 1086.24]  And if it is a highly business critical application, which means if it went down for, say, more than 15 minutes, then we wouldn't be in business.
[1086.24 --> 1100.46]  If it's that kind of app, then you need to have your alerting in place, monitoring, like, the right level of logging in place, which actually gives us any of the audit records that actually show us what's happened with the applications.
[1101.32 --> 1104.10]  And then any sort of health check.
[1104.16 --> 1108.08]  So there's probably, like, two levels of monitoring that we should think about.
[1108.18 --> 1109.76]  One is the application level monitoring.
[1109.76 --> 1111.96]  And then there is the system level monitoring.
[1112.16 --> 1120.04]  So being able to figure out where the problem is soon enough is something very critical when it's a 15 minutes recovery thing.
[1120.30 --> 1132.34]  But if it is an application that's less critical, then maybe just having the application level monitoring is good enough where you could take longer to actually investigate, look into the locks and actually figure out where the problem area is and stuff.
[1132.34 --> 1137.66]  So I would suggest teams to think about, like, how critical their app is.
[1137.76 --> 1143.50]  And that is something the business should, like, help them with, not something that the team just decides, oh, this is the most critical thing.
[1143.92 --> 1155.60]  And once you know the business criticality of something, then it is coming up with some sort of check saying if it is a highly critical system, then we do both application as well as system monitoring.
[1156.08 --> 1159.12]  Otherwise, just one of them based on your use cases and stuff.
[1159.12 --> 1166.40]  And, like, in the past, I've spoken about, like, the use method and red method that we could use for these kind of things.
[1166.68 --> 1171.02]  Like, I prefer use and red method over the Google's four signals.
[1171.18 --> 1176.20]  It depends on what your team's needs are and what fits into your use cases.
[1176.84 --> 1183.22]  So you would use a red method, which is rate, error, and duration for every single application that you build.
[1183.22 --> 1188.72]  And it's very easy to see that in a microservice world where you have different kinds of applications.
[1189.38 --> 1192.84]  You have the same three parameters that you're measuring across all of them.
[1192.96 --> 1199.62]  So it actually helps the team analyze irrespective of if that belongs to your team or any other team.
[1199.70 --> 1201.10]  You just know where the problem is.
[1201.46 --> 1203.82]  And the same with systems side of things.
[1203.82 --> 1208.40]  You would go with, like, the use method, which is utilization, saturation, and errors.
[1208.86 --> 1213.86]  And you would do this for the CPU, disk, or network, and all of those different areas.
[1214.06 --> 1216.82]  And you basically know where the problem is.
[1216.86 --> 1218.06]  And it's easy to find out.
[1218.40 --> 1220.24]  I would say it is hard.
[1220.44 --> 1221.68]  It takes time.
[1221.98 --> 1226.96]  So invest based on how much returns you would get on these when you put these checks in.
[1226.96 --> 1233.96]  So that is something the team should be mindful about when they are investing in monitoring or, like, learning and stuff.
[1234.88 --> 1239.90]  Is the primary counterbalance, in your mind, the effort that it takes to keep this monitored well?
[1240.00 --> 1240.88]  Or is it also cost?
[1241.06 --> 1243.88]  Do you think about the cost to operate or the back end?
[1244.52 --> 1245.74]  It is the cost.
[1246.00 --> 1248.72]  And at the end of the day, it should be the cost to the business.
[1248.72 --> 1253.22]  As in, how much does having the system down cost us?
[1253.70 --> 1260.80]  And you basically work backwards from there, saying, if this was down for 15 minutes, it would cost the business so much.
[1260.88 --> 1271.34]  Which means we, as a team, should be investing more time in actually getting the right amount of measures so we can solve the problem or narrow down the problem quickly.
[1271.34 --> 1278.98]  And, like, I would always focus on the business value rather than the team's individual product value and stuff.
[1279.44 --> 1287.52]  But, yeah, it depends on, like, if you were an internal system, like, in one of the teams I was in, we were building monitoring tools for other teams.
[1287.72 --> 1291.68]  So we don't have real business value as such as our team.
[1291.88 --> 1296.76]  But we were supporting teams that had, like, really high value systems.
[1296.76 --> 1304.68]  So that kind of meant that we had to think about the application level as well as system level monitoring on our systems and stuff.
[1308.98 --> 1312.98]  This episode is brought to you by our friends at FireHydrant.
[1313.26 --> 1316.04]  FireHydrant is the reliability platform for every developer.
[1316.46 --> 1320.24]  Incidents, they impact everyone, not just SREs.
[1320.40 --> 1325.98]  They give teams the tools to maintain service catalogs, respond to incidents, communicate through status pages,
[1325.98 --> 1328.14]  and learn with retrospectives.
[1328.50 --> 1333.90]  What would normally be manual error-prone tasks across the entire spectrum are responding to an incident.
[1334.18 --> 1337.36]  They can all be automated in every way with FireHydrant.
[1337.66 --> 1342.74]  They have incident tooling to manage incidents of any type with any severity with consistency.
[1343.28 --> 1346.42]  Declare and mitigate incidents all from inside Slack.
[1346.80 --> 1349.82]  Service catalogs allow service owners to improve operational maturity
[1349.82 --> 1353.12]  and document all your deploys in your service catalog.
[1353.12 --> 1359.36]  Incident analytics allow you to extract meaningful insights about your reliability over any facet of your incident
[1359.36 --> 1361.08]  or the people who respond to them.
[1361.48 --> 1365.40]  And at the heart of it all, incident runbooks, they let you create custom automation rules,
[1365.64 --> 1370.86]  convert manual tasks into automated, reliable, repeatable sequences that run when you want.
[1371.22 --> 1375.24]  You can create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1375.74 --> 1378.32]  Now your processes can be consistent and automatic.
[1378.32 --> 1380.46]  The next step is to try it free.
[1380.60 --> 1384.96]  Small teams, up to 10 people, can get started for free with all FireHydrant features included.
[1385.30 --> 1386.70]  No credit card is required.
[1387.16 --> 1389.30]  Get started at firehydrant.io.
[1389.68 --> 1391.62]  Again, firehydrant.io.
[1391.62 --> 1406.90]  I love that advice of pay attention to the value you're going to get from the effort that you put in.
[1407.34 --> 1409.20]  When I, I like mono repos.
[1409.34 --> 1410.76]  I just like to put that out there.
[1410.82 --> 1411.70]  I love mono repos.
[1411.70 --> 1417.60]  And the reason I like them is because you can have a pull request that has a unit test, some back-end code,
[1417.72 --> 1423.36]  maybe some API changes, front-end code in there too, hopefully with some front-end tests maybe.
[1423.74 --> 1427.26]  And it's nice that that all gets applied to the system in one go.
[1427.60 --> 1432.08]  Does that also apply to like this sort of field or the instrumentation of that?
[1432.20 --> 1438.20]  Should we be having those kinds of conversations at that point so that we kind of think about it as we go?
[1438.20 --> 1442.96]  I would love to say yes, but I've not seen a team do it really well.
[1443.22 --> 1450.84]  So I can see the challenges of like when you have this mono repo and everyone's contributing to the same central repository,
[1451.22 --> 1458.54]  there is a challenge that the parameters that you would think about for your product and your monitoring systems
[1458.54 --> 1462.00]  might be different to what another team would be looking at.
[1462.00 --> 1469.38]  So there is a challenge with how do you then look at this as a product that we sell to customers?
[1469.72 --> 1475.14]  Like you have to think about capability monitoring maybe rather than your individual product monitoring
[1475.14 --> 1479.52]  where you're thinking about what is the capability that I'm providing to the customer?
[1480.18 --> 1484.14]  And those should probably be things that we have at a central level.
[1484.28 --> 1487.24]  And we do it as in when we add new features,
[1487.24 --> 1491.34]  we make sure we don't break the monitoring that we've got across the capability.
[1491.34 --> 1497.80]  But on a single individual product team's perspective, yeah, I don't know how much value it would add.
[1497.90 --> 1499.12]  So it depends on that, I guess.
[1499.40 --> 1500.76]  So yeah, I'm sure.
[1501.14 --> 1504.26]  Have you seen it work in your teams or something?
[1504.90 --> 1509.30]  Well, we have at least the conversation when there's a PR for like a big feature,
[1509.92 --> 1514.56]  we will chat about it and say like, what do we need?
[1514.64 --> 1515.64]  What do we need from this?
[1515.64 --> 1519.18]  It's like, what's going on here that later we're going to need?
[1519.38 --> 1521.56]  And it's that thing about becoming your future selves.
[1522.20 --> 1527.12]  So yeah, but I don't know that we've got that right yet or anything, you know,
[1527.20 --> 1531.54]  because in a way we don't really know what's important upfront necessarily.
[1531.82 --> 1534.32]  So it's, you know, but sometimes you do.
[1534.38 --> 1538.64]  And I like that there are guidelines that we can follow to give us a good foundation.
[1538.64 --> 1541.96]  And then, of course, we're going to have to fine tune it depending on our particular case.
[1542.36 --> 1542.70]  I agree.
[1543.02 --> 1543.18]  Yeah.
[1543.92 --> 1547.44]  All this, to me, starts to distill down into, right?
[1547.50 --> 1551.66]  Like it's some amount of like, if you are doing the centralized monitoring, right?
[1551.66 --> 1553.06]  Or there's a level of that, right?
[1553.10 --> 1557.72]  And then you have to communicate this down to these teams and you have to get them to buy in, right?
[1558.56 --> 1559.88]  You know, what do you do that?
[1559.96 --> 1562.58]  Or even how would you suggest someone else do that well?
[1562.58 --> 1570.34]  So central teams pushing things is like, irrespective of it being monitoring or anything in general is really hard.
[1570.84 --> 1579.58]  And it should always be driven by, like what I've seen work really well is the ones that are driven by like value add to the individual teams itself.
[1580.14 --> 1590.14]  So as an example, when we were building this Amazon Linux, like a base plate image that everyone could apply and they can run their own EC2 instances.
[1590.14 --> 1599.66]  When they had this, what we said we will do as part of it is we said you're going to get monitoring to like, I think we were pushing logs to Splunk in that case.
[1599.74 --> 1601.72]  So you would get that feature for free.
[1601.86 --> 1603.60]  You would get authentication for free.
[1603.76 --> 1610.74]  You would get like, have those kind of things that you will get for free as part of whatever features that you would give.
[1610.96 --> 1616.34]  And that has often been a nice way to drive teams to be like, oh, yes, I like that.
[1616.52 --> 1617.32]  And I will do it.
[1617.48 --> 1617.52]  Right.
[1617.52 --> 1621.68]  Make it so easy that they can't, like they would rather adopt it rather than try and do it themselves.
[1621.94 --> 1622.78]  Yeah, exactly.
[1622.98 --> 1632.98]  So like another example that came to mind was we had this central repository for like a CRM system, which we had to enter all of our system information.
[1632.98 --> 1642.88]  And basically it was like a, because we had so many microservices, we had like a central system where we could go and query for any particular system with something called as a system code.
[1643.08 --> 1649.46]  And we would know if that system was live, was active, who was working on it, all of those information.
[1649.46 --> 1660.58]  And what we did when we built this was we said, if you put the right information in this, then you would automatically have a dashboard that would show up only your teams monitoring in it.
[1660.74 --> 1666.56]  That was like an incentive for teams to be like, oh, if I did this, then I get my own dashboard.
[1666.76 --> 1667.30]  Let me do that.
[1667.30 --> 1673.82]  So I think it's that showing intensive value beyond just what you want them to achieve out of it.
[1673.94 --> 1676.64]  That's how I've seen it work really well in teams.
[1676.94 --> 1683.70]  So yeah, you need to have some sort of courage to actually get people to move towards your solutions and stuff.
[1683.92 --> 1684.02]  Yeah.
[1684.20 --> 1684.40]  Yeah.
[1684.40 --> 1684.44]  Yeah.
[1685.06 --> 1685.34]  Yeah.
[1685.34 --> 1685.82]  That's great.
[1685.92 --> 1687.94]  I think that applies to everything.
[1690.02 --> 1690.42]  Yeah.
[1690.48 --> 1693.56]  If you make it easy and it's sort of a no brainer.
[1693.56 --> 1705.72]  And like one example of that is where we can, like, if we've got APIs, we can just instrument on those, on the endpoints very easily in a simple way, usually with some middleware or something in the code.
[1705.88 --> 1708.02]  And there's lots of packages that do this.
[1708.32 --> 1714.28]  So I do quite like, yeah, I think, and I think there's probably space for more things like that.
[1715.02 --> 1717.28]  More of that for devs.
[1717.48 --> 1718.04]  Yeah.
[1718.18 --> 1730.16]  And I think it's the, like, I would really, like, want to see central teams be more mindful about this because as a central team, you're building these amazing tools.
[1730.76 --> 1737.66]  And at the end of it, like, you kind of think, oh, if I put a documentation together and self-service, everyone's going to come and use it.
[1737.66 --> 1748.26]  But then each individual product teams have their own little agendas to work towards and their own, like, the product initiatives to their own OKRs, all of those things.
[1748.26 --> 1761.72]  So this is like an extra bit of, like, cognitive load onto those teams, which they can avoid if you were to do a lot more promotion within teams saying, if you did this, you would get a lot of benefits.
[1761.72 --> 1765.72]  And it will take some of the risks that you have taken on yourself.
[1765.94 --> 1769.84]  And also it's that education piece of you care about your product.
[1770.04 --> 1772.08]  We will help you care about your product.
[1772.20 --> 1774.06]  That's something to think about.
[1774.06 --> 1775.24]  Yeah.
[1776.96 --> 1783.84]  So what are some common mistakes that we make when we're trying to do this with the best intentions in the world?
[1783.96 --> 1792.18]  We want to do this properly, but are there any things you see that people misunderstand or common mistakes, common gotchas that you've seen?
[1792.78 --> 1803.16]  I think it's knowing how much is enough is, like, one of the things that I've often seen where there are teams who just put the basic thing available because it's there in a checklist somewhere.
[1803.16 --> 1807.30]  And then they move on, which is probably not the best for your product.
[1807.30 --> 1817.56]  So it's being aware of the value of your product and, like, what is the life cycle that your product or the journey that your product is going on?
[1817.66 --> 1819.30]  That is probably one of the things.
[1819.64 --> 1828.08]  The other thing that I have seen and I've struggled a lot with is, like I mentioned about this use method and red method to actually build your dashboards.
[1828.34 --> 1832.94]  It's very hard to get, like, your network-related monitoring right.
[1832.94 --> 1836.24]  And your saturation for networks.
[1836.40 --> 1837.72]  Like, how do you do that?
[1838.12 --> 1852.84]  And get the wrong set of, like, I've seen myself having a wrong set of dashboards and alerting and wondering why this is going off every time something happens when it shouldn't have and stuff.
[1852.84 --> 1869.62]  So I think it's just, like, being okay to experiment and, like, continuously tinker your monitoring and alerting as you go along is probably something that teams should be conscious that, like, it's not that you build it once and then it's there.
[1869.70 --> 1870.34]  It's there forever.
[1870.72 --> 1873.94]  But there is a continuous evolution that happens with your monitoring.
[1873.94 --> 1877.18]  Like how your feature sets go through that cycle.
[1877.52 --> 1881.76]  You have to do the same with your observability side of things as well.
[1882.34 --> 1882.72]  Yeah, yeah.
[1883.02 --> 1884.52]  Matt, can I answer too?
[1885.16 --> 1886.04]  Let me just check.
[1886.74 --> 1886.96]  No.
[1887.66 --> 1888.54]  Oh, come on.
[1888.84 --> 1891.70]  Brutal, but please, I'd love to hear what you think.
[1891.70 --> 1897.54]  So, but, Niana, you were talking about the value, like, derived, right, and focusing on that for the customers.
[1897.76 --> 1903.44]  That I do think that's a common gotcha where you build all these tools and you're like, we did it.
[1903.52 --> 1904.00]  We did it.
[1904.04 --> 1904.78]  Like, it's all there.
[1904.92 --> 1906.12]  All you have to do is this, right?
[1906.16 --> 1911.82]  And I think the common gotcha is forgetting that you need to deliver something that someone could just adopt easily.
[1911.90 --> 1916.54]  Like you said, like, it is a version of, I was thinking, like, car parts, right?
[1916.54 --> 1921.86]  And then, like, or Legos, I guess, but, like, dropping off, like, a collection of car parts and being like, there you go.
[1922.20 --> 1925.30]  And you're like, you know, like, I want to drive, right?
[1925.30 --> 1929.02]  Like, I don't, like, I get that I can get there, but you haven't helped me really at all.
[1929.38 --> 1932.58]  And there's, you know, and you call a Lyft and that's where the metaphor, I think, breaks.
[1932.88 --> 1936.26]  But I do think there's some version of that too, right?
[1936.28 --> 1945.94]  Like stopping short of actually delivering the value to the person consuming it as opposed to just dropping a collection of pieces that can work, but they have to do the last mile.
[1945.94 --> 1951.30]  Yeah, well, in a way, what helps that definitely is going to be this, you build it, you run it.
[1951.44 --> 1958.92]  You know, we're not throwing this thing over the wall to someone, for someone else to operate, which I know that actually lots of, lots of people do still do that.
[1959.14 --> 1960.58]  And there's a disconnect.
[1961.02 --> 1965.98]  When you are yourselves kind of running it, you're the customer of that data.
[1966.20 --> 1973.22]  So a bit like when you're dogfooding software, if you write, if you're building dev tools, like we do at Grafana, we dogfood a lot.
[1973.22 --> 1975.46]  Like we'll use our tools a lot internally.
[1975.46 --> 1981.96]  That's how they're so good, frankly, like, because they've been, you know, it's not like we're imagining the user of this.
[1982.32 --> 1983.46]  We are the user of it.
[1983.50 --> 1985.40]  And I think that makes a big difference, doesn't it?
[1985.80 --> 1986.00]  Yeah.
[1986.22 --> 1994.30]  And also, I think like one of the comments I've heard a few people say about is build your code in such a way that you can debug it at three in the morning.
[1994.30 --> 1997.16]  I mean, it doesn't mean that you have to do it every day.
[1997.36 --> 2003.78]  But if it breaks at a time that you're not fully in focus, you still can get to it easily.
[2004.06 --> 2009.58]  And that is something which I think, yeah, people should be thinking about while building the products and stuff.
[2009.58 --> 2012.72]  That's such a great point, I think.
[2012.96 --> 2017.02]  And that leads me on to this next question, which is around like drills.
[2017.40 --> 2024.38]  Do we should we be doing like drills at 3 a.m. and living that experience to see what it's like?
[2024.52 --> 2028.08]  Three o'clock is probably taking the mickey out of people if you were doing drills.
[2028.08 --> 2031.24]  Do people do drills?
[2031.72 --> 2032.68]  I guess they do.
[2033.10 --> 2033.24]  Right.
[2033.32 --> 2034.04]  But it's probably not.
[2034.12 --> 2035.36]  It's not common, is it?
[2035.82 --> 2037.00]  I have seen it done.
[2037.96 --> 2041.96]  And I think it's a very artificial environment where the drills happen.
[2041.96 --> 2047.10]  So one of the things that we did when I was at the FT was we had this incident drills.
[2047.64 --> 2051.80]  So basically, you emulate an incident and then you go about with the team.
[2052.18 --> 2055.28]  How do you go about actually figuring out where the problem is?
[2055.28 --> 2062.38]  So you start with like which alert it was and then look at the traces and then look at what the logs were.
[2062.52 --> 2064.22]  And you go through the whole cycle of it.
[2064.54 --> 2070.80]  It was a way to like ease the whole out of our support that we had within the organization.
[2071.34 --> 2071.70]  Yeah.
[2071.76 --> 2075.24]  But at the same time, there were a lot of people who were not very keen of this.
[2075.82 --> 2080.26]  Because it's an artificial environment, people felt like that is not reality.
[2080.44 --> 2081.64]  So why do it?
[2081.70 --> 2083.02]  That's because you didn't do it 3 a.m.
[2083.02 --> 2085.34]  Yeah, maybe that.
[2085.86 --> 2089.14]  I think there's like a touch of maturity in actually embracing drills.
[2089.24 --> 2090.84]  Like whether or not it's artificial, right?
[2090.86 --> 2093.12]  Like it's that idea like, oh, this is artificial.
[2093.32 --> 2093.84]  This is dumb.
[2094.10 --> 2094.82]  You know, we don't want to do this.
[2094.84 --> 2095.92]  It's not going to be like this in real life.
[2096.04 --> 2103.20]  And then I think like you think about any kind of, I don't know, like either team environment or any kind of like practice that you need to do.
[2103.20 --> 2105.64]  Because it's more than just debugging the code, right?
[2105.66 --> 2107.56]  It's like everything is interconnected, right?
[2107.56 --> 2111.74]  And you want to be able to do some of these things more than once.
[2111.80 --> 2114.06]  So that way every time doesn't feel like you're the first time on stage.
[2114.70 --> 2121.76]  And it does, it feels like you just want to be like, hey, like what's the right analogy to make if you want to convince someone to actually practice?
[2122.52 --> 2123.18]  I don't know.
[2123.18 --> 2124.22]  Yeah, definitely.
[2124.46 --> 2125.64]  It's not the same.
[2125.84 --> 2128.26]  It's not the same because you know it's a drill.
[2128.60 --> 2135.46]  Like unless you're doing something where you literally, you break something and it's not really broken or maybe it is.
[2135.54 --> 2138.26]  And you're, you know, doing something kind of, that seems a bit extreme.
[2138.46 --> 2140.86]  But you are, it is going to feel different.
[2141.04 --> 2144.68]  But that still doesn't mean that there's not plenty of stuff to practice.
[2144.68 --> 2151.50]  And, you know, like practicing your, when you practice driving, you know, there's an instructor next to you watching everything.
[2151.64 --> 2155.10]  That's a very strange situation to be in.
[2155.24 --> 2161.04]  But, but you still are like, you still move the steering wheel and do the, I don't drive, but there's a gear stick.
[2161.18 --> 2161.52]  I know that.
[2161.74 --> 2162.68]  And the horn.
[2164.02 --> 2165.28]  You press the horn to go.
[2165.54 --> 2165.94]  Yeah.
[2166.06 --> 2166.76]  Horn to go.
[2166.82 --> 2167.92]  And then you leave that on.
[2168.00 --> 2169.02]  So everyone knows you're there.
[2169.10 --> 2171.88]  I do because they need to get out of the way.
[2171.88 --> 2176.58]  I think there's also like value in like this.
[2176.84 --> 2179.56]  The other way of looking at drills is like shadowing.
[2179.76 --> 2185.36]  And when there's an actual incident, not, not having just one or two people involved in it.
[2185.44 --> 2192.36]  Yes, it might be the most critical thing, but having more people just listen in and see what's happening and like just be there.
[2192.70 --> 2198.02]  Sometimes helps them understand, oh, this is how I would go about solving this, looking at those people.
[2198.02 --> 2203.58]  So, yeah, I think it's, it's a mixture of drills and a shadowing maybe that could work in teams.
[2204.06 --> 2207.94]  I even think yesterday, and I realized why I'm all fired up about this.
[2208.14 --> 2209.10]  I parsed through it.
[2210.02 --> 2216.36]  Yesterday we did, I visited the sales team and they were doing these workshops and they were doing radical candor, right?
[2216.36 --> 2221.40]  Which is like all about like feedback and giving feedback and getting feedback and, and being able to, to do it well.
[2221.40 --> 2224.06]  And then you break out and you're like, okay, yeah, check, check, check.
[2224.12 --> 2224.42]  I get it.
[2224.42 --> 2224.78]  I get it.
[2224.84 --> 2225.10]  I get it.
[2225.12 --> 2226.06]  Like I could totally do that.
[2226.22 --> 2229.88]  And then you break out into these triads and then you practice it, right?
[2229.92 --> 2233.16]  And there's a part of you that goes like, oh, I don't, I don't need to do this.
[2233.16 --> 2233.92]  Like I get it.
[2233.92 --> 2234.52]  I get the concepts.
[2234.58 --> 2242.16]  And then you try and do it and you're like, and you kind of feel yourself like places that, you know, are a little bit creaky or, you know, maybe you don't quite get it as much.
[2242.16 --> 2246.30]  So I think, I think it's actually where I'm fired up to where, even if it is artificial, right?
[2246.34 --> 2253.08]  Some of those, some of those joints might be, you know, either rusty or creaky or, or don't articulate well until, and you don't realize that until you do it.
[2253.36 --> 2255.34]  I think that was a rubbish point.
[2256.32 --> 2257.50]  We can cut that.
[2257.64 --> 2258.28]  Cut, cut, cut.
[2259.22 --> 2264.82]  I think it's also like a good exercise to do just to test your like documentation and stuff.
[2264.82 --> 2276.28]  And like, if it's, if your documentation is up to scratch and like, when you've written something you've written with, with good intent, but when someone's actually following it, does it make sense?
[2276.28 --> 2279.52]  Is something that the drills can actually capture and stuff.
[2279.80 --> 2283.14]  So yeah, there's more than one benefit of having drills.
[2288.50 --> 2291.34]  This episode is brought to you by Honeycomb.
[2291.50 --> 2293.28]  Find your most perplexing application issues.
[2293.28 --> 2301.06]  Honeycomb is a fast analysis tool that reveals the truth about every aspect of your application in production.
[2301.52 --> 2305.52]  Find out how users experience your code in complex and unpredictable environments.
[2305.80 --> 2310.72]  Find patterns and outliers across billions of rows of data and definitively solve your problems.
[2311.16 --> 2312.64]  And we use Honeycomb here at Change.
[2312.68 --> 2316.50]  Well, that's why we welcome the opportunity to add them as one of our infrastructure partners.
[2316.50 --> 2324.34]  In particular, we use Honeycomb to track down CDN issues recently, which we talked about at length on the Kaizen edition of the Ship It podcast.
[2324.58 --> 2325.28]  So check that out.
[2325.50 --> 2325.98]  Here's the thing.
[2326.22 --> 2329.48]  Teams who don't use Honeycomb are forced to find the needle in the haystack.
[2329.60 --> 2332.76]  They scroll through endless dashboards playing whack-a-mole.
[2332.98 --> 2336.02]  They deal with alert floods, trying to guess which one matters.
[2336.02 --> 2341.62]  And they go from tool to tool to tool playing sleuth, trying to figure out how all the puzzle pieces fit together.
[2342.02 --> 2348.28]  It's this context switching and tool sprawl that are slowly killing teams' effectiveness and ultimately hindering their business.
[2348.68 --> 2355.44]  With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business.
[2355.70 --> 2356.12]  Production.
[2356.66 --> 2359.10]  With Honeycomb, you guess less and you know more.
[2359.10 --> 2364.70]  Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[2364.86 --> 2368.34]  Again, honeycomb.io slash changelog.
[2368.78 --> 2375.30]  And by Acuity, a new platform that brings fully managed Argo CD and enterprise services to the cloud or on-premise.
[2375.62 --> 2380.48]  The platform is a versatile Kubernetes operator for handling cluster deployments the GitOps way.
[2380.80 --> 2384.32]  And I'm here with Kelsey Hightower, angel investor and advisor to Acuity.
[2384.82 --> 2388.54]  Kelsey, why are you excited about Argo CD and what's happening here with Acuity?
[2388.54 --> 2395.62]  When I think about Argo CD, it represents the transition from traditional CICD.
[2395.78 --> 2399.82]  You know, you have a big server with a built-in workflow engine.
[2400.28 --> 2406.36]  And you can only do what that system can do, whether it's Jenkins, whether it's Spinnaker, you name it.
[2406.62 --> 2408.76]  Those things tend to be all-in solutions.
[2409.08 --> 2414.78]  And they're all predicated on having like their own built-in workflows, UIs, and ways of doing things.
[2414.78 --> 2427.06]  And then when I think about kind of the Argo CD, that whole open source movement kind of backed by the ideas we saw in the Kubernetes world, which was each of those steps is nothing more than just a step in a workflow.
[2427.36 --> 2431.54]  And after 10, 20 years of doing CICD, how best to represent those steps?
[2431.54 --> 2439.54]  And it turns out this whole container thing is probably the best way to have little snippets of logic sit at each of those steps in the workflow.
[2439.54 --> 2443.46]  And then you can kind of exchange them and share them to build any pipeline you want.
[2443.72 --> 2447.98]  So the way to look at this is Kubernetes has never had a workflow engine or tool.
[2447.98 --> 2457.94]  And so when you think about kind of Argo workflow or Argo CD, which is kind of a specialized workflow, kind of attacking the how do you roll out software problem, that's the way I would think about it.
[2457.98 --> 2463.82]  So if you're all in on Kube and you like the Kubernetes ecosystem, then you kind of have a choice of workload types.
[2463.96 --> 2467.18]  And I would probably just say it's another workload type you can put in your toolbox.
[2467.18 --> 2474.58]  So if you've got something that can benefit from a workflow engine and reuse the logic that you already have in containers, it kind of feels like the perfect fit.
[2475.00 --> 2475.56]  The perfect fit.
[2475.64 --> 2475.92]  All right.
[2475.98 --> 2476.46]  Thanks, Kelsey.
[2476.46 --> 2480.60]  Well, the next step is to head to Acuity.io slash changelog.
[2480.68 --> 2483.30]  They are inviting all of our listeners to join the closed beta.
[2483.84 --> 2486.32]  Again, Acuity.io slash changelog.
[2486.46 --> 2487.94]  Links are in the show notes.
[2499.38 --> 2506.24]  Niana, you mentioned earlier, like this idea that, you know, if you do too much, you can overdo it.
[2506.24 --> 2510.14]  And end up with basically alert fatigue, just alerts going off.
[2510.20 --> 2512.26]  What do we mean really by alert fatigue?
[2512.46 --> 2515.18]  I'm going to give an example so people can relate to it.
[2515.18 --> 2522.22]  I was in one of the teams where we used to get close to 1500 alerts on a weekly basis.
[2522.22 --> 2528.44]  And this was like we had around 80 odd microservices.
[2528.44 --> 2530.62]  So it wasn't like just one microservice or anything.
[2531.12 --> 2534.30]  But then my team was like three people looking at this.
[2534.78 --> 2543.58]  And it's at that point which you realize that are they actually looking at this thing or is it all just being ignored as like just noise?
[2543.58 --> 2544.72]  Let's just ignore it.
[2544.86 --> 2553.20]  And I think it's that point where you start ignoring your alerts is where you've gone to that stage where you can't take any more alerts.
[2553.32 --> 2555.92]  So you're fatigued with the whole alerting itself.
[2555.92 --> 2565.32]  And I think it's better to have less alerts for the most important things rather than have too many and try to just like filter it out.
[2565.46 --> 2575.14]  One of the exercises we did when we had these alert fatigues and like thousand odd alerts is we consciously stopped some of the alerts to see who will start shouting.
[2575.14 --> 2581.30]  And it happened that more than 50% of these alerts when we turned off, no one actually shouted at us.
[2581.38 --> 2583.32]  So it was like, was that even important?
[2583.68 --> 2593.44]  Going through that exercise on a regular basis where you see if you're ignoring more than at least 10% of your alerts, then go and do something about it.
[2593.64 --> 2595.74]  Maybe turn them off and no one will care.
[2595.74 --> 2610.20]  And I think teams need to be conscious that it's okay to miss a faulty alert compared to missing out on a real alert, which would have cost us like millions of pounds or whatever it is.
[2610.40 --> 2622.94]  So I think it's being careful to put the right alerts in and stopping at that and not just going overboard with, oh, let's take an example that we have Grafana in our systems and we have alerting with Grafana.
[2622.94 --> 2630.60]  I have this tool so I can put as many alerts as possible, not going wild with it, but actually like knowing where to stop.
[2630.84 --> 2633.30]  That's how I would describe this whole alert fatigue.
[2633.52 --> 2636.20]  And it's with time, it does happen with teams.
[2636.20 --> 2644.50]  So it's worth going back and auditing them and making sure you keep them clean as much as possible.
[2645.44 --> 2650.26]  I wonder if you could do a, like what would be like the equivalent of a bug bounty for alerts?
[2650.26 --> 2655.76]  Like how do you incent people to go and clean those up and celebrate being like, they're gone?
[2656.24 --> 2657.32]  Oh, that's hard.
[2657.54 --> 2662.36]  What I've done in this is actually gone and turned them off myself and be like, let's see who's going to shout.
[2663.74 --> 2667.30]  And like when no one shouts, you know that they're not important enough.
[2667.40 --> 2672.10]  So that is something that I've done, but I don't know how you would, interesting.
[2672.24 --> 2673.16]  Do you have any ideas?
[2673.54 --> 2677.46]  We need some analytics, don't we, on the usage of it really?
[2677.46 --> 2684.74]  Then we can say, you know, no one's looked at these alerts for ages, you know, or you could put a specific time on it if you want.
[2684.84 --> 2686.82]  I don't know, I don't want to design the application now.
[2686.94 --> 2688.16]  But yeah, something like that.
[2688.22 --> 2695.18]  I mean, I like the idea that you should go back and look at them and pay attention to whether you still need them and things.
[2695.24 --> 2703.62]  This is a little bit like how in GitHub, like, or in your project management tool, if you have loads of stuff in there, most of it's just getting ignored.
[2703.62 --> 2714.76]  And in a way, it creates this also this idea that you're so far away from being done, which we of course are, but you don't, you know, it sort of reinforces that.
[2714.90 --> 2718.88]  So it is that thing of if there's just so much there, it stops being useful.
[2719.20 --> 2725.18]  I like the idea that, does it take experience though, do you think, to know what's useful, what's not?
[2725.18 --> 2725.90]  Does that?
[2726.14 --> 2727.00]  It could do.
[2727.24 --> 2732.88]  I mean, the more you see these things, you will realize where it's important, where it's useful and where not.
[2733.18 --> 2742.88]  And this is where I've seen some of the junior engineers and teams struggle, which is like, they start worrying about every single alert that comes on Slack or whichever is your preferred tool.
[2742.98 --> 2744.36]  And they're like, oh, what do I do?
[2744.44 --> 2745.14]  I've got this alert.
[2745.26 --> 2749.30]  It might be my change, but it might not be related to your change at all.
[2749.30 --> 2758.54]  So I think it's something that the team should do on a regular basis as like a team activity or something like that, where they sanity check their alerts.
[2758.98 --> 2765.24]  One way we used to do is any alert that we actually did anything with, we started putting some everything.
[2765.68 --> 2767.00]  All of our alerts used to come to Slack.
[2767.10 --> 2769.14]  So we used to start putting some emojis on it.
[2769.26 --> 2772.68]  So we know which of them were actually things that mattered.
[2772.68 --> 2778.14]  And like on a weekly basis, we were like, oh, there were 10 of these, which we did nothing with.
[2778.54 --> 2779.72]  So maybe we can get rid of it.
[2779.88 --> 2785.18]  So that like, it's very hard to get that feedback cycle on alerts I've found.
[2785.56 --> 2788.30]  Matt, you need to collect the emojis and then feed it back.
[2788.42 --> 2790.52]  Is the API going the other way on emojis?
[2790.78 --> 2796.44]  We do that for in the Grafana incident tool, but I need to tell the on-call team about that idea.
[2796.52 --> 2797.22]  That's such a good idea.
[2797.38 --> 2798.18]  That is kind of fun.
[2798.28 --> 2802.16]  You could collect that data and literally, yeah, you then, oh, hello.
[2802.68 --> 2804.24]  You're like, what does dancing penguin mean?
[2804.56 --> 2804.86]  Yeah.
[2806.24 --> 2806.64]  Yeah.
[2806.90 --> 2807.82]  It means it's cool.
[2809.76 --> 2811.90]  Who owns that idea legally?
[2812.04 --> 2812.52]  I don't know.
[2812.98 --> 2813.62]  I do.
[2813.62 --> 2814.00]  I feel like.
[2814.32 --> 2814.42]  Yeah.
[2817.28 --> 2818.14]  That's a good idea.
[2818.26 --> 2818.66]  Solved.
[2822.34 --> 2827.02]  I want to, I wanted to quickly touch on as you progress in your career, right?
[2827.04 --> 2829.76]  Often you're going to walk into new organizations, right?
[2829.78 --> 2832.62]  And you're, you're new to Lego and everything today is just reinvigorating.
[2832.68 --> 2835.86]  And for us, the thought that we had this, or that I was kind of noodling on this morning,
[2835.86 --> 2837.90]  which is all these things are true.
[2837.90 --> 2841.34]  All these methods are like, are kind of proven.
[2841.76 --> 2846.42]  And in, you know, in some ways, like it has nothing to do with the technology and everything
[2846.42 --> 2848.30]  to do with the landscape that you're walking into.
[2848.38 --> 2851.86]  And then, then you have to figure out how, how and what you introduce.
[2851.86 --> 2857.82]  And I guess I'm curious, like how much about open source tooling makes it easier to transfer
[2857.82 --> 2858.78]  into a new organization?
[2859.48 --> 2864.72]  And even just how much, like, how do you approach going into a new org, having this experience,
[2864.72 --> 2867.84]  but then also not understanding how everything fits together?
[2867.84 --> 2868.56]  Hmm.
[2869.06 --> 2870.46]  I mean, this is so relatable.
[2871.02 --> 2872.42]  I'm going through this now.
[2872.52 --> 2872.66]  Yeah.
[2872.66 --> 2877.26]  Like, given I've been in the Lego group for only three months and I care about monitoring
[2877.26 --> 2880.42]  and like in general sustainability of products quite a lot.
[2880.42 --> 2886.70]  But I've been looking at different teams doing this and thinking, okay, this team has this
[2886.70 --> 2888.28]  Grafana dashboard to do it.
[2888.36 --> 2891.06]  This other team has Neuralic and they're doing something with it.
[2891.22 --> 2896.86]  I think for me, I was lucky that I was in a team that was building monitoring tools as
[2896.86 --> 2901.24]  a service, like providing monitoring tools as a service to other teams.
[2901.24 --> 2907.92]  So for me, it was like easier to catch on to what is happening in different areas within
[2907.92 --> 2908.64]  the Lego group.
[2908.64 --> 2915.54]  But I think what I fall back to is always think about what are the core aspects of monitoring.
[2916.00 --> 2920.42]  So it's things like logging, metrics, alerting, tracing.
[2920.76 --> 2923.20]  So notifications, some of those core things.
[2923.48 --> 2928.68]  And it is looking at those aspects and thinking, how is the team solving these problems?
[2929.28 --> 2936.08]  And where the team have done, used a tool, I have often just endorsed what they've got and
[2936.08 --> 2941.86]  looked into it, but where they haven't, I have often suggested open source tools in those
[2941.86 --> 2944.28]  use cases because two reasons.
[2944.42 --> 2946.98]  One, it's easy to get started and get going with it.
[2947.08 --> 2951.28]  You don't need any licensing and all of those kinds of challenges that come with a proprietary
[2951.28 --> 2951.76]  tool.
[2951.76 --> 2958.18]  And on the other side, there's a lot of community that can help you getting started with the
[2958.18 --> 2958.76]  tool as well.
[2958.76 --> 2965.34]  So I think those are reasons why I would prefer, like when suggesting to teams, I would prefer
[2965.34 --> 2968.16]  open source technologies when it comes to this space.
[2968.16 --> 2975.36]  I mean, as an example, when I was doing some experimentation for my own personal project, I could have gone
[2975.36 --> 2978.84]  with one of the tools that was already available in the organization when I was working.
[2979.00 --> 2983.76]  But then I was like, I mean, if I left this organization, I can't take that tool with me.
[2984.14 --> 2987.64]  So it's better to have it on more open source tools.
[2987.92 --> 2991.84]  I mean, in that case, I used, I think it was Graphite and Grafana that I used in that case.
[2991.84 --> 2998.58]  But it is that while there is transferable skills within the organization, like as an
[2998.58 --> 3006.06]  example, the Lego technology, I think we have around 200 or 250 odd teams in it.
[3006.70 --> 3013.82]  And if these people within the teams have to move between each other, speaking the common
[3013.82 --> 3015.26]  language is quite important.
[3015.68 --> 3020.64]  And having that community outside of the Lego group who can help us with this is quite
[3020.64 --> 3021.08]  important.
[3021.08 --> 3025.74]  And I feel like that is where the power of using open source technologies comes from.
[3026.10 --> 3030.34]  And I mean, I have come from an organization where we were a very big advocate of open source
[3030.34 --> 3030.84]  technology.
[3031.08 --> 3035.96]  So I probably would be singing the song of let's go all in on open source.
[3037.84 --> 3040.76]  So I'm interested then what's next?
[3041.02 --> 3044.90]  What's coming up and how do you keep your finger on the pulse of what's going on?
[3044.90 --> 3051.94]  I often think about like less about tools and more about the capabilities that we really
[3051.94 --> 3053.30]  need within an organization.
[3054.16 --> 3059.14]  And like it could be anything from like, what do we need in terms of system infrastructure
[3059.14 --> 3060.00]  side of things?
[3060.00 --> 3063.56]  Or like the topic for today, more around observability.
[3063.56 --> 3070.30]  So around observability, like I often think the capabilities that we need are logging metrics.
[3070.30 --> 3076.40]  And like an organization can invest in having multiple tools for the same thing.
[3076.56 --> 3079.94]  Or it could be one tool that does all of it.
[3080.06 --> 3082.60]  It depends on the kind of organization you are.
[3082.60 --> 3091.42]  So I have often leaned towards like what's happening in like the DevOps communities or like in the
[3091.42 --> 3098.56]  monitoring communities to actually get insights from them saying, oh, there's I think two years
[3098.56 --> 3103.50]  ago was when I was introduced to Loki, which is the logging tool.
[3103.68 --> 3110.58]  And I got super excited about this mainly because we were using another logging tool within the
[3110.58 --> 3112.50]  organization, which was super expensive.
[3112.60 --> 3118.74]  And like, do we use this super expensive tool, which has some belts and visits, which we don't
[3118.74 --> 3119.12]  use?
[3119.22 --> 3120.92]  Or can we go with something like Loki?
[3121.42 --> 3127.28]  And it is finding out capabilities that you care about and looking at what is happening in
[3127.28 --> 3129.48]  that particular market and stuff.
[3129.74 --> 3136.34]  Within the monitoring space, logging, I think my preference within logging would be like if
[3136.34 --> 3142.36]  you are in the AWS land, then something like AWS CloudWatch or like Loki, Splunk.
[3142.36 --> 3146.66]  These are a couple of tools that I have used in the logging space.
[3146.82 --> 3149.70]  You can use the same kind of tools for metrics as well.
[3150.04 --> 3156.92]  But there are better tools for metrics like Pometheus is really good or Graphite, which again, like I have
[3156.92 --> 3159.74]  spent quite a lot of my career in Graphite.
[3159.74 --> 3164.76]  So I probably have a preference in this space and see what innovation is happening in the
[3164.76 --> 3165.70]  Graphite space.
[3165.88 --> 3170.44]  But yeah, Pometheus is probably another one which is really good in the time series database
[3170.44 --> 3171.52]  side of things.
[3172.02 --> 3175.36]  And then it's also to do with like your metrics aggregation.
[3175.44 --> 3179.60]  So you have all of these different metrics and logs and everything that you're collecting,
[3179.60 --> 3181.78]  but how do you visualize them together?
[3181.78 --> 3186.76]  So you need something around the visualization layer, which is where like Grafana or like
[3186.76 --> 3189.66]  Kibana, one of these kinds of tools would come in handy and stuff.
[3190.14 --> 3194.20]  And finally, I think it's the whole, you're doing all of this because you want to alert
[3194.20 --> 3194.48]  things.
[3194.64 --> 3196.72]  So what do we have in the alerting space?
[3196.80 --> 3200.22]  Thinking about like, do I use like Slack notifications?
[3200.22 --> 3204.92]  Do I use email notifications, SMSs, page of duty, whatever.
[3205.52 --> 3210.46]  And it's just making sure you understand the capabilities of what you're trying to solve
[3210.46 --> 3213.24]  and finding core products in each of those areas.
[3213.34 --> 3216.92]  And it could be the same product that solves everything or it could be different products.
[3217.12 --> 3223.08]  And yeah, I tend to lean towards communities and conferences to actually figure out what is
[3223.08 --> 3225.14]  hot in the market and in places.
[3225.98 --> 3226.10]  Yeah.
[3226.10 --> 3230.52]  And what I really like about this is like, that's all kind of like through the lens of
[3230.52 --> 3233.50]  release the way that you think about it as like, what are the problems that you're trying to solve
[3233.50 --> 3235.22]  for the, for the customer?
[3235.36 --> 3235.50]  Right.
[3235.52 --> 3237.12]  And then what is the value that you're trying to provide?
[3237.16 --> 3241.88]  So even at that point, like all of these could become sort of like, it's not interchangeable,
[3241.88 --> 3244.58]  but you can solve the problem in 400 different ways.
[3244.66 --> 3244.96]  Right.
[3245.04 --> 3248.52]  And, and I just really liked that you start with, it feels like you start with that approach
[3248.52 --> 3250.34]  to say like, what do you actually need to do?
[3250.64 --> 3251.80]  What do you need to protect?
[3252.28 --> 3254.12]  And then figure out how to do it.
[3254.30 --> 3255.48]  And I like that.
[3255.48 --> 3259.66]  That feels like the most transferable skill between company to company.
[3259.90 --> 3260.02]  Yeah.
[3260.14 --> 3265.22]  And also like within teams, when there are so many different teams and every team's autonomous
[3265.22 --> 3270.20]  to use their own tools and stuff, then like, I think you need the core principles to be
[3270.20 --> 3272.94]  the same irrespective of what tools they're using.
[3272.94 --> 3278.94]  And that's where I find having the capabilities and the principle layer set, right, would help
[3278.94 --> 3282.70]  teams figure out what is the best tool for their use cases and stuff.
[3282.70 --> 3283.94]  Well, that's amazing.
[3284.12 --> 3286.16]  Loads of great practical advice there.
[3286.24 --> 3289.80]  And you yourself have spoken at conferences on this subject as well.
[3289.94 --> 3293.78]  I noticed that people can, we'll put, put one in the show notes for people interested,
[3294.14 --> 3296.58]  but you can also Google or use any search engine.
[3296.68 --> 3297.78]  Other search engines are available.
[3298.50 --> 3304.16]  You can duck, duck, go and find just for your name and you'll, yeah.
[3304.16 --> 3304.94]  Nayana Shetty.
[3305.44 --> 3308.20]  Well, unfortunately that is the time.
[3308.38 --> 3310.60]  That's all the time we have, I'm afraid.
[3311.16 --> 3312.32]  Thank you so much.
[3312.94 --> 3314.24]  Matt Toback was here, weren't you, Matt?
[3314.64 --> 3315.32]  I was.
[3315.36 --> 3318.54]  Is there anything that you want to say to your future self just before we go?
[3319.06 --> 3320.12]  Oh, I love that.
[3320.12 --> 3325.00]  I think it is, you don't have to solve all problems today.
[3325.18 --> 3329.32]  There are things that you can leave for the future to solve.
[3330.32 --> 3333.12]  That is what I would say to my future self.
[3334.94 --> 3339.14]  It'd be more useful if we could send messages to our past selves though, because we could
[3339.14 --> 3341.44]  like tell them what the stocks are going to do in that.
[3341.66 --> 3344.18]  No, because we, we know what happens, right?
[3344.32 --> 3345.42]  The space-time continuum.
[3346.18 --> 3347.02]  It's just not good.
[3347.16 --> 3348.02]  Biff gets it, doesn't he?
[3348.30 --> 3349.04]  Biff, he does.
[3350.12 --> 3350.56]  Okay.
[3351.70 --> 3352.40]  We won't do it then.
[3353.12 --> 3354.22]  We won't do it then, Matt.
[3354.38 --> 3355.40]  You've, yeah.
[3356.08 --> 3356.44]  Okay.
[3356.96 --> 3358.40]  Well, yes.
[3358.40 --> 3359.20]  Thank you so much.
[3360.26 --> 3361.14]  I've enjoyed it.
[3361.24 --> 3364.60]  I mean, this is a topic that I enjoy speaking in general.
[3364.84 --> 3365.28]  So yeah.
[3365.60 --> 3368.50]  Are you speaking at any other conferences coming up or will you?
[3369.06 --> 3371.30]  No, because I'm new to the organization.
[3371.30 --> 3376.88]  I'm just like stepping away from speaking so that I can gather some insights from the organization
[3376.88 --> 3378.02]  before I start speaking.
[3378.64 --> 3379.30]  So yeah, none.
[3379.30 --> 3382.78]  But the videos of your past self are still available, of course.
[3383.02 --> 3384.76]  I do recommend people check them out.
[3385.36 --> 3385.50]  Yeah.
[3385.88 --> 3389.62]  Thank you so much to Matt Toback and our special guest, Nayana Shetty.
[3389.94 --> 3391.30]  I've been Matt Raya, still am.
[3391.74 --> 3393.40]  And thank you very much for listening.
[3393.54 --> 3396.24]  We'll see you next time on Grafana's Big Tent.
[3396.24 --> 3410.30]  Have you learned that?
[3410.42 --> 3411.96]  Have you learned how to play the riff?
[3412.20 --> 3413.18]  I have not yet.
[3413.32 --> 3413.90]  But I have time.
[3414.24 --> 3415.56]  You should let it.
[3415.56 --> 3417.66]  I'm going to on the airplane to Whistler.
[3417.80 --> 3418.92]  I'm going to take the bass out.
[3420.18 --> 3422.58]  My seatmate won't be terribly happy with that.
[3422.94 --> 3425.14]  Please put your seat backs and basses away.
[3425.58 --> 3426.58]  We are coming into land.
[3427.28 --> 3429.00]  You could do upright in a seat, maybe.
[3429.40 --> 3429.84]  Oh, yeah.
[3429.84 --> 3432.34]  You'd have to get a ticket for like a double bass.
[3432.34 --> 3437.40]  But you could also do like Seinfeld links with it.
[3437.48 --> 3441.86]  It could be like make a little joke, a zinger to the staff.
[3443.80 --> 3445.08]  Just do a bit of bass.
[3445.66 --> 3446.48]  That would be good, wouldn't it?
[3446.58 --> 3447.52]  Yeah, that would be nice.
[3452.62 --> 3458.22]  If you enjoyed this conversation, maybe subscribe at BigTent.fm.
[3458.36 --> 3461.60]  And if you're a long-time listener of GoTime, share the show with a friend.
[3461.60 --> 3464.52]  It's the best way to pay it forward and spread the love.
[3464.90 --> 3467.72]  Also, don't forget to check out Changelog++.
[3468.14 --> 3470.42]  That's our membership program with a bunch of perks.
[3470.84 --> 3471.78]  Support our work.
[3472.00 --> 3473.04]  Make the ads disappear.
[3473.50 --> 3476.56]  And hey, we just added a free pack of stickers to everyone who joins.
[3476.92 --> 3479.84]  Learn more at changelog.com slash plus plus.
[3480.08 --> 3482.18]  Thanks again to Fastly for CD-ing for us.
[3482.42 --> 3485.40]  To the mysterious Breakmaster Cylinder for the always fresh beats.
[3485.58 --> 3486.50]  And to you for listening.
[3486.80 --> 3487.52]  We appreciate you.
[3487.80 --> 3491.22]  Stay tuned for Dead Program's time travel-inspired guest appearance.
[3491.22 --> 3493.94]  It's coming up next time on GoTime.
[3493.94 --> 3497.26]  Game on.
