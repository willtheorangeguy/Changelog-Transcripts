[0.00 --> 18.34]  Welcome to the ChangeLog episode 0.3.1.
[18.64 --> 19.64]  I'm Adam Stachowiak.
[19.78 --> 20.52]  And I'm Wynne Nethelen.
[20.76 --> 21.62]  This is the ChangeLog.
[21.66 --> 23.66]  We cover what's fresh and new in the world of open source.
[24.08 --> 26.92]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.92 --> 29.12]  Also head to github.com forward slash explore.
[29.12 --> 33.78]  You'll find some trendy repos, some feature repos from our blog in the audio podcasts.
[34.12 --> 37.36]  If you're on Twitter, follow ChangeLogShow, not the ChangeLog.
[37.50 --> 38.18]  And I'm Adam Stach.
[38.36 --> 40.66]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.04 --> 44.58]  Fun episode this week, talking web sockets with some experts in the area.
[44.94 --> 50.44]  Peter over at Yahoo, Martin from Push Your App, and Guillermo from Socket.io,
[50.62 --> 53.70]  along with guest host Michael Smith from Way Down Under again.
[54.12 --> 55.36]  Yeah, that's a nice line up there.
[55.36 --> 61.38]  Yeah, Michael's got a project node WebSocket server that is an implementation of WebSocket server side.
[61.46 --> 63.36]  So I guess we should mention what WebSockets are.
[63.78 --> 64.46]  Yeah, what is it?
[64.64 --> 70.10]  It's a persistent connection between the browser and the server so that you can do server push down to the browser
[70.10 --> 76.52]  and they can just open that long-running connection and it's more two-way, bi-directional communication between client and server
[76.52 --> 80.70]  without having to do long-pulling or AJAX techniques like we currently do.
[81.32 --> 85.44]  Right. So the idea is to move away from the AJAX piece of it, speed it up, and be more native?
[86.04 --> 90.34]  Yeah, especially as more and more apps are poised to go real-time,
[90.44 --> 94.08]  this is just the ever-evolving landscape of web development.
[94.32 --> 94.68]  Cool.
[95.12 --> 96.50]  Fun episode this week. Should we get to it?
[96.76 --> 97.32]  Let's do it.
[97.32 --> 112.02]  All right, we're joined today by Peter, Martin, and Guillermo and Michael Smith to talk about HTML5 WebSockets.
[112.38 --> 115.78]  Before we dive right in, let's go around the horn and each of you introduce yourself,
[115.96 --> 120.34]  kind of what you do in the landscape of WebSockets, where you work, and your role there.
[120.52 --> 121.26]  Peter, let's start with you.
[122.30 --> 127.08]  So I'm Peter Grice. I work at Yahoo. I'm a principal engineer. I work on mail.
[127.74 --> 130.44]  We're looking at using WebSockets for a couple of different things.
[130.58 --> 133.80]  We don't have anything in production yet because, obviously, WebSockets is pretty new,
[133.98 --> 138.00]  but we're looking at using it for adding different real-time features to mail,
[138.18 --> 140.10]  message notifications, other things like that,
[140.40 --> 145.16]  and also doing some experiments with using it to accelerate attachment uploads.
[145.84 --> 146.62]  All right, Martin?
[147.18 --> 150.28]  Hi there. I work at a company called New Bamboo.
[150.74 --> 152.48]  We're a Ruby shop in London.
[153.88 --> 157.30]  So as well as client projects, we've got a few products that we're working on at the moment.
[157.32 --> 163.84]  One of those is called Pusher App, and the idea of Pusher App is making it really simple
[163.84 --> 168.16]  for people to be able to push events to browsers.
[168.62 --> 175.86]  We have an API which you push events to, and those are then via a PubSub model sent to browsers.
[175.86 --> 183.32]  We've used this internally on a few of our client projects and other products,
[183.54 --> 184.82]  and it's been working really nicely.
[185.42 --> 186.70]  I should say WebSockets.
[187.10 --> 190.70]  We use WebSockets to implement Pusher App.
[191.26 --> 191.64]  Guillermo?
[192.28 --> 192.56]  Hello.
[192.56 --> 194.14]  My name is Guillermo Rauch.
[194.36 --> 198.66]  I'm the CTO of LearnBoost, an education startup in San Francisco.
[199.48 --> 202.72]  And I created Socket.io, which is two projects.
[203.04 --> 208.34]  One is a client that provides WebSocket-like API on the browser
[208.34 --> 215.34]  that basically gives you WebSocket and a bunch of other different transports
[215.86 --> 222.76]  in a way that jQuery provides $AJAX,
[223.20 --> 229.38]  and they give you XML HTTP requests for standard-compliant browsers
[229.38 --> 232.16]  and ActiveX object for Internet Explorer.
[232.54 --> 237.80]  I do the same thing for many different browsers and many different transports,
[237.80 --> 242.24]  but the developer thinks it's a WebSocket-like API.
[242.72 --> 246.02]  On the server side, I created Socket.io-node,
[246.18 --> 249.54]  which is an implementation of all these different types of requests
[249.54 --> 255.72]  so that you also develop as if you were receiving data from a socket.
[256.50 --> 256.98]  Perfect.
[256.98 --> 262.92]  So regular listeners of the ChangeLog will know that we normally cover projects
[262.92 --> 266.90]  on the podcast, but sometimes we take a step back and cover broader topics,
[267.10 --> 269.64]  and we'll dive into some of your projects in just a moment.
[269.90 --> 272.78]  But, Michael, why don't you give an overview for those that might not know
[272.78 --> 276.04]  what WebSockets is and why it should get us excited.
[276.96 --> 277.56]  Okay, sure.
[278.10 --> 284.26]  WebSockets are a new piece of technology that is currently falling under the umbrella term
[284.26 --> 285.24]  of HTML5.
[285.24 --> 291.18]  They're basically a way to get bi-directional communication between your web browser
[291.18 --> 298.68]  and a server, and there's no need for constantly opening up new connections
[298.68 --> 300.10]  or things like that.
[301.06 --> 306.26]  So very fast, very real-time, quite similar to almost having a TCP socket,
[306.26 --> 308.40]  although there's a bit more to it than that.
[309.46 --> 314.12]  And currently we've got browser support in Safari, Chrome,
[314.62 --> 319.84]  Firefox 4 is coming, I've heard, and same with an internal build of Opera.
[320.70 --> 325.52]  I haven't heard anything on Internet Explorer support, but we can only hope.
[325.52 --> 331.80]  So speaking of support for additional browsers, I guess both in Socket.io and Push Your App,
[331.86 --> 335.92]  you guys are doing some fallback techniques for older browsers.
[336.70 --> 339.36]  Martin, why don't you speak for a moment what you guys are doing in Push Your App for those?
[339.36 --> 340.36]  Right.
[341.60 --> 345.36]  We actually use a library which...
[345.36 --> 347.50]  Well, sorry, I'll start again.
[347.92 --> 351.52]  We actually use a library that is called...
[351.52 --> 352.68]  I need to look it up, actually.
[352.82 --> 352.98]  Sorry.
[354.08 --> 356.10]  Feel free to go first on Socket.io.
[356.52 --> 357.20]  Yeah, for a second time.
[357.56 --> 359.42]  Guillermo, why don't you jump over and take that?
[359.78 --> 360.10]  Sure.
[360.10 --> 360.54]  Sure.
[362.04 --> 364.20]  The way that Socket.io works on the client,
[364.38 --> 369.28]  it uses feature detection for deciding what transport to use.
[369.80 --> 373.52]  So if the WebSocket constructor is there, it will, of course, use WebSocket.
[374.00 --> 378.60]  And on the server side, Node will trigger an upgrade event
[378.60 --> 381.76]  based on this handshake that is produced.
[382.52 --> 386.56]  And, of course, the communication will happen normally like any other WebSocket server.
[386.56 --> 394.86]  However, like Michael said, there is limited support for WebSocket today.
[395.60 --> 397.56]  And so we have to resort to other transports.
[398.88 --> 407.58]  An example is called HTML5, which is an iframe that is inserted into an ActiveX object component
[407.58 --> 413.40]  so that the spinner in the browser is not triggered when fetching data from an iframe.
[413.40 --> 416.98]  So this is all done transparently by Socket.io.
[417.26 --> 425.30]  And this technique was actually discovered by or made popular by the Gmail chat engineers a few years back.
[426.04 --> 429.96]  And that's the sort of thing that Socket.io solves for you.
[430.12 --> 433.16]  So how does that differ from Pusher app, Martin?
[433.16 --> 438.14]  Yeah, so what we do on Pusher app is we use a library called WebSocket.js,
[438.86 --> 444.70]  which uses a flash socket to emulate a WebSocket effectively.
[445.56 --> 454.02]  It connects to the WebSocket server using all the same handshakes as a real browser-initiated WebSocket.
[454.28 --> 456.30]  And it exposes the same API in JavaScript.
[456.30 --> 463.42]  So we sense whether the WebSocket is available at the browser level.
[463.52 --> 465.12]  If not, we use the WebSocket.js.
[465.52 --> 473.28]  And what we also do is we first initiate a non-secure, a non-TLS WebSocket connection.
[474.30 --> 480.58]  That fails for a large number of proxies, intermediary proxies, which we probably come on to in future.
[480.92 --> 484.62]  And we fall back to a secure WebSocket in those cases.
[484.62 --> 490.66]  And we'll put this in the show notes, but it looks like WebSocket.js is another open source project like Socket.io.
[490.88 --> 492.40]  Yes, yes it is, yes.
[493.36 --> 493.64]  Peter?
[494.74 --> 495.80]  Go ahead.
[497.42 --> 501.86]  Yeah, actually Socket.io also uses FlashSocket if Flash is available.
[502.32 --> 509.94]  So like I said, using feature detection, I can know if the client has Flash installed and ready to use, and I pick that one.
[509.94 --> 516.36]  So Socket.io has also a priority list based on how bidirectional the transports are.
[516.66 --> 518.44]  So it will try with WebSocket first.
[518.78 --> 535.26]  It will try with Flash second, which might fail if the client is behind the proxy, because the WebSocket protocol in their draft specifies using the connect HTTP method to bypass proxies.
[535.26 --> 542.00]  This cannot be done by Flash, because Flash doesn't have the authentication information of the proxy.
[542.28 --> 545.40]  It's not given to Flash by the user agent.
[545.90 --> 549.42]  So Flash WebSocket.js will fail behind proxies.
[549.92 --> 560.40]  In that case, Socket.io will fall back to other transports like long polling, HTML file, which have higher latency, and that's why they are lower on the list of priority.
[560.40 --> 566.42]  So from an architecture standpoint, how would WebSockets differ for something like traditional long polling?
[567.30 --> 571.24]  Well, this is what essentially Socket.io solves.
[571.42 --> 574.96]  Those two methods of communication are really different.
[575.92 --> 582.06]  In one, you know that the socket will be open, and you have three events, connect, disconnect, and message.
[582.06 --> 588.88]  And with long polling, you essentially have many disconnections on the request side.
[589.30 --> 596.32]  So there is a chance that the server might try to send a message to the client, and the client is temporarily disconnected, or he's between reconnections.
[596.66 --> 598.70]  So a long polling request is closed.
[599.40 --> 603.52]  The server tries to send a message before the client opens another one.
[603.52 --> 605.50]  So that's another thing that Socket.io does.
[605.84 --> 621.98]  It buffers messages that are sent between these disconnections by the client, and when the client reconnects, it sends him a buffer, a chunk of messages, while he was temporarily disconnected, which might be a couple milliseconds, or, I don't know, depending on the client's connection, it can be a long time.
[622.56 --> 624.28]  Can I ask you a quick question, Guillermo?
[624.28 --> 639.98]  How do you manage to, if you're going to scale this, and you need more than one Node.js server, do you have to make sure that the request is sticky, so the reconnection comes back to the same process, in order for that buffering to work, or how do you do that?
[639.98 --> 640.20]  Exactly.
[640.94 --> 642.84]  Yeah, for now, it's a single process.
[642.84 --> 664.58]  Of course, of course, you can put a message queue or a Redis server in front of it, and you can make it scaled to different nodes in terms of, like, since the information you deal with will be in one process, scaling takes a little more work, but it's definitely possible.
[664.58 --> 678.50]  So, another thing you could do is use an HTTP load balancer to direct the request to a particular server instance, either using any of the headers that are in there, or inspecting other properties of the request.
[678.50 --> 694.88]  Typically, this is harder to do on, you know, if there are multiple processes on a single box, but if your router is smart enough, or if you have enough routing smarts in the manager on the box itself, you can do that, without actually needing to have a separate data store, like a Redis, or whatever.
[696.36 --> 705.58]  Yeah, we're actually using a load balancer called HA Proxy for PusherApp, which we found works extremely well.
[705.58 --> 714.46]  Well, we're using it in layer 4 mode, but you can, it allows you to do a lot of the sticky sessions support, that kind of thing.
[715.00 --> 723.06]  Okay, so, if you were to do load balancing within, say, Node, how would you go about doing it?
[723.18 --> 728.92]  Would you still use that load balancing server, or would you use some other technique?
[730.02 --> 731.28]  You might want to answer that, Peter.
[732.82 --> 733.22]  Sure.
[733.22 --> 736.82]  So, there are a couple of different ways of doing it within Node.
[737.02 --> 745.58]  A lot of the frameworks that exist today, like Connect or Multinode, are both good at distributing incoming connections among a bunch of different processes.
[746.42 --> 751.06]  For these guys, they don't have any support for stickiness at all.
[751.24 --> 757.76]  So, any incoming request has, you know, a relatively equal chance of being served by any of the processes, so that doesn't really get you what you want.
[757.76 --> 773.68]  What you can do instead is accept all connections in one process, read part of the request, enough of the request to know which process should be serving it, and then go and send the socket and the part of your request that you saw off to the right worker.
[773.68 --> 778.56]  I have a blog post up on how to do this that can probably go out in the show notes or something.
[778.88 --> 781.28]  But, you know, you can use that technique.
[782.16 --> 786.24]  Is there anything intrinsically browser-dependent as far as the client side?
[786.24 --> 790.50]  Because I know, you know, XHR really took off.
[790.62 --> 793.28]  You know, it made Ajax possible, right?
[793.78 --> 799.90]  But I've seen that same technique, asynchronous calls in iPhone applications that are native applications.
[800.12 --> 804.16]  Would this be something that someday may be used in a native mobile device?
[804.16 --> 812.08]  Okay, currently there is support in, well, sort of support in iPhone libraries.
[812.50 --> 820.96]  There's, I think, two projects that give you the headers required to include WebSockets within your iPhone app.
[821.78 --> 824.32]  Although I don't think they're currently supported.
[825.00 --> 830.98]  I think they were drafted for iPhone 4, but they didn't make it in in time.
[831.48 --> 833.10]  So I might have more information on that.
[834.16 --> 843.14]  As for the browser side, the main thing that needs to be done is for, A, the browsers to implement the protocol.
[844.32 --> 849.82]  And then to make sure that they actually communicate and use it.
[849.82 --> 860.36]  And actually do the communication of the protocol with the server in the proper ways.
[860.36 --> 867.78]  So Guillermo and Martin, what types of applications are you guys seeing being built with Socket.io and with Pusher App?
[868.36 --> 870.04]  I've heard of a couple different ones.
[870.04 --> 878.62]  There are some projects that build on top of Socket.io to give you, like, APIs to build different things more easily.
[878.62 --> 883.52]  Because essentially, Socket.io only gives you the socket API.
[884.08 --> 887.42]  So you need to do a little more to build an application.
[887.74 --> 897.52]  Although you can build a thin protocol based on JSON, pass JSON messages, and, like, have a chat application like the example that ships with Socket.io.
[897.52 --> 903.76]  A really interesting one is called Dnode, which does asynchronous remote method invocation.
[904.86 --> 907.98]  This was created by the Stack VM guys.
[907.98 --> 916.02]  And it's built on top of Socket.io, and it's a good base for building applications.
[916.50 --> 924.34]  I've also seen a chat application with video enabled by Flash and avatars that move on the screen.
[925.04 --> 928.48]  I've seen an Asteroids game built with Socket.io.
[928.48 --> 939.72]  And recently, I heard of someone trying to build a drawing application, which was passing many, many messages by many people at the same time.
[940.48 --> 944.44]  Socket.io used to rely on JSON for doing message buffering.
[944.72 --> 948.20]  So it would send you an array of messages, and it would be parsed by JSON.
[948.50 --> 956.76]  That turned out to be, like, very CPU intensive, and it's been since removed in 0.5, which was released this week.
[956.76 --> 972.90]  So today, it's suitable for many different applications, from games to chat applications, or tying your data model to making your data alive on browser with something like Dnode.
[973.36 --> 981.58]  From my point of view, the way Pushar App actually came about was that we had an application called TrueStory,
[981.58 --> 986.90]  which is a collaborative application to manage an Agile backlog.
[987.54 --> 997.70]  And what we wanted is that we wanted, so you could have edit stories in one browser, and those stories would be, the changes would be reflected in another browser.
[998.48 --> 1002.24]  You could drag and drop, reorder, change sprints, and that kind of thing.
[1002.24 --> 1007.64]  And so we actually, that's one of the reasons that Pushar exposes a kind of event-binding API.
[1008.26 --> 1015.08]  So in the browser where the event was being changed, or sorry, where the story was being changed,
[1015.50 --> 1022.44]  we'd trigger an update call would go to your, you know, Rails application or whatever,
[1022.44 --> 1028.96]  and that would send a story-updated event on the channel to all the subscribers,
[1029.10 --> 1031.14]  all the people who are viewing the backlog in their browsers.
[1032.04 --> 1037.04]  So we've seen some people do application, you know, collaborative applications like that.
[1037.92 --> 1044.40]  The other thing we've seen a lot of on Pushar is people who are just using Pushar
[1044.40 --> 1049.18]  because it's so easy to send data out to browsers.
[1049.40 --> 1054.58]  So real-time Twitter feeds, just real-time information.
[1055.76 --> 1064.30]  Group Dashpon is one example where real-time purchases on Groupon are displayed on Google Maps, for example.
[1065.16 --> 1071.54]  Another example we've got is another drawing application where users can draw pictures on their iPad,
[1071.54 --> 1076.10]  and those drawings are shown in real-time on the web.
[1076.62 --> 1078.16]  That's called WebPad.
[1078.56 --> 1084.96]  Martin, talk a moment about channels in Pushar, and how many channels would I have in an application?
[1085.32 --> 1088.24]  Is my app a channel, or would I have multiple channels in my app?
[1088.94 --> 1091.20]  It very much depends, actually, on the application.
[1091.64 --> 1095.00]  For example, the application I spoke about, Group Dashpon,
[1096.04 --> 1100.86]  that I believe has a single channel, which is Groupon purchases.
[1100.86 --> 1105.28]  So everybody who's viewing that web page would be subscribed to that channel.
[1105.78 --> 1109.40]  So there could be potentially hundreds of users subscribed to one channel
[1109.40 --> 1114.82]  and pushing information out efficiently to all of those users via a single API call.
[1115.50 --> 1121.86]  In the TrueStory collaborative application, there might be a single channel per backlog.
[1121.86 --> 1128.92]  So you might, in your web application, you have domain objects,
[1129.10 --> 1136.30]  which you want to share their state, share state on those domain objects with other users.
[1137.32 --> 1143.02]  So there may be, I don't know, 10 people using the application at the same time,
[1143.52 --> 1145.96]  each, you know, two of them each viewing each backlog.
[1145.96 --> 1148.86]  So there would be a channel for each of those.
[1149.60 --> 1151.28]  But typically, we're seeing it.
[1151.44 --> 1156.24]  It's not that there is, in most cases, we don't have a single channel per user.
[1156.60 --> 1161.34]  It's a channel per object, which people collaborate on or are interested in.
[1162.06 --> 1166.62]  Okay, so I should also note that the channels that Martin is speaking of,
[1166.82 --> 1169.70]  they're not actually built into the WebSocket protocol,
[1169.70 --> 1173.64]  but rather a layer on top of them,
[1174.12 --> 1180.00]  which I think you're still using URL-based routing or something?
[1181.62 --> 1184.98]  No, what we do, we started with that approach, you're right.
[1185.84 --> 1189.34]  The way we do it at the moment is that once the WebSocket is connected,
[1191.04 --> 1195.26]  the JavaScript sends a JSON event.
[1195.26 --> 1201.32]  I mean, it's just JSON, but it has an event name,
[1201.46 --> 1204.72]  which is push or subscribe and the name of the channel.
[1205.38 --> 1207.52]  And then internally, in the Socket server,
[1207.66 --> 1211.82]  we then subscribe to the queue that publishes those events.
[1212.62 --> 1213.84]  And so, yes, you're absolutely right.
[1214.06 --> 1217.26]  Channels are an abstraction which we've added on top of WebSockets.
[1217.26 --> 1224.04]  And the other abstraction we've added is the idea of being able to trigger events
[1224.04 --> 1227.40]  and have those events then triggered in JavaScript.
[1227.66 --> 1232.22]  So it's just a matter of saying push a .bind event name
[1232.22 --> 1235.58]  and then the anonymous function which you want to be executed.
[1236.16 --> 1237.00]  But you're absolutely right.
[1237.10 --> 1242.02]  These are things that we've added on because our applications,
[1242.32 --> 1243.96]  they all needed that kind of thing.
[1243.96 --> 1249.24]  Okay, so going off the idea of triggering events and things like that,
[1249.40 --> 1258.16]  there's also a new HTML5 protocol which is called EventSource,
[1259.02 --> 1264.90]  which allows you to trigger events on the browser from the server.
[1265.32 --> 1266.64]  I'm not sure if it's bidirectional.
[1267.58 --> 1269.78]  Peter, would you have any more information on that?
[1270.30 --> 1271.32]  I wish I did.
[1271.32 --> 1271.80]  Okay.
[1272.58 --> 1278.38]  The way I understand it is EventSource is pretty much a one-way WebSocket.
[1279.22 --> 1280.02]  That's the idea.
[1280.30 --> 1283.30]  From a JavaScript API point of view, that's what you get.
[1283.60 --> 1286.20]  So you can also receive events from the server.
[1286.34 --> 1287.94]  You can't push events to the server.
[1288.70 --> 1289.34]  Right, exactly.
[1289.88 --> 1294.46]  So the way that you send messages to the server is actual, like, normal AJAX.
[1294.46 --> 1300.86]  It's very similar to the multi-part flag in the XMLHTP request object,
[1301.06 --> 1303.16]  which is only supported by Firefox.
[1303.80 --> 1306.34]  That is also implemented by Socket.io,
[1306.68 --> 1309.96]  and that gives you a single way we can say WebSocket,
[1310.44 --> 1314.12]  a connection that is always open and pushing parts of messages.
[1314.12 --> 1318.74]  In that respect, EventSource is very similar to it.
[1319.62 --> 1324.20]  And it's my understanding that it's only implemented in Opera so far.
[1324.64 --> 1325.20]  I'm not sure.
[1326.00 --> 1327.46]  Sometimes the technology comes along,
[1327.50 --> 1331.42]  and it forces us to take a fresh look at how we solve some problems.
[1331.42 --> 1334.48]  I know the NoSQL database movement has done that for me,
[1334.56 --> 1338.80]  and that now when I model my data in the database,
[1338.96 --> 1342.46]  it really changes the way I look at the application as a whole.
[1343.18 --> 1348.46]  Peter, talk about what WebSockets does to how you architect applications at Yahoo.
[1349.40 --> 1349.92]  Sure.
[1350.08 --> 1354.40]  So what we're interested in with WebSockets is, you know,
[1354.50 --> 1356.20]  once browsers actually support this thing,
[1356.20 --> 1360.26]  it'll provide a first-class API that you can always use
[1360.26 --> 1363.38]  and always expect to work as opposed to going,
[1363.62 --> 1366.66]  jumping through all the hoops that Guillermo has done a great job of doing
[1366.66 --> 1370.50]  and building a library that can kind of handle all the different browser use cases,
[1370.66 --> 1374.92]  proxy use cases, different performance and connection limitations
[1374.92 --> 1376.04]  that different browsers have.
[1376.40 --> 1378.50]  You know, there's kind of a whole world of stuff
[1378.50 --> 1382.54]  that you need to try to navigate with the current set of ways
[1382.54 --> 1385.00]  that you can have this kind of full duplex communication.
[1385.00 --> 1386.56]  You know, it is doable now,
[1386.56 --> 1390.58]  and Guillermo's stuff is, you know, kind of living proof of that.
[1390.96 --> 1397.76]  But the promise of WebSockets is a unified API that you can expect to work,
[1397.84 --> 1400.52]  at least in some really small number of years,
[1400.64 --> 1403.70]  once browser and proxy support is there for that.
[1403.92 --> 1408.24]  Before we go around the horn and ask what's on each of your open source radars,
[1408.88 --> 1412.22]  Michael, why don't you give a shout-out for your own WebSocket server
[1412.22 --> 1416.34]  and then kind of list some resources that the WebSocket noob, including myself,
[1416.46 --> 1417.48]  could go and check out?
[1418.28 --> 1421.42]  Okay, so I do actually write my own WebSocket server,
[1422.26 --> 1423.28]  Node WebSocket server.
[1424.04 --> 1431.06]  It's different to Guillermo's in that rather than adding support
[1431.06 --> 1434.86]  for all the backwards compatible transport methods,
[1435.12 --> 1437.60]  it just gives you the WebSocket connections.
[1437.60 --> 1440.92]  And then as for resources,
[1441.40 --> 1444.60]  probably the best place to find out more about WebSockets
[1444.60 --> 1448.90]  would have to be the protocol outline,
[1449.26 --> 1451.98]  which is in the WhatWig working group,
[1452.38 --> 1455.08]  or, yeah, WebApps working group,
[1455.44 --> 1459.58]  which is sort of part of the W3C, but not really.
[1460.42 --> 1463.08]  And they're the ones authoring the specification,
[1463.54 --> 1466.62]  which is being led by Ian Hickson at the moment.
[1467.60 --> 1470.68]  And then there's also a few other resources
[1470.68 --> 1473.76]  that we'll link to in the show notes.
[1474.28 --> 1476.50]  I don't have URLs offhand.
[1478.20 --> 1481.08]  Or socket.io and pushyourapp.com, right?
[1482.34 --> 1483.76]  Well, this is the part of the episode
[1483.76 --> 1485.06]  where we kind of turn it upside down
[1485.06 --> 1488.62]  and ask what's on our guest, open source radars.
[1488.70 --> 1489.82]  We'll start with you, Guillermo.
[1489.94 --> 1493.68]  What open source projects have got you excited
[1493.68 --> 1495.30]  and that you want to go play with?
[1495.30 --> 1500.76]  Well, I don't know if you guys seen the Hummingbird demo for Node,
[1500.90 --> 1505.18]  which is basically WebSocket and MongoDB for real-time analytics.
[1506.18 --> 1508.22]  We're actually also users of MongoDB,
[1508.44 --> 1510.62]  and we developed our own ORM.
[1510.62 --> 1514.78]  And what we're hoping to release in the upcoming months
[1514.78 --> 1518.48]  is an easy way to build web applications
[1518.48 --> 1521.56]  that have data displaying on the browser,
[1521.68 --> 1527.06]  which is updated all the time based on socket.io and server push,
[1527.60 --> 1529.02]  and of course, real-time.
[1529.02 --> 1533.46]  Aside from that, in general,
[1533.62 --> 1538.16]  I think it's interesting to watch all the Node.js-related projects,
[1538.38 --> 1540.42]  since Node makes it really easy to build
[1540.42 --> 1544.98]  this kind of real-time applications and modules.
[1545.66 --> 1546.30]  What about you, Martin?
[1546.86 --> 1550.72]  I think the thing that's really exciting me at the moment is Redis.
[1551.06 --> 1552.64]  All the projects I've worked on recently,
[1552.74 --> 1553.68]  I've used Redis in,
[1553.68 --> 1557.50]  and it's just incredibly liberating
[1557.50 --> 1562.44]  to have a really fast atomic data store
[1562.44 --> 1565.12]  that I can share between multiple processes.
[1566.88 --> 1568.56]  Another open source,
[1569.18 --> 1572.30]  I should mention that we're using EM WebSocket,
[1572.62 --> 1573.92]  which is a Ruby.
[1573.92 --> 1577.72]  If you're interested in a Ruby event machine client,
[1577.92 --> 1581.10]  then that's a great one to look at.
[1581.10 --> 1581.78]  Peter?
[1582.84 --> 1583.86]  A couple things.
[1584.72 --> 1588.78]  So the Node.js YUI-3 bindings are, I think, really exciting
[1588.78 --> 1593.84]  because they let you have this really rich set of tools
[1593.84 --> 1596.32]  that you can run both on browser and on the server.
[1596.78 --> 1598.42]  And for doing things that you would normally
[1598.42 --> 1599.94]  only really think about doing in a browser,
[1600.22 --> 1602.72]  like you can take these really complex web applications
[1602.72 --> 1603.82]  written in YUI
[1603.82 --> 1606.70]  and decide that you're going to render them statically on the server
[1606.70 --> 1608.90]  if the client has low bandwidth
[1608.90 --> 1610.78]  and you don't want to deal with downloading all the JavaScript
[1610.78 --> 1615.02]  or the client has a CPU that's not particularly strong,
[1615.20 --> 1617.00]  and so you just want to hand it some static HTML
[1617.00 --> 1618.26]  and make life really easy for it.
[1618.30 --> 1621.06]  So I think that provides a really kind of compelling platform
[1621.06 --> 1623.86]  for building user experiences
[1623.86 --> 1626.06]  that can handle a wide variety of clients.
[1626.76 --> 1629.26]  Another thing that I'm starting to watch
[1629.26 --> 1630.66]  and is actually really new
[1630.66 --> 1633.00]  and I think is an interesting fit for WebSockets
[1633.00 --> 1635.24]  is Telehash.
[1635.24 --> 1638.46]  This is Jeremy Miller, the creator of XMPP.
[1638.88 --> 1643.44]  This is his distributed JSON routing protocol.
[1643.86 --> 1646.04]  It's really, really early going right now.
[1646.18 --> 1647.82]  You know, there's only a basic protocol up
[1647.82 --> 1649.98]  and a couple of really kind of bare bones implementations,
[1650.12 --> 1652.76]  but it looks like a really kind of neat way
[1652.76 --> 1653.78]  of shooting around data.
[1654.48 --> 1655.12]  With all of these tools,
[1655.18 --> 1656.86]  do you think the application landscape
[1656.86 --> 1659.22]  for the web developers getting easier
[1659.22 --> 1660.32]  or more complicated?
[1660.32 --> 1662.96]  I mean, you know, some things are easier.
[1663.18 --> 1665.38]  You know, in some sense,
[1665.46 --> 1667.28]  the promise of WebSockets is
[1667.28 --> 1671.44]  it will become easy to build these real-time full duplex pipes,
[1671.72 --> 1674.00]  whereas now it is possible, but it is just hard.
[1675.20 --> 1679.72]  So, you know, there are, I guess, more choice.
[1679.82 --> 1681.84]  It does make things difficult to some extent,
[1682.02 --> 1684.86]  but, you know, with great power comes great responsibility.
[1685.86 --> 1687.54]  All right, thanks everyone for joining us today,
[1687.70 --> 1689.14]  and we'll see you in cyberspace.
[1689.14 --> 1719.12]  We'll see you in the next one.
[1719.14 --> 1721.14]  Whoo!
[1721.14 --> 1721.88]  Oh, man!
[1721.88 --> 1736.90]  oh
