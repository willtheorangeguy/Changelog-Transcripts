[0.00 --> 4.80]  A lot of us get fascinated by technological advances in AI, right?
[4.82 --> 9.84]  The fact that we can ask questions out of an AI agent and express a meaningful, almost
[9.84 --> 10.92]  human-like response.
[11.32 --> 17.76]  When it comes to actually putting these systems into production, I want to say that AI in
[17.76 --> 23.98]  some sense is an engineering discipline, but I think we are very much far away and it's
[23.98 --> 24.92]  for a reason, right?
[24.94 --> 26.94]  It's not because we are unwilling to do so.
[26.94 --> 31.38]  It's just that the inputs are not as deterministic as some of these other systems, right?
[31.50 --> 36.10]  So whenever you have a change in your data distribution or something happens, then how
[36.10 --> 40.34]  do you put in the right unit and regression tests to make sure that you're going to be
[40.34 --> 41.92]  able to catch some of these errors?
[42.28 --> 44.26]  How do you keep track of the number of people?
[44.44 --> 49.56]  And I can easily tell you the number of instances where a team deploys a feature and then there
[49.56 --> 53.54]  are 20 other teams with unbeknownst to you are starting to use this feature.
[53.92 --> 56.36]  And the next time you make the change, all hell breaks through.
[56.94 --> 61.28]  Bandwidth for ChangeLog is provided by Fastly.
[61.66 --> 63.54]  Learn more at Fastly.com.
[63.78 --> 66.86]  We move fast and fix things here at ChangeLog because of Rollbar.
[67.00 --> 68.66]  Check them out at Rollbar.com.
[68.88 --> 71.10]  And we're hosted on Linode cloud servers.
[71.44 --> 73.44]  Head to linode.com slash ChangeLog.
[73.44 --> 76.34]  This episode is brought to you by DigitalOcean.
[76.78 --> 77.38]  Droplets.
[77.70 --> 78.48]  Managed Kubernetes.
[78.84 --> 79.68]  Managed databases.
[80.20 --> 80.80]  Spaces.
[81.04 --> 81.92]  Object storage.
[82.20 --> 83.46]  Volume block storage.
[83.70 --> 87.20]  Advanced networking like virtual private clouds and cloud firewalls.
[87.40 --> 92.74]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure
[92.74 --> 93.64]  the way you want to.
[94.04 --> 97.56]  DigitalOcean is designed for developers and built for businesses.
[97.56 --> 104.64]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[104.98 --> 108.40]  Head to do.co slash ChangeLog to get started with a $100 credit.
[108.40 --> 110.90]  Again, do.co slash ChangeLog.
[110.90 --> 135.20]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[135.60 --> 136.54]  and accessible to everyone.
[136.54 --> 140.96]  This is where conversations around AI, machine learning, and data science happen.
[141.38 --> 145.42]  Join the community and Slack with us around various topics of the show at ChangeLog.com
[145.42 --> 147.30]  slash community and follow us on Twitter.
[147.44 --> 149.04]  We're at Practical AI FM.
[155.76 --> 159.42]  Welcome to another episode of Practical AI.
[159.76 --> 161.32]  This is Daniel Whitenack.
[161.42 --> 164.54]  I am a data scientist at SIL International.
[164.54 --> 170.86]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal emerging technology
[170.86 --> 172.60]  strategist at Lockheed Martin.
[172.90 --> 173.84]  How are you doing, Chris?
[174.28 --> 175.54]  I am doing very well today.
[175.58 --> 176.26]  Daniel, how's it going?
[176.58 --> 177.28]  It's going great.
[177.36 --> 178.94]  It's a nice, cool day here.
[179.32 --> 180.82]  And so no complaints.
[181.24 --> 185.28]  Over the weekend, the internet's been crashing at my wife's business.
[185.72 --> 188.68]  And it's because there's been too many...
[188.68 --> 191.06]  The access points couldn't handle the number of devices.
[191.56 --> 193.32]  It wasn't so much of like a bandwidth issue.
[193.32 --> 194.56]  It was like an access point.
[194.72 --> 196.32]  So we just went full in.
[196.46 --> 197.80]  And like I ordered...
[197.80 --> 203.80]  Some people might be familiar with Ubiquiti or Unify network appliances and that sort of
[203.80 --> 204.02]  thing.
[204.02 --> 212.72]  So I got like a new gateway plus 48 port switch plus a network video recorder and four cameras
[212.72 --> 216.20]  and a bunch of cable and all that stuff.
[216.26 --> 217.24]  And two new access points.
[217.34 --> 218.80]  I think there's something ridiculous.
[218.80 --> 221.74]  You can have like 500 people or something on these access points.
[221.74 --> 225.24]  So might have gone a little bit overboard, but...
[225.24 --> 225.28]  Maybe.
[225.40 --> 225.60]  You?
[225.86 --> 226.22]  No.
[228.06 --> 229.60]  It was really fun.
[229.92 --> 235.74]  It was like a nice different sort of tech thing that I'm not qualified to be interacting
[235.74 --> 237.78]  with at all, but it was fun.
[238.02 --> 238.18]  Yeah.
[238.72 --> 238.94]  Yeah.
[239.02 --> 240.38]  The weather's been really nice.
[240.44 --> 241.40]  I'm enjoying the fall weather.
[241.50 --> 242.44]  Things are cooling down.
[242.62 --> 245.56]  Spent the weekend outside as much as I possibly could doing that.
[245.56 --> 251.98]  And then we're into this week and just as an incidental note, this is the GPU technology
[251.98 --> 253.12]  conference week for NVIDIA.
[253.20 --> 253.40]  Yes.
[253.40 --> 256.82]  So I've been kind of watching the announcements and some of the talks on that.
[257.26 --> 262.90]  So lots of cool new things for us to talk about going forward as people adjust to this
[262.90 --> 264.10]  year's announcements.
[264.72 --> 268.04]  But I'll leave it there for a point where we're actually going to dive into that.
[268.36 --> 268.98]  Yeah, definitely.
[268.98 --> 276.68]  And people should check out our episode number 106, where we had Will Rameon talking about
[276.68 --> 280.10]  the GTC conference and some of the things related to that.
[280.26 --> 284.80]  So if you're at GTC, that would be a good one to listen to as well.
[285.10 --> 285.38]  There you go.
[285.94 --> 287.22]  It's all virtual this year, though.
[287.28 --> 288.94]  You know, it's a virtual GTC.
[289.08 --> 290.40]  Yeah, it is all virtual.
[290.54 --> 290.96]  That's good.
[291.04 --> 291.20]  Yeah.
[291.20 --> 299.50]  But I'm sure at GTC, people are virtually exchanging some LinkedIn requests to connect
[299.50 --> 300.32]  back and forth.
[300.90 --> 303.46]  And of course, we're all used to that at this point.
[303.66 --> 304.98]  And that's part of our lives.
[305.64 --> 309.96]  And they're doing a lot of cool machine learning and AI stuff at LinkedIn.
[310.28 --> 316.32]  And we're really excited today to have Suju Rajan with us, who is Senior Director of Enterprise
[316.32 --> 317.46]  AI at LinkedIn.
[318.06 --> 318.60]  Welcome, Suju.
[319.24 --> 319.54]  Hello.
[319.74 --> 320.28]  Hey, Daniel.
[320.40 --> 320.84]  Hey, Chris.
[320.84 --> 321.96]  Thanks for having me here.
[322.44 --> 322.76]  Yeah.
[322.94 --> 323.76]  Great to have you.
[324.12 --> 327.68]  I know I could look on your LinkedIn and look at your whole background.
[328.38 --> 334.18]  But for the sake of those listening at home, could you kind of give us a sense of your
[334.18 --> 340.46]  background, how you got interested in AI and machine learning and eventually ended up where
[340.46 --> 341.08]  you're at right now?
[341.62 --> 341.92]  Wow.
[342.20 --> 349.32]  Goes back a very long way, right back to my undergrad, where I had a professor and I was taking
[349.32 --> 352.44]  a class on image and signal processing with him.
[352.44 --> 358.88]  And one of my undergrad senior year projects was on using bi-directional associated memories
[358.88 --> 360.36]  for recognizing digits.
[360.62 --> 362.32]  And it actually worked very well.
[362.32 --> 377.34]  And I remember, you know, compared to these days when the scale of the data is huge, it was like this tiny computer in which I had my MATLAB code running out all of these different BAM and EBAM architectures and whatnot.
[377.34 --> 387.66]  So that resulted in my getting admitted to UT Austin under Professor Jody Kosh, whose lab was doing data mining.
[387.80 --> 388.84]  Kind of dates me now.
[389.26 --> 391.04]  But data mining was what it was.
[391.04 --> 396.84]  Do people still label themselves as doing data mining?
[396.84 --> 397.76]  Is it cool anymore?
[398.24 --> 399.16]  I don't know.
[399.56 --> 400.20]  Maybe it's cool.
[400.20 --> 400.30]  No.
[400.60 --> 402.36]  Sadly, I was there with you.
[402.68 --> 403.74]  It's not cool anymore.
[403.76 --> 404.96]  It's not as so cool.
[406.82 --> 409.22]  But people still data mine.
[409.70 --> 409.90]  Yeah.
[410.10 --> 412.20]  But I don't think they'll ever go away.
[412.50 --> 414.66]  But yes, let's not call us data mining.
[414.66 --> 414.96]  Okay.
[414.96 --> 420.22]  I just want the listeners to know that once upon a time, data mining was in fact cool.
[420.34 --> 421.54]  And we wanted to do that.
[422.26 --> 422.70]  Yes.
[422.98 --> 425.22]  And we had NSF funding.
[425.90 --> 426.30]  Exactly.
[428.06 --> 431.92]  So at UT Austin, again, was a very interesting application.
[432.32 --> 434.46]  It was to analyze satellite images.
[434.86 --> 437.80]  And it was very hard to get labeled data for these images.
[437.80 --> 441.98]  So you would have like these marshy lands in Botswana and all of those places.
[441.98 --> 445.62]  And you had to identify what was the sort of vegetation that grows.
[445.62 --> 450.82]  And we were collaborating with the Center for Space Research.
[451.08 --> 458.32]  And they'd actually fly out people to go walk and record that, hey, this is the sort of vegetation that is growing and whatnot.
[458.64 --> 458.76]  Yeah.
[458.90 --> 460.04]  Talk about annotation.
[460.58 --> 461.56]  Seriously, right?
[462.94 --> 465.68]  No mechanical turkeys to fly out to Botswana.
[465.68 --> 465.80]  Yeah.
[466.12 --> 473.88]  But over there, my thesis was on knowledge transfer, because you kind of wanted to learn from seasonal data to some extent.
[473.88 --> 480.58]  So you can extrapolate to satellite images in the future, also from related geographic regions as well.
[480.70 --> 486.16]  So you don't basically to bring down the cost of annotation while maintaining good performance.
[486.40 --> 487.78]  So that was what I did.
[487.84 --> 488.98]  Had a very fun time.
[489.42 --> 491.36]  Converted into an internship at Yahoo.
[492.42 --> 494.90]  Yahoo Labs, Yahoo Research, lots of different names.
[494.90 --> 502.22]  But it was a fantastic nine years as an individual contributor, applied machine learning scientist, call it what you will.
[502.60 --> 507.34]  But got to work on a whole bunch of different machine learning applications.
[507.34 --> 512.98]  And I think it was right at the point where ML was kind of taking off, big data was taking off.
[513.40 --> 515.42]  MapReduce was sort of starting to come in.
[515.50 --> 517.68]  But when it started, we didn't have it yet.
[517.80 --> 521.90]  In the beginning, it was still all of these single models that you would build to build classifiers,
[521.90 --> 528.54]  better keyword clustering for sponsored search, targeting for advertisements and whatnot.
[528.92 --> 530.80]  So had a lot of fun.
[531.16 --> 533.76]  Eventually, it became larger and larger data.
[533.86 --> 538.30]  Now we had to do news clustering within a few hundred milliseconds and so on and so forth.
[538.34 --> 542.78]  We had to have all of these models that were tens of 20 milliseconds, if I may,
[542.78 --> 549.30]  to be able to figure out if someone's going to convert for an ad or read a news article and so on.
[549.30 --> 551.54]  So had a lot of fun doing that.
[551.88 --> 560.28]  Eventually switched into managing a group that worked on, again, personalization across a whole bunch of Yahoo products.
[560.42 --> 564.32]  This was on the apps, on video recommendation, news recommendation.
[564.32 --> 570.70]  Really got a good sense for what would work as a consumer-facing machine learning product.
[570.90 --> 573.18]  How do we measure interactions?
[573.76 --> 577.72]  Following which, I went to Criteo, where I headed the Criteo AI lab.
[578.58 --> 582.42]  This was my full deep dive into computational advertising.
[582.82 --> 585.40]  And now if you talk to anyone about machine learning for advertising,
[585.88 --> 588.68]  they immediately think of CTR prediction.
[588.84 --> 590.20]  And hey, it's kind of done, right?
[590.24 --> 591.74]  It's sort of already there.
[591.74 --> 594.90]  There's nothing interesting going on in that space.
[595.38 --> 599.78]  But given the amount of money that is spent on advertising,
[599.78 --> 604.10]  there is a lot more that's got to do with the causality of the models, right?
[604.10 --> 610.10]  Because the people who are funding these campaigns want to know that something useful is coming for that money that they are spending.
[610.10 --> 615.10]  So how do we show that our models actually work was an interesting phenomenon.
[616.02 --> 619.06]  And more than anything else, I was working at this company,
[619.06 --> 622.02]  which was sort of like a demand-side platform.
[622.82 --> 627.98]  So you're kind of listening to all of these publishers who want to put ads on their different pages.
[628.32 --> 631.00]  And you have all these advertisers that you're synchronizing with.
[631.56 --> 636.62]  But if you've ever had a deep dive into that world, there are so many, many, many players.
[636.98 --> 638.98]  There's this waterfall model that they have, right?
[638.98 --> 641.56]  Like the first party publishers want the first dibs.
[641.60 --> 645.36]  If they cannot do it, then it goes to the exchanges and so on and so forth.
[645.36 --> 655.22]  But all of that entails a very, very, very, very tiny window in which you need to sort of make that bid and then assemble the ad unit to be shown and so on and so forth.
[655.22 --> 663.08]  So it was a very interesting time where I learned quite a bit about the real-world constraints, right?
[663.10 --> 673.46]  It's not as much about the technical complexity of the model, but hey, can it work in this specific constraints in terms of the latency in which you have to operate?
[673.94 --> 674.12]  Okay.
[674.12 --> 675.64]  So that was Curio AI Lab.
[675.86 --> 681.20]  Also got to show that there were lots of cool problems in computational advertising.
[681.72 --> 684.78]  So we established the lab as a pretty strong presence in Europe.
[685.30 --> 692.22]  And off late, a little over a year now, I've been at LinkedIn where I head what we call enterprise AI.
[692.74 --> 697.94]  So think of all the business-facing applications LinkedIn has, one of which is talent solutions.
[697.94 --> 701.24]  This is where recruiters come to LinkedIn to look for candidates.
[701.24 --> 704.56]  And we also have all of our members who are trying to find the right jobs.
[704.90 --> 709.28]  So how do we make sure that this marketplace works well, right?
[709.34 --> 710.52]  So that's one aspect of it.
[710.60 --> 713.00]  Of course, there's the advertising aspect of it.
[713.52 --> 723.32]  Sales navigator notion where folks who want to pitch their cool new products and services to LinkedIn members, how do we make sure that it's relevant and there is value on both sides?
[723.32 --> 724.54]  So these are some of them.
[724.66 --> 729.64]  And AI for all of these different business-facing applications is what I'm working on right now.
[730.22 --> 730.94]  Super interesting.
[731.24 --> 738.18]  So you've definitely always been at the forefront of these different fields as they're really, you know, have so much momentum.
[738.68 --> 749.68]  Does it seem like the sort of current hype and influx of people into machine learning and AI, does it seem like, you know, faster paced or more momentum than in the past to you?
[749.68 --> 756.82]  Or does it just seem like a sort of new area that, you know, people are putting focus on and switching from other things?
[756.82 --> 761.92]  For better or worse, we became a cool area to be in, right?
[761.92 --> 769.10]  There's a lot of media coverage on what AI can unlock.
[769.86 --> 771.18]  But it is true, right?
[771.48 --> 774.78]  Maybe 10 years ago, it was sort of behind the scenes.
[774.92 --> 776.42]  Nobody really talked about it.
[776.48 --> 778.32]  Hey, why do you see the results that you do?
[778.66 --> 780.64]  Why are you being shown the ads that you have?
[780.64 --> 782.94]  Was not really a part of the discourse.
[782.94 --> 797.68]  But I think all of these interesting innovations in terms of, I want to call it the PR events that some of the big companies sort of set up, helped the field get the recognition that it perhaps deserves to have, right?
[797.68 --> 807.46]  Given how integrated some of these models are into our daily lives, you know, the fact that whether I get a home loan or not is perhaps has a machinery model behind it, right?
[807.48 --> 809.56]  And it's important for folks to be aware of it.
[809.94 --> 812.32]  I would say it's a combination of both.
[812.70 --> 820.38]  It feels like a new space because there is a lot more recognition of the fact that it is very integrated, right?
[820.44 --> 825.80]  And data-driven decisions and AI models are never going to go away from now on.
[825.80 --> 831.96]  So how do you want to think about this field from a societal standpoint, I think, deserves conversation.
[832.44 --> 835.50]  And that's how we make sure we don't make the wrong choices.
[835.94 --> 839.06]  And at the same time, open sourcing has become a big deal, right?
[839.14 --> 845.20]  With TensorFlow and PyTorch and all of these larger companies, quote, democratizing it, as they call it.
[845.30 --> 849.96]  Like, hey, get onto AWS and you have the SageMaker and the whole lot of it.
[850.04 --> 851.32]  Just give us your data, right?
[851.32 --> 862.38]  And the fact that it is becoming a lot more accessible means that a lot more folks are also interested without having to, you know, in the past it used to be, hey, you had to go to this lab.
[862.46 --> 863.56]  You had to get a PhD.
[864.02 --> 867.88]  You had to publish papers before you can even think about machine learning.
[868.14 --> 871.28]  And, you know, the barrier for entry is a lot lower these days.
[871.28 --> 880.68]  But given the ubiquity of the application, I think it's important for everyone to understand what AI can do and the implications that it has.
[881.06 --> 882.24]  So for the better.
[882.38 --> 884.98]  But I wish we didn't have as much media attention.
[884.98 --> 906.56]  So I guess, and I wanted, you sort of answered the thing I was about to ask you, and that is kind of, since you did your PhD and you did one in machine learning, and just to put things in context, you know, it was unusual, I would argue, for lots of people to have machine learning PhDs at the point where you did in 2006 and you were done with that program and stuff.
[906.56 --> 908.82]  And obviously, you've seen this change.
[909.24 --> 914.04]  Did you ever have any inkling where this might go in terms of the evolution?
[914.16 --> 921.84]  You've talked a little bit about the change over time, but just your perception of machine learning as you came out of your program versus your perception of it now.
[922.20 --> 923.34]  What really strikes you?
[923.46 --> 928.46]  Like, what were the big things that when you do look back, you're kind of like going, wow, I never saw that coming.
[928.56 --> 930.04]  Or I told you so.
[930.96 --> 932.32]  I told you so.
[932.32 --> 938.06]  So the fact that a lot of problems, I don't think it's fully there yet, right?
[938.12 --> 950.30]  I think the biggest thing folks somehow forget is for any machine learning or AI to work on, at least this is my personal take, you have to have enough data to make it be meaningful, right?
[950.44 --> 954.92]  And otherwise, it's handcrafted rules, you do some tiny things here and there.
[954.92 --> 963.56]  Of course, you could overfit like heck, DNN, but this is, but I think what changed, I don't know if it is necessarily a change.
[963.66 --> 979.98]  The rise of all of these companies like Facebook and Amazon and, you know, if I may, the Microsofts of the world, right, the Googles and whatnot, that managed to get as much user data and hence were required to deploy machine learning models.
[979.98 --> 988.84]  Did I predict the rise of these platforms as much and that they would aggregate these massive amounts of user engagement that it would be required?
[989.14 --> 989.84]  Perhaps not.
[989.92 --> 993.70]  But Google was sort of taking off at that point when I was doing my PhD as well.
[993.78 --> 995.76]  And Yahoo was one of these forefront companies.
[995.76 --> 1007.22]  But within Yahoo, for instance, the fact that, hey, from everything from news recommendation to figuring out what tags to put on your email to what ads to show was driven by a machine learning model.
[1007.38 --> 1009.40]  So that aspect was always the case.
[1009.94 --> 1020.82]  But that there would be these few centers where it's just going to explode and the democratization aspect of it, that it is also good for these companies to open source code there.
[1020.82 --> 1023.54]  And not necessarily what is running in production.
[1023.68 --> 1029.62]  I know for a fact it cannot be the same models because we are struggling to adopt some of these frameworks when you're outside of Google and whatnot.
[1030.20 --> 1035.62]  But in that sense, opening that up, I think, was a change that I didn't necessarily see coming.
[1036.00 --> 1038.64]  Like you would think that, hey, this would be a secret sauce.
[1038.74 --> 1043.34]  This is something that we kind of want to keep internally in our company because this is the thing.
[1043.34 --> 1055.72]  But that there is so much learning and sharing of what machine learning is that is as a field, the accessibility of it and the opening up of it to more and more people that I didn't see coming.
[1056.28 --> 1066.62]  You know, just to make a point that you just said there, if you put that in context, as you were describing that, I was thinking back about the time, roughly, that you were getting out of your PhD program.
[1066.62 --> 1068.94]  We were doing MySpace.
[1069.62 --> 1085.18]  And if you think about the evolution of social media from the days of MySpace as the first major platform that did not survive in a meaningful way to where we are today with LinkedIn and Twitter and Facebook and stuff, it's quite a change in terms of the data aggregation.
[1085.28 --> 1087.54]  As you said, it's a completely different world.
[1087.54 --> 1093.28]  And even how we shop, how we get information, how we look at videos, right?
[1093.52 --> 1099.22]  This much acceleration and how humanity lives packed into such a short period of time.
[1099.60 --> 1104.28]  Sometimes I think I'm lucky to be a part of this and you're always excited to see what it looks like.
[1104.64 --> 1109.02]  But on the other side, I guess with anything that gets accelerated, then comes all the challenges, right?
[1109.04 --> 1110.44]  Are we thinking about this, right?
[1110.52 --> 1114.42]  And it's good that we've started asking these questions, but there are no clear answers.
[1115.52 --> 1116.74]  That's why we are here, right?
[1116.74 --> 1121.68]  So the answers are also interesting to think and ponder and make sure we are doing the right things on.
[1138.68 --> 1144.22]  Change Log++ is the best way for you to directly support practical AI.
[1144.22 --> 1155.14]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal, and help sustain our production of practical AI into the future.
[1155.96 --> 1164.02]  Simply follow the Change Log++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1164.56 --> 1168.38]  Once again, that's changelog.com slash plus plus.
[1169.88 --> 1172.16]  Change Log++ is better.
[1174.22 --> 1176.04]  Change Log++.
[1176.04 --> 1178.58]  Change Log++ is better.
[1189.58 --> 1198.06]  So Suju, we've talked a lot about the AI industry in general and, you know, interesting shifts that have happened and all of that.
[1198.06 --> 1201.32]  And I'm sure some of those are even visible, you know, within LinkedIn.
[1201.48 --> 1205.60]  I was thinking while we were talking, like, you know, how many people have switched their
[1205.60 --> 1213.54]  title from like data mining person or data scientists or like data analysts to like AI
[1213.54 --> 1216.38]  engineer or AI, you know, whatever.
[1216.80 --> 1217.92]  So that's super interesting.
[1217.92 --> 1223.72]  But I think more to the things that you're working on personally, I'd love to hear particularly
[1223.72 --> 1228.62]  you brought up some ideas around recruiting and that sort of thing.
[1228.98 --> 1234.66]  Maybe before we jump into the specific things within LinkedIn, could you give us a sense
[1234.66 --> 1241.62]  of how machine learning and AI are kind of starting to influence recruiting in a more
[1241.62 --> 1242.28]  meaningful way?
[1242.96 --> 1243.48]  Sure.
[1243.90 --> 1247.90]  So historically, how would recruiters hire, right?
[1248.04 --> 1249.62]  It came down to your network.
[1249.70 --> 1251.40]  Of course, it was a physical network.
[1251.68 --> 1253.10]  You probably had your Rolodex.
[1253.10 --> 1258.02]  You'd go through contacts to say, I'm hiring for these candidates and so on and so forth,
[1258.06 --> 1261.92]  or you would engage in some external job sites and whatnot, right?
[1262.44 --> 1268.28]  But the burden then is, I think this is sort of underappreciated to some extent.
[1268.62 --> 1274.92]  There are a lot of noisy applicants that might come through and you do not want to, as a recruiter,
[1275.08 --> 1278.26]  send the noisy applicants up to your hiring manager.
[1278.26 --> 1280.32]  That's not going to set you up for success.
[1280.32 --> 1284.94]  It also limits the number of candidates that you can give your bandwidth to, right?
[1284.96 --> 1289.56]  You can't talk to 100 people in two weeks in any meaningful way to close them.
[1290.14 --> 1298.32]  So for sure, as there are more and more jobs that are not at this current point in our existence,
[1298.32 --> 1300.92]  but in general, as more and more jobs.
[1300.92 --> 1302.74]  I would say we're living in an anomaly.
[1303.10 --> 1304.34]  Yeah, that's probably true.
[1304.34 --> 1309.56]  Taking that outlier out of the, hopefully outlier out of the picture.
[1309.80 --> 1315.44]  How do we help our recruiters be, have to spend their time on, let's say,
[1315.68 --> 1320.34]  those candidates that are necessarily worth spending their time on, right?
[1320.38 --> 1324.18]  Because it's not just because you call up someone, they're going to immediately, you know,
[1324.20 --> 1325.78]  drop their job and move over, right?
[1325.78 --> 1330.60]  You still need to work on the storytelling, as our recruiters call it, to convince them
[1330.60 --> 1332.00]  that this company is worth it.
[1332.42 --> 1340.34]  So if we could, in some form or fashion, make the hiring of our members be that much more
[1340.34 --> 1344.48]  efficient, I think that is the change that we are trying to drive as well.
[1344.48 --> 1349.86]  There is also a lot these days, for sure, and LinkedIn is also trying out some of these
[1349.86 --> 1355.30]  interesting elements where, you know, maybe it is not all about going on site, right?
[1355.36 --> 1360.16]  And proving over and over again, going through the same lead code exercises over and over again
[1360.16 --> 1362.58]  to show that, hey, I can do this job, right?
[1362.62 --> 1367.80]  So what if you could have your credentials in some sense assessed by a platform, right?
[1367.84 --> 1371.78]  So we have all of these skill assessments that you can take, which I'm sure you've seen in
[1371.78 --> 1374.80]  some of these other places like HackerRank, PeekCode and whatnot, right?
[1375.02 --> 1379.10]  But think of it as your credentials that sort of travel with you, right?
[1379.20 --> 1385.12]  And if you could then not have to prove yourself on these same elements over and over again,
[1385.12 --> 1391.14]  but what really matters, what is the differentiation for this recruitment company or this particular
[1391.14 --> 1393.82]  job that would make you that much of an ideal fit?
[1394.74 --> 1400.54]  So it's a lot more about given the enormous number of candidates that have their profiles online,
[1400.54 --> 1408.62]  how can we make it that much faster for the recruiters to hone down that smaller set and
[1408.62 --> 1410.46]  then spend their time in converting them?
[1410.86 --> 1413.28]  The same is true on the seeker side as well.
[1413.42 --> 1415.44]  There are lots of non-traditional roles now.
[1415.54 --> 1417.60]  There are lots of options to switch carriers, right?
[1417.62 --> 1419.62]  You're not like a carrier employee anymore.
[1419.74 --> 1422.76]  People take these very interesting paths.
[1423.00 --> 1428.48]  And so how do we sort of help our seekers understand here are all these carrier trajectories one can
[1428.48 --> 1430.40]  have what are the skills that you require?
[1430.80 --> 1435.98]  Say if I wanted to switch to becoming a PM instead of being in the AI field for design
[1435.98 --> 1437.02]  or some such thing, right?
[1437.04 --> 1438.76]  So what would that path look like?
[1439.18 --> 1445.02]  So helping our members also be aware of here are the opportunities, here are the skills that
[1445.02 --> 1445.68]  are required.
[1446.32 --> 1450.94]  And in some ways, even tying it up with LinkedIn Learning to say here are the courses that you
[1450.94 --> 1453.34]  could take if you wanted to switch gears.
[1453.34 --> 1457.90]  I think that is where we want to think about recruitment moving forward, right?
[1458.60 --> 1459.88]  Technology is interesting.
[1460.02 --> 1460.84]  It keeps changing.
[1461.14 --> 1467.16]  So can we automate the reskilling and the up-leveling of our members and continue to show to them
[1467.16 --> 1471.10]  all the opportunities that come with a new workforce, new marketplace?
[1471.48 --> 1473.04]  So I think that's where it's headed.
[1473.36 --> 1475.32]  It's also going to be a lot more data-driven.
[1475.82 --> 1480.64]  A lot of our hiring managers and whatnot want to understand the landscape, right?
[1480.64 --> 1485.88]  Like, yeah, I'm trying to hire this particular profile in, say, Lafayette, right?
[1485.90 --> 1489.66]  So what is my probability of getting someone with these skill sets?
[1489.76 --> 1491.48]  Do I need to broaden my search?
[1491.88 --> 1496.38]  What is the typical salary band that is being paid in some of these other places that I'll
[1496.38 --> 1497.32]  have to compete with?
[1497.76 --> 1502.26]  And maybe even this world after we all come out of this COVID situation, right?
[1502.28 --> 1504.60]  What does the future of remote working look like, right?
[1504.60 --> 1507.48]  What are the pay scales that you'll all have to think about at that point?
[1507.48 --> 1512.28]  So it's also a lot more of trying to understand from the broader trends that are happening
[1512.28 --> 1513.02]  in the industry.
[1513.20 --> 1515.54]  So it's not as niche as it used to be, right?
[1516.18 --> 1519.06]  These tools are being made available in a data-driven way.
[1519.56 --> 1521.56]  So yeah, hopefully that answered some of it.
[1522.08 --> 1526.08]  It's really interesting to think about, like you were saying, the path that someone takes
[1526.08 --> 1530.22]  to a certain position and the changes that go along with that.
[1530.22 --> 1536.70]  Yeah, because there's so many unique trajectories, particularly into machine learning and AI,
[1536.94 --> 1538.22]  into those positions.
[1538.22 --> 1542.58]  You've got people coming from science, people coming from engineering, people coming from
[1542.58 --> 1547.28]  even other places, philosophy, liberal arts, economics, business.
[1547.88 --> 1551.30]  And so there are so many sort of unique trajectories.
[1551.68 --> 1558.62]  And I often get asked when I'm doing a workshop or just talking to someone doing mentoring or something
[1558.62 --> 1563.64]  like that, like, what are the steps I need to take, like, between where I'm at now and
[1563.64 --> 1567.38]  where, like, this position that I want or have in my mind?
[1567.78 --> 1569.08]  What's the sort of pathway there?
[1569.14 --> 1572.90]  And I, of course, have my own bias opinion about that.
[1572.96 --> 1578.50]  But it is really interesting to think about, you know, mapping out the trajectories and helping
[1578.50 --> 1581.86]  a person understand from where I'm at now to where I want to be.
[1581.86 --> 1584.66]  You know, how do people typically get there?
[1584.80 --> 1586.74]  Where do they jump off from and to?
[1587.16 --> 1589.36]  That's super interesting to me.
[1589.42 --> 1595.26]  And it also makes me think sort of like a graph structure sort of coming up.
[1595.34 --> 1600.08]  I think somewhere in I heard or I read about, you know, LinkedIn's knowledge graph.
[1600.08 --> 1604.80]  And I was looking through a couple of the links in one of your blog posts with the papers
[1604.80 --> 1605.90]  and I saw some graphs.
[1605.90 --> 1612.64]  So, yeah, that seems like a very interesting relationship where you've got, like, people
[1612.64 --> 1617.34]  who work for companies, who are in places, who are in industries.
[1617.98 --> 1621.82]  And there's, of course, time in there and all sorts of things.
[1621.98 --> 1627.44]  So it seems like there's definitely even a unique data structure that's going on with
[1627.44 --> 1628.56]  the LinkedIn data.
[1628.68 --> 1629.18]  Is that correct?
[1629.48 --> 1635.48]  Yeah, I think LinkedIn has been very open about calling it the economic graph, right?
[1635.48 --> 1639.38]  So how do we see the whole job space evolving?
[1639.76 --> 1642.70]  And to your point, yes, it starts with industries and companies.
[1642.92 --> 1644.86]  What are the skills that our members are acquiring?
[1645.18 --> 1648.96]  What are the sorts of educational qualifications people are getting?
[1649.08 --> 1650.50]  What are the titles that we have?
[1650.88 --> 1657.20]  And sort of standardizing all of this and normalizing it, if I may, into an internal representation
[1657.20 --> 1662.84]  so that, you know, I can look at, say, Chris's trajectory and then map it down to my math.
[1662.84 --> 1662.94]  Oh, gosh.
[1663.20 --> 1664.40]  Oh, don't do that to me.
[1664.88 --> 1671.18]  Or figure out, hey, how can we learn broadly that, hey, this is the movement in mass in terms
[1671.18 --> 1675.92]  of it's no longer, I don't know, things that used to be in MATLAB anymore, right?
[1675.92 --> 1679.60]  It's more of these other sorts of tools that are becoming that much more popular.
[1680.22 --> 1684.46]  And being able to make sense of all of this data, right?
[1684.46 --> 1689.32]  As you can imagine, not everybody writes the same things in their job postings or on their
[1689.32 --> 1689.82]  profiles.
[1690.08 --> 1695.26]  So how do we, if I may project it down, even though that's not exactly what we're doing,
[1695.32 --> 1700.60]  but into a common vocabulary that we can drive products and machine learning systems across
[1700.60 --> 1702.48]  LinkedIn is what we do.
[1702.48 --> 1708.20]  And besides internal LinkedIn, the economic graph is also used in lots of different forums,
[1708.30 --> 1711.24]  right, to give insights into what are the fields that are hiring.
[1711.48 --> 1714.60]  Here are the top things that candidates or members are interested in.
[1714.68 --> 1717.58]  Here is how skills are changing across the world and so on.
[1717.60 --> 1721.76]  So, of course, and sometimes you also get very interesting insights in terms of behavior,
[1721.94 --> 1726.26]  how women behave, how men behave when they approach a job and whatnot, right?
[1726.28 --> 1728.20]  So it unlocks a whole bunch of value.
[1728.20 --> 1734.88]  And I think that is the most remarkable asset that we have, purely members sharing our journeys
[1734.88 --> 1736.42]  and career journeys.
[1736.80 --> 1741.82]  And of course, from the marketplace of hirers, how is the job landscape changing?
[1742.00 --> 1743.76]  How are the skill demands changing?
[1743.90 --> 1744.64]  And so on and so forth.
[1744.86 --> 1744.96]  Yeah.
[1745.60 --> 1746.58]  So that's super cool.
[1746.66 --> 1750.98]  I guess to continue building on kind of what you're doing, because I love where this conversation
[1750.98 --> 1755.62]  is going as you've kind of laid out how you're looking at the problems that you're trying
[1755.62 --> 1756.64]  to solve going forward.
[1756.98 --> 1762.78]  If you start thinking about where AI technology is today and these types of problems, where
[1762.78 --> 1769.16]  are you matching up various AI architectures or even approach in general to solving problems
[1769.16 --> 1771.80]  that LinkedIn and LinkedIn's customers care about?
[1772.28 --> 1776.22]  Where does AI fit into that large set of tasks that you guys are addressing?
[1776.22 --> 1783.58]  Well, so I want to say in almost all product surfaces that we have, just given the scale
[1783.58 --> 1784.64]  of the data, right?
[1784.78 --> 1791.10]  So we're talking 700 million plus members, any given day, 14 million to 20 million job
[1791.10 --> 1793.62]  postings, even in my small domain, right?
[1793.68 --> 1796.42]  So there are things like, hey, do we show job opportunities to people?
[1796.50 --> 1800.20]  How do we run things on the feed, given the number of users who show up and so on and so
[1800.20 --> 1800.36]  forth?
[1800.58 --> 1803.66]  But maybe just talking about the talent space itself, right?
[1803.66 --> 1809.04]  Now, making sense of these member trajectories as an example.
[1809.80 --> 1814.12]  And again, while one view could have been, hey, let's just pass and code all of these
[1814.12 --> 1818.22]  features and try to build some sort of a simple model which says, hey, am I going to apply
[1818.22 --> 1819.08]  to this job posting?
[1819.18 --> 1820.34]  And of course, that is restrictive.
[1820.60 --> 1826.60]  Then how can we not have to do with these sorts of standardized categorical features?
[1826.60 --> 1831.60]  If I were to look at the entirety of the text that the job posting has, can we leverage some
[1831.60 --> 1836.58]  of these recent, I don't know, fine-tuned versions of BERT, say the internally BERT option to give
[1836.58 --> 1841.38]  us some of these semantic meanings because of not all job postings are created exactly
[1841.38 --> 1845.14]  the same, even though they might be talking about exactly the same jobs, right?
[1845.14 --> 1852.38]  So putting all of these into play, basically to, at this point, we are leveraging, if I
[1852.38 --> 1858.84]  may, more deeper understanding of member career trajectories, if I may, plus whatever is available
[1858.84 --> 1865.72]  on the job posting sites to be able to do more than am I just going to click on that particular
[1865.72 --> 1866.36]  job posting?
[1866.36 --> 1868.82]  It's even more of, am I going to apply?
[1869.14 --> 1875.10]  If a recruiter is going to reach out to me as an example, am I going to accept that recruiter's
[1875.10 --> 1875.54]  connection?
[1875.92 --> 1881.96]  And to get to that notion of understanding what the job posting is really about, and we've
[1881.96 --> 1888.58]  taken it a little step further in our recruiter-facing projects, where as a recruiter, you perhaps
[1888.58 --> 1893.44]  don't need to give very, very explicit signals in terms of, you know, here are all these Boolean
[1893.44 --> 1897.28]  operations I want to do on the member places to get me that narrow set.
[1897.68 --> 1902.18]  But just identify a few of the candidates that you're interested in, and behind the scenes,
[1902.26 --> 1907.66]  we are able to then say, hey, this is the role that the recruiter is looking for, given their
[1907.66 --> 1909.10]  interests that they have shown.
[1909.40 --> 1914.64]  So let's organically start pushing some of these matches, if I may, which we call recommended
[1914.64 --> 1916.10]  matches down to our recruiters.
[1916.10 --> 1918.18]  So that's something that we're working on.
[1918.96 --> 1923.14]  Underlying all of these, I'm not going to say are incredibly complex models.
[1923.14 --> 1926.70]  At some point, we could even set this up as an RL problem, right?
[1926.76 --> 1931.78]  Like say, hey, Suju's benefit or whatever, the thing that she wants to optimize in her
[1931.78 --> 1935.42]  life is maximize her career potential, whatever it is, right?
[1935.42 --> 1938.60]  Or economic potential or some title potential or whatnot.
[1938.82 --> 1943.42]  Now, given that is my long-term strategic play, what are the series of short-term actions
[1943.42 --> 1944.44]  that I need to take?
[1944.44 --> 1950.78]  To be able to almost be a coach to a member's career trajectory is my personal dream of where
[1950.78 --> 1952.90]  I wanted to take this thing.
[1953.28 --> 1956.60]  But the interesting part is LinkedIn is just one view of it, right?
[1956.62 --> 1963.30]  In the sense that I can see that, hey, Suju is applied to this particular job, post which
[1963.30 --> 1964.70]  it sort of moves off of LinkedIn.
[1964.82 --> 1966.84]  And we get very delayed feedback, if I may.
[1966.94 --> 1970.68]  So maybe after four months, if I'm an active LinkedIn user, I change my profile.
[1970.68 --> 1973.22]  And then we, hey, this actually worked, right?
[1973.28 --> 1975.86]  And now we are able to get these sorts of positive signals.
[1975.86 --> 1981.72]  So coming up with all of these proxies and trying to make our AI models be smart enough
[1981.72 --> 1987.12]  where at least we are efficient, right, from a matching process is where the current focus
[1987.12 --> 1987.50]  is on.
[1987.82 --> 1990.04]  But is there scope to do 20 times more?
[1990.16 --> 1990.86]  Definitely yes.
[1991.06 --> 1992.72]  And this is where we want to take the thing.
[1993.20 --> 1998.86]  So I guess as you look at all this possibility and all the things that you can apply different
[1998.86 --> 2003.88]  AI architectures to, it made me wonder as you were talking, how much crossover is there?
[2003.88 --> 2007.84]  I realize that you guys are owned fully by Microsoft and yet LinkedIn remains its own
[2007.84 --> 2008.20]  brand.
[2008.84 --> 2015.56]  How much crossover is there between the AI teams at LinkedIn as a subset of Microsoft and
[2015.56 --> 2019.02]  the various Microsoft AI teams as a whole?
[2019.86 --> 2026.18]  And just to ask, you probably don't have anything you can announce yet, but we're all interested
[2026.18 --> 2031.04]  in the fact that GPT-3 just came under license from OpenAI.
[2031.52 --> 2036.76]  And do you foresee some interesting use cases going forward with GPT-3 and LinkedIn?
[2037.48 --> 2040.94]  Well, I'm not going to comment on the larger collaboration.
[2040.94 --> 2043.48]  That's why I was giving you the out right there.
[2043.74 --> 2044.80]  So I recognize that.
[2045.32 --> 2049.82]  But I just got to say, I can certainly think of some interesting things to do there.
[2049.82 --> 2050.78]  Exactly.
[2050.98 --> 2051.20]  Right.
[2051.56 --> 2057.48]  I think the biggest benefit of all of these models, especially that in terms of how we
[2057.48 --> 2061.94]  want to represent, I don't know, the text that humans generate, right?
[2061.94 --> 2067.92]  Or even images or even how we want to think about knowledge overall in some senses.
[2068.16 --> 2071.06]  But the cost of doing that, of course, is non-trivial, right?
[2071.06 --> 2077.52]  So in these cases, can we go this fine-tuned approach sort of a route where we start with
[2077.52 --> 2081.90]  these pre-trained models, then get it into the LinkedIn-specific context, and then see,
[2082.06 --> 2086.86]  hey, end-to-end, if we were to optimize for an outcome of an hiring, are we able to see
[2086.86 --> 2087.86]  more benefits?
[2087.96 --> 2091.38]  This is an active piece of work that is constantly ongoing in LinkedIn.
[2091.76 --> 2096.08]  So trying to make sense of these glove embeddings at some point.
[2096.22 --> 2098.04]  It was Lee glove embeddings, if I may.
[2098.12 --> 2098.76]  Then there is Bert.
[2098.76 --> 2100.60]  And then there is Lee Bert that we are trying to do.
[2100.70 --> 2105.94]  And of course, as this space evolves and the heavy lifting is done maybe once or twice,
[2105.94 --> 2111.94]  and then it's more about adapting these architectures to your internal use cases and seeing what the
[2111.94 --> 2114.22]  benefit is, I think it makes a ton of sense.
[2114.70 --> 2119.54]  And it seems also wasteful in some senses for all of us to be doing these massive trainings
[2119.54 --> 2125.00]  over and over again, that piggybacking on some of these methodologies to see what is
[2125.00 --> 2127.00]  the value that it unlocks, for sure.
[2127.00 --> 2132.90]  I think the dream case is for us to show up at LinkedIn and say, hey, I want to get to
[2132.90 --> 2134.32]  be X in the next two years.
[2134.44 --> 2134.88]  Help me.
[2135.28 --> 2141.02]  Right now, can we make use of everything that we understand about our members' journeys,
[2141.36 --> 2143.30]  about the skills that they have acquired?
[2143.68 --> 2149.66]  You know, in some interesting world, if we could also, if the companies, for instance,
[2149.76 --> 2151.00]  are willing to participate, right?
[2151.00 --> 2155.12]  Like, I want to uplevel my talent to this kind of a place.
[2155.18 --> 2156.88]  Like, I want to upskill all of these folks.
[2157.00 --> 2162.82]  Now, how do we have these personalized recommendations for folks in the career trajectory space?
[2162.82 --> 2169.04]  Can we learn globally and say, hey, this is what a career transformation looks for someone
[2169.04 --> 2171.20]  in the automobile industry, right?
[2171.20 --> 2175.08]  I think it's definitely doable in some ways.
[2175.74 --> 2177.12]  I need some help here, you know.
[2177.22 --> 2177.48]  Okay.
[2177.48 --> 2201.34]  So, I would love to get into a few of the, you know, practicalities of some of this work
[2201.34 --> 2202.20]  at LinkedIn.
[2202.20 --> 2209.44]  And I've read a bit through some of the information about the, you know, recruiter systems and all
[2209.44 --> 2209.82]  of that.
[2210.26 --> 2217.04]  It seems like there's kind of maybe a couple of different areas that have been drawn out
[2217.04 --> 2218.04]  in what I've read.
[2218.12 --> 2223.40]  One of those is kind of the search side of things and representing candidates.
[2223.76 --> 2228.06]  And then the second side is more of a personalization side of things.
[2228.06 --> 2229.90]  I was wondering if you could touch on those two.
[2229.90 --> 2236.38]  And if the representation side of things, like if you have a sort of, are you developing
[2236.38 --> 2240.56]  kind of embeddings of candidates within the graph of LinkedIn?
[2240.86 --> 2246.38]  And that's what you're leveraging in part to maybe pre-compute that and get search done.
[2246.50 --> 2247.82]  How does that tie in?
[2247.96 --> 2253.48]  Sort of building off of the standardized version of us looking at the data that we have, right?
[2253.48 --> 2262.18]  So, Daniel, exactly to your point, we do have a notion of what a member embedding needs to look like.
[2262.36 --> 2266.14]  And the data for LinkedIn comes from our LinkedIn profiles, right?
[2266.60 --> 2272.82]  So, in this sense, understanding that, hey, this particular member has a, in that space,
[2272.96 --> 2277.60]  sort of looks like people who are in this technical industry, in this location.
[2277.60 --> 2284.72]  And here are the sorts of jobs that they kind of apply to as much as we can represent them in that member embedding space.
[2285.22 --> 2288.18]  Likewise, we have things that are on the job embedding side as well.
[2288.32 --> 2295.02]  And someone asking for a data miner, maybe because they were under a rock, is also still asking for an AI scientist.
[2295.02 --> 2299.68]  So, how can we sort of bring that job embedding view into it?
[2300.30 --> 2303.14]  And in some senses, be able to scale this.
[2303.26 --> 2310.98]  Because if you think about where, there was an earlier question of what are the different services in which we have AI, right?
[2311.00 --> 2312.36]  There is the search aspect of it.
[2312.44 --> 2315.56]  Then we also organically recommend jobs to people.
[2315.68 --> 2319.82]  There is something that we call instant jobs where you want to be the first to apply.
[2319.82 --> 2325.86]  So, members actually sign up for alerts to say, hey, the moment you see a job come into our system, then send me an alert right away.
[2325.92 --> 2329.18]  So, you need this to be high, high, high precision, as an example.
[2329.32 --> 2332.96]  Then on the flip side, on the recruiter search, as an example, right?
[2332.98 --> 2335.62]  It's all about matching members to their jobs.
[2335.80 --> 2340.82]  So, we sort of try to build this notion of what we call these two-tower embeddings,
[2340.82 --> 2349.22]  which represent the member side and the job side, and bring that together along with more near-line and real-time features
[2349.22 --> 2356.60]  to sort of then personalize it to what that particular member is also looking for to do, if I may, our matching, right?
[2356.64 --> 2360.68]  Of course, if it's on the search angle, then you also have the query context that comes into play.
[2360.68 --> 2366.78]  On the recommendation side, it's a lot more just based off of your activity signals and so on and so forth,
[2366.80 --> 2370.90]  that we try to infer intent to be able to make those recommendations.
[2371.38 --> 2375.08]  But to your point, yes, on the underlying surface, we do have these embeddings.
[2376.08 --> 2385.04]  And we are going to be writing a blog post pretty soon about at least this particular data layer in our talent solution business.
[2385.60 --> 2387.68]  Awesome. Yeah. Thank you for explaining that.
[2387.68 --> 2392.98]  And for listeners that are maybe new in the space as well, when we're talking about embeddings,
[2393.16 --> 2401.64]  we're talking about, you know, you could think about representing a candidate or member in this case as a series of numbers.
[2401.76 --> 2405.68]  You could encode them and you could define how those numbers should be yourself, you know,
[2405.74 --> 2407.82]  that you could encode that in a certain way.
[2408.02 --> 2416.00]  But you could also say, well, I may not be able to, you know, pick the right encoding for this candidate for my task.
[2416.00 --> 2423.24]  I'll let my model learn how to encode or how to represent this certain entity or the set of data.
[2423.38 --> 2425.48]  In this case, a set of data about a candidate.
[2425.68 --> 2432.32]  And that sort of learned representation or learned set of numbers that represents, in this case, the job or candidate,
[2432.70 --> 2433.70]  we would call an embedding.
[2433.70 --> 2435.76]  So thank you for mentioning that.
[2436.38 --> 2441.32]  Kind of curious, as we've been talking about this, and within the context of LinkedIn is very good.
[2441.32 --> 2447.76]  If you look at its long evolution, you know, from the very beginnings when it was basically just an online resume.
[2448.32 --> 2457.24]  And over the years, you've developed that into really finding the person in that resume and showing those different aspects.
[2457.24 --> 2461.90]  Do you have any thoughts on, you know, and I'm not pushing you in an exact direction,
[2462.30 --> 2468.74]  but any thoughts on kind of how you find that personality, those soft skills beyond just, you know,
[2469.10 --> 2474.60]  good at presentations kind of thing, you know, that are not strictly like a hard skill like doing Python,
[2474.92 --> 2480.74]  but finding the person and trying to fit that personality type into different types of cultures and jobs?
[2480.74 --> 2487.38]  Because I would imagine that that's pretty complicated and that maybe any thoughts on how AI might be able to be used
[2487.38 --> 2489.54]  or anything that y'all might be able to share on that?
[2490.12 --> 2496.92]  So LinkedIn per se tries to, what we do at LinkedIn tries to learn from career transitions even now, right?
[2496.98 --> 2502.82]  So that's something that we have as a signal that goes into our recommended models as recently to say,
[2502.92 --> 2505.60]  hey, this is the career trajectory that this person has.
[2505.72 --> 2507.02]  Went from here to here to here.
[2507.02 --> 2512.56]  In some senses, you could start thinking of how long did it take for this person to get there to say,
[2512.68 --> 2518.82]  hey, this person is like an outlier superstar, or this is like an average sort of a career path that,
[2519.02 --> 2522.00]  you know, could be something that the recruiters may be interested in.
[2522.24 --> 2531.22]  But you are asking an excellent question in terms of, hey, how can we factor in more latent aspects of what a member brings to a table, right?
[2531.22 --> 2539.18]  Not just that, hey, look at my Python proficiency code, but this person is really, really motivated executor of tasks kind of a thing.
[2539.54 --> 2540.54]  Not yet.
[2541.08 --> 2543.90]  This is not something that we are able to leverage right now.
[2543.90 --> 2551.70]  But again, what we are trying to do in some of our recruiter facing projects, we call this our recruit assistance connect.
[2551.94 --> 2560.64]  This gives LinkedIn an inside view into how the candidate is sort of progressing through their different interview funnels, as an example, right?
[2560.68 --> 2567.14]  And now, maybe from understanding and at some point, if all the interviews are moving to video interviews,
[2567.14 --> 2571.30]  we already have debuted a notion of what we called video introduction.
[2571.86 --> 2578.52]  And this, to your earlier question, also makes use of Microsoft technology to sort of try to figure out, hey, how is the,
[2579.72 --> 2584.92]  today it is with the intention of giving feedback to the candidate to say, hey, speak with more confidence,
[2584.92 --> 2588.26]  or, you know, you had all these ums and ahs and so on and so forth.
[2588.32 --> 2591.22]  So to enable the candidate to prepare for that, right?
[2591.22 --> 2599.26]  Now, with the permission of the candidate and of course, the company which is gathering all of this data can be at some point,
[2599.36 --> 2602.00]  then learn from all of these behavioral signals.
[2602.00 --> 2605.72]  But I think it has to be more than just your resume at that point, right?
[2605.76 --> 2609.48]  You need to have all of these other data points flowing into the system.
[2609.58 --> 2615.82]  So we are making smaller steps, but still within the world of what is being collected for the purposes of recruiting.
[2615.82 --> 2623.40]  But I can visualize a case for someone wanting to say, hey, then, you know, in some very ambitious world,
[2623.52 --> 2627.70]  if we could then say, hey, how is this person interfacing within the company, right?
[2628.26 --> 2631.98]  How quickly are you able to start collaborating with your teammates?
[2632.24 --> 2638.04]  How quickly are you able to be up and running in being able to get something shipped to production and so on and so forth, right?
[2638.36 --> 2639.82]  Does this data exist?
[2639.94 --> 2641.46]  Of course, it does exist, right?
[2641.46 --> 2645.62]  Now, do we think we'd be able to drive the right decisions?
[2645.84 --> 2650.28]  Do we think we'll be able to build the right models to tease apart the Latin signals?
[2650.38 --> 2657.82]  So make sure, again, the idea here should be to want to do something to propel everybody forward, right?
[2657.88 --> 2661.30]  And at the expense of nobody else in some way, right?
[2661.74 --> 2662.90]  Would we do it well?
[2663.10 --> 2665.40]  I need to think about this a little bit more.
[2665.56 --> 2667.32]  I want to say we want to get there.
[2667.32 --> 2672.90]  And more so, more than anything else, there is inefficiency in the interview process, right?
[2672.96 --> 2675.60]  Like, hey, I've spent 20 years working.
[2676.00 --> 2679.26]  And how are you going to judge whether I'm going to be good for my job?
[2679.30 --> 2681.08]  Of course, there is some skill and art to it.
[2681.36 --> 2685.48]  But it's also exhausting that you have to keep taking and talking about these credentials,
[2685.70 --> 2690.28]  establishing this credibility over and over and over again every time you want to switch something else.
[2690.28 --> 2697.06]  So how can we sort of package that into something more than assessments to say, hey, here is this candidate.
[2697.26 --> 2703.38]  In my mind, I call it a credit score of sorts, if I may, that you can sort of carry along with you.
[2703.54 --> 2704.84]  But we are ways from there.
[2704.90 --> 2707.32]  But I think the building blocks are being put in place.
[2707.84 --> 2709.80]  So we take the pain out of recruiting.
[2709.94 --> 2713.74]  Sorry, it was a little bit of fiction and a little bit of reality.
[2714.56 --> 2715.04]  I liked it.
[2715.06 --> 2715.58]  No, it's good.
[2715.96 --> 2718.38]  I appreciate the answer there.
[2718.38 --> 2724.58]  As I was asking it, I thought, I was imagining if anybody was thinking about this, it was going to be you guys.
[2724.72 --> 2728.20]  And I imagine you guys are going to be leading on this, given your position.
[2728.46 --> 2731.42]  So thank you for tackling a tough question for me there.
[2732.18 --> 2735.16]  And I have kind of a selfish question.
[2735.52 --> 2743.72]  I think from your perspective, it seems like you've spent a lot of time transitioning a lot of bleeding edge AI technology
[2743.72 --> 2748.14]  into the enterprise, into practical usage, into production usage.
[2748.38 --> 2755.40]  Even at LinkedIn, I'm looking at some of these blog posts about the search and recommendation and recruiter product.
[2755.72 --> 2757.74]  And there's links to research papers.
[2758.10 --> 2766.96]  And to some degree, you're tasked with bringing that bleeding edge research stuff into actual practical usage.
[2766.96 --> 2785.04]  And I'm just curious about your perspective or any recommendations that you could provide to other people out there who are wanting to use some of these, you know, maybe new AI technologies or new models that are published in terms of like the tech debt that comes with them.
[2785.04 --> 2792.92]  And the things that you need to think about as you're transitioning some of this technology into an actual practical use case.
[2792.92 --> 2795.54]  Thank you for asking this question.
[2795.92 --> 2805.68]  I think while a lot of us sort of get fascinated by, if I may, the technological advances in AI, right?
[2805.68 --> 2814.00]  The fact that we can ask questions out of an AI agent and express a meaningful and maybe almost human-like response.
[2814.40 --> 2824.24]  When it comes to actually putting these systems into production, I want to say that AI in some sense is an engineering discipline.
[2824.24 --> 2827.96]  But I think we are very much far away.
[2828.20 --> 2830.22]  And it comes, it's for a reason, right?
[2830.24 --> 2832.26]  It's not because we are unwilling to do so.
[2832.62 --> 2836.96]  It's just that the inputs are not as deterministic as some of these other systems, right?
[2837.02 --> 2847.72]  So whenever you have a change in your data distribution or something happens, then how do you put in, quote, the right unit and regression test to make sure that you're going to be able to catch some of these errors?
[2847.72 --> 2850.04]  How do you keep track of the number of people?
[2850.24 --> 2859.32]  And I can easily tell you the number of instances where, you know, a team deploys a feature and then there are 20 other teams with, unbeknownst to you, are starting to use this feature.
[2859.54 --> 2862.42]  And the next time you make the change, all hell breaks through, right?
[2862.50 --> 2866.00]  So how do you sort of have that discipline?
[2866.18 --> 2873.84]  And of course, many, many simple things that we possibly haven't spent enough time on in terms of feature lineage.
[2873.84 --> 2881.72]  When something goes haywire, how are we, are we able to quickly monitor, alert, track, rollback to a previously versioned system?
[2881.82 --> 2884.36]  How do we recover from that particular point of view?
[2884.64 --> 2888.14]  Do we keep going back to reduce, if I may, feature bloat, right?
[2888.18 --> 2896.16]  Because it's very interesting as a machine learning researcher to keep on adding, here's some set of new features, here's some set of new features.
[2896.16 --> 2903.78]  But at some point, you want to sort of take a step back and say, hey, holistically, how much have I improved this particular platform?
[2903.96 --> 2909.98]  Have some of the changes that we have done reversed some of the other changes that we would have pushed out otherwise.
[2910.42 --> 2916.82]  And even within a field of metrics, right, there is one layer of things that maybe we are pushing in the right direction.
[2916.82 --> 2921.14]  But then when you take a step back and say, hey, but what about long term engagement?
[2921.50 --> 2924.24]  Is this something that we have been able to holistically measure?
[2924.24 --> 2938.94]  So the more the field progresses, I wish a lot of us were a lot more diligent and cognizant of what it takes to maintain a machine learning system and production, especially if you're supporting a large organization, right?
[2938.94 --> 2945.62]  Then there are lots of customers and the outputs of your model could be used in many interesting ways.
[2945.94 --> 2948.60]  So how do you have the right contracts in place, right?
[2948.70 --> 2955.24]  And say, at least in some machine learning teams, the idea is, hey, here is this nice thing that the PM comes up with.
[2955.26 --> 2956.36]  Then you quickly work on it.
[2956.40 --> 2957.06]  Things work well.
[2957.12 --> 2957.92]  Everyone celebrates.
[2958.16 --> 2959.68]  And then you move on to the next thing.
[2959.68 --> 2965.44]  Then now who maintains, understands, or even figures out, hey, has this model drifted with time?
[2965.70 --> 2977.34]  And as much as I want to say AI has been democratized, people who are not familiar with what to expect out of the system don't even know what a rollback for this model should look like, or how do you even diagnose this thing?
[2977.34 --> 2992.92]  So there's been some good work from folks like in TensorFlow with TensorFlow X platform and these sorts of paradigms where we talk about AI metadata, which we need to be very religious about, which we need to start having health assurance and model monitoring and these sorts of things on.
[2992.92 --> 3009.20]  But as a discipline, as much as we want to train our folks in terms of all the latest and greatest in DNN tech, I wish we also had courses which talk about machine learning, model maintenance, and tech debt in schools as well.
[3009.58 --> 3014.42]  Because as this is going to just grow larger, it's going to become that much more important.
[3015.12 --> 3015.24]  Yeah.
[3015.34 --> 3019.72]  And it sounds like maybe at least at this point, hopefully that will change in the future.
[3019.84 --> 3021.00]  I certainly hope so.
[3021.00 --> 3044.44]  But it sounds like maybe in the interim, it's up to us who are maybe leaders on teams or leading certain projects to really insist and ask hard questions around this and anticipate into the future what we might need to monitor and where sources of bias are and what happens over time when we need to trace back what happened with a certain model.
[3044.44 --> 3053.12]  Do you have any other practical tips for maybe team leaders who are trying to push their team in this direction and are maybe struggling?
[3053.44 --> 3055.80]  Well, I want to maybe plug a paper.
[3056.06 --> 3062.22]  Google has definitely the machine learning depth of machine learning depth, sorry, is the paper that came out a few years ago.
[3062.22 --> 3082.12]  But more recently, they also released a framework of machine learning test scores, which basically is a very simple thing, which looks at, you know, the minimum score you could have gotten along either your feature monitoring, feature health about your model monitoring, and so on, so forth, which sort of gives you a simple rubric, if I may, to figure out how good is your system, right?
[3082.12 --> 3086.38]  Is it a house of cards, which is going to collapse the first time something goes on?
[3086.72 --> 3089.36]  Or is it a robust thing that can be deployed in production?
[3089.56 --> 3095.14]  So I think even adopting such a framework, and most of these things perhaps are not even automated.
[3095.38 --> 3107.84]  But if you have been in the weeds, and you understand how your model has been set up, you should be able to come up with this simple checklist to say, hey, yes, I think we are going to be robust to something catastrophic happening, because it will.
[3108.14 --> 3112.00]  There's no reason to think that anyone's going to be an exception.
[3112.12 --> 3120.50]  That would be a first start to even figuring out with respect to, if I may, the health of something that is being deployed in production.
[3120.86 --> 3125.52]  Now, this is like 101, if I may, like the basics of what you need to keep in mind.
[3125.92 --> 3133.96]  But Daniel, you also mentioned something even more fantastic, which is about, there is like model biases and data biases in the data.
[3134.14 --> 3137.42]  And then there is all the choices that our models make, right?
[3137.48 --> 3140.54]  Like, because we were going after a particular product objective.
[3140.54 --> 3146.22]  Now, what is the longer term impact that this may have overall in our user base?
[3146.28 --> 3149.48]  Is it going to be unfair to some segments of our population?
[3149.78 --> 3155.86]  That's an even bigger ethical fairness question that I think is becoming more and more pertinent these days.
[3156.28 --> 3157.68]  But it's interesting, right?
[3157.72 --> 3162.84]  In one hand, we are talking about like pure health and just monitoring of the system.
[3162.84 --> 3173.20]  And on the other hand, we are in the crossroads where we are even having to think about societal impacts, which I think speaks to the rocket ship speed at which this field has grown.
[3173.90 --> 3177.66]  But something for everyone getting into AI to be aware of.
[3177.94 --> 3178.04]  Yeah.
[3178.04 --> 3182.68]  Yeah, I think that's a really good perspective as we kind of come here to a close.
[3182.82 --> 3192.10]  I really appreciate you kind of bringing us in on a couple of those practical things because obviously you've developed a lot of great systems that have made an impact over time.
[3192.10 --> 3194.60]  And it's great to get that perspective.
[3195.04 --> 3201.24]  We certainly appreciate you joining us on the podcast and taking time out of your busy schedule to join us.
[3201.24 --> 3214.82]  And of course, you know, all you people out there on LinkedIn right now, make sure and post this episode when it's coming live on LinkedIn and, you know, get that in the LinkedIn knowledge graph for all time.
[3215.48 --> 3218.64]  But yeah, thank you so much, Suju, for joining us.
[3218.70 --> 3220.10]  It's been a real pleasure.
[3220.10 --> 3227.08]  And I hope we do get to meet at some type of networking event in the future in the real world.
[3227.26 --> 3228.80]  So thank you so much.
[3228.80 --> 3229.64]  Of course.
[3229.82 --> 3231.66]  Thank you, Chris and Daniel, for having me.
[3231.74 --> 3236.46]  It was very nice talking about the future and the lesson of everything in the real world.
[3236.54 --> 3236.92]  Thank you.
[3240.56 --> 3251.78]  If you enjoy Practical AI, we would enjoy a five-star review on Apple Podcasts, a blog post in response to something said on the show, and or a recommendation to a friend or colleague.
[3252.22 --> 3255.34]  Those word-of-mouth recommendations really do make a difference.
[3255.84 --> 3258.70]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[3258.80 --> 3262.88]  It is produced by Jared Santo with music by the mysterious Breakmaster Cylinder.
[3263.32 --> 3266.34]  Thanks again to our partners who support this show's existence.
[3266.68 --> 3268.56]  Shout out to Fastly, Linode, and Robar.
[3268.88 --> 3270.10]  That's all we have for you today.
[3270.42 --> 3271.72]  We'll talk to you again next week.
[3271.72 --> 3273.82] اف We'll see you again next week.
[3273.82 --> 3276.72]  We'll see you on his next week.
[3280.92 --> 3281.36]  We'll talk to you again here.
[3281.60 --> 3284.46]  We'll see you soon.
[3285.04 --> 3285.36]  Thanks again to ourpm class.
[3285.44 --> 3285.56]  Bye.
[3285.58 --> 3286.88]  We'll see you then.
[3286.90 --> 3287.10]  Bye.
[3287.20 --> 3287.26]  Bye.
[3287.80 --> 3288.54]  Bye.
[3288.66 --> 3289.18]  Bye.
[3289.18 --> 3289.66]  Bye.
[3289.76 --> 3289.80]  Bye.
[3289.80 --> 3290.18]  Bye.
[3292.20 --> 3292.68]  Bye.
[3293.30 --> 3293.74]  Bye.
[3293.74 --> 3294.80]  Bye.
[3294.94 --> 3294.98]  Bye.
[3295.12 --> 3295.58]  Bye.
[3295.80 --> 3296.06]  Bye.
[3296.06 --> 3296.08]  Bye.
[3296.28 --> 3296.38]  Bye.
[3296.86 --> 3297.00]  Bye.
[3297.08 --> 3297.60]  Bye.
[3297.60 --> 3298.02]  Bye.
[3298.08 --> 3298.56]  Bye.
[3298.56 --> 3328.54]  Thank you.
