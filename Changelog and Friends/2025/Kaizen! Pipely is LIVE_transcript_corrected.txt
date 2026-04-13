**Jerold Santo:** Well, we're here...

**Adam Staravia:** How did Kaiden begin?

**Jerold Santo:** It was a long time ago in Japan...

**Adam Staravia:** Ha-hah!

**Jerold Santo:** I don't know. How did our Kaiden begin?

**Gerhard Lazy:** 1300. \[laughs\] That was the year. Something like that. It began with this crazy idea that "Let's improve, but in a consistent way, so that every 10 Ship It episodes we'll talk about the improvements that we drive in the context of Changelog." Share them publicly. And that was our reminder that "Hey, 10 episodes, we'll be talking about everything that we've done." Some called it navel-gazing. I don't think that's what it was...

**Jerold Santo:** That was me, probably...

**Adam Staravia:** Jerold...

**Gerhard Lazy:** \[laughs\] It was good fun. And... Yeah, it's been four years. It's been four years.

**Jerold Santo:** It's been four years since our --

**Adam Staravia:** It's been longer than four years.

**Jerold Santo:** Has it?

**Adam Staravia:** A decade...! We've been Wizening a decade. We just started calling it Kaiden...

**Gerhard Lazy:** Yeah, we've been calling it as a Kaiden... So Kaiden 1 was about four years ago.

**Adam Staravia:** Kaiden as it is materialized roughly four years ago... But the relationship -- the reason why I bring that up is I want to say one thing. These guys are my ride or die people. Gerhard's amazing... Jerold, you know you're amazing --

**Jerold Santo:** I know I am.

**Adam Staravia:** But the magic and the beauty that's come from this relationship has just been tremendous. And to be here and share that with you all, and to share Kaiden 20, this navel-gazing approach to our platform, this constant attention to detail of improvement... And I think particularly with what we'll talk about today is unique to us specifically, in that we've built some infrastructure that's used by us specifically, where a behemoth - not negatively - is just not maybe the right fit, and we've been holding it wrong to some degree.

**Jerold Santo:** Right.

**Adam Staravia:** But this, what we're doing here, is just a wild ride, and I'm excited about this moment.

**Jerold Santo:** Is there a way to hold it right? That's the question I continue to ask myself. It turns out if you gaze at your navel long enough, there's cool stuff in there.

**Gerhard Lazy:** Definitely. \[laughter\] But it has to be long enough, and you have to do something about it. You have to have a proactive approach to it. Otherwise...

**Jerold Santo:** So thank you for joining us as we pull out a few of our treasures that we've found along the way... And something that we've built over the last -- when did we start Ripely?

**Gerhard Lazy:** Ripely was, I think, 18 months ago, roughly... The idea was "Shall we do this thing? I mean, we've been talking about it long enough. Shall we actually try doing something about it?" And the beginning was, as all beginnings, "Can we do this? How long will it take? What will it take? Do we know what even needs to happen?" And that's how the conversation started. And many of you that have listened to those conversations remember us, how we were pondering, "Should we, should we not? Are we crazy?" Three wise men, the question mark was really the emphasis... Are we wise doing this? We have no idea.

**Jerold Santo:** Right.

**Gerhard Lazy:** And then along the journey, the best part was the friends that joined us. So it's turned out this was not such a crazy idea... And just the idea of improving something in public so that others see how we do it, and it's our approach, and maybe it will inspire others. And I think that worked really well, and here we are today, with friends...

**Adam Staravia:** With friends...

**Gerhard Lazy:** And again, that's the focus. Improving with friends. It makes me so happy.

**Adam Staravia:** Thank you all for being here for that.

**Gerhard Lazy:** Thank you. We appreciate you very much.

**Jerold Santo:** For sure. Absolutely. So it all started with a dream, a pipe dream...

**Gerhard Lazy:** Indeed.

**Jerold Santo:** ...on a Kaiden number that I can't remember.

**Gerhard Lazy:** 13, I think. I think so.

**Jerold Santo:** Kaiden 13, when we were lamenting our cache miss ratio on Vastly... But they had this really nice Varnish as a service that we'd been using for a long time; we just didn't like the way that we had to use it through Vastly, which was through a web UI, and a strange comment based versioning control system that we invented on top of it... You had to put the name of the person who does the thing and the thing you're doing as you update the config... Which would produce this gnarly, I don't know, thousand-line Varnish config that would work mostly sometimes.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** And it was great when it worked, but when it didn't work, it was very difficult for us to have visibility and debugability in order to fix that. And so I said on Kaiden 13, "Wouldn't it be cool if we could just have this 20-line Varnish config in the sky, just deployed around the world, and it could just be for us, everything we need and nothing we don't?" And Gerhard got a twinkle in his eyes...

**Gerhard Lazy:** Yeah. I love a challenge...

**Jerold Santo:** And he said "20-line? I can give you 500 lines." \[laughter\]

**Gerhard Lazy:** Well, I think it's close to a thousand now, but anyway, anyway... There are reasons...

**Jerold Santo:** So it was a pipe dream. But that began our journey down this particular path, which we are at the end of, or a milestone at least... You're never at the end of this kind of path...

**Gerhard Lazy:** Nope.

**Jerold Santo:** ...where we decided on our Kaiden 19 "Hey, we're ready to run this." We call it -- Ripely is the open source project. Pipe dream is our instance of that, because this has been our pipe dream. And we're there. We're almost there.

**Gerhard Lazy:** We are. Yeah.

**Jerold Santo:** But on Kaiden 19, we were like right at the precipice... And I said, "What if we just get together and do it together?" And you guys said, "Yeah."

**Adam Staravia:** Let's do it!

**Gerhard Lazy:** And I was like "How about on stage in Denver?" And they're like "Sure." And so here we are. There's your setup, Gerhard... The way Maidens usually work is Gerhard works way harder than Adam and I do, and he prepares...
**Adam Staravia:** We show up.

**Jerold Santo:** Yes. And then I say something like "Gerhard, take us on a ride. Tell us what we're going to do." And so Gerhard, take us on a ride. What are we going to see today out of Ripely and Kaiden 20?

**Gerhard Lazy:** Thank you very much. So we will start with a little bit of history, so that everyone is able to visualize a couple of very important milestones. Then we're going to ask you a few questions... So you better think of some good questions to get back at me or at us. So let's see how that goes. And then we'll do something special, because everyone took their time... This took considerable effort on all your parts to be here, and we want to recognize that effort by doing something special, on stage, live. So let's see how that goes.

**Adam Staravia:** \[08:39\] What are we doing...?

**Gerhard Lazy:** Alright, so first, let's start with the beginning. The beginning is July 26th, 2025. This is an important moment. We're all here today. It's the first time that this is happening. Kaiden 20 is the moment. Thank you all for being here. I'm sure that you all know this -- now, it says 20 episodes. Actually, it's 19; one was republished. But it's been 19 Kaiden episodes... And this started actually in 2021, in July. I had to look this up. I wasn't sure exactly how long it was, but that's when this started. So this journey, officially, when we started having these conversations, all recorded, all remote, happened many years ago, and it took us this long to finally do this in person.

**Adam Staravia:** 10 years.

**Gerhard Lazy:** Right. And if you count exactly when this unofficially started, it's been a decade.

**Adam Staravia:** It's been a decade.

**Gerhard Lazy:** So we're good friends now.

**Adam Staravia:** I'm stretching it by one. 2016 was the year we launched what is now our platform. It's an open source platform, Changelog.com. You all know that. It's on GitHub. Some of you contributed, you're probably in the issues, or at least reading them... But it's been a journey. It's 2025, it's not quite 10 years, but I'm rounding up. Give me a gimme.

**Gerhard Lazy:** Yeah. Next year maybe we do something even greater, right? Maybe. We're building up to that.

**Adam Staravia:** That's right.

**Jerold Santo:** Yeah, jumping the gun.

**Gerhard Lazy:** Okay. So the reason why we're doing this is that it's about friends. This is the new context. It used to be Ship It. Before it was unofficial, it used to happen just among like a few people, and now all of you are here, and we appreciate you. So thank you very much. Because as you know, it's so much better with friends. So Changelog & Friends is the context, and including friends that want to be here, but maybe can't, next year hopefully, or the next time we meet, it's a good reason to make this crowd bigger. But this is how it began. This is the first moment we have met in person, and it's amazing.

