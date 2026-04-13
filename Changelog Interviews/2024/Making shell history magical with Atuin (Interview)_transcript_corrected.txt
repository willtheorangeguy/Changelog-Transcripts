**Jerold Santo:** Well, we are here with Ellie Huntable, creator of Again. Ellie, welcome.

**Ellie Huntable:** Hi, I'm happy to be here.

**Jerold Santo:** Happy to have you. This is a really cool tool... This is one of those tools that you use, and you're like "Where have you been all my life, tool? I didn't know I needed you." And in fact, I don't even know this entire subset of things, like shell history, was so powerful, until last summer, when we did a show about the Linux command line, and I confessed on that show that I just learned Ctrl+R after multiple decades of Linux use. I had never known about Ctrl+R. And after that show came out, I had a few people on Mastodon say "You have to check out Again. It's like Ctrl+R on steroids, or Ctrl+R with levels up..." I don't know, I can't remember exactly what they said. And I checked it out, and indeed, it was awesome. We put that on Changelog News, and multiple people found it and thought it was cool... And then a few months later you announced you're working on it full-time, and I thought "We've got to talk to Ellie." In fact, Adam, you also linked this up to me privately, like "Should we talk about this?"

**Adam Staravia:** Yeah.

**Jerold Santo:** And I was like "We already booked it."

**Adam Staravia:** Hah! I was like "That's the best day ever, really." Whenever I suggest something, and you're like "Oh, already done."

**Jerold Santo:** Yeah. So we're super-excited to have you. Let's open up with Again, what it is, and why you built it.

**Ellie Huntable:** Yeah, sure. So you've kind of covered it quite well, but firstly, Again replaces Ctrl+R. It provides like a nicer search interface for your command history... But it goes a little bit further than that. There are a few similar tools that make Ctrl+R nicer, like AZF a lot of people use... But the main, sort of this killer feature, I guess, is that it lets you sync the shell history you have between N different machines.

I started this because I had the problem myself, kind of scratching my own itch... I had this really long command that I regularly used at work, that was suddenly useful at home as well... But my work laptop was like at the other side of the room, closed, locked, whatever... And I couldn't quite remember how to do it exactly, so I had to go in and like boot the machine up, login, copy-paste it across, and it was really long-winded... And I actually didn't really want to make a new tool. I kind of assumed someone would have solved this problem already, but I couldn't find anything... So I went from there, and... I had a little bit of time off work for some reason, and I kind of polished up a GitHub README, put it online and forgot about it for a little while... But it turns out a lot of people had the same problem too, so it grew from there.

**Adam Staravia:** I concur, I have that problem as well. I do a lot of homemaking, so not a lot of production work, really... And a lot of my machines are ephemeral because they're VMs, so I will like be embedded and do things and test out, and like, that command history's just like stuck in that machine that's now not even real. It's just back to digital dust on the disk again. So the command line history is there, not with me.

\[08:00\] Now, I'm also a user of Warp, which does supplant some of that... And I thought "Well, this is sort of like an interesting thing... Does Warp use something like this behind the scenes? How does this work with that kind of terminal?" Because warp is doing some smarts there, and keeping some of that history. I don't even know how it works, but it does work, to some degree, but not always perfect, long history... So I imagine that Again is a little bit better than that.

**Ellie Huntable:** Yeah. I mean, from what I know of Warp, they're doing a lot of different things. Shell history there, as far as I know, is not synchronized... And the kind of frustrating thing right now is that Again doesn't work on Warp. Their key binding stuff's not customizable completely, as far as I know... But yeah, there's a comparison to be made, but the main goal with Again I guess is to run in as many places as possible. I actually heard from someone that it runs on their phone, and they only knew this because they were complaining about compile times on phones being quite high... And I was like "Sorry, what? It runs on phones?" So that was pretty cool.

**Adam Staravia:** Are they using Terminus? What are they using? Do you know what app they were using on the phone?

**Ellie Huntable:** Off the top of my head I think it's like Termux, or something like that.

**Adam Staravia:** Yeah, the one I'm using is called -- I think it's called Terminus. Really cool, I like it.

**Jerold Santo:** Well, I'm not using Warp, because they did not yet support Tmux. Until they get there, I will continue not to use it. But... Excited about that. I've actually had this problem inside Tmux even. I think this is fixable with a config, where I'd have multiple Tmux sessions, and even they would not share their history between the two sessions... And at some point, I've found a way of fixing that particular thing, to have those shared, but it was kind of a pain. And Again would have solved that I assume as well, even on the same machine, between sessions, right?

**Ellie Huntable:** Yeah, it does. That's actually something a lot of users say... There is for most shells some config you can do to make sure that all the sessions are shared. But it's not usually the default, and Again just does that automatically.

**Jerold Santo:** So open source, brew install, or apt get, or actually you have a nice - if you're cool with curling and piping into Bash or whatever, Ellie will take care of you and just figure out what system you're on, and what particular shell you're running, whether it's Bash, Shell etc. and get it all installed. Of course, you can do it manually... But sync... Immediately, I hear sync, and I think service. Right? And so this, I guess, leads into the bigger conversation around the sync service, because that's kind of a core aspect of what Again does for you, in addition to just a better UI around finding and navigating and executing your history. But immediately, it's like login, you know? Because the sync service is there. And I went ahead and did it, with a little trepidation.

Now, your docs are nice, and you say right up front end-to-end encrypted, so everything's safe here... But that's going to be a core thing of what you're doing, and you're doing for an open source project now. Do you want to talk more about the sync side of things?

**Ellie Huntable:** Yeah. So you said you were a bit hesitant, right? And for me, trust is super-important, so the end-to-end encryption was a definite requirement from the very beginning. It did make a lot of development very frustrating, because key sharing, key management, all of this stuff is just not that easy. There's also two sides to that, I guess, because users don't want to give me their shell history if it's not encrypted, but I also don't want - I think right now we've got like 70 million lines of history on the server, and I don't want that not encrypted, because all the API keys, all the credentials, all the stuff that you shouldn't paste into your shell, but lots of people do, is just going to be sat there, and that would make me a huge target as well. So it's kind of best for everyone.

\[11:44\] The idea with the sync service, as it's all encrypted, is pretty much just a dumb blob store. It syncs encrypted data; that data can be shell history, in this case it is, but it doesn't really have to be. It's just small little bits of information. There's a very tiny amount of metadata that we sync as well, just in order to make the sync work. Mostly just timestamps and host names. The host names are hashed, just as long as they're different... But yeah, it's actually very simple. I'm giving a really in-depth tech talk about it next month, which I'm looking forward to, but... Yeah.

**Adam Staravia:** I guess sync is required to use Again...

**Ellie Huntable:** Sync isn't required. So you don't have to sign in, you don't have to register, you can just use it locally if you want to, as like a better search interface. If the fact that it's encrypted still isn't enough for you to trust me, you can go ahead and host your own. So there's a Docker image, there's some documentation on how to get it running... There's a Helm chart as well... I know there's quite a lot of people that self-host, and I normally get questions and stuff about it most days... So I've tried to make sure there are options there for whatever your risk tolerance is, I guess.

