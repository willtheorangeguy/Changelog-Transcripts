**Jerold Santo:** Let's begin at the beginning... Postgres.

**Heidi Linnakangas:** Yes, Postgres.

**Jerold Santo:** 1986, something like that. It wasn't forever ago...

**Heidi Linnakangas:** There's a release from Berkeley University in 1995...

**Jerold Santo:** Okay.

**Heidi Linnakangas:** I'm not sure how long it was developing in the university before that. Several years...

**Jerold Santo:** I read there are roots back into the '80s, but I could be wrong.

**Heidi Linnakangas:** It could be. It could be.

**Jerold Santo:** Either way, that's ancient history, right?

**Heidi Linnakangas:** That's a long time ago.

**Jerold Santo:** And yet, it's the darling of most developers today, Postgres.

**Heidi Linnakangas:** It's become popular. When I started to hack on Postgres, it was not the case. It was not the most popular one, it was not the darling.

**Jerold Santo:** What happened?

**Heidi Linnakangas:** I'm not sure what's happened. I think Postgres has just matured. People used to ask "Why Postgres, and why not MySQL, or something else?", but I don't really hear that anymore. It's the default now.

**Adam Staravia:** Do you think it could be somewhat technical, and then also somewhat drama-related? There's been a lot of drama in the MySQL space, hasn't there? Like with being open source--

**Jerold Santo:** Licensing, and acquisitions...

**Adam Staravia:** ...and really be shifting... This drama behind the scenes to sort of like make it not very community-friendly... Postgres is also very good technically. I wonder if that's also a reason to be like "Don't go there."

**Heidi Linnakangas:** I'm sure it's a factor. Postgres has always had a slightly different community that many other open source projects; it's truly community-driven and not like owned by any single company.

**Jerold Santo:** Yeah.

**Heidi Linnakangas:** So that's different. I think that has helped to keep it alive for a long time. You can't acquire Postgres.

**Jerold Santo:** That being said, that community is aging. I'm not sure -- you may have seen James Governor's recent posts on Redmond about the aging Postgres community, and how do we actually transition...

**Heidi Linnakangas:** Sure.

**Jerold Santo:** Like, where do we go from there.

**Heidi Linnakangas:** Yeah. There's always new people coming, but it's right. I mean, the core people who have been added for a long time are definitely aging. None of us is getting any younger.

**Jerold Santo:** Right.

**Adam Staravia:** Can you summarize some of that, Jerold?

**Jerold Santo:** Well, just if you look at the core contributors to Postgres, generally speaking they're men in their 50s. They're in the fourth quarter of their careers, at least; maybe they would argue that, but they're not in the kickoff stage of a career...

**Adam Staravia:** Or halftime...

**Jerold Santo:** Or halftime. I would argue fourth quarter. Maybe they say third quarter. Regardless, they're getting on the older age of the spectrum, and they're like "What happens to the project as those very key players retire, move on, lose interest?"

**Heidi Linnakangas:** It's not dominated by any one person, though. So there's a lot of people working on it. And if you look at the wider ecosystem, there are a lot of extensions, and there's a lot of stuff happening around Postgres, and there's young people there.

**Jerold Santo:** Yeah.

**Heidi Linnakangas:** \[08:06\] So there's a lot of potential if you can draw them in to become more active on Postgres itself.

**Jerold Santo:** Well, Neon - I mean, you and your team... I'm not sure your age, but there's fresh -- we'll call it fresh blood in the ecosystem. Like, here's a brand-new startup, relatively - a couple of years old - contributing, building extensions etc.

**Heidi Linnakangas:** For sure. And putting my community hat on, that's one reason why I'm excited to work for Neon. I hope I can actually make a difference on that, and bring some new blood to the community as well through the company.

**Jerold Santo:** So you were a Postgres guy before Neon?

**Heidi Linnakangas:** Yeah, I've been a Postgres guy; since 2006 I've been working full-time on Postgres.

**Jerold Santo:** Okay, a long time.

**Heidi Linnakangas:** For different companies.

**Jerold Santo:** Very cool.

**Adam Staravia:** How did you know it was the right choice? What was your criteria for choosing?

**Heidi Linnakangas:** For Postgres? Well, I've never really used Postgres, so my background is that I was working on a systems integrator, and I had some free time on my hands... So I've always been a programmer, I've always been doing stuff, and I'm a big fan of the relational model once I got introduced to SQL, and that... So I had some free time, I was on paternity leave with my daughter, and she was a good sleeper, so I was looking around for projects to contribute to, or if there was something in the open source world I could do. So I started looking at databases. I looked at MySQL code, I looked at Postgres, I think I looked at some others... But Postgres was the one that was easy to read, and easy to -- it was a pleasure to kind of read through, and understand, and learn more. So I stuck with that.

**Jerold Santo:** One thing we heard yesterday from an All Things Open attendee is that back in June of this year, I believe, on the Postgres mailing list you proposed - or maybe not proposed, but brought up something that's probably been stirring for a little while... He called it like the most significant change to Postgres, if it lands or if it happens, in a long time. Do you want to tell us about that?

**Heidi Linnakangas:** You must be talking about the multi-threading -- changing to multi-threading architecture?

**Jerold Santo:** Yes.

**Heidi Linnakangas:** So yeah, that came up in a conversation in Pocono at the end of May, with some other hackers. We were talking about some features, and like "Wouldn't it be easier if we had a multithreaded architecture?" So what I ended up -- I kind of summarized the discussions... Because it seems like there's a rough consensus that if we had multithreaded architecture, it would be better at this point. But there's a lot of history, of course. It's not an easy change to go from multi-process architecture to multithreaded.

**Jerold Santo:** Yeah. Can you explain the foundational difference between multi-process and multithreaded?

**Heidi Linnakangas:** Right. So the key difference between multi-process and multithreaded architecture is that when a new connection comes in, Postgres launches a new process to handle that connection. In a multithreaded architecture you would only launch a new thread. And the difference between a process and a thread is basically that threads also share the same address space in the process, whereas with processes, each process has its own address space. And that makes a difference in how easily you can share data, or share data structures between the connections. So a multithreaded architecture would it make it a lot easier to resize things like buffer cache, a lot of other caches that are currently not shared across the connections in Postgres, that would make it easier to share them.

**Jerold Santo:** Right.

**Adam Staravia:** Does that change the CPU utilization as well?

**Heidi Linnakangas:** It might, yeah --

**Adam Staravia:** I mean, if I looked at top, would I just see, like, when Postgres is being pinged, just like one line, or if I had eight cores, all eight cores lit up?

**Heidi Linnakangas:** Yeah, so multi-threading wouldn't directly do that. Just by switching to multithreaded we wouldn't get that. Postgres kind of already utilized multiple cores by launching multiple processes to process one query.

**Jerold Santo:** Right.

**Heidi Linnakangas:** But when that parallel query was implemented a few years ago, that was actually -- a lot of effort went into working around the fact that we did some multi-process architecture. So you actually had to build an infrastructure to share the data between the processes... Which would be a lot simpler in a multithreaded architecture. So I think we could probably do more. It would probably speed up the development of parallel query as well, although that would be separate projects to do that...

**Adam Staravia:** \[12:09\] That's another mailing list post.

**Heidi Linnakangas:** Yeah.

**Adam Staravia:** So the summarization...

**Jerold Santo:** Multi-threaded software has specific requirements in order for it to be thread-safe, right?

**Heidi Linnakangas:** Yeah, sure. That used to be a problem 20 years ago, when this was probably the first time discussed... I think if you look back at the '95 or '96 discussions - and I think I've seen some comments saying "Well, Postgres is multi-process now, but maybe it will switch to multithreaded later", and that was like 25 years ago...

**Jerold Santo:** \[laughs\] Right.

**Heidi Linnakangas:** What was the question?

**Jerold Santo:** Well, I didn't quite get there, but here it is... If you are assuming multiprocess for all these years, these 25 years, and not thinking multithreaded, I imagine it's not an insignificant change to the software.

**Heidi Linnakangas:** Oh, sure. Yeah. So thread-safety - that used to be a big deal a long time ago... But nowadays, libraries -- I mean, most software, when people are writing software now, they would start with a multithreaded architecture. So that's not really a problem anymore. Like, all the libraries are multithreaded, or multi-thread-safe; they're all thread-safe versions of everything. So that was a good argument, or would have been a problem 20 years ago; not really a problem anymore. But of course, switching - all the existing code needs to be adopted somehow.

**Jerold Santo:** Yeah, exactly.

**Heidi Linnakangas:** So that is a problem. And that's the hard part of all of this, really - changing Postgres itself, but \[unintelligible 00:13:29.08\] the whole ecosystem to be thread-safe. Most of it probably already would be, but how do you know? How do you tell?

**Jerold Santo:** Exactly.

**Heidi Linnakangas:** So that's going to be the hard part in this, to figure out how do you detect the cases where something is not thread-safe?

**Jerold Santo:** I mean, it seems like this feature is an excellent case study in how a large change to an open source multi-organization-teamed core team introduces an idea, agrees on the idea, the governance involved, and then the actual work, who does it, how does it get divvied out, and then how does it actually land, and transition... Isn't that a really complicated beast?

