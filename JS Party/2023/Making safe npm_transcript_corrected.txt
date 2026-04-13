**Jerold Santo:** Hello, world. It's your internet friend. It's me, Jerold, and I am here with my friend, Chris. What's up, Chris?

**Christopher Miller:** What's up?! How are you doing?!

**Jerold Santo:** Happy to see you once again. I'm doing alright. How are you doing?

**Christopher Miller:** I'm just great. Sarcasm detected... Across is also here. What's up, Across?

**Across Aboukhadijeh:** How's it going, Jerold?

**Jerold Santo:** It's always good to have you on the pod. And we are joined by a special guest, Bradley Faria's. His friends call him Bubbles; enemies call him Bubbles maybe, even. Bradley works with Across at Socket. Bradley, welcome to JS Party.

**Bradley Deck Faria's:** Hey, good to be here.

**Jerold Santo:** Happy to have you as well. We're here to talk about some of your recent work on accomplishing the impossible, which is taking NPM and making it not dangerous, making it safe. You guys recently announced this CLI tool from Socket, Safe NPM or NPM Safe, depending on your affectation... Or just Socket NPM, if you will. And we're here to talk about, we want to learn about how it works, why you built it, how you built it, maybe dive into some of the details... Hopefully, we can learn a little bit more along the way about how NPM works, the command line, how NPX works, why they're dangerous, and so on. So maybe we start off with that - "NPM install", something we all typed hundreds of times, most likely...

**Bradley Deck Faria's:** Maybe even every day...

**Jerold Santo:** Yeah. It turns out -- and by the way, spoiler alert, NPM uninstall also fraught with danger, which I learned as reading your guys' announcement. I didn't realize it could install things. It's supposed to uninstall things. Anyway, we'll save that for later. Let's start with NPM install, why it's problematic and what you all have been doing to fix that. Take it away, Brad.

**Bradley Deck Faria's:** Sure. So I was trying to figure out a little bit how to satisfy some customer stuff at Socket. We were seeing questions about how developer machines could be protected. Most of our product at Socket was done through GitHub analysis; you've done plenty of shows where people have kind of GitHub CI workflows, and things like that... But people were asking, "What do we do when we have an installation script, or security problem on a developer machine?" This was a real-world incident, as well. It happens every so often, every few years, I think, developer machines have a fairly big incident from NPM. And the question came up, "Well, why are things running on your machine?" And generally, that's going to be when you run NPM install, it might run install scripts, or it might install malware directly onto your machine. Both are possible, and so we had to spend time trying to understand all the ways people are using NPM on a daily basis.

So we had to basically write something that would let a developer transparently still type "NPM install" on their machine, they wouldn't need to update any code, but it would add protections. So we wrote a wrapper script around NPM in a way that would allow it to be used transparently, while we injected essentially some stopping points where we could do some checks. And so we actually will check for risk, and things, to let people make that decision when it occurs. It'll show the person the risk in your terminal after you type NPM install. It will be like "Oh, this has a CVE. This is a typo squat. This has installed scripts." And it just gives developers a way to pause and understand what they're about to do is risky, and even let them cancel everything.

**Jerold Santo:** Okay. So to make sure I'm tracking here... So Socket has all these threat detection tools that you all have built. And it does static analysis, it does other things, looking for typo squats, and has this corpus of knowledge about NPM packages and their level of safety, or danger, or just what it thinks about them. And there's like a ranking, all that kind of stuff. And that's all well and good for people who run it against their GitHub repos. Because if there's a problem inside your repo, when you push it to GitHub, then Socket is going to help you in that way, right Across?

**Across Aboukhadijeh:** Yeah, it'll show up on the pull request as a GitHub check.

**Jerold Santo:** \[05:43\] Right. But there's this other threat vector, which is the actual developer's machines themselves. You can also be attacked on your machine, not on your GitHub repo. And so now when I'm running NPM, whatever, I'm letting somebody else's code execute on my machine, and that can cause all sorts of other problems such as - well, they can just run arbitrary code on my machine. Once they can do that, of course, they've hacked me locally, but then they can also take that power and leak my information, or get production credentials off my machine etc. to hack servers. And so this tool is still using that same corpus of knowledge that you guys have built with Socket, and it's extending where it works. So now it works as a wrapper for NPM. Is that all right and correct, Across? Am I understanding everything?

**Across Aboukhadijeh:** Yeah, that's exactly correct. So it transparently wraps the NPM command, and you can continue then using NPM in the same way that you normally do. And if there are no risks, we won't interrupt the installation process; it will work just like it normally does. But in that small percentage of cases where there's something you want to know about, it'll give you a speed bump and ask you if you're really sure.

**Christopher Miller:** And I suppose this is configurable, and so I can say, "No, I actually don't care about this stupid CVE"?

**Across Aboukhadijeh:** Yeah. Actually -- it's funny you mentioned CVEs, because we don't even actually warn about CVEs by default, just because that's the typical reaction of the developer community. So CVEs are not the focus of Socket right now, even though we do have all that same information that you get from NPM audit, or GitHub's advisory database. Yeah, unfortunately, the typical reaction of developers to seeing CVE information is "Yeah, I already know. I've got like hundreds of those."

**Bradley Deck Faria's:** So yeah, you've seen plenty of NPM audit reports, but they do check CVEs, but they always just tell you already ran the code that has the problem. So that's their normal behaviour. So we're trying to move the knowledge forward before you install the dangerous thing, not telling you already did something dangerous.

**Across Aboukhadijeh:** And to add to that too, like, we're looking for stuff that isn't even covered by CVEs. Because when you have a supply chain attack, it's not in a CVE. It's usually some packages are compromised, and nobody knows it yet. And so anyone who's unlucky enough to install it for that period, when it's full of malware, is going to have a sad, a really sad day. And so that's why we want to step in and let people know what's in those packages before they install them.

