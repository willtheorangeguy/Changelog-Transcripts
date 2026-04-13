**Jerold Santo:** Alright, we are here to Kaiden once again, for the 11th time, second time on Changelog & Friends, and we're joined by our old friend, Gerhard Lazy. Welcome back, Gerhard.

**Gerhard Lazy:** Hi. It's so good to be back. It feels like I'm back home.

**Jerold Santo:** You're home here with us.

**Adam Staravia:** We have the comfy couch over there for you, that you can just sit back and relax... You've got the mic boom arm, you can bring the mic really close... You've got comfortable headphones... And of course, your favourite drink.

**Gerhard Lazy:** Yeah. It feels great. For you too, I hope, dear listener. If not, pause it, go and do your thing, and then resume.

**Adam Staravia:** That's right. So Kaiden - be always improving.

**Gerhard Lazy:** That's it.

**Adam Staravia:** Is that what we are doing? Are we improving? Or are we just making progress?

**Jerold Santo:** Hm...

**Gerhard Lazy:** My perspective? We are improving. \[laughter\] Now, what are we approving - let's talk about that.

**Jerold Santo:** What and how...

**Adam Staravia:** Okay...

**Jerold Santo:** Yeah, so we're trying to, for sure. That is the aim, is to continuously improve... And in order to do that, I guess you change things, right? You're like "Well, we've been doing x. Let's try y." And this is our new two-month cadence. It has been roughly two months since we've last recorded, so we're good there. It's the summer months, which for me at least a little bit is more time to do work on things, because less news, fewer events, fewer things going on. More vacations, which does slow us down. I think we've all taken a little bit of time. But Kaiden 11 - if you look at the discussion we have, which is discussion 469 on our changelog.com repository on GitHub - we'll link it up, of course, but Gerhard does a great job of outlining each Kaiden with its own discussion. This one's got a bunch of stuff in it, Gerhard. This is maybe the best Kaiden ever.

**Gerhard Lazy:** I think so. I really do. So many things changed. I couldn't believe it, because when you work on it, and it's like a week in, week out, you maybe add one thing, or maybe even half a thing... There were weeks when nothing happened.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** But then, two months are up, and you look at it, and you have like seven things, and some of them are huge. And you think "Whoa, that's a lot of things that changed." Did they improve, back to Adam's question? Well, let's figure it out. I mean, I always have my perspective, and I can share the things which I think improved... But for the listeners, what improved? And for you, Jerold, what improved, with Adam as well? ...when it comes to the app, when it comes to the service, did you notice anything improving? ...no. \[laughter\] Is that obvious?

**Jerold Santo:** I had to think about it... Front-facing features, maybe not so much. I mean, this has all kind of been infrastructure, backend... Of course, I'm always tweaking the admin and improving it for us... The biggest thing for me has been the change of how we deliver all transactional email through the application, which did introduce a very difficult to debug bug, which I haven't actually quite figured out yet; I just worked around, which we can talk about. But we're using Oban for all email delivery, which includes all of our newsletter delivery. So literally, for a while, the first step was just like, okay, when we send out Changelog News, we need to send that out with persistent background queue. We can't just ephemerally do that, because it's just a lot of emails, and you don't want to have something die midway through the process, and like half of our readers don't get their newsletters. We need to make sure that's robust. And so I put that through Oban. We also don't want it to be sending duplicates, which actually is kind of the bug that it's doing it anyway...

**Adam Staravia:** His face, you all. You missed his face in the video. So I saw his face and it was just hilarious. I had to laugh, sorry about that.

**Jerold Santo:** What did my face look like? Defeat? Was it utter defeat on my face?

**Adam Staravia:** It was just like, it was disgust, and defeat, and humour, at the same time.

**Gerhard Lazy:** Well, let's look at it this way. We're sending emails twice as hard. Twice is better than none. \[laughs\]

**Jerold Santo:** We laugh so that we don't cry, Adam. We laugh so we don't cry. The weird thing about this is that it's not like "Hey, everybody gets two emails." That would kind of make more sense.

**Adam Staravia:** It's just you, right?

**Jerold Santo:** It's not just me. I wish it was just me. It's a handful of people that get like 30-40 of the exact same email. It's like it's dequeuing them. I can't figure it out, but I just reduced it down to a single worker, because I had five workers going, and somehow it was just dequeuing. I'd love to figure that out. But right now we're back to okay. But yeah, it was very embarrassing. It's like a certain, a handful -- and one time it was our guest; I'm trying to think who the guest was. He was very gracious about it...

**Gerhard Lazy:** Solomon?

**Jerold Santo:** It wasn't Solomon, no. But maybe it was, and he didn't tell me about it... It's just like, you get 35 of this Thank-you email, versus one. But everybody else just gets one. Very strange.

**Gerhard Lazy:** We like you a lot. You don't have enough Changelog in your inbox.

**Jerold Santo:** We're DDoSing your inbox...

**Adam Staravia:** Yeah.

**Jerold Santo:** So that was a big change, and also a bit of a headache... But it did prompt me to finally do what I had said I was going to do last year, which was we signed up for Oban Web, which is supporting the Oban Pro cause. And we don't have that quite in place... Because I want more visibility in our background jobs, basically. The way I'm getting visibility right now is I proxy the Postgres server so I can access it, and I literally am looking at the table of Oban jobs, and doing things...

**Gerhard Lazy:** \[06:11\] Like a boss, straight in prod. Of course. \[laughter\]

**Jerold Santo:** As you do when you're the boss.

**Gerhard Lazy:** Real developers develop in production, let's just be honest about it...

**Jerold Santo:** You've got to do what you've got to do, man. I've got to see what's going on here, so...

**Gerhard Lazy:** You have to agree with that.

**Adam Staravia:** That's where the action's at, you know?

**Jerold Santo:** I would rather have the nice web UI, but right now all I have is a UI into the database table.

**Gerhard Lazy:** Now, because you mentioned that, that's the one thing which I didn't get to. It's on my list...

**Jerold Santo:** Ah... So close.

**Gerhard Lazy:** What else is coming up? It will not take long... But I had a good reason for it.

**Jerold Santo:** What's that?

**Gerhard Lazy:** I did all the other eight things. \[laughter\]

**Jerold Santo:** I guess that's good enough... You accomplished all these other things instead. Yeah. So the weird thing about that, and I guess the reason why I had to pull you in on it... Because otherwise -- so Oban Web is just distributed as an Elixir package... And the thing is, is because it's effectively an open core kind of thing, where he has Oban, which is a package which is open source and free, and all that, and then he has a subscription, it's distributed via its own Hex repository that he hosts, and has some sort of credentials... Which is fine locally, but then you have to somehow get that so that your CI, when it goes to install all the things to deploy, it can actually authenticate to his Hex server. And that's why I was like "Yeah, Gerhard should probably do this, because I'm not sure exactly how much Go code has to be written in order to get that done..." And so that's why I passed it off to you.

But yeah, I would love to have Oban Web for the next Kaiden, because it will help me figure out exactly what's going on with these duplicate emails. That being said, aside from that particular bug, it is really nice to have the persistence and the ostensible opportunity just to have a single send, versus if we have 15 nodes running the app, who knows who's going to grab that and just send it, right? So that's a big one for me, and the replayability of the emails, to resend in case of bounces, and stuff; we didn't have that before, so that's cool.

**Gerhard Lazy:** Right. So by the way, I hope this isn't a surprise, I would hate for it to be, but let's see what happens... We are running two instances of the Changelog, which means that even though you scaled down the worker to one, there will be two Oban workers running.

**Jerold Santo:** Right. That I do know, but I fixed it anyway... So I don't care at this point. It's working...

**Gerhard Lazy:** Amazing.

**Jerold Santo:** ...maybe. Listener, if you've gotten more than one email from us - and maybe 15, maybe 73 emails - do let us know. We want to know these things.

**Adam Staravia:** Oh, gosh. That's a lot of emails.

**Jerold Santo:** Yes.

**Adam Staravia:** So we're finally distributed then? We have two versions of the app, so we are finally telling the truth, in terms of we put our app in our database, close to our users?

**Gerhard Lazy:** So it's all in Ashburn, in Virginia, so it's all in US East, in that data centre. Now, we have the option of obviously spreading them across multiple locations, and we should do that. That's like the next step. So from one, we go to two; that is like a nice improvement. And then if that works, and we're happy with that, we can go to more, and that's the plan. But before we can do that, we should also obviously replicate the database. So we should have multiple followers - one leader, multiple followers - and then obviously, all the apps which are not running in Virginia, in Ashburn, they should connect their local Postgres follower.

**Jerold Santo:** So they're connecting closer to themselves.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** Versus back to the one in Virginia.

**Gerhard Lazy:** Exactly. And then we can even like remove shielding, for example, from Vastly. But that's a change which I didn't want to do before we had multiple locations. So right now we're like a single region, but more than one, which is already an improvement.

**Jerold Santo:** Right.

**Adam Staravia:** \[09:56\] Can we do a quick TL;DR/TL;DL of why it's finally happening? It's caching, basically, right? That's the reason why we haven't been able to replicate the application, was because of caching issues...

**Jerold Santo:** Yes, but no.

**Gerhard Lazy:** Yes and no. \[laughter\]

**Adam Staravia:** Okay, so not a TL;DL then... Give the short long version of that. Why?

**Gerhard Lazy:** So the Oban workers were an important part of that. So knowing that we're not basically missing important operations was essential. So because the jobs now are going to the database, when let's say the app stops halfway through doing something, that's okay; the other instance can pick up the job, and resume it, and send the email. In this case, 38 times. I mean, there's something there... \[laughs\]

**Jerold Santo:** Well, they're just overachievers. I always liked my code to go above and beyond, so...

**Gerhard Lazy:** So that was one. The other one, the caching side of things... I think it's okay if multiple backends have like different caches. I think that's okay. Obviously, we'll need to look into that as well. And this is back to you, Jerold... Where are we with that? Because I still don't know what is the plan after all this -- we've been back and forth for a year now, two years? We're getting closer, but we're not there yet.