**Heidi Linnakangas:** Yes, it is.

**Jerold Santo:** How does it work?

**Heidi Linnakangas:** We'll see how it ends up... \[laughter\] Postgres doesn't have like a very -- there's no voting system... It's actually hard to even make decisions like that, because it's not well-defined how would you do that. The rough idea is that you try to find consensus, and if someone very strongly disagrees, then we work through those disagreements. But yeah, it can be hard to pull off big changes like that. But at the end of the day, the first thing that needs to happen is someone actually needs to do all the work to show this is worthwhile.

**Adam Staravia:** \[unintelligible 00:14:44.10\] because you got the idea out there... Is there any code -- or are you asking for consensus, and then the work? What's the stage of this idea?

**Heidi Linnakangas:** It's just an idea at the moment. I spend a few hours, days maybe, thinking about it, and writing some very preliminary stuff that -- some small changes that we should make anyway just to clean up the code. But no, there's no real concerted effort yet. Yeah, that's going to be a lot of work. I mean, the first thing to do is -- and what I wanted to do with posting in June was to make sure that I'm not missing some... That I actually understood \[unintelligible 00:15:20.12\] that there is consensus, that this would be a good thing if we had it, and that there is no strong objections from any of the core people on that. Otherwise, it would be pointless to spend any time on it. But the next step really needs to be done to actually start to write some code to do that. I don't know if I'm going to do that. Maybe. Or maybe I'll have to do it together with the team.

**Jerold Santo:** Sure. Is that something that would be beneficial for Neon? I imagine it would be...

**Heidi Linnakangas:** It would be.

**Jerold Santo:** Any that Neon would be willing to fund the development of.

**Heidi Linnakangas:** Yeah. I think we -- yeah. So it would benefit Neon, because we do all the scaling, and that becomes easier in a multithreaded architecture, because that makes it easier to resize some of the \[unintelligible 00:16:03.20\] it makes it easier to share some of those caches. Kind of the same problems that everyone has; it would benefit everyone. But yeah, for Neon, that would really help with all the scaling part.

**Jerold Santo:** \[16:14\] Gotcha. When we had Nikita on the show, probably 18 months ago roughly --

**Adam Staravia:** Exactly this time last year.

**Jerold Santo:** Oh, was it?

**Adam Staravia:** I think so.

**Jerold Santo:** Okay, a year ago. He mentioned three or four patches that Neon adds to Postgres to customize for your guy's needs, and how they were trying to upstream those... He wasn't sure if that was ever going to happen, but he thought, you know, good chance, but takes time etc. Any update on upstream contributions from your team?

**Heidi Linnakangas:** Yeah, so those patches are still out there. Not much has happened, unfortunately. The biggest \[unintelligible 00:16:43.06\] we have is to do what's called the Storage Manager API in Postgres... Which isn't really an API, because there hasn't really been any other implementations in the past 20 years. So that patch is still out there to make that more pluggable, but there has been no progress.

So with the Postgres community, and I'm sure other communities have the same problem, it's hard to sometimes get the attention to these things; if no one else is really feeling the pain, there isn't much happening. Although on that there have been a lot of good discussions, and some other ideas people could do with those patches and those APIs... But yeah, nothing has been committed yet.

**Adam Staravia:** The patches are essentially the way it writes to disk; instead of writing to the disk, it writes distributed?

**Heidi Linnakangas:** Yeah. So Neon plugs in at a very low level. So whenever Postgres would read a page, an eight kilobyte page from disk, we get it at that point. So you read it from elsewhere, like from our storage system. So yeah, having an extension point there in Postgres would help to eliminate those patches.

**Adam Staravia:** That sounds like your competitive advantage though, Neon's competitive advantage. If that patch goes into open source, does that become a threat?

**Heidi Linnakangas:** Well, it's already out there, open source. Anyone can already start and use it.

**Adam Staravia:** Yes, I suppose. That's true.

**Heidi Linnakangas:** And Neon lives and dies with Postgres. We care about the community.

**Adam Staravia:** Right, okay. That's what I was trying to get to. If this can be used by the enemy, let's just say - is that a bad thing?

**Heidi Linnakangas:** You know, I made peace with that thought a long time ago, when I started to work on Postgres. It's a liberal license, people can take it and do whatever they like with it...

**Adam Staravia:** I think it speaks to the company, though; it speaks to the DNA and the outlook of the company, which is why I asked that...

**Heidi Linnakangas:** Yeah, sure.

**Adam Staravia:** It's like, do people see Neon as a player, a safe player, I don't know, a nice player in the Postgres world? Or are you trying to build a proprietary moat?

**Heidi Linnakangas:** I sure hope people see \[unintelligible 00:18:29.19\]

**Adam Staravia:** Okay. That's a better word, friendly.

**Heidi Linnakangas:** We want to partner with everyone, and we like to make friends.

**Adam Staravia:** Right.

**Jerold Santo:** So you're waiting on those particular patches; who knows...? Postgres as a project - you say you live and die with it... It seems like through its history it's had times when it's "fallen behind" with features... And other people pop up and say "Look at these -- NoSQL, for instance. Look what we can do with JSON." And then eventually, Postgres was like "Well, we added all the JSON things, and now we can also do that." What's next in that line? What are you seeing out there, or maybe what you guys are building, where it's like Postgres can't do that, but people are doing it, and now it's going to have to catch up at some point?

**Heidi Linnakangas:** Um, that's a good question. I mean, putting my Neon hat on, there's the storage related stuff that we are doing, separation of compute and storage... Although that is out there in the open source, so people could take it and run with it. I don't know if that will fully take over the world, or if that will stay to be something that we do; we'll see. But there are competitors doing similar architectures as well.

Then there's all the exciting stuff happening with pg vector, for example; the vector service. That's a hot topic. But I think that is like -- I think Postgres is actually doing pretty well there. Pg vector is popular, and it keeps improving at its own pace, and that's all good. It's a similar thing with PostGIS. Postgres is pretty dominant in \[unintelligible 00:19:56.23\] world with that.

**Jerold Santo:** Yeah, geospatial stuff. Good point. Are those things that, when using Neon -- are those things that are pre-integrated for you as a user of a Neon database? Or is it like click a box, get pg vector? How does it work with plugins?

**Heidi Linnakangas:** \[20:14\] Yeah, we provide those extensions. You create the extension, and you get it.

**Jerold Santo:** So you have full Postgres access, and you're just doing your thing, huh?

**Heidi Linnakangas:** Yup.

**Jerold Santo:** Okay. So geo-distributed Postgres around the world. Let's talk about that.

**Heidi Linnakangas:** Okay.

**Jerold Santo:** Can you do that?

**Heidi Linnakangas:** No, we don't do that at the moment... \[laughter\] We've been thinking of that. We have a lot of good ideas, but we've not implemented --

**Jerold Santo:** I know you do. I remember asking Nikita about that as well. I'd love to hear from your mind - what are some ideas around this?

**Heidi Linnakangas:** So what you could do... First, you can run read-only replicas in different regions...

**Jerold Santo:** Sure.

**Heidi Linnakangas:** That's kind of the first step, easy step. With Neon, we could also run the storage in different regions, and do kind of the replication at the lower level...

**Jerold Santo:** Okay.

**Heidi Linnakangas:** We have no plans for multi-master or multiple-writer systems; there are other projects trying to do that. But that's always a hard problem, and it introduces a whole new set of problems... So we're not going there at the moment.

**Jerold Santo:** Yeah. You've got to kind of break the CAP theorem to do that, and people are claiming it's possible... Is there a real demand for that, or is it just something that people like me like to talk about and ask about?

**Heidi Linnakangas:** I don't know, I haven't really seen very -- we don't hear a lot of people requesting that, let's put it that way. People talk about it, people ask about it, but not in a serious way. I don't think we've lost any customers because we don't have it.

**Adam Staravia:** Given Neon today, what is the current architecture? If you're not geodistributed, what is the architecture? When you deploy Neon, what is the benefits of using it? Why do people choose Neon for -- you know, you don't write to this, you write to disk, you write to distribute that? How does that actually play out? What's the architecture?

**Heidi Linnakangas:** So the core of the architecture is the separation of compute and storage. And then we have a control plane that kind of manages these Postgres instances and VMs. And there's a proxy, there are some moving pieces... But the big differentiator that we get with that architecture is it's serverless. So what we mean by that is that we actually shut down Postgres if you're not using it. So that's perfect if you're a developer, and you don't need to worry about forgetting to shut it down, in a nutshell.

**Adam Staravia:** Right.

**Heidi Linnakangas:** The other thing that the storage system can do is the branching, and it kind of replaces traditional backups and \[22:23\] archive. So you can do point in time query, you can easily spin up a new Postgres instance against an older point in time, start running queries against that, stuff like that... And the branching is something that is kind of unique, and we hear a lot of good things about that; people like that. If you're a developer, you want to create a branch of your development database, or even your production database, and do your changes, run your PR against that... And when you're done, you can forget about it, or you can refresh that.

**Adam Staravia:** Right. You said storage system. Is that like a different term, that sits above the database? So Neon is the storage system, and then there's the database... Give me an idea what you mean when you say storage system.

