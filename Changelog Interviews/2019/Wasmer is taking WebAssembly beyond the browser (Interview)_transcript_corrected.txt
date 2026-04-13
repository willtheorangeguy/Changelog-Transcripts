**Jerold Santo:** So there was a tweet by Steve Flank that, Adam, I think you were a fan of, where he said that "2019 is going to be a huge year for WebAssembly, even if many people don't know it yet, and may not see the effects until 2020." We're not joined by Steve, we're joined by Cyrus of Wasmer, and I just wanted to pitch that over to you and ask you if you agree with Steve, if you know what he's talking about... Are you inside on this? What do you think about WebAssembly in 2019?

**Cyrus Akbar:** Completely, yeah. I completely agree with Steve. WebAssembly will be very big this year. We are just warming up. The main reason we believe it's going to be big is because there is a lot of agreement in the industry that WebAssembly is the path to go for executing things like universal binaries in a universal way; first across browsers, and then outside of browser environments. Basically, right now there are a lot of companies pushing towards that, and we are one of those.

**Jerold Santo:** Wasmer.io is what you're up to. "It's a standalone, just-in-time WebAssembly runtime, with an aim to be fully-compatible with Scripted, Rust and Go." Can you unpack that description and put it in layman's terms for me, so I can understand it?

**Cyrus Akbar:** Completely. What we are trying to do is move WebAssembly to the server side. Up to basically one year ago, WebAssembly was mainly a way for executing performant code on the browser; however, we believe WebAssembly will also be big on the server side, and we are trying to do a similar thing that Node.js did, moving JavaScript to the server side, but with WebAssembly instead.

So first we are focusing on creating a runtime that will let developers use WebAssembly on the server side, and second we are adding integrations into other languages. Basically, you can call WebAssembly not just from JavaScript, but also from Python, or from Ruby, or from Rust, or from any other language. That's basically what we are focused on.

**Jerold Santo:** I understand why you would want to run WebAssembly in the browser... I guess where I'm missing it, and where I'm going to need your help - and I obviously am missing it, because lots of people are excited about this, I just don't get it yet - is why would you want to run WebAssembly outside the browser, server-side when you could just write... Like, the example you give is NGINX (let's just take that) running via WebAssembly. But why can't I just compile NGINX and run it? Why run WebAssembly in-between, so to speak?

**Cyrus Akbar:** \[04:23\] The main reason for using WebAssembly there is that it provides a way of running binaries universally. Right now, if you're using NGINX, to run NGINX in your system you need to compile it specifically for your platform and architecture. That means if you're on Linux, you need to compile it for your Linux distribution and the certain architecture that you are using; on Windows you need to compile it differently... And this is super-tedious.

So that means you need to distribute the source code and let the developer compile the source code itself to be able to use it. We believe it will be much nicer if we provide universal binaries that can be used across any platform or architecture, without actually any further change. So your same nginx.Wasm could run on Linux, could run on Windows, in Macintosh, or eventually in your phone, without any change. We believe that's going to be huge.

**Jerold Santo:** So that's kind of the old promise of "Write once, run anywhere", only it actually delivers.

**Cyrus Akbar:** Yes. This concept is similar to what Java or the JVM was trying to achieve, with the main difference that right now any other language actually can target very easily to WebAssembly. So it provides a nice transition for projects that already exist, either because they are developed in C, or C++, or Rust, or any other language, and they can be compiled very easily to WebAssembly. That means you can transition or reuse your projects or target WebAssembly very easily.

**Adam Staravia:** What makes WebAssembly good for this, this universal binary idea?

**Cyrus Akbar:** What makes it great first is that we have a universal agreement, or agreement across all the industry. That means companies like Google, Apple, Mozilla - they're all pushing towards a standard that everyone agreed on. This is big.

The second thing is it started from the need of executing performant code on the browser... Actually, this started from a prototype that was actually in JavaScript, asm.js. From that, actually it's been shaped exactly to fit the needs of executing byte code in a way that was very performant on the user side.

**Jerold Santo:** So in the browser there's a specific surface area of functionality that needs to be available, and the server on an operating system level - there's just way more things there, right? I just feel like there's much more surface area to the APIs, and to the system calls, and all the different things that need to be bridged, so to speak. So is this a huge undertaking, or is it easier than I'm thinking?

