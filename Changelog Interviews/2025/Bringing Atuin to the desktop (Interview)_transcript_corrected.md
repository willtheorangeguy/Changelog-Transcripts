**Jerold Santo:** Well, I am joined once again by Ellie Huntable with Again, which has been making my shell magical for years now... Ellie, welcome back to The Changelog.

**Ellie Huntable:** Hi, great to be here.

**Jerold Santo:** Great to have you. You sound closer. You were so far away last time... I think we had a schedule around our different time zones... But now you're in the States. What happened? What changed?

**Ellie Huntable:** I moved to San Francisco. That's been very recent, just like a month ago, but it's been good so far.

**Jerold Santo:** Good so far. And where were you before? Somewhere in the UK, right?

**Ellie Huntable:** I was in London.

**Jerold Santo:** In London. Okay. And you were often on a motorcycle, I remember that part...

**Ellie Huntable:** All the time, yeah. Still am. I bought one like four days after moving here, so...

**Jerold Santo:** Okay... Did you upgrade? Did you downgrade? Did you side grade?

**Ellie Huntable:** Side grade. I have a 1290 Super-Duke now. The roads here are more fun, and the weather's more amenable to motorcycling, so it's a good change.

**Jerold Santo:** Okay. And there in SF, it's got to be -- you're in the San Francisco area, is that what you said?

**Ellie Huntable:** Yeah, yeah.

**Jerold Santo:** Lots of hills.

**Ellie Huntable:** Yeah. They're fun, too.

**Jerold Santo:** Fun a.k.a. dangerous, depending on your appetite for destruction, I guess...

**Ellie Huntable:** Pretty much.

**Jerold Santo:** So Again - such a cool tool. Very few times do I cover a tool in Changelog News and then install it and then use it, and it integrates itself into my life... And it's been years now. So I just use it happily, Control+R for the win. I love it. I don't use probably any of the fancy stuff that you've added since then, but that was like your deal originally, was Again the CLI, which is like synchronized and prettified and just better, in my opinion, shell history. And the sync was really a big part of what you were building, which is the part that I don't care about. I'm a one-computer person.

**Ellie Huntable:** You can use it to back up as well. It's pretty good for that.

**Jerold Santo:** Yeah, that's true. And you had some cool stuff with how you're handling sync, and how you do that without violating privacy, and there were all kinds of talk about that... And then you continue to work on it, and now you're working on something that's very related and very cool and different, which is Again Desktop. Can you take us on the journey from when we last spoke - which was about 18 months ago - on the show about Again, the CLI, and where you went from there, what you built?

**Ellie Huntable:** Yeah, sure. So the CLI records every shell command you run, is kind of the whole point. It makes it really easy to recall them. But what is trickier with that is sort of recording whole workflows. So if you're looking for an individual command, it's great. It's really easy. But if I was looking for "How do I set up a new staging environment? How do I onboard a new developer? How do I do something that's a long sequence of steps, and maybe needs annotations and various other things?", the CLI helped, but didn't solve the problem. We had a bunch of discussion over years, to be honest. I've had this idea for a really long time, of like "How can we solve this essentially documentation problem?" And Again Desktop is the answer there, at least in my opinion.

\[07:50\] So what it is it's essentially a run book editor. What I mean by that is we started off by just building something that was good for recording notes and documentation. You can just write English words down, and share them with people... But where it gets really powerful is the executable blocks we added. So we have things like terminal blocks, which are - if you imagine Notion with its database blocks, instead of a database, we have an embedded terminal that you can actually execute a command. And this sort of takes it from a confluence page that goes stale, to something that you can actually run and read in the same place.

A lot of people have asked how this is relevant to the CLI, and I can kind of see that it might not be immediately obvious. However, where it does become quite powerful with the CLI is all the data you've been recording in your case over years in the CLI, is accessible in the Desktop app, too. So you can screw around on your machine, figure something out locally in your terminal, and then when you go to document it later on, you can write down what you did, and you can pull in your shell history into the executable blocks.

**Jerold Santo:** Yeah, that's really cool. So if I recall correctly, you had full-time jobs at one point, which was at -- I remember PostHog. What was it, before? Was it Coinbase?

**Ellie Huntable:** Coinbase before that.

**Jerold Santo:** Okay, so a couple of serious jobs. And then you had quit your jobs in order to do this, open source, try to make it sustainable, living the dream, so to speak... And there was a question on "Well, where do you take it from here?" And desktop seems like a good place to take it, because you're not just syncing for people; you're providing collaboration, you're writing tooling around docs... And these are the people who are, generally speaking running infra at corporations, right? So is your end user, basically -- like, is DevOps still the term? I don't know, a platform engineer? I'm not sure what they're calling themselves today.

**Ellie Huntable:** Maybe a separate conversation, but I think DevOps kind of like failed.

**Jerold Santo:** DevOps is over? Okay...

**Ellie Huntable:** \[laughs\] But no, it's sort of platform, SRE, DevOps... Whatever you want to call it. People that do Shying and Kubernetes and stuff for their jobs.

**Jerold Santo:** We used to be called sysadmins back in the day. I feel like we abandoned that because we wanted to get a raise, you know... But at the end of the day - I mean, you're administering systems, so I like the term sysadmin. I always have. I probably always will. How does it work? I mean, how does -- do you pronounce it Again?

**Ellie Huntable:** Again, yeah.

**Jerold Santo:** Again. Kind of like Tattooing.

**Ellie Huntable:** Pretty close, actually. Maybe we should change the logo to have like a turtle and a desert planet. That would be pretty cool.

