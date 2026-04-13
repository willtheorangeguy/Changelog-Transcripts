**Jerold Santo:** Oh yeah, the sound of those BMC _beets_ means it's that time again, my friends! What time? Well, UNIX time, 1.524762000, of course. Confused by that? Just put that in your Date class and instantiate it, but make sure you multiply it by 1,000 first, because JavaScript reasons.

Hi, I'm Jerold Santo. Thanks for tuning in if you're listening in real-time at Changelog.com/live, but you're not chilling in the JS Party chat room in community Slack - what are you waiting for? Go to changelog.com/community, sign up for free, party with us live as we record, and participate. The more, the merrier. We would love to see you in there.

What is up, Cana Downey? Thanks for making it. We have a lot of people hanging out in the Slack, and we're super excited today to have a special guest with us - Adam Baldwin, a.k.a. evil packet, head of security at NPM. Adam, thanks for joining us.

**Adam Baldwin:** Thanks for having me, this is super exciting.

**Jerold Santo:** Chris Miller is also here. Chris, you go by Bone Skull on the worldwide webs... I don't know why. Give us a quick and dirty history on that handle.

**Christopher Miller:** Oh, boy... Have you heard of a webcomic - it's an older one - White Ninja?

**Jerold Santo:** I have not.

**Christopher Miller:** It's probably obscure... But there's a webcomic called White Ninja, and people liked it, and there was White Ninja fan comics, and people would draw their own White Ninja comics and send them in, so they would publish these. One of those had an evil villain named Bone Skull, and I really thought that was a brilliant name for an evil villain, so I adopted it.

**Jerold Santo:** So you're a villain then.

**Christopher Miller:** I suppose, yeah. Sure.

**Jerold Santo:** Very good. We need all kinds of rolls around here, and Bone Skull, the evil villain, is an excellent role. Rounding out our panel this week is the incomparable Sub Hinton. Sub, how are you doing, friend?

**Sub Hinton:** I'm doing very well today, thank you.

**Jerold Santo:** So we're here today to talk about Node, and we're here to talk about security, but we can't claim that this episode was our idea, because it was the brainchild of a long-time listener, Jenn Turner. And I know that she's a long-time listener because she asked for this a long time ago. This was a request by Jenn in our Ping repo over a year ago... And to tell everybody about Ping - that's a GitHub repo (github.com/thechangelog/ping) where you can request show ideas, tell us feedback... It's an open inbox. There's a JS Party label, so if you have ideas for future JS Parties, hop over to that - there's a link in the show notes - and submit, and maybe wait a year, or faster... But this one took a year. Sorry about that, Jenn. Your patience has paid off, and thanks for being an awesome part of our community.

\[04:12\] I will just go ahead and read what Jenn said verbatim, and we'll kick into the conversation. She said she was catching up with evil packet (that's you, Adam), the creator of the Node Security project and later Node Security platform, and "I think it would be cool to hear him talk about the security goings-on." So Adam, tell us about the security goings-on.

**Adam Baldwin:** Wow, that's a very open-ended question. There's a lot going on, we could probably talk for days on this subject. Let's see... So you've probably seen in the news that my team at ^Lift Security recently joined NPM; that's probably the biggest news that I have. We joined NPM as part of their sort of security push, so we're now their internal security team, as well as working on a security product at NPM. That's the starting point...

**Jerold Santo:** When did that happen? This was all very recent, right?

**Adam Baldwin:** A couple of weeks ago. We've been working with NPM since the company started... Fun story - my first contribution ever to open source was a pull request to the registry to fix up a security bug.

**Jerold Santo:** Really?

**Adam Baldwin:** Yeah. So we've been working with NPM for quite a while, but it's just been a recent announcement.

**Jerold Santo:** So what was that bug, and what did you fix?

**Adam Baldwin:** It was a cross-site scripting bug. It was something with rendering -- either rendering README's or some portion of the package contents, if I remember correctly.

**Jerold Santo:** Correct me if I'm wrong, but it seems like cross-site scripting plus SQL injection is like 99% -- I mean, okay, buffer overflows, of course, but that's pretty much most of the vulnerabilities on the web, are those things. Is that fair to say?

**Adam Baldwin:** I don't know. I mean, I spent the last ten years doing application audits with my team, and we saw just about everything you can possibly think of. I don't really think that one class wins, because we have assessments where we don't find cross-site scripting, or we don't find SQL injection; we'll find some other bugs, some exposed keys or who knows what... It's fascinating having to go now to being an offender, right? For the last ten years we've been offence; we've been working with companies to test their applications, and now we're focused solely on NPM, the ecosystem, and so now we're going to defence.