**Jerold Santo:** What's it all written in? Can you tell us how it works, and all that jazz? Not the full tech talk, but like the quick tech talk.

**Adam Staravia:** A teaser.

**Ellie Huntable:** Yes. So it's all in Rust. Back when I started, my Rust was like -- I'd done it on and off for years, but I never had a job writing Rust, so it was only when I had the energy for side projects... And at the time I was working in Go, and the idea of doing more Go after writing Go all day wasn't really something I wanted to do... And I think one of the biggest selling points of Rust, which maybe isn't included in all the Go versus Rust blog posts is that Rust's just really fun. There are loads of different ways of doing things. When it all works, you sort of feel quite satisfied about it. And three's just like a sense of satisfaction I don't think's there with a lot of other languages. So that was a big selling point for me.

**Jerold Santo:** I've never heard that one. I've heard a lot of Rust enthusiasts, and enthusiasm... I've heard some comparisons - of course hosting... Not hosting, but producing a Go Time podcast, Rust comes up a lot on that... And certain gophers are excited, and other ones are dreading Rust, or combatting it. And I've heard "Rust - hard to learn", and "Sometimes complicated, but worth it..." I've never heard fun. Never heard that. So... "Satisfying" I think is the keyword you used there. What's so satisfying about it?

**Ellie Huntable:** I think, especially in the early days, the compiler shouts at you a lot... It's actually very friendly, so if you're new, don't be scared by me saying "shouting." It's super-friendly. But there are a lot of things you can do slightly wrong; there'll be a lot of \[unintelligible 00:14:12.02\] errors, all these things... And when you first get to the point where like you can write a bunch of code and then there's not really very many errors to fix, that's like a big point of satisfaction.

There's also quite a lot of functional programming inspired functionality, so like maps and filters, all this stuff... And when you first get to the point where you're like "Hang on, this big if/else chain can be written as some pattern matching and some combinatory and stuff", that also feels really nice. I guess it makes you feel a little bit smart, which people like, so...

**Jerold Santo:** Now you're speaking my language. I love good functional tooling in a language or a standard library.

**Ellie Huntable:** Yeah. I think it's kind of the opposite to Go there. Like, Go is obviously intentionally very simple, and Rust is kind of the opposite, I guess, in a lot of ways.

**Jerold Santo:** Well said, well said. So you wrote it in Rust because this was a side project; this was just something that you were doing to scratch an itch, and people liked it... If you look at the stars on the GitHub star watch thing that's embedded in the README, it was kind of slow and steady, and then eventually, there were a few inflection points. How did people find it? Did you get the word out on your own? Did you slap-up a website? Tell us about the boring kind of branding and marketing side of open source.

**Ellie Huntable:** Yeah, I think at first I just put it on Twitter, and I had a decent number of retweets. I wouldn't say it went like viral or anything, but that got me like my first kind of slow momentum. The inflection points you mentioned were mostly Hacker News and Reddit. I tried posting on Hacker News myself a few times, and it just never really picked up. It's always been when other people post it. There was one inflection point from last year in May, where I was actually on holiday, and that morning I was meant to be going on with this big trip, and I woke up, and my phone was going crazy... And I was like "Wait, what's going on here?" So I was in the car, replying to comments, and stuff... But that was really cool.

\[16:02\] I think a lot of the marketing is down to just having a README that's very clear as to what it is, that makes a lot of sense. Having a nice logo and stuff can be very helpful... I tried to make the installation very, very straightforward. So the call to Bash you mentioned earlier literally just calls your package manager for you, and adds something to your Ash, or whatever config file... So kind of the friction for people giving it a try is very low, so that helped a lot. I think a lot of it's also just luck. It was like the right thing at the right time. It was a need a lot of people had, it turned out.

One other thing that really helped - I gave a talk at FOSDEM, that wasn't really intended as marketing; it was more like I wanted to give a talk, and I had this project, so it was an easy fit. That helped a lot. A lot of people shared it, a lot of people told me they saw my talk... So that was really helpful, too.

**Adam Staravia:** How many people suggest this is a problem? How many people really want their shell history to just go with them? Is this a pervasive issue with developers at large?

**Ellie Huntable:** I think it's a very - almost bimodal problem... Because I've heard some people will just say to me "Why would I want that? I don't get it. This is not something I need." And I've had a lot of people almost say what you said earlier, and like "Wow, where has this been?", I guess. There's been uses sort of telling me that they've been manually keeping their Bash history file over the last 10 years, and having something automate it really helps them out...

And I think there's a lot of people who never really realized the value of their shell history and having something long-term until they've had tools that make it easier... Because most people might use the default setup where not very much history is maintained, it's not shared across sessions, that kind of thing. So...

**Adam Staravia:** I think you don't need it until you know you need it, because you're trying to do some stuff like you did, where you had a command on your work laptop, and it's like "I'm not going to remember that. Maybe I'll throw it in a doc somewhere." Maybe that's the easy way to sort of move some things around, which - I do that as well. But at the same time, your history in some case is like muscle memory; if you can easily search it and find a ZFS command, or the there's a docker PS command I run that just has like a nice formatting, that doesn't do the - like, which machines on this machine are running Docker, and how many instances are there... It's just like a prettier format that I've cargo-culled essentially around, that is just now part of my history. And then when it's not, I bring it back in. But having this, it's like "Well, I don't ever have to lose the history ever again."

**Jerold Santo:** Plus with the nature of the terminal, the more you use it, the more you kind of scrap together, you know, longer and longer commands over time, that do something very specific... And then not need that for a very long time, I've found. And then six months, eight months, two years later, and you're like "I've done this before... And I can't remember exactly what I did, but I know I called cut at some point", or like some terminal command that's in there. And if I can just type in "cut" and look at all the -- I don't cut very often. But if I have the history, and I can remember cut, I can look at the seven times I used cut, and one of them you'll see, like "There it is right there." And you just save yourself so much time being able to just remember that without having to remember it. It really is a time saver...

**Ellie Huntable:** Definitely.

**Jerold Santo:** ...and I got sold on setting your history to like a gazillion, or whatever -- is it infinity? What's the --

**Adam Staravia:** It's so many...

**Jerold Santo:** Ellie, you probably know how this works better than we do. Is there like a maximum history size? Hist size I think might be the --

**Ellie Huntable:** Yeah, it's hist size. I always used to just spam a bunch of numbers until I thought that was probably enough...

**Jerold Santo:** \[laughs\]

**Adam Staravia:** Pretty much.

**Jerold Santo:** Like "How large is my disk", you know... Yeah.