**Jerold Santo:** That would be cool. The turtle is cute though, so that always gets me going... But Again Desktop - how does it work?

**Ellie Huntable:** Oof... It has a lot going on. \[laughs\]

**Jerold Santo:** It was an easy question for me to ask. It sounds like it would be a hard one for you to answer.

**Ellie Huntable:** Yeah. So, I mean, at a very high level, it's a desktop app. It's not an Electron app, it's a Kauri app - I'm not sure if I'm saying that correctly - which is a web view, but it's your system web view, instead of a copy of Chrome. And the backend's all written in Rust, which I'm very happy with, instead of Node.js. We'll talk about that more if you want later. But we essentially launch a web app locally in Kauri, and it contains an editor called Block note, which is a really cool open source project built on top of Tiptop and Prose Mirror, that provides like a block style editor... And we extended that with all of our custom blocks.

So to start off with, you're just editing -- you have a choice between a local file, which is currently essentially JSON. We're working on that. YAML, sorry. But again, we're working on that. Or you can use our hub, which you sign up for, you can create an organization or a single player, and it provides sort automatic syncing, offline-first editing, and the idea of that being like collaborative style features. You could have like multi-cursors with people all zooming around, which we can see being really useful for incidents, or helping someone figure something out... As much of it as possible is implemented in Rust.

So right now we can't -- again, we released this as beta. There's still a lot of like "Right now it doesn't, but it will" going on. But a lot of the execution is written in Rust, and the idea there is we can bring it to be a runtime which is embedded in a desktop app, that runs in a CLI, all over the place, for executing run books.

\[12:03\] My kind of long-term vision there, I guess, is that current automation is kind of an all or nothing approach. You start off with "Someone might maybe have documented something", and that's that alone is a stretch. Or you kind of have to write a million lines of YAML and have it 100% automated. And we find that there's very little in the middle; there's no happy medium. And a lot of the time, things just end up documented or not even written down because the automation is just such a high barrier of entry.

The idea of the desktop app is to kind of make it easier to meet people where they might be comfortable, and that might just be writing down what you need to do, but it might be automating the whole thing with our blocks, and then running it with our runtime. So it's designed to be flexible enough to handle most sort of abilities.

**Jerold Santo:** Mm-hm. So there's probably a group of our listeners who, when you say "Run books that run", which is one of the catchphrases for Again Desktop - they live in run books, they write run books, they copy and paste stuff all the time, they use their shell history all the time... And then there are other ones, more like myself, who -- I mean, okay, I used to be a system administrator, but most of the stuff that I had to deploy or manage at this point is like ./setup.sh, or deploy.sh, and I can just have a little script, and it's good enough. And so that's at least my perspective. And there's probably a continuum of those folks.

For those who don't understand run books all that well, besides like "It's a script of some kind", or "It's a list of things that I must do", can you expand more on what kind of stuff a run book can do, and how they're usually used?

**Ellie Huntable:** Yeah. We've found a bunch of use cases. It could start off just being super-simple, almost like what you might write a README for, in our system anyway. So go install these dependencies, run this migration command, run this command to generate some fixtures etc, etc. So it can be very sequential, "run this, do this, do that". But we also find that people use them a lot for like database operations... So maybe you need to run a bunch of SQL to set up a new schema, or migrate from one system to another... And we've made it flexible enough to make that easier, too. So our dropdowns you can power with the output of a shell command to select an environment you might want to run in, or a URI that you might want to use in a query. There are a lot of database use cases, too... But also, we use them a lot for our local development. So there's a collection of maybe values in a local database you need to tweak, or files that need generating... You can use them a lot.

So you might have a home lab somewhere that has a bunch of setup required, and things can run over SSH, too... So it can show you -- yeah, you can use it for setting up a remote system, too. So maybe you need to set up your ZFS, and then you need to install K3S, or Docker Compose, or however you're running things, and it can help you with that, too.

**Jerold Santo:** So one of the challenges I think with this, especially in the diverse world of computers that we live nowadays, is different stuff on different people's computers. So this helps with sync -- I mean, if I'm using this as a team collaboratively, like through your hub... I'm not sure if there's a separate thing I can self-host or whatever; we can talk about that. But I'm syncing the run books across a team, and we're collaborating on those things, and that's all well and good... But oftentimes our environments are like drastically different. And so we've tried to throw a containerization at that, tried to help fix that... Is there any sort of concept or help in regard to that inside of Again?

**Ellie Huntable:** We don't currently, but it's something I'm really actively thinking about. We find a lot of people right now just have like a dependency step that does its best to set up the dependencies that you might need... But obviously, like you say, someone else might have a completely different local system than you.

\[16:07\] The only approach I can think of so far is having a container integration. So we have the concept of contextual blocks, which you would use for specifying that something needs to run over SSH... I'm currently thinking of doing something similar for containers, where I can say "This should run in my local development container", and it will sort of transparently make that work. I'm not a huge fan of it as an answer. Furthermore, I find containers for local dev to be clunky, especially on Mac, when you're running on a VM.

**Jerold Santo:** Amen.

**Ellie Huntable:** But I'm also not sure if there's actually anything better, so...

**Jerold Santo:** Right. It turns out maybe Linux is the answer in that case. I mean, I've been on a Mac for a very long time, and I've had this exact complaint for a very long time, and it doesn't seem to be getting resolved at any point... And so everyone else is like "Well, we just use Linux for dev." It's like "Well, that seems like an answer."

**Ellie Huntable:** Especially recently, I've been more and more tempted.

