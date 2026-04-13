[0.00 --> 18.46]  Welcome to the ChangeLog episode 0.3.7.
[18.68 --> 19.70]  I'm Adam Stachowiak.
[19.98 --> 20.76]  And I'm Wynne Nethlin.
[20.94 --> 21.88]  This is the ChangeLog.
[21.92 --> 23.68]  We cover what's fresh and new in the world of open source.
[24.08 --> 26.82]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.90 --> 27.74]  We're also up on GitHub.
[27.74 --> 29.88]  Head to github.com forward slash explore.
[29.98 --> 34.10]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcasts.
[34.48 --> 36.56]  If you're on Twitter, follow ChangeLogShow.
[36.94 --> 38.04]  Not the ChangeLog.
[38.22 --> 38.98]  And I'm Adam Stach.
[39.46 --> 40.02]  And I'm Penguin.
[40.16 --> 41.74]  P-E-N-G-W-Y-N-N.
[42.10 --> 43.06]  Fun episode this week.
[43.16 --> 45.48]  Talked to Julian Guinness-Dew from Superfeeder.
[46.08 --> 48.60]  Talked about the real-time web feeds and more, huh?
[48.98 --> 49.98]  The real-time web.
[50.02 --> 51.58]  You know, it's a lot of new technologies.
[51.76 --> 52.64]  It's a changing landscape.
[52.64 --> 56.78]  So we talked about PubSubHubbub, which is a real-time web protocol.
[56.78 --> 57.90]  Also, XMPP.
[58.30 --> 60.34]  And touch briefly on WebSockets.
[60.50 --> 62.04]  And also, like, the Twitter streams.
[62.56 --> 64.70]  Yeah, a lot of this stuff is really just going to the real-time web.
[64.88 --> 65.98]  But it's pretty intense.
[66.04 --> 68.16]  WebSockets, Node, and everything else.
[68.50 --> 69.70]  We'll drop a link in the show notes.
[69.78 --> 72.02]  There's a really cool demo of Superfeeder in action.
[72.36 --> 74.30]  Pulling all the live check-ins from Goala.
[74.48 --> 77.02]  And someone's hooked it up to WebSockets and Chrome.
[77.06 --> 80.84]  And you can see a real-time Google map with all the check-ins from Goala.
[80.92 --> 81.48]  It's really interesting.
[81.72 --> 82.56]  Wow, that sounds fun.
[82.90 --> 83.36]  Fun episode.
[83.48 --> 84.00]  Should we get to it?
[84.18 --> 84.72]  Let's do it.
[84.72 --> 98.98]  We're chatting today with Julien Genestou from Superfeeder to talk about the real-time web and PubSubHubbub.
[99.34 --> 102.78]  Julien, why don't you introduce yourself and let the folks know who you are and why they should care.
[103.44 --> 103.78]  Sure.
[104.14 --> 104.52]  Hello.
[104.68 --> 106.50]  I am Julien Genestou, as you said.
[106.50 --> 109.32]  I am a French dude living in San Francisco.
[109.68 --> 116.82]  And I created a monster called Superfeeder, which actually aims at making the web real-time.
[118.16 --> 119.34]  Basically, that's what we do.
[119.64 --> 128.80]  And we do that using the PubSubHubbub protocol, but a few other older ones like XMPP and its venerable PubSub, as well as a few other techniques.
[128.80 --> 128.88]  Thanks.
[129.92 --> 134.46]  So, as some background, what makes this technology important nowadays?
[136.24 --> 137.68]  So, there's different approaches.
[138.28 --> 140.62]  The very technical approach is it saves bandwidth.
[141.40 --> 149.10]  The current way of building services is just when you want to interact with another service is to build something that pulls these other services.
[149.26 --> 153.42]  So, basically, every two seconds, you're going to go check the API, check the RSS feed, check the content.
[153.42 --> 164.02]  It works fine when you have a few endpoints, but when you start having, like, thousands, tens of thousands, hundreds, millions of thousands, it's just a mess.
[164.30 --> 172.40]  And you're wasting a lot of bandwidth on your own, a lot of CPU time, as well as wasting the bandwidth of the third-party service that you're actually querying.
[173.38 --> 177.06]  It's really like the kid in the backseat who always asks, are we there yet?
[177.12 --> 177.72]  Are we there yet?
[177.78 --> 178.38]  Are we there yet?
[178.42 --> 179.02]  Every two seconds.
[179.02 --> 187.66]  It's very annoying, and it can be fixed by having an approach where you can say, hey, all right, listen, kiddo, I'm going to tell you when we get there, so do not ask anymore.
[188.24 --> 191.72]  And that's really what Pops Up Up and the real-time web is aiming at doing.
[192.30 --> 195.74]  There's also another way of seeing things.
[196.12 --> 200.06]  So, the first wave of the web was really a read web.
[200.14 --> 203.22]  So, you would go on the web, and you would read stuff, learn stuff.
[203.22 --> 208.42]  So, in a way, most of the first websites, the media sites, were actually just this.
[208.42 --> 217.24]  Then we had the blogs, the first kind of sharing websites, like Flickr, stuff like this, which would be right.
[217.66 --> 223.74]  And now we're entering a third phase where you're not doing read and write, but you're also subscribing to content.
[224.16 --> 227.58]  Saying, hey, all right, on Twitter, I am following people, which is like subscribing to people.
[227.68 --> 231.32]  On Facebook, I'm subscribing to my friend's stream.
[231.32 --> 239.46]  And you could really go much beyond this in seeing that search engines actually subscribe to sites to index their content and stuff like this.
[239.56 --> 241.48]  So, there's different ways of seeing the thing.
[242.08 --> 245.60]  So, you mentioned a couple of protocols, PubSubHubbub and XMPP.
[246.22 --> 248.50]  What's the payload look like for this type of messaging?
[249.60 --> 254.50]  So, in both cases, they – I mean, so XMPP is actually based on XML.
[254.50 --> 257.98]  So, it's mostly XML, even everything XML.
[258.62 --> 263.78]  Right now, PubSubHubbub is also aiming only at fixing the issue of Atom and RSS feeds.
[264.56 --> 274.00]  We're working with the team there at making – at supporting other types of data like JSON, like other types.
[274.70 --> 276.22]  It's not in the spec yet.
[276.32 --> 279.74]  I hope it's going to come very soon because a lot of our users actually ask for it.
[279.74 --> 286.72]  So, I guess one of the real-world scenarios is you've got a feed that you want to check and you want to be notified when that feed updates.
[287.08 --> 290.64]  So, how does that – how does the protocol work?
[291.34 --> 294.08]  So, the first thing when you say you is to define who is you.
[294.46 --> 297.88]  In the case of PubSubHubbub or XMPP, it's not an end user.
[298.08 --> 299.48]  It's really like another service.
[299.98 --> 307.56]  So, the most common use case is like, hey, Google Reader needs to know when a feed is updated because it wants to show this to its users.
[307.56 --> 322.38]  And the way to do this is to use this PubSubHubbub protocol if the feed – or actually the feed's publisher use it – is to use a third party called the Hub and tell them, hey, Hub, please tell me whenever the content is updated.
[323.06 --> 330.18]  And the Hub's job is basically going to listen to the publisher so that the publisher tells them, hey, the content has been updated.
[330.40 --> 336.42]  And then fan out the update to all the subscribers, to all the Google readers out there who said, hey, I want this content.
[336.42 --> 340.00]  Is there any notion of discovery around finding hubs for content?
[340.84 --> 341.06]  Yes.
[341.30 --> 352.02]  So, the way the protocol works right now is basically the publisher who publishes the feed defines which hub will get its content in real time.
[352.38 --> 360.66]  So, in the RSS feed itself, you will have a link attribute or – well, it's an item link attribute.
[360.66 --> 365.68]  Sorry, node with the rel equal hub attributes.
[366.28 --> 369.46]  And then the href of this link is actually the URL of the hub.
[369.58 --> 381.06]  So, the discovery is really done inside the feed themselves, which is good because it means that basically having a PubSubHubbub feed is not different of having a regular RSS item feed,
[381.06 --> 390.36]  which means that you can really build on top of these and you're not breaking past software and application that we're not using PubSubHubbub.
[390.52 --> 399.00]  So, from the publisher side, they just have to annotate their feed with the special link that, I guess, publishes where the hub is.
[399.08 --> 401.34]  And then what is involved in setting up the hub?
[401.34 --> 407.12]  So, and then the publisher – it's the first thing of – the first job of the publisher is to set up this discovery.
[407.58 --> 410.92]  And it's also to ping the hub saying, hey, all right, this content has been updated.
[411.10 --> 411.98]  This content has been updated.
[412.44 --> 417.70]  The hub then, which is this third party in charge of finding out the subscription, will get these pings.
[418.10 --> 421.20]  If somebody subscribes to the content, it will go fetch the feed.
[421.80 --> 427.40]  So, it's – the notification from the publisher to the hub is actually light.
[427.50 --> 429.66]  It means like it just tells them there is something.
[429.66 --> 435.66]  And then the hub can decide to go pull or not the feed based on the fact that there is subscription.
[436.52 --> 444.46]  It will then diff the content to know what's new versus what's old and then publish in a fat way.
[444.60 --> 447.54]  So, it's actually sending the content to all the subscribers.
[448.16 --> 449.62]  So, does the publisher have to be involved?
[449.72 --> 454.56]  Is there any such thing as a third party hub where – let's say I wanted GitHub's public timeline in XML.
[455.24 --> 456.38]  Do they have to be involved?
[457.26 --> 457.64]  Yes.
[457.64 --> 466.22]  You would need GitHub to actually designate their own hub and say, hey, all right, this is where you can get our content in real time.
[466.92 --> 471.50]  The way it works right now, Google – so, a lot of feeds are actually already PubSubHubHub.
[471.60 --> 474.22]  So, you might already be using this protocol without really knowing it.
[475.32 --> 477.90]  There's three big hubs out there.
[477.90 --> 481.30]  The biggest one, which is the first historical one, is the Google Hub.
[481.88 --> 484.70]  It was built by two engineers at Google.
[485.24 --> 490.56]  And the goal was to make all the Google-owned feeds real time.
[490.70 --> 498.42]  So, it involves like FeedBurner feeds, Google Reader shared feeds, Google Buzz feeds, Blogger feeds, a lot of feeds like this.
[498.42 --> 500.52]  And it's actually also an open hub.
[500.62 --> 504.40]  So, you can – if you have your own service, you can also designate them as the hub.
[504.90 --> 507.86]  There is a second hub, which is basically the WordPress.com hub.
[508.86 --> 511.50]  So, WordPress.com implemented their own hub.
[511.94 --> 514.74]  So, it's both a publisher and a hub in this case.
[515.30 --> 517.66]  And you cannot use it from the outside world.
[517.72 --> 520.88]  So, if you've got your own little WordPress.org blog, you cannot really use it.
[521.40 --> 526.92]  And then the third solution is the solution provided by Superfeeder, which is basically, hey, like the Google Hub.
[526.98 --> 528.68]  So, it's a hub that is public to anyone.
[528.76 --> 529.60]  We can designate it.
[529.60 --> 533.52]  And that's actually branded to your publisher site.
[533.96 --> 542.18]  So, we host the hubs for people like Tumblr, Passers, Gowalla, Sixerport, tons of others like BuzzFeed.
[542.38 --> 545.92]  And working on like very interesting use cases with like e-commerce websites and stuff like this.
[546.12 --> 558.78]  So, one of the more interesting demos that I saw was a Gowalla feed powered by Superfeeder that was hooked up to a WebSockets app in the browser where it showed all of the check-ins in real time in Google Chrome.
[558.78 --> 563.50]  What do technologies like this mean for kind of new era in web design?
[564.42 --> 564.60]  Sure.
[564.82 --> 568.46]  So, what you must not forget is like PubSubHub is a server-to-server protocol.
[568.64 --> 577.02]  So, it's really like, hey, from the blogger server to a hub and then to Google Reader.
[577.26 --> 580.94]  So, the end user doesn't really see it, which means that it doesn't come to the browser.
[581.16 --> 586.64]  But then when you have something that comes to the server, you can really easily build something that achieves the last mile.
[586.64 --> 597.54]  And we call the last mile the thing which comes from like a browser – sorry, a server to a browser, a server to an iPhone, a server to an iPad, a server to – you name it, basically.
[597.66 --> 600.34]  Any type of devices that is connected to the web.
[601.02 --> 603.88]  So, what we built for Gowalla is a very, very simple example.
[604.08 --> 608.92]  It's like since we get all the notification for all their feeds, we have some kind of a fire hose, right?
[608.92 --> 616.20]  So, Superfeeder has this thing called Track, which enables you to filter feeds on different criteria.
[617.08 --> 619.82]  So, filter notification, sorry, on different criteria.
[620.26 --> 630.32]  So, instead of saying, hey, I want the Gowalla feed of Wins updates, you can say, I want any Gowalla update within two miles of Austin.
[631.28 --> 634.52]  And you would get that pushed to you as if it was a real feed on the site.
[634.52 --> 641.66]  And we also obviously have some kind of a fire hose so you can say, hey, I want any Gowalla update and get them.
[642.02 --> 652.68]  What we built after this is basically this little node server that does WebSockets and that turns Publish Hub Hub notification into WebSocket notifications.
[653.28 --> 661.62]  So, when you connect the browser, you can just get an update, subscribe to any feed, and then whenever they arrive, you can show that on your browser the way you want.
[661.96 --> 662.70]  Very interesting.
[662.70 --> 667.36]  So, how similar is that set up to what Twitter is doing with a lot of their real-time streams?
[668.46 --> 673.74]  So, Twitter is basically doing all this in a single proprietary stack.
[674.20 --> 681.40]  So, basically, you can subscribe to, I think, the streaming API with your own libraries.
[681.70 --> 682.60]  It doesn't use WebSocket.
[682.80 --> 685.36]  It doesn't use anything that is part of the open web.
[685.98 --> 689.92]  Maybe just auth is actually the only open thing out of Twitter, I would say.
[689.92 --> 701.80]  And it's sad because if you want to build something that is a little bit more than just using their own streaming API, I don't know, building some kind of server-to-server process, you cannot.
[702.36 --> 706.34]  It's really hard to build something that subscribes to thousands of users on Twitter.
[706.82 --> 713.58]  They make it hard on purpose because they obviously don't want to make this kind of data available because they're selling it.
[713.58 --> 719.94]  So, I think it's like similar technologies in terms of what you can do with it.
[720.30 --> 723.06]  But on one end, you've got some kind of private proprietary stack.
[723.24 --> 734.00]  And on the other end, you've got some very open stack, which is like an open protocol defined by a community of people from a lot of different companies, whether it's Microsoft, Google, even Facebook is part of it now and people like this.
[734.00 --> 738.56]  So, what are the pros and cons between PubSubHubbub and XMPP?
[739.32 --> 742.12]  So, they solve two different types of issues.
[742.68 --> 745.22]  And actually, PubSubHubbub came much later.
[745.48 --> 748.60]  I mean, XMPP is, I think, like 11 or 12 years old now.
[748.98 --> 752.78]  And PubSubHubbub is barely a year and a half.
[752.78 --> 761.22]  So, the idea when they built PubSubHubbub was like, hey, all right, we got this awesome PubSub patterns on the web like XMPP.
[761.94 --> 767.54]  One of the early designers of the protocol, Brad Fitzpatrick, actually built his own XMPP server.
[767.66 --> 770.76]  So, he was really convinced of like the interest of having this.
[771.28 --> 776.60]  At the same time, he also found out that basically XMPP is just too different from your regular web technologies.
[776.60 --> 780.80]  It's too different from the web stack, which meant that a lot of people were really scared about it.
[780.80 --> 784.76]  And I had a lot of issues scaling services with this because they didn't know how it works.
[784.86 --> 788.56]  Or even if they did, it was just too different from PubSubHubb, from HTTP.
[789.20 --> 798.72]  So, they built basically the whole PubSub pattern on top of HTTP because even though you could do it with XMPP, people wouldn't because it was just too complex.
[799.26 --> 800.10]  What about reliability?
[800.42 --> 803.68]  If I'm not there to catch a feed when it updates, do I hear it?
[804.16 --> 808.56]  So, it really is up to the hub that you would use.
[808.56 --> 825.92]  So, actually, none of the public hubs at the moment, whether it's the Superfeeder, the PubSubHub, the Google App Engine Hub, or the WordPress Hub, has some kind of, how can I say, like storage of the entry and then are able to actually resend you the data when you're back.
[826.28 --> 828.24]  Because we deal with massive amounts of data.
[828.62 --> 832.02]  Superfeeder currently pushes 30 million Atom updates per day.
[832.02 --> 838.96]  So, if you're off for, like, just an hour, we might already store 1 million Atom entries just for you.
[839.68 --> 842.32]  So, it's not really easy to scale this.
[842.36 --> 850.74]  But we're working on, like, storing the data so that whenever you come back, when your endpoint is available again, we'll push that to you in a way that hopefully won't take you down again.
[851.16 --> 853.90]  So, this is primarily a real-time update feature.
[853.90 --> 860.32]  But if you've got to catch everything that comes from a feed, it's just a single tool, I guess, in the stack instead of it being your primary?
[861.24 --> 862.34]  I'm not sure I understand the question.
[862.88 --> 870.48]  So, if you absolutely have to have all the data coming out of a separate service, I guess you could always just pull that feed independently, right?
[870.92 --> 871.68]  Yes, of course.
[871.80 --> 874.46]  You can still pull the feed from time to time, make sure.
[874.46 --> 882.08]  But, I mean, if you really, really need to get the data all the time, I would suggest making sure that your service is not going to be offline anyway.
[883.18 --> 885.52]  I mean, obviously, you can be offline for two seconds.
[885.84 --> 888.62]  And then it's a big deal, I mean, because you might miss something.
[888.72 --> 889.72]  So, you might want to pull.
[889.82 --> 893.10]  But as long as you're offline at any time, you will miss some data.
[893.86 --> 897.60]  We deal with feeds sometimes that are very high-frequency updates.
[897.90 --> 902.56]  So, it means that some feeds might have, like, an entry every minute, and they just have 10 entries.
[902.56 --> 906.52]  So, it means that after 10 minutes, you might have lost some content, even if you pulled it.
[907.24 --> 907.70]  Make sense?
[907.86 --> 908.06]  Sure.
[908.86 --> 912.96]  So, when people say, hey, what happens if I'm offline?
[913.12 --> 916.10]  It's like, I'm sorry, but there is no perfect solution if you're offline.
[916.74 --> 919.80]  You'd rather make sure that your service is never going to be offline.
[920.14 --> 921.64]  There's a ton of techniques to actually do this.
[921.74 --> 928.76]  I mean, one of them is to just process everything in an asynchronous way so that you put every message in a queue, and then you deal with the queue.
[928.76 --> 935.22]  So, whenever your workers have issues, you can still store the data in the queue, and then process it whenever you're better.
[935.50 --> 939.48]  So, I'm looking at your GitHub repo and see a lot of Ruby out there.
[939.60 --> 941.16]  What sort of languages do you speak?
[942.32 --> 954.02]  So, we built most of Superfeeder on top of XMPP, which means that basically any component in our architecture is a little XMPP worker who sends presence,
[954.02 --> 960.92]  which is one of the three XMPP verbs, I would say, to other workers saying, hey, I'm here.
[961.18 --> 962.18]  Please send me some work.
[962.66 --> 964.56]  So, other workers will send some work.
[964.66 --> 967.14]  So, the whole bus is XMPP.
[967.46 --> 976.08]  Then each of the workers is actually using different languages, different techniques, I would say, based on what they do.
[976.08 --> 985.36]  So, our parsers, for example, are built with some C at the very core of it, and then on top of that, a lot of Ruby to make the rules.
[985.70 --> 991.24]  So, we actually do some – Superfeeder does something that is mapping the different RSS formats.
[991.48 --> 997.98]  So, if you're using RSS – I mean, if you're subscribing to an RSS feed, an Atom feed, and a FeedBurner feed, you might see different items.
[998.22 --> 1003.62]  And rather than you deal with the complexity of these different formats, we just normalize it to Atom.
[1003.62 --> 1007.06]  And these rules are actually written in Ruby in our parsers.
[1007.54 --> 1013.84]  We also use a lot – I mean, I think pretty much only Event Machine because, obviously, we do a lot of networking stuff.
[1014.10 --> 1018.18]  And waiting on sockets would just not make any sense for us.
[1018.62 --> 1021.42]  So, we use Event Machine, which is the reactor pattern.
[1021.54 --> 1023.86]  So, everybody is talking about, like, Node at the moment.
[1024.40 --> 1026.98]  Event Machine is pretty much, like, one of the grandparents of Node.
[1027.28 --> 1032.80]  I would say Python's Twisted is the other grandparent of Node.
[1032.80 --> 1035.34]  Yeah, we covered all three of those on the changelog recently.
[1035.44 --> 1036.28]  And I'm fascinated by it.
[1036.28 --> 1039.08]  It seems like a new pattern for developing web applications.
[1039.34 --> 1045.96]  And I think Node might be benefiting just from the fact that since there was no set of libraries out there when it started,
[1046.12 --> 1048.24]  everything could be built from the ground up to support async.
[1048.48 --> 1055.42]  What sort of problems did you find using Ruby to do that with Event Machine and having libraries that would support it?
[1055.42 --> 1061.34]  So, we still have some issues with Event Machine based on the fact that some implementation are not there yet.
[1062.66 --> 1064.88]  Actually, one of the biggest issues is very interesting.
[1065.04 --> 1073.16]  It's like the DNS resolution inside Event Machine is still synced, which means it's actually blocking the reactor.
[1073.30 --> 1073.90]  So, it's really bad.
[1073.96 --> 1077.98]  So, we actually created our own little resolver in an async way.
[1077.98 --> 1082.64]  And we hope that at some point Event Machine will include some kind of async DNS resolution.
[1083.64 --> 1093.46]  We also find issues where libraries for most of the, I would say, very recent data stores are not either up to date or even present.
[1094.12 --> 1095.74]  I'm thinking about Redis, for example.
[1095.74 --> 1106.02]  We had to basically kind of hack a lot on top of what was the first initial item to make sure that it would still work with newer versions of Redis.
[1106.56 --> 1110.34]  I know that Cassandra doesn't have an Event Machine implementation either.
[1111.62 --> 1113.78]  Mongo has had issues in the past as well.
[1113.78 --> 1125.24]  I mean, like the driver, the asynchronous driver was not really complete in terms of features compared to the regular blocking driver.
[1125.74 --> 1127.46]  You kind of walked into that subject.
[1127.58 --> 1129.02]  So, let's talk about NoSQL for a minute.
[1129.12 --> 1130.94]  What's your favorite platform out there?
[1131.80 --> 1132.10]  Redis.
[1132.40 --> 1134.08]  We absolutely love Redis.
[1134.70 --> 1141.28]  I mean, there's always a big debate about, hey, all right, as long as you store everything in memory, it's easy.
[1141.40 --> 1142.98]  So, basically, Redis is doing something easy.
[1143.60 --> 1147.96]  And what I usually tell people is like, yeah, they do something easy, but they actually made the decision to do this.
[1148.20 --> 1151.06]  And not a lot of data stores actually made that decision.
[1151.58 --> 1153.56]  So, we use Redis as much as we can.
[1153.56 --> 1157.80]  We still have a few missing features from Redis.
[1157.98 --> 1159.98]  The biggest one is obviously the cluster node.
[1160.12 --> 1166.38]  So, I know that Antiris is actually working on this, is the maintainer of Redis.
[1166.96 --> 1168.54]  And it should be live by the end of the year.
[1168.66 --> 1170.66]  But we might actually have to use Mongo.
[1170.84 --> 1177.12]  And we already started evaluating this for specific things where we really need some kind of clustorable approach.
[1177.12 --> 1186.52]  We're adding a server which is double or increase the size of our store rather than do some kind of sharding, which was really becoming and is still a big deal for us right now.
[1186.78 --> 1190.20]  We're trying to get Antiris on the show to talk about Redis.
[1190.34 --> 1192.24]  Hopefully, we'll put that together soon.
[1192.24 --> 1196.78]  But it's amazing how many of these new NoSQL stores support JavaScript out of the box.
[1198.72 --> 1200.86]  Well, I mean, what do you mean?
[1200.98 --> 1204.46]  In terms of they use JSON for the data structures and stuff like this?
[1204.68 --> 1209.40]  JSON for the data structures and then a lot of the APIs with Couch and Mongo are written in JavaScript.
[1209.40 --> 1212.72]  Yeah, well, so Redis is different to that regard.
[1212.84 --> 1216.80]  I think Redis doesn't have any native JavaScript thing.
[1219.08 --> 1225.42]  What I find interesting about Redis as well is they took it from a very, very low-level approach.
[1225.92 --> 1228.16]  Just installing Redis is very simple.
[1228.34 --> 1231.18]  You just have to download the code and just make.
[1231.44 --> 1232.02]  And that's it.
[1232.26 --> 1235.84]  You don't need any third-party libraries or things like this.
[1235.84 --> 1241.84]  So the approach that they had as well was like, hey, all right, we're going to build this very high-performance thing.
[1242.30 --> 1244.02]  So we need to control all the chain.
[1244.18 --> 1252.78]  So we really need to make sure that we're not reusing any complex libraries that would make Redis much slower or much bigger or much harder to maintain.
[1254.00 --> 1257.90]  It looks like the web development landscape has changed quite a bit in the last few years.
[1257.90 --> 1261.86]  It used to just be you would have a front-end architecture, a back-end architecture.
[1261.86 --> 1266.54]  But now it seems like you have to have a NoSQL solution for a lot of these things and a queuing solution.
[1266.72 --> 1270.78]  What of these queue systems have you played with, I guess, like Rescue on top of Redis and some others?
[1271.42 --> 1273.04]  So we use RabbitMQ.
[1273.42 --> 1274.86]  I haven't really played with Rescue.
[1275.76 --> 1277.00]  I'm not sure how you pronounce it.
[1278.28 --> 1280.02]  We should definitely give it a look.
[1280.46 --> 1283.98]  We use RabbitMQ, and we do not use a lot of queue systems.
[1283.98 --> 1293.48]  I mean, XMPP actually has a lot of features that could be implemented via a queue system.
[1293.58 --> 1295.70]  So we don't really use that a lot.
[1296.44 --> 1297.00]  It's funny.
[1297.10 --> 1301.32]  You mentioned the pronunciation of Rescue there with, I guess, your French.
[1301.48 --> 1303.46]  So Resc would be the French pronunciation.
[1303.68 --> 1310.16]  But that's an important part of creating an open-source project is coming up with a name that kind of brands the thing.
[1310.28 --> 1311.98]  So Superfeeder, where did that come from?
[1311.98 --> 1316.56]  Basically, it's like let's make feeds better.
[1317.04 --> 1320.44]  So it's kind of like if they're better, they're like super, right?
[1320.48 --> 1321.48]  So they're like super feeds.
[1321.96 --> 1327.36]  And the machine that makes these feeds super is actually a super feeder in a way.
[1327.90 --> 1329.56]  So that's the way we built it.
[1329.92 --> 1334.76]  It's fun because it was actually initially an internal component to another much bigger application.
[1334.76 --> 1343.26]  And when we started implementing this component, which was supposed to be a smaller or just a small bit of the whole system,
[1343.42 --> 1348.14]  we found out that it was actually kind of an endless, I mean, hole.
[1348.32 --> 1353.20]  Like we would dig something and find something else and dig further and dig further and dig further and dig further and dig further.
[1353.20 --> 1358.64]  So much that at some point say, hey, all right, why don't we just do this and make sure that we do it fine?
[1358.76 --> 1362.62]  And then maybe in like 10 years or 15 years, we'll find something to build on top of.
[1362.62 --> 1366.98]  So let's talk about super feeder for a moment in your monetization strategy.
[1367.12 --> 1369.36]  So do you charge publishers or subscribers or both?
[1371.84 --> 1372.88]  Neither and both.
[1373.32 --> 1376.84]  So the PubSubHubbub pattern is really an open web pattern.
[1376.96 --> 1378.44]  So you should not charge anyone.
[1378.52 --> 1379.22]  And we do not charge.
[1379.30 --> 1383.28]  So we make the content from Tumblr real time and you can get that in real time for free.
[1383.80 --> 1385.62]  And that's implementing the PubSubHubbub protocol.
[1385.78 --> 1389.30]  So in a way, you don't even need to know that it's actually using super feeder.
[1389.30 --> 1393.02]  However, there's still a massive proportion of feeds out there.
[1393.18 --> 1397.98]  I would say like something like 70 or 80% of them were not PubSubHubbub enabled.
[1399.00 --> 1406.74]  And for this, you would need some kind of third-party application to do the polling for you if you don't want to do the polling and push it to you as if they were PubSubHubbub.
[1407.26 --> 1408.58]  So I'm not sure that makes any sense.
[1408.70 --> 1411.60]  But the idea is like, hey, all right, you got 100 feeds.
[1411.82 --> 1414.18]  Out of those, 20 of them are actually PubSubHubbub.
[1414.30 --> 1417.74]  So you can subscribe to the designated hub and get the content pushed to you, right?
[1417.74 --> 1419.94]  Then you have the 80 more feeds.
[1420.24 --> 1421.14]  So how do you deal with them?
[1422.00 --> 1426.06]  Some people, and that's actually what they've been doing for years, build some kind of pollers.
[1426.30 --> 1429.16]  So like, all right, fine, we're going to build something that polls the feed.
[1429.34 --> 1435.54]  And whenever there's a new protocol, a new way of getting the content or whenever there's a new flavor of RSS or item,
[1435.62 --> 1442.50]  we just implement the extra layer to make sure that our 80 remaining feeds are being dealt with correctly.
[1442.50 --> 1453.26]  The other approach, and that's what we're trying to convince people, is like, all right, you've seen how easy it is to deal with PubSubHubbub feeds with these 20 feeds that you're dealing with.
[1453.92 --> 1460.18]  Why not having some kind of third-party push that to you as if they were all PubSubHubbub?
[1460.18 --> 1463.16]  So that's basically what Superfeater does.
[1463.26 --> 1468.88]  So we just implement this polling or all these techniques to avoid polling.
[1469.56 --> 1471.92]  We implement the date anomalization on top of it.
[1472.02 --> 1474.96]  And then we push it to you as if it was PubSubHubbub.
[1475.70 --> 1477.74]  Obviously, there is some kind of cost involved with this.
[1477.90 --> 1481.18]  So we are actually going to charge for the content that you push to you.
[1481.22 --> 1482.22]  But it's really cheap.
[1482.22 --> 1490.06]  Like, you can get a couple million notifications for less than $100 a month.
[1490.68 --> 1493.38]  So one of your repos out on GitHub is popular feeds.
[1493.56 --> 1497.14]  And it's a text file with over 4,200 feeds in this thing.
[1497.34 --> 1501.04]  Does this power any sort of process at Superfeater or is this just out there for informational purposes?
[1501.84 --> 1504.42]  No, it's only for informational purposes.
[1504.62 --> 1510.64]  So we actually had a lot of our users say, hey, all right, we want kind of a firehose of the blogosphere.
[1510.64 --> 1516.86]  Like, we want the top 50, the top 100, the top 10,000, the top 100,000 feeds pushed to us.
[1517.46 --> 1521.18]  And it was really hard to tell them, like, here is the top 1,000 feeds.
[1521.24 --> 1522.54]  We have no idea because it's not our job.
[1522.60 --> 1523.80]  Our job is to distribute the content.
[1524.24 --> 1531.64]  So actually, last weekend, we worked on kind of identifying a list of popular feeds based on, like, TechMeme on –
[1531.64 --> 1536.64]  I'm sorry – a few other services out there where actually list feeds and OPML files.
[1536.64 --> 1543.00]  So we had a lot of other services, like, all top, and a few other services to identify which one were popular.
[1543.60 --> 1548.62]  Then we kind of, like, I'm going to say, mashed that up with the Superfeater data.
[1548.90 --> 1555.02]  Because since we have a lot of feeds, we nearly have 3 million now, we know which one actually subscribed by more than one user, right?
[1555.02 --> 1561.68]  So we kind of mashed all the data together to identify kind of a short list of what we think is the most popular feeds out there.
[1562.98 --> 1564.32]  Wow, 3 million feeds.
[1564.40 --> 1566.28]  Yeah, I just noticed the counter on the homepage.
[1566.74 --> 1568.10]  3.1 million feeds out there.
[1568.52 --> 1569.86]  Those are entries, I guess.
[1570.44 --> 1572.84]  So these are entries, and that's billion.
[1573.08 --> 1573.92]  Yes, I just noticed billion.
[1574.06 --> 1574.28]  Wow.
[1574.72 --> 1577.32]  We currently push, like, about 30 million a day.
[1578.60 --> 1579.08]  Unbelievable.
[1579.08 --> 1580.94]  Yeah, it's a lot of data.
[1581.24 --> 1588.62]  And the interesting thing about Superfeater is, like, most of services actually deal with scalability in terms of, hey, how can I reply to as many requests per second?
[1589.12 --> 1593.86]  And we actually do the exact ways, like, how can we push as much content per second as we can?
[1594.38 --> 1597.98]  How can we push more data rather than how can we deal with incoming requests?
[1598.52 --> 1598.80]  Gotcha.
[1598.80 --> 1605.40]  Well, this is the part of the show where we kind of turn it around and ask our guests what's on your open source radar.
[1605.58 --> 1609.76]  What out there in open source land has you excited that you just want to play with?
[1610.90 --> 1618.98]  So definitely Redis is one of my loved, how can you say, I mean, most loved project right now.
[1619.10 --> 1620.80]  I mean, I'm trying to build some stuff with them.
[1621.14 --> 1622.52]  They have a PubSub store.
[1622.52 --> 1627.28]  So it means that basically you can build with Redis a way to subscribe to items.
[1627.28 --> 1629.44]  And whenever something is published there, you get notification.
[1630.36 --> 1634.78]  Node.js is also something that I've been playing with a lot in the past few weeks.
[1635.98 --> 1638.66]  And this is really because we're moving hosts right now.
[1638.92 --> 1640.06]  I love Chef as well.
[1640.78 --> 1651.08]  It's something that not everybody might know, but it's a solution that helps you deploy and manage the configuration of your servers.
[1651.08 --> 1653.80]  So when you have one or two, it's not that big of a deal.
[1653.88 --> 1662.54]  But when you start having 10, 30, 50, or 80 superfeeder, it's really starting to become a mess to deal with the different configurations,
[1663.10 --> 1669.34]  the different versions, the different roles of each of the different servers that you might use, and stuff like this.
[1669.34 --> 1675.50]  And I would definitely recommend anyone with more than maybe three servers look into Chef because it's really great.
[1676.88 --> 1677.16]  Yep.
[1677.32 --> 1680.92]  Pretty much these three are our current love projects.
[1681.06 --> 1681.96]  Chef from OpsCode.
[1682.02 --> 1683.40]  It is an awesome piece of software.
[1683.64 --> 1686.18]  We should do a DevOps show on the changelog pretty soon.
[1686.96 --> 1687.64]  I think it would be interesting.
[1687.76 --> 1687.88]  Yeah.
[1689.04 --> 1693.86]  And it's one of the things where basically I had really no knowledge before sending Superfeeder in it.
[1693.86 --> 1704.24]  And it felt like, oh, my, how am I going to – I mean, I'm going to spend like two-thirds of my days dealing with patches or configuration that I need to update or anything like this.
[1704.44 --> 1713.04]  And having Chef has been like, all right, I can just put the receipts, which is really like the way it works, like put the receipts of what a server is, and it just builds it.
[1713.04 --> 1717.32]  And whenever I need to update, I just change one thing there, and it builds and updates all the servers.
[1717.98 --> 1721.26]  It's saving like months of work.
[1721.26 --> 1730.52]  You know, and also moving to the cloud has just made this type of skill set that more valuable because you need reproducible processes that you can set these servers up.
[1730.68 --> 1730.92]  Definitely.
[1731.52 --> 1732.90]  Well, there's still a few differences.
[1733.12 --> 1736.86]  Like, I mean, we are moving right now from a host to a different – to another host.
[1737.02 --> 1739.20]  So, I mean, moving from Slicehost to Linode.
[1739.86 --> 1742.46]  And it's – we still have like some issues.
[1742.54 --> 1746.34]  We actually had to update a few of our Chef receipts, maybe because we did it wrong the first time.
[1746.34 --> 1755.74]  But, I mean, hopefully and ideally at some point, we will be able to have like this very, very generic way of describing the servers and describing like the IPs and stuff like this.
[1755.74 --> 1762.00]  So that whenever you just plug a new IP and a root password and it just deploys whatever on any cloud service and you can actually do benchmarks.
[1762.70 --> 1776.72]  And that's one of the things that I want to really work on in the coming weeks as well is like do some kind of like Chef receipts to deploy a very basic script in an identical way over different providers, whether it's Rackspace, Slicehost, Linode, EC2.
[1776.96 --> 1778.12]  I mean, you name it.
[1778.12 --> 1784.72]  And then just get all the results back and make sure that we always use the most performance machine per dollar spent.
[1785.46 --> 1786.18]  Very interesting.
[1786.32 --> 1787.48]  Well, thanks for joining us today, Julian.
[1787.56 --> 1788.66]  We certainly appreciate it.
[1789.02 --> 1789.66]  Thanks for having me.
[1789.70 --> 1790.08]  It was great.
[1790.08 --> 1790.16]  Thank you.
[1808.12 --> 1809.12]  Thank you.
[1809.12 --> 1810.12]  Thank you.
[1810.12 --> 1811.12]  Thank you.
[1811.12 --> 1812.12]  Thank you.
