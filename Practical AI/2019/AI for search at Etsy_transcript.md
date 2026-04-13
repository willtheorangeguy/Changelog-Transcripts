[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.36 --> 18.18]  This episode is brought to you by DigitalOcean.
[18.58 --> 19.22]  Guess what?
[19.42 --> 24.22]  DigitalOcean recently added MySQL and Redis to their list of managed databases.
[24.42 --> 29.12]  Their full managed databases lineup now includes the three most popular databases out there for developers.
[29.12 --> 31.82]  Postgres, MySQL, and Redis.
[32.26 --> 36.76]  Eliminate the complexity involved in managing, scaling, and securing your database infrastructure.
[37.20 --> 40.60]  And instead, get back to focusing on building value for your users.
[41.20 --> 45.70]  Learn more and get started for free with a $50 credit at do.co slash Changelog.
[45.84 --> 47.98]  Again, do.co slash Changelog.
[59.12 --> 66.20]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[66.70 --> 71.08]  This is where conversations around AI, machine learning, and data science happen.
[71.58 --> 75.84]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[76.18 --> 77.02]  Follow us on Twitter.
[77.12 --> 78.60]  We're at Practical AI FM.
[78.86 --> 79.94]  And now onto the show.
[79.94 --> 88.34]  Welcome to another episode of Practical AI.
[88.70 --> 90.16]  This is Daniel Whitenack.
[90.28 --> 93.32]  I'm a data scientist with SIL International.
[93.78 --> 100.88]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[101.08 --> 102.00]  How are you doing this week, Chris?
[102.14 --> 102.98]  Hey, I'm doing fine.
[103.04 --> 103.64]  Daniel, what's up?
[103.64 --> 106.08]  Uh, not, not much.
[106.48 --> 107.04]  Busy day.
[107.64 --> 110.12]  It's submission day for ACL.
[110.86 --> 113.68]  And I'm trying to get something ready.
[113.80 --> 115.16]  We'll see if I actually make it.
[115.58 --> 119.48]  By the time this goes live, I will have either failed or not made the deadline.
[119.84 --> 121.94]  And ACL is for the listeners?
[122.56 --> 127.02]  Yeah, that's the, uh, computation, it's a large computational linguistics conference,
[127.02 --> 134.40]  but it's kind of one of the larger natural language processing community research conferences.
[135.04 --> 138.16]  And so there's like EMNLP and then there's ACL.
[138.46 --> 144.20]  Um, and there's larger, you know, like right now started maybe today when we're recording
[144.20 --> 148.52]  is the start of, uh, NeurIPS, which is another large AI research conference.
[148.70 --> 153.86]  And hopefully I'll be live streaming some of that later and trying to keep up because
[153.86 --> 154.44]  I'm not there.
[154.44 --> 156.76]  But yeah, it's one of those, those sorts of conferences.
[156.76 --> 160.68]  So we'll see if I, if I make it, we'll make it through.
[160.78 --> 164.34]  I got to say, I had one of the coolest weeks last week I've ever had.
[164.44 --> 166.50]  I started at Carnegie Mellon university.
[166.50 --> 170.42]  We had, there was a big conference on future of AI and STEM and society.
[170.42 --> 175.00]  I got to do a breakout on AI and ethics and such and STEM and what things that could be
[175.00 --> 175.22]  done.
[175.30 --> 178.82]  That was really a cool conversation, solved all sorts of world problems right there.
[179.08 --> 179.62]  I bet so.
[179.82 --> 180.06]  Yeah.
[180.06 --> 182.96]  I got to sit on a panel called protecting AI from threats.
[182.96 --> 187.54]  And the guy beside me was a general Cartwright who used to be the vice chairman of the joint
[187.54 --> 188.32]  chiefs of staff.
[188.72 --> 191.26]  And, uh, he just had brilliant insights.
[191.60 --> 195.22]  He's not an AI person the way we are, but was just really impressed with what he had to
[195.22 --> 195.48]  say.
[195.74 --> 200.34]  And then, uh, did a, an opening keynote in Philadelphia later on, on ethics and AI.
[200.34 --> 204.08]  And finally, we finished out the week listeners will probably recognize us.
[204.14 --> 209.26]  We had the championship for alpha pilot, which we had a previous episode on in Austin, Texas,
[209.26 --> 213.02]  and we handed out a $1 million prize to team MavLab.
[213.26 --> 213.84]  They're from Holland.
[213.84 --> 214.12]  Awesome.
[214.20 --> 215.74]  And so it was a pretty cool week.
[216.22 --> 216.40]  Yeah.
[216.42 --> 218.04]  That sounds extremely eventful.
[218.04 --> 226.34]  And, uh, I imagine that in the midst of all of that travel and logistics and all of those
[226.34 --> 231.88]  things, uh, you were utilizing some form of search in some way to, to manage your life.
[231.88 --> 232.32]  Hmm.
[232.32 --> 233.20]  I might've been.
[233.58 --> 233.92]  Yeah.
[234.00 --> 240.30]  Today on the show, we have, uh, Andrew Stanton with us, who is a staff product manager of
[240.30 --> 242.98]  search ranking and platform at Etsy.
[242.98 --> 248.10]  And I'm, I'm excited to talk with Andrew about search, but also some other things.
[248.10 --> 253.24]  And also this is the first episode, I think, where I told my wife who was coming on the
[253.24 --> 258.46]  show and she recognized, you know, obviously Etsy and was pretty, pretty psyched that I
[258.46 --> 259.86]  was talking to someone from Etsy.
[260.02 --> 262.06]  So we're all excited to talk to you.
[262.18 --> 262.86]  Welcome Andrew.
[263.26 --> 264.52]  Thank you so much for having me.
[264.96 --> 265.88]  Yeah, definitely.
[266.22 --> 270.38]  Um, so maybe to start us out, if you could just give us a little bit of your background,
[270.38 --> 277.60]  how you got into AI ML related things and search and, uh, and eventually ended up at Etsy.
[278.06 --> 278.18]  Yeah.
[278.24 --> 278.92]  Great question.
[279.34 --> 283.82]  So I've been kind of blessed to be working with machine learning and search, uh, on and
[283.82 --> 285.42]  off for about 15 years at this point.
[285.94 --> 289.94]  And the irony is I actually never intended to go into either, uh, when I was in school
[289.94 --> 292.18]  as much more interested in kind of distributed systems.
[292.68 --> 298.14]  And the funny thing was, is that, you know, as our data grows, I kept running face first into
[298.14 --> 300.76]  places where we needed to have more sophisticated search.
[300.76 --> 305.04]  We needed to have better predictive performance than kind of standard heuristics.
[305.98 --> 310.72]  So when I was, uh, in undergrad, I was actually working full time for AOL at the same time.
[310.80 --> 315.90]  And big focus at that point was working for an online radio show of all things, but it ended
[315.90 --> 320.34]  up boiling down to this kind of predictive problem where we were trying to understand how
[320.34 --> 324.20]  basically our, our listeners would kind of tune in from around the world.
[324.20 --> 329.70]  And so that was my first kind of face plants into a linear regression and kind of a time
[329.70 --> 330.40]  series prediction.
[330.80 --> 335.62]  Uh, when I left, I ended up moving into something called entity recognition, which is this kind
[335.62 --> 340.82]  of process of trying to understand from unstructured data, the different types of entities that might
[340.82 --> 346.20]  be represented in it could be people, could be companies, could be, uh, any type of, uh,
[346.20 --> 347.50]  entity that might be useful.
[347.50 --> 351.60]  And then building kind of this, uh, typo resistant search on top of it.
[351.60 --> 358.10]  And that was also probably my, my first, uh, real interaction with extremely big data.
[358.22 --> 359.88]  We were dealing with billions and billions of records.
[360.16 --> 365.44]  And so how you build kind of performance search on top of this entity recognition system, which
[365.44 --> 369.82]  is constantly ingesting, you know, hundreds of millions of records per day turned out to be
[369.82 --> 372.68]  kind of this, this scratch and itch sweet spot for me.
[372.98 --> 378.24]  From there, uh, went and worked on a bunch of different problems, uh, ended up, uh, in a startup,
[378.24 --> 382.60]  uh, called blackbird technologies where we were working on e-commerce search in the B2B space.
[382.76 --> 388.38]  And our big kind of a value add was being able to leverage a multimodal deep learning to
[388.38 --> 394.52]  basically tease apart a lot of these products that companies had to, uh, provide a better
[394.52 --> 395.90]  search experience on top of it.
[396.16 --> 400.64]  Uh, we were acquired by Etsy back in 2016 and I've been making my home ever since.
[400.64 --> 406.36]  And that, uh, that sort of multimodal, uh, side of search, when you mean that you meaning
[406.36 --> 409.40]  like images and text sort of thing.
[409.70 --> 409.94]  That's exactly right.
[410.10 --> 410.34]  Okay.
[410.52 --> 410.86]  All right.
[410.86 --> 416.66]  So like products, if you're searching products on a website, there's obviously product photography,
[416.66 --> 417.18]  right?
[417.66 --> 418.00]  Mm-hmm.
[418.40 --> 420.22]  I guess that could factor in somehow.
[420.48 --> 420.78]  Yeah.
[420.86 --> 424.48]  I would say a good example would be to think about something like Craigslist or Facebook
[424.48 --> 424.96]  marketplace.
[424.96 --> 429.86]  You have kind of an image and then you have maybe a sentence or two about what that item
[429.86 --> 434.48]  is, but somehow you have to understand that when a potential buyer comes in and they type
[434.48 --> 439.20]  in kind of this highly specific query, such as colors and materials and other types of
[439.20 --> 444.20]  attributes, you have to take this, this very unstructured piece of information and convert
[444.20 --> 446.86]  it into something which is both relevant and searchable.
[447.44 --> 451.48]  So kind of wondering, as we start to dive in and we're talking about search right off the
[451.48 --> 456.54]  bat, before we get fully into, into what Etsy is doing with search, can you kind of talk
[456.54 --> 460.34]  a little bit about what types of search problems are out there?
[460.64 --> 464.78]  We tend to use the word search in all sorts of different contexts, you know, and there's
[464.78 --> 467.70]  full text search, webpage search, product search, you name it.
[467.96 --> 471.54]  Can you kind of give us an idea of kind of the overall landscape of what search problems
[471.54 --> 473.82]  look like and how they're related, if at all?
[474.32 --> 475.86]  Yeah, that's, that's a really good question.
[476.18 --> 480.50]  There's really, I would say maybe three major areas of search.
[480.50 --> 485.42]  There's information search, which, you know, from stuff like Google, you go in, you type
[485.42 --> 489.38]  CNN, 99% of the time you're intended to go to CNN.com.
[489.62 --> 493.84]  Maybe you find the Wikipedia page is number two, but largely you're searching to find pieces
[493.84 --> 494.52]  of information.
[494.90 --> 501.10]  The second type is probably e-commerce search, which I'm most familiar with, Amazon, Walmart,
[501.60 --> 503.00]  Alibaba, et cetera, et cetera.
[503.16 --> 507.98]  How do you match these buyers who are oftentimes giving these very vague queries like jewelry
[507.98 --> 511.48]  and trying to understand, you know, what are the latent factors that are actually interesting
[511.48 --> 512.04]  to the buyer?
[512.46 --> 515.58]  The third, which has kind of grown up much more recently is probably question and answering.
[515.72 --> 520.26]  So kind of the stack overflow problem where you are asking questions, much more natural
[520.26 --> 526.82]  language, but you're trying to tease out this kind of community aspect of retrieval where
[526.82 --> 532.02]  the intent is not necessarily on finding a single piece of information, but perhaps finding
[532.02 --> 534.30]  a collection of pieces of information.
[534.30 --> 536.68]  And the domain is a little bit more NLP heavy.
[537.52 --> 544.40]  So in those different areas, I mean, obviously e-commerce developed at a certain time and certain
[544.40 --> 548.78]  things like stack overflow are probably have been more popular of recent times.
[549.34 --> 554.60]  Looking back over the history of search, you know, when did machine learning and AI start
[554.60 --> 558.98]  being applied to these types of search problems?
[558.98 --> 564.94]  Was it always applied or did it kind of start out as rule-based algorithms and like, oh,
[565.12 --> 570.70]  you know, this thing includes this word this many more times than this other thing.
[570.78 --> 571.80]  And so it's ranked higher.
[571.92 --> 574.46]  I'm assuming some of those things started earlier.
[574.58 --> 577.52]  When did AI start being applied to search?
[578.54 --> 580.78]  It's always been somewhat applied, right?
[580.84 --> 587.02]  So you can think about kind of the nexus as originally starting with catalogs.
[587.02 --> 591.98]  You had a bunch of records you wanted to retrieve across these kind of old library systems.
[592.34 --> 595.02]  And I don't know if you remember, but you used to have to give these kind of Boolean queries
[595.02 --> 598.14]  and then these kind of quasi-rankers built into it.
[598.66 --> 602.90]  For machine learning, you know, we've always tried to use and try to understand relevancy.
[603.08 --> 607.48]  And so we've had things like TF-IDF and BM25, which have kind of existed for several decades
[607.48 --> 608.16]  at this point.
[608.16 --> 614.98]  And those are like methods that are based on counting instances of tokens and working
[614.98 --> 620.08]  off of tokens that are in certain samples and not other samples and that sort of thing, right?
[620.08 --> 620.50]  Correct.
[620.76 --> 623.20]  Oftentimes it's statistical based.
[623.80 --> 628.62]  The idea is that rarer tokens contain more information is kind of the primary motivator
[628.62 --> 629.04]  for it.
[629.42 --> 635.12]  And they were really the first attempts at kind of understanding relevancy inside of kind of
[635.12 --> 636.10]  free text search.
[636.10 --> 637.52]  Facets and filters.
[637.72 --> 642.38]  So there was a company that really started popularizing this in the e-commerce space
[642.38 --> 642.96]  called Indeka.
[643.18 --> 645.64]  That was, I believe, late 90s, early 2000s.
[645.66 --> 646.44]  I used to work with them.
[646.86 --> 647.40]  Oh, wonderful.
[647.58 --> 648.68]  So you know them well.
[648.88 --> 653.88]  They kind of innovated on things such as filters and facets and really kind of scaled out the
[653.88 --> 657.96]  initial, you know, ecosystem for e-commerce search.
[657.96 --> 664.22]  As it came to machine learning, I would say probably the biggest step functions in terms
[664.22 --> 669.20]  of improvements were kind of the learning to rank work in the early 2000s, late 90s, where
[669.20 --> 674.60]  we started to apply, you know, basic machine learning problems such as support vector machines,
[674.68 --> 678.92]  such as in the case of SVM rank, to kind of improve relevancy across a whole bunch of different
[678.92 --> 679.36]  signals.
[679.36 --> 684.56]  And at that point, it moved away from these kind of generative type models such as TFID up to these
[684.56 --> 685.76]  more discriminative type models.
[686.90 --> 687.14]  Awesome.
[687.64 --> 687.82]  Yeah.
[687.94 --> 697.32]  And has, I guess, there been a lot of momentum in new, like, deep neural network, unsupervised,
[697.46 --> 700.96]  all these sorts of, like, kind of hype things that are happening now?
[701.06 --> 703.34]  Has that impacted the search world a lot?
[703.56 --> 704.86]  Oh, so much.
[705.40 --> 705.66]  Okay.
[705.66 --> 706.06]  Yeah.
[706.36 --> 706.72]  Yeah.
[706.84 --> 707.34]  Tell us.
[707.52 --> 708.10]  Tell us more.
[708.52 --> 709.18]  Oh, goodness.
[709.38 --> 709.70]  Okay.
[709.76 --> 710.44]  Where to start?
[710.86 --> 716.36]  So, I would say search is really an interesting kind of problem space because it's really kind
[716.36 --> 718.50]  of a confluence of a bunch of different technologies.
[719.02 --> 723.08]  You can think of the most, a pretty standard stack is looking like something like a solar
[723.08 --> 725.30]  and elastic search where you index all your documents.
[725.48 --> 730.72]  You retrieve some type of candidate set based on the input query and other conditionals like
[730.72 --> 731.16]  filters.
[731.16 --> 736.02]  And then you re-rank them a bunch of times and then spit out some output to the end user.
[736.98 --> 740.96]  We have innovated in the industry across every single one of those elements.
[741.12 --> 742.62]  Learning to rank models have improved.
[742.90 --> 748.20]  The recent hotness in deep learning has really started to have an effect in search in the
[748.20 --> 750.74]  form of things such as neural IR.
[750.74 --> 756.10]  So, this idea that you can build these massive models, these massive neural nets, which know
[756.10 --> 761.26]  how to translate from the query space to the document space and just replace the retrieval
[761.26 --> 765.74]  systems that were historically just text-based matching.
[765.74 --> 772.36]  So, I'm kind of curious, you know, what types of data get involved in when you're building
[772.36 --> 777.16]  out a machine learning model these days and, you know, what data is relevant?
[777.28 --> 779.12]  Where do you go for your data for search?
[779.42 --> 782.76]  It's just not something that I'm familiar with and I was rather curious.
[782.76 --> 782.90]  Yeah.
[783.32 --> 787.30]  I was thinking while Chris was saying that, like, are there data sets, like you're talking
[787.30 --> 792.64]  about learning to rank and like going from query to document, are there like existing
[792.64 --> 798.24]  data sets that, you know, are kind of standard in that or is it still like a lot of people
[798.24 --> 802.22]  using you have to kind of build up your own internal data sets and that sort of thing?
[802.64 --> 803.82]  I would say it's a bit of both.
[803.82 --> 803.94]  Yeah.
[804.30 --> 806.48]  There's definitely learning to rank data sets out there.
[806.62 --> 813.10]  So, the Yahoo learning to rank challenges from the mid-2000s, you have Microsoft had
[813.10 --> 816.66]  a bunch of different learning to rank data sets over the years, such as the Web 10K and
[816.66 --> 817.44]  the Web 30K.
[817.98 --> 821.74]  You have Trek and you have a whole bunch of these kind of historical data sets.
[821.90 --> 827.18]  The problem with them is that they were all universally kind of overfitted to kind of the information
[827.18 --> 827.94]  piece, right?
[827.98 --> 829.78]  So, that kind of web search element.
[829.78 --> 835.46]  And the problem is, is that we've learned that search inside e-commerce is actually quite
[835.46 --> 835.98]  a bit different.
[836.60 --> 842.22]  So, when it comes to taking a lot of these kind of benchmark data sets and applying them,
[842.46 --> 845.94]  they don't necessarily translate well from one domain to another.
[846.34 --> 852.80]  So, most companies will build up their own data sets internally and they will apply a variety
[852.80 --> 857.28]  of different methods, some of which might be state-of-the-art in kind of the traditional
[857.28 --> 860.90]  information sets, some which might be bespoke to their own needs.
[861.96 --> 869.14]  So, I'm kind of curious, you know, can you kind of tell us a little bit about why search
[869.14 --> 870.68]  is relevant to Etsy?
[870.90 --> 874.86]  Just to cover a little bit about the tie-in on why it is that you're doing that.
[875.14 --> 876.98]  What does Etsy need search for in that way?
[877.66 --> 883.08]  So, Etsy has over 60 million results and most of them, or a good portion of them, are handmade,
[883.38 --> 885.02]  customized, one-of-a-kind.
[885.02 --> 890.18]  And we have a big vintage basis where you only have an example of one.
[890.92 --> 896.08]  And so, unlike Google or Bing or Yandex or any of these kind of massive search engines
[896.08 --> 901.60]  where you're constantly returning a top result, we have this constant turnover in inventory
[901.60 --> 904.10]  and our inventory is just growing every day.
[904.60 --> 907.30]  The other problem with Etsy is that we don't have SKUs.
[907.76 --> 911.52]  So, unlike Amazon, who's able to leverage a lot of the structured data that's provided to
[911.52 --> 915.98]  them by the manufacturer, we basically rely on our sellers to figure it out and our machine
[915.98 --> 920.92]  learning algorithms to try to tease apart the different pieces in there into the type
[920.92 --> 923.36]  of information which is actually useful to the buyer.
[923.68 --> 928.36]  To give you an idea of why search is needed, like before, you know, back in the late 90s,
[928.52 --> 931.14]  inventories were so small you could properly navigate through.
[931.24 --> 935.90]  You'd go through a drop-down box at the top and click on jewelry and then you'd see all
[935.90 --> 937.42]  200 items that were for sale.
[937.76 --> 941.08]  If you go on Etsy right now and you type in jewelry, you'd get 18 million results.
[941.48 --> 944.46]  There's no human out there that is going to go through 18 million results.
[945.08 --> 949.90]  And so, that's where ranking and search and personalization, all these different elements
[949.90 --> 954.74]  kind of come together to try to hone down that 18 million total results set to something
[954.74 --> 956.22]  that's actually digestible by the buyer.
[957.22 --> 957.62]  Yeah.
[957.82 --> 962.56]  And I was just thinking while you were describing things, it seems almost like there's so many
[962.56 --> 968.30]  outliers in Etsy in the sense that like I just searched for, for example, I searched for
[968.30 --> 976.60]  R2-D2 because, you know, we've been watching Star Wars stuff recently and I see like R2-D2
[976.60 --> 980.04]  like gift pack of like planting pots.
[980.04 --> 988.80]  And then I see a R2-D2 like chalk bag for rock climbing, which if I'm just thinking like
[988.80 --> 997.58]  an R2-D2 rock climbing chalk bag seems like extremely outlier to me in terms of like products
[997.58 --> 1000.96]  that you could create some rules around, right?
[1001.44 --> 1002.64]  It seems super challenging.
[1003.00 --> 1004.48]  It's a really good point.
[1004.86 --> 1011.44]  Etsy, we have a lot of very niche niches and that's really spectacular for the buyer too
[1011.44 --> 1015.82]  because that means there is likely something out there for you that almost feels like it
[1015.82 --> 1020.46]  was made specifically for you for that one person, that Star Wars lover who, you know,
[1020.46 --> 1025.14]  likes to get up on rock walls, that that's a very applicable gift and understanding when
[1025.14 --> 1028.44]  to surface those versus when not to is a big part of the challenge.
[1028.44 --> 1044.24]  This episode is brought to you by Brave.
[1044.40 --> 1046.08]  Big news from the Brave team.
[1046.20 --> 1048.08]  Version 1.0 is official.
[1048.44 --> 1053.70]  That means our favorite open source privacy focused blazing fast browser is ready for primetime.
[1053.70 --> 1058.62]  Their brand new iOS app landed just in time for the announcement and the Brave team is
[1058.62 --> 1062.56]  celebrating by granting 8 million basic attention tokens to the community.
[1062.98 --> 1067.00]  That means when you download the iOS app, you get 20 baht absolutely free.
[1067.38 --> 1072.28]  Put it to good use by heading to changelog.com, hitting the triangle icon in the upper right
[1072.28 --> 1074.24]  hand corner and flipping us a tip.
[1074.24 --> 1094.06]  So it was mentioned to us that Etsy is using neuroevolution for search.
[1094.06 --> 1101.36]  And I guess if you could kind of tell us a little bit about what is neuroevolution and
[1101.36 --> 1102.56]  kind of what does that mean?
[1102.64 --> 1104.00]  It's a new term to me.
[1104.28 --> 1107.80]  And so I'm kind of curious not only to understand what it is, but how it relates to search.
[1108.78 --> 1108.98]  Yeah.
[1109.22 --> 1112.06]  So neuroevolution has been kind of a moving definition.
[1112.46 --> 1115.00]  It originally started, at least the first time I heard about it.
[1115.08 --> 1115.78]  Been evolving?
[1116.24 --> 1117.36]  It is about evolving.
[1117.72 --> 1120.90]  It's combining kind of these evolutionary algorithms.
[1121.10 --> 1124.92]  You might have remembered them as things like genetic algorithms from back in the early
[1124.92 --> 1125.76]  2000s.
[1125.76 --> 1132.94]  But really, neuroevolution is kind of combining these kind of evolutionary algorithms to neural
[1132.94 --> 1133.72]  nets, effectively.
[1134.50 --> 1140.92]  I first came aware of it from a project called NEAT, which I believe was mid-2000s.
[1141.04 --> 1145.82]  And the idea was that it could actually evolve both network structures as well as the weights
[1145.82 --> 1150.76]  associated with those neural nets to solve these kind of black box problems.
[1150.76 --> 1157.86]  I know jargon is often a point of confusion, but we've talked before on the program about
[1157.86 --> 1162.96]  meta learning and sort of learning to learn and different things involved with that.
[1163.32 --> 1168.92]  Is that sort of how evolutionary algorithms are being applied to neural nets?
[1169.00 --> 1172.54]  You mentioned kind of learning architecture and weights and other things.
[1172.88 --> 1178.04]  Or is evolutionary algorithms, is that a sort of different piece of the puzzle?
[1178.04 --> 1181.98]  Metal learning is much more about, as you say, learning to learn, right?
[1182.06 --> 1187.42]  So you can either figure out ways to learn optimizers to train models, or you can learn
[1187.42 --> 1192.32]  parameter weights, which make fine tuning on those models a lot faster, such as the case
[1192.32 --> 1193.62]  of mammal and reptile.
[1194.20 --> 1200.08]  Neuroevolution is more of like a competitor to things like stochastic gradient descent, I
[1200.08 --> 1200.44]  would say.
[1200.60 --> 1207.28]  It's more of a way of learning models based on these kind of beliefs of populations of answers
[1207.28 --> 1209.02]  that can kind of compete with each other.
[1209.74 --> 1215.90]  And based on a very rough estimation of, say, Darwin, where the best survive, the candidates
[1215.90 --> 1220.48]  in the population, which ended up performing better, end up persisting through multiple
[1220.48 --> 1221.52]  generations of work.
[1221.94 --> 1226.44]  So I'd say it's more common to think of it as kind of more of a learning paradigm.
[1226.94 --> 1229.08]  It became a little bit more popular recently.
[1229.08 --> 1236.10]  Back in, I think, just 2017, OpenAI published this paper on how they applied this one particular
[1236.10 --> 1241.98]  technique from neuroevolution called evolutionary strategies to train agents in reinforcement
[1241.98 --> 1242.32]  learning.
[1242.42 --> 1244.26]  And they applied it to the standard Atari datasets.
[1244.96 --> 1246.98]  And they found out that it was actually very competitive.
[1247.74 --> 1253.48]  And so this field, which was much more popular in the early 2000s, that kind of got back-burnered
[1253.48 --> 1258.48]  when neural nets started really taking off in, I guess, 2013 when Alex and I showed that
[1258.48 --> 1261.06]  they were actually useful for solving these big problems.
[1261.26 --> 1265.40]  We're starting to see resurgence because much of the same reasons that neural nets have become
[1265.40 --> 1267.88]  successful, neuroevolution has become successful.
[1268.02 --> 1269.68]  The computation is finally there.
[1270.62 --> 1275.70]  For some clarification, can you talk a little bit about, you mentioned, you know, kind of as
[1275.70 --> 1279.64]  a replacement for stochastic gradient descent, could you actually kind of talk about where
[1279.64 --> 1281.98]  you might use neuroevolution instead of that?
[1282.22 --> 1286.94]  Because obviously, as a lot of our listeners and certainly myself having come into this,
[1287.00 --> 1289.32]  we're very familiar with stochastic gradient descent.
[1289.54 --> 1293.84]  And can you kind of say where it would be productive to consider neuroevolution to replace
[1293.84 --> 1295.24]  it in kind of a use case?
[1295.66 --> 1296.38]  Sure, absolutely.
[1296.54 --> 1298.72]  And I can speak specifically to Etsy's use case.
[1299.50 --> 1303.78]  So whenever you can compute a gradient, it's almost always better to use SGD.
[1304.02 --> 1307.98]  The problem that you have is that there are a number of domains where it's very difficult
[1307.98 --> 1310.82]  to compute the gradient of the actual objective function.
[1311.36 --> 1312.96]  And you can think of reinforcement learning, right?
[1312.96 --> 1317.58]  We have this environment where we send in some actions and we get some rewards, and then
[1317.58 --> 1318.54]  we get an updated state.
[1318.60 --> 1324.84]  But there's no rule closed form mathematical equation we can use to try to understand where
[1324.84 --> 1326.08]  to step the policy next.
[1326.70 --> 1331.20]  And so most of the policy gradient methods and Q learning and all those are really trying
[1331.20 --> 1336.04]  to do sort of credit assignment and figure out ways to kind of compute gradients which improve
[1336.04 --> 1336.86]  the model.
[1336.86 --> 1341.92]  Neuroevolution is really nice because it makes very little assumption about the underlying
[1341.92 --> 1343.28]  objective function.
[1343.70 --> 1348.74]  In fact, all it really needs is to be able to know what you're putting into your fitness
[1348.74 --> 1354.50]  function and get some type of fitness score out of it where the higher the fitness score
[1354.50 --> 1358.12]  is, the better the model is or the input space is that you pass into it.
[1358.76 --> 1364.80]  So anytime you have like a situation where it's very difficult to compute a gradient and you
[1364.80 --> 1368.92]  need to do it based on sampling or some other form of estimation, it can be quite competitive.
[1369.66 --> 1375.02]  In those scenarios where it might be hard to compute a gradient, is that typically when
[1375.02 --> 1380.46]  like when you have such like in the problem with Etsy, I'm trying to connect this to the
[1380.46 --> 1381.48]  search problem with Etsy.
[1381.48 --> 1388.98]  Is that because there's so much diversity in your data set between like query and product
[1388.98 --> 1395.96]  match or rank where, you know, there's not kind of recognized categories of things, but
[1395.96 --> 1396.88]  there's so much diversity?
[1397.10 --> 1399.10]  Is that what produces that sort of scenario?
[1399.10 --> 1404.00]  So in the case of Etsy, one of the challenges we have is that we're a two-sided marketplace,
[1404.38 --> 1406.08]  which really means we have two customers.
[1406.22 --> 1407.26]  We have buyers and we have sellers.
[1408.04 --> 1412.56]  And one of the places where things like evolution algorithms have been very successful is in this
[1412.56 --> 1415.44]  particular subfield called multi-objective optimization.
[1416.40 --> 1421.32]  And the idea is that relevancy is only one of the factors that go into a healthy marketplace.
[1422.18 --> 1423.46]  Let me give you a hypothetical.
[1423.88 --> 1427.44]  So imagine that you want to make your seller successful.
[1427.44 --> 1429.68]  Now you have this kind of problem, right?
[1429.82 --> 1433.82]  You have sellers who've been on the site for a long time and they're relying on a consistent
[1433.82 --> 1435.82]  form of income from the marketplace.
[1436.34 --> 1440.16]  But at the same time, you want to make sure that new sellers are also successful.
[1440.78 --> 1446.10]  And so you need to kind of expose them artificially higher in the rankings to make sure that they
[1446.10 --> 1446.54]  can do it.
[1447.04 --> 1451.02]  Now, those two needs are naturally in conflict with each other because there's only so much
[1451.02 --> 1452.48]  space for search.
[1453.00 --> 1456.50]  Yeah, you can't optimize one because you would necessarily kill the other.
[1456.50 --> 1457.56]  That's exactly right.
[1457.68 --> 1463.80]  And so that's called the rate between tradeoff between those two objectives is called kind
[1463.80 --> 1467.14]  of the Pareto frontier, the Pareto efficiency of the actual problem.
[1467.68 --> 1471.88]  And it turns out that it's really hard to do when you start combining a lot of these different
[1471.88 --> 1472.70]  objectives in there.
[1472.84 --> 1477.80]  And especially when you start boiling them down to things which require relevance to be
[1477.80 --> 1481.98]  considered as well, which is a very hard gradient to compute in the best of times.
[1481.98 --> 1487.00]  And so you have this kind of black box function, which have all these different factors, which
[1487.00 --> 1488.54]  have these tradeoffs between them.
[1489.08 --> 1494.46]  How can you, in a very principled way, train a model that's able to kind of adjust for those
[1494.46 --> 1499.46]  tradeoffs and kind of learn an optimal balance between all of them?
[1499.46 --> 1506.82]  So I'm kind of thinking when you are implementing this, and I'm still kind of very focused on how
[1506.82 --> 1512.82]  neuroevolution can be implemented in a kind of a practical way, what kind of challenges did you find
[1512.82 --> 1517.20]  yourself facing in implementing that into your algorithm versus some of the more traditional
[1517.20 --> 1519.64]  approaches that might have been more obvious?
[1520.36 --> 1521.86]  Yeah, it's a good question.
[1522.08 --> 1523.96]  I think there were a couple of different challenges.
[1523.96 --> 1529.56]  First, neuroevolution is many things, but it is not computationally efficient.
[1530.16 --> 1536.00]  Because you're basically relying on sampling, kind of basically you have like a model, let's
[1536.00 --> 1537.60]  say, you have parameters of that model.
[1538.04 --> 1544.24]  The way you can kind of estimate a gradient step is by sampling slight perturbations of the
[1544.24 --> 1548.80]  parameters around that model space and trying to intelligently combine them into kind of a
[1548.80 --> 1552.46]  gradient, which hopefully improves the model's performance.
[1552.46 --> 1559.24]  Unfortunately, we've learned from certain types of research in zeroth order optimization that
[1559.24 --> 1564.74]  as the dimensions of the model increases, you need about a square of that in terms of samples to
[1564.74 --> 1565.88]  accurately measure that.
[1566.48 --> 1572.10]  And so as your model gets bigger, you need to spend more and more time in that exploratory space.
[1572.32 --> 1573.74]  And that gets really expensive.
[1574.30 --> 1578.98]  Now, where you can kind of mitigate some of that is by using more efficient languages,
[1578.98 --> 1585.28]  being smarter about the size of your space, being smarter about the type of algorithms that you're
[1585.28 --> 1586.36]  using to combine them.
[1586.50 --> 1589.54]  So one of these is something called evolutionary strategies.
[1590.02 --> 1591.04]  And it's actually pretty good.
[1591.10 --> 1600.46]  You can combine it with these second order approximators like Atom or RMS prop or Momentum to kind of take
[1600.46 --> 1607.02]  advantage of some of the work inside of the classic stochastic gradient and sense base to speed up optimization.
[1607.02 --> 1614.76]  But it really becomes a question of how do you maintain the efficiency of the search at the same time, get the results that you're hoping for.
[1615.76 --> 1622.46]  So before we move on to some of those things that you just mentioned, like the language, which I particularly want to follow up on,
[1622.46 --> 1628.52]  I was wondering if you could just kind of give an update as far as, you know, how did this end up working?
[1628.68 --> 1631.18]  Did it improve things by leaps and bounds?
[1631.34 --> 1632.24]  Was it marginal?
[1632.66 --> 1637.02]  And what are your thoughts in terms of after doing these neuroevolution experiments?
[1637.56 --> 1641.12]  What's next in terms of upgrading search at Etsy?
[1641.44 --> 1645.34]  Or do you feel like there's other things maybe that are more important to focus on now?
[1645.62 --> 1646.34]  Yeah, great question.
[1646.66 --> 1652.12]  So the way we decide to integrate it, I mentioned before kind of a rough topology of what a search stack looks like.
[1652.12 --> 1656.94]  You have an information retrieval system like solar elastic search where you get some candidate sets back.
[1656.94 --> 1663.00]  And then you go through this cascade ranking system where you're constantly re-ranking and refining down the result set.
[1663.70 --> 1668.80]  And that means you can go from simple models, which are very fast, but are operating on a fairly large candidate set,
[1668.88 --> 1672.42]  down to expensive models, which are slow, but are operating on a much smaller one.
[1672.76 --> 1676.50]  We put it at the very end, and we call it kind of the business intelligence layer.
[1676.50 --> 1683.66]  And it allows us to kind of incorporate both beliefs or priors about what would be beneficial for the marketplace,
[1684.06 --> 1685.94]  but apply it at the end of the ranking.
[1686.04 --> 1689.12]  So we're always getting the best possible relevance we can out of our systems,
[1689.12 --> 1693.64]  but we're adjusting the ordering at the end to try to influence these other factors.
[1693.64 --> 1698.00]  From online experiments, it worked about as well as we could have asked for.
[1698.64 --> 1699.98]  It is somewhat funny.
[1700.10 --> 1705.18]  There were trade-offs as well as we find the metrics that we're optimizing for.
[1705.54 --> 1711.08]  It's one of those funny things where you almost have to be like a lawyer when you're writing the type of fitness functions for these things to evolve,
[1711.30 --> 1716.28]  because it will follow the letter of the law, but it will do it in kind of weird ways.
[1716.28 --> 1720.38]  So, for example, we were optimizing relevancy at K, right?
[1720.46 --> 1725.48]  So precision at K, where you want to get the item that was purchased in the top 10 results.
[1725.90 --> 1731.88]  And what we were finding is that it would oftentimes put that purchase at the 10th position,
[1732.42 --> 1734.28]  even though that's not what we actually wanted.
[1734.34 --> 1737.16]  We wanted to move it higher up because as far as it cared,
[1737.26 --> 1741.54]  all it needed to do was get into that top 10 position and it was able to make balances up there.
[1741.94 --> 1745.28]  So it'll do what you say, not necessarily what you want it to do.
[1745.28 --> 1751.80]  Yeah. So it sounds like maybe like part of the future is really now that you have some of these things implemented,
[1751.80 --> 1759.70]  really exploring the policies that you put in place and the strategies that you're using to kind of rein these things in.
[1759.82 --> 1760.40]  Is that right?
[1760.60 --> 1761.46]  That's exactly right.
[1761.86 --> 1767.00]  A lot more work on metrics, a lot more work on kind of understanding what the trade-offs in the marketplace are.
[1767.84 --> 1773.84]  So I know that one of the things that we talked about earlier on in the conversation that I've been kind of waiting to get to,
[1773.84 --> 1779.64]  because I'm pretty fascinated with it, is that you guys are using Rust in your line.
[1779.72 --> 1780.94]  You've mentioned it a couple of times.
[1781.44 --> 1783.96]  And I know kind of Daniel and I are both interested in that.
[1784.10 --> 1785.26]  We're both actually gophers.
[1785.40 --> 1790.46]  And, you know, there's a friendly competition a little bit culturally between the Rust and the Go people.
[1790.74 --> 1792.96]  We certainly have a great respect for each other.
[1793.02 --> 1798.86]  I'd love to understand how you're using Rust in productizing your machine learning systems.
[1798.86 --> 1801.42]  Oh, it's a wonderful question.
[1802.18 --> 1805.86]  So for folks who don't know, Rust is a language that was developed by Mozilla.
[1806.52 --> 1808.68]  And Mozilla, this was back in, I guess, 2010.
[1808.80 --> 1809.46]  They had a problem.
[1809.98 --> 1812.54]  Mozilla is most well-known for its browser, Firefox.
[1813.36 --> 1818.74]  And every week it felt like there was some type of security flaw that was being found that they had to release a patch for.
[1818.74 --> 1822.12]  And they started looking at kind of the core reasons behind it.
[1822.16 --> 1829.92]  And they realized that these kind of low-level systems languages, which browsers like Chrome and Firefox and Internet Explorer and all those are written in,
[1830.28 --> 1841.74]  are really not optimized for solving these kind of common problems that you run into that can, you know, result in things like buffer overflows or use after free or null pointer dereferencing.
[1841.74 --> 1848.14]  All these kind of problems that you might run into and practice when you're writing in a language like C or C++.
[1848.66 --> 1853.44]  So they got together and they started looking around at kind of modern programming language theory.
[1853.44 --> 1860.16]  And they kind of picked and choose some of the best pieces from languages in the ML space, such as Haskell and OCaml,
[1860.36 --> 1865.58]  as well as practical pieces such as, you know, algal-based systems such as C and C++,
[1865.96 --> 1877.04]  and try to combine it together with really strong static analysis to produce a language which was both extremely fast and a suitable replacement for C and C++ in systems language,
[1877.04 --> 1884.36]  but at the same time kind of had the static analysis you needed to write safe and efficient code.
[1884.84 --> 1893.94]  So just as a quick follow-up, could you describe a little bit about how one would apply Rust, you know, in that environment?
[1894.18 --> 1902.24]  Does it basically replace the kind of the software architectures that are wrapping your machine learning pipeline?
[1902.84 --> 1904.56]  Or how does that work?
[1904.56 --> 1906.96]  Where does it fit into the overall architecture?
[1907.96 --> 1911.36]  So I'll talk about more generally, and then I'll talk about the Etsy-specific case.
[1911.98 --> 1917.14]  More generally, the kind of frameworks that most people are accustomed to using are actually written in Python.
[1917.88 --> 1922.48]  But the lie about Python is that none of the fast bits are actually written in Python.
[1922.68 --> 1928.18]  It's all indexing into C and C++ or Cython or, in some cases, Fortran.
[1928.68 --> 1933.16]  And what Python really becomes is this kind of domain-specific language for gluing these together.
[1933.16 --> 1942.58]  The ones that are probably most familiar to everyone on the show are Scikit-Learn, TensorFlow, PyTorch, LightGBM, XGBoost.
[1942.82 --> 1947.04]  All of those have the kind of core performance pieces written in C and C++.
[1947.90 --> 1950.34]  And they also aren't immune to these problems.
[1950.34 --> 1959.96]  And so you can actually look and find TensorFlow has had to release patches because they also, by nature of being in C and C++, have these problems with safety and reliability.
[1959.96 --> 1969.34]  So the place where Rust tends to have the biggest benefit is by replacing those back-end components with a safer, faster language.
[1969.98 --> 1976.34]  And we've had a lot of kind of work recently done in this space to make it a little bit easier to integrate with Python.
[1976.34 --> 1985.10]  And so there's a project called Py03 out there, which makes it much simpler to interface between the back-end and the front-end, as it applies to Etsy.
[1985.42 --> 1989.36]  So in the learning-to-rank space, we have to do a lot of feature engineering.
[1989.72 --> 1993.26]  The state-of-the-art is still gradient-boosting models for the most part.
[1993.34 --> 2001.92]  And that means that a lot of the benefits you get from neural nets, that feature engineering piece kind of being deferred to the algorithm, you have to do manually.
[2001.92 --> 2013.94]  And we were running into this case where every night we were training hundreds of millions or billions of records, and we were trying to plumb them through a whole bunch of different features, and it was taking an exorbitant amount of time.
[2014.44 --> 2027.58]  The second piece that's really challenging in the search space is that the machine learning algorithms are traditionally written in Python, but Solr and Elastic and these kind of core inverted-indice-based systems are actually written in languages like Java.
[2027.58 --> 2042.22]  And what we really didn't want to have to do is write feature engineering twice, so do something like the hashing trick in Python, and then have to port that same implementation over to something like Java to get the models trained in Python and then deployed on Java.
[2042.72 --> 2050.28]  And so we were really looking for a language which would allow us to kind of embed it in both Python and Java at the same time, and that kind of puts some restrictions.
[2050.54 --> 2052.28]  So you mentioned that you both are gophers.
[2052.28 --> 2061.22]  One of the problems with Go is that it actually has managed memory, and Java and Python don't necessarily work particularly well with managed memory while managing their own memory.
[2061.80 --> 2075.64]  And so those types of constraints made it kind of hone down the number of opportunities we had, and we were mostly focused on trying to find one where we thought we could be productive quickly, but at the same time didn't have to pay a performance penalty.
[2075.64 --> 2096.46]  And with that, as you looked into Rust for those particular problems like you're talking about with feature engineering, but also considered maybe some of the neural evolution things that you were exploring, I'm assuming that some of those fundamental or foundational papers like the OpenAI paper that you mentioned,
[2096.46 --> 2106.62]  if you went and looked at the implementation, maybe the model is implemented in Python and PyTorch or TensorFlow or something like that.
[2106.96 --> 2112.90]  How does that piece fit in along with the sort of feature engineering, pre-processing stuff?
[2113.16 --> 2120.96]  Are you taking models kind of from the one frameworks and then doing a lot of the feature engineering and that sort of thing with Rust?
[2121.14 --> 2122.30]  And how does that play together?
[2122.30 --> 2125.96]  So we really have two main systems that are written in Rust.
[2126.16 --> 2129.84]  Both are powering hundreds of billions of predictions a day.
[2130.48 --> 2134.02]  So our first one was Buzzsaw, which we wrote a paper on back in 2018.
[2134.80 --> 2138.42]  And it really is kind of the backbone of how we do feature engineering at Etsy at this point.
[2138.76 --> 2140.04]  We pump a lot of data through it.
[2140.10 --> 2141.42]  It can scale across clusters.
[2141.66 --> 2143.76]  We can embed it inside Python and inside the Java.
[2144.46 --> 2148.56]  And it's really nice because when you're training models, especially in the search space,
[2148.70 --> 2152.18]  you want to make sure that what you're training against doesn't change.
[2152.30 --> 2159.24]  And so you can imagine that by adjusting the implementation of, say, TF-IDF just slightly,
[2159.24 --> 2162.52]  you can actually have these changes to the prediction space.
[2162.76 --> 2168.00]  But because we're able to ship the library to both our cluster compute, which does the pre-processing,
[2168.00 --> 2174.18]  and run that exact same code in our Python-based learning to rank prediction services,
[2174.40 --> 2178.18]  we don't have to worry about that gap in terms of implementation.
[2178.18 --> 2183.64]  As for the neuroevolution space, as I mentioned before, it's not super sample efficient.
[2184.22 --> 2188.66]  So there's been a lot of work around trying to figure out how to scale up these systems.
[2188.82 --> 2195.34]  And one of the ways we were very successful in doing that is by moving the neuroevolution pieces down into Rust rather than from Python.
[2196.06 --> 2200.00]  And so when we originally prototyped this out in Python, it worked.
[2200.00 --> 2201.64]  It was slow, but it worked.
[2202.16 --> 2209.26]  But by moving it into Rust, the main core implementation, we were able to speed it up by some 100x and reduce the memory footprint of it
[2209.26 --> 2213.10]  and just scale up both of our data as well as the size of the models.
[2213.96 --> 2216.00]  Was that sort of re-implementation overhead?
[2216.36 --> 2219.68]  Was that high or did you find it going fairly smoothly?
[2219.68 --> 2224.72]  And I'm not sure about, you know, maybe you had experienced Rust people and that sort of thing,
[2224.80 --> 2231.10]  or was it more like you have experienced AI, like Python people, and they're kind of dipping into Rust?
[2231.48 --> 2233.16]  I would say it's more the louder than the former.
[2233.82 --> 2238.44]  Rust is a new language by the general timelines of language.
[2238.60 --> 2245.30]  I mean, C++ came out in 1985, I believe, and Java was 98, Python was 1990.
[2245.48 --> 2248.06]  So there's been a lot of time to kind of bake engineers there.
[2248.06 --> 2251.46]  Rust only hit 1.0, I believe, back in 2015.
[2252.26 --> 2255.88]  So it's still new, and there's still kind of this community building that's going on.
[2256.32 --> 2260.96]  So most of our developers are coming from, I know Python, I know a little bit C++.
[2261.68 --> 2267.32]  You know, I had to deal with Java in school, but that's largely my experience in languages that I use in my day-to-day.
[2267.64 --> 2272.36]  From an implementation perspective, swapping from Python to Rust, there was some cognitive overhead
[2272.36 --> 2275.90]  in terms of learning how to work with static analysis,
[2275.90 --> 2281.42]  learning how to use these kind of more advanced features that come in the language to your benefit.
[2281.94 --> 2284.70]  And then there's just the nature that when you're writing code in Python,
[2285.00 --> 2287.56]  you're really gearing for kind of a prototyping space.
[2287.64 --> 2289.68]  You're not really necessarily thinking about performance.
[2290.22 --> 2294.44]  But when you move to a language like Rust, and you're trying to do it to squeak out performance,
[2294.44 --> 2300.22]  you have to think about things such as memory allocation, using SIMD, potentially using CUDA,
[2300.34 --> 2304.14]  and how those all kind of play in to building robust systems.
[2304.80 --> 2305.44]  So I'm kind of curious.
[2305.60 --> 2309.42]  You're recognizing that Rust is still a very new language,
[2310.42 --> 2315.40]  and kind of scratching that itch of the languages that it's replacing.
[2315.40 --> 2319.76]  As you're looking further into using it in the kind of AI ML space,
[2319.96 --> 2325.80]  do you think that the community, though it be small today, is likely to grow and develop going forward?
[2325.88 --> 2330.86]  Do you think it's a substantial enough use case for Rust to really kind of blossom in that area?
[2331.44 --> 2332.16]  I do.
[2332.56 --> 2334.74]  I don't think we're necessarily all the way there yet.
[2335.20 --> 2339.28]  But I think there's a bunch of indicators that are really positive for it.
[2339.32 --> 2342.54]  First, big companies are starting to depend on it.
[2342.54 --> 2346.74]  So Dropbox, for example, uses Rust in their storage layer because they need reliability.
[2347.56 --> 2349.78]  Facebook came out earlier this year with their cryptocurrency,
[2350.06 --> 2352.26]  which is written in Rust because they need the security.
[2353.04 --> 2356.08]  Microsoft, just a few days ago, published a result of a project
[2356.08 --> 2359.84]  where they were trying to replace core pieces of their Windows 10 code with Rust
[2359.84 --> 2361.54]  because they got tired of security flaws.
[2362.32 --> 2366.70]  So we're kind of seeing a lot of big companies starting to adopt it,
[2366.82 --> 2369.00]  at least in prototyping cases,
[2369.00 --> 2372.54]  and more seriously in the case of companies like Facebook.
[2373.34 --> 2377.56]  I think that it is going to be really valuable
[2377.56 --> 2380.86]  because the one thing that I've noticed for us
[2380.86 --> 2384.34]  is that there's really kind of three payments that you have to make, right?
[2384.48 --> 2386.02]  When it comes to building machine learning,
[2386.10 --> 2388.00]  there's the cost of development,
[2388.20 --> 2389.30]  there's the cost of running,
[2389.30 --> 2390.72]  and then there's the cost of maintenance.
[2391.50 --> 2394.58]  And Python does a great job at the cost of development, right?
[2394.58 --> 2398.82]  We have this rich ecosystem filled with libraries out there.
[2398.92 --> 2399.86]  You can just pip install them.
[2399.90 --> 2400.60]  They just kind of work.
[2401.00 --> 2402.78]  You can prototype an idea very quickly.
[2403.46 --> 2404.84]  But it's not an efficient language.
[2405.00 --> 2406.86]  So that cost to run starts adding up,
[2406.92 --> 2409.74]  especially when you have to clone it over hundreds of machines
[2409.74 --> 2411.22]  to train these very large models.
[2411.84 --> 2412.62]  And the final piece,
[2412.78 --> 2414.10]  and this is the more insidious one,
[2414.12 --> 2415.02]  is the cost of maintenance.
[2415.48 --> 2417.74]  What is the cost of failure in your systems?
[2418.22 --> 2419.80]  And when we think about things like production,
[2420.42 --> 2422.42]  whenever our learning to rank models go down,
[2422.42 --> 2424.42]  we start losing money really quickly.
[2424.64 --> 2426.54]  We have 18 million results for jewelry, right?
[2426.84 --> 2429.66]  It turns out that there are better answers in there than others.
[2430.20 --> 2432.88]  And so we need to be very cognizant
[2432.88 --> 2435.32]  of what that long-term effect actually is
[2435.32 --> 2437.76]  when it comes to building out quote-unquote production.
[2438.44 --> 2438.62]  Yeah.
[2438.86 --> 2442.90]  And I mean, that's something that definitely resonates with us.
[2443.06 --> 2446.30]  Like we mentioned, having worked a little bit in Go,
[2446.70 --> 2450.96]  I'm really curious to start dipping into Rust a little bit
[2450.96 --> 2452.42]  and get my hands dirty.
[2452.86 --> 2454.34]  Are there good places like,
[2454.66 --> 2458.38]  let's say for people that have some experience
[2458.38 --> 2461.50]  doing Python stuff in machine learning and AI,
[2461.92 --> 2463.72]  what are some good ways for them
[2463.72 --> 2466.84]  to start getting into Rust a little bit?
[2466.96 --> 2468.72]  Are there kind of tutorials
[2468.72 --> 2471.20]  or machine learning parallels
[2471.20 --> 2472.62]  that they could go to out there
[2472.62 --> 2475.28]  in terms of common machine learning problems
[2475.28 --> 2475.98]  and that sort of thing?
[2476.30 --> 2477.34]  Yeah, it's a really good question.
[2477.34 --> 2480.08]  So I will say this about Rust is that
[2480.08 --> 2482.14]  I feel like I'm marketing right now,
[2482.22 --> 2483.14]  but the truth is,
[2483.16 --> 2484.80]  is that it's the nicest community
[2484.80 --> 2485.70]  that I've ever run into.
[2485.88 --> 2488.26]  So the IRC channels, the Rust subreddit,
[2488.82 --> 2491.56]  just generally the way Mozilla has run the community
[2491.56 --> 2494.38]  is the most welcoming I've ever seen.
[2494.98 --> 2496.32]  Yeah, with Mozilla behind it,
[2496.34 --> 2499.58]  I think one could expect some good things in that sense.
[2499.74 --> 2500.90]  And they've done a really good job
[2500.90 --> 2502.38]  at kind of baking it and kind of,
[2502.94 --> 2505.34]  I heard a really interesting quote recently,
[2505.34 --> 2506.60]  which I think does kind of resonate.
[2506.96 --> 2509.46]  You know, Google built Go for Google, right?
[2509.48 --> 2511.02]  They didn't necessarily build it for the community,
[2511.02 --> 2513.28]  whereas it really does feel like Mozilla
[2513.28 --> 2514.94]  kind of built Rust for the community.
[2514.94 --> 2516.08]  And it just so happened
[2516.08 --> 2517.74]  to also work extremely well for them.
[2518.60 --> 2520.52]  And that really is kind of permeated
[2520.52 --> 2521.78]  through all layers of it.
[2521.94 --> 2524.54]  And so you can find good books on Rust,
[2524.64 --> 2526.30]  on kind of adopting it from other languages.
[2526.30 --> 2528.32]  You can find a lot of GitHub repos.
[2528.84 --> 2531.66]  I know there's not much value in popularity contests,
[2531.66 --> 2534.72]  but it's one, I believe, the most loved language
[2534.72 --> 2537.04]  on Stack Overflow for like five years running now.
[2537.56 --> 2540.96]  So there's a lot of joy kind of involved in that space.
[2541.12 --> 2542.88]  And there's lots of people very eager
[2542.88 --> 2544.18]  to help you with your problems.
[2545.00 --> 2545.14]  Great.
[2545.40 --> 2549.06]  Well, as we come near to a close here in our conversation,
[2549.58 --> 2550.72]  we've talked about search,
[2550.78 --> 2552.56]  we've talked about evolutionary algorithms,
[2552.56 --> 2553.82]  we've talked about Rust.
[2554.16 --> 2556.68]  I'd be curious just to hear about,
[2556.68 --> 2562.04]  what you're excited about in terms of the search space
[2562.04 --> 2565.12]  and how AI is influencing that space
[2565.12 --> 2565.96]  as we look forward.
[2566.18 --> 2568.14]  What are the biggest open problems
[2568.14 --> 2570.92]  that you think are really interesting
[2570.92 --> 2572.36]  that people are working on?
[2572.58 --> 2574.72]  Or what are you just excited about
[2574.72 --> 2577.78]  kind of over the next years as the community grows?
[2578.30 --> 2579.36]  Yeah, that's a wonderful question.
[2579.74 --> 2582.92]  So we've never lived in a more exciting time for search.
[2582.92 --> 2586.76]  We have this kind of openness now in industry
[2586.76 --> 2589.08]  in terms of publishing state of the art.
[2589.22 --> 2591.68]  You have Alibaba who's been making a lot of work recently
[2591.68 --> 2594.70]  and then the classics like MSR and Google
[2594.70 --> 2599.04]  and other folks who are really publishing great research
[2599.04 --> 2601.22]  on how to both build production grade systems
[2601.22 --> 2602.92]  and how to kind of push the state of the art
[2602.92 --> 2605.10]  in terms of retrieval.
[2605.66 --> 2606.72]  At KDD this year,
[2606.82 --> 2609.64]  one of the big workshops was from LinkedIn
[2609.64 --> 2611.62]  and they published this fabulous deck
[2611.62 --> 2614.24]  on how they've kind of integrated machine learning
[2614.24 --> 2616.56]  at every level of their search platform.
[2617.16 --> 2618.72]  So using things like GANs
[2618.72 --> 2622.10]  and using BERT to kind of tease apart the NLP pieces.
[2622.38 --> 2624.54]  Then you have great papers
[2624.54 --> 2626.42]  talking about how folks like Amazon
[2626.42 --> 2629.02]  are embedding billion parameter neural nets
[2629.02 --> 2631.40]  inside of their information retrieval stacks.
[2632.22 --> 2633.70]  So these real production problems
[2633.70 --> 2637.16]  that folks like Chinese e-commerce companies deal with
[2637.16 --> 2638.20]  such as Singles Day, right?
[2638.20 --> 2640.30]  How do you handle the scale of those systems?
[2641.02 --> 2643.40]  And one of the things that I've been starting to see
[2643.40 --> 2644.60]  as a trend over the last few years
[2644.60 --> 2648.00]  is that the blending between lines
[2648.00 --> 2649.46]  of where machine learning starts
[2649.46 --> 2651.04]  and distributed systems
[2651.04 --> 2652.52]  and systems engineering starts
[2652.52 --> 2655.90]  is starting to be a little bit fuzzier.
[2656.40 --> 2658.94]  And it turns out that the best search systems
[2658.94 --> 2661.52]  are really going to incorporate techniques
[2661.52 --> 2665.66]  from both worlds into the code that's being built
[2665.66 --> 2667.80]  rather than kind of having them segregated apart.
[2668.20 --> 2671.74]  So all the improvements that we get out of conferences
[2671.74 --> 2674.76]  like NERFs and ICLR and SIG IR
[2674.76 --> 2676.26]  and all these wonderful conferences,
[2676.26 --> 2678.82]  we're finding they're making their way faster into search
[2678.82 --> 2680.60]  to actually solve real problems.
[2681.10 --> 2681.70]  Awesome.
[2682.04 --> 2683.24]  That's great to hear.
[2683.42 --> 2686.36]  And I definitely resonate with a lot of what you said,
[2686.40 --> 2686.92]  like I mentioned.
[2686.92 --> 2690.60]  And I certainly hope that we do see some of those trends.
[2690.60 --> 2694.06]  And of course, we'll keep looking for great things
[2694.06 --> 2697.38]  coming out of Etsy and what you're contributing to search.
[2697.94 --> 2702.44]  And really appreciate you releasing your findings
[2702.44 --> 2705.76]  and other things, like you said, with Buzzsaw and other things.
[2706.02 --> 2707.30]  So yeah, great work.
[2707.30 --> 2710.54]  And thank you so much for taking time to talk with us.
[2710.84 --> 2711.84]  I really appreciate being here.
[2711.90 --> 2712.26]  Thank you.
[2712.26 --> 2714.98]  All right.
[2715.04 --> 2717.64]  Thank you for tuning into this episode of Practical AI.
[2717.90 --> 2719.38]  If you enjoyed this show, do us a favor.
[2719.50 --> 2720.90]  Go on iTunes, give us a rating.
[2721.14 --> 2723.02]  Go in your podcast app and favorite it.
[2723.12 --> 2724.82]  If you are on Twitter or social network,
[2724.94 --> 2725.84]  share a link with a friend.
[2725.90 --> 2726.60]  Whatever you got to do,
[2726.74 --> 2728.28]  share the show with a friend if you enjoyed it.
[2728.54 --> 2731.24]  And bandwidth for ChangeLog is provided by Fastly.
[2731.36 --> 2732.80]  Learn more at Fastly.com.
[2732.80 --> 2735.34]  And we catch our errors before our users do here at ChangeLog
[2735.34 --> 2736.20]  because of Rollbar.
[2736.40 --> 2738.80]  Check them out at Rollbar.com slash ChangeLog.
[2738.90 --> 2741.60]  And we're hosted on Linode cloud servers.
[2741.96 --> 2743.56]  Head to Linode.com slash ChangeLog.
[2743.66 --> 2744.12]  Check them out.
[2744.20 --> 2745.02]  Support this show.
[2745.44 --> 2748.60]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2749.06 --> 2751.12]  The music is by Breakmaster Cylinder.
[2751.54 --> 2754.96]  And you can find more shows just like this at ChangeLog.com.
[2755.04 --> 2757.10]  When you go there, pop in your email address,
[2757.38 --> 2759.90]  get our weekly email keeping you up to date with the news
[2759.90 --> 2762.40]  and podcasts for developers in your inbox.
[2762.40 --> 2764.58]  Thanks for tuning in.
[2764.72 --> 2765.46]  We'll see you next week.