Alright. Now, you haven't noticed here, but this is something that I pay attention to, because the person that takes the picture is never in the pictures... So we need to acknowledge the person taking pictures. And that is Aaron. He's over there. He's still filming.

**Jerold Santo:** Hey, Aaron.

**Gerhard Lazy:** Thank you very much. So yeah, thank you for being here and capturing this moment for all of us. That's so great. So we are friends, I think we can call ourselves friends when we go for a beer, and we go for a hike, and we share a meal... So that's, I think, what it means to the beginning of a nice friendship, that enjoy making things better. That's really what brings us together. And we do it in a public way, we share... And even when we get it wrong, that's fine, because it's always about improving, it's not about being a hundred percent right, or knowing it all, figuring things out. And that makes me so happy.

So you all know this, we post these as discussions on the changelog.com GitHub repository. This specific Kaiden is discussion 546. And if you want to do a bit of digging to see what went into making this Kaiden, that's where you can go for like the technical stuff, for the pull requests, for the code... All of it is there. And I think the first step that we need to do is set the record straight. And the reason why I remembered it is because of that very small thumbnail. There's three people there... There's BSD PhD. So PHK is a Paul-Henning Camp. I didn't know who he was until recently. He is the guy that had a huge contribution to FreeBSD, NTP time counters, FreeBSD jails, MD5 Crypt, and... You all know this...

**Jerold Santo:** Can I say it?

**Gerhard Lazy:** \[12:30\] Yes.

**Jerold Santo:** The bike shed.

**Gerhard Lazy:** That's it. That's right.

**Jerold Santo:** He invented the bike shed.

**Gerhard Lazy:** 1999, the guy that -- so I think that's really important. And we didn't know - a bit of history - this was an important moment, and I think I'm going to switch the screen now to this... Because this is important. So Andrew O, he wanted to set the record straight. No, Walgreen. Sorry. Walgreen, May 13th. He wanted to set the record straight about Varnish, which is the technology that we use, the relationship to Vastly, and the relationship to Varnish Enterprise. And it's all here. So Vastly is not running Varnish Plus, which is a Varnish software product; they have their own fork. So that is important. It's similar, but not quite the same.
What we use is not nothing from Varnish software, not Varnish Plus... We're using the Varnish Cache, the open source, project as anyone can consume it. So we have built -- everything that we've built is an open source technologies. And that is important to us, because that is in our DNA. So there's some history here that's important... So we are building on Varnish Cache, open source.

Alright, back to where we were... Cool. So we did this thing, and this thing is important, but actually, we did a few things over, I think, four years...? We did quite a few things and years.

**Jerold Santo:** 10 years. \[laughs\]

**Gerhard Lazy:** 10 years. 10 years. Okay, 10 years.

**Jerold Santo:** Just keep that in mind. Adam's not going to let it go.

**Gerhard Lazy:** Nine...

**Adam Staravia:** "Ten years later..."

**Gerhard Lazy:** Yeah, that's a good one. So they were all good. I think most of the things were good, that we've done.

**Jerold Santo:** Most of the things were good, but that's not all things.

**Gerhard Lazy:** Right. Shall I fix this now? \[laughs\] No, it's okay. Okay, sorry. My bad. So what are some of the things that you don't think went as well? Let's talk about that. Out of your collective memory... Maybe even someone from the audience can tell us a few things that didn't go so well.

**Adam Staravia:** S3 costs. Yeah, we spent more money than we should have on S3.

**Jerold Santo:** We were ballooning, and we didn't know it, until that one Kaiden episode where I finally looked at it. And then I was like "Oh... We should change this. We should address this."

**Adam Staravia:** The bill went from like 15 bucks a month to like maybe 180 at peak, I believe... Which is still small. We're not massive.

**Gerhard Lazy:** We're a lean operation.

**Adam Staravia:** Yeah. But that's not cool.

**Jerold Santo:** But now we're on R2, and we're spending like eight bucks a month.

**Adam Staravia:** Yeah. They basically pay us. Or they should pay us.

**Gerhard Lazy:** They should pay us, yeah.

**Jerold Santo:** Now it's good, but that wasn't good.

**Gerhard Lazy:** I deleted a few things, that I shouldn't have... \[laughter\] As you do... Right? Flying too close to the sun. It's a good thing from that perspective.

**Jerold Santo:** And there was one time when Gerhard went into -- I don't know what it is anymore; a config, or one of my pieces of code... And he changed something that to me was inscrutable. Like, why, what, who? But I had so much respect for the guy and so much imposter syndrome that I thought surely, he knows better than I do.

**Gerhard Lazy:** I remember that. Yeah.

**Jerold Santo:** Yeah. "And I must be a fool, but it looks wrong. But I'm going to go ahead and roll with it, because Gerhard knows what he's doing." And then I found out much later you had no idea what you were doing.

**Gerhard Lazy:** No, I did not.

**Jerold Santo:** \[laughs\]

**Gerhard Lazy:** \[16:00\] So this is something really important, and it's at the heart of what we do - we are figuring stuff out, and we are okay to admit it publicly. We mess things up. But there's no way you're going to learn if you don't make mistakes. It doesn't matter how much experience you have, it doesn't matter how many things you think, you never know. Let's be honest, you don't really know. You're mostly making stuff up. Some things help you, but it's all in the confidence that you will be able to figure it out, you will be able to push through... Just stick with it long enough. That's all it takes.

Alright. So today we did the biggest thing ever... What was that?

**Adam Staravia:** A live show?

**Gerhard Lazy:** A live show. Yes, yes, yes. That's one.

**Adam Staravia:** We showed up in a city we don't live in...

**Gerhard Lazy:** Right.

**Adam Staravia:** People flew here with us... That's a big thing. Is that what you're referring to?

**Gerhard Lazy:** Yeah. That's one of the big things.

**Adam Staravia:** What else?

**Gerhard Lazy:** Well... \[laughter\]

**Jerold Santo:** I'm so curious what we did...

**Adam Staravia:** What did we do?! Tell us!

**Gerhard Lazy:** What did Gerhard do? \[laughs\]

**Adam Staravia:** Yeah, let's scratch that. What did Gerhard do?

**Gerhard Lazy:** Yeah, yeah, yeah.

**Jerold Santo:** What'd you do, Gerhard?

**Gerhard Lazy:** So I did something I will show you very soon. Trust me, it's coming... But it's the biggest thing ever. Alright, so the problem -- the fact that it's green, don't let that mislead you. It's a bad thing. Psychology of colour is very important.

**Jerold Santo:** So what is this?

**Gerhard Lazy:** The 17.93% is the cache hit ratio on our current production CDN... Which is low. That's really, really low. It means that less than 20% of the requests get served really fast, 80% plus are slow. And while it doesn't really impact us - I mean, it's all good for us - it impacts you. When you load something, it takes a while to load. And it shouldn't be that way. Things should be very, very smooth. And when something goes wrong, in the backend for example, if 80% of the requests have to go back to the backend, it means that they can fail. So the chances of something failing are fairly high if there's something wrong with the backend, and that's the other thing which I keep thinking about a lot.

**Jerold Santo:** Yeah. And it's worth noting that our data is unidirectional. I mean, we rarely change anything once we publish.

**Adam Staravia:** Episode one is still episode one, 19 years later.

**Jerold Santo:** Yeah. Every once in a while we might put the wrong audio in the wrong episode, or we might have to edit something that --

**Adam Staravia:** Or you ship the entire wrong audio, like I've done recently...

**Jerold Santo:** Yeah, like Adam did recently... So we make mistakes, and when you make a mistake, you want to be able to quickly rectify it, purge everything, and get back to where you were. But generally speaking, you put a mp3 up on a CDN, and then you deliver that same mp3 in perpetuity. And so this number is abysmal. That's terrible. We should never have misses. And that's what I've been saying for 10 years... "How do we keep having cache misses?" Okay.

**Gerhard Lazy:** \[laughs\] And the problem is that -- in this case, it's mostly the website. So the Changelog website appears slow in a lot of cases, and that's not great. So that was the problem that we were trying -- or that was the thing that we were trying to improve. That's how this started.

Alright. Episode 26 - this is what Jerold was mentioning when we began - Should we build a CDN? That was the moment we were thinking "Should we do this?" I mean, are we really at that point? And it took a while, but the conclusion was yes. I mean, we should at least try and see how far we get. That was 18 months ago.