**Christopher Miller:** And so on of the things that it will do then is if there's a new lifecycle script, like a post-install script, it will tell you, right?

**Bradley Deck Faria's:** So this is a little interesting... So if you use install scripts, we treat all install scripts as effectively equivalent, because you can run arbitrary code. So if you can run arbitrary code, a pre-installation versus post install, if they change from pre-install to also having a post-install, we will not give you a new alert, because you're already running arbitrary code when you run it. So there are a bunch of things that you might initially think are great to warn developers about, but it makes a tool completely unusable. Every time you add that speed bump... So you see this in other tools as well - they will add a speed bump every single time you install something that has, say, an installation script. And you know it has an installation script. Some of the most popular packages on NPM have installed scripts. But after you've already run the risky thing, you're effectively already host if you didn't agree with it before. So we're only going to alert you if something has changed.

And for particularly install scripts, if they add an installation script, and they didn't have any before, that's something to be worried about. But there's not really a change in risk, actually, if you just changed from pre-installed to post-install, or something like that.

**Christopher Miller:** \[10:06\] Right, yeah.

**Bradley Deck Faria's:** That was too lengthy?

**Christopher Miller:** You answered my question, but I asked it incorrectly, I think...

**Jerold Santo:** \[laughs\] Okay, ask it the right way this time.

**Christopher Miller:** Well, no, no, he answered it. It was "Does it alert if somebody adds a new script where they never had one before?" That's what I meant.

**Bradley Deck Faria's:** Yeah. But there's a real -- like, we spent actually way more time than I loved on trying to get the developer actually able to use this tool every day. And so it's really detailed in how you have to approach meeting the developer where they're at. That's the key thing, I think, for this rollout that we've had. We've had this feedback period, and developers have shown us problems with us over-alerting or under-alerting, and everybody wants different things, which is interesting to see. And you've got to find that default middle ground.

**Jerold Santo:** When you say "Everybody wants different things", you mean like their appetite for being interrupted, or being talked to is dramatically different, or varying, so that some developers are like "Leave me alone, unless this is an absolute emergency", and other people are like "Actually, I really appreciate being interrupted every time an installation script changes, or every time an --" Is that what you're saying, does people just care about different things?

**Bradley Deck Faria's:** Yeah. So they care about different categories of issues is one. Some people aren't so concerned with things like licensing, or stuff like that. Others really want everything; they want any -- even the most minute of issues. The installation script has changed one string in it, and they want to stop what they're doing until their security team can audit it, which is vastly different, I think, than most developers, who need to be able to install a React component or something, and get their day-to-day work done.

**Jerold Santo:** Yeah. Chris, what's your appetite in this way? I'm kind of a leave-me-alone kind of person.

**Christopher Miller:** I mean, it's just been way too noisy...

**Jerold Santo:** Jaded. Yeah.

**Christopher Miller:** So yeah, I'm just jaded, and just like "Oh, this is baloney. I don't really care about any of it." Yeah, I'm not the right person to ask...

**Jerold Santo:** \[laughs\]

**Across Aboukhadijeh:** Part of the problem with most of the security tooling, in my opinion, is that by focusing on these vulnerabilities, these are all theoretically going to affect you, but they're not actually all affecting you in a real way. They're all like potential ways that your app could get attacked or get compromised.

**Christopher Miller:** Right.

**Across Aboukhadijeh:** And there are a lot of problems with the CVE system, but the fundamental problem is they're all theoretical problems in your app. And not to mention the severities are all really inflated on the reports. So everything is basically critical or high, because if you use it in the exact, correct way, it could be really, terrible. But it's probably not used that way; the vast majority of these are just not going to affect you.

So I don't want to downplay -- I mean, obviously, there are very significant CVEs, that can be a big deal for you, but just if you just look at the kind of hundreds of warnings that you get on a NPM audit, how many of those are actually affecting you, or going to lead to your application getting compromised - it's a very small percentage of those.

\[13:47\] So that's the key Original Sin, or whatever, of a lot of the security tooling, which is why we've focused almost entirely on supply chain attacks, and malware, and stuff that basically if you have one of those in one of your dependencies, you will not be upset that we told you about it. You will not see it as like an interruption, or like "Why is this tool annoying me?" Like, that's the stuff we're looking for. So it's pretty different.

**Christopher Miller:** I think build what people need, not what they want, right? So...

**Across Aboukhadijeh:** Yeah. And it's interesting to hear you say that, because what you want will drastically change once you get it. So one thing that this tool does, that most other tools aren't doing, this Socket NPM, is it actually compares what's on disk already. Most tools that you use, they want big numbers. They want to scare the people; they want to be like "Yeah, we're providing value by blocking your developers." And that's not really what needs to happen. We're not trying to scare people. We're trying to let them just like "Oh, you fat-fingered the name of a package you're going to install." I did this last week, and it stopped me. It was like "That's a typo." But there was a package on NPM with that, that did things. And it stopped. That I'm appreciative for. But once you have like "Oh, I want all the warnings in the world", you really start to understand that all these security researchers are given value by over-inflating everything. "Every single possible way you can do prototype pollution is critical!" That's probably not true. "Why aren't you using this fuzzing library in your testing?", or stuff like that. And those don't actually affect that many people; they do affect some, but for your day-to-day developer, there's actually much lower-hanging fruit that malware authors are going to write towards. There's no reason for them to go to those extremes normally.

**Christopher Miller:** Yeah. I mean, when NPM Audit first came out, and Snyk, and all that, I was like "Oh, cool. Look at all this stuff." But I wanted to see all the things that were wrong, and I wanted to fix them, but that got old really quick.

**Jerold Santo:** Oh, yeah.