**Cyrus Akbar:** It's actually not really that hard. For example, one of the projects that I started targeting -- or actually created (kind of) WebAssembly, was Scripted. How Scripted started was we have a native binary that we wanted to execute on the browser, so basically it provided a bridge between LLVM IR and JavaScript. So it just translated LLVM byte code into JavaScript byte code.

With this first bridge, what Scripted did is basically designing an interface that will help on executing this code on the browsers. And how they did it is by creating wrappers around the miscalls that actually don't exist in the browser. For example, for opening a file, or actually opening a socket, or closing a socket - all that they did is creating a set of miscalls that work, and are just fake, but reply with the same structure that WebAssembly was suspecting. This set of miscalls is, on the Scripted side, is something like 200, but there are other implementations that actually require implementing much less miscalls.

\[08:24\] So the truth of the fact here is at the end, with a set of more or less like 50 real miscalls, you can implement almost all the calls that any native library or native binary will need to do to talk with the operating system, and that will be enough. And in general, this set of miscalls will be, again, like opening a file, closing it, reading its contents, opening a socket... I don't know, maybe getting a random number, and things like that.

**Jerold Santo:** So at the end of the day there's only about 50 - is that what you're saying? ...that you have to implement for any particular platform.

**Cyrus Akbar:** Yeah. Basically, any other one is just a superset, or is just like a play between these 50. So with 50 you will be very much served.

**Jerold Santo:** Is that where Wasmer comes into play - it provides that interface to those system calls? Or how does Wasmer come into -- I know you say it's a runtime, but...

**Cyrus Akbar:** First, before starting Wasmer, curiously enough I just started ruby in all the WebAssembly runtimes, and the fastest ones were actually on the browser side, and there were other implementations, or trying to have like a WebAssembly virtual machine on the server side. I reviewed all of them, and funnily enough, the faster one was Firefox... So I started sneaking into how they were implemented the WebAssembly runtime, and basically what I did is I created a toy project using their WebAssembly engine, but trying to use it outside of JavaScript, so removing all the JavaScript part.

We started kind of just creating the runtime as a pet project, which was a very cool project... And then -- can you repeat what was the question? I think diverged a little bit.

**Jerold Santo:** Well, I was just trying to figure out where Wasmer fits into the picture with regard to the system calls.

**Cyrus Akbar:** Yeah, regarding the system calls, how Wasmer fits is we provide different integrations or interfaces. For example, Scripted defines a set of miscalls on top of LBC, and we just kind of like -- rather than creating these miscalls or emulating these miscalls in JavaScript, we do it natively, with native functions... But the truth of the fact is we can plug Scripted, or we can plug any other kind of ABI.

For example, today Mozilla released this new project, a WebAssembly common interface called WAS. They basically redefined the set of miscalls; rather than being 200 \[unintelligible 00:11:00.00\] I think it's just like 40-50. And the cool fact of Wasmer is you can plug the ABI that you want to use for a certain binary.

There will be some WebAssembly binaries that are compiled using Scripted, and therefore will use the Scripted miscalls, and then there will be other WebAssembly modules that are compiled using this new WAS interface. Then you will need to use this WAS interface instead. The cool thing about Wasmer is you can plug any pre-existing ABI's that we already created, or you can plug your own ABI.

**Jerold Santo:** Can you explain what ABI means, and what that entails?

**Cyrus Akbar:** \[11:41\] ABI is Application Binary Interface, but what it really means - it's an interface that you use for having your miscalls. So it just has a set of miscalls that is defined. There are something like 30 different ways of opening a file; so what is the open function, how many arguments received, and how many types output - that will be the definition of the open function. But then the ABI might have other miscalls. Basically, the ABI will mainly define what is this set of system call functions, what are their inputs and what are their outputs, and that's it. That's what an ABI is. A famous ABI, for example, is LBC; Ming GW is another one, based on LBC... So there are multiple.

**Jerold Santo:** Okay, so an ABI is like an API, but it's a binary interface, and that means that there are specific contracts or agreements of how you're going to access certain functions inside the binaries... Am I understanding it correctly?

**Cyrus Akbar:** Yes, you got it completely right.