**Heidi Linnakangas:** So we wrote a completely new server software that runs below Postgres, and it deals with those eight kilobyte pages, and it understands the Postgres write-ahead log format, the transaction logs, and parses that... So whenever Postgres needs to read a page, it goes and fetches the page from the storage system instead, and there's an interface for that. So that's different from just running Postgres on a remote volume, because it actually understands about the Postgres disk format, and it can do this branching, it can do the copy on write stuff underneath that.

**Adam Staravia:** Gotcha.

**Jerold Santo:** What else is exciting to you right now in the world of Postgres, or even beyond?

**Heidi Linnakangas:** Well, I mentioned pg vector already. I think that's an exciting thing; people are doing a lot of exciting stuff with that. In the Postgres world there's stuff happening with asynchronous IO, from colleagues at Microsoft; they're doing work on that. I think that will improve the IO speed, and that's perfect for Neon as well, because we've separated \[unintelligible 00:24:03.03\] that actually helps us a lot. So I'm hoping to spend personally some time reviewing those patches to see them go in.

**Jerold Santo:** Cool.

**Adam Staravia:** I love it.

**Jerold Santo:** Yeah. Thanks for talking with us, man.

**Adam Staravia:** Neon's awesome. Thank you.

**Jerold Santo:** Appreciate it.

**Heidi Linnakangas:** Thank you.

**Break:** \[24:20\]

**Jerold Santo:** Are we started yet?

**Adam Staravia:** This is the show, man.

**Jerold Santo:** Alright. We're here with Robert al-Khalil.

**Robert al-Khalil:** Hello, hello.

**Jerold Santo:** His second appearance on the Changelog.

**Adam Staravia:** Apparently...

**Robert al-Khalil:** Allegedly.

**Adam Staravia:** Allegedly, sorry. That's a better word. Apparently also works...

**Jerold Santo:** So according to you... And with some verifiable memory of mine, we talked to you at OSCAN probably 2018...

**Adam Staravia:** 2017.

**Jerold Santo:** 2017 maybe...

**Robert al-Khalil:** I would say 2019, yeah.

**Jerold Santo:** Okay. And we talked about WebAssembly.

**Robert al-Khalil:** We did.

**Adam Staravia:** Was this in Europe? Was it in Europe?

**Robert al-Khalil:** No, no. It was in Portland?

**Jerold Santo:** It was in Portland. You were there. I went to OSCAN London one time, by myself...

**Adam Staravia:** 2018 is when that was.

**Jerold Santo:** Okay. Was WebAssembly a thing then?

**Adam Staravia:** Yeah, it was.

**Robert al-Khalil:** Yeah. It was a thing.

**Jerold Santo:** It must have been, because you were into it...

**Robert al-Khalil:** Not as much a thing as it is now...

**Adam Staravia:** Okay, this is sparking a memory, okay?

**Jerold Santo:** Is it?

**Adam Staravia:** Yeah...

**Jerold Santo:** Well, backstory for you, Adam, is he walked by earlier and we both kind of locked eyes... And I was like "Do I know you?" and he was like "Do I know you, or something?" And then he's like "Yeah, I think you had --" And I was like "I have no memory of this."

**Adam Staravia:** I said the same thing. I'm like "I know this guy."

**Robert al-Khalil:** I have a memorable face.

**Adam Staravia:** So Jerold and I went to an OSCAN together in Austin, I want to say, right?

**Jerold Santo:** Probably...

**Adam Staravia:** 2017...

**Jerold Santo:** Portland in 2018.

**Adam Staravia:** Portland 2018.

**Jerold Santo:** That's probably where we've met.

**Robert al-Khalil:** Ah, yes.

**Adam Staravia:** And then we haven't been there since, because it stopped.

**Robert al-Khalil:** Yeah.

**Adam Staravia:** So that's why I thought the only OSCAN we had been to was in Austin. So in my memory until this moment \[unintelligible 00:30:11.27\] now inserted one brand new OSCAN in my life which I went to.

**Jerold Santo:** I definitely went to Portland in 2019, in the summer, for sure. So... Yeah, because I took my daughter and my mom to be with family... And that was OSCAN, so...

**Adam Staravia:** Okay, maybe it was 2019 then.

**Jerold Santo:** Anyway...

**Adam Staravia:** Either way.

**Jerold Santo:** Neither here, nor there.

**Adam Staravia:** History has been painted...

**Jerold Santo:** Robert was there...

**Adam Staravia:** He's probably correct, and we're probably wrong.

**Jerold Santo:** He was into WebAssembly, he was into bio informatics...

**Robert al-Khalil:** Yes, I am.

**Jerold Santo:** You're still into both of these things...

**Robert al-Khalil:** Surprisingly, yes.

**Jerold Santo:** And I don't know what we talked about then specifically, but one thing that is interesting to me about WebAssembly is how much promise it has, but how little in my purview, practical use it has, beyond tinkerers or people with very specific needs. So just curious your perspective on that.

**Robert al-Khalil:** Yeah, I think I generally agree with that. I think people who think that WebAssembly is going to be used everywhere are just wrong. It's just not what it's meant for. It's a very heavy-duty tool. Like, if you have needs for running compute-intensive workloads in the browser, like Figma, and Photoshop, Google Earth - or bioinformatics, I should add - all those are great applications for WebAssembly. Because for the first time, you can take code that's not written in JavaScript and bring it to the browser. But if you're building your typical web application that doesn't have any sort of compute, any sort of processing audio/visual, then you probably don't need it. That's kind of my view on it.

**Jerold Santo:** Okay. What about these people that are taking it server-side? There's a lot of talk about that as well. I mean, do you dip into that area at all?

**Robert al-Khalil:** \[31:54\] A little bit. So there is a lot of excitement about that. I don't share that excitement... Because here's the thing - when you're running WebAssembly in the browser, it lets you do something that was previously impossible; you just couldn't take a C program and run it in the browser... Except maybe asm.js. But that was kind of a precursor. It lets you do things like SIMD. That's also impossible with just JavaScript. But once you leave the browser, you can do whatever you want. So WebAssembly is one extra alternative to the other hundred you have.

So from that angle, there are a few use cases that I think are pretty valuable for WebAssembly on the server. Maybe you want to extend your application, let's say, with plugins, and you want to let users write whatever code they want, and you want to execute that securely... WebAssembly is a good sandbox for that. But then, again, you're not going to reimplement that yourself, you're going to use some other tool that maybe under the hood uses WebAssembly to solve that problem.

**Jerold Santo:** Okay. What kind of stuff are you doing?

**Robert al-Khalil:** So I'm doing mostly web stuff. So bringing bioinformatics tools to the web, for either building applications that analyze data in the browser, so that you don't have to figure out bioinformatics dependencies, which are kind of a mess... If you want to keep your data private, it's kind of a local-only type workflow.

The other thing I'm really interested in is something I'm talking about tomorrow, is using WebAssembly to power interactive tutorials for command line tools... So that you can -- you know, instead of when a student logs into your website, you spin up a container for them. That's super-expensive. You could run these tools in the browser, give them a similar experience, and much, much cheaper for you to host.

**Adam Staravia:** What should we know about bioinformatics that makes sense to us? What exactly is bioinformatics?

**Robert al-Khalil:** Oh, that's a good place --

**Adam Staravia:** Can you say that three times fast?

**Robert al-Khalil:** Bioinformatics, bioinformatics, bioinformatics.

**Jerold Santo:** That was not fast enough.

**Adam Staravia:** I was going to say, there was a pause in there.

**Jerold Santo:** "I'll say it three times slowly..." \[laughter\]

**Adam Staravia:** Please explain.

**Robert al-Khalil:** So bioinformatics is using computer science and software engineering to analyze biological data.

**Adam Staravia:** Okay. Like DNA.

**Robert al-Khalil:** Yes, exactly. So for example, if you're interested in knowing, I don't know which diseases you might be at risk for, you could take a blood draw, isolate the DNA, sequence it, figure out what all the letters are, and compare those to a reference, and figure out what's different there, and has that been associated in the past with some disease, or something like that.

**Adam Staravia:** Right.

**Robert al-Khalil:** And so the process of figuring that out, the algorithms and the software around that is basically bioinformatics.

**Adam Staravia:** So what does it take to take this kind of applications that are like probably behind a desktop application, right? They're probably written in C, or for a desktop environment, and you want to take those kinds of applications to the web, to essentially open it up where you can just go to any platform: Linux, Mac, Windows... Is that the reason why?

**Robert al-Khalil:** Yeah, yeah. One example is - I have this website called fastq.bio. So it takes in some data that you get out of an instrument, and runs some really quick data analysis to tell you how good of a quality the data is... And it runs in the browser, because that's just super-convenient. People drag and drop their files, and they're done. They don't have to figure out how to install it, how to set it up, and all that stuff. So that's one use case. You wouldn't necessarily do super-heavy duty analysis, because it's still the browser; you're kind of limited by what the user has. But it's a nice way to cover a ton of use cases that previously were not covered.

**Adam Staravia:** \[35:56\] And you specialize in the WASM world, in bioinformatics, in particular. That's where your usage of WASM is, in that silo.