**Jerold Santo:** Yeah. As has a lot of people. I think the lustre and the excitement around Apple's products and ecosystem has just kind of like tarnished a little bit. I used to be very excited -- and maybe it's just like "Well, they haven't really changed much." Even the iPhone events, and stuff like that... I used to plan my Monday around the keynote, and "Let's watch it on the big screen" and "I can't wait to see it." And we'd even have shows... We used to comment, and we still do at times... But just like react to the Apple announcements. And honestly, especially the last one, I didn't even watch it. I was just like -- I don't know.

**Ellie Huntable:** Yeah, I didn't even know what changed for a few days.

**Jerold Santo:** It's like "It's another new phone. Maybe I'll get it because it's been three years, but my current phone still works." Although they just released some MacBook pros, and so maybe I'll go look at those and change my mind, but... Yeah, it's definitely -- maybe that just shows age, and exposure. Maybe not just age, but exposure over time, for all of us, to these things. It's been like decades of kind of the same thing, just iteratively better... Anyway, a bit off-topic. I definitely think that Linux is gaining mind share once again. Maybe not once again, but in a new group of people that it previously didn't have mind share in. And fast containers for dev is one reason why that might be nice.

**Ellie Huntable:** Yeah. I actually found the new Asa hi - however you say it, the Linux on macOS - I have another Mac that's running that, and it's incredibly good.

**Jerold Santo:** Is it?

**Ellie Huntable:** A lot of my experience was like running Arch on a MacBook in 2015, and that was dramatic. Whereas you install this, and it just works, which was really cool. I recommend it.

**Jerold Santo:** Yeah, that is super-cool. That is super-cool. We tried to do a show on the Asa hi Linux, and those folks are hard to get a hold of. They don't like to come on podcasts. If you know anybody, and you can put in a word... Because it is a fascinating technology. But they're a shy bunch, that's for sure. What have been some of the challenges with this? I mean, you've been working on it for a couple of years... What have been the hard parts?

**Ellie Huntable:** With the CLI, the hard parts realistically have been the sheer amount of data people have. So if we ever want to change anything with database schemas, it's a migration which professionally, when we run a huge database migration, it's like "Let's really pay attention to what's going on here." Whereas when we release something, there's like hundreds of thousands of database migrations going on, and if one of them goes wrong, that's someone who's lost data, and we have to figure out how to recover that... So it's very -- like, mistakes I might've made a few years ago are sticking around.

**Jerold Santo:** Right.

**Ellie Huntable:** With the desktop app, it's a different set of challenges, I think. It's very -- the CLI is quite simple. The command line environment is -- it is very varied, but it's still a terminal. You still have command control sequences and various other things... With the graphical app, it's a bit different. People running it on macOS, it's reasonably a consistent experience. But people on Linux, who I really want to support as best we can, the graphical environments differ hugely. So making sure things run consistently for different people has been kind of hard... We kind of -- we joke; there's two of us working on it... We joke that we're sort of building a terminal and a text editor at the same time, and neither of those things are known as particularly easy things to build... \[laughs\]

**Jerold Santo:** \[20:25\] Well, they're kind of dramatically different, too. I mean, the desktop, besides like you said, kind of the spiritual ties and the fact that you can pull in some of that shell history into the desktop... I mean, they're kind of like wildly different products, aren't they?

**Ellie Huntable:** I think so. I think they solve very similar problems. They're all about knowing what to do next and not forgetting what you've already done. And I think when you're looking at a shell prompt that does not have any shell history and then does not have any good documentation, it's very much like what you can remember, what you can figure out and what you can google; or I guess these days ask an LLM. But we're trying to solve the problem of making the shell really easy to use, making repeatable workflows quick and easy... And when you look at it that way around, they are kind of the same thing. It's just trying to solve like an ecosystem of problems, rather than just one.

**Jerold Santo:** Mm-hm. And so why did you go to the desktop? You could have just taken the shell, and maybe done a TUI, or expand it... I mean, it kind of is a TUI already, right? But expanded it and put this kind of functionality in, where it already existed. Why'd you decide to start fresh with a graphical interface?

**Ellie Huntable:** Yeah. So the end goal is to have both a TUI, a CLI, and a desktop app. But I think the desktop app is the most, like, revolutionary change. I'm kind of putting myself on a pedestal, I guess... \[laughter\] But there's a lot we can do in the graphical app that you either can't do with a TUI, or it feels clunky. The editing experience we can give people in a desktop app is a lot better than we could provide in a TUI.

We have another example, we have Prometheus blocks. So imagine you have a run book that is how to react to an incident, and you can have a chart in your documentation that's real time, with a terminal underneath it, that lets you change stuff, and you can see what you're doing and what reaction that has at the same time. And doing that in a TUI - I'm sure we could probably render a chart somehow, but it wouldn't have the same impact, and it wouldn't be as explorable. And a lot of what we're trying to do is make it exploratory, and make it something where things aren't quite as strict, they don't necessarily have to run in order... And again, fitting that into a TUI is not as straightforward.

An early prototype was actually a web app... So if you think like a Jupyter notebook style experience, where you run a server, and then you open it locally... And I didn't really like how that felt. I think we couldn't integrate with the system quite as well, even with the web app angle... And the desktop feels a lot nicer. We're not necessarily shutting off any of these things as future sort of expansions, but the desktop's, I think, where it starts. I like to think of it more as you're putting a terminal into some docs, and not putting some docs into a terminal.

**Break**: \[23:08\]

**Jerold Santo:** How has it been working with Kauri as a platform? We've done a couple of shows on it. We have a few production apps out there... There are. They are out there. It's not trying to belittle it. But hasn't been a huge upsell. I mean, Electron still is the 800-pound gorilla in the room.

