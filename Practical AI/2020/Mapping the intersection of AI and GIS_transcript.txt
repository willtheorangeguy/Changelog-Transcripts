[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.46 --> 20.04]  This episode is brought to you by DigitalOcean.
[20.38 --> 25.14]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 --> 36.82]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 --> 42.54]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 --> 46.34]  Head to do.co slash Changelog to get started with a $100 credit.
[46.64 --> 48.80]  Again, do.co slash Changelog.
[55.14 --> 66.00]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[66.30 --> 70.40]  This is where conversations around AI, machine learning, and data science happen.
[70.74 --> 75.42]  Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[75.42 --> 76.76]  And follow us on Twitter.
[76.90 --> 78.56]  We're at Practical AI FM.
[78.86 --> 80.24]  Okay, here's Daniel and Chris.
[80.24 --> 87.80]  Welcome to another episode of the Practical AI Podcast.
[88.46 --> 89.52]  My name is Chris Benson.
[89.68 --> 92.04]  I'm a principal AI strategist at Lockheed Martin.
[92.30 --> 96.72]  And with me, as always, is Daniel Whitenack, a data scientist with SIL International.
[97.12 --> 97.74]  How's it going, Daniel?
[98.12 --> 99.48]  It's going great.
[99.72 --> 107.20]  Got a few more guests in the house these days because my brother-in-laws are back from college due to college being canceled.
[107.20 --> 107.64]  Yeah.
[107.64 --> 109.56]  Or at least virtual for now.
[109.74 --> 111.56]  So, it's a fun household right now.
[111.70 --> 116.26]  And yeah, that makes working from home, I get a little bit more interaction with humans.
[116.76 --> 117.16]  Yep.
[117.26 --> 119.42]  Coronavirus is making life interesting.
[119.64 --> 120.78]  We have my daughter home.
[120.86 --> 122.94]  Our school system is closed indefinitely.
[123.24 --> 127.24]  So, yep, we're doing homeschooling and working and no travel.
[127.38 --> 129.70]  So, like I said, life is interesting right now.
[129.80 --> 131.90]  Hopefully, not in too bad a way.
[132.04 --> 133.18]  We're in early days.
[133.18 --> 136.10]  Hopefully, things will not get terrible.
[136.36 --> 137.82]  I'm crossing my fingers to see.
[138.44 --> 138.82]  Yeah, yeah.
[138.96 --> 145.94]  And regardless, people across the world really are, I'm guessing, looking at maps a lot.
[146.54 --> 147.26]  I bet they are.
[147.26 --> 152.64]  And geography and all sorts of related things, which is very relevant to our conversation today.
[152.80 --> 153.96]  Who do we have on the show today, Chris?
[153.96 --> 168.22]  We have today two guys from ESRI, which is the Environmental Systems Research Institute, whose names are Daniel Wilson, who is the AI lead for professional services, and Rob Fletcher, senior data scientist at ESRI.
[168.42 --> 169.64]  And welcome to the show, gentlemen.
[170.66 --> 171.02]  Thank you.
[171.48 --> 171.84]  Thanks.
[171.84 --> 188.54]  So, I guess, as we get started here, if maybe first Daniel and then Rob, if you could each give us kind of an introduction to yourself, kind of what you do and kind of how you got to this point in your career before we kind of dive into learning a little bit more about ESRI.
[188.98 --> 189.26]  Sure.
[189.66 --> 194.72]  So, I have basically spent my entire career doing data science, but I didn't start that way.
[195.42 --> 199.30]  I went to school originally for engineering physics and applied mathematics.
[199.84 --> 201.22]  Thought that's where I wanted to go.
[201.22 --> 204.10]  I went to school for engineering physics.
[204.50 --> 208.62]  I think there's a first engineering physics other than me that's been on the podcast.
[209.02 --> 210.08]  So, that's great.
[210.72 --> 211.16]  Cool.
[211.30 --> 212.34]  Colorado School of Mines.
[212.74 --> 213.26]  No way.
[213.54 --> 213.94]  Me too.
[214.42 --> 214.60]  Yeah.
[215.70 --> 216.46]  Oh, wow.
[217.14 --> 219.26]  Yeah, this is so weird right now.
[219.42 --> 220.08]  There's a coincidence.
[220.40 --> 220.88]  That's funny.
[221.08 --> 221.32]  Yeah.
[221.74 --> 225.06]  Y'all are probably in the same class at the same time and just don't know it yet there.
[225.10 --> 226.14]  That's very possible.
[227.14 --> 229.98]  Yeah, I graduated in 2004.
[229.98 --> 233.84]  Yeah, I'll have to talk to you afterwards to catch up on that.
[234.22 --> 234.82]  Yeah, sounds good.
[234.88 --> 235.98]  I'm sure there was a lot of overlap.
[237.38 --> 237.82]  Yeah.
[237.94 --> 241.78]  So, really, I got started there because I was interested in math and physics.
[241.78 --> 246.24]  And I kind of just wanted to get into studying the universe.
[246.68 --> 250.14]  Found it really interesting, especially on the applied mathematics side.
[250.40 --> 251.96]  Really wanted to get into theoretical physics.
[252.42 --> 257.04]  So, that's kind of the path that I started down was studying things like general relativity.
[257.48 --> 259.90]  And I was really fascinated with string theory at the time.
[259.90 --> 263.50]  And then life happened as, you know, life tends to.
[263.86 --> 267.94]  And I ended up getting a job at a software company, mostly in the federal government space.
[268.28 --> 272.98]  Started there and I basically told my manager, hey, I want to do some math.
[273.12 --> 275.86]  I don't really know what math means in this context, but I love math.
[276.04 --> 277.08]  And I want to figure out how to do it.
[277.08 --> 283.22]  So, I kind of got put on a data science team, got a trial run working with the team.
[283.60 --> 285.58]  It wasn't really called data science at the time.
[285.68 --> 287.72]  It was back in 2009.
[288.46 --> 293.58]  Data science wasn't really commonly said, at least most of the circles that I was in.
[293.98 --> 295.22]  But that's kind of what we were doing.
[295.34 --> 301.60]  We were working with a lot of different sensor data types and spatial data, primarily spatial data.
[301.60 --> 308.24]  And really what we did was apply machine learning, statistics, or other algorithms to geospatial data.
[308.74 --> 310.46]  So, my career kind of grew out of that.
[310.70 --> 311.88]  I'm pretty much self-taught.
[312.06 --> 318.72]  Most of my machine learning that I learned initially was from Christopher Bishop's Pattern Refundition Machine Learning book.
[319.22 --> 320.90]  And then I had some really great mentors there.
[321.48 --> 322.76]  So, that's kind of where I learned it.
[322.84 --> 329.84]  But I got hungrier and hungrier for more machine learning, artificial intelligence, statistics, any field of applied mathematics, really.
[329.84 --> 332.66]  And just kept learning more and more and more.
[333.06 --> 338.54]  And as things started to grow in the industry as well, I tried to keep pace and follow it.
[338.76 --> 340.40]  I've been with Esri for about two years.
[340.80 --> 348.22]  And since then, things have been really exciting, especially in the geospatial realm, which is where we're seeing a lot of changes happening right now.
[348.84 --> 349.30]  Very cool.
[349.52 --> 350.20]  Rob, how about you?
[350.76 --> 350.98]  Yeah.
[351.06 --> 354.04]  So, I started off very similar to Daniel, actually.
[354.04 --> 360.12]  I was very interested in engineering to begin with, but I ended up switching over to when I did my bachelor's degree.
[360.38 --> 362.22]  I studied physics and mathematics.
[362.84 --> 365.72]  I was really obsessed with this stuff at the time.
[365.90 --> 368.12]  And so, I decided to go straight through to grad school.
[368.24 --> 372.74]  And so, I ended up going to the University of Pennsylvania to do my PhD in particle physics.
[373.56 --> 379.66]  And while I was there, the main experiment I worked on was Large Hadron Collider, Geneva, Switzerland, on the Atlas experiment.
[379.66 --> 383.16]  So, I did quite a bit of work there, kind of all over the place.
[383.30 --> 384.92]  I did a lot of coding.
[385.28 --> 391.06]  You know, we don't really hire software engineers in physics experiments because they're expensive and grad students are very cheap.
[391.38 --> 394.96]  So, we kind of had to do everything and just get our hands in everywhere.
[395.94 --> 402.62]  And so, to start off with, I was doing a lot of software, kind of writing a lot of packages that sort of helped do analysis, things like that.
[402.62 --> 408.48]  As I got further into my PhD, I started working on more actual analysis-type topics.
[409.08 --> 415.04]  One of the first kind of major projects I worked on was doing an electron identification-type task.
[415.36 --> 422.76]  So, we get all these signals in the detector, and we needed to make a decision whether they were an electron or, you know, something else.
[422.76 --> 424.04]  That was the originating particle.
[424.50 --> 429.48]  I guess I didn't realize it at the time, but this was, you know, a pretty traditional kind of classification problem in machine learning.
[429.48 --> 435.88]  So, I was, you know, doing data science, you know, even quite a while ago and just didn't really understand that that's what I was doing.
[435.98 --> 437.38]  I was just sort of solving problems.
[438.50 --> 448.36]  Later on in my PhD, I went on to work on some physics that has to do with extending the Higgs boson model, something called the 2-Higgs doublet model.
[448.74 --> 456.42]  So, we were specifically looking for these kind of additional Higgs bosons that might be lurking somewhere in physics and then produce two photons.
[456.42 --> 466.20]  So, I wrote a lot of code, did a lot of analysis in that specific area right there, and then I think really kind of tipped me over the edge and got me thinking about data science.
[466.68 --> 480.36]  I noticed that as we were doing these things, you know, this detector was collecting just so much data all the time that a lot of these older kind of statistical methods that were used to assess uncertainties and really kind of backbones a lot of these analyses,
[480.36 --> 484.60]  these things were just kind of crumbling under the weight of all of this data that we had.
[484.68 --> 486.90]  It was just so much data that these things were falling apart.
[487.64 --> 492.80]  And so, I really kind of started thinking out of the box and trying to see, well, like, there's got to be something better.
[492.92 --> 499.74]  I mean, a lot of these methods were, you know, old methods that were developed in, you know, the 60s and 70s that some of the original particle physics experiments.
[499.74 --> 505.48]  And so, I really wanted to start looking around and seeing what other kind of advances had been made.
[505.58 --> 511.50]  And that sort of got me into some of the machine learning data science stuff that I started finding.
[511.72 --> 520.40]  And I ended up for a portion of my thesis using Gaussian process regression to estimate backgrounds in this model that I was working on.
[520.94 --> 524.66]  And, you know, again, it was sort of, you know, just the kind of tip of the iceberg for me.
[524.66 --> 528.10]  I didn't really completely understand that I was doing data science at the time.
[528.18 --> 533.06]  It was just sort of, hey, here's some new fancy technique, which is actually not even all that new.
[533.16 --> 536.20]  But I can start using to make a real difference in these analyses.
[537.38 --> 540.64]  And so, from there, I decided I really wanted to get out of academia.
[541.04 --> 543.52]  I just kind of didn't really want to pursue that.
[543.72 --> 547.70]  I wanted to go into industry and was trying to decide what to do.
[547.82 --> 551.40]  I started applying for data science jobs because it was kind of the hot thing at the time.
[551.40 --> 555.58]  And got a couple of offers and just really wasn't crazy about any of them.
[555.68 --> 557.32]  None of the jobs really sounded that interesting.
[557.62 --> 565.28]  It was, you know, a lot of them were kind of, you know, how many more clicks can you get on a button that generates ad revenue?
[565.46 --> 566.24]  You know, things like that.
[566.30 --> 569.28]  I just didn't really, it wasn't interesting to me at all.
[569.66 --> 573.30]  And then I actually came across Esri because my wife has worked for Esri for quite a while.
[573.36 --> 577.42]  And she let me know that, hey, we're actually looking for a data scientist.
[577.58 --> 578.44]  Maybe you should apply.
[578.44 --> 583.20]  So, you know, it's something that never crossed my mind, but that's why I applied for that.
[583.34 --> 584.54]  And I was one of the first ones.
[584.62 --> 587.16]  I was actually the second data scientist hired at Esri next to Daniel.
[587.72 --> 592.92]  And so, very new team and really kind of had this very uncertain sort of direction that it was going.
[593.08 --> 593.98]  And that really excited me.
[594.12 --> 598.76]  I thought it was really interesting that there was this whole new realm of topics that this company,
[599.24 --> 603.68]  and to some extent, entire space of GIS just really hadn't tackled yet.
[603.86 --> 606.42]  That just sounded like a ton of fun to me and I couldn't pass that up.
[606.42 --> 608.70]  So, I ended up accepting that job.
[608.80 --> 612.52]  And so, I've been at Esri now for almost two years, a little less than two years now.
[613.22 --> 614.26]  Super interesting backgrounds.
[614.50 --> 620.58]  And I'm excited because I didn't know we'd be talking about particle physics or I'd be talking to an ore digger today.
[620.94 --> 623.56]  But excited about those things.
[623.94 --> 625.88]  But let's turn a little bit to Esri.
[626.18 --> 629.62]  For those that aren't familiar, what does Esri do?
[629.90 --> 632.10]  What businesses are they involved with?
[632.16 --> 635.50]  And what are their primary products or services?
[635.50 --> 637.42]  I guess I'll take that one.
[637.76 --> 642.16]  So, Esri is a GIS software company.
[642.80 --> 645.38]  GIS is Geographic Information Systems.
[645.96 --> 653.02]  So, basically, Esri deals with all aspects of geospatial data from collection, storage, to analysis.
[653.02 --> 667.40]  A large amount of our users are in the state and local government, federal government spaces, where they use our software as a system of record for city management, land data, road networks, parcels.
[667.84 --> 668.58]  Really, you name it.
[668.62 --> 673.32]  If it's a place on the earth, it's probably in a geospatial database.
[673.70 --> 676.98]  And Esri maintains a lot of different geospatial databases.
[676.98 --> 681.42]  So, with that data, are you providing some of that data?
[681.80 --> 686.56]  Or are you serving mostly as a system to manage that sort of data?
[686.64 --> 687.42]  Or a little bit of both?
[687.88 --> 688.78]  A little bit of both.
[688.94 --> 691.64]  So, we actually have what's called the Living Atlas.
[691.64 --> 700.84]  And it's basically a collection of geospatial data, authoritative geospatial data, that ArcGIS subscribers can use or Esri subscribers.
[701.16 --> 707.22]  I kind of glossed over this, but ArcGIS is really the name for our primary software platform.
[708.34 --> 711.06]  And could you tell us a little bit about what ArcGIS is?
[711.60 --> 712.48]  And how is that?
[712.54 --> 716.66]  I guess that's a particular implementation or product, if you will, of GIS.
[716.90 --> 717.42]  Is that fair?
[717.42 --> 725.40]  Yeah, well, so GIS, kind of geographic information systems, the software behind it, started several decades ago.
[725.74 --> 730.96]  And I think it's fair to say Esri really started that side of things.
[731.18 --> 740.90]  ArcGIS specifically has evolved into a collection of desktop and server products for geospatial analysis and data manipulation.
[740.90 --> 752.70]  Some of that's for production mapping, where people take imagery or other content or even paper maps and turn that into products that people can use.
[753.36 --> 760.72]  So, just as a side note here, I actually got exposed to ArcGIS a little bit more recently.
[760.90 --> 766.32]  So, SIL, some of our listeners will know that we do language-related work around the world.
[766.32 --> 774.52]  And one of the things we do is we have a mapping team that does language survey work, and they produce maps of, you know, what languages are used where.
[774.64 --> 783.78]  And so, there's all these sorts of polygons around the world where certain languages are used and populations exist and all of those sorts of things.
[783.78 --> 789.18]  And so, just to give an example, that was one example that I was exposed to recently.
[789.30 --> 792.06]  So, I'm assuming that, I know they're using ArcGIS for this.
[792.12 --> 802.56]  So, I'm assuming that ArcGIS is kind of managing those polygons and allowing them to do analysis over them, combine them, and that sort of thing.
[802.60 --> 803.24]  Would that be accurate?
[803.24 --> 803.96]  Yep.
[804.08 --> 818.46]  Basically, all functions of that from geographic coordinate systems to computational geometry to normal database, relational database utilities, kind of larger scale spatial databases as well.
[818.96 --> 819.20]  Yeah.
[819.28 --> 830.26]  Just looking through your website here while we're talking, it talks about spatial analysis and remote sensing and real-time visualization and analytics, both in 2D and 3D.
[830.26 --> 835.94]  Are all these applications centered around ArcGIS or other product?
[836.06 --> 836.92]  Rob, would you take that one?
[837.12 --> 837.32]  Yeah.
[837.50 --> 839.72]  So, most of them are centered around ArcGIS.
[840.16 --> 844.60]  We do have a lot of kind of extensions and other products that kind of add on to all of these things.
[844.66 --> 853.48]  Like you said, there's the desktop products, which are the ArcGIS ones, and then we also have some server products, you know, things that are cloud-based to do kind of like large data consumption or analysis.
[854.00 --> 859.76]  And there's also a bunch of other extensions we have that can do things, like even producing the data, like, for instance, Grown to Map.
[859.76 --> 870.46]  So, these are things that, you know, you can take drone footage, and as long as you have the correct metadata, it can do all the sort of math under the hood to actually, you know, put those, the imagery taken by drone onto a map.
[870.52 --> 873.94]  So, you can get, you know, produce your own kind of imagery products and things like that.
[874.92 --> 875.28]  Interesting.
[875.28 --> 884.42]  And you mentioned that, I forget who mentioned that, that one of the sort of big clients of Esri are local and national governments.
[884.56 --> 890.64]  I guess, who's primarily, like, using ArcGIS for, like, the main use cases?
[890.76 --> 892.70]  What are the main use cases, I guess I should say?
[892.84 --> 898.64]  Why is it important to have this sort of specialized ability to deal with spatial data?
[898.64 --> 905.22]  So, a lot of the state and local government usage we see, some of it on, like, the county level where they might track, say, like, parcels of land.
[905.48 --> 912.78]  This allows them to keep a really good system of record and inventory of where all these parcels are, any historical information about them.
[912.84 --> 916.16]  So, all of these different geometries that you see in there are actually enriched with data.
[916.16 --> 923.04]  So, you can kind of think of it as, you know, being like a relational database, but a relational database that has spatial properties to it.
[923.10 --> 925.76]  And so, it's not just, you know, a row and a table.
[926.14 --> 931.14]  It's, you know, a polygon that sits on a map that also has all that relational information associated with it.
[931.58 --> 939.40]  And so, doing this allows state and local governments to, you know, keep track of, like I said, things like parcel data, tax information.
[939.40 --> 943.88]  We get a lot of utilities where they can look at where, you know, water lines are.
[943.98 --> 951.62]  They can use this to actually do analysis to try to find out, you know, what kind of precautions need to be taken if, let's say, somebody needs to go in and dig something.
[952.22 --> 954.80]  They can basically give an area where we say, we need to dig right here.
[955.02 --> 961.56]  And based on this whole system of record with all this geometry, you can come up with things like, oh, are there any gas lines or water lines or power lines?
[961.60 --> 963.02]  Or is there anything nearby?
[963.46 --> 966.44]  Are you in some zone that needs to be low noise?
[966.44 --> 970.18]  Is all of this analysis can be kind of done inside of the platform.
[970.32 --> 979.48]  And so, the state and local governments use this to do a lot of planning, to keep track of all of their things, but also to do analysis and kind of forward-looking as well.
[979.64 --> 986.62]  Like, for example, if you wanted to, you know, do some, like a site selection type problem, you know, we need to put something new somewhere.
[987.04 --> 987.82]  Where do we put it?
[987.90 --> 989.02]  Where's the best place to put it?
[989.02 --> 999.98]  Where are we going to not infringe on, you know, other people's property or, you know, keep it near where, you know, some other utility that it needs to have access to, things like that.
[1000.62 --> 1002.58]  So, quick question, just as a quick follow-up.
[1002.66 --> 1005.38]  You mentioned the word polygon in reference to this.
[1005.46 --> 1008.90]  And I was wondering if you could take a second and just tell us what that is in this context.
[1008.90 --> 1015.60]  Sure. A polygon in this context is really just a series of points that exist on, you know, in some map space.
[1015.76 --> 1016.88]  They're X-Watt coordinates.
[1017.54 --> 1023.72]  And in general, what makes it a polygon in our realm is that the first point is equal to the last point.
[1023.90 --> 1026.34]  And that means that it's just, you know, it's a closed thing.
[1026.48 --> 1033.18]  And so, you have some defined shape that's just a series of X-Watt coordinates on a map, basically.
[1033.18 --> 1047.70]  Hi there.
[1048.06 --> 1051.18]  This is Daniel Whitenack, one of the co-hosts of Practical AI.
[1051.56 --> 1058.36]  And when I'm not working on Practical AI, I'm developing my own AI applications or I'm training teams at other companies.
[1058.52 --> 1062.90]  I've been doing this for over 10 years now and I've trained more than a thousand people.
[1063.18 --> 1069.26]  Now I'd like to invite you to my new live online training event called AI Classroom.
[1069.78 --> 1076.92]  In AI Classroom, I'm going to teach the practical skills I've learned over the years using the latest open source AI technology.
[1077.02 --> 1084.34]  You will learn both AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[1085.04 --> 1091.68]  After attending AI Classroom, you'll be able to understand the latest models, implement your own models and code,
[1091.68 --> 1099.98]  train computer vision and NLP models, create model inference servers, and experiment with state-of-the-art methods like reinforcement learning.
[1100.66 --> 1103.04]  AI Classroom is taking place this May.
[1103.50 --> 1109.92]  It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[1109.92 --> 1116.44]  There will be two cohorts with convenient time zones for Eastern and Western hemispheres, so don't miss out.
[1116.94 --> 1120.80]  Tickets and more information is available at datadan.io.
[1121.22 --> 1123.16]  That's datadan.io.
[1123.70 --> 1126.40]  And early bird pricing lasts until April 3rd.
[1126.58 --> 1128.56]  See you online in AI Classroom.
[1128.56 --> 1144.02]  So, Daniel, I've got a question for you.
[1144.02 --> 1149.42]  We've been kind of getting this crash course in these last few minutes about GIS and specifically ArcGIS
[1149.42 --> 1154.24]  and kind of some of the use cases and applications in a general sense.
[1154.24 --> 1160.32]  I'd like to start pulling artificial intelligence, machine learning ideas into it and kind of understand
[1160.32 --> 1168.48]  how is Esri using AI and ML in the context of GIS and specifically ArcGIS and your other products and services.
[1169.02 --> 1169.98]  Yeah, sounds good.
[1170.06 --> 1171.56]  So, that's a really big question.
[1171.88 --> 1175.12]  And there's definitely a lot of sides of that that I'd like to address.
[1175.38 --> 1176.14]  Sure, absolutely.
[1176.14 --> 1187.12]  I'd like to first start with what I think most people tend to think of when they think about applying artificial intelligence to spatial data or geospatial data, geographic data.
[1187.76 --> 1193.46]  And that's things like aerial drone and satellite imagery and extracting features from that.
[1193.72 --> 1199.56]  So, that could be something as simple as, you know, we have a satellite image of an area and we want to extract all the buildings in there.
[1200.08 --> 1202.32]  And historically, that's been a manual process.
[1202.32 --> 1213.52]  You know, a human has gone through satellite imagery and they've drawn boxes around the building footprints of a house or drawn borders around things or drawn lines where there are roads or anything like that.
[1214.04 --> 1223.12]  And we're finding that we can automate a lot of that using mostly modern day deep learning techniques, convolutional neural networks and the like.
[1223.98 --> 1228.96]  And that's where a large amount of our use case and a lot of our focus on our AI strategy has revolved around.
[1228.96 --> 1233.06]  But I also want to say that that's just a piece of everything.
[1233.38 --> 1242.54]  Really, what we're trying to do is find these areas where geospatial information in geographic context adds value to an analysis problem.
[1243.24 --> 1246.04]  There are countless areas where we found applications of AI.
[1246.58 --> 1248.22]  Love to talk about some of those, definitely.
[1248.74 --> 1248.86]  Yeah.
[1249.00 --> 1255.80]  So, before we get into the specific applications, I guess I just have a sort of general question about AI and spatial data.
[1255.80 --> 1263.46]  So, you talked about like polygons and relational information to geographic entities.
[1263.78 --> 1279.72]  When we're thinking about like AI models that use geospatial data, are there specific like types of models or types of encoders that work with this sort of data out of the box?
[1279.72 --> 1295.14]  Or most of the time, are you kind of thinking of using like pulling features out of, let's say, ArcGIS that are related to geography and using those as kind of more, I guess, quote unquote, standard features in an AI model?
[1295.76 --> 1297.38]  So, I think the answer is all of the above.
[1298.12 --> 1304.88]  I think the most common applications that we're seeing are things like using geospatial information.
[1304.88 --> 1313.72]  So, when we say data in a relational database that has a geometry like a polygon, more generally we're talking about an arbitrary shape for an object.
[1313.86 --> 1320.86]  So, that could be a polygon, could be a series of points in a line that we call a polyline, a point, or things like that.
[1321.18 --> 1328.48]  Sometimes you can extract features purely off of that geometry and then tie that back to the attributes that are in the attribute table.
[1328.48 --> 1338.24]  So, an example is if we're trying to make predictions about something on, say, a road network, an application that I've put a lot of work into is car accident prediction.
[1338.82 --> 1350.12]  There's a lot of features that you can apply to a point on the road that could be extracted from both its geographic context, the attributes of the road itself, or the geometry, such as like how curvy that is.
[1350.12 --> 1353.88]  And when we apply this in machine learning models, there's a lot of different applications.
[1354.28 --> 1361.76]  So, this could be a normal kind of standard out-of-the-box machine learning algorithm, something like a random forest or support vector machine.
[1362.12 --> 1368.20]  It could be a graph neural network if you're talking about something on a road graph.
[1368.74 --> 1372.92]  But really, it's not limited to any one set of models or one type of data.
[1373.08 --> 1374.72]  There's a lot of different applications.
[1374.72 --> 1386.16]  Yeah, and I'd also like to just say that one of the things that really attracted me to this problem set in general is that using geospatial information in especially deep learning models, it's not always clear how to do that.
[1386.26 --> 1391.04]  You mentioned kind of extracting these into kind of the standard sort of inputs that you would normally get.
[1391.42 --> 1393.40]  And that's definitely something that we do sometimes.
[1393.74 --> 1400.78]  But I think also we try to put a lot of thought into, well, how can we use the objects themselves as input?
[1400.78 --> 1423.30]  And this is just, I think, in general, a very difficult question because you take something like a polygon, for example, try putting a polygon into a neural network, and it can be hard because if you have some arbitrary number of points that make up vertices of the polygon, it's really difficult to fit that into something that's like a confined or a predefined neural network that has a certain number of inputs.
[1423.30 --> 1428.74]  So I think in general, it's actually a pretty difficult problem to kind of tackle in the general sense.
[1428.98 --> 1431.28]  And that's one of the things I think is really exciting about this field.
[1432.00 --> 1436.30]  And so on that point, and I know Daniel mentioned graph neural networks.
[1436.30 --> 1440.66]  So are you actively exploring these kind of unique ways?
[1440.76 --> 1448.26]  Because I know this is something that you face with like text, for example, too, which could be, you know, you could have three words or you could have 17 words.
[1448.58 --> 1457.20]  But most of the time you sort of encode this information into a fixed size vector somewhere in your model.
[1457.68 --> 1459.96]  Is it a similar strategy that you're pursuing?
[1459.96 --> 1465.84]  Or maybe what are some of the methodologies that might be worth noting that people are exploring in this area?
[1466.78 --> 1475.74]  One area that I found really interesting and been following very closely over the last couple of years, and it's very similar to the NLP side of the world, is attention.
[1476.42 --> 1485.96]  So attention normally has been used within a natural language processing context to look at the relationship between words in a sentence or characters in a word.
[1486.20 --> 1489.68]  As you go, can you define attention also for anyone out there that doesn't know it?
[1489.92 --> 1490.48]  Sure.
[1490.48 --> 1497.94]  So that's basically training a neural network, what parts of an input are relevant to its computation.
[1498.90 --> 1507.54]  So it's a learned way of kind of approximating, you know, if you look at a scene, you're not looking at every last part of a scene.
[1507.66 --> 1512.56]  What you're doing is you're parsing it into the most important parts first and paying the most attention to those.
[1512.56 --> 1516.12]  So in the context of a neural network, attentions are similar to that.
[1516.80 --> 1519.04]  And mathematically, it's a pretty simple operation.
[1519.46 --> 1526.68]  But applying attention outside of a natural language processing context, we've been trying it across spatial entities.
[1527.14 --> 1530.16]  So let's say you have a bunch of points on the ground.
[1530.28 --> 1535.76]  We've actually been working on a project to apply reinforcement learning to police patrol optimization.
[1535.76 --> 1552.58]  And within that particular application, the units that we're applying attention over are things like locations of crime or police patrols or, you know, basically spatial entities that have an XY coordinate and then maybe other attributes.
[1552.58 --> 1560.50]  In this case, what we're doing is we're looking at where we're applying attention to that is how do all of those relate to each other and using that as the input to the model.
[1560.88 --> 1566.44]  So it's not about bringing in new features, but how the features are handled within the model.
[1566.94 --> 1567.44]  That's interesting.
[1567.66 --> 1576.56]  It makes me wonder about like with that application, it seems like there's these really interesting intersections with geospatial data and time as well.
[1576.56 --> 1588.08]  Because I'm assuming when you're optimizing those sorts of police patrols, obviously crime in certain areas is going to be very time dependent as well, or possibly even weather dependent.
[1588.08 --> 1595.12]  So it seems like there could be multiple layers of geospatial data that's also changing per time.
[1595.22 --> 1597.54]  It seems like quite a rich data set.
[1598.16 --> 1598.76]  Yeah, absolutely.
[1599.14 --> 1605.66]  And we're finding that a lot of the times that we're applying machine learning to geospatial problems.
[1605.66 --> 1607.52]  It's not just one data set.
[1607.52 --> 1612.10]  So a lot of machine learning models are built on top of relational data.
[1612.30 --> 1617.40]  So bringing multiple tables together and then creating one big set of input features in running the model.
[1618.12 --> 1622.10]  And that's still kind of true for geographic information.
[1622.26 --> 1630.56]  But it's about bringing together a lot more disparate sources of information together into a model that I think makes it an especially unique challenge.
[1630.56 --> 1643.56]  Yeah, and I think that understanding the time characteristics and some of the problems, especially with something like crime prediction and modeling how crime is distributed, not only over space, but over time, is pretty difficult.
[1643.66 --> 1645.78]  And that's something that we've spent a lot of time on.
[1646.12 --> 1647.70]  But also, you mentioned weather in there.
[1647.94 --> 1651.22]  And that's something that obviously comes up all the time.
[1651.34 --> 1660.10]  Weather is a big factor whenever you're talking about, especially larger areas, where even weather can be different across an entire area where you're trying to make predictions.
[1660.10 --> 1673.90]  So sourcing very good weather data has been a big task of ours that we're always on the lookout for better weather data, more predictions in shorter quantities of time and things like that.
[1673.90 --> 1686.22]  So one of the things that I was noticing as I was looking through Ezra's material here that really caught my eye and Daniel's eye as well actually related to some stuff that we had already talked about in past episodes.
[1686.22 --> 1695.04]  So you have done some work with the DODs, the U.S. Department of Defense's Joint AI Center, which shorthand is called the JAIC.
[1695.24 --> 1705.46]  And before I lead into the question, I'll note to listeners that we actually had an episode with Greg Allen, Chief of Strategy and Communications at the JAIC, which was episode 72.
[1705.46 --> 1708.02]  It was entitled How the U.S. Military Thinks About AI.
[1708.02 --> 1713.64]  So if you and anybody that's interested in that can dive into the JAIC's perspective on that episode.
[1713.74 --> 1722.66]  But going into that, at Lockheed Martin, we apparently have done some similar work to you guys in terms of the context of humanitarian assistance and disaster relief.
[1722.66 --> 1727.24]  And you had a YouTube video talking about some of the work that Ezra's done with the JAIC.
[1727.24 --> 1731.02]  And I was wondering if you would just kind of tell us about that as a use case.
[1731.34 --> 1735.86]  And then you have a bunch of other interesting use cases that you note online as well.
[1735.98 --> 1738.06]  And later on, I wanted to ask you about those as well.
[1738.12 --> 1741.04]  But if you would tell us about what you're doing with the JAIC, that would be fascinating.
[1741.86 --> 1742.34]  Yeah, sure.
[1742.48 --> 1749.08]  So we are specifically involved with a portion of the JAIC that we call HATR, which is the Humanitarian Aid and Disaster Response.
[1749.08 --> 1757.22]  The main focus of this particular mission is this rapid response to any kind of natural disaster.
[1757.50 --> 1764.38]  The kind of rapid response we're talking about is, you know, picture kind of zero to two weeks after something like a hurricane.
[1764.88 --> 1768.86]  So this is when, you know, allocation of resources are very, very important.
[1769.44 --> 1772.52]  And it can be very difficult to gather information at the same time.
[1772.52 --> 1780.68]  And so one of the big things that we are supporting with the JAIC is using satellite imagery and any other data that we can access to,
[1781.02 --> 1790.82]  how can we enable them to make better, smarter decisions in a shorter frame of time so that they can help the most people possible that are affected by these types of disasters?
[1791.40 --> 1796.34]  So I appreciate you leading us into this topic of humanitarian assistance, disaster relief.
[1796.34 --> 1804.30]  So you talked about kind of gathering whatever imagery and data might be relevant to responding quickly in the case of a disaster.
[1804.42 --> 1811.44]  Could you give us kind of a scenario of how that might play out and how the system might help in terms of what you're trying to achieve?
[1812.34 --> 1812.98]  Yeah, definitely.
[1813.54 --> 1820.90]  So how we kind of envision this being used is immediately after a disaster, as soon as this imagery becomes available,
[1821.28 --> 1824.40]  which, you know, kind of varies depending upon what kind of imagery it is.
[1824.40 --> 1826.28]  But there's lots of satellite imagery you can get.
[1826.36 --> 1831.50]  And also NOAA captures aircraft-borne imagery pretty soon after these events happen.
[1832.16 --> 1838.56]  And so one of the main use cases that we're working on has to do with road detection and specifically road debris detection as well.
[1838.94 --> 1848.54]  So what we kind of want to do in the end is we want to be able to give them a system that allows them to understand how the state of the road network where in the affected area.
[1848.54 --> 1861.72]  So let's say, you know, you could find because of blockages in the road, you could find that there are some community that is completely cut off from any sort of aid because all of the roads are completely blocked in there.
[1861.96 --> 1873.02]  So this gets you this idea that we call a service area where we can say, yeah, we know that this place is blocked off and we need to maybe, you know, contract special vehicles come in and actually deliver resources to them.
[1873.02 --> 1884.78]  It can also help with things like routing. So if an agency like the Jake comes in and they have some sort of base set up and they need to be able to distribute resources or send out emergency crews, they need to know where they can get to as well.
[1884.94 --> 1896.20]  So this kind of real-time routing is something else that we're looking at where we can say, you know, I need to get from our base of operations or whatever point we have here out to some other point.
[1896.42 --> 1902.16]  How do I get there so that I'm not going to get blocked by trees or by flooding or, you know, things like that.
[1902.16 --> 1913.74]  So we really want to be able to give them the information that they need to be able to move around in this area without being hindered by, you know, running into a dead end and turning around and trying to find another way around.
[1914.08 --> 1924.04]  So I'm curious on that front, one of the things I'm thinking about as I'm thinking about these use cases is like the work that's going to have to go into the data set behind this.
[1924.04 --> 1936.74]  And I'm guessing like, you know, if let's say the satellite imagery exists of previous disasters and you kind of have that data set, it seems like there's like, I guess, two major challenges from my side.
[1936.84 --> 1941.08]  I guess one is the data labeling bit and the overhead with that.
[1941.08 --> 1946.58]  And then second is the sort of variability you could get with disasters, right?
[1946.66 --> 1959.58]  So like, let's say a tornado or something in one part of the country is going to look very like the ground cover is going to look very different from a tornado in a in a separate part of the country.
[1959.58 --> 1964.20]  So are you thinking about those problems at all in terms of have you been able to deal with those?
[1964.28 --> 1971.84]  Is it a matter of brute force and data labeling or their tricks to kind of dealing with this robustness issue?
[1972.66 --> 1982.88]  So on the data labeling side, we've actually partnered up with a company called Figure Eight that does large scale image annotation for deep learning models.
[1983.08 --> 1985.02]  And they've been doing it for a very long time.
[1986.12 --> 1988.66]  There are those challenges that you mentioned, though.
[1988.66 --> 1994.98]  There's a large amount of disaster imagery collected by Digital Globe and NOAA that's publicly available.
[1995.30 --> 2001.18]  So Digital Globe has an open data program that you can get disaster imagery going back.
[2001.54 --> 2003.74]  I don't remember how many, but several years.
[2003.88 --> 2010.90]  So we have quite a few earthquakes and tornadoes and hurricanes from disparate areas.
[2010.90 --> 2021.38]  And then kind of bringing all that data together, we can label that at scale so that we have a large data set to build our model upon.
[2021.54 --> 2022.50]  That's a good start.
[2022.66 --> 2028.90]  But we also have a large collection of high resolution pre-disaster imagery.
[2029.44 --> 2033.50]  Some of that is from Digital Globe, from their pre-disaster imagery in the open data catalog.
[2033.50 --> 2040.56]  And some of that is internal imagery that we have at Esri from a variety of sources that we can use for this.
[2041.08 --> 2042.00]  Sarah, was that a question?
[2042.14 --> 2043.06]  No, that was great.
[2043.18 --> 2045.70]  I was just going to actually add a little bit to that.
[2046.26 --> 2048.36]  It's a pretty amazing time.
[2048.48 --> 2051.82]  I love the work that you guys are describing that you've done there.
[2051.82 --> 2055.38]  I know at my employer, we've done some similar stuff.
[2055.62 --> 2062.02]  We're basically creating data sets that are multi-sensor, multi-platform, and spatiotemporally synchronized and stuff.
[2062.28 --> 2063.30]  So similar stuff.
[2063.50 --> 2072.18]  But it's really, I just wanted to comment that it's really an amazing time, I think, that we're going to come into for the HATER use case, for the humanitarian disaster relief use case.
[2072.18 --> 2081.74]  Because, you know, we're going to be able to finally apply AI technologies and data science in general to make a really meaningful impact through the DOD.
[2081.74 --> 2092.26]  And I love the way the DOD, through the JAIC, has really engaged a lot of different organizations, each contributing what they can, just as Esri is, into this.
[2092.62 --> 2095.90]  You know, it's a pretty inspirational thing that we're all trying to accomplish.
[2095.90 --> 2111.68]  So I think I was pretty thrilled to see you guys doing that work there and understand that going forward, I think that we're going to have people all over the world as they look at these humanitarian assistance disaster relief scenarios, being able to have tools that they've never had available before to save lives.
[2111.94 --> 2115.36]  And I just wanted to really kind of draw out that social good on it.
[2116.08 --> 2118.84]  Yeah, I think that, you know, we're really happy working on this.
[2118.90 --> 2125.68]  This is one of those projects that makes you feel really good, you know, when you can get results and really deliver things to people because you know it's making a difference.
[2125.90 --> 2131.10]  And also to kind of touch on some of those other things, you know, there's a lot of other people in the community contributing to this as well.
[2131.10 --> 2139.98]  And this is actually one of the goals of the JAIC is also to kind of establish a platform that allows everyone to come in and contribute to this.
[2140.14 --> 2147.20]  It's not just Esri building models and, you know, running them, you know, for these different use cases.
[2147.68 --> 2154.68]  What we're also trying to do is we're trying to use, you know, this huge GIS platform that Esri has been building over a very, very long time
[2154.68 --> 2158.70]  as this sort of basis that other people can come in and start contributing to.
[2159.08 --> 2165.90]  So I think one of the big things for me that really makes these AI platforms really an attractive offering for something like this is that,
[2166.26 --> 2169.42]  you know, there's a lot of companies out there that can produce AI and do a great job of it.
[2169.46 --> 2170.48]  They do really amazing work.
[2170.74 --> 2173.64]  But in the end, you know, they give you sort of a model file.
[2173.64 --> 2174.52]  Maybe they give you weights.
[2174.68 --> 2179.48]  Maybe they even give you some results of, you know, what the output of their AI model is.
[2180.28 --> 2181.44]  But then what?
[2181.56 --> 2182.86]  You know, what do you really do with that?
[2182.86 --> 2187.10]  And I think that that's one of the things that Esri really brings to the table is that we have this entire platform
[2187.10 --> 2192.56]  with these hundreds of geoprocessing tools that have been built over a very long time by some very smart people
[2192.56 --> 2197.68]  that can now take that data and run further analysis on it and really make use of it.
[2197.68 --> 2204.96]  So in this case, you know, AI can be thought of as just sort of producing the data that you can then do even more analysis on.
[2205.50 --> 2207.98]  And, you know, you can kind of unleash this entire platform on it.
[2208.42 --> 2210.12]  I really like what you're saying about the platform.
[2210.12 --> 2212.82]  And we've discussed like a lot about satellite imagery.
[2213.34 --> 2214.72]  And I'm just kind of scrolling.
[2214.90 --> 2219.38]  As Chris said, you've got a lot of great use cases on your blog as well.
[2219.48 --> 2225.28]  And I see a lot of those are talking about 3D data as well, which we haven't really talked about much.
[2225.32 --> 2227.56]  So there's like the satellite imagery part.
[2227.68 --> 2232.28]  And we haven't really talked a lot about 3D data and AI on this podcast.
[2232.28 --> 2243.66]  So before we get too much further, I kind of wanted to see what your thoughts were in terms of the current state of AI utilizing 3D data and challenges around that.
[2243.66 --> 2246.02]  And what sort of use cases that fits into?
[2246.62 --> 2247.10]  Yeah.
[2247.26 --> 2254.32]  3D data has actually been a pretty big focus for, I'd say, the last year for my team and some others within Esri.
[2254.50 --> 2256.30]  There's a lot more LiDAR being collected.
[2256.30 --> 2261.32]  That's where a lot of the 3D data that we're talking about is coming from is from vehicle mounted LiDAR.
[2261.58 --> 2276.52]  So sometimes it's a Department of Transportation for a state or city that is driving around to collect roadside assets, such as street signs or anything that they need to know exactly where it is.
[2276.52 --> 2280.86]  And in the end, a human has to go through and extract those manually.
[2281.48 --> 2293.26]  So what we're doing with 3D deep learning, it's all been deep learning to this point, is trying to extract objects like that or run segmentation models to find buildings or vegetation.
[2293.72 --> 2296.18]  There's a lot of different applications that we've been seeing.
[2296.18 --> 2306.24]  So with 3D data specifically, I'm just thinking like, oh, 3D data, like it must be so big and hard to work with.
[2306.32 --> 2307.12]  Is that the case?
[2307.24 --> 2314.34]  Or are these, you know, these 3D data sets, are they in general like very large and hard to deal with computationally?
[2314.54 --> 2317.76]  Or is that just kind of a misconception on my part?
[2318.20 --> 2319.66]  Well, so it depends.
[2320.08 --> 2322.62]  That's usually the answer to most questions is it depends.
[2322.62 --> 2329.50]  But there's actually been a lot of really good advances in the last couple of years that make that problem less simple.
[2329.94 --> 2341.04]  A lot of times when I've worked with 3D data in the past, it has been with what's called a voxel model where, you know, with an image, you can have a 2D array of pixels and, you know, work in that space.
[2341.04 --> 2345.54]  Or you can stretch that into three dimensions and then your pixels become voxels.
[2345.54 --> 2355.20]  Now, data explodes when you start getting into voxel space because now you're talking about, you know, the cube of the number of points.
[2355.40 --> 2361.20]  But you can actually run deep learning models directly on groups of points themselves.
[2361.68 --> 2372.04]  So as long as the number of points in the, you know, the type of objects that you're detecting isn't absolutely massive, you can run these on regular hardware such as GPUs.
[2372.04 --> 2377.04]  To talk about a couple of specific models, we've been looking at things like PointNet and PointCNN.
[2378.38 --> 2381.92]  So PointNet and then Point Convolutional Neural Network.
[2381.92 --> 2391.54]  Those actually take in the individual points as features and they use a set of shared weights, basically, and then aggregations further down in the network.
[2391.54 --> 2397.18]  So you can have a network that takes an arbitrary number of points as an input.
[2397.78 --> 2412.24]  And it basically embeds that collection of points into some lower dimensional feature space that is then used by just, you know, pretty much a normal neural network to do classification and segmentation and object detection.
[2412.24 --> 2421.48]  And I noticed, you know, as you talk about that specifically, I noticed I'm looking at your blog as you're talking and you can, because you had, you guys have so much interesting stuff here.
[2421.58 --> 2423.24]  There's the PointCNN article.
[2424.22 --> 2425.66]  Could you take us through a use case?
[2425.66 --> 2428.70]  I want to ask about actually several of the use cases that you had here.
[2428.80 --> 2433.38]  Would you take us through that PointCNN one where you talk about replacing 50,000 man hours with AI?
[2433.94 --> 2434.28]  Sure.
[2434.68 --> 2438.44]  I'll do my best on that one since I did not directly work on that project.
[2438.96 --> 2439.60]  No worries.
[2440.22 --> 2443.86]  Dimitri, the guy who wrote the article, would be the perfect one to ask if you were here.
[2444.34 --> 2449.20]  But so that was using that algorithm I mentioned before called PointCNN.
[2450.86 --> 2456.20]  It's close, maybe not quite the state of the art at the moment, but it's still a very, very good algorithm.
[2456.90 --> 2461.88]  And in that case, what we did was we had a large training data set that was created manually.
[2461.88 --> 2470.72]  So some humans went through and they labeled utility poles and wires within a large LiDAR data set.
[2470.80 --> 2475.62]  I believe that was an airborne LiDAR data set, but I'm not entirely sure on that one.
[2476.10 --> 2484.38]  And it was a TensorFlow-based implementation of PointCNN, and it was trained on a single NVIDIA GV100 GPU.
[2484.76 --> 2486.88]  So it has 32 gigabytes of RAM.
[2486.88 --> 2494.72]  So to answer your question about size, to get a high performance, you still want to have a pretty large GPU or a set of GPUs.
[2495.08 --> 2498.10]  But in this case, we didn't even need multiple GPUs to train that model.
[2498.86 --> 2499.06]  Yeah.
[2499.28 --> 2500.88]  I just had one other quick follow-up.
[2501.10 --> 2503.88]  A moment ago, you were talking about voxels.
[2503.88 --> 2516.72]  And I'm wondering if you would go ahead and kind of tell us, not everyone, I've worked with it, obviously, but not everybody has, if you would describe what a voxel is and talk about how that works into a typical process.
[2516.72 --> 2520.64]  So when you're working with three-dimensional space, what is a voxel?
[2520.76 --> 2523.36]  How does it apply to a modeling process?
[2523.54 --> 2528.12]  And if you have a favorite use case that, you know, where you've used it, that would be great.
[2528.12 --> 2530.60]  I'm trying to make it tangible in this sense.
[2531.08 --> 2531.24]  Sure.
[2531.38 --> 2533.92]  So 3D data can be represented in a lot of ways.
[2534.26 --> 2538.88]  So one way is a point cloud, which is just each point has XYZ and some attributes.
[2539.30 --> 2541.44]  You can represent 3D objects as meshes.
[2541.72 --> 2553.78]  So when you're looking at like 3D models, such as in video games or in three-dimensional 3D animation movies, like Pixar animation and stuff like that, that's when you deal with mesh surfaces.
[2553.78 --> 2556.10]  And there's some other categories, too.
[2556.44 --> 2558.68]  The whole field of computer graphics talks about that.
[2559.20 --> 2564.00]  Voxels is what happens when you aggregate information into a fixed grid.
[2564.40 --> 2572.80]  So just like an image is a two-dimensional grid, a voxel, you can represent a 3D object as a 3D image made out of voxels instead of pixels.
[2573.38 --> 2577.76]  So just instead of an X width and a Y width, you'd also have a Z width as well.
[2578.30 --> 2578.78]  Awesome.
[2578.92 --> 2579.50]  Thanks for sharing.
[2579.50 --> 2586.44]  And I guess as we kind of get to the end here, there's obviously a lot of things that we don't have time to cover.
[2586.60 --> 2593.92]  And I encourage people to check out the Esri blog and some of their videos online, which we'll link in the show notes to explore further.
[2594.12 --> 2604.62]  But I was curious from both of your perspectives, what are you most excited about in terms of geospatial data and AI in the near future?
[2604.62 --> 2611.86]  What are you most excited about either working on personally or things that you've seen people working on out there that really excites you?
[2612.16 --> 2613.12]  Rob, you want to start out?
[2613.78 --> 2614.18]  Yeah, sure.
[2614.34 --> 2626.84]  One of the big things that I've been kind of tackling recently and been doing a lot of reading on is, I guess not particular to geospatial, but I think could play a big role in it, is unsupervised learning.
[2626.84 --> 2644.28]  We kind of consistently see the case that when we do engage with a client and a client asks us to do a problem, especially if it's something like an imagery type problem, they tend to not have enough imagery to really make a data scientist comfortable in results you might get from that.
[2644.28 --> 2653.56]  And so one of the big things that I've been thinking about a lot lately is some way of kind of doing unsupervised pre-training on some of these networks.
[2653.90 --> 2656.36]  Because satellite imagery all looks very similar.
[2656.50 --> 2668.46]  I would say, for the most part, satellite imagery from different parts of the world looks a little bit more similar than just your kind of random image net data set or something like that, just sort of cell phone pictures or oriented imagery.
[2668.46 --> 2688.84]  And I think that that could be a big advantage in that if you can extract a lot of information, you know, I kind of think of something like the image equivalent of BERT, for example, which, for those who don't know, is a language model that gets pre-trained on a massive corpus of text in order to sort of learn not necessarily specific tasks, but learn kind of about language in general.
[2688.84 --> 2702.08]  I've been really interested in this idea for sort of imagery where, you know, instead of learning to do some specific tasks, say, find a car or find a tree, you can teach some network to kind of understand what an object is.
[2702.22 --> 2715.86]  You know, if I see a line kind of going, you know, that's perfectly straight over here, you know, I can assume that, you know, that line is probably going to continue over here and that these all kind of constitute maybe one object or one thing that is like a discrete unit.
[2715.86 --> 2724.42]  And I think if you can get to that state, I think that the amount of data that you'll actually need to make really good progress on some of these imagery related tasks go way down.
[2724.88 --> 2733.70]  And this really opens up AI to a lot of companies that maybe don't have the capital or the time to invest in huge data sets and to label them as well.
[2734.52 --> 2737.44]  Sounds good. Daniel, do you have, what are you excited about?
[2737.44 --> 2747.22]  Well, I'm excited about most of it, but let me just kind of mention that a lot of the work that I've been doing for my career has been in the computer vision side.
[2747.72 --> 2752.44]  And I want to say I kind of lost interest in it as soon as deep learning started getting good.
[2752.96 --> 2756.14]  So really what I'm interested in is everything that's not imagery.
[2756.58 --> 2757.36]  Imagery is huge.
[2757.36 --> 2766.96]  It's there's a lot of amazing opportunities and ways that we can apply deep learning to it and extract a lot of value.
[2767.08 --> 2768.18]  So don't get me wrong.
[2768.26 --> 2769.98]  It's a very amazing place to be.
[2770.10 --> 2780.98]  But the problems that I've had the most fun working on and I think are really kind of the future of a lot of this geospatial data are either multimodal or non imagery data sets.
[2780.98 --> 2792.00]  So that's bringing things like imagery and text and what we call vector data or, you know, basically tabular data that also has, you know, geometric information, all of those together.
[2792.54 --> 2795.18]  So just to motivate that a little bit.
[2795.60 --> 2799.22]  The problem that I've been working on most recently is a car accident prediction.
[2799.32 --> 2804.04]  I actually have an article on that medium blog about the way we used to do it.
[2804.10 --> 2807.70]  And I hopefully will have one about the way we're doing it now coming out fairly soon.
[2807.70 --> 2819.18]  But that's that's a situation where if you think about it, you know, imagine yourself on the road and there is, you know, the terrain affects how far you can see affects the slope of the road.
[2819.46 --> 2821.98]  The road itself could be made in a curvy way.
[2822.38 --> 2823.74]  The speed limit changes things.
[2823.88 --> 2826.24]  The number of lanes changes things.
[2826.30 --> 2828.60]  The position of the sun in the sky changes things.
[2829.06 --> 2829.90]  The weather.
[2830.20 --> 2835.74]  So cloud cover or precipitation, snow, the conditions of the roads themselves.
[2835.74 --> 2839.36]  And all of that can be captured in a lot of different data sets.
[2839.64 --> 2840.66]  Some of that could be imagery.
[2841.12 --> 2845.04]  Some of that could be in the the actual geometry described on the road.
[2845.16 --> 2846.30]  Some of that could be in the table.
[2846.54 --> 2848.04]  It's all in different places.
[2848.04 --> 2855.20]  And it becomes really difficult to assemble all that information together into a model that can actually make a real world impact.
[2855.20 --> 2867.26]  So that's really what excites me is within the geospatial context is all of this data can be brought together in really interesting and novel ways that I think people are just starting to scratch the surface of.
[2867.26 --> 2872.02]  My whole career, I've been working on spatial data science.
[2872.44 --> 2876.96]  And it's been really hard to find, you know, oh, someone's done it before.
[2877.16 --> 2878.84]  I mean, chances are someone's tried it before.
[2878.84 --> 2889.96]  But it's such a hard and interesting problem that now that I think with the advent of so much large scale spatial data, a lot of people are starting to take notice of this field.
[2890.06 --> 2893.48]  And there's a lot of great work happening that we can capitalize on.
[2893.60 --> 2896.22]  I'll tell you what, that's a great place to close it out.
[2896.70 --> 2898.54]  Well said, both of you.
[2898.54 --> 2902.88]  And so I guess we'll wind up Daniel Wilson and Rob Fletcher.
[2903.28 --> 2909.36]  Thank you so much for coming on the show with Daniel Whitenack and myself to tell us all about what Esri is working on.
[2909.70 --> 2910.84]  It's been really fascinating.
[2911.22 --> 2912.20]  And I'll talk to you soon.
[2912.78 --> 2912.94]  Yeah.
[2912.98 --> 2913.92]  Thank you for having us.
[2914.28 --> 2915.12]  Thank you for having us.
[2919.32 --> 2921.18]  Thank you for listening to Practical AI.
[2921.68 --> 2928.52]  If you're not following Practical AI FM on Twitter, you're missing out on clips and highlights from past episodes, links and repos.
[2928.54 --> 2931.56]  From around the AI and data science community and more.
[2931.98 --> 2933.90]  Follow us, Practical AI FM.
[2934.10 --> 2934.86]  You won't regret it.
[2935.20 --> 2937.94]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2938.18 --> 2939.70]  It's produced by me, Jared Santo.
[2940.02 --> 2942.88]  And our music is brought to you by the Beat Freak, Breakmaster Cylinder.
[2943.38 --> 2944.54]  We have awesome sponsors.
[2944.72 --> 2945.28]  Support them.
[2945.44 --> 2946.24]  They support the show.
[2946.70 --> 2950.88]  Special thanks to Fastly, Linode, and Rollbar for helping us do what we do.
[2951.22 --> 2954.58]  If you aren't receiving Changelog Weekly every Sunday, you are missing out.
[2954.92 --> 2957.14]  It's our take on this week in the world of software.
[2957.14 --> 2958.94]  What's interesting and why.
[2959.28 --> 2962.34]  Head to changelog.com slash weekly to subscribe.
[2962.74 --> 2964.40]  Get it for the price of a free cheeseburger.
[2965.08 --> 2966.10]  Thanks again for listening.
[2966.40 --> 2967.42]  We'll talk to you next week.
