**Jerold Santo:** Hello, JavaScript world. I'm Jerold, your internet friend, and the sound of those Break master Cylinder beats means it's time, once again, for a JS Party. Today I am joined by my fellow panellist, Ball. What's up, man?

**Kevin Ball:** Hey, hey. Glad to be here.

**Jerold Santo:** You, sir, are an independent businessman now, aren't you? Why don't you give us a status update? I know on New Year's you talked about that, and you've been doing it a little bit now... Do you want to tell us real quick what you're up to on your day-to-day?

**Kevin Ball:** Yeah, so I am -- and in fact, if you're listening to JS Party, you may have heard I'm even running an ad.

**Jerold Santo:** He is...

**Kevin Ball:** Talk about businessman...

**Jerold Santo:** Yeah.

**Kevin Ball:** But no, I've been coaching engineers and engineering managers, and it's been great. It's really fun to get to talk with folks, and work with them and help them improve... And you know me, I love geeking out with tech people... And here we're mostly working on like if you're stuck, how do we work you through a non-technical problem... But it's just fun. And yeah, I'm working towards a new podcast that I'm going to be releasing a while in the future, but I'm doing interviews, and I'm gonna start putting those out on YouTube...

**Jerold Santo:** Cool!

**Kevin Ball:** ...and working on all sorts of stuff. So it's good, but that's not the focus here...

**Jerold Santo:** No.

**Kevin Ball:** ...here in the JavaScript world. I'm excited to talk with our guest.

**Jerold Santo:** Yes, we have here with us for the first time - hopefully not the last time - Erick Wendell. Welcome to the show.

**Erick Wendell:** Hello! I'm so happy to be here. This is going to be great. We're going to be speaking about some low-level stuff, some research I was doing, and a lot of assumptions and studies I was doing here, trying to talk to people about how Node.js and how JavaScript actually works behind the scenes. So I think a lot of people, even beginners, will love this chat.

**Jerold Santo:** I'm excited to learn, because this is an area of expertise that I completely lack, personally. So I'm ready to learn from you, Erick. For those who don't know him - you are a Node.js core committer, keynote speaker, professional educator, you've got a great YouTube channel, a bunch of stuff online, helping everybody learn his wonderful world. And you're going to be speaking here soon at Beds Cone, which leads us into our regular segment, Holly.

**Jingle:** \[03:19\]

**Jerold Santo:** Holly at Beds -- how do you say it? B E JS? Bees? I've never had to say it before. The Belgian way of celebrating the JavaScript realm. It's a great conference, one I have not been to personally, but everybody who goes sings Omar's praises, who's one of the core organizers of this event. It's on May 12th in Brussels. Also, online. Erick will be there, and many other people as well. You can check it out at bejs.io/conf. Omar was kind enough to hook us up with a discount code for JS Party listeners. Use the code part-time for a 30% discount. That's for both real-life, meat space tickets, and online tickets. And he also gave us five free online ticket codes that we can give away. So we'll be giving those away to our JS Party channel in the community Slack. Join there, it's totally free; jsparty.fm/community, if you want to get one of those five free online tickets. So Holly at Omar and his friends at Beds Cone, coming up May 12th.

Erick, you're speaking at this conference... Have you been to it before?

**Erick Wendell:** Actually, I've been to Brussels... The best beer I've ever had.

**Jerold Santo:** Yes?

**Erick Wendell:** Actually, the biggest, I would say too... So I'm really looking forward to seeing more places. I've been there just for a day... But it's a pretty nice city. The environment, the people... It's very -- I like my country; people are very receptionists People really like other people, right?

**Jerold Santo:** Very cool. Well, I'm still excited to go there someday. I know Omar are still working on that behind the scenes. One of these days we will connect those dots and I will be there in the flesh. But if you can't get there in the flash, you can get there online, definitely do that. I highly recommend it. This has been Holly.

**Jingle:** \[05:16\]

**Jerold Santo:** Alright, let's dive into the nitty-gritty here. As you were saying before, Erick, you've done some serious research and put together a course, or some training materials, trying to figure out and teach people about JavaScript runtimes. Bun, Demo, and of course, Node.js, the one that I believe you have the most expertise with, teaching us how they actually work... And in order to do that, along the way, I guess, kind of like how you could recreate one for yourself, from first principles, or from scratch. So we would love to take up this topic. Of course, this will be part of your topic at the upcoming conference that you're going to speak at... Can you get us started? Maybe where you went down on this path, or what's the best way to teach people, to get us all on the same page about this topic?

**Erick Wendell:** \[06:04\] Well, I think the best thing about being a developer is because we get really curious, right? So I was trying to figure out some questions that were really hard to find on the internet, like "How is a database driver made? Who makes it?" or even how JavaScript works, or what is a runtime, or what is the difference between Java and actually Node.js behind the scenes?

So a lot of those questions I saw people actually complaining on the internet, and I saw a lot of theory about this... But in the end it was like "This doesn't seem right."

So I actually started contributing to Node.js, I actually solved a really nice bug there... But I felt like I just wanted to learn more about this tech, and I think I want to give a deep knowledge about this. So I asked actually ChatGPT back then, I was like "How is Node made?" So what do I need to make -- actually, I don't remember if I did the same research for ChatGPT back then, but I for the research now I was doing the same questions.

So it was pretty hard to find any resources about it... So I went to the Node.js on the v1 branch, when it was started back in 2009, and I realized the whole thing is, I would say, just - but it's not "just", right? It's too widely to say "just"... But it's a proxy for V8. I think that magic back then in Node.js was the ability to get a JavaScript string sent to a C++ layer, and you could bridge. So you can say "When I call console.log, actually I'm not calling -- console.log doesn't exist in JavaScript." Console.log is actually print on C++. And for me, I was like "Oh, my God."

