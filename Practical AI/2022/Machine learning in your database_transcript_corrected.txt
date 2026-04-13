[0.00 → 7.80] I think there's a big disconnect between what is flashy and hype and academia or coming out of open AI.
[8.22 → 11.88] There's a lot of reinforcement learning or unsupervised applications.
[12.54 → 19.64] But in the business context that we saw across at least 20 different models and machine learning applications at Instacart,
[19.64 → 25.40] they all basically boil down to you've got some relational data, and you're trying to predict a single column.
[25.92 → 27.96] And you're going to do some joins and that's it.
[27.96 → 30.22] First thing is you pump it through linear regression.
[30.72 → 33.18] You work your way up through the scikit-learn algorithm.
[33.62 → 37.28] You hit XGBoost and your predictions are gold standard.
[37.50 → 40.08] You don't even need deep learning 90% of the time.
[50.38 → 55.76] Welcome to Practical AI, a weekly podcast making artificial intelligence practical,
[55.76 → 58.24] productive, and accessible to everyone.
[58.62 → 62.92] This is where conversations around AI, machine learning, and data science happen.
[63.26 → 68.66] Join us at practicalai.fm slash community and follow the show on Twitter.
[68.86 → 71.02] We're at practicalai.fm.
[71.24 → 75.90] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[76.10 → 77.94] Check them out at fastly.com.
[77.94 → 87.68] Welcome to another episode of Practical AI.
[88.04 → 89.66] This is Daniel Whiten ack.
[89.78 → 92.58] I'm a data scientist with SIL International.
[92.96 → 98.46] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[98.76 → 99.46] How are you doing, Chris?
[99.64 → 100.58] Doing very well, Daniel.
[100.62 → 101.24] How's it going today?
[101.66 → 102.66] It's going great.
[102.80 → 104.26] I missed you last week.
[104.26 → 111.26] I had a good conversation about various interesting topics, but it's good to have you back with me.
[111.74 → 112.14] Yeah, sorry.
[112.24 → 112.92] I missed that one.
[113.16 → 115.46] The day job got in the way on that one.
[115.72 → 116.38] So, happy to try.
[116.80 → 120.98] Yeah, the actual practical AI of your life got in the way.
[122.12 → 125.10] The practical AI of my life definitely got in the way on that one.
[125.18 → 125.98] Sorry, I missed it.
[126.08 → 127.42] I'm glad to be here today, though.
[127.46 → 128.82] I think we're going to have a great conversation.
[128.82 → 135.88] Yeah, this is definitely something that I think fits very well within our theme of practical AI.
[136.44 → 145.78] And something that I'm really excited to talk about because I think it might solve some of my own struggles in my own development life.
[146.32 → 152.92] So, today we have with us Montana and Lev, who are the founders, creators of Postgres ML.
[153.32 → 154.32] Welcome, Montana and Lev.
[155.02 → 155.26] Hi.
[155.40 → 156.40] Thanks for having us, Daniel.
[156.76 → 157.48] Thanks for having us.
[157.48 → 158.98] Yeah, definitely.
[159.42 → 165.22] So, before we get into all the details about Postgres ML, what that means and what it is,
[165.22 → 176.18] do you want to give us just maybe a little bit of a backstory about how two people sort of find their way together into, you know,
[176.30 → 181.02] connecting machine learning things into a popular database?
[182.00 → 184.16] Maybe we'll start with you, Montana.
[184.66 → 187.00] You want to give your sort of side of that?
[187.00 → 190.80] Yeah, I mean, it's kind of a long-winded story.
[191.08 → 198.18] It's definitely not the first time that, you know, I've taken a stab at machine learning infrastructure and trying to make things simpler.
[198.58 → 201.32] I joined Instacart about seven years ago.
[201.84 → 207.16] I had been a, you know, chief data scientist prior to that, and mostly it was all self-taught.
[207.26 → 208.40] I didn't really deserve the title.
[208.80 → 210.78] But at small startups, you get to pick your own.
[211.14 → 214.36] And that's what I wanted to be when I grew up, so to speak.
[214.36 → 217.72] Anyway, when I joined Instacart, it was a really exciting time.
[218.28 → 221.78] There were a couple dozen engineers in the company.
[222.08 → 231.28] We were getting large enough that we needed to move out of a monolithic Rails app into more of a distributed architecture that would be horizontally scalable.
[231.28 → 256.00] One of the first projects that I did when I started there was pulling all the product catalogue data out of the single Postgres database that we had, moving it into a new Postgres database, but then fronting that with Elasticsearch so that we would have this horizontally scalable, you know, catalogue system that could power the whole e-commerce website as we added thousands and thousands of stores to Instacart's platform.
[256.00 → 285.98] And that was really exciting.
[285.98 → 294.52] We had to sort of lead several SWAT team initiatives around the company to pull out more systems into more distributed architectures to help stitch these things together.
[294.52 → 303.94] And as our team grew, we brought on a VP of engineering, Jeremy Stanley, who's a brilliant data scientist, one of the best people that I've ever worked with.
[303.94 → 317.20] And he sort of put out a call for help of, hey, if anybody can help us get some of these models that we're building in our, on our laptops to actually impact the product somehow, we'd love to talk.
[317.20 → 328.12] And so, you know, I got to work very closely with him to help figure out how we would productionize a lot of these systems and to help build a lot of the tooling that data scientists need.
[328.54 → 330.64] You know, they're going to use Python.
[330.90 → 332.28] Should they be using Conda?
[332.80 → 334.92] What does a pip install actually look like?
[334.98 → 336.18] How do you get that into production?
[336.18 → 347.16] The whole nightmare of dependency management and lifecycle management of models when they're not just build once, but they have to be rebuilt continuously with new data as it comes in.
[347.58 → 350.68] And then you have to get the feature data to the actual model.
[350.80 → 354.12] But it can't be the data that's coming out of your snowflake warehouse.
[354.12 → 358.04] At the time, we were on Redshift, you know, because that's too slow and latent.
[358.50 → 361.16] We were learning everything and building it on the fly.
[361.28 → 362.98] And it was chaotic, but fun.
[363.32 → 369.36] Actually, we published a lot of that work in a library called Lore, which was Instacart's open source platform.
[369.36 → 377.46] You know, as the ecosystem evolved around us really quickly over the last, you know, five, six years, things have changed at break back speed.
[377.60 → 382.58] There's a new platform library company coming out every day that's doing something really cool.
[382.58 → 394.20] And so we grew that internally, but it didn't really make sense to keep a lot of the stuff that we had built because, you know, original libraries built better embedded solutions.
[394.20 → 395.82] They actually built the bridges.
[396.20 → 400.78] We could take some of our tape and glue out of the middle and things got simpler.
[400.78 → 415.66] But, you know, fast-forward another couple of years at Instacart, the original system that we had built with Elasticsearch as the heart of our data architecture, our data infrastructure, it really became like the beating heart.
[415.90 → 422.96] If anybody had any data, and this included all of our machine learning feature data, you would just shove it into the Elasticsearch document.
[422.96 → 427.08] And then anybody who needed data would just get it right out of the Elasticsearch document.
[427.26 → 430.32] And so, you know, our documents grew to several hundred fields.
[430.82 → 434.66] And many of these fields themselves were nested JSON documents.
[435.02 → 438.06] They could be tens of kilobytes of additional payload data.
[438.50 → 440.82] And so our Elastic document size blossomed.
[441.58 → 448.56] And Instacart, I think, is unique in one of its constraints, in a couple of its constraints.
[448.68 → 450.84] One is the real-time nature of the business.
[450.84 → 458.46] Instacart is not like Amazon, where if there's, you know, if it's not in stock, Amazon tells you it's not in stock, it'll be two days late.
[458.96 → 460.16] Instacart can't do that.
[460.54 → 469.62] If we don't, you know, if we say, sorry, we're not going to be there in 45 minutes, we don't have your entrée that you're planning to cook for your family, your family is going to go hungry.
[470.08 → 472.78] And that's going to be a really, terrible customer experience.
[472.78 → 477.18] And so everything at Instacart is built from the product, from the machine learning.
[477.18 → 480.44] It has to be rapid and online and responsive.
[480.72 → 485.56] It can't be, you know, an offline 24-hour batch job that we get around too eventually.
[486.34 → 490.86] And so I think that is a really challenging technology problem.
[491.12 → 493.88] It's a really challenging business and product problem as well.
[494.22 → 504.92] At the same time, Instacart is a platform for hundreds of different grocers throughout the country that have tens of thousands of stores, all that have different inventory.
[504.92 → 515.38] So it's true that we have, you know, one product, one box of Captain Crunch cereal, you know, it has an image, it has nutrition facts, it has this universally true data about it.
[515.80 → 520.70] But then it also has little facets of data that are specific to every single store.
[520.78 → 522.94] Like what is it actually being sold for in that store?
[523.20 → 525.12] Is there a manager special that day?
[525.48 → 529.12] Is it in stock on the shelves or did it just, did they just sell the last box?
[529.12 → 534.64] And so, you know, if you think about this from a data architecture perspective, it's a pretty classic, you have two tables.
[535.04 → 537.10] One is your products, one is your offerings.
[537.38 → 539.10] You join those two tables together.
[539.64 → 541.92] You denormalize that data into Elasticsearch.
[542.46 → 542.92] Easy.
[543.62 → 546.28] Except, you know, we actually have a million products.
[546.56 → 547.78] We have 10,000 stores.
[548.24 → 550.28] You multiply that together, you get 10 billion.
[550.28 → 555.68] And so all of a sudden, this is an incredibly large Elasticsearch cluster.
[556.28 → 563.78] And it's growing very, very rapidly because, you know, Instacart was at the time expanding into whole new verticals beyond grocery.
[564.22 → 565.90] It was basically all retail.
[566.54 → 571.52] And it's like, oh, now we have like this whole other dimension, and we want to join whole other things.
[571.52 → 573.34] And how are we going to scale the cluster?
[573.46 → 581.24] And I remember seeing a graph plotted of like our Elasticsearch capacity increase per node added to the cluster.
[581.62 → 583.56] There were some diminishing returns there.
[583.64 → 587.44] You don't get perfectly linear scaling when you add nodes to a cluster.
[587.86 → 591.38] At the same time, there's, well, that curve is asymptotic and flattening.
[591.76 → 595.78] There's another curve that's coming up exponentially, which is Instacart's growth rate,
[595.78 → 601.30] both in terms of rights to Elasticsearch and times of timely ingestion to the system.
[601.82 → 612.48] And this is another thing that, you know, Instacart had contractually agreed to providing updates to the website on behalf of retailers in very short amounts of time.
[612.84 → 619.46] So one of the things that I've heard that, you know, Walmart, for instance, does is they have a green-blue deployment for Elasticsearch, right?
[619.62 → 624.28] And they will spend 24 hours filling up their green cluster with updates.
[624.28 → 626.64] They'll flop over to it, all traffic gets that.
[626.92 → 630.56] And then for the next 24 hours, they'll, you know, refresh their blue cluster.
[630.78 → 632.06] And then they'll flip over to it.
[632.40 → 637.08] And so you can just rebuild your cluster every night, flip back and forth between the two.
[637.44 → 644.48] And that way you avoid like a lot of the incremental update penalties you get in a Lucene index in this inverted index world.
[644.86 → 650.84] That's not a strategy, for example, that Instacart can employ because of the tight time constraints.
[650.84 → 662.94] And so we were all sitting around kind of pulling our hair out, trying to figure out how we were going to out scale the business with our technology and getting a little desperate, honestly.
[663.48 → 666.18] Like I think Postgres was not the first idea.
[666.18 → 672.04] But eventually, we did decide that fundamentally, this is a join problem.
[672.04 → 681.90] If we could do the join at read time rather than index time, then that would potentially eliminate a huge amount of work.
[681.90 → 688.16] Because many of the documents that we were joining and indexing were actually never read before they were re-indexed again.
[688.74 → 697.14] And so we could actually, by not doing those useless amounts of work, we could reduce the amount of work in the system substantially.
[697.92 → 702.54] And so we built a prototype for this system of what would it look like.
[702.88 → 707.56] You know, people have been sharding Postgres for decades, something that people know how to do.
[707.56 → 709.38] It's a little finicky, you have to get it right.
[709.38 → 718.48] But even more recently with things like Timescale DB and Cites data, they make sharding a lot more manageable, a lot more tolerable.
[719.04 → 721.48] And so we started looking at some of those options.
[722.08 → 723.62] And we started to look at the...
[723.62 → 727.56] Postgres also has these full-text search capabilities built into it.
[728.20 → 734.86] They don't nearly have the bells and whistles of Elastic, but the basics are there.
[734.86 → 742.42] And so, you know, I started talking with our NLP guys and our search engineering team and saying, like, what are we actually using in Elastic?
[742.78 → 746.00] What machine learning functionality in Elastic do you have?
[746.12 → 749.02] And they're like, oh, we tried, but it fell over, so we couldn't do it.
[749.10 → 750.70] We couldn't actually use a lot of...
[750.70 → 751.90] It's too much load on the cluster.
[752.04 → 752.88] It's already on fire.
[753.52 → 756.52] And so what we learned is that most things happen at the application layer.
[756.52 → 767.78] And most things are like joins between various microsystem data stores, feature stores that had gotten kicked out of Elasticsearch because they were creating too much load on the heart of the company.
[768.16 → 771.20] And then we would join those all at request time at the application layer.
[771.76 → 774.64] Sometimes that would take eight seconds for our P90.
[775.14 → 776.30] It could be quite slow.
[776.30 → 780.56] And sometimes what we would find is like we would do these eight seconds of work.
[781.10 → 785.98] And then at the last step, we would find everything, all of our high candidate, high quality results were out of stock.
[786.14 → 791.20] So we would have nothing to show because we had to implement several constraint layers upstream.
[791.76 → 798.18] When we really got into the nature of the system that we had built, it was this distributed machine learning, beautiful beast.
[798.18 → 800.88] It was not a pretty picture.
[801.00 → 802.32] It's a very complicated picture.
[803.06 → 807.60] And so we just said, well, we don't really have any other options.
[807.84 → 809.48] We're going to try to do this in Postgres.
[809.62 → 810.62] We stood up our prototype.
[810.86 → 811.66] We had it running.
[812.14 → 817.64] We were shadow testing its search results against Elasticsearch, what we were getting back and forth.
[818.08 → 824.38] We were finding lots of data ingestion bugs, bugs that had been in our data pipeline going into Elasticsearch for years.
[824.38 → 829.26] We discovered several of those because we had to rebuild the pipeline in parallel for Postgres.
[829.38 → 830.60] It was a totally different pipeline.
[831.38 → 834.42] Obviously, we found several bugs in our Postgres implementation as well.
[834.58 → 837.98] When you're doing a second system rewrite, that's never a fun thing.
[838.32 → 840.82] I don't typically recommend people go that route.
[841.44 → 846.62] But things were looking okay until the pandemic started.
[847.28 → 853.84] You know, we had plotted out the intersection of those two curves looking something like a year out that we would have to figure this.
[853.84 → 856.70] This thing out and to kind of experiment and prototype.
[857.44 → 862.08] And we went through that year of growth in about a week, the first week of the pandemic.
[862.80 → 865.44] And I remember getting page the next Sunday.
[865.56 → 867.82] Everybody does their grocery shopping on Sunday morning.
[868.24 → 871.58] So if there's a new load issue, it's going to be Sunday morning when we get page.
[871.68 → 872.86] And so I remember getting page.
[873.42 → 877.50] And Elasticsearch was, you know, timing out 30-second requests.
[877.50 → 880.20] We were, you know, we had stopped indexing.
[880.32 → 887.56] So we were, you know, in danger of not meeting SLAs unless we could get indexing going again when traffic would go away.
[887.80 → 889.36] We did all kinds of things.
[889.46 → 893.02] You know, we thought about putting up a stop sign on the website and saying,
[893.34 → 894.56] sorry, Instacart is full.
[894.68 → 896.10] You have to come back another time.
[896.76 → 898.94] Luckily, we never had to actually deploy that.
[899.14 → 902.88] Luckily, we were able to scale our way out of the pandemic.
[902.88 → 905.18] But it was a lot of work.
[905.52 → 911.46] And so while we were in the middle of this incident, we said, well, we've got this other cluster over here.
[911.66 → 916.60] We think that the results are about the same as the cluster that we're, you know, using.
[916.88 → 921.26] That's kind of dead right now because it's just timing out 100% load.
[921.48 → 926.12] So we just flipped the switch, put all the load against Postgres and started using it.
[926.38 → 931.64] Of course, it immediately went to 100% CPU utilization and also caught on fire.
[931.64 → 938.00] But we were able to find a few missing indexes for some long tail queries that we hadn't really optimized.
[938.62 → 945.90] And within a couple of hours, we got that cluster to a point where we could, you know, actually serve traffic again.
[946.68 → 948.64] And so that was really exciting.
[949.04 → 953.56] To really get the system bolted down took a couple of months after that.
[953.56 → 960.64] But for the most part, we had sort of shifted what was the primary system and what was the secondary system.
[960.76 → 966.08] Elasticsearch from that point going forward was really the backup to this new system that we had.
[966.14 → 970.84] And we had a couple of incidents with the new system as we started throwing more and more data into it.
[970.88 → 977.56] Because after we did the original optimizations, we got down to like 4% CPU usage or something in the Postgres cluster.
[977.56 → 982.26] And it was vastly undersealed compared to our Elasticsearch cluster.
[982.40 → 983.74] I mean, it was just tiny compared to it.
[983.88 → 985.34] It was really amazing.
[985.84 → 990.56] But at the same time, I mentioned all these other feature stores, model stores, everything else that we had.
[991.00 → 996.54] All of those, you know, whether they were Regis or whether they were Postgres or Cassandra, those were all melting down as well.
[997.00 → 998.98] Those were not horizontally scalable systems.
[998.98 → 1009.12] We learned a lot about scaling every system we had, whether that was RabbitMQ or Regis or if you can name a database, we probably tried it at some point at Instacart.
[1009.46 → 1010.74] So we had lots of fun.
[1011.20 → 1023.04] But our solution in this case was basically like figure out which database has the most CPU usage, pull all the data out of it and dump it into this new horizontally scalable Postgres cluster that we have.
[1023.04 → 1026.06] And so we just did that over and over again.
[1026.40 → 1032.36] And we barely kept ahead of, you know, our doubling week-over-week growth curve for the next eight weeks.
[1032.48 → 1036.26] And like I mentioned, sometimes we missed optimizations.
[1036.68 → 1043.58] We didn't really have the time to vet and test the system that we were building like we should have or could have.
[1043.72 → 1048.52] But I think that we did the best that we could with the resources that we had.
[1048.52 → 1058.76] And we spent, you know, at least a year after that iterating, adding more, really unlocking some new machine learning for our search team that we could now do.
[1059.28 → 1062.20] And we didn't get as far as I really wanted, though.
[1062.74 → 1069.08] Because at the time there was is a library called Mad lib, which is an Apache Foundation project.
[1069.26 → 1071.14] It's, I think, 10 years old.
[1071.56 → 1072.60] It's been going for a while.
[1073.00 → 1075.02] But there were some constraints at the time.
[1075.02 → 1077.70] They were locked to a specific older version of TensorFlow.
[1078.04 → 1079.72] I think my memory is fuzzy.
[1080.04 → 1081.38] I didn't get a lot of sleep back then.
[1081.86 → 1091.68] But we weren't able to actually take a lot of our deep learning models and put them into Mad lib and run them inside the database to eliminate some of the microservices.
[1092.06 → 1097.16] So we actually kept quite a bit of the microservice architecture and kept building around that.
[1097.32 → 1102.62] But it kind of bothered me because we were able to clean up so much of the distributed system.
[1102.62 → 1104.04] I felt good about it.
[1104.18 → 1108.18] The system that we ended up with was much better than the system that we started with.
[1108.76 → 1115.14] And it was kind of full circle for me coming from like, you know, I joined Instacart, and I was all about distributing everything.
[1115.64 → 1122.26] But by the end, I was all about pulling everything back into one fairly monolithic system.
[1122.26 → 1137.28] And so that, I think, was kind of eye-opening for me about the complexity, both organizational but also technological, that these systems can develop and how powerful it can be if you can simplify the system.
[1137.48 → 1143.68] For example, you know, I think when we were on the Elasticsearch pipeline, we had a dedicated infrastructure team.
[1143.82 → 1146.18] We had a dedicated catalogue team just to the pipeline.
[1146.18 → 1152.18] We have a dedicated search team, dedicated machine learning, engineering, all of those resources, you know.
[1152.56 → 1163.12] And we had, you know, upstream of that catalogue data acquisition specialists that would get new kinds of data to do new kinds of products and services or add new features to the website.
[1163.12 → 1172.04] But it took multiple quarters of planning and execution from the like, you can set a few product managers that are around the room.
[1172.18 → 1175.76] They conceptualize like, hey, we want to add this feature to the website.
[1176.10 → 1178.06] They're like, okay, we'll go source the data.
[1178.24 → 1179.58] We'll get the data into the pipeline.
[1179.72 → 1181.22] We'll adjust it into Elasticsearch.
[1181.60 → 1184.12] The search team will start using it, and then they'll display it.
[1184.22 → 1186.52] And, you know, they'll start work this quarter.
[1186.90 → 1189.32] The search team will get to the next quarter.
[1189.82 → 1192.40] Oh, wait, we don't have the data in the right format.
[1192.40 → 1195.76] Let's circle back for another quarter of this whole process.
[1196.00 → 1198.74] And so it was really, really problematic.
[1222.40 → 1241.22] So, Montana, fascinating to hear about this sort of, like, progression at Instacart, the sort of scale up and the issues, especially around the pandemic and having to respond in that way and how you sort of, like, that path, that journey led you into Postgres.
[1241.22 → 1256.10] Before we sort of, like, continue into, like, the Postgres ML story, I'm curious, like, Lev, were you experiencing this also with Montana or were you coming from, like, a different side of things?
[1256.10 → 1268.64] Or how, like, how did you experience your sort of, like, journey into, like, thinking more deeply about Postgres and where it intersects with data science, machine learning, all of these things?
[1268.64 → 1274.42] I'm laughing because, you know, that system that Montana is talking about, I might have been the guy who built it.
[1274.42 → 1279.56] The Elastic search system or the Postgres?
[1279.76 → 1280.10] The Postgres system.
[1280.72 → 1282.84] I came in as a true believer.
[1283.04 → 1285.58] I was told that Elastic was wrong and Postgres was right.
[1285.80 → 1286.84] And I'm like, sounds good.
[1286.92 → 1287.70] Let's build Postgres.
[1288.14 → 1291.10] And it's not like we built it on RDS or anything.
[1291.16 → 1293.02] We actually built it straight up on EC2.
[1293.02 → 1296.84] So I had to learn things like, ooh, how do I install Postgres or own Ubuntu?
[1297.00 → 1297.74] Should I pick Ubuntu?
[1297.88 → 1299.02] What kernel version do I need?
[1299.52 → 1303.50] And it wasn't because, you know, we kind of like, oh, yeah, self-hosting is the way.
[1303.62 → 1307.50] It's because RDS was too slow to power our workloads.
[1307.76 → 1313.12] If you have I run on, if you're on your databases on RDS, you know that the disks are, they're network disks, right?
[1313.52 → 1317.16] So latency is at least, like, you know, 10 milliseconds depending on the day.
[1317.40 → 1320.08] You know, IO2 is probably a little bit better, but still not quite there.
[1320.08 → 1324.68] And RDS, for those that don't know, is a managed database service, right?
[1324.98 → 1325.72] Yeah, that's the one.
[1325.80 → 1328.04] Yeah, the AWS relational database service.
[1328.24 → 1330.36] They have Postgres, MySQL, all the fun ones.
[1331.12 → 1340.56] Anyway, so instead we picked SSDs, like the raw, you know, NVMe, the cool ones that could do like four, five, six, ten times more workload than the network drives.
[1340.76 → 1342.64] And that's when Postgres really came alive.
[1342.84 → 1348.64] And all of a sudden I could scan like a 100 gigabyte table in like 30 seconds.
[1348.64 → 1350.76] And I'm like, oh, wait, so this thing actually scales?
[1352.12 → 1356.52] Because before we just spent like cutting these tables, partitioning them, making them as small as possible.
[1356.52 → 1358.00] And I'm like, wait, but why?
[1358.20 → 1361.54] I could just read this whole thing from a disk at like two gigabytes a second.
[1361.62 → 1362.64] Like, what's the big deal?
[1363.88 → 1365.52] You know, technology came a long way.
[1366.06 → 1369.98] Yeah, so, you know, those Sundays that Montana talked about, he was getting paged.
[1370.04 → 1371.42] I was also getting paged.
[1371.42 → 1377.08] You know, I worked at Instacart Infrastructure for about three years, cumulatively.
[1377.58 → 1378.86] Well, I started as an app engineer.
[1379.16 → 1384.86] I came in, and I was supposed to build like widgets and like the checkout page that we might have used at some point.
[1384.86 → 1388.86] But, you know, like a week later, they told me like, hey, we need to fix our Postgres setup.
[1389.08 → 1390.32] Our databases are falling over.
[1390.70 → 1391.98] I'm like, all right, sounds good.
[1392.08 → 1393.78] I think I've heard of Postgres before.
[1393.98 → 1395.28] Let's see what I can do.
[1395.28 → 1398.44] And then I wasn't an app engineer anymore.
[1399.88 → 1401.62] I kind of learned that on the fly.
[1401.70 → 1404.50] I started like memorizing the documentation and everything.
[1404.50 → 1412.98] And then a year later, you know, I got sat down in a room and Montana was presenting his new Elasticsearch replacement.
[1413.16 → 1415.32] And I'm like, whoa, we're going to sharp this ourselves?
[1415.46 → 1416.72] Is that what's going on?
[1416.80 → 1420.24] I think I might be able to do that, but okay.
[1420.24 → 1425.72] And yeah, we spent quite some time building that thing.
[1426.42 → 1433.10] So as you get into Postgres ML and like, this is a great story you guys are telling together.
[1433.28 → 1434.60] I'm really into it.
[1434.90 → 1439.06] But like, as you're looking at this, how does that lead down to that?
[1439.16 → 1450.22] You know, without losing the thread, where are you going that's going to arrive at that moment where you're starting to really think about, you know, what you need to be doing next in that capacity?
[1451.00 → 1459.06] Yeah, I think Lev should tell you about PG Cat, and I'll tell you about Postgres ML because I think there are two different pieces of the puzzle.
[1459.66 → 1466.06] But to answer your question, you know, like I mentioned, we weren't able to get a lot of deep learning models into Postgres.
[1466.70 → 1473.68] And so because we couldn't get that, we didn't even really start with all the XGBoost models or even simpler models that we were running.
[1473.68 → 1482.22] And I think there's a big disconnect between what is flashy and hype and academia or, you know, coming out of open AI.
[1482.60 → 1487.92] Like there's a lot of reinforcement learning or unsupervised applications or whatever.
[1487.92 → 1501.38] But in the business context that we saw, you know, across at least 20 different models and machine learning applications at Instacart, they all basically boiled down to you've got some relational data, and you're trying to predict a single column.
[1501.38 → 1503.94] And you're going to do some joins and that's it.
[1504.24 → 1506.30] First thing is you pump it through linear regression.
[1506.82 → 1509.40] You work your way up through the sidekick learn algorithms.
[1509.68 → 1513.50] You hit XGBoost and your predictions are, you know, gold standard.
[1513.72 → 1517.26] You don't even need machine deep learning 90% of the time.
[1517.26 → 1527.04] And so thinking through like the convoluted data architectures and data engineering and everything else that we had to do to get features to models.
[1527.24 → 1529.92] I was like, well, the data is just, it's in Postgres right there.
[1530.04 → 1540.98] You can just try to join, and you can just do a select, and you don't even need to bring a lot of it to the application layer if you can actually do your ranking or whatever it is that you're trying to do.
[1541.10 → 1545.02] You know, ranking is obviously a big application of machine learning.
[1545.02 → 1551.70] You need to know what your popular things are, your trending things are, your relevant things are, your possible alternatives to this thing are.
[1551.86 → 1558.70] Like there's all these different ways that things are associated to things in this high dimensional space that data scientists love.
[1559.22 → 1569.98] And so being able to pull things only the most relevant of those dimensions out of the database, the application layer, which is actually a really expensive operation compared to things like deep learning.
[1570.32 → 1572.28] People think deep learning inference is expensive.
[1572.28 → 1592.92] It's really not relative to like taking thousands of rows out of a database, serializing them, sending them over a copper wire that's multiple feet long, you know, reading them into a JSON blob on the other side in some dynamic language that's allocating a ton of memory to do all of these operations so that you can operate on this in Python or Ruby or whatever it is.
[1592.92 → 1595.78] And that's where actually most of the latency in the system comes from.
[1596.08 → 1598.10] It's not from the models themselves.
[1598.24 → 1601.26] The models themselves are like highly optimized C code.
[1601.92 → 1607.24] Sure, it may have millions or even billions of parameters, but it's relatively fast and optimal.
[1607.78 → 1613.66] And so I was just thinking like, what if we could cut all of that complexity, all of that latency out and keep things in the data layer?
[1613.66 → 1618.74] And I was talking to Lev about this, and I was like, I'm going to go on vacation, but when I get back, I'm going to start on this project.
[1618.92 → 1624.38] And so, you know, on vacation on day one, I see Lev emails me and he's got a new commit.
[1624.48 → 1626.52] He's like, I've got deep learning in Postgres.
[1627.54 → 1632.26] And Lev is really phenomenal this way in that he's very competitive.
[1632.70 → 1635.46] If you tell him about something, he'll try to beat you at it.
[1635.46 → 1638.92] We all have a Lev in our life, you know?
[1639.08 → 1642.84] No, it's fantastic to be challenged by somebody that way.
[1643.24 → 1644.42] I really appreciate it.
[1644.64 → 1646.52] It's a lot of fun working with Lev.
[1646.52 → 1656.00] But I think that, you know, that was sort of my itch, which I would consider, you know, my thesis defence at Instacart was like, can we do this with Postgres?
[1656.36 → 1657.80] Can we actually go all the way?
[1658.16 → 1663.76] And can we get to a data architecture that doesn't really involve any ETL or ELT, whichever you prefer?
[1663.76 → 1665.30] It's just the database.
[1665.88 → 1668.90] And the data just sits there until you know that you want it.
[1669.44 → 1672.34] And that was what really drove the creation of Postgres ML.
[1673.00 → 1677.32] But I think Lev had a different itch with the system that we built.
[1677.50 → 1681.46] And so he actually went off and built another solution that he should tell you about.
[1681.88 → 1685.62] Shame on you for going on vacation, and he beat you to it.
[1687.02 → 1693.32] Yeah, I guess it's a good segue into sharding and load balancing and running Postgres at scale.
[1693.32 → 1697.54] Well, it's funny because Postgres itself doesn't have any sharding capabilities.
[1697.96 → 1701.62] Like you can just spin up a single primary and that's all you get.
[1701.74 → 1707.10] You can have some partitions, you know, you can have some foreign tables or FTWs, like foreign data wrappers, if you ever heard about that.
[1707.82 → 1710.28] But by the end of that sentence, you're like, I don't know.
[1710.62 → 1712.22] What are you talking about?
[1712.96 → 1714.14] Please just do this for me.
[1714.22 → 1714.46] Okay.
[1714.54 → 1715.46] And I'm like, yeah, sure.
[1715.50 → 1716.34] I can do this for you.
[1717.06 → 1723.14] So I rewrote, I took the sharding logic that we kind of invented at Instacart, but, you know, it kind of already existed.
[1723.30 → 1725.20] You know, you always reinvent the same thing over and over.
[1725.52 → 1728.32] You put it into like the proxy, like a pooler essentially.
[1728.66 → 1732.64] And you put that in front of your database and then your clients, they're just connecting to Postgres.
[1732.82 → 1733.74] They don't know about sharding.
[1733.88 → 1734.70] They don't know about replicas.
[1734.80 → 1735.68] They don't know about load balancing.
[1735.82 → 1737.02] They don't know any of failover.
[1737.28 → 1738.36] They don't know anything about it.
[1738.36 → 1741.40] And they just get the data, whatever they want.
[1741.60 → 1743.76] I called it PG Cat because I'm obsessed with cats.
[1744.16 → 1745.34] I just said that on the internet.
[1745.56 → 1747.96] So about 50% of people are like, this guy is amazing.
[1748.52 → 1750.68] The other 50% are like, dogs are the best.
[1751.26 → 1751.98] I hate this guy.
[1752.28 → 1753.24] Unsubscribe, unsubscribe.
[1756.24 → 1757.86] That's a good number I hear.
[1758.28 → 1760.14] Hey, at least you get the 50%.
[1760.14 → 1760.86] Yeah.
[1760.94 → 1763.06] I mean, it's a fun project that I like.
[1763.06 → 1768.24] We kind of wrote at the application layer, like all the try-catch Ruby Python logic to
[1768.24 → 1769.88] talk to five different replicas.
[1770.04 → 1771.58] We just implemented it at the infer layer.
[1771.76 → 1775.98] And now the database is magically sharded, magically load balanced, magically highly available.
[1776.66 → 1779.28] It's everything that we wanted but couldn't have.
[1779.70 → 1779.88] Yeah.
[1780.44 → 1780.92] I don't know.
[1781.44 → 1782.18] I liked it.
[1782.54 → 1782.68] Yeah.
[1783.06 → 1786.80] So the two sides, you sort of have the PG Cat stuff.
[1786.80 → 1793.38] And then you have like, oh, the idea, can we run some of this sort of like pull thousands
[1793.38 → 1799.32] of rows out, do some sort of like ranking or search or ML operation on them.
[1799.36 → 1802.04] There's sort of like these ideas floating around.
[1802.72 → 1807.84] Is Postgres ML, is it sort of leveraging both of those things?
[1808.22 → 1812.40] And that sort of like is some of what makes it what it is?
[1812.40 → 1817.46] Or how did those things influence how you think about like Postgres ML and like what it is?
[1817.94 → 1821.00] Yeah, I think we're very early with Postgres ML.
[1821.14 → 1824.18] Like I think we only released it a couple of months ago.
[1824.38 → 1827.74] We started working on it maybe 10 weeks ago or something.
[1828.16 → 1832.60] So it's still what we would consider, you know, public alpha, basically.
[1832.82 → 1836.42] Like the point was like, does anybody care about doing machine learning in Postgres?
[1836.58 → 1839.12] Is anybody interested in this idea at all?
[1839.36 → 1840.36] Or are we crazy?
[1840.36 → 1845.58] Because I have a lot of qualms about putting more load on the primary data store.
[1845.98 → 1850.88] That is something that I think anytime you can avoid doing that, that's probably a good thing.
[1850.98 → 1853.86] At least that's my naive take on it.
[1854.14 → 1860.26] But when I start seeing Lev's work with PG Cat and sharding and pooling and failover and load balancing,
[1860.70 → 1867.08] then I think, well, actually, maybe the simplicity that you can get from having a single data store
[1867.08 → 1871.78] instead of every database technology in the world and the expertise that you can build
[1871.78 → 1877.64] and the muscle that you can build around that single technology will lead you to a much better place in the end.
[1878.18 → 1883.38] So if we, Postgres ML doesn't combine any of the PG Cat stuff right now.
[1883.46 → 1884.78] These are two separate pieces.
[1884.78 → 1893.42] But we're actually working to put them together in an online service offering that we've started a company together so that we could go full-time.
[1893.56 → 1899.90] I know Chris was mentioning he's got those real life obligations that sometimes get in the way of all the fun stuff that we're doing.
[1900.68 → 1906.54] And so Lev and I also have real life obligations that get in the way of these fun projects that we love talking about.
[1906.54 → 1914.60] So quit those, and we're going full-time on a new venture together to put these two pieces together
[1914.60 → 1919.96] and really get to Postgres at scale with machine learning capabilities.
[1920.22 → 1924.60] That's the goal for what we want to build and offer and make it easy for the other people.
[1925.16 → 1929.22] So to clarify, you've moved on from Instacart, if I'm understanding that correctly.
[1929.64 → 1930.02] That's correct.
[1930.04 → 1930.46] That's right.
[1930.74 → 1931.00] Okay.
[1931.00 → 1931.06] Okay.
[1936.54 → 1964.76] I'm sort of curious, I think, about like when someone comes to Postgres ML, like I know it's sort of new, it's beta.
[1964.76 → 1967.46] What is the experience?
[1967.74 → 1973.98] Could you just sort of describe like what is the experience like of doing ML in Postgres?
[1974.22 → 1980.46] Maybe like running through, maybe you could give an example of sort of like a training type of thing.
[1980.80 → 1987.96] And then maybe like a deployment or inferencing type of workflow, just to give people a sense of like,
[1987.96 → 1997.32] hey, I might know how to run SQL against Postgres, but what does it mean to, quote, do machine learning and Postgres?
[1998.02 → 1998.20] Yeah.
[1998.30 → 2003.88] So, you know, Python is really, I think, the dominant language in the machine learning ecosystem these days.
[2003.88 → 2012.96] And so what Postgres ML is right now in this sort of alpha public release is a wrapper around all of your favourite Python libraries.
[2013.48 → 2023.12] We just define a little SQL or PL Python function that calls out to scikit-learn or calls out to XGBoost or whatever your favourite Python library is.
[2023.12 → 2038.50] And when we define these Postgres functions to take in all the parameters that you could possibly pass to scikit-learn and just forward them on so that you get all the sci kit functionality for training these models.
[2038.64 → 2041.72] And so in Postgres ML, training is a single function call.
[2041.72 → 2047.80] So you would, you know, select star from Postgres ML dot train, and then you pass it a few arguments.
[2047.96 → 2051.04] You pass it, you know, the name of the algorithm that you want to use.
[2051.38 → 2056.22] And that, you know, that's either linear regression or that's XGBoost or anything on the menu.
[2056.44 → 2062.66] I think this is actually a fascinating rabbit trail to go down is why I think that's the right approach.
[2062.66 → 2072.12] I think most business uses of ML can safely treat ML as a black box that they put inputs in, and they get inputs out.
[2072.44 → 2079.80] Now, you need to be very careful about the outputs of that black box, and you need to watch it closely and make sure that it's doing the correct thing for your business.
[2080.30 → 2084.58] But you don't need to understand the math behind how these algorithms actually work.
[2085.04 → 2090.54] Compute is cheap enough now that you can train your data with 50 different algorithms and just pick the best.
[2090.54 → 2092.74] Like, you don't need to have this.
[2093.10 → 2098.90] I've seen a lot of theorizing from a lot of people about why a model is doing what it's doing and how they're going to tweak something.
[2099.08 → 2102.74] And, you know, it's pretty much a crap shoot of whether that actually makes it any better or not.
[2103.04 → 2105.82] It's always better to just test a bunch of different stuff.
[2106.40 → 2111.10] And so that's another feature of Postgres ML is that we have, you know, hyperparameter search.
[2111.50 → 2115.96] You just feed it a bunch of, in this train, you feed it a bunch of different configurations that you want.
[2116.16 → 2118.50] And then it will build all the models for you.
[2118.50 → 2123.32] And then you can just compare which one is the best, and that will be the one that's automatically deployed in your database.
[2123.92 → 2128.70] So people always focus on the math behind the algorithms because I think those are intellectually interesting.
[2129.28 → 2135.14] But what they don't focus on, but which is actually a lot of data science work, is the curation of the data.
[2135.66 → 2143.22] And so that data cleaning, that data curation, the feature engineering work the data scientists do day to day, Postgres is fantastic at that.
[2143.48 → 2144.62] You have SQL.
[2144.82 → 2147.60] You can manipulate your data in just about any way you want.
[2147.60 → 2155.72] No, it may not have all the typical functions that data scientists might be used to for treating data in particular ways.
[2155.82 → 2157.06] Like if you want to impute a value.
[2157.44 → 2160.86] Actually, Postgres can coalesce nulls to anything you want.
[2161.24 → 2162.54] It can coalesce it to an average.
[2162.68 → 2166.34] It can coalesce it to a minimum, a max, or some random value.
[2166.34 → 2172.48] As you're telling me that, could you also walk us through a little bit of like what a simple workflow would look like?
[2172.68 → 2174.06] I wasn't trying to cut you off.
[2174.14 → 2181.14] I was wanting to see if you would add that in just so people kind of know what like I start here, and I go, bam, bam, bam.
[2181.32 → 2183.82] And I end up here with that output.
[2183.82 → 2194.50] And just to give me a sense, because as someone who hasn't used it yet, I'm really curious about this because so many of us in the development world, aside from just the data science world, are using Postgres every day.
[2194.62 → 2196.32] So I'm pretty excited about that.
[2196.36 → 2198.44] If you could just kind of fit that into what you're telling me there.
[2198.76 → 2199.34] Yeah, absolutely.
[2199.34 → 2204.30] So you start with getting your data into a relation, and that's either a table or a view.
[2204.92 → 2206.54] And this is going to be your training data.
[2207.16 → 2215.98] So however you want to create that table or create that view, whether you want it to be a view with a bunch of joins out to your application tables, that's fine.
[2216.20 → 2225.40] If you want to, you know, suck the data up into the application, munch it with a bunch of Python, dump it back out into your feature table in Postgres, that's fine too.
[2225.40 → 2233.46] But that is, you know, I think the bread and butter of a lot of data science is that kind of feature engineering, creating that table.
[2233.46 → 2245.70] I think it's really magical if you can create it with a view, because if you can create the view of your training data, you should be able to reuse the view for your inference calls.
[2246.20 → 2248.30] And you can get the same features out.
[2248.66 → 2254.64] You have to be very careful in an application database where the application is updating rows.
[2254.64 → 2266.16] And so you have to make sure that you're not training with, you know, a false view of the past, but you actually have the true append-only log somewhere that you can train from what the values were at the time.
[2266.62 → 2275.72] But if you can get that, and if you can build your OLTP database in such a way that it handles that, then you can get this very magical, I have this view.
[2276.14 → 2282.42] I pass that view to my training function along with an algorithm name, whatever hyperparameters I want to pass to that algorithm.
[2282.42 → 2290.38] What happens is, you know, Postgres ML calls out to Python, runs the whole pipeline, you end up with a trained model.
[2290.70 → 2293.94] It serializes that model back into the database.
[2294.12 → 2296.86] And so it's just stored in a Postgres ML models table.
[2296.86 → 2306.42] And then later on, you can call the PGML predict function, and you pass it the model name, and you pass it the parameters that you want to make an inference on.
[2306.68 → 2311.36] It loads that model from the model store, makes your prediction.
[2311.90 → 2316.94] And it's very similar to what you would do with the application layer with online inference.
[2316.94 → 2318.62] So let me ask you this.
[2318.80 → 2332.70] If you are coming at this as someone who has been in Postgres for a while, like so many of us have been, but you aren't necessarily really strong on the ML side, and, you know, the idea of models is kind of new to you.
[2332.70 → 2352.16] You're not the person necessarily that was not like naturally jumping into TensorFlow or PyTorch or one of the other options out there is what is the delta between what you know in the Postgres world and what it takes to be productive with Postgres ML so that you're getting model output, and you're like you're making that leap.
[2352.34 → 2356.88] What's that delta of learning or levelling up that the practitioner needs?
[2356.88 → 2358.20] Yeah, absolutely.
[2358.40 → 2361.08] Again, we're at alpha level of functionality.
[2361.32 → 2365.32] So there's a pretty big gap of where I want to take it and where it is now.
[2365.46 → 2367.96] But we've started work on what we call the dashboard.
[2368.60 → 2375.50] And the dashboard actually has, you know, a click button wizard that you can go through, and you can select your algorithm from a drop-down list.
[2375.60 → 2378.68] You can select your source table data from a drop-down list.
[2379.10 → 2380.36] You can hit the train button.
[2380.50 → 2381.44] It will do it for you.
[2381.74 → 2384.42] And you can do this with as many different algorithms as you want.
[2384.42 → 2394.00] And you just compare the output and all of them are ranked by, you know, I've gone in, and I've selected what is the way that you should compare the outputs of these algorithms.
[2394.20 → 2396.34] There's a key metric for everything.
[2397.04 → 2403.36] And so right now there's actually two main tasks that supervised learning is perfect at.
[2403.66 → 2408.56] And that's either classification, which is, you know, you have some fixed numbers of examples.
[2408.68 → 2411.46] You want to know if it's hot dog or not hot dog, whatever it is.
[2411.46 → 2419.96] Or it's a regression where you're predicting some floating point value of whether it's zero or one or some gray area in between.
[2420.34 → 2427.30] And actually regression is probably a more advanced implementation or raw value of classification.
[2427.50 → 2433.72] You can build classification on top of regression by just rounding to zero or one in a lot of cases.
[2433.92 → 2435.20] It's not completely true.
[2435.46 → 2437.22] Some algorithms are not amenable to that.
[2437.22 → 2447.70] But generally, I think that's a useful way for us to think about it is I'm either trying to predict some number or I'm trying to predict some class of thing in most business cases.
[2448.58 → 2451.02] And so you can do that through a UI.
[2451.62 → 2455.18] We will tell you how good your predictions are for every different algorithm.
[2455.64 → 2456.56] You just pick the best one.
[2456.56 → 2462.84] You don't really need to know what the difference is between a support vector machine and a gradient boosted tree model is.
[2463.06 → 2466.36] Like, it's maybe fun for some people to learn about those things.
[2466.44 → 2468.10] But most people shouldn't care.
[2468.48 → 2471.90] They should be, you know, three-letter acronyms, but they should have a score next to them.
[2472.04 → 2475.50] You pick the one with the best score, and you move on with whatever your business is.
[2475.50 → 2489.72] So one of the things that I was pretty excited to see in this sort of initial release, which I think you mentioned thinking about, like, how do I run deep learning or advance things in Postgres?
[2489.72 → 2499.46] What I've found in a lot of the cases where I'm, like, applying, especially for, like, NLP type of things, I'm applying a sort of sophisticated model.
[2499.66 → 2505.52] But really what I'm doing is a bunch of operations on embeddings, like word embeddings or sentence embeddings.
[2505.52 → 2508.36] I'm doing similarity calculations and all of those things.
[2508.36 → 2519.94] And I see that there's this element within PostgreSQL of vector operations, which is, I think, like, really important for, like, so much of my own work.
[2520.42 → 2529.72] Lev, I'm wondering if you could comment on sort of, like, why that was important to include in terms of, like, when you were thinking through initial features.
[2529.72 → 2542.44] And also maybe, like, the future of kind of the set of models that you want to support in PostgreSQL and, like, how you would go about deciding, like, roadmap on that.
[2542.50 → 2546.54] Because there's just such a, you know, amazing diversity of things out there.
[2547.06 → 2547.64] Oh, yeah, for sure.
[2547.74 → 2551.98] I mean, I worked for about a year with, like, closely with machine learning engineers and data scientists.
[2552.40 → 2554.00] And I look at their Python code.
[2554.12 → 2555.62] I used to look at their Python code every day.
[2555.84 → 2558.98] And it was never just a call to a train and never just a call to predict.
[2558.98 → 2562.78] It wasn't just, like, just load a CSV file, magically train, and then predict something.
[2563.32 → 2566.60] There were so many transformations, so many different, like, averages, calculations.
[2566.90 → 2568.02] Like, it was never straightforward.
[2568.28 → 2572.16] It was never, like, oh, there's just one SQL query, and you get all the data magically you want.
[2572.58 → 2574.66] The data, first, was never clean, right?
[2574.92 → 2580.60] Whatever business you're running, you're always going to have, like, kind of, like, you know, kind of dirty, like, unnetted, you know, data.
[2580.68 → 2584.18] So data scientists, like, yourself, you're probably going to tell me, like, I'm telling you something obvious.
[2584.18 → 2588.68] But, like, you always have to, like, massage it and clean it up and, like, add averages, you know.
[2588.74 → 2590.88] And then the actual value itself is just garbage.
[2591.02 → 2593.64] You just end up throwing it away or just adding something to it, right?
[2593.92 → 2595.90] Daniel loves data cleaning, just to warn you.
[2595.98 → 2596.24] Okay.
[2596.32 → 2597.28] Just letting you know.
[2597.46 → 2601.64] If you don't, I don't see what the point is of being a data scientist because that's all you do.
[2601.64 → 2606.36] So, I mean, yeah, I mean, one day deep neural nets are going to clean their own data.
[2606.58 → 2608.72] But, you know, today we still have to do it ourselves.
[2609.34 → 2612.82] So you've got to have some kind of, like, you know, mathematical operations on your data.
[2613.00 → 2614.78] Like, you have to be able to transform things.
[2615.00 → 2622.46] You know, that's the main, like, talking point somebody says, like, oh, but I can't do, like, I can't do my, like, important fancy transformation in SQL.
[2622.64 → 2623.78] My answer is, well, yes, you can.
[2624.16 → 2625.02] Of course you can.
[2625.32 → 2628.40] Like, we're not going to limit you to just, you know, just pick whatever view you want.
[2628.40 → 2634.74] It's like, pick a view you can transform and clean the data and then pass it to the models and then get the results back.
[2635.14 → 2636.68] So that's why that's important.
[2637.62 → 2644.62] I think there's an important thing there, Daniel, is that, you know, Lev and I are not data scientists by trade.
[2644.92 → 2646.08] We work closely with them.
[2646.56 → 2651.06] But, you know, I think a big ask for your listeners would be, like, kick the tires on PostgreSQL.
[2651.26 → 2655.50] Tell us what sucks and what's missing so that we can cater.
[2655.50 → 2660.86] Because, you know, I have experience with NLP, and so that's why I think, you know, and embeddings.
[2661.04 → 2663.10] And so that's why I think vector operations are important.
[2663.30 → 2667.18] But there's a ton of other feature engineering that needs to be done in the world.
[2667.54 → 2670.42] I'm sure there are huge holes in the functionality right now.
[2670.74 → 2674.46] And so just filing GitHub issues of, you know, I would rather have this function available.
[2674.84 → 2677.24] That would be super helpful feedback for us.
[2677.24 → 2680.18] Well, yeah, I mean, the call has gone out.
[2680.48 → 2682.18] Many listeners will hear this.
[2682.42 → 2690.32] And I'm sure at least, you know, a good portion of those listeners have Postgres running in their company's infrastructure.
[2690.74 → 2692.54] They're working with it in some way.
[2692.70 → 2695.46] So, yeah, I know that I'm definitely going to jump in.
[2695.60 → 2698.54] And we'll make sure to include links in the show notes.
[2698.54 → 2705.72] So listeners, go and find those links, kick the tires with Postgres ML, see how it works out for you.
[2705.72 → 2718.92] As we kind of wrap up on this discussion, I wonder if maybe you could both just briefly mention something that, like, really excites you about where this is headed.
[2718.92 → 2726.72] Maybe it's something that's not implemented yet or, like, a reality that you want to see happen because something like this exists.
[2727.16 → 2735.52] What is it that, like, really kind of excites you and keeps you motivated to make sure that something like this exists and grows?
[2735.88 → 2738.26] Let's start out with Montana, maybe?
[2738.26 → 2747.82] Yeah, for me, I think it's about the simplicity that we can bring back to workflows, and we can get to the parts that really matter and are really valuable.
[2748.32 → 2760.68] So that we used to believe a lot in end-to-end machine learning at Instacart in the early days when a data scientist would need to become Python proficient and production proficient and be able to maintain and monitor their models in production.
[2760.68 → 2775.14] And it's really unrealistic at scale to expect one person to have all the skill sets necessary across data engineering, data science, machine learning engineering, infra operations, and just good software engineering.
[2775.46 → 2783.42] And expect them to go through the checklist of, you know, there's probably 100 items on a decent ML deployment checklist that you need to make sure that you're covered on.
[2783.70 → 2786.12] It really requires a team of people right now.
[2786.12 → 2803.76] And so being able to simplify a lot of that work, abstract a lot of that work, so that smaller teams that, like we're at Instacart at the time, like we started out with, can reasonably get back into production at a very high level of quality at the same time without dropping some of those things.
[2804.12 → 2805.72] Well, Montana kind of stole that line from me.
[2805.76 → 2814.44] I was going to say simplicity because I spent, like, so much time reading, like, complicated Python code and then literally, like, PhD level, like, mathematicians were talking to me, like,
[2814.44 → 2819.34] hey, what's HTTP, like, what's, like, how am I supposed to launch, what's the service?
[2819.68 → 2821.60] Like, how am I supposed to launch my model into production?
[2821.72 → 2828.20] And I'm like, I'm sorry, like, I don't know, I'll just do it for you, don't worry about it, just give me your code, I'll rewrite it, and I'll launch it, you know?
[2828.50 → 2830.74] That was the my main sticking point.
[2830.94 → 2835.70] Like, I wish I could, you could just, like, you just run a query and deploy everything immediately.
[2835.86 → 2840.64] That's, like, the simplicity of it is, and the ergonomics, I think that's something that's really exciting.
[2840.76 → 2843.60] Like, I'm really motivated by making people's lives easier.
[2843.60 → 2850.98] Like, I want, like, machine learning engineers to do machine learning that they actually enjoy, as opposed to figuring out how to, like, how to load balance a service.
[2851.14 → 2852.30] That doesn't make any sense, right?
[2853.42 → 2860.10] So, I think, like, the impact that's going to have on a lot of people, hopefully, that really, that really excites me, honestly.
[2860.68 → 2861.12] Awesome.
[2861.38 → 2867.26] Well, thank you both for such a great description and a story kind of behind Postgres ML.
[2867.26 → 2873.70] I know I'm really excited to see this materialize and excited to get hands-on with it.
[2874.04 → 2886.56] Like I say, we'll include show notes and, or links in our show notes so that our listeners can find their way and make sure and engage with the team, open some issues, open some discussions with the Postgres ML team.
[2886.96 → 2888.34] Thank you both, Montana and love.
[2888.70 → 2889.14] Thank you.
[2889.52 → 2890.54] Yeah, thank you, guys.
[2890.80 → 2891.28] Appreciate it.
[2891.28 → 2921.26] Thank you.
[2921.28 → 2951.26] Thank you.