**Adam Staravia:** \[19:48\] I had this one command back in my more tried and true Ruby days whenever I would blow away gems. It was a for loop, that is now on a Mac that doesn't exist for me... And if I wanted to, like you said, recall that command, it's just gone. It's not part of this new environment. Maybe I'm running Jekyll, and I want to blow away the gems and do something different... Now I don't have that for loop readily available. I could probably google it. Maybe there's a gist out there where I stuck it in a gist on GitHub somewhere from back in the day, which is how we used to sort of like \[unintelligible 00:20:20.15\] some ideas and kind of share them, too... But now if I wanted to do that for loop, I'd probably just be like "I don't know how I did it. Forget it."

**Ellie Huntable:** I find as well that as time goes on, the number of sort of original commands you write goes down. Even if you're recalling something from three, four years ago, like you've written it before, and having that history means that the longer you have it for, the less time you spend typing, and that sort of compounds over time.

**Jerold Santo:** For sure.

**Adam Staravia:** Maybe there's a saying, like "Command-lined--" I don't know what... "Prompts/commands are code, too."

**Jerold Santo:** For sure.

**Adam Staravia:** I don't know, maybe that translates here, because you kind of want to keep it in a way, and it's not quite code you write and gets stored. It's history.

**Jerold Santo:** Well, there are entire websites dedicated to awesome command lines, right? Commandlinefoo.com... I'm not sure if it's still active, but I used to go there and just read other people's command lines, and be able to learn what I can do. Ellie, your statement about reusing the same commands over time rings true, because one of the coolest things about Again is the stats sub-command. It has stats built into it. And so you can get a top list of your commands, and also it lists out total commands and unique commands. And I have in mind 15,000 total command history, which I just installed it, and then loaded my history into it... 15,511. I wonder if my hist size is 15,000 or something like that... Or if that's just really how many commands I've done in my days, at least on this computer. And of those 15,500, 4,800 are unique. So would that mean like one in three --

**Ellie Huntable:** Something like that.

**Jerold Santo:** So I'm repeating myself quite a bit, you know? Like, two out of three commands is not unique. I think that's right; that's top of the head math. Here's the moment where I come off later sounding like an idiot, Ellie... Like "Well, this math was awful..." But the point stands. Lots of repeat commands in there, you know?

**Ellie Huntable:** I always find -- we've got a channel on the Discord where people share that sort of Again stats output, and the number of times it's CD or LS at the top is huge.

**Adam Staravia:** Yeah.

**Jerold Santo:** I've got CD at number one as well.

**Adam Staravia:** What else do you do?

**Jerold Santo:** Mix... I run mix a lot. I'm an elixirs, so I run mix... Which is usually just mix test. And I just run mix test over and over again. Gist, which is git status. That's my shorthand for git status. Ex, which is also Elixir; that's starting the Elixir shell. And then smug.

**Ellie Huntable:** What's smug?

**Jerold Santo:** Smug is a Go-based tool for managing Tmux sessions... So you can like to define different Tmux sessions using YAML, or some sort of little config file format. And you can use smug to manage them. So I can say "smug start changelog", and that will launch a specific Tmux session, with three terminals, and this one runs that command, this goes to this directory, this starts that command. And then I can just switch between them quickly. Because I have a few things that I do, but that's about it... And so I use smug to just start that thing, suspend this one, start that one... And it is always just set up the way you like it. So I run that command a lot in order to get into whatever it is that I'm up to... So that's a cool one. It's based off of -- there's an old project in Ruby called Terminator, which does the same thing. And I think Terminator either got unmaintained, or I got sick of having to deal with Ruby in regard to it, and I wanted a universal binary... And Go is very good at that, and so there's one called smug in Go, which - I replaced it. And I think it even uses the Terminator config format or something, so it's like an easy switch... So that's my top five. And then ls, coming in at number six.

**Adam Staravia:** \[24:02\] For sure. That's kind of a cool tool, because getting started is half the battle, right? I guess it creates that momentum. There are no minutiae to do, no ceremony to do. It's just like - what was it, smug changelog, that was it?

**Jerold Santo:** Smug start changelog.

**Adam Staravia:** Yeah, and you're off to the races... Because it's like "Hey, this is what my environment is whenever I do this development, and starting is pretty easy, it's already set up for me..." That's pretty cool. I like that.

**Jerold Santo:** What's your top five, Ellie?

**Ellie Huntable:** So ls, CD, kind of boring... FG as well. You mentioned the Cmd+Z thing earlier, so that's one there for me.

**Jerold Santo:** Totally.

**Ellie Huntable:** Git status and vim as well. So vim is basically Neovim, but it's like a distribution... I had a Neovim set up I maintained for like years and years, and I got to the point where I was tired of constantly updating plugins... So Luna Vim just has them all from the get-go.

**Jerold Santo:** Nice.

**Adam Staravia:** I would share mine, but I haven't trusted you yet... \[laughter\] I'm actually stuck. I was like "Let me trust Ellie in a VM." So I use Warp, I SSH into this VM... And the thing I get whenever I do Again status is - maybe you can help me with this. It says, "Error could not fetch history." I did import my history... And then if I do a different stats, for example, it says "Error. Failed to find Again session in the environment. Check that you have correctly set up your shell." \[unintelligible 00:25:28.24\] command. This is Ubuntu. I think it's 2304, potentially... And I just use your command. I'm like "Yeah, I trust your Bash command. I'll just - whatever you want to do on my machine." Because it's a VM, I don't care, right? And that's what I did. And then I was like "Well, maybe I messed that up somehow." And so I did the import process to import my Ash history. And thus far, I only get errors whenever I do Again stats, or history, because there's nothing there yet.

**Ellie Huntable:** We usually see that error when the sort of shell plugin half isn't properly installed... So maybe it installed to a different config file to the shell you're using, which can sometimes happen, depending on the setup... So an Again session basically just tracks like the current shell session... So we track history per - even though they're all merged, we also track the history per session, and if it can't find that variable, it's not being set by the shell integration.

**Adam Staravia:** Would that be in my Ash file, in my RC file?

**Ellie Huntable:** Yeah, it'll be in your SRC. There should be like Again in it, in there somewhere.

**Adam Staravia:** Yeah. I don't think it's in there then, so that's probably my issue... Well, actually, it's evil... Yeah, there's an addition at the very bottom. It's \[unintelligible 00:26:36.02\] Doesn't need to be a live debug here, but that was my hurdle here. I was trusting you on a VM, okay? I was trying my best to protect my machine from Ellie, at all costs...

**Jerold Santo:** Well, you wouldn't have your history in there either, then...

**Adam Staravia:** Well, I actually did it in a VM that I know I don't need anymore, but it does have some ZFS history. So I was like "Well, it's probably going to be a ZFS fine-tune command." It's like an older thing that --

**Jerold Santo:** You're tainted, man. You're riggin' it.

**Adam Staravia:** Yeah, it's got some history in it... So I was like "Okay, I can use this." And the VM has a backup yesterday, so I'm cool with like - if this VM dies, I'll just like blow it away and restore it from a backup. That's how Proxmox works; it's pretty easy. Okay, so I've got this issue... Maybe I'll try it on my Mac...