**Jerold Santo:** Okay. So rewind a little bit, because you might have lost me on the WAS and on the ABI side, just because I wasn't completely tracking on what ABI's are... Can you explain again how WAS - which is what Mozilla announced today; we'll have a link to that in the show notes... WAS being a system interface to run WebAssembly outside the web, is what we're talking about here?

**Cyrus Akbar:** yes.

**Jerold Santo:** Basically, they're trying to standardize this interface.

**Cyrus Akbar:** Yes.

**Jerold Santo:** So is that an ABI that they're standardizing, or are there multiple ABI's? I just don't quite understand.

**Cyrus Akbar:** Before WAS, the main way for running C projects on the browser was Scripted. With Scripted you have a lot of sets of miscalls, but it was not really designed in the sense of trying to run outside the browser, or basically on server-side environments. What WAS is doing is trying to redefine this ABI so it's a much cleaner way of interacting. So WAS is just a cleaner way of having the Scripted ABI, with much less system calls to implement.

**Jerold Santo:** Okay. This is very much bleeding edge, right? I mean, we're talking about a thing that was just announced, literally today, as we record, March 27th. An ever-moving space, so...

**Cyrus Akbar:** Yes.

**Jerold Santo:** ...grab on tight and hold on for as long as you can, because things are moving fast.

**Cyrus Akbar:** Completely! Actually, before Scripted, one of the things that we were researching on was Cloud ABI, which was a similar set of miscalls that WAS is doing, with the only difference that it will let you define permissions on top of that. So before opening for example a file, it will check if you have permission, or someone gave you permission for opening the file, and therefore it will let you execute the miscall, or it will fail if that's not the case.

Cloud ABI, for example, was another potential ABI for WebAssembly, but regarding WAS, WAS actually fits much better with what WebAssembly needs... Because Cloud ABI was not designed with WebAssembly in mind.

**Break:** \[15:10\]

**Adam Staravia:** So it seems like what this direction that was taken is just like being able to not limit certain types of applications to a certain platform. Almost akin, Jerold, to your stop-limiting your open source libraries potential, where you write something for React, or jQuery, or a certain language, and you're using X, and you can't use it in Y. It's almost like we're going that direction to get to this universal binary, run anywhere, whether it's NGINX, SQLite, or whatever; being able to be on every platform, and not limiting what it can run on.

**Cyrus Akbar:** Completely. As you said, there are two sides of where WebAssembly can be really successful. One is for having universal binaries that can be run without any modification on any platform, and also in any architecture (that means like any chipset). That means running NGINX in your Linux system, or that same NGINX binary in your Macintosh system, or on Windows, or even eventually on your phone. And the same could go with SQLite, or other binaries.

This is one side of where WebAssembly will be very successful, which is universal binaries. The other one that I think will be also key will be for having universal libraries. What does this actually mean? It means having a library that can be used across any other language.

Imagine you have a face detection library. This face detection actually provided a binary image; it detects the squares of where the face is. So right now, if you search, you will find different implementations. One face detection library will be implemented in JavaScript, then in Python, then in Rust, then in C you will have another one... So depending on the system you are at, you will use one or other library. But what I think WebAssembly will unleash is this generation of universal libraries that can be used across any language.

Imagine you create your face detection library in Rust, and you compile it to WebAssembly, basically using the Rust tool chain. The cool thing is as soon as you have this face detection library .Wasm, you can use this library in Python, or you can use this in JavaScript, or you can use it in Rust, without actually needing to reimplement it. I think that's going to be really powerful.

**Adam Staravia:** Having that power is fascinating. When you're at that language - let's say in JavaScript - trying to use this face detection library that's written in Rust, compiled to WASM, what's the dev experience like from a JavaScript developer's perspective to interface with these libraries?

**Cyrus Akbar:** From the JavaScript perspective, the cool thing is JavaScript has actually a WebAssembly engine already embedded. So if you are using Node.js, you will have already a way for interacting with WebAssembly very easily. The only thing that you will need to do is first point to where this WebAssembly file is located, then create a WebAssembly module, and then from that, instantiate it.

The difference from a WebAssembly module and a WebAssembly instance is you can see one is the program, and the other is the process running that program. Basically, one module can have multiple instances running, or multiple processes running that code. The cool thing is JavaScript already has a way of using WebAssembly, but it's actually the only language that right now is able to do it.

