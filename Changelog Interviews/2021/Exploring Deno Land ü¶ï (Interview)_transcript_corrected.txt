**Jerold Santo:** Well, we're here with Ryan Dahl, creator of Node, creator of Demo. Ryan, we're big fans of you, and we're so happy that you're here on the show.

**Ryan Dahl:** Hello. Glad to be here.

**Adam Staravia:** I think this is a first.

**Ryan Dahl:** Yes.

**Adam Staravia:** You've never been on the Changelog before, even back in the day.

**Ryan Dahl:** Nope. Never been.

**Adam Staravia:** We've only talked about Node, not about the creator of Node.

**Jerold Santo:** Yeah, we've talked about Node, we haven't talked with the creator of Node. What a shame. Here we are to fix that.

**Adam Staravia:** Well, ten years later, is... Welcome.

**Ryan Dahl:** Thank you. I think this is only the second podcast ever I've done.

**Jerold Santo:** Oh, wow.

**Adam Staravia:** Is that right? Well, thank you for giving us part two of that.

**Jerold Santo:** That's right, we're honoured. So you're not here to talk about Node, you're here to talk about Demo. You've rearranged the letters; you've been hard at work for a couple of years now... And I would like to go back to your Scoff EU talk, which has become famous now, in 2018, the ten things that you regret about Node.js... Which turned out not being ten, it seems like. I don't know if you've named it that, or they've named it that on the YouTube file... Because it was like seven, and then you introduced Demo... And I was going through it, trying to find--

**Ryan Dahl:** They named it that, yeah. It was not ten... \[laughter\]

**Jerold Santo:** Yeah, that's just the way they named it on YouTube. I don't even think your slides said that.

**Adam Staravia:** They were like "One, two, three, four, five, six, seven... That's close enough to ten. We'll just call it ten."

**Jerold Santo:** Yeah. Round numbers and lists apparently work on the internet, so... \[unintelligible 00:03:04.01\]

**Ryan Dahl:** Yeah. If you go to the title -- if you look at that talk and see the title slide, it has a completely different title. It's not "Ten things I regret about Node."

**Jerold Santo:** Well good, because you had seven of them... And it seems like that was a talk that was put together somewhat last-minute, maybe because Demo wasn't quite as far along as you hoped it would be, or what was the back-story on that? Because even in the beginning you said "This wasn't my talk, but now it is my talk." Was that the thing, is Demo wasn't quite ready to give more of a fleshed out version of it?

**Ryan Dahl:** Yeah, I was working on a different project, and I had applied to give this talk on this other project. It was something very similar to TensorFlow.js. So it was TensorFlow binding to Node, so that you could train machine learning models in Node... Plus something that's like Python's Jupyter Notebook, or in JavaScript there's this Observable company...

**Jerold Santo:** Yeah.

**Ryan Dahl:** \[03:58\] ...like a website where you could insert a bit of code and plot functions, and stuff. TensorFlow.js and Observable actually came out just before that talk, and... A month before that we decided "Actually, these projects are kind of dead-end. We should do something else." And Scoff insisted that I continued to give a talk on something else, so I put together this Demo demo.

**Jerold Santo:** Nice. So there's a bunch of stuff about Node... Anytime you make design decisions, in retrospect, it's easy to look back, and it's hard not to find flaws in things that we create... But we don't always get a second shot at it, and Demo seems to be, to a certain degree, a second shot, or at least another round of something different, but similar... And I'm just curious, of the seven or so things there that you listed - which, if you don't remember, they are not sticking with promises, the security system (which I think you definitely are addressing with Demo), the build system, packaged JSON, Node modules... Those are a few things, just high-level, that you mentioned, that were regrets. How many of those do you feel like you've alleviated with Demo? How many things did you fix?

**Ryan Dahl:** I mean, all of those things, I think. Generally, Demo is an effort to move the server-side JavaScript platform forward in kind of radical steps. Node has a lot of users, of course, and they try very hard to maintain backwards-compatibility, which is laudable and great for all the users of it... But that means that it's very slow in taking on new changes. And I think the major change in JavaScript over the last couple of years - maybe two major changes are async/await syntax and the ES modules syntax; these are pretty radical changes to the language. And JavaScript is like this evolving system over time. The JavaScript of today is nothing like the JavaScript of 15 years ago... And yeah, it just felt like Node was not keeping pace with web browsers in terms of bringing these new features.

**Jerold Santo:** So now you're a few years into Demo... We've hit 1.0 last year. Lots going on, lots formalizing... I'm wondering now, since you've gotten into the weeds for a couple of years, and you look back - have you made any mistakes so far? You had seven or so of Node that you regretted... Any regrets with Demo yet?

**Ryan Dahl:** Yeah, definitely. I mean, it's hard to make software and not make mistakes, of course...

**Jerold Santo:** Totally.

**Ryan Dahl:** This is going to be very controversial, but the TypeScript aspect of Demo - Demo has TypeScript compiled into it - is super-nice, very friendly, very nice to be able to just get up and started easily. But browsers do not support TypeScript, and Demo's overarching philosophy is bringing server-side JavaScript closer to browser JavaScript. And in this aspect of supporting TypeScript out of the box, we are kind of overstepping our goals. So we're supporting this extension to JavaScript.

I don't know about you all, but I feel like TypeScript is eventually what JavaScript is going to be. I feel like it is kind of the next generation of JavaScript. Furthermore, I'm very eager, and I think many people are, to go in that direction. But it's a big complication to our system to support TypeScript, and I think weakens our argument that Demo is web-compatible.

**Jerold Santo:** Yeah.

**Ryan Dahl:** So we're certainly not removing it now, because Demo depends on it...

**Jerold Santo:** Right. Go back and start over, would you-- yeah.

**Ryan Dahl:** But yeah, I think it would have been easier for us to get started had we not supported that out of the box initially.

**Jerold Santo:** That being said, it seems like it was also a big draw and a big differentiator at first.

**Ryan Dahl:** Absolutely.

**Jerold Santo:** \[07:54\] Let me just say that I was around when you announced Node, back in '09 or whenever it was; I remember it was right around the iPhone time... And I remember the reaction to Node. Probably not as well as you do, because you were on the project, and I was just an innocent by-stander... And maybe you remember it differently, but to me, it was like immediate -- it was a hit. Everybody was excited. We had Micheal Rogers on the show a little bit back, and he was just reminiscing a little bit how nothing existed for Node. When Node came out, and you announced it, there was no ecosystem, there was nothing, and then everyone just piled in. People saw fertile ground... And you're looking at me a little weird, like maybe that's not how you remember it, but... It seemed like people came in droves to fill out that ecosystem. It just was immediately a hit. And I think it filled a real need. First, let me stop and say - did you have that same feeling, or am I seeing it through rose-coloured glasses?

**Ryan Dahl:** I think that's a fair characterization of what happened, yeah.

**Jerold Santo:** Yeah. Adam, you were around...

**Adam Staravia:** Yeah.

**Jerold Santo:** Node was huge immediately -- like, maybe not immediately, but people were very excited about Node, right?

