[0.16 --> 7.38]  Hey, welcome back. You are listening to the Change Law. We feature the hackers, the leaders, and the innovators in the world of software.
[7.86 --> 18.80]  Today, we're joined by Ryan Dahl, Node.js creator, and now the creator of Dino, a simple, modern, and secure runtime for JavaScript and TypeScript that uses V8 and is built in Rust.
[19.10 --> 26.78]  We talk with Ryan about the massive success of Node and how it impacted his life, how he eventually created Dino, and what he's doing differently this time around.
[26.78 --> 30.42]  We also talk about the Dino company and what's in store for Dino Deploy.
[30.88 --> 33.98]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[34.20 --> 39.36]  We love Linode. They keep it fast and simple. Check them out at linode.com slash changelog.
[39.68 --> 43.94]  Our bandwidth is provided by Fastly. Learn more at fastly.com.
[44.22 --> 48.44]  And get your feature flags powered by LaunchDarkly. Get a demo at launchdarkly.com.
[48.44 --> 60.94]  This episode is brought to you by our friends at Influx Data and their upcoming IoT application training.
[60.94 --> 66.64]  You'll build a fully functional sample application called IoT Center and build it on InfluxDB.
[67.12 --> 71.64]  With functions such as the new IoT device registration and IoT device emulation,
[71.64 --> 76.02]  this demo app is based on Node.js and React, uses Kafka to write measurements,
[76.42 --> 79.78]  and requires no dB installation with InfluxDB Cloud.
[80.22 --> 86.60]  Space is limited and it's free to join, so register now at influxdata.com slash changelog to save your spot.
[87.02 --> 90.38]  Again, that's influxdata.com slash changelog.
[90.38 --> 110.62]  Hello, we're here with Ryan Dahl, creator of Node, creator of Dino.
[110.84 --> 114.08]  Ryan, we're big fans of you, and we're so happy that you're here on the show.
[114.58 --> 115.92]  Hello. Glad to be here.
[116.22 --> 117.12]  I think this is a first.
[117.76 --> 118.12]  Yes.
[118.12 --> 121.16]  You've never been on the changelog before, like right, even back in the day.
[121.50 --> 121.70]  Nope.
[122.10 --> 122.30]  Never.
[122.38 --> 125.10]  We've only talked about Node, not about the creator of Node.
[125.44 --> 128.88]  Yeah, we've talked about Node, but we haven't talked about the creator of Node.
[129.30 --> 130.72]  What a shame. Here we are to fix that.
[131.14 --> 133.26]  Well, 10 years later, or ish.
[134.10 --> 134.46]  Welcome.
[134.92 --> 135.24]  Thank you.
[135.64 --> 139.10]  Yeah, I think this is only the second podcast ever I've done.
[139.50 --> 139.82]  Oh, wow.
[140.10 --> 142.76]  Is that right? Well, thank you for giving us part two of that.
[143.04 --> 143.74]  That's right. We're honored.
[144.30 --> 147.04]  So, you're not here to talk about Node. You're here to talk about Dino.
[147.04 --> 151.10]  You've rearranged the letters. You've been hard at work for a couple of years now.
[152.02 --> 157.36]  And I would like to go back to your JSConf EU talk, which has become famous now in 2018,
[157.68 --> 162.94]  the 10 things that you regret about Node.js, which turned out not being 10, it seems like.
[163.30 --> 166.14]  I don't know if you even named it that or they named it that on the YouTube file,
[166.70 --> 171.72]  because it was like 7, and then you introduced Dino, and I was going through it trying to find it.
[171.72 --> 174.14]  They named it that, yeah, it was not 10.
[174.70 --> 176.72]  Yeah, that's just the way they named it on YouTube.
[176.98 --> 178.42]  Like, I don't even think your slides said that.
[178.42 --> 181.04]  They're like 1, 2, 3, 4, 5, 6, 7. That's close enough to 10. We'll just call it 10.
[181.04 --> 186.36]  Yeah, round numbers and lists apparently work, you know, on the internet. So, somebody threw 10 on it.
[186.46 --> 190.32]  Yeah, if you go to the titles, if you like look at that talk and see the title slide,
[190.32 --> 194.62]  it has a completely different title. It's not 10 things I regret about Node.
[195.30 --> 200.38]  Well, good, because you had 7 of them. And it seems like that was a talk that was put together somewhat last minute,
[200.46 --> 203.22]  maybe because Dino wasn't quite as far along as you hoped it would be.
[203.30 --> 205.76]  Or what was the backstory on that? Because even in the beginning, you said,
[205.88 --> 207.96]  this wasn't my talk, but now it is my talk.
[207.96 --> 212.58]  Was that the thing, is Dino wasn't quite ready to give more of a fleshed out version of it?
[213.26 --> 218.70]  Yeah, I was working on a different project, and I had applied to give this talk on this other project.
[218.70 --> 226.08]  It was something very similar to TensorFlow.js. So, it was TensorFlow binding to Node,
[226.24 --> 233.64]  so that you could train machine learning models in Node. Plus, something that's like Python's
[233.64 --> 240.28]  Jupyter Notebook, or in JavaScript, there's this Observable company, like a website where you could
[240.28 --> 247.42]  kind of insert a bit of code and plot functions and stuff. And yeah, TensorFlow.js and Observable
[247.42 --> 251.86]  actually came out just before that talk. And a month before that, we decided, like,
[251.94 --> 259.04]  actually, these projects are kind of dead end, or we should do something else. And JSConf would
[259.04 --> 263.90]  insisted that I continue to give a talk on something else. So, I put together this Dino demo.
[264.38 --> 268.86]  Nice. So, there's a bunch of stuff about Node. Anytime you make design decisions, you know,
[268.90 --> 274.48]  in retrospect, it's easy to look back. And it's hard not to find flaws in things that we create.
[274.48 --> 278.84]  But we don't always get a second shot at it, you know, and Dino seems to be, to a certain degree,
[278.92 --> 283.66]  a second shot, or at least another round of something different, but similar. And I'm just
[283.66 --> 288.88]  curious of the seven or so things there that you listed, which if you don't remember, they're
[288.88 --> 293.74]  not sticking with promises, the security system, which I think you definitely are addressing with
[293.74 --> 298.92]  Dino, the build system, package JSON, Node modules. Those are a few things, just high level,
[298.92 --> 303.66]  that you mentioned, that were regrets. How many of those do you feel like you've
[303.66 --> 307.50]  alleviated with Dino? How many things did you fix?
[308.40 --> 314.56]  I mean, all of those things, I think. You know, generally, Dino is an effort to
[314.56 --> 323.74]  move the server-side JavaScript platform forward in kind of radical steps. Node has a lot of users,
[323.74 --> 330.66]  of course, and they try very hard to maintain backwards compatibility, which is laudable and
[330.66 --> 338.44]  great for all of the users of it. But that means that it's very slow in taking on new changes. And,
[338.54 --> 343.30]  you know, I think the major change in JavaScript over the last couple of years, maybe two major
[343.30 --> 352.08]  changes are async await syntax and the ES modules syntax. These are pretty radical changes to the
[352.08 --> 357.28]  language. And, you know, JavaScript is like this evolving system over time. The JavaScript of today
[357.28 --> 364.48]  is nothing like the JavaScript of 15 years ago. And yeah, it just felt like Node was not keeping
[364.48 --> 368.44]  pace with web browsers in terms of bringing on these new features.
[369.14 --> 374.54]  So now you're a few years into Dino. We've hit 1.0 last year. Lots going on, lots formalizing. I'm
[374.54 --> 379.02]  wondering now, since you've gotten into the weeds for a couple of years, you look back,
[379.02 --> 384.22]  have you made any mistakes so far? You had seven or so with Node that you regretted. Any regrets with
[384.22 --> 384.64]  Dino yet?
[385.22 --> 391.18]  Yeah, definitely. I mean, it's hard to make software and not make mistakes, of course.
[391.30 --> 391.48]  Totally.
[392.00 --> 397.36]  I mean, this is going to be very controversial, but the TypeScript aspect of Dino, Dino has
[397.36 --> 403.38]  TypeScript compiled into it, is super nice, very friendly, very nice to be able to just get up and
[403.38 --> 411.22]  started easily. But browsers do not support TypeScript. And Dino's overarching philosophy is that
[411.22 --> 419.30]  is bringing server-side JavaScript closer to browser JavaScript. And in this aspect of supporting
[419.30 --> 427.30]  TypeScript out of the box, we are kind of overstepping our goals. So, you know, we're supporting this
[427.30 --> 433.68]  extension to JavaScript. I mean, I don't know about you all, but I feel like TypeScript is eventually
[433.68 --> 439.24]  what JavaScript is going to be. I feel like it is kind of the next generation of JavaScript. And,
[439.72 --> 443.22]  you know, I'm very eager, and I think many people are, to kind of go in that direction.
[443.74 --> 452.64]  But it's a big complication to our system to support TypeScript. And I think weakens our argument that
[452.64 --> 459.94]  Dino is web-compatible. So, we're certainly not removing it now because Dino depends on it.
[460.18 --> 462.54]  Right. Go back and start over, would you? Yeah.
[462.88 --> 467.80]  But, yeah, I think it would have been easier for us to get started had we not supported that out of
[467.80 --> 468.82]  the box initially.
[469.38 --> 474.20]  That being said, it seems like it was also a big draw and a big differentiator at first.
[474.30 --> 474.66]  Absolutely.
[475.14 --> 480.64]  Let me just say that I was around when you announced Node back in 2009 or whenever it was. I remember it
[480.64 --> 486.94]  right around the iPhone time. And I remember the reaction to Node. Probably not as well as you do,
[487.06 --> 490.90]  because you were on the project. I was just an innocent bystander. And maybe we remember it
[490.90 --> 496.18]  differently. But to me, it was like immediate. It was a hit. Everybody was excited. We had Michael
[496.18 --> 500.28]  Rogers just on the show a little bit back, and he was just reminiscing a little bit how like nothing
[500.28 --> 505.12]  existed for Node. Like when Node came out, you announced it. There was no ecosystem. There was
[505.12 --> 510.56]  nothing. And then like everyone just piled in. Like people saw fertile ground. And you're looking at me a
[510.56 --> 514.88]  little weird. Like maybe that's not how you remember it. But it seemed like people came in
[514.88 --> 520.56]  droves to fill out that ecosystem. It just was like immediately a hit. And I think it filled a real
[520.56 --> 524.66]  need. Well, first of all, let me stop and say, did you have that same feeling or am I seeing it
[524.66 --> 525.58]  through rose colored glasses?
[526.12 --> 528.48]  I think that's a fair characterization of what happened.
[529.04 --> 529.74]  Adam, you were around.
[530.46 --> 530.56]  Yeah.
[530.80 --> 535.06]  Node was huge immediately. Like maybe not immediately, but like people were very excited about Node,
[535.10 --> 535.30]  right?
[535.30 --> 535.66]  Yeah.
[535.78 --> 535.90]  Yeah.
[536.40 --> 540.92]  Well, then there was a lot of things even like with Walmart Labs and Black Friday. This
[540.92 --> 546.04]  wasn't back in the 2009 days particularly, but there was a lot of inertia around, you know,
[546.48 --> 552.56]  high traffic websites and scalability and, you know, it's enterprise ready. So a lot of different
[552.56 --> 558.14]  enterprise teams were happy to move on to something more modern despite these seven flaws as you've
[558.14 --> 562.64]  described in your talk, you know, because I think every step forward is a good step forward,
[562.64 --> 567.06]  even if it's got some flaws, which software has flaws every single time.
[567.26 --> 573.44]  Yeah. So I guess my point is, is that it filled a huge void and it got a huge rush of enthusiasm
[573.44 --> 579.78]  and adoption because of that. And then Dino comes out and it doesn't come out into that same moment
[579.78 --> 585.02]  in time, right? It comes out later where you have a mature Node ecosystem. You have millions of packages
[585.02 --> 591.36]  on NPM. You have people doing this full-time careers and consultant. I mean, there is a thriving
[591.36 --> 598.26]  Node ecosystem already. And so into that milieu or that culture, Dino has to set itself apart,
[598.32 --> 603.04]  right? And TypeScript was one of the ways that it kind of did that to start. What were the other
[603.04 --> 606.50]  big ideas that Dino has that sets it apart from everything else?
[606.94 --> 613.44]  First important aspect is that it's written in Rust instead of C++. Node is a very large C++ project.
[614.32 --> 618.98]  And I'm not sure how you guys feel about this, but I'm very convinced that I will never start
[618.98 --> 626.44]  another C++ project. Rust really solves the C++ problem as it were. And I think that there's many
[626.44 --> 632.96]  great things about Rust, but the thing that is most important to me is the ability to have a single
[632.96 --> 640.84]  build system. So this cargo system of linking together different Rust crates. In C++, there's no
[640.84 --> 649.96]  one defined way of how to take different C++ libraries and smash them together. So Chrome has
[649.96 --> 656.92]  this GN project. Node uses this GIP project. There's CMake. There's a lot of different tooling for
[656.92 --> 665.94]  kind of compiling together dependencies in C++. And this ends up being a huge, huge complexity in terms of
[665.94 --> 673.26]  bringing in external third-party code into a big project. And so, you know, in Node days, when we want
[673.26 --> 680.46]  to, you know, we built a web server and like, you know, you have to parse HTTP. And it's such a difficult
[680.46 --> 686.82]  problem that we ended up writing our own HTTP parser for this. It's so difficult to bring in external code
[686.82 --> 693.06]  that you end up often having to just write the stuff over again because it's so difficult to link.
[693.06 --> 699.84]  And this is very different in Rust, right? If I need a YAML parser, if I need an HTTP server,
[700.24 --> 707.44]  any sort of third-party stuff, I would do what people are used to doing in JavaScript or Ruby or
[707.44 --> 712.90]  Python. You can just kind of include dependencies and have this all compiled together really nicely.
[713.18 --> 721.78]  And that's an important aspect for a platform like Deno or Node because, you know, we provide all of
[721.78 --> 730.16]  these APIs to do various things, right? You want to open a WebSocket. You want to have an HTTP2 web
[730.16 --> 737.28]  server. All these various systems that it talks to need implementations. And it's very nice that we're
[737.28 --> 743.72]  able to just link in third-party implementations of all these various systems pretty easily. So
[743.72 --> 751.36]  from a maintainer's perspective, rewriting it in Rust is a really killer feature that kind of allows us
[751.36 --> 756.22]  to iterate much, much quicker. Yeah. Maybe it kind of a feature that end users don't appreciate
[756.22 --> 762.76]  as well as the authors and maintainers, but they will appreciate over time as you are allowed to
[762.76 --> 769.78]  continue at a certain pace that, you know, the C++ ecosystem didn't allow with Node. Or maybe
[769.78 --> 774.46]  at a certain point, Deno will also get so many lines of code and so much stuff in it that, I mean,
[774.48 --> 779.44]  it will slow down. And any project that's mature is move slower than when it's young, but maybe it'll
[779.44 --> 786.18]  keep a pace that keeps your users happy. Sure. Just talking about other aspects of Deno kind of
[786.18 --> 793.38]  internally that are important is the binding interface, kind of the boundary between JavaScript
[793.38 --> 802.70]  and the native language, in this case, Rust, in Node's case, and C++. Node was fairly ad hoc at adding
[802.70 --> 809.02]  bindings. We just kind of added them all over the place. There was no set system for calling from
[809.02 --> 815.48]  JavaScript into C++ and vice versa. And in Deno, there's a system for this. We call them ops.
[815.48 --> 822.08]  And so this kind of organizes all of the various bindings that you have to the system facilities
[822.08 --> 829.38]  really nicely. And in particular, organizes all of the async calls that you might make. So ops in our
[829.38 --> 833.96]  system are either a synchronous function, like a function you call into Rust and it returns a value
[833.96 --> 840.68]  immediately, or it's an async function, which returns a promise that eventually resolves to a value. And so
[840.68 --> 846.24]  one of the really nice aspects in Deno is that everything is organized as promises. It's kind of
[846.24 --> 851.32]  promises all the way down. There's not kind of random callbacks that happen throughout the system.
[852.00 --> 857.26]  This was actually a pretty big design mistake. I forget if I did discuss this or how much I discussed
[857.26 --> 862.92]  this in the talk, but WebSockets are on my mind right now because we're doing a lot with WebSockets.
[863.58 --> 866.98]  WebSockets have this on-message callback, right?
[866.98 --> 873.98]  And one of the problems with this is that you can't really stop the system from giving you new
[873.98 --> 879.30]  messages. You can just get flooded with these callbacks. There's no way to kind of throttle
[879.30 --> 886.38]  this incoming stuff. And so because of the inability to stop these new messages coming in through this
[886.38 --> 891.96]  WebSocket, you can get into really bad situations where you're always handling the newest WebSocket
[891.96 --> 896.82]  message because you're getting flooded from this one socket, say. And this is not
[896.82 --> 901.56]  specific to WebSockets. This happens in different parts of the system. That's quite bad.
[902.64 --> 910.58]  This actually causes pretty, this manifests itself in kind of bad tail latency situations where,
[910.78 --> 916.78]  you know, usually the system is fine, except under pressure when like suddenly, like, you know,
[917.06 --> 921.42]  one part of the system is getting flooded with these callbacks. And so you start getting really
[921.42 --> 927.06]  bad latencies. WebSockets in particular have, there's a new standard out called WebSocket
[927.06 --> 933.44]  streams, which addresses this, allowing you to create some back pressure that is to not accept
[933.44 --> 939.54]  the newest message if you're not ready to handle it. And in general, this async await paradigm syntax
[939.54 --> 945.14]  and the usage of promises everywhere generally kind of solves this problem. Because as long as you're
[945.14 --> 949.72]  always getting these promises and you're awaiting them, you're kind of stopped at a certain line.
[949.72 --> 956.04]  You're not kind of unboundedly accepting new callbacks from the system. Anyway, that's all
[956.04 --> 961.86]  to say that Dino is promises all the way down. And so kind of from the fundamental layer, we've tried
[961.86 --> 969.46]  to deal with this back pressure problem. Another big differentiator is the package management story,
[969.72 --> 975.02]  right? That's right. Tell us about how Dino sees the world of packages. So yeah, I mean,
[975.02 --> 981.30]  I would bring this back to in general, Dino is trying to use web APIs, we try not to introduce
[981.30 --> 988.98]  invented APIs, like I had to do in 2009. When I started node, there's just a lot of APIs that were,
[989.16 --> 996.08]  you know, there was no module system. And so we invented this require syntax to link to JavaScript
[996.08 --> 1002.94]  files together. Yes, modules, ECMAScript modules is a standard. Now, this is part of the new JavaScript
[1002.94 --> 1009.86]  standard, which defines import and export, I'm sure you guys are familiar with it. And this works in
[1009.86 --> 1016.92]  web browsers these days, these imports and exports and ways to link different files together. And the
[1016.92 --> 1023.88]  way that this works on the web is you can actually do import a URL from not just a relative URL, but a
[1023.88 --> 1030.70]  absolute URL that exists on a different server. And so you can actually pull in code, you know, if you
[1030.70 --> 1037.94]  think of like a HTML page and scripts tags, you know, you can script source, have a link to
[1037.94 --> 1044.42]  hgpsjquery.org slash jquery version 1.2.js. That's how we used to do it back in the day,
[1044.44 --> 1049.08]  we just have our script sources, and you just have your list of sources and everything was so simple,
[1049.40 --> 1056.58]  which is quite nice, right? I mean, it's really nice to have a HTML file and just drop in a link to
[1056.58 --> 1064.60]  the jquery CDN and suddenly have that available without having to do a whole thing.
[1064.82 --> 1065.48]  Yeah, totally.
[1065.64 --> 1070.86]  A whole installation procedure, right? Anyway, Dino is built around the idea that we think this is
[1070.86 --> 1077.26]  sufficient actually to link remote code together. I mean, the problem is really, I've got code that
[1077.26 --> 1084.66]  I'm developing locally. And I really want to include some third party library. How do I do that?
[1084.66 --> 1091.12]  In the node system, you would download that third party code into a node modules folder.
[1091.68 --> 1098.22]  And this require system and knows how to look into this node modules folder. So when you do require
[1098.22 --> 1104.20]  express, it looks in the local directory node modules, and then looks for the express folder.
[1104.94 --> 1108.90]  And, you know, it has some special knowledge about looking up package JSON,
[1108.90 --> 1117.16]  and looking up index.js has kind of this algorithm of how to find what module you're referring to there.
[1117.58 --> 1122.70]  And we've basically done away with all of that. We've just said, you know, if you've got code that
[1122.70 --> 1128.42]  you're working on locally, then, you know, you store that in your local folder, and that's yours to
[1128.42 --> 1135.40]  deal with. And if you want to link to some third party code, you can, of course, download it into a
[1135.40 --> 1142.74]  vendor folder, if you wanted to, and dot slash relative include relative import that. But you
[1142.74 --> 1149.54]  can also just import the remote URL via HTTP. So our module system is really the web browsers module
[1149.54 --> 1156.22]  system, which is exactly HTTP. So you know, we don't have, unlike NPM, which has a specific protocol for
[1156.22 --> 1162.54]  distributing packages, you have to ask the NPM server what the latest package is, get the link to
[1162.54 --> 1168.52]  the tarball, download the tarball. We don't define a protocol like that. We just have HTTP, and you
[1168.52 --> 1172.34]  can download JavaScript or TypeScript over HTTP.
[1173.72 --> 1178.26]  And what are the advantages of that, then? If pulling a module, say for NPM, for example,
[1178.84 --> 1184.48]  the stability of being able to make those, you know, NPM install, for example, and being able to,
[1184.84 --> 1188.56]  I suppose, sit there and wait, like some people might, you know, what are the advantages,
[1188.56 --> 1194.52]  I suppose, of that system over this older one? Obviously, it's, you know, modern in terms of
[1194.52 --> 1199.08]  the way the web browser is working. But what are the specific, you know, DevEx, you know,
[1199.40 --> 1202.22]  DevExperience kind of advantages there?
[1202.70 --> 1209.98]  I think it has the effect of feeling immediate. And there's nothing to install ahead of time,
[1209.98 --> 1215.06]  because the Dino system itself actually takes care of downloading that. And so, you know,
[1215.06 --> 1220.94]  I would say the other DX effect is that you can have scripts that are single files. In Node,
[1221.00 --> 1227.08]  you generally, at minimum, need to have a package JSON and your JavaScript file. Your package JSON
[1227.08 --> 1233.10]  needs to define where you're linking. And your JavaScript file has some source code in it.
[1233.94 --> 1239.62]  In Dino, you can say where you're linking on line one, and the rest of the script can be your code.
[1239.62 --> 1245.02]  So you can actually define a complete program, both where to get your third party code,
[1245.16 --> 1250.54]  and your own code all in one file, run it without, you know, creating a directory. And
[1250.54 --> 1254.66]  I guess what I'm trying to say is there's less boilerplate to deal with.
[1255.04 --> 1255.42]  It's minimal.
[1255.56 --> 1256.02]  Yeah, simple.
[1256.22 --> 1256.92]  It's very minimal.
[1257.56 --> 1263.24]  Yeah, I mean, you can have, you know, file tabbing fatigue or swapping from different files.
[1263.44 --> 1267.02]  I love that a lot in a whole different land. With like Tailwind, for example,
[1267.02 --> 1271.92]  you can do a lot in the same file or in the same HTML file. You're not jumping back from CSS to HTML.
[1272.14 --> 1276.80]  So similar to how that world might work, you're not jumping back and forth. You can stay in the
[1276.80 --> 1283.26]  same file, have this sort of immediate instant gratification of just moving forward, and not
[1283.26 --> 1287.80]  have to jump back and forth between different ways to define what your application is needed to inherit
[1287.80 --> 1290.04]  from or to import, etc.
[1290.04 --> 1297.24]  When you have a large application, if you have hundreds of files, right, having one extra package
[1297.24 --> 1302.44]  JSON file is not a big deal. Like it's no big deal to have a, you know, if you have hundreds of modules,
[1302.58 --> 1308.32]  and you have one extra one, it's not a big deal. So, you know, I think in kind of the tail end of
[1308.32 --> 1313.94]  larger projects, it probably doesn't feel that different. But when you get down to the very small
[1313.94 --> 1321.34]  scripts, the one off scripts, Dino scales down to to a much smaller installation, I would say much
[1321.34 --> 1328.78]  less boilerplate, right? When you do npm in it, it's going to ask you for, I don't know, the license
[1328.78 --> 1334.52]  of your project, you know, the name of your project, all of that stuff is, let's say you're trying to
[1334.52 --> 1340.12]  write a script that's going to rename a bunch of files in a folder. Who cares? I don't care what the
[1340.12 --> 1345.64]  license is. Like, why am I spending any time at all thinking about that problem? Like that is boilerplate.
[1346.20 --> 1351.64]  Yeah. What about the potentially hidden advantage? And I'm assuming this the internet essentially is
[1351.64 --> 1357.74]  your package manager, right? You can link to a raw file on GitHub, you can link to some random site on
[1357.74 --> 1363.32]  adamsdokowiak.com or changelaw.com and just inherit from that. Is that how Dino works? You can just pull
[1363.32 --> 1368.28]  in from any URL, or as you'd mentioned, even a relative from, you know, somewhere locally?
[1368.28 --> 1375.88]  Yeah, that's right. So yeah, you can pull in files from any server. And the nice side effect of this is
[1375.88 --> 1382.06]  that the node ecosystem and all essentially all other programming languages are dependent on a
[1382.06 --> 1388.94]  specific server to distribute third party packages, right? Whether that's crates.io, whether that's
[1388.94 --> 1396.34]  golang.org or npmjs.com. If that server goes down, everything breaks, we are heavily dependent on that.
[1396.34 --> 1401.48]  But contrast that with this is just not very webby. This is not how web browsers work.
[1402.22 --> 1407.80]  It would be a bad day if Google went down. But hopefully, hopefully web browsers continue to
[1407.80 --> 1415.68]  operate like your website should isn't necessarily dependent on any one specific server existing.
[1415.68 --> 1421.86]  And that's nice. Like that's a distributed system. And because of this aspect that you can download
[1421.86 --> 1429.24]  code from any URL, Dino is not dependent on our website, Dino.land, nor is it dependent on any
[1429.24 --> 1434.18]  other website. You can use, you know, unpackage.org for pulling in your third party dependencies,
[1434.18 --> 1436.18]  or you can use GitHub directly.
[1436.56 --> 1437.00]  Great.
[1437.10 --> 1439.56]  Which might be nice since that's where the code is actually stored.
[1439.56 --> 1442.92]  Right. Then if GitHub goes down, we're screwed again. But we were already screwed. So
[1442.92 --> 1448.24]  great website, by the way. I love the dinosaur brand. I love the name. Dino.land is such a cool
[1448.24 --> 1453.06]  domain. Just wanted to give you props for that really quick. What about versioning? I mean,
[1453.08 --> 1457.26]  if I'm a library author, are there idioms around that? Do I just have a new file with like the
[1457.26 --> 1463.98]  version in my file name? How do we deal with things like, you know, Lodash 3.7.1 is out? How do I go get it?
[1463.98 --> 1473.40]  I mean, ultimately, a version is a string of characters. And so is a URL. And so you can
[1473.40 --> 1479.26]  have a version in a URL to specify the version. Think back to the jQuery CDN example, right?
[1479.62 --> 1479.74]  Yeah.
[1479.86 --> 1482.80]  You have perfect ability to link to any version of jQuery.
[1483.38 --> 1488.08]  Good answer. What about existing NPM? Are all the existing NPM packages
[1488.08 --> 1494.62]  then supported if I can find the exact URL of the source code? Is that they'll just work? Or are
[1494.62 --> 1498.68]  they using some things that might not be ESM compatible and stuff like that?
[1499.50 --> 1504.96]  Yeah. So if it's not using ESM, then it's going to be probably problematic.
[1506.00 --> 1511.22]  It may be problematic, even if it is using ESM. Unfortunately, we're kind of in this state
[1511.22 --> 1518.78]  right now in JavaScript, where there's a lot of fragmentation between TypeScript, CommonJS,
[1519.42 --> 1527.00]  Deno, Node. You know, I hate to contribute to that. But I also am, you know, I feel like fighting the
[1527.00 --> 1532.82]  good fight, trying to make things simpler. All NPM packages are available on, for example,
[1533.00 --> 1535.54]  unpackage.org or Skypack.
[1535.80 --> 1536.20]  Skypack.
[1536.20 --> 1543.28]  So you should be able to access those files through HTTP. And if they're ESM, then you're
[1543.28 --> 1550.24]  close to that, to it working. I think the problematic thing is if they use Node APIs. So
[1550.24 --> 1557.60]  Node, for example, has, you know, require FS, you can require FS and like open a file. Deno has
[1557.60 --> 1564.78]  alternative APIs for that. We do not have a top level FS module. We have a compatibility layer for that.
[1564.78 --> 1571.28]  So that's in our standard library. By the way, Deno has a standard library. And you can find that at
[1571.28 --> 1579.12]  deno.land slash std slash node. And using that compatibility layer, you get pretty close,
[1579.22 --> 1583.98]  although there's definitely a lot of modules where there's going to be require some work,
[1584.08 --> 1589.88]  but you can get pretty close to importing a lot of modules. There's a long tail end of
[1589.88 --> 1591.72]  things that are incompatible though.
[1591.72 --> 1620.68]  This episode is brought to you by Retool. Retool is the local platform for developers to build
[1620.68 --> 1626.14]  internal tools, super fast and super easy. They have a ton of integrations and templates to start
[1626.14 --> 1631.16]  with, with a click of a button in seconds. You can start with a new Postgres admin panel application,
[1631.56 --> 1635.76]  kick off an admin panel for reading from and writing to your database built on Postgres.
[1636.20 --> 1641.16]  This app lets you look through, edit and add users, orders and products. It's too easy to
[1641.16 --> 1645.40]  get started with Retool. Head to retool.com slash changelog to learn more and try it for free.
[1645.40 --> 1648.36]  Again, that's retool.com slash changelog.
[1658.60 --> 1666.52]  So Ryan, on your website, deno.land, awesome website. It says a secure runtime for JavaScript
[1666.52 --> 1671.18]  and TypeScript. And of course, secure by default is the top level bullet of Deno features. We haven't
[1671.18 --> 1674.06]  talked about security yet. You want to give us the skinny?
[1674.92 --> 1682.28]  Yeah. So obviously if you're pulling in random packages over HTTP, you should be worried if you're
[1682.28 --> 1688.28]  pulling in code because, you know, you, maybe you've audited this code, but probably not like
[1688.28 --> 1693.68]  that code probably depends on some other code and that those can end up pulling in many, many
[1693.68 --> 1694.28]  dependencies.
[1694.58 --> 1698.76]  It's kind of like those installers where they're like, curl this URL, pipe it into bash. And then a lot of
[1698.76 --> 1702.68]  people will show up in the comments like, please don't do that because bash is going to execute
[1702.68 --> 1707.82]  arbitrary code that's in that URL. Anyways, cut you off. But I just was reminded of that where it's
[1707.82 --> 1712.90]  like, yeah, but it's as long as it's safe, you know, like audit it and you'd be happy. But if you
[1712.90 --> 1715.38]  don't audit it, you probably shouldn't be piping into bash.
[1715.84 --> 1723.04]  Unfortunately, it's really hard to audit all of your code these days. I mean, we depend on society level
[1723.04 --> 1728.56]  infrastructure, right? There's no possible way if you plan to be a productive developer to
[1728.56 --> 1733.66]  go out and actually read through all of the dependencies and the transitive dependencies
[1733.66 --> 1738.30]  of your dependencies. You know, by the way, you're talking about like curling bash scripts.
[1738.56 --> 1743.36]  When you NPM install something, arbitrary code from the internet is running on your computer
[1743.36 --> 1749.86]  without any security sandboxing. So, you know, and beware when you are NPM installing something,
[1750.34 --> 1757.40]  you are completely and utterly open to having your computer taken over. It takes one bad actor in the
[1757.40 --> 1759.48]  ecosystem to make that happen. And we've seen that.
[1760.78 --> 1769.08]  We have seen that, yes. This is mitigated in web browsers. Web browsers do not allow you to
[1769.08 --> 1775.04]  access your local file system. They do not allow you to do a lot of stuff, right? Web browsers are a
[1775.04 --> 1782.44]  secure sandbox. And this is a really nice property of V8 and the JavaScript language is that it does not
[1782.44 --> 1789.44]  necessarily have access to the system. We, Dino and Node, give access to the system so that you can do
[1789.44 --> 1794.80]  things like writing a little script to rename a bunch of files. The purpose of a server-side JavaScript
[1794.80 --> 1801.50]  system is to interact with the system. But in Node, we did this without any constraints. We just opened
[1801.50 --> 1806.50]  all sorts of holes. So you can access the file system, you can access the network, you can do all sorts of
[1806.50 --> 1814.44]  stuff. There's no gating on those privileges. In Dino, we're much more aware of opening holes into the
[1814.44 --> 1820.98]  system. And I mentioned earlier these ops and how Dino has a very centralized system for calling from
[1820.98 --> 1827.78]  JavaScript into Rust. By having this centralized system, we also have kind of centralized gating
[1827.78 --> 1834.46]  for security. And so by default, when you run a Dino program, whether that's a local program on your
[1834.46 --> 1842.50]  computer or a remote program via a HDP URL, it's given no access to the system. All it can do is
[1842.50 --> 1849.68]  compute. So it cannot access your file system. It cannot open outbound connections. Can't do anything
[1849.68 --> 1854.84]  mischievous. It can calculate some numbers. It can print to standard out, but that's about it,
[1855.08 --> 1862.32]  which sometimes is all you want. To allow programs to, in web browsers, they have this system for kind of
[1862.32 --> 1869.38]  opting in to more privileges. So for example, websites can access your webcam, right? But not just any
[1869.38 --> 1874.50]  website can access your webcam. It needs to like elevate its privileges. So, you know, you get this
[1874.50 --> 1881.50]  little pop-up that says, do you want to allow website X to access your webcam? Dino is very similar. When you
[1881.50 --> 1888.68]  try to access the file system, it's going to fail if you don't have the privileges and you can give it
[1888.68 --> 1894.32]  those privileges. And you give it those privileges via command line flags, right?
[1894.74 --> 1901.54]  Via command line flags. So we have, you can do allow all if you want to node mode,
[1901.70 --> 1908.74]  where there's, there's no privileges. There's no gating. We have allow write to write to the file
[1908.74 --> 1915.92]  system. We have allow run to run sub processes. We have allow read to read file system. We have allow
[1915.92 --> 1923.64]  plugin to load kind of rust plugins, which we can't assure are not going to do something nasty. We have
[1923.64 --> 1930.38]  allow net for making outbound network connections and allow end for environmental variables, which may
[1930.38 --> 1931.72]  often contain secrets.
[1932.80 --> 1937.06]  Is that something you can put in the file itself or does it have to be a flag to the runtime?
[1937.06 --> 1944.42]  It has to be a flag. We are considering having a configuration file. We are really conservative
[1944.42 --> 1950.84]  about adopting kind of new file formats. You know, I was just talking about how we try to keep things
[1950.84 --> 1956.54]  as boilerplate free as possible. And so we don't want to force people to write a configuration file. We
[1956.54 --> 1962.56]  don't want, you know, kind of overhead of configuring your system before you ever get started. So for now,
[1962.56 --> 1969.14]  they are command line flags and they're pretty obvious and annoying. And that's kind of purposeful because
[1969.14 --> 1974.60]  these are security things. They should be obvious and annoying. You should, you know, be very clear that you
[1974.60 --> 1982.14]  are allowing the system to run arbitrary sub processes. Yeah. So via command line flags is how you enable them.
[1982.30 --> 1987.54]  How often are those flags being used by, you know, general applications you see being built? Like all the time.
[1987.54 --> 1993.44]  All the time. All the time. Yeah. I mean, it depends on what you're doing. I mean, if you say have a,
[1993.82 --> 2001.86]  let's say you're writing a program like ES Lint, this ES Lint like program doesn't need to make outbound
[2001.86 --> 2008.14]  network connections. It doesn't need to write to the disk. All it needs to do is read from the disk. So
[2008.14 --> 2012.56]  you would only, you would only enable the allow read in that case.
[2012.56 --> 2016.68]  Yeah. So I was telling you during the break that I was writing this little script with Dino the other
[2016.68 --> 2023.62]  day and basically it went out to the Slack API, got some data from there about members of our community
[2023.62 --> 2029.76]  and then, uh, looped over. I was trying to like pick a random winner for a giveaway from like a certain
[2029.76 --> 2035.02]  channel from one of our Slack channels. And then it, you know, picked a random three or something and
[2035.02 --> 2043.36]  just printed them out, you know, very simple use case. And I had to use allow net and obviously
[2043.36 --> 2047.58]  cause I'm hitting Slack API. Right. And then I also had to use allow end because I could have just
[2047.58 --> 2052.60]  hard coded the token into the script, but I just used it as an environment variable. And I could say
[2052.60 --> 2055.46]  from a script from a person who's just trying to get stuff done, it is kind of annoying. You're just
[2055.46 --> 2060.78]  like, ah, you know, I didn't know about dash all. I would have just used that. But now I know I'll just
[2060.78 --> 2065.46]  use that all the time, baby. Node mode. Yeah. Node mode, please. I mean, if, if, if you're the one
[2065.46 --> 2070.48]  who's writing it, then you're pretty sure that it's going to be okay. I think it's the problem
[2070.48 --> 2074.36]  comes when you're running somebody else's code. Yeah. Like I said, this is a inconvenience,
[2074.50 --> 2080.30]  but it's like a very explicitly well-considered inconvenience. That's like, yes, we're doing this
[2080.30 --> 2085.12]  because of the trade-off is completely worth it. Right. This is a shift left kind of moment where
[2085.12 --> 2091.94]  you're taking typical, maybe security concerns that, you know, you might rather just say Dino
[2091.94 --> 2096.12]  run or whatever the command is to run a Dino application, but you're kind of shifting left
[2096.12 --> 2101.98]  saying these are security concerns that Dino resolves and has control over and putting them
[2101.98 --> 2106.96]  more front and center rather than, you know, as you said, in a configuration file, which is less minimal,
[2107.26 --> 2112.68]  requires more potentially different file format or other concerns. Like this is a, a shift shift
[2112.68 --> 2117.30]  left kind of moment. Would you say that? Sure. I haven't heard the term shift left before.
[2117.88 --> 2122.32]  Shift left is whenever you take the security concerns, which if you take a, you know, a product
[2122.32 --> 2128.26]  life cycle left to right, left being dev iteration, you know, right going to production. I see.
[2128.54 --> 2133.08]  A shift left is you sometimes think about security further to the right. Once it's shipped,
[2133.18 --> 2138.32]  potentially shift left is a term using security minds to take that security concern and shift it more
[2138.32 --> 2144.56]  left into dev land. Yeah. I should mention that there is a new feature dash dash prompt,
[2144.88 --> 2150.02]  Dino run dash dash prompt. So if you don't want to allow all the current behavior is if you hit one
[2150.02 --> 2155.22]  of these ops, that's trying to access the file system and you don't have the correct allow flags,
[2155.66 --> 2160.76]  you get an exception. The process drops out, errors out. There is a new feature that's kind of has an
[2160.76 --> 2165.48]  interactive prompt that will be like, Hey, I'm trying to read this environmental variable.
[2165.48 --> 2171.66]  Are you, do you want to allow this? Yes or no. And so you can kind of yes or no through the exact
[2171.66 --> 2176.46]  accesses that the system is doing. And we think that we're going to enable this by default actually,
[2176.52 --> 2181.76]  and not require this dash dash prompt flag. And so this is kind of going more in the direction of,
[2181.94 --> 2187.30]  as always in the direction of web browsers, we'd like this programming model where you opt into
[2187.30 --> 2193.26]  additional privileges. No, I like that. It sounds like a good, a good compromise, right? You're kind of
[2193.26 --> 2197.36]  shifting a little bit further, right? But you're following the web browsers lead where it's like,
[2197.42 --> 2202.98]  are you sure you want to give this person access to your webcam? You know? And if you say yes,
[2203.70 --> 2211.48]  it's on you. So security front and center, we've talked about packages and how that all stuff works,
[2211.60 --> 2216.06]  importing other people's code. We've talked about TypeScript. What are some other aspects of Dino that
[2216.06 --> 2220.58]  are cool and exciting? There's some tooling things, there's a formatter, there's some of these kind of
[2220.58 --> 2225.58]  developer experience things that help you stay productive, right? Yeah. So there's a bunch of
[2225.58 --> 2232.78]  subcommands in Dino. So Dino run being the most obvious one to run a script, but we're kind of
[2232.78 --> 2237.54]  taking this go approach where we're just going to build in all the tooling for you so that you don't
[2237.54 --> 2244.48]  need to bring in all this other third party tooling. So for example, we have a code formatter built into
[2244.48 --> 2249.98]  the system. So you can Dino format your code. We have a linter built into the system. You can Dino
[2249.98 --> 2257.68]  lint. We have a test runner, Dino test to run tests. We actually have all sorts of stuff in there. We
[2257.68 --> 2264.86]  have test coverage and we have a documentation generator and we have a dependency analyzer,
[2265.06 --> 2270.52]  Dino info. It'll show you your dependency tree. Generally, Dino knows all about your source code.
[2270.58 --> 2276.24]  It knows all about your dependencies and what it's doing. And you know, why not? We're distributing this
[2276.24 --> 2282.00]  executable. All of this stuff is written in Rust and so compiles down really tightly. And so, you know,
[2282.06 --> 2289.38]  our formatter that you run is not prettier. It's something called dprint and it's written in Rust
[2289.38 --> 2295.90]  and it's like a hundred times faster. And our linter is not ESLint. It's DinoLint and DinoLint is written
[2295.90 --> 2306.64]  in Rust and is very, very fast. We have a DinoLSP, which allows VS code to talk to Dino and get kind
[2306.64 --> 2313.24]  of tab completion, really nice editor interaction. So Dino can basically tell your editor, you know,
[2313.30 --> 2319.64]  documentation, all sorts of interesting interactions that Dino can help provide VS code.
[2319.78 --> 2320.88]  That's all really cool stuff.
[2320.88 --> 2326.68]  How much of that stuff is informed or inspired by other languages? Are you a language aficionado?
[2326.84 --> 2330.92]  Do you watch what the Go folks are doing, what the Elixir folks are doing, what the
[2330.92 --> 2335.34]  Haskell folks are? Are you watching these different ecosystems and saying, oh, there's a good idea?
[2335.38 --> 2340.52]  Because I think, you know, GoFoom kind of made this formatter a popular thing to do at the language
[2340.52 --> 2345.38]  level, not at like a third party level. And it seems like you're pulling in lots of good ideas.
[2345.38 --> 2351.24]  Absolutely. I mean, this heavily inspired by Go, not just in these various toolings,
[2351.30 --> 2356.08]  but all throughout the system. It's important to continually improve and take good ideas where
[2356.08 --> 2356.94]  you can get them.
[2357.74 --> 2361.38]  So the standard library is pretty fleshed out as well. I'm just wondering, like, where are the
[2361.38 --> 2367.22]  holes? Because Dino's still, it's a 1.0, but it's newer. It's not as mature. Is the ecosystem still
[2367.22 --> 2373.00]  waiting for like large holes to be filled? I know you're working on, or you recently shipped
[2373.00 --> 2377.64]  HTTP2 web server backend. So like things that you expect to be there are kind of there,
[2377.76 --> 2381.24]  but at a certain point, do you get to where you're looking for a package and it's only
[2381.24 --> 2384.74]  in Node, it's not in Dino. Is that still the situation?
[2386.30 --> 2391.74]  Yes, that is still the situation. You know, things take time. I expect this will be worked
[2391.74 --> 2397.74]  out over time. I remember back in like 2010, people would be like, how do I connect to my
[2397.74 --> 2406.06]  SQL with Node? And I would, you know, turn red face and apologize that I did not have a,
[2406.06 --> 2410.74]  my SQL library yet. And they're like, but how is that going to happen? And I said, I don't know
[2410.74 --> 2416.34]  how that's going to happen. I just hope that that is solved at some point. And like, it's embarrassing
[2416.34 --> 2420.86]  to even think that that was a concern because that was totally not a concern. Like all those problems
[2420.86 --> 2426.30]  got worked out, like essentially without my interaction, you know, Dino and Node are very
[2426.30 --> 2430.96]  similar systems. They're both built on V8. They're both JavaScript. They're pretty similar.
[2431.18 --> 2438.54]  The differences are relatively superficial. I mentioned this Dino land slash standard library,
[2438.90 --> 2444.66]  the Node compatibility layer. This is a work in progress. If you go check it out, there's something,
[2445.22 --> 2452.58]  I think we're maybe at 40% compatibility now. So we're still filling these things out. And I think
[2452.58 --> 2459.72]  over time, it will be less and less of a problem to take existing code and run it in Dino. But,
[2459.80 --> 2465.10]  you know, there's still a lot of work to do. So you mentioned this HTTP2 web server. So up until
[2465.10 --> 2473.68]  recently, Dino was using a web server written in TypeScript that was a loose port of Go's web server.
[2473.68 --> 2483.00]  So it's built on top of TCP sockets and TLS sockets. And, you know, it was a nice HTTP 1.1 server,
[2483.24 --> 2491.60]  but had some problems in that it didn't support HTTP2. And because we just made this port ourselves and
[2491.60 --> 2497.60]  are not particularly interested in writing web servers, we're kind of dead ended with that code
[2497.60 --> 2504.74]  base, like we're forced to then write an HTTP2 web server, HTTP2 being a much more complicated
[2504.74 --> 2511.34]  protocol than HTTP 1.1. What we'd really like to do, I mentioned this earlier about linking in native
[2511.34 --> 2518.60]  code libraries using Rust. Rust obviously has a web server already implemented. In fact, Dino already has
[2518.60 --> 2525.18]  that web server in its binary somewhere deep inside of it. What we really want to do is just allow people to
[2525.18 --> 2533.42]  call from JavaScript into this hyper web server in Rust and start up a nice fast HTTP2 web server.
[2533.90 --> 2540.18]  This work is still unstable. It's shipped in Dino 1.9. So, you know, people can use it if they use the
[2540.18 --> 2546.82]  dash dash unstable flag. But yeah, now we're working on this native web server, which I think is serving
[2546.82 --> 2553.26]  websites is quite important to server side JavaScript tasks. And it's quite fast. It has very good latency,
[2553.26 --> 2560.06]  very good throughput. So, you know, we have some preliminary analysis of its performance on the 1.9
[2560.06 --> 2565.30]  release notes. We hope to stabilize this in the next couple of months, and people will have a very
[2565.30 --> 2567.74]  fast web server available right out of the box.
[2583.10 --> 2589.14]  This episode is brought to you by Cloud Zero. They help teams monitor, control, and predict their cloud
[2589.14 --> 2595.06]  value. And I talk with Ben Johnson, co-founder and CTO at Obsidian Security. They get tremendous value from
[2595.06 --> 2600.82]  using Cloud Zero. Ben shared with me the challenges they face driving innovation and customer value,
[2600.82 --> 2605.06]  while also trying to control and understand their Amazon Web Services spend.
[2605.06 --> 2612.90]  We want our engineers to move fast, to innovate, and to really focus on driving customer value. Yet, at the
[2612.90 --> 2621.06]  same time, reality is we have to pay for cloud compute and storage. And the challenge around AWS is often
[2621.06 --> 2626.26]  that you have multiple accounts, you have lots of different services, you have some people who only
[2626.26 --> 2631.54]  have access to development environments, not necessarily production. A lot of these different challenges
[2631.54 --> 2638.18]  across services, across accounts, that make it hard to understand the positive or negative impact
[2638.18 --> 2645.46]  to the costs that the new feature, the scale, you know, maybe the change in architecture are having.
[2645.46 --> 2651.22]  And so, giving our team more insight into the ramifications, again, positive or negative,
[2651.22 --> 2655.78]  of their changes in order to, maybe we need to really move fast, let's have less worry about cost right
[2655.78 --> 2660.50]  now, or maybe now we're in a more stable place, let's drive down the cost so we can, you know,
[2660.50 --> 2666.02]  give those cost savings on to our customers or improve our own margin. So, a product like Cloud Zero can
[2666.02 --> 2671.54]  really help your team get a handle on costs, get alerted to those spikes, feel good when you actually
[2671.54 --> 2675.62]  see the costs drop, and do all that without a whole lot of investment of your own time.
[2675.62 --> 2679.70]  All right, if your organization shares similar struggles as Band and Obsidian Security,
[2679.70 --> 2684.90]  check out Cloud Zero today. Learn more and get a demo at cloudzero.com slash changelog.
[2684.90 --> 2687.22]  Again, cloudzero.com slash changelog.
[2698.42 --> 2704.90]  So, we're on back March 29th, you announced the Dino company, and obviously you got a great
[2705.46 --> 2710.66]  new start to what you begin with Node. A lot of new beginnings here, a lot of wrongs made right,
[2710.66 --> 2716.10]  and to put behind that, a company. So, why are you on this path? I suppose more than 10 years,
[2716.10 --> 2721.14]  you know, 2009, now it's 2021. What's the path? What's the new company? What are you doing?
[2721.14 --> 2728.82]  David Plylar Programming languages are important. You know, the world is built on software and of the
[2728.82 --> 2734.74]  programming languages, dynamic programming languages are, I would say, what most people are interacting with
[2734.74 --> 2740.90]  day to day-to-day, you know, but most business needs are best expressed in, you know, Ruby on Rails or,
[2741.54 --> 2748.66]  you know, Node, JavaScript, or Python. Because, you know, to be honest, most problems are not compute-bound,
[2748.66 --> 2754.18]  they are engineering-bound, right? All of our time spent as programmers is kind of what we're trying
[2754.18 --> 2761.54]  to optimize for. And scripting languages, dynamic programming languages are the best way to get going
[2761.54 --> 2769.86]  fast. You know, I work on this problem because I think it's very empowering to be able to take a
[2769.86 --> 2778.18]  system like Node or Dino or Perl or Ruby and just start programming really fast. I got started with
[2778.18 --> 2784.42]  Perl myself, and I don't know if you guys feel this way, but there's that feeling of power when you first,
[2784.42 --> 2789.06]  like, really grok the language and you kind of get over, you know, you have to climb some mountains
[2789.06 --> 2793.38]  before you feel powerful in Perl. But, you know, once you get there, like, suddenly, like, the world
[2793.38 --> 2799.22]  is your oyster and you can just solve all sorts of problems very quickly. Yeah, I just don't think
[2799.22 --> 2804.50]  there's enough effort being, obviously, you know, I'm talking a lot about Rust, Go. These programming
[2804.50 --> 2811.46]  languages are very important, but they're targeted at kind of different use cases. You know, I love Rust.
[2811.46 --> 2818.10]  I would never start a new C++ project, as I said, but I'm not going to use that to rename a bunch of
[2818.10 --> 2823.86]  files on my folder. I'm just going to smash my keyboard for a while and write some JavaScript.
[2823.86 --> 2832.34]  Of the dynamic programming languages, JavaScript is the biggest. V8 is the fastest VM in JavaScript.
[2832.34 --> 2839.70]  It's the fastest dynamic language VM period. And JavaScript has this standardization,
[2839.70 --> 2844.82]  this industrial standardization process with it. It's tied to the web. So, you know,
[2844.82 --> 2849.62]  if you believe that the web is going to be here in a couple of years, JavaScript will certainly be
[2849.62 --> 2855.30]  here in a couple of years. It is as tied to the web as HTML is. So it's certainly not going anywhere.
[2856.02 --> 2861.22]  So, you know, if you're going to choose one of these languages to invest and build on,
[2861.78 --> 2866.74]  I think it's pretty clear that JavaScript is the language, ultimately, that we're going to be using.
[2866.74 --> 2872.66]  I think, you know, once you play around with this stuff a bit and you learn Python and you learn Ruby
[2872.66 --> 2877.86]  and you learn JavaScript and Perl, you get the feeling that they're pretty much the same thing.
[2878.18 --> 2882.18]  Like there's different syntax here. There's different ways to do different things,
[2882.18 --> 2888.66]  but they are very similar systems, essentially with, you know, different function names, different
[2888.66 --> 2895.62]  syntax. And yeah, I think those surface level features are fairly unimportant. And so,
[2895.62 --> 2902.50]  you know, I think JavaScript is really the one that we should be pushing to be using to push forward
[2902.50 --> 2908.98]  kind of the needs of the world to create fast software, create software quickly, I should say.
[2908.98 --> 2909.46]  Yeah.
[2909.46 --> 2910.66]  Bet on JavaScript, basically.
[2911.94 --> 2913.06]  Bet on JavaScript.
[2913.46 --> 2917.30]  One of the things you say in your mail too, and you kind of alluded to this a little bit was
[2918.02 --> 2922.90]  in the philosophy section of the introduction, you say, among other things, Dino is a great
[2922.90 --> 2927.70]  replacement for utility scripts that may have been historically written in bash or Python.
[2928.42 --> 2932.18]  I didn't really consider this, but that's pretty interesting too, because most often I'll reach
[2932.18 --> 2937.14]  for things like bash to do different things and on a file system or not too often Python,
[2937.14 --> 2941.54]  because I'm not a Pythonista, but I've definitely used bash before and I've used things in Ruby,
[2941.54 --> 2944.34]  like make and other things like that, you know?
[2944.34 --> 2944.74]  So, so.
[2944.98 --> 2945.30]  Rake.
[2945.30 --> 2945.70]  Rake.
[2945.70 --> 2946.02]  Rake.
[2946.02 --> 2947.94]  Isn't make and rake fairly the same?
[2947.94 --> 2949.38]  Isn't rake built on make?
[2949.38 --> 2952.02]  Well, rake is based off of make, but make is not.
[2952.02 --> 2952.42]  Yeah.
[2952.42 --> 2952.82]  Yeah.
[2952.82 --> 2953.86]  You just misspoke.
[2953.86 --> 2954.66]  Rake was what you meant.
[2954.66 --> 2955.14]  My bad.
[2955.14 --> 2956.58]  Rake slash make then.
[2956.58 --> 2957.46]  Thank you for correcting me.
[2957.46 --> 2958.02]  Sure.
[2958.02 --> 2960.98]  You know, being able to do that kind of thing where, you know, you're betting on JavaScript,
[2960.98 --> 2965.62]  not too often you do those kinds of things like scripts like that with JavaScript,
[2965.62 --> 2971.06]  maybe for its lack of ability to have secure access to the runtime or, or the system
[2971.06 --> 2972.18]  and file system and whatnot.
[2972.18 --> 2972.58]  Yeah.
[2972.58 --> 2978.02]  I mean, bash is another dynamic language, you know, one that starts a sub process for
[2978.02 --> 2983.78]  every statement in your program, but generally you would use bash because it's widely available
[2983.78 --> 2986.10]  on all of the different systems that you're running on.
[2986.10 --> 2987.62]  It's very portable.
[2987.62 --> 2988.90]  It's not a great programming.
[2988.90 --> 2991.46]  I don't think anybody loves bash as a programming language.
[2991.46 --> 2992.26]  It's pretty hard.
[2992.26 --> 2992.42]  Yeah.
[2992.42 --> 2993.22]  Yeah.
[2993.22 --> 2998.50]  I regularly access documentation to confirm my syntax is correct or just car called.
[2998.50 --> 2999.14]  Just car called.
[2999.14 --> 3000.42]  That's sometimes easier.
[3000.42 --> 3001.62]  Copy and paste, you know?
[3002.18 --> 3003.30]  There's lots of it out there too.
[3003.30 --> 3003.38]  Yeah.
[3003.38 --> 3004.18]  So it makes it easy.
[3004.18 --> 3004.58]  Yeah.
[3004.58 --> 3004.74]  So it makes it easy.
[3004.74 --> 3008.98]  There's probably a subreddit somewhere where there's, you know, people who just love bash
[3008.98 --> 3012.66]  and it's like their thing, but they're a, you know, they're a rare bunch for sure.
[3013.46 --> 3017.70]  Now, like you said, if you take all of the scripting languages together, I agree with you.
[3017.70 --> 3019.70]  I've done Python, Perl, Ruby, JavaScript.
[3019.70 --> 3024.58]  The more you learn, the more you start to realize they have their own idiosyncrasies.
[3024.58 --> 3028.74]  They have their own view of the world, but they're all kind of in the same ilk.
[3028.74 --> 3038.58]  And I would tend to agree, even though Ruby's my first love, that JavaScript is the one to bet on because it's already ubiquitous.
[3038.58 --> 3039.46]  It's in the browser.
[3039.46 --> 3043.06]  It's used pervasively server-side now, thanks to Node.
[3043.94 --> 3047.06]  And it is definitely not going anywhere.
[3047.70 --> 3052.58]  So you've picked that as your place to build and to create.
[3053.46 --> 3055.14]  And you want to do this into the future.
[3055.14 --> 3057.06]  This is an ambitious, big project, right?
[3057.06 --> 3061.90]  So you've started a company around it, which is different than what you did with Node.
[3062.54 --> 3063.66]  That was a long time ago.
[3063.80 --> 3066.88]  Why don't you tell a little bit of what went down the first time when you created Node?
[3066.88 --> 3069.24]  What happened with you?
[3069.36 --> 3071.44]  I know you had a full-time job, et cetera.
[3071.52 --> 3072.64]  Things are different with your life.
[3072.90 --> 3073.72]  There's a company now.
[3073.78 --> 3074.72]  This is different than Node.
[3075.00 --> 3077.24]  Can you just compare and contrast the two situations for us?
[3077.78 --> 3077.96]  Yeah.
[3078.22 --> 3081.90]  I was much younger, obviously, when I started Node.
[3082.18 --> 3088.02]  Shortly after starting it, I took a job at Joyent where they said, come work for us.
[3088.02 --> 3091.70]  You can continue working on this project, which seemed like a great deal.
[3091.70 --> 3097.58]  And I moved from Germany to San Francisco and continued building Node.
[3097.78 --> 3111.84]  And kind of throughout 2009, 2010, first part of 2012, when it became more and more clear that Node was really a thing, Joyent sat down and made a business deal with me.
[3111.84 --> 3120.20]  And I ended up selling Node to Joyent, whatever that means when it's an MIT-licensed open-source project.
[3120.38 --> 3125.20]  But I gave them control of the project and gave them the website and whatnot.
[3125.40 --> 3128.80]  That worked out very well for myself, personally.
[3129.16 --> 3131.94]  And I'm not sure how well it worked out for Joyent, actually.
[3132.12 --> 3133.12]  For myself, it was great.
[3133.40 --> 3140.64]  I've seen some comments online that kind of paint a different picture of the situation that was exploited by Joyent or something like that.
[3140.64 --> 3141.22]  I feel that at all.
[3141.34 --> 3142.30]  Not at all the case.
[3142.92 --> 3143.38]  Well, that's good.
[3144.02 --> 3146.04]  So after you left Joyent, what did you do next?
[3146.18 --> 3148.32]  I know you're doing research and development at some point.
[3148.44 --> 3150.12]  But did you have a job after that?
[3150.16 --> 3150.98]  Did you take some time off?
[3151.54 --> 3152.66]  I took some time off.
[3152.66 --> 3155.38]  I worked on some other projects that were unsuccessful.
[3155.80 --> 3159.46]  I worked for a while at Google doing machine learning stuff.
[3160.46 --> 3170.44]  It was, I think, 2018 that my collaborator in Node, Burt Belder, who founded the company StrongLoop,
[3170.64 --> 3174.20]  was, so Burt's journey is also interesting.
[3174.64 --> 3182.50]  He was an early contributor to Node and did one of the most important refactors in Node early on.
[3182.50 --> 3185.96]  Early on, Node only worked on Mac and Linux.
[3186.62 --> 3188.58]  And we wanted to port it to Windows.
[3189.42 --> 3193.00]  And, you know, Node is doing all this asynchronous I.O.
[3193.00 --> 3199.52]  And so it uses ePoll and KQ, these non-blocking sockets.
[3199.78 --> 3207.90]  These are fairly intricate, not well understood operating system APIs that differ from operating system to operating system.
[3208.04 --> 3210.82]  And in particular, on Windows, it's completely different.
[3211.40 --> 3215.00]  Their non-blocking I.O. system is called I.O. completion ports.
[3215.00 --> 3219.76]  And we wanted to do a very proper port to Windows.
[3220.04 --> 3227.24]  We wanted to use I.O. completion ports so that Node would work as a native proper program on Windows.
[3227.82 --> 3230.22]  And this was a massive undertaking.
[3230.54 --> 3232.74]  And Burt led this effort.
[3232.98 --> 3234.84]  We collaborated with Microsoft on it.
[3235.28 --> 3237.02]  It took probably a year.
[3237.28 --> 3240.06]  But at the end of the day, Node works on Windows.
[3240.26 --> 3242.10]  In fact, Node is very well supported on Windows.
[3242.10 --> 3243.60]  And it's very fast.
[3243.70 --> 3245.98]  I don't think people run servers on Windows too much.
[3246.08 --> 3248.26]  So maybe it doesn't matter how fast it is on Windows.
[3248.64 --> 3252.16]  That was a very successful, massive undertaking.
[3252.68 --> 3258.32]  As I said, Burt went on to found this company, Strongloop, that did Node-y sort of things.
[3258.54 --> 3260.02]  Built some products on top of Node.
[3260.52 --> 3265.20]  They sold that to IBM, I think, in 2015 or so.
[3265.20 --> 3273.52]  And around 2018, I left Google and Burt wanted to leave Strongloop and our IBM.
[3274.04 --> 3276.28]  Yeah, we teamed up and started working on projects.
[3276.54 --> 3282.02]  I already mentioned this TensorFlow in Node project that we were originally working on.
[3282.44 --> 3286.78]  But we just had the idea to kind of poke around for a while and see what we could do.
[3286.78 --> 3302.00]  So after you conceived the idea of Dino and maybe you had a prototype or you had maybe even you had announced the project, was the Dino company right there in your guys' minds kind of like, okay, here's a path forward from then?
[3302.10 --> 3306.60]  Or is that a newer conception that you came up with later?
[3306.60 --> 3313.18]  So early on in Node, as I mentioned, I was young and naive about how software is developed.
[3313.70 --> 3318.84]  You know, I was very much of the idea that, oh, you know, you just throw some code out there on the Internet.
[3319.12 --> 3320.48]  You collaborate with people.
[3320.72 --> 3322.36]  This is how software gets built.
[3322.86 --> 3329.50]  But, you know, Node grew bigger and bigger and bigger and there's more and more people involved.
[3329.70 --> 3334.64]  And it becomes clear at some point that organization really matters.
[3334.64 --> 3340.56]  It matters very much to have full-time professional engineers working on it.
[3341.22 --> 3345.90]  And, you know, people can contribute code, you know, kind of on a one-off basis.
[3345.90 --> 3354.06]  But if you really want to get things done, like port nodes to Windows and use I.O. completion ports, you need full-time engineers.
[3354.22 --> 3360.18]  These people need to get paid and they need to be able to focus on a problem for a long period of time.
[3360.18 --> 3376.08]  And so you realize that, you know, at a certain scale, software becomes a lot more about kind of managing budget and trying to manage an organization and kind of the meta problems around getting funding for people.
[3376.08 --> 3389.48]  And so it's always been clear to me that if we're going to go down this route and build this programming system that is going to be very much like Node, that if it's going to ever scale, it needs to have some funding model.
[3389.64 --> 3395.80]  There's no way that this can work where people are just going to randomly work on stuff on kind of a one-off basis for free.
[3395.80 --> 3400.60]  There needs to be some way of paying people to work on the problem.
[3401.52 --> 3408.94]  And, you know, Node is not a piece of software that is unused, that is not attached to revenue streams.
[3409.30 --> 3411.66]  There's all sorts of companies using this.
[3411.78 --> 3416.28]  If I could have one cent for every Node installation, oh, how great that would be.
[3416.94 --> 3421.30]  You know, this is open source software, of course, and it's very liberally open source.
[3421.30 --> 3426.50]  And I believe in that, and I think that's important for a programming system like this.
[3426.86 --> 3444.12]  But, yeah, we see that these systems have commercial applications to them, and these can provide connections to reality for the software itself that is making sure that we're actually solving a useful problem, but also provide funding to develop the software.
[3444.12 --> 3455.56]  Yeah, I guess we've known very early that we did not know if this project would go forward or fail, but we always knew that if it's going to grow, that it would need to turn into a company eventually.
[3456.28 --> 3458.62]  At what point did the company become the company then?
[3458.68 --> 3461.50]  I know you had the announcement in March, late March.
[3461.92 --> 3465.84]  You mentioned a sizable round of seed capital.
[3465.84 --> 3475.70]  You can name names if you'd like to, but at what point was that when the company began and the team of, you know, full-time expert engineers working to prove to happen?
[3475.86 --> 3477.60]  When did that, was it chicken and egg?
[3477.72 --> 3478.84]  You know, which came first?
[3479.58 --> 3484.26]  No, Bert and I, you know, first of all, worked on this ourselves for, I think, a year.
[3484.44 --> 3486.24]  So that was kind of our first investment.
[3486.24 --> 3490.94]  And I think we hired our first engineer in 2019 or so.
[3491.62 --> 3493.22]  And, yeah, we've grown from there.
[3493.36 --> 3495.22]  I think we're eight people now.
[3495.22 --> 3495.92]  Gotcha.
[3496.88 --> 3503.88]  So if there's a video game called Build an Open Source Business, and the first step is, you know, pick your license.
[3504.78 --> 3505.76]  You guys chose MIT.
[3505.96 --> 3509.02]  That would be like, you know, setting that video game on hard mode, wouldn't it?
[3509.14 --> 3510.70]  It's like, well, I want the biggest challenge.
[3510.98 --> 3514.36]  I'm going to let my software as free as you could possibly let it free.
[3514.36 --> 3519.76]  There's a lot of startups, a lot of businesses switching over to things like SSPL, AGPL.
[3519.76 --> 3527.48]  Any concern about, you know, AWS offering, you know, competing with you or the big dogs coming in and eating your lunch?
[3527.48 --> 3533.26]  Everybody's trying to kind of figure out open source companies and how to do this properly.
[3533.26 --> 3541.42]  And one model of doing this is the open core model where your open source software would be free.
[3541.60 --> 3548.42]  But then you kind of have an enterprise edition that you add on some extra nice features and you would charge for that.
[3548.42 --> 3563.54]  You can also kind of get into some licensing trickery where maybe you make your software AGPL license and, you know, kind of allow people to run this locally or kind of in non-commercial applications for free.
[3563.78 --> 3570.32]  But, you know, once you kind of get into the commercial realm of things, you are then asked to pay a fee.
[3570.32 --> 3577.24]  I think for Dino, this is a programming system that we're asking people to program against.
[3577.46 --> 3579.36]  We're asking a lot of our users, right?
[3579.40 --> 3581.82]  We're asking them to invest a lot in the system.
[3582.34 --> 3592.12]  And I personally would be very, very uncomfortable with programming using as the base layer of my, you know, this Dino sits below all of your other software.
[3592.42 --> 3598.12]  I would feel very uncomfortable if there was some weird payment hook at that layer of the system.
[3598.12 --> 3602.00]  It would prevent me from ever even trying out the software, in fact.
[3602.18 --> 3604.28]  And I think that's the case with Dino.
[3604.42 --> 3619.00]  If we tried to make Dino itself commercial and, you know, people are looking at Python and Node and Ruby as alternatives, I think many would choose the solutions to this problem that do not have a payment hook in it.
[3619.48 --> 3626.30]  We are pursuing a different funding model or revenue model.
[3626.30 --> 3632.38]  As I said, we think the software is pretty useful and we think it's useful in different commercial applications.
[3632.62 --> 3640.22]  I haven't mentioned it yet, but, you know, you know, you download it as this one executable, but it's actually a collection of software.
[3640.22 --> 3648.08]  And we've been pretty careful in breaking up this into different bits that we can recombine in different ways.
[3648.78 --> 3656.90]  And so we have a product that we've been working on for the last six months or so that is a different runtime.
[3657.06 --> 3659.24]  It is called Dino Deploy.
[3659.24 --> 3665.14]  And it has the same, a very similar API to Dino, a very web browser-y API.
[3665.50 --> 3669.50]  It's a JavaScript runtime, but it doesn't run on your computer.
[3669.72 --> 3670.66]  It runs in the cloud.
[3671.10 --> 3674.88]  You can think of it as a dynamic CDN if you want to.
[3675.16 --> 3679.94]  So we have processes running in 22 locations around the world.
[3679.94 --> 3685.76]  And we have an Anycast IP and you can provision a domain name on our system.
[3686.52 --> 3695.20]  And when you go to access your domain name, it resolves to this Anycast IP and that gets routed to the nearest data center.
[3695.38 --> 3699.18]  So, you know, if you're in Tokyo, it gets served locally in Tokyo.
[3699.18 --> 3705.12]  And rather than a CDN, which responds with static content, this invokes a JavaScript hook.
[3705.68 --> 3707.50]  So, you know, it is a serverless system.
[3707.84 --> 3711.72]  So, you know, think AWS Lambda or Cloudflare Workers.
[3712.24 --> 3716.16]  So it's a system for responding to requests dynamically.
[3716.50 --> 3722.88]  The best way to describe it is it's a web server, a multi-tenant web server with V8 built into it.
[3723.10 --> 3724.80]  It is completely a separate system.
[3724.94 --> 3727.90]  And this thing, AWS cannot, this is not open source.
[3727.90 --> 3729.28]  This is proprietary code.
[3729.86 --> 3732.08]  But it's still Deno in terms of the API.
[3732.40 --> 3734.10]  So I'm using Deno to develop.
[3734.34 --> 3735.26]  I can use it locally.
[3735.46 --> 3738.06]  I can deploy it on my VPS fine.
[3738.18 --> 3749.78]  But if I want to run it in this capacity where my users are in Tokyo, so my Deno process is running in Tokyo, then Deno deploy is just like, you know, a push away or a sign up away.
[3750.18 --> 3751.46]  It's a pretty cool idea.
[3752.10 --> 3752.52]  That's right.
[3752.64 --> 3752.76]  Yeah.
[3752.76 --> 3757.44]  You know, of course, you can take Deno, the executable that you download that's free.
[3757.90 --> 3760.52]  And you can wrap that up in a Docker.
[3760.52 --> 3767.42]  And you can send that out to AWS Lambda and kind of have a very similar experience.
[3767.62 --> 3770.14]  But that is not what we are doing internally.
[3770.14 --> 3773.58]  We are not running Deno in some Docker container.
[3773.88 --> 3776.92]  We actually are kind of using the VA isolate.
[3776.92 --> 3779.94]  We were talking about how this is a secure sandbox before.
[3779.94 --> 3791.00]  So instead of having multiple Linux VMs running for all of the different tenants on this web server, we actually have all of these little VA isolates running.
[3791.32 --> 3793.50]  And these, as we mentioned, are secure sandboxes.
[3793.50 --> 3799.36]  So we don't have to worry too much about hackers being able to see other people's requests and whatnot.
[3799.78 --> 3802.12]  And the nice thing about these is they're super lightweight.
[3802.12 --> 3805.30]  This is essentially like opening a tab in a web browser.
[3805.60 --> 3808.26]  So think of a web server with a bunch of tabs in it.
[3808.36 --> 3811.54]  And each of the tabs is for a different tenant on the system.
[3812.30 --> 3816.18]  And so we can respond to requests very, very fast.
[3816.48 --> 3821.66]  We have cold start times in sub, I think, less than 10 milliseconds.
[3821.94 --> 3822.98]  Not sure the exact number.
[3823.66 --> 3825.84]  And we do all sorts of nice optimizations.
[3825.84 --> 3828.82]  Obviously, it only runs JavaScript, right?
[3828.90 --> 3830.32]  This is not a Linux VM.
[3830.58 --> 3833.04]  So you cannot run your Python process in this.
[3833.40 --> 3845.36]  But because we've kind of taken this, because we've built explicitly on top of VA, we can make all sorts of very nice optimizations like Cloudflare has done to speed the response time.
[3845.70 --> 3851.02]  I think Amazon would have to be really motivated to do an Amazon deploy with a Deno repackaged.
[3851.28 --> 3854.94]  I'm not sure that's part of their business model to serve customers, but I could be wrong.
[3854.94 --> 3856.62]  You never know what they're going to do next.
[3856.92 --> 3857.74]  You just never know.
[3857.88 --> 3858.62]  You just never know.
[3859.08 --> 3865.48]  The liberally licensed, the permissively licensed, MIT, you know, open source, single binary collection.
[3865.84 --> 3867.88]  Sure, maybe they would do that, but I don't think that's their model.
[3868.48 --> 3880.84]  So I think your goal, though, is to provide Deno as it is to, I guess, to maybe solve some of the problems you didn't do well enough with Node and sort of live on those dreams you had with Deno.
[3880.84 --> 3886.98]  But then still have this commercially applicable ability on top of Deno.
[3887.08 --> 3892.12]  And you mentioned in your announcement for the company, we've been hinting at commercial applications.
[3892.66 --> 3895.78]  And so, correct me if I'm wrong, deploy is just one application.
[3895.78 --> 3898.86]  So applications of this infrastructure for years.
[3899.28 --> 3901.62]  What are some other ideas that you have that you can share?
[3901.72 --> 3905.42]  Is there anything you could tease or mention or early announce?
[3905.42 --> 3905.90]  Right.
[3906.76 --> 3911.30]  We're working on this deploy product, and that's the only thing we're going to be working on for the foreseeable future.
[3911.58 --> 3914.20]  But other applications would be, say, Electron.
[3914.58 --> 3925.28]  We think we could do a much better kind of GUI application framework than Electron has, given that we have Rust and that Deno is kind of broken up into these building blocks.
[3925.28 --> 3933.34]  Generally, there's all sorts of systems that kind of want little one-off JavaScript, little bits to be scriptable.
[3934.00 --> 3939.92]  And we think that there may be all sorts of kind of hidden use cases where people might want to have a Deno API.
[3940.32 --> 3944.64]  That is, and by the way, I should be explicit, like Deno is trying not to have an API.
[3944.92 --> 3946.90]  Deno is trying to be the web browser API.
[3946.90 --> 3955.48]  Deno is trying to not have a specific Deno API, but just if you want to encode a string into a UN8 array, you use Text Encoder.
[3955.82 --> 3958.92]  We don't have a special Deno API for that.
[3959.42 --> 3964.74]  But yeah, I think there's databases that may want to do, say, MapReduce with JavaScript.
[3965.42 --> 3968.18]  Potentially, there's some commercial application there.
[3968.68 --> 3972.32]  But yeah, I think for the moment, we're focused on this Deno deploy.
[3972.32 --> 3979.10]  The idea is that if you're writing a website, you write some JavaScript, you might run this locally with Deno on your computer.
[3979.40 --> 3983.94]  You know, maybe spin up a little local server to serve that front-end JavaScript.
[3984.44 --> 3993.56]  That kind of server-side code to assist you in writing this front-end stuff, or maybe any back-end code that you write, is also very web browser-y.
[3994.00 --> 3997.04]  It uses the same WebSocket APIs, for example.
[3997.68 --> 4000.22]  And so, you know, there's basically three different deployments.
[4000.22 --> 4007.98]  It's the web browser, front-end JavaScript, your local computer, where you're going to be writing some kind of server-side JavaScript, say.
[4008.16 --> 4011.72]  And then maybe you want to deploy that server and run it globally.
[4011.90 --> 4014.34]  So then you send out that code to Deno deploy.
[4014.78 --> 4017.98]  And by the way, you can take that executable and you can deploy it yourself.
[4017.98 --> 4022.64]  So you're in no ways, like, locked into using our Deno deploy system.
[4022.92 --> 4027.00]  But, you know, we're going to have the best way for you to deploy your Deno scripts.
[4027.76 --> 4029.42]  What's the state of Deno deploy currently?
[4029.42 --> 4030.62]  Is it in beta?
[4030.82 --> 4032.04]  I know people can use it.
[4032.14 --> 4032.64]  It's in beta.
[4032.88 --> 4034.88]  What is the state of it as a commercial product?
[4034.96 --> 4036.84]  Is it, it's not collecting funds currently?
[4036.96 --> 4037.92]  People aren't paying for it currently.
[4037.96 --> 4040.20]  It's sort of available to use.
[4040.36 --> 4042.44]  How do you plan to convert that into commercial?
[4043.06 --> 4043.92]  What's the current state?
[4044.28 --> 4046.28]  Yeah, it's in open beta right now.
[4046.66 --> 4049.48]  I would consider it a technology demo at this point.
[4049.58 --> 4053.78]  We're working on cool features that will be announced soon.
[4054.36 --> 4057.02]  Yeah, we will have a general availability announcement.
[4057.02 --> 4062.42]  We don't have a deadline for that yet, but we hope that it will be later this year.
[4062.94 --> 4065.92]  So, you know, we're kind of thinking in the six month timeline or so.
[4066.46 --> 4067.28]  But yeah, it's usable.
[4067.48 --> 4068.34]  People should try it out.
[4068.50 --> 4069.82]  It hooks up with your...
[4069.82 --> 4070.30]  Production ready then?
[4070.48 --> 4071.00]  Production stable?
[4071.00 --> 4072.90]  I would not know.
[4073.06 --> 4073.68]  Consider it that.
[4073.96 --> 4074.72]  He said usable.
[4074.92 --> 4075.80]  He didn't say production.
[4076.20 --> 4076.60]  Okay.
[4077.02 --> 4077.14]  Yeah.
[4077.22 --> 4078.56]  We have no SLA.
[4079.42 --> 4082.96]  So it's something that, you know, if you're interested, you should try it out.
[4083.08 --> 4087.58]  But I would not use it for production problems at this point.
[4087.58 --> 4093.90]  So if there's a future then for Dino, a place of competition might be with Deploy.
[4094.04 --> 4103.14]  Because if you claim here now that you intend for Dino Deploy to be the best way to run a Dino application, then that might be the way.
[4103.24 --> 4104.96]  If Dino wins like Node has won.
[4104.96 --> 4113.80]  And, you know, we haven't asked you if you plan for, I assume so, but if you plan for Dino to take over what Node is, to replace Node particularly.
[4114.26 --> 4124.34]  But if it becomes as big as Node has become and as usable as Node has become, then, you know, that's the place to compete with you would be on the deploy.
[4125.56 --> 4126.50]  I guess.
[4126.68 --> 4128.24]  I'm not sure what you're asking actually.
[4128.72 --> 4133.76]  Well, to deploy, you know, similar maybe for, you know, there's some examples for WordPress, for example.
[4133.76 --> 4138.22]  Like there's particular hosts that are like amazing at hosting WordPress.
[4138.98 --> 4147.14]  If Dino wins, it becomes very popular to gain market share, to have a commercially viable application or a company or a SaaS product.
[4147.26 --> 4151.22]  You might want to compete with you all to host Dino applications.
[4152.04 --> 4152.14]  Yeah.
[4152.22 --> 4157.90]  I mean, would encourage anybody who wants to also be running a Dino service.
[4158.08 --> 4158.44]  Yeah, sure.
[4158.58 --> 4160.94]  Ultimately, that's good for the ecosystem anyways.
[4160.94 --> 4168.32]  And, you know, Dino, the company, probably pretty good competitor when it comes to running Dino in these different contexts, right?
[4168.78 --> 4170.94]  So I think I would assume you're welcoming competition.
[4171.28 --> 4171.36]  Yeah.
[4171.48 --> 4176.94]  And, you know, by the way, we're investing a lot in kind of this Rust JavaScript infrastructure.
[4176.94 --> 4187.86]  And so, you know, when you go out and see products that are kind of serverless products that execute JavaScript and don't look like extremely node-y.
[4188.14 --> 4190.28]  So, you know, a lot of this stuff is actually node.
[4190.74 --> 4192.94]  But kind of newer server-side JavaScript APIs.
[4194.16 --> 4194.88]  Yeah, look carefully.
[4195.02 --> 4198.88]  It may actually be Dino or one of its kind of lower layers of crates.
[4199.26 --> 4199.28]  Yeah.
[4199.28 --> 4202.38]  We expect that and we encourage that.
[4202.66 --> 4204.48]  Yeah, this helps the ecosystem.
[4204.84 --> 4208.72]  Take me back to Dino Deploy for a second, just like thinking through it as an end user.
[4209.14 --> 4215.70]  And it seems like a lot of these serverless solutions don't have like the database story.
[4215.90 --> 4221.88]  When it comes to my backend, if I'm going to run all my code, my dynamic website at the edge,
[4221.88 --> 4225.90]  but my database isn't co-located with those edge nodes.
[4226.32 --> 4231.20]  It's like in New York City running on a Postgres server or whatever.
[4231.48 --> 4235.76]  It kind of defeats a lot of the advantages of having that locality of that runtime.
[4235.76 --> 4239.26]  Because most backends aren't just doing mere math.
[4239.74 --> 4243.10]  You know, they're like, yeah, there's some data stored in some place and they're going to go hit the database
[4243.10 --> 4245.64]  and they're going to figure it out and they're going to put stuff in, take stuff out.
[4245.64 --> 4250.72]  But is there anything with Dino Deploy that like co-locates a database or makes it so that
[4250.72 --> 4254.82]  my Dino backend has all the things it needs right there with it?
[4255.54 --> 4255.88]  Not yet.
[4256.02 --> 4260.24]  You certainly see Cloudflare going in this direction with durable objects.
[4261.12 --> 4268.80]  So, you know, right now Dino Deploy is kind of this, I would consider kind of the minimal viable product,
[4269.08 --> 4271.00]  which is that it responds to requests.
[4271.00 --> 4271.40]  There you go.
[4271.42 --> 4273.82]  So you can send back a response.
[4273.82 --> 4275.56]  You can make outbound requests.
[4275.56 --> 4280.76]  So, you know, let's say you have a Firebase database hosted by Google somewhere.
[4281.30 --> 4285.32]  You can make outbound requests to that data store for any persistent needs.
[4285.66 --> 4290.16]  We've basically pushed the persistence problem out of our problem space at the moment.
[4290.66 --> 4292.36]  And, you know, there are problems.
[4292.62 --> 4299.36]  Sometimes you just want a little redirect server and there's no need to have persistence in some applications.
[4299.62 --> 4302.22]  Obviously, many applications need persistence.
[4302.22 --> 4308.90]  And this is one of several features that we're looking at in kind of the coming months.
[4308.90 --> 4309.34]  Cool.
[4310.02 --> 4314.16]  So what happened with Node last time around, I referred to it earlier with Michael Rogers' reference,
[4314.36 --> 4317.24]  was that there was a lot of opportunity in the early days.
[4317.84 --> 4327.92]  And a lot of people jumped in and became influential, impactful JavaScript people because they helped out with the early days of Node.
[4327.92 --> 4333.60]  And this is potentially a new opportunity with this new round with Dino, where it's early days.
[4333.68 --> 4336.16]  You have core team.
[4336.32 --> 4337.82]  You have people doing stuff.
[4338.34 --> 4339.26]  There's a standard library.
[4339.34 --> 4343.16]  There's a lot more stuff that Dino has, I think, than that Node had when it first began.
[4343.26 --> 4347.86]  But the question is, if I'm a developer, I'm an open source person, and I'm thinking, you know what?
[4347.90 --> 4350.46]  I'm going to take a bet on Dino as an ecosystem.
[4350.46 --> 4352.38]  And I would love to be impactful.
[4352.60 --> 4355.96]  I would love to help out in ways that are big.
[4356.38 --> 4357.28]  What's the best way?
[4357.48 --> 4364.84]  What's the easy stuff, low-hanging fruit, or the real fertile ground for getting involved and being impactful with your code in the Dino ecosystem?
[4365.62 --> 4372.40]  I think the standard library is, we haven't talked about this that much, but in Node, there is no standard library.
[4372.56 --> 4375.00]  There's a lot of utilities built into Node itself.
[4375.00 --> 4387.38]  But part of the Node dependency problem is that when you just want a small little utility, when you want to left pad your string or whatever, you have to end up pulling in a third-party dependency.
[4388.14 --> 4393.28]  And in Dino, what we're doing is collecting all of the main useful things.
[4393.48 --> 4399.14]  And it's a bit ambiguous which things should be considered part of the standard library and which things shouldn't be.
[4399.28 --> 4403.42]  But in general, if a lot of people need those utilities, we put them in there.
[4403.42 --> 4405.26]  That's a very nice way to contribute.
[4405.60 --> 4406.50]  We have a style guide.
[4406.64 --> 4407.36]  We have tests.
[4407.84 --> 4410.32]  You know, it's something that affects the entire community.
[4410.58 --> 4417.76]  So if people contribute modules to the standard library, and obviously, people should ask first before randomly contributing things.
[4417.88 --> 4421.88]  It would be unfortunate if you did a bunch of work, and then we have to reject it for some reason.
[4421.90 --> 4422.44]  Right, where do you ask?
[4422.50 --> 4426.26]  This is a very useful way to be very useful in the Dino community.
[4426.56 --> 4427.66]  Where do those questions go?
[4427.74 --> 4428.88]  Is it issues on repos?
[4428.94 --> 4429.90]  Is it mailing list?
[4429.90 --> 4434.60]  Yeah, there's a Dino underscore STD repo on GitHub.
[4435.34 --> 4438.18]  And yeah, just open an issue and discuss it.
[4438.54 --> 4443.66]  But yeah, generally, we're very open to adding new libraries in the STD.
[4444.00 --> 4445.36]  Is the STD in Rust also?
[4445.50 --> 4447.00]  Or is that in TypeScript or JavaScript?
[4447.56 --> 4448.26]  That's in TypeScript.
[4448.60 --> 4451.16]  Yeah, these are utilities built on top of Dino.
[4451.16 --> 4460.22]  So obviously, you know, if people know Rust and want to kind of get into the internal system of Dino, there's a whole world there to explore.
[4460.48 --> 4461.78]  But that's a bit deeper.
[4462.36 --> 4463.32]  We have a Discord.
[4463.68 --> 4464.72]  You know, it's very active.
[4465.10 --> 4468.04]  And there's a lot of channels where people are discussing new ideas.
[4468.42 --> 4473.20]  And so I would encourage anybody to jump on there and hit me up with any ideas.
[4473.20 --> 4480.98]  Are there any particular applications out there currently leveraging Dino that you want to call out or that you've been impressed by?
[4481.96 --> 4482.82]  No, actually.
[4483.96 --> 4487.20]  Still early days?
[4487.88 --> 4488.84]  Still early days.
[4488.94 --> 4490.90]  I mean, people are playing around with stuff.
[4491.22 --> 4495.10]  And, you know, generally, this is the same, very similar system to Node.
[4495.10 --> 4500.08]  And so if you make a chat server, I wouldn't call that out as particularly interesting, necessarily.
[4500.46 --> 4508.06]  I think the interesting bits are kind of around the tooling and how we can make these workflows much faster for people and simpler.
[4508.50 --> 4512.50]  But the actual applications built on top are very similar in the end.
[4512.74 --> 4516.36]  Let's say I'm sitting on an existing Node app, which is medium-sized.
[4516.90 --> 4520.50]  And it's running a business, but it's not like 50 million lines of code.
[4520.88 --> 4521.94]  What would a port take?
[4522.00 --> 4523.04]  Or what would a port look like?
[4523.04 --> 4526.44]  Relatively straightforward, or are there serious dragons there?
[4527.04 --> 4532.46]  If it's already using ES modules and TypeScript, it should be relatively straightforward.
[4533.06 --> 4538.54]  If it's common JS and kind of old-school-style Node stuff, it'll be a bigger undertaking.
[4539.00 --> 4540.38]  Thanks for sharing so much, man.
[4540.40 --> 4541.86]  This has been very enlightening.
[4542.10 --> 4542.26]  Yeah.
[4542.38 --> 4544.74]  I really enjoyed it, and I appreciate you coming on.
[4545.02 --> 4545.20]  Yeah.
[4545.60 --> 4550.72]  I appreciate you making time in your schedule to finally do the podcast with us after so many years.
[4550.72 --> 4554.12]  And I guess we've never really invited you either, but sorry.
[4554.12 --> 4554.98]  No wonder you ever came on.
[4554.98 --> 4556.66]  It's been hard to get a hold of for the last 11 years.
[4557.20 --> 4559.98]  But I'm glad you made time to show up here at the ChangeLog.
[4560.02 --> 4560.72]  We appreciate that.
[4560.80 --> 4561.52]  So thank you, Ryan.
[4561.86 --> 4562.04]  Yeah.
[4562.10 --> 4562.76]  Thanks for having me.
[4565.14 --> 4565.74]  All right.
[4565.78 --> 4567.44]  That's it for this episode of the ChangeLog.
[4567.52 --> 4568.60]  Thank you for tuning in.
[4569.00 --> 4572.66]  We have a bunch of podcasts for you at changelog.com.
[4572.70 --> 4573.32]  You should check out.
[4573.56 --> 4574.58]  Subscribe to the Master Feed.
[4574.58 --> 4577.24]  Get them all at changelog.com slash master.
[4577.36 --> 4579.72]  Get everything we ship in a single feed.
[4580.12 --> 4584.10]  And I want to personally invite you to join the community at changelog.com slash community.
[4584.32 --> 4585.20]  It's free to join.
[4585.44 --> 4586.54]  Come hang with us in Slack.
[4586.76 --> 4588.94]  There are no imposters, and everyone is welcome.
[4589.36 --> 4592.40]  Huge thanks again to our partners, Linode, Fastly, and LaunchDarkly.
[4592.76 --> 4596.24]  Also, thanks to Breakmaster Cylinder for making all of our awesome beats.
[4596.62 --> 4597.74]  That's it for this week.
[4597.92 --> 4598.88]  We'll see you next week.
[4598.88 --> 4598.90]  We'll see you next week.
[4604.58 --> 4634.56]  We'll see you next week.
[4634.58 --> 4664.56]  We'll see you next week.
