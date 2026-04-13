**Jerold Santo:** Alright, Kaiden. Gerhard, we are here to Kaiden. The first Kaiden after our onstage Kaiden.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** How's it going? How's your life? Your life has changed since then.

**Gerhard Lazy:** It has, yes. Yes. A new job that started in early September, actually; September brought in that change. It was a good change. As you know, new jobs are always exciting. There's always so many things to do, and we have to meet everyone on board, do things properly... So that was really the whirlwind. I really enjoyed that very much. Well, obviously before that even, we had our family holiday, which was amazing. I always love going outdoors and spending -- the proper outdoors not the... Well, the mountains.

**Jerold Santo:** Is that what the proper outdoors is, the mountains?

**Gerhard Lazy:** Exactly. The proper outdoors for me is mountains, and lakes... That just goes together.

**Adam Staravia:** \[unintelligible 00:05:12.25\]

**Gerhard Lazy:** Yeah, which is why Denver was really, really nice. I really enjoyed that. It was close to what I enjoy. But otherwise -- I mean, how is it October already? That's what I don't know.

**Jerold Santo:** Right?

**Gerhard Lazy:** It was July, and then now it's October. How did that happen?

**Adam Staravia:** Well, there's this thing called time...

**Jerold Santo:** Every 24 hours you change the day...

**Adam Staravia:** It just keeps going. You know, I'm with you on that. I don't know how it's October. I feel like it was just January. Furthermore, I feel like it was a very fast year this year, for some reason.

**Jerold Santo:** Yeah. Agree.

**Adam Staravia:** It was going slow, and then it got really, really fast.

**Jerold Santo:** That's kind of how life goes, right? It starts off slow, and you're like 10 years old, wishing you were an adult, and you're like "When am I going to be able to drive? When am I going to be able to drink legally?" I don't know what the 10-year-olds want to do anymore, but... \[laughter\] Back when we were kids... And then you get there, and you're like "Slow down, life." And then now all of a sudden you're in your forties, and you're like "Holy cow." Life is like a vapour.

**Adam Staravia:** \[unintelligible 00:06:10.23\]

**Jerold Santo:** Totally. Tell us about the new job. What are you doing now? You spent years at Dagger...

**Gerhard Lazy:** Yeah, it was almost four years, it was time for change. The new company's called Loophole Labs. They're focusing on infrastructure primitives, some fascinating things that revolve around live migration... That is definitely the central piece. And when I say live migration, I mean the memory, the disk, the connections... How do you migrate connections from one host to another? I find that fascinating.

What's most interesting is the size. So if you have 64 gigabytes to migrate, how do you do that in milliseconds? I mean, what does your connection even need to look like?

**Jerold Santo:** Migrating between physical hosts?

**Gerhard Lazy:** Between physical hosts.

**Jerold Santo:** Really?

**Gerhard Lazy:** Yup. Not VMs.

**Adam Staravia:** 64 gigs?

**Gerhard Lazy:** Mm-hm...

**Jerold Santo:** You might need like a hundred gigabit home lab to do that.

**Gerhard Lazy:** Exactly. That is coming up, yes. That is coming up indeed. So that just sent me down that rabbit hole, like "Okay, so I need a new home lab basically, because 10 gigabits is just not enough. So what would a hundred gigabit look like?"

**Jerold Santo:** I know what it looks like. I've been watching your channel, dude...

**Gerhard Lazy:** \[laughs\] Alright. What did you think?

**Jerold Santo:** I'm loving it. I love seeing the -- you've got lots of engagement... That video blew up, "The hundred-gigabit home lab." I love the production quality. I know all the -- I know you sweat the details. It's fun to watch, and the narrative is cool, and... Yeah, I'm just happy for you. It's going well.

**Gerhard Lazy:** Yeah. I'm just so pleased... And it's part of today's Kaiden as well.

**Jerold Santo:** Oh, it is?

**Gerhard Lazy:** Everything connects. Everything connects, seriously.

**Jerold Santo:** It's all one continuous connection. Adam, have you seen any of Gerhard's recent videos?

**Adam Staravia:** Not as recent, but I've seen them before. Not this hundred-gigabit, so I'm a little jealous.

**Jerold Santo:** You'll like this one, because it's kind of up your wheelhouse. Although his home lab is better than yours... I mean, that's the sad part. I mean, happy for him, but sad for you.

**Gerhard Lazy:** \[08:09\] So I think this is going to be almost like a challenge. Like, how can we improve the home labs, too? Linux, Ubuntu, Arch, a couple of things are going to come up... Networks, because they're fascinating... GPUs - how do you run all this stuff in a way that does not break the bank? Because that's the other consideration. I'm not a data centre... I wish I was, but I'm not. Furthermore, I'm very sensitive to noise, so I can't have like fans blaring, and 1U, 2U servers, the really shrill ones... So I'm just the Noctua person, that goes for whisper-quiet everything; even fanless, if it's possible... I tried fanless for a hundred gigabits, and it runs really hot. That's the one thing which I was not expecting, just how hot these things run. 400 gigabits is even more crazy, and 800... Wow. So that's really like the next frontier. That's what I'm looking at: 400, 800 and beyond... And all this to service some workloads that have very sensitive latencies in terms of throughput latency... I mean, how do you run a remote GPU? I mean, that's crazy. And what I mean by that - the GPU is in a rack, you're on your laptop, and you're running against the GPU. So you have an NVIDIA GPU on your laptop. How does that even work?

**Jerold Santo:** So the software on your laptop believes there's a GPU available to it, but it's over the network.

**Gerhard Lazy:** The kernel.

**Jerold Santo:** Oh, the kernel.

**Gerhard Lazy:** It's a kernel extension. And it's presented as a local device, but it's actually a remote device. So it intercepts all the calls, and it has to have very low latency and very fast network to carry all this stuff around, and it makes it appear as if it was local.

**Jerold Santo:** That's amazing.

**Gerhard Lazy:** NVIDIA GPUs in MacBook pros. I never thought I would see the day.

**Jerold Santo:** That's crazy.

**Gerhard Lazy:** Yeah, I know. So that's like a preview into the new job and what's coming. It's only been like a month. I can't believe it's already been a month... But it all connects. It really all connects, and that's the important part. So all roads lead to Changelog. Isn't that what Adam keeps saying?

**Jerold Santo:** That's right.

**Adam Staravia:** Yes, sir.

**Jerold Santo:** There are many ways to get to Changelog.

**Gerhard Lazy:** Indeed.

**Jerold Santo:** Do you have a visual aid for us this Kaiden? Do you have a deck? Did you bring your deck?

**Gerhard Lazy:** Oh, yes. Always, always. So we need to trust screen-sharing... October 16th, I'm going to try an intro. See if you like it.

**Jerold Santo:** Okay.

**Gerhard Lazy:** I'm going to try and do the job easier for like the intro.

**Jerold Santo:** Okay.

**Gerhard Lazy:** It's October 16th, 2025, and you're listening and watching Kaiden 21, where Adam, Jerold and Gerhard do some mopping. Not moping, mopping. Double P. Mopping.

**Jerold Santo:** Mopping. Not moping.

**Gerhard Lazy:** Yeah. So stick with us to the end, so that you can rate our mopping performance. That's the plan.

**Adam Staravia:** I'm so good at mopping.

**Jerold Santo:** I'm going to find out how good I am.

**Gerhard Lazy:** Alright, let's do that. Well, the audience gets to rate us. So at the end of this -- this is all, again, leading to some performance rating, some mopping performance rating.

**Jerold Santo:** Gosh, I'm getting nervous already. Here we go.

**Gerhard Lazy:** Launching Ripely together was one of my 2025 highlights. I mean, seriously.

**Jerold Santo:** Ditto.

**Gerhard Lazy:** It was just so amazing. After 18 months of building Ripely in the open, with Friends, we shipped it on stage in Denver, and it was so awesome. Seriously, such a great feeling. The audience was clapping, Jerold and Adam were smiling... I was so proud of what we have achieved. Really, really proud. But do you remember what happened a few hours right after we did the stage bit?

**Jerold Santo:** \[11:57\] Uhm, hiking?

**Gerhard Lazy:** Yes... And before that there was something else...

**Jerold Santo:** Lunch?

**Gerhard Lazy:** Lunch, yes. Yes. That's right.

**Jerold Santo:** Adam, help me out here...

**Adam Staravia:** A selfie?

**Gerhard Lazy:** I don't know what you remember.

**Jerold Santo:** A selfie?

**Gerhard Lazy:** Yeah...

**Adam Staravia:** Well, this is not a selfie, technically... This is more of a--

**Jerold Santo:** Take us where you -- that's a gangster selfie right there.

**Gerhard Lazy:** This is like a gangster selfie. I really like it.

**Jerold Santo:** That's right. Technically --

**Gerhard Lazy:** I think it's one of my favourite pictures.

**Jerold Santo:** Technically not a selfie, but that's a great picture right there. A Kaiden for next time, an improvement suggestion for next time... Emo night? Emo night Brooklyn? I think we have to just --

**Jerold Santo:** Oh, that's the other... For those not watching, but listening, underneath the marquee, which - we made sure that they put the Changelog Podcast on their marquee... And underneath there, apparently that night is going to be emo night Brooklyn, which is a weird thing to have in Denver, but...

**Gerhard Lazy:** Yeah. And it reads as if the Changelog Podcast, that's what's happening.

**Jerold Santo:** It's our emo night Brooklyn.

**Gerhard Lazy:** There should have been like a line between the two. Alright, so we wrapped it up at the venue, we went to lunch, and after we went to a hike.

**Jerold Santo:** That's right.

**Gerhard Lazy:** But right after lunch, as I was getting ready for the hike, I thought to myself "Let me check the fly.io metrics."

**Adam Staravia:** Oh, my gosh...

**Jerold Santo:** Okay, I know where you're going with this.

**Gerhard Lazy:** \[laughs\] Alright. So for those who are listening, we are looking at a point in time snapshot of the fly.io app Grafana dashboard for Pipe dream. So for the CDN that we'd just launched, we're just looking at that screenshot. So I think I was mentioning Pipe dream and Ripely. Do you still remember, Jerold, the difference between the two?

**Jerold Santo:** I do. So Ripely is the software. It's the open source project that allows us to run Pipe dream, which is our instance of Ripely's running on Fly's network that actually serves as our CDN. Correct?

**Gerhard Lazy:** That's right. Yes, that is correct. And Pipe dream?

**Jerold Santo:** Pipe dream is -- I think I just told you what Pipe dream was.

**Gerhard Lazy:** Oh, okay. Sorry. Yes, you did. \[laughter\]

**Jerold Santo:** There's a trick question at the end...? \[laughs\]

**Adam Staravia:** Let me bump that up for you here...

**Jerold Santo:** Do you just want me to say it cleaner? Yeah, Pipe dream is our Ripely instances running as a distributed network around the world on Fly's network.

**Gerhard Lazy:** That's it. Yes.

**Jerold Santo:** Okay.

**Gerhard Lazy:** Ripely, the generic one, Pipe dream, the specific one just for us.

**Jerold Santo:** Because it was our pipe dream.

**Gerhard Lazy:** Yes, exactly.

**Jerold Santo:** But Ripely is for everybody. It's not just for us.

**Gerhard Lazy:** Exactly. Yes, that's where we're going with this. That's right. So we're looking at this Grafana dashboard, and clockwise we see Pops by traffic in North America. That is the top left. Network IO in the top right. And CPU and memory utilization at the bottom. What stands out to you?