**Adam Staravia:** Yeah. Well, I think there were a lot of things even like with Walmart Labs, and Black Friday... This wasn't back in the 2009 days particularly, but there was a lot of inertia around high-traffic websites, and scalability, and it's enterprise-ready, so a lot of different enterprise teams were happy to move on to something more modern... Despite these seven flaws, as you've described in your talk. Because I think every step forward is a good step forward, even if it's got some flaws, which - software has flaws every single time.

**Jerold Santo:** Yeah. So I guess my point is it filled a huge void, and it got a huge rush of enthusiasm and adoption because of that... And then Demo comes out, and it doesn't come out into that same moment in time. It comes out later, when you have a mature Node ecosystem, you have millions of packages on NPM. You have people doing this full-time careers, and consultants... I mean, there is a thriving Node ecosystem already. And so into that milieu, or that culture, Demo has to set itself apart, right? And TypeScript was one of the ways that it kind of did that to start. What were the other big ideas that Demo has that sets it apart from everything else?

**Ryan Dahl:** The first important aspect is that it's written in Rust instead of C++. Node is a very large C++ project, and I'm not sure how you guys feel about this, but I'm very convinced that I will never start another C++ project. Rust really solves the C++ problem, as it were. There are many great things about Rust, but the thing that is most important to me is the ability to have a single build system; this cargo system of linking together different Rust crates. In C++ there's no one defined way of how to take different C++ libraries and smash them together. Chrome has this GN project, Node uses this Gyp project, there's CMake... There's a lot of different tooling for compiling together dependencies in C++. And this ends up being a huge, huge complexity in terms of bringing in external third-party code into a big project.

In Node days, we built a web server, and you'd have to parse HTTP, and it's such a difficult problem that we ended up writing our own HTTP parser for this. It's so difficult to bring in external code that you end up often having to just write the stuff over again, because it's so difficult to link. And this is very different in Rust. If I need a YAML parser, if I need an HTTP server, any sort of third-party stuff, I would do what people are used to doing in JavaScript, or Ruby, or Python - you can just kind of include dependencies and have this all compiles together really nicely. And that's an important aspect for a platform like Demo or Node, because we provide all of these APIs to do various things. You want to open a WebSocket, you want to have an HTTP/2 web server - all these various systems that it talks to need implementations... And it's very nice that we're able to just link in third-party implementations of all these various systems pretty easily. So from a maintainer's perspective, rewriting it in Rust is a real killer feature that kind of allows us to iterate much quicker.

**Jerold Santo:** \[12:31\] Yeah, maybe kind of feature that end users don't appreciate as well as the authors or maintainers, but they will appreciate over time as you are allowed to continue at a certain pace that the C++ ecosystem didn't allow with Node. Or maybe at a certain point Demo will also get so many lines of code and so much stuff in it that -- I mean, it will slow down. Any project that's mature moves slower than when it's young. But maybe it'll keep a pace that keeps your users happy.

**Ryan Dahl:** Sure. Just talking about other aspects of Demo, internally, that are important, is the binding interface; kind of the boundary between JavaScript and the native language, in this case Rust, in Node's case in C++. Node was fairly ad-hoc at adding bindings; we just kind of added them all over the place. There was no set system for calling from JavaScript into C++ and vice versa... And in Demo there's a system for this. We call them ops. This kind of organizes the various bindings that you have to the system facilities really nicely... And in particular, organizes all the async calls that you might make. So ops in our system are either a synchronous function, like a function you call in to Rust, and it returns a value immediately, or it's an async function which returns a promise that eventually resolves to a value.

One of the really nice aspects in Demo is that everything is organized as promises. It's kind of promises all the way. There's no kind of random callbacks that happen throughout the system.

This was actually a pretty big design mistake. I forget if I did discuss this, or how much I discussed this in the talk, but WebSockets are on my mind right now, because we're doing a lot with WebSockets. WebSockets have this on-message callback, right?

**Jerold Santo:** Right.

**Ryan Dahl:** And one of the problems with this is that you can't really stop the system from giving you new messages. You can just get flooded with these callbacks. There's no way to throttle this incoming stuff. So because of the inability to stop these new messages coming in through this WebSocket, you can get into terrible situations where you're always handling the newest WebSocket message because you're getting flooded from this one socket, say. And this is not specific to WebSockets; this happens in different parts of the system.

That's quite bad... This actually causes pretty -- this manifests itself in bad tail latency situations, where usually the system is fine, except under pressure, when suddenly one part of the system is getting flooded with these callbacks, so you start getting really bad latencies.

WebSockets in particular - there's a new STDOUT called WebSocketStream, which addresses this, allowing you to create some back-pressure, that is to not accept the newest message if you're not ready to handle it. And in general, this async/await paradigm, syntax, and the usage of promises everywhere generally kind of solves this problem... Because as long as you're always giving these promises, and you're awaiting them, you're kind of stopped at a certain line. You're not kind of unboundedly accepting new callbacks from the system.

Anyway, that's all to say that Demo is promises all the way down, and so kind of from the fundamental layer we've tried to deal with this back-pressure problem.

**Jerold Santo:** \[16:02\] Another big differentiator is the package management story, right?

**Ryan Dahl:** That's right.

**Jerold Santo:** Tell us about how Demo sees the world of packages.

**Ryan Dahl:** Yeah, I would bring this back to -- in general, Demo is trying to use web APIs. We try not to introduce invented APIs, like I had to do in 2009 when I started Node; there were just a lot of APIs that were -- you know, there was no module system, so we invented this require syntax to link to JavaScript files together.

ES modules, ECMAScript modules is a standard now. This is part of the new JavaScript standard, which defines import and export. I'm sure you guys are familiar with it... And this works in web browsers these days. These imports and exports and ways to link different files together. And the way that this works on the web is you can actually do import a URL; not just a relative URL, but an absolute URL that exists on a different server. So you can actually pull in code -- you know if you think of like an HTML page and script tags, you can script source, have a link to https://jquery.org/jquery-v1.2.js

**Jerold Santo:** That's how we used to do it back in the day. We'd just have our script sources, and you'd just have your list of sources. Everything was so simple.

**Ryan Dahl:** Which is quite nice, right? It's really nice to have an HTML file and just drop in a link to the jQuery CDN and suddenly have that available without having to do a whole installation procedure, right?

Anyway, Demo is built around the idea that we think this is sufficient, actually, to link remote code together. I mean, the problem is really -- I've got code that I'm developing locally, and I really want to include some third-party library. How do I do that? In the Node system you would download that third-party code into a Node modules folder, and this requires system knows how to look into this Node modules folder. So when you do require express, it looks in the local directory Node modules, and then looks for the Express folder, and it has some special knowledge about looking up package.Jason, and looking up index.js... It has this algorithm of how to find what module you're referring to there. And we've basically done away with all of that. We've just said "If you've got code that you're working on locally, then you store that in your local folder, and that's yours to deal with." And if you want to link to some third-party code, you can of course download it into a vendor folder if you wanted to, and./relative-include/relative import that... But you can also just import the remote URL via HTTP.