**Robert al-Khalil:** Yeah, that's right.

**Adam Staravia:** Okay.

**Robert al-Khalil:** So I have a tool called Biomass...

**Adam Staravia:** Biomass?

**Robert al-Khalil:** Yes.

**Adam Staravia:** That's really cool.

**Robert al-Khalil:** Can you say Biomass three times --

**Adam Staravia:** Biomass, Biomass, Biomass...

**Jerold Santo:** Much easier.

**Robert al-Khalil:** That's true. Speaking of which, how do you guys pronounce WASM? Is it WASM, or WASM?

**Jerold Santo:** Well, I call it WASM. But I'm open to either direction.

**Adam Staravia:** I don't even understand why I call it WASM, but I do call it WASM. It's WebAssembly... Wasm...

**Jerold Santo:** One time I called it WASM, because I wanted it to rhyme with awesome... But that was just a means to an end.

**Adam Staravia:** That's so awesome...

**Robert al-Khalil:** Right. Right.

**Jerold Santo:** But I do call it WASM, and I'm not sure why.

**Adam Staravia:** I don't know either. I think we may have been on a podcast with somebody who seemed to be more knowledgeable than we were, and called it WASM, and so we kept going there with him.

**Jerold Santo:** That's true. Although it didn't work for Richard Hip. I mean, I still call it SQLite...

**Adam Staravia:** SQ-a-Lite.

**Jerold Santo:** And he's definitely more knowledgeable than I am about the project...

**Adam Staravia:** Yeah.

**Jerold Santo:** So yeah, I'll stick with WASM until I'm convinced otherwise.

**Robert al-Khalil:** Sounds good to me.

**Adam Staravia:** And what do you call it?

**Robert al-Khalil:** I call it WASM...

**Adam Staravia:** And so why do you call it WASM?

**Jerold Santo:** Because we did.

**Robert al-Khalil:** I don't know. \[laughter\]

**Adam Staravia:** Nobody knows...!

**Jerold Santo:** Well, that's the thing, sometimes just the first way you hear it is just how you do it.

**Robert al-Khalil:** Right.

**Jerold Santo:** What's a weird phenomenon in computer science and podcasting - or real-life conversing - is a lot of times with a term, or an acronym, or whatever it is...

**Adam Staravia:** You've never pronounced it.

**Jerold Santo:** We'll read it for years... But we'll all read it to ourselves for years, and we've never actually had to say it to somebody else. And then you have that moment of "How do I say this? I've been reading it for years, writing it for years..." And it's a weird moment that we all experience...

**Adam Staravia:** That's right.

**Jerold Santo:** And maybe we just had that with WASM.

**Adam Staravia:** Okay.

**Jerold Santo:** But I'm glad that we're all on the same page.

**Adam Staravia:** That is good. We have consensus.

**Robert al-Khalil:** Excellent.

**Jerold Santo:** Although on our show recently Christina Warren did say "Yes, I call it GIF", and then she just continued to talk as if we shouldn't stop the world and discuss... Do you remember that?

**Adam Staravia:** Well, she's here. We can get her on the mics again.

**Jerold Santo:** Christina's here?

**Adam Staravia:** Yeah, I saw her downstairs.

**Jerold Santo:** Alright. We'll have to get her on the mic.

**Adam Staravia:** Hey listen, our listeners, aka Jerold, listened to this part of the show and was upset, because we didn't get that beef about GIF vs. GIF.

**Jerold Santo:** I was upset at the moment, but she talks too fast, so I just let it go.

**Adam Staravia:** I thought it was an appropriate amount of speaking cadence, but... I will agree. I missed that argument.

**Jerold Santo:** Alright. Let's get back to --

**Adam Staravia:** We had better things to cover though.

**Jerold Santo:** We did. \[unintelligible 00:38:26.29\] We also have better things to cover right now.

**Adam Staravia:** Yeah, we do. We're sidetracked. Okay, so bioinformatics, taking applications that are for the desktop, to the web... What kind of applications make the most sense? You mentioned this one where it sort of does like data analysis... What does the web need? What does the user base need of the web that can use these kinds of tools, in specific to what you know, and then just in general for what WASM can actually do?

**Robert al-Khalil:** Yeah, so I think it's pretty similar across the board, I think, for bio. Tools that do some sort of preview of an analysis are really useful. Some analyses are just tiny, too. Like, if you're analyzing, let's say, the genome of viruses, they're pretty tiny, so you could actually just run the whole thing in the browser. And so that gives you both the advantages of not having to install the tools, and to do it in a privacy-conscious way. In terms of more broadly outside bio - because you have audiences that aren't biologists, is that right?

**Jerold Santo:** That are what?

**Robert al-Khalil:** That are not biologists.

**Jerold Santo:** We haven't surveyed them recently, but I think that's fair.

**Robert al-Khalil:** Okay. \[laughter\]

**Adam Staravia:** I would say we've got at least one...

**Robert al-Khalil:** Okay. \[laughs\] That's good. I guess there are a few categories. If you have a tool that you already have in another language, and you really want to bring it to the web, and you don't want to rewrite it all in JavaScript, I think that's a great use case.

**Jerold Santo:** Yeah.

**Robert al-Khalil:** \[39:56\] If you have a slow application that has portions of it that are really heavy JavaScript compute, in some cases - this is something that also tends to be overplayed. This not always happens, but you can get performance improvements by switching it off with WebAssembly. But you can also get worse performance. And yeah, that's kind of the couple of applications that I think are pretty relevant.

**Adam Staravia:** Describe worse performance. Because sometimes access is enough, and I'll wait, because maybe with the web it's easier. And I can't install it on my system, or I can't, because literally I can't install the application. But I can browse the web, and I can authenticate on the web.

**Robert al-Khalil:** Yeah. So one big thing that I've noticed is that when you have a WebAssembly module, and it needs to communicate a lot back and forth with the JavaScript world, that is super-expensive. So if ideally your module takes in a little amount of data, does a bunch of stuff and returns small amounts of data, but if you're constantly returning large trunks, that's because WebAssembly only understands numbers. So if you pass in strings, it converts to a number; you pass in an object, it converts to a number.

**Adam Staravia:** Do you know the conversion, by any chance? Like, if I said the word "the", what number is that, to WASM?

**Robert al-Khalil:** Oh, of course. It's 86,12 -- no, I'm kidding. \[laughter\]

**Adam Staravia:** It'd be cool if you knew...

**Robert al-Khalil:** It would...

**Jerold Santo:** It would... You could have kept going, we totally bought it.

**Adam Staravia:** I would have been spooked. I would have been like "Oh, my gosh!" Well, that's cool; numbers only.

**Jerold Santo:** Numbers only. So that translation layer in between is expensive...

**Robert al-Khalil:** Yeah. And so that's actually one way in which you can try to optimize the performance, is if you switch off some JavaScript with WebAssembly, you can try to trim that down in order to speed it up.

**Jerold Santo:** Yeah, it makes sense. Back to your current interest of CLI tutorials in the browser...

**Robert al-Khalil:** Yeah.

**Jerold Santo:** Are you giving people full-fledged Linux environments in the browser? Or how does it work?

**Robert al-Khalil:** Not yet. So right now, in the v1, every tool I have to compile to WebAssembly, and then I have this sort of Xterm.js; it simulates a console... And I kind of hook those up together. In the future, what I'm going to do is actually switch that up with a full-blown Linux OS in the browser; that's going to be a little slower, but it's going to be worth it for getting some things on there that are otherwise hard to do just by directly compiling. And this is using an open source project called v86. So they wrote essentially a CPU emulator in Rust. And so they compiled that to WebAssembly, and that's kind of how they emulate the whole operating system. And it boots up, there's a BIOS, there's everything. It's pretty wild.

**Adam Staravia:** That'd be kind of cool, man. Can you simulate any BIOS, or just a particular BIOS?

**Robert al-Khalil:** I honestly don't know what a BIOS does...

**Adam Staravia:** Okay... Well, I don't either.

**Jerold Santo:** It's a basic input/output system... \[laughter\]

**Adam Staravia:** Except for I know how to get there; in most cases Delete-Delete-Delete, or maybe one of the F's... It could be an F11, it could be an F10, who knows...

**Jerold Santo:** Just hit all the F's till you find it...

**Adam Staravia:** \[unintelligible 00:43:18.25\] "Which was it, Delete? Gosh, I missed it!" You know, it's like, "Boot it up already!" Well, I think of that because if you can emulate those things, you can kind of give somebody a playground to configure hardware, or to configure a BIOS, or whatever it might be to be like "Okay, this is how you change the boot order. This is how you set these two NVMe drives to be the boot." Or to the USB, or whatever it might be. Or this is how you set up virtualization in this particular Intel CPU, for example. Those are the kinds of things that you kind of have to have the hardware to learn; until you have the hardware, you can't learn it. And then you're kind of by yourself... You know what I mean? If you could do it in an environment like that, there could be interactivity, because you're emulating it, you know?

**Robert al-Khalil:** \[44:00\] I love this. Yeah. I was mostly thinking, like, once you're logged in, past boot time... But yeah, this is an interesting use case for it.

