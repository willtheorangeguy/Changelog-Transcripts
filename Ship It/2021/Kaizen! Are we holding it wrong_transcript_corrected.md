**Gerhard Lazy:** So we're back for the third Kaiden. I can't believe it's been 30 episodes, and I'm not the only one. Adam can't believe either than it has been 30 episodes of Ship It.

**Adam Staravia:** Yeah... It really is insane, honestly... I mean, this show was just an idea recently. I think anybody who makes things come to life from nothing is always flabbergasted by the creation, I suppose, once you sort of get into it... But podcasting is a little bit different, because it really is a journey. It's a journey pre-production, and it's a journey post-production. Now we're obviously post-production, 30 episodes in, and I think it's just kind of crazy, looking back and thinking this was just an idea... And then in particular to podcasts, the impact to us and to the audience. That's why I love it. That's why I love the game.

**Gerhard Lazy:** Yeah. I mean, we shipped it, right? It took us a while; it took us five months to ship the first three episodes... And then it was like a roll. What blows my mind is that my mind is on episode 40. And most people don't realize this. The next five episodes are pretty much locked in. The guests, the topics, the flow... And even the five ones after that are nebulous, nothing locked in for real, but it's coming... So for me, it's even more mind-blowing, because I'm already like in February. I'm thinking February right now.

**Jerold Santo:** Yeah, you just live in the future. I think you might be the most prepared and scheduled out podcaster in the entire universe, Gerhard.

**Gerhard Lazy:** \[laughs\] Okay... I want to think that's a compliment...

**Jerold Santo:** I'm happy that I got us scheduled out through December, but you're -- no, it is.

**Gerhard Lazy:** Thank you.

**Adam Staravia:** That's a compliment.

**Gerhard Lazy:** I don't want to leave myself open to unique encounters and like...

**Jerold Santo:** \[04:15\] Yeah, that's a challenge. Serendipity is taken out when you're scheduled out.

**Gerhard Lazy:** That is a great word. I haven't heard it in a while. I thought I was the only one using it. Okay...

**Jerold Santo:** Happy to surprise and delight.

**Gerhard Lazy:** Right. Well, thank you very much in which case, Jerold. I appreciate that. Thank you. And what I'm really excited about is -- I don't think many people realize this, but there's like a theme to this; there are like multiple themes. A couple of episodes, they kind of cluster together, and there's a build-up... And a lot of the episodes that we had -- like the last 10–15 ones, they're leading to something. They're building to something. And that will be the Christmas episode, episode 33, which I'm very excited about. We'll come back to that a bit later, but... One of the things which is on my mind is the incident 2. Our last episode, 20, our last Kaiden, episode 20, was all about incidents. We called it "Five incidents later."

**Adam Staravia:** Yeah.

**Gerhard Lazy:** And there was something which I wanted to understand, which I didn't at the time... Was why was an unhealthy pod put back into service. Do you remember that?

**Jerold Santo:** I do remember that. We didn't have answers.

**Gerhard Lazy:** Yes. So my answer is we're using the "latest" tag. What that means is that if something is unhealthy, and it has to go back to the previous one, it will use the "latest" tag. But "latest" has moved on. So it doesn't keep the old SHA, the one that was working; it says "always the latest." So if you were to go back, then you always go back to the latest. Any by the way, the latest already moved, so that's like the broken version.

**Jerold Santo:** Oh, you're pointing back to the same version, which is broken.

**Gerhard Lazy:** Exactly. Exactly.

**Jerold Santo:** Why are we doing that?

**Gerhard Lazy:** Um, some corners have been cut... \[laughter\]

**Adam Staravia:** The honesty, I love it.

**Gerhard Lazy:** ...and that worked well for quite some time. So I have to say that even though those corners have been cut, there was like a trade-off to be made. It was like a conscious trade-off... And it only failed once. So that trade-off has bitten us once.

**Jerold Santo:** Right.

**Gerhard Lazy:** But I think it is high time that we revisit the whole Git Ops approach. The Git Ops approach that we have, but not really have, to how we run our infrastructure. So while we do version all the manifests, and everything is in the repo, and we apply them, some manifests reference "latest", and "latest" can move. So we cannot -- basically, right now we don't capture everything we run at the SHA that we run. So Ingress NGINX, external DNS - we have versions for those, but for our app, we have "latest".

The thinking goes we always want to be running "latest". When do you not want to run "latest"? Apparently, when "latest" is broken.

**Jerold Santo:** \[laughs\] Exactly. The one time when you definitely do not.

**Gerhard Lazy:** That's when you don't want to run "latest". \[laughs\] But that's something that -- yeah, we will be investing in. I will be spending a bit of time on that, among many other things. But that explains this incident too, which - I didn't have an explanation ten episodes ago.

**Jerold Santo:** Yeah. How did you learn of this?

**Gerhard Lazy:** Um, I looked at the manifest, and I tried to understand what happens. So I went through the steps of what would happen, or of what happens in Kubernetes when -- like, the new one gets put in service, it fails, the old one crashes, and when it gets restored, it gets restored with "latest". So that's what happens.

**Jerold Santo:** \[07:56\] So my developer brain sees something like this, and I think infinite loop. Is that going on here, or does it just fail? Because if it runs "latest", "latest" is broken, it runs "latest", "latest" is broken... Does it just keep doing that over and over again?

**Gerhard Lazy:** Yeah. So in our case, what happened was that the version that was running - that crashed. Because it's just meant to restore it, right? It crashes - not a problem, it will come back.

**Jerold Santo:** Right.

**Gerhard Lazy:** But when it comes back, it doesn't know which version it should come back with, because it has "latest", and it resolves that when it boots. And "latest" has moved along, which is where the problem comes from. So we need to capture the version of the app that we want to run. Not the app, it's the app container image. Currently, because we use "latest", that always changes. So yeah...

**Adam Staravia:** That's a challenge.

**Jerold Santo:** It's always nice to get answers to mysteries...

**Gerhard Lazy:** Yes. I love a good mystery, especially when I have an answer for it...

**Jerold Santo:** Exactly.

**Gerhard Lazy:** Otherwise it drives me crazy. I hate it. Like, "Oh, \*\*\*\*! What's the answer?!"

**Jerold Santo:** It's like that show, Unsolved Mysteries, which I always avoided, because... Come on, give us the solution already. Have you guys ever watched that one? It's probably dead now, but back in the day they would show these mysteries, and they're like, people who are actively being sought by FBI, or whatever... And there's no solution. At the end they're like, "If you know where this person is, please let us know."

**Gerhard Lazy:** Unsolved cases.

**Jerold Santo:** And I'm always like, "I want the solution!"

**Adam Staravia:** Yeah. It's those shows that don't have endings essentially that get me. It's like, "I can't watch that..." It drives me crazy.

**Jerold Santo:** Yeah.

**Adam Staravia:** Okay... So what are we doing to solve this then? If "latest" can't be used, how do we uncut that corner?

**Gerhard Lazy:** So right now we have Keel.sh, which basically watches the Docker image updates, and when there is an update, it will just basically update itself. But what we have in the deployment, it's also "latest". So we need to use Git Ops properly. What that means is commit in the manifest the version of the app that should be running, and that should automatically be applied, which is where Argo CD comes in, or something like that. I'm thinking Argo CD; maybe there will be something else.

So basically, the infrastructure gets continuously reconciled with what is versioned in the repo, and what we version in the repo is the app updates. So when a new image is built, there will be a new push to the repo, a new commit to the repo, which has the exact version of the app that should be running, and there'll be a reconciler which will make sure that that is true. And that's currently what we don't have.

So finish Git Ops... We're 90%, maybe 95% there. Because we version the manifests, but we don't update them when the app updates. And we don't apply them when the app updates. So that's what's missing.

**Adam Staravia:** Is there like one place to learn exactly what the requirements are for Git Ops to comply, I suppose? You could search on Google what is Git Ops, and there are a lot of pages that describe what is Git Ops.

**Gerhard Lazy:** I think GitOps.org is a good resource. That's the one that I would recommend for learning what Git Ops is. And in a few episodes we'll have Alexis from Weave Works, where we'll be talking all about Git Ops.

**Adam Staravia:** So GitOps.org doesn't resolve to anything for me...

**Gerhard Lazy:** GitOps.tech. That's the one.

**Adam Staravia:** So this is what you would consider the canonical resource for learning about Git Ops at least... It's going to link out to Weave Works, it's going to link out to a PDF, an EPUB book... So I guess this is a book, too?

