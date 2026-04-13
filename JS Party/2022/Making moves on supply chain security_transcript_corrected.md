**Nick Nisi:** Hello, party people! Welcome to JS Party. I'm your host this week, Nick. Hoy-hoy! Welcome. We are very excited -- well, first off, let me introduce my co-panellist here, and that is Chris a.k.a. skull. How's it going?

**Christopher Miller:** Hi! Great. Super.

**Nick Nisi:** Wood!

**Christopher Miller:** Wood!

**Nick Nisi:** Welcome back. I haven't been on the show with you in a long time, so I'm very excited to be here today.

**Christopher Miller:** I hope to not disappoint you.

**Nick Nisi:** You never could. \[laughs\] And with us as well is JS Party regular, Across Aboukhadijeh. How's it going, Across?!

**Across Aboukhadijeh:** How's it going, Nick?! It's great to be here.

**Nick Nisi:** Yeah, welcome. Now, we are talking about a very exciting, new project from you called Socket. You have a couple of guests on as well to talk about that with you. First off, we have Mich Lysenko. Mich, how's it going?

**Nikola Lysenko:** Hi. It's going pretty good.

**Nick Nisi:** Awesome. Tell us a little bit about yourself.

**Nikola Lysenko:** Yeah, I mean, I've just been doing a lot of Node and JavaScript stuff since like the pretty early days of these things.

**Nick Nisi:** Nice.

**Nikola Lysenko:** I did a bunch of WebGL things maybe ten years ago, and done some work with numerical computing... Then previously I was out in China, working on some MMORPG browser game things, which -- it's still running, basically, but now I'm back in America, post-COVID, and working on this.

**Nick Nisi:** Nice! Very cool. That is a lot of wildly varying things, I was going to say, and then I realized that --

**Nikola Lysenko:** There's more stuff. I gave a bridged version. I don't wanna lock in that.

**Nick Nisi:** Oh, for sure. But that's like such a cool and unique segment.

**Nikola Lysenko:** Yeah, I've got a blog, actually. 0 FPS. It's got a bunch of voxel things, and stuff like that.

**Nick Nisi:** Oh, nice. 0 FPS. We will add that to the show notes, so people can check that out. And then with us as well we've got Bret Comes. Bret, how's it going?

**Bret Comes:** \[04:04\] Good! Great to be here.

**Nick Nisi:** Welcome. Tell us a little bit about yourself.

**Bret Comes:** I'm a software engineer, an open source citizen, I've been doing Node for a long time, since like maybe 0.12... Contributed to a lot of projects, and worked on a lot of little small projects of my own... So yeah, just kind of living the JavaScript life.

**Nick Nisi:** Very cool. Well, yeah, I think it's safe to say that we're all JavaScript fans here... So we're talking about this exciting new project that the three of you are working on, which is called Socket. Across, do you want to take it away and tell us what Socket is?

**Across Aboukhadijeh:** Yeah, sure. So Socket is a platform that protects your apps from supply chain attacks. A software supply chain attack is when a JavaScript package gets taken over by a malicious actor. It can be compromised, hijacked... We've also seen maintainers go rogue and sabotage their own packages... And when this happens, the apps that you're building that use open source, packages will get compromised as well, because they're built on open source dependencies.

The average app has something like 90%-95% of the lines of code in the app coming from open source packages. The average JavaScript app has thousands and thousands of these dependencies. I think last I checked the Hello World of a React app has like a thousand dependencies.

So yeah, there's a lot of potential for bad things to happen if any of those get compromised, and so Socket is sort of an attempt at solving that problem and making it safer to use open source.

**Nick Nisi:** Very cool. That is awesome, and terrifying. I'm just thinking about that React example. It's so nice that I can easily spin up React and have a Hello World immediately, but there's so much happening that I don't know about, because I've never really dug into what's actually being pulled down.

**Christopher Miller:** To be fair, that one is particularly egregious, so...

**Nick Nisi:** Yeah.

**Nikola Lysenko:** It's actually kind of surprising that bad things don't happen more often. It is still a relatively rare event, but even rare events at scale are actually very common.

**Nick Nisi:** Yeah, that is a good point. Generally, people seem to be pretty good about being good stewards of open source. You all are a very good example of that... But when supply chain attacks do happen - you hear about them a lot. And it's happening more and more, because we have so much more interconnected dependency on open source - or seemingly so, right now - that any kinds of problems like this just immediately rise to the top of our attention feed.

**Across Aboukhadijeh:** Yeah, it's both a blessing and a curse. We can build apps so much faster because all this great, free code is out there... And for the most part, it feels pretty costless to add dependencies to your app. It helps you get your job done faster, it helps you solve problems that you might not even know how to solve yourself, or not want to go and learn how to solve... And that's why we can build stuff so quickly today. That's why a team of like two or three people can build a really complicated app, that would have taken dozens of people to build before.

So it's really great, we're not against using open source; we just think that with the threat of supply chain attacks increasing, we need to take some steps to responsibly use open source... In the same way that it's become pretty common to scan for vulnerabilities in your open source packages. We think that scanning for supply chain attacks is a logical next step that the industry and all developers need to start thinking about and implementing in their apps to make sure that their open source is safe from supply chain attacks.

**Christopher Miller:** A question I've seen thrown around recently is "What if this happened in JavaScript land? Why is it a thing with NPM packages?" And of course, there's a lot of speculation as to the reasons why, but what do you think it is?

**Bret Comes:** \[08:01\] I think it's because the scale of the JavaScript ecosystem is so much larger than every other ecosystem... Kind of like rare cosmological events. Like I was saying before, when you have large-scale numbers of things happening over and over every day, like people installing packages every day, things getting published every day, even if it's a very small probability of somebody introducing one of these vulnerabilities, just the sheer number increases the count of those that you see.

**Nikola Lysenko:** Also, it's like, everyone has some JavaScript in their tech stack... It's like, back in the old days, would you bother writing viruses for some obscure Linux that runs on like a toaster? It's not worth it. So if you're an attacker, you're obviously going to go after JavaScript, because that's where the money is, right?

So yeah, we're going to see them there, and then as it gets more locked down, and we figure out how to fix it, the little cockroaches will scurry off to the other places where it's more vulnerable. So we're coming for you next, Main, we're coming for you Python. We'll get you! They're just next, that's all it is. We're just the biggest, so we're going to get hit first.