**Christopher Miller:** But yeah, I'm --

**Jerold Santo:** Which is why you're jaded.

**Christopher Miller:** Which is why I'm jaded, yeah.

**Jerold Santo:** And I'm with you. And this one thing I told you, Across, from the very beginning, I think when you came on the Changelog and talked about Socket, is like you need to be very careful with your false positives... Because you only have our attention, our interest, our patience for so long as a tool, until we just completely write you off. And low-context security tools that don't understand that that vulnerability is only run as a transitive dependency for Webpack, which only operates during builds of this thing, and never runs in production at all - like, how many times I have to tell a tool that. Eventually, I'm just completely done with that tool. It's just noise in my life. And so it's a challenge, I think, where you guys sit, because we have years and years and years of these types of tools, meaning security tools, that have been providing not much value, because they've had very little context into what I'm actually doing. And your opportunity with Socket is you can not be that. But then you also have to have that value moment that Brad just described, when it saves you from a typo squat, when it saves you from this thing... And those happen very infrequently. Which is great. You don't want to be vulnerable all the time. You don't want to be constantly being attacked. But when you do, you finally have that a-ha moment, and you're like "Okay, I get it." But it doesn't happen all that often.

**Christopher Miller:** The developers who are asking you to "Give me all the warnings, and all the license things, and all this, and all that", they're going to get sick of it.

**Bradley Deck Faria's:** Maybe... But there are companies that truly are like heavily security-auditing everything they run.

**Jerold Santo:** Sure.

**Christopher Miller:** \[18:02\] I don't know about who you're targeting for your customer base or anything, so... But yeah, maybe you focus on those people, maybe you have one for somebody else, that is normal...

**Jerold Santo:** Right. Or just strike a balance...

**Across Aboukhadijeh:** I think that balance is like we want to focus on the stuff that's most significant out of the box, and keep the alert level really, really low, so that every developer can just install this, and have it as like a security blanket. Kind of like how once you start using ESLint to catch -- I don't know if you guys use ESLint to catch bugs; not just the style stuff, but like the actual kind of bug-catching features of it... Once you have that -- or even TypeScript is a better example these days; you sort of feel unsafe when you're programming without it, because you're like "Oh well, this would have caught this class of bugs that I now am not like getting protected from." But you don't want it to get in the way. So that's kind of the way we want it to work out of the box. And then if some team is like really paranoid and says, "You know what - we want to be warned about every time a package reads a file, uses the FS module to read a file on my disk, just warn me about that." We can let them configure it that way if they want to... But that's not going to be how it works by default, ever.

**Bradley Deck Faria's:** Oh, that would make me cry in most situations... \[laughter\] People don't understand how many times people are writing the files...

**Break:** \[19:31\]

**Jerold Santo:** So when you set out, Brad, to write this wrapper program, surely there was -- I mean, we can tell how much thought you've put into even just the way that it operates. But actually getting it to do what it does - how do you build something like that? I assume this is a binary that you install, and then you run it, and then it calls NPM, or shells out or something, and kind of - it wraps; it's a wrapper library, we know that much. How do you build such a thing?

**Bradley Deck Faria's:** So it actually went through around three iterations, and three different attempts to do this. The first attempt was "Okay, we will match NPM's interface. We'll make our own CLI; it'll have the same commands." That's a lot of maintenance, especially if NPM updates. So this thing needs to work with multiple versions of NPM. It needs to work on old NPCs, it needs to work on new and PMS. So that was scrapped pretty quickly.

The next kind of attempt we did was "Okay, what if we just invoke the NPM CLI? It has a dry run mode built by default. Maybe we could invoke it twice. Once in dry run mode, once without dry run mode." So this actually doesn't provide enough information for you to have a good user experience. It won't tell you exactly what's being installed; it'll tell you the number. It actually has all the data, you just can't get it out of the CLI, for what it's about to do, or would do in a dry run mode.

\[22:14\] So after that, we reached once again a level deeper, and we actually wrote a wrapper script that will still invoke NPM, but it rips out a piece of NPM and replaces it with our dry run wrapper that will run in a dry run mode before it does any sort of real behaviour that writes to disk. This was actually fairly pleasant to write, compared to some other ecosystems or package managers.

We looked at a few plugin systems on other package managers. NPM actually was in a unique infrastructure position here, where they use a library called Arborist. And we only really needed to replace Arborist, it looked like. So we just had to swap out Arborist, which is what it does if you set your log level really high; you'll see this little thing logged called "Build the deal tree." That is where NPM does a full resolution of the entire module graph before it does any sort of removal of packages, or installation of new packages. And that is the only thing we really needed to replace with our first iteration of this. And so Node happily uses common JS here. This would be very hard if NPM was written in ES Modules.

**Jerold Santo:** Why is that?

**Bradley Deck Faria's:** So mocking ES Modules... I spent a lot of time -- I was on TC-39, I helped write the loader spec for Node... There's a variety of reasons. We actually have a spawn Sync call at the front of our wrapper to invoke an ES Module-only package to do something. It has like timing issues, it's very hard to mock, and has some memory leaks. It's very lucky that NPM is still writing common JS.

**Christopher Miller:** And so basically, you load the entry point and then you monkey-patch, and then that's it?

**Bradley Deck Faria's:** We actually monkey-patch before the entry point occurs. And that's where the timing is problematic for ES Modules.

**Christopher Miller:** Right. Right, right, right.

**Bradley Deck Faria's:** So there's no way for them to really stop us.

**Christopher Miller:** Well, yeah. I mean, that's how like the module-level mocking tools work anyway in CJS. You're careful not to load the thing, and then you configure it, and then you tell it to load, and it swaps it out, right?

**Jerold Santo:** So the full dry run move - was that your second iteration, or that's still happening now, like with your released version?