**Jerold Santo:** CPU utilization stands out to me, because at about 1437 it went nuts.

**Gerhard Lazy:** That's it. Yeah, yeah. So that's exactly what happened.

**Adam Staravia:** A hundred percent nuts.

**Gerhard Lazy:** Yeah. It was crazy.

**Jerold Santo:** There's a title... A hundred percent nuts.

**Gerhard Lazy:** A hundred percent nuts. Like, CPU just freaked out. So after we updated DNS on stage, once DNS propagated and more traffic started reaching our shiny new CDN, some instances were just getting overwhelmed. And users hitting those Pops, they started experiencing a slow and unresponsive Changelog.com. We're going to pretend that there's a Bad Boys meme here... We bad-bossed it.

**Adam Staravia:** Oh, my gosh...

**Jerold Santo:** What's the bad boys' meme? I don't even know if I know this meme.

**Gerhard Lazy:** You know, when stuff blows up, and they just walk away \[unintelligible 00:15:35.20\]

**Jerold Santo:** Oh, they're walking in front of the explosion.

**Gerhard Lazy:** Exactly, and stuff blows up behind them... So that's exactly what I did. I have to take responsibility for this.

**Jerold Santo:** You exploded everything.

**Gerhard Lazy:** Pretty much. And the CPUs, they were on fire.

**Jerold Santo:** And you just walked away. You went to lunch.

**Gerhard Lazy:** Yeah. So honestly, I under-provisioned.

**Jerold Santo:** Okay...

**Gerhard Lazy:** \[15:55\] So our CDN was running on these tiny instances, and it just didn't get very far. So we're looking at an impossibly tiny bike that someone is actually riding. That's what we're seeing right now.

**Adam Staravia:** I can't even believe they can ride that bike, by the way. We're watching a video. I don't know, is this on -- okay, it doesn't matter. There's a video with a bike, and a dude on a very, very small bike, and... It's impossible to ride that thing.

**Gerhard Lazy:** Well, if you're watching this maybe this will make it part of the B-roll. Who knows? We'll see. We'll see what the editor will decide. But I under provisioned. I mean, that's really what happened.

**Jerold Santo:** Okay...

**Gerhard Lazy:** And I know that you've heard me say this many times over the years in the Kaiden... I'll say it again. Always blue, green. Always. And in this case, it means that it -- in this case, it meant that all infrastructure remained in place. We just deleted some DNS entries on stage in Denver, and because we took that approach, really, all I had to do was to add the DNS records back, and confirm that the traffic was coming back to life. Everything was healthy again, so it just took minutes... It took maybe 10–15 minutes for everything to propagate; up to 30, but that was just like the edges... And everything was back to normal. And because we blue-greened, there was nothing that could not be undone rather quickly.

**Jerold Santo:** Explain the concept of blue/green for those of us who aren't Sees.

**Gerhard Lazy:** So blue/green in this context means whenever you introduce a change, try to introduce it alongside what you already have, what you're already running. Because if you run the new system in parallel, it means that it's very easy to go back to the previous system.

In this case, one is blue and one is green. So rather than doing an in-place replace, replacing in place whatever you're running, doing an in-place upgrade, or taking things down and putting the new things up... You don't want to do that. You want to run two of the same setup, and then either gradually - which is what we did; we were gradually migrating traffic. That's why we knew that 20% was good, 30% was good... So again, we're not news. We've done this before. But in this case, I just could not estimate how much traffic it will hit the new instances, and especially bot traffic. I mean, there was a lot of bot traffic. I don't know whether it was LLM scraping... Furthermore, I don't know what exactly it was, but there was a lot of traffic hitting specific instances, and they were just like falling over. They didn't have enough memory, they didn't have enough CPU...

So in this case, because all the previous infrastructure was in place, updating the DNS record, and in this case adding some DNS records was enough for the previous IPs to start propagating, and then everything continued working as before.

**Jerold Santo:** So the actual mechanism that you used in order to do a blue/green with a CDN was running both CDNs concurrently, and using DNS to just point different directions. And so your rollback was literally just to go delete the new DNS entries, or a few of them. We had options...

**Gerhard Lazy:** So when we were on stage, we were serving, I think, five IPs. One IP was the new CDN, and the four IPs was the previous CDN... Which meant that 20% of the requests based on how DNS would resolve would hit the new CDN, and then everything else would go to the existing CDN. Now, I think when we were on stage, I think we were maybe one in three, so we were about 33%... It was more than one, because that's how we started, like 20% --

**Jerold Santo:** And we took it to 100%.

**Gerhard Lazy:** Exactly. So on stage we took it to 100%...

**Jerold Santo:** And then we went to lunch.

**Gerhard Lazy:** We went to lunch... I checked the numbers, like "Crap! This thing is on fire." It was really like blowing up. So all I had to do is add back the previous IPs, so that when DNS queries would hit --

**Jerold Santo:** So that Vastly would serve some of our requests, and Ripely would serve others.

**Gerhard Lazy:** Exactly, exactly. So we went back to about 33%.

**Jerold Santo:** \[19:59\] Okay. So they couldn't handle 100% with the underprovisioning that you had done with our Fly VMs.

**Gerhard Lazy:** That's correct, yes. They were too small, they didn't have enough memory, not enough CPU, and there were too few of them. There were certain hotspots that needed more than one instance, and that's what we did.

**Jerold Santo:** Okay. Mop it up, Gerhard. Mop it up.

**Gerhard Lazy:** Exactly. I was mopping in that case. Well, instead of dealing with a Changelog.com incident, we went hiking.

**Jerold Santo:** That's right.

**Gerhard Lazy:** Like, nobody knew that this thing had happened, right? And this is video, so it's actually \[unintelligible 00:20:33.08\] So we were relaxed, we enjoyed great conversations... Jerold was looking for great drone footage to shoot for news...

**Jerold Santo:** That's right.

**Gerhard Lazy:** We were in the amazing Red Rocks area, which is just where Jerold is pointing very soon. He's coming up to pointing it. He was like "See?" Looking around, "Where can I fly this thing?" And look at that. There, let's go there. That's where the Red Rocks area -- did you use any of the footage that you shot, Jerold?

**Jerold Santo:** I did create one episode that featured B-roll from Denver... I'm not sure how much or if any of that was actual drone footage. I had to fly the drone all the way across the valley to get it over to Red Rocks, which was really kind of boring. Even if you speed it up, it's kind of just like "Eh, there's a highway..." And I can't remember. It's been a few months... I know we made a Denver version of Changelog News with the B-roll from Denver, but I combined a bunch of stuff, and I probably slipped a little bit in... But I also have not the best -- I'm getting better at driving the drone. In fact, I have a show coming up next week. By the time this publishes, it'll be this week's Changelog News, where I'm following around the tractors as they harvest. I did the soybean harvest, and now I got the corn harvest... And I'm getting good. I'm flying at like 10 feet above the tractor, and keeping it centre frame, and stuff... So I wasn't very good at flying it then, because it was pretty new. But... A little bit probably snuck in, but not enough to be exciting.

**Gerhard Lazy:** I mean, it was great to know that, to basically see how news is being put together, where you just literally take this drone out, fly it around, and then you decide whether it was something worth using or not...

**Jerold Santo:** Yeah, basically.

**Gerhard Lazy:** ...seeing that production. So I think we had two in one in that point. And that was really cool. On this hike, I would have missed this rattlesnake... Was it not for Matt Johnson, that almost walked into it.

**Jerold Santo:** You don't want to walk into a rattlesnake, by the way.

**Gerhard Lazy:** No, you don't. \[laughter\] So yeah. But it was my first time seeing a rattlesnake up close, and... It made it a happy memory, because Matt was quick to react... But things could have turned out very, very differently. Now, you have to imagine this is summer, we were in shorts, we were engrossed in our nerdy talk, and nearly walked into this rattlesnake. So it was very close calls. It's the exact same thing as shipping an under-provisioned system into production. \[laughter\] Almost the same. Almost the same.

**Jerold Santo:** Same shorts even, probably.

**Gerhard Lazy:** Yeah, yeah, yeah. Yeah, exactly. Exactly. Same shorts.

**Jerold Santo:** Short once again.

**Gerhard Lazy:** Yeah, that was a close one. So this is the analogy to what we avoided, both in real life, but also on stage.

**Jerold Santo:** Now, the nice thing about a rattlesnake is, you know, God gave him those rattles, and those rattles are very useful... Because a rattlesnake doesn't want to be messed with. So when you get close to a rattlesnake and don't know it, they'll let you know that you're close. And that rattle, that shake is saying "Get away from me." However, I don't think we got any notifications, to draw the analogy... Our Fly machines didn't say anything, did they? "There's no rattle on that side of the equation." Was there?

**Gerhard Lazy:** Well, I did receive some emails that instances were running out of memory and crashing, but it was happening after a while, so that was maybe the equivalent of that.

**Jerold Santo:** \[24:03\] Right.

**Gerhard Lazy:** But in this case, because we were so engrossed in the conversations, we never heard the rattles.

**Jerold Santo:** There you go. Okay, fair. We weren't checking our emails.

**Gerhard Lazy:** There were drones buzzing around... \[laughter\] It was a bit crazy. So yeah, we did not pay attention to that. Alright. So if you're watching this next piece, and if you don't like meat, look away.

**Adam Staravia:** Oh, boy...

**Jerold Santo:** Oh, I know what this is going to be.

**Gerhard Lazy:** Just listen. I'm going to play it for you. Adam, would you like to describe what is happening?

**Adam Staravia:** Well, we asked very politely, "Can you show us the kitchen and how things are done?" And they said yes. And then they took about 20 minutes to prepare a tour, and they allow us to come in there and hold exactly how the chefs prepare and prep the meat to come out to the very awesome Fog ode Chão patrons... Which is kind of cool. And so there's Jerold, holding it like a beast, about to eat it, but not, because that's somebody else's.

**Jerold Santo:** Yeah. That's not my food.

**Adam Staravia:** That's not your food. But you just had some versions of that.

**Gerhard Lazy:** It's not the snake.

**Adam Staravia:** It's not the snake.

**Jerold Santo:** That would have been apropos, wouldn't it?

**Adam Staravia:** Yeah. This is not the snake.

**Gerhard Lazy:** Yeah. Oh man, that was perfect. Really, perfect. So yeah --

**Adam Staravia:** The funny thing about that one too though is that you never get what you don't ask for. That's my -- if it's one advice I give anybody in the whole entire world, it's like "You don't get what you don't ask for. So ask, and you might get it."

**Jerold Santo:** And what Adam's referring to is the tour of the kitchen at Fog ode Chão.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** Because I wasn't going to ask. I was ready to pair a check and go home. And Adam's like -- we had very kind wait staff, and they were discussing with us, talking about "Did you know the actual chefs are the ones that deliver the food?" I was like -- I had no idea about that. So they're giving us an insider look, and Adam just said "Can we see the kitchen?"

**Adam Staravia:** "Could you give us a tour?"

**Jerold Santo:** And then he's like "Yes, I can."

**Adam Staravia:** "I can arrange that."

**Jerold Santo:** And we were all kind of awestruck, because normally we're used to hearing no. But yeah. If you don't ask, you don't receive. So thank you, Adam, for giving us this sweet shot of the Changelog T-shirt on me while I eat that rattlesnake. Or no, that's a pork chop, I think. I don't know what that is.