**Jerold Santo:** Right. So one thing that we should point out in regard to this... I think the Fly machine upgrade to Apps v2 is pushing us into this new world. We did not at this point in our lives choose to go into this new world. And maybe Gerhard you knew the date better than I did, but we knew this migration was coming when Fly was saying "You have to upgrade to Apps v2." I just didn't realize it was going to happen when it did. And so I wasn't ready; the code wasn't ready. And the migration went through just fine. You did some work there, you can talk about the details of that work. We're now on Apps v2, and that allows us to run these multiple nodes at the same time. It requires it, really. Doesn't it require it?

**Gerhard Lazy:** So you can run just a single one... So a couple of things. First, this migration was like a progressive rollout. So certain apps of ours - we've received notifications like "Hey, these apps will be migrated to from v1 to v2 within like the next week." And then our app, the Changelog app - it required a blue/green deployment strategy. Blue/green was not implemented for Apps v2 until maybe a month ago, maybe two months ago... Something -- and actually, it was like a month ago. Because two months ago they didn't have this option. So a month ago, this was enabled. Shortly after, I think a week after, we received this notification, "Hey, this app will be migrated to v2." But the problem for us is that our deployment configuration - I wasn't sure whether it will work with v2. Because what they say is, "Hey, if you have a chance, try and save the Fly config after the upgrade, because some things may have changed in the configuration."

So in our case, we didn't have to do that. Everything continued working, which was a nice surprise... But when you go to v2 and when you go to Machines, or Apps v2, their strong recommendation is to run more than one. And the reason for that is the app will not be automatically placed on another host if a host was to have a physical failure.

**Jerold Santo:** Gotcha.

**Gerhard Lazy:** It doesn't happen that often, so on and so forth... But actually, the bigger the provider is, the more often it happens. So in our case, I think we would have been fine, but I wanted to make sure that we're running on two hosts, just to prevent the app going down, and then me having to basically jump into action and fix it. So that was, I think, pull request 457, and you can check it out on GitHub. So I was ensuring that the app deploys, they work on Fly.io Machines; I did a few small changes, a few small improvements. The Fly CTL, the CLI was updated, a couple of things like that... And then everything worked as it should have. The warning which you get in the Fly dashboard if you run a single instance, they say "We strongly recommend that you run more than one", and they explain in their documentation why. So it's basically a strong recommendation, and we did it.

**Adam Staravia:** \[14:12\] I see.

**Jerold Santo:** Okay, so we did... But I will now confess that we were not ready to do it. I didn't know we were doing it yet. And I did not fix the caching problem, which we did experience. So a few people mentioned, "Hey, this Go Time episode appears in my podcast app and then it disappears. And then it appears again." I call that flapping; I'm not sure exactly what it is. But basically, depending on which version of the app you're hitting, the cache may or may not be up-to-date. So the reason for this is that the way the code works is after you publish, or edit, or whatever, we go and clear the cache, which is just right there in memory, in the application server. And we do not clear the cache across all of our application servers, because we aren't good enough to write that code yet.

I do have what I think is the best case fix for this, which I learned from Lars Wickman, but I'm not going to exactly use what he built. I think we just should use the Phoenix Pub/Sub implementation. But in the meantime, I was like "Well, this isn't cool, so I'm just going to reduce our cache times." These are response caches. So you hit Changelog.com/podcast/feed. We deliver you an XML file of like multiple megabytes, right? We cache that right there inside the application, because it's not going to change. And we will cache it for infinity, until we have an update. Well, I just changed that to two minutes. And I was like "Well, we'll just cache it for two minutes", and every two minutes we'll go ahead and just regenerate, and we'll watch Honeycomb, and see if that puts ridiculous amounts of strain, and slows down our response times etc, etc, etc. This is behind Vastly, by the way; it's just that Vastly has a lot of points of presence, and every single one of them is going to ask for that file... And so there are still a lot of requests. That was just kind of good enough. It's working, things are fast enough, they're good enough; doggone it, people like us. So -- that's an old Stuart Smalley line, for those who missed it...

\[16:11\]

*Because I'm good enough, I'm smart enough, and doggone it, people like me.*

**Jerold Santo:** But that's not really a fix, it's just a workaround. It stopped the flapping, because basically, if you're out of date, you're only going to be out of date for 120 seconds, and then you're going to get the new file. And so that's what I'm doing right now. I'm just clearing the caches every two minutes, and so every app server is going to be eventually consistent every two minutes. I'd much rather have the solution that actually makes sense, which is clustered app servers that are Pub/Subbing an opportunity to clear their caches, and we can go back to infinity, because there really is no reason to regenerate that until there's an update... But for now, we're just doing every two minutes. That was my quick fix, and I was hoping that it wouldn't provide or require too much extra processing on our app servers. From what I can tell in Honeycomb - and I'm no expert - it seems like everything's okay. Obviously, not operating at full potential at the moment.

**Gerhard Lazy:** Yeah. So this is a very interesting thing that you mentioned, because one of the improvements that we did, we set up both Los that we were allowed to set up in Honeycomb - we can come back to why there's only two. So the first SLO is we want to make sure that 95% of the time podcast feeds should be served within one seconds. So in the last 30 days, that is our SLO. The second one is 98% of all responses should be either 200 or 300. So these are the two Los. Now, what we can do now is dig into the first SLO, which is 95% of the time the podcast feeds should be served within one second, and see how that changed since you've made the caching change. What I've seen is no change when I was looking at this.

**Jerold Santo:** Oh, good.

**Gerhard Lazy:** So I'm going to share my screen now... Make sure that --

**Jerold Santo:** That I audibly describe what we're looking at for our listener?

**Gerhard Lazy:** Exactly, and that I'm not missing anything important. So I will try to do this as good as I can...

**Jerold Santo:** \[18:04\] We're looking at Gerhard's screen.

**Gerhard Lazy:** Yes, thank you.

**Jerold Santo:** And this is a Honeycomb browser of podcast feed response latency. Go ahead.

**Gerhard Lazy:** That's it. So 95 -- so, all configured. Right now, the budget burned down - we are at -5.68%.

**Jerold Santo:** Is that good or bad?

**Gerhard Lazy:** Well, we've burned our budget, which means that more than 95 -- so you can see 94.72.

**Jerold Santo:** So we're failing.

**Gerhard Lazy:** 94.72% of the time we are serving our feeds in less than one second.

**Jerold Santo:** Oh, I can fix that. We just change the budget so that we pass it. \[laughs\]

**Gerhard Lazy:** Yeah, exactly. So that will be exactly -- so let's just agree on a new budget. That's it.

**Jerold Santo:** Yeah, exactly.

**Gerhard Lazy:** Yeah. But this is just like supposed to give us an idea of how well we are serving our feeds. Now, these feeds, as you know, they're across all podcasts.

**Jerold Santo:** And all clients all around the world, right?

**Gerhard Lazy:** Exactly. Okay, so now I'm sharing all of it, like the entire Brave browser, so I can basically open multiple tabs. So I was looking at the first one, 95% of the time. So regardless of whether cached or unbaked I have some saved queries here. So now we can see what is the latency of cached versus unbaked feeds. These are the last 28 days.

**Jerold Santo:** We're looking at hits and misses.

**Gerhard Lazy:** Exactly. When we hit them, it's more or less the elapsed time. So I can just drill down in these and I can see in the last 28 days they are served roughly within 0.55 seconds. So between half a second --

**Jerold Santo:** 550 milliseconds, yeah. We'll take it.

**Gerhard Lazy:** So let's go to the last 60 days and see if that changed. That shouldn't have changed, by the way. We have a few big spikes... And by the way, this is Vastly. So Vastly is serving these. We can see some spikes all the way to seven seconds. But overall, we're serving within half a second.

**Jerold Santo:** No big change.

**Gerhard Lazy:** So let's flip this and let's say "Show me all the misses", because this means it goes to the app, right? So --

**Jerold Santo:** 2.5 seconds.

**Gerhard Lazy:** That's it. So what we're seeing here - we can see how many of these requests went through. So we have about 2,000 in a four-hour period, 2,500, and we can see that latency-wise we are at 2.3 seconds, 2.8 seconds... It varies. But over the last six days - we have obviously an increase here, up to 4 seconds, 4.6 seconds, with July 9th. But otherwise, it hasn't changed.

**Jerold Santo:** Right. So my change was no big deal.

**Adam Staravia:** A nothingburger.

**Jerold Santo:** Which is nice.

**Gerhard Lazy:** Yeah. So here's the other thing... Let's have a look at the URL. I think this is an interesting one. So let's group them by URL, because what will be interesting is to see which feeds take the longest, like the P 95. And you can see all the misses. So this is the podcast feed. The P 95 is 2.9 seconds. Practical AI 1.5 seconds, but the one which has the highest latency is the Master feed. And I don't think that's surprising.

**Jerold Santo:** Not at all. If you actually just go download the Master feed - I just did it the other day - it's about 11 megabytes. I mean, it's a gigantic file.

**Gerhard Lazy:** Yup.

**Jerold Santo:** And we're recalculating the contents of that once every two minutes. Every other time, it's just sending the file. But even just sending that file from - I guess it's from Fly to Vastly - is just going to take some time. And then sending it from Vastly, obviously, to wherever it goes - well, that's up to Vastly. But the only way we can make that faster - there are two ways I can think of. One is you cache it forever. So you just get rid of that calculation time, which happens once every two minutes, right? Then all you have is send time. We're already doing GZIP and whatever else you can possibly do in terms of just HTTP stuff... The only way you can make it faster is take stuff out of it, I think.

**Gerhard Lazy:** Yeah, limiting it.

