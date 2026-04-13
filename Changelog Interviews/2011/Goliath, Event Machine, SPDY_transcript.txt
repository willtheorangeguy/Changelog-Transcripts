[0.00 --> 18.06]  Welcome to the Changelog episode 0.5.5.
[18.24 --> 19.32]  I'm Adam Stachowiak.
[19.66 --> 20.56]  And I'm Wyn Netherland.
[20.70 --> 21.62]  This is the Changelog.
[21.66 --> 23.54]  We cover what's fresh and new in the world of open source.
[23.98 --> 26.54]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.68 --> 27.60]  We're also up on GitHub.
[27.60 --> 29.64]  Head to github.com slash explore.
[29.74 --> 33.90]  You'll find some training repos, some feature repos from the blog, as well as our audio podcast.
[34.16 --> 37.62]  And if you're on Twitter, follow Changelog Show and me, Adam Stach.
[38.04 --> 40.36]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.56 --> 42.64]  This episode is sponsored by GitHub Jobs.
[42.74 --> 45.48]  Head to the changelog.com slash jobs to get started.
[46.00 --> 51.62]  If you'd like us to feature your job on this show, select advertise on the changelog when posting your job, and we'll take care of the rest.
[52.28 --> 56.26]  Mogui's looking for an iOS, Android, Windows, mobile app developer.
[56.26 --> 63.50]  Mogui's backed by Marc Andreessen's Ning, and they're looking for someone that is familiar with the mobile platform.
[63.72 --> 65.82]  Preferably Java C++ experience.
[66.88 --> 70.48]  B-S-R-M-S in computer science is a plus.
[70.82 --> 76.20]  If you're interested in full-time in Palo Alto, apply at lg.gd slash 9L.
[77.24 --> 81.08]  Python is in big demand over at Urban Mapping.
[81.08 --> 86.42]  So they're the developer's core team of MapFluence, their hosted mapping and analytics platform.
[86.92 --> 90.00]  Looking for also a bachelor's of science, computer science.
[90.64 --> 93.92]  Expert at Python and Django and RESTful Web Services.
[94.50 --> 99.82]  Also a big plus if you know MapReduce, Pig, Cascading, Hadoop, there it is.
[100.04 --> 101.26]  All sorts of NoSQL stuff.
[101.70 --> 104.08]  If you're interested, lg.gd slash 9E.
[104.08 --> 109.06]  Fun episode this week, talk to Ilya Grigorik over at PostRank.
[109.66 --> 117.36]  Got the scoop on Goliath, their invented non-blocking asynchronous Ruby framework built on top of the event machine, which is really, really cool.
[117.64 --> 118.34]  That's a mouthful.
[118.66 --> 119.34]  It is a mouthful.
[119.42 --> 126.90]  I got the scoop on why our PostRank numbers don't show any interaction with our feed.
[126.90 --> 133.82]  So pointing me to some things we can fix to fix up our Tumblr feed so that we can see who's interacting with our content.
[134.32 --> 135.04]  All 12 of you.
[135.24 --> 138.32]  We had a couple design episodes there, but I have to comment on their design.
[138.40 --> 139.30]  Their design is phenomenal.
[140.16 --> 141.54]  PostRank, yeah, we got into that.
[142.42 --> 145.00]  You know, Ilya said he started with a Photoshop background.
[145.14 --> 151.98]  And he was a designer first and got into development out of necessity and made a career out of it.
[151.98 --> 153.46]  You know, he's a founder over at PostRank.
[153.52 --> 160.80]  They do some really, really cool things around social media analytics and things and some really high volume throughput.
[161.20 --> 162.46]  And they do it all in Ruby.
[162.54 --> 164.06]  Who says Rails can't scale?
[164.30 --> 164.64]  That's right.
[164.74 --> 166.20]  Who says that stuff?
[166.44 --> 167.38]  I know some other podcast.
[167.56 --> 169.10]  It's ours, but some other podcast.
[169.48 --> 169.68]  Yeah.
[169.88 --> 171.34]  Well, what do we have to promote this week?
[173.94 --> 174.34]  Me?
[174.78 --> 175.04]  Me?
[175.24 --> 175.44]  You?
[176.26 --> 177.18]  Oh, RedDirtRubicon.
[177.38 --> 177.92]  Don't miss it.
[177.92 --> 183.04]  A little birdie told me there's a special bare bones package that just went on sale today.
[183.12 --> 186.72]  $199 gets you into the conference if you don't need anything.
[187.34 --> 187.86]  There you go.
[187.94 --> 192.96]  And we're also ordering another packet of stickers, so stay tuned to that as well.
[193.86 --> 194.18]  Cool.
[194.28 --> 201.32]  If you are at CodeConf this weekend, catch, I believe, Kenneth and Steve are going to be out there.
[201.32 --> 206.28]  And if you are at RedDirtRubicon, as we mentioned, look us up.
[206.32 --> 209.50]  We'll be doing a special live episode on the 21st.
[209.64 --> 210.58]  Looking forward to that.
[210.96 --> 213.56]  And stay tuned to some other great stuff this summer.
[214.02 --> 214.18]  Cool.
[214.78 --> 215.36]  Fun episode.
[215.46 --> 215.98]  Want to get to it?
[216.24 --> 216.96]  Let's do it.
[226.10 --> 229.00]  Chatting today with Ilya Gregorik from PostRank.
[229.00 --> 232.28]  So Ilya, why don't you introduce yourself and a little bit about your role at PostRank.
[233.68 --> 234.08]  Sure.
[234.30 --> 239.10]  So I'm the founder, CTO, I guess, of PostRank.
[239.26 --> 241.26]  We're a fairly small company and startup.
[241.52 --> 245.02]  About 15 people at this point up in Waterloo, Canada.
[245.88 --> 250.52]  And we're aggregating quite a bit of data from the social web.
[251.18 --> 255.68]  Ended up building a framework called Goliath to do a lot of our API serving.
[255.84 --> 256.86]  So here we are today.
[256.86 --> 263.46]  You know, I think your name in Ruby circles has become almost anonymous with performance
[263.46 --> 267.42]  and high performance Ruby scaling and things of that sort.
[267.58 --> 273.10]  So what's your, I guess, journey to performance been like with Ruby and web frameworks?
[274.80 --> 277.06]  Well, that's an interesting and loaded question.
[277.06 --> 286.70]  And as far as Ruby and performance and, you know, that's, so I think a lot of that work,
[286.94 --> 292.28]  especially stuff that you read on my blog, has come around by necessity more so than anything.
[292.28 --> 299.94]  It certainly wasn't a, you know, a motivated or coordinated move towards that.
[300.08 --> 307.12]  It's just when we started PostRank, we, our focus has been around aggregating lots and lots of data.
[307.34 --> 316.78]  So what today, I guess, is often called big data, archiving it and then processing it for a variety of kind of internal use case and also our clients.
[316.78 --> 323.06]  And it just so happens that Ruby was kind of my favorite language at the time.
[323.06 --> 325.36]  So we chose it as the primary platform.
[326.16 --> 331.48]  And throughout that whole experience, we basically tried to figure out, you know, how do we make use of Ruby?
[331.58 --> 335.94]  Because we were using it on the front end for stuff like Rails and everything else.
[336.08 --> 342.32]  And we loved the productivity that it enabled us to have in terms of developing new products and just iterating very fast,
[342.82 --> 350.34]  being able to reliably test and quickly test all this stuff, you know, unit testing, integration testing and all the rest.
[350.34 --> 355.24]  And we wanted to propagate all of that experience throughout our entire infrastructure.
[356.08 --> 364.86]  So that led to lots of interesting kind of optimization work in terms of, you know, we needed to build fast crawlers to collect that data.
[365.06 --> 366.82]  So how do you do that with Ruby?
[366.98 --> 374.74]  And that, frankly, that's what got me started in many ways down this whole path of web servers and clients and all the rest.
[374.74 --> 379.32]  And then extending that to, okay, well, we downloaded this data.
[379.56 --> 385.16]  Now we need to push it through five or six stages of processing.
[385.50 --> 391.52]  So let's say you downloaded an RSS feed, which is something that smells like XML.
[391.90 --> 393.00]  It's not quite RSS.
[394.58 --> 397.04]  It's malformed XML at that point.
[397.58 --> 402.22]  You know, let's transform it to something like JSON, which is something that we can actually work with.
[402.22 --> 405.44]  And then let's run it through language analysis and all of these different steps.
[405.82 --> 408.80]  So just trying to coordinate all of those steps and how do you do that?
[408.88 --> 411.16]  You know, what is the architecture that makes sense?
[411.72 --> 415.86]  What is the right choice of language or library for all of those things?
[415.86 --> 426.90]  So long story short, I think almost everything you'll find, for example, on my blog is directly correlated to what we've been doing
[426.90 --> 430.46]  or at some point researching or trying to improve within our infrastructure.
[430.46 --> 439.82]  And that's, quite frankly, been more by necessity than, you know, any specific reason for, okay, I need to optimize this specific step of the infrastructure.
[440.74 --> 448.18]  You know, your blog, igvita.com, has been a great resource for me learning different tools in the Ruby stack.
[448.44 --> 451.24]  And a set of those has been NoSQL options.
[451.36 --> 453.30]  I think you've played with every one of them out there.
[453.38 --> 453.90]  Do you have a favorite?
[453.90 --> 456.96]  I do and I don't.
[458.40 --> 460.72]  There's ones that we use and there's ones that we don't.
[461.38 --> 466.42]  You know, as everybody else, I think at this point, quite fascinated with everything that's going on in the space.
[466.96 --> 468.80]  It's definitely been a bit of an explosion.
[468.80 --> 474.44]  And just trying to dig in beyond just a feature list, right?
[474.48 --> 477.42]  And trying to really understand what's going on.
[477.50 --> 478.46]  What's the data schema?
[478.62 --> 481.80]  How does it actually affect how you are?
[482.60 --> 492.64]  Because ultimately, I think a lot of these solutions come down to you really need to put a lot of thought up front in terms of what you're designing for or what are you optimizing for?
[492.64 --> 498.86]  Because frankly, MySQL is probably the right answer in 90% of the use cases still for most people.
[500.06 --> 504.04]  And, you know, as developers, we may not like that because it's not the shiny new thing.
[504.22 --> 511.50]  But usually that's, you know, when you align the business goals with what you actually should be doing, that's usually the right solution.
[512.30 --> 515.92]  But having said that, you know, we've at Postrink specifically, we've deployed.
[516.74 --> 517.68]  Oh, let's see.
[517.78 --> 519.36]  So we definitely have a lot of MySQL.
[519.36 --> 525.32]  Well, we're running a fairly large, scaling up a fairly large Cassandra cluster at this point in time.
[526.32 --> 531.56]  We're logging about 50 or 60 gigs of data into it every day today.
[532.42 --> 536.48]  We have MongoDB for some, you know, highly unstructured data.
[536.78 --> 537.90]  And it's great for that.
[538.04 --> 540.82]  We have Redis for some of the data structure stuff.
[541.10 --> 542.16]  We definitely have Memcache.
[543.24 --> 545.96]  So, you know, it's a mixed bag of tools.
[545.96 --> 550.82]  And I think you need to pick the right tools for the right job.
[551.06 --> 553.60]  It's not just a matter of, you know, having a favorite.
[554.40 --> 556.56]  You just need to know what each tool is good for.
[557.80 --> 561.94]  Let's switch over and talk about Goliath, your new project that runs on top of Vent Machine.
[562.12 --> 563.34]  So how did this project come about?
[564.74 --> 564.90]  Yeah.
[565.00 --> 568.98]  So that's, so Goliath is definitely not new from our perspective.
[568.98 --> 580.88]  And the background on this guy is, you know, we actually started work on, I guess, the first version of Goliath back in, oh boy, early 2008.
[581.58 --> 586.60]  So this has actually been something that, a framework that we've been using and iterating on for a while.
[587.20 --> 594.04]  And what we released recently is technically the version four of our internal API stack.
[594.04 --> 604.62]  And back when we started in 2008, one of the first things that we realized was the ecosystem around Ruby web service wasn't that great.
[606.32 --> 613.10]  I believe, more effectively kind of the de facto deployment target.
[613.92 --> 619.22]  And we wanted something that wouldn't lock us into the threat model.
[619.38 --> 621.84]  We wanted something that would give us higher concurrency.
[621.84 --> 625.84]  And, you know, we started looking around at the available alternatives.
[627.38 --> 630.30]  Thin was, you know, just coming around.
[630.52 --> 635.48]  It wasn't, I wouldn't even call it a production ready mode at that point.
[636.24 --> 645.12]  Eb, if you remember that, that guy, which later evolved into Node.js, of course, you know, made some rounds.
[645.12 --> 657.46]  But none of the solutions were really there in terms of providing a full stack, you know, for testing, development, or even a sensible DSL at that point.
[657.58 --> 658.60]  They were all pretty raw.
[659.18 --> 663.48]  So given all of that, we effectively started our own project around it.
[663.66 --> 666.80]  And the first version of Goliath started as just one file.
[666.80 --> 669.16]  It was very simple.
[669.40 --> 670.66]  It was fast.
[671.00 --> 673.46]  It served just our needs and nothing else.
[674.84 --> 677.68]  As, you know, most projects start.
[678.36 --> 684.60]  And then over time, we've started iterating and made a lot of different mistakes along the way.
[684.80 --> 687.30]  Hence the version 4 by the end.
[688.10 --> 691.28]  You know, we had a mixed model where it was first fully evented.
[691.28 --> 697.72]  Then we went a mix of threads and events, which was, it worked, but it was, you know, lots of lessons learned there.
[698.50 --> 702.36]  We did a complete rewrite with version 3, which is completely evented.
[702.82 --> 704.58]  Didn't like where it actually ended up.
[704.70 --> 708.86]  And then ended up with version 4, which is the most recent one, which is the one we open sourced.
[708.86 --> 717.04]  And today I'm going to call Goliath kind of the, you know, 85, maybe approaching the 90% solution.
[717.04 --> 721.32]  It's very simple to write a Hello World app from scratch.
[721.80 --> 723.12]  You know, that's very fast.
[723.28 --> 730.76]  That runs in a raw TCP socket and serves, I don't know, some insane amount of requests per second.
[731.68 --> 735.66]  It's fairly hard to get to an 80% solution.
[736.22 --> 741.30]  You know, you really need to start to put some thought around how you handle all the edge cases in HTTP spec.
[742.14 --> 746.26]  Handle all the, you know, how do you develop a good DSL random and all the rest.
[746.26 --> 750.40]  And then getting to, you know, 90 and 100% is very hard.
[750.60 --> 751.86]  That takes literally years.
[752.24 --> 760.14]  And I think Goliath is kind of getting to that point, even though it's new in terms of being as an open source project.
[760.70 --> 765.20]  It's definitely been something that we've worked on and spent a lot of time working on for the past couple of years.
[766.28 --> 769.16]  So at its core, Goliath is a non-blocking framework.
[769.58 --> 773.82]  How much of a barrier to entry is that for the average Rubyist, do you think?
[773.82 --> 779.22]  Well, that's an interesting question.
[779.40 --> 792.04]  I'm not sure that it's much more of a barrier than any other framework because what we tried to do with Goliath is actually to simplify the,
[792.04 --> 797.04]  or hide almost, the fact that it's completely asynchronous under the hood.
[797.24 --> 801.76]  So, of course, you know, the first thing that you should think about when you hear asynchronous is,
[802.44 --> 805.38]  what does that mean for the programming style, right?
[805.44 --> 814.38]  Usually when you think about asynchronous, you end up defining, having to define callbacks and functions which fire at some later time when the event completes.
[814.38 --> 824.20]  So Node.js is something that you guys have discussed at length on this show before, and that's definitely a great example of that, right?
[825.30 --> 833.24]  With Goliath, we actually try to take advantage of some of the features that Ruby 1.9 exposes to hide some of that complexity.
[833.24 --> 842.42]  And, you know, maybe I should step back here and say that the version 3 that we wrote internally for Goliath was actually completely asynchronous.
[843.12 --> 850.74]  And it was very much the same flavor as Node.js with all the libraries, except it was in Ruby.
[850.74 --> 870.32]  And what we found, though, was after we ran with that for about six months, we found that the APIs that we were building were getting complicated enough such that the testing and the maintenance of them was becoming very, very expensive for us.
[870.82 --> 872.30]  The code became complex.
[872.56 --> 875.60]  You know, it was very hard to maintain in an ongoing basis.
[875.60 --> 879.28]  So we took a step back and said, look, this is not going to scale.
[879.84 --> 881.16]  How do we solve this problem?
[881.66 --> 890.04]  And we started looking around and realized that Ruby 1.9 has this really nice feature called fibers, which are continuations.
[890.34 --> 898.68]  And if we were to do some extra work under the hood and within the actual library, we could actually hide a lot of the complexity of these callbacks.
[898.68 --> 912.46]  So we can, on behalf of the developer, effectively, instead of having to define a callback, we could do it for you and then make it look as if you have a completely synchronous API.
[912.82 --> 922.84]  So at the end of the day, when you look at a Goliath, when you look at the code that you write for a Goliath API, it looks completely synchronous.
[922.84 --> 933.52]  So you could, in fact, you know, take your Rails code and pretty much copy it over and not worry about having to define extra functions, callbacks, and all the rest.
[934.04 --> 936.68]  You have very logical flow.
[937.00 --> 942.56]  If else, you don't have to worry about callbacks and urbacs and all this kind of stuff.
[942.70 --> 946.50]  So our goal was to actually simplify it such that you don't have to think about it.
[946.50 --> 960.08]  And I think we succeeded at that because, you know, for new guys that start with us at PostRank, we just give them the framework and they pretty much are oblivious to the fact that it's underneath, it's running on this asynchronous core.
[960.66 --> 964.78]  The only thing they have to pay attention to is, of course, the fact that they're using the right libraries.
[965.64 --> 967.34]  So they're not using a blocking library.
[967.60 --> 968.48]  So let's talk about that for a moment.
[968.58 --> 969.62]  That was going to be my next question.
[969.82 --> 974.02]  So what's the Ruby landscape look like for non-blocking libraries?
[974.02 --> 977.02]  It's pretty good.
[977.36 --> 977.92]  Is it growing?
[978.42 --> 982.02]  Compared to Node.js, which is like non-blocking, you know, by default, right?
[982.20 --> 985.60]  And so the whole ecosystem that grew up around it has been non-blocking.
[985.74 --> 991.24]  So Ruby, are we getting there or is it still a lot of work to be done to take advantage of this style of programming?
[993.54 --> 1002.74]  To be honest, I'm not sure how to answer that exactly because I think the most prevalently used framework within Ruby
[1002.74 --> 1005.34]  for doing this kind of programming is Event Machine.
[1006.14 --> 1014.22]  And Event Machine does have quite a bit of work and drivers that have been built around it for all of your common suspects.
[1014.22 --> 1020.84]  So, you know, anything from Memcache to MySQL to Cassandra to everything else, HTTP clients and so forth.
[1020.84 --> 1029.00]  So as far as getting, you know, good coverage in terms of your most common apps, I think it's all there.
[1029.38 --> 1035.36]  And I think most of the clients are in good functioning state and I haven't had too many problems with that.
[1035.36 --> 1050.60]  Now, it's interesting that you compare that to Node.js because intentionally or not, I think when Ryan picked JavaScript, right,
[1050.66 --> 1053.56]  he basically made a break with everything.
[1053.82 --> 1059.38]  He basically said, look, we're going to have to write completely new drivers for just about everything.
[1059.38 --> 1063.10]  And there's been a lot of work that's been done in that space now.
[1063.28 --> 1071.10]  And I think now if you're just starting with Node today, you already have a pretty good ecosystem of drivers for virtually all of the, you know,
[1071.30 --> 1072.96]  major components that you would need.
[1073.66 --> 1078.34]  But in the process of doing so, because he completely broke away from any other language,
[1078.34 --> 1085.68]  he basically forced the user to always make the right choice in some sense because you can't, in Node,
[1085.80 --> 1089.64]  you can't really make a mistake of picking the wrong driver.
[1090.92 --> 1097.44]  Whereas in Ruby, if you're developing Ruby, you have to be very conscious of what it is that you're doing
[1097.44 --> 1101.12]  because you could pull in some driver that all of a sudden is doing the wrong thing
[1101.12 --> 1104.28]  and your performance goes out the door.
[1105.38 --> 1107.92]  So I think both are comparable.
[1108.34 --> 1113.78]  You know, there's obviously a reason as to why we chose to stick with developing Goliath.
[1114.38 --> 1120.02]  And fundamentally, I think, you know, there's no reason to break apart from the Ruby language
[1120.02 --> 1123.00]  and force yourself down the JavaScript path.
[1123.54 --> 1125.96]  And I should say, I love JavaScript.
[1126.12 --> 1127.02]  There's nothing wrong with it.
[1127.04 --> 1127.80]  It's a great language.
[1128.40 --> 1131.16]  But I just enjoy Ruby so much more.
[1131.16 --> 1138.90]  And the type of code that you can write with stuff like fibers and all the rest is, to me, much more readable and maintainable.
[1139.80 --> 1145.12]  And hence, hence our development and all of the work around Goliath.
[1145.80 --> 1151.76]  The fact that we can reuse components like RSpec, Cucumber, and all the rest to drive our tests,
[1151.76 --> 1154.96]  and we have access to all of the Ruby standard library.
[1155.70 --> 1157.76]  It's kind of, it's a double-edged sword, right?
[1157.80 --> 1164.08]  On one hand, you break apart from bad gems and libraries which are blocking where they shouldn't be.
[1164.34 --> 1169.86]  But at the same time, you do have the full capability and library of all of the Ruby gems.
[1169.86 --> 1172.50]  So you just have to be a little bit more careful.
[1174.56 --> 1179.64]  Speaking of the Ruby library and the standard library and the ecosystem of Ruby gems around it,
[1179.96 --> 1185.02]  as a community, how do you think we're adapting to the move to 1.9?
[1187.14 --> 1190.88]  I'm actually really pleased to see that a lot more people are migrating.
[1191.48 --> 1197.90]  I believe just a couple of days ago, I saw some announcement from the Rails core
[1197.90 --> 1203.06]  saying that the next version of Rails will require Ruby 1.9.
[1203.16 --> 1206.96]  So it's no longer a suggested option, it's a required option.
[1207.60 --> 1209.66]  And I think that's obviously big news.
[1209.84 --> 1217.22]  And I think overall, even though it seems like it took a little bit longer than it should have
[1217.22 --> 1221.50]  to start moving the community to 1.9,
[1222.06 --> 1226.02]  there seems to be a fairly big shift that has happened, I'm going to say,
[1226.02 --> 1231.98]  in the last six to eight months, where more and more people are adopting 1.9 as their default platform.
[1232.52 --> 1235.16]  And I think there's many different reasons for that.
[1235.56 --> 1238.96]  Some of it is just availability of better tooling around it,
[1239.60 --> 1241.38]  like RVM and everything else,
[1241.50 --> 1244.94]  that just make it much, much easier to both develop and deploy
[1244.94 --> 1248.86]  against multiple runtimes.
[1248.86 --> 1255.64]  And then just the fact that more and more gem authors are paying attention to 1.9 now.
[1255.92 --> 1262.52]  So I've been running on 1.9 as my primary platform for almost a year and a half or two years at this point.
[1262.62 --> 1264.32]  I developed all my gems on 1.9.
[1264.96 --> 1268.60]  I only switched back to 1.8 to run the spec test.
[1268.60 --> 1271.94]  And I think that's becoming the default now.
[1272.10 --> 1275.74]  So I'm happy to say that we're getting there.
[1277.20 --> 1281.76]  So in the readme for Goliath, you mentioned performance numbers on MRI, JRuby, and Rubinius.
[1282.12 --> 1289.10]  How important was it to you to publish those and support Goliath on a multiple Ruby stack?
[1289.10 --> 1296.00]  So I think this is one area that I'd love to explore in the future with Goliath.
[1296.30 --> 1302.62]  So initially, we developed Goliath to run on 1.9 MRI specifically, so the CRuby.
[1303.12 --> 1308.64]  And we had a couple of dependencies in there which were specifically C extensions.
[1308.86 --> 1316.54]  So for example, Thin can only run on MRI because it uses the mongrel parser and some C code under the hood.
[1316.54 --> 1321.58]  And of course, Event Machine itself is a C++ core.
[1322.40 --> 1324.86]  But Event Machine also has a Java version.
[1325.84 --> 1335.88]  So when we were developing Goliath, we tried to find and remove any bottlenecks that would not allow us to run on multiple runtimes.
[1336.24 --> 1339.08]  So we wanted to be able to run on JRuby.
[1339.80 --> 1345.78]  And part of the reason for that is MRI has a global interpreter log.
[1345.78 --> 1357.06]  And you're basically stuck to a single core, which is the same story for Node.js and virtually other evented servers out there.
[1357.48 --> 1365.40]  But if you could imagine running Goliath on, let's say, JRuby, which doesn't have a global interpreter log,
[1365.40 --> 1377.80]  then in theory, nothing stops us from spinning up a bunch of operating system or OS threads and running multiple reactors within the same process.
[1378.22 --> 1385.34]  And that, of course, opens up a lot of interesting opportunities for simplifying the deployment and doing all this kind of stuff.
[1385.34 --> 1392.50]  So to be honest, it was when we were removing these bottlenecks, we were looking a little bit more to the future.
[1392.50 --> 1405.70]  So with the hope that as these alternative runtimes, and I know many people wouldn't consider, or rather would consider JRuby to be their primary runtime, not an alternative runtime.
[1405.70 --> 1415.72]  As these systems develop, we can take advantage of the performance that they can offer us with Goliath.
[1416.30 --> 1421.94]  And, for example, JRuby is a very interesting one that I'm looking forward to investigating in the future,
[1421.94 --> 1429.54]  because at the moment, fibers, which we depend on fairly heavily in Goliath, are pretty slow in JRuby.
[1429.82 --> 1437.20]  They are mapped directly to operating system-level threads, so expensive to spin up and maintain.
[1437.92 --> 1447.20]  But there is some patches and work in JRuby that should change that dramatically to the tune of making it even faster
[1447.20 --> 1452.42]  than kind of the lightweight processes that we have currently on MRI.
[1452.94 --> 1461.26]  And when that happens, it could well be the case that Goliath will run just several times faster on JRuby than does on MRI.
[1462.08 --> 1466.96]  And I think that's a great story, that we don't have to lock ourselves to a specific runtime.
[1468.04 --> 1475.04]  So you mentioned in the ReadMe, suggesting that you stand this up behind an HA proxy or Nginx equivalent.
[1475.38 --> 1476.06]  What do you guys run?
[1477.20 --> 1481.04]  Primarily, HA proxy.
[1481.22 --> 1483.88]  That's kind of our primary weapon of choice.
[1484.16 --> 1487.64]  We do have some Nginx processes deployed.
[1488.42 --> 1500.36]  The reason we prefer HA proxy is because it allows us to have much more control over the load balancing and all the other parameters.
[1501.16 --> 1504.24]  So more intelligent failover and all the rest.
[1504.24 --> 1515.60]  And when we need additional features that Nginx can expose, for example, do GZIP compression for us or something else, then we deploy it as needed.
[1517.96 --> 1520.28]  Talk a bit, if you would, how you're using it at PostRank.
[1520.28 --> 1521.28]  Goliath?
[1521.28 --> 1522.28]  Goliath?
[1522.28 --> 1523.06]  Yes.
[1523.06 --> 1527.86]  So Goliath we have deployed for a number of different applications.
[1527.86 --> 1539.94]  One of the choices that we made very early on in terms of architecture was to build a lot of our own infrastructure within PostRank around the idea of web services.
[1539.94 --> 1549.44]  So instead of specifying or using some sort of RPC mechanism, let's just use HTTP as our primary source.
[1549.54 --> 1552.00]  So everything should talk over JSON and over HTTP.
[1552.00 --> 1564.96]  So we rely on a lot of very high-performance endpoints within our system, which are serving hundreds of requests a second for our own internal use and for our clients.
[1565.04 --> 1566.24]  So we share the same endpoints.
[1567.18 --> 1579.52]  So to do that, obviously, we need something that is able to handle the concurrency and also to be able to handle features like HTTP pipelining, keep alives, to minimize the overhead.
[1579.52 --> 1587.52]  So internal services for kind of request-response style requests.
[1587.76 --> 1589.54]  We have streaming APIs.
[1589.98 --> 1598.04]  So, for example, if you've ever worked with the Twitter search API, which is you open a connection and just feeds you data, JSON data.
[1598.42 --> 1600.32]  We have some of those deployed as well.
[1600.52 --> 1602.78]  So we're streaming data over Goliath.
[1602.78 --> 1625.92]  Goliath is also capable of doing streaming uploads, which is something that we added fairly recently, such that, for example, if a client is pushing you a, I don't know, let's say a 5 megabyte image and you want to store that into S3, you don't have to buffer that in memory, which is what most web servers do today, at least in the Ruby space.
[1625.92 --> 1628.92]  And then they give you the whole image and then you can push it to S3.
[1629.40 --> 1635.74]  Goliath actually allows you to progressively load that and push it directly to S3.
[1637.36 --> 1640.18]  So those would be the primary use cases.
[1641.06 --> 1654.02]  But between the keepalive support, pipelining, and the streaming APIs, we easily push tens of gigabytes of data through that stack every day.
[1655.92 --> 1662.88]  So the sort of client libraries you're using, I'm assuming you're doing some sort of parallel network transport for each of these.
[1662.94 --> 1666.16]  So what's your basic favorite transport library?
[1668.84 --> 1679.08]  So a lot of the, I'm not sure this is actually what you're asking, but a lot of the messaging and communication that we do in terms of coordinating web services within Postrank is done over AMQP.
[1679.08 --> 1690.96]  So, for example, some of the HTTP streaming web services that we have, they quite literally act as direct front ends to AMQP queues, right?
[1691.00 --> 1698.64]  Where we would connect to some endpoints after all the data has been processed and just stream that data to our clients.
[1700.20 --> 1700.44]  Oh, gotcha.
[1700.50 --> 1706.00]  So all of your HTTP transport is then just a long persistent connection streaming sort of API?
[1706.00 --> 1706.28]  Right.
[1707.74 --> 1707.90]  Yep.
[1708.10 --> 1708.36]  Gotcha.
[1710.48 --> 1718.24]  So Postrank, for those that don't know, is a way to show, among other things, a way to show what's popular on your particular blog.
[1718.56 --> 1722.66]  We're dying to use this on the changelog, but until we get off Tumblr, we can't.
[1722.70 --> 1723.96]  We've hit a snag.
[1723.96 --> 1737.96]  So Postrank uses the URLs that are in your feed to determine, I guess, what sort of participation your audience is having with your content by matching it to what's bookmarked in Delicious and other social venues.
[1738.72 --> 1744.52]  But Tumblr does not include the slug on the post items, right?
[1744.60 --> 1746.22]  So they have the integer at the end.
[1746.34 --> 1747.84]  So none of our content matches.
[1747.84 --> 1753.96]  So every day I get an email saying that my Postrank content is so sad because nobody's marking our stuff.
[1755.44 --> 1756.78]  Well, we can probably fix that.
[1757.28 --> 1774.12]  And actually, so the crazy thing that we do at Postrank is, as you mentioned, we aggregate this, what we call engagement activity, which is effectively any time somebody shares or does something around a piece of content on the web, we want to know about it.
[1774.12 --> 1786.64]  So we aggregate, for example, every tweet that contains a URL or every vote from Dig or Reddit or Hacker News and all these other sites and every comment from all these sites as well.
[1787.12 --> 1794.60]  So one way to picture what we're doing is we're trying to assemble a firehose of all the different firehoses of the activities around all this content.
[1794.60 --> 1799.98]  And we don't collect that data for specific URLs that we care about.
[1800.06 --> 1802.18]  We collect that data for all of the URLs.
[1803.10 --> 1806.08]  So as you can imagine, that's quite a bit of data.
[1806.40 --> 1822.36]  So even though the plugin that you're referring to, which is the top posts widget that we have, is not picking up the right URL, we have all the tweets and everything else for content around the changelog show.
[1822.36 --> 1827.52]  So you can actually use our API and just send it all the URLs that you guys have created.
[1827.88 --> 1828.20]  Oh, gotcha.
[1828.70 --> 1834.20]  And you can get the actual metrics or you can actually get the full conversation as well.
[1834.60 --> 1841.04]  This is something that I alluded to earlier where we're pushing a lot of data into Cassandra.
[1841.18 --> 1842.46]  That's what we're using it for.
[1842.46 --> 1850.58]  We launched this project four or five months ago where every activity that we collect.
[1850.74 --> 1868.24]  So, for example, if somebody today shares a tweet with a link to the changelog, one of the changelog episodes, we'll actually store the content of that tweet and all the associated metadata about it and then allow you to look it up on a URL basis.
[1868.24 --> 1872.96]  So you can actually say, well, I have this URL, show me all the activity.
[1873.28 --> 1878.34]  So there's people bookmarking it on Delicious, there's tweets, there's hacker news comments and all the rest.
[1878.42 --> 1879.96]  And you can see that as just one stream.
[1882.40 --> 1886.16]  Now, I've seen you guys hire from time to time to switch topics for a moment.
[1886.16 --> 1895.70]  What would you tell the job candidate that was looking to get on it at PostStrength or that may be new to the Ruby community or new to even open source development?
[1895.90 --> 1899.14]  What, as an employer, do you look for in a developer?
[1901.32 --> 1902.14]  Well, let's see.
[1902.40 --> 1904.14]  A GitHub account.
[1904.50 --> 1906.34]  That's always a good place to start.
[1907.04 --> 1908.02]  And a blog.
[1908.02 --> 1916.34]  At the end of the day, and I've interviewed a lot of students specifically.
[1916.54 --> 1919.44]  So we're located in Waterloo in Canada.
[1919.82 --> 1925.74]  And Waterloo has a fairly well-known computer science program, University of Waterloo.
[1926.24 --> 1931.20]  So we interview a lot of co-op students for basically every semester.
[1931.36 --> 1932.38]  We have at least a couple.
[1932.38 --> 1952.96]  And, you know, honestly, one thing that always surprises me is I go through a pile of resumes, 50 to 100 each time, is the fact that out of those 50 or 100, they're all bright computer science students, very smart guys, usually guys, for good or for worse.
[1954.86 --> 1959.72]  Very few of them actually have something that they're passionate about.
[1959.72 --> 1964.72]  You know, very few of them have a blog or something that they've written or contributed to.
[1964.86 --> 1966.46]  Very few of them have a GitHub account.
[1967.02 --> 1975.48]  So, frankly, my first pass over that stack of resumes is always just to look for, do you have a blog or do you have a GitHub account?
[1976.04 --> 1980.40]  And I just, you know, usually there's at least three or five people that match.
[1980.72 --> 1982.64]  And I immediately put them to the side.
[1982.74 --> 1987.52]  And I know that I'm going to interview them even without considering or looking at the marks.
[1987.52 --> 1991.90]  Because they're already showing something that most people don't.
[1992.44 --> 2007.66]  But overall, I think the best people that we've hired, they've all had a consistent streak of having projects that they're passionate about, that they've contributed to, and having a history of kind of open source contribution.
[2007.66 --> 2012.00]  So, how did you come to Ruby and what language background did you come from?
[2013.80 --> 2017.58]  I think as many people, I started with PHP and Perl.
[2018.30 --> 2025.24]  I actually, I was never much of a computer geek, if you will.
[2025.24 --> 2030.04]  So, I got into web development through web design.
[2030.30 --> 2034.44]  I was one of the Photoshop wranglers for a while.
[2035.16 --> 2045.10]  And effectively got into the whole programming world by learning HTML and then learning that my clients wanted more dynamic sites.
[2045.10 --> 2047.16]  So, I started doing PHP and then Perl.
[2047.28 --> 2051.48]  And then before I knew it, I was in computer science.
[2051.70 --> 2053.44]  And then before I knew it, I was doing Ruby.
[2053.66 --> 2056.04]  So, it's kind of an odd path.
[2056.72 --> 2058.06]  You know, it's very similar to my own path.
[2058.18 --> 2061.98]  And I tell folks that I feel like Merlin, living my life backwards, started out on the front end.
[2062.04 --> 2069.32]  And I keep going deeper into the stack, you know, just trying to deliver on things that are in my head.
[2069.32 --> 2072.90]  And I think your blog just, you know, oozes that design.
[2073.16 --> 2080.96]  What sort of commonality do you see between design as a communication medium and programming as a communication medium?
[2082.02 --> 2085.22]  I think they're one and the same in many ways.
[2086.44 --> 2093.06]  To me, presentation is at least 50% of the actual deliverable product, whatever that product may be.
[2093.06 --> 2101.58]  And depending on the context, you know, that could be a nice packaging around your product.
[2101.72 --> 2107.72]  It could be a nice DSL project that you built.
[2108.44 --> 2111.56]  It could be a well-structured readme, right?
[2111.64 --> 2118.04]  The ability to actually communicate something to another person is kind of, I think, is the most important aspect.
[2118.04 --> 2121.42]  Then you really have to pay attention to what is the most important aspect.
[2121.68 --> 2127.80]  Because ultimately, the process of design is more about subtraction than adding stuff.
[2128.58 --> 2134.48]  So you really need to be clear about what it is that you're trying to communicate, whatever it is that you're working on.
[2134.64 --> 2138.78]  You know, new open source project or a new design template.
[2140.34 --> 2141.22]  Do you have a programming hero?
[2142.56 --> 2143.90]  A programming hero?
[2144.16 --> 2146.02]  Honestly, there's probably too many.
[2146.02 --> 2149.66]  Give us one and don't say Linus.
[2152.48 --> 2153.76]  Give us one.
[2156.50 --> 2164.80]  I think one person that impressed me early on was Brad Fitzpatrick.
[2165.16 --> 2168.52]  So, you know, Life Journal, Memcash, Payment, all the rest.
[2168.52 --> 2172.60]  And I can't even say specifically why.
[2173.48 --> 2180.12]  But I remember reading some interviews very early on about just how he started Life Journal.
[2180.12 --> 2190.40]  And the work that they were doing around Memcash, you know, ProBall and all the other projects that came out that, you know, a lot of us don't even think about today.
[2190.58 --> 2193.44]  But Ron, a lot of our infrastructure on.
[2193.44 --> 2199.38]  And how it was for him was always about just solving his own problem.
[2200.22 --> 2207.88]  You know, he never started with some grandiose vision of, you know, I need to build a really fast memory cache server.
[2207.88 --> 2211.92]  It's just I have this specific problem at my company.
[2212.54 --> 2215.86]  I started this project on a whim because my friend said I should.
[2216.04 --> 2218.18]  And, you know, here I am just slugging it out.
[2220.86 --> 2223.62]  Are we in a golden age of web development and perhaps just don't know it?
[2225.76 --> 2227.58]  Golden age of web development.
[2227.58 --> 2232.26]  Has there been a better time to be a bit pusher on the web?
[2236.34 --> 2239.36]  I think it's getting better and better, right?
[2239.50 --> 2248.48]  So when I think about the skill set that you have, I think it's an incredibly valuable skill set as a web developer.
[2248.48 --> 2257.48]  And I think it's only going to get more and more important, especially with the spread of technologies like HTML5 and everything else.
[2257.58 --> 2266.42]  When I think about, you know, one area that I haven't done much work on and I really want to kind of get into is mobile.
[2267.96 --> 2285.86]  And just based on my own observations and kind of research around that area, it seems like more and more larger organizations that have spent a lot of time and effort developing custom apps for each platform are now migrating to HTML5.
[2285.86 --> 2287.46]  Like Facebook is a great example.
[2288.30 --> 2293.14]  Twitter, all of these guys are converting their mobile clients to HTML5.
[2293.40 --> 2299.76]  And, you know, when you think of HTML5, of course, you know, you're doing CSS, JavaScript, and all the rest.
[2299.94 --> 2304.56]  So I think it's only going to get more and more important.
[2305.02 --> 2309.08]  In some ways, it's going to get more complicated, but it's also going to get more interesting as well.
[2309.08 --> 2314.28]  You know, every time I go to your site, I see the tagline, a goal is a dream with a deadline.
[2314.48 --> 2317.74]  And you're one of the most productive developers that I follow.
[2317.94 --> 2319.40]  Are you goal-oriented?
[2321.00 --> 2322.12]  Definitely, yes.
[2322.82 --> 2324.32]  So how do you manage that workflow?
[2327.02 --> 2327.90]  Well, let's see.
[2328.02 --> 2328.78]  Remember the Milk.
[2329.30 --> 2330.52]  I don't know if you've used the app.
[2330.60 --> 2330.88]  Oh, yeah.
[2330.88 --> 2333.80]  But I live and die by that thing.
[2334.24 --> 2340.90]  I don't think there's anything specific about Remember the Milk, short of just it's a great app built with a – it's very clean.
[2341.26 --> 2342.32]  It knows its purpose.
[2342.52 --> 2343.50]  It doesn't get in the way.
[2344.44 --> 2346.42]  But, you know, I definitely love my checklists.
[2347.48 --> 2350.82]  Are you a GTD guy or you have your own workflow inside there?
[2350.82 --> 2354.94]  I am definitely familiar with all the GTD stuff.
[2356.22 --> 2361.76]  Over time, I think I realized that it's not the process, right?
[2361.90 --> 2369.24]  It's – I think a lot of – rather, a lot of people spend a lot of time focusing on how to improve your process instead of actually doing stuff.
[2369.24 --> 2382.48]  So I can't say I'm, you know, I'm a diehard GTD person, but, you know, I definitely follow my inbox zero rules and make sure that I review my goals for the day or for the weekend and so on and so forth.
[2382.48 --> 2395.46]  So, you know, if there's any advice I could give to my college-age something self, it would be that a little effort every day will always outshine these big bursts of productivity.
[2395.46 --> 2403.36]  What are some of the habits that you have that you think have made you more productive as a developer?
[2405.94 --> 2408.38]  Well, I think it's exactly what you said.
[2408.80 --> 2412.22]  It's the small little things that add up over time, right?
[2412.30 --> 2420.62]  There's – I don't remember the exact quote, but the general message is, you know,
[2420.62 --> 2429.88]  we tend to overestimate what we can get done in a day and underestimate what we can get done in a week or a month.
[2431.28 --> 2442.14]  So, you know, it's not about doing heroic things on any given day as much as it is just having a clean path towards what's the next thing I need to do to move, you know, this thing along.
[2442.14 --> 2446.26]  So a couple of closing questions.
[2446.42 --> 2450.44]  Are you a Vim, TextMate, Emacs, or BBEdit guy?
[2453.62 --> 2459.64]  So I don't have any religious allegiances to any one of the editors.
[2460.06 --> 2468.26]  I do spend probably 50% of my time in Vim and TextMate.
[2468.26 --> 2471.70]  So I switch between the two quite a bit.
[2473.22 --> 2476.80]  This is where I outsource a lot of my discovery to my guests.
[2477.26 --> 2481.28]  So what one project do we need to post on the changelog that we haven't covered yet?
[2482.54 --> 2485.04]  Ah, one project.
[2486.94 --> 2492.36]  Does it count if I don't give you a project but instead a technology?
[2492.58 --> 2492.90]  Sure.
[2492.90 --> 2496.36]  So I've been digging into Speedy.
[2497.04 --> 2511.66]  And I don't know if you've paid attention to this but about a year ago or so, Google released this project or I guess a study that they did around a new protocol that they were trying to define called Speedy.
[2511.66 --> 2528.66]  And their goal was to see how can we speed up the performance of loading webpages, you know, the common webpages that we all visit, Yahoo.com, MSN.com, or even Google.com, by over 50%.
[2528.66 --> 2540.74]  And they took a low-level approach and said, well, you know, of course there's JavaScript optimization, compression, all the rest, but what we can do at protocol level.
[2540.90 --> 2547.30]  And they basically came up with a whole bunch of ideas around, well, HTTP is maybe not the ideal transport.
[2547.30 --> 2562.94]  When it was designed at the beginning, we didn't pay much attention to latency, you know, and later we've introduced a functionality like HTTP pipelining, keep alive, and all the rest, which frankly don't even work most of the time.
[2562.94 --> 2570.12]  So this is a little known fact, but HTTP pipelining is disabled in all browsers except Opera.
[2570.42 --> 2577.98]  And even Opera only uses it after some very weird edge cases where it can actually do so.
[2578.30 --> 2586.78]  And that's primarily because a lot of the servers don't support pipelining or when they claim it's supported, they don't actually do it properly.
[2587.16 --> 2590.74]  And then, of course, all the cache servers in between, which tend to break this kind of stuff.
[2590.74 --> 2596.28]  So it's not a great protocol at the end, it turns out.
[2596.80 --> 2605.00]  So Speedy is about redoing a lot of that work and basically building a new protocol instead of HTTP to replace it.
[2606.48 --> 2616.56]  And so they did this stuff about a year ago, released some numbers, and basically showed that, yes, we could, given some of these optimizations that we propose,
[2616.56 --> 2622.18]  we can actually get over 60% improvement in latency for delivering these web pages.
[2622.84 --> 2627.86]  They posted some source code, a client that was available in Chromium.
[2628.50 --> 2632.84]  And after that, I didn't see much coverage around this at all.
[2632.84 --> 2644.78]  And just recently, a thread popped up where they basically said that if you're running Chrome and you're talking to Google Web Services,
[2645.18 --> 2647.72]  then 90% of the traffic is going over Speedy.
[2649.08 --> 2649.68]  Right?
[2649.68 --> 2656.04]  So if you're a web developer today, there's high likelihood that you actually are using Chrome.
[2656.28 --> 2663.70]  And if you're using a Google Web Service, chances are you're not running over HTTP, you're running over Speedy, which is really, really interesting.
[2664.06 --> 2664.50]  That's amazing.
[2665.06 --> 2665.82]  Yeah, exactly.
[2666.54 --> 2672.14]  And I guess Google can actually do that because they control their own servers and they control the browser.
[2672.14 --> 2674.70]  So they're able to make this sort of change.
[2676.22 --> 2681.32]  But, of course, it's not a proprietary protocol.
[2681.84 --> 2682.76]  The spec is out there.
[2682.96 --> 2687.44]  So can we make use of that for our own web services?
[2687.72 --> 2698.34]  I would love to make PostRank web pages load 50% faster without actually modifying any of our UI code or anything in that respect.
[2698.34 --> 2703.26]  In fact, I'd love to just replace the web server and make it talk Speedy and off we go.
[2704.30 --> 2712.02]  Has anything materialized as far as an Apache module or anything like that to make it a little bit more palatable for the actual average developer?
[2712.90 --> 2715.70]  Yeah, so they actually released an Apache module.
[2716.06 --> 2722.22]  So if you're – I'm not sure how – I actually haven't tried it with something like, let's say, Passenger.
[2722.58 --> 2724.26]  I wonder if we can make that work.
[2724.26 --> 2736.24]  But what I've been digging into myself is I've been trying to build an actual parser for Speedy in Ruby, in pure Ruby.
[2736.38 --> 2738.88]  And this is more for kind of my own education.
[2739.10 --> 2746.32]  I find that the best way for me to learn is to actually try and build something because I can read the spec and I kind of nod along and I think I understand it.
[2746.88 --> 2749.80]  And then I start to write code and I realize that I didn't get it at all.
[2749.80 --> 2753.50]  So I'm actually working on one right now.
[2753.70 --> 2764.56]  And it's both very simple and very interesting in how they've made some of the decisions around how the packet exchange should be done.
[2765.04 --> 2771.70]  The fact that you can send multiple streams over the same TCP channel and they can be intermixed and all the rest.
[2771.70 --> 2789.60]  So definitely a project or a technology to look into for a lot of web developers, I think, because even though it's a fairly low-level web server type technology, I think it's something that we should be paying attention to because it's a significant improvement.
[2789.60 --> 2794.26]  You know, we've had pretty much the same transport stack for years.
[2794.36 --> 2805.04]  I can remember, I guess, 15 years ago or so, maybe more, having to download and install a PPP stack or a TCP IP stack for my operating system just to connect to the Internet.
[2805.32 --> 2812.78]  So, you know, maybe we're due for the next evolution on top of TCP for basic dial tone of the web.
[2812.78 --> 2842.76]  Yeah, absolutely.
[2842.78 --> 2872.76]  Oh, wow.
[2872.78 --> 2875.46]  So, you know, quick images in parallel.
[2876.72 --> 2882.72]  So you take that and then you take a look at technologies like XeromQ, right?
[2882.80 --> 2888.62]  And XeromQ is trying to do something similar but something more generic.
[2888.92 --> 2894.82]  They're saying, hey, look, TCP is great, but we need message-oriented messaging.
[2895.20 --> 2900.68]  You know, we shouldn't have to worry about parsing out where the message ends.
[2900.68 --> 2903.00]  All messaging should be message-oriented.
[2903.78 --> 2907.78]  And it all should be done, you know, as fast as possible.
[2908.12 --> 2910.16]  And you should have all these different transports.
[2910.42 --> 2915.38]  It shouldn't matter if you're sending data over TCP, UDP, or Unix pipe.
[2915.38 --> 2925.46]  So I think if you think about what Speedy is doing and XeromQ is doing, there's a really interesting opportunity there to connect the two and build something very interesting.
[2925.96 --> 2931.86]  You know, you could build a web server that is completely message-oriented.
[2931.86 --> 2939.76]  And you wouldn't need an HA proxy or an Nginx or anything else in between.
[2939.90 --> 2941.66]  You could just bring up a Ruby process.
[2941.80 --> 2942.88]  You would know where to connect.
[2943.04 --> 2950.98]  You would know how to parse that message without having to implement an entire parser in C just to parse out the boundaries of the message.
[2950.98 --> 2960.14]  And respond quickly without having to register with anybody or say that I'm up or down.
[2961.08 --> 2962.24]  Definitely exciting stuff.
[2962.32 --> 2965.04]  We learned about XeromQ on the Zed Shaw interview.
[2965.16 --> 2969.64]  That was the first time we'd heard of it and got a quick look at it there.
[2969.76 --> 2976.10]  We need to get somebody from the Chromium Project to talk about Speedy, which when I first saw it, I guess when it first came out, was it last year sometime?
[2976.10 --> 2981.02]  I thought it was Spidey, S-P-D-Y for those that are listening at home but don't have access to the show notes.
[2981.18 --> 2983.52]  Pronounced Speedy right here on the executive summary.
[2984.08 --> 2985.20]  Well, Ilya, thanks for joining us.
[2985.26 --> 2991.82]  It's definitely been fascinating to talk about Goliath and this non-blocking async style of programming and some other things.
[2992.86 --> 2993.72]  Great. Thanks a lot.
[3006.10 --> 3036.08]  Thank you.