**Gerhard Lazy:** That's a joke.

**Adam Staravia:** It looks like maybe... I'm going to guess. Who can guess this? I'm thinking rib eye. Is that rib eye?

**Jerold Santo:** It might be.

**Adam Staravia:** Sirloin.

**Jerold Santo:** It looks like maybe sirloin. That's what I would have picked if they gave me the choice, would be the sirloin, because that was to die for.

**Adam Staravia:** Potentially piranha. Is that piranha?

**Jerold Santo:** I don't know. You're the connoisseur.

**Adam Staravia:** It looks like piranha. I can see the fat cap there on the left-hand side...

**Gerhard Lazy:** I remember that. It was so good.

**Adam Staravia:** That's piranha.

**Gerhard Lazy:** And with fruit... I mean, that's how I like my meat, with fruit. It was just amazing. It was like one of the amazing meals I had in the US, ever. Like seriously, it's just like above, above them all, which is so, so good. The thing which I wanted to convey is that even though we had a short trip - it was only two days - it was a very rich trip. Many things happened. It wasn't just about tech, it was literally friends coming together and spending a bit of time, and it just felt so good. So natural. It flew by. I mean, we were joking about how fast time flies by, but those two days were -- I remember when the border agent was asking me how long are we staying for, and I said two days. And he was like "Really? Two days? Where are you coming from?" I said the UK. "Really? Can I see --" He just would not believe me that I'm flying in for two days? It was so worth it.

**Jerold Santo:** I'm happy to hear that, because that's a long trip for you.

**Gerhard Lazy:** It was perfect. It was really, perfect. So this was the end of my Denver trip, and... It is the favourite thing that we did together, ever. So it was perfect... And this is obviously leading to something... What are your thoughts on doing this again next year, 2026?

**Adam Staravia:** A hundred percent.

**Gerhard Lazy:** \[28:04\] And I'll give you a couple of moments to think about that... \[laughter\]

**Adam Staravia:** I was like "A hundred percent."

**Gerhard Lazy:** Jerold, Jerold.

**Adam Staravia:** Sorry. Jerold, you answer.

**Jerold Santo:** Oh, I'm for it. I'm already -- I'm for it. I mean, Adam was like "Let's do it four times a year", or something.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** We were talking about how many times, not --

**Adam Staravia:** I'd say two to three. Two to three. Four is too much... Two's for sure. Three might be pushing it, but I'd love to do more live shows like this. And twice a year is enough, in my opinion. Three, four, maybe... Two for sure.

**Gerhard Lazy:** Honestly, I'd be very happy if we do this again, at least like a repeat. That'd be very nice. It doesn't have to be the same place... But at least once a year would be a good habit I think to start having... Because so many things happen around, and it's not just the show, it's everything else. And I don't know how many people want to join us now...

**Adam Staravia:** At least 50...

**Gerhard Lazy:** Here's an opportunity to comment... Here's an opportunity to comment.

**Adam Staravia:** You do have to be close to Denver, or willing to travel. And we had many people travel, which was kind of cool.

**Gerhard Lazy:** Now, you know that I like to do things well in advance... For example, most of my next year's holiday's already booked. The only one which I couldn't book is actually ended of October, because flights only become available like a year before... So I need to wait a few more weeks.

**Jerold Santo:** You're such a planner. Holy cow.

**Gerhard Lazy:** I am. That's why I'm asking...

**Jerold Santo:** That's why he's asking, Adam. He wants to get something on the calendar.

**Gerhard Lazy:** Right. So I think it would be a good time like in the next maybe three months...

**Jerold Santo:** Well, what's your opinion on Denver, Gerhard? Is that our place now? Or is it more like "That was fun. Let's go somewhere else and let a different subset of our audience and friends have an easier time getting there"? And we know Denver is not accessible for everybody... Austin obviously would be another good choice, because it's close to Adam, and it's close to lots of people that we know. I'm not sure if you've got directs to Austin, Gerhard, but...

**Gerhard Lazy:** I do.

**Jerold Santo:** You do. So thoughts on a new location, versus right back to the mountains?

**Gerhard Lazy:** I'm all up for it. I've been to Austin, it's a really nice place. I had a good time there. The Colorado River, which is a different Colorado River, was very nice to kayak on... That was like a good experience, for example. And yeah, I mean, there are so many things that we could do.

The more interesting question would be who would like to join? ...to see where do we have the most loyal fans, so that we're there for them as well, and they can join us, and we can do something together. And do you want to do any interviews? What does that look like? Will there be a conference before or after? So how do we structure it, so that it makes sense on all accounts? What about holidays? ...because all of us have holidays, and other conferences... So what would make sense?

**Jerold Santo:** Well, I think thank you for getting the conversation started. We're definitely in to do it again, and I think it's time now, in October, to start discussing the details of what that might look like. I don't think we have to wait until next summer, but I haven't seen your calendar, Gerhard... As you know, I'm going to be crossing the pond in May, with my family, taking my daughter and wife over to France and Italy, to celebrate her graduation... So that's going to be a big trip for my family, but... I don't know what yours looks like, I don't know what Adam's looks like... So let's get talking and get some stuff figured out. To our listeners - comment, let us know where should we go, when should we do it, and what should it look like? What would you like to be a part of? Should it be just like this last one, an interview episode, a Kaiden episode, and then festivities around that? Should it be more? Should it be less? Please let us know in the comments.

**Gerhard Lazy:** I think if you ask Adam, he'll say "Changelog Con." The first Changelog conference ever. Go, go, go.

**Adam Staravia:** \[32:00\] Maybe... I kind of liked it just as it was though, honestly. I wouldn't mind having some trusted -- not like demos, but some show and tell. Furthermore, I think there's a lot of pontification from the stage... Furthermore, I'd love to have some show and tell type stuff, if that was a thing. And maybe that's demoing. I'm thinking Oxide with their racks, and stuff like that. That's kind of show and tell. But I don't know.

**Gerhard Lazy:** That would be really cool.

**Adam Staravia:** I really just enjoyed exactly as it was, honestly. I think a lot of it was perfect... I think it was just short enough and just sweet enough that it was doable, repeatable... And it was just an interview, and just Kaiden on stage, and just hanging out with friends... And it was more community than it was brands, or what's new in tech kind of thing. I think it was just the right kind of feels, honestly. So I'm not sure. I haven't thought a lot about the design of it enough to want to change it much.

**Gerhard Lazy:** Yeah. Okay. Well, we got the conversation started, we got some thoughts... We can put it on the back burner and come back to it maybe between now and the next Kaiden, see if we've reached any conclusions or any suggestions which are firming up... But this was good.

**Jerold Santo:** I think we should set a goal and say "By the next Kaiden, we will have a date and a city." And that way we can at least say the date, start booking flights, or whatever we have to do. And then the details of what we're going to do while we're there, we can figure those out from there... But at least in the next quarter we should know for sure, by the end of the year, what we're doing, where, and when.

**Gerhard Lazy:** I like that. I like that very much, actually.

**Adam Staravia:** While we're on that subject, I did have my friend here that could tell me a couple of details about Austin, at least...

**Jerold Santo:** Your friend?

**Adam Staravia:** Claude.

**Jerold Santo:** Oh, Claude. Hey, Claude. How are you doing?

**Adam Staravia:** The latest model. They're actually suggesting Sonnet 4.5 right now, over Opus 4.1. They're calling it legacy. Furthermore, they're calling Opus 4.1 Legacy. That's kind of funny, it was like brand new a month ago, and now it's Legacy all of a sudden. Anyway, it's hot here in Austin, so the best month, they say, to come here is March through May, or October through November. And we're obviously in October now, so we can't do it next month... So I think if it was Austin, I would agree with this, that it's before summer, not during summer. So March through May, somewhere in there, if it's Austin.

**Gerhard Lazy:** Yeah, I think that's a good time.

**Break**: \[34:33\]

**Gerhard Lazy:** We're looking at all the different steps that we had to take between being on stage at Denver... Do you know which \[unintelligible 00:36:04.24\] were there? Just looking at this list... It's a list on the Ripely repo -- by the way, we're looking at the README... All the various release candidates of 1.0, before going to 1.0. I thought it would happen on stage, it didn't. Or soon after. It didn't. But it did happen now. So we are beyond, and we are running on 1.0. If you look at 1.0 RC4, limit Varnish memory to 66%. And that's the one commit which I pushed that was on stage. There was the next one, RC5, handle varnish JSON response, failing on startup, and bump the instance size to performance. That was the scale-up that needed to happen.

So really, we didn't need much in terms of resources. One CPU, a performant CPU, and eight gigabytes of RAM. That was enough. And then we could send 50% of the traffic. And we were on that 50% for quite some time. So RC7, RC6, more locations, backend timeout...

Now, the one thing which was failing, and this was discovered after, I think, we were routing more and more traffic, is that uploads were failing. Mp3 uploads were failing. And that was pull request 39. Do they work now, Adam?

**Adam Staravia:** I think so, yeah. I mean, I've been uploading...

**Jerold Santo:** The answer is yes.

**Gerhard Lazy:** Nice, great.

**Adam Staravia:** I can't say no. I can't say -- I guess I can say yes. Yes, it does.

**Jerold Santo:** They work, yes.

**Gerhard Lazy:** Great. So that was like the one thing which --

**Jerold Santo:** I had Vastly hard-coded for a while, because it wasn't working, and we needed to keep uploading mp3s. And then when you asked us to test it, I removed that from my Etsy hosts...

**Gerhard Lazy:** That's right.

**Jerold Santo:** ...and I have had no issues. I didn't report back, because I was saving it for Kaiden to tell you "Yes, you fixed it. Thank you."

**Gerhard Lazy:** Nice, great. That's what I wanted to hear.

**Jerold Santo:** You probably were hoping that I'd report back, but I didn't say anything at all. I did test it, though.

**Gerhard Lazy:** Well, as long as you don't have the hard-coded IPs, \[unintelligible 00:38:04.14\]

**Jerold Santo:** Yeah, I took those out.

**Gerhard Lazy:** Nah, it's a good time to remove them from everywhere. Because everyone else is going to Pipe dream, so everyone's using the new CDN, and uploads are also working, so there should be no more issues. And 100% of the traffic is being served with 1.0. So 1.0 was tagged on yesterday. This was only yesterday.

**Jerold Santo:** Okay.

**Gerhard Lazy:** However. However. The traffic has been served through the new instance on -- I think it was on the 5th. Yes, on the 5th of October, everything switched across. All the traffic. We're looking now at the screenshot from Honeycomb, which is showing the requests going to Vastly, and we can see that after October 5th, they dropped. And there's a few - there will always be a few - hard-coded IPs, whatever the case may be. It's not human traffic, that's for sure. That sounds wrong. It's not people hitting the website. It's mostly bots.

**Jerold Santo:** Human traffic in...?

**Gerhard Lazy:** Yeah, exactly. \[laughs\] It's bots. So we have been running 100% on the new system for more than 10 days now... And I wanted to be -- like, why did it take so long? Because that was July. I wanted to be certain that everything worked fine. Like, after the last time, I went extra, extra, extra cautious. I needed all the metrics, there were the summer holidays, I joined the new startup, I was a bit busy... And I had to build the most insane home lab ever, which took me a while, but that's going to come a bit later. So this is what it looked like. Now, do we remember, now that everything is said and done, why did we need to build our own CDN? What's the reason behind it?

**Adam Staravia:** Frustration.

**Gerhard Lazy:** Frustration... Okay, that's a good one.