Our module system is really the web browser's module system, which is exactly HTTP. So unlike NPM, which has a specific protocol for distributing packages, you have to ask the NPM server what the latest package is, get the link to the tarball, download the tarball... We don't define a protocol like that. We just have HTTP, and you can download JavaScript or TypeScript over HTTP.

**Adam Staravia:** What are the advantages of that then? If pulling a module for NPM, for example, the stability of being able to make those -- NPM install, for example, and being able to sit there and wait, like some people might, what are the advantages of that system over this older one? Obviously, it's modern in terms of the way the web browser is working, but what's the specific dev experience advantages there?

**Ryan Dahl:** \[20:02\] I think it has the effect of feeling immediate, and... There's nothing to install ahead of time, because the Demo system itself actually takes care of downloading that. So I would say the other DX effect is that you can have scripts that are single files. In Node, you generally at minimum need to have a package.Jason and your JavaScript file. Your package.Jason needs to define where you're linking, and your JavaScript file has some source code in it. In Demo you can say where you're linking on line one, and the rest of the script can be your code. So you can actually define a complete program, both where to get your third-party code, and your own code, all in one file, run it without creating a directory, and... I guess what I'm trying to say is there's less boilerplate to deal with.

**Adam Staravia:** It's minimal.

**Jerold Santo:** Yeah, it's simple.

**Ryan Dahl:** It's very minimal.

**Adam Staravia:** You can have file tabbing fatigue, or swapping from different files... I love that a lot -- in a whole different land, with Tailwind, for example, you can do a lot in the same file or in the same HTML file; you're not jumping back from CSS to HTML. So similar to how that world might work, you're not jumping back and forth. You can stay in the same file, have the sort of immediate/instant gratification of just moving forward, and not have to jump back and forth between different ways to define what your application is needing to inherit from, or to import etc.

**Ryan Dahl:** When you have a large application, if you have hundreds of files, having one extra package.Jason file is not a big deal. It's no big deal to have a -- you know if you have hundreds of modules, and you have one extra one, it's not a big deal. So I think in the tail end of larger projects, it probably doesn't feel that different. But when you get down to the very small scripts, the one-off scripts, Demo scales down to a much smaller installation, I would say. Much less boilerplate.

When you do NPM unit, it's going to ask you for (I don't know) the license of your project, the name of your project... All of that stuff is -- let's say you're trying to write a script that's going to rename a bunch of files in a folder. Who cares? I don't care what the license is. Why am I spending any time at all thinking about that problem? That is boilerplate.

**Adam Staravia:** Yeah. What about the potentially hidden advantage in it? I'm assuming this - the internet essentially is your package manager. You can link to a raw file on GitHub, you can link to some random site, adamstacoviak.com, or changelog.com and just inherit from that. Is that how Demo works? You can just pull in from any URL? Or as you'd mentioned, even a relative from somewhere locally?

**Ryan Dahl:** Yeah, that's right. You can pull in files from any server. And the nice side effect of this is that that Node ecosystem and essentially all other programming languages are dependent on a specific server to distribute third-party packages, whether that's crates.io, whether that's golang.org, or npmjs.com. If that server goes down, everything breaks. We are heavily dependent on that. But contrast that with -- this is just not very webby; this is not how web browsers work. It would be a bad day if Google went down, but hopefully web browsers continue to operate. Your website isn't necessarily dependent on any one specific server existing... And that's nice. That's a distributed system. And because of this aspect that you can download code from any URL, Demo is not dependent on our website, demo. Land, nor is it dependent on any other website. You can use unpackage.org for pulling in your third-party dependencies. Or you can use GitHub directly, which might be nice, since that's where the code is actually stored.

**Jerold Santo:** \[23:56\] Right. Then, if GitHub goes down, we're screwed again. But we're already screwed, so... Great website, by the way. I love the dinosaur brand, I love the name. Demo.land is such a cool domain. I just wanted to give you props for that really quick.

What about versioning? I mean, if I'm a library author, are there idioms around that? Do I just have a new file with like the version in my file name? How do we deal with things like "Lodash 3.7.1 is out. How do I go get it?"

**Ryan Dahl:** Ultimately, a version is a string of characters, and so is a URL... So you can have a version in a URL to specify the version. Think back to the jQuery CDN example - you have perfect ability to link to any version of jQuery.

**Jerold Santo:** Good answer. What about existing NPM -- are all the existing NPM packages then supported if I can find the exact URL of the source code? Will it just work? Or are they using some things that might not be ESM-compatible, and stuff like that.

**Ryan Dahl:** Yeah, so if it's not using ESM, then it's going to be probably problematic. It may be problematic even if it is using ESM. Unfortunately, we're kind of in a state right now in JavaScript where there's a lot of fragmentation between TypeScript, common JS, Demo, Node... I hate to contribute to that, but I also am (I feel like) fighting the good fight, trying to make things simpler. All NPM packages are available on, for example, unpackage.org, or Skyjack...?

**Jerold Santo:** Skyjack.

**Ryan Dahl:** So you should be able to access those files through HTTP. And if they're ESM, then you're close to it working. I think the problematic thing is if they use Node APIs. Node for example has requires. You can requires and open a file. Demo has alternative APIs for that. We do not have a top-level FS module. We have a compatibility layer for that. That's in our standard library. By the way, Demo has a standard library. And you can find that at deno.land/std/node. Using that compatibility layer, you get pretty close, although there are definitely a lot of modules where it's going to require some work... But you can get pretty close to importing a lot of modules. There's a long tail end of things that are incompatible though.

**Break:** \[26:25\]

**Jerold Santo:** So Ryan, on your website, demo. Land (awesome website) it says "A secure runtime for JavaScript and TypeScript", and of course, "Secure by default" is the top-level bullet of Demo features. We haven't talked about security yet. Do you want to give us the skinny?

**Ryan Dahl:** \[27:52\] Yeah, so obviously if you're pulling in random packages over HTTP, you should be worried if you're pulling in code, because maybe you've audited this code, but probably not. That code probably depends on some other code. And those can end up pulling in many dependencies.

**Jerold Santo:** That's kind of like those installers where they're like "Curl this URL, pipe it into Bash", and then a lot of people will show up in the comments like "Please don't do that, because Bash is going to execute arbitrary code that's in that URL." Anyway, I cut you off, but I just was reminded of that, where it's like, "Yeah, but as long as it's safe... Audit it and you'll be happy. But if you don't audit it, you probably shouldn't be piping into Bash."

**Ryan Dahl:** Unfortunately, it's really hard to audit all of your code these days. I mean, we depend on society-level infrastructure, right? There's no possible way -- if you plan to be a productive developer, to go out and actually read through all the dependencies and the transitive dependencies of your dependencies.

By the way, you're talking about curling Bash scripts - when you NPM install something, arbitrary code from the internet is running on your computer, without any security sandboxing. And beware, when you are NPM installing something, you are completely and utterly open to having your computer taken over. It takes one bad actor in the ecosystem to make that happen.

**Adam Staravia:** And we've seen that.