**Jerold Santo:** And we used to do that. We used to limit it, because I think we have over 1,100 episodes in there, and there's everything, pretty much. Not the transcripts, thankfully. That would really balloon it up. But chapters, etc, etc. There's lots in there. Show notes, links, descriptions... All the stuff, for every episode we've ever shipped. The only way to make that smaller is you just limited it to N episodes, where N is some sort of number like 500, or 100. We used to do that. I would happily continue doing that if the podcast indexes would just keep our history. But they won't. They'll purge it. And then you'll go to our Master feed, and you'll see 100 episodes. And you'd be like "Cool, they have 100 episodes." Like, no, we've put out 1,100+ episodes. We want people to know that, we want people to be able to listen to them...

\[22:31\] We used to have complaints, "Hey, why don't you put the full feed in there?" There is a feature called paginated feeds. It's a non-standard RSS thing that we used to do, and we paginated that, and it was a much smaller thing, and it was great... Except Apple Podcasts didn't support, Spotify didn't support it, blah, blah, blah. It's that old story. So I was like "Screw it, I'm just going to put everything back in there, and it's just going to be expensive and slow", and that's what it is. What do you guys think about that? Is that a good trade-off, just leave it? Because it's an 11-megabyte file. I don't know... What do you do?

**Gerhard Lazy:** Well, I think that serving the full file is important for the service to behave the same. So I wouldn't change that. If you change the file, it will appear differently in these players... So I don't think we should change that.

**Jerold Santo:** If they all supported pagination, I would happily paginate it every 100 episodes or so, and we'd have a bunch of smaller files that are all faster responses. I would love to do that, just like you do with your blog. But you can't make these big players do the cool stuff. They never do the cool stuff. They always do what they want to do, so...

**Gerhard Lazy:** But I think that's okay. So if we look at how long it takes to serve this master feed from Vastly, from the CDN directly, versus our app... So when it's a cache hit, when it's served directly from Vastly, we are seeing a P 95 of 2.7 seconds.

**Jerold Santo:** Okay.

**Gerhard Lazy:** When our app serves it directly, it's 9.9 seconds. So it's roughly three times slower. I don't think that's so bad. Our app is three times slower than Vastly. I think that's okay.

**Jerold Santo:** I also think with this kind of content it's okay. If this was our homepage, this would not be okay. If we had humans consuming this, it would not be okay. But podcast apps, crawlers... Like, "Oh, sorry, you had to wait three seconds to get our feed." Who cares? You're a crawler, you wait around until there's the next one.

**Adam Staravia:** Yeah.

**Jerold Santo:** So the fact that we have slow clients and clients that aren't people, they're actually just more machines consuming it, I have less of a problem with that being just not superfast. If this was our homepage, it'd be all hands on deck until we get it fixed. There's no way I'd make people wait around for this kind of stuff.

**Gerhard Lazy:** What I'm wondering if we can improve this is do we care about the cache hits, or do we care about the cache misses? Because based on the one that we care about, we can maybe see if there are some optimizations we can do about -- cache hits I'm not sure what we can improve, because it's not us, it's basically Vastly.

**Jerold Santo:** I'm not either.

**Gerhard Lazy:** But cache misses - and I think this is something fascinating. If I dig into Honeycomb, into the cache misses, you will notice something interesting. You will notice that there was quite some variability... So it would take anywhere from 4 seconds to 15 seconds, like we see with the squiggly lines. But then from August the fourth we are seeing five seconds, eight seconds, six seconds... So it's less spiky, and it seems to keep within 10 seconds. So there seems to be an improvement. So I'm wondering what changed there. Did something change on August the fourth? I have a hunch, and I'm going to see if it's that. I'm not sure.

**Jerold Santo:** August fourth - I'm looking at the commits on August fourth. Run Dagger engine as a Fly machine... That was your commit on August fourth.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** And that was the only one, in terms of things that might have gone live.

**Gerhard Lazy:** Well, I think August second... That's when I commented -- this was merged last week... We upgraded PostgreSQL.

**Jerold Santo:** \[26:03\] We upgraded Postgres on August second?

**Gerhard Lazy:** Yup. Went from Postgres 14 to Postgres 15.

**Jerold Santo:** It's possible, because the app is hitting the database -- not on every miss, but every miss once every two minutes. And that's going to be really slow. And so that could slow down on the requests. So if Postgres is getting our data back out faster somehow, because of some sort of optimization that they did - which I could certainly see - then that might be what explains that. Because there's no application changes from us.

**Gerhard Lazy:** So again, all these other pull requests... I mean, we went from AWS S3 to Cloudflare - again, I don't think that's related now.

**Jerold Santo:** No.

**Gerhard Lazy:** And that happened on --

**Jerold Santo:** It was just over the weekend.

**Gerhard Lazy:** Three days ago, August 7th. August 5th, actually. So that happened after our improvement.

**Jerold Santo:** But that wouldn't have anything to do with the feeds. That's the mp3 themselves, but not the feed files. Well, cool. So Kaiden, right? So we upgraded Postgres, and we got a little bit faster in our cache miss responses on our feed endpoints. Well, let's just wait till they do Postgres 16. It will get even better, you know?

**Gerhard Lazy:** Yeah, I'm just trying to see if this impacted others. So let's go maybe last 14 days, just like to see this a little bit better. I'm looking at the cache misses, and it's difficult for me to see right there at the end, the last seven days... I think it was just the Master feed that's improved. Furthermore, I mean, that's the one that there's some improvement there. But in this view it's difficult to see the P 95. Miss, miss... Go Time feed... I mean, maybe we can just zoom in that. I mean, do we want to continue doing this, or shall we switch topics?

**Jerold Santo:** I don't know. Adam, how bored are you at this point?

**Adam Staravia:** One more layer. One more layer.

**Jerold Santo:** Okay. Oh, he's never bored. He's always going to go one more. Alright, peel the onion...

**Gerhard Lazy:** So this one seems to have not changed. So the Go Time feed hasn't changed. If anything, it looks slightly worse here. But again, we would need to continue digging to see "Hey, what client?", which data centre it's coming from, things like that. Maybe it's location specific, right? It's a client, for example, from Asia, which is going to Ashburn. Obviously, that's going to be slower. We have a few clients from a certain geographical region...

**Jerold Santo:** Getting routed to the wrong place, yeah.

**Gerhard Lazy:** ...which would add to this latency. Exactly, routing differently, or whatever. But the Master feed is improving, which is, by the way, the one that takes the longest. I think that's a good one.

**Adam Staravia:** And the improvement was around eight seconds, roughly, plus or minus?

**Gerhard Lazy:** Yeah. Roughly eight seconds, yeah. I mean, in terms of percentages, it's more than 2x. 3x. Almost 3x faster. So that's a huge one.

**Adam Staravia:** So to kind of zoom back out a little bit, Jerold, you're saying the perfect world would be a Pub/Sub multi-geo application to know if the update should happen and do it indefinitely... Or infinitely I think you said. Versus this temporary you weren't ready necessarily to version from v1 to v2 Apps, and then you made it update every two minutes, instead of infinitely, because that would obviously have the cache issues we have with clients.

**Jerold Santo:** Yeah, exactly. There's no reason not to cache forever because the file doesn't change until we trigger a change by updating something.

**Adam Staravia:** Right. When it updates, we update it and then cache it again, forever.

**Jerold Santo:** Exactly. And right now, when we update it, we clear the cache. But it only clears it on the app server that's running the instance of the admin that you hit. The other app servers that aren't running that request don't know that there's a new thing. Well, with Phoenix Pub/Sub and clustering, you can just Pub/Sub it; you don't even have to use Postgres as a backend, which is what Lars Wickman's solution does... And you can just say, "Hey, everybody, clear your caches", and they'll just clear it that one time. And then we never have to compute it until we're actually publishing or editing something. So that's darn near as good as a pre-computed. Because I know there's a lot of people out there thinking, "Why don't you just pre-compute these things? This is why static site generators exist", etc. Because that is just a static XML file, effectively, until we change something.

\[30:07\] That's a different infrastructure, that's a different architecture that we don't currently have... And so it's kind of like Easy button versus Hard button. I've definitely considered it, but if we can just cache forever, and have all of our nodes just know when to clear their caches, then everything just works hunky-dory. For now, we'll just go ahead and take the performance hit, recalculate every two minutes... That seems to be not the worst trade-off in the world looking at these stats... But that would be a way of improving these times.

**Gerhard Lazy:** But now that you mentioned that, when we used to cache, when we used to have a single app instance, I didn't see much better times. The feed was being served in more or less like the same time, right? This is the Go Time feed when he had misses, so let's go with 60 days. In a 60-day window, it was just under two seconds, and it hasn't changed much, even when it was cached.

**Jerold Santo:** That's weird.

**Gerhard Lazy:** So what I'm wondering is, again, going back to like generating these files - could we upload them to our CDN? And our CDN -- by the way, we have two...

**Jerold Santo:** Of course.

**Gerhard Lazy:** This is another thing to talk about. We have Cloudflare, R2... So could we upload the file to R2 and serve it directly from there?

**Jerold Santo:** Yes, that was one of my other architecture options, is doing that. You have a lot of the same problems in terms of like updates, and blowing things away, and all that... It's definitely a route that we could go. We have a dynamic web server that is pretty fast, and is already working... And so just running the code at the first request to me makes a lot of sense. But we can certainly, at the time of update, or publish, or whatever it is, go ahead and run all the feeds, pre-compute them, and upload them somewhere.

**Gerhard Lazy:** I'm thinking Oban. We want more Oban, right?

**Jerold Santo:** We could...

**Gerhard Lazy:** And it doesn't matter which instance picks up the job, and which instance uploads the feed... Ultimately, one of them will upload the feed on our CDN, and that will be that.

**Jerold Santo:** So one thing we don't want to change is the URLs to our feeds... And our URLs to our feeds currently go to the application. And so the application would have to be wise to say, "Does this file exist already on R2?" And if it does, serve it from there. If not, serve it myself.