**Nick Nisi:** Yeah. That is such a good point though. If you're not a Java developer, you probably won't be using Maven. If you're not a Ruby developer, you're probably not using Ruby Gems. But all of those projects are probably using NPM. Because if they touch the web, they probably have some JavaScript in there. That really highlights how wide-ranging and vast the JavaScript landscape really is, compared to other languages.

**Bret Comes:** The other element to this is that Node introduced nested dependencies early on in the language. That whole module system essentially scaled too well, relative to the state of Python or Ruby at the time, which had shipped module systems that all required system-level dependencies where you couldn't have two projects installed at the same time on your system, just by default. You had to use extra tooling. So there was an intrinsic sort of resistance -- you know, like, some pain there involved... Whereas in Node it was just the natural thing; you could just install anything you wanted. There's almost no cost initially. That's sort of what caused it to scale up to what it is today, in a sense.

**Across Aboukhadijeh:** Yeah, the average NPM package has 79 dependencies. It's what I saw in a paper from earlier in 2021. I find it hard to believe; that seems like a lot, but yeah, that's what they've found. 79 dependencies... Including transitive, obviously.

**Christopher Miller:** Including transitive dependencies?

**Across Aboukhadijeh:** Yeah, a total. So the average NPM package had 79 total dependencies, yeah.

**Christopher Miller:** That seems low. \[laughter\]

**Nikola Lysenko:** It depends on what corners of NPM you hang out in.

**Bret Comes:** Are those for packages, or projects? There's also that distinction where projects need a lot of dependencies, and packages need a few less, but they also multiply in the package... So is that for just modules?

**Across Aboukhadijeh:** Yeah... I think they were looking at all the packages on NPM, and then just figuring out how many total dependencies they had.

**Bret Comes:** That's wild.

**Across Aboukhadijeh:** But yeah, that seems high for the part of NPM that I hang out in, I guess. There's so many sub-communities in NPM...

**Bret Comes:** In the React ecosystem that sounds about right, so...

**Nick Nisi:** Yeah...

**Bret Comes:** Maybe they're \[unintelligible 00:11:12.13\] dependencies too, so...

**Across Aboukhadijeh:** Yeah, they're probably including dev dependencies.

**Nick Nisi:** I can tell you, I have switched over my Git workflow to exclusively using work trees in a bare repo... And that means that I'm constantly creating new work trees and then pre-installing and then deleting those work trees... And on my M1 Mac it takes about five minutes to just delete the Node modules; it just sits there and hangs. There's so much going into all of that. That's not a very scientific number, but it takes a long time, because there's a lot there... Which is amazing.

So there are a couple of tools out there... NPM specifically has an audit command that tells you some information about packages that they're using, and it highlights some things in yellow, and red, and yells at me a lot... And then there are other companies, like Snyk, that I've seen on PRs and things like that... Can you tell me, what does Socket do differently? Or how does Socket compare to the existing landscape that's out there?

**Across Aboukhadijeh:** \[12:13\] Yeah, so I think it's worth maybe just spending a second distinguishing between vulnerabilities and malware.

**Nick Nisi:** Okay, yeah.

**Across Aboukhadijeh:** I think vulnerabilities are when the maintainer of a project makes a mistake in their program, they introduce a security bug, and then a security researcher usually finds and reports it to the maintainer, they get it fixed, and then a report is written up, and it goes into a database of all the known vulnerabilities. Basically, this database just tells you which versions of packages you ought not to use anymore, and what the safe version is that you should update to.

That's basically what stuff like NPM Audit and Snyk are looking at. They're basically looking through your project and making sure that you're not using any of those versions that are known to have problems. And that's great, everyone should do that, it's useful; you don't want to be running code that is known to have these problems.

Now, that's very different from a supply chain attack and malware getting into a package, because when one of those gets into a package it's usually -- it's not like a thing that you want to run on your computer for even like a moment. You can run a package that has a vulnerability on your computer, and it can be fine; you can even deploy to production if it's like a low-severity vulnerability, and it probably won't affect you for a long time, or ever... Especially, there are a lot of these vulnerabilities -- I don't know if everyone is familiar with regular expression denial of service, but that's the one that we all see constantly in NPM Audit. It's in a lot of stuff, and it's bad, but it's not the end of the world.

**Nikola Lysenko:** Especially in a CLI.

**Across Aboukhadijeh:** Yeah, especially in a CLI, especially in dev tools. So that's why vulnerabilities are good to get rid of, but it's not the end of the world. In fact, you probably have multiple known vulnerabilities that you're ignoring right now in your project, and just hoping to get to later, right? Whereas if you have even a single supply chain attack in your Node Modules folder, you're going to have a very bad day if that happens. You're going to have cryptocurrency miners running on your computer, you're going to have your environment variables being sent off to some random server to an attacker, you're going to have passwords being harvested from different apps on your computer, you're going to have your files being deleted... These are all attacks we've seen in the last few months, that are real supply chain attacks that have happened.

So this is kind of a different threat, because it's so much more drastic; what happens is so much worse. And it's also a thing where you don't really have much time to react to it. So when a package is compromised, if you install it at any point after it's been compromised, and before it's been caught and removed from the NPM registry, then you're owned. It's bad; you have to clean up your servers, you have to probably redo your whole computer and assume everything on it has been tainted... It's not a good place to be.

So you don't want to have a very reactive approach, where you're kind of like waiting for these reports to be written and get added to some database, and then check that database. That's just too slow of a process. You'll need something that actually can look at the code and figure out "What is this code doing? What is its behaviour gonna actually be?" and to warn you if that behaviour has changed in some way that's really suspicious or indicates that it might be a compromise in some way, and then warn you before you run it; before you install it, and before you run it on your laptop or on your production servers.

So that's the difference. Socket looks for that, and it needs to therefore have a proactive approach. That's very different from existing tools.

**Christopher Miller:** So how does that work in practice? Does Socket act as sort of like the gatekeeper, sort of, to upgrades? Or what happens there?

**Across Aboukhadijeh:** Yeah, essentially. So the current thing we provide is a GitHub app that you can install, and it watches all changes to the package.Jason file, package lock file, Yarn lock, whatever you use. And when a new dependency is added, or a dependency is updated, it will look at it and try to figure out whether it has security issues.

\[15:59\] So the current thing you can go install on our website just looks for typo squats, which is one of the number one -- I think it's the number one or number two supply chain attack that happens right now, which is basically when somebody registers a name that's one or two letters off from another popular package and hopes that people accidentally will install it. So we'll look for that, and we'll warn you if one of those dependencies is about to get into your app.