One of the things that we are doing here at Wasmer is trying to make it very easy to call WebAssembly or to use these WebAssembly modules outside of JavaScript. We've just integrated an extension into PHP, so you can for example take this face detection library .Wasm and use it from your PHP code, just instantiating the WebAssembly module and then calling a function that exists on this WebAssembly module, for instance.

**Jerold Santo:** \[20:07\] I'm sitting over here, thinking about graphical interfaces...

**Cyrus Akbar:** Yeah.

**Jerold Santo:** ...because I would love to have something like Slack, where they could write it once, run it on all these different platforms, but not have to ship Chromium and all the overhead of Slack. Maybe they could run the exact same binary in the browser and have a web app, although on the web I would like to have a regular web app. That being said, what about graphical interfaces? Are we pretty far away from that? Is there a lot more filling to do that, or are we pretty close?

**Cyrus Akbar:** Actually, we are not really that far. UIs in general are a little bit more complicated, because they require an interface to touch the graphic system... But in general, I would say we are not really that far.

One other thing that right now the industry is pushing towards that direction is with Electron. Electron embeds/uses Chromium under the hood, and then you can have your application running like in any system... But the cool thing - with WebAssembly you can do exactly the same, with the difference that rather than having a JavaScript runtime, you will have a native runtime, running at native performance. Then the RAM usage will be much lower, the performance will be much higher, and I think it'll also be a super-attractive area for WebAssembly. I think we are really not that far... Probably like a few months off.

**Jerold Santo:** Well, that will be awesome. And you can do it in any language you want. There's no limit. As long as your language has WebAssembly support...

**Cyrus Akbar:** Yes, as long as your language actually can compile to WebAssembly.

**Jerold Santo:** Right.

**Cyrus Akbar:** Cool thing right now - we have C, or C++, or Rust, that actually can target WebAssembly super-easily... But we have other interpreted languages - for example Python - that cannot compile directly to WebAssembly. So the way to go there is actually compiling the interpreter itself to WebAssembly, and then execute the interpreter in the machine.

**Jerold Santo:** What...?

**Cyrus Akbar:** Yeah. \[laughs\]

**Jerold Santo:** That's a nice hack. Is there first-party support coming? I'm thinking of Python, Ruby, Elixir... Is there a place where you say "Can I WebAssembly it yet?" A .com, and all the languages are there, with what kind of support they have, or... What's the situation with these other languages?

**Cyrus Akbar:** There is one great repo created by one of our ex team members, Steve. I think it's Awesome WebAssembly Languages, or something like that... And you can see all the languages that can compile, or any language that can be executed or compiled to WebAssembly. So the list is actually pretty big.

One cool thing that we did in Wasmer was being able to run Lua, the Lua interpreter. We have a Lua-compile-to-WebAssembly, the Lua interpreter, and now you can just do "Wasmer run Lua.Wasm", and you will basically run the Lua interpreter. But almost any other language that you can think of, even Java, can compile to WebAssembly very easily.

Talking about Java, there is a very interesting project called Team. This VM actually compiles Java byte code to WebAssembly byte code. Then you can have your universal WebAssembly byte code, with your code that is actually written in Java, but targets WebAssembly. I think that's a very interesting idea.

**Jerold Santo:** We have found Awesome WebAssembly Languages repo, link in the show notes... Lots of languages listed here, and then each one has a little emoji; it's either an egg, or a baby chick, or a hatching out of the egg, or a full-on chicken. There's no legend, so I'm not sure exactly what these indicate; I guess it's just starting to support it, or it's -- I don't know. There's a lot of them, a lot going on there. That's interesting.

**Cyrus Akbar:** Yeah. For example, right now we are actually working on having the PHP interpreter in WebAssembly. There is already a project that targets web, so we are trying to just complete the miscalls needed to actually get the PHP interpreter in WebAssembly. And we are super-close.

\[24:08\] Then you can start seeing how the ecosystem will grow into a place where you can install these universal libraries - PHP, Python, or whatever - in a way that is super-localized and doesn't require you to compile the project itself for using it.

**Adam Staravia:** That's a good point. What is the installation process currently? Will we ever see a package manager for this, or is there a package manager for this?