**Gerhard Lazy:** No, because remember, we have Vastly in front. So we can add some to rulings to Vastly to say "Hey, if this is a feed request, forward it to R2, don't forward it to the app."

**Jerold Santo:** What if R2 doesn't have the file, for some weird reason?

**Gerhard Lazy:** Well, it will, right? It will have like an old one.

**Jerold Santo:** That's what you think... What if it doesn't?

**Gerhard Lazy:** Well, you've already uploaded the file once. You're just updating --

**Jerold Santo:** Well, we have to blow it away... Maybe it's just a race condition at that point.

**Gerhard Lazy:** Why can't you just re-upload it? You're doing a PUT.

**Jerold Santo:** Well, that's true. Is that atomic? I guess that's at that point atomic.

**Gerhard Lazy:** It should be. I mean, the file is already there. You're just basically updating an existing object, because it's an object store.

**Jerold Santo:** Right.

**Gerhard Lazy:** You're saying "Hey, there's this new thing. Just take this new thing", and then the new thing will be served.

**Jerold Santo:** Okay. Yeah, we could definitely try that route. And then we'll just turn off caching at the -- well, our application server would never even --

**Gerhard Lazy:** Never see those requests.

**Jerold Santo:** So we would lose some telemetry that way, because we are watching those requests from the crawlers. Because some crawlers will actually report subscriber counts...

**Gerhard Lazy:** I see.

**Jerold Santo:** And so our application's logging subscribers, which is a number that we like to see, from those feed crawler requests. So if we lose that visibility, may we could get it at the Vastly layer somehow...

**Gerhard Lazy:** Vastly logs everything to S3.

**Jerold Santo:** We're putting more and more stuff into Vastly at this point as well, so I'm tentative... I like to have everything in my codebase, if possible.

**Adam Staravia:** The folks at Cloudflare right now are really upset by this conversation.

**Gerhard Lazy:** Well, we're using Cloudflare behind, so... That's there. \[laughs\]

**Adam Staravia:** I know. But we're not using their stats. We're not using -- the more entrenched we are to Vastly's way of things, they're like "No, that's the dark side!"

**Jerold Santo:** Right. And the Vastly folks are probably thinking "You're using Cloudflare. No! That's the dark side!"

**Gerhard Lazy:** \[34:02\] Yeah. Well, we're using both. \[laughs\] So we have two CDNs.

**Adam Staravia:** But we're using them differently though, aren't we? Aren't we using them differently? Like, we're using R2 simply as object storage, not CDN necessarily.

**Jerold Santo:** That's right. We replaced AWS with Cloudflare. Not Vastly with Cloudflare... So far. Who knows where we go from here? But let's talk about this migration, because this was a big chunk of work that we accomplished...

**Adam Staravia:** Yeah.

**Gerhard Lazy:** Well, the first thing which I want to mention is that you've made this list, which really helped me. It was like a great one. I wasn't expecting it to be this good... No, I was. I'm joking.

**Jerold Santo:** Aw...

**Gerhard Lazy:** No, no, no. I was. I was.

**Jerold Santo:** This is better than I normally do. I was like "You know what? Let's open a pull request. Let's do this the right way."

**Gerhard Lazy:** Yeah. I was surprised just by how accurate this list was. I was like "Wow, Jerold knows a lot of things, like how this fits together. Furthermore, I'm impressed!" \[laughter\] So I genuinely appreciated you creating this... By the way, this is pull request 468 if you want to go and check it out. I mean, you created like the perfect, like "Hey, this is what I'm thinking. What am I missing?" And actually, you didn't miss a lot of things.

**Jerold Santo:** Good.

**Gerhard Lazy:** So we went from S3 to R2, whereas you know, we're using AWS S3 to store all our static assets; all the mp3s, all the files, all the JavaScript, and the CSS, and SVGs, and all those things... And we migrated, might I say with no downtime, like zero downtime...

**Jerold Santo:** Zero downtime...

**Gerhard Lazy:** ...on a weekend, as you do... I was sipping a coffee, "Okay, so what should I do this weekend? How about migrating hundreds of gigs from S3 to R2?" And it was a breeze. It was a real breeze.

**Jerold Santo:** That's awesome.

**Gerhard Lazy:** And your list played a big part in that, Jerold. So thank you for that.

**Adam Staravia:** That's good stuff. Wow. Let's put a little clap in there. \[clap 00:35:46.08\]

**Jerold Santo:** Thanks, guys. I appreciate that applause. I'm looking at number six, make sure we can upload new files - and you didn't do that yourself, but you can check it off, because I just uploaded Changelog News yesterday, and everything worked swimmingly. We published a new mp3 file without any issues whatsoever.

**Gerhard Lazy:** Amazing!

**Jerold Santo:** Where should we start? Should we start with why on this one? I mean, I think --

**Adam Staravia:** Well, why is easy, right?

**Jerold Santo:** Maybe Adam can cue up with why here...

**Adam Staravia:** Well, I just pay attention to how much money we spend... \[laughter\] \[unintelligible 00:36:13.11\]

**Jerold Santo:** That's right. Every dollar comes out of our bottom line pretty much, right?

**Adam Staravia:** And I was like, "Why is this doubling every so months?" And it had been very, very small for so long; like, sub 10 bucks for a very long time. In the last year or so it's gotten to be 20, 30, 40, 50... And then recently, it was over 100. I think about six months ago. A few Maidens ago. And I'm like "Why?" And we couldn't really explain exactly why. But then we explained some of it. But then it only went down a little bit. I think it went back down to like 120 bucks. But that's a lot of money to spend on object storage. It's just -- it's more than we want. And we didn't get free egress... Well, you take free egress.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** So one theory you mentioned -- I think we actually got to 150 at one point. Maybe the last time we recorded Kaiden. Which really was like "Okay, let's make some moves here, because--"

**Adam Staravia:** Yeah, because if it goes to 300... Like, if it doubles from 150 to 300, that's an issue.

**Jerold Santo:** So I knew that it'd be a bigger lift to migrate our entire application, which is the bulk of it because of all of our mp3... Which Vastly of course is serving them, but we are putting this as the origin for Vastly, and so it's requesting them from S3 for us... And that was the major cost, was like outbound traffic; the major cost on S3. And so we knew with R2 we'd had zero on that... This took two months-is from then; like, when we actually landed this. It was almost two months from us realizing that we should do this. However, Changelog. Social, which is a Mastodon app server, was also on S3. And I immediately switched that one over to R2, just to try out R2. And it was superfast and easy to do that. And I think we went from 150 down to 120... It started to drop precipitously after that, and I think it's because of the way the Fediverse works. When we upload an image to Mastodon, as I do with my stupid memes and stuff, and we put it out on our Mastodon server - well, that image goes directly from S3... Oh, I put Vastly in front of it too, I thought. I might have. But somehow, that image is getting propagated around, because all the Mastodon instances that have people that follow us have to download that image for them to be able to see it.

\[38:26\] And so this architecture of the Fediverse, where it's all these federated servers - they're all having to download all those assets. And so I think maybe that was a big contributor to that cost, was just changelog.social. And once I switch that, it started to come down. And now it's going to go to pretty much zero because of this change.

**Gerhard Lazy:** Yeah, it will be just a few dollars. And I think we have a few things to clean... So I basically enabled Storage Lens, which is an option in S3. And you can dig down, so I'm just going to once again share my screen, I'm going to click around for a few things, I'm going to come back... 2469. Obviously, you won't have access to this, but if you're using AWS S3, you can enable Storage Loans and have a play around with it.

So what I want to see is here, extended Storage Lens. Okay, and now it loads up, and we can see where the cost goes. So we can see the total storage, we can see the object count, we can see the growth and how things are changing, and how many more things we're adding... This was in the last day, today, all requests, like month to month... So you can see we have a 1% change in total storage month to month. So we're approaching the one terabyte mark; not there yet, but getting there quickly. And if we see which are the buckets that contribute, and I have to remember -- where was I? Oh, there we go. So we can see Changelog assets, which are the static ones; they contribute 22%. Changelog Uploads Jerold, they contribute 21%. This is the storage costs. And Changelog.com backups, which is mostly Nightly, they contribute, again, 20%. So they're like roughly evenly spread. So I'm wondering, is anything here that we can clean up? Anything here that we don't need?

**Jerold Santo:** Well, we can get rid of Changelog Uploads Jerold, because that was my dev environment. Basically, I would mirror production with the assets, so that I had the most current assets... Because I like to do that when I'm developing, have it look real. And so I just had this AWS S3 sync command that would just sync from /assets to mine, which is why they're roughly the same amount of gigabytes. I probably haven't run it in a while.

**Gerhard Lazy:** I see.

**Jerold Santo:** And so that's all moved over to R2. So that whole bucket could just get blown away.

**Gerhard Lazy:** Okay. Should we do that now live?

**Jerold Santo:** Yeah, let's do it.

**Gerhard Lazy:** What's going to happen, right? What's the worst thing that can happen?

**Adam Staravia:** Do it live!

**Jerold Santo:** Like some sort of ta-da sound?

**Gerhard Lazy:** Right. Boom, everything explodes. So I think we won't be able to do that. We'll need to delete the individual objects, by the way...

**Jerold Santo:** Ah, you can't just delete a bucket? What's wrong with these people? It's too dangerous.

**Gerhard Lazy:** I remember this again, this not being possible... So let's -- again, let me search for Jerold. I've found the bucket. So we select it... Let's say Delete. And to confirm, "Buckets must be empty before they can be deleted."

**Jerold Santo:** Ah, you know what? R2 has the same exact thing, because I created a test bucket... I tried to move our logs over there as well. That failed. Maybe we can talk about that. But I couldn't delete it without emptying the bucket first. And, I'll say this - R2 does not have the ergonomic tooling that's built up around S3. And so in order to delete all the objects inside the R2 bucket, we're talking about you're writing JavaScript, basically. There's the GUI apps, the tools... All that stuff isn't there. And it's API-compatible with S3, but not really. It kind of goes back to our conversation, Adam, with Craig Keratins about "Postgres compatible isn't actually Postgres compatible."