**Jerold Santo:** Open an issue.

**Adam Staravia:** ...and I haven't gone deeper. But don't feel bad. I do trust you. \[laughter\]

**Ellie Huntable:** Well, if you don't, it's cool. You can run it on your home lab, too.

**Jerold Santo:** That's true.

**Adam Staravia:** Well, I was trying to.

**Jerold Santo:** That'd be a cool thing, Adam, to set it up on your home lab and run it.

**Adam Staravia:** Yeah, I actually like that idea a lot. Running your own server - I think it's super-cool that you offer that. I did like a lot of the installation process. I can at least share some of my thoughts on the experience here, which was your thoughtfulness in the messaging I think is super-cool. Like, you have the ASCII art going on, and you've got these very polite prompts, detected Linux, checking distro, Ubuntu detected... It gives me all these details, all this different stuff... It runs apt get update from me, which is super-kind of you to give me the latest repositories available...

**Jerold Santo:** \[28:04\] Super-kind... \[laughs\]

**Adam Staravia:** Yeah, super-kind of you. And at the very end, it does all its thing, and it's like "Hey, thank you." And this is how you can like to use it, and contribute, and become a part of community, which I think is super-important for any tool that wants to be adopted... Like, tell me how to adopt. And you've done that. So - very, very well done on that part of it. Even though I've had this Ash evil issue. I'll figure it out.

**Ellie Huntable:** Sorry about that. But no, thank you. Obviously, I don't know how many people click on the links at the bottom of the installer... But I hope that it does help, to some degree.

**Adam Staravia:** Yeah. And you did give a prompt in the next step too, which is Again register, or Again login. So you've already done that... It is kind of hard. I would say if I didn't go there and do that, it would be kind of hard to understand what the next steps are. Like, give me a quick win. The import - like, hey you might want to import. Because I didn't know that. That might be something to add there. Like "Hey, to get started, just run this command to import, and then you can run stats", as an example, because you probably have all the data, and you can run stats, because you have all of it imported. And you get a quick win, like "Oh, I get how this thing works. I get how this thing will help me."

**Ellie Huntable:** That's a good suggestion, thank you. I'm actually thinking of doing like Again Setup, which just is this kind of little linter interactive wizard that just does the lot for you.

**Adam Staravia:** Even better. Yeah. ATI. That could be fun.

**Ellie Huntable:** Yeah.

**Jerold Santo:** Well, I would definitely agree on the setup process and the documentation was all very hand-holding and nice. And even when I was feeling like "I don't know if I want you, like --", right there you're like "No, it's end-to-end encrypted." I'm like "Alright, so this person cares."

**Ellie Huntable:** I also kind of figured that if I was a user, I would be like "No way are you're getting my data", so I had to make sure it was like something I would use if I was on the other side.

**Jerold Santo:** Exactly.

**Break**: \[29:44\]

**Jerold Santo:** So when you decided to quit your job to do this, what --

**Adam Staravia:** What were you thinking...?!

**Jerold Santo:** When -- who, what, when, where, why?

**Ellie Huntable:** So I started 2023, and this was just like a random little side project. It was going okay, it was some bit of fun... And then after my talk at FOSDEM, some of the other speakers I was speaking to, one of them sort of says to me "You should take this more seriously, think about monetizing it" etc. And I wasn't 100% convinced at the time, but it sort of sat in the back of my head, and throughout that year, after a lot of the reception I got, I started spending an extra few hours \[unintelligible 00:35:45.19\] few days just polishing, improving, that kind of thing. And the user growth we got was huge. We had more growth in 2023 than we'd had in the previous two years, by a long shot.

And I kind of got to the end of the year, and I'd always fancied having a go at building my own company, and I had this project that was continuously growing... It was sort of continuously demanding more time as well. And I got to the point where I was like "Either I give this a go and try to make something of it, or I reduce how much time and energy I'm putting into it, because it's not sustainable. I can't have a full-time job and be handling support, and prioritizing issues, and all of this, in a way that's going to continue to grow."

I think there's a bit of a gap in sort of the shell as it is. It hasn't really changed a lot in a long time, and the way you said earlier, about how "The shell's code, too", or something like that; maybe I'm not quoting you exactly, but I think there's a ton of developer tools focused around writing software, but people who spend a lot of time in the terminal are almost underserved right now.

**Adam Staravia:** Yeah, I agree. The command line code is code too, I guess. I don't know. Your command line commands are code, too.

**Ellie Huntable:** Exactly.

**Adam Staravia:** I feel that. Even during the process, you recognize which distro I'm using. That's cool code. Is that in Rust as well? What are you doing to confirm which distro? Do you have like a massive if statement, or like something like that? Or \[unintelligible 00:37:12.01\] statements?

**Ellie Huntable:** It's a chunky Bash script.

**Adam Staravia:** Yeah, okay. I mean, that's fun, too.

**Jerold Santo:** That's code, too. \[laughs\]

**Ellie Huntable:** Yeah.

**Adam Staravia:** And I like Bash scripts even, too. I mean, I like them because they're useful tooling that you can make for you. They're very bespoke for what you need. And I think in my last year and a half, I've become more empowered with ChatGPT and coding tools, because there's just so much knowledge out there in AI land to generate, or at least guide me on Bash scripting... Where I'd never really -- I felt intimidated by it, because I was like "I'm not that kind of hacker, Adam. Come on, you can't do this." But then I'm like "I need to do it", and so I found out how to do it with my buddy, Code Gen AI stuff... And now I have lots of Linux tooling that I use myself for various things, that are not really probably useful to anybody else, but they're useful to me only, and they can be highly specific. Whereas before, I would have never done it. But it's totally code, too. And I have no idea where to keep it at. It's in a repository, but the true version of it - how do you deploy it? How do you easily get into like an apt repository you can install yourself... That whole world is weird. If you write your own little tools, how do you install your own little tools? I would love somebody to solve that problem better, or at least document how to better add a repository to apt, so that I can easily install my own things from a GitHub repository... Because my central repository of it essentially is living in my bin folder, my own personal bin folder. Wherever I put my stuff at. That's the version, and it changes without being versioned. Because I'm an idiot. It's just my own tooling. If that was better, that'd be cool.

**Ellie Huntable:** It'd definitely be very cool.

**Jerold Santo:** Adam, do you remember RVM?

**Adam Staravia:** Oh, yeah. Of course.

**Jerold Santo:** Ellie, are you aware of RVM? Ruby Version Manager?

**Ellie Huntable:** Yeah, there's a few similar for other languages as well.

**Jerold Santo:** Yeah, it was kind of the first one that ended up being like NVM, Node Version Manager etc. And RVM was famous, but also a little bit infamous, because the entire thing was written in Bash. And it was a lot of code. And it was very complex once you got into there... And RVM had some -- I mean, a lot of users, a lot of bugs, a lot of issues. And then as a user, you dive into it, and you're a Ruby person or something, and all you're seeing is like -- I can't remember the guy's name who wrote it, but he knew Bash very, very, very well, to the degree where you're like "This is borderline too much Bash..." Anyway. At one point, he decided that he was going to make a package manager, or I guess for the listeners who aren't aware, RVM, Ruby Version Manager --