4:Ooh, so this is -- it's a little bit mixed now in our third iteration. The second one was we tried a fool dry run. We would just invoke the NPM CLI using --dry run. This is kind of the recommended way to do it by NPM configuration currently. But it just tells you it added X number of packages and removed X number of packages. That's the only information you can get out of the CLI.

**Jerold Santo:** I see.

**Bradley Deck Faria's:** You don't know what was removed or what was added, which can get really confusing, because what's removed and added can actually be the same package name. So Arborist is what we're using now in the third iteration, not the CLI. And we do a dry run with Arborist, and it gives you a full list of where things are going to be installed, what used to be there... So if you're updating, say you are patching a CVE, or something, if you're updating; you can see the previous version and the new version. And so we do this dry run, and then after we get all the package version information of what's new, what's old, we actually synchronize that up to our API, and then throw away actually the dry run. We don't use it again.

\[26:14\] NPM has some global state going on. A lot of npm codebases is not really built to be hooked into, and so we have to throw away that tree, even though it did a bunch of work, and do an effectively fresh install, and make sure it's only going to install what it said it would in the dry run.

**Christopher Miller:** Did you ever consider trying to do something like swapping out FS, and then having like a virtual file system, or anything like that?

**Bradley Deck Faria's:** I've thought about it, but having done that in the past, no. Let's go with no. \[laughter\]

**Christopher Miller:** Fair enough.

**Jerold Santo:** There be dragons, or what?

**Bradley Deck Faria's:** Yeah, so I have like a 2014 conference talk about writing an archive loader for Node, similar to what Electron does with ASA files. Virtual file systems are very hard to write in a way where you won't get into edge cases. It's much easier for us to intercept and take over a whole library. Because we're not changing how they're writing to disk, we just don't want them to touch the disk at all. So anything they do to disk would get really complicated fast. We'd have to understand how their cache system works, because they synchronize tarballs down. We'd have to prevent them from even downloading the tarball anyway, because we don't want to download malware at all. So now we're intercepting FS calls too, also with HTTPS calls. So yeah, it gets super-complicated.

**Christopher Miller:** So the dry run doesn't grab the tarball at all?

**Bradley Deck Faria's:** No, it only needs the metadata information to do version resolution.

**Christopher Miller:** Right. What is it called, the Pacifist? Document!

**Bradley Deck Faria's:** Document is what they normally call it.

**Jerold Santo:** Oh, my goodness... Who called it that, and why? I need to speak to the manager... So is there a perceived, or even maybe not tangible, but still there performance hit with running this wrapper? Because it seems like you're doing some dancing before I actually get my commands called.

**Bradley Deck Faria's:** There's some... There is a cache going on in NPM, so it's not as big as doing the two different runs of the CLI. But I'd say the most common thing I see is we encounter some really wild versions, or packages we haven't crawled at Socket yet... And it has to pause if it encounters a package we've never seen before, waiting on the API to do a full transitive crawl, checking all the dependencies of it. It doesn't take very long, but you might see like a spinner as it counts down the number of transitive dependencies it's trying to analyze. I was doing it this morning on one of ours, and it was like 2,500 packages on a clean installation to be analyzed... And so you just see this number just going down as fast as you can. But it's visible, the performance loss, when you do that.

**Across Aboukhadijeh:** I want to say though that one of the benefits of the approach we took at Socket is that the analysis isn't happening locally, on your machine. So when we do an analysis of a package, it's done on our servers, and that way we can cache the results for everybody. So when the CLI requests these results from the server, most of them are cached, but like Bradley said, we're not doing it for -- we're not pre-analyzing every single package on NPM yet, just because that would be incredibly expensive.

\[30:00\] We've done kind of a pre-analysis on every latest version of every package over, I think over 500 weekly downloads. So that's almost everything that you would install by typing NPM install. But if you do have some random old version of a package in your lock file, it might be the first time we're seeing it. So we'll analyze it, and then save the results, and then it'll be fast after that for everybody else, including you. That's how we designed it.

**Bradley Deck Faria's:** That's also necessary so that we don't have to download malware tarballs onto your local machine. We have to do it remotely.

**Jerold Santo:** It makes sense. So as an end user though, I have two APIs, because I'm basically reliant upon being readily available, and fast. I have to have Socket's API, and then I have to have NPM as well. And so potentially, I have two points of failure for my stuff getting installed. Chris, go ahead.

**Christopher Miller:** Oh, I was just going to ask, is this like an open source project, or what?

**Bradley Deck Faria's:** It is open source. We're not trying to make it generic yet. We have some designs on making things generic. Furthermore, we actually had to do a major UX tweak in the last week. So in particular around how people are using in NPX or NPM Exec. I don't know if you're using those in your installation scripts, but a bunch of people are, apparently. So even if it's open source, it's a little unstable, while we figure out all the interesting use cases in the open source ecosystem.

**Christopher Miller:** We use that. So there's like a lifecycle script to do a clean reinstallation of everything, right? And we want to IMAF some stuff, and so I don't have Node modules, so I use NPX IMAF, right?

**Bradley Deck Faria's:** Yeah. So we'll still intercept that. We've always intercepted that. But by default, there is no ability from NPM to prompt and tell you're about to install something, so NPX will blindly install it. Normally, it'll prompt you "Oh, do you want to install IMAF?" But if it doesn't have a terminal to prompt you over STDIN, it'll just blindly install, regardless.

**Jerold Santo:** That sounds like a security impossible problematic point.

**Bradley Deck Faria's:** We used to error on it, but this week we pushed an update. We have it on our blog post. We had to like to put down an inter-process communication server and synchronize terminals. This isn't too uncommon, and things like VS Code do it... But it was just something that we weren't expecting to do. We thought an error would be enough, but too many people are using NPX, and install scripts even. So yeah...