**Adam Staravia:** Yeah, as a black box. I mean, you go to the forums, you'll find zillions - and I don't mean like literally zillions, but quite a lot - of people saying "How do you do this with this BIOS?", or whatever. All the BIOS out there. And you've got somebody showing screenshots... That's cavemen knocking rocks together, trying to make fire.

**Robert al-Khalil:** \[laughs\] Yeah, true.

**Adam Staravia:** You can have this emulator, and be like "This is how it works."

**Robert al-Khalil:** That would be amazing. I'll send you a link when it's ready.

**Adam Staravia:** And you don't have to have the hardware. It's just \[unintelligible 00:44:30.07\] in the browser to play with.

**Robert al-Khalil:** Yeah.

**Jerold Santo:** So once you're logged in, how leaky is the abstraction right now? ...meaning, like -- maybe you know what I mean.

**Robert al-Khalil:** I do not know. \[laughs\]

**Adam Staravia:** What do you mean by leaky abstraction? I'm just kidding.

**Jerold Santo:** What I mean is -- so for instance, a lot of text editors have vim mode. Most vim users will use vim mode for about 7 to 12 minutes and be like "This is not vim. I can see all the places where this is clearly not vim." Leaky abstraction is not the right term, I just overuse that term. Yeah, your emulation ends -- maybe we call it the uncanny valley of what you're actually trying to emulate, where it's like "Yeah, this is not good enough."

**Robert al-Khalil:** Yeah... So if you're using SIMD instructions that are too fancy, that won't be supported. If you're doing multi-threading, the emulator doesn't really support that, so you'll just have to stick to one thread. Those are kind of the big ones. You're also just limited by how much RAM you can use in the browser. And also, more realistic limitations... Like, if you're trying to run some Java program - I tried this recently... It works, but it takes a few minutes.

**Jerold Santo:** Yeah, it's just slow.

**Robert al-Khalil:** So it's not practical in that case.

**Jerold Santo:** Right. Kind of the 80/20 rule...

**Robert al-Khalil:** Yeah.

**Jerold Santo:** Okay. How big of a performance hit, boot up time - or load time, let's just call it that - will it be to switch to this full Linux environment? And is anybody else doing this currently, like, loading Linux completely in the browser?

**Robert al-Khalil:** Yeah, so there are projects that are using it... I am not aware of people building tutorial sites with it, which is a shame, because it's a really powerful tool. Most tutorial platforms I'm aware of tend to do the whole "We'll spin up a container, shut it down after a while", which is super-expensive.

**Jerold Santo:** Expensive for them to run, for the users?

**Robert al-Khalil:** Yeah, yeah. Typically, what you'll see is they'll start "Hey, we have a free tier." They'll be like "Hey, maybe you can use it for a few hours." And then it turns into "There's no free tier, because we can't support this."

**Jerold Santo:** Yeah, they can't support it long-term. It makes sense.

**Adam Staravia:** Well, think about Debian. Debian just released a new version, and I believe the installation process changed enough to be talked about. So it'd be cool to emulate for Debian, when they launch, like "Here's how the new installation process works. Here are the screens that have changed if you're doing a unique disk set, and this is how you need to do rate, or whatever, or choose this or that, or choose ZFS, or whatever it may be. Then you can emulate it in the browser." This is like a great example, because you can see it before you actually have to install it. Or you can install it, but you have to have the hardware, and enough hardware to expend on a tutorial. Or at least be able to virtualize with, say, Proxmox. But maybe Proxmox can't support the latest Debian, which it can; I'm just saying, what if there's something there? If you emulate it, you can sort of just -- it's marketing, in a way. It's almost like "Here's how it works. And if you don't know how it works, this is how it works."

**Robert al-Khalil:** This sounds awesome.

**Adam Staravia:** You should do these things.

**Robert al-Khalil:** I want this.

**Jerold Santo:** Well, he's focused on bioinformatics, right? You're teaching specifically those kinds of tutorials.

**Robert al-Khalil:** For the most part, yes.

**Adam Staravia:** That's your plan with Xterm.js though, right? Didn't you say that?

**Robert al-Khalil:** Yeah.

**Jerold Santo:** Your platform is beyond, right? You can use those generally.

**Robert al-Khalil:** Yeah, you can use this for anything, really. Now, of course, I am going to add tutorials that are not bio-specific, like git, and grew, SED, AWK, all these things that I think everybody --

**Jerold Santo:** The basics. Yeah.

**Robert al-Khalil:** Yeah.

**Jerold Santo:** Core utils...

**Adam Staravia:** \[48:05\] So give an example of how these tutorials would work then. Let's say I have zero idea of how I would use AWK, or grew.

**Robert al-Khalil:** Yeah, so there's an AWK tutorial right now. You can go to sandbox.bio and click on the AWK tutorial. It basically shows you tutorial contents on the left... And it shows you some scenarios. Let's say you want to analyze a tab-separated file, and filter out rows that have a number greater than whatever in a column. So you can do these sorts of things. AWK, by the way, is a whole programming language, which is amazing... You can launch processes within it, you can write to files, you can -- it's quite deep. But yeah, so the tutorial has these sorts of examples, and then you have exercises. Some of them, I admit, are probably a bit too complicated. You're doing a bit too much math for AWK, but just to show you how powerful it is.

**Adam Staravia:** And you're working in like an emulated environment that is a terminal, with an emulated version of AWK.

**Robert al-Khalil:** That's right, yeah. It's using a new AWK version, I don't know, five point something.

**Jerold Santo:** How do you author these tutorials?

**Robert al-Khalil:** So some of them I've made up, some of them I worked with others who already wrote text-based tutorials, and we kind of bring them into this interactive place... And it kind of brings them to life.

**Jerold Santo:** Interactive place... Okay, describe this interactive place.

**Robert al-Khalil:** Oh, I just mean like --

**Jerold Santo:** Is it like the good place? The bad place?

**Robert al-Khalil:** It's a very good place. \[laughter\]

**Robert al-Khalil:** That could be the sequel. It's a very good place.

**Jerold Santo:** There you go.

**Robert al-Khalil:** But yeah, so basically, we just take the Markdown, put it into the sandbox.bio kind of template, and it uses a tool that I've already compiled to WebAssembly. We can just use it directly. If not, then we have to bang our heads against the wall, figure that out first, and then put it in.

**Adam Staravia:** We just had a conversation, too -- what was that conversation about, Jerold? Gosh... Cinema. Kind of similar to this, in a way... I mean, it's not tutorial, but it's recording what you did, so it's almost -- it's a playback...

**Jerold Santo:** Right.

**Adam Staravia:** ...in an emulation state. I mean, if you can rewind, and touch, and feel, and kind of delete, that'd be kind of cool, too. It's not quite the same, but it's got the similar fidelity. The fidelity is there. It's literally an example of what was recorded... And so this is probably an example of what could be real life. So they're very similar in that way. What am I trying to say, though?

**Robert al-Khalil:** What are you trying to say?

**Adam Staravia:** Oh, is embeddings, and like using this thing to -- is this something where... You said it's sandbox.bio?

**Robert al-Khalil:** Yes.

**Adam Staravia:** Okay, so that's the URL?

**Robert al-Khalil:** Yes.

**Adam Staravia:** Okay.

**Robert al-Khalil:** That's for the tutorial website.

**Adam Staravia:** So you're using this to show off tutorials that you want to show off, right?

**Robert al-Khalil:** Correct.

**Adam Staravia:** And can I author my own tutorials, and put them on there, or take them and do something... Like, how can I -- if I believe in what you believe with this thing, and I want to do my own things, I want to show off whatever...

**Robert al-Khalil:** Yeah, so we're not yet at the point where we can have an automated system where you can log in and create tutorials, but typically, the way it works is you email me "Hey..."

**Adam Staravia:** Okay. \[unintelligible 00:51:28.05\]

**Robert al-Khalil:** Yeah.

**Adam Staravia:** Okay.

**Jerold Santo:** Classic collab.

**Adam Staravia:** Could you fork the repo, or something like that?

**Robert al-Khalil:** Sure, yeah. If you want to just play with having Debian in the browser, you could also look at v86, which is what I'm using to emulate it, and you could run it on your own site; or if you want to embed it, or... All that's possible.

**Adam Staravia:** \[51:55\] Yeah. Well, I was actually thinking about this recently, and I just did this with screenshots. I did a fresh installation of -- because I've been messing with Ubuntu 22.04, or sorry, 23.04... And I got a redundant OS installation, I've got two discs, I've got a swap, I've got a boot, I've got root, and all that stuff like that... And so rather than just choosing one drive, I want to have the system be fully redundant by having two drives in mirror. And I like to show that off, either in written, but the only way I could do it really was like through screenshots, and then \[unintelligible 00:52:27.25\] those screenshots. Now, will I do a full emulation? It'd be kind of cool to have all that I already have, but then at the end, or somewhere else, a sidecar would be like "Here's literally the environment to go and do just that. You've got two discs, so when you get to that part, you can configure these discs, because you can follow my instructions." So rather than having to pull down a VM, or Proxmox, or actual \[unintelligible 00:52:50.09\] you take a USB stick and boot up into it and do the full thing yourself... It's accessibility to what's kind of trivial to some, redundant OS installation on Linux, but there are a lot of steps in there. There are a lot of steps in their in like choosing the partition, adding the partitions and giving them the paths, and stuff like that, and adding them... It's a mess, really. So I want to do the example through screenshots, but the best version of that really would be an interactive playground they could do... I mean, just follow the steps.