Defenders have to worry about everything. You pick one category - one category is your starting point, but you really have to worry about all the various things.

**Sub Hinton:** I had a question for you, Adam, about Node.js in particular. Given that you've worked with security for the last ten years, you've sort of seen security before Node.js - is there anything unique to Node itself in regard to vulnerabilities that you might not see in other ecosystems? Because a lot of the information that I've read online has really been just referencing some of the OWASP Top Ten best practices anyway.

**Adam Baldwin:** \[07:37\] Yeah, I don't think there's really anything too unique to Node. Developers have implemented all the similar types of libraries and things as other languages. The OWASP Top Ten doesn't do a good job of giving examples for us, for JavaScript, for Node. You see a lot of PHP and Java examples, and I think that's reminiscent of back when that project sort of got its start. So all the same problems exist, and we do have some sort of unique things, just because dealing with the asynchronous nature of JavaScript I think, you know the \[unintelligible 00:08:19.25\] conditions in this kind of things are more prevalent... So you can get weird, interesting security behaviour because of that; that's probably one of the unique things.

The other thing too with JS, I guess - not Node specifically, but with NPM - is that we have this giant ecosystem of packages that we can sort of tap into to rapidly build our applications; that's not necessarily unique, because we have that with other industries as well, but that's definitely -- we're the largest registry, so we make use of that within Node.

**Sub Hinton:** Totally. A perfect point that Kevin, one of our other JS Party hosts, just came up in the chat was that the one thing that's kind of unique or weird about Node.js or installing packages with NPM is that a lot of those packages are used both on the client and the server, which introduces some different things...

**Adam Baldwin:** Yeah, because the security models in the browsers, as well as in the server, are quite different, right? So one piece of code might not be adequate in both places. That's a great point.

**Jerold Santo:** Another aspect of this that perhaps makes security overwhelming to many of us is that it's not just our practices that matter, it's really, well you just said the communities practices, because our dependencies practices matter, and our transitive dependencies, and their dependencies, and so on and so forth - they matter so much. I found this interesting quote in the NPM 6 announcements, which there's been some security stuff that you've done with NPM 6. Node 10 just came out, we can talk about what's new and fresh there, but this was just an interesting statement out of the NPM 6 announcements, that says "76% of developers express concern with whether the open source code they use is secure, but more interestingly, 87% expressed concern about the safety of their own code." Put another way, more developers trust the security of the open source code they use than they trust themselves.

**Adam Baldwin:** I'm curious what Sub and Chris think. Do you agree with that?

**Christopher Miller:** Well, I don't know... I mean, certainly for myself, I don't feel I'm an expert at security, just as a software engineer. Historically, it wasn't something in my career that I focused on, so from that end I feel like, well, I don't know really what I'm doing, so maybe hopefully other people do. But then again, I don't think they do either. I don't think a lot of people do.

**Jerold Santo:** \[laughs\]

**Adam Baldwin:** We're just making it up as we go.

**Sub Hinton:** I think that's a perfect point. I tend to be more knowledgeable around the IoT security side of things, so I won't say that I know a ton about web security, and to be honest, I really do rely on people that work in that field and that are passionate enough to be able to share things that make it easy for me to learn at least the really important things to know.

**Jerold Santo:** \[11:53\] This kind of goes to the two extremes of the programmer mindset which I think Chris demonstrated there, and I know I've definitely had both of these thoughts. On one side, you have "Not invented here syndrome" which is you tend to trust your own stuff better than other people's, right? And of course, that's a generic thing, but that applies to security practices as well. Then on the other hand you have -- I don't know, there's not as much of a nice term for it (maybe there is), but it's kind of like the dependency hell side, where you always reach for somebody else's code over your own, and that tells me that you don't have trust in your own software, you're just gluing bits together.

So it seems like we kind of waffle on who we trust - us or others. And like you said, Adam, maybe we are just mostly all making it up as we go.

**Christopher Miller:** I mean, I feel like I do trust open source software a bit more just because there are eyes on it, especially if it's a mature, popular package. Those issues are going to get addresses eventually, if there are enough eyes on it. It could be OpenSSL.

**Jerold Santo:** Exactly.