**Ellie Huntable:** Generally very good. There are some issues that the team are aware of and are working on... So firstly, the development experience has been really nice. Being able to write Rust has been perfect for us, especially we're doing a lot of systems stuff. Being able to include all the libraries we've already written has been awesome... It's a lot lighter as well. So when someone downloads like a 20-meg package, it's a lot nicer than asking them to go download like five, six, seven hundred, or whatever Electron apps that are now. The resource usage is lighter... I don't know if it's necessarily as light as people might say, because you are still running a web browser, it's just not another instance of Chrome.

**Jerold Santo:** Right. As you proliferate Taurus, you're not going to have multiple Chromiums in the background.

**Ellie Huntable:** Exactly.

**Jerold Santo:** But if you're just going to run one, you're still going to run a full Chromium, right?

**Ellie Huntable:** Exactly. Yeah.

**Jerold Santo:** Gotcha.

**Ellie Huntable:** macOS has been nice because every user is -- you know, they're using the same web view that's consistent; it's what we develop on, so it's fine. Linux has been -- honestly, I thought it would be worse. So it's a lot better than I expected. Kauri on Linux currently uses an old WebKit version, which has some performance problems... I think the performance is when there are many DOM elements. There are several very long GitHub issue threads, if anyone's interested, but... It's luckily for us been mostly okay on most systems, but it's not quite as performant as it could be on macOS. The team are looking to use Chromium embedded framework on Linux, which would solve the performance problems, but I'm not sure if that's just doing Electron again. But what has been good for us is, again, the Rust on the backend means that anything that needs to be fast, we can make sure it's really fast, rather than it's all JavaScript.

**Jerold Santo:** So another opportunity you had with this project - it was a fresh start codebase-wise - was Again CLI. I would say the reception to it that I see, and that I have, was like universally positive. It's just like "This just makes my life better." Open source... But the question is "Can we make money off of it? Who knows?" And now you come out with a desktop app, and it's like an opportunity to make some money, but also open source... You're following that same pattern. So your thoughts on that?

**Ellie Huntable:** Yeah, so the CLI was -- I mean, I could definitely charge people for hosting. I've had a number of people say "Oh, let me pay you single-digit dollars a month for shell history hosting." And that was nice. However, the way I looked at it was I don't want to work on shell history by myself forever. So it needs to have the potential to do more, and it also has to have the potential for it to be more than just me. And we have something like 26,000, 27,000 maybe people syncing their shell history... And I worked out that realistically, a hundred percent of them are not going to sign up to pay. It's going to be quite a low amount. And we can't charge very much for it, so it's quite a niche, realistically.

\[27:56\] It also really doesn't cost very much in terms of infrastructure to run. I self-host the Postgres on a Hetzner machine. It's cheap, it's really performant, and other than my time, it's not a big sync. Desktop, I think has a lot more potential in terms of like business project. There's a very direct organization use case, potentially even stronger than the single player use case, really... And there's a lot more scope to do fascinating and flexible things with it.

It is open source, it's Apache 2... What is not, yet open source is the hub for syncing. So we have two types of workspace. You can have an offline workspace, that gives you local files on your disk. You can put them in Git... Whatever you want, basically. But the hub is the synchronizing real time backend, and it's not open source right now. Basically, we haven't figured out what to do with it yet, and I would very much rather have something closed source, and then six months from now decide to open source it, than open source something, realize I've backed myself into a corner, and then have to do a horrible license change, and it's a nightmare.

**Jerold Santo:** Right. What we say around these parts is "Rug pull, not cool."

**Ellie Huntable:** Exactly.

**Jerold Santo:** So definitely keep your cards close to your chest, and then if you want to flip one over and show that you've got the ace of spades later, fine. Go ahead and do that.

**Ellie Huntable:** Yeah. And I feel very strongly that if you're running it on your machine, it should be open source. If it's a desktop app, you should be able to see what's going on, you should be able to change it...

**Jerold Santo:** Yeah, I think that's a good distinction. That's a good place to draw a line in the sand, I think. And I think you're right, because when it comes to run books, I just feel like anybody who's playing single player don't care that much about something like this, because they've got their scripts... They might have a Notion or Obsidian, and they just have their docs in there if they write down -- or it's all living in their head. Usually, when you need a run book, it's like "Hey, I put together how we do this. Now we can all run it when I'm on vacation", or whatever happens when it's your turn to be working and not my turn.

**Ellie Huntable:** Exactly.

**Jerold Santo:** And so it's almost de facto team, right? Like, it's going to be collaborative... Obviously, there are the outliers who will be using it because they just like your software or whatever, or it's a prettier way to manage their own docs and scripts... But for the most part, I do think it's going to be something that organizations will adopt. Whereas the CLI is just like hackers and nerds... Sure, they work in an organization, but it's going to be harder for them to get their org to sponsor or buy the thing.

**Ellie Huntable:** Exactly. And the only real way I could see the CLI applying to an org is like "Share your shell history with your team", which I don't think anyone's ever going to want to do, because it's weird.

**Jerold Santo:** Yeah, it is kind of weird. It's like, at first you're like "That'd be great." And then you realize all the things you type in, and you're like "No."

**Ellie Huntable:** I don't know, it's like my team seeing my browser history. There's not anything weird there, I just don't want to.

**Jerold Santo:** Yeah. It just doesn't -- it's just useless, and maybe embarrassing at times, you know? You're like "Sometimes I type things that is wrong", you know? Or "I feel like a command is going to work, and it doesn't." And it's like "There it is. That's my shell history."