**Robert al-Khalil:** Yeah. I'd be curious to see if it works with all the configuration of like disks, and BIOS, and all that combination...

**Adam Staravia:** Well, if I were doing it, it would be the happy path. You would only have two disks... I mean, sure, you can go with one desk, but that's not why you're here. You're not here to configure one desk, you're here to configure two disks, in redundancy. And so it'd be the happy path of being able to configure Ubuntu, a new system, with two disks, with redundancy... And it would walk you through all that stuff.

**Robert al-Khalil:** Yeah.

**Adam Staravia:** That would be kind of cool, because you could literally see what you would see on your screen if you were in your home lab doing this, or in the environment you're in, doing this. And to me, that's empowering... Because now, every system I want to have this rock-solid, I'm going to use my own tutorial for my future self. "This is how you do it, Adam", you know what I mean?

**Robert al-Khalil:** Yeah, I think that would be a super-powerful use case for that.

**Jerold Santo:** I'm thinking like nix Craft tutorials... You know nix Craft?

**Adam Staravia:** Oh, yeah.

**Jerold Santo:** ...the website that we all find eventually whenever you're trying to --

**Adam Staravia:** Yes, when you do anything nix - Linux...

**Robert al-Khalil:** Oh, yes.

**Jerold Santo:** So he's got really detailed tutorials, but it'd be really cool -- and they're step by step, "Type this, type this..." It'd be really cool if each one had a button that's like "Launch an emulation", and you can follow the tutorial in an emulator.

**Robert al-Khalil:** Yeah, that'd be amazing.

**Adam Staravia:** Yeah, that's what I'm talking about. See, you're where I'm at.

**Jerold Santo:** I am where you are.

**Adam Staravia:** I've scribed it...

**Jerold Santo:** I'm connecting the dots.

**Adam Staravia:** I went the long way around the leg, and he's like "Let's just go across the leg." \[laughter\] On a speedboat.

**Jerold Santo:** This is kind of how we talk to ChatGPT.

**Adam Staravia:** Yes, that's right.

**Jerold Santo:** I get straight to the point.

**Adam Staravia:** Thank you, ChatGPT.

**Jerold Santo:** Adam has a very cordial conversation with it.

**Adam Staravia:** Oh, yeah. "That is great insight, ChatGPT. Tell me more." \[laughter\]

**Jerold Santo:** So use cases like that I think would be really powerful... How far away are we from that?

**Adam Staravia:** You should do this, man. Make it a thing.

**Robert al-Khalil:** I would love to, but first, I know very little about hardware stuff, so...

**Adam Staravia:** Oh. Well, there's that...

**Robert al-Khalil:** This would need a collaboration of sorts.

**Jerold Santo:** Okay... So if you're listening to this, and you can fill in the gaps where Robert has them, email him. If you want to collab, if you want to fork...

**Adam Staravia:** Robert \[at\] sandbox.bio?

**Robert al-Khalil:** Um, no.

**Adam Staravia:** That's not his email. Okay.

**Robert al-Khalil:** Well, my email is quite long. Robert.al-Khalil \[at\] gmail.com.

**Jerold Santo:** Okay, there we go. We'll throw that in the show notes for folks. And the repo lives...

**Robert al-Khalil:** On GitHub.

**Jerold Santo:** On GitHub. We'll link that up. Cool. Cool stuff, man.

**Adam Staravia:** I like it. So much possibility... So much potential... And I believe you could do it.

**Robert al-Khalil:** Yeah. I love it.

**Adam Staravia:** And you should do it.

**Robert al-Khalil:** We should. Let's do it.

**Adam Staravia:** Thank you for doing all you've done so far.

**Jerold Santo:** Let's do it! WASM. Alright. Thanks for talking to us...

**Robert al-Khalil:** Yeah, thanks for having me.

**Jerold Santo:** I'm sure this was better than the first one.

**Robert al-Khalil:** I think it was, yes. \[laughter\]

**Adam Staravia:** "I'm sure." Jerold's like "I'm sure." We'll see; if it ships, then you'll know if it was good.

**Jerold Santo:** That's true. The last one never shipped.

**Robert al-Khalil:** You should diff it. Maybe I just said the same thing. I don't remember.

**Jerold Santo:** Oh...

**Adam Staravia:** We could transcript diff it.

**Jerold Santo:** Transcript and diff it... There's an idea.

**Break**: \[56:30\]

**Jerold Santo:** So we're here with M. Scott Ford... You have a name like a great novelist. Have you ever been told that?

**Scott Ford:** No, I have not been told that.

**Jerold Santo:** M. Scott... We'll just call you Scott, right?

**Scott Ford:** Yeah, just Scott.

**Adam Staravia:** What does the M stand for?

**Scott Ford:** Matthew.

**Adam Staravia:** Okay.

**Scott Ford:** Yeah. My parents named me Matthew Scott, but never called me Matthew...

**Jerold Santo:** Huh. They must have decided later they liked the middle name better.

**Scott Ford:** Yeah, something like that.

**Adam Staravia:** \[unintelligible 01:00:27.25\]

**Scott Ford:** There's a story there somewhere... Yeah, I don't know that I ever got the full story, so...

**Jerold Santo:** Okay...

**Adam Staravia:** It could be a conspiracy.

**Scott Ford:** \[laughs\]

**Jerold Santo:** Yeah. You and I go way back...

**Scott Ford:** Yeah.

**Jerold Santo:** Years and years... Your wife, Andrea, was a speaker at my conference...

**Scott Ford:** Yup.

**Jerold Santo:** Probably a decade ago, I don't know. Listener of the show...

**Scott Ford:** Yeah, I've been listening to the show for quite a long time.

**Jerold Santo:** I came on your guys' podcast, Legacy Code Rocks...

**Scott Ford:** Yup, Legacy Code Rocks.

**Jerold Santo:** ...probably a decade ago... Always good to see you. I think we've met once or twice before, but good to have you here...

**Scott Ford:** Yeah, I met you at Sustain...

**Jerold Santo:** Oh, that's right, \[unintelligible 01:01:07.03\] to Sustain.

**Scott Ford:** I think you recorded me and Andre for that.

**Jerold Santo:** Right on. Lots of history.

**Adam Staravia:** Lots.

**Jerold Santo:** And you co-own Corgi bytes, which is a consultancy... How do you describe yourselves?

**Scott Ford:** Yeah, so we focus on kind of modernization and maintenance, and just kind of the joy of making improvements to software systems... We have a team of people who love making code better. Building out test suites, fixing bugs, paying down technical debt... Yeah. I was talking with Adam yesterday, I love fixing bugs. Just going through a list of bugs and finding and fixing them... It's so much fun.

**Adam Staravia:** Guess what's available? Ilovebugs.com.

**Jerold Santo:** Seriously?

**Adam Staravia:** Yeah.

**Scott Ford:** Yeah, it was like 4,200 bucks, but yeah, it's available.

**Jerold Santo:** Okay, so that's not totally available...

**Adam Staravia:** \[unintelligible 01:01:58.10\]

**Scott Ford:** Yeah, it's true.

**Adam Staravia:** In today's -- well, we spent $1,000 on changelog.com. That was eight years ago.

**Scott Ford:** Yeah, because before you were at the changelog, right?

**Jerold Santo:** TheChangelog.com, yeah.

**Adam Staravia:** But if you were really passionate about bugs, you would have the domain Ilovebugs.com.

**Jerold Santo:** \[laughs\] Somebody's out there holding that thing, thinking "Someone's this passionate about bugs. They're going to give me that 4,200."

**Adam Staravia:** No, this is available on the market. This isn't even like a broker. This is available on the market.

**Jerold Santo:** 4,200.

**Adam Staravia:** Yeah. It's a premium domain, so they're holding it as like a premium cost domain.

**Jerold Santo:** Well, cash is tight these days...

**Scott Ford:** Yeah.

**Jerold Santo:** So Corgi bytes has been a longtime business...

**Scott Ford:** Yeah, so it was founded in 2008. I had no idea what I was going to do with it; it was pretty much just the name. And then Andre came on, and we started doing consulting... We did like small little websites at first, and didn't really enjoy that. I was trying to figure out what is it that I liked doing, and then stumbled in on, like -- I love fixing code. I love turning a mess into something that looks new; so like a brownfield into a Greenfield. That transformation process is something that I genuinely enjoy doing. So building a company around that has been a lot of fun.

**Jerold Santo:** There's people who like brand-new cars, and there's people who like to restore old cars. And those people tend to be different people. And some people just love that.

**Scott Ford:** Yeah. I've sometimes fantasized... Like, if I had enough money and time to do it, I would probably love getting a late 1990s era car, and fixing it up, and turning it into an EV.

**Jerold Santo:** That'd be cool...