**Christopher Miller:** Wait, what did you do?

**Bradley Deck Faria's:** Oh, there are a lot of people who install things in their pre- and post-install scripts.

**Christopher Miller:** No, sorry, you said something about IPC, and something... I'm like "What...?"

**Bradley Deck Faria's:** Oh, that part. Yeah. So basically, the problem is NPM normally will use a pipe, and not standard IO when it spawns child processes for pre- and post-install scripts. So you can't actually be like "Please tell me if you're okay with all these risks you're about to do." NPM would just log it to a file, basically, if you wanted. You can change that behaviour using --foreground scripts, and then it won't use a pipe; it'll inherit standard IO to the child processes. But if you do that, it has a lot of weird effects. Like, it suddenly can't do install scripts in parallel; you get a lot of garbage printed to your console, because people are putting debug things in their pre- and post-install scripts...

**Across Aboukhadijeh:** Or are asking for donations.

**Bradley Deck Faria's:** Yeah, there's a lot of that. There are a lot of install scripts doing that. So we had to put essentially a server down on disk, which gets connected to by finding an environment variable. And it basically says, "Hey, I need to capture standard IO." And it tells that to the root process, doing the original NPM install. So once it captures it, then it can talk over standard IO, through the root process.

**Christopher Miller:** Wow, that's a pain in the butt.

**Bradley Deck Faria's:** It's not too uncommon in a GUI world, but I think it would be nice if more tools allowed this. The whole reason NPX has that security concern, it's because it doesn't want to do this handshake.

**Break:** \[34:50\]

**Jerold Santo:** Let's take it back to the basics for a moment for those of us who are just thinking about "Well, maybe I would use this", right? "But maybe I'm just a person who uses NPM from the command line, and NPX - I don't know very much about them... And I'm thinking what's a wrapper program? How would I -- what would I do in order to make my NPM safe in regard to this program?" Just give us like the ABCs of using it.

**Bradley Deck Faria's:** Let's see. The first thing you do is install our command line. So it'd be like 'NPM install @socketsecurity/CLI'

**Across Aboukhadijeh:** -g.

**Jerold Santo:** -g, because you're gangsta.

**Bradley Deck Faria's:** Well, if you want it to be global, yeah.

**Jerold Santo:** Oh, that's what that means? I always thought it was the gangsta flag, I always drop the gangsta on there.

**Bradley Deck Faria's:** Basically, yeah. \[laughter\] And from there, make sure that the Socket command is in your path. If it's -g, that'll be true. And then you can -- we made sure it works with command aliasing. So you just, if you're in Unix, do 'alias NPM = socket NPM alias NP = socket NP' And then do everything normally. You don't have to update your codebase, or anything.

**Christopher Miller:** No API key, or anything like that? Not for the defaults, no. So if you want other things, like org settings, then you're going to need an API key.

**Jerold Santo:** It's just too easy, Across. Just too easy.

**Across Aboukhadijeh:** Yeah, we like to make things easy. We know that developers don't want to Fitz with stuff when it comes to this. You've just gotta make it easy; gotta make it really straightforward.

**Jerold Santo:** What if I already have an alias in there that says NPM=yarn? Is it going to chain? It's just going to work magically? I'm pretty sure it's not gonna work with yarn, is it?

**Bradley Deck Faria's:** No, we looked at yarn's plugin system, and it didn't have quite the right information that we wanted. Ppm just put up a PR yesterday to add the hooks we need. I have to double-check them today.

**Jerold Santo:** Are people using yarn still? Do you guys know the numbers on yarn? I mean --

**Bradley Deck Faria's:** Which one...?

**Jerold Santo:** Which number? Which yarn? How many yarns are there?

**Bradley Deck Faria's:** So I counted six different integrations we'd have to do to support, just if you say the word yarn.

**Jerold Santo:** Okay...

**Bradley Deck Faria's:** \[38:06\] We'd have to write like six different things.

**Across Aboukhadijeh:** But officially, there are three versions that everyone uses, right?

**Bradley Deck Faria's:** Kind of... \[laughter\] I'd say five. There's five officially, because you have PNP mode, which I would actually separate out.

**Jerold Santo:** Is it worth all that effort, Across? I mean, you're the businessman. Is this worth it for the business?

**Bradley Deck Faria's:** It's one of the most updated feature requests; or most up-voted.

**Across Aboukhadijeh:** Yeah, people really like yarn, especially in big companies; a lot of customers are using yarn. We haven't committed to doing it yet, but if enough people keep asking us for it... Like Bradley said, it's one of our top up-voted requests... Which is -- by the way, it's always fun when you work super-hard on a feature like this Safe NPM, and then you put it out there, and the first thing you get is "Can you make it work in yarn? Can you make it work in Ppm? Can you make it work here?" I mean, obviously, we'll do it eventually... But yeah, people always ask for the next thing.

**Bradley Deck Faria's:** We also have other languages. Some of the other languages will be fairly easy once we get all the user experience story ironed out with this just one integration.

**Across Aboukhadijeh:** But Python package management is a whole other story...

**Christopher Miller:** I was going to make a joke about Python... \[laughter\]

**Across Aboukhadijeh:** Go ahead. Let's hear it.

**Christopher Miller:** Just like, you know, 500 integrations and...

**Jerold Santo:** Right.

**Across Aboukhadijeh:** People like to make fun of JavaScript for being crazy... And yeah, it's really eye-opening to look at the other ecosystems and realize actually we have it pretty good in JavaScript. Our package dependency format is a JSON file. It's easy to parse it, it's really straightforward, and everyone else - or not everyone else, but a lot of other ecosystems have basically these arbitrary files where you can run anything in there, and it's just a convention that they follow a certain format, but theoretically, you could have code doing anything in there; like looping, and if statements, and HTTP requests in the file that declares the dependencies. So That's craziness. That's -- yeah, we have it pretty good in JavaScript land, I think.