**Ellie Huntable:** Absolutely. We have had a lot of people ask about self-hosting it, which is something I really want to support, but there's also the other angle of supporting it, and I've found with the CLI that it's self-hostable, and has been for forever, and it's tricky to support people. Generally, the Docker Compose we provide works, but a lot of the time people want to run it differently, they want to do their own thing with it, and supporting that is super-hard... So we're now kind of at the point where unless you're using our Docker Compose, and it doesn't work, I probably can't help you. Mostly from just a time and energy perspective. With the desktop app, I wouldn't really want to be in the same place, and it is a lot more complicated to run for the backend.

**Jerold Santo:** Sure.

**Ellie Huntable:** So if we do open source it, and I would like to, it would definitely be like "You can run it... It's on you."

**Jerold Santo:** Yeah. Yeah, that makes a lot of sense... Versus like a GitHub enterprise thing, where you're going to go install it on their premises and operate it for them. Yeah, that makes sense. Going back to the CLI and potential monetization - people are desiring to give you money, and that's because they love the work that you do... And I've seen that online, the response to it is almost universally positive. It's very good software, people love it, they seem to love you, and they just want to give you money. Did you try even just turning that lever on? Like, even though it might not be your end goal, or something that you want to work on --

**Ellie Huntable:** \[32:23\] So we had GitHub Sponsors for a long time, and --

**Jerold Santo:** Well, what about the hosted sync? Like "Let me give you two bucks a month to do this."

**Ellie Huntable:** I think that changes what it is. Maybe someday I will, but I think realistically, it doesn't cost me very much to run, and I'm quite happy providing it as just a thing people can use.

**Jerold Santo:** Okay.

**Ellie Huntable:** The two bucks a month - I mean, I guess... But then it becomes a -- like, supporting people, because there's suddenly... Like, they're paying, they're actual customers, and it's a strong expectation there. But we haven't had any downtime in like a year, so probably we'd probably be fine, but...

**Jerold Santo:** Probably. It sounds like you designed it pretty well, and it's relatively efficient.

**Ellie Huntable:** I'm happy with it.

**Jerold Santo:** You're not having to constantly be working on it, and maybe upgrading, whether it's vertical, or scaling the other way... So that's nice. Remember when Radiohead came out with their In Rainbows album, and it's like "Pay what you want"? And I don't think free was an option on that one, but basically -- I mean, you could do something like that, where it's between zero and N dollars, where N is whatever you want to give me, but zero is what it costs... I think you have a not insignificant amount, which could also be called a significant amount of money... You know, maybe put some petroleum in your motorcycle, or something like that.

**Ellie Huntable:** It's true. It's quite expensive these days.

**Jerold Santo:** It is. And it's not getting cheaper.

**Ellie Huntable:** Yeah. I think honestly, for me, I want to explore what we can do with the desktop app, and then maybe the future of the CLI might change... But where it is now, I'm super-happy with how it's going. I'm super-happy to let people just have it and use it. Realistically, my thoughts on monetizing open source software are more around like "Individuals just use it for free. Go have fun", and then it's the companies that should be paying. They get a lot out of open source, so...

**Jerold Santo:** Right. So how has the reception then been to the desktop release? Because it's in beta, it's out there, it's open source... And it hasn't been very long, maybe a month or so that it's been out.

**Ellie Huntable:** Yeah. It's been perfect. We have emphasis on opt-in telemetry.

**Jerold Santo:** Nice.

**Ellie Huntable:** I split that up. It's actually opt-out, but you can't opt out on the launcher.

**Jerold Santo:** Okay. So it's opt-out, but you just click a button right there.

**Ellie Huntable:** Yeah. It's right in your face when you start it up, so it's easy. And it's pretty much - we gained about a thousand signups on the hub, which was really cool to see. We've got people making hundreds and hundreds of run books, which is also really cool to see... I think the biggest thing for me though, rather than that telemetry, is more the community response. So in our Discord we have a separate channel for the desktop app, and people have been in there really active using it.

GitHub issues usually imply there's an issue, but it also implies that people care enough to actually tell you that something's not working for their use case, or something's going wrong, and provide like a bunch of steps... We've had people provide some actually really thoughtful GitHub issues as well, which has been nice to see and nice to work on. I think for me, it's also good validation... So again, I've been working on this for around a year, in one form or another, and we did release in a closed beta back in April, and that had a nice reception... But it's the validation of "You can go download it right now. It's on the website, go try it and let us know what you think", and that going successfully as well, which is really nice validation that the problem that I see as a problem and that I have built a solution to is a problem that other people see, too.

**Jerold Santo:** \[35:54\] Yeah. Well, I did download it, and I'm staring at it currently... It looks very nice. I like that there are some examples, because I'm a guy with zero run books, and... I can put my deployment script into here and write about it, but just trying to kick the tires. You have the Again desktop release... This is actually how you guys release a new version of it?

**Ellie Huntable:** Yup. We run that all the time.

**Jerold Santo:** You run that one all the time... Which is maybe like seven or eight steps... Updated 23 hours ago, so you're still currently working on it. That's always awesome. And then there's also one --

**Ellie Huntable:** Yeah, we've also got one for the CLI as well. That one's not yet open source, but it's mostly automated; the first 80% of it just runs, and then there's a nice little step of "Go look at this, make sure it's correct, merge the pull request, and then come back to the run book."

