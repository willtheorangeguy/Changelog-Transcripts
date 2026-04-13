[0.00 --> 18.20]  Welcome to the ChangeLog episode 0.4.5.
[18.32 --> 19.28]  I'm Adam Stachowiak.
[19.66 --> 20.52]  And I'm Wynne Netherland.
[20.70 --> 21.50]  This is the ChangeLog.
[21.54 --> 23.10]  We cover what's fresh and new in open source.
[23.52 --> 26.32]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.46 --> 27.26]  We're also up on GitHub.
[27.26 --> 29.44]  Head to github.com slash explore.
[29.54 --> 33.58]  You'll find some trending repos, some feature repos from the blog, as well as the audio podcasts.
[33.94 --> 38.04]  If you're on Twitter, follow ChangeLog Show, ChangeLog Jobs, and me, Adam Stach.
[38.62 --> 41.02]  And I'm Penguin, P-E-N-G-W-I-N-N.
[41.40 --> 43.90]  This week's episode is sponsored by GitHub Jobs.
[44.20 --> 46.94]  Head to thechangelog.com slash jobs to get started.
[47.52 --> 52.30]  If you'd like us to feature your job on the show, select Advertise on the ChangeLog when posting your job, and we'll take care of the rest.
[52.76 --> 55.14]  Just like our buddy Chris Epstein over at Caring.com did.
[55.14 --> 58.70]  He needs a really senior Rails engineer who's also wicked smart.
[60.32 --> 61.36]  Interested in this job.
[61.50 --> 64.62]  It's lg.gd slash 5S for the short link.
[65.48 --> 67.16]  Erlang in the back and Python in the front.
[67.26 --> 71.68]  UK-based SmartKits is merging internet and financial tech in real time.
[71.78 --> 75.18]  If you're game, check out short link lg.gd slash 5i.
[75.92 --> 80.54]  AppSpark's looking for a lead iOS developer who can take charge of the UI and UX decisions over there.
[80.54 --> 86.94]  If you sling the cocoa, the objective C, and you want to know more, it's lg.gd slash 5j.
[87.50 --> 88.44]  Fun episode this week.
[88.68 --> 91.92]  Talk to Salvatore Sanfilippo from Redis.
[92.38 --> 94.02]  I actually love this interview a lot.
[94.12 --> 103.20]  It was a lot of fun to edit, but the fun thing I think we'll take from this really is how he mentions his liking or disliking of the term of NoSQL.
[103.20 --> 109.88]  Yeah, it's nice to get another take on someone that's created a wildly popular NoSQL solution and what they think of that term.
[109.94 --> 111.22]  It's kind of like HTML5.
[111.56 --> 114.40]  It's one of those things you ask 10 people, you get a dozen definitions.
[114.80 --> 119.96]  And not to mention the fact that he didn't even look at the other solutions the entire time he started the development of Redis.
[120.10 --> 124.68]  And the cool thing of how this all even got popularized was a pretty cool story I think he told.
[124.68 --> 134.96]  You know, it seems to be a common thread in really popular applications is to build something that you want to consume yourself and just put the blinders on and, you know, darn the torpedoes.
[134.96 --> 137.14]  I'm going to build something that I want to use.
[137.54 --> 140.42]  Yeah, a couple months later was a damn near full-time job for him.
[140.92 --> 143.24]  Been kind of disappointed we had to sit on this one for a week.
[143.30 --> 146.26]  We recorded this a week ago and finally getting to release it.
[146.28 --> 146.80]  Should we get to it?
[146.98 --> 147.52]  Let's do it.
[154.68 --> 160.00]  We're chatting today with Salvatore Sanfilippo, the creator of Redis.
[160.46 --> 164.80]  So, Salvatore, why don't you take a moment and introduce yourself and a little bit about the project.
[165.54 --> 166.12]  Hi, all.
[167.60 --> 168.84]  I am Salvatore.
[169.08 --> 170.66]  I'm from Sicily, Italy.
[170.66 --> 179.64]  And I'm currently the lead developer of Redis together with Peter Norduis.
[179.64 --> 186.70]  I did a lot of years for 10 years, the freelance programmer.
[187.78 --> 194.88]  And then I switched to, I'm now working for VMware.
[195.42 --> 200.74]  That is supporting the development of Redis.
[200.74 --> 212.14]  And not just my development of Redis, but VMware is also paying the development time of Peter for Redis.
[212.86 --> 221.64]  So, my usual day is just hacking on Redis the whole time.
[221.64 --> 229.44]  And this was very, an interesting change compared to the past.
[230.44 --> 234.28]  Redis started something like a hobby.
[235.02 --> 244.22]  Well, not completely without something to gain because I used it for my startups, for web startups.
[244.70 --> 248.96]  But the project itself was not funded in any mean.
[248.96 --> 253.10]  For those that don't know, Redis, would you call it a key value store?
[253.82 --> 269.74]  Well, it is very, very pretty hard to find the right position of Redis in an everyday more complex database field.
[270.46 --> 276.86]  Because in some way, Redis is for sure a key value database.
[276.86 --> 290.04]  This is clear from the fact that you can mostly access, read data just by the primary unique index that is the key itself.
[290.52 --> 294.00]  So, in some way, it is for sure a key value database.
[294.00 --> 310.28]  But from another point of view, most of the key value database that there were before Redis were, from a mathematical standpoint, just a string to string map.
[310.74 --> 313.74]  While in Redis, values can be much more complex.
[313.74 --> 318.74]  And every value itself is something like a small database.
[319.18 --> 328.90]  Just to provide an example, the sorted set is something like a balanced tree itself.
[329.28 --> 336.06]  So, it's like there is an outer shell that works like a key value database.
[336.06 --> 340.02]  But the single values have specific data models.
[340.54 --> 352.68]  So, Redis is the sum of a key value database with a number of data models that are conceived in order to address, model, different kinds of problems.
[353.04 --> 358.62]  From everyone that I've spoken to that's used Redis, the very first thing that they talk about is speed.
[358.98 --> 363.08]  Does that come from it being written in C or what's the internals of Redis?
[363.08 --> 373.08]  Redis started to be fast in order to solve a specific problem I had with...
[373.08 --> 381.88]  I needed to write an analytic program, web analytics, that was really, really fast.
[381.88 --> 394.58]  And I needed to track real-time user interaction with the site to show these interactions in a web interface, Ajax web interface.
[395.08 --> 403.10]  I tried to model this problem with MySQL and it worked for a few months.
[403.10 --> 419.00]  But when we started to get more and more users, we realized that this was not the way to do things because the cost for every user was impossible to handle.
[419.88 --> 423.24]  Later, this project was more or less aborted.
[423.24 --> 429.42]  But the idea was to create a freemium business model.
[429.78 --> 434.58]  So, free users had to cost very little to us.
[434.92 --> 438.86]  Otherwise, it was impossible to go forward with the project.
[439.30 --> 444.60]  So, I started to write Redis with the goal of making it fast.
[444.60 --> 462.48]  What is, I think, interesting is that actually Redis started as a free database, not because the internals, the C internals were very optimized, like 3D game or something like that.
[462.48 --> 466.54]  It was fast because it was in C.
[467.00 --> 477.54]  It used an event model, an event-driven programming, and the data model itself was designed to be fast.
[478.32 --> 492.30]  So, it's not the fluid of an optimization, of micro-optimizations, but the API that Redis exports is designed in order to take little time,
[492.48 --> 498.10]  when dealing with the internal data structures exported by Redis.
[498.86 --> 503.00]  Let's talk a moment about some of the features of Redis.
[503.12 --> 507.88]  So, how does it compare in replication to other NoSQL options?
[508.88 --> 521.10]  To be honest, when I started to write Redis, I started without any kind of idea about the other NoSQL solutions.
[521.10 --> 531.58]  And, well, what is interesting is that after almost two years, I more or less, I'm continuing to never look to other solutions.
[532.06 --> 541.80]  I, for sure, played a bit with the most interesting solutions of the NoSQL environment,
[541.80 --> 548.28]  but I never focused on the implementation of other systems in a very specific way.
[549.90 --> 559.06]  But I think that Redis replication, by the way, is implemented in a completely different way.
[559.06 --> 566.42]  Because of the design of Redis, it needed to be very different,
[566.58 --> 572.02]  because I wanted non-blocking replication from the point of view of the master.
[572.40 --> 580.22]  I want automatic resynchronization when there was a problem in the link connecting the master to the slave.
[580.22 --> 589.14]  And I wanted to have such features with very, very little symbol code.
[589.32 --> 597.80]  So, I needed to take all these compromises together and to try to model something that could work.
[597.80 --> 608.12]  And the final solution for replication was to use the persistence code we had.
[608.12 --> 617.96]  So, in order to create a replica, what happens is that the slave asks the master for a sync.
[618.48 --> 625.14]  It's a Redis command, seeing that it's not conceived to be used by clients.
[625.14 --> 627.72]  It's just for the slave.
[628.36 --> 635.78]  When a master receives the sync command, it starts to produce just a dump.
[636.24 --> 640.72]  A dump, exactly like when you call BG save.
[641.16 --> 644.42]  So, it's like the usual persistence.
[644.42 --> 661.10]  So, we obtain a single file, an RDB file, that is transmitted back to the slave as a bulk file.
[661.68 --> 663.62]  It's just a file transfer thing.
[663.62 --> 678.82]  But when we started to produce this dump file, we also started to log every write query we received from clients and accumulate these writes in a buffer.
[678.82 --> 693.64]  So, when the slave will finally receive the dump, it will load this dump and the master will start to transmit the accumulated buffer of change.
[694.08 --> 699.62]  And this buffer of change, it's just exactly like the Redis protocol itself.
[700.12 --> 703.84]  So, it's not something like a binary log and so forth.
[703.84 --> 714.52]  At this point, the master will continue forever to write a stream of commands received from clients to the slaves, to old slaves.
[715.88 --> 721.22]  And so, the slave will continuously be updated.
[722.28 --> 729.86]  What is important is that Redis replication is not a synchronous replication, but is a sync.
[729.86 --> 740.06]  So, while a command is processed in the master, the client will get the OK from the master.
[740.48 --> 745.22]  And later, the command is put in a query.
[746.10 --> 747.74]  It is sent to the slave.
[747.88 --> 755.26]  So, if you get the OK code from the master, it doesn't mean that the slave is updated as well.
[755.26 --> 763.90]  But what is interesting is that science, we have a very efficient efficiency, is very good.
[764.32 --> 773.74]  So, actually, the delay is in the order of less than one millisecond, usually, between the master and the other replicas.
[774.64 --> 776.02]  And it's working very well.
[776.02 --> 783.86]  The replication is also a very important piece of the Redis cluster.
[784.04 --> 789.68]  This is our next big project I'm developing currently.
[790.12 --> 792.82]  You mentioned the invented model in the internals.
[792.98 --> 799.50]  When you build personal applications using Redis, what sort of application server model do you follow?
[799.70 --> 803.54]  Is it also invented or what's your tool set of choice?
[803.54 --> 808.72]  When I write for what kind of applications?
[809.26 --> 814.40]  When you yourself are building web applications, are you putting something invented in front of it,
[814.46 --> 819.28]  like Twisted or Event Machine or Node.js or just your personal flavor of application?
[820.24 --> 820.78]  Oh, okay.
[821.18 --> 825.34]  Well, I love to use Ruby with Sinatra.
[825.98 --> 828.12]  This is my pick.
[828.12 --> 836.52]  I love to have very, very small frameworks because I think that the more complex frameworks,
[837.44 --> 843.74]  for sure, it's true that you can do a lot of things with very little code.
[844.12 --> 848.70]  But in the end, I think that when you want to create something more complex,
[849.12 --> 854.80]  you have, in some way, to learn more and more how the framework itself works.
[854.80 --> 863.82]  And sometimes this learning activity may result in more or the same time needed to build it your own.
[865.14 --> 869.00]  So what I do is to take Ruby with Sinatra.
[869.42 --> 873.68]  And then I use a set of libraries I developed for myself.
[874.18 --> 878.84]  For example, I have a library that's called MySQL.rb.
[878.84 --> 883.66]  That is something like Active Records, but much more simple,
[884.10 --> 887.48]  that I use to talk with MySQL.
[887.94 --> 892.14]  And then I use the Redis gem to talk with Redis.
[892.62 --> 899.94]  And a library I wrote myself for HTML generation, programmatic generation,
[900.38 --> 904.18]  that is designed in order to be very fast.
[904.18 --> 910.58]  All these libraries are the kind of code you take around,
[911.16 --> 918.10]  you got from your old project, and put in your new project, and then hack on it.
[918.40 --> 921.36]  So I don't have really repositories for this code.
[921.66 --> 924.46]  I don't release this code as open source.
[924.46 --> 930.52]  But it's a few years at this point that I'm using this kind of framework,
[930.82 --> 934.98]  composed of my libraries and Ruby and Sinatra.
[935.30 --> 938.44]  I'm looking at the client list on Redis.io,
[938.66 --> 942.80]  and there's wide support for a lot of languages for Redis.
[942.94 --> 949.08]  Where do you see growth and what communities are growing in using Redis?
[949.08 --> 956.46]  The reason there are so many languages listed in the Redis.io site
[956.46 --> 959.48]  is because the Redis protocol was so simple
[959.48 --> 964.98]  that everybody had the fun of writing a client.
[966.18 --> 971.14]  But actually, there are a few of these clients
[971.14 --> 974.72]  that are with good support,
[974.72 --> 978.60]  with a lot of users, with a big user base,
[978.98 --> 981.82]  and others are a bit like hacks.
[983.40 --> 988.90]  The big users of Redis are for sure in the Ruby, Python,
[989.82 --> 996.16]  and possibly more and more in the Java languages.
[996.88 --> 1002.12]  There is also a good amount of people using the C client,
[1002.68 --> 1003.82]  even directly.
[1004.72 --> 1010.04]  Also, I think the Perl module is used enough.
[1010.72 --> 1013.00]  What's interesting is that the C client,
[1013.94 --> 1018.82]  well, there is something special about the C client.
[1019.14 --> 1021.56]  It is the only client we support directly.
[1022.24 --> 1024.68]  I and Peter has the Redis project.
[1025.10 --> 1026.16]  We wrote this client,
[1027.16 --> 1029.82]  and we support this client in a direct way.
[1029.82 --> 1034.82]  And there are a lot of people using Redis in very high performance environments
[1034.82 --> 1043.84]  that don't want to use an intermediate layer to talk with Redis.
[1043.84 --> 1052.06]  So they use directly written programs to write queries to Redis.
[1052.68 --> 1055.84]  And I think this is a bit strange,
[1056.92 --> 1060.64]  as I expected the C client to be very little used,
[1060.84 --> 1065.44]  because currently dynamic languages are much,
[1065.44 --> 1068.32]  much more interesting for the fast of development.
[1069.12 --> 1073.76]  Earlier, you said that you didn't look too much at the other NoSQL solutions out there.
[1073.76 --> 1078.50]  What do you feel about that term, NoSQL, and what does it mean to you?
[1079.90 --> 1081.88]  The term?
[1082.42 --> 1082.98]  Yes.
[1083.04 --> 1086.42]  Is that an adequate label for apps like this?
[1086.42 --> 1090.92]  Yeah, I think I have mixed feelings about it,
[1091.00 --> 1094.72]  because I don't like the NoSQL word itself.
[1095.46 --> 1102.56]  But, after all, as Evan, the Signed Patterns book demonstrated clearly,
[1102.88 --> 1108.10]  if there is no word for something, ever a very bad word,
[1108.64 --> 1112.30]  it is very hard to communicate to the programming community
[1112.30 --> 1114.28]  that we are on something,
[1115.02 --> 1122.62]  that we are trying to do something after a lot of years of database monoculture.
[1123.26 --> 1127.00]  So, while the NoSQL term may be the best term,
[1127.56 --> 1139.38]  for sure it was something like an incredible marketing thing to have such a term.
[1139.38 --> 1142.46]  It's like Web 2.0.
[1142.78 --> 1145.60]  It's not exactly a very cool term,
[1146.04 --> 1153.36]  but it was a very interesting way to communicate to all the web developers
[1153.36 --> 1155.24]  that something was changing.
[1155.82 --> 1162.50]  Now, the NoSQL term, it's a bit embarrassing in some way,
[1162.50 --> 1166.44]  because the SQL solutions are so different
[1166.44 --> 1171.70]  that the term is really making less and less sense.
[1172.02 --> 1176.40]  For instance, I can see in the NoSQL arena,
[1177.00 --> 1182.42]  databases that are actually more or less evolutions
[1182.42 --> 1188.28]  of the OSQL paradigm with a new implementation,
[1188.28 --> 1194.56]  maybe much more concerned with performances than with consistency,
[1195.14 --> 1198.70]  maybe with new protocols to talk to the database,
[1199.14 --> 1202.02]  but it's, after all, the same data model.
[1202.36 --> 1203.30]  You have objects.
[1204.38 --> 1208.22]  These objects can have complex indexes,
[1208.48 --> 1211.96]  and you can run complex queries against these objects.
[1211.96 --> 1218.60]  And this is a very worthwhile evolution of former databases.
[1219.24 --> 1226.12]  Then there are databases in the NoSQL world
[1226.12 --> 1228.88]  that are completely different than this paradigm,
[1229.38 --> 1234.74]  yet we use the same term to address the whole space
[1234.74 --> 1237.00]  of these alternative solutions.
[1237.00 --> 1242.00]  It's working currently, but I guess we are near the...
[1242.78 --> 1245.78]  We are starting to see that the term used
[1245.78 --> 1250.90]  a little less than it was used before.
[1251.12 --> 1255.74]  I see the news in Hacker News that are more and more
[1255.74 --> 1261.74]  not about NoSQL, but more about Redis, MongoDB, Cassandra,
[1262.84 --> 1264.08]  React, and so forth.
[1264.08 --> 1267.06]  So I think things are evolving.
[1267.68 --> 1269.98]  Talk to us a bit about Redis PubSub.
[1272.58 --> 1278.74]  Yes, Redis PubSub was a bit of a strange addiction to Redis
[1278.74 --> 1290.58]  because, well, after all, you can think that it's not a fit for Redis
[1290.58 --> 1296.76]  because Redis is a database, and PubSub is clearly a messaging primitive.
[1298.26 --> 1301.48]  So why we added it?
[1301.82 --> 1307.06]  Because to start Redis itself in the internal, in its core,
[1307.26 --> 1312.88]  its internal core is very suited for this kind of message-passing activities.
[1312.88 --> 1321.66]  And then we had already something that looked like more messaging data structure
[1321.66 --> 1325.26]  than a database data structure that was the list.
[1325.72 --> 1332.86]  The list is very useful as a database kind of database value,
[1332.86 --> 1341.14]  but it's also because it supports push and pop operation in constant time.
[1341.14 --> 1347.26]  It was very interesting as a primitive form to create messaging solutions.
[1347.68 --> 1351.38]  And actually, GitHub started using it for rescue.
[1351.38 --> 1357.44]  And then we started to get more and more requests
[1357.44 --> 1365.70]  about providing more powerful lists to create instead,
[1365.88 --> 1372.58]  because the list can be used just as one producer, one receiver,
[1372.58 --> 1377.96]  or if there are multiple receivers of these messages,
[1378.44 --> 1382.54]  they can pick the same message all the consumers.
[1383.28 --> 1385.92]  One consumer will get the first message,
[1386.34 --> 1389.28]  the second consumer will get the next message, and so forth.
[1389.74 --> 1396.08]  So instead of trying to evolve the list to create something it was not designed to,
[1397.12 --> 1400.12]  we tried to add something different.
[1400.12 --> 1404.38]  That is a simple fire and forget PubSub functionality.
[1405.22 --> 1410.78]  Another important concern was about the need for users
[1410.78 --> 1419.72]  to communicate to other clients that something was different in the data space.
[1420.14 --> 1421.28]  For instance, you have a key.
[1421.92 --> 1424.12]  And when this key will be modified,
[1424.72 --> 1427.68]  you want to inform another client
[1427.68 --> 1430.48]  that this modification take place.
[1432.84 --> 1433.74]  So what do you do?
[1433.74 --> 1439.38]  There was the possibility of providing a generic way
[1439.38 --> 1444.00]  to communicate state change in the key space.
[1444.46 --> 1450.00]  So I can create a feature that is able to...
[1450.00 --> 1451.88]  You can listen to a key,
[1452.22 --> 1456.98]  and when this key will get some kind of read, write operation, and so forth,
[1456.98 --> 1460.44]  the listening client will get a message.
[1460.76 --> 1462.06]  But if you think about it,
[1462.56 --> 1464.84]  this is a lot of different use cases.
[1465.28 --> 1469.14]  Do you want to listen for the election of the keys, of this key?
[1469.68 --> 1469.98]  Do you want...
[1470.54 --> 1474.68]  If it's a list and can be changed in many ways,
[1474.92 --> 1477.42]  it can be popped, pushed,
[1477.78 --> 1480.58]  what kind of operations you are interested in?
[1480.58 --> 1487.70]  So it's easy to realize how much involved such an API could start to be.
[1489.00 --> 1493.38]  So PoopSub was also able to solve this kind of problems.
[1493.58 --> 1496.40]  If you want to communicate to some client
[1496.40 --> 1498.62]  that there was a state change in a key,
[1498.92 --> 1502.24]  what you do is to use a address transaction,
[1503.00 --> 1506.24]  that is the sum of multi-indexec command,
[1506.24 --> 1510.44]  and you, inside the transaction, put two commands.
[1510.76 --> 1514.08]  One to actually change your data,
[1514.40 --> 1518.28]  and one to publish in a given channel
[1518.28 --> 1521.32]  the fact that this key was changed.
[1521.96 --> 1525.78]  So basically, we provided a more general form of communication
[1525.78 --> 1530.14]  between clients that can be used to communicate
[1530.14 --> 1536.70]  the changes in the keys,
[1536.78 --> 1538.12]  in the key space,
[1538.48 --> 1541.32]  but it is also more generic than this.
[1541.32 --> 1543.60]  What was interesting is that
[1543.60 --> 1547.22]  after we provided this new feature,
[1547.66 --> 1549.60]  we saw more and more people
[1549.60 --> 1554.08]  switching from messaging solutions to Redis,
[1554.08 --> 1558.44]  because Redis was much more simple to start with,
[1558.80 --> 1561.04]  the performance was very, very good,
[1561.74 --> 1567.96]  and so people started to use Redis as a messaging system.
[1567.96 --> 1569.86]  And at this point,
[1570.28 --> 1572.48]  we have really three kinds of users,
[1573.10 --> 1577.56]  and with big overlaps in these three sets of users.
[1578.00 --> 1581.44]  That is, Redis is used as a database,
[1581.44 --> 1584.10]  Redis is used as messaging,
[1584.62 --> 1589.48]  that is the sum of the least commands,
[1589.96 --> 1591.16]  rescue and so forth,
[1591.50 --> 1592.50]  and pubsub.
[1592.92 --> 1595.34]  And finally, Redis is used as a cache.
[1596.50 --> 1597.88]  There are three businesses
[1597.88 --> 1600.26]  that are going in parallel.
[1601.00 --> 1603.14]  Now that services like Redis2Go
[1603.14 --> 1604.88]  are offering hosted Redis,
[1604.98 --> 1607.32]  and even add-ons for sites like Heroku,
[1607.32 --> 1610.02]  what has that done for the adoption of Redis?
[1610.02 --> 1613.08]  I'm not sure these services
[1613.08 --> 1617.98]  are currently very, very, very useful for users.
[1618.20 --> 1619.18]  The reason is,
[1619.84 --> 1623.04]  I think there is a lot of value in theory
[1623.04 --> 1625.08]  in managing instances
[1625.08 --> 1628.08]  of some kind of software.
[1628.92 --> 1633.02]  But Redis is so simple
[1633.02 --> 1637.24]  to run for the final user,
[1637.24 --> 1642.48]  and these services are usually a bit expensive,
[1642.96 --> 1644.52]  that I'm not sure it makes sense
[1644.52 --> 1647.96]  for many users to adopt this kind of,
[1647.96 --> 1649.84]  to use this kind of services.
[1650.26 --> 1654.82]  So I don't think they are doing a lot
[1654.82 --> 1658.60]  to make Redis more popular.
[1659.16 --> 1661.44]  What I think these services should,
[1661.44 --> 1664.16]  these companies should focus on
[1664.16 --> 1668.10]  is in providing the more value
[1668.10 --> 1669.30]  in these solutions.
[1669.72 --> 1671.42]  More value is backups
[1671.42 --> 1675.58]  to make sure that these instances
[1675.58 --> 1677.90]  are easy to scale,
[1678.22 --> 1680.28]  to make sure that upgrades
[1680.28 --> 1682.90]  are very simple to perform,
[1683.30 --> 1685.36]  and without downtime
[1685.36 --> 1687.26]  from the point of view of users.
[1687.26 --> 1690.40]  There are clear ways to do this.
[1690.50 --> 1691.10]  For instance,
[1691.52 --> 1693.46]  if you have a spare box,
[1693.94 --> 1695.62]  a fresh box you can use,
[1696.04 --> 1698.04]  and you want to upgrade Redis,
[1698.26 --> 1699.44]  you start a new instance
[1699.44 --> 1700.64]  with the new release,
[1701.10 --> 1702.24]  and then you start
[1702.24 --> 1704.64]  the replication process,
[1704.64 --> 1707.78]  and so you switch
[1707.78 --> 1711.80]  instantly the IP address
[1711.80 --> 1712.74]  to the new box,
[1713.46 --> 1714.82]  the one that was the slave,
[1715.00 --> 1716.96]  and you issue a command
[1716.96 --> 1717.88]  to the slave
[1717.88 --> 1719.54]  to turn it into master.
[1719.92 --> 1722.88]  So you upgrade your Redis instance
[1722.88 --> 1726.82]  without any service interruption.
[1727.38 --> 1728.40]  I think the value
[1728.40 --> 1729.88]  is in this kind of services.
[1730.08 --> 1731.40]  So you can say as a user,
[1731.58 --> 1733.30]  okay, I will get this
[1733.30 --> 1735.68]  hosted Redis solution
[1735.68 --> 1737.42]  because I will stop
[1737.42 --> 1739.00]  to think about it.
[1739.30 --> 1740.78]  If I want a bigger instance,
[1741.04 --> 1742.38]  I will just pay more,
[1742.68 --> 1744.36]  and they will do the upgrade
[1744.36 --> 1745.82]  needed to do this
[1745.82 --> 1747.58]  without any kind of interruption
[1747.58 --> 1748.68]  of my services.
[1749.40 --> 1751.74]  I'm sure they will make the backups.
[1752.16 --> 1753.64]  I'm sure they will be able
[1753.64 --> 1756.26]  to rotate my app-end-only file
[1756.26 --> 1758.80]  if I use this kind of persistence model
[1758.80 --> 1762.10]  without problem in the Chrome service,
[1762.10 --> 1765.42]  without problem in the additional memory
[1765.42 --> 1767.24]  used by the background process,
[1767.38 --> 1768.02]  and so forth.
[1768.34 --> 1769.56]  But my impression is that
[1769.56 --> 1771.84]  the current solutions in the market
[1771.84 --> 1773.90]  are not providing all this
[1773.90 --> 1776.14]  interesting added value.
[1776.48 --> 1778.48]  What's the largest Redis installation
[1778.48 --> 1780.02]  that you've come across
[1780.02 --> 1782.44]  as far as memory and other resources?
[1782.44 --> 1785.70]  Well, I'm not sure,
[1785.88 --> 1788.50]  but one of the biggest I remember
[1788.50 --> 1790.32]  I saw currently
[1790.32 --> 1794.64]  was in Blizzard.
[1795.48 --> 1801.86]  Blizzard, the guys from World of Warcraft
[1801.86 --> 1803.76]  are using Redis
[1803.76 --> 1805.86]  to power the front-end
[1805.86 --> 1809.26]  of the web interface,
[1809.40 --> 1812.16]  the mobile interface of the game,
[1812.66 --> 1814.44]  where there are the avatars,
[1814.82 --> 1816.76]  and you can check your avatar,
[1817.32 --> 1819.62]  and it's used to power
[1819.62 --> 1820.96]  this part of site
[1820.96 --> 1824.46]  and to create the 3D renders
[1824.46 --> 1826.16]  that there are in this page.
[1826.16 --> 1827.88]  And they are using
[1827.88 --> 1830.02]  just for this
[1830.02 --> 1833.16]  eight nodes of Redis
[1833.16 --> 1836.56]  with, if I remember correctly,
[1837.08 --> 1840.40]  16 gigabytes of RAM
[1840.40 --> 1842.38]  for instance.
[1843.00 --> 1844.88]  I think there is also
[1844.88 --> 1846.84]  an advertising company,
[1847.06 --> 1849.02]  I'm not remembering very well
[1849.02 --> 1850.18]  what the name is,
[1850.74 --> 1851.78]  that is using
[1851.78 --> 1854.82]  a much larger installation of Redis,
[1854.82 --> 1863.30]  with 64 gigabyte instances of Redis,
[1863.60 --> 1866.28]  and 10 nodes of Redis.
[1866.70 --> 1869.38]  So, I think that
[1869.38 --> 1872.50]  currently the biggest installations
[1872.50 --> 1874.68]  I can report
[1874.68 --> 1879.30]  are about real servers,
[1880.94 --> 1883.62]  and with 10 hosts
[1883.62 --> 1885.66]  in the range of 10 hosts
[1885.66 --> 1888.36]  with many gigabytes of RAM
[1888.36 --> 1889.84]  for every host.
[1890.52 --> 1891.88]  Also, there is
[1891.88 --> 1892.40]  a
[1892.40 --> 1895.38]  DIG
[1895.38 --> 1897.28]  and stack overflow
[1897.28 --> 1899.00]  that are using Redis,
[1899.30 --> 1901.02]  and I think this may be
[1901.02 --> 1903.06]  pretty large installs,
[1903.26 --> 1904.22]  but I'm not sure
[1904.22 --> 1905.80]  exactly how much
[1905.80 --> 1907.44]  Redis servers
[1907.44 --> 1908.56]  and how much memory
[1908.56 --> 1909.06]  is used
[1909.06 --> 1910.92]  for this kind of installations.
[1910.92 --> 1912.62]  I've got a question
[1912.62 --> 1913.16]  from Twitter.
[1913.28 --> 1914.68]  Justin Campbell wants to know
[1914.68 --> 1916.98]  if VMware plans
[1916.98 --> 1918.18]  to include Redis
[1918.18 --> 1919.56]  in a future product release.
[1920.52 --> 1920.70]  Well,
[1920.94 --> 1922.22]  I think
[1922.22 --> 1922.90]  that
[1922.90 --> 1924.38]  there is the idea
[1924.38 --> 1925.48]  to use Redis
[1925.48 --> 1927.06]  to provide services
[1927.06 --> 1928.66]  inside VMware,
[1928.98 --> 1930.36]  some kind of services.
[1930.36 --> 1930.72]  services.
[1932.62 --> 1934.58]  So, I really hope
[1934.58 --> 1935.52]  we will see
[1935.52 --> 1936.52]  soon
[1936.52 --> 1938.10]  something interesting
[1938.10 --> 1939.38]  about Redis
[1939.38 --> 1940.00]  and VMware.
[1940.48 --> 1941.76]  But, for sure,
[1942.08 --> 1943.26]  there is a lot of
[1943.26 --> 1944.50]  interest
[1944.50 --> 1946.52]  inside VMware
[1946.52 --> 1947.70]  about Redis,
[1947.70 --> 1949.22]  and there are people
[1949.22 --> 1949.94]  working
[1949.94 --> 1951.28]  to solutions
[1951.28 --> 1952.08]  that will
[1952.08 --> 1954.54]  use Redis
[1954.54 --> 1957.38]  both internally
[1957.38 --> 1958.64]  and
[1958.64 --> 1960.22]  as
[1960.22 --> 1960.84]  exposed
[1960.84 --> 1961.48]  service.
[1962.18 --> 1963.16]  So, you're in Italy,
[1964.06 --> 1964.66]  and for those
[1964.66 --> 1965.22]  that think
[1965.22 --> 1966.30]  that you have
[1966.30 --> 1967.28]  to be in San Francisco
[1967.28 --> 1967.90]  or somewhere
[1967.90 --> 1970.04]  with a larger
[1970.04 --> 1970.64]  tech scene
[1970.64 --> 1971.48]  to create
[1971.48 --> 1972.32]  a popular
[1972.32 --> 1973.88]  open source
[1973.88 --> 1974.30]  project,
[1974.44 --> 1974.98]  how did you go
[1974.98 --> 1975.62]  about spreading
[1975.62 --> 1975.96]  the word
[1975.96 --> 1976.56]  about Redis?
[1976.56 --> 1978.26]  I think that
[1978.26 --> 1979.54]  it was
[1979.54 --> 1981.78]  very, very strange
[1981.78 --> 1982.74]  the curve
[1982.74 --> 1983.82]  of popularity
[1983.82 --> 1984.80]  of Redis.
[1985.32 --> 1986.96]  It was something
[1986.96 --> 1987.92]  I learned
[1987.92 --> 1988.78]  about
[1988.78 --> 1989.90]  from
[1989.90 --> 1990.84]  because
[1990.84 --> 1992.08]  when I released
[1992.08 --> 1993.42]  the first version
[1993.42 --> 1994.26]  of Redis,
[1994.46 --> 1995.48]  it was very, very
[1995.48 --> 1995.96]  simple.
[1996.56 --> 1997.12]  A few
[1997.12 --> 1999.46]  lines of code
[1999.46 --> 2000.52]  demonstrating
[2000.52 --> 2001.82]  the first
[2001.82 --> 2003.56]  ideas
[2003.56 --> 2004.44]  that was
[2004.44 --> 2005.24]  get,
[2005.48 --> 2005.82]  set,
[2005.82 --> 2006.42]  and
[2006.42 --> 2006.92]  a few
[2006.92 --> 2007.62]  operations
[2007.62 --> 2008.38]  about
[2008.38 --> 2009.10]  lists.
[2009.92 --> 2010.98]  I had
[2010.98 --> 2011.84]  this prototype.
[2012.44 --> 2013.06]  This prototype
[2013.06 --> 2013.88]  was already
[2013.88 --> 2014.60]  working
[2014.60 --> 2016.32]  inside my
[2016.32 --> 2017.28]  production
[2017.28 --> 2017.92]  system,
[2018.46 --> 2018.96]  and I
[2018.96 --> 2020.50]  put
[2020.50 --> 2021.08]  a
[2021.08 --> 2022.00]  homepage
[2022.00 --> 2022.76]  for it,
[2023.30 --> 2023.60]  and
[2023.60 --> 2025.76]  posted it
[2025.76 --> 2026.04]  in
[2026.04 --> 2026.96]  Hacker News.
[2027.80 --> 2028.48]  When I posted
[2028.48 --> 2029.04]  it in
[2029.04 --> 2029.58]  Hacker News,
[2029.70 --> 2030.16]  there was a
[2030.16 --> 2030.92]  very good
[2030.92 --> 2031.82]  response
[2031.82 --> 2033.02]  from people.
[2033.02 --> 2033.86]  And
[2033.86 --> 2034.76]  especially
[2034.76 --> 2036.56]  Ezra
[2036.56 --> 2037.80]  Zygmuntowicz,
[2038.46 --> 2039.56]  that is now
[2039.56 --> 2039.98]  working
[2039.98 --> 2041.96]  for VMware
[2041.96 --> 2042.72]  as well.
[2043.28 --> 2043.44]  Well,
[2043.54 --> 2044.18]  I think
[2044.18 --> 2044.80]  Ezra
[2044.80 --> 2046.00]  did a
[2046.00 --> 2046.74]  really huge
[2046.74 --> 2047.52]  difference
[2047.52 --> 2049.02]  in the
[2049.02 --> 2049.94]  popularity
[2049.94 --> 2050.64]  of Redis
[2050.64 --> 2051.46]  in the first
[2051.46 --> 2052.36]  months of the
[2052.36 --> 2053.34]  life of Redis.
[2053.34 --> 2053.98]  because,
[2054.38 --> 2055.58]  after all,
[2055.88 --> 2056.58]  you can't
[2056.58 --> 2057.76]  expect all
[2057.76 --> 2058.32]  the people
[2058.32 --> 2059.92]  out here
[2059.92 --> 2060.48]  to be
[2060.48 --> 2061.66]  so brave
[2061.66 --> 2062.40]  to use
[2062.40 --> 2063.10]  a new
[2063.10 --> 2064.00]  solution
[2064.00 --> 2066.18]  without
[2066.18 --> 2067.06]  any kind
[2067.06 --> 2067.78]  of guru
[2067.78 --> 2069.02]  that is
[2069.02 --> 2070.18]  somewhat
[2070.18 --> 2072.42]  popularizing
[2072.42 --> 2073.10]  this solution.
[2073.50 --> 2073.86]  And then
[2073.86 --> 2074.32]  there was
[2074.32 --> 2074.84]  GitHub.
[2075.22 --> 2075.62]  GitHub
[2075.62 --> 2077.06]  started to
[2077.06 --> 2078.12]  use Redis
[2078.12 --> 2080.76]  in interesting
[2080.76 --> 2081.32]  ways,
[2081.68 --> 2082.04]  and to
[2082.04 --> 2082.86]  make users
[2082.86 --> 2084.06]  aware of
[2084.06 --> 2084.50]  this kind
[2084.50 --> 2085.70]  of uses.
[2086.26 --> 2086.80]  I think
[2086.80 --> 2087.54]  you really
[2087.54 --> 2087.96]  need,
[2088.72 --> 2089.78]  in your
[2089.78 --> 2090.82]  initial
[2090.82 --> 2092.54]  user base,
[2093.00 --> 2093.46]  a few
[2093.46 --> 2094.66]  brave users.
[2095.04 --> 2095.60]  But users
[2095.60 --> 2096.26]  are not
[2096.26 --> 2096.94]  brave just
[2096.94 --> 2097.48]  because they
[2097.48 --> 2098.24]  are hazard
[2098.24 --> 2099.24]  those with
[2099.24 --> 2099.86]  their production
[2099.86 --> 2100.42]  systems.
[2101.02 --> 2101.48]  The reason
[2101.48 --> 2102.56]  is I think
[2102.56 --> 2103.08]  that when
[2103.08 --> 2104.58]  an hacker
[2104.58 --> 2105.02]  is very
[2105.02 --> 2105.38]  good,
[2105.82 --> 2106.44]  it starts
[2106.44 --> 2106.96]  to be
[2106.96 --> 2107.54]  confident
[2107.54 --> 2108.50]  that he
[2108.50 --> 2109.00]  can pick
[2109.00 --> 2109.40]  the good
[2109.40 --> 2110.06]  solutions
[2110.06 --> 2110.66]  for
[2110.66 --> 2112.74]  modeling
[2112.74 --> 2113.72]  his
[2113.72 --> 2114.22]  problems.
[2114.54 --> 2114.94]  Then when
[2114.94 --> 2115.56]  you start
[2115.56 --> 2116.14]  to have
[2116.14 --> 2117.06]  a few
[2117.06 --> 2119.26]  interesting
[2119.26 --> 2120.34]  users in
[2120.34 --> 2120.92]  your user
[2120.92 --> 2121.34]  base,
[2121.78 --> 2122.14]  they will
[2122.14 --> 2122.60]  start to
[2122.60 --> 2123.28]  be like
[2123.28 --> 2124.52]  a green
[2124.52 --> 2125.40]  light for
[2125.40 --> 2125.80]  all the
[2125.80 --> 2126.80]  other users.
[2127.48 --> 2128.14]  But so
[2128.14 --> 2128.54]  Redis
[2128.54 --> 2129.18]  started to
[2129.18 --> 2129.96]  get adoption
[2129.96 --> 2131.04]  every day
[2131.04 --> 2131.54]  more and
[2131.54 --> 2131.88]  more and
[2131.88 --> 2132.84]  more for
[2132.84 --> 2133.76]  the first
[2133.76 --> 2136.20]  two or
[2136.20 --> 2136.98]  three months.
[2137.54 --> 2138.50]  then there
[2138.50 --> 2139.82]  was a
[2139.82 --> 2141.46]  stop in
[2141.46 --> 2142.16]  the adoption
[2142.16 --> 2142.70]  rate of
[2142.70 --> 2143.04]  Redis.
[2143.44 --> 2143.74]  Okay,
[2143.92 --> 2144.52]  there was
[2144.52 --> 2145.14]  a few
[2145.14 --> 2146.78]  users using
[2146.78 --> 2147.16]  it,
[2147.60 --> 2148.02]  a few
[2148.02 --> 2148.90]  new users,
[2149.30 --> 2149.78]  but I
[2149.78 --> 2150.30]  clearly
[2150.30 --> 2152.64]  was saying
[2152.64 --> 2153.38]  that there
[2153.38 --> 2153.90]  was a
[2153.90 --> 2154.78]  stop in
[2154.78 --> 2155.48]  the adoption
[2155.48 --> 2156.54]  rate of
[2156.54 --> 2157.18]  new users.
[2157.64 --> 2157.98]  So what
[2157.98 --> 2158.68]  I did
[2158.68 --> 2160.36]  was to
[2160.36 --> 2161.30]  reconsider it.
[2161.68 --> 2162.50]  I started
[2162.50 --> 2163.12]  to think,
[2163.50 --> 2164.32]  so maybe
[2164.32 --> 2164.96]  this is
[2164.96 --> 2165.96]  after all
[2165.96 --> 2166.88]  not really
[2166.88 --> 2167.60]  interesting
[2167.60 --> 2168.72]  for most
[2168.72 --> 2169.24]  users,
[2169.84 --> 2170.74]  but then
[2170.74 --> 2171.76]  I realized
[2171.76 --> 2172.96]  that actually
[2172.96 --> 2174.84]  I really
[2174.84 --> 2176.14]  trusted the
[2176.14 --> 2177.12]  project and
[2177.12 --> 2179.00]  continued the
[2179.00 --> 2179.90]  development,
[2180.38 --> 2181.12]  even if it
[2181.12 --> 2182.36]  was completely
[2182.36 --> 2183.44]  a free effort
[2183.44 --> 2184.28]  at the time,
[2184.92 --> 2186.10]  and it
[2186.10 --> 2186.64]  was a lot
[2186.64 --> 2187.28]  of work.
[2187.28 --> 2188.08]  It started
[2188.08 --> 2188.92]  to be
[2188.92 --> 2190.00]  almost a
[2190.00 --> 2190.44]  full-time
[2190.44 --> 2191.74]  job after
[2191.74 --> 2192.04]  a few
[2192.04 --> 2192.46]  months,
[2193.04 --> 2193.84]  and I
[2193.84 --> 2195.18]  pushed more
[2195.18 --> 2195.48]  and more
[2195.48 --> 2196.00]  features,
[2196.16 --> 2196.76]  more work,
[2196.90 --> 2197.46]  created a
[2197.46 --> 2197.68]  better
[2197.68 --> 2198.44]  implementation,
[2198.76 --> 2199.24]  and so
[2199.24 --> 2199.52]  forth.
[2199.98 --> 2201.42]  And users
[2201.42 --> 2203.22]  started to
[2203.22 --> 2204.38]  actually
[2204.38 --> 2205.38]  acknowledge
[2205.38 --> 2206.20]  all this
[2206.20 --> 2207.06]  work and
[2207.06 --> 2208.04]  started to
[2208.04 --> 2209.26]  adopt it
[2209.26 --> 2209.68]  more and
[2209.68 --> 2209.86]  more.
[2210.10 --> 2210.50]  So I
[2210.50 --> 2210.86]  think there
[2210.86 --> 2211.74]  are like
[2211.74 --> 2212.46]  two different
[2212.46 --> 2212.92]  stages.
[2213.34 --> 2213.98]  One stage
[2213.98 --> 2214.40]  is the
[2214.40 --> 2215.46]  wow stage,
[2215.80 --> 2216.30]  when you
[2216.30 --> 2217.30]  put this
[2217.30 --> 2217.84]  project in
[2217.84 --> 2218.24]  the Anchor
[2218.24 --> 2218.72]  News front
[2218.72 --> 2219.04]  page,
[2219.18 --> 2219.58]  and people
[2219.58 --> 2219.90]  say,
[2220.02 --> 2220.16]  oh,
[2220.26 --> 2220.70]  but this
[2220.70 --> 2221.04]  is cool,
[2221.04 --> 2223.08]  I could
[2223.08 --> 2223.68]  have uses
[2223.68 --> 2224.18]  for this
[2224.18 --> 2224.56]  project,
[2224.66 --> 2224.88]  and so
[2224.88 --> 2225.20]  forth.
[2225.66 --> 2228.26]  Then the
[2228.26 --> 2229.08]  hype will
[2229.08 --> 2229.70]  stop for
[2229.70 --> 2230.12]  a bit.
[2230.46 --> 2230.86]  Then you
[2230.86 --> 2231.44]  need to
[2231.44 --> 2232.64]  carry this
[2232.64 --> 2234.58]  environment,
[2234.90 --> 2235.96]  this small
[2235.96 --> 2237.42]  child into
[2237.42 --> 2238.38]  something more
[2238.38 --> 2238.80]  big,
[2239.26 --> 2240.06]  more supported,
[2240.86 --> 2242.06]  with more
[2242.06 --> 2244.16]  real world
[2244.16 --> 2244.94]  usable.
[2245.48 --> 2246.12]  And this
[2246.12 --> 2246.64]  is really
[2246.64 --> 2247.80]  hard work.
[2248.14 --> 2248.64]  And during
[2248.64 --> 2249.90]  this time,
[2250.28 --> 2250.66]  you should
[2250.66 --> 2251.18]  try to
[2251.18 --> 2252.62]  give up.
[2253.82 --> 2254.54]  You should
[2254.54 --> 2255.32]  try to
[2255.32 --> 2256.98]  put more
[2256.98 --> 2257.34]  and more
[2257.34 --> 2258.00]  value to
[2258.00 --> 2258.68]  your project.
[2259.02 --> 2259.72]  And eventually
[2259.72 --> 2260.76]  users will
[2260.76 --> 2262.52]  recognize
[2262.52 --> 2264.78]  that this
[2264.78 --> 2265.30]  work and
[2265.30 --> 2265.74]  will start
[2265.74 --> 2266.36]  to trust
[2266.36 --> 2266.98]  this solution
[2266.98 --> 2267.38]  more and
[2267.38 --> 2267.62]  more.
[2267.80 --> 2268.48]  When you're
[2268.48 --> 2268.94]  not busy
[2268.94 --> 2269.52]  hacking on
[2269.52 --> 2269.94]  Redis,
[2270.16 --> 2271.02]  what tools
[2271.02 --> 2271.42]  in the
[2271.42 --> 2271.96]  open source
[2271.96 --> 2272.70]  world do
[2272.70 --> 2272.92]  you want
[2272.92 --> 2273.18]  to play
[2273.18 --> 2273.46]  with?
[2274.00 --> 2275.56]  I like
[2275.56 --> 2275.98]  a lot
[2275.98 --> 2276.56]  programming
[2276.56 --> 2277.12]  languages.
[2277.12 --> 2277.24]  languages.
[2277.96 --> 2278.42]  This was
[2278.42 --> 2279.28]  one of
[2279.28 --> 2284.44]  my biggest
[2284.44 --> 2286.44]  interests
[2286.44 --> 2287.06]  before
[2287.06 --> 2288.24]  Redis was
[2288.24 --> 2288.68]  for sure
[2288.68 --> 2289.06]  programming
[2289.06 --> 2289.56]  languages.
[2289.56 --> 2290.60]  So what
[2290.60 --> 2291.30]  I like is
[2291.30 --> 2292.40]  to download
[2292.40 --> 2293.82]  some new
[2293.82 --> 2294.66]  language and
[2294.66 --> 2295.42]  to try
[2295.42 --> 2296.08]  what is
[2296.08 --> 2296.66]  different
[2296.66 --> 2297.92]  from all
[2297.92 --> 2298.26]  the other
[2298.26 --> 2299.02]  languages I
[2299.02 --> 2299.36]  know.
[2299.70 --> 2300.16]  What of
[2300.16 --> 2301.06]  these ideas
[2301.06 --> 2301.84]  I can
[2301.84 --> 2302.64]  somewhat
[2302.64 --> 2304.06]  use in
[2304.06 --> 2305.12]  my code
[2305.12 --> 2306.30]  written for
[2306.30 --> 2307.28]  languages not
[2307.28 --> 2309.10]  explicitly
[2309.10 --> 2310.28]  supporting
[2310.28 --> 2311.00]  these new
[2311.00 --> 2312.14]  ideas but
[2312.14 --> 2312.94]  many times
[2312.94 --> 2313.40]  you can
[2313.40 --> 2314.86]  adapt this
[2314.86 --> 2316.06]  concept even
[2316.06 --> 2316.38]  if your
[2316.38 --> 2317.10]  language is
[2317.10 --> 2318.18]  not completely
[2318.18 --> 2319.38]  intended for
[2319.38 --> 2320.22]  these kind
[2320.22 --> 2320.68]  of things.
[2321.16 --> 2321.72]  So I
[2321.72 --> 2322.44]  really enjoy
[2322.44 --> 2324.52]  in general
[2324.52 --> 2325.08]  programming
[2325.08 --> 2325.68]  languages.
[2326.32 --> 2327.16]  Well thanks
[2327.16 --> 2327.52]  for taking
[2327.52 --> 2327.90]  the time.
[2328.02 --> 2328.16]  I know
[2328.16 --> 2329.24]  it's in
[2329.24 --> 2329.60]  the evening
[2329.60 --> 2330.20]  over in
[2330.20 --> 2330.94]  Italy and
[2330.94 --> 2331.42]  surely
[2331.42 --> 2331.96]  appreciate
[2331.96 --> 2332.82]  finally getting
[2332.82 --> 2333.34]  to catch up
[2333.34 --> 2333.66]  with you and
[2333.66 --> 2334.02]  this is one
[2334.02 --> 2334.26]  of those
[2334.26 --> 2335.02]  episodes that
[2335.02 --> 2336.18]  is going to
[2336.18 --> 2336.56]  be difficult
[2336.56 --> 2337.12]  to sit on
[2337.12 --> 2337.48]  for a week
[2337.48 --> 2337.88]  before we
[2337.88 --> 2338.58]  publish but
[2338.58 --> 2339.44]  thanks again.
[2340.14 --> 2340.46]  Thank you.
[2343.90 --> 2344.68]  Thank you for
[2344.68 --> 2345.12]  listening to
[2345.12 --> 2345.52]  The Change
[2345.52 --> 2345.80]  Log.
[2345.94 --> 2346.46]  This episode
[2346.46 --> 2346.92]  is sponsored
[2346.92 --> 2347.78]  by LessConf.
[2348.16 --> 2348.82]  LessConf is a
[2348.82 --> 2349.22]  conference for
[2349.22 --> 2349.74]  people who do
[2349.74 --> 2350.62]  amazing things
[2350.62 --> 2351.08]  and that means
[2351.08 --> 2351.30]  you.
[2351.72 --> 2352.24]  Take advantage
[2352.24 --> 2352.82]  of early bird
[2352.82 --> 2353.48]  pricing right
[2353.48 --> 2353.92]  now until
[2353.92 --> 2354.98]  February 14th.
[2354.98 --> 2355.22]  Head to
[2355.22 --> 2356.10]  lessconf.com to
[2356.10 --> 2356.86]  learn more and
[2356.86 --> 2357.20]  register.
[2357.42 --> 2357.70]  Thanks for
[2357.70 --> 2357.94]  listening.
[2361.42 --> 2362.60]  It's when
[2362.60 --> 2365.02]  I found
[2365.02 --> 2365.80]  myself
[2365.80 --> 2366.98]  for the
[2366.98 --> 2368.42]  first time
[2368.42 --> 2370.70]  Safe in
[2370.70 --> 2372.14]  your arms
[2372.14 --> 2373.70]  As a dark
[2373.70 --> 2374.40]  passion
[2374.40 --> 2375.86]  shone
[2375.86 --> 2378.64]  Was mine
[2378.64 --> 2380.26]  alone
[2380.26 --> 2382.74]  Open
[2382.74 --> 2384.02]  Open
[2384.02 --> 2386.02]  Open
[2386.02 --> 2394.96]  Open
[2394.96 --> 2395.46]  Open
[2395.46 --> 2396.00]  Open
[2396.00 --> 2396.32]  Open
[2396.32 --> 2396.82]  Open
[2396.82 --> 2397.06]  Open
[2397.06 --> 2397.40]  Open
[2397.40 --> 2397.44]  Open
[2397.44 --> 2398.44]  Open
[2398.44 --> 2398.48]  Open
[2398.48 --> 2399.04]  Open
[2399.04 --> 2400.00]  Polar
[2400.00 --> 2400.56]  Open
[2400.56 --> 2402.52]  Open
[2402.52 --> 2404.42]  Open
[2404.42 --> 2404.98]  Open
[2404.98 --> 2405.54]  Open
[2405.54 --> 2406.88]  Open
[2406.88 --> 2407.62]  Open
[2407.62 --> 2408.38]  Open
[2408.38 --> 2408.76]  Open
[2408.76 --> 2409.90]  Open
[2409.90 --> 2410.82]  Open
[2410.82 --> 2411.46]  Open
[2411.46 --> 2411.50]  Open
[2411.50 --> 2415.46]  Open
[2415.46 --> 2415.50]  Open
[2415.50 --> 2415.56]  Open
[2415.58 --> 2415.98]  Open
[2415.98 --> 2416.00]  Open