**Gerhard Lazy:** So the last time when I've seen it -- I'm seeing this has a few updates. I wasn't aware of the book, so that must be something new...

**Adam Staravia:** It does say "We've just released our short book on Git Ops."

**Gerhard Lazy:** \[11:57\] There you go. So that's the new element which I wasn't aware of. If you scroll down, you see push-based deployments, pull-based deployments, which is what we have, by the way... We have a pull-based deployment model. And Weave Works were the ones that coined the term of Git Ops, and this is the canonical resource, for me at least, when it comes to Git Ops.

**Adam Staravia:** Okay. So they have this graph down there... Or, sorry, this -- what do you call this thing? Infographic, I guess... A graphic to look at, essentially outlining what --

**Jerold Santo:** Is there information on the graphic?

**Adam Staravia:** Say again?

**Jerold Santo:** Does the graphic have information on it?

**Gerhard Lazy:** Yes.

**Adam Staravia:** It does have information on it.

**Jerold Santo:** Oh, that's a classic infography then.

**Adam Staravia:** That's right. It's really just a graphic of what the flow is, from application repository all the way to deployment, what should happen in there. So are you seeing that we're somewhat adhering to this push-based deployment graph here, this idea?

**Gerhard Lazy:** Yes. The difference is that in the pull-based deployment there's an operator that observes the image registry, and then updates the environment repository. The environment repository is basically which stores the config for everything that's running in an environment. So basically, those would be our YAML manifests. Currently, that doesn't happen.

**Adam Staravia:** And the reason why this flow is prescribed is to prevent things like calling on "latest" when "latest" is broken.

**Gerhard Lazy:** Yes. Or "latest" changes. Because you don't know what you're running, so you're trying to capture your production as much as you can. Not as much as fully, like to the SHA. Not even to the version, because when you tag an image with a version, like v1.0, you can update the tech to point to a different SHA. So you want to point to a specific SHA, which will not change. It's like a Git SHA, but it's the equivalent in container images, which is what we would want.

**Adam Staravia:** Which is important for recovery from a disaster. So in this case, a disaster happened, the application failed, you needed to reboot, you rebooted, but you called upon latest, and latest wasn't right... So if you had had continuity in place, the operator would have told the environment repository which SHA to point to, essentially, so that when you reboot, you don't pull from a broken "latest".

**Gerhard Lazy:** Yeah. So a couple of things had to go wrong in our case when instant 2. The version that was running - that one came down as well. So the version that was running came down, it had to be rebooted, the pod, and when the pod was restarted, because it was pointing to the latest, it pulled the broken version. So that happened as well, on top of latest being broken.

So it needs to be like a sequence of events for this to happen, which is what happened in our case, and that's why those are rare. So as I mentioned, in the year since I had this set up, it only happened once. It was enough for us to have an incident. It wasn't a major one, it was just a minor one, because production was up, everything was cached, we served from the CDN... We ARE serving from the CDN everything, except the authenticated users, except the dynamic requests. So not like the gets. This was like a post, a patch, and we have quite a few of those. I didn't actually realize how many of those we have... Because whenever we visit a link, like news and press, that's the most popular one we keep hitting; we keep doing a lot of posts. So there's that.

But anyway, it was like up for anyone that was casually browsing it; people could listen to podcasts. Only a few URLs that were not in the CDN were not available.

**Adam Staravia:** That's a good -- to your point, Jerold, the unsolved mysteries... If you listen to Kaiden 20, we solved some more mysteries for you. So if you left that conversation thinking "Gerhard, what actually happened behind the scenes?" Well, we've kind of recapped some of that, so... The mystery is solved for those unsolved mysteries of Kaiden 20. You're welcome.

**Gerhard Lazy:** \[16:12\] But I do have very exciting news... So not only we solved that mystery, we did something even better. And I think we discussed this also in episode 20, about a tighter Honeycomb integration. So one of the things which we did since - we integrated Honeycomb with Vastly, with our CDN, so we can see a lot more details about how the CDN behaves. Which are the cache hits, which are the misses... I don't mean "misses" like the missus; I mean like M-I-S-S-E-S. There's no U there.

**Jerold Santo:** Solved clarification...

**Gerhard Lazy:** Yeah... \[laughs\] And we can just drill down, observe a lot of stuff... That's amazing. The level of visibility which we have right now - we can answer so many questions, including the pull requests which we had open. I'm going to fire it up now, because I forgot the exact number. There were some new pull requests since.

This is issue (not pull request) 383. "Why do some mp3 requests take 60 seconds or more, while others complete quicker?" So we have an answer to this question, as well as full visibility into how the CDN behaves, the app behaves, the Ingress NGINX, how it behaves and how they interact among one another... And some of the details which we get are fascinating. I can finally be properly curious in prod, and I didn't know what it meant until I did this integration, and some of the level of detail is just amazing.

We can for example see the top URL's, the top episodes by browser, by user agent, by data centre, by country, by city... It's just so much insight. And this is just like the content stuff. Then it comes to the CDN. As I mentioned, the cache status; how many hits versus how many misses. We can slice and dice by audio requests. And rather than building dashboards, we can do something even more amazing, which is literally started with a query, and keep asking questions, and keep getting answers, until we understand what's happening.

**Adam Staravia:** So this is the first time we've been able to have observability to this level on our CDN. So to recap, we leverage it quite well, because all requests go through Vastly first, prior to hitting our application. So it would make sense that if you make that choice and lean that heavily, trust that much on your CDN - in this case we do; we trust Vastly, they do an amazing job for us, for many years now... But now we actually have observability into various specifics of how it operates for us, where we never had before.

**Gerhard Lazy:** Correct.

**Adam Staravia:** And this is thanks to the details and visibility that Honeycomb gives us.

**Gerhard Lazy:** Correct. Yeah. That was one of the big improvements since episode 20. And we can see the slowest requests, and we understand that the XML ones, like the sitemap, or the feeds that are the slow ones, they take 5 seconds sometimes to load. The website is fairly fast; the only time when it gets slow is when we serve static assets from the website. So in the Phoenix app, when there's a cache miss in the CDN, it has to go to the app - actually, Ingress NGINX... Ingress NGINX has to go to the app, and the app has to store a PNG, or JPEG. It's usually a PNG. That's the one that took quite a bit of time. So I was looking at it -- was it earlier? Yes. Let me find it, it's right here. That was an interesting one. It was icon-small... No, it wasn't that one. Time elapsed. This was it. It was actually a GIF. News item, 1.4 minutes to serve it. That's how long it took to serve that news item GIF, all the way to Hong Kong. So someone from Hong Kong was accessing it...

**Adam Staravia:** \[20:37\] They were waiting that long, huh?

**Gerhard Lazy:** They were waiting that long because they had to go all the way to our data centre in New York.

**Adam Staravia:** It’s probably a big GIF, too.

**Jerold Santo:** Yeah, they always are. I mean, GIFs are just large files, unfortunately.

**Adam Staravia:** Yeah, they tend to be legs. At least a Meg, sometimes ten. Maybe 50, but...

**Gerhard Lazy:** Let's see... How big is it? We have that as well, that information. Body size... 18 kilobytes? No, it can't be.

**Jerold Santo:** No. Megabytes.

**Gerhard Lazy:** Like 18 million... Let's see.

**Adam Staravia:** Should we ask Siri to do some math for us again?

**Gerhard Lazy:** Yes, Siri. 18 million bytes.

**Jerold Santo:** We should ask Honeycomb to do that math for us.

**Gerhard Lazy:** Right. So that's the one thing which we need to set. I was setting some derived queries... But let's see. But not for this specific thing. 17 kilobytes -- 17 megabytes.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** We have a 17-megabyte GIF. And serving it to Hong Kong, that’s how long it takes.

**Adam Staravia:** It’s pretty heavy, yeah.

**Jerold Santo:** Yeah Sometimes we do lazy-load those, so you're not actually waiting end user experience. You can read what the news item is, and then as long as it takes a minute and a half to read, by then the image is loaded; it's still too long, but...

**Adam Staravia:** Yeah. Well, I don't think anybody's optimizing for reading -- unless your image, or something like that. Maybe you're optimizing for those things to be superfast; large GIFs like that, for example.

**Jerold Santo:** Well, if we had it on a CDN in Hong Kong, it would be much faster.

**Adam Staravia:** Okay. That's the question I was thinking of asking... Like, okay, the observability lets us know this event happened, right? The event being this GIF was served from New York to Hong Kong at this speed, it's this size, etc.