**Jerold Santo:** Plus the hacker spirit. Plus our cache hit ratio was out of our own hands... We wanted it in our own hands.

**Gerhard Lazy:** \[40:03\] Yeah, yeah. It was like the previous screenshot. So this is the moment I turned off all traffic from like forever, in this case, from Vastly. It was only a few days, but you can see that in those few days we had 155,000 cache hits. Sorry, cache misses. 155,000 cache misses. And we had 370,000 cache hits. So the ratio does not look right. That green line, the cache hits, there were days when there were more; or like periods, not days. There were periods, up to maybe half an hour, an hour, when there were more misses than hits. And you do not expect a CDN to behave that way. And by the way, this is across both changelog.com and cdnchangelog.com. So it includes both the static assets, everything. Just a small window, but it just shows the problem.

Now, as a percentage, that translates to 70.5%. So 70.5% cache hits, and that is really not great. Okay, I know you've been expecting this... So let's see. What do you think is our current cache hit versus miss ratio? This is across all requests. So now that we switched across, we had 10 days to measure this... On the new system, what do you think is the cache hit versus miss ratio?

**Jerold Santo:** Now, you're giving us four choices. This is a multiple choice question.

**Gerhard Lazy:** Only one. Only one's correct.

**Jerold Santo:** 85% is A, B is 89%, C is 95%, and D is 99%. Adam, what are you thinking?

**Adam Staravia:** I'm locking in C.

**Gerhard Lazy:** 95%. Okay.

**Jerold Santo:** I'm going for the gusto. I'm going 99%.

**Adam Staravia:** Whoa...! \[laughter\] Straight to D.

**Jerold Santo:** I love to be wrong, but if I'm right, I'm going to be... Ah, I'm so wrong...!

**Gerhard Lazy:** 89.5%.

**Adam Staravia:** So close. Both of us were wrong.

**Gerhard Lazy:** That's the answer. Yeah.

**Jerold Santo:** How good would that have been though...? Well, you know, some stuff is fresh. It just is.

**Gerhard Lazy:** Yeah, we can improve on this. I mean, it's not -- now, the important thing is it went from 70% to 90%.

**Jerold Santo:** That's right.

**Gerhard Lazy:** That was a big jump. Now, 100% --

**Jerold Santo:** And it's in our hands now. We can actually affect it.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** Before, we could only complain. Now we can actually do stuff.

**Gerhard Lazy:** And even that - after a few years of complaining, you just become tired of complaining...

**Jerold Santo:** Yeah. Yeah, we grew weary.

**Gerhard Lazy:** And we just built our own. Okay, so can we do better?

**Adam Staravia:** We just built our own...

**Gerhard Lazy:** Can we do better than 89.5%? So I think everyone is thinking this... But really, what I think we should be thinking is, "Do we need to do better? Do we need to do better than 89%?"

**Adam Staravia:** Good question.

**Gerhard Lazy:** Feeds... If you look at all the feeds, we are at 99.5% cache hit ratio. Before, they were at 96.8%. So what are feeds, for our listeners and watchers that don't know? Who wants to answer that?

**Jerold Santo:** What are they?

**Gerhard Lazy:** Yes, what are they?

**Jerold Santo:** These are XML files that represent the current state of our podcast syndication, our episodes that we're shipping and have shipped. And so they're hit often by robots who are scraping feeds in order to update their podcast indexes, and let people know which episodes are available. And they should be at 99.5%, because they only change when we publish a new episode, which is at this point in our lives three times a week. On a Monday, on a Wednesday, and on a Friday. And every other request, every other day and time is the same exact content.

**Gerhard Lazy:** \[43:53\] That's it. So I would say that this is possibly the most important thing to serve. Because if we don't serve feeds correctly, how do you know what content Changelog has? How do you know when content updates? And this is like worldwide. So I think this is pretty good. And improving on 99.5%, I don't think we should do it.

**Jerold Santo:** No.

**Gerhard Lazy:** The homepage, before, the hit ratio was 18.8%.

**Adam Staravia:** Oh, my gosh...

**Jerold Santo:** I don't understand that...

**Gerhard Lazy:** I know. \[laughs\] This was my biggest issue, for as long as I can remember. Today, it's 98.5%.

**Jerold Santo:** And to our listener who's probably out there thinking, "You guys were certainly doing it wrong", we spent years trying to do it differently. Like, go back and listen to all the chains, of us trying to change the way that we actually configure and respond, and our headers, and our... I mean, we tried, and we ended up with 18.8% cache hits on our homepage.

**Gerhard Lazy:** That's it. That's the best we could do.

**Jerold Santo:** And so here we are.

**Gerhard Lazy:** That was so bad. So bad. Now, mp3s, I would say the second most important thing - it was 86%. Now it's 87.5%. Maybe this can be better. Maybe this can be improved. We just need basically more memory, or to store them on disk, do a bunch of things... Because by the way, caching is in memory... And I still need to understand why memory, once it gets filled, it doesn't remain filled. So I've seen this weird behaviour where after a few hours, memory starts dropping. But why? Because there's no pressure on memory. Why are objects getting evicted?

**Adam Staravia:** Interesting.

**Gerhard Lazy:** My assumption is that we're storing some large objects, and if there are smaller objects that need to be stored in memory, the larger objects get evicted, which means that the cache drops. But I would need to understand that a little bit better. Still, mp3s aren't worse than they were before.

News... I know this is something that's very important to Jerold. It was 52.6% cached before. Now it's 83%. So... Improvements across the board. Now, we could improve it, especially news and mp3s, I would like to look into that. But I think news is like top of my list. But is there anything else that you think that we should pay attention to, or in terms of the cache hit ratio? Any other resources?

**Jerold Santo:** No. I mean, mp3s are static assets. You could go look at other static assets; images, etc. But I just don't think we want to squeeze this radish too hard. I agree that news, and probably taking a low-hanging fruit pass on the mp3 endpoints, and seeing what we could do there, would probably bear some good fruit. But even those, I wouldn't spend hours and hours trying to make them much better.

**Gerhard Lazy:** What I'm thinking - I would just basically double up the memory and see how that changes things... Which is just a config setting. It'll take me maybe a minute. That'll be my first action item.

**Jerold Santo:** Okay.

**Adam Staravia:** Yeah, I imagine news could be very similar to feeds, because once news is published, it's similar to the feed. It's changing once a week, and once it's published, it likely never changes again. It never has changed, right?

**Jerold Santo:** Not that we've moved, all of our comments and everything exist elsewhere. I mean, they're in Zulip, they're on YouTube... So there's no comment feed there, there's no reason for anything to really be new, except on publish.

**Gerhard Lazy:** Yeah, okay.

**Adam Staravia:** So I'd say news could be similar to feed, pushing that to the boundary, because it doesn't change much. I'd love to explore that when you do the mp3 exploration of large objects getting pushed out... I'd love to just sit on your shoulder, I suppose, or as a fly on the wall kind of thing, just to explore that with you... Because I'm super-curious about what makes that cache get purged out of the memory, myself.

**Gerhard Lazy:** \[47:54\] Yeah. Well, pairing up is something that I'm getting better and better every day. Recorded and published pairing sessions. Jerold has the experience, not Adam...

**Jerold Santo:** That's right.

**Gerhard Lazy:** Yeah, that sounds great. Now, it gets better.

**Adam Staravia:** Oh, my God...

**Gerhard Lazy:** Okay? It gets better.

**Jerold Santo:** What does?

**Adam Staravia:** All of it...

**Gerhard Lazy:** Do you recognize the \[unintelligible 00:48:14.19\]

**Jerold Santo:** Okay, so that looks like --

**Adam Staravia:** This is Johnny Mnemonic, right?

**Jerold Santo:** No...

**Gerhard Lazy:** Say again?

**Adam Staravia:** Johnny Mnemonic, is this...?

**Jerold Santo:** No... That's -- is that Hugh Jackman?

**Gerhard Lazy:** Yes...

**Jerold Santo:** This is not Wolverine.

**Adam Staravia:** This is Swordfish.

**Gerhard Lazy:** Yes...! \[laughs\]

**Jerold Santo:** Oh, no...

**Gerhard Lazy:** \[unintelligible 00:48:36.12\]

**Jerold Santo:** I'm very nervous right now, Gerhard...

**Gerhard Lazy:** That's okay, it's fine. It's recorded.

**Jerold Santo:** Swordfish broke the show previously... Okay.

**Gerhard Lazy:** I'm ready for it this time. \[laughs\]

**Jerold Santo:** That doesn't mean that I'm ready for it... You're going to play this live for me right now on camera? Okay...

**Gerhard Lazy:** I will, yes. So this clip is going to blow you away, okay?

**Adam Staravia:** I'm going to watch it.

**Jerold Santo:** I'm hoping this is Sora. Okay, Halle Berry, John Travolta... Hugh Jackman has a gun to his head... He's typing. He has to hack something in a certain amount of time. Was it 30 seconds?

**Gerhard Lazy:** 45 seconds.

**Jerold Santo:** 45.

**Adam Staravia:** Look at his fingers.

**Gerhard Lazy:** He types very, very furiously.

**Jerold Santo:** He's typing furiously.

**Adam Staravia:** Oh, access denied.

**Gerhard Lazy:** He gets very disappointed when that happens. \[laughter\] He gets very disappointed...

**Jerold Santo:** Yes...

**Gerhard Lazy:** ...when access gets denied. Alright, so that was a moment of fun.

**Jerold Santo:** I wonder what that was for... \[laughs\]

**Gerhard Lazy:** Things get better, okay?

**Jerold Santo:** Okay. So that's the moment of disappointment...

**Gerhard Lazy:** Exactly. Even if you're under pressure, and you have to deliver, things will be better. So Pipe dream gets better. Now, we looked at the cache hit ratio... What I would like to look at next is the response time in seconds.

**Jerold Santo:** Okay.

**Gerhard Lazy:** These are all the feed requests before and after. So the P50 for all the feed requests used to be two milliseconds. And you would think "Wow, that's pretty good." Well, in the new system it's like half a millisecond. So it's a four time improvement. The P75 is 13 times better. So for 75% of the users, the feed responses get served 13 times as quickly as they were before. The P90, 95, 99 - it gets progressively better, which means that the requests are served much quicker, at least four times as quick as they were before. And you might be thinking "Hey, that's bots. What about humans?" So what about the homepage? For 50% of the users, the homepage is 860 times quicker. That's nearly three orders of magnitude quicker. That's a crazy amount quicker. Now, obviously it is the fact that it was not cached. Like, only 18% of the requests were cached.

**Jerold Santo:** Right.

**Gerhard Lazy:** But the page is instant. Like, now it's instant. It's 0.000 -- three zeros, three seconds. That's like a third of a millisecond.

**Jerold Santo:** That's nice.

**Gerhard Lazy:** So...

**Jerold Santo:** You're welcome, humans...

**Gerhard Lazy:** You're welcome, humans. Now, what does that look like? I think 863 times is really difficult to imagine, so I'm going to play something for you to see what it means. So what we have here is one second at the top; that's how long it takes. No, hang on. I'm not playing it. I should be playing it. There you go. Now I'm playing it. Okay. While 833 seconds at the bottom is still loading. And it will continue loading for so long that we're not going to wait 15 minutes for this thing to load, okay? We're not going to wait that. So that's the difference between how fast the homepage loads now, versus how it used to load before. This is for the majority of the users.