**Jerold Santo:** Well, speaking of craziness, riddle me this, guys - why would NPM uninstall ever install packages?

**Bradley Deck Faria's:** Yeah, this was a surprise...

**Jerold Santo:** This is what got me the most...

**Christopher Miller:** Can I answer?

**Jerold Santo:** Oh, Chris knows why.

**Christopher Miller:** I want to try, I want to try.

**Jerold Santo:** Okay, go ahead.

**Christopher Miller:** Because you can add an uninstallation, or post uninstall, or pre uninstall lifecycle script that does literally anything. Right?

**Bradley Deck Faria's:** That's one, but that's not the surprising one.

**Christopher Miller:** Okay, what's the surprising one?

**Bradley Deck Faria's:** So sometimes you have two dependencies that depend upon a third dependency. So we're going to say A and B are two dependencies; they all depend on C. But A wants the 1.1.x. So you're stuck on 1.1. But B wants anything greater than 1.0. So that means B can install 1.2, but not while A is installed. So if you remove A, NPM, I said earlier, builds the ideal tree; the perfect version of the world. And then it sees "Oh, I could actually install a newer version of C, because A is gone." And so removing A updates and installs a new version of C, which can then install more dependencies that never existed before, or whatever.

**Christopher Miller:** I wonder if this is why if you went, and you did a NPM link, and then you go, and you run NPM install, or uninstall, or something else, it kills all your symlinks, and you have to do it all over again.

**Across Aboukhadijeh:** I have a question, Bradley... Didn't NPM use to, in the old days, just install -- in that situation, wouldn't it just install two versions of C, and give A one it wants, and give B the best one that it wants too, so you'd have two copies of C?

**Across Aboukhadijeh:** \[42:10\] Oh, now we're getting into package manager fights... Yes, it originally did that. And then people saw yarn, and yarn deduped, like this does. So NPM adopted that behaviour. And now we're seeing NPM responding to Poems, kind of global shared cache as well. And it added that like two months ago, or something. So it's an ever-evolving thing. And so the only way to keep up to date is to get these hooks in some way, and we declare, like, "This is the data we need", and we write them to each integration.

**Christopher Miller:** It's unfortunate that NPM was never really built to be extended.

**Bradley Deck Faria's:** Maybe... But even with these plugin systems on other package managers, we're having to go and change the hooks. So it's hard to know what hooks you actually need until you write an actual thing to use them. And a lot of the times people are using the hooks for things, and they aren't respecting what users have already installed on disk - that's a big thing. We've been talking to a couple of package managers about this, and they were surprised that we want to know what's already on disk. So that's not usually in the plugin system.

**Jerold Santo:** So this affects your version of NPM, because it can't simply say "You're uninstalling, so you should not ever install anything, because that's actually a legitimate NPM feature." Whether it's misguided or not, it's a real feature of the package manager. And so now you have to be able to I guess - what, watch what it's doing at uninstall, and making sure that it doesn't install things that shouldn't be, but can install things it should be? Or do you just punt? How do you deal with that?

**Bradley Deck Faria's:** Yeah, so NPM was probably the easiest to do, even without a plugin system, this. So Arborist, their library for basically doing all the version resolution, and building your ideal tree, will show you any operation it's about to do. Anything it's going to remove, anything it's going to add, and anything it's going to update. And so instead of checking for "This is an installation or uninstall command being run", we always just completely take over Arborist, and whenever Arborist generates an installation or an update, that kind of stuff, that is what we're checking against. We have no consideration for the commands. There are so many ways to install stuff using NPM: NPM CI, NPM install, NPM update, NPM uninstall... Yeah.

**Jerold Santo:** So help me understand if I understand this correctly... When you install Socket NPM, are you taking your custom Arborist, are you monkey-patching the existing NPM on my system, or are you shipping a custom NPM alongside it, that I'm now using instead? Which one of those two is true?

**Bradley Deck Faria's:** So Arborist hasn't changed in years, luckily, so we're actually monkey-patching; we're not doing it on disk, we're not modifying it, so you can still use your normal NPM... But we are monkey-patching it if you go through the wrapper. And this gets a little more complicated.

\[45:42\] We actually ship a shim that will alias the NPM and NPX commands. There's like a little Bin folder inside ours, but we don't actually ship vendored versions of NPM. These little shims, we put them on your path variable, so there are some cases where tools are trying to muck with your path, and we check that our NPM is still on the path, and if you call into this shim, it will monkey-patch NPM right before it runs in-memory.

**Across Aboukhadijeh:** So it doesn't mess with your NPM at all. You can have them both running next to each other, and if you don't do the alias trick that we talked about, then you can just decide if you want to run NPM install, or socket NPM install. You can have them both.

**Jerold Santo:** But we call it a wrapper, though; you're actually wrapping a different version of NPM than the one that's on my disk, or you're taking -- or you're shimming the one on my disk, and changing it at runtime to operate a little differently?

**Bradley Deck Faria's:** Yes.

**Jerold Santo:** Okay.

**Bradley Deck Faria's:** We are using the one on your machine. So it works, I think, on anything that's not end-of-life.

**Jerold Santo:** Did you have to do anything specific in regard to Windows? NPM famously has great Windows support. One of the reasons why I think it took off as an ecosystem was that Windows developers could do lots of Node things... Was there anything that you guys had to do for Windows support, or was it just kind of baked into the cake?

**Bradley Deck Faria's:** We actually had to disable Windows support, because we found some bugs. So NPM, when you run commands on Windows, and particularly the standard way you interact with cmd.exe, it creates wrapper files, these .bat files, which use some more complicated than I enjoy shell scripting in order to just invoke the proper command. So we actually looked at how we could support Windows, and we cannot programmatically, safely - that's the keyword - invoke those shell scripts to see what they're actually about to run. So it's not supported for now, unfortunately, but we haven't had any requests to add support for it either.