And we have a bunch of other things we can detect on our website, which we're now gonna work on adding to our GitHub app as well, to protect you from other stuff, like suddenly an installation script is added, or suddenly a network access is happening, or suddenly files are being read and sent to some server. That kind of stuff. So that's coming in the coming weeks and months.

**Christopher Miller:** Is Socket mainly targeted towards applications and not necessarily libraries?

**Across Aboukhadijeh:** I think it can be used on libraries, too. Anything that has a package.Jason file with dependencies in it. A library can use it to protect itself, and make sure that its dependencies are good. So yeah, there's no reason why you couldn't use it there as well.

**Bret Comes:** On my modules I want to get warnings on my Dependabot updates if there's something weird about them, or something fishy is added in this new package...

**Nikola Lysenko:** Yeah. You can think of it like almost like if you're using Dependabot, you should probably be using Socket, too... Because if something's automatically bumping your versions, you also ought to be automatically checking those versions, basically. If Dependabot says "Update this", then maybe in the future Socket will say "Whoa, hold on. Maybe take a look before you do that. It might not be a good idea."

**Christopher Miller:** Right. A lot of these supply chain attacks that we see now tend to be in transitive dependencies. You may have pinned your dependency, but your dependency didn't pin the transitive dependency... So anybody pulling down your app or your library or whatever, is going to get that new version installed, right? And so it's on that user to go and use Socket too, right? It's not my problem anymore, because -- or how does that work?

**Nikola Lysenko:** Yeah, we scan transitive dependencies. It's the whole dependency tree for all packages and all versions that you have. So it's a holistic, deep scan of all dependencies.

**Across Aboukhadijeh:** Of course, this is assuming that you have a package lock file in place. So if you have a package lock file, then we'll look at the actual versions that you're installing, all the way down the tree.

**Nikola Lysenko:** Yeah. If there's just a package.Jason file, the best we can do is make a guess about NPM install will do. But there's always going to be a race condition there, because NPM could update between when we do the scan and when you do the deployment. So for safety purposes, you should just use a package lock file. But if it's not there, you could make a pretty good guess about what's going to happen, so we do the thing as like a fallback.

**Bret Comes:** In module development though, even if you have a package lock for your development and your tests, the consumers who are installing you - they don't get those guarantees that your model does.

**Christopher Miller:** Sorry, that's what I was trying to say.

**Bret Comes:** Yeah. I think we're still thinking about that use case.

**Nikola Lysenko:** You could do NPM shrink wrap, but that can sometimes cause dependency -- like, exponential bloat, basically.

**Bret Comes:** As a module maintainer, I actually appreciate and practice the package lock-free development workflow, because in some sense you get a more accurate picture at any given moment like what your actual consumers are going to be seeing.

If you test against the lock file of the module, you actually might miss -- you rerun that test, it's gonna work exactly like you ran it two weeks ago; but if you ran it without the lock file, you actually see what it's doing today.

I think we're still brainstorming how to handle that use case... I've thought of ideas other products have done, almost like a iron test on things, just to see what's going to happen without the lock file. So maybe there'll be something like that in the future.

**Nikola Lysenko:** Yeah. In the future we can also rerun them, but there's still going to be some delay between when we detect the change and when the analysis is actually done for that... And then if you deploy before it's done, you're going to miss that.

So practically speaking, the only way you can be confident that what you're testing and deploying is what's actually running is to have a lock file. So if you're consuming and deploying packages, you definitely need a lock file set up. And if you don't want to do it, that's fine. It's your choice. But you're taking a risk, basically.

**Bret Comes:** \[20:08\] Yeah. So ultimately, if you're deploying a project to some sort of production environment, that line will -- if they have Socket installed, they'll get the analysis at that level for the entire tree as well. So that's kind of the idea at the moment.

**Nikola Lysenko:** Yeah. So just use a lock file, man... \[laughter\] Like, why do you want to be so weird about this...?

**Christopher Miller:** Well, I look forward to what you come up with in the future for module authors and library authors for that.

**Bret Comes:** Yeah, for modules that's the thing. There's kind of a gateway -- like a little gate in front of projects getting deployed to production, and that's kind of the gate we're at right now. I'd like to see it move more into the module ecosystem as well. For example, maybe rather than just reacting to changes in the pull request, we could open an issue if something weird shows up in your whole tree, so...

**Across Aboukhadijeh:** If a new version of a transitive dependency has been published.

**Bret Comes:** Yeah, like a weekly or daily report or something.

**Nikola Lysenko:** Yeah, that would be pretty cool.

**Break:** \[21:04\]

**Nick Nisi:** So you have this site, socket.dev, and it's really cool that you can go in and just start using it to search for packages on NPM. And then you can get information -- like, one thing that I really like about it is there's a score for different things, like supply chain security quality, maintenance vulnerabilities, and license score. I love that. Not to compare it to Lighthouse, but it is almost that approach, of kind of gamifying your security, which I think is really cool, and a good way to get people to pay attention to it more, for better or worse.

So I was just curious if you could walk through a little bit of what you get when you go look at a package on Socket.dev. I'm looking at React, for example, but any package. What is it telling you there?

**Across Aboukhadijeh:** So when you go to a package page, you get those scores you mentioned. They're basically a composite of a bunch of different issues that we look for. We do static analysis of the package and look for specific -- what we call issues, or red flags. They're basically things that you want to know about in a package. Stuff like the package uses the file system, talks to the network, runs shell commands... Maybe the package looks like a typo squat, or it's unmaintained, or it's deprecated, or it's known malware, or it has a high number of Codes, or was refactored recently with a major refactor, or it doesn't use an open source license... There's all these different issues; we have like 70+ issues that we look for...

**Nick Nisi:** \[24:03\] Wow.

**Across Aboukhadijeh:** ...and you can find -- basically, whenever a package has one of those that's really severe, we highlight it right there at the top of the page, so you'll know before you install it and add it to your project. And the cool thing is if you use Socket, you'll even get told if the package has like an installation script that's going to run, and it will even give you a link directly to the -- Mich actually implemented that part; you get a link directly to the line where you can see what that install script would do.

**Nick Nisi:** Oh, that's cool.

**Across Aboukhadijeh:** It's really cool, yeah. You don't need to install it and then be surprised that some install script is running. It's just a really basic feature that's super-useful to have. So that's the kind of thing... And then we summarize all that into the scores that you see at the top of the page. Those are in beta right now, we're working on improving them, but they basically give you this high-level kind of summary of "Okay, this package has like a zero on its supply chain security. Maybe I should figure out what is it doing that's giving it such a low score", and maybe maintainers can improve their packages by looking at that.

