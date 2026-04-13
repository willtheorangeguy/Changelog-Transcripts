[0.00 → 8.94] what up gophers jarred here this episode is different from what you're used to hearing
[8.94 → 13.38] from go time we've been clipping highlights of the show for a while now to share on Twitter
[13.38 → 18.00] and YouTube and a side effect of that effort is I have a bunch of awesome clips just sitting on
[18.00 → 24.66] my hard drive collecting digital dust so here's a beta test of the best of style clips show covering
[24.66 → 29.46] the summer months I hope you enjoy it you might if you missed a few episodes or if you listen
[29.46 → 34.12] distracted sometimes like I do please let me know what you think in the comments if people dig it
[34.12 → 39.94] we'll probably do this more often if not well I'll just pipe the whole thing to dev know oh yeah and
[39.94 → 46.34] since it's a special kind of episode we have a very special intro song for you here we go
[46.34 → 57.28] band with her changelog is provided by fast learn more at fastly.com we move fast and fix things here
[57.28 → 62.20] changelog because of Rollbar check them out at rollbar.com, and we're hosted on Linde cloud
[62.20 → 72.16] servers head to leno.com changelog this episode is brought to you by digital ocean droplets managed
[72.16 → 79.04] Kubernetes managed databases spaces object storage volume block storage advanced networking like
[79.04 → 84.82] virtual private clouds and cloud firewalls developer tooling like the robust API and CLI
[84.82 → 89.76] to make sure you can interact with your infrastructure the way you want to digital ocean is designed for
[89.76 → 97.24] developers and built for businesses join over 150 000 businesses that develop manage and scale their
[97.24 → 102.60] applications with digital ocean head to do.co slash changelog to get started with a 100 credit
[102.60 → 105.12] again do.co slash changelog
[105.12 → 118.58] I see bars and kilobytes kilobytes
[118.58 → 145.08] ale nom
[145.08 → 147.08] Kilobytes.
[154.08 → 155.08] R's.
[155.08 → 156.08] Kilobytes.
[157.08 → 158.08] R's.
[159.08 → 160.08] Kilobytes.
[164.08 → 165.08] R.
[165.08 → 166.08] Kilobytes.
[166.08 → 167.08] R.
[167.08 → 168.08] Kilobytes.
[168.08 → 169.08] R.
[169.08 → 170.08] R.
[170.08 → 171.08] R.
[171.08 → 172.08] R.
[172.08 → 173.08] R.
[173.08 → 174.08] R.
[174.08 → 175.08] R.
[175.08 → 177.08] First up, we have a panel-only show.
[177.08 → 183.08] Yana, Matt, and John discuss how to effectively work with databases in episode 132, The Trouble
[183.08 → 184.08] with Databases.
[184.08 → 188.08] It just so happens this was the most popular episode of the summer.
[188.08 → 195.08] The way the database works or the way it models things is a lot of things in common with the
[195.08 → 196.08] storage engine.
[196.08 → 201.08] So the way you store, the way you shard, the way you really partition the data, there's
[201.08 → 206.08] a lot to do with the type of capabilities it provides to query.
[206.08 → 212.08] So from a high-level perspective, it's always important, I think, for a user to understand
[212.08 → 217.08] how at some sort of lower layer things are stored.
[217.08 → 223.08] So you can estimate what is feasible, what kind of use cases are actually a good fit for
[223.08 → 224.08] that type of database.
[224.08 → 229.08] Even though it sounds like a bit of work, I really suggest people to take a look at
[229.08 → 232.08] what type of use cases make sense.
[232.08 → 239.08] And in the end of the day, at the storage level, what do they do before evaluating anything?
[240.08 → 244.08] The classic example of that I've heard is that I've been told that at Stripe, one
[244.08 → 247.08] of the common things they've done is that they have a NoSQL database that they're using
[247.08 → 250.08] for all the really high-speed transactions.
[250.08 → 253.08] But then on the back end, when they want to run analytics and do all these other things,
[253.08 → 255.08] it's really hard to do that.
[255.08 → 259.08] And a lot of times people want SQL, they want to be able to use some tools that use SQL for
[259.08 → 260.08] that.
[260.08 → 262.08] So they actually take a lot of that data and translate it into a SQL database.
[262.08 → 265.08] And while it's delayed, it's only used internally, so that's okay.
[265.08 → 270.08] So they're taking that trade-off and deciding it's useful to have this data in both formats.
[270.08 → 272.08] And it's like you said, they didn't switch from one to the other.
[272.08 → 277.08] It's more of a this makes sense for this use case, and we port it over to this for another use case.
[277.08 → 283.08] Yeah, in my experience, I'm seeing always like two or three databases in a system.
[283.08 → 285.08] You can't really fight the trade-offs.
[285.08 → 288.08] You get benefit from them differently.
[288.08 → 293.08] So, basically, there's usually a relational database and other database for warehousing reasons,
[293.08 → 295.08] like analytics and so on.
[295.08 → 301.08] And then there's usually a database like, or something like elastic for, you know, for search reasons.
[301.08 → 306.08] So, you know, you can at least like list three core data resources.
[306.08 → 307.08] Yeah.
[307.08 → 311.08] And then of course, backup could even be a different one where you're taking, taking backup
[311.08 → 316.08] and putting it in some kind of cold storage or just less active place.
[316.08 → 321.08] It's common, I think, for developers to want to get the perfect solution from the beginning
[321.08 → 323.08] and just build that.
[323.08 → 328.08] But probably a better strategy is to just start with something, one thing, simple,
[328.08 → 330.08] do what you're going to do with it.
[330.08 → 337.08] There are like three things you can have, you know, in distributed systems, you can't have
[337.08 → 339.08] three of these things you have to pick to.
[339.08 → 343.08] And those three things are represented by CAP, which is C-A-P.
[343.08 → 346.08] CAP means consistency, sorry.
[346.08 → 348.08] A means availability.
[348.08 → 353.08] P means partition tolerance, like, you know, network partitioning tolerance.
[353.08 → 363.08] And what he says is, if you want 100% consistency and 100% network failure partitioning tolerance,
[363.08 → 366.08] you can't have 100% availability.
[366.08 → 369.08] You always have to make that sacrifice.
[369.08 → 374.08] You know, we're talking about relational databases as well as like, Stimulus, NoSQL type of databases.
[374.08 → 379.08] Actually, relational databases are more like CP systems.
[379.08 → 381.08] They have higher consistency.
[381.08 → 383.08] They are more tolerant to partitioning.
[383.08 → 389.08] On the other hand, NoSQL databases are, you know, compromising from consistency.
[389.08 → 394.08] They're eventually consistent, but they provide higher availability.
[394.08 → 396.08] So they're AP systems.
[396.08 → 401.08] So if you have this like mental model, I think databases are becoming easier to understand because, you know,
[401.08 → 408.08] that like there's a limit, like there's like physical limits to the world, and you can't have it all.
[408.08 → 413.08] And I've worked for some project managers that really just don't agree with this.
[413.08 → 415.08] They want all three.
[415.08 → 416.08] Yes.
[416.08 → 418.08] Because, you know, it's just hard to explain.
[418.08 → 419.08] It's almost like.
[419.08 → 422.08] Spanner is actually a typical CP system.
[422.08 → 432.08] It has 100% consistency, and it's very tolerant to partitioning, but its availability is significantly higher than any other relational database,
[432.08 → 438.08] which is provides five nines of availability, which means like five minutes downtime a year.
[438.08 → 440.08] You know, that's like amazing.
[440.08 → 447.08] Like most of the relational databases require 10 minutes or whatever a month for maintenance and so on.
[447.08 → 455.08] Or if you want to upgrade the, you know, the schema, it requires downtime or the failover requires downtime.
[455.08 → 457.08] So how did this happen?
[457.08 → 463.08] Like, you know, the Spanner team kind of says that they're beating the cap theorem because they provide this like high availability.
[463.08 → 474.08] And it has a lot to do the way how the internals of this distributed system is working, plus our good networking infrastructure.
[474.08 → 481.08] So we're just kind of like, you know, improving the availability, not to 100%.
[481.08 → 486.08] We're still talking about five nines, but five nines is actually a lot in practice.
[486.08 → 493.08] So, you know, our goal is like, maybe you shouldn't make as many as compromises.
[493.08 → 500.08] We will try to, you know, provide you a higher availability, but you will still have the like transactional relational database.
[500.08 → 509.08] But at the same time, we have a lot of limitations around like, you know, the type of the schema limitations, for example, some SQL limitations.
[509.08 → 516.08] I actually was reading Martin Lehman's book, maybe like two months ago.
[516.08 → 522.08] And then in my dream, I saw myself writing that blog post.
[522.08 → 530.08] And as soon as I woke up, I took notes, like, I think I dropped the 10 items on the cover of that book.
[530.08 → 537.08] So that blog post actually like probably came from some of the ideas that I got from his book and so on.
[537.08 → 544.08] So that's hilarious that like, you know, I saw that like the article was being very useful in my dream.
[544.08 → 545.08] And it turned out to be true.
[545.08 → 546.08] It's so funny.
[546.08 → 553.08] Well, if people didn't feel stupid before, the fact that Yana's coming up with this stuff in her sleep is certainly going to do that.
[553.08 → 555.08] That's how Paul McCartney wrote yesterday, by the way.
[555.08 → 558.08] He just woke up and had the song.
[558.08 → 559.08] My dreams are way less productive.
[559.08 → 563.08] Yeah, I just dreamed my legs were made of jelly.
[563.08 → 564.08] That's not helping anyone.
[564.08 → 566.08] I can't turn that into a blog post.
[566.08 → 567.08] Probably could.
[567.08 → 568.08] I might.
[574.08 → 583.08] On episode 135, John was joined by Chris Brando, Ben Johnson and Aaron Schlesinger to discuss some of their mistakes and how they learn from them.
[583.08 → 593.08] One of the mistakes I made when I first was jumping into Go was that I just felt like I over planned, or I tried to like over optimize for getting things perfect.
[593.08 → 598.08] So you'd read about how you shouldn't use MVC and you shouldn't do all these different things.
[598.08 → 601.08] And I sat down, and I'm like, all right, I'm going to write this side project.
[601.08 → 602.08] It was a side project.
[602.08 → 603.08] It wasn't like my main work stuff.
[603.08 → 608.08] So I was like, I'm going to build this thing, and it's going to be a good go code.
[608.08 → 613.08] And I think I spent so much time rewriting some stuff because I was like, oh, this is a bad way.
[613.08 → 614.08] And I realized why.
[614.08 → 616.08] And then I'd go back and rewrite it.
[616.08 → 622.08] And in the end, I'm pretty sure what I ended up doing was just using a simple MVC model and just got it done.
[622.08 → 625.08] And then later I was able to come back and tweak things and adjust.
[625.08 → 633.08] But it just I wasted so much time trying to like to meet the expectations of everybody, I guess, is how I'd put it.
[633.08 → 642.08] And to me, that was a big mistake because I feel like you learn more by just kind of jumping in and doing stuff rather than like trying to find the optimal path.
[642.08 → 653.08] I guess kind of a long ongoing mistake in my career is just not understanding the underlying technologies that I use, especially early on, like using like an HTTP framework, like web framework.
[653.08 → 655.08] You know, just assume that that's what you do.
[655.08 → 666.08] But like understanding that framework and maybe even like layers on top of that framework is a lot of times more complicated than just understanding HTTP or whatever the underlying technology is.
[666.08 → 674.08] So I feel like I've done that for a long time in my career, but more recently just trying to step back and just understand, like, you know, what do those frameworks actually give me?
[674.08 → 675.08] What do they add?
[675.08 → 679.08] And just a lot of times the net HTTP is, you know, enough with a router.
[679.08 → 686.08] So I guess first off, are you talking about going all the way down to actually understanding how like TCP works and going even below that or?
[686.08 → 691.08] I mean, I think it's a trade-off of like, what do you get for that abstraction that you're working with?
[691.08 → 705.08] Like, I'm, I mean, I'm not pushing bits across an Ethernet accord, but if I can, you know, understand like, you know, just basic headers and what they do, rather than having some other library on top of that to actually, you know, set certain parameters.
[705.08 → 714.08] I feel like just understanding that kind of underlying HTTP RFC or some aspects about it helps me just to write more direct code.
[714.08 → 731.08] I feel like if you go on GitHub and you look at some popular open source projects, I feel like that's sort of the Instagram of programming and that you see the perfect result after everyone's, you know, put on the makeup and rolled camera and everything.
[731.08 → 734.08] And, you know, we put that on ourselves.
[734.08 → 741.08] Whereas, you know, like Ben, you just said, you could just go in and write a for loop, and it'll be good for a while.
[741.08 → 744.08] It's just, you got to start somewhere.
[744.08 → 751.08] And there's always the telltale sign of like initial commit has like 20 source files and 4,000 lines of code.
[751.08 → 753.08] And you're like, that was your initial commit.
[753.08 → 756.08] It's like that clearly was not your initial commit.
[756.08 → 763.08] I like to just kill the dot get repo or the folder and just restart after probably a couple of hundred commits in.
[763.08 → 764.08] Oh, I'm the same way.
[764.08 → 769.08] It's like I've got the initial version and then that eventually gets to something, and I'm like, okay, I'm okay with sharing this.
[769.08 → 772.08] And then delete, you know, and just go from scratch.
[772.08 → 776.08] On one hand, I get why you do it because you don't necessarily want that bad history there.
[776.08 → 784.08] But on the other hand, it is kind of hard for somebody jumping in who actually thinks that might be the initial commit.
[784.08 → 790.08] Next up, 136.
[790.08 → 799.08] This is when Matt joined the show as a guest with his Pace co-founder David Hernandez to talk about the technical decisions they made while building Pace with Go.
[799.08 → 802.08] Yeah, absolutely.
[802.08 → 807.08] And I tell teams this when I talk to different teams as well about that when they're choosing their technology.
[808.08 → 809.08] That's a big thing.
[809.08 → 815.08] You know, GRPC, for example, might be the perfect choice from a purely technical perspective.
[815.08 → 821.08] But if nobody on the team has experience with GRPC, then there's a learning curve there.
[821.08 → 830.08] And some people talk about them in terms of innovation tokens and things, you know, you're not allowed, they say, to just all the technology can't be new and unfamiliar.
[830.08 → 836.08] You can do some of that, but there's effort and there's kind of a cost to being productive in any of those.
[836.08 → 842.08] And we had that already on the front end because we hadn't done much front end work for a while.
[842.08 → 847.08] And we knew we wanted to use a it was going to be a rich front end.
[847.08 → 850.08] So we knew it had to be somewhat of a modern.
[850.08 → 863.08] So you weren't trying to emulate GRPC, basically, you wanted to, you got some ideas from how sort of it works, and you stole some, and I use that very generously.
[863.08 → 866.08] You stole some ideas, some implementation details, rather.
[866.08 → 867.08] Sure.
[867.08 → 871.08] And you sort of issued the whole binary format.
[871.08 → 880.08] You just went, you're playing JSON, and basically you solved your own problem in a sense, and rather than sort of bringing in something for the sake of, because it's cool.
[880.08 → 881.08] Yeah.
[881.08 → 884.08] Stealing from open source is not really stealing, isn't it?
[884.08 → 887.08] It's just kind of Robin Hood.
[887.08 → 888.08] Why?
[888.08 → 889.08] Yeah.
[889.08 → 893.08] Different sizes comes with different problems.
[893.08 → 895.08] Speed is different.
[895.08 → 906.08] And that's why people try to put things like microservices, not because the microservices are better technology, because it's easier to control the size of the team or the responsibility, things like that.
[906.08 → 917.08] In this case, everything is easy in that sense, because we are two people, but we became from full stack developers to full company developers.
[917.08 → 922.08] We do support, we do marketing, we do accountancy.
[922.08 → 926.08] So it's not only the tech stack is quite wide in that sense.
[926.08 → 930.08] You have to worry about a lot of more things in this case.
[930.08 → 931.08] Yeah.
[931.08 → 938.08] I remember that release manager wanted to do like two releases a month and then be in sync with everyone.
[938.08 → 940.08] And they asked how many times we were releasing.
[940.08 → 947.08] And it was that day was something between 10 and 20 or something, you know, it was a very different mindset of rapid.
[947.08 → 953.08] As soon as it's a bit better than it was, you know, we want to kind of get it out.
[953.08 → 962.08] On episode 137 databases, we're back on the table.
[962.08 → 963.08] See what I did there.
[963.08 → 970.08] This time, Johan Braun horst joined Johnny, Matt and John to focus in on Postgres.
[970.08 → 977.08] Big thing that Postgres has over SQLite in Go specifically is perfect library support.
[977.08 → 982.08] Unfortunately, the SQLite driver that everyone uses is a C Go driver.
[982.08 → 986.08] And as most of you probably know, C Go means building with C.
[986.08 → 987.08] It means longer build times.
[987.08 → 990.08] It means less portable binaries and stuff like that.
[990.08 → 997.08] So in Go with Postgres, we actually have several different pure Go libraries to speak with Postgres, which is really great.
[997.08 → 999.08] So that's just one reason to use Postgres.
[999.08 → 1005.08] But other things such as the stability of the software, for example, as you say, it's over 20 years old.
[1005.08 → 1008.08] It's been used by thousands of companies worldwide.
[1008.08 → 1015.08] You know, it's not going to be just, you know, corrupt your files because those bugs have been ironed out by now.
[1015.08 → 1024.08] So within databases, I think you often say you don't want to use something that's less than 10 years old, because like this data needs to live for a long time.
[1024.08 → 1028.08] You want to make sure it doesn't, you know, corrupt on the disk or whatever.
[1028.08 → 1032.08] And Postgres is one such stable, mature solution.
[1032.08 → 1035.08] It's also very fast because it's written in C and C is fast.
[1035.08 → 1044.08] Yeah, no, I was sitting here nodding along to what you were saying there that start with Postgres, because I think a lot of users come into the space knowing what to use.
[1044.08 → 1054.08] And that was kind of the hope with my talk, just giving you an introduction to something you can use, some opinionated tips on what libraries to use and so on, giving you like a head start.
[1054.08 → 1062.08] Just getting started with actually like moving away from the problem of choosing a technology and actually using the technology to solve your problems.
[1062.08 → 1077.08] I really agree with that sentiment that a lot of people will try and, you know, Google, what should I use to store my data or even like read some popular programmers blog where they have tested out the latest technology and found it to be perfect for their very specialized use case.
[1077.08 → 1081.08] And then apply that to like all of their problems, because that's all they know.
[1081.08 → 1090.08] And, you know, starting with something well tested, well established, like you say, good to develop mind share like Postgres will take you very far before you need to change.
[1090.08 → 1094.08] How do you actually use Postgres?
[1094.08 → 1104.08] And I'm even thinking like in the context of, say, a website that is hosting a blog, at what point would you make a connection to Postgres?
[1104.08 → 1112.08] Do you tend to make one connection per instance of your code running and then create sessions off that?
[1112.08 → 1116.08] Or does each handler, would each handler make its own connection?
[1116.08 → 1120.08] How does it actually work, you know, from a Go developer's point of view?
[1120.08 → 1128.08] Yeah, so if we take a step back and look at the standard library database SQL package, that actually has a connection pool built in.
[1128.08 → 1141.08] So if you come from another language like Python or Ruby, you might be familiar with putting something, I think there's a Postgres bouncer or something like that, which does connection pool in between your database and your client.
[1141.08 → 1145.08] In Go, you don't need to do that sort of thing because it's already built into the standard library.
[1145.08 → 1151.08] So what you would normally do when you connect to the database is just created a single SQL.db handle.
[1151.08 → 1153.08] And then that's safe for concurrent use.
[1153.08 → 1158.08] So you can use that in all of your handlers, even though they're being called from different Go routines from different clients.
[1158.08 → 1165.08] And you can also configure things such as max connections on the SQL connection.
[1165.08 → 1168.08] But normally that's all handled by the Go standard libraries.
[1168.08 → 1171.08] You don't really have to worry about it, which is really nice.
[1171.08 → 1174.08] Actually, I have never had the pleasure of using an ORM.
[1174.08 → 1177.08] So what am I doing on this show talking about databases?
[1177.08 → 1186.08] I would very early on in my career, I was kind of persuaded against using an ORM because naturally, as a beginner programmer, I was like, oh, this looks cool.
[1186.08 → 1191.08] But I never really had to use it because I was told by someone who knew better than me that that was a bad idea.
[1191.08 → 1202.08] So here I am saying to other beginners like myself, Bonds was, that you should try not to use the ORM, even though it looks really appealing at first.
[1202.08 → 1206.08] You should probably just learn to use SQL, and it's really not that bad.
[1206.08 → 1209.08] And you'll learn to love it, I think, like I do.
[1209.08 → 1217.08] I would agree with that, having come from the other side, because everything specific to Rails that I learned is useless to me now.
[1217.08 → 1222.08] And everything I learned about SQL along the way when I couldn't get that to work is much more useful to me.
[1222.08 → 1224.08] And it'll carry over to any language.
[1224.08 → 1225.08] That's right.
[1225.08 → 1230.08] Well, that would have been an unpopular opinion section, but everyone agrees.
[1230.08 → 1232.08] It's not that unpopular, I guess.
[1232.08 → 1234.08] It's not happened before where we all agree.
[1234.08 → 1237.08] I need to ask, have you met Bobby Tables?
[1237.08 → 1238.08] I have met Bobby Tables.
[1238.08 → 1240.08] This is a great one, actually.
[1240.08 → 1263.08] So the reference that Johnny is making there is to an XKCD comic, which has a very illustrative way of showing just exactly what SQL injection means, where there's a school principal who's making a call to a concerned parent, I suppose, asking about their son Bobby Tables, dash, drop table students or something like that.
[1263.08 → 1266.08] The parent says, yes, we can't hit Bobby Tables.
[1266.08 → 1270.08] And then the principal says, well, I hope you're happy we've lost this year's student records.
[1270.08 → 1279.08] It's hilarious because obviously the implication there is that they had to enter their kid's name somewhere in some sort of form or something.
[1279.08 → 1282.08] And they thought, hey, it would be fun to see if this is vulnerable to SQL injection.
[1282.08 → 1288.08] And then they put in that command that would, if it was vulnerable to SQL injection, drop the table, call students.
[1288.08 → 1291.08] And of course, the joke then is that it actually did.
[1291.08 → 1293.08] And principal is furious about it.
[1293.08 → 1298.08] And the kind of lesson, I guess, is that you shouldn't have been vulnerable to SQL injection.
[1298.08 → 1301.08] Now he's got no job, though.
[1301.08 → 1304.08] So that's no good telling him that, is there?
[1304.08 → 1306.08] His life's devastated by that.
[1306.08 → 1307.08] But yeah.
[1313.08 → 1317.08] Episode 138 was quite a departure and inspiring to many listeners.
[1317.08 → 1319.08] Inspiring to many listeners so we hear.
[1319.08 → 1325.08] Jackie Grin rod and DeShawn Carter joined John to talk about their first week with the Go programming language.
[1327.08 → 1329.08] You know if somebody is trying to learn Go, what do you suggest?
[1329.08 → 1330.08] I think, Jackie, you said exorcism.
[1330.08 → 1332.08] Is that where you would suggest people start?
[1332.08 → 1340.08] So I found it worked really well for me because you'd put your solution in, you could see how other people solved it, but you'd also have mentors come and comment.
[1340.08 → 1345.08] And the really nice thing for me about the mentors was that they're perfect at giving like iterative feedback.
[1345.08 → 1349.08] So give me like some feedback and be like, here's how you can solve this a little bit more elegantly.
[1349.08 → 1350.08] And then I would do that.
[1350.08 → 1354.08] And then they'd come back and be like, OK, so now that you've done that, here's like another step you can do.
[1354.08 → 1356.08] And so we got to like that final iteration.
[1356.08 → 1362.08] And I do have all those commits like tracked so I can kind of watch the way that I grew as I was learning and the feedback I got.
[1362.08 → 1365.08] So I would actually recommend that because it was a very nice experience for me.
[1365.08 → 1371.08] You got to do it, and you also got like professional feedback from people who do this, which you might not always get if you're just learning a language on your own.
[1372.08 → 1383.08] On the front of learning things, an advantage that I didn't really realize, like I knew I had it, but I didn't really consider it until a conversation I had, I think last week or this week, was about concepts like garbage collection.
[1383.08 → 1386.08] I would have learned that in my computer science classes.
[1386.08 → 1393.08] And there are things that I just kind of knew about going into this that I didn't really think about as in terms of like what I'm learning it on the job in an ops role.
[1393.08 → 1396.08] Maybe that's not something that just gets presented to you.
[1396.08 → 1400.08] It might be like this kind of concepts that you need to learn outside just the code.
[1400.08 → 1409.08] And that's kind of been interesting to figure out, like, how do you review either like best practices across different languages or different architecture patterns, which is not my strength.
[1409.08 → 1415.08] But trying to figure that out while learning the language can be pretty overwhelming and just figuring out where to start.
[1415.08 → 1424.08] But yeah, there was people that were consistently there, and it was nice because it was kind of like having this little support circle that I really didn't expect this.
[1424.08 → 1430.08] Like I expected streaming to be more like people coming in and being like, hey, you're doing that wrong.
[1430.08 → 1432.08] Like, hey, why didn't you do this?
[1432.08 → 1435.08] So it was really nice.
[1435.08 → 1437.08] I'm going to paint a picture.
[1437.08 → 1438.08] This is very similar.
[1438.08 → 1440.08] Like I said, every rep counts.
[1440.08 → 1441.08] I've been to the gym.
[1441.08 → 1445.08] You guys been to the gym, maybe not lately, but it's kind of the same experience.
[1445.08 → 1449.08] Like you definitely went out and you kind of said, hey, I'm going to go to the gym.
[1449.08 → 1453.08] I put it on a schedule, and I'm going, and maybe you have a gym buddy.
[1453.08 → 1454.08] I think everything goes better.
[1454.08 → 1455.08] You know, you're pairing.
[1455.08 → 1457.08] You had some accountability.
[1457.08 → 1462.08] And I basically said, I'm going to buy some weights, and I'm going to put them out here.
[1462.08 → 1463.08] And this was my path.
[1463.08 → 1468.08] I didn't put any like deadline, or I didn't have any severe accountability.
[1468.08 → 1471.08] I was kind of fitting it in, but it was my number one focus.
[1471.08 → 1476.08] But still, not only is it going to be stickier for you, I think that accountability.
[1476.08 → 1479.08] Yeah, I think you probably went further faster.
[1479.08 → 1487.08] How much time does your team spend building and maintaining internal tooling?
[1487.08 → 1489.08] I'm talking about those behind the scenes apps.
[1489.08 → 1491.08] The ones no one else sees.
[1491.08 → 1494.08] The S3 uploader you built last year for the marketing team.
[1494.08 → 1498.08] That quick Firebase admin panel that lets you monitor key KPIs.
[1498.08 → 1503.08] Maybe even the tool your data science team hacked together so they can provide custom ad spend analytics.
[1503.08 → 1505.08] Now, these are tools you need so you build them.
[1505.08 → 1507.08] And that makes sense.
[1507.08 → 1514.08] But the question is, could you have built them in less time, with less effort and less overhead and maintenance required?
[1514.08 → 1516.08] And the answer to that question is, yes.
[1516.08 → 1518.08] That's where Retool comes in.
[1518.08 → 1522.08] Rohan Copra, engineering director at DoorDash, has this to say about Retool.
[1522.08 → 1531.08] Quote, the tools we've been able to quickly build with Retool have allowed us to empower and scale our local operators, all while reducing the dependency on engineering.
[1531.08 → 1532.08] End quote.
[1532.08 → 1562.08] 
[1562.08 → 1565.08] Again, retool.com slash change load.
[1565.08 → 1585.08] Next up, Testify's maintainer, Bryan Snacks joins Matt and Mark Bates to talk about testing frameworks in Go.
[1585.08 → 1590.08] Because you literally put those things as strings into the test code.
[1590.08 → 1591.08] Yeah.
[1591.08 → 1595.08] And then from that you can generate some quite nice looking failures.
[1595.08 → 1599.08] If something fails, you can, you know, it reads quite nicely.
[1599.08 → 1601.08] But I found it to be too verbose, actually.
[1601.08 → 1608.08] And just saying, you know, not equal and then showing you the two values or something was just easier to see.
[1608.08 → 1616.08] The thing I like about BDD versus unit testing actually has to do with this kind of the names of the tests.
[1616.08 → 1617.08] Hmm.
[1617.08 → 1621.08] You know, when you're writing a simple test, right, you know, test that create does something, right?
[1621.08 → 1623.08] That's a pretty simple test name.
[1623.08 → 1631.08] But when you start having all those weird variants, right, then the string based text names become really, really useful.
[1631.08 → 1637.08] You know, when you can, when you just need a little bit more description as to what it is you're trying to test.
[1637.08 → 1642.08] And that's harder to do in a unit type of test where you have a function name.
[1642.08 → 1643.08] Hmm.
[1643.08 → 1644.08] Yeah.
[1644.08 → 1647.08] Have you seen property based testing as well?
[1647.08 → 1650.08] This is another kind of style.
[1650.08 → 1663.08] Yeah, it's almost like fuzzing for your functions where you specify not what values to test with, but what types of values your function takes as input.
[1663.08 → 1669.08] And obviously also what kind of output you expect.
[1669.08 → 1688.08] And then the property based testing framework of which one example is copter will then just generate, you know, whether it's random or in some specific sequence will generate plenty of values to then test your function and try and find edge cases for you that do not conform to a specification.
[1688.08 → 1690.08] That's really cool, isn't it?
[1690.08 → 1691.08] Yeah.
[1691.08 → 1696.08] The first exposure I had to that was with hypothesis in Python, and it was pretty awesome.
[1696.08 → 1705.08] I mean, an obvious problem there is, you know, have, especially if your functions are a bit more complex, that it can take a while for tests to run.
[1705.08 → 1711.08] Because you're now running the same function 10,000 times rather than once or five times.
[1711.08 → 1717.08] But, you know, for pure functions where, you know, where your code doesn't have side effects.
[1717.08 → 1718.08] Yeah.
[1718.08 → 1725.08] It's very good at finding edge cases and little behaviours that you didn't anticipate.
[1725.08 → 1728.08] In Ruby, we had a great thing called Time Cop.
[1728.08 → 1737.08] And it was such a random Ruby thing where it would override basically time. Now to be whatever it wanted it to be.
[1737.08 → 1739.08] Because you could just override anything.
[1739.08 → 1744.08] So you could say, like, I want to be three weeks into the future and time. Now would return three weeks in the future.
[1744.08 → 1746.08] Great Scott.
[1746.08 → 1747.08] Yeah.
[1747.08 → 1752.08] It was spectacularly awful and good and fun.
[1752.08 → 1753.08] Yeah.
[1753.08 → 1756.08] It was one of the things you can only do in a dynamic language though.
[1756.08 → 1757.08] Yeah.
[1757.08 → 1759.08] It's also the reason I'm not using a dynamic language.
[1759.08 → 1769.08] No, the way I look at it at least is if it's something that's, how likely is it to change?
[1769.08 → 1771.08] Basically, how likely is your database state to change?
[1771.08 → 1774.08] How likely is your time to change?
[1774.08 → 1781.08] If it's anything other than low, take it out, mock it out, make it as a dependency that's injected.
[1781.08 → 1784.08] But that's a rule of thumb that I follow anyway.
[1784.08 → 1794.08] Episode 140 was our most anticipated show of the summer.
[1794.08 → 1799.08] The latest draft proposal for Generics was posted in late June, and it took us a few weeks.
[1799.08 → 1807.08] But we managed to get Robert Gruesomer and Ian Lance Taylor on the show to answer many of the community's nagging questions about the latest proposal.
[1807.08 → 1814.08] Robert and I released the updated design draft for moving forward with Generics.
[1814.08 → 1835.08] The biggest change was that we dropped the idea of contract and just decided that instead of having a separate syntactic construct, which was a contract, that we could just use interface types to describe the contract between the type argument and the type parameter.
[1835.08 → 1845.08] A lot of people looking at contracts had seen that they seemed a lot like interfaces and people had trouble separating out exactly when you would use a contract and when you would use an interface.
[1845.08 → 1847.08] So we simplified this.
[1847.08 → 1850.08] And this was, I should add, almost entirely due to Robert.
[1850.08 → 1854.08] We simplified this to just use interface types.
[1854.08 → 1860.08] And then the second big step we made was we've released a translation tool and a type checker.
[1860.08 → 1866.08] So we have a type checker that works for the design draft, the description of generics in the design draft.
[1866.08 → 1871.08] So that gives us, you know, some confidence that what we have written about can actually work.
[1871.08 → 1876.08] And we have a translation tool which translates code into ordinary Go.
[1876.08 → 1879.08] The translation tool is not, by any means, a final thing.
[1879.08 → 1881.08] There are cases it doesn't handle.
[1881.08 → 1886.08] It's just an experimental tool, but it lets people actually write code that can actually run using generics.
[1886.08 → 1895.08] So we can get a feel for whether generics actually works for people and whether it actually addresses the issues that they have.
[1895.08 → 1912.08] So more practically for the Go community, when do you think that you're going to get enough feedback to move forward with moving from a draft proposal to actually putting it forth as a proposal to change in the language?
[1912.08 → 1915.08] Yeah, we don't have any timelines in mind, I'd say.
[1915.08 → 1923.08] As we mentioned earlier, we're still trying to pin down some of the precise semantics, which I don't think is going to affect any existing code.
[1923.08 → 1925.08] In fact, I'm sure it's not going to affect any existing code.
[1925.08 → 1927.08] We want to make sure that we understand it.
[1927.08 → 1932.08] We want to make sure that, you know, the multiple Go compilers will implement the same thing.
[1932.08 → 1935.08] We're going to have some sense of how to add to the language spec.
[1935.08 → 1938.08] So those are the steps we're looking at now.
[1938.08 → 1943.08] I mean, we're certainly going to move forward as fast as we can toward making a formal proposal.
[1943.08 → 1945.08] Of course, at that time, none of it will be a surprise.
[1945.08 → 1950.08] People will have seen all the ideas already, and we'll just have to see how it flies.
[1950.08 → 1954.08] So far, I feel like the reaction has been largely positive, which is encouraging.
[1954.08 → 1957.08] But I don't know exactly what the timeline is going to be.
[1957.08 → 1964.08] My experience with generics was maybe C++ with templates and probably the highest,
[1964.08 → 1970.08] the highest point there was when I was able to, as Ian alluded to before, it's Turing complete.
[1970.08 → 1977.08] I was able to write a program using C++ templates that would decide whether a constant was a prime number or not.
[1977.08 → 1980.08] And the compiler would decide it at compile time.
[1980.08 → 1984.08] So that's not the kind of thing we would like to support.
[1984.08 → 1993.08] With respect to, you know, what I'd like to see or not see is, honestly, I'm worried about the kind of code that people are going to write.
[1993.08 → 1995.08] I mean, there's no question about that.
[1995.08 → 2005.08] And we see some of the examples that people send us that cause crashes in the prototype, and they're just unbelievably convoluted and really, really hard to decipher.
[2005.08 → 2010.08] But as other people have pointed out, those people are really pushing the envelope.
[2010.08 → 2012.08] They're trying to just see what can I do with this thing.
[2012.08 → 2017.08] And I hope this is not going to be, you know, the kind of code that people are going to write down the road.
[2017.08 → 2033.08] I think one of the first things we need to do, if we have this for real, we need to come up with a kind of best practices guide that guides everybody a little bit as to how you should use generics and when you should use them and when you should not use them.
[2033.08 → 2034.08] I think there's also very important to desarrollo.
[2034.08 → 2038.08] In these two things I've been working with community of learning to implement humanity, and I may not do that for l administrations, but I won't add that quickly.
[2038.08 → 2039.08] I'll divide my together to our away.
[2039.08 → 2040.08] You can just add this.
[2040.08 → 2045.08] Many of our друга statistics are interesting, but if we don't know, we have arms behind or perpendicular to normal analysis and provide tools for it to the field.
[2045.08 → 2048.08] And those are» kinda important.
[2048.08 → 2052.78] The experimental tool has no similarity whatsoever to any real implementation.
[2053.24 → 2057.70] So we know it's slow, and it's going to be slow, and that's just inevitable.
[2058.42 → 2068.40] If this does move forward to become a proposal, and it gets accepted, then most likely the implementation will be to start with a branch of the main Go tool chain,
[2068.40 → 2078.16] and we'll start adding generic support on that branch, which will involve changing the compiler mainly and any other changes to other tools that are required.
[2078.64 → 2083.42] And so that'll be the time to start giving feedback about changes to build speed.
[2083.74 → 2087.94] We've talked about it with some of the compiler developers, like Keith Randall especially,
[2088.40 → 2093.06] and we think we can do it without a significant increase in build speed.
[2093.22 → 2094.56] I mean, there will be some increase in build speed.
[2094.56 → 2099.90] We don't think it's going to be a huge increase, but, you know, this is really speculative at this point.
[2100.14 → 2103.28] So the time to give that feedback is when we're able to start doing development,
[2103.40 → 2108.32] and hopefully people will also be able to contribute work when we start doing that work on the public branch.
[2109.54 → 2114.48] Programming language evolution is really a social process.
[2115.02 → 2120.80] It doesn't actually matter if you have seen the light, and you know exactly the perfect language,
[2120.80 → 2125.04] you know, and you would just put it out there and, you know, maybe it's 20 years ahead.
[2125.14 → 2130.28] Nobody would even buy it because people would not see the reasoning why you got to that point.
[2130.42 → 2134.14] And so you really have to get everybody along.
[2134.48 → 2137.98] And some people may already be where you are and some people may not,
[2138.10 → 2140.92] but you have to get everybody along in little steps.
[2140.92 → 2144.54] And that's how we eventually end up where we want to be.
[2144.80 → 2147.80] And we can see this with all kinds of things like a garbage collection.
[2147.88 → 2152.88] A garbage collection was invented, you know, 1950 something with Lisp.
[2153.04 → 2155.90] You know, the first Lisp had garbage collection, 1958, I believe.
[2156.56 → 2162.26] And it's taken forever before it became accepted as something that the programming language should,
[2162.70 → 2164.62] you know, a mainstream programming language should have.
[2165.24 → 2168.24] Maybe Java was the first one that really made it mainstream.
[2168.24 → 2174.00] And now this is not something that is, I mean, still disputed or debated, I should say,
[2174.06 → 2176.62] but it's not as outrageous anymore.
[2176.74 → 2178.44] And so I think that's true for other things.
[2184.76 → 2192.52] On episode 141, guest Daniel Marti helped Matt and Johnny explore Go's encoding JSON package.
[2194.40 → 2197.26] Yeah, and it's JavaScript object notation.
[2197.26 → 2199.50] So it comes out of JavaScript.
[2200.20 → 2203.94] But it turns out to be really kind of useful across a lot.
[2204.12 → 2207.18] Every language really has now some kind of JSON support.
[2207.82 → 2209.50] It's practically everywhere.
[2210.08 → 2214.44] Practically every language out there that's modern today has to have JSON support because you just do.
[2214.76 → 2218.62] And your computer, you might not see it, but it definitely is running JSON at some level.
[2218.62 → 2219.26] Hmm.
[2219.58 → 2220.02] Yeah.
[2220.12 → 2225.44] And so there's like, it's an object, and it has fields and those fields have some types.
[2225.80 → 2230.98] And it's the types that we're used to as well in Go, like strings and numbers and Booleans.
[2231.26 → 2232.04] Any others?
[2232.18 → 2234.60] Other objects, arrays, those kinds of things.
[2234.66 → 2236.22] I think that might be the whole list.
[2236.66 → 2240.06] And why did it get such popular use on the web?
[2240.06 → 2244.40] I mean, it kind of is kind of perfect, isn't it, for web technologies?
[2244.92 → 2249.96] I would say it came from all the success that browsers had, you know, the modern web had.
[2250.36 → 2258.10] And, you know, suddenly HTTP, HTML, CSS and JavaScript and JSON, all these technologies kind of took everybody by surprise.
[2258.10 → 2260.20] Initially, everybody thought they were just toys.
[2260.74 → 2263.76] But now suddenly people are building real companies on top of them.
[2264.52 → 2267.58] And JSON is just, you know, has too much momentum.
[2268.26 → 2271.20] I don't think anything is ever going to replace it at this point, honestly.
[2272.06 → 2278.20] And I have mixed opinions and feelings about all the third-party JSON re-implementations out there.
[2278.86 → 2280.22] I think some of them do make sense.
[2280.22 → 2288.58] For example, one use case is you do absolutely want the most performance you can get because maybe this is a bottleneck for you.
[2288.80 → 2297.52] And you don't mind Go generating some code to then, you know, write, generate automatically a decoder for you for JSON.
[2298.02 → 2300.70] So you can use packages like easy JSON for that, which is pretty popular.
[2301.00 → 2307.12] And the trade-off there is you have to run Go generate, and your binary is going to weigh quite a little bit more because it has quite a lot of extra code.
[2307.12 → 2312.72] But that extra code, it just encodes all the logic directly in binary code, in machine code.
[2313.04 → 2317.72] So there's no reflect, there's no dereferences, there's no extra work involved.
[2318.50 → 2322.16] So I think that's clearly one of the cases where it might make sense for a use case.
[2322.56 → 2323.90] I like how you framed that as well.
[2323.98 → 2326.46] You're saying maybe it's a bottleneck in your case.
[2326.70 → 2327.42] And that's the thing.
[2327.48 → 2332.72] It's like once you've seen that this is a place where an improvement is going to make a difference for you,
[2332.72 → 2338.94] then it's worth taking on the extra pain, whether it's complexity or learning a new API or whatever it is.
[2339.26 → 2343.76] I like that approach because, well, I think it's what we should always be doing.
[2343.90 → 2350.34] You know, as you alluded to, Johnny, we kind of can get a bit obsessed with why wouldn't we want the fastest possible thing?
[2350.38 → 2354.28] And the answer is it might be good enough just using the standard library.
[2354.28 → 2366.52] There are some bugs, for example, there's one that I would say affects most code bases out there, which is the standard, you know, you have an HTTP endpoint and the body is JSON.
[2366.68 → 2367.54] So you want to decode it.
[2367.90 → 2376.90] So what you do is you take the R.body, and you do JSON.new decoder.decode with the body and then into some structure.
[2377.44 → 2378.78] And if you do that, it's buggy.
[2379.08 → 2380.12] If you just do that.
[2380.54 → 2381.52] I've just got to go.
[2382.50 → 2383.82] What do you mean it's buggy?
[2383.82 → 2385.04] Tell me why, please.
[2385.42 → 2390.38] So this was found by Joe, one of the maintainers, I want to say about a year ago.
[2390.62 → 2397.40] And the bug is the decoder is meant to be useful for streams of JSON values.
[2398.04 → 2407.10] And that is, for example, when you do go test with the JSON flag, it's going to give you a new line separated stream of JSON values of JSON objects.
[2407.40 → 2410.10] Yeah, that's kind of how I was using it in those tools I was talking about.
[2410.30 → 2410.84] Yep, exactly.
[2410.84 → 2414.18] In a way, it is kind of streaming in a way.
[2414.40 → 2415.34] Like it takes the reader.
[2415.90 → 2418.72] For each object, it buffers it, I guess.
[2418.86 → 2421.22] But it discards that previous object, doesn't it?
[2421.40 → 2421.56] Yeah.
[2421.82 → 2422.56] Yeah, next time.
[2422.62 → 2422.80] Right.
[2422.88 → 2424.70] So in a sense, it's streaming.
[2424.98 → 2428.18] It appears to you as if it's streaming, but internally, that's not what it's doing.
[2428.18 → 2432.62] Well, it's still doing it only one object at a time, which you could say is a stream.
[2432.74 → 2435.10] It's just if it's a great big fat object, then.
[2435.50 → 2435.86] Exactly.
[2436.40 → 2436.88] In trouble.
[2437.24 → 2437.34] Yeah.
[2437.34 → 2449.82] Episode 142 was all about that infrastructure with special guest Shabekshah Japan.
[2449.82 → 2460.54] Maybe we should bust some of this jargon because, you know, you hear infra, I hear systems engineering, and I hear DevOps.
[2461.04 → 2463.48] Do we agree at least on what these terms mean?
[2463.88 → 2464.12] No.
[2464.12 → 2464.62] No.
[2466.04 → 2466.44] No.
[2466.90 → 2468.92] I mean, it's kind of funny.
[2469.10 → 2472.78] I mean, let's take, for example, one of the hot new titles out there, right?
[2472.82 → 2473.70] SRE, right?
[2473.80 → 2474.02] Yeah.
[2474.20 → 2479.88] And you'd think that, like, that would carry some sort of consistency, right, from organization to organization.
[2480.40 → 2482.04] That is entirely not the case.
[2482.14 → 2482.34] Yeah.
[2482.38 → 2483.02] Like at all, right?
[2483.68 → 2488.96] An SRE at Google is going to be very different from an SRE at Salesforce, which is going to be very different from an SRE at Microsoft.
[2489.44 → 2493.36] Yes, there is a through line between these things, and that goes for the other titles as well.
[2493.36 → 2496.60] Systems engineering, you know, DevOps engineer.
[2496.80 → 2497.78] I cringe a little bit when I say that.
[2497.90 → 2498.08] Yeah.
[2498.84 → 2502.38] But, like, basically, these things are going to mean different things in different organizations.
[2502.58 → 2511.40] Even in different sort of – and over the lifespan of an engineering team, right, the definition of that role may also change, right?
[2511.44 → 2521.24] So it's not – I don't think there is one sort of solid definition, right, of what, you know, software engineer, database engineer, infrastructure engineer, ops, whatever it is.
[2521.24 → 2523.26] I think it's going to be different everywhere you go.
[2523.50 → 2523.76] Yeah.
[2524.00 → 2526.38] I thought SRE was text speak for sorry.
[2527.00 → 2527.94] That's how I was thought.
[2527.94 → 2532.60] That's exactly what I ran into as well.
[2532.68 → 2533.82] It's a chicken-and-egg problem.
[2533.96 → 2538.32] You need experience to get a job, but to get a job, you need experience.
[2538.32 → 2540.18] So, like, where do you actually start?
[2540.26 → 2548.62] Because there is a very hard limit to, like, how much you can do and learn on your own when it comes to a job of this type, especially if you want to work at scale.
[2548.80 → 2552.96] Like, you simply cannot replicate the kind of things you'll be doing every day at home.
[2552.96 → 2554.40] So why is that, though?
[2554.54 → 2556.36] And it's such a big missed opportunity.
[2556.92 → 2564.20] Like, I'm seeing a lot of, like, people without a lot of experience coming into this field and, like, looking things from a very, like, new perspective.
[2564.60 → 2564.76] Yeah.
[2564.76 → 2573.30] In my experience, they've been really much more effective in terms of, like, pointing out the, you know, the core friction points than the experienced engineers.
[2573.44 → 2577.72] I think experienced people have a lot of, like, you know, they're accepting the current status.
[2577.72 → 2584.74] And they always assume that, like, there's all this, like, layers of things that, you know, you have to satisfy in order to kind of, like, provide.
[2584.86 → 2590.54] But is a new inexperienced engineer just coming in, like, questioning some of these, like, things more carefully?
[2591.24 → 2602.30] And that's sort of, like, the perspective that we are missing in infrastructure in general because, you know, there's no good connectivity, and we're just doing a bad job in terms of hiring people into this area.
[2602.68 → 2603.70] Yeah, completely.
[2607.72 → 2621.18] Last but not least, on episode 143, Francesc Cambó and Isabella Rettelmeier join Matt and Yana for a deep dive on Go's context package.
[2623.18 → 2631.20] Like, there's a very straightforward way of cutting down the latency, like, the tail latency in your requests.
[2631.20 → 2644.80] So if you have a request, let's say that you have a request that you send into a server, and it takes five milliseconds 99% of the time, but then there's 1% of the time that it takes one minute, which is not good.
[2645.16 → 2651.46] So what you could do is make that call multiple times, and you're going to do it with cancellation.
[2651.46 → 2655.12] So you're going to do context with cancel of your original context.
[2655.82 → 2663.60] And then what you're going to do is you're going to use the same context for all of those calls and have deferred cancel at the top of your function.
[2663.88 → 2670.34] And then as soon as any of those values returns, and you return from that function, the rest will be cancelled.
[2670.34 → 2676.06] And that's going to take down your 99th percentile from like one minute down to five milliseconds.
[2676.76 → 2684.86] So that's like small things that you can get a lot of performance, especially when you're using a server that is not something you manage.
[2685.02 → 2690.54] So you cannot go and complain to them about like, hey, your 99th percentile latency is awful.
[2690.96 → 2693.36] You can still fix it by doing this little hack.
[2694.10 → 2696.58] Why is there context.to do?
[2696.80 → 2697.20] Hmm.
[2697.94 → 2698.78] Great question.
[2699.40 → 2699.74] Yeah.
[2699.74 → 2700.62] I don't know.
[2702.08 → 2708.24] So context.to do and context. Background do exactly the same thing.
[2708.76 → 2710.30] They return an empty context.
[2710.78 → 2716.32] In an empty context, that doesn't have values, doesn't have timeouts, it never gets cancelled.
[2716.90 → 2718.88] So it's literally an empty struct.
[2719.04 → 2719.68] That's what it is.
[2719.68 → 2727.88] So the interesting thing is that when you return a background, what you're saying is that, oh, this is something that I'm starting from scratch.
[2727.88 → 2731.02] So you're basically saying there's no previous context.
[2731.02 → 2732.62] This is something that I'm creating, right?
[2732.68 → 2736.96] So for instance, in the example of the CLI, you're running your CLI.
[2736.96 → 2739.58] And at the beginning, there's no previous context or anything.
[2739.58 → 2743.28] Like maybe at one point, we'll have actually a context coming from signal.
[2743.72 → 2744.70] That would be an interesting thing.
[2744.74 → 2746.08] But otherwise, we don't have anything.
[2746.08 → 2748.70] So you would call background.
[2748.70 → 2761.04] Context.to do is actually was added just so as different functions, like you need to start, like you're creating a tree of functions that are calling and passing context around.
[2761.04 → 2768.24] So how do you do it if you want to add it to all of them, but little by little?
[2768.66 → 2774.42] Like if you start from the top, it's going to be, you cannot pass functions until they're accepted.
[2774.80 → 2781.46] But if you do it the other way around, like you build a function that starts by saying, oh, I accept a context now.
[2781.60 → 2783.12] And you can pass a context to me.
[2783.26 → 2788.66] Then the caller could say, oh, okay, so I should have a context, but I do not have it yet.
[2788.66 → 2795.34] So instead of calling context. Background, which implicitly says, I do not have a context and I will never will.
[2796.02 → 2800.04] So to do it just, hey, I do not have it yet, but let's fix it later.
[2800.16 → 2805.72] So it's literally just so when you grab to do, you can find where you need to still do more work.
[2806.24 → 2807.22] I think that's kind of cool.
[2807.28 → 2809.60] Like the fact that they thought about these.
[2810.20 → 2817.92] Otherwise, I mean, you could have done the same, calling context. Background and then having on top like a comment doing to do has a real context.
[2817.92 → 2819.58] But they did it this way.
[2819.64 → 2824.68] So it's more explicit, and you actually could do code analysis and look like, hey, this is not done yet.
[2828.74 → 2829.80] What's up, gophers?
[2829.96 → 2836.82] Are you looking for a way to instantly debug and troubleshoot your applications and services running in production on Kubernetes?
[2837.00 → 2837.68] That's a mouthful.
[2838.00 → 2841.84] Well, Pixie gives you a magical API to get instant debug data.
[2841.84 → 2845.20] And the best part is this doesn't involve changing code.
[2845.54 → 2849.22] There are no manual UIs and all this lives inside Kubernetes.
[2849.90 → 2859.42] Pixie is an API which lives inside your platform, harvests all of your data that you need and exposes a bunch of interfaces that you can ping to get data you need.
[2859.82 → 2862.66] Pixie is essentially like a decentralized Splunk.
[2862.66 → 2869.70] It's a programmable edge intelligence platform which captures metrics, traces, logs and events without any code changes.
[2870.02 → 2875.02] And the team behind Pixie is working hard to bring it to market for broad use by the end of 2020.
[2875.58 → 2878.08] But I'm here to tell you how you can get your hands on the beta today.
[2878.58 → 2883.08] Links are in the show notes, so check them out so you can click through to the beta and their Slack community.
[2883.40 → 2887.14] Once again, links from the show notes, check them out and look forward to Pixie Day coming soon.
[2892.66 → 2922.64] Pixie Day coming soon.
[2922.66 → 2924.34] Rolling UNPO Rockabilly.
[2924.68 → 2925.16] Enjoy.
[2928.16 → 2930.32] Unpopular opinion.
[2936.22 → 2938.02] Unpopular opinion.
[2941.86 → 2942.72] I don't know.
[2942.86 → 2948.28] I feel like most new technologies are just not necessary, I guess, would be my unpopular opinion.
[2949.16 → 2950.22] Docker, honestly.
[2950.22 → 2951.22] Like Kubernetes.
[2951.22 → 2951.90] Like Kubernetes.
[2951.90 → 2952.90] A lot of those.
[2952.90 → 2955.30] I feel like you can run a stack.
[2955.30 → 2956.56] Not the same stack.
[2956.56 → 2962.64] But you can run basically like what we used to run back in the 90s or whatnot or early 2000s where it's just like here's a web server running.
[2962.90 → 2964.34] You can run a business off of that.
[2964.46 → 2965.28] Probably be fine.
[2965.28 → 2968.62] I mean, obviously, back up your data, but that would be my unpopular opinion.
[2968.62 → 2983.76] I think for me, an unpopular opinion I have is, I guess, once your organization or your, I guess, the engineers in your organization reach a certain level that you shouldn't really just take software from other companies.
[2983.76 → 2994.10] Like, I think GRPC is like a big one for me where it's just like once you have a group of people that understands how to like to build things with TCP and HTTP, you could probably just build it yourself.
[2994.28 → 3000.76] And you should do that because your organization's needs are going to be very different from like what Google needed for when they built GRPC.
[3000.76 → 3006.94] So I think it's like I fall closer to that what used to be called not invented here syndrome.
[3007.10 → 3010.20] And I think like that's probably where we should be edging back to.
[3010.36 → 3013.42] But I realize that that is wildly unpopular with a lot of people.
[3013.84 → 3017.34] And they usually say, you know, just use whatever is out there because that's better.
[3018.16 → 3020.42] Well, I mentioned REST APIs earlier.
[3020.96 → 3022.62] I don't think they're good.
[3023.18 → 3024.78] That's my unpopular opinion.
[3025.56 → 3030.54] I think they cause more confusion than problems they solve.
[3030.76 → 3035.94] Actually, an unpopular opinion I have is, you know, you should try and work in tiny teams.
[3036.26 → 3042.04] A lot of the problems when it comes to software engineering come at scale.
[3042.30 → 3045.02] And that's not just code scale, but people scale.
[3045.34 → 3056.78] So if you can have tiny little teams working on a problem, and you can do this within bigger teams, like just literally as, you know, two or three people, you are now a new little team.
[3056.78 → 3065.18] You can be so effective in such a small group because you cut out a lot of the work needed really to marshal the team.
[3065.50 → 3066.54] You can't always do it.
[3066.76 → 3069.78] And it sounds a little bit antisocial, but that would be my unpopular opinion.
[3069.92 → 3070.72] Tiny teams.
[3071.34 → 3077.28] I have this library that I like to use, which is called Squirrel, and it's a query builder.
[3077.74 → 3079.90] And it uses the builder pattern.
[3080.98 → 3081.22] Aha!
[3081.52 → 3083.42] Everyone hates the builder pattern in Go, right?
[3083.48 → 3090.82] And for a good reason, because the builder pattern doesn't work well with the static typing that Go provides because we don't have generics.
[3091.46 → 3093.24] And Squirrel suffers from this problem as well.
[3093.24 → 3097.18] But it also provides a lot of power at the same time.
[3097.58 → 3101.78] So it's like the one exception to the rule of don't use the builder pattern anywhere
[3101.78 → 3105.34] is for query building, use the squirrel package
[3105.34 → 3109.82] because it's really easy to use and constructing queries with.
[3110.94 → 3113.58] So the builder package then, just for anyone not familiar,
[3113.74 → 3115.64] this is where you get these fluent APIs
[3115.64 → 3119.48] where every method returns the main object itself
[3119.48 → 3121.72] and then lets you chain them.
[3121.72 → 3122.48] Yeah, right.
[3122.48 → 3124.36] And I should say I hate these
[3124.36 → 3127.68] because you can't define interfaces that work with them at all.
[3128.34 → 3129.14] It's just a nightmare.
[3129.94 → 3131.38] So I do have one question, Johan.
[3132.20 → 3135.90] Could you reconstruct the squirrel package using functional options?
[3137.22 → 3137.66] Potentially.
[3138.92 → 3141.42] So do either of you have something you'd like to share?
[3141.78 → 3142.34] I have one.
[3142.62 → 3145.80] I think that pair programming is an unpopular opinion.
[3146.30 → 3148.58] I did it early in my career, took a lot of time off.
[3149.58 → 3151.68] A lot of companies are afraid to adopt it.
[3151.68 → 3154.64] I work for a company that I think does it really well.
[3155.00 → 3158.60] But I still think it's an unpopular opinion that pair programming, mod programming,
[3159.16 → 3162.80] I think that's the way things are going to be done if you want to be successful in the future.
[3162.80 → 3167.98] I think the closest I have is that hopefully it's not controversial here because that'd make me sad.
[3168.22 → 3175.60] But the documentation contribution is contribution that is as important and sometimes more important than just the actual code.
[3176.00 → 3178.40] And I see a lot of that where people always kind of drop the docs.
[3178.56 → 3179.72] That's the closest thing I have right now.
[3179.72 → 3181.38] But, you know, it's important.
[3181.54 → 3187.84] It builds up that how do we bring people into our circle that's building this tech and expand and then be able to build better things together.
[3188.14 → 3190.88] So hopefully not too much of a hot take here.
[3191.12 → 3192.52] But I think it is.
[3192.58 → 3193.36] I think it's a hot take.
[3193.68 → 3195.68] And yeah, let's fight the good fight.
[3195.88 → 3196.62] Keep preaching it.
[3196.62 → 3201.46] I don't know if it's an unpopular opinion, but, you know, I like short identifiers.
[3202.06 → 3202.86] I do.
[3203.34 → 3209.92] And I feel like the closer they are to where you use them, the shorter they can be.
[3210.76 → 3216.00] And the further away they are from where you use them, the longer they should be.
[3216.56 → 3224.30] And then there are some exceptions, like when an identifier is really, really, really important in your package and prevalent,
[3224.30 → 3227.82] then it can be one letter, even if it's a global.
[3228.70 → 3232.96] And, you know, the most prominent example for that is perhaps testing.t.
[3233.42 → 3235.46] I'm not sure if you're allowed to be a teacher now.
[3236.44 → 3237.08] Uh-oh.
[3237.72 → 3238.72] Why, Don?
[3239.18 → 3247.20] Every teacher, like, expects you to write really long, like, self-explanatory variable names, regardless of where you use them or when you're using them.
[3247.20 → 3248.20] At least that was my experience.
[3248.30 → 3250.42] I felt like every teacher wanted long variable names.
[3250.42 → 3263.10] So I will comment on your change list if it uses, you know, in a simple for loop, if the iteration variable is called index, I will, you know, probably comment on that.
[3263.34 → 3265.64] So, you know, call it I or J or whatever.
[3265.64 → 3270.56] Okay, I don't know if this opinion is unpopular, but I feel like I write it a lot.
[3270.74 → 3274.80] So there's certainly people who don't seem to grasp it.
[3274.88 → 3281.64] And that's that the language is not perfect, but every change to the language carries a heavy cost.
[3281.64 → 3289.96] So when you want to come and argue for why the language should be changed, and, you know, we see that a lot.
[3290.04 → 3295.00] I'd say that there's probably one a day suggestion for some way to change the Go language.
[3295.56 → 3303.64] Don't just talk about how it makes the language better, but also spend some time to talk about how it makes the language worse.
[3303.64 → 3308.72] Because there's no such thing as a 100% good change to the language.
[3308.82 → 3309.82] I shouldn't say there's no such thing.
[3309.90 → 3310.70] Maybe it's out there.
[3311.20 → 3312.68] Maybe no one has thought of it yet.
[3313.28 → 3319.88] But probably it's a good bet that all the 100% good changes to the language have already been made.
[3320.68 → 3327.92] And so when you want to change the language, spend some time to think about how it makes things worse as well as how it makes things better.
[3328.24 → 3331.62] I think I just saw you drop a metaphorical mic.
[3333.64 → 3340.26] We're going to go back now and think a lot about how generics makes things worse.
[3341.20 → 3346.90] So my unpopular opinion is that encoding JSON is fast enough.
[3348.28 → 3349.74] Oh, come on.
[3349.96 → 3350.30] Wow.
[3350.66 → 3353.16] This is the guy responsible for making it faster.
[3355.84 → 3357.52] Well, I'm going to say generally.
[3358.12 → 3361.28] Where generally means it most likely applies to you.
[3361.28 → 3368.12] But it might not apply to the one person that's doing something completely esoteric, such as handling 20 gigabytes of JSON.
[3368.64 → 3369.96] But most people don't do that.
[3370.90 → 3373.58] And kind of my point goes back to the trade-offs, right?
[3373.78 → 3379.58] Yes, if you pick another package, you can get maybe a 2x, 3x, maybe even 4x improvement.
[3379.58 → 3383.38] But is it really worth sticking with JSON at that point?
[3383.70 → 3390.94] The overlap between the people that are stuck with JSON, because they are, and the people that have to deal with a lot of data, is very small.
[3391.06 → 3396.70] Because the people that have to deal with a lot of data, they generally pick better formats that are faster to decode.
[3396.70 → 3400.06] I think that is a pretty solid argument, actually.
[3400.52 → 3402.52] Yeah, that's not unpopular with me, that one.
[3402.72 → 3403.78] I think you've nailed that.
[3404.44 → 3404.64] Yeah.
[3405.34 → 3409.56] Well, you would think that the amount of people yelling about encoding JSON being too slow would disagree.
[3410.64 → 3411.04] Sure.
[3411.98 → 3414.84] Well, but that's because we gave them the tools to benchmark things.
[3414.92 → 3416.02] I don't know what you expect.
[3416.40 → 3417.92] Of course, you're going to be moaning.
[3418.20 → 3418.94] We should take them back.
[3420.48 → 3423.52] JSON isn't always as bad as people make it out to be.
[3424.52 → 3424.92] Hmm.
[3425.26 → 3426.02] Tell me more.
[3426.02 → 3427.04] Who is he?
[3427.30 → 3428.94] Who is this Jason you talk about?
[3429.60 → 3432.10] Yeah, that Jason who gets so much flack.
[3432.24 → 3433.58] Why are you defending him all the time?
[3433.96 → 3434.22] Yeah.
[3434.36 → 3439.66] Well, I've seen a lot of people switch, in my opinion, prematurely to protobuffs in particular.
[3440.06 → 3445.20] Sometimes to thrift, where you just change from one problem to another.
[3445.20 → 3450.14] And especially, I think, for anything that is used externally to your company.
[3450.36 → 3451.88] So, for example, open source code.
[3452.24 → 3455.92] Protobuffs can get very complicated, especially if you're exposing something.
[3456.02 → 3458.76] That is going to be used across multiple languages.
[3458.76 → 3461.26] So, nice to use in Go.
[3461.76 → 3465.52] Not necessarily as nice to use in Ruby, for example, or in PHP.
[3466.14 → 3467.70] Yeah, or indeed the web browser.
[3467.94 → 3469.14] Actually, yeah.
[3469.36 → 3470.02] That's a big one.
[3470.18 → 3472.42] We did an episode on this very recently.
[3472.90 → 3474.34] We called it Encoding JSON.
[3474.34 → 3484.16] And we actually spelled the episode title using JSON to see if any podcasting technology is vulnerable to JSON injection attacks.
[3484.52 → 3487.26] So far, everything's just been fine, which is a shame.
[3488.94 → 3491.04] Jana, do you have an unpopular opinion?
[3491.40 → 3492.88] I have a controversial one.
[3492.88 → 3494.08] Oh, let's do it.
[3494.18 → 3496.10] Let me just re-record the theme tune then.
[3500.10 → 3502.04] God, that's a controversial opinion.
[3502.64 → 3506.08] I do think that I really like to Go as a language.
[3506.48 → 3512.98] You know, like the simplicity and verbosity-wise, it's just one of the best options that you have.
[3512.98 → 3520.34] But all the proto-generated artifacts is just making everything just kind of like messed up.
[3520.62 → 3528.18] Like each time I have to touch, you know, some proto-generated photos, it just doesn't look like Go anymore.
[3528.32 → 3529.72] It's like so cryptic.
[3529.82 → 3533.98] Like there's all these like types on top of the standard library I have to learn about.
[3534.56 → 3536.30] You know, proto has its own like struct.
[3536.30 → 3544.46] Like all the like, you know, mess and even like the timestamp, for example, type is like a completely different representation.
[3544.96 → 3551.98] So you basically have to adopt into that like verbose alternative universe.
[3552.64 → 3555.60] And it's just like my main pain point.
[3556.26 → 3562.28] And I've been like trying to collect all these like gotchas and tips and everything about photos for a long time.
[3562.28 → 3569.10] And I can tell you there's like at least 20 pages of me putting some tips like here and there.
[3569.18 → 3579.90] And I still need to go back to that document in reference to be able to kind of like take a look like, hey, this is what I'm supposed to do if I, you know, see a type like this, proto-generated type like this.
[3580.24 → 3583.10] And that's just like a big struggle to me.
[3583.62 → 3588.78] They've been trying to improve, you know, the generated artifacts, but it's just too late, I think.
[3588.78 → 3597.76] I don't know if it's popular or unpopular, but I think that generics in Go are a good idea.
[3598.58 → 3601.36] I would say that's unpopular with many people that I know.
[3602.18 → 3613.50] But I do think that like I gave this talk long time ago around functional programming in Go and basically why not to do it.
[3613.84 → 3616.20] And one of the biggest reasons, like there were two reasons.
[3616.20 → 3622.98] The first one is because there's no tail precursor optimization, which means that your program is actually 10 times slower just because of it.
[3623.40 → 3626.16] So that's, you know, like that's a small thing that maybe we should fix.
[3626.50 → 3633.94] But the biggest thing was the fact that if you want to do any kind of like interesting composition of types without generics, you're out of luck.
[3634.18 → 3635.18] You cannot really do it.
[3635.22 → 3636.84] You need to do empty interfaces everywhere.
[3637.50 → 3637.62] Right.
[3637.62 → 3641.02] So generics, I'm very excited about seeing them.
[3641.10 → 3643.32] Like I've been trying them and how they look.
[3643.38 → 3649.62] And now that, you know, contracts are kind of like gone or at least like they make much more sense.
[3649.68 → 3651.42] They're not as complicated as they used to be.
[3651.90 → 3653.58] I'm pretty excited about getting to use it.
[3653.70 → 3657.40] So I don't know when it's going to be released for real, but looking forward to that.
[3657.40 → 3663.50] Okay, those were your summer hits.
[3663.98 → 3667.78] I'd love to know if you find value in this style episode.
[3667.98 → 3669.84] Please leave a comment one way or the other.
[3670.20 → 3674.62] Open your show notes, click discuss on Changelog News, and let your voice be heard.
[3675.00 → 3677.12] You can also tweet at me if that's easier.
[3677.30 → 3678.68] I'm at Jared Leto.
[3678.80 → 3680.30] That's J-E-R-O-D.
[3680.86 → 3681.64] S-A-N-T-O.
[3681.64 → 3686.68] Special thanks to BMC for all the music and sounds you hear on our shows,
[3686.82 → 3691.08] especially that Johnny Portico I See Bars remix we played at the top.
[3691.32 → 3692.30] I see bars.
[3692.90 → 3693.72] 10 kilobytes.
[3694.00 → 3695.16] Pretty dope if you ask me.
[3695.90 → 3697.82] Thanks also to our longtime sponsors.
[3698.48 → 3699.42] Shout out to Vastly.
[3699.80 → 3700.94] Shout out to Linde.
[3701.24 → 3702.22] Shout out to Rollbar.
[3703.18 → 3704.38] That's all for now.
[3704.54 → 3707.12] Back to our regularly scheduled programming next week.
[3707.12 → 3711.06] The panel did a Reddit AMA, so we're answering all the community's questions.
[3711.06 → 3712.80] with a couple special guests.
[3713.34 → 3714.34] Stay tuned for that.
[3714.58 → 3715.60] We appreciate you listening.
[3716.00 → 3717.02] Talk to you again next time.
[3741.06 → 3771.04] We'll be right back.