The other question is it was a miss - so why was it a miss? These are questions we'll begin to answer ourselves as we dig into this. Okay, why was it a miss? Okay, now we know, and we’ve figured... What was the answer to that? Why was it a miss? Why was it a cache miss?

**Jerold Santo:** First, Hong Kong visitor of the day... Or it's expired, or who knows...

**Gerhard Lazy:** Yeah. I mean, those are kept in cache right on Vastly, and they can't cache like the entire Internet. Even for us, they can’t the cache all of our content.

**Jerold Santo:** They can probably cache all of our content at all of their pops, and barely ever notice, don't you think?

**Gerhard Lazy:** They could, but I think the reason why they're not is that they have to shed some of the extra content that is not accessed within, I don't know, x hours, days, whatever. So they don't guarantee that everything will be in the CDN all the time, even though our headers asked for it to be in CDN for a few weeks, I believe or something. I'm not sure exactly this one... We can check to see how long it should be kept in the CDN for, this specific request, but as far as I remember, it’s just meant to be a few weeks at most. So if that wasn't accessed in a few weeks, then it may expire when it's requested again, which will be a miss.

**Jerold Santo:** Right.

**Adam Staravia:** Why don't they just make people pay for that desire then? I guess if you're a larger site, with much more assets than we have, then maybe that becomes more and more expensive... But it's in our affordance right now to ask them to do that.

**Gerhard Lazy:** Yeah, that’s a great, great idea.

**Adam Staravia:** \[24:02\] So why wouldn't they offer it as a service, like "Hey, just cache the whole thing indefinitely, and I’ll pay for it."

**Gerhard Lazy:** I would love us to be able to do that. All our stuff should be cached all over the world. I agree.

**Adam Staravia:** What’s our assets on stuff like that? What would be the weight, in terabytes?

**Gerhard Lazy:** No...

**Jerold Santo:** No.

**Adam Staravia:** Or in Gigs?

**Gerhard Lazy:** 100–150 Gigs? Not that much.

**Adam Staravia:** That's pretty reasonable. I mean, I can go buy a 14-terabyte hard drive for under 400 bucks.

**Gerhard Lazy:** Yeah, but you need to multiply that times how many times you want, how many ops you want.

**Adam Staravia:** That’s true.

**Gerhard Lazy:** But still, you’re right, it's not a lot of data. I wish it was cached, and I wish we had an e-tag implementation, so that if the content doesn’t change, it won't expire from the cache. I mean, we have it configured, we have cached shielding, or pop shielding, which means that there should be at least one pop where this is always kept in cache. So if another one doesn't have it, it should get it from that pop, rather than come to us.

**Adam Staravia:** Right. And their network’s probably faster than ours.

**Gerhard Lazy:** Of course, yes.

**Adam Staravia:** Right. It should be at least, by design.

**Gerhard Lazy:** It's optimized, right? I mean, they should -- they have all the optimization, they have the best routing between their pops, which is how it should be. So you're right. But this, we've never had before, and this is the exciting thing. Now we know why our 99th percentile -- why we have such a bad tail latency. Because sometimes this stuff happens. We didn't have this visibility before, and that's the exciting stuff.

**Jerold Santo:** When does the law of diminishing returns come in?

**Adam Staravia:** The now known from the unknowns

**Gerhard Lazy:** I didn't hear any of you. \[laughs\] Do you want to try again?

**Jerold Santo:** When does the law of diminishing returns come in? Because you know, slow clients are slow. We can't make every request fast. Where do we know, "Now, we're just basically toiling away at something that's not worth our time anymore", versus "This is actually a valuable optimization"?

**Gerhard Lazy:** I'm really glad you brought this up, because we have -- this is something which we weren't able to see before... We have Apple Watches consuming MP3 files. And they are slow, so they take many, many minutes. Our longest consumer was something like 40 minutes. Imagine someone being connected to our website and consuming MP3's for 40 minutes. It was an Apple Watch, and there were a couple of others like that.

So when it comes to content that is not in the cache, I don't think we should spend much more time on that, except if we're talking about using an object store versus local store, but that's like a separate conversation. However, we should absolutely try to serve as much as we can from the CDN, especially when it comes to the static content. GIFs, PNGs, MP3s - all that stuff should be served directly from the CDN, which is exactly what Adam was suggesting.

**Adam Staravia:** I mean, it'd be different if we had an unreasonable ask from them; if it was like, terabytes and terabytes of data - that's unreasonable. But if it's like, sub-200 gigs, that's not unreasonable to ask a CDN, to in perpetuity hold that until it's expired.

**Gerhard Lazy:** What are you thinking, Jerold?

**Jerold Santo:** Well, this is what I've been saying for years. That's what I had been thinking. \[laughter\]

**Gerhard Lazy:** Okay, you're being facetious now, right? Facetious...

**Jerold Santo:** No. Facetious... No, I'm not. I've been saying it for years - can't they just cache our stuff forever, and just keep it and never request it again until we tell them that it's fresh? I understand that, okay, if we're going to do what Adam proposes, you're kind of becoming a snowflake, right? Like, "Hey, Vastly. Please treat us differently." But isn't there just a way that they can scale to all their customers, to let you say, "Don't ever request this again, please"?

**Gerhard Lazy:** I would love to have that conversation with someone from Vastly. I've been trying for years.

**Jerold Santo:** That’s what I’ve been saying for years. I don't want them to keep asking me for new --

**Adam Staravia:** Well, I don't want them to treat us differently either.

**Jerold Santo:** ...my ShipIt-28.mp3 hasn't changed, it's not going to change. It's never going to change. It’s never going to change.

**Adam Staravia:** \[28:07\] Right. We know it's never going to change. So, just keep them.

**Gerhard Lazy:** I will not name any names, the people that I reached out that I knew within Vastly, but if a listener knows someone within Vastly that wants to have this conversation, I would love to do that improvement... Because Honeycomb - this new integration showed us how much can improve within the CDN. And we are reaching diminishing returns within the app, within our own infrastructure, where the biggest wins right now are in the CDN.

**Adam Staravia:** Right.

**Jerold Santo:** For me, imposter syndrome sets in when I think "Surely, we're holding it wrong." You know, like the Steve Jobs response to the antenna on the iPhone 4 is "You're holding it wrong."

**Gerhard Lazy:** Yes.

**Jerold Santo:** I feel like we're just not using Vastly right...

**Adam Staravia:** All these years.

**Jerold Santo:** I mean, I understand how to set HTTP headers, and we use e-tags, and we set cache control, we've tweaked some stuff, but I just feel like we're not using it right for some reason, and that's why part of me is just wondering... That's where I like the toiling away, like "Well, how many times can we tweak the way that we tell Vastly to do things?" But I don't know. I just thought this is how CDNs work, is like "Hold on to it till it's fresh, please." That seems like a button you click in a click op somewhere, but I don't know.

**Gerhard Lazy:** Yeah. So I'm surprised when content that should be cached for -- now that I think of it, some of it is even cached like for a whole year. The stuff that we know is not going to change. And that content is being requested, even though it was requested before, and it's requested again, and it hasn't passed a year. So what's going on Vastly? I can’t answer that.

**Jerold Santo:** Right. I mean, our old episodes, the long tail of listens on our shows is bewilderingly awesome. Like, you go back to a show, and you're like, "Wow, 33 people listened to this today", and it's four years old. Every day, our MP3s are being requested, pretty much all of them, plus or minus some outliers. So they shouldn't be expiring, unless you set the expiration to an hour, or 30 minutes, or six hours. But if we're setting it to a long time, I do not understand why we have so many cache misses.

**Adam Staravia:** Especially, I mean, given -- it'd be different if our content was highly volatile in terms of change. We're a media company, the things we create are long-term artifacts, so just by nature of the business we're bringing, like the character type we are, the persona, so to speak even, we know that the reason we're using the CDN is to be globally fast. And the data we're giving them to be globally fast doesn't change, if ever. So we want to be globally fast forever, and pay for that. And we put Vastly in front of everything to enable that, so that even if our app is down, we're still serving cache pages, and the same thing for our actual files, like MP3s and GIFs and things like that. Just by the nature of us being a media company or a media entity, the things we have tended to never change.

I think we've changed like an episode, just to go back and update... We call it a remastering, and we were doing that for a bit. We were remastering some of these shows Jerold was talking about, that had high degrees of listens, that are several years old. So rather than having that listener go back and listen to an old show and still be sort of like unimpressed by the audio quality in comparison to now, we went back and remastered those.