**Ryan Dahl:** We have seen that, yes. This is mitigated in web browsers. Web browsers do not allow you to access your local file system. They do not allow you to do a lot of stuff, right? Web browsers are a secure sandbox. And this is a really nice property of V8 and the JavaScript language, is that it does not necessarily have access to the system.

We, Demo and Node, give access to the system so that you can do things like writing a little script to rename a bunch of files. The purpose of a server-side JavaScript system is to interact with the system. But in Node, we did this without any constraints. We just opened all sorts of holes, so you can access the file system, you can access the network, you can do all sorts of stuff. There's no gating on those privileges. In Den owe're much more aware of opening holes into the system... And I mentioned earlier these ops and how Demo has a very centralized system for calling from JavaScript into Rust. By having this centralized system, we also have centralized gating for security.

So by default, when you run a Demo program, whether that's a local program on your computer or a remote program via an HTTP URL, it's given no access to the system. All it can do is compute; it cannot access your file system, it cannot open outbound connections... It can't do anything mischievous. It can calculate some numbers, it can print to STDOUT, but that's about it (which sometimes is all you want) to allow programs to -- in web browsers they have this system for opting in to more privileges. For example websites can access your webcam. But not just any website can access your webcam; it needs to elevate its privileges. So you get this little pop-up that says "Do you want to allow website x to access your webcam?" Demo is very similar. When you try to access the file system, it's going to fail if you don't have the privileges. And you can give it those privileges.

**Jerold Santo:** And you give it those privileges via command line flags, right?

**Ryan Dahl:** Via command line flags. You can do allow all if you want a Node mode... \[laughter\] There are no privileges, there's no gating. We have allowed to write, to write to the file system. We have allowed run, to run subprocesses. Furthermore, we have allowed read to read the file system. Furthermore, we have allowed plugin to load Rust plugins, which we can't assure are not going to do something nasty. Furthermore, we have allowed net for making outbound network connections, and allow env for environmental variables, which may often contain secrets.

**Jerold Santo:** Is that something you can put in the file itself, or does it have to be a flag to the runtime?

**Ryan Dahl:** \[32:13\] It has to be a flag. We are considering having a configuration file. We are really conservative about adopting new file formats. I was just talking about how we try to keep things as boilerplate-free as possible. So we don't want to force people to write a configuration file. We don't want the overhead of configuring your system before you ever get started.

So for now they are command line flags... And they're pretty obvious and annoying, and that's kind of purposeful, because these are security things. They should be obvious and annoying. You should be very clear that you are allowing this system to run arbitrary sub-processes. Yeah, so via command line flags is how you enable them.

**Adam Staravia:** How often are those flags being used by general applications you see being built?

**Jerold Santo:** All the time.

**Ryan Dahl:** All the time. I mean, it depends on what you're doing. Let's say you're writing a program like ESLint - this ESLint-like program doesn't need to make outbound network connections. It doesn't need to write to the disk. All it needs to do is read from the disk. So you would only enable the allow read in that case.

**Jerold Santo:** Yeah, so I was telling you during the break that I was writing this little script with Demo the other day, and basically it went out to the Slack API, got some data from there about members of our community, and then looped over -- I was trying to pick a random winner for a giveaway, from a certain channel from one of our Slack channels... And then it picked a random three or something, just printed them out. A very simple use case. And I had to use allow net, obviously, because I'm hitting the Slack API; and then I also had to use allow env, because -- I could have just hardcoded the token into the script, but I just used it as an environment variable. And I can say from a person who's just trying to get stuff done, it is kind of annoying. You're just like "Aright..." You know? I didn't know about -all. I would have just used that. But now I know. I'll just use that all the time, baby...

**Adam Staravia:** Node mode.

**Jerold Santo:** Yeah, Node mode, please.

**Ryan Dahl:** I mean, if you're the one who's writing it...

**Jerold Santo:** Totally.

**Ryan Dahl:** ...then you're pretty sure that it's going to be okay.

**Jerold Santo:** Yeah, exactly.

**Ryan Dahl:** The problem comes when you're running somebody else's code.

**Jerold Santo:** Yeah, like I said, this was an inconvenience, but it's like a very explicitly, well-considered inconvenience that's like "Yes, we're doing this because the trade-off is completely worth it."

**Adam Staravia:** This is a shift left kind of moment, where you're taking typically maybe security concerns that you might rather just say "demo run" or whatever the command is to run a Demo application. But you're kind of shifting left, saying "These are security concerns that Demo resolves and has control over" and putting them more front and centre. Rather than -- as you said, in a configuration file, which is less minimal, requires potentially a different file format, other concerns... Like, this is a shift left kind of moment. Would you say that?

**Ryan Dahl:** Sure. I haven't heard the term shift left before.

**Adam Staravia:** Shift left is whenever you take the security concerns, which if you take a product lifecycle, left to right, left being dev, iteration, right going to production...

**Ryan Dahl:** I see.

**Adam Staravia:** A shift left is you sometimes think about security further to the right, once it shipped, potentially. Shift left is a term used by security minds to take that security concern and shift it more left into dev land.

**Ryan Dahl:** Yeah, I should mention that there is a new feature --prompt. Demo run --prompt. So if you don't want to allow all -- the current behaviour is if you hit one of these ops that's trying to access the file system, and you don't have the correct allow flags, you get an exception, the process drops out, errors out. There's a new feature that has an interactive prompt that will be like "Hey, I'm trying to read this environmental variable. Do you want to allow this, yes or no?" So you can kind of yes or no through the exact accesses that the system is doing. And we think that we're going to enable this by default actually, and not require this --prompt flag. So this is kind of going more in the direction of -- as always, in the direction of web browsers. We like this programming model where you opt into additional privileges.

**Jerold Santo:** \[36:24\] I like that. It sounds like a good compromise. Kind of shifting a little bit further right, but you're following the web browser's lead, where it's like "Are you sure you want to give this person access to your webcam?" And if you say yes, then it's on you.

So security front and centre. We've talked about packages and how that all stuff works, importing other people's code, we've talked about TypeScript... What are some other aspects of Demo that are cool and exciting? There are some tooling things, there's a formatter, there's some of this kind of developer experience things that help you stay productive, right?

**Ryan Dahl:** Yeah, so there's a bunch of sub-commands in Demo, demo run being the most obvious one to run a script. But we're kind of taking this Go approach where we're just going to build in all the tooling for you, so that you don't need to bring in all this other third-party tooling.

For example, we have a code formatter built into the system, so you can demo format your code. We have a linter built into the system. You can demo lint. We have a test runner - demo test - to run tests. We actually have all sorts of stuff in there. Furthermore, we have test coverage, we have a documentation generator, and we have a dependency analyzer - demo info - which will show you your dependency tree.

Generally, Demo knows all about your source code, it knows all about your dependencies and what it's doing... And why not? We're distributing this executable; all of this stuff is written in Rust, and so it compiles down really tightly...

So our formatter that you run is not Prettier. It's something called Reprint, and it's written in Rust, and it's like 100 times faster. And our linter is not ESLint, it's demo lint, and demo lint is written in Rust and is very fast.