So it's actually not JavaScript, it's other things. So I was searching the same way on Bun and Demo, and actually they follow the same rule. So this leaves out a lot of other questions, but in summary, something that actually blew my mind was like "Oh, actually the best language here --" We shouldn't make any friends here, or fight \[unintelligible 00:08:29.27\] because in the end V8 is the Chrome engine used as a proxy to execute functions. So this is fascinating for me, and actually this leads to the other subject, which is recreating React Native in other multi-platform applications that execute as JavaScript, but actually you can execute operating systems, or mobile-native APIs, only using JavaScript. But it's not JavaScript, right? \[Laughs\]

**Kevin Ball:** So can we break down a few different pieces? So what are we talking about when we talk about JavaScript runtime? There is how JavaScript the language itself is parsed and turned into executing instructions, and then there are the libraries or the functions that are built-in, which I think is what you're talking about in terms of the proxy layer... And then there's all the memory management, and that whole set of things. So which parts are in v8, and which parts are being implemented when you -- say you're a Node core developer; what are you doing there?

**Erick Wendell:** \[09:37\] Nice. So the whole thing here, I'm going to split in three different pieces. We have, I would say, the frontend. So we receive JavaScript code, we have V8 to interpret this JavaScript and make these C++ instances. So I would say "Oh, when I have a thread coming from the JavaScript language, I'm going to call it a thread on C++." So in the Node.js core my job today is we do some -- imagine that I'm trying to consume some file. In JavaScript, we cannot consume a file. We have the V8, which is the interpreter, and the runtime there that parses all this data, and actually calls another layer, the bridge, to call our operating systems, like Mac, or Linux, and other stuff. To call this file, we have the third layer, which is the Linux, that we can make async calls, and that's a lot of the runtime of Node.js.

I'm trying to summarize, because I know a lot of people got a lot of not-C++ previous background. But the point here, the whole goal of the Node.js here is if I'm a C++ developer, I know how to go in the core, I know how to save memory, to reallocate some variable, but I'm just a JavaScript developer. I know jQuery, I know a lot of form handling... So how this could be accessible - so via this bridge we can call "Oh, C++, just return for me the whole file buffer, which is the whole "storage" there, and I'm going to try handling this data on the JavaScript side. So I would say the Node.js is just some back and forth. I'd say "Please, operating system, give me some data", and then on the JavaScript side I'm going to write some algorithm to actually put in another layer, so the user can consume.

In the beginning, when you look at the Node.js core and how this stuff was working, actually they were exposing everything. Like "Oh, I want to say --" Like, I'm going to use the console.log. The console.log - we have the STDOUT to receive a data, or to actually throw some error. We have the STD error. So we were exposing these functions; we have like a C++ call that received that variable, and we were printing that.

So in the JavaScript side you're going to say "Oh, I'm going to use console. Something that is some function already declared on the C++ land." So everything that we have on Node.js right now is actually functions that were exported on the C++ side to make this thing.

This sounds a bit confusing when you just hear it, but when you're looking at the code, it's pretty straightforward. It's like "Oh, I'm going to call something in English that is going to make something easier from their side, but here in Portuguese is more accessible for me to handle this piece of data just using the language I already know, so I don't have to handle any memory.

But just to conclude about the V8 - in this case, all the optimizations that we have above the language, like for loops, the syntax, and everything, V8 is doing behind the scenes with the V8, with Google. So in my side, as a Node.js contributor, I barely touch the C++ side. I go on the high-level APIs, child processes, or strings, just making this back and forth, but receiving this data from the low level and trying to make the life of users easier.

**Kevin Ball:** Okay, so let me see if I understand, because this has kind of blown my mind a little bit.

**Erick Wendell:** \[laughs\]

**Kevin Ball:** Essentially, all the logic of how these different things are working is already implemented in V8. And what Node core is doing, and also what Demo was doing, and what Bun is doing, is finding ways to essentially take data structures that live in JavaScript, and functions that live in JavaScript, possibly mutate them a little bit so they'll work better in one way or another, pass them off to C++, get back what it responds, mutate it in a way that's going to make sense for the JavaScript caller, and pass it back up. Is that accurate?

**Erick Wendell:** \[14:12\] Perfect. Yes. So this leads to other questions, right? So this is just as simple as it seems. Why we have a lot of runtimes coming out - so what makes one more special than another is how they handle the data. So Bun uses now Big, which is a programming language that I've never seen before; it's even hard to read the docs, I don't know how Jerold was doing this... And they use the JavaScript runtime that runs on Safari, which is JavaScript Core. So they say that it's faster, but for me as a software developer it was pretty hard to try using this.

Just to get some vocabulary - Node.js, Demo and React Native and all this stuff, they are trying to embed V8. So this is one of the pieces of the puzzle. So when you are saying data, \[unintelligible 00:15:04.19\] but I was following a lot of the Bun and how it actually is affecting Node.js right now... And they say "Oh, we are consuming buffers, we are consuming strings, but if I put here -- like, I break this string the middle, I can send it faster to the user land."

So every runtime now is trying to adapt these algorithms to send data faster, and actually easier to the user, and safer to the runtime as well. This is mind-blowing for me.

**Kevin Ball:** And does that end up changing something about the user side API, and how people have to interact with data? Or from a JavaScript developer side it's plug and play, it's all the same, and all of this changing in how you're buffering or streaming data around is below the level that I'm worrying about?