**Jerold Santo:** But we can also programmatically purge endpoints from Vastly by way of our system. It'd be easier to code that up. I just don't -- I've never done it, because I feel like it keeps purging anyway. And every once a while, I'll hop in there and just purge one manually. Especially if it’s released...

**Adam Staravia:** I'm with you, Jerold. I feel like we're holding it wrong. I do. I feel -- I don't know why we're holding it wrong. It seems like the logical way a CDN should work is the way we think it does work... Yet we are holding it seemingly wrong.

\[32:12\] So yeah, listeners, if you're out there, if you know somebody at Vastly who knows more than we do... We have connections in there, but we've hit certain dead-ends on that front... But we'd love to have some help... Like, Vastly, come on this show. Come on YouTube with Gerhard and triage how we use our CDN and help us DE-antennagate ourselves and hold it right. \[laughter\] You know what I mean? Let’s not CDN-gate ourselves here.

**Gerhard Lazy:** Over the years, we've had some epic support threads with Vastly. Epic. Some of them have not been solved.

**Adam Staravia:** Unsolved mysteries.

**Gerhard Lazy:** Many unsolved mysteries when it comes to Vastly.

**Adam Staravia:** Just hold it right, please.

**Gerhard Lazy:** I'm looking... So I think we're holding it right, but I think there's stuff happening within Vastly which we don't fully understand.

**Adam Staravia:** Right. And maybe that's just how it works. It doesn't make sense why it is that way. So if it works that way and that's how it does work, that seems odd, given the reason you'd use a CDN.

**Gerhard Lazy:** I think we can Kaiden Vastly. I think that's what you're getting to.

**Jerold Santo:** Yeah.

**Gerhard Lazy:** Because in the last 24 hours, we had 3,000 misses on MP3 files. This is in the last 24 hours.

**Adam Staravia:** That's incredible.

**Jerold Santo:** It doesn't make sense.

**Gerhard Lazy:** It doesn't make sense. Exactly.

**Adam Staravia:** The whole reason we engaged with Vastly in the origin, before we got to what we could do application-wise, was to deliver our MP3s globally, fast, forever. So to have 1,000 misses in the last 24 hours is egregious.

**Gerhard Lazy:** 3,000.

**Adam Staravia:** Especially--

**Gerhard Lazy:** That's crazy. I agree with you.

**Adam Staravia:** Triple that. 3x that. Because if we can have one pop -- so let's just say it’s a size requirement. Too much data, forever... Okay, sure. We have to purge somewhere. Fine. Then have one pop be the canonical. That one is forever. And then you can miss somewhere else and pull from your own pop fast, not from us.

**Jerold Santo:** Well, we shield through LaGuardia, so we should have that. LaGuardia should have it, if Hong Kong doesn't. **Gerhard Lazy:** Exactly, yeah.

**Jerold Santo:** So I'm not super-clear if that still shows up as a miss, if Hong Kong misses but grabs it from LaGuardia, and it doesn't grab it from us. Gerhard, you know the difference? But—

**Gerhard Lazy:** Yeah... So I'm not sure, but that's something worth digging into. This is exactly—

**Jerold Santo:** Yeah. Let’s solve this mystery.

**Gerhard Lazy:** Exactly. How does this stuff work within Vastly? This is the first time we could have a perfect conversation about this, because of this integration.

**Adam Staravia:** We have data now. We have wisdom. Before, we had assumption. Now we have like, "Look, here's Honeycomb."

**Gerhard Lazy:** Facts. Hard facts.

**Adam Staravia:** "This is where it goes. This is how it works." Yeah.

**Gerhard Lazy:** It’s amazing.

**Adam Staravia:** Even asking for support makes it so much harder, when you have no visibility into what's going on. Now we do, so we are armed with more data to support ourselves differently in our argument back like why things are not working the way they should be, or how we think it should be.

**Gerhard Lazy:** Yeah.

**Break:** \[35:19\]

**Adam Staravia:** So Jerold and I got some brand-new computers recently, brand new M1 Macs, and like any new Mac, you take your sweet time setting it up... And in my case, Jerold, you may concur with your case, I'm doing it all manually. I'm not scripting anything this time, I want to take my time... Because the M1 Mac is so different, even Homebrew has a couple -- it has one slight variance in how you set it up with what you add to your, in my case, and I think yours too, Jerold, the.SRC file. So there are a couple particulars to deal with, and I haven't gotten to the point yet to set up the app. Actually, I have, but I haven't done it yet. So my thought’s like if I'm setting up changelog.com for a dev environment on my new Mac - how? What's the way? The README isn't super clear, there's a Docker path I'm not sure is still working... So what do we do? How do you do it? Have you set it up, Jerold? Where are you at?

**Jerold Santo:** I have not set it up yet, because I haven't needed to. I still have my old laptop right here, that I can use. I would not use Docker, because I didn't use Docker last time.

**Adam Staravia:** Okay.

**Jerold Santo:** I would set it all up individually. But maybe I'd even just procrastinate until we're on Code spaces. What do you think, Gerhard?

**Gerhard Lazy:** That's exactly what I'm thinking.

**Adam Staravia:** It’s even better.

**Jerold Santo:** \[laughs\]

**Gerhard Lazy:** That’s exactly what I’m thinking. The reason why—

**Jerold Santo:** I don’t even want to set it up if I don't have to.

**Gerhard Lazy:** Exactly. I uninstalled Docker about six months ago, or four months ago, something like that, and it's not coming back on my machine, or any other machine, like my local machine... However, I'm running Docker on Linux, on a Linux server in Linde, which is my development machine.

**Adam Staravia:** Is that right?

**Gerhard Lazy:** That's right. So what we want is GitHub Code spaces, where we can run our own infrastructure. So rather than using the Azure VMs, which is what runs GitHub Code spaces, we want to be running our own, whether it's Linde, or - and this is where the big one comes in - Equinix Metal.

**Jerold Santo:** I don’t think they’ll go there, will they? GitHub.

**Gerhard Lazy:** Well, no, they won't, but like, can they allow people to use, like -- you know, as you can run your own GitHub runners with the GitHub Actions... So you should be able to run your own hardware, wherever it is, with GitHub Code spaces. I think it's a natural next step. Because whatever needs -- because you pay for the hardware. That's where the cost for the GitHub Code spaces is... And that's fine if you want the simplicity. But if you want to run, for example, on the ARM servers, or fast Intel servers with dedicated CPUs, dedicated NVMe's, 20-gigabit networks, why wouldn't you go to Equinix Metal? So that's what I'm thinking... Because in that world, everything is amazing.

**Adam Staravia:** \[40:18\] So I guess then—

**Gerhard Lazy:** Or it will be when I’m finished with it.

**Jerold Santo:** It’s all rainbows and—

**Adam Staravia:** Isn't the thing with GitHub Code spaces that is their -- like, their thing is their infrastructure, so their VMs, their hardware, and it's optimized... Obviously, it's probably Azure-backed, considering their parent company, etc. But isn't that what they sell? Are they selling the agnostic route to dev environment to the cloud? They’re selling—

**Gerhard Lazy:** Not currently—

**Adam Staravia:** ... Codespaces, which is hosted by them, right?

**Jerold Santo:** Right. It seems like it's natural for us to want that, but it doesn't seem natural for GitHub to want to offer that. So maybe it's like a Cloud spaces alternative which is geneticized, is the answer.

**Gerhard Lazy:** So there’s Gitpod, I’m aware of that.

**Jerold Santo:** Yes, right.

**Gerhard Lazy:** There's Tilde.dev as well. There's a couple like that... But what I really want to do, having listened to the GitHub Code spaces episode on the Changelog (I forget the number), I tweeted Cory, like, "Hey, we should talk." He said, "Yeah, sure. Email me", and I didn't have time to follow up on that email. But I really want to do that, because I see the potential of GitHub Code spaces, but I would use it slightly differently now. We're always up for partners, aren't we, Adam?

**Adam Staravia:** Yeah.

**Gerhard Lazy:** So if GitHub wants to sponsor Changelog with the GitHub Code spaces, we'll be more than happy to use it, and help it improve. But my first go-to would be what I know, right? Like, bare-metal servers somewhere, or Li nodes, or wherever, spin them up... And that's where Cross plane comes in. There's like a couple of things happening in the background that will start coming together. There's an Equinix Metal episode with Zac coming. Number 29, I think. Actually, it came out... By the time we're listening to it, it came out, the episode with Zac.