**Nick Nisi:** Nice.

**Nikola Lysenko:** Yeah. It's not just issues, too; we also collect a bunch of other statistics, and all of this feeds into the scores. So the Lighthouse analogy is exactly where we're working from with this stuff. And expect the list of things that we check to get improved over time. The current version is very close to like a minimum viable product to get it up and running and bootstrapping it... But every day we're adding more stuff, and it's getting better, so it's going to keep improving in terms of what it can catch.

Now, to go back to something earlier, with React - it's interesting that on the React page there's actually a kind of bug with the analysis on that package, where it says "There are no tests on React", which is actually true. There are no tests in the React NPM package, because what React does is when they publish their package online, they actually go through and delete a bunch of code, and do some kind of complicated packaging build step to ship it out to NPM before they do that... Which - hey, I guess if they want to do that, that's their choice... But what a lot of people would do, if you're looking at, say, NPM or some other website for inspecting a package, you typically would like to look at the code for that package before you download it and install it. And a lot of people I think may naively assume that the code that they see on the GitHub repository is in some way related to the code that you get in your NPM package. But NPM makes no guarantee that these two things are even remotely correlated. There's no check that NPM does that the GitHub repository code looks like the package code. And currently, short of just installing the package, there's no easy way within the default NPM ecosystem to just say "Okay, what's going on actually inside this package?"

So at the moment, Socket does not really look at the GitHub side of things at all. We will bring more of that into our analysis in the future, but we're very focused on what's actually in the package.

So all the scores and all the data that we have reflects the content of what you would get if you install it. So in the case of React, because they modified the code from GitHub, and they deleted all the tests, there are no tests in their package. So you probably want to look around inside them. And this is actually a common way for people to sneak in a vulnerability or something kind of sketchy, if you're not looking for it. Because they can just say "Oh yeah, I have a totally legit package on GitHub, but I can put something sneaky in it when I send it out to NPM", and then if you install it, you're going to get owned. But with Socket you can actually look at what's actually in the package, and see what's in the code, and poke around in there, and we have contextual links and navigation, and you can look at what it's actually going to do if you were to install the thing on your computer. So if someone's going to go AWOL or whatever, with tests or whatever, you probably want to know that.

In the case of React, we can probably in the future, for tests, once we're ingesting the GitHub data, say like "Oh, they don't have tests in their package, in their NPM file, but we've found them in the GitHub repo, so maybe it's okay..." But that's not implemented yet. Eventually, I think we will get there, but we're not quite at that stage right now.

**Christopher Miller:** This is like a debate, "Should you publish your tests?" Right? In your experience, what percentage would you say of the packages publish their tests versus don't?

**Nikola Lysenko:** From what I've seen, only extremely weird people care about this and delete their tests. I don't know why it's a big issue, actually.

**Bret Comes:** \[28:17\] It's an extreme optimization.

**Nikola Lysenko:** Yeah, yeah. It's like, "What if we delete all our white space in our package file, too? We shouldn't publish anything that's not metal" Like, I don't know; I guess if you really want to do that, but... Why?

**Across Aboukhadijeh:** Some people also minify their files that they publish in their packages. Or browser or webpack the code, so that there's only one file that needs to be required...

**Bret Comes:** There are reasons for them to do that...

**Across Aboukhadijeh:** Yeah, I'm not trying to say that people should never do that. There are definitely some pros to doing that. But it does definitely make it harder to figure out what's going on in the package... Because you now open it up, and it looks absolutely nothing like what's on GitHub, and you're just hoping that nothing has been snuck in there. So that's where it really helps to actually see what is the code doing.

**Nikola Lysenko:** And this is why we have a concept of supply chain risk. It doesn't mean that they're doing something bad, but now it's more likely they could do something bad. So if they're deleting tests, if they're minifying their code and doing all this other stuff, you must be a little sketched out about that. And maybe it's fine, but it's like processed food; you get a little bit of cadmium, or nickel contaminants here and there... And maybe one or two is okay, but the cumulative effect can give you terminal brain cancer.

**Across Aboukhadijeh:** The other thing too is I think there are things we can do with our scores and with the stuff we show on the package page to maybe encourage better practices... Not that we want to create a lot more work for maintainers, but there are certain things, best practices that I think it would be great if we could make more normal... Something like being able to say "We took the GitHub code, we ran NPM install, NPM build, and then we ran NPM pack", which is what basically simulates a publishing, and it gives you a tarball. And we compared it to what was on NPM, and we've found that it was identical. That's almost like a notion of a reproducible build. We could say "This package -- you can go get the GitHub code, and you can run those commands yourself, and you will be able to confirm that that's the code they put on NPM." That's a great thing to know about a package. Versus some other package that might require random system libraries to be installed, and who knows what versions those are, and now the code doesn't even necessarily match, and so you don't know that what you're installing and running is actually what you saw on GitHub.

So stuff like that, where probably like 99% of most packages will be able to pass that test. NPM install, NPM build, NPM pack - that produces the same thing. But some of them aren't going to pass that, and we should probably be a little bit more suspicious of those packages, and encourage them to --

**Nikola Lysenko:** Yeah. You should take a closer look.

**Across Aboukhadijeh:** Exactly, yeah.

**Nick Nisi:** Would they have to have their dependencies pinned in their package lock in order for that to reliably --

**Bret Comes:** Unless they're rendering it into their NPM package during build, they shouldn't.

**Across Aboukhadijeh:** Yeah, that's a good point. He's making the point that if their Webpack version is loose, or something, then maybe it produces a slightly different output. That is a challenge, and we haven't built this yet, but this is --

**Nikola Lysenko:** The other thing to is also - going back to what you said, we don't want to make more work for maintainers. The thing is, doing all that extra packing, minifying, deleting test crap - I mean, that's actually more work. We're trying to convince maintainers to not do that, because it seems like you're helping, but this might be a case where the cure is worse than the disease. Just stop making it so complicated. You can just publish the damn files right why? Because everyone's already running this thing through a build step anyway when they're consuming it. You're not optimizing anything that's worthwhile here. It's making it more fragile, basically, right?

**Nick Nisi:** Sure.

**Nikola Lysenko:** But people are going to do what they're going to do, and I'm sure people will argue with me about that philosophy.

