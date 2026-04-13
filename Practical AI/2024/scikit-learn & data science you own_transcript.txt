[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.32]  Learn how at Fly.io.
[35.46 --> 36.64]  Okay, friends.
[36.74 --> 40.96]  I'm here with a new friend of ours over at Timescale Avthar Suothen.
[41.32 --> 44.68]  So Avthar, help me understand what exactly is Timescale.
[44.88 --> 46.44]  So Timescale is a Postgres company.
[46.92 --> 52.20]  We build tools in the cloud and in the open source ecosystem that allow developers to do
[52.20 --> 53.08]  more with Postgres.
[53.08 --> 58.22]  So using it for things like time series, analytics, and more recently, AI applications like RAG
[58.22 --> 59.26]  and Search and Agents.
[59.52 --> 65.48]  Okay, if our listeners were trying to get started with Postgres, Timescale, AI application development,
[66.00 --> 66.68]  what would you tell them?
[67.00 --> 67.70]  What's a good roadmap?
[67.96 --> 72.98]  If you're a developer out there, you're either getting tasked with building an AI application,
[73.18 --> 76.72]  or you're interested and you're seeing all the innovation going on in the space and want
[76.72 --> 77.64]  to get involved yourself.
[77.64 --> 84.14]  And the good news is that any developer today can become an AI engineer using tools that
[84.14 --> 85.22]  they already know and love.
[85.48 --> 90.16]  And so the work that we've been doing at Timescale with the PGAI project is allowing developers
[90.16 --> 95.40]  to build AI applications with the tools and with the database that they already know, and
[95.40 --> 96.26]  that being Postgres.
[96.56 --> 99.20]  What this means is that you can actually level up your career.
[99.20 --> 101.22]  You can build new interesting projects.
[101.58 --> 105.58]  You can add more skills without learning a whole new set of technologies.
[106.08 --> 108.10]  And the best part is it's all open source.
[108.38 --> 111.44]  Both PGAI and PG Vector Scale are open source.
[111.60 --> 115.98]  You can go and spin it up on your local machine via Docker, follow one of the tutorials on the
[115.98 --> 116.70]  Timescale blog.
[116.94 --> 122.00]  Build these cutting edge applications like RAG and Search without having to learn 10 different
[122.00 --> 126.44]  new technologies and just using Postgres and the SQL query language that you will probably
[126.44 --> 127.88]  already know and are familiar with.
[127.88 --> 129.26]  So yeah, that's it.
[129.32 --> 130.06]  Get started today.
[130.32 --> 136.12]  It's a PGAI project and just go to any of the Timescale GitHub repos, either the PGAI
[136.12 --> 141.00]  one or the PG Vector Scale one and follow one of the tutorials to get started with becoming
[141.00 --> 142.86]  an AI engineer just using Postgres.
[143.34 --> 150.20]  Okay, just use Postgres and just use Postgres to get started with AI development, build RAG,
[150.42 --> 153.44]  search AI agents, and it's all open source.
[153.44 --> 156.76]  Go to timescale.com slash AI.
[157.32 --> 158.92]  Play with PGAI.
[159.08 --> 162.90]  Play with PG Vector Scale all locally on your desktop.
[163.06 --> 163.94]  It's open source.
[164.44 --> 167.62]  Once again, timescale.com slash AI.
[167.62 --> 187.44]  Welcome to another episode of Practical AI.
[187.86 --> 189.46]  This is Daniel Whitenack.
[189.58 --> 196.28]  I am the CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[196.28 --> 199.66]  a principal AI research engineer at Lockheed Martin.
[200.18 --> 200.90]  How are you doing, Chris?
[201.36 --> 202.90]  Doing very well today, Daniel.
[202.96 --> 203.44]  How's it going?
[203.80 --> 204.56]  It's going great.
[204.84 --> 209.96]  I was saying that I'm really pumped to be talking about something that's near and dear to my
[209.96 --> 212.90]  heart over many, many years.
[213.16 --> 218.96]  Because today we have with us Jan, who's the CEO at Probable, and Guillaume, who's an open
[218.96 --> 220.74]  source engineer at Probable.
[221.30 --> 221.60]  Welcome.
[222.18 --> 223.02]  Thanks for having us.
[223.02 --> 231.82]  Well, Jan and Guillaume are working on data science that you own, including projects like
[231.82 --> 238.06]  Scikit-learn, which is, of course, very near and dear to me, along with other data scientists
[238.06 --> 239.64]  all around the world.
[240.08 --> 246.36]  So Jan, if you could, since you're coming from the CEO perspective, help us understand a little
[246.36 --> 252.28]  bit, maybe for those that have heard of Scikit-learn or some of the other projects that you're
[252.28 --> 254.98]  involved with, but they haven't heard of Probable.
[255.52 --> 258.86]  If you could give us a sense of what is Probable.
[259.30 --> 264.28]  As you mentioned, kind of in the lead up to this conversation, it's a slightly different
[264.28 --> 270.94]  kind of company that came about in different sorts of ways than other types of startups.
[270.94 --> 273.64]  So yeah, if you could give us a little bit of context, that would be great.
[274.12 --> 276.58]  Well, very glad to be on the show with you to date.
[277.00 --> 283.56]  And Probable is a company that is typically known as a spinoff from a research center in
[283.56 --> 284.88]  France called Inria.
[285.28 --> 291.08]  And Inria is the place where this technology, Scikit-learn, has been developed over the past
[291.08 --> 292.14]  10, 15 years.
[292.94 --> 294.48]  Not many people know that.
[294.48 --> 300.78]  And the project has been somewhat protected and sort of incubated within that research center.
[301.68 --> 309.76]  And after all that time, as you know, Scikit-learn has been adopted or even probably participated
[309.76 --> 316.08]  in creating the field of data science because it is applied math and essentially has created
[316.08 --> 323.76]  a sort of paradigm for how data scientists approach data science, typically through two functions,
[323.76 --> 325.44]  fit and predict.
[326.12 --> 331.20]  And the French government has a national strategy for AI, like many, many countries.
[331.64 --> 335.16]  And the government decided to double down on Scikit-learn.
[335.82 --> 338.14]  And they came up with a budget.
[338.58 --> 341.86]  They entrusted the research center with that budget.
[342.32 --> 346.56]  But then they also asked for the project to be break-even at some point.
[347.38 --> 351.60]  And the team said, okay, break-even is fine, but we don't do that in the research center.
[351.76 --> 352.42]  We don't break-even.
[352.42 --> 356.72]  So why don't we call an entrepreneur to try and help us figure it out?
[356.98 --> 357.86]  And they called me.
[358.46 --> 365.44]  So I have a track record as a software engineer and an entrepreneur in tech for the past 25
[365.44 --> 366.12]  plus years.
[366.80 --> 368.22]  But I'm not a data scientist.
[368.22 --> 370.00]  So I did my due diligence.
[370.00 --> 376.48]  And I sort of dug deep to find out what this project was all about under the hood.
[377.12 --> 377.82]  Is it any good?
[377.96 --> 378.94]  Is the community any good?
[379.10 --> 387.82]  And of course, Scikit-learn is this quite amazing jewel of a technology that every data
[387.82 --> 389.00]  scientist on the planet uses.
[389.14 --> 394.60]  I discovered that it was downloaded 1.5 billion times, cumulatively 80 million times a month,
[394.60 --> 398.08]  22% in the US, only 3% in France.
[398.62 --> 402.30]  So this is a project that is used all over the world.
[402.66 --> 410.18]  And Probable is essentially the spinoff that takes all of the team, including Guillaume here,
[410.58 --> 417.98]  from the research center and turns it into an open source company that inherited the mission
[417.98 --> 420.78]  that was initially given to the research center.
[421.04 --> 428.56]  And the mission is to build a suite of open source technologies, including Scikit-learn,
[429.02 --> 431.92]  but above and beyond Scikit-learn as well, for data science.
[432.60 --> 433.92]  So the scope is large.
[434.72 --> 435.64]  The mission is noble.
[436.42 --> 438.08]  And this is what we're building, essentially.
[438.26 --> 443.22]  So Probable is a one-year-old company that has already started doing many, many things.
[443.22 --> 451.10]  And Guillaume is the representative here for Scikit-learn, this technology that is used,
[451.24 --> 453.16]  again, by every data scientist on the planet.
[453.78 --> 457.74]  Well, this has brought up a lot of interesting questions on my end.
[457.78 --> 462.22]  And I really love the part of your pitch and at least how you framed it on your website
[462.22 --> 468.78]  and in your materials online about data science that you own and the open source side of this,
[468.78 --> 475.06]  which I know from experience, there can be some interesting challenges around finding
[475.06 --> 479.44]  business models that really work with open source technologies.
[479.84 --> 486.14]  And we've seen technologies where companies start with a posture towards open source and then
[486.14 --> 489.74]  gradually become more closed over time.
[489.74 --> 495.52]  So I'm wondering, from the leadership perspective, it sounds even in the way that this company was
[495.52 --> 503.00]  formed that there is a posture towards stewarding the Scikit-learn and these types of projects.
[503.24 --> 510.74]  But from your perspective, what is your posture towards stewarding these projects in the open source side?
[511.32 --> 516.62]  And how do you view the business element of this to make it sustainable in the longer term?
[517.10 --> 520.76]  So that is the hard question, but it is the one that is important here.
[521.36 --> 524.90]  Scikit-learn is a technology that is, again, applied math.
[524.90 --> 527.26]  It's not rocket science, but it's applied math.
[527.72 --> 529.04]  And it's quite intricate.
[529.78 --> 535.30]  The thing is, the scientific community uses it day in, day out.
[535.80 --> 537.42]  And everyone depends on this.
[537.42 --> 544.38]  So typically, when I discovered the scope of the project and the mission that was entrusted to the research center,
[544.62 --> 547.64]  I realized that this project is bigger than me, number one.
[548.08 --> 552.18]  Number two, the mission is to actually create more open source.
[552.18 --> 556.48]  In other words, in 2024, it's even more acute.
[557.16 --> 562.88]  Typically, big tech keeps on amassing so much power, concentration.
[563.56 --> 568.36]  And we could argue that they do not distribute as much as they should.
[569.06 --> 571.96]  So that's not a judgment, but it is a fact.
[572.54 --> 574.34]  And Scikit-learn is precisely the contrary.
[574.58 --> 577.50]  It actually enables so many companies to do data science.
[577.50 --> 589.22]  So with that in mind, before creating the company, we decided to craft a sort of architecture for the company that would respect that.
[589.22 --> 597.18]  And so, you know, before we created the company, before Guillaume joined as a co-founder, before I even incorporated the company,
[597.64 --> 608.46]  we had a template that actually created the governance, the shareholding structure, and also leveraging a new law in France that allows us to do a sort of B Corp.
[608.46 --> 617.22]  So a company with a mission, where the mission is clearly stated in the bylaws, and that mission is to create open source for data science.
[617.86 --> 625.66]  So in a way, we've created a sort of constrained environment that is unlike many companies, because it's by design.
[625.66 --> 637.92]  This company by design has created guardrails so that the governance cannot take this company too far on the right, let's say, proprietary technology, or even changing the license.
[638.02 --> 639.16]  That's not in the cards.
[639.80 --> 650.70]  And we've created a sort of mechanism where, you know, if we do not uphold to the mission, then we can actually lose some of the assets, such as the brand.
[650.70 --> 656.14]  We are the official brand operator, but the brand belongs to the research institute, right?
[656.26 --> 656.56]  Still.
[656.78 --> 667.72]  So there are many mechanisms, trigger mechanisms that force us, including shareholders that we would bring in, to actually bind with the mission long term.
[668.32 --> 668.42]  Gotcha.
[669.12 --> 672.60]  You've raised so many questions for me that I want to ask.
[672.60 --> 686.10]  I actually want to take just a moment and kind of go back, because it occurred to me as we're talking about this, for some folks listening who may have never even used Scikit-learn, they might have heard the name and stuff, and you talked about it being applied math.
[686.20 --> 697.00]  Could you guys expand on that a little bit for somebody who hasn't had a chance to ever actually utilize it themselves in terms of what it's doing and kind of catch them up to us in the conversation a little bit?
[697.00 --> 702.02]  And then I'm going to pepper you with a few more questions, because you've got me really interested.
[702.22 --> 703.84]  You hit so many topics on that last.
[704.28 --> 704.50]  Yeah.
[704.64 --> 707.82]  So maybe I can give a bit of background.
[708.62 --> 712.36]  So Scikit-learn, basically, the tagline is machine learning in Python.
[713.12 --> 716.84]  So it goes back to the, let's say, statistical roots.
[716.84 --> 721.40]  So the simple answer is we try to make pretty predictive modeling.
[721.72 --> 731.64]  So try to use mathematics to form like data viewable in the future to like give answer to a specific question, to a specific paradigm.
[732.22 --> 741.92]  The big difference with generative AI or deep learning is just that all the statistics that you have there are simple stuff.
[741.92 --> 754.98]  So they are fundamentals and deep learning build on those, but are just like much more, let's say, costly to train, costly to in the inference states or not in the same scope as well.
[755.66 --> 764.56]  And Scikit-learn is like the de facto choice when you want to have like tabular data, so Excel spreadsheets data structuring this way.
[764.56 --> 775.46]  So that's a de facto way of training, like to be able to hit those spreadsheets and give back some labels or some like regression, let's say.
[775.96 --> 784.54]  And whatever is like image or NLP or like, this is like, let's say, deep learning and Transformers is more in that area.
[784.70 --> 791.62]  So we are more like back to what was machine learning like a few days ago, but that have many, many, many applications.
[791.62 --> 801.72]  Well, considering how incredibly popular and foundational in the data science world, could you kind of give me a little bit of a landscape view?
[801.78 --> 805.12]  And I'm not sure which of you would be the right one to answer, so you guys pick between yourselves.
[805.58 --> 814.40]  But a little bit about kind of how that fits into the data science landscape with AI coming in, just so that with people listening, they can kind of go,
[814.40 --> 819.56]  Ah, I see how it fits into the many organizations and tools that are out there.
[819.72 --> 821.86]  How do you think about that for that?
[821.90 --> 827.30]  And then I'll get back a little bit more to the organizational stuff that Yael was talking about a few minutes ago.
[827.76 --> 838.56]  So maybe I can answer like partly, which is by giving use cases and to see that, for instance, with a partner as well that we worked over the years,
[838.56 --> 842.04]  to give like where do you find machine learning?
[842.14 --> 849.30]  And for instance, machine learning can be found in healthcare where you want to, you know, you want to know if the drugs works or not.
[849.30 --> 860.14]  Then if you want to find diseases as well in some type of data, it could be as well like fraud detections in banks, in insurance, predictive maintenance,
[860.42 --> 864.04]  and those type of like all applications that you have since like many years.
[864.04 --> 867.82]  So let's say the use cases are very, very large.
[868.54 --> 875.70]  And what brings like Cyclone on that is that this is not, I mean, it's not for one of the use case.
[875.92 --> 882.56]  I mean, it was fought from the beginning to be general enough such that you can apply to any of those use cases and to come back to,
[882.66 --> 887.60]  let's say, classification and regression programs, let's say, or unsupervised learning as well.
[888.08 --> 892.10]  But like that you can apply the tool anywhere in that field.
[892.10 --> 895.00]  So maybe, Jan, you have something more to add?
[895.48 --> 902.18]  Perhaps also at the macro level is to say, you know, Cyclone does a lot of things, including deep learning.
[902.66 --> 909.86]  But to be frank, when you want to do deep learning, typically you'd go to PyTorch or TensorFlow.
[910.62 --> 913.46]  But for everything else, you know, Cyclone.
[913.84 --> 918.58]  In other words, in the great AI family of algorithms, there is machine learning.
[918.58 --> 920.80]  And within machine learning, you have deep learning.
[921.26 --> 929.76]  Within deep learning, you have other categories of algorithms such as, you know, transformer-based models that lead to LLMs.
[930.28 --> 933.18]  So it's basically, you know, Russian dolls of sorts.
[933.18 --> 941.02]  And scikit-learn is the biggest provider of algorithms in the machine learning space.
[941.48 --> 951.06]  And in fact, if you look at the downloads, typically, scikit-learn is downloaded as many times as PyTorch and TensorFlow combined.
[951.06 --> 962.58]  Which is crazy because now everyone is talking about, you know, LLMs, of course, but also deep learning because deep learning is currently in a spring state, not quite a winter yet.
[962.84 --> 969.40]  So, of course, deep learning and Gen.AI is a wonderful breakthrough.
[969.40 --> 976.00]  That being said, you know, I like to simplify sometimes the 80-20 Pareto distribution.
[976.52 --> 983.74]  So I had the intuition that 80% of the use cases out there use scikit-learn when it comes to machine learning.
[984.28 --> 986.30]  And people actually tell me, no, Jan, you're wrong.
[986.60 --> 989.26]  It's more like 90-95%, right?
[989.26 --> 1000.54]  Because in terms of, you know, technology that is robust, that is tried and true, that is used to actually, you know, turn a profit or return on investment.
[1001.36 --> 1002.74]  Banks and insurance companies, right?
[1003.10 --> 1004.58]  Guillermo is mentioning fraud detection.
[1005.20 --> 1007.98]  Fraud detection typically uses scikit-learn.
[1008.34 --> 1009.98]  And that actually saves money.
[1010.36 --> 1013.08]  That actually, you know, banks would be losing money without that.
[1013.42 --> 1016.26]  So it is actually quite essential.
[1016.90 --> 1018.36]  But again, it's applied math, right?
[1018.36 --> 1021.92]  So scikit-learn is only a facilitator to this category of problems.
[1037.00 --> 1037.86]  What's up, friends?
[1037.96 --> 1043.44]  I'm here with a friend of mine, a good friend of mine, Michael Greenwich, CEO and founder of WorkOS.
[1043.44 --> 1055.50]  WorkOS, WorkOS is the all-in-one enterprise SSO and a whole lot more solution for everyone from a brand new startup to a enterprise and all the AI apps in between.
[1056.00 --> 1060.86]  So, Michael, when is too early or too late to begin to think about being enterprise ready?
[1061.24 --> 1064.58]  It's not just a single point in time where people make this transition.
[1064.80 --> 1066.68]  It occurs at many steps of the business.
[1067.04 --> 1069.38]  Enterprise single sign-on, like SAML, auth.
[1069.38 --> 1071.72]  You usually don't need that until you have users.
[1072.24 --> 1073.92]  You're not going to need that when you're getting started.
[1074.34 --> 1075.70]  And we call it an enterprise feature.
[1075.98 --> 1081.18]  But I think what you'll find is there's companies, when you sell to like a 50-person company, they might want this.
[1081.38 --> 1084.86]  They actually, especially if they care about security, they might want that capability in it.
[1084.98 --> 1088.58]  So it's more of like SMB features even if they're tech forward.
[1088.94 --> 1093.86]  At WorkOS, we provide a ton of other stuff that we give away for free for people earlier in their lifecycle.
[1094.06 --> 1095.08]  We just don't charge you for it.
[1095.08 --> 1101.06]  So that AuthKit stuff I mentioned, that identity service, we give that away for free up to a million users.
[1101.38 --> 1102.84]  One million users.
[1103.42 --> 1108.04]  And this competes with Auth0 and other platforms that have much, much lower free plans.
[1108.20 --> 1110.38]  I'm talking like 10,000, 50,000.
[1110.58 --> 1111.82]  Like we give you a million free.
[1112.04 --> 1116.48]  Because we really want to give developers the best tools and capabilities to build their products faster.
[1116.80 --> 1118.28]  You know, and to go to market much, much faster.
[1118.28 --> 1122.44]  And where we charge people money for the service is on these enterprise things.
[1122.68 --> 1126.76]  If you end up being successful and grow and scale up market, that's where we monetize.
[1126.86 --> 1128.88]  And that's also when you're making money as a business.
[1129.24 --> 1132.12]  So we really like to align, you know, our incentives across that.
[1132.58 --> 1136.06]  So we have people using AuthKit that are brand new apps just getting started.
[1136.56 --> 1139.88]  Companies in Y Combinator, side projects, hackathon things.
[1140.26 --> 1143.68]  You know, things that are not necessarily commercial focus, but could be someday.
[1143.94 --> 1146.94]  They're kind of future-proofing their tech stack by using WorkOS.
[1146.94 --> 1150.40]  On the other side, we have companies much, much later that are really big.
[1150.78 --> 1153.18]  Who typically don't like us talking about them.
[1153.32 --> 1156.64]  Their logos, you know, because they're big, big customers.
[1157.14 --> 1162.22]  But they say, hey, we tried to build this stuff or we have some existing technology, but we're sort of unhappy with it.
[1162.48 --> 1164.18]  The developer that built it maybe has left.
[1164.48 --> 1168.42]  I was talking last week with a company that does over a billion in revenue each year.
[1168.54 --> 1172.74]  And their SKIM connection, the user provisioning, was written last summer by an intern.
[1172.86 --> 1175.82]  Who's no longer obviously at the company and the thing doesn't really work.
[1175.82 --> 1177.46]  And so they're looking for a solution for that.
[1177.56 --> 1179.40]  So there's a really wide spectrum.
[1179.58 --> 1183.94]  We'll serve companies that are in a, you know, their office is in a coffee shop or their living room.
[1183.94 --> 1188.14]  All the way through, they have a, you know, their own building in downtown San Francisco or New York or something.
[1188.42 --> 1191.86]  And it's the same platform, same technology, same tools on both sides.
[1192.16 --> 1193.26]  The volume is obviously different.
[1193.40 --> 1197.36]  And sometimes the way we support them from a kind of customer support perspective is a little bit different.
[1197.68 --> 1198.34]  Their needs are different.
[1198.52 --> 1200.38]  But same technology, same platform.
[1200.66 --> 1201.70]  Just like AWS, right?
[1201.72 --> 1203.58]  You can use AWS and pay them $10 a month.
[1203.58 --> 1205.72]  You can also pay them $10 million a month.
[1206.06 --> 1206.54]  Same product.
[1206.72 --> 1207.58]  Or more, for sure.
[1207.62 --> 1207.94]  Or more.
[1208.74 --> 1214.72]  Well, no matter where you're at on your enterprise-ready journey, WorkOS has a solution for you.
[1215.08 --> 1220.82]  They're trusted by Perplexity, Copy.ai, Loom, Vercel, Indeed, and so many more.
[1221.24 --> 1224.84]  You can learn more and check them out at WorkOS.com.
[1224.90 --> 1228.04]  That's W-O-R-K-O-S dot com.
[1228.04 --> 1230.88]  Again, WorkOS dot com.
[1233.58 --> 1253.06]  So, Jan, you were kind of already going there.
[1253.20 --> 1255.98]  And I love the direction that you're going with this.
[1255.98 --> 1264.26]  But I think maybe I could tee up a softball for you here because I'm personally passionate about the answer to this question.
[1264.26 --> 1267.20]  And you probably have a better view on it.
[1267.20 --> 1289.40]  But there might be people out there maybe listening to this podcast who are thinking, well, now that we have Gen.AI, we have large language models, I could put in a prompt to one of these models to do fraud detection or to find entities in text or to make some prediction of a classification.
[1289.40 --> 1319.38]  And, you know, sometimes that works.
[1319.38 --> 1324.04]  And I'm curious your perspective on this from the business side.
[1324.16 --> 1327.42]  And maybe Guillaume has some ideas on the technical side.
[1327.74 --> 1327.86]  Yes.
[1328.04 --> 1333.04]  So, Psychitern typically is this one technology that is patrimonial.
[1333.26 --> 1335.18]  In other words, it belongs to everybody.
[1336.26 --> 1342.42]  In fact, there is another stat when you look at, you know, the figures that are public, by the way.
[1342.42 --> 1343.94]  The number of dependencies.
[1344.36 --> 1350.32]  So, Psychitern is actually used by nearly 900,000 projects on GitHub.
[1350.82 --> 1353.38]  So, there's nearly a million projects that depend on Psychitern.
[1353.62 --> 1357.50]  And there's a new law that I discovered recently.
[1357.62 --> 1358.42]  Someone mentioned that.
[1358.88 --> 1359.70]  Lindy's effect.
[1359.70 --> 1366.78]  Which means that something that's been used long enough will remain important for long enough.
[1367.60 --> 1371.28]  So, not saying that Psychitern will go the way of COBOL.
[1371.76 --> 1373.50]  But Psychitern is here to stay.
[1373.74 --> 1377.00]  And we are with the community, the guardians of that.
[1377.00 --> 1385.26]  So, we're going to make sure that Psychitern remains there forever for companies that actually need it in a stable version.
[1385.96 --> 1390.34]  And, of course, Guillaume and the team are building up new features as we go.
[1390.74 --> 1390.80]  Right?
[1390.80 --> 1392.94]  So, there's a dedicated effort.
[1393.20 --> 1400.08]  And I should say that we have carved out nearly, you know, 10 people in the team are doing only that.
[1400.64 --> 1403.36]  Contributing to Psychitern and the other associated libraries.
[1403.36 --> 1416.22]  Now, your question, Daniel, is, you know, whether Psychitern will be obsolete in, say, a number of years because general purpose technology has made it, you know, irrelevant in some ways.
[1417.06 --> 1420.26]  Number one, Psychitern is extremely frugal.
[1420.76 --> 1422.38]  It actually works on CPUs.
[1422.74 --> 1426.42]  And it is well-controlled, well-understood.
[1426.80 --> 1429.82]  It's actually quite predictable in some ways.
[1429.82 --> 1435.78]  Whereas, deep learning is usually known as a black box where it's really, really hard to introspect.
[1436.70 --> 1443.76]  And so, Psychitern does produce for certain categories of problems things that are actually working quite well.
[1443.94 --> 1448.12]  More so than large language models, for sure, today.
[1448.42 --> 1456.44]  And more so than any sort of deep learning-based technology that we understand today.
[1456.44 --> 1469.48]  Now, it is possible that with additional data, additional training and techniques and even evolutions on the transformer-based model, we could improve and probably render obsolete Psychitern.
[1469.62 --> 1473.56]  But to us, and then Guillaume and I, we talk about that.
[1473.64 --> 1475.64]  And with the team, we also experiment with other LMs.
[1475.64 --> 1484.68]  And we are also trying to figure out how we can use these new technologies to actually help our first persona.
[1485.10 --> 1486.68]  And that is the data scientist.
[1487.10 --> 1492.66]  So, we are a technology provider to help data scientists.
[1492.66 --> 1497.28]  And increasingly so, the data scientist in enterprises.
[1497.80 --> 1505.80]  Because we will be creating value-adding services and solutions so that we can generate revenue to sustain our mission.
[1505.80 --> 1517.56]  So, the goal for us is to actually project ourselves while contributing to open source, but also create a sort of business value proposition, not dissimilar to Red Hat.
[1517.80 --> 1523.34]  Because that is the closest type of company that we identify with, in terms of spirit.
[1523.34 --> 1531.24]  To that point that you're making right there, you know, I'd like to get back to something that you said earlier that feels like you're kind of tying back to it anyway there.
[1531.36 --> 1535.56]  And that's that you talked about, you know, the mission to create more open source.
[1535.92 --> 1540.88]  And the mission that you're trying to create this environment that you're describing by design, you said.
[1541.42 --> 1550.66]  Which is, you know, and that with Psychit Learn here to stay for the long haul, it's going to be something that, you know, is not going away soon.
[1550.66 --> 1552.94]  It's solving such a high percentage of the problems.
[1553.30 --> 1565.62]  Could you describe a little bit about kind of what you're thinking around that in terms of further developing this particular set of software and the ecosystem around it so that we have the benefit, you know, for many years to come?
[1565.72 --> 1566.84]  How are you approaching that?
[1567.16 --> 1572.24]  So, the company is built with multiple business units, if you wish.
[1572.38 --> 1574.32]  That's a big word for startup, right?
[1574.32 --> 1581.80]  But we have multiple revenue lines and multiple activities even within the open source team, which is dedicated.
[1581.96 --> 1588.44]  So, Guillaume perhaps can elaborate on some of the other libraries that we support that complement Psychit Learn.
[1588.58 --> 1591.38]  So, you know, that's one way to answer the question.
[1591.46 --> 1595.52]  But also, we are building a new product, which I call reversible SaaS.
[1595.52 --> 1601.28]  So, we are building a product that will provide additional value to data scientists.
[1602.08 --> 1609.22]  And the goal is to create a sort of, I don't want to use the term copilot because that is too close to LLMs.
[1609.54 --> 1610.80]  But it is the spirit.
[1611.30 --> 1618.42]  We are building a companion to augment the work of data scientists all the way to teams.
[1618.42 --> 1623.72]  So, that is an additional product on top of Psychit Learn because Psychit Learn just works.
[1624.62 --> 1626.14]  And so, we don't want to change that.
[1626.72 --> 1636.30]  And contrary to a company that would build a SaaS solution with a proprietary approach, we want to say, okay, whatever you guys use is fine.
[1636.72 --> 1639.46]  We need to find a way to add new value.
[1640.06 --> 1643.00]  And some of it will be open source, fairly modular.
[1643.00 --> 1653.14]  But for those companies that have more money than time, that need more service than be on their own, we'll have a solution for you and we'll make your life easier.
[1653.58 --> 1657.52]  And, you know, data scientists are a new breed.
[1657.96 --> 1659.16]  It's a new type of job.
[1659.26 --> 1660.72]  It's not been around for very long.
[1660.72 --> 1667.86]  And in a way, when I talk to people, so, you know, I've been in code forever and you know this, right?
[1667.88 --> 1673.06]  The developers, when they get hired, they are turnkey in some ways, right?
[1673.46 --> 1678.46]  They have their Git environment and they know how to peer code and that's all pretty standard.
[1678.56 --> 1681.50]  But when you talk about data scientists, it's actually quite artisanal.
[1681.84 --> 1684.04]  It's an art and a science at the same time.
[1684.04 --> 1689.96]  And you're manipulating two objects, actual code, but data scientists are not coders.
[1690.20 --> 1691.88]  And you're manipulating actual data.
[1692.26 --> 1692.94]  It's not code.
[1693.46 --> 1694.10]  It's patterns.
[1694.68 --> 1700.90]  And so data scientists have a difficult task, which is to combine these two things and create value for the enterprise.
[1701.18 --> 1704.78]  And then they talk to business units and they're like, what do I do with this model?
[1705.48 --> 1706.84]  How do I put it in production, right?
[1706.84 --> 1710.52]  So there is a huge conundrum to solve and that's what we're going to do.
[1711.02 --> 1715.38]  Additionally to building open source that are modules that people can use.
[1715.66 --> 1720.30]  Maybe Guillaume, you can elaborate on some of the other libraries that are key to actually help.
[1720.80 --> 1721.00]  Yeah.
[1721.40 --> 1724.56]  So within Probable, so we have the open source team.
[1724.82 --> 1729.24]  And so we worked for like many years on Psychicland already, but we see the importance.
[1729.24 --> 1737.44]  And as a community, which is the importance of putting models into productions and as well getting closer to the data sources.
[1738.06 --> 1745.84]  So we are just like working on libraries that should like make those come together.
[1746.30 --> 1751.10]  So for instance, we have a library that is more on the MLB side that is called SCOPS.
[1751.10 --> 1764.38]  We work a bit to make like the persisting more secure in some way, but we look as well on how to bring databases like SQL words into like closer to the machine learning models.
[1764.86 --> 1770.96]  So like how can you transform data with states, with different tables and how you can be in your Python words.
[1771.08 --> 1776.06]  We were caring so much about like SQL for instance and how you can bring this into psychic learn.
[1776.06 --> 1786.88]  And within psychic learn as well, we want to improve like whatever is visualization, evaluations, inspection of models, which is on the top of just like training an algorithm.
[1787.28 --> 1792.06]  Because this is so we want to augment all those aspects in like beyond us.
[1792.52 --> 1797.32]  And either is in psychic learn or either this is like library connected to psychic learn, let's say.
[1797.68 --> 1800.00]  So the one before is called scrub, by the way.
[1800.44 --> 1801.82]  So it's like scrubbing data.
[1801.82 --> 1806.18]  So it's scrub and scops are two libraries that we look at.
[1806.96 --> 1817.24]  So, you know, as we're kind of talking about the libraries now, you know, you have this robust open source contributor community built up around psychic learn and the various projects within it.
[1818.02 --> 1820.32]  How does probable work with those?
[1820.40 --> 1823.06]  How have you guys set up that relationship?
[1823.44 --> 1829.66]  What is the governance look like on that with, you know, because you have both your core team that you alluded to earlier.
[1829.66 --> 1835.66]  That's working in probable, you know, at probable on this, but you also have that larger open source community.
[1836.60 --> 1838.10]  How, how does that all work?
[1838.16 --> 1840.62]  Can you kind of tell us how that's evolved?
[1840.72 --> 1842.44]  I imagine it's quite mature by now.
[1842.78 --> 1843.44]  And that's the point.
[1843.58 --> 1851.24]  The maturity means that by design, we decided to not affect the license of psychic learn.
[1851.64 --> 1853.12]  We're not branching it out.
[1853.30 --> 1854.52]  We're going to care for it.
[1854.52 --> 1860.00]  And so the governance of psychic learn being so sane already means you don't touch it.
[1860.22 --> 1862.06]  If it ain't broke, don't fix it.
[1862.30 --> 1864.14]  So the governance is unchanged.
[1864.66 --> 1870.94]  So the center of gravity was at INRIA, the research center, but also involving people all over the world.
[1871.72 --> 1873.90]  I don't know, Guillaume, how many contributors?
[1874.08 --> 1874.50]  Maybe 200?
[1875.18 --> 1876.30]  Or even more.
[1876.30 --> 1878.82]  I think like in a year you have more, more than that.
[1878.94 --> 1881.02]  You have maybe like maybe three, four hundred.
[1881.74 --> 1888.62]  And the core team is like, let's say half of it might be around France, around Paris, around probables.
[1888.80 --> 1898.52]  But then there's like another half of 10-ish person around the world that contributes very like almost every day, let's say, by communicating with the community.
[1899.04 --> 1902.42]  And as Ian mentioned, like we didn't want to change that.
[1902.70 --> 1904.12]  Nothing changed in that regard.
[1904.12 --> 1910.12]  So the only thing that we actually did more, we did more to bring transparency.
[1910.94 --> 1911.90]  So to explain to people.
[1912.06 --> 1923.70]  So now that we're improbable, we feel that because we are a private entity, we need to communicate what are we doing and what are our roadmap and which community items are we going to work on?
[1923.98 --> 1932.02]  Just to like bring more trust such that, I mean, we don't like go like in the dark and that nobody knows now what we're doing.
[1932.02 --> 1939.60]  So we try to really to pay attention to every six months to mention which of the items that are defined by the community.
[1939.84 --> 1949.68]  They are not defined by by probable, but from the items, which one we have the capacity to work with the human resources that we have, let's say, at hand.
[1949.68 --> 1952.62]  So we really want to show that.
[1953.46 --> 1963.60]  And then by design, the open source team that is full time on PsychicLearn and other open source libraries means it's a cost center to the company.
[1963.60 --> 1966.00]  So that cost center is by design.
[1966.10 --> 1967.78]  And we know that's a cost we have to cover.
[1968.16 --> 1970.70]  So we will cover it through different types of activities.
[1970.92 --> 1977.24]  So, for instance, and this was something that was done in the past where brands were sponsors.
[1977.66 --> 1988.04]  So either they hire someone that becomes a core developer and they're naturally sponsoring someone to build up this technology,
[1988.04 --> 1992.50]  or they were giving money as a donation to the research center.
[1992.50 --> 1999.18]  But now that the team is with us, we are translating this into a contractual sponsorship framework.
[1999.88 --> 2006.26]  And so, you know, brands who want to contribute to PsychicLearn and help us compensate for salaries,
[2006.50 --> 2009.12]  we'll get something in return, exposure.
[2010.14 --> 2016.44]  And if they actually put more money into it, then we'll have a conversations around the roadmap.
[2016.90 --> 2020.00]  Find a way to make it converge in a win-win kind of way.
[2020.00 --> 2024.56]  Right? Because Guillaume, for instance, can say, you know, this brand wants us to do something,
[2024.62 --> 2025.90]  but it makes no sense for the community.
[2026.16 --> 2029.66]  Then we won't take their money for the sponsorship type of business.
[2029.88 --> 2030.02]  Right?
[2030.50 --> 2035.86]  However, if companies want to pay us to do a certain type of paid-for software, we'll look at it.
[2036.30 --> 2038.10]  But that's a different branch of the company.
[2038.42 --> 2040.44]  So we've really clearly separated.
[2040.44 --> 2043.32]  And by design, we know there's a cost to it.
[2043.82 --> 2053.02]  And that cost is actually, if we are doing well, it's compensated by the fact that we have done good by the brand.
[2053.58 --> 2057.72]  In other words, hopefully the community will actually resonate with what we're doing.
[2058.12 --> 2064.38]  And so they'll pay us back by actually appreciating what we're doing, which will carry the message further.
[2064.38 --> 2070.92]  So we think that there is a self-fulfilling prophecy if we actually keep adding value to the whole scheme,
[2070.92 --> 2073.38]  as opposed to removing value.
[2073.48 --> 2076.84]  And I will not name certain projects that have chosen a different way.
[2077.12 --> 2080.28]  But on the other hand, going back to the governance of the company,
[2080.84 --> 2086.30]  when a company flips and becomes VC-funded or only VC-funded,
[2087.06 --> 2090.58]  VCs require a sort of return on investment that is too radical.
[2090.58 --> 2097.74]  And so that sort of forces a change of posture vis-à-vis the community and the licensing scheme.
[2098.18 --> 2102.80]  In our case, we've actually created a structure that is balanced in terms of shareholding groups.
[2103.38 --> 2108.34]  And so we will ultimately have, that's the goal of the structure,
[2108.52 --> 2113.82]  the architecture is to have as much money from public support than from private support.
[2114.14 --> 2115.70]  So it's, again, sort of balanced.
[2120.58 --> 2142.04]  You know, when we started podcasting back in 2009,
[2142.46 --> 2144.92]  an online store was just the furthest thing from our minds.
[2144.92 --> 2148.26]  Now we have merch.changelog.com.
[2148.40 --> 2150.48]  And you can go there right now and order some t-shirts.
[2150.78 --> 2152.18]  And that's all powered by Shopify.
[2152.94 --> 2154.32]  What did we do before Shopify?
[2154.50 --> 2155.56]  I'll tell you, we did nothing.
[2155.70 --> 2156.40]  We couldn't sell.
[2156.64 --> 2159.66]  There were other ways, of course, but they were very hard, very difficult.
[2160.16 --> 2165.96]  Shopify let us build out an entire front end, obviously, branded like Changelog is.
[2166.28 --> 2167.08]  It's amazing.
[2167.36 --> 2168.96]  Merch.changelog.com.
[2168.96 --> 2173.18]  And our favorite feature is we use their API to generate a new coupon code,
[2173.28 --> 2176.96]  a personalized coupon code for every guest that comes on our podcast.
[2177.42 --> 2180.66]  And they get a free t-shirt from our merch store.
[2180.90 --> 2181.64]  And that's so cool.
[2181.96 --> 2183.04]  They choose the shirt they want.
[2183.38 --> 2184.56]  They use the coupon code.
[2184.72 --> 2186.50]  It arrives free of charge to them.
[2186.74 --> 2188.44]  And life is amazing.
[2188.84 --> 2195.24]  But also, you can go there right now to merch.changelog.com and buy some threads yourself.
[2195.44 --> 2196.34]  And that's awesome as well.
[2196.34 --> 2200.36]  So upgrade your business and get the same checkout we use with Shopify.
[2200.88 --> 2208.46]  Sign up for your $1 per month trial period at shopify.com slash practical AI, all lowercase.
[2208.80 --> 2213.58]  Go to shopify.com slash practical AI to upgrade your selling today.
[2213.82 --> 2217.56]  Again, shopify.com slash practical AI.
[2226.34 --> 2244.64]  So as we come back out of break here, I'd like to, I want to turn to kind of a fun question
[2244.64 --> 2245.40]  for you.
[2245.44 --> 2250.30]  And I'd like, I'd like each of you to take a swing at it because it's not specific to being
[2250.30 --> 2253.22]  the CEO or being, doing the technology itself.
[2253.76 --> 2261.26]  If each of you could describe kind of a cool use case, something fun or interesting, or that's
[2261.26 --> 2267.44]  really captured your imagination with scikit-learn and kind of share that with the listeners
[2267.44 --> 2272.08]  in terms of something that just kind of really took you as your thing.
[2272.08 --> 2276.78]  I'd love to hear, I'm expecting it to be a bit different coming from each of you and your
[2276.78 --> 2280.80]  different roles, but I'd love to hear kind of how, how you see that and what's the thing
[2280.80 --> 2281.74]  that sticks out in your mind.
[2282.16 --> 2284.26]  Guillaume, you start because I have to think about it now.
[2286.44 --> 2289.08]  So it's a very technical one, let's say.
[2289.08 --> 2291.64]  But so during my PhD, I was doing classification.
[2291.64 --> 2298.26]  So, which is something that I was trying to find people that has a specific type of cancer,
[2298.42 --> 2301.28]  so prostate cancer versus people that didn't have it.
[2302.10 --> 2307.18]  And inside that space, you had one fairly specific problem, which is called imbalanced
[2307.18 --> 2307.62]  data.
[2308.14 --> 2311.20]  And it's what introduced me basically to scikit-learn because I had that problem.
[2311.26 --> 2316.66]  I was using scikit-learn for the specific issues and how to tackle those type of issues.
[2316.66 --> 2322.60]  And what is really funny is that, so it's how I got introduced to scikit-learn and speak
[2322.60 --> 2323.90]  for instance with the developers.
[2323.90 --> 2329.14]  And I developed one library, which is called imbalanced learn, that is merging as well with
[2329.14 --> 2331.28]  scikit-learn, like it's compatible in some ways.
[2331.64 --> 2336.34]  And for many years, I maintained that package even when I was maintaining as well scikit-learn.
[2336.78 --> 2341.32]  And over years, years after years, we did everything by the book, basically.
[2341.52 --> 2345.96]  In that library, we implemented the arguments that were inside the literatures and everything
[2345.96 --> 2346.60]  was fine.
[2347.18 --> 2352.92]  Until that, as part of INRIA and now Probable, we have as well time to educate ourselves and
[2352.92 --> 2359.20]  to try to as well then bring through the documentations of scikit-learn to explain some concept to
[2359.20 --> 2359.46]  people.
[2360.06 --> 2365.48]  And by doing this, we find out that most of the research there didn't look at the problem
[2365.48 --> 2366.26]  properly.
[2366.26 --> 2373.48]  And by communicating with other core dev, we just found out that a huge part of this thing
[2373.48 --> 2377.78]  was just wrong and that you should look at it in another way.
[2377.78 --> 2383.70]  And then it's pretty funny because with this, we found like some useless stuff that was,
[2383.84 --> 2385.16]  for instance, inside imbalanced learn.
[2385.26 --> 2387.46]  But then now we have like better content.
[2387.66 --> 2391.68]  We went to conferences to explain these programs and people start to tell us, oh, yes, actually,
[2391.74 --> 2392.34]  that's right.
[2392.34 --> 2397.24]  And it's fun that you come and say that whatever you were doing like five years ago or 10 years
[2397.24 --> 2402.36]  ago is actually like obsolete or not good or, I mean, that's, we wouldn't expect from there.
[2402.80 --> 2407.80]  And it's something that I find really like fun when you do open source because you can,
[2408.50 --> 2413.10]  like, you are just here to contribute to something and just to bring like the best of what you
[2413.10 --> 2413.74]  do to everyone.
[2414.28 --> 2417.02]  And everybody will be like thankful for that.
[2417.02 --> 2423.38]  Even, I mean, and you are not defending your own, like, let's say, scientific paper or like
[2423.38 --> 2424.94]  that's all what is true.
[2425.42 --> 2430.56]  And for me, that's like one experience that comes from my PhD from like now eight or nine
[2430.56 --> 2433.06]  years ago to up where I am now.
[2433.16 --> 2438.14]  And then like, I see like an evolution where I was with very good people and you could like
[2438.14 --> 2440.04]  correct errors that you do in the past.
[2440.32 --> 2444.64]  And actually that will benefit everyone afterwards because that's learning inside the documentation
[2444.64 --> 2447.22]  of section or even inside the library.
[2447.72 --> 2452.64]  And then like everybody will just like, it says a million of users will be affected and
[2452.64 --> 2454.52]  say, Oh, actually that's good.
[2454.72 --> 2459.00]  And this is something that's, I would have stayed in academia for instance, three, that
[2459.00 --> 2464.18]  wouldn't have happened because you wouldn't have like time or be critic enough because you
[2464.18 --> 2468.36]  would have been like in, in, in the books, like pursue books and go like this.
[2468.36 --> 2470.58]  So that's one anecdote, let's say.
[2470.82 --> 2471.22]  It's good.
[2471.22 --> 2476.78]  I might be the CEO, but I do have the imposter syndrome because scikit-learn is so impressive.
[2477.14 --> 2478.26]  It's day in, day out.
[2478.40 --> 2486.28]  I mean, that team and Guillaume is very humble and, you know, very discreet, but the amount
[2486.28 --> 2493.20]  of knowledge and the amount of technicality that is trapped inside this library is mind-blowing.
[2493.52 --> 2495.92]  And you haven't met the other members of the team.
[2495.92 --> 2503.04]  And it's pretty much very, very hard to compete in terms of the amount of CPU cycles that go
[2503.04 --> 2503.38]  in there.
[2504.02 --> 2507.70]  So scikit-learn is the gift that keeps on giving in some ways.
[2507.94 --> 2511.30]  And the team is just out of this world and nice.
[2511.44 --> 2514.60]  And it's just a pleasure to work with that team all the time.
[2514.60 --> 2521.88]  Now, the more I discover scikit-learn and the more I find it amazing because of what the
[2521.88 --> 2523.06]  brand means to people.
[2523.30 --> 2528.74]  And so last week and today, actually, we just released, and if you allow us to actually put
[2528.74 --> 2530.00]  the link in the notes.
[2530.42 --> 2530.76]  Of course.
[2530.96 --> 2531.46]  Absolutely.
[2531.68 --> 2537.50]  We released the very first official scikit-learn certification program.
[2537.50 --> 2543.76]  And what's amazing is that we, so this is the first time, so we're doing it step-by-step
[2543.76 --> 2545.64]  and the system works.
[2545.82 --> 2546.60]  People can register.
[2546.78 --> 2548.44]  They can pass or fail the test.
[2548.86 --> 2555.12]  But without advertising, we had like within a couple of days, 600 registrations all over
[2555.12 --> 2555.62]  the world.
[2556.32 --> 2561.44]  A lot from India, actually, because people in India, they do work also remotely for other
[2561.44 --> 2562.72]  clients across the world.
[2562.72 --> 2567.68]  So they do need a stamp of approval to showcase their ability to provide a service.
[2568.32 --> 2575.06]  So very interesting that this brand almost instantly can promote a sort of service that
[2575.06 --> 2575.70]  is value-adding.
[2576.12 --> 2576.92]  So that's the one thing.
[2577.02 --> 2582.44]  But then on a more technical level, I fell in love with one new feature that came out
[2582.44 --> 2590.08]  with 1.5 of scikit-learn developed by another co-founder and core developer, Jeremy.
[2590.70 --> 2592.60]  And that is the callback feature.
[2592.72 --> 2593.30]  Why?
[2593.66 --> 2596.04]  Because scikit-learn, in fact, is a platform.
[2596.46 --> 2597.18]  It is a platform.
[2597.52 --> 2604.94]  And the callback feature allows us to provide extensions, if you wish, where people can hook
[2604.94 --> 2609.28]  into the inner workings of scikit-learn as they are building new models.
[2610.08 --> 2616.82]  And in fact, I find that to be essential because we are entering an age of liability with regards
[2616.82 --> 2617.34]  to AI.
[2617.90 --> 2620.12]  Companies need to be able to introspect.
[2620.12 --> 2626.08]  They need to actually find out why the model is producing such and such results.
[2626.50 --> 2628.56]  And so introspection is critical.
[2629.08 --> 2633.66]  And as I said earlier, deep learning is sort of a black box type of approach, which I love,
[2633.74 --> 2634.08]  by the way.
[2634.08 --> 2640.44]  Again, in 1992, I was building deep learning models in the middle of the winter of AI at
[2640.44 --> 2640.86]  the time.
[2641.24 --> 2646.20]  But scikit-learn is actually quite introspective, quite transparent, frugal, as I said.
[2646.20 --> 2653.68]  And so callbacks are yet another feature that provides actual introspection into how we build
[2653.68 --> 2654.20]  models.
[2654.56 --> 2659.72]  Because talk about insurance companies, fraud detections, you've got human beings at the
[2659.72 --> 2664.30]  end of the spectrum being handled by algorithms.
[2665.10 --> 2666.02]  And so that is critical.
[2666.02 --> 2671.16]  And I think we fulfill a very important need with these features.
[2671.46 --> 2674.20]  So again, scikit-learn, the gift that keeps on giving.
[2674.50 --> 2678.90]  And I'm impressed every day with a bit of an imposter syndrome because that team is just
[2678.90 --> 2681.76]  so, so powerful with this tool.
[2682.36 --> 2687.44]  And, you know, speaking of this team, Guillaume, I'm going to throw a question at you.
[2687.96 --> 2689.60]  People out there have been listening to this.
[2689.60 --> 2693.28]  They're kind of going, OK, I want to dig into this.
[2693.58 --> 2697.00]  So you're going to get some new developers that are going to come.
[2697.22 --> 2699.28]  How should they engage?
[2699.50 --> 2702.42]  How should they find and get started in the projects to develop?
[2702.88 --> 2705.32]  What's a good onboarding path for those developers?
[2705.86 --> 2710.40]  Probably the best onboarding path is like if you have a chance that's inside your local
[2710.40 --> 2715.38]  community, there's some people that do what we call first-time contribution to open source
[2715.38 --> 2716.62]  or like coding sprints.
[2716.62 --> 2720.18]  Go speak to those people because, I mean, they will help you to get onboard.
[2720.82 --> 2725.44]  But then like if you are behind your computer and then you don't know where to start, is
[2725.44 --> 2730.36]  where we have like documentations that describe what do we call contribution?
[2730.52 --> 2732.92]  Because contribution is not only coding.
[2733.22 --> 2741.02]  It could be speaking, debugging, documenting, organizing sprints and those type of things.
[2741.02 --> 2746.80]  So we have like what we consider as contribution and how you can help basically and where you
[2746.80 --> 2747.18]  can help.
[2747.28 --> 2749.70]  So, of course, the natural thing is to come and code.
[2750.18 --> 2753.10]  And then we explain you how to start with that.
[2753.16 --> 2758.20]  So this is on the documentation channel, the documentation webpage.
[2758.72 --> 2761.94]  And afterwards, everything is online and public.
[2762.08 --> 2763.18]  So there is nothing private.
[2763.18 --> 2765.68]  So we have different channels of communications.
[2766.08 --> 2771.26]  The main one is GitHub and it's going through the issue tracker or the pull request, like
[2771.26 --> 2772.70]  depending on which side you are.
[2773.42 --> 2779.16]  And the core developer will be, I would say, 24 hours over 24 because we are around the
[2779.16 --> 2779.36]  world.
[2779.60 --> 2785.06]  So that's like if I'm sitting there's somebody else in Australia or in the US that probably
[2785.06 --> 2786.52]  can like just answer to you.
[2786.52 --> 2788.88]  And then we'll just like give you feedback.
[2789.26 --> 2791.36]  And then and it's where your journey starts.
[2791.70 --> 2796.70]  You should not be shy and you should not be scared of making a mistake because we are
[2796.70 --> 2797.64]  not judgmental.
[2797.82 --> 2802.46]  That's we all started by by that stage of like saying, like, I don't know what I'm doing
[2802.46 --> 2805.14]  and I need to ask people what should I do.
[2805.20 --> 2806.32]  And that's a normal step.
[2806.50 --> 2811.24]  And afterwards, you just grow with the community and then the community bring you over.
[2811.24 --> 2815.88]  I mean, but the most difficult thing is, yeah, is the first step, like engaging and saying
[2815.88 --> 2818.70]  like, so I'm the imposter syndrome as well.
[2818.92 --> 2822.56]  But that people say, I don't want I mean, like this, like those very skilled people, they
[2822.56 --> 2824.36]  will never want to speak to me.
[2824.42 --> 2826.10]  And that's not the case.
[2826.48 --> 2828.62]  So just come and just try your best.
[2828.68 --> 2830.54]  And then people will just communicate with you for sure.
[2831.24 --> 2832.10]  Great guidance there.
[2832.68 --> 2838.40]  As we wind up, I'd like to get for each of y'all, for both Probable and for Scikit Learn,
[2838.98 --> 2841.14]  kind of what you think about for the future.
[2841.24 --> 2847.40]  And, you know, and I'll let you define what time span the future is, you know, whether
[2847.40 --> 2850.00]  it's, you know, a few months or years out.
[2850.18 --> 2855.74]  But I'd really like to, you know, to wind up, paint us a picture of when when the duties
[2855.74 --> 2860.78]  of the day have finished and you're just relaxing and you're thinking about what's
[2860.78 --> 2862.26]  possible going forward.
[2862.76 --> 2863.50]  What do you think about?
[2863.90 --> 2865.18]  I'll go with the mission.
[2865.70 --> 2868.70]  The mission is bigger than me, bigger than us.
[2868.70 --> 2872.70]  And so that's why the governance creates a self-sustaining model.
[2872.86 --> 2875.58]  So, of course, you know, it's not trivial.
[2875.80 --> 2879.46]  So there's a lot of work to achieve the mission long term.
[2879.90 --> 2882.30]  But that mission ends up with an IPO.
[2882.86 --> 2885.72]  In other words, this company is not meant to be sold or wrapped up.
[2885.72 --> 2891.40]  The goal is to do an IPO so that this company can carry on with the mission and allowing
[2891.40 --> 2894.64]  people to invest and be part of that story.
[2894.78 --> 2900.20]  And that's why earlier Daniel had asked a question about, you know, investors and all
[2900.20 --> 2900.34]  that.
[2900.34 --> 2907.14]  So we do have 70 individual investors, including people who were contributors or are contributors
[2907.14 --> 2913.48]  to Psychic Learn who don't have the chance yet to be employees full time of the company.
[2913.86 --> 2916.64]  So the goal is to create this sort of dynamic vehicle.
[2916.64 --> 2924.66]  And if we look at the North Star, there is no such company today that is the provider of
[2924.66 --> 2927.16]  open source machine learning technology.
[2927.40 --> 2928.80]  That company does not exist.
[2929.06 --> 2933.88]  And we aim to be that because we need that in an age where there's too much concentration
[2933.88 --> 2936.32]  within just a handful of players.
[2936.54 --> 2937.40]  That's not OK.
[2937.50 --> 2939.80]  It's not OK for the global South.
[2939.94 --> 2942.50]  It's not OK for Europe, which is lagging behind.
[2942.82 --> 2944.14]  But it's not even OK for the US.
[2944.14 --> 2949.84]  The US may have big tech, but that's not OK as a single model.
[2950.30 --> 2953.10]  We need people to own their data science.
[2953.62 --> 2955.30]  That's why that is our tagline.
[2956.00 --> 2956.50]  That was good.
[2956.74 --> 2957.88]  Guillaume, what are your thoughts?
[2958.54 --> 2965.36]  Yeah, so maybe more on, so on ProVable, I'm really thinking that we have a mission, let's
[2965.36 --> 2967.44]  say, to help more data scientists.
[2967.56 --> 2972.46]  But I will speak more about like, about Psychic Learn and the ecosystem.
[2972.46 --> 2980.96]  So for me, the mission is we should stay focused on what's happening out there and make sure
[2980.96 --> 2982.24]  that Psychic Learn is still relevant.
[2982.64 --> 2984.38]  So we have the foundational model.
[2984.48 --> 2985.02]  That's fine.
[2985.38 --> 2990.94]  But we need as well to understand where this is deployed and how this is used, because we
[2990.94 --> 2997.10]  can make such progress that bring, for instance, make it easier to bring databases to Psychic Learn
[2997.10 --> 3002.00]  or to bring Psychic Learn models into productions and to reduce friction and everything.
[3002.68 --> 3005.30]  And as well, bring values on understanding the model.
[3005.44 --> 3008.90]  I mean, we are speaking about AI acts as well in Europe now.
[3009.28 --> 3014.70]  So I'm sure there's like plenty of, let's say, area where we can have real impact.
[3014.70 --> 3017.84]  And then there's as well technology that's moved very fast.
[3018.06 --> 3021.08]  So for instance, before we knew Pandas, now this is Polar.
[3021.20 --> 3027.64]  So we need to move like in a fraction of seconds saying, how do we like deliver value to the
[3027.64 --> 3031.10]  user that just makes the switch and still can you Psychic Learn?
[3031.26 --> 3033.78]  Like, can I, can we do like accept those things?
[3034.12 --> 3036.58]  And then, so we have to make this audit of what's happening.
[3036.72 --> 3039.08]  So this is difficult to say where we will be in five years.
[3039.08 --> 3043.76]  Because in five years, we have all those things that can, let's say, we have the full chain
[3043.76 --> 3045.58]  of machine learning that probably will be here.
[3045.72 --> 3051.90]  So we should be aware, but we should be aware of whatever moves very fast around us to stay
[3051.90 --> 3052.46]  relevant.
[3053.24 --> 3054.84]  That was well said too.
[3055.40 --> 3062.00]  Gentlemen, you guys have done a fantastic job of teaching the rest of us about this.
[3062.20 --> 3065.16]  And thank you very much for coming on the show today.
[3065.66 --> 3066.04]  You're welcome.
[3066.62 --> 3067.16]  Always a pleasure.
[3069.08 --> 3077.60]  All right, that is our show for this week.
[3077.98 --> 3083.90]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[3084.14 --> 3086.38]  There you'll find 29 reasons.
[3086.60 --> 3089.80]  Yes, 29 reasons why you should subscribe.
[3090.36 --> 3091.82]  I'll tell you reason number 17.
[3092.38 --> 3095.14]  You might actually start looking forward to Mondays.
[3095.14 --> 3098.04]  Sounds like somebody's got a case of the Mondays.
[3098.04 --> 3103.00]  28 more reasons are waiting for you at changelog.com slash news.
[3103.18 --> 3108.88]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the beats and to you for listening.
[3109.30 --> 3111.92]  That is all for now, but we'll talk to you again next time.
[3111.92 --> 3112.68]  Ooh.
[3112.68 --> 3121.22]  Game on.
[3121.22 --> 3129.18]  Sixth two.
[3133.18 --> 3133.44]  Okay.