So there's like a couple of things coming together, which make me really excited, and which I think setting anything locally for development - it is a time sink, and should have environments which are pre-built for development in an automated way, and you just click a button, and you have it. And when you're finished with it, you take it down, and you don't have to worry about it. You don't have to worry about upgrading PostgreSQL, or are you running the right version of Erlang, or should you install Docker, or put up with Docker desktop updates, which have been getting really annoying in recent months, which is one of the reasons why I uninstalled it.

**Adam Staravia:** My main issue has always been -- I manage Homebrew, I upgrade some things in there. I don't want to specifically upgrade particular things, so I say ‘upgrade all’ essentially, or just ‘brew upgrade’ after update, and next thing you know, Postgres is updated to the latest and my Postgres is broken... And that was always the culprit. And then a couple of times, it was Erlang, and that kind of thing.

Because my local hackery things that aren't really connected to a dev environment shouldn't overlap with my actual dev environment for the application. I'm kind of in that weird space where it's like my truck - I have a gas-guzzling Ford F-150. I love the new EV F-150, the Lightning coming out. Furthermore, I want to buy a new truck sometime soon, because I’m due, it's like seven years old... But I don't want to buy a gas vehicle. I want to buy an electric vehicle.

\[43:49\] So I don't want to spin up my own dev environment. I want to use Code spaces, or some prescribed dev space that I don't have to worry about, that's always just fresh... Because I’m me, my identity is me, you know my trustworthiness, or the application should, or our config should, so I can then get access to a certain database maybe a drive-by contributor shouldn't get access to... That kind of thing. And even drive-by contributions - those are harder to do, probably. Maybe through dot dev it's somewhat easy if it's a typo or something like that. But if it's a contribution, I think it's much easier for us.

**Gerhard Lazy:** So I'm thinking of the GitHub Code spaces experience, but maybe not necessarily running on Azure as it is today. But I'm not suggesting that we should all set up some bare-metal servers. No way. It's an approach that our contributors should be able to use as well. And you're right, identity should be baked in. But that's like the long-term. Short-term. I think you want the short-term. The short-term answer is use your old machine. \[laughs\]

**Adam Staravia:** I would say short term answer would be "Can we get sit up on Code spaces in their current blessed way?" and hope for a future where they have a more infinitely configurable version that's for the ways you want to use it. So I'd say let's re-engage with Cory and GitHub on that front. I know they’re willing, we've talked to them recently, so we know they're willing. That gate has not closed. They want us to be on Code spaces and leverage it that way.

**Gerhard Lazy:** Amazing.

**Adam Staravia:** So I'd say let's use it the way they want us to use it currently, get going that way, and then whenever it needs to scale in different ways, then it can. Or you can use Gitpod to do it your own way with Equinix Metal, because that's what Gitpod does, right? Gitpod lets you be anywhere; they're agnostic. Whereas Code spaces is simply GitHub, simply Azure infrastructure.

**Gerhard Lazy:** I'm happy if the Changelog.org would have this capability, if GitHub Code spaces was part of the Changelog.org, and we could use it out of the box. I think that would be amazing, right? So if we can contribute to that, and we can make sure that anyone wanting to contribute that the Changelog app, we could get that working very well with Code spaces, which currently isn't... That, you're right; that is a good short-term solution. So I think you just gave me a Christmas gift, Adam.

**Adam Staravia:** I'm going to hold on to that. I’m not going to set it up locally. I’m going to wait -- I’m going to wait for my Christmas gift, which is Code spaces wrapped in a bow.

**Jerold Santo:** The challenge with this path being short-term is that Gerhard is the most organized podcaster in the universe, and he's scheduled it into March and April. \[laughter\] So that doesn’t sound very short-term to me.

**Gerhard Lazy:** I’ll need to make room. I'll need to -- I don't know, someone cancel an interview, maybe... \[laughter\]

**Adam Staravia:** No, here's what can happen... Honestly, behind the scenes, what happens is you may plan that way, but you have got to plan for a buffer; even if you have it planned out, there's always a -- Jerold and I have done this, too. We've had it planned up several weeks to a month, and something happens, and we're like, "We’ve got to go change the order."

**Gerhard Lazy:** Yeah.

**Adam Staravia:** And so because you get to run the show, you can make those calls.

**Gerhard Lazy:** Yes.

**Adam Staravia:** Just because you're setting that motion. Now, if you've made a promise or whatever, reach back out to them and say, "Hey, I'm sorry. We've got a timely episode coming out. I need to bump you back one week." They're probably not going to be upset. And if they are, give them a free T-shirt, or whatever it takes to make them sweet

**Gerhard Lazy:** How do you do that? I don't know how to give them a free T-shirt.

**Adam Staravia:** You tell me or Jerold.

**Jerold Santo:** We'll talk offline. We'll talk offline.

**Gerhard Lazy:** Alright. Okay.

**Adam Staravia:** It's too easy. And we'll make it happen. It’s too easy.

**Gerhard Lazy:** Okay. It's amazing, what a free T-shirt will do... \[laughter\]

**Adam Staravia:** Yes. We love our listeners, and we love our guests just as much, if not more... So if ever we have to apologize, we’ll do it with very sweet kindness.

**Gerhard Lazy:** Alright. GitHub Code spaces in December, here I come.

**Jerold Santo:** There you go. Let's make happen.

**Gerhard Lazy:** Let’s make it happen.

**Jerold Santo:** Christmas is coming early. Or right on time. So I think the actual short-term solution is brewed install Elixir, brew install Postgres, clone the repo...

**Gerhard Lazy:** I don't think that's going to work.

**Jerold Santo:** Why not?

**Gerhard Lazy:** I guess the versions have changed. I never even tried—I think by default PostgreSQL will be version 13, or maybe even 14 if it's out yet. I don't know whether things will work with that.

**Jerold Santo:** Oh, it does. I’m running it.

**Gerhard Lazy:** Are you? Okay.

**Adam Staravia:** And the README is a little off, too.

**Gerhard Lazy:** The README is off. Yes.

**Adam Staravia:** ...in terms of what it prescribes. It just said dependencies are Elixir and Erlang; it doesn't say which Postgres, and everything else.

**Jerold Santo:** \[48:16\] Just wait for the transcript to come out, of this episode, and then follow that. I'm telling you, brew install Elixir, brew install Postgres, clone the repo...

**Gerhard Lazy:** Okay. So first step--

**Jerold Santo:** `mix deps. Get`

**Gerhard Lazy:** ... Gerhard gets a new MacBook M1 for Christmas. \[laughter\]

**Jerold Santo:** I already got one, Gerhard. I can do this work.

**Gerhard Lazy:** Alright. Just post it to me. \[laughter\]

**Jerold Santo:** Well, unfortunately, with the ship dates on these new MacBooks, I also don't think that's a short-term solution either.

**Gerhard Lazy:** I know. 4–6 weeks. I've seen that. Yes, I know what you mean.

**Adam Staravia:** You had to order it like a month ago to get it on time for Christmas.

**Gerhard Lazy:** Yes, I know.

**Jerold Santo:** Alright, so the short-term solution is keep your old machine around, and use that till we have a medium-term solution.

**Gerhard Lazy:** Exactly. Yes.

**Adam Staravia:** Which I do. It's right next to me. It's no problem to use it. But, like anybody, I want to get set up on this new machine and never look back to the old, and just format the drive and roll on.

**Break:** \[49:15\]

**Jerold Santo:** Last Kaiden we talked about moving our uploads to the cloud, specifically S3 is cloud. I wanted to give a quick update on progress there. I wanted to have it done by the time we recorded this, and the fact that Gerhard, you and I met (was it last week?) to discuss a game plan to getting us from where we are to 100% cut over. We did not quite get there, and that's because I had a yak shave instead. So I thought I would take you guys on a little journey.

**Gerhard Lazy:** I did a few as well, so it's okay. Your yak shave held yak shaves. It's all good.

**Jerold Santo:** \[laughs\] So... You know, I only have so much time to work on the platform, and I have to use that time wisely, and sometimes it's GitHub issues-based development when things come in, because then you know it’s a user or a listener or a reader’s need, or something that they hit up against. So I end up prioritizing things that I want to do; probably not always the wisest... But it happened again. I had my waffle branch, which waffle is the new replacement for Ark. Ark is the upload library that we had used previously, that went unmaintained, taken over by the community and now called Waffle... And so we've cut over to that, I have my branch... It's like, I said it was -- what did I tell you? How many percentage points did I have done when I told you the other day, Gerhard?