**Across Aboukhadijeh:** But to be clear, we support Windows Subsystem for Linux. So that's what most people are -- most people are using WSL, so it'll work fine on that.

**Bradley Deck Faria's:** I think that's why we haven't had any requests yet.

**Christopher Miller:** Does it work if you bundle NPM with your app? \[laughs\] So if I've got a library or an app, and I've added NPM as a dependency, because I want control over what -- because my thing wants to run NPM, I want control over what version of NPM I'm running. And so how you do that - you depend on a version of NPM. Right? Is safe NBM going to hop in there, or is going to be like "I don't know about that"?

**Bradley Deck Faria's:** As long as the NPM in question is in the path as NPM, it should intercept it.

**Christopher Miller:** I mean, it'll be in Node Modules, NPM.

**Bradley Deck Faria's:** Yeah, but it has to be in the path.

**Across Aboukhadijeh:** You'd have to basically change your script to run Socket NPM instead of your local NPM, I think.

**Bradley Deck Faria's:** Not normally. If you were running it by requiring it from Node Modules, it's not going to patch that. But if you run it from the command line, it should, in all normal cases. We actually go out of our way to try to make sure your path looks correct.

**Jerold Santo:** Today's extreme edge case brought to you by Chris Miller. Chris, is this something you're doing?

**Christopher Miller:** I've considered it. It's on the table.

**Jerold Santo:** It's on the table... \[laughs\]

**Bradley Deck Faria's:** If it isn't working, let us know, because that one should be working.

**Christopher Miller:** I mean, that NPM is not going to be in the path, so it shouldn't work, right?

**Bradley Deck Faria's:** If you use any sort of NPM run, it will be in your path.

**Christopher Miller:** Nope.

**Jerold Santo:** \[laughs\]

**Christopher Miller:** Anyway, so don't worry about it. Don't worry about it. I'm not gonna --

**Jerold Santo:** \[50:08\] Give it a try, Chris, and let them know. I mean...

**Christopher Miller:** It's just... You know.

**Bradley Deck Faria's:** Also know that NPM's Bin directory is now considered deprecated... So don't rely on that.

**Jerold Santo:** Alright, guys, are there any other interesting implementation details, dragons that you uncovered and slayed/slew them in order to accomplish this? \[laughter\] Or what -- anything else left on the table that we have to pick up and chew on?

**Bradley Deck Faria's:** There's certainly stuff still left on the table for us to do. We've got a bunch of specific requests on edge cases, particularly around installations from Git repositories. We saw some interesting oddities there. Like, you can't ignore scripts from Git dependencies, even if you use NPM's configuration to ignore scripts. Like, it'll run them anyway, and stuff like that. So we could do better there. Some people want a bunch more configuration options.

**Jerold Santo:** Alright... Across, anything else that we haven't asked about this cool new tool?

**Across Aboukhadijeh:** No, I just -- I mean, I'm just glad we got it out. It's been one of the things I wanted us to build since the beginning of Socket, because it always felt like a gap in -- yeah, we're trying to stop malware, but we're stopping it in your pull requests, and not on your local machine... So it's been just one of those things we wanted to do, but we never really had the time to just like to sit down and do it. And now that we did, it's great. People really seem to like it. And I wish we did it sooner, but better late than never, so... Yeah.

**Jerold Santo:** Awesome. Chris, are you going to give this a try? Are you going to use this tool? Are you too jaded? What's your --

**Christopher Miller:** No, I'll give it a shot. Yeah.

**Jerold Santo:** Alright.

**Christopher Miller:** I want like a VS Code plugin, and I want it -- when I open my PKG.Jason file I want it to show squiggles, and stuff, of the stuff that's bad from Socket.

**Jerold Santo:** Okay...

**Christopher Miller:** So get on that...

**Jerold Santo:** Feature requests coming at you, guys. I don't know.

**Bradley Deck Faria's:** Just go to the marketplace and install it.

**Christopher Miller:** It's already there?

**Bradley Deck Faria's:** Yeah.

**Across Aboukhadijeh:** It exists.

**Christopher Miller:** Awesome.

**Jerold Santo:** Oh, those are the best kind of feature requests...

**Christopher Miller:** I love it.

**Jerold Santo:** When they already exist.

**Christopher Miller:** Yeah. Squiggles.

**Across Aboukhadijeh:** Bradley also wrote our VS Code extension, so...

**Jerold Santo:** Okay. Submit your bug reports to Bradley on that one as well. Keep them off Across' desk.

**Bradley Deck Faria's:** I really want usability improvements more than bug reports... Because people are running these all day, every day, so...

**Jerold Santo:** Alright. Well, submit your usability improvements to Bradley, not to Across, was what I was told.

**Across Aboukhadijeh:** Yeah. I mean, if anyone is interested in rolling this out as a default NPM wrapper for their whole company, please get in touch. We're talking to a few people, a few customers that want to do this, so we'd love to understand the use case more. But we've gotten interest from people who just said, "We just want to, on our default developer image, on all new laptops, just like give everybody the wrapper, so that their NPM gets that protection." I know smaller companies don't usually do that type of stuff, but larger companies do have lots of software running on the developer machine, usually, for security stuff. So if anyone's interested in that, please reach out to us, and we'd love to learn more about how you'd want to do that, and help support it.

**Jerold Santo:** Very cool, guys. Well, thanks for coming on the show, Bradley, Chris, and Across. It's always a pleasure. Of course, all the links to all the things that we referenced on today's show will be in your show notes. That's JS Party for this week, and we'll catch you on the next one.