**Erick Wendell:** Well, I would say it depends on each platform. We have ECMAScript right now. ECMAScript says "Oh, this you should have on JavaScript", so in terms of language. But about APIs, every platform would choose whatever they want. This is why we have the Winter Working Group, which is a working group for those runtimes to share knowledge and say "Oh, we built a new string API, which is faster than what is proposed from JavaScript. Let's try to implement them all and let's try to make this a path."

But I've seen -- like, Cloudflare workers I've never tried, but I've seen a lot of benchmarking people who are saying a lot of good stuff about them... But the worker threads, and a lot of internal stuff would be different, they would implement as they want. This is what I was talking to - oh, in Node.js we use print, but they could use Ruby, or they could use Rust to bring this differently, so they can implement whatever they want.

**Jerold Santo:** So let me see if I understand this correctly, at least with the big three that we know of. So Node.js is powered by V8. Demo is also powered by V8. And Bun is powered by JavaScript Core, which is a separate project altogether. And so V8 is maintained by developers at Google, and probably open source other people... JavaScript Core - this is a Safari thing; this is powered by Apple engineers, basically.

**Erick Wendell:** Sure, yeah. And it's pretty hard to embed I don't know how they did. The docs are very hard.

**Jerold Santo:** Right, sure. Okay, so that makes sense. And so you also mentioned another moving part, which is Linux, which you said allows for synchronicity. Is Linux then a separate thing from V8? Is it part of V8? Is it used by these other projects, or do they use something else?

**Erick Wendell:** Actually, V8 and Linux is a library that was made for Node in the beginning.

**Jerold Santo:** \[18:06\] Okay.

**Erick Wendell:** Everyone says "Oh, Node.js is not single-threaded. JavaScript is not single-threaded", but Linux makes this very powerful abstraction and Go thing. So it's an external library, so you can install it on C++. In this video I did you have to compile them all. I think both Demo, Bun and Cloudflare Workers uses Linux in the same logic. I'm not 100% if they are using this as well. But the good point here is we can schedule a test for the operating system. So every different operating system, they handle tasks differently. On Windows you can call threads from a way, you can create a new process in a way, on a Mac in another way, and so on.

So the Linux makes the process easier to make multi-platform of this. So you can call internal APIs for every different operating system from there. I'm talking this because you could actually use only C++ threads if you want, and handle \[unintelligible 00:19:16.29\] - there are a lot of crazy other concepts - by hand. But Linux makes this even easier to make everything.

So we have the JavaScript layer, we have the C++ that I usually call the controller, which is the intermediary between the C++, the Linux, and the V8. So we are sending a string from JavaScript to C++, the V8 parses this JavaScript string to C++ classes; we schedule background tasks, we schedule timers, threads, or whatever they want for the operating system. And then when the operating system finishes, it calls back the V8, it calls back our C++ functions, which calls back our JavaScript function. So this is wonderful for me how it was working. It's nice.

**Jerold Santo:** Yeah. It's a relatively thin layer. Now, there's a large API surface with Node and with these other runtimes. So while it's a thing layer, it's broad, meaning it has a lot of surface. And so that's why it's still a lot of work, right? You might wonder, "Wow, maybe Node isn't a big deal." Well, it's a lot of code, and a lot of surface area.

I did look up while you were talking... It seems that Demo is using Tokyo, which is a Rust package for Asunción, which is one of the differences between Demo and Node... So just trying to google while you were talking so we can --

**Erick Wendell:** Nice.

**Jerold Santo:** I know you're just going from memory. So okay... Ball, do you have thoughts before we move on this topic?

**Kevin Ball:** Yeah, I mean - I think it's a fascinating point of... So we've been talking a lot about the different -- there's just been a lot of buzz in the community that "Oh, Bun is so fast. It's doing this." And Demo was pushing this, and doing that. And that sort of mentality - these are places where there's a lot of competition and differentiation happens... It almost feels a little at odds with the view of these; they're thin proxy layers.

So I guess the thing that I'm trying to wrap my head around is what are the dimensions on which these different runtimes are competing?

**Erick Wendell:** I think there's a lot of gossip around this as well. But I think right now it's because Demo came, tried to help Node with a lot of other stuff we had, like package managing... Ryan Dahl was talking "Oh, this is something that we should change..." And I think the whole right now is because Node is so big - it's more than 10 years - that it's hard to like "Oh, let's introduce some breaking change." We don't have some freedom to implement more stuff. In Demo - "Oh, I'm gonna change from JavaScript to use TypeScript", so users could benefit of using more and more tools, and everything.

\[22:20\] But in my opinion, this movement, "Oh, let's create a new runtime", and all that stuff, it's because it's going -- I don't know if it's going to sound bad, but for the community it's a good hype that is pushing forward all the runtimes. Because of Demo, Node.js has been improving a lot in performance ways, in a lot of other approaches. But I have no idea how they are working, because it's not so -- we haven't seen any conferences; I think it's very small right now. But I think in the future we will not think about like "Oh, I'm using Bun, or I'm using Node." We're going to have a JavaScript runtime in every cloud. Because when we're talking about Rust and C++, they are a world of a difference, right? So we could easily make a mistake on C++, or forget some memory handling. In Rust, they tried to fix this by the approach of the language.

So for AWS, Google or Microsoft, I would say it should be easier to handle or to control these barriers when deploying these kinds of functions. So I would say they are trying to go to some standard, they are trying to make -- I would say the same thing, but they are pushing, like "Oh, I'm your friend. We are trying to run together", but in the end they are trying to compete, because there's space for everyone. But for me, at some point everyone's going to be just in one side, I would say.

