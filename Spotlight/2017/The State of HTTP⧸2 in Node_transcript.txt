[0.52 --> 5.72]  Bandwidth for ChangeLog is provided by Fastly. Learn more at Fastly.com.
[7.18 --> 11.14]  You're listening to Spotlight, a show that takes place around big announcements,
[11.68 --> 15.12]  at conferences, in the hallways, and behind the scenes.
[15.50 --> 19.68]  It's about getting out and having meaningful conversations with real people in the community.
[20.26 --> 23.30]  It's ChangeLog in the trenches, shining our spotlight.
[30.00 --> 36.60]  Welcome to our Spotlight series titled The Future of Node, recorded at Node Interactive 2016 in Austin, Texas.
[36.92 --> 43.82]  We produce this in partnership with the Linux Foundation, the Node.js Foundation, and it's sponsored by IBM and StrongLoop.
[44.12 --> 49.96]  Check out IBM API Connect, a comprehensive solution to manage your entire API lifecycle from creation to management,
[50.32 --> 53.08]  at developer.ibm.com slash apiconnect.
[53.20 --> 58.38]  Also, check out Loopback from StrongLoop, a highly extensible, open-source Node.js framework
[58.38 --> 64.14]  that enables you to create dynamic, end-to-end REST APIs with little-to-no coding at loopback.io.
[64.40 --> 66.84]  In this episode, I talk with James Snell.
[67.20 --> 73.56]  James is a technical lead for Node at IBM and a member of Node's TSC and CTC.
[74.14 --> 79.30]  We talked about the work he's doing on Node's implementation of H2, the state of H2 in Node,
[79.60 --> 83.98]  what this new spec has to offer, and what the Node community can expect from this new protocol.
[84.36 --> 84.86]  Let's take a listen.
[84.86 --> 88.58]  So what's the state of H2 in Node?
[88.62 --> 90.04]  I know you're working on it now.
[90.20 --> 93.90]  You've recently tweeted about a prototype server.
[93.90 --> 99.32]  So the current state is just trying to figure out how it would work in Node.
[101.24 --> 104.96]  There's a lot of new things within H2.
[105.26 --> 110.12]  It's a brand-new protocol, even though it's got the HTTP semantics with the crest response headers
[110.12 --> 110.80]  and that kind of thing.
[110.80 --> 113.64]  On the wire, it's very, very different.
[113.92 --> 116.56]  So it requires a completely new implementation.
[117.16 --> 121.02]  So kind of teasing the edges of what that implementation would need to look like, how it would work,
[121.08 --> 127.56]  what the issues are, what the additional state management, what impact that's going to have on Node.
[128.06 --> 133.14]  It's trying to figure out what that impact is going to be.
[133.14 --> 137.44]  And then if we were going to put it in core, if it's something that was going to land there,
[137.60 --> 144.32]  what would that look like in terms of APIs and in terms of just kind of the performance profile and that kind of thing?
[144.44 --> 145.32]  So that's where we're at.
[145.86 --> 149.08]  We had a discussion earlier, Thomas Watson and Sam.
[149.18 --> 150.54]  I forget his last name from IBM.
[150.90 --> 151.18]  Roberts.
[151.40 --> 151.86]  Sam Roberts.
[151.98 --> 152.12]  Okay.
[152.16 --> 153.20]  Thank you for jogging my memory.
[153.20 --> 155.80]  And he wanted to talk.
[155.86 --> 158.72]  Sam was really passionate about talking about keeping Node small.
[158.96 --> 159.08]  Yeah.
[159.30 --> 163.74]  And Thomas actually coined, I don't know if it's him or not, but he coined the term small core.
[164.00 --> 164.28]  Right.
[164.68 --> 171.16]  And so one of the discussions we had in that conversation was what should or should not be in Node core.
[171.54 --> 176.60]  And so as you're developing H2, you've got to be thinking about H1 being there, whether it should stay there,
[176.60 --> 178.24]  if you did deprecate it, how you would do that.
[178.56 --> 183.04]  So end that argument between them because they didn't really come to a conclusion of what should happen.
[183.04 --> 186.10]  And do you think H2 should be in Node core or should it be a module?
[187.18 --> 188.84]  Personally, I think it should be in core.
[189.54 --> 194.30]  And the reason for that, Node has always been a platform for web development, right?
[194.46 --> 197.04]  You know, there's always been that web server.
[197.20 --> 199.84]  And that is, you know, it's a primary use case.
[199.96 --> 203.88]  Even though there's so many different places Node is being used and in different use cases,
[204.54 --> 206.80]  a lot of it always goes back to having Node.
[206.86 --> 208.92]  And if you look, there is no standard library in Node.
[209.42 --> 210.52]  But there's HTTP, right?
[210.58 --> 211.50]  There's URL parsing.
[211.50 --> 215.38]  There's support for these fundamental web protocols that are built in.
[215.48 --> 217.38]  And that's the only thing that's built in, right?
[217.64 --> 223.32]  Now, if HP1 wasn't already there, I wouldn't be thinking that we should add HP2, right?
[223.40 --> 224.12]  There's other...
[224.12 --> 224.78]  You'd be a module at that point.
[224.90 --> 225.42]  Right, right.
[225.44 --> 225.62]  Okay.
[225.84 --> 229.10]  There are other protocols that are becoming increasingly more important to the web.
[229.18 --> 230.64]  Web sockets, for instance, right?
[230.68 --> 232.08]  We don't have Web sockets support in there.
[232.12 --> 234.44]  And we shouldn't have it because it's not already there.
[235.20 --> 236.10]  Quick is another one.
[236.10 --> 241.72]  You know, it's a protocol that's, you know, starting to gain a lot of traction, you know, relative to TCP IP.
[241.98 --> 244.76]  It's got a long ways to go, but it's a very good protocol.
[245.34 --> 253.60]  But, you know, I wouldn't support any effort to actually get it into core unless it became much more fundamental to the web architecture, right?
[253.60 --> 258.78]  So, with HP2, the decision basically just comes to, we already have HP1, right?
[259.08 --> 262.44]  We know HP2 is going to continue in relevance, you know, grow in relevance.
[262.58 --> 266.38]  It is going to be, you know, we have a lot of people asking for it.
[267.08 --> 271.86]  It just makes a lot of sense to have it in core and have it available.
[271.86 --> 276.12]  We also talked about, and maybe you can even end this argument, too.
[276.18 --> 279.98]  We talked about how you define what should or shouldn't be in core.
[280.06 --> 286.26]  And it sounded like you said, maybe I'll answer this for you and you can agree or disagree, but it sounded like you said around web fundamentals.
[286.40 --> 289.56]  Like, if it's fundamental to doing web stuff, it makes sense to put in core.
[289.68 --> 295.98]  But what do you think about, you know, keeping node core small or what should, how to define what should or shouldn't be in node core?
[296.34 --> 299.98]  If it's not already there, then it shouldn't be there.
[300.08 --> 301.34]  It shouldn't be added, right?
[301.86 --> 305.76]  So, another example of this was URL parsing, right?
[305.86 --> 310.92]  You know, we have URL parse, but it's fundamentally broken in a number of important ways.
[311.10 --> 312.04]  You know, it's there.
[312.40 --> 314.46]  You know, it fundamentally works.
[315.08 --> 320.42]  But there's quite a few use cases where URL parse just doesn't function correctly.
[320.50 --> 323.14]  So, we added a new whatwg URL parser.
[323.42 --> 328.88]  You know, it's the same parsing API that you use in the browser for, you know, new URL and that kind of thing.
[328.88 --> 331.52]  So, now we have two URL parsers in core, right?
[331.52 --> 336.02]  And there was a big debate whether that should just go out as a separate module or, you know, does it belong in core?
[336.18 --> 338.48]  And that question's still not completely settled.
[338.78 --> 343.76]  The only reason that would be added to core is because URL parsing is already in core.
[343.96 --> 344.12]  Right.
[344.34 --> 344.58]  Right.
[344.58 --> 354.86]  And I think that is the key distinction that, you know, we're not adding something that's brand new that doesn't already exist as part of the platform.
[355.00 --> 357.30]  We're just evolving what's already there.
[357.84 --> 358.28]  Right.
[358.36 --> 360.90]  So, that's where I think we draw the line.
[360.90 --> 369.68]  So, for those who may not be as familiar as you might be with Node Core, what exactly makes up Node Core to make you say don't add more to it, just keep things in modules?
[369.68 --> 379.12]  So, the basic protocol supports, you have DNS, you have UDP, TCP, TLS, HP, right?
[379.46 --> 383.92]  These fundamentals of just basic web application programming, right?
[384.48 --> 386.12]  That is what core is to me.
[386.18 --> 387.88]  Now, there are things that are in support of that.
[388.02 --> 391.58]  You know, obviously, we have to have, you know, a file system I.O., right?
[391.58 --> 397.34]  We have to have an inventing system, buffer, right, for just basic data management.
[397.80 --> 405.82]  I view those as being more kind of utility capabilities, right, in support of the web platform capabilities that are there.
[406.72 --> 410.04]  To me, that is a large part of what Node is.
[410.16 --> 417.64]  And if you look at all the different use cases where Node is being used, those are still the fundamental things that are being used the most, right?
[417.64 --> 425.70]  You know, even if you look at Electron, you know, those are basically web applications, right, that are bundled into a native app, right?
[425.92 --> 426.00]  Right.
[427.30 --> 427.74]  Yeah.
[428.14 --> 433.72]  You cannot get away from those fundamental pieces of that basic protocol support.
[434.18 --> 436.26]  And that, to me, is what defines Node.
[436.78 --> 437.94]  It's almost what you said.
[438.26 --> 439.72]  I said you said, but you said it.
[439.82 --> 439.96]  Yeah.
[439.98 --> 440.52]  Web fundamentals.
[440.84 --> 441.44]  Web fundamentals, right.
[441.46 --> 443.28]  If it's around that, it belongs in core.
[443.54 --> 443.86]  Otherwise.
[444.36 --> 444.60]  Right.
[444.98 --> 446.68]  Otherwise, you know, put it out to the ecosystem, yeah.
[446.68 --> 449.06]  So, you're working on H2.
[450.18 --> 452.30]  What's interesting about H2 for the Node community?
[453.54 --> 456.80]  That it's actually a very different protocol than H1.
[457.58 --> 458.02]  Yeah.
[458.02 --> 464.08]  You know, it has the same name, but that, too, is really, really important.
[464.66 --> 469.68]  The fact that it uses a binary framing instead of a text framing, right, you know, and just line delimination.
[469.68 --> 485.56]  Stateful header compression is, you know, adds an interesting dimension of there's a whole lot more state management that has to occur over long-lived sockets that just doesn't exist currently in Node.
[485.56 --> 489.16]  And when you're dealing with, you know, with H1.
[489.16 --> 498.22]  You know, with the header compression and the multiplexing and stuff that the protocol enables, you can get much more efficient use of your connections.
[498.22 --> 513.34]  And when we start getting into the real-world benchmarks of, you know, like real applications rather than the peak load type benchmarks that I've been doing currently, I think we'll see much more efficient use of Node and of the connection there.
[513.34 --> 523.08]  But it does require a different way of thinking about your web applications, your web APIs, because you're not just pipelining individual requests one at a time.
[523.64 --> 531.44]  You can have, you know, the protocol provides no limits to the number of in-flight requests and responses you can have simultaneously over a single connection.
[532.14 --> 534.88]  And then you add things like push streams on top of that.
[534.88 --> 548.72]  It adds a significant new thing that you just have to consider of how you're building your applications and, you know, what the interaction is going to be with your, you know, in terms of performance and concurrency and all these things that you just don't currently have to deal with.
[549.60 --> 559.16]  So I think there's going to be a lot of just kind of coming to terms with the protocol and getting experience with the protocol and kind of figuring out what those best practices are.
[559.16 --> 565.06]  Because it's still a very young protocol, you know, and there's not a lot of industry best practice to draw from.
[565.70 --> 573.62]  So, you know, it's just kind of let's get it out there and get it in the hands of people to use and, you know, see how it evolves from there.
[574.34 --> 579.40]  I talked to Michael Rogers earlier about kind of the state of the union, so to speak, for Node.js.
[579.40 --> 587.40]  And he was coming at it from a direction and governance side, less of a code side.
[587.44 --> 592.30]  But one thing he said was a really important factor in this next year is security.
[592.90 --> 599.94]  And so how does H2 play into or the work you're doing on H2 support the overall mission of being more secure?
[600.28 --> 600.42]  Right.
[600.72 --> 602.82]  So there's two things there.
[602.82 --> 613.30]  With H1 in core right now, a number of design decisions were made early on to favor performance over spec compliance, right?
[614.92 --> 624.28]  It turns out that there are a number of compliance things in the spec that says, you know, don't allow white space in headers, right?
[624.28 --> 630.86]  And there's very good reasons for that because you get into, you know, requests smuggling and, you know, response splitting.
[631.08 --> 638.38]  And there's a lot of real specific security issues that come if you allow invalid characters into an H1 request.
[639.06 --> 641.96]  Node was like, yeah, you know, we want things to go fast.
[642.10 --> 643.28]  So we're not going to check this.
[643.36 --> 644.20]  We're not going to check that.
[644.20 --> 653.80]  And it was a very deliberate decision not to fully support the H1 spec.
[654.28 --> 662.36]  And what we found is that that caused a number of security issues that we've been dealing with, you know, over the past year or two years and stuff like that.
[664.44 --> 671.96]  With H2, we're going to be taking an approach where we're going to be very spec compliant, right?
[672.04 --> 674.40]  And we're not favoring performance over that.
[674.46 --> 676.22]  We're not sacrificing one or the other.
[677.06 --> 682.76]  It is going to be absolutely compliant to the specification without taking those kind of performance shortcuts.
[682.76 --> 697.62]  And that is something that I am emphasizing, you know, in my own development as I'm going through this, that making sure that we can, that we're hitting all of those, you know, you must do this or you must not do this that are fine in that specification.
[697.62 --> 707.62]  And I think by adhering to the spec as closely as we possibly can, we mitigate a lot of those potential security issues.
[707.62 --> 717.90]  The other important thing is that even though H2 does not require TLS, you know, per the spec, you can do plain text if you want.
[718.50 --> 733.84]  The browser implementations, the primary clients of H2 right now, you know, Chrome, Firefox, Safari, and some of the others, they require that they will only talk to H2 server over TLS, right?
[733.84 --> 734.64]  It's just mandated.
[734.80 --> 736.32]  They won't even connect to a plain text server.
[736.44 --> 742.26]  So automatically out of the gate, you're using, you know, secured connections.
[742.90 --> 746.16]  And that alone is going to be a significant improvement to security.
[746.94 --> 754.90]  The one kind of limiting factor there is Node hasn't really had a great reputation as a TLS terminator.
[755.84 --> 759.36]  A lot of people, it's just the best practice, put a proxy in front of it, right?
[759.36 --> 765.52]  And then they'll reverse proxy back over a plain text connection back to Node and just to ensure the performance.
[765.88 --> 770.94]  A lot of that has to do with the way the crypto works with the event loop and OpenSSL and that kind of thing.
[771.38 --> 774.90]  So I think a lot of work is going to need to go in to try to improve that.
[775.18 --> 781.82]  If we want to improve the performance of Node as a TLS endpoint and make that, you know, improve on that story.
[781.82 --> 788.62]  So what gets you most excited about H2 being available?
[789.14 --> 794.70]  I know you're working on things like you talked about the state of things, but what's the most exciting to you that's going to change things for it?
[795.42 --> 801.54]  Just seeing the getting into the hands of developers and seeing what they do with it, right?
[802.52 --> 804.76]  It is a very young protocol, right?
[804.76 --> 807.00]  It is brand new and I have my issues with it.
[807.00 --> 813.08]  I was actually involved with, you know, the working group for a while that was actually creating it and I was one of the co-editors on the draft.
[813.20 --> 817.46]  So it was early on, you know, you know, had, you know, some interest in where it could go.
[818.26 --> 819.74]  Then I got out of it for a little while.
[819.84 --> 824.52]  I had some issues with how it was designed and I'm not completely happy with the protocol by any stretch.
[824.62 --> 826.26]  I do have my issues with it.
[827.22 --> 829.56]  But I want to see what developers do with it, right?
[829.56 --> 837.58]  And I love seeing all the different ways that people are using Node today in ways we didn't even imagine that, you know, that they could or would or anything else.
[838.28 --> 851.96]  And I want to see that also with the protocol, just the experimentation and just the all the different new types of applications that could be, you know, that could be developed or all the different ways that it could be innovated on and built on.
[851.96 --> 856.16]  Any ideas, any pontification you could do on what could be built?
[856.38 --> 861.94]  There are all kinds of opportunities for more interesting RESTful APIs.
[862.22 --> 869.48]  You know, push streams are something that are really interesting.
[869.62 --> 874.00]  And so far they've only really been looked at as a way of pre-populating a request cache, right?
[874.10 --> 876.94]  You know, I'm going to push it out so you don't have to do it.
[876.94 --> 892.62]  But I think with REST APIs, push streams offer some really interesting opportunities for new kinds of APIs that are providing, you know, event notifications or, you know, the servers more proactively pushing data to the client.
[892.62 --> 909.00]  One person I was talking to and one of the ways that they were kind of prototyping stuff and, you know, using H2 is they have they would create a tunnel using over an H2 connection where they would, you know, open the connection with their client.
[909.00 --> 919.60]  But then once the connection was established, they would switch roles, right, and allow the server to act as the client, you know, to the server, you know, and the client was acting as the server.
[919.72 --> 925.78]  And they were doing this as a way of doing testing over their network environment.
[925.78 --> 930.50]  That kind of thing, you can't do that with H1, right?
[930.60 --> 940.54]  But because of the, you know, the multiplexing and, you know, the communication model that exists in H2, that kind of stuff is allowed, right?
[940.56 --> 941.38]  It's something you can do.
[942.60 --> 952.64]  H2 is going to enable new extensibility models, kind of new possibilities for new kinds of protocols that kind of coexist with H2P semantics.
[952.64 --> 955.68]  And we already see some of that work already happening within the working group.
[955.84 --> 960.54]  There's proposals for other kinds of protocols that are layered into the mix.
[962.44 --> 965.16]  And, you know, you kind of wonder, well, you know, who would do that kind of thing?
[965.22 --> 966.52]  Well, look at WebSockets, right?
[966.80 --> 975.90]  Look how WebSockets emerged and, you know, its relationship with H1 and kind of the difficulties that existed trying to get those two things to work together, right?
[975.90 --> 988.72]  With this, the framing model is going to allow you to more naturally experiment with those kinds of new protocols without the pain that we had with, you know, trying to introduce WebSockets into it.
[988.80 --> 993.92]  So there's a lot of new types of innovations, I think, that could come out of it.
[993.96 --> 999.40]  But we need to build a kind of a collective experience working with it in order to be able to tease those things out.
[999.40 --> 1003.54]  You mentioned some things you're not happy with with the H2P protocol.
[1003.64 --> 1006.12]  I couldn't let you not tell me what those are.
[1006.42 --> 1008.52]  So what are the gotchas?
[1008.62 --> 1010.74]  What are the things that are just bugging you about this protocol?
[1013.00 --> 1014.06]  Staple header compression.
[1016.02 --> 1017.74]  It's very effective, right?
[1017.88 --> 1023.90]  You get some, you know, in terms of headers in H2P are very repetitive.
[1023.90 --> 1032.22]  You know, you're sending the same data over and over and over again, you know, cookies or, you know, user agent strings, you know, all these kinds of things.
[1032.32 --> 1037.98]  And when it comes to actually what's transmitted over the wire, it's a lot of waste, like a date, right?
[1038.24 --> 1041.92]  And each one is 29 bytes because it's encoded as a string.
[1042.62 --> 1050.46]  You know, that can be, like, more compactly encoded as just a couple of bytes if you're using a more efficient encoding, right?
[1050.46 --> 1053.52]  So it's very, very wasteful as it exists today.
[1054.94 --> 1061.92]  HPAC, which is the stateful header compression protocol in H2, uses this state table that's maintained at both ends.
[1062.34 --> 1064.02]  There is actually two in each direction.
[1064.20 --> 1066.80]  So the sender has two, the receiver has two.
[1067.94 --> 1072.38]  And it, you know, the receiver gets to say how much state is actually stored.
[1072.52 --> 1075.82]  The sender gets to say what's actually stored in that table.
[1075.82 --> 1083.36]  But for the entire life of the connection of that socket, however long that socket is kept open, you have to maintain the state, right?
[1083.76 --> 1085.86]  And that doesn't exist in H1 today.
[1085.96 --> 1088.10]  H1 is a completely stateless protocol.
[1089.06 --> 1093.08]  So H2 switches that and makes it where you have to maintain state.
[1093.32 --> 1098.26]  You have to maintain this server affinity, right, over a long-lived connection.
[1098.26 --> 1112.74]  And even though you're multiplexing multiple requests in flight at the same time, you have to process those headers sequentially and serialize the access to those things.
[1113.56 --> 1117.60]  Because if that state table gets out of sync at any point, you just tear down the connection.
[1117.78 --> 1119.94]  You can't do anything else on it.
[1119.94 --> 1128.20]  And even over multiplex requests, you know, all of those requests and responses share the same state tables.
[1128.86 --> 1133.86]  So it adds an additional layer of complexity that just didn't exist previously.
[1133.86 --> 1134.06]  Wasn't there before.
[1135.18 --> 1138.86]  And personally, I don't think it was needed, right?
[1138.90 --> 1140.12]  I think that there were other ways.
[1140.12 --> 1140.32]  You could have done differently.
[1140.32 --> 1144.90]  I actually, you know, like I said, I worked on the spec.
[1145.08 --> 1145.24]  Right.
[1145.24 --> 1145.92]  I was one of the co-authors.
[1146.10 --> 1154.94]  And I had a proposal for just using a more efficient binary encoding, you know, of certain headers like dates, right?
[1155.00 --> 1160.82]  Or instead of, you know, representing numbers as text, representing them, you know, is binary, right?
[1160.82 --> 1160.86]  Right.
[1162.98 --> 1172.24]  The compression ratios weren't as good, but you could transmit that data without incurring the cost of managing the state, right?
[1172.26 --> 1178.76]  So it would be just like what H1 has today where you're still sending it every time, but you're sending less every time.
[1179.96 --> 1181.60]  Makes sense to shrink it rather than...
[1181.60 --> 1181.82]  Right.
[1181.94 --> 1182.76]  Shrink it, yeah.
[1183.06 --> 1183.80]  Rather than adding the state.
[1183.80 --> 1188.56]  I kind of agree with you on the state because it seems like it's adding this extra layer of like...
[1188.56 --> 1188.74]  Right.
[1189.10 --> 1191.72]  It's almost like somebody shakes your hand and doesn't let it go.
[1192.04 --> 1192.56]  Well, yeah.
[1192.66 --> 1194.44]  And in a lot of ways, that's exactly what it is.
[1194.96 --> 1199.74]  Now, Google has a ton of experience with Speedy, right?
[1199.74 --> 1205.20]  And, you know, a lot of what's in HP2 came out of the experience, you know, came out of the work that Google did on Speedy.
[1205.38 --> 1209.28]  And I have a huge amount of respect for everything that they did and provided.
[1210.12 --> 1211.86]  HPAC also came out of Google.
[1211.86 --> 1217.22]  So they did a ton of research in terms of what would work, right?
[1217.32 --> 1224.00]  And they had concluded that state-bore hydrocompression was the only way to get the, you know, like real benefits out of H2.
[1225.04 --> 1227.30]  You know, I disagreed with some of those conclusions.
[1227.56 --> 1231.06]  But, you know, the working group decided, you know what, this is what we're going to move forward with.
[1231.10 --> 1232.40]  And that's what they did.
[1232.54 --> 1234.76]  And at this point, it's like, I don't like it.
[1235.36 --> 1237.52]  But, you know, that's what it is.
[1237.78 --> 1240.12]  And, you know, that's what we're moving forward on.
[1240.12 --> 1250.58]  So some of the other things there, in terms of, like, additional complexity, is H2 has its own flow control, has its own prioritization.
[1250.80 --> 1253.04]  You can have streams depend on other streams.
[1253.14 --> 1257.30]  And when you set the priority on one, it, you know, sets the priority for the entire graph.
[1257.30 --> 1263.96]  You know, it's, you know, there's just a lot there that just doesn't exist in H1, right?
[1264.10 --> 1268.24]  That, you know, how much of that do we expose to developers, right?
[1268.34 --> 1269.30]  Like, you know, in Node.
[1269.48 --> 1271.22]  We have to provide an API for all this stuff.
[1271.66 --> 1273.30]  Do we provide an API for flow control?
[1273.90 --> 1275.74]  That doesn't exist in Node currently, right?
[1275.88 --> 1277.96]  I mean, how would we even do that in a way that's efficient?
[1278.82 --> 1282.06]  About prioritization, how do we, you know, what kind of APIs do we do there?
[1282.06 --> 1293.28]  This additional complexity is something that, as Node core looking at this, we have to decide how much of that do we pass on to the user versus how much of that do we do ourselves.
[1293.66 --> 1301.18]  If we do it all ourselves, we're providing fewer knobs for, you know, the users to turn, to tune things.
[1301.56 --> 1305.68]  And we're making it less interesting for them because we're hiding some of those features.
[1305.88 --> 1306.92]  We're hiding those capabilities.
[1306.92 --> 1310.16]  And is that the right thing to do, right?
[1310.30 --> 1316.34]  So the additional complexity kind of, you know, it's not something we can easily deal with.
[1316.42 --> 1317.92]  It's something we have to kind of.
[1318.54 --> 1319.34]  It's right there in your face.
[1319.34 --> 1320.28]  Right there in your face.
[1320.44 --> 1321.42]  You have to do something about it.
[1321.98 --> 1326.20]  So stateless compression, that's one thing.
[1328.10 --> 1329.58]  Maybe give me the flip side of that.
[1329.58 --> 1336.46]  Like what's, I guess you've already kind of described it to a bit with the complexity, but what's the worst that could happen?
[1336.46 --> 1341.00]  The server affinity issue is actually the biggest issue here.
[1342.00 --> 1349.70]  A lot of the proxy software vendors had some real significant problems with H2 as it was being defined.
[1350.08 --> 1353.88]  And you had a lot of criticism being put forth.
[1354.22 --> 1359.44]  I can't remember his name, but the author of, I believe it's the Varnish Proxy is very public.
[1359.44 --> 1359.66]  Yeah.
[1360.30 --> 1362.78]  And his discontent with the protocol.
[1363.82 --> 1370.28]  Because of the binary framing and the way the headers are actually, you know, transmitted, right?
[1370.28 --> 1381.14]  You can't do what a lot of the proxies do currently, which is just kind of read the first few lines, determine, you know, where you're going to route that thing to, then stop and just forward it on.
[1381.34 --> 1381.60]  Right?
[1382.22 --> 1385.28]  Which is a super efficient way of doing it.
[1385.28 --> 1388.96]  You have to process the entire block of headers, right?
[1389.04 --> 1392.10]  Then make the determination of whether you're going to do anything with it or not.
[1392.20 --> 1398.52]  At that point, you basically have to terminate that connection and open another connection, you know, to your backend.
[1398.86 --> 1403.72]  And you have, so that proxy is actually having four state tables for compression.
[1403.72 --> 1411.98]  And then a lot more stuff that they're having to do that that existing proxy middleware currently doesn't have to do, right?
[1412.32 --> 1413.86]  So, you know.
[1414.12 --> 1415.16]  I can see why you're against it.
[1415.54 --> 1416.70]  Well, you know, it's.
[1417.26 --> 1418.00]  It could have just gone the other way.
[1418.10 --> 1419.96]  It would just shrunk it instead of.
[1420.50 --> 1422.52]  It's not the same thing back and forth, but just shrink it.
[1422.86 --> 1425.68]  It added, you know, it added a lot of complexity.
[1426.40 --> 1427.92]  What are the plus sides of this complexity?
[1428.08 --> 1430.68]  Like, you're talking about the bad side, but what's the performance?
[1431.24 --> 1431.60]  Performance.
[1431.60 --> 1435.02]  It's using that socket much more efficiently.
[1436.10 --> 1443.40]  You know, I was doing a peak load benchmark here the other day with, you know, just a development image of H2 in core.
[1444.18 --> 1446.92]  I was serving 100,000 requests at the server.
[1447.48 --> 1451.88]  There was 50 concurrent clients going over eight threads, right?
[1451.96 --> 1456.20]  So just as much, just throw a bunch of stuff at the server and see what happens, right?
[1456.22 --> 1457.46]  See how quickly it can respond.
[1457.46 --> 1465.16]  With the H1 implementation in core currently, I was able to get 21,000 requests per second doing that.
[1465.44 --> 1468.18]  But 15% of them just failed, right?
[1468.28 --> 1470.88]  Where Node just didn't respond, right?
[1470.88 --> 1474.58]  And a lot of that has to do with, I was running a test on OSX.
[1474.68 --> 1479.22]  There's some issues there with assigning threads, you know, how quickly can assign threads.
[1479.52 --> 1484.48]  And, you know, when we get an extreme high load, you can run into some issues.
[1485.30 --> 1488.90]  With H2, I was able to get 18,000 requests per second.
[1488.90 --> 1492.94]  And so fewer transaction rate, but 100% of them succeeded, right?
[1493.40 --> 1496.18]  And it was using fewer sockets.
[1496.36 --> 1497.46]  Now, it was keeping them open longer.
[1498.16 --> 1502.08]  The downside of that was it was using significantly more memory, right?
[1502.34 --> 1506.46]  But it had a better success rate, right?
[1506.48 --> 1511.24]  And it was using the bandwidth much more efficiently.
[1511.24 --> 1520.60]  And the header compression, for example, we were able to save 96% of the header bytes, you know, compared to H1, right?
[1520.78 --> 1528.92]  So, you know, actually it's 96% fewer header bytes sent over the wire with 100,000 requests.
[1529.38 --> 1531.20]  That's a massive savings, right?
[1531.38 --> 1540.40]  And if you're looking at the platform as a service where people are paying for bandwidth, you know, paying for this stuff, saving that much is significant.
[1540.40 --> 1540.90]  A lot of money.
[1541.06 --> 1541.26]  Right.
[1541.82 --> 1542.96]  They'll spend that money in memory, though.
[1543.20 --> 1543.94]  Yeah, yeah, yeah.
[1544.68 --> 1546.28]  They'll make up for it in other ways.
[1547.26 --> 1552.12]  And, you know, that increase in performance is significant.
[1552.24 --> 1553.20]  You can't discount it.
[1553.56 --> 1558.76]  There is, with the fact that TLS is there, it's required, there is an improvement in security.
[1559.24 --> 1561.00]  But there are definite trade-offs.
[1561.30 --> 1566.86]  And anyone looking to adopt H2 has to be aware of what those trade-offs are.
[1566.86 --> 1576.14]  And it's something that, as we're going through in core, trying to figure this thing out, there's also going to be trade-offs in terms of API, right?
[1577.56 --> 1589.84]  And one, like, simple example is the fact that the status message in H1, you know, how you have, like, the preamble on a response, HP, you know, 1.1, 200, OK.
[1589.84 --> 1594.00]  That OK doesn't exist in H2.
[1594.74 --> 1597.58]  They completely remove the status message, right?
[1597.66 --> 1600.02]  So no more 404 not found.
[1600.16 --> 1602.08]  It's just 404, right?
[1602.28 --> 1604.04]  No more 500 server error.
[1604.38 --> 1605.72]  There's no server error, right?
[1606.04 --> 1607.62]  There is no standard way.
[1607.70 --> 1608.18]  Just the number.
[1608.42 --> 1608.54]  Yeah.
[1608.78 --> 1611.20]  There's no standard way of conveying the status message.
[1611.64 --> 1613.36]  They just completely removed it from the protocol.
[1613.36 --> 1621.92]  Well, there are existing applications out there that use the status message, right, and actually put content there that the clients read.
[1622.26 --> 1624.18]  Now, it's not recommended, right?
[1624.30 --> 1634.30]  And H1 spec, you know, doesn't assign any semantics, reliable semantics, that anyone should use to, like, say, hey, that's a thing we should use.
[1634.74 --> 1638.40]  But as users do, they'll use whatever's available to them, right?
[1638.40 --> 1641.66]  That's a bummer because people will stop saying 200, OK, now they'll just say 200.
[1641.66 --> 1642.92]  They'll say 200, right, right.
[1642.92 --> 1645.24]  The 404 not found, the whole jokes, you know.
[1645.44 --> 1645.62]  Right, right.
[1645.70 --> 1646.60]  Nobody will get it anymore.
[1647.84 --> 1655.52]  So if you look at nodes API or things like Express, you know, they have, like, you know, here's how you set the status message.
[1656.22 --> 1660.26]  Well, that's a breaking change in those APIs when you go to H2.
[1660.26 --> 1673.82]  So we have to make a decision of how closely does the H2 API have to match the H1 API and act the same way when we know that there are distinct differences that mean it can't.
[1673.82 --> 1678.32]  So it makes upgrading or changing to H2 a very deliberate choice.
[1678.50 --> 1678.56]  Yeah.
[1679.20 --> 1680.58]  It's going to have to be very deliberate.
[1680.92 --> 1687.80]  And it's only going to be in very simple, simple scenarios, which probably aren't realistic, that somebody would be able to say, OK, it works in both.
[1688.24 --> 1688.50]  Right.
[1688.50 --> 1696.88]  It's going to be a thing where you have to design your application specifically for H2 in order to take advantage of the capabilities of the event.
[1696.88 --> 1698.28]  It's kind of putting a high barrier in front of it, too.
[1698.36 --> 1707.46]  I mean, you can't expect adoption of what is, as you said, a better performing protocol if you put a mountain in front of it.
[1707.56 --> 1707.76]  Right.
[1708.08 --> 1708.24]  Right.
[1708.24 --> 1710.26]  No one's going to want to climb that.
[1710.64 --> 1715.48]  Or it's less enjoyable or less likely or whatever.
[1715.62 --> 1716.46]  People do it.
[1716.66 --> 1719.04]  We have lots of people that say they really want this.
[1719.20 --> 1720.34]  They really want H2.
[1720.52 --> 1726.38]  And we have a lot of people that are talking about it not necessarily for user-facing, right?
[1726.58 --> 1729.42]  Setting up websites that anyone on the Internet can access.
[1729.42 --> 1738.98]  They want to put it in their data center and have server-to-server communication be much more efficient, which is a huge use case for H2.
[1739.46 --> 1750.54]  Especially since that is within protected environments and you have more control over what the client and a server, there's opportunities there where you don't have to necessarily worry about TLS.
[1750.76 --> 1755.20]  You can do a plain text connection and you'll get far greater performance out of it.
[1755.68 --> 1757.56]  But, again, it has to be a very deliberate choice.
[1757.56 --> 1758.28]  Right.
[1758.68 --> 1763.02]  So H2, is this something that you're solely working on or do you have a team working on it with you?
[1764.14 --> 1766.04]  Right now, it's been primarily myself.
[1766.18 --> 1768.56]  I'm working on kind of growing that team of contributors.
[1769.34 --> 1771.40]  Is it in IBM or is it open source contributors?
[1771.46 --> 1772.32]  It's open source.
[1772.48 --> 1775.42]  I'm doing everything out in the open out on the GitHub repo.
[1775.42 --> 1776.32]  Is it on your user then?
[1777.00 --> 1779.04]  We're doing it under the Node organization.
[1779.36 --> 1786.50]  So if you go github.com, node.js, slash HTTP2, all the work's being done there.
[1786.50 --> 1789.46]  I saw that repo there, but I saw Ryan Dahl in there.
[1789.60 --> 1790.66]  So this is not a new repo?
[1791.16 --> 1794.42]  So it's a clone of the Node core.
[1794.66 --> 1794.84]  Okay.
[1794.84 --> 1794.98]  Right?
[1795.12 --> 1799.92]  So even though the decision hasn't been made to get it into core yet.
[1799.98 --> 1800.24]  Right.
[1800.34 --> 1801.36]  You're assuming it is.
[1801.36 --> 1802.80]  Assuming it is and developing it this.
[1803.04 --> 1803.46]  I'm falling.
[1803.46 --> 1804.38]  I was wondering why.
[1804.48 --> 1806.14]  I was like, I expected it to be a module.
[1806.86 --> 1807.84]  But then again.
[1807.94 --> 1815.28]  Well, it's being implemented in such a way that we could easily extract it out as a native module if we needed to, if that decision was made.
[1815.62 --> 1815.72]  Right.
[1816.12 --> 1818.62]  It doesn't, I think, I can't say it doesn't use any.
[1818.62 --> 1820.96]  With all this change, wouldn't it make sense just to cut the cord?
[1820.96 --> 1827.56]  And, you know, one thing Thomas and Sam were talking about was verbally and documentation-wise deprecate it.
[1827.62 --> 1833.12]  Don't do anything to the way it responds or, you know, using anything within Node core.
[1833.40 --> 1835.42]  Why not just verbally deprecate it and then?
[1835.60 --> 1838.20]  It's way too early for us to do that.
[1839.08 --> 1842.24]  AH2 is a very immature protocol.
[1842.24 --> 1842.76]  Right.
[1843.48 --> 1845.50]  It still has to be proven.
[1845.86 --> 1849.26]  And the vast majority of the web is still driven by H1.
[1851.38 --> 1856.68]  Going out there and saying that, okay, we're going to deprecate this when H2 has not yet been proven.
[1857.00 --> 1857.30]  Right.
[1857.48 --> 1859.94]  Would be, you know, very premature.
[1860.14 --> 1860.98]  So what do you do then?
[1861.00 --> 1862.24]  You just offer both?
[1862.42 --> 1862.78]  Both.
[1862.94 --> 1863.10]  Yeah.
[1863.42 --> 1863.62]  Yeah.
[1863.68 --> 1868.58]  And just say that, you know, Node is going to be a platform for HTTP development.
[1868.92 --> 1869.10]  Right.
[1869.20 --> 1869.72]  One and two.
[1870.16 --> 1870.40]  Right.
[1870.40 --> 1877.76]  And there will be mechanism that's built into the H2 specification that you can actually run H1 and H2 on the same port.
[1878.46 --> 1880.40]  You know, you can have a server that will offer both.
[1880.58 --> 1883.34]  And the client negotiates which one they want to use per socket.
[1884.28 --> 1888.12]  We're not quite there yet in terms of how we're going to figure out how to make that work in Node.
[1888.22 --> 1893.04]  But, you know, that's a key capability of H2.
[1893.04 --> 1902.16]  So if we are going to fully implement that spec, that means also implementing that upgrade path, which means we can't necessarily get rid of H1.
[1902.40 --> 1902.56]  Yeah.
[1902.56 --> 1905.76]  And the fact of the matter is we can't get rid of anything in core.
[1906.16 --> 1906.32]  Right.
[1906.44 --> 1911.88]  I mean, you see that, you know, in things like the recent buffer discussions, whether we deprecate, you know, things.
[1911.88 --> 1923.04]  We just we can't get rid of things that are that are so critical to what the Node ecosystem is doing that even having a deprecation message in there is problematic.
[1923.04 --> 1923.48]  Yeah.
[1924.00 --> 1930.28]  And something so fundamental as H1, I don't think we would ever get to a point where we would fully deprecate.
[1930.82 --> 1947.34]  I'll retract that deprecation statement and say it more like instead, because when we were having that discussion about the options of deprecating things was not to put it in where it was a response, but more so in like documentation where it was frowned upon.
[1947.66 --> 1949.46]  You know, it wasn't forced.
[1949.46 --> 1952.90]  And then you're obviously so much more closer.
[1952.98 --> 1954.60]  So I'm just outside of looking in.
[1954.70 --> 1960.38]  But I'm thinking, like, if it's so deliberate to choose it, wouldn't it make sense or potentially make sense?
[1960.44 --> 1964.90]  And this would be a decision you will eventually make to offer it as a module instead.
[1965.16 --> 1968.64]  That way you can have a clean break when it is time to move over.
[1968.78 --> 1972.58]  I'm just thinking if it's that deliberate, why not make it that deliberate where it's actually a require?
[1972.58 --> 1976.74]  Well, I mean, it's a legitimate, you know, it's a legitimate question.
[1976.74 --> 1980.72]  And that's actually one of the decisions the CTC has to make.
[1980.86 --> 1983.52]  You know, I have an opinion on it.
[1983.90 --> 1988.96]  But, you know, unfortunately, it's not just all up to me.
[1989.60 --> 1990.02]  Right.
[1990.10 --> 1997.22]  We have to listen to, you know, folks like Sam and Thomas and the ecosystem and figure out what is the right approach to take.
[1997.22 --> 2002.70]  And we're not close enough yet to reaching that decision.
[2003.08 --> 2003.28]  Right.
[2003.34 --> 2014.32]  So I'm being very deliberate in how I write this code to ensure that if we need to pull it out, if that ends up being the right thing to do, we can.
[2015.44 --> 2018.92]  You know, it's not making breaking changes to any existing part of node.
[2018.92 --> 2024.58]  It is a very distinct separate code path from the existing H1 stuff.
[2026.04 --> 2032.66]  You know, it would be a native module, you know, and all the things that come along with native modules, you know, so we'd have, you know, there would be some considerations there.
[2032.88 --> 2033.06]  Right.
[2033.24 --> 2035.54]  But if we needed to, we could.
[2035.54 --> 2042.16]  And, you know, like I said, I have my opinion on what it ultimately should do, but it's up to the community.
[2042.34 --> 2048.94]  It's up to, you know, the core team to make that decision for whatever reasons they want to make that decision.
[2050.36 --> 2050.76]  Cool.
[2050.84 --> 2055.02]  Let's close with any closing thoughts you might have on this subject.
[2055.12 --> 2059.34]  Anything I might not have asked you that you're like, I got to put this out there before we close down.
[2059.50 --> 2062.54]  Oh, you know, we've really covered, you know, a lot of it.
[2062.54 --> 2070.94]  I mean, kind of the big thing I would say is, you know, if the folks are really passionate about this, we need to hear from users.
[2071.08 --> 2080.02]  We need to hear from folks that, you know, that, you know, have ideas on how to implement it, right, or how to test or what kind of applications they want to build with this thing.
[2080.48 --> 2084.78]  I've had a lot of conversations so far, but, you know, it's a big ecosystem.
[2085.00 --> 2086.30]  There's a lot of people out there.
[2086.30 --> 2086.60]  Right.
[2086.60 --> 2092.72]  You know, so, you know, we can't have enough input on that direction.
[2093.28 --> 2101.92]  That information, that input is what's going to help drive that decision of what's going to happen with this code, right?
[2102.52 --> 2104.22]  What's the best way for people to reach out to you then?
[2104.32 --> 2106.34]  Like, if it's feedback you want, is it you personally?
[2106.52 --> 2107.82]  Is it, should they go to the repo?
[2107.82 --> 2109.04]  Go to the repo.
[2109.14 --> 2109.66]  Go to the repo.
[2109.80 --> 2113.94]  Open issues, you know, for the folks that really want to, like, you know, get in there.
[2114.06 --> 2115.42]  You know, pull requests are great.
[2116.16 --> 2118.52]  I've been making, there's been a lot of churn in the code.
[2118.62 --> 2121.84]  I've been getting in there and just, like, you know, hammering away at it for the past few weeks.
[2121.96 --> 2122.42]  With the machete?
[2122.84 --> 2123.54]  Yeah, pretty much.
[2124.00 --> 2127.36]  People have been asking, you know, it's like, well, where are the two do so we know where to jump in?
[2127.40 --> 2132.74]  It's like, well, I don't even know what the heck I'm going to do tomorrow, let alone what they recommend you jump in on.
[2133.20 --> 2136.06]  But, you know, it's starting to stabilize more.
[2136.06 --> 2143.02]  And there are very distinct areas that I know for sure, you know, tests, performance benchmarks, you know, those kinds of things.
[2143.16 --> 2143.34]  Right.
[2143.48 --> 2147.20]  That, you know, absolutely could use some help on.
[2147.94 --> 2151.04]  So anyone that wants to jump in, just go to that repo.
[2151.26 --> 2152.16]  Take a look at what's happening.
[2152.16 --> 2153.06]  Testing performance, things like that.
[2153.12 --> 2153.36]  Right.
[2153.52 --> 2153.76]  Okay.
[2153.76 --> 2157.56]  Well, we'll link up the repo in the show notes for this.
[2157.86 --> 2163.38]  And, James, thanks so much for, we're closing down, literally closing down Node Interactive.
[2163.66 --> 2163.76]  Oh, yeah.
[2164.26 --> 2166.48]  So thank you so much for taking the time to speak with me.
[2166.86 --> 2167.16]  Oh, yeah.
[2167.16 --> 2168.46]  It's important that we have this conversation.
[2168.62 --> 2171.94]  So I know that the Node community is going to appreciate what you have to say.
[2172.12 --> 2172.44]  Right on.
[2172.60 --> 2172.82]  Right on.
[2172.88 --> 2173.28]  Thanks, man.
[2173.44 --> 2173.66]  Thanks.
[2176.16 --> 2181.90]  Thanks again to our friends at the Linux Foundation and the Node Foundation for working with us on this project,
[2181.90 --> 2185.94]  as well as our friends at IBM and Strongloop for sponsoring this podcast series.
[2186.26 --> 2187.44]  It was a blast being there.
[2187.70 --> 2188.88]  We'll be there again next year.
[2188.94 --> 2192.16]  So look out for us in 2017 at Node Interactive.
[2192.54 --> 2196.94]  If you want to hear more JavaScript-focused podcasts from Changelog, check out JS Party,
[2197.18 --> 2202.54]  our new live weekly show with Michael Rogers, Alex Sexton, and Rachel White.
[2202.94 --> 2205.38]  Head to changelog.com slash JS Party.
[2205.78 --> 2206.40]  Click subscribe.
[2206.96 --> 2207.78]  Don't miss the show.
[2208.38 --> 2209.20]  And thanks for listening.
[2211.90 --> 2211.96]  And thanks.
[2215.22 --> 2220.42] 問 you.
[2220.82 --> 2221.04]  We'll see you next time in the就 intangable episode.
[2221.06 --> 2221.56]  Bye.
[2221.56 --> 2221.66]  Bye.
[2221.66 --> 2221.72]  Bye.
[2221.84 --> 2221.96]  Bye.
[2222.04 --> 2223.78]  Bye.
[2223.78 --> 2224.10]  Bye.
[2224.16 --> 2224.42]  Bye.
[2224.62 --> 2225.14]  Bye.
[2225.16 --> 2225.64]  Bye.
[2225.96 --> 2226.62]  Bye.
[2226.62 --> 2227.12]  Bye.
[2227.20 --> 2228.08]  Bye.
[2228.08 --> 2228.68]  Bye.
[2228.68 --> 2229.06]  Bye.
[2229.14 --> 2230.14]  Bye.
[2230.34 --> 2230.78]  Bye.
[2230.98 --> 2232.56]  Bye.
[2232.68 --> 2232.70]  Bye.
[2232.82 --> 2234.66]  Bye.
[2234.66 --> 2235.24]  Bye.
[2235.60 --> 2236.68]  Bye.
[2237.08 --> 2237.24]  Bye.
[2238.14 --> 2238.66]  Bye.
[2238.86 --> 2239.16]  Bye.
[2239.16 --> 2241.76]  Bye.