**Across Aboukhadijeh:** But getting back to your original question - you asked how many packages have their tests published... The biggest number that you need to think about there is I think someone did -- I saw this stat a while ago, so it's out of date, but something like 60% of NPM packages don't even have tests, period. At all. So it's not like they remove them, they just never wrote them.

**Nick Nisi:** Shocked, I tell you...

**Across Aboukhadijeh:** \[31:57\] It's something you probably want to know about you choose a package...

**Bret Comes:** The other piece or tidbit I'd throw out there as well - back in the early days of Node there were a lot of DX design ideals around how Node modules should work, and one of the original ideas was you could actually just go into Node modules and get a nit dependency and make contributions out of your dependencies' folder. And we've obviously gone far away from that... NPM in some sense has turned into a much more simple tool, which is just shipping tarballs here to your local development or CI pipeline... But in some sense, it's like - maybe you want to know, "How is this maintainer treating this tarball?" Is it just like a sort of built binary packed that they send you, or is there actually a strong connection with the original source files?

**Nikola Lysenko:** Yeah.

**Bret Comes:** So it's not going to be like a serious penalty necessarily without it, it's just metrics that -- it's kind of like a shortcut to like... Like, the idea is you look at the Socket security report of a particular package, and rather than having to go research these little details, that we all know how to do... Developers and maintainers - we can just answer these questions a little quicker, without having to dig around the files tab and see what it's actually doing.

**Nick Nisi:** Yeah. And I can see that, removing tasks or doing optimizations like removing white space, things like that, being like holdouts from the original days of JavaScript. You're shipping to the browser, so you want to have as little things as possible... But it's also possible that it's just accidental, in the case of like -- I don't know, maybe my entire codebase is written in TypeScript, and then the build command is just looking at what files start from main, or whatever... And tests are never part of that, and so it just never gets built out, and there really is no connection.

**Across Aboukhadijeh:** That's why this stuff is going to be important to get right, and to be really sensitive to -- there's so many different workflows people have, and there are so many things you can use NPM for... You know, originally we had a bug where we would find packages that just had CSS in them, and we would classify them as empty packages, packages that don't do anything... But it's like, no, actually, CSS packages - it's like a thing people use NPM for. So, like, okay, you know... So we're discovering all these different things. Some people publish C code to NPM, and just use it -- you know, there's so many things people are using it for, so...

**Nick Nisi:** Oh, interesting.

**Bret Comes:** Exotic workflows...

**Across Aboukhadijeh:** Exotic workflows... Yeah.

**Bret Comes:** We have ESM in the browser now, so you can actually publish real ESM artifacts to NPM, and then pull them out of NPM with something like UNPEG, or (I think) Skyjack, or something... Directly into the browser. In that case, maybe you would minify it. Maybe the CDN should do it. These kinds of questions people are still exploring and deciding about, so...

**Nikola Lysenko:** I still think it's premature optimization. \[laughter\] Old-school.

**Bret Comes:** There was no browser workflow out of NPM when Node came out. It was always assumed that you would essentially download it to Node modules and then run it through a bundler first... So as things get stretched, and those assumptions start making less sense... Some context, so --

**Nick Nisi:** Yeah, one thing I'm curious about is - going back to those... What did you call them, the security scores?

**Across Aboukhadijeh:** The scores at the top of the page? Yeah, we should be calling them securities. They're quality scores, or security scores.

**Nick Nisi:** Quality scores, okay. This is interesting, me looking at React and being able to see that, but I'm thinking more in terms of like my day-to-day application development... Is there a way that I could get scores, similar to how I get Lighthouse scores for my app, and how I'm performing it, that I could get this as a total of --

**Nikola Lysenko:** Yeah, right now... \[laughs\]

**Bret Comes:** Almost done!

**Nick Nisi:** Awesome. Awesome.

**Bret Comes:** So right now the Socket security website - it's like a really great research tool when you're looking at individual packages, and sort of the next stepping stone we're working on is generating reports specifically tailored for a project.

**Nick Nisi:** Awesome.

**Bret Comes:** So rather than having to go through individual packages, it's like we can just show you everything that's in it, from like a high-level view. It makes that research task a little bit easier, and we can surface things that are interesting, rather that you're having to find them yourself.

**Nick Nisi:** \[36:02\] That's awesome.

**Christopher Miller:** Is your formula public?

**Bret Comes:** Is it public?

**Across Aboukhadijeh:** The formula meaning like how each issue affects the ultimate score?

**Christopher Miller:** I mean, how the security score is calculated, essentially.

**Nikola Lysenko:** It's basically like an average of a bunch of little statistics which are collected... And the thing is we're always adding more to it. So it's probably like -- I don't know, does Lighthouse publish their score? Or do people even care that it's public? It's just kind of like --

**Across Aboukhadijeh:** I think we should publish it. I think it's basically like -- there's a way it's attached to each particular issue or metric... So it's probably helpful to people to understand where the scores come from. It's something we'd like to publish, I think. We're a small team, and we're just trying to get something working right now; we just haven't written up as much documentation about this.

**Nikola Lysenko:** It's not stable enough that it's really worth writing it up... Because by the time you get done writing it up it's going to be like "Oh, we've got to change it again." So it's not really -- yeah, those aren't stable right now.

**Across Aboukhadijeh:** We've been saying the scores are in beta, because while the issues we detect are pretty reliable so far, I think the scores, how we weigh each thing - it feels like there's a little work to go.

**Nikola Lysenko:** It's more or less just like a weighted average; it takes some kind of geometric/harmonic mean thing of a bunch of different numbers... It's some simple statistical gadget.

**Across Aboukhadijeh:** It's very inspired by Lighthouse though.

**Nikola Lysenko:** Yeah, same idea.

**Across Aboukhadijeh:** Finding these issues and then just sort of like -- the more of the bad issues you have, the more the score goes down. It's intuitive.

**Nikola Lysenko:** Yeah. Basically, this thing is like "Okay, this thing is good if it goes bad, or this thing is bad if it goes worse", and then you just kind of feed each of them through some kind of distribution that reweights them, and then we take a weighted average of all those. Sometimes we also feed it through another thing that adjusts it for popularity... So it's just like - yeah, whatever. There's a bunch of random stuff. I don't know. It's a grab-bag of random little things. I'll write it up eventually.

**Bret Comes:** It's kind of like, every little thing that goes -- we try to capture every little thing that goes through your head as a developer when you're hand-assessing dependencies... And trying to codify those into a boolean value of that.