**Adam Staravia:** \[unintelligible 00:39:50.22\] is his name. We talked to him back in 2013, Jerold. That was a long time ago.

**Jerold Santo:** I feel like there was another fellow that's not \[unintelligible 00:39:57.28\] I remember Michael.

**Adam Staravia:** \[unintelligible 00:40:00.29\]

**Jerold Santo:** Yes!

**Adam Staravia:** \[unintelligible 00:40:02.19\] maybe...

**Jerold Santo:** \[unintelligible 00:40:04.04\] Did they work on it together?

**Adam Staravia:** I think he was the originator...

**Jerold Santo:** \[40:10\] Okay... \[unintelligible 00:40:10.11\]took it over and had to maintain it. Okay, it's all coming back to me.

**Adam Staravia:** I think Michael took over a lot of the issues really though, and he felt -- there was like a burnout stage there too with Michael.

**Jerold Santo:** Wayne was super-into Bash. Maybe he still is. I haven't kept up with him.

**Adam Staravia:** Yeah.

**Jerold Santo:** And I remember at one point he talked about writing a Bash package manager for x, where x is whatever it is you wanted to manage. It was one of these "I'm going to engineer the general thing that solves all problems", kind of situations that we get into as engineers... And the reason why I think of it is that his deal was like "You should just be able to package-manage your Bash scripts, just like you can other things", which is kind of what you're asking for, Adam.

**Adam Staravia:** Yeah.

**Jerold Santo:** It's like, "Just give me a way of packaging up and deploying, even if only to myself", which a lot of us do with our dot files synced across machines. It's like, you write your little Bash scripts and your functions and stuff into your dot files, and use Git to basically synchronize those across machines... Which is a poor man's solution, but it works, to a certain degree...

**Adam Staravia:** Better than going the route of doing it distro, or package manager-specific, like apt, for example... Because if I need the same bin options on my Mac, then maybe there are dependencies required, or whatever; I don't know.

**Jerold Santo:** Usually, you'll end up with some sort of platform-specific conditions in your scripts, which - I know I've had in my days when I'd check "Is it Mac, or is it Linux?"

**Adam Staravia:** All the ones I've been writing translate from Mac to Linux, no problem. So long as the package \[unintelligible 00:41:46.01\] or ZFS, or whatever, those things - as long as it's present, then it runs.

**Jerold Santo:** Anyway.

**Adam Staravia:** And there are checks you can do in the Bash. But anyway, we're in the weeds...

**Jerold Santo:** I was just thinking, I was just reminiscing, and thinking a little bit about that as something that doesn't exist, that I know of... Maybe people know ways that you can deploy out your little scripts to yourself and to others in a way that's a lot like NPM install, or cargo install, where they have these language-specific things. This would be more generic.

**Ellie Huntable:** I think it would be cool, also even for internal tooling... I've been in jobs before where some of the onboarding is like "Please copy-paste all of this from the wiki into your dot files", and it's not great, right?

**Jerold Santo:** Right. So maybe a new frontier for Again at some point, you know?

**Ellie Huntable:** I actually just made it sync aliases earlier today.

**Jerold Santo:** Really?

**Ellie Huntable:** So there's some scope for that, too.

**Jerold Santo:** Oh, okay... So now we're starting to see what may be a potential future for this looks like.

**Ellie Huntable:** Maybe.

**Adam Staravia:** I use something from Thought bot for some of these things... I think it's cup, or RC something...

**Jerold Santo:** Yeah, there's lots of different -- people have taken different whacks at this, I think, over the years... But yes, syncing aliases...

**Ellie Huntable:** So yeah, kind of the inspiration there - I had a lot of feedback from users that it's the first thing they install on their machine, and then from there they recall other commands for setting up the rest... And it's like "Well, if you didn't have to recall the commands, and you could just install it on your machine, and then your setup's right there, then that would be in the next step."

**Jerold Santo:** Bam.

**Ellie Huntable:** Yeah.

**Jerold Santo:** So this is like -- this could be your dot file synced, and your environment setup synced, without a GitHub repo or something. All you needed as Again, and you're already logged in.

**Ellie Huntable:** Exactly.

**Jerold Santo:** I love it. I love it.

**Adam Staravia:** We sidetracked a little bit... Is it trivial to run your own server in a home lab or on prem? Like, is it pretty easy?

**Ellie Huntable:** It should be. And if you have any problems, let me know, because I want to make it easier... It's just Postgres, at least Postgres 14, and run a binary. And that's it.

**Adam Staravia:** I guess I can probably voucherize that. I would prefer Docker in that scenario.

**Ellie Huntable:** We have a Docker image, too. There's a Docker image, there's an example with Docker Compose, and there's a Helm chart.

**Adam Staravia:** Oh, that's too easy then.

**Jerold Santo:** And I think there's some Kubernetes community distro thing people have for home labs that have it included, too... I can't remember what it's called now, but...

**Adam Staravia:** I'll test it out after this conversation. I'll give play with it and give you some feedback. Oh, I see it, yeah. Under your docs, self-hosting. Server setup, Usage, Docker, Kubernetes. Very cool.

**Jerold Santo:** \[44:13\] So here's a setup that I think has worked in the past... It's like open source library or framework or system with a hosted business attached to it, where the end user is more mainstream, more normal, less nerdy. But when you have open source tool service as the business model with your core audiences super-nerds, like Adam, who gets excited because he heard Docker, or somebody even nerdier, who hears Helm chart and is like "Let's go!", which I'm sure some of our listeners are like "Oh, good. Helm chart. Cool." It seems like that's harder for the business side, isn't it? Where it's like, the people who are your core demographic of potential purchasers - because they're all command line users - they also are super-down with self-hosting.

**Ellie Huntable:** I think it's split. I think a lot of the sort of early users are very down for self-hosting, very down for customizing things... But I think there are tons of people that don't actually know how nice the shell can be, and how things can be better... And if there was a very easy way for them to have a nice setup, that felt modern and was good, and they didn't have to know what sort of scripts and plugins they need to install and which things they need to add, and all of this, which most people will just stop caring as soon as they start seeing this huge list of stuff... If it was nice, with no effort, I think we could have more people using the terminal much more.

**Jerold Santo:** I agree with you. And I also want to recognize that amongst the nerdy ones, like Adam, there's also me. I have no interest at all in self-hosting, even though I totally could do it. I just don't want to. Furthermore, I would happily sign up for the service and pay the money on a recurring basis to have you handle that for me. So even amongst -- there's a lot of homemakers, a lot of self-hosted amongst us nerds, and then there's also the ones that are just like "I'd rather not. I'd rather give Ellie my money and --"

**Ellie Huntable:** Maybe I'll hold you to that recurring payment thing.

