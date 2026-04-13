[0.00 --> 4.54]  You can take reinforcement learning from an AI standpoint, or you can take reinforcement from
[4.54 --> 9.44]  a statistics standpoint. So, you know, people would probably be familiar with things like
[9.44 --> 15.38]  Optimizely that use bandit algorithms for optimization. And so that's one of our favorite
[15.38 --> 20.70]  techniques is actually a Bayesian bandit style reinforcement learning. And the reason for that
[20.70 --> 25.78]  is that it just works with very little overhead, as opposed to building, you know, these big
[25.78 --> 29.82]  complex machine learning models where anything can happen. And yes, you can probably do a lot
[29.82 --> 34.56]  better in a very fixed use case. But if you have broad use cases and lots of different
[34.56 --> 36.78]  variables changing, it's a different story.
[39.18 --> 45.06]  Bandwidth for ChangeLog is provided by Fastly. Learn more at Fastly.com. We move fast and
[45.06 --> 49.86]  fix things here at ChangeLog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[49.86 --> 53.78]  on Linode cloud servers. Head to linode.com slash ChangeLog.
[53.78 --> 61.10]  Whether you're working on a personal project or managing enterprise infrastructure, you deserve
[61.10 --> 66.78]  simple, affordable, and accessible cloud computing solutions so you can take your project to the
[66.78 --> 72.18]  next level. Simplify your life with Linode's Linux VMs to develop, deploy, and scale your
[72.18 --> 78.36]  applications faster and easier. Get started on Linode today with $100 in free credit for our
[78.36 --> 83.74]  listeners. You can find all the details at linode.com slash ChangeLog. Or if you're not at your desk,
[83.92 --> 91.48]  just text ChangeLog to 474747 and get instant access to that $100. Linode has 11 global data
[91.48 --> 98.40]  centers and provides 24-7, 365 human support with no tiers or handoffs, regardless of your plan size.
[98.40 --> 103.44]  In addition to shared and dedicated compute instances, you can use that $100 credit on S3
[103.44 --> 109.88]  compatible object storage, manage Kubernetes, and more. Visit linode.com slash ChangeLog and click
[109.88 --> 116.32]  on the create free account button to get started. Or just text ChangeLog to 474747. Get started today
[116.32 --> 117.22]  on Linode.
[125.66 --> 130.72]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[130.72 --> 136.04]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[136.12 --> 140.72]  and data science happen. Join the community and Slack with us around various topics of the show
[140.72 --> 145.26]  at ChangeLog.com slash community and follow us on Twitter. We're at Practical AI FM.
[151.74 --> 159.26]  Well, welcome to another episode of Practical AI. This is Daniel Whitenack. I am a data scientist
[159.26 --> 166.34]  with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a principal
[166.34 --> 170.56]  emerging technology strategist at Lockheed Martin. How are you doing, Chris?
[171.04 --> 175.90]  I am doing very well, Daniel. I'm enjoying this beautiful fall weather, and how's it going with
[175.90 --> 183.70]  you? Going good. It's a busy week. There's a conference paper deadline tomorrow that I'm trying
[183.70 --> 190.62]  to meet. So last night, and I'm guessing tonight, will be a little bit restless for me.
[191.02 --> 195.04]  I'll bet. I mean, has anyone out there ever actually submitted their conference paper
[195.04 --> 197.70]  before like those final moments?
[198.00 --> 199.04]  Like before the actual day of?
[199.04 --> 199.32]  Yeah.
[199.32 --> 204.56]  I don't know. I mean, when you have to make like three LaTeX tables that like each one,
[204.56 --> 209.24]  you know, the tweaking of those ads, like each one adds like a day or something.
[209.88 --> 214.98]  Yeah. I'm terrible about that. I'm like, yeah. Yeah. Coming down to the final hours.
[215.54 --> 221.16]  Yep. But it's a good time. I enjoy it. And we're collaborating with some interesting people. So it's
[221.16 --> 228.56]  good to do that and good exercise to kind of organize all your thoughts into that paper format. It's kind of
[228.56 --> 231.96]  good. But yeah, what's going on in your world?
[231.96 --> 236.56]  I am actually trying to do as little AI as possible right now. The weather has been just
[236.56 --> 243.10]  too nice outside. And if I even look at my laptop, my wife gives me a scathing look like you idiot.
[243.64 --> 244.36]  What are you doing?
[244.36 --> 245.44]  Are we not? Like hiking?
[245.74 --> 251.04]  Exactly. Look outside the window. Yeah. I spent most AI. So we're trying to get some outdoor time
[251.04 --> 252.36]  in when we're not working right now.
[252.80 --> 258.78]  Awesome. Awesome. Well, Chris, I don't know if you remember, actually, this is kind of a long story,
[258.78 --> 267.02]  but part of the reason why this podcast exists is because I met our editors. I met them at GopherCon.
[267.12 --> 274.00]  I believe it was in 2016. So I do a little bit of Go programming, as our listeners probably know.
[274.72 --> 281.86]  And I met Adam Stokowiak. And actually, I think it was just Adam there, who is editor-in-chief at
[281.86 --> 288.20]  the Changelog. And that's actually what got us started talking about doing an AI podcast.
[289.02 --> 295.14]  Well, at that same conference, I met our guests today and have been following their company for
[295.14 --> 300.30]  some time and using some of their packages that they've open source. And they're just doing really
[300.30 --> 306.50]  cool stuff. And so today we're joined by Hamish Ogilvie, who is a founder at Sojari,
[306.84 --> 310.96]  talking to us all the way from Australia, I believe. How are you doing, Hamish?
[310.96 --> 315.64]  I'm good. I'm in San Francisco, though. Oh, really? Did you move?
[316.26 --> 320.28]  I did. I did. I had to move across. Yeah. We ended up with most...
[320.28 --> 323.92]  So from our perspective, it's earlier today rather than tomorrow.
[324.52 --> 326.48]  That's right. That's right. Yeah.
[327.08 --> 327.56]  Awesome.
[328.26 --> 329.16]  Not Tuesday yet.
[329.18 --> 331.72]  So is the whole company now in San Francisco?
[332.18 --> 337.18]  No, most of our guys are in Sydney still. We have a few people in Vietnam, New York,
[337.18 --> 340.58]  Ohio, and then there's a few people here in the Bay Area as well.
[340.58 --> 350.28]  Yeah. So were you all doing kind of remote workers before it was cool and necessary to do remote workers now in this world?
[350.44 --> 354.52]  I'd like to say we were, but we weren't. We were actually...
[354.52 --> 360.64]  Engineering we always had in one location, which was in Sydney, and I was probably the exception to the rule.
[360.64 --> 364.40]  But I came across to build our team up in the US.
[364.60 --> 376.52]  But we always had an in-house, like no remote engineers because some of the stuff that we do is so complicated that we often fill whiteboards and argue for two hours at a time before we make a plan to do anything.
[376.52 --> 382.20]  And so COVID's been really interesting because that's kind of flipped everything.
[382.42 --> 386.54]  And everybody's working from home, although it's not too bad in Sydney at the moment.
[386.64 --> 387.90]  The guys still get into the office.
[388.22 --> 393.18]  But yeah, we're talking about reducing office space and everyone's working remote.
[393.34 --> 394.90]  So it's definitely a different world.
[394.90 --> 400.32]  Yeah, I would say there's a lot of things about working remote that can be really efficient.
[400.32 --> 410.66]  But that sort of like trying to get a new effort underway and like brainstorming and whiteboard time, it's pretty incredible when you're in person.
[410.66 --> 416.98]  And I'm not sure that I've experienced anything of that sort of nature in a remote setting.
[417.08 --> 419.24]  There's a business opportunity right there.
[419.24 --> 429.20]  Yeah, I'm sure there's like virtual like remote team whiteboarding that's actually really amazingly wonderful, which pardoning those that are already in that space.
[429.20 --> 430.84]  I haven't experienced it either.
[430.84 --> 441.00]  I think I have to have some type of special surface to write on or something because otherwise drawing with my mouse, it just looked like something a four-year-old would draw or something.
[443.00 --> 446.68]  Even if you go past that, you've still got time changes and stuff for us as well.
[446.96 --> 447.98]  Oh, yeah, sure.
[448.08 --> 448.60]  That's rough.
[448.60 --> 450.88]  Yeah, it's brutal, whichever way you look at it.
[450.94 --> 452.70]  But it's definitely not solved.
[452.92 --> 453.40]  That's for sure.
[454.16 --> 462.28]  Well, as interesting as that topic is, I think you and I have talked a bit about what you're doing at Sajari and some of your work there.
[462.44 --> 470.56]  But I actually don't know your kind of personal background and how you got into the space and, you know, eventually ended up founding Sajari.
[470.76 --> 472.62]  So maybe you could give us a little bit of that story.
[473.14 --> 476.78]  Yeah, I'll try to give you the short version because it's probably a long story.
[476.78 --> 479.40]  But my background was actually originally in physics.
[479.62 --> 480.94]  I got a PhD in physics.
[481.34 --> 483.00]  Score another one for the physicists.
[483.56 --> 484.26]  No kidding.
[484.46 --> 486.02]  You guys are just all over the place.
[486.24 --> 487.92]  Yeah, we have a few on here occasionally.
[489.36 --> 491.78]  We're broken out and physicists have gone to AI.
[491.96 --> 492.88]  What's going on with that?
[492.88 --> 493.88]  I know.
[493.88 --> 493.90]  I know.
[494.04 --> 495.00]  It's a common path.
[495.38 --> 496.10]  It's funny.
[496.44 --> 501.46]  But I was one of the rare few when I first kind of made that path into the space.
[501.56 --> 506.70]  And then now I think the university's got full programs set up around transitioning people down that line.
[507.50 --> 509.30]  But, yeah, so I did PhD in physics.
[509.44 --> 510.48]  Used to design lasers.
[510.48 --> 517.60]  So some of my lasers are still used for surgery and skin treatments and other things.
[517.76 --> 519.72]  But I shipped out into analytics.
[520.52 --> 525.40]  Worked in analytics for probably four or five years and then jumped out to start the business.
[526.02 --> 526.60]  So, yeah.
[527.14 --> 527.74]  Different route.
[528.18 --> 533.24]  Maybe you could just, because I'm interested in kind of the backstory of Sajari a bit.
[533.24 --> 540.64]  But maybe before we get into that, maybe you could just say kind of in a short blurb what Sajari is, what it's trying to do.
[541.46 --> 541.72]  Yeah.
[541.84 --> 546.26]  So we're basically trying to offer machine learning based search as a service.
[546.46 --> 548.68]  But we want it to be really, really fast.
[549.16 --> 554.08]  And so I guess one of the tradeoffs that people make is speed for accuracy.
[554.38 --> 558.36]  So we're trying to kind of mesh the two of those things together in a short way.
[558.92 --> 559.16]  Cool.
[559.16 --> 559.46]  Yeah.
[559.46 --> 572.22]  And how did that idea, how did the sort of AI and search, but also the performance side of that, how did that kind of creep up as something that you thought was a space that you wanted to live in?
[572.64 --> 572.88]  Yeah.
[572.98 --> 574.20]  So it's really interesting.
[574.36 --> 583.60]  But search kind of interested me even back during my PhD because I was doing something really obscure that was very difficult to find literature on.
[583.60 --> 589.54]  And you'd go to search for things and type in, you know, if you typed in two keywords, you get the phone book.
[589.62 --> 594.40]  If you type in three, you get very, very few results.
[594.48 --> 595.98]  You type in four words, you get nothing.
[595.98 --> 599.38]  And that's just the space because it was very small.
[599.60 --> 604.04]  And it always seemed really bizarre to me because I'd written a bunch of papers.
[604.42 --> 609.30]  I had, you know, enormous volumes of context in text that I'd actually written.
[609.80 --> 614.14]  And yet I couldn't use that to actually search and find something on context.
[614.14 --> 621.98]  And so that kind of sparked my brain, I guess you would say, because it always seemed like we should be able to search more conceptually.
[622.40 --> 628.50]  And then the university actually spun out some of the research that I was doing during my PhD into a company.
[628.68 --> 631.40]  And one of the first things that they did was an IP literature search.
[631.48 --> 634.00]  And then the patent emerged all over again.
[634.00 --> 643.54]  The IP search company was basically they had a spreadsheet and they said you keep filling it up with queries until you keep getting the same results.
[643.54 --> 646.54]  And so just looking at that was kind of crazy.
[647.32 --> 658.52]  And so fast forward, I kind of ticked along in the background and chatted to some friends about it and played around the background and couldn't really get any of the technology out there to do what we wanted to do.
[658.76 --> 663.68]  And kind of saw that there was this convergence of, you know, machine learning was starting to come up.
[664.20 --> 668.26]  Search technology was basically mostly built from around the 90s.
[668.42 --> 670.80]  It hadn't changed too much in approach.
[670.80 --> 672.70]  It's changed a lot more recently.
[672.70 --> 679.90]  But you could kind of see that there was this convergence of smart machine learning and information retrieval.
[680.18 --> 684.78]  And so we kind of we jumped on that train and been following it ever since.
[684.94 --> 691.02]  I think the fast side of things, when we're talking previously about making things really fast.
[691.02 --> 705.64]  I don't know if you guys saw, but there was a study a few years ago, Amazon, they intentionally added blocks of 100 milliseconds delay in their e-commerce queries and saw a drop of 1% of revenue for every 100 milliseconds delay they introduced.
[705.64 --> 711.24]  I think Google did the same thing and saw a 20 percent drop in click through rates and things like that.
[711.32 --> 715.04]  So there was this huge correlation between speed and performance.
[715.04 --> 720.78]  But then, you know, a lot of the things that you do in AI can be quite hard to make performant.
[721.18 --> 724.58]  And so there's just these interesting challenges where you're trying to balance.
[724.72 --> 725.66]  That's definitely true.
[725.66 --> 730.20]  And it's like you'll read about this cool model and you want to make it work.
[730.20 --> 732.82]  But then you read about like, oh, how do you make it performant?
[733.06 --> 736.20]  Oh, you like get like this like GPU server.
[736.28 --> 737.14]  Take the smarts out.
[737.14 --> 743.26]  Yeah, that like just like brute force it, which not all of us have the capability to do.
[743.34 --> 744.90]  Maybe some fortunate people do.
[745.40 --> 745.52]  Yeah.
[745.88 --> 760.04]  So as we kind of get going here and I know Daniel's known you for a while, but I'm kind of as I'm learning as a novice here, like can you differentiate a little bit more or talk about kind of the specific areas that you're addressing versus a Google?
[760.04 --> 768.76]  So like, you know, with obviously AI being a topic that's in search kind of broadly at this point, what areas are you guys really addressing?
[769.14 --> 771.56]  And how does that differentiate you from the others that are out there?
[771.96 --> 772.10]  Yeah.
[772.16 --> 778.50]  So interestingly, we jumped into site search around 2015 when we were first kicking things off.
[778.58 --> 783.72]  And the reason that we did that was because Google was talking about getting out of site search.
[783.88 --> 789.80]  And I don't mean searching the public web, but I mean searching your, you know, your internal website, for instance.
[790.04 --> 799.28]  And so they retracted back and sunsetted the Google search appliances, those bright yellow boxes that people used to put in there in their data centers.
[799.68 --> 801.12]  What a different world it is.
[801.32 --> 809.96]  But they also got rid of their product where they were doing that as a service and basically said you could use ad supported or find another product, basically.
[809.96 --> 811.78]  And so we saw an opportunity there.
[811.86 --> 817.38]  And it was a good test bed to start in because all of the data was public already.
[817.52 --> 821.38]  So you didn't have security implications and privacy.
[821.70 --> 823.88]  So it was kind of an easy area to get started.
[824.20 --> 834.08]  And I've done so much in the background in marketing analytics and site tagging and things like that, that we saw that we could basically automate that entire workflow.
[834.08 --> 836.70]  And so that was the origins of the company.
[836.88 --> 850.68]  And then now as we move forward, we're kind of going where the transactional value of search is highest, which is e-commerce search, where you're just seeing that you can, you know, you make small changes and they mean millions of dollars.
[850.90 --> 857.90]  And you can measure it, which is very different to searching a website where people, they don't care as much, if you know what I mean.
[857.90 --> 872.20]  I'm kind of curious on the site search side of things in terms of how big and how many like results a site needs to have to like really like until this really starts becoming a problem.
[872.20 --> 880.92]  And I was wondering if that's at all related to as well, like you can put in a lot of design work in terms of making your site easy to navigate.
[880.92 --> 890.72]  But it seems like if you're able to search something and have it come up sort of instantly and it was a good result, then it also maybe reduces the burden there.
[890.94 --> 900.80]  So could you talk to that a little bit in terms of like the scale that we're talking about and sort of when this type of thing becomes a really big problem?
[901.50 --> 907.40]  Yeah, I mean, I think it's interesting because remember websites back in the day had these enormous navigational structures.
[907.40 --> 912.14]  And, you know, there's 500 links on a page and then now you go to sites and there's basically nothing.
[912.62 --> 920.22]  And so we've had this interesting move where everything's gone to mobile and people have an expectation that they can just search and find what they want.
[920.70 --> 925.98]  And so you find that you don't need that much content before it actually becomes useful.
[926.68 --> 936.50]  And the second aspect to this is that in user testing, we've actually had customers that have come to us and they said in user testing, the first thing people do if there's a search icon, they go to the search icon.
[936.50 --> 942.82]  They don't want to be bothered, you know, going through five different nested navigation structures to find what they want.
[942.88 --> 944.84]  If there's a search box there, but it has to work.
[945.08 --> 956.18]  I was just going to say, I've noticed that especially like I will go through other avenues myself, but I do notice like my wife, she goes to the search box for absolutely everything.
[956.32 --> 962.22]  I mean, like everything and like almost doesn't use navigation other than that.
[962.66 --> 965.04]  And that's user testing showing that more and more and more.
[965.04 --> 969.54]  It's just becoming a base level expectation, which is kind of interesting.
[970.06 --> 972.88]  But the other side to that is that you actually get people's intent.
[973.20 --> 982.22]  So we talk about it in terms of intent analytics, but like a cable TV company that's a customer, for instance, cancel is their biggest search.
[982.22 --> 990.06]  And when people search for cancel, they may happen to know their account ID so they can automatically do things like feed retention programs.
[990.56 --> 996.70]  You can't do these things as easily as if people are navigating around because you don't know specifically what their intention is.
[996.74 --> 1000.80]  But if they type it in, you've got a pretty good idea that you know what it is.
[1000.80 --> 1009.54]  And so the other thing that we see is that if you have searches that are by far and away bigger than anything else, then they probably should be navigation components.
[1010.42 --> 1019.78]  And so there's a whole suite of sort of this, I guess, it's a workflow where you can just continually improve user experience.
[1019.78 --> 1023.22]  I was going to say it almost informs the UX of the site itself.
[1023.48 --> 1026.26]  So you can evolve it with the results from the search.
[1026.36 --> 1026.96]  That's great.
[1027.50 --> 1027.94]  That's right.
[1028.12 --> 1028.28]  Yeah.
[1028.56 --> 1029.26]  It's really interesting.
[1029.38 --> 1031.02]  I wasn't thinking along that vein.
[1031.14 --> 1036.86]  It's almost like you're treating the search box because I've worked a bit in chat and other things.
[1036.86 --> 1042.62]  And it's like you're treating that query almost as like a chat bot input.
[1042.62 --> 1051.02]  Not that the user is wanting a chat response, but you're trying to detect like potentially the T's and those sorts of things and track those over time.
[1051.46 --> 1053.08]  That's super interesting.
[1053.08 --> 1053.44]  Yeah.
[1053.96 --> 1068.78]  Because users' website data a lot of times is something that they hold near and dear and don't want to like, they don't want to give their data out or, you know, all of that sort of stuff.
[1069.00 --> 1071.46]  So especially like usage type things.
[1071.46 --> 1088.18]  So has that been an interesting challenge in terms of like bringing AI to someone's site or maybe their own infrastructure versus like them or maybe it's not, maybe they reach out to Sajari service and like as an API or something.
[1088.40 --> 1089.54]  How does that balance work?
[1090.06 --> 1090.22]  Yeah.
[1090.32 --> 1096.04]  So we do get a lot of companies that ask to host our stuff internally and we don't do it at the moment.
[1096.04 --> 1103.84]  We've just chosen to offer a service for now, which is tough because we know that we could do some really interesting things.
[1103.94 --> 1113.96]  And there's been banks and defense and investment companies that have, you know, treasure troves of data and they want to be able to actually start doing more interesting things with it.
[1113.98 --> 1118.04]  But there's no way they're going to ship it out to third party providers.
[1118.82 --> 1125.02]  And so we haven't gone down that route yet, but we do keep it in mind for the future for sure.
[1125.02 --> 1125.50]  Yeah.
[1125.50 --> 1137.06]  As Daniel was asking you that and I was listening to you talking, it made me think, I suddenly realized that we all probably assume that we know search really, really well over the years.
[1137.32 --> 1139.72]  But I know it's evolving very rapidly.
[1140.02 --> 1144.34]  It just occurred to me that I probably don't know search nearly as well as I think I do.
[1145.04 --> 1153.88]  So actually, if you would take just a moment and maybe kind of give us a landscape of how searches have evolved, what is search right now as we are at the end of 2020?
[1153.88 --> 1161.86]  And, you know, what is different from the way we might have thought of it a few years ago, you know, when we were originally thinking we were learning it so well?
[1162.34 --> 1163.10]  Wow. Where to begin?
[1163.36 --> 1165.82]  I know. It's wide open. You can go anywhere you want on it.
[1165.82 --> 1174.04]  Yeah. It's really interesting because when you see things like AI and machine learning and where they can apply in search, it's not just one area.
[1174.28 --> 1177.38]  It's many, many different areas that they can apply.
[1177.38 --> 1191.20]  And so I think like historically, you know, we saw search engines split away from databases because you wanted to be able to run these really long tail language based queries that used to just absolutely crush databases.
[1191.58 --> 1199.66]  And so search engines enabled you to do basically write out indexes that were immutable, that you could have very high career concurrency on.
[1199.66 --> 1203.52]  But then that came with trade-offs where you couldn't update the data as fast.
[1203.66 --> 1208.68]  And then we fast forward through the years and machine learning became more and more involved in search.
[1208.90 --> 1219.12]  And so I guess we sort of transitioned to learn to rank models where people could re-rank a set of results with machine learning.
[1219.38 --> 1220.98]  And that started becoming popular.
[1220.98 --> 1225.30]  We've got NLP entity extraction and things like that.
[1225.40 --> 1233.18]  So if you go to an e-commerce site and you search for size 14 black shoes, then you should get size 14 black shoes.
[1233.32 --> 1236.82]  But most often you don't, which is really interesting.
[1237.32 --> 1241.66]  And so there's this sort of language extraction aspect to it.
[1241.68 --> 1248.58]  And then you've got things like reinforcement learning, which we're big fans of, to say you don't want to build a model.
[1248.58 --> 1252.00]  And one of the challenges that we have is that we have hundreds of customers.
[1252.30 --> 1257.32]  And so we kind of go and build a custom model for somebody paying on a credit card.
[1258.04 --> 1259.90]  It's just not economical.
[1260.26 --> 1265.66]  So how do you improve performance for them without the added overhead?
[1266.06 --> 1271.48]  And so reinforcement learning is one of the ways that we see that work really well.
[1272.12 --> 1273.10]  So there's a lot.
[1273.56 --> 1277.58]  I mean, it's a hard question to answer, really.
[1277.58 --> 1278.66]  It's so broad.
[1279.14 --> 1281.12]  Yeah, it's interesting to me.
[1281.26 --> 1285.56]  Of course, we've talked about reinforcement learning a few times on the podcast.
[1285.86 --> 1295.46]  And, you know, I think particularly in relation to robotics or maybe automation or autonomous vehicles and that sort of thing.
[1295.46 --> 1309.36]  So I think maybe people might not be as familiar with the idea of reinforcement learning in search or also like marketing analytics type things, which I've also heard.
[1309.58 --> 1312.66]  So you said you were big fans of reinforcement learning.
[1312.66 --> 1324.38]  I know there's still some people out there that are like, you know, maybe think that it's not quite there in terms of like being practical yet or something like that.
[1324.58 --> 1326.62]  How has your experience been over the years?
[1326.72 --> 1335.92]  When did you start thinking that this is really practical for our use cases and has the tooling around it to make it useful, I guess?
[1335.92 --> 1340.50]  And we may want to define it along the way, by the way, just for those who have joined who aren't familiar with it.
[1340.84 --> 1343.70]  Yeah, that's the interesting thing in defining it.
[1343.78 --> 1350.84]  I mean, you can take reinforcement learning from an AI standpoint or you can take reinforcement from a statistic standpoint.
[1350.84 --> 1358.18]  So, you know, people would probably be familiar with things like Optimizely that use bandit algorithms for optimization.
[1358.48 --> 1364.74]  And so that's one of our favorite techniques is actually a Bayesian bandit style reinforcement learning.
[1365.16 --> 1376.64]  And the reason for that is that it just works with very little overhead as opposed to building, you know, these big complex machine learning models where things you anything can happen.
[1376.64 --> 1380.46]  And yes, you can probably do a lot better in a very fixed use case.
[1380.54 --> 1387.60]  But if you have broad use cases and, you know, lots of different variables changing, it's it's a different story.
[1388.04 --> 1388.12]  Yeah.
[1388.28 --> 1388.46]  Yeah.
[1388.52 --> 1398.08]  So could you kind of describe, I guess, then, like from your perspective, where reinforcement learning is specifically applicable to search?
[1398.18 --> 1405.20]  Like what sort of tasks are because I think most people when they think of search, they think of, oh, I put in a query and then I get a result.
[1405.20 --> 1411.04]  But of course, you're doing much more sophisticated analytics and, you know, intent mapping and routing.
[1411.24 --> 1415.92]  So where does it fit into that puzzle from your perspective in terms of tasks?
[1416.34 --> 1416.54]  Yeah.
[1416.72 --> 1432.92]  So, I mean, I can give you an example, say with COVID-19 this year, you if people went pre-COVID and searched for face masks that, you know, you can imagine women sitting at home in front of the TV with the face masks on and then COVID hits and everybody's looking for N95 respirators.
[1432.92 --> 1434.34]  How do you evolve?
[1434.42 --> 1436.14]  Like when that change started to happen?
[1436.36 --> 1438.48]  How do you know when someone's searching for face masks?
[1438.56 --> 1443.18]  Do they want the face masks of the parts or do they want an N95 respirator?
[1443.42 --> 1445.84]  And that's a that's an example where.
[1446.14 --> 1447.76]  It took me a second to get there.
[1447.84 --> 1451.54]  I was like, I don't think about that first type of face mask.
[1451.90 --> 1453.04]  You're talking about very often.
[1453.04 --> 1454.24]  It took me a moment to.
[1454.32 --> 1458.94]  You're talking about like the like the the goop you put on one's face.
[1458.94 --> 1460.48]  The green face, right?
[1460.76 --> 1461.34]  With the towel.
[1461.74 --> 1461.86]  Yeah.
[1461.98 --> 1462.16]  Yeah.
[1462.64 --> 1463.30]  I'm sorry.
[1463.52 --> 1464.38]  Mud mask.
[1464.82 --> 1465.02]  Yeah.
[1465.30 --> 1465.58]  Sorry.
[1466.46 --> 1467.34]  No, no, no.
[1467.42 --> 1470.44]  I had my own search difficulty in my mind.
[1471.14 --> 1472.00]  Context, right?
[1472.38 --> 1476.58]  Daniel, we've really shown, you know, we're not thinking expansively enough.
[1477.08 --> 1477.68]  Shame on us.
[1478.02 --> 1478.94]  It's a common problem.
[1479.08 --> 1482.26]  And I mean, I guess it alludes to the same problem that you have in search context.
[1482.66 --> 1486.14]  What is the context and text in particular is highly ambiguous.
[1486.14 --> 1491.20]  You can use the situation to help you.
[1491.30 --> 1495.12]  You can use past queries so you can see if there's a pattern in what people are doing.
[1495.72 --> 1497.12]  But overall, it's ambiguous.
[1497.44 --> 1499.52]  And this is where keyword search kind of falls down.
[1499.80 --> 1505.04]  And another example that we saw quite a quite a lot of is as seen on TV.
[1505.04 --> 1515.10]  So if you type TV, you could possibly match on things that say as seen on TV because they have TV in the text.
[1515.26 --> 1516.94]  But obviously, there'd be poor results.
[1517.08 --> 1518.16]  But how do you know that?
[1518.70 --> 1519.66]  A word is a word.
[1519.66 --> 1529.26]  And so one of the interesting things is that AI and word embeddings and other things have been able to transition that out into vectors.
[1529.68 --> 1535.30]  And so you can start to actually see the context that something's used in to understand what the meaning is.
[1535.38 --> 1538.46]  So when you search for TV, you get TVs.
[1538.90 --> 1540.82]  You don't get as seen on TV.
[1540.82 --> 1547.90]  And so there's a whole host of interesting ways to try to embed that context into the way that the indexes work.
[1548.82 --> 1554.82]  But going back to reinforcement learning, the reinforcement learning is really interesting because it's trying to look for the maximum reward.
[1555.76 --> 1561.54]  And so in the case that we mentioned before, the N95 had a high purchase rate.
[1561.86 --> 1567.72]  And so that's rewarding the algorithm to move more towards that and optimize the results.
[1567.72 --> 1571.82]  So the medical masks are the cosmetic style masks.
[1572.16 --> 1574.56]  And that happens in a relatively short time frame.
[1575.62 --> 1578.36]  And so then you have trade-offs in time frame.
[1578.76 --> 1581.08]  You know, if you put a six-month time frame, it wouldn't have changed.
[1581.32 --> 1584.02]  You put a two-week time frame on, it would change.
[1584.08 --> 1586.22]  But you've got less data, so you've got less certainty.
[1587.02 --> 1591.14]  So there's a whole host of different things that play into how that would work.
[1591.52 --> 1593.52]  But yeah, it works really well.
[1593.52 --> 1598.56]  I feel like I'm almost asking it as a tangent, but I was just curious as we're talking about reinforcement learning.
[1598.90 --> 1602.92]  Just out of curiosity, are there other architectures that you're finding very common?
[1603.16 --> 1608.34]  Or is reinforcement learning really kind of the dominant architecture given the use case that you're addressing?
[1608.80 --> 1609.58]  It's really interesting.
[1609.76 --> 1615.06]  I mean, I think learn-to-rank style stuff is probably more popular, I feel like.
[1615.06 --> 1621.30]  But reinforcement learning, I know a lot of people have picked up more reinforcement learning, particularly recently.
[1621.54 --> 1623.28]  But Microsoft were big pioneers of that.
[1623.36 --> 1626.10]  There's a whole host of research articles on Microsoft.
[1626.32 --> 1629.64]  I think they have a whole unit dedicated to reinforcement learning.
[1630.70 --> 1630.88]  Yeah.
[1631.12 --> 1635.20]  But for us, that's always been one of our main things.
[1635.24 --> 1641.62]  And it's probably getting more and more popular because it's easier than learn-to-rank models and such, for sure.
[1641.62 --> 1649.50]  So one of the things that even in my workshops that I teach, and this topic comes up kind of a lot,
[1649.82 --> 1655.30]  I like searching around for tooling for reinforcement learning and all of that.
[1655.48 --> 1658.98]  And there's some things that have come onto the scene.
[1659.20 --> 1662.48]  They seem like they're sort of rapidly advancing.
[1663.04 --> 1671.08]  Have you found yourself having to sort of roll your own internal kind of infrastructure around reinforcement learning?
[1671.08 --> 1674.40]  We rolled our own for performance benefits.
[1674.88 --> 1676.98]  And it's probably quite different.
[1677.22 --> 1681.20]  But we actually bake some of that information into the indexes themselves.
[1681.44 --> 1682.24]  That makes sense.
[1682.66 --> 1682.70]  Yeah.
[1682.90 --> 1683.22]  Yeah.
[1683.38 --> 1690.06]  It does, except the implementation is very difficult because you actually have to be able to live edit the reverse indexes,
[1690.18 --> 1694.06]  which historically in search is a no-no.
[1694.28 --> 1697.52]  Basically, I mean, search indexes have been immutable, particularly the scoring.
[1697.52 --> 1709.12]  And I think it was a few years ago, LinkedIn, they released a few different libraries around actually being able to update the scores for intersections in the reverse indexes in place.
[1710.00 --> 1716.90]  And part of the logic behind that was they don't have to rebuild the entire index every time they do it.
[1716.90 --> 1720.20]  And so it's not a common thing, though.
[1720.74 --> 1728.20]  It's one of those things that if you're used to immutable index structures, you would probably not even try to do this because it would seem so foreign.
[1728.42 --> 1733.84]  But because we built our own index from the ground up, we were thinking about this from day one, basically.
[1733.84 --> 1737.60]  So, yeah, probably makes it a little bit different, I guess.
[1737.76 --> 1737.86]  Yeah.
[1738.02 --> 1747.54]  And for those out there that may be a little bit more new to search, when you're immutable indexes and reverse indexes,
[1747.66 --> 1755.82]  could you just explain sort of briefly how that fits into search and how it would interact with a model or something like that?
[1755.82 --> 1756.10]  Yeah.
[1756.10 --> 1756.66]  Yeah.
[1756.66 --> 1767.42]  So a reverse index is basically like when you read the back of a book and you have a list of terms that link to the pages that those terms actually exist on.
[1767.62 --> 1772.40]  And it's very similar, but the links are to actual document IDs.
[1773.24 --> 1778.14]  So for any given term, you can tell which documents that term appeared in, where it appeared in the document.
[1778.46 --> 1782.68]  And we also include things like the context of how it occurred in the document as well.
[1783.14 --> 1785.00]  That's what reverse indexes do.
[1785.00 --> 1786.58]  And what was the second part, Dan?
[1786.76 --> 1787.08]  I forgot.
[1787.70 --> 1787.98]  Yeah.
[1788.10 --> 1800.10]  So just like why in general these would be immutable and like why maybe it's necessary that they not be in the case of applying these more advanced techniques.
[1800.82 --> 1801.04]  Yeah.
[1801.04 --> 1810.32]  So the beautiful thing about immutability is that you can have as many readers as you want, basically, because you know the data is not going to change.
[1810.64 --> 1814.62]  So as soon as you have mutable indexes, you have to manage concurrent reads and writes.
[1815.00 --> 1820.80]  Which has a whole heap of locking and other implications that can affect performance and other things.
[1820.80 --> 1828.58]  So originally when, you know, search indexes were first done, they were immutable because of speed and performance reasons.
[1828.88 --> 1833.20]  And remember back a while ago, disk space was very expensive.
[1833.50 --> 1834.62]  CPUs were expensive.
[1834.62 --> 1840.48]  And so if you could compress the information down to as small as you could possibly get, that had huge advantages.
[1841.42 --> 1845.78]  And so historically, search indexes are very well compressed.
[1846.02 --> 1852.68]  And they can do that because they know exactly what's in the data set before they write it out into an index.
[1852.68 --> 1857.00]  So I'll give you an example, delta encoding.
[1857.00 --> 1871.18]  If you know the maximum minimum number in a list of numbers, then you can massively cut down the size of the storage for those numbers because you know that you can basically add an offset to recreate the number.
[1871.18 --> 1876.24]  And so there's all these compression techniques that allow them to get the indexes very small.
[1876.70 --> 1884.02]  When you're working with mutable indexes, you can't do that the same way because you may change a number.
[1884.48 --> 1888.66]  And then that would change the boundaries for how things are encoded.
[1888.66 --> 1893.24]  And so you just have a different set of tradeoffs that you have to deal with.
[1893.84 --> 1902.68]  From an algorithmic standpoint, it works okay today with things like Elastic and Solar because people have built in these sort of differential.
[1903.70 --> 1909.52]  When you delete something or when you edit something, they don't actually make that deletion or edit straight away.
[1909.66 --> 1912.12]  They buffer them and then re-merge them out to disk.
[1912.12 --> 1919.14]  So you kind of buffer up the changes and then you pay for them in one big hit as they're re-merged out to disk.
[1919.34 --> 1921.88]  And so just different tradeoffs there.
[1921.98 --> 1931.94]  But from an algorithmic standpoint, that's why Learn to Rank is typically a second, third, however many passes where you get an initial set of results.
[1931.94 --> 1935.20]  And then you basically re-rank them with a model externally.
[1935.20 --> 1937.50]  And so the model you can update more frequently.
[1938.10 --> 1941.54]  And it's totally decoupled from the way that the indexes work.
[1942.12 --> 1949.24]  So we kind of went a different route where we said we wanted to have the indexes more involved in that initial ranking process.
[1949.38 --> 1951.54]  We wanted to have a better initial ranking process.
[1952.18 --> 1954.66]  So it's just a different way of solving the problem.
[1954.66 --> 1966.72]  So
[1966.72 --> 1977.26]  ChangeLog++ is the best way for you to directly support practical AI.
[1977.26 --> 1988.16]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal, and help sustain our production of practical AI into the future.
[1989.00 --> 1997.06]  Simply follow the ChangeLog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1997.06 --> 2001.44]  Once again, that's changelog.com slash plus plus.
[2002.44 --> 2005.18]  ChangeLog++ is better.
[2007.26 --> 2013.34]  ChangeLog++ is better.
[2021.86 --> 2032.44]  So I guess to get very practical, given that we were practical AI, I wanted to ask if I am in charge of an organization's website,
[2032.44 --> 2036.48]  and we are trying to figure out what to do that.
[2036.52 --> 2041.88]  And I decide, hey, I want to put your tool set into my website to be able to apply search.
[2042.38 --> 2048.46]  What does that workflow look like to me as that practitioner who has to actually get it up and running?
[2049.12 --> 2050.28]  What am I experiencing?
[2050.86 --> 2052.10]  What do I need to know?
[2052.70 --> 2055.64]  What kind of prerequisites are there that I need to be thinking about?
[2055.64 --> 2058.80]  Can you describe that whole process of how you go implement it?
[2059.52 --> 2061.70]  Yeah, so there's basically two ways that we implement.
[2061.70 --> 2063.98]  The easiest way is just by a crawl.
[2064.30 --> 2067.78]  So you point it at a website, tell it what to touch, what not to touch,
[2067.82 --> 2070.50]  and then we go and crawl that information that's public.
[2070.64 --> 2073.32]  You can also link it into intranets and things like that.
[2073.72 --> 2075.24]  But basically it's a crawl process.
[2075.48 --> 2081.02]  The positive side of that is that it's very easy, very low overhead, no code basically to implement it.
[2081.16 --> 2085.30]  The downside is that crawling is kind of a black art.
[2085.62 --> 2089.52]  It's amazingly hard to keep everything up to date and in sequence.
[2089.52 --> 2097.90]  It's you can't, you have to know when somebody changed a particular piece of content and then to go and recrawl it, for instance.
[2098.04 --> 2099.04]  And so that's difficult.
[2099.04 --> 2105.76]  So in applications like e-commerce, you find that people want to have things more tightly coupled to their data.
[2106.44 --> 2109.12]  And so in those cases, you have integrations.
[2109.24 --> 2112.36]  So we have integrations for things like Shopify, for instance.
[2113.00 --> 2119.90]  You can use an API so you can custom load your data in, which gives you a lot more control.
[2119.90 --> 2124.20]  And so some of the e-commerce customers we have do over 500 product updates a second.
[2124.92 --> 2132.70]  And they have, they're updating things like inventory in real time, the performance of things in real time and other such things.
[2132.80 --> 2136.32]  And even the other day, I went to buy a jacket online and it wouldn't go through.
[2136.40 --> 2138.66]  It kept telling me I could buy it, but it wouldn't go through.
[2139.14 --> 2141.26]  And then I just basically gave up.
[2141.26 --> 2145.80]  And then I went back in 20 minutes later or a half hour later and the jacket was actually sold out.
[2146.12 --> 2152.48]  And so you could tell that the search and the front end was not aware that it was sold out.
[2152.68 --> 2156.34]  And so it was kind of letting me, but then when it went through the purchase, it wasn't.
[2157.14 --> 2164.36]  And so there's this sort of the need for real time data integration is much more important with things like e-commerce.
[2164.36 --> 2174.68]  So would it be fair to kind of, given those integrations and given the fact that, you know, that's a whole bunch of different dependencies that you have to deal with and those integrations.
[2175.06 --> 2182.90]  I mean, would you almost think of an implementation sort of as a system of systems where you, you know, based on whatever that user is needing.
[2183.12 --> 2191.08]  And as you address that, obviously you're, you've going to, you've talked about the speed and all the things that you've done to make your service fantastic.
[2191.08 --> 2203.22]  How do you keep these integrations that are depending on APIs beyond your control from impacting, you know, how, you know, if something does go down, them thinking that is, is your service as opposed to another.
[2203.54 --> 2205.22]  How do you manage that process?
[2205.60 --> 2207.28]  It's a really good question.
[2207.40 --> 2209.78]  It's one that we think about all the time.
[2210.14 --> 2218.70]  And at the moment, we're kind of taking this approach of middleware where we kind of, we have a translation layer that, that does the connection with the external services.
[2218.70 --> 2222.22]  But then once it's inside, it's all kind of the same for us.
[2222.24 --> 2228.00]  So it's, it's much easier for us to have a consistent view and see when something connecting to external is broken.
[2228.60 --> 2239.06]  But there are interesting implications as well, because say things like we, we're trying to generate a decent ranking algorithm few out of the box.
[2239.06 --> 2247.72]  So if we see that you have something like a size or a color, then we're trying to add in the NLP automatically to be able to pick that out.
[2248.00 --> 2254.08]  So that if somebody does come along and search for size 14 black shoes, it will automatically map exactly to your categories.
[2254.08 --> 2255.90]  And so you will get that exact result.
[2255.90 --> 2258.62]  And so there's interesting implications here.
[2258.70 --> 2263.88]  If you come along and then you get rid of sizes tomorrow, I mean, I don't see why you would do that.
[2264.02 --> 2266.02]  Then what's the implication there?
[2266.12 --> 2274.14]  So there's not only the connecting the data, but there's also how it's inferred in search is, is another problem there.
[2274.14 --> 2279.92]  And so one of the things that we're trying to do is actually run algorithms in the background.
[2279.92 --> 2281.90]  And we do quite a bit of backtesting as well.
[2282.02 --> 2292.42]  So if you come up with a new algorithm, you can actually look behind the scenes and we can backtest to see would that have given you a greater return on historical data.
[2292.94 --> 2298.28]  And what we're looking to do moving forward is actually be making changes in the background,
[2298.28 --> 2307.32]  backtesting them for people automatically and then reporting back to them to say, hey, we found a new algorithm that is actually better for you.
[2307.90 --> 2313.38]  If you press this button, you can put it into an A-B test and then, you know, move it into live.
[2314.14 --> 2322.48]  And eventually I would like to get to the point where we're actually surfacing and allowing people externally to come in and write better algorithms within our system.
[2322.58 --> 2324.00]  So it's quite complicated.
[2324.00 --> 2333.36]  Yeah. And coming from a company that does manage all of these different models and config for all sorts of different clients,
[2333.48 --> 2343.86]  do you have any kind of practical advice and wisdom for in terms of model management and sort of managing like,
[2343.86 --> 2355.52]  or maybe even automating some of the training and updating of models while not also losing the ability to debug when things go wrong?
[2355.64 --> 2356.40]  Any advice there?
[2357.10 --> 2364.62]  Yeah, I would say version everything and make it part of your entire workflow so that that flows all the way through to the analytics.
[2365.24 --> 2369.44]  And so we record analytics for every single key press.
[2369.44 --> 2374.82]  We know exactly what that flowed through, where it hit, how long it took, everything.
[2375.16 --> 2380.26]  And so versioning in that is critically important to making things work.
[2381.16 --> 2385.12]  And yeah, that's probably the thing that stands out the most.
[2385.74 --> 2394.68]  Do you have to do something like very meta and like search your own search analytics or something to like be able to like find things?
[2394.86 --> 2395.18]  Basically.
[2395.68 --> 2395.88]  Yeah.
[2396.06 --> 2396.50]  Basically.
[2396.84 --> 2397.06]  Yeah.
[2397.68 --> 2398.52]  That's funny.
[2399.44 --> 2411.00]  I'm curious, as you look forward, you know, we're kind of going through this time over the last couple of years where voice has become a big mode of making queries instead of everything being through a keyboard or touch.
[2411.00 --> 2421.86]  And as we look forward and there are other modes of interaction that are on the horizon, how does that change how you think about the process of search on the front end?
[2421.86 --> 2429.72]  And maybe, you know, given the fact that not all modes of interaction yield the same information at the same place.
[2429.90 --> 2434.62]  Does that change how you have to architect your solution to accommodate those?
[2435.04 --> 2437.62]  Any thoughts on kind of where you're going with that?
[2437.62 --> 2438.34]  Definitely.
[2438.78 --> 2444.88]  And it raises a really important point because when people use voice queries, they add a lot more context.
[2445.34 --> 2450.38]  Google went through this period where the query length, the average query length got shorter and shorter and shorter.
[2450.38 --> 2453.68]  And then now we're in a period where it's getting longer and longer and longer.
[2454.10 --> 2460.48]  And that is definitely due to the technology, like being able to take longer queries, understand the context.
[2461.14 --> 2469.04]  And like when at the start of this, when we were talking about academic search, you know, three or four keywords and you get no results.
[2469.16 --> 2470.24]  That doesn't happen today.
[2470.24 --> 2475.88]  And that's because there's a better understanding of how to map that text through into the indexes.
[2475.88 --> 2484.94]  And so I think as voice gets more and more, you're going to see these sort of hybrid models and keywords aren't going away.
[2485.10 --> 2489.18]  If you search for very specific things, then you want to get very specific things.
[2489.28 --> 2493.50]  And people, if they don't see those specific things, they're less likely to click on the result.
[2493.50 --> 2501.74]  So it kind of feeds back into itself, but then you have the hybrid of turning things into vectors and understanding them with models.
[2501.98 --> 2510.56]  And so you'll probably see that different queries, some will optimize more to the old style and some will optimize more to the newer style.
[2510.82 --> 2512.02]  Yeah, if that makes sense.
[2512.54 --> 2513.64]  I don't know if I explained that well.
[2513.96 --> 2514.32]  It does.
[2515.04 --> 2515.52]  No, you did.
[2515.62 --> 2516.14]  That was good.
[2517.02 --> 2522.64]  So you emphasized e-commerce a couple of times as you were discussing use cases.
[2522.64 --> 2530.70]  And I know that this year in particular has just been insane in terms of the growth of e-commerce.
[2531.10 --> 2543.00]  And I'm wondering if that's shifted some of the priorities within Sajari in terms of having a lot more inbound requests for that type of search.
[2543.00 --> 2550.90]  What have you seen in terms of the impact that that kind of whole segment, you know, the explosion of that segment of the industry has?
[2551.50 --> 2554.70]  How has that affected your growth and the company in general?
[2555.32 --> 2556.38]  Yeah, it's really interesting.
[2556.54 --> 2560.62]  I mean, I wish we went to e-commerce earlier than what we did.
[2560.62 --> 2562.96]  In a way, we always plan to.
[2563.32 --> 2569.62]  And it's a natural area for us because we have so much focus on improving the transaction rate.
[2569.76 --> 2572.28]  And so we always talk about the flywheel of improvement.
[2572.40 --> 2576.06]  How do you get continuous improvement in search that drives more revenue, etc.
[2576.06 --> 2579.46]  And I wish we switched into e-commerce sooner.
[2579.62 --> 2581.54]  But this year has been incredible.
[2581.70 --> 2587.28]  I think it's about 350% growth in e-commerce queries from e-commerce customers.
[2587.88 --> 2591.00]  I mean, they're just growing at such a rapid rate.
[2591.12 --> 2591.82]  It's crazy.
[2592.58 --> 2593.70]  There's definitely demand there.
[2593.72 --> 2600.04]  But then there's also fatigue in e-commerce because some of them have just been trying to keep the machine working.
[2600.04 --> 2609.66]  I don't know if you guys wouldn't have seen this, but in Australia, Kmart brand had a virtual queue because they got so busy.
[2609.78 --> 2611.82]  It would actually say, you know, you're fifth in the queue.
[2611.92 --> 2618.66]  You have to wait three minutes before you can shop online, which is it seems kind of crazy for today.
[2618.66 --> 2624.58]  But you have to remember that a lot of these companies are still operating on some legacy systems that don't scale.
[2625.46 --> 2627.18]  And so they've had to deal with those.
[2627.18 --> 2632.68]  They've had to deal with, you know, increase in inventory and all sorts of other problems.
[2632.86 --> 2637.78]  And so it's top of mind, but they're also busy, if you know what I mean.
[2638.36 --> 2638.72]  I do.
[2638.92 --> 2648.76]  I guess, you know, as you're looking forward, you know, as we're kind of winding up here and you're kind of thinking about the future of your company,
[2648.76 --> 2659.68]  how you're implementing these algorithms and you're busy tracking the future of AI on one side and maybe the AI and kind of more specifically the future of search on the other,
[2660.04 --> 2663.18]  whether it includes AI or the other non-AI components of it.
[2663.40 --> 2665.28]  That's a lot to track together.
[2665.74 --> 2667.90]  What are you expecting and hoping to see?
[2667.90 --> 2673.64]  And how do you think that will impact your own service as you develop this over the next few years?
[2673.82 --> 2675.66]  What's your whole future outlook at this point?
[2676.06 --> 2677.56]  Yeah, I think it's a really good question.
[2677.70 --> 2680.82]  And in terms of keeping up with AI, it's almost impossible.
[2681.16 --> 2685.00]  I mean, you guys do this blog regularly and you probably still struggle.
[2685.18 --> 2686.98]  I know the reason why we do this podcast.
[2686.98 --> 2690.08]  Yeah, it's moving so fast.
[2690.22 --> 2699.92]  And I think, like, for us, being able to be pluggable is really important because I think that the AI aspect has to be able to evolve on its own.
[2700.94 --> 2708.32]  And from the search side, we're trying to get better at we have the mutable indexes, like I mentioned before,
[2708.32 --> 2715.06]  and we're working on being able to distribute them globally so that wherever you're searching, it's right by where you are.
[2715.06 --> 2718.50]  But that means you also need to distribute models and other things.
[2719.08 --> 2725.86]  So there's a whole host of challenges from a DevOps standpoint, systems engineering, that you need to deal with as well.
[2726.24 --> 2728.96]  So I think pluggability is one of the big things.
[2729.32 --> 2732.58]  Don't try to keep up or stay ahead because you're going to struggle.
[2733.12 --> 2733.40]  Awesome.
[2733.90 --> 2737.96]  Well, thank you so much for enlightening us on so many things.
[2738.14 --> 2739.94]  And it's great to connect again.
[2739.94 --> 2743.68]  I know I've been wanting to make this conversation happen for quite some time.
[2743.68 --> 2749.72]  So I'm really happy to connect and hope that someday we're able to see each other again in person.
[2750.10 --> 2752.20]  But thanks for chatting with us virtually.
[2752.46 --> 2753.58]  It was a real pleasure.
[2753.98 --> 2757.00]  And I'm looking forward to seeing what Sajari does in the future.
[2757.56 --> 2758.02]  Thanks, Dan.
[2758.38 --> 2759.02]  And thanks, Chris.
[2759.30 --> 2759.80]  Great chat.
[2760.14 --> 2760.58]  Thank you.
[2760.68 --> 2760.88]  Great.
[2773.68 --> 2790.40]  Thanks again to our partners who support this show's existence.
[2790.68 --> 2792.62]  Shout out to Fastly, Linode, and Robar.
[2792.94 --> 2794.16]  That's all we have for you today.
[2794.68 --> 2795.78]  We'll talk to you again next week.
[2795.78 --> 2825.76]  We'll be right back.
