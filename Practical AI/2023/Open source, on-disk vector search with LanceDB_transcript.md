[0.00 --> 8.58]  Welcome to Practical AI.
[9.16 --> 15.90]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.90 --> 18.72]  are changing the world, this is the show for you.
[19.18 --> 24.32]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.32 --> 24.62]  listen.
[24.88 --> 26.70]  Check them out at Fastly.com.
[26.70 --> 31.96]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.40 --> 33.64]  No ops required.
[33.98 --> 36.02]  Learn more at fly.io.
[43.02 --> 46.28]  Welcome to another episode of Practical AI.
[46.64 --> 48.18]  This is Daniel Whitenack.
[48.32 --> 51.56]  I am CEO and founder at Prediction Guard.
[51.56 --> 57.24]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[57.24 --> 57.54]  Martin.
[57.84 --> 58.58]  How are you doing, Chris?
[58.76 --> 59.64]  Doing good today.
[59.72 --> 60.32]  How's it going, Daniel?
[60.74 --> 61.58]  Oh, it's going great.
[61.70 --> 67.12]  I was just, well, we were just remarking before actually starting the recording that one of
[67.12 --> 72.96]  the great things about doing these episodes is that we get the excuse to bring on the show
[72.96 --> 81.54]  the coolest open source and tooling and other projects that I'm using day to day and get the
[81.54 --> 82.72]  chance to interact with.
[82.88 --> 85.10]  And one of those is LanceDB.
[85.44 --> 91.50]  And we're really excited today to have with us Chung Hsu, who is the CEO and co-founder
[91.50 --> 92.54]  at LanceDB.
[92.88 --> 93.10]  Welcome.
[93.54 --> 93.78]  Thanks.
[93.86 --> 94.32]  Hey, guys.
[94.46 --> 95.72]  Super excited to be here.
[95.84 --> 96.98]  Thanks for having me on.
[97.76 --> 98.40]  Yeah, yeah.
[98.40 --> 102.14]  Well, first off, congrats on all your success.
[102.36 --> 108.82]  I was scrolling through LinkedIn and saw like a video of LanceDB up on the NASDAQ screen
[108.82 --> 110.62]  in Times Square.
[110.84 --> 112.00]  So that was cool to see.
[112.10 --> 114.02]  That must mean good things, I'm assuming.
[115.38 --> 121.18]  Yeah, this is possible via Brex and also Essence VC.
[121.70 --> 123.12]  So big thanks goes out to them.
[123.60 --> 124.20]  Cool, cool.
[124.30 --> 124.44]  Yeah.
[124.44 --> 129.76]  Well, I mentioned I've had a chance to look through some of what you're doing and actually
[129.76 --> 131.08]  use it day to day.
[131.18 --> 136.76]  Actually, that was a result of a previous episode that was, I think, titled, you know,
[136.80 --> 139.38]  Vector Databases Beyond the Hype with Prashant.
[139.86 --> 144.24]  I think the question that we asked him was like, oh, there's all these vector databases.
[144.24 --> 145.94]  You've compared all of them.
[146.64 --> 151.92]  What are some of the things that stand out or some of the vector databases that stand out
[151.92 --> 156.26]  in terms of what they're doing technically or how they're approaching things?
[156.72 --> 158.54]  And one of them he called out was LanceDB.
[158.98 --> 163.96]  I think in particular, he was talking about kind of on-disc index stuff.
[164.28 --> 167.24]  And so I'm sure we'll get into that in a little bit more.
[167.78 --> 169.08]  But that's how I got into it.
[169.12 --> 173.66]  So I recommend listeners maybe go back and get some context from that episode.
[173.66 --> 180.42]  But as we get into things, could you maybe give us a little bit of a picture as to how
[180.42 --> 182.44]  LanceDB came about?
[182.60 --> 188.94]  I know there's a lot of hyped vector database stuff out there and people might not sort of
[188.94 --> 193.66]  realize how these things were developed, how they came about, what the motivation was.
[194.18 --> 198.52]  And so if you could just give us a little bit of a sense of that, at least for LanceDB.
[199.24 --> 199.88]  Yeah, absolutely.
[199.88 --> 203.72]  And first, I wanted to also give a big shout out to Prashant as well.
[204.22 --> 207.24]  As you were saying, there's a lot of hype and noise in this area.
[207.34 --> 208.54]  There are a lot of different choices.
[209.36 --> 215.54]  And for users and developers who are building generative AI tooling and applications, it's
[215.54 --> 218.92]  always kind of confusing, like which one is good?
[219.18 --> 224.00]  And should you listen to the marketing from one tool versus another?
[224.34 --> 229.36]  So it's great to see someone with an engineering background who can write so well to actually
[229.36 --> 233.90]  take the time and just try out a ton of different tools and interview a bunch of different companies
[233.90 --> 235.76]  and come to his own conclusions.
[236.08 --> 241.36]  I'm super happy and excited that he's a fan of LanceDB and we hope to make that better for
[241.36 --> 243.40]  him and also all of our users.
[244.36 --> 246.20]  So back to LanceDB, I think...
[246.20 --> 250.00]  So we started the company two years ago at this point.
[250.46 --> 255.46]  And we didn't start out as a vector database company, actually.
[255.82 --> 260.30]  Because I think if you kind of remember, ChatGPT is barely one year old.
[260.50 --> 261.82]  Yeah, the dawn of AI.
[262.28 --> 263.32]  Yes, exactly.
[263.32 --> 270.80]  And so the original motivation was actually serving companies building computer vision
[270.80 --> 273.58]  and building new data infrastructure for a computer vision.
[274.10 --> 276.96]  So I had been working in this space for a long time.
[277.04 --> 281.80]  I'd been building data and machine learning tooling for about almost two decades at this
[281.80 --> 282.12]  point.
[282.26 --> 287.02]  I started out my career as a financial client and then I became involved in Python Open Source.
[287.20 --> 289.64]  I was one of the original co-authors of the Pandas Library.
[289.64 --> 294.76]  And that really got me sort of excited about open source, about Python and building tools
[294.76 --> 297.44]  for data scientists and machine learning engineers.
[298.14 --> 306.12]  And so at the time, this was in 2020 and 2021, what I observed was that the company I was working
[306.12 --> 309.12]  for, 2BTV, so it was a streaming company.
[309.26 --> 316.40]  So we dealt with both machine learning problems for tabular data and also for unstructured data
[316.40 --> 319.32]  like images and the video assets and things like that.
[319.32 --> 326.60]  And what I had noticed was that anytime a project touched this multimodal data for AI, from images
[326.60 --> 333.42]  to like the text for, you know, let's say subtitles or summaries to the poster images, these projects
[333.42 --> 335.62]  always took a lot longer.
[336.34 --> 342.12]  They were much harder to maintain and it was difficult to actually put into production.
[342.12 --> 348.54]  At the same time, so my co-founder, Leigh, who I had met during my days at Cloudera, he
[348.54 --> 351.46]  was working at Cruise and sort of dealing with the same issues.
[352.02 --> 358.12]  And so we put our heads together and our conclusion was that, hey, it's not the sort of top application
[358.12 --> 360.96]  or workflow layer or orchestration layer that's the problem.
[360.96 --> 363.68]  It's the underlying data infrastructure.
[363.68 --> 368.40]  If you look at sort of what's been out there, like, you know, Parquet and Oryl has been around
[368.40 --> 373.38]  and they've been great for tabular data, but they really, they really suck for managing
[373.38 --> 374.28]  unstructured data.
[374.86 --> 382.48]  And so we essentially said, hey, what would it take to build a single source of truth where
[382.48 --> 388.80]  we can toss in the tabular data plus the unstructured data and give much better performance
[388.80 --> 395.76]  at a much lower cost, a total cost of ownership, an easier foundation to build on top of for
[395.76 --> 398.04]  companies dealing with a lot of vision data.
[398.62 --> 404.64]  And so this comes in handy when you want to explore your large vision data sets for, you know,
[404.66 --> 405.70]  let's say all time is driving.
[406.02 --> 411.46]  This comes in really handy for things like recommender systems and things like that.
[411.46 --> 416.58]  And so we started out building out that layer, that storage layer in the open source.
[417.28 --> 424.42]  And that took about a year's worth of effort to really get to a shape that is usable, kind
[424.42 --> 427.84]  of like Parquet or Oryl and other formats in these tools.
[428.34 --> 435.34]  And that was when generative AI became really, it burst onto the scene and became sort of a
[435.34 --> 436.50]  revolutionary technology.
[436.50 --> 443.86]  And what happened at the time was we had originally built in vector index for our computer vision
[443.86 --> 449.58]  users to say, hey, let's deduplicate a bunch of images or let's find the most relevant samples
[449.58 --> 451.78]  for training, for active learning and things like that.
[452.14 --> 457.58]  And it was sort of that open source community that discovered that, hey, this can be really
[457.58 --> 459.46]  good for generative AI as well.
[459.46 --> 464.96]  That's when we sort of separated out another repo to say, hey, this is a vector database.
[465.68 --> 471.24]  And it's much easier to communicate with the community than to say, hey, you're looking
[471.24 --> 472.16]  for a vector search.
[472.76 --> 474.20]  Use this columnar format.
[474.96 --> 476.76]  And so that's how we got onto this path.
[477.44 --> 478.16]  Quick question for you.
[478.20 --> 480.20]  It's really a follow up to something you said.
[480.82 --> 483.08]  It's been a couple of moments now as we were going through that.
[483.08 --> 488.30]  But I was just curious when you were talking about kind of going through the analysis on
[488.30 --> 492.50]  the top workflow versus whether it was infrastructure and you said y'all concluded infrastructure.
[492.84 --> 497.12]  I was just wondering, you kind of went on past that into that, but I was kind of wondering
[497.12 --> 499.04]  how did y'all come to that determination?
[499.04 --> 503.02]  For those of us who are not deeply into that thought process, I was wondering where your head
[503.02 --> 504.02]  was at when you were doing that.
[504.68 --> 508.08]  Yeah, it wasn't an easy decision or conclusion.
[508.08 --> 514.90]  Thinking back, it was kind of, you know, so it was like 2022 initially seemed pretty crazy
[514.90 --> 517.14]  when we sort of first came up on it, right?
[517.42 --> 521.28]  If you think about it, it's like, why would you make a new data format like in 2022?
[521.58 --> 522.98]  Like Parquet has been working so well.
[523.40 --> 527.84]  And I think it was really observing the pain of our own teams.
[528.00 --> 532.22]  And also we went out and interviewed a lot of folks managing unstructured data.
[532.22 --> 538.34]  And so for them, it was, you know, one, data was split into many different places.
[538.80 --> 543.52]  Like the metadata might be managed in Parquet and the raw assets are just dumped onto local
[543.52 --> 544.66]  hard drives or S3.
[545.14 --> 550.02]  And then you might have, you know, other tabular data managed in other systems.
[550.02 --> 555.68]  And they would always talk about how painful it is to stitch everything together and manage
[555.68 --> 556.28]  it all together.
[556.62 --> 561.80]  And some of the outcomes are like, it's really hard to maintain those data sets in production.
[561.80 --> 568.32]  Like you have a Parquet data set that has the metadata and then links to S3 or something
[568.32 --> 569.32]  like that to all the images.
[569.62 --> 574.54]  And then somebody moves that S3 directory or something like that.
[574.60 --> 575.94]  And now all of your data sets are broken.
[576.36 --> 581.42]  Or something like we would interview folks are like, hey, what are you doing to explore
[581.42 --> 583.36]  your visual data sets and things like that?
[583.36 --> 587.26]  And they're like, well, you know, I use MacBook and there's this app on that called Finder.
[587.76 --> 591.20]  And if you single click on a folder, it shows you a bunch of thumbnails.
[591.80 --> 595.46]  It's sort of this horrible way to actually work with your data.
[595.60 --> 601.04]  But it was because it was so hard to manage all of that, that machine learning engineers
[601.04 --> 603.50]  and researchers were stuck with these subpar tools.
[604.58 --> 611.04]  You mentioned kind of this transition of thinking from some of the original use cases that you
[611.04 --> 617.96]  were talking about with computer vision to this world of generative AI that we're living in now.
[617.96 --> 624.68]  From my impression, from an outsider's perspective, it seems like LanceDB has kind of positioned
[624.68 --> 630.74]  itself very well to serve this kind of generative AI use cases, which I'm sure we'll talk about
[630.74 --> 632.64]  in a lot more detail later on.
[632.76 --> 639.30]  I'm wondering from your perspective, like how has that overwhelming demand for the generative
[639.30 --> 645.84]  AI use case kind of changed your mindset and direction as a company and a project and open
[645.84 --> 647.18]  source tooling and all of that?
[647.80 --> 653.12]  And how do you envision the kind of what you're targeting as the use cases moving forward,
[653.22 --> 653.50]  I guess?
[654.26 --> 660.78]  I think certainly generative AI has brought in a lot of different changes and new thinking.
[660.78 --> 669.56]  One was the sort of focus around use cases of semantic search and just retrieval in general.
[670.08 --> 676.04]  I think with the advent of generative AI, I think retrieval becomes much more important
[676.04 --> 677.12]  and ubiquitous.
[677.82 --> 684.36]  For us, what that means is, you know, increased investments in terms of getting the index to
[684.36 --> 685.86]  work really well and really scalable.
[685.86 --> 692.56]  And then sort of making that data management piece to work really well as well and integrating
[692.56 --> 700.30]  with frameworks for RAG and for, you know, agents and for just generative AI in particular.
[700.98 --> 708.56]  When we started out, inevitably, we were dealing with, you know, multi-terabyte to petabyte scale,
[708.86 --> 710.64]  like vision data sets and things like that.
[710.64 --> 713.12]  And we're still dealing with a lot of that.
[713.20 --> 718.84]  But for generative AI, I think there was a renewed focus on ease of use because a lot
[718.84 --> 724.48]  of users are coming in who don't have, you know, years of experience in like data engineering
[724.48 --> 726.32]  or machine learning engineering.
[726.98 --> 733.34]  And what they're looking for is a easy to use and easy to install package that doesn't
[733.34 --> 738.42]  require, you know, you to like be an expert in any of these underlying technologies.
[738.42 --> 744.12]  We also spent some effort into, okay, that was sort of the motivation behind us making
[744.12 --> 747.88]  LanceDB, the vector database, one, open source, and two, embedded.
[748.34 --> 755.40]  Because we felt like there were lots of options on the market that required you to say, figure
[755.40 --> 757.90]  out, okay, like, what is the instance I need?
[758.18 --> 759.90]  How many instances do I need?
[760.02 --> 760.78]  What type of it?
[760.86 --> 763.62]  Okay, like now I have to shard the data and blah, blah, blah.
[763.62 --> 769.54]  And coming from that data background, you know, what I had been working with a lot is like,
[769.82 --> 774.80]  you know, SQLite or DuckDB that just runs as part of your like application code that was
[774.80 --> 777.60]  and just would just talk to files that live anywhere.
[777.92 --> 780.64]  And it was super easy to install and use.
[780.88 --> 786.42]  So that's sort of what gave us that inspiration to make an embedded vector database.
[786.42 --> 793.56]  You had just got into this sort of idea of embeddings, or sorry, embedded databases, which
[793.56 --> 796.32]  well, embeddings are related, but that's another topic.
[796.70 --> 801.56]  But the idea that LanceDB is embedded, you mentioned DuckDB and other things that kind
[801.56 --> 804.86]  of operate in the same sort of sphere.
[805.24 --> 813.66]  I'm wondering, for those that maybe are trying to position LanceDB's vector database tooling
[813.66 --> 821.50]  within a kind of wider ecosystem of vector databases and like plugins to other databases that support
[821.50 --> 822.78]  vector search.
[822.96 --> 828.36]  Could you explain a little bit about like, what does it mean that LanceDB is embedded?
[828.60 --> 830.96]  Like, what does that mean practically for the user?
[831.10 --> 834.16]  Maybe people aren't familiar with that term quite as much.
[834.56 --> 836.56]  So what does that mean practically for the user?
[836.56 --> 843.56]  And are there other kind of like general ways that you would differentiate LanceDB's tooling
[843.56 --> 846.64]  and the database versus some other things out there?
[847.22 --> 849.28]  So I love sort of geeking out about these topics.
[849.66 --> 855.40]  So at the very bottom layer, in terms of technology, I think there's a couple of things that fundamentally
[855.40 --> 856.92]  sets LanceDB apart.
[857.30 --> 862.62]  One, as you mentioned, is the fact that it's embedded or runs in process.
[862.62 --> 866.78]  I think we are one of two that can run in process in Python.
[867.06 --> 870.32]  We're the only one in JavaScript that runs in process.
[870.88 --> 876.32]  Number two is the fact that we have a totally new storage layer through Lance column or format.
[876.82 --> 881.84]  What this allows us to do is add data management features on top of the index.
[882.32 --> 888.74]  And then number three is the fact that the indices, the vector indices and others in LanceDB
[888.74 --> 895.28]  are disk-based rather than memory-based so that it allows us to separate compute and storage
[895.28 --> 897.46]  and allows us to scale up a lot better.
[897.86 --> 903.94]  So those are kind of the big value propositions that these technological choices bring to users
[903.94 --> 904.56]  of LanceDB.
[905.02 --> 906.62]  So number one, ease of use.
[907.00 --> 908.76]  Number two, hyper-scalability.
[909.36 --> 911.26]  Number three, cost-effectiveness.
[912.06 --> 915.10]  And then number four, the ability to manage all of your data together.
[915.10 --> 921.90]  And not just the vectors, but also, if you think about it, the metadata and also the raw assets,
[922.06 --> 926.16]  whether they're images, text, or videos.
[927.04 --> 932.68]  Could you kind of describe a typical use case of a developer doing this,
[932.74 --> 938.90]  where you're kind of taking those features that are distinguishing LanceDB from other possibilities,
[939.02 --> 942.42]  other competition, but just talk about what that workflow looks like,
[942.42 --> 947.28]  you know, or if there is a major one or a couple, and just kind of get it very grounded
[947.28 --> 951.26]  so somebody that's listening can kind of understand how they're going to do it from A to Z
[951.26 --> 953.40]  when they're integrating LanceDB into their workflow?
[953.94 --> 959.50]  So there's a couple of sort of prototypical workflows that we see from our users.
[959.50 --> 965.38]  I think at the smaller scale for LanceDB, you know, you're installing it via like PIP
[965.38 --> 967.88]  or NPM or something like that.
[968.08 --> 972.80]  And in general, you get some input data that comes in as like a Pandas data frame
[972.80 --> 974.26]  or maybe a Polar's data frame.
[974.50 --> 978.06]  And then you interface with an embedding model.
[978.16 --> 981.94]  You can do that yourself, or you can actually configure the LanceDB table to say,
[982.02 --> 987.80]  hey, use OpenAI embeddings, or hey, use these Hugging Face embeddings.
[988.36 --> 990.18]  LanceDB can actually take care of all that.
[990.18 --> 996.66]  So it's a pretty quick sort of data frame to LanceDB, and then you can search it.
[996.80 --> 1001.44]  And then that comes out as, you know, data frames or Python dicks or things like that,
[1001.44 --> 1007.72]  that plugs into the rest of your workflow that are likely data frame or pedantic or Python
[1007.72 --> 1008.30]  dick based.
[1009.00 --> 1009.66]  So that's number one.
[1009.74 --> 1015.38]  And then a kind of number two is really these large scale use cases where some of our users
[1015.38 --> 1021.82]  have anywhere from like 100 million to multiple billions of vectors in one table.
[1022.54 --> 1025.92]  And that's a much bigger production deployment.
[1026.68 --> 1032.48]  And typically, what makes LanceDB stands out in that area is, one, it's very easy for them
[1032.48 --> 1035.90]  to process the data using a distributed engine like Spark.
[1036.22 --> 1039.10]  And they can write concurrently and get that done really quickly.
[1039.66 --> 1043.80]  I think we're one of the few that offers GPU acceleration in terms of indexing.
[1043.80 --> 1047.54]  So even for those really large data sets, you can index pretty quickly.
[1048.26 --> 1053.48]  And then number three is, because we're able to actually separate the compute and storage,
[1053.82 --> 1060.56]  even at that large vector size, you don't really need that many query nodes.
[1060.90 --> 1068.10]  Like, you can actually just have one or two, like fairly average and commodity query nodes
[1068.10 --> 1073.36]  that runs on your storage of choice, depending on what latency requirements you want.
[1073.36 --> 1076.14]  And then just have a very simple architecture.
[1076.70 --> 1080.70]  For these types of architectures, the query nodes are stateless, and they don't need to
[1080.70 --> 1081.44]  talk to each other.
[1081.86 --> 1085.38]  So when you need to scale up, or when a node drops out, it has to come back in.
[1085.82 --> 1088.48]  There's no sort of leader election, there's no coordination.
[1089.08 --> 1091.98]  It really lowers the complexity of that whole stack.
[1092.40 --> 1097.94]  So another great example of this kind of architecture and the benefits that it brings is Neon,
[1097.94 --> 1099.36]  the Neon database.
[1099.36 --> 1106.74]  So I think Nikita, who's the founder, recently had a good Twitter thread about the difference
[1106.74 --> 1110.30]  between Neon and other databases.
[1111.12 --> 1115.08]  And he called it shared data versus shared nothing architecture.
[1115.56 --> 1121.14]  And I think that's also what we kind of strive to deliver in LastCB versus other vector databases.
[1121.14 --> 1128.22]  Yeah, I know one of the things that I really enjoyed in trying out a lot of things with
[1128.22 --> 1132.76]  LanceDB is I can pull up a collab notebook, right?
[1132.86 --> 1135.34]  And try out, like I can import LanceDB.
[1135.76 --> 1141.34]  I can import like a subset of the kind of database that I'm going to be working, or the data that
[1141.34 --> 1142.02]  I'm working with.
[1142.06 --> 1143.08]  It all runs fine.
[1143.46 --> 1147.74]  I don't have to like set up some client server type of scenario.
[1147.74 --> 1153.46]  And then when people ask, well, how are you going to push this out to a larger scale?
[1153.72 --> 1160.68]  The appeal of just saying, hey, well, we can just throw up this LanceDB database on S3
[1160.68 --> 1162.14]  and then connect to it.
[1162.28 --> 1168.14]  That's a very appealing thing for people because also those storage layers are available everywhere
[1168.14 --> 1173.60]  from on-prem to cloud to whatever sort of scenarios you're working with.
[1173.62 --> 1175.94]  So it's very, very flexible for people.
[1175.94 --> 1177.48]  Could you explain a little bit?
[1177.50 --> 1182.24]  Because this is something like I've been asked a couple times, but so this is my selfish
[1182.24 --> 1184.96]  question because I have you on the line.
[1185.48 --> 1187.48]  So you're helping me with my own day to day work.
[1187.62 --> 1193.30]  But when I'm when I'm talking to like some people, clients that I'm working with, I'm like,
[1193.38 --> 1197.02]  oh, we can just throw this up on on S3 and then access it.
[1197.52 --> 1202.06]  Usually their question is something like, well, like because they have in their mind a database
[1202.06 --> 1209.24]  has a compute node and like the somehow the performance of queries into the database is
[1209.24 --> 1217.10]  tied to the sizing of that compute node and maybe like how that's sort of clustered or sharded
[1217.10 --> 1218.48]  across the database.
[1218.48 --> 1223.68]  And then like this idea, oh, I'm just going to have even just a Lambda function that connects
[1223.68 --> 1225.66]  to S3 and does a query.
[1225.66 --> 1226.02]  Right.
[1226.04 --> 1230.14]  Like this kind of in some ways it like breaks things in people's mind.
[1230.30 --> 1232.76]  And so a lot of times their question is like, how does that work?
[1232.82 --> 1239.08]  How can a query to this large amount of data be efficient when the data is just like sitting
[1239.08 --> 1241.54]  there and in S3 or in another place?
[1241.54 --> 1245.20]  So could you help with help me with my answer, I guess, is what I'm asking?
[1245.84 --> 1246.52]  Yeah, absolutely.
[1246.72 --> 1251.48]  So this goes back to what we talked about earlier with separation of compute and storage.
[1252.06 --> 1257.16]  And if you've been sort of steeped in like data warehousing, data engineering land, this
[1257.16 --> 1264.18]  has been a big arc of data warehouse innovation in the past decade by allowing us to scale up
[1264.18 --> 1266.12]  the storage versus the compute separately.
[1266.12 --> 1272.78]  This is the thing that makes the system seem magical, where you can process a huge amount
[1272.78 --> 1278.66]  of data on what seems like pretty commodity or pretty weak compute.
[1279.24 --> 1284.46]  And so the analogy that I like to make with the situation is kind of like a lot of us are
[1284.46 --> 1288.06]  familiar with, let's say, like DuckDB demos or videos.
[1288.06 --> 1295.70]  And you could see instances where DuckDB is processing hundreds of gigabytes of data.
[1296.12 --> 1301.88]  On just a laptop and in a very vast amount of time, and they are able to spit out results
[1301.88 --> 1303.54]  and almost interactively.
[1304.36 --> 1310.72]  And there are companies, you know, from like Mother Duck to, you know, there's a new company
[1310.72 --> 1316.66]  called Valplan that is looking to essentially distribute DuckDB queries on AWS Lambdas.
[1316.98 --> 1318.28]  It's basically the same thing.
[1318.34 --> 1321.36]  It's all about the separation of compute and storage.
[1321.36 --> 1327.34]  And that's only possible if you have the right underlying data architecture for storing
[1327.34 --> 1328.76]  vectors and the data itself.
[1329.60 --> 1337.32]  And just for someone that like is not a database developer, can you describe in any words like
[1337.32 --> 1341.74]  the generalities of that data structure that enables such a thing?
[1342.48 --> 1342.64]  Yeah.
[1342.76 --> 1343.60]  So it's two things.
[1343.74 --> 1346.36]  One is the columnar format.
[1346.36 --> 1351.26]  So typically, you know, from Gen AI to machine learning, you can have very wide tables, but
[1351.26 --> 1354.82]  typically a single query only needs like a couple of columns.
[1355.44 --> 1360.38]  So columnar format allows you to only have to fetch and look at like a very small subset
[1360.38 --> 1361.02]  of that data.
[1361.46 --> 1369.48]  Number two is that columnar format needs to have be paired with an index, like the vector index
[1369.48 --> 1371.24]  in this particular scenario.
[1371.24 --> 1377.00]  And that vector index, in order to give this separation of compute and storage, has to
[1377.00 --> 1378.38]  be based on disk.
[1378.52 --> 1383.36]  So you have to be stored the data on disk, not force the user hold everything into memory,
[1383.66 --> 1386.12]  and then be able to access that very quickly.
[1387.02 --> 1392.24]  And then number three is how to connect that index with the columnar format.
[1392.58 --> 1398.70]  So a columnar format like Parquet does not give you the ability to do fast random access.
[1398.70 --> 1404.28]  So even if you had that good index using Parquet, you would not be able to get interactive performance
[1404.28 --> 1405.50]  in terms of queries.
[1405.96 --> 1412.26]  And it's only by having a new columnar format like LANDS that can give you fast random access
[1412.26 --> 1416.54]  and fast scans that you can successfully put these two together and deliver the thing.
[1416.70 --> 1421.74]  So those are the three sort of big pillars that I think in our data architecture that makes
[1421.74 --> 1422.32]  this possible.
[1422.56 --> 1428.48]  While we were talking here, I'm going through GitHub on your repo and stuff, and was surprised
[1428.48 --> 1430.96]  it's something that kind of prompting the next question.
[1431.24 --> 1437.98]  It looks like you're really addressing a wide range of different types of needs.
[1438.22 --> 1441.76]  And so there's obviously Python, as you would expect, but you have JavaScript.
[1442.24 --> 1447.24]  And then I was delighted to discover that there's a Rust client in there, which is when I'm not
[1447.24 --> 1449.80]  doing AI specific things most of the time.
[1449.96 --> 1452.04]  That's my language of choice these days.
[1452.04 --> 1455.36]  Could you talk a little bit about kind of two things?
[1455.68 --> 1460.74]  The broader, like what you're trying to achieve, like how you choose what languages to support
[1460.74 --> 1462.26]  and how you're getting there.
[1462.36 --> 1467.12]  And then if you'll scratch my itch, what is your intention with that Rust client?
[1467.24 --> 1467.68]  Is it ready?
[1467.76 --> 1468.32]  What does it do?
[1468.60 --> 1470.24]  Just because I'm fascinated with that.
[1470.34 --> 1470.54]  Sorry.
[1471.00 --> 1471.92]  Yeah, absolutely.
[1472.22 --> 1473.48]  I love talking about Rust.
[1473.48 --> 1479.24]  The Rust package is actually not a client, but so on the core of both the data format and
[1479.24 --> 1481.18]  the vector database is actually in Rust.
[1481.54 --> 1486.58]  So the Rust crate that we have is actually the database or the embedded database.
[1487.22 --> 1493.06]  And so, and we actually build, for example, the JavaScript, again, the same thing with JavaScript.
[1493.52 --> 1497.12]  It's not just a client, but it's also an embedded database in JavaScript.
[1497.12 --> 1504.20]  So that is actually based on top of the Rust crate and kind of like you have in, say, like
[1504.20 --> 1505.44]  Polars or something like that.
[1505.52 --> 1508.92]  You have like a Rust core and then you connect that into JavaScript.
[1509.68 --> 1519.08]  So we had actually started out in 2022 writing in C++ because Parquet is written in C++,
[1519.64 --> 1523.50]  you know, like serious data people and database people write in C++, right?
[1523.58 --> 1525.06]  Until they find Rust, of course.
[1525.54 --> 1526.06]  Right.
[1526.06 --> 1535.18]  And it was sort of a hack project during Christmas time in 2022, at the end of 2022, where we had
[1535.18 --> 1541.38]  to get a hack project for a customer, actually, and where we had to actually re-implement partially
[1541.38 --> 1543.74]  the repath for Lance format.
[1544.50 --> 1551.38]  And what we found was just, it was so good that we decided to just actually rewrite everything
[1551.38 --> 1551.82]  in Rust.
[1552.26 --> 1555.48]  I think biggest things were, we were a lot more productive.
[1555.48 --> 1564.06]  We rewrote roughly six months of solid C++ development in about three weeks with Rust.
[1564.60 --> 1569.98]  And we had, this was like us learning Rust as beginners, as we went along.
[1570.28 --> 1577.30]  A lot of that initial Rust code has again been rewritten over the past year, but it just
[1577.30 --> 1578.60]  made us feel a lot more productive.
[1578.60 --> 1582.96]  And then number two is the safety that Rust offers you has been amazing.
[1583.22 --> 1588.16]  With C++, like every release, it just didn't have a good feeling.
[1588.24 --> 1591.96]  It was almost like, you know, where's that next set fault going to come from?
[1592.28 --> 1600.02]  Whereas with Rust, you know, we felt very confident making multiple releases per week with, you know,
[1600.02 --> 1607.48]  major features and we did not see anywhere near the sort of issues that we saw with C++.
[1608.24 --> 1608.38]  Right.
[1608.44 --> 1610.34]  So everything has been really great.
[1610.48 --> 1616.94]  I know that like Rust has become really popular now for, actually, even with vector databases,
[1616.94 --> 1618.82]  like Quadrant, I think is Rust.
[1619.22 --> 1625.36]  Pinecone, they're not open source, but in turn, they publicly said that they've written their whole stack in Rust as well.
[1625.36 --> 1631.90]  So one more question from you along the same line before I let it go, because we've hit that sweet spot that I love.
[1631.90 --> 1639.72]  Do you think, and this is not specific to LanceDB, but based on what you're saying, clearly you're thinking ahead on these things.
[1639.72 --> 1648.28]  As we go forward and you see both the AI applications and you see the different types of workflows and infrastructures,
[1648.82 --> 1655.54]  you know, becoming broader and more supportive, the multi-language aspect of getting out of only Python, for instance,
[1655.70 --> 1665.00]  do you foresee that as a convergence where you're seeing language agnosticism developing in this space as it has in other areas of computer science?
[1665.00 --> 1671.06]  Or do you think that we're still going to be kind of locked in on the current sets of infrastructure and tooling,
[1671.20 --> 1673.54]  very Python oriented for the indefinite future?
[1673.78 --> 1675.16]  What is your thinking along those lines?
[1676.00 --> 1683.58]  So I think generative AI definitely changes the picture in that I think there's a very large TypeScript, JavaScript community
[1683.58 --> 1690.02]  that has been brought into the arena to build AI tools.
[1690.02 --> 1697.30]  And so I think this is also an underserved segment where, you know, it's not just vector databases,
[1697.54 --> 1704.62]  but data tooling in general lags far behind in JavaScript slash TypeScript land versus Python.
[1705.06 --> 1713.36]  And I think there's a real opportunity for the open source community to create good tools for this part of the community as well.
[1713.36 --> 1722.26]  I want to hear about some of the actual use cases that you've seen people implement with LanceDB.
[1722.84 --> 1728.22]  Maybe if there's ones that stand out like, oh, this was cool because whatever it was,
[1728.32 --> 1733.82]  they used it at scale or it's like fits a very typical generative AI use case or whatever.
[1733.82 --> 1741.24]  And then maybe something that surprised you in terms of, oh, I didn't always when you put a project out into the world,
[1741.34 --> 1745.66]  there's these things where, oh, I really didn't expect people to be using it that way.
[1745.80 --> 1747.56]  But yeah, that sort of makes sense.
[1747.64 --> 1752.70]  So do you think of anything that fits into one or both of those categories?
[1753.06 --> 1760.10]  The use cases for LanceDB in the community that I see falls into three or four large buckets.
[1760.10 --> 1764.88]  One is, of course, generative AI, RAG, and things like that.
[1765.92 --> 1772.26]  And I think there, I think it's not so much the use of LanceDB that I think is really cool,
[1772.40 --> 1777.04]  but it's the applications that people build with it that is really cool and amazing.
[1777.68 --> 1782.46]  And I think a lot of the applications that people build that is cool,
[1782.56 --> 1789.02]  that really takes advantage of LanceDB is things where you need RAG to be very agile.
[1789.02 --> 1795.74]  And that you need it to be really sort of tightly bundled with your application.
[1795.74 --> 1802.74]  You can sort of call this RAG from anywhere and have it return pretty quickly and without too much complexity.
[1803.30 --> 1810.54]  And so this is where I see a lot of folks from like your standard like chatbots and chat with documentation
[1810.54 --> 1817.82]  to things like productivity tools where they build things that help people organize their daily schedules
[1817.82 --> 1829.74]  to much more high stakes things in production and like code generation or like healthcare and legal and things like that.
[1829.74 --> 1836.38]  And so there, I think typically you see vector data sets sizes from like the tens of thousands
[1836.38 --> 1841.02]  up to single digit millions of vectors typically.
[1841.80 --> 1847.84]  And so production means you really scale up both the number of data sets that you have
[1847.84 --> 1849.66]  and then the number of vectors that you have.
[1849.66 --> 1856.06]  And one of the cool things that I've seen that takes advantage of LanceDB and Lance Format uniquely
[1856.06 --> 1863.50]  is there's a code analysis tool that sort of analyzes your GitHub repository
[1863.50 --> 1869.02]  and plugs it into a RAG like customer success sort of tool.
[1869.70 --> 1872.04]  And what they want to be able to do is say,
[1872.18 --> 1877.72]  query the state of the database like this today versus yesterday versus a week ago
[1877.72 --> 1879.92]  to say, hey, was this issue fixed or not?
[1880.28 --> 1881.74]  And like what's still outstanding?
[1882.38 --> 1888.94]  And so LanceDB uniquely gives you this ability to version your table and also do time travel.
[1889.08 --> 1892.22]  So you can say any data vector database can do like,
[1892.40 --> 1895.96]  give me the 10 most similar things to this input uniquely.
[1896.16 --> 1898.88]  But what LanceDB gives you the ability to do is say,
[1899.24 --> 1903.30]  give me the 10 most similar as of yesterday or as of a week ago.
[1903.74 --> 1905.96]  And we do that sort of automatically for you.
[1905.96 --> 1909.90]  Yeah. And then I think the other big buckets are, you know,
[1910.10 --> 1913.74]  e-commerce and a search and like recommender engines, right?
[1913.74 --> 1917.00]  This is like the traditional use case for vector databases.
[1917.38 --> 1921.16]  And there you tend to see much bigger like single data sets that are, you know,
[1921.16 --> 1923.52]  say I want to store like item embeddings.
[1923.62 --> 1926.24]  Maybe that's, you know, up to a couple of million, up to 10 million.
[1926.60 --> 1928.12]  I want to store item embeddings.
[1928.12 --> 1929.88]  That could get up to like hundreds of millions.
[1929.88 --> 1934.82]  It's you don't have as many tables, but you have potentially have very large tables.
[1935.08 --> 1939.06]  Right. And then of course the last bucket is this like computer vision,
[1939.42 --> 1941.12]  like AI native computer vision,
[1941.26 --> 1946.46]  either generative computer vision or things like autonomous vehicles and things like that.
[1946.56 --> 1953.68]  And there's a whole sort of combination of more complicated use cases that enables active learning,
[1953.86 --> 1955.44]  deduplication and things like that.
[1955.44 --> 1964.36]  And the thing that is very unique about the use case of LAN CB in there is companies that are managing all of their training data
[1964.36 --> 1966.30]  in LAN CB and LAN format as well.
[1966.40 --> 1970.64]  So you can use the vector database to find the most interesting samples.
[1971.02 --> 1978.48]  And then you can actually use the tooling on top of the format to essentially keep your GPU utilization high
[1978.48 --> 1985.56]  and keep your GPU fed very quickly during training or if you're fine tuning or, you know, if you're running evals and things like that.
[1986.20 --> 1986.92]  Yeah. So cool.
[1987.08 --> 1996.82]  I, one of the things that has been most fun for me recently is this combination of an LLM, LANsDB and DuckDB,
[1997.18 --> 1999.96]  where like you can create these really cool.
[1999.96 --> 2007.82]  So if I'm using an open LLM that can generate like SQL queries or something,
[2008.12 --> 2011.08]  but I have like all of these different SQL tables,
[2011.22 --> 2017.40]  like what we're doing is like putting descriptions of the SQL fields and tables in LanceDB
[2017.40 --> 2022.48]  and actually on the fly, like matching and pulling those to generate a prompt,
[2022.60 --> 2026.80]  which goes to the LLM to generate the SQL code, which is executed with DuckDB.
[2026.80 --> 2034.58]  And this gives you like the kind of really nice natural language query to your data type of scenario,
[2034.58 --> 2036.44]  which has been really fun to play with.
[2036.58 --> 2037.36]  That's really good to hear.
[2037.52 --> 2038.90]  Actually, sorry to interrupt.
[2039.26 --> 2041.12]  So, because you kind of nerd-side me.
[2041.56 --> 2042.68]  So getting it up there.
[2043.08 --> 2047.90]  So one of the things that's really cool about DuckDB is its extension mechanism.
[2048.82 --> 2055.46]  And so I think they've also published like a extension framework for Rust-based extensions.
[2055.46 --> 2058.92]  And so we have sort of a basic integration going there.
[2059.32 --> 2064.30]  And I think in New Year, what you can expect from us is actually we're going to be spending a little more time
[2064.30 --> 2067.84]  to make that integration be more rich.
[2068.02 --> 2071.38]  Meaning our goal is for you to be able to say,
[2071.80 --> 2075.44]  to write like a DuckDB UDF to do vector search.
[2075.62 --> 2079.94]  And then the results come back as like a DuckDB table,
[2079.94 --> 2084.10]  where you can then run additional query, like DuckDB queries on top of that.
[2084.10 --> 2089.14]  And so, and sort of the same thing with like Polars, right?
[2089.20 --> 2097.28]  So you can, and the goal is to essentially make it so that like vector database is no longer a thing
[2097.28 --> 2098.54]  that you even have to think about.
[2098.66 --> 2103.46]  It's people are generally more familiar with like DuckDB or Polars as the sort of that tool
[2103.46 --> 2105.32]  that just stitches together the workflow.
[2105.64 --> 2110.36]  So we just want that to make it feel even smoother and more transparent.
[2110.36 --> 2113.16]  A couple of moments ago, when you were talking about the use cases,
[2113.26 --> 2116.02]  you were talking about, you know, like autonomous vehicles and stuff.
[2116.08 --> 2118.82]  And I was wondering if we could pull that thread a little bit more.
[2118.98 --> 2120.36]  It seems like it is a fantastic...
[2121.28 --> 2122.04]  Chris loves drones.
[2122.54 --> 2123.56]  Yeah, I love drones.
[2123.56 --> 2126.36]  And I love things that are not by data centers.
[2126.56 --> 2126.72]  Yeah.
[2126.90 --> 2129.44]  I love things that are off on the edge,
[2129.56 --> 2132.36]  whether it be for inference or including training concerns
[2132.36 --> 2137.22]  concerns that you may not have all the things that were so spoiled with,
[2137.32 --> 2139.58]  with our cloud providers out there.
[2139.76 --> 2144.30]  And it seems like, you know, there's many types of opportunities to use that.
[2144.86 --> 2146.44]  What's your thinking around that?
[2146.52 --> 2149.62]  Have you seen any use cases, any ideas for the future
[2149.62 --> 2152.68]  in that kind of autonomous on the edge world?
[2153.30 --> 2153.92]  Yeah, definitely.
[2153.92 --> 2155.70]  So we certainly have...
[2155.70 --> 2159.48]  So some of our users are like robotics or device companies
[2159.48 --> 2164.10]  where they either collect data and write it as Lance on the edge,
[2164.22 --> 2167.06]  or they sort of collect data as like, let's say,
[2167.12 --> 2171.44]  Protobuf or something like that and send it off to be converted into Lance
[2171.44 --> 2174.24]  for like analytics, vector search, and so on and so forth.
[2174.48 --> 2177.70]  I think in this world, you're going to know it better than me.
[2177.84 --> 2178.28]  So what...
[2178.28 --> 2182.14]  But what I see is that one is the data is super complicated.
[2182.14 --> 2186.22]  So especially with, let's say, like a vehicle's types of use cases,
[2186.40 --> 2188.78]  you're getting visual data from the cameras,
[2189.04 --> 2191.94]  you're getting point clouds from the lidars,
[2192.42 --> 2196.96]  you're getting time series data from the sensor readings over time,
[2197.12 --> 2200.78]  and then you've got manual input data from like the auditors
[2200.78 --> 2202.48]  and the drivers that are sitting in the car.
[2203.02 --> 2205.92]  You're also getting metadata about the car, about the weather,
[2206.08 --> 2207.86]  about the geography and all that, right?
[2207.86 --> 2212.34]  So like being able to manage that and query all that together,
[2212.34 --> 2217.08]  I think will be super important for, you know, robotics and vehicles
[2217.08 --> 2218.86]  and any sort of...
[2218.86 --> 2222.20]  Any company that's putting things out there in the real world
[2222.20 --> 2224.66]  that's generating data in the physical world.
[2225.20 --> 2226.50]  And I think that...
[2226.50 --> 2228.06]  Yeah, I mean, it's a really hard problem,
[2228.18 --> 2230.94]  but I think that the potential is huge, right?
[2230.94 --> 2237.90]  Because I think for AI, we're going from this era of like very canned
[2237.90 --> 2242.34]  by question and answer to much more free form question and answer,
[2242.48 --> 2244.90]  but it's still a little bit passive, right?
[2244.94 --> 2247.22]  You're like, you're asking it for information.
[2247.70 --> 2250.14]  But what's really exciting would be like, you know,
[2250.20 --> 2253.34]  you marry these sort of generalized AI capabilities
[2253.34 --> 2257.30]  with a drone or a robot or, you know,
[2257.30 --> 2260.52]  something that can go out and be active out in the real world.
[2261.52 --> 2265.20]  That gets me super excited about what's to come.
[2265.32 --> 2267.80]  I'm wondering as we close out here,
[2268.04 --> 2270.18]  it's been a fascinating discussion.
[2270.60 --> 2272.94]  At the end here, could you just take a moment
[2272.94 --> 2275.94]  and make a few observations about
[2275.94 --> 2280.26]  what is exciting from your perspective right now
[2280.26 --> 2283.46]  in this sort of practical AI space?
[2283.46 --> 2285.00]  Because that's where you're living.
[2285.00 --> 2287.98]  What excites you about, you know,
[2288.08 --> 2290.52]  whatever it is the next six months, the next year,
[2290.52 --> 2293.02]  and what you think is kind of coming
[2293.02 --> 2295.64]  as this tooling rolls out there further and further,
[2295.78 --> 2297.66]  people learn to apply it better and better.
[2298.10 --> 2299.22]  What's exciting for you?
[2299.68 --> 2300.48]  That's a great question.
[2300.72 --> 2303.58]  I think there are lots of things
[2303.58 --> 2306.00]  that I think holds a lot of promise
[2306.00 --> 2308.12]  in the next six to 12 months.
[2308.12 --> 2314.76]  I think we'll see one is this explosion of retrieval,
[2315.12 --> 2317.00]  kind of information retrieval tools.
[2317.48 --> 2319.52]  So we already see a lot of companies
[2319.52 --> 2321.28]  that are adding like generative AI
[2321.28 --> 2323.64]  in like customer success management
[2323.64 --> 2327.74]  and like documentation and things like that.
[2327.82 --> 2330.98]  And so I think we'll see a lot of applications
[2330.98 --> 2333.44]  providing value that is, you know,
[2333.44 --> 2336.02]  that can be also personalized and, you know,
[2336.02 --> 2338.66]  not just like chat GPT style answers,
[2338.66 --> 2341.48]  but actually personalized to their own data
[2341.48 --> 2344.36]  or their own, you know, cases or things like that.
[2344.84 --> 2346.20]  And then number two is,
[2346.32 --> 2348.34]  I see a lot of successes
[2348.34 --> 2351.48]  in very domain specific agents
[2351.48 --> 2354.60]  that are able to dive deep into legal
[2354.60 --> 2357.74]  or healthcare or some domain very specifically
[2357.74 --> 2360.98]  and build things that seem sort of magical,
[2361.22 --> 2362.74]  whether it's, you know, compliance
[2362.74 --> 2364.36]  or driving better outcomes
[2364.36 --> 2366.50]  or, you know, creating things
[2366.50 --> 2369.14]  that would democratize a lot of these
[2369.14 --> 2373.44]  sort of like very deep expertise type of domains.
[2373.74 --> 2376.58]  And then I think a little bit further out
[2376.58 --> 2380.58]  are generalized like low code and no code tools
[2380.58 --> 2383.06]  for you to build, you know,
[2383.10 --> 2384.64]  very sophisticated applications
[2384.64 --> 2387.42]  using generative AI through code generation
[2387.42 --> 2389.76]  and sort of creative,
[2389.90 --> 2392.14]  let's say creative interfaces and things like that.
[2392.36 --> 2394.86]  So those are things I think will deliver
[2394.86 --> 2395.66]  in the short term.
[2395.90 --> 2397.56]  And then, you know, personally,
[2397.86 --> 2399.50]  like I love games
[2399.50 --> 2400.90]  and I'm actually super excited
[2400.90 --> 2403.38]  about what generative AI brings to gaming.
[2403.96 --> 2405.52]  You know, we talk about open world
[2405.52 --> 2406.76]  and things like that.
[2406.76 --> 2409.52]  And this is, this can be really open
[2409.52 --> 2411.86]  where you could just get lost
[2411.86 --> 2414.44]  for a long, long time in a generative world.
[2415.04 --> 2415.36]  It's awesome.
[2415.36 --> 2418.24]  Thank you so much for taking time to talk with us.
[2418.24 --> 2422.10]  And please pass on my thanks to the Lance DB team
[2422.10 --> 2425.92]  for making me look good in my day job
[2425.92 --> 2428.68]  by giving me great, great tools that work really well.
[2429.08 --> 2431.14]  Appreciate what you all are doing.
[2431.50 --> 2434.16]  And yeah, I just looking forward to seeing
[2434.16 --> 2436.78]  what comes over the coming months.
[2437.18 --> 2438.92]  And yeah, I encourage our listeners
[2438.92 --> 2440.30]  to check out the show notes,
[2440.52 --> 2442.90]  follow the links to Lance DB, try it out.
[2442.90 --> 2446.40]  It only takes a few minutes and hope to talk to you again soon.
[2446.52 --> 2447.12]  Thanks so much.
[2447.46 --> 2447.86]  Thank you, Daniel.
[2447.96 --> 2448.58]  Thank you, Chris.
[2448.90 --> 2450.80]  It was a super fun talking to you with you guys.
[2450.92 --> 2453.72]  And if you have any feedback, please let us know.
[2453.84 --> 2456.36]  We hope to make you look even better in the new year.
[2456.36 --> 2467.52]  Thank you for listening to Practical AI.
[2468.06 --> 2470.62]  Your next step is to subscribe now,
[2470.82 --> 2471.86]  if you haven't already.
[2472.30 --> 2474.08]  And if you're a longtime listener of the show,
[2474.42 --> 2477.18]  help us reach more people by sharing Practical AI
[2477.18 --> 2478.32]  with your friends and colleagues.
[2478.82 --> 2480.92]  Thanks once again to Fastly and Fly
[2480.92 --> 2483.70]  for partnering with us to bring you all Change Talk podcasts.
[2483.70 --> 2488.10]  Check out what they're up to at Fastly.com and Fly.io.
[2488.48 --> 2489.90]  And to our Beat Freakin' Residence,
[2490.04 --> 2490.90]  Breakmaster Cylinder,
[2491.06 --> 2493.80]  for continuously cranking out the best beats in the biz.
[2494.08 --> 2495.00]  That's all for now.
[2495.26 --> 2496.42]  We'll talk to you again next time.
[2496.42 --> 2510.08]  Game on!