**Jerold Santo:** Hey, I'm into it. I'm interested, for sure. Especially if you are just gonna automatically sync all my things. It's cool. It's very cool.

**Adam Staravia:** Yeah. My reasoning is not to not pay...

**Jerold Santo:** We know that. We know that you're just a tinkerer.

**Adam Staravia:** We even talked about that with Obsidian. I think Nick and I talked about that when we were at that conference. We were talking about Obsidian \[unintelligible 00:46:30.21\]

**Ellie Huntable:** I love Obsidian. Yes. It's my favourite thing.

**Adam Staravia:** And you use their sync service?

**Ellie Huntable:** I do.

**Adam Staravia:** Were you early enough to get the half off discount? Nick Nisi got this early adopter, super-cool person discount that's like forever...

**Jerold Santo:** Super-cool person discounts... \[laughs\]

**Adam Staravia:** Because Nick is cool...

**Jerold Santo:** I don't think that strikes true for Nick, but... We'll see.

**Adam Staravia:** Come on... \[laughter\] Well anyway, I pay 10 bucks a month. Do you pay 10 bucks a month for sync?

**Ellie Huntable:** Yeah.

**Adam Staravia:** Yeah. I don't want to pay that number, but that's not exactly what I think the value is that Obsidian gives me. It's thinking. It seems to be pretty trivial to do. Like, why not just give somebody the option to run their own server? I don't know, but that's why I think about this; not so much not paying you, but more like just even data protection, or just for learning. How does this actually run? What does it take to -- because I don't get to do SRE stuff as a living...? I'm a podcaster. My SRE for a living is myself and my home lab and tinkering. And so that's why I do it, to learn. Less about keeping my own dollars...

**Ellie Huntable:** Yeah, when I have been SRE for a living, my home lab got neglected quite a lot.

**Adam Staravia:** Yeah. What's your home lab then?

**Ellie Huntable:** It's pretty simple... It's just like a little Ubuntu server with a bunch of ZFS stuff running on it. With a bunch of Docker containers for my home media setup, and like a Prometheus and Grafana dashboard setup, and stuff. Doing a little bit of home automation at the moment, just because maybe future me will want to know the temperature in my kitchen 10 years ago... \[laughs\]

**Jerold Santo:** You never know.

**Ellie Huntable:** We'll see.

**Jerold Santo:** Very cool.

**Break**: \[48:16\]

**Jerold Santo:** So when you decided to quit the job, let's go back there.

**Adam Staravia:** Yes, I like this. Go back there. I was about to go back there.

**Jerold Santo:** Yeah, good. We moved far afield...

**Adam Staravia:** "Yeah, good. You're boring me, Adam."

**Jerold Santo:** Yeah, good. You're on track. Well, we're on the same page. I also was happy you brought us back to the home lab. But - well, you kind of gave a little bit of your thought and your reasoning, but maybe just expand more, talk about money, talk about life... Tell us the inside scoop on what you're thinking about it.

**Ellie Huntable:** Yeah, sure. I mean, money-wise I'm quite lucky. I've had a good career. Furthermore, I've got plenty of savings. My outgoings are pretty low. Like, it's just me. I've got no kids, mortgage, whatever... So it's a bit of rent, and money for my motorbikes. That's pretty much it.

**Jerold Santo:** Nice.

**Ellie Huntable:** But yeah, so the outgoings were low. I had enough for at least a year, so I'm good there... I just figured that - you know, have you ever had something that you have to work on, and like if you don't, it's going to bug you forever? It's one of those things, I figured I had to give it a go, otherwise I'd always wonder "What if I had tried? What if I had done this?" And at the end of the day, it's maybe a small risk, but I don't think doing this will make me any less employable if it doesn't work out... So it's something I really wanted to at least give a shot.

**Jerold Santo:** Did you set parameters around what success looks, what failure looks, when you're going to call it a day if there is one, or do you have a business model? How much did you put into it where you're like "I just want to work on this, I'm going to give it a shot"?

**Ellie Huntable:** Yeah, I was kind of trying to get a nice balance between planning enough, but also not making it too rigid... Because obviously, when you go from fitting something into your mornings and doing something full-time, a lot can change. So the way I saw it was like the first six months of the year wouldn't be focusing too much on getting revenue, they'd be focusing on making sure I'm building the right thing, making sure I'm building something people want, making sure that any sort of frustrations peoples had were solved. And then the latter six months of the year I'd be thinking more about making sure I can pay rent. That's the main plan. I'd kind of like to start addressing some more team use cases later in the year as well, but again, the first, at the beginning it's just focusing on making sure individuals are very, very happy with their shell.

**Jerold Santo:** And how long have you been doing it?

**Ellie Huntable:** So full-time, like six weeks. Otherwise, it's like three years now. The first majority of that was very sporadic, though.

**Jerold Santo:** Yeah. So six weeks full-time. Are you having a blast, or what?

**Ellie Huntable:** Yeah, it's been great. It's cool, because -- I don't know, I've had loads of ideas I've wanted to explore, but I've never had the time and the energy... So being able to tie up so many loose ends from last year... As an example, the first version of the sync that Again had was like mostly good for most use cases, and it lasted way better than I thought. I think there was a comment from the first version that was like "This is really naive. Improve it", and I've never got around to fixing it. So that was like a prototype sync v2 that was sitting around for all of last year. And in the first few weeks of full-time I managed to finish it, and we rolled it out a couple of weeks ago. It's working so much better, and it's nice to have been able to do that. I think that's very important for laying the foundations for everything else.

**Adam Staravia:** What are you doing to ensure you're building the right thing? Is it just Discord? Is it emailing? Is interviewing? And what do you do to ensure this?

**Ellie Huntable:** It's a big mix... So Discord has been great; that's been growing constantly. People give me some really nice feedback there. I think -- I can't stick to just Discord, so there's also a forum now, which is mostly for support, and that's been perfect, too. I've been doing user interviews too, so I have like little video calls with people and talk about what they like, what they don't like, what other problems they might have, what they'd be willing to pay for, what they might not want to pay for, that kind of thing. That's been going pretty well, too.

**Adam Staravia:** Did you say mountain bikes when you said to --

**Jerold Santo:** \[56:00\] No, she said motorbikes, didn't she?

**Ellie Huntable:** Yeah, I'm kind of obsessed. It's like my not-computer thing to do.

**Adam Staravia:** Where do you live at again?

**Ellie Huntable:** I live just outside of London.

**Adam Staravia:** A lot of good trails there, right?

**Ellie Huntable:** Kinda... I mean, the UK is a bit mixed.

**Adam Staravia:** It's always raining...

**Ellie Huntable:** It rains a lot.

**Adam Staravia:** You can ride in the mud, though. We can't ride in the mud around here.

**Ellie Huntable:** I mean, it's --

**Adam Staravia:** It sucks, but I like it.

**Ellie Huntable:** Yeah, I mean... Motorcycles in the rain - they're still fun, but it's very different, and it's like more dangerous.