**Nikola Lysenko:** I think you're giving it too much credit for what it is. It's more just about right... In the future, it'll probably be some statistically normalized thing, where it just looks at a bunch of different metrics, we'll calculate the distribution for every package on NPM... It'll probably be like a quantile deal, something like that, for most of the scores. That's what'll probably happen. And then you can click on each issue, and you can see "Okay, I'm in the top 10% of packages here" or "This thing is like bottom percent", or whatever.

**Across Aboukhadijeh:** Was that too much information? \[laughter\]

**Nikola Lysenko:** We're working on product design...

**Bret Comes:** We have like a thousand tangents

**Nikola Lysenko:** Yeah... I don't know, you bring a few people -- we're doing product development right now, and this is what you're going to get. \[laughter\] Sorry we're putting you all to sleep.

**Nick Nisi:** No, I don't think you're putting us to sleep at all. It's just, you're very passionate about it, which is awesome to hear you working on it and just so excited about the product and the implications that it can have, which is really great.

**Christopher Miller:** I mean, honestly, I didn't care what the algorithm is. I just wanted to know if it was public.

**Nick Nisi:** So you could gamify it.

**Christopher Miller:** No, but just because it's good to have that sort of people, or else people will be like "Well, it's a black box", and then somebody's going to get pissed off about their score, and like "How do I improve my score...?"

**Nikola Lysenko:** If you're mad at your score, you can blame me. It's my fault that you score is bad. \[laughter\] So it's definitely me.

**Bret Comes:** It should be clear what is negatively impacting the score, and actions you can take to basically release another version that --

**Nikola Lysenko:** Correct. The reason your score is bad is that I hate you. \[laughter\] That's what you can take away from this conversation.

**Bret Comes:** No Mich.

**Across Aboukhadijeh:** This is why we don't let Mich do public interviews. \[laughs\]

**Nikola Lysenko:** There was like some "I don't know, should we let him on here?" And then I'm like, "I don't know, guys, do you think this is a good idea?" No, there's actually -- it's just there are bugs, basically, and we're still working on it. It will get better, I think. I will learn to love. \[laughter\]

**Nick Nisi:** \[40:04\] So I'm trying to think of how just like a JS/TypeScript developer working on a day-to-day app - how should I approach introducing something like this into the app, or to my team, something that they should care about?

**Across Aboukhadijeh:** Well, the easiest thing is to just install the GitHub app. It's kind of the primary thing. If you want to go a step above just doing manual research of individual packages on Socket, you can install this GitHub app, pick which repos you want it to be installed on, or just do all the repos in your org, and then it will watch pull requests for changes to the package.Jason file and the other associated files, and then leave a comment when it sees typo squats.

So far, typo squats is what the app does, and it's not a thing that happens super-often, but when it does, it is something that you would want to know about, because it does have quite a lot of potential consequences... And that app will kind of expand with more functionality over time. We're gonna probably introduce a socket.yaml file that you can add to your project or to a top-level repo, that would control the settings of Socket and what thing it alerts on, what it does, what actions it takes... But if you go ahead and add the current app today, it will evolve and expand into this more full-featured thing over the coming weeks.

But typo squatting is already -- it's a thing where if you add it today, probably you're not going to get an alert from it unless you make a mistake, in which case you'll probably be really happy that it sent you an alert... But the kind of stuff it catches is stuff like -- you know, there's a package called Browsers List that a lot of people use; I guess you guys have used it or heard of it... But there's a common typo people make with that, which is to install Browser List, singular, Browser List... And that package is a completely different thing. It used to do something else, and then now it was removed from NPM... And it was a security holding package for a while, which makes me think somebody was doing something nefarious with it.

Now if you install it, it just throws an exception instantly. So if someone's published something else there, it'll throw an exception and tell you that you've made a typo... But anyway, this is a package where -- there's no reason to add this package to your JSON file. There's no good that will come from this. And in fact, using Socket, we've found a tool - actually, Preach. Everyone knows Preach. The Preach project was depending upon Browser List, and Browsers List. They installed both of them. Probably because someone typed the first NPM install, and then typed it again correctly the second time, and forgot to remove the old package.

So that's the kind of thing that if you installed the Socket GitHub app, we can catch. We can tell you "What are you doing installing Browser List? That thing only gets 10,000 install every month. You probably wanted the other one, which gets 10 million installs every month." So that's what it can do today.

**Bret Comes:** The other thing you can do that's even less -- rather than having the app installed is just start using the Socket.dev website to research new packages, or packages that are hassling you and your project. You can find some weird stuff in there sometimes, like "Hey, look, this thing is writing to the file system, even though it's just like a date picker" or whatever.

You can use it as like a way to justify "We should fork and make this better", or "We should just get rid of this. This thing is doing weird stuff." Just a shortcut to doing research within the transient dependency tree of various packages. And then yeah, once we have project reports out too, that'll even automate that process a little bit further, but will require the app installed.

**Nick Nisi:** If I go look at a package on Socket.dev - I'm interested in installing this package, so I go and preemptively just do a quick check... Will it tell me about any transitive dependencies that might be like trying to do shell access, or anything like that?

**Bret Comes:** Yeah.

**Nick Nisi:** Very cool. Okay.

**Bret Comes:** There are two tabs in there. One's called Package Issues, the other is called Dependency Issues. The Package Issues are just like the issues related to the top-level package, and then Dependency issues sort of collects all issues it sees through the entire dependency chain.

**Nick Nisi:** Oh, cool.

**Nikola Lysenko:** We're going to be working on making this stuff more accurate and digestible, too. At the moment it's still kind of noisy, and things will -- some of them are not ideal, but I think it's actually informative, and you can still find surprising stuff, even in its current state. So it is getting better. There are a lot of things that are almost working right now, that we'll have out there pretty soon.

**Break:** \[44:18\]