**Gerhard Lazy:** I think it was like 90%.

**Jerold Santo:** 90?

**Gerhard Lazy:** Yes, 90% is what I remember.

**Jerold Santo:** Yeah. So probably I'm at like 94% now... And then here comes an issue, issue number 393 hit our GitHub issues, which we'll link up... Newsletter links proxy encodes special URLs with HTML instead of percent based. This is a tiny little bug that was just interesting to me.

\[51:59\] So what happened is, in our Changelog weekly newsletter, which goes out every Sunday morning, it includes all the shows from that week, every episode we put out, as well as all the news and the links and the repos and the commentary for the week, we linked to Chris Manson's post called It's All Gravy. And his website is Chris.manson.ie, probably because he loves Internet Explorer, and then /it's-all-gravy... Only it is a contraction, right? So, it's, its apostrophe s. And the son of a gun left the apostrophe in there. Now, I'm giving him a hard time, because I know Chris, he's a JS Party listener, hangs out in the chat... And he left that apostrophe in the URL. First, isn't that just like, blasphemous right there, having an apostrophe in your clean URLs, people?

But what happened with that apostrophe is the way that we encode that creates the HTML encoding instead of percent-based, which you'd expect in the URL, which caused people that clicked on that link in our newsletter to go to a web page, which was a 404, because it was incorrect.

Now, certain browsers actually manage it okay, and the apostrophe looks fine in the address bar and everything, which I thought was kind of interesting. And so I thought, "Here's a bug I should chase down, while not working on these uploads to the cloud branch that I'm supposed to be working on..." And so I started to figure out - okay, mystery time... What is going on here?

So I dive into our codebase and I find the line of code in question, and everything looks legit to me, and then I realize, okay, I'm calling this Phoenix... So we are an Elixir/Phoenix application, for those who haven't been following along the whole time... And at a certain point, we call into Phoenix. And Phoenix has an HTML library that generates HTML, and there's a function called link... So if you're familiar with -- every web framework has like a link function; link to was Rails’ invention, which everybody's pretty much copied. Phoenix’s link works very similarly. So all we're doing is calling that and just passing it the URL, which has the apostrophe in it.

So I started digging a little deeper, and I started thinking, it's like, "Whatever is happening is outside my domain, right? It's a dependency that's doing it." So I don't know, Gerhard... What do you do in this circumstance? You’ve got a dependency that's not doing something totally right? What's your first move? I guess you're more of an ops guy, so maybe your developer chops are maybe rusty, but what’s your instinct?

**Gerhard Lazy:** No, not really. Not really.

**Jerold Santo:** Okay, good.

**Gerhard Lazy:** So I would look at an issue to see if there is an issue in the repo for the DEP. I would try and find the code, see what happened around it. Like, I would call a blame, see if that is different... And if I can't find anything, I would just open an issue on that repo, explain my problem, link to my code, and ask the developers, "Hey, how would you solve this? What do you think? Is it legit? Am I holding it wrong?"

**Jerold Santo:** Yeah, exactly.

**Gerhard Lazy:** "What’s the problem here?"

**Jerold Santo:** Yeah. So the interesting thing about this one is I'm not really savvy with these character encodings, and I'm not sure why it's doing the HTML encoding versus the URL encoding, but my first question is, like, is this even a bug? Or is this just like the way it would work if you pass it an apostrophe?

And when I start to have these questions - you laid out a very clear path to potential victory, but I'm lazier than you, so my first thing is like, "Am I running the latest version?" That's just what I ask myself. Like, maybe this was fixed between my version and now. So my first step is, "Well, let's just upgrade stuff." And I start to -- even if it's like a procrastinating thing, I'm like, "I'm going to go check out my deps tree and see how old everything is." A bunch of stuff was out of date, so this begins the yak shave. So instead of fixing that, I'm like "Here's what I'm going to do - I'm going to update all of our deps."

**Gerhard Lazy:** \[56:11\] Update everything. Oh, my goodness me. Okay... What can possibly go wrong...? \[laughs\]

**Jerold Santo:** Exactly. So we're on Phoenix 1.5, and 1.6 was out. Most Elixir packages do a pretty good job of following semantic versioning. So I knew this was a minor upgrade, so there are some breaking changes, but -- or no, a major upgrade breaks changes. There shouldn't have been any API changes, right? Yeah... So this one kind of bit me. So there were API changes. \[laughs\] So I thought I could just safely upgrade. And I did all the auto upgrades... So inside of Elixir's mix tool, if you have patch version upgrades, it'll just auto do those for you. They're green, you can just upgrade those, because they're assuming semantic versioning.

So I did all those, ran the tests, everything was fine. Then I went to upgrade Phoenix, which was a minor version upgrade from 1.5 to 1.6. Got that done. While it was kind of doing its thing, I was like, "Well, I'm going to go read the changelog and see what's going on." And I did notice that they made a breaking change, which I guess that's not SemVer, so that should have gone to 2.0. They don't want to go 2.0, because it's too major, or whatever... But I did notice it, and I'm like, "Man, this is something that I need to look at." So I did the upgrade to Phoenix 1.6, had some failing tests... I was like, "Alright, good. My tests are testing things, and they change the API..." And so I'm going to have that, but it's like two changes.

So what did they change? Well, the way Phoenix works as it passes the request data from your controllers down into your views and to be used in the template, there's this bag of data called assigns, and in the assigns, there’s a bunch of -- it’s literally a map, or a struct, or a dictionary, or a hash, depending on what your language of choice is, right? So it's keys and values, and there were two keys that no longer exist - view module and view template. What do these keys hold in them? Well, they hold in them the information of what's the currently active or being used module that's handling this request, and which template is going to be used to render.

So I did find those. There were two places I was using those, and I changed them. And there was a new way of doing it. Fine. And I upgrade, and all my tests pass, and so what do I do? I ship it, baby. I send it out there, and it's all good. And then I start to realize, via Twitter, that our Twitter embed’s broken. It's just showing like the default news and podcast for developers thing, and like a stock share image. We actually have player embeds, where you can click play right there on Twitter and start playing the episode. So that Phoenix upgrade, even though I thought I'd covered all my bases, broke all the metadata on all of our pages, across the entire site.

**Gerhard Lazy:** Wow...

**Jerold Santo:** ...which led to Twitter embeds breaking, all third-party integrations that are based on the meta elements in your HTML - busted. That led to me refactoring our entire meta module, because that data is gone, and the entire thing in that module is like, "Which view am I, and which template am I? Okay, here's my meta information." So I refactored that entire meta module; it took me a few hours... I'm not even happy with the way it works now. I liked it better before. And I fixed it... And the yak was shoved, or shaven. What's past tense for shave?

**Gerhard Lazy:** Shaven.

**Jerold Santo:** I shaved it. I shaved that sucker. But I did not get our cloud uploads done... So that's my excuse, and I'm sticking with it.

**Gerhard Lazy:** Well, first, you were very determined to shave this yak... \[laughter\]

**Jerold Santo:** Yes, I was.

**Gerhard Lazy:** And I'm glad that you didn't give up, until it was all done.

**Jerold Santo:** Success, baby!

**Adam Staravia:** Yes. Well, the question is, did the upgrade even fix the original URL issue?

**Jerold Santo:** \[01:00:15.25\] No... It’s not a bug. It’s a feature. \[laughter\]

**Adam Staravia:** That's the best!

**Gerhard Lazy:** By the way, the number is 394. I checked. It’s not 393. 394.

**Jerold Santo:** Oh, I’m sorry.

**Gerhard Lazy:** That's okay. That's okay. Second of all, this reminds me of exactly what happened. You said that you had to shave a yak, and we had to get together, where I upgraded -- I've set up the new version of our Kubernetes deployment... And it's amazing how I was shaving a similar yak.

You know how you do an upgrade of Kubernetes, like from 1.20 to 1.21, and then you think, "Hmm, maybe I should upgrade Ingress NGINX. Or even better, "I should replace it with Traffic." Why? Because then we don't have a cert manager. Excellent. So, Traffic and take care of all of that. Great.

What about external DNS? Let's do that as well. What about Honeycomb agent? Let’s do that as well. What about Grafana agent? Oh, crap. They broke something... \[laughter\] So maybe try and figure out what the config is. And before you know it, like two days, like three days, whatever, you say like, "No, no, this is just too much. I just have to keep some of the older versions, because it's just too hard, and I'm biting too big of a chunk", which is exactly what you've done, right? And before we know it, the yak is like a herd. \[laughter\]