**Cyrus Akbar:** Cool! Good thing that you asked that. We are working on the first package manager for WebAssembly, and it will be released very soon. Hopefully, at the same time that this show is aired.

**Adam Staravia:** So this is like breaking-breaking.

**Jerold Santo:** Breaking news.

**Cyrus Akbar:** Yeah, it's super-breaking. We are actually very excited, because for example now we have SQLite compiled to WebAssembly and uploaded to our WebAssembly package manager, and you can just do "warm install SQLite", and then "warm run SQLite" and you will run SQLite locally, but at native speed. That means with all the things that SQLite has.

**Adam Staravia:** Let's say you're on Mac - will this replace someone using Homebrew to install SQLite?

**Cyrus Akbar:** Yeah, that will probably be it. And the cool thing is it will work on Linux, and then Windows as well. Exactly the same binaries will work on Windows, Linux, Mac, and could work also on your phone; we just need to build the integration, but that should be not really hard.

**Adam Staravia:** So what's the UX for installing currently? Is it a cURL command, or something like that, to install?

**Cyrus Akbar:** It will be similar to what NPM is doing.

**Adam Staravia:** But I mean now - what's the way it is now, and how it will change, I guess.

**Cyrus Akbar:** Oh, okay. Right now, the way you have to do it is you will first need to compile whatever you have to WebAssembly, then you will need to upload this WebAssembly package or module somewhere, and then from that, when you want to use it, you need to download it manually, and then for running it, you will need to use Wasmer, for example, to target this file that you downloaded, and try to execute it. This is how it was done until now. How it will be done in the future will be - you'll just do "warm install SQLite" and then "warm run SQLite", and that's it.

**Adam Staravia:** I might be splitting hairs here, Jerold, and correct me if I'm wrong, but I'm kind of feeling like WebAssembly might not be the best long-term name. Thank god for the acronym, Wasm...

**Cyrus Akbar:** Oh, yeah... \[laugh\]

**Adam Staravia:** Because at some point we might just digress to Wasm and move on, because WebAssembly will eventually not make sense anymore.

**Cyrus Akbar:** Yes, completely. Actually, I completely agree with that. But WebAssembly actually started from the web, so that's the reason behind the name... But yeah, I guess in the future we'll just call it Wasm. WebAssembly is actually not really tied to the web anymore, but we can see a lot of applications on the server side.

**Jerold Santo:** So the potential to replace Electron-style applications, the potential to replace all package managers, Applet, Homebrew, whatever your distribution or operating system-specific package managers, because it's universal; there's one SQLite, and it doesn't matter what system you're on, it's going to work.

**Cyrus Akbar:** Yeah.

**Jerold Santo:** That's a pretty bright future, if you ask me... If it delivers, that's a bright future.

**Cyrus Akbar:** Yes. Actually, I'm super-sure it will deliver. Funnily enough, before starting Wasmer, I was kind of like sneaking to this idea of what could be possible, and when I realized what are all the possibilities that we have with WebAssembly, I was like "I need to create something. That's going to be really, huge." And the truth is we are not really that far from that future.

**Jerold Santo:** How long have you been working on this stuff, and how did you initially get that insight? What were you up to when you stumbled upon this When did you see the light, and why?

**Cyrus Akbar:** \[28:04\]First, I started developing on open source for a long time. Funnily enough, I released a graphical library for Python. That was about three years ago. While I was trying to create this framework, at some moment basically I dropped my job and I created a company solely focused on this graphical framework for Python. So at that moment I was trying to compete with companies that actually were much more funded than me, because I didn't get any money from investors... So at that moment - the way to compete against them is "Okay, I'm going to make this library available in more languages, but without making the effort of recreating the same framework in another language."

I was taking a look at writing to WebAssembly, and I started basically researching more into WebAssembly and what I can do with it, and what can be done, and I then realized that WebAssembly can be the perfect bridge to compile my framework to WebAssembly, and then be used across any language. So that's what was the first idea. Then from that I started realizing WebAssembly can also be big not just for universal libraries, but also for universal binaries.