**Adam Staravia:** Yeah.

**Jerold Santo:** \[41:46\] Cloudflare's S3 compatible API is not 100% compatible. It's like mostly, but enough that certain tools that should just work, don't. So Transmit, for instance, which is a great FTP -- it started off as an FTP client; it has S3 support... I think I complained about this last time we were on the show, so I'll make it short... But it doesn't support R2 because of like streaming uploads, or some sort of aspect of S3's API that R2 doesn't have yet. So anyway... I haven't deleted a bucket from our R2, because you have to actually highlight all, and then delete, and it paginates, and then you're like Okay", and there are thousands of files. How do you delete them from S3? Just open up an app and select all and hit Delete, or what?

**Gerhard Lazy:** Well, I think I would try and use the AWS CLI for this...

**Jerold Santo:** You would?

**Gerhard Lazy:** Yeah. That's how I'd approach it. And I think just like that, I would maybe script it; like list and delete things as a one-off. Now, I would try to Transmit to see if that works. I mean, we're talking S3 now, right? So--

**Jerold Santo:** I just opened it up in Transmit and hit Delete.

**Gerhard Lazy:** Yeah, I'm doing the same thing now to see if I can delete it from Transmit.

**Jerold Santo:** Oh, it's going to be gone already. I already did it. That's why nice GUI apps are just for the win. I just opened it up in Transmit, select all... Hopefully I did the right bucket. It was pretty fast.

**Adam Staravia:** All you had was just the uploads folder in Changelog Uploads Jerold, right?

**Jerold Santo:** There was a static folder, but it's already gone, because I've just deleted it...

**Gerhard Lazy:** Nice.

**Jerold Santo:** You'd better look at it quick, because it's going away... That's why it'd be great to have a Transit for R2. So somebody out there should build a little Mac GUI for R2. You can call it D2.

**Adam Staravia:** I believe somebody said they wanted to call it D2. Was that in Slack or Twitter?

**Jerold Santo:** That was on Twitter. Jordi Mon Companies, who's a listener, and one of the hosts of Software Engineering Daily. We know Jordi... He's the one who said "Call it D2." I was like "That's a good idea."

**Gerhard Lazy:** That'd be a good one.

**Adam Staravia:** Is it Jordi?

**Jerold Santo:** Yes.

**Adam Staravia:** In my brain I've had it mapped to Jury.

**Jerold Santo:** It could be Gordy. It's a J name that, you know, whenever someone's potentially around the world, J's are pronounced differently. But he's from the UK... I don't know. I'm going to go with Jordi.

**Adam Staravia:** Okay.

**Jerold Santo:** Yeah, call it D2. Write it in Kauri... We'll cover it here on Changelog News, of course. But yeah, R2 is just too new to have all the great tools. I mean, S3 just has everything.

**Gerhard Lazy:** Yeah. It's been around for a while, for sure. So what I wouldn't delete - I wouldn't delete the Changelog assets on S3. I mean, we can consider that our backup.

**Jerold Santo:** Backup, yeah.

**Gerhard Lazy:** If something was to go catastrophically wrong with R2 - and I don't expect it to happen, but you know, better be safe than sorry. I mean, we can keep those 100 and whatever, 200, or however many gigs we have in S3 for this... We won't be doing any operations against them, so it shouldn't cost us much other than storage space. And continue using R2... Maybe even set up a sync between R2 and S3, so that we have a backup to the backup, or like a backup to our new CDN, in a way, so that will be good... But yeah, I think that's a good idea. So we are on R2. We did it, and it was a breeze.

**Adam Staravia:** Why not consider B2?

**Jerold Santo:** Like Back blaze?

**Adam Staravia:** Mm-hm. Versus S3.

**Gerhard Lazy:** So I listened to the episode... By the way, great episode. Loved it.

**Jerold Santo:** The Back blaze episode?

**Gerhard Lazy:** The Back blaze episode. And I'm using them, and I have been using them for many, many years. When I've set up my Kubernetes backup strategy - by the way, I have a Kubernetes cluster in production. That's a thing. And all my workloads are now running on Kubernetes. We can talk about it later.

**Adam Staravia:** In your home lab?

**Gerhard Lazy:** No, no, no. In production.

**Adam Staravia:** Okay.

**Jerold Santo:** For Dagger, or...?

**Gerhard Lazy:** Well, what that means - I mean, I've been hosting a bunch of websites for decades.

**Jerold Santo:** Oh, that's right.

**Gerhard Lazy:** So it's mostly WordPress websites, some static websites... We're talking 20 websites. I won't be giving any names; again, they're like longtime customers...

**Adam Staravia:** BBC...

**Jerold Santo:** Nytimes.com...

**Adam Staravia:** That's right.

**Gerhard Lazy:** That's it. That's it. BBC... All of them.

**Jerold Santo:** TheVerge.com...

**Gerhard Lazy:** All of them. Yeah, exactly. So I've set up this production cluster... I mean, this was the second one. I set it up in June, and I've been hosting these workloads. Furthermore, I was using a lot of DigitalOcean droplets. Furthermore, I had about 10. So all of these I consolidated in two bare metal servers. And they're running Talos, and it's all production. So obviously, production needs backups and it needs restores. So what I did when I was migrating between Kubernetes clusters, these workloads - the backups were going to B2. And B2 was okay, but slow. Sometimes unexpectedly slow.

\[46:16\] I have the same feedback from Transistor FM. I had them on Ship It, and they were saying some operations on B2 - sometimes they're slow. So they can take minutes instead of seconds. And that was my experience as well. Restoring things from B2 was incredibly slow. So it took me 30 minutes to restore like 10 gigs, roughly... And that's not normal.

So what I did, I said "Okay, I have to try R2." I tried R2. Same restore - three minutes. So there's a 10x difference between B2 and R2 in my experience. Again, it's limited to me. So that's why for big restores I'm restoring for R2, but of course, I'm using both B2 and R2, because I have two backup mechanisms in place.

**Jerold Santo:** Of course.

**Adam Staravia:** The reason why I suggest or even ask B2 versus S3 is if it's only for backup, B2 based on their pricing page is 0.005 cents per gigabyte per month. And S3, if this is accurate, is 0.026, which is five times the cost per gig.

**Gerhard Lazy:** Yeah.

**Adam Staravia:** So if it's just backup, we can deal with slowness, right? I mean, if it's a restore, we can deal with slowness. We could just buffer that into our mental space. And then keep five times our dollars.

**Jerold Santo:** So here's a question related to Kaiden, infrastructure and whatnot. If we were to say, okay, well, we want a backup service that takes R2 things and puts them to B2 once a day, or once a week. Or even if it's just a mirror, just constantly mirroring... Where would we put that? Where would it run? How would it work?

**Gerhard Lazy:** We could write an Oban worker for it...

**Jerold Santo:** True.

**Gerhard Lazy:** What I would do is I would solve it as a CI/CD job, yeah.

**Jerold Santo:** So it'd be a customer robotic arm inside our Dagger.

**Gerhard Lazy:** That's it.

**Jerold Santo:** And it would pick it up, and it would move it and drop it...

**Gerhard Lazy:** It would be GitHub Actions, and it will just run there. We could have an Oban worker as well. I mean, whatever we're more comfortable with.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** But then should our app know about this? Maybe it should. I mean, it has access to all the credentials...

**Jerold Santo:** It's easy in terms of secrets and stuff. It's already there. I mean, we obviously have to add the B2 stuff.

**Gerhard Lazy:** I think the question is do you want to do it? Or should I? \[laughter\] That's what it comes down to.

**Jerold Santo:** That's a perfect question. I'd rather you do it... \[laughter\]

**Gerhard Lazy:** There you go. So that settles it.

**Jerold Santo:** I don't want to do it... \[laughs\] Do you like how I had to act like I thought about it for a second? I made it dramatic...

**Adam Staravia:** Yeah, you did. You really acted that out good, Jerold.

**Jerold Santo:** I did.

**Adam Staravia:** What's interesting to think about just kind of almost separating this conversation a bit is you mentioned Dagger, and you mentioned GitHub Actions... And I'm just curious if Dagger is a potential acquisition target for GitHub. Because if you are complementary, and you're improving, and every time we have a problem like this, your solution is a background job built into CI, using Go code, whatever code you want, because that's what the move from CUE to everything else went to for Dagger... And you're so complimentary in terms of Dagger to GitHub Actions. You're not cannibalizing, you're only complementing.

**Gerhard Lazy:** I can definitely see it.

**Adam Staravia:** So a year from now, Gerhard will work from GitHub.

**Jerold Santo:** Hah...!

**Gerhard Lazy:** Anything is possible. \[laughs\] So that's a good idea there, for sure. Now, on that subject - again, I didn't want to talk too much about Dagger in this Kaiden, but I'll just take a few minutes. So I noticed that we had - again, this is Fly Apps v2 migrations related, where we used to run a Docker instance in Fly, and that's where Dagger would run. We'd have all the caching, everything, so our CI jobs would be fast... And part of that migration, the networking stopped working.

\[50:16\] So I was thinking, okay, well, we have all this resiliency in all these layers, but we don't have resiliency in our CI. So if our primary setup stops working on Fly in this case, then nothing works. So I thought, "Well, why don't we use the free GitHub runners?" And that's exactly what we did.

So now if you look in our CI - and there is a screenshot in one of these pull requests; let me try and find it... It's called "Make our Ship It YAML GitHub workflow resilient", 476. So the TL;DR, it looks like this. When Dagger on Fly stops working, there's a fallback job where we go on the free GitHub runners. It takes longer, it takes almost three times as long, all the way up to maybe 10 minutes... But if the primary one fails, we fall back to GitHub. We are also running on Kubernetes. Dagger on Kubernetes. So we have three runtimes now. Fly, GitHub, and Kubernetes. And the common factor is Dagger. It made it really simple to have this sort of resiliency, because at its core, it's the same thing. We just vary the runtime. But we didn't have to do much. I mean, you can go and check our Ship It YAML GitHub workflow to see how that's wired up. Again, it's still running, it's still kicked off by GitHub Actions... But then the bulk of our pipeline runs in one of these places.

