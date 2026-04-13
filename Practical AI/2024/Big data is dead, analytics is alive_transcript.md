[0.00 --> 7.28]  Welcome to Practical AI.
[7.70 --> 15.00]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[15.00 --> 17.72]  changing the world, this is the show for you.
[18.06 --> 20.68]  Thank you to our partners at Fly.io.
[21.16 --> 26.86]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on
[26.86 --> 30.72]  six continents, so you can launch your app near your users.
[31.28 --> 33.22]  Learn more at Fly.io.
[35.18 --> 41.80]  Hey friends, you know we're big fans of Fly.io, and I'm here with Kurt Mackey, co-founder and
[41.80 --> 43.38]  CEO of Fly.
[43.76 --> 47.84]  Kurt, we've had some conversations and I've heard you say that public clouds suck.
[48.20 --> 53.62]  What is your personal lens into public clouds sucking, and how does Fly not suck?
[53.62 --> 55.90]  All right, so public clouds suck.
[56.12 --> 60.60]  I actually think most ways of hosting stuff on the internet sucks, and I have a lot of
[60.60 --> 62.80]  theories about why this is, but it almost doesn't matter.
[62.96 --> 67.98]  The reality is, like, I've built a new app for, like, generating sandwich recipes because
[67.98 --> 72.32]  my family's just into specific types of sandwiches that use Braunschweiger as a component, for
[72.32 --> 72.68]  example.
[72.98 --> 74.82]  And then I want to, like, put that somewhere.
[75.24 --> 80.50]  You go to AWS, and it's harder than just going and getting, like, a dedicated server from
[80.50 --> 80.78]  Hetzner.
[80.78 --> 84.62]  It's, like, it's actually, like, more complicated to figure out how to deploy my dumb sandwich
[84.62 --> 89.56]  app on top of AWS because it's not built for me as a developer to be productive with.
[89.64 --> 90.86]  It's built for other people.
[90.98 --> 94.82]  It's built for platform teams to kind of build the infrastructure of their dreams and hopefully
[94.82 --> 97.90]  create a new UX that's useful for the developers that they work with.
[98.04 --> 101.22]  And again, I feel like every time I talk about this, it's like, I'm just too impatient.
[101.44 --> 106.64]  I don't particularly want to go figure so many things out purely to put my sandwich app
[106.64 --> 110.22]  in front of people, and I don't particularly want to have to go talk to a platform team
[110.22 --> 114.42]  once my sandwich app becomes a huge startup and IPOs and I have to, like, do a deploy.
[114.96 --> 119.70]  I kind of feel like all that stuff should just work for me without me having to go ask permission
[119.70 --> 121.14]  or talk to anyone else.
[121.50 --> 124.36]  And so this is a lot of, it's informed a lot of how we've built Fly.
[124.48 --> 125.70]  Like, we're still a public cloud.
[125.78 --> 130.08]  We still have a lot of very similar low-level primitives as the bigger guys.
[130.08 --> 134.30]  But in general, they're designed to be used directly by developers.
[134.30 --> 137.46]  They're not built for a platform team to kind of cobble together.
[137.58 --> 141.28]  They're designed to be useful quickly for developers.
[141.42 --> 145.40]  One of the ways we've thought about this is if you can turn a very difficult problem into
[145.40 --> 148.50]  a two-hour problem, people will build much more interesting types of apps.
[148.62 --> 152.40]  And so this is why we've done things like made it easy to run an app multi-region.
[152.56 --> 157.64]  Most companies don't run multi-region apps on public clouds because it's functionally impossible
[157.64 --> 160.72]  to do without a huge amount of upfront effort.
[161.08 --> 165.66]  It's why we've made things like the virtual machine primitives behind just a simple API.
[165.90 --> 169.86]  Most people don't do, like, code sandboxing or their own virtualization because it's just
[169.86 --> 171.20]  not really easy.
[171.46 --> 174.06]  It's not, there's just no path to that on top of the clouds.
[174.52 --> 179.18]  So in general, like, I feel like, and it's not really fair of me to say public clouds suck
[179.18 --> 180.58]  because they were built for a different time.
[180.66 --> 185.12]  If you build one of these things starting in 2007, the world's very different than it is
[185.12 --> 185.52]  right now.
[185.52 --> 190.32]  And so a lot of what I'm saying, I think, is that public clouds are kind of old and there's
[190.32 --> 193.80]  a new version of public clouds that we should all be building on top of that are definitely
[193.80 --> 198.30]  gonna make me as a developer much happier than I was like five or six years ago when
[198.30 --> 199.74]  I was kind of stuck in this quagmire.
[200.32 --> 203.98]  So AWS was built for a different era, a different cloud era.
[204.38 --> 209.42]  And Fly, a public cloud, yes, but a public cloud built for developers who ship.
[209.50 --> 210.20]  That's the difference.
[210.54 --> 212.92]  And we here at Change, all our developers who ship.
[212.92 --> 214.58]  So you should trust us.
[214.90 --> 217.14]  Try out Fly, Fly.io.
[217.50 --> 221.02]  Over 3 million apps, that includes us, have launched on Fly.
[221.36 --> 226.98]  They leverage the global anycast load balancing, the zero config private networking, hardware
[226.98 --> 233.04]  isolation, instant wire guard VPN connections with push button deployments, scaling to thousands
[233.04 --> 234.00]  of instances.
[234.70 --> 236.56]  This is the cloud you want.
[236.96 --> 237.46]  Check it out.
[237.78 --> 239.04]  Fly.io.
[239.04 --> 241.42]  Again, Fly.io.
[258.42 --> 262.08]  Welcome to another episode of the Practical AI Podcast.
[262.50 --> 264.18]  This is Daniel Whitenack.
[264.18 --> 270.22]  I am CEO at Prediction Guard, where we're building a private Securigen AI platform.
[270.66 --> 277.42]  And I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer
[277.42 --> 278.34]  at Lockheed Martin.
[278.60 --> 279.26]  How are you doing, Chris?
[279.54 --> 280.90]  Hey, doing very well today, Daniel.
[280.94 --> 281.34]  How's it going?
[281.74 --> 282.82]  It is going great.
[282.92 --> 288.92]  I'm super excited about this one because it's a very, you know, we schedule a lot of shows
[288.92 --> 291.06]  and they're all interesting, of course.
[292.08 --> 296.96]  But occasionally there's like a show on a topic that intersects with something that I'm
[296.96 --> 301.36]  working on at the moment or something that I found that is really exciting and, you know,
[301.48 --> 302.88]  found to be really useful.
[303.04 --> 310.14]  And so selfishly, I'm really extra excited about this episode this week, which is with
[310.14 --> 312.22]  Till and Aditya from Mother Duck.
[312.58 --> 313.02]  How are you doing?
[313.60 --> 314.18]  Doing good.
[314.58 --> 315.36]  Excited to be here.
[315.36 --> 315.80]  Yes.
[316.58 --> 318.96]  And note, duck as in the bird.
[319.34 --> 321.94]  So editors, you don't have to bleep us out.
[322.36 --> 326.26]  Sure, that's something that is an old, old joke for you all.
[326.80 --> 333.78]  I can pinpoint very easily how I ran across DuckDB and Mother Duck is there was a blog post.
[334.10 --> 335.64]  The title is very simple.
[335.78 --> 337.24]  It said Big Data is Dead.
[337.78 --> 341.80]  And immediately when I saw the title, I was like, thank goodness, finally.
[341.80 --> 347.50]  But I'm wondering, like, if you can maybe just kind of step back.
[347.62 --> 353.56]  It doesn't necessarily have to be the points in that blog post, but how you see the kind
[353.56 --> 360.24]  of data analytics, big data, AI intersections as of now.
[360.24 --> 366.90]  And what are the sort of concerns and issues that people are thinking about that is driving
[366.90 --> 368.28]  them to DuckDB?
[368.60 --> 372.54]  And then, of course, we'll obviously get into DuckDB and Mother Duck and all that you're
[372.54 --> 372.84]  doing.
[372.96 --> 376.20]  But setting that stage of, you know, what are people struggling with?
[376.28 --> 381.72]  What have they realized in the past about this sort of big data hype in one way or the
[381.72 --> 382.90]  other, positive or negative?
[382.90 --> 389.24]  And how has that kind of changed the way that people are thinking about analytics and databases?
[389.80 --> 393.36]  I can tell a story about how I got in touch with DuckDB.
[393.90 --> 397.54]  It started at the very beginning of the DuckDB project.
[397.80 --> 405.32]  I was actually doing my master's thesis back then at the CWI where DuckDB originated from.
[405.32 --> 414.80]  And after I graduated, Hannes, who is the developer or the founder of DuckDB Labs, reached out and
[414.80 --> 418.28]  we were talking and they were saying, hey, we're working on this new project.
[418.28 --> 421.38]  We're working on this database system.
[421.76 --> 425.38]  Are you interested in like maybe joining, maybe working on it?
[425.44 --> 429.44]  But I was very focused on machine learning and stuff like this.
[429.48 --> 434.24]  So I wanted to go into data analytics, data science, these kind of things.
[434.24 --> 441.28]  So a year later or so, I was working at a telco company and we were analyzing, you know,
[441.32 --> 443.56]  customer data with Spark and so on.
[444.40 --> 449.04]  And one day there was like one of the first versions of DuckDB was released.
[449.22 --> 455.42]  So I pip installed it and I run the first like simple aggregation query on a maybe 100
[455.42 --> 457.20]  megabyte data set or something like this.
[457.34 --> 460.56]  And I was surprised because I thought something was going wrong.
[460.56 --> 464.86]  I thought it's impossible that it just did the aggregation, right?
[464.92 --> 470.82]  Because from working with Spark, I was so used to, okay, now spinner starting for 10 seconds
[470.82 --> 471.42]  at least.
[472.20 --> 472.34]  Right.
[472.44 --> 474.14]  And then that was really eye opening.
[474.34 --> 478.06]  And I've heard similar experience from a lot of people.
[478.32 --> 483.04]  Even until today, I hear very similar stories and experiences.
[483.04 --> 487.64]  Yeah, for me, it started in a different way.
[488.18 --> 494.20]  I first figured out DuckDB Wasom existed, that you could run an analytical engine in the
[494.20 --> 494.54]  browser.
[495.64 --> 498.96]  And to think about something like that was super crazy.
[499.56 --> 503.90]  And the kind of stuff that you could do on top of it started to look super crazy.
[504.08 --> 509.08]  And one of the things that I was super excited about when DuckDB Wasom released was the possibility
[509.08 --> 511.18]  to do geospatial analytics.
[511.18 --> 518.16]  So back then, when I started, my first encounter with DuckDB was doing geospatial analytics.
[518.88 --> 524.00]  And then to think about that could actually be done in the browser was mind-blowing.
[524.44 --> 526.54]  And that's when my journey into DuckDB started.
[527.12 --> 531.04]  So let me ask you all a follow-up question as you're diving into your passion.
[531.26 --> 535.96]  For those out there who may be listening who are not already familiar with it, and they're
[535.96 --> 540.66]  hearing database, they're hearing big data is dead, they're hearing doing this in the
[540.66 --> 541.08]  browser.
[541.62 --> 547.72]  Give me a little bit of background on kind of the ecosystem that you were coming from
[547.72 --> 554.20]  a bit and also what this idea was so that people can kind of follow you into that.
[554.20 --> 560.08]  What is it that caught your passion and attention and made you say, ah, this is the way?
[560.08 --> 563.42]  And assume somebody doesn't already have a familiarity with it.
[564.16 --> 570.70]  So I guess I was going into this coming from the machine learning side of things.
[571.00 --> 578.88]  So I was used to working with scikit-learn pandas or the Spark equivalents to that, like
[578.88 --> 583.52]  Spark ML, building data prep pipelines and so on and so forth.
[583.52 --> 590.84]  So, and then encountering this DuckDB thing suddenly that apparently is doing aggregations
[590.84 --> 595.32]  of the sizes of data I was working with much, much, much faster.
[595.90 --> 596.14]  Yeah.
[596.22 --> 602.66]  Sparked some fantasies around, hey, how much of the data preparation pipeline can we push
[602.66 --> 604.00]  into DuckDB actually?
[604.00 --> 610.56]  And this idea or this fantasy has been following me, you know, for the past years and I think
[610.56 --> 611.92]  it's still an exciting topic.
[612.66 --> 618.22]  To follow up a little bit on that, the way that large data or big data has been analyzed
[618.22 --> 624.08]  in the last years, I mean, predominantly that you required some server in the cloud, you required
[624.08 --> 628.12]  resources that were not local to be able to perform like large analysis.
[628.12 --> 634.30]  But something that DuckDB opened up that made possible was to use local compute in your local
[634.30 --> 642.72]  Mac book, for example, was to utilize that compute at the most to like perform this kind of huge
[642.72 --> 643.80]  analysis.
[644.88 --> 650.96]  And that, I guess, sets Spark to a change in the ecosystem, I would say.
[651.50 --> 653.16]  And I guess that's where we're at.
[653.64 --> 655.56]  I resonate so much with this.
[655.56 --> 661.50]  So like coming from a background also as a data scientist, living through the years of
[661.50 --> 664.96]  like being told, hey, you know, use Spark for this.
[665.44 --> 671.00]  Like basically my experience in this sort of ecosystem was like I would try to write a query
[671.00 --> 673.52]  and it would get the right result.
[673.88 --> 678.44]  But to your point, Till, like I would just be waiting forever to get a result.
[678.58 --> 682.60]  And so I'd have to send it to some like other guy whose name was Eugene.
[682.60 --> 686.50]  Eugene was really smart and he could figure out a way to like make it go fast.
[686.62 --> 688.10]  And I never became Eugene.
[688.70 --> 690.66]  So like I resonated with this very much.
[691.26 --> 697.16]  And the fact that this concept of, hey, there's these seemingly big data sets out there.
[697.16 --> 706.90]  And I want to do maybe even complicated analytics types of queries over these or even, you know,
[706.94 --> 714.46]  execute workflows of, as you mentioned, Till aggregation or other processes at query time.
[714.46 --> 722.42]  I could do that with a system that I could just run on my laptop or I could run in process is really intriguing.
[722.42 --> 727.46]  So maybe now is a good time then to like introduce DuckDB formally.
[727.70 --> 729.34]  So like I'm on the DuckDB side.
[729.46 --> 733.68]  It says DuckDB is a fast in process analytical database.
[734.28 --> 740.52]  So maybe one of you could like take a stab at, you know, thinking about those data scientists out there
[740.52 --> 746.80]  who are maybe at the point of not also not believing that what we just described is is maybe possible
[746.80 --> 749.22]  or they're living in a world where that's not possible.
[749.62 --> 756.50]  Describe what DuckDB is and maybe why that becomes possible as a function of what it is.
[757.06 --> 764.30]  I think I can talk a little bit about the motivation behind DuckDB or at least the way I perceived it at the time.
[764.30 --> 769.64]  And that was actually originated from the R ecosystem.
[769.64 --> 781.62]  Yeah, so Hannes was very involved in that ecosystem and people were using R to essentially crunch relatively large data
[781.62 --> 785.62]  with relatively primitive methods.
[786.70 --> 794.78]  And so at the time CWI had a database system and an analytical database system called Monedeby
[794.78 --> 802.90]  that has incorporated the idea of vectorized columnar query execution.
[803.84 --> 812.16]  And it was a large system that was not really easy for the typical R users to adopt.
[812.82 --> 818.88]  So the first idea was to say, hey, let's maybe build a light version of Monedeby
[818.88 --> 824.78]  and integrate it with, I think it was Dplyr or something like this.
[824.88 --> 827.16]  And we just let it run on the client.
[827.82 --> 834.08]  But eventually it turned out to be easier maybe to just rebuild the, you know,
[834.08 --> 838.84]  a database system from scratch that was actually designed to run in process,
[838.84 --> 843.02]  to be super lightweight, super easy to install and everything,
[843.02 --> 851.06]  essentially to give the power of this vectorized query execution into the hands of data analysts.
[851.76 --> 856.60]  I'm wondering if you could, when you talk about that being in process and lightweight,
[856.96 --> 862.54]  could you describe what that means for someone that may not be familiar with the term in process?
[863.18 --> 867.42]  And how is that different from other databases that are not in process,
[867.74 --> 868.94]  you know, that have their own processes?
[869.60 --> 872.12]  Can you describe a little bit of what that means?
[872.12 --> 878.76]  So classical database systems operate in the client server architecture.
[879.14 --> 885.68]  Usually you have a database server running somewhere and you have a client that sends SQL queries
[885.68 --> 888.16]  essentially to the database server.
[888.44 --> 893.66]  And then the result is transferred back to the client through some kind of transfer protocol.
[893.66 --> 902.34]  And one paper that Tannis and Mark, who is Mark Brassford, who is also co-founder of Dr. B. Lapsus,
[902.54 --> 907.04]  they were working on a paper that basically benchmarked these client protocols.
[907.28 --> 910.12]  And it turned out that that was actually a huge bottleneck.
[910.50 --> 914.12]  So even when you're running Postgres on your local machine,
[914.68 --> 917.66]  you still have this client server protocol bottleneck.
[917.66 --> 926.08]  So, and the way to get around this is to have the database actually running within your process that is,
[926.40 --> 936.16]  you know, in that case, maybe R or Python and has access to the result set just in memory.
[936.16 --> 939.96]  And no transfers to happen.
[939.96 --> 947.94]  And maybe I'd like to just add in that if for those who maybe haven't done programming and stuff in our audience,
[948.10 --> 955.04]  that when it's expensive to go between processes and so that database server in a different process,
[955.20 --> 959.04]  it takes a lot of resource to go from the process you're in off to that and back.
[959.14 --> 965.26]  And so this puts it all into one, you might say, one little sandbox where you're able to maximize that.
[965.34 --> 966.64]  Would that be a fair assessment?
[966.64 --> 967.16]  Yeah.
[967.38 --> 967.60]  Yeah.
[967.74 --> 974.06]  So I think one of the other advantages of having this type of a model is that you can share memory between the processes.
[974.38 --> 977.46]  So just to go a little bit inside the technical aspects of this,
[977.88 --> 982.52]  is that the bottleneck that Till was explaining was more like the data transfer bottleneck.
[982.86 --> 986.78]  But in this case, when it's running within the process, you can share the same memory.
[986.92 --> 990.92]  You can share the variables that you're crunching inside.
[991.16 --> 993.36]  Let's say a Python script that you're crunching a variable,
[993.36 --> 997.48]  and then you have access to the variable inside your database as well, for an example.
[998.14 --> 1002.48]  And this makes it super powerful for the developer, for the developer experience as well.
[1002.82 --> 1008.00]  And I guess one of the things that apart from the database itself being super fast,
[1008.44 --> 1013.28]  the developer experience of using DuckDB is so awesome in that sense,
[1013.48 --> 1016.32]  that I guess that has also led to the success of it.
[1016.32 --> 1029.12]  Okay, friends, I'm here with a new friend of ours over at Timescale Avthar Suwathan.
[1029.52 --> 1032.86]  So Avthar, help me understand what exactly is Timescale?
[1033.08 --> 1034.64]  So Timescale is a Postgres company.
[1035.18 --> 1041.28]  We build tools in the cloud and in the open source ecosystem that allow developers to do more with Postgres.
[1041.28 --> 1047.46]  So using it for things like time series, analytics, and more recently, AI applications like RAG and Search and Agents.
[1047.72 --> 1053.68]  Okay, if our listeners were trying to get started with Postgres, Timescale, AI application development,
[1054.20 --> 1054.88]  what would you tell them?
[1055.20 --> 1055.88]  What's a good roadmap?
[1056.18 --> 1061.18]  If you're a developer out there, you're either getting tasked with building an AI application,
[1061.40 --> 1065.86]  or you're interested and you're seeing all the innovation going on in the space and want to get involved yourself.
[1065.86 --> 1073.44]  And the good news is that any developer today can become an AI engineer using tools that they already know and love.
[1073.68 --> 1079.96]  And so the work that we've been doing at Timescale with the PGAI project is allowing developers to build AI applications
[1079.96 --> 1084.42]  with the tools and with the database that they already know, and that being Postgres.
[1084.76 --> 1089.40]  What this means is that you can actually level up your career, you can build new interesting projects,
[1089.68 --> 1093.76]  you can add more skills without learning a whole new set of technologies.
[1093.76 --> 1099.64]  And the best part is it's all open source, both PGAI and PG Vector Scale are open source.
[1099.78 --> 1104.90]  You can go and spin it up on your local machine via Docker, follow one of the tutorials on the Timescale blog,
[1105.12 --> 1111.02]  build these cutting edge applications like RAG and Search without having to learn 10 different new technologies
[1111.02 --> 1116.08]  and just using Postgres in the SQL query language that you will probably already know and are familiar with.
[1116.40 --> 1117.48]  So yeah, that's it.
[1117.54 --> 1118.28]  Get started today.
[1118.50 --> 1120.02]  It's a PGAI project.
[1120.02 --> 1125.78]  And just go to any of the Timescale GitHub repos, either the PGAI one or the PG Vector Scale one,
[1125.90 --> 1131.08]  and follow one of the tutorials to get started with becoming an AI engineer just using Postgres.
[1131.54 --> 1137.18]  Okay, just use Postgres and just use Postgres to get started with AI development,
[1137.62 --> 1141.66]  build RAG, search, AI agents, and it's all open source.
[1141.66 --> 1144.96]  Go to timescale.com slash AI.
[1145.58 --> 1147.14]  Play with PGAI.
[1147.28 --> 1148.92]  Play with PG Vector Scale.
[1149.16 --> 1151.10]  All locally on your desktop.
[1151.26 --> 1152.14]  It's open source.
[1152.62 --> 1155.82]  Once again, timescale.com slash AI.
[1171.66 --> 1183.64]  So Aditya, you were just describing the developer experience, which I would definitely say is kind of fitting that magical experience
[1183.64 --> 1187.22]  that you alluded to with DuckDB.
[1187.54 --> 1193.20]  And maybe just to give a sense of people, like, you know, when I was initially exploring this,
[1193.26 --> 1195.70]  similar to some of the experiences that you all talked about,
[1195.70 --> 1202.88]  I would encourage our listeners to go out and install DuckDB locally and try something because it is a really interesting experience,
[1202.94 --> 1208.42]  especially for those that have worked with traditional database systems in the past.
[1208.68 --> 1214.64]  And all of a sudden, so you kind of install DuckDB locally, import it as a library,
[1214.64 --> 1223.28]  then you can query, you know, point to CSV files or JSON files or Parquet files or even a database like a Postgres database
[1223.28 --> 1225.80]  or data stored in an S3 bucket.
[1225.80 --> 1234.94]  And you have this consistent then SQL interface that's familiar that you can do queries over that data.
[1235.48 --> 1241.88]  So I don't know, maybe one of you could describe some of the, you know,
[1241.88 --> 1251.42]  just to give people a sense of the use cases for DuckDB, maybe on one side where it's like the primary or the key
[1251.42 --> 1258.74]  or the most often occurring use cases that you see people grabbing DuckDB and using it for.
[1259.22 --> 1265.06]  And then maybe on the other side, just to kind of help people understand where it fits,
[1265.18 --> 1270.74]  maybe where it wouldn't be as relevant if you have any of those thoughts.
[1270.74 --> 1273.30]  I can give like a brief overview of this.
[1273.72 --> 1278.06]  Some of the biggest users of DuckDB come from the Python ecosystem,
[1278.72 --> 1285.00]  which means that it's being a stand-in for a data frame, for example.
[1285.72 --> 1290.86]  And one of the advantages of using DuckDB is that it's really fast on aggregates.
[1291.48 --> 1296.92]  And for the Python ecosystem, it helps with standing in for a data frame
[1296.92 --> 1300.08]  to be used with other ML libraries, for example.
[1300.08 --> 1303.32]  So that's like one part of the ecosystem.
[1303.42 --> 1308.06]  And the other part of the ecosystem is for a data engineer to be able to pull in data
[1308.06 --> 1311.38]  from different sources, like you said, you know, Postgres, from CSV,
[1311.76 --> 1314.86]  and to be able to join those different data sets.
[1315.96 --> 1317.98]  Joins are really good with DuckDB as well.
[1318.36 --> 1323.08]  And to create transformed data sets is also pretty useful.
[1323.08 --> 1328.36]  And on the third ecosystem for a data analyst who is writing SQL,
[1328.82 --> 1333.62]  and one of the really nice aspects of DuckDB is the SQL dialect itself.
[1334.00 --> 1339.78]  It's pretty flavored that you have a lot of DuckDB functions that makes data cleaning easy,
[1339.92 --> 1341.12]  data transformation easy.
[1341.82 --> 1345.62]  For example, we also have a dialect that says from table,
[1345.62 --> 1347.86]  and that's just going to show you the table.
[1348.18 --> 1352.34]  Instead of going select start from table, you can go from table,
[1352.46 --> 1355.20]  and that will, you know, just fetch data from that table.
[1355.40 --> 1359.98]  So there are these flavors of dialect for DuckDB that makes it nice.
[1360.38 --> 1363.88]  You know, I was also looking through the DuckDB website and stuff,
[1363.88 --> 1368.30]  and I know it runs on kind of all the major platforms and architectures,
[1368.48 --> 1371.88]  and you support a variety of languages on it.
[1372.24 --> 1377.84]  I'm curious, because I'm asking a question to my own interest selfishly,
[1377.90 --> 1382.12]  as Dan would say, do you support kind of embedded environments
[1382.12 --> 1385.16]  and kind of, you know, on the edge, that kind of stuff,
[1385.56 --> 1387.96]  where you find it embedded and operating,
[1388.46 --> 1390.96]  where it's not necessarily, you know, on a cloud server
[1390.96 --> 1392.14]  on one of the major platforms?
[1392.14 --> 1393.86]  Is that a typical use case?
[1394.38 --> 1397.60]  That is one of good use cases for DuckDB.
[1398.08 --> 1402.40]  Since it's the in-process protocol that it has for running DuckDB,
[1402.82 --> 1407.42]  it can run wherever you run Python or R or anywhere.
[1408.14 --> 1412.56]  And they've also optimized it to run in different architectures as well.
[1413.08 --> 1414.72]  So this makes it possible.
[1415.06 --> 1419.38]  And to kind of go beyond that, you can also run it in the browser.
[1419.38 --> 1422.16]  So any edge environment, you can run it.
[1422.56 --> 1424.14]  Of course, there's a lot of optimization for,
[1424.58 --> 1426.92]  there are like a lot of edge environments at the moment.
[1427.32 --> 1430.08]  Not everything is optimized to run DuckDB,
[1430.34 --> 1434.68]  but I guess it's also moving towards being run in every edge environment as well.
[1434.68 --> 1439.14]  Some of our listeners might be curious why, you know,
[1439.36 --> 1443.02]  a person like me is sort of living day to day in the AI world,
[1443.02 --> 1447.52]  is thinking, is super excited to talk about DuckDB.
[1447.74 --> 1451.24]  I mean, certainly I have a past in more broadly data science,
[1451.24 --> 1452.92]  and this is pain I've felt over time.
[1452.92 --> 1461.36]  But also there's a very relevant piece of this that intersects with the needs of the AI community
[1461.36 --> 1464.88]  more broadly and the workflows that they're executing.
[1465.62 --> 1470.96]  And one of those, you know, is where I kind of started getting into this,
[1471.02 --> 1477.54]  is in these sort of dashboard killing AI apps that people are trying to build in the sense that like,
[1477.54 --> 1483.26]  hey, another pain of mine as a data scientist in my life is building dashboards,
[1483.36 --> 1485.04]  because you always build them and, you know,
[1485.10 --> 1487.82]  they never answer the questions that people actually have.
[1488.26 --> 1493.06]  And so there's this real desire to have like a natural language question input.
[1493.32 --> 1499.40]  And then you can then compute very quickly the answer to that natural language question
[1499.40 --> 1504.26]  by using the LM to generate a SQL query to a number of data sources.
[1504.26 --> 1509.24]  But then when you start thinking about, oh, well, now I have these CSV files
[1509.24 --> 1511.76]  that people have uploaded into a chat interface,
[1511.76 --> 1515.60]  or I have these types of databases that I need to connect to,
[1515.68 --> 1517.72]  or I have this data in S3 buckets,
[1518.14 --> 1520.62]  and my answer could come from these different places.
[1520.76 --> 1525.48]  All of a sudden, this kind of rich SQL dialect that you talked about,
[1525.54 --> 1532.24]  that's very quick and can run with a standardized API across those sources,
[1532.24 --> 1535.76]  becomes incredibly intriguing for me.
[1536.80 --> 1540.06]  Transparently, that's how I sort of like got into this is I'm like,
[1540.44 --> 1545.90]  thinking of all of these sources of data that I could answer questions out of using an LM.
[1546.32 --> 1553.00]  But how do I standardize a fast interface to all of these diverse sets of data,
[1553.00 --> 1555.66]  and also do it in a way that doesn't, you know,
[1555.98 --> 1558.92]  is easy to use from a developer's perspective.
[1558.92 --> 1563.32]  But I also know that you all see much more than I do,
[1563.46 --> 1566.36]  and maybe that is an entry point that you're seeing.
[1566.52 --> 1569.60]  I'm wondering if one of you could talk a little bit more broadly
[1569.60 --> 1572.64]  of how the problems that DuckDB is solving
[1572.64 --> 1575.66]  and the problems that your customers are looking at
[1575.66 --> 1580.96]  are intersecting with this rapidly developing world of AI workflows.
[1581.46 --> 1586.58]  I mean, one way to describe DuckDB is it's the SQLite for analytics.
[1586.58 --> 1593.14]  So it is basically a very easy way,
[1593.34 --> 1596.90]  a very developer-friendly way to achieve what you just described.
[1597.08 --> 1601.78]  If I want to create a demo for my new text-to-SQL model,
[1602.24 --> 1603.94]  if I use DuckDB for it,
[1604.12 --> 1610.58]  I can even make a completely like wasn't-based demo out of it, for example.
[1610.58 --> 1615.18]  I don't have any issues with CSV upload.
[1615.72 --> 1621.50]  There might be databases where I have to specify the limiter of the file that the user uploads.
[1621.66 --> 1624.44]  So I would have to show a dialogue to my user where it says,
[1624.58 --> 1628.96]  oh, that's comma separated and it has a header row and so on.
[1629.50 --> 1631.10]  With DuckDB, it just works.
[1631.10 --> 1636.70]  So it takes away some of the edges you might have with other databases.
[1637.60 --> 1639.68]  And on top of that, as you said,
[1639.76 --> 1644.80]  it integrates with different storage backends like it can read from S3,
[1645.02 --> 1647.10]  it can read from HTTP.
[1647.84 --> 1652.30]  When I see an interesting file on, let's say, Hugging Face or GitHub,
[1652.30 --> 1660.48]  I just run read CSV from this URL and I have the data set locally in my CLI or in my Python.
[1661.02 --> 1665.10]  Furthermore, when I have a, say, a Python environment,
[1665.46 --> 1668.40]  I start a colab notebook, right?
[1668.46 --> 1670.08]  And I create some data frames.
[1670.26 --> 1673.82]  Then with DuckDB, I can just read those data frames.
[1673.96 --> 1678.14]  I've seen very cool demos of people basically using text-to-SQL
[1678.14 --> 1682.18]  for analytics on Pandas data frames.
[1682.86 --> 1686.58]  And under the hood, it's just DuckDB sitting there
[1686.58 --> 1691.08]  and basically reading straight from those Pandas data frames,
[1691.20 --> 1696.24]  which, by the way, is one of the other benefits of shared memory of in-process.
[1696.66 --> 1699.58]  It's not only for fetching results,
[1699.58 --> 1702.86]  it's also for reading data straight from the process.
[1703.06 --> 1704.26]  So in that case, from Pandas.
[1705.16 --> 1706.28]  That's very exciting.
[1706.28 --> 1709.16]  I'm happy to talk more about text-to-SQL.
[1709.46 --> 1712.98]  We have had a project about that at MotherDuck.
[1713.38 --> 1714.36]  But yeah.
[1714.84 --> 1715.00]  Yeah.
[1715.14 --> 1720.28]  And maybe also, before we get into maybe some of those stories,
[1720.78 --> 1728.22]  I think that that's one side of it is like the integration of this analytics piece into AI workflows.
[1728.40 --> 1730.66]  But then also, if I'm not mistaken,
[1730.84 --> 1735.24]  there is sort of vector search capabilities within DuckDB as well.
[1735.24 --> 1737.28]  I don't know if one of you could speak to that.
[1737.70 --> 1737.86]  Yeah.
[1738.10 --> 1740.92]  That's one of the exciting aspects of DuckDB as well.
[1740.92 --> 1748.12]  So if I could take a step back and think about other ecosystems where, let's say, Postgres has been shining a lot.
[1748.30 --> 1751.80]  Postgres has exploded into the kind of possibilities that you can do
[1751.80 --> 1758.32]  because it has kind of like an amazing extension mechanism where you could add extensions and capabilities of Postgres.
[1758.32 --> 1766.78]  And in a similar way, DuckDB has an extension mechanism that you have access to the internal workings of DuckDB.
[1767.12 --> 1771.82]  And you could add more workflows on top of what DuckDB can do.
[1772.28 --> 1776.88]  DuckDB has these capabilities of doing vector search, for example.
[1776.88 --> 1786.20]  And it also has hybrid search, where you also have full text search and vector search that you could put together to create hybrid search.
[1786.58 --> 1789.84]  One of the ways it does is that it has a really nice data type.
[1790.26 --> 1795.52]  I can go into the rabbit hole of the inner workings of how they make this happen, which is also pretty exciting.
[1795.52 --> 1804.98]  But one of the things that they make this possible is to provide an array data type where you can have an array of floating points.
[1805.40 --> 1807.58]  And then you can store this as a data type.
[1807.72 --> 1813.06]  And then that eventually becomes an embedding vector that you can do cosine similarity against.
[1813.54 --> 1816.12]  So that is to do like an embedding based search.
[1816.12 --> 1825.14]  Then you can also have full text search where you can create a inverted index of keywords to your documents.
[1825.38 --> 1831.84]  And you can search across your keywords to find your ideal documents and rank them according to the score.
[1832.00 --> 1839.62]  And then you could fuse both of these scores from embedding search and from full text search to have like a hybrid search.
[1840.16 --> 1843.04]  So, yeah, so all of these are possible and they're very accessible.
[1846.12 --> 1859.58]  Well, there's no shortage of helpful AI tools out there.
[1859.58 --> 1866.42]  But using these AI tools means you got to switch back and forth, back and forth between yet one more tool.
[1866.84 --> 1869.84]  So instead of simplifying your workflow, it just gets more complicated.
[1870.40 --> 1872.90]  But that's not how it works when you're using Notion.
[1872.90 --> 1876.98]  Notion is the perfect place to organize lots of stuff.
[1877.10 --> 1882.80]  Tasks, tracking your habits, writing beautiful docs, collaborating with your team, knowledge bases.
[1883.16 --> 1891.20]  And the more content you add to Notion, the more this cool thing called Notion AI can personalize all of the responses for you.
[1891.52 --> 1896.16]  Unlike generic chatbots, Notion AI already has the context of your work.
[1896.24 --> 1899.14]  Plus, it has multiple knowledge sources.
[1899.14 --> 1904.66]  It uses AI knowledge from GPT-4 and Cloud, and that helps you chat about any topic.
[1905.04 --> 1906.10]  And here's the kicker.
[1906.30 --> 1914.94]  Now in beta, Notion AI can search across Slack discussions, Google Docs, Sheets, Slides, and even more tools like GitHub and Jira.
[1915.34 --> 1916.18]  Those are coming soon.
[1916.18 --> 1928.12]  And unlike specialized tools or legacy suites that have you bouncing between different applications, Notion is seamlessly integrated, infinitely flexible, and beautifully easy to use.
[1928.22 --> 1932.10]  So you are empowered to do your most meaningful work inside Notion.
[1932.10 --> 1950.78]  From small teams to massive Fortune 500 companies, these teams, both small and large, use Notion to send less email, cancel more meetings, save time searching for their work, and they reduce spending on tools, which helps everyone stay on the same page.
[1950.78 --> 1956.50]  You can try Notion for free today by going to notion.com slash practical AI.
[1956.98 --> 1965.84]  That's all over case, notion.com slash practical AI to try the powerful, easy to use Notion AI today.
[1966.26 --> 1970.38]  And of course, when you use our link, you're supporting our show, and I know you love that.
[1970.64 --> 1973.88]  Again, notion.com slash practical AI.
[1980.78 --> 1992.94]  So, Till, you are starting to get into even some of the things now that you're doing at Mother Duck on top of DuckDB.
[1993.64 --> 2002.24]  I'm wondering, you know, hopefully we can get to some of those use cases or the things that you've been doing with customers or internally.
[2002.24 --> 2017.02]  But I'm wondering, before we do that, you know, I see also this sort of story about DuckDB's efficiency, but with this kind of multiplayer aspect as part of what you're doing at DuckDB.
[2017.02 --> 2033.68]  So, maybe one of you could describe kind of, now I think we have a sense of what DuckDB is, and it's this free thing that, you know, is open and I can pull down, I can install, I can run it very quickly, run it on my laptop, run it in my browser, do these analytics queries.
[2034.32 --> 2043.24]  So, now kind of describe maybe a little bit of how you're taking that further with Mother Duck and how you're thinking about some of the enterprise use cases.
[2043.24 --> 2051.32]  I like to describe Mother Duck as giving your DuckDB a cloud companion.
[2052.06 --> 2068.72]  So, it's easy to think or to associate, okay, we bring Mother Duck to the cloud, which is one way how we describe ourselves as well, to associate that with we provide infinite scale up in the cloud.
[2068.72 --> 2080.72]  You give us a workload and we start how many hundred DuckDBs in the background that, in a task-like fashion, let's say, process your data concurrently.
[2080.72 --> 2104.46]  But, actually, one of the hypotheses that Mother Duck is based on, or that the company was founded on, is that actually single node compute, which means one DuckDB database, with nowadays hardware, cloud hardware, actually gets you very, very, very far.
[2104.46 --> 2120.16]  So, when your local compute resources reach a limit, you will have cloud cloud, single cloud instances with up to, how much is it, 24 terabyte of memory?
[2120.62 --> 2122.86]  That's relatively big data.
[2123.46 --> 2126.10]  So, that's one aspect, right?
[2126.16 --> 2129.26]  So, scaling up with one cloud companion, DuckDB.
[2130.10 --> 2133.56]  Another aspect is, yeah, collaboration.
[2133.56 --> 2142.26]  So, once you are connected to a cloud instance, you can have shared context with other users in your organization.
[2142.88 --> 2144.92]  You can create shared data sets.
[2145.66 --> 2149.60]  You can have shared notebooks, and so on and so forth.
[2149.98 --> 2160.72]  And with that, of course, comes all the enterprise SOC 2 kind of things that some of the enterprise customers require to adopt tools like DuckDB.
[2160.72 --> 2161.72]  Thank you.
[2161.72 --> 2167.94]  I'm curious if you could, you really captured my imagination with that description.
[2168.26 --> 2175.56]  And so, like, because, you know, by drawing, for instance, with kind of, you know, the old school Postgres things that people would do with that.
[2175.56 --> 2180.56]  And you just talked about having many DuckDB instances operating concurrently.
[2181.66 --> 2188.00]  You know, what kinds of problems, kind of, you know, grounding it in a practical way from a user's perspective.
[2188.00 --> 2201.52]  What kind of problems do you see people solving with that kind of architecture and that new capability that they may not have historically had over the years with previous database capabilities on other platforms?
[2202.14 --> 2205.56]  What new sets of concerns can they address now with those?
[2205.56 --> 2218.62]  I would come from the perspective on this that there are a lot of companies out there that when they want to go to the cloud with their analytics workload, they have relatively limited choices.
[2219.28 --> 2222.88]  One of those choices is, like, Snowflake or Databricks.
[2223.48 --> 2225.48]  And they, of course, are optimized.
[2225.64 --> 2228.28]  Those systems are optimized for a big data scale.
[2228.28 --> 2246.78]  So, but then one of our observations is that a lot of companies actually don't have that amount of data when they run queries or they might have big data, but the queries they are running only access a very small subset of the data, for example.
[2247.48 --> 2250.08]  You know, you run monthly reports.
[2250.38 --> 2253.48]  They don't touch your entire historic data set.
[2253.48 --> 2266.10]  So, those companies might want to have something that is easier, first, easier to use, easier to set up, and that's also more cost-efficient than other existing solutions.
[2266.52 --> 2282.34]  One of the things that we haven't touched upon in this yet is kind of how MotherDuck and DuckDB go hand-in-hand with, like, the remote and the local aspect, where you have on your local and your remote the same client,
[2282.34 --> 2288.64]  so that you could actually, you're running the same thing, so it's easy to go from one place to the other doing the same thing.
[2289.24 --> 2303.16]  And what MotherDuck also provides is a dual execution where your local DuckDB, if you're running it locally, can communicate with your remote MotherDuck and execute seamlessly between both.
[2303.16 --> 2315.74]  And, for example, a query where you have a table in your local DuckDB and you want to join it with a remote DuckDB, you can join both of these tables together to run an aggregate.
[2316.10 --> 2329.36]  And then there's, like, a query optimization that we run where we transfer the data which was required from the remote to your local or from your local to remote and execute it intelligently in a way, if I could say that.
[2329.36 --> 2338.64]  And this kind of opens up new opportunities in, like, the dual execution aspect of running the local and the remote with the same client.
[2339.10 --> 2349.48]  I'm curious, again, selfish question, is you're doing that and you have the local version and the remote version, the connection between the two there, you know, what does that look like?
[2349.48 --> 2358.76]  Is it something that if they're widely separated, if, you know, MotherDuck's in the cloud and I'm out on a device that's not cloud-based, is that efficient communication?
[2359.06 --> 2361.28]  How do you all handle those different types of use cases?
[2362.16 --> 2371.74]  Yeah, so one of the principles of this dual execution is to reduce the amount of data that has to be transferred as much as possible.
[2371.74 --> 2381.90]  One of the use cases, for example, is I have a really large data set on S3 and I want to join it with a small table that I have on my notebook.
[2381.90 --> 2403.10]  So, in that case, an optimizer, query optimizer, will make the decision to, instead of downloading the one terabyte data set to your local device and doing the join there, to instead upload your small local file to the cloud worker and do the processing there.
[2403.10 --> 2406.64]  So, that saves, in that case, a lot of bandwidth.
[2406.98 --> 2409.94]  The same with, you know, filter pushdown.
[2410.10 --> 2416.86]  I query a large data set on S3 again and the transfer only has to happen for the filter.
[2417.08 --> 2422.02]  And that's, you can get something similar with DuckDB as well if the data is partitioned.
[2422.14 --> 2428.32]  So, DuckDB has clever ways to optimize remote file access as well without MotherDuck.
[2428.32 --> 2440.94]  But the thing you get with MotherDuck is it even filters the data if your data is not partitioned because the cloud worker still takes care of doing the bulk of the work and only gives you the result you actually want and need.
[2440.94 --> 2458.64]  A lot of what we've talked about are the features of DuckDB and then what MotherDuck is adding on that and also how that intersects with AI workflows like the text-to-SQL case or the RAG case where we're doing, you know, vector or semantic search or we're doing hybrid search.
[2458.64 --> 2463.60]  All of those things are super relevant to people building their AI workflows.
[2464.12 --> 2479.04]  But I also find it interesting that I see, Till, you wrote one of the blog posts that I'm looking at now, which is like you're also thinking as a company about how to use AI intelligently in your own product as well.
[2479.04 --> 2491.80]  For the users of your product who are maybe technical users, they're building their own workflows, but also you have sort of AI integrated into some of the features of that.
[2491.90 --> 2493.90]  I'm looking at this fix-it feature.
[2494.08 --> 2504.24]  So, I'm wondering if you could talk a little bit about that, how this is both you're enabling AI developers, but also you are definitely integrating this technology as well.
[2504.32 --> 2505.34]  At least that's how it seems.
[2505.34 --> 2510.56]  Yeah, as Aditya mentioned, one of the big appeals of DuckDB is the simplicity.
[2511.38 --> 2514.12]  That's what brings a lot of users to DuckDB.
[2514.70 --> 2526.04]  I think that simplicity can be extended towards usage of AI to a certain extent, like usage of AI in the context of data analytics, data management.
[2526.82 --> 2528.86]  And there are multiple aspects to that.
[2529.16 --> 2532.10]  On one hand, there's user experience side of things.
[2532.10 --> 2536.06]  So, how can we make it easier for people to write SQL?
[2536.70 --> 2541.78]  And I think the answer to that is not our only text to SQL.
[2542.40 --> 2544.74]  And part of that story is fix-it.
[2545.02 --> 2559.96]  So, one of our main aims with fix-it was to keep it, basically make it non-intrusive and not interrupting your flow of writing SQL while still being helpful when it triggers.
[2559.96 --> 2573.10]  And I think Cursor, for example, is an excellent example of integrating AI into IDEs or into the workflow of software developers.
[2573.10 --> 2578.84]  And in our case, we have to think more about data engineers and data analysts.
[2579.66 --> 2582.92]  And I think it's a super exciting time for those kind of things.
[2582.92 --> 2599.34]  I think Mother Duck is a particularly interesting place to work on those kind of things because one of the unique advantages that we have is we have an actual database running on the client side in the browser of the user.
[2599.52 --> 2607.18]  If someone is using our web UI, that user is actually DuckDB running in their browser that can do parsing, binding.
[2607.18 --> 2612.62]  And that gives us so much information about the current state of the query that the user is writing.
[2613.44 --> 2622.00]  And fix-it only, like, scratches the surface of what is possible in terms of SQL writing assistant in that sense.
[2622.92 --> 2624.32]  So, I'm curious.
[2624.42 --> 2633.78]  As we start winding up, you really got me thinking about use cases that I had not thought about before and all the things I might be able to do here.
[2633.78 --> 2636.66]  So, I'm a little bit like a kid in a candy store.
[2636.88 --> 2640.40]  I got to ask you, and I'd like each of you to take a swing at it.
[2641.22 --> 2645.94]  It's pretty cool what you've talked about today in terms of what is possible for us.
[2646.08 --> 2647.82]  How are you thinking about the future?
[2648.02 --> 2651.42]  Like, what are the new cool things that you have in mind?
[2651.42 --> 2661.34]  And, you know, I often say, like, when you're kind of not necessarily working hard on a problem, but you're kind of chilling out at the end of the day, and your mind is just wandering in free form.
[2661.80 --> 2664.26]  And you're thinking, boy, what if we could do this?
[2664.28 --> 2667.70]  I could imagine that, you know, and I can kind of see a path forward to get there.
[2667.70 --> 2679.54]  How are each of you thinking about MotherDuck and DuckDB in terms of what the future might offer if you want to kind of, you know, get out there and wax poetic a little bit?
[2679.74 --> 2684.24]  And it doesn't have to be grounded in current work, but more in imagination and aspiration.
[2684.94 --> 2692.52]  One of the things that I really like about the current state of AI is how good the local models are, the small models that you can run locally.
[2692.52 --> 2696.16]  And there's a great ecosystem out there building on top of that.
[2696.74 --> 2701.16]  One of the things that I see with the local models, of course, they hallucinate.
[2701.66 --> 2708.84]  But to prevent hallucination, you can use a really nice rag mechanism to put context into those local models.
[2709.40 --> 2711.30]  And these local models could be on the edge as well.
[2711.72 --> 2712.74]  It could be on your local laptop.
[2712.86 --> 2714.56]  It could be on the edge.
[2715.30 --> 2720.34]  And knowledge bases are essentially created to kind of prevent these kind of hallucinations.
[2720.34 --> 2726.66]  And one wasteful aspect of creating knowledge bases is that everybody's creating very similar knowledge bases.
[2727.68 --> 2733.50]  And what if there could be a mechanism where we could share these knowledge bases?
[2734.06 --> 2736.80]  A user could create a knowledge base and they could share a knowledge base.
[2736.80 --> 2751.96]  And one of the imaginative worlds that I've driven is how Matadak could be there to do these kind of shareable knowledge bases where you essentially have a world of remote knowledge bases out there in your remote tables.
[2751.96 --> 2766.20]  And then you have a local DuckDB client that helps you pull a knowledge base that you want, use the local knowledge base, argument your local model with the relevant context for your current question.
[2766.72 --> 2769.60]  And then whenever you don't want the knowledge base, you could also drop the knowledge base.
[2769.60 --> 2775.44]  And that's like having a remote knowledge base repository and pull whatever you want.
[2775.80 --> 2783.30]  This is like one of the dreams that I think about how Matadak and DuckDB could be useful for this.
[2783.92 --> 2797.76]  And another aspect of talking about knowledge bases and RAG applications is that not all applications and workflows require a real-time database to build agents on top of them.
[2797.76 --> 2804.08]  And some of these agents could be running as background agents that do some workflow once every day.
[2804.28 --> 2812.40]  And instead of having a real-time database for that, what if you could provide a very lightweight analytical engine that's quite cheap to run locally as well?
[2812.80 --> 2817.04]  And that could also, you know, you could offload some work to the remote cloud.
[2817.30 --> 2823.48]  So this is another thing that keeps me excited at night to think about what could be these kind of use cases.
[2823.84 --> 2827.26]  Which, yeah, these are the two use cases that I am quite excited about.
[2827.76 --> 2831.98]  Yeah, I mean, maybe I can add two things.
[2831.98 --> 2843.50]  One thing that actually connects to that and that is bringing AI and machine learning capabilities more into the database.
[2843.50 --> 2854.78]  So one of the things we've seen in the past is that the inference costs of language models have dropped quite significantly compared to two years ago.
[2855.78 --> 2865.12]  It's now, I think, only it's 2% of the price for inference with GPT4 mini compared to GPT3.
[2865.12 --> 2873.52]  And that actually makes it possible to run language model inference on your tables.
[2874.20 --> 2879.46]  And also to do things like embedding compute on your tables.
[2879.84 --> 2883.60]  And SQL is just a really, really convenient user interface for that.
[2883.60 --> 2888.46]  So we added this embedding function some time ago that works really well together with a vector search.
[2888.78 --> 2893.08]  So you can basically do embedding based search only in SQL.
[2893.48 --> 2896.02]  Now we're adding the prompting capabilities.
[2896.02 --> 2903.18]  So you can do language model based data wrangling in your database and that together with local models.
[2903.76 --> 2907.94]  And this hybrid execution model, we say, okay, we do part of the work locally.
[2908.24 --> 2912.00]  Maybe if you have a GPU, do part of the embedding inference locally.
[2912.36 --> 2917.32]  If you want to do it faster, do it in the cloud with a few A100.
[2917.32 --> 2921.46]  And again, everything is in SQL.
[2921.72 --> 2922.52]  That's awesome.
[2922.74 --> 2930.70]  Yeah, well, thank you both for taking time out of your analytics AI database work to come talk to us.
[2930.78 --> 2932.34]  This has been super amazing.
[2932.96 --> 2937.94]  And I would definitely encourage people out there, please, please, please go try out some things.
[2938.42 --> 2940.16]  Try out some examples with DuckDB.
[2940.44 --> 2945.62]  Check out the Mother Duck website and some of the great blog posts, content that they have there,
[2945.62 --> 2947.76]  or examples, or things that they're doing.
[2948.16 --> 2954.88]  Check it out because it's definitely a really wonderful thing that you can add into your AI stack
[2954.88 --> 2956.66]  and think about and experiment with.
[2956.82 --> 2959.50]  So thank you so much, Till and Aditya, for joining.
[2959.62 --> 2960.16]  It's been a pleasure.
[2960.56 --> 2961.72]  Thank you guys for having us.
[2961.98 --> 2962.46]  Thank you, guys.
[2962.68 --> 2964.30]  It was pretty awesome to be here.
[2971.74 --> 2972.68]  All right.
[2973.04 --> 2975.36]  That is Practical AI for this week.
[2975.62 --> 2977.20]  Subscribe now.
[2977.38 --> 2982.36]  If you haven't already, head to practicalai.fm for all the ways.
[2982.84 --> 2988.78]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2989.34 --> 2993.98]  Sign up today at practicalai.fm slash community.
[2994.58 --> 3000.38]  Thanks again to our partners at fly.io, to our beat-freaking-residents, Breakmaster Cylinder,
[3000.66 --> 3001.52]  and to you for listening.
[3001.88 --> 3003.64]  We appreciate you spending time with us.
[3004.00 --> 3005.18]  That's all for now.
[3005.18 --> 3007.12]  We'll talk to you again next time.