Pipely.tech - we had this up for a while. We talked about it at Christmas. A new CDN is born. It hasn't been updated recently, but it will be... But this is the home for the open source project that we would like others to use at some point. I think it's getting there. It's not quite there yet, but we have made many improvements to make it easier to consume.

**Break**: \[20:03\]

**Gerhard Lazy:** This is something that has been bugging me for years. We run on Fly.io and Fly.io has points of presence all over the world. But our application only runs in a -- well, in Ashburn, Virginia, because it's closest to the database. Of course, it's going to be close to the database, because data has gravity. But we wanted to distribute the application for a long, long time, but it was never the right model. With a CDN, that's exactly what we want to do. We want to get those instances all over the world, so finally we can say that after all these years we are holding Fly.io right. And it's been working pretty well.

**Jerold Santo:** Is that the big thing?

**Gerhard Lazy:** I think it is a big thing.

**Jerold Santo:** Is that the big thing you were referencing earlier?

**Gerhard Lazy:** No, no, no, no, no. It's coming. It's coming. I'm building up to it.

**Jerold Santo:** I'm just waiting for that moment.

**Gerhard Lazy:** This is one of the things. We are holding it right.

**Adam Staravia:** I want to say one thing too, real quick. Leave that there. That slide's good. The next one's good.

**Gerhard Lazy:** Next one?

**Adam Staravia:** Yeah, the next one's fine. \[unintelligible 00:23:52.06\] show some things, but you see Fly here... They're not here. We didn't make this about sponsors. We want it to be about you all, us doing a normal live show together that wasn't like "Hey, let's charge an enormous amount for tickets", or whatever it was. Furthermore, we just want to go somewhere, have some fun, get together, and just share this story. But I do want to recognize that Fly, and Kurt, and the team there have been extremely supportive of us. I'm not saying you should use them, but they love us, we love them... And what we're building is really on top of the best platform, we believe. So Fly is amazing.

**Gerhard Lazy:** Fully agree. Yeah, I fully agree with that. Jerold? All good?

**Jerold Santo:** Yeah.

**Gerhard Lazy:** Alright. So this happened about six hours ago or seven hours ago. This is 1 a.m. last morning, okay? Something went wrong. So things will continue going wrong. You will never really get there. It's all about the mindset of "Can we do it a little bit better?" And again, we are figuring stuff out. So this was yesterday, last night. So this is a question for the audience... Who would like to see us improve this specific crash live?

**Jerold Santo:** Ooh... Yeah?

**Gerhard Lazy:** Alright, let's do it. Cool. So what do you think happened here? Let's do like a very quick understanding of what the problem is. What do you think happened here?

**Jerold Santo:** Can you describe the architecture of Ripely? ... Pipe Dream, in terms of what's going on out there?

**Gerhard Lazy:** Yeah, I can. So it's Varnish instances... I mean, Varnish is really at the heart of it. There are a couple of other components around it, but Varnish is the heart of it. Varnish makes requests to backends. The backends, in this case, would be assets, for example. We store static assets, we were mentioning MP3 files, PNG files, JavaScript, CSS, that kind of stuff... Which rarely changes. Then there's a Feeds backend. Feeds stores generated feeds for users, Plus members, and shows, various shows.

**Jerold Santo:** Correct. Every show has its own feed, and then you can also create your own custom feed. So there's something on the order of 600 to 800 feeds, I would say.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** Eight of which are way more important than the others, because they are publicly consumed by all the podcast indexes.

**Gerhard Lazy:** Exactly. And those feeds get the most requests from all the platforms, the podcasting platforms that consume the Changelog episodes... And they distribute them to their audiences; or to your audiences, but through that platform.

**Jerold Santo:** Correct, yeah.

**Adam Staravia:** Our audiences.

**Gerhard Lazy:** Our audiences, yes. Our audiences, for sure. And what this is, basically - we get these instances that are distributed around the world, so that the delivery of that content gets accelerated. The one thing which I haven't mentioned is the Changelog application, the website, which is an important one... That's where many users go to, for example, look at the homepage, look at news, things like that. And that is the one which is most sensitive to latency, because as I mentioned, it's only in one location, close to the database... So we need to accelerate delivery of that website to users which are around the world, including Australia, South Africa, South America... All over the world. We have a very diverse audience. And we want those users to have just as good experience as anyone else that's maybe in North America.

**Jerold Santo:** So in this case, 1 of our 10 instances of the Ripely application crashed.

**Gerhard Lazy:** Ran out of memory and crashed.

**Jerold Santo:** Misty Bird 4931.

**Gerhard Lazy:** Yeah, Misty Bird. That's the one. Misty Bird crashed. That's what happened, exactly.

**Jerold Santo:** Okay. So now to your question to the audience was...

**Gerhard Lazy:** Why do we think the application crashed?

**Jerold Santo:** Why do you think it crashed?

**Gerhard Lazy:** And anyone can answer except Matt, Nail, and James... \[laughs\]

**Jerold Santo:** Do they already know why it crashed? It ran out of memory...

**Gerhard Lazy:** Yes, of course. Thank you.

**Jerold Santo:** I appreciate that answer...

**Gerhard Lazy:** Someone's paying attention... \[laughs\] But why did it run out of memory? Why do you think it ran out of memory?

**Jerold Santo:** Because there wasn't enough memory. \[laughter\]

**Gerhard Lazy:** Right. I love some trolling. Seriously, now. You're going to make me say it, right? Okay, so as more content gets cached in memory, the problem is there's a configuration which - I wish it was easier to make, but you have to manually adjust how much memory you give to Varnish out of the total memory available.

\[28:19\] So there is a dance that you need to make, so that you know how much is enough so that when more memory gets allocated, the thing doesn't fall over. I wish this particular thing was easier; maybe something that we can improve. But for now, you have to fine-tune it and find if you have four gigabytes of memory total, how much should Varnish be allowed to use? And if you think it's four gigabytes, it's way too much.

So that's what we're going to do now. I'm going to switch to some live coding and show what happened. So -- actually, you know what? Let me try this. How's the font? Can everybody see the font? Can everybody see what's there? I'll make it a little bit bigger. A little bit bigger. Okay. So this is the change. And if I'm going to undo this, you'll see what it was before.

So I thought - let me take responsibility of this; I thought that 800 megabytes is going to be enough. This was the case when the application had two gigabytes. So the instance had two gigabytes, and 800 megabytes of headroom was enough, so the application wouldn't crash because of out of memory issues. And apparently, when you have four gigabytes, 800 megabytes are not enough. So what happened is 33 percent. 33 percent should be enough for this to work. And again, you have to specify this explicitly. I'm sure that we'll improve this at some point. This is what this looks like. So we're going to push this change into production, live right now. Here it is, here's the change. So we'll say "Increase Varnish memory--" Or limit. Let's do that. "Limit varnish memory to 66%." Varnish memory can only use 66%. Okay, I committed. What's going on? Of course, I need to connect. Let's do that. Let's connect.

**Jerold Santo:** Oh, you're offline.

**Gerhard Lazy:** Yeah, I'm offline. Let's do this. Again, this is live. This is not recorded; it hasn't happened. Let's see how this -- I normally record these things, but let's see what's going to happen.

**Jerold Santo:** Yes... Good time to go live, Gerhard. Let me just read this Bill Gates quote...

**Gerhard Lazy:** Okay...

**Jerold Santo:** You thought eight hundred megabytes ought to be enough...

**Gerhard Lazy:** Yes.

**Jerold Santo:** Bill Gates: "640K ought to be enough for anybody."

**Gerhard Lazy:** Right. Right. Apparently not.

**Jerold Santo:** So you know, it's not an unreasonable thing that you thought.

**Gerhard Lazy:** Nope.

**Jerold Santo:** Okay.
**Gerhard Lazy:** Alright. So what happened is we committed and we pushed this one commit... And to deploy something into production all that we have to do is tag the repository. So tag and commit. So RC3 is the last one that went out. You can see when it went out, it was two days ago. We're going to do an RC4 now. And all we have to do is this. \[unintelligible 00:31:08.06\] So I'll do just tag, because I don't want to remember the command; it's quite long. So I'm going to do the SHA. The SHA in this case is going to be -- sorry, tag. So v1.0.0 RC...

**Jerold Santo:** Four.

