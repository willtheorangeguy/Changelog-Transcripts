[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.46 --> 20.04]  This episode is brought to you by DigitalOcean.
[20.36 --> 25.12]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.12 --> 36.82]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 --> 42.54]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 --> 46.34]  Head to do.co slash Changelog to get started with a $100 credit.
[46.72 --> 48.80]  Again, do.co slash Changelog.
[55.12 --> 65.52]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[65.98 --> 69.92]  This is where conversations around AI, machine learning, and data science happen.
[70.34 --> 74.94]  Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[74.94 --> 76.30]  And follow us on Twitter.
[76.46 --> 78.10]  We're at Practical AI FM.
[78.10 --> 86.28]  Welcome to Practical AI.
[86.64 --> 88.20]  This is Daniel Whitenack.
[88.34 --> 91.42]  I'm a data scientist with SIL International.
[92.04 --> 97.24]  Normally, I would be joined by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[97.24 --> 102.94]  But he's in the midst of some family health-related things, so he's taking the time that he needs.
[102.94 --> 108.50]  But we're definitely excited to chat about a really interesting topic today.
[108.64 --> 117.88]  Actually, in our Slack channel, I remember some conversation a couple of weeks ago where we were discussing the issue of, hey, I trained my model.
[118.16 --> 119.46]  It works great on my data.
[119.72 --> 121.90]  I evaluate, and it all seems good.
[122.30 --> 127.54]  But then when I try to integrate this into code, the performance is actually really terrible.
[127.80 --> 131.18]  And it's kind of a mismatch between production things.
[131.18 --> 135.16]  And I think that we're going to be able to get into some of those things today.
[135.32 --> 140.58]  Today, we have as our guest, Nikita Shamganov, who is the CTO of MemSQL.
[141.08 --> 142.98]  We're really excited to talk to you today.
[143.34 --> 143.98]  Nikita, welcome.
[144.68 --> 145.54]  Happy to be here.
[145.80 --> 147.86]  Like Daniel said, my name is Nikita.
[148.02 --> 151.20]  Actually, I'm co-CEO and founder of MemSQL.
[151.56 --> 152.50]  I don't mind the confusion.
[152.66 --> 153.94]  I started as the CTO.
[154.40 --> 156.84]  And I took over as CEO in 2017.
[157.50 --> 157.94]  Gotcha.
[157.94 --> 165.92]  And recently, about a year ago, brought a co-CEO, Raj Verma, with the thinking that we're going to take the company public.
[166.74 --> 167.32]  Ah, gotcha.
[167.58 --> 175.74]  On that note, why don't you give a little bit of maybe the background first of yourself, and then we can get into maybe a little bit of the background of MemSQL.
[176.24 --> 177.60]  I think that would be great context.
[178.30 --> 178.70]  Definitely.
[178.70 --> 183.12]  So, I've spent my career in data management and databases, specifically.
[183.76 --> 193.60]  I came to the United States after finishing my grad school in St. Petersburg, Russia, and joined the SQL Server engine team.
[194.20 --> 201.42]  So, I went from kind of very research-oriented life and work to basically system engineering.
[201.42 --> 208.08]  When you build databases, it's actually a very different cadence versus using databases.
[208.44 --> 211.14]  When you use databases, you think about things like performance.
[211.40 --> 214.16]  You think about SQL as the API to the database.
[214.84 --> 216.96]  And then you think about reliability and uptime.
[217.38 --> 220.54]  And when you build a database, you think about quality.
[221.10 --> 227.36]  You think about the life of somebody who is using the database and how you make that life easier.
[227.36 --> 235.90]  And obviously, you think about performance and scalability and how the database user or developer can achieve that performance and scalability.
[236.32 --> 242.62]  It sounds like an interesting transition from the sort of academic world to the systems engineering world.
[242.86 --> 247.46]  Was it a hard shift for you or was that sort of focus on the user and reliability?
[247.82 --> 251.86]  Was that something that you were already kind of passionate about going into that work?
[252.22 --> 255.24]  I was very passionate about engineering in general.
[255.24 --> 261.84]  What I loved about building databases is that the product, the database engine, is like a computer science in a box.
[262.26 --> 263.44]  It has algorithms.
[263.74 --> 264.70]  It has data structures.
[264.98 --> 266.56]  It has system engineering.
[267.00 --> 270.70]  You interface with networking, I.O., CPU, caches.
[270.98 --> 276.36]  You need to be aware of the computer architecture in order to build world-class software.
[276.86 --> 278.70]  So, that certainly resonated a lot.
[278.70 --> 285.18]  And that was the core premise of why I wanted to start working on world-class industry products.
[285.92 --> 290.16]  And then, from there, the passion to the user came in.
[290.38 --> 300.40]  And over time, just that curiosity about building new things and breaking ground and entrepreneurship came through the years while working at SQL Server.
[300.40 --> 305.10]  And over time, mind you, during that time, Microsoft was going through a cloud transition.
[305.94 --> 313.78]  Everything that we're seeing today at scale, at that time, all of that stuff was being born, being conceived.
[314.10 --> 316.30]  And major architectural choices were made.
[316.64 --> 317.42]  Some of them were right.
[317.50 --> 318.48]  Some of them were not right.
[318.94 --> 321.64]  So, that's my kind of big company background.
[321.64 --> 324.18]  And then, I switched and joined Facebook.
[324.80 --> 334.62]  And, in fact, one of the premises of me joining Facebook was not to make a lot of money or because, you know, that was a pre-IPO, you know, 2010, right?
[335.10 --> 341.12]  I actually moved to the Silicon Valley and meet the kind of people I will later start a company with.
[341.78 --> 348.72]  And what happened is that as I walked into Facebook on day one, I met my future co-founder, Eric.
[348.72 --> 355.88]  And relatively shortly after, within six to eight months, we started MemSQL and I left Facebook.
[356.72 --> 358.54]  Oh, that's a wild ride, I guess.
[358.72 --> 366.64]  Moving to a total new place, experiencing, you know, Facebook and that culture, especially at that sort of stage, and then founding something.
[366.80 --> 374.72]  So, maybe describe a bit how, like, that happened so fast, the idea for MemSQL and the sort of motivation that this was something that was really needed.
[374.92 --> 375.54]  How did that occur?
[375.54 --> 381.68]  Yeah, so distributed systems at SQL Server, we always knew that was the future, right?
[381.78 --> 384.28]  Especially as you go into the cloud transition.
[384.84 --> 395.44]  And the time, you know, you know, back in, like, 2008, 2010, Microsoft had a flagship product, SQL Server, which is a single-node database system.
[395.62 --> 396.32]  Very, very good.
[396.52 --> 397.40]  Very, very powerful.
[397.68 --> 398.26]  Really proud.
[398.42 --> 399.10]  I worked on this one.
[399.10 --> 405.34]  The main competitor, Oracle, had distributed systems at its disposal, Oracle Exadata and Oracle Rack.
[405.34 --> 416.74]  And the way the database market is structured is that the top-tier workloads that have high performance requirements, high availability requirements, do require distributed systems.
[417.44 --> 419.28]  And Microsoft didn't have that.
[419.90 --> 424.72]  And so, that top of the market, Microsoft was losing to Oracle then.
[424.72 --> 427.42]  Actually, I think they mostly caught up right now.
[428.12 --> 436.76]  But then, architecturally, single-node databases are very hard to change and make, turn them into a distributed system.
[437.56 --> 444.80]  That was some of the, you know, kind of moonshot projects that my co-founder and CTO, Adam, worked on at Microsoft.
[444.80 --> 447.84]  And that moonshot project didn't succeed.
[448.02 --> 453.06]  When I walked into Facebook, the need for distributed systems became apparent.
[453.68 --> 458.32]  Because every Facebook workload is that high-level, high-end workload.
[458.98 --> 461.58]  And sometimes it's from the reliability standpoint.
[461.84 --> 463.50]  Sometimes it's from the scale standpoint.
[463.74 --> 465.22]  Most of the time, the scale standpoint.
[465.66 --> 470.94]  Because, you know, back in 2010, I think Facebook was on the march to cross a billion active users.
[471.54 --> 473.24]  So, that was on everyone's mind.
[473.24 --> 474.36]  That was everyone's goal.
[474.80 --> 477.22]  How can we cross a billion active users?
[477.52 --> 482.34]  And obviously, you know, history shows that Facebook had blown through that goal quite successfully.
[483.22 --> 487.26]  Were they trying to architect something internally to deal with that?
[487.36 --> 489.78]  Or was it sort of an open problem when you were there?
[490.34 --> 492.20]  It's more than one system, right?
[492.28 --> 494.60]  For something that is so big, right?
[494.96 --> 500.00]  As Facebook, it turns out that all the data workloads are split into categories.
[500.00 --> 501.92]  Some of them are data lakes.
[501.92 --> 506.62]  And, you know, Hadoop basically got a lot of advancements at Facebook.
[507.38 --> 510.64]  Some of them are operational, you know, powering Facebook.com.
[510.72 --> 518.48]  And multiple data management technologies are on the critical path between, you know, typing Facebook.com and actually seeing the news feed.
[518.48 --> 523.84]  There's a separate data management solution for messaging, separate news feed, and the list goes on.
[524.50 --> 532.00]  And within that, also, there's a whole bunch of kind of point solutions for various analytical workloads, right?
[532.00 --> 534.16]  One is for time series.
[534.70 --> 538.94]  In fact, there's a startup called SignalFX who took some of the ideas.
[539.18 --> 543.24]  And then the folks from Facebook left, started that company that was recently acquired by Splunk.
[543.64 --> 544.18]  I gotcha.
[544.68 --> 551.78]  And then there was a system called Scuba that gives you real-time analytics and a lot of ideas there influenced MemSQL roadmap as well.
[552.48 --> 559.18]  So, long story short, lots and lots of data management systems and data management workloads inside Facebook.
[559.18 --> 562.88]  But each and every one is a distributed system.
[563.60 --> 567.18]  And so, that pervasiveness of distributed system, we're captivating.
[568.04 --> 572.88]  It, like, really validated the thinking that the future of database systems is distributed.
[573.54 --> 575.20]  And that's how we started MemSQL.
[575.48 --> 575.82]  Awesome.
[576.08 --> 578.26]  And we started this as a memory, hence the name.
[578.82 --> 579.04]  Yeah.
[579.18 --> 587.10]  Now, in fact, the name is kind of limiting because MemSQL has evolved way past being in memory and memory only.
[587.10 --> 590.60]  It's the version one that was in memory and single node.
[590.60 --> 596.76]  But very quickly, we expanded to a distributed system, built tiered architecture from memory to disk.
[597.12 --> 600.60]  And now we expanded it to S3 or, you know, other object stores.
[600.60 --> 601.08]  Yeah.
[601.08 --> 601.60]  Yeah.
[601.60 --> 608.50]  I'd be interested to hear a little bit about, I mean, you kind of gave a sense of the initial founding and some of the initial ideas.
[608.68 --> 618.12]  I'd be curious as far as right now with MemSQL, could you just give a sort of high-level view of the sorts of things that people are turning to MemSQL for?
[618.50 --> 622.62]  Kind of the consistent things that you see really people getting value out of?
[622.62 --> 629.32]  And then maybe some of the newer things that are enabling maybe new sorts of workloads that you didn't even anticipate in those early days?
[630.08 --> 630.32]  Definitely.
[630.84 --> 634.06]  So, first of all, databases are very elongated.
[634.76 --> 634.88]  Yeah.
[634.88 --> 644.00]  And the most successful database products on the planet, which are Postgres, MySQL, SQL Server, and Oracle, are all 30 plus years old.
[644.28 --> 644.52]  Yeah.
[644.64 --> 651.12]  And we still use it today, which is basically if you turn into any other piece of technology, that's not the case.
[651.52 --> 651.82]  Yeah.
[651.92 --> 652.08]  Right?
[652.14 --> 654.68]  Technology is very transient, right?
[654.72 --> 658.98]  We're building something and something new comes in and completely disrupts what's there before.
[659.48 --> 662.30]  But database seems to stay for a long time.
[662.30 --> 662.82]  Yeah.
[663.18 --> 667.82]  I think in my experience from working at the different places, I've encountered Postgres a lot.
[668.26 --> 674.60]  I've encountered, you know, right now I'm working on a team that's using SQL Server for certain things.
[675.06 --> 685.02]  Of course, I've encountered certain things like, you know, Mongo or other databases that are, you know, like the NoSQL or those sorts of databases.
[685.02 --> 691.20]  But I think, like you were talking about the user experience, it always seemed like to me the natural user experience.
[691.20 --> 695.36]  And you gain a lot of power with that SQL interface to the database.
[695.76 --> 697.16]  The relational, yeah, for sure.
[697.62 --> 703.88]  And so, yeah, so the vision is a single pane of glass to all your data and all your workloads.
[704.06 --> 709.04]  But when you start peeling the layers and understanding what would it take to deliver on that vision,
[709.04 --> 718.92]  you start understanding how you scale storage, how you scale compute, and how you scale both storage and compute for your low latency operational workloads.
[718.92 --> 727.04]  Think about powering your apps and, you know, loading your web page and, you know, the results need to come back to you and ideally sub-100 milliseconds
[727.04 --> 735.38]  to running what is called big, expensive analytical queries that scan large volumes of data to give you insights.
[736.80 --> 738.44]  Those insights could be reports.
[739.10 --> 745.08]  Those insights could be information, analytical information, which is also called decision support.
[745.40 --> 745.52]  Right.
[745.52 --> 746.58]  You need to make a decision.
[747.02 --> 748.94]  So you need to know what works, what doesn't.
[749.80 --> 757.14]  You need to know, you know, how your sales are doing in this state versus the other state, this product versus that product.
[757.64 --> 765.82]  And so that is a continuous process of evaluating and looking at data and understanding, driving insights out of data.
[765.82 --> 777.16]  So the interesting piece about what I just described is that for your operational needs, you need a SQL database, right?
[777.30 --> 779.60]  Like Postgres, Lifeline, SQL, like SQL Server.
[779.96 --> 781.06]  I mean, you don't need it.
[781.12 --> 782.42]  I mean, you can use a MongoDB.
[782.60 --> 784.00]  You can use a NoSQL database.
[784.68 --> 787.04]  But you need an operational database, right?
[787.10 --> 788.20]  Let's just put it this way.
[788.20 --> 796.12]  And for the majority of workload, today, people are using relational databases that speak SQL.
[796.56 --> 804.30]  And for a smaller part of the market, they use NoSQL databases, which is more preference and user experience and whatnot.
[804.98 --> 810.36]  And then for an analytical system, people use data warehouses, Teradata, Snowflake, BigQuery.
[810.96 --> 813.78]  And the interface to those databases is also SQL.
[813.98 --> 814.46]  Yeah.
[814.46 --> 822.14]  And what you just started the podcast with is like, oh, I trained my model against the data that sits in the data lake or a data warehouse.
[822.68 --> 824.50]  And now I need to put it in production.
[824.50 --> 828.22]  And I have data quality, data consistency issues.
[828.36 --> 829.82]  My performance is not the same.
[830.22 --> 833.22]  A lot of that comes from the underlying data management.
[833.92 --> 843.46]  And if you really peel the layers, it comes from the fact that you run this very same model on top of data and data management systems that are different.
[843.46 --> 843.90]  Yeah.
[843.90 --> 847.46]  And one can argue that, well, they're different.
[847.64 --> 849.80]  They've got their reasons for them to be different.
[850.04 --> 860.64]  But there is a more contrarian viewpoint here that is we live in the world of clouds where things are abstracted away from you.
[860.64 --> 879.08]  And that gives you, ideally, a serverless interface that speaks SQL and that gives you access to all your data and gives you access to all your data for reporting capabilities, for low latency capabilities, for operational workloads.
[879.08 --> 888.34]  And that would allow you to never leave your data universe as you go and move from one workload to another.
[888.96 --> 889.84]  And that can be huge.
[890.30 --> 891.26]  That can be huge.
[891.26 --> 902.64]  Because whatever data you trained, for example, your example, whatever data you use to train the model lives in that ocean of data and that data is easily accessible to you.
[902.96 --> 904.44]  And then you train the model.
[904.56 --> 914.68]  So now you need to convert new data that isn't coming or, you know, marry new data to an old data and convert it into pixels, which is your app or a website or whatever.
[914.68 --> 922.68]  And that can be done right there off of the same data set you've been operating on, which is certainly not the case today.
[923.02 --> 936.76]  Today, you have a data lake, a data warehouse, and a number of operational databases that can be integrated by a third piece of software, like ETL tools or integration tools, which just generates a lot of complexity.
[936.76 --> 946.90]  And a lot of that can be simplified if you imagine a world of having a serverless SQL low latency API to all your data.
[947.96 --> 950.18]  That's the vision where we're driving towards.
[951.10 --> 953.74]  And this is a multi-year, probably multi-decade.
[953.86 --> 955.28]  My SQL is nine years old today.
[955.70 --> 958.50]  So it's going to be a multi-decade kind of life's work.
[958.50 --> 968.04]  But the workloads that we see emerging and the new workloads that are enabled by a system like this are real-time analytics and real-time decision support.
[968.98 --> 978.94]  When you need to kind of go back and look at the history of what was happening to make a real-time decision and do it at scale as well.
[979.26 --> 981.96]  So that is something that we see a lot in financial markets.
[982.56 --> 987.54]  You know, MemSQL is a give or take $40 million run rate company with 70% growth.
[987.54 --> 991.26]  We just had an article in TechCrunch where it revealed our numbers.
[992.06 --> 995.02]  And a good amount of that revenue is coming from financial markets.
[995.62 --> 998.40]  And if you think about it, like, that's what happens there, right?
[998.46 --> 1005.48]  There's a constant stream of information that's coming in, modifying that data state that you have.
[1005.70 --> 1009.46]  And you need to make decisions about, you know, buy, sell.
[1009.72 --> 1012.70]  You need to make decisions in wealth management.
[1013.10 --> 1016.50]  You need to make decisions in portfolio management and trading.
[1016.50 --> 1024.64]  But also, you need to make decisions in various systems that, for example, monitor, you know, something that's very, very large.
[1025.44 --> 1025.60]  Right?
[1025.74 --> 1028.84]  So in Morgan Stanley, for example, it's a trading system.
[1029.10 --> 1037.42]  And we monitor this trading system, providing decision support to, oh, should we provide some sort of maintenance?
[1037.76 --> 1039.26]  Should we reroute our trades?
[1039.52 --> 1040.58]  You know, all of those things.
[1040.58 --> 1043.64]  That's what NMSQL is used for today.
[1043.94 --> 1045.06]  And that's new.
[1045.28 --> 1048.68]  Like, we didn't have a system on the market that had those capabilities before.
[1048.68 --> 1062.92]  I'm Jared Santo, JS Party's producer and one of nine regular voices you'll hear on the show.
[1063.28 --> 1067.26]  We are a party-themed podcast, so fun is at the heart of every episode.
[1067.64 --> 1070.92]  One way we keep things fun is by mixing it up and trying new things.
[1071.22 --> 1072.96]  We play games like JS Jeopardy.
[1072.96 --> 1078.56]  This gives you access to an outer function scope from inside an inner function.
[1078.94 --> 1079.98]  Oh, I think that...
[1079.98 --> 1080.32]  Never mind.
[1080.84 --> 1081.68]  Global scope?
[1083.12 --> 1083.92]  Incorrect, unfortunately.
[1083.92 --> 1084.94]  Yeah, I didn't think so.
[1085.58 --> 1088.30]  Debate hot topics like should websites work without JS?
[1088.80 --> 1091.74]  I'm going to appeal to authority and read some quotes at this time.
[1092.46 --> 1092.98]  Okay.
[1094.44 --> 1096.34]  I've lost complete control of this panel.
[1096.46 --> 1097.30]  Go ahead, Ross.
[1097.46 --> 1098.14]  The first quote.
[1098.24 --> 1099.74]  No code is faster than code.
[1100.20 --> 1101.94]  Discuss and analyze the news.
[1101.94 --> 1110.30]  Yeah, this reminds me of when you're playing Pokemon and you have like, you know, an electric Pokemon versus a water Pokemon and you try like an attack.
[1110.70 --> 1112.58]  Share wisdom we've collected over the years.
[1113.14 --> 1118.00]  To be honest, a lot of what we rely on is pretty garbage.
[1121.24 --> 1124.02]  And like, I mean, I wrote some of it, so it's okay.
[1124.12 --> 1125.04]  Like, I can say this.
[1125.52 --> 1129.42]  Interview amazing devs like John Rezig and Amelia Wattenberger and a whole lot more.
[1129.72 --> 1131.44]  Oh, and did I mention we record the show live?
[1131.44 --> 1132.02]  We do.
[1132.02 --> 1136.22]  You can be part of the hijinks each and every Thursday at changeodd.com slash live.
[1136.54 --> 1137.86]  This is JS Party.
[1138.12 --> 1141.60]  Please listen to a recent episode that piques your interest and subscribe today.
[1141.96 --> 1143.12]  We'd love to have you with us.
[1143.12 --> 1161.14]  I definitely liked where you're going in terms of describing the sort of single window to all of your data via the SQL interface.
[1161.14 --> 1163.36]  And I know that we talked a little bit.
[1163.42 --> 1168.58]  So we kind of touched on the AI and machine learning elements of this and how they fit in.
[1168.66 --> 1174.96]  You're talking about going on this journey to create the single window of single interface to all of your data.
[1174.96 --> 1188.92]  How did AI and machine learning workloads start to cross your path at MIM SQL and start to be something that you felt like needed to be part of the strategy of how you were building out the system?
[1188.92 --> 1191.72]  Yeah, this is a great question.
[1191.72 --> 1206.30]  When we did our analysis, we discovered that about 20 to 30% of all the workloads that MIM SQL support have some sort of machine learning or AI angle to this.
[1206.42 --> 1206.78]  Oh, wow.
[1206.78 --> 1209.06]  So this is a very large number.
[1209.86 --> 1216.12]  And when we looked at it, you know, we always wanted to have AI, like dedicated AI capabilities in the system.
[1216.12 --> 1221.76]  And we certainly use AI internally to make certain decisions around workload management, query optimization.
[1221.98 --> 1234.18]  But the fact that the modern workloads and obviously people put modern workloads on MIM SQL have a lot of AI and ML capabilities was eye opening to us.
[1234.18 --> 1234.46]  Yeah.
[1234.46 --> 1235.02]  Yeah.
[1235.02 --> 1245.44]  In those cases that you noticed, was it like people that were, like you were saying, using MIM SQL to do kind of large queries to prepare their training data for an AI model?
[1245.76 --> 1246.44]  Actually, both.
[1246.90 --> 1247.64]  Both? Okay.
[1247.92 --> 1249.66]  And like two specific examples.
[1250.12 --> 1252.74]  Well, we have a great integration with Spark.
[1253.46 --> 1261.28]  So we have a Spark, MIM SQL Spark connector that allows, gives you very fast data exchange between MIM SQL and Spark.
[1261.28 --> 1264.34]  You know, fast mean multi-cluster to cluster.
[1264.72 --> 1268.06]  So like a multi-channel bus between the two.
[1268.34 --> 1274.34]  We noticed that people put all their data into MIM SQL, grab it through Spark, store models somewhere else.
[1274.62 --> 1277.12]  So we don't take part in hosting models.
[1278.00 --> 1279.32]  So this is the first part.
[1280.08 --> 1286.30]  And what people like about MIM SQL is that two-way path for data exchange between MIM SQL and Spark.
[1286.72 --> 1289.16]  If you have something in Spark, you can persist it in MIM SQL.
[1289.32 --> 1290.36]  You have something in MIM SQL.
[1290.36 --> 1292.22]  You can pull it into Spark.
[1292.76 --> 1295.10]  And MIM SQL is a world-class query processing engine.
[1295.44 --> 1308.84]  So you can send SQL query to it to do the kind of the first pass and slice and dice data before it gets fed into training algorithms, which MIM SQL itself doesn't support.
[1308.96 --> 1311.18]  It's just the backbone for that data.
[1311.18 --> 1318.08]  And the second use case that we started to see being pronounced is, well, people build apps on top of MIM SQL.
[1318.50 --> 1323.22]  And those apps have, you know, models, evaluate models real time.
[1323.22 --> 1337.06]  And they need to, usually there's some sort of an SLA for an app either displaying this information to the end user or the app is completely kind of back office and they just, you know, crunching data.
[1337.06 --> 1341.30]  And for that, they need to pull data from somewhere, run this data against the model.
[1341.30 --> 1346.18]  And based on the results that you see from that model, you know, do something.
[1346.32 --> 1347.60]  Typical example is fraud.
[1347.60 --> 1361.18]  And we do in transaction fraud detection for some of the major banks where the SLA is 40 milliseconds to make a decision if that particular transaction is fraudulent or not.
[1361.88 --> 1365.42]  And in order to make that decision, you need to go, you know, you have a model.
[1365.60 --> 1366.68]  That model is already trained.
[1366.68 --> 1378.00]  Then you need to grab some data for that specific account, go back and look at the previous, you know, thousand transactions, feed those transactions against the model.
[1378.32 --> 1382.12]  And then the model will tell you if it's a fraudulent transaction or not.
[1382.32 --> 1384.62]  So MIM SQL is supporting use cases like this.
[1385.42 --> 1386.38]  Yeah, that's really interesting.
[1387.24 --> 1387.44]  Right.
[1387.58 --> 1390.64]  So again, like both sides of the spectrum, right?
[1390.64 --> 1403.26]  Both just providing basically a data lake or data warehouse capabilities, put all your data in one place, let data scientists play with that data and use whatever data science tools, the tools du jour, right?
[1403.50 --> 1404.22]  Should it be Spark?
[1404.32 --> 1405.20]  Most talk SQL.
[1405.98 --> 1406.56]  Yeah, yeah, yeah.
[1406.74 --> 1407.58]  Should it be Spark?
[1407.70 --> 1408.92]  Should it be Pandas?
[1409.08 --> 1411.82]  Should it be TensorFlow or PyTorch?
[1411.88 --> 1412.16]  Whatever.
[1412.60 --> 1416.34]  We provide very, very fast data exchange to whatever frameworks you use.
[1416.76 --> 1420.08]  And the second one is, oh, I want to put my model into production.
[1420.64 --> 1428.06]  So I'm going to register that model somewhere in my, you know, either in Kubernetes, SageMaker, you know, there are tools for that now.
[1428.48 --> 1430.32]  And it's a rapidly evolving space.
[1431.22 --> 1433.40]  But it all starts with data anyway.
[1433.40 --> 1444.12]  So you need to have a data backbone and you need to have data management system with system of record capabilities in order to provide, you know, uptime, low latency, all of those things.
[1444.12 --> 1456.16]  And where it's going is we're thinking to keep building world-class integrations with systems that both data scientists use for training and engineers use for putting models into production.
[1456.16 --> 1459.90]  And then you need to enable that exchange from a push-button standpoint.
[1460.58 --> 1476.82]  Given you have a model, put that model somewhere, tell MimSQL about that model, and you'll be able to consume that model either from SQL, through user-defined functions, or through an application, query the model, query the data, you know, and the application provides the glue.
[1476.82 --> 1479.96]  Okay, so yeah, I was curious about that piece.
[1480.24 --> 1487.62]  So it sounds like right now this sort of workflow is you have an application like a Python application or whatever it is.
[1487.78 --> 1491.76]  You load your serialized model into memory.
[1491.76 --> 1502.04]  And then when it's time to fulfill a user request, then you make a SQL query against MimSQL, get the data you need, run it through your model, and respond to the user.
[1502.12 --> 1502.76]  Is that about right?
[1503.28 --> 1504.38]  Yeah, that's how it works today.
[1504.58 --> 1514.08]  And where it's heading is this will still be at probably 50% of the use cases because certain things you still want to control and write very, very custom logic.
[1514.08 --> 1514.52]  Yeah.
[1514.80 --> 1527.88]  But we want to make MimSQL aware of models that are stored in a particular repository and being able to, through SQL, to run data through those models and return results back into MimSQL.
[1528.22 --> 1529.34]  Yeah, that's really interesting.
[1529.84 --> 1537.54]  Yeah, the reason that's useful is that sometimes you want to run that model against a very large volume of data.
[1537.54 --> 1550.34]  And so if your application row by row pulls data from a database, runs it against the model, gets the results, potentially stores it back in the database, that is an extremely inefficient way.
[1551.16 --> 1561.04]  But what you can do is you can establish, similarly to Spark Connector, a multi-channel bus with optimized data format.
[1561.04 --> 1570.66]  We're thinking Apache Arrow or something like this, where running a model against a billion records should be a one or two second proposition.
[1571.22 --> 1571.98]  Yeah, that's awesome.
[1571.98 --> 1598.18]  I'm thinking of like a facial recognition use case or something like that, where you may want to run, compare the embedded representation of this image against thousands and thousands and thousands or maybe even millions of records that you have in your database that are reference faces from your facial recognition or something like that.
[1598.26 --> 1600.56]  Am I following the right sort of path here?
[1600.56 --> 1606.92]  You are, and we have use cases like this, where people store feature vectors in the database.
[1607.50 --> 1611.48]  In a way, people run this use case in MimSQL from the do-it-yourself kind of way.
[1612.76 --> 1616.82]  MimSQL supports vector tensor operations as a built-in.
[1617.48 --> 1627.56]  And obviously, facial recognition models, not all the time, but often, is represented as kind of a TensorFlow DAG, I would say, that evaluates.
[1627.56 --> 1632.48]  And the individual nodes in the DAG are vector math, right?
[1632.52 --> 1635.86]  They're not something that's spectacularly complex.
[1636.32 --> 1642.64]  It's a vector dot product, also known as a scalar vector multiplication, right?
[1642.64 --> 1644.70]  So, MimSQL does that.
[1644.70 --> 1658.82]  And we have customers that, in production, do facial recognition over millions of faces to enable things like, you know, somebody walks into a supermarket and they want to custom tailor the experience for that person.
[1659.06 --> 1661.16]  Or security systems in airports.
[1661.16 --> 1671.88]  And what happens is, there's a camera, the camera looks at the next phase, the feature vector, custom logic extracts a feature vector out of the new phase.
[1671.88 --> 1687.00]  And then, you run a query against MimSQL that says, give me all the records where vector dot product of feature vectors stored in the database, multiplied by the vector you just received, is, you know, between 0.9 and 1.
[1687.24 --> 1687.46]  Yeah.
[1687.66 --> 1689.58]  And that gives you all the similar faces.
[1689.92 --> 1695.78]  And because MimSQL is a distributed system, even though it's, you know, it's a brute force way of doing it, there's no index.
[1695.78 --> 1701.38]  You just go literally run the dot product against, you know, millions of faces stored in the database.
[1701.82 --> 1708.28]  But because everything is so tightly optimized, you can still run this within, you know, 50 to 100 milliseconds.
[1709.20 --> 1709.84]  Yeah, that's crazy.
[1710.34 --> 1711.78]  And that's running in production, right?
[1711.84 --> 1712.80]  It's running in production.
[1712.80 --> 1720.48]  And like I said, for both kind of government security use cases, as well as, you know, things like walking into a grocery store.
[1721.40 --> 1727.36]  And the system suggests, oh, grades that they usually buy are not in the system right now, but go buy this something else.
[1728.18 --> 1728.28]  Gotcha.
[1728.64 --> 1728.86]  Yeah.
[1729.16 --> 1734.80]  So I was curious as we were talking, and we were talking about, I guess that's a computer vision use case.
[1734.80 --> 1739.64]  And I'm thinking about, like, the types of data that are involved in machine learning and AI workloads.
[1739.64 --> 1742.24]  And we've got, you know, of course, imagery and video.
[1742.50 --> 1746.34]  And we've got a lot of natural language processing going on these days.
[1746.62 --> 1751.58]  And, you know, some of these types of data I've dealt with in SQL databases before.
[1752.04 --> 1754.94]  Of course, numbers and strings and that sort of thing.
[1755.30 --> 1762.90]  But I wouldn't typically think of, like, oh, I'm going to store this image or video or, like, an audio file or something in a database.
[1762.90 --> 1782.12]  So are you thinking that in the longer term that a good workflow around this is that you're storing the sort of feature vectors or embedded representations of maybe text or audio or maybe, like, spectrograms of audio via, like, the tensor built in or those sorts of things?
[1782.12 --> 1783.60]  Or are there other ways around that?
[1783.94 --> 1784.88]  This is a great question.
[1785.10 --> 1788.96]  To me, it's what it is now and what is it going to be as we go.
[1788.96 --> 1797.06]  So, and I will give you a very kind of product-centric answer to this question, you know, like, what would a product manager think?
[1797.62 --> 1798.94]  And they always start with a user.
[1799.16 --> 1807.12]  The user in this particular case is, again, data scientist from the training standpoint and an engineer from building an app standpoint.
[1807.12 --> 1817.44]  I think today, data scientists and with the tools that the data scientists use, it's a lot more natural to store this data in a data lake, right, basically in S3.
[1817.74 --> 1818.42]  Yeah, just fine.
[1818.76 --> 1823.92]  It's bottomless, it's files, it's cheap, and all the tool sets work out of the box.
[1824.44 --> 1830.86]  And the reason to put that data into a database is only when you get some sort of additional benefits to that.
[1830.86 --> 1833.96]  When you put structured data, the benefits are obvious.
[1834.56 --> 1841.30]  The aggregations, so it enables low latency access to that data and enables very fast aggregations and reporting.
[1841.84 --> 1850.56]  So, you can slice and dice that data in the database before pulling the data out and use your custom tools to provide reporting.
[1851.32 --> 1856.48]  For unstructured data, the only benefits that I see are governance.
[1856.48 --> 1866.04]  Database can provide that unified access layer to all your data, but it doesn't give you any compute benefits over that, right?
[1866.10 --> 1867.44]  You get a kind of kind of wash.
[1867.80 --> 1871.08]  So, that's the way we think about it right now, as well as exploring.
[1871.74 --> 1884.74]  I think what's going to happen in the future, that databases, just like MemSQL, will give you an option to access that data that's stored in the data lake and in the file system
[1884.74 --> 1895.24]  through the database API with the benefit of marrying that data and really understanding metadata, potentially building a full-text-like index against that data.
[1895.70 --> 1901.16]  So, you can marry that data with the rest of your enterprise data, which is usually relational.
[1901.88 --> 1902.00]  Gotcha.
[1902.64 --> 1912.76]  But do not yank the direct access to the file system because that's what data scientists do every day, and they would be confused.
[1912.76 --> 1913.86]  Uh-huh.
[1913.98 --> 1916.26]  If you remove that access pattern from them.
[1916.74 --> 1917.10]  Yeah.
[1917.34 --> 1923.58]  I guess on that side of things, we kind of talked a lot about the operationalizing of models.
[1923.78 --> 1932.52]  On the training side, now we're kind of talking about access to files and all of those things, and you're saying you have the one interface or the integration with Spark.
[1932.86 --> 1935.96]  You know, for me, a lot of times I store everything in S3.
[1936.06 --> 1937.70]  Like you were saying, it's very natural for me.
[1937.70 --> 1945.32]  I just like say I want this file and I'm going to use it, but there's definitely issues that come up very quickly on that front too.
[1945.32 --> 1952.52]  I know even like this morning, it's like trying to like deal with, you know, like 200 gigabytes of audio data.
[1952.76 --> 1957.22]  And like the, I was just sitting around for a while and making coffee.
[1957.22 --> 1961.52]  It's not very productive or fun to deal with those sorts of things.
[1961.52 --> 1970.02]  When you say like, I guess on the training side of things, you have maybe people that are used to the Spark interface can do that.
[1970.38 --> 1979.88]  Are there other ways with MemSQL that like, like if I want to access my audio files in S3, is there a way to do that with MemSQL outside of Spark?
[1979.98 --> 1981.96]  Are there other sorts of interfaces I can use?
[1982.24 --> 1983.38]  Not at the moment.
[1983.94 --> 1984.18]  Okay.
[1984.18 --> 1986.40]  But I will share some of the thinking, right?
[1986.66 --> 1986.84]  Yeah.
[1986.90 --> 1999.26]  So right now there's a lot of technology we're building around just relational data and providing that single pane of glass window into all your relational data.
[1999.88 --> 2001.46]  That's where we kind of the strongest.
[2001.46 --> 2009.64]  When we think about S3, we think how we can offload all the data that's not currently touched by the system into S3.
[2010.00 --> 2013.50]  We call this thing bottomless and making databases bottomless.
[2013.50 --> 2017.14]  Like if you think about Postgres, Postgres is not bottomless, right?
[2017.18 --> 2020.50]  It's bound to the amount of hard drive that you run Postgres on.
[2020.86 --> 2023.88]  But we want to make it completely bottomless and very, very cheap.
[2024.70 --> 2029.68]  And S3 is probably one of the cheapest ways to store data in the cloud.
[2029.80 --> 2034.30]  And we have things like MinIO that is one of the cheapest ways to store data on premises.
[2035.00 --> 2035.08]  Yeah.
[2035.60 --> 2039.28]  When specifically around that pattern that you described, right?
[2039.28 --> 2046.30]  I have an audio file and it's 200 gigabytes and it's a pain to go and transfer that file from one device to another.
[2046.92 --> 2051.10]  And it's a pain to download this from S3 to your local storage and all those things.
[2051.10 --> 2054.78]  So the thinking there is, again, is through integrations.
[2054.78 --> 2069.74]  If MemSQL is aware that here's the file in that particular format stored in S3 and you want to somehow either bring computation to data or you want to access to a subset of that file.
[2069.96 --> 2076.08]  And only that you want to bring into your training environment, also either running on the cloud or somewhere else.
[2076.26 --> 2078.02]  So we want to enable those things.
[2078.02 --> 2080.46]  That's where it stops so far.
[2081.02 --> 2081.10]  Yeah.
[2081.18 --> 2082.84]  That's where our thinking stops so far.
[2083.04 --> 2087.80]  We're certainly aware of the scenarios and we're aware of some of the pains that people go through.
[2088.26 --> 2092.52]  The place where we think MemSQL can add value is versioning.
[2093.42 --> 2097.60]  Because you oftentimes need to run and rerun experiments.
[2098.80 --> 2101.44]  And the model, it's not just the model.
[2101.56 --> 2103.84]  It's the model and the data that's been trained on.
[2104.36 --> 2106.96]  That's really the unit that is consistent.
[2106.96 --> 2112.00]  And if the data changed, the model might be rendered obsolete, might not be.
[2112.46 --> 2121.38]  So it just versioning makes a ton of sense from the ability to run experiments, verify experiments, share and exchange the models and data across data scientists.
[2121.94 --> 2127.96]  So I think that's where we can provide a nonlinear amount of value over time.
[2127.96 --> 2144.16]  Changelog News is the best way to keep up with the ever-changing world of software.
[2144.16 --> 2152.96]  We track, log and contextualize the coolest projects, the best practices and the biggest stories each and every week.
[2153.48 --> 2161.10]  Make changelog.com your daily destination or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[2161.78 --> 2164.64]  Join more than 15,000 enthusiastic readers.
[2164.64 --> 2167.04]  It'll cost you exactly zero dollars.
[2167.04 --> 2171.12]  And you can subscribe right now at changeball.com slash weekly.
[2171.12 --> 2188.22]  All right.
[2188.22 --> 2197.04]  Well, turning now a bit, I think, from the sort of AI and ML integrations, maybe to more sort of analytical workloads.
[2197.36 --> 2210.98]  I know that when we were talking before the show and in conversations leading up to the show, it sounds like that, you know, there's some pretty interesting things going on in terms of MemSQL being used during the COVID-19 pandemic.
[2210.98 --> 2221.12]  And, of course, there's interesting, you know, tracing work going on and all of those things that I've heard about, but I haven't really heard about how some of those things are being enabled.
[2221.32 --> 2223.76]  So I'd be curious to hear a little bit more about that.
[2224.66 --> 2224.92]  Definitely.
[2225.42 --> 2238.38]  So let's step back for a second and think about what different parts of the world and different companies and governments, what do they fundamentally want to accomplish as we go through the pandemic?
[2238.38 --> 2241.04]  The first one is, you know, simple.
[2241.32 --> 2242.88]  How do we stop the spread of the virus?
[2243.28 --> 2246.58]  And, okay, well, maybe we cannot really stop it.
[2246.78 --> 2251.00]  Or let's say we put our actions and efforts to do that.
[2251.18 --> 2258.44]  But since it's spreading and it's a matter of fact, what else can we do and how we can drive our decisions based on data?
[2259.28 --> 2260.10]  What kind of decisions?
[2260.28 --> 2262.84]  Well, could be capacity planning for ventilators.
[2262.84 --> 2263.96]  All right.
[2263.98 --> 2275.20]  We know that, you know, there's an outbreak there and we will likely have our healthcare system overrun and we need to provide extra capacity to the healthcare system.
[2275.20 --> 2276.22]  But how much capacity?
[2277.08 --> 2281.54]  So all of those questions require answers and the answers are in data.
[2282.62 --> 2284.36]  That's where data science comes in.
[2284.36 --> 2295.04]  And that's where just starting from collecting the data, putting it in one place, organizing the data and feeding this information to people who have the levers of power.
[2295.52 --> 2298.16]  Second one is like, who owns the data?
[2298.88 --> 2304.26]  We have obviously Apple and Google who own the data because they have a device.
[2304.52 --> 2308.88]  Every individual on this planet, not every, but most of them now own a smartphone.
[2308.88 --> 2325.66]  So you can tap into that stream of data and getting information about who is at which location at any point in time and then marry that location with migration patterns and marry that location with like individual tracing.
[2326.20 --> 2334.92]  You know, given that we know that this person has COVID-19, you know, who are all the people that this person came across in the past two weeks?
[2334.92 --> 2338.84]  So we can go reach out to them and say, hey, you probably want to be tested.
[2339.62 --> 2345.42]  The second entity that has that data, obviously, maybe government, but I don't know about that.
[2345.54 --> 2346.68]  But certainly telcos.
[2347.54 --> 2352.90]  Telcos have this information, maybe not as accurate because they don't have a GPS on the device.
[2353.38 --> 2357.36]  Well, actually, they do GPS on the device, but they may not be able to tap into the GPS.
[2357.90 --> 2361.64]  But they can triangulate the location based on cell towers.
[2361.64 --> 2367.74]  So we're working with some of the largest telecommunication operators here in the United States, as well as around the world.
[2367.98 --> 2373.22]  And I think the one that's public is True Digital, one of the largest telcos in Southeast Asia.
[2373.86 --> 2374.82]  And we do both.
[2375.00 --> 2381.44]  We do the migration patterns where, you know, if you go back to like, you know, March, February timeframe,
[2382.00 --> 2386.42]  we already knew that there was an outbreak in China and there was an outbreak in Italy.
[2386.42 --> 2389.36]  And we already knew how bad that was.
[2390.18 --> 2399.62]  And looking at the flights from Italy and like tracing individuals that land and then starting to see this pattern of people getting sick emerge,
[2399.78 --> 2401.94]  you can start driving decisions off of this.
[2402.34 --> 2405.76]  And you can start putting policies in place that can stop the spread.
[2405.88 --> 2407.46]  You can start doing capacity planning.
[2407.46 --> 2415.72]  You can start manufacturing masks and ventilators and distribute them into places based on the patterns that we're observing.
[2416.54 --> 2422.38]  And so that's how data management solutions are helpful to companies that have the data.
[2422.80 --> 2430.54]  And also the insights that those systems generate are useful for people with the levers of power to drive policy and to drive decisions.
[2430.54 --> 2435.80]  Yeah, Google and Apple, especially Google, has the technology, but, you know, telcos don't.
[2435.88 --> 2438.36]  And that's where we partner and give them those abilities.
[2439.44 --> 2446.46]  Yeah, it strikes me that, you know, the things you're discussing, there's definitely a lot of potential and value there.
[2446.62 --> 2452.92]  And earlier on in the episode about facial recognition and a lot of things that are possible there on a sort of large scale.
[2452.92 --> 2465.84]  And I think that as people are now in this pandemic and kind of layered on top of that, all of the climate that's in our country and around the world around, you know, injustice and policing,
[2465.84 --> 2473.18]  there's a lot of people asking really good questions about actually data management and security and privacy.
[2473.18 --> 2484.20]  And I'm curious, you know, with you being in a position to have so many conversations with different types of entities around like how they view data management,
[2484.20 --> 2492.40]  how that's changing as we think about these powerful applications of kind of large scale analytics,
[2492.40 --> 2498.68]  but also the potential concern with privacy and tracking and all of those things.
[2498.68 --> 2506.40]  I'm just curious to get some of your thoughts on how large organizations are starting to view data management and security,
[2506.40 --> 2514.44]  maybe now a little bit different than they might have in the past, given all of the things that are going on in our world.
[2514.80 --> 2516.84]  Definitely. It's a multifaceted question.
[2516.84 --> 2526.94]  It starts with data management to highlight everything that's going on and the big problems that we face
[2526.94 --> 2531.08]  and big issues that we face as a nation. How can data management help here?
[2531.68 --> 2539.44]  And I think one of the answers to that of many, right, there's so many things that would go into solving these big issues that you raised.
[2539.44 --> 2545.24]  But one of those things where data management can actually help is with data sharing and data consumption.
[2545.72 --> 2556.06]  Imagine that police data was given by the government to the whole world in the easiest way from the consumption standpoint.
[2556.06 --> 2558.32]  And it's completely real time.
[2559.04 --> 2564.84]  So if you have an arrest and that arrest by regulation has to be a part of a public record,
[2565.06 --> 2570.08]  that is in the system in 10 seconds after that arrest happened.
[2571.30 --> 2575.42]  And so that information is just live, real time for everyone's consumption.
[2575.42 --> 2579.58]  And with our vision of a single pane of glass towards all your data and all workloads,
[2579.80 --> 2587.22]  we will be able to enable those things, enable anybody to log in into our cloud service and consume that data,
[2587.46 --> 2590.54]  assuming the provider is willing to publish that data.
[2591.26 --> 2599.76]  Imagine that climate change data is available to anybody in real time, and it's live and it's easy to consume.
[2599.76 --> 2604.04]  So where we live today is a lot of data sets are public.
[2604.66 --> 2609.14]  And a lot of data sets are public, and there's regulation that forces them to be public,
[2609.14 --> 2613.30]  but they are published in a non-standard, obscure way.
[2613.56 --> 2614.74]  Yeah, they're not discoverable.
[2615.10 --> 2616.10]  They're not discoverable.
[2616.28 --> 2619.46]  So to consume that data set, it's a project.
[2619.84 --> 2624.70]  It's like going to a library or going to a court and asking for permission,
[2624.88 --> 2627.76]  and they will bring these papers and put it on the table.
[2627.76 --> 2630.50]  I'm inspired by re-watching rather Spotlight,
[2631.00 --> 2636.44]  where they got access to some sensitive data that had to buy law be public,
[2637.08 --> 2638.52]  and they had to jump through hoops.
[2639.00 --> 2640.60]  But imagine all that data is discoverable.
[2641.40 --> 2643.46]  It is at your fingertips, and that data is up to date.
[2644.24 --> 2647.96]  So you don't have to think about it like, oh, like I downloaded this from last month.
[2648.00 --> 2650.40]  What changed between last month and today?
[2650.98 --> 2651.98]  So it's just there.
[2652.22 --> 2655.00]  That can make a lot of things easier, more transparent,
[2655.00 --> 2657.92]  and we'll be living in a better world.
[2658.46 --> 2662.58]  We need to think about the implications of that from the like, you know,
[2663.00 --> 2665.12]  what if bad guys had access to this data?
[2665.38 --> 2667.26]  But that's a policy question.
[2667.34 --> 2668.68]  That's not a data management question.
[2669.12 --> 2673.42]  I think data management should enable us to live in a world like this,
[2673.46 --> 2675.14]  and the technology is already there.
[2675.14 --> 2681.44]  Yeah, and I imagine that if you have this sort of single way to interact with data
[2681.44 --> 2686.12]  that's centered around SQL, and people are familiar with that, they're able to use it.
[2686.18 --> 2688.74]  There's also, in addition to the sharing of data,
[2688.86 --> 2692.06]  there's sort of the sharing of methodologies that can happen.
[2692.48 --> 2695.48]  For example, even in our last episode that we recorded,
[2695.58 --> 2700.88]  we talked about some tooling that's out there around fairness and bias and other things.
[2700.88 --> 2704.94]  It's a little bit like you have to read a good amount of documentation.
[2705.30 --> 2707.38]  You have to figure out how to use these things.
[2707.56 --> 2710.10]  I wouldn't say it's like seamless and, you know,
[2710.28 --> 2713.02]  easily integrated into your workflow at this point.
[2713.10 --> 2715.08]  But I could imagine, for example,
[2715.20 --> 2720.74]  if a suite of tooling that is easily accessible via certain SQL workloads
[2720.74 --> 2725.64]  that look for bias in your data on certain, you know, features
[2725.64 --> 2730.00]  or highlight certain things in your data set and all of those things.
[2730.16 --> 2732.06]  And whether you're using, like you say,
[2732.12 --> 2734.94]  whether you're using TensorFlow or PyTorch or Spark or whatever,
[2735.22 --> 2737.60]  you could potentially have access to those things
[2737.60 --> 2739.64]  in terms of people sharing their methodologies
[2740.18 --> 2743.48]  because things are centralized in terms of the SQL language.
[2743.82 --> 2744.58]  Do you see that?
[2744.58 --> 2749.70]  I'm wondering, you know, what's the MemSQL community like, I guess,
[2749.76 --> 2754.94]  in terms of, you know, people working on projects built on top of MemSQL?
[2754.94 --> 2756.72]  What's that community like?
[2756.78 --> 2758.78]  And do they share certain things like that
[2758.78 --> 2762.26]  or certain things available that are maybe open source
[2762.26 --> 2766.50]  that are built on top of MemSQL that people can work on in a collaborative way?
[2766.94 --> 2769.58]  The community is on the forum.memseql.com.
[2769.86 --> 2773.36]  And then there is a community of mostly enterprise developers, actually,
[2773.44 --> 2775.66]  because that has been our focus so far
[2775.66 --> 2779.04]  that are sharing through MemSQL events and conferences.
[2779.68 --> 2783.66]  Where we're going is, you know, now that we've gotten here
[2783.66 --> 2786.90]  and we're opening up the platform more and more to the community,
[2786.90 --> 2789.14]  we're thinking a lot in terms of free
[2789.14 --> 2793.18]  and how we can make a lot of the things that got us here,
[2793.48 --> 2797.02]  you know, to got us to the 40 million run rate with 70% growth.
[2797.18 --> 2800.88]  How can we take some of that and open them up?
[2801.04 --> 2805.76]  And by opening up, providing certain set of features
[2805.76 --> 2807.52]  and capabilities to the world for free.
[2807.52 --> 2811.02]  So on our dime, you go in the cloud, you log in,
[2811.46 --> 2814.68]  and there's this free tier of stuff that you can do.
[2815.28 --> 2816.94]  That's our current thinking so far.
[2817.12 --> 2820.38]  And I'm actually going to be personally overseeing that effort here at MemSQL.
[2820.84 --> 2821.98]  Yeah, that's really exciting.
[2822.12 --> 2826.18]  I'll be excited to kind of dig in and play around with those things.
[2826.48 --> 2829.70]  One other thing that I guess is COVID related
[2829.70 --> 2832.32]  and also related to our changing world is,
[2832.32 --> 2836.38]  I guess people's just workflow and productivity during this time.
[2836.86 --> 2840.60]  I'm just curious with MemSQL growing so fast
[2840.60 --> 2843.00]  and obviously a lot changing, a lot happening.
[2843.50 --> 2845.58]  How has that been for MemSQL?
[2845.84 --> 2848.46]  And how do you see kind of, I guess,
[2848.82 --> 2852.20]  tech work from home and productivity sort of stuff
[2852.20 --> 2855.02]  moving forward from your perspective as a CEO?
[2855.90 --> 2856.12]  Yeah.
[2856.32 --> 2859.90]  So first of all, we are in the uncharted territory, right?
[2859.90 --> 2864.84]  MemSQL wasn't the company that was born remote first, right?
[2864.90 --> 2867.50]  Even though we're global and we have office in San Francisco,
[2867.74 --> 2872.14]  Seattle, Lisbon, Kiev, Ukraine, India, I think it's Bangalore,
[2872.38 --> 2874.38]  and sales offices all over the place,
[2874.62 --> 2877.78]  there's still concentration in each location
[2877.78 --> 2882.76]  and usually a particular concentration of like a component
[2882.76 --> 2885.64]  that people work on within an individual location.
[2885.92 --> 2889.10]  We weren't impacted from our performance standpoints.
[2889.10 --> 2891.28]  It's like it's been one quarter of COVID.
[2891.92 --> 2894.56]  That was basically just finished our COVID quarter.
[2894.70 --> 2896.60]  We demonstrate tremendous results.
[2896.84 --> 2899.52]  We're very happy and excited about the future.
[2899.98 --> 2902.20]  And we obviously shifted all our workflows
[2902.20 --> 2904.68]  into working from home workflows.
[2905.76 --> 2908.66]  Now, the worry that I have,
[2908.74 --> 2910.60]  and I'm being paid to be paranoid,
[2911.04 --> 2914.52]  is that it works fine so far
[2914.52 --> 2918.06]  because we are tapping into the social capital
[2918.06 --> 2921.16]  that we've built over the years, right?
[2921.48 --> 2924.66]  And a quarter of COVID is we spending that social capitals
[2924.66 --> 2928.12]  and all this like social links are established
[2928.12 --> 2931.60]  between people and they fill them while working,
[2931.84 --> 2933.26]  you know, at a particular location
[2933.26 --> 2935.66]  and looking into people in the eye,
[2936.00 --> 2937.24]  to their friends and colleagues.
[2937.50 --> 2938.46]  So that's gone, right?
[2938.46 --> 2940.56]  So every meeting is a formal meeting,
[2940.86 --> 2941.70]  if you think about it.
[2942.26 --> 2944.10]  We're missing out on hallway conversations.
[2944.72 --> 2946.68]  Yeah, I guess I hadn't thought about it that way.
[2947.16 --> 2947.58]  But it's true.
[2947.96 --> 2948.12]  Yeah.
[2948.68 --> 2950.58]  We're missing out on hallway conversations.
[2950.88 --> 2953.12]  We're missing out on, you know,
[2953.66 --> 2955.28]  grabbing coffee together
[2955.28 --> 2959.24]  and having this like nice positive experiences,
[2959.42 --> 2962.76]  brainstorming while walking towards a nice coffee shop
[2962.76 --> 2964.10]  and grabbing a latte.
[2964.10 --> 2966.88]  So I want those things to be back.
[2968.32 --> 2971.54]  So hopefully this will happen relatively soon
[2971.54 --> 2974.46]  and we'll have a dent in the social capital
[2974.46 --> 2975.30]  that we've built
[2975.30 --> 2977.94]  and then we'll kind of fill up that dent
[2977.94 --> 2979.14]  by getting back together.
[2979.72 --> 2979.82]  Yeah.
[2980.10 --> 2980.82]  So that's my hope.
[2980.96 --> 2983.46]  Obviously, we can't control that.
[2983.60 --> 2985.12]  The situation controls us a little bit.
[2985.50 --> 2986.22]  Yeah, it's interesting.
[2986.38 --> 2989.26]  I mean, so I've been working remote previous to COVID.
[2989.42 --> 2990.70]  I've been working remote for, I think,
[2991.24 --> 2992.84]  maybe about three or four years now.
[2992.84 --> 2995.28]  And I definitely get what you're saying.
[2995.52 --> 2999.12]  I've had to intentionally over time,
[2999.20 --> 3001.72]  like develop relationships with local,
[3001.72 --> 3004.02]  like data scientists or technical people
[3004.02 --> 3006.54]  that are, you know, maybe not.
[3006.78 --> 3009.24]  So they're not working at the same organization that I am.
[3009.60 --> 3012.18]  But it's a chance for me to like get together
[3012.18 --> 3014.56]  with those people and just talk about things.
[3014.56 --> 3017.40]  Because sometimes I wonder just sitting at my computer,
[3017.54 --> 3018.98]  I brainstorm a lot of things.
[3018.98 --> 3020.62]  And sometimes I wonder if I'm crazy
[3020.62 --> 3022.80]  because I'm just I'm not talking about those things
[3022.80 --> 3025.66]  to anyone except in when I'm like presenting them
[3025.66 --> 3027.24]  to my supervisor,
[3027.24 --> 3028.66]  I'm presenting them to a group
[3028.66 --> 3029.76]  and I'm supposed to, you know,
[3029.78 --> 3031.40]  sound like I know what I'm talking about,
[3031.50 --> 3032.38]  hopefully a little bit.
[3032.76 --> 3036.20]  So that, yeah, it's not that sort of informal environment.
[3036.20 --> 3038.30]  And that's very interesting observation.
[3038.30 --> 3040.84]  I hope that some of that can come back.
[3041.40 --> 3041.60]  Definitely.
[3042.14 --> 3042.44]  Yeah.
[3042.86 --> 3043.94]  As we wrap up here,
[3044.22 --> 3046.98]  I'd love to give you a chance to just let people know.
[3047.30 --> 3049.82]  Obviously, there's memsql.com.
[3049.94 --> 3052.08]  We'll have the links in the show notes.
[3052.28 --> 3056.28]  But as like a data scientist or AI sort of person,
[3056.74 --> 3059.96]  are there ways that people can kind of play around
[3059.96 --> 3062.46]  with memsql and get a little hands-on
[3062.46 --> 3064.80]  and see what it feels like
[3064.80 --> 3066.12]  and how to do certain things?
[3066.12 --> 3068.36]  Where would you recommend that they start getting onboarded?
[3069.14 --> 3069.54]  Definitely.
[3069.88 --> 3071.60]  So if you want free forever,
[3071.82 --> 3072.90]  we have our software
[3072.90 --> 3075.62]  and we give our software to up to four servers.
[3075.88 --> 3077.20]  Like I said, it's a cluster software
[3077.20 --> 3080.80]  to install whenever you want and run forever.
[3081.20 --> 3083.56]  So we call this our software free tier.
[3083.70 --> 3086.22]  It grew three times over the past year
[3086.22 --> 3087.52]  from the active user standpoint.
[3088.08 --> 3091.46]  It's basically one of the best column stores on the planet.
[3092.22 --> 3093.94]  So data is highly compressed,
[3093.94 --> 3096.50]  stored on disk, very fast reporting.
[3097.18 --> 3099.82]  Everything is updatable, transactional, system of record.
[3100.92 --> 3101.10]  All right.
[3101.40 --> 3103.48]  And so where other companies like, I don't know,
[3103.64 --> 3105.56]  that run on-premises, you know,
[3105.62 --> 3106.94]  the Verticas, the Green Plums,
[3107.38 --> 3108.62]  they want to charge you for that.
[3108.86 --> 3109.84]  You know, you get it free
[3109.84 --> 3112.46]  and you can put billions and billions of data points
[3112.46 --> 3113.02]  in the system
[3113.02 --> 3116.06]  and get very, very fast SQL response from it.
[3116.56 --> 3119.10]  In the cloud, our free tier is time-based.
[3119.10 --> 3120.94]  So I encourage people to log in
[3120.94 --> 3123.30]  and, you know, you can play around with a system
[3123.30 --> 3126.38]  that would allow you to not use any software
[3126.38 --> 3128.82]  and consume everything as a service.
[3129.14 --> 3131.36]  But because we're running it on our infrastructure,
[3131.72 --> 3134.78]  we're limiting access to free for a period of time.
[3134.92 --> 3137.78]  We'll be announcing more changes there.
[3137.90 --> 3140.80]  We'll give the system for you for free forever
[3140.80 --> 3142.22]  for a limited usage,
[3142.34 --> 3144.06]  but that hasn't come out yet.
[3144.20 --> 3145.70]  So that's something we're working on.
[3146.04 --> 3148.46]  So that would be probably the best places to start.
[3148.46 --> 3151.12]  And of course, go to forum.mimsequel.com
[3151.12 --> 3152.34]  to learn about the system.
[3153.06 --> 3153.12]  Awesome.
[3153.34 --> 3155.24]  Yeah, we'll have those links in the show notes.
[3155.36 --> 3157.88]  Really appreciate you chatting about everything today.
[3157.98 --> 3160.48]  I think our listeners will really enjoy the content
[3160.48 --> 3162.94]  and hopefully check some of these things out.
[3163.26 --> 3165.40]  And yeah, thank you so much for joining us
[3165.40 --> 3169.10]  and hope to have one of those hallway chats with you
[3169.10 --> 3172.02]  at some point when things are actually open up.
[3172.12 --> 3174.18]  Well, if you're in Silicon Valley or I'm there,
[3174.34 --> 3175.88]  I will make sure to pin you
[3175.88 --> 3177.70]  and we'll hopefully make that happen.
[3178.46 --> 3179.30]  Yeah, definitely.
[3179.66 --> 3180.56]  Yeah, thank you so much.
[3180.96 --> 3181.38]  Bye, Daniel.
[3181.80 --> 3182.08]  Bye.
[3185.46 --> 3188.68]  Thank you for listening to this episode of Practical AI.
[3189.06 --> 3190.28]  People ask us all the time.
[3190.36 --> 3191.98]  They say, hey, how can I support your work?
[3192.52 --> 3195.12]  One easy way is to leave a five-star review
[3195.12 --> 3196.12]  on Apple Podcasts.
[3197.12 --> 3199.42]  Tell folks why you listen and why they should too.
[3199.56 --> 3200.84]  It only takes about 30 seconds.
[3201.02 --> 3201.72]  And believe it or not,
[3201.86 --> 3204.40]  those ratings and reviews really do help us rank higher
[3204.40 --> 3206.34]  in AI-related search results.
[3206.34 --> 3208.94]  Practical AI is hosted by Daniel Whitenack
[3208.94 --> 3209.78]  and Chris Benson.
[3210.26 --> 3211.46]  It's produced by Jared Santo.
[3211.72 --> 3212.22]  That's me.
[3212.64 --> 3213.80]  And our music is brought to you
[3213.80 --> 3215.62]  by the one and only Breakmaster Cylinder.
[3216.14 --> 3218.08]  We are sponsored by amazing people
[3218.08 --> 3219.24]  at companies who get it.
[3219.46 --> 3221.40]  Thanks again to Fastly, Linode, and Rollbar.
[3221.86 --> 3223.14]  Did you know we have a master feed
[3223.14 --> 3224.22]  of all ChangeLog podcasts?
[3224.78 --> 3225.30]  We do.
[3225.72 --> 3227.58]  It's your one-stop shop for everything we produce.
[3227.84 --> 3228.50]  If you like this show,
[3228.56 --> 3229.50]  you'll love the ChangeLog,
[3229.62 --> 3231.04]  Brain Science, and GoTime.
[3231.04 --> 3233.26]  Check it out at changelog.com slash master
[3233.26 --> 3234.88]  or search for ChangeLog Master
[3234.88 --> 3236.24]  in your favorite podcast app.
[3236.48 --> 3237.16]  You'll find us.
[3237.54 --> 3238.34]  That's it for now.
[3238.54 --> 3239.74]  We'll talk to you again next week.
