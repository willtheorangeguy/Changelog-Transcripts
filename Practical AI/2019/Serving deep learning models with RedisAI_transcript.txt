[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 --> 45.20]  So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.18 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.30]  And now onto the show.
[106.66 --> 108.96]  Welcome to Practical AI.
[109.42 --> 111.06]  This is Daniel Whitenack.
[111.22 --> 114.48]  I am a data scientist with SIL International,
[114.88 --> 117.16]  and I'm here with my co-host Chris Benson,
[117.54 --> 120.80]  who's a chief AI strategist at Lockheed Martin.
[121.38 --> 122.14]  How are you doing, Chris?
[122.30 --> 123.06]  Doing great, Daniel.
[123.10 --> 123.74]  How's it going today?
[123.74 --> 124.88]  It's going great.
[125.00 --> 131.34]  You know, I finally got a break in the heat wave that's been all over the U.S. here.
[131.46 --> 133.42]  I know you're a little bit further south than me,
[133.58 --> 135.10]  but I stepped out yesterday,
[135.10 --> 137.78]  and I almost thought I needed a jacket
[137.78 --> 140.80]  because the difference in temperature was so drastic.
[141.18 --> 144.04]  I haven't gotten the benefit of the cold weather down here.
[144.12 --> 147.72]  I'm in Atlanta, and so it's still quite toasty and humid here.
[147.72 --> 151.06]  You know, last week I was up in Boston the whole week,
[151.16 --> 154.08]  and I was really counting on nice, cool Boston weather,
[154.24 --> 155.72]  and it just didn't happen.
[155.88 --> 160.50]  It was only about five degrees cooler up there than it was down here,
[160.60 --> 161.72]  so it was sad.
[162.26 --> 162.42]  Yeah.
[162.64 --> 164.98]  Well, I have a bit of story.
[165.22 --> 167.30]  So when I first joined,
[167.92 --> 170.68]  or my first job as a data scientist was with this startup,
[170.96 --> 174.84]  and at the time everybody was into microservices and all of this stuff,
[174.84 --> 177.38]  and, you know, we started talking about microservices.
[177.60 --> 178.54]  I learned what those were,
[178.66 --> 182.08]  but they kept saying things like Redis this and Redis that,
[182.16 --> 184.38]  and we're going to use Redis for this and Redis for that,
[184.78 --> 190.14]  and eventually I learned that Redis is this cool data thing
[190.14 --> 194.48]  that can be used for, like, message passing and data caching
[194.48 --> 197.62]  and data store and all this stuff,
[198.06 --> 204.34]  and recently I saw that Redis released this project called Redis AI,
[204.84 --> 207.02]  so that's going to be the topic of today's conversation.
[207.02 --> 208.72]  We're joined by Peter Cayo,
[209.12 --> 212.22]  who is a senior product manager at Redis Labs.
[212.48 --> 212.96]  Welcome, Peter.
[213.40 --> 213.88]  Hi, guys.
[214.32 --> 214.56]  Yeah.
[214.80 --> 218.12]  So, Peter, could you just give us a little bit of a background
[218.12 --> 222.06]  about how you got into software and how you ended up at Redis?
[222.38 --> 224.76]  Oh, that's a, well, it's quite a long story,
[224.86 --> 225.84]  but I'll try to keep it short.
[225.84 --> 230.20]  And so, effectively, I was, when I was a kid,
[230.50 --> 231.42]  I was into astronomy,
[231.94 --> 236.70]  and I wanted to always kind of, like, motorize my telescope
[236.70 --> 240.16]  so it could effectively follow the turning of the sky,
[240.24 --> 242.16]  so to have long exposure to photos.
[243.02 --> 243.44]  Right.
[243.54 --> 244.38]  That sounds awesome.
[244.38 --> 248.62]  Yeah, that brought me into electromechanical engineering
[248.62 --> 250.74]  and then afterwards computer science.
[250.74 --> 253.82]  My first job was at TomTom.
[254.18 --> 257.46]  Well, sometimes in the U.S. they say TomTom,
[258.00 --> 258.92]  so it depends a bit,
[259.16 --> 261.70]  but I was working on the,
[261.84 --> 263.90]  to the portable navigation devices, right?
[263.96 --> 267.24]  I was working on the map back in Belgium, in Ghent.
[267.66 --> 270.60]  Map quality assurance was a difficult problem, right?
[270.66 --> 272.20]  So TomTom tries to differentiate
[272.20 --> 276.12]  and how will the quality of these maps,
[276.48 --> 277.48]  and they have many rules,
[277.64 --> 279.40]  and one of those rules is a very expensive rule.
[279.40 --> 281.44]  Is the map still connected, right?
[281.50 --> 283.60]  Can you still travel from everywhere to everywhere?
[284.54 --> 285.60]  You could imagine, for example,
[285.66 --> 287.30]  you have a continent, you have an island,
[287.44 --> 288.32]  there's a bridge in between,
[289.12 --> 291.62]  and the map editor says this bridge is now one-way traffic.
[291.80 --> 293.46]  So in the morning, you go to the island,
[293.54 --> 294.42]  in the evening, you want to go back,
[294.52 --> 296.90]  but your device says, no, sorry, can't do.
[297.76 --> 298.84]  That would be a problem.
[299.34 --> 300.14]  That would be a problem.
[300.88 --> 303.92]  So for that, effectively, we were using a graph database.
[304.48 --> 306.18]  We were effectively using Neo4j,
[306.18 --> 311.16]  and I rolled into the NoSQL database world
[311.16 --> 312.64]  because I joined Neo4j,
[313.24 --> 315.22]  worked there for three, three and a half years.
[315.80 --> 317.60]  And afterwards, I joined Redis,
[317.92 --> 319.52]  first as a solutions architect,
[320.10 --> 321.70]  and then afterwards, they said, like,
[321.72 --> 323.54]  hey, we've got one of these modules here,
[323.66 --> 324.68]  it's graph-related.
[325.14 --> 326.96]  And I joined, effectively, the product management team
[326.96 --> 330.66]  to initially first support the Redis graph module.
[330.66 --> 333.62]  But now I have seven of these modules
[333.62 --> 337.24]  under my, what's called supervision or umbrella.
[337.78 --> 338.64]  Oh, wow, that's great.
[338.80 --> 338.94]  Yeah.
[339.08 --> 340.60]  How many in total, like,
[340.70 --> 343.34]  what is the ecosystem of modules around Redis?
[343.46 --> 344.94]  I imagine there's quite a few.
[345.72 --> 347.12]  There is quite a few, right?
[347.22 --> 349.08]  So I don't know exactly,
[349.18 --> 351.32]  but I think we have 20, 25 open source modules.
[351.82 --> 353.48]  Maybe it's a bit good for the audience
[353.48 --> 355.28]  that I introduce what these modules are
[355.28 --> 356.84]  and effectively introduce what Redis is
[356.84 --> 359.10]  because that will make the story nicer.
[359.10 --> 360.68]  Yeah, that's no problem.
[361.36 --> 363.22]  So Redis is a key value store.
[363.98 --> 365.14]  It's an in-memory database.
[365.24 --> 366.14]  It's a NoSQL database.
[366.52 --> 368.08]  The most typical in-memory database
[368.08 --> 369.44]  that most people know is Memcache.
[369.54 --> 371.34]  And in Memcache, the value is always a string.
[371.86 --> 373.82]  In Redis, however, you can have different data types.
[373.92 --> 374.86]  It can be either a string,
[374.98 --> 376.44]  but it can also be a numeric value,
[376.94 --> 379.34]  a list, a sorted set, a hash, et cetera.
[379.42 --> 380.50]  So you have many data types.
[380.66 --> 382.64]  You can effectively see it as memory as a service.
[382.80 --> 384.02]  So if you're coding, you could say,
[384.12 --> 386.98]  okay, I have this data structure
[386.98 --> 389.34]  that is residing within a distributed database.
[390.14 --> 391.60]  So could you just give an idea?
[391.76 --> 393.76]  So you've kind of called out Redis
[393.76 --> 397.70]  as this key value store and a NoSQL database.
[397.70 --> 399.74]  And you also mentioned like graph databases.
[399.74 --> 402.16]  Could you just kind of generally describe,
[402.28 --> 405.52]  you know, how the NoSQL databases
[405.52 --> 409.16]  are separate from what people might have in mind
[409.16 --> 411.48]  that they execute like select statements on?
[411.86 --> 413.06]  Sometimes confusing, right?
[413.06 --> 415.42]  So NoSQL stands for not only SQL.
[416.12 --> 417.74]  So it was the movement that,
[418.24 --> 421.36]  well, we're living in some buzzwords, right?
[421.38 --> 422.20]  So there is big data.
[422.38 --> 424.12]  There is much more data.
[425.06 --> 427.08]  Yeah, we have a podcast about AI,
[427.28 --> 428.72]  so we totally get the buzzwords.
[431.90 --> 433.04]  Nothing but buzzwords.
[433.62 --> 434.34]  Nothing but, yeah.
[435.12 --> 436.64]  So database had to consume
[436.64 --> 440.02]  or to ingest higher volumes of data.
[440.02 --> 442.66]  And there were some performance issues.
[442.90 --> 445.36]  So it's not the entire picture,
[445.46 --> 446.84]  but what people kind of like did
[446.84 --> 447.98]  was they create some databases
[447.98 --> 449.52]  and they threw away everything
[449.52 --> 451.12]  that was kind of like reducing the performance
[451.12 --> 453.36]  or slowing down the performance of your database.
[453.96 --> 456.08]  So NoSQL databases typically have a,
[456.68 --> 459.16]  well, they also have a different paradigm,
[459.28 --> 461.50]  but they also have like less strict authentication.
[461.74 --> 463.92]  They're quite frequently, they're schema-less.
[464.44 --> 468.44]  So you can put lots of heterogeneous data inside it.
[468.44 --> 471.78]  And in that NoSQL section of database,
[471.92 --> 474.20]  you have quite a lot of database models, right?
[475.12 --> 476.36]  So there's a key value store,
[476.44 --> 477.38]  but there's also graph.
[477.94 --> 480.26]  You could see search also as a database model.
[480.72 --> 481.54]  There's a time series,
[481.64 --> 483.54]  which is effectively ramping up lately,
[483.76 --> 485.16]  which is another database model,
[485.52 --> 486.62]  for which you also, by the way,
[486.66 --> 488.00]  have a very interesting module.
[488.46 --> 490.20]  But yeah, I don't know if you want me
[490.20 --> 490.86]  to explain further,
[491.08 --> 493.28]  but I'll talk more about NoSQL databases
[493.28 --> 494.86]  or how they came to life.
[494.86 --> 498.56]  That was really helpful for me.
[498.78 --> 501.16]  I know that like if we kind of zero down
[501.16 --> 502.78]  in on the key value stores.
[503.40 --> 505.54]  So you mentioned like one distinguishing feature
[505.54 --> 507.34]  of Redis is that like the values
[507.34 --> 509.44]  don't have to just be strings.
[509.64 --> 511.42]  So you gave some other examples of things
[511.42 --> 512.74]  that they could be.
[512.84 --> 513.82]  I forget what those were.
[514.24 --> 515.48]  There is, for example, there is a list.
[515.92 --> 516.82]  So it's a simple,
[516.98 --> 518.46]  well, it's a list data type, right?
[518.50 --> 520.54]  So you can, effectively, it's interesting.
[521.30 --> 523.14]  Sometimes when I give a talk,
[523.14 --> 524.80]  I ask people, so for example,
[525.14 --> 526.40]  let's do the exercise, right?
[526.42 --> 529.18]  So you have two sets of items
[529.18 --> 532.62]  and inside Redis, they will reside as a set.
[532.74 --> 535.70]  So for example, imagine you have two products
[535.70 --> 537.00]  and they have a set of tags.
[538.00 --> 540.28]  Now, what could you do with these two sets?
[540.42 --> 542.24]  Which questions could you ask the database
[542.24 --> 543.68]  with two sets?
[544.00 --> 544.82]  Maybe I should hint.
[545.70 --> 552.14]  So overlapping entries or something like that?
[552.14 --> 552.54]  Correct.
[552.70 --> 553.68]  So you could do an intersection,
[553.88 --> 554.56]  you could do a union.
[555.02 --> 557.16]  So this is kind of like what Redis is, right?
[557.20 --> 558.40]  So your data structure,
[558.54 --> 560.30]  in fact, all the methods you could do
[560.30 --> 562.06]  on your programming language,
[562.88 --> 565.16]  they kind of like have commands,
[565.50 --> 568.20]  well, commands that you could execute against Redis.
[568.50 --> 568.80]  Okay.
[569.04 --> 570.90]  So you could have like value,
[571.00 --> 572.34]  a bunch of values as lists
[572.34 --> 576.18]  and execute some command
[576.18 --> 579.42]  or in some Redis client or something
[579.42 --> 581.22]  to get the intersection of those values.
[581.22 --> 581.94]  Correct.
[582.08 --> 582.86]  So in a list,
[582.94 --> 584.18]  you could get the first element,
[584.32 --> 585.38]  you could get the last element,
[585.54 --> 586.92]  you could query your range
[586.92 --> 587.90]  or get the exact element.
[588.32 --> 589.52]  You could also pop an element.
[591.18 --> 592.28]  But in a set,
[592.70 --> 593.94]  you could ask, for example,
[594.04 --> 596.24]  well, is this in a very efficient way?
[596.32 --> 597.48]  Does this element belong
[597.48 --> 600.32]  or is this present in your set, et cetera?
[600.32 --> 601.58]  So I was going to ask,
[601.94 --> 602.86]  could you kind of like,
[603.18 --> 605.04]  what are some of the most typical ways
[605.04 --> 607.22]  that Redis users are using Redis?
[607.48 --> 609.98]  What's a couple of really common use cases
[609.98 --> 611.62]  that people are most likely to do?
[612.28 --> 614.14]  Well, it's very broad, right?
[616.20 --> 617.74]  It's a general purpose database.
[617.96 --> 619.62]  You could use it for anything.
[620.08 --> 621.90]  But the most common thing
[621.90 --> 623.90]  that people are using Redis for currently
[623.90 --> 625.06]  is for session caching.
[626.06 --> 627.98]  So your shopping baskets, et cetera.
[628.12 --> 631.32]  So everything that you keep track of in sessions.
[631.84 --> 632.50]  Also for caching.
[633.40 --> 634.74]  But there are also many things
[634.74 --> 636.04]  you could use as a queue, right?
[636.84 --> 638.30]  So there is next to the,
[638.40 --> 641.60]  well, originally there was the list data type
[641.60 --> 643.74]  where you could effectively distribute messages with,
[644.38 --> 647.02]  blocking on this list,
[647.20 --> 648.68]  on retrieving the first element,
[648.88 --> 649.50]  the last element.
[649.50 --> 653.30]  But nowadays we also have a streams data type,
[654.08 --> 657.24]  which is, well, we'll call it Kafkaesque, right?
[657.28 --> 658.52]  So it has similar capabilities.
[659.60 --> 660.22]  You can have,
[661.72 --> 663.74]  you can use it as a stream or as a topic.
[664.42 --> 666.00]  Sorry, as a topic or as a queue.
[666.42 --> 667.18]  So in a queue,
[667.32 --> 668.86]  you can have, for example, a consumer group.
[669.52 --> 671.54]  And each message will only be consumed
[671.54 --> 672.44]  by a single consumer.
[673.02 --> 674.56]  But if you have to use it as a stream,
[674.66 --> 675.32]  you could, for example, say,
[675.38 --> 676.74]  I want to start reading the stream from here,
[676.82 --> 677.80]  or I just want to catch up
[677.80 --> 678.96]  from the end of the stream, et cetera.
[679.50 --> 680.74]  So also for that,
[681.70 --> 683.58]  with that specific data type,
[683.64 --> 685.64]  you could effectively do a message broker
[685.64 --> 690.22]  or event sourcing use cases.
[690.86 --> 691.60]  Gotcha, okay.
[692.22 --> 693.04]  But there are many more,
[693.10 --> 693.62]  there are many more.
[693.74 --> 695.38]  People use it sometimes to do distributed locking.
[695.76 --> 699.78]  Yeah, so you've kind of also alluded to the fact
[699.78 --> 701.98]  that like at least some of these modules of Redis
[701.98 --> 704.16]  are open source.
[705.06 --> 707.38]  Like Redis as a company,
[707.38 --> 709.00]  I know that like there's some things
[709.00 --> 711.68]  that are like open or open-ish.
[712.02 --> 713.52]  Like how does the company operate
[713.52 --> 716.22]  and like Redis itself,
[716.58 --> 718.08]  like can you find it on GitHub?
[718.50 --> 721.34]  And what's kind of the model around Redis?
[721.80 --> 722.90]  That's a good question, right?
[722.90 --> 726.36]  So Redis itself is entirely open source.
[726.50 --> 728.24]  So it's a DSD license.
[728.94 --> 730.00]  So you can take it,
[730.12 --> 731.74]  you can fork it,
[731.82 --> 733.14]  you can resell it,
[733.16 --> 734.54]  you can do whatever you want with it.
[735.40 --> 737.54]  Then there is a piece where we have these modules.
[737.74 --> 740.54]  These modules have a Redis source available license.
[741.10 --> 743.38]  So the idea is that you can effectively do anything
[743.38 --> 744.12]  with these modules,
[744.60 --> 747.06]  apart from creating a database as a service
[747.06 --> 748.70]  with these modules.
[748.70 --> 751.62]  So you can embed it inside your product.
[752.64 --> 753.04]  And effectively,
[753.22 --> 754.48]  it's a bit of a strategic way
[754.48 --> 757.26]  to compete to cloud providers,
[757.76 --> 760.00]  just simply taking all the open source products
[760.00 --> 761.98]  and then effectively offering them as a service.
[762.32 --> 764.52]  The last part is our Redis enterprise part,
[764.60 --> 765.98]  which is a closed source part.
[766.34 --> 768.48]  It doesn't have any data
[768.48 --> 770.84]  or engineering specific capabilities.
[771.12 --> 771.38]  However,
[771.44 --> 773.54]  it has lots of enterprise features
[773.54 --> 776.18]  that your company might be interested in
[776.18 --> 777.72]  or is most likely interested in.
[777.72 --> 779.62]  So there's easy to scale your database.
[779.84 --> 780.04]  There is,
[780.60 --> 783.58]  there's actually an entire database management system.
[784.22 --> 785.04]  The way you,
[785.04 --> 786.94]  I sometimes position this is that,
[787.08 --> 788.32]  do you want to become an expert
[788.32 --> 789.26]  in building your application
[789.26 --> 790.46]  or do you want to become an expert
[790.46 --> 791.50]  in deploying Redis, right?
[791.54 --> 791.92]  So if you.
[792.26 --> 792.62]  Yeah,
[792.82 --> 793.38]  that makes sense.
[794.06 --> 795.10]  If you don't want to do the second one,
[795.14 --> 797.10]  then we've got an enterprise solution for that.
[797.48 --> 798.10]  So could you,
[798.10 --> 799.88]  could you give us some examples
[799.88 --> 800.94]  of some of the modules
[800.94 --> 802.24]  that you have available?
[802.70 --> 804.02]  I'm curious about what,
[804.08 --> 804.88]  what the scope of those are.
[804.88 --> 805.60]  Well,
[806.38 --> 806.46]  I,
[806.68 --> 808.54]  the story effectively is,
[808.62 --> 810.12]  so we have all these data types
[810.12 --> 811.18]  and,
[811.34 --> 813.86]  and the original core contributor
[813.86 --> 815.16]  or creator of Redis,
[815.40 --> 816.24]  Salvatore San Felipe,
[816.84 --> 818.88]  he was receiving lots of requests
[818.88 --> 819.30]  and said like,
[819.36 --> 819.44]  oh,
[819.44 --> 820.50]  you don't have this data type.
[820.60 --> 821.52]  How about this data type?
[821.82 --> 822.00]  So,
[822.06 --> 822.40]  so he,
[822.50 --> 823.44]  he created an API
[823.44 --> 824.82]  so you could effectively create
[824.82 --> 825.72]  your own modules
[825.72 --> 826.96]  and your own,
[827.04 --> 827.24]  sorry,
[827.30 --> 829.16]  your own data structures
[829.16 --> 830.32]  and your own commands
[830.32 --> 831.42]  against those data structures.
[831.60 --> 831.92]  So,
[832.08 --> 832.68]  as we,
[832.80 --> 833.36]  the commands were,
[833.46 --> 833.76]  for example,
[833.86 --> 834.58]  do the intersection
[834.58 --> 835.42]  in between two sets
[835.42 --> 836.50]  and the sets was effectively
[836.50 --> 837.28]  the data structure.
[838.28 --> 838.68]  And,
[838.68 --> 839.22]  and that way,
[839.28 --> 840.10]  effectively could say like,
[840.14 --> 840.28]  well,
[840.36 --> 841.62]  I'm receiving lots of requests.
[841.86 --> 842.56]  Now you can build
[842.56 --> 843.38]  your own data structures
[843.38 --> 844.48]  and by,
[844.56 --> 845.38]  by creating those,
[845.50 --> 846.84]  you effectively inherit
[846.84 --> 847.56]  all the goodies
[847.56 --> 848.38]  from the moddership,
[848.44 --> 848.54]  right?
[848.54 --> 849.14]  So Redis has,
[849.28 --> 849.78]  has,
[849.92 --> 852.54]  has many things inside.
[852.60 --> 853.48]  So it has memory management,
[853.48 --> 854.26]  but it also allows you
[854.26 --> 854.50]  to,
[854.50 --> 855.80]  to cluster your database.
[856.40 --> 856.54]  And,
[856.62 --> 858.46]  one of the misconceptions
[858.46 --> 859.48]  that many people have,
[859.52 --> 859.82]  by the way,
[859.84 --> 861.84]  is that Redis is purely a cache.
[861.94 --> 862.86]  It's effectively a database.
[863.00 --> 863.18]  However,
[863.30 --> 864.44]  data lives in memory first
[864.44 --> 865.36]  and then we have
[865.36 --> 866.24]  tunable durability.
[867.16 --> 868.36]  So now if you implement
[868.36 --> 868.76]  your data,
[868.76 --> 869.34]  your data structure
[869.34 --> 870.06]  inside a module,
[870.24 --> 871.66]  you can also benefit
[871.66 --> 872.42]  from that durability
[872.42 --> 874.40]  and also have an entire
[874.40 --> 876.58]  spectrum of client libraries
[876.58 --> 877.64]  that can effectively connect
[877.64 --> 878.74]  to your database
[878.74 --> 880.02]  and reach out to those
[880.02 --> 880.58]  data structures
[880.58 --> 881.32]  in those modules.
[881.94 --> 882.76]  Now to answer your question,
[882.88 --> 882.96]  right,
[883.02 --> 885.42]  so there are quite a lot of them,
[885.70 --> 887.52]  but the ones that,
[887.56 --> 889.00]  that we effectively think
[889.00 --> 889.40]  that are,
[889.60 --> 889.76]  well,
[889.88 --> 890.40]  that we are effectively
[890.40 --> 892.62]  contributing the most to,
[892.82 --> 892.96]  there are,
[892.96 --> 893.82]  there are seven of those.
[894.16 --> 896.62]  So the most mature one
[896.62 --> 897.74]  is most likely going to be
[897.74 --> 898.30]  Redis Search.
[898.66 --> 899.74]  So it's an inverted index.
[899.90 --> 900.80]  It's kind of like
[900.80 --> 901.76]  Apache Lucene.
[902.36 --> 903.22]  And Apache Lucene,
[903.36 --> 904.74]  for those who don't know,
[905.06 --> 905.76]  Apache Lucene is effectively
[905.76 --> 906.70]  the core,
[906.70 --> 908.20]  a building box
[908.20 --> 908.96]  of Elastic Search
[908.96 --> 910.76]  and solar technology.
[910.98 --> 911.04]  So,
[911.10 --> 912.36]  but we've built our own
[912.36 --> 913.30]  inverted index.
[914.88 --> 915.86]  It's written in C.
[916.20 --> 918.08]  We serve the entire data
[918.08 --> 918.60]  or the index
[918.60 --> 919.74]  from within memory
[919.74 --> 921.22]  and also the index
[921.22 --> 922.22]  is instantly reflected.
[922.92 --> 923.46]  So we do have
[923.46 --> 924.90]  some advantages there.
[924.98 --> 925.98]  We don't have feature parity,
[926.10 --> 926.42]  of course,
[926.50 --> 927.74]  to these products
[927.74 --> 928.44]  that have been around
[928.44 --> 930.24]  for decades,
[930.42 --> 930.72]  I think.
[931.64 --> 932.04]  However,
[932.14 --> 932.90]  we get a very,
[932.96 --> 933.92]  very high performance
[933.92 --> 935.56]  in that search.
[936.42 --> 936.92]  And there is
[936.92 --> 937.84]  Redis Graph,
[938.30 --> 939.00]  which adds
[939.00 --> 939.98]  graph capabilities.
[941.34 --> 941.74]  Well,
[941.96 --> 943.04]  I know all these modules,
[943.14 --> 943.22]  right?
[943.24 --> 943.66]  So I can talk
[943.66 --> 944.88]  for hours about them.
[945.02 --> 945.98]  So Redis Graph itself
[945.98 --> 947.40]  is a very interesting
[947.40 --> 948.74]  technology.
[949.06 --> 949.68]  So I always try
[949.68 --> 950.42]  to differentiate
[950.42 --> 953.06]  graph native technologies
[953.06 --> 954.28]  and graph technology.
[954.28 --> 955.82]  So you can put
[955.82 --> 956.88]  a graph API
[956.88 --> 958.12]  on top of a relational database.
[958.56 --> 958.78]  However,
[958.86 --> 959.00]  yeah,
[959.02 --> 960.04]  it will be quite slow,
[960.10 --> 960.22]  right?
[960.24 --> 961.18]  You can make it one table,
[961.24 --> 961.76]  which is nodes,
[961.84 --> 962.28]  another table,
[962.36 --> 963.02]  which is relationships.
[963.76 --> 964.48]  But when you have
[964.48 --> 965.30]  to do a traversal
[965.30 --> 965.74]  or search,
[965.86 --> 966.24]  for example,
[966.60 --> 967.34]  a Dextra algorithm,
[967.44 --> 968.22]  which is a search algorithm
[968.22 --> 969.82]  between two nodes,
[970.34 --> 971.42]  you will have to do a join
[971.42 --> 972.40]  in between those tables
[972.40 --> 973.16]  continuously.
[973.52 --> 974.94]  So a graph native database.
[975.46 --> 976.34]  I'm so glad
[976.34 --> 977.18]  you're calling this out
[977.18 --> 978.26]  because I actually
[978.26 --> 978.80]  got burned
[978.80 --> 979.86]  by this very issue
[979.86 --> 980.62]  on a project
[980.62 --> 982.28]  where we were trying
[982.28 --> 984.62]  to implement a graph database
[984.62 --> 986.48]  and I mistakenly chose
[986.48 --> 989.36]  like a graph layer
[989.36 --> 991.90]  on top of MongoDB,
[992.18 --> 993.74]  which is another database.
[994.36 --> 995.60]  And it was so slow.
[995.96 --> 996.60]  And basically,
[996.82 --> 997.88]  the graph logic
[997.88 --> 999.38]  was really interesting
[999.38 --> 1000.92]  and good for the project,
[1000.92 --> 1001.74]  but we got burned
[1001.74 --> 1003.08]  because of this issue
[1003.08 --> 1003.84]  that you're talking about.
[1003.94 --> 1005.18]  So thanks for explaining that.
[1005.66 --> 1006.06]  Yeah, yeah.
[1006.08 --> 1007.50]  So the difference
[1007.50 --> 1008.82]  is that you have graph native,
[1008.94 --> 1010.92]  you have an 01 time complexity
[1010.92 --> 1012.18]  to go from one node
[1012.18 --> 1013.10]  to another node, right?
[1013.68 --> 1015.08]  So instead of an O log N
[1015.08 --> 1016.02]  in a relational database,
[1016.30 --> 1017.06]  and typically,
[1017.20 --> 1018.32]  you do try to keep the data
[1018.32 --> 1019.26]  as close as possible,
[1019.58 --> 1022.16]  residing within the same key,
[1022.28 --> 1023.38]  effectively, in Redis.
[1024.12 --> 1025.58]  We've got Redis Bloom,
[1025.68 --> 1026.18]  which is a set
[1026.18 --> 1027.38]  of probabilistic data structures
[1027.38 --> 1028.28]  like a Bloom filter,
[1028.40 --> 1029.02]  a Cocoa filter.
[1029.58 --> 1030.72]  We also added Top K.
[1031.70 --> 1032.80]  We've got Redis JSON,
[1033.22 --> 1035.14]  which is going to
[1035.14 --> 1036.22]  take your JSON document
[1036.22 --> 1037.20]  and is going to split it up
[1037.20 --> 1037.80]  inside a tree
[1037.80 --> 1039.50]  so that in an atomic operation,
[1039.72 --> 1041.04]  in a large JSON document,
[1041.16 --> 1041.80]  you could, for example,
[1042.18 --> 1043.86]  append some data
[1043.86 --> 1044.44]  to an array
[1044.44 --> 1045.64]  where you could increment
[1045.64 --> 1046.76]  a numeric value
[1046.76 --> 1047.96]  inside your JSON documents
[1047.96 --> 1049.02]  without having to fetch it
[1049.02 --> 1050.36]  and putting it back.
[1050.96 --> 1052.04]  And then there is Redis Time Series,
[1052.22 --> 1054.98]  which is the last one
[1054.98 --> 1056.36]  that went GA,
[1056.74 --> 1057.84]  which effectively adds
[1057.84 --> 1058.92]  time series capabilities
[1058.92 --> 1061.46]  to Redis.
[1061.56 --> 1062.24]  It allows you to do,
[1062.34 --> 1062.76]  for example,
[1063.54 --> 1064.56]  in the role of IoT,
[1064.70 --> 1065.26]  it's very interesting
[1065.26 --> 1065.98]  that you've got
[1065.98 --> 1067.74]  lots of raw data,
[1067.84 --> 1068.46]  but you also would like
[1068.46 --> 1069.58]  to downsample it.
[1069.92 --> 1070.78]  You could do that
[1070.78 --> 1071.94]  inside Redis already, right?
[1072.02 --> 1072.80]  There are many ways
[1072.80 --> 1073.32]  to do that.
[1073.68 --> 1074.46]  I already had to write
[1074.46 --> 1075.94]  lots of client-side codes
[1075.94 --> 1077.24]  and Redis Time Series
[1077.24 --> 1078.24]  comes with a toolbox
[1078.24 --> 1079.46]  to do aggregations
[1079.46 --> 1081.28]  over lots of samples
[1081.28 --> 1082.48]  or to downsample them
[1082.48 --> 1084.58]  so you don't keep
[1084.58 --> 1085.84]  all your raw data
[1085.84 --> 1086.80]  the further you go
[1086.80 --> 1087.84]  into history.
[1088.32 --> 1090.24]  One more interesting module
[1090.24 --> 1091.34]  before we dig
[1091.34 --> 1092.18]  into potentially
[1092.18 --> 1092.92]  into Redis AI
[1092.92 --> 1093.86]  is Redis Gears.
[1093.86 --> 1095.34]  And it's interesting
[1095.34 --> 1096.40]  to mention
[1096.40 --> 1099.34]  because Redis Gears
[1099.34 --> 1100.20]  will be kind of
[1100.20 --> 1101.00]  like the serverless
[1101.00 --> 1101.84]  of Redis.
[1102.74 --> 1104.18]  So you can do two things.
[1104.28 --> 1105.02]  You can do like
[1105.02 --> 1105.94]  map-produced type
[1105.94 --> 1106.46]  of operations
[1106.46 --> 1107.50]  on top of your
[1107.50 --> 1108.76]  entire data set
[1108.76 --> 1111.26]  because Redis allows you
[1111.26 --> 1112.44]  to key value stores
[1112.44 --> 1113.16]  so you can shard it,
[1113.20 --> 1113.98]  you can partition it.
[1114.30 --> 1114.92]  So if you want to run
[1114.92 --> 1116.00]  a query across
[1116.00 --> 1116.74]  all these shards,
[1117.24 --> 1118.00]  there was no clean
[1118.00 --> 1119.00]  solution for that.
[1119.10 --> 1119.62]  So Redis Gears
[1119.62 --> 1121.04]  will give that to you.
[1121.58 --> 1122.20]  The second part
[1122.20 --> 1122.82]  is that it can also
[1122.82 --> 1125.08]  execute certain scripts
[1125.08 --> 1128.16]  based upon certain triggers
[1128.16 --> 1128.94]  or certain events.
[1129.48 --> 1130.00]  So it could be,
[1130.10 --> 1130.36]  for example,
[1130.36 --> 1131.06]  you add something
[1131.06 --> 1132.38]  to a stream
[1132.38 --> 1133.06]  or you change
[1133.06 --> 1133.78]  a certain key
[1133.78 --> 1134.94]  but it can also
[1134.94 --> 1135.68]  be time-based
[1135.68 --> 1136.36]  and then you execute
[1136.36 --> 1137.80]  certain codes.
[1138.44 --> 1139.64]  And this kind of
[1139.64 --> 1140.60]  like makes the entire
[1140.60 --> 1142.52]  multi-model story
[1142.52 --> 1144.08]  very beautiful.
[1144.42 --> 1145.08]  And I know
[1145.08 --> 1146.12]  in our company
[1146.12 --> 1147.02]  I'm the first one
[1147.02 --> 1147.78]  to say if somebody
[1147.78 --> 1147.98]  says,
[1148.12 --> 1148.22]  hey,
[1148.66 --> 1149.50]  multi-module,
[1149.72 --> 1150.42]  multi-model,
[1150.56 --> 1151.46]  please be cautious
[1151.46 --> 1151.98]  about that.
[1151.98 --> 1153.74]  So it's not
[1153.74 --> 1154.32]  because we have
[1154.32 --> 1155.22]  multiple modules
[1155.22 --> 1155.80]  in a database
[1155.80 --> 1156.68]  that we're a
[1156.68 --> 1157.68]  multi-model database
[1157.68 --> 1158.70]  but Redis Gears
[1158.70 --> 1159.32]  kind of like
[1159.32 --> 1160.54]  allows you to do that.
[1161.08 --> 1161.54]  So you have,
[1161.66 --> 1161.84]  for example,
[1161.84 --> 1162.74]  a stream of data,
[1162.86 --> 1163.94]  you get some
[1163.94 --> 1166.08]  name change,
[1166.16 --> 1166.58]  for example.
[1167.18 --> 1167.82]  You could say,
[1167.94 --> 1168.10]  hey,
[1168.60 --> 1169.64]  the script is going
[1169.64 --> 1170.32]  to react upon
[1170.32 --> 1171.22]  that new piece
[1171.22 --> 1171.56]  of data.
[1171.64 --> 1172.18]  It's going to say,
[1172.48 --> 1172.58]  hey,
[1172.62 --> 1173.14]  Redis Search,
[1173.62 --> 1174.34]  please update
[1174.34 --> 1175.78]  the name
[1175.78 --> 1176.56]  of this person
[1176.56 --> 1177.38]  but also,
[1177.56 --> 1177.64]  hey,
[1177.72 --> 1178.32]  Redis Graph,
[1178.82 --> 1179.26]  make sure
[1179.26 --> 1180.28]  that graph person
[1180.28 --> 1181.04]  or the graph node
[1181.04 --> 1181.56]  is updated.
[1182.76 --> 1183.68]  So it can effectively
[1183.68 --> 1185.34]  talk to all these modules
[1185.34 --> 1186.88]  and then it becomes
[1186.88 --> 1187.18]  very,
[1187.28 --> 1187.78]  very interesting.
[1188.38 --> 1189.48]  So you just mentioned
[1189.48 --> 1191.06]  kind of this idea
[1191.06 --> 1192.92]  of multi-modules
[1192.92 --> 1194.46]  or multi-module
[1194.46 --> 1196.58]  and like the ability
[1196.58 --> 1197.48]  to run scripts,
[1197.60 --> 1198.06]  the ability
[1198.06 --> 1199.60]  to put things together.
[1199.72 --> 1200.62]  You also mentioned
[1200.62 --> 1201.52]  Redis AI,
[1202.16 --> 1202.92]  which is really
[1202.92 --> 1204.00]  what we want to get into
[1204.00 --> 1204.82]  in the rest
[1204.82 --> 1206.18]  of this discussion.
[1206.18 --> 1207.82]  But I was wondering
[1207.82 --> 1208.50]  just kind of
[1208.50 --> 1210.26]  in terms of background,
[1211.06 --> 1212.90]  what is the background
[1212.90 --> 1214.08]  on Redis AI
[1214.08 --> 1215.06]  in terms of
[1215.06 --> 1216.18]  why the team
[1216.18 --> 1216.86]  was motivated
[1216.86 --> 1218.22]  to create it?
[1218.28 --> 1218.92]  Was it something
[1218.92 --> 1219.72]  that users
[1219.72 --> 1221.30]  were asking for?
[1221.38 --> 1221.74]  They're like,
[1221.82 --> 1221.94]  oh,
[1221.98 --> 1222.78]  we love Redis
[1222.78 --> 1223.78]  but we want to integrate
[1223.78 --> 1224.40]  this somehow
[1224.40 --> 1226.08]  with like AI models
[1226.08 --> 1227.14]  or like what's
[1227.14 --> 1228.08]  the backstory on that
[1228.08 --> 1228.92]  and kind of how did it
[1228.92 --> 1229.76]  come about?
[1230.02 --> 1230.94]  It came effectively
[1230.94 --> 1231.88]  from three ways,
[1231.96 --> 1232.06]  right?
[1232.10 --> 1233.08]  So the first one
[1233.08 --> 1235.36]  is that Salvatore
[1235.36 --> 1236.74]  as when he created
[1236.74 --> 1237.52]  this module API,
[1237.64 --> 1238.14]  the first module
[1238.14 --> 1238.56]  he created
[1238.56 --> 1239.66]  was neural Redis.
[1240.08 --> 1240.46]  So that was
[1240.46 --> 1241.32]  the first kind of
[1241.32 --> 1242.38]  like indication
[1242.38 --> 1242.84]  that there was
[1242.84 --> 1243.64]  it could be
[1243.64 --> 1244.50]  potentially a need
[1244.50 --> 1244.92]  for that.
[1245.24 --> 1245.86]  Then there was also
[1245.86 --> 1248.12]  some engineers
[1248.12 --> 1249.42]  inside Redis Labs
[1249.42 --> 1249.90]  who created
[1249.90 --> 1250.60]  a module called
[1250.60 --> 1251.18]  Redis ML.
[1251.46 --> 1251.84]  So they thought
[1251.84 --> 1252.68]  that they could,
[1252.84 --> 1253.08]  for example,
[1253.16 --> 1254.40]  have very specific
[1254.40 --> 1255.24]  data structures,
[1255.72 --> 1256.48]  for example,
[1256.62 --> 1258.12]  for a random forestry,
[1258.72 --> 1259.62]  for some regression,
[1259.78 --> 1260.88]  some specific data structures
[1260.88 --> 1261.70]  for these models
[1261.70 --> 1262.54]  or these AI models
[1262.54 --> 1263.28]  and effectively
[1263.28 --> 1263.88]  host them
[1263.88 --> 1265.80]  inside Redis.
[1266.22 --> 1266.66]  And then there was
[1266.66 --> 1267.16]  also somebody
[1267.16 --> 1269.14]  who was creating
[1269.14 --> 1269.90]  Redis DL,
[1270.10 --> 1270.76]  another module
[1270.76 --> 1271.34]  which is then
[1271.34 --> 1272.06]  focused on
[1272.06 --> 1273.78]  deep learning.
[1274.12 --> 1274.56]  And we kind of
[1274.56 --> 1275.14]  like combined
[1275.14 --> 1275.74]  these efforts
[1275.74 --> 1276.40]  and we created
[1276.40 --> 1278.32]  one module
[1278.32 --> 1279.02]  which is called
[1279.02 --> 1279.98]  Redis AI.
[1280.64 --> 1280.84]  Now,
[1281.34 --> 1282.20]  that's how it
[1282.20 --> 1282.82]  came to life,
[1282.88 --> 1283.02]  right?
[1284.16 --> 1285.16]  But the need
[1285.16 --> 1285.74]  or explaining
[1285.74 --> 1286.22]  the need
[1286.22 --> 1287.96]  is also
[1287.96 --> 1289.02]  quite important.
[1289.78 --> 1291.30]  So there are
[1291.30 --> 1292.54]  two things
[1292.54 --> 1293.12]  we believe
[1293.12 --> 1293.36]  there,
[1293.42 --> 1293.56]  right?
[1293.60 --> 1294.30]  So there is
[1294.30 --> 1295.06]  data locality
[1295.06 --> 1295.96]  and then there's
[1295.96 --> 1296.32]  effectively
[1296.32 --> 1298.66]  the DevOps
[1298.66 --> 1299.14]  part
[1299.14 --> 1301.26]  of publishing
[1301.26 --> 1302.28]  your model.
[1302.74 --> 1303.18]  The publishing
[1303.18 --> 1303.82]  of your model,
[1304.10 --> 1304.60]  it's quite,
[1305.00 --> 1305.58]  it's always
[1305.58 --> 1306.06]  straightforward,
[1306.20 --> 1306.50]  it's always
[1306.50 --> 1307.08]  convenient.
[1307.26 --> 1307.56]  So you can,
[1307.64 --> 1307.92]  for example,
[1307.92 --> 1308.44]  have your
[1308.44 --> 1309.62]  model,
[1309.76 --> 1310.20]  you wrap it
[1310.20 --> 1310.86]  inside the Flask
[1310.86 --> 1311.46]  application,
[1311.90 --> 1312.60]  but then you have
[1312.60 --> 1313.08]  to scale it
[1313.08 --> 1313.48]  yourself,
[1313.58 --> 1314.04]  you have to add
[1314.04 --> 1314.80]  all these things
[1314.80 --> 1316.52]  manually.
[1317.52 --> 1318.40]  So with Redis,
[1318.48 --> 1318.78]  we effectively
[1318.78 --> 1319.86]  have all these
[1319.86 --> 1320.38]  things already.
[1320.70 --> 1321.64]  We can scale it,
[1321.72 --> 1322.84]  we can cluster
[1322.84 --> 1323.56]  your database.
[1324.18 --> 1325.02]  So we have all
[1325.02 --> 1325.58]  these clients
[1325.58 --> 1325.86]  already,
[1325.88 --> 1326.34]  they can connect
[1326.34 --> 1326.68]  to it.
[1326.90 --> 1327.52]  We already have
[1327.52 --> 1328.16]  high availability,
[1328.44 --> 1329.40]  we have effectively
[1329.40 --> 1330.56]  also durability.
[1331.20 --> 1331.82]  So if your
[1331.82 --> 1334.02]  Flask application
[1334.02 --> 1334.52]  goes down
[1334.52 --> 1335.52]  and you didn't,
[1335.72 --> 1336.12]  for example,
[1336.28 --> 1336.42]  well,
[1336.90 --> 1337.28]  if there's no
[1337.28 --> 1337.94]  high availability,
[1338.24 --> 1338.96]  then your
[1338.96 --> 1339.90]  model serving
[1339.90 --> 1340.48]  would no longer
[1340.48 --> 1341.20]  be available.
[1341.60 --> 1342.14]  So all the
[1342.14 --> 1343.18]  goodies that Redis
[1343.18 --> 1343.76]  brings as a
[1343.76 --> 1344.00]  database,
[1344.12 --> 1344.90]  you suddenly also
[1344.90 --> 1345.52]  get for free
[1345.52 --> 1346.10]  if you would
[1346.10 --> 1346.94]  add Redis
[1346.94 --> 1347.52]  AI to,
[1348.18 --> 1348.66]  or some,
[1348.72 --> 1348.88]  some,
[1349.04 --> 1349.80]  these models
[1349.80 --> 1350.92]  to Redis.
[1351.42 --> 1352.06]  The second
[1352.06 --> 1352.90]  part is that
[1352.90 --> 1353.58]  we believe
[1353.58 --> 1354.08]  is a data
[1354.08 --> 1354.60]  locality.
[1355.66 --> 1356.30]  For that,
[1356.38 --> 1356.72]  maybe it's
[1356.72 --> 1357.36]  interesting to
[1357.36 --> 1358.44]  give a model
[1358.44 --> 1360.84]  or to tell
[1360.84 --> 1361.52]  a story,
[1361.60 --> 1361.92]  for example.
[1362.06 --> 1362.42]  You have a
[1362.42 --> 1362.70]  chatbot
[1362.70 --> 1363.22]  application,
[1363.68 --> 1363.86]  and this
[1363.86 --> 1364.22]  chatbot
[1364.22 --> 1364.86]  application
[1364.86 --> 1365.56]  has a
[1365.56 --> 1365.78]  certain
[1365.78 --> 1366.12]  model,
[1366.26 --> 1366.50]  so it
[1366.50 --> 1366.86]  takes in
[1366.86 --> 1367.52]  two tensors,
[1367.82 --> 1368.46]  or two
[1368.46 --> 1369.98]  input parameters.
[1370.36 --> 1370.72]  The first
[1370.72 --> 1371.18]  one is your
[1371.18 --> 1372.58]  latest message
[1372.58 --> 1373.46]  that the
[1373.46 --> 1373.76]  chatbot
[1373.76 --> 1374.20]  received,
[1374.54 --> 1375.08]  but also the
[1375.08 --> 1375.44]  second one
[1375.44 --> 1375.66]  is the
[1375.66 --> 1376.08]  intermediate
[1376.08 --> 1376.52]  state.
[1377.00 --> 1377.40]  So there's
[1377.40 --> 1377.72]  an intermediate
[1377.72 --> 1378.28]  state of the
[1378.28 --> 1378.88]  past or the
[1378.88 --> 1379.42]  history of
[1379.42 --> 1380.10]  that conversation.
[1380.44 --> 1381.10]  And combined
[1381.10 --> 1381.56]  with that,
[1381.76 --> 1383.44]  it produces an
[1383.44 --> 1384.30]  output, and the
[1384.30 --> 1384.84]  output is the
[1384.84 --> 1386.08]  response, but it's
[1386.08 --> 1386.70]  also a new
[1386.70 --> 1387.60]  intermediate state
[1387.60 --> 1388.88]  that is a new
[1388.88 --> 1390.24]  history of your
[1390.24 --> 1390.80]  conversation.
[1391.34 --> 1392.28]  Now you want to
[1392.28 --> 1392.82]  keep that as
[1392.82 --> 1393.52]  close as possible
[1393.52 --> 1394.14]  to that model.
[1394.24 --> 1394.68]  You don't want to
[1394.68 --> 1395.40]  go and fetch it
[1395.40 --> 1395.80]  from another
[1395.80 --> 1396.70]  database, then
[1396.70 --> 1397.16]  bring it to
[1397.16 --> 1397.82]  your application
[1397.82 --> 1398.74]  or to your
[1398.74 --> 1399.84]  own Flask
[1399.84 --> 1400.44]  wrapper where
[1400.44 --> 1400.96]  you've written,
[1401.74 --> 1402.56]  where you try to
[1402.56 --> 1403.56]  deploy your model,
[1403.56 --> 1404.68]  add another
[1404.68 --> 1406.12]  data fetching.
[1406.40 --> 1407.14]  For sure, if that
[1407.14 --> 1408.20]  data you want to
[1408.20 --> 1408.70]  fetch becomes
[1408.70 --> 1410.02]  large, there will
[1410.02 --> 1411.22]  be some latency.
[1411.94 --> 1413.26]  And what we
[1413.26 --> 1414.08]  believe in Redis is
[1414.08 --> 1414.64]  that everything
[1414.64 --> 1415.80]  should be extremely
[1415.80 --> 1416.38]  fast, right?
[1416.46 --> 1417.02]  Because there's a
[1417.02 --> 1417.54]  high throughput,
[1417.96 --> 1418.54]  well, there's a
[1418.54 --> 1419.30]  demand for high
[1419.30 --> 1420.22]  throughput databases
[1420.22 --> 1421.12]  or high throughput
[1421.12 --> 1422.48]  requests with very
[1422.48 --> 1423.00]  low latency.
[1423.16 --> 1423.66]  Everything needs to
[1423.66 --> 1424.26]  be more and more
[1424.26 --> 1425.92]  snappy by actually
[1425.92 --> 1427.32]  creating these data
[1427.32 --> 1428.24]  structures or by
[1428.24 --> 1429.08]  creating Redis AI.
[1429.08 --> 1431.46]  we could now run
[1431.46 --> 1433.58]  your inference
[1433.58 --> 1434.48]  where your data
[1434.48 --> 1435.22]  lives, right?
[1435.50 --> 1436.12]  Because people
[1436.12 --> 1436.92]  sometimes also have,
[1437.00 --> 1437.60]  for example, some
[1437.60 --> 1439.00]  extra input data,
[1439.22 --> 1440.18]  get a user profile
[1440.18 --> 1441.28]  and feed it to your
[1441.28 --> 1442.78]  model to do a
[1442.78 --> 1444.46]  better inference or
[1444.46 --> 1445.30]  classification, right?
[1445.56 --> 1447.18]  So now that data
[1447.18 --> 1448.26]  doesn't need to be
[1448.26 --> 1449.20]  fetched from another
[1449.20 --> 1450.14]  host or from another
[1450.14 --> 1450.96]  database.
[1451.08 --> 1451.68]  It's already there.
[1451.98 --> 1452.74]  It can live within
[1452.74 --> 1453.48]  Redis next to the
[1453.48 --> 1453.66]  model.
[1454.26 --> 1455.04]  So, you know, as you
[1455.04 --> 1455.88]  talk about the chatbot
[1455.88 --> 1456.82]  example, you know,
[1456.88 --> 1457.86]  where is the tensor
[1457.86 --> 1458.40]  serving?
[1458.40 --> 1459.26]  Where you're
[1459.26 --> 1459.98]  executing deep
[1459.98 --> 1460.50]  learning models?
[1460.62 --> 1461.44]  How does that fit
[1461.44 --> 1461.90]  into this?
[1461.98 --> 1462.52]  Could you kind of
[1462.52 --> 1463.90]  give it to us, give
[1463.90 --> 1464.76]  the context of that
[1464.76 --> 1465.66]  so that we can kind of
[1465.66 --> 1466.36]  map it together?
[1466.76 --> 1467.56]  There are three data
[1467.56 --> 1468.46]  structures inside
[1468.46 --> 1469.94]  Redis AI that we add.
[1470.26 --> 1471.46]  So there's a tensor,
[1471.96 --> 1472.70]  there's a script, and
[1472.70 --> 1473.22]  there's a model.
[1473.82 --> 1474.44]  So you can effectively
[1474.44 --> 1475.94]  now, the key value
[1475.94 --> 1476.66]  store, the value now
[1476.66 --> 1477.52]  can be a tensor.
[1477.66 --> 1478.38]  So you can host your
[1478.38 --> 1479.98]  tensors inside Redis.
[1480.34 --> 1481.00]  Is that answering your
[1481.00 --> 1481.30]  question?
[1481.54 --> 1482.16]  I think so.
[1482.18 --> 1482.68]  I was just wanting to
[1482.68 --> 1483.64]  kind of like break it
[1483.64 --> 1484.78]  down in the sense of
[1484.78 --> 1486.14]  with the chatbot kind
[1486.14 --> 1487.42]  of walking through how
[1487.42 --> 1488.12]  you're using
[1488.12 --> 1489.60]  the module, how
[1489.60 --> 1491.46]  Redis AI is fitting
[1491.46 --> 1492.34]  into that example.
[1492.98 --> 1493.88]  So if you were coming
[1493.88 --> 1494.64]  into it for the first
[1494.64 --> 1495.84]  time as a user that
[1495.84 --> 1496.46]  was wanting to use
[1496.46 --> 1497.52]  this, just kind of
[1497.52 --> 1498.80]  taking that as a
[1498.80 --> 1500.02]  contextual example
[1500.02 --> 1500.96]  about how I might do
[1500.96 --> 1501.12]  that.
[1501.18 --> 1501.94]  Like if I sit down
[1501.94 --> 1503.42]  after a conversation
[1503.42 --> 1504.22]  and try to do it,
[1504.32 --> 1504.94]  can you just kind of
[1504.94 --> 1506.32]  describe it end to end
[1506.32 --> 1507.10]  in terms of how that
[1507.10 --> 1507.58]  happens?
[1508.34 --> 1508.48]  Right.
[1508.48 --> 1510.14]  So your training part
[1510.14 --> 1511.56]  is still going to be
[1511.56 --> 1512.90]  going to be the same,
[1513.00 --> 1513.14]  right?
[1513.60 --> 1516.02]  So once you've trained
[1516.02 --> 1517.20]  your model and you're
[1517.20 --> 1518.34]  sure that it's the
[1518.34 --> 1519.20]  right fit for it,
[1519.32 --> 1520.00]  you can effectively
[1520.00 --> 1522.76]  import it inside
[1522.76 --> 1524.30]  Redis AI.
[1524.70 --> 1526.14]  So we're building quite
[1526.14 --> 1527.06]  some tooling around it
[1527.06 --> 1527.92]  to make it more easy
[1527.92 --> 1528.68]  so that you can do it,
[1528.76 --> 1529.12]  for example,
[1529.24 --> 1529.90]  directly from
[1529.90 --> 1530.98]  scikit-learn.
[1531.64 --> 1533.20]  There's already a
[1533.20 --> 1533.86]  connector for that.
[1533.92 --> 1534.40]  We also have a
[1534.40 --> 1535.00]  connector, for example,
[1535.08 --> 1536.02]  from Spark.
[1536.02 --> 1536.96]  So you take your
[1536.96 --> 1537.56]  model and you can put
[1537.56 --> 1538.86]  it inside Redis.
[1539.12 --> 1539.94]  The next thing is if
[1539.94 --> 1540.48]  you want to build an
[1540.48 --> 1541.28]  application, you will
[1541.28 --> 1542.72]  have some client
[1542.72 --> 1544.14]  library that is going
[1544.14 --> 1545.36]  to connect to Redis.
[1545.98 --> 1546.62]  And from that client
[1546.62 --> 1547.46]  library, you could
[1547.46 --> 1549.42]  post effectively your
[1549.42 --> 1550.86]  tensor inside Redis.
[1550.98 --> 1551.44]  You could say, hey,
[1551.48 --> 1552.36]  here's my new message.
[1552.74 --> 1553.48]  There's also the
[1553.48 --> 1554.30]  output tensor.
[1554.44 --> 1555.06]  Well, there's also the
[1555.06 --> 1555.90]  input tensor of the
[1555.90 --> 1556.56]  intermediate state.
[1557.22 --> 1558.18]  And then you can
[1558.18 --> 1559.28]  effectively run that
[1559.28 --> 1559.52]  model.
[1559.70 --> 1560.44]  It's another command
[1560.44 --> 1561.76]  that you can run from
[1561.76 --> 1562.66]  the client side or the
[1562.66 --> 1563.70]  client library application
[1563.70 --> 1564.96]  side to do your
[1564.96 --> 1565.30]  inference.
[1565.30 --> 1566.50]  Yeah, I'm going to
[1566.50 --> 1568.26]  kind of, so I have a
[1568.26 --> 1569.26]  theory going in my
[1569.26 --> 1570.54]  mind and I want to
[1570.54 --> 1571.22]  kind of check it.
[1571.32 --> 1572.02]  So you mentioned the
[1572.02 --> 1573.18]  three data structures.
[1573.18 --> 1574.18]  You got the tensor,
[1574.68 --> 1576.00]  the graph or the
[1576.00 --> 1577.38]  model, and then the
[1577.38 --> 1577.66]  script.
[1577.78 --> 1578.52]  So would it be true
[1578.52 --> 1579.48]  that you could kind of
[1579.48 --> 1581.24]  have tensors stored
[1581.24 --> 1582.64]  in Redis and these
[1582.64 --> 1585.04]  might be like test
[1585.04 --> 1586.16]  examples or maybe
[1586.16 --> 1587.00]  these are like
[1587.00 --> 1588.08]  knowledge base articles
[1588.08 --> 1588.94]  if you're answering
[1588.94 --> 1589.90]  questions out of a
[1589.90 --> 1590.74]  knowledge base or
[1590.74 --> 1592.18]  maybe it's like some
[1592.18 --> 1593.34]  images or something.
[1593.84 --> 1595.18]  And you could execute
[1595.18 --> 1596.76]  like certain of the
[1596.76 --> 1598.06]  scripts of the script
[1598.06 --> 1599.80]  database or data
[1599.80 --> 1601.00]  structures on those
[1601.00 --> 1602.00]  tensors to maybe do
[1602.00 --> 1603.28]  like pre-processing or
[1603.28 --> 1604.52]  something and like
[1604.52 --> 1605.20]  combine them in
[1605.20 --> 1606.46]  interesting ways before
[1606.46 --> 1607.78]  they would be passed
[1607.78 --> 1609.10]  off to maybe the
[1609.10 --> 1610.74]  graph data structure to
[1610.74 --> 1612.24]  actually perform an
[1612.24 --> 1614.20]  inference with a model.
[1614.30 --> 1614.74]  And then maybe it
[1614.74 --> 1615.54]  would go back to the
[1615.54 --> 1616.44]  scripts for like
[1616.44 --> 1618.06]  post-processing and
[1618.06 --> 1619.34]  then stored the
[1619.34 --> 1620.64]  results stored in like
[1620.64 --> 1621.92]  tensor data structure
[1621.92 --> 1622.16]  again.
[1622.16 --> 1623.94]  Is that kind of on the
[1623.94 --> 1624.52]  right track?
[1624.84 --> 1626.34]  That is exactly it.
[1626.58 --> 1627.50]  That is exactly it.
[1627.52 --> 1628.32]  That's how we want it
[1628.32 --> 1628.84]  to be.
[1628.94 --> 1629.88]  So you can have these
[1629.88 --> 1631.40]  three data structures
[1631.40 --> 1632.12]  and you can combine
[1632.12 --> 1632.94]  them and mix and
[1632.94 --> 1633.86]  match them as you go.
[1634.36 --> 1635.00]  So you can also use
[1635.00 --> 1636.38]  those as well if you
[1636.38 --> 1637.48]  would like to run
[1637.48 --> 1638.36]  several models and
[1638.36 --> 1639.16]  combine the results
[1639.16 --> 1639.94]  you can also use a
[1639.94 --> 1641.10]  script and run them
[1641.10 --> 1642.84]  several graphs underneath.
[1643.20 --> 1643.88]  One more thing is
[1643.88 --> 1645.20]  that well that is
[1645.20 --> 1645.66]  coming up is
[1645.66 --> 1646.18]  effectively you will
[1646.18 --> 1646.98]  have a command which
[1646.98 --> 1647.52]  is a direct
[1647.52 --> 1649.06]  acyclic graph so you
[1649.06 --> 1650.14]  can effectively execute
[1650.14 --> 1650.78]  those commands
[1650.78 --> 1651.64]  combined right so you
[1651.64 --> 1652.36]  could for example do
[1652.36 --> 1655.32]  you set a tensor but
[1655.32 --> 1656.12]  then the output is
[1656.12 --> 1656.92]  passed to a script.
[1657.20 --> 1658.10]  The script's output is
[1658.10 --> 1659.76]  then passed to a
[1659.76 --> 1660.60]  model and then the
[1660.60 --> 1661.84]  model output is once
[1661.84 --> 1662.54]  again passed to a
[1662.54 --> 1663.16]  script and you can
[1663.16 --> 1664.42]  then the output of
[1664.42 --> 1665.52]  that script could be a
[1665.52 --> 1665.98]  tensor that is
[1665.98 --> 1666.74]  persistent inside
[1666.74 --> 1667.26]  Redis right.
[1667.56 --> 1668.32]  So you can kind of
[1668.32 --> 1669.40]  like pipeline those
[1669.40 --> 1670.82]  those commands in a
[1670.82 --> 1672.82]  single single call
[1672.82 --> 1673.70]  towards Redis.
[1674.34 --> 1675.94]  But your explanation
[1675.94 --> 1676.58]  was spot on.
[1676.90 --> 1678.02]  Awesome yeah so I'm
[1678.02 --> 1678.90]  just part of the
[1678.90 --> 1680.92]  reason why I have
[1680.92 --> 1682.18]  that excuse me I
[1682.18 --> 1682.88]  have that in mind
[1682.88 --> 1684.58]  is like I have I
[1684.58 --> 1685.26]  have a direct use
[1685.26 --> 1685.92]  case I'm thinking
[1685.92 --> 1687.40]  of in the problems
[1687.40 --> 1688.28]  I'm solving now so
[1688.28 --> 1689.56]  we have like a
[1689.56 --> 1690.20]  bunch of knowledge
[1690.20 --> 1691.26]  based articles that
[1691.26 --> 1692.38]  we're doing reading
[1692.38 --> 1694.42]  comprehension on but
[1694.42 --> 1695.54]  we're also doing like
[1695.54 --> 1696.62]  a full text search of
[1696.62 --> 1698.02]  those based on TF
[1698.02 --> 1699.98]  IDF and so my
[1699.98 --> 1700.94]  thought is oh well
[1700.94 --> 1702.78]  what if I could so I
[1702.78 --> 1703.54]  don't know check me
[1703.54 --> 1704.34]  on this to see if
[1704.34 --> 1704.88]  this would be a
[1704.88 --> 1705.62]  proper way to use
[1705.62 --> 1706.56]  Redis AI but I
[1706.56 --> 1708.12]  could like store the
[1708.12 --> 1709.32]  knowledge base
[1709.32 --> 1710.80]  article text as
[1710.80 --> 1712.48]  certain maybe
[1712.48 --> 1713.50]  string elements
[1713.50 --> 1714.92]  string data
[1714.92 --> 1716.18]  structures in Redis
[1716.18 --> 1717.16]  and then I could
[1717.16 --> 1718.52]  use maybe a script
[1718.52 --> 1720.08]  in combination with
[1720.08 --> 1721.52]  the the graph that
[1721.52 --> 1722.50]  would store like my
[1722.50 --> 1723.72]  vectorizer my TF
[1723.72 --> 1725.34]  IDF vectorizer to
[1725.34 --> 1726.72]  transform those into
[1726.72 --> 1729.02]  like actual tensors
[1729.02 --> 1730.76]  in the tensor data
[1730.76 --> 1732.14]  structure and then
[1732.14 --> 1733.14]  when I would do like
[1733.14 --> 1734.44]  a document search on
[1734.44 --> 1735.32]  those maybe I could
[1735.32 --> 1736.48]  use some of the like
[1736.48 --> 1738.44]  overlapping or or
[1738.44 --> 1739.50]  score generation
[1739.50 --> 1740.98]  script or something
[1740.98 --> 1742.24]  to actually do the
[1742.24 --> 1743.42]  do the matching I
[1743.42 --> 1743.82]  don't know what do
[1743.82 --> 1744.58]  you think I think
[1744.58 --> 1745.42]  that makes perfect
[1745.42 --> 1746.20]  sense to me that
[1746.20 --> 1746.66]  this is effectively
[1746.66 --> 1748.06]  what we want to do
[1748.06 --> 1748.88]  and it can even be
[1748.88 --> 1750.86]  more beautiful as well
[1750.86 --> 1751.66]  you mentioned for
[1751.66 --> 1752.26]  example you would
[1752.26 --> 1753.02]  fetch your knowledge
[1753.02 --> 1754.70]  graph as a as a
[1754.70 --> 1755.96]  tensor if your
[1755.96 --> 1757.12]  knowledge graph is
[1757.12 --> 1758.94]  changing over time
[1758.94 --> 1759.46]  right you could
[1759.46 --> 1760.80]  effectively host that
[1760.80 --> 1761.74]  knowledge graph inside
[1761.74 --> 1763.30]  Redis graph so
[1763.30 --> 1764.48]  then it's there it's
[1764.48 --> 1765.20]  living as a database
[1765.20 --> 1765.74]  you can effectively
[1765.74 --> 1766.62]  let it evolve over
[1766.62 --> 1768.16]  time it might be for
[1768.16 --> 1768.62]  example that you
[1768.62 --> 1769.50]  want to add scoring
[1769.50 --> 1770.64]  or you could say
[1770.64 --> 1771.44]  well on given
[1771.44 --> 1772.30]  searches you want to
[1772.30 --> 1773.22]  bumper certain
[1773.22 --> 1774.28]  certain notes or
[1774.28 --> 1775.34]  certain relevancies
[1775.34 --> 1776.98]  or you may you might
[1776.98 --> 1777.86]  want to make custom
[1777.86 --> 1779.04]  queries you want to
[1779.04 --> 1780.54]  use as an input for
[1780.54 --> 1781.42]  your graph right if
[1781.42 --> 1782.04]  you want to say well
[1782.04 --> 1782.82]  if you want to make
[1782.82 --> 1783.26]  something very
[1783.26 --> 1784.46]  tailor-made and then
[1784.46 --> 1786.76]  effectively gears could
[1786.76 --> 1787.80]  effectively be also
[1787.80 --> 1788.84]  be gluing all these
[1788.84 --> 1789.58]  things together right
[1789.58 --> 1790.42]  so but your script
[1790.42 --> 1792.50]  could already well not
[1792.50 --> 1793.22]  not at this moment in
[1793.22 --> 1793.66]  time but it's
[1793.66 --> 1794.54]  something we plan to
[1794.54 --> 1795.50]  do your script could
[1795.50 --> 1796.52]  effectively then consult
[1796.52 --> 1797.48]  Redis graph and
[1797.48 --> 1798.44]  fetch that data for
[1798.44 --> 1799.58]  you okay yeah so
[1799.58 --> 1800.62]  there could be like
[1800.62 --> 1802.22]  so there there could
[1802.22 --> 1803.70]  be routing logic that
[1803.70 --> 1804.88]  routes between all of
[1804.88 --> 1805.76]  these different scripts
[1805.76 --> 1806.92]  and the graphs and the
[1806.92 --> 1807.78]  scripts could call the
[1807.78 --> 1808.78]  graph so the scripts
[1808.78 --> 1810.48]  could get get data
[1810.48 --> 1811.78]  from the tensors and
[1811.78 --> 1812.54]  and all of that is
[1812.54 --> 1813.58]  that right yes
[1813.58 --> 1814.90]  correct it's a bit
[1814.90 --> 1815.70]  confusing here because
[1815.70 --> 1816.78]  we're saying graph we
[1816.78 --> 1818.08]  can say well that's
[1818.08 --> 1819.20]  why we renamed it to
[1819.20 --> 1820.68]  to to model inside
[1820.68 --> 1822.18]  Redis and Redis AI
[1822.18 --> 1823.20]  okay because we
[1823.20 --> 1824.12]  already have Redis
[1824.12 --> 1825.80]  graph that's why we
[1825.80 --> 1827.22]  yeah no that that
[1827.22 --> 1827.70]  makes sense I'm
[1827.70 --> 1828.36]  looking at one of
[1828.36 --> 1829.56]  these uh figures from
[1829.56 --> 1831.00]  the from the Redis AI
[1831.00 --> 1833.18]  uh docs and there's a
[1833.18 --> 1835.18]  graph blob uh uh
[1835.18 --> 1836.34]  section so that that
[1836.34 --> 1837.12]  makes sense that would
[1837.12 --> 1838.00]  uh that would help
[1838.00 --> 1839.60]  with the uh with the
[1839.60 --> 1840.50]  confusing terminology
[1840.50 --> 1841.32]  which is I guess
[1841.32 --> 1841.94]  always the hardest
[1841.94 --> 1842.60]  part of software
[1842.60 --> 1843.26]  engineering right
[1843.26 --> 1844.62]  I'll take that as a
[1844.62 --> 1846.40]  note to myself to
[1846.40 --> 1847.34]  update the documentation
[1847.34 --> 1847.84]  yep
[1847.84 --> 1849.36]  all right well this is
[1849.36 --> 1850.56]  this is truly practical
[1850.56 --> 1851.98]  AI so you know solving
[1851.98 --> 1853.44]  solving problems on
[1853.44 --> 1853.84]  the fly
[1853.84 --> 1869.92]  hey guess what brain
[1869.92 --> 1871.52]  science is officially
[1871.52 --> 1872.84]  launched episode number
[1872.84 --> 1873.54]  one is on the feed
[1873.54 --> 1874.90]  right now so head to
[1874.90 --> 1875.96]  change all.com slash
[1875.96 --> 1876.86]  brain science to
[1876.86 --> 1878.46]  listen to subscribe and
[1878.46 --> 1879.52]  to join us on this
[1879.52 --> 1880.64]  journey of exploring the
[1880.64 --> 1882.16]  human mind once again
[1882.16 --> 1883.48]  change law.com slash
[1883.48 --> 1884.86]  brain science or search
[1884.86 --> 1885.98]  for brain science in
[1885.98 --> 1886.84]  your favorite podcast
[1886.84 --> 1887.16]  app
[1887.16 --> 1908.04]  it looks like Redis AI is
[1908.04 --> 1909.84]  currently supporting PyTorch
[1909.84 --> 1911.22]  via LiveTorch and
[1911.22 --> 1912.68]  TensorFlow via live
[1912.68 --> 1914.40]  TensorFlow and also Onyx
[1914.40 --> 1916.40]  Runtime as backends.com slash
[1916.40 --> 1916.86]  Runtime as backends.com slash
[1916.86 --> 1917.80]  That's pretty awesome.com
[1917.80 --> 1920.02]  How big of a role did
[1920.02 --> 1921.02]  Onyx play in your
[1921.02 --> 1922.36]  strategy you know around
[1922.36 --> 1923.46]  modules and stuff and
[1923.46 --> 1924.66]  can you describe it a bit
[1924.66 --> 1926.02]  to our users on even
[1926.02 --> 1927.14]  defining what Onyx is
[1927.14 --> 1927.54]  actually?
[1928.04 --> 1928.62]  Onyx Runtime is
[1928.62 --> 1930.50]  effectively the Microsoft
[1930.50 --> 1932.04]  backend or the
[1932.04 --> 1933.92]  Microsoft variant and the
[1933.92 --> 1935.20]  reason why we added it
[1935.20 --> 1936.40]  was because we wanted to
[1936.40 --> 1938.04]  combine well we used to
[1938.04 --> 1939.40]  have Redis ML right so
[1939.40 --> 1940.42]  that was purely machine
[1940.42 --> 1942.12]  learning and and and
[1942.12 --> 1943.22]  Onyx Runtime effectively
[1943.22 --> 1945.16]  allows you to also serve
[1945.16 --> 1946.28]  machine learning models
[1946.28 --> 1948.00]  well compared to PyTorch
[1948.00 --> 1948.58]  for example and
[1948.58 --> 1948.84]  TensorFlow.
[1949.38 --> 1951.32]  So Onyx provides like a
[1951.32 --> 1953.04]  intermediate between a
[1953.04 --> 1953.80]  bunch of different
[1953.80 --> 1954.84]  frameworks right?
[1955.34 --> 1955.98]  Yes it does.
[1956.52 --> 1958.42]  Yeah so the am I right
[1958.42 --> 1959.56]  that you have like PyTorch
[1959.56 --> 1961.12]  and TensorFlow sort of the
[1961.12 --> 1962.74]  native libraries and then
[1962.74 --> 1964.34]  you kind of use Onyx for
[1964.34 --> 1966.06]  like everything else is
[1966.06 --> 1966.80]  that the kind of thought
[1966.80 --> 1967.44]  process or?
[1967.92 --> 1968.66]  That is a thought process
[1968.66 --> 1969.90]  exactly right so we can
[1969.90 --> 1971.68]  we can export we can use
[1971.68 --> 1972.50]  Onyx Runtime as an
[1972.50 --> 1973.30]  intermediate format
[1973.30 --> 1974.70]  effectively we're using it
[1974.70 --> 1976.28]  in certain ways where we
[1976.28 --> 1978.10]  for example want to fetch
[1978.10 --> 1979.32]  some models from Spark we
[1979.32 --> 1980.20]  can effectively then
[1980.20 --> 1982.56]  transform them in Onyx
[1982.56 --> 1984.04]  Runtime and then upload
[1984.04 --> 1985.80]  them into our backends.
[1985.98 --> 1987.78]  It's interesting to talk
[1987.78 --> 1988.52]  about these different
[1988.52 --> 1990.00]  backends because the
[1990.00 --> 1991.98]  model commands on how you
[1991.98 --> 1993.86]  execute or you effectively
[1993.86 --> 1995.96]  want to do your regression
[1995.96 --> 1997.94]  classification agnostic from
[1997.94 --> 2000.10]  from the backend that it's
[2000.10 --> 2001.36]  running for so when you
[2001.36 --> 2002.62]  would set your model when
[2002.62 --> 2003.82]  you say hey here at a
[2003.82 --> 2006.50]  say I want you to host or
[2006.50 --> 2008.14]  serve my model you would
[2008.14 --> 2009.94]  have to add some some
[2009.94 --> 2011.14]  some backend specific
[2011.14 --> 2013.62]  stuff but once you want to
[2013.62 --> 2015.96]  run it it doesn't know
[2015.96 --> 2016.96]  anymore which backend is
[2016.96 --> 2017.58]  effectively underneath
[2017.58 --> 2018.46]  obviously you're going to
[2018.46 --> 2019.74]  say I knows but it's your
[2019.74 --> 2021.10]  client doesn't need to
[2021.10 --> 2022.98]  specify hey run me this
[2022.98 --> 2025.38]  with TensorFlow so which
[2025.38 --> 2026.72]  makes that your your your
[2026.72 --> 2028.98]  client library or well
[2028.98 --> 2030.02]  your application developers
[2030.02 --> 2032.26]  that want to run want to
[2032.26 --> 2033.18]  work with your model or
[2033.18 --> 2035.56]  your your your data science
[2035.56 --> 2037.16]  trained model they they
[2037.16 --> 2039.18]  get a fixed API and as you
[2039.18 --> 2040.08]  as data scientists you
[2040.08 --> 2042.26]  decide well over time we
[2042.26 --> 2043.78]  think that our model in
[2043.78 --> 2046.48]  PyTorch is better than our
[2046.48 --> 2048.08]  model in TensorFlow you can
[2048.08 --> 2049.52]  just update that by setting
[2049.52 --> 2051.28]  or setting a new model with
[2051.28 --> 2053.00]  the same key inside Redis
[2053.00 --> 2056.00]  effectively Redis AI and
[2056.00 --> 2056.90]  and all your client
[2056.90 --> 2057.90]  libraries will still keep
[2057.90 --> 2059.18]  on working yeah that's
[2059.18 --> 2061.42]  that's pretty cool so I'm
[2061.42 --> 2063.20]  just trying to think so
[2063.20 --> 2064.90]  what you just said makes
[2064.90 --> 2066.22]  sense I'm trying to connect
[2066.22 --> 2068.32]  it to like you know
[2068.32 --> 2069.96]  practically if like let's
[2069.96 --> 2070.94]  say we take the example
[2070.94 --> 2072.70]  that I that I had before so
[2072.70 --> 2074.66]  I've got like my vector
[2074.66 --> 2076.76]  riser that I've I've created
[2076.76 --> 2077.90]  let's say in scikit-learn
[2077.90 --> 2079.54]  which I can convert to
[2079.54 --> 2083.10]  Onyx format and I want to
[2083.10 --> 2085.16]  and I create a bunch of
[2085.16 --> 2086.88]  knowledge graph or
[2086.88 --> 2088.24]  knowledge base article
[2088.24 --> 2091.68]  entries in in Redis what
[2091.68 --> 2092.84]  would be kind of the steps
[2092.84 --> 2095.14]  I would go through to to
[2095.14 --> 2096.72]  actually get something
[2096.72 --> 2098.42]  running to where I could
[2098.42 --> 2100.42]  take all of those articles
[2100.42 --> 2102.60]  in and then vectorize them
[2102.60 --> 2105.88]  with my with my scikit-learn
[2105.88 --> 2108.08]  TF-IDF vectorizer and then
[2108.08 --> 2110.50]  save them to back into Redis
[2110.50 --> 2112.04]  what what would be required
[2112.04 --> 2112.92]  for me to do would that be
[2112.92 --> 2114.38]  like writing some some
[2114.38 --> 2116.28]  Python would that be like
[2116.28 --> 2119.28]  some sort of custom client
[2119.28 --> 2120.22]  what what all would be
[2120.22 --> 2121.68]  involved there so it's a
[2121.68 --> 2122.76]  good question we do have a
[2122.76 --> 2123.66]  couple of client libraries
[2123.66 --> 2124.50]  so there's a there's a
[2124.50 --> 2125.76]  Python client for Redis
[2125.76 --> 2128.66]  AI there's also a conversion
[2128.66 --> 2130.16]  toolkit that we we kind of
[2130.16 --> 2132.14]  like created to help you
[2132.14 --> 2133.18]  convert in between these
[2133.18 --> 2134.14]  different models if that
[2134.14 --> 2135.54]  would be necessary so via
[2135.54 --> 2137.46]  Onyx runtime so so which we
[2137.46 --> 2139.04]  can probably share later on
[2139.04 --> 2139.74]  or at the end of the
[2139.74 --> 2142.82]  podcast so from within your
[2142.82 --> 2144.62]  Python code you could
[2144.62 --> 2146.32]  effectively just publish
[2146.32 --> 2148.06]  your your model inside
[2148.06 --> 2149.44]  Redis AI you could push it
[2149.44 --> 2150.38]  directly you could connect
[2150.38 --> 2152.14]  hey here's my database I
[2152.14 --> 2153.64]  want to push this model
[2153.64 --> 2156.00]  obviously that there might
[2156.00 --> 2156.82]  be other ways that you
[2156.82 --> 2157.80]  still want to want to do
[2157.80 --> 2158.60]  this right you might have
[2158.60 --> 2159.54]  some some intermediate
[2159.54 --> 2161.24]  some some versioning of
[2161.24 --> 2162.14]  your or exporting your
[2162.14 --> 2163.56]  model as a binary so you
[2163.56 --> 2165.04]  can actually version it and
[2165.04 --> 2165.88]  then you could ship it to
[2165.88 --> 2167.98]  to to DevOps so they can
[2167.98 --> 2169.56]  effectively well there is
[2169.56 --> 2170.72]  there is clearly there is
[2170.72 --> 2171.52]  there is a component
[2171.52 --> 2172.96]  missing there to make this
[2172.96 --> 2174.56]  easily right to to to to
[2174.56 --> 2176.80]  to version your model and
[2176.80 --> 2177.64]  to effectively say hey this
[2177.64 --> 2178.56]  is now the new release we
[2178.56 --> 2179.60]  want to publish inside
[2179.60 --> 2182.22]  Redis AI and you could do
[2182.22 --> 2183.34]  it directly you could say
[2183.34 --> 2185.34]  hey here's my my my client
[2185.34 --> 2186.98]  and and I directly push it
[2186.98 --> 2188.50]  to Redis and then
[2188.50 --> 2189.74]  afterwards if you want to
[2189.74 --> 2192.02]  want to do that you want to
[2192.02 --> 2193.40]  run that model you can once
[2193.40 --> 2194.50]  again use the same client
[2194.50 --> 2196.08]  and however that client
[2196.08 --> 2197.56]  can also be wrapped in any
[2197.56 --> 2198.62]  other application that wants
[2198.62 --> 2200.48]  to consume that model so
[2200.48 --> 2201.42]  I'm just kind of curious
[2201.42 --> 2202.18]  we've kind of talked a
[2202.18 --> 2202.88]  little bit about some of
[2202.88 --> 2204.02]  these use cases are there
[2204.02 --> 2205.18]  any before we move on are
[2205.18 --> 2206.00]  there any other really
[2206.00 --> 2207.44]  typical use cases that
[2207.44 --> 2208.82]  you're seeing Redis AI being
[2208.82 --> 2209.90]  used for that we haven't
[2209.90 --> 2211.36]  already covered one of the
[2211.36 --> 2212.68]  things where we think is
[2212.68 --> 2213.90]  is a transaction
[2213.90 --> 2215.52]  classification and the
[2215.52 --> 2216.72]  reason why we think that's
[2216.72 --> 2219.02]  a very good fit is because
[2219.02 --> 2221.44]  it's it's it's a high volume
[2221.44 --> 2223.68]  high number of requests you
[2223.68 --> 2224.92]  want to do and you only
[2224.92 --> 2226.28]  have limited time to do so
[2226.28 --> 2227.56]  so you don't want to waste
[2227.56 --> 2229.14]  time to find all your
[2229.14 --> 2230.38]  metadata or to fetch all
[2230.38 --> 2231.54]  your metadata from user
[2231.54 --> 2233.30]  profiles that live in
[2233.30 --> 2234.46]  potentially in different
[2234.46 --> 2236.34]  data source so I think
[2236.34 --> 2237.58]  transaction classification
[2237.58 --> 2238.82]  some some fraud detection
[2238.82 --> 2241.50]  are the ones we think that
[2241.50 --> 2243.54]  that will really benefit from
[2243.54 --> 2245.28]  from that data locality and
[2245.28 --> 2246.46]  the scale we can offer with
[2246.46 --> 2249.18]  with Redis I have a kind of
[2249.18 --> 2252.36]  I guess more philosophical
[2252.36 --> 2255.06]  question to to ask so I
[2255.06 --> 2255.82]  would say that like
[2255.82 --> 2257.98]  probably at least from my
[2257.98 --> 2259.12]  experience like there's
[2259.12 --> 2260.64]  probably a lot of like
[2260.64 --> 2262.66]  maybe even most like
[2262.66 --> 2263.78]  software engineers these
[2263.78 --> 2264.90]  days like they've heard at
[2264.90 --> 2265.96]  least heard of Redis or
[2265.96 --> 2267.16]  they may even be familiar
[2267.16 --> 2269.08]  or worked with it but maybe
[2269.08 --> 2270.54]  like data scientists and AI
[2270.54 --> 2271.84]  people are like less
[2271.84 --> 2274.16]  familiar with Redis so do
[2274.16 --> 2275.68]  you envision I guess my
[2275.68 --> 2277.52]  question is like there's a
[2277.52 --> 2278.60]  lot of people already using
[2278.60 --> 2279.96]  Redis for certain things
[2279.96 --> 2281.08]  like you've already
[2281.08 --> 2281.98]  mentioned like message
[2281.98 --> 2283.26]  brokers and other things
[2283.26 --> 2284.74]  where they they have data
[2284.74 --> 2286.10]  already flowing through
[2286.10 --> 2287.96]  Redis do you think that
[2287.96 --> 2289.74]  it's likely that kind of
[2289.74 --> 2290.74]  the software engineers
[2290.74 --> 2292.74]  already using Redis will
[2292.74 --> 2295.26]  kind of be able to kind of
[2295.26 --> 2297.24]  bolt on AI sort of
[2297.24 --> 2298.70]  functionality into those
[2298.70 --> 2299.94]  existing applications like
[2299.94 --> 2300.54]  maybe they want to
[2300.54 --> 2301.48]  introduce like fraud
[2301.48 --> 2302.72]  detection in terms of
[2302.72 --> 2304.06]  their the traffic going
[2304.06 --> 2305.02]  across their network or
[2305.02 --> 2306.60]  something like that or are
[2306.60 --> 2308.68]  you kind of hoping to
[2308.68 --> 2310.02]  kind of position Redis
[2310.02 --> 2311.44]  AI more as like a
[2311.44 --> 2312.50]  general purpose sort of
[2312.50 --> 2313.62]  model serving framework
[2313.62 --> 2315.76]  where you know AI or
[2315.76 --> 2316.72]  data science people when
[2316.72 --> 2317.58]  they go out looking for
[2317.58 --> 2318.50]  the best way to serve
[2318.50 --> 2320.08]  their their model kind of
[2320.08 --> 2321.58]  Redis AI is up there with
[2321.58 --> 2322.72]  like you know TensorFlow
[2322.72 --> 2324.48]  serving or whatever else it
[2324.48 --> 2325.58]  is do you think that
[2325.58 --> 2327.40]  there's like I don't know
[2327.40 --> 2329.02]  maybe it's unclear right now
[2329.02 --> 2330.04]  in terms of which direction
[2330.04 --> 2331.64]  it was go but it would go
[2331.64 --> 2332.58]  but I was curious to hear
[2332.58 --> 2334.38]  your thoughts I think we
[2334.38 --> 2335.62]  would love it to be both
[2335.62 --> 2337.48]  effectively obviously but
[2337.48 --> 2341.32]  so I do think that we
[2341.32 --> 2342.08]  still have to build some
[2342.08 --> 2343.04]  tooling around this right
[2343.04 --> 2344.34]  so to make the full
[2344.34 --> 2346.08]  fledged model serving
[2346.08 --> 2347.34]  engine to make it very
[2347.34 --> 2349.28]  practical by the way one
[2349.28 --> 2350.00]  thing I also want to
[2350.00 --> 2350.94]  mention here is that
[2350.94 --> 2352.74]  we're effectively not all
[2352.74 --> 2354.58]  development of Redis AI is
[2354.58 --> 2356.16]  done by Redis Labs it's
[2356.16 --> 2357.72]  also done by TensorWork so
[2357.72 --> 2359.00]  we're partnering with them
[2359.00 --> 2361.74]  and TensorWork is a
[2361.74 --> 2362.84]  company that is building
[2362.84 --> 2364.12]  kind of like several tools
[2364.12 --> 2367.92]  for AI purposes so one of
[2367.92 --> 2368.72]  the things they're building
[2368.72 --> 2369.66]  is this might be
[2369.66 --> 2370.32]  interesting for you guys
[2370.32 --> 2371.58]  to also look into is a
[2371.58 --> 2373.56]  versioning system for data
[2373.56 --> 2374.94]  so you could effectively
[2374.94 --> 2379.06]  well like Git you could
[2379.06 --> 2380.00]  effectively branch and
[2380.00 --> 2382.24]  make PRs on top of your
[2382.24 --> 2384.24]  data yeah the data you
[2384.24 --> 2385.12]  want to serve to well it's
[2385.12 --> 2387.22]  called Hangar and I'll also
[2387.22 --> 2388.72]  well recommend you to look
[2388.72 --> 2391.40]  into it but over time
[2391.40 --> 2392.54]  effectively we think we will
[2392.54 --> 2394.44]  get a very nice toolkit
[2394.44 --> 2395.96]  and Redis AI will be one of
[2395.96 --> 2397.08]  those pieces into it right
[2397.08 --> 2398.76]  so you want to be I think
[2398.76 --> 2400.80]  combined with TensorWork we
[2400.80 --> 2401.62]  would like to make the
[2401.62 --> 2402.58]  story where we can say hey
[2402.58 --> 2403.52]  you've got a complete
[2403.52 --> 2405.76]  solution towards you for
[2405.76 --> 2408.00]  serving your model on the
[2408.00 --> 2409.00]  other hand on the other
[2409.00 --> 2410.96]  end of the spectrum is in
[2410.96 --> 2412.48]  that in that case well I
[2412.48 --> 2413.22]  don't know who the personas
[2413.22 --> 2414.28]  would be for sure it's a
[2414.28 --> 2416.56]  data scientist but also for
[2416.56 --> 2417.64]  example DevOps people that
[2417.64 --> 2418.80]  want to have a good solution
[2418.80 --> 2421.20]  for preserving those those
[2421.20 --> 2422.58]  models on the other hand
[2422.58 --> 2423.56]  there is potentially also
[2423.56 --> 2425.08]  data engineers and our
[2425.08 --> 2428.06]  software engineers who do
[2428.06 --> 2430.04]  already have Redis as a as a
[2430.04 --> 2431.62]  tool in their toolbox and
[2431.62 --> 2432.52]  with these modules they can
[2432.52 --> 2434.36]  make all these beautiful new
[2434.36 --> 2436.70]  new applications so ways you
[2436.70 --> 2440.36]  could use Redis AI combining
[2440.36 --> 2441.58]  them for example with other
[2441.58 --> 2442.76]  modules so if you have a search
[2442.76 --> 2444.52]  application and you want to
[2444.52 --> 2446.12]  say well hey I have the these
[2446.12 --> 2447.92]  top 100 results here or have
[2447.92 --> 2450.10]  200 results why don't I run
[2450.10 --> 2452.00]  them again through some model
[2452.00 --> 2454.46]  to update or to fine tune the
[2454.46 --> 2455.44]  scoring in between those
[2455.44 --> 2457.24]  results might have a big impact
[2457.24 --> 2459.58]  on the user experience so we
[2459.58 --> 2461.08]  hope in that way this is just
[2461.08 --> 2462.86]  an example right but we hope in
[2462.86 --> 2464.28]  that way that we will we will
[2464.28 --> 2466.24]  enable that many new or
[2466.24 --> 2467.64]  interesting applications will
[2467.64 --> 2467.92]  appear.
[2468.62 --> 2470.20]  So we're kind of already talking
[2470.20 --> 2471.18]  about you know what you're
[2471.18 --> 2472.50]  thinking of going forward so I'll
[2472.50 --> 2474.12]  just go ahead and you know ask
[2474.12 --> 2475.42]  you know what what is your
[2475.42 --> 2476.98]  development roadmap look like
[2476.98 --> 2478.42]  kind of what future directions
[2478.42 --> 2479.98]  are you interested in taking
[2479.98 --> 2481.82]  and and I know that we've you
[2481.82 --> 2483.24]  know obviously there are
[2483.24 --> 2484.40]  features that you're going to
[2484.40 --> 2485.72]  have in mind but you know it
[2485.72 --> 2486.86]  sounds like you know we've
[2486.86 --> 2487.72]  really covered a lot of
[2487.72 --> 2489.88]  tooling are there any as part
[2489.88 --> 2490.88]  of that are there any kind of
[2490.88 --> 2492.32]  higher level applications that
[2492.32 --> 2493.78]  might sit on top of Redis as
[2493.78 --> 2494.64]  part of that development
[2494.64 --> 2495.10]  roadmap?
[2495.72 --> 2497.06]  Yes we should definitely look
[2497.06 --> 2498.48]  into that and we're open for
[2498.48 --> 2500.14]  for for lots of tips and
[2500.14 --> 2501.18]  recommendations on top of
[2501.18 --> 2503.24]  that for that we do have a
[2503.24 --> 2504.24]  kind of like a roadmap for
[2504.24 --> 2505.68]  Redis AI itself we do have a
[2505.68 --> 2506.36]  couple of features that we
[2506.36 --> 2507.76]  want to add so we would like
[2507.76 --> 2509.00]  this Redis Gears module to
[2509.00 --> 2511.32]  talk neatly to to Redis AI
[2511.32 --> 2512.76]  that might be interesting to
[2512.76 --> 2514.62]  well yeah you have the script
[2514.62 --> 2516.18]  but you could also fetch data
[2516.18 --> 2517.44]  more easily or maybe even
[2517.44 --> 2519.20]  connect to to to other data
[2519.20 --> 2520.74]  sources outside Redis.
[2521.18 --> 2522.98]  There is also some batching
[2522.98 --> 2525.34]  that we want to to to have so
[2525.34 --> 2526.52]  so that we can effectively you
[2526.52 --> 2528.16]  can run several models and in
[2528.16 --> 2529.88]  one go so there will be also
[2529.88 --> 2531.00]  one other thing that we want to
[2531.00 --> 2533.12]  add is some tooling to get some
[2533.12 --> 2535.32]  performance statistics about
[2535.32 --> 2536.66]  how well your your model is
[2536.66 --> 2538.40]  running or behaving so what is
[2538.40 --> 2540.94]  the the average time and and
[2540.94 --> 2542.68]  the beauty about well the beauty
[2542.68 --> 2544.48]  that we we hope to achieve is
[2544.48 --> 2545.22]  that well there's already an
[2545.22 --> 2547.16]  entire ecosystem around Redis so
[2547.16 --> 2548.58]  some guy somehow will have
[2548.58 --> 2549.64]  written for example some
[2549.64 --> 2552.92]  Prometheus connector right and so
[2552.92 --> 2554.18]  if we so if you can connect that
[2554.18 --> 2555.78]  up then you immediately get a
[2555.78 --> 2557.30]  some Grafana dashboard out of the
[2557.30 --> 2559.00]  box that could show how well your
[2559.00 --> 2560.82]  model is behaving that is one
[2560.82 --> 2562.98]  thing I'm sure we will have many
[2562.98 --> 2564.54]  more there's some some versioning
[2564.54 --> 2565.60]  potentially of models that we
[2565.60 --> 2567.10]  also would like to do so we can
[2567.10 --> 2569.24]  have or we can keep track of
[2569.24 --> 2570.88]  several models or versions so you
[2570.88 --> 2572.88]  can have you can switch in between
[2572.88 --> 2574.94]  them or do a B testing in between
[2574.94 --> 2576.00]  them that could also be an
[2576.00 --> 2578.44]  interesting thing to look into in
[2578.44 --> 2578.78]  the future.
[2579.34 --> 2581.76]  Awesome so as we kind of wrap up
[2581.76 --> 2583.98]  here I was wondering if you could
[2583.98 --> 2586.28]  just share kind of maybe where I
[2586.28 --> 2588.02]  think on one front like where
[2588.02 --> 2589.46]  people that are interested in
[2589.46 --> 2591.50]  experimenting with Redis AI where
[2591.50 --> 2593.48]  where they should go to kind of get
[2593.48 --> 2595.78]  up and running I guess and then
[2595.78 --> 2598.16]  second I'm sure that it's I mean
[2598.16 --> 2600.16]  there's a lot of work to do there's
[2600.16 --> 2601.18]  a lot of tooling that's needed
[2601.18 --> 2602.66]  integrations all of that stuff so
[2602.66 --> 2604.04]  maybe there's people out there that
[2604.04 --> 2608.36]  have used Redis or or not but that
[2608.36 --> 2610.54]  would be willing to to contribute so
[2610.54 --> 2612.62]  where where should they go to kind
[2612.62 --> 2614.50]  of get get plugged in so on one
[2614.50 --> 2616.64]  front you know people that want to
[2616.64 --> 2618.76]  be potentially users and then maybe
[2618.76 --> 2620.70]  people that want to contribute as
[2620.70 --> 2622.76]  well what's the best way for those
[2622.76 --> 2624.56]  those groups to get involved and
[2624.56 --> 2625.14]  find out more.
[2625.64 --> 2627.14]  So if you just want to get started
[2627.14 --> 2628.82]  with it there's a Docker container
[2628.82 --> 2631.34]  effectively all the info is on
[2631.34 --> 2634.12]  redis.io to to quick start that is
[2634.12 --> 2634.80]  for example there's a Docker
[2634.80 --> 2636.84]  container you can just pull it it
[2636.84 --> 2639.36]  comes preloaded with with with all
[2639.36 --> 2640.46]  the backends so it comes with
[2640.46 --> 2643.16]  TensorFlow Pythorch and OX runtime
[2643.16 --> 2644.50]  backends and you can just get
[2644.50 --> 2646.30]  started with with that and if you
[2646.30 --> 2647.94]  would like to to contribute there is
[2647.94 --> 2649.34]  a Google groups where you can
[2649.34 --> 2651.06]  effectively well all Redis.io right
[2651.06 --> 2651.82]  so if you would search for the
[2651.82 --> 2653.34]  Google group already say I can
[2653.34 --> 2654.60]  effectively reach out to to all
[2654.60 --> 2655.64]  developers that are working on
[2655.64 --> 2657.58]  Redis.io and contribute there right
[2657.58 --> 2660.08]  to get a project you feel free to
[2660.08 --> 2662.12]  open issues I mean we would love
[2662.12 --> 2663.78]  that right all the feedback you guys
[2663.78 --> 2665.34]  can give us would be would be highly
[2665.34 --> 2667.50]  appreciated I think we actually we
[2667.50 --> 2669.84]  react quite quickly to those those
[2669.84 --> 2671.06]  two right we would we would love to
[2671.06 --> 2672.48]  help or to make Redis.io a
[2672.48 --> 2674.68]  success. Awesome yeah I think that
[2674.68 --> 2677.24]  that's that's great and of course
[2677.24 --> 2679.48]  we'll post all of those links that
[2679.48 --> 2680.86]  were just mentioned on our show
[2680.86 --> 2683.30]  notes and of course if you if you're
[2683.30 --> 2685.22]  having trouble finding things or want
[2685.22 --> 2687.04]  to kind of follow up with questions
[2687.04 --> 2689.44]  find us on our slack team at
[2689.44 --> 2691.84]  changelog.com slash community or
[2691.84 --> 2693.82]  LinkedIn page we're happy to make the
[2693.82 --> 2695.48]  connections for you forward on links
[2695.48 --> 2697.58]  but I I thoroughly enjoyed today's
[2697.58 --> 2699.64]  conversation I was able to like nerd
[2699.64 --> 2701.88]  out a bit and think about my own my own
[2701.88 --> 2703.54]  problems a little bit so I appreciate
[2703.54 --> 2706.16]  you being being patient with me Peter
[2706.16 --> 2707.64]  and sharing so much great information
[2707.64 --> 2709.34]  you're welcome no I really enjoyed it
[2709.34 --> 2711.18]  too so it's a it was an honor for me to
[2711.18 --> 2713.32]  be here so thank you for for asking me
[2713.32 --> 2717.24]  all right thank you for tuning into this
[2717.24 --> 2719.42]  episode of Practical AI if you enjoyed
[2719.42 --> 2721.20]  this show do us a favor go on iTunes
[2721.20 --> 2723.42]  give us a rating go in your podcast app
[2723.42 --> 2725.02]  and favorite it if you are on Twitter
[2725.02 --> 2726.72]  or social network share a link with a
[2726.72 --> 2728.20]  friend whatever you gotta do share the
[2728.20 --> 2729.76]  show with a friend if you enjoyed it and
[2729.76 --> 2731.54]  the bandwidth for changelog is provided
[2731.54 --> 2734.04]  by fastly learn more at fastly.com and
[2734.04 --> 2735.84]  we catch our errors before our users do
[2735.84 --> 2737.74]  here at changelog because of rollbar check
[2737.74 --> 2740.46]  them out at rollbar.com slash changelog and
[2740.46 --> 2743.22]  we're hosted on linode cloud servers head to
[2743.22 --> 2745.22]  linode.com slash changelog check them out
[2745.22 --> 2748.04]  support this show this episode is hosted by
[2748.04 --> 2750.98]  Daniel Whitenack and Chris Benson the music is
[2750.98 --> 2753.22]  by Breakmaster Cylinder and you can find
[2753.22 --> 2756.42]  more shows just like this at changelog.com when
[2756.42 --> 2758.62]  you go there pop in your email address get
[2758.62 --> 2760.26]  our weekly email keeping you up to date
[2760.26 --> 2762.88]  with the news and podcasts for developers in
[2762.88 --> 2765.26]  your inbox every single week thanks for
[2765.26 --> 2766.64]  tuning in we'll see you next week
[2766.64 --> 2768.64]  you