What I eventually saw is "This is going to be big for edge computing, or in general for localized computing." Right now, for example, if you have a website that is running on Docker, for example, the way it will work is maybe you set up with Kubernetes, or something else, and then you will have an instance that is running all the time, all day long; even if you have three requests a day. So that means if you have a total of 90 requests in a month, you will need to have a server running fully for 30 days. The cool thing is with WebAssembly we have much more optimized times, so rather than having a startup time compared to Docker of 1 second, it's 5 milliseconds, and rather than having a container focused on the operating system, that has an operating system and then your application, it's just the application itself.

So what I saw is because of these startup times were super-low, and because the container sizes rather than being in the order of hundreds of megabytes, will be in the order of just a few megabytes, so it will enable the next generation of edge computing. That means we can start thinking of having servers that run only when you request them. So rather than having to pay for full 30 days of usage, even if you've got a server with 30 requests, you might just need to pay for 30 seconds. And we can afford to do that, because we can spin up and spin down WebAssembly instances in a very performant way. Actually, that's our long-term business.

**Jerold Santo:** I was going to ask what your commercial angle was, and it sounds like you've just described it right there.

**Cyrus Akbar:** Yeah. One of the things that we are seeing now is -- I'm not sure if you saw how Google released this gaming platform, which was ultra-cool... It lets you run very cool games, that will be streamed to your laptop, or your phone, or whatever... So actually the game is executed somewhere else, but you will see the UI, the video, the streaming on your laptop itself, or whatever device you are using.

We can see this, for example, is a very compelling thing for WebAssembly... But not just in this case. You can start thinking on running things localized, of where you are at right now. And the cool thing is this binary can be shipped very easily to the remote place where it will be executed. I believe that's also going to be big, and we are seeing a lot of pushing from the industry towards that.

**Break:** \[32:02\]

**Adam Staravia:** The way we had connected with you was through Joseph Jacks; go back to the show we did with him -- Jerold, what's the number of that show, by the way? Look it up for me real quick... He introduced us to you, I'm assuming, because of his interest in the funding of future commercial open source companies, and things like that he has a general interest in. I'm curious what the back-story is into that.

**Cyrus Akbar:** How I got connected with Joseph - basically, when I started pitching the idea to investors, almost all investors were looking with candy eyes to the product... So then I knew I had something big between hands. So at that moment I started researching into what kind of investor I want to bring on board, and how they can help us. At that moment, I started looking into OSS Capital, which was the firm that Joseph was directing.

Basically, they are a VC firm that is completely focused on open source projects, because they believe in the long-term open source is going to win. It's going to win regarding companies using it, regarding how right now a lot of open source projects are able to monetize or to have value from the industry... And the thesis is actually open source is going to be big, we are going to have a lot of interest in the industry, on monetizing or spending money on certain tooling. And as long as basically we create a powerful platform, then probably the company eventually will be able to capture a certain percentage of that value generated; maybe a 5%, or a 2%. But 2% of a market that is gigantic can be super, super-big.

**Adam Staravia:** Sure. Getting there is the hard part though, right? You've got to put the work in - not just you, but others - and it is open source, so that means you tend to come in free, or funded, in the case of commercial open source. What's your state now - are you working somewhere, do you freelance? How do you and your team make money?

**Cyrus Akbar:** Right now we are not making money. Right now, our goal for this stage is just trying to get adoption, trying to improve WebAssembly, trying to basically make the barrier for entry in people or developers to WebAssembly much lower; make them tools so they can use WebAssembly in a very easy way.

In the long-term, how we will make money will be more on the decentralized computing platform, or we can call it edge computing. That's how we'll make money. But that's not something that we are focused on right now.

\[36:01\] We are a team of six engineers. The cool thing... Fun fact - before working as CEO of Wasmer, I was CTO at Try.com, and in there it was so hard to find good developers... Because we were in the fashion industry, and developers in general are not interested about fashion... But with Wasmer instead I got much more reach from people that were interested in working in this area. So the cool thing is it was very easy to get people that are very passionate into WebAssembly, and trying to attract them. It was actually not a very challenging thing... I guess because people can foresee what WebAssembly will be in the future, and they want to be part of that.

**Adam Staravia:** So is it safe to say that this discussion we've been having -- we've just discussed in the last section how we're seeing a potentially bright future of universal binaries and libraries, and this beautiful world that could potentially take over the Electrons, the Homebrews, or the Applets, whatever... That between now and then, you and your team are sacrificing and investing into a long-term future. I think that's one interesting area of open source -- obviously, open source is free, but you've got to somehow sustain yourselves until that day comes, right?