We have demo LSP, which allows VS Code to talk to Demo, and get tab completion, really nice editor interaction... So Demo can basically tell your editor documentation, all sorts of interesting interactions that Demo can help provide VS Code.

**Jerold Santo:** That's all really cool stuff. How much of that stuff is informed or inspired by other languages? Are you a language aficionado? Do you watch what the Go folks are doing, what the Elixir folks are doing, what the Haskell folks...? Are you watching these different ecosystems and saying "Oh, there's a good idea." Because I think go FMT kind of made this formatter a popular thing to do at the language level, not like a third-party level... And it seems like you're pulling in lots of good ideas.

**Ryan Dahl:** Absolutely. This was heavily inspired by Go. Not just in these various tooling, but all throughout the system. It's important to continually improve and take good ideas where you can get them.

**Jerold Santo:** So the standard library is pretty fleshed out as well. I'm just wondering, where are the holes? Because Demo still -- it's at 1.0, but it's newer; it's not as mature. Is the ecosystem still waiting for large holes to be filled? I know you recently shipped HTTP/2, web server back-ends... So things that you expect to be there are kind of there, but at a certain point do you get to where you're looking for a package, and it's only in Node, it's not in Demo? Is that still the situation?

**Ryan Dahl:** Yes, that is still the situation. You know, things take time... I expect this will be worked out over time. I remember back in 2010 people would be like "How do I connect to MySQL with Node?" and I would turn red-faced...

**Jerold Santo:** \[laughs\] You write a driver.

**Ryan Dahl:** ...and apologize that I did not have a MySQL library yet... And they're like "But how is that going to happen?" and I said "I don't know how that's going to happen. I just hope that that is solved at some point." And it's embarrassing to even think that that was a concern, because that was totally not a concern. All those problems got worked out essentially without my interaction.

\[40:20\] You know, Demo and Node are very similar systems. They're both built on V8, they're both JavaScript... They're pretty similar. The differences are relatively superficial. I mentioned this Deno.land/standardlibrary, the Node compatibility layer... This is a work in progress. If you go check it out, there's something -- I think we're maybe at 40% compatibility now. So we're still filling these things out, and I think over time it will be less and less of a problem to take existing code and run it in Demo.

But there's still a lot of work to do... You mentioned this HTTP/2 web server - up until recently, Demo was using a web server written in TypeScript that was a loose port of Go's web server. It's built on top of TCP sockets and TLS sockets. It was a nice HTTP 1.1 server, but had some problems in that it didn't support HTTP/2. And because we just made this port ourselves and are not particularly interested in writing web servers, we're kind of dead-ended with that codebase. We were forced to then write an HTTP/2 web server... HTTP/2 being a much more complicated protocol than HTTP 1.1.

What we'd really like to do - I've mentioned this earlier, about linking in native code libraries using Rust... Rust obviously has a web server already implemented. In fact, Demo already has that web server in its binary somewhere, deep inside of it. What we really want to do is just allow people to call from JavaScript into this hyper web server in Rust and start up a nice, fast HTTP/2 web server. This work is still unstable. IT's shipped in Demo 1.9, so people can use it if they use the --unstable flag... But yeah, now we're working on this native web server, which - I think serving websites is quite important to server-side JavaScript tasks... And it's quite fast. It has very good latency, very good throughput. We have some preliminary analysis on its performance on the 1.9 release notes. We hope to stabilize this in the next couple of months, and people will have a very fast web server available right out of the box.

**Break:** \[42:39\]

**Adam Staravia:** Ryan, back in March 29th you announced the Demo company, and obviously, you've got a great new start to what you began with Node. A lot of new beginnings here, a lot of wrongs made right... And to put behind that a company. So why are you on this path? I suppose more than ten years - Node 2009, now it's '21... What's the path? What's Demo company, what are you doing?

**Ryan Dahl:** Programming languages are important. The world is built on software, and of the programming languages, dynamic programming languages are, I would say, what most people are interacting with day-to-day. But most business needs are best expressed in Ruby on Rails, or Node/JavaScript, or Python, because to be honest, most problems are not compute-bound, they are engineering-bound. All of our time spent as programmers is what we're trying to optimize for... And scripting languages, dynamic programming languages are the best way to get going fast.

I work on this problem because I think it's very empowering to be able to take a system like Node or Demo or Perl or Ruby and just start programming really fast. I got started with Perl myself, and I don't know if you guys feel this way, but there's that feeling of power when you first really grok the language, and you get over the -- you have to climb some mountains before you feel powerful in Perl... But once you get there, suddenly the world is your oyster, and you can just solve all sorts of problems very quickly.

Yeah, I just don't think there's enough effort being -- obviously, I'm talking a lot about Rust, Go... These programming languages are very important, but they're targeted at different use cases. I love Rust. I would never start a new C++ project, as I said, but I'm not going to use that to rename a bunch of files on my folder. Furthermore, I'm just going to smash my keyboard for a while and write some JavaScript.

Of the dynamic programming languages, JavaScript is the biggest; V8 is the fastest VM in JavaScript. It's the fastest dynamic language VM, period... And JavaScript has this industrial standardization process with it. It's tied to the web, so if you believe that the web is going to be here in a couple of years, JavaScript will certainly be here in a couple of years. It is as tied to the web as HTML is, so it's certainly not going anywhere.

So if you're going to choose one of these languages to invest in and build on, I think it's pretty clear that JavaScript is the language ultimately that we're going to be using.

I think once you play around with this stuff a bit, and you learn Python, and you learn Ruby, and you learn JavaScript and Perl, you get the feeling that they're pretty much the same thing. There's different syntax here, there are different ways to do different things, but they are very similar systems, essentially with different function names, different syntax... And yeah, I think those surface-level features are fairly unimportant. I think JavaScript is really the one that we should be using to push forward the needs of the world to create fast software, or create software quickly, I should say.

**Adam Staravia:** \[48:22\] Yeah. Bet on JavaScript, basically.

**Ryan Dahl:** Bet on JavaScript.

**Adam Staravia:** One of the things you say in your manual too, and you kind of alluded to this a little bit, was in the philosophy section of the introduction you say "Among other things, Demo is a great replacement for utility scripts that may have been historically written in Bash or Python." I didn't really consider this, but that's pretty interesting too, because most often I'll reach for things like Bash to do different things in a file system -- not too often Python, because I'm not a Pythons, but I've definitely used Bash before, and I've used things in Ruby like Make, and other things like that.

**Jerold Santo:** Rake...

**Adam Staravia:** Rake. Isn't Make and Rake fairly the same? Isn't Rake built on Make?

**Jerold Santo:** Well, Rake is based off of Make, but Make is not Ruby.

**Adam Staravia:** Yeah.

**Jerold Santo:** You just misspoke; Rake was what you meant.

**Adam Staravia:** My bad. Rake/Make then. Thank you for correcting me.

**Jerold Santo:** Sure.

**Adam Staravia:** You know, being able to do that kind of thing, where you're betting on JavaScript -- not too often will you do those kinds of things, scripts like that with JavaScript. Like before, its lack of ability to have secure access to the runtime, or the system and the file system and whatnot.