**Christopher Miller:** But I think as a general rule, I would trust -- two similar projects, one is open source, one is proprietary, I would probably trust the open source one.

**Jerold Santo:** And you can look at systems holistically as well. I would turn to Node.js, for instance, and I would say there are definitely a lot of interested parties, NPM of course one of them - and Adam, you're specifically a contributor - who are highly invested on the security of this thing, so I would tend to trust it, versus a similar project that wasn't so standardized or just broadly used.

The problem we got into, Chris, with OpenSSL is it was the worst of both worlds. It was completely ubiquitous, and also almost utterly unsupported, so it really took everybody by surprise.

**Christopher Miller:** Yeah. I mean, that's another can of worms, why that happens, but... Yeah.

**Adam Baldwin:** There's no 100% guarantees on either side. We're going to find interesting ways to abuse software in the future, and so we can't really be perfect forever. Something's going to come along, whether it's code we wrote or code somebody else wrote, and I don't think it's wrong to reach for somebody else's package and reuse that code... But there's not a lot of guarantee that people are looking at that code just because it's open source, and I think that's something that I'd like to change, and incentivize eyeballs on those 675,000 packages.

**Sub Hinton:** Yeah, how much static analysis can you do of code that's already out there, versus what things can't be picked up in an automated sense and genuinely needs humans to look at it?

**Adam Baldwin:** It's really hard. We did some of that early on - that was the goal of the Node security project really early on, to surface sort of like hot spots... If you just look for child\_process.exec(), for example... Back when we started the projects there was like 12,000 modules in the registry, so we could literally look at all of those modules and say "Okay, which ones are using child\_process.exec()? Oh, there's 600 of them. We could actually audit with humans every single instance of those, right?" But as that scaled, and we got that nice curve up into the right, and we're growing extremely fast - we can't automate that.

\[15:40\] The problem is that static analysis in JavaScript is really hard. It's not impossible, but it's really hard. You really need humans to validate the results of the machine. The machine finds the hot spot, and then you put that into a queue for humans to look at. That's a really efficient way of doing it. We kind of shied away from that early on, because we didn't want, sort alike are we just giving O-days out there for people? Are they going to contribute, are they not? That was sort of an interesting challenge that we had with the project, but it's still a perfect method... But full automation I don't think is -- it's not going to be easy, let's just say that.

**Sub Hinton:** That does make a lot of sense, especially given that JavaScript is very dynamic, so it would be quite difficult. Yeah, that's a perfect point, thanks.

**Jerold Santo:** Do we need more TypeScript in our life?

**Sub Hinton:** \[laughs\]

**Jerold Santo:** Another can of worms?

**Adam Baldwin:** I actually haven't spent a lot of time using TypeScript. I like anything that brings a little bit of safety in, although I do like the "I can do whatever I want" mentality, too. So the developer in me wants to say "Yeah, just let me do whatever I want", but the security person in me says "Yeah, strong types are probably nice."

**Jerold Santo:** The panellist Nick Nisi in the chat, and also in our idea document. I'd call him a closet TypeScript fan, but he's not in the closet, he's out of the closet... He's a big TypeScript fan, and he was trying to have a show called TS Party; not a whole new podcast, but an episode of JS Party called TS Party. If you think that's a good idea out there in listener land, let us know. If you think that's a terrible idea, let Nick know, and we can pass on that one.

**Break:** \[17:37\]

**Jerold Santo:** Okay, let's talk about the super fresh and new. We have Node 10, which just released, we have NPM 6, which I think was 24th April, which is two days ago - so this stuff is fresh. Adam, some of you and your teams work with the Node security platform - it's starting to make its way into NPM. Can you talk about plaudit and the other security-related features that have been announced?

**Adam Baldwin:** Yeah, as you can kind of expect with the acquisition of the Node Security platform, we're kind of wedging that work into NPM, and that'll make its way out as plaudit. The current speculation is that it's going to be very similar to what NSW was, which was you running NSW on your project, and it gives you that analysis of your dependencies deep down in the tree - do they have a vulnerability or not?

I'm not going to let the cat out of the bag quite yet, but we've added a twist to that, so we're going to go a little bit deeper than what we are doing with NSW, and hopefully it's a better experience.

**Jerold Santo:** Can you give us a peek at the cat? Can you open the bag up and just let us look at the cat for a second?