**Cyrus Akbar:** Yeah, which can be tricky. But the cool thing is if we are aligned with the investors into how we are gonna approach this space, how we are gonna eventually monetize it - if we are aligned with them, then we should be in a good place.

There are certain industries, like Uber or Lyft, that takes longer to monetize, but once you do, you will be in a very good spot. So I guess it's just a matter of trying to pitch the right idea and trying to get the right investors on board.

**Adam Staravia:** So has the idea been pitched then? Do you have investors on board? What's the state?

**Cyrus Akbar:** We pitched to a few investors. In general, everyone is very interested. We've got some cautious investors which are not sure yet if WebAssembly is going to take off, or how it's going to take off, and they wanted to stay a little bit more cautious about that. But in general, we are in a good place regarding investment, and we are more on the side of deciding who we want to bring on board and what they are going to bring - either if it's networking, or knowledge, or what they are going to bring. And based on that, we are choosing them.

**Adam Staravia:** By the way, that episode number that I could not get, and I gapped... Thanks, Jerold. Episode 320, "Venture capital meets commercial open source software, with Joseph Jacks." Great conversation. We went through the growing landscape of commercial open source, in particular this spreadsheet that he created of 100 million dollar plus revenue companies, 13 years in the making; it seems to just now be getting some serious attention. We kind of asked of "Why open source now?" and it kind of makes sense, because hey, this last year we had so many billion-dollar acquisitions in the open source space; it makes sense why there's so much more people coming.

I'm curious though, because when the herds form, people get slaughtered. Hopefully that didn't happen here. You know what I'm saying...

**Jerold Santo:** \[laughs\] Wait, "When the herds form, people get slaughtered?"

**Adam Staravia:** Well, if you're leading, you get ahead; if you're following, then that's when -- in terms of blue ocean or red ocean, for example. Blue ocean means that the landscape is open, water to be had, whatever; when you've got a red ocean, that means there's lots of people feeding off of what's there, in terms of this metaphor that's out there, around blue ocean and red ocean... You've got some blood in the water; once more and more people come into a blue ocean, it gets red.

**Cyrus Akbar:** Yes, completely. I think as a business, what we are trying to do is trying to get as much a stake of that as you can, so that when people are trying to come in, you will really have a very good position, so you can remain stronger. I guess that's one of the attractions of WebAssembly - is this starting to take off? Is this still early? But we will start seeing more companies and more companies approaching this space; we'll see how the ecosystem improves and matures... And from that, the companies that are there from the start probably will be in a very good place.

**Jerold Santo:** \[40:11\] One thing I'd like to revisit is you talking about this package manager that you're excited to be releasing. You said there's "warm install" or whatever it is, and you download SQLite.Wasm from a repository... Is this an attempt of becoming the NPM for WebAssembly? Because I think NPM would like to be the NPM for WebAssembly.

**Cyrus Akbar:** Yes. I mean, NPM is actually trying to be the package manager for WebAssembly... But the truth is NPM is designed with JavaScript in mind. The way packages work in NPM is very different from how we think it should work with WebAssembly. We are designing a package manager from the ground up, designed explicitly for WebAssembly. That means what kind of ABI you wanna use for your WebAssembly module, how they are going to interoperate... Because of that, we believe we cannot reuse a package manager that already exists, and we need to create something that is completely tailored to the WebAssembly needs.

Plus, we need no JavaScript, Node.js, and basically we want to make this package manager friendly for people that wanna use a package from Python, or want to use a package from Rust, or from PHP, without the need for them to have to install Node.js on their servers.

**Jerold Santo:** So will this be a centralized service, or are you thinking decentralized? We were talking decentralized during the break, so we're just curious what the plans are, if this will be a centralized repository.

**Cyrus Akbar:** The registry will be centralized, the main one... But the cool thing is you will be able to plug into any registry that you want. And another cool thing that we are investigating is actually to move packages to be stored in a decentralized manner, so that you actually don't depend on any explicit registry. But news to come on that a little bit later, probably in a month or so.

**Adam Staravia:** Do we have an official name for this package manager?

**Cyrus Akbar:** Yes.