**Ryan Dahl:** Yeah, I mean - Bash is another dynamic language, one that starts a sub-process for every statement in your program... But generally, you would use Bash because it's widely available on all the different systems that you're running on. It's very portable. It's not a great programming -- I don't think anybody loves Bash as a programming language.

**Adam Staravia:** It's pretty hard, yeah.

**Ryan Dahl:** Yeah.

**Adam Staravia:** I regularly access documentation to confirm my syntax is correct... Or just cargo cult, because that's sometimes easier. Copy and paste. There's lots of it out there too, so it makes it easy.

**Ryan Dahl:** Yeah.

**Jerold Santo:** There's probably a Subreddit somewhere where there's people who just love Bash, and it's like their thing... But they're a rare bunch, for sure. Now, like you said, if you take all the scripting languages together - I agree with you; I've done Python, Perl, Ruby, JavaScript... The more you learn, the more you start to realize they have their own idiosyncrasies, they have their own view of the world... But they're all kind of in the same ilk. And I would tend to agree, even though Ruby is my first love, that JavaScript is the one to bet on, because it's already ubiquitous. It's in the browser, it's used pervasively server-side now thanks to Node, and it is definitely not going anywhere. So you've picked that as your place to build and to create, and you want to do this into the future; this is an ambitious, big project, so you've started a company around it... Which is different from what you did with Node. That was a long time ago, but why don't you tell a little bit of what went down the first time when you create Node, what happened to you -- I know you had a full-time job etc. Things were different with your life. There's a company now, this is different from Node... Can you just compare and contrast the two situations for us?

**Ryan Dahl:** Yeah, I was much younger, obviously, when I started Node. Shortly after starting it I took a job at Joint, where they said "Come work for us. You can continue working on this project", which seemed like a great deal. I moved from Germany to San Francisco, and continued building Node... And kind of throughout 2009, 2010, first part of 2012.

When it became more and more clear that Node was really a thing, Joint sat down and made a business deal with me, and I ended up selling Node to Joint, whatever that means when it's an MIT-licensed open source project... But I gave them control of the project and gave them the website and whatnot. That worked out very well for myself personally. I'm not sure how well it worked out for Joint, actually... For myself it was great. I've seen some comments online that kind of paint a different picture of the situation, that I was exploited by Joint, or something...

**Jerold Santo:** \[52:14\] You didn't feel that at all?

**Ryan Dahl:** Not at all the case.

**Jerold Santo:** Well, that's good. So after you left Joint, what did you do next? I know you were doing research and development at some point, but did you have a job after that, or did you take some time off?

**Ryan Dahl:** I took some time off, I worked on some other projects that were unsuccessful... I worked for a while at Google, doing machine learning stuff... It was 2018 that my collaborator in Node, Bert Elder, who founded the company Strong Loop, was -- so Bert's journey is also interesting. He was an early contributor to Node, and did one of the most important refactors in Node early on. Early on, Node only worked on Mac and Linux, and we wanted to port it to Windows. Node is doing all this asynchronous IO, so it uses poll and queue, these non-blocking sockets... These are fairly intricate, not well understood operating system APIs that differ from operating system to operating system... And in particular on Windows it's completely different. Their non-blocking IO system is called IO Completion Ports, and we wanted to do a very proper port to Windows.

We wanted to use IO Completion Ports, so that Node would work as a native, proper program on Windows. This was a massive undertaking, and Bert led this effort. We collaborated with Microsoft on it. It took probably a year, but at the end of the day, Node works on Windows. In fact, Node is very well-supported on Windows, and it's very fast. I don't think people run servers on Windows too much, so maybe it doesn't matter how fast it is on Windows... That was a very successful, massive undertaking.

As I said, Bert went on to fund this company Strong Loop that did Body sort of things, built some products on top of Node. They sold that to IBM I think in 2015 or so. Around 2018 I left Google, and Bert was wanting to leave Strong Loop (or IBM), and we teamed up and started working on projects. I already mentioned this TensorFlow in Node project that we were originally working on... But we just had the idea to kind of poke around for a while and see what we could do.

**Jerold Santo:** So after you conceived the idea of Demo, and maybe you had a prototype, or you had maybe even announced the project - was the Demo company right there in your guys' minds, kind of like "Okay, here's a path forward from then", or is that a newer conception that you came up with later?

**Ryan Dahl:** So early on in Node -- as I mentioned, I was young and naive about how software is developed... I was very much of the idea that "Oh, you just throw some code out there on the internet, you collaborate with people... This is how software gets built." But Node grew bigger and bigger and bigger, and there's more and more people involved, and it becomes clear at some point that organization really matters, it matters very much to have full-time professional engineers working on it, and people can contribute code on a one-off basis. But if you really want to get things done, like port Node to Windows and use IO Completion Ports, you need full-time engineers; these people need to get paid, and they need to be able to focus on a problem for a long period of time.

\[55:55\] So you realize that at a certain scale, software becomes a lot more about managing budget and trying to manage an organization and kind of the meta problems around getting funding for people. So it's always been clear to me that if we're going to go down this route and build this programming system that is going to be very much like Node, that if it's going to ever scale, it needs to have some funding model. There's no way that this can work where people are just going to randomly work on stuff on kind of one-off basis for free. There needs to be some way of paying people to work on the problem.

And Node is not a piece of software that is unused, that is not attached to revenue streams. There are all sorts of companies using this. If I could have one cent for every Node installation - oh, how great it would be. This is open source software, of course, and it's very liberally open source... And I believe in that, and I think that's important for a programming system like this... But yeah, we see that these systems have commercial applications to them, and these can provide connections to reality for the software itself that is making sure that we're actually solving a useful problem... But also provide funding to develop the software.

I guess we've known very early that -- we did not know if this project would go forward or fail, but we always knew that if it's going to grow, that it would need to turn into a company, eventually.

**Adam Staravia:** At what point did the company become the company then? I know you had the announcement in March... Late March you mentioned a sizeable round of seed capital... You can name names if you want to, but at what point -- was that when the company began, and the team of full-time expert engineers working to improve Demo happened? Was it a chicken and egg -- which came first?

**Ryan Dahl:** No, Bert and I first worked on this ourselves for a year. So that was kind of our first investment, and I think we hired our first engineer in 2019 or so... And yeah, we've grown from there. I think we're eight people now.

**Adam Staravia:** Gotcha.

**Jerold Santo:** So if there's a video game called "Build an open source business", and if the first step is "Pick your license", you guys chose MIT. That would be like setting that video game on hard mode, wouldn't it? It's like, "Well, I want the biggest challenge. I'm going to let my software as free as you could possibly let it free." There are a lot of startups, a lot of businesses switching over to things like SSPL, AGPL... Any concern about AWS competing with you, or the big dogs coming in and eating your lunch?

**Ryan Dahl:** Everybody's trying to figure out open source companies and how to do this properly... And one model of doing this is the open core model, where your open source software would be free, but then you'd kind of have an enterprise edition that you add on some extra nice features, and you would charge for that.