**Adam Baldwin:** \[19:44\] We're going to make Schrödinger's NPM on it, right. We're going to peek in... And we are going to see more actionable security alerts; things that are more actionable for developers. Instead of just being handed a pile of things that you really may not know how to handle, we're going to give you a little bit better guidance on that.

**Jerold Santo:** So as of right now, if I'm on NPM 6, and I type "NPM audit", what exactly happens?

**Adam Baldwin:** Right now you're going to get an error message that the registry doesn't support a NPM audit.

**Jerold Santo:** \[laughs\] Okay.

**Adam Baldwin:** But that's because NPM 6–we're getting the client out in preparation to ship with Node 10, which didn't happen... But yeah, so right now you get that message that says it doesn't currently support it. But after we get the back-end piece out of beta, you'll run NPM audit basically on any project that's got packaged JSON and a package lock, and it's going to do that analysis... It's going to submit that back to us, we'll run down through the tree, doing some analysis, and then give a result.

We had an interesting question - will registry mirrors be able to get the same audit features? We're going to have documentation on the API, so likely they'll be able to take bundle and do interesting things with it. It doesn't have to necessarily be a security audit.

**Sub Hinton:** And would you recommend that folks put this into their continuous integration system that they've set up?

**Adam Baldwin:** Yeah. I mean, CI is going to be the best place to put this. When you run NPM install, you're also going to get a summary of what might be lurking down in the dependency tree. So you'll get a summary that says "We found 254 vulnerabilities, this many highs, this many lows. We analyzed 12,000", or whatever. You'll get that little summary when you NPM install. Then during your CI process you'd see that, and then during NPM audit we can just have it exit code 1 and a failure build would be something to do.

What I want it to be though is a good experience for developers, so that as they're NPM installing something, they know it's got a known vulnerability, or as they run NPM audit... We want to keep those things out of the project, we'll keep things updated, so... CI is a great place for it; we're definitely going to support that tooling, and it's a natural place to have it. That's the majority of where NSW got put in, so I suspect we'll see that pattern quite a bit.

**Sub Hinton:** Very cool.

**Jerold Santo:** So let's say that plaudit is live, and I'm using it, and I'm enjoying its output. What are actionable mitigation steps, or how actionable do you think that mitigation will be when we find specifically transitive dependencies that are issues? Is it just "Don't upgrade", or remove a dependency? What are the kind of things that it will allow us to change to be able to take a hold of our security with our dependencies in mind?

**Adam Baldwin:** What's nice is -- you have a package lock, and we know about the dependency deep down in the tree, we can tell you what dependency to update to what version, and we know the SemVer ranges, the contracts that those dependencies have, so we'll be able to say "Update this dependency deep down in the tree, and it won't break the SemVer contract."

\[23:48\] Of course, sometimes you just don't have a version that you can update to, or there's no fix-out. In those cases, you do end up having to do a manual review yourself, so being able to have good recommendations on those security advisories, sort of being able to understand what the impact is to you. If it's top-level dependency, obviously that's easy for you to take action on, but if it's a transitive dependency, some low-level dependency - you may not have the ability to update that. That is a source of friction and something that we want to work on eliminating. That's really pull requests and getting dependence of packages to update as security vulnerabilities are published... So there'll be some work in that space as well.

**Christopher Miller:** I have experienced that particular problem before, where a transitive dependency has some terrible problem - not necessarily a security problem, but... You know, there needs to be a chain of PRs happening to get that fixed, basically. I've just kind of wondered how could NPM support or basically allow me, as the package owner, to go in and basically fix some deep dependency and have it stick? I guess I'm curious about how you might tackle that.

**Adam Baldwin:** I don't think we've got complete answers for that. That's kind of a management problem. I think we can do so with good tooling to let authors/publishers know when they have something that's got an issue... And because we had that graph - we have the dependency graph - we know which places we have to push on. As an example, if we updated this package, this version, for a certain dependency, we know the impact it has on that dependency graph, so we'll be able to focus those efforts a bit, which is nice.

Plaudit is not gonna naturally solve that problem. What it's intended to do is for you to understand that dependency tree as a developer, to be able to take action where you can take action, and make security top of mind for developers as well. We have 10 million users, and making this security something that's top of mind to developers is going to raise the floor for everyone when people start becoming aware of these things. Education will happen... I suspect that you'll see some movement just naturally in the community when these things start becoming transparent.