**Jerold Santo:** Where's the Kubernetes stuff?

**Gerhard Lazy:** That's the production Kubernetes which I told you about.

**Jerold Santo:** Oh, it's at your house?

**Gerhard Lazy:** Well, no, it's not. \[laughter\] I have an experimental Kubernetes cluster in my house... This is a real production one. Running like in a real data centre, not my house. \[laughs\]

**Jerold Santo:** Hey, man... It's not like you've never run any of our production stuff from your house.

**Gerhard Lazy:** Exactly. I did. And it worked really well, I have to say, for a while... And then obviously, we improved on that. It was a stopgap solution.

**Jerold Santo:** Hey, you know, we've had the work from home movement. Everybody's taken their work from home, and it's like "Well, why not bring your work to your house, take your CI home with you?"

**Gerhard Lazy:** Exactly. I took the CI.

**Jerold Santo:** Okay, so this is a production Kubernetes thing of yours that this is running on. This is like -- that's a third fallback, or...?

**Gerhard Lazy:** That one's slightly special in the sense that that one doesn't deploy yet. So it runs, and it builds, but it doesn't deploy. So there is this limitation in GitHub Actions... And again, if someone from GitHub is listening to this, I would really, really appreciate it if some thought was given to this. So when you select Runs On, when you say "GitHub runs on", all the labels have to match. So what that means is that you can't have a fallback; you can't say "Runs on this, or that, or that, or that." You can't define like a nice fallback. So then what you do - you have to basically say "This job needs the other job, and if that job --" It's just a mess.

So if for example Kubernetes was not available, how do we specify a fallback? And when I say not available, it can't pick up a job. So it won't fail, it's just not available. So a job will basically wait to be picked up for a certain amount of time, and then it will time out most likely. Again, I haven't tested this fully... But that mechanism, the Runs On mechanism is pretty inflexible in GitHub Actions.

Now, in the case of Fly and Docker, that's fairly straightforward. It basically starts on GitHub, and then eventually it hands over to Fly, because we start another engine... Anyway. I mean, you can go and check the workflow. I don't want to go too much into the details. But that's like a simpler proposition. When we have a third one, which may or may not be there, it's a bit more complicated.

**Jerold Santo:** Gotcha.

**Gerhard Lazy:** \[53:54\] So right now I'm just like running it as an experiment to see how well it behaves, to see if it is reliably long-term, and if it is, then maybe make a decision in a month's time or two months' time. But for now, it's Fly with the GitHub fallback.

**Jerold Santo:** Cool. Resiliency for the win. Always have two...

**Gerhard Lazy:** Yes.

**Jerold Santo:** ...and now we have three, just in case.

**Adam Staravia:** Well, I didn't even consider that we would keep S3 for a backup, or consider B2 as a lower-cost backup... Because I thought, "Well, we'll just cut our ties, keep our dollars, and move to R2." And that's done. But that does make sense. Because what if R2 poops the bed? We're going to have some issues. We've got almost a terabyte of assets we've been collecting over these years; our JavaScript, our feeds, whatever we're going to put there, ever... If we have no business continuity, which is a phrase I learned 20 years ago now - business Continuity... That's key in backups. Right? You can't just put the backup over there. You've got to get it back to keep doing business. So that does make sense. And I didn't consider that, and I'm glad you did.

**Gerhard Lazy:** Yeah. And the costs will go down, because again, we are using R2, which is free for egress. S3 isn't, so we're not pulling anything from S3. I mean, if anything, we can move the bits over to B2, so that the storage costs will be lowed... But again, there'll be one-off operations... And by the way, when you write, actually, the operations, you pay for them... But anyway, the point is it will be -- well, it will cost us something from S3 to migrate off S3, but it's like a one-off cost.

**Adam Staravia:** We've already done that though, haven't we? Didn't we just move from R2 to B2?

**Gerhard Lazy:** Oh, that's right. Actually, that's a good point. Yes, exactly. We migrated from R2 to B2. That's correct. So maybe delete S3 after we migrate to B2? That's there...

**Adam Staravia:** Cool.

**Jerold Santo:** Well, you can delete my bucket now, because all the files are gone. So go ahead and get that done, at your leisure. It doesn't have to be --

**Gerhard Lazy:** Okay. Let's see me refresh... Yeah, that's right. So let's get this thing done.

**Adam Staravia:** Yup. Confirmed, it's gone. Bucket's there, files are gone.

**Jerold Santo:** I've got an emotional attachment to this bucket, though... I've been using this for a long time.

**Gerhard Lazy:** You have another one in R2, by the way...

**Jerold Santo:** That's not the same.

**Gerhard Lazy:** ...which is Assets Dev, that you can use.

**Jerold Santo:** That's right. But that's shared across multiple people, so it's not as personal. Like, this was my bucket, man. This was MY bucket.

**Gerhard Lazy:** I see. We can create one for you, it's okay. We can create one for you. \[laughter\]

**Adam Staravia:** It's free.

**Jerold Santo:** I appreciate you consoling me as you delete my bucket...

**Gerhard Lazy:** \[laughs\] Changelog Uploads Jerold. No fat-fingering, delete bucket, boom.

**Jerold Santo:** Don't misspell that... Boom. It's gone forever. Alright...

**Gerhard Lazy:** Cool. What about the backups? What about the Nightly backups? Is that something that we can clear? Because by the way, there are a lot of backups going all back to 2000 and something; I forget what it was.

**Jerold Santo:** Those are assets backups? Or database.

**Gerhard Lazy:** I think it's a database. No, this is another one. This is the small one. This is like from our pre-Fly migration. We can come back to this a bit later, because it has just like a few -- and this costs us nothing. Backups, Nightly... They start in 2015.

**Jerold Santo:** Oh, it's Nightly. This is a backup of Changelog Nightly.

**Gerhard Lazy:** Yup.

**Adam Staravia:** We don't need that.

**Gerhard Lazy:** We don't need that?

**Jerold Santo:** No, man.

**Adam Staravia:** I don't think so...

**Gerhard Lazy:** But this is still happening.

**Jerold Santo:** Yeah, it is, because my code works... I wrote this years ago.

**Adam Staravia:** 2015.

**Jerold Santo:** I forgot about this... We've been backing up Changelog Nightly every night.

**Adam Staravia:** It might be some of the first code you wrote for this company, Jerold.

**Jerold Santo:** It might have been.

**Gerhard Lazy:** So the last backup is 76 megabytes. Do I want to delete the old ones? What's the plan here?

**Jerold Santo:** Yeah, man. There's no reason to have them, because each one has the entire contents of the previous ones.

**Gerhard Lazy:** Oh, I see.

**Jerold Santo:** It's not like differentials or anything. It's like the entire folder structure of Changelog Nightly, which is all static files. Every night, we had two static files and send an email, and then we back it up. And so that's just been happening for years...

**Adam Staravia:** Wow.

**Jerold Santo:** ...and so I forgot about it. So yeah, this can --

**Gerhard Lazy:** Okay, so we'll fix this.

**Jerold Santo:** Just keep the most recent one. Just keep one. In fact, tonight we'll have a new one, so you can delete them all. We'll create a new one tonight.

**Gerhard Lazy:** Cool.

**Adam Staravia:** \[57:57\] What do we do about tomorrow, though?

**Jerold Santo:** Well, we can make it run less often. \[laughter\] We can run it like weekly...

**Gerhard Lazy:** No, hang on... I think that's fine. I think that's fine. What we can do is set some sort of expiration, or like auto-purging on the objects...

**Jerold Santo:** Oh, yeah, let's do that.

**Gerhard Lazy:** Okay. That's a better idea. Good. Okay, cool. So we'll fix that as well. Great!

**Adam Staravia:** Keep the last 10...

**Gerhard Lazy:** Great.

**Jerold Santo:** I can't believe the Nightly folder structure of just HTML files is 76 megabytes of HTML. That seems like a lot.

**Gerhard Lazy:** Well, it may be worth something. It's a tar, so it means there is no archiving, no compression of any kind. I'm wondering if we can make it small. Where does Nightly run, by the way?

**Jerold Santo:** It's a production Kubernetes cluster in my closet...

**Gerhard Lazy:** In your closet, right? \[laughs\]

**Jerold Santo:** It's on an old Digital Ocean droplet.

**Adam Staravia:** I'd actually like to get rid of that, but you know...

**Gerhard Lazy:** Don't say where it is, because I'm sure it's so unpatched, I think... It's like a honeypot to this point. \[laughs\] The exploits have exploits at this point.

**Jerold Santo:** Yeah, thankfully it's just straight up static files served by, I think, NGINX.

**Gerhard Lazy:** No SSH.

**Jerold Santo:** Oh, yeah. No SSH. Don't tell anybody that they can SSH to it.

**Gerhard Lazy:** Okay. No FTP. Nothing.

**Jerold Santo:** Nope. Can't connect to it.

**Gerhard Lazy:** Right. Completely fire walled.

**Jerold Santo:** It's actually air-gapped. Yeah, I don't even know how it does what it does, because you have to walk over to it and put the thumb drive into it.

**Adam Staravia:** For every request you need to have somebody go plug it in.

**Jerold Santo:** Yeah. Every night we plug it in, and it runs, and then we unplug it.

**Gerhard Lazy:** Shouldn't we put it on the Fly. What do you think?

**Jerold Santo:** We certainly could. Honestly, Changelog Nightly is like an entire subject. The quality has been degrading lately because of the rise of malware authors just attacking GitHub constantly. And so there's a lot of malware stuff. The only change that I've made to Changelog Nightly in the last couple of years is just fighting off malware. We just don't want malware repos showing up. And there are constantly -- it's cat and mouse. It has been.