**Scott Ford:** It's almost like, for me, sometimes it's the bridge of the old and the new. So taking something that's old, breathing new life into it, and making it do more than it used to; making it better than it was before.

**Jerold Santo:** Modernizing it. I love it, too. I mean, you and I - we've found common ground. Furthermore, I did some rescue projects back when I was consulting... Furthermore, I loved it.

**Scott Ford:** It's kind of fun.

**Jerold Santo:** I kind of like being the hero... You know, like, this is all bad, and it's like "Well, here comes Jerold. He's going to make it better."

**Scott Ford:** Yeah. And I think for me, it's less about the hero and more about, you know, there are folks who think it's not possible, and...

**Jerold Santo:** \[01:04:15.21\] It's a challenge.

**Scott Ford:** It's almost like a challenge, and like a Hold my Beer kind of moment. Like "No, we can turn this around. You don't have to start over this. This can be made better."

**Jerold Santo:** What's the gnarliest turnaround you've done? ...maybe in terms of lines of code, or time spent, or you thought you weren't going to be able to do it...

**Scott Ford:** Yeah, so there was a system several years ago that they were kind of -- they were on a cloud server, and they weren't doing a very good job keeping the underlying server up to date. So I wanted to help them move from infrastructure as a service solution to more of a platform as a service solution, because I thought that the organization would be able to do a better job keeping up with that, and then they wouldn't have to worry about like OS-level updates anymore. They could just kind of focus on their code. Because the OS-level updates were way behind; like eight years behind. They hadn't done any Windows updates on this Windows Server for like eight years. And that was a challenging transition. It took a lot longer than I thought it would. We ended up crediting the client some time because of that, and just kind of recognizing that I thought it was going to go easier than it actually turned out to be. We kept finding services that were running on that server, like in the background, that we didn't know about, and one of them we didn't have a source code for; that was fun to grapple with that as a challenge.

**Jerold Santo:** Yeah.

**Scott Ford:** That was definitely one that was difficult.

**Jerold Santo:** Okay. Long-standing business hits against this recent macroeconomic downturn, and it's gone south, huh?

**Scott Ford:** Yes, it has been challenging. So we've lost a significant amount of our revenue. Our team is probably about a quarter of the size as it was a year and a half ago... And I've talked with other business owners that have companies of a similar business model to ours, software services, and there are a lot that have been hit really hard. A lot have gone out of business... Andrea said she had read an article with a - I forget who it was... I could probably find it if you wanted it for show notes... But it had a quote in there that there's like an extinction-level event for small software companies going on right now. And there's a lot more talent on the market, so from a services' perspective it's a lot easier for companies to hire full-time than it used to be... So I think there's less motivation to work with contractors, or stretch your team out that way.

I also think it's just a way that organizations have been trying to cut expenses and cut costs. And when you look at a balance sheet, when you look at a profit and loss statement, contractors come out of a different part of that than full-time employees do. So for your investors, it can look like the organization is doing better if you cut those expenses kind of further down on the profit statement.

**Jerold Santo:** Yeah.

**Scott Ford:** So, yeah, I think all the economic factors that are going on right now, so inflation, interest rates, two wars, the small/medium-sized bank failures... I think Silicon Valley Bank really caused a lot of VCs to really pull back some money. I've heard stories of companies that were funded with, say, $30 million, had their funding pulled... And so the business had to shut down. Or the investor was just like "The money I've given you, I want back", or "The money I haven't given you yet, you're not getting." So that's definitely a challenge that's going on right now.

I kind of think of like that VC funding almost as like plankton in an ecosystem... And like that dries up, and the smaller fish get affected first, and then they're not using services from the bigger fish, and then so they start to get affected... So I think there is kind of like that ripple effect to the ecosystem.

**Adam Staravia:** \[01:08:16.29\] Is that similar to krill?

**Scott Ford:** \[unintelligible 01:08:17.25\] yeah.

**Adam Staravia:** Yeah. The little guys, basically. The smallest of the small, that the whales chase.

**Scott Ford:** Yeah.

**Adam Staravia:** And then that dries up, and you've got a big whale that's just hungry, right?

**Scott Ford:** Yeah. Well, the big whale can go without food for a little while, but it's gonna start to affect it, too. So...

**Adam Staravia:** Yeah. And then what does it eat, right? It's like "Oh, man, my krill is gone. I guess I'll just die." We think about this too, like how has the market shifted in terms of what it perceives as value... Because when you have less, you scrutinize more, and you think "Did I just spend my money there because we had the money, and we thought it was viable, and so it was viable?" And now that we reconsider-- because I think in the last three years, since the pandemic, the whole globe has been reconsidering almost everything.

**Scott Ford:** Absolutely.

**Adam Staravia:** And so in a reconsideration of what the value is, do you think that the value of these rehab projects has changed? Or do you think it's just that there's no money?

**Scott Ford:** I think the values changed... I also think that low-code/no-code platforms have had a factor as well. It's a lot easier to build something kind of quick and dirty, that might meet your immediate needs... And maybe do that as an experiment for starting over, without having to engage a development team. And that's a capacity that's great. It will be an enabler for business. And so I think on the larger economic scale, that's good, and it does kind of affect the organizations that would have helped build the thing that low-code/no-code platform is now building instead.

**Adam Staravia:** Yeah.

**Scott Ford:** I do think that for the maintenance side I predict in the next five years - kind of within the next five years - you'll have organizations that have really built a lot on top of those low-code/no-code platforms, and start to bump up against the constraints, and want to start to break out... And so I think there'll be a market for helping organizations move that functionality outside those platforms, or find ways to extend that functionality, maybe through extensions that the vendor provides, or things like that where there's custom software that needs to be built there. I do see that as an opportunity. And yeah, that has an effect.

And I'm sure AI is having an effect at some point as well. I don't know how to quantify that... I imagine it's -- and it could just be part of like a wait and see on a lot of organizations, when they're trying to make hiring decisions on how they're going to grow their team. Maybe they're just waiting to see how productive their teams are going to be, and how that productivity might change as they start leveraging AI.

**Adam Staravia:** You mentioned in our conversation yesterday - which was not on the air, obviously... And to some degree, even TMI... But you mentioned essentially the business model is wrong, I'm Trying it, and you can fill in the gaps...

**Scott Ford:** Yeah.

**Adam Staravia:** ...the business model is wrong, or it needs to change, and you consider products...

**Scott Ford:** Yes, absolutely.

**Adam Staravia:** ...in and around what you already do, but a product that you can buy, that has a finite value that's maybe easier to buy even...

**Scott Ford:** Yeah, because there are a lot of problems that we've seen over the years that many teams have been facing, and I do think there's a market for building solutions to help teams solve those problems themselves without having to hire an outside contractor or an outside team. And so there are aspects that I think could be productized. And we've gotten started a little bit on one product... We've been working on it for a couple of years, don't really have -- we've got like an alpha demo that we've shown to people, and I've gotten some feedback on.

\[01:12:00.27\] We're still kind of working -- we're hoping to have a beta out; probably first quarter next year is kind of realistic for having something that people could actually sign up for and give us better feedback on. That's called Freshly. It's around analyzing dependency freshness, and looking at how fresh or out of date software dependencies are, like third party dependencies; most of them open source dependencies. And really assessing the quality of an application or a project from that perspective.

We also wanted to be able to assess at multiple levels of the -- you mentioned, Adam, that you're not a big fan of supply chain as a term for this ecosystem.

**Adam Staravia:** It's generally a pejorative... Like, open source is not a supply chain; it is a common. It's not a supply chain we just tap into and get. It's a negative...

**Scott Ford:** Yeah. If you think about your dependency graph, I think it would be great to evaluate multiple nodes on that dependency graph, and not just evaluate your node. So how well are the upstream projects that you're depending on, how well are they keeping up with dependencies that they're managing? And so I think that could be some pretty good meta analysis as well. A way to maybe even measure the health of a project that you're thinking of working with.

**Adam Staravia:** And the similarity between maintenance, this idea of Freshly, how old are my dependencies, how fresh are my dependencies, and this aspect of security... Because a lot of maintenance, or even like a refresh on a project, like you've talked about, it's kind of a security burden.

**Scott Ford:** It is.

**Adam Staravia:** Some of these products might be security-issue, that you're talking about...?

**Scott Ford:** Yeah... And so I think having out of date dependencies, one of the motivations for upgrading them is very much to try to avoid security issues. That's one of the motivations. I think there's also motivation around team productivity. It's a lot easier to work with the latest version of a library than it is an older version, just in terms of finding documentation. When you go look for the documentation for a project, you're going to find the latest version is going to be easiest to find.

**Adam Staravia:** It's usually findable, yeah.

**Scott Ford:** Yeah. Blog posts are gonna usually cover more recent versions than what you're working with, has been my experience. But yeah, on the security angle, I think that is a big motivator to try to avoid some of those security issues. And a lot of people we put the product in front of to kind of give demos, they've told us in addition to just seeing how out of date things are, they do want some perspective of how security plays a role.