\[52:21\] So the cache hit ratio, the connection there was that everything was slow, and there's nothing we could do about it. And I think slow is relative, because when you're talking about milliseconds, I think there's about 50 or maybe 100 milliseconds when things were nearly instant... But in our case, the homepage was taking 150 milliseconds to get served. And the tail latency is really crazy. Like, the tail latency was over a second for the homepage to serve. That was a long time. By the way, this thing is still going, and it's not even like 10% there.

**Adam Staravia:** What's the rationale behind this video? Explain to me how this is supposed to explain things...

**Gerhard Lazy:** So the top one shows you how quickly it takes for one second to finish, right? So the response, the one-second response, it just visualizes it, how quickly that gets served. The bottom one shows you how long the previous CDN, how long in comparison 863 seconds is. So now things are loading in a second, or the equivalent of a second, and before, things were taking 863 seconds to go. The same request.

**Adam Staravia:** They were?

**Jerold Santo:** Longer. Relative, not absolute.

**Gerhard Lazy:** Relative.

**Adam Staravia:** Okay.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** So the one second, it represents our current loading speed, which is like a millisecond. But we can't visualize that, because it's too fast.

**Gerhard Lazy:** Exactly.

**Jerold Santo:** And 863 seconds, that's how much slower it used to be. So it's a relative example.

**Adam Staravia:** Right. Relative to one second, versus relative to milliseconds. I understand, okay.

**Jerold Santo:** That way we can actually visualize it. And now it's at two point -- oh, he reset it. Okay. I was going to say, it's going backwards...

**Gerhard Lazy:** It's loading again, because it finished.

**Jerold Santo:** So it's like 15 minutes versus one second. And then reduce that down to milliseconds, and we're basically that much faster.

**Gerhard Lazy:** Exactly. Yeah. Waiting 15 minutes, versus waiting a second. That's exactly the speed difference between what we used to have, and what we have now.

**Jerold Santo:** Right.

**Gerhard Lazy:** It's just really fast. \[laughs\] Really, really fast.

**Adam Staravia:** That was a CDN thing. That was not -- that was traversing DNS, into CDN, getting a cache hit or miss, serving, rehydrating, getting new from cache... That's where all the time was spent.

**Gerhard Lazy:** So in this case, these were the responses from the Varnish perspective. So if I go back here, and we're looking at this table... So this is the homepage, the response time. How long does it take to serve the homepage from Varnish's perspective? Whether it's in the cache, whether it needs to go to the application, and request it, and then eventually finish serving the actual response... So before, P50 - 259 milliseconds. That's how long it used to take.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** And now, it takes a third of a millisecond.

**Adam Staravia:** What changed specifically with Varnish then?

**Gerhard Lazy:** Well, caching. Most of the -- if we go back to the table, if we go back here, now 98.5% of the requests are served from cache. We don't need to go back -- I mean, the homepage is almost always in cache. We very rarely have to go back to the application to fulfill a request. Before, only 18% or 19% of the requests could be served from cache.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** So Varnish had to go to the application, the application had to serve the response, so that Varnish could serve the response back to the user, to the end user.

**Jerold Santo:** You keep saying Varnish. Don't you mean Vinyl?

**Gerhard Lazy:** Yes, I do. \[laughter\] I do. Well, not yet --

**Jerold Santo:** Not to change the subject on you, but --

**Gerhard Lazy:** \[56:10\] Yeah, Vinyl is coming up in January.

**Jerold Santo:** There's a curveball.

**Gerhard Lazy:** So it's not here yet.

**Jerold Santo:** For those not in the know, they're renaming the Varnish software, because of legal disputes, to Vinyl Cache. So Varnish Cache, the open source project, will be renamed to Vinyl Cache.

**Gerhard Lazy:** That's correct.

**Jerold Santo:** Whereas Varnish Software, the company, will continue as Varnish Software, the company.

**Gerhard Lazy:** I'm going to jump ahead... I mean, this is -- yeah, Jerold is coming from the future now.

**Jerold Santo:** I am.

**Gerhard Lazy:** So PHK, Paul-Henning Camp, he posted on September 15th - this is on varnishcache.org. It was just about a month ago. He wrote "20 years old, and it is time to get serious, sir." That is the title of the blog post. And he talks about the open source Varnish Cache rename. Some legal disputes, indeed... We can go and read it out, but basically, Varnish 8.0, the open source Varnish - 8.0 will be the last one that will be called Varnish Cache. So from March next year - and I think this is very interesting - it will be Vinyl. The name of Varnish, the open source Varnish, will get renamed to Vinyl.

**Jerold Santo:** Okay, now I know who we have to have as a guest on our interview in Austin. PHK, launching the Vinyl Cache, live on stage... I think he lives over on your side of the ocean.

**Gerhard Lazy:** Or Berlin, yeah, because he is --

**Jerold Santo:** Yeah, he probably wouldn't come to Austin. But we can try.

**Gerhard Lazy:** So that's -- yeah. Alright, so speaking of speed, this one's for Adam.

**Adam Staravia:** I love speed.

**Gerhard Lazy:** You know that I joined Loophole Labs, that's it, so... What we do, it requires a really fast, low-latency network. And by that, I mean at least 100 gigabits. I need to have subbed one millisecond latency. So about two months ago, I started building a new 100-gigabit home lab. And I know that Adam has been asking me for a really long time to do a video on my home lab. Jerold already watched it a few weeks ago... This is live, and the easiest way is to go to yt.makeitwork.tv. That will take you to YouTube, and there you can go and watch it. And I take you through the entire journey, why I had to build it, a couple of interesting things... Yeah, it's -- what did you think about it, Jerold? The portions that you managed to watch.

**Jerold Santo:** Yeah, like I said earlier, I thought it was perfect. It's cool --

**Gerhard Lazy:** What did it miss? How would I improve it? Maybe that's a better question. What would have made the video better?

**Jerold Santo:** What would have made the video better? I don't know in terms of like content that was missing... I feel like the way that you do your summarized intro is compelling, but sometimes it is like jump cuts so fast, or... It's sometimes hard for me to track exactly. So that's like a hard thing to give feedback on, I'd have to give you specifics for you to actually know what -- but even though I'm like compelled to continue watching, and I do enjoy it, there are times when I'm confused. And so I think as you continue to refine that - because I know it's a style that you're doing, and you've gotten better at it, since... Because I've seen some of your videos from a year ago, is. And it is definitely getting there, where I'm like, I look forward to it... But I also am sometimes not sure what's going on. I'm not sure if that's on purpose - maybe it is - to keep me intrigued, as there are all kinds of techniques to keep people watching on social media... But I think you can continue to refine the narrative that kicks off from the beginning, in making it more cohesive, or just laying more breadcrumbs perhaps for the person who's not initiated. Because you're so deep into what happened, and you know the whole story from front to back, and you're telling it, and that's great. But I think that's one thing that could be improved.

**Gerhard Lazy:** Very nice.

**Jerold Santo:** And \[unintelligible 01:00:03.11\] I don't know about stuff that's missing, because I wasn't there for what got dropped...

**Gerhard Lazy:** \[01:00:10.02\] That's great. That's great. So yeah, okay. That's excellent feedback. Alright. Well, Adam, when you get a chance to watch it, if you get a chance to watch it, I would love to get some feedback from you too in terms of what would make it better for you.

**Adam Staravia:** For sure.

**Gerhard Lazy:** As you watch it, anything that could be improved... Because the next one is coming up. So how fast is the Pipe dream? That's what we're going to answer now. How fast is the Pipe dream on this 100 gigabit home lab? Because you remember we talked before, we were looking at how much -- like, when we benchmark these things, Fly.io itself is limiting us to how much bandwidth we can push. We wouldn't want to be pushing tens of gigabytes or hundreds of gigabytes. That would be crazy. Because that costs someone money... So running benchmarks like that is not great. But also the WAN, there's a limit there. But in this case, the limit is 100 gigabits. We know that. So this is a new home lab, this is what it looks like, it's running Ubuntu 24.04... I think the most interesting thing is the CPUs about it. So it has a Thread ripper 9970X. And the reason for the Thread ripper is that I need a lot of PCIe lanes, so I couldn't use like a regular consumer-grade CPU. I needed 16 lanes for the GPU, the RTX 4080, which is there at the bottom, and I needed another 16 lanes for the network card. Even though it's a PCIe 3.0, if you give it, for example, eight lanes of, in this case, PCIe 5, it can only use eight lanes of PCIe 3. So you would basically half its speed. And eight lanes of PCIe 3.0 means 64 gigabits. So really, I need a full 16 lanes, doesn't matter -- I mean, it needs to be at least PCIe 3 to achieve its full speed. And the card is the thing that you see -- there's some green LED lights... It's right below the fan for the CPU.

Alright, so that's one. This is the server. We're going to be running Pipe dream on this host. And this is the other part of the Home lab... This is my older machine. It's about three years now. It's a Ry zen 7 5800X. Furthermore, it has 16 threads; not 16 cores, 16 threads. A small GPU, a GeForce GT 730. It's a fanless one. This is the one at the bottom. And again, the reason why I had to do this is that I needed the 16 lanes, which are right under, again, that CPU cooler for the network card.

If I was, for example, to put an NVMe in a specific slot, or if I was going to fill any other PCIe slots, the first slot, because it shares bandwidth, the first PCIe slot would be limited to 8x, which again, would create that 64 gigabits limit. So I needed to give this full 16 lanes, and that's where this limitation came from.

Now, this is the star of the show, this is what those cards look like. You can see there's a DAC cable... Obviously, you need two; now they have two modules, which is interesting, because the card itself, in terms of the PCIe bandwidth, will max out at 128 gigabits. So it can't go beyond that from a PCIe slot perspective. Even though each module could do 100 gigabits, really in combination you can only push 128 theoretical maximum. And these are older cards... It's an NVIDIA Eleanor Connect X5, so they've been around for many years now. I think 2020 at this point, so they're like about five-year-old cards.

**Jerold Santo:** What's the price range on these? Are they expensive?

**Gerhard Lazy:** They can be, yes. These specific ones, I got them off eBay and I paid for both of them 500 pounds, which I think it's about $800, I think. 700–800 dollars, roughly. Now, in the U.S. I think you can get them for even cheaper, because you get more hardware, data centre hardware that just gets sold for a good price. So refurbished stuff, or in this case it's just used, it's not refurbished.

\[01:04:22.05\] And a DAC cable... The cable can be a bit expensive. You can pay anywhere between -- close to $100. I think this one was about 60 pounds. And then you need two. And the reason why you need two is here because I'm configuring the two modules in a bond, in a network bond. It's an LACP bond, and in this case what it means is that I'm basically having two cables, and I'm creating a single virtual connection that uses both modules. So again, the theoretical maximum is 128 gigabits, but in reality, it's more like 112. I was not able to push it beyond that.

So HTTP stat... What I'm showing here is that if I do an HTTP stat from the client, H22, by the way... H22 is the client. That's the year, Home lab 2022. And W25, the workstation 25, but it's also a home lab, but it's also a workstation. It's a combined thing because of the many cores that it has, and it has a multirole, that host.

Alright, so from the client from H22 I'm basically going to that private IP, 10.25.10.1.4.1, and on port 9000, the Pipe dream is running. And you can see here the response is going to the app. There's just basically a Pipe dream running in a container locally, as it would run on Fly. Alright, so let's see what this baby can do. I'm reusing OHA, I'm running 64 clients, and I'm sending a million requests to the homepage. Let's see what it will do. That was it. That was 1 million requests sent to the homepage.