**Jerold Santo:** Mm-hm. Yeah, if you look at the three that we're talking about, Ball, it seems that Demo is using -- okay, it's Rust instead of C++... But it's still V8 at its core. So it's using more similar things to Node, and really competing on API design, implementation details, the user experience, and performance, and those kinds of things.

Bun seems to be more of a desire to be a drop-in replacement for Node. So whereas Demo -- of course, they famously added support for NPM and stuff recently, but it didn't even have NPM support for a long time. So it's really much like a clean break. Whereas Bun is trying to be like "Hey, what if you just take your Node app, swap out that dependency of Node for Bun, and not change a single API call, and it's whatever-X faster, or more reliable", or whatever. That's Bun's goal, it appears, at least for now. And the way they're going about that is saying "Well, no V8. JavaScript Core. And no C++. Okay, we're going to use Big", which us armies can't even understand, for some reason; it's that hard, it's that cool...

In terms of what the competition looks like, it seems like those are the things. And it's really implementation details then that matter. It's like, "Well, we implement this using Linux and you don't. And Tokyo is better for these reasons, for this use case", and us users are just kind of like "Okay, I guess I'll wait and see the benchmarks, or which ecosystem has the packages I need." That's a pretty important part of it...

**Kevin Ball:** Yeah. And it's interesting what you're highlighting with Demo... The differences are not in the code you're writing so much. I mean, maybe a little bit, but it's the things around that. And particularly the security - I think I remember that Demo has an ability, similar to what actually the Kauri folks were talking about, where you can say "I only want to expose these system APIs", and therefore kind of lock down... Even if I'm pulling in NPM packages from wherever, I know that if I have not given file system access, it doesn't matter if somebody inserts some random file read over there, it ain't going to happen.

**Jerold Santo:** \[26:04\] Yeah, that is absolutely true. One of the downsides, or one of the bummers about that, Ball, is actually a lot like something you talked about a couple of weeks back with tree-shaking; we all got excited about tree-shaking, and then we realized that most of our apps need most of the code, most of the time... And you're like "Well, we tree-shook it, but not much fell out...", and that kind of was the reality.

**Kevin Ball:** You just give all the permissions, like the apps on the --

**Jerold Santo:** Well, with a significantly complicated Demo app, you're going to need all those things... And so because it's at the executable layer, and not package by package, which is just a constraint of the technology today - like, they just actually can't do it any more granular. There's people working on that with like shadow realms, that you kind of have to give it most of the things.

So at the end of the day, it's kind of like "Well, it's philosophically the opposite of Node", in regard to security specifically... But in practice - okay, for a very constrained application, then it's different; but for a broad, general web app or whatever that's doing lots of things, you kind of have to give it all those things anyway. So that's a bummer, but it's just where we are.

**Kevin Ball:** You're going to get the return of microservices, right? I'm going to separate my app, not because it makes sense for what I'm trying to do, but because it lets me pinpoint my security pieces...

**Jerold Santo:** Right, draw boundaries...

**Kevin Ball:** Draw boundaries.

**Jerold Santo:** Finally, a good argument for microservices... Nah, just kidding. \[laughter\]

**Erick Wendell:** And actually, there's a very good post about how James Snell actually wrote the article, speaking about the security and how Demo made... And actually, it's a very, very close point; like, "Oh, I know you can use a lot of this stuff, but in the end sometimes you want to fix this problem using some infrastructure around this."

**Jerold Santo:** Yeah.

**Erick Wendell:** So everything -- like, on VPCs, and all of this. It's rarely when you go to the application. But again, I would say Demo was only able to do this because they were beginning, and they have freedom to do this.

**Jerold Santo:** Sure.

**Erick Wendell:** In JavaScript, in Node.js, I think the runtime is a bit harder to touch this \[unintelligible 00:28:05.10\] so I don't know \[Laughs\]

**Jerold Santo:** Right. You know, I joke a lot about people who write modern software, because that's one of the selling points... Like, "This is a modern library." And really, what that means is you just didn't start it very long ago. You know, okay, it's modern because you just started it last week... But actually, Node has been out there, serving millions of users for many years, and continues to do so... And so it can't actually go modern in certain ways, because it has dependencies. And I'm not talking about NPM packages; like, actual real humans depending on it... And that's the luxury of new things; it's like "Yeah, we can start fresh, and we can drop all the old stuff..." And we need to do that in order to learn and grow and innovate, but you know, the big dog is still feeding the family, right?

**Kevin Ball:** Well, and you notice that as they start to go along, they discover "Hey, some of those things we thought we could drop, people actually care about them."

**Jerold Santo:** Right.

**Kevin Ball:** Like "Hm... Package management."

**Jerold Santo:** \[laughs\] Yeah, that's true.

**Erick Wendell:** That's one thing that I've seen people avoiding using, ECMAScript modules. ECMAScript modules for me is the next level of JavaScript, because now we can have this single file working on the frontend, on the browser, on the Node.js, in all those runtimes, with the same language and without, I like that. In Node, we have Required, but what if in Den owe could have another kind of import? So this for me is very game-changing for every application.

The bug I solved in the Node.js Core - it was actually because of this. Everything was working fine, we were using Common JS, we were using Require. But for me and for students that I've been teaching here, I teach everything, like trying to use the latest version, the latest JavaScript always, so I was always using ECMAScript. But the community is not so widely using this.

\[30:04\] So some things are breaking right now, but we haven't seen much impact yet, because people are not changed, because maybe -- either they are afraid, or it's close too much of TypeScript; I've heard these words, oh my God... \[laughter\] But yeah, for you who's listening, and you are not using ECMAScript modules, this is crazy nice for all your applications, because now it's truly asynchronous, now you can share your code without using Webpack, or other mediator to create and make that single culture run in different platforms.

