[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.38]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to linode.com slash changelog.
[15.36 --> 18.62]  This episode is brought to you by Linode, our cloud server of choice.
[18.82 --> 21.88]  And we're excited to share they've recently launched dedicated CPU instances.
[21.88 --> 38.78]  If you have build boxes, CI, CD, video encoding, machine learning, game servers, databases, data mining, or application servers that need to be full duty, 100% CPU all day, every day, then check out Linode's dedicated CPU instances.
[39.34 --> 43.44]  These instances are fully dedicated and shared with no one else.
[43.52 --> 47.46]  So there's no CPU steal or competing for these resources with other Linodes.
[47.72 --> 51.40]  Pricing is very competitive and starts out at 30 bucks a month.
[51.40 --> 55.60]  Learn more and get started at linode.com slash changelog.
[55.70 --> 57.82]  Again, linode.com slash changelog.
[68.68 --> 76.22]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[76.34 --> 81.10]  This is where conversations around AI, machine learning, and data science happen.
[81.40 --> 85.88]  Join the community and snag with us around various topics of the show at changelog.com slash community.
[86.20 --> 87.04]  Follow us on Twitter.
[87.14 --> 88.64]  We're at Practical AI FM.
[89.16 --> 89.96]  And now onto the show.
[94.50 --> 104.24]  Welcome to another fully connected episode of Practical AI, where we're going to keep you fully connected with everything that's happening in the AI community.
[104.24 --> 108.26]  And we'll also take some time to discuss the latest AI news.
[108.26 --> 113.28]  We'll dig into learning resources and help you level up your machine learning game.
[113.60 --> 121.52]  So I'm joined by my co-host, Chris Benson, who is a chief AI strategist with Lockheed Martin RMS APA Innovations.
[121.78 --> 126.00]  And I'm Daniel Whitenack, a data scientist with SIL International.
[126.36 --> 127.64]  So how are you doing, Chris?
[127.70 --> 129.00]  Welcome back from your travels.
[129.40 --> 130.66]  Yeah, thank you very much, Daniel.
[130.74 --> 131.66]  It's good to be back.
[131.66 --> 138.48]  I was, as you know, in London recently for the Applied AI conference that was there.
[138.86 --> 141.60]  Sounds right within our wheelhouse on Practical AI.
[141.82 --> 142.84]  It definitely was.
[142.92 --> 146.08]  I was given the honor of giving the opening keynote, which was a whole lot of fun.
[146.40 --> 150.40]  I also got to meet some interesting and record some interesting people there.
[150.50 --> 153.66]  So hopefully there may be some episodes coming up that have to do with that.
[153.88 --> 154.12]  Awesome.
[154.24 --> 154.92]  Can't wait to hear them.
[155.10 --> 155.70]  So how about you?
[155.76 --> 156.40]  What have you been up to?
[156.40 --> 159.12]  I came back from vacation recently.
[159.38 --> 163.44]  So catching up on all things email and message and all of that.
[163.54 --> 166.88]  And finally digging into some some projects again.
[167.26 --> 171.82]  I'm excited to get a little bit more hands on this week.
[172.36 --> 172.80]  Excellent.
[173.32 --> 180.56]  Well, we've had a lot happening since our last episode out there and wanted to kind of dive on into it.
[180.56 --> 193.18]  A lot of our listeners are probably already aware, but, you know, we're always talking about AI in the context of different countries are doing and what's happening in the private sector versus government and things like that.
[193.18 --> 215.44]  And recently, on February 11th, 2019, the White House issued their executive order on maintaining American leadership in artificial intelligence, which is significant because many of us in the AI community and beyond had been waiting to hear if the U.S. was going to have a national AI strategy issued from the top level.
[215.56 --> 216.74]  So it is out there.
[216.84 --> 218.34]  And today we're going to talk about that.
[218.86 --> 219.66]  Yeah, it's exciting.
[219.86 --> 220.64]  Exciting stuff.
[220.74 --> 222.12]  Well, maybe exciting stuff.
[222.12 --> 222.52]  We'll see.
[222.52 --> 223.52]  It is.
[223.60 --> 237.70]  Now, I want to do something slightly unusual in that since we're talking about something that is fairly close in some areas to what I do at work, I want to explicitly note that the opinions that I express on the show are strictly my own and they are not in any way representing Lockheed Martin.
[238.18 --> 242.86]  And because I love my job and I want to make sure that everyone knows I'm just speaking for myself.
[243.30 --> 246.26]  So I probably won't do that very often, but I will in this show.
[246.58 --> 246.94]  Awesome.
[246.94 --> 253.46]  Well, I was looking through this, you know, when it came out, the executive order.
[254.66 --> 266.50]  There's a lot of different sections of it that we'll kind of explore, but it has things related to policy and principles and objectives and even data and computing resources.
[266.50 --> 277.48]  What I think is interesting is it seems a little bit like the U.S. is a little bit late to the game with respect to with respect to this executive order.
[277.48 --> 288.46]  I know on a previous show of ours, you pointed us to an article about artificial intelligence strategies, and I see that they have kind of a timeline on that.
[288.46 --> 302.32]  It's a medium article we'll link in the show notes, but there have been a whole bunch of these national strategies that have come out around AI from Canada back in 2017, China, Taiwan.
[303.44 --> 307.08]  Let's see, France, Australia, Korea.
[307.08 --> 313.16]  So this is kind of definitely in line with what other countries have been doing.
[313.34 --> 317.40]  So it wasn't so much of a surprise to see it from our government.
[317.52 --> 319.76]  I don't know about from your perspective, Chris.
[319.76 --> 331.34]  No, I think, I mean, obviously there are many organizations in the private sector, academia and in the government in terms of various government agencies that have been involved in AI.
[331.34 --> 338.56]  And many of those organizations, both private and public, have put out AI strategies of their own.
[338.64 --> 345.22]  But I think all of us have been waiting quite a long time for a national strategy, something at the highest levels of government that we're doing.
[345.42 --> 351.86]  And so now that that is out, we wanted to kind of dissect it and talk about the good, the bad and the ugly with it.
[352.28 --> 356.68]  And so I'm kind of looking forward to figuring out how it relates to the rest of it here.
[357.28 --> 357.76]  Yeah, definitely.
[357.76 --> 365.60]  And I know before our show, you did a little bit of research as far as kind of the origins of the executive order.
[366.08 --> 370.94]  Obviously, being an executive order, it kind of comes from the White House or the president.
[371.46 --> 376.60]  But you kind of found out a little bit more information about who might have had some input here.
[376.82 --> 377.56]  Do you want to share that?
[378.00 --> 378.12]  Sure.
[378.26 --> 382.26]  Just as part of kind of figuring out who might have written the document, I'm going to speculate.
[382.44 --> 386.06]  So I don't have any specific knowledge of who wrote it.
[386.06 --> 387.96]  But I was kind of looking around.
[388.32 --> 398.86]  I'm guessing that the actual executive order was probably put together by Dr. Lynn Parker, who is the assistant director for artificial intelligence at the White House Office of Science and Technology Policy.
[399.12 --> 410.60]  And she would have, if she was that person or whoever was, probably would have had input from a number of senior level U.S. officials, have various interests in technology and government policy.
[410.60 --> 418.74]  One of those was likely Michael Kratzios, who would be the deputy assistant to the president for technology policy at the White House.
[419.02 --> 424.32]  They may have also gotten some feedback from people at the Department of Defense and other agencies.
[424.76 --> 426.24]  But I don't have any firm knowledge.
[426.38 --> 434.30]  I was just trying to, as I, when I finished the executive order, I thought it was fairly well written in terms of kind of laying out some of the issues.
[434.30 --> 439.92]  It was written by somebody in the know, but probably somebody without a whole lot of resources at their disposal.
[440.42 --> 440.46]  Right.
[440.62 --> 448.60]  Someone that might know really good directions, but might not have the authority to actually implement a lot of concrete things.
[448.96 --> 449.32]  Right.
[449.44 --> 461.02]  It's kind of, and I say this a little tongue in cheek, if you or I might have written it knowing that we might not have any authority within us to be able to make stuff happen at the top levels of government.
[461.02 --> 464.98]  But, you know, so I think it was, I think it was well written, all things considered.
[465.22 --> 478.98]  And I certainly want to note that in my opinion, I think it has to be a very tough job to be in a government advisement position and understand the implications of some of these technologies without really having a whole lot available to do something with it.
[479.02 --> 480.78]  And that's a personal opinion I hold.
[480.78 --> 486.20]  So I have some sympathy for whoever did write the EO, the executive order on this.
[486.20 --> 486.72]  Yeah.
[487.16 --> 498.74]  And I mean, we mentioned that a lot of other countries have issued these, but I think probably at the top of people's mind is China's recent stance on AI.
[498.74 --> 516.52]  Even back in 2017, they kind of published this whole plan of artificial intelligence development in which they wanted to become the world leader in AI and attach to that a bunch of funding, which we'll talk a little bit more about.
[516.90 --> 524.32]  And kind of as a first step of that, the plan was to catch up with the US on AI technology and applications by 2020.
[524.60 --> 526.28]  So that's just around the corner.
[526.28 --> 540.28]  And so I imagine that some of that pressure from that plan and the immediate goals of it also maybe spurred or motivated the release of this document.
[540.72 --> 541.46]  Yeah, I would agree.
[541.76 --> 544.42]  I think, you know, there have been a lot of other countries.
[544.62 --> 547.82]  You named a whole bunch of them earlier that have jumped out there.
[547.82 --> 554.80]  So like we started the show with, we've been waiting for a while on this and at least something is out.
[555.30 --> 560.14]  Frankly, we might be hoping for some iterations on this down the road, but we'll see where we go on that.
[560.82 --> 571.10]  I know that, you know, previously there have been research reports on the state of AI and stuff, but not an overall cohesive agenda that's been laid out at the federal level.
[571.10 --> 576.38]  Cool. Well, let's maybe jump into what's in the executive order itself.
[576.64 --> 579.78]  And I'd love to hear some of your perspectives on that, Chris.
[580.00 --> 586.10]  In general, kind of overall, there's five major areas of action within the executive order.
[586.62 --> 595.94]  And we'll, of course, post links to the executive order itself and a few articles that we found useful in terms of responding to the executive order.
[596.02 --> 598.38]  We'll put those in the show notes for the episode.
[598.38 --> 599.78]  So make sure and check those out.
[600.06 --> 604.26]  But overall, the executive action has five major areas.
[604.26 --> 609.88]  The first is having federal agencies increase funding for AI research and development.
[610.44 --> 615.28]  The second is making federal data and computing power more available for AI purposes.
[616.08 --> 620.00]  The third is setting standards for safe and trustworthy AI.
[620.52 --> 623.46]  The fourth is training an AI workforce.
[623.46 --> 632.66]  And the fifth is engaging with international allies with the caveat of protecting the tech from foreign adversaries.
[632.66 --> 639.12]  So those are kind of the five sections if you read through the executive order.
[639.30 --> 643.46]  So let's maybe start with this area of AI research and development.
[643.78 --> 652.62]  So it's definitely clear from the executive order that there is a need to increase research and development activity in AI.
[652.62 --> 657.64]  What was your thoughts about how they presented that in the executive order, Chris?
[658.04 --> 678.40]  Well, kind of going back to they said many of the right things, but without the detail that's needed, they kind of laid out the bullet points that I think most of us in the AI world would probably tend to agree to, which is why I do think the actual text was written by somebody in the field and not just maybe a policy person who doesn't expect that.
[678.40 --> 683.40]  But since it doesn't have the detail, you know, detail usually comes from initiative.
[683.66 --> 686.60]  It comes from the fact that you're wanting to change the game.
[686.90 --> 695.42]  And to some degree, the R&D says basically, let's go do R&D without going into specific somewhat areas and why it could have done a lot more in that area.
[695.42 --> 701.06]  And as we go forward, I'll kind of talk a little bit more about it as we get to kind of what's not in the executive order.
[701.64 --> 701.76]  Yeah.
[701.88 --> 721.60]  In the objective section, which is section two, you know, first under there is basically they just say promote sustained investment in a AI R&D in collaboration with industry, academia, international partners and allies and all other non-federal entities to generate technological breakthroughs.
[721.60 --> 727.26]  And of course, they say a few other things related to AI budgeting and other things.
[727.40 --> 729.32]  But yeah, I kind of agree with what you're saying.
[729.48 --> 739.00]  They're saying that this is something that we need to pursue, but we're relatively light on the details of how that actually is going to happen.
[739.08 --> 741.64]  So it's good that they're promoting AI R&D.
[741.90 --> 745.26]  It's not clear at all to me where things will go from there.
[745.26 --> 763.08]  Sure. And, you know, and even going on to the next point where they talk about kind of making the federal data and computing power available for AI purposes, as you mentioned before, it's very generic talk in it about sharing data models and computing resources with researchers in the private sector.
[763.08 --> 767.74]  And it notes that agencies are expected to help those researchers access those resources.
[768.40 --> 770.02]  But, you know, kind of stops at that point.
[770.10 --> 778.64]  So it kind of states the obvious on what on what we need to do in the background without making any kind of leap or strong directive in a detailed sense.
[778.96 --> 785.16]  Yeah, this one was it kind of made me think a little bit because there is a lot of government data available now.
[785.16 --> 797.08]  And in my experience in working with government data on various projects, it's not so much that it's not available, but that it's incredibly hard to work with and access.
[797.08 --> 816.02]  I don't know if you've worked with government data in general and their APIs and such, but for me, at least with the ones that I worked with, they were kind of prohibitively slow and hard to hard to parse and other things, which caused me to have to implement a lot of data caching and all of these sorts of things when I was working with.
[816.12 --> 818.20]  I forget which API I was working with.
[818.20 --> 821.88]  So I wonder if, you know, I mean, a lot of this data is already available.
[822.14 --> 826.92]  So I'll be curious to note how they are wanting to promote access.
[827.38 --> 835.24]  I would be skeptical to think that they're going to, you know, improve all of their APIs and, you know, go in that direction.
[835.38 --> 837.04]  It's a very slow process.
[837.36 --> 840.74]  I don't know that they could really do a lot very quickly there.
[840.84 --> 845.40]  So I'm not sure about the directions that they have in mind, I guess, with that one.
[845.52 --> 846.00]  Sure.
[846.00 --> 853.00]  I guess moving on a little bit, they did note that an ethics aspect, which I am glad to see there.
[853.80 --> 862.62]  It doesn't go, again, into great depth, but at least, you know, they noted that civil liberties, I think that was mentioned several times in the piece.
[862.62 --> 884.36]  And so if you compare it to what China is doing with their surveillance state, which is very much AI driven, surveilling and having a score associated with every citizen in China, I'm glad to see that we are at least keeping that kind of ethical concern over the negative aspects of AI that would be potential.
[884.36 --> 886.78]  In other words, what bad actors would be, I might choose to do.
[886.94 --> 890.36]  So that was good to see that, to talk about the positive.
[890.48 --> 891.80]  I just wish they had gone into more detail.
[891.92 --> 892.76]  Any thoughts on that?
[893.28 --> 893.40]  Yeah.
[893.68 --> 894.86]  I mean, it is interesting.
[895.12 --> 914.12]  I mean, I have no idea of knowing exactly what our U.S. government is doing, but it is interesting and kind of how the U.S. is home to many large organizations that have shown really poor and concerning use of data over the past couple of years.
[914.12 --> 927.14]  So even though the government might say, oh, we're not going to do this with AI, and I hope that they don't do certain things like, you know, utilize facial detection, you know, extensively and assign me a score.
[927.14 --> 949.38]  I think one of the interesting things will be if they're actually willing to put regulations in place to help regulate those large tech corporations that have been shown to have concerning methodologies around the things that are how they treat data, how they share it, how they sell it, all of those sorts of things.
[949.38 --> 957.62]  So I think I'm interested in more seeing that intersection between the private and public sector in terms of regulation.
[958.02 --> 958.12]  Yep.
[958.22 --> 959.36]  I agree with you completely.
[959.76 --> 964.32]  And the other thing you noted earlier when you were going through the bullets was training workers.
[964.96 --> 969.14]  And, you know, essentially, this is calling for educational grants to be established.
[969.50 --> 970.84]  And that's great.
[971.00 --> 972.82]  I like the call for that.
[973.20 --> 974.90]  And I think that is a useful thing.
[974.90 --> 980.66]  I just wish I had seen a little bit more in terms of actual federal commitment to going and doing this.
[980.78 --> 984.18]  I think this is going to be a huge issue going forward.
[984.50 --> 989.82]  And we have the most transformative technology maybe ever that is going to impact our lives.
[990.00 --> 996.32]  And so I think the idea of getting the workforce into alignment with this is pretty critical.
[996.32 --> 997.04]  Yeah.
[997.20 --> 1008.50]  After I mean, we've said this many times on the show that not all tech people might end up working as AI practitioners or as researchers.
[1008.50 --> 1015.64]  But even, you know, most software engineers are going to be interacting with AI at somewhere in the software stack.
[1015.64 --> 1018.02]  And it's going to be a major part of business strategy.
[1018.02 --> 1030.92]  And so people that even aren't AI practitioners necessarily are going to need some exposure to what AI is, how to interact with it, what the concerns are, how these systems work.
[1031.06 --> 1037.40]  I think that level of education is something that we could definitely see some improvement on.
[1037.40 --> 1041.98]  So, you know, we've kind of talked about what's what's in the executive order.
[1042.48 --> 1047.92]  And I'm sure our listeners are hearing a little bit of disappointment across a number of those.
[1047.92 --> 1056.38]  So let's kind of cut to the chase and let's talk about what we are not seeing in the in the executive order issued by the White House.
[1056.38 --> 1069.90]  And I guess to start us off, I'll throw out the idea of what I was hoping to see, given the fact that we are in, you know, a critical juncture where we're trying to maintain in the U.S.
[1070.52 --> 1073.48]  a superior level of AI expertise.
[1073.48 --> 1087.52]  And we are identifying in this moment, politically speaking, China as sort of an adversary in the space is I was hoping to see more of a powerful national vision that would commit the U.S.
[1087.52 --> 1091.68]  to maintaining global leadership in the artificial intelligence space.
[1091.68 --> 1104.14]  I guess considering just how important this technology is and will continue to be in the future, transforming the world around us, not just jobs, but the way we live our lives and stuff.
[1104.14 --> 1121.54]  I would love to have seen something along the lines of John Kennedy's moonshot speech to Congress where he he in 61, he put the nation on a course to land on the moon by the end of the decade, you know, because he recognized how important it was to be.
[1121.68 --> 1124.50]  A leading power in the space race.
[1125.00 --> 1138.90]  And so considering that, at least in my own personal view, I think AI is every bit as important to the future of the country and in all countries, I would have loved to have seen something a little bit more powerful than that.
[1139.38 --> 1139.52]  Yeah.
[1139.78 --> 1151.66]  And I think if we kind of look back to that moonshot speech and kind of go back to thinking about the space race, although I certainly don't want to make it out to where I'm going to be.
[1151.68 --> 1163.64]  You know, we certainly we don't think on this show that, you know, we as the U.S. are better than Chinese AI researchers or something and we don't want to promote division.
[1163.64 --> 1170.40]  But at the same time, I would be very excited to see the U.S. lead in this in this area.
[1170.54 --> 1184.80]  And similar to kind of the Cold War space race era when they were really pursuing space technology, something that was, you know, directly connected to our advances in that area was funding.
[1184.80 --> 1198.24]  Right. And as far as this executive order goes, it kind of lays out that we should be doing a lot of these things, but it doesn't actually allocate any federal funding towards executing this vision.
[1198.24 --> 1213.80]  So I feel like if they do really have this vision that we should be leaders in in AI, you know, there has to be funding associated with that, you know, and there has to be a plan for funding associated with that that really isn't found in this executive order.
[1213.80 --> 1228.98]  So, Daniel, you absolutely called out the elephant in the room and everybody I know that had this interest as we do and as our listeners do in this area and was hoping to see great things.
[1228.98 --> 1237.74]  That was the number one comment that I heard from people that I know as we all consume this document was, where's the funding?
[1238.06 --> 1248.38]  You know, how can you tell us that this is so important to to America's own interest to be able to drive forward in this area if you're not going to allocate funding to do that?
[1248.38 --> 1262.20]  You know, to draw the analogy with the moonshot, there was funding made to NASA to be able to accomplish this, you know, tremendous challenge that President Kennedy issued to the country.
[1262.64 --> 1268.70]  And that was not just to point out that was that was not, you know, just a government or military thing.
[1268.70 --> 1270.66]  It was a it was a societal effort.
[1270.66 --> 1275.00]  It was something where we're all going together, going to go do a great thing.
[1275.52 --> 1282.10]  And and that is that is what I don't think is is present in this executive order is there.
[1282.26 --> 1286.76]  They speak toward things they'd like to do, but there's no funding to drive it.
[1287.08 --> 1296.60]  And therefore, you know, I fail to see how the White House is truly leading the way into getting us into the future that we all together need to be in.
[1297.14 --> 1299.50]  And so that's my own personal perspective.
[1299.50 --> 1321.68]  Yeah. So just to kind of make things more specific, really what the executive order does say around funding, at least for R&D sorts of things, is it asks federal agencies to prioritize research in AI by reallocating resources within their existing budget.
[1321.86 --> 1325.96]  So these federal agencies are already funding research.
[1326.14 --> 1326.36]  Yep.
[1326.36 --> 1336.20]  So I'm assuming we're talking about the NSF and the DOE and all of these organizations or agencies, I should say, that are already funding research.
[1336.20 --> 1339.98]  Like when when I was in my Ph.D., we were funded by the DOE.
[1340.44 --> 1350.42]  So they're already funding certain things and they're really not saying, you know, you're going to get more money to support AI funding.
[1350.42 --> 1357.30]  But we're asking you to prioritize that, which means that funding for other things will obviously go down.
[1357.30 --> 1361.04]  The problem is, is that those agencies are already doing that.
[1361.12 --> 1368.20]  The ones that have they have smart people in these agencies and they they have seen AI coming.
[1368.36 --> 1371.64]  They have recognized how it could be useful in their own domains.
[1371.64 --> 1375.76]  And they're already allocating funds that are existing into there wherever they can.
[1375.76 --> 1380.48]  And so the problem there is that the executive order doesn't change that in any way.
[1380.54 --> 1386.02]  It's basically it's basically calling them to calling on them to do something that they're already doing.
[1386.02 --> 1404.62]  Yeah, yeah, exactly. So if we if we kind of compare this to China's approach with funding AI, we can see that China explicitly is stating that it's spending one hundred and fifty billion on AI between now and 2030.
[1404.62 --> 1417.22]  And then even individual cities, there's certain individual cities that are spending upwards of 15 billion on AI initiatives within the cities.
[1417.22 --> 1420.50]  So they're already making that commitment.
[1420.50 --> 1428.40]  They're executing on, you know, China is executing on this vision to become leaders in AI and they're putting money behind it.
[1428.40 --> 1445.10]  And I think that, as you've already stated in the analogy with the space race, I think that trickles down not only to the government and defense organizations, but it trickles down to universities, even, you know, high schools and lower level education where people are really emphasizing STEM education.
[1445.10 --> 1448.66]  They're getting educational grants. There's resources available.
[1449.04 --> 1456.18]  There's a whole trickle down effect from that money being behind the vision and people being on board with it.
[1456.18 --> 1460.62]  Yeah, there's the dichotomy between what China is doing.
[1460.76 --> 1467.00]  You know, they truly have put a moonshot level initiative into place and they're backing it with the funds.
[1467.14 --> 1469.70]  And I truly respect them for doing that.
[1469.94 --> 1473.24]  They clearly get it and they get it at all levels of government.
[1473.82 --> 1476.32]  And frankly, nothing against China at all.
[1476.42 --> 1479.16]  I think that, you know, they're doing what I would do if I was in their shoes.
[1479.16 --> 1485.92]  I wish that the United States would would take a similar initiative on our side at the same kind of level.
[1486.18 --> 1491.34]  I think we will feel the pain down the road if we don't write that boat fairly soon.
[1491.56 --> 1496.62]  And I think there's a I wanted to recommend originally I heard about a particular book.
[1496.70 --> 1501.34]  It was actually my boss, Matt Tarascio, who actually told me about it.
[1501.44 --> 1505.62]  It's called AI Superpowers, China, Silicon Valley and the New World Order.
[1505.62 --> 1507.78]  And the book is it's great book.
[1507.84 --> 1508.62]  I highly recommend it.
[1508.62 --> 1515.80]  It makes a strong argument that China is probably doing much better than most of us in the West have given them credit for.
[1516.16 --> 1521.88]  We really we have a bias in the U.S. about our leadership and AI as we like to talk about it.
[1522.18 --> 1529.00]  The book would argue that, you know, we may not be quite in the leadership position that we think we are if we're being honest with ourselves.
[1529.00 --> 1531.34]  And I think that that is an important point to take home.
[1531.34 --> 1545.92]  Whether the book is is exactly on on point or not, it it should call us to attention that it is not a foregone conclusion that the United States would automatically be the dominant power in the artificial intelligence domain.
[1545.92 --> 1553.98]  And so I think that that is that is pretty key right there that we really need to do, in my opinion, what China is doing.
[1553.98 --> 1558.24]  So I think more power to them for for doing what they think is right.
[1558.62 --> 1560.20]  Great people, great country.
[1560.60 --> 1562.94]  I just wish we could learn a lesson from the Chinese on that one.
[1563.52 --> 1563.64]  Yeah.
[1563.78 --> 1572.24]  And I think you're really getting at kind of a last point that I've really seen people talk about a lot in in respect to this executive order.
[1572.24 --> 1589.80]  And it really stems from the fact that, you know, we do have this bias in the U.S., many of us that even the title of the executive order, you know, maintaining leadership in in A.I., you know, kind of implies that U.S. natives are the best at the best at A.I. that there is.
[1589.80 --> 1595.80]  But the fact of the matter is some of the most brilliant minds in A.I. have not come from the U.S.
[1596.22 --> 1602.60]  And many of the most brilliant minds in A.I. that are in the U.S. have immigrated to the U.S.
[1602.98 --> 1615.06]  And so the U.S., you know, at least in the past, has really taken a great stance on importing a lot of great minds into into the country and been open about that.
[1615.06 --> 1624.80]  But it's become, you know, increasingly hard to get students that come here and study computer science, for example, that study A.I. that are doing A.I.
[1624.88 --> 1625.56]  PhDs.
[1626.02 --> 1631.72]  It's it's getting increasingly hard for them to be able to stay here and contribute to U.S.
[1631.96 --> 1633.14]  led companies.
[1633.62 --> 1637.32]  I know this is something that OpenA.I. has talked about a lot.
[1637.32 --> 1643.70]  I know it's something that, you know, has impacted me a lot, seeing friends of mine who has in Ph.D.
[1643.78 --> 1650.80]  program with and have worked with over time, just really, you know, not having the desire to stay in the U.S.
[1651.24 --> 1659.44]  because of all the issues around visas and all of those things and just deciding to either go back to their home country or become A.I.
[1659.50 --> 1661.18]  practitioners in another country.
[1661.18 --> 1667.92]  So I think that this is something that really is at the core of what needs to be addressed for us to maintain leadership.
[1668.44 --> 1669.48]  I completely agree with you.
[1669.56 --> 1679.84]  I think that there is once upon a time, a few decades back, Ronald Reagan, another Republican president, used to refer to America as a shining city upon a hill.
[1679.84 --> 1691.12]  And the idea around that was no matter where in the world you were, America had this reputation as being the place where you could, if you're willing to work hard, you could make anything happen.
[1691.32 --> 1704.80]  And and accordingly, so many immigrants from around the world that were ready to accept that challenge developed tremendous interest in and loyalty to the United States and wanted to come here and bring their families here and help America along.
[1704.80 --> 1708.94]  I think that we're at risk of losing that in the current climate.
[1709.42 --> 1718.94]  And we're now taking some of these great minds that would otherwise love to come and be part of this American experience and and asking them to to go back to wherever they came from.
[1719.06 --> 1721.70]  And of course, they're going to take that expertise with them.
[1722.24 --> 1725.62]  So it's not just the the immigrants that are losing out.
[1725.74 --> 1726.80]  It is our country itself.
[1726.80 --> 1733.12]  It's losing out on these great minds to help us in this next great age where artificial intelligence plays such a major role.
[1733.12 --> 1734.36]  Yeah, definitely.
[1735.18 --> 1761.44]  Increasingly, you know, when it's becoming easier to run a company outside of the major tech hubs, like let's say San Francisco or New York and having a company that's fully distributed and that sort of thing, there's it's hard to convince people that, you know, living in living in San Francisco to create your company is really the best choice, especially with all of these visa issues and all of that.
[1761.44 --> 1766.20]  So kind of getting to some overarching general thoughts.
[1766.70 --> 1780.44]  My my general thoughts on on this executive order are probably not a surprise based on my previous comments in that, you know, I'm kind of skeptical as far as the actual change that will be sparked by the executive order.
[1780.44 --> 1788.46]  Given that all of the agencies and the companies and the educational organizations already see the advantage of A.I.
[1788.84 --> 1794.86]  and are already making efforts with within their own power to promote A.I. research and development and education.
[1794.86 --> 1801.06]  I think the thing that would spark more change would be actual funding and next steps.
[1801.20 --> 1805.32]  So I'm I'm skeptical that this executive order on its own will change anything.
[1805.32 --> 1815.50]  But I'm definitely hopeful that maybe there will be some next steps coming along with it that will provide actionable items like funding and programs and that sort of thing.
[1815.50 --> 1819.94]  And I completely agree with what you just said and that and I subscribe to that.
[1820.48 --> 1825.02]  I think it's interesting, you know, from that overarching thing to even extend that a little bit.
[1825.18 --> 1830.16]  I don't think that this EO will be a major change creator in our country.
[1830.60 --> 1834.94]  I think one of the things is there we have so many forward thinking organizations in the U.S.
[1834.94 --> 1836.90]  that have already developed their own A.I.
[1836.96 --> 1842.06]  strategies in the absence of any overarching national ones that have come before.
[1842.06 --> 1849.26]  And, you know, the limitation there is that, you know, they tend to be within what that organization's domain or purview is,
[1849.68 --> 1854.32]  as opposed to whether they're in the private sector or government agencies or whatever.
[1854.78 --> 1860.68]  You know, within the private industry, you know, we have the obvious names that all of us associate with the A.I.
[1860.70 --> 1864.18]  world like Google and Microsoft, Amazon, Apple, you know, and others.
[1864.38 --> 1870.24]  And they have provided public leadership in the A.I. space since there wasn't something else out there.
[1870.24 --> 1883.26]  And we should also note that there are many powerhouses in this space, like Baidu and Alibaba and Huawei and such that are also major powerhouses in this.
[1883.42 --> 1885.32]  I know you spent some time in academia, Daniel.
[1885.44 --> 1888.46]  I mean, what do you think about some of the leadership that we've seen from academia?
[1888.46 --> 1898.54]  Yeah, I think that definitely that's still one area where we see a lot of leadership in the A.I. space from especially places like Stanford,
[1898.54 --> 1904.56]  where there's just a huge leadership role in academia in in the U.S.
[1904.74 --> 1907.48]  But, you know, that that's gradually changing as well.
[1907.54 --> 1917.46]  I think the immigration issue kind of overlaps with that because we're also educating a lot of brilliant A.I. researchers that aren't staying here.
[1917.46 --> 1923.70]  So, yeah, even if we have that leadership in academia, which is is great, there's still that issue lingering.
[1924.20 --> 1926.60]  Sure. It definitely exists there.
[1926.72 --> 1928.72]  You know, there's one other group.
[1928.80 --> 1930.46]  You know, we've talked about some government agencies.
[1930.46 --> 1934.78]  I work for Lockheed Martin, so I'm particularly aware of of military impacts.
[1934.78 --> 1944.44]  You know, in terms of leadership, you know, in 2017, the U.S. Department of Defense published the summary of the 2018 Department of Defense Artificial Intelligence Strategy,
[1944.94 --> 1948.24]  subtitled Harnessing AI to Advance Our Security and Prosperity.
[1948.24 --> 1959.42]  And they did what other government organizations are doing, where they allocated existing funds into various programs within the Department of Defense that could drive forward.
[1959.54 --> 1968.44]  And there are there there has for decades, you know, since the start of the Internet and before we have the Defense Advanced Research Projects Agency,
[1968.44 --> 1972.80]  which we all call DARPA and most people, I think, are familiar with that at least a little bit.
[1972.94 --> 1979.40]  And they have been funding A.I. research at a level of about two billion dollars over several years.
[1979.58 --> 1988.64]  And so that two billion is a good pot of money which smart people can dip into and try to make things happen in the A.I. research.
[1988.64 --> 1993.44]  And they obviously work with the private sector and they work with academia quite a lot.
[1993.60 --> 2001.16]  And so even though that is a military basis, there's a lot of crossover into into the private industry space.
[2001.16 --> 2009.68]  Also, more recently, I should note, as I say this, as I talk about DARPA and the next thing is that working at Lockheed Martin, I work my team.
[2009.68 --> 2018.30]  Actually, the team that I'm on works directly with DARPA and in terms of implementing A.I. priorities, as well as this other agency, which is actually a new one.
[2018.32 --> 2020.74]  It just came about a few months ago, which is the Joint A.I. Center.
[2020.74 --> 2023.56]  It's called JAIC for short, J-A-I-C.
[2024.12 --> 2027.24]  And it's public knowledge that they're there.
[2027.44 --> 2030.54]  They focus more on applied A.I. versus the research side.
[2030.70 --> 2034.24]  And and they are funding at one point seven billion over five years.
[2034.38 --> 2036.28]  I think that was reported by The New York Times recently.
[2036.84 --> 2045.14]  And so, you know, these organizations are really trying to push forward what we can do in partnership with the private sector and academia.
[2045.74 --> 2047.02]  And that's great.
[2047.04 --> 2048.36]  But they've been doing this for some time.
[2048.36 --> 2055.30]  And once again, you know, they the DOD Department of Defense far outran the White House in this case.
[2055.54 --> 2060.52]  And so as a private citizen, again, speaking only for myself, I just think that should have been reversed.
[2060.64 --> 2063.50]  I think it would have been good if the White House had said, hey, this is our national priority.
[2063.50 --> 2069.62]  And all the government agencies, as well as private industry, you know, kind of patriotically jump on board with stuff.
[2069.88 --> 2071.98]  But the best leaders don't follow the crowd.
[2072.04 --> 2074.02]  The best leaders get out in front and lead the way.
[2074.46 --> 2075.10]  Yeah, for sure.
[2075.10 --> 2081.24]  And this whole time, I've read a couple of books on the space race era.
[2081.94 --> 2083.60]  I forget their titles off the top of my head.
[2083.66 --> 2092.14]  But I would recommend if you're interested in this sort of topic around, you know, how a government could effectively promote a technological vision.
[2092.54 --> 2099.38]  There's a lot of interesting stuff that happened in that time period that I think is relevant here and would recommend reading up on that.
[2099.80 --> 2103.58]  Any other comments on the on the executive order generally, Chris?
[2103.58 --> 2118.40]  No, I guess I'll go back to something that I know we both have said several times in this podcast is I would love it if the White House would go back and bring us something a little bit a little bit grander and take a leadership position.
[2118.92 --> 2123.52]  This for what it's worth, this is I say this completely in a nonpartisan way.
[2123.52 --> 2131.58]  Get out there and lead us and lead the world and show the amazing things that we can do with this new technology that's that's here to stay.
[2132.00 --> 2137.88]  So I hope there is a round two of executive order that gives us that AI moonshot.
[2138.08 --> 2139.36]  Yeah, me too, for sure.
[2139.36 --> 2156.58]  Well, before we jump off of this fully connected episode, like we always do at the end of these, we really want to give you some good learning resources so that you can level up your machine learning game, learn more about AI and particularly as relevant to the topic we discussed.
[2156.58 --> 2170.68]  In terms of the topic we discussed today, you know, there's parts of this that overlap with government data and regulation and ethics and kind of general knowledge of AI across across the society.
[2170.68 --> 2178.58]  So we wanted to point you first to this new course, AI for everyone from deep learning dot AI just came out.
[2178.86 --> 2181.46]  I believe this last week was when I saw it.
[2181.54 --> 2193.94]  But this, I think, would be a great resource if you're one of those people that maybe aren't a practitioner, but you really want to learn more about AI, how it's impacting society and what it actually is beyond the hype.
[2194.06 --> 2195.98]  I think that this might be good for you.
[2195.98 --> 2222.88]  I think also for us as AI practitioners, this might be a good one to kind of help us learn how to express AI to people that aren't so technical and also to point people like managers or even acquaintances with this course so that we can help people get a better understanding of AI and, you know, proper expectations for what AI is capable of.
[2222.88 --> 2224.78]  You know, and just to note, I agree.
[2224.92 --> 2230.96]  I think that is a course that nearly everybody, as it's called AI for everyone, nearly everyone should jump into that.
[2231.24 --> 2234.70]  I'm often asked, my job title is AI strategist.
[2234.78 --> 2237.24]  And that's kind of a new thing that's coming into being these days.
[2237.64 --> 2240.34]  And a lot of people say, well, how do you do that?
[2240.38 --> 2244.14]  Or how do I understand the business side of how AI can be implemented?
[2244.14 --> 2251.44]  And a lot of that is understanding where it can be used and being able to communicate effectively what these capabilities are and what the impact is.
[2251.62 --> 2255.04]  And a course like that that you just talked about is a great starting point for that.
[2255.12 --> 2256.34]  So I would encourage people as well.
[2256.34 --> 2259.90]  Yeah. And a couple others that I'll just mention quickly.
[2260.30 --> 2262.96]  Intel AI just came out with this article.
[2263.20 --> 2265.12]  Again, we'll link all these in the show notes.
[2265.26 --> 2269.90]  Kind of listing out some of the existing ethics toolkits for AI.
[2270.10 --> 2283.78]  So these include things like Deon, which has checklists for data privacy, security, IBM Fairness 360, Digital Impact Toolkit, Lime, and others as well that they list out and kind of describe in this article.
[2283.78 --> 2298.12]  So I think that would be a good chance for you to look into things that you as a practitioner could go ahead and start making part of your workflow to develop AI responsibly, even in the absence of formal regulation.
[2298.42 --> 2303.12]  Then finally, there's a couple links that we'll provide for government data that is available.
[2303.44 --> 2309.14]  So, of course, there's the federal in the US, there's a federal data portal called data.gov.
[2309.14 --> 2330.76]  Also, one that I found really useful is a little bit closer to home for me is the City of Chicago data portal, which has just a wealth of data about Chicagoland and a lot of different agencies and processes and information about Chicago that can be really useful if you're kind of looking into things you can do with public data.
[2331.04 --> 2333.46]  So definitely recommend to check those out.
[2333.72 --> 2334.42]  I definitely will.
[2334.42 --> 2339.64]  I use data.gov regularly, but I haven't seen the Chicago site, so I'm going to go check that out after the show.
[2340.02 --> 2340.32]  Awesome.
[2340.78 --> 2345.52]  Well, thanks for helping me kind of pick apart this executive order, Chris.
[2345.70 --> 2347.50]  I hope it was useful for our listeners.
[2347.72 --> 2356.12]  If there are additional comments on this or other things that you'd like to have us discuss on the show, we'd really love to hear from you.
[2356.38 --> 2358.30]  Reach out to us on our Slack channel.
[2358.44 --> 2362.54]  You can join that by going to changelog.com slash community.
[2362.54 --> 2365.60]  We're also on LinkedIn under Practical AI.
[2366.10 --> 2373.00]  And we'd love to hear from you, hear what you're liking, and get some feedback and additional topic ideas.
[2373.18 --> 2375.52]  So thanks for being part of the community.
[2375.52 --> 2378.16]  All right.
[2378.22 --> 2380.84]  Thank you for tuning into this episode of Practical AI.
[2381.10 --> 2382.56]  If you enjoyed the show, do us a favor.
[2382.68 --> 2384.06]  Go on iTunes, give us a rating.
[2384.38 --> 2386.20]  Go in your podcast app and favorite it.
[2386.30 --> 2389.02]  If you are on Twitter or a social network, share a link with a friend.
[2389.10 --> 2391.50]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2391.76 --> 2394.42]  And bandwidth for changelog is provided by Fastly.
[2394.54 --> 2395.98]  Learn more at fastly.com.
[2396.12 --> 2399.38]  And we catch our errors before our users do here at changelog because of Robar.
[2399.56 --> 2402.00]  Check them out at robar.com slash changelog.
[2402.00 --> 2406.76]  And we're hosted on Linode cloud servers at linode.com slash changelog.
[2406.86 --> 2407.30]  Check them out.
[2407.38 --> 2408.22]  Support this show.
[2408.36 --> 2411.84]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2412.30 --> 2413.72]  Editing is done by Tim Smith.
[2413.98 --> 2416.02]  The music is by Breakmaster Cylinder.
[2416.46 --> 2419.84]  And you can find more shows just like this at changelog.com.
[2419.90 --> 2421.98]  When you go there, pop in your email address.
[2422.28 --> 2428.30]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2428.72 --> 2429.46]  Thanks for tuning in.
[2429.46 --> 2430.40]  We'll see you next week.
[2432.00 --> 2432.50]  Bye.