**Gerhard Lazy:** Why don't we just shut it down?

**Jerold Santo:** It still provides a little bit of value for about 4,000 people, you know...?

**Adam Staravia:** Yeah, it really does.

**Jerold Santo:** And me. I still read it. I still find cool stuff in there. It's just harder yet to scan through some crappy stuff. There are just some crappier repos in there, just because GitHub's so big now. It's become a little bit rigid, because it's like an old Ruby codebase that sometimes -- like, I've got gem file problems on my local machine... You know, I can't run it locally; I only can run it from that Digital Ocean server. So I go in there in Vim and edit stuff.

**Gerhard Lazy:** So you don't want me to see it, that's what you're saying.

**Jerold Santo:** No, I don't want you to look at it.

**Gerhard Lazy:** Gerhard is not allowed anywhere near this thing. \[laughter\] It just flips over!

**Jerold Santo:** This is legacy code. This is legacy code. I've thought about rewriting it in Elixir, and just like bringing it in and having like a monorepo deal. And then I'm like "Why would I put any time into this? There are so many things I can work on."

**Gerhard Lazy:** I see.

**Jerold Santo:** So Nightly is just kind of out there. We could definitely put it on Fly. I think that would definitely help our security story... But it might be tough, because it's like Ruby 2, it's like old gems, stuff like that...

**Gerhard Lazy:** If there's a container for it, it doesn't really matter. It really doesn't.

**Jerold Santo:** That's what I'm telling you there, it's Ruby 2, it's old gems... There's no container, man. This is like pre-Docker.

**Gerhard Lazy:** No, no, I mean, there is a Ruby 2 container.

**Jerold Santo:** Oh, yes. I'm saying there's no Dockerfile for Changelog Nightly, is my point.

**Gerhard Lazy:** We don't need a Dockerfile. If there is a Docker container that we can start off, that's okay. We can keep it exactly as it was. So I'm looking now at the Ruby Official on Docker Hub image...

**Jerold Santo:** Ruby 2.3.3, patch 222.

**Gerhard Lazy:** 2.3. Yeah, there we go. Six years ago. It exists. We can pull it, we can base it off on this.

**Adam Staravia:** I kind of learning this with ChatGPT recently, with running -- I didn't want to set up a dev environment, it was actually just for fun, trying to run Jekyll without having to actually install Jekyll, or anything. Because Jekyll is notoriously just kind of hard to maintain, because it's Ruby, and gem files, and all the reasons... And so I'm like "I want to just run the entire thing in a Docker container", but still hit it from a typical web browser, like I would to develop a blog.

\[01:02:02.02\] And so my Jekyll blog lives in -- I think I had Ruby 2.7. I don't even remember what exactly, but it was something that was like safe for ARM, because I'm on an M1 Mac, and all that good stuff. It was like a special Dockerfile there that I could just run and build on. Similar to what you're saying here, you just kind of go back in time to a Dockerfile that was out there for Ruby 2.3.3 and call it a day.

**Jerold Santo:** Patch 222.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** We can totally do this. And it will -- like, Challenge accepted. Show me Nightly.

**Jerold Santo:** Show me Nightly. \[laughs\] Show me yours, and I'll show you mine.

**Adam Staravia:** Well, that would save us $22 a month, Gerhard, I think; something like that. That's how much we spend on this Nightly server for DO. It's about 25 bucks a month.

**Jerold Santo:** And that's literally the only thing on there.

**Gerhard Lazy:** You mean you have hundreds of gigabytes of backups \[unintelligible 01:02:47.14\]

**Jerold Santo:** Hundreds of gigabytes of backups. We're really redundant.

**Gerhard Lazy:** But we'll fix that.

**Adam Staravia:** Since we're mentioning Changelog Nightly though, and the clamminess of it, I do want to highlight a spam situation, the most recent one... I think it's actually a student, and the person's handle on GitHub is rsriram9843. He has, or they have, I'm not sure their gender - Desktop Tutorial, Project 3, Project 1, Project 4, Develop Demo... So check those out. They seem to be pretty popular, because they're in the latest Nighties top new repositories. There you go.

**Jerold Santo:** You don't think it's spam, or you do think it's spam?

**Adam Staravia:** Well, I mean, it looks like a normal person. Maybe they did that, I don't know. It could be a -- I don't know, it seems like a normal person. Would it qualify as spam, that it doesn't belong there?

**Jerold Santo:** Yeah. Like, it's a bot, or it's malware.

**Adam Staravia:** They very well might be a bot. I mean...

**Jerold Santo:** Yeah.

**Adam Staravia:** In that case, if it is, don't go there. I've just identified a bot to not check out.

**Jerold Santo:** Here's how far I've gotten, but I haven't pulled the trigger yet, on trying to actually have a malware/spam detection system for Nightly that's actually good... Does I take a list of a bunch of good repos? Here's what we have: owner, which is like GitHub handle, repo, which is the name of the repo, and then like the description. That's what we have. And I took 20 good ones; these are legit, but they're diverse... Because you can put emoji in there, some people write in different languages etc. And I pass it off to ChatGPT, and I say "Here's an example of 20 good projects on GitHub." And then I pass it some bad ones and I say "Is this one good or bad?" and it's about 60% accurate.

**Adam Staravia:** Really?

**Jerold Santo:** It's slightly better than a coin toss. And I thought, "Well, that's not good enough, because I can't --" I mean, this is all automated. I'm not going to act on 60% confidence, or 60% accuracy. I can't just be like "Nope, not good." I think you'd have to like fine-tune... It gets above my pay grade of being like "Okay, let's take a Llama and fine-tune it." I would love for somebody who's interested in such things to try it. For now, I'm like doing a bunch of fuzzy-matching on just common things that spammers do in their names. There's duplication, there's like these words, there's leet code, and inevitably, it's cat and mouse. But I would love -- I think you have to almost go to a GPT to actually have a decent system. And just -- that's as far as I've gotten. I thought, "Well, not only is this not accurate enough with my current implementation... I'm on an old rigid Ruby 2 codebase that I can't really -- what am I going to do, pull in the OpenAI gem?" I'm never going to be able to get modern tooling into this system, until Gerhard saves us with a Dockerfile, or whatever he's going to do.

**Gerhard Lazy:** A Dagger pipeline, but yes, close enough.

**Jerold Santo:** Yeah, sorry. Wrong company.

**Gerhard Lazy:** I'll dagger it. That's what's going to happen. \[laughs\]

**Jerold Santo:** We need to dagger this sucker. That will be Kaiden. Slightly better.

**Gerhard Lazy:** It'll be in the next one. Cool. So the last thing which I want to mention before we start thinking about wrapping up and thinking about the next Kaiden, is I mentioned that now we have status.changelog.com.

**Jerold Santo:** Oh, yeah.

**Gerhard Lazy:** Yeah, that's another thing that happened. So when we are down - hopefully never...

**Jerold Santo:** We've got 100% uptime on changelog.com...

**Gerhard Lazy:** \[01:06:15.29\] Now, the checks, they don't run every 30 seconds. We are still on the free tier. This is Better Stack, and I think the checks are like every three minutes. So if there's downtime which is less than three minutes, it won't even be picked up by this tool, by this system. However, if there is an incident, we will be communicating it via status.changelog.com. So if Changelog was to be down - again, not going to happen on my watch, but it has happened many years ago, and it wasn't use, it was Vastly... Remember that episode? ... I forget which one it was...

**Jerold Santo:** Yes. But BBC was down too, so...

**Gerhard Lazy:** Again, after I say this - boom, everything crashes and burns. No, not going to happen. I'm not gonna even tempt it. But yeah, so that's, I think, the one thing which I wanted to mention. We have a status page.

**Jerold Santo:** Very cool. And for those of us on my side of the pond, you go to status.changelog.com. If you're in the UK, you go to status.

**Gerhard Lazy:** Yes, status. That's it.

**Jerold Santo:** Both will get you there. It just depends on how you like to say it.

**Gerhard Lazy:** S-T-A-T-U-S. Like POTUS. \[laughs\]

**Jerold Santo:** We can agree on that. Like POTUS. You got the US in there, I appreciate it.

**Gerhard Lazy:** So what are we thinking for next Kaiden? What would we like to see?

**Jerold Santo:** Oh, my goodness... I would like to see Changelog Nightly upgraded in the ways that we just discussed, off of Digital Ocean specifically... I would like to see...

**Gerhard Lazy:** Clustering working?

**Jerold Santo:** Clustering. I think we need to get clustering working, so we can use Phoenix Pub/Sub. I think we have to do Elixir releases to do that. Furthermore, I was reading about it a little bit.

**Gerhard Lazy:** That's there.

**Jerold Santo:** So that's when I stopped and was like "Hm... Releases... This is outside my wheelhouse."

**Gerhard Lazy:** So I looked into that, by the way, but then I decided to leave them out of scope for the migration that was I think for the previous Kaiden... But there's some code in our pipelines to do that.

**Jerold Santo:** Okay. I would like to see Oban Web installed, so we can have that observability...

**Gerhard Lazy:** Top of my list.

**Jerold Santo:** That one should be easy enough.

**Gerhard Lazy:** Adam was mentioning Middleware.io, trying it out maybe?

**Jerold Santo:** What's Middleware.io?

**Adam Staravia:** Did I mention that? I did. Oh, yeah. AI-powered cloud observability platform.

**Jerold Santo:** Oh, shiny.

**Adam Staravia:** That's a nice headline. I do like that. It gets me in there, because it's AI-powered.

**Jerold Santo:** Right. That's how you raise money today, is you AI-power stuff.

**Adam Staravia:** And it's also cloud observability. It's also a platform.

**Gerhard Lazy:** \[laughs\] It has all the buzzwords. Was it generated by any chance? Is it a real website?

**Jerold Santo:** Yes...

