[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.18 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[102.28 --> 111.24]  Welcome to another Fully Connected episode where Daniel and I keep you fully connected
[111.24 --> 113.88]  with everything that's happening in the AI community.
[114.10 --> 116.72]  We'll take some time to discuss the latest AI news,
[116.84 --> 120.74]  and we'll dig into some learning resources to help you level up on your machine learning game.
[121.26 --> 122.50]  My name is Chris Benson.
[122.64 --> 124.76]  I'm the chief AI strategist at Lockheed Martin.
[125.00 --> 130.04]  And with me is my co-host, Daniel Whitenack, who is a data scientist with SIL International.
[130.14 --> 130.78]  How's it going today?
[130.78 --> 132.24]  It's going great.
[132.38 --> 136.10]  You know, dealing with allergy season, but such is life.
[136.32 --> 136.96]  How about with you?
[137.44 --> 138.54]  Exactly the same.
[138.74 --> 141.32]  I live in Atlanta, so there are plenty of pollen to go around.
[142.02 --> 146.58]  And looking forward to enjoying the weather without quite so much around.
[147.04 --> 147.28]  Yeah.
[147.56 --> 151.40]  If you hear me sipping something, it's tea with honey in it.
[151.46 --> 153.16]  And that seems to be doing the trick.
[153.40 --> 153.56]  Yep.
[153.74 --> 154.84]  I have my drink along.
[154.96 --> 159.46]  So we'll go through the episode and people will hear gulps from both of us as we go along here.
[159.46 --> 160.40]  No worries.
[160.60 --> 166.28]  So, you know, it's been a little while since TensorFlow Dev Summit this year.
[166.44 --> 166.64]  Yeah.
[166.78 --> 167.74]  Did you watch it online?
[168.12 --> 168.64]  I did.
[168.74 --> 173.48]  I didn't watch every part of it, but I watched quite a few videos of it since I wasn't there.
[173.48 --> 174.68]  And it was pretty awesome.
[174.80 --> 175.74]  A lot of the announcements.
[175.74 --> 183.76]  I had been, you know, we had our episode previously where we were talking about TensorFlow 2 and, you know, in contrasting it with PyTorch.
[184.08 --> 190.10]  And, you know, having gone to this point, I was really excited about some of the announcements we knew were going to come out of this.
[190.10 --> 199.46]  And so even though it's been a little while, I wanted to recap kind of what happened at TensorFlow Dev Summit this year, what the announcements are, and some of the implications.
[199.68 --> 200.20]  You good for that?
[200.48 --> 201.44]  Yeah, that sounds great.
[201.56 --> 206.62]  I was at the TensorFlow Dev Summit not this year, but the previous one.
[206.70 --> 209.40]  It was definitely very inspiring and lots of good stuff.
[209.40 --> 217.14]  You know, like you said, we had the episode about TensorFlow 2.0 when it wasn't really like we were just kind of hearing about it.
[217.36 --> 220.60]  So making some of those things concrete, I think, would be great.
[220.76 --> 224.60]  Also, because I'm learning a lot about them right now as well.
[224.74 --> 229.24]  So I'd be happy to learn some things from you and do a little bit of recap.
[229.70 --> 232.70]  Well, I am certainly no expert at it, but I've used it.
[232.80 --> 234.34]  I'm delighted as we get into it.
[234.34 --> 248.78]  So some of the key things about TensorFlow is they had announced the alpha release at the Dev Summit and have gotten into it a little bit and been reading the docs and trying some of the various examples they offer and starting to think about making it my primary tool going forward.
[248.78 --> 258.40]  And the very first thing I think that will impact the most people is the fact that they have officially adopted Keras as kind of their primary interface into it.
[258.40 --> 273.40]  It's kind of an 80-20 rule in that now you're going to do 80% of your work probably through Keras and you would only go through some of the traditional very difficult things that maybe Keras doesn't hit if you're out there kind of as an edge case through more of the traditional TensorFlow API.
[274.36 --> 278.98]  And so they're deprecating some APIs and combining it and trying to generally clean it up.
[279.16 --> 280.68]  Have you used Keras in the past?
[280.84 --> 284.30]  Yeah, I mean, I've done some like examples and that sort of thing.
[284.30 --> 295.38]  I think maybe like so Keras in general, it's kind of like a wrapper around some or a higher level interface around some of the TensorFlow internals.
[295.50 --> 297.00]  Is that like how you would describe it?
[297.36 --> 298.46]  Yeah, I would.
[298.66 --> 303.70]  And that's mostly actually how I've used TensorFlow in the past is actually with Keras on top of it.
[303.88 --> 306.86]  And I think a lot of people in the community would say the same thing.
[306.86 --> 310.22]  And it's a much more user-friendly API.
[310.38 --> 311.34]  It's a higher level API.
[311.78 --> 319.64]  And it feels a lot more familiar to people who have done object-oriented or functional programming in other languages.
[319.98 --> 321.56]  And so it's a lot simpler.
[321.96 --> 324.66]  But most of the things you're going to do are covered by it.
[324.66 --> 340.60]  And then if you happen to be one of those people who has some sort of either extremely complex use case or kind of an edge or maybe you're working on a new architecture in some way, then you might abandon Keras and go into the other lower level APIs that they offer.
[340.60 --> 345.52]  Yeah, so maybe it would be helpful for me as well to just think about.
[345.98 --> 362.60]  So if we were to do programming with TensorFlow and let's say that we're creating a neural network of some kind prior to TensorFlow 2.0 and Keras being default, from your perspective, what would it look like to kind of program TensorFlow without Keras?
[363.38 --> 368.60]  Like to me, it seemed kind of like you had to write a lot of code and a lot of boilerplate.
[368.60 --> 370.90]  Is that kind of your experience?
[371.12 --> 375.24]  Or what's kind of the main thrust of what Keras adds and gives you?
[375.66 --> 375.76]  Sure.
[375.90 --> 384.70]  So I think the biggest thing that people are talking about that was welcome and certainly makes it easier is the fact that it is defaulting to eager execution.
[385.12 --> 389.40]  And so eager execution is where you're typing your commands out.
[389.46 --> 390.66]  It's going ahead and doing them.
[390.70 --> 395.14]  And you're seeing a lot of the other popular frameworks have already been doing that.
[395.14 --> 410.72]  And so prior to give you a contrast prior to eager execution becoming the default through Keras in TensorFlow 2, TensorFlow 1.x graph is essentially you can think of it as having to write out a plan and all the way through.
[410.88 --> 414.86]  And then, you know, you kind of get a complete plan and then you run it.
[414.86 --> 426.36]  And so whereas, you know, if you're used to working in a lot of languages where you can just type in a command and every command can take effect immediately, you didn't have that option in TensorFlow 1.x.
[426.44 --> 427.90]  So you create these graphs.
[428.00 --> 428.80]  It was more complicated.
[429.00 --> 430.06]  It was a lower level API.
[430.06 --> 435.54]  And so it was more effort to create it if you were not already familiar with the syntax.
[435.80 --> 439.64]  And then you'd have to kind of run it and see where you're at and kind of start all over.
[439.92 --> 442.68]  So that was both a challenge for those users.
[442.86 --> 446.38]  It was also really the source of power in TensorFlow 1.
[446.38 --> 455.14]  And that, you know, that is fundamentally what you're working on is you're working on a graph that you are assigning all the various attributes and nodes to.
[455.30 --> 459.58]  And you're creating this architecture in your graph and then you would go execute it.
[459.58 --> 471.94]  And Keras is kind of giving you a very friendly wrapper, as you said, around that so that a lot of the complexity that you were subjugated to in TensorFlow 1.0 if you were not using Keras, a lot of that's been taken away.
[472.04 --> 475.68]  And reasonable defaults have been put in place because that's what most people are going to use anyway.
[475.68 --> 486.08]  So I think the user experience is now probably competitive with things like PyTorch and other frameworks that people have said, you know, I just don't want to deal with TensorFlow.
[486.30 --> 487.26]  Let's go do X.
[487.68 --> 487.84]  Yeah.
[488.02 --> 490.68]  So you're exactly describing me.
[490.98 --> 502.62]  So a lot of these things, like when I would try to do examples with TensorFlow, especially if I wanted to like start with an example that was kind of similar to where I wanted to get it with my model for work.
[502.62 --> 510.74]  I would start with that example, but it was really hard for me to kind of grasp what I needed to change to kind of adapt it to my situation.
[510.90 --> 517.88]  And I think a lot of that had to do with maybe the verbosity partly, but I think mostly the eager execution.
[518.22 --> 521.24]  So kind of like what you're saying here, there's really two things at play.
[521.36 --> 527.04]  There's the API or the syntax or the kind of packages that allow you to build things up quickly.
[527.04 --> 529.08]  That's kind of the Keras side of things.
[529.20 --> 531.38]  So I'm looking at a Keras example right now.
[531.52 --> 538.52]  And, you know, you can kind of import these Keras layers and there's dense layers and 2D convolutional max pooling.
[538.66 --> 546.38]  And so these sorts of things just like give you really quick access to commonly used like building blocks of neural networks.
[546.38 --> 554.96]  And so I think that removes kind of some of that verbosity element allows you to build things really quickly and like add them kind of build up a model very quickly.
[555.38 --> 558.44]  And the other thing then, like you were saying, was the eager execution.
[558.68 --> 570.02]  So even if you were able to build up this model very quickly, I think that the graph sort of execution that you had in TensorFlow 1, which also is still part of TensorFlow 2.
[570.02 --> 571.98]  So you can do that if you want to or need to.
[572.38 --> 583.54]  But I think that was really a blocker for me personally, you know, kind of in the same way that I always struggled programming Spark jobs and other things that were not executed immediately.
[583.64 --> 598.36]  When I like when I sent a command, if things were just kind of instructions were getting stored up and they weren't executed immediately is really tough for me to get over that hurdle of debugging and optimization and kind of interactive development.
[598.36 --> 600.36]  I never really got the hang of that.
[600.42 --> 605.04]  And I think that carried over when I was trying to do things in TensorFlow 1.
[605.50 --> 607.70]  Yeah, I think a lot of people had that experience.
[608.00 --> 616.08]  So I think a couple of the key things to call out are that the way Keras is doing it is much more kind of Pythonic.
[616.24 --> 623.82]  It's the way you would expect Python to be structured, whereas TensorFlow under the hood, it's really focused on the graph.
[623.82 --> 630.24]  And you're really almost thinking almost like it's a language unto itself in terms of the way it's put together.
[630.38 --> 638.72]  And I'm not talking about the syntax, but it's not a natural way of thinking necessarily for everybody who is using Python out there, whereas Keras very much was.
[638.82 --> 641.86]  So it's kind of working in a mind frame that they're already used to.
[642.22 --> 647.28]  And now with the eager execution, you know, the TensorFlow site notes that it's a more intuitive interface.
[647.38 --> 650.10]  It's easier debugging and a more natural control flow.
[650.10 --> 660.42]  And I think just that sense of familiarity and the expectations you have will be met will bring a lot of people back that may have looked at it the first time and said, ooh, too much.
[660.54 --> 661.90]  You know, I don't want to deal with all that.
[662.04 --> 664.00]  And hopefully it'll bring them back in.
[664.28 --> 666.60]  Yeah, it's like I just saw a tweet recently.
[666.76 --> 671.30]  And I'm sorry if you wrote this tweet and I forget, mentioned you, I forgot who it was.
[671.30 --> 682.12]  But it was something like, you know, when you first start doing out or doing side projects and other things with with programming, you're like, oh, I'm going to write everything in C and low level.
[682.12 --> 684.34]  And like, I'm going to understand all these pieces of it.
[684.44 --> 688.70]  And 10 years later, when you're doing side projects, you just want to build something like super quick.
[688.96 --> 690.76]  And I think it's the same actually in organizations.
[690.76 --> 694.96]  Like after a certain point of time, you just need to be able to iterate really quickly and all that.
[694.96 --> 697.14]  So, yeah, I'm really happy to see this.
[697.38 --> 705.18]  Also, it's pretty cool how they you can actually like switch back and forth between like kind of offloading things to the graph and then executing it.
[705.24 --> 710.24]  And then coming back, there's this like little decorator you can call TF function on a function.
[710.60 --> 713.98]  And, you know, and then it's a graph apparently or it goes to the graph.
[714.12 --> 715.28]  And so that's pretty cool.
[715.34 --> 720.22]  I think that they've I mean, I hope I know it's been something that they put a lot of thought into.
[720.22 --> 730.02]  So I hope it works out that it is actually a lot easier to use and, you know, really eases the burden, the logical burden as people try to learn TensorFlow.
[730.26 --> 731.58]  I'll certainly be trying myself.
[731.94 --> 743.06]  You know, when I was in New York City recently at the AI conference that O'Reilly puts on and somebody and I'm trying to remember who it was that I was talking to, but somebody had a great analogy.
[743.06 --> 752.66]  And they were they were saying if you want to think of the old version of TensorFlow, you could almost think of it as some programmers may recognize this, not everybody, but an abstract syntax tree.
[753.00 --> 769.12]  And in the sense that when you're writing in a programming language and you have whatever the syntax of what you're working in, it gets compiled down into what's called an AST, abstract syntax tree, which is a representation of the language that is let's just say it's more friendly to the system to be able to utilize.
[769.12 --> 779.38]  And so they were kind of comparing that the graph of TensorFlow one is to creating an AST and then having to go and execute it, whereas, you know, versus the more Pythonic approach.
[779.38 --> 790.26]  And one of the things that I noticed that I was really kind of welcoming and seeing was that I noticed that Keras, it has what I've used mostly, which is an object oriented approach, which is kind of its default.
[790.48 --> 793.68]  But it also has a functional approach, which is strictly functional.
[793.80 --> 799.08]  And therefore, people coming into this from functional programming languages should find that very welcoming.
[799.30 --> 803.42]  So it's it kind of gives you an option from a lot of different areas.
[803.42 --> 811.50]  You know, if you're coming in from a very functional ethos, then you should feel right at home in Keras there as well, just like the rest of us who've, you know, done OO for years.
[811.82 --> 812.80]  Yeah, this is exciting.
[812.80 --> 816.10]  And I know that there's a bunch of resources online.
[816.10 --> 818.42]  We'll put some links in the show notes.
[818.42 --> 829.80]  But I know that there's several Google CoLab notebooks and other other resources if you're wanting to kind of experiment a little bit with with TensorFlow 2.0.
[829.80 --> 834.94]  There's a bunch of stuff out there. And they announced a bunch of learning resources at the summit as well.
[835.04 --> 836.98]  So we'll kind of go through those soon.
[837.42 --> 839.58]  But there's a lot of resources out there.
[839.72 --> 843.44]  And I guess, is it still the alpha release of TensorFlow 2.0?
[843.52 --> 844.22]  Or has that changed?
[844.70 --> 846.92]  As we're recording this, I think it's still the alpha.
[847.18 --> 850.54]  I tried updating a few days ago, and it was the same.
[850.66 --> 854.40]  They had not done a more current one that I can't swear to it at this point.
[854.40 --> 860.66]  But I'm hoping that they're getting enough feedback within the community to get a next build out pretty soon.
[861.06 --> 861.52]  Cool. Yeah.
[861.62 --> 869.92]  And we would love if anyone that's interested wants to join the conversation that we're having around TensorFlow 2.0, you can join.
[870.02 --> 874.52]  We have a practical AI Slack team, a Slack channel in the Changelog Slack.
[874.68 --> 878.40]  You can join that at changelog.com slash community.
[879.00 --> 883.44]  We also have a LinkedIn page where you can provide some comments.
[883.44 --> 885.98]  So let us know what you're thinking about TensorFlow 2.0.
[886.10 --> 891.18]  If you think things are improved or not improved in certain ways, let us know.
[891.22 --> 892.52]  We'd love to hear your feedback.
[893.02 --> 898.28]  So they made some other announcements as well that are kind of in the ecosystem at large.
[898.36 --> 903.46]  And I thought maybe probably the next thing that certainly got me very excited was TensorFlow datasets.
[903.46 --> 914.22]  So they have actually, within the TensorFlow namespace, just like you have now tf.keras, you also have tf.data.datasets.
[914.60 --> 926.00]  And they have really done a lot of work to try to make all the work on getting data into TensorFlow and pulling it from various places much, much easier than they previously had.
[926.00 --> 930.58]  And they have a TensorFlow, a tf.data.api that goes along with that.
[930.58 --> 943.42]  And they're putting lots of popular research datasets such as MNIST and Street View House Numbers and the 1 billion word language model benchmark and large movie reviews dataset.
[943.60 --> 946.52]  All these things are now in it and they're going to keep adding that in.
[946.52 --> 958.72]  So I haven't tried that side of it, but I think the effort is, you know, we're always talking about how we spend 80% of our time getting the data ready and, you know, finding the right data and combining it and all that.
[958.78 --> 963.92]  And I think this is intended to really make that process a bit less painful.
[964.72 --> 964.88]  Yeah.
[965.02 --> 971.42]  So I have a little bit of a gripe here and I don't think it's not against this necessarily.
[972.00 --> 975.08]  So I'm all for this TensorFlow datasets thing.
[975.08 --> 985.34]  And I think particularly for like getting up to speed with TensorFlow and figuring out like the different patterns and getting something, you know, from zero to running.
[985.66 --> 987.06]  This is really great.
[987.50 --> 990.86]  My gripe, and actually I just encountered this like over the weekend.
[991.08 --> 994.04]  I was, I shouldn't say I was working over the weekend because I shouldn't have been.
[994.18 --> 999.04]  But I was more playing over the weekend with PyTorch, not with TensorFlow.
[999.04 --> 1009.00]  And a lot of these APIs, like the TensorFlow datasets, there's also this in scikit-learn and other modeling packages where you can like import this dataset or that dataset.
[1009.00 --> 1012.26]  And it does seem kind of like magic as it comes in.
[1012.42 --> 1019.58]  And so I was working off some example that was like a machine translation example using RNNs or recurrent neural networks.
[1019.98 --> 1025.24]  And it used one of these datasets and not the TensorFlow datasets, but a different one.
[1025.24 --> 1028.22]  And so I was able to run it pretty quickly.
[1028.22 --> 1036.14]  But then I was like thinking, okay, well, now I want to use my own data, which is not available in the API that loads datasets.
[1036.14 --> 1049.12]  And it was really tough for me to figure out like, how do I get my custom dataset into the format that the automatically loaded dataset was imported into?
[1049.34 --> 1050.70]  And that's caught me several times.
[1050.78 --> 1055.70]  Even in like scikit-learn, it's like you kind of do this magical import and it's great.
[1055.70 --> 1060.34]  But then figuring out the format that was imported and what happened, it was a little bit tough.
[1060.42 --> 1062.08]  So maybe that's not the case with these.
[1062.08 --> 1069.26]  But in general, that's my one gripe about these sorts of things is it kind of hides a little bit of that pain.
[1069.60 --> 1070.90]  Yeah, I think so.
[1071.04 --> 1081.52]  I'm waiting to try it out myself because I know when I was watching the video of the announcement for it, it sounded pretty awesome, as you would expect.
[1081.74 --> 1085.34]  But I haven't actually tried it, like I said, to see if it helps.
[1085.34 --> 1095.02]  I know that the things that they were talking about were they have this whole API that supposedly will help you bring in your data and use it.
[1095.40 --> 1098.86]  And if it's not in the right format, it will help you convert.
[1099.62 --> 1106.12]  I know that they have this concept of the dataset builder and that every dataset is supposed to be exposed as a dataset builder.
[1106.12 --> 1111.38]  And so, you know, you can download, extract, and write it to a standard format.
[1111.60 --> 1119.30]  And I know they had a method call that's like download and prepare and that you can load it from disk with the as dataset and some of the others.
[1119.74 --> 1123.14]  So they were very clear.
[1123.40 --> 1129.58]  You know, it looked like they were well-written as method calls in that it was very clear what you would do with them.
[1129.64 --> 1130.38]  They were named well.
[1130.38 --> 1135.60]  I do not know if it fully meets the expectation that they at least set with me.
[1136.04 --> 1138.76]  I'm looking forward to less pain in the future.
[1138.94 --> 1141.74]  And I will be frustrated if it turns out not to live up to that.
[1142.26 --> 1142.86]  Yeah, for sure.
[1143.02 --> 1149.32]  So, like, please reach out to me if you know how to ease some of my burden on this front.
[1149.44 --> 1155.36]  It looks like I'm kind of looking through some of the examples now on the TensorFlow datasets site.
[1155.36 --> 1162.72]  And it looks like they're imported as this tf.data.dataset format or type.
[1163.14 --> 1170.84]  So if that's fairly standardized and there's good documentation around that type, then maybe that would ease some of my concerns.
[1171.20 --> 1177.88]  But, yeah, it's like the thing loads in and then you can immediately call some model to train on this dataset.
[1178.14 --> 1181.60]  And it's sometimes hard to figure out what the format of that is.
[1181.68 --> 1184.36]  But it seems like this is a fairly standardized thing.
[1184.36 --> 1185.52]  So maybe it's not an issue.
[1185.98 --> 1186.28]  I hope so.
[1186.30 --> 1192.50]  It'll be interesting to see if the community at large, you know, really, you know, takes this on.
[1192.68 --> 1199.10]  I think to be really useful, you'd have to start, I mean, put in, you know, hundreds or thousands of different datasets.
[1199.10 --> 1204.82]  So people, you know, where it's already there and people don't have to go and do the conversion themselves and such.
[1204.82 --> 1212.12]  I think it would be cool to have something like, you know, if you go to data.gov and look at all the different datasets that are available there.
[1212.50 --> 1215.14]  And I've pulled from that as a source in the past.
[1215.26 --> 1221.78]  And if you could get, I don't know, an initiative door, many of these datasets that are very useful get pulled over and automatically converted.
[1221.90 --> 1224.90]  Maybe upcoming census data would be great.
[1224.90 --> 1235.00]  So I'm kind of looking to see where the promise goes down the road and whether or not they get much larger than the 29 that they announced.
[1235.54 --> 1236.38]  Yeah, yeah, for sure.
[1236.52 --> 1239.36]  I'm interested to follow it.
[1239.36 --> 1248.62]  This episode is brought to you by Discover.Bot.
[1248.82 --> 1252.80]  Learn everything there is to know about bots at Discover.Bot slash Practical AI.
[1253.36 --> 1261.22]  Discover.Bot was built by Amazon Registry Services as an online community for bot creators and makers of all skill levels to learn from one another, to share stories.
[1261.22 --> 1271.44]  And they regularly publish guides and resources to answer questions like how to set up payments to your bot, how to stop shopping cart abandonment, what KPIs are worth measuring, how to write an engaging chat bot dialogue.
[1271.88 --> 1273.82]  You can even register .bot domains there.
[1274.10 --> 1278.78]  Learn more and explore this huge library of bot resources at discover.bot slash practical AI.
[1279.18 --> 1281.56]  Again, discover.bot slash practical AI.
[1291.22 --> 1303.26]  It seems like, you know, there was, I guess this TensorFlow data set is kind of, you know, was announced and integrated within TensorFlow.
[1303.26 --> 1310.00]  But there were also a lot of things that were announced that are kind of like, like add-ons or bolt-ons to TensorFlow.
[1310.40 --> 1312.36]  They're actually calling them add-ons as well.
[1312.36 --> 1312.56]  Add-ons.
[1312.70 --> 1312.92]  Okay.
[1313.02 --> 1316.66]  So I'll call them add-ons to be, to be correct.
[1316.66 --> 1320.90]  So I don't offend anyone at Google, which I, I hope to not do.
[1321.10 --> 1325.54]  But yeah, so one of those was TensorFlow federated.
[1325.54 --> 1335.06]  Like I have this memory in my mind when they like announced TensorFlow federated, even with like the same picture, like I feel like it was like a year or two ago.
[1335.06 --> 1336.96]  And I remember them talking about it.
[1336.96 --> 1344.16]  And I don't remember anything between then and now until they announced it, you know, at the Dev Summit.
[1344.16 --> 1349.38]  So maybe it just kind of took that long to materialize into existence or, or something.
[1349.38 --> 1351.58]  But it does seem pretty cool.
[1351.68 --> 1354.92]  Did you understand kind of the gist of what TensorFlow federated is?
[1355.22 --> 1361.42]  I've read what they have on the site about it, but I'm not sure that I have fully grokked how I'd use it.
[1361.72 --> 1371.04]  On the site, they say it's an open source framework for machine learning and other computations on decentralized data, which isn't a terribly useful statement by itself.
[1371.46 --> 1372.86]  What's your understanding of it?
[1372.86 --> 1377.18]  Yeah, so the video associated with this one did, did help me.
[1377.48 --> 1391.62]  It seems like to me that there's kind of a relevant cycle that happens with TensorFlow federated in that you've got all of these devices, whether they're phones or tablets or whatever they are, with some small amount of the data set that you want to train on.
[1391.62 --> 1399.28]  And so what happens is you initialize a model on each of these devices and then do a bit of training on each device.
[1399.28 --> 1412.72]  And then those devices send updates to a central server, which kind of combines all the models together from all the different devices and then sends out a new initial model for them to continue to retrain.
[1412.72 --> 1425.78]  So you've kind of got this cycle going on where the devices are pushing up initial and next models to a centralized server that's combining them and then pushing a model back to the devices.
[1426.22 --> 1428.00]  So it's a pretty interesting idea.
[1428.00 --> 1432.02]  Yeah, I know that, of course, there's implications for privacy and other things.
[1432.02 --> 1438.12]  If you don't have to have people's data leave their devices, of course, that's a really nice thing.
[1438.12 --> 1448.52]  But also, you know, you may not have to do as much data transformation or like store as much data on, you know, in your own infrastructure either.
[1449.10 --> 1455.50]  I don't know how the one thing that I question about this is like, how many people other than Google would use this?
[1455.78 --> 1458.64]  That's the one thing I maybe struggle with a little bit.
[1458.64 --> 1465.84]  Yeah, I mean, if you're if you're using like a cloud provider and your GPUs or TPUs or whatever you're using is abstracted away.
[1465.84 --> 1476.08]  I don't know the maybe if I know like my employer has a whole bunch of DGX machines and maybe for splitting large workloads across those.
[1476.38 --> 1477.84]  I suppose that might make sense.
[1478.18 --> 1486.48]  Yeah, if I mean, if you had an app that was very privacy sense, you know, privacy restrictive or, you know, your data really couldn't leave devices.
[1486.82 --> 1489.08]  Okay, yeah. And are you talking about federated or privacy?
[1490.12 --> 1493.52]  Federated, but I guess that leaves leads to privacy.
[1493.52 --> 1499.38]  So federated is, I think, related, you know, our listeners, please correct me if I'm wrong.
[1499.50 --> 1510.00]  But, you know, there is a privacy advantage to federated in the sense that you are training on a federation of devices without data leaving those devices.
[1510.48 --> 1517.90]  And so you don't have to pull data, you know, maybe sensitive data from people's devices back to a central place to train on it.
[1517.90 --> 1524.40]  But then there is another announcement that they had around a specific library TensorFlow privacy.
[1524.78 --> 1525.02]  Yep.
[1525.22 --> 1531.38]  Which deals with differential privacy, which I hear is on trend.
[1531.80 --> 1541.00]  Yeah, I'm assuming that this is kind of a response to the fact that over the last year, privacy issues around data sets has become, you know, we keep we're talking about it on so many episodes.
[1541.00 --> 1547.86]  At some point, you know, there's GDPR and which is the general data protection regulation in Europe.
[1547.86 --> 1557.48]  And so I guess this is an early attempt to formalize, you know, how we do privacy guarantees in data sets, you know, and for training and such.
[1557.48 --> 1572.88]  Yeah, and for our listeners and for myself as well, this idea of differential privacy is is really a way to put limits on kind of the impact to people's private information that you're storing.
[1572.88 --> 1586.40]  I remember I probably point our listeners to some great talks that I've listened to in the past from Jim Klukar and others from Amuda, who they were a guest on our show.
[1586.88 --> 1591.00]  Actually, maybe it was early on one of the first episodes.
[1591.16 --> 1591.32]  Yeah.
[1591.74 --> 1597.26]  But they have some great information related to differential privacy if you want to learn a little bit more about that.
[1597.26 --> 1602.94]  But it does seem that this idea is filtering into the mainstream now.
[1603.14 --> 1605.62]  So definitely something to to check out.
[1605.72 --> 1609.32]  What what other announcements were interesting for you, Chris?
[1609.64 --> 1615.76]  Well, they talked about TensorFlow probability as a library for probabilistic reasoning and statistical analysis.
[1615.76 --> 1619.90]  Sounds like something those finance people would like.
[1620.84 --> 1621.80]  Probably so.
[1621.80 --> 1632.68]  And they, you know, they they talk about that it is a Python library built on TensorFlow that makes it easy to combine probabilistic models and deep learning on model hardware.
[1632.68 --> 1634.98]  And then they they call out TPUs and GPUs.
[1635.14 --> 1641.02]  So this is one I haven't delved very far into, but I'm looking forward to trying it out.
[1641.02 --> 1645.62]  Chris, have you used a TPU in for your work yet?
[1646.02 --> 1647.02]  I have not.
[1647.02 --> 1653.74]  Well, I'm assuming I have in terms of using collaboratory because I've done that plenty of times.
[1653.92 --> 1655.82]  But at work we have.
[1656.04 --> 1657.54]  So and this is just us.
[1657.60 --> 1659.38]  We have NVIDIA DGXs.
[1659.46 --> 1662.42]  So we're using GPUs from NVIDIA in that case.
[1662.42 --> 1665.22]  And that may change over time or we may add other vendors in.
[1665.26 --> 1667.74]  But that's where the bulk of my my focus has been.
[1667.74 --> 1675.82]  Yeah, I was just kind of curious about maybe I can look up some statistics online about the adoption of TPUs versus GPUs.
[1675.82 --> 1678.38]  But I'll have to come back with that in a follow up episode.
[1678.94 --> 1680.06]  Yeah, I'd be curious.
[1680.18 --> 1684.84]  I mean, I don't do you know if if there if TPUs are being sold outside of Google Cloud?
[1684.90 --> 1687.48]  Because I'm just not familiar with it since I haven't been doing it directly.
[1687.48 --> 1692.06]  I mean, not not to my knowledge, but someone please correct us if we're wrong.
[1693.18 --> 1700.60]  But yeah, my only interaction so far is in is in CoLab and trying them out there.
[1700.78 --> 1703.48]  And but haven't haven't done a lot with them.
[1703.48 --> 1706.98]  Yeah, you know, maybe this is an invitation to Google to come on the show.
[1706.98 --> 1713.12]  You know, a while back, we did have NVIDIA's chief scientist Bill Daly come on and talk about GPU technology.
[1713.34 --> 1719.28]  So if someone from Google wants to come on and talk about their TPUs, we you have an invitation right here.
[1719.74 --> 1720.60]  Sounds good.
[1720.94 --> 1724.98]  Along those same lines, though, they did talk about like performance enhancements.
[1724.98 --> 1728.98]  They also talked about a talking about the Dev Summit.
[1728.98 --> 1735.88]  Now they talked about, you know, another add on or bolt on called mesh tensor flow.
[1736.02 --> 1736.40]  Yeah.
[1736.46 --> 1749.80]  Which sounds very esoteric and interesting, but apparently some type of thing that allows for massively parallel goodness of some kind that I don't fully understand.
[1749.80 --> 1751.96]  But yeah, I should watch the talk again.
[1752.36 --> 1752.64]  I should.
[1752.80 --> 1758.38]  Once again, that's one of those things that sounds very Google-ish to me, you know, just from a scale standpoint.
[1758.92 --> 1762.34]  So it'll be interesting to say how many people are uptaking that.
[1762.72 --> 1763.70]  Yeah, I don't.
[1764.26 --> 1764.54]  Yeah.
[1764.82 --> 1770.00]  Sometimes that's kind of with when I was there at Dev Summit and also this year watching remotely.
[1770.00 --> 1778.36]  It's like I really enjoy some of the things and hearing about some of the things and some of them are like immediately like, oh, yeah, that's great for users.
[1778.64 --> 1782.20]  And then other things I'm like, oh, that's really cool that Google did that.
[1782.20 --> 1787.78]  But and now I'm glad I know, but I don't know that it's going to impact in in very many ways.
[1787.78 --> 1797.74]  But I'm sure there's a lot of like research people maybe in like higher performance computing and like these large scale models and other things that it's going to make their life a ton better.
[1797.74 --> 1798.78]  And that's that's great.
[1799.08 --> 1799.56]  That's true.
[1799.64 --> 1812.14]  You know, one of the add on announcements I am keenly interested in and we just had a show on reinforcement learning and, you know, kind of got schooled in what deep reinforcement learning is and the state of the art.
[1814.10 --> 1827.18]  And timely for that is TF Agents, which is a library for reinforcement learning and TensorFlow, because historically, at least, you know, in my exposure, people may be using TensorFlow and deep learning, but they would tend to turn to other tools.
[1827.18 --> 1831.90]  And maybe there may be some TensorFlow people out there saying saying, wait, we have a way of doing it.
[1831.96 --> 1835.84]  But they're really standardizing it on TensorFlow 2.0 with this add on.
[1836.00 --> 1846.08]  So I'm looking forward to trying that out because that's that's a passion area for me is is reinforcement learning because robotics and simulation, you know, it's it's all about that.
[1846.08 --> 1862.48]  All right. So because we're practical here at practical AI, I think one really interesting thing to talk about with respect to TensorFlow 2.0 and recent announcements is the TensorFlow Extended or TF X, I guess you're calling it.
[1862.56 --> 1862.98]  Yep.
[1862.98 --> 1868.64]  So I think that's a lot of stuff, which is really concerned with, in my understanding, end to end workflows.
[1868.64 --> 1890.98]  So as our listeners, I'm sure know, and, you know, if you have kind of tried to implement any sort of AI related thing in production, you realize that, you know, the training bit, which is often emphasized to the training of a model or the fitting of a model is often a very small part of the overall work that's required and pipelining that's required to put AI into production.
[1890.98 --> 1894.80]  So you have to have things that deal with data pre-processing.
[1895.40 --> 1899.54]  You have to have things that deal with model serialization and optimization.
[1899.54 --> 1906.54]  You have to have things that deal with logging and monitoring and also serving of models through some API.
[1907.50 --> 1909.84]  And so there's a lot of different pieces of this.
[1909.98 --> 1918.68]  And my understanding is that TensorFlow Extended is meant to deal with the kind of complexity of that scenario.
[1919.12 --> 1920.08]  That's what I got out of it.
[1920.08 --> 1921.02]  And I got that, too.
[1921.06 --> 1938.32]  And I actually think this may be this is certainly one of those most important announcements that came out of it, because if there's it, I think this is where looking slightly outside the deep learning space and looking at software in general and how you make it work in a real life situation.
[1938.32 --> 1943.62]  This is Google's answer to making it work in the real world by giving you an end to end platform.
[1943.62 --> 1951.08]  Because, you know, for a while, as TensorFlow came out, there were a lot of things that you had to do on your own and figure your own way out.
[1951.14 --> 1958.78]  And it was it was interesting as I worked with several different organizations that were interested in in doing deep learning and operationalizing it.
[1958.78 --> 1959.50]  It was funny.
[1959.50 --> 1968.52]  I could go from both, you know, like the last two organizations, they both were using TensorFlow, but they were both doing it in very, very different ways.
[1968.52 --> 1970.18]  And there was no standardization there.
[1970.34 --> 1982.96]  So I'm hoping that this is something that the entire community can buy into and we can make it better and better and therefore have a very sane expectation on how you how you operationalize.
[1982.96 --> 1984.64]  So I'm pretty excited about this.
[1984.64 --> 1985.32]  Yeah.
[1985.54 --> 1995.22]  So just to give people an idea, I think the the main things here that TensorFlow extended includes what they're calling components.
[1995.22 --> 1997.96]  I think I'm using getting the word right.
[1998.04 --> 2003.80]  So they have components and those components share or report kind of metadata.
[2004.06 --> 2007.50]  And those components are connected together in pipelines.
[2007.50 --> 2017.98]  And you might have a component, let's say, for training, a component for evaluation, a component for post-processing or whatever that is.
[2018.40 --> 2022.66]  All of those are kind of separate and you can pipeline them together.
[2023.22 --> 2027.90]  And then they all report sort of metadata to this common metadata store.
[2028.40 --> 2033.70]  And that metadata store then kind of tracks when and how those components have run.
[2033.70 --> 2042.04]  And then there's an orchestration element that would orchestrate those components working together to accomplish one or more tasks.
[2042.66 --> 2050.98]  So it's very kind of pipeliney in the same way that people talk about pipelines with, let's say, the Airflow project and others.
[2050.98 --> 2064.60]  And they showed examples with TensorFlow extended where it integrates with things like Airflow or Kubeflow pipelines, where you're trying to manage these sort of pipeliney things and track them over time.
[2065.34 --> 2071.14]  So you just explained it much better than the TensorFlow extended landing page does.
[2071.46 --> 2073.32]  That was a really good explanation.
[2073.32 --> 2088.52]  Thanks. Well, I mean, we were just talking before we started recording about how I am very in the mindset of Kelsey Hightower's philosophy of good developers copy and great developers paste.
[2089.20 --> 2095.76]  And so a lot of that that's in my mind stuck there is from the talk that was given at the Dev Summit about TensorFlow extended.
[2095.92 --> 2102.04]  And he walks through in much more detail, of course, about these components and how they're kind of fit together in pipeline.
[2102.04 --> 2108.68]  So if you're interested in that and hearing kind of more depth around that, it was a good talk.
[2109.10 --> 2123.66]  One of the things that really stood out to me, though, and is in line with a lot of different platforms that are out right now, including things like Packaderm and Domino and even Floyd Hub and other things are this idea of lineage tracking.
[2123.82 --> 2130.66]  And so utilizing the metadata that you're getting off of these components to actually track how many times have you run training?
[2130.66 --> 2143.68]  And when you ran that training, what was the graph of kind of loss per iteration and like all of these sorts of things kind of allowing you to trace back what component did what, when, how.
[2143.68 --> 2158.12]  One of the other things, I guess, you know, keeping in line with practicalities and also keeping in line with the various things that you might want to do with models, including doing this pipelining.
[2158.28 --> 2161.34]  But then once you train a model, where does it end up?
[2161.58 --> 2166.80]  And so they talked about a couple of things as far as where that model might end up.
[2166.88 --> 2169.06]  One of those was TensorFlow Lite.
[2169.46 --> 2171.68]  Another was TensorFlow for JavaScript.
[2171.68 --> 2185.26]  And so there was a lot of talk about kind of shifting and pushing models to low power devices, kind of embedded devices and mobile devices or even in the browser.
[2185.50 --> 2192.44]  And that seems to be kind of following a trend that's been going on for some time about porting models to these sorts of devices.
[2192.44 --> 2205.56]  Yeah, I know in my own experience, we've targeted both mobile and IoT at a couple of different companies a lot and being able to push inference out as far out to the edge as possible due to all sorts of different constraints.
[2205.56 --> 2211.94]  So I think TensorFlow Lite is, I mean, it's been around, but it's such a key part of the ecosystem.
[2212.80 --> 2221.22]  And we're also, you know, if you had asked me a few years ago about JavaScript, and I say this as someone who does JavaScript separate from deep learning,
[2221.38 --> 2226.06]  I have been pleasantly surprised to see it working so well in the JavaScript world.
[2226.06 --> 2234.42]  And I had a, we may have an upcoming interview at some point here with someone who has done some work on TensorFlow for JavaScript.
[2234.76 --> 2239.42]  So I think being able to push it out to all these different targets is pretty crucial.
[2239.60 --> 2242.20]  One that we haven't mentioned yet was also Swift for TensorFlow.
[2242.20 --> 2248.28]  And so I think if you take these, all these last few things we've talked about kind of in combination,
[2248.28 --> 2260.26]  I think that may be the single biggest strength for TensorFlow is that the ecosystem is, is made operationalizing and pushing to various production targets.
[2260.26 --> 2261.36]  It's been thought out.
[2261.44 --> 2262.80]  They have a standard way of doing it.
[2262.82 --> 2265.46]  And there are these different approaches that are targeting those.
[2265.46 --> 2270.76]  And I haven't seen that at that level of sophistication from some of the other frameworks yet.
[2270.76 --> 2271.78]  And that may be coming.
[2272.34 --> 2277.06]  But if there's anything I think that will keep TensorFlow up there as one of the dominant frameworks,
[2277.16 --> 2281.24]  it's the fact that they've thought about the operational side to such an extensive, you know, degree.
[2281.90 --> 2288.10]  Yeah, on the operational side and kind of the building side, as a tinkerer, they also announced a couple of cool things.
[2288.10 --> 2297.14]  For a while, I've been a fan of the Movidius NCS USB sticks from Movidius, which is part of Intel now,
[2297.14 --> 2303.92]  which basically allows you to it's kind of like a USB drive that you plug into your computer.
[2304.20 --> 2315.94]  And it has a specialized hardware chip in the USB stick that allows you to run inference on things like, you know, a Raspberry Pi or something like that.
[2315.94 --> 2326.92]  So Google seems to be hopping on this bandwagon as well and doing some interesting things with this so-called Edge TPU, which seems to be a similar idea.
[2327.06 --> 2335.20]  So it's like a version of the TPU that's meant to be run on these sort of embedded devices or like a single board computer sort of things.
[2335.20 --> 2346.26]  And so this project is called Coral and they released a dev board, which is kind of like a Raspberry Pi profile board where you can have one of these chips embedded in there.
[2346.38 --> 2351.34]  And there's also a USB accelerator as well, similar to the Movidius NCS.
[2351.44 --> 2356.54]  Although I guess this one has a USB-C interface, so that might be nice.
[2356.68 --> 2359.38]  But yeah, I think these things are just like tons of fun.
[2359.38 --> 2369.96]  Like it's super fun to grab one of these USB sticks and then create like a little smart camera or something that classifies people at your front door.
[2370.16 --> 2371.66]  You know, like fun projects like that.
[2371.72 --> 2376.66]  It just makes them accessible and, you know, really enjoyable.
[2376.66 --> 2379.48]  So I appreciate them coming out with things like that.
[2379.48 --> 2381.66]  And there's more and more of those things coming out in general.
[2382.12 --> 2385.80]  Yeah, I've seen and, you know, the ability to prototype quickly.
[2386.28 --> 2387.80]  These really accelerate that.
[2387.80 --> 2402.06]  So one of the places I've seen certainly the Movidius sticks and now as we look at Coral going forward is companies having an idea and somebody says, you know, I'm just going to take a few hours and mess around and see what I think about that.
[2402.24 --> 2409.78]  And they can just try it at a really low cost and they don't have to be necessarily hooked up to a big infrastructure and have all that plumbing worked out.
[2409.78 --> 2416.30]  And then, you know, they can kind of, you know, quickly figure out whether something is worth pursuing further or not.
[2416.30 --> 2420.08]  And I've seen that done many, many times with these small pluggable units.
[2420.70 --> 2420.80]  Yep.
[2420.90 --> 2428.24]  And maybe you are the type of person that's saying right now, oh, I want to experiment with TensorFlow 2.0.
[2428.34 --> 2433.64]  I want to experiment with some of these new kind of bolt on things and learn more.
[2433.82 --> 2436.74]  Well, we have some resources for you.
[2436.74 --> 2447.24]  Whenever we do one of these fully connected episodes, we like to end by providing some useful, practical resources for people to get hands on, dive in, learn more about the topic.
[2447.50 --> 2455.38]  And thankfully, some of these resources for TensorFlow 2.0 and other things were announced at the Dev Summit.
[2455.78 --> 2461.18]  So one of those was a TensorFlow 2.0 course from deeplearning.ai.
[2461.30 --> 2463.22]  I think it's a TensorFlow 2.0 course, right?
[2463.22 --> 2464.10]  It is.
[2464.28 --> 2470.14]  And they have, I think it's a specialization where they are going to have four courses total.
[2470.36 --> 2474.74]  And I believe as we are recording this, they've had the first one out for a while.
[2474.92 --> 2475.64]  And I went through it.
[2475.68 --> 2476.08]  It was good.
[2476.16 --> 2477.32]  It's a very good course.
[2477.76 --> 2483.34]  And they announced that the second one was available in the last week or so, as I say this right now.
[2483.70 --> 2487.66]  So the deeplearning.ai version is halfway out there.
[2487.66 --> 2495.18]  So it's certainly, you know, by the, if you jump into it now, by the time you get through that and into the second one, probably the third one will be out as well.
[2495.62 --> 2495.74]  Yeah.
[2495.84 --> 2500.14]  They're also, I mean, I love a lot of the stuff that's come out of Fast.ai.
[2500.14 --> 2511.76]  And Fast.ai is kind of embracing the Swift aspect of TensorFlow and is integrating Swift for TensorFlow into one of their latest courses.
[2512.06 --> 2518.72]  If you're into Fast.ai or have used some of their stuff before, that might be a great place to start from that too.
[2518.94 --> 2520.58]  I don't know anything about Swift.
[2520.78 --> 2523.50]  So I think that it might be an interesting one for me.
[2523.96 --> 2524.44]  Sounds good.
[2524.44 --> 2534.72]  I know another one of the key educational things that they talked about in addition to deeplearning.ai was Udacity has a TensorFlow 2.0 course.
[2535.00 --> 2536.06]  I have not tried that one.
[2536.44 --> 2537.42]  So that's coming up.
[2537.46 --> 2538.64]  I'd like to dive into that one.
[2539.04 --> 2541.22]  But that's also out there as well.
[2541.32 --> 2543.56]  And both of those were announced at the Dev Summit.
[2543.56 --> 2544.20]  Yeah.
[2544.38 --> 2555.00]  And if you haven't been able to get a spot at the Dev Summit one of these past years, it is kind of limited in how many people can go and all of that stuff.
[2555.12 --> 2557.40]  And that's kind of unfortunate that it has to be that way.
[2557.84 --> 2566.20]  But they did announce that in collaboration with O'Reilly, they are starting a TensorFlow World conference.
[2566.20 --> 2568.62]  So the conference name is TensorFlow World.
[2569.08 --> 2575.56]  And so this is a conference that if, you know, for whatever reason, you can't come to the Dev Summit.
[2575.74 --> 2589.94]  And I think it's more meant to be a community conference that you can come to this TensorFlow World conference where you can learn about use cases of people using TensorFlow, go through some tutorials, hear from the TensorFlow team as well.
[2590.08 --> 2591.38]  But it sounds pretty cool.
[2591.60 --> 2592.48]  I would love to check it out.
[2592.54 --> 2595.38]  And I think also this is an opportunity as well.
[2595.38 --> 2602.76]  If you're doing something with TensorFlow, you can submit proposals or submit talks to the conference as well.
[2603.18 --> 2605.68]  Well, yeah, the call for speakers just closed last week.
[2605.80 --> 2606.44]  Oh, sorry.
[2606.58 --> 2607.96]  We didn't get to you in time.
[2608.12 --> 2613.90]  But I'm sure that if you were in the world and you're doing that TensorFlow stuff, you probably already knew.
[2614.22 --> 2621.10]  But you'll still have the opportunity to participate in tutorials and go for the great talks and all of that stuff.
[2621.22 --> 2622.56]  So definitely check that out.
[2622.56 --> 2624.66]  And I was really thinking about it.
[2624.68 --> 2627.80]  And then I realized the date got by me before I realized that it closed.
[2627.90 --> 2629.94]  So it closed on April 23rd.
[2630.08 --> 2630.64]  Things happen.
[2630.86 --> 2632.12]  So yeah, things happen.
[2632.30 --> 2633.04]  It's life.
[2633.18 --> 2633.32]  Yeah.
[2633.40 --> 2634.22]  Don't miss it.
[2634.30 --> 2638.78]  The deadlines for EMNLP and other things are coming up, too.
[2639.04 --> 2642.98]  I don't know when the deadline for NeurIPS is, but some of those are coming up.
[2642.98 --> 2649.64]  So if you're doing cool AI stuff on the research side, don't forget about your deadlines and make sure and get your papers on.
[2650.10 --> 2650.50]  There you go.
[2650.78 --> 2654.68]  And I'll close out saying I am seriously considering going to TensorFlow World.
[2654.86 --> 2656.28]  So I'm going to explore that a little bit.
[2656.52 --> 2663.24]  And I'm excited to see that the community is big enough to be able to support a conference unto itself now.
[2663.60 --> 2664.04]  For sure.
[2664.04 --> 2667.12]  And thanks for suggesting this topic, Chris.
[2667.26 --> 2670.70]  I had a great time kind of going through some of these things for you.
[2670.76 --> 2675.38]  And like I say to our listeners, please engage with us on Slack or on LinkedIn.
[2675.94 --> 2679.56]  Let us know your thoughts about TensorFlow 2.0.
[2679.74 --> 2682.34]  We're excited to hear your thoughts and see what you build.
[2682.94 --> 2683.76]  Yep, absolutely.
[2683.90 --> 2688.32]  Looking forward to diving in myself and hearing from our listeners on what they're doing with it.
[2688.48 --> 2691.66]  So I guess until next time, I'll talk to you later, Daniel.
[2691.92 --> 2692.14]  All right.
[2692.18 --> 2692.40]  Bye-bye.
[2692.68 --> 2693.02]  Bye-bye.
[2693.02 --> 2693.06]  Bye-bye.
[2694.04 --> 2696.04]  All right.
[2696.08 --> 2698.72]  Thank you for tuning into this episode of Practical AI.
[2698.96 --> 2700.44]  If you enjoyed this show, do us a favor.
[2700.56 --> 2701.90]  Go on iTunes and give us a rating.
[2702.20 --> 2704.08]  Go in your podcast app and favorite it.
[2704.14 --> 2706.90]  If you are on Twitter or social network, share a link with a friend.
[2706.96 --> 2709.30]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2709.60 --> 2712.28]  And bandwidth for Changelog is provided by Fastly.
[2712.28 --> 2713.84]  Learn more at Fastly.com.
[2714.04 --> 2717.24]  And we catch our errors before our users do here at Changelog because of Rollbar.
[2717.44 --> 2719.86]  Check them out at Rollbar.com slash Changelog.
[2720.16 --> 2722.66]  And we're hosted on Linode cloud servers.
[2722.66 --> 2724.64]  Head to Leno.com slash Changelog.
[2724.72 --> 2725.18]  Check them out.
[2725.24 --> 2726.08]  Support this show.
[2726.42 --> 2729.66]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2730.12 --> 2732.20]  The music is by Breakmaster Cylinder.
[2732.62 --> 2736.02]  And you can find more shows just like this at Changelog.com.
[2736.02 --> 2738.16]  When you go there, pop in your email address.
[2738.16 --> 2744.48]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2744.62 --> 2745.66]  Thanks for tuning in.
[2745.78 --> 2746.60]  We'll see you next week.
[2746.60 --> 2763.46]  Because you've listened all the way to the end of the show, got a little preview here for you of our upcoming podcast called Brain Science.
[2763.46 --> 2772.30]  This podcast is for the curious that explores the inner workings of the human brain to understand behavior change, how about formation, mental health, and the human condition.
[2772.66 --> 2779.00]  This show is hosted by myself, Adam Stachowiak, and my good friend, Mariel Reese, a doctor in clinical psychology.
[2779.44 --> 2780.60]  It's brain science applied.
[2780.68 --> 2784.80]  Not just how does the brain work, but how do we apply what we know about the brain to better our lives?
[2785.36 --> 2785.78]  Here we go.
[2785.78 --> 2791.60]  That applied brain science really stood out to me because I don't want it to just be data.
[2791.98 --> 2793.64]  I want you to go, how can this fit?
[2793.76 --> 2794.64]  What can I take away?
[2794.96 --> 2796.32]  Now how am I going to change?
[2796.70 --> 2807.04]  And that that sort of is where you come in more and even some of the questions like, so like I want to ask you, what are some of the most challenging things working in the tech world when it comes to relationships?
[2807.52 --> 2809.58]  Probably the most important one is isolation.
[2809.58 --> 2816.96]  More and more of the world and companies are being, for good reasons, they're being okay with what they call distributed teams.
[2817.40 --> 2817.52]  Yeah.
[2817.62 --> 2821.80]  And that means that you and I, we work for the same company, but you work from your home office.
[2821.86 --> 2822.90]  I work for my home office.
[2823.40 --> 2837.32]  I might go into the office a couple of times a week if I live local, but even if I live in San Francisco, I'm still probably a remote worker, even though I can hop in an Uber or hop on, you know, the train or whatever and go into the office and be there in a half hour.
[2837.32 --> 2838.34]  But why waste the time?
[2838.34 --> 2851.70]  You know, and this is where I would revisit what I want to talk about with resonance and that whenever we're learning, no matter what thing, it's really helpful when we get feedback that's both immediate and specific.
[2851.70 --> 2859.66]  And so when you're by yourself and you don't have any interaction with other people, how can you get any feedback?
[2860.14 --> 2870.12]  I mean, you're losing most of the nonverbal communication and you also don't have all of the voice inflections or facial expression.
[2870.58 --> 2875.70]  Have you ever tried to, you know, be sad, feel sad and smile at the same time?
[2875.70 --> 2876.78]  Try it.
[2877.98 --> 2879.46]  It's pretty hard.
[2879.88 --> 2880.36]  Right.
[2880.44 --> 2887.56]  Because facial expression is exactly what's involved when it comes to empathy, which is relationships.
[2887.56 --> 2898.56]  I was reading a research article recently and it talked about, you know, how couples who are together a really long time end up sort of looking like each other.
[2899.42 --> 2900.14]  Remember what that's?
[2900.82 --> 2901.10]  Yeah.
[2901.10 --> 2909.84]  And so what they've looked at is when we actually empathize with other people, facial expression is really key within that.
[2910.42 --> 2922.08]  And so when you empathize with the partner you're with over and over and over again, your face begins to make the same creases and facial expression as it relates to where somebody else is emotionally.
[2922.46 --> 2923.02]  Wow.
[2923.32 --> 2923.68]  Right?
[2923.68 --> 2926.04]  So that's beefy.
[2927.04 --> 2934.68]  Well, again, this is sort of the hotbed when it comes to neuroscience these days is mirror neurons.
[2935.26 --> 2938.86]  And these mirror neurons are what are involved with empathy.
[2939.16 --> 2944.08]  And so mirroring, meaning I get another person's emotional world.
[2945.04 --> 2948.98]  And so one of the research studies looked at Botox.
[2948.98 --> 2957.24]  And what they found is that Botox, because it actually assists in paralyzing facial muscles.
[2957.40 --> 2957.68]  Right.
[2957.78 --> 2960.88]  But then you can't contort your face so you don't get wrinkles.
[2961.36 --> 2964.08]  But actually levels of empathy go down.
[2964.74 --> 2965.26]  Uh-uh.
[2965.92 --> 2966.52]  Right.
[2966.72 --> 2969.48]  Because your physical appearance can't reflect your inner appearance.
[2969.94 --> 2971.46]  Yeah, you got it.
[2971.46 --> 2978.14]  And so when you're working in these remote locations, it might facilitate better work or more focus.
[2978.14 --> 2984.10]  And it allows people to be distributed and to capitalize on the talents across the country.
[2984.16 --> 2984.40]  Right?
[2984.96 --> 2985.26]  Yeah.
[2985.52 --> 2985.84]  Wow.
[2985.96 --> 2988.42]  So that's like a treasure trove, in my opinion.
[2988.88 --> 2994.10]  Talking about in a scientific way, you know, not just like, hey, this is my opinion.
[2994.20 --> 2994.64]  Yeah.
[2994.64 --> 2996.28]  About all the cons of that.
[2996.28 --> 3001.22]  Because I think what we can do is still have remote work, but do it in more healthy ways.
[3001.60 --> 3006.28]  Because I'm fully, I mean, I've been self-employed remote worker since 2006.
[3006.80 --> 3008.04]  Now I'm a unique animal.
[3008.44 --> 3009.58]  I know that.
[3009.70 --> 3010.72]  My wife knows that.
[3010.92 --> 3011.36]  Right.
[3011.38 --> 3012.26]  And I'm fine with it.
[3012.54 --> 3014.56]  I'm a good human being, but I've got some flaws.
[3014.76 --> 3017.54]  And I'm willing to accept and share those to some degree.
[3017.54 --> 3025.90]  And I think the problem is we just lack maybe a more purposeful or intentional feedback loop.
[3026.02 --> 3026.40]  Yeah.
[3026.56 --> 3032.66]  Which I think is super important to being able to operate in this world in just good ways.
[3032.76 --> 3037.44]  I don't know, healthy ways is probably the best way to use in this show context is healthy ways.
[3038.14 --> 3042.02]  One of the things that's fundamental, I would say, to being human is change.
[3042.02 --> 3042.82]  Right.
[3042.92 --> 3049.00]  And so sometimes people come in and are really key in our life for a period of time.
[3049.00 --> 3050.04]  And then things change.
[3050.04 --> 3054.32]  Either we grow or they grow or they change in a different direction.
[3054.32 --> 3059.86]  And then the relationship changes or that feedback loop gets modified in some way.
[3059.94 --> 3061.70]  That isn't always a bad thing.
[3062.20 --> 3070.40]  It's just going, my sense of choice actually is a critical component when it comes to feeling good about my life.
[3070.40 --> 3089.88]  If I feel like everything is sort of outside of me and I don't have any charge over it, like I didn't choose to work in a more remote location or I didn't choose to go to school or I didn't choose this person, then it feels far more oppressive as opposed to I actually participated in the outcome that I'm actually experiencing.
[3090.50 --> 3095.22]  So I then also have more charge over whether or not I want to change it.
[3095.22 --> 3103.68]  I think this feedback loop process that we're talking about here is super common to developers.
[3104.32 --> 3111.90]  You know, from people who write code to people who plan and to engineer and to manage and lead.
[3112.12 --> 3115.92]  Like there's no one in the software process that doesn't understand the feedback loop.
[3115.92 --> 3136.94]  And the reason why is because in product development, they have this concept of agile and basically it means you produce something, you put it out there and you expect the feedback loop to happen in order to gain insights and course correction to then release another version of it that continually and iteratively becomes more and more improved.
[3136.94 --> 3141.80]  So this whole process in day-to-day work in software is normal.
[3142.80 --> 3150.38]  And I think it's interesting how we're going to apply to their lives and people's lives, you know, to take the same importance of a feedback loop, for example, and apply it.
[3150.74 --> 3150.86]  Right.
[3151.04 --> 3158.94]  Well, so this is very much how it goes in relationship, which is why there is an importance when it comes to sort of things resonating.
[3158.94 --> 3165.78]  You ever walk into a room or an interaction with a couple other people and like something just feels wonky or off?
[3166.14 --> 3168.88]  You're like, I can't put my finger on it.
[3169.02 --> 3170.08]  Definitely been there.
[3170.64 --> 3171.20]  Right.
[3171.82 --> 3184.16]  Well, and so to be able to identify that in relationships and even go, wow, I need to, I'm experiencing this person in my world with the limited interactions that I have with them.
[3184.16 --> 3186.42]  It hasn't really resonated with me.
[3186.64 --> 3188.44]  And so I don't get good feedback.
[3188.84 --> 3194.26]  So now I'm going to be more defensive because I feel as though there's a threat.
[3194.44 --> 3196.68]  It doesn't necessarily mean the person is threatening.
[3196.82 --> 3200.18]  However, my brain is going to tell me, hey, we need to be more protective.
[3200.60 --> 3204.92]  We need to do some strategies so that you're not fully exposed.
[3204.92 --> 3220.74]  You know, one way I look at scenarios like this, I would say as of late is because if you ever watched a TV show or a movie where the, you know, the narration, the storytelling part of it, they expose a character in a certain light.
[3220.96 --> 3223.22]  And you may dislike that.
[3223.30 --> 3224.82]  They may be a villain or villainess.
[3225.08 --> 3225.32]  Right.
[3225.68 --> 3226.00]  Sure.
[3226.00 --> 3238.02]  But the moment they turn the story to their backstory and why they are the way they are or why they're acting the way they're acting, you then kind of fall in love with them and you're almost rooting for them.
[3238.16 --> 3238.46]  Right.
[3238.52 --> 3253.10]  I feel like that's the same thing that happens day to day to our lives is that, you know, there are people who seem villainous or not for us, but we don't understand their backstory and why they are the way they are for us to have and employ that empathy.
[3253.10 --> 3265.04]  That's required to have this, this dance, as you say, this iteration of relationship, you know, we, we just assume they are who they are and we project, you know, our worst fears onto them and they become true.
[3265.86 --> 3267.32]  Yes, you got it.
[3267.40 --> 3279.46]  This is why in the absence of, you know, a face, I don't really get to engage with people in the same sort of humanness that we are all in.
[3279.46 --> 3281.48]  And so you're exactly right.
[3281.62 --> 3287.70]  I mean, over and over and over again, because you can identify and go, oh, that's why they're harsh.
[3287.70 --> 3296.76]  Or, you know, I recently had an interaction I had shared with someone that I, I was a competitive gymnastics coach for a number of years.
[3296.76 --> 3307.14]  And so somebody thought that my response to them when they were really struggling was kind of harsh, but they remembered that I had told them I was a coach for so long.
[3307.14 --> 3311.18]  And they're like, oh, this is just another side of her coming out.
[3311.30 --> 3311.58]  Right.
[3311.74 --> 3314.74]  And I'm not sure I prefer it, but I get it.
[3314.80 --> 3320.06]  And then it switched for their reaction because then they're like, oh, wait, we're on the same team.
[3320.94 --> 3324.70]  She's not trying to like oppress me or fight back against me.
[3324.78 --> 3328.30]  She actually is helping me, trying to get me to where I want to go.
[3328.30 --> 3332.30]  My wife and I, we've learned this, this concept of goodwill, right?
[3332.46 --> 3332.70]  Yeah.
[3332.86 --> 3337.80]  I can take your feedback or your criticisms in a different light.
[3337.88 --> 3341.08]  If, if I know that you have goodwill for me.
[3341.12 --> 3341.52]  Yep.
[3341.64 --> 3345.72]  Meaning that you're not trying to harm me, that you are for me, not against me.
[3345.72 --> 3349.62]  And sometimes change, as we all know, is painful and can be painful.
[3349.62 --> 3356.00]  So sometimes the necessary feedback and or criticism that can influence that change can also be painful.
[3356.26 --> 3364.66]  But I can accept it differently if I know that she or they or whomever is in the scenario with me has goodwill for me.
[3364.94 --> 3369.18]  You know, whereas if you know that they're not for you, then you obviously take it a whole different way.
[3369.22 --> 3371.64]  And that's, that's an okay thing.
[3371.64 --> 3379.46]  But we often are, you know, in relationship with people that are giving us crucial feedback and we need to have that kind of, that lens.
[3379.56 --> 3384.48]  Like it was significant in our marriage to understand, hey, I know there are times when you give me feedback.
[3384.48 --> 3388.66]  I am not happy about it, but, but I know you have goodwill for me.
[3388.72 --> 3390.94]  So therefore I calm down.
[3390.94 --> 3391.86]  I listen.
[3392.92 --> 3401.46]  I, you know, I take that in and I process it, whatever, but I take it in a different way because I know that she's for me and not against me.
[3401.64 --> 3402.12]  Yep.
[3402.44 --> 3423.18]  One of the key things when it comes to change is a sense of openness and even relationally, like of going, I need to be able to see some, how somebody else responds or how they're feeling as based on their perspective of what they're going through and not just my perspective of their perspective.
[3423.18 --> 3431.32]  And so this goodwill is like, I believe that we're on the same side and that you're not trying to make it harder for me.
[3431.42 --> 3437.94]  But so I can understand if I were sitting where you were sitting, had the background that you had, why you would have taken it in that way.
[3437.94 --> 3445.50]  And then I can provide an opportunity to clarify or create more connection, even when it doesn't feel good.
[3445.50 --> 3451.86]  And I, I honestly think this is so much of what's missing in people's relationships.
[3451.86 --> 3472.66]  If I look at relational interactions through, uh, the notion of conditioning, wherein I get a sort of hit of dopamine, feel good feelings, because I went to a person, I had a conversation that didn't necessarily feel good, but there was openness on both parties to hear one another's perspective.
[3472.66 --> 3480.90]  That it actually then reinforces like, oh, when I go and I have this exchange with people, I feel better.
[3481.54 --> 3491.32]  So now I'm going to go and engage with other people and get the feedback, even if I might not like the feedback, because now I'm buffered and I'm not alone in this.
[3491.32 --> 3493.62]  And I, somebody else sees my world.
[3495.76 --> 3497.76]  That's a preview of brain science.
[3497.76 --> 3505.32]  If you love where we're going with this, send us an email to get on the list, to be notified the very moment this show gets released.
[3505.64 --> 3513.46]  Email us at editors at changelaw.com in the subject line, put in all caps, brain science with a couple bangs.
[3513.46 --> 3519.10]  If you're really excited, you can also subscribe to our master feed to get all of our shows in one single feed.
[3519.10 --> 3525.02]  Head to changelaw.com slash master or search in your podcast app for change all master.
[3525.02 --> 3532.34]  You'll find it subscribe, get all of our shows and even those that only hit the master feed again, changelaw.com slash master.
[3532.34 --> 3536.44]  You'll find out more.
[3541.08 --> 3542.20]  And finally,czne degree in the podcast.
[3542.20 --> 3543.40]  We don't know.
[3548.30 --> 3557.80]  You'll find the Bradley for the Western Professor.
[3557.80 --> 3558.30]  Thanks, Dan.
[3558.56 --> 3561.72]  For now,וכ Chicagoéré got to learn more.
[3561.72 --> 3561.78]  You'll follow us a little bit.