**Adam Staravia:** Oh, my gosh.

**Gerhard Lazy:** So it took less than five seconds to complete. We pushed 225,000 requests per second. In terms of data, we transferred 12.5 gigabytes in five seconds.

**Jerold Santo:** Wow.

**Gerhard Lazy:** We reached 2.8 gigabytes per second, and that's just over 22 gigabits per second. So if you were to guess, what would you say the bottleneck is, in this case? If you just had to guess. It's not the network. We know it's not the network.

**Jerold Santo:** Yeah, it's not the network. I mean, it has to be --

**Adam Staravia:** Docker maybe? Container?

**Jerold Santo:** The CPU...

**Gerhard Lazy:** The CPU.

**Adam Staravia:** Oh, the CPU?

**Gerhard Lazy:** Yeah, it's actually -- yeah, so the container... I mean, it doesn't have any overhead. It uses binds to the local network, so there's no Dating, no bridging... Nothing happening from a networking perspective. It binds to a port on the local network, so when you go to 9000, it's the port local 9000 on the host.

Now, I'm wondering what happens if we fetch the master feed? Because the master feed is huge. It's 13 megabytes in size, so it's about a hundred times the size of the homepage. So we're going to do something very similar. The difference is we're only going to run a hundred thousand requests, not a million requests. And this is what that looks like. Okay...

**Jerold Santo:** It's taking a little bit longer.

**Gerhard Lazy:** Mm-hm. What do we see? What do we see here? So here we see the CPU and the network for the client H22. And what stands out is that many of the cores are 90, 80... Close to 90% usage. We can see the network throughput, it's 4.59 gigabytes per second, which in this case is 36 gigabits. So we're getting close to 40 gigabits per second. But in this case, we can definitely see that it is the CPU that seems to be the bottleneck. But the CPU on the client - so this is where we're running the benchmark from. So I'm wondering, what does the CPU look like on the host, on the big one?

**Jerold Santo:** \[01:08:30.22\] The Thread ripper.

**Gerhard Lazy:** The Thread ripper.

**Jerold Santo:** It looks pretty quiet from this...

**Adam Staravia:** Pretty chill.

**Gerhard Lazy:** That's it, yeah. I think the peak that -- there's one core which is 11%, but otherwise, everything is like less than even 5%. So most of the cores are chilling. So this confirms that we have the bandwidth... I mean, we went from 20 to about 40 gigabits per second; from 20 gigabits to 40 gigabits per second. And we can see the CPU is fine... So Pipe dream could serve more from the instance perspective, but the client where OHA runs, the one that benchmarks, seems to be approaching the limit. Even so, we are able to send 100,000 requests, and I think it takes, I know, about 40 seconds; something like that, roughly. We can see again, the host, the client, which is running really, really hot, \[unintelligible 01:09:20.18\] constant, so that's nice and constant... And we'll see it now at the end finish 100,000 requests. It transferred about 40-something gigabytes. This in terms of traffic would cost a few dollars, just this benchmark. We transferred 200 gigabytes of data for this one. And the peak, the request per second was 2,200. That's pretty good. That's pretty good.

So I'm wondering what would happen -- there's one more thing which I would like to do. What would happen if we move the client from the host with a slower CPU, to the host with the faster CPUs? So we do like a swap around. We run Pipe dream on the slower host, but we run the client that benchmarks things on the faster host. So what would that look like? Alright, so same 100,000 requests, but now we've reversed where we run these things, and this is what that looks like.

**Jerold Santo:** It's looking faster.

**Gerhard Lazy:** Mm-hm. This is the client... This is where Varnish runs. Sorry, this is where Pipe dream runs. The CPUs are 100%, basically. And this is where a benchmark runs. We see some -- yeah, this is really... So let me just go a little bit back. There we go.

**Jerold Santo:** We're getting up to 80 gigabits per second now.

**Gerhard Lazy:** 80 gigabits per second, yes. So we're able to nearly achieve the performance -- like, saturate the network... And we can see the CPUs -- we still have plenty of CPU room on the new workstation, the Thread ripper, which has 64 threads. So plenty of CPUs there.

**Jerold Santo:** Which is now running in OHA, it's not running Pipe dream.

**Gerhard Lazy:** Correct. Not Pipe dream.

**Jerold Santo:** So we haven't maxed the client out. Now we're actually maxing the server out.

**Gerhard Lazy:** That's it. So in this case, if this host had faster CPUs, it could go faster. But now we're just basically bottlenecked on the CPU.

**Jerold Santo:** Well, you're going to have to upgrade your host, Gerhard.

**Gerhard Lazy:** I think I will.

**Jerold Santo:** We need answers. \[laughter\]

**Adam Staravia:** We need answers.

**Gerhard Lazy:** I think we will. But this just goes to show that the setup scales really, really nicely. And this is what we've been all working towards... Fly.io and Vinyl and Changelog.io. Sorry, Changelog.com. So it's a good combo. In this case, honestly, Fly is sometimes throttling us on the bandwidth. That makes sense. I don't think they were expecting a CDN to run on Fly, honestly... I mean, some of the peaks we can be pushing up to 10 gigabits. Furthermore, I've seen in the metrics so far, \[unintelligible 01:11:58.01\] only the peaks.

\[01:12:02.08\] I don't know what the limit is on Fly, but I think talking to them about this would be a good idea. I've been mentioning this, but I think that following up on this... Because -- I mean, maybe throttling is what we want, but it will affect other users. So are they okay with us running a CDN? What can we expect from this setup? So yeah... So Vinyl, we already know, we've been here, that Vinyl is the rename... Varnish will become the open source Varnish, cache will become Vinyl from March next year. So by the time we meet next, Ripely and Pipe dream will be Vinyl.

Alright. We're closely approaching the wrap-up... What's next? Let's talk about what's next. The first thing on my list is I want my BAM. What does BAM mean?

**Jerold Santo:** Oh, your big-ass monitor.

**Gerhard Lazy:** That's it. The big-ass monitor. \[laughter\] So now when I switch my big-ass monitor behind me, what I see is all of Pipe dream. All of it. I see all the traffic going through Changelog... It's beautiful. Look at it. I see all the areas, which are like the -- it's just so nice. Seriously. This is the best painting I could hang in my study. And I have it on all the time, so I just see -- it refreshes periodically. This is the fly.io dashboard. On the left, I have the edge... How does the edge behave? This is the fly proxy for our CDN. And on the right, depending on how you're looking at it, on the right I see the Fly app, which is in this case Pipe dream itself, in terms of memory usage, CPU usage, all those things. And it's a thing of beauty. Now I understand when there's a problem, I see the memory when it drops... All the things are just there, and it works well.

So the BAM is done. That was a quick one. And thank you, Fly, for a great dashboard. It was perfect. But the one thing that keeps coming up is out-of-memory crashes. They rarely happen, but they still happen. And even though we have the limit set up, I need to understand what exactly triggers those crashes, how to prevent them from happening... So sometimes - and I say sometimes; I think the last time it happened maybe a week ago, two weeks ago... It hasn't been this week. So an instance, when it gets overloaded, it runs out of memory, it crashes... All it means is that the requests, they get routed to a different instance. And when the instance restarts, it starts with an empty cache. It takes a while for the cache to fill in memory. So I'd like to dig into that. Remember the logs, our events, our metrics, Jerold, that we've been talking about, where currently they're being stored in S3?

**Jerold Santo:** Yeah.

**Gerhard Lazy:** ...and then you have the job, a cron job, which processes them... I'd really like to sort out that pipeline, because part of Pipe dream, part of rolling this out, I just realized how everything is put together, basically, and I think we can improve on that. So what I'm thinking is, if we were able to ship all the logs in a column-like format, so like a wide format, in something like Clichés - and I'm thinking Clichés specifically - this would just make everything so much easier; the whole metrics and analytics pipeline that we have. Not to mention that, in a way, that would be two of everything, and Honeycomb could be one of them... But Clichés, if it stores all these requests, it could be our other event store.

**Jerold Santo:** Right.

**Gerhard Lazy:** And we could visualize all those events... So that would be good. Now, do we know anyone at Clichés, at Clichés Cloud, specifically? Do we have any Clichés Cloud friends?

**Adam Staravia:** Danny... We talked to Danny a couple of years ago. Remember that, Jerold? At Open Source Summit in Vancouver...

**Jerold Santo:** \[01:16:01.24\] I don't remember that, but that's why there's two of us.

**Adam Staravia:** I'm pretty sure we know some folks... If not through acquisition, directly. So we'll hunt our contacts and come back to you.

**Gerhard Lazy:** So Clichés would be fascinating. Or anything that can store lots of events. Because every single request in our case would be stored there. We would batch them and do all of that, but we would write quite a few events... I mean, it's basically every single request would end up in that data store, and then we'd need to be able to aggregate them, and read them back really, really quickly... Which I think would do away with any of the analytics, eventually. But we're currently doing Postgres, with the background jobs... All of that can just --

**Adam Staravia:** Come from that.

**Gerhard Lazy:** ...go. Exactly.

**Adam Staravia:** You know, the challenge there is that -- what stack on Clichés in particular? Because that's tying us to yet another behemoth that might make us hold it wrong, potentially, and be forced to build something else. Clichés spelled H-A-U-S, instead of H-O-U-S... You know, the German version of it. What exactly do you like about that flow? What makes that be the first class citizen for you for data transporting?

**Gerhard Lazy:** So I've used it for a couple of years... We've been using it at Dagger, and continue doing so... And it works really well at a large scale. So it processes not billions, trillions of events. It scales really nicely, and it's really fast. And the Clichés Cloud team specifically, they've been very supportive, and they seem to be innovating and doing things in a very thorough way. So it's something that has always been dependable.

Now, we currently use Honeycomb for like the whole UI thing, but we also store a subset of the requests in S3, and then we process them, and I think we store them in Postgres... So we duplicate these things in a couple of places. If we had a single place where we store them - and this could be like Clichés; that would be like the primary store - we could read any metrics. Whatever we need; we can create materialized views... It's just so flexible in terms of how we can slice it and dice it. It would be our alternative to Honeycomb. And we still love them, and I definitely see us continuing using them, but it wouldn't be the only one.

And we would have the same view in terms for alerting, or monitoring, or anything like that... We would need to do something separate. So it just centralizes every single request coming from every single instance, in this case. Yeah, and obviously, we'll still store them in S3. Clichés can read from S3, which is really nice... It supports like a special Parquet format, which means that you can have data store in long-term storage, in an S3-like system, and then if whatever was to happen with Clichés, it's down, or there's a problem with it... It hardly ever happens. I mean, I think I've seen it only happen once in like almost four years. So it's been very reliable in that way. But it means that we can revamp how we do analytics. I'm not sure how you think about that, Jerold, because - I mean, you've been mostly using that, like the analytics that you get in the app. How does it -- I mean, do you need to upgrade it? Do you need to work with it? Or do you just forget about it, mostly? You set it up and you forgot about it?

**Jerold Santo:** Mostly forgot about it. I think that the biggest drawback is how infrequently it updates at this point... I mean, maybe that's a feature, because we don't check our analytics obsessively, like maybe we could...

**Adam Staravia:** On the daily... Yeah.