**Break:** \[30:40\]

**Jerold Santo:** So if we're going to go back to the beginning a little bit - and I was going to ask you, Erick, as an interested developer, if I wanted to code up a Node.js from first principles, from scratch, what would my first few steps be? Now, I know step one could be "Go watch my YouTube video on how to do this", but assuming that we don't have that much time and detail, and you're audio-only, what would be starting point for people who are like "Yeah, I'd like to give it a try, even just to learn." What would they do?

**Erick Wendell:** The first step for me was trying to search examples on GitHub. I found some people trying to use V8, just get a string, parse it, and print out... But it was very hard, because we need the environment. We need to compile the V8, and the doc for me didn't work well. But I would say for technology or anything, I'm gonna start looking at -- right now, I'm going to go to the GitHub and search if someone is doing something.

So I would say the Node.js docs - it's very good teaching the whole lifecycle; so how JavaScript callbacks is handling... I would say even too much information sometimes. Like, we were talking about Linux, but actually, Linux doesn't matter much for us JavaScript developers, because they are heavy operating system, and if we touch that level, we should learn how the system works.

But I would say get individual piece... So "Oh, I know right now what V8 can do and cannot do." We don't have set timeout, we don't have set interval, we don't have set immediate Everything that goes outside, everything that goes asynchronous there, that's going to be executed in the future - it's not the paper of the V8 right now. Everything that is asynchronous in Node is Linux.

So now, in my case, I ran to the GitHub on the Node.js there, and I noticed that in the beginning Ryan Dahl wasn't using Linux. It was Libia, I would say, that only worked on Linux and in a few operating systems. That's why they built the Linux.

Once you learn the Linux, and once you learn the role of the V8, you start wondering, "Okay, how can I integrate them?" So you can use Rust, you can use other programming languages, but I would sometimes say we're going to feel a bit frustrated; it's not about the language, it's not about the APIs. It's making this whole environment. This is why we're \[unintelligible 00:34:16.20\] watch my video. Not because only the content, because I built the whole ecosystem for you on the Gitpod there, so you can just start using it right away; you can actually implement challenges, and other stuff. So yeah, learn every piece individually, and try and understand what you could do, and you cannot do in every piece.

**Jerold Santo:** When you say you built the whole environment on Gitpod, real quick... When you say that, what do you mean by that?

**Erick Wendell:** Well, I went there, I downloaded V8, and Compile, and got the binary. Linux - same thing. And now I'm sharing so everyone can code in the cloud, implement C++ code, and everything from that environment, and you don't have to worry about environment, which I severed at least a month to make this work. So it's crazy.

**Jerold Santo:** \[laughs\] Erick suffered, so you don't have to... Just go use his Gitpod. Ball?

**Kevin Ball:** Riffing on that for a sec, I think we as JavaScript developers sometimes forget how challenging it can be when you're building from source code in a compiled language, in a new environment... That in and of itself can be a month-long odyssey.

**Jerold Santo:** Right?!

**Kevin Ball:** So there was something you said that made me realize I was unclear on where the lines are of what V8 offers you. Because you said "Okay, you don't have set interval, you don't have set timeout", and it made me realize "Okay, what exactly is V8, versus something that Chrome, or Node, or whatever is providing?" And I'm guessing now it has to do with what's in the JavaScript spec versus what's a Web API, versus what... But is there a clean line that you can draw for us there?

**Erick Wendell:** \[35:55\] Well, we could go to the ecmascript.com website, in the docs... Like, look what are variables, loops, structures, classes... Promises. Oh, this for me was mind-blowing. For me, promises are async functions that can be used to notify you of something that's executing in the end. It's almost like this is not V8, because V8 cannot handle anything in the future. We actually have one which is 'Kill microtask'' but it's so specific that I don't mention it much. But there, in the end, a promise object is just a wrapper for a callback. So you just have an object that when the C++ calls you back, then you can have that object change. So that object lives on V8.

So as far as I know, I don't know everything, because I'm still learning a lot... And just a parenthesis here. To make this project work, I actually reached out to the Google team, I reached out to some Node.js developers, and they have no idea how to make this from scratch. So it was crazy. Crazy. So I actually found a guy who worked at the \[unintelligible 00:37:12.04\] with me, and he used to work at the Linux and V8. He joined me on a call and helped me out. So I made it work just because of him.

So I would say the limit for V8 is the language itself. I would say the syntax abstract tree I would say the cons how the interpretive variable, how functions it's being executed. And just it. Just it, It's a bunch of things, but it's hard.

**Jerold Santo:** Right. Does that help, Ball?

**Kevin Ball:** It does, and once again, it shines light on how large the Node project is...

**Jerold Santo:** Right, that's what I was saying. Surface area. There are lots of things that need it to provide.

**Kevin Ball:** There are a lot of things that need to be implemented; it's not necessarily just a simple proxy over to V8, right? Like, how do I deal with an async function, and dealing with that? Well, it sounds like the way you do that is you use Linux, and you call out to that layer of C++. But that had to be written. The original Node - that was part of the development. Now it's there, and we can just use it, but all of these things that -- I mean, this highlights an interesting thing... You start developing JavaScript, and even now, with Node, since it provides all this, the line of what's a language and what are functions that we have all kind of agreed upon, that are in a different spec, they're not part of JavaScript, even though everywhere you write JavaScript you could depend on them being there... Like, that's not something that most of us have in our heads.

