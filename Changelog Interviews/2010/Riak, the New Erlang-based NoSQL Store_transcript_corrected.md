[0.00 → 19.86] Welcome to the Changelog, episode 0.1.4.
[20.02 → 21.24] I'm Adam Stachowiak.
[21.48 → 22.44] And I'm Wynn Netherlands.
[22.66 → 25.94] This is the Changelog, bringing you what's fresh and new in the world of open source.
[26.22 → 28.90] We focus on the projects and people of open source.
[28.90 → 34.54] You can follow us at thechangelog.com or for a real-time view, tail.thechangelog.com.
[35.12 → 35.14] Yeah.
[35.50 → 37.40] You can also check us out at GitHub, too.
[37.52 → 41.22] We hang out on the Explore page, so GitHub.com forward slash Explore.
[41.92 → 45.58] They've got some trending repos listed there as well as some feature repos from our blog
[45.58 → 52.86] and also all the audio podcasts from 0.1 whatever all the way up to this one here.
[53.00 → 55.12] So just go ahead and go to GitHub and check it out.
[55.44 → 56.90] 14 episodes we've been on the air.
[56.96 → 57.44] Can you believe it?
[57.44 → 60.34] Yeah, it's kind of like a dynasty, isn't it?
[60.68 → 61.14] That's right.
[61.62 → 64.20] You know, and like everybody else, it seems like we're on Twitter.
[65.40 → 66.46] ChangeLog Show is our handle.
[67.04 → 70.20] And me personally, I tweet at Penguin, P-E-N-G-W-Y-N-N.
[70.42 → 70.68] Yep.
[70.76 → 72.24] I'm Adam Stack pretty much everywhere.
[72.36 → 77.14] Twitter, Facebook, Friend Feed, which was consumed by Facebook, and everywhere else.
[77.54 → 78.54] We've got a great show today.
[78.54 → 84.26] We talked with Andy Gross from Basho, the company behind ROC, another NoSQL database entry.
[84.76 → 94.16] And Sean Cribs, a freelance Ruby developer that's written a cool new Ruby library for ROC that he scooped on the show when we recorded it.
[94.16 → 97.98] And we posted that to the Changelog, and it went from – what's it at now?
[98.02 → 103.92] It's like at one watcher when we got the scoop, and I think it was up close to 100, if I'm mistaken.
[103.92 → 104.26] I don't know.
[104.36 → 108.58] It blew up like most things that get posted to the Changelog.
[108.98 → 111.14] It's the Changelog effect is what it is.
[111.32 → 111.62] Yeah.
[111.62 → 114.40] Ripple is the name of the library.
[114.92 → 116.36] It's now at 88 watchers.
[116.52 → 116.92] Oh, boy.
[117.24 → 118.62] Pretty hot on the GitHub.
[119.08 → 119.68] The GitHub.
[120.38 → 120.60] Cool.
[120.72 → 123.14] So ROC, another NoSQL database entry.
[123.96 → 125.22] Stop me if you've heard this one before.
[125.64 → 129.90] Erlang with JavaScript, JSON with a REST interface.
[130.30 → 131.22] Yeah, definitely.
[131.70 → 132.46] Sounds like?
[132.84 → 133.60] Sounds like all of them.
[134.02 → 136.12] Sounds like Couch DB especially.
[136.48 → 138.64] But they assure us that the architecture is quite different.
[138.64 → 142.18] This one's architected for scalability from the get-go.
[142.28 → 151.92] They tell us with a masterless replication scheme where all you need to know is one node of the replication network,
[152.18 → 155.26] and you can get on and get data from any of the nodes, which is pretty cool.
[156.02 → 163.64] You know, I was pondering this over the weekend, the irony that all of these NoSQL databases have JSON support in some regard,
[164.44 → 166.82] and yet in HTML5, what are we doing?
[166.90 → 167.94] We're putting SQL in the browser.
[167.94 → 168.28] Yeah, I know.
[169.10 → 170.60] Was it you that tweeted something like that?
[170.68 → 171.34] Yeah, I did.
[171.80 → 171.94] Yeah.
[172.46 → 181.74] You know what I really want is Congo or Couch or some of these other NoSQL technologies that have this rich JSON store that I can query built into my browser.
[181.90 → 182.56] Forget the SQL.
[182.74 → 185.00] You know, that's just ugly writing SQL with escaped JavaScript.
[185.80 → 190.52] I really want a hash database that I could just stash my JSON objects and search them right there in the browser.
[190.52 → 191.82] So go figure.
[191.98 → 199.44] We wait all this time to finally get database into the browser, and it's nothing we want.
[199.78 → 200.42] That's right.
[200.54 → 201.00] That's right.
[201.00 → 204.16] So they also started this off by scratching their own itch, too.
[204.16 → 213.36] They actually started this off much like Congo, where they were solving their own problem and created an enterprise version and then led the way with pushing that into open source.
[213.82 → 214.72] You know, that happens a lot.
[214.82 → 226.22] You know, with Wans troth, when he was talking about GitHub and how GitHub was a side project, and they were actually working on Tampa full-time and then figured out that what was the side project turned out to be the bigger play.
[226.22 → 230.98] It seems like oftentimes you don't know what's going to be successful when you start it.
[231.28 → 232.50] We've got a great episode today.
[232.56 → 233.14] Should we get to it?
[233.34 → 233.70] Absolutely.
[242.50 → 243.02] All right.
[243.06 → 251.72] We're joined by Andy Gross from Basho, the company behind Rock, the cool new database document store, and Sean Cribs, a freelance Ruby developer.
[251.72 → 256.84] Andy, why don't you introduce yourself, let the folks know a little bit about yourself and Basho.
[257.42 → 257.86] Hi.
[257.94 → 258.08] Yeah.
[258.20 → 259.44] I'm Andy Gross.
[259.56 → 261.52] I'm the VP of Engineering at Basho Technologies.
[262.24 → 269.30] I've been working at Basho for about two years, and it's the best gig I've ever had.
[269.36 → 270.18] We have an awesome team.
[270.52 → 280.44] I've worked with people that I've worked with in the past, and we've assembled recently an awesome group that's growing by the day.
[280.44 → 292.52] And we both produced the React open source project and offer support and an enterprise version of the same for the market.
[292.78 → 298.86] So we're trying to just drive this NoSQL thing as hard as we can.
[299.14 → 304.66] For the folks that don't know what about React and its entry into the NoSQL space?
[304.78 → 307.56] How did that come about and a little bit about the project before we introduced Sean?
[307.56 → 310.44] It's a fascinating story.
[311.78 → 318.04] We started off actually as a company that was actually producing, writing web apps.
[318.52 → 321.88] And going into it, we said we were going to plan for success.
[321.88 → 336.24] And one thing that a number of us have been burned by at previous startups is tying ourselves to a relational database and then having to change that architecture at the worst possible time, which is when you start to get popular.
[336.24 → 352.96] So one of the things we said going in, and it was awesome that we had buy-in from the other founders too, that we were going to write our own data persistence layer, which is – it can be seen as relatively controversial.
[352.96 → 360.88] So initially, React was just an internal Basho product that we used to power our applications.
[361.82 → 368.64] And it wasn't until August 2009 that we went open source.
[368.80 → 373.40] We said this NoSQL thing is really our core competency.
[373.60 → 376.64] We're a bunch of distributed systems guys.
[376.64 → 385.06] The apps worked out okay, but we thought NoSQL was a much bigger opportunity.
[385.92 → 390.04] So we spent a couple of months changing directions, getting React ready for open source.
[390.36 → 391.94] We released it in mid-August.
[392.08 → 400.60] I think – I don't remember the exact first release of React, but we're coming up on the six-month anniversary of its first open sourcing.
[400.60 → 405.42] So I think we've come an amazingly far since then.
[407.30 → 420.14] But again, it was initially an internal tool, internal data store that we implemented for the purposes of not having to be woken up at one in the morning.
[420.14 → 428.54] One anecdote that people like to tell at Basho is that one day we had two nodes die at about 11 in the evening.
[429.50 → 434.26] And the relevant people got on a call, and we knew the properties of our data store.
[434.66 → 435.48] And we said, you know what?
[435.96 → 437.98] We can leave this until the morning.
[437.98 → 451.48] And we went to sleep and fixed it the next day, which really got our minds forward-looking towards, I think, the future of this company is going to be in the NoSQL space.
[452.86 → 455.44] I've recently discovered it, and it's a very cool project.
[455.56 → 458.24] Before we get too deep into it, we should introduce Sean.
[458.50 → 461.84] And for the folks that are Ruby-as in the audience, I'm sure they know who you are.
[461.84 → 467.36] But, Sean, for the other folks out there, why don't you introduce yourself and let us know how you came across React.
[467.36 → 469.50] Sure. Hi. I'm Sean Cribs.
[470.16 → 474.32] I've been a freelance Ruby web developer since 2007.
[474.98 → 480.64] Before that, I worked for a small community college in Kansas City, also doing Ruby development there.
[482.06 → 487.30] And I got interested in React after I heard it go open source.
[487.80 → 490.94] One of my recent interests has been Erlang.
[491.12 → 495.50] And so I went to the Erlang Factory Conference last year.
[495.50 → 497.96] I guess it was end of April.
[499.04 → 501.48] And I met Justin Chee hi for the first time.
[503.14 → 505.46] Justin is the – I don't know if Andy mentioned it.
[505.54 → 507.40] He's the CTO of Basho.
[507.96 → 512.78] And he was talking about Web Machine, which is another one of Basho's open source projects.
[512.78 → 520.88] But it turned out that they released their – as Andy said, their React in August.
[521.00 → 524.20] I was like, hmm, so this is what they're using Web Machine for.
[525.06 → 531.34] And then I got the chance to go to NoSQL East and talk to the whole team a bit more about it.
[531.34 → 544.60] And I've been really interested in the NoSQL movement since I first heard about it because, as most Ruby web developers discover with their active record projects,
[544.80 → 551.98] that there are just certain edge cases that make working with an SQL database really difficult.
[551.98 → 560.66] Times when you want to have pieces of your data that are completely dependent on one another.
[562.36 → 564.44] And when you get your database huge.
[564.68 → 567.98] Those are the two things that I find that people run into.
[567.98 → 583.22] And so in addition to just being kind of tangentially interested in React for personal reasons, I got contracted in January.
[583.58 → 587.46] I started working on this contract or arranging this contract in December.
[587.46 → 597.58] But I got contracted in January to build a Ruby library, so the client could move their Rails app off of MySQL onto React.
[597.98 → 599.40] So that's interesting.
[599.54 → 605.84] The growing crowd of NoSQL databases is just getting bigger every day.
[606.02 → 607.74] So is this a fad?
[607.82 → 608.48] Is this a trend?
[608.56 → 613.12] Is this a replacement for traditional relational database architecture?
[613.12 → 615.54] Or is it just a complement to that architecture?
[616.36 → 620.84] I think currently it's going to have to be complementary for the time being.
[620.84 → 631.58] However, unlike other types of databases that have been fads or just ill-conceived, in my opinion, like XML databases,
[632.22 → 642.80] you've seen some of the seminal NoSQL projects arise out of necessity as internal projects that companies like, well, Basho,
[643.26 → 648.78] but also Facebook and LinkedIn with Cassandra and Voldemort, respectively.
[648.78 → 657.88] And that indicates to me that solving a real problem that people have.
[658.24 → 660.86] I don't think anyone ever asked for an XML database.
[661.52 → 672.46] But when you see companies actually implementing their own data stores that are so fundamentally different but so relevant to the problems that modern web apps face at scale,
[672.46 → 679.92] that's indicative of something that's not a fad and actually a market need.
[679.92 → 682.06] So a question from Twitter already.
[682.34 → 688.50] Jake Don asks, what makes React different from the other players in the space?
[690.56 → 693.14] Yeah, I'll try to condense it.
[693.76 → 696.58] React is fundamentally distributed from the start.
[696.58 → 707.50] Our philosophy on how we proceeded in developing it was to get the distributed systems fundamentals down early.
[707.50 → 719.66] I've seen in other projects shortcuts that have been taken with regard to proper distributed systems theory made early on,
[719.66 → 724.54] and then people realize there's a need to say implement vector clocks,
[725.12 → 731.96] which are logical, non-physical timestamps, and eliminate the need for all your servers to be perfectly time-synced.
[732.38 → 736.68] And it's really hard to get that stuff, to retrofit that stuff onto a store,
[737.16 → 741.88] onto a data store that you've made compromises on with regard to those things earlier.
[741.88 → 746.46] So React is fundamentally distributed.
[746.94 → 748.74] It works fine on a single node.
[748.84 → 750.90] It scales down excellently.
[751.38 → 757.02] When we were developing applications, every developer on their MacBook had the entire stack running,
[757.56 → 762.36] including four React nodes operating just as they would in production.
[762.96 → 766.30] It also scales up to hundreds of nodes just as easily.
[766.30 → 775.24] So that's where I see – that's one of the primary key differentiators of React.
[775.50 → 781.84] We were very deliberate about getting the fundamentals right first.
[783.14 → 788.50] And more recently, we've been tackling – now that we have that done,
[788.50 → 797.40] we've been tackling making it easy to use and not something that's perceived as a complicated,
[799.48 → 801.04] hard-to-use piece of software.
[801.88 → 808.16] And I think that was the right path to take because now I'm very confident in the core of React,
[808.36 → 814.34] and we can start delivering features like things that Sean has been working on
[814.34 → 817.60] and some of the more recent features in the latest releases of React,
[818.02 → 823.86] like JavaScript-based Map Reduce and some of the other things in the pipeline that I'm sure we'll get to later.
[824.50 → 826.86] Could you talk for a moment about the language breakdown?
[827.42 → 828.60] What's the core technology?
[828.72 → 831.44] I understand Erlang is at the centre of this.
[831.70 → 833.84] So what's the architecture?
[834.76 → 836.98] So React is mostly written in Erlang.
[836.98 → 842.36] I caught the Erlang bug while I was working at Apple,
[842.56 → 849.04] working on asynchronous high-throughput, low-latency systems,
[849.64 → 853.94] trying to do that in Twisted Python and then in C++
[853.94 → 861.82] and basically wanting to scream because of that.
[861.82 → 870.02] And Bob Impolite, who I then went to work for at Loki Media,
[870.58 → 872.54] had turned me on to Erlang.
[873.24 → 877.96] And it was just a dream come true for me to be able to work in that environment.
[878.12 → 881.34] It's extremely powerful, extremely proven,
[881.34 → 895.32] and has been used and proven to provide uptimes greater than any other measured language or product out there.
[895.98 → 902.24] So the core distributed system, the core React code is mostly Erlang.
[903.70 → 905.94] We do have extensions.
[905.94 → 911.24] The storage layer, we have pluggable storage.
[911.34 → 915.90] Our preferred storage layer is In-store, which is another Basho open-source project.
[916.16 → 922.38] That is an Erlang wrapper around embedded InnoDB.
[923.34 → 930.62] And our JavaScript support is Mozilla's Spider Monkey, which is written in C.
[930.62 → 941.78] And we use Erlang's interfacing foreign function interface capabilities to talk back and forth between those subsystems.
[942.24 → 945.18] But the core is in Erlang.
[945.72 → 949.76] So I guess you mentioned Erlang, JSON, REST.
[950.72 → 952.20] Do you have people stop you right there?
[952.52 → 957.34] And do you have the reaction to have to draw some sort of distinction to Couch at that point?
[957.34 → 960.92] Yeah, I think Couch is a great project.
[961.12 → 971.20] And Couch really got out there early and really got people aware of NoSQL in general and just, you know,
[971.26 → 973.36] hey, there's a new way of doing this type of thing.
[973.36 → 987.66] I would say our primary difference with Couch is in what I was talking about before is that Couch is, you know, really at its core a single-node system.
[987.78 → 988.66] They support replication.
[989.92 → 997.36] But Couch databases are, you know, single-node concepts.
[997.36 → 1009.78] ROC has the node – ROC, even if you're running it on a single node, the lower-level abstractions are dealing with consistent hashing and virtual nodes.
[1010.40 → 1015.06] And when you add a second node, things don't change.
[1015.30 → 1019.10] And it's not – you don't have to point your database at another node to replicate to.
[1019.74 → 1023.38] You just add a node and the data distributes itself in the background.
[1023.38 → 1035.04] Contrast this to sharding, which is, in my opinion, you know, of all the things to bring forward from the relational era,
[1035.54 → 1042.02] one of the last things I'd choose to bring forward because sharding is fragile.
[1042.02 → 1052.24] When you're spreading your data around across many machines, you increase, you know, just the meantime between failure of hardware,
[1052.88 → 1058.38] you're getting much – you know, you're getting yourself into a trap where it's much more likely you're going to lose a bunch of data.
[1058.38 → 1070.30] ROC, on the other hand, does – provide you with all the benefits of sharding without exposing both the operational pain of having to deal with a setup like that
[1070.30 → 1074.34] and, you know, its inherent fragility.
[1075.38 → 1083.08] ROC, you basically tell it, look, I want each piece of data to be replicated on this many nodes, and ROC takes care of it.
[1083.08 → 1093.28] So when you add nodes, you add throughput, you add storage capacity in a roughly linear fashion,
[1094.24 → 1103.00] and just as importantly, without any additional operational pain like adding shards causes.
[1103.52 → 1106.30] So the concepts of master-slave really don't exist with ROC?
[1106.30 → 1112.76] No, not at all. It's fundamentally just distributed. No node is special in a ROC cluster.
[1112.96 → 1119.52] There's no central point of failure, nor is there a central point of sort of need for operational attention.
[1119.78 → 1122.66] Every node is homogenous. They're all the same.
[1123.44 → 1127.28] If they disappear, your app's not going to go down.
[1127.92 → 1133.24] If a shard disappears, whatever range of data that shard has is going to go with it,
[1133.24 → 1135.32] and you better have had a backup of it.
[1136.26 → 1146.26] With ROC, just the sort of core distributed functionality ensures that your data is going to remain available
[1146.26 → 1149.68] when you add or remove nodes from a cluster.
[1150.24 → 1153.94] Yeah, that has interesting ramifications for peer-to-peer type applications.
[1154.08 → 1157.60] If you only need to know one node to connect to, it kind of changes things.
[1157.96 → 1158.74] Yeah, it's true.
[1158.74 → 1166.96] The calculation of where a piece of data should be written to or read from is a function that can be executed
[1166.96 → 1172.16] strictly based on local data to any individual node, and this is consistent hashing.
[1172.32 → 1178.94] This is the technology that Akamai really introduced into the web caching world,
[1179.48 → 1182.56] and we've applied it here to databases.
[1182.76 → 1184.92] Akamai never wanted to tackle the database problem,
[1184.92 → 1187.30] which is something that frustrated me while I worked there.
[1188.38 → 1196.98] But consistent hashing is – and sometimes it's hard to – the differences are subtle and there are nuances here.
[1197.62 → 1205.82] So sometimes I've explained consistent hashing as sort of dynamic, optimal sharding or some combination of words like that.
[1205.82 → 1215.16] But what it really is handling the problem of ensuring that you have replicas of data,
[1215.88 → 1221.68] both replicas of data and spread of data, which is what sharding provides,
[1223.28 → 1230.60] at a much lower layer that isn't exposed to your application or to your operations personnel.
[1230.60 → 1234.86] You know, another powerful feature of React is the notion of link walking,
[1235.02 → 1240.40] and one of the better explanations I've seen is up in your blog, Sean, seancribs.com, with two Bs.
[1241.18 → 1245.26] Why don't you give the folks an overview of link walking and why it's so powerful?
[1246.54 → 1246.76] Right.
[1247.02 → 1252.24] So every object that you store in React has a bunch of metadata associated with it,
[1252.84 → 1257.36] and one of those pieces of metadata is the links.
[1257.36 → 1265.66] So there's an IETF working draft, I believe, or proposal about an HTTP header called link.
[1266.46 → 1273.80] And basically it kind of looks like what you might see on a content type header or any of the other HTTP headers,
[1274.06 → 1281.08] except that it has a link to some other location and then various attributes that are attached to it.
[1281.08 → 1288.20] So React lets you make one-way associations to other pieces of data.
[1289.48 → 1296.28] So let's say I had my own, we're building like a social network, a quintessential example,
[1296.88 → 1303.10] and my record in there has a link to Win and to Andy and to Adam.
[1303.10 → 1312.02] And then if I wanted to see who my friends are, say I tag that link with friend as the tag,
[1312.64 → 1321.84] I could just construct a URL and get at that URL beginning with my user record and then the link spec, we call it,
[1321.90 → 1327.68] which is better described on my blog than I can do in person without a whiteboard.
[1327.68 → 1335.14] But you would tell it, follow, get my friends, and React will go out, find the user record,
[1335.56 → 1341.24] and then follow those links and return all the people who are my friends, all the records like that.
[1341.92 → 1348.44] So that's just a fundamental different way of handling, I guess, joints, what we call joints in the relational world, right?
[1349.02 → 1349.42] Right.
[1349.42 → 1356.82] Well, it's actually more useful to think of it like a graph database, which has nodes and edges.
[1357.48 → 1364.52] Or another analogy that I like to use is building data structures in C.
[1365.12 → 1368.94] With data structures in C, you build like a struct, which has some pointers,
[1369.34 → 1372.50] and those pointers point to other places in memory.
[1372.50 → 1380.72] This is a bit more analogous to the C way of building data structures in that it's just a pointer.
[1381.50 → 1385.08] And you can follow that pointer with very little cost.
[1385.82 → 1390.82] Another, I guess, fundamental difference between React and some of the other players is the way it handles Map Reduce
[1390.82 → 1397.18] and the way that it expects a set of keys to be passed into the map function before it's run.
[1397.18 → 1402.72] Talk a little bit about that, Andy, and why that architecture and what makes that different and powerful.
[1403.64 → 1407.92] Yeah, it makes it powerful, and it's very deliberate the way we chose that.
[1409.30 → 1415.58] Right now, we're not trying to compete with Hadoop in terms of being a Map Reduce engine.
[1416.12 → 1421.30] Map Reduce here, we're trying to expose as a query mechanism, basically,
[1421.52 → 1424.28] that you can have in the request loop of your application.
[1424.28 → 1433.50] And Sean really led into this with the fact that the way web applications are structured nowadays,
[1433.50 → 1440.20] you tend to start with a root object, like a user, and you can fan out from there to their friends,
[1440.48 → 1446.36] their blog posts, their comments, whatever other sort of domain objects that you have.
[1446.36 → 1459.54] And throughout the course of a web session, you'll know the keys ahead of time that you want to perform an operation on.
[1460.28 → 1465.22] And this is getting back a little bit to the consistent hashing stuff I was talking about before.
[1465.90 → 1475.14] Given a bucket and key in React, any node can determine what node that data lives on.
[1475.14 → 1483.66] So we can farm out and distribute the computation and move basically the computation to the data,
[1484.36 → 1488.26] rather than having to move the data to where the function is executing.
[1488.26 → 1495.92] So it's quite efficient and therefore very suitable for an actual query mechanism,
[1496.24 → 1503.18] as opposed to the Hadoop use case, which is typically offline log processing.
[1503.32 → 1510.38] I don't know of many apps with Hadoop somehow integrated into the actual real-time request cycle of their applications.
[1510.38 → 1518.74] You know, I've been developing web applications, I guess, 10 years or so, maybe a little longer than that now.
[1519.38 → 1523.74] And something that strikes me, you know, the queries are represented in JSON.
[1524.30 → 1528.06] And so, you know, early on in web development, we had server technologies,
[1528.06 → 1531.94] and we found ourselves writing JavaScript to go against the DOM,
[1531.94 → 1535.60] but a lot of that JavaScript was dynamic and generated from server code.
[1536.10 → 1539.86] And so now we're passing queries to a lot of these data stores,
[1540.02 → 1542.96] React being one of them that uses JSON under the hood,
[1543.50 → 1548.64] where we express things like Map Reduce inside of JavaScript functions inside a JSON object that's passed back.
[1548.78 → 1551.18] But, Sean, let me ask you, as a Rubbish, right,
[1551.42 → 1554.96] right now I'm sure that you're writing a lot of this JSON by hand
[1554.96 → 1557.78] as these libraries are just starting to evolve.
[1557.98 → 1559.60] But, you know, where do you see that going?
[1559.70 → 1563.60] And are we going back to straddling two languages to do one task?
[1563.60 → 1568.58] Well, I think that most, at least for most Subsists,
[1568.84 → 1573.38] if they're doing Rails or Mere or Sinatra apps,
[1573.98 → 1576.44] they're already familiar with JavaScript.
[1577.60 → 1583.80] And I think that there's a great respect from Rubbish toward JavaScript,
[1583.80 → 1585.42] and its capabilities.
[1587.40 → 1589.84] There is that cognitive disconnect,
[1590.10 → 1593.28] but I think that web developers are the type of people
[1593.28 → 1595.90] who work in many domains at once anyway.
[1596.88 → 1599.54] And having the Map Reduce be in JavaScript,
[1599.76 → 1601.96] which is something familiar to most web developers,
[1602.16 → 1604.52] I think is more of an advantage than a drawback.
[1604.94 → 1606.48] I just wanted to add a little bit to that.
[1606.82 → 1609.58] And then this kind of struck me, too.
[1609.66 → 1612.10] I haven't been a web developer for most of my career.
[1612.10 → 1617.46] I was a web developer back in the days when JavaScript was sort of a hack
[1617.46 → 1619.60] to do browser detection and other things.
[1619.72 → 1624.38] And it's really turned into a nice sort of little language
[1624.38 → 1630.24] that is able to express these types of operations.
[1630.24 → 1636.20] And it also is, you know, everybody kind of knows at least a little bit of JavaScript.
[1637.60 → 1647.92] So it neatly bypasses what could be a difficult choice of what dynamic language VM
[1647.92 → 1652.88] you choose to implement inside the core of your data store.
[1652.88 → 1657.34] You know, you see Google App Engine, they're rolling out support for various languages.
[1657.82 → 1662.84] And I think they're leveraging the JVM and its support for compiling those languages
[1662.84 → 1664.60] down to Java to a large degree.
[1664.60 → 1672.00] But I think JavaScript is really, you know, a net win.
[1672.10 → 1672.74] It's easy to learn.
[1672.86 → 1673.36] It's simple.
[1674.14 → 1679.40] It doesn't have a lot of real rough edges, especially when you're dealing with it in a non-DOM,
[1679.50 → 1682.58] when you're not talking about the DOM manipulation aspects of it.
[1682.58 → 1684.20] It's expressive.
[1684.40 → 1684.76] It's clear.
[1684.94 → 1685.48] It's concise.
[1686.66 → 1694.68] And I think it's absolutely the right choice for, you know, the React not produced feature
[1694.68 → 1695.94] that we're talking about.
[1696.38 → 1698.48] Well, Sean, you mentioned the cognitive disconnect there.
[1698.60 → 1701.02] You know, I'll ask that Adam's dying to ask.
[1701.16 → 1705.66] And he wants to keep our streak alive about discussing Node.js on this show.
[1706.10 → 1708.86] So how does this play nice with Node.js?
[1709.14 → 1711.02] And would it be easier just to keep everything in JavaScript?
[1711.02 → 1716.16] Well, it would play absolutely nicely with Node.js.
[1716.32 → 1724.52] In fact, if I remember right, there was a recent client written for Node.js using Node.js's
[1724.52 → 1728.50] built-in HTTP for React.
[1729.32 → 1732.52] And I just think I saw that flying by in the GitHub feed the other day.
[1733.84 → 1740.48] But on the other hand, you know, Couch DB has had this concept of a Couch app for a while,
[1740.48 → 1746.70] which is basically you just store a bunch of JavaScript and other files in Couch DB,
[1746.94 → 1752.30] and you can serve that out as an application because Couch DB has an HTTP server in it.
[1752.54 → 1755.80] Well, there's honestly no reason why you couldn't do that with React, too.
[1755.80 → 1763.92] One of the advantages of the raw interface, which is what I've been writing my Ruby code against,
[1764.56 → 1767.22] is you can store any content type that you want in React.
[1768.36 → 1771.18] So it basically acts like an HTTP server.
[1771.98 → 1778.34] And there's also already in the client libraries for React that comes in the main distribution,
[1778.34 → 1784.24] a very basic sort of jQuery-is client for React.
[1784.72 → 1787.12] Looks like we've got some questions rolling in on Twitter.
[1787.48 → 1788.10] Adam, you want to?
[1788.34 → 1789.06] The Twitter.
[1789.48 → 1790.94] The Twitter, as I call it.
[1791.18 → 1795.84] Yeah, I've done this entire podcast without saying one where I was trying to get to like minute 44,
[1796.00 → 1797.72] but we're like seven seconds away, so.
[1798.48 → 1800.92] Well, normally you jump in so late, I feel like we have to introduce you.
[1801.06 → 1802.06] This is my co-host, Adam.
[1802.36 → 1803.54] Yeah, hey, this is Adam.
[1803.54 → 1808.10] Well, there are a few questions on Twitter, but I think I have a more pressing question,
[1808.34 → 1812.66] and it's kind of funny we got so far into the podcast and really haven't talked about it, but, you know.
[1812.72 → 1813.14] Sorry, tweets.
[1813.98 → 1818.92] We have this company called Basho that was formed, and, you know, you guys have this product,
[1819.06 → 1821.62] but it's open source, it's commercial.
[1822.18 → 1823.20] How did that story come about?
[1823.28 → 1827.72] Like, when the company formed, how did you initially like plan revenue and the formation,
[1827.94 → 1829.54] and was it all joined around this product?
[1829.54 → 1834.70] Well, when the company formed, we were doing an entirely different business.
[1834.92 → 1842.80] We were actually writing applications that are relatively uninteresting in the context of this podcast,
[1843.34 → 1847.30] but we chose – we implemented React as a strictly internal project,
[1847.30 → 1852.82] so we wouldn't have to deal with, you know, scaling issues later on.
[1852.82 → 1862.42] But it was always a dream of mine that one day we'd be able to, you know, release React as open source.
[1864.00 → 1871.22] And when NoSQL started to really gain steam, we sort of, you know, weighed our options,
[1871.60 → 1878.56] and we ditched the app business, and we went – you know, we really just sort of leaned into it
[1878.56 → 1881.00] as far as the NoSQL stuff goes.
[1882.44 → 1888.90] And Basho, as a corporate entity, we are extremely devoted to open source.
[1889.26 → 1898.60] We have an enterprise product that provides things like wide area, multi-master replication,
[1899.62 → 1907.00] enhanced SNMP monitoring, web UI tools, things that are valuable to enterprises.
[1907.00 → 1917.94] But we really try to err on the side of putting as much stuff and – as much value into the open source project as possible.
[1918.70 → 1927.68] So, you know, Basho as a company, what I think is nice about Basho is that, you know,
[1927.68 → 1933.64] as a customer of Basho, you, you know, A, you get access to our enterprise features.
[1934.02 → 1938.94] You get input and voting rights onto – into, you know, our product roadmap.
[1939.68 → 1949.02] NoSQL being relatively new and no deployment of NoSQL at scale being, you know, the same.
[1949.46 → 1955.04] You get, you know, pretty, you know, basically direct access to the developer team
[1955.04 → 1960.46] in terms of, you know, getting your implementation right from the ground up.
[1962.38 → 1968.38] And, you know, we – but primarily, you know, we are an open source software company.
[1968.72 → 1970.16] We have an enterprise product.
[1970.40 → 1976.80] You know, obviously we have to make money and we have very valuable enterprise features.
[1976.80 → 1985.82] But we realize that, you know, there are a few NoSQL or NoSQL-like databases that are closed source.
[1986.00 → 1987.40] And I just don't think that's viable.
[1988.50 → 1998.06] The way that Basho is going to succeed is by being a responsible and effective open source company
[1998.06 → 2002.20] and nurturing, you know, a community.
[2003.14 → 2008.90] And we've already reaped many rewards on that and, you know,
[2008.96 → 2013.24] couldn't be more thrilled with the attention that React has gotten
[2013.24 → 2016.96] even only six months after its initial release.
[2017.62 → 2020.90] There's already a ton of community interest.
[2022.64 → 2024.88] I was going to ask you, what's your user base like?
[2024.88 → 2028.86] We have, you know, we have customers.
[2029.84 → 2034.10] I can talk about a couple of them, or I can talk about one of them at least without –
[2034.10 → 2037.38] I'm just curious, like numbers-wise, like how many – do you know what your community is?
[2037.46 → 2040.02] Like actual usage, like both enterprise and open source?
[2040.68 → 2041.04] Yeah.
[2041.38 → 2049.76] We have, you know, more enterprise customers than you could count on your hands.
[2050.20 → 2051.02] I can say that.
[2051.72 → 2051.88] And we have –
[2051.88 → 2052.24] So, a level.
[2052.24 → 2052.72] Yeah.
[2053.20 → 2053.48] Yeah.
[2053.72 → 2054.86] And we –
[2054.86 → 2056.42] Just teasing you.
[2056.86 → 2057.10] Yeah.
[2057.90 → 2063.58] And a really active and growing every day, you know, React users mailing list
[2063.58 → 2067.18] and we try to be right out there on Twitter talking about stuff.
[2067.18 → 2075.16] We have a couple deployments that are a pretty big deal.
[2075.34 → 2087.42] Loki Media uses us in a couple of really critical applications, and they get, you know, a ton of traffic.
[2087.42 → 2100.00] The one I'm most familiar with is all their session management is done through React and that's something that gets, you know, I don't know the exact numbers.
[2100.34 → 2108.86] So, one I'm comfortable saying right now would be, you know, millions of hits a day, hundreds of requests a second.
[2108.86 → 2109.50] Awesome.
[2109.50 → 2114.78] So, and, you know, that's on sort of the startup side.
[2114.92 → 2117.04] We've also gotten interest across the board.
[2117.04 → 2139.68] I mean there's – I've been surprised throughout this process how forward-looking some companies you'd think would be still stuck in the, you know, Java, Hibernate, Oracle realm of failure that are willing to actually embrace these technologies.
[2139.68 → 2145.14] So, we're in some trials with some pretty big names that we hope to announce soon.
[2146.90 → 2152.66] But it's really – I feel it's taking off and this is not just a Basho thing.
[2152.76 → 2166.78] I think this is great for the entire community, and it's a young community and I think that at this stage, you know, successes for any company are great for everyone.
[2166.78 → 2189.86] You know, successes customer-wise, successes funding-wise, I'm always happy to see any company in this area succeed because I think it's important, and I think it can really change the shape of how people build applications, whether it's web startups or, you know, big enterprises.
[2189.86 → 2202.98] Right. So, how does – my question I have is how does the product being open source – how does that – does it allow for greater adoption of the enterprise version?
[2203.14 → 2209.04] Do they play together or does it – how does the relationship between open source and enterprise kind of play out?
[2209.04 → 2218.22] So, I mean, the enterprise version is basically open source React with some add-on applications like I talked about before.
[2219.02 → 2230.50] The way we've gotten a lot of the customers we have currently are people download the open source version, do a shootout with us versus Couch or Congo or Cassandra or whatever,
[2230.50 → 2237.04] and then approach us saying, hey, we like you, let's try the enterprise bits now.
[2237.04 → 2250.76] I think without that open source component, we'd be at a real loss and a strategic disadvantage with respect to the whole market and the opportunities that are there.
[2250.76 → 2263.96] So, and we try to err very strongly on the side of, you know, if there's a question about whether a feature should be held back or open source, my argument is always let's open source it.
[2266.60 → 2272.82] So, you know, we spend a lot of work on – and this is largely Dave Smith's work.
[2272.82 → 2281.16] I would love to shout out every single Basho developer here because they're an amazing team, the best team I've worked with across all the companies I've been at.
[2281.42 → 2285.56] But we're growing so fast that I couldn't name them all probably right now.
[2287.82 → 2302.62] But Dave Smith, Dizzy Co on Twitter has done an amazing job of taking embedded InnoDB, which, you know, has been proven – you know if you think the LAM stack has been successful, right?
[2302.62 → 2307.00] You know, that's my SQL right there and to a large part InnoDB.
[2307.98 → 2316.98] So we've taken InnoDB and wrapped it up in Erlang, and we use that as, you know, pretty much our recommended store.
[2317.36 → 2322.32] There's a relatively simple API for which anybody can write a back end for.
[2322.52 → 2327.32] People have written back ends that store React data in Regis, which I think is really cool.
[2327.52 → 2328.70] I'm a big fan of Regis.
[2328.70 → 2332.02] You could store it in S3.
[2332.42 → 2340.84] You have to implement, you know, less than five methods to be a fully functional React back end.
[2343.04 → 2354.34] So open source is – I can't overstate how central it is to both our, you know, vision and our success.
[2354.34 → 2372.66] Do you ever see it – we're stemming off the vein here, but do you ever see the enterprise version kind of going away and you guys just sort of take over support for large implementations and maybe consulting and training and stuff like that and go straight open source?
[2372.74 → 2375.84] Or is it always going to have this enterprise vein to the product?
[2375.84 → 2377.84] That's a good question.
[2378.02 → 2380.04] You know, I'm not the biz dev guy.
[2380.28 → 2384.46] If you were to ask me my honest opinion on most of these questions, I'd default to open source.
[2384.60 → 2391.00] But we have to make, you know, we have to make money to keep putting great stuff into open source.
[2391.44 → 2395.22] The current plan is to continue with the enterprise features.
[2395.22 → 2405.60] However, and I sometimes refer to this as the sleepy cat model, sleepy cat being the ones who wrote Berkeley DB and were later acquired by Oracle.
[2406.46 → 2411.78] And, you know, version one of an enterprise feature will be a holdback for a little while.
[2412.36 → 2415.50] And then when we write version two, we put version one out in open source.
[2415.50 → 2423.90] And, you know, if we can't come up with something more compelling in a year, then we failed.
[2424.54 → 2437.32] So, you know, while we do have things that are held back, the goal is to gradually, you know, release those features back into the open source.
[2438.00 → 2440.44] So, you know, we're committed to open source.
[2440.86 → 2441.58] Well, you have to make money.
[2441.58 → 2445.82] I mean, I know that you guys are committed to open source, but you do have to make some money.
[2446.08 → 2448.66] But we have a couple more questions from our Twitter audience.
[2449.02 → 2452.02] And the first question comes from Bradford W.
[2452.44 → 2456.44] And he wants to know about Search and how React is going to plan a search.
[2457.40 → 2459.26] Search, that's a great question.
[2459.42 → 2463.44] Search is a product that is in beta testing with a couple of customers.
[2463.70 → 2466.72] Collect is the one that we've announced.
[2466.72 → 2483.00] First, we, React, when you see people about, you see people talking about NoSQL and a phrase I've often seen thrown out is, oh, it would be awesome to throw a consistent hashing layer.
[2483.64 → 2489.46] And I'm using finger quotes there on top of this, you know, name your single node system here.
[2490.08 → 2491.66] Tokyo Tyrant, Regis or whatever.
[2491.80 → 2492.74] And it will perform awesome.
[2492.74 → 2503.80] It's hard to, it's easy to underestimate how much work writing that consistent hashing layer is.
[2504.46 → 2509.04] And React, however, is basically a consistent hashing layer.
[2509.18 → 2515.74] Since we have pluggable storage backends and a bunch of other pluggable hooks in terms of how data is partitioned,
[2515.74 → 2527.46] React search is basically using React as a consistent hashing layer around what I can best describe as, you know, what solar is in a single node.
[2527.46 → 2539.36] So the React search product is, has the same properties of React in that you can add a node and the data gets spread across it in the search case.
[2539.46 → 2546.12] You know, you were talking about search indices get spread across it, has the same basic scaling properties as React,
[2546.98 → 2556.10] but provides a solar compatible interface to that data.
[2556.10 → 2569.36] So it's, it's really just, you know, take React in its current use as a key value store and, and use that to solve a search problem.
[2571.06 → 2574.02] And we're having great success with that.
[2574.20 → 2576.22] React search is currently in limited beta.
[2576.54 → 2577.80] We're a growing company.
[2577.80 → 2591.46] We don't want to, you know, over, we don't want to, it's in beta because we don't want to release it and not be able to support people on it effectively.
[2591.74 → 2599.26] We are, we're very conscious of, of what our, our capacity is in our support pipeline.
[2599.26 → 2605.48] But most of React search will be in the open source version of React.
[2606.06 → 2620.84] The enterprise holdbacks for React search are probably, probably going to be focused around API compatibility with existing search products like Lucene and solar and being able to import your solar schemas into React.
[2620.84 → 2630.22] But that is another very exciting internal project that, that will come out of beta soon.
[2630.30 → 2638.42] And I've seen people clamouring for it on Twitter and, and it will be out, and it will be huge.
[2639.58 → 2644.46] Speaking of clamouring on Twitter, this is one of the most active talk back channels we've had on an episode.
[2644.60 → 2646.08] It must be the hour that we're recording it.
[2646.08 → 2650.86] So, uh, question for you, Sean, you mentioned earlier the different content types in React.
[2651.12 → 2660.92] And, um, the, uh, the question from Alexander Similar is, and he draws a comparison to MongoDB's Bison and its four megabyte max width.
[2661.24 → 2665.98] You know, how does React handle binary and are there any limitations on content size?
[2666.14 → 2671.96] Right now there's like, and this is just from what I understand, a small limitation of, um,
[2671.96 → 2676.96] the HTTP layer that's on top of, of the, the data store part of React.
[2677.22 → 2679.78] But, um, there's a, a size limitation.
[2680.52 → 2684.40] However, um, there's no content type limitation.
[2685.06 → 2690.06] So React just, um, Erlang has this concept of binaries, which are basically bit strings.
[2690.72 → 2697.60] Um, and, uh, once it gets into React, it just says, okay, this is, you know, this is binary data.
[2697.60 → 2701.98] So I'm just going to ship it out into the cluster and replicate and do all those great things that React does.
[2702.66 → 2706.06] Um, so there's no, there's really no restriction.
[2706.36 → 2711.82] You just have to specify the content type when you do the put or post request to React.
[2712.46 → 2719.20] Um, so, I mean, there's no reason why you couldn't store an image or an audio file or a video.
[2719.20 → 2729.14] Um, and, you know, serve that out, uh, as part of your application or, uh, use it to, uh, you know, like a global file system.
[2729.68 → 2734.32] Yeah, it, it, it's really a minor limitation and, and just something we really have to get to.
[2734.58 → 2743.06] Uh, what I've actually been working on to address this is, uh, an abstraction, uh, between the web interface and the backend storage layer
[2743.06 → 2748.86] that represents a stream of data such that we don't have to accept an entire body.
[2749.54 → 2757.46] You know, obviously you're not going to fit a DVD in memory on your average computer, which is, you know, what a standard web server is going to want to do.
[2758.00 → 2769.36] Uh, it's not a, uh, a huge amount of work to expose, uh, streaming storage abstractions such that you could upload, you know, via HTTP, uh,
[2769.36 → 2774.28] and chunked encoding, uh, a very large binary and have us store it as an object.
[2774.28 → 2777.46] And, you know, it's something I expect we'll implement pretty soon now.
[2779.16 → 2784.30] Alexander also has a, uh, a follow-up question for, uh, whoever wants to answer this one.
[2784.56 → 2789.82] Uh, can you save map reduce output somewhere, and can you update output with Delta from the last execution?
[2792.34 → 2793.72] I, I could take that one.
[2793.86 → 2799.34] The, um, you know, you get the map reduce output back as, uh,
[2799.36 → 2805.12] Um, you know, if you're doing it from the Erlang interface, uh, you get it back as Erlang terms.
[2805.30 → 2816.90] If you're doing it over HTTP, you get it back as JSON and there's nothing stopping you from going and saving that back as another React object, uh, to sort of cache that map reduces execution.
[2817.40 → 2828.18] Uh, we also, uh, at, uh, you know, low level layer, you know, for any given map reduce function and a data and, and that functions arguments,
[2828.18 → 2832.86] we, assuming the function doesn't change, we cache those results.
[2833.00 → 2842.56] So if you're doing, dealing with stuff like time series data, you may run a relatively long-running query that, that aggregates, say, an hour's worth of data.
[2842.82 → 2851.08] But then if you want to do another incremental map reduce over that for the next minute's data, you're going to hit the cache for everything but that last minute.
[2851.08 → 2867.46] Um, so we do, we do caching of, um, of map reduce results, caching of map reduce functions, um, and have plans in the pipeline for, uh, making that cache even more, uh, intelligent and useful.
[2867.46 → 2883.96] Uh, another thing that's related to this, and this is a, uh, a common dig against NoSQL DBs, especially the key value oriented ones is, uh, you essentially need to know the key, uh, if you want to access the data.
[2883.96 → 2904.98] Uh, now that we have JavaScript, uh, uh, integration, what we're likely to add in the very near future is something along the lines of, uh, GASP, you know, here's something from SQL land, uh, a trigger or stored procedure that basically says, you know, when you put an object into this bucket, run this JavaScript.
[2904.98 → 2920.90] And what that JavaScript function can do is essentially do, uh, like what Couch DB does with incrementally updating views, uh, but it can also do, you know, arbitrary computation, um, uh, besides that.
[2921.10 → 2930.94] So I think, uh, and this is, this comes back to one of my points about, you know, uh, making, you know, planning for success and having that be easy.
[2930.94 → 2934.94] Uh, people knock NoSQL out.
[2934.98 → 2941.34] Uh, people knock NoSQL value stores for lack of queryability, um, uh, especially the distributed ones because that becomes a harder problem.
[2941.34 → 2960.60] Uh, we definitely plan on adding some sort of secondary indexing capability through, uh, or implemented as, uh, some sort of post commit hook, uh, that gets executed, uh, a JavaScript function that gets executed every time you put an object into a bucket.
[2960.60 → 2963.22] So you can have views that index adjacent document.
[2963.22 → 2972.00] Uh, obviously you can get it by its key and its ID, but you can, you can, uh, index it on a secondary property as well.
[2972.00 → 2980.92] And I, I might also add that, um, because you're not, you know, you're not chained to the idea of an auto incrementing ID.
[2981.48 → 2984.52] Um, you're not chained to the idea of foreign keys.
[2984.52 → 2997.46] Um, you have the freedom to pick useful keys, um, as well as, you know, if you really, really need that extra speed, um, that React's not providing, you can create your own kind of pseudo index in another bucket.
[2997.46 → 3019.38] Um, and this is one of the things, uh, I'm considering in my Ruby code too, is that, you know, well, if you want to find something frequently by one aspect of that data, why not just store another object, um, and link to the original, uh, from that object and use, use the key that, uh, has meaning.
[3019.38 → 3028.76] Yeah. And, and we've used that in our own applications and, in, in bachelor applications from our previous iteration and in toy applications that I've written to great success.
[3029.12 → 3037.96] And on one hand, it might seem like, uh, wow, that's a pain. You have to maintain your own indexes, but it also gives you a great deal of flexibility as well.
[3037.96 → 3049.24] So it, it, it's sort of two-sided. And, and while we do want to actually natively support, uh, you know, retrieval based on, uh, a key other than,
[3049.24 → 3069.58] in an object's ID, uh, there actually are some benefits and a lot of use cases where it makes sense to, uh, to essentially, you know, build your own index custom suited for your application and, and do that work, uh, when you're storing the, the primary object, like you were saying, Sean.
[3070.68 → 3074.48] So Sean, you're the same, uh, Sean Cribs of radiant CMS fame, right?
[3074.90 → 3075.80] That is correct.
[3075.80 → 3086.02] So how do you see these document stores changing the CMS landscape? If there ever was a use case for deep, um, you know, schema less stores, I would think CMS would be it.
[3087.34 → 3102.68] Yes. And actually, um, that's part of what drew me to it. Um, uh, I had done as a proof of concept, uh, converting of radiance model layer over to MongoDB and really enjoyed the benefits, um, of what it provided.
[3102.68 → 3110.90] Uh, but on the other hand, um, I was also thinking about, uh, you know, maybe moving this into kind of multi-tenant type thing.
[3111.52 → 3121.80] And, um, then I got into the idea of, oh, well, gosh, I'm going to have to build multiple databases to keep my customers or, uh, the multiple sites, uh, separate.
[3121.80 → 3129.34] Um, and then, uh, I, it really just would, would have been a management nightmare.
[3129.78 → 3142.12] So, uh, when I saw the idea of links, um, which, which is really what drew me back to React after, after I was using Congo, um, I thought, well, that's, this is completely natural.
[3142.12 → 3150.76] So, um, you know, I can, I can take, um, I can go ahead and put the individual parts of each page into the page object.
[3150.76 → 3154.36] That makes a lot more sense than having it linked to be another table.
[3155.02 → 3159.68] Um, but then I can, um, you know, have my users go across all the different sites.
[3160.12 → 3169.24] Um, you know, maybe you have, maybe you're an editor on this site, and you own this site, and you pay for this site or you, um, you know, or you're just a, a reviewer on this site.
[3169.24 → 3184.86] Um, so there's, there are a lot of possibilities definitely for CMS, um, simply because the problem of a content management system is one of semi-structured data, um, and definitely sparsely populated semi-structured data.
[3185.78 → 3189.18] So, so we heard that you have a Ruby driver coming out.
[3189.26 → 3190.86] Do you want to kind of mention that real quick?
[3191.36 → 3191.80] Sure.
[3192.00 → 3193.90] Um, I'm releasing it tonight.
[3194.04 → 3195.26] Um, it's going to be called Ripple.
[3195.26 → 3199.92] Um, and I might, uh, interject a little bit of the story behind that name.
[3199.92 → 3202.58] Um, and, and Andy's chuckling there.
[3203.12 → 3208.06] Um, actually, RIO, um, is an Indonesian word meaning Ripple.
[3208.46 → 3214.42] So, uh, when we were trying to decide the name of it, I started off with RIO client, but it's, you know, very, uh, vanilla.
[3214.90 → 3222.44] Um, Ripple, I think is, uh, really nice because, um, it describes also kind of the idea of how RIO works.
[3222.44 → 3225.06] So, um, this will be released tonight.
[3225.24 → 3227.20] Um, it's going to be on a gem cutter.
[3227.68 → 3228.88] Uh, it's going to be Ruby gem.
[3229.60 → 3234.30] Uh, it'll be on GitHub, GitHub.com slash Sean Cribs slash Ripple.
[3235.28 → 3238.50] And, um, I'm going to encourage people to fork it.
[3238.80 → 3250.26] Um, so what it has in it is a very, uh, robust Ruby client driver, um, that gives you all the basics of working with RIO.
[3250.26 → 3257.92] Um, including things like knowing what types of HTTP responses RIO will return on different requests.
[3258.16 → 3260.48] Um, and I try to take those into account.
[3260.86 → 3275.44] And so you get a pretty, uh, pretty rich layer that includes the ability to manipulate buckets and, uh, insert and retrieve and delete and reload objects that you have, uh, in your application.
[3275.44 → 3284.10] And, uh, also, um, it's not entirely complete, but, uh, I'm going to go with the release early, release often on this.
[3284.34 → 3289.72] And, um, there's also a modelling layer, which is, uh, has a lot of similarities to Monographer.
[3289.72 → 3295.22] Um, and, uh, I have to give a John Moon maker props on Monographer.
[3295.34 → 3295.94] It's a great library.
[3296.32 → 3298.34] And I took a lot of inspiration from that.
[3298.54 → 3307.46] So, um, it's actually the, the, probably the most interesting thing about the modelling layer is that it's, uh, Rails 3 only.
[3307.60 → 3317.82] So, um, it's, uh, uses the active model library, um, to provide a lot of the more complicated things that you'd expect out of that type of library.
[3317.82 → 3327.44] And if you're new to, uh, to MongoDB and didn't catch, uh, episode, I believe it was 011, where, uh, we interviewed John about Monographer.
[3327.56 → 3329.92] You can get all the details of that.
[3330.04 → 3331.60] But we're at the part of the show.
[3331.68 → 3340.06] If you guys have, um, tuned in and hung around to the end of the show, you know that, uh, we're to the segment where we ask you what's on your open source radar.
[3340.26 → 3341.20] So, Andy, you're up first.
[3341.30 → 3345.20] What gets you excited in the world of open source other than what's going on at Basho?
[3345.20 → 3351.38] Uh, other than what's going on at Basho, um, Node.js is, is fascinating to me.
[3351.56 → 3358.66] Uh, I think there's, uh, you, uh, I mean, I think I'm not unique, uh, in being interested in that.
[3359.14 → 3362.60] Uh, I think it's, you're going to see a lot more stuff based on Node.js.
[3362.84 → 3371.10] And I'm excited about some of the work the community's doing on, uh, native, uh, Node.js support, uh, for React.
[3371.10 → 3379.52] Um, and I've been, uh, you know, I, uh, admittedly I'm not a, a Ruby person, actually.
[3379.52 → 3400.50] Uh, and I've just been really impressed by ever since we've started to, um, improve our support for Ruby, uh, the level of attention and the level of interest, uh, and, uh, the, the great, uh, feedback that I've had, uh, with, with members of the Ruby community that I haven't known before.
[3401.10 → 3419.14] Um, so, you know, in general terms, I'm just looking for, uh, I'm very excited for, um, you know, what's to come both in Sean's work and, and other people's work with regard to, uh, Ruby, uh, integration and, and, and working with React.
[3419.14 → 3426.38] I'm also really excited about, um, projects like RabbitMQ and, and AMP in general.
[3426.38 → 3445.84] Um, I think React and, and, and RabbitMQ make great sense, and we've actually talked quite a bit with people about integrating them further, whether that's providing a AMP, uh, interface to React or, uh, using React as a backend for persistent, um, AMP storage.
[3445.84 → 3451.98] Um, and, uh, you know, that's really it.
[3452.06 → 3462.26] I, I, I, I should be, uh, you know, more attentive to projects that are going out right now, but I have such a full plate, uh, that, you know, just, you know, no SQL stuff in general.
[3462.26 → 3485.68] Um, and I, I, I'm looking forward actually having spent, uh, many years, you know, I enjoy Erlang, but professionally before that I was, uh, tied to, uh, T plus and other languages that, uh, that I'd, I'd like to forget and, uh, reuse those neurons for learning, uh, learning more, uh, learning more Ruby stuff.
[3485.68 → 3499.04] So, uh, it's been a real eye-opening experience, uh, you know, having this role in this project and being to a gate, uh, being able to engage with, uh, these various communities in particular, uh, um, Ruby.
[3499.82 → 3500.80] How about you, Sean?
[3501.32 → 3506.56] Well, uh, I've been doing a lot of JavaScript lately, uh, jQuery, uh, front end stuff.
[3506.66 → 3508.64] That's, uh, always on my mind.
[3508.80 → 3513.22] Um, I like, uh, working with and building beautiful interfaces that work well.
[3513.22 → 3517.90] Um, so, um, I'm always on the lookout for new jQuery, uh, plugins.
[3518.18 → 3522.44] And I was really pleased to see, uh, when that fork came out, uh, just a couple of weeks ago.
[3523.08 → 3534.54] Um, also on, on my mind a lot, probably because of who I've been working with, but, um, there's a big resurgence of, of Lisp and scheme variants lately.
[3534.54 → 3541.14] Um, and, uh, particularly Clojure, uh, is, is the big juggernaut in this space right now.
[3541.14 → 3546.80] Um, but also, um, there's, has some smaller friends like, uh, LIFE, which is a Lisp-flavoured Erlang.
[3547.00 → 3550.04] So you can write Lisp for your Erlang applications.
[3550.42 → 3555.28] Um, and also, uh, Gambit scheme, uh, has, uh, been looking pretty cool.
[3555.36 → 3561.78] So I'm, I'm going to try to get into some Lisp this year, uh, in addition to doing more Erlang and, and, uh, and JavaScript.
[3561.78 → 3573.58] Yeah, talking about, uh, languages in general, uh, besides projects, uh, I would really love to have the time to explore Clojure some more, uh, and explore Haskell some more.
[3573.80 → 3576.28] Every time I try to learn Haskell, I end up feeling stupid.
[3576.28 → 3584.98] But I think, uh, if I actually gave it, uh, the old college try, I could really kind of wrap my head around it and, and be a better programmer as a result.
[3584.98 → 3592.68] So, it's so funny to hear you guys mention, uh, Node.js, um, cause that's like, I don't know what, like nine shows in a row in?
[3593.22 → 3593.54] Right.
[3593.86 → 3594.52] Something like that.
[3595.06 → 3597.78] But, uh, Andy, Sean, it's, uh, thank you so much for coming on the show.
[3597.86 → 3599.22] It's, uh, it's been great having you guys.
[3599.22 → 3608.74] It's, uh, Andy, it's great to see Basho's step up and scratch their own itch and, um, you know, give back to the community, even, uh, at the measures you have.
[3608.80 → 3613.12] It's such an exciting time for the NoSQL, uh, ecosystem and community.
[3613.26 → 3617.40] But, uh, how can people reach out to both of you guys via Twitter or email or?
[3618.22 → 3619.30] Uh, I'll go first.
[3619.40 → 3625.48] I'm, uh, I'm, uh, at argv0, A-R-G, V-0, A-R-G are my initials.
[3625.48 → 3630.80] And argv0 is, uh, C for, uh, the name of the program that is being executed.
[3631.26 → 3631.46] Awesome.
[3631.46 → 3634.62] I thought, I thought it was clever in meta back in 99 and it stuck.
[3635.00 → 3636.42] Um, so you can reach me.
[3636.92 → 3639.84] Twitter is usually, you know, my primary medium these days.
[3639.84 → 3647.34] But, uh, if you want to catch me on email, I'm either Andy at bashos.com or you can always reach me on the React users, uh, mailing list.
[3648.70 → 3651.12] And, uh, I'm Sean Cribs on Twitter.
[3651.34 → 3654.68] Um, just S-E-A-N-C-R-I-B-B-S.
[3654.68 → 3655.76] That's the easy one.
[3656.16 → 3657.14] Yeah, that's the easy one.
[3657.26 → 3658.14] Very vanilla, right?
[3658.40 → 3660.34] Um, but it's memorable.
[3660.58 → 3661.88] So I like to use that.
[3662.10 → 3662.18] So clever.
[3662.94 → 3669.88] And also, um, Andy isn't on there as often, but I, I'm frequently on, uh, Free node IRC.
[3670.20 → 3676.88] Um, so I hang out in the Radiant CMS and the Erlang OTP and also recently the ROC channel.
[3677.08 → 3681.18] So, um, if you want to get, get me live, that's where to find me.
[3681.18 → 3685.12] Yeah, I mean, I, I, I try to be in the ROC channel as much as possible as well, too.
[3685.20 → 3687.20] So you can catch me there live also.
[3687.92 → 3697.28] Anyone out there, if you're listening, if you didn't catch out to Spell Andy's, uh, Twitter handle, just check the, uh, Change Log Show Twitter threads, and you'll see, you'll see some corresponding.
[3697.68 → 3701.08] And both of these guys are on, uh, the Change Log Show, uh, guest list.
[3701.18 → 3703.76] It's Change Log Show forward slash guests.
[3704.42 → 3704.82] Yeah.
[3705.22 → 3705.68] On Twitter.
[3705.68 → 3706.64] Awesome.
[3706.96 → 3708.46] Well, guys, thanks again for coming on the show.
[3708.54 → 3711.12] It's been a pleasure having you and enjoy your evening.
[3711.60 → 3712.22] It's been great.
[3712.30 → 3713.24] Thank you very much, guys.
[3719.50 → 3722.46] Thank you for listening to this edition of the Change Log.
[3723.56 → 3730.24] Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[3730.24 → 3740.00] Also be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of the Change Log.
[3740.00 → 3748.48] Safe in your arms as a dark passion show.
[3749.28 → 3752.90] Was mine alone.
[3752.90 → 3756.70] Oh, man.
[3757.48 → 3759.94] Oh, man.
[3760.28 → 3761.68] Oh, man.
[3761.78 → 3764.50] Bring it back.
[3764.72 → 3768.34] Bring it back to open.
[3768.34 → 3769.64] Bring it back.
[3786.04 → 3787.04] Like we're on.