**Jerold Santo:** \[01:20:02.28\] That being said, if we can get that information faster and learn something along the way, I think it's worth it. And I'm certain that this would change the way that we do things enough that we could get that information much faster than via a cron job. So I'm interested in it. Would it bring huge value to us to be able to see the downloads faster? Probably not, because we've habitually not done that. We just check in on it every once in a while... But I'm up for learning and trying and improving, so I definitely think it's worth the R&D budget.

**Gerhard Lazy:** Okay. I mean, again, it comes as a suggestion. I think we've been doing this for such a long time in terms of discussing these things in public, and I think this keeps coming up. We can defer it. It doesn't need to happen. It's just something that I had to touch in the context of the Pipe dream, as I was looking at where the metrics are going, the feed requests, how is that like put together, what do we write in S3... All those things. The different buckets... All that stuff I had to go through, basically, part of this.

**Jerold Santo:** Well, I'd love just to chop that part off. It's just there as a thing that we do, but it doesn't have to be that way. That's just how we did it.

**Gerhard Lazy:** Okay. So do you have a thing that you would like to improve between now and the next Kaiden, either of you? Because I can keep going through this list, but I'm wondering if there's something that you're thinking about, or something that's bugging you that you would like to see improved...

**Jerold Santo:** I've kind of just become content of late with the way things are. Adam?

**Gerhard Lazy:** Okay.

**Adam Staravia:** Hm... I think the only thing I think about really when I think about this system - it's kind of sad, in a way... It's that if eventually - and it's not the case currently, but if eventually the case is that our true traffic comes from one of the spokes, versus the hub... Like, how important does the hub remain? And the one thing we're not tracking really is the mp4 file that we upload to YouTube in terms of the system, right? So we don't have a store. So we have the mp3 for the Plus version and the public version side by side, in perpetuity, for all time, back to episode one of all podcasts. What we don't have is that corresponding video file, because it's not part of this pipeline. It's not part of the serving pipeline. And that's what I think about. And I think about the analytics and the effort there... You know, how does the change to watching, viewing, listening patterns change this show over time change the system? That's what I think about. So I'm not really sure.

**Jerold Santo:** I've certainly considered a modification where we upload the mp4 to our system, and let it redistribute to the various places that we want it to live. That's a much heavier lift than I think there's benefit, at the moment at least...

**Adam Staravia:** I agree, yeah.

**Jerold Santo:** We still have the MPs, so it's not like we don't own that content. We just don't own it on R2, alongside our mp3s.

**Adam Staravia:** And it's kind of a sad spend of money, to store a file you send to YouTube one time.

**Jerold Santo:** Right.

**Adam Staravia:** You know? So I get that.

**Jerold Santo:** And we could also start to get diverse with it and say "Well, we're also going to be on Peer Tube, and we're going to upload to Rumble", or I don't know what all these places are now, because people kind of scatter from YouTube, and then they gather again, and they scatter... But so far, the point of our video is to be on YouTube at the moment. And so we haven't thought beyond that. But if YouTube changes in some sort of dramatic way, where - I mean, we've seen changes over the time, where it's like "Let's be in more places", similar to how we're not just on Twitter/X anymore, we're on more social networks... There may be a day when that happens with YouTube, and we'd be happy to have the pipeline set up to where we can just add another connector to it and say "We're also on this video watching platform." Or "You can view our stuff directly, watch it directly on our website" and we'll let Cloudflare bear that burden. Although if it's passing through Pipe dream, we're going to have some serious bandwidth going through Fly.io.

\[01:24:27.16\] So those are things I've thought of, but I've never been even -- at this point, I'm not even close to pulling that trigger. Gerhard, you're on YouTube now, but you also have makeitwork.tv, so you're actually tackling this, to a certain extent.

How do you do it?

**Adam Staravia:** Jellyfin, right?

**Gerhard Lazy:** That's one, yes. Jellyfin is -- if you have a client, that's right, you connect to the server, and you can download things, you can store them on your device. So it's like a media library, a proper media library and a media server. I find that works really well. I mean, I always prefer watching it that way. But I also store it on a CD, and in this case, Bunny. So Bunny has a stream, I think it's called, and I think Cloudflare has streamed as well, where you just basically upload media content, in this case mp4 files. So the CDN part works well. I would love to replace that, to be honest, because I'm not entirely happy with how that system works... The chapters are a bit clunky. There are quite a few things that are clunky. The trick play isn't great... Again, lots and lots of things. Just the way you upload things is just too much work... So I'd love to automate that. But YouTube really is like the main distribution mechanism, not just because of how easy it makes it to just upload the file, and then it gets redistributed everywhere, but also -- it's almost like you have something to sell. Do you go on eBay, or do you go to a flea market or elsewhere? Do you build like your own shop to sell that thing? And eBay a lot of the time is easy because that's where a lot of the buyers are. That's where people are looking and searching. Or Craigslist, or Gumtree we had in the UK; I think it's still a thing. So YouTube is a place where lots and lots of people already are, so in terms of distribution it just makes it so easy.

Now, I'd like to give the option of "Hey, if you don't want YouTube, that's okay. You can also download it from the CDN" that I pay for, that I set up, and in this case I haven't built, but that's coming. Or Jellyfin. Now, I don't know how many users would set up a Jellyfin, to be honest, for Changelog... But I like the idea of basically -- having that one-to-one relationship between the creator, and the watcher/the listener/the viewer. There's nothing in between. So YouTube can't push its ads, YouTube can't ban certain content in certain places if it happens, however it happens... Again, it's very difficult to know that, because you need to be in those places to know how that works. And I also like the idea of people being able to download the content. And again, the podcast players make it easy. For YouTube, you have to pay that premium. You have to go YouTube Premium, which I do, and I have for many years, and I think it works great... But again, my experience, my YouTube experience is very different to most people, because I don't think many people pay for YouTube. It's just like an extra expense. So that's my take. Yeah.

**Jerold Santo:** Yeah, it'd be cool if there was a vibrant community of people that consumed video via open standards, like they do with podcasts. I mean, the coolest thing about podcasting is that phrase, "Get this wherever you get your podcasts." And it's like, that's because it's an open standard that you can just directly subscribe to a feed, and people can build apps for those... And that's amazing. That doesn't exist for video. Will it someday? Maybe. There are nerds out there, and we get the emails about open standards for video podcasts.

\[01:28:09.00\] Actually, Apple launched the iTunes Podcast section, with video podcasts as like a first-class citizen, it's just that nobody -- the bandwidth was so expensive back then. This is like either pre YouTube, or like right around the time that YouTube started. And people just weren't watching. We just didn't have the technology to actually make that a thing that you just watch. You didn't have the phone, you had to like to move the files around, they were large. I think Mac Break weekly was like one of the few ones we ever saw. They were like shipping 4k video podcasts in 2007 or something, and it was crazy.

**Gerhard Lazy:** Wow. That's hardcore.

**Jerold Santo:** Because they come from the TV side, where they're used to putting out video... And where most of us are just coming from the audio side. Anyway, those things existed. Apple obviously just kind of like -- it still actually is part of their RSS spec, but no one uses it. Even Apple Podcasts, I'm not sure if it even uses it. Spotify has their own deal for video; it's not using the open way, it's using their own proprietary way. There's weirdness there, where if your video file duration or details differ from your audio file, you may end up serving one or the other, even to audio listeners, which you don't want to... And so it's just kind of murky right now. And I think it would take some sort of black swan event and maybe a sea change in opinion, and some sort of new tech that makes it feasible, at which point I'd be all about it. I just think right now it's like a lot of effort... And there's a lot of effort to like to re-encode your video into all these different formats, depending on blah, blah, blah, and then serve that... A lot of cache misses if you'see got six versions of your video, depending on the client...

**Adam Staravia:** Six times the storage, too.

**Jerold Santo:** Yeah, it's like money, time and effort for right now a very minuscule advantage.

**Adam Staravia:** Yeah. Let YouTube pay that price, and their tech stack, and their developers, and their bandwidth, and their servers etc. Yeah, my only concern is that really, is like "Where do we begin?" Where do we reach diminishing returns in innovation, with the CDN, beyond mp3 and smaller file? It doesn't seem to naturally scale to the video, because the incumbents have that solved in ways we just don't see that we need to solve those problems.

The only problem I guess that I see is the fact that we don't have this video file artifact alongside the mp3 artifact, that is the same thing but a different flavour of it. It's elsewhere in our archiving stack, and I would say largely inaccessible... Certainly not via an API. Potentially, but it's not.

**Jerold Santo:** Right.

**Gerhard Lazy:** I think building a standard or contributing towards the standards takes a really long time, and lots of effort. And that's why no one wants to do it, and they're waiting for someone else to do it, because they know how much investment that takes... No one's in the mood for that type of investment.

**Jerold Santo:** Right.

**Gerhard Lazy:** I think it's going to be very interesting what happens with AI, because there's a lot of money right now in AI, and I think it will change, not before long... So where will that money go next? We'll see. I'm definitely curious for the next big thing which is coming... But one thing that may work well is if Changelog had an app, had a native app, whether it's an Android or iOS app, and then you control how you display the video and the MP3. And if you had something like that, then you'd be in full control how you would expose your mp4 files, and how you would integrate them in the player. And that's a more holistic experience, where you can do transcripts really well, you can do comments really well, maybe integrate with some sort of Zulip or something like that, where it feels like a system, and it's more like a community of people that are interested in this type of things, rather than just some content that gets distributed on different platforms.

\[01:32:13.25\] Again, the problem in that case is that most people are already on those platforms, so it's easy for them to consume things. But there will come a point where they just want something different. The float plane - I mean, that's a new thing that's been around for a few years. So that's one example. There's another one. I forget what it's called... I know that you can pay for -- man, I wish I remembered the name. Furthermore, I was doing a research maybe like six months ago... Or like nine months ago, actually; it was more than six months ago. And I was looking at YouTube alternatives, and there's like this other platform for media, which stores and distributes higher end, like 4K videos, 8K videos... But for that, you end up paying. So it's not free. And then you get creators that publish only on that platform. I forget its name. I can look it up, and maybe we can add in the show notes, because I have it somewhere. But that is another interesting thing. Vimeo... I remember when Vimeo was a thing. But I still -- I know it's around, but I don't think many still use it, in terms of like people going and browsing Vimeo. I don't think it's even a thing anymore.

**Jerold Santo:** Yeah, they pivoted quite a bit. It's a very successful business to this day, but it's serving enterprise, and more professionals, who are using videos for various purposes, not as a general consumer product at all.

**Gerhard Lazy:** And video is hard, because the transcoding part is really hard. And... Yeah. I mean, you always have the trade-off, do you pay storage, or do you pay for compute? As in, do you transcode on the fly, like Jellyfin and Plex does, and then you need like GPUs? Or do you pre-transcode, and you save multiple versions, you store multiple versions, and then you serve those? And then you have so many codecs. I mean, it's just not even funny. Like AV1, H265... What do you pick? Different phones, different devices... It's not an easy -- mp3 at this point is almost like a universal format. There isn't a video equivalent. That's a hard problem.

**Adam Staravia:** Yeah.

**Gerhard Lazy:** Anyway.

**Adam Staravia:** That is what makes video dramatically harder. And that's, I think, where the divide is at. And that's why I brought that up, is because you've got this divide of the potential of the precursors that almost everyone, that I'm aware of at least, is still paying attention to podcasts via not really a podcast client anymore. They're usually on some sort of platform. And they're usually -- they ask me what show do I produce, and I tell them, and they immediately open up YouTube, and they start searching for it. "Oh, is it this one?" I was like "Yes." "Okay." So that's where folks are tending to go. And here we are, optimizing for this, and the migration may be that. Do the worlds eventually collide? How do they work long-term, et cetera? Still no. And I think... Yeah, exactly - do you transcode it on the fly, or do you make multi versions of it? I think you just don't do that unless you know for sure you should... Just transcode if you can.