You can also get into some licensing trickery, where maybe you make your software AGPL-licensed, and kind of allow people to run this locally, or kind of in non-commercial applications for free... But once you get into the commercial realm of things, you are then asked to pay a fee.

I think for Demo - this is a programming system that we're asking people to program against. We're asking a lot of our users, we're asking them to invest a lot in the system... And I personally would be very, very uncomfortable with programming using the base layer of my -- you know, Demo sits below all of your other software; I would feel very uncomfortable if there was some weird payment hook at that layer of the system. It would prevent me from ever even trying out the software, in fact... And I think that's the case with Demo. If we tried to make Demo itself commercial, and people are looking at Python, and Node, and Ruby as alternatives, I think many would choose the solutions to this problem that do not have a payment hook in it.

\[01:00:11.01\] We are pursuing a different funding/revenue model. As I said, we think this software is pretty useful, and we think it's useful in different commercial applications. I haven't mentioned it yet, but Demo - you download it as this one executable, but it's actually a collection of software, and we've been pretty careful in breaking this up into different bits that we can recombine in different ways... So we have a product that we've been working on for the last six months or so that is a different runtime. It is called Demo Deploy, and it has a very similar API to Demo, a very web browser API. It's a JavaScript runtime, but it doesn't run on your computer, it runs in the cloud. You can think of it as a dynamic CDN if you want to... So we have processes running in 22 locations around the world, and we have an Any cast IP, and you can provision a domain name on our system. When you go to access your domain name, it resolves to this Any cast IP, and that gets routed to the nearest data centre. So if you're in Tokyo, it gets served locally in Tokyo.

And rather than a CDN which responds with static content, this invokes a JavaScript hook. It is a serverless system, so think AWS Lambda, or Cloudflare workers... So it's a system for responding to requests dynamically. The best way to describe it is it's a web server, a multi-tenant web server with V8 built into it. It is completely a separate system, and this thing AWS cannot -- this is not open source; this is proprietary code.

**Jerold Santo:** Right. But it's still Demo in terms of the API, so... I'm using Demo to develop, I can use it locally, I can deploy it on my VPS fine, but if I want to run it in this capacity where my users are in Tokyo, so my Demo process is running in Tokyo, then Demo deploy is just like, you know, a push away or a sign-up away. It's a pretty cool idea.

**Ryan Dahl:** That's right. Of course, you can take Demo - the executable that you download, that's free - and you can wrap that up in a Docker and you can send that out to AWS Lambda and kind of have a very similar experience... But that is not what we are doing internally. We are not running Demo in some Docker containers. We actually are kind of using the V8 isolate... Furthermore, we were talking about how this is a secure sandbox before. So instead of having multiple Linux VMs running for all the different tenants on this web server, we actually have all of these little V8 isolates running. And these, as we mentioned, are secure sandboxes, so we don't have to worry too much about hackers being able to see other people's requests and whatnot... And the nice thing about these is they're super lightweight.

This is essentially like opening a tab in a web browser. So think of a web server with a bunch of tabs in it, and each of the tabs is for a different tenant on the system. We can respond to requests very fast. We have cold start times in less than ten milliseconds. I'm not sure the exact number. And we do all sorts of nice optimizations.

Obviously, it only runs JavaScript. This is not a Linux VM, so you cannot run your Python process in this. But because we've built explicitly on top of V8, we can make all sorts of very nice optimizations, like Cloudflare has done, to speed the response time.

**Adam Staravia:** I think even, so someone has to be really motivated to do an Amazon deploy with a Demo repackaged. I'm not sure if that's part of their business model to serve customers... But I could be wrong.

**Jerold Santo:** You never know what they're going to do next.

**Adam Staravia:** \[01:04:08.04\] I mean, you just never know. You just never know... The liberal license, the permissive license MIT, open source, single binary... A collection - sure, maybe they would do that, but I don't think that's their model. So I think your goal though is to provide Demo as it is to -- I guess to maybe solve some of the problems you didn't do well enough with Node, and sort of live on those dreams you had with Demo, but then still have this commercially-applicable ability on top of Demo. And you mentioned in your announcement for the company, "We've been hinting at commercial applications." So correct me if I'm wrong, Deploy is just one application, so "...applications of this infrastructure for years" - what are some other ideas that you have that you can share? Is there anything you tease, or mention, or early-announce?

**Ryan Dahl:** Right. We're working on this deploy product, and that's the only thing we're going to be working on for the foreseeable future. But other applications would be, say, Electron... We think we could do a much better kind of GUI application framework than Electron has, given that we have Rust, and then Demo is kind of broken up into these building blocks... Generally, there are all sorts of systems that kind of want little one-off JavaScript little bits to be scriptable... And we think that -- there may be all sorts of hidden use cases where people might want to have a Demo API. And by the way, I should be explicit - Demo is trying not to have an API. Demo is trying to be the web browser API. Demo is trying to not have a specific Demo API, but just - if you want to encode a string into an unit array you use a text encoder. We don't have a special Demo API for that.

But yeah, I think there are databases that may want to do, say, Map Reduce with JavaScript. Potentially, there's some commercial application there... But yeah, I think for the moment we're focused on this Demo Deploy. The idea is that if you're writing a website, you write some JavaScript, you might run this locally, with Demo on your computer; maybe spin up a local server to serve that frontend JavaScript. That kind of server-side code to assist you in writing this frontend stuff, or maybe any backend code that you write is also very web browser. It uses the same WebSocket APIs, for example...

So there's basically three different deployments - the web browser, frontend JavaScript, your local computer where you're going to be writing some server-side JavaScript, and then maybe you want to deploy that server and run it globally, so then you send out that code to Demo Deploy. And by the way, you can take that executable, and you can deploy it yourself. So you're in no ways locked into using our Demo Deploy system... But we're going to have the best way for you to deploy your Demo scripts.

**Adam Staravia:** What's the state of Demo Deploy currently? Is it in beta? I know people can use it...

**Ryan Dahl:** It's in beta.

**Adam Staravia:** What is the state of -- it has a commercial product; it's not collecting funds currently. People aren't paying for it currently. It's sort of available to use... How do you plan to convert that into commercial? What's the current state?

**Ryan Dahl:** Yeah, it's in open beta right now. I would consider it a technology demo at this point. We're working on cool features that will be announced soon. Yeah, we will have a general availability announcement. We don't have a deadline for that yet, but we hope that it will be later this year. We're thinking in the six months timeline or so. But yeah, it's usable. People should try it out. It hooks up with your --

**Adam Staravia:** Production-ready then? Production-stable?

**Ryan Dahl:** I would not, no, consider it that.

**Jerold Santo:** \[laughs\] He said usable, he didn't say production steady...

**Adam Staravia:** Okay...

**Jerold Santo:** You can use it.

**Adam Staravia:** \[unintelligible 01:07:46.20\]

**Ryan Dahl:** Yeah. We have no SLA. It's something that -- you know if you're interested, you should try it out... But I would not use it for production problems at this point.