**Adam Staravia:** Maybe a website, since it's coming soon?

**Cyrus Akbar:** Yes, it's going to be wapm.io (WebAssembly Package Manager). And yeah \[unintelligible 00:42:07.14\] is also super-cool. I believe the community is going to take it with a lot of attention, and I think it's going to be really great for developers that want to start using WebAssembly, or publishing WebAssembly modules from Rust, or from C, or whatever, and they want to create these universal libraries that can be used across anywhere.

**Adam Staravia:** Dream a little bit for us. Paint us a picture. Take us a couple of years in advance. Everything that you're talking about works out great; WebAssembly continues to rise and shine. Edge devices, Vastly, all these people that are really into this edge computing stuff. What you've built is amazing. What does that future look like?

**Cyrus Akbar:** I believe in general what we will start seeing is more applications or more libraries will compile to WebAssembly, and will start using WebAssembly as the main way of running things, either locally or remotely.

I think in the future we'll start seeing -- maybe the next generation of a browser are like "We actually don't depend on HTML or JavaScript", and maybe the UI is a little bit different. Or maybe an operating system where your programs load from the cloud and execute securely in their own Windows, but at a native performance, in a native way. So I foresee we'll start using WebAssembly much more for these use cases in the long-term, and we want to be there to be the provider/platform that empowers that.

**Adam Staravia:** And what about the community getting involved? Are there any inroads for -- I know you've got Spectrum.fm, or was it something else?

**Jerold Santo:** .chat, isn't it?

**Adam Staravia:** .chat.

**Cyrus Akbar:** \[43:45\] Yeah, .chat. Yes, we've got a Spectrum. Chat where we are talking with the community. I think the URL is Wasmer.spectrum.chat. If anyone wants to enter, that's one way we communicate. The other thing that we'll start doing is start being more \[unintelligible 00:43:59.09\] into the WebAssembly specification itself, to help shape it for the future. But in general, all these things -- because we are also users, so for our own libraries. Basically, what we ship, we use it internally. And because of that, it helps us to shape it in a way that actually will feed a lot of different scenarios... And the way we approach this is we create a prototype, and from there we gather information from the community, to see if basically the designs that we are doing matches different scenarios that I think we should cover... And from that, it's just a conversation, and trying to do something that will fit a lot of use cases in the long-term.

**Adam Staravia:** Do you want to give any shout-outs to anybody that's been on your team, that's really done some amazing stuff? It sounds like you've got a pretty solid team going on there, maybe even some dream collaborations, other organizations really digging into WebAssembly that you want to give a shout-out to, or say "Hey, reach out and talk to us!:

**Cyrus Akbar:** Regarding my team, I got very lucky. Everyone in my team is super-talented. They know they are much more expert on compilers, or memory utilization that I actually have ever been. I'm super-happy about every one of them. I will name them, just because probably it will make them happy: Lachlan, Mackenzie, Ivan, Brandon, Steve (who is no longer with us, but he was also very key for us), Yang, Mark... And then a lot of other people that have been contributing on the outside.

In general, companies have been reaching out and using it. One of those is NEAR Protocol. That was one of the first companies \[unintelligible 00:45:42.16\] our runtime. Right now we have other edge computing platforms that are going to use our runtime as well, which is awesome. Basically, for the listeners - if you know any use case where you think WebAssembly can be compelling for you, and you are not sure yet how to approach this space, feel free to email me at syrus@wasmer.io. I will be super-happy to see how we can use the power of WebAssembly to fit the needs that you have.

**Adam Staravia:** Very cool. Well, Cyrus, thank you very much for your time today. Thanks for sharing what you're doing. It's super-cool to see what's happening here. I don't know, will I at some point bail on Homebrew...? That would be a shame, right Jerold? That'd be a sad future; but maybe a happy future, who knows...?

**Jerold Santo:** We'll wait and see.

**Cyrus Akbar:** Yeah. Maybe we can start having Homebrew on Windows in the future itself. Or maybe on the phone. I think that will be something super-interesting. When I say Homebrew, I really mean Warm (the WebAssembly Package Manager).

**Adam Staravia:** Gotcha. Well, thanks again for your time. It's been an awesome conversation. Thank you so much.

**Cyrus Akbar:** Thank you. I really enjoyed our conversation as well.
