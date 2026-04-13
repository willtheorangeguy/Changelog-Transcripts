[0.00 --> 4.60]  As we look forward, we've been talking for years about kind of AI everywhere and IoT
[4.60 --> 9.38]  everywhere, Internet of Things everywhere, and all of the things, and that there's a
[9.38 --> 13.60]  sense of scale in the future that we may not have had in the past.
[13.60 --> 20.60]  That presents a fairly substantial logistical challenge to get all of that data from all
[20.60 --> 25.92]  of those different places to all the other places together and have a coordinated system
[25.92 --> 27.60]  that provides the services.
[27.60 --> 30.88]  So data fabric, it's the trucking system of data.
[31.00 --> 32.02]  It's not the sexy part.
[35.80 --> 37.08]  Hey, Jared here.
[37.58 --> 41.88]  One of the things we can count on in the software industry is change.
[42.50 --> 47.18]  The state of the art changes so fast, in fact, that keeping up can feel like a whole other
[47.18 --> 49.12]  job on top of your actual job.
[49.90 --> 51.98]  That's why we created Change Log Weekly.
[52.56 --> 56.88]  It's our totally free newsletter that we drop in your inbox each and every Sunday.
[57.60 --> 62.46]  We link to the latest news, the best articles, and the most interesting projects that you
[62.46 --> 63.14]  should be aware of.
[63.82 --> 68.36]  We also add a little commentary from us saying why something's important, pointing you to
[68.36 --> 71.88]  other instances of a trend, or just making a dorky joke to keep it lively.
[72.46 --> 77.42]  So if you haven't yet, I recommend subscribing to Change Log Weekly and help us help you keep
[77.42 --> 78.04]  up with the latest.
[78.04 --> 82.22]  Head to Change Log.com slash weekly and sign up today.
[82.42 --> 85.00]  Again, it's totally free and we never spam you.
[85.14 --> 85.46]  Yuck.
[86.34 --> 89.84]  One last time, that's Change Log.com slash weekly.
[89.84 --> 108.48]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[108.48 --> 110.12]  and accessible to everyone.
[110.48 --> 114.78]  This is where conversations around AI, machine learning, and data science happen.
[114.78 --> 120.52]  Join us at practicalai.fm slash community and follow the show on Twitter.
[120.74 --> 122.70]  We're at Practical AI FM.
[123.12 --> 127.76]  Thank you to our partners at Fastly for shipping our pods super fast all around the world.
[127.98 --> 129.82]  Check them out at fastly.com.
[136.00 --> 141.06]  Welcome to another fully connected episode of the Practical AI podcast.
[141.06 --> 146.38]  In these episodes, Chris and I keep you fully connected with everything that's happening
[146.38 --> 147.46]  in the AI community.
[147.76 --> 153.72]  We'll take some time to discuss some of the latest AI news and trends, and we'll dig into
[153.72 --> 157.12]  a couple of learning resources to help you level up your machine learning game.
[157.70 --> 159.34]  This is Daniel Whitenack.
[159.44 --> 165.20]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson,
[165.48 --> 168.16]  who is a tech strategist at Lockheed Martin.
[168.78 --> 169.40]  How are you doing, Chris?
[169.40 --> 170.96]  I am doing very well.
[171.12 --> 175.42]  It's kind of the end of winter as we're recording this, starting to warm up a little bit.
[175.56 --> 180.28]  Got to say, my heart is with the people of Ukraine right now, because we're about two
[180.28 --> 186.52]  weeks into that event as we record this today, and spending a lot of my spear cycles just
[186.52 --> 188.12]  thinking about those folks.
[188.38 --> 189.14]  Yeah, definitely.
[189.54 --> 190.02]  Yes.
[190.06 --> 195.98]  For those listening at a later date, we are in the midst of a world crisis over in the
[195.98 --> 197.74]  Ukraine and war over there.
[197.74 --> 201.66]  So, yeah, it's definitely on a lot of people's minds.
[202.40 --> 208.40]  And I know we have, of course, SIL has partners all around the world and definitely, yeah,
[208.82 --> 214.88]  just really concerned and praying for those involved in really tough situations.
[215.30 --> 216.14]  So, yeah.
[216.26 --> 223.74]  It seems like in recent years, it's just like from one giant global craziness to the next,
[223.86 --> 224.18]  really.
[224.18 --> 225.20]  It has been.
[225.28 --> 230.08]  We've had a string of them, it seems like, with the pandemic being the giant global thing
[230.08 --> 230.82]  in the middle of it.
[230.88 --> 233.30]  But we've rolled right out into this.
[233.50 --> 236.78]  And I didn't want to make the beginning of the show all about this, because that's not
[236.78 --> 238.48]  what our folks are here to talk about.
[239.02 --> 241.50]  But just our hearts are with those folks.
[241.90 --> 247.66]  And I know we have some folks listening to us from that part of the world, and we're thinking
[247.66 --> 248.02]  about you.
[248.02 --> 248.20]  Yeah.
[248.42 --> 248.78]  Hang in there.
[248.78 --> 249.58]  Yeah, hang in there.
[249.70 --> 254.64]  And it's not totally disconnected from the subject in that hopefully over the coming years,
[254.64 --> 264.48]  we can find more and more ways to apply technology and AI to really be helpful and beneficial in
[264.48 --> 265.38]  these situations.
[265.38 --> 273.70]  So not just used as a tool to give concentrated power to one party or another, but actually
[273.70 --> 276.82]  to sort of democratize good things.
[276.98 --> 283.36]  I know in recent weeks, we've had several different conversations about kind of geospatial
[283.36 --> 289.68]  data and satellite imagery and opening that up to people that could use it in multiple
[289.68 --> 290.22]  ways.
[290.22 --> 295.50]  And I think we talked about some of that in relation to kind of dealing with tropical storms
[295.50 --> 299.90]  or disasters, but of course, kind of wartime situations and the aftermath.
[299.90 --> 307.66]  It seems like a definite overlap with that general set of data and tasks is maybe, you
[307.66 --> 313.52]  know, I'm sure that there are people out there thinking about how we can, as maybe AI practitioners
[313.52 --> 320.30]  work to provide, whether it's open data or open models to help in these sorts of situations.
[320.30 --> 324.44]  If you have any ideas or you know people working in those areas, let us know.
[324.50 --> 325.54]  We'd love to have them on the show.
[325.94 --> 326.34]  Absolutely.
[326.80 --> 331.72]  And getting technology out there into the hands of folks who really need it.
[331.96 --> 333.90]  And in a lot of cases, it doesn't yet.
[334.00 --> 336.26]  And that's a big problem for us all to solve.
[336.38 --> 336.54]  Yeah.
[336.84 --> 341.92]  And actually, there may be some part of today's conversation can kind of help us along that
[341.92 --> 342.28]  path.
[342.66 --> 349.36]  There's a lot of context that this conversation could be had in to avoid conflict of interest
[349.36 --> 350.98]  because I'm in the defense industry.
[351.12 --> 356.94]  I'm not going to talk about it in the context of war and conflict, but we wanted to talk
[356.94 --> 359.16]  a little bit about some of the logistics of data.
[359.36 --> 364.14]  And probably I think the use case I've picked to start us off with at least is maybe kind
[364.14 --> 365.04]  of talking about healthcare.
[365.04 --> 368.34]  And I'm going to do this as a non-expert in healthcare.
[368.90 --> 369.36]  And you too?
[369.86 --> 371.82]  Neither of us are medical doctors.
[372.46 --> 372.90]  Yeah.
[373.04 --> 377.74]  I wanted to talk a little bit about moving data around where it needs to be because that
[377.74 --> 380.56]  could be applied to just about any industry on the planet.
[380.76 --> 382.28]  And it's a need that everybody has.
[382.84 --> 388.92]  And there's a popular buzzword that goes with this these days, which is data fabric.
[389.20 --> 389.32]  Yeah.
[389.36 --> 395.80]  It seems like there's just so many terms like data, this data, like we've got data lake,
[396.02 --> 399.02]  data warehouse, data mart, data fabric.
[399.78 --> 405.30]  I don't know what, there's probably other things out there like data bodega, data hot dog
[405.30 --> 405.66]  stand.
[405.88 --> 409.44]  I don't know what the other things out there are.
[409.44 --> 411.46]  Maybe we need a data dictionary.
[411.84 --> 412.50]  But yeah.
[413.46 --> 413.90]  Yeah.
[414.04 --> 419.50]  I mean, I know we're going to be talking about data fabric or like what people mean when they
[419.50 --> 420.12]  say that.
[420.34 --> 426.14]  Maybe before we go there, would it be useful to maybe just differentiate it from a couple
[426.14 --> 429.08]  of these other terms that people have in mind?
[429.22 --> 429.92]  I think so.
[430.10 --> 434.20]  One thing I have discovered, just like in the early days, we used to say this in the early
[434.20 --> 439.10]  episodes for those who have been with us for a long time, that many people define AI in
[439.10 --> 440.06]  many different ways.
[440.06 --> 440.26]  Yeah.
[440.36 --> 444.62]  And maybe that has coalesced a little bit around deep learning more recently.
[444.62 --> 448.44]  I think that there's more of an understanding about what we're talking about when we say
[448.44 --> 448.74]  AI.
[448.88 --> 454.68]  But just in the same way, I'm discovering that data fabrics have many different definitions
[454.68 --> 456.10]  from many different people.
[456.38 --> 459.18]  So I'm going to offer my definition.
[459.18 --> 459.54]  Cool.
[459.82 --> 460.66]  Add it to the mix.
[460.66 --> 463.02]  Add it to the mix there and we can see.
[463.34 --> 468.56]  So for me, I'm just like I did with AI way back when we were talking about that topic
[468.56 --> 470.80]  in one of our fully connected episodes.
[471.00 --> 474.28]  I define data fabric fairly narrowly.
[474.32 --> 481.10]  And I try not to encompass all those other data star terms that we have pointed out exist.
[481.10 --> 487.12]  So if you think of a fabric being something that you lay down, like a physical fabric being
[487.12 --> 491.58]  something that you lay down across something, across a small geography.
[491.84 --> 492.44]  Curtain or blanket.
[492.72 --> 494.80]  A curtain or blanket's a perfect example.
[494.94 --> 496.92]  And it kind of covers those things.
[496.92 --> 499.04]  And to some degree, it connects those things.
[499.04 --> 508.22]  And so playing off that analogy, I would say that a data fabric is a way of getting data
[508.22 --> 515.44]  from data producers, points of origin, to all of the consumers of that data, a destination,
[515.68 --> 516.84]  one or more destinations.
[516.84 --> 523.10]  And it may be across a very diverse digital landscape on how you do that.
[523.14 --> 528.32]  And with technologies of different types, different generations, completely different
[528.32 --> 529.14]  architectures.
[529.84 --> 537.76]  And a data fabric's purpose is to make the data go from point A to point B in a timely manner
[537.76 --> 544.30]  with performance guarantees and ensuring arrivals so that you can do productive things with
[544.30 --> 549.24]  that data at whatever the consumer of that data is trying to do with that data.
[549.68 --> 552.20]  So it's a logistical thing.
[552.42 --> 559.64]  Another analogy might be thinking about trains moving across the landscape or highway systems
[559.64 --> 564.94]  with large trucks moving goods and services all over the place, getting them where they
[564.94 --> 566.32]  need to be to all the...
[566.32 --> 569.76]  They may start at one place, but they may move those goods and services around.
[569.94 --> 574.44]  And so I think that is also a decent analogy for what a data fabric should do.
[574.84 --> 580.24]  So I guess one question would be like, initially, when I got into data science, I had my first
[580.24 --> 588.12]  position as a data scientist working with data that was in a SQL database.
[588.12 --> 594.58]  To me, in that scenario, my sort of pattern of access to that data was with SQL queries.
[594.58 --> 603.20]  Where does the data fabric sit in as you sort of scale maybe all the people that need access to
[603.20 --> 603.80]  data?
[604.58 --> 608.24]  Like, are we talking about just SQL queries or does this go beyond that?
[608.38 --> 609.52]  I imagine it does.
[610.14 --> 612.16]  I think it goes way beyond that.
[612.24 --> 614.10]  It can be inclusive of that, maybe.
[614.10 --> 619.88]  But if you think about historically with us, you know, all of us will running with that
[619.88 --> 620.72]  SQL example.
[620.72 --> 625.86]  We have a SQL database and we make queries to it and we're pushing data into it and we're
[625.86 --> 629.08]  pulling data out of it and we're running analytics on it and we're transforming it.
[629.08 --> 634.72]  But it's all within a very local context there.
[635.24 --> 639.98]  And I think as we look forward, we've been talking for years about kind of AI everywhere
[639.98 --> 646.16]  and IoT everywhere, Internet of Things everywhere, and all of the things and that there's a sense
[646.16 --> 650.12]  of scale in the future that we may not have had in the past.
[650.12 --> 659.10]  And so that presents a fairly substantial logistical challenge to get all of that data from all of
[659.10 --> 664.98]  those different places to all the other places together and have a coordinated system that
[664.98 --> 666.12]  provides the services.
[666.42 --> 669.62]  So a data fabric is really a big software system.
[669.66 --> 670.36]  It's what it is.
[670.36 --> 676.06]  A big distributed software system and potentially globally distributed depending on how you're
[676.06 --> 676.92]  using it.
[676.92 --> 679.90]  And so it's the trucking system of data.
[680.04 --> 681.06]  It's not the sexy part.
[681.46 --> 683.30]  It's not the thing we like to talk about in AI.
[683.94 --> 687.68]  But one thing, and I know this has come up in a whole bunch of conversations that we've
[687.68 --> 692.90]  had on this show, both with guests and just ourselves, is that there's a lot of underlying
[692.90 --> 698.36]  work to get data ready and to the right place and such so that you can use it for your AI.
[698.68 --> 703.38]  And then you have the AI modeling process, which is a very small percentage of the overall
[703.38 --> 704.00]  process.
[704.18 --> 706.46]  And then it has to get deployed out and all this stuff.
[706.46 --> 711.96]  And a data fabric covers just the part of that of getting the data to the right place
[711.96 --> 715.18]  so that you can do something presumably useful and productive with it.
[715.32 --> 715.44]  Yeah.
[715.58 --> 719.98]  I was just having over the past couple of weeks, having some discussions with another
[719.98 --> 726.28]  colleague at SAL talking about how we think about the products or the things that we build
[726.28 --> 731.04]  more in terms of like the outcomes we're trying to achieve with those things.
[731.04 --> 737.58]  So if I was to spin this a different way, like how would I know if I had a data fabric?
[737.84 --> 743.52]  Like what would the outcome be in terms of the way teams would operate or interact with
[743.52 --> 743.76]  that?
[744.54 --> 748.56]  So kind of thinking about characteristics that make up the data fabric to some degree?
[748.70 --> 748.72]  Yeah.
[748.72 --> 753.46]  Like if I went into a new company and I was trying to figure out if they did or didn't
[753.46 --> 759.52]  have a data fabric yet, or maybe they were just stuck in the old days with like random,
[759.76 --> 761.98]  you know, other systems around.
[761.98 --> 765.78]  How would I determine like, yes, they do or no, they don't?
[765.96 --> 773.52]  I would say if they do, they probably have a specific software architecture, a system that
[773.52 --> 775.62]  is designed to move data around.
[775.96 --> 782.88]  And I think a notable thing about that system is it is highly scalable and is designed to
[782.88 --> 788.32]  handle in number of endpoints in being any number that you choose to apply to that.
[788.32 --> 794.94]  And that the architecture fundamentally is able to support the addition and loss of endpoints
[794.94 --> 798.78]  as a standard operating procedure in it without it.
[798.90 --> 800.16]  That's not a remarkable thing.
[800.26 --> 805.20]  And you're not manually setting up connections to SQL servers, you know, constantly and that
[805.20 --> 805.64]  kind of thing.
[806.00 --> 813.94]  So you're able to take an endpoint, maybe an IoT device out there or some end user, maybe
[813.94 --> 817.52]  a tablet computer if you're in a hospital might be another case.
[817.52 --> 823.58]  And it just plugs into your data architecture and might work with many SQL databases and
[823.58 --> 828.90]  many other systems out there aggregating the data in the right places and making it available
[828.90 --> 830.42]  for use for there.
[830.50 --> 836.24]  And it's a software system designed to handle all of that complexity under the hood, or maybe
[836.24 --> 838.42]  I'll say under the blanket or something, you know, here.
[839.10 --> 839.40]  Nice.
[839.40 --> 845.80]  I ask all that, I guess, just to try to, because when you were first like, hey, let's, let's
[845.80 --> 847.18]  talk about data fabric.
[847.40 --> 851.16]  I was like, well, I want to know a little bit of what that means.
[851.16 --> 853.98]  So I kind of tried to learn a little bit.
[854.24 --> 856.80]  And the Google searching was not that helpful.
[857.04 --> 862.64]  So like, I went to Gartner, which they always give a definition, right?
[862.64 --> 867.14]  And their definition, I'm not saying anything bad about the person who made this definition.
[867.14 --> 871.52]  It's probably really, you know, strategically worded or whatever.
[872.24 --> 879.32]  But it says a data fabric utilizes continuous analytics, a new term I didn't know either.
[879.80 --> 880.58]  Continuous analytics.
[880.58 --> 889.30]  Continuous analytics over existing discoverable and inferenced metadata assets to support the
[889.30 --> 898.02]  design, deployment, and utilization of integrated and reusable data across all environments, including
[898.02 --> 900.10]  hybrid and multi-cloud platforms.
[900.86 --> 902.48]  There's a lot of words there.
[902.72 --> 903.74]  There's a lot of words there.
[903.82 --> 905.98]  And I agree with many of the words.
[905.98 --> 911.96]  But one of the things I'll call out, or it's my own bias, but I think I'm right, obviously,
[912.22 --> 915.42]  is the, I believe analytics is a separate thing.
[915.54 --> 922.92]  I believe analytics are, systems are consumers of and producers for, you know, a larger environment
[922.92 --> 925.02]  where a data fabric may be serving that.
[925.34 --> 929.44]  But to me, that is a use case that a data fabric serves.
[929.44 --> 935.94]  And I have seen many people try to describe data fabrics in terms of analytics and being the
[935.94 --> 937.90]  digital bully that I am.
[938.16 --> 939.64]  I tell them they're wrong.
[939.98 --> 940.90]  They're wrong.
[941.10 --> 941.98]  It's not that.
[942.08 --> 942.98]  It's about the logistics.
[959.38 --> 963.58]  I'm Jared Santo, GoTimes producer and a loyal listener of the show.
[963.58 --> 968.12]  This is the podcast for diverse discussions from around the Go community.
[968.62 --> 972.02]  GoTimes panel hosts special guests like Kelsey Hightower.
[972.74 --> 977.64]  And sometimes you can leverage a cloud provider and make margins on top.
[977.74 --> 978.92]  That's just good business.
[979.36 --> 983.02]  But when we're at the helm making the decision, we're like, yo, forget good business.
[983.52 --> 987.80]  I'm about to deploy Kafka to process 25 messages a year.
[988.76 --> 990.54]  It's nerd pride, right?
[990.54 --> 993.82]  Picks the brains of the Go team at Google.
[994.26 --> 998.12]  You don't get a good design by just grabbing features from other languages and gluing them
[998.12 --> 998.46]  together.
[999.14 --> 1003.22]  Instead, we tried to build a coherent model for the language where all the pieces worked
[1003.22 --> 1003.94]  in concert.
[1004.60 --> 1007.54]  Shares their expertise from years in the industry.
[1008.10 --> 1009.78]  Don't expect to get it right from the start.
[1010.02 --> 1011.36]  You'll almost definitely get it wrong.
[1011.44 --> 1013.46]  You'll almost definitely have to go back and change some things.
[1013.46 --> 1016.78]  So yeah, I think it goes back to what Peter said at the start, which is just make your
[1016.78 --> 1020.76]  code, write your code in a way that is easy to change and then just don't be afraid to
[1020.76 --> 1021.24]  change it.
[1021.64 --> 1024.20]  And has an absolute riot along the way.
[1024.78 --> 1024.92]  Yeah.
[1024.96 --> 1028.56]  You know that little small voice in your head that tells you not to say things?
[1029.26 --> 1030.24]  What is that?
[1031.08 --> 1032.04]  How do you get one?
[1033.68 --> 1034.56]  You want one of those?
[1034.68 --> 1035.68]  Is it like an in-app purchase?
[1036.54 --> 1038.00]  It is go time.
[1038.40 --> 1040.26]  Please select a recent episode.
[1040.48 --> 1042.16]  Give it a listen and subscribe today.
[1042.16 --> 1043.84]  We'd love to have you with us.
[1057.90 --> 1062.94]  So Chris, I think I'm getting what you're saying in that like in this definition or the
[1062.94 --> 1069.30]  definition we were talking about from Gardner, analytics sort of serves as a potential kind
[1069.30 --> 1074.58]  of plug-in application to whatever we're calling data fabric.
[1075.24 --> 1076.66]  And then they describe this.
[1076.96 --> 1082.44]  So it's operating over and they're describing it as existing discoverable and inferenced metadata
[1082.44 --> 1083.14]  assets.
[1083.44 --> 1085.16]  That's a mouthful.
[1085.54 --> 1085.88]  It is.
[1085.88 --> 1094.30]  So metadata assets, I assume just means like data telling you what assets are available
[1094.30 --> 1100.10]  or the kind and number and type or like what's the metadata?
[1100.72 --> 1105.12]  So I'm going to define metadata in the context of a data fabric.
[1105.22 --> 1109.28]  Meaning if you're talking about metadata in a different context, you might take it slightly
[1109.28 --> 1109.60]  different.
[1109.60 --> 1114.46]  But I would always define metadata in the context of the thing that you're discussing because
[1114.46 --> 1115.82]  it's meta relative to that.
[1116.12 --> 1118.52]  I like how you're weaving these things together.
[1118.82 --> 1119.98]  Oh, God.
[1120.18 --> 1121.20]  Oh, that was a bad one.
[1121.26 --> 1122.32]  That was even worse than mine.
[1122.80 --> 1124.38]  I hope folks are still with us.
[1124.86 --> 1132.50]  So I would think of metadata as being the metadata around the data, which are the messages you're
[1132.50 --> 1133.06]  moving around.
[1133.06 --> 1139.66]  So if you use the word messages to say I'm moving data from one physical place to another
[1139.66 --> 1146.12]  one or one digital place to another one, and there are things that I care about regarding
[1146.12 --> 1152.16]  that data in the message, such as the security status of that data, you know, what, you know,
[1152.50 --> 1153.96]  and that can be a lot of different things.
[1153.96 --> 1156.00]  The routing information of that data.
[1156.26 --> 1157.34]  Who can access it.
[1157.50 --> 1158.08]  Yeah, exactly.
[1158.20 --> 1163.04]  All those things, the there's a whole bunch of things where you could that metadata
[1163.04 --> 1165.20]  it could be in the form of tags.
[1165.36 --> 1167.78]  It could be addressing prioritization.
[1168.18 --> 1171.72]  It could be addressing, you know, recipients priorities.
[1172.14 --> 1176.84]  It may be that your data fabric is overwhelmed with the amount of data that moves through in
[1176.84 --> 1181.00]  your and you're having to make you have a service in your data fabric that is having
[1181.00 --> 1187.92]  to prioritize those data packets based on your needs that you have informed in one mechanism
[1187.92 --> 1189.24]  or another, the data fabric of.
[1189.24 --> 1195.46]  So there's all these metadata bits that are being attached to the data you're moving around.
[1195.72 --> 1201.04]  But having said that, what the data is, the primary data that you're moving from a producer
[1201.04 --> 1204.50]  to the consumers, you don't really care about in the data fabric.
[1204.50 --> 1209.90]  Other than the fact that you've attached those tags of characteristics and things that you care
[1209.90 --> 1211.18]  about that we just described.
[1211.18 --> 1216.68]  You're just moving it from one place to another and ensuring, providing guarantees that based
[1216.68 --> 1221.50]  on your priority and the importance and stuff like that that you've assigned, that it's fulfilling
[1221.50 --> 1222.52]  that promise.
[1222.98 --> 1229.46]  So you mentioned sort of moving and like message, moving messages around and packets around and
[1229.46 --> 1232.12]  such operations like that.
[1232.12 --> 1236.70]  So let's let's cut if we bring it down to like the health care use case you were kind
[1236.70 --> 1237.28]  of proposing.
[1237.28 --> 1243.64]  Let's say, yeah, let's say I'm a data scientist and I'm creating a new model to parse health
[1243.64 --> 1245.42]  care records or something like that.
[1245.54 --> 1245.64]  Right.
[1245.72 --> 1245.92]  Yes.
[1246.12 --> 1251.68]  And let's say there's an S3 bucket over here or something and it includes some health care
[1251.68 --> 1259.16]  records and there's metadata attached to it and it gets moved from like there to somewhere
[1259.16 --> 1259.38]  else.
[1259.46 --> 1262.28]  What's special about the the moving part?
[1262.54 --> 1267.34]  Like if I have the metadata about like where it is and I know where it is and what's in
[1267.34 --> 1274.66]  it and who can access it, why is this sort of distributed or movement of data piece?
[1274.66 --> 1279.18]  Why is that like a key piece of of what you're you're kind of describing?
[1279.58 --> 1283.76]  It may be that you don't really have a requirement for a data fabric if it's fairly basic.
[1283.76 --> 1289.36]  If you're basically saying there is one producer and there's one consumer and you don't have
[1289.36 --> 1295.10]  really an enormous number of them, you don't have thousands or millions of instances of a
[1295.10 --> 1295.98]  producer and a consumer.
[1296.26 --> 1300.84]  So you're saying part of this would come in where let's say I had a thousand hospitals
[1300.84 --> 1308.62]  and they were all pushing records into, let's say, separate buckets or maybe even like
[1308.62 --> 1314.32]  a mix of on-premises file storage NFS or something and and S3.
[1314.52 --> 1315.76]  Is that is that more?
[1316.40 --> 1318.40]  Yeah, I think the scale matters.
[1318.68 --> 1322.84]  There is a cost implementing a data fabric and that cost is not trivial.
[1322.84 --> 1325.88]  And therefore, there is a level of requirement.
[1325.88 --> 1332.06]  There is a level of need that should be in place to substantiate paying that cost and recognizing
[1332.06 --> 1338.64]  that above a certain scale of operation, the data fabric is saving you cost over the long
[1338.64 --> 1340.52]  haul versus producing more.
[1340.52 --> 1348.48]  So the point with the data fabric is that at some point, the automation of all that becomes
[1348.48 --> 1350.22]  a cost effective solution.
[1350.46 --> 1356.40]  But if your needs are very low or minute in terms of what you need, you may not want to
[1356.40 --> 1357.98]  deploy a data fabric to cover that.
[1357.98 --> 1363.28]  If it's a very small operation, manually centering everything up might make more sense in a small
[1363.28 --> 1363.76]  operation.
[1363.76 --> 1369.52]  Whereas if you're dealing with millions or let's say thousands of data producers, well,
[1369.54 --> 1371.12]  it might be millions actually going forward.
[1371.24 --> 1376.82]  And you also might have millions of consumers of that data that becomes untenable, obviously,
[1376.82 --> 1381.40]  to try to do all that in a very by the connection mechanism.
[1381.40 --> 1388.16]  So you need a system that can handle that at that massive parallel and concurrent scale.
[1388.68 --> 1393.00]  So you know me, I always try to get down to the distill the practical.
[1393.38 --> 1399.36]  So if I get what you're saying, let's say we have the scenario where we have thousands of
[1399.36 --> 1399.96]  hospitals.
[1400.32 --> 1407.42]  All of those are producing medical records, which in and of themselves have security issues
[1407.42 --> 1408.98]  and things attached to them.
[1408.98 --> 1415.72]  But then they're stored in, let's say, S3 or mix of NFS or sort of a diversity of sources.
[1416.24 --> 1417.28]  So those are my producers.
[1417.58 --> 1421.64]  And then up at my consumers, I have maybe a few different things.
[1421.64 --> 1427.04]  I have like hospital web apps or something for staff members to access records.
[1427.24 --> 1433.98]  And then I have like a team of data scientists internally that's building like models to maybe
[1433.98 --> 1436.92]  parse those records automatically in a better way.
[1436.92 --> 1445.50]  And then I have a third group of maybe researchers who are researching like a certain disease or
[1445.50 --> 1451.96]  effect of a trial or something within a certain certain set of those records right across different
[1451.96 --> 1452.28]  places.
[1452.28 --> 1454.04]  So in between those people.
[1454.04 --> 1459.00]  So I've got on the one side, the data on the other side, I've got these different consumers
[1459.00 --> 1460.84]  sort of in the middle.
[1460.84 --> 1468.84]  If I put a quote fabric there, the things that would need to happen or each of those people
[1468.84 --> 1474.06]  would need to efficiently get the data that they need, regardless of what it's stored in.
[1474.06 --> 1480.68]  And they would need to be authenticated against that data and understand in a sort of like
[1480.68 --> 1486.22]  metadata way where all of the right pieces of data are located.
[1486.22 --> 1491.40]  So the data fabric would sort of do that in a metadata kind of protocol between the consumers
[1491.40 --> 1494.58]  and the data and make that process efficient.
[1494.74 --> 1495.98]  Am I sort of getting there?
[1496.38 --> 1499.34]  I would argue you're getting there, but I'll actually, I want to throw in a couple of things
[1499.34 --> 1503.94]  that make it, that would raise the value proposition of applying a data fabric.
[1504.14 --> 1509.18]  You mentioned the fact that these, all these, these producers, the actual machines or whatever
[1509.18 --> 1511.40]  are going to S3 as an example.
[1511.40 --> 1517.88]  But what I would argue is the use cases that you described in the example, none of those
[1517.88 --> 1518.54]  are real time.
[1518.78 --> 1522.86]  None of those implied that there might be a life or death concern there.
[1523.00 --> 1529.96]  It might be that as we have more and more machines that are constantly producing data and sensors,
[1530.48 --> 1534.76]  constantly producing data that you could have critical care patients in that hospital,
[1534.76 --> 1540.22]  that it's not just an analytical thing, but there's also, but even the analytics themselves,
[1540.40 --> 1544.36]  there are, there are analytics that are needed in near real time to save a life.
[1544.36 --> 1549.40]  And there are analytics that might be able to, to be happen, you know, kind of whenever,
[1549.52 --> 1552.44]  because you're doing a study maybe or something, and they're not urgent.
[1552.60 --> 1558.66]  And there might also be sensor data on that patient that needs to alert a condition that the,
[1558.72 --> 1560.10]  that the sensor is picking up.
[1560.10 --> 1563.88]  And you need a doctor in that room working on that patient immediately.
[1564.10 --> 1568.64]  So it's not going to go to an S3 bucket, or at least not just to an S3 bucket.
[1568.82 --> 1575.16]  It also needs to alert with specific data that goes right to whatever kind of unit that doctor
[1575.16 --> 1577.80]  is carrying around who's in a completely different part of the hospital.
[1578.22 --> 1582.68]  And that doctor understands I have an urgent situation and I, I, it's measured in seconds
[1582.68 --> 1583.72]  and I need to do something.
[1583.84 --> 1585.84]  And things like that happen in real life.
[1585.84 --> 1591.38]  It happens today in real life, but we don't have very good mechanisms to deal with that.
[1591.48 --> 1597.10]  And so if you can automate like that urgent thing to where you're, you're able to prioritize
[1597.10 --> 1601.92]  that the data that's coming from a sensor that is critical immediately to a patient's
[1601.92 --> 1606.76]  life would get priority over a data that's just going to the S3 bucket at any point, if
[1606.76 --> 1608.44]  there's any kind of resource contention.
[1608.68 --> 1611.86]  And so you're able to get the information to that.
[1611.86 --> 1616.40]  And it may be that they're not, not all things are going to the S3 bucket as a data
[1616.40 --> 1616.82]  store.
[1617.00 --> 1621.66]  There might be data stores that are collecting things for historical reasons, but you also
[1621.66 --> 1626.68]  may be sharing data directly between one device and another device without putting a store
[1626.68 --> 1629.22]  between them so that you get more efficient.
[1629.22 --> 1635.32]  Or you may be meshing multiple sensors together regarding that patient together so that you get
[1635.32 --> 1639.00]  a complete picture of that patient's condition at the time.
[1639.00 --> 1646.44]  And so as you do that, the data fabric gives you that logistical routing prioritization,
[1646.64 --> 1651.90]  the metadata, and the intelligent services wrapped around it, which may include AI.
[1651.90 --> 1659.08]  You may have lots of deep learning models that are part of that mesh that are there to provide,
[1659.34 --> 1661.78]  that are able to actually do the metadata tagging.
[1661.88 --> 1662.98]  It looks at the data.
[1663.14 --> 1665.96]  It looks at other considerations that are inputs to the model.
[1665.96 --> 1670.28]  And the model is giving you inference that say, this is what you do with the data right
[1670.28 --> 1670.50]  now.
[1670.74 --> 1675.78]  So the model itself can be a service and supporting the data fabric.
[1676.38 --> 1676.48]  Yeah.
[1676.62 --> 1683.20]  So I guess in this case, they referenced this inferenced metadata or discoverable and inferenced
[1683.20 --> 1683.74]  metadata.
[1684.16 --> 1690.96]  So if you've got sort of a producer of data, like you're saying a sensor or something like
[1690.96 --> 1698.06]  that that's kind of under defined or annotated, something like that, then, you know, maybe
[1698.06 --> 1704.98]  there's actually automation or models in place there to infer certain things about that, about
[1704.98 --> 1708.38]  that data and prioritize it accordingly or something like that.
[1708.60 --> 1712.06]  I'm really glad you brought that up because if you think about it, kind of going back to
[1712.06 --> 1716.84]  the very beginning of our conversation, there's lots of different types of technologies and
[1716.84 --> 1722.56]  different generations of technologies, modern new stuff, old, antiquated, you know, legacy
[1722.56 --> 1725.82]  stuff that's out there and all of it needs to plug in.
[1725.94 --> 1733.92]  So another typical function or service of a data fabric is the connectivity to lots of different
[1733.92 --> 1736.82]  types of connected technology.
[1737.40 --> 1743.90]  In some cases, it's essentially kind of wrapping a limited set of functionality and legacy so that
[1743.90 --> 1748.36]  you can basically bring more functionality to something that otherwise you would not think
[1748.36 --> 1751.14]  of having it and therefore make better use of it.
[1751.58 --> 1756.50]  So that's a key thing is being able to actually connect all the things in a productive way.
[1756.78 --> 1756.88]  Yeah.
[1757.18 --> 1764.88]  And maybe that connection piece gets to this integrated and reusable data side of things
[1764.88 --> 1766.52]  that was in the definition.
[1766.88 --> 1772.40]  So you've got the metadata, but then it's sort of integrated and reusable across different environments,
[1772.40 --> 1777.62]  whether that's the kind of edge environment like you're talking about with the doctor being
[1777.62 --> 1782.66]  alerted or something like that, or that's an environment where you're doing some sort of
[1782.66 --> 1787.84]  batch analysis for research purposes or something like that.
[1788.36 --> 1793.78]  And they specifically also call out the hybrid and multi-cloud sort of thing.
[1793.92 --> 1799.32]  And I guess that that's probably because like in a healthcare or a hospital situation,
[1799.32 --> 1803.60]  like we have in mind, but there are many other examples of this, right?
[1803.94 --> 1811.50]  There's still a lot of mix between where data is stored at the edge or on premises or at a certain
[1811.50 --> 1816.12]  location and the mix of where it's stored online.
[1816.44 --> 1820.62]  We'd like to think that everything we do is in the cloud, but it's not quite so.
[1821.06 --> 1821.58]  It's not all.
[1821.76 --> 1824.18]  And we have more and more things at the edge.
[1824.18 --> 1828.00]  And the edge is like this gigantic blanket term.
[1828.56 --> 1831.62]  You know, we talk about the edge like, oh, of course I know where the edge is.
[1831.68 --> 1832.38]  It's the edge, man.
[1832.52 --> 1833.98]  You know, we know where that is.
[1834.26 --> 1842.40]  But the edge actually describes a huge variety of potential targets that you're trying to
[1842.40 --> 1845.76]  deploy data to or pull data from.
[1846.40 --> 1849.64]  And so, yeah, that diversity is important.
[1850.00 --> 1851.38]  And so we can address that in a moment.
[1851.38 --> 1857.38]  So, Chris, you're talking about the kind of diversity of environments and platforms and
[1857.38 --> 1862.64]  cloud means a lot of things and edge means a lot of things.
[1862.84 --> 1869.66]  I guess you've seen a lot of different types of edge devices and producers of data.
[1870.42 --> 1874.92]  And am I right that those could be, I mean, you've already mentioned sensors, but in a lot
[1874.92 --> 1879.70]  of cases and I know I've looked at a little bit of this for my wife's business to like
[1879.70 --> 1886.22]  specifically in manufacturing to a lot of times edge devices are actually fairly beefy
[1886.22 --> 1891.00]  compute nodes that are just they're sitting in a factory there.
[1891.16 --> 1895.40]  They're not in the cloud or in a data center, but they're, you know, sitting out on the factory
[1895.40 --> 1896.58]  floor or something like that.
[1896.92 --> 1897.00]  Yeah.
[1897.38 --> 1899.62]  Endpoints at the edge can have huge capability.
[1899.62 --> 1902.42]  And not only that, but you want to be able to take advantage of it.
[1902.42 --> 1907.04]  And I think if you look, if we go back over this conversation and kind of, I'm going to
[1907.04 --> 1913.00]  tie it all together a little bit in a bow here is that the data fabric has a way of declaring
[1913.00 --> 1921.44]  context for different kind of data profiles that you're able to, to create, to support whatever
[1921.44 --> 1923.48]  your need is that you're supporting there.
[1923.48 --> 1929.90]  And you might have a few profiles or for at large scale, you might have thousands, potentially
[1929.90 --> 1931.30]  millions of profiles.
[1931.46 --> 1937.68]  Each of those profiles, kind of this, this aggregation of routing, aggregating data, producers,
[1937.96 --> 1940.62]  consumers that are all trying to affect a purpose.
[1940.62 --> 1948.34]  And so the whole idea here is to automate and scale this in a standardized way and allow
[1948.34 --> 1953.38]  the fact that you have endpoints that may come and go as doctors come and go from the
[1953.38 --> 1957.84]  hospitals or machines are moved around or there, it goes from one ward of the hospital
[1957.84 --> 1958.34]  to another.
[1958.46 --> 1961.04]  And that changes the capability in a particular area.
[1961.16 --> 1966.74]  All these things are possible by acknowledging simple things about where's my data originating?
[1966.74 --> 1967.96]  Where is it going to?
[1968.50 --> 1973.28]  What are the, what's the metadata that makes it useful for the various purposes I have?
[1973.42 --> 1979.38]  And how do I capture that in a profile that's reusable over time in a productive way?
[1979.64 --> 1983.08]  So I'm going to play devil's advocate here a little bit.
[1983.22 --> 1989.20]  So it seems like at a certain point when you had sort of disparate data systems and like,
[1989.28 --> 1995.20]  if you wanted to do this, you sort of figured out where the database was and connected your
[1995.20 --> 1996.36]  app and like whatever.
[1996.74 --> 2003.02]  That was all handled, at least in scenarios I've been involved with via documentation,
[2003.26 --> 2003.44]  right?
[2003.46 --> 2008.00]  You have some documentation and here's like how this system works and here's how this
[2008.00 --> 2009.20]  system works and et cetera.
[2009.30 --> 2011.00]  And you figured it out and you did your thing.
[2011.26 --> 2017.62]  It sounds like with this like data fabric idea that you've sort of got all these, you still
[2017.62 --> 2023.26]  got all this like diversity of producers of data and maybe the way it's stored.
[2023.26 --> 2031.08]  But then you've got this layer of metadata and tagging and rules, which sort of brings all
[2031.08 --> 2032.32]  of that together.
[2032.82 --> 2039.22]  But in my mind, this metadata is going to end up looking like so complicated, right?
[2039.62 --> 2042.50]  Like, so how do you, how do you make it discoverable?
[2042.50 --> 2043.66]  I guess is what I'm getting at.
[2043.66 --> 2048.50]  So like if I'm, if I have a new application and I'm building the next best thing for my
[2048.50 --> 2055.94]  company and there's this layer of extremely complicated metadata, what advantage do I have
[2055.94 --> 2060.82]  in that scenario versus like the previous scenario where maybe I just go searching through docs
[2060.82 --> 2063.16]  to figure out which system to connect to or something?
[2063.16 --> 2067.02]  And to abstract it a little bit, and because I think it's important maybe in this last
[2067.02 --> 2071.86]  segment that we do talk a little bit about possible implementation just to keep it practical
[2071.86 --> 2072.90]  since we like to do that.
[2073.12 --> 2077.16]  If you're thinking of it that way, then, you know, you have endpoints that are coming and
[2077.16 --> 2077.40]  going.
[2077.52 --> 2081.48]  And so you have to have kind of a distributed registry of some sort.
[2081.56 --> 2085.08]  There's different options on how you might do that, but you need a registry that can handle
[2085.08 --> 2085.38]  that.
[2085.38 --> 2090.58]  And you also need kind of the equivalent or maybe going back to our joke earlier about
[2090.58 --> 2096.58]  a data dictionary that kind of identifies the characteristics of the metadata and it
[2096.58 --> 2098.80]  constrains them to an operable sort.
[2098.90 --> 2101.82]  You can't have an infinite number of things or it becomes unmanageable.
[2101.98 --> 2107.66]  So in your use case, whoever, whatever your business is and your organization does, the data
[2107.66 --> 2113.74]  fabric has to be addressing the characteristics that matter to your situation.
[2113.74 --> 2119.94]  And you have to have a manifestation of that in the sense of these kind of dictionaries
[2119.94 --> 2124.38]  that capture those and registries of your endpoints with the right metadata to do it.
[2124.40 --> 2125.56]  So it's got to get real.
[2125.84 --> 2132.36]  At the end of the day, today, as we are sitting here in 2022, you usually do this through microservices
[2132.36 --> 2133.10]  with containers.
[2133.46 --> 2138.70]  I like to tell people Kubernetes in all the places and people were kind of coming into an
[2138.70 --> 2143.14]  era where people are not just thinking about a Kubernetes cluster, but they're now starting
[2143.14 --> 2148.28]  to think about multi-clusters, sometimes maybe thousands of clusters that are connected.
[2148.88 --> 2150.74]  And you might put a cluster on a small device.
[2150.88 --> 2155.36]  You might have a whole Kubernetes cluster that is in something that fits in your pocket because
[2155.36 --> 2158.90]  of the things that it's doing and the way the services that you need there.
[2159.40 --> 2164.62]  So there's some really, we live in an amazing moment where not only are things like data
[2164.62 --> 2170.28]  fabrics being ideated to, you know, in terms of as a solution for massive scale that we're
[2170.28 --> 2176.10]  seeing coming into the real world, but also we're having these technologies that were used
[2176.10 --> 2179.60]  to be hard and we're now getting good at them and we're starting to put them everywhere.
[2179.92 --> 2186.18]  And if you take advantage of kind of the way we do things across these different areas,
[2186.18 --> 2191.42]  like Kubernetes and containerization, handling that layer, standard networking protocols underneath
[2191.42 --> 2197.16]  it, microservices to handle the things that the data fabric needs to do that are in a standardized
[2197.16 --> 2197.68]  way.
[2198.24 --> 2199.34]  It's a doable thing.
[2199.44 --> 2204.28]  You just got to constrain it and you have to not try to, you know, to use the cliche to
[2204.28 --> 2205.28]  boil the ocean with it.
[2205.32 --> 2209.58]  It's got to be really practical to your use case and not trying to overreach.
[2209.64 --> 2213.64]  And that's why I tell people your analytics is not your data fabric.
[2213.80 --> 2214.76]  You're getting carried away.
[2215.74 --> 2216.52]  Add that in.
[2216.60 --> 2217.48]  You already have analytics.
[2217.64 --> 2218.98]  Plug it into the data fabric you build.
[2218.98 --> 2230.20]  And so as an AI practitioner, if I'm sort of working with my organization to provide some
[2230.20 --> 2237.46]  better thinking around data management, you know, maybe we're dealing with kind of distributed
[2237.46 --> 2242.78]  systems like you've talked about and a variety of producers of data and all of those things
[2242.78 --> 2244.50]  as an AI practitioner.
[2244.50 --> 2250.12]  And very often, you know, we might be part of these conversations, although maybe we're
[2250.12 --> 2254.42]  not like the architect of the system, but maybe part of the conversation.
[2254.42 --> 2262.78]  I guess some things that might be useful for the practitioner to bring to the table are,
[2262.78 --> 2272.04]  you know, sort of requests and advocacy for kind of standard protocols and access layers
[2272.04 --> 2278.50]  for data, which would include like prioritization and kind of speaking to like, hey, if I create
[2278.50 --> 2282.72]  a training data set, I want to make sure I'm not like overreaching.
[2282.92 --> 2285.18]  I'm using data that I should have access to.
[2285.42 --> 2290.06]  I don't want to get in trouble, you know, by using data I shouldn't have access to.
[2290.18 --> 2293.78]  But I also want to make sure that I can update my models.
[2294.00 --> 2298.42]  And so I want to make sure I have a standardized way of accessing this data that's coming from
[2298.42 --> 2299.88]  all of our devices everywhere.
[2299.88 --> 2303.74]  So that's the maybe the AI practitioner consumer point of view.
[2303.88 --> 2307.70]  But also, I mean, an AI practitioner could bring things to the table.
[2307.70 --> 2317.62]  Sounds like in terms of the actual annotation and services built in to whatever fabric this is in terms of
[2317.62 --> 2319.64]  data is coming off of these devices.
[2319.64 --> 2324.46]  There may be ways to annotate them automatically with models.
[2324.62 --> 2325.14]  Absolutely.
[2325.38 --> 2328.64]  That make them more useful at the next level up.
[2328.96 --> 2329.22]  Right.
[2329.46 --> 2329.76]  Yes.
[2329.84 --> 2339.86]  So whether that's detecting entities and text or detecting anomalous conditions, which would change a priority of something.
[2340.10 --> 2344.08]  It sounds like that's a piece that the AI practitioner can play as well.
[2344.22 --> 2344.74]  Oh, totally.
[2344.98 --> 2347.22]  And not only that, you actually didn't go where I thought you were.
[2347.24 --> 2347.60]  Oh, OK.
[2347.60 --> 2349.78]  I never do, Chris.
[2350.68 --> 2356.06]  No, you're addressing like using the inference to do the metadata and all that.
[2356.28 --> 2361.40]  But it may be that the actual data that's moving across the data fabric, not the data fabric itself,
[2361.52 --> 2365.72]  but the constituent data that it's moving from producer to consumers,
[2366.24 --> 2375.94]  it may be that those many, many of those consumers may be MLOps pipelines that are taking data in and doing continuous training.
[2376.14 --> 2377.20]  I had to say that.
[2377.20 --> 2387.50]  Or iterative training on a rapid scale and producing models or producing things that matter, you know, for how do I treat this thing in the hospital?
[2387.62 --> 2389.12]  How do I treat that thing in the hospital?
[2389.32 --> 2390.68]  And it's going all the time.
[2390.76 --> 2392.68]  And none of that's the data fabric itself.
[2392.68 --> 2396.02]  Those are lots of AI models that are getting fed.
[2396.36 --> 2399.28]  We've spent several episodes talking about MLOps.
[2399.50 --> 2401.28]  We kind of figured out how to do that.
[2401.36 --> 2406.02]  We've got some really amazing capability out there that our listeners now know about.
[2406.02 --> 2412.14]  And now if they can get the data from all those other places to where it needs to be, then you can go do all that.
[2412.24 --> 2418.04]  And you can be that AI practitioner that's incredibly productive because you're able to do it continuously.
[2418.44 --> 2424.24]  So it fits that piece of the puzzle where you need automation, standardization and scale.
[2424.24 --> 2429.90]  Yeah. And it sounds like this is necessarily a multidisciplinary venture.
[2430.52 --> 2436.66]  So like I'm thinking, well, let's say that there's people out there in their own company.
[2436.66 --> 2445.66]  They're saying, hey, it would be great if we could move towards this layer of, you know, standardization and access, whatever that looks like in their situation.
[2446.02 --> 2450.12]  It sounds like that that is a multidisciplinary thing.
[2450.12 --> 2469.80]  So if you're like including maybe AI analytics people, but also DevOps people or MLOps people and infrastructure people in order to kind of make this work, it sounds like you probably need some like buy in from those different groups and some willingness to.
[2470.20 --> 2475.44]  Because I could also see someone say, well, this just seems like it seems like a lot of work.
[2475.44 --> 2480.86]  I'm just going to like copy some stuff out to my own S3 bucket and like deal with my own stuff.
[2482.00 --> 2487.22]  We're in early days and noting like, you know, in the time that we've been doing, we've been doing this podcast for several years.
[2487.46 --> 2493.48]  And in that time, the resources available for deep learning have evolved quite a lot.
[2493.84 --> 2496.50]  And so we're in early days right now for data fabrics.
[2496.50 --> 2506.94]  And I think that probably not terribly long after we release this episode, we're going to discover they're just you're having companies and open source projects and such.
[2507.10 --> 2513.14]  Some are already out there and you're going to see a whole bunch more pop up because scale is becoming very real in this area.
[2513.14 --> 2517.66]  And it needs it needs a community of solutions around that to choose from.
[2517.66 --> 2522.34]  So I think you'll see a lot of out of the box data fabrics that can then be applied and customized.
[2522.70 --> 2525.28]  And there are some stuff that's already out there.
[2525.36 --> 2527.80]  Then we may talk to some of those in the days ahead.
[2527.94 --> 2531.96]  So it's just the infancy of this particular part of the ecosystem.
[2532.32 --> 2534.18]  I'm glad to know what it is now.
[2534.56 --> 2545.50]  And I feel more comfortable saying the term data fabric now, whereas before I probably would have cringed just a little bit to say it.
[2545.50 --> 2548.20]  So I appreciate that part of the conversation.
[2548.76 --> 2555.56]  It's always great to, you know, have these conversations and learn about a topic together in this format.
[2555.92 --> 2563.54]  Speaking of learning, we do always like to share some learning resources in these episodes where it's just Chris and I.
[2564.28 --> 2569.10]  And the one that I wanted to share, I don't think we have a ton this episode,
[2569.10 --> 2575.62]  but I think one I wanted to share, which I kind of forgot was open and online,
[2576.32 --> 2581.04]  is Jake Vander Plaas' Python Data Science Handbook.
[2581.22 --> 2587.20]  If you just search for Python Data Science Handbook, there's a GitHub static page.
[2588.08 --> 2592.14]  And you can see, so just to kind of give some of the table of contents,
[2592.48 --> 2596.38]  there's, you know, starting with IPython, moving into NumPy,
[2596.38 --> 2603.06]  and data manipulation with pandas, but then going to data visualization and machine learning.
[2603.68 --> 2609.62]  And each of these kind of has a way to run the examples straight from the page
[2609.62 --> 2613.52]  and open it in a CoLab notebook, which is always good to see
[2613.52 --> 2617.14]  and an easy way to run things and run a bunch of tutorials.
[2617.90 --> 2620.88]  So I would definitely, you know, take a look at this.
[2620.88 --> 2629.24]  And if you want to buy the book, you can, but also there's more than enough to dig into on this online site
[2629.24 --> 2632.36]  and you can open it in, you know, the notebooks and such too.
[2632.96 --> 2634.50]  So that sounds like a really good one.
[2634.58 --> 2636.48]  And I'm going to offer one as well.
[2636.98 --> 2641.02]  The one that I'm going to offer, it's in the theme of data fabrics
[2641.02 --> 2644.34]  and the fact that we have containers with microservices
[2644.34 --> 2647.36]  and we're using containerized software to move things around.
[2647.58 --> 2651.16]  I like writing those microservices in Go.
[2651.70 --> 2653.60]  I think it is a good lane.
[2653.66 --> 2657.58]  If you're ready to move beyond Python into doing some software services
[2657.58 --> 2661.18]  and microservices around your data operations and your AI,
[2661.64 --> 2664.56]  then I think Go is a darn good language to do that in.
[2664.56 --> 2669.94]  So I'm going to reference Go.dev, G-O.D-E-V.
[2670.32 --> 2674.16]  It is maintained by the Go programming language team.
[2674.34 --> 2677.74]  It has a lot of great resources to get going and understand the language.
[2678.24 --> 2679.76]  And it's a good place to start.
[2680.36 --> 2683.02]  And so if you have some pretty cool things that you're doing out there
[2683.02 --> 2686.42]  and you want to try to get it out there in the world by integrating it into software,
[2686.94 --> 2688.36]  this is an awfully good place to start.
[2688.56 --> 2689.24]  Yeah, awesome.
[2689.64 --> 2694.34]  Yeah, well, I've been excited to get to chat about these things with you, Chris.
[2694.34 --> 2696.54]  And I appreciate you setting me straight.
[2697.22 --> 2700.66]  So yeah, looking forward to chatting about more in the future.
[2700.78 --> 2701.72]  We'll see you next time.
[2701.86 --> 2702.60]  See you next time.
[2702.68 --> 2703.22]  Thanks a lot, Daniel.
[2706.36 --> 2709.32]  All right, that is Practical AI for this week.
[2709.68 --> 2714.72]  If this is your first time listening, subscribe now at practicalai.fm
[2714.72 --> 2717.92]  or just search for Practical AI in your favorite podcast app.
[2718.04 --> 2718.64]  We're in there.
[2718.94 --> 2722.20]  And if you're a longtime listener, please do share the show with your friends.
[2722.20 --> 2725.10]  It is the best way you can help Practical AI succeed.
[2725.58 --> 2729.58]  Thanks again to Fastly for shipping our shows super fast all around the world
[2729.58 --> 2731.46]  to Breakmaster Cylinder for the Beats.
[2731.74 --> 2732.64]  And to you for listening.
[2732.90 --> 2733.60]  We appreciate you.
[2733.92 --> 2735.06]  That's all for this week.
[2735.20 --> 2736.30]  We'll talk again next time.
[2736.30 --> 2748.36]  We'll talk again next time.
[2748.82 --> 2750.14]  Bye.
[2750.14 --> 2750.68]  Bye.
[2750.68 --> 2751.38]  Bye.
[2751.54 --> 2751.60]  Bye.
[2751.76 --> 2752.26]  Bye.
[2752.26 --> 2752.82]  Bye.
[2752.98 --> 2753.24]  Bye.
[2753.26 --> 2753.28]  Bye.
[2753.44 --> 2754.24]  Bye.
[2754.24 --> 2755.08]  Bye.
[2760.78 --> 2761.42]  Bye.
[2761.42 --> 2761.90]  Bye.
[2763.24 --> 2763.40]  Bye.
[2763.56 --> 2763.80]  Bye.
[2763.80 --> 2763.82]  Bye.
[2763.92 --> 2763.94]  Bye.
[2764.02 --> 2764.06]  Bye.
[2764.16 --> 2764.48]  Bye.
[2764.50 --> 2765.02]  Bye.
[2765.02 --> 2767.78]  Game on!