**Adam Staravia:** \[01:07:58.25\] So if there's a future then for Demo, that place of competition might be with Deploy. Because if you claim here now that you intend for Demo Deploy to be the best way to run a Demo application, then that might be the way. If Demo wins like Node has won... And we haven't asked you if you planned for -- I assume so, but if you planned for Demo to take over what Node is, to replace Node particularly... But if it becomes as big as Node has become, and as usable and Node has become, then that's the place to compete with you, would be on the deployment.

**Ryan Dahl:** I guess... I'm not sure what you're asking, actually.

**Adam Staravia:** Well, to deploy, similar maybe for -- you know, there are some examples from WordPress, for example. There are particular hosts that are amazing at hosting WordPress. If Demo wins and becomes very popular, to gain market share, to have a commercially viable application, or a company, or a SaaS product, you might want to compete with you all to host Demo applications.

**Ryan Dahl:** Yeah, I mean, I would encourage anybody who wants to --

**Adam Staravia:** Compete. To compete.

**Ryan Dahl:** ...also be running a Demo service, yeah.

**Adam Staravia:** Sure.

**Jerold Santo:** Ultimately, that's good for the ecosystem anyway...

**Adam Staravia:** Yeah.

**Jerold Santo:** ...and Demo the company. Probably a pretty good competitor when it comes to running Demo in these different contexts, right? So I would assume you're welcoming competition.

**Ryan Dahl:** Yeah. And by the way, we're investing a lot in this Rust/JavaScript infrastructure... So when you go out and see products that are serverless products that execute JavaScript and don't look like extremely Body... So a lot of this stuff is actually Node, but kind of newer server-side JavaScript APIs - yeah, look carefully. It may actually be Demo or one of its lower layers of crates. We expect that and we encourage that. This helps the ecosystem.

**Jerold Santo:** Taking it back to Demo Deploy for a second, just thinking through it as an end user... And it seems like a lot of these serverless solutions don't have the database story; when it comes to my backend, if I'm going to run all my code, my dynamic website at the edge, but my database isn't collocated with those edge nodes. It's in New York City, running on a Postgres server or whatever - it kind of defeats a lot of the advantages of having that locality of that runtime... Because most backends aren't just doing mere math. There's some data stored in some place, and they're going to go hit the database, and they're going to figure it out, and they're going to put stuff in and take stuff out... Is there anything with Demo Deploy that collocates a database, or makes it so that my Demo backend has all the things it needs right there with it?

**Ryan Dahl:** Not yet. You certainly see Cloudflare going in this direction with Durable Objects. Right now, Demo Deploy is this -- I would consider it kind of the minimum viable product, which is that it responds to requests.

**Jerold Santo:** There you go.

**Ryan Dahl:** So you can send back a response... You can make outbound requests. Let's say you have a Firebase database hosted by Google somewhere... You can make outbound requests to that data store for any persistent needs. We've basically pushed the persistence problem out of our problem space at the moment. And you know, there are problems -- sometimes you just want a little redirect server, and there's no need to have persistence in some applications. Obviously, many applications need persistence, and this is one of several features that we're looking at in the coming months.

**Jerold Santo:** Cool. So what happened with Node the last time around? I've referred to it earlier with the Micheal Rogers reference, was that there was a lot of opportunity in the early days, and a lot of people jumped in and became influential, impactful JavaScript people because they helped out with the early days of Node. And this is potentially a new opportunity with this new round with Demo, where it's early days... You have a core team, you have people doing stuff, there's a standard library... There's a lot more stuff that Demo has, I think, than that Node had when it first began.

\[01:12:13.11\] But the question is, if I'm a developer, I'm an open source person, and I'm thinking "You know what - I'm going to take a bet on Demo as an ecosystem, and I would love to be impactful, I would love to help out in ways that are big", what's the best way, what's the easiest stuff, low-hanging fruit, the real fertile ground for getting involved and being impactful with your code in the Demo ecosystem?

**Ryan Dahl:** I think the standard library is -- we haven't talked about this that much, but in Node there is no standard library. There are a lot of utilities built into Node itself. But part of the Node dependency problem is that when you just want a small little utility, when you wanna Left pad your string, or whatever, you have to end up pulling in a third-party dependency. And in Demo, what we're doing is collecting all the main useful things, and it's a bit ambiguous which things should be considered part of the standard library and which things shouldn't be... But in general, if a lot of people need those utilities, we put them in there. That's a very nice way to contribute.

We have a style guide, we have tests... It's something that affects the entire community, so... People contribute modules to the standard library. And obviously, people should ask first before randomly contributing things. It would be unfortunate if you did a bunch of work, and then we'd have to reject it, for some reason.

**Jerold Santo:** Right. Where do you ask?

**Ryan Dahl:** This is a way to be very useful in the Demo community.

**Jerold Santo:** Where do those questions go? Is it issues on repos, is it mailing lists?

**Ryan Dahl:** Yeah, there's a demo\_STD repo on GitHub... Just open an issue and discuss it. Generally, we're very open to adding new libraries in the STD.

**Jerold Santo:** Is the STD in Rust also, or is that in TypeScript, or in JavaScript?

**Ryan Dahl:** That's in TypeScript, yeah. These utilities built on top of Demo. Obviously, if people know Rust and want to get into the internal system of Demo, there's a whole world there to explore. But that's a bit deeper.

We have a Discord, it's very active, and there are a lot of channels where people are discussing new ideas, so I would encourage anybody to jump on there and hit me up with any ideas.

**Adam Staravia:** Are there any particular applications that are currently leveraging Demo that you want to call out, or that you've been impressed by?

**Ryan Dahl:** No, actually...

**Adam Staravia:** \[laughs\] Still early days?

**Ryan Dahl:** Still early days. I mean, people are playing around with stuff... And generally, this is a very similar system to Node. So if you make a chat server, I wouldn't call that out as particularly interesting necessarily. I think the interesting bits are around the tooling and how we can make these workflows much faster for people, and simpler. But the actual applications built on top are very similar in the end.

**Jerold Santo:** Let's say I'm sitting on an existing Node app which is medium-sized, and it's running the business, but it's not like 50 million lines of code. What would a port take, or what would it look like? Relatively straightforward, or are there serious dragons there?

**Ryan Dahl:** If it's already using ES modules in TypeScript, it should be relatively straightforward. If it's common JS and kind of old-school style Node stuff, if you would be a bigger undertaking.

**Jerold Santo:** Thanks for sharing so much, man. This has been very enlightening.

**Adam Staravia:** Yeah.

**Jerold Santo:** I really enjoyed it, and I appreciate you coming on.

**Ryan Dahl:** Yeah.

**Adam Staravia:** I appreciate you making time in your schedule to finally do the podcast with us after so many years. I guess we've never really invited you either, but... Sorry.

**Jerold Santo:** \[laughs\] No wonder you never came on.

**Adam Staravia:** You've been hard to get a hold of for the last 11 years... But I'm glad you made time to show up here at the Changelog, we appreciate that... So thank you, Ryan.

**Ryan Dahl:** Yeah, thanks for having me.