**Jerold Santo:** Yes. Somewhere in there I completely lost the thread, you know?

**Adam Staravia:** Yeah... It feels necessary as you keep biting more off though, right? As you go deeper into the yak shave. I mean, I guess this is an onion analogy more than a shave, I guess... Every new hair you shave away -- I don't know how to describe... Like, you just have to go further, you know what I mean? It feels like it's perpetual, and you just need to keep going. And then it's one part, personal determination, and then knowing you as a list, extra offer, you've got to get through this thing, whatever it is. So it's like, perseverance though...

**Gerhard Lazy:** I'm wondering, how much actual work happens like this? Really valuable work, like upgrades, fixes, refactorings... Because you start somewhere, and rather than doing the bare minimum, you say "Well, I'm going to do a little bit more, and a little bit more..." and before you know it, you're like a week in, and everything is amazing, but you’ve wasted the week on something which wasn't even on the board.

**Jerold Santo:** Right. It was not even on my agenda.

**Adam Staravia:** I wonder as well, because that's the state of flow, right? You can get through that yak shave, probably, because of a state of flow. Was this a sustained session, Jerold, or was it multiple sessions?

**Jerold Santo:** This was all one session. This is basically taken my afternoon that I would have otherwise spent finishing that cloud uploads thing.

**Adam Staravia:** Right. Did you plan to spend the amount of time that you spent? So did you consume the time you desired to spend, or did you consume more?

**Jerold Santo:** Way more. I did not want to rewrite that meta module at all.

**Adam Staravia:** Right. This is my point then. So you want to do it in one session, you were in a state of flow, despite your aim, so to speak, being off... You shaved the yak, you didn't do what you intended to. However, you probably did as much work as you could have done in eight hours, or whatever number - some sort of multiple beyond that - because you're in such a momentum mode going on. That's my assumption at least, because you were in a state of flow. So to your point, Gerhard, I wonder as well - because when you get that kind of momentum, sometimes you just have to run with it.

Speaking of new, we've got some gifts coming up. It's going to be the holiday season, Christmas... You’ve got some Christmas gift for us, Gerhard?

**Gerhard Lazy:** I do, actually. I have four, five... We'll see how many. But a couple. More than a couple.

**Adam Staravia:** \[01:04:03.00\] Okay.

**Gerhard Lazy:** What I'm thinking is, I was mentioning --

**Adam Staravia:** Two. More than one, right? Two.

**Jerold Santo:** More than two.

**Gerhard Lazy:** More than three.

**Adam Staravia:** More than two, okay. A couple.

**Gerhard Lazy:** More than a few. Several. Several gifts. So I was mentioning at the beginning of the show that a lot of the episodes, when I spend time talking to the people that come on the show, there's always a background story to it. Usually, like a past story we share, we have a common past, but also I see a common future.

What that means is when we covered Cross plane, I was mentioning even during the episode that I want to make Cross plane part of our infrastructure, part of our setup. So what that looks like is managing our Kubernetes, managing our infrastructure with Cross plane. So how do we do that? What does that look like? What is the simplest thing that we can do to improve our Kubernetes deployments, so that when you want two, three, four, it's really simple to do that? What about using Upbound Cloud for that, rather than running around Cross plane? So that is one of the gifts - how do we use Cross plane to manage our infrastructure, our new infrastructure, the 2022 one, and going forward, what are the benefits of doing that?

So we're bringing them on board, with our story, with our Changelog story, with our setup story that's been evolving... And the mix is what makes it amazing, because we have the opportunity to try all these different tools out, show our approach, whether it's right or wrong, it doesn't matter. The point is, it's good enough for us, and there's always something to learn. We create great content, we promote the good stuff, the stuff that we believe in, that we use, and most importantly, we help it improve. We get feedback to those projects, to those products, and as a result, they improve.

Honeycomb is another one. We’ll have specific Honeycomb integrations. Dagger - I want to mention that as well. And that happened like over the last couple of weeks... Preparing episode 33, where a few gifts will be mentioned. Parka, I want to mention that as well. That actually happened today. In my lunch break, we were recording that segment, which will be part of episode 33, and that's the Parka one.

**Adam Staravia:** Yeah. I like seeing Solomon Sykes in our pull requests/comments back and forth on the Dagger stuff you're working on. I was paying attention to just that commentary. And so just one... You know, I think it's super cool that -- you know, we've been a podcast... Ship It is part of the network, but the network itself has been around for more than 12 years now.

We talked to Solomon like way back early days of Docker even, when he did that first talk to announce Docker, essentially... And now to be at a place to have the right kind of infrastructure for this... What was just once a Tumblr blog, happily on WordPress at one point as well, and worked just fine. Maybe we had a ton of misses there. Not misses, but actual misses; but we didn't have any caching, so we were good to go. And now to see this feature, Dagger, these GIFs, and Solomon Sykes, who is one of the creators of Docker - those catching up in the comments of our pull requests... It's cool. I love that. I was loving seeing that. It’s just -- the whole circle of life kind of thing. You know, like you had said even with Ship It, the pre-story, and then the future story. Like, I love all that serendipity, Gerhard, really, coming together.

**Gerhard Lazy:** It is a journey. It's really being. And many journeys coming together.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** And the little contributions that we can make to those projects, they're definitely helping us. We couldn't run the infrastructure the way we do without all the great tooling that's out there. And I wish we had more time to try it all, and to give all the feedback that we can.

\[01:08:12.00\] I think whenever people pitch the idea or request an episode, like "We would like to have this conversation", I'm thinking, "Am I excited about this? Is this something which I would use?" If the answer is no, it doesn't mean that tool is wrong. It means I'm not into it. I wouldn't use it. It’s a no from that perspective. So I love trying out the things that we have on the show, all the people - just go beyond that, go beyond that conversation and see what happens. Literally, see what happens. I love that stuff.

**Adam Staravia:** I like bringing that feedback to them too, in particular Honeycomb. I love just -- or even with Dagger, and Cross plane. I think we can give that kind of feedback differently than, say, a customer would, or a drive-by user who's just on the free tier, for example, of whatever it might be. We're going to give a different layer. Because one, to Vastly’s credit even, like - if you’re a listener who works at Vastly, we're not bashing you. We love Vastly. We're just unhappy with current things or certain things, and we want to improve them. That doesn't mean we're negative Vastly. We're quite pro Vastly. And I think that through the podcast and the content that comes from it, and just our willingness to try and be curious, but then put that on air on a podcast and flesh it out, for the sake of ourselves, as well as the listeners, who are like, "How are they solving these problems? How is Jerold shaving this yak? How is Gerhard shaving that yak?" He has no packets lost. Great. Okay, cool. Two ISPs later. All that fun stuff. That, to me - that's a journey. That's a narrative. That's a story. And I think that we can give that feedback to Cross plane, to Honeycomb, and even sharing how we have that observability into our CDN which we never had before - that is super cool. That may not be something that Charity and the team at Honeycomb thought about. Sure, you can observe anything really, but have they considered, like, should you observe your CDN? Well, I think now that we have this tool in our hand, the answer is emphatically yes, especially when it's your front layer.

**Gerhard Lazy:** Yeah, and it's all those ANDs which are really exciting for me... So Cross plane AND Dagger. Honeycomb AND Grafana Cloud. Most people don't think like that. They think, "Competitors."

**Adam Staravia:** Either/or.

**Gerhard Lazy:** No, no. It’s an AND proposition, because they all have their strengths and their weaknesses. And if you don't know what the trade-offs are, well that means that you don't know them well enough. Because there's no such tool which is just perfection. There's no such thing. It doesn't exist. So stop looking for it, and try and understand which trade-offs you're making.

So Honeycomb is helping us in specific ways. Grafana Cloud is helping us in other ways, and we'll have people on the show to talk about those things, and to talk about the improvements. If you want to know what's coming up in episode 33, you can go to our changelog.com, the repo on GitHub, github.com/thechangelog. There are a couple of pull requests opened, and the pull requests have Shipped It Christmas gifts. It's an Echoes initiative, Echoes HQ; they were on the show. Arnaud was on the show. So we're using Echoes for that purpose, and it's all coming together, like one big, happy family—

**Adam Staravia:** And they’re red.

**Gerhard Lazy:** And they’re red, yes, for Christmas. Exactly.

**Adam Staravia:** That’s right. Red and white actually, because the text is white, and the --