**Christopher Miller:** I think this kind of gets into another question I had about tooling. You want plaudit to be able to tell somebody that this dependency that they have has this problem, and if there's a way to mitigate that, and show you how, or whatever... But there are other tools right now, and I've kind of struggled a bit, like, "Which one do I use?" There's Snyk, there's NSW, there's ^Lift (or not anymore), there's the Node Source as the certified packages, and I think even GitHub is doing some dependency analysis... So it's like, which of these things do I use? Do they all keep their own database? Which is the most accurate? What's better for open source? All these kinds of questions. Because I feel like a lot of people are trying to solve this problem, and it's kind of confusing to me.

**Adam Baldwin:** \[28:11\] Yeah, you make a good point, there are lots of options out there. When I started NSW, the first comment after we built the prototype was "This belongs inside NPM", and there's a reason for that - it's because that's the tooling the developer is using every day; they have to change no habits to become aware of security issues within the dependency trees, and that's why it's a good fit. So anything that can be seamless, where you don't have to spend time and energy on socializing new tooling, or integrating something - that's a win for me.

**Jerold Santo:** I would tend to agree than NPM is the spot for tooling, the best place, for reasons that you said, for this particular thing. Anything else in addition to, or expansions on plaudit, things in development coming down the pipeline, tools that are security-focused that people can look forward to?

**Adam Baldwin:** We had a few other announcements... We obviously do have a lot more plans; there's a lot of work going on behind the scenes that we really don't talk about, like improving the application security practices within NPM, and the infrastructure, and all those things... Because now NPM has an actual security team inside the company, which is fantastic. Things that we were doing externally, audits, we're now doing them internally. So that's one thing that's going on.

CJ just announced (I think) this last week we're going to start signing packages. We're going to be PGP signing packages, so NPM is going to assert, and you'll be able to verify that the package you received is the package that you should have received... And going beyond just SHA hashing, which is good, because that also protects users that are using alternative clients like Yarn. So if you're using Yarn, and you're getting your proxy through the Yarn package domain, they technically control the tarballs and the hashes; they're just a proxy, they could do more, so we want you to be able to assert that the package you got from the registry is from the registry. Of course, this work will continue to hopefully allow additional signing in the future, but that's another piece that's coming that's fascinating.

Kearney asks about any plans for publisher signing. There are plans, the discussion has been happening for many years, and I think these are the first steps to getting to that point.

**Jerold Santo:** Getting back to plaudit, I'm going to represent ball's question in the chat... He asks if there's any distinction between "These packages do not have known issues, but have not been thoroughly reviewed" versus "These packages have been thoroughly audited." So trying to drill down at "If I run plaudit, how confident can I be about the actual security?"

**Adam Baldwin:** Yes, it brings up a very good point... Just because it doesn't have any problems doesn't mean that somebody has actually looked for it. Right now that's a problem across basically all tooling. Unless you have somebody auditing those packages, you have no confidence. The ^Lift team does audit of the top hundred modules for the NPM enterprise offering. So we do some thorough auditing of those packages and keep an eye on those, but there isn't a good indicator for thoroughly audited.

\[32:23\] This is a challenge that we had early on. I at one point could tell you that -- Chris, there is not a list of those NPM packages someplace; I could probably dig that up though.

At one point I could tell you that we audited every 12,000 of those modules early on for child process \[unintelligible 00:32:43.03\] So I could tell you that we audited those for one thing. Even then, there's going to be blind spots, so I think the goal is to figure out how to incentivize those individuals to audit things, and then to figure out how to capture those efforts. It's going to be a challenge, and it's something that we're looking forward to as a challenge... But there's no tooling that really gives you that confidence level yet.

For me, that's frustrating; it can be frustrating, but we're going to expose all the signals that we do have. Right now we have the database, and I know there are some differences in those databases. Right now we maintain our database, which was at one point in time donated to the Node.js Foundation, which sort of kindled and started up the Node Security Working Group... So they're maintaining ecosystem reports right now, so we're doing just some of that, as well as we have internal research that goes into our data set as well.

**Sub Hinton:** I consume a lot of packages that have native modules, and I'm wondering whether you've had a strategy for those packages, or if that's gonna change going forward, given that we have things like WebAssembly growing in popularity as well.