**Adam Staravia:** Yeah. Okay. A little side-track there. I wanted to check that, because I thought I heard you said motorbikes, or mountain bikes. I wasn't sure which one.

**Jerold Santo:** So for other people who are into motorbikes, which I'm not - I'm asking this for them - what motorbike do you have? Is it awesome?

**Ellie Huntable:** The Husqvarna 701 Supermom.

**Jerold Santo:** Okay, Husqvarna I'm aware of, because they make very good riding lawnmowers around these parts.

**Ellie Huntable:** And chainsaws, apparently.

**Jerold Santo:** Yes, chainsaws too.

**Ellie Huntable:** And they're all just three numbers, so you don't know what you're getting. It could be a chainsaw, it could be a sewing machine, it could be a motorbike.

**Jerold Santo:** \[laughs\] Do they make sewing machines, too?

**Ellie Huntable:** They do. I've found that out recently.

**Jerold Santo:** That's hilarious. You never know until the box shows up, and you're like "That's too small for a motorbike. It looks like a sewing machine."

**Ellie Huntable:** Exactly.

**Adam Staravia:** What do you think the possibility is, with Again? What do you think you might be going towards? I know this is early days, six weeks full-time at least... But what do you think that -- what's the big dream?

**Ellie Huntable:** I think the big dream is to kind of hit all the use cases. Like, I want power users to love using it because it's customizable, it lets them get what they want out of it... I would love it if people who are less comfortable in the command line, and kind of freak out, and are a bit scared, feel so much more confident using it... And I would love for teams and organizations to be using it just to accelerate their productivity, to make sure everyone's got the right setup on their machines, and to make sure that sort of the shell that hasn't changed for a really long time is heading in the right direction, I guess.

**Adam Staravia:** You mentioned, I guess, Warp, to some degree... A lot of folks use Terminal app on Mac, or pick your terminal flavour on Linux... I'm not even sure, I don't use Linux desktops, so I can't say for sure. It's still not the year of Linux desktop, so there you go...

**Ellie Huntable:** Maybe next year.

**Jerold Santo:** It's always next year.

**Adam Staravia:** It's always next year. How does Again fit into the world of like warps, for example, where they want to supercharge or be the terminal of the future, and they're trying to -- and there's even our friends that... Not bubble tea, but... What's their name, Jerold?

**Jerold Santo:** Charm.

**Adam Staravia:** Charm, yes. You all are sort of like all wanting to improve the command line, one organization project dream at a time... And I feel like there's a version of you all that come together and just like coalesce into a great symphony, or something like that. How does it work with the Warps, and the non-Warps, and the things that sort of add things? Is it challenging to work around those things? Like you mentioned, it doesn't work right. Describe that.

**Ellie Huntable:** Yeah, I mean, I guess it's different challenges. Warp are in a nice place where they control the sandbox. Everyone's using their terminal, they've got the whole thing from the bottom up... And the downside there is that they have to convince someone to download and use a new terminal, which - I don't know anyone there, but I imagine they struggle with that... Whereas the challenges that we have are a little bit different, in that the friction to get started with Again is quite low. It's just a plugin to install into what you already have. But the flip side there is that the number of things it can conflict with and the number of different setups people have is like huge... And I didn't realize when I started this, the number of weird, very weird installs some people would have... Like, some strange terminal on Windows that when you're SSH-ed into a different machine and have three specific plugins it doesn't work, and it's like "Well, great. I never really envisioned someone would do that... But let's see how we can sort that out." Yeah, I'm not sure if I answered the question, but...

**Adam Staravia:** \[01:00:00.15\] Well, I think just mapping around the - I guess, the land of terminal, which is like the Wild Wild West, in a lot of ways. There's no right way or wrong way. It's just the way. And there is no --

**Ellie Huntable:** Exactly.

**Adam Staravia:** There's no way to determine this random SSH session on Windows with \[unintelligible 01:00:15.17\] plugins. You just can't predict that, right?

**Ellie Huntable:** Exactly. So I think there's somewhere in the middle where everything converges, and that's where the answer is... But we'll see.

**Jerold Santo:** So you don't need much money, so I'm guessing you haven't raised any money, or have decided to take on investment... Do you have a posse? Do you have folks behind you rooting for you? You have fans, I know that, because they hit us up on the socials, and they're like "Hey, Again's awesome."

**Ellie Huntable:** The support has been amazing, actually. I didn't really realize that many people cared that much... So that's been lovely, especially on Mastodon. Lots of people are like "What? On Mastodon? Why? Where?" And every time I post about it there, I get loads of nice feedback and loads of support, so that's lovely. Thank you to anyone listening to this.

I think funding-wise, no, I don't have any funding. I sort of consider a little bit of angel money at the moment, maybe... But again, I don't need loads of money right now. The most expensive thing is my time, and I'm good with that for now. I guess I'm not ruling it out for the future, but it's not a thing in the present. I don't think -- if someone gave me $2 million tomorrow, pretty much the only thing I could do with it is hire people, and I don't think that's the right thing right now. Furthermore, I think it'd be the wrong incentive at this point.

**Jerold Santo:** Sure. Is there anybody else working on it with you?

**Ellie Huntable:** Not full-time, not like this. There are a lot of open source contributors who are amazing, and I really appreciate them all. It kind of varies. There are some regular contributors, and some of them have their special sort of interest areas of what they like to work on... And there's a lot of drive-by contributes, too. So someone will have something that annoys them, and then they'll come and fix it, and then vanish. I post everyone a sticker, so... I mean, I know it's not going to show up for the audio, but I got one of these, and every --

**Jerold Santo:** Cute. Is that a turtle with a wizard hat on?

**Ellie Huntable:** It's got a wizard hat on, and it's sparkly. It's for everyone who contributes.

**Jerold Santo:** And the shell is kind of a gem, or something.

**Ellie Huntable:** Exactly. It's like a magic shell. So anyone that wants one, I'll ship them out.

**Jerold Santo:** Nice. It's cool.

**Adam Staravia:** I like that mascot.

**Jerold Santo:** What's the name? Again?

**Ellie Huntable:** It doesn't have a name... I should probably -- Again, yeah.

**Jerold Santo:** No, like what does Again mean? Why did you pick that name?

**Ellie Huntable:** Oh. My favourite book series is the sort of Terry Pratchett Disc world universe. I don't know if you're familiar with it... The premise kind of comes from a lot of -- the premise is that there's like a giant turtle in space, flying, swimming around... He has four elephants on his back, and then the world is like a flat disc on the back of the elephants. It's kind of like a wacky fantasy series.

**Jerold Santo:** Okay.

**Adam Staravia:** Oh, yes.

**Ellie Huntable:** And the name of that turtle is The Great Again. It kind of came from that. It's been adjusted slightly... But the concept comes through like a lot of old religion and mythology, of like the world turtle.

**Jerold Santo:** Gotcha. Interesting. The world turtle. The magical shell.