**Erick Wendell:** Yeah. And for me, it was crazy... The V8, when you go to the docs, they have some tutorial there, and they say you can use D8. And it's like a shell code that you can try using the evil -- actually, it's... I don't remember anything, but yeah, it's on the console \[unintelligible 00:39:05.13\] and I was using Console.log. Console.log doesn't exist. What?!

**Jerold Santo:** \[laughs\]

**Erick Wendell:** So in this they implemented print, just to show you that it doesn't exist in V8. So it's... It's nice. It's wonderful how technology works. And this is what I talk to people - we should fight of technology, if P2P or JavaScript is better, because in the end C++ is the machine code doing everything for us... So we should learn how this thing works behind the scenes, so we can make our abstractions better, right?

**Jerold Santo:** \[39:41\] Right. It's just amazing, as JavaScript browser, frontend/backend, whatever we're doing, developers building applications for customers, libraries for our colleagues... - whatever it is, like how high up we are on the shoulders of the giants. We're so high up that sometimes you can't even see the ground, and we need somebody like Erick to come by and spending a month setting up the ground so that we can even stand on it... Which is really just a privilege, and I think speaks to the importance - even though we're standing on these shoulders, to be able to look down and see what's going on down there. It really makes it less scary. It demystifies, empowers us to build better, smarter... And so there's a reason -- even though you shouldn't have to learn this stuff, and I'd argue that for many people they never do, and they don't have to... But you will be a better developer, you will be a more confident developer if you can see how the parts underneath you are put together... Like, Ball and I are learning right now certain aspects.

So I guess it's just a sales pitch for this kind of content. I know that a lot of times when we're looking at continuing education for ourselves, it's like "How can I learn the next new framework, the next new CSS trick, or whatever it is, to make my apps better?", that's all well and good. But also, not just going out, but going down and learning what's underneath you is really empowering.

**Erick Wendell:** One thing that for me was -- I won't say the most interesting, because everything was like... I was like a kid in a kindergarten; I was like "This is so nice!" But the \[unintelligible 00:41:11.23\] because we were talking about Linux being single-threaded; like, how they handle the events, how they synchronize so we won't have any threading problem; like tread safe, and this kind of stuff... We don't usually speak when we're working with JavaScript, because the Linux handled this.

However, we should have some stars, right? Because I'm delegating some function, and this function is going to be started somewhere. But I'm talking about millions of users concurrently accessing that application, and this is being started somewhere. So I was like "Oh my God, so still this is fast, still they know how to handle memory..." It's so few people that know about V8, and this kind of thing, that usually it's the same person. When you go to the conferences, when you speak to people at V8, you see that it's the same 10–20 people that know how the thing works. So this is crazy nice, but it's still in my opinion, as an instructor right now, everyone should know, everyone should be able to help to improve this technology.

**Jerold Santo:** Yeah. The giants are tall, but they're also few.

**Erick Wendell:** Yeah.

**Jerold Santo:** And you find out, once you get down there you're like "Oh, V8. How many people are on the V8 team?" And it's like 6, or 8, or a dozen, but it's just not that many people, and it's like wow, these 6, 8 or a dozen people pretty much power everything that powers the ecosystem. So it's just fascinating how we go from the top end side of app developers, and users it's like millions; and then as you get down to the dependencies, further down, there's just like one lonely dev in Nebraska maintaining these things, for example...

**Erick Wendell:** And for you, who are watching right now - you may be thinking "Oh, maybe ChatGPT knows", right? No...

**Jerold Santo:** \[laughs\] ChatGPT doesn't know that.

**Erick Wendell:** When you go in there, and you try making specific questions about V8, they don't know; the code doesn't compile. And it's hard. Sometimes -- I always wondered how those people are maintained. I don't know, I don't have this information, but I'm not sure why these docs -- are these docs private at Google, or why it's not so public?

When you go to the docs, you can see the old docs that goes only on the signature. You see what is the input, and the output of the function, but what if you want to convert a function, convert an integer, a string to an integer? In my case - oh my God, I was searching at the tests. So I got to the whole thing I was searching, and said "Oh, maybe I see something how to use", because of the error that was showing to me. So it's pretty hard, but I don't know why this is not so accessible for everyone. Maybe there's no reason, but I don't know.

**Jerold Santo:** \[44:08\] Well, speaking of things that ChatGPT doesn't know... I just broke it yesterday. I asked a question, I was like "How do I do this?" It was like function parameters, blah-blah-blah. And it's like "Try this." And I looked at it and I thought "Oh wow, I didn't know you could do that. That doesn't look right. But I guess you can do it." So I went and copied and pasted it, and it broke. And I went back to ChatGPT and like "No, you can't do that. Here's what happens." And it says "Oh, I'm sorry about that. I messed up. Here, try this." And it gave me the exact same code. I'm like "Ohh, I've found a loop here. It's just going to keep telling me the exact same code, even though it's broken."

**Kevin Ball:** ChatGPT is an amazing technology in an even more amazing hype cycle.

**Jerold Santo:** Yes. The hype cycle is strong right now.

**Kevin Ball:** It can do a lot of really powerful and cool things, but it ain't AGI.

**Jerold Santo:** No. And we humans are very good at cherry-picking the best examples and putting them on social networks, so that we get lots of retweets and likes.