**Jerold Santo:** Gotcha. So I'm looking at the Again Desktop release run book, and in the upper right there is a green Play button, and in front of me is "Notes. This run book is a copy of the run book that we use at Again", blah, blah, blah. "Here's dependencies, the release process, version bumps..." It has a typical kind of Markdown-looking documentation, with executable blocks in there, that will run, I assume, on my local machine if I hit the Execute button?

**Ellie Huntable:** That's right, yeah.

**Jerold Santo:** Okay. The upper right-hand corner, with the Play - is that going to run the entire script, top to bottom kind of a thing?

**Ellie Huntable:** Yeah, that's what it does. So again, it's meant to be flexible enough that you can pick an individual block to run if you need to, or rerun, or whatever... But then if you've built it to be sequential, you can just run the whole thing, end to end.

**Jerold Santo:** Nice. And then I assume it just like stops when certain parts fail... Because inevitably, with somebody else's run book, it's going to be like "No, you don't have this thing installed."

**Ellie Huntable:** Yeah, it does. Terminals are the only exception. So terminals need to exit in some way, and they won't exit themselves. So because it's an interactive terminal, we don't know when the command you've run is done, or when what you're trying to do has finished... So you either need to exit the terminal within your script, or you need to press Stop.

**Jerold Santo:** And when you say terminals, you're referring to like an interactive thing that's going to go on in here?

**Ellie Huntable:** Yes. So we have terminals and scripts. Terminals, it will run like your terminal emulator, just in your docs.

**Jerold Santo:** Okay, so it's going to like block and wait for a response.

**Ellie Huntable:** Yeah, exactly. Whereas scripts - it's like running Bash on something, basically.

**Jerold Santo:** Right. So in this desktop release, the first thing I see is just a curl command. That's a script, right?

**Ellie Huntable:** Yeah.

**Jerold Santo:** And then this says "Terminal, install Cargo Bump." That looks like it's also a script.

**Ellie Huntable:** Oh, those are terminals. So if you run one of them, it'll open a terminal locally and run the thing.

**Jerold Santo:** Gotcha. I'm afraid to do that. Oh, look at this... Oh, because I can actually stop, and I can say no, which I'm glad I can, because I'm going to stop it right there... Okay, so terminals are interactive, and then scripts are just going to run, and whatever the response of the script the exit code or whatever.

**Ellie Huntable:** Yeah. The cool thing with scripts is we can capture the output. So if we want to capture the output of a terminal, there's a ton of control codes and various other things going on... But with a script, we can capture the output, and that we save in our local template system. So we support Ginger pretty much, and you can use the output of blocks to feed in as the input of other blocks.

As an example, you might have a Postgres block, and the input for that - you might need a database URI that you can only get by running an AWS secrets manager command, or like a 1Password thing. So you can have all the setup to get you to that point in your own book, and then you can run the query with the output and the script.

**Jerold Santo:** Gotcha. Super-cool. So these examples are very useful, especially if I'm going to start writing my own, because they show you kind of how somebody is really using it... Is there going to be, or is there currently some sort of like compendium of example? Like, beyond your guys' official examples. I assume some sort of hub that's like shared coding thing...

**Ellie Huntable:** \[40:00\] So if you were to go to hub.atuin.sh/ellie, you can see my profile...

**Jerold Santo:** Okay, so this is a thing.

**Ellie Huntable:** Yeah...

**Jerold Santo:** For the listener, she didn't ask me to ask this question. I didn't tee her up on purpose. I really did not know.

**Ellie Huntable:** \[laughs\] Yeah. You can currently share run books only.

**Jerold Santo:** Okay.

**Ellie Huntable:** And they only work for using an online workspace. You can mark them as private, public, or unlisted... I might share a Getting Started guide, or a migration guide, or a self-hosting guide for something I'm sharing with the world... Maybe I'll do a build guide for the desktop app.

One of the other things we want to share on the hub is actual blocks. Currently, you can have saved blocks. Maybe you have something for setting up your dependencies that you do across like 10 different run books... You can just save that locally and then import it into various other run books. But in the future, you'll also be able to share those via the hub, and access other people's blocks... To try and kind of just speed up what everyone's doing.

**Jerold Santo:** This is very cool. This seems like fertile ground for early adopters to get out there and build out their profile, you know? Is it accessible to everybody at this point, it's just not like indexed?

**Ellie Huntable:** Yeah, go ahead. It's not indexed... Go ahead. \[laughs\]

**Jerold Santo:** Yeah, go ahead. How do you do it? Like, if I wanted to start publishing, what would I do?

**Ellie Huntable:** In the desktop app, when you start it up, it'll offer to make an account. If you said no, just click your profile on the bottom left, and you can register there, and that will get you set up with an account. Connect you to the desktop app... You should be good to go.

**Jerold Santo:** Gotcha. Yeah, so I did appreciate that... One of the things I don't appreciate about desktop apps, that should just be usable local without any sort of account, is when they still don't tell me I can use them locally without an account... And yours does say "Hey, sign up." And then it's like "But if you don't want to, click right here and just use it." And so that shows me that you're a person that I, because I do appreciate that. Just let me use a thing. And then if I want to sign up for a reason, like having a profile, make it valuable, then I'll go ahead and sign up when I want to.

**Ellie Huntable:** Exactly. I want it to be useful offline, I want it to be useful open source... And I think one of the big things we're aiming for is, you know, we might not be around in three years time. I would very much like to be... However, if we're not, and someone has built out their whole entire workflow on this, it would really suck if they couldn't use it anymore. So it's important that they still can.

**Jerold Santo:** Yeah. How portable do you think it would be if I was building my run books, assuming the worst you? Like, you disappear, the company disappears, the GitHub repo's gone... Like, I can't run it, I never got the self-hosted thing... Could I get them out relatively easily? It's got to be close to text at the end of the day, right Yeah. So if you're using an offline workspace, it's just YAML on your disk...