**Gerhard Lazy:** Four. There you go. Nice. We'll just do head, right? Of course, it's going to be head. And the discussion -- this is the changelog discussion where you can basically listen about this thing. So this is us preparing Kaiden 20. Remember that GitHub discussion I talked about... That's what this is going to do. And I'm going to push it now... No, push. Git push.

**Jerold Santo:** Oh...

**Gerhard Lazy:** Oh, what happened... Undefined... That should have been fine. It looks like the connection dropped.

**Jerold Santo:** Someone's blocking port 22.

**Gerhard Lazy:** No, no, the connection dropped. Let me just go back...

**Jerold Santo:** \[31:57\] Let me read a Bill Gates quote.

**Gerhard Lazy:** Yes, sure. Another one. \[laughter\[

**Jerold Santo:** "Dear ChatGPT, give me another Bill Gates quote."

**Gerhard Lazy:** That's good. Push again... I mean, just make this... It's going slow... There you go. That pushed. Cool. So the tag went out, and what we're going to see now is -- actually, this one right here is going to go to the actions... So this is a live -- this one right here, 1.0.0 RC4, and it's going to push this change into production across all instances, it's going to roll them live. We're deploying this. So why is it significant?

**Jerold Santo:** Let me set the record straight.

**Gerhard Lazy:** Sure.

**Jerold Santo:** Bill Gates in 1996 said, "I've said some stupid things and some wrong things, but not that. No one involved in computers would ever say that, that a certain amount of memory is enough."

**Gerhard Lazy:** Right.

**Jerold Santo:** So I guess I take it back.

**Gerhard Lazy:** Is that true?

**Jerold Santo:** I don't know. \[laughter\]

**Gerhard Lazy:** Is that factually correct?

**Adam Staravia:** What is your source of information?

**Gerhard Lazy:** Yes...
**Jerold Santo:** So there you go. He may or may not have said that... We're watching it roll out.

**Gerhard Lazy:** I see. So now we're seeing like a live rollout, and we'll see -- so publish and deploy tag... It's doing all the validation... Go on, go on... It's moving on, it's going through the changes...

**Jerold Santo:** Errors, errors, errors...

**Gerhard Lazy:** Yeah, it's saying errors, but it's going to resolve itself. It just takes a while. So there you go.

**Jerold Santo:** How long does it normally take, Gerhard?

**Gerhard Lazy:** Well, last time I think it took two and a half minutes.

**Jerold Santo:** And you thought this was a good idea.

**Gerhard Lazy:** Of course. Why not? Look, we're already creating the new machine instance. Look at that. That's going...
**Jerold Santo:** Alright...

**Gerhard Lazy:** So this is something that I think is important to get right early on... And that thing is "How long does it take you to push a change into production?" So how long does it take you to make a change and see that change roll live? And this is something that we've been working on for quite a few years on this thing. We do push to production, we own our production... We don't develop in production. That would be crazy, even for us. But it's like all this mentality of "If I'm going to make a change, how long will it take me to see that change happen?" And if you can shorten that time, you're in a good place.

**Jerold Santo:** Yeah.

**Adam Staravia:** 10 years ago, it took 20 minutes or so...

**Jerold Santo:** It was long.

**Adam Staravia:** It was a long time.

**Jerold Santo:** It was long enough that you go do something else.

**Adam Staravia:** And now it's two and a half minutes, maybe.

**Gerhard Lazy:** And this is a global CDN. So we are pushing this change to all the instances of the global CDN. Where do we run them? Let's have a look. So this is it. So we are in Ashburn, Virginia. These are the instances. Two days ago, if I'm going to refresh this, you'll see the new instances come live. So that was two days ago, that was like the last deploy... Let's refresh. Deploying 57 now. That's the commit. We have new instances coming up. And you can see we do blue/green.

Of course, we need to blue/green to deploy the new ones. The old ones are still there. Two of everything, it's an important rule... And yeah, this works fairly well. It will not have any downtime, and we can look at that in a minute.

So Ashburn, Virginia, Chicago, Dallas, Texas, Santiago, Chile, San Jose, California, Heathrow, of course (London), Frankfurt, Sydney, Australia, Singapore and Johannesburg. So these are all places where we deploy these instances, and they will accelerate all the content to our users.

**Jerold Santo:** Yeah. Does anybody out there have a deployment pipeline that runs faster than two and a half minutes?

**Gerhard Lazy:** Does anyone have a deployment pipeline? Let's start there. \[laughter\]

**Adam Staravia:** I've got a hand up...

**Adam Staravia:** Two people, three people... Four people.

**Jerold Santo:** Alright, I think we're winning.

**Adam Staravia:** Five people, six people.

**Gerhard Lazy:** Cool.

**Jerold Santo:** Two and a half.

**Gerhard Lazy:** Two and a half. Nice.

**Jerold Santo:** It only feels long when you're on stage.

**Gerhard Lazy:** Yeah.

**Adam Staravia:** Deploying now.

**Jerold Santo:** When you're sitting at your desk...

**Gerhard Lazy:** This is real. This is real. Like, not edited... This is what it feels like. Now, I don't think two and a half minutes is long. I think we can improve it. But you need to think about all of these need to happen behind the scenes. The allocation of resources, the health checking... How do you know what you've put out there is correct? And you need to wait a while to make sure that the thing doesn't crash. That's why you need to wait at least 60 seconds before you can say "Yup, this is good." You need to do a few health checks. Because if the thing starts falling over, you don't want to leave that thing running in production, of course.

\[36:18\] Cool. So I think we're in a good place... The one thing which I wanted to show is if I come back here -- can you see that? Is that graph looking good to you? Yup? Cool. So do you see this yellow line? This was the instance that crashed. So this one -- there we go. It's San Jose, California. For some reason, there are a lot of requests hitting this instance. And those requests, they don't look like human requests, so I think we may have some sort of bot situation going on. Some sort of, I don't know, LLM trying to learn...

**Jerold Santo:** OpenAI caller?

**Gerhard Lazy:** Yeah. There are a lot of requests. And if I'm going to look at this one, the CPU utilization, this is the same instance right here, the one in San Jose, California. I mean, look just how abnormal this instance behaves. And if I'm going to remove that, you can see all the others. So all the other instances, the CPU usage is fine, but this one is spiking up to 100%, because it has a lot of requests. Now, obviously, this is in front of the application, so a five-minute load average... We can also see here, San Jose, California... Yes?

**Jerold Santo:** Can we see the endpoints that it's serving?

**Gerhard Lazy:** The endpoints that it's serving? We can, yes. So let's do a tiny \[unintelligible 00:37:33.18\] right now.

**Adam Staravia:** This is what happens - Jerold's like "Can we do X?"

**Gerhard Lazy:** "Of course we can. Of course, we can, Jerold. Of course."
**Adam Staravia:** And at the moment, Gerhard's like \[unintelligible 00:37:37.10\]

**Gerhard Lazy:** No, we can. We can definitely do this. Okay. So I'm going to switch to this view... And this is the last seven days. And I'm going to make this a little bit bigger for you to see. Can you see that alright? Okay. So you can see that we're here, July 26th... So the application went into production a few days ago. So not all of it, not completely, but we started routing a bunch of traffic to the application, to see how well it would handle our users.

**Jerold Santo:** Is that the biggest thing we ever did?

**Gerhard Lazy:** Almost. \[laughs\] It's getting close.

**Jerold Santo:** I'm still waiting for this.

**Gerhard Lazy:** It's getting close.

**Jerold Santo:** Okay.

**Gerhard Lazy:** But this basically shows that we had many, many steps towards this moment. And now, together with you, we've shown you how we can update something that's running live, that is serving -- I mean, this doesn't sound like a lot of requests, a thousand... But the granularity is 30 minutes. And we are sending a portion of the traffic, and it's handling it pretty well. And we can see that the biggest users, or like the most requests are coming from ORD.

**Jerold Santo:** Chicago.

**Gerhard Lazy:** Chicago. That's the one. Frankfurt next. London, Heathrow. And it's not me running load tests in Singapore. So these are like the -- and then San Jose, California, right here.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** So we are running live traffic. Not all of it. A portion of it. But we wanted to see, will this thing continue working well?

**Jerold Santo:** Did you know that?

**Gerhard Lazy:** No.

**Adam Staravia:** I don't think so.

**Jerold Santo:** Yeah. So technically, we're not launching Pipe dream today, because we launched it on Thursday, just me and you.

**Gerhard Lazy:** Exactly. \[laughs\] Sorry, team. We did it.

**Jerold Santo:** Well, we barely launched it. We launched one out of five.

**Gerhard Lazy:** One out of five, yeah.

**Jerold Santo:** Yeah, so roughly 20% of requests go through our Pipe dream at this point.

**Gerhard Lazy:** So whenever you go to Changelog.com - that's it. One out of five requests hit the new instance. And we were able to see how does it behave with 20% of traffic. And it's working. No one complained. Adam didn't even notice. And that's one of the best things to roll things out - you do it in such a way so that... I mean, it is a big thing to us and to people that understand and know what goes behind it... But to everyone else, did anything change? Because if you do this type of job correctly, all people see is maybe little improvements. And if they're not paying attention, even those they will miss.

**Adam Staravia:** They think you're always just badass.

**Gerhard Lazy:** \[40:12\] Well, I think we are a good team. \[laughter\] And the other thing which I want to mention is that while what you see here, again, it feels very -- it just happens. It's like a small thing. The work that went into it, it was months and months of preparation, months and months of discussion... People joining us, working with us... I want to thank James. I mean, he was the first one that has joined this --

**Adam Staravia:** Thank you, James.

**Gerhard Lazy:** Thank you very much. James A. Rosen. Yeah, thank you, James. Thank you. Talking in the various issues... The first one that we had, basically being with us for almost two years now, discussing problems that we thought were problems At some point we were questioning, are we maybe too strict? Are we too demanding out of this? And no, no. I mean, we want things to be better. And this is why we want things to be better. So James, thank you very much for all the conversations, keeping us big picture; that's all objective perspective as well. That was so, so helpful. And then Matt Johnson, I appreciate that.

**Jerold Santo:** Thanks, Matt.

**Gerhard Lazy:** Just, thank you. Thank you.

**Jerold Santo:** What did Matt do?

**Gerhard Lazy:** It was all about like VCL and going a bit deeper -- just to have like another perspective on VCL... I mean, he has a lot of experience in VCL and Varnish in general, but also documentation, also like a diligent approach to "How should we do this so that it's easier for others?" And that was like so great to have that help. Now, that was months and months and months of -- I mean, again, all of us have full-time jobs, all of us do something else. But in our spare time, we find a bit of time to help others... And this was that. So thank you very much for that.

**Jerold Santo:** Matt had a good idea last night. Can I pitch it to you?

**Gerhard Lazy:** Of course. Yes, please. Yes.

**Jerold Santo:** Okay. So my desire was a 20-line VCL.

**Gerhard Lazy:** Yes.

**Jerold Santo:** You gave me a thousand lines. Matt says...

**Gerhard Lazy:** We can count.

**Jerold Santo:** ...you guys can just pull most of it out and do an included...

**Gerhard Lazy:** \[laughs\] Yeah, that's cheating. But yes.

**Jerold Santo:** I won't look...

**Gerhard Lazy:** Yeah, of course. Great.

**Jerold Santo:** Every time I'll go to the repo I'll be like "Oh, this is nice..."

**Gerhard Lazy:** We can give you 20 lines, Jerold. We can give you less than 20 lines. Yes, I think that's a very good idea. Yeah, \[unintelligible 00:42:23.08\] We'll Kaiden that, for sure.

**Jerold Santo:** Okay. Cool.

**Gerhard Lazy:** So I wasn't prepared to do this, but let's do it. So we have like a bunch of targets here... There's one that says "How many lines?"

**Jerold Santo:** Oh, my goodness...

**Gerhard Lazy:** \[laughs\] Right. So let's just run that live and see what happens. So how many lines -- I'm going to tap this... So let's see how many lines we have.

**Jerold Santo:** Okay. Almost a thousand.

**Gerhard Lazy:** 961. Hang on... Let's see what's in Varnish. Hang on a second... Oh, no. We don't want that. This is not correct.

**Jerold Santo:** We just want ours.

**Gerhard Lazy:** We just want ours. Okay. Shall we change this live? Alright, let's see what's going to happen.

**Jerold Santo:** Why not...?

**Gerhard Lazy:** Why not? So we want only VC -- actually, no.

**Jerold Santo:** Actually, that might work.

**Gerhard Lazy:** Varnish... No, we want inside VCL. So yeah, that's just like one change. So let's go adjust file... Do you want to do it?

**Jerold Santo:** Nope.

**Gerhard Lazy:** I feel like you're stepping in. Alright, so let's see. How many lines, how many lines... There you go. So Varnish, let's do Varnish... Alright, let's see that. Varnish -- sorry, VCL. Okay. Let's see if that works. There we go. How many lines? There you go. These are the actual lines. All the lines. So 364. That's like the main one. And these are like the includes. 24 in this one, and 106 and 15.

**Jerold Santo:** Right.

**Gerhard Lazy:** How many totals? Less than a thousand. I think it's less than a thousand. 500?

**Jerold Santo:** Yeah, is.

**Gerhard Lazy:** Getting to 500. Between 450 and 500, roughly.

**Jerold Santo:** A lot of these are just like static redirects.

**Adam Staravia:** Any savants out there? Do the math.

**Gerhard Lazy:** Say again?

**Adam Staravia:** Any savants out there? Do the math.

**Gerhard Lazy:** Look at that. 15... That's how we do it. 106 plus 24 plus 364. Look at that. 509.

**Adam Staravia:** 509.

**Gerhard Lazy:** 509 lines. So there we have our answer. Cool. So it's still good. Still good. Alright. So...

**Jerold Santo:** \[44:02\] Did you want to thank Nail?

**Gerhard Lazy:** Yes, of course. \[laughter\] Nail. How could I forget Nail? Of course. So one really important thing is that Varnish cannot terminate backends which have SSL in front. So if the backend is talking HTTPS, Varnish cannot use it out of the box. Varnish Enterprise and other products can, but the open source Varnish cannot. We did a bit of digging, and we realized -- that's how we learned about Paul-Henning Camp, PHK for short, and he was always against including SSL anywhere near varnish, because it would complicate things too much. SSL is really, really complicated. So with Nail's help, we wrote -- I don't know, he wrote 50, 60 lines of Go code that intercepts all the requests going to those backends, terminates SSL for Varnish, and presents the requests unencrypted. A really simple, elegant solution. One of the almost like sidecars that sits next to Varnish, and helps it terminate requests which need SSL. So I'm not sure if that's --

**Jerold Santo:** Does that do you justice, Nail?

**Adam Staravia:** Genius! Absolutely genius.

**Jerold Santo:** Let's hear it for him. Nail...

**Adam Staravia:** Good job, Nail.

**Gerhard Lazy:** Thank you, Nail.

**Jerold Santo:** ...and his SSL termination.

**Gerhard Lazy:** Thank you. TLS exterminator.

**Jerold Santo:** TLS exterminator.

**Gerhard Lazy:** That's the one.

**Jerold Santo:** That's a good name.

**Gerhard Lazy:** Cool.

**Break**: \[45:27\]

**Gerhard Lazy:** We improved it. We're here. We did it. Kaiden 20. One more thing... This is too far out. This is too far out. Too far. Actually, no.

**Jerold Santo:** We're good...
**Gerhard Lazy:** Yeah, we're good. We're good. We're doing good. Anything else you want to cover before we do this? There's one more thing that we're going to do.

**Adam Staravia:** \[47:57\] One more thing...

**Gerhard Lazy:** Kaiden 20. Any thoughts? Any comments from the... I mean, you're here. Do you have any questions? Do you have any comments? Do you have any thoughts? Anything?

**Adam Staravia:** We've got a question.

**Gerhard Lazy:** We're among friends.

**Adam Staravia:** Do you want to come to the mic?

**Jerold Santo:** Can we talk about how we're using Dagger?

**Gerhard Lazy:** Alright. Okay.

**Adam Staravia:** Alright...
**Gerhard Lazy:** So I can show you. How about that?

**Jerold Santo:** Yeah, show them.

**Gerhard Lazy:** Cool. So there is one very tiny change that I have here, which is using --cloud... This is an experimental feature that exists in the Dagger CLI. The reason why we do this is that we need a remote engine, a remote Dagger engine, so that everything that runs in the context of Dagger is quicker. Over Wi-Fi, it would be over -- my tethered connection would be very, very slow. So how we use Dagger -- in this case, let's go here. We have a couple of commands. The one I think that's the most interesting one, for example, for running tests. So let me show you what that looks like. I'm just doing test. You can see there it does like the --cloud. Let's see how fast it goes. It starts an engine in the cloud, it connects to it...

So we need to set up Varnish. We need to connect Varnish to all the backends, the TLS exterminator... And we want to do it in a way that is as close to production as possible. So it's almost like we want to run the system as it runs in production, but we want to do it locally. Okay, in this case it's a remote engine, but from the perspective of how it gets put together, it's literally just the same context of running containers. And because everything runs in containers, we get the exact reproducibility that we get in Fly. So you get the same configuration, the same Linux subsystem, the same kernel, or like a very similar kernel... And what that means -- I mean, in this case it's even using Firecracker behind the scenes, so it's very close to Fly... So we are able to test the system most accurately, and we're even able to run the system most accurately as it would do in production. And that part is hard, because whatever you do locally -- if I was running, for example, on the Mac, everything would be different. Even if I would have a VM, things would be different. So it's like that containers, the container image, the interaction between all the components... And when we ship something in production, it's as close as possible to that image; even down to the Go version.

So right now, for example what's happening here, we're pulling down -- I mean, some of it is cached. We're pulling down various dependencies, and you can see they're all Linux ones. So Linux, Linux... And again, a VM on a Mac - it gets you close, but it's not the same thing. You get like subtle differences. I'm not sure if that answers your question... Yeah? Cool.

**Jerold Santo:** Good use of Dagger... Any other questions before we do the big thing?

**Adam Staravia:** In the back...

**Gerhard Lazy:** I think Nail had one? Was it? Yeah.

**Jerold Santo:** Does Varnish only cache to RAM, or does it also use disk?

**Gerhard Lazy:** So it can use disk as well, but we don't have disk configured. So the configuration is cache to RAM only. It is the fastest one. If we have disks, as you know, the problem is the host - they can't move around. So it's no longer stateless.

That has certain challenges about placement... But also, disks tend to be a little bit slower. Not by much, but a little bit slower.

As an optimization, it would be worth exploring that, especially with NVMe disks, which is what we would get in Fly. So that is something as a future improvement, but right now everything gets served from memory, which is exactly what happens in Vastly as well. Because that's what gives you that highest performance.

**Jerold Santo:** So follow up to that... Our crash last night was because it needed more RAM than we allocated to Varnish. And in Varnish there's no way to say, "Just use all the RAM available." So if you tell it that, it uses more than it has available, because it tries to allocate more than you have... So you need to set an upper limit.

**Jerold Santo:** It can't know how much the machine has?

**Gerhard Lazy:** Well, it knows, but it doesn't do the allocation correctly.

**Jerold Santo:** Is that a bug?

**Gerhard Lazy:** \[52:06\] I don't know whether it's a bug. It's just not working well with the system available to the host.

**Adam Staravia:** That's a bug.

**Gerhard Lazy:** Maybe, maybe.

**Jerold Santo:** Varnish is how many years old?

**Gerhard Lazy:** 20-something.

**Jerold Santo:** 20-something. There's no way that bug is a bug. It has to be a decision.

**Gerhard Lazy:** Right. So I gained a lot of respect, for specifically in-memory problems, because they're very, very hard... I spent maybe three years optimizing memory allocations on the RabbitMQ team, for RabbitMQ, in the context of Erlang. And I've learned that there are so many subtle differences between how memory gets allocated on different runtimes... In the case of Varnish obviously it's C, so it's as efficient as it gets... But it's very difficult to know how much you should allocate ahead of time, and what you should free. Timing... Something has somewhere to give.

**Jerold Santo:** Sure.

**Gerhard Lazy:** And usually, what you need to do is over-allocate. Basically, you give it more than it needs, so that when you get these spikes... There's enough for it to spike so that it doesn't crash things over. Memory these days is cheap, so honestly, skimping on that is not worth it. And there are a couple of ways, we can go around it. Disks is one of them, limiting what Varnish can do, but also seeing if the Varnish memory allocation can improve. Because I know what it takes, for example what it took in RabbitMQ to do that... It took me years, and I was full-time on that. So it took a while... Including to understand what happens behind the scenes.

So you need to break it down in a way that you map and observe everything when it comes to memory allocation, and then you realize what needs to be tuned to your use case. That's the other thing. Because every context tends to be different. So the allocations, they are generic. To make them configurable to you or specific to you, so that they're optimized for your use case, it takes a bit of understanding of what you actually need.

**Jerold Santo:** Yeah. I'm probably reducing it down too much, but I feel like you could just say "This machine has four gigs. Just use three, and if you need more, you've got another gig in there."

**Gerhard Lazy:** Right, so --

**Jerold Santo:** "Just don't crash."

**Gerhard Lazy:** Yeah, true.

**Jerold Santo:** But my follow-up, I guess, would be - assume that we figure that out, that little dance...

**Gerhard Lazy:** Yup.

**Jerold Santo:** What happens when our instances become overwhelmed? Varnish might not be crashing, but maybe it's slowing down, maybe the machine's bogged, can't do stuff... Is there an autoscaled -- I mean, the answer is more RAM on the Fly instances, or more Fly instances in other regions, or in the same region...

**Gerhard Lazy:** That's right, yeah. So there is a big difference between regions, by the way... And this is the sort of thing that you only realize once you start using it. These are like the last 24 hours; I'm not going to refresh. It's a little bit outdated, like you can see here... It was 10.42 AM, so it was this morning before we started recording. And what you can see here is to this one, the San Jose, California, the SJC, is the one which shows the highest fluctuation. A lot of these, once they load up on memory, like Heathrow, they tend to be fairly stable... But then you have a few, for example this one, Santiago, Chile... This is like 2.3 gigs. So this one is not using all the available memory. This next one in Sydney is 1.84. And you can see that the memory is decreasing, because it doesn't need -- I mean, this is something... I'm not sure why it does this. For example, I wouldn't expect this line to go down. I would expect it to stay stable. So I'm not quite sure what's happening here. But this one, the lowest one, in Johannesburg, it's using 816 megabytes of RAM. So this shows you there is a difference between different regions and how many requests they need to serve.

**Jerold Santo:** Sure.

**Gerhard Lazy:** \[55:49\] So what I'm thinking is we should optimize for the regions that we have, and the ones which are busy, we should give them bigger instances, maybe beefier instances... But others like Johannesburg doesn't need that much. And the problem is you can't use different scaling strategies for different nodes, and they have multiple deployments... So it complicates things a little bit. But this is a refinement.

**Jerold Santo:** Yeah. I think we need more listeners in Johannesburg. I mean, what's up with that?

**Gerhard Lazy:** Exactly.

**Adam Staravia:** That's what I was thinking.

**Jerold Santo:** Alright, there was one other question out there, I thought...

**Adam Staravia:** It was back here.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** Okay. I like it. Okay.

**Jerold Santo:** Right. So the pads look like \[unintelligible 00:56:28.09\]

**Gerhard Lazy:** Right.

**Jerold Santo:** I forgot about that. Thank you.

**Gerhard Lazy:** Yeah. Thank you. Thank you very much. So we're looking at Honeycomb, and one of the integrations that we have in Pipe dream is we are sending every single request to Honeycomb, and some requests to S3. So we see what's happening with these instances. So what that means is we are able to -- for example, if I come back to the boards again... Let's hope the tethering works. It will be a little bit slow... Okay, so let's go Pipe dream requests, and I think maybe Pipe dream content, but let's go requests... We can see the get. Okay. And now we can slice them and dice them. The 404s and the 500s.

So maybe let's do -- let's do get. Okay. So let's go to the method... And the only thing that we need to do -- so this is one hour ago. So these are all the requests in the last hour. And we can say, "Give me the URL", which is what we've been asking. So group by URL. And what this is going to show us is the get, but also the number of requests. So what you see here is that the most popular request is podcasts feed, which got 203 requests in the last hour. And this is global. So we can do one more... We can say -- let me remove that, and let me remove requests... And let me do a data centre. So we can see which data centre is hit the most. So let's go that... And we can see that Frankfurt - 71 requests went to podcasts feed. Chicago, the next one, 47. San Jose, California... So these are the most requested URLs.

If we zoom out a little bit - let's look at the last seven days, so we get like a bigger perspective... \[unintelligible 00:58:19.03\] seven days... Okay, so you can see when it went live. So you can see that for some reason, this one - I don't know who this person is - uploads 9,500 times. Shall we go and check who this is? I don't think you'll know who this is. Avatars --

**Jerold Santo:** Somebody has a stalker.

**Gerhard Lazy:** ...people... Let's see. Okay. So let's go to Changelog.com... No, let's go -- where is it? Where was it? Not this one, this one... Okay. Copy that. Copy-pasting hard. Uploads... And I think this will be --

**Jerold Santo:** CDN.

**Gerhard Lazy:** CDN. There you go. So let's see who this is.

**Jerold Santo:** Ohhh...! \[laughter\]

**Gerhard Lazy:** You have a stalker, or a few. Who knows...?

**Adam Staravia:** Who is that guy?

**Gerhard Lazy:** Yeah, yeah. Do you recognize him? Who's this other guy? Like, 6QD. So that's Z4, as you say it over here. Alright, so let's see who was this next other person...

**Jerold Santo:** This is a fun side quest we're on right now...

**Gerhard Lazy:** Why not? There we go.

**Jerold Santo:** It's Ball!

**Gerhard Lazy:** Ball. There we go.

**Adam Staravia:** Ball. He was in on it.

**Gerhard Lazy:** Shall we keep going? Do you want to find who this person is?

**Jerold Santo:** Yes.

**Gerhard Lazy:** That's like the third most popular one, so we might as well...

**Jerold Santo:** Come on, be Adam. Be Adam...
**Gerhard Lazy:** Adam? Let's see... Alright. Let's try that... Uploads...

**Jerold Santo:** Nick. So somebody is loading maybe a JS Party page way too many times.

**Gerhard Lazy:** That's possible. But it will show up here if it was the case.

**Jerold Santo:** True...

**Gerhard Lazy:** But then we have like this randomness thing --

**Adam Staravia:** \[unintelligible 00:59:47.23\]

**Gerhard Lazy:** What's that?

**Adam Staravia:** Is dysfunctional doing something with... Something?

**Jerold Santo:** Oh, on their website? Maybe...

**Adam Staravia:** Because they're connected there.

**Gerhard Lazy:** You know what we could do? We could do user agent.

**Jerold Santo:** I think someone's hot linking us, man...

**Gerhard Lazy:** Let's do user agent, and we'll see where these requests are coming from.

**Jerold Santo:** It's going to be a robot.

**Gerhard Lazy:** Empty string.

**Jerold Santo:** Oh, you don't \[unintelligible 01:00:05.25\]

**Gerhard Lazy:** They don't want to be known. Okay. Shall we do --

**Adam Staravia:** Masquerading and hiding.

**Jerold Santo:** \[01:00:12.16\] Let's get to the San Jose URLs. This is what we were trying to get, right?

**Gerhard Lazy:** San Jose URLs. Okay. Let's do that.

**Jerold Santo:** Filter to San Jose, all URLs...

**Gerhard Lazy:** Okay... So it's not even here in the list, if you look at that. And look, this one has an empty string, so that's fascinating. We have somewhere an issue. So this needs to be. Or -- no, hang on. This was like when we were doing the testing, so maybe that's one not so much. Practical AI. Alright. Okay, so let's do server data centre equals SJC.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** Run query. And let's see what do we get. Most popular in San Jose...

**Adam Staravia:** \[unintelligible 01:00:42.04\]

**Gerhard Lazy:** Yeah, that's really cool, isn't it?

**Adam Staravia:** It's so awesome.

**Gerhard Lazy:** Look at that. Pocket Casts... This MP3 was requested a lot. 428 times. Is this the last episode?

**Jerold Santo:** Yeah, that one just went out yesterday, right?

**Gerhard Lazy:** There we go.

**Jerold Santo:** So it's just a popular episode in San Jose.

**Gerhard Lazy:** That's it.

**Jerold Santo:** Well, that's better than I thought it was going to be, which was a hacker...
**Gerhard Lazy:** Yeah. No, this is good.

**Adam Staravia:** Popular in Cali. Not a problem.

**Gerhard Lazy:** Look, Overcast. Pocket Casts and Overcast.

**Jerold Santo:** Yeah, they're just downloading stuff.

**Gerhard Lazy:** This is good. This is good traffic.

**Jerold Santo:** We love it.

**Gerhard Lazy:** Yeah. Nothing wrong with that.

**Jerold Santo:** Cool. Okay, any other technical or otherwise questions from the audience...

**Gerhard Lazy:** Comments... Anything.

**Jerold Santo:** ...before Gerhard does his big reveal? Alright, everybody wants to see what you got, Gerhard.

**Gerhard Lazy:** Alright. Let's do it. Cool. So coming back here... Just one more thing... This is the important one. No, that's something else. \[laughter\]

**Adam Staravia:** Oh, my gosh...

**Jerold Santo:** You flashed something...

**Gerhard Lazy:** Alright. I flashed something, yes. \[laughter\]

**Jerold Santo:** \[unintelligible 01:01:41.13\]

**Gerhard Lazy:** So what we're going to do now, we are going to shift all the traffic...

**Jerold Santo:** All the traffic.

**Gerhard Lazy:** ...to Pipe dream. So all the production traffic is going to go to Pipe dream. Shall we do it?

**Adam Staravia:** Get your podcasts --

**Jerold Santo:** Of course you should do it...! That's why we're here.

**Gerhard Lazy:** Alright. Okay, this is the moment. So all that we have to do -- this is how simple it is.

**Jerold Santo:** It's always DNS.

**Gerhard Lazy:** No scripting -- it is. No automation... It is DNS, it all comes down to that.

**Jerold Santo:** Yes.

**Gerhard Lazy:** We are going to delete these one by one.

**Jerold Santo:** These are the A records that you're pointing to...

**Adam Staravia:** Pause... Let me get my own recording of you doing this.

**Gerhard Lazy:** Go for it. Okay, Kaiden 20, in Denver. Let's do that.

**Jerold Santo:** This is going to be anticlimactic, because you're going to delete those, and then we'll be like... "They're deleted."

**Gerhard Lazy:** Theatre. Now, if this one goes down... So let's see if the system can handle all the loads, right? Like, what can happen? So after this, the only requirement is we walk away, okay? We do this thing, and we go for lunch, or something like that.

**Jerold Santo:** That's what's next, is lunch, I think.

**Gerhard Lazy:** Alright. So boom. We have four more to go. Three more to go. Sorry. After this one, three more to go.

**Jerold Santo:** It's not deleting.

**Gerhard Lazy:** It's not deleting. It's slow. It's my tether.

**Jerold Santo:** Shout-out to Unsimple. Big fans.

**Gerhard Lazy:** Thank you very much. One more, one more... Cool. And the DNS'ES, like one by one... So more and more requests are going to go to this one, which is the Pipe dream.

**Jerold Santo:** The Pipe dream.

**Gerhard Lazy:** Pipe dream. There we go.

**Jerold Santo:** Alright.

**Gerhard Lazy:** So delete...

**Jerold Santo:** So we're at one out of three... Now half our traffic will be going to Pipe dream.

**Gerhard Lazy:** Yup. Look at that.

**Jerold Santo:** And now 100%.

**Gerhard Lazy:** Well, we have one more. So we're 50-50...

**Jerold Santo:** What's this one?

**Gerhard Lazy:** That was it.

**Jerold Santo:** Oh, that's CDN.

**Gerhard Lazy:** That's CDN. We have to do the same thing for CDN as well.

**Jerold Santo:** Yeah, delete the CDN ones, too.

**Gerhard Lazy:** There you go.

**Jerold Santo:** Alright. So this is app requests now.

**Adam Staravia:** Is this goodbye to Vastly?

**Gerhard Lazy:** This is it.

**Adam Staravia:** This is the farewell to Vastly?

**Gerhard Lazy:** This is it.

**Adam Staravia:** This is a triumphal moment and a \[unintelligible 01:03:32.13\] at the same time.

**Jerold Santo:** Only if it works.

**Gerhard Lazy:** Only if it works.

**Jerold Santo:** If not, we'll have to go crawling back to them...

**Gerhard Lazy:** I may need to add these back... \[laughs\]

**Adam Staravia:** We still love you, Vastly.

**Gerhard Lazy:** If this crashes and burns, we'll have to go back, for sure.

**Jerold Santo:** \[laughs\] The good news is they have no idea what we're doing, so...

**Gerhard Lazy:** Yeah, exactly. And this is not a live-live show, so we're not streaming this, so it's okay.

**Jerold Santo:** That's right.

**Gerhard Lazy:** It's in this room.

**Adam Staravia:** Amongst friends.

**Gerhard Lazy:** If it doesn't work out, we edit this part out. So that's okay.

**Adam Staravia:** He always says that, we never do. Okay?

**Gerhard Lazy:** Cool. We ship it all. There you go. One more to go... I think this is one, and one more to go.

**Jerold Santo:** We're at 60-second TTLs, so this should be fast.

**Gerhard Lazy:** \[01:04:08.06\] 60-second TTL. They should be fast, yes.

**Jerold Santo:** Alright. If you can get your phone out and hit our website, please...

**Gerhard Lazy:** Yeah. Let us know how it goes, but that's it. We only have these two...

**Jerold Santo:** Let's generate some traffic.

**Adam Staravia:** Where's the real-time dashboard showing the activity?

**Gerhard Lazy:** Real-time dashboard, of course... Let's do that. Last 15 minutes... Let's see everything crash and burn...

**Adam Staravia:** Oh, my gosh... \[laughter\]

**Jerold Santo:** No --

**Gerhard Lazy:** What's the worst that could happen?

**Jerold Santo:** Well, the worst thing that could happen is all our Fly instances run out of memory.

**Adam Staravia:** Well, there are no peaks and valleys so far...

**Gerhard Lazy:** Let's go back to here. Let's go to the memory. There we go. Every one minute. Let's maybe go to the last one hour... So let's see. We had like a spike there, but that was... This is like 12:20, so I think it's still good. I think what we're going to see... So two things we're going to see. We're going to see -- let's come back here to the Pipe dream request. We're going to see a change... These requests will start going up. More and more traffic is going to start hitting. Look at that.

**Jerold Santo:** Oh, my goodness.

**Gerhard Lazy:** Boom. That was the spike right there. More requests getting resolved here... Status - still 200. That's good. So that's all good.

**Jerold Santo:** I'm going to our website.

**Gerhard Lazy:** And 404s, 500s... So things are looking good. Let's see, what else do we have? Let's load a few more boards. And the opposite is obviously in here \[unintelligible 01:05:15.06\] Nice. So it kind of works... Still...

**Jerold Santo:** It works on my machine...

**Adam Staravia:** It's so fast.

**Gerhard Lazy:** Vastly service stats... So these are Vastly service stats. The requests went up as well. I'm not sure what happened there. Why did they go up?

**Jerold Santo:** Because I just told everybody to go to it.

**Gerhard Lazy:** Right. I don't think we have that many people here. But still... Cool. So that's the requests... All good.

**Jerold Santo:** Playing mp3s...

**Adam Staravia:** Let's play a mp3. Latest show.

**Gerhard Lazy:** Nice. Let's do Pipe dream service... So there we have a few again. The cache, we can see things going up here... So this is last seven days. We'll need to zoom in a bit, so let's go 24 hours, so that we see the spikes. There you go. That was the spike.

**Adam Staravia:** And what is that spike?

**Gerhard Lazy:** This one is more hits. That's good. More hits. We're getting more hits. That's good.

**Jerold Santo:** More hits. So it will take time, because the real question is, was it all worth it? And the answer to that is, "Well, do we fix that cache hit ratio?"

**Gerhard Lazy:** Let's check it out.

**Jerold Santo:** That's the actual answer to the question.

**Adam Staravia:** What's the 17%?

**Gerhard Lazy:** Look at that, look at that. So let's go back to that. Let's look at last 24 hours...

**Jerold Santo:** 17% cache hits.

**Gerhard Lazy:** This is the homepage. That's the one that we're focusing on.

**Jerold Santo:** Sure.

**Gerhard Lazy:** So we're looking at the homepage, last one day we had 3,700 hits, and we had 33 misses.

**Jerold Santo:** I think that's better.

**Gerhard Lazy:** That's better.

**Jerold Santo:** It is better.

**Gerhard Lazy:** That's much, much better.

**Adam Staravia:** It is better.

**Jerold Santo:** We chained it.

**Gerhard Lazy:** How much better? We did it. No way. No way. Let's see.

**Jerold Santo:** Let's do the math on that.

**Gerhard Lazy:** 3715 plus 33... That's 99.1% hit rate.

**Jerold Santo:** Woo-hoo.

**Adam Staravia:** That's a lot of nines.

**Gerhard Lazy:** \[01:06:51.02\] Yeah. Two, to be exact... \[laughter\]

**Adam Staravia:** That's two nines...!

**Jerold Santo:** That's way more nines than we're used to...

**Gerhard Lazy:** More than we had. It was like 17%. 17%. So this is much better. Alright, so... Obviously, this will take a while for all the traffic to start shifting through... It is DNS, it's cached... But things - look at that. Things are happening. Things are happening.

**Adam Staravia:** So theoretically, 60 seconds later those TLS records should expire, and then require a new hit, which goes to a new route, which is through Ripely.

**Gerhard Lazy:** Changelog.com. And changelog.com, right now for me, it returns a single IP address. That's it.

**Jerold Santo:** Bam.

**Adam Staravia:** Because we're still in Ashburn.

**Gerhard Lazy:** No, this is the Pipe dream IP address. This is it. So this is one... And if I do changelog.com - now, this is the DNS that updates the quickest. That is the Google DNS. That's very fast. The Google DNS knows we're up. There's also -- I use DNS checker. Let's see if it's still a thing. It's been a while since I've used DNS checker, a service that tries to resolve the IP address from a couple of locations. More than a couple... Let's see. DNS checker, let's go Changelog.com... What is the -- we'll do CDN as well. Changelog.com... This is, I think, the important one. So all the DNS is San Francisco. I'm going to make this a little bit bigger, for everyone to see... That's the new IP address. We can see all the locations...

**Adam Staravia:** All updated.

**Gerhard Lazy:** So all of it is the new IPs. We don't see any of the old ones.

**Adam Staravia:** The world knows about what we did.

**Gerhard Lazy:** Yeah, I think so. They took notice. I think it's been good. I think. Yes, question. That is a fly.io IP address.

**Jerold Santo:** That was a fly.io IP address.

**Gerhard Lazy:** Let me show you that. So we have just IPs... You can see what IPs the CDN is using... And you will see that it's this IP address, which is a dedicated one... That's the IP that we're using. That's it.

**Adam Staravia:** Should they clap now?

**Gerhard Lazy:** Only if you want... Only if it was good.

**Jerold Santo:** You did it, Gerhard...!

**Gerhard Lazy:** Thank you, thank you.

**Jerold Santo:** Mind-blowing.

**Gerhard Lazy:** We did the thing.

**Jerold Santo:** We did the thing.

**Gerhard Lazy:** Thank you. Thank you, because you were a part of this. And we did it with you, and for you, and this was so good. Thank you very much.

**Jerold Santo:** Thank you. So a couple of special thanks... We've already thanked our Ripely folks... Thanks to a couple of Denver liaisons... Dan Moore. Is Dan here? Hey, Dan. How are you?

**Adam Staravia:** Dan...!

**Gerhard Lazy:** Good to see you. Thank you, Dan. And Kendall Miller. Did Kendall leave, or is he still sticking around? He left. He was here earlier... Thank you to you two for helping us find this theatre, for helping us connect with Nora again after all those years... We don't live here, and so I had no idea what I was doing or who I was talking to... So it's always awesome to have locals and friends willing to help out and make it awesome.

**Gerhard Lazy:** Yeah. It was great.

**Jerold Santo:** So that's our show...

**Adam Staravia:** One person didn't get thanked.

**Jerold Santo:** Yes.

**Adam Staravia:** Jason.

**Gerhard Lazy:** Oh yeah, Jason. Where is Jason?

**Adam Staravia:** Come up here, Jason...

**Jerold Santo:** Jason, come here. Jason's our editor.

**Adam Staravia:** He's behind the scenes, but he's very much part of this team. He doesn't get seen... He gets mentioned a lot, but critical, critical, behind the scenes here at Changelog. Thank you, Jason.

**Jerold Santo:** Thank you, Jason.

**Gerhard Lazy:** Thank you.

**Jerold Santo:** Alright. Anything else, Gerhard?

**Gerhard Lazy:** Thank you all. I really appreciate it.

**Adam Staravia:** Yes, thank you. We really, really appreciate all coming. Thank you.
