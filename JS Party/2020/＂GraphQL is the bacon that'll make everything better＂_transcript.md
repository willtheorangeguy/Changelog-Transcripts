[0.00 --> 3.66]  Once again, GraphQL is the bacon that's going to make everything better.
[3.88 --> 7.80]  But if you're not careful, you'll get a little bit bloated if you have too much bacon.
[11.46 --> 14.20]  Bandwidth for Changelog is provided by Fastly.
[14.58 --> 16.46]  Learn more at Fastly.com.
[16.70 --> 19.78]  We move fast and fix things here at Changelog because of Rollbar.
[19.92 --> 21.60]  Check them out at Rollbar.com.
[21.84 --> 24.02]  And we're hosted on Linode cloud servers.
[24.36 --> 26.36]  Head to Linode.com slash Changelog.
[26.36 --> 30.36]  This episode is brought to you by Rollbar.
[30.70 --> 32.46]  Move fast and fix things.
[32.74 --> 34.84]  Resolve errors and minutes and deploy with confidence.
[35.40 --> 37.68]  Head to Rollbar.com slash Changelog.
[37.76 --> 38.56]  Request a demo.
[38.72 --> 39.60]  Get started today.
[40.04 --> 42.24]  It's loved by developers, trusted by enterprises.
[42.80 --> 45.26]  And most of all, we use it here at Changelog.
[45.62 --> 48.28]  Move fast and fix things with Rollbar.
[48.74 --> 51.54]  Once again, Rollbar.com slash Changelog.
[56.36 --> 67.00]  Welcome to JS Party, your weekly celebration of JavaScript and the web.
[67.34 --> 69.50]  We have some great shows coming down the pipeline.
[70.12 --> 73.36]  Next week, we're discussing the framework wars with a focus on Vue.js.
[73.84 --> 77.62]  Then Michael Rogers is back to share his journey migrating to ES modules.
[78.02 --> 80.90]  After that, we're talking Node best practices with Yoni Goldberg.
[80.90 --> 84.62]  But right now, it's time for a serving of GraphQL that's heavy on the metaphors.
[84.74 --> 86.10]  Hey, it's party time.
[86.36 --> 102.90]  Hello and welcome to JS Party.
[103.20 --> 103.84]  This is K-Ball.
[103.92 --> 105.28]  I'll be your emcee this week.
[105.38 --> 107.50]  I'm so excited to be back on the show.
[107.64 --> 110.34]  And these guys miss me so much, they let me run things today.
[110.34 --> 115.60]  I am joined by the one and only Jared Santo.
[115.60 --> 116.88]  So, Jared, how are you doing?
[117.10 --> 117.70]  Shaboy!
[118.04 --> 118.74]  What's up, man?
[118.78 --> 119.56]  Good to have you back.
[120.14 --> 120.62]  Yeah, yeah.
[120.82 --> 122.00]  And Nick Neesey.
[122.44 --> 123.00]  Hoi hoi.
[123.08 --> 123.62]  Welcome back.
[123.74 --> 124.34]  Hoi hoi.
[124.82 --> 127.10]  I cannot tell you how much I've missed that hoi hoi.
[127.54 --> 128.28]  All right.
[128.64 --> 132.86]  So, today, y'all are going to indulge me and talk about something that I have been digging
[132.86 --> 137.98]  into quite a bit over the last three to six months, both while I was gone, but even some
[137.98 --> 140.80]  before that, which is the subject of GraphQL.
[140.80 --> 145.92]  And I think, from what I was hearing, y'all have different levels of experience.
[146.34 --> 150.46]  So, obviously, I'm going to pick on you a lot and make you explain things so that we
[150.46 --> 152.66]  get that played out in front of everybody.
[152.84 --> 156.08]  But let's start with just kind of describing what is GraphQL.
[156.34 --> 159.62]  And I actually want to hear everybody's answers starting from the least knowledgeable.
[160.18 --> 162.78]  So, Jared, you said you had only played a tiny, tiny bit.
[162.92 --> 163.54]  How dare you?
[163.62 --> 165.14]  From your perspective, what is GraphQL?
[165.14 --> 168.90]  Yeah, so I've talked about it a lot, but I haven't used it a lot.
[169.22 --> 173.26]  Most of my experience with GraphQL is toying with it with the GitHub API.
[174.04 --> 177.14]  And so, I can tell you what I think GraphQL is as a noob.
[177.26 --> 187.00]  And that would be an API architecture wherein the API clients are allowed to craft queries
[187.00 --> 193.82]  and mutations according to what's been laid out by the API provider and can put together
[193.82 --> 199.14]  the exact data they require to suck down into their little API clients.
[199.32 --> 202.40]  There's probably more to it than that, but that's my noob description.
[202.76 --> 203.08]  How'd I do?
[203.50 --> 204.22]  Not too bad.
[204.50 --> 207.42]  Nick, do you want to add or amend anything on that?
[207.86 --> 208.16]  Yeah.
[208.16 --> 214.58]  So, previously I've used libraries like D3 and Chart.js to make these graphs, but this
[214.58 --> 218.32]  is the next iteration on that, a full language to create awesome graphing.
[219.78 --> 221.24]  Quick libraries.
[222.92 --> 226.78]  Yeah, I think that that kind of goes to my understanding of it.
[226.86 --> 231.86]  It's all schema-driven and type-safe, so the queries know exactly what they can pull and
[231.86 --> 234.80]  exactly what they will get back, which is pretty cool.
[234.80 --> 240.52]  And as opposed to something like REST, where you have specific endpoints to fetch things
[240.52 --> 246.44]  from, you kind of just have a grab bag endpoint where you can just say, this is what I want,
[246.64 --> 250.96]  this is all of the properties that I specifically want on that, and then you can have relationships
[250.96 --> 251.72]  between that.
[251.90 --> 255.74]  So, one example that I always think of is pulling a tweet.
[256.20 --> 260.08]  You can grab the tweet, but then you can say, I also want the number of likes that it
[260.08 --> 264.44]  has, and then I also want the replies to that, which would be other tweets that are all
[264.44 --> 269.74]  related to that top tweet, which may or may not be correct, but that's the way I at least
[269.74 --> 270.86]  think about it in my mind.
[271.66 --> 272.94]  How does this metaphor apply, Gabe?
[273.04 --> 275.96]  Also, the server metaphor, you're at a restaurant, right?
[276.00 --> 278.18]  An API, think of it like serving up stuff, you know?
[278.68 --> 283.44]  So, a REST API where you have endpoints that Nick just described, this would be like where
[283.44 --> 286.14]  your waiter comes and they're like, here, here's the menu, right?
[286.22 --> 287.28]  What would you like to order?
[287.80 --> 289.08]  And you say, I'll take a hamburger.
[289.28 --> 290.76]  And they say, okay, I'll go get you a hamburger.
[290.76 --> 291.44]  They send it back.
[292.06 --> 295.84]  Whereas, maybe a GraphQL API is more like an open buffet where it's like, here's all
[295.84 --> 296.52]  of our food.
[297.08 --> 298.30]  You know what's in front of you.
[298.56 --> 299.56]  Pick and choose what you want.
[299.80 --> 302.10]  Make your plate and take it back to your table.
[302.36 --> 302.50]  No?
[302.88 --> 304.98]  That doesn't sound good in these times, at least.
[306.90 --> 309.38]  That would, yeah, make GraphQL very contagious.
[309.60 --> 309.92]  Dangerous.
[310.42 --> 310.78]  Dangerous.
[311.10 --> 311.46]  Dangerous.
[312.10 --> 312.32]  Yeah.
[312.42 --> 315.14]  I mean, I feel like you two have summed it up pretty well.
[315.24 --> 316.30]  I'm not sure I dig the metaphor.
[316.30 --> 321.34]  But one of the layers that I would put on top of that is, if you think about a REST
[321.34 --> 324.26]  API, everything is centered around resources.
[325.06 --> 327.94]  And each resource has its own place that you go and get it.
[328.32 --> 332.32]  But if there are relationships between those resources, you have to, on the client side,
[333.10 --> 338.04]  understand those relationships and go and fetch the pieces that you want.
[338.98 --> 343.34]  GraphQL starts from also having a whole set of resources.
[343.34 --> 347.22]  That's the schema that you're talking about, the schema-driven nature of it.
[347.70 --> 351.00]  But it maps out the connections between those resources.
[351.38 --> 358.48]  So that anytime you are accessing one resource, you can specify all the graph of relationships
[358.48 --> 360.14]  you want to follow down and pull data from.
[360.72 --> 368.00]  And then the other piece, in terms of having the single place to go, it is one location,
[368.00 --> 368.54]  one endpoint.
[368.74 --> 377.06]  But there's this set of top-level queries that you can run where the API provider still
[377.06 --> 382.04]  gets to define what are the ways into my buffet, so to speak.
[382.20 --> 383.82]  Oh, I knew it was coming back around.
[383.96 --> 386.80]  See, you actually do like this metaphor the more you think about it.
[386.86 --> 387.64]  Keep going, please.
[388.28 --> 389.76]  Oh, I'll play with anything you give me.
[389.90 --> 390.46]  You know that.
[390.46 --> 397.04]  But you can't necessarily grab at the top-level every resource that you might want to access.
[397.22 --> 401.90]  Some resources might only be accessible within the context of another resource.
[403.12 --> 406.70]  And the options that you have available are those top-level queries.
[406.84 --> 413.22]  So you can think of everything within GraphQL that you're querying as a graph that starts
[413.22 --> 415.32]  with a single node at the top, which is a query.
[415.32 --> 421.32]  So query is the top, and then it steps down a relationship to, here's a set of queries
[421.32 --> 421.86]  that are available.
[422.04 --> 424.58]  Maybe, let's use the GitHub API as an example.
[425.16 --> 431.96]  If we look at the GitHub API, what are the queries for public schema that's available?
[432.98 --> 434.44]  GraphQL API queries.
[435.26 --> 437.38]  Like the first one that it lists is marketplace listings.
[437.84 --> 443.50]  So that would be one hop down that's going to give you a set of listings in the marketplace.
[443.50 --> 446.30]  Does that have any relationships?
[446.42 --> 447.68]  That actually doesn't have relationships.
[448.16 --> 454.30]  But from that, you can kind of hop down and ask for the sets of things that you would want
[454.30 --> 455.20]  from that query.
[455.86 --> 458.08]  So say we were doing your buffet query.
[458.66 --> 465.86]  You might say that you can only start with pancakes or eggs.
[466.14 --> 467.52]  And those are the top-level things.
[467.56 --> 469.02]  You can't just get bacon on its own.
[469.12 --> 469.78]  Some breakfast buffet?
[469.78 --> 473.86]  But you could get eggs with a relationship to bacon, or you could get pancakes in a relationship
[473.86 --> 474.56]  to bacon, right?
[474.60 --> 479.56]  Like you have these sort of entrees into the API that you can start with, and then you
[479.56 --> 481.80]  can follow down the relationships as far as you go.
[482.88 --> 485.12]  What kind of buffet doesn't have bacon as a top-level entry?
[485.28 --> 485.60]  Come on.
[486.06 --> 487.56]  Just start with the bacon and go from there.
[488.48 --> 490.00]  Well, that's API design.
[490.56 --> 494.98]  So one of the things I thought, actually, before I started dealing with GraphQL is, okay,
[495.06 --> 495.68]  everything's there.
[495.76 --> 496.30]  Where's the API?
[496.30 --> 498.28]  Like, do you still have to design your API?
[499.26 --> 505.90]  And that set of top-level queries actually makes a pretty big difference in terms of
[505.90 --> 509.82]  how do you think about exposing things in your API?
[510.00 --> 513.98]  What are the core concepts that are the ways that people can enter into this thing?
[514.76 --> 516.84]  And maybe you want to expose everything at the top there.
[516.92 --> 519.68]  Maybe every resource that you have has a top-level query.
[519.68 --> 524.10]  So, you know, I can always start with bacon and then get the things related to bacon,
[524.22 --> 526.70]  and I can always start with something else and get the things related to that.
[527.10 --> 528.44]  But that may not be the right answer.
[529.60 --> 531.30]  Isn't it like REST APIs in that way?
[531.40 --> 534.04]  I mean, your endpoints are your top-level menu items, right?
[534.84 --> 535.74]  In a RESTful API.
[536.16 --> 537.12]  In many ways, yes.
[537.22 --> 542.16]  It's like if you had a REST API, but at every point that you had a REST API,
[542.50 --> 545.12]  like say you have a relationship ID, a foreign key.
[545.12 --> 548.20]  In a traditional REST API, you'd get that key,
[548.36 --> 551.16]  and then you'd go fetch the resource for that key from another endpoint,
[551.64 --> 552.74]  the resource for that endpoint.
[553.40 --> 555.44]  Here you can just say, I want to follow that relationship.
[555.58 --> 556.50]  Give me back all the data.
[557.10 --> 557.70]  Why is that better?
[558.48 --> 561.16]  There's a couple of reasons why it has advantages.
[561.40 --> 562.84]  It also can have disadvantages.
[563.28 --> 568.12]  I think it's really interesting to look at what are some of the pros and cons of GraphQL,
[568.34 --> 569.74]  because this is not a panacea.
[569.90 --> 571.70]  It's not a better for everything.
[571.70 --> 579.20]  One of the ways in which it is better is it reduces the number of network calls
[579.20 --> 580.14]  that you're going to have to make,
[580.54 --> 583.60]  especially like on a mobile phone or something like that.
[583.94 --> 589.30]  You want to be making as few calls over the slow part of the network as possible.
[589.80 --> 592.40]  The slow part of the network is between the phone and the API server.
[593.12 --> 595.80]  So if you can consolidate that all into a single request
[595.80 --> 598.38]  and pull back only the data you need,
[598.44 --> 599.94]  you can be much more network efficient.
[599.94 --> 601.54]  Even if on the back end,
[601.68 --> 603.76]  like one way that you can implement a GraphQL server
[603.76 --> 605.70]  is have a wrapper around a REST API.
[607.24 --> 608.40]  That may still be valuable,
[608.58 --> 612.30]  but then all those independent API calls are happening in your data center network,
[612.40 --> 613.26]  which is super fast.
[613.92 --> 616.46]  This might be a good time to actually talk a little bit
[616.46 --> 619.74]  about some of those benefits and drawbacks.
[620.32 --> 621.34]  I'd be once again curious,
[621.50 --> 623.26]  Nick, it sounds like you've been playing with it a little bit.
[623.32 --> 626.78]  What have you found to be good or bad in your first look?
[626.78 --> 627.22]  Yeah.
[627.88 --> 629.90]  So I guess I'll start with the bad first.
[630.32 --> 632.58]  It's another layer on top of things to learn.
[632.68 --> 637.58]  This whole language for defining a schema or defining your query that you have to learn.
[637.68 --> 639.62]  So there's syntax involved around that.
[639.92 --> 641.52]  It's got types to it,
[641.52 --> 644.32]  which are different from the way you define TypeScript types.
[644.48 --> 646.12]  So you have to learn that.
[646.26 --> 647.22]  You have to keep those separate.
[647.84 --> 649.86]  And then I could be wrong about this,
[649.92 --> 653.76]  but don't you have to explicitly define everything that you want to get back?
[653.76 --> 655.92]  Whereas with a rest endpoint, you can just say,
[656.04 --> 659.92]  give me back all the bacon and it'll give you back whatever it has on that.
[660.12 --> 660.44]  All the bacon.
[660.52 --> 660.64]  Yeah.
[660.90 --> 661.18]  Yeah.
[661.52 --> 661.88]  Yeah.
[661.88 --> 663.42]  It is much more verbose.
[663.82 --> 664.06]  Yeah.
[664.44 --> 666.04]  And sometimes I don't know what I want.
[666.82 --> 668.02]  And so that's bad.
[668.64 --> 668.82]  Yeah.
[668.98 --> 672.12]  It's harder to programmatically explore in that way,
[672.18 --> 675.84]  though it does expose an endpoint that lets you programmatically explore
[675.84 --> 677.16]  what the schemas look like.
[677.68 --> 679.18]  Are you talking about like the,
[679.18 --> 683.14]  is it called GraphiQL, like that tool area?
[683.62 --> 683.86]  Yeah.
[683.94 --> 685.84]  Or, I mean, so your GraphQL server,
[685.98 --> 688.44]  actually, I don't know necessarily if that is,
[688.50 --> 689.92]  I think that that is part of the spec.
[690.08 --> 691.92]  I know it's a part of the GraphQL server we've been using.
[691.92 --> 694.36]  It has a schema endpoint where you can just,
[694.62 --> 695.72]  your client can fetch back,
[695.88 --> 697.78]  here's the schema for all of the things.
[698.76 --> 701.46]  And then you could programmatically explore what's in there or not.
[701.50 --> 702.74]  But if you're just poking around at it,
[702.80 --> 706.10]  yeah, it is definitely more painful than,
[707.06 --> 708.98]  let me fetch this and examine the data.
[709.60 --> 709.70]  Yeah.
[709.86 --> 710.18]  Right.
[710.20 --> 713.24]  That is one thing that I was going to put in the pro category is that,
[713.30 --> 716.60]  that tool and specifically like those calls that it's making to figure out
[716.60 --> 717.70]  what you can actually get.
[717.90 --> 720.86]  Those are introspection queries that it is doing on its own.
[720.98 --> 724.36]  And it's really cool that that's just kind of built into the spec to say,
[724.42 --> 727.34]  like, tell me what I can do here and then bring that back.
[727.38 --> 729.60]  And then you can build really powerful tools like that.
[729.78 --> 730.66]  I think it's called GraphiQL.
[730.66 --> 734.86]  It gives me a blank canvas to start writing a query and I can hit control space
[734.86 --> 737.88]  and it will tell me what I can autocomplete here and what makes sense.
[737.88 --> 740.72]  And it'll immediately like show a little red line on that line.
[740.72 --> 743.88]  If it's something that I can't actually fetch or if it's not formed correctly.
[743.88 --> 747.98]  So it really does help you as much as possible when you're exploring like that,
[748.00 --> 749.56]  which is what I've been doing quite a lot.
[749.56 --> 751.26]  So I do like that.
[751.66 --> 757.54]  And I do like the tooling so far that I've been playing around with is really powerful
[757.54 --> 762.30]  in that I basically give it like, this is what our database model looks like.
[762.40 --> 765.30]  And this is the type of queries that you can expect.
[766.04 --> 771.36]  And it just figures out all the plumbing for me and then gives me back exactly what I want,
[771.44 --> 772.04]  which is really cool.
[772.04 --> 774.24]  That is super cool.
[774.40 --> 779.36]  And I feel like, I mean, you mentioned the typing being different than in TypeScript,
[779.82 --> 781.50]  at least with the tooling that we're using.
[781.64 --> 785.42]  You can auto-generate TypeScript types based on the queries that you're running.
[786.08 --> 786.76]  That's cool.
[786.96 --> 791.34]  Define a particular query and have it generate an explicit TypeScript type
[791.34 --> 794.02]  that has only the fields that are coming back from your query,
[794.16 --> 799.48]  which lets you just kind of get really nice end-to-end type safety.
[799.48 --> 801.40]  Is that like Apollo CodeGen?
[802.20 --> 802.64]  Yeah.
[803.22 --> 803.66]  Yeah.
[803.90 --> 804.96]  So I'm playing with that too.
[805.06 --> 806.20]  And that is cool.
[806.44 --> 809.98]  But I'm annoyed with it right now because it doesn't, if you change those,
[810.04 --> 813.04]  it doesn't actually go and clean up the types that it created previously.
[813.42 --> 817.96]  So like my result right now is just blow away that generated types directory
[817.96 --> 821.26]  and then let it regenerate everything, which is kind of annoying.
[821.52 --> 823.76]  But yeah, I'm sure it's something that can be fixed.
[824.40 --> 826.30]  Well, so far I've gone the opposite way with,
[826.42 --> 829.46]  I don't really touch schema generation on my own.
[829.48 --> 831.14]  So I don't think about the GraphQL schema.
[831.52 --> 837.42]  I am using a library called Nest that has a GraphQL plugin for it.
[837.86 --> 840.20]  And so I define all of the types for like my,
[840.68 --> 844.08]  what my queries will look like in TypeScript with decorators.
[844.24 --> 846.54]  And then it generates a schema for me from that.
[847.82 --> 848.26]  Yeah.
[848.32 --> 851.46]  I think one of the really cool things that you're touching on a little bit in
[851.46 --> 856.32]  the tooling is all the same type of magic that you can get with an IDE
[856.32 --> 860.78]  when you go to a strongly typed language and all of the amazing different guarantees
[860.78 --> 861.70]  and other things you can do.
[861.80 --> 864.12]  This allows you to do end to end with your API server.
[865.00 --> 867.50]  Well, you were touching on discovery there, Nick.
[867.62 --> 869.88]  And I think it's worth pointing out.
[870.32 --> 871.74]  Maybe it's not worth pointing out.
[871.74 --> 872.64]  I'm going to point out anyways,
[873.12 --> 879.88]  that RESTful APIs in IDEA are also discoverable
[879.88 --> 883.16]  because of the hypermedia linking in the response.
[883.52 --> 885.70]  It's just that RESTful APIs in practice
[885.70 --> 889.98]  don't usually implement that part of RESTful APIs, the concept.
[890.52 --> 892.62]  GitHub actually had a really nice hypermedia API
[892.62 --> 893.84]  where you could say,
[893.84 --> 896.36]  here is the repo and here are all of the issues.
[896.78 --> 897.76]  The response could say,
[897.94 --> 898.92]  here's my repo object.
[899.26 --> 902.06]  And as a part of that object is a link to a URL
[902.06 --> 905.92]  wherein all of those issues for the repo exist.
[906.22 --> 907.46]  My point is you could also,
[908.14 --> 908.66]  in concept,
[908.94 --> 912.36]  programmatically crawl or discover a RESTful API
[912.36 --> 913.92]  like you could with the schema.
[914.28 --> 914.90]  What's it called?
[915.00 --> 916.14]  Schema endpoint,
[916.58 --> 918.48]  where it will tell you your GraphQL schema.
[919.00 --> 920.44]  And so that would have been pretty cool if it took off.
[920.50 --> 920.82]  Unfortunately,
[920.90 --> 922.74]  it's difficult to implement server side
[922.74 --> 924.32]  and it's just always one more thing.
[924.42 --> 924.96]  And lots of times,
[925.08 --> 927.22]  that's the part that gets dropped off of the RESTful APIs,
[927.38 --> 929.06]  which leaves developers like us,
[929.38 --> 932.54]  instead of letting our tooling discover how it all works,
[932.92 --> 934.22]  is basically just reading the docs
[934.22 --> 934.54]  and saying,
[934.70 --> 935.42]  where are the comments?
[935.48 --> 936.72]  And it's constructing the URL.
[937.38 --> 938.00]  So in practice,
[938.00 --> 938.92]  it didn't really pay off.
[939.00 --> 940.06]  But in concept,
[940.22 --> 943.24]  RESTful APIs also were supposed to be discoverable.
[943.80 --> 944.52]  And some of them are,
[944.52 --> 945.20]  like the better ones,
[945.28 --> 946.00]  the better implementer ones.
[946.82 --> 950.08]  I think part of what makes that hard to implement
[950.08 --> 952.72]  is because it requires a sort of centralization
[952.74 --> 953.28]  of thought
[953.28 --> 955.04]  because every endpoint needs to know
[955.04 --> 956.14]  about every other endpoint
[956.14 --> 957.58]  or at least all of their references.
[958.62 --> 959.72]  And as you say,
[959.80 --> 962.34]  a good API that's well and centrally controlled
[962.34 --> 963.68]  and designed is going to have that.
[964.86 --> 965.98]  But many are not.
[966.34 --> 967.62]  And they're developed independently.
[967.76 --> 968.42]  Whereas GraphQL,
[969.30 --> 970.26]  by being more rigid,
[970.46 --> 971.50]  it forces into,
[971.64 --> 973.76]  everything is going through this GraphQL endpoint,
[974.02 --> 975.14]  so we know about everything,
[975.30 --> 977.88]  so we can force that level of explicitness.
[978.32 --> 979.80]  And that produces the tooling, right?
[979.80 --> 981.42]  The thing that happened around RESTful APIs
[981.42 --> 982.94]  is because it wasn't reliable
[982.94 --> 985.56]  to have those linking between resources,
[986.12 --> 987.38]  the tooling wasn't built out
[987.38 --> 990.24]  in order to do the discoverability, right?
[990.28 --> 991.06]  The actual discovery.
[991.86 --> 993.04]  And so you couldn't rely on it,
[993.10 --> 995.04]  so habitually we didn't think about it.
[995.10 --> 996.62]  And so we always just go read the docs
[996.62 --> 997.58]  and find the endpoints
[997.58 --> 999.42]  and hardcode those into our clients and whatnot.
[1000.06 --> 1001.20]  So I think a big win
[1001.20 --> 1004.24]  is that because it's there from the start,
[1004.34 --> 1004.90]  by default,
[1005.02 --> 1006.16]  on all GraphQL APIs,
[1006.46 --> 1007.82]  now that you can build your tooling saying,
[1007.82 --> 1008.66]  it's going to be there.
[1008.78 --> 1010.48]  And that makes a huge difference in practice.
[1010.48 --> 1027.82]  This episode is brought to you by
[1027.82 --> 1028.80]  DigitalOcean,
[1028.98 --> 1029.60]  Droplets,
[1030.02 --> 1030.80]  Managed Kubernetes,
[1031.18 --> 1032.28]  Managed Databases,
[1032.60 --> 1033.16]  Spaces,
[1033.40 --> 1034.26]  Object Storage,
[1034.54 --> 1035.80]  Volume Block Storage,
[1036.06 --> 1037.00]  Advanced Networking
[1037.00 --> 1038.34]  like Virtual Private Clouds
[1038.34 --> 1039.54]  and Cloud Firewalls,
[1039.54 --> 1041.12]  developer tooling like the Robust,
[1041.22 --> 1042.98]  API and CLI
[1042.98 --> 1044.32]  to make sure you can interact
[1044.32 --> 1045.08]  with your infrastructure
[1045.08 --> 1046.00]  the way you want to.
[1046.42 --> 1048.30]  DigitalOcean is designed for developers
[1048.30 --> 1049.92]  and built for businesses.
[1050.64 --> 1053.18]  Join over 150,000 businesses
[1053.18 --> 1053.82]  that develop,
[1054.14 --> 1054.48]  manage,
[1054.62 --> 1056.06]  and scale their applications
[1056.06 --> 1056.98]  with DigitalOcean.
[1057.40 --> 1059.26]  Head to do.co slash changelog
[1059.26 --> 1060.76]  to get started with a $100 credit.
[1061.08 --> 1063.22]  Again, do.co slash changelog.
[1063.22 --> 1079.64]  All right.
[1079.70 --> 1083.18]  So we've talked some about GraphQL
[1083.18 --> 1084.28]  as a mental model,
[1084.36 --> 1085.06]  what some of the pros,
[1085.18 --> 1085.78]  some of the cons,
[1085.86 --> 1086.38]  things like that,
[1086.38 --> 1087.50]  even some of the different tooling
[1087.50 --> 1088.48]  that it creates.
[1088.48 --> 1090.18]  So let's dive into
[1090.18 --> 1092.40]  something a little bit more concrete,
[1092.40 --> 1093.42]  looking at
[1093.42 --> 1095.00]  what are different approaches
[1095.00 --> 1096.90]  to actually implementing GraphQL,
[1097.14 --> 1099.14]  what are the different pieces of it
[1099.14 --> 1100.98]  that you would need to implement,
[1101.24 --> 1103.56]  and maybe some specific examples
[1103.56 --> 1104.54]  and implementations.
[1105.52 --> 1106.54]  Nick, you want to lead us off
[1106.54 --> 1107.50]  since you've been working
[1107.50 --> 1108.68]  particularly with one?
[1109.44 --> 1109.58]  Sure.
[1110.10 --> 1110.86]  So like I said,
[1110.90 --> 1113.98]  I've been using NestJS for this
[1113.98 --> 1115.32]  and its own plugin
[1115.32 --> 1116.62]  called NestJS GraphQL
[1116.62 --> 1118.94]  that is actually just a wrapper
[1118.94 --> 1120.74]  on top of Apollo,
[1121.02 --> 1123.58]  or there's another one, I think.
[1123.70 --> 1124.94]  But Apollo is the one that I'm using.
[1125.60 --> 1126.90]  Fastify, I think, is another thing.
[1127.70 --> 1129.74]  Anyway, it is interesting
[1129.74 --> 1131.48]  because it lets me just, like,
[1131.54 --> 1132.18]  set up everything
[1132.18 --> 1134.14]  in a very similar way
[1134.14 --> 1135.76]  to the way that I was setting up
[1135.76 --> 1136.80]  REST endpoints with Nest,
[1136.86 --> 1137.72]  where I can create,
[1137.84 --> 1138.60]  instead of a controller
[1138.60 --> 1140.44]  to control all of the
[1140.44 --> 1141.56]  RESTful endpoints I have,
[1141.84 --> 1142.66]  I create a resolver,
[1143.12 --> 1144.24]  and the resolver can have, like,
[1144.26 --> 1144.92]  a query method
[1144.92 --> 1146.46]  or specifically, like,
[1146.52 --> 1148.78]  the pieces of the GraphQL model
[1148.78 --> 1150.20]  that I want to fetch.
[1150.52 --> 1151.86]  And then it can pull that data
[1151.86 --> 1152.82]  and do any kind of processing
[1152.82 --> 1153.84]  it needs to the query
[1153.84 --> 1154.88]  and then pass that along
[1154.88 --> 1156.14]  to a service
[1156.14 --> 1157.84]  that can go read from the database
[1157.84 --> 1159.44]  and query exactly what I need
[1159.44 --> 1161.28]  and then deliver that
[1161.28 --> 1163.44]  or do any other kind of processing.
[1163.60 --> 1164.60]  So it's really nice
[1164.60 --> 1165.84]  and easy to set up.
[1166.24 --> 1167.30]  It's a TypeScript first library
[1167.30 --> 1170.02]  and it's very decorator heavy,
[1170.22 --> 1171.56]  which is interesting.
[1171.98 --> 1174.68]  But it does things kind of magically,
[1174.94 --> 1176.72]  but it's pretty easy to pick up on.
[1177.58 --> 1178.68]  You used a keyword there
[1178.68 --> 1180.70]  that I don't think we actually
[1180.70 --> 1182.38]  dug into defining yet,
[1182.48 --> 1183.66]  but that is pretty core
[1183.66 --> 1184.64]  to implementing at least
[1184.64 --> 1185.76]  GraphQL servers,
[1186.08 --> 1186.78]  the server side,
[1186.86 --> 1187.56]  which is resolver.
[1188.24 --> 1189.76]  Do you want to describe
[1189.76 --> 1190.82]  a little bit what that is
[1190.82 --> 1192.40]  or I can take a stab at it
[1192.40 --> 1193.12]  or whatever you prefer?
[1193.56 --> 1194.72]  As best I can,
[1194.72 --> 1195.42]  I'll try.
[1195.96 --> 1197.68]  So a resolver would be something
[1197.68 --> 1199.88]  that provides the instructions
[1199.88 --> 1203.02]  for taking the GraphQL string,
[1203.16 --> 1205.58]  the query that it receives
[1205.58 --> 1208.84]  and actually doing something with that.
[1208.92 --> 1209.64]  So passing that off
[1209.64 --> 1212.30]  to do whatever it needs to with that.
[1212.40 --> 1213.20]  So that could be like,
[1213.20 --> 1214.20]  you know,
[1214.34 --> 1215.46]  making sure that,
[1215.70 --> 1216.04]  I don't know,
[1216.14 --> 1217.46]  I'm falling apart here a little bit,
[1217.50 --> 1219.10]  but maybe like type checking arguments
[1219.10 --> 1220.68]  that might be passed in to the query
[1220.68 --> 1222.08]  or things like that could happen there.
[1222.08 --> 1223.56]  Yeah, I think that's good.
[1223.68 --> 1225.72]  The resolvers take responsibility
[1225.72 --> 1227.52]  for mapping from the query to the data.
[1228.32 --> 1230.18]  And one of the interesting things
[1230.18 --> 1231.22]  that I've seen there
[1231.22 --> 1233.90]  is like those can be more or less granular.
[1234.20 --> 1236.10]  So you could have a single resolver
[1236.10 --> 1238.04]  that resolves all of an object,
[1238.28 --> 1240.30]  everything that it has there,
[1240.32 --> 1241.88]  or you can actually break apart
[1241.88 --> 1244.08]  different resolvers per field
[1244.08 --> 1245.10]  in that object,
[1245.22 --> 1248.10]  depending on how your data is stored.
[1248.28 --> 1249.74]  And so if, for example,
[1249.74 --> 1251.50]  you're building up a GraphQL object
[1251.50 --> 1253.06]  out of several different objects
[1253.06 --> 1253.86]  in your database,
[1254.80 --> 1258.68]  those references to different objects
[1258.68 --> 1260.46]  could actually be in different resolvers
[1260.46 --> 1261.66]  or different parts of the object
[1261.66 --> 1262.78]  could be in different resolvers.
[1263.50 --> 1266.76]  And then if those fields aren't queried,
[1266.84 --> 1267.70]  those resolvers aren't called,
[1267.76 --> 1269.22]  you don't have to take those database heads.
[1269.68 --> 1272.06]  So they can actually give you a mechanism
[1272.06 --> 1275.70]  for making your backend much more efficient.
[1276.70 --> 1278.16]  Speaking of backends and efficiency,
[1278.16 --> 1279.70]  what happens on a backend
[1279.70 --> 1283.50]  when somebody crafts a GraphQL API
[1283.50 --> 1285.74]  that just spans like six of your tables
[1285.74 --> 1287.04]  and just causes all these joins?
[1287.14 --> 1289.10]  Because let's take a blog scenario, right?
[1289.48 --> 1291.20]  Blog post has comments,
[1291.36 --> 1292.30]  comments have authors,
[1292.48 --> 1293.70]  authors have blog posts.
[1294.22 --> 1295.46]  So couldn't I just say
[1295.46 --> 1301.18]  blog.comments.authors.first.blog.comments
[1301.18 --> 1302.10]  or posts.com?
[1302.16 --> 1303.84]  Can't I just drill down
[1303.84 --> 1305.78]  and just completely screw over your backend?
[1305.78 --> 1306.18]  Yes.
[1311.62 --> 1312.42]  Okay, cool.
[1312.68 --> 1314.32]  And this is actually one of the things
[1314.32 --> 1315.88]  that I saw coming into this
[1315.88 --> 1320.88]  is the first version of the GraphQL server
[1320.88 --> 1322.76]  that I've been working a lot on
[1322.76 --> 1323.70]  was written by somebody
[1323.70 --> 1324.98]  who had a front-end background
[1324.98 --> 1328.62]  who did not understand databases and schema.
[1328.62 --> 1329.42]  Right.
[1329.66 --> 1333.28]  And it was ridiculously slow
[1333.28 --> 1334.42]  even in good cases
[1334.42 --> 1337.54]  and so easy to write pathological queries
[1337.54 --> 1340.10]  that would just totally destroy the backend
[1340.10 --> 1342.12]  and take minutes to resolve.
[1342.68 --> 1343.06]  Mm-hmm.
[1343.72 --> 1345.34]  There's a few different layers to this.
[1345.42 --> 1348.78]  So one is appropriately setting up your resolvers.
[1349.46 --> 1351.98]  If somebody's asking for a particular,
[1352.44 --> 1353.30]  what was your example,
[1353.46 --> 1354.62]  post and their comment
[1354.62 --> 1355.66]  and their whatever and their whatever
[1355.66 --> 1357.62]  and they're just going down one whole thing,
[1357.72 --> 1358.84]  like your resolvers should be such
[1358.84 --> 1360.80]  that it just follows that one trail
[1360.80 --> 1362.52]  and doesn't load everything at this level
[1362.52 --> 1363.58]  and everything at that level
[1363.58 --> 1364.72]  and then everything at that level.
[1365.44 --> 1370.22]  And you may want to set up your top-level queries
[1370.22 --> 1372.24]  such that it's impossible to do something
[1372.24 --> 1374.16]  that's going to span all of those different things.
[1374.16 --> 1376.30]  But there are other techniques you can do.
[1376.44 --> 1381.10]  You can implement checks on how complex is this query,
[1381.20 --> 1382.88]  how much data is going to have various other things
[1382.88 --> 1384.84]  and just throw errors and say,
[1384.96 --> 1387.02]  hey, no, you can't make that query.
[1387.28 --> 1388.04]  It's too much.
[1389.46 --> 1391.10]  Doesn't that break the promise of GraphQL?
[1391.30 --> 1392.76]  I mean, I'm supposed to be able to just go up to the buffet
[1392.76 --> 1393.48]  and grab what I want.
[1394.50 --> 1394.68]  Yeah.
[1395.98 --> 1397.06]  It's not safe.
[1397.54 --> 1399.14]  It does, but it is still your API.
[1399.48 --> 1399.94]  I agree.
[1399.94 --> 1402.94]  And one of the trade-offs that you get
[1402.94 --> 1406.24]  as you create this great flexibility
[1406.24 --> 1407.36]  and this great power
[1407.36 --> 1408.88]  is there's now a great responsibility
[1408.88 --> 1411.12]  that you need to put limits on it
[1411.12 --> 1413.82]  or you need to be confident
[1413.82 --> 1415.12]  that your backend can handle
[1415.12 --> 1416.78]  every type of query that can be crafted.
[1417.48 --> 1419.02]  It seems like it would map well
[1419.02 --> 1420.80]  on top of a denormalized database
[1420.80 --> 1423.10]  or a document-based database.
[1423.20 --> 1426.04]  Whereas if you are retrofitting a GraphQL API
[1426.04 --> 1429.06]  on top of an established, highly relational,
[1430.04 --> 1430.92]  charted even,
[1431.02 --> 1433.28]  like a very established relational database
[1433.28 --> 1435.66]  that you could potentially expose
[1435.66 --> 1438.04]  more of the performance problems
[1438.04 --> 1440.46]  unless you take very precise and extreme measures
[1440.46 --> 1441.56]  in order to stop that.
[1441.94 --> 1443.58]  Whereas maybe it's mapped on top of something
[1443.58 --> 1445.14]  that already is more document-oriented,
[1445.68 --> 1447.18]  you're not going to be crossing tables anyways
[1447.18 --> 1448.34]  because your data is right there
[1448.34 --> 1449.18]  stored in the same document.
[1449.34 --> 1450.58]  Is that a fair assumption?
[1451.58 --> 1453.10]  I think that's definitely fair.
[1453.10 --> 1457.48]  I think it's really easy to,
[1459.02 --> 1460.34]  if you're not careful,
[1460.66 --> 1463.40]  create the ability to do pathological queries.
[1465.50 --> 1468.76]  And implementing a GraphQL server
[1468.76 --> 1472.42]  on top of any sort of complex data situation
[1472.42 --> 1474.28]  is not a trivial task.
[1474.38 --> 1476.28]  This is something that, you know,
[1476.68 --> 1478.10]  there should be somebody who's an expert
[1478.10 --> 1479.88]  in that data system on there.
[1479.88 --> 1482.54]  Though one of the things you highlight
[1482.54 --> 1484.42]  that is kind of interesting to explore
[1484.42 --> 1487.76]  is you can also set up
[1487.76 --> 1489.64]  what is essentially a proxy layer
[1489.64 --> 1491.30]  on top of an existing REST API.
[1491.86 --> 1496.02]  So if you have a big established working system
[1496.02 --> 1497.82]  and you have a REST API there,
[1498.36 --> 1499.54]  you can set up a proxy
[1499.54 --> 1503.28]  that just is calling out to your REST endpoints.
[1504.22 --> 1505.84]  And REST is very good for cacheability.
[1505.84 --> 1507.94]  So you can have that proxy be caching things
[1507.94 --> 1509.44]  in all appropriate ways
[1509.44 --> 1510.60]  and managing the cache
[1510.60 --> 1512.58]  so that you can take advantage
[1512.58 --> 1514.34]  of those individual endpoints
[1514.34 --> 1515.38]  not being pathological.
[1516.08 --> 1516.70]  And with that,
[1516.80 --> 1518.12]  you still get a lot of benefits
[1518.12 --> 1520.34]  in terms of you insert typing
[1520.34 --> 1523.16]  such that you have all these tooling benefits
[1523.16 --> 1525.58]  exposed to the client developers.
[1525.90 --> 1528.20]  And you get that advantage
[1528.20 --> 1530.84]  that all of those individual API requests
[1531.38 --> 1533.14]  are happening inside of your fast data center
[1533.14 --> 1536.52]  instead of over the slow public network.
[1537.66 --> 1538.18]  That's pretty cool.
[1538.76 --> 1540.20]  Coming back a little bit
[1540.20 --> 1542.96]  to implementation options.
[1543.80 --> 1545.82]  So I guess that piece
[1545.82 --> 1547.60]  of being able to wrap a REST API,
[1547.70 --> 1549.96]  maybe you can imagine the GraphQL proxy
[1549.96 --> 1550.62]  as your bacon
[1550.62 --> 1551.82]  that you're wrapping around everything.
[1553.12 --> 1554.80]  You know, it makes everything taste better.
[1555.28 --> 1555.66]  Well played.
[1556.22 --> 1557.90]  Well, before you get into specific ones
[1557.90 --> 1558.42]  that you might build,
[1558.46 --> 1559.10]  I would just want to mention
[1559.10 --> 1560.50]  that what I see a lot of,
[1560.50 --> 1562.20]  which seems like is cool
[1562.20 --> 1563.86]  to try out GraphQL
[1563.86 --> 1565.44]  from a server-side provider,
[1565.92 --> 1567.48]  is probably not scalable and usable.
[1567.70 --> 1567.96]  It's like,
[1568.08 --> 1569.12]  so many of these things are like,
[1569.18 --> 1570.16]  hey, we'll just generate
[1570.16 --> 1571.62]  your GraphQL API for you.
[1571.78 --> 1572.04]  I mean,
[1572.52 --> 1573.50]  take your Postgres database,
[1573.72 --> 1574.42]  take your MongoDB,
[1574.62 --> 1575.82]  take your existing REST API
[1575.82 --> 1577.60]  and just like slap us in front of it.
[1577.70 --> 1579.24]  And now you have a GraphQL API.
[1579.38 --> 1580.48]  I see a lot of those tools
[1580.48 --> 1581.88]  and they are shiny and neat.
[1582.28 --> 1583.58]  And I would play with them,
[1583.64 --> 1584.56]  but I wouldn't necessarily
[1584.56 --> 1586.02]  think to roll that out
[1586.02 --> 1587.02]  on my production system.
[1587.28 --> 1588.54]  Am I off base on that?
[1588.54 --> 1590.80]  I don't think you're off base at all.
[1590.94 --> 1592.92]  I think that those are,
[1593.02 --> 1593.14]  I mean,
[1593.18 --> 1597.86]  similar to kind of vanilla active record
[1597.86 --> 1599.84]  that you might get in Ruby on Rails
[1599.84 --> 1601.42]  or vanilla what have you.
[1601.54 --> 1603.26]  They're great for fast prototyping.
[1603.42 --> 1604.86]  They're great for early projects.
[1605.52 --> 1607.62]  And as you develop scale
[1607.62 --> 1608.78]  and as you have to deal
[1608.78 --> 1609.90]  with complex data,
[1610.12 --> 1612.62]  you're going to have to deal
[1612.62 --> 1613.36]  with those problems
[1613.36 --> 1614.32]  as programming problems.
[1614.40 --> 1615.26]  And you're going to have to think
[1615.26 --> 1616.34]  about your schema design.
[1616.34 --> 1617.24]  Cool.
[1617.88 --> 1618.94]  So Nest, Nick,
[1619.00 --> 1621.20]  is a specific node library
[1621.20 --> 1622.36]  that does this for you
[1622.36 --> 1624.08]  or that you use to build it?
[1624.84 --> 1626.18]  Yeah, that you use to build it.
[1627.14 --> 1627.98]  And so Nest,
[1628.52 --> 1629.42]  like default Nest
[1629.42 --> 1630.88]  would be for REST endpoints.
[1631.02 --> 1631.70]  And then they have a plugin
[1631.70 --> 1632.48]  that lets you.
[1632.62 --> 1632.88]  Okay.
[1633.78 --> 1634.80]  Instead of creating controllers
[1634.80 --> 1635.32]  for those,
[1635.52 --> 1636.82]  create resolvers for
[1636.82 --> 1638.98]  and mutations for GraphQL.
[1639.74 --> 1640.52]  And Nest is a tool
[1640.52 --> 1641.48]  like Express.js
[1641.48 --> 1642.68]  or like any sort of service,
[1642.86 --> 1645.28]  like it's an HTTP library?
[1645.28 --> 1645.72]  Yeah.
[1646.38 --> 1647.16]  So it's a wrapper
[1647.16 --> 1648.16]  on top of Express too.
[1648.58 --> 1648.96]  Oh, it is.
[1648.96 --> 1650.14]  Just kind of an amalgamation
[1650.14 --> 1650.68]  of everything.
[1650.78 --> 1651.68]  So it's not like Express.
[1651.84 --> 1652.66]  It's just wrapping Express.
[1653.00 --> 1653.30]  Yeah.
[1654.10 --> 1655.06]  The old Russian doll.
[1655.88 --> 1656.74]  We're at the level
[1656.74 --> 1658.00]  of meta frameworks now.
[1658.38 --> 1659.86]  Everything's a meta framework, right?
[1660.30 --> 1661.16]  This is true.
[1661.68 --> 1662.52]  That's where the interesting
[1662.52 --> 1663.38]  stuff is happening.
[1663.72 --> 1664.46]  I like to get close
[1664.46 --> 1664.98]  to the metal
[1664.98 --> 1666.22]  and use Express.js.
[1666.76 --> 1667.52]  That's kind of one
[1667.52 --> 1668.22]  of the downsides
[1668.22 --> 1669.54]  that I didn't mention
[1669.54 --> 1670.32]  is if you just wanted
[1670.32 --> 1671.48]  to like do a quick query,
[1671.62 --> 1672.34]  like there's a lot more
[1672.34 --> 1673.10]  ceremony around
[1673.10 --> 1674.20]  making a request,
[1674.20 --> 1675.16]  whereas with a REST endpoint,
[1675.26 --> 1675.70]  I can just,
[1676.14 --> 1676.28]  you know,
[1676.28 --> 1677.84]  from my DevTools console,
[1678.64 --> 1679.28]  use Fetch
[1679.28 --> 1680.16]  and grab the data.
[1680.68 --> 1681.62]  And I can still do that,
[1681.66 --> 1682.48]  but I have to know
[1682.48 --> 1683.56]  exactly how
[1683.56 --> 1685.28]  the query is formed,
[1685.28 --> 1686.72]  like in that RESTful call
[1686.72 --> 1689.10]  and how arguments are passed
[1689.10 --> 1689.92]  and things like that
[1689.92 --> 1691.04]  and send it along.
[1691.60 --> 1692.30]  But then another thing
[1692.30 --> 1693.28]  that has always confused me
[1693.28 --> 1694.06]  when I look at
[1694.06 --> 1695.18]  REST is,
[1695.50 --> 1695.92]  or sorry,
[1696.00 --> 1696.38]  at GraphQL
[1696.38 --> 1698.50]  is there seem to be,
[1699.18 --> 1699.30]  well,
[1699.30 --> 1700.36]  are there different flavors
[1700.36 --> 1700.84]  of it?
[1701.40 --> 1702.34]  Apollo seems like
[1702.34 --> 1703.60]  a flavor,
[1703.84 --> 1704.36]  I don't know,
[1704.46 --> 1705.60]  I might be referring
[1705.60 --> 1706.26]  to it incorrectly,
[1706.42 --> 1707.94]  but I always hear it
[1707.94 --> 1708.78]  referred to as like
[1708.78 --> 1709.76]  a flavor of GraphQL.
[1709.88 --> 1710.84]  Is that an accurate
[1710.84 --> 1711.42]  way of putting it?
[1712.06 --> 1712.92]  That's a great question
[1712.92 --> 1713.66]  that I don't have
[1713.66 --> 1714.90]  a super strong sense.
[1715.28 --> 1716.12]  What is a flavor?
[1716.70 --> 1717.40]  Let me add a couple,
[1717.84 --> 1718.92]  a little more detail
[1718.92 --> 1719.26]  on that.
[1719.38 --> 1719.58]  So,
[1720.02 --> 1720.44]  there have been
[1720.44 --> 1721.46]  evolutions of the spec.
[1721.76 --> 1722.04]  So,
[1722.32 --> 1722.90]  as in anything
[1722.90 --> 1723.90]  with an evolving spec,
[1724.04 --> 1724.62]  you're going to have
[1724.62 --> 1726.62]  different flavors
[1726.62 --> 1727.88]  where people have
[1727.88 --> 1728.76]  chosen to stick
[1728.76 --> 1729.44]  out of one version
[1729.44 --> 1729.76]  of spec
[1729.76 --> 1730.34]  and maybe haven't
[1730.34 --> 1730.76]  updated.
[1731.46 --> 1732.36]  Another thing
[1732.36 --> 1733.80]  that is interesting
[1733.80 --> 1735.12]  to look at
[1735.12 --> 1735.62]  and explore
[1735.62 --> 1736.42]  is that GraphQL
[1736.42 --> 1737.24]  has this
[1737.24 --> 1738.38]  essentially
[1738.38 --> 1740.60]  abstraction leaker
[1740.60 --> 1741.28]  or whatever
[1741.28 --> 1742.46]  for the query language,
[1742.56 --> 1743.64]  which is directives.
[1743.96 --> 1745.06]  You can define
[1745.06 --> 1746.48]  relatively arbitrary,
[1746.68 --> 1747.22]  and I haven't used
[1747.22 --> 1747.94]  this too much,
[1748.00 --> 1748.74]  so I don't know
[1748.74 --> 1749.78]  the boundaries
[1749.78 --> 1750.60]  of that arbitrary,
[1750.74 --> 1751.44]  but you can define
[1751.44 --> 1752.52]  relatively arbitrary
[1752.52 --> 1753.88]  new behavior and logic
[1753.88 --> 1755.24]  in your GraphQL API
[1755.24 --> 1756.16]  using directives.
[1756.16 --> 1756.62]  And these
[1756.62 --> 1757.96]  can then function
[1757.96 --> 1758.98]  essentially as decorators
[1758.98 --> 1759.70]  on your queries
[1759.70 --> 1760.64]  in different ways.
[1761.72 --> 1761.96]  So,
[1762.28 --> 1763.94]  that is another way
[1763.94 --> 1764.52]  which different
[1764.52 --> 1766.10]  implementations of GraphQL
[1766.10 --> 1767.20]  can potentially
[1767.20 --> 1768.62]  create
[1768.62 --> 1769.64]  what feel like
[1769.64 --> 1770.42]  different flavors
[1770.42 --> 1771.32]  because if they have
[1771.32 --> 1772.24]  built-in decorators
[1772.24 --> 1773.94]  that aren't user-defined
[1773.94 --> 1774.78]  but are just part of
[1774.78 --> 1775.90]  when you install Apollo,
[1776.02 --> 1776.60]  you get this.
[1777.42 --> 1777.60]  But,
[1777.80 --> 1778.66]  that's mostly just me
[1778.66 --> 1779.14]  spitballing.
[1779.20 --> 1780.00]  I don't have a
[1780.00 --> 1781.78]  super good sense.
[1782.84 --> 1783.62]  There's also aspects
[1783.62 --> 1784.46]  of it that are not
[1784.46 --> 1785.52]  defined in the spec
[1785.52 --> 1786.74]  but are determined
[1786.74 --> 1787.64]  by the implementation
[1787.64 --> 1788.52]  and people are starting
[1788.52 --> 1790.52]  to figure out norms
[1790.52 --> 1791.36]  such as how do you
[1791.36 --> 1792.16]  handle pagination
[1792.16 --> 1792.74]  and whatnot
[1792.74 --> 1793.38]  where it's like
[1793.38 --> 1794.96]  that's not formalized
[1794.96 --> 1795.78]  but Apollo does have
[1795.78 --> 1796.80]  a way that it does it
[1796.80 --> 1798.14]  and then you can do it
[1798.14 --> 1798.54]  that way
[1798.54 --> 1799.16]  or maybe you can do it
[1799.16 --> 1799.66]  some other way.
[1800.56 --> 1800.88]  Yeah,
[1801.04 --> 1801.84]  I had to deal with
[1801.84 --> 1802.80]  pagination recently.
[1803.24 --> 1804.40]  It did not feel natural
[1804.40 --> 1806.24]  and it was something
[1806.24 --> 1807.24]  where I essentially
[1807.24 --> 1808.56]  created a different
[1808.56 --> 1809.50]  top-level query
[1809.50 --> 1811.26]  and a different object
[1811.26 --> 1811.86]  that included
[1811.86 --> 1813.18]  pagination-related things
[1813.18 --> 1814.10]  and then had the
[1814.10 --> 1815.88]  repeating value.
[1815.96 --> 1816.34]  Cursor,
[1816.62 --> 1816.88]  yeah.
[1817.46 --> 1817.86]  Yeah,
[1817.92 --> 1818.56]  I use a library
[1818.56 --> 1819.94]  called sjsquery
[1819.94 --> 1821.06]  where I just give it
[1821.06 --> 1821.64]  a resolver
[1821.64 --> 1823.64]  and the DTO
[1823.64 --> 1824.42]  or what the
[1824.42 --> 1825.62]  queries will look like
[1825.62 --> 1826.60]  and it will
[1826.60 --> 1827.46]  automatically paginate
[1827.46 --> 1828.24]  everything.
[1828.76 --> 1829.18]  That's one of the
[1829.18 --> 1830.90]  really cool libraries
[1830.90 --> 1831.32]  that we're using
[1831.32 --> 1832.30]  on top of all of this.
[1833.02 --> 1833.42]  Interesting.
[1833.56 --> 1834.10]  What's that called?
[1834.62 --> 1834.90]  It's called
[1834.90 --> 1835.56]  an sjsquery.
[1836.40 --> 1836.98]  I feel like Nick
[1836.98 --> 1837.64]  probably doesn't ever
[1837.64 --> 1838.68]  actually write code.
[1838.90 --> 1839.58]  He just kind of
[1839.58 --> 1841.40]  instructs things
[1841.40 --> 1842.30]  to do the coding
[1842.30 --> 1842.82]  for him.
[1843.20 --> 1843.56]  He's like,
[1843.62 --> 1844.58]  this is what I use.
[1844.70 --> 1845.68]  They're called macros.
[1846.02 --> 1847.14]  Down underneath there,
[1847.64 --> 1849.00]  inside my Vim macro,
[1849.54 --> 1850.34]  it does all the coding
[1850.34 --> 1850.80]  for me.
[1852.04 --> 1852.64]  I think Nick
[1852.64 --> 1853.40]  is just operating
[1853.40 --> 1854.46]  at a higher level
[1854.46 --> 1855.16]  of abstraction
[1855.16 --> 1856.16]  than the rest of us.
[1856.18 --> 1856.96]  That's my point,
[1857.04 --> 1857.24]  yeah.
[1857.94 --> 1858.94]  If you abstract it enough,
[1859.02 --> 1859.30]  then...
[1859.30 --> 1860.06]  He's either a wizard
[1860.06 --> 1860.68]  or a fool.
[1860.78 --> 1861.36]  I can't figure out
[1861.36 --> 1861.64]  which one.
[1861.68 --> 1862.22]  I think he's probably
[1862.22 --> 1862.60]  a wizard.
[1863.60 --> 1864.70]  I think he's a wizard.
[1864.70 --> 1865.70]  I'm really curious
[1865.70 --> 1866.68]  how that handles
[1866.68 --> 1867.26]  pagination.
[1867.58 --> 1867.78]  So,
[1868.44 --> 1869.44]  what does it do
[1869.44 --> 1870.24]  to the underlying
[1870.24 --> 1870.94]  queries?
[1871.40 --> 1872.00]  I'm looking
[1872.00 --> 1873.50]  at their docs
[1873.50 --> 1873.84]  right now.
[1873.90 --> 1874.02]  Oh,
[1874.06 --> 1874.34]  interesting.
[1874.86 --> 1875.06]  So,
[1875.14 --> 1875.78]  they do kind of
[1875.78 --> 1876.48]  a similar thing
[1876.48 --> 1877.54]  where they have
[1877.54 --> 1879.00]  a meta object
[1879.00 --> 1879.80]  that wraps
[1879.80 --> 1881.22]  the underlying objects
[1881.22 --> 1881.82]  that includes
[1881.82 --> 1883.06]  a page info object
[1883.06 --> 1884.08]  and then
[1884.08 --> 1885.30]  an edges object
[1885.30 --> 1885.92]  which has all
[1885.92 --> 1886.32]  the different
[1886.32 --> 1887.90]  whatever the results were.
[1888.62 --> 1889.12]  That makes sense.
[1889.62 --> 1889.78]  Yeah.
[1890.32 --> 1890.56]  So,
[1890.66 --> 1891.34]  on the client side,
[1891.44 --> 1891.54]  Nick,
[1891.54 --> 1891.86]  are you doing
[1891.86 --> 1892.40]  the client and
[1892.40 --> 1892.94]  the server side
[1892.94 --> 1893.70]  in this project?
[1894.06 --> 1895.20]  Just the server side
[1895.20 --> 1895.52]  right now.
[1895.54 --> 1895.68]  Like,
[1895.70 --> 1896.64]  are you using
[1896.64 --> 1897.54]  the GraphQL API
[1897.54 --> 1898.10]  or you're not even
[1898.10 --> 1898.92]  using it yourself?
[1899.68 --> 1899.92]  Right.
[1899.92 --> 1900.48]  That is something
[1900.48 --> 1901.24]  I wanted to bring up
[1901.24 --> 1902.44]  is if you had
[1902.44 --> 1903.04]  any experience
[1903.04 --> 1903.36]  with,
[1903.36 --> 1903.68]  like,
[1904.98 --> 1905.42]  I guess,
[1905.48 --> 1906.38]  service-to-service
[1906.38 --> 1908.04]  GraphQL calls
[1908.04 --> 1909.04]  like on the server side.
[1909.32 --> 1909.82]  Is that something
[1909.82 --> 1910.74]  that you've handled
[1910.74 --> 1911.06]  before,
[1911.14 --> 1911.38]  KBall?
[1911.86 --> 1912.08]  Oh,
[1912.16 --> 1912.52]  interesting.
[1913.16 --> 1913.54]  No,
[1913.60 --> 1914.24]  it is not
[1914.24 --> 1915.80]  because all of our
[1915.80 --> 1916.88]  service-to-service
[1916.88 --> 1917.52]  stuff on our
[1917.52 --> 1918.28]  backend right now
[1918.28 --> 1918.90]  is using
[1918.90 --> 1919.76]  GRPC.
[1920.44 --> 1920.62]  So,
[1920.70 --> 1921.16]  we're not
[1921.16 --> 1922.38]  currently
[1922.38 --> 1923.20]  doing that.
[1923.26 --> 1923.68]  We only use
[1923.68 --> 1924.52]  GraphQL to communicate
[1924.52 --> 1925.24]  to the client.
[1925.24 --> 1926.68]  Interesting.
[1926.96 --> 1927.10]  Yeah,
[1927.16 --> 1928.38]  so I've only been
[1928.38 --> 1929.20]  working on a
[1929.20 --> 1929.66]  proof-of-concept
[1929.66 --> 1930.60]  with this stuff
[1930.60 --> 1931.14]  for the last few
[1931.14 --> 1931.62]  weeks and
[1931.62 --> 1932.98]  it's all
[1932.98 --> 1933.42]  server side.
[1934.40 --> 1934.62]  Mm-hmm.
[1935.30 --> 1936.20]  I just wondered
[1936.20 --> 1936.90]  how a client
[1936.90 --> 1937.50]  would then interact
[1937.50 --> 1938.34]  with the pagination
[1938.34 --> 1938.80]  like is
[1938.80 --> 1940.32]  maybe the
[1940.32 --> 1941.14]  there's an
[1941.14 --> 1941.62]  auto-generated
[1941.62 --> 1942.12]  client
[1942.12 --> 1943.92]  that knows
[1943.92 --> 1944.66]  that the way
[1944.66 --> 1945.12]  that Nest
[1945.12 --> 1945.92]  does pagination
[1945.92 --> 1946.40]  there's like a
[1946.40 --> 1946.98]  Nest client
[1946.98 --> 1947.50]  that knows
[1947.50 --> 1947.82]  that
[1947.82 --> 1948.74]  and so they
[1948.74 --> 1949.28]  already do
[1949.28 --> 1949.82]  the pagination
[1949.82 --> 1950.42]  for you or
[1950.42 --> 1950.68]  something.
[1951.06 --> 1951.52]  That's why I
[1951.52 --> 1951.88]  asked that.
[1951.88 --> 1952.52]  So,
[1952.64 --> 1953.48]  this NestJS query
[1953.48 --> 1954.56]  you give it
[1954.56 --> 1955.06]  the objects
[1955.06 --> 1955.36]  that you're
[1955.36 --> 1955.84]  working with
[1955.84 --> 1956.36]  and it will
[1956.36 --> 1956.92]  define the
[1956.92 --> 1957.44]  schema that
[1957.44 --> 1958.54]  includes that
[1958.54 --> 1959.14]  page info
[1959.14 --> 1960.26]  and edges
[1960.26 --> 1962.42]  as leaves
[1962.42 --> 1962.86]  in that
[1962.86 --> 1963.50]  graph.
[1963.90 --> 1964.42]  The client
[1964.42 --> 1965.14]  knows exactly
[1965.14 --> 1965.82]  what it can
[1965.82 --> 1966.46]  expect from
[1966.46 --> 1968.10]  that on
[1968.10 --> 1968.70]  any kind of
[1968.70 --> 1969.10]  pageable
[1969.10 --> 1970.04]  resolver.
[1971.00 --> 1971.20]  Gotcha.
[1971.84 --> 1972.50]  That's interesting.
[1972.88 --> 1973.42]  I think that's
[1973.42 --> 1973.98]  actually pretty
[1973.98 --> 1974.70]  cool how it's
[1974.70 --> 1975.08]  dealing with
[1975.08 --> 1975.54]  pagination
[1975.54 --> 1976.08]  looking at
[1976.08 --> 1976.58]  that now.
[1977.50 --> 1977.58]  So,
[1977.74 --> 1978.22]  is Nest
[1978.22 --> 1979.00]  only handles
[1979.00 --> 1979.40]  the server
[1979.40 --> 1979.76]  side or
[1979.76 --> 1980.40]  it's generating
[1980.40 --> 1981.38]  for you all
[1981.38 --> 1981.82]  that client
[1981.82 --> 1982.38]  side work
[1982.38 --> 1982.92]  as well
[1982.92 --> 1983.48]  so that you
[1983.48 --> 1983.84]  plug that
[1983.84 --> 1984.36]  into whatever
[1984.36 --> 1984.88]  you're doing
[1984.88 --> 1985.22]  on the
[1985.22 --> 1985.54]  client?
[1986.46 --> 1986.66]  What would
[1986.66 --> 1987.84]  be required
[1987.84 --> 1988.80]  on the
[1988.80 --> 1989.58]  front end
[1989.58 --> 1989.86]  on the
[1989.86 --> 1990.10]  client?
[1991.18 --> 1991.84]  I'd want
[1991.84 --> 1992.56]  to have
[1992.56 --> 1994.70]  access to
[1994.70 --> 1995.90]  all of
[1995.90 --> 1997.04]  the types
[1997.04 --> 1998.20]  clearly.
[1999.02 --> 1999.88]  I guess that's
[1999.88 --> 2000.50]  the main thing
[2000.50 --> 2001.28]  is the types
[2001.28 --> 2001.78]  and then whatever
[2001.78 --> 2002.40]  library is
[2002.40 --> 2002.84]  handling how
[2002.84 --> 2003.42]  it runs
[2003.42 --> 2003.90]  queries and
[2003.90 --> 2004.42]  doing caching
[2004.42 --> 2004.92]  and things
[2004.92 --> 2005.28]  like that.
[2005.34 --> 2005.42]  So,
[2005.54 --> 2007.24]  I guess the
[2007.24 --> 2007.68]  question is,
[2007.76 --> 2008.42]  is it exporting
[2008.42 --> 2008.90]  all those
[2008.90 --> 2009.24]  types?
[2009.66 --> 2010.38]  It has to.
[2010.62 --> 2010.82]  Alright,
[2010.90 --> 2011.22]  I've answered
[2011.22 --> 2011.52]  my own
[2011.52 --> 2011.86]  question.
[2012.88 --> 2013.28]  That's
[2013.28 --> 2013.66]  something that
[2013.66 --> 2014.08]  I haven't
[2014.08 --> 2014.52]  really touched
[2014.52 --> 2015.18]  on yet in
[2015.18 --> 2016.14]  my exploration
[2016.14 --> 2017.40]  and so I
[2017.40 --> 2017.82]  assume that
[2017.82 --> 2018.54]  somehow the
[2018.54 --> 2019.48]  client would
[2019.48 --> 2019.86]  have access
[2019.86 --> 2020.16]  to the
[2020.16 --> 2020.42]  schema.
[2020.74 --> 2021.30]  Is that
[2021.30 --> 2021.74]  right?
[2022.42 --> 2022.60]  Maybe?
[2022.74 --> 2023.52]  Or at least
[2023.52 --> 2024.40]  from a tooling
[2024.40 --> 2024.68]  level,
[2024.88 --> 2026.72]  it knows what
[2026.72 --> 2027.20]  it can query
[2027.20 --> 2027.90]  based on that.
[2028.42 --> 2028.86]  And then tools
[2028.86 --> 2029.74]  like Apollo
[2029.74 --> 2031.20]  CodeGen will,
[2031.64 --> 2032.02]  from what I've
[2032.02 --> 2032.18]  gathered,
[2032.28 --> 2032.68]  that will go
[2032.68 --> 2034.02]  through an
[2034.02 --> 2034.72]  AST walker
[2034.72 --> 2035.44]  and just find
[2035.44 --> 2035.98]  all of the
[2035.98 --> 2036.58]  places where
[2036.58 --> 2037.14]  you're making
[2037.14 --> 2037.92]  GraphQL calls,
[2038.32 --> 2038.82]  look at those
[2038.82 --> 2039.14]  queries,
[2039.14 --> 2039.66]  and then
[2039.66 --> 2040.14]  define
[2040.14 --> 2041.36]  interfaces in
[2041.36 --> 2041.62]  TypeScript
[2041.62 --> 2043.12]  that match
[2043.12 --> 2043.72]  exactly what
[2043.72 --> 2044.12]  you'd be getting
[2044.12 --> 2044.56]  back or what
[2044.56 --> 2045.04]  you expect to
[2045.04 --> 2045.42]  get back.
[2047.20 --> 2047.60]  Yes,
[2048.02 --> 2048.96]  that is
[2048.96 --> 2049.34]  correct.
[2050.10 --> 2050.38]  And I guess
[2050.38 --> 2050.82]  what I would
[2050.82 --> 2051.24]  want,
[2051.36 --> 2051.90]  ideally,
[2052.18 --> 2052.46]  since
[2052.46 --> 2053.60]  NestJS is
[2053.60 --> 2054.44]  also doing
[2054.44 --> 2054.98]  this all in
[2054.98 --> 2055.80]  JavaScript or
[2055.80 --> 2056.20]  TypeScript,
[2056.52 --> 2057.70]  I would love
[2057.70 --> 2058.24]  something that
[2058.24 --> 2058.76]  lets me have
[2058.76 --> 2059.26]  end-to-end.
[2059.38 --> 2059.66]  Because right
[2059.66 --> 2060.22]  now I'm doing
[2060.22 --> 2061.48]  GraphQL in
[2061.48 --> 2062.42]  Python and
[2062.42 --> 2062.90]  then I'm on
[2062.90 --> 2063.46]  the server side
[2063.46 --> 2063.72]  and then I'm
[2063.72 --> 2064.36]  querying it with
[2064.36 --> 2064.68]  JavaScript.
[2065.28 --> 2065.64]  And there's
[2065.64 --> 2066.22]  always this step
[2066.22 --> 2066.58]  of, okay,
[2066.60 --> 2067.40]  my client thinks
[2067.40 --> 2068.02]  it's doing this,
[2068.02 --> 2068.56]  it sends this
[2068.56 --> 2069.00]  query and
[2069.00 --> 2069.24]  then the
[2069.24 --> 2069.72]  backend says,
[2069.82 --> 2070.08]  wait, what
[2070.08 --> 2070.52]  are you talking
[2070.52 --> 2070.80]  about?
[2070.84 --> 2071.28]  That's not a
[2071.28 --> 2072.22]  query, right?
[2072.30 --> 2073.18]  But presumably
[2073.18 --> 2073.92]  if you're doing
[2073.92 --> 2074.82]  everything end-to-end
[2074.82 --> 2075.50]  in JavaScript or
[2075.50 --> 2076.04]  TypeScript, you
[2076.04 --> 2077.24]  can deal with
[2077.24 --> 2078.38]  that and catch
[2078.38 --> 2078.70]  it at the
[2078.70 --> 2079.24]  tooling level
[2079.24 --> 2079.84]  rather than
[2079.84 --> 2080.38]  at the
[2080.38 --> 2081.52]  testing runtime
[2081.52 --> 2081.88]  level.
[2082.74 --> 2082.82]  Yeah,
[2083.12 --> 2083.52]  presumably.
[2086.20 --> 2086.90]  I mean, I
[2086.90 --> 2087.58]  think Apollo
[2087.58 --> 2088.64]  CodeGen looks at
[2088.64 --> 2089.28]  the GraphQL
[2089.28 --> 2090.58]  schema, so it
[2090.58 --> 2091.56]  does some
[2091.56 --> 2091.94]  amount of
[2091.94 --> 2092.16]  that.
[2092.54 --> 2092.70]  I don't
[2092.70 --> 2092.84]  know.
[2093.40 --> 2093.58]  Yeah.
[2093.84 --> 2094.24]  We're getting
[2094.24 --> 2095.22]  outside of my
[2095.22 --> 2096.14]  six months
[2096.14 --> 2096.66]  experience.
[2096.66 --> 2098.80]  What I've
[2098.80 --> 2099.12]  done in the
[2099.12 --> 2099.88]  past for
[2099.88 --> 2100.62]  that kind
[2100.62 --> 2101.12]  of sharing
[2101.12 --> 2102.74]  is, and
[2102.74 --> 2103.14]  not with
[2103.14 --> 2103.68]  GraphQL, but
[2103.68 --> 2104.06]  with like
[2104.06 --> 2104.84]  RESTful endpoints
[2104.84 --> 2106.00]  is I've
[2106.00 --> 2108.20]  used, so
[2108.20 --> 2108.60]  Nest has a
[2108.60 --> 2109.10]  plugin for
[2109.10 --> 2109.70]  Swagger, so
[2109.70 --> 2110.30]  it'll auto
[2110.30 --> 2111.30]  generate Swagger
[2111.30 --> 2112.16]  documentation for
[2112.16 --> 2112.56]  all of your
[2112.56 --> 2113.48]  endpoints for
[2113.48 --> 2114.20]  RESTful calls.
[2114.70 --> 2115.48]  And you can
[2115.48 --> 2116.14]  export that as a
[2116.14 --> 2116.70]  JSON file, and
[2116.70 --> 2117.30]  then I've just
[2117.30 --> 2117.86]  written a parser
[2117.86 --> 2118.86]  that goes
[2118.86 --> 2120.24]  through the
[2120.24 --> 2120.94]  JSON and
[2120.94 --> 2122.40]  creates interfaces
[2122.40 --> 2122.86]  out of that
[2122.86 --> 2123.46]  that are then
[2123.46 --> 2124.30]  just automatically
[2124.30 --> 2125.08]  generated and
[2125.08 --> 2125.92]  placed into the
[2125.92 --> 2126.32]  project.
[2126.66 --> 2128.70]  Not the most
[2128.70 --> 2129.36]  straightforward way,
[2129.46 --> 2130.42]  but it is a
[2130.42 --> 2131.34]  way to kind of
[2131.34 --> 2131.98]  not have to
[2131.98 --> 2132.44]  think about
[2132.44 --> 2133.14]  writing all of
[2133.14 --> 2133.70]  those interfaces.
[2134.64 --> 2135.02]  I love it.
[2135.08 --> 2135.72]  Nick, you always
[2135.72 --> 2136.46]  find a way to
[2136.46 --> 2137.40]  autogen, man.
[2137.84 --> 2138.30]  Generate that
[2138.30 --> 2138.54]  stuff.
[2139.22 --> 2139.80]  I need to suck
[2139.80 --> 2140.30]  some of that
[2140.30 --> 2140.92]  stuff into my
[2140.92 --> 2141.18]  head.
[2141.28 --> 2141.58]  I know.
[2141.86 --> 2142.84]  I feel like I
[2142.84 --> 2143.66]  toil away at my
[2143.66 --> 2144.14]  code, and it
[2144.14 --> 2144.78]  just kind of like
[2144.78 --> 2146.02]  tells things to
[2146.02 --> 2146.62]  do things for
[2146.62 --> 2146.82]  him.
[2147.02 --> 2147.42]  I should hang
[2147.42 --> 2147.78]  out with you
[2147.78 --> 2148.04]  more.
[2148.36 --> 2148.76]  Work less.
[2148.76 --> 2148.78]  Work less.
[2148.78 --> 2148.84]  Work less.
[2148.84 --> 2148.88]  Work less.
[2148.88 --> 2149.04]  Work less.
[2149.04 --> 2149.38]  Work less.
[2149.38 --> 2149.84]  Work less.
[2149.84 --> 2150.84]  Work less.
[2150.84 --> 2150.88]  Work less.
[2150.88 --> 2152.88]  Work less.
[2152.88 --> 2152.90]  Work less.
[2152.90 --> 2152.94]  Work less.
[2152.94 --> 2152.96]  Work less.
[2152.96 --> 2156.64]  Work less.
[2156.66 --> 2163.66]  What up, party
[2163.66 --> 2164.00]  animals?
[2164.28 --> 2165.02]  Here's some news
[2165.02 --> 2165.60]  that you may not
[2165.60 --> 2166.22]  have heard yet.
[2166.64 --> 2167.88]  Gatsby now has a
[2167.88 --> 2168.72]  partnership program.
[2168.92 --> 2169.94]  If you are building
[2169.94 --> 2170.90]  Gatsby sites for
[2170.90 --> 2172.02]  clients, or you're
[2172.02 --> 2172.82]  not yet, but you
[2172.82 --> 2173.72]  wish you were, you
[2173.72 --> 2174.60]  can now grow that
[2174.60 --> 2175.48]  with confidence by
[2175.48 --> 2176.58]  getting support and
[2176.58 --> 2177.66]  resources directly
[2177.66 --> 2178.30]  from the Gatsby
[2178.30 --> 2178.68]  team.
[2179.02 --> 2180.02]  Become a Gatsby
[2180.02 --> 2180.86]  certified partner
[2180.86 --> 2181.88]  today to accelerate
[2181.88 --> 2182.90]  your growth alongside
[2182.90 --> 2183.50]  their amazing
[2183.50 --> 2183.96]  ecosystem.
[2184.42 --> 2185.60]  Get exclusive access
[2185.60 --> 2186.26]  to Gatsby's
[2186.26 --> 2186.64]  product, and
[2186.66 --> 2187.72]  roadmap, beta
[2187.72 --> 2188.60]  test new features,
[2188.92 --> 2189.56]  access training
[2189.56 --> 2190.46]  materials, and
[2190.46 --> 2191.14]  connect with the
[2191.14 --> 2191.74]  Gatsby team.
[2192.06 --> 2192.88]  There's a whole
[2192.88 --> 2193.70]  bundle of
[2193.70 --> 2194.62]  partnership benefits.
[2194.84 --> 2195.50]  The sky's the
[2195.50 --> 2196.50]  limit, so check out
[2196.50 --> 2197.40]  Gatsby's partnership
[2197.40 --> 2198.42]  program using the
[2198.42 --> 2199.18]  link in the show
[2199.18 --> 2200.32]  notes or point your
[2200.32 --> 2201.02]  browser to
[2201.02 --> 2202.44]  gatsbyjs.com
[2202.44 --> 2203.72]  slash changelog.
[2203.88 --> 2205.08]  Once again, there's
[2205.08 --> 2205.80]  a link in your
[2205.80 --> 2206.78]  show notes or
[2206.78 --> 2208.50]  gatsbyjs.com
[2208.50 --> 2209.82]  slash changelog.
[2209.82 --> 2232.96]  All right, let's get
[2232.96 --> 2234.14]  back into it and
[2234.14 --> 2236.02]  talk about one
[2236.02 --> 2237.18]  subject that we have
[2237.18 --> 2238.10]  not talked about much
[2238.10 --> 2238.98]  yet, which is
[2238.98 --> 2239.56]  mutations.
[2240.00 --> 2240.38]  How do you
[2240.38 --> 2241.12]  actually change
[2241.12 --> 2242.10]  data using a
[2242.10 --> 2243.00]  GraphQL API?
[2243.42 --> 2243.94]  This is something
[2243.94 --> 2244.80]  that Jared was
[2244.80 --> 2245.36]  talking about on the
[2245.36 --> 2245.52]  break.
[2245.56 --> 2246.32]  He said, well, you
[2246.32 --> 2247.02]  know, you have a
[2247.02 --> 2247.64]  read-write API.
[2247.78 --> 2248.24]  We've only talked
[2248.24 --> 2248.76]  about read.
[2248.84 --> 2249.38]  How does write
[2249.38 --> 2249.66]  work?
[2250.34 --> 2250.72]  This is a
[2250.72 --> 2251.42]  querying language,
[2251.54 --> 2253.22]  not a query.
[2253.22 --> 2253.58]  language.
[2253.58 --> 2254.90]  But if you're going
[2254.90 --> 2257.08]  to replace rest, rest
[2257.08 --> 2258.98]  you've got to do
[2258.98 --> 2259.80]  some amount of
[2259.80 --> 2261.10]  updating those things,
[2261.22 --> 2262.58]  state transfer, right?
[2262.62 --> 2264.08]  Or crud, create,
[2264.20 --> 2265.38]  read, update, and
[2265.38 --> 2265.72]  delete.
[2265.96 --> 2266.88]  How is that going to
[2266.88 --> 2267.14]  work?
[2267.30 --> 2269.24]  So who wants to
[2269.24 --> 2269.84]  lead us off here?
[2270.68 --> 2271.48]  I'll go last.
[2271.64 --> 2272.74]  Also, not at all.
[2273.82 --> 2275.02]  Yeah, I have not
[2275.02 --> 2275.86]  gotten that far in my
[2275.86 --> 2277.56]  POC yet, so I
[2277.56 --> 2278.46]  haven't mutated
[2278.46 --> 2279.06]  anything.
[2279.28 --> 2280.02]  Nick will get back to
[2280.02 --> 2280.24]  us.
[2280.30 --> 2280.98]  So it's you, K-Ball.
[2281.10 --> 2281.86]  How do you mutate?
[2281.86 --> 2282.92]  All right, that's
[2282.92 --> 2283.12]  me.
[2283.28 --> 2286.14]  So I think the way
[2286.14 --> 2286.64]  to think about
[2286.64 --> 2287.78]  mutations is it's
[2287.78 --> 2290.00]  actually coming back
[2290.00 --> 2290.84]  to this question of
[2290.84 --> 2292.84]  query design and
[2292.84 --> 2293.60]  API design.
[2293.80 --> 2295.08]  It's much more
[2295.08 --> 2296.44]  explicit, or at
[2296.44 --> 2297.32]  least has the
[2297.32 --> 2298.38]  potential to be much
[2298.38 --> 2298.88]  more explicit.
[2299.10 --> 2300.44]  So we talked about
[2300.44 --> 2301.58]  how all the queries
[2301.58 --> 2302.80]  are this kind of
[2302.80 --> 2304.04]  graph descending from
[2304.04 --> 2305.06]  the top level query.
[2305.18 --> 2305.86]  So you have query,
[2306.20 --> 2307.04]  you define what the
[2307.04 --> 2308.10]  first level of things
[2308.10 --> 2308.66]  you're allowed to
[2308.66 --> 2310.06]  query is, and then
[2310.06 --> 2310.76]  you can follow
[2310.76 --> 2311.60]  relationships.
[2311.86 --> 2312.64]  down through the
[2312.64 --> 2313.56]  different resources
[2313.56 --> 2314.52]  through the types.
[2315.34 --> 2316.44]  On the mutation
[2316.44 --> 2319.08]  side, it's similar
[2319.08 --> 2320.32]  in that you have a
[2320.32 --> 2321.40]  top level mutation
[2321.40 --> 2323.08]  object where you're
[2323.08 --> 2324.38]  defining the mutations
[2324.38 --> 2326.68]  that are allowed to
[2326.68 --> 2326.98]  happen.
[2327.88 --> 2329.32]  And I have not used
[2329.32 --> 2330.38]  this a huge amount,
[2330.46 --> 2332.26]  so I'm not an expert
[2332.26 --> 2333.08]  on this at all, and I
[2333.08 --> 2334.04]  don't actually have a
[2334.04 --> 2335.24]  strong sense the
[2335.24 --> 2336.24]  extent to which there
[2336.24 --> 2337.36]  is that same level of
[2337.36 --> 2338.10]  nesting and following
[2338.10 --> 2338.74]  relationships.
[2338.74 --> 2340.46]  But if you look at
[2340.46 --> 2342.34]  the mutations part of
[2342.34 --> 2343.38]  the GraphQL API, what
[2343.38 --> 2345.36]  you'll see is they
[2345.36 --> 2348.28]  have a ton of
[2348.28 --> 2350.14]  mutations defined, and
[2350.14 --> 2350.96]  they're all very
[2350.96 --> 2351.64]  explicit.
[2352.34 --> 2353.36]  So whereas in a
[2353.36 --> 2354.50]  REST API, you might
[2354.50 --> 2355.72]  assume that you're
[2355.72 --> 2356.40]  going to expose
[2356.40 --> 2357.54]  mostly CRUD
[2357.54 --> 2358.28]  functions, so you
[2358.28 --> 2359.10]  just have an update
[2359.10 --> 2359.98]  endpoint that lets you
[2359.98 --> 2360.98]  update the fields on
[2360.98 --> 2361.62]  your object, and
[2361.62 --> 2362.16]  maybe there's some
[2362.16 --> 2363.10]  permissions around that
[2363.10 --> 2363.78]  or what have you.
[2363.78 --> 2367.38]  in a GraphQL API,
[2367.80 --> 2368.76]  you're going to have
[2368.76 --> 2369.70]  much more explicit
[2369.70 --> 2371.16]  mutations, and some
[2371.16 --> 2371.98]  of those maybe just
[2371.98 --> 2373.10]  update this object and
[2373.10 --> 2374.30]  use, pass in the new
[2374.30 --> 2375.58]  object types or things
[2375.58 --> 2377.10]  around that, but if
[2377.10 --> 2377.78]  you look at, for
[2377.78 --> 2378.76]  example, the GitHub
[2378.76 --> 2380.02]  API, there's a lot of
[2380.02 --> 2381.02]  things about accept this
[2381.02 --> 2382.76]  suggestion, clone this
[2382.76 --> 2383.82]  thing, do this thing,
[2383.84 --> 2384.80]  you have a mutation
[2384.80 --> 2386.26]  for each type of action
[2386.26 --> 2387.14]  that you're wanting to
[2387.14 --> 2387.46]  enable.
[2388.36 --> 2390.08]  And so it feels in
[2390.08 --> 2390.90]  some ways much more
[2390.90 --> 2393.00]  like defining an
[2393.00 --> 2395.84]  internal API that
[2395.84 --> 2396.64]  you might call
[2396.64 --> 2397.48]  programmatically,
[2397.68 --> 2399.64]  rather than this
[2399.64 --> 2401.50]  model that I think
[2401.50 --> 2402.72]  CRUD particularly,
[2403.10 --> 2404.12]  and the combo of
[2404.12 --> 2404.88]  CRUD and REST, a
[2404.88 --> 2405.96]  lot of stuff got
[2405.96 --> 2407.24]  sort of plumbed
[2407.24 --> 2407.96]  together where most
[2407.96 --> 2408.94]  REST APIs are just
[2408.94 --> 2409.58]  implementing CRUD
[2409.58 --> 2410.18]  functionality.
[2411.22 --> 2412.62]  This idea of, I just
[2412.62 --> 2413.60]  have an object and I'm
[2413.60 --> 2415.00]  going to give you new
[2415.00 --> 2416.36]  fields for it, or
[2416.36 --> 2417.40]  new override certain
[2417.40 --> 2418.12]  fields for it.
[2418.38 --> 2419.66]  It's more towards
[2419.66 --> 2421.26]  what type of API
[2421.26 --> 2422.50]  would I extend
[2422.50 --> 2425.06]  inside of my project,
[2425.48 --> 2427.16]  add this thing, do
[2427.16 --> 2428.16]  this thing, change
[2428.16 --> 2429.56]  this thing, where I'm
[2429.56 --> 2430.56]  explicitly calling out
[2430.56 --> 2431.48]  the fields that I want
[2431.48 --> 2431.90]  from you.
[2432.02 --> 2432.70]  And because everything
[2432.70 --> 2433.62]  is strongly typed, I
[2433.62 --> 2434.76]  can have those fields
[2434.76 --> 2436.32]  be objects with
[2436.32 --> 2438.10]  particular types, but
[2438.10 --> 2440.20]  that's kind of where it
[2440.20 --> 2440.38]  goes.
[2440.46 --> 2441.18]  And I think you can
[2441.18 --> 2444.22]  specify, for an
[2444.22 --> 2445.64]  object, which fields do
[2445.64 --> 2446.82]  you accept in that
[2446.82 --> 2447.60]  mutation as well.
[2447.60 --> 2448.74]  So it may not be every
[2448.74 --> 2449.78]  field in that object,
[2450.30 --> 2451.50]  but instead say, hey, I
[2451.50 --> 2453.00]  want, you can pass in
[2453.00 --> 2454.02]  this object, but really
[2454.02 --> 2455.00]  only these fields from
[2455.00 --> 2455.48]  this object.
[2456.16 --> 2456.54]  How would you do
[2456.54 --> 2457.08]  something like a
[2457.08 --> 2457.62]  delete then?
[2457.90 --> 2459.08]  Would you say, here's a
[2459.08 --> 2460.68]  mutation called delete
[2460.68 --> 2462.24]  post, and you call that
[2462.24 --> 2462.76]  mutation?
[2463.76 --> 2464.16]  Yep.
[2464.26 --> 2465.46]  If you look at the,
[2466.42 --> 2467.70]  once again, the GitHub
[2467.70 --> 2469.02]  API is a great public
[2469.02 --> 2469.96]  example, and it's super
[2469.96 --> 2470.62]  well documented.
[2471.12 --> 2473.12]  They have delete issue,
[2473.24 --> 2473.90]  delete issue comment,
[2474.06 --> 2474.82]  delete label, delete
[2474.82 --> 2475.68]  package version, delete
[2475.68 --> 2476.60]  project, delete project
[2476.60 --> 2477.52]  card, all of these are
[2477.52 --> 2479.32]  top level mutations that
[2479.32 --> 2480.06]  they expose.
[2481.10 --> 2481.84]  Do each of those then
[2481.84 --> 2483.76]  have, you're now going
[2483.76 --> 2484.62]  to assume that you
[2484.62 --> 2485.90]  understand how GitHub's
[2485.90 --> 2487.24]  backend works, but each
[2487.24 --> 2488.06]  of those has then a
[2488.06 --> 2489.58]  resolver that takes care
[2489.58 --> 2490.30]  of that functionality,
[2490.48 --> 2491.24]  some sort of function
[2491.24 --> 2492.20]  that lives somewhere that
[2492.20 --> 2493.58]  says delete this thing,
[2493.60 --> 2494.14]  and then it goes and
[2494.14 --> 2495.92]  make sure you can do
[2495.92 --> 2496.94]  that, and it has any
[2496.94 --> 2497.94]  sort of like background
[2497.94 --> 2498.70]  jobs that have to
[2498.70 --> 2499.44]  happen when that
[2499.44 --> 2501.14]  happens, and it resolves
[2501.14 --> 2502.84]  that, and is that how
[2502.84 --> 2503.92]  that works on the API
[2503.92 --> 2504.32]  side?
[2504.32 --> 2506.82]  Yeah, I think so.
[2507.20 --> 2508.38]  At a conceptual level, I'm
[2508.38 --> 2508.98]  sure there's details
[2508.98 --> 2509.60]  missing there.
[2510.16 --> 2511.00]  I'm sure there are, and
[2511.00 --> 2512.36]  there may be abstractions
[2512.36 --> 2513.36]  in there or whatever, but
[2513.36 --> 2514.74]  yeah, it's very, very
[2514.74 --> 2516.64]  explicit in terms of what
[2516.64 --> 2517.82]  changes are enabled and
[2517.82 --> 2518.12]  allowed.
[2518.88 --> 2520.74]  Is there a standard for
[2520.74 --> 2521.64]  like what gets returned
[2521.64 --> 2522.74]  from a mutation?
[2523.52 --> 2524.76]  Not that I'm aware of.
[2526.10 --> 2527.64]  So in the case of
[2527.64 --> 2530.38]  GitHub's, well, there's
[2530.38 --> 2533.26]  add star, delete team
[2533.26 --> 2533.76]  discussion.
[2535.28 --> 2536.62]  The input is the
[2536.62 --> 2537.50]  delete team discussion
[2537.50 --> 2538.44]  input, and the return
[2538.44 --> 2539.42]  fields is the client
[2539.42 --> 2540.64]  mutation ID, a unique
[2540.64 --> 2541.46]  identifier for the
[2541.46 --> 2542.46]  client performing the
[2542.46 --> 2542.92]  mutation.
[2544.78 --> 2547.14]  So probably a minimal
[2547.14 --> 2547.80]  response.
[2548.10 --> 2548.56]  It seemed like you'd
[2548.56 --> 2549.28]  have like a success or
[2549.28 --> 2550.04]  a failure kind of a
[2550.04 --> 2550.26]  thing.
[2550.78 --> 2552.10]  In this case, maybe if
[2552.10 --> 2553.04]  it's a success, they
[2553.04 --> 2553.80]  just return the client
[2553.80 --> 2554.10]  ID.
[2556.18 --> 2557.02]  I was trying to find
[2557.02 --> 2557.58]  delete star.
[2557.70 --> 2558.42]  I found add star.
[2560.10 --> 2561.60]  Delete issue returns
[2561.60 --> 2563.06]  two fields, the client
[2563.06 --> 2564.18]  mutation ID, which is
[2564.18 --> 2564.82]  the same as the other
[2564.82 --> 2565.50]  one, and the
[2565.50 --> 2567.18]  repository that the
[2567.18 --> 2568.28]  issue belonged to,
[2569.54 --> 2570.22]  which I assume is the
[2570.22 --> 2571.26]  entire object, not just
[2571.26 --> 2572.24]  the repository ID.
[2573.06 --> 2574.72]  So even amongst GitHub's
[2574.72 --> 2575.96]  responses, it seems
[2575.96 --> 2577.72]  they're consistent but not
[2577.72 --> 2578.86]  like identical.
[2580.84 --> 2581.84]  Depending on the delete.
[2582.66 --> 2583.42]  Yeah, I asked that and I
[2583.42 --> 2584.04]  was going to kind of ask
[2584.04 --> 2585.48]  about like error handling
[2585.48 --> 2587.02]  too, like if there's any
[2587.02 --> 2589.08]  kind of standard for that.
[2589.08 --> 2589.76]  And the reason I'm
[2589.76 --> 2591.80]  asking is like when you
[2591.80 --> 2592.88]  implement this, like
[2592.88 --> 2593.94]  Apollo, for example,
[2594.68 --> 2595.58]  would Apollo handle
[2595.58 --> 2597.10]  errors like on the
[2597.10 --> 2597.68]  client side different
[2597.68 --> 2598.66]  from like another
[2598.66 --> 2600.74]  library that you might be
[2600.74 --> 2601.60]  using to hit an Apollo
[2601.60 --> 2602.14]  back end?
[2602.74 --> 2603.36]  Is there some kind of
[2603.36 --> 2604.42]  standard that is followed
[2604.42 --> 2604.88]  or is it just
[2604.88 --> 2606.38]  abstractions all the way
[2606.38 --> 2607.46]  up or all the way
[2607.46 --> 2607.68]  down?
[2608.30 --> 2609.14]  That's a great question
[2609.14 --> 2611.44]  and I don't have the
[2611.44 --> 2613.02]  answer for you there.
[2613.46 --> 2615.00]  I feel like in Apollo what
[2615.00 --> 2616.74]  happens is it sends back
[2616.74 --> 2618.58]  essentially a message
[2618.58 --> 2619.28]  saying there was an
[2619.28 --> 2619.42]  error.
[2619.52 --> 2620.32]  Go check your GraphQL
[2620.32 --> 2620.72]  server.
[2621.66 --> 2622.42]  I don't remember.
[2623.28 --> 2625.22]  Like I don't know the
[2625.22 --> 2626.14]  top of my head and that
[2626.14 --> 2627.90]  definitely feels like a
[2627.90 --> 2630.18]  place where we have a
[2630.18 --> 2630.88]  little bit of a hole.
[2631.02 --> 2633.18]  One thing that is kind of
[2633.18 --> 2636.46]  odd is GraphQL will return
[2636.46 --> 2638.12]  a success code with an
[2638.12 --> 2640.18]  error message rather than it
[2640.18 --> 2641.38]  being an HTTP error.
[2642.96 --> 2643.44]  Interesting.
[2643.60 --> 2645.36]  So that's kind of funky.
[2645.36 --> 2647.14]  They're using HTTP as a
[2647.14 --> 2648.76]  transport layer not really
[2648.76 --> 2649.14]  as.
[2649.32 --> 2649.74]  Exactly.
[2650.14 --> 2650.54]  Yeah.
[2651.62 --> 2654.30]  In fact I think it may not
[2654.30 --> 2655.64]  even necessarily.
[2657.54 --> 2658.90]  I'm not sure that's part of
[2658.90 --> 2660.52]  the spec so much as that is
[2660.52 --> 2662.26]  just a common choice.
[2662.54 --> 2663.36]  I was going to say we have a
[2663.36 --> 2664.52]  transport layer it's called
[2664.52 --> 2665.02]  TCP.
[2666.62 --> 2668.24]  So it seems like HTTP would
[2668.24 --> 2670.94]  be superfluous in that use.
[2672.04 --> 2673.20]  Yeah but it makes it easy to
[2673.20 --> 2674.14]  build client side.
[2674.24 --> 2674.84]  It's pervasive.
[2674.84 --> 2676.38]  Interactions with it.
[2676.62 --> 2676.76]  Right.
[2676.84 --> 2677.98]  Like you want to be able to
[2677.98 --> 2679.60]  hit this thing from a
[2679.60 --> 2682.28]  browser and it's way easier
[2682.28 --> 2684.12]  to hit an HTTP based API
[2684.12 --> 2686.30]  than a TCP based API.
[2687.06 --> 2687.46]  Right.
[2687.58 --> 2688.62]  So real time follow up on
[2688.62 --> 2689.20]  the GitHub API.
[2689.40 --> 2690.14]  The reason I couldn't find
[2690.14 --> 2691.50]  delete star is there was not
[2691.50 --> 2691.74]  one.
[2691.84 --> 2693.06]  It's called remove star.
[2693.88 --> 2694.06]  Yep.
[2694.48 --> 2695.38]  And that's the delete
[2695.38 --> 2696.50]  function is that we remove.
[2696.88 --> 2697.62]  That's fun.
[2697.92 --> 2699.56]  So a little flexibility there
[2699.56 --> 2700.84]  because you know now they're
[2700.84 --> 2702.16]  more semantic like you don't
[2702.16 --> 2703.16]  do delete a star.
[2703.16 --> 2703.92]  Really.
[2704.44 --> 2705.94]  Well you just kind of remove
[2705.94 --> 2706.84]  the fact that you started
[2706.84 --> 2708.00]  that repo so they're being a
[2708.00 --> 2709.38]  little bit more descriptive
[2709.38 --> 2711.22]  but less discoverable because
[2711.22 --> 2712.46]  I'm everything else says
[2712.46 --> 2713.50]  delete and then it goes to
[2713.50 --> 2714.54]  start it says remove.
[2715.20 --> 2715.32]  Yep.
[2715.50 --> 2716.20]  What you want to bet those
[2716.20 --> 2717.14]  were implemented by different
[2717.14 --> 2718.86]  teams than the ones doing
[2718.86 --> 2719.90]  delete these things.
[2720.04 --> 2720.80]  There's a whole set that are
[2720.80 --> 2721.18]  removed.
[2721.30 --> 2722.14]  There's a whole set that are
[2722.14 --> 2724.88]  delete and maybe they have an
[2724.88 --> 2726.40]  internal consistency for which
[2726.40 --> 2727.32]  things but.
[2727.32 --> 2728.36]  Yeah.
[2729.00 --> 2730.52]  The fun of API design.
[2731.30 --> 2732.46]  So there's a cool question
[2732.46 --> 2733.54]  coming out of the chat room
[2733.54 --> 2734.28]  from Lars.
[2734.42 --> 2736.28]  Maybe one of you two can help
[2736.28 --> 2737.26]  him out.
[2737.94 --> 2739.20]  And he asks.
[2740.78 --> 2742.18]  Where do you learn the actual
[2742.18 --> 2742.84]  QL?
[2743.10 --> 2744.00]  Where do you learn the query
[2744.00 --> 2744.32]  language?
[2744.44 --> 2745.72]  What's the best resource for
[2745.72 --> 2746.68]  learning the query language?
[2747.50 --> 2748.62]  That's a great question.
[2749.06 --> 2750.16]  There's a.
[2750.16 --> 2753.48]  website called how to graph QL
[2753.48 --> 2756.62]  dot com that has sort of
[2756.62 --> 2757.94]  interactive tutorials and a
[2757.94 --> 2758.82]  bunch of stuff and I've heard
[2758.82 --> 2760.48]  folks talk about that as a
[2760.48 --> 2761.04]  good resource.
[2761.46 --> 2762.42]  I have not actually used it
[2762.42 --> 2763.18]  because I learned it all on
[2763.18 --> 2763.48]  the job.
[2764.12 --> 2765.40]  So I just kind of learned it
[2765.40 --> 2766.96]  by looking at the code that
[2766.96 --> 2769.24]  we had and then sitting
[2769.24 --> 2770.34]  developers down when I got
[2770.34 --> 2771.88]  stuck and be like what the
[2771.88 --> 2772.72]  heck is going on here?
[2772.80 --> 2773.86]  Can you explain this to me?
[2774.42 --> 2775.76]  But I've heard great things
[2775.76 --> 2777.46]  about how to graph QL dot com.
[2778.26 --> 2778.82]  Are you Nick?
[2778.82 --> 2780.56]  I will definitely check that
[2780.56 --> 2780.80]  out.
[2780.90 --> 2782.88]  But mine has also been on the
[2782.88 --> 2783.78]  job learning and kind of
[2783.78 --> 2785.34]  looking at other queries.
[2785.72 --> 2786.84]  But like I said, this is a
[2786.84 --> 2787.88]  proof of concept.
[2788.00 --> 2789.10]  So we don't really have like
[2789.10 --> 2791.14]  established queries lying
[2791.14 --> 2791.66]  around anywhere.
[2791.66 --> 2793.62]  So it's more just what have I
[2793.62 --> 2795.24]  typed into the graphical
[2795.24 --> 2795.88]  interface?
[2796.12 --> 2798.38]  And then I heavily rely on the
[2798.38 --> 2800.22]  control space to tell me what
[2800.22 --> 2802.34]  I can and can't do in this.
[2802.44 --> 2803.46]  And then it's like throwing
[2803.46 --> 2804.42]  spaghetti at the wall to see
[2804.42 --> 2804.92]  what sticks.
[2805.74 --> 2806.64]  Eventually it'll work.
[2806.88 --> 2808.18]  And you also got the up arrow.
[2808.18 --> 2809.20]  You know, you can go back to
[2809.20 --> 2809.64]  your history.
[2809.80 --> 2810.68]  What have I typed before?
[2811.14 --> 2811.46]  Up arrow.
[2811.56 --> 2811.84]  Up arrow.
[2811.84 --> 2812.08]  Up arrow.
[2812.78 --> 2813.82]  What's an arrow key?
[2814.54 --> 2814.82]  Sorry.
[2815.80 --> 2816.32]  L?
[2816.52 --> 2816.74]  J?
[2816.92 --> 2817.10]  K?
[2817.20 --> 2817.64]  I don't know.
[2817.88 --> 2818.02]  K.
[2818.56 --> 2818.90]  K.
[2819.72 --> 2820.08]  Okay.
[2823.54 --> 2825.56]  GraphQL dot org itself is also
[2825.56 --> 2826.12]  pretty good.
[2826.28 --> 2829.28]  It's got reasonable learn
[2829.28 --> 2831.02]  resources, though they also
[2831.02 --> 2832.54]  reference straight out to how
[2832.54 --> 2835.14]  to graph QL for doing tutorial
[2835.14 --> 2835.82]  related stuff.
[2835.82 --> 2837.76]  they've got a bunch of
[2837.76 --> 2839.46]  interesting things there.
[2839.96 --> 2841.12]  I will say that the query
[2841.12 --> 2842.58]  language itself is simple
[2842.58 --> 2844.06]  enough that everything I
[2844.06 --> 2845.56]  needed to know at the time
[2845.56 --> 2846.44]  that I was using it was
[2846.44 --> 2847.50]  basically just like clicking
[2847.50 --> 2849.92]  and seeing in the graphical
[2849.92 --> 2851.76]  editor the query that it
[2851.76 --> 2853.02]  generated based on what I was
[2853.02 --> 2853.72]  trying to do.
[2854.28 --> 2855.86]  And it's pretty straightforward
[2855.86 --> 2857.96]  to just copy and paste that
[2857.96 --> 2859.64]  around and tweak it.
[2860.24 --> 2861.12]  So I didn't feel like there was
[2861.12 --> 2862.84]  all that much to learn on that
[2862.84 --> 2863.82]  side, which is probably one of
[2863.82 --> 2865.54]  the reasons why it is so
[2865.54 --> 2866.94]  beloved by front enders and
[2866.94 --> 2867.82]  people who just want to get
[2867.82 --> 2868.92]  their data and get on with
[2868.92 --> 2870.04]  their day is that there's not
[2870.04 --> 2871.08]  too much to learn on the
[2871.08 --> 2872.06]  query side, on the
[2872.06 --> 2873.28]  implementation side and maybe
[2873.28 --> 2874.48]  on the mutation side as well.
[2874.88 --> 2875.30]  Not sure.
[2875.76 --> 2876.54]  Seems like there's a whole
[2876.54 --> 2877.36]  bunch there.
[2878.26 --> 2878.98]  But just the query language
[2878.98 --> 2879.80]  itself is pretty basic.
[2880.84 --> 2881.20]  Absolutely.
[2881.48 --> 2882.52]  Well, and I think that's one of
[2882.52 --> 2885.00]  the easy gotchas in GraphQL
[2885.00 --> 2887.06]  is folks will come in and
[2887.06 --> 2888.14]  particularly folks who are
[2888.14 --> 2889.18]  just on the front end side
[2889.18 --> 2889.96]  will come in and say, hey,
[2889.96 --> 2891.18]  this makes my life so much
[2891.18 --> 2891.54]  easier.
[2891.54 --> 2893.28]  We can just throw it in and
[2893.28 --> 2894.26]  it's going to make everything
[2894.26 --> 2894.68]  golden.
[2895.86 --> 2899.44]  And what I have seen having
[2899.44 --> 2901.08]  to do a lot of retrofitting
[2901.08 --> 2902.56]  work on the server side here
[2902.56 --> 2904.66]  is that that approach leads to
[2904.66 --> 2906.62]  catastrophically slow GraphQL
[2906.62 --> 2909.04]  servers and poorly designed
[2909.04 --> 2911.06]  schema and various other things.
[2911.96 --> 2914.24]  So this is a real domain.
[2914.42 --> 2916.64]  There are real concerns.
[2916.64 --> 2918.24]  And if you're creating that
[2918.24 --> 2919.90]  server side implementation,
[2919.90 --> 2923.26]  it's going to go a lot better
[2923.26 --> 2925.06]  if you have some understanding
[2925.06 --> 2926.12]  of your underlying data
[2926.12 --> 2927.42]  systems and how they work.
[2929.90 --> 2931.38]  One aspect of GraphQL we
[2931.38 --> 2932.16]  haven't brought up, which I
[2932.16 --> 2933.76]  think is the coolest use case
[2933.76 --> 2934.88]  of it so far is the way that
[2934.88 --> 2936.94]  Gatsby uses it to normalize all
[2936.94 --> 2938.54]  these disparate data sources into
[2938.54 --> 2942.12]  a single GraphQL usable thing.
[2942.12 --> 2943.78]  And I know there's a lot of
[2943.78 --> 2944.98]  complexity in those things.
[2945.02 --> 2945.98]  And of course, you could have,
[2946.58 --> 2947.46]  especially if you're spanning
[2947.46 --> 2948.82]  multiple data sources and stuff,
[2948.84 --> 2950.08]  it could get real hairy.
[2950.48 --> 2952.00]  But conceptually, I think that
[2952.00 --> 2952.92]  is super rad.
[2952.98 --> 2953.84]  I think it's the coolest thing
[2953.84 --> 2954.44]  about Gatsby.
[2955.18 --> 2956.18]  It is super cool.
[2956.20 --> 2958.46]  And it lets them create a
[2958.46 --> 2960.28]  dissociation between data source
[2960.28 --> 2962.94]  and accessing that data source.
[2963.02 --> 2964.54]  So all that you have to do to
[2964.54 --> 2965.80]  incorporate a new data source
[2965.80 --> 2967.30]  with a new way of interacting is
[2967.30 --> 2969.26]  you write something that knows
[2969.26 --> 2971.48]  how to translate from that to
[2971.48 --> 2971.94]  GraphQL.
[2972.74 --> 2977.06]  And then your client code just
[2977.06 --> 2978.78]  behaves in the same old way
[2978.78 --> 2979.76]  it's always behaved.
[2979.84 --> 2981.64]  And I think that is a really
[2981.64 --> 2982.46]  neat way to do it.
[2982.48 --> 2984.30]  And they do it at build time.
[2984.74 --> 2986.62]  But one could imagine doing that
[2986.62 --> 2988.22]  in real time, too, in that
[2988.22 --> 2989.20]  wrapping approach that I
[2989.20 --> 2990.90]  mentioned, where you wrap around
[2990.90 --> 2994.56]  all sorts of different APIs and
[2994.56 --> 2995.96]  provide a single consistent
[2995.96 --> 2996.84]  interface to them.
[2997.34 --> 2998.00]  You're not going to have me
[2998.00 --> 2998.94]  disagree with wrapping.
[2998.94 --> 3001.22]  Once again, GraphQL is the
[3001.22 --> 3002.08]  bacon that's going to make
[3002.08 --> 3003.16]  everything better.
[3003.84 --> 3005.58]  But if you're not careful, you'll
[3005.58 --> 3006.90]  get a little bit bloated if you
[3006.90 --> 3007.88]  have too much bacon.
[3009.32 --> 3012.24]  You don't know how much I've
[3012.24 --> 3014.58]  missed playing with these puns
[3014.58 --> 3015.66]  and metaphors with you all.
[3016.56 --> 3018.20]  One thing we didn't talk about was
[3018.20 --> 3019.74]  this concept of fragments, which I
[3019.74 --> 3021.70]  think is also quite interesting,
[3022.28 --> 3024.08]  particularly on the client side.
[3024.40 --> 3027.30]  So fragments allows you to
[3027.30 --> 3030.06]  essentially take sub pieces of a
[3030.06 --> 3033.04]  GraphQL query and treat them as
[3033.04 --> 3035.52]  their own individual queries, but
[3035.52 --> 3036.88]  then kind of roll them up so that
[3036.88 --> 3038.30]  you only do that one big query at
[3038.30 --> 3038.62]  the top.
[3038.74 --> 3041.66]  So in the code that I'm working
[3041.66 --> 3044.94]  with right now, each component
[3044.94 --> 3047.34]  thinks in its own set of data that
[3047.34 --> 3048.76]  it's going to run or that it's going
[3048.76 --> 3050.08]  to query and it writes a fragment.
[3050.08 --> 3053.54]  But then the top level page loads
[3053.54 --> 3055.40]  up all those fragments, composes them
[3055.40 --> 3057.48]  into a single query, and it only hits
[3057.48 --> 3058.30]  the API once.
[3058.30 --> 3062.62]  So it lets you, as a developer, think
[3062.62 --> 3064.62]  only about the data that you need for
[3064.62 --> 3066.14]  the piece that you're working on.
[3066.54 --> 3069.82]  But then from a performance
[3069.82 --> 3072.74]  standpoint, you can normalize all that.
[3072.82 --> 3074.04]  So you're doing a single query that's
[3074.04 --> 3076.24]  going to generate the info that you
[3076.24 --> 3078.02]  need and send that all at once to the
[3078.02 --> 3079.68]  server and get it all back right on
[3079.68 --> 3080.12]  page load.
[3080.82 --> 3082.60]  Another nice thing with fragments is
[3082.60 --> 3084.40]  that it will give you an interface
[3084.40 --> 3086.16]  name in TypeScript with like Apollo
[3086.16 --> 3088.26]  CodeGen, for example, that is the
[3088.26 --> 3088.98]  name of that fragment.
[3089.70 --> 3091.72]  So if you need to reference that type
[3091.72 --> 3094.70]  later, you easily have access to it
[3094.70 --> 3095.88]  and can pull it from there because
[3095.88 --> 3097.74]  otherwise it gives it some really
[3097.74 --> 3099.98]  funky name that's like whatever the
[3099.98 --> 3102.02]  query name is, underscore result.
[3102.18 --> 3103.54]  A lot of underscores in there, which
[3103.54 --> 3104.40]  looks ugly.
[3105.52 --> 3106.56]  So yeah, fragments are super
[3106.56 --> 3107.60]  interesting area.
[3107.84 --> 3109.98]  And there are tools like Relay, which
[3109.98 --> 3111.92]  will automatically roll up all those
[3111.92 --> 3113.60]  fragments, but it's also not super
[3113.60 --> 3117.00]  hard to kind of explicitly roll up
[3117.00 --> 3117.88]  and import your fragments.
[3118.24 --> 3120.00]  With that, I think we've covered a
[3120.00 --> 3121.80]  heck of a lot about GraphQL.
[3122.00 --> 3123.02]  Thank you for indulging me.
[3123.08 --> 3123.82]  This has been fun.
[3124.84 --> 3126.26]  We'll sign off till next week.
[3126.34 --> 3127.00]  Thank you, Jared.
[3127.22 --> 3127.62]  Thank you.
[3127.82 --> 3128.52]  Thank you, Nick.
[3129.18 --> 3130.76]  And the party will continue.
[3130.96 --> 3132.42]  Same time, same channel.
[3132.82 --> 3133.56]  Next week.
[3133.56 --> 3138.26]  What's your take on GraphQL?
[3138.60 --> 3140.38]  Are you all in or still skeptical?
[3140.74 --> 3141.96]  We'd love to hear your thoughts.
[3142.18 --> 3143.96]  You can comment on this and every
[3143.96 --> 3145.38]  episode on ChangeAll.com.
[3145.70 --> 3147.08]  There's a link in your show notes for
[3147.08 --> 3148.62]  easy clickings or just hit up
[3148.62 --> 3150.60]  ChangeAll.com in your browser du jour
[3150.60 --> 3152.28]  and let your voice be heard.
[3152.86 --> 3153.94]  Oh, and did you know we have an
[3153.94 --> 3154.82]  awesome weekly newsletter?
[3155.12 --> 3157.40]  Over 15,000 devs just like yourself
[3157.40 --> 3159.16]  hit the easy button on keeping up with
[3159.16 --> 3160.94]  what's fresh and new in the software
[3160.94 --> 3161.34]  world.
[3161.34 --> 3163.34]  We include the hottest repos, the best
[3163.34 --> 3164.96]  articles, and the biggest news with
[3164.96 --> 3166.82]  just enough commentary to add context
[3166.82 --> 3167.68]  and nerdy jokes.
[3167.88 --> 3169.12]  But not so much that you're overwhelmed.
[3169.52 --> 3170.94]  Check it out at ChangeAll.com slash
[3170.94 --> 3171.26]  weekly.
[3171.44 --> 3172.30]  I think you'll dig it.
[3172.50 --> 3173.94]  Thanks to K-Ball for emceeing once
[3173.94 --> 3175.76]  again, Nick Neesey for bringing his
[3175.76 --> 3177.96]  wizardry, BMC for the beats, and our
[3177.96 --> 3180.02]  sponsors for making it all possible.
[3180.50 --> 3182.26]  Shout out to Fastly, Linode, and
[3182.26 --> 3182.68]  Rollbar.
[3183.00 --> 3184.10]  That's all for now.
[3184.54 --> 3186.12]  Framework Wars next week.
[3191.34 --> 3198.70]  Clap your hands, everybody, if you've got
[3198.70 --> 3199.80]  what it takes.
[3200.04 --> 3201.96]  Because I'm Curtis Blow, and I want you
[3201.96 --> 3204.24]  to know that these are the boys.
[3205.56 --> 3207.14]  Well, we're happy to have you back, and
[3207.14 --> 3208.84]  in the limited capacity that we have,
[3208.88 --> 3210.48]  we'll take whatever K-Ball we can get.
[3211.08 --> 3213.02]  I did already drink quite a few cups
[3213.02 --> 3214.34]  this morning, so...
[3214.34 --> 3217.44]  Nick actually tried to code up an
[3217.44 --> 3219.02]  auto-generated K-Ball, but it didn't
[3219.02 --> 3220.28]  work out like we thought it would.
[3221.22 --> 3222.68]  Ooh, I want to hear more about that.
[3223.46 --> 3224.72]  Well, you can't, because I just made
[3224.72 --> 3225.00]  it up.
[3225.90 --> 3227.34]  Nick, tell them more about the K-Ball
[3227.34 --> 3227.96]  you tried to write.
[3228.96 --> 3230.98]  Well, it's just layers of
[3230.98 --> 3232.34]  abstractions, and then...
[3232.34 --> 3235.78]  If you obstruct anything enough, you
[3235.78 --> 3237.04]  eventually just end up talking about
[3237.04 --> 3238.34]  Vim with me, so...
[3239.06 --> 3240.56]  Yeah, well, you know, now we can hang
[3240.56 --> 3241.84]  out and talk TypeScript, too, because
[3241.84 --> 3242.78]  I've been in that world a lot.
[3242.78 --> 3244.08]  Yeah, that is...
[3244.08 --> 3247.00]  Anyway, we should probably get back
[3247.00 --> 3247.14]  to...
[3247.14 --> 3247.90]  I'll see myself out.
[3247.96 --> 3248.94]  Slowly, everyone's gonna...
[3248.94 --> 3249.28]  Hey!
[3250.60 --> 3250.80]  ...
[3250.80 --> 3251.26]  ...
[3251.26 --> 3251.54]  ...
[3251.54 --> 3251.88]  ...
[3251.88 --> 3251.96]  ...
