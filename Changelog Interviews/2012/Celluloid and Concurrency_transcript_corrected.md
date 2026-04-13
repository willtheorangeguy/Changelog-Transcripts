[0.00 → 4.14] This episode of The Change Log is brought to you by Pusher.com.
[4.62 → 10.76] Pusher is a hosted API for quickly adding scalable real-time functionality to web and mobile apps.
[11.00 → 16.86] If you're building anything that needs to get data from the server back to the client asynchronously,
[17.14 → 18.92] you need to check out Pusher.
[19.38 → 21.62] They've got a number of tutorials to help you get started,
[21.86 → 25.28] everything from a quick start guide to building a real-time chat client,
[25.56 → 28.56] push notifications, activity streams, and more.
[28.56 → 34.84] Use our coupon code CHANGELOG to save 15% off your first month.
[35.06 → 38.88] Join the real-time web today and get your free API account.
[39.34 → 40.76] Head to Pusher.com.
[40.76 → 41.28] Pusher.com.
[53.98 → 54.54] Pusher.com.
[54.54 → 84.52] Don't push me away!
[84.54 → 114.52] Don't push me away!
[114.56 → 144.52] Don't push me away!
[144.52 → 147.10] Tony, for those that don't know, you want to introduce yourself.
[148.04 → 153.64] Hi there, I'm Tony Farceur. I've been doing Ruby about seven years now, I guess.
[154.70 → 158.38] Kind of jumped in with the Rails bandwagon there in 2005.
[158.38 → 161.96] I got on board with Rails 0.11.
[162.90 → 169.28] This was back when everybody was deploying with fast CGI and City was the cool hotness of the day.
[169.98 → 171.80] So I guess I've been around a while.
[171.80 → 177.28] So why celluloid? Why don't you give us a little background behind this project?
[178.14 → 181.42] So I used to do a lot of network programming in C.
[182.28 → 186.34] And when you do stuff in C, right, you have to build your own abstractions.
[187.32 → 192.00] So I had kind of an idea of what I wanted to do or always wanted to do in C.
[192.14 → 193.40] And then I discovered Erlang.
[194.36 → 200.80] And Erlang had sort of taken all the stuff I had wanted to do and had a really nice face on it.
[200.80 → 210.12] And Erlang was kind of how I discovered things like the actor model and basically seeing approaches to concurrency that also worked for distribution.
[211.40 → 212.76] When did you start the project?
[213.72 → 217.20] I started it around this time last year.
[217.34 → 218.96] It's a little bit over a year old now.
[220.30 → 226.64] I was like lying in bed one night, kind of, you know, around like 3 a.m. or something, trying to go to sleep.
[226.64 → 235.20] Just kind of thinking about, so I was working on a programming language array, which was like trying to bring Ruby to the Erlang VM.
[235.94 → 242.28] I was thinking, you know, do I really need to make a new programming language, or can I just take all the Erlang ideas back over to Ruby?
[242.58 → 244.64] Which is something I had tried before.
[244.90 → 251.64] I had tried a reactor, which was, yeah, another project trying to bring sort of Erlang ideas to Ruby.
[252.64 → 254.90] And I abandoned that, switched to Rhea.
[254.90 → 260.44] And I was like, again, like, you know, maybe I can bring all this stuff to Ruby.
[260.60 → 264.04] We don't need a new language and everybody can just write this stuff in Ruby.
[264.30 → 265.66] Let's dive in there for a moment.
[265.76 → 267.30] What are some of these Erlang ideas?
[268.16 → 275.62] So the big problem, I think, is Subsists don't like concurrency, and we really need it in the modern world, right?
[275.66 → 278.48] We have computers with multicore processors.
[278.48 → 285.38] You know, we have Rails applications that sit around and do nothing while they're talking to the database.
[286.32 → 289.24] So, I mean, all these things can be solved with threads.
[289.86 → 294.28] And Subsists just don't want to use them and I would really like to change that.
[294.28 → 304.24] What are some of the libraries that you can or can't use if you're using celluloid sort of adapter support do you need to really take advantage and exploit this?
[305.38 → 309.94] So celluloid will work with any thread-safe Ruby gems you want to use.
[310.02 → 315.98] So if you want to use Rails, you want to use Sinatra, you can actually drop celluloid in the background.
[315.98 → 323.42] Right now there's unfortunately no celluloid Rails plug-in type of thing to kind of give you a happy path for that.
[324.20 → 328.42] But if you're using Rails in thread-safe mode, you can just go ahead and drop in celluloid.
[329.58 → 332.72] Let's talk about some of these, I guess, subprojects of celluloid.
[332.96 → 335.44] There's the I.O. project, there's D-Cell and Reel.
[335.56 → 336.84] What are these three?
[338.16 → 342.62] So the first one you mentioned was celluloid I.O., right?
[343.14 → 343.40] Mm-hmm.
[343.40 → 350.02] Okay, so celluloid I.O. lets you do vented I.O. inside an actor.
[350.38 → 355.74] So it's basically a combination of the actor model and the reactor pattern.
[357.18 → 366.22] So basically each of these objects is kind of, each of the concurrent objects slash actors is kind of like an event loop in and of itself, right?
[366.22 → 374.26] So the actor model works by having actors, you send them messages, and then they can send you messages back.
[375.00 → 382.60] So when you're waiting for messages with celluloid I.O., you can also wait for other I.O. handles in the system.
[382.60 → 393.26] So you can have one actor that's potentially waiting for, you know, 10,000 possibly other sockets or something, right?
[393.26 → 400.46] So it's similar to, like, event machine or Node.js, but you can have as many of those actors as you want in the system.
[400.88 → 405.42] You can kind of isolate what connections they deal with.
[405.46 → 409.48] So you don't have one event loop dealing with all your clients.
[409.48 → 414.64] And then in the same event loop, you're, like, trying to make outgoing connections to other services.
[415.84 → 422.48] If you've ever had to debug somewhere where one of these event loops is getting stuck, it's really nasty.
[423.02 → 431.76] So celluloid I.O. specifically lets you isolate which actors are handling what, so that's easier to debug.
[431.76 → 439.32] So the canonical example of these types of projects are usually chat servers, but let's get a little bit more specific.
[439.48 → 446.10] Without divulging anything that you can't share, what types of apps at Living Social are you building with this sort of project?
[447.06 → 451.46] So we're not actually using celluloid I.O. at Living Social.
[451.80 → 459.38] We're presently investigating DSO, and that's – we're building an internal platform as a service.
[459.38 → 464.18] So it's some of the monitoring and automation around that.
[464.34 → 469.26] We're investigating using DSO, but, you know, it's still in the preliminary stages.
[469.86 → 470.12] Gotcha.
[470.40 → 477.42] So Adam Eyes on the commit list here on celluloid I.O. just assumed that it was a Living Social joint.
[477.46 → 478.02] Yeah, yeah.
[479.12 → 480.80] No, I mean, he's just a fan.
[483.42 → 485.68] So what about DSO?
[485.68 → 500.34] So DSO, one of the neat things about the actor model is it's really easy to extend from building concurrent systems inside a single VM to distributed systems that run on multiple computers.
[501.34 → 508.88] And that's because the actor model provides you this really high-level abstraction with, you know, this sort of vague terms.
[508.88 → 514.12] So, I mean, the basic idea is an actor has a mailbox, and that mailbox has an address.
[514.52 → 517.44] So it doesn't really matter where that actor lives.
[517.48 → 518.60] It can be in the same VM.
[518.80 → 520.38] It can be on the other side of the world.
[521.22 → 523.86] As long as you have its address, you can send it a message.
[524.36 → 532.38] So DSO lets you build systems with celluloid that span multiple computers.
[532.38 → 535.46] How drastically does that change your architecture?
[536.68 → 539.14] So the idea is it shouldn't.
[539.98 → 547.78] Basically, you can prototype everything inside a single VM, and then when you actually want to pull it apart and distribute it into separate services,
[548.66 → 553.08] it's just as easy as starting services in different VMs instead of all in the same VM.
[553.08 → 556.92] So a couple of times here in the docs you mentioned zero MQ.
[557.60 → 557.86] Yeah.
[557.86 → 561.16] And we talked about that when Zed Shaw was on the show.
[561.70 → 566.94] What's the selling point for zero MQ other than, I suppose, speed?
[568.32 → 569.88] Well, it isn't actually speed.
[570.78 → 573.42] So, I mean, zero MQ is very fast.
[574.38 → 581.30] It's built, diesel and celluloid ZMQ are built on this library called FIRM,
[581.30 → 587.18] made by Chuck Reams, and he's done a perfect job of optimizing that as much as possible
[587.18 → 589.22] and getting the latency as low as possible.
[589.48 → 591.80] But really, it's not about speed.
[591.94 → 597.74] It's about having a higher level message transport than TCP itself.
[598.70 → 603.92] So zero MQ is some really neat features as far as if your network gets partitioned
[603.92 → 607.32] and you try to send a message to another node, right?
[607.32 → 611.84] With TCP, that can potentially time out or give you an error.
[612.86 → 617.04] And zero MQ will hold on to those messages in memory and queue them up.
[617.80 → 622.68] And then as soon as that connection becomes available again, it can send them all off.
[623.36 → 629.18] So it sort of gives you some basic features of message queues, but without a broker.
[630.32 → 633.04] How long has zero MQ been around?
[633.04 → 633.78] How long has the world done?
[633.78 → 634.38] How long has the world done?
[634.38 → 638.20] I've known about it for like three years, I think, maybe even more.
[640.02 → 642.76] It's not like terribly new at this point.
[642.86 → 647.76] It's actually fairly mature and, you know, a lot of people are using it now.
[648.20 → 654.34] There are projects like Storm, which is sort of this distributed function processing system
[654.34 → 655.24] built in Clojure.
[655.46 → 659.14] And people are doing really neat stuff with it now, so I'm a fan.
[659.14 → 666.40] Are projects like Celluloid and Decal, this invented model and this distributed model,
[666.54 → 674.76] is this the frontier of Ruby and frontier of some other languages, or is this just somewhere where you like to play?
[675.86 → 684.50] Well, I mean, so there's Erlang, which has been doing this thing for like almost 20 years now, or more than that, I guess.
[684.50 → 689.50] But so, I mean, Erlang was really ahead of its time as far as this stuff goes.
[690.14 → 694.12] I would definitely say this is the frontier for concurrency in Ruby.
[694.42 → 697.36] There's really no other game in town as far as I know.
[697.60 → 702.96] So instead of pulling these features into Ruby, how come we're not seeing frameworks, I guess, built on top of Erlang?
[703.10 → 704.64] What's the barrier there?
[705.52 → 707.94] So that's been tried quite a bit, actually.
[707.94 → 713.76] There were a bunch of projects to do that, probably most notably Vertebra from Engine Yard.
[714.50 → 719.40] Tried to do this, and it just ended up being overcomplicated.
[720.50 → 732.90] Ezra had a simpler project with RabbitMQ called Nanite, which is sort of, you can sort of look at that as being a little bit similar to Decal.
[732.90 → 738.62] But Decal is a lot more full-featured, I would say.
[739.62 → 748.30] Nanite gave you one agent, and Decal gives you as many as you want that are as easy to implement as just writing or a Ruby class.
[748.30 → 751.68] And then Decal doesn't have a broker, right?
[751.80 → 758.88] So with Nanite, you had to deal with setting up RabbitMQ, and its high availability is a little bit tricky.
[759.14 → 761.72] You have to do like a SAN or a DRBD or something.
[762.26 → 766.14] So Decal doesn't have any of those problems because it's fully decentralized.
[766.14 → 768.78] What about Reel?
[769.98 → 774.02] So Reel is a web server I wrote on top of Celluloid.io.
[775.52 → 785.56] Some of the goals there were to have a nice modern web server without a Rack API because Rack is kind of problematic in Celluloid.
[785.56 → 793.18] Specifically, the way it implements middleware loves to sort of use a ton of your stack, right?
[794.76 → 802.80] Celluloid uses fibres, and on Ruby 1.9 YARD, at least, you only have a 4 kilobyte stack for fibres.
[803.96 → 812.52] So using Rack in conjunction with fibres is kind of impractical, as some people who tried to run like a full Rails stack on top of it discovered.
[812.52 → 826.42] So the other thing, in addition to just not using Rack, that I want to accomplish is having a nice integrated web server built on Celluloid.io with WebSocket support.
[827.36 → 835.86] That feature is kind of vaporware right now, but I've been looking at some stuff like WebSockets that's available for Ruby,
[835.86 → 842.40] and it seems like there's some pretty awesome libraries I can tap into since I try to tackle that problem.
[843.34 → 846.06] So Real appears to be pretty bare metal.
[846.54 → 847.48] Yeah, yeah.
[847.64 → 853.88] So it lacks a lot of the routing and DSL and some of the things we've come to expect from Ruby Web Frameworks.
[854.20 → 854.80] Yeah, yeah.
[854.92 → 861.96] So I suppose it's geared more towards single-purpose, just ultra-fast types of servers?
[862.64 → 868.16] Well, there's that, and also I've been trying to get it working with Web Machine.
[869.38 → 874.22] So Sean Cribs kind of pushed a proof of concept of a Web Machine driver for it,
[874.26 → 881.52] and I just need to add some missing features to Real and write some tests for that after there.
[881.52 → 887.30] And I think you can use Web Machine for all the stuff where you need a higher level of abstraction.
[887.30 → 890.14] Sean Cribs is from Basho in the ROC.
[890.14 → 890.42] Yeah, yeah.
[890.78 → 891.02] Yep.
[892.10 → 894.90] So also slings a bit of Erlang, if I recall.
[895.32 → 895.90] Yeah, yeah.
[898.04 → 902.62] So what sort of projects is you building if you're not building these low-level projects?
[902.62 → 909.62] I mean, I'm always fascinated by folks that are building frameworks and libraries that ultimately other developers build,
[910.42 → 911.86] and that's what they're doing exclusively.
[912.06 → 917.00] But what sort of, I guess, user-facing work are you doing?
[918.58 → 923.64] So I don't really have any super serious projects I'm building with Celluloid.
[923.64 → 932.64] And a couple of them I built in IRC bot called Cellular, sort of similar to Hue bot, but more Unix philosophy,
[932.86 → 934.50] where each script is just a script.
[935.38 → 939.16] And if you print from it, it prints to the IRC channel, that kind of thing.
[940.10 → 942.28] The other one is called the Cryptosphere.
[943.70 → 949.38] This is a project I recognize kind of above my technical ability right now,
[949.88 → 951.92] but it's something I like to hack on.
[951.92 → 959.76] And it's sort of like a peer-to-peer distributed encrypted data store that's completely decentralized,
[960.26 → 961.48] so anybody can join.
[963.14 → 967.46] I guess the closest projects today would be something like Freenet.
[967.76 → 969.08] There's also Gnu Net.
[970.00 → 972.54] Well, your projects have come up on a couple of episodes.
[972.72 → 976.48] The most recent ones were the Adhesion episode and then also Travis CI.
[976.48 → 982.12] So do you have, I guess, other developers that are working on their projects ping you
[982.12 → 987.04] and asking you questions about how to integrate Celluloid, or are you actively marketing the project?
[987.62 → 988.52] Yeah, definitely.
[988.80 → 994.48] So there's an IRC channel just found Celluloid on Free node.
[994.74 → 998.08] And actually there's been quite a bit of traffic in there lately.
[998.08 → 1004.18] So yeah, like Ben Lang field, I believe is his name for Adhesion, right?
[1004.90 → 1005.62] Has been...
[1005.62 → 1005.94] Right.
[1006.24 → 1012.18] I mean, he isn't on the IRC channel per se, but he's definitely been one of the main ones talking to me.
[1012.32 → 1019.26] And obviously Erlang was created for telephony, so I think that's a perfect fit there.
[1019.26 → 1026.18] But yeah, I mean, there's been a lot of people who already have a project, and they've, you know,
[1026.20 → 1030.34] been dealing with some of the issues of threads, and they're like, I just want something simpler.
[1031.06 → 1037.70] So it's been a lot of investigation of rewriting existing projects with Celluloid.
[1038.84 → 1042.28] Are you seeing an uptick in adoption of these projects?
[1042.74 → 1045.92] Yeah, or not, if not adoption, then interest.
[1045.92 → 1051.84] So, you know, just people who've, you know, they basically are to the point where they're like,
[1051.90 → 1055.40] I need a framework because my multi-thread program is too complex.
[1055.86 → 1060.14] So definitely a lot of interest from that type of person.
[1060.78 → 1068.04] How much influence, if any, have you gotten from either Node or Twisted or some of the other frameworks in the other languages?
[1069.12 → 1074.82] So definitely I've gotten a lot of inspiration out of Python.
[1075.92 → 1083.80] There are a lot of similar projects to this that I had sort of looked at when I was originally developing Reactor.
[1085.36 → 1091.10] Some of those are like, there's one called Camellia, another one called Event let.
[1092.42 → 1095.28] So those projects were pretty influential.
[1095.28 → 1102.40] See beyond that, I mean, the main influence of Celluloid in general is Erlang.
[1102.40 → 1108.50] Hey, everyone, just wanted to tell you about a cool project that supports the Changelog.
[1108.56 → 1110.48] It's called Hacker Newsletter.
[1110.68 → 1117.88] It's a weekly newsletter delivered every Friday that shares some of the best articles on startups, technology, programming, and more.
[1118.30 → 1123.46] All links are curated by hand from the ever-popular Hacker News website.
[1123.46 → 1130.88] And right now, two big events are happening, the 100th issue of Hacker Newsletter and 10,000 subscribers.
[1131.62 → 1140.40] So to celebrate, 10 lucky subscribers who opened the 100th issue, which comes out June 8th, will win some very cool prizes.
[1141.08 → 1144.68] For full details, subscribe today at HackerNewsletter.com.
[1144.68 → 1148.66] Shifting gears for a moment, we had a plan to talk about Light Rail.
[1148.88 → 1156.54] And from the time that we set up this interview until today, there's been another project that's been introduced, which is the Rails API.
[1158.12 → 1164.70] So we were talking before we started recording, and it sounds like you're going to kind of shut her down on Light Rail.
[1165.50 → 1170.42] Yeah, so, I mean, the whole goal of Light Rail was working at Strobe.
[1170.42 → 1177.76] I was there with three Rails core members, Yehuda Katz, Carl Leak, and Jose Valid.
[1178.52 → 1191.72] And Carl and Jose had built a Rails 3 stack specifically for Strobe, which had been stripped down to Action Controller Metal specifically.
[1192.76 → 1195.36] And from there, we just pulled in the stuff we needed.
[1195.36 → 1200.92] So I thought I'd just put that out there and see if it stuck.
[1201.80 → 1205.46] And, you know, I talked to Jose, like, is this a good idea?
[1205.58 → 1206.64] Am I competing with Rails?
[1207.42 → 1214.12] And it turns out I was kind of competing with Rails, even though Jose gave me the go-ahead to release it there.
[1214.12 → 1224.52] But, you know, it's been a little bit of a debacle trying to get a standard way to build Rails apps that are only JSON APIs.
[1225.66 → 1231.08] But now I would say don't use Light Rail, check out Rails API instead.
[1231.92 → 1234.08] From Santiago Pastries, I should mention.
[1234.56 → 1235.04] Yeah, yeah.
[1235.12 → 1235.88] It's on the blog.
[1236.78 → 1242.62] Any big differences between what they've done with Rails API and what Light Rail is, was?
[1242.62 → 1253.14] So Rails API contains a lot of stuff that's an evolution of stuff that Jose had originally developed that we shipped in Light Rail.
[1254.02 → 1264.46] He had this thing called wrappers in Light Rail that actually has been pretty much completely rewritten and replaced by this thing called Active Model Serializes.
[1264.46 → 1269.58] But the basic idea is there's a canonical way to represent JSON.
[1271.50 → 1278.12] So, you know, like right now, everybody makes their own JSON APIs, and they all look completely different.
[1279.06 → 1288.54] So Active Model Serializes was trying to give you a way to standardize so everything that sort of talks this specific JSON format can all talk to each other.
[1288.54 → 1293.54] And you don't have to write a bunch of one-off JSON generators and JSON clients.
[1294.56 → 1297.52] Is that set a level above the models?
[1297.62 → 1298.48] Are they mixed into the models?
[1298.58 → 1299.58] Is it a presenter pattern?
[1299.74 → 1301.06] How does that work?
[1301.44 → 1308.70] It's its own object that interacts with the models, but has some context beyond what the model does.
[1308.70 → 1311.80] I think right now the context is only the current user.
[1312.66 → 1326.96] But it provides an abstraction for serializing JSON and specifically stuff like you have a client who wants to pull in a resource, but that has a bunch of associations, and you want to grab those all in a single request.
[1327.88 → 1330.06] It gives you an abstract way to do that.
[1330.06 → 1332.00] That's a common use case.
[1332.10 → 1342.96] I think that's a lot of times when a lot of these projects in this space kind of fall down for me is they assume that you've got one representation of this particular resource throughout your entire API.
[1343.34 → 1349.66] And a lot of times there's little nuggets that you want to share in this context that you want a fuller representation in another context.
[1350.94 → 1357.26] I've been using Builder, which is DHH's project recently, and I've liked it for that reason.
[1357.26 → 1364.70] You kind of handcraft and roll your own JSON in that regard, and it supports partials and views.
[1366.16 → 1367.98] Terrible name, but neat project.
[1368.92 → 1381.48] I mean, I think that's kind of the underlying philosophical debate is like, is a serialized closer to a view, or is it actually some higher level abstraction that's completely different?
[1381.48 → 1389.92] There's a lot of room for, I guess, implementation details when you come to build an API in Rails.
[1390.32 → 1405.82] I know that the Rails way is to really support bare array APIs, and it seems like inevitably you want some sort of wrapper envelope or something or some sort of response object where the actual return value is hanging off of that.
[1405.82 → 1414.16] So that you can see the total number of records and pagination info and some other things that just, unless you stuff those into headers that are just difficult if you return bare arrays.
[1416.12 → 1430.56] Yeah, I mean, so there are actually some security concerns around bare APIs, or bare arrays, I mean, because arrays in JavaScript map onto objects, so you can redefine things that arrays do.
[1430.56 → 1435.62] And potentially a malicious script can get access to that data that way.
[1436.36 → 1439.10] So bare arrays in general are bad.
[1439.84 → 1447.92] But the real advantage of something like active model serializes, I think, is it handles relational data.
[1448.92 → 1455.42] So if you, when I was talking about including other resources, you know, there are a bunch of ways to do that, right?
[1455.42 → 1460.72] You could sort of nest the resources you want inside the one you retrieved.
[1461.62 → 1465.56] And that's bad because you could end up nesting it in several places.
[1466.30 → 1472.20] And then the question becomes, which of these is the canonical one, right?
[1472.24 → 1475.48] If you have three copies of the same resource inside your JSON.
[1475.48 → 1486.96] So active model serializes flattens that all out and then uses IDs as a way to associate, you know, the parent data to its associations.
[1487.98 → 1495.70] You know, when I came to Ruby and Rails, I guess 2006, one of the selling points was, you know, convention over configuration.
[1496.08 → 1497.80] And it was just an easy on-ramp.
[1497.86 → 1500.64] It seems like we're getting a lot more complex with the problems we're trying to solve.
[1500.64 → 1507.08] Do you see any issues with just introducing so many different decisions for the new Rails developer that's coming to the stack?
[1508.62 → 1510.60] I think it's the other way around.
[1510.74 → 1517.96] I think it makes it, say, the end user has to do less because more of these decisions have already been made for them.
[1519.26 → 1520.94] You know, some people may not like that.
[1521.04 → 1524.78] Some people may want to build their own JSON serializes.
[1524.78 → 1535.30] Having done that by hand, like, so many, many times over the years, I'd love for there to be just one solution for that problem.
[1535.64 → 1538.12] Do you consider yourself a polyglot?
[1539.04 → 1543.90] I do in that I investigate a lot of languages.
[1544.46 → 1548.08] I like to learn little tricks from them.
[1548.08 → 1553.98] But really, the only two languages I'm super comfortable with are Ruby and Erlang.
[1555.14 → 1562.92] So, I mean, there are not a lot of other languages I'd be really confident in building, like, a large project in right now.
[1563.46 → 1568.96] So, a lot of times I'll ask folks what features of languages would they want to steal and bring into their favourite language.
[1569.28 → 1571.66] And you've gone down that path with Erlang.
[1571.66 → 1577.28] I've actually, you know, in more than one way tried to fix that problem.
[1577.40 → 1583.78] Any other features from any other languages you've used other than the concurrency problems that you'd like to solve in Ruby?
[1584.92 → 1593.08] So, the two big ones I've seen kind of getting a little bit more attention lately are object capability systems.
[1593.08 → 1604.76] So, the idea of a capability system is you can have complete control over what objects in the system another object can access.
[1605.94 → 1610.40] So, this is sort of an outgrowth of the actor model itself, actually.
[1610.72 → 1615.58] So, you can introduce an object to another object, basically.
[1615.74 → 1618.94] And as soon as you do, that object can access the other object.
[1618.94 → 1625.60] And where this is a huge concern right now is in the browser, because we're trying to do mashups, right?
[1625.66 → 1627.50] We're trying to pull in third-party code.
[1628.00 → 1632.60] But right now, that code can basically do whatever it wants.
[1632.98 → 1634.68] It can go nuts on the page.
[1634.76 → 1636.86] It can read anything in the DOM.
[1637.16 → 1644.60] It can transmit stuff back to whatever server it wants via, like, a script tag or image tags or anything like that, right?
[1644.60 → 1648.74] So, the situation there is kind of out of control.
[1648.92 → 1652.82] And there's a lot of people at EMMA trying to sort that out right now.
[1654.12 → 1658.16] There's actually a language called E, which nobody's ever heard of.
[1658.44 → 1660.14] But it was built on...
[1660.14 → 1661.12] That's got to be hard to Google.
[1661.54 → 1662.00] Yeah.
[1662.72 → 1666.40] But it was built on object capability systems.
[1666.70 → 1668.64] And I think those are pretty interesting.
[1668.64 → 1675.42] The other thing I really like comes out of this framework called Kill'em on Java.
[1676.42 → 1679.12] And that's this idea of linear ownership transfers.
[1679.72 → 1688.20] So, right now, when you write a multi-thread program in immutable state language, any thread can just trash that state, right?
[1688.28 → 1691.62] Like, any thread that has the handle of the object can do whatever it wants.
[1691.62 → 1701.86] There's an ownership transfer system or way to prevent that by handing off ownership of a particular object to another thread.
[1702.82 → 1705.18] So, you can go, I'm done with this object.
[1705.36 → 1706.08] Here you go.
[1706.30 → 1710.98] And if you try to use that handle again from the original thread, it raises an exception.
[1712.32 → 1719.54] So, I think that's a good way to build safe multi-thread programs, even though you have mutable state.
[1719.54 → 1721.78] You mentioned a few patterns.
[1721.96 → 1726.02] There seems to be the scale between developer and then programmer and then computer scientist.
[1726.76 → 1726.86] Yeah.
[1727.16 → 1733.54] How fluent does a developer coming to the Rails stack or Ruby stack nowadays have to be in these patterns?
[1733.76 → 1736.18] Or how much of them are just baked into the tools they use?
[1737.50 → 1747.20] I still like to say onboarding in Rails is fairly easy once you get over the hurdle of installing Rails, especially on a Mac.
[1747.20 → 1757.28] But, you know, I think really there's not a lot of background you need to get started in Rails right now.
[1757.88 → 1763.94] I think they've done a perfect job keeping the API clean and easy to use.
[1764.58 → 1768.42] So, I wouldn't say you have to be a computer scientist to use Rails.
[1768.42 → 1773.20] There seems to be an uptick, though, in interest, I guess, in these patterns in the Ruby community.
[1773.40 → 1780.40] I'm hearing a lot more about DCI and some other patterns that keep rearing their head every couple of weeks.
[1780.72 → 1782.90] Do you have an opinion on DCI?
[1783.56 → 1787.50] I have a fairly negative opinion of DCI itself.
[1787.50 → 1796.52] If you actually read the description, it cannot be implemented in the ways that Ruby is what they're calling DCI.
[1797.26 → 1801.56] You know, they explicitly say it can't be implemented in any of those ways.
[1802.38 → 1806.08] So, the first is through a mix-in, a runtime, basically, right?
[1806.18 → 1809.62] Like, you have a module, you extend on an object.
[1809.62 → 1813.80] But, so that one's bad because it blows the method cache.
[1814.70 → 1819.24] So, there's another way to implement it, which is through delegation.
[1820.20 → 1825.46] If you actually read the DCI paper, they say you cannot use either of those to implement DCI.
[1826.36 → 1832.18] So, I'm kind of confused as to what DCI actually is if it isn't either of those things, right?
[1832.18 → 1839.88] How many of these patterns do you think have affinity to the language they were originally, you know, thought up in, I guess, like a better phrase?
[1841.36 → 1846.50] I think Ruby can handle almost object-oriented programming patterns.
[1847.30 → 1849.32] So, I mean, it kind of depends.
[1849.60 → 1854.96] The reason I ask that, a lot of times when I'm in JavaScript circles, I see Subsists that are getting into Node
[1854.96 → 1861.14] and try to, you know, port a lot of the module behaviour that we take for granted in Ruby into JavaScript
[1861.14 → 1865.00] and just, you know, start pulling their hair out because JavaScript's fundamentally a different language.
[1865.60 → 1866.14] Yeah, yeah.
[1867.06 → 1870.48] I mean, so, you could ask Hugo about that, right?
[1871.28 → 1877.42] C has actually done a full mix-in system inside of Ember.js, which has its own object model.
[1878.12 → 1879.80] Thoughts on hypermedia APIs?
[1879.80 → 1884.40] I definitely like not having to construct URLs.
[1885.24 → 1889.36] If that's really the only thing hypermedia gets you, I guess that's a win.
[1889.72 → 1891.26] We need to do a show on this.
[1891.50 → 1893.72] I'm still kind of on the fence myself.
[1893.92 → 1894.80] I like the promise.
[1894.98 → 1900.40] I mean, everybody's got this dream of pointing, you know, some sort of code to a root URL
[1900.40 → 1903.12] and just have this wrapper organically unfold.
[1903.12 → 1911.14] What troubles me about a lot of the things that I'm reading is just the lack of type on some of the returns.
[1911.38 → 1916.52] And the folks that are building out hypermedia APIs will talk about, well, it's just mime types, right?
[1916.98 → 1917.14] Yeah.
[1917.14 → 1919.84] A lot of their examples are HTML and XML, which are not typed.
[1919.96 → 1926.26] And then as, you know, just a Joe Blow Ruby wrapper developer that I am, you know,
[1926.26 → 1931.66] there are things we take for granted and that Jason has just made like a dial tone.
[1931.76 → 1933.04] We don't even think about it, right?
[1933.22 → 1933.36] Yeah.
[1933.36 → 1938.26] If I have to sit there and construct, you know, objects for every mime type I'm going to consume, I'd go crazy.
[1939.46 → 1939.82] Yeah.
[1940.02 → 1945.24] I mean, that's where you get into stuff like soap did code generation and that kind of thing.
[1945.24 → 1948.50] So, you know, I mean, perhaps it could be done at runtime.
[1948.86 → 1954.12] Perhaps you could point something at an API and have it metaprogrammed all that stuff for you.
[1954.22 → 1955.04] I'm not really sure.
[1956.22 → 1961.82] You know, I'm kind of on the distributed objects side of that debate, right?
[1961.94 → 1968.40] Like, you know, there's all this stuff that requires a lot of standardization if we're building HTTP APIs,
[1968.52 → 1971.40] which just goes away if you're using distributed objects.
[1971.40 → 1974.78] I should say I'm quite ignorant on the subject so far.
[1974.86 → 1979.70] I'm learning more, but we need to do a show with Micah Munson and maybe Steve Flank,
[1979.82 → 1982.16] our contributor here on the changelog.
[1982.26 → 1985.66] He's got a book coming out on hypermedia APIs just to talk about the subject.
[1985.66 → 1991.64] It seems to be really hot, but also kind of it's one of those things where, you know,
[1991.68 → 1997.98] if you are in JavaScript circles, if you want to end a debate, you just, you know, start screaming Crockford, right?
[1997.98 → 2002.92] And if you're talking about big data, you'll say, you know, Dynamo and Werner Juggles, right?
[2003.30 → 2007.96] But if it's HTTP and REST now, it seems like people just scream fielding.
[2008.78 → 2014.38] Nobody really understands that paper, but yet we all claim this is what fielding would have wanted.
[2015.48 → 2019.16] I mean, I think we have the problem solved fairly well.
[2019.26 → 2022.58] It's all just kind of bike-shedding around these little minor issues.
[2022.58 → 2027.26] I guess my big thing is we're still trying to embrace REST.
[2027.90 → 2028.34] Yeah, yeah.
[2028.96 → 2032.46] And I'm happy when I stumble across a Resist API.
[2033.34 → 2039.22] As long as they're not wrapping, you know, clearly wrapping every database table, you know,
[2039.24 → 2042.92] as a REST endpoint call, that's fine.
[2042.92 → 2051.00] As long as I don't have to deal with a schema or document-type definition, I'm cool with it too.
[2051.18 → 2058.04] But it seems like we're raising the bar a bit on people that are still trying to get their heads around Resist APIs.
[2058.80 → 2059.26] Yeah, yeah.
[2060.72 → 2065.88] So when you're not hacking on celluloid or decal or some of these other projects,
[2066.06 → 2067.80] what's got you excited as far as open source?
[2067.80 → 2079.08] So there's a project I've been contributing to in Python called Tahoe, the least authority file system.
[2079.96 → 2084.88] I just redesigned their landing page there because it's kind of ugly.
[2085.94 → 2088.88] But this is a really neat tool.
[2089.36 → 2091.22] So I mentioned the cryptosphere earlier.
[2092.20 → 2094.18] Tahoe is kind of the inspiration for that.
[2094.18 → 2101.28] But it's a great tool for if you want to run a cooperative backup system with your friends.
[2102.08 → 2106.26] If you have a bunch of people who have cable modems or run servers or whatever,
[2106.46 → 2110.32] you can kind of just install this on all those computers.
[2110.86 → 2114.82] And so long as the bandwidth and storage is more or less free to you,
[2115.38 → 2118.22] then you get free collaborative backups with this.
[2118.22 → 2120.18] And you can also use it to share data.
[2121.24 → 2123.96] So I've been really enjoying that.
[2124.18 → 2128.32] I'm definitely a big fan of Travis CI.
[2128.68 → 2133.58] I just got to hang out with all those guys at Hailstone, except for Matthias.
[2134.78 → 2139.50] I finally got an invitation to the private version of that.
[2139.58 → 2140.68] It's quite well done.
[2141.06 → 2141.70] Yeah, nice.
[2144.02 → 2146.04] I have not seen it myself yet.
[2146.60 → 2147.94] What about your text editor?
[2147.94 → 2151.62] So I use a few different ones.
[2152.16 → 2155.40] I still use Text man as my primary editor.
[2156.94 → 2160.32] I have been sort of investigating Mac Vim.
[2161.10 → 2165.18] So I've known how to use Vi since I was like 13 or something.
[2165.18 → 2170.88] But I don't really like using it as my day-to-day editor, I guess.
[2172.72 → 2175.02] So I'm a Mac user, right?
[2175.10 → 2180.34] And OS X is this sort of ubiquitous Emacs-style key bindings throughout the whole OS.
[2180.34 → 2189.58] So if I go to switch to Vim, I have to sort of context shift to Vim mode instead of just using the Emacs key bindings.
[2190.64 → 2194.28] I played around with Emacs quite a bit when I was learning Clojure.
[2194.28 → 2199.88] And it seems pretty cool, but I just couldn't get over the learning curve.
[2200.30 → 2205.78] And I wasn't really sure if I did, I would really actually enjoy it.
[2206.38 → 2211.58] So yeah, for now, I generally kind of stick with TextMate.
[2211.68 → 2216.34] And I use Vim on the command line for sort of short one-off type edits.
[2216.96 → 2218.46] What was your thoughts on Clojure?
[2219.44 → 2220.94] I really like Clojure.
[2220.94 → 2225.72] I think it solves a lot of the problems that made Lisp impractical in the past.
[2227.74 → 2232.36] You know, just being on the JVM, they can tap into the whole ecosystem of JVM libraries.
[2233.68 → 2236.18] And they finally, well, they being Roach Hickey,
[2236.42 → 2241.46] finally added syntax for some other data structures besides Lisp, right?
[2241.58 → 2244.92] So it has maps and vectors that are really handy.
[2246.40 → 2249.66] As far as trying to build something big in Clojure,
[2249.66 → 2254.76] I'm just not sure if I would really prefer doing it in Clojure to Ruby.
[2256.46 → 2264.26] In terms of everything like maintainability and my ability to sort of comprehend the code base,
[2264.36 → 2266.72] I think it's just easier to do in Ruby.
[2267.50 → 2270.74] Although I think probably the result, if I wrote in Clojure,
[2270.80 → 2273.64] would be a lot faster and have better performance.
[2273.64 → 2275.52] Do you have a programming hero?
[2276.46 → 2277.88] Yeah, it's a tough question.
[2278.00 → 2279.08] I guess I have a few of them.
[2280.02 → 2281.80] I'm a big fan of the Erlang guys.
[2282.86 → 2288.18] I've never met Joe Armstrong, but I've met the co-creator of Erlang, Robert Herding.
[2289.00 → 2291.74] And they're both pretty cool guys.
[2291.84 → 2294.62] I think they were really way ahead of their time with Erlang.
[2294.62 → 2302.48] And a lot of this stuff, you know, it's becoming relevant now that we have these massively multicore computers
[2302.48 → 2307.44] and really fast internet and everybody's building distributed programs now.
[2308.00 → 2311.46] I ask all three of those questions now because the last three episodes,
[2311.58 → 2313.42] see, I always assume that nobody's ever heard this show.
[2313.42 → 2318.36] So we kind of end the episodes and those questions.
[2318.54 → 2322.02] The last three episodes we've hung up and someone's pasted in our chat later,
[2322.58 → 2324.72] hey, dude, you didn't ask me X question.
[2325.00 → 2326.66] I still had my answer ready.
[2328.12 → 2329.84] All right, nice chatting with you today, Tony.
[2329.96 → 2333.46] Thanks for giving us the lowdown on celluloid and the other projects.
[2333.66 → 2334.12] Appreciate it.
[2334.24 → 2334.70] Yeah, cool.
[2334.70 → 2353.20] See it in my eyes.
[2353.66 → 2356.74] So how could I forget when?
[2358.18 → 2362.58] I found myself for the first time.
[2362.58 → 2366.30] Safe in your arms
[2366.30 → 2368.56] And the dark passion