One of the dependency freshness measures that we're using is called lib year, and you can learn more about that at libyear.com. And then I've taken a security approach to that, and built what I call like a liability index, which computes a similar metric as lib year, but it looks at -- where lib year looks at the distance in time between the version that you're using and the latest version, the liability index, which I published at liabilityindex.com - we haven't implemented a version of it yet, but it looks at the version you're using, and the distance between the next version that doesn't have any published vulnerabilities. So if the version you're on has published vulnerabilities, how many years in the future...

**Jerold Santo:** Do you have to go...

**Scott Ford:** ...do you have to go in order to find a version that doesn't have any published vulnerabilities? And so I think that could give more of kind of security-focused approach to that. And maybe even looking at different levels for liability index at the critical level, or different severity levels.

**Adam Staravia:** This makes me think about Source graph. Source graph is an intelligence platform that helps you understand code. \[unintelligible 01:15:47.25\] understanding is like "Is my stuff vulnerable, or prone to vulnerabilities?"

**Scott Ford:** \[01:15:55.02\] And one of the things that we're trying to do that's unique with Freshly is not just capture how things are right now, but capture how they used to be, and graphing that over time. So these metrics that we're collecting, and we're computing, we're mining information from a source code repository, and computing what these metrics would have been like in the past, and graphing that information. And I think the trend can really paint a fascinating picture for leadership, and hopefully get budget for some of these improvement efforts.

Something I've seen on a lot of teams is there'll be engineers on the teams who are aware this is a problem, they want to fix it, they don't like that they're living with this status quo, and they feel like their leadership hasn't given them enough flexibility to really go in and solve the problem. They feel like they're told to obsess over features instead, and some of these essential maintenance activities get prioritized.

**Jerold Santo:** Sure. And you think bubbling that up to somebody with decision-making would help them...

**Scott Ford:** That's my hope, is that if leaders, the people who are kind of in control of the priorities, and people who are in control of funding - if they had a better understanding of the problem, I think they would make different choices. I think, in a large respect, how out of date dependencies are is -- it's invisible; it's even invisible to the team, a lot of times. They just kind of pull in a package, they start using it and they move on. And there's not really much to help them stay up to date and kind of keep aware of that. That's starting to change a little bit with different package ecosystems. I feel like NPM is doing a pretty good job with letting people know when things are out of date when they do a NPM install. NPM-outdated is a perfect tool set for folks, and it has perfect output, and if it's easy to read... And I think more package ecosystems are starting to adopt that strategy and that approach. My hope is that that helps kind of increase awareness. I really do think it's interesting to see how well the team has been doing at keeping up with that churn.

And obviously, because of supply chain attacks - again, that's what they're called in the security ecosystem, is supply chain attacks... Sorry, Adam... \[laughs\]

**Adam Staravia:** I don't think it's the right term, but it is that term that people use, so I'm cool with it. This is all in conversation, because I was talking about WebSocket and how they secure the open source supply chains... And I'm like, you get it.

**Jerold Santo:** Socket Security, you're talking about... Not WebSocket.

**Adam Staravia:** Gosh, I'm such a fool.

**Scott Ford:** Oh, Socket Security. Okay.

**Adam Staravia:** Anyway...

**Scott Ford:** No worries.

**Adam Staravia:** Strike that. We'll fix it. We'll edit that out, like Mat says. \[laughter\]

**Jerold Santo:** It's staying in.

**Adam Staravia:** Socket. Thank you for helping me out on that.

**Scott Ford:** So supply chain attacks are definitely a big risk, and you can have an upstream library that gets taken over by a nefarious actor... And so staying up with the latest and greatest all the time, so just like -- if you're using Dependabot, just merging those in blindly, that might not be the best idea, because you do make yourself vulnerable to some of those vulnerabilities.

**Jerold Santo:** Totally.

**Scott Ford:** At the same time, you don't want to let yourself get months out of date.

**Jerold Santo:** Right. Where's the balance...?

**Scott Ford:** Yeah. Because with the Equifax breach from 2017, that was one Apache Struts dependency on the date that they were attacked, they were out of date by two months for the library that had the patch for that vulnerability. So a two-month window for that project, and that was a very impactful vulnerability. It was a very impactful event. It affected a lot of people.

**Adam Staravia:** The freshness of that library was stale by two months.

**Scott Ford:** Yes. When you look at that particular vulnerability. I don't know if all the vulnerabilities were patched in that release, but I know that the vulnerability that they were ultimately exploited on was two months out of date. And I think a lot of it is -- a lot of teams don't make updating things a regular part of their practice. It tends to be really challenging. It takes a lot of effort to upgrade some of these dependencies, especially if they include breaking changes. A lot of times software systems are really tightly coupled to these dependencies, so upgrading them is really non-trivial.

\[01:20:15.24\] And so I think -- kind of going back, Martin Fowler has a quote where "If something is difficult, you need to do it more often." So if software teams got in the habit of updating dependencies more often and kind of doing it as a practice, and really devoting time or even maybe devoting a team member whose job it is to stay on top of this stuff, then I think that could really help turn things around and keep projects healthier.

**Jerold Santo:** But on the other side, the supply chain attacks like the event-stream one etc. those hit people who don't have the dependencies pinned to a version, and their CI is just going to pull the latest...

**Scott Ford:** Exactly.

**Jerold Santo:** And so that's the other side; it's too fresh. So what is the right balance? It seems like unless you have a known vulnerability, staying one minor release behind is actually a best practice...

**Scott Ford:** Yeah.

**Jerold Santo:** And once there is a known vulnerability, now you've got to immediately get up to the latest. I don't know.

**Scott Ford:** Yeah, that can be a perfect strategy. And it also comes down to risk tolerance, and different organizations have different levels of risk tolerance... And there are organizations that aren't interested in staying on the bleeding edge. And I think there is a good argument to be made for if something's not broken, then don't fix it. Just because it's old, doesn't mean it's bad.

**Jerold Santo:** Right.

**Scott Ford:** But I do think that you do have these productivity impacts, and you do have these security impacts when you are working with older libraries and older versions of frameworks.

**Jerold Santo:** Yeah. Well, I mean, hopefully these products will breathe new life into Corgi bytes.

**Scott Ford:** Yeah, I think it'll be a little bit of transformation; kind of like in the cycle of growth, and reinvention, and rebirth... And I think that will be part of the lifecycle. When we were focused as a business on building small websites, building five-page websites, stuff like that, that business model didn't last very long, and the business went into an incubation period, and it was reborn out of that... It might be what's about to happen again. We'll see.

**Jerold Santo:** Yeah. You never know.

**Adam Staravia:** That does make sense. I mean, you've got to evolve. When change happens, resilience is change, really, essentially. You've got to change with the change...

**Scott Ford:** That's right.

**Adam Staravia:** ...a wise man once said. Right?

**Scott Ford:** Was that you? \[laughs\]

**Adam Staravia:** Maybe...

**Jerold Santo:** Martin Fowler?

**Adam Staravia:** I don't know... Well, good luck on that change...

**Scott Ford:** Thanks.

**Adam Staravia:** Good luck navigating it.

**Scott Ford:** I appreciate that.

**Adam Staravia:** And the product direction - I agree with Jerold, it does sound like the way to go...

**Scott Ford:** I think so, too.

**Adam Staravia:** Because if you can give an executive in I don't know what timeframe something that is authoritative and finite in terms of there is lack of freshness, or you're this far behind best practices, or some sort of indicator that says "I'm not hearing it from my developers, who in quotes 'whine' or complain, that I lovingly trust... But really, I need this authoritative thing that says "Hey, get your stuff together", you know?

**Scott Ford:** And trying to give your engineering teams a way to translate the data that the system is collecting in a way that can be easily consumed by their leadership. So instead of having a graph with a bunch of data on a webpage, and then trying to get your loot your manager to log into that, instead generate a PowerPoint deck, something you can toss into an email and forward to somebody... And in there could be a link to that dashboard. Like, if somebody wants to see the dashboard --

**Adam Staravia:** Like "Here's our vulnerability score", or something like that. Or "Here's our staleness factor, or freshness factor, or Freshly factor", or whatever it might be. And that could actually be quite good at marketing too for you... Because then it becomes maybe a race, or a competition of sorts, with executives, or CEO to CEO, like "Hey, what's your freshness factor?"

**Scott Ford:** Yeah. And it would help even within like an organization that might have a portfolio of projects - are there projects that are doing better than others? And then getting curious about the teams that are doing better; what are they doing differently, and is there knowledge that those teams might have, which might make sense to share with other teams?

**Adam Staravia:** Yeah, good plan. You should do it.

**Jerold Santo:** Yeah, man.

**Scott Ford:** Thanks. Working on. It just takes time. Building software - it takes time.

**Adam Staravia:** It takes time.

**Scott Ford:** Even with AI's help, right? It still takes time. I can't just snap my fingers and say "Hey, GitHub Copilot, build this for me." Or "Hey, AWS Code Whisperer, build this for me."

**Jerold Santo:** Right. You still have to fix those bugs that it spits out at you.

**Scott Ford:** That's right. \[laughs\]

**Jerold Santo:** Well, thanks for stopping by, Scott.

**Scott Ford:** Yeah, I appreciate you letting me chat.

**Jerold Santo:** You bet.
