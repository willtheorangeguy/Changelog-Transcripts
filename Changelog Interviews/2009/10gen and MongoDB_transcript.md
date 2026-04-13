[0.00 --> 20.84]  Hello and welcome to 007 of the Changelove, that's 007.
[20.96 --> 21.84]  I think you know who I am.
[21.88 --> 23.18]  My name is Adam Stachowiak.
[23.18 --> 25.28]  You can check me out on Twitter at AdamStack.
[25.48 --> 26.78]  I got my boy Wynn here with me.
[26.90 --> 27.72]  We had an awesome interview.
[28.36 --> 28.96]  It was a lot of fun.
[28.96 --> 30.24]  It was a lot of fun.
[30.52 --> 31.96]  And I'm Wynn Netherland, for those that don't know.
[32.46 --> 35.12]  You can reach me on Twitter at Penguin, P-E-N-G-W-Y-N-N.
[36.00 --> 40.92]  And this week we talked to Mike Dieroff from MongoDB, from 10Gen, the company behind MongoDB,
[41.10 --> 42.52]  which is a lot of fun.
[42.72 --> 45.06]  It's a very cool database application.
[45.20 --> 45.70]  Have you used this yet?
[46.54 --> 49.36]  Just in some stuff with you, that's pretty much it.
[49.56 --> 56.52]  But beyond just this, I think you might have some sort of fetish with James Bond and 007 with this.
[56.52 --> 59.28]  And I also have a gem out there called Octopussy.
[60.00 --> 60.92]  Octopussy, that's right.
[61.02 --> 63.16]  It's a good hub gem that we've created.
[63.80 --> 64.74]  You know, I like James Bond.
[64.86 --> 65.52]  I like the movies.
[66.20 --> 68.76]  The older ones, I think, are better than the more recent ones.
[69.02 --> 75.04]  But I couldn't resist doing the whole James Bond takeoff on 007, right?
[75.36 --> 77.78]  Anytime you have 007, you've got to represent.
[77.78 --> 83.82]  Our condolences to Stephen Bristol, because I remember, I think it was in Goldeneye, 007 kills 006.
[86.52 --> 87.56]  Oh, poor Stephen.
[88.68 --> 93.36]  So we're going to be in, I guess, a little hiatus here for Christmas over the next week?
[93.60 --> 93.86]  Yep.
[94.88 --> 98.54]  Got some travel planned to go see some family, and I'm sure you've got some things going on yourself.
[98.98 --> 100.52]  You're going to the Great White North, right?
[100.94 --> 102.68]  Yeah, well, yeah, you'd almost call it that.
[102.68 --> 103.92]  I'm heading into Canada first.
[104.02 --> 106.94]  I'm flying in, dropping into Toronto tomorrow, actually.
[107.10 --> 108.42]  Tomorrow I take off, tomorrow morning.
[109.04 --> 116.78]  And by, I guess, around 2.30 in the afternoon, Eastern Standard Time, since we're in Central here, I'll be in Toronto.
[117.10 --> 118.06]  I'll be picking up my car.
[118.14 --> 119.34]  I'll be picking up my beautiful daughter.
[119.54 --> 121.94]  And we'll be driving down to see some family in Pennsylvania.
[122.84 --> 127.40]  We'll hang out there for a couple weeks and then back up to TO and back down to Houston.
[128.22 --> 128.88]  Good deal.
[129.10 --> 130.46]  Well, we've got a great interview this week.
[130.46 --> 132.66]  I think it was a lot of fun talking to Mike.
[133.48 --> 135.16]  And without further ado, let's get to it.
[142.12 --> 145.88]  Hi, we're talking today with Mike Duroff from TenGen about MongoDB.
[146.22 --> 147.38]  Mike, what's your role at TenGen?
[147.50 --> 149.42]  And give us a little background on the MongoDB project.
[150.58 --> 155.12]  Yeah, so TenGen provides support and sponsors the development of MongoDB.
[155.12 --> 161.78]  And at TenGen, my primary focus is working on the Ruby and Python drivers for MongoDB.
[162.88 --> 166.06]  So that's a little bit of background of what I do there.
[166.78 --> 171.60]  And as far as MongoDB itself, for those folks that may not know, what exactly is MongoDB?
[171.60 --> 177.88]  Yeah, so MongoDB is an open source, high performance, schema-free, document-oriented database.
[178.18 --> 180.12]  So there's a lot of buzzwords there.
[180.34 --> 188.70]  But I think the point is that there's recently been this trend towards using non-relational databases.
[189.24 --> 191.84]  Some people are referring to it as the NoSQL movement.
[191.84 --> 197.58]  And I think the reasons for that are that there are some shortcomings in terms of the traditional RDBMS,
[197.84 --> 201.76]  in terms of both its ability to scale out horizontally,
[202.00 --> 207.22]  and also in terms of flexibility for developers working within the relational paradigm.
[208.18 --> 215.16]  And so we've seen a bunch of different types of products that are trying to address this in the non-relational space.
[215.16 --> 220.58]  So there's things like key value stores, which have a pretty simplistic data model,
[220.70 --> 222.52]  basically put and get on a single key.
[223.06 --> 228.28]  But that allows them to scale very well and very easily, and also to offer pretty good performance.
[228.70 --> 235.46]  And I think with MongoDB, the goal is to sort of bridge the gap between those sort of key value stores,
[235.52 --> 238.58]  which have this simple data model, and something like an RDBMS,
[238.80 --> 244.44]  which has a much more complicated data model and is full of features.
[244.44 --> 249.30]  And so with MongoDB, we're sort of trying to maintain the scalability and performance of the key value stores
[249.30 --> 254.90]  and add some functionality more like what you'd see out of a relational database.
[255.56 --> 258.50]  You know, I discovered Mongo early 2009.
[258.92 --> 259.94]  How old is the project?
[261.18 --> 269.74]  Yeah, so MongoDB actually comes out of this full-stack cloud computing platform that we were working on at Tengen.
[269.74 --> 275.80]  And so originally, when I joined the company a couple years ago,
[275.84 --> 281.26]  we were working on this cloud computing platform, sort of like a Google App Engine, basically.
[281.74 --> 287.40]  There was an application server, a load balancer, and a database, which became MongoDB.
[287.40 --> 291.56]  And so that project was also open source.
[291.96 --> 299.26]  And that was started in the end of 2007, I guess.
[300.32 --> 303.82]  Or end of 2008, sorry.
[304.86 --> 305.36]  2007.
[305.98 --> 307.52]  Sorry, end of 2007.
[307.52 --> 316.20]  And so we didn't ever see sort of the traction that we wanted from developers
[316.20 --> 319.40]  with switching their entire application over to this new stack.
[320.08 --> 325.04]  And so eventually, around this time last year, actually, in the end of 2008,
[325.74 --> 331.02]  we decided to stop focusing on this full-stack platform
[331.02 --> 334.96]  and start focusing on, you know, a much more narrow problem.
[334.96 --> 340.66]  And we decided that sort of the most interesting piece of technology we had built at the time was the database.
[341.22 --> 343.74]  So we split the database out from the rest of the project
[343.74 --> 348.32]  and developed some drivers for all these different languages
[348.32 --> 351.92]  and released it as a standalone open source project.
[352.60 --> 356.42]  And that was the first release was in the beginning of February of this year.
[357.30 --> 360.14]  And so since then, we've seen a lot of traction.
[360.14 --> 365.46]  And, yeah, so it looks like it was a good decision to make that move.
[365.58 --> 369.28]  But the project itself was started, like I said, in the end of 2007.
[369.58 --> 371.90]  So it's been around for about two years now.
[372.12 --> 376.70]  And it's been used in production for almost as long as it's been around.
[376.92 --> 380.20]  So it does have some time behind it.
[380.94 --> 382.86]  In my time and my exposure to the project,
[382.92 --> 387.14]  I'm amazed at how fast you guys turn out releases and especially bug fixes.
[387.28 --> 388.00]  How big is your team?
[388.00 --> 391.10]  So the team right now is actually growing.
[391.84 --> 395.82]  We do have open positions if people out there are interested.
[397.88 --> 403.14]  And for most of this year, we've been a pretty small team, around four.
[404.22 --> 407.66]  And recently, we've grown.
[407.84 --> 412.58]  So we're up to six full-time developers now in hiring.
[412.58 --> 417.12]  And we've hired some additional people as well, besides developers.
[418.82 --> 420.68]  But, yeah, the team is growing rapidly.
[421.06 --> 423.20]  And it's a great bunch of people.
[423.32 --> 424.38]  So it's been fun working here.
[425.28 --> 430.12]  What kind of insight do you have behind the Series A and Series B rounds that you guys have recently secured?
[430.12 --> 435.24]  Yeah, so I'm not a business person.
[435.34 --> 435.82]  I'm a developer.
[436.04 --> 439.00]  So I don't know how much my insight is worth.
[439.30 --> 447.26]  But I think it is interesting to see that it's almost like the space is sort of growing up a little bit.
[447.26 --> 451.82]  We recently closed, as you mentioned, a Series B round.
[452.22 --> 458.36]  And a couple of other companies that are sort of related in the space have raised a couple rounds recently as well.
[458.78 --> 460.48]  So there's people.
[460.58 --> 463.22]  I'd say it was $3.4 million in November.
[463.36 --> 463.98]  That's huge.
[464.14 --> 464.46]  Yeah.
[464.46 --> 475.36]  And for open source to start to collect that kind of money towards focusing on these high-performance type of products like you guys are doing, that's a pretty wild story.
[476.04 --> 476.22]  Yeah.
[476.34 --> 485.40]  So, I mean, I think it's sort of a testament to the fact that – to where we see this space going.
[485.40 --> 490.84]  So, like I said, we've seen some significant adoption over the past year.
[491.42 --> 500.68]  And I think that we're going to see even more over the next couple months as people start to – people who maybe haven't heard of MongoDB start to learn about it and get interested.
[500.88 --> 509.14]  And I think there's – that this is technology that can be applied to a vast array of projects out there.
[509.28 --> 513.34]  So hopefully we'll continue to see it pick up in terms of usage.
[513.34 --> 519.56]  I'm just browsing the production deployments page, and that's – I had an update since I was last out there.
[519.66 --> 522.38]  I guess Discuss is the biggest name maybe outside of EA.
[523.04 --> 525.38]  Any insight to how those guys are using Mongo?
[526.28 --> 526.60]  Yeah.
[526.66 --> 531.02]  So Discuss, I'm actually not too sure of how they're using it.
[531.04 --> 538.82]  I think that I talked with those guys back in maybe June at a Python meetup.
[538.82 --> 544.78]  And at that time they were using it for a URL shortening service, I think.
[545.02 --> 550.32]  So not – at that time it wasn't their main, you know, where the comments are stored.
[550.78 --> 553.84]  But at the time I think they were talking about moving more stuff onto it.
[554.00 --> 559.36]  So I really am not sure how far along they are with that or what is actually running on it now.
[559.64 --> 563.08]  Some of the other big names on there are SourceForge is using it.
[563.08 --> 572.90]  They've been using it since May as well, and they've been serving up – basically all of their project pages are stored entirely in MongoDB now.
[574.58 --> 576.10]  GitHub is also on there.
[576.16 --> 580.72]  They're using it for some internal stuff right now and looking at expanding what they're using it for.
[580.72 --> 582.16]  And EA.
[582.30 --> 593.02]  EA is using it for their rupture site, which is, I guess, there's, you know, high score stuff and sort of community around their games.
[593.52 --> 599.00]  And so, yeah, so we've seen some high profile sites pick it up recently as well.
[600.04 --> 606.90]  You know, one thing that's, I guess, amazed me at all of the NoSQL databases, and I don't think we've named any of them.
[606.90 --> 608.64]  Maybe we can discuss those in a moment.
[609.34 --> 614.24]  Couch and some of the others being, I guess, the major players.
[614.40 --> 620.00]  But the common line between these seems to be JavaScript for the internal scripting language.
[620.10 --> 623.44]  Can you speak to why you guys chose JavaScript and what it's meant?
[623.96 --> 626.18]  Yeah, so it's sort of funny in our case.
[627.32 --> 634.42]  We chose JavaScript, and it sort of fell out of this cloud computing platform that I was talking about earlier.
[634.42 --> 641.80]  So this cloud computing platform was multi-language, but the first language we supported was server-side JavaScript.
[642.64 --> 652.56]  And the reason for that is that at the time we felt that JavaScript is a language that most web developers already know, at least to some degree.
[653.18 --> 659.02]  And it's also a pretty nice language, and it's pretty easy to get started with.
[659.14 --> 660.64]  So we thought it made sense there.
[660.64 --> 663.96]  And so as part of that, the database also spoke JavaScript.
[664.82 --> 675.20]  So then when we pulled out MongoDB as its own standalone project, there was already a bunch of useful features that were built on JavaScript, like the database shell, for example.
[675.32 --> 681.18]  So we have this administrative shell that comes with the distribution, and that's all JavaScript.
[681.50 --> 685.02]  So you can explore your database, but you can do so programmatically.
[685.02 --> 686.54]  So it's sort of nice.
[687.12 --> 691.94]  And so we had already had a lot of this stuff built, and we stuck with JavaScript.
[692.52 --> 698.48]  So right now there's an embedded SpiderMonkey interpreter in the database.
[698.60 --> 700.76]  We're thinking about possibly switching to V8.
[702.92 --> 710.56]  But yeah, I think JavaScript makes a lot of sense because, like I said, it sort of is this least common denominator for a lot of web developers.
[710.56 --> 713.66]  And it's a pretty nice language to work with.
[713.74 --> 714.76]  It's pretty easy to work with.
[715.12 --> 717.24]  Is there any support for JavaScript outside the shell?
[718.26 --> 718.60]  Yeah.
[718.86 --> 724.70]  So in addition to using it in the shell, like I said, there's an embedded JavaScript interpreter in the database.
[724.90 --> 727.20]  So there's a couple ways that that gets used.
[727.20 --> 738.36]  You can do what's called an eval, where you actually send arbitrary JavaScript code that gets executed on the database server itself.
[738.62 --> 748.30]  So that can be useful for doing some more complex operations without network turnaround in between, client-server interaction in between.
[748.30 --> 751.50]  And there's also a where clause.
[751.98 --> 760.90]  So MongoDB has a nice query syntax with a bunch of interesting query operators, and it does have index support and all that sort of stuff.
[761.10 --> 767.06]  But if our query syntax doesn't quite express things the way you need to, you can use arbitrary JavaScript.
[767.32 --> 773.26]  So you can pass a where clause that will get evaluated against all of your documents and decide which ones to be returned.
[773.26 --> 779.40]  So I guess in both of those cases, that would be passing JavaScript from another language binding like Ruby or Python.
[779.72 --> 786.72]  Any support for like a Node.js type of setup where you would call Mongo directly from a server-side JavaScript?
[787.42 --> 787.62]  Yeah.
[787.78 --> 794.16]  So there are some people who are working on a Node.js integration layer.
[794.16 --> 804.48]  We actually, Elliot has pulled out some of the internal V8 code and made it into, from the shell, and made it into a standalone V8 driver.
[806.32 --> 812.20]  But it's a little bit tricky to integrate that with Node because Node.js expects everything to be asynchronous.
[812.70 --> 814.76]  So I think there's some people working on that.
[815.62 --> 817.86]  I'm not sure how far along that is.
[817.96 --> 820.78]  But yeah, that's definitely an interesting way to go as well.
[820.78 --> 824.24]  And another server-side thing that depends on the JavaScript is MapReduce.
[824.52 --> 829.86]  So MongoDB has relatively recently added support for full MapReduce.
[830.12 --> 834.06]  And you express these Map and Reduce functions in JavaScript.
[835.98 --> 836.50]  Right.
[836.70 --> 837.80]  Yeah, those are nice.
[837.86 --> 839.12]  Those are new in 1.1 or 1.2?
[840.08 --> 845.58]  They appeared sometime in the 1.1 cycle, probably 1.1.2 or so.
[845.58 --> 851.90]  But they are in 1.2 now, which 1.2 is the latest stable, which was released last week.
[852.36 --> 859.82]  So I'm in a conversation with Michael Bly on Twitter this afternoon around views in Mongo.
[859.92 --> 861.32]  I'm not sure if you saw that one.
[862.68 --> 867.34]  Any plans to store saved views in Mongo a la Couch's implementation?
[867.34 --> 871.78]  Yeah, so that's an interesting point.
[871.94 --> 877.08]  So the way CouchDB works, you do queries in Couch through MapReduce views.
[877.92 --> 885.06]  And basically, in CouchDB, the MapReduce thing is custom index building.
[885.22 --> 890.42]  Whereas in MongoDB, our MapReduce support is more for aggregation and that sort of thing.
[890.44 --> 891.52]  And it's real-time, right?
[891.60 --> 892.36]  Yeah, right.
[892.36 --> 897.28]  So in CouchDB, you specify a MapReduce function to do your queries, pretty much.
[898.08 --> 904.26]  And so as you're inserting documents, that view is getting updated to maintain an index.
[904.84 --> 906.30]  Basically, it's a custom index.
[906.94 --> 913.76]  And so the equivalent thing in Mongo would be if we supported some sort of custom indexing.
[914.84 --> 916.74]  And I think that's probably on the roadmap.
[917.12 --> 917.54]  I don't know.
[917.70 --> 920.78]  There's a lot of things on the roadmap right now.
[920.78 --> 924.92]  So one thing that we're pushing pretty heavily on is sharding.
[925.04 --> 927.00]  So we support auto-sharding now.
[927.58 --> 928.22]  It's in alpha.
[928.92 --> 931.46]  So the database supports full replication.
[931.68 --> 932.66]  That's stable.
[933.48 --> 938.68]  But the auto-sharding stuff is to allow for this sort of infinite horizontal scalability.
[938.88 --> 940.22]  That's in alpha right now.
[940.28 --> 943.04]  So we're really pushing on getting that to be more stable.
[943.04 --> 946.64]  And there's a bunch of other things we're working on as well right now.
[946.84 --> 952.34]  Big things like concurrency, better support for concurrency, some durability stuff.
[952.68 --> 958.34]  So I'm not sure when we'd expect to see custom index building.
[958.48 --> 960.46]  But it's certainly a possibility at some point.
[960.46 --> 973.84]  And that may be a feature left to the ORM drivers out there just to be able to take those map produced functions and compile them down and save them just for convenience sake so that the developer doesn't have to keep up with them.
[973.84 --> 980.84]  Oh, well, you can already save JavaScript to the server side and call it.
[981.08 --> 984.00]  So you can store JavaScript functions on the server side.
[984.16 --> 993.10]  I think the difference between that and something like CouchDB's views is that those views are updated on writes.
[993.44 --> 997.34]  So it's more like an index than a special type of query.
[997.34 --> 1004.26]  So to have something equivalent, we'd really need to support custom index building.
[1004.38 --> 1008.22]  And we found that in general, you can build indexes.
[1008.34 --> 1012.96]  You can specify indexes on compound indexes, indexes on embedded documents.
[1013.52 --> 1016.04]  And we have a pretty rich query language as well.
[1016.42 --> 1022.06]  And so queries in MongoDB are a little bit more traditional, a little bit more like you're used to with an RDBMS.
[1022.06 --> 1023.84]  So they're dynamic queries.
[1024.50 --> 1026.74]  And like I said, you specify indexes manually.
[1027.34 --> 1029.48]  And I think we found that that resonates pretty well.
[1029.56 --> 1033.26]  So I don't think there's too, too much of a need for this sort of custom view thing.
[1033.48 --> 1037.00]  But it'll be a possibility further down the line, I think.
[1037.98 --> 1045.52]  You know, one of the interesting aspects of how you guys store data in Mongo is, I believe this is the correct pronunciation, Bison, B-S-O-N.
[1045.90 --> 1046.26]  Is that right?
[1046.32 --> 1046.44]  Yeah.
[1046.52 --> 1048.76]  So I've been saying it Bison.
[1048.76 --> 1050.58]  And around here, we've been saying it Bison.
[1050.98 --> 1054.46]  But I think that's probably open to interpretation.
[1055.04 --> 1055.32]  So Bison.
[1055.32 --> 1058.08]  So that's binary serialized object notation.
[1058.20 --> 1058.54]  Is that right?
[1059.04 --> 1059.28]  Right.
[1059.42 --> 1064.60]  So Bison is, it stands more or less for binary JSON.
[1064.96 --> 1066.88]  So I'm not a linguist.
[1066.96 --> 1071.18]  I don't know if we're committing serious fouls there in terms of that abbreviation.
[1071.34 --> 1073.34]  But it stands for binary JSON.
[1073.34 --> 1077.38]  And so what Bison is, is this serialization format that we've defined.
[1078.02 --> 1081.78]  And all of our drivers can serialize to and from Bison.
[1082.90 --> 1088.70]  And it's pretty much a serialization of a superset of JSON.
[1088.70 --> 1102.24]  So it's JSON, plus we support some additional types, like a separate type for floating points, then for integers, and a date type, and a regex type, both of which are very useful if you're building a database.
[1102.70 --> 1105.04]  And JSON doesn't have anything like those.
[1106.38 --> 1110.40]  So it's slightly a superset of JSON, but it's a binary encoding.
[1110.40 --> 1117.22]  So it's lightweight, and there's some stuff in there to make it fast and easy for the database to traverse.
[1118.06 --> 1124.82]  So what happens is that the driver takes a document and encodes it to this Bison format and sends it to the database.
[1124.82 --> 1129.96]  And the cool thing is that that's already a format that the database understands.
[1130.08 --> 1132.74]  So it pretty much just takes that data and writes it right to disk.
[1132.82 --> 1135.84]  And that's one thing that allows MongoDB to be so fast.
[1136.56 --> 1138.52]  And then the database understands that format.
[1138.64 --> 1145.36]  So it's able to reach inside and do operations on embedded documents and build indexes and all that sort of good stuff.
[1145.90 --> 1152.10]  Have you actually built anything with Mongo, or is it primarily an internal project that you're working on?
[1152.10 --> 1157.54]  So the stuff that I've been building has been primarily internal stuff.
[1157.70 --> 1163.60]  But yeah, I've been eating my own dog food a little bit, and it's pretty nice.
[1163.74 --> 1172.64]  I think that people – so like I said, there's two reasons I think people are sort of jumping into these nonrelational databases.
[1172.88 --> 1175.36]  And one is the promise of scalability, which is a big one.
[1175.94 --> 1177.92]  But the other is flexibility.
[1177.92 --> 1188.26]  And I think that working with these as a developer, and for the people listening out there, you should go ahead and go to MongoDB and download it and go through the tutorial.
[1188.40 --> 1195.78]  Because I think you'll find that in a lot of cases it can be a lot more flexible and fun to work with and easier to work with than a relational database.
[1196.06 --> 1200.34]  So there are more reasons to use them than just performance and scalability.
[1200.34 --> 1205.18]  You know, the flexibility also introduces – I wouldn't say problems, but challenges.
[1205.52 --> 1208.68]  I've used Couch and used Mongo and discussing with colleagues.
[1208.96 --> 1213.46]  You really have to kind of rethink how you model the data in your application.
[1213.70 --> 1214.54]  Have you found the same?
[1215.44 --> 1217.96]  Yeah, so certainly you do.
[1218.72 --> 1222.58]  And I think that's both an advantage and a disadvantage.
[1222.58 --> 1228.82]  So one thing that's interesting about data in MongoDB is that the notion of embedded documents.
[1229.34 --> 1237.24]  So documents are what we call these objects that you're storing in the database, which are more or less JSON-like.
[1237.48 --> 1239.22]  So in Ruby, it's a hash.
[1239.30 --> 1240.32]  In Python, it's a dictionary.
[1240.80 --> 1241.78]  In JavaScript, it's a map.
[1241.86 --> 1242.96]  Or in Java, it's a map.
[1243.54 --> 1245.54]  In JavaScript, it's an object, whatever it is.
[1245.84 --> 1249.00]  But so it's not just a first-level thing, though.
[1249.00 --> 1257.38]  So in a relational database, if you were working on a blog, for example, you'd probably have a table for posts and a table for comments.
[1258.06 --> 1262.92]  And when you wanted to get a post and its comments to display on a page, you'd do a join.
[1263.66 --> 1277.06]  And in something like MongoDB, where you can store embedded documents, one good way to represent that relationship would be to actually take those comment documents and actually embed them right within the post itself.
[1277.06 --> 1281.66]  And so that allows you to go ahead and get a post with all of its comments.
[1282.46 --> 1285.08]  And it's all coming from the same place, and it's all a single document.
[1285.26 --> 1289.60]  And so you're going to see significant performance increases by doing that versus doing a join.
[1291.50 --> 1296.44]  And in some cases, it can also be easier to work with to use these embedded documents.
[1296.44 --> 1315.42]  So it does create some – I don't think problems is the right word, but there's certainly some things you have to think about, which is when does it make sense to embed documents versus referencing other documents in a different collection and doing more like a join type thing.
[1315.42 --> 1318.60]  And there are certainly cases where each makes sense.
[1318.82 --> 1328.22]  So there are some different sets of things you need to think about in terms of designing your schema as it is, or as you might call it.
[1328.74 --> 1342.54]  You know, early on when I was working with Mongo, I found myself developing, I guess, wider schemas than deep schemas based on whether or not I needed to return a particular type as a top-level object itself.
[1342.54 --> 1349.08]  But with MapReduce, you guys have kind of muddied the waters even more because now I get kind of the best of both worlds.
[1349.36 --> 1355.84]  Can you talk about how long it took to develop MapReduce and any challenges that you came across in developing that feature?
[1357.08 --> 1362.60]  Yeah, so it didn't take too long to have a basic implementation going, I don't think.
[1362.92 --> 1365.96]  Elliot has been the one primarily working on the MapReduce stuff.
[1365.96 --> 1380.34]  And it didn't take too, too long because we already had the JavaScript interpreter embedded and we already had a mechanism for sending commands to the database and all that sort of stuff.
[1380.50 --> 1386.92]  So it was more, I think, coming up with the model that we're going to use for MapReduce.
[1386.92 --> 1390.78]  And then there's been some, you know, making sure that things are performing.
[1391.06 --> 1396.54]  So MapReduce, as it is right now, is probably more of an offline thing.
[1396.74 --> 1408.88]  So you wouldn't be doing a MapReduce job as a simple query, you know, that you're using to generate a response to a page, like, instantaneously in real time.
[1408.88 --> 1420.68]  So the way it is right now, it would be more of, like, every couple minutes do a MapReduce job, generate some results, and then use those results to respond to later queries.
[1421.02 --> 1424.66]  So that's been the model that we're working with now.
[1424.92 --> 1429.00]  And so I think some of the difficulties are getting MapReduce right in a sharded environment.
[1429.24 --> 1437.64]  So one of the good things about MapReduce is that it's possible to do in a sharded environment versus something like group, which is a little bit more difficult to do.
[1437.64 --> 1441.52]  And so getting that right is certainly a problem.
[1441.76 --> 1446.18]  And then performance stuff has been something that we've been working on with that as well.
[1446.82 --> 1453.58]  You know, two of my favorite features of MongoDB regarding updates are upserts, which are really, really nice.
[1453.70 --> 1461.26]  And this is, you know, we specify the key and then a hash of values, and then we'll do one fire and forget update or insert.
[1461.50 --> 1466.40]  And then the other are the modifier operations, the set, ink, push, push all.
[1467.64 --> 1470.82]  How did those come about as far as features?
[1471.04 --> 1477.70]  Do you guys just develop to scratch your own itch, or how do features get, I guess, developed into the framework?
[1478.26 --> 1480.74]  Yeah, so upsert and the update modifier.
[1480.88 --> 1484.56]  So I'll introduce those a little bit more for people who might not be familiar with them.
[1485.12 --> 1487.70]  But MongoDB supports an update operation.
[1487.90 --> 1491.70]  And one option when you do an update is to do an upsert, which says,
[1491.70 --> 1496.66]  if you can't find a document to update, then go ahead and create this new document instead.
[1497.06 --> 1501.68]  And like you said, that can be really nice for doing a fire and forget insert or update.
[1502.36 --> 1505.74]  And then the other thing that you mentioned are these atomic operators.
[1505.74 --> 1516.06]  So we support a bunch of different atomic operators for updates, like increment, set, append to an array, a bunch of different things.
[1516.14 --> 1517.34]  And those can be really nice, too.
[1517.46 --> 1522.98]  So for doing something like real-time analytics, if you have some document and you want to increment a counter,
[1523.60 --> 1525.44]  you can just send a single update operation.
[1525.64 --> 1528.90]  You don't need to go get the document, modify it, and save it back.
[1528.90 --> 1531.92]  And you can do that increment like that.
[1532.24 --> 1537.06]  And so those are very useful as well and allow for some good performance benefits.
[1537.52 --> 1538.78]  And those have been around for a while.
[1539.80 --> 1542.72]  I mean, we've been adding more modifiers as time goes on.
[1542.82 --> 1547.36]  But those have been around for, I think, at least as long as I've been working on the project.
[1547.50 --> 1551.68]  So I'm not sure who came up with them or who to give credit to for them.
[1551.68 --> 1563.56]  But certainly MongoDB as a whole, the thought process behind it comes from the experiences that our founders have had with developing large infrastructure.
[1563.96 --> 1570.42]  So our CEO, Dwight, was one of the co-founders of DoubleClick and worked on the ad-serving architecture there.
[1570.76 --> 1579.14]  And Elliot, who's our CTO, was a co-founder of ShopWiki and has done a ton of stuff there as well.
[1579.14 --> 1583.90]  So both of them have plenty of experience with developing large infrastructure.
[1584.12 --> 1591.42]  And so I think that part of MongoDB has been to sort of scratch what their issues were with developing that infrastructure.
[1591.90 --> 1598.52]  You know, one of the things that I really liked about using CouchDB was Futon, the built-in admin interface that it supports.
[1600.30 --> 1602.48]  What's the state of GUI tools for Mongo?
[1602.70 --> 1605.12]  And are you guys working on anything or just leaving it to the community?
[1606.16 --> 1607.14]  Yeah, so that's a good question.
[1607.14 --> 1621.18]  I think that up until recently, we've sort of been hoping for somebody from the community to take charge of a project like that and head it up.
[1621.46 --> 1624.96]  So MongoDB does support some administrative tools like the shell.
[1625.62 --> 1629.26]  And we have a basic web console, which can be very useful for debugging.
[1629.54 --> 1633.72]  And when you run the database, that starts by default as well.
[1633.72 --> 1643.62]  But like you say, we don't have a nice sort of GUI tool that does all the things that you might want, let you inspect your database and add data and do all that sort of stuff.
[1643.62 --> 1659.54]  But I think our feeling now is that maybe we'll have to get a project like that started and sort of put some momentum behind it and then hope that we get some community involvement that way.
[1659.54 --> 1667.40]  Because there's been a few projects from the community that have been pretty good attempts or pretty good steps in the right direction in terms of that.
[1667.48 --> 1672.20]  But I don't think there's anything that's been really solid and a really great UI.
[1672.20 --> 1682.94]  And especially once we get things like sharding out there, it'd be nice for an admin tool to support some of the sharding layouts and that sort of stuff as well.
[1683.14 --> 1691.44]  So I think it might end up being that we need to sort of put some momentum behind that and see where the community wants to take it afterwards.
[1692.40 --> 1699.30]  Would, I guess, a more restful interface on top of Mongo built into the server kind of facilitate that?
[1699.30 --> 1702.54]  I think it might.
[1704.26 --> 1718.12]  Part of the problem there is that if you're just using it over a rest layer, then you have to manage permissions and authentication and stuff that way as well.
[1719.08 --> 1725.88]  Like you said, there is a rest layer in Mongo in the default Mongo server now.
[1725.88 --> 1732.88]  But it's pretty simplistic, and I'm not sure it's quite ready for something like this to be built on top of it.
[1733.20 --> 1745.18]  And I think we think that going forward, the right model is to build a nice rest layer in one of the client languages like Python or Ruby or PHP or whatever,
[1745.18 --> 1754.44]  and talk to the database through underlying calls in the driver and then implement the rest layer in one of these other languages rather than implementing it in C++.
[1756.46 --> 1758.96]  So I think that would probably be the model that we would recommend.
[1759.90 --> 1767.54]  And that might be a part of this admin project, or the UI could just talk to one of the drivers directly.
[1767.54 --> 1771.92]  I think either way has its advantages and disadvantages.
[1772.76 --> 1782.10]  Mike, could you talk a minute about, I guess, the different languages that have bindings for MongoDB and what sort of traction you're getting in each community?
[1782.88 --> 1783.60]  Yeah, sure.
[1783.86 --> 1790.38]  So I'm going to pull up the drivers page right now just to make sure that I don't miss any.
[1790.38 --> 1794.30]  But obviously we support Ruby and Python.
[1794.46 --> 1797.12]  That's what I work on for the most part.
[1797.32 --> 1803.38]  We have a PHP driver, a Perl driver, a Java driver, C++.
[1805.00 --> 1813.52]  Recently we have a standalone C driver that was recently released, and that hasn't had too, too many eyes on it.
[1813.52 --> 1820.52]  So we're hoping to get some people from the community to start using that and recommend directions to take with that.
[1820.90 --> 1824.10]  And we also have that JavaScript driver that I mentioned.
[1824.92 --> 1828.48]  So that's the ones that are sort of supported by 10-gen.
[1829.50 --> 1831.64]  And all of those have seen a good amount of traction.
[1831.64 --> 1844.28]  I think Ruby has probably seen the most in terms of community interaction, but certainly PHP, Python, Java, and Ruby have all seen a ton of users and a ton of stuff.
[1844.38 --> 1847.44]  And actually Perl has seen a good amount of usage as well.
[1848.66 --> 1858.26]  There are some people using the C++ driver, and hopefully we'll get some people using the C driver for things like web server extensions and that sort of stuff.
[1858.26 --> 1867.80]  I have an NGINX module for MongoDB's GridFS that I wrote, and I'm hoping to port that to the C driver when I get a chance.
[1868.36 --> 1870.30]  And then we have a ton of community-supported drivers.
[1870.44 --> 1882.30]  So there's a C-sharp.net driver, ColdFusion, AirLang, Factor, F-sharp, Go, Groovy, PowerShell, and a couple of other ones as well.
[1882.30 --> 1888.08]  So there's been a lot of work from the community as well in terms of adding support for these different languages.
[1888.26 --> 1890.14]  Very cool.
[1890.48 --> 1892.84]  Hey, something – I know it's been a while since I've actually chimed in here.
[1892.92 --> 1894.86]  Wynn's been mostly driving this thing, but –
[1894.86 --> 1896.74]  That's because I'm just an excited fanboy.
[1898.72 --> 1899.38]  That's true.
[1899.46 --> 1899.92]  That's true.
[1900.48 --> 1906.60]  Something I'm curious of, it seems like 10GEN was developing this cloud computing platform,
[1906.72 --> 1909.28]  and then they spun it off into just being MongoDB-focused.
[1910.04 --> 1918.76]  As a company, though, just focusing on MongoDB, how do you guys get the word out about new things that are happening with MongoDB,
[1918.88 --> 1920.00]  and how do you interact with the community?
[1921.04 --> 1928.74]  Yeah, so I think one way that has sort of dominated has been through Twitter.
[1928.74 --> 1936.66]  So a lot of the way that we sort of track what the community is talking about has been through Twitter searches for MongoDB,
[1936.94 --> 1938.86]  and that actually works very well.
[1938.94 --> 1943.62]  For those of you working on open source projects, that's a great way to get some feedback,
[1943.88 --> 1947.46]  because people are out there talking about it, whether or not they're talking to you or not.
[1948.84 --> 1949.88]  So that's worked really well.
[1949.88 --> 1955.58]  We also have a Google group that we use for doing support and that sort of stuff,
[1955.66 --> 1958.14]  so that gets a lot of traction.
[1959.04 --> 1964.44]  We have an IRC room on Freenode, Sharp MongoDB on Freenode,
[1964.66 --> 1968.82]  and there tends to be people in there at all hours of day and night.
[1969.36 --> 1972.78]  So for quick questions, that's a good way to go about getting them answered.
[1973.32 --> 1978.10]  But in terms of community, I mean, I think the keys have really been just paying attention
[1978.10 --> 1985.34]  to sort of these back channels, mainly Twitter, and then getting out there and talking about it.
[1985.42 --> 1990.08]  So we've also done, I think, a pretty good job of getting out to conferences,
[1990.46 --> 1995.46]  and people like Wynn and others from the community have also done a good job of getting out there
[1995.46 --> 1998.06]  and talking about MongoDB at conferences and meetups and stuff.
[1998.68 --> 2000.68]  And I think that's been really good as well.
[2001.94 --> 2003.00]  I'm curious, though.
[2003.04 --> 2005.56]  I didn't hear GitHub.com mentioned at all on that.
[2005.56 --> 2014.58]  Yeah, so all of the projects are hosted on GitHub, and that's been great, too.
[2014.76 --> 2019.10]  So that makes it really quite easy for people to contribute back to the projects.
[2019.44 --> 2024.90]  So to contribute to any of the MongoDB projects, it's pretty much fork and pull request,
[2025.10 --> 2028.86]  and we'll take a look at your commit and merge it back into the main line.
[2029.20 --> 2030.96]  And that's been really good as well.
[2030.96 --> 2036.06]  Do you get a lot of contributions that way, or has it been pretty much you guys focused?
[2037.10 --> 2040.30]  No, we've seen a good amount of community contributions.
[2040.54 --> 2049.24]  I think contributions to the core server have been probably mainly coming from within Tengen.
[2050.62 --> 2054.30]  There's certainly been some people who've done things like packaging,
[2054.76 --> 2057.44]  Debian scripts for the server, that sort of stuff,
[2057.44 --> 2059.38]  and contributed those.
[2059.50 --> 2063.74]  But there hasn't been too, too many outside contributors
[2063.74 --> 2066.50]  who have been really getting into the nitty-gritty in terms of the server.
[2067.10 --> 2071.08]  But certainly on the drivers, we've had a ton of contributions from the community.
[2071.50 --> 2072.76]  It's been really great, actually.
[2073.52 --> 2078.96]  And not only on the drivers themselves, but also on additional tools built around them.
[2078.96 --> 2085.32]  So one example is in Ruby, there's this project called MongoMapper that John Neumaker started,
[2085.76 --> 2088.60]  and that's been really great.
[2088.70 --> 2094.58]  That's basically like an object mapper that's built on top of the lower-level Ruby driver.
[2095.32 --> 2098.08]  And people seem to really like it.
[2098.60 --> 2102.94]  And so things like that, we've seen a ton of community development going on.
[2103.60 --> 2106.30]  Is there any equivalent to MongoMapper in the Python community?
[2106.30 --> 2110.84]  Yeah, so there's a couple, actually, that have been started.
[2111.02 --> 2114.56]  The big one that's been around for a while is MongoKit.
[2115.12 --> 2117.48]  And these are listed, for those of you following along at home,
[2117.56 --> 2124.30]  if you go to the Python page, which is api.mongodb.org slash Python,
[2124.94 --> 2126.50]  and you click on the Tools link,
[2126.72 --> 2131.52]  there's a list of tools that have been built around the Python driver.
[2131.52 --> 2135.32]  And I think the big one up until now has been MongoKit,
[2135.52 --> 2139.96]  which is a similar type of thing, a framework that provides validations
[2139.96 --> 2143.80]  and that sort of stuff on top of PyMongo, which is the Python driver.
[2144.88 --> 2149.64]  And another interesting one to look at was just announced in the past couple of weeks,
[2149.76 --> 2151.16]  and that's called Ming.
[2151.38 --> 2154.18]  And that was released by the SourceForge people, actually.
[2154.18 --> 2157.70]  So SourceForge was one of the really early adopters of MongoDB,
[2158.74 --> 2162.62]  and they developed this Python library as part of that.
[2163.00 --> 2164.46]  And so they've open sourced it.
[2164.58 --> 2166.82]  And I haven't gotten to play with it yet,
[2166.94 --> 2170.06]  but I've looked through the source and looked through the docs,
[2170.12 --> 2171.68]  and that looks really nice.
[2171.84 --> 2176.16]  So it'll be interesting to see if people start to pick up on that going forward.
[2176.90 --> 2181.48]  You know, one of the questions that we had posed to the changelog for you, Mike,
[2181.48 --> 2186.34]  was any plans for full-text support in MongoDB?
[2187.08 --> 2190.16]  Yeah, so there's a Jira ticket open.
[2190.26 --> 2191.78]  We use Jira for our bug tracking.
[2191.94 --> 2196.02]  There's a bug ticket open right now for full-text search.
[2196.66 --> 2203.30]  And I think the status of that now is still sort of gathering ideas from the community
[2203.30 --> 2207.42]  and seeing exactly what the right model is going forward.
[2207.42 --> 2214.22]  I think one thing to note is that in terms of basic full-text search,
[2214.92 --> 2218.20]  MongoDB has this built-in feature called multi-key indexing.
[2218.46 --> 2221.58]  So if you have an array and you create an index on that array,
[2222.12 --> 2225.04]  that index will actually be keyed on each element of the array.
[2225.28 --> 2230.24]  So for doing things like getting all documents that have a certain tag
[2230.24 --> 2232.64]  or something like that, you can make those queries really fast.
[2232.94 --> 2234.18]  And that's really nice.
[2234.26 --> 2237.00]  You can do some basic full-text search like that.
[2237.00 --> 2239.74]  I think that's actually how the Business Insider,
[2239.90 --> 2243.14]  which is a site that runs on MongoDB, does their search.
[2243.88 --> 2247.50]  But in terms of more general purpose, advanced full-text search,
[2248.16 --> 2252.58]  my guess is that the model will be something along the lines of
[2252.58 --> 2255.70]  having some basic support built into MongoDB
[2255.70 --> 2258.58]  for sort of pretty simplistic full-text search,
[2258.58 --> 2264.22]  and then making sure that integration with tools like Sphinx or Lucene
[2264.22 --> 2267.26]  or whatever else is really nice and really easy.
[2268.60 --> 2273.32]  And like I said, there's a ticket open now where people are sort of going back and forth
[2273.32 --> 2274.92]  on what the right model is.
[2275.66 --> 2278.52]  But I imagine we'll see something like that.
[2278.80 --> 2281.20]  You mentioned earlier that you guys are hiring at MongoDB.
[2281.20 --> 2283.82]  What sort of skills would one need to join the team?
[2284.62 --> 2288.12]  Well, I think the best way, if people are interested,
[2288.56 --> 2292.64]  I think the email address is jobs at 10gen.com.
[2292.76 --> 2294.94]  So if you're interested, you can send stuff that way.
[2294.94 --> 2301.56]  But I think really the best way to impress us and to make an impact
[2301.56 --> 2305.74]  would be to look at the code that's out there.
[2305.80 --> 2308.20]  Like I said, it's all on GitHub, and it's easy to contribute to
[2308.20 --> 2314.38]  and find a bug or find a feature that you'd like to see and contribute,
[2314.88 --> 2319.20]  make a fix or implement a feature and send us a pull request.
[2319.80 --> 2323.50]  And I think that's probably the best way to show that you're actually interested
[2323.50 --> 2327.54]  and to find out if the job would work for you
[2327.54 --> 2331.44]  and for us to see if you would work for the job, I guess.
[2332.64 --> 2334.82]  The open source job interview. I like it.
[2334.84 --> 2336.06]  Right. Yeah, it's perfect.
[2336.20 --> 2338.16]  That's one of the big benefits of being open source.
[2338.50 --> 2340.94]  So I'm not sure if you've listened to an episode yet, Mike,
[2340.98 --> 2344.76]  but we normally wrap each interview by putting our guests on the spot
[2344.76 --> 2347.34]  and ask, what's on your open source radar?
[2347.46 --> 2350.14]  What open source projects out there other than the one that you're working on
[2350.14 --> 2351.52]  has got you most excited?
[2351.52 --> 2356.52]  So I'm sort of a languages...
[2357.60 --> 2359.88]  I'm sort of really interested in languages,
[2360.14 --> 2364.28]  so some of these new JVM languages are sort of interesting to me,
[2364.38 --> 2366.06]  Scala, Clojure, et cetera.
[2366.96 --> 2369.22]  I tend to track the development of those.
[2371.10 --> 2374.72]  In terms of R space, there's a bunch of interesting projects
[2374.72 --> 2377.04]  that are going on in the NoSQL space.
[2377.14 --> 2379.12]  If you ask me, I think MongoDB is the most interesting,
[2379.12 --> 2383.36]  but there's other projects, too, like Cassandra, CouchDB, Redis, et cetera,
[2383.48 --> 2385.64]  that are all interesting and worth a look.
[2387.24 --> 2389.68]  But yeah, open source is moving fast,
[2389.78 --> 2393.50]  so there's only going to be more cool stuff in the future, I think.
[2394.66 --> 2396.92]  Well, it's been a wild ride in 2009.
[2397.10 --> 2401.46]  I think 2010 is just going to bode well for MongoDB adoption
[2401.46 --> 2405.94]  as other services I see cropping up, like MongoHQ and some others.
[2405.94 --> 2407.92]  So hopefully you guys will have continued success.
[2408.88 --> 2409.42]  Yeah, hopefully.
[2411.18 --> 2411.94]  Well, that's been it.
[2412.02 --> 2414.58]  It's been a wild ride, and we thank you for joining us.
[2414.86 --> 2415.66]  Adam, you have any questions?
[2416.34 --> 2421.06]  No, just thanks for taking your time to have a good time with us on the show
[2421.06 --> 2421.74]  and answer some questions.
[2421.88 --> 2424.08]  I know that a lot of the stuff you talk about
[2424.08 --> 2425.62]  is going to benefit the open source community,
[2425.76 --> 2427.24]  and that's the aim here.
[2427.92 --> 2428.74]  Yeah, thanks, guys.
[2428.74 --> 2431.62]  I think it's great what you guys are doing with the show,
[2431.74 --> 2435.36]  so it was quite an honor to come on and get to chat with you guys.
[2435.74 --> 2436.44]  Awesome. Thank you.
[2436.50 --> 2436.94]  And you know what?
[2437.12 --> 2439.18]  I don't think we mentioned it since we're going to put it in the intro.
[2439.28 --> 2442.68]  This is episode 007, so it shows you how cool you are.
[2442.98 --> 2444.12]  That is perfect.
[2444.50 --> 2445.22]  That is perfect.
[2445.44 --> 2446.48]  007, baby.
[2447.80 --> 2448.78]  All right. Thanks, Mike.
[2449.18 --> 2449.96]  Yep. Thanks, guys.
[2450.74 --> 2457.76]  Thank you for listening to this edition of The Changelog.
[2458.74 --> 2462.48]  Be sure to tune in weekly for what's fresh and new in open source.
[2463.68 --> 2468.54]  Also, visit thechangelog.com to follow along, subscribe to the feed, and more.
[2468.72 --> 2469.78]  Thank you for listening.
[2469.78 --> 2470.78]  Thank you.