**Gerhard Lazy:** Yeah. I know that Jellyfin, that's exactly what it does. And I really like it for that, because it's very good on storage. But the CDN, the one that I use, does transcode, so they store multiple versions. Now, luckily, I capped the maximum, and I think I only published 1080p on the CDN, because of the multiple versions which they transcode, and they make available... But on Jellyfin it's just like the 4K one, so that's my approach to it.

**Adam Staravia:** What are your thoughts on number four here? Four, five and the question mark here.

**Gerhard Lazy:** Well, Changelog.com \[unintelligible 01:35:52.26\] what I was thinking is there are a few utilities that we're using that need an upgrade. For example, Dagger needs an upgrade really badly. It's like such an old version on the Changelog. Upgrade or replace, still undecided. We'll see how that goes.

\[01:36:10.17\] The deployments - I wanted to improve them for a while. There was always something else... So improving the time to deploy. I think was like four minutes last, or three minutes. There were two minutes at some point, and then we went back to three minutes again... And I know that at least a minute and a half of that is Fly.io. So what do we need to optimize there, so the deployments are a little bit quicker?

Postgres - I mean, it's been stuck on 16 at this point... I think. 16 point something. So maybe we want to upgrade something there, so we don't fall behind too much... And replacing Overwind with Unit. So Overwind is a supervisor that runs, for example, the log manager, it runs Varnish, Vinyl, it runs the proxies... It runs multiple things in the context of the Pipe dream, and Ripely, really. But Overwind sometimes, some things can get stuck because of just how it's configured. There's some duct taping there, especially how the logs are streamed. So that's something that I'd like to improve. And I know that Unit - I've used it in the past - is very reliable. It's a very old supervisor, a very Unix-y supervisor... So I'd like to replace Overwind, which is Go-based, with Unit, which is much more old school, and it does everything we need. So that's like an improvement, but that's a Ripely/Pipe dream improvement. And the question mark was like "What else?" I think we tackled the question mark in the conversation.

**Adam Staravia:** Gotcha.

**Gerhard Lazy:** Alright, so we're almost at the end... If you like this, as a listener, as a viewer, you can like, subscribe - you know the drill - and comment. That's something that is also an option. I mean, we touched on many things. Maybe you have a few ideas of how to do things better, or maybe there are a few suggestions that listeners and watchers have...

I'll be more than happy to answer any follow-up questions, as we will all. Suggestions, maybe, for the next get-together, for the next Changelog get-together... You can do it on the YouTube video. I think you -- do people, by the way, comment on YouTube videos, the ones that you post?

**Jerold Santo:** Yeah, a little bit.

**Gerhard Lazy:** Okay. And do you reply to those comments?

**Adam Staravia:** Oh, yeah.

**Gerhard Lazy:** That's a lot of work. I just discovered that recently, last week. Oh, man. When you get like 100 comments, it takes a while to go through them... But it's a good problem to have, for sure. Zulip also works... I think all of us are there. Or even GitHub. That's also -- we have the discussion for this Kaiden.

**Jerold Santo:** Right.

**Gerhard Lazy:** Just remember to tag me, because otherwise I will miss your message. I have many things on mute, and unless you CC, I'll miss it.

**Adam Staravia:** Absolutely. Same. Too many inbounds must get tagged or cc'd.

**Gerhard Lazy:** One more thing. Last thing. Last thing and then we're done, okay? Last thing. So you know about Make. It. Work.TV. Make. It. Work. Club is something new. So the 100 Gigabit Home lab comes from Make. It. Work. Club. It's on school. It's a community of the most loyal Make. It. Work.TV members, but also those that want to go beyond just watching. So the ones that want to interact... We meet every two weeks. Both Adam and Jerold have an invitation. While we were talking, I sent you an invitation, so you can join. You can see the various conversations which are happening there... And the next one is tomorrow, and it's usually every other Friday. It's usually 9 a.m. Pacific time. Tomorrow's one is going to be 7 a.m. because some of us have kids, and meetings and other commitments... So it's going to be before work for some people. We'll be talking about a smart garage door opener. We talk home labs, we talk Talos, Linux, that comes up quite a lot... Quite a few things. Kubernetes... It's all there. You can go log in and check it out.

\[01:40:01.19\] Adam and Jerold, you are part of it. I just wanted to get it. I just wanted to get it into a point where there's enough to show and enough for you to see. So it's been going on for about a month now, a month and a half... There are plenty of threads... And there's only, I think, 17 members. So it's not that many. It still feels like a small community, it has a small vibe to it... It's a bit like this, but with more people. So it can be a bit more chaotic. I think the 100 gigabit, I think we're maybe 9 or 10 people. So it was quite the group discuss... But still, with a presentation and focusing on them, and... You've seen the video, Jerold, so you know what it was like.

**Jerold Santo:** Cool.

**Gerhard Lazy:** But did you get your invites? Just double-checking that, in your email. I just want to make sure that part worked.

**Jerold Santo:** I've got mine right here.

**Gerhard Lazy:** You've got yours. Adam, did you get yours?

**Adam Staravia:** Let me see if I got mine.

**Gerhard Lazy:** And then you can decide whether you want to accept it or not, but... I just wanted that to be out there.

**Adam Staravia:** I do have my invite. I do see it. Yes.

**Gerhard Lazy:** Thank you.

**Adam Staravia:** I have my invite.

**Gerhard Lazy:** So this is the Changelog++ equivalent. You can think of it like the Changelog++ equivalent.

**Jerold Santo:** Gerhard++.

**Gerhard Lazy:** Yeah. You can drop in any time when we meet every two weeks, and you're more than welcome to look at the threads, comments, ask for like -- someone, for example Misha, he was asking, he wants to build his own router... A router, how the Americans pronounce it...

**Adam Staravia:** A router.

**Gerhard Lazy:** Router, yeah... So he wants to build that... And Nail built, for example - it's like a smart garage door opener. He just didn't want to get out of the car for the door to open, so now he has all that programmed, so he's going to talk about it tomorrow.

**Adam Staravia:** Interesting.

**Gerhard Lazy:** Yeah, there are quite a few things. So check it out. Alright, that was me... How do we want to wrap it up?

**Adam Staravia:** Well, you put a bow on that present there. That was cool. Talking about a garage door open would be kind of cool... I just talk to my phone. I just tell Siri, "Open the main garage", and she makes it happen.

**Gerhard Lazy:** That's nice.

**Adam Staravia:** And it's just part of Apple HomeKit... And the fact that my garage door opener is on the network, and it has those kinds of... I really didn't do anything to make that happen besides just flip a switch, and talk to it. And that was kind of cool.

**Gerhard Lazy:** That's really cool.

**Adam Staravia:** Now, sometimes she's like "You don't have a main garage door." And I'm like "No, no, let's try this again. Hey, Siri, do this." And she's "Okay." Gosh... Shush. Don't be opening my garage, girl... \[laughs\] I had to stop her right now. Yeah, she was hearing me say her name. She's excited. She's always like "Can we open the garage, please?" Or maybe not...

Or maybe not...

**Gerhard Lazy:** What are you keeping there? What are you keeping there? Breaking bad sort of situation going on... \[laughter\]

**Adam Staravia:** Yeah, yeah, yeah.

**Gerhard Lazy:** \[01:43:04.23\] No, no, no. It's not that, yeah. But someone had to set up the smart garage door for you, right? I mean, did you set it up? Because you need to have the whole -- it needs to be hooked up to your home network.

**Adam Staravia:** All I did was enable the Wi-Fi access to my network, and the garage door opener is on the network, it has an app that runs it... And the app allows me to install, I guess -- it's been so long since I've touched it, so I don't remember how I did it, but it was... It was like shortcuts, I guess, essentially. You can create shortcuts on your iPhone. And so that's all I did, was just leverage the shortcuts that talk to the app that has the authentication to the thing via the network... And that's whether I'm at home or not at home. So it's not even land-bound, it's its WAN-bound, so it's really awesome. I can be literally in the mountains, with very little service, and I can tell my garage door to open or close. And I can even tell if it's open or closed, because if I say "Hey, close it", she's like "I'm closing your main garage." She's like "Oops, already done." She reminds me that it's already closed. So I didn't really have to do much to do that, thankfully.

**Gerhard Lazy:** But to set it up. So to take a regular garage door...

**Adam Staravia:** Right. A normal one.

**Gerhard Lazy:** That part. A normal one. That's what Nail did, and that's what he's going to talk about.

**Adam Staravia:** A non-networked one... Yes, that would be -- that'd be dope, honestly.

**Gerhard Lazy:** That's what he's going to talk about, how he set up the whole thing, all the devices, what did he pick, how did he connect everything... It was just like a regular garage door. It had nothing. And then he made it smart.

**Adam Staravia:** Well, the good thing about those garage doors - they tend to have an outlet which has two plugs, one being used by the garage door opener, and then one that's used for nothing, basically. So thankfully, if you needed an outlet for your device to pair it to, I'm assuming the answer is maybe yeah, right? We'll find out. \[unintelligible 01:45:05.02\]

**Gerhard Lazy:** Mine is just mine is just a regular one, exactly. So that's what I want to do. Like, if I wanted to set this up, what would I need to do to make it work as smart one?

**Adam Staravia:** Yeah. I think the thought pattern around how to tackle that... You know, I simplified it by just having one that was already networked. But if you have one that is not networked, then there you go. You've got to create the network.

**Jerold Santo:** I know how we can end this show. I can just ask Gerhard to review my new hat.

**Gerhard Lazy:** Your new hat. Yes...! I thought it was there. Yes...! Oh, I'm so happy.

**Jerold Santo:** What do you think?

**Gerhard Lazy:** I'm so happy there was -- I think it looks amazing on you.

**Jerold Santo:** Do you like this hat? I know you like blue...

**Gerhard Lazy:** I love it. I love it.

**Jerold Santo:** That hat's blue, it's a blue UnderArm our hat...

**Gerhard Lazy:** Man, I was looking for it everywhere, and I thought "I think I left it in Jerold's truck."

**Jerold Santo:** You did.

**Gerhard Lazy:** It makes me so happy to know that you have it.

**Jerold Santo:** I've got it here for you, and when we get together again, I will bring it to you.

**Adam Staravia:** There you go.

**Gerhard Lazy:** It's yours. It's yours.

**Jerold Santo:** It's mine?

**Gerhard Lazy:** \[unintelligible 01:45:57.11\] a gift. It's yours. It suits you so well.

**Jerold Santo:** It does look good on me, you're right.

**Gerhard Lazy:** I know you like hats, so... It does.

**Jerold Santo:** Thank you.

**Gerhard Lazy:** It's yours, Jerold. It makes me so happy --

**Adam Staravia:** It's your hat now, Jerold. Hats on to you, Jerold.

**Jerold Santo:** Hats off to Gerhard, hats on to me.

**Adam Staravia:** \[laughs\]

**Gerhard Lazy:** I think we may have a title there.

**Jerold Santo:** I think we might. Hats off to Gerhard. Alright, Kaiden. Good stuff, you all.

**Gerhard Lazy:** Kaiden.

**Adam Staravia:** It was awesome. Bye, friends.
