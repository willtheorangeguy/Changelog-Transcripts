[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.38]  And we're hosted on Linode cloud servers.
[12.74 --> 14.76]  Head to Linode.com slash Changelog.
[17.72 --> 19.56]  Linode is our cloud server of choice.
[20.08 --> 23.00]  Grab the Nano plan for just $5 a month, just $5.
[23.38 --> 28.56]  That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[28.56 --> 31.32]  Let's be honest, you can go a long ways on that $5.
[31.86 --> 36.20]  When you do need to scale up, their prices are predictable, so you can put your calculator down.
[36.30 --> 36.86]  You won't need it.
[37.16 --> 42.34]  We've been running Changelog.com on Linode for years, and we're always impressed by their award-winning support team.
[42.86 --> 45.60]  Check them out at Linode.com slash Changelog.
[45.78 --> 48.96]  Once again, that's Linode.com slash Changelog.
[58.56 --> 65.38]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[65.82 --> 69.78]  This is where conversations around AI, machine learning, and data science happen.
[70.18 --> 74.80]  Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[75.18 --> 76.14]  And follow us on Twitter.
[76.28 --> 77.92]  We're at Practical AI FM.
[78.30 --> 79.62]  Okay, here's Daniel and Chris.
[79.62 --> 87.30]  Welcome to another episode of Practical AI.
[87.66 --> 89.22]  This is Daniel Whitenack.
[89.34 --> 99.68]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[99.84 --> 100.54]  How's it going, Chris?
[100.76 --> 101.66]  Doing great, Daniel.
[101.70 --> 102.30]  How's it going today?
[102.74 --> 103.80]  It's going great.
[103.80 --> 109.38]  It was a beautiful weekend after finishing a paper submission to a conference.
[109.86 --> 112.58]  So, you know, all was good.
[112.68 --> 118.84]  I got to relax and be outside a little bit and feel the satisfaction of having that done.
[119.02 --> 119.88]  So, what about you?
[120.20 --> 120.82]  Sounds good.
[120.96 --> 122.58]  Just family stuff over the weekend.
[122.74 --> 129.98]  I had the satisfaction of both my daughter, who's in second grade, is into basketball, and we raised the goal all the way up to the 10-foot mark.
[130.18 --> 130.42]  Whoa.
[130.74 --> 132.14]  So, she's learning that.
[132.22 --> 132.92]  The big time.
[132.92 --> 135.52]  And we transitioned her up to a larger bicycle as well.
[135.60 --> 137.34]  So, both big daddy moments for me.
[137.34 --> 139.92]  So, not AI related, but it was a good weekend in that way.
[140.26 --> 141.22]  That is exciting, though.
[141.58 --> 141.76]  Yeah.
[142.02 --> 142.26]  Yeah.
[142.46 --> 142.74]  Cool.
[142.94 --> 145.00]  Well, I'm excited about this show today.
[145.30 --> 152.98]  We have a topic that is very interesting related to conversational data and extracting insights.
[152.98 --> 159.22]  We're joined by Mike McCourt, who is a data scientist at Invoca, to talk a little bit about that subject.
[159.34 --> 160.00]  So, welcome, Mike.
[160.54 --> 160.96]  Hi.
[161.04 --> 161.84]  Thank you for having me.
[161.84 --> 170.78]  Before we jump into that, would you just give us a little bit of a background to help us understand how you got into AI and data science stuff?
[170.90 --> 171.90]  And then we'll take it from there.
[172.38 --> 172.78]  Absolutely.
[173.10 --> 173.26]  Yeah.
[173.30 --> 178.30]  So, my arrival into the AI world was totally fortuitous.
[178.70 --> 180.72]  I had not planned on it at all, really.
[180.72 --> 185.80]  My original goal was to be a college professor.
[186.42 --> 195.94]  And I really wanted to study astrophysics and to do research in that field and to teach studying how structure formed in the universe and how we came to be here.
[196.94 --> 199.84]  And so, you know, I worked for probably 10 years.
[199.84 --> 202.04]  I was dutifully towards that end.
[202.36 --> 208.76]  I majored in physics and theoretical physics in college and got a PhD in astrophysics.
[209.74 --> 215.94]  And then I moved all the way across the country for a postdoc position, just like a research position in science.
[216.50 --> 219.60]  And then moved all the way across the country again for another one.
[219.60 --> 228.60]  And, you know, as I was dutifully working towards this goal of being a professor, I was getting less and less sure that that was the life I wanted.
[229.60 --> 235.72]  And at the same time, I'd seen this new field of AI just like take off and blossom.
[236.44 --> 237.70]  And what year was this around?
[238.22 --> 241.64]  Well, so I was in college 2004 to 2008.
[241.88 --> 242.14]  Okay.
[242.22 --> 245.32]  And basically never heard of AI in that timeframe.
[245.32 --> 251.18]  I mean, I knew of some people in the computer science department who were doing research in AI.
[251.90 --> 257.60]  And then like midway through grad school, 2010, 2011, I started to hear more and more about it.
[257.70 --> 258.52]  It seemed interesting.
[259.56 --> 263.92]  And like by the end of grad school, you know, to an outsider, AI was like hot.
[264.14 --> 267.20]  And by the end of my first postdoc, AI was really hot.
[267.56 --> 271.46]  You know, I saw how fast the field was moving and new inventions were coming.
[271.72 --> 273.92]  And it seemed like it was advancing by leaps and bounds.
[273.92 --> 277.06]  And eventually I got jealous and I wanted to make the switch.
[277.74 --> 279.80]  So, yeah, it's interesting.
[280.02 --> 282.14]  It seems like you're even the years.
[282.26 --> 287.24]  So I was also in college 2004 to 2008 and then went to grad school in physics.
[287.24 --> 291.02]  So we've got a lot of similarities there, except I guess you stuck.
[291.38 --> 293.42]  You had more perseverance than I did.
[293.52 --> 295.26]  I didn't make it through the postdoc.
[295.50 --> 298.02]  I jumped ship before then into industry.
[298.40 --> 298.56]  Yeah.
[298.64 --> 299.60]  But it is interesting.
[299.60 --> 307.70]  I guess there's really a lot of astrophysics and also high energy physics people getting into this space.
[307.82 --> 309.22]  At least that's my understanding.
[309.44 --> 312.12]  Now I'm kind of more removed from it than you may be.
[312.46 --> 318.02]  As the non-physicist in the group, I have to say, I've noticed that it seems like the AI is breaking out with physicists these days.
[318.02 --> 320.24]  It's a good thing, by the way.
[320.62 --> 321.28]  Yeah, totally.
[321.86 --> 322.14]  Yeah.
[322.64 --> 322.88]  Yeah.
[322.88 --> 324.22]  So you jumped earlier than I did.
[324.32 --> 325.92]  I think you could see harder than I could.
[326.44 --> 332.62]  But yeah, I feel like almost all of my colleagues now from grad school are in data science or AI.
[332.62 --> 340.74]  Yeah, well, it's definitely very competitive in terms of like tenure track physics positions right now.
[340.74 --> 349.34]  But the demand for AI talent and data science talent is so huge that, you know, I think that's driving a bit of that.
[349.84 --> 354.56]  Before we dive in, you know, and talk about what we were planning, I'm just kind of curious with both of you here.
[354.56 --> 362.88]  Any thoughts on is there kind of a natural progression, do you think, these days for physicists to move into AI and kind of natural synergy between the two?
[363.38 --> 364.68]  I'll let Mike go there, maybe.
[364.88 --> 366.62]  He was in physics longer than me, maybe.
[367.28 --> 369.08]  I made the jump more recently, I think.
[369.32 --> 375.90]  Yeah, I think for me, I felt like physics prepared me extremely well for the jump into data science.
[375.90 --> 385.90]  You know, I think in physics, what you're trained to do is to take some observation about the world, some fact that you'd like to understand and explain.
[386.28 --> 390.10]  And then you come up with a model that you believe could explain it.
[390.24 --> 395.64]  And then you have to grind through the math and turn that model into something that can make predictions.
[396.26 --> 402.66]  And in the process, you have to collect some data, you have to inform your model, you have to fit four parameters in the model,
[402.66 --> 405.16]  and you have to understand your uncertainty and all those.
[405.90 --> 408.52]  And then at the end of the day, you have to make a prediction.
[409.20 --> 414.28]  And then you have to convince someone else to go run an experiment and test your prediction.
[414.64 --> 420.18]  And if your predictions come out well, then you believe that you've learned something about the universe, and you can publish that.
[420.74 --> 423.62]  I think that process in AI is pretty similar.
[424.30 --> 426.54]  Yeah, it's a great parallel there that you outline.
[427.34 --> 428.84]  Yeah, so the focus is different.
[428.84 --> 433.22]  You know, in physics, we don't really care about the predictions on their own.
[433.22 --> 435.48]  The predictions are there to test our theories.
[435.78 --> 439.68]  And the theory and the model is really the product that we want to give to the world.
[440.24 --> 448.96]  And working in AI, you know, the model actually is typically something that we, well, sometimes we hide it, or at least it's not really the focus.
[449.48 --> 452.24]  The internal workings of the model isn't what we care the most about.
[452.36 --> 454.14]  It's the predictions that we care the most about.
[454.70 --> 456.84]  But I think that process is broadly similar.
[456.84 --> 457.96]  Yeah, definitely.
[458.20 --> 458.82]  I agree.
[459.10 --> 461.80]  And I think you expressed it much better than I could.
[462.00 --> 471.84]  So it seems like you've also developed the important data science characteristic of being able to explain things and frame things well.
[472.12 --> 475.04]  So I don't know if that's something you learned in physics or afterwards.
[475.40 --> 477.26]  But yeah, appreciate that.
[477.52 --> 484.94]  So tell us a little bit more about how you got involved with Invoca and your path to sort of what you're doing right now.
[484.94 --> 487.84]  I got very lucky landing at Invoca.
[488.88 --> 495.10]  So like I said, I was kind of, I was very, I had a laser-like focus on my physics career trajectory.
[495.50 --> 502.68]  I'd never really considered anything else until I kind of got towards the end and realized AI seemed more interesting to me.
[503.06 --> 507.68]  So I was not really aware of what was going on in industry.
[508.08 --> 510.74]  And I made the jump a little bit blind.
[510.74 --> 516.38]  But, you know, while I was making major life decisions, I decided I wanted to work in AI.
[516.84 --> 519.80]  And I decided that if possible, I wanted to live in Santa Barbara.
[520.66 --> 522.04]  I'd always loved the city here.
[522.36 --> 525.54]  And I didn't know if there would be AI positions in Santa Barbara.
[525.96 --> 527.10]  So I just started searching.
[527.10 --> 530.14]  And I found this company called Invoca.
[530.72 --> 535.58]  And, you know, as a scientist, Invoca does call analytics for marketing.
[536.30 --> 537.76]  I didn't know that much about phone calls.
[537.84 --> 539.48]  And I knew almost nothing about marketing.
[540.16 --> 541.84]  But it looked like an awesome company.
[542.32 --> 546.42]  Especially what was really interesting to me was the data set that Invoca has.
[546.54 --> 550.98]  Because we study phone calls here, that's an unusual data set.
[551.20 --> 555.50]  Most of the research, at least, in AI now is not focused on phone calls.
[555.50 --> 558.96]  So it's kind of a unique problem in a big data set.
[559.76 --> 561.82]  And it looked like a fantastic company to work for.
[562.34 --> 564.98]  And so even though I came in knowing almost nothing about marketing,
[565.58 --> 569.88]  I was able to convince them that my skills as an astrophysicist would be useful to them.
[571.10 --> 575.14]  And landed a fantastic job at a really great company here.
[576.42 --> 578.70]  So you kind of led right into where I was about to ask you.
[578.78 --> 581.06]  And that is, I had looked at Invoca's website.
[581.06 --> 586.02]  And it talks about Invoca being this AI-powered call tracking and analytics platform.
[586.58 --> 589.98]  And so you've already kind of talked a little bit about this interesting data set.
[590.16 --> 594.32]  And so I guess for those of us who are not in that particular field,
[594.32 --> 597.96]  could you talk a little bit about what call analytics mean?
[598.10 --> 601.78]  And also, I noticed on the webpage, it talks about campaign attribution.
[602.06 --> 604.40]  And it refers to some actionable data.
[604.74 --> 607.66]  And if you could kind of talk about how all those fit together
[607.66 --> 610.08]  and what they mean in this context, I'd really appreciate it.
[610.08 --> 610.84]  Absolutely.
[611.24 --> 613.54]  So keep in mind, I'm not a marketer.
[613.66 --> 616.34]  So I'll do my best at explaining the value proposition of what we do.
[616.82 --> 623.08]  You know, I think now marketers, when a transaction happens online,
[623.50 --> 626.82]  marketers are used to getting all of this attribution information.
[627.48 --> 629.60]  So if you buy something online, they know who you are.
[630.06 --> 631.62]  They know what ads you've seen.
[632.32 --> 633.82]  They know what webpages you've been to.
[633.82 --> 639.44]  And they can use this information to really analyze their marketing campaigns and optimize them.
[640.08 --> 645.08]  And try to make sure that they're spending money on ads that are driving business to the company.
[645.74 --> 649.74]  And hopefully that are relevant and interesting to consumers.
[650.34 --> 650.42]  Yeah.
[650.50 --> 653.00]  So it's not just like broadcast marketing.
[653.46 --> 657.08]  The trend, at least now, is very targeted marketing, right?
[657.08 --> 660.00]  Yeah, it's changed a lot in recent decades.
[660.26 --> 663.90]  But as soon as you pick up the phone, they lose a lot of that information about you.
[664.18 --> 668.66]  If you don't finally make your purchase online, but you pick up the phone and call them and make your purchase there,
[669.14 --> 670.82]  then a lot of that attribution is lost.
[671.80 --> 675.94]  And that's important because a lot of high-value transactions still happen over the phone.
[676.66 --> 679.62]  You know, if you're buying a new sweater, you'll do that online.
[679.62 --> 686.52]  But if you're getting an air conditioner installed in your house, you typically want to pick up the phone and talk to someone before you make that decision.
[686.84 --> 690.10]  That's a great point in terms of how real life works when you're doing that.
[690.92 --> 691.14]  Yeah.
[691.38 --> 698.08]  And so if you're shopping for mortgages or home improvement things, or if you're booking vacation on the cruise line,
[698.28 --> 701.54]  big, high-value transactions, they still tend to happen over the phone.
[701.54 --> 713.08]  And Invilco works to close that gap so that marketers can analyze the transactions that happen over the phone and link those to their marketing campaigns.
[713.70 --> 714.64]  And I'm just curious.
[714.84 --> 720.04]  I did spend a number of years as a technology person in marketing organizations.
[720.04 --> 722.38]  And how do you actually make the link?
[722.76 --> 725.38]  Or do you, in this case, if they're starting online?
[725.38 --> 730.38]  And, you know, traditionally, marketing has focused so much on analytics with online activity.
[730.84 --> 733.22]  And then they've totally moved over into this new medium.
[733.22 --> 736.70]  And you start your analytics there, which I guess we're about to learn about.
[736.92 --> 739.16]  But how do you actually make that connection between the two?
[739.82 --> 741.50]  Yeah, that's an excellent question.
[742.10 --> 744.50]  And I have only a thin understanding of it.
[744.64 --> 745.80]  There's a whole...
[745.80 --> 748.34]  This is kind of the core of Invoca's technology.
[748.48 --> 749.98]  And I just work on the AI part.
[749.98 --> 756.42]  But essentially, it works when you sign up with Invoca, you get a number of phone numbers.
[757.52 --> 762.64]  And then when ads are shown, a number gets swapped into each individual ad.
[762.90 --> 767.14]  And so that when someone calls the number, that number gets forwarded to your business.
[767.72 --> 771.28]  But the number they called can be used to see what ad they called in from.
[772.38 --> 774.04]  Yeah, I think together we're getting there.
[774.04 --> 782.36]  I know in a previous employer, actually, the first data science position I had after leaving physics was with a telecom company.
[783.00 --> 785.30]  And I think most people don't realize this now.
[785.40 --> 800.30]  But it is super easy for you to, you know, spin up, you know, even a thousand, a hundred thousand, you know, numbers, unique numbers, and then destroy them right away after you've used them these days via API and things like this.
[800.30 --> 809.50]  So you can be very smart with your phone campaigns in terms of using unique numbers for even just a single purpose, like doing this link, which is pretty interesting.
[810.16 --> 810.74]  Yeah, exactly.
[810.74 --> 815.58]  But then it starts to get complicated because you want to make sure it's a phone number that no one's used for a while.
[816.18 --> 818.38]  So there are a ton of people working on that here.
[818.70 --> 819.56]  I find it interesting.
[820.16 --> 821.06]  Yeah, it is interesting.
[821.34 --> 827.00]  And I think, you know, also, it's fairly transparent to the user, which is interesting.
[827.00 --> 835.84]  And in a similar way to most people don't realize that they're being, you know, tracked by Facebook when they're not actually on Facebook or Instagram, right?
[835.84 --> 849.82]  There's people that have this, like, embedded thing in their website, or like most people should, that are doing any type of marketing that links their activity on that website, assuming they're logged in to Facebook or Instagram to their account.
[849.82 --> 854.86]  And I think a lot of that world is kind of transparent to most people.
[854.96 --> 860.86]  At least it was to me before I kind of got into some of these related things.
[861.24 --> 870.32]  That point you made a moment ago about having so many numbers available, I don't think I have ever thought of using phone numbers in such a disposable way.
[870.74 --> 871.96]  It makes perfect sense.
[872.04 --> 874.34]  And I do do programmatic stuff with phone numbers.
[874.34 --> 881.22]  You know, there are companies out there, obviously, where you can, you know, get phone numbers for your business and program them into your stack and stuff.
[881.32 --> 885.20]  But I don't think I had thought about it in the context that you guys are discussing.
[885.36 --> 887.12]  So it's an interesting thought there.
[887.84 --> 888.00]  Yeah.
[888.16 --> 889.96]  No, I've had the same phone numbers since high school.
[890.36 --> 894.84]  So this process really, really surprised me.
[895.14 --> 896.92]  But yeah, it's amazing to see it work.
[897.40 --> 897.56]  Yeah.
[897.56 --> 910.96]  And I'm assuming, I mean, I don't know, it was interesting for me as a physics person coming into this world that like you were talking about some of these problems around, oh, you don't want to reuse the number too much.
[910.96 --> 913.80]  You know, what's the optimum amount to do that?
[913.96 --> 916.20]  How many numbers do I need to spin up?
[916.24 --> 920.22]  What's the volume of that and the geography and targeting?
[920.22 --> 932.12]  Like these are very complicated problems that aren't like, you know, the fundamental pure science problems of like nature, but they are really interesting problems, at least for me.
[932.12 --> 942.98]  I found them interesting as a physicist just in terms of their complexity and, you know, also their connection to real life and how you could make a real life impact for people.
[943.14 --> 944.36]  I don't know if it was similar for you.
[945.04 --> 945.62]  Oh, absolutely.
[945.62 --> 960.76]  Yeah, I think one of the really fun things that I learned as a physicist is that, you know, you can use math to make a model of something and then optimize it and then apply that to the real world and see it work.
[960.96 --> 968.10]  It's kind of amazing to me that I can listen to a problem, write something out on the chalkboard, grind through the math, and then end up with something useful.
[968.10 --> 978.52]  So, Mike, I think we should probably transition to the more AI related things that you're doing at Invoca since this is practical AI and we definitely want to hear about those things.
[978.96 --> 988.04]  And one of the things I know that was highlighted as we were talking before the show was this product called Signal AI and some of the things you're doing around that.
[988.58 --> 995.56]  Could you maybe just give us a bit of the motivation behind that product and, you know, at Invoca and how it came about?
[995.56 --> 996.86]  Yeah, absolutely.
[997.28 --> 1002.32]  As I mentioned, we do, well, the kind of core of Invoca is call tracking.
[1002.52 --> 1009.02]  So you can attribute a phone call to an ad that would allow you to see which ads were driving the most calls.
[1009.98 --> 1014.62]  But really, you know, as a marketer, what you want to understand is what's driving revenue.
[1015.30 --> 1019.00]  And that requires understanding what actually happened on each of the calls.
[1019.20 --> 1022.72]  So you don't want to just optimize for a marketing campaign that drove more calls.
[1022.72 --> 1027.50]  You want to optimize for one that drives more calls of people who actually go on and buy something.
[1028.06 --> 1035.82]  Yeah, you don't want vanity metrics similar to like you wouldn't want to optimize an ad for just like clicks of the like button on Facebook or something like that.
[1036.20 --> 1036.70]  Yeah, exactly.
[1036.94 --> 1038.24]  You know, at the end of the day, you need revenue.
[1038.24 --> 1041.64]  And so Signal.ai is our answer to that.
[1041.84 --> 1056.38]  So it's a product that will actually analyze what takes place on the call and tell you whether it was a purchase or whether it was an appointment or a cancellation or whatever it is that you happen to want to track to attribute to your campaigns.
[1056.38 --> 1059.80]  So Signal.ai is a supervised model.
[1060.34 --> 1066.00]  And what that means is that the model is trained by labeled data that's provided by the user.
[1066.48 --> 1073.32]  So if you, you know, let's say that you're a dentist's office and what really matters to you is appointments.
[1073.32 --> 1081.24]  You're looking for new patients, new people to come in, and you want to increase the number of appointments you're getting per month.
[1081.24 --> 1090.10]  You would provide us with, say, 150 calls where an appointment was made and 150 calls where an appointment was not made.
[1091.04 --> 1101.90]  And you can train a Signal.ai model that would now listen to all of your incoming calls as they're routed through Invoca and tag them as true or false for appointment.
[1101.90 --> 1115.96]  And then you can feed this information back into your marketing system to try to optimize not only which ad campaigns they're driving the most calls, but which ad campaigns are actually bringing people into your office for appointments.
[1117.18 --> 1126.50]  So are you primarily classifying the call from the AI perspective, or are you doing more than just classification with the AI stuff?
[1126.70 --> 1129.30]  Can you kind of talk about, you know, how that fits in directly?
[1129.30 --> 1132.62]  Yeah, so Signal.ai, exactly. It's classification.
[1133.58 --> 1137.12]  You know, was it an appointment? Was it rescheduling, cancellation?
[1137.80 --> 1146.68]  I'm just kind of curious, are there any other aspects of, like, particularly around NLP, natural language processing, that you guys are focused on, like, aside from classification?
[1147.28 --> 1155.42]  Well, I think for Signal.ai, a lot of the processing that we do, you know, at the end of the day, what we want is classification.
[1155.42 --> 1162.34]  Classification is actually difficult on phone calls for a number of reasons that I find interesting.
[1162.70 --> 1166.64]  One is that phone calls range really widely in length.
[1167.70 --> 1176.08]  And so if you listen to phone calls made to businesses, a lot of them are, you know, three minutes long or even less than a minute in some cases.
[1176.08 --> 1179.34]  And some of them are, can be two hours long.
[1180.10 --> 1186.62]  And so a classification algorithm has to be able to handle this wide range and lengths of phone calls.
[1186.62 --> 1198.26]  And that can be tricky because if the classifier is looking for a particular pattern in a phone call, you know, if the phone call is really, really long, the odds that that pattern is going to appear randomly increases.
[1198.26 --> 1204.18]  So it's tough to be able to handle that range of lengths in phone calls.
[1204.84 --> 1217.32]  And then another thing that I find really interesting about phone calls is that, you know, English is such a rich language that no two people are going to express themselves the exact same way.
[1217.32 --> 1228.66]  Even for something as simple as scheduling, sticking with the example of a dentist's office, you know, scheduling an appointment for a cleaning at a dentist's office, that's a relatively simple thing to do.
[1229.12 --> 1237.58]  But if you listen to a hundred phone calls where people are all doing the same thing, they have the same goal, no two of them are going to use the exact same sequence of words.
[1238.04 --> 1242.78]  You know, there's enough freedom in English that we can all express ourselves a little bit differently.
[1242.78 --> 1248.62]  A classifier algorithm that's working on phone calls has to be really sensitive at pulling these patterns out of speech.
[1249.84 --> 1256.56]  But at the same time on phone calls, there are certain things that are exactly the same from one call to the next.
[1257.42 --> 1265.14]  You know, if there's a hold message on the call, if you call or I call, we're going to hear the exact same sequence of words in the hold message.
[1265.14 --> 1274.84]  And so if a classifier algorithm is too sensitive at pulling these patterns out, you know, it'll get tripped up on these recordings that are present in phone calls.
[1274.84 --> 1277.26]  Yeah, so I have so many questions.
[1277.36 --> 1278.88]  This is super interesting.
[1278.88 --> 1291.14]  I guess the first is the other thing that I was thinking about when you were talking about, you know, challenges specific to phone calls, you were talking about the sort of structure of them, how there are maybe repeating things.
[1291.14 --> 1295.58]  But a lot of times there are varied links and there's a lot of variants in terms of language.
[1295.94 --> 1300.26]  You know, there's also the element of accent and all of that, I'm assuming.
[1300.26 --> 1316.34]  So one of the things I was wondering was, are you primarily in the system analyzing the raw audio or are you converting that to text and then doing sort of text based methods to do classification?
[1316.34 --> 1330.78]  And along with that, I'm assuming that like phone calls, for example, the audio is not going to be as good of quality as, you know, our wonderful quality practical AI recordings or other audio recordings, maybe.
[1331.04 --> 1333.32]  So like, are there also issues with that?
[1333.60 --> 1335.12]  Those are some of the things going through my mind.
[1335.58 --> 1337.28]  Yeah, these are excellent questions.
[1337.28 --> 1344.26]  So by the time it reaches me and on the data science team here, the phone calls already been transcribed.
[1345.04 --> 1350.10]  And so I'm fundamentally working with text data, but they're transcripts of phone calls.
[1350.52 --> 1357.74]  And so I don't personally work on analyzing, you know, the waveform of the audio and turning that into text.
[1357.74 --> 1369.48]  But, you know, we do have, you see significant differences with dialect and accent, the way that people will explain things varies quite a lot across the country.
[1369.48 --> 1396.92]  And, you know, again, doing classification, like, you know, if I'm canceling, if let's say we have a model for appointment set, and it's trained on phone calls from people in California, you know, me as a Californian canceling an appointment, that might seem more like the trues for appointment set, because I'm from the same region, than someone from, you know, Maine, who's making an appointment.
[1396.92 --> 1402.56]  And so we really do have to be careful about how we handle dialect and regional differences.
[1403.32 --> 1412.30]  And then, yeah, as you mentioned, the audio quality varies widely, you know, somebody may be making a call from home, and the audio quality is fantastic.
[1412.78 --> 1415.26]  And you can hear everything and understand every word that's said.
[1415.86 --> 1421.26]  Or they may be calling on a cell phone from, you know, driving on the freeway, and the audio quality is terrible.
[1421.26 --> 1429.52]  What sort of real variance and impact does that make in the actual since you're kind of the consumer of the text, and it's already been transcribed?
[1429.84 --> 1439.62]  Do you see like, an incredible amount of noise in the text because of those issues? Or is it fairly clean? And then there's kind of outliers here and there?
[1440.26 --> 1446.20]  You know, I think there's kind of a continuum from transcripts that are nearly perfect to ones that are almost all noise.
[1446.20 --> 1452.32]  So we get the whole range. And we treat it almost as a like a quasi linguistic phenomenon.
[1452.76 --> 1459.50]  When a word is mistranscribed due to noise in the audio, that's kind of like an artificial synonym.
[1460.32 --> 1472.20]  You know, so words like higher, tire, fire, higher, those might all be synonyms on, you know, for the purposes of phone call transcripts,
[1472.20 --> 1474.32]  even though they have different meanings in the dictionary.
[1474.96 --> 1481.28]  So I'm curious, as you go through this process, and I've been listening to you and Daniel, and Daniel's also a real NLP expert.
[1481.48 --> 1483.50]  And so I'm trying to learn from both of y'all.
[1483.58 --> 1487.52]  Are you using multiple models in your workflow as you're coming through this?
[1487.64 --> 1491.22]  Or is there one master model? You know, which approach are you taking?
[1491.22 --> 1499.16]  And how do you account for variability within the different speakers, given the fact I know Daniel mentioned accent a few minutes ago?
[1499.38 --> 1506.66]  So as you run into all these variations that you can have, I guess from an accent standpoint, that would be out from because you're only dealing with text, right?
[1506.72 --> 1512.78]  But at some point, are you thinking about doing the raw audio and maybe you do things like sentiment analysis or anything?
[1513.00 --> 1517.02]  And I guess I'm, I'm running all over the place here, but I'm just trying to understand.
[1517.02 --> 1527.28]  Yeah. So are you using multiple models in your workflow for like different types of calls, like calls of this accent type or of this dialect?
[1527.64 --> 1532.40]  It has one model and then calls of a different accent or dialect have a different model.
[1532.66 --> 1534.66]  Also, you mentioned like segmenting things.
[1534.66 --> 1538.02]  So like the whole music or message and that sort of thing.
[1538.10 --> 1542.24]  So do you have different models that analyze the different parts of the call?
[1542.24 --> 1548.24]  Or are you kind of just saying we have one big model that has enough complexity to handle all those things?
[1548.76 --> 1549.80]  Yeah, that's a great question.
[1550.32 --> 1555.68]  And it's a nice segue into a new product that we're working on at Invoca.
[1556.26 --> 1558.20]  Oh, it was perfect then. Well done, Chris.
[1558.66 --> 1558.90]  Yeah.
[1559.88 --> 1564.10]  So just to quickly answer your question about one model or multiple models.
[1564.10 --> 1579.92]  Another thing that's a little bit tricky about working on phone calls in our industry is that, you know, we have customers that might work in the healthcare industry or in the financial services industry or banking industries where they're really, really concerned about privacy.
[1580.32 --> 1585.82]  And so we have a policy with Signal AI where there's really one model per customer.
[1586.96 --> 1590.04]  And so each customer's model is only trained on their own data.
[1590.04 --> 1606.16]  So, you know, we might do, since we've transcribed millions of phone calls, you know, we might do much better if we could, say, take a whole lot of that data and pre-trained models that then get, you know, refined using each customer's data.
[1606.68 --> 1609.18]  But we've decided not to do that.
[1609.56 --> 1612.98]  And so each customer's model is trained only on their own data.
[1613.70 --> 1615.50]  And so sometimes there's not that much data.
[1615.50 --> 1619.54]  We might have to make a model with only a few hundred phone calls.
[1620.04 --> 1622.60]  That has to handle all these different regional variations.
[1623.58 --> 1632.70]  And so the way that we try to make that work in practice is partly by recognizing and stripping out hold messages as well as we can.
[1633.18 --> 1635.76]  You know, often a hold message essentially plays advertisements.
[1636.42 --> 1638.38]  And that can sound just like a purchase.
[1638.60 --> 1640.80]  And that actually can be really confusing to our models.
[1641.50 --> 1643.86]  So we try to strip that stuff out as well as we can.
[1643.86 --> 1650.86]  And then once the recorded stuff is removed, then we try to make our models really, really parsimonious.
[1651.90 --> 1661.60]  And so they only include words and phrases into their predictions if there's solid statistical evidence that they really matter.
[1661.82 --> 1663.04]  I don't know if that answered your question.
[1663.04 --> 1663.80]  Yeah, no, it did.
[1663.80 --> 1667.06]  And I'm kind of curious a little bit more on that.
[1667.32 --> 1674.82]  Like, given the sort of privacy things that you're dealing with and all of that stuff and your limitation to have this model per customer.
[1674.82 --> 1681.90]  Like, in your experience, how much data is 100 calls enough to create something useful?
[1682.16 --> 1683.86]  Or how much is needed?
[1684.04 --> 1686.90]  And then I'm assuming, are you kind of updating this over time?
[1687.02 --> 1694.34]  Is there some sort of human-in-the-loop element from the client who's able to kind of help fine-tune things over time?
[1695.00 --> 1695.70]  Yeah, absolutely.
[1695.70 --> 1699.58]  So a customer can upload some data and train their own model.
[1699.88 --> 1706.38]  Another tricky thing about our industry is, or at least in Boca's models, is we decided to make them totally self-serve.
[1707.14 --> 1710.58]  So our models are not actually trained by data scientists.
[1710.92 --> 1712.30]  They're trained by the customer.
[1713.02 --> 1716.22]  And so we really have to make them as bulletproof as we can.
[1716.80 --> 1720.90]  But a customer can upload some data and get their model up and running.
[1720.90 --> 1727.76]  And when their model makes predictions, every call that comes through in Boca gets marked now as true or false.
[1728.32 --> 1729.46]  Let's say for appointments.
[1729.74 --> 1734.74]  And then the customer has the opportunity to listen to some calls and correct them.
[1735.10 --> 1739.34]  If we mark a call as true, the customer can listen to that and say, no, that wasn't an appointment.
[1739.76 --> 1740.94]  And they give it a little thumbs down.
[1741.56 --> 1749.02]  And then through the thumbs up and thumbs down gestures, we retrain the model and it should get better over time.
[1749.02 --> 1754.24]  There's also opportunities to collect more data and upload it.
[1754.48 --> 1760.74]  Let's say as time moves on, your business grows, the conversation drifts or changes over time.
[1761.18 --> 1764.22]  You can upload new data and update the model that way.
[1764.78 --> 1771.42]  So in practice, I think 100 calls, it's awfully hard to train a model on 100 calls.
[1771.82 --> 1774.98]  That's also often what people are willing to give us at first.
[1774.98 --> 1780.62]  It's a hard sell to say, you can have this great model if you listen to a thousand calls and label them.
[1781.04 --> 1781.88]  Yeah, who wants to do that?
[1782.26 --> 1782.58]  Exactly.
[1783.24 --> 1794.20]  So even though that would make my job a lot easier, ultimately, we serve the customers and we have to make do with the amount of work that they're willing to do.
[1794.20 --> 1802.24]  Have you heard of our newest show called Brain Science?
[1802.56 --> 1803.62]  Yes, Brain Science.
[1803.74 --> 1805.40]  It's a different kind of show, I know.
[1805.76 --> 1811.18]  And it's probably one of the ones that reaches the furthest out from our typical listener audience.
[1811.36 --> 1815.16]  But this podcast is what we call for the curious.
[1815.16 --> 1826.92]  And what's cool about this show is we're exploring the inner workings of the human brain to understand things like behavior change, habit formation, mental health, and pretty much what it means to be human.
[1827.46 --> 1834.74]  If you've ever thought about why you do what you do or why others do what they do, then this show is for you.
[1835.06 --> 1840.46]  Head to changelaw.com slash brain science to listen, subscribe, and learn more about this awesome show.
[1840.46 --> 1846.96]  Here's a preview of a recent episode called One Small Act of Kindness, talking about empathy and mirror neurons.
[1847.68 --> 1851.70]  So it sounds like pliability and flexibility is a pretty crucial role, too, in relationships.
[1851.70 --> 1869.18]  Because if you're not flexible, bendable, pliable, whatever, however you want to phrase that, if you're rigid, that's only going to be difficult for you to flex, to enable change, or to, what you've said before, recalculate.
[1869.18 --> 1869.70]  Yeah.
[1869.70 --> 1876.84]  Accept new data, analyze that data, make a new plan, and iterate towards a new action.
[1877.60 --> 1877.78]  Yeah.
[1877.96 --> 1885.36]  And so one of the other things involved with this flexibility would be what researchers have discovered as mirror neurons.
[1885.98 --> 1886.14]  Right.
[1886.14 --> 1896.30]  And so mirror neurons are these neurons within the brain that help us sort of get access to another person's emotional experience.
[1896.30 --> 1907.58]  And so there's an action component in it that it was first discovered actually with monkeys and this sort of mimicry that occurred by watching somebody else do an action.
[1907.58 --> 1916.66]  Well, in the same way, I can sort of watch somebody else walk through something in terms of an emotional experience.
[1916.66 --> 1924.58]  And if I'm holding space for them in my mind, like my body physiologically, these mirror neurons come to play.
[1924.58 --> 1942.82]  Is that why people cry when they watch movies or certain movies because their mirror neurons are firing because they're watching somebody go through a situation and they're empathizing with them and can't help but encapsulate themselves into their scenario and feel what they're feeling?
[1943.04 --> 1943.82]  Is that why?
[1943.82 --> 1944.54]  Yes.
[1944.94 --> 1945.30]  Okay.
[1945.50 --> 1950.42]  So is that why anybody cries at anything when it's like, say, a movie related because that's what's happening?
[1950.60 --> 1950.74]  Yeah.
[1950.82 --> 1953.74]  Think about it sort of like this emotional contagion, right?
[1955.04 --> 1956.48]  That's interesting to put it that way.
[1957.00 --> 1963.24]  We've said mirror neurons several times, but this emotional contagion, I believe, is actually a better subtitle for mirror neurons.
[1963.62 --> 1963.96]  Mm-hmm.
[1963.96 --> 1964.80]  Yeah.
[1964.80 --> 1964.88]  Yeah.
[1965.10 --> 1976.50]  And so some of this emotional contagion or mirror neurons, like the research has been rooted in aspects of pain because if I can recognize sort of the suffering of another.
[1976.62 --> 1976.88]  All right.
[1976.90 --> 1981.54]  To keep listening, head to changelaw.com slash brainscience slash nine.
[1981.82 --> 1986.42]  That will take you to the episode titled One Small Act of Kindness.
[1987.06 --> 1990.46]  Mariel and I dig into this thing called empathy as a construct.
[1990.46 --> 1994.16]  We ask questions like what key brain structures are involved.
[1994.64 --> 2002.18]  How can we better understand empathy to be able to better navigate ourselves and our relationships with others, both at home and in the workplace?
[2002.88 --> 2005.28]  It's a deep subject, a very fun subject.
[2005.70 --> 2012.70]  Again, changelaw.com slash brainscience slash nine or search for brainscience on your favorite podcast app and subscribe.
[2013.24 --> 2014.20]  We'd love to have you as a listener.
[2020.46 --> 2035.54]  So, Mike, a moment ago you were talking about the fact that you have this customer self-service part of your process.
[2035.54 --> 2037.18]  And I found that interesting.
[2037.42 --> 2041.34]  It's an interesting choice that you made there and not something we hear all the time.
[2041.34 --> 2052.74]  I mean, I was really wondering if you would kind of take a moment and tell us a little bit about how you've made that work for you, what that customer experience is like for them to do it, and the fact that they can update.
[2052.98 --> 2056.32]  And, you know, what does it mean that they can update their model from your perspective?
[2056.82 --> 2067.14]  When a customer signs up with us, they go through a process of determining what outcomes on calls are important for their business, whether it's appointments and cancellations or purchases and new customers.
[2067.14 --> 2072.70]  And then they curate examples of training data that they then upload.
[2073.28 --> 2077.90]  And once that happens, our models train on that data kind of behind the scenes.
[2078.24 --> 2083.30]  We typically have a few different varieties that we try out and train.
[2084.44 --> 2088.28]  And then we measure how well each of these models is performing.
[2089.08 --> 2094.10]  So as they upload the data itself, are they able to initiate training?
[2094.10 --> 2102.66]  Or is that essentially just kind of flagging that there's new data there and you or somebody else on the team would then address the data and prep the data and get it ready?
[2102.84 --> 2110.08]  I guess, how automated is it between the point where they're offering the data and you're actually training on the data?
[2110.46 --> 2116.70]  I was just curious, you know, in terms of it seems like there's a whole bunch of tasks that would have to happen in there.
[2117.20 --> 2117.34]  Yeah.
[2117.48 --> 2120.52]  From my perspective on the data science team, it's totally automated.
[2120.52 --> 2123.82]  So we don't initiate anything or okay anything.
[2124.14 --> 2127.84]  So the customer uploads the data and the models train automatically.
[2128.18 --> 2130.30]  We do model selection automatically.
[2130.64 --> 2135.62]  Choose the best performing one and then offer that to the customer with some summary statistics.
[2136.10 --> 2138.80]  You know, this is how accurate the model is.
[2139.14 --> 2143.40]  If you're whether you're sensitive to false positives or false negatives.
[2143.40 --> 2146.84]  You know, these are the relevant criteria for you.
[2147.12 --> 2156.64]  And then once the customer sees this summary of the model, they can decide whether to go live with it or to wait and get more data to try to improve it.
[2156.64 --> 2164.46]  So I'm curious, you know, coming from, I guess, a more less speech perspective and more of a text perspective.
[2164.46 --> 2182.96]  I know that sometimes with like text documents from like chatbots or assistants and that sort of thing, you can do kind of unsupervised topic modeling and determine like what, you know, computationally, what are the topics that the model is kind of finding on its own?
[2182.96 --> 2186.08]  You know, and there's a few different ways to do that.
[2186.16 --> 2200.08]  But I was wondering if you've explored those sorts of ways to ease the burden on the customer to do the labeling and that sort of thing, or maybe suggest to them like, oh, it seems like there's different things happening here than over here in your data.
[2200.24 --> 2204.22]  Have you considered these things and being kind of proactive in that way?
[2204.96 --> 2206.66]  Yeah, it's like you read my mind.
[2206.66 --> 2215.26]  So the Signal AI process where a customer determines what's useful to them, labels data, uploads it and gets the model.
[2215.52 --> 2217.62]  That process works well for a lot of people.
[2217.82 --> 2222.92]  But, you know, we always want to understand what's difficult or what are the pain points for customers.
[2223.82 --> 2230.90]  And two of the main questions that people came up with was, one, can I avoid having to label data myself?
[2230.90 --> 2238.22]  And two, you know, the Signal AI, it only tells me what I ask it to look for.
[2238.54 --> 2241.02]  You know, I want AI to tell me what I don't know about.
[2241.30 --> 2243.18]  I want AI to tell me what I should be looking for.
[2243.46 --> 2255.04]  And so we've recently come up with an unsupervised model, exactly like a topic model, as you mentioned, that will chew through calls automatically without any human labels.
[2255.04 --> 2264.52]  And it'll just ingest calls from a customer and kind of passively analyze them and look for recurring themes that take place on the calls.
[2265.36 --> 2268.36]  And then present those as kind of a summary to the customer.
[2268.78 --> 2271.68]  Like, hey, we analyzed 20,000 calls.
[2272.00 --> 2274.72]  And this is what people talk about when they call your business.
[2275.50 --> 2280.64]  So first of all, you're right in that basically every time I go into a project, I don't want to label data.
[2280.76 --> 2282.62]  And I'm saying, do I really have to label data?
[2282.62 --> 2286.20]  But most of the time in my projects, the answer is always yes.
[2286.20 --> 2302.94]  But the one thing I found as I've kind of tried some of these unsupervised methods, it may be hard to kind of understand what the clusters or what the topics correspond to, even though, you know, computationally, they're distinct.
[2302.94 --> 2305.84]  Has that been a problem as you've tried to develop these methods?
[2306.08 --> 2313.86]  And how have you kind of faced some of those challenges associated with unsupervised methods in terms of, you know, how many topics do I consider?
[2314.16 --> 2316.98]  And how do I represent this to the user and that sort of thing?
[2317.52 --> 2322.34]  Yeah, this really sent me down a road where I did a lot of math.
[2322.34 --> 2328.10]  So I think it's an interesting case that often you can run an unsupervised algorithm.
[2328.56 --> 2337.02]  And just to be clear, an unsupervised algorithm is one where no human has provided labels or provided any indication of what the model should be looking for.
[2337.66 --> 2341.12]  A model just choose through raw data and looks for patterns to identify.
[2341.12 --> 2348.08]  Often, you know, these unsupervised models, they can find patterns that make sense to a computer.
[2348.68 --> 2353.64]  And they're useful for prediction and they're useful for clustering and all this sort of stuff.
[2354.24 --> 2358.52]  But if a human looks at what the patterns are, they're completely unintelligible.
[2359.52 --> 2360.70]  They make sense to the model.
[2360.86 --> 2361.82]  It makes sense to a computer.
[2361.96 --> 2363.66]  But as a human, you can't make sense of them.
[2363.66 --> 2373.40]  And so, you know, we tried to design an unsupervised algorithm that would be where every element of it would be human interpretable.
[2374.36 --> 2377.38]  And we did that by imposing a lot of restrictions on the model.
[2378.02 --> 2382.90]  And so we looked at some linguistic features that seemed important for phone calls.
[2383.62 --> 2387.48]  And we made sure that we had a mathematical model that could reproduce those features.
[2387.82 --> 2392.14]  And then we put those constraints on our model at essentially every level.
[2392.14 --> 2405.72]  So that's kind of like you did have labeled data and you tried to recreate your labeled data with the unsupervised method to validate that you're creating clusters or topics that actually made sense.
[2405.80 --> 2407.46]  Is that the kind of strategy?
[2408.50 --> 2408.92]  No.
[2409.04 --> 2411.66]  So there are no labels that are made by humans.
[2411.98 --> 2414.72]  But there are statistical properties of language.
[2415.02 --> 2415.60]  Oh, I see.
[2415.82 --> 2416.86]  We think are really important.
[2417.34 --> 2422.08]  Could you guys, for just a second, could you kind of address maybe an example of what a couple of those might be?
[2422.64 --> 2425.06]  In terms of like the characteristics you're looking for there?
[2425.76 --> 2426.00]  Yeah.
[2426.32 --> 2426.54]  Yeah.
[2426.64 --> 2429.62]  So are you guys familiar with Zip's Law?
[2430.30 --> 2434.84]  So I'm guessing that you should probably just give a brief definition.
[2435.28 --> 2435.54]  Yeah.
[2436.04 --> 2437.42]  I think this is fascinating.
[2438.10 --> 2447.66]  So Zip's Law, it turns out that if you look at a big corpus of text and you count up the occurrences of every unique word that appears in the text,
[2447.66 --> 2448.74]  and then you sort them.
[2449.82 --> 2452.66]  So you know how often the most common word is.
[2452.94 --> 2456.16]  And that word's typically in written text.
[2456.26 --> 2457.18]  It's not in phone calls.
[2457.64 --> 2460.32]  So you take the most common word and you see how often that appears.
[2460.94 --> 2465.62]  The second most common word will appear about half as often as the most common word.
[2465.62 --> 2470.96]  And the tenth most common word will appear about a tenth as often as the most common word.
[2471.58 --> 2476.00]  And the hundredth most common word will appear about a hundredth as often as the most common word.
[2476.22 --> 2476.68]  And so on.
[2477.36 --> 2481.00]  And so language really sorts itself out into this interesting relationship.
[2481.48 --> 2482.82]  And that's called Zip's Law.
[2482.82 --> 2485.72]  And I think that's important.
[2486.04 --> 2487.12]  Well, for two reasons.
[2487.34 --> 2497.52]  One is that on the Wikipedia page for Zip's Law, there's this amazing plot where someone has analyzed all of the English language Wikipedia pages.
[2497.74 --> 2500.34]  And they've made this plot for English.
[2500.84 --> 2505.44]  And of course, it follows this relationship because that's how the relationship was discovered.
[2505.44 --> 2511.60]  But then they went and did it for Spanish and for French and German and Croatian.
[2511.84 --> 2513.88]  And I think they did it for 30 different languages.
[2515.16 --> 2519.02]  And they're, you know, Latin-based languages and Germanic languages and Asian languages.
[2519.66 --> 2522.36]  And amazingly, all of them obey this relationship.
[2523.36 --> 2531.02]  And so there seems to be something really fundamental about human communication that creates this behavior.
[2531.66 --> 2535.14]  Where there's some words that are really common and they appear all the time.
[2535.44 --> 2539.10]  And then there's a long, long tail of rare words.
[2539.84 --> 2543.14]  And the rare words tend to be really specific words that have a lot of meaning.
[2543.88 --> 2547.04]  And so language tends to sort itself out into this relationship.
[2548.00 --> 2550.80]  I don't think we fully understand what creates it.
[2551.04 --> 2553.80]  But it is clear that it's a common property across language.
[2554.46 --> 2557.92]  And so that's an example of something that we really wanted our model to be able to recreate.
[2558.46 --> 2563.28]  And it's also interesting because a lot of statistical models that are kind of implicitly assumed
[2563.28 --> 2568.32]  in some common machine learning algorithms are kind of under the hood.
[2568.32 --> 2572.00]  They assume that distributions are roughly Gaussian-ish.
[2572.40 --> 2574.66]  That things roughly follow the normal distribution.
[2575.78 --> 2579.42]  And this distribution of words is completely unlike that.
[2579.68 --> 2582.16]  It breaks that assumption really, really violently.
[2582.16 --> 2588.90]  And so with these patterns that you know should be exhibited in language.
[2588.90 --> 2592.72]  So let's say that you have these 20,000 phone calls like you mentioned.
[2593.16 --> 2599.42]  And you could do some sort of topic modeling to break them up into however many topics.
[2599.42 --> 2600.70]  Let's say there's five topics.
[2600.70 --> 2613.20]  Would you then impose that sort of test on each of those clusters of calls on the transcripts to see if they follow that?
[2613.34 --> 2618.90]  Or how does that sort of test fit into the sort of clustering or the breaking up of topics?
[2618.90 --> 2626.52]  Yeah, so the way that our model is laid out, and again, it's designed so that not only a computer can understand it,
[2626.56 --> 2632.98]  but it's designed so that a human could look into the model at any piece of it and try to be able to make sense of it.
[2633.44 --> 2635.42]  We sort of laid it out hierarchically.
[2636.52 --> 2640.56]  So if you think at the very bottom, we have the data, all of the phone calls.
[2641.36 --> 2644.10]  And the phone calls have all these properties that make them hard to analyze.
[2644.10 --> 2652.76]  So the word choice follows Zip's law, this funny distribution, and there's all this uniqueness and dialect and all that.
[2653.72 --> 2655.66]  So the phone calls at the bottom are really messy.
[2656.20 --> 2661.12]  And then we want to move up through layers of abstraction.
[2662.60 --> 2670.68]  And so, you know, at the very top of the model, well, we want to say this is what has to be common across all of the calls in the data set.
[2670.68 --> 2674.12]  And, you know, if they're speaking English, that's going to be the dictionary.
[2674.46 --> 2676.84]  It's going to be the list of words that can be spoken.
[2677.84 --> 2683.36]  And that, you know, the dictionary may be an infinitely long list because people can invent new words all the time.
[2684.00 --> 2686.82]  But it's at least a countably infinite list.
[2687.34 --> 2690.66]  So that's the stuff that's common across all of the calls in the data set.
[2690.66 --> 2700.78]  And then our model works by kind of starting from the dictionary at the top and moving through these layers of specialization.
[2701.44 --> 2705.16]  And so we have this list of words that make up the dictionary.
[2705.16 --> 2716.48]  And then, you know, we know while we're speaking language and language follows this Zips law where there's some really common words and some really rare words that are still important.
[2717.32 --> 2724.26]  And so we have to derive a probability for each word that follows this power law relationship.
[2724.68 --> 2730.66]  And so that gives us, I call it a lexicon, but it's essentially the words with their associated probabilities.
[2730.66 --> 2738.88]  And then where the topic modeling comes in is we say, okay, well, the words, the dictionary defines the language you're speaking.
[2739.46 --> 2743.62]  That lexicon now defines kind of what an average phone call looks like.
[2743.90 --> 2748.66]  And so that's going to vary from one customer to the next or from one industry to the next.
[2749.44 --> 2753.80]  You know, you're going to use different words if you're calling a car dealership or a hospital.
[2754.02 --> 2757.90]  But then that lexicon, it's still too abstract.
[2757.90 --> 2761.10]  It's just telling you what an average call looks like.
[2762.28 --> 2766.12]  And so that lexicon is going to go through, again, several layers of specialization.
[2767.06 --> 2771.34]  And each of those are going to be these power law type distributions.
[2771.84 --> 2777.06]  But it's going to split that lexicon into, well, these are the words that you use if you're making an appointment.
[2777.66 --> 2778.98]  Or if you're canceling an appointment.
[2778.98 --> 2782.36]  Or if you're a new customer who's enrolling for the first time.
[2783.12 --> 2783.78]  Or so on.
[2784.56 --> 2784.84]  Gotcha.
[2784.84 --> 2791.94]  So you have the commonalities of the language and how words are used in the language.
[2792.12 --> 2797.66]  It sounds like your goal in developing the unsupervised method is then to take things those steps lower.
[2797.90 --> 2802.88]  Where you, what you're really trying to develop are those probabilities of,
[2803.36 --> 2807.98]  or the power laws associated with the words associated with reservation.
[2807.98 --> 2809.80]  Or the words associated with purchase.
[2809.80 --> 2811.58]  Or with making an appointment.
[2811.58 --> 2813.94]  Or whatever the thing is.
[2814.08 --> 2823.02]  So you have these sets of calls that have a certain more distinct statistical relationship amongst themselves that allow you to separate them out.
[2823.24 --> 2826.02]  That's kind of the goal that I'm picking up on.
[2826.22 --> 2827.26]  Did I say that right?
[2827.82 --> 2827.98]  Yeah.
[2828.10 --> 2829.02]  No, that's exactly right.
[2829.22 --> 2831.84]  We want our topics to kind of float above the data.
[2832.36 --> 2834.86]  The topics, you know, because all calls are going to be different.
[2834.86 --> 2838.74]  And everyone has their own dialect and their own individual problems.
[2839.34 --> 2841.36]  So none of the conversations are going to be the same.
[2841.70 --> 2849.52]  We want the topics to be something that kind of floats above that data set and represents the themes that are consistent throughout it.
[2849.76 --> 2857.04]  And we do this through this sort of process of hierarchically splitting the dictionary into these probability distributions.
[2857.04 --> 2863.48]  And then to try to make sure that our models are interpretable, we don't want to fit those topics directly to the data.
[2864.10 --> 2868.04]  You know, so we take the lexicon and we split it into the topics that you talk about.
[2868.46 --> 2872.20]  And then each topic we say, well, you know, this is a phone call.
[2872.26 --> 2873.68]  You've got a caller and an agent.
[2873.98 --> 2876.76]  And they have totally different roles in the conversation.
[2876.76 --> 2884.46]  And so if I'm calling to make an appointment, well, the words that I say are going to be totally different from the words that the agent says.
[2885.14 --> 2887.34]  And so we go through another exercise of the splitting.
[2887.56 --> 2901.16]  And then to handle individual dialects and regional variations across the country, we also actually take a really extreme step where all of those caller side topics are then split.
[2901.16 --> 2905.60]  And every caller gets their own personal variant of each topic.
[2906.14 --> 2906.28]  Gotcha.
[2906.76 --> 2912.94]  So that's the process by which, you know, we're looking for patterns that are consistent all the way across the data set.
[2913.30 --> 2917.42]  And so we've got the data at the bottom, you know, that's totally messy and totally idiosyncratic.
[2917.64 --> 2921.34]  It has all this rich, interesting information, but it's too much information.
[2922.02 --> 2925.18]  And then at the top, you know, we've got the dictionary, which is kind of uninteresting.
[2925.38 --> 2928.10]  We can all agree on it, but there's not that much information there.
[2928.28 --> 2933.66]  And then we go through these successive layers of specialization to get these two ends to meet.
[2933.66 --> 2939.08]  And then at the middle, you know, that's where we have the topics and that's what we present to the customer.
[2939.08 --> 2949.38]  And so by doing that and by tuning the math pretty carefully to match this FIPS law, I think we made something that where we end up with really interpretable results.
[2949.38 --> 2961.12]  So I guess as we wind up here, what are you excited about in terms of the future of unsupervised language methods and AI and conversational data or other related topics?
[2961.32 --> 2962.80]  What does it look like for you going forward?
[2962.80 --> 2974.00]  Well, something that I'm actually really interested in now, you guys mentioned earlier, the possibility of having some labeled data and using that to inform the topic model.
[2974.78 --> 2978.10]  That's actually something we're working on prototyping right now.
[2978.18 --> 2979.20]  And I'm really excited about.
[2979.20 --> 2987.68]  And that's a case where we could have a semi-supervised model where, you know, let's say going back to the signal AI problem.
[2988.38 --> 2993.22]  If someone says, appointment set is important for me, but I'm only going to give you 100 calls.
[2993.78 --> 2997.20]  I may have 100,000 calls that are unlabeled.
[2997.20 --> 3017.66]  And so designing a model that's semi-supervised that can accept some labeled calls and some unlabeled calls, use the labels to inform the topics so that I get not just the words and phrases, but all of the conversation topics that are relevant to this and using that to make a more powerful predictive model.
[3017.76 --> 3019.98]  That's the direction that we're headed at the moment.
[3019.98 --> 3025.76]  Cool. That sounds exciting and something that I could talk with you about for many hours.
[3025.96 --> 3028.30]  But unfortunately, our time has come to an end.
[3028.40 --> 3032.18]  Hopefully, we can stay connected and keep the conversation going.
[3032.42 --> 3041.52]  But really appreciate you joining us to talk about this stuff and chat about how to develop insights from speech and conversational data.
[3041.62 --> 3044.14]  It was really interesting and appreciate you joining us, Mike.
[3044.32 --> 3045.68]  Well, thanks so much. I really enjoyed it.
[3045.68 --> 3050.32]  Thanks for listening to this episode of Practical AI.
[3050.78 --> 3053.30]  Do you know someone who's trying to break into the AI game?
[3053.42 --> 3054.02]  Send them our way.
[3054.30 --> 3058.64]  We appreciate every recommendation because word of mouth is how people hear about podcasts.
[3059.48 --> 3061.24]  Shoot them a quick email or a Slack message.
[3061.40 --> 3062.38]  Put out a tweet, whatever.
[3062.78 --> 3063.52]  Or get crazy.
[3063.88 --> 3064.58]  Get up from your desk.
[3064.68 --> 3068.12]  Walk across the room and tell them in real life, hey, might start a good conversation.
[3068.50 --> 3071.08]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[3071.08 --> 3075.50]  It's produced by me, Jared Santo, with music by the oh-so-mysterious Breakmaster Cylinder.
[3075.68 --> 3077.30]  And we're brought to you by awesome sponsors.
[3077.46 --> 3077.96]  Support them.
[3078.06 --> 3078.76]  They support the show.
[3079.04 --> 3082.28]  We've got Fastly on bandwidth, Linode on hosting, and Rollbar on bugs.
[3082.62 --> 3084.28]  If you haven't yet, hit up our master feed.
[3084.38 --> 3085.80]  Your neural networks will thank you.
[3086.08 --> 3088.54]  It's all Change Dog podcasts in one easy subscription.
[3088.98 --> 3090.24]  Get it for the price of a free hot dog.
[3090.52 --> 3091.26]  Thanks again for listening.
[3091.46 --> 3092.18]  We'll talk to you next week.
[3092.18 --> 3092.20]  We'll talk to you next week.
[3092.20 --> 3094.18]  We'll talk to you next week.
[3094.18 --> 3096.18]  We'll talk to you next week.
[3096.18 --> 3104.18]  We'll talk to you next week.
[3105.68 --> 3107.72]  Bye.
[3108.06 --> 3108.22]  Bye.
[3108.24 --> 3112.32]  Bye.
[3112.34 --> 3114.50]  Bye.
[3115.00 --> 3115.28]  Bye.
[3119.50 --> 3122.52]  Bye.
[3122.76 --> 3124.42]  Bye.
[3124.96 --> 3127.10]  Bye.
[3127.36 --> 3128.32]  Bye.