**Gerhard Lazy:** Yes. It’s not coincidental. So there are many things coming together, and Dagger is improving, because it reflects some of the feedback that we're giving. Honeycomb as well. Cross plane as well. Every single person I get to talk to, they're taking notes of what they can improve. Fredrik - it was amazing to do that with him, to give him ideas... Because end users, the ones that are paying for it, for that product, they maybe are not as patient or not as knowledgeable, or they’re more entitled, or rushed, or...

**Adam Staravia:** Precisely. Willing.

**Gerhard Lazy:** \[01:12:21.13\] Exactly. But we’re not. We genuinely want to help. We genuinely want to promote this stuff - what works, what doesn't work, and let's make it better. So, Kaiden.

**Adam Staravia:** Yeah. I love that. And I guess, to some degree, on that note, there's an order of things. So we talked about this show, in the initial part of the show, just the beginnings, how there were early innings... It was just an idea at one point. And as part of bringing that idea to life, one, Gerhard, we had to have a deeper conversation with you, and understand your desire. Clearly, you've realized a lot of that desire for us in your execution of Ship It, even so far to plan well ahead.

But all that's possible because, one, our willingness, but then two, capable and willing partners behind the scenes. And in no particular order, I'm going to thank some people who were on the charge this year, involved next year as well... Planet Scale, Fly, Equinix Metal, Render, Linde, Ray gun, Sentry, Honeycomb, Grafana Labs, Teleport, Launch Darkly, Incident, Fire Hydrant, Cockroach Labs... And I'm sure at least a couple more that I may have forgotten and didn't get in the list. If so, I apologize, but... Great partners make it possible to do this kind of fun stuff, and I am so thankful for them. I'm so thankful for you. I'm so thankful for our listeners. What would this show be if it didn't have listeners, right?

So you're listening right now, we really appreciate you taking your time to either subscribe, or listen to a segment, or listen to a full-length show, even if you're not a subscriber. Thank you for giving us a little bit your time, hopefully a bit of your future trust and listen to this show further. We hope to one day have a beautiful vanity URL to give this, but until then, it's changelog.com/shipit. All the links to subscribe are there. You can subscribe via email, you can come in Slack... Hey, there is a community, it is free, so you can hang your hat, call this place home. Everyone's welcome, no matter where you're at in your hacker journey. We welcome you to be here. There are no imposters here. You can go to changelog.com/community for you to join, hang with us.

I love it, man. I'm loving the momentum and the direction we're going. Furthermore, I think enough pats on the back, but I'm just so thankful for this team here, the listeners, our partners... Really, I am. We’re just so blessed - really, we are - to be doing this show. It's so much fun.

**Gerhard Lazy:** Thank you, Adam. That was beautiful. Thank you very much. That’s reached a very special place. Thank you.

**Adam Staravia:** Cool. So 2022, here we come. We’ve got a little more shows left, but this is the last Kaiden episode. We'll come back here in 2022 with Kaiden, with Kaiden... 40?

**Gerhard Lazy:** Kaiden 40, that’s the one.

**Adam Staravia:** Kaiden 40. And hopefully, we'll have our Kaiden T-shirt in the merch store... So stay tuned to that. One more gift, potentially, a New Year’s gift, merch.changelog.com/. Until then, we’re out.

**Outro:** \[01:15:37.01\]

**Jerold Santo:** Hey you all, Jerold here. So during the tail end of our recording, right after I told my yak shave story, Gerhard pretty much broke the show. Turns out he's been deep on a yak shave of his own regarding his home network setup and some nagging internet connection issues. I guess my yak shave story triggered Gerhard to consider the ridiculous length he's gone through, and - well, hilarity ensues.

Gerhard laughs uncontrollably, which makes me laugh uncontrollably. Adam keeps it together and desperately attempts to get us back on track, but not going to happen. It was so broken that we cut it from the episode, but it was also so funny that we figured we'd throw it in at the end, for those of you with a few extra minutes to spare and the curiosity to hear what it sounds like when the show goes off the rails.

Alright, here it is.

**Gerhard Lazy:** I’m sorry. I’m just \[laughs\] I’m just trying to hold something in.

**Adam Staravia:** Something is making Gerhard laugh huge.

**Gerhard Lazy:** It’s just too good. \[laughter\]

**Adam Staravia:** Oh, he's got a hidden thought that he can't get out, because it’s making him laugh too much.

**Gerhard Lazy:** I just remembered... \[laughs\]

**Jerold Santo:** What? \[laughs\]

**Gerhard Lazy:** \[laughs\]

**Adam Staravia:** I can't even look at this face. I'm sorry.

**Gerhard Lazy:** It’s just too good—

**Adam Staravia:** I can’t look at him. I have to look away.

**Gerhard Lazy:** \[laughs\] Okay. Alright.

**Jerold Santo:** What did you remember?

**Adam Staravia:** If you’re listening to this, try hard to look away.

**Gerhard Lazy:** \[exhales\]

**Jerold Santo:** Okay, got it.

**Adam Staravia:** He's taking off his glasses and everything.

**Gerhard Lazy:** It took me three weeks... \[laughs\]

**Jerold Santo:** Three weeks? \[laughs\] Oh my God, man...

**Gerhard Lazy:** It’s just too good to-- \[laughter\]

**Adam Staravia:** That’s true determination, because you not only did it -- you didn't do it in one session, you did it in multiples, and you kept going.

**Gerhard Lazy:** Multiple weeks.

**Jerold Santo:** \[laughs\] Multiple weeks...

**Gerhard Lazy:** \[laughs\] Three routers later... \[laughing out loud\]

**Jerold Santo:** \[laughing out loud\]

**Gerhard Lazy:** Two internet connections later... \[Laughter\] And all my packets aren't getting lost anymore. \[laughter\]

**Jerold Santo:** Oh, man...! \[laughs\]

**Adam Staravia:** That is an extreme yak shave, Gerhard.

**Jerold Santo:** That is.

**Gerhard Lazy:** \[laughs\] I’m sorry.

**Adam Staravia:** Extreme tales of yak shaving. That’s the next show.

**Gerhard Lazy:** That is the next show. Actually, there's like an episode with new ISPs -- I have two ISPs now. Both fibre connections

**Jerold Santo:** Two ISPs now... \[laughing out loud\]

**Gerhard Lazy:** Yeah, like two fibre connections coming into the house. Three routers

**Adam Staravia:** The funny part about this is like -- you have to think about that beyond just being two ISPs, that's two separate people coming to your house to install fibre...

**Gerhard Lazy:** Yes.

**Adam Staravia:** Because that's two separate fibre lines. That's like true dedication. \[laughter\] That's new holes into your house.

**Gerhard Lazy:** \[laughs\] Yes, exactly. Two holes in my wall. You’re right. I have two holes.

**Adam Staravia:** That's one more plug in your -- whatever. Maybe you even have a UPS for this even, I'm sure...

**Gerhard Lazy:** Not yet. \[laughter\]

**Jerold Santo:** Not yet. \[laughing out loud\] He just added that to his list of things to do.

**Adam Staravia:** That's some serious dedication.

**Jerold Santo:** Don't give him anything else to do, Adam.

**Adam Staravia:** I'm just thinking like - the logistics of doing that. That's being on the phone to order it, that's deciding to pay for it. That's one more line item on the budget, so to speak. That's somebody coming in your house, new hole, new fibre, new equipment. At least you're getting to use that LAN fill over though, on the unify system

**Gerhard Lazy:** I do actually, yeah. I do. Not load balancing yet, but I'm working towards it.

**Adam Staravia:** I’m sure you’ll be -- yeah.

**Gerhard Lazy:** \[laughs\]

**Jerold Santo:** Alright, we’ve got to reel this in. What's the summary here, Gerhard? What's the takeaway from this?

**Gerhard Lazy:** The summary is that now I have two LAN connections

**Jerold Santo:** \[laughing out loud\] You've already said that part. What's the takeaway?

**Adam Staravia:** What's the takeaway here?

**Gerhard Lazy:** You need two of each. \[laughing out loud\] Except your life. You only want one of those.

**Jerold Santo:** There you go. So I think we should do Gitpod and Code spaces. \[Laughter\]

**Gerhard Lazy:** \[laughs\] Of course.

**Adam Staravia:** Yes, because you never know.

**Jerold Santo:** Kubernetes AND Fly.io, AND Render. That’s how we roll.

**Adam Staravia:** Well, I can agree with the N-plus. I mean that is smart. I mean, you can never have enough. That was actually coined best in the movie Contact. Anybody remember that? Why build one when you can build two?

**Gerhard Lazy:** I think I've had enough fun... \[laughter\]
