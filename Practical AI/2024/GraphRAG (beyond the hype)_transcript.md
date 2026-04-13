[0.00 --> 7.28]  Welcome to Practical AI.
[7.70 --> 15.00]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[15.00 --> 17.72]  changing the world, this is the show for you.
[18.06 --> 20.68]  Thank you to our partners at Fly.io.
[21.16 --> 26.86]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on
[26.86 --> 30.72]  six continents so you can launch your app near your users.
[31.28 --> 33.26]  Learn more at Fly.io.
[35.32 --> 39.32]  Okay, friends, I'm here with Annie Sexton over at Fly.
[39.48 --> 42.08]  Annie, you know we use Fly here at ChangeLaw.
[42.08 --> 43.10]  We love Fly.
[43.44 --> 45.96]  It is such an awesome platform and we love building on it.
[46.00 --> 51.26]  But for those who don't know much about Fly, what's special about building on Fly?
[51.50 --> 56.32]  Fly gives you a lot of flexibility, like a lot of flexibility on multiple fronts.
[56.32 --> 57.84]  And on top of that, you get...
[58.56 --> 64.22]  So I've talked a lot about the networking and that's obviously one thing, but there's various
[64.22 --> 67.34]  data stores that we partner with that are really easy to use.
[67.84 --> 71.28]  Actually, one of my favorite partners is Tigris.
[71.48 --> 75.04]  I can't say enough good things about them when it comes to object storage.
[75.24 --> 78.84]  I've never in my life thought I would have so many opinions about object storage, but
[78.84 --> 79.38]  I do now.
[79.64 --> 83.88]  Tigris is a partner of Fly and it's S3 compatible object storage.
[83.88 --> 87.50]  That basically seems like it's a CDN, but it's not.
[87.60 --> 91.96]  It's basically object storage that's globally distributed without needing to actually set
[91.96 --> 93.02]  up a CDN at all.
[93.12 --> 95.90]  It's like automatically distributed around the world.
[96.22 --> 99.54]  And it's also incredibly easy to use and set up.
[99.70 --> 101.94]  Like creating a bucket is literally one command.
[102.18 --> 107.04]  So it's partners like that that I think are this sort of extra icing on top of Fly that
[107.04 --> 110.56]  really makes it sort of the platform that has everything that you need.
[110.56 --> 113.00]  So we use Tigris here at Changelog.
[113.12 --> 114.54]  Are they built on top of Fly?
[114.82 --> 118.00]  Is this one of those examples of being able to build on Fly?
[118.44 --> 118.66]  Yeah.
[118.82 --> 123.64]  So Tigris is built on top of Fly's infrastructure and that's what allows it to be globally distributed.
[124.04 --> 129.28]  I do have a video on this, but basically the way it works is whenever, like let's say a
[129.28 --> 132.50]  user uploads an asset to a particular bucket.
[132.62 --> 136.56]  Well, that gets uploaded directly to the region closest to the user.
[136.56 --> 140.16]  Whereas with a CDN, there's sort of like a centralized place where assets need to get
[140.16 --> 140.64]  copied to.
[140.76 --> 144.52]  And then eventually they get sort of trickled out to all of the different global locations.
[144.68 --> 148.82]  Whereas with Tigris, the moment you upload something, it's available in that region instantly.
[149.28 --> 152.78]  And then it's eventually cached in all the other regions as well as it's requested.
[153.20 --> 157.36]  In fact, with Tigris, you don't even have to select which regions things are stored in.
[157.46 --> 159.04]  You just get these regions for free.
[159.30 --> 162.48]  And then on top of that, it is so much easier to work with.
[162.48 --> 168.58]  I feel like the way they manage permissions, the way they handle bucket creation, making
[168.58 --> 173.40]  things public or private is just so much simpler than other solutions.
[174.02 --> 176.94]  And the good news is that you don't actually need to change your code if you're already
[176.94 --> 177.62]  using S3.
[177.78 --> 178.66]  It's S3 compatible.
[178.86 --> 181.56]  So like whatever SDK you're using is probably just fine.
[181.60 --> 183.10]  And all you got to do is update the credentials.
[183.34 --> 184.96]  So it's super easy.
[185.62 --> 185.92]  Very cool.
[185.98 --> 186.36]  Thanks, Annie.
[186.52 --> 188.82]  So Fly has everything you need.
[188.82 --> 193.68]  Over 3 million applications, including ours here at Changelog Multiple Applications,
[194.12 --> 195.32]  have launched on Fly.
[195.72 --> 201.62]  Boosted by global anycast load balancing, zero configuration private networking, hardware
[201.62 --> 207.28]  isolation, instant wire guard VPN connections, push button deployments that scale to thousands
[207.28 --> 207.86]  of instances.
[208.24 --> 210.16]  It's all there for you right now.
[210.58 --> 211.74]  Deploy your app in five minutes.
[211.88 --> 213.84]  Go to fly.io.
[214.24 --> 216.22]  Again, fly.io.
[218.82 --> 231.58]  Welcome to another episode of Practical AI.
[232.00 --> 233.76]  This is Daniel Whitenack.
[233.90 --> 239.98]  I am CEO and founder at Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[240.40 --> 243.92]  who is a principal AI research engineer at Lockheed Martin.
[244.28 --> 244.92]  How are you doing, Chris?
[244.92 --> 246.28]  Doing very well today, Daniel.
[246.34 --> 246.72]  How's it going?
[246.72 --> 255.68]  It's going extra wonderful today because if I think back over the past couple of years
[255.68 --> 263.28]  and the way that these shows that we produce together have also impacted my day-to-day work,
[263.50 --> 269.92]  one of the ones that has impacted me a lot and also I think been super beneficial, just
[269.92 --> 285.82]  super happy to have our guest from that show back who is now an AI engineer at Kuzu, Prashanth
[285.82 --> 286.10]  Rowe.
[286.68 --> 289.08]  Great to have you back on the show.
[289.66 --> 290.02]  Oh, yeah.
[290.12 --> 290.54]  Hi, Daniel.
[290.66 --> 291.10]  Hi, Chris.
[291.20 --> 292.44]  Very good to be back on the show again.
[292.44 --> 297.80]  Yeah, I've taught a lot of workshops over the past couple of years.
[298.12 --> 300.46]  I've done trainings with our customers.
[300.98 --> 302.26]  I've built things with our customers.
[302.88 --> 308.84]  And always when it gets down to vector databases, I'm like, hey, you know, anything I say,
[309.48 --> 311.58]  you can maybe learn some things from me.
[311.58 --> 317.04]  But if you really want to learn about vector databases and get the right sort of intuition,
[317.04 --> 322.62]  you really need to go to this series of blog posts on the data quarry, which is your blog,
[323.20 --> 327.24]  which was the first thing that I saw, which brought you originally on the show.
[327.34 --> 332.74]  We talked through vector databases and trade-offs between different types of vector databases
[332.74 --> 334.48]  and all of those things.
[334.74 --> 343.76]  Since that time, of course, you've moved on to a company, a data company, working in a different
[343.76 --> 348.38]  type of data, which we'll talk about today, but also is related to some of those things.
[348.72 --> 349.36]  So, yeah.
[349.38 --> 350.54]  How has the year been?
[351.34 --> 354.38]  Lots of updates and fun things it sounds like you're working on.
[354.94 --> 355.38]  Oh, absolutely.
[355.38 --> 361.32]  So I think I can summarize very briefly where I'm coming from since the last time we spoke,
[361.32 --> 363.60]  which was, I guess, just about a year ago.
[364.36 --> 370.14]  So as we spoke in our previous episode on vector databases, in 2023, I was working in
[370.14 --> 375.04]  the Royal Bank of Canada, and I spent most of that year thinking about vector search and
[375.04 --> 377.80]  the difference between the various database options there.
[378.20 --> 382.72]  And during that time, I was also simultaneously working on using graphs and graph databases.
[383.08 --> 385.80]  And I'll talk a little bit more about what they are and how they're useful.
[386.34 --> 390.80]  But as I was working on them, and I think I mentioned this even in the conversation we had
[390.80 --> 394.88]  last year is that I'm very interested in understanding how these two worlds come together.
[395.22 --> 399.22]  Because I know knowledge graphs and graphs have been around for a long time in their
[399.22 --> 399.76]  own space.
[400.30 --> 405.40]  And there was a huge hype around vector search and vector semantic search around this time
[405.40 --> 405.86]  last year.
[406.30 --> 411.52]  So there was a lot of scope, I guess, to understand how these two systems and these two methods
[411.52 --> 415.84]  can work better together in a way that we can build more advanced retrieval systems.
[415.84 --> 421.18]  So while I was thinking about those topics, I discovered new open source embedded graph
[421.18 --> 423.40]  database, Kuzu, which is where I now work.
[423.86 --> 428.16]  And I happened to meet the CEO, Semih Saliholu, at a local meetup in Toronto.
[428.60 --> 433.46]  And that got me really interested in what this tool and technology is all about, because I'd
[433.46 --> 434.82]  been using other graph databases.
[435.50 --> 439.46]  And when I discovered Kuzu, the fact that it's embedded and open source, which I'll talk
[439.46 --> 442.50]  a little bit more about, was very attractive to start with.
[442.50 --> 448.42]  So I spent my spare time outside of work experimenting with it and engaging with the developer team,
[448.50 --> 452.38]  as well as working with other people in the community in terms of understanding how they're
[452.38 --> 454.18]  using graph databases and graph tooling.
[454.86 --> 459.82]  So long story short, I realized at the end of last year that this was a great and fun
[459.82 --> 463.50]  opportunity for me to really go deep into the world of graphs and graph databases.
[464.28 --> 467.90]  And at the beginning of this year, I moved over and joined Kuzu as an AI engineer.
[467.90 --> 471.26]  And currently, I'm leading the developer relation efforts.
[471.54 --> 475.96]  And I'm engaging with the growing user community of Kuzu, which is really, really fun in itself.
[476.50 --> 480.74]  And of course, working with use cases that are taking this whole space forward and working
[480.74 --> 483.54]  with the community to understand what they are using these tools for.
[484.00 --> 487.54]  And I should also add, I'm still very plugged into the vector database ecosystem.
[487.78 --> 488.76]  I've not left that behind.
[489.26 --> 492.32]  And I'm actively experimenting with some of those in my spare time as well.
[492.60 --> 496.44]  And I still very much enjoy using LUNCEDB, which is the tool I mentioned last year in
[496.44 --> 497.36]  our conversation as well.
[497.92 --> 502.96]  So again, it's really exciting to see how these different kinds of tools are coming together.
[503.54 --> 506.48]  And yeah, I'd love to go deeper into some of these topics in our conversation.
[507.06 --> 507.40]  Fantastic.
[507.80 --> 514.28]  Yeah, the episode that we did last time with Lance and with the other vector database issues,
[514.46 --> 515.56]  that was a great episode.
[515.72 --> 519.96]  And if anyone isn't familiar with that, they definitely should go back and listen to that
[519.96 --> 520.52]  one as well.
[520.52 --> 526.54]  But just to lay a little bit of foundation here, some groundwork for those who may not
[526.54 --> 531.64]  be intimately familiar with graphs and how are they useful and applicable and such, could
[531.64 --> 536.18]  you kind of start us off with just, you know, what is a graph and why should we care about
[536.18 --> 537.68]  it and what's it going to do for us?
[538.12 --> 542.80]  So graphs are sometimes also known as knowledge graphs, and they're a great way to represent
[542.80 --> 545.30]  structured data via nodes and edges.
[545.30 --> 551.06]  The nodes are basically entities in the real world, like a person or a company, and the
[551.06 --> 556.82]  edges are relationships between these entities, like worked with or is CEO of and so on.
[557.22 --> 561.80]  Now, more formally, I also want to make the point here that the term knowledge graph is
[561.80 --> 565.84]  actually used to mean something slightly more involved than what I just described.
[566.36 --> 572.34]  Knowledge graph, in theory, can be used to express data that's quite hard to tabulate and store
[572.34 --> 572.88]  as records.
[572.88 --> 575.90]  It supports some logical reasoning over graphs as well.
[576.22 --> 579.28]  This is kind of what you would do when you store Wikipedia data, for example.
[579.66 --> 583.46]  But that's outside the scope of what we should go into for the purposes of this discussion.
[583.98 --> 588.98]  For most people and developer audience, the term graph and knowledge graph can be used
[588.98 --> 589.64]  interchangeably.
[589.90 --> 592.58]  So I just use them interchangeably for this discussion.
[592.68 --> 597.86]  It's kind of like distinguishing machine learning and AI to some degree.
[597.86 --> 604.88]  The edges, pun intended, don't matter that much in terms of their actual use.
[605.50 --> 608.70]  I want to direct you for one second before we get past the point.
[608.70 --> 615.48]  You did mention about graphs and briefly mentioned it in relation to a relational database.
[616.10 --> 621.34]  And just because they've been around so long and it's where a lot of people are starting
[621.34 --> 622.92]  from on relational databases.
[623.68 --> 629.88]  And you talked about the edges of the graph describing those relationships and being able
[629.88 --> 632.76]  to do that in some ways much better than a relational database can.
[632.76 --> 637.66]  Could you talk just for a moment so people can kind of make the jump from where they're
[637.66 --> 642.72]  at into this new tool and maybe think next time I'm going to leave whatever database
[642.72 --> 646.36]  I'm in, Postgres, you name it, and actually try a graph approach.
[646.76 --> 650.70]  Could you talk just for a second about what the difference there is and bring people along
[650.70 --> 651.18]  on that path?
[651.56 --> 655.94]  So I think we're going into the description of what a graph database is, right?
[656.34 --> 660.14]  So I'll just quickly, before I go into the database aspect of things, I just want to
[660.14 --> 664.52]  point out the benefit of what a graph is even useful for.
[664.72 --> 668.74]  Because most people need to understand what a graph is for, and then you think about where
[668.74 --> 669.28]  to store it.
[669.58 --> 669.96]  Great point.
[670.36 --> 675.14]  So I think I want to highlight that the benefits of graphs become obvious when you're looking
[675.14 --> 676.92]  at data itself that's highly interconnected.
[677.50 --> 683.86]  So for example, in medicine, you can have relationships between patients and symptoms of diseases, drugs
[683.86 --> 686.36]  that treat those diseases and their side effects.
[686.36 --> 689.44]  And these all have complex interweaving relationships with one another.
[689.44 --> 694.46]  Similarly, in finance, you can have chains of direct or indirect transactions, let's say
[694.46 --> 696.36]  between onshore and offshore accounts.
[696.98 --> 699.92]  And these ultimately connect to given individuals anywhere in the world.
[700.36 --> 705.74]  So you could choose to model these using tables in a relational database, or you could choose
[705.74 --> 707.86]  to model this as a graph in a graph database.
[708.60 --> 711.46]  And in either case, there are pros and cons.
[712.02 --> 716.84]  But specifically, when you're analyzing patterns and you want to actually understand these complex
[716.84 --> 721.04]  relationships in an analytical way, using a graph database can actually be very powerful.
[721.36 --> 722.22]  It's a lot more intuitive.
[722.48 --> 725.06]  It's much easier to construct the queries that can answer these questions.
[725.60 --> 729.36]  And this is where the idea of a graph and how you model the data as a graph becomes very,
[729.42 --> 729.76]  very powerful.
[730.42 --> 732.00]  But going back to the idea of databases.
[732.70 --> 737.78]  So a graph database can be thought of as a specialized database that allows you to scalably
[737.78 --> 740.38]  manage and query data that's organized as a graph.
[740.38 --> 745.30]  And the performance aspects of these graph databases come from specialized data structures
[745.30 --> 751.72]  and operators that allow you to express complex joins and efficiently traverse paths in your data.
[752.42 --> 755.18]  Now, a lot of listeners may have heard of graph databases already.
[755.64 --> 759.20]  And the most popular graph database model is called the Property Graph Data Model,
[759.66 --> 762.14]  which was invented and popularized by Neo4j.
[762.42 --> 764.56]  And I've been a user of Neo4j myself in the past.
[764.96 --> 769.76]  Today, you have many other graph databases like Kuzu that also implement the Property Graph Data Model.
[770.34 --> 775.36]  But in general, you start off with a data model, which is more conceptual,
[775.82 --> 779.30]  which allows you to express how to store and query your data.
[779.86 --> 785.08]  And a graph database basically is the underlying system that allows you to express the graph data model of choice.
[785.72 --> 791.10]  And the reason it's more intuitive than a relational database for certain kinds of queries
[791.10 --> 797.34]  that involve connected data and the sort of interrelated data is that it allows you to express your queries
[797.34 --> 799.30]  in a much more concise and intuitive manner.
[799.30 --> 805.32]  Using the query languages that graph databases offer, as well as the performance aspects of traversing the paths in the data.
[805.32 --> 814.26]  And just to sort of hone this in a concrete way, are you able to give a few examples?
[814.52 --> 819.44]  Like there's sort of the typical personnel-related things that you already mentioned,
[819.56 --> 827.54]  like Daniel is a node and he's CEO of Prediction Art, and that's another node, and there's organizations.
[827.54 --> 837.94]  Maybe for people that can't connect how such a structure would kind of be relevant to data that maybe they have in their enterprise,
[838.06 --> 843.48]  could you give just a couple other examples of data that could be represented as a graph
[843.48 --> 848.08]  in maybe in different verticals or that you've run across in your use cases with Kuzu,
[848.74 --> 852.86]  sort of data that's kind of beyond that kind of social network type of data, I guess.
[852.86 --> 859.64]  Absolutely. I think social networks get a little excessive credit for being the original graphs that we know about.
[860.10 --> 864.14]  Of course, they're very powerful and of course they're used, graphs are heavily used in social networks.
[864.58 --> 869.92]  But yeah, I think I mentioned an example of the medicine scenario which I described,
[870.04 --> 874.96]  which is you have not just individual persons or patients in a network,
[874.96 --> 880.70]  but you also have the drugs and the different symptoms of the diseases that are being treated by those drugs.
[881.14 --> 884.88]  Each of these can branch out into much more complex relationships themselves.
[885.60 --> 890.82]  And a lot of this data that you might imagine in a healthcare scenario or a biomedical scenario,
[891.18 --> 894.90]  this data pre-exists in structured form in many different sources.
[895.34 --> 900.34]  You might actually have medical records of people in a relational database or a data lake somewhere.
[900.34 --> 909.60]  A lot of existing workflows that work with these kinds of datasets tend to just stick with the database that is already used as a primary store.
[910.20 --> 915.26]  And many of those happen to be relational databases, which is fine because they're the most, I guess,
[915.42 --> 918.50]  efficient and convenient way to store this kind of data.
[918.74 --> 924.06]  When you have records of people, let's say what drugs they've been taking and what symptoms those drugs may cause and so on.
[924.06 --> 932.02]  So, I guess the idea here is that you can actually think of that very same data that exists in a relational database as a graph
[932.02 --> 939.04]  and store that in a graph database and apply your graph query logic in a way that allows you to answer specific questions
[939.04 --> 943.08]  that might have been quite complicated to answer using SQL in the relational database.
[943.62 --> 946.22]  So, that's one example of, let's say, a healthcare scenario.
[946.66 --> 952.64]  I've already mentioned the financial transaction scenario where you have a transaction graph between individuals,
[952.64 --> 959.62]  the merchants they've interacted with, the money transfers they've made between their accounts, how these accounts are connected.
[960.04 --> 964.92]  So, financial institutions make heavy use of graphs to answer these kinds of questions.
[965.36 --> 967.74]  Traffic networks is another common use case.
[968.16 --> 975.42]  If you're working with city authorities and you want to understand the flow of traffic and the numbers of people moving between locations,
[975.94 --> 978.30]  this is something that can actually be well modeled in a graph.
[978.30 --> 984.36]  And the kinds of questions you can answer can also change based on whether you choose to model this as tables or as a graph.
[984.86 --> 986.26]  And there are many, many other examples.
[986.70 --> 988.14]  I will highlight one thing, though.
[988.44 --> 998.44]  The example of Wikipedia that I gave earlier, the idea of Wikipedia as a graph, I think, reinforces the idea that knowledge graphs are a term to be used,
[998.44 --> 1005.38]  I guess, with a bit of caution in the sense that, in general, a graph is a general representation of how nodes and entity,
[1005.52 --> 1007.54]  like nodes are connected to other nodes in the network.
[1008.04 --> 1014.04]  A knowledge graph is something that you can think of as the collection of all knowledge that is available in that domain.
[1014.58 --> 1020.84]  And in the case of Wikipedia, you can imagine that there are certain scenarios where it's quite hard to tabulate every bit of information.
[1020.84 --> 1028.40]  As an example, if you have, I don't know, the current president of the U.S. is Joe Biden.
[1028.88 --> 1037.62]  So based on the current political structure and the different parties that Joe Biden represents and all the other people represented in those parties,
[1037.84 --> 1042.74]  and then the relationship between a party and a state, the relationship between the state and the country,
[1042.74 --> 1055.74]  you can imagine that this becomes a very complicated branching sort of structure and not all of it renders very well in a table because you can't imagine like one table that connects to another table when you have this kind of complicated data.
[1056.28 --> 1064.44]  So there are certain scenarios where actually the data model and the way you build your graph can actually really have a big impact on the kinds of questions you can ask of your data.
[1064.92 --> 1069.26]  So that's why I tend to use the term knowledge graph in a bit more specialized way.
[1069.26 --> 1082.20]  In general, I would say that you can think of your tabular data or records as a graph very conveniently using the property graph model and model things like transaction networks and social networks and drug interaction networks and so on.
[1082.20 --> 1098.46]  What's up, friends?
[1098.56 --> 1104.42]  I'm here with a new friend of ours over at Assembly AI, founder and CEO Dylan Fox.
[1104.86 --> 1106.72]  Dylan, tell me about Universal One.
[1106.72 --> 1110.52]  This is the newest, most powerful speech AI model to date.
[1110.52 --> 1111.88]  You released this recently.
[1112.24 --> 1112.72]  Tell me more.
[1113.12 --> 1120.98]  So Universal One is our flagship industry leading model for speech to text and various other speech understanding tasks.
[1121.32 --> 1123.16]  So it's about a year long effort.
[1123.56 --> 1132.46]  That really is the culmination of like the years that we've spent building infrastructure and tooling at Assembly to even train large scale speech AI models.
[1132.46 --> 1141.10]  It was trained on about 12 and a half million hours of voice data, multilingual, super wide range of domains and sources of audio data.
[1141.20 --> 1142.34]  So it's super robust model.
[1142.52 --> 1155.90]  We're seeing developers use it for extremely high accuracy, low cost, super fast speech to text and speech understanding tasks within their products, within automations, within workflows that they're building at their companies or within their products.
[1155.90 --> 1167.62]  Very cool. So Dylan, one thing I love is this playground you have. You can go there, assemblyai.com slash playground, and you can just play around with all the things that is Assembly.
[1167.84 --> 1172.96]  Is this the recommended path? Is this the try before you buy experience? What can people do?
[1172.96 --> 1184.76]  Yeah, so our playground is a GUI experience over the API that's free. You can just go to it on our website, assemblyai.com slash playground. You drop in an audio file, you can talk to the playground.
[1185.10 --> 1194.24]  And it's a way to, in a no code environment, interact with our models, interact with our API to see what our models and what our API can do without having to write any code.
[1194.24 --> 1208.24]  Then once you see what the models can do and you're ready to start building with the API, you can quickly transition to the API docs, start writing code, start integrating our SDKs into your code to start leveraging our models and all our tech via our SDKs instead.
[1208.80 --> 1215.62]  Okay. Constantly updated speech AI models at your fingertips. Well, at your API fingertips, that is.
[1215.62 --> 1221.26]  A good next step is to go to their playground. You can test out their models for free right there in the browser.
[1221.26 --> 1226.92]  Or you can get started with a $50 credit at assemblyai.com slash practical AI.
[1227.36 --> 1231.66]  Again, that's assemblyai.com slash practical AI.
[1231.66 --> 1255.78]  Well, Prashant, before we get into one thing that I'm really excited to talk about on the show, which I've been telling Chris we need to talk about for a while, which is GraphRag.
[1255.78 --> 1271.62]  But before we get there, we sort of talked a bit about graphs. I think it would be useful to kind of just give people a reminder of the kind of what most people would refer to maybe when they're referring to a RAG workflow, an AI RAG workflow.
[1271.62 --> 1281.16]  I was at a CIO dinner last night, and one of the speakers is like, we all hear about the RAG and the RAG and the RAG and RAG and RAG.
[1281.16 --> 1289.54]  And everybody's hearing about these things, but maybe it's worth just a quick 30-second, one-minute reminder.
[1289.54 --> 1297.38]  So when most people are referring to the RAGs or the RAG workflow, what are they referring to?
[1297.86 --> 1302.08]  Yeah, this is a very fascinating topic. I think about RAG a lot.
[1302.48 --> 1308.42]  So let me just, I think, take a step back and describe the term itself.
[1308.42 --> 1312.02]  So the term RAG itself is really interesting to me.
[1312.50 --> 1315.28]  As we know, it stands for Retrieval Augmented Generation.
[1315.84 --> 1322.20]  The key thing to note here is that the term RAG emerged prior to the emergence of the term LLM.
[1322.74 --> 1330.86]  And it's come as a result of generative language model improvements that came, I think, in the end of 2019, early 2020 time period.
[1330.86 --> 1340.04]  And there were two papers that came around in early 2020, one by Google and another by Facebook Research that introduced the term Retrieval Augmented Generation.
[1340.52 --> 1342.76]  Now, note that retrieval itself is not new.
[1343.06 --> 1346.24]  We know information retrieval is a field that's been around for decades.
[1346.96 --> 1351.80]  So, and we've also had systems that can do keyword-based information retrieval for decades.
[1352.48 --> 1358.66]  So what is new right now is the fact that generative models, generative models have become much better than they used to be.
[1358.66 --> 1361.16]  So the generation capability is what's new.
[1361.50 --> 1367.48]  So when you look at the term RAG, the term Retrieval Augmented comes before the term Generation in that acronym.
[1368.22 --> 1374.74]  So I hope that makes it clear as to the fact that the generation part is what we are stressing is the novel aspect of it.
[1375.20 --> 1383.56]  Now, in 2020, the way RAG was done was to combine sequence-to-sequence language model, which was the standard way of doing language modeling back then.
[1383.78 --> 1386.66]  And those models could generate text quite convincingly.
[1386.66 --> 1390.88]  And you combine those models with the retrieval capabilities of dense embeddings.
[1391.26 --> 1397.00]  And the Facebook research paper that introduced the term RAG based their work on dense embeddings of Wikipedia articles.
[1397.64 --> 1403.00]  Now, you had the initial makings of vector embedding-based retrievals that we are taking for granted today.
[1403.44 --> 1405.88]  And later in 2020, GPT-3 was released.
[1405.88 --> 1409.46]  So you had the coinage of the term LLM, or large language model.
[1409.98 --> 1418.08]  And you could think of GPT-3 as one of the first large language models that really extended the capabilities of pre-existing models at that time.
[1418.46 --> 1427.08]  But what really made RAG take off, in my opinion, from 2021 and beyond, was the arrival of this whole host of new systems that we call vector databases.
[1427.08 --> 1433.68]  And they began offering specialized features to make retrieval from these dense embeddings far easier and also more scalable.
[1434.14 --> 1438.94]  And this is what led to the explosion of all those vector database companies that we discussed about last year.
[1438.94 --> 1445.40]  And I hope this gives some context as to the term RAG itself and how, I guess, it grew to what it has become today.
[1446.30 --> 1449.98]  So I guess we've been teasing this for a while on the show here.
[1450.12 --> 1451.72]  We've talked about graphs.
[1451.84 --> 1454.20]  We've talked a little bit about RAG to get people.
[1454.98 --> 1459.54]  Everyone's waiting for us to ask you the question about, you know, graph RAG and get into the topic.
[1459.54 --> 1465.50]  So without further ado, if you want to dive in and kind of give us an intro to that, we'd love to hear that.
[1465.98 --> 1466.26]  Absolutely.
[1466.68 --> 1470.18]  So let's understand what we were doing with RAG and then go into graph RAG.
[1470.44 --> 1470.60]  Yep.
[1470.70 --> 1475.72]  So the early approach to doing RAG is, we call it naive RAG now.
[1476.24 --> 1479.42]  And in that approach, you just create chunks of your data.
[1479.66 --> 1482.20]  You embed that using an embedding model.
[1482.50 --> 1484.30]  And you store them in a vector database.
[1484.72 --> 1489.18]  So essentially, you just store the chunks on the chunk embeddings in a vector database.
[1489.54 --> 1497.00]  And when you do a retrieval, you convert your query into an embedding model using the same embedding model that you used to embed the data.
[1497.48 --> 1502.28]  And this returns the most similar chunks that are similar to the query vector.
[1502.28 --> 1507.04]  So you typically return like the top K, like let's say top 5 or top 10, whatever number you choose.
[1507.62 --> 1513.96]  And these top K chunks can then be sent to the LLM as context to synthesize a response in natural language.
[1514.54 --> 1517.50]  So in a nutshell, that's kind of what you could say traditional RAG does.
[1517.50 --> 1521.40]  Now on paper, this naive approach to doing RAG is great.
[1521.92 --> 1524.68]  But it quickly became obvious that this has limitations.
[1525.22 --> 1530.14]  The first limitation is that the dense embeddings are typically done at the sentence level.
[1530.84 --> 1533.10]  And many user queries use keywords.
[1533.60 --> 1537.58]  And keyword-based search methods like BM25 can do a fair job at this.
[1537.64 --> 1538.78]  And they've been around for a long time.
[1538.78 --> 1546.74]  So towards the end of last year, you could see a lot of these vector database vendors starting to offer a combination of hybrid search methods.
[1547.04 --> 1557.14]  And the term hybrid search itself is becoming more popular, where you perform both keyword-based search, which is a form of sparse vector search, with dense vector search, which is a search via dense embeddings.
[1557.14 --> 1562.36]  And you pass the retrieve chunks from either of these approaches to a re-ranker module.
[1562.66 --> 1568.72]  So you had specialized modules that do re-ranking that give you the most relevant chunks from either of these retrievals.
[1569.24 --> 1574.00]  And this is how you combine the sparse and dense vectors into what you call a hybrid search.
[1574.00 --> 1581.76]  Now, even hybrid search can have its limitations, which is, I guess, where people began exploring further options earlier this year and maybe beyond.
[1582.38 --> 1588.40]  Because neither sparse nor dense embeddings can capture explicit relationships between entities very well.
[1588.72 --> 1590.44]  And I'll demonstrate this with an example.
[1590.78 --> 1595.32]  In certain cases, you can really benefit by modeling some of these entities explicitly.
[1595.78 --> 1602.26]  So let's look at an example of a professor and, let's say, the PhD students the professor is advising.
[1602.26 --> 1610.04]  So let's say you had a block of text which is talking about the students and the professor and a bunch of other things related to their work in the university.
[1610.56 --> 1616.26]  So in natural language, we understand the relationship between the professor and the student as follows.
[1616.82 --> 1619.30]  Student X worked with professor Y.
[1619.68 --> 1623.58]  Because we know that the act of being a student of a professor means that you worked with them.
[1624.06 --> 1626.84]  But in the text itself, you may not have expressed it that way.
[1626.98 --> 1629.28]  The text may be written as so-and-so.
[1629.38 --> 1631.70]  Person X was a student of person Y.
[1631.70 --> 1635.98]  Now, if you try to search this using the query, who did X work with?
[1636.64 --> 1639.06]  This is a very intuitive question in natural language.
[1639.46 --> 1641.48]  We humans immediately can put two and two together.
[1641.70 --> 1646.74]  That work with and student relationship are more or less semantically similar here.
[1647.18 --> 1654.44]  So we are able to piece together this information and know that a person was a student of someone and inherently they worked with that person.
[1654.44 --> 1664.72]  However, if you try to search for this using vector search, the dense embedding may not capture the relationship correctly where student of isn't close enough to work with in the vector space.
[1665.28 --> 1671.42]  So your vector search alone may not retrieve this answer because you didn't model the relationships in that explicit way.
[1671.42 --> 1682.04]  However, if you had chosen to model this as a graph, you would explicitly capture this relationship using this concept of a triple, which is person X worked with person Y.
[1682.04 --> 1684.62]  So this is the idea of where triples come in.
[1684.66 --> 1688.14]  A triple essentially is two nodes that are connected via a relationship.
[1688.42 --> 1689.60]  You have a source and a target.
[1690.28 --> 1693.34]  And the person X is a source, person Y is a target.
[1693.68 --> 1696.32]  And the worked with is what represents the relationship.
[1696.32 --> 1717.66]  So the very powerful idea here is that where graphs come into this whole picture and why it's relevant to RAG is that you can actually provide additional valuable context to an LLM by modeling these relationships explicitly and simultaneously retrieving both from a dense embedding vector search as well as a graph traversal.
[1717.66 --> 1729.70]  And then using the retrievals in combination with one another to provide additional context to the generation LLM so that you can actually include this explicit relationship in your answer.
[1730.06 --> 1733.76]  And this actually has been proven in practice from some work that's been done recently.
[1734.50 --> 1735.44]  I want to ask a question.
[1735.54 --> 1745.96]  It may be a bit of a stretch, but could, as you were describing that, that failure of making those explicit, if you're doing that, could that lead to hallucination in terms of your output from the model?
[1745.96 --> 1748.34]  Because it's not able to make that explicit.
[1748.86 --> 1752.42]  And so it's still trying to provide information that comes up with whatever it comes up with.
[1752.56 --> 1754.40]  Is that a possibility there?
[1754.72 --> 1755.74]  That's a very fair point.
[1755.90 --> 1757.18]  And you're absolutely right.
[1757.50 --> 1760.06]  Hallucination, I think, is definitely a high possibility.
[1760.20 --> 1762.72]  Or, like, it's definitely likely in certain scenarios.
[1763.16 --> 1767.32]  You obviously cannot predict when hallucination happens, which is a big issue in general with LLMs.
[1767.86 --> 1771.82]  Now, I think I definitely want to expand on this a little bit.
[1771.82 --> 1782.96]  But the selling point for graph rag, by the way, the process I was just talking about before is essentially what you could loosely define as graph rag, where you bring a graph as part of the retrieval process.
[1782.96 --> 1794.40]  Now, the so-called, I guess, benefit of graph rag, as it was, you could say, marketed in the last several months by various sources, is the fact that it reduces hallucinations.
[1794.92 --> 1806.96]  And it's important to note that whenever context is provided to an LLM for the purposes of generation, essentially you provide a prompt, and the prompt is what LLM uses to provide a response.
[1806.96 --> 1812.94]  In the event of providing such a prompt, it's always possible that at some point of time you will have a hallucination.
[1813.10 --> 1817.00]  It doesn't matter whether the information came from a graph or the information came from a vector retrieval.
[1817.32 --> 1819.10]  The source of the information is irrelevant.
[1819.74 --> 1825.30]  So the very act of using an LLM to generate text means that there is an inherent chance of hallucination.
[1825.78 --> 1829.96]  So I wouldn't state that the benefit of graph rag is that it eliminates or reduces hallucination.
[1829.96 --> 1844.32]  What I would state the benefit is, is that it actually increases the chance of factual accuracy in the sense that a relationship that was not explicitly captured in this vector embedding is now explicitly captured in the graph.
[1844.84 --> 1851.72]  And by providing both these pieces of context to the LLM, you're essentially increasing the chances of a factually correct or a more relevant response.
[1851.72 --> 1858.56]  Yeah, so one of the things I'm thinking about is people might have some thoughts in their mind.
[1858.70 --> 1866.72]  Like I know maybe people have built some sort of naive rag system or maybe even implemented some advanced rag methodologies.
[1867.48 --> 1870.68]  But most of the time what they've had is a sort of set of documents.
[1870.86 --> 1873.02]  Like you say, they split up into chunks.
[1873.22 --> 1874.56]  They embed those.
[1874.68 --> 1879.70]  They retrieve one or more chunks, maybe even in a hybrid way or in some advanced way.
[1879.70 --> 1884.86]  But here you're saying you're combining the vector approach and the graph approach.
[1885.06 --> 1889.76]  I'm wondering if you could break down very concretely for us the data side.
[1889.90 --> 1900.12]  So if I have like documents or if I have internal data, what I would need to have in place and how I would construct the data side to be ready to do graph rag.
[1900.12 --> 1911.18]  And then at the time that I, let's say I receive a user query question in my chat bot or whatever that is, what is actually kind of concretely retrieved?
[1911.30 --> 1915.74]  And how is that combined or how could that be combined with the prompt into the model?
[1915.88 --> 1920.42]  So just walking us through that, those kind of very concrete things might be helpful for people.
[1920.42 --> 1922.18]  Sure. That makes a lot of sense.
[1922.76 --> 1933.96]  So the two key stages in any rag application, not just graph rag, is the fact that you divide it into an indexing stage and a retrieval or a serving stage.
[1934.28 --> 1939.68]  So to get the data in and store it and index it is what we call as indexing stage.
[1939.68 --> 1948.08]  So this is the stage that is upfront or upstream where you have data that already exists in different structured or unstructured sources.
[1948.60 --> 1966.56]  Now you could apply a variety of techniques, including using NLMs itself for the stage where you could extract the entities or you could say named entities from the unstructured data or structured data that already exists and store them as entities or nodes in a graph database.
[1966.56 --> 1970.92]  And simultaneously, you can also extract relationships from this unstructured text.
[1971.00 --> 1973.60]  There are many different methods that you could use to extract the relationships.
[1974.30 --> 1988.02]  Now, what I've noticed in recent times is a lot of these recent papers are using LLMs to help with this information extraction step where you actually use the LLM to extract portions of your chunks.
[1988.02 --> 2000.18]  And then from those portions, you further refine it and say, OK, from this block of text, tell me what are the triples, which is nodes connected to other nodes by a relationship, exist in that block of text.
[2000.88 --> 2006.04]  So once all these triples are extracted, they're essentially stored in a graph database.
[2006.04 --> 2012.34]  And simultaneously, you can also have a parallel pipeline that stores the vector embeddings in a vector database.
[2012.80 --> 2019.54]  In some cases, you can have both the vectors as well as a graph entities sitting in the same database.
[2019.96 --> 2021.52]  Certain databases have those features.
[2022.12 --> 2024.92]  In other cases, you may not want to have them both in the same database.
[2025.00 --> 2029.98]  You may want to leverage the graph database for its strengths and the vector database for its strengths.
[2030.48 --> 2034.18]  And you may also have pre-existing workflows that already have the data in those systems.
[2034.18 --> 2043.16]  So it's perfectly valid to have your independent sources of data move the respective datas into those respective databases.
[2043.48 --> 2048.70]  For example, your graph entities would go into your graph database and the vector embeddings would go into a vector database.
[2049.12 --> 2056.62]  Downstream of this, you could do additional post-processing, like linking the chunk reference IDs to individual entities in the graph.
[2057.00 --> 2063.48]  Essentially, the node that represents an entity in the graph can have an ID that links it back to which chunk it is a part of.
[2063.48 --> 2069.34]  So that when you retrieve a particular chunk, you can actually point to which entities are existing in that chunk.
[2069.68 --> 2076.02]  So these are a lot of additional upfront steps that people are doing to construct both the graph as well as the vector store.
[2076.52 --> 2083.66]  And once this indexing stage is complete, the retrieval stage can actually begin, which is the stage that we are very familiar with.
[2083.78 --> 2086.54]  You have a user query that comes in in natural language.
[2086.54 --> 2089.10]  You transform that into an embedding.
[2089.42 --> 2096.24]  You find a similarity search on that embedding, which returns the most similar vectors from the vector database.
[2096.68 --> 2107.02]  And then simultaneously, you can also use whatever methods you have to translate that query into a graph query and retrieve the entities and relations from the graph that answer that same question.
[2107.02 --> 2113.88]  And then use a re-ranker to combine the retrievals in a way that provides additional context to the LLM for generation.
[2114.36 --> 2119.86]  So again, just to summarize, the two key stages in the RAG pipeline include indexing and serving.
[2120.40 --> 2126.84]  And each of these stages has a suite of tools that you can use to help the user achieve the required outcome.
[2126.84 --> 2141.04]  Well, our friends over at Speakeasy have the complete platform for API developer experience.
[2141.18 --> 2146.68]  They can generate SDKs, Terraform providers, API testing, docs, and more.
[2146.68 --> 2155.16]  And they just released a new version of their Python SDK generation that's optimized for anyone building an AI API.
[2155.16 --> 2169.00]  Every Python SDK comes with Pydantic models for requests and response objects and HTTPX client for async and synchronous method calls and support for server sent events as well.
[2169.56 --> 2175.58]  Speakeasy is everything you need to give your Python users an amazing experience integrating with your API.
[2176.32 --> 2179.80]  Learn more at speakeasy.com slash Python.
[2180.10 --> 2183.72]  Again, speakeasy.com slash Python.
[2185.16 --> 2200.16]  So I am, here we are after break.
[2200.16 --> 2205.42]  I am still thinking about what you were telling us going into break and trying to grok it myself.
[2205.42 --> 2219.54]  And I'm kind of thinking about how I can use it in a practical sense to help me get it down and kind of get it from the notional sense into more of a practical thing that I can go do after we stop talking on the podcast.
[2219.92 --> 2221.38]  Can you give me like an example?
[2221.86 --> 2230.56]  Something really hands on that folks out there might be doing that really puts it into that, okay, I get it.
[2230.56 --> 2232.44]  Now I'm going to go do it kind of context.
[2232.64 --> 2237.02]  I actually have a repo that I can share once we're done with this conversation.
[2237.38 --> 2240.34]  And I would love for people to pick this up and experiment with it.
[2240.72 --> 2247.52]  And obviously, because I work at a company that builds a graph database, I'm very eager to talk to users who are using these kinds of tools.
[2247.52 --> 2256.56]  So for my experiment, I've used Kuzu as a graph database and LanceDB as a vector database, because each of these, as I mentioned, have their own benefits in their domains.
[2257.30 --> 2260.76]  And a practical example that I want to demonstrate is this.
[2261.24 --> 2269.78]  So the data set I'm thinking about, which I can showcase in the repo, is you have a block of text about the scientist, Madam Curie.
[2269.78 --> 2275.42]  You know, she discovered radium and polonium and she won two Nobel Prizes and she was related to Pierre Curie.
[2275.68 --> 2276.38]  They were spouses.
[2277.10 --> 2280.74]  And she also was related to other scientists in the whole ecosystem.
[2281.40 --> 2289.82]  So I have a text sample that contains Madam Curie's contributions to science and the relationships that existed in her life.
[2290.14 --> 2291.96]  So this is unstructured text.
[2292.44 --> 2294.92]  So the first step is we can do two things here.
[2294.92 --> 2302.10]  We can do the conventional naive rag retrieval, where I try to ask a question, who did Pierre Curie work with?
[2302.70 --> 2304.38]  And that's a very simple question to answer.
[2304.96 --> 2309.24]  And a vector search will definitely give you an answer if you embed the text and do the required steps.
[2309.80 --> 2314.56]  So what I notice in this data set is there is an implicit relationship.
[2314.68 --> 2318.00]  And this is why I gave that example earlier about the professor and the students.
[2318.00 --> 2328.38]  There is one particular person in this data set, Paul Langevin, who was a student of Pierre Curie and who later had a relationship with Marie Curie after Pierre Curie passed away.
[2328.92 --> 2333.16]  So it's mentioned in the text that Paul Langevin was a student of Pierre Curie.
[2333.84 --> 2336.64]  Now, the question asks, who did Pierre Curie work with?
[2336.88 --> 2341.32]  We obviously know that Pierre Curie worked with Madam Curie to find or discover these elements.
[2341.82 --> 2345.52]  Now, we also know implicitly that Pierre Curie worked with Paul Langevin, who was his student.
[2345.52 --> 2353.40]  The vector search, if you naively chunk these and store them in a vector database, which I do in LanceDB, gives me one of the answers.
[2353.62 --> 2355.48]  It gives me Marie Curie worked with Pierre Curie.
[2355.86 --> 2367.44]  But the graph search, because of the fact that I explicitly insert the relationship, and I have some code that shows how the information was extracted from the unstructured data using the Lama Index framework.
[2368.00 --> 2372.38]  So it's very intuitive and easy to begin experimenting once you actually install the required packages.
[2372.38 --> 2381.96]  So what I'm getting at here is, in the graph, I was able to retrieve both the answers, like Paul Langevin as well as Marie Curie, who worked with Pierre Curie.
[2382.60 --> 2392.68]  And rather than just using the result from the graph, there may be other scenarios where my question may have been a little bit more vague or fuzzy, and a vector search might have given me a better result.
[2392.68 --> 2396.88]  I'm sure if you tinker with the dataset and the questions here, you'll find such examples.
[2397.28 --> 2403.08]  So what I've done is, I've included a re-ranker downstream of the vector search and the graph search.
[2403.64 --> 2415.64]  And when I retrieve the result and pass it as context to the LLM, I'm adding that re-ranker step so that I get the most relevant graph search results, as well as the most relevant vector search results.
[2415.64 --> 2419.78]  In this case, the vector search missed one of the entities, but the graph search captured it.
[2420.40 --> 2428.46]  So the combined context from both these retrievals allowed me to get the generator model to actually give me the correct response.
[2429.34 --> 2435.62]  And if you want to experiment more with this, I think it's pretty straightforward to come up with other queries that will show the reverse result to be true,
[2435.72 --> 2441.20]  where the semantic match between the vector search and the query might be closer.
[2441.20 --> 2446.42]  You might get a more relevant result from the vector search and the graph search missed the result because of a mismatch.
[2446.96 --> 2448.88]  So that's kind of where I'm going at here.
[2449.18 --> 2455.16]  There are many ways you can combine vector search and graph reversals to improve the retrieval accuracy.
[2455.68 --> 2460.02]  So I'd love for the community to think about these individual parts.
[2460.38 --> 2464.82]  I think my biggest takeaway from what I've seen in the last few months of reading the literature
[2464.82 --> 2474.90]  and talking to people who are questioning what graph rag is, is that people tend to think of graph rag as like a graph based solution alone.
[2475.30 --> 2485.88]  Whereas the more I think about it, I think that the two approaches of using dense vector retrieval and using graphs kind of go hand in hand for the purposes of rag.
[2485.88 --> 2494.00]  All this being said, there are a lot of, I guess, conflicting articles that you may see online and blog posts claiming that this is the way to do graph rag.
[2494.22 --> 2503.60]  The key takeaway for everyone should be think of it as a suite of tools and methodologies that come together to enhance retrieval in a way that you can get better generation.
[2503.60 --> 2511.56]  I would love to maybe double click on one of the things that you mentioned, which I had in my mind and I think other people might have in their mind,
[2512.06 --> 2520.36]  mainly because I don't know how many years ago it was, five or six years ago, I was doing some graph related data work.
[2520.98 --> 2522.92]  And I know I looked at a lot of things at that time.
[2523.00 --> 2529.48]  There was even a whole area of research called automatic or automated knowledge graph creation.
[2529.48 --> 2540.28]  And there's sort of this idea that, you know, if once you have a graph, there's so much that is opened up to you in terms of querying and the rich structure and all of that.
[2540.40 --> 2545.78]  But sometimes it can be daunting to construct the graph in the first place.
[2545.78 --> 2548.80]  And you mentioned kind of this nice tooling around Lama Index.
[2549.18 --> 2556.46]  And of course, we had Jerry on the show in the past and such an amazing project there that's helping many people.
[2556.46 --> 2559.38]  But I'm wondering if I could double click on that point.
[2559.60 --> 2569.24]  Like what has been your experience kind of current state in terms of how much work and how hard it is to do that graph construction piece?
[2569.46 --> 2576.90]  In addition to because I think one of the things people love about RAG, right, is you just kind of put a bunch of documents in and hands off.
[2577.00 --> 2579.84]  You construct these chunks and oh, cool.
[2579.90 --> 2582.60]  Like you get some some nifty things out of it.
[2582.60 --> 2593.16]  Of course, there's the element that you you highlighted, which is sometimes it's hard for people to get that last bit of performance that isn't captured by naive RAG.
[2593.26 --> 2596.60]  But yeah, on that on that graph data construction piece.
[2596.70 --> 2596.84]  Yeah.
[2596.88 --> 2598.42]  How does that look right now?
[2598.50 --> 2600.12]  And what have you found to be useful?
[2600.12 --> 2601.86]  You hit the nail on the head.
[2602.08 --> 2612.76]  I think the biggest issue that people I speak to are having in relation to both graph RAG and in general using graphs is how do you create the graph from existing data that you have in other forms?
[2613.48 --> 2618.70]  And yeah, I was exactly going to touch upon this anyway as my next point, which is graph RAG is by no means perfect.
[2619.12 --> 2623.00]  And the most significant challenge is indeed around graph construction.
[2623.36 --> 2626.96]  Now, there's two things regarding graph construction that we can delve into.
[2626.96 --> 2638.22]  The first is that the quality of the graph is absolutely paramount because as we know in any RAG system, the quality of your retrieval greatly impacts the quality of the generation downstream.
[2638.48 --> 2643.42]  Like a poor retrieval with garbage results is going to result in a garbage output from the generation model.
[2644.08 --> 2651.82]  So first of all, we have to stress on the fact that to get the most out of graph RAG, we need a high quality graph.
[2651.82 --> 2657.44]  But then you go one step further back, which is how do you even get a graph from unstructured text?
[2658.12 --> 2668.30]  So as you mentioned, Lama Index and I think Langchain as well, some of these frameworks offer valuable tooling to help you extract triples or entities and relationships from unstructured text.
[2668.72 --> 2670.86]  And they do this primarily through the use of LLMs.
[2671.26 --> 2678.60]  But as we know, LLMs themselves have issues with hallucinations or they just have issues in general with reproducibility.
[2678.60 --> 2682.82]  You are not guaranteed to get the same results if you run the same LLM multiple times.
[2683.00 --> 2689.44]  And although some APIs provide seeds where you can control the reproducibility, that still doesn't mean that it's not random.
[2689.72 --> 2692.30]  The output of an LLM is still more or less unpredictable.
[2692.70 --> 2701.52]  So there are a lot of other parallel works going on that are not using LLMs to extract triples from an unstructured text source.
[2702.08 --> 2704.82]  And I can talk about a few of those that I found really exciting.
[2704.82 --> 2707.90]  And in fact, that's kind of the stuff I've been exploring in this space.
[2708.00 --> 2710.16]  And I'd love to chat with people who have been doing this as well.
[2710.94 --> 2713.86]  So there are custom machine learning models coming out.
[2714.18 --> 2716.88]  One of them is called Rebel, which is R-E-B-E-L.
[2717.60 --> 2723.34]  And it's been around for a while, but I think they're upgrading their internals now for a newer version.
[2724.02 --> 2729.78]  So that's a model that's trained explicitly for the purposes of extracting triples for the purposes of a graph.
[2729.78 --> 2733.14]  And there's another model, I think, called Relic, R-E-L-I-K.
[2733.74 --> 2737.12]  That's also an open source model that's been released recently.
[2737.60 --> 2741.76]  And people have been using it to extract relationships from unstructured text.
[2742.16 --> 2744.64]  Now, it's not to say that these are mature models.
[2744.78 --> 2746.84]  It still requires a little bit of coercing.
[2747.24 --> 2750.96]  And people need to understand their outputs and what they're getting from them.
[2751.30 --> 2757.34]  But the idea here is that these models are, I guess, more controllable in what you can output from them.
[2757.34 --> 2759.72]  It's not like an LLM where you just don't know what you're going to get.
[2760.20 --> 2765.38]  And, of course, I think because of the fact that they're small models, you can actually use them at scale on very large data.
[2765.78 --> 2767.56]  So that's one angle of things.
[2767.88 --> 2770.92]  I'm sure a lot of users have heard of the NLP library, Spacey.
[2771.46 --> 2773.50]  And I've been using Spacey for many years myself.
[2773.64 --> 2775.08]  It's a very, like, it's an amazing library.
[2775.52 --> 2780.34]  On its own, Spacey doesn't have the tools to extract relationships and entities from text.
[2780.38 --> 2784.18]  Of course, you can extract named entities or named entity recognition, NER.
[2784.18 --> 2790.10]  But recently, there have been some add-on modules or libraries that plug into Spacey.
[2790.54 --> 2794.20]  Two of them, which I'll name here, they're called Gliner and Glyrel.
[2794.46 --> 2797.04]  G-L-I-N-E-R and G-L-I-R-E-L.
[2797.56 --> 2801.66]  And as their name suggests, one of them is for extracting named entities from text.
[2801.72 --> 2804.98]  And the other one is for extracting explicit relationships from text.
[2805.24 --> 2811.04]  But they plug into the underlying Spacey tokenizer and the underlying Spacey representation of the data.
[2811.04 --> 2813.58]  So I feel like it's a lot more usable.
[2813.88 --> 2816.80]  And there are some experimental notebooks that I've been working on.
[2816.88 --> 2824.28]  And I'm going to be experimenting more on this to see how they compare in relation to using just LLMs alone to extract data.
[2824.46 --> 2826.84]  So, yeah, I think this is a very active space.
[2827.06 --> 2830.64]  And there is no right answer in terms of how you can use these tools.
[2830.64 --> 2839.56]  But I feel like there's enough options and methods out there that people don't have to feel that I'm relying on, you know, completely black box, unreliable LLM to do things.
[2840.30 --> 2842.56]  What you've covered so far is really fascinating to me.
[2842.62 --> 2845.32]  And I'm learning a lot in this conversation.
[2845.32 --> 2858.92]  As we're kind of winding up on this, you know, and we've been covering, you know, GraphRag as well as the components that make that up and kind of talking about how to combine vector search, graph search.
[2859.16 --> 2866.56]  And it feels like a, you know, a brave new world that we're leaping into, even for the AI topic, which is that way anyway.
[2867.34 --> 2868.04]  Where's this going?
[2868.26 --> 2872.80]  Like where do you envision this going over various timelines in the future?
[2872.80 --> 2874.80]  You know, things are happening at light speed.
[2874.92 --> 2877.20]  So you just go a few months and there's a lot of change.
[2877.36 --> 2883.56]  But if you could maybe pick a couple of points out and tell us kind of what you think might happen.
[2884.20 --> 2885.72]  If you're wrong, no big deal.
[2885.78 --> 2889.98]  But I'd love to see what your imagination has in store for us there.
[2890.48 --> 2894.96]  Yeah, I'd love to see this a year from now because I know half the stuff I'll say will be out of date or wrong.
[2895.32 --> 2896.72]  Of course, but that's fine.
[2896.80 --> 2897.50]  That's this topic.
[2898.06 --> 2902.70]  The stuff I said last year, I think I was still spot on in the sense that I did talk about graphs and vectors.
[2902.70 --> 2903.26]  Last year, too.
[2903.38 --> 2905.00]  And it's still relevant today.
[2905.22 --> 2907.50]  So, yeah, I'll take my chances this time around.
[2908.40 --> 2910.68]  So I think, yeah, you're absolutely right.
[2910.78 --> 2912.14]  Things change way too fast.
[2912.38 --> 2917.28]  And my personal take here is that graph rag is at a point in time.
[2917.76 --> 2924.48]  And we don't even know in the next three to five year time frame whether rag is going to be as hot as it is today.
[2924.68 --> 2924.82]  Right.
[2925.16 --> 2927.28]  I don't think LLMs are going away anywhere.
[2927.46 --> 2927.98]  Let's face it.
[2927.98 --> 2930.72]  I mean, they're here to stay and they're going to continue to evolve.
[2930.84 --> 2935.28]  We've just seen with the O1 model that came out from OpenAI, they are able to do reasoning.
[2935.84 --> 2938.50]  They're able to do so much more than what people give them credit for.
[2938.50 --> 2954.64]  So as this capability keeps evolving and LLMs keep morphing into whatever else they become, there's no guarantee that the kinds of tasks being done today using custom models, machine learning models, won't be done by an LLM.
[2954.64 --> 2961.06]  Now, some of the wild takes that I've seen involve the fact that you don't need to index anything in a database.
[2961.22 --> 2970.22]  You could potentially have your LLMs parameters store the index in a very fuzzy way and you could retrieve from that index, assuming that research goes in a certain way.
[2970.68 --> 2971.90]  But obviously, that's a long way away.
[2971.98 --> 2973.74]  I don't see that happening in the next few years.
[2973.74 --> 2980.50]  What I'm particularly excited about in the next few years is everyone's been talking about agentic systems.
[2980.86 --> 2993.56]  And if you look at the pivots that all these framework companies have had in the last year, Langchain, Lama Index, they're heavily trying to push this field forward in terms of how agents can help build, I guess, more capable systems.
[2993.56 --> 2997.84]  Now, RAG is just one small subset of the things agents are orchestrating.
[2997.98 --> 3006.46]  They can actually do many other things related to recommendation and, say, like search and retrieval and a host of other activities.
[3006.46 --> 3025.68]  So the conventional way or the standard way of doing agents has been using this framework called React, which is you could say like it's sort of like a graph based framework, but it's sort of static where you kind of decide the behavior of the system by programming in these paths and the agent acts on it.
[3025.68 --> 3028.64]  And then you send it back after the reasoning step is over and so on.
[3028.64 --> 3043.22]  But where I think actually graphs are going to be very interestingly used in the future, and I've seen some examples of frameworks that are already doing this, is can you use an underlying graph representation of action spaces to guide your agents?
[3043.48 --> 3049.00]  That is, can the agent actually actively update the action space via a graph structure?
[3049.70 --> 3057.74]  And once that happens, you can essentially have sort of more powerful agents that are not constrained by a rigid static sort of framework.
[3057.74 --> 3066.64]  You kind of have a dynamically updating agentic system, but it's not as open-ended as having this recursive agent calling that we have today, right?
[3066.74 --> 3067.78]  You still have a framework.
[3067.88 --> 3071.26]  The graph kind of acts as like a base structure for the agent to take its actions.
[3071.76 --> 3074.38]  So that's definitely one aspect of where agents are going.
[3074.90 --> 3082.66]  But that being said, the field of graph, you could say knowledge graphs and their role in symbolic systems, they've been around.
[3082.66 --> 3083.88]  It's been around for so long.
[3083.88 --> 3097.06]  And in the future, they could potentially be symbolic systems that utilize graphs in conjunction with these statistical models that are based on LLMs and a hybrid sort of symbolic statistical system that combines these tools together.
[3097.22 --> 3109.26]  That may not technically be called an agent, but it's still a hybrid sort of AI system in the sense that you might have leveraged the power of an LLM for the language capabilities, but then use symbolic systems to do the other tasks.
[3109.26 --> 3116.90]  All this is to say that I think graphs are way broader of an entity than what we are seeing today in terms of how they're used.
[3117.34 --> 3120.50]  There's a lot of other use cases that we couldn't go into in this discussion.
[3120.98 --> 3122.76]  And GraphRag obviously is a very, very small part of it.
[3122.76 --> 3132.50]  So I would say I'm currently excited about GraphRag, but I don't see this being like a topic that is going to be as talked about in the long term.
[3132.86 --> 3140.92]  But graphs as an entity and graph databases, these are systems that are going to actually be a core component of many systems of the future.
[3140.92 --> 3145.88]  Yeah, it's a good perspective to have because this is such a broad topic.
[3146.16 --> 3155.60]  And of course, we'll look forward to you coming back onto the show to give us more of a deep dive and or reading your blog post.
[3155.78 --> 3159.74]  I highly recommend people check out the links to Prashant's blog posts.
[3159.94 --> 3165.06]  And also, we'll make sure and include in the show notes links to the things that we've discussed here.
[3165.20 --> 3167.94]  But yeah, thank you so much for joining again.
[3167.94 --> 3178.84]  This has been a real pleasure and I feel like I've got a lot of things now that I want to go check out and try hands-on and learn more.
[3179.22 --> 3184.26]  So thanks for bringing out my curiosity on the topic.
[3184.86 --> 3185.78]  Yeah, no, thanks a lot, Daniel.
[3185.86 --> 3186.38]  Thanks a lot, Chris.
[3186.56 --> 3190.76]  And I just want to end by saying Kuzu is an embedded database.
[3190.90 --> 3193.88]  So you can just pip install Kuzu and it's super easy to get started.
[3194.28 --> 3196.06]  And you can find me on Twitter and LinkedIn.
[3196.06 --> 3201.32]  I'm sure Daniel will share the links and we can always chat more with anyone who's interested about graphs.
[3201.78 --> 3202.92]  Yeah, definitely check it out.
[3203.06 --> 3208.06]  And we'll also link some of the examples that you mentioned as well.
[3208.20 --> 3211.08]  So people can get hands-on and try some things.
[3211.24 --> 3222.50]  I love this element of these embedded tools out there that both let you try things locally and then even, you know, have a pathway to getting those things into production.
[3222.50 --> 3223.42]  So, yeah.
[3223.50 --> 3225.74]  Also, thank you for building great tools.
[3225.98 --> 3228.00]  That's a great contribution.
[3228.46 --> 3230.68]  So thanks and we'll talk to you soon.
[3231.22 --> 3231.82]  Thank you very much.
[3231.88 --> 3232.98]  Yeah, it was a pleasure talking to you both.
[3252.50 --> 3281.32]  Thanks again to our partners at Fly.io, to our Beat Freak in Residence, the one and only Breakmaster Cylinder, and to our longtime sponsors at Sentry.
[3281.32 --> 3286.40]  Use code CHANGELOG when signing up for a new Sentry team plan and save $100.
[3287.34 --> 3288.54]  That's all for now.
[3288.78 --> 3290.36]  We'll talk to you again next time.