**Adam Staravia:** Yeah, I've heard some people say -- I'm not sure what the context was, but like we're all just on a world, on a turtle's back, flying through space, or something like that. I've heard that at least somewhere, in a geek land of some sort. I'm not sure which.

**Ellie Huntable:** There's a big intersection between computer nerds and Terry Pratchett fans.

**Jerold Santo:** That makes sense.

**Adam Staravia:** Okay.

**Jerold Santo:** Is there a tie-in to turtles all the way down from that, or no?

**Ellie Huntable:** No, but it is fitting. I mean, there might be, but not that I'm aware of.

**Jerold Santo:** The synapses connected in my brain, but I don't know the history of the phrase "Turtles all the way down" well enough. But I just figured, nerds and turtles - there you go.

**Adam Staravia:** Nerds and turtles. Well, does the mascot, the icon, does it have a name?

**Jerold Santo:** No.

**Ellie Huntable:** It does not. I've been debating --

**Adam Staravia:** Can I suggest a name?

**Ellie Huntable:** Go for it.

**Adam Staravia:** Shelley.

**Ellie Huntable:** I like that, actually.

**Jerold Santo:** Oh, that's cute.

**Ellie Huntable:** Yeah, maybe it's Shelley.

**Adam Staravia:** That's a pun, and it's good.

**Jerold Santo:** That's a good pun.

**Adam Staravia:** Yeah. I would dig it.

**Jerold Santo:** That's almost as good as my TNT tie-in from the other day.

**Adam Staravia:** So good... Yeah.

**Jerold Santo:** \[01:04:12.08\] \[laughs\] So bad it was good. I like Shelley. That's actually good-good. It's not bad-good. That's good-good. So Ellie, which rhymes with Shelley by the way, in case you didn't notice... How can we help? How can the Changelog community, our listeners, fellow nerds, terminal junkies, Adam and I - like, I'm rooting for you. I think it's really cool. I hope you make it even cooler, and that you can do this as long as you want to. So how can we help, how can we get involved? What would help you?

**Ellie Huntable:** I mean, even just being here and sharing it is huge... So I think if anyone who wants to help out could check it out, give it a try, let me know what you think... All the feedback is good, even if it's not obviously positive. Sharing it with people you think might be interested is also great. So this has spread pretty much entirely through word of mouth. So continuing that would be fantastic. But no, just more of the same. It's fantastic. Thank you so much.

**Jerold Santo:** Adam, any final thoughts, or lines of questioning?

**Adam Staravia:** Not necessarily. I think the trust factor is - like, in the whole happy path of getting started is all registering. And I think there's an analogy, initially. Even with Jerold, when we first talked to Zach Lloyd with Warp - we talked to him twice now on the podcast - it was like "We don't want to have to register to use the terminal." And I get it, I understand all the superpowers you get from doing it, and I get that we can trust you, I understand all that... I think just generally hackers are like "I would rather not..." So I'd like a more squeaky, or I guess a more smooth path to the nonregistered version to sort of get a win early on, and let the trust be earned over the usage of the tool. Like, that would be feedback from me. Because that's -- that would be my hurdle, really. And I know this isn't feedback time, but that's my one thought after talking to you, and knowing what the tool is, and what it can do... That's, I think, probably a hurdle you're having to deal with.

And the server is awesome, but I don't think somebody's going to stamp a server just to bifurcate the option to trust you. I think it's just going to be like "Let's just figure out how to get to a win with it, without having to do the whole -- let me put it in your cloud, kind of thing", or whatever, however that looks, you know?

**Jerold Santo:** Well, what's the third option? So if they're not going to run their own server, and you don't want them to register, what could Ellie do?

**Adam Staravia:** Well, you don't have to, right? You can just like sync it locally. Isn't it local, if you don't register?

**Ellie Huntable:** Yeah, you can use it offline. It won't sync, but it's still useful.

**Jerold Santo:** But that's the core feature that it offers, Adam.

**Adam Staravia:** Well, you get the usage of the tool. I think that's what's cool for me. It's like "Well, okay, now that I see this tool is cool, and how I can use it in this one single environment, I know I want it over there too, and over here too, and now I actually want to opt into sync later on." Give me the tool and its usefulness, and let sync be a superpower that I sought after, after I trust you. Because I don't need to have syncing to enjoy stats immediately, as an example. That was my hurdle here on the call, was I just couldn't share that with you all, because I have my issues. And I'll go back and fix that, and that's not your problem... But I think ultimately, you may have the loss of somebody's attention at that moment if they're just like "I can't figure it out. It's not that big of a deal to me, let me move on." I think over time, that'll be a challenge.

**Jerold Santo:** Yeah, maybe if you started with the stats and the history, the actual Ctrl+R replacement as this part of this setup that you're working on... And at the end of the setup was now the sync option, which requires either self-host or login right now. Register. I can see that, because I think I would potentially download it and use it to get to the stats, and just to replace Ctrl+R, if that was obvious and good enough for me... To be like "Oh, I love Ctrl+R on steroids", or whatever way you are able to pitch that... Because I realize that steroids have also bad effects on the body, so maybe not the best --

**Adam Staravia:** Call it on strawberries. Strawberries are great for you. They give you energy.

**Jerold Santo:** Oh, on strawberry.

**Adam Staravia:** Yeah, antioxidants. Amazing for you. Great for your skin.

**Jerold Santo:** Alright, so Ctrl+R on strawberries, plus the history, the stats might get me install it. And then by the way, sync. Oh, wow.

**Adam Staravia:** Yeah.

**Jerold Santo:** So I can see what you're saying there, Adam.

**Adam Staravia:** Yeah.

**Jerold Santo:** But I think as you build your developer environment synced everywhere thing, a lot of people are going to come for that exact reason, and they're \[unintelligible 01:08:29.07\]

**Adam Staravia:** For sure. For sure.

**Jerold Santo:** Because I think we understand that a sync requires some sort of "cloud computer." Somewhere that's not our computer. And so either registering or hosting your own server makes complete sense.

**Ellie Huntable:** Definitely, thank you. I'll bear that in mind.

**Jerold Santo:** Whereas with Warp, it was like "It's a terminal. I don't want to have to sign up and sign in to use a terminal." But it's a sync service. This becomes a sync service, so I get the reason. But I agree.

**Adam Staravia:** For sure.

**Ellie Huntable:** Thank you. I think I'll do something like that for the sort of handhold the setup \[unintelligible 01:09:02.18\] maybe.

**Adam Staravia:** But I dig it. I'm excited for you. I think Shelley's a hit. Turtle in the back, worlds on a turtle's back, flying through space...

**Jerold Santo:** How do we get some of those stickers?

**Adam Staravia:** Yeah, let's get some stickers.

**Ellie Huntable:** If you send me your address after this, I'll send you some.

**Adam Staravia:** Fantastic.

**Jerold Santo:** Alright...

**Adam Staravia:** Alright, it's been fun. Thanks, Ellie.

**Ellie Huntable:** Yeah, it's been great. Thank you so much.