**Adam Staravia:** They reached out... I asked you if you saw it. So usually, we get lots of inbound requests from people... Some are legitimate, some are whatever. But my smell test is "Gerhard, did you hear of this? Would you try this out? Would you want to try it out?" And I don't think I've spoken to them yet, but we do have something in the works to get connected. So I will escalate that up my list to make sure I do so, and then - I think you said, Gerhard, you wanted to play with it, right? So we can probably get an account to see if you like it and go from there, kind of thing.

**Gerhard Lazy:** Cool. One worth trying the wildcard.

**Adam Staravia:** Yeah. There you go.

**Gerhard Lazy:** What about something that gives us more than two Los? I mean, that's something we didn't talk about...

**Jerold Santo:** Yeah, we didn't talk about that... But come on. Honeycomb, what's the deal with that? Two?

**Gerhard Lazy:** I know...

**Adam Staravia:** I will tell you... Here's what's happening. While we were talking on this podcast, I was emailing Christine Yen, because she's going to come on a future episode of Founders Talk... And I like her, and I like the whole team there. And I think they do amazing work. And we obviously reference and leverage Honeycomb as critical infrastructure. I don't think we could do what we do quite the way we do it. The listeners didn't get to see you share your screen, but Jerold and I did... They'll hear what you said about what was on your screen, and they'll follow along, hopefully... But we were like knee-deep into layers and layers of observability data that sits on a Honeycomb. And we don't have to program, or what do you call that - instrument these things to do it? It just captures it and we just ask the questions. Obviously, I think it has a length of time of logs that it can go through. Six weeks, or eight weeks, or a couple of months... I'm not sure what the --

**Gerhard Lazy:** \[01:10:26.23\] Yeah, it's two months. 60 days.

**Adam Staravia:** Two months, 60 days.

**Gerhard Lazy:** Traces, and everything.

**Adam Staravia:** Enough for us. Maybe we can get more, I don't know.

**Gerhard Lazy:** We're hitting the limit, by the way... We have 100 million events per month, and we're exhausting that, because we're sending all the traces.

**Adam Staravia:** Yes, we're getting emails about it. They keep telling us. Like "Hey, you've gone over X again this month."

**Jerold Santo:** Right... Threatening.

**Gerhard Lazy:** And by the way, we are paying for it.

**Adam Staravia:** We are paying for it. Yeah, we are paying for it. Because we haven't made this connection yet. So my hope is - and Christine may be listening to this right now, because I sent an email, "Hey, Christine, literally, we're talking about Honeycomb as I type this, because we're on the podcast..."

**Jerold Santo:** We're talking about you right now...

**Adam Staravia:** ...and it goes out this Friday. And here's an echo, because I'm now talking to her and everybody else in this very moment here... And I'm just suggesting, like Hey, we're big fans of Honeycomb. We want to partner with them, we want to find ways to speak more about them... But more importantly, improve. Two Los on the free plan... I'm curious, why is that limit there?

**Gerhard Lazy:** It's the Pro Plan? It's the paid plan.

**Jerold Santo:** It's the Pro Plan.

**Gerhard Lazy:** The free one, you don't get any.

**Adam Staravia:** Gosh, there you go. So if you're paying for the Pro Plan, you should get more than two Los. And if you don't, why? What's the cost to enable an SLO?

**Jerold Santo:** Well, here's a quick question before we go. There are also now triggers, and I was in there poking around, and I see the Los, and I see the triggers... And triggers seem to be based on similar things that Los are based on. It's like, "If this happens, trigger." Do these work together? Are they separate features, Gerhard? Do you understand triggers better than I do inside of Honeycomb?

**Gerhard Lazy:** So triggers is almost like alarms. So it's like an alert.

**Jerold Santo:** Right. But isn't an SLO also like an alarm? Like "Hey, you haven't reached your objective."

**Gerhard Lazy:** Kind of, but it gives you like the perspective of like the last 30 days, right? So when you click on one --

**Jerold Santo:** Does it email you?

**Gerhard Lazy:** Yes, I do get emails, and you can --

**Jerold Santo:** This one says "Triggered" right there. It says it's been triggered.

**Gerhard Lazy:** I mean, this basically gives you almost like a graph, and you can do comparisons to start understanding "When does this SLO fail?" And by the way, some of these things aren't that helpful. And again, to Adam's point, there's more to discuss this. But what's important - we have a budget, and it tracks the budget, and we see whereabouts we are. A trigger will not have that. A trigger will say "Hey, this thing just happened." So an SLO - I think it goes further. You have obviously an SLI, and it keeps track of that, and then you receive emails when you're just about 24 hours from exhausting your budget. And that makes it really helpful.

**Jerold Santo:** Right. Okay, fair enough.

**Adam Staravia:** They're deeper. There are more things to track.

**Jerold Santo:** It seems a bit redundant to me, but I can see how you might just have some one-off triggers that don't need to be like full-on Los. I wonder if we could use those to get around some of our two-SLO maximum, maybe.

**Gerhard Lazy:** Interesting.

**Adam Staravia:** Possibly.

**Gerhard Lazy:** So it's almost like when something is slow... But again, can you take into account -- maybe it can, and we just need to write a query that takes it into account. But then apart from the dashboard view and the comparison view, there must be something else about Los as well. I mean, why not just call them the same thing if it's just that?

**Jerold Santo:** Because I think SLO is like buzzword-compatible at this point. It sounds like a thing that you could charge money for.

**Gerhard Lazy:** I see. Query run every 15 minutes... So maybe...

**Jerold Santo:** Anyway, let's look into triggers a little bit. But yeah, we definitely want to get some more Los.

**Adam Staravia:** Yeah, more Los. And we spell that M-O-A-R.

**Jerold Santo:** Because Gerhard says, "Look, you should have two of everything, except for wives and Los." \[laughter\] You should have less than two wives, and more than two Los.

**Gerhard Lazy:** Yes. Absolutely. Absolutely. \[laughs\]

**Jerold Santo:** Two of everything else.

**Adam Staravia:** \[01:13:57.14\] Right. Right. So... Hi, Christine, if you're listening. Can't wait to talk. Stoked. Love Honeycomb. More Los.

**Jerold Santo:** More Los, please.

**Adam Staravia:** Yeah. This has been a fun Kaiden, though. I mean, let me -- I've been quiet quite a bit during this show, because you all do the work, and I just get the \[unintelligible 01:14:14.12\] as necessary... It's great to see all this work done. I mean, it's great to see us now improving, yes, but I think paying attention to how we spend money with S3, and making changes, and leveraging other players in this space... Mad respect for Cloudflare. We'd love to find ways to work with them, in any way, shape or form. And the same with Better Stack. I think, the status page is something we haven't really looked further into with working with them... But part of this journey with Kaiden is improving, but also finding the right tools out there that we like, that we can trust in terms of who's behind the business, and the way they treat the community, and the way they frame and build their products... Finding those folks out there that we can work with ourselves, and leverage, but then also promote to our listener base, and saying "Hey, these are things that we're using in these ways, and all of our code is open source on GitHub. You can see these integrations." I think that's beautiful... To have an open source codebase, and to integrate with Dagger since 0.1, or whatever the release was initially when you first got us on there... And then having that conversation with Solomon on the Changelog, and kind of going into all that... All this stuff is out there in the open, and we just invite everybody listening to this show to just follow along, as you'd like to, to see where we go, and then how it works when we put it into place. So that's kind of fun. I like doing it with you all. It's a lot of fun.

**Gerhard Lazy:** Yeah, same here. I mean, this really is unique. I mean, to be able to discuss it so openly, and to share the code... We're not just like talking about ideas, or like what we did. This is like a summary, and "Hey, by the way, there is a GitHub repo, and you can go and check all these things out. If there's something that you like, use it, try it out, and let us know how it works for you."

So yes, we're doing it for us, of course, but also, a lot of effort goes in to share this so it's easy to understand, it's easy to try using it; try it out and see if it works for you. And we're open about the things that didn't work out, because a bunch of things didn't.

**Jerold Santo:** Right.

**Adam Staravia:** Precisely. To close the loop on the invitation, I would say if you've made it this far, and you haven't gone here to this particular webpage yet and joined the community, you should do so now... Because we are just as open and welcoming in Slack, in-person, as we can be. Go to changelog.com/community. Free to join. We'd love to talk to you in there. Lots of people in Slack... It's not overly busy, but it's definitely active, and there's a place for you there. So if you don't have a home, or a place to put your hat, or hang your coat, or your scarf, or whatever you might be wearing, or take your shoes off and hang out for a bit, that is a place for you to join; you're invited. And everyone's welcome, no matter where you're at on your journey. So I hope to see you there. What else is left? What can we look forward to?

**Gerhard Lazy:** One last thing... If you join the dev channel in Slack, please don't archive it...

**Jerold Santo:** What the heck? I just noticed that.

**Gerhard Lazy:** \[unintelligible 01:17:05.24\] joined and archived. And it just messes up with our client, so please don't do that. Don't archive channels. I don't know why people can do that... I mean, maybe there's some fix that we should do.

**Adam Staravia:** Yeah, maybe.

**Jerold Santo:** You think that'd be a setting. Like, no.

**Adam Staravia:** That's the limit of our invitation. We are very open and very inviting until you archive our channels, and then we don't want it to happen. So don't do that.

**Jerold Santo:** That's like coming into our house and being like "Oh, I threw away your kitchen table. I hope you didn't need that."

**Adam Staravia:** "I gave it to your neighbour."

**Jerold Santo:** "I got rid of that."

**Adam Staravia:** "Your neighbour needed the table." \[laughter\]

**Gerhard Lazy:** Yeah. Be nice. Be nice.

**Jerold Santo:** Be nice...

**Adam Staravia:** That's right. Otherwise, welcome. Otherwise, welcome. But alright, Kaiden!

**Gerhard Lazy:** Looking forward to the next one. Kaiden.

**Jerold Santo:** Kaiden. Always.
