[0.00 → 17.90] Welcome to the Changelog episode 0.5.1.
[18.04 → 18.98] I'm Adam Stachowiak.
[19.32 → 20.12] And I'm Wynne Edwin.
[20.30 → 21.32] This is the Changelog.
[21.36 → 23.40] We cover what's fresh and new in the world of open source.
[23.80 → 26.72] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.80 → 27.82] We're also up on GitHub.
[27.82 → 33.50] Head to GitHub.com. You'll find some training repos, some feature repos from the blog, as well as our audio podcast.
[33.82 → 37.58] And if you're on Twitter, follow Changelog Show, Changelog Jobs, and me, Adam Stack.
[38.10 → 40.56] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.10 → 45.14] This episode is sponsored by GitHub Jobs. Head to the changelog.com slash jobs to get started.
[45.38 → 51.32] If you'd like us to feature your job on this show, select advertise on the Changelog when you post your job, and we'll take care of the rest.
[51.32 → 61.82] Just like FedEx looking for a senior technical analyst, Boss Edition must be skilled in web logic, Unix, Linux, Java, J2E, the whole Java stack.
[62.40 → 66.58] If you're interested, apply it at LG.Gd slash 9a.
[66.58 → 71.66] And Java's not the only game in town for FedEx. They're also looking for a senior-level PHP dev.
[72.14 → 77.62] Got strong PHP skills, SQL query skills against Unix and Linux environments.
[78.00 → 81.52] Java, SQL to Oracle databases are also pluses for this position.
[82.10 → 86.94] You'll also be located in Clear vale, Tennessee. Relocation assistance is available, and it is full-time.
[87.04 → 88.96] Check out LG.Gd slash 9b.
[88.96 → 94.96] White Glove House call Health is a four-year-old startup that's revolutionizing healthcare as we know it.
[95.16 → 100.14] If you sling Rails or even iOS, they're looking for a developer with at least two years of Ruby
[100.14 → 104.02] and four years of practical general software development experience.
[104.70 → 106.14] Full-time in Austin, Texas.
[106.56 → 111.48] If you're interested, apply at LG.Gd slash 9c.
[111.92 → 113.04] Fun episode this week.
[113.22 → 117.52] We talked to Elliot Horowitz over at Tinged, the company behind MongoDB.
[117.52 → 122.04] Steve and I had fun talking about our favourite NoSQL store.
[122.64 → 125.18] So I hear the listeners can't tell the difference between Steve and Kenneth.
[125.58 → 126.12] Did you hear that?
[126.58 → 128.54] Yeah, people get them mixed up all the time.
[128.90 → 130.02] On this fake radio show.
[130.40 → 131.68] On this fake radio show.
[131.84 → 134.34] This is like the cable access of the internet, you know?
[134.60 → 138.12] It reminds me of, oh, come on, what is it?
[139.26 → 139.80] Wayne's World?
[139.90 → 140.24] Yeah!
[141.02 → 142.06] You knew where I was going.
[142.62 → 143.06] Party on.
[143.36 → 144.00] Party on, Wayne.
[145.12 → 147.04] Speaking of party on, we'll be at South by Southwest.
[147.04 → 148.36] West, this week, at least I will.
[148.66 → 153.06] You are still up in the air on that, but at least look for me.
[153.56 → 155.28] I'm hanging back in Houston this time.
[155.68 → 156.00] Are you?
[156.32 → 156.72] Yeah.
[157.36 → 160.32] Well, Penguin will be solo handing out changelog stickers.
[160.64 → 165.70] So if you see me in the concourse, holler out, and you can get a changelog sticker for your laptop.
[166.28 → 169.38] And we're also getting some tea, so please stay tuned to that.
[169.38 → 173.28] If you see us at one of the conferences, ask us for them because we'll have them soon.
[173.96 → 180.20] And if you're out there, and would like to sponsor these changelog t-shirts, we are now soliciting sponsors for these changelog t-shirts.
[180.74 → 181.28] I love it.
[182.10 → 184.18] You don't get your name on it, but you get to help pay it for them.
[184.48 → 185.16] There you go.
[185.86 → 186.74] Kenneth will be at Pylon.
[187.40 → 188.96] Steve will be at Comecon.
[189.06 → 195.54] And we'll both be doing a special live episode at Red Dirt Rubicon, Oklahoma City, April 21st and 22nd.
[195.54 → 196.24] Looking forward to that.
[196.56 → 197.58] Absolutely looking forward to that.
[197.68 → 199.06] Love that conference, too.
[199.10 → 200.92] They're doing a lot of great stuff, so hope to see you there.
[201.40 → 202.36] Should be a fun time.
[202.36 → 202.40] All right.
[202.80 → 204.52] So, great episode this week.
[204.60 → 209.56] We even get a take of web scale from Elliot.
[210.04 → 210.76] Very cool.
[211.10 → 211.98] Sounds like a fun episode.
[212.06 → 212.66] You want to get to it?
[212.90 → 213.48] Let's do it.
[222.38 → 227.92] We're chatting today with Elliot Horowitz, founder over at Engen, the company behind MongoDB.
[227.92 → 232.66] So, Elliot, why don't you introduce yourself and a little bit about your day-to-day role over at Congo.
[233.14 → 233.48] Hi.
[233.58 → 233.86] Thanks.
[233.98 → 234.92] I'm Elliot Horowitz.
[235.04 → 237.42] I'm the CTO and co-founder of Engen.
[237.94 → 241.96] So, I've been working on MongoDB for about three and a half years now.
[243.30 → 256.48] Day-to-day, I write a lot of code for Congo, work with a lot of clients, and do a lot of roadmap development and other sorts of things with the community.
[256.48 → 261.02] So, as one of the project founders, why don't you give a little backstory about how MongoDB came about?
[261.98 → 271.52] MongoDB really came out from my and Dwight Harriman's frustration working with databases in sort of the previous decade before we started MongoDB.
[271.52 → 285.28] You know, I think he and I once counted, and in a decade before we started working on this, between the two of us, we wrote a dozen different data storage pieces for systems.
[285.28 → 297.36] So, you know, things varying from simple, you know, things for storing massive numbers of images to distributed, you know, key value store-like things.
[297.86 → 300.94] They're all very niche.
[301.08 → 305.64] They all have sort of very specific purposes in mind, and we're not general in any way.
[305.64 → 316.78] And I think in every single case, we had tried some off-the-shelf solution first, whether it was a relational database or some other key value store-type system.
[317.56 → 320.10] And in all cases, they fell down for some reason.
[321.30 → 329.72] And so, basically, what we said is, you know, there's probably a way we can generalize this and actually create a database that we would want to use and that we think we could use for most of our problems,
[329.72 → 332.72] rather than having to reinvent the wheel every time.
[333.80 → 337.38] And so that's really where the motivation for MongoDB came out.
[337.86 → 342.38] And then the design mostly came out from things that, you know, what would we want to use?
[342.38 → 347.78] You know if we were going to, you know, when we were starting our next project, what was the ideal database we'd want to use?
[348.78 → 353.20] Neither of us were, you know, particularly looking to build a database.
[353.42 → 358.94] It was more about, you know, we wanted to build something that we would want to use from our experience.
[359.72 → 362.34] Talk a little bit about those problems you're trying to solve.
[362.46 → 365.02] Were they performance-related or just design-related?
[365.48 → 369.90] So it was a little bit of, you know, both from a design perspective, a scale problem.
[370.64 → 374.94] You know, in some cases, it was storing billions of images.
[375.84 → 379.34] So, you know, for storing billions of images, you know, relational databases aren't perfect at that.
[379.70 → 380.66] You could use file systems.
[380.78 → 382.18] You could use distributed file systems.
[382.46 → 386.76] But they all have some problem that we found.
[386.76 → 391.10] And so, you know, in our case, we were trying to store billions and billions of very small images.
[391.88 → 394.14] And all the solutions we tried didn't work very well.
[394.60 → 403.78] In other cases, we were sort of jury-rigging massive amounts of complexity on top of key value stores in order to do document-like retrieval.
[404.40 → 404.52] Right?
[404.52 → 410.86] So if you have, like, sort of richer data types, right, there are sorts of known ways to solve this with relational databases.
[411.34 → 413.30] But it ends up being a very complicated problem.
[413.64 → 416.34] Or you end up storing a big blob in a relational database.
[416.46 → 417.60] But then it's hard to index on it.
[417.62 → 418.60] It's hard to query on it.
[419.18 → 428.36] And so we had sort of built a bunch of various, you know, basically hacks around both relational databases and key value stores to sort of make this work for us.
[428.36 → 432.30] But in the end, you know, neither was very general.
[433.08 → 434.02] You know, they were all hacks.
[434.18 → 436.56] So we never, you know, they were never full-fledged databases.
[437.10 → 439.70] And so they always ended up causing some pain here or there.
[440.16 → 442.22] And really, we never wanted to write them in the first place.
[442.28 → 443.86] We really just wanted to work on our application.
[444.38 → 448.34] But we couldn't because of, you know, database limitations.
[448.86 → 455.58] It seems like one of the cries that sort of come out of the whole NoSQL thing is that, you know, different data stores for different usages.
[455.58 → 459.98] So, you know, Congo is really flexible and does have a lot of usages.
[460.14 → 463.82] But it seems like, do you, I guess, you're saying you disagree with that to a certain degree?
[464.04 → 474.28] Or is it just that most of your data should be able to be stored in one database with, you know, side applications as opposed to having, like, a more complicated setup, I guess?
[474.44 → 479.04] So I think there are definitely a few general types of databases that will make sense long term.
[479.48 → 479.76] Right?
[479.80 → 482.34] There are definitely places where relational databases make sense.
[482.44 → 484.58] There are definitely places where document databases make sense.
[484.58 → 493.52] I think that the world has gone very far on the one size doesn't fit all and, you know, running lots of different kinds of data stores.
[493.90 → 500.12] And I think that's really a reaction to limitations with, you know, the current technology.
[500.74 → 500.84] Right?
[500.84 → 506.06] I don't think it's necessarily the right approach to have six different storage engines running inside an application.
[506.06 → 513.64] I think it's that there is no one storage engine that can solve, you know, one or two that can solve all of your problems.
[514.44 → 522.36] And so, you know, what people started doing, you know, completely, you know, reasonable people and rational people said, okay, I'm going to use this.
[522.36 → 524.72] I can't find a database that solves all my problems.
[524.72 → 531.12] But if I pick and choose different storage engines and different databases, then I could actually get my work done.
[531.12 → 541.22] And I think that's more of a reaction to the current state of technology than the correct long term way about thinking storage.
[542.18 → 550.56] I think that there is definitely a, you know, an ability to create a database that solves the majority of problems.
[550.56 → 557.20] So, like, the pendulum swings one way, and then it swings back the other way, and now we're kind of finding a happy middle place, I guess.
[558.06 → 558.40] Right.
[558.46 → 560.78] I mean, I think that's sort of the goal.
[561.00 → 562.02] I don't think we're there today.
[562.36 → 567.26] But I think the goal is definitely to find the place where most of your data lives in one storage engine.
[567.36 → 573.28] And maybe you use a few very niche products or certain areas, you know, maybe for data warehousing.
[573.28 → 580.58] You know, a data warehouse storage system versus an online storage system may look very different.
[581.50 → 590.16] But I don't think that it's, you know, I don't think it's a matter of having eight different storage engines.
[590.26 → 593.66] I think it may be having, you know, one, two, or maybe three in some cases.
[594.38 → 596.32] The NoSQL field is getting kind of crowded.
[596.32 → 605.48] Any of those that were out there when you started down this path that you looked at and just felt that wasn't a good fit for what you wanted to do?
[608.06 → 615.66] So, if you look at NoSQL as a whole, right, see, there are really a few different types of general databases.
[616.08 → 617.68] So, you've got, you know, key value stores.
[617.90 → 618.96] You've got graph databases.
[620.22 → 621.70] And you've got document databases.
[624.06 → 625.54] And they're all very different.
[625.54 → 632.24] And so, I think that, you know, I think fundamentally what we want to do is it doesn't fit well into the mould of a key value store.
[633.00 → 637.28] You know, I think key value stores are very good in some cases.
[637.46 → 642.04] They're very, you know, there are a lot of good things about key value stores, but it's not a general database.
[643.46 → 649.04] Graph databases, again, there are certain areas where they work exceptionally well, probably better than anything else.
[649.36 → 652.80] But, again, it's not a general, you know, it's not a general solution.
[652.80 → 667.78] I think document databases definitely are the sort of the solution for most sort of at least in terms of the web infrastructure and online systems is generally the right approach to most problems.
[667.78 → 673.58] So, with all these different choices, one of the problems is sort of like developer education.
[673.98 → 680.24] So, how do you manage to explain to developers how the differences of all these different databases?
[680.48 → 689.62] I mean, I definitely saw a number of blog posts about Congo where people had simply set it up wrong or had incorrect expectations about the way things worked.
[689.62 → 693.00] And, you know, it didn't work out for them, but that's not really a fault of Congo.
[693.16 → 695.14] It's more that they didn't read the docs.
[696.04 → 696.40] Right.
[696.58 → 698.90] I mean, so, you know, this is a constant battle for us.
[699.02 → 704.98] And, you know, I think it's just a matter of, you know, making the documentation as good as possible and making sure that, you know, we talk to lots of people.
[705.10 → 709.64] We're doing conferences around the world, you know, basically just where we go.
[709.72 → 715.94] And we just sort of talk about Congo and what are good use cases for it, how it works, what are the design philosophies behind it,
[715.94 → 718.10] such that when you're using it, you can use it more effectively.
[718.10 → 721.12] And it's a constant, you know, it's a constant battle.
[721.74 → 726.96] I think it's, you know, Congo is in some ways very close to relational databases.
[727.12 → 728.20] A lot of things feel familiar.
[729.18 → 734.78] But a lot of things, you know, once you sort of dive deeper than the very basic level, things change dramatically.
[735.80 → 740.62] And both change in how you have to use it and the expectations you have to get from it.
[741.08 → 743.62] And so there's a big gap there.
[744.04 → 746.14] And that's what's going to take time to close.
[746.14 → 755.42] And also, the other thing to remember about Congo is because we are looking at a, you know, we're trying to build sort of a general database and not, you know, a niche product,
[756.78 → 759.94] Congo is definitely a very large scope project.
[760.36 → 762.32] And we've been working on it for over three years now.
[762.32 → 767.82] And our list of sort of, you know, core features is still not complete.
[768.78 → 778.66] You know, you know, our roadmap for the next 18 months has tons of features on it that we think are, you know, just sort of not like advanced features or not like nice to haves,
[778.74 → 781.50] but are just basically core features you need for a database like this.
[781.50 → 785.80] And so, you know, in our minds, MongoDB is definitely not done.
[787.24 → 790.68] I mean, that's definitely something, you know, an expectation we have to manage.
[791.20 → 797.58] That it's just like, yeah, MongoDB is great for lots of cases today, but in no way is it, you know, complete in our minds at this point.
[798.46 → 801.82] Well, it's been over a year since we last covered Congo on the changelog.
[801.88 → 804.00] We were big fans then, still big fans now.
[804.00 → 808.48] So we're looking down the barrel at 1.8, the upcoming release.
[808.60 → 810.64] What's new in 1.8 for MongoDB devs?
[811.24 → 815.78] So MongoDB 1.8 has a bunch of new stuff in it.
[816.36 → 825.38] The biggest, sort of the most notable feature for sure is single server durability or journaling.
[826.76 → 830.88] And so this has definitely been one of the concerns people have had with Congo previously,
[830.88 → 836.76] where, you know, previous to 1.8, no single instance of Congo was durable.
[837.08 → 839.90] So if you wanted to make, you know, guarantee the integrity of your data,
[840.30 → 843.66] the correct way to do it was making sure you had, you know, multiple servers of the data
[843.66 → 848.30] and using replica sets to make sure you had multiple copies so that any hardware failure
[848.30 → 852.18] or even a data centre failure would not cause data loss.
[853.12 → 858.50] When we originally designed MongoDB, we really had more enterprise in mind,
[858.96 → 860.04] more large-scale deployments,
[860.04 → 864.08] and so we hadn't focused too much on sort of the very small instances
[864.08 → 866.30] or just someone who wants to run a two- or three-node instance.
[867.50 → 871.94] And so on of the big problems people have had, both in the small scale and in the large scale,
[872.56 → 874.44] was the lack of journaling.
[874.58 → 879.08] So 1.8 has journaling, which means that on a single server, you know,
[879.26 → 882.26] if you lose, you know, on a hardware failure, on power failure,
[882.84 → 884.96] your database will not end up in a corrupt state.
[885.40 → 887.36] You will have a consistent database.
[887.36 → 889.24] So that alone is good.
[889.32 → 893.70] It also means that even if you have multiple data centres,
[893.74 → 894.90] it means that you can recover faster.
[895.50 → 897.72] So even for the enterprises, it's still really nice because, you know,
[897.76 → 899.74] recovery time is faster in the event of a failure.
[900.10 → 902.18] So there are a lot of good things about journaling.
[902.78 → 905.46] So journaling is definitely the biggest feature in 1.8.
[905.46 → 911.20] And then for the very small deployments, it's a game changer because a lot of people, you know,
[911.24 → 914.10] if they wanted to run a single instance on a single server,
[914.86 → 919.20] Congo really wasn't a good fit for them because there was no way to guarantee data integrity.
[920.74 → 922.14] So that's definitely the biggest issue.
[922.30 → 923.62] That's definitely the biggest feature with 1.8.
[923.62 → 929.60] I think that's one of the reasons I love Congo so much is it's so approachable for new developers.
[929.78 → 933.40] I mean, it's really – it maps very closely to relational databases.
[933.60 → 934.64] It's easy to get your head around.
[934.86 → 938.92] But at the higher end, what are some of the larger installations you've seen in Congo?
[939.96 → 942.26] So there are a number of large ones.
[942.38 → 947.14] You know, some of the large ones of note are, you know, places like Shutter fly and Foursquare.
[947.14 → 954.06] You know, both of them are storing, you know, very large datasets with lots of throughput.
[954.68 → 960.16] You know, Craigslist is loading up a fairly monstrous dataset into Congo as we speak.
[960.72 → 962.72] So there's some pretty large-scale deployments out there.
[963.40 → 964.98] And the enterprise is really like Congo.
[965.22 → 970.58] You know, so for the single developer, one of the main reasons to use Congo is the data model
[970.58 → 976.26] and how easily it is to code with it and how agile it is in terms of being able to add fields
[976.26 → 978.52] or adapt your schema as your application changes.
[979.14 → 980.96] At the enterprise, it's actually two things.
[981.04 → 982.42] One is the agility, right?
[982.42 → 987.74] We talked to one customer who switched to Congo simply because they were 18 months behind in their product roadmap
[987.74 → 991.26] because working with Oracle is becoming such a bottleneck.
[991.66 → 996.50] You know, having to change schemas and work within the limitations there
[996.50 → 1000.48] was causing major delays on their product roadmap.
[1001.54 → 1004.72] And larger companies also, of course, care about scalability
[1004.72 → 1009.06] in terms of being able to scale horizontally using Congo sharding.
[1010.50 → 1016.88] Sometimes it's helpful to be able to describe a technology to also maybe draw a distinction to some other technologies.
[1017.56 → 1020.70] So maybe we can go down the list and name a few of these
[1020.70 → 1025.70] and just kind of highlight some differences and approaches between a few of these NoSQL solutions.
[1025.94 → 1029.06] So Congo versus React, what do you see as the big difference there?
[1029.06 → 1037.40] All right, so React and all the sort of the Dynamo style databases are really distributed key value stores.
[1038.08 → 1041.72] And I think, you know, I've never used React in production,
[1041.88 → 1048.78] but I have no reason not to believe it's not a very good, highly scalable distributed key value store.
[1048.78 → 1055.44] The difference we've seen in something like React and Congo is that Congo really tries to solve a much more generic problem.
[1056.72 → 1061.10] So, you know, one is sort of a couple of, you know, a couple of key points.
[1061.18 → 1061.94] One is consistency.
[1062.84 → 1067.68] So, you know, Congo is fully consistent, and all Dynamo implementations are eventually consistent.
[1068.40 → 1073.52] And for a lot of developers and for a lot of applications, eventual consistency just is not an option.
[1073.52 → 1077.06] So I think for, sorry?
[1078.26 → 1085.60] So I think for the default data store for a website, you need something that's fully consistent.
[1086.72 → 1094.38] The other, you know, the other major difference is just data model and queryability and being able to manipulate data.
[1094.70 → 1097.64] So, for example, with Congo, you can index on any fields you want.
[1097.70 → 1098.86] You can have compound indexes.
[1099.28 → 1103.50] You can sort, you know, all the sort of the same kinds of queries you do with the relationship.
[1103.52 → 1104.72] You can do a lot of relational databases work with Congo.
[1105.50 → 1108.26] In addition, you can, you know, update individual fields.
[1108.44 → 1109.34] You can increment counters.
[1109.62 → 1114.76] You can do a lot of the same kinds of update operations you would do with, you know, with a relational database.
[1115.42 → 1120.40] So it maps much closer to a relational database than to a key value store, right?
[1120.46 → 1128.52] You know, key value stores are, you know, are great if you need, you know, if you've got billions of keys, and you need to store them, they'll work very well.
[1128.52 → 1139.58] But if you need to sort of replace a relational database with something that has, that is pretty feature comparable, they're just simply, you know, they're not designed to do that.
[1140.04 → 1144.58] What I hear a lot, document versus document, MongoDB versus Couch DB.
[1144.58 → 1146.04] Where do you see that one shaking out?
[1146.46 → 1151.18] So I think we've decided, you know, there are a few major differences between Congo and Couch.
[1151.28 → 1159.88] And I think a lot of it ends up being around how it interacts with, you know, both on the API side and sort of where we've been focusing.
[1159.88 → 1169.52] I think Couch has gone for a more, or so they have map reduced views, which are sort of very elegant.
[1171.10 → 1173.82] And there are some nice features there.
[1173.88 → 1179.68] And they've also spent a lot of time working on master-master replication and conflict resolution.
[1179.68 → 1187.54] And one of their, you know, one of the major things they've been talking about, you know, recently at least, is you have to do online syncing versus offline syncing, right?
[1187.54 → 1192.48] If you want to use something on your, you know, have a database that runs in your phone and in the cloud and have it all sync up.
[1193.12 → 1196.18] And, you know, that's an application that Congo simply would not work for at all.
[1196.80 → 1201.84] Congo's more focused on the core website infrastructure side of things.
[1201.84 → 1211.08] So, more large scale, you know, Congo has, you know, sharding built in, much more closely, much more similar feel to a relational database.
[1211.56 → 1217.42] Whereas, you know, if you want to do a query with sorting, you create an index, you create a compound index.
[1217.78 → 1220.90] The same way you would in a relational database, you would actually just go and create the index.
[1221.34 → 1225.56] You would do a query, you know, similar to the way you do in a relational database, right?
[1225.56 → 1230.94] In Congo, you would say, you know, if I want to find everyone who lives in New York sorted by age, it would be something like, you know,
[1230.94 → 1235.40] find where name equals, you know, where city equals New York, sort by age.
[1236.94 → 1241.10] And so it's a much more relational feel to it.
[1242.66 → 1245.38] Speaking of geospatial, you guys have just tweaked.
[1245.70 → 1253.96] Is it in 1.7 or 1.8 that you tweaked the geoindex to be not just rectangular but elliptical?
[1254.90 → 1257.26] So 1.7, 1.8 is kind of the same thing.
[1257.66 → 1259.28] 1.7 is the development version.
[1259.28 → 1262.52] So basically in 1.8, we'll have a spherical version of geo.
[1262.98 → 1273.68] So if you do want sort of more precise geospatial indexing on a sphere, it will work much better.
[1274.86 → 1276.18] So that's in 1.8.
[1277.00 → 1282.82] So if someone's evaluating Congo, what types of application tasks do you think that Congo does extremely well?
[1283.42 → 1288.10] You know, so the most common use cases for Congo are, you know, sort of core website infrastructure.
[1288.10 → 1293.14] So things like user profiles or, you know, any kind of CMS type data.
[1293.14 → 1301.24] Those are the kinds of, you know, data models that really don't work terribly well in a relational database that work very well in Congo.
[1301.74 → 1302.10] Right?
[1302.12 → 1311.72] If you look at user profiles, for example, in a relational database, a user profile may very well encompass, you know, 50 different rows and seven different tables.
[1312.38 → 1315.56] In Congo, the nice thing is you can actually just put it all into a single document.
[1315.56 → 1316.00] Right?
[1316.40 → 1319.52] So if you're just thinking about sort of user profiles and addresses.
[1320.20 → 1326.60] Well, if any user may have three addresses, in a relational database, you'd have a users table and a user address table.
[1327.22 → 1333.50] And so if you wanted to find everyone who lived in New York, you'd end up doing a join between the user table and the user address table.
[1334.20 → 1335.80] In Congo, you'd have a single document.
[1336.10 → 1338.66] That document would have an array of addresses in it.
[1338.66 → 1340.42] And you can index on that array of addresses.
[1340.96 → 1348.04] So if you wanted to find all people who live in New York, you'd simply do a query like users where address. City equals New York.
[1349.18 → 1359.08] So it's sort of a so it's both simpler from a code perspective, and it's much more performant because you've got a single document on disk.
[1359.08 → 1361.08] It's always going to be contiguous on disk.
[1361.16 → 1363.34] So it's like, you know, you can do one seek and load the whole thing.
[1363.64 → 1365.42] If you want to update it, it's talking to a single place.
[1365.80 → 1369.52] And you're never doing any sort of joins between two tables.
[1369.62 → 1371.14] So it's much easier to scale horizontally.
[1372.08 → 1378.50] One of the things that a lot of other NoSQL databases have that Congo doesn't is a sort of REST interface.
[1378.50 → 1381.16] Is that one of those core features that you guys are thinking about adding?
[1381.32 → 1383.24] Or is that something that is just not Mongolia?
[1384.60 → 1386.48] I think there's nothing wrong with a REST interface.
[1386.48 → 1392.36] I think that's something that we would probably put on the nice-to-have side of the world.
[1392.50 → 1396.34] I think REST is, you know, Congo is definitely meant to be behind a firewall.
[1396.96 → 1399.18] It's not meant to be sort of the front end to your website.
[1399.98 → 1403.90] We think that, you know, a lot of business logic should really live outside the database.
[1404.40 → 1409.64] That if you want a really horizontally scalable database, your database tier and your application tier do have to be separate.
[1410.16 → 1416.42] And then between the application tier and the database, simply a binary protocol.
[1416.48 → 1420.06] It's going to end up being faster and a little bit cleaner to implement.
[1420.74 → 1422.62] And you can, you know, do more things with it.
[1423.48 → 1425.98] And so we've decided to go down that route.
[1426.28 → 1430.00] And I think having a REST interface in the database is a nice thing.
[1430.20 → 1436.80] There are a bunch of community-driven layers on top of the database that give a fairly nice REST interface as well.
[1437.20 → 1441.88] So if people do want to use REST, they can use some of these third-party layers on top of it.
[1442.34 → 1447.32] I've pretty much only used Congo from Ruby myself, but I know that you guys have a lot of other drivers to other languages.
[1448.06 → 1452.08] What's sort of the breakdown, do you know, of what people use Congo in different language communities?
[1452.32 → 1454.18] Or, you know, which ones you see more often?
[1454.26 → 1455.34] How's that sort of breakdown?
[1455.34 → 1458.70] We really see it across the board.
[1459.06 → 1466.14] You know, there's a ton of, you know, a ton of Java, a ton of C Sharp, lots of Ruby, Python, PHP.
[1467.02 → 1472.76] We have users using Perl, C++, Erlang, Haskell, Node.js.
[1473.58 → 1479.64] You know, pretty much I've seen projects in almost every language I can think of.
[1479.64 → 1484.62] I've personally used the Racket driver, which is pretty nice.
[1486.48 → 1488.48] Again, that's a community-driven project.
[1489.40 → 1494.46] And so there's a lot of, there are a lot of drivers at this point.
[1494.84 → 1501.62] But in terms of where the usage is, it's pretty much, when I think about, you know, web development breakdown,
[1501.74 → 1502.62] it's pretty much where I'd expect.
[1502.80 → 1506.44] Most of the enterprises are using Java or C Sharp.
[1506.44 → 1511.76] A lot of the smaller sites or a lot of the startups are using, you know, Python or Ruby.
[1512.82 → 1514.16] There's still a lot of, there's a lot of PHP.
[1515.28 → 1517.16] So it's a little bit all over the map.
[1518.00 → 1520.26] I, I'm very interested in startups.
[1520.60 → 1524.76] And so you guys have a sort of interesting quality because you are a, you know, startup.
[1524.98 → 1526.50] You have a lot of the big name investors.
[1526.88 → 1530.06] But unlike a lot of startups now, you're not a website.
[1530.20 → 1531.58] You're actually a core technology.
[1531.84 → 1535.14] So do you see that as being a little bit different of a feel?
[1535.14 → 1538.04] Do you feel like you're still involved in the whole web startup world?
[1538.28 → 1542.40] Or is this, you know, is that sort of dividing factor in any kind of way?
[1543.80 → 1548.50] It's definitely very interesting because we sort of are, we go back and forth in that line a lot of times.
[1549.10 → 1552.04] Especially because we work with a lot of the, you know, web startups.
[1552.48 → 1555.22] So in some ways we feel very in touch with that universe.
[1555.36 → 1558.82] But at the same time, we are definitely not in the same space.
[1558.82 → 1567.00] We definitely don't, you know, we don't, you know, go to the same kinds of things.
[1567.10 → 1568.54] We're not affected by the same kind of changes.
[1569.22 → 1575.28] So there are some similarities, but I'd say we're more different than similar to a web startup on average.
[1575.96 → 1581.22] I have some snobby systems friends that always poo-poo, you know, web 2.0 websites.
[1581.36 → 1583.08] They kind of laugh at me every time I say that word.
[1583.08 → 1587.06] Speaking of laughing, what's your take on web scale?
[1588.50 → 1591.32] The web scale video or the video?
[1591.74 → 1595.24] And the fact that it's sort of been turned into the meme, I guess, is like, you know.
[1595.34 → 1603.92] Yeah, so, I mean, so the day the video came out, I have to say that the Tenpin offices were, there was a lot of laughter going on that day.
[1603.92 → 1611.20] And the guy who wrote it actually, or who made it, actually emailed us the same day, because he's actually a Congo user.
[1611.82 → 1614.88] And he emailed us saying, you know, hey, by the way, I'm sorry about that.
[1615.08 → 1616.78] I didn't mean it that way.
[1617.44 → 1620.50] And, you know, in our mind, it's all, you know, it's all in good fun.
[1620.50 → 1636.04] And I think it's one of those things with the new technology, with a, you know, somewhat, I wouldn't call it controversial, but with a sort of hot field where there are lots of companies vying for attention and users.
[1637.38 → 1641.10] It's very, you know, people like latching on to things like that.
[1641.24 → 1645.80] So it's, but on our mind, it's all, it's actually pretty funny.
[1645.80 → 1658.10] You know, I, my take on it was that Congo is so approachable, and that developers that may not really understand document databases and things come to Congo, and they can get their heads around it pretty easily.
[1658.24 → 1663.12] In the same way that a lot of people that don't write JavaScript feel that they can write JavaScript when using jQuery.
[1663.54 → 1666.56] So it kind of, you know, lowers the barrier of entry there.
[1667.68 → 1673.44] And I think it's important to be able to talk about the technologies you're using other than just the buzzwords and the website.
[1673.44 → 1680.18] I think that was one of the, the things that made it, so funny is because, you know, that verbiage is directly from the MongoDB org website.
[1681.64 → 1682.08] Right.
[1682.22 → 1685.86] No, it's, yeah, no, it was really quite funny.
[1687.14 → 1690.82] So under the hood for a moment, BSON, binary JSON.
[1691.40 → 1700.16] So when we interviewed Douglas Crockford, he said that the, the JSON spec would never change because it would always be frozen in time at, at 1.0.
[1700.16 → 1703.46] So has the same held true for BSON?
[1704.74 → 1705.44] Yes and no.
[1705.54 → 1711.30] So one of the nice things about BSON is that it's typed, and the types are in the document itself.
[1711.60 → 1713.82] So it's very easy to add new types.
[1714.50 → 1724.34] So that's one of the thing, you know, probably one of the main disadvantages to JSON for us was sort of the lack of types and the inability to extend it easily to add types.
[1724.34 → 1729.74] So that was really one of the main things that we did was make it easily, you know, make it easy to add types.
[1730.02 → 1732.96] So it's very easy for us to add types whenever, you know, as needed.
[1733.50 → 1736.60] So from that perspective, it's, it's really quite easy to do.
[1737.20 → 1739.34] At some point, we probably will do a version 2.0.
[1739.42 → 1743.56] There's a probably a few very subtle things we'd like to tweak at some point.
[1743.56 → 1751.02] And, you know, and the header and the BSON document headers actually have space reserved for a version field.
[1751.16 → 1754.90] So it will actually be fairly simple to, to change it at some point.
[1755.56 → 1757.72] And the website mentions protocol buffers.
[1757.78 → 1758.98] We've covered those here in the changelog.
[1759.04 → 1765.70] Was that something you considered when you set out to do Congo or is it, you needed the reversibility from the get-go?
[1765.70 → 1775.12] Yeah, we, we looked at protocol buffers briefly and, you know, protocol buffers were not quite so, you know, this was three and a half years ago.
[1775.46 → 1778.06] So they weren't quite where they are today.
[1778.22 → 1785.92] But overall, I think they're a little bit different from what we think is the right fit for Congo at the mapping side.
[1786.26 → 1789.02] So I don't think it's the right fit for us.
[1789.02 → 1796.62] I, I just went to the MongoDB roadmap to try to find a good question to ask you about what's coming in the future.
[1796.68 → 1801.06] And it says that I should contact my administrator because the page has been deleted.
[1801.36 → 1803.60] So what is the, is the future secret?
[1803.74 → 1804.66] What are you guys working on?
[1804.76 → 1807.20] Or can you just not tell me, or you have to kill me?
[1808.56 → 1810.00] No, I'm not sure which page you're looking at.
[1810.00 → 1817.56] But so the roadmap for, so the so for two points, so 1A is coming out in the next week or so.
[1817.56 → 1820.32] And so that has a bunch of stuff.
[1820.58 → 1827.88] And then after that, the next release is going to be 2.0, which will be coming out sometime in, in May or June.
[1828.44 → 1833.04] So 2.0 will have a number of things, some of which will be better aggregation.
[1835.26 → 1837.80] One of the major focuses for this year is going to be concurrency.
[1837.80 → 1841.52] So there will be some fairly large concurrency improvements for 2.0.
[1842.14 → 1844.18] We're going to be looking at doing online compaction.
[1844.18 → 1848.08] We're going to be looking at doing TTL timeout collections.
[1848.30 → 1851.58] So if you have time-sensitive data, you can age it out easily.
[1853.58 → 1858.30] Those are sort of, and then better aggregation is going to be another focus for this year.
[1858.76 → 1862.32] So when you're not hacking on MongoDB, what are you hacking on?
[1862.32 → 1868.60] There are not too many hours of the day when I'm not hacking on MongoDB at this point.
[1869.86 → 1877.50] I do have a, you know, I tend to write a lot of one-off C++ projects for myself to, you know,
[1878.40 → 1882.70] whether it's my, like, little CLI, you know, command line-based to-do list or a few other things.
[1882.84 → 1888.60] But at this point, the vast majority of my time is on MongoDB.
[1888.60 → 1892.84] And that's your for-fun language, too, that nothing higher level than that?
[1894.08 → 1897.34] I play around with Python for a lot of scripting stuff.
[1897.54 → 1900.22] I do like Scheme, so I play with Racket a lot.
[1900.46 → 1907.52] But once I delve into anything remotely complex, I usually end up defaulting back to C++ at this point.
[1907.52 → 1917.62] I think C++ has gotten a bad rap in many ways, and especially a lot of the new stuff coming out, you know, C++ 0x.
[1918.30 → 1923.72] It's really, it's quite an interesting language, and it's actually evolving in a very interesting way.
[1923.90 → 1926.88] So I'm pretty excited to see it changing.
[1927.88 → 1929.54] Vim, TextMate, Emacs?
[1929.54 → 1930.02] Emacs.
[1930.74 → 1931.18] Emacs.
[1932.14 → 1939.94] This is a we've got a 10-gen definitely has a definitely split, but Emacs definitely comes out on top.
[1941.50 → 1944.16] So who is your programming hero?
[1945.64 → 1948.38] Who do you aspire to be like in your epic hacking?
[1950.98 → 1952.64] I would have to get back to you in that one.
[1955.20 → 1956.08] That's a tough one.
[1956.08 → 1964.96] You know, I think there's a lot of, you know, it's a very good question, because there's definitely, you know, I think there are a lot of hackers who, you go two ways, right?
[1964.98 → 1970.94] You've got the hackers who go more project management style, right?
[1971.00 → 1971.82] You know, you've got Linus.
[1971.94 → 1972.06] Yeah.
[1972.34 → 1981.94] You know, you've got the Linus style who, I think I saw a quote from him recently where he said, most of the code he writes these days is in his email editor in response to people telling him how to fix their code.
[1981.98 → 1982.86] Yeah, yeah, I saw that.
[1982.86 → 1989.72] And then you've got people who write books, and then you've got people who end up just, you know, writing code for a long time.
[1989.80 → 1996.88] And I'm definitely in the writing code for a long time mindset at this point, but we'll see what happens over the next decade or so.
[1998.18 → 2003.98] You know, I was turned on to MongoDB from a lightning talk at, I think, Mountain West Rubicon a couple of years ago.
[2004.10 → 2006.10] I've been using it for almost two years now.
[2006.10 → 2010.84] So any tips or advice for spreading the word about your awesome open source project?
[2011.74 → 2021.10] Yeah, I think the key for people to, like, understand why Congo is interesting is to understand that it's not a key value store, that it's actually good for multiple things, right?
[2021.24 → 2028.10] If you look at the two main things that's interesting because of agility and because of scalability.
[2028.10 → 2032.06] And on the agility side, it's not only that you can change the schema at will.
[2032.20 → 2043.16] It's that it's very easy to get into because, you know, a document database maps very well to the way you think about objects in the real world, to the way that your code is arranged, right?
[2043.24 → 2047.60] You know, a MongoDB document looks very similar to a Ruby object.
[2047.60 → 2051.94] So it's a very, you know, if you just want to get in and start programming, it works very well.
[2052.42 → 2057.40] When you want to then start making sure it's performing well, it's got all the indexing, all the features there to help you.
[2057.74 → 2060.30] And then if you're doing well, and you need to scale it, it also helps you there.
[2060.94 → 2066.34] So I think that, you know, one of the keys about Congo is that it's not just sort of, it doesn't try to solve one problem.
[2066.86 → 2069.44] It tries to really address the database problem as a whole.
[2069.44 → 2078.96] And really, you know, has this, you know, has features at both when you're starting out, when you're sort of in the middle stages and when your needed to scale it up all the way.
[2079.66 → 2080.80] Well, we love using Congo.
[2081.22 → 2085.08] Look forward to the new features in 1.8 and then the big 2.0 release.
[2085.66 → 2086.90] And thanks for taking the time today, Elliot.
[2087.38 → 2088.32] No problem. Thanks for having me.
[2099.44 → 2129.42] Thank you.