**Christopher Miller:** So recently there was a supply chain attack, and a popular package - I think it was noetic - included another package, which is called peacenotwar. And peacenotwar - first it (I'm not sure) it started looking at your IP address and zeroing out your hard drive if you live in Russia, and then it pulled that out, and I think what it does now is it creates a file on your desktop... I don't know. But I'm curious, since this was a big deal, how did Socket approach that? What was the experience for a Socket user, if they had depended upon, say, noetic?

**Nikola Lysenko:** \[48:07\] Well, at this point we basically only have a GitHub app that detects typo squats, so it wouldn't do anything on peacenotwar. But once we have a fully functional application that you can install, it would file an alert that basically this thing gained access to a file system at the top level require. So it would have alerted on noetic for this particular thing if it was actually running. And then you'd get some message like "Hey, all of a sudden this module is accessing the file system when you require it, which is probably not what you wanted." So it would eventually do that.

At this current stage though, we're still trying to get the application up, and bring that up and running, so it wouldn't catch it right away... Unless you actually went to the website and looked at the package, then you would have seen it.

**Nick Nisi:** That's cool. Cool to hear that you have a plan to address those, because I guarantee that won't be the last one.

**Across Aboukhadijeh:** That's the one that's most important to address, really... You've been using a package for a year, and then suddenly a new version comes out and behaves completely differently than it did for the last year. And someone on your team is trying to update to that new version, maybe it's Dependabot doing it, or maybe it's someone just updating all the dependencies, or maybe somebody deleted the package lock and regenerated it... However, it's getting updated, you want to know when the dependency has had that drastic of a change in its behaviour. That's what we want to do, is come and leave a comment in that situation, on that PR, and say "Hey, you should know this project is now doing all this weird stuff, and here's a link to the line of code where it's doing that if you want to investigate further."

**Bret Comes:** Basically, a report of every new system call that's added, abruptly, essentially.

**Nikola Lysenko:** Yeah. And also where they're used, too. In the future, probably within the next month, we should have a more fine-grained analysis where it'll tell you not just like "Does it use the file system?" but where does it use the file system, and how does it use it. So we will eventually have this thing where it will tell you "Okay--" If you call a function with some arguments, and then it reads from the file system, it's a very different thing than if it's like you import the module and all of a sudden it uses the file system. Or if it has like an installation script that then does a bunch of stuff in the file system.

So it's not just like "Does it use the file system?" but "Where does it use it?" and "When did it start using it?" It's much more alarming if a package starts using the file system in a minor version or a patch version update, and it previously didn't, than if it was just using from the very beginning and people have been using this module for all time. So we'll have that stuff implemented soon, and we're going to have an app that can do it.

At the moment though, you have to just look at the website to check for yourself basically, to do that. But we're trying to get this thing built as quickly as we can, and we have all the pieces there, it's just not quite up yet.

**Across Aboukhadijeh:** We're going as fast as we can. If you want to help us build this, email us. We're hiring. You can join Socket and help build this, and then we'll go faster, and then we'll have more features to talk about the next time.

**Nikola Lysenko:** Yeah. It's like this thing -- we sort of announced it and then the demand for this thing was just much greater than we were expecting, and we're like, "Oh, we've got to go a lot quicker now", right? So we're kind of in that scramble to catch up really quick.

**Nick Nisi:** So when you're looking for things like that, like flags that might stick out, can you talk about how maybe that pipeline works a little bit, and -- I don't know how you might do this, but if I mistakenly set up a prepared script or something that runs shell commands, and then remove it out, am I forever tainted as like a vulnerable package on Socket? Or how do I clear my name on things like that?

**Nikola Lysenko:** Yeah, so each analysis is specific to each version, and each package. But it does keep track of which version introduced this line of code. So we have kind of like a NPM blame as an analogy. A blame that tells you where things actually got added and when they got added to a package.

**Nick Nisi:** Nice.

**Nikola Lysenko:** \[51:56\] So you can see "Okay, this version was compromised, but maybe subsequent versions are okay." And I think at the moment it's sort of just the facts type of stuff; it says "Oh, it was compromised at one point in the past", we might report that, but if the current version looks legit, it's okay. So yeah, that's basically what it is; it looks at each version in terms of when did things happen in that package, basically. If the current version doesn't have an installation script, then it won't see an installation script.

**Nick Nisi:** So as we've alluded to, NPM is quite popular, and there are a lot of packages out there... So how does Socket scale to analyze all of these packages and give you that in a timely manner?

**Nikola Lysenko:** So I can answer this a little bit... Basically, what we've got is a kind of in-house little Homebrew sort of function compute type of system, where all the packages are unpacked into a giant content addressable data store... A giant, immutable -- you can call it like a data lake, or a data swamp, or whatever...

**Across Aboukhadijeh:** \[laughs\] A data swamp... Is that a term of art, a data swamp? I think you've just made that up.

**Nikola Lysenko:** I think that's a thing people say... But basically, we just take pretty much the entire dataset of NPM, and then we just break it down. So we have like the tarballs, and then we have like the files in the tarballs, and then all the package.Jason things, we break them into this giant, immutable data structure, that we can then query by just walking hash pointers basically to search through that.

And then we have functions which can read data from this giant data swamp thing, and then generate new little blobs that go into this giant immutable data store. So we can sort of do searches on this thing by walking pointers. It's basically like a tree, or like a directed acyclic graph of pointers to blobs of data. And all the analysis, like running a linter, doing points to analysis, parsing a file, whatever - each of these things is just reading a tarball, sort of like walking through the contents of the tarball to read it out. It all happens in memory, and it's streamed in over the network, and they're all just functions. So if one of them crashes, you can just rerun it... And they're all also generated on demand. So it's like if you go to a page, it can just say "Oh, I need this data, which is this function of this hash", and then it can just walk down all those hashes and get all the data back, and then return you a result. And if we've already calculated it, because they're just functions, we can memorize them to optimize the execution; so we just cache the results of that.

So the parallelism happens at the level of functions, and we can also memorize them at the level of functions. You can even have things where it's like you have these very big, deep, complex function trees, but you can start calculating it, and if it crashes halfway through, then the stuff that's already been done, you can keep it, and then it can just restart from that next time. Basically, a user goes to a page, it starts crunching numbers, and then they navigate away - then we can just cancel that whole task, and the next time someone comes back in, it'll start calculating the rest, and then results just stream back in as you're clicking through stuff and walking around. That's it - we've just got functions, and we've got data, and they're just pure, immutable functions. That's all that there is.

**Christopher Miller:** But all this is computed lazily, right?

**Nikola Lysenko:** Of course, it's on-demand.

**Christopher Miller:** And do you have anything that polls, or sits on a feed and waits for new published packages then?

**Nikola Lysenko:** Yeah, so the way that works is we basically tail the NPM package feed, and then you have sort of like a root point, which is like the state of all packages on NPM. Then new packages come in, you build a new block, and you throw it back in there, update a pointer, and it redoes everything basically. 

**Across Aboukhadijeh:** The following NPM part is really important to be able to detect when new stuff gets published that's sketchy... I don't know if we're currently -- are we currently running analysis on the feed?

**Nikola Lysenko:** \[55:49\]'Yeah, we currently don't have a thing in real-time. I very briefly turned on a Slack integration, and then it just spammed the thing, and we were like "Okay, we need a better way to manage inspecting this." So at the moment we're sort of reading it in real-time as it comes in, but we're not actually looking at it as it comes in real time, if that makes some sense.

**Across Aboukhadijeh:** We want to get to a place where basically as a package is published, we just do the full analysis on it, and then if we find that publish was particularly suspicious, we can take an action. For example, when we notice that a package suddenly has all these changes made to it, and it's maybe a new maintainer, maybe it's something about it, the collective publish just looks like something's wrong, then we can take an action. So it might start off by being just like we put it on a page that's like Suspicious Publishes, or we throw it on a Twitter feed, or we send it to a Slack channel that we look at... But we wanna eventually take some actions based on that, such as like having a security expert actually look at it and say "Oh hey, this is actually a terrible publish. Let's go get NPM to take it down right now." We'll tell them about it, we'll report it to NPM, and we'll block it for anyone that has the GitHub app installed, so that they won't accidentally install this malware, even if NPM still hasn't taken it down yet... Because sometimes they take a few days to get back to you.

**Nikola Lysenko:** Yeah. But at the moment, all of our analyses are generated on demand. So if the thing is a new package in the feed, we don't aggressively alert NPM yet, because we just don't have people to look at and review all those things at this point. But if you happen to be running our current -- we have like a temporary version of the GitHub app, but when this is actually live, it will run the analysis on your packages as you do a commit. So if you're using Socket, then you have a bad package in your package.Jason file, you will definitely get the alert in a timely fashion. But you probably don't care about all the new stuff coming into the NPM feed, because you're not using those packages.

So from the user perspective, or in terms of any question you can ask, the data will be there when you ask that question. It's just like, "Do we want to start aggressively looking at the new stuff as it's coming in, and having people reviewing it?" We will do that, it's just - when we have enough people, basically, to do that. We've only been doing this for a couple of months now, so we just don't have the people yet.

**Christopher Miller:** It would be cool to eventually see some sort of hook for like a dev environment, maybe a pre-commit hook, or something, that does the analysis before you -- I don't know, maybe it's a pre-push.

**Nikola Lysenko:** Yeah, that's exactly what we're going to have. So you will have that.

**Bret Comes:** We also talked about maybe doing a NPM proxy, or like a CLI replacement that also does a little check before you install stuff... Because it's out there, you don't -- even if we catch it at the PR layer, you're still doing it on your dev machine, which has SSH keys and whatever else on it, so...

**Nikola Lysenko:** Yeah.

**Across Aboukhadijeh:** There's lots to build.

**Bret Comes:** These are ideas; those aren't there yet, but... We're trying to basically attack things that are going to provide the biggest amount of value first, and then we'll just --

**Nikola Lysenko:** Right. The other reason we do this stuff lazily too is that as I said multiple times - and apologized for, and I know I'm joking a little bit - we are working on this thing, and we're adding new stuff every day, multiple times a day, so we're constantly adding new things and we're improving stuff. And when we do that, we can't just stop the world and re-analyze NPM.

So the other big advantage of doing everything lazily is that we can ship code so much faster. We can just push a new analysis, and then -- you know, like, okay, the next time you check it is'll update. Whenever you look at it, it's always going to be the most recent thing. So that's why we do it that way.

**Nick Nisi:** Yeah. That's awesome, that you have that infrastructure in place to lazily re-analyze things as you need it, and as you're adding new features... I was going to end the show by asking "What's next? What's something cool?", but we have spent the entire show talking about all of these amazing things that are coming, that I'm so excited for... It really does seem like this could become a super-invaluable piece of your development workflow for everyone. For package maintainers, down to people just working on everyday apps for companies... It could be so important to just use this a like a starting point for everything. Every time you add a new package, check Socket first. Did I check Socket? Did the Socket come back and tell me anything? It's just really cool. Really awesome.

**Nikola Lysenko:** Yeah. And even though things are not perfect yet, I still think that what we have now is actually pretty dang useful. Because it's often a starting point for asking a question. And you can click those issues, and the key thing is we do have the actual data there. I think our presentation of the data inside NPM packages is currently the best you can find anywhere on the net. So if you want to look around at what's going on inside a package, you get the issues, but they're kind of more just like a hint of something to take a look at... But then you can take a look at it, and you can navigate through the files, you can click links, and you can see the actual code that's in that package and all of its dependencies, all linked together.

So right now, that works, and it's pretty great. I think it's just a fun website to click around and play with, and we're soon going to have an app that's going to make this a hundred times more useful.

**Across Aboukhadijeh:** By the way, the thing with mixed referencing is really cool. You can actually -- when you're going into a package and looking at its files, you can click... It's sort of like what VS Code can let you do, but it works across NPM packages. So you can click on like a package name, and it'll jump you to the files in that package, it'll take you to the main file... But it'll do it for the right version, too. It'll take you to the specific version.

**Nick Nisi:** Oh, cool.

**Across Aboukhadijeh:** So you can actually follow the tree of packages all on the website. It's really neat.

**Nick Nisi:** Nice.

**Nikola Lysenko:** Yeah. And if you try to do this -- like, there's nothing that really supports that kind of workflow besides Socket right now, which I think is kind of cool... I mean, I personally find it very useful to just click around in the files on packages, right?

**Across Aboukhadijeh:** And thanks for all the kinds words, Nick, and the excitement. We're going to try to make it as good as we can, and make it something that's really useful to people, and make it live up to all of your hopes and dreams, hopefully.

**Nick Nisi:** Absolutely. I think you're off to a great start, and there's a lot here, and a lot of potential coming, so I'm very excited to keep going, keep looking at it and to make it a regular part of my flow, for sure.

So yeah, thank you so much for joining us. I do want to mention - and we've kind of alluded to it throughout the show, but Across was on the Changelog podcast talking about Socket in more depth, and different angles, so we'll definitely have a link to that show in the show notes as well.

Thank you so much, Across, Mich and Bret for coming on, and thank you, Chris, for being here as well. We will see you next time!

**Nikola Lysenko:** Bye!

**Bret Comes:** Thanks for having us!

**Christopher Miller:** Bye-bye!

**Outro:** \[01:02:24.18\]

**Horse JS:** If you are writing your first NPM package, I highly recommend keeping it.
