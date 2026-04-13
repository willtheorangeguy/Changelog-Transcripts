[0.00 --> 4.20]  Hey, I'm Chris Anderson. I'm a big Change Log listener and so are you.
[4.52 --> 7.50]  I work on CouchDB and this is the CouchDB theme song.
[11.44 --> 17.06]  CouchDB! CouchDB! CouchDB! CouchDB! Relax!
[30.00 --> 59.98]  Don't push me away!
[60.00 --> 65.38]  I'm just here at Diddy. If you're on Twitter, follow us at Change Log Show, not the Change Log.
[65.64 --> 67.12]  And I am Adam Stack.
[67.64 --> 72.06]  And I am Penguin, P-E-N-G-W-Y-N-N, Whiskey Yankee, November, November.
[72.62 --> 78.74]  Cool episode this week. So much fun participating in the NoSQL Big Data Smackdown.
[79.14 --> 82.12]  Brought to you by InfoChimps and Rackspace at South by Southwest.
[82.72 --> 86.68]  Let's give a hand to J. Chris first for that awesome CouchDB theme song.
[86.80 --> 88.50]  Yeah, that was pretty wild.
[88.50 --> 90.62]  And you like to dance even better.
[91.08 --> 94.14]  Yeah, there was a dancing company with that. It's a shame that...
[94.14 --> 95.34]  Did we get it on video?
[96.10 --> 100.06]  I don't think we did. It's like half Running Man, half Wedding Chicken song.
[100.24 --> 103.58]  Yeah, it was some oddity. I don't know. It had some Tigger in there too somewhere.
[104.04 --> 104.76]  Bouncing all around.
[105.02 --> 106.92]  Such a fun time at the Smackdown.
[107.08 --> 108.98]  You know, the lineup for the Smackdown.
[108.98 --> 115.22]  We got together and debated the merits of each of these higher-end NoSQL data stores.
[115.82 --> 117.26]  Stu Hood from Cassandra.
[117.72 --> 119.74]  Jan Lennart from CouchDB.
[120.04 --> 124.16]  Myself representing MongoDB as the best fanboy that I could be.
[124.32 --> 132.48]  And Vern Wogels from Amazon, the CTO of Amazon, which I found out later who he was after he joined us from the peanut gallery about, what, five minutes in?
[133.28 --> 137.26]  It was about five minutes in and he came in and started putting the smackdown on you guys.
[137.44 --> 139.38]  He did. Clearly the alpha geek in the room.
[140.70 --> 144.46]  We did get video of the event. Hopefully we can do something fun with that and post it later.
[144.84 --> 151.22]  Yeah. Well, we would have done this with the video in mind because that was actually the intention was to post a video of it.
[151.78 --> 157.34]  But, man, I had some troubles getting that video exported in the right way and I hate video.
[157.80 --> 160.18]  It's hard to do it when you're on-site at a conference anyway.
[160.18 --> 167.42]  We just got back from South by Southwest within the last 48 hours or so trying to catch our breath from a fun conference.
[167.52 --> 168.66]  What a fun conference down in Austin.
[169.10 --> 170.34]  Yeah. It was an awesome conference.
[170.44 --> 171.24]  It's been a lot of good people.
[171.74 --> 173.72]  Geez, we met Tony Hsieh passing by.
[173.84 --> 175.18]  We met Guy Kawasaki.
[175.98 --> 182.16]  We met up with Technowini, a.k.a. Rick Olson, and met up with a lot of people.
[182.42 --> 182.96]  It was a lot of fun.
[183.06 --> 185.56]  A couple of guys flagging us down saying, hey, listen to the changelog.
[185.76 --> 189.02]  So it made us feel good we have at least a dozen listeners out there or so.
[189.02 --> 190.12]  Gave out some shirts.
[190.60 --> 190.96]  We did.
[191.50 --> 194.54]  Kind of bummed that we won't get to JSConf this year, it looks like.
[194.68 --> 201.10]  So write your congressman, voice your outrage that we won't cover the coolest JavaScript conference this year.
[201.44 --> 204.92]  Yeah, a sudden turn of events leaves us in a lurch not being able to make it there.
[205.28 --> 209.48]  No solution in sight yet, but I'm hopeful.
[209.48 --> 211.32]  We've got a busy docket this year.
[211.46 --> 215.94]  Chirp and Texas JS and perhaps RailsConf.
[216.06 --> 219.00]  We'll see a full docket already.
[219.12 --> 226.44]  Hoping to get out to OSCON in July at OSCON and let them know that the changelog needs to represent the conference.
[226.90 --> 227.22]  That's right.
[227.30 --> 229.62]  Yeah, sometimes the crowd can help us, I suppose, right?
[229.62 --> 241.12]  Speaking of crowd, you know, the crowd is fully involved in the SmackDown, as you'll hear in the interview, as is kind of a rogue bird that was sitting right by the microphone the whole time.
[241.14 --> 241.86]  Yeah, I did hear that bird.
[242.84 --> 243.78]  Well, it's a fun episode.
[243.88 --> 244.46]  Should we get to it?
[244.66 --> 245.44]  Yeah, one time.
[245.44 --> 255.60]  Questions that you have immediately.
[256.38 --> 259.30]  Hopefully they'll be relevant, but, you know, anything.
[259.44 --> 261.14]  Anything you're curious about.
[262.02 --> 267.28]  So, right now we have Cassandra, MongoDB, and CouchDB represented.
[268.40 --> 270.22]  Everyone's claiming that they're NoSQL.
[270.80 --> 274.24]  Nobody really knows what the exact definition of NoSQL is.
[274.24 --> 276.18]  It means many different things.
[276.34 --> 277.30]  It means data models.
[277.70 --> 278.82]  It means replication.
[280.16 --> 281.72]  It means, what else, scaling.
[282.98 --> 288.12]  So, first up, let's talk a little bit about the data model.
[289.04 --> 293.94]  So, Cassandra has a really interesting data model that allows massively wide rows.
[294.98 --> 297.60]  And, I mean, we're all document stores, right?
[299.40 --> 302.14]  So, what do you guys think about huge documents?
[302.14 --> 304.80]  They're flying huge.
[305.36 --> 307.56]  Huge, like as large as a machine can fit.
[307.78 --> 308.28]  They're awesome.
[309.18 --> 309.40]  Yay.
[310.06 --> 315.90]  I guess the definition of a document differs than in Cassandra and CouchDB.
[316.04 --> 319.54]  I don't know that much about Cassandra, but CouchDB can handle big documents,
[319.62 --> 324.02]  but we tend to think of them as small items, small entities that you handle individually.
[324.02 --> 329.54]  I believe Mongo's got a four gig per document rule limit.
[329.54 --> 331.52]  If I'm, not four gig, four meg.
[331.78 --> 332.68]  No, four gig.
[333.00 --> 333.44]  MongoDB.
[333.80 --> 334.04]  Sorry.
[334.38 --> 334.72]  MongoDB.
[335.08 --> 335.20]  Right.
[335.94 --> 336.18]  Right.
[336.30 --> 336.62]  Four banks.
[337.68 --> 337.94]  Okay.
[338.34 --> 344.38]  And so everyone is, everyone, all these other competitors use JSON and kind of are untyped.
[344.38 --> 346.88]  I don't like that.
[347.30 --> 348.64]  I don't like that they're untyped.
[348.78 --> 352.40]  I mean, because you can do massively interesting things if you have type data.
[352.64 --> 355.54]  I mean, it might be sorted, so you can slice little pieces out of it.
[355.76 --> 357.10]  That's something that Cassandra provides.
[357.26 --> 364.24]  So, if you have a document and it allows it to grow large because you might want to get just a little piece of your document out.
[365.02 --> 370.04]  Mongo actually uses the VSON spec, so it is pseudo-typed at the file system level.
[370.04 --> 373.40]  So, it's got, it's not just strings in the database.
[373.60 --> 374.18]  You have ints.
[374.24 --> 375.72]  You have other database types.
[375.82 --> 379.56]  You can even store files in the file system, grid.fs.
[380.18 --> 380.34]  Yeah.
[380.48 --> 381.48]  CoachDB uses JSON.
[381.90 --> 384.80]  It does have a bunch of data types.
[385.20 --> 389.36]  The nice thing about JSON is it's a subset of all the programming language that we're using.
[389.46 --> 393.70]  It's the lowest common denominator that everybody can serialize objects into in exchange.
[393.80 --> 398.04]  So, I can have a Java object and serialize it into JSON, load it up in Python, and can just work with it
[398.04 --> 404.64]  without having like thousands and thousands of lines of code who does some object translation between some arcade format and something else.
[404.72 --> 406.70]  So, JSON is really, really good for data in exchange.
[407.24 --> 407.86]  But it's slow!
[408.30 --> 408.62]  What?
[409.52 --> 411.50]  Oh, so he says it's slow.
[411.50 --> 418.00]  So, Bobby Polito from the Python community wrote a JSON compiler, a JSON module for Python,
[418.10 --> 422.26]  which is actually faster than the protocol buffers Google claims are so fast.
[422.32 --> 422.88]  So, shut up.
[428.04 --> 428.36]  All right?
[428.62 --> 432.42]  So, I believe we disagree on typed, and that's fine with me.
[434.10 --> 435.42]  I want to add to the typed.
[435.66 --> 442.16]  The web is not really typed, and people who are using the web are usually not, I hope, most of them are not computer scientists.
[442.46 --> 444.20]  Like, sorry to all the computer scientists and me.
[444.68 --> 449.10]  But you should, like, it's great that you use the web, but the web is something that enables everybody to share data
[449.10 --> 451.00]  or to express themselves in some way.
[451.68 --> 458.20]  And having them to teach about data types is really just like, it's just an arcane artifact of programming.
[458.50 --> 461.24]  They shouldn't think about how do I store arrays and objects and stuff.
[461.32 --> 463.54]  They should just stuff whatever they have into a database.
[463.64 --> 464.50]  They should not think about it.
[464.96 --> 465.06]  So.
[466.64 --> 471.02]  I would hope that the people that are developing web applications are computer scientists, but maybe not.
[471.22 --> 471.60]  I don't know.
[471.82 --> 472.32]  There should be.
[472.32 --> 479.66]  So, there was an argument yesterday, I guess, that the iPhone app store has over 100,000 applications on it.
[480.06 --> 483.88]  And when GeoCities was shut down, it had over 100,000 websites on it.
[484.26 --> 490.84]  So, it's a different magnitude of scale if you let everybody participate in the open web.
[491.40 --> 496.52]  So, you definitely do want to have everybody who has an interest in doing web stuff doing web stuff
[496.52 --> 499.90]  and not restricted to the, like, getting it right computer sciences type.
[499.90 --> 502.48]  Because I'm really bored of all the stuff we come up with.
[502.86 --> 507.46]  And the amateurs really have no clue what everything is about doing the real cool and interesting applications.
[509.48 --> 510.46]  That's a lot of crap.
[511.54 --> 511.90]  Awesome.
[512.18 --> 512.42]  Yeah.
[512.52 --> 513.28]  Let me explain why.
[513.38 --> 517.20]  You know, so, how many programming languages do you know that are completely untimed?
[517.56 --> 518.24]  Except for Perl.
[521.44 --> 521.80]  Yeah.
[521.80 --> 524.96]  So, everybody that's developing applications actually has types.
[525.28 --> 527.88]  And suddenly you go to the database and all your types disappear.
[528.66 --> 529.80]  That's not true.
[530.90 --> 531.96]  Jason defines types.
[532.04 --> 532.50]  You can do that.
[532.54 --> 537.18]  But you don't have to worry about it as much as if you're like, you don't have to go up front and define, okay, this.
[537.58 --> 542.36]  I will need an array of integers to store whatever list I'm having.
[542.40 --> 543.70]  You don't have to think about that that much.
[544.02 --> 547.34]  It's easier for a programmer to do it naturally than for a non-programmer even more.
[547.40 --> 551.08]  Yeah, but you force everybody to rewrite all their programs with these things in mind.
[551.24 --> 551.48]  So?
[551.48 --> 552.54]  So, yeah.
[552.84 --> 553.76]  Well, that's a lot of work.
[553.82 --> 555.78]  There seem to be quite a few programs out there.
[555.94 --> 557.68]  You know, GUC, this exists.
[557.96 --> 558.12]  Yeah?
[558.20 --> 559.04]  And all these other things.
[559.12 --> 560.76]  So, what about this compatibility stuff?
[560.84 --> 565.90]  Why do you guys force, you know, everybody to rewrite all their applications?
[566.46 --> 567.86]  I'm just playing devil's advocate here.
[567.86 --> 568.62]  No, absolutely.
[568.88 --> 570.10]  Well, so also, Hadoop.
[570.22 --> 573.26]  Hadoop is completely unstructured by default, right?
[573.30 --> 575.04]  So you throw anything in it and then you process it.
[575.24 --> 576.70]  You can do something similar with CouchDB.
[577.14 --> 580.70]  So, I don't know why I'm defending CouchDB, but I just want to point that out.
[581.82 --> 583.10]  Type doesn't always win.
[583.46 --> 583.78]  Magnostic!
[583.78 --> 589.44]  So, there's a lot of, I think, for many of these things, Cohen, it's not actually about
[589.44 --> 589.72]  type.
[590.22 --> 594.66]  It also, when you look at consistency models and things like that, where traditional database
[594.66 --> 597.72]  applications, you know, are used to a very different model.
[597.90 --> 602.74]  So, you either have to rewrite your applications, fixing, according to the new model, whether
[602.74 --> 608.78]  it's type or whether it's a consistency model or, you know, other things around it.
[609.58 --> 611.52]  Suddenly, you force everybody to rethink.
[611.64 --> 612.64]  Now, that may be a good thing.
[612.88 --> 612.96]  Right.
[612.96 --> 613.72]  Yeah?
[614.00 --> 615.70]  But it definitely hurts adoption.
[616.62 --> 617.06]  Yeah.
[617.22 --> 619.02]  So, let's talk about consistency really quickly.
[619.96 --> 621.42]  Let's talk about the different models.
[621.76 --> 628.04]  Cassandra has kind of a peer-to-peer model that comes from Werner's brainchild, Dynamo,
[628.40 --> 633.50]  where any node can accept a write and then if enough nodes have accepted the write, then
[633.50 --> 634.14]  the write succeeds.
[634.28 --> 635.06]  Otherwise, it doesn't.
[635.32 --> 637.16]  And at real time, you resolve all that.
[637.74 --> 641.38]  I don't know about, I don't know how I feel about the CouchDB and Mongo models.
[641.38 --> 644.32]  I mean, Mongo hasn't actually figured that part out, right?
[644.92 --> 645.56]  I mean...
[645.56 --> 645.86]  That's right.
[645.92 --> 648.30]  There's a two-second delay before you actually commit to the database.
[648.42 --> 649.02]  Is that what you're talking about?
[649.94 --> 650.34]  No.
[650.56 --> 653.82]  So, I believe Mongo is still master-slave type replication.
[654.08 --> 654.32]  Sure.
[654.54 --> 654.80]  Sure.
[654.80 --> 659.34]  I must admit, core committers to these projects, and I'm just a Microsoft...
[659.34 --> 659.90]  I mean, a...
[659.90 --> 660.30]  Microsoft?
[660.54 --> 661.38]  Mongo fanboy.
[661.50 --> 662.54]  It used to be a Microsoft fanboy.
[662.68 --> 662.96]  Uh-oh.
[663.16 --> 664.52]  But the M word.
[666.50 --> 667.62]  Define a little bit what you're talking about.
[667.66 --> 669.34]  Let's see if I can defend it just as an end user.
[669.80 --> 670.06]  Okay.
[670.06 --> 675.82]  So, if you have a data center in Washington and you have another data center in California,
[676.32 --> 679.18]  you can do a write in one of those data centers.
[679.54 --> 683.84]  And even if the other data center is down, depending on your tunables, you can still succeed that
[683.84 --> 684.10]  write.
[684.62 --> 688.68]  Because no one of those nodes is actually responsible at a given time.
[688.88 --> 690.10]  Like, it's not...
[690.10 --> 692.00]  There's no one dedicated to a particular key.
[692.48 --> 692.70]  Right.
[692.78 --> 694.26]  And in this case, advantage Cassandra.
[694.26 --> 697.84]  But, you know, I would argue in most applications, that's not needed.
[697.84 --> 698.16]  Oh.
[699.58 --> 700.56]  Wow, wow, wow, wow.
[702.20 --> 703.16]  It's not...
[703.16 --> 707.40]  Actually, the whole consistency model, the eventual consistency model, doesn't come from
[707.40 --> 710.82]  the fact that this is something that you want at the application level.
[711.10 --> 714.50]  It is basically abstractions from the implementation leaking up.
[715.26 --> 716.62]  The fact that...
[716.62 --> 717.86]  There's two reasons for replication.
[718.04 --> 725.30]  Either you do it for gaining fault tolerance, or you do it for getting a higher level of concurrency
[725.30 --> 728.40]  so you can get better read throughput, or write report, or whatever.
[729.04 --> 730.86]  For those two reasons, you have to replicate.
[731.28 --> 733.02]  If you have to replicate, you have to make a decision.
[733.14 --> 734.56]  Do I write to all replicas?
[735.24 --> 736.56]  And guarantee to all...
[736.56 --> 740.50]  Guarantee to write to all web replicas, such that my reads are always consistent?
[741.18 --> 742.94]  That might not be a well-performing issue.
[743.04 --> 746.76]  Because, you know, at writes, you know, you get a huge cost.
[746.76 --> 750.84]  And especially if you cannot get your quorum, you know, you may have to fail your writes.
[750.84 --> 755.30]  And there's a number of applications where that may not be useful for you.
[755.56 --> 762.98]  So these are things that are actually leaking up from the implementation through the APIs.
[763.60 --> 766.42]  If everybody could get a choice, everybody would want strong consistency.
[767.36 --> 771.26]  It's just that with strong consistency means that you have to take a lot of other trade-offs.
[771.68 --> 774.50]  The main one being not being able to get much write throughput,
[774.78 --> 779.12]  and the other one is being that there's a number of failure scenarios in which you will be dead in order.
[779.12 --> 781.38]  So are you saying that Dynamo wasn't user-friendly?
[782.32 --> 783.28]  No, absolutely not.
[784.26 --> 785.04]  No, no, actually.
[785.58 --> 790.58]  So there's a range of things, I think.
[790.84 --> 794.22]  So Dynamo is sort of one of the systems that predates a number of these.
[795.56 --> 798.76]  And where we made consistency models explicit.
[799.08 --> 803.40]  It's not that we were the first one to store for an eventually consistent system.
[803.56 --> 807.40]  I think, actually, most relational databases give you eventual consistency.
[807.40 --> 811.90]  You just don't know it, mainly because if you use replication in a traditional relational database,
[812.22 --> 815.66]  like one of the commercial ones, there's a delay when the logs are being shipped.
[815.98 --> 819.48]  And if you read from the slave, you do not get the consistency.
[819.76 --> 821.14]  There's always a window.
[821.82 --> 825.54]  But, okay, so why wasn't Dynamo user-friendly?
[825.74 --> 832.24]  It's not only for the consistency level, but also, for example, because you have to have the key if you came to the database.
[832.24 --> 836.26]  There's no way to do a list to figure out what are my keys.
[836.60 --> 837.64]  So you have to have a key.
[837.98 --> 839.58]  And the key normally comes from somewhere else.
[839.64 --> 842.40]  For example, through a customer database where we developed it.
[843.06 --> 847.46]  So when we developed Dynamo, it was to support shopping carts.
[847.50 --> 848.52]  That was one of the use cases.
[848.52 --> 853.08]  So that meant you went to the database, you went to the storage system, and you really had a key.
[855.08 --> 860.92]  And that's why, for example, S3 is a user-friendly key-value storage system.
[861.26 --> 863.64]  But Dynamo actually isn't that much user-friendly.
[864.06 --> 865.42]  With S3, you can do a list.
[865.56 --> 869.54]  You can do a prefix list on what are my keys and then find things out.
[869.90 --> 871.52]  That stuff, for example, is not in...
[873.04 --> 874.64]  What's the name of that one?
[874.64 --> 879.06]  Isn't S3 built on Dynamo?
[879.36 --> 879.66]  What?
[880.44 --> 882.44]  Isn't S3 built on Dynamo?
[884.06 --> 884.76]  No comment.
[885.22 --> 885.66]  Damn it.
[885.90 --> 886.06]  Yeah.
[886.98 --> 887.40]  Uh...
[887.40 --> 888.80]  No, show...
[888.80 --> 892.58]  Uh-oh.
[895.64 --> 896.08]  Hey!
[897.44 --> 898.12]  What are you doing?
[898.70 --> 899.88]  Show up!
[901.32 --> 902.64]  There's a ball color in here.
[902.64 --> 908.90]  You weren't expecting to get started, so soon, were you?
[908.98 --> 909.86]  You got stuck over here.
[910.04 --> 910.36]  No!
[910.60 --> 911.28]  You're right in there.
[911.58 --> 911.74]  Yeah.
[912.24 --> 916.40]  So the answer is no, because if you would be an engineer, you would be a developer, you
[916.40 --> 916.88]  would figure...
[916.88 --> 921.06]  You would know that if you have to do a list operator on top of this, that's a completely
[921.06 --> 922.34]  different internal architecture.
[922.60 --> 926.80]  So is Dynamo used and Dynamo principles used throughout all of these systems on Amazon
[926.80 --> 928.26]  where you have to get enormous scale?
[928.60 --> 928.88]  Yes.
[928.88 --> 929.74]  Yeah?
[930.04 --> 933.56]  Whether the system in itself, as we described, it was mainly built from the shopping cart
[933.56 --> 933.92]  first.
[934.26 --> 937.54]  But all of these things consist of modules that are being reused throughout the whole
[937.54 --> 937.78]  company.
[938.04 --> 941.90]  It's more the principles that matter than the actual implementation.
[942.68 --> 945.96]  So I would say that Cassandra is actually a little bit more user-friendly in that case
[945.96 --> 946.88]  because we...
[946.88 --> 946.94]  Absolutely.
[947.32 --> 947.58]  Yeah.
[947.58 --> 947.86]  Okay.
[947.86 --> 952.20]  We're not using hashing in order to determine where a key lives.
[953.24 --> 955.40]  So you can actually do those list operations.
[955.72 --> 961.06]  You can basically treat it like you would Bigtable from Google and get a list of all of your keys.
[961.80 --> 966.28]  I imagine you can do that with the competitors, but Cassandra's implementation is better.
[966.28 --> 971.80]  So I like that you guys all focus on the big data problem on the massive scale and on all
[971.80 --> 974.48]  the websites that have these problems, which are like seven.
[976.48 --> 981.24]  CatchDB is more like the personal database, something that you can use for whatever you
[981.24 --> 981.66]  want to do.
[982.00 --> 986.80]  It doesn't force you to think in these big...
[986.80 --> 988.50]  to have these big thoughts.
[988.90 --> 994.34]  But if you start out small, CatchDB allows you to grow gradually with whatever usage pattern
[994.34 --> 995.68]  you have, so we are...
[995.68 --> 996.80]  I think we are...
[996.80 --> 1000.86]  These guys are building Ferraris and DragStars, so we are building a hundred record of databases
[1000.86 --> 1004.06]  that everybody can use but can get along with for a long, long time.
[1004.54 --> 1004.98]  Absolutely.
[1005.12 --> 1005.40]  Absolutely.
[1005.62 --> 1007.68]  And there's a reason that Couch rhymes with ouch.
[1009.30 --> 1015.12]  You know, anybody that's used Mongo coming from CouchDB, it's just night and day as far
[1015.12 --> 1019.86]  as the ease of use in getting set up, getting the server installed, finding wrappers for
[1019.86 --> 1020.68]  your language of choice.
[1020.68 --> 1024.94]  And suddenly, you know, I don't have to know what I'm going to ask for up front.
[1025.06 --> 1029.34]  It reminds me of the Seinfeld episode when Kramer's doing the movie phone and he says,
[1029.66 --> 1031.70]  why don't you just tell me the movie you want to watch, right?
[1031.98 --> 1033.86]  It's the same thing with your views up front.
[1033.94 --> 1036.70]  You have to materialize these up front, but with Mongo, you know, I can just...
[1036.70 --> 1040.24]  So you're saying you have indexes magically appear with no performance?
[1040.36 --> 1041.66]  Well, indexes are one thing, right?
[1041.72 --> 1043.22]  But views are something totally different, right?
[1043.28 --> 1046.82]  So when I set an index, yeah, it takes effect for that index to kick in, right?
[1046.82 --> 1047.68]  It takes time for...
[1047.68 --> 1048.80]  Nobody can cheat for that.
[1048.88 --> 1053.96]  But I can get around it if I have a low, you know, edge case where I need to do a query.
[1054.18 --> 1056.66]  With Couch, I have to know what that view is.
[1056.84 --> 1057.84]  You can have that hard query with Couch.
[1057.84 --> 1063.12]  Yeah, but realistically, anything beyond, you know, dynamic and Couch just...
[1063.12 --> 1065.80]  In my own experience, just haven't been, you know, it's like all in one.
[1066.02 --> 1067.14]  Oh, you should try New Year's.
[1067.22 --> 1068.68]  Okay, maybe I need to upgrade.
[1069.42 --> 1070.52]  It's supposed to be as HD.
[1070.52 --> 1074.44]  So let me tell you why all of these guys suck.
[1075.72 --> 1076.16]  Yes!
[1076.74 --> 1079.48]  Because you should not run your own database.
[1080.24 --> 1081.46]  That time has passed.
[1081.84 --> 1088.20]  These guys force you to run your own database, to manage replication, to go dive deep into that.
[1088.54 --> 1090.80]  You should all of this have to be a service.
[1091.16 --> 1092.62]  How can you, you know...
[1092.62 --> 1093.90]  Well, how do you...
[1093.90 --> 1097.00]  The cloud is awesome, but what do you do if your DSL provider crats out?
[1097.04 --> 1098.68]  What do you do when the 3G is not?
[1098.86 --> 1101.16]  What if you're on AT&T and you have no more coverage?
[1101.22 --> 1102.10]  How do you reach the cloud?
[1102.20 --> 1103.04]  You're dead in the water.
[1103.18 --> 1103.86]  You're dead in the water.
[1103.86 --> 1106.26]  With a really great cloud that you have that nobody can reach.
[1106.52 --> 1109.14]  You go to a bar and you have a few beers.
[1109.22 --> 1110.28]  You come back and...
[1110.28 --> 1110.52]  Exactly.
[1111.00 --> 1114.66]  And your customers will lead you left and right if you're offline.
[1114.82 --> 1117.86]  Well, you know, given that we've been doing this for a while, I think our customers...
[1118.48 --> 1121.48]  I kind of have an idea what customers do in this particular case.
[1121.48 --> 1122.88]  But again, you're one of the...
[1122.88 --> 1122.98]  No.
[1122.98 --> 1124.50]  You're one of the seven sides who...
[1124.50 --> 1125.32]  No, no, no, no, no.
[1125.34 --> 1129.22]  But what is more, if you aggregate all these customers that we have, whether you have S3,
[1129.60 --> 1133.40]  Simple TV, you know, EBS and all the other services, you should no longer...
[1133.40 --> 1135.70]  I mean, these guys, you are wasting your time.
[1136.30 --> 1137.20]  You know, and I love it.
[1137.24 --> 1137.88]  You know, this stuff.
[1138.00 --> 1140.58]  I really love this data stuff and these databases.
[1140.76 --> 1143.24]  I would build 10 more Dynamo's.
[1143.34 --> 1143.66]  Yeah?
[1143.84 --> 1145.44]  Because it is really, really cool.
[1145.70 --> 1147.34]  But you're not solving your customers' problems.
[1147.40 --> 1147.64]  Exactly.
[1147.64 --> 1150.98]  Because you're forcing them to do a lot of operational skills.
[1150.98 --> 1152.58]  I agree with you wholeheartedly.
[1153.02 --> 1153.38]  Awesome.
[1154.06 --> 1154.88]  You shouldn't...
[1154.88 --> 1155.60]  You shouldn't...
[1155.60 --> 1158.60]  People who use databases shouldn't use...
[1158.60 --> 1160.06]  We want to use stuff.
[1160.32 --> 1161.44]  They shouldn't think about the database.
[1161.52 --> 1162.38]  It's something they would use.
[1162.70 --> 1166.86]  Part of the thing we're doing is abstracting the database away to build very, very cool applications
[1166.86 --> 1170.20]  and getting CouchDB into all the deployments you can think of.
[1170.28 --> 1173.66]  That when you want to build something, it's already there and can just use it.
[1173.84 --> 1174.94]  You don't have to think about it.
[1174.94 --> 1178.84]  Like, my mom should be able to run a CouchDB server without knowing that she runs a CouchDB server.
[1179.08 --> 1180.26]  That's the thing we're trying to do.
[1180.30 --> 1181.50]  We should not run a database.
[1181.70 --> 1182.98]  That's nothing you would ever want to do.
[1183.46 --> 1185.86]  Remember, guys, if you guys have any questions, just throw up a hand.
[1186.02 --> 1187.04]  I mean, I'm sure you have comments.
[1187.04 --> 1188.84]  We'll chat real quick, but there.
[1188.84 --> 1195.24]  Also, so the comments on the seven biggest sites, like, don't you guys want to be the next biggest site?
[1195.46 --> 1197.40]  Or you want to be the number one site.
[1197.58 --> 1198.80]  So why would you build...
[1198.80 --> 1202.04]  Actually, I would like to really argue against the seven biggest sites.
[1202.38 --> 1204.12]  If I look at the amount of data...
[1204.12 --> 1205.04]  I mean, everybody here...
[1205.04 --> 1205.46]  Right, seven people.
[1205.46 --> 1207.64]  Because you all think about big data, right?
[1207.80 --> 1208.54]  That's why we're here.
[1208.86 --> 1212.30]  And how many of you work not for the biggest seven sites?
[1213.00 --> 1214.38]  I think most of you, don't you?
[1214.56 --> 1214.74]  Yeah?
[1215.34 --> 1215.78]  Yeah.
[1216.04 --> 1218.32]  So there's tons of data out there.
[1218.32 --> 1219.64]  Everybody has this big data.
[1219.78 --> 1225.06]  The time where small data sets were normal, I mean, everybody has petabytes data sets.
[1225.12 --> 1226.38]  And that's only the start of it.
[1226.54 --> 1227.70]  It's also a controlled thing.
[1228.22 --> 1231.58]  If Amazon, if Google, if Apple, if all these people own all your data.
[1231.66 --> 1232.46]  Facebook, for example.
[1232.52 --> 1233.24]  They own all your data.
[1233.34 --> 1234.40]  They own all the URLs.
[1234.86 --> 1237.70]  The web wasn't meant to be a couple of big silos.
[1237.86 --> 1240.06]  People should be in control of their own data.
[1240.12 --> 1242.00]  They should be able to use their own data as they fit.
[1242.24 --> 1244.72]  They should be able to put it under the URLs they control.
[1244.72 --> 1250.74]  So instead of being under the whatever these guys are doing, to screw them over.
[1250.88 --> 1252.16]  It's a big privacy issue.
[1252.50 --> 1253.04]  It's another thing.
[1253.04 --> 1253.14]  No.
[1253.82 --> 1254.68]  Oh, it definitely is.
[1255.04 --> 1260.00]  There's a bunch of privacy laws in Germany that I cannot use S3 to store user data.
[1260.00 --> 1260.90]  Yes, you can.
[1261.18 --> 1261.76]  Oh, you can't?
[1261.92 --> 1262.80]  Yes, you can.
[1262.90 --> 1263.10]  Okay.
[1263.26 --> 1263.50]  Stop.
[1263.76 --> 1264.06]  Stop.
[1264.10 --> 1264.38]  Yes.
[1264.60 --> 1265.12]  Let me see.
[1265.12 --> 1268.56]  The September 1 law in Germany, the new privacy law.
[1268.66 --> 1269.30]  No, it's not the new one.
[1269.50 --> 1269.78]  Yes.
[1270.02 --> 1274.60]  Has the definition of a data processor where or not, yes or no, you can use that.
[1274.82 --> 1278.48]  And so with S3, you can use it as a data processor.
[1279.76 --> 1285.50]  I'm thinking about a very specific policy where in Germany, if I'm asking somebody to delete all my data,
[1285.50 --> 1288.36]  he needs to be able to prove that everything is deleted.
[1288.36 --> 1295.10]  If it's somewhere in the cloud, stored somewhere in S3 on some data center that the U.S. government has access to at any time.
[1295.22 --> 1296.14]  No, that's not true.
[1296.46 --> 1299.40]  As you know, and at least Amazon does, I don't know whether it's for the other guys,
[1299.70 --> 1306.80]  we comply with safe harbor rules, which means that if you follow the data protection direction, the directorate of the EU,
[1307.22 --> 1308.72]  we follow safe harbor rules.
[1308.82 --> 1315.80]  There's an explicit number of lists of things that you have to do when the government comes to you and asks for access to this data,
[1315.80 --> 1321.26]  which is to notify you, to give you the ability to retrieve your data or to remove your data before other ones get access.
[1321.36 --> 1323.76]  There's very explicit rules around this.
[1324.00 --> 1327.72]  Werner, the rest of us agree against you in the sense that we're open source.
[1328.30 --> 1330.96]  So anyone can host our application, right?
[1331.54 --> 1332.98]  But they still have to host it.
[1333.04 --> 1335.26]  Yeah, we'd love to use you for your virtual private server.
[1335.52 --> 1340.88]  No, no, I'm more than happy that you guys, when Cassandra and Mongo and others on Amazon Institute,
[1341.38 --> 1343.68]  which you can do with EBS and tons of people do these kind of things,
[1343.68 --> 1346.34]  yet you're wasting your time because that's not what you should be doing.
[1346.42 --> 1348.54]  You should be building better value for your customers.
[1348.96 --> 1350.90]  And it is by not focusing on your database.
[1352.24 --> 1354.52]  That's what we're doing with the local databases.
[1354.74 --> 1357.52]  We're giving, like, take Salesforce as an example.
[1357.86 --> 1359.86]  Everybody who's used Salesforce is making a lot of money.
[1359.98 --> 1363.20]  If Salesforce goes down, an entire industry is unable to use stuff.
[1363.52 --> 1366.96]  If you have an offline version of Salesforce that would, for example, use...
[1366.96 --> 1368.48]  How often did Salesforce go down?
[1368.56 --> 1369.26]  Oh, it does happen.
[1369.26 --> 1370.72]  And Salesforce...
[1370.72 --> 1371.58]  Sorry, sorry, sorry.
[1371.88 --> 1373.68]  Salesforce doesn't even have to go down for that.
[1373.78 --> 1375.40]  You need to have a connection to Salesforce.
[1375.92 --> 1378.82]  And again, if your cable provider, if your cell provider craps out,
[1378.86 --> 1380.58]  who's a happy Comcast customer?
[1381.44 --> 1381.84]  Exactly.
[1383.42 --> 1388.80]  So are you arguing that Amazon should allow you to download the entire Amazon database
[1388.80 --> 1390.22]  and then shop locally?
[1390.76 --> 1392.42]  It should allow users...
[1392.42 --> 1393.20]  And buy things locally?
[1393.54 --> 1393.96]  Yes!
[1394.10 --> 1394.42]  Yes!
[1395.22 --> 1395.80]  Well, okay.
[1396.68 --> 1398.02]  Can I hack it on the plane?
[1398.02 --> 1398.84]  I guess that's the question.
[1398.98 --> 1401.52]  When you fly back from South by Southwest, can I hack the application?
[1401.80 --> 1402.04]  Exactly.
[1402.14 --> 1402.76]  But another question.
[1403.12 --> 1407.04]  So, you know, we go back to the seven biggest sites things for a moment.
[1407.14 --> 1412.12]  You know, I hear NoSQL often, and, you know, the popular blog post a couple weeks ago
[1412.12 --> 1415.78]  talking about how MySQL can scale and the NoSQL line and all of this stuff.
[1415.88 --> 1418.96]  But, you know, we're kind of like in what we were with Web 2.0 a few years ago
[1418.96 --> 1421.10]  where we have this term out here that we haven't really defined.
[1421.54 --> 1424.14]  How many people think NoSQL means big and scaling?
[1424.14 --> 1425.86]  All right.
[1426.04 --> 1429.28]  How many people think non-relational schemeless?
[1430.48 --> 1430.94]  All right.
[1431.00 --> 1431.74]  A few more hands.
[1431.80 --> 1435.42]  And I think that's the distinction that we've got to put some sort of definition to this
[1435.42 --> 1439.32]  term NoSQL so that we can, when we have smackdowns like this, we can agree with what we're
[1439.32 --> 1439.74]  arguing about.
[1439.78 --> 1440.02]  All right.
[1440.26 --> 1445.36]  I think NoSQL is about choice of data storage, which we're wasting our time on.
[1445.36 --> 1450.74]  But if I'm building an application that needs very fast logging, I'm looking at memcache and
[1450.74 --> 1451.78]  Redis and MongoDB.
[1451.98 --> 1455.02]  If I need something that has offline peer-to-peer replication, I'm looking at CouchDB.
[1455.40 --> 1459.82]  If I'm looking at something that needs to be hosted and I shouldn't think about it, I
[1459.82 --> 1462.04]  look at S3 and the other stuff Amazon and other people are doing.
[1462.48 --> 1466.40]  If I have hundreds and thousands of servers that I need to keep busy, I look at Hadoop or Xandre.
[1466.70 --> 1469.08]  Well, I would like to point out that this is a big data meetup.
[1469.08 --> 1472.68]  And SimpleDB, I think, has a 10 gigabyte limit?
[1473.10 --> 1473.84]  Per domain.
[1474.12 --> 1474.64]  Per domain.
[1475.16 --> 1475.64]  Well, okay.
[1475.94 --> 1479.54]  So basically what you have to do is you have to do your own partitioning.
[1480.20 --> 1480.60]  Right.
[1480.70 --> 1482.34]  I'm not saying that any...
[1482.34 --> 1483.68]  Do your own partitioning.
[1484.08 --> 1484.30]  Okay.
[1484.84 --> 1486.08]  So let me...
[1486.08 --> 1491.60]  So when I think about NoSQL and given that we have some history in this or what I think
[1491.60 --> 1498.42]  before came before SQL was that for a very long time, the database, any data storage,
[1498.42 --> 1504.70]  and whether it was a database or whether it was just storage, the default application
[1504.70 --> 1507.98]  to use there or the default service to use there was a relational database because there
[1507.98 --> 1508.54]  was nothing else.
[1508.62 --> 1512.76]  Maybe you can have some B2B, but I mean, those are basically the only two choices.
[1513.00 --> 1519.54]  Now, what drove us to start building different types of databases is because if you look closer
[1519.54 --> 1525.46]  at how your processing is and you can decompose processing into different steps, you see that
[1525.46 --> 1529.62]  for most of those different steps, you have different data storage requirements.
[1530.38 --> 1535.60]  And that for each of those different requirements, you can find a very dedicated solution that
[1535.60 --> 1542.06]  is capable of being very fast, very reliable, while doing the generic thing, throwing all
[1542.06 --> 1543.72]  requirements into one big bucket.
[1544.12 --> 1548.50]  You end up with something, actually technology that has been developed in the 80s, where we
[1548.50 --> 1553.10]  expect to have 21st century scaling and performance out of.
[1553.10 --> 1554.06]  That's impossible.
[1554.06 --> 1556.26]  And so that was the thing that drives it.
[1556.26 --> 1560.00]  And if I look at the things that Amazon offers, it's not necessarily that I think that Simple
[1560.00 --> 1562.56]  DB is the one and only table solution.
[1562.56 --> 1563.56]  No.
[1563.56 --> 1566.22]  It is a bucket of tools that you get these days.
[1566.22 --> 1570.50]  You have S3, you have Simple DB, you have maybe you want to run, you want some RAM caching.
[1570.50 --> 1575.50]  But the most important is that we now have a whole range of solutions that people can pick from.
[1575.50 --> 1577.50]  So you said impossible.
[1577.50 --> 1578.50]  I wouldn't say impossible.
[1578.50 --> 1580.50]  I would say just not discovered yet.
[1580.50 --> 1583.50]  I mean, you can't, you can't, or relational.
[1583.50 --> 1586.50]  Well, there are ways to implement things that are somewhat relational on top of these scores.
[1586.50 --> 1588.50]  Okay, so, but not breaking the model.
[1588.50 --> 1589.50]  Yeah?
[1589.50 --> 1595.50]  So for example, if you want to do, implement everything like inner transactions, like multi-level
[1595.50 --> 1597.50]  views and all of these kind of things.
[1597.50 --> 1598.50]  Absolutely.
[1598.50 --> 1601.50]  Without breaking existing application, you cannot.
[1601.50 --> 1606.50]  So this was, you know, if we couldn't build an absolutely infinite scalable relational database
[1606.50 --> 1610.50]  and kept all of the running programs intact, we would have done it.
[1610.50 --> 1611.50]  Right.
[1611.50 --> 1612.50]  Absolutely.
[1612.50 --> 1614.50]  And we, CapTheorem, I'm sure everyone has heard of it.
[1614.50 --> 1615.50]  CapTheorem, we all agree.
[1615.50 --> 1617.50]  I don't think any of us have transactions.
[1617.50 --> 1620.50]  So I mean, we'll just, we'll skip right over that, right?
[1620.50 --> 1624.50]  Well, except, ah, so now Simple DB has transactions.
[1624.50 --> 1625.50]  Now?
[1625.50 --> 1627.50]  But, ah, atomic gets inputs, isn't it?
[1627.50 --> 1628.50]  No, no, no, no, no, yes.
[1628.50 --> 1630.50]  You have conditional inputs.
[1630.50 --> 1631.50]  Conditional, okay.
[1631.50 --> 1635.50]  Which, which are actually in the line with eventual consistency, yeah?
[1635.50 --> 1640.50]  Here, you actually, if you cannot figure out the consistency model, you ask the system
[1640.50 --> 1642.50]  to do this for you, yeah?
[1642.50 --> 1646.50]  And remember, under the covers, Simple DB is still an eventual consistent system.
[1646.50 --> 1651.50]  It is just that there's a number of operations on top of that with a different failure model,
[1651.50 --> 1653.50]  that, that you can use both.
[1653.50 --> 1655.50]  Let, let's talk data size real briefly.
[1655.50 --> 1659.50]  Um, I'd just like to point out that we have users of Cassandra that are storing multiple
[1659.50 --> 1661.50]  terabytes of data per node.
[1661.50 --> 1664.50]  So, how do you guys respond to that?
[1664.50 --> 1665.50]  How many users are doing that?
[1665.50 --> 1668.50]  We have, ah, at least three or four.
[1668.50 --> 1673.50]  Twitter and Dig and, um, Reddit are probably all using multiple, well, you know, gigabytes.
[1673.50 --> 1674.50]  Facebook.
[1674.50 --> 1677.50]  We've got a couple of these.
[1677.50 --> 1680.50]  Meibo and the BBC, one of the biggest ones, that do multi-terabyte sizes.
[1680.50 --> 1681.50]  Maybe not on a single box.
[1681.50 --> 1685.50]  Cashmere definitely supports that, but, like, these guys haven't run into the, they aren't
[1685.50 --> 1688.50]  one of the seven biggest, so they're not there yet.
[1688.50 --> 1692.50]  So, how many of those sites started on a system of that scale?
[1692.50 --> 1695.50]  And would we have them today if they had?
[1695.50 --> 1699.50]  If they had, if they had seen the future, they probably would have started on Cassandra.
[1699.50 --> 1700.50]  Oh, magic!
[1700.50 --> 1704.50]  I don't know, you know, there's, there's, we, we, we like to believe that it's only the big
[1704.50 --> 1706.50]  sites that have big data.
[1706.50 --> 1710.50]  But think about anybody that builds a Facebook game these days.
[1710.50 --> 1711.50]  Yeah?
[1711.50 --> 1715.50]  That means that you can go from zero to 25 million users in a month.
[1715.50 --> 1717.50]  Yeah, start a, start a lot of optimism.
[1717.50 --> 1721.50]  And so, imagine all the logging you need to do, all the objects you need to keep around,
[1721.50 --> 1722.50]  all these things you need to do.
[1722.50 --> 1726.50]  Running into petabytes of data is something that you do very, very, very quickly these,
[1726.50 --> 1727.50]  these days.
[1727.50 --> 1728.50]  Yeah?
[1728.50 --> 1730.50]  You run a marketing campaign on the web.
[1730.50 --> 1732.50]  A marketing campaign is no longer just a website.
[1732.50 --> 1737.50]  It's a website, it's video, it's user contributed content, it's casual gaming, it is integration
[1737.50 --> 1739.50]  into social networks, all of these things.
[1739.50 --> 1741.50]  That's a modern marketing campaign.
[1741.50 --> 1747.50]  All the data that those things generate, you're talking about terabytes of data quickly.
[1747.50 --> 1748.50]  That's a good point.
[1748.50 --> 1752.50]  So let's talk about some of the, the use cases and the scenarios that you would need
[1752.50 --> 1755.50]  in most applications that do just, just that thing.
[1755.50 --> 1762.50]  Can you, Cassandra or couch, and I don't know the answer to this, update documents partially?
[1762.50 --> 1764.50]  Do I have to get the whole document before I can update it?
[1764.50 --> 1767.50]  Are those positional updates and incrementals and things?
[1767.50 --> 1768.50]  Yeah.
[1768.50 --> 1769.50]  Okay.
[1769.50 --> 1770.50]  Are those new?
[1770.50 --> 1771.50]  No, it's been in full while.
[1771.50 --> 1772.50]  Okay, okay.
[1772.50 --> 1773.50]  And yeah, Cassandra can.
[1773.50 --> 1776.50]  I mean, we can have very, very large rows, so obviously you're not pushing the whole row
[1776.50 --> 1777.50]  at once.
[1777.50 --> 1778.50]  People can just insert more things.
[1778.50 --> 1781.50]  People build indexes within a single row for the rest of their data.
[1781.50 --> 1786.50]  What sort of operators are built in to do that for you automatically to do things like
[1786.50 --> 1790.50]  incrementing a value, adding something to an array, updating a key and a hash?
[1790.50 --> 1792.50]  Let me call you Bob for a second.
[1792.50 --> 1794.50]  You write a JavaScript function for that.
[1794.50 --> 1799.50]  Yeah, I mean, I can drop down and do that in Mongo too, but I mean, there's convenience
[1799.50 --> 1800.50]  is what I'm putting out.
[1800.50 --> 1804.50]  We have a very small set of a standard library to put these functions, but we're like, users
[1804.50 --> 1807.50]  have not asked for that a lot, a whole lot.
[1807.50 --> 1810.50]  So it is expandable, of course, but we don't have a lot of that yet.
[1810.50 --> 1813.50]  Okay, so let me ask you guys another question.
[1813.50 --> 1815.50]  So you're open source.
[1815.50 --> 1816.50]  Yeah.
[1816.50 --> 1821.50]  So if you put out a new release, do your customers have to take your database down?
[1821.50 --> 1822.50]  No.
[1822.50 --> 1823.50]  No.
[1823.50 --> 1825.50]  So explain how you do it.
[1825.50 --> 1827.50]  Well, so what did you expect?
[1827.50 --> 1831.50]  So we, CacheBit is a very robust file format and everything since the last three versions
[1831.50 --> 1833.50]  use the same file format so you don't have to do any upgrades.
[1833.50 --> 1836.50]  So the server can deal with the same thing that you're actually doing.
[1836.50 --> 1841.50]  So CacheBit has a very robust file system, a file system storage model that has been
[1841.50 --> 1844.50]  stable for a couple of versions so whenever you upgrade, you never have to change anything
[1844.50 --> 1847.50]  without your, with your existing setup.
[1847.50 --> 1849.50]  On top of that, CacheBit is built in Erlang.
[1849.50 --> 1851.50]  Who's a fan of Erlang here?
[1851.50 --> 1852.50]  Woohoo!
[1852.50 --> 1859.50]  Erlang has the capacity, has the, has a feature that allows you to upgrade a version at
[1859.50 --> 1863.50]  runtime so it can run two versions at the same time while serving an database without
[1863.50 --> 1866.50]  having to take it down so it has live upgrades built in.
[1866.50 --> 1872.50]  So Cassandra, I mean we're changing the file format soon.
[1872.50 --> 1874.50]  You will have to restart the cluster.
[1874.50 --> 1879.50]  I mean saying that you'll never have to change the file format is kind of, you know.
[1879.50 --> 1882.50]  So what happens then if you have 10,000 nodes running?
[1882.50 --> 1883.50]  You can do a rolling restart.
[1883.50 --> 1884.50]  Yeah?
[1884.50 --> 1885.50]  That's the thing.
[1885.50 --> 1888.50]  How long does this rolling restart take?
[1888.50 --> 1891.50]  Just from a practical point of view, we've done these things a few times.
[1891.50 --> 1893.50]  I mean what else do operations folks have to do?
[1893.50 --> 1894.50]  I mean it's fun.
[1894.50 --> 1895.50]  No, I'm kidding.
[1895.50 --> 1896.50]  Honestly.
[1896.50 --> 1900.50]  So this is one more case why you should not be worried about this stuff.
[1900.50 --> 1902.50]  You know, use this storage as a service man.
[1902.50 --> 1904.50]  This is, this is old fashioned.
[1904.50 --> 1906.50]  This is so 1990s.
[1906.50 --> 1907.50]  I disagree.
[1907.50 --> 1913.50]  So with Cassandra, with Cassandra you can, you can run a single node incredibly easy.
[1913.50 --> 1915.50]  You can get a second node started incredibly easy.
[1915.50 --> 1916.50]  It can be anywhere.
[1916.50 --> 1919.50]  They're data center, you know, locality aware.
[1919.50 --> 1922.50]  Well I mean we have 45 node installs.
[1922.50 --> 1925.50]  All of, I mean Twitter is running on 45 nodes.
[1925.50 --> 1928.50]  And, but yeah, you know, Facebook had 150.
[1928.50 --> 1934.50]  It's easy enough to grow your cluster that I think it may be more difficult to use EC2
[1934.50 --> 1937.50]  than it is to, to manage your Cassandra cluster.
[1937.50 --> 1943.50]  I'd like to tag, I'd like to tag in J. Chris from the Catch Me Project who's got a few things to say.
[1943.50 --> 1948.50]  I'm talking about that, I'm breaking the rules, but I just wanted to bring the debate up a notch.
[1948.50 --> 1951.50]  So all this they've been talking about as far as I'm concerned, this is geek stuff.
[1951.50 --> 1952.50]  I'm not, I don't care.
[1952.50 --> 1956.50]  I'm a developer, I write Erlang, but you shouldn't have to worry about any of this.
[1956.50 --> 1958.50]  Your database is yours.
[1958.50 --> 1959.50]  It lives at the edge.
[1959.50 --> 1960.50]  It's your data.
[1960.50 --> 1962.50]  Replication means any copy of the data.
[1962.50 --> 1963.50]  You can move it around.
[1963.50 --> 1965.50]  You can build workflows on top of replication.
[1965.50 --> 1968.50]  None of these guys, they're all zigging.
[1968.50 --> 1969.50]  We're zagging.
[1969.50 --> 1972.50]  So I would really, I would like to see some people talking about the use case.
[1972.50 --> 1977.50]  I want to share photos with grandma and I don't want to ask Mark Zuckerberg for any favors.
[1977.50 --> 1983.50]  Stuff it in S3 because then you get URLs that are just completely addressable from the web.
[1983.50 --> 1985.50]  You don't need any intermediary servers.
[1985.50 --> 1988.50]  You know, key value, just web addressable stuff.
[1988.50 --> 1989.50]  That's the way to go.
[1989.50 --> 1991.50]  Does grandma know how to use curl?
[1991.50 --> 1994.50]  I mean, I don't know.
[1994.50 --> 1997.50]  I assume you're going to develop an app for her.
[1997.50 --> 2000.50]  But next up.
[2000.50 --> 2005.50]  So in terms of performance, I don't even know if we need to talk about it because I think
[2005.50 --> 2007.50]  Cassandra has you guys topped.
[2007.50 --> 2015.50]  So CapsDB doesn't optimize for single query performance.
[2015.50 --> 2019.50]  So everything might just be fast enough, not as fast as it can get.
[2019.50 --> 2034.50]  But by the properties that running systems come with, it can handle thousands and ten thousand, maybe a hundred thousand concurrent connections and have a constant stream of performance out of whatever your hardware supports without falling over.
[2034.50 --> 2037.50]  I would argue Mongo is fast enough.
[2037.50 --> 2038.50]  I mean, Cassandra is good to be on that.
[2038.50 --> 2040.50]  You don't have a concurrency story.
[2040.50 --> 2044.50]  What if a thousand users hit you at the same time, you're dead in the morning.
[2044.50 --> 2045.50]  They're just caching.
[2045.50 --> 2046.50]  They're written in C.
[2046.50 --> 2048.50]  I mean, that's a good, right?
[2048.50 --> 2049.50]  Aren't they fast enough?
[2049.50 --> 2051.50]  It doesn't scale concurrently.
[2051.50 --> 2056.50]  So how easy is it to also quickly hook up a CDN to your store?
[2056.50 --> 2061.50]  Okay, just with one flip of the bit suddenly have, you know, caching all over the world and things will be very well.
[2061.50 --> 2062.50]  Not open source.
[2062.50 --> 2063.50]  So, what is it?
[2063.50 --> 2069.50]  SV doing this with a whole number of 25,000 transactions per second?
[2069.50 --> 2070.50]  Stop it!
[2070.50 --> 2071.50]  We got your points!
[2071.50 --> 2072.50]  Come on!
[2072.50 --> 2076.50]  So, Cassandra can do 25,000 requests per second per node.
[2076.50 --> 2077.50]  That's great.
[2077.50 --> 2079.50]  What is your job, brother?
[2079.50 --> 2081.50]  Do we have more audience questions before that?
[2081.50 --> 2082.50]  All right.
[2082.50 --> 2083.50]  Talk about transactions.
[2083.50 --> 2084.50]  When?
[2084.50 --> 2086.50]  Do you need transactions?
[2086.50 --> 2090.50]  Banks have relational data because they have transactions.
[2090.50 --> 2094.50]  Banks have entities that need transactions that will always be relational databases.
[2094.50 --> 2095.50]  Can I hear you?
[2095.50 --> 2096.50]  Yeah, I'll repeat the question.
[2096.50 --> 2097.50]  He's asking about transactions.
[2097.50 --> 2099.50]  Do people need transactions?
[2099.50 --> 2100.50]  Raise your hands.
[2100.50 --> 2103.50]  Okay, so that's your answer.
[2104.50 --> 2105.50]  Wait, wait.
[2105.50 --> 2108.50]  First of all, transactions have nothing to do with relational databases.
[2108.50 --> 2113.50]  The fact that they were offered by the same particular tool, that's a different thing.
[2113.50 --> 2119.50]  Transactions is just that you get a number of guarantees, asset guarantees about the update of your data.
[2119.50 --> 2120.50]  That's all.
[2120.50 --> 2122.50]  Now, I have nothing to do with relational databases.
[2122.50 --> 2124.50]  Also, NoSQL is about using the right tool for the job.
[2124.50 --> 2125.50]  Yeah.
[2125.50 --> 2126.50]  Exactly.
[2126.50 --> 2129.50]  So, there are engines for building transactions.
[2129.50 --> 2130.50]  Zookeeper is one of them.
[2130.50 --> 2131.50]  It's open source as well.
[2131.50 --> 2132.50]  That's how you should do your transactions.
[2132.50 --> 2134.50]  And that's how a lot of people do.
[2134.50 --> 2138.50]  So, let's talk a little bit about ecosystems.
[2138.50 --> 2141.50]  Cassandra, I mean I'm going to name drop.
[2141.50 --> 2142.50]  Cassandra has a few good installs.
[2142.50 --> 2143.50]  Cloudkick.
[2143.50 --> 2144.50]  Twitter.
[2144.50 --> 2145.50]  Cloudkick.
[2145.50 --> 2149.50]  Alphabetically, Cloudkick is at the top.
[2149.50 --> 2152.50]  But yes, also Twitter, Facebook.
[2152.50 --> 2153.50]  What do you guys got?
[2153.50 --> 2154.50]  I got the BBC.
[2154.50 --> 2155.50]  I got Canonical.
[2155.50 --> 2161.50]  It's not as big as you can get, but we probably have a few more installs than you guys have.
[2161.50 --> 2162.50]  It's been awesome since I've been out to the list.
[2162.50 --> 2163.50]  And the discuss is out there.
[2163.50 --> 2164.50]  SourceForge.
[2164.50 --> 2165.50]  Move to MongoDB.
[2165.50 --> 2172.50]  Of course, tail.thechangelog.com is how you keep up with open source software.
[2172.50 --> 2175.50]  I almost lost for a while.
[2175.50 --> 2181.50]  Someone tweeted a remark saying that when I see Stan, I tell you to go to the bar.
[2181.50 --> 2182.50]  That was a joke.
[2182.50 --> 2189.50]  Before someone thinks that that is an official company statement.
[2189.50 --> 2194.50]  I think just with any other database or whatever, you know, you protect yourself at multiple different levels.
[2194.50 --> 2195.50]  You use caching.
[2195.50 --> 2197.50]  You be intelligent about where you store your data.
[2197.50 --> 2203.50]  You know, S.V. also gives you multiple zones and availability zones where you can actually store your data.
[2203.50 --> 2209.50]  There's many techniques that you can use to protect yourself from these kind of failures.
[2209.50 --> 2216.50]  Just that's the, that's the real answer to giving the hotel a little funnier.
[2216.50 --> 2221.50]  So how about wide area replication?
[2221.50 --> 2224.50]  I mean, people are geographically distributed.
[2224.50 --> 2227.50]  Cassandra supports wide area replication.
[2227.50 --> 2229.50]  It's kind of native.
[2229.50 --> 2231.50]  How do people accomplish that with your stores?
[2231.50 --> 2232.50]  Or do they fall down?
[2232.50 --> 2238.50]  CoachDB has master master or multi-master replication building, which has been built for geographic
[2238.50 --> 2239.50]  distribution in mind.
[2239.50 --> 2241.50]  So we just have to ask.
[2241.50 --> 2245.50]  I believe currently Mongo is master-slave, but I believe master-master is coming.
[2245.50 --> 2248.50]  Yeah, but it never works with your data model.
[2248.50 --> 2255.50]  Multiple regions where each of the regions is guaranteed to store the data independently.
[2255.50 --> 2257.50]  Store your data in the EU.
[2257.50 --> 2259.50]  It's guaranteed to only stay in the EU.
[2259.50 --> 2264.50]  Not only, not even metadata about the data will ever leave the EU.
[2264.50 --> 2268.50]  So you get, you get geographical replication for free.
[2268.50 --> 2273.50]  New East Coast goes, disappears off the earth, which actually appears to be happening at the
[2273.50 --> 2274.50]  moment.
[2274.50 --> 2278.50]  You know, you'll still have the other sides and you still have Asia and things like that as
[2278.50 --> 2279.50]  well.
[2279.50 --> 2281.50]  So a big table recently had an outage.
[2281.50 --> 2282.50]  I guess it was App Engine.
[2282.50 --> 2286.50]  And I love Google because they're very, very open about what went down.
[2286.50 --> 2287.50]  Amazon is too.
[2287.50 --> 2292.50]  But, so what went down was that their master and slave replication basically got out of
[2292.50 --> 2293.50]  sync between data centers.
[2293.50 --> 2298.50]  So I don't know if, I don't know how I, how I feel about master-slave replication.
[2298.50 --> 2300.50]  Can we, can we break that?
[2300.50 --> 2301.50]  Is Mongo planning to break that?
[2301.50 --> 2302.50]  Good question.
[2302.50 --> 2303.50]  Good question.
[2303.50 --> 2306.50]  Good, good, good question.
[2306.50 --> 2308.50]  Yeah, you can break it.
[2308.50 --> 2310.50]  It's not that hard to break it.
[2310.50 --> 2312.50]  But, I mean there's advantages on all sides.
[2312.50 --> 2317.50]  You know, as always the cap theorem is not that it forces us to use a particular consistency
[2317.50 --> 2318.50]  model.
[2318.50 --> 2319.50]  You get to make the trade-offs.
[2319.50 --> 2323.50]  I think, you know, Cassandra as well as Dynamo before that, one of the exercises in Dynamo
[2323.50 --> 2328.50]  was really to make sure that we were given the hands of the developers the choice to go
[2328.50 --> 2329.50]  forward.
[2329.50 --> 2334.50]  Do you want to be really highly available or are you willing to sacrifice some of your
[2334.50 --> 2335.50]  consistency model there?
[2335.50 --> 2338.50]  And there's no switch you can use there.
[2338.50 --> 2344.50]  Plus, I think, actually, but the biggest innovation in all of this was something called
[2344.50 --> 2345.50]  sloppy quorum.
[2345.50 --> 2348.50]  The fact that you could take writes even if your quorum is down.
[2348.50 --> 2351.50]  And you could always, always write through the system.
[2351.50 --> 2354.50]  Here, if a customer wants to put something in his shopping cart, they're going to tell him,
[2354.50 --> 2357.50]  no, the storage system failed, timed out.
[2357.50 --> 2360.50]  No, it just always works.
[2360.50 --> 2362.50]  And I don't actually have a response to that.
[2362.50 --> 2363.50]  I guess that's possible in CouchDB.
[2363.50 --> 2364.50]  Yeah.
[2364.50 --> 2369.50]  But only because no node actually knows whether it's responsible for something.
[2369.50 --> 2371.50]  But I think we had a question.
[2371.50 --> 2375.50]  I think the one question you really need to answer with NoSQL is why do I want to do this
[2375.50 --> 2378.50]  instead of just staying with MySQL and buying a bigger machine?
[2378.50 --> 2385.50]  I can buy a 10 terabytes RAM, 504 machine that will run MySQL or Oracle or whatever just fine.
[2385.50 --> 2388.50]  Why do I want to know SQL?
[2388.50 --> 2390.50]  So the question was why not just scale up?
[2390.50 --> 2391.50]  Why scale out?
[2391.50 --> 2395.50]  I would say that the question, the answer when it comes to Oracle is price.
[2395.50 --> 2396.50]  That's very, very clear.
[2396.50 --> 2398.50]  We're all open source.
[2398.50 --> 2402.50]  And when it comes to MySQL, eventually that machine goes down.
[2402.50 --> 2410.50]  And you have some sloppy situation where you have to either use patches to MySQL to not lose your data or you have to implement something else.
[2410.50 --> 2413.50]  You have your ops team implement DRVD or something.
[2413.50 --> 2416.50]  Now, let's back to the big data versus the schemeless questions.
[2416.50 --> 2423.50]  And I think if you're comparing something like Mongo to MySQL, I think it's a more fair comparison because it's a...
[2423.50 --> 2424.50]  Back a little bit.
[2424.50 --> 2425.50]  You mentioned highly available.
[2425.50 --> 2427.50]  I would mention highly productive, right?
[2427.50 --> 2434.50]  So a lot of applications now, let's face it, a lot of the data that you use, you're not creating in-house.
[2434.50 --> 2436.50]  You're consuming APIs from other places.
[2436.50 --> 2438.50]  A lot of that is coming from JSONs.
[2438.50 --> 2441.50]  It's coming from other hashes that are up in the sky, right?
[2441.50 --> 2445.50]  Using something like MySQL, then you have to model that schema and stash those.
[2445.50 --> 2448.50]  Using a NoSQL store, you can just stash the hash.
[2448.50 --> 2459.50]  So in answer to that question, when I see somebody writing a Ruby app or a Java app or anything with a middle-tier application layer,
[2459.50 --> 2462.50]  I look at that as a huge waste of time.
[2462.50 --> 2465.50]  With couch apps, it's just the browser and the couch DB, right?
[2465.50 --> 2470.50]  You got a jQuery guy and you got somebody who knows how to keep the server from dying.
[2470.50 --> 2471.50]  That's all it takes.
[2471.50 --> 2473.50]  And, you know, Werner's on that same case.
[2473.50 --> 2474.50]  He's got HTTP.
[2474.50 --> 2475.50]  I agree with that.
[2475.50 --> 2480.50]  What does having an HTTP-based database mean that you don't need all that crap in the middle?
[2480.50 --> 2484.50]  Well, I was actually arguing that you have to have a range of things to be able to pick from.
[2484.50 --> 2486.50]  And one of them is an HTTP accessible.
[2486.50 --> 2490.50]  But coming back to your question, actually, I think there's a number of use cases,
[2490.50 --> 2497.50]  and especially where it goes about existing software where you still may want to run your relational database.
[2497.50 --> 2503.50]  When we built the first services at Amazon Storage Services, we did not offer a relational storage service.
[2503.50 --> 2509.50]  Why not? Because you thought that, you know, that would send the wrong signal because you really want to build scalable apps.
[2509.50 --> 2510.50]  You don't do that.
[2510.50 --> 2512.50]  However, there's a ton of applications.
[2512.50 --> 2518.50]  If you use Ruby and you use Active Records, you know, or any standard ORM kind of tool, you know,
[2518.50 --> 2520.50]  they all want to talk to MySQL.
[2520.50 --> 2525.50]  And so here you have a whole range of developers that just want to focus on writing Ruby.
[2525.50 --> 2529.50]  They don't want to run databases or whatever, and they don't care about what the backend is.
[2529.50 --> 2532.50]  And that's your argument about very small databases, very small datasets.
[2532.50 --> 2533.50]  They don't care.
[2533.50 --> 2538.50]  As soon as you have to scale, as soon as reliability becomes an issue, all of these kind of things,
[2538.50 --> 2544.50]  then it turns out that relational databases have their limitations at points that, you know, will hurt you.
[2544.50 --> 2547.50]  You bring up an excellent point about Active Record.
[2547.50 --> 2548.50]  I don't want to bitch about it.
[2548.50 --> 2550.50]  It's really, really cool for what it does.
[2550.50 --> 2552.50]  But it is a thing of simplicity.
[2552.50 --> 2554.50]  CouchDB is built with simplicity in mind.
[2554.50 --> 2559.50]  And the thing that we have in the store here is that Active Record the last time I looked
[2559.50 --> 2561.50]  had around 25,000 lines of Ruby code.
[2561.50 --> 2565.50]  And I know this is apples and whatever bungalows in comparison.
[2565.50 --> 2567.50]  CouchDB comes at around 15,000 lines of code.
[2567.50 --> 2573.50]  So our entire database is smaller than the wrapper you're using to solve your programming issues.
[2573.50 --> 2577.50]  So we compress the stack by using pure CouchApps without ORMs,
[2577.50 --> 2581.50]  without all the middleware crap that you could, like, find bugs in that takes a long time to use.
[2581.50 --> 2586.50]  Like, it's just boring and slow and, I don't know, it just, it plain sucks.
[2586.50 --> 2587.50]  I'm sorry.
[2587.50 --> 2592.50]  You know, I welcome this renaissance we've got for JavaScript and all these new NoSQL databases
[2592.50 --> 2594.50]  that are embracing this language of the past.
[2594.50 --> 2599.50]  But the problem of Couch is the fact that you have to do everything in JavaScript.
[2599.50 --> 2602.50]  Talk to Apple, Google, Mozilla about the language of the past.
[2602.50 --> 2603.50]  I'm a JavaScript fanboy.
[2603.50 --> 2604.50]  You listen to the changelog.
[2604.50 --> 2606.50]  We mention Node.js on every episode.
[2606.50 --> 2612.50]  But the problem with Couch is you have to drop down to MapReduce and JavaScript to do anything.
[2612.50 --> 2615.50]  Anything of consequence, you have to drop down to JavaScript.
[2615.50 --> 2617.50]  And, you know, I'm familiar with JavaScript.
[2617.50 --> 2618.50]  I love JavaScript.
[2618.50 --> 2622.50]  But I know a lot of the folks that I work with feel like you have to have hazmat gloves to touch JavaScript.
[2622.50 --> 2623.50]  Yeah, that's cool.
[2623.50 --> 2625.50]  But they're like the CS majors of everybody.
[2625.50 --> 2629.50]  People who tinkle with the web designers who just started to use jQuery, they're comfortable with that.
[2629.50 --> 2630.50]  They can use Couch.
[2630.50 --> 2632.50]  You're going to get a web designer and a Couch database?
[2632.50 --> 2633.50]  Yes.
[2633.50 --> 2634.50]  Oh, okay.
[2634.50 --> 2635.50]  Just like at a C.
[2635.50 --> 2636.50]  I have a lot of them.
[2636.50 --> 2637.50]  And his name is Bob.
[2637.50 --> 2640.50]  But, so guys, we have to start wrapping up.
[2640.50 --> 2641.50]  Is it a quick one?
[2641.50 --> 2643.50]  Yeah, it's about data modeling.
[2643.50 --> 2647.50]  A lot of people who review relational databases always think about their data models.
[2647.50 --> 2653.50]  I just have the impression when you talk about these NoSQL databases that you just set data modeling at the site and you don't think about how you model it.
[2653.50 --> 2658.50]  So, the question was about data models and there are names for what we do.
[2658.50 --> 2661.50]  In a relational database, you typically want to normalize.
[2661.50 --> 2664.50]  And in a non-relational database, you want to denormalize.
[2664.50 --> 2665.50]  And it's really just that simple.
[2665.50 --> 2668.50]  So, you duplicate, but that's fine, is what we say.
[2668.50 --> 2676.50]  So, in closing statements, let's just talk about what you would use if you couldn't use your own product.
[2676.50 --> 2684.50]  So, you would implement some, you're implementing something, it's going to be a perfect fit for CouchDB, but your manager says, no, you can't use CouchDB.
[2684.50 --> 2686.50]  So, what's your next choice?
[2687.50 --> 2692.50]  I think I'd probably use Preservere, which is actually written in JavaScript.
[2692.50 --> 2694.50]  So, there you go.
[2694.50 --> 2695.50]  Cool.
[2695.50 --> 2701.50]  So, because it's written in JavaScript and all the other languages are boring.
[2701.50 --> 2704.50]  But does it scale?
[2704.50 --> 2712.50]  So, if I couldn't use Cassandra, I'd have to say, React's really interesting, but the kind of closed source project they have going on.
[2712.50 --> 2716.50]  And Voldemort's interesting too, but they don't have ordered keys.
[2716.50 --> 2718.50]  And I love ordered keys.
[2718.50 --> 2720.50]  But, yeah.
[2720.50 --> 2721.50]  So, maybe React.
[2721.50 --> 2722.50]  Maybe Couch.
[2722.50 --> 2723.50]  Woo!
[2723.50 --> 2730.50]  I couldn't use Mongo, perhaps Couch, but it depends on the scenario, we need to do dynamic queries or something like that.
[2730.50 --> 2733.50]  That was just a pain point for a lot of several apps that we went through.
[2733.50 --> 2740.50]  I would like to probably check out Redis or some of the other systems that probably should have been up here.
[2740.50 --> 2744.50]  And let me just say that I hope I didn't deter anybody from using MongoDB.
[2744.50 --> 2745.50]  I'm just a fanboy.
[2745.50 --> 2749.50]  Like I said, I wish somebody from TenGen could have been here to adequately represent the database.
[2749.50 --> 2751.50]  It's a cool database.
[2751.50 --> 2758.50]  Actually, I think the one database that was left out, which I think is very different from these ones, is Neo4j.
[2758.50 --> 2770.50]  I think that if you look at databases that build things for a very specific domain, where you have graphs, where actually all your data is structured as graphs.
[2770.50 --> 2775.50]  Take any social network or anything with multiple relationships and multiple connections.
[2775.50 --> 2779.50]  Neo4j is absolutely rocks in that sense.
[2779.50 --> 2784.50]  I don't think they deserve, partitioning that is a pretty hard thing to do.
[2784.50 --> 2785.50]  Exactly, yeah.
[2785.50 --> 2787.50]  Partitioning a graph, it's a computer science problem, but it's not true.
[2787.50 --> 2788.50]  Sure.
[2788.50 --> 2790.50]  No, no, so hey, why don't we build one?
[2790.50 --> 2791.50]  Yeah.
[2791.50 --> 2792.50]  Exactly.
[2792.50 --> 2793.50]  So if I can't use...
[2794.50 --> 2796.50]  I don't know, I'll go to a bar for a few hours.
[2796.50 --> 2799.50]  I'll come back and then people will say I can use S.Vegan.
[2799.50 --> 2801.50]  Alright, so we're cooling down.
[2801.50 --> 2802.50]  Any other questions, guys?
[2804.50 --> 2808.50]  If not guys, let's all say thank you, the non-relational database snack bag!
[2809.50 --> 2816.50]  Thank you for listening to this edition of The Changelog.
[2816.50 --> 2825.50]  Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[2826.50 --> 2834.50]  Also be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Changelog.
[2834.50 --> 2835.50]  The Changelog.
[2835.50 --> 2836.50]  The Changelog.
[2836.50 --> 2847.50]  Safe in your arms as the dark passion shown was mine alone.
[2847.50 --> 2857.50]  Open, open, open, for us to try.
[2857.50 --> 2864.50]  Bring it back, bring it back to our ground.
[2864.50 --> 2871.50]  Open, open, for us to try.
[2871.50 --> 2872.50]  Bring it back to our ground.
[2872.50 --> 2902.48]  Thank you.