**Erick Wendell:** \[laughs\] But for me -- I'm curious, right? For everything. Like, oh, why is my webcam green now? I try to make a lot of questions. And sometimes these questions -- it's like 1 AM, so I go to ChatGPT, how to make a web driver from scratch. Right now I'm trying to do the same thing I did for Node, recreating Node, but I want to do on the mobile devices. So I was like "Maybe the idea is the same, but don't they use Linux to make this stuff?" I don't know, the mobile seems not so powerful in processing power, and this kind of stuff... And in the end, I was searching there... Every of those platforms, they are using C++, or byte code to make those bridges... So you can call native APIs from Android, from iOS, the same way we are doing on the desktop. So this is how native scripts, React and Native, they are doing behind the scenes. But again, I already like a week worked on this, and I couldn't set up the environment. This is so hard...

**Jerold Santo:** Oh, even harder, probably... Yeah. So that's your next video, is going to be how to recreate React Native from scratch, or what's it going to be?

**Erick Wendell:** Well, I wouldn't say the next, because I've already been spending a lot of time on this...

**Jerold Santo:** Sure.

**Erick Wendell:** ...but for these conferences I'm going to speak about recreating Node in a lot of conferences, and I would put it as like a plus. "Oh, look, you know how to make an input on your Android. This is how we can do the same idea." But it's a bit harder, because in my case I don't know Android, and I don't know iOS. And I'm not an expert on C++. So you can see a lot of bad practices on my code, because I'm just -- some people be like, try and find the answers. So this is a bit harder for me, but I don't give up easy.

**Kevin Ball:** I feel like that's actually a key to becoming a good developer, and to going deep in all of these things.

**Jerold Santo:** Yes.

**Kevin Ball:** It's like, once you get outside the domain you know, it's going to be hard. There's going to be dead ends, there's weird, esoteric knowledge that somehow has not made its way into the documents, or into ChatGPT, or into whatever else you're using to teach yourself. And you're going to get stuck for a while. And you've gotta not give up to easy, and keep banging your head, and try changing your question or your search phrase until you figure out what is the weird thing that somebody's documented in a blog post that wasn't picked up by whatever, that gets you past that barrier.

**Jerold Santo:** It's kind of like a video game... There are two kinds of video game players. There are the ones who get stuck, and they're like "This isn't fun anymore. I'm here to have fun. I'm going to move on." And I totally understand that, because that's logical. Like, if the goal is fun, and this isn't fun - why am I doing it? But then there's the kind of video game player that I am, where it's like "Oh, I'm stuck right here. My life is going to be hell for the next seven hours until I get past this level." And I'm just going to go over and over and over until I get past it.

\[48:08\] Sometimes I feel like programming has been like that, for me personally, where I'm like "I'm just stuck. I don't know my way out." This is pre-GPT tooling, pre-lots of helps... And I'm like "Well, it's me and the keyboard here. Let's bang our head on it until we finally figure it out." And it sounds like you've persevered through some of that yourself, Erick, in getting this thing out there.

**Erick Wendell:** Yeah. In my case there is always some voice here, there's a reason. Because why anyone hasn't done anything that you are trying to do, right? My video on recreating Node - there's no content on the internet; so this is why I'm building blog posts, making a lot of stuff, to try to get more people. But when you're the first, this is very nice. Like, "Oh, I was the first. Mad science." I actually implemented the WebSocket protocol using JavaScript from scratch, like binary data, and a lot of stuff, because I was making questions... And this is very nice when you reach the point. But the path - oh, my God. You think "I'm going to give up at some time." Your mind is like "No, you shouldn't do it. You have a lot of other stuff to do."

**Jerold Santo:** Right?! Well, I guess as a fellow content creator then, let me ask you a question about that. I guess all three of us here are people that create stuff for the internet... You had this video - we'll put it in the show notes; it's the one that we've been talking about the whole show. It's an hour and 25 minutes, it has chapters and stuff, it has all the things that a polished video should have. And literally, months of work, literally, before you could even start recording. When you're making something like that, do you ever just stop and say "What if nobody cares? What if nobody watches this?" I mean, you've done a great job; it has 123,000 views, so - massive success on that front. So that's amazing. It's got to feel good. But do you ever wonder, like "What if I put --" Because a lot of us do put things out into the world, and it's like "Meh..." And you're like, "Dang..."

**Erick Wendell:** It happens almost every time with me. But I sometimes noticed I try creating -- actually, right now I'm more trying to balance... This is content that I love to do; this is something that I really like doing. I know that's not going to be hype. This is actually my story here, producing content in Brazil. Everyone else is trying to teach beginners and intermediate developers... But I'm seeing a limbo. So from the intermediate to advanced, and especially, there's no one speaking... Because it's hard to put people in my marketing team to say "No, these guys didn't buy. Those people don't buy courses I was like "Let's try out." I wanted to check this out, I wanted to fail, but I wanted to fail fast.

But in this case of the recreating Node, it was something so interesting for me that even if it was only me, and I was like "Oh, mom, come here and see what I did!"

**Jerold Santo:** \[laughs\]

**Erick Wendell:** So this is kind of -- I remember being at a bar, having some caipirinhas, some drinks, and I showed the GitHub on my phone, and I'm like "Did you know that JavaScript doesn't have console.log? They don't have set timeout?" like a mad scientist.

**Jerold Santo:** This is like your opening line in a bar?

**Erick Wendell:** Yeah. So I would say I'm getting paid now to study, I'm getting paid to research, being a content producer. So sometimes we fail... I made a video asking how people create that code coverage, too. Is it from JavaScript, or how does it work? I published it; like, you can see the views. It's so low, but I actually don't even care. I know that this was the purpose, right?

**Jerold Santo:** Right. Well, that's the right attitude right there.

**Kevin Ball:** \[51:57\] Do you feel like you have a sense of when something's going to go or not? Because I was just talking to somebody about this, and they're like "Yeah, I had one that went really well. So now can I just take that?" I'm like "You know, every single thing that I put out there, I don't know if it's going to go or not."