**Outro:** \[54:06\]

**Jerold Santo:** I'm a yarn user, so... Sorry, guys. Not that I really have a preference to yarn; it was like, when it first came out, it was so much faster that we just switched over to it. And I think NPM is probably just about as fast now, because they did a bunch of work after that... And now it just bugs me that I have to use yarn, because I use NPM on, so many like small things, and then on our main project I have to remember how to use yarn... And then I'm like "What's it? Yarn I instead of this, or yarn add...?"

**Christopher Miller:** Can you switch back easily, or is it too integrated at this point?

**Jerold Santo:** No, I can switch back. It's just like inertia-based?

**Bradley Deck Faria's:** It's a huge, huge amount of effort to make this work with yarn.

**Jerold Santo:** Yeah... I would almost just like wait it out, you know...

**Bradley Deck Faria's:** Maybe...

**Jerold Santo:** Eventually, all of us yarn people will be dead or moved on? I don't know.

**Bradley Deck Faria's:** Because there's also Bun now too, which - we talk to them. All sorts of people.

**Across Aboukhadijeh:** And what's the other one? Demo, yeah. Also, Demo. Which is all --

**Bradley Deck Faria's:** I guess they do PKG.Jason now.

**Jerold Santo:** Yeah, Demo's a whole other ball of wax.

**Across Aboukhadijeh:** I think yarn got so much help from -- adoption really started when NPM was kind of in its... There was like a little bad period where not much was happening, and it was this perfect competition that showed up, that was like "Well, why is NPM not deterministic, and why is it slow? Let's fix all this." And that competition made them up their game, and now a lot of the benefit -- like Workspaces, and all that stuff was perfect, and now a lot of those reasons have gone away. But yeah, I don't know, I'm not really a yarn user, so I don't know what other reasons people use it for as well, but...

**Jerold Santo:** Right. Well, I'll tell you what mine was; it was a straight-up -- I was in that malaise where I was like "Why is this taking so long?" And I was like "Oh, another tool that does the same thing, but faster?" Easy switch-over, I was just like "Let's do this", and then I just stayed there. I wonder if -- is that going to be the Demo story? Is it going to be like "Demo came in and made Node to do a bunch of stuff, and now they stepped up to the plate, Node got better, and Demo kind of just like stayed fringe" or not? I don't know.

**Christopher Miller:** I don't think Node has done anything in response to Demo.

**Jerold Santo:** No?

**Bradley Deck Faria's:** I mean, they've done a bunch... They have the HTTPS imports, but it's flagged due to nightmare-level security problems of just that security model. We have - the permissions model gets unflagged this month, for all those...

**Across Aboukhadijeh:** They have web APIs, like the file API, blobs and stuff...

**Bradley Deck Faria's:** Yeah, they've got a lot now.

**Christopher Miller:** The test runner...?

**Bradley Deck Faria's:** But I think that's the problem with differentiating features. "We do this, but more." You're just telling the original people to ship more; you're not really bringing something new to the table.

**Jerold Santo:** Brand new.

**Across Aboukhadijeh:** Yeah. But if they were staying -- yeah, maybe that just means they need to go faster and add more stuff, and just be ahead.

**Jerold Santo:** Right.

**Bradley Deck Faria's:** Well, they've had to carve backward. They just added PKG.Jason.

**Jerold Santo:** That's right, they did. I asked Ryan that when he was on the show about -- I feel like what you could come out and say is like, with Demo, you can build this type of application that you can't build with Node. Like, it actually has something that's new and different, that's like "Actually, you're going to need a Demo thing to get that done." Does it have anything like that? And it was more like "No." He's like "You can build anything in the world you want with Node." It's just like "This is me doing Node the right way, or what I think is the better way." And so it's like better Node; it's not like "By the way, there's a brand-new class of apps." Like, that's the kind of stuff that I think is more disruptive, right? Versus just more, or just different, or just better in certain miniscule ways that can be easily caught up to by effort... I don't know.

**Across Aboukhadijeh:** I mean, isn't that the story of all of JavaScript? It's like, people have always said, "Well, if we could just do it over, and do it the right way, wouldn't everything be better? Like, why are we using this bad language?" There's always that argument. And then it's always never really panned out for those people. I'm not saying that's exactly the argument he was making, but it sounds a little like it.

**Jerold Santo:** Right.

**Across Aboukhadijeh:** I mean, no one really cares about the words in the language that much to switch everything over to something new. If that's the only benefit, is that "Oh, it's nicer in some aesthetic way", that's not really going to make a difference for people enough. It needs to be like 10x better to get over that inertia. \[laughter\]

**Jerold Santo:** That's a mic drop moment...

**Bradley Deck Faria's:** Yeah. Honestly, I think Bun's gonna just be the biggest problem for Demo.

**Jerold Santo:** Because it's going to steal some of their inertia, their attention?

**Bradley Deck Faria's:** So Demo requires you to have a Greenfield project to really excel; it requires you to write something that doesn't have as many tutorials... It also requires you to have this security system that you always have to disable in production, for the most part. It's just a very strange thing. And then Bun came along and was like "Okay, we're going to take the TypeScript integration idea, we're going to take the Node modules install thing to speed it up, and we're just going to strap that onto Node." And that is a much more compelling thing than having to rewrite any sort of software.

**Jerold Santo:** Well, I mean, taking a cue from TypeScript's playbook - the fact that it's a superset, and it's just adoptable, and you don't have to rewrite anything. Like, you're literally already using it. One of the reasons why people are like "Oh, okay, I can just change this to .ts", or not even have to do that, and try this out. That's a huge advantage for any sort of adoption, is like "Well, be a superset", or be API compatible. It's much harder to start brand new. I mean -- but you get more radical ideas that way, I guess... Assuming that your ideas are radical in the first place.
