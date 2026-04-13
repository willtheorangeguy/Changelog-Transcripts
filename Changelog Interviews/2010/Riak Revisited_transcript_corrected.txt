[0.00 → 18.34] Welcome to the Changelog episode 0.4.0.
[18.56 → 19.52] I'm Adam Stachowiak.
[19.90 → 20.78] And I'm Won Netherlands.
[20.98 → 21.92] This is the Changelog.
[21.96 → 23.88] We cover what's fresh and new in the world of open source.
[24.26 → 27.26] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.62 → 28.46] We're also up on GitHub.
[28.46 → 34.80] At GitHub.com slash explore, you'll find some trending repos, some feature repos from our blog, as well as the audio podcasts.
[35.14 → 37.06] If you're on Twitter, follow Changelog Show.
[37.24 → 38.56] As well as me, I'm Adam Stack.
[39.16 → 41.62] And I'm Penguin, P-E-N-G-W-Y-N-N.
[42.26 → 43.00] Fun episode this week.
[43.08 → 46.92] Talked to the guys at ROC for the second time to see what's new with their NoSQL store.
[47.58 → 52.24] And probably more versed in this space after the NoSQL smackdown from South by Southwest last time,
[52.40 → 57.78] which I think we chatted with them right before that event back in March.
[57.78 → 62.62] Yeah, it was kind of an unexpected surprise, really, to run into that NoSQL smackdown.
[62.70 → 64.30] And you got to participate, which was fun.
[64.44 → 67.58] But excited to revisit that scenario, too.
[68.00 → 73.28] Yeah, we need to do that, especially now that the field has, I guess, expanded a bit.
[73.38 → 76.66] There are more players in the space and see how they stack up.
[76.66 → 83.76] You know, a couple of questions that I didn't ask the React guys that I wish I had of, you know, one of them is, are you web scale?
[84.44 → 87.86] Have you seen the MongoDB cartoons that made the Internets?
[88.04 → 89.02] I hadn't seen them yet, no.
[89.48 → 90.50] I'll put that in the show notes.
[90.86 → 91.38] That'd be awesome.
[91.76 → 93.70] It's the MySQL guy versus the Congo guy.
[93.70 → 99.18] So I was curious of how, you know, RIO stands up to the scaling issue.
[99.40 → 101.56] But RIO is such a versatile player.
[101.64 → 107.78] It looks like it plays kind of at the low end against Congo and definitely at the high end against Cassandra with some of its architecture.
[108.04 → 109.56] Just some amazing stuff.
[109.64 → 111.76] And they've got the new RIO search that's out.
[112.34 → 116.22] So Mark and Andy give you the scoop on all things RIO.
[116.32 → 118.20] And John Winemaker joins us for this episode.
[118.20 → 120.38] So he's been playing with RIO, I know.
[120.58 → 123.60] So I pulled him in to ask some tough pointed questions.
[123.76 → 126.84] And plus he's big in the Congo space too.
[126.88 → 131.50] So he's kind of got a side-by-side picture of what to expect and good questions to ask when comparing.
[132.06 → 132.50] Exactly.
[132.88 → 135.70] You know, I'll be out in California, I guess, in a couple of weeks.
[135.70 → 139.12] And we're recording this first or second week of November.
[139.28 → 140.44] I forget what day it is.
[140.72 → 144.34] I'll be out there in the 15th through the 19th.
[144.34 → 147.78] Hopefully we can line up some talks with some folks out in the Bay Area.
[148.20 → 149.00] That'd be exciting.
[149.70 → 156.00] If you've got somebody that you would like to see on the changelog or hear on the changelog to talk about a project near and dear to your heart,
[156.20 → 158.48] email us at ping at the changelog.com.
[158.80 → 160.10] We'll see if we can get him on the show.
[160.62 → 160.98] Absolutely.
[161.36 → 161.98] This is a good show.
[162.00 → 162.58] You want to get to it?
[162.88 → 163.50] Let's do it.
[163.50 → 179.10] We're joined today by Andy Gross and Mark Phillips from Basho, makers of the React NoSQL database.
[179.30 → 183.04] Andy, why don't you start and introduce yourself for the folks that didn't catch the first episode.
[183.92 → 184.52] Hi, Won.
[184.58 → 185.46] I'm Andy Gross.
[185.56 → 187.40] I'm VP of Engineering here at Basho.
[187.40 → 190.50] Like you said, we make the React NoSQL database.
[191.12 → 194.28] Among other things, we've actually just released React Search as well.
[194.78 → 195.68] It's great to be here.
[197.32 → 197.94] And Mark?
[199.02 → 199.62] Hey, guys.
[199.90 → 200.80] This is Mark Phillips.
[200.90 → 203.40] I'm the community manager at Bastard Technologies.
[204.06 → 209.98] As Andy said, we have a whole slew of software that we're really excited about, React and React Search being the two primary.
[210.40 → 211.40] Thrilled to be here as well.
[211.46 → 212.02] Thanks for having us.
[213.20 → 216.98] Mark, if I slip up and call you FARC, it's because that's what your Twitter handle is.
[216.98 → 217.72] You know what, Won?
[217.74 → 218.68] That is totally acceptable.
[219.90 → 226.22] And I should mention we're joined today by John Wanamaker, who's, I guess, of Monographer fame.
[226.32 → 227.44] John, why don't you say a quick hello?
[228.36 → 229.18] Hello, everyone.
[231.36 → 233.38] And you can introduce yourself for the folks that don't know.
[234.34 → 235.24] I'm John Wanamaker.
[235.24 → 240.78] I work at Ordered List and do a lot with Congo, React, and other various NoSQL databases.
[241.06 → 243.28] And occasionally, I'm forced to throw in MySQL in the loop.
[243.28 → 250.48] So I guess the last time we spoke to you guys, it was back in February when we first discovered React.
[250.76 → 256.40] So tell us, I guess, what has changed in the React project since February.
[257.24 → 257.74] Sure.
[257.92 → 259.98] We've had a lot of stuff change, actually.
[259.98 → 264.98] We have released a bunch of usability improvements.
[265.84 → 275.22] We can now download React as a binary build for various platforms, Debian, Ubuntu, CentOS, OpenSolaris, Polaris, et cetera.
[276.00 → 284.46] We've replaced some of the earlier storage backends with a brand-new high-performance storage backend called Bit Cask.
[284.46 → 291.90] And we've also released React Search, which is a nice complement to the React key value store.
[292.82 → 297.80] Key value systems tend to have a somewhat limiting query model in that you can only look things up by keys.
[298.84 → 306.36] With React Search, you can also search in a full-text fashion similar to Lucene or Solar.
[306.50 → 309.34] You can search by the values of your objects as well.
[309.34 → 313.86] So it makes data a lot more discoverable and gives you a much richer query interface.
[314.62 → 315.58] A couple other things.
[315.72 → 316.58] We've opened an office.
[316.72 → 318.30] The company's opened an office in San Francisco.
[319.06 → 326.82] We switched from Mercurial to Bitbucket to GitHub and a bunch of other things that we'll probably get to later in the podcast.
[328.58 → 333.60] We'll dive into the GitHub versus Mercurial switch in just a moment.
[333.60 → 337.52] But let's talk about React Search for a moment.
[337.82 → 342.08] Is it a standalone application or does this have to be used with the key value store?
[343.44 → 346.32] It can be used in a number of different ways, actually.
[346.44 → 347.24] You can use it.
[347.36 → 349.00] You can integrate it with the key value store.
[350.46 → 358.46] React stores data in batches of keys and values called buckets, somewhat analogous to an RDBMS table.
[358.46 → 363.80] And with React Search, for individual buckets, you can mark them as searchable.
[364.62 → 369.80] And just by side effect, everything that's put into that bucket has a full-text search index.
[370.26 → 373.22] So you can use it in an integrated fashion with React key value.
[373.72 → 378.52] It also exports an Apache Solar-compatible API.
[378.52 → 382.76] So you can use it as if it was an Apache Solar server.
[384.20 → 385.84] Use existing Solar clients.
[386.26 → 392.18] Use that same RESTful API to treat it as if it were just a more scalable Apache Solar.
[392.78 → 398.92] What sort of languages is you seeing, I guess, buy into React as a NoSQL solution on the key value store side?
[399.90 → 400.26] Yeah, sure.
[400.46 → 403.76] So obviously we do really well with the Erlang community.
[404.16 → 404.90] That's where we started.
[404.90 → 407.64] And that was the first interface we really supported heavily.
[407.64 → 412.56] Since then, I think you guys had Sean back on in February, and he was writing the Ripple driver.
[413.06 → 418.62] And I'm sure, as John can tell you, that is a beautiful piece of code that has really taken with a lot of the Ruby community.
[418.82 → 422.50] So we've seen a ton of adoption with Ruby and Ripple.
[423.84 → 426.18] Outside of that, Java, Python.
[426.50 → 431.06] And over the last two or three months, we've seen a ton of uptake with Node.js,
[431.06 → 435.98] thanks to a nifty little library written by somebody from the community called React.js, actually.
[435.98 → 439.34] And his name is Francisco Tricky, at Franco6 on Twitter.
[439.52 → 440.94] So pretty good spread across the board.
[441.50 → 444.40] But Ruby, Node.js, Java, and Python, I would say, are the top four.
[445.30 → 450.78] That may be the fastest, other than the Node episode itself, that we've kept the Node.js streak alive here in the changelog.
[450.78 → 455.24] So, John, you're a Congo guy, writing Monographer.
[455.42 → 461.96] I was actually quite surprised to see you start to commit on some React wrapper commits on GitHub.
[462.16 → 463.36] So you played with React.
[463.50 → 466.48] Any questions for these guys as far as comparing and contrasting?
[466.48 → 467.48] Yeah.
[468.70 → 477.18] So I guess, why don't you guys talk a little bit, I guess, from your point of view of, not necessarily, we can talk about data modelling as well,
[477.24 → 481.36] but just from an administration point of view, maybe what are the benefits of using React?
[481.48 → 486.64] What kind of tools do you guys have that maybe other databases don't have or where you do things a little bit differently?
[486.64 → 487.04] Sure.
[488.48 → 497.72] So one of our main focuses, a lot of the people at Basho came from Akamai Technologies, where we operated, at the time, probably one of the larger distributed systems.
[497.86 → 500.86] Google came along and quickly eclipsed us.
[501.44 → 509.04] But one of the core design philosophies about React is ease of operations.
[509.82 → 513.64] So we've spent a lot of time on making it easily elastic.
[513.64 → 516.40] So it scales both up and down.
[516.84 → 517.90] So you add a node.
[518.14 → 520.08] It's a single command line to add a node.
[520.64 → 526.14] And when you add that node, you get a linear increase in throughput and storage capacity.
[527.36 → 528.90] And it also scales down.
[529.68 → 532.52] You can run many nodes on your laptop.
[532.94 → 540.84] I can run easily in the tens, 50 React nodes on my MacBook here with no sort of loss of functionality.
[540.84 → 547.82] The other aspect to that it is a truly sort of decentralized system in that no node is special.
[548.06 → 554.40] There's both not a single point of failure, but it also means that you don't have to pay special attention to a given node.
[554.80 → 556.08] They're all sort of fungible.
[556.18 → 557.36] They can come in and out of the network.
[557.62 → 559.12] And that's tolerated really well.
[559.20 → 563.46] So that's one of the main focuses of React is that it should be easy to operate.
[563.46 → 569.76] You know, in the way that you describe React is a lot of the same language that the Cassandra folks use to describe that platform.
[569.88 → 571.78] What distinctions could you draw between the two?
[572.70 → 575.38] So, yes, React and Cassandra are very similar.
[575.52 → 587.64] I'd say that if you were to sort of segment the NoSQL space, you'd have React, Cassandra, and Voldemort probably in the same group in their goals in that they focus on scaling out.
[587.64 → 597.52] But React is a little – Cassandra has a slightly different data model, a slightly more complex data model, and that's from its sort of Google Bistable influence there.
[597.52 → 604.24] So React is much more of a sort of just traditional key value store at heart.
[604.34 → 608.74] It doesn't have the sort of column family model that comes from Bistable.
[609.28 → 620.74] It also has a couple of interesting features that aren't found in Cassandra, like the link relationships you can establish between objects and built-in JavaScript Map Reduce.
[620.74 → 628.22] And in the future, we'll probably be releasing some more queryability improvements at the React meetup the other night here in San Francisco.
[629.58 → 644.34] We announced some improvements to Map Reduce that allow you to sort of build some meaning into the values of your – into your keys and then perform, you know, regular expression matches of your keys in a Map Reduce job.
[645.04 → 648.84] Cassandra has Map Reduce as well, but it's more of a traditional sort of Hadoop integration there.
[648.84 → 652.20] So you mentioned Map Reduce and JavaScript.
[652.56 → 654.68] What sort of decisions did you draw to Couch?
[655.94 → 660.68] So Couch is – it's actually very similar to Couch, at least in the implementation.
[661.00 → 664.36] We both embed the Spider Monkey JavaScript virtual machine.
[665.06 → 675.44] It's different from Couch in that Couch does sort of incremental Map Reduce in that every time you write to the database, it maintains an index for you.
[675.44 → 687.54] So React's Map Reduce is much more focused as a sort of ad hoc query mechanism in that you don't – React doesn't automatically run Map Reduce when you write to the database.
[687.84 → 692.06] You issue a Map Reduce job as a query, you get the result back, and React doesn't save that for you.
[692.06 → 696.10] If you want to save that, it's – you put it back into the database yourself.
[696.10 → 707.44] So Couch is Map Reduce is more of a sort of internal query mechanism where ours is an external user-facing means of querying the database.
[707.96 → 709.84] So you mentioned links a little bit.
[710.02 → 712.34] Why don't you go into a little bit of the benefit of that?
[712.46 → 719.46] I see when I look at it a little bit, a little hint of the graph side of the database world and stuff.
[719.80 → 723.26] Maybe where are some distinctions between there or what the benefits are?
[723.26 → 729.68] Sure. So links are basically a tag you can put on an object.
[729.82 → 735.78] Any object can have a list of links to other objects, other keys and values in the React database.
[736.20 → 739.96] It's a three-tuple of bucket, key, and tag.
[740.72 → 747.42] So by – this allows you to have sort of ad hoc, flexible, lightweight relationships between objects.
[747.42 → 751.50] It's not quite a full-fledged graph database, nor is it meant to be.
[752.30 → 767.00] But you can model things like – a social networking example would be a user has friends, and those friends have wall posts, Facebook wall updates or whatever.
[767.00 → 780.30] And you can – from the HTTP side of things, you can craft together a URL that just basically says slash users slash win slash friends.
[780.50 → 785.10] And then you can put a tag on those, like friends in Texas.
[785.10 → 798.34] So it's not – it doesn't have full sort of graph traversal features, but it's a nice way – and like I said before, you know, accessing stuff by keys and values can be somewhat limiting.
[798.34 → 813.10] So we added the link feature to allow you to easily add a little more riches to your data and a little richer query interface by being able to just, you know, dynamically establish these relationships between objects.
[814.06 → 817.82] Well, it seems like a venting is the new hotness in web application architecture.
[818.06 → 820.14] Node is built that way from the ground up.
[820.24 → 822.14] What about the other drivers for ROC?
[822.24 → 826.22] Which of these support that sort of asynchronous architecture?
[826.22 → 826.32] Sure.
[827.22 → 834.26] So all the drivers are – the API to ROC, we have two of them, actually.
[834.40 → 839.26] I think the first time we talked we only had one, which was the HTTP interface.
[839.84 → 848.34] We find that the HTTP interface goes a long way in that, you know, it's – any language can talk HTTP.
[848.34 → 863.68] But we've recently added – or maybe not recently, but definitely since the last time we were on – a protocol buffers interface, which is a sort of binary protocol that doesn't have some of the parsing overhead of HTTP.
[863.68 → 872.12] As far as – I said Node.js is probably the most sort of event callback-driven driver that we have.
[872.18 → 877.20] The other ones provide a relatively synchronous interface to ROC.
[877.32 → 880.50] So I don't think there's – maybe the Erlang one does as well.
[880.58 → 881.22] The Erlang one.
[881.58 → 883.52] Node and Erlang are kind of similar in their design.
[884.52 → 886.86] Node is probably the most event-driven one.
[886.86 → 890.72] We also have a native JavaScript interface that's not integrated with Node.
[890.82 → 894.10] It's more of a sort of proof of concept that we provide.
[894.46 → 898.34] But all the other ones are a relatively synchronous interface.
[898.96 → 900.36] Talk to us about Bit Cask.
[901.54 → 901.94] Bit Cask.
[902.32 → 903.84] So Bit Cask is really cool.
[904.32 → 906.60] And that's another thing that's happened since the last time we were on.
[906.60 → 916.66] Eric Brewer, father of the cap theorem and arguably sort of grandfather of NoSQL, joined Basho's board of directors this past year.
[917.56 → 933.86] And when we were talking about storage backends, he came up with a fascinating idea with Bit Cask in that you can – if you have the capacity to keep all your keys in memory, which a lot of use cases you can do that.
[933.86 → 947.20] You can have a really simple, easy to design, easy to implement, relatively easy to implement storage system that uses basically the commit log as the database itself.
[947.84 → 960.98] So Bit Cask is an append-only file format where when you write a value to the database, you write it to disk and then update a pointer in memory that points to the file and offset in the file on disk.
[960.98 → 968.02] And by keeping the keys in memory, you guarantee that for a read, you only have to do one file I.O.
[968.02 → 975.40] It's a very fast memory lookup in a hash table that points at a file, and then you find that file and seek to a certain point to read the value.
[976.14 → 979.38] And for writes, it's just a simple append to a file.
[979.38 → 994.66] So Bit Cask offers very, very predictable latency given that you can keep – if you can keep all your keys in memory, we actually recommend that people use Bit Cask as opposed to our previous recommended storage backend, which was embedded in ODB.
[994.66 → 1005.84] And like I said, the latency is very, very predictable since you don't have to do a lot of random seeking around in a file to read a value.
[1006.00 → 1010.32] It's a guaranteed one disk I.O. for a read and a simple append for a White.
[1010.32 → 1024.60] And it allows us to also leverage the file system cache in the kernel to allow us not to have to provide any sort of complicated caching layer in React itself.
[1025.18 → 1030.36] So for a lot of use cases, or for at least the use cases that you can guarantee, you can keep all your keys in memory.
[1030.60 → 1031.40] And this is just the keys.
[1031.48 → 1033.00] This isn't the whole value.
[1034.10 → 1035.52] Bit Cask is the recommended backend.
[1035.52 → 1046.00] And nowadays, we really only recommend In-store for use cases where you have so many keys that the memory requirement of Bit Cask isn't going to work.
[1047.10 → 1053.62] So we talked a little bit about administration and how you guys are real big on making that easy.
[1054.34 → 1059.46] We've talked a little bit about data modelling, and I guess I'd be kind of curious about going into that a little bit more.
[1059.46 → 1066.54] So pretty much right now, you have key and value and then Map Reduce for dynamic lookups.
[1067.72 → 1073.34] Maybe we could talk now a little bit about search and how that fits into the equation of getting at your data.
[1075.62 → 1082.70] So like we talked about before, yeah, key and value access is sort of the React default.
[1082.70 → 1087.66] We then added Map Reduce on to have a slightly more rich query model.
[1088.46 → 1094.18] But it's still, there's some overhead in sort of walking through your entire bucket to find out about data.
[1096.40 → 1097.48] Interesting story about search.
[1097.56 → 1103.70] Search was really born out of one of our engineers, John Mueller-Ally's frustration with the limitation of the key value model.
[1104.64 → 1111.08] If you guys have seen that NoSQL cartoon of the three guys in the office complaining about distributed Map Reduce and Erlang,
[1111.08 → 1114.40] that was actually written by a Basho guy.
[1115.64 → 1123.24] And that was sort of the day that search was born out of a desire to have a much more queryable interface to React.
[1123.90 → 1136.72] So search from the outside looks a lot like, well, Apache Solar in its API and Apache Lucene in its query syntax.
[1136.72 → 1144.38] So the Lucene sort of query syntax has become kind of a standard, a semi-standard in information retrieval.
[1144.94 → 1154.34] So in addition to the existing types of Map Reduce jobs where you either pass in a list of buckets and keys or pass in just a bucket and iterate through the whole thing,
[1154.34 → 1163.30] with search, you can insert a Map Reduce job that is formed as a Lucerne-style query.
[1163.44 → 1172.16] So you could say, you know, podcast and changelog show and get all the documents whose values matched that in some way
[1172.16 → 1175.66] and then pass those documents on to a next phase of the Map Reduce.
[1175.66 → 1182.54] So I think you'll probably see, whereas before people would go through a lot of effort to sort of know the keys ahead of time
[1182.54 → 1185.48] or have to go through an entire bucket to find what they wanted,
[1185.90 → 1195.00] now users can simply write in a full-text search query and start their Map Reduce jobs off that way
[1195.00 → 1199.82] or insert that kind of query to any point in the Map Reduce job.
[1199.82 → 1210.06] So that's how you can access it from the key value store side by just by adding another Map Reduce job type, Lucene search.
[1210.92 → 1214.04] And it's not actually, sorry, it's not actually implemented in Lucene.
[1214.24 → 1220.66] It exposes the API, and we do have a little bit of Apache solar code for text analysis,
[1221.08 → 1226.92] but on the back end it's all written in Erlang in the same sort of style as the React key value store.
[1226.92 → 1232.24] And so is it content aware, or what does it kind of assume as a value?
[1232.40 → 1237.50] Like if you store JSON, can you search on an individual key in JSON
[1237.50 → 1240.46] or do you need to have that actually as a separate React key?
[1241.94 → 1247.74] You can actually make schemas for individual buckets.
[1249.12 → 1251.98] So you can define different fields.
[1251.98 → 1257.60] I believe it's XML or JSON from the solar interface.
[1258.16 → 1264.48] So you can say, you know, this field is a date, this field is a time, this field is a number, this field is a string,
[1264.98 → 1267.78] and get the right sort of indexing semantics there.
[1267.90 → 1270.60] So it's not quite the solar schema format.
[1271.12 → 1273.24] It's our own sort of format for the schema file,
[1273.24 → 1279.14] but you have a lot of flexibility in defining what fields are what data type
[1279.14 → 1280.66] and which ones get indexed and which don't.
[1281.36 → 1284.52] So you guys mentioned earlier that you made the move from Bitbucket over to GitHub.
[1284.88 → 1289.66] So, Mark, I guess building a community around any project is crucial.
[1290.04 → 1291.80] What went into the decision to go to GitHub?
[1293.08 → 1298.22] So the decision to go to GitHub was not one that we made easily and hastily.
[1298.22 → 1306.18] You know, we, since before we open-sourced React, it was developed using Mercurial in-house.
[1306.52 → 1309.00] And, you know, that was something that we were used to in all our developers,
[1309.42 → 1313.06] though they were both versed in Git and Mercurial.
[1313.58 → 1315.72] You know, they stuck with Mercurial because that's what we knew,
[1316.24 → 1318.38] and that's what we were accustomed to.
[1318.52 → 1322.86] So we open-sourced back in August of last year and didn't think much of it.
[1322.86 → 1328.40] You know, we were, to be honest, focused much more on, you know,
[1328.44 → 1331.30] pushing out consistent releases that just made the code stronger.
[1331.56 → 1336.04] And, you know, we weren't really pushing for that type of community involvement
[1336.04 → 1341.90] that's, you know, really advantageous to a large open-scale, large open-source project.
[1342.36 → 1346.56] So the move to GitHub was, one, driven not by, you know,
[1346.60 → 1349.56] need for better version control technology.
[1349.56 → 1352.90] And Mercurial was a great system.
[1353.48 → 1356.56] And, you know, all our guys, all our hackers liked it just fine.
[1356.98 → 1362.26] But, you know, the way that GitHub has taken Git and put so much momentum behind it
[1362.26 → 1365.08] is just something that you can't ignore.
[1365.30 → 1369.60] So, you know, for me as a community manager and for, you know, the entire company
[1369.60 → 1372.30] looking for that deep level of community involvement,
[1372.38 → 1375.20] it was just something that was inevitable for us.
[1375.20 → 1382.90] Yeah, I mean, there's been a huge uptick in pull requests since we moved to Git.
[1383.38 → 1386.10] Mark, I'd say maybe, what was it, four or five months back,
[1386.14 → 1387.36] we started mirroring onto GitHub.
[1388.36 → 1390.28] And that was probably what did it for us.
[1390.42 → 1394.34] Once we did that, people expected to be able to submit pull requests
[1394.34 → 1396.52] and have them integrated quickly and easily.
[1397.16 → 1402.76] So it was really about the community and about desire for ease of external code contributions
[1402.76 → 1404.46] that made us move to GitHub.
[1405.34 → 1410.80] Yeah, and, you know, before when you asked about where we're seeing the most developer uptake,
[1411.36 → 1416.04] so Sean Cribs' Ripple library and the React.js library that was contributed from the community
[1416.04 → 1418.28] are both hosted on GitHub and have always been there.
[1419.14 → 1421.58] And, you know, just judging my numbers of followers,
[1422.22 → 1424.22] granted that doesn't actually indicate code quality,
[1425.04 → 1429.04] you know, those far surpassed any driver that we have.
[1429.04 → 1432.72] And actually Sean's driver code surpasses that of the React repo itself.
[1433.02 → 1436.36] But I don't suspect it'll be like that much longer now that we've switched.
[1436.84 → 1443.18] So it was primarily for community involvement and the exposure that GitHub offers.
[1443.72 → 1449.54] So as users of both Git and Mercurial, what contrast could you make between those two?
[1452.02 → 1457.20] I think, I mean, they're really, they both provide the same real features.
[1457.20 → 1462.92] People that have, people have compared the two and sort of done a side-by-side comparison.
[1463.04 → 1466.26] There are some things that are easier in one, some things that are easier in another.
[1467.08 → 1470.82] So on the merits of technology, I'd say they're both about the same.
[1470.88 → 1476.48] I think we originally chose Mercurial because we're all sort of old Python guys in previous lives.
[1476.48 → 1485.30] And the notion that we could write sort of commit hooks and stuff in Python was the initial sort of,
[1485.98 → 1489.18] is what made Mercurial and therefore Bitbucket initially attractive.
[1489.38 → 1493.38] But we never actually ended up writing any, never ended up having to use that functionality.
[1494.74 → 1497.76] And so, you know, I had a little bit of a learning curve getting used to Git.
[1497.96 → 1501.14] But, you know, it's really just a tool for us.
[1501.14 → 1507.46] And, you know, the community was the big driver for that, for the switch.
[1508.98 → 1514.28] And so for you guys, you talked about how you switched to GitHub and how you have contributions going up.
[1515.12 → 1518.24] Since Basho is kind of primarily the company behind React,
[1518.34 → 1521.84] what kind of percentage or feeling do you overall have of, like, who,
[1522.08 → 1526.10] like contributing from outside of Basho and, like, contributing inside of Basho?
[1526.10 → 1534.46] So we have, I think, there's like a thanks file in the React source code.
[1534.58 → 1541.62] And there's probably at least 30 people now outside of Basho who have contributed in some sort of meaningful way to the project.
[1543.56 → 1546.26] Being in Erlang and being sort of a database,
[1547.16 → 1552.48] there is a somewhat high bar to really making meaningful contributions to the core.
[1552.48 → 1555.60] But we're actually starting to see people do that now.
[1556.36 → 1560.16] So most of the contributions are, you know, bug fixes, documentation improvements,
[1560.54 → 1562.82] changes to the client libraries.
[1563.46 → 1566.44] And we don't really have that many developers contributing to the core.
[1566.58 → 1572.76] But we're seeing people starting to come up to speed enough with the sort of core, you know,
[1572.82 → 1577.22] distributed systems code and database, you know, storage system code,
[1577.22 → 1580.58] where I wouldn't be surprised in the future, in the near future,
[1580.58 → 1587.66] if we had some external contributors actually making sort of large-scale changes across the entire code base.
[1588.16 → 1594.40] But until now, it's been mostly bug fixes and contributions to the various client libraries.
[1595.06 → 1596.72] So back in March at South by Southwest,
[1596.92 → 1601.54] I had the privilege of participating in the NoSQL Smackdown at South by.
[1601.54 → 1606.18] And one of the exercises that we had to do was to kind of size up the competition,
[1606.28 → 1607.26] the other players in the space.
[1607.30 → 1611.76] And the only ones that were represented were Congo, Cassandra, Couch,
[1612.04 → 1616.86] and I guess Amazon was represented, even though it's not open source.
[1618.42 → 1620.48] They're Dynamo database technology.
[1620.92 → 1624.04] If you guys had to prepare for such a hypothetical competition,
[1624.28 → 1628.62] what distinctions would you draw between ROC and, I guess, the rest of the field?
[1628.62 → 1629.84] Where does ROC shine?
[1629.84 → 1640.20] So it's really around both operational easy use and predictable latency is one of the ones that,
[1640.38 → 1646.78] since we released Bit Cask, we're really sort of proud of the fact that, you know,
[1646.84 → 1652.18] there's not going to be wildly varying latency in your queries.
[1652.18 → 1664.86] So in these days when, you know, we're really moving towards sort of soft real-time systems where the correctness of a result has a direct relation to how quickly you can get that data,
[1666.92 → 1668.64] latency is really important.
[1668.64 → 1678.34] And especially when these databases are, you know, or users of ROC are building sort of, you know, service-oriented,
[1679.30 → 1682.44] you know, using ROC as a layer in another system.
[1682.44 → 1690.56] So every sort of millisecond of latency is, you know, comes out of some sort of bottom line SLA for the rest of the system.
[1690.96 → 1700.26] It's very important to be able to predict, you know, well, ROC will always, you know, 99.9% of the time respond in this amount of time.
[1700.26 → 1715.16] So the sort of simplicity and elegance of the Bit Cask data model and some of the soft real-time properties of Erlang make it very suitable for latency-sensitive applications.
[1715.90 → 1720.02] And like I said before, you know, we're always focusing on operational ease of use.
[1720.56 → 1729.88] So if you want really predictable scaling without headaches when you add and remove nodes, then I think that's really where ROC shines.
[1730.70 → 1736.82] So on the MongoDB side, they tell you up front that if you need transactions, it's probably not your store of choice.
[1737.42 → 1740.80] What caveats would you state with ROC?
[1743.50 → 1751.16] Well, again, you know, I think for most of the NoSQL projects, you know, transactions, joins are just off the table to start with.
[1751.60 → 1755.36] With ROC, I'd add that, you know, it is a key value store at heart.
[1755.36 → 1766.60] So trying to bolt on more complex data models is, you know, just be aware of what the strengths of the system are.
[1767.16 → 1773.08] That being said, you know, with things like search, that sort of caveat is becoming more and more blurred.
[1773.08 → 1780.04] And we do plan to release other database products that have richer query models.
[1781.56 → 1787.28] But I would say, you know, just know that it's a key value store and design your app accordingly.
[1787.28 → 1792.52] So I think my next question would be maybe for Mark Moore.
[1793.56 → 1796.84] You know, obviously the developers that are listening to this are open source developers.
[1796.96 → 1801.96] They're people who, you know, they end up with their own little kind of communities around projects and stuff.
[1801.96 → 1806.78] And I was just wondering if, you know, Basho and React, and now this is starting to get to be pretty well known and stuff,
[1806.86 → 1813.10] if you had any tips for someone who's managing their own project, like how to get the word out or how to manage, you know,
[1813.16 → 1816.06] community contributions and awareness and things like that.
[1816.12 → 1817.70] Maybe if you had any tips for the people that are listening.
[1818.36 → 1818.60] Certainly.
[1819.74 → 1820.08] Thanks.
[1820.16 → 1820.92] Thanks for asking that.
[1821.14 → 1824.00] And quite frankly, I'm quite flattered you would do so.
[1824.00 → 1833.78] You know, we've come a long way since we first open sourced, and I think I took this position back in, maybe it was May or so, maybe April or May.
[1834.52 → 1841.16] And what I found to be the most effective, and we were lucky because we had a clean slate, but what I found to be most effective was just get the basics down.
[1841.52 → 1845.80] So I think when we were on the show last, or when Andy and Sean were on the show last in February, we didn't even have a wiki.
[1846.20 → 1847.72] You know, make sure you have a wiki up there.
[1847.72 → 1857.44] Something that I've done that for some reason has been remarkably successful is I write something called the React Recap three days a week,
[1857.52 → 1858.78] so usually Monday, Wednesday, and Friday.
[1859.40 → 1871.38] And that is just a plain text email with anywhere from three to ten bullet points with what's been happening in the community over the last two days or three days.
[1871.38 → 1885.18] And it goes through anything from blog posts written by people using React to new libraries that have appeared to bug fixes that have gone into new wiki pages to events happening in any corner of the globe.
[1886.16 → 1894.02] I even go into our – we log our IRC channel, and I go and kind of curate conversations that may not appear in the wiki,
[1894.22 → 1899.52] and I kind of dig through there for tidbits that people might want and also for things that help us update the wiki.
[1901.38 → 1907.86] Other than that, you know, just – I send a lot of emails to, you know, to people who have expressed interest here
[1907.86 → 1912.12] and who have a question that didn't get a follow-up maybe a few days ago.
[1913.18 → 1918.78] So it's a lot of one-on-one stuff that isn't really happening in the public forum,
[1918.86 → 1922.92] which kind of generates a bigger buzz maybe a week or a month down the line.
[1922.92 → 1926.74] And other than that, stay up to date on the space.
[1927.56 → 1934.28] You know, so I spend a lot of time reading blogs about Congo and Cassandra and the other players in the space
[1934.28 → 1935.80] and MySQL and Postgres and all those guys.
[1936.28 → 1939.70] So I guess that would be some advice to offer.
[1940.14 → 1942.86] So it's not just about grabbing developer mind share.
[1942.94 → 1948.74] You also need some wins and, I guess, demonstrating adoption of the platform.
[1948.74 → 1955.44] You know, John's living proof with Congo that they're using it over with Harmony, their CMS application.
[1955.54 → 1957.52] What big wins do you have with Basho?
[1958.76 → 1965.94] So open source, I would say the one we're most proud of these days is probably the Mozilla use case.
[1967.32 → 1971.02] And maybe Andy can speak more to the specific stuff they're doing with querying and whatnot.
[1971.02 → 1979.76] But they're running several React clusters, one of which is to kind of log data given through their test pilot project.
[1980.82 → 1982.78] So we've worked those guys pretty extensively.
[1983.00 → 1990.16] There's some great blog posts by them both on just using React and kind of benchmarking and performance, stuff like that.
[1990.16 → 1995.62] But there's another nifty little startup out of Amsterdam we're pretty excited about called Wide Script.
[1996.06 → 2001.82] And Frank Francisco Trick, who wrote the React.js library, is kind of the lead dev on that project.
[2002.50 → 2006.58] And those guys are not out of beta yet, but I'm really excited to see what they do with that.
[2007.42 → 2008.92] So Mozilla, Wide Script.
[2009.70 → 2011.50] There's actually a page on our wiki called Who is using React?
[2011.80 → 2015.64] So if you go to wiki.bashr.com and on the left column there, you'll see who is using React.
[2015.80 → 2018.40] There's about 15 companies that we know of open source.
[2018.40 → 2025.24] There's another great company called Imagist, which is using actually React and React search right now.
[2025.34 → 2027.04] We just found out a few days ago.
[2028.58 → 2033.94] And oddly enough, I'm getting a lot of emails out of the blue that just say, oh, by the way, we have React in production.
[2034.72 → 2038.46] Which is really nice because you know that the database is rock solid.
[2038.56 → 2043.16] And these are people we've never heard from on the mailing list or never seen an IRC or never tweeted about using React.
[2043.16 → 2052.20] And I think it kind of speaks to the simplicity of getting a three or five node cluster running and just starting to pump data into it and serve requests out of it.
[2052.42 → 2054.88] So that's that.
[2055.34 → 2060.06] Well, this is the part of the show where we turn it upside down and ask what's on your developer radar.
[2060.28 → 2062.84] It seems like through the magic of Skype, we may have lost Andy.
[2062.92 → 2063.84] We'll see if we can get him back.
[2063.92 → 2066.18] But if not, Mark, why don't you go ahead and answer the question?
[2066.28 → 2070.32] What out there in the world of open source has got you excited that you just can't wait to play with?
[2070.32 → 2071.42] Oh, Geez.
[2072.92 → 2080.64] So a bit of a tough question for me because I'm focused more on the promoting and the code development rather than actually the usage.
[2081.72 → 2083.88] So I'm sure everybody has answered Node.
[2084.82 → 2087.04] We're pretty excited about Node as a technology.
[2087.92 → 2098.90] We partnered with Joint to kind of build cookie cutter and really powerful React machines on their platform.
[2098.90 → 2107.98] And through that, we've been talking to a few of the guys over there, Ryan Dahl, and I believe Isaac is his name who did NPM, about better ways to integrate React with Node.
[2108.42 → 2112.04] So a lot of our developers have been checking out Node and seeing where we can kind of contribute to that.
[2112.04 → 2121.58] Other than that, I'm actually just pretty filled about the other NoSQL databases.
[2123.64 → 2131.32] You know, a lot of people see us as in competition, but we're good friends with a lot of those guys, and they write perfect software as a rule.
[2131.32 → 2137.86] And a lot of the people that we see using React are actually using React alongside of, you know, a MongoDB or alongside of a Regis.
[2138.10 → 2140.22] Your Regis seems to pop up in every single application.
[2142.18 → 2148.42] And so, you know, just seeing that the other players in the space do really well is something that is good for the space, but also something that we're all interested in.
[2148.54 → 2152.20] So, you know, if we come off as cutthroat, it's not the way it is.
[2152.90 → 2154.06] We're excited about Regis, too.
[2154.08 → 2156.36] We're trying to get an anti-res on the show.
[2156.36 → 2161.16] Yeah, if the amount of code that he writes is any indication, I don't think you'll be seeing him for any time.
[2163.02 → 2163.66] One second.
[2163.76 → 2164.96] Let me drag Andy back in.
[2166.50 → 2167.02] All right.
[2167.28 → 2172.00] So, Andy, we're just at the radar question, so I'll pose it to you as well.
[2172.28 → 2176.06] So, Andy, what's got you excited in the world of open source to play with?
[2177.16 → 2177.78] Oh, God.
[2179.36 → 2181.52] Lots of stuff that I don't have time to play with.
[2181.52 → 2185.16] I think some of the new JVM languages, well, I guess they're not so new anymore,
[2185.16 → 2188.54] but things like Scala and Clojure are very interesting to me.
[2190.28 → 2196.18] And, you know, they're sort of the top of my queue of things to investigate and learn.
[2197.12 → 2199.94] Other than that, I'm really excited about Node.js.
[2200.40 → 2206.12] I've gotten a little time to play with it since the React.js library was released, but doing more things with that.
[2206.12 → 2213.78] But mostly, you know, this may sound unoriginal and kind of lame, but React, you know, of all the things that I do
[2213.78 → 2219.72] and all the open source projects I've been involved with, I really look forward to some of the stuff we have in the pipe for React
[2219.72 → 2221.66] and exciting new stuff as well.
[2222.50 → 2223.98] Well, thanks so much for joining us today.
[2224.66 → 2225.50] Thanks for having us.
[2225.50 → 2243.84] See it in my eyes
[2243.84 → 2247.48] So how could I forget when
[2247.48 → 2250.66] I found myself
[2250.66 → 2253.24] for the first time
[2253.24 → 2256.96] Safe in your arms
[2256.96 → 2259.06] As a dark passion
[2259.06 → 2260.00] You're