**Adam Baldwin:** Yeah, that's a fascinating topic. You have a whole different class of vulnerabilities you have to worry about, where overflows and things like that matter, right? Parsing becomes a lot more difficult. You don't have the memory safety that you do. The strategy has been -- Jon Mendoza, one of the ^Lift team members now at NPM built up a framework for fuzzing native modules, and we actually ran a class on it, and that content is out there someplace... Where using a buzzer like AFL to write test harnesses for a module and then run just thousands of hours of CPU over those, getting good coverage over all the logical conditions and throwing garbage input into it, right? That's the strategy there - if you're writing native modules, you should be fuzzing them. Obviously, your regular test cases, but... You know, he ran thousands of hours over Node's HTTP parser, and a lot of the more popular modules found interesting exploitable modules, like BSON parsing modules, and I found some crashes for like node-sass, and things like that.

\[35:46\] You also have to remember - and this is the interesting sort of edge case or sharp edge for modules... Just because there is a bug and just because we can find it doesn't mean that it's either a) exploitable, and b) exploitable in the use case for that module. You might say, "Well, I've got a bug that does a denial service for node-sass." Well, how likely are you going to take user input on the server side and put it into node-sass, like, use it as a build time operation? So that's always a consideration when looking at the security of your dependencies, as well as "Do we reach that condition?" Anyway, that's a little long-winded answer for native stuff.

**Sub Hinton:** No, that's a fascinating insight.

**Adam Baldwin:** Thanks. Check out -- AFL is the buzzer, for anyone doing native stuff.

**Christopher Miller:** I think you bring up a good point about the context in which a module is used. For example, my project is a test framework, and certainly you're probably not going to expose that somehow to the greater internet... I haven't had a security problem discovered in Mocha, but there have been security problems in dependencies of dependencies. And then it's like "Well, how important is this really?" People are going to want me to fix it or whatever, but that's like, yeah it's a DDoS but...

**Adam Baldwin:** It's not reachable.

**Christopher Miller:** Right. But it's not just that particular module with the problem, but it's whatever module depends on that module might be in a different context. It's kind of a tough call, and all you can really do is report that "Okay, this thing has a problem. I suppose that it might even be a severe problem", but for a module that uses that one with the issue, it might not be such a big deal.

**Adam Baldwin:** Context does matter, like you said. It matters a lot, and unfortunately, like I said, static analysis with JavaScript is extremely difficult... But it's not impossible. Getting better signals is going to be an important part of feature tooling for that, and it's also something that we're very conscious of. We thought that was a common complaint; it was like, "Well, this is something that's used at build time." But at the same time -- so developers also do ridiculous things with software, so you might say, well, the common case for Mocha is it's being used in this case, where if some developer might stand up a thing where you can plug in some stuff on a web page and run Mocha server side, right? It's possible, and if it's possible, likely somebody will do it... But that's your individual threat model.

For dependencies, my general rule of thumb is keep things updated. It can't hurt. It is a maintenance burden, but it's also like we've got good language to say "Okay, yes, you found this vulnerability. Yes, it's deep down in the dependency tree, it is not reachable", and that's something that we'll be working on, enabling developers to sort of signal those things within their packages, so that we could say "We looked at it, it's not a threat." You don't have to answer that 25 times or 100 times to the community. We're definitely aware of that, and we'll be hopefully helping to address that.

**Break:** \[40:14\]

**Jerold Santo:** Alright, we're going to switch things up a little bit. We've had a blast talking to Adam about Node and security and NPM and all these things, but as he said, there's a lot that's on the cusp of happening; plaudit does't' quite work yet, it's going to be there... We're going to have Adam back on a regular basis to talk about these things, answer our security questions, tell us what's new in Node.

For now, we're going to switch gears a little bit and talk about wishful thinking. So the idea for this segment is to share and discuss projects that we've always wanted to start but have never had the time, or never had the inclination to get off the ground... Crazy ideas, big ideas - whatever they are. It could be something that we hope a listener takes on and builds - if so, say that - or it could be something that you still plan on creating. In that case, be aware that you are sharing it with a bunch of strangers, so maybe you should move fast, because somebody else might like your idea as well.

Let's see what we've been thinking of. Sub, let's start with you. Do you have any projects that you haven't quite gotten around to?

**Sub Hinton:** Yeah, this is going to be a weird one, but I think that that's almost expected of me sometimes. \[laughter\] This is going to be a hardware-related one, of course, but what I've wanted to do for a long time is to design quite a small little circuit board that has a microcontroller on it and a little OLED screen or something like that, and then produce a large amount of them - let's say like 20-30 of them - arrange them all on one wall, and then mesh-connect them either with Bluetooth, or Wi-Fi or something like that, and then just let them talk to each other and just create this continually evolving piece of software that allows them to all react to each other and show different things on the screen as a result of that. This is going to be very expensive and take a lot of time and exploration, so I just haven't been able to sit down to do it yet.