**Jerold Santo:** Right.

**Kevin Ball:** And there have been things where I was like "This is going to go, this is going to go", and it's like... Nothing. And then I had things where I threw this out in response to somebody's question, and it took me an hour to write up in more detail, and I threw it up there, and it's still generating hundreds of page hits off of Google every day. And I'm just like "Really? That's what's going?"

**Jerold Santo:** Right.

**Erick Wendell:** I have a formula right now, that is every day I publish a text - it's like 2,000 characters on LinkedIn, and this is, I would say, like my school. So I publish there, and if it goes viral, like a thousand likes or more, I know this was a validated content. So from there, I actually push forward and I create a YouTube video. So when this goes viral on YouTube, I get this, and I publish a blog post and create a talk to submit at \[unintelligible 00:53:07.05\]

So the whole point for me is trying to fail fast. But as you said, sometimes -- I'm exhausted sometimes. We cannot be creative every day. So sometimes I'm like "Oh, I'm gonna just say whatever I had from some experience. "Five tips I suffer, you shouldn't suffer." This goes high. I was like "Oh my God." I didn't put enough energy there, and it goes viral. So sometimes it goes as we don't expect. I would say the constancy, and publishing every day is what makes our life easier.

**Jerold Santo:** Right. We can't control the outputs... Like, we can't control the results, but can control our inputs or our own personal outputs. So focus on both quality and consistency has been my formula... More than quantity. I mean, consistent with a quantity is a good thing... But just focus on doing things that you think are good, and have a thick skin when the thing that you really thought was awesome goes out with a dud... And just be genuinely happily surprised when things do manage to land. That seems to carry is through...

But it can hurt your feelings a little bit when you've put a lot of work into something, and it doesn't seem to do what you were hoping it does. I don't know if "hurt your feelings" is the way to -- just disappoint, I guess.

Okay, we're coming up at the end here... Any final thoughts, Erick, or Ball? Anything else we wanna talk about today before we call it a show?

**Erick Wendell:** Oh, just about this last piece... If you are thinking to build content, sometimes take a break. Don't push too much at the beginning, because it's so stressful. You don't make enough money sometimes; you get a lot of haters... As you are growing, and you have a lot of people saying "Oh, this is wrong, this is wrong, this is wrong", but you can see that the amount of the haters is very low compared to the people that you actually help. So educating people, and actually sharing what's in your mind would help a lot of other people. So this is really nice.

**Jerold Santo:** Well said. Ball. Last chance to say something before the show is over.

**Kevin Ball:** I love what Erick just said. Our tendency as human beings is to focus on the bad. So whether that's the piece that didn't go, that you just published and it was dead silence, or the one hater who's out there saying "This is wrong. This is terrible."

**Jerold Santo:** Right.

**Kevin Ball:** I think all of us - that's where our emotions get caught up, and it's easy to overlook all the people who read it and were like "This is great" and never said anything. But there's a lot of those out there. So yeah... And I think it comes back to the same thing you were talking about with development, right? Like, push through. Be stubborn.

**Jerold Santo:** Right.

**Kevin Ball:** \[55:54\] Dang it, I'm publishing for me as much as for anyone. And you never know... This is the last thing - you never know where someone impacted. I had somebody reach out to me a week or two ago, that was like -- he's an entrepreneur, he's had multiple companies, and he said "I don't know if you remember me, but I share your blog post from a decade ago with every company that I work with. Would you like to reconnect?" And I was mind-blown. I didn't even know if that blog post is still alive. It was on an old site... It's that old. I had no idea. And you have no idea which of the things that you wrote changed somebody's trajectory, and they are going off -- or you recorded on YouTube, or whatever it is. But it does happen. People see your stuff and it can change their lives. So don't stop writing, or publishing, or whatever it is because of some hater.

**Jerold Santo:** Yeah. Just to pile onto that... I would say celebrate your wins, no matter how small, even in development. You get past that one thing, celebrate that win, whatever that looks like for you. Maybe it's just a step back and play your favourite song, or maybe you're going to go out for a beer, or ice cream, or maybe you're going to take a day off... Whatever you're going to do. But celebrate those wins, because they really do power you through the downward parts, the struggle. It is toil, both when we're talking about software development and content creation, and really anything that you do in life that's worthwhile, it's going to have some toil... And so if you can celebrate those wins, the big one, the small ones, then you can kind of get through the doldrums on the other side.

Speaking of doldrums... We're coming to the end of our show; it's beginning to tail off. Erick, where is the best place to connect with you on the internet?

**Erick Wendell:** Well, I would say follow me on LinkedIn. LinkedIn is the best one. But if you want to chat directly with me, maybe Twitter, because I reached the friendship amount there, and I have no idea how to delete, and LinkedIn is so messy for this... But Twitter, or Instagram... I'm very accessible, but I'm busy as well, so don't be sad if I take like a week to respond, because it's been crazy; you see, the content is crazy... But I always try to give some advice. And actually, sometimes I don't know the answer, but I know how to link to other people as well.

**Jerold Santo:** Very good. And if you want to see Erick in the flesh, and you happen to be in and around Brussels in May, check out Beds Cone. One last shout-out to our friend Omar, and that conference, which I've heard only good things about, which as a conference organizer I know feels good... Because they have the same struggles as content creators have, as well as that one hater who leaves the bad review... Don't be that guy or gal; don't be that one hater.

Anyway, let's call it a show. Erick, I appreciate you coming on. Ball, I always appreciate you. I'm Jerold, this is JS Party, and we'll talk to you on the next one.