**Jerold Santo:** There you go.

**Ellie Huntable:** ...and the format is quite verbose, but a bunch of scripts, and you can pull it all out and it's fine. What you can also do is you can export Markdown. So it is -- we don't really like the fact that there's this YAML as our file format... So the end goal will be to use Markdown as the file format. But what you've probably noticed is that the editor is richer than Markdown provides sort of Markdown for.

**Jerold Santo:** For sure.

**Ellie Huntable:** So figuring out a very light extension we can do that lets us encode everything we need to encode, but also makes it so that you can still actually edit it in a text editor, and read it, and various other things. So that's not done yet, and that's something I want to do correctly, and would actually appreciate input on if anyone has any thoughts. But if you export Markdown, you'll see that there is some front matter in the code blocks, which is how we're currently seeing things.

**Jerold Santo:** Gotcha. Yeah, I think that would definitely be a huge upgrade, the way to get that done. What else are you working on? What else is in the pipeline?

**Ellie Huntable:** Yeah, so coming really soon is a new runtime. The current runtime is very much like "Let's get something that works and see if people like this", and the new runtime is going to be let's make sure things are really, really robust, and flexible, and will allow you to run run books from the CLI... Which is in my mind very important, because then it allows you to run them in the CI systems as well. So maybe you have a README that's getting set up, and you could actually test your README, and that would be really cool.

\[44:18\] Maybe you have a bunch of disaster response run books, and it's really important that they actually work, and you don't find out that they don't work at 3 a.m. when you need them... And if you get things set up right, maybe you could test that on a schedule in some automated system somewhere. I think it's also important just to be able to execute these things without a desktop app if you really don't want to do it, so that's what's coming soon.

**Jerold Santo:** Mm-hm. So when you say a new runtime, can you unpack that phrase for me, and tell me more about what that means?

**Ellie Huntable:** Yeah. So when you click Play on a terminal, there's a bunch that goes on behind the scenes. Currently, the frontend makes a call to the backend to ask it to open a pseudo terminal, and then it gets a handle back, and then it starts writing to that with the input you've provided it... That's like a special case. So the frontend knows that it's a terminal, it knows that it has to open a PTY, and do X, Y and Z. What we're trying to do is get it to the point where the frontend just says "Run this block", and that's it. And that means that the frontend doesn't have to be a desktop app, it could be anything... And it also opens the door to a lot more flexibility in how blocks are defined. So we're not there right now. However, I would love for people to be able to write their own blocks, their own integrations, whether these are backed by a shell command, or some set of code; it doesn't really matter. But right now it's very much like every block works, but it's like a nice sort of combined effort between the frontend and the backend, and we'd like it to be the frontend as minimal as possible.

**Jerold Santo:** It's more minimal, does less heavy lifting, so that a different terminal could call a run book and run it from there. Is that going to require you to first figure out a more permanent serialization format, or you already have that?

**Ellie Huntable:** No... So the serialization is -- there's the in-memory format and then the on-disk format. The on-disk format is the one that's up for change, the in-memory one we're happy with.

**Jerold Santo:** Okay. Right on. It is open source... Is it open contribution? How do you, why do you, when do you, how do you...? Tell me more.

**Ellie Huntable:** \[laughs\] So we accept contributions from anyone. We accept fixes especially quickly. Features - this is something I never really planned out with the CLI, because I didn't think anyone would care when I first released that. We never really thought about how to accept feature requests from people... And in the early days, I was very much like "Oh my God, someone's built something cool. Let's merge it and let's go." And towards sort of more recently, it's been "Is this something I want to maintain long-term? Is this something that people actually want, or does this just sort of bloat the code for no real reason?"

For instance, there's been a pull request open for a really long time that I feel kind of bad about, but someone's added PowerShell support, which is super-cool. However, when he first opened the pull request, I haven't seen very many pull requests from the guy. And if he's listening, I really appreciate your work and thank you very much... However, when he first opened it, I didn't know if he'd stick around, and I made it very clear that I could not maintain a PowerShell integration. It's not something I have any familiarity with. And the dude stuck around for like six months, making fixes to various things, making other PRs... And now it's like "Well, I have trust in your code, and I also have trust that when you say you're going to stick around and keep it going, you probably will." So that's also a consideration I never really had originally.

But jumping back to your original question - open contribution, fixes... Like, anyone fix anything and open a pull request, I'm super-grateful, and we'll review it as quickly as possible. Features - if there's an open issue for something and someone really wants it and wants to make a PR for it, that's awesome. But I do generally prefer an issue before someone makes a PR, purely because it really sucks to say no to something someone's put a lot of effort into.

**Jerold Santo:** Right. It's a lot easier if it's just an issue. If there's code behind it, you're like "Oh, you spent all this time..."

**Ellie Huntable:** \[48:20\] Yeah, you spent all this time on it, and then that's not something we're going to merge, and I'm really sorry.

**Jerold Santo:** Do you communicate a roadmap, or like a place where you're headed? Because sometimes it's hard to know... Like, I have a feature request. Obviously, I could just ask... But if I knew "Here 's's our direction", I could at least say if I'm tangential to it or not.

**Ellie Huntable:** So a roadmap is on the roadmap. \[laughs\]

**Jerold Santo:** Okay... \[laughs\]

**Ellie Huntable:** I'm planning on doing it soon.

**Jerold Santo:** You have a roadmap that includes to create a roadmap. I like that.