**Adam Baldwin:** That sounds really cool.

**Jerold Santo:** Are you actually going to pull it off, or are you putting it out there and hoping someone else does it, and you can just look at their results? Or are you going to do this?

**Sub Hinton:** I think it's just going to be so highly individual what someone writes, so what I would actually love to do is to design the PCB and make that be the open source part of it, so that other people can then go and do that and then write their own software for it... So I'd rather that people were able to use that as a building block to then do their own, if that makes sense... Because I think there's so many cool different interpretations you could do of this.

**Christopher Miller:** Have you done PCB design before?

**Sub Hinton:** Yeah, yeah. I've done a few circuit boards, and they've mostly been artistic ones. I have a profile on ASH Park that I can actually share, but... Furthermore, I've designed like a Met card shaped one from the MTA system in New York, and I've also designed one that looks like an angler fish whose lure lights up when you hold a magnet near it... So I sort of want to take this to the next level and create a bunch that can actually talk to each other, rather than just one-off PCBs.

**Adam Baldwin:** Would they take environment input too, or...?

**Sub Hinton:** Yes. They would essentially have a bunch of pin-outs that you could just plug different sensors or different outputs into, so they would be extensible, ideally.

**Jerold Santo:** Could you somehow plug them into your body and have it gauge your mood or your temperature, and it could be like a big mood ring kind of a thing?

**Sub Hinton:** \[44:12\] \[laugh\] You might wanna talk to Scott Hansel man about that, because he's done some really cool work to do with his own body and measuring levels of things, as well.

**Adam Baldwin:** I've got some friends with little chips in their hands, an NFC or whatever.

**Sub Hinton:** Oh yeah. Rachel White, one of the hosts, actually has one in her hand.

**Adam Baldwin:** Yeah, bringing it back to security - I've heard people complain about the security aspects of those, and I'm like "It's a convenience feature." It's what it is, but... It's super fun.

**Jerold Santo:** Very cool. Well, Sub, if somebody's interested in participating with you or building this thing, what's the best way to hit you up and talk to you more about this project?

**Sub Hinton:** You can just tweet at me, honestly. I don't communicate by text message, and very rarely by email, so Twitter is definitely the best way.

**Jerold Santo:** Okay. @noopkat on Twitter. Hit her up and let Sub know if you want to participate in that project. Cool, let's kick it over to Chris. Chris, my friend, what do you not have that you wish you had, out there in the software world?

**Christopher Miller:** Well... Yeah, I leave a trail of unfinished projects, but... I've been playing video games quite a bit in the past six months or so. I just kind of got back into PC gaming after maybe about four years of not really playing things much, and kind of discovered I really enjoyed roguelike games. Furthermore, I've got this bug, and I just want to make a video game so bad. Furthermore, I don't know where I'm going to find time -- I mean, I've got a baby and a 6-year-old, and all these things, so I'm not going to have time to make a game, but I would love to... Furthermore, I mean, I'd want to.

Furthermore, I started looking at frameworks, and I was like "Can I make a reasonable game in JavaScript?" and it's like "Meh..." I mean, HTML5 games - I don't even know who plays those or where they go, or anything... Furthermore, I don't know anything about that.

Furthermore, I started looking at tools like Game Maker and Unity and stuff, and I don't know... Furthermore, I just want to go through the tutorials and maybe that'll just satisfy me. But I want to make a roguelike with like stealth elements, or something like that. That would be a ton of fun.

**Jerold Santo:** One way you might be able to find more time is to get your 6-year-old involved, and then you're not stealing time, you're making time together. Have you considered that?

**Christopher Miller:** Actually, no. That's a great idea. The biggest difficulty in that for me, I think would be art assets. If my daughter could just draw stuff for me, we could skin it and put it into the game.

**Jerold Santo:** That would be awesome! She would love that. How cool would that be, if she gets to draw something and all of a sudden it's part of a video game?

**Christopher Miller:** Yeah.

**Jerold Santo:** It'd also be I think very endearing to the players. Or not endearing, but you know what I'm saying... It'd be cool, it would be like "Yeah, this is all drawn by a young girl, and then her dad puts it into play" - I think that would be super cool.