**Ellie Huntable:** Yeah. So soon, we'll be writing a ton of issues. Realistically, I've got internal notes and various other things on what needs doing, and now that we're open source, that needs to be made public. The format of the roadmap will probably be mostly GitHub issues, just because that's what's accessible to most people, and pretty much everyone has a GitHub account... But we will be using the forum and the blog more, too. So a lot of the development so far has been on the forum; it's generally where we've found discussions live best. GitHub issues, I tend to prefer keeping actionable. There's a clear reason to close one because a PR has been merged, or something like that. GitHub discussions never really did it for us. They felt like an afterthought from GitHub, to be honest...
**Jerold Santo:** Well, it came years later.

**Ellie Huntable:** Exactly. So Discourse - we host a Discourse forum, and that's been a nice place to host discussions.

**Jerold Santo:** What about the CLI? Do you consider it mostly done? Does it have a major feature requests? Is there a roadmap for that, or what's the status of the CLI tool?

**Ellie Huntable:** Yeah, there's less of a roadmap, more of a bug fixes I will try and get to as soon as possible. Features - I tend to prefer features a lot of people ask for, or that I personally really feel the need for... Which is a little bit selfish, but you know... But it's very much -- I would rather see enough demand for a feature before bringing it in, unless it's very, very obvious that it's needed. There's been a lot of -- I think recently I saw someone talking about being able to add comments and tags and various other things to commands, and I think that is useful... However, my thoughts there are that the interface for actually searching them needs to be perfect. Because there's no point in adding organizational metadata and not being able to search through it effectively. So I think that's quite a large change, and therefore one that unless a lot of our users want it, it's not necessarily worth doing, because then we'd have to maintain it, too.

**Jerold Santo:** And are those conversations going on in the GitHub issues, or is there a separate place for those?

**Ellie Huntable:** Usually GitHub issues, people will make a feature request, and then it can be discussed. But yeah, I need to get better at managing those, because it's a bit of a mess.

**Jerold Santo:** \[51:01\] Fair. Such is life, it gets messy, and sometimes it stays messy... Especially when you have a shiny new object that you're paying all your attention to, right? I mean, this thing is a big lift; I can tell that you put a lot of work into this. And you can't spend all your time on the CLI when you're building a desktop app, right?

**Ellie Huntable:** Yeah, I think it's definitely -- I don't want to neglect the CLI. We had one of our users thank us for not neglecting it, which was nice, because I'm glad people feel that way. But the CLI is definitely much more mature... We've noticed -- you know, when I first released it, a lot of the early issues were very "This does not work at all on my system because of X, Y, Z." And now it's very "This does not work with a very, very specific setup and very specific set of use cases", which is sort of for us more of a signal of maturity, and less of a "S\*\*t, I just broke everything", and more of a "We need to figure out how to integrate with something I'd never considered."

**Jerold Santo:** Something new, or something obscure. Yeah, from my perspective - I mean, I've just been using it kind of how you built it on day one, originally, just ever since. And it just does what it does, and it's mostly invisible. I don't think about it very often. I use it all the time, but without thinking about it, like you do good shell tools. You're like "Well, I don't think about ls very often either, but I'm going to use that one all the time as well."

**Ellie Huntable:** We have a lot of people tell us that they didn't realize how valuable it was until they didn't have it.

**Jerold Santo:** Oh, yeah. That's got to feel good.

**Ellie Huntable:** Yeah, that's cool.

**Jerold Santo:** And who knows, when I get a new machine, maybe I'll finally get the sync to be useful for me... I'm like the only person that doesn't care about syncing things.

**Ellie Huntable:** Let me know if you do, it'd be cool. \[laughter\]

**Jerold Santo:** And I'm going to try to find a way to use this desktop app. I love your work, and I think you put a lot of thought into the way you go about building software, and I think that that's rare, and just refreshing... And it just makes for tools that are delightful to use. And I can tell you put a lot of love into this one, even though it's not exactly right in my daily use wheelhouse. I'll still look for a reason to go beyond kicking the tires.

**Ellie Huntable:** Yeah. I hope you do, but I think in terms of users, it's like, the CLI has a very broad -- you know if you use a terminal, it's probably useful. Whereas the run books app is like maybe less broad use case, but in terms of the actual use, it's much deeper.

**Jerold Santo:** For sure. If you're a user of this, it's going to be part of your daily job, and your team will rely upon it. It'll be very valuable for the people who do use it. So I agree, it'll go deep. And these are people who are generally well-employed at places that have complicated infrastructure, and they need tools like these to make their job not miserable all the time, you know?

**Ellie Huntable:** Exactly. Yeah. That's what we've been seeing.

**Jerold Santo:** Very cool. It was awesome to catch up with you. You've been doing a lot... Anything that we didn't talk about with regard to Again, the CLI, the desktop, San Francisco, motorcycles...? Anything else that you think we should discuss?

**Ellie Huntable:** think we covered pretty much everything. It's been a good chat.

**Jerold Santo:** Absolutely. Well, the website atuin.sh - there you'll find both the desktop app and the CLI. Maybe you'll use them both, maybe you'll use one of them... Maybe you won't use either one, but you can check them out. They're open source. If you want a good Rust codebase to check out, and maybe contribute to our listener, I would submit that to you because she makes good software, folks, and she pays close attention to the details that matter. So check that stuff out.

Ellie, thank you so much. I wish you all the best with this new endeavour... And definitely keep us in the loop, especially if the self-hosted thing comes out. As more things are released and open sourced, don't be a stranger.

**Ellie Huntable:** Thank you very much. It's been great talking to you.