**Christopher Miller:** \[47:51\] It would definitely be a unique game, a unique appearance. I haven't seen anything quite like that, but then again, I've stuck mostly to games on Steam and I haven't really got into what indie developers are making. I'm sure somebody has tried something like that... But that's a perfect idea.

**Jerold Santo:** Cool. Let's pass it over to Adam. Have you got any wishful thinkings out there?

**Adam Baldwin:** When you asked -- I had this weirdest project that I've wanted to do... It was just more of an experiment to see if it's possible and how hard it would be. I really like side-channel attacks, where you have an effective temperature or timing or all kinds of weird things like that, where you can measure things... So I've always wanted to know -- basically, I wanted to build an interface where it has you type a sentence, and as you're typing a sentence, you try to type another sentence using Morse code, so the timing between characters would be the signal for the other sentence.

Basically, as you're typing, the cadence between the first letter and the second letter is either a dot or a dash, which would basically type the other thing. More of like a game, or a challenge. I always thought that would be fun to build. It wouldn't be that difficult, I don't think, but I think it would be challenging to actually do - having to first learn Morse code, and then second, being able to type at a cadence like that would be... I don't know, it was a ridiculous thing I thought of one time and never ever built it. \[laughs\]

**Jerold Santo:** I learned enough Morse code to save myself in case my ship went down when I was a kid, which was "SOS." The nice thing about that is you only really need two letters, you don't even need three... But I've since forgotten it, so if I'm in a sinking boat, I'm not going to be of much use... But, I mean, who is? I was asking a lot, right? \[laughs\] "Jerold, you're not of much use in this sinking boat." It's like, "I'm sorry, guys... I used to know SOS."

Yeah, that sounds like an interesting one. It seems like that could be kind of a weekend hack. It's not like a make a video game style scope, so I feel like you could pull that one together if you ever get around to it... Very good, that's definitely right in the wheelhouse of some of the stuff that we're talking about.

**Adam Baldwin:** Yeah, I don't have free time.

**Jerold Santo:** Yeah, exactly. I'll go last here - most of my stuff that I don't build that I want to build is Changelog-related, because I'm a part-time change logger here; we don't have full-time bandwidth, so there's lots of stuff that I would love to build and haven't got around to... And one of those things is very low priority, because I don't even own an Alexa or any of the devices that Alexa inhabits... But I thought it'd be cool to have an Alexa skill, like "Hey Changelog, play the latest JS Party", that kind of thing. I hear it's really easy to do, and I'm sure it is, and I've never done it.

\[51:08\] Part of what slowed me down is I started thinking "Well, all we need is a little API, which is pretty easy", or I could do a GraphQL API, which would be a lot cooler... And then I'm like, "Okay, so first I've got to build a GraphQL API", and then I'm like "If I'm going to do that, I should do it during our Monday afternoon live streams", because that's very much an experimental live stream type of thing. Then I was like, "Well, that means I only get about two hours a week to work on this", and so I basically just like shoved a bunch of work in front of that work... So I thought it'd be cool to just make the API code be available and then have one of our listeners perhaps contribute some open source... But that's why I haven't done it. Eventually \[unintelligible 00:51:49.08\]

**Christopher Miller:** I think Alexa actually integrates with some service that pulls podcasts, and you may be able to say "Alexa, play the latest episode of JS Party", and she will be like "Yes, here it is."

**Jerold Santo:** Back when I first looked at it, those really sucked, and there was a bunch of language in between you and actually playing it... But I'm sure it may have gotten better. Yeah, if we can just submit our feeds into an index, I could have this done by the end of the show.

**Christopher Miller:** I can't remember what service is used under the hood, but yeah...

**Jerold Santo:** I think I would also be more motivated if I actually owned an Alexa device, which I don't. That would probably push me over the edge, because I'd be like "Now I wanna actually play with this thing." But I haven't got one, so... No dice. So that's it for me.

Great show, everybody. Any last words, parting words? Adam, thanks so much for joining us. We're excited that you're being so gracious to come back on a somewhat regular basis and keep us updated.

**Adam Baldwin:** Yeah, this was exciting, this was fun. I love talking about security and I love hearing the perspectives of other developers; the questions from the community were great. This was fun.

**Jerold Santo:** Alright, that is a wrap, folks. This party is over. You don't have to go home, but you can't stay here. We will see you next week. Say bye, everyone!

**Christopher Miller:** Bye, everyone!

**Adam Baldwin:** Bye, everyone.

**Sub Hinton:** Bye!
