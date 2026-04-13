**Jerold Santo:** Gerhard is here once again. We are chaining in 2024. Yeah.

**Gerhard Lazy:** Great to be back.

**Adam Staravia:** Two zero two four. Here we go.

**Jerold Santo:** We made it. We're here.

**Gerhard Lazy:** Yeah. The first Kaiden for this year. And it happened so soon.

**Jerold Santo:** We all made it back from Chicago... No crazy stories on the way home. We've already shared all of our crazy stories on the way there, so... Here we are.

**Adam Staravia:** Did we actually share those stories, though? I think it was like in a --

**Gerhard Lazy:** I've learned how to say cheers, Adam and Jerold style. It involves a single glass... \[laughs\]

**Adam Staravia:** Oh, yes...

**Gerhard Lazy:** That was so funny. \[laughs\] That was one of my highlights.

**Jerold Santo:** Say more.

**Gerhard Lazy:** So apparently, the way you say cheers is both of you hold the same glass, you hold it up... So \[unintelligible 00:01:23.08\] holding your hands... And you say cheers. I haven't seen that one before, that was so funny. \[laughter\]

**Adam Staravia:** That's funny that it's funny.

**Jerold Santo:** It is funny. It was so inconsequential to me, I don't even remember it. No offence...

**Gerhard Lazy:** I think it was a picture moment. I think we have a picture of that somewhere.

**Jerold Santo:** We're holding the same glass?

**Gerhard Lazy:** Pretty much, yeah.

**Jerold Santo:** We're pretty close. We're pretty close around here.

**Adam Staravia:** We're not holding the exact same glass. We're holding our own versions of the glass, and we're clinking them, right? Is that what you're talking about?

**Gerhard Lazy:** No. No, no.

**Adam Staravia:** Gosh, maybe I am missing it.

**Gerhard Lazy:** There was a picture of this, so...

**Jerold Santo:** Pics or it didn't happen. Yeah, I don't remember that. Pics or it didn't happen.

**Gerhard Lazy:** No, no, it didn't happen. That's okay. What happened in Chicago can stay in Chicago.

**Jerold Santo:** Unless you have a picture, and then it can come out. I'd have no problem with it.

**Gerhard Lazy:** I can look it up, it's there somewhere.

**Adam Staravia:** Okay... I'll take your word for it.

**Jerold Santo:** So the receipts are in the show notes. If Gerhard can come up with receipts, they will be in the show notes. If not, then we just know he's just fabricating evidence... Yeah.

**Gerhard Lazy:** Yeah.

**Adam Staravia:** Since this is the new year, can I just say that I remember when Gerhard used to version our infrastructure by the year...

**Jerold Santo:** Yes.

**Adam Staravia:** And now it's sort of versioned, I guess, every two months, or kind of continuously, in a way, really... That was crazy, right? We're in a whole new era of continuous improvement.

**Gerhard Lazy:** Yeah. I mean, I do -- it's almost like a generation. So for example, our Fly app, the one that is currently running in production, is 2022, 03, 13. And guess how I remember it? I just remember; it just sticks with you. And the next one, the one that we're currently experimenting with, is 2023, 12, 17. So 17th of December, this is the new generation of the Changelog app.

**Jerold Santo:** That's already old and busted. It's '23. We're on '24 now.

**Gerhard Lazy:** Yeah. Well, guess what? We can delete that one and set a new one up, and that's okay.

**Adam Staravia:** It's too easy, right?

**Gerhard Lazy:** Yeah. It's too easy.

**Jerold Santo:** I like your propensity to date-stamp things, because it's very nice for remembering "Hey, when did I do that thing?" What I don't like about it is it makes things feel old. For instance, one subdirectory in our codebase that I do not appreciate - and I'm here to air my grievances - is 2022.fly. A, that's just an ugly folder name. B, it's forever ago. C, I have to like to go in there to do stuff with Fly, when I could just have all that in the root and just be chillin'. So I'd just like you to defend the decision-making process there, Gerhard, and explain it to me... How did that come to be?

**Gerhard Lazy:** So really it was the generation of the app. It was 2022, we've set it up for 2022, and I just created the Fly folder. Because before, if you remember, we had the various Kubernetes clusters, and then we had the versioned by year...

**Jerold Santo:** We were kind of straddling for a while, weren't we?

**Gerhard Lazy:** Yeah, exactly. This was our migration to Fly, which happened in 2022. That's how long ago it's been.

**Adam Staravia:** Wow.

**Gerhard Lazy:** And since then, we really haven't changed the app. We've done a bunch of other things, but that app in its implementation state as is. There is a new fly.io directory, where we're starting to capture apps...

**Jerold Santo:** Oh.

**Gerhard Lazy:** Yeah, that's been there for a while.

**Jerold Santo:** Is it year-stamped?

**Gerhard Lazy:** It's just Fly, because the apps are timestamped in the directory, and the one that we have there, you'll see it's the Dagger engines.

**Jerold Santo:** Gotcha.

**Gerhard Lazy:** Because our CI also runs on Fly, the workers themselves... And that's what that is. So the new app, which is basically part of a PR, 492 - and we'll get to that in a minute...

**Jerold Santo:** In flight, in progress...

**Gerhard Lazy:** Exactly. It's in flight. It's also in that directory. So the app is timestamped. And we have multiple apps, because the idea is we have more than one. Changelog social, for example is another app that we run on Fly, but that's in a different repo. Maybe we consolidate, maybe we don't. I don't know. The point is, it's a nice way to store all your apps, because we have more than one. And then you know which one you're targeting. It makes it very simple to not make mistakes when you want to work against a specific app. You can't basically be in the root, and the root has changed, and then maybe you're targeting a different app instance... This way it's very clear which app instance you're working against.

**Adam Staravia:** It makes sense.

**Jerold Santo:** Well said. Good defence.

**Adam Staravia:** Are those tied to the machine then, like you said? Or does that make sense, to tie it to the machine? Or did I miss that part while I was trying to grok everything you're saying?

**Gerhard Lazy:** No, it's just the app instance. So each app is backed by multiple machines.

**Adam Staravia:** Okay.

**Gerhard Lazy:** So that is like a subdivision of the app.

**Adam Staravia:** And this Fly directory, Fly.io directory is part of the 492 pull request, or this is predating that?

**Jerold Santo:** It predates it.

**Adam Staravia:** Okay. Because I didn't see it in master.

**Jerold Santo:** It's there. I've got it in my codebase...

**Adam Staravia:** Is it there on master?

**Gerhard Lazy:** Yup.

**Adam Staravia:** It's just hidden. Oh, I see it. Because it only has one directory, it's --

**Jerold Santo:** There's no year, so --

**Adam Staravia:** That's why. Okay, cool.

**Gerhard Lazy:** But more are coming. More apps like this one, for example, the second one... Because we've been doing this for a while. We have two apps, two Changelogs running at the same time, and we don't want that to be part of a pull request for too long. This 492 is a special case; again, we'll come back to that. But that's the idea. You can have multiple apps running at the same time, and you do like a long blue/green.

**Jerold Santo:** \[06:20\] Awesome.

**Adam Staravia:** I dig it.

**Gerhard Lazy:** One thing which I would like to do now, because it is the beginning of a new year, is taken a step back and take a bigger take on this.

**Jerold Santo:** Okay.

**Gerhard Lazy:** So what I'm thinking - and we have time; this is edited, so it's okay... \[laughter\]

**Adam Staravia:** It's a big idea.

**Jerold Santo:** When I answer this real quickly, everybody will know that there's like six minutes of silence that got edited out while I was thinking about my answer.

**Gerhard Lazy:** What is the one thing that you want to achieve this year?

**Jerold Santo:** Regarding changelog.com?

**Gerhard Lazy:** You can make it as big or as small as you want.

**Jerold Santo:** Okay.

**Adam Staravia:** We have some big ideas. They're more like features though, not infra.

**Gerhard Lazy:** We can go there. This is basically so we don't constrict the creativity and the space.

**Jerold Santo:** Right. This is open-ended on purpose. He's setting us up here.

**Gerhard Lazy:** Open-ended on purpose. Yes. And mine is big. I can tell you, mine is really, huge.

**Jerold Santo:** Okay.

**Adam Staravia:** Oh, wow. Why don't you go first?

**Gerhard Lazy:** Okay. It's as if I'm prepared... \[laughter\]

**Adam Staravia:** Yeah.

**Gerhard Lazy:** I am. So I'll go...

**Jerold Santo:** No edit necessary here. Yeah, go ahead.

**Gerhard Lazy:** My birthday doesn't happen every year.

**Jerold Santo:** That's right, you're a leap-year baby.

**Gerhard Lazy:** And this one is special, because it also kicks off a new decade for me.

**Jerold Santo:** Oh...!

**Gerhard Lazy:** So just to put it into perspective, the next time that my birthday coincides with a new decade, I'll be 60 years old.

**Jerold Santo:** So this is like \[unintelligible 00:07:40.08\] score. You're scoring.

**Gerhard Lazy:** Yeah, pretty much. So after two decades of hands-on experience, which is well over 10,000 hours, I have this urge to produce something that I haven't done before. Something in the content space, something that combines audio, and video, and AI. And AI is a very important element. And 2024 is a combination of so many things for me, that it makes me really excited for it. Because it doesn't come often.

**Jerold Santo:** No. This is a lot of pressure.

**Gerhard Lazy:** I think this is it. The next one I'll be 60. So... It's big. I told you it's big.

**Jerold Santo:** Do you have more than that? Or is that all you're saying?

**Gerhard Lazy:** That's all I'm saying... Because --

**Jerold Santo:** So big that you're not going to put any sort of box around it yet.

**Gerhard Lazy:** Remember last time when I've done this? Let's see if this time it works better. Bringing something up, and then disappointing you. So I'm not going to say anymore...

**Jerold Santo:** Yeah, don't build it up too big.

**Adam Staravia:** So content, and AI.

**Jerold Santo:** And video and audio.

**Gerhard Lazy:** Yup.

**Jerold Santo:** Okay. Is there any more details? That's it.

**Gerhard Lazy:** Just content space.

**Jerold Santo:** And it's going to ship on your birthday?

**Gerhard Lazy:** Before, but yes. I'm going to do something special for my birthday, for sure.

**Adam Staravia:** It's a one-time thing, or is it an episodic thing?

**Gerhard Lazy:** I think it's going to be an episodic thing... But I have like all these interests in hardware, and software, and combining things... And it is the long-term that I'm thinking about. Not months, not even the years. Decades. Something that can be tracked over decades. Something that when I'm 60, I can look back, and I can say "Wow, the last 20 years have been amazing." So that's the timescale that I'm thinking at.

**Jerold Santo:** Okay, so you're going to start something, but you're not going to finish it. It's going to be a new thing you're starting.

**Gerhard Lazy:** Yeah, something like that.

**Jerold Santo:** Okay.

**Adam Staravia:** How do you start and not finish?

**Gerhard Lazy:** I'll finish when I'm 60.

**Jerold Santo:** Or when he's done.

**Gerhard Lazy:** Or when I'm done, exactly.

**Adam Staravia:** Okay.

**Jerold Santo:** \[laughs\]

**Gerhard Lazy:** But this is enough. I had fun...

**Adam Staravia:** How frequent are these episodes? Are they yearly, are they monthly, are they weekly?

**Gerhard Lazy:** Let's see what happens.

**Adam Staravia:** Okay... Wow.

**Jerold Santo:** He's not going to say. He's \[unintelligible 00:09:35.11\] That's a good goal. I mean, I feel like I shouldn't have any goals shared after that one. I mean, I'm gonna sound like a mere piker no matter what I say. \[laughter\]

**Gerhard Lazy:** We can make a smaller one. I mean, this is big. There are different timescales in the context of --

**Jerold Santo:** This is like a project of a lifetime.

**Gerhard Lazy:** Yeah, something like that. It feels that way. Almost like a next evolution of something that I've been working on for a long, long time. And Ship It was part of it, by the way. That was just a small part.

**Jerold Santo:** It was a stepping stone on your way to this other thing.

**Gerhard Lazy:** \[10:04\] Pretty much. And before that, it was the RabbitMQ videos. IGIR. Those were fun. That was like all \[unintelligible 00:10:07.27\] videos.

**Jerold Santo:** Well, I hope you achieve that goal.

**Gerhard Lazy:** It's still live. Tgi.rabbitmq.com. People can go and check it out. I was terrible... But I've learned so much. \[laughter\] So go and have some fun.

**Jerold Santo:** There you go.

**Gerhard Lazy:** See how not to do videos... I was learning.

**Jerold Santo:** Yeah, that's how you learn. Alright... I liked that one. Adam, what's your goal for the year?

**Adam Staravia:** Oof...

**Jerold Santo:** Big or small. It doesn't have to be as big as Gerhard's. It probably won't be.

**Adam Staravia:** I have to.

**Jerold Santo:** Oh. He always does this. He'll end up with seven...

**Adam Staravia:** Yeah. Well, I think we know what one goal is, which is to finally get Plus in-house, meaning not on Super-Cast. And I think that there are some things that will all gain from that. Both how we promote it, how listeners understand it, how it can grow, how it can be embedded in the application process, and just how all the workflows work. I think there's a lot of gain there, and I know we've been taking incremental steps towards that.

And I think one that you and I were kind of passionate about, Jerold - so if you don't mind me talking about the one we just talked about at the tail end of the last year, which has the word J-O-B in it, and I guess an S... Is that cool? Can I mention that?

**Jerold Santo:** Well, we're coaling, so yeah, go ahead. It doesn't mean it's going to happen, but it's a goal. Yeah, I think so... I think it's worth talking about.

**Adam Staravia:** And it feels even weird to put this as a goal, because it seems very simple, but I think to execute at the level we like to execute at, it is not very simple. And so we were talking with our friends at Go Time about just different ways to sustain that podcast... And during that conversation, the idea of a job board came back up, as a way to alternatively sustain a podcast. So that show has not had the best track record of being well sponsored, but it also is a really awesome podcast. And that's not its fault that it has trouble gaining and maintaining sponsors, I think it's just a challenging thing for the podcast industry. And I was like "Well, what if we found a different way to give value back to that community?" And so the conversation sort of stemmed towards, you know, it may be a Go-focused job board. And then I think afterwards, Jerold and I had a brief conversation, or it was in Slack or something like that, like "What if it was just changelog. Jobs?" So there is a .jobs TLD, and so like if we had changelog. Jobs, and we made it a SaaS product where you can subscribe to it to have jobs there frequently, being the job promoter, not the jobseeker... And we leveraged our podcast network and found a way to automatically or systematically pull those job promotions in and out of the podcast, to make them dynamic, basically, then we have a real interesting way to have a job board that has an interesting economic footprint behind it, where it's SaaS-based or one-off based... And we really do a pretty good job of this job board. Not just like put it up and go post a job kind of thing, but far more embedded into the network.

I think if we can execute on that well, then we have a decent, I would just say moneymaker on our hands that helps us sustain whenever sponsorship's slim, or as we prop up Plus, and that becomes more and more of a leg... Which, honestly, for those who support us on the Plus side, we want it to be more of a leg to our chair, I suppose, in terms of stability... But we never really anticipated it being that. Traditionally, sponsorships have always trumped the amount of revenue we can gain from Plus. But I think there's an untapped market on subscribers supporting you. And I think that's where bringing Plus inside gives us that chance, but then also this opportunity for Changelog. Jobs being a great indie re-entered place to get and look for cool jobs. And I think one part of that is maybe the vetting process.

\[14:06\] So lots of interesting things on how to execute, not just throwing it up and "There you go, post a job", but something that's a bit more well-executed, and really for the indie market. Because most of the indie markets in the job space that have been boards have been bought up by the big guys, the big folks.

**Jerold Santo:** Or neglected.

**Adam Staravia:** Yeah, or neglected. I mean, GitHub Jobs is pretty cool, but - I mean, obviously, GitHub is not jobs... And I think it went by the wayside last time I checked. Early, early on, that was one of our first sponsorships here on this podcast, and it's kind of cathartic, Jerold, to say that my dream thing for this, I suppose goal, is to promote Jobs - I said before, we will never promote jobs on this podcast. \[laughs\] I'm never saying again, man...

**Jerold Santo:** Why are you telling \[unintelligible 00:14:51.06\] Why are you bringing it back up?

**Adam Staravia:** It always bites me. I mean, I don't mind... That's cool. But I think if -- I really don't mind; I like being wrong, honestly. I love being wrong when it's right to be right, I suppose... Because I think if we do this right, it could be a cool, fun thing for the community, and it could be a good revenue driver for us. And it'd be kind of cool to put that infra behind that. The frontend, the backend, all the things that we've been building... It would just be kind of easy to extend what we're already doing well.

**Jerold Santo:** Yeah.

**Adam Staravia:** So that's my...

**Gerhard Lazy:** One thing which I would like to add to this - because it does connect. I was exchanging some DMs with someone from our community. Her name is Mary Hightower. And I'll just read the one sentence which is very relevant to this. This was end of November, so a few months back. "One thing", and I'm quoting Mary. "One thing I've seen in the Changelog crowd is the perspective of how to build software in teams well." I think that's something important, because it is in Changelog's DNA to care about those things. And it's not me saying this, it's someone that has been in our community, and I'm sure that others must feel similar to this. Because there is a perspective on "What does it mean to be a good team? What does it mean to have a successful community, a successful relationship?" And coming back, Changelog & Friends. Look at us, what we're doing now. How open we are, how we're trying to support those that maybe are less fortunate than us when it comes to their work environment.

**Jerold Santo:** Yeah. Well said. I think that's on point, and entirely irrelevant... And the reason why something like this - which to me has always seemed like potentially a bolt-on - could actually be very integral, and valuable, if we execute it right... Which is always for us strengths and weaknesses; our strength is our weakness. We know that perfection is the enemy of progress, and progress over perfection... And that's why we Kaiden, and that's why we do MVPs, and all these kinds of things... Because Adam and I both desire the perfection, and sometimes we just don't build the thing, because we're like "Well, we can't figure out how to do it perfect, or even well, and so we're not going to do it right now."

**Gerhard Lazy:** Yeah.

**Jerold Santo:** Hopefully, we can eschew that, and get a jobs' thing going in order to provide that value, and to sustain shows like Go Time... And really, our entire network, when advertising wanes. So to me, it's feeling less and less like a bolt-on moneymaker, and more like true value for all of us. So I'm into it, whereas in the past I've kind of poo-pooed it. So I've had a change of tone.

**Adam Staravia:** Same. Me too. That's why it was so cathartic that we would actually go back to it, or that it would become an idea again, I suppose... Like, how in the world does that even make sense? ...and somehow it does make sense, now that that's even something we're promoting, or suggesting... And it has always seemed like a bolt-on that didn't really provide the value. It always seemed like "Well, this would only be so that we can find one more way to sustain."

**Jerold Santo:** Right.

**Adam Staravia:** \[18:06\] Whereas now I feel like if we can embed them into the shows, in the ways we think we can, and swap them out when necessary dynamically, then I think that's a big win for us and a big win for the folks trying to find the right folks. And I think if we could do a good job on vetting who comes into that pool, and just some way to provide - like you were saying, Gerhard, quoting Mary Hightower... Hi Mary, by the way... You know, I think that's great. Building great software, building great teams I think has always been the fun part of the conversations. We've just had that conversation with Dan more on Letters to Developers. Such a cool conversation, the first show out of the gate this year... And I think it's going to be a big hit for the year, and it's show number one for 2024.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** So Adam shared two, therefore I will share zero...

**Gerhard Lazy:** Three. \[laughs\]

**Jerold Santo:** Yeah. One, two, three. No, he stole mine. So Changelog Plus 2.0 was exactly what I was going to say.

**Adam Staravia:** Sorry, Jerold.

**Jerold Santo:** No, it's alright.

**Gerhard Lazy:** You're doubling down. It's definitely going to happen.

**Jerold Santo:** We're on the same page. That's a good thing. We should have similar goals, shouldn't we? Yeah, bringing Changelog Plus on-site, in our control, and making it way better... We have lots of ideas, and we've kind of been inching towards that. We haven't gone all-in on it, because there's always been one more thing that pops up that's more important... For instance, even our big conversation today about Postgres is a thing that is currently just more important than that... Although you're doing the bulk of the lifting on that. There are other things that are popping up, which I'm sure we'll be talking about soon, which are more time-sensitive than that... And so it kind of always gets pushed off.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** And I just want to stop pushing it off and actually get it done... Because a) we've had more subscribers recently. So thank you to all of you who joined...

**Adam Staravia:** Yes. Big time.

**Jerold Santo:** It's been very uplifting to see so many people joining on, even in its current state, which we know is not as good as it could be... And 90% of the people are there just to support us, and we love that. But we also want to quid pro quo that, and provide value back, and make it awesome. So it's been a thing that I think I even wanted to do last year, and just didn't do it... So it's like, enough is enough. Let's do this, and let's do it well. And not perfect, because then it'll never ship. But ship something, and do the bulk of the work, and then refine from there. So that's my goal.

**Gerhard Lazy:** That's a good one. That's a good one.

**Break:** \[20:33\]

**Gerhard Lazy:** Okay, well, my next goal is to encourage you to open up GitHub discussions 485. It's in the changelog.com repository... Because the bulk of this conversation is going to happen around that. And if you're listening, you can go there; by then it should have been done, but you can see all the topics, all the links... Everything's there.

**Adam Staravia:** Links in the show notes too, by the way.

**Gerhard Lazy:** I think the biggest thing for us - and we mentioned this a couple of times - it is pull request 492, where we are migrating Postgres to Neon.tech. So that's the big thing. And it's the biggest change I think that we had since Kaiden 12, is to set up Neon.tech as a managed Postgres alternative to our current Postgres, which is running on Fly.io. Let's open up this pull request, and let's take a look at it and just load some of the context.

**Jerold Santo:** Let's do it.

**Gerhard Lazy:** So when I started this, the first thing which I did - and this is almost like the Boy Scout rule - update dependencies. And I know that we should have bots that do this automatically, but sometimes, especially when it comes to the major versions, you would want to do that yourself. For example, Erlang -that was an okay, 25 to 26, that upgrade. Postgres - this was like a bigger one, from 15 to 16. Nothing changed, so it was still good, but those types of upgrades you would want to supervise. You wouldn't just want like a bot to do it for you, and then you figure out "Oh, there's all these things which I've missed."

And to be honest, end of the years are perfect for these big upgrades. So that's like 490, which is a precursor to this pull request. We can come back to the Elixir upgrade, because by the way, that's the one thing which didn't work very smoothly, but we can come back to that later, and just focus on this one.

So we have a new app instance, as we discussed, the 2023 12.17, which is running on Fly, and that is configured to use Postgres. So Adam is the one that set up Postgres for us. How was that, Adam? How was the whole initial setup of Postgres?

**Adam Staravia:** You mean Neon?

**Gerhard Lazy:** Yup. On Neon.

**Adam Staravia:** It was actually pretty easy. Barely an inconvenience, for my \[unintelligible 00:26:21.03\] Screen Fan lovers out there... It was pretty easy. I mean, I think I just went in there -- the only confusing thing was there wasn't the idea of orgs. You create a project, and inside that project you invite people. So that was kind of, I guess, the only oddity. I mean, I did nothing besides -- you're giving me way too much credit, honestly. I just talked to the folks; the folks behind Neon are amazing.

**Gerhard Lazy:** You started it. Without that, this would not have been possible. So...

**Adam Staravia:** Well, if you want me to give you the real getting started story, it began at All Things Open, really. Their CTO was there, and their team was there, Ralph and others were there, and I was like "Jerold, we should just go over there and talk to them, because we want to have a managed Postgres. Gerhard's been pushing for this..." And my first -- you know, you might want things, Gerhard, but then I go and ask Jerold "Do you also want this? Do you bless this?" Because Jerold really is our CTO, really. And so I would never make a tech choice without conferring with both of you guys that that's what we should do.

**Gerhard Lazy:** Yeah.

**Adam Staravia:** So I asked Jerold, and he's like "Yeah, that works. Let's do that." And so I went over, and we ended up getting them on the pod, and we talked further, and then we talked further afterwards... And I just laid it out, like "Hey, we love Fly. Big love to Fly. But we want something that's future-focused." And I think in my discussions with Kurt Mickey, who is the co-founder and CEO of Fly.io, he was always like "We have different ambitions, and databases are part of it, but we know we're not providing the state of the art thing. It's good, it's good for everybody, but this isn't something that we're sort of like laying further into." Now, that may have changed in that year and a half ago conversation... But I was always like, I know, after our conversation, after Jerold and I's conversation with Nikita Shamgunov, the CEO of Neon, I think about a year back... Right, Jerold?

**Jerold Santo:** Yup.

**Adam Staravia:** \[28:09\] About a year and some back now... That he really laid out a lot of good promise. And he had experience in databases before. He had been previously successful around databases with Teacake, I believe... I forget what -- SQL cache, or I forget what his previous startup was that was acquired... But he had had some success. And he impressed us in that podcast about where they're taking Postgres... In particular serverless managed Postgres, and then the idea of maybe getting \[unintelligible 00:28:34.09\] which they're not quite there yet... And then I think what really impressed me recently talking to them was around the way that they plan to bolt in bringing this dev mode to Neon and Postgres, really where you're -- and you all can probably speak to this more than I can, but the way you interact with the database is one in production, but then also in dev. And so to innovate and to experiment with a database at the dev level always requires some sort of cloning of the production database, and this weird flow. And they've made it a way, because it's serverless and because it's sort of ephemeral, to allow you to just branch off the database.

This isn't a new concept necessarily for databases. I think -- who's it out there? Gosh, their other name... It's the SQL one. The MySQL one.

**Gerhard Lazy:** Planet Scale?

**Adam Staravia:** Planet Scale. Yes, thank you. I think Planet Scale really began a lot of this branching idea with the tests, and whatnot... So it's not a new concept, but it's a new concept to Postgres. They have upstream commits, they have a lot of promise. And so we're really enjoying the process of where Neon can go. So that's sort of the precursor backstory.

Well then, All Things Open, talked to them, talked about partnerships and stuff like that, and they're like "Let's do it." And so they gave me the keys, I went in, I opened up the project, and I invited Gerhard. That's what I did to kickoff Neon, for the long story short. But it really began a year or so ago, the idea of Neon being something that we can use. And just knowing we like to play with cool things, managed serverless Postgres is something we should be playing with. And now we are.

**Gerhard Lazy:** Yeah. So I'm very curious to see what Jerold thinks about connecting to a branch for his local development. Would you do that? Do you see yourself doing that?

**Jerold Santo:** Absolutely. Is that weird for you? Do you expect me to say no?

**Gerhard Lazy:** No. I mean, do you see yourself --

**Jerold Santo:** Well, generally I'm a naysayer. \[laughs\]

**Gerhard Lazy:** Yeah, you are. Also, it's not local, so it's going to be slower, and you'll need an internet connection, and all of that...

**Jerold Santo:** I agree, it will be. Not slower like Docker for Mac slower, which for me was a long time naysayer, like "No, I'm not going to run my developer environment through Docker. I already have it set up." I mean, that's years-long thing, with "How should people contribute? Let's set up Docker containers. Jerold won't use it, so it's not going to be good", that whole deal...

**Gerhard Lazy:** That's right.

**Jerold Santo:** I'm way less concerned about some slower query times in development, because I have a recurring pain with development, where I do like to have fresh data as I'm coding... It's just more realistic, it's more enjoyable. I prefer that. And so I am often doing a Fly proxy, a pg\_dump into my local, and a pg\_restore, or whatever the actual command is, in order to get fresh data. And I'll do that once a week. Every time I'm starting up a new coding session. Sometimes I'll be like "Oh, this is fine. It's last week's data, no big deal." Other times, especially - like there's a bug. Well, the bug often has to do with data that's in production, that's not in development, of course, and so I want freshens... And so I'm just constantly doing that. It's just part of my workflow. I go get a cup of coffee. It's not a very large database \[unintelligible 00:31:40.27\] wait for it... And that's a pain that I live with. But I do want that snapshot to be relatively recent.

Being able to connect to a dev mode which is just a branch of production, that I'm assuming I can either resync, or just do a new snapshot whenever I'd like to, and it just is somewhere else, and I just change my connection string... I don't have to version Postgres locally... And it's one less dependency on my local box.

\[32:08\] I'm here for it. I haven't tried that yet. I haven't used it. Obviously, we are in flight with even doing this... So maybe I'll end up hating it and be like "Nah, I'll just run my local Postgres, and do a snapshot, and everything will be fine." But I'm definitely not nay saying it yet. I'm excited to try it, and I think it's going to be better than what I currently do.

**Gerhard Lazy:** I think that's a really cool idea, because it helps me figure out what else is important part of this pull request, the 492. And my most important take on this was like "Okay, so if we do this, what will this unlock? What will this enable us to do differently or better than we're doing today?" And what you're saying to me sounds like -- that's like a great goal to work towards, because it will simplify things a lot; you don't need Postgres locally.

One other thing - it's almost like a complication to this - what about contributors? What about people that don't have access to our production data, and we will not be able to give them access to production data, even if it's a branch?

**Jerold Santo:** They're currently in the exact same box. Like, they're already there. They live there right now.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** And that's one of my pains. People are like "I'd love to contribute." "Cool. Go clone the repo and check the contributing guide." And they're like "Awesome! Can I have some data that's like real?" Because they don't even have like podcasts when they're -- you know... And we had seed data in the past, and it's just like, we are not an open source project like most open source projects, where it's like there are dozens if not hundreds of strangers working together... It's like, we have a flyby contributor once in a while, and we want to enable them, but oftentimes that person who comes maybe once every few months are not worth maintaining seed information. I had a long -- like, my to-do list, at the bottom of it is "Find a way of just taking production and sanitizing it, and reducing it down to what they could use, and provide that for people." And I don't have it done. I don't have answers for them. I'm like "Yeah, you can just do it without data. It's no big deal, hopefully..."

One guy was working on the player, which -- he couldn't play a mp3, so he couldn't actually do... I can't remember what he was trying to do. And I'm like "Well, it's going to take me hours to get you going." So that's where we already are, so we aren't losing anything. We're not solving that problem, though, it sounds like. Yeah. Maybe we are. Maybe there's a way you can provide them a sanitized branch, you know?

**Gerhard Lazy:** Yeah. I think this is where Neon -- it'll be a great conversation with Neon to see "Okay, so when we do create a branch, can we add some extra stuff that runs part of that branch, so it puts it in a state which is okay to share?" And then we can automate that in some way, so that whenever someone wants to contribute, they basically connect to the latest one, and they don't have to do anything, because the connection string doesn't change... And what we make available -- so that'd be an interesting one.

**Jerold Santo:** And I kind of got that far. I'll have to go back and find it, but I do have at least the start of like "What is the series of SQL commands I would run to take production and sanitize it, and reduce it to useful, but not real?" And I started like writing some deletes, and stuff. I probably have that somewhere, but I never actually got to a place where I could then -- it was all ad hoc, like "Okay, I'm going to go get a snapshot, I'm going to delete stuff, and I'm going to give you the SQL file via Dropbox, or something lame", right? So this could be cool in that way, maybe.

**Gerhard Lazy:** Yeah. So that sounds like a step four; we're still this step zero. We're still migrating towards it, in that the pull request is open... And one of the first observations was that the latency increased. And if you think about it, it makes sense, because with Fly, Postgres was local, so we get sub-millisecond latency. In Neon's case, the Postgres is remote; it's running in AWS. Still the same region, but it adds a couple of milliseconds. And when you have lots of queries, which we do on some pages, they add up.

\[35:55\] So for example, when we started this, the homepage latency just shot up by 3x, and Jerold, you came \[unintelligible 00:36:01.25\] and reduced the number of select statements; we had 70 plus, now we have 15... So while it was 3x before, now it's like maybe 10%, which is 0.1. So that's a huge, huge improvement. So how do we feel about knowing that the latency of all our database queries will increase? Are we okay with that?

**Jerold Santo:** Yes, because we are leveraging cached information most time.

**Gerhard Lazy:** Okay.

**Jerold Santo:** And also, I can now be more diligent as well. So a lot of the reason was I never had a good enough reason to go optimize that particular page... And then I did, and I spent an hour or two, and now it went from 70 to 15 queries. And I could do that on other things as well. I know you posted /feed is also super-slow. 477 selects, I think, which is too many for anything... But that page is never live; it's always precomputed. And so -- I mean, when you hit it on Fly directly, of course, it's going to hit. But when you hit it through changelog.com, it's going to a precomputed XML file that's on R2. So we've already kind of solved for that in other ways...

And we can use Honeycomb, and know when stuff gets slow, and then we go optimize it, just like the developers do. So I'm not really concerned with that. I think it sucks having network latency when you don't need it. We could avoid it with this other thing... But I think the wins outweigh the drawbacks. What do you think, Gerhard?

**Adam Staravia:** Is there a way to reduce it natively? Like you said, they're in the same region. Is there a way that, from an infra standpoint, we can put them closer, even though they're different networks? Like, how can we get them "closer", to not have that much latency?

**Gerhard Lazy:** So there's nothing this team can do to improve that, because we are already in the Fly region, which is closest to the Neon region... So we can't basically pick another region, either on Fly or on Neon. Maybe there are some improvements that Neon or Fly can do, but it's the speed of light. That's what we're working against here. So let's say we make it to like a millisecond quicker; it will not have the same impact as for example if we optimize some of the queries, so we don't have to run 400 plus. If we could reduce those, that would help. I think those are the biggest wins, or the bigger wins that we should be looking at, rather than physically getting these two things closer.

**Adam Staravia:** Yeah.

**Jerold Santo:** But are you saying that our Fly machines -- so we had a Fly instance, multiple Fly instances that are running app servers, and we had one Fly instance that was running Postgres... And are you saying that those did not have network latency between them? Are you saying now there's more network latency?

**Gerhard Lazy:** They have a much lower network latency. So we have --

**Jerold Santo:** They're still traversing the network stack though, right? Like, they're not collocated on the same machine.

**Gerhard Lazy:** Correct. But he doesn't leave the Fly network. So it's all happening within the Fly network. And we have two Postgres instances, a primary and a replica. This is on Fly. And we have the same setup on Neon. We have the primary, it's called the read-write instance, and we have a read-only, which is a replica. And the next point is maybe we should look into that. Maybe we should configure to use read replicas. But before we talk about that - again, same setup in Neon as we have in Fly; the difference is that the physical distance is greater, and there's more network hops. And when I say network hops, some of them are invisible, because you don't see all network hops that happen. But anyway, we're just basically adding one, maybe one and a half millisecond latency... And again, these aren't always the same; they're variable. But basically, we're adding more latency to every single SQL statement per query, exactly, and they just add up. The more you have, you're basically paying the network latency penalty for each of those queries, rather than having one query that you know does more, and then it comes back with all the results. It goes back and forth, back and forth.

**Jerold Santo:** Right. And is there any sort of like connection pooling, or other things we could do in order to reduce that per-query cost? We have all that set up.

**Gerhard Lazy:** \[40:13\] We do have that. It's literally -- you run one, you have to wait for the response, you run another one... And some of them do run in parallel, but eventually, you've run all these things, and all the responses have to come back for it to be able to rebuild the page. While if you use fewer request responses, it will be quicker.

**Jerold Santo:** Just the law of math and physics. Doing less costs less than doing more.

**Gerhard Lazy:** Yeah, pretty much... But again, it's the light of speed. That's what we're dealing with here. Physical distances... And we're doing many round trips back and forth.

**Jerold Santo:** Well, then let's work on that, Gerhard. What can we do about that? Let's Kaiden speed of light. Can we slowly make that faster, iteratively? \[laugh\]

**Gerhard Lazy:** Um, I don't think in my lifetime, but... \[laughs\] I don't want to say never, but...

**Jerold Santo:** What about by 60? This could be your next 20-year project. \[laughs\]

**Gerhard Lazy:** Maybe, maybe. A shorter project would be to look at the read replicas. I think they would help. So having some read replicas, and having some -- I'm not sure within the same region, but distribute them a little bit... Because Fly - I mean, we have this option of distributing our app, and we haven't used it. We're still in a single region. And we haven't used it because we haven't configured read replicas yet. If we had a read replica in every single location, this would be a lot more interesting. So what do you think about read replicas in the context of our Phoenix app, Jerold?

**Jerold Santo:** I think it's interesting. I wouldn't put it like high priority, just because of the obvious reason that most requests are never hitting our app, you know?

**Gerhard Lazy:** You say that...

**Jerold Santo:** I do... They shouldn't... \[laughs\]

**Gerhard Lazy:** But remember the issue with Fly? Sorry, not Fly. Vastly. Oh, my goodness me. I was leaving that towards later, because that's not a fun one... But we'll dig into it.

**Jerold Santo:** That's bad again?

**Gerhard Lazy:** Well, it's been bad since October, and we can't seem to get anywhere with the Vastly support, that one. So our hit ratio, it really tanked.

**Jerold Santo:** It's way down.

**Gerhard Lazy:** Exactly. And we've been trying to figure this out with Vastly, what is going on, and we can't get a clear answer.

**Jerold Santo:** No changes on our end that we can identify.

**Gerhard Lazy:** No changes on our end, no.

**Adam Staravia:** Can you zoom out a bit and give a one-minute version of that problem, and exactly what's happening, so there's context?

**Gerhard Lazy:** Okay, so let's talk about that.

**Jerold Santo:** He's excited, you can tell, to talk about this... \[laughs\]

**Gerhard Lazy:** Yeah, I'm prepared for this. This burned a lot of my budget that I have for Changelog. That's why this hurt. This burned almost like a whole month of work budgets this whole Vastly CDN thing. It was really that bad. And there is an issue, it's issue 486; it's a long one. If you open it up to see just how much we talked... And James A. Rosen was there, so thank you, James, for helping out... It's honestly -- like, it will take you at least 30 minutes to read it. So can you imagine how long it took? And this is only the public stuff. There's also something even longer, which is the whole Vastly support thread, that I wouldn't even want to open.

But anyway, October 8th. This is when it started. Our CDN cache misses increased by 7x. So we had about 750,000 cache misses in a two-week period. And after October 8th, we had 5 million cache misses. That's a crazy amount of number.

Now, this has improved since... So we didn't do anything. December 28th, we are now at 900,000. Now, obviously, requests go up and down, but we still have more than we should do. Most of these requests are to the homepage. 80% of them are HTTP/1, 19% are HTTP/2, and only 1% are HTTP/3. 75% of all text HTML requests are cache misses. So this is like highly makeable content, that there shouldn't be any misses, and we get no explanation for why this just started happening. I got so frustrated that I want to build my CDN...

**Jerold Santo:** \[44:19\] Hah!

**Gerhard Lazy:** That's not the 20 years project. So yeah, so three years ago, Kurt posted about this. He wrote "The five-hour CDN" on the Fly.io blog.

**Adam Staravia:** I recall something about this... I think on a Kaiden, briefly.

**Gerhard Lazy:** Yeah. And actually, it wouldn't be that difficult, honestly. That would be easier to do than deal with all the Vastly issues. That's where I'm at now. And this has been years. This is not the first time, by the way. This is a long, long, long story. I'm using a similar approach. I have something like this configured in my Kubernetes clusters; I have quite a few, NGINX caches everything, I have origins configured, and it works. And you can serve stale content... It's not rocket science, but at least we'd have full control over. So what I'm thinking is let's deploy some NGINX instances all over the world using Fly, let's serve all requests from those. They'll have some local disks, we cache all requests there... Problem solved. We're done. That's it.

**Jerold Santo:** Worth a try.

**Gerhard Lazy:** And I'm thinking cdn.gerhard.io. \[laughter\] I even have a name for it. Not a logo yet, but I can ask ChatGPT to create me one... What do you think about that?

**Adam Staravia:** Well, I don't know what it takes to build a CDN. I think in the conversation, one of it is streaming logs; that is how we have built around. And the question was whether if Cloudflare had that similar support. Because the obvious answer here would be "Okay, if we're having challenges with Vastly--" And they're aware of this stuff; we've brought it to their attention that we have had challenges.

**Gerhard Lazy:** Multiple times.

**Adam Staravia:** And it's strange to me, because we obviously have such -- it's not like we're here trying to badmouth anybody, but we do have a mouthpiece to the developer community, and we're using the technology to showcase... The technology. So it would make sense, in my opinion, if you had that kind of relationship, with such a content -- I guess media company is probably a better way to say it, that you would want to put some effort into ensuring that they get the right help, to ensure that these problems aren't there. And maybe it's just a Vastly thing, maybe it's an US thing... I don't think it is, because we've seemed to have exhausted every single possible thing we could do around it... And so the obvious next choice would be "Okay, maybe we're just -- we're not holding it wrong, it's just we can't hold it right. And we can't figure it out, because there's no support to hold it right." And so we go and talk to Cloudflare, we decide to build our own thing... And I think it really comes around what does it really take to build a CDN for the kind of company we have, and the kind of content we have that we need to cache, globally. Does it make sense to build something in-house? Does it make sense to move to the next key player in the industry, which is Cloudflare? They've shown desire to work with us, we're talking with them... It's not come to full fruition, but there's a lot of desire. But I don't like to bet on desire necessarily, so I don't want to say there's something happening there... But it's definitely on the table to talk about, and they're talking with us, we just haven't landed the plane of the deal.

And I think for us, we look at infrastructure partners like this, like Honeycomb, like Vastly has been, like Linde has been in the past; like Fly is, like Type Sense is... Are we want integrated, embedded partners? Not because that's what we necessarily want, but because we see that's what they get the best benefit of. We get the best benefit, because we get to have that deep relationship, and that conversation back and forth to improve. And I'm sure if Neon succeeds with us, and we fully migrate our Postgres there, and we're super-happy with all the things we've been sort of talking about, that there's going to be a deep embedded relationship.

\[47:55\] I've kind of come up with this idea over the holidays, this embedded sponsorship. It's different from just sort of flying by and throwing some money at content, and hoping that you can talk to their audience. It's far more of a partnership in embedded, and so that's why I go that route. And I think Cloudflare has an opportunity to work with us, if that works out. We've given Vastly years to work that out, and they haven't done it. And that's just a shame. I really would love to have them figure that out. I've begged them in email, in conversations. And I don't mind saying that, because I've worked it personally to the Nth degree that I'm kind of sad and upset that that's where we're at. They are amazing, maybe not amazing for us... But we've just not gotten the kind of support we need to get past these challenges, over and over and over.

So I guess my question to you is, does it make sense for us to build our own CDN? Was does it really take? Should a small operation like ours try to do that? Or does it make sense to go to the Goliaths and the behemoths like Cloudflare and Vastly, like we have done? Should we try something different? What should we do?

**Gerhard Lazy:** One thing which I want to mention here - and this is really important - is that if we didn't have Fly, and if we didn't have the partnership that we have with Fly, I wouldn't be suggesting this. So that's the first thing. The second thing is, as crazy as this idea was three years ago when Kurt laid it out, having sat on it for years, and understanding what we need... We're not that complicated from a technological perspective. Our app isn't that complicated. And it's not changing that much. We're not a big team. And that means that our needs are fairly simple and straightforward, which means that some of the big companies - they can't really meet them, because they're too big. There's too much there. There are a lot of complications, and 99% of the stuff we don't even care about. We don't care whether it's Varnish, we don't care whether it's NGINX, we just care about the experience, and the experience is too complicated. So I'm sure there's a way that we can make this work, but is it worth our time? And the answer is no. That's what I keep coming back to. What we need is something really simple. And we don't have that really simple thing.

Even our config, what we need in terms of streaming logs - it's such a simple feature that we require. And yes, sure, we can go and start the conversation with someone else, not just - back to Jerold's point, it would take a few hours to explain to someone or to do something for someone, what he could do himself in like 5 or 10 minutes. That's like an equivalent there to what we would need. And it's really not that complicated... And we're leveraging someone like Fly, which have come light-years in the last three years. They're like light-years apart where they were as an organization, as like the services they offer...

**Adam Staravia:** Can you gush a bit about that light-year change just real quick? I mean, they are a partner, they're not sponsoring this message I'm asking you to say... But can you gush a little tiny bit about their improvements? Because that is the home of changelog.com. I almost said thechangelog.com, Jerold, accidentally... You know, Fly is the home of changelog.com.

**Gerhard Lazy:** Let me change this question. Since we went from Kubernetes to Fly.io, how many shoes did we have because of Fly.io? Was Postgres a problem for us on Fly? Not really...

**Adam Staravia:** No.

**Gerhard Lazy:** I mean, we had some issues, like minor issues, but nothing big. Nothing of the scale of Vastly. How many times have we reached out to support and they couldn't help us?

**Adam Staravia:** \[unintelligible 00:51:28.18\]

**Gerhard Lazy:** Exactly, Fly. There you go. From a technological perspective, the machines, the way they work, the deployments - I mean, they just work for us. They just kind of meet our needs exactly where they are. And things are fairly fast... It's very easy to spin up new apps. I know that not everyone has this amazing experience with Fly, but we've served billions of requests in the last two years, and we're still good. We didn't have anything big, or anything bad to say about them.

I mean, I can talk, for example, why our Dagger on Fly has been failing, and there are some problems with the WireGuard... I mean, it's not all great, and we can talk about that. But that's a very specific use of Fly, in a very specific context.

**Adam Staravia:** \[52:17\] And it's not their core competency, necessarily. Their core competency is what they provide to us. It's the edges where they're sort of moving and innovating that still need work, which is par for the course.

**Gerhard Lazy:** Yeah. So - I mean, this basically has to do with the Fly -- there's intermittent Fly.WireGuard gateway issues when you're connecting, for example, from CI, from GitHub in this case. Sometimes that whole setup -- and it's very difficult to say whether it's Fly or whether it's GitHub, or Microsoft Azure where this runs. So it's difficult to say what exactly is happening, \[unintelligible 00:52:49.00\] that specific combination isn't working well. But because we have to have everything, it's okay, because we've been falling back to the GitHub runners. Builds have been a bit slower, but they worked. Deploys, were taking ten minutes, rather than --

**Jerold Santo:** And I get the GitHub Action run failed emails when my deployment goes out successfully, and I'm like...

**Gerhard Lazy:** So I just want to balance this out, in that we have had some issues with the Fly, but not in the path that we really care about. Production hasn't been down because of them... Again, knock on wood that it doesn't happen, but it's been good. Now, should we put all our eggs in one basket? You know, two of everything. If we run everything on Fly and Fly goes down...

**Adam Staravia:** We're down.

**Gerhard Lazy:** Yeah.

**Adam Staravia:** Let me ask you a different question then. So if we did decide to build our own CDN - like, this is one more thing for a small team like ours to maintain uptime, too. Like, what would we be taking on in terms of burden? It's one thing that we don't have the need for, let's just say 99%, like you'd said, of a Cloudflare or a Vastly feature set; we really only need the good 1%, because our needs are just limited, and we don't have exhaustive needs... And we did decide, okay, let's build our own CDN. Again, eggs in one basket; we're going to build it on Fly if we decide to do that. But what would it be in terms of build time, burden to maintain, if it's down...? How do we -- I mean, it seems like we'd have to probably have more of your time... I mean, I don't know; it just seems like we're taking on way more responsibility, because Vastly is in front of everything. And while there are some challenges there, and there are some misses of recent, we're relying on them to do their job, and they kind of do their job for the most part. We've had some issues, obviously, but we wouldn't be taking all that on ourselves. Does that make sense?

**Gerhard Lazy:** So let's break it down in terms of the big pieces that we need to get into place. We have one new application, which is our CDN application. All of that is NGINX, exactly as it's described in Kurt's blog. We have an NGINX config that has all the rules that currently we are defining in Vastly. We distribute this app across all the Fly regions; maybe not all-all of them, but most of them. So a couple like US West, US Central, US East, South Americas, a few in Europe... And all this is like literally run a few commands in Fly and you have all these app instances spun up. They're the same config, same everywhere... We get one dedicated IP; it's an Any cast IP. Again, a Fly feature. So regardless where you are, you use the same IP. That would be cdn.changelog.com; it will hit one of those Fly instances. If the instance is down, I think the way it works - the Fly proxy, which you're basically hitting the proxy on any of the edge, again, where you are - it will redirect to the running instance.

And then you have some very small rules, which basically tell you what do you do. So let's say that you're serving a mp3. If you don't have the mp3, it will stream it from wherever it is, and it will cache it locally. So you have some disks attached to every single NGINX instance, so that you have like a local ephemeral cache of all the content that's requested in that region. It's just a simple config; you just add the volume - boom, you're done. That's it. I mean, there's not much more -- I suppose it's like the config for the NGINX, so that Jerold gets the logs.

**Adam Staravia:** \[56:19\] That can't be it. What about logs, and stuff like that? What about the things we need for stats, and the application...?

**Gerhard Lazy:** Logs, exactly. Yeah. So NGINX logs; we'll get them in the form that we need to, we'll write them to a disk... I mean, Fly has NATO. That's how they distribute all the logs. I know that's not always reliable. There are small issues, and I know because I've been using this for another project for like the past year... This is for Dagger, by the way, so I know exactly how NATO works, how log distribution works in Fly... And the challenge would be to get those logs reliably from the NGINX instances to S3. I think that's the one thing which is like an unknown, in the sense that I know the limitations of NATO, which is internal to Fly. But maybe there's something more that we can do there. We cannot do this without a little bit of Fly's help. And what I mean by that - we wouldn't want our logs to get lost, right? Vastly has been very reliable as far as I know when it comes to delivering those logs. I know that we can get them in the right format, because NGINX is super-configurable. What I don't know is how reliable will it be to get those logs from Fly into S3.

One tool that I've used, and I love is called vector.dev. It's an open source tool, very lightweight, written in Rust, that consumes - they're called inputs. So it can be anything from like a log file, to STDIN, STDOUT, whatever. It has a couple of sources, and then it does transformations, and it has syncs. So we could collocate some of those vector instances right next to NGINX. They are super-lightweight; think megabytes of memory usage, hardly any CPU usage... And they could distribute those logs reliably. They have backup mechanisms, they have all sorts of things. So even that, I would have an idea of how to do. Time-wise, we're talking days of my time.

**Adam Staravia:** Hm. Preach. I like it.

**Gerhard Lazy:** So I think by the next Kaiden, if I set myself to do this, this would be done by the next Kaiden.

**Jerold Santo:** What about costs? I mean, we would have to compare apples to apples of Vastly pricing versus Fly pricing. It looks like it's about 0.02 cents per gigabyte. Mostly I'm worried about outbound data transfer. 100 gigabytes per month free - that's North America and Europe - and two cents per gigabyte outbound data transfer. So I think we would do some sort of analysis of what we are doing currently on Vastly, and what that would cost with our own CDN on Fly... And that'd be interesting to compare.

**Gerhard Lazy:** Yeah. So if we did -- let's go five cents per gigabyte. We would still be within our sponsorship account, because Fly sponsors our infra. We would not exceed our sponsorship limit. Oh, sorry... No, hang on. I may be wrong. Hang on, hang on, hang on... Times this; I have an extra time. Um, maybe it would be slightly over. Slightly over. But then we -- I mean, we have a bunch of redundant infra that we can shut off. Maybe we can increase the sponsorship a little bit, or Fly can increase the sponsorship little bit.

**Adam Staravia:** Right. We can always go back to them with a new cause and idea to say... I had an idea, I suppose; and this may not fly...

**Gerhard Lazy:** \[laughs\]

**Adam Staravia:** \[59:44\] But I was thinking like the idea of really simple syndication. What if it was a really simple CDN, like \[unintelligible 00:59:47.21\] Like a repo we started up, where you could do the same thing we're going to do if we decided to do this, and it became a template, via open source, as it works... Call it \[unintelligible 00:59:59.26\] and it's meant to run on Fly, and you can spin up your own really simple CDN, essentially, and kind of follow our blueprint. And I think that that's promotion for Fly. That's obviously promotion for open source, Gooding, in a way... Because that's what we're asking for, is just a really simple CDN. Don't give us all the extras.

**Gerhard Lazy:** I mean, if we think of it as an experiment to try out, and see how far we can get... Maybe we can invest a little bit of time and see "Will this work?" I mean, we have the blueprint, we have a couple of things which are out there... I think we're relying a lot on NGINX and NGINX caching. As a feature, that's one of the NGINX Plus features, especially managing the cache, and visibility into the cache.

**Jerold Santo:** Or maybe there are other tools that are more CDN-focused and open source. I don't know, Traffic, I know is popular in the cloud-native world as an alternative to NGINX. I don't know the reasons, you probably do... But just as an example of like maybe NGINX isn't necessarily the solution.

**Gerhard Lazy:** Yeah. I'm thinking something battle-hardened, that has been used for this purpose for many, many years, even decades to this point... And there's only really three options. There's Varnish, there's NGINX, or Apache. Apache, I would discount, because again, I don't want to go into that. So it's either Varnish or NGINX. Varnish is a beast.

**Jerold Santo:** Why don't we just export our Varnish config and just import it into our News thing? We've already written the code. I mean, I know VCL now, Gerhard. I know VCL.

**Gerhard Lazy:** That's might just work... Really? \[laughs\] I get lost in those thousands of lines of... Stuff.

**Jerold Santo:** That's what makes me think, like, is this a really simple CDN? Because when I look at our Varnish config on Vastly, I think "It's actually doing more lifting than we think it's doing." But maybe some of that is -- a lot of it is generated based on we turned on a few features, and they boilerplate out some stuff... But when I started thinking about replacing Vastly with anything, I go back to that Varnish config and I realize, "Okay, I do have --" and I have more rules that I would like to deploy as we take Plus on-site, and stuff. It's going to get more. I'm happy to write an NGINX config. I'm already right in VCL. So I'm not against it. I just think, like...

**Gerhard Lazy:** You've used both. Which one do you prefer at this point?

**Jerold Santo:** Well, it's tough, because I've only ever used Varnish through the Vastly admin, and so it's like this weird thing that you're doing, and you're kind of -- you write it directly, but then it exports it to the right place... And you've got to set priorities in order to get the code where you want it to be... And so that's never what I want, right? And I've written NGINX configs the way I want to write them, in Vim, or in Sublime Text. So I like NGINX better just because I've never just gone and like downloaded Varnish and ran it. So it's tough for me to compare. But they're both fine. I mean, I used to know NGINX very well. I haven't run it personally for years... But for me, NGINX configs are pretty straightforward stuff, you know?

**Gerhard Lazy:** Yeah.

**Jerold Santo:** You can still screw it up good. And I will say that ChatGPT led me astray a couple of times on Varnish stuff... It's gotten it right, but also got it wrong a couple of times, where I was like "Nope, that's not how you do it." I had to learn the hard way.

**Adam Staravia:** One plus is that ChatGPT and all the GPTs knows NGINX configs very, very well. So when you're lost, you can be found.

**Gerhard Lazy:** At this point, all I'm trying to say is that there's a lot of frustration that has built up over the years; it doesn't seem to be getting any better... And it's almost like I want to do something about it, and maybe this is not it... I mean, it's close to me; the heart of a hacker... The hacker has to hack.

**Adam Staravia:** The Easy button to me -- I'd love to do some sort of hacking. I think I would love to investigate further really what it would take for us. Because I love to tinker, just like you do. But do we want to hold a CDN forever as our own responsibility? That's not really the business we're trying to be in. I think that we are in the business of partnering with great tech stacks, and great infrastructure partners, and helping them evolve to fit our needs... More so than us trying to tinker. I mean, I would totally tinker with this \[unintelligible 01:04:06.15\] kind of idea, but I think at the end of the day I want a great partner as a business. I want to promote a great partner to a great developer audience, that makes sense for them to try out and use on their own.

\[01:04:19.29\] To me, Cloudflare seems like the winner of what we should try next, unless you investigate and further "sell us" on the idea that this makes sense for us to build and hold ourselves. Because if there are legs there, then that's kind of cool. And maybe that's kind of fun. It would put us more in the Fly basket, which I'm not against, because we can certainly circle back with Kurt and the team there, and showcase our ideas, and they love that; they love the hacker spirit. So I can't imagine we would get turned away with this idea.

I think my primary concern would be going against the grain in terms of infrastructure partners, and then going against the grain of building out a service that we may not actually want to manage ourselves. But I like the idea of the tinker. It would almost be fun to do just for the fun of it, really.

**Jerold Santo:** There's a lamp into this as well that we could deploy, which is that we could leave cdn.changelog.com completely alone. We have two domains on Vastly. And then we have Changelog.com, which is fronting our app servers. And those are two different things inside Vastly. And obviously, one has the bulk of the traffic, and the other one has way less traffic. The feeds are going to be big, but it's not even -- the logs we don't care about as much. The mp3 download logs are the ones that we want. That's the bulk of the traffic; we could leave that alone for now, and tinker with changelog.com, which is really just fronting our app servers anyway, and it has a bunch of logic, like where the feed rewrites are, and go to R2, and... There's lots that you would get done there. But it's probably like 20% of the work that it would be if you took them both on at the same time, \[unintelligible 01:05:53.07\] So you could build kind of a poor man's version of this as a tinkerer, which maybe takes one day for Gerhard, versus three, or something. And we could roll it out and leave CDN alone, and then if it doesn't work, turn it off and go back to what we were doing. So I think that's a way we could do it with way less risk, and probably more fun.

**Gerhard Lazy:** What about Cloudflare, Jerold? Have you looked at the logs?

**Jerold Santo:** Just enough to know that I think that we need the enterprise plan before I can even play with the features... Which is kind of weird to me. And they don't tease them where I would expect, like in the Cloudflare UI. You expect it to be like "Here's a feature you can't use. Hit a button here." But this feature just doesn't exist until you get to the docs. And then you're like "Oh, log push", which seems to be exactly what we need, because it just writes your logs out in real time to R2. That's the feature we need for our analytics... And then I haven't looked at it for rewrite rules and all the other stuff we're doing fancy... You know, how could I recreate the Varnish functionality over in Cloudflare - I haven't got that far yet, because I figured why do it if we're not sure yet. So I'm pretty sure we can get everything done there that we got done in Vastly, I just don't know exactly how, with the log pushes and Enterprise feature, which - we're just on a standard plan right now, and so I can't even...

**Adam Staravia:** I'm sure we can get that bless, like "Hey, just turn that on for us..."

**Jerold Santo:** Yeah, I just can't even look at it. I didn't look at it yet, because you just can't.

**Adam Staravia:** That's been the main hang-up, really... Because - I mean, to zoom way, way back, we wanted to actually run Cloudflare and Vastly side by side. And I think, Jerold - I can't recall; remind me why we did or didn't do that, but we have the idea of doing it... And it came around that we were always unsure of how to do essentially what log push does, which is moved those logs streaming to another service, so that we can consume them and use them for the stats and whatnot.

**Jerold Santo:** Or any blessed way that we could get the data that we need from Cloudflare. The first time we looked at it, which was probably five years ago now, they just didn't even have it. Like, they'd have your dashboard, and they'll show you what you've done, and that was it. Like, you can't say "Yeah, but how many requests to this endpoint did we serve?" They just didn't have that kind of stuff back then. They seem to have that kind of stuff now.

\[01:08:02.04\] There's other stuff called Website Analytics, which is in beta, which has even more granular data... So I think they've been adding that over time. And then the log push service seems to be exactly what we would be after. Maybe there's an even easier way that they have, that's like "This is the Cloudflare way." And I have to ask them that. I haven't asked them. But the question is like "Hey, if I wanted to count downloads to a mp3 endpoint, how would I get that done?" I'm pretty sure most Cloudflare engineers would be like "Oh, here's how you do it." I just haven't asked. And maybe the answer is "You do it with log push." Okay. Well, we don't have that. So that's where that is.

Well, I'll be down tinkering with this personalized Fly CDN, even if it's just for changelog.com, which just fronts our app servers. We don't really care about the data, we don't need to strain the logs... We just need the rewrites to work, so that it gets the feeds from the right place on R2, and... The basics there. And if that works great, and nothing works out with Cloudflare or Vastly, and the costs makes sense, then you just do the other part... Which is going to be harder. But once you've done the easy part, the hard part becomes less hard.

**Gerhard Lazy:** I think it's worth trying a couple of things. I think if Cloudflare will work from a certain perspective, we should definitely try out and see how far we can get. I think this Fly thing has some merit to it, at least trying it out and seeing, again, how far we can get. Maybe we'll come across things that will be blockers, like real blockers. Or Kurt, after he hears this, he says "Hey, you guys are crazy. Don't do it. That was a joke." \[laughter\]

**Jerold Santo:** Yeah. "Actually, I wrote that three years ago, and I do not believe it anymore. Please don't do that."

**Adam Staravia:** Yeah, that's true. "You guys are crazy." Or maybe he's like "You guys are crazy, and I love it!"

**Jerold Santo:** Maybe.

**Gerhard Lazy:** Yeah, let's do it. \[laughs\]

**Break:** \[01:09:49.02\]

**Gerhard Lazy:** To be honest, I think Fly should have a CDN... Because that's one of the first things that are fairly easy to run as a distributed systems worldwide... Because the state is decoupled.

**Jerold Santo:** It's the simplest use case, right?

**Gerhard Lazy:** Yeah. So if Fly invests in something next, I think a CDN should be it. The thing which we haven't talked about, and maybe we should, is Sup abase on Fly.

**Jerold Santo:** Oh, yeah, because that popped up just recently, after we were already starting with Neon. I mean, we wanted to be managed Postgres for a while, and they weren't doing anything about it... And so we're like "Well, let's go talk to Neon." And then... Tell them the rest, Gerhard.

**Gerhard Lazy:** There is a Sup abase Postgres on Fly.io. It's in the Fly docs. I think this was in December 13th, or something like that. Yeah, it was fairly recent. Sup abase partnered with Fly.io to offer fully-managed Postgres database on the Fly.io infrastructure. Low latency. It's just right there in the intro; I think that makes a lot of sense.

So yeah, I think was like bad timing, I suppose, or good timing, depending on how you look at it... I think the Neon -- I really wanted to see that through. But it's interesting to see something like Postgres appearing on Fly as a managed service through partnership... So I'm wondering, maybe a CDN is next. And this is my wishful thinking.

**Jerold Santo:** Yeah, maybe. It's definitely an obvious move... I mean, it's not obvious that they would partner with Sup abase. I think that for me was kind of a pleasant surprise... It makes sense, like "Oh, yeah. This is a great partnership." I think both companies are very impressive, and aligned in that way, and it benefits both... So I thought it was a good idea. Obviously, I felt like it was late to the game, because we had been wanting managed Postgres for a long time on Fly... So much so that we made a different move.

**Gerhard Lazy:** That's right.

**Jerold Santo:** And still interested in maybe trying and comparing the two. Obviously, depending on how tightly Sup abase is integrated into Fly's infrastructure, I expect them to have that advantage in terms of performance. Yeah, maybe that's -- maybe they go out and find a CDN-focused upstart that could integrate into Fly.

**Gerhard Lazy:** If I was to pick a CDN - and I haven't tried them, but I did a bit of research... Key CDN looked interesting. Not because it's based in Switzerland. That has nothing to do with it. But there's that as well. So Key CDN.

**Jerold Santo:** It was real fast for you; they were really close.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** One of your favourite places.

**Gerhard Lazy:** Yeah.

**Jerold Santo:** I haven't shopped CDNs for a long time. I just have been happy for the most part, until October the eighth. \[laughter\]

**Gerhard Lazy:** It's almost like a yearly thing. Like, every year, something like that happens, and then we spend a few days with support, and we get nowhere, end up going in circles and say "You know what - flip the table. I build my own." And then I calm down... \[laughter\]

**Jerold Santo:** And then you're like "I don't really want to build my own..."

**Adam Staravia:** Yes. Yes, we should.

**Jerold Santo:** Here we are, like "Yes, you should, Gerhard."

**Gerhard Lazy:** This is like the third time this thing has happened over the last couple of years, so I think there's something there. And it will happen again, I'm sure. It's just a matter of time.

**Adam Staravia:** I guess, just to layer one more on - thank you, James A. Rosen for helping us out... But to have to reach out to an ex Vastly person, or for them to actually reach out to us, probably with like "Oh my gosh, you guys are feeling so much pain. I just need to step in and help you all", that is just not cool, really.

**Jerold Santo:** That's not great.

**Adam Staravia:** But did you know that for Tercel Postgres is powered by Neon?

**Jerold Santo:** No... Is this an advertisement? \[laughs\]

**Adam Staravia:** No.

**Jerold Santo:** It just sounded like that. "Did you know that Tercel Postgres...?" Is this a product placement?

**Gerhard Lazy:** Where's the jingle?

**Jerold Santo:** Yeah.

**Adam Staravia:** Well, the reason why I say that is because Sup abase is available on Fly, and it just makes sense to say "Well, maybe Neon at some point will be also available on Fly."

**Jerold Santo:** Yeah, that might be to Fly's advantage to do that. Right?

**Adam Staravia:** Right. It makes sense. But at the same time, I've had this back of the head thought that maybe Neon will be acquired by Tercel.

**Jerold Santo:** Yeah. Are they the only database provider on Tercel now, or...?

**Adam Staravia:** Well, Tercel Postgres is Neon. So Postgres on Tercel is Neon. You don't even account... I'm just reading from their docs. I'm not at all advertising. It is not SOC-2 Type 2 compliant. Coming soon. I'm just reading from their docs... But it just makes me think, maybe Neon will be acquired at some point. I don't think so, but it just gave me this feeling, because when I talked to Nikita for these ads spots we did with them - which was sponsored - his perspective was around the JavaScript developer, and you never bet against JavaScript; this idea that he had said. And they're quite embedded... I just wonder if there are fruits that are happening where eventually they might get acquired by them. I don't know.

\[01:20:05.14\] Because Tercel is such an acquisition behemoth these days; they're acquiring a lot of different stuff. Just a thought there... But maybe at the same time we can expect to have a Neon Postgres inside of Fly, where we just basically have the same great features we love, that we're thinking we'll love, with Dev Mode and whatnot, and branching, and copy-on-write, and all the fun stuff they provide... Maybe it's just like "Well, now it's just -- network latency is gone. It's just not there anymore, because it's within the Fly infra." And that's going to be a good thing for us. The good thing is, really, is that we have choice. We have so much choice as developers, and that really is the fun part of it, right?

**Jerold Santo:** There are a lot of choices here. It's almost the paradox of choice.

**Adam Staravia:** Yeah, the paradox of choice in the grand scheme.

**Jerold Santo:** We'll all end up doing nothing again. Like "Yeah, we didn't do anything..."

**Gerhard Lazy:** Build your own. There are 14 choices... \[laughs\] It's not the right one. There'll be 15 choices now. 15 standards. \[laughs\]

**Jerold Santo:** We'll release our open source CDN, and it'll be 15 of them, right?

**Gerhard Lazy:** Yeah. So I kept one more thing as last...

**Jerold Santo:** Alright, one more thing.

**Gerhard Lazy:** This is like an Easter egg. It's not Easter yet, and it won't be Easter next time we record, I don't think... But still. \[laughs\] Part of the pull request 492, I snuck something in that I wanted to have for ages.

**Jerold Santo:** Oh, my goodness. Did I notice it?

**Gerhard Lazy:** I don't know. Let's have a look. This is a test. See if you can notice a feature which I snuck in pull request 492.

**Jerold Santo:** Okay. I've now switched to the file changes tab; I'm gonna just scroll through the file... Is that where I'll find it probably snuck in, is just some sort of file change here?

**Gerhard Lazy:** I think it's actually if you -- if you look at the pull request of the conversation, it's actually the second comment. Actually, it's the comment; the first comment which I made after the description.

**Jerold Santo:** Don't give me all these hints, man...

**Gerhard Lazy:** Yeah, too easy. That was for Adam. You keep looking at the code, Jerold. That's okay. Let's see who gets there first. \[laughs\]

**Adam Staravia:** Is it this video?

**Gerhard Lazy:** No, that's actually a surprise how the autoscaling slider works in Neon, which is very counterintuitive... So I left that gotcha there, and I gave support to their product team about, you know, how that could be improved.

**Adam Staravia:** Is that 1Password?

**Gerhard Lazy:** Yes.

**Adam Staravia:** I'm glad you mentioned that, because I love 1Password... And you're doing more with this -- what's happening here? What's this about?

**Gerhard Lazy:** So in a nutshell, our application needs a single secret now.

**Jerold Santo:** Shh... Don't tell them.

**Gerhard Lazy:** Op\_service\_accounts or \_token. Single secret. And during boot, the application uses the OP, the 1Password CLI, to inject all the secrets that it needs at boot time. So it pulls them down from the 1Password vault when it boots.

**Jerold Santo:** And is that hosted by like 1Password cloud, or where's the vault?

**Gerhard Lazy:** Correct. That's all 1Password cloud, yes.

**Jerold Santo:** Okay. And so we don't have any additional infrastructure for that.

**Gerhard Lazy:** Nothing additional, no.

**Adam Staravia:** Spell it out for us, really detailed, why is this cool? I mean, I think I understand why it's cool, but spell it out.

**Gerhard Lazy:** We have a single secret that gives the app access to all the secrets that it needs, and there's a dedicated vault for that app. What that means is that that secret only allows the app to access just-in-time secrets when it boots. We don't write them anywhere. We could, but we don't. It's all in memory. When the app boots, it has access, boom, it pulls them down. The secrets never leave 1Password apart from loading into the app's memory. We don't configure them in Fly, which is what was happening before. Every single secret the app needs, we configure it in Fly. Remember how we wrote \[unintelligible 01:23:32.09\] Jerold? That's a pain. So that process we no longer have to do anymore. Because if you want to update a secret, you update 1Password, you restart the app, and boom. At boot time, the app picks up the new secret. That's it.

**Jerold Santo:** \[01:23:48.23\] Does 1Password Vault have some sort of webhook or something that they could trigger? Because then you just take step two out, you know? That's what I want.

**Adam Staravia:** Yeah.

**Jerold Santo:** It just lets the app restart itself.

**Adam Staravia:** Like reboot my app when I add a secret, kind of thing?

**Gerhard Lazy:** We've done step one, so please continue being excited for step one, before talking about step two... \[laughter\]

**Jerold Santo:** Don't you love how I'm never satisfied? I'm like "No. Not cool. This would be cooler."

**Gerhard Lazy:** You and every other developer. That's why we keep chaining this. It never gets old.

**Jerold Santo:** It just keeps getting better.

**Gerhard Lazy:** "You know what would be cool? If we improved this." And before you know it...

**Jerold Santo:** Gerhard's like "Can you just appreciate this for a second before you ask for more?" That's cool, Gerhard, I'm loving this. I'm loving this.

**Gerhard Lazy:** And it hasn't even been merged yet. So again, let's merge it first. Let's start using it.

**Jerold Santo:** Let's get it merged. Okay. That's a nice Easter egg.

**Adam Staravia:** Well, he did ask if this covered all the secrets, and you said "It looks correct", so I think that's all we needed to worry about in there. That is kind of cool. So a cooler thing I think is that it's limited. Even if it could somehow leak, it's only the secrets that we store in 1Password for that vault, for the infra, right? So there's a barrier, there's a perimeter to its touchpoint of secrets.

**Gerhard Lazy:** That's it. And if this was leaked - yeah, rotate the server was token, basically; rotate all the secrets in the vault, and we're good. Again, that would be like a step number three, where "Could we automatically rotate all the secrets that were leaked from 1Password?" And that's almost like a 1Password request.

**Adam Staravia:** Yeah. This is where I also say that we're working with 1Password behind the scenes to make this embedded partnership more apparent as well. We were using this tech, we're paying for this tech; we're not promoting it because they're paying us, and we're actually pursuing them to pay us... Not so that I can keep promoting it, but because we love it so much, and we'd love to work with them to share more of this story on the inside, and maybe even have that relationship where we're "Hey, this is how we're using it", and Jerold's response was "Could there be a webhook?" And maybe they're like "Yes, there could be a webhook." It reminds me of this book I read my kids... But anyway. That's cool. So hopefully, we can get a 1Password sponsorship here soon, because of just how we keep using it, and improving it in terms of our infrastructure... That's awesome. I love that. I've been using 1Password since the dawn of time, basically. Furthermore, I just adore it. It's awesome.

**Jerold Santo:** So those Fly secrets then go by the wayside?

**Gerhard Lazy:** Pretty much, yeah. The only secret which we set is this 1Password service token, and then the 1Password CLI loads all the secrets directly from 1Password.

**Jerold Santo:** So when I want to add a new secret - let's say I integrate a new service - I go add it to the 1Password Vault, and then I go restart the app, I push the code that references it, and by the time the thing boots up, it's going to have access to it? That's pretty cool, man. I love it.

**Gerhard Lazy:** Yeah. There's still a file there... There is the env. Op file, where we put what secrets you want. That's part of the pull request.

**Jerold Santo:** Added to there.

**Gerhard Lazy:** Exactly. Because that's what gets it in the environment, in the app's environment just in time, when the app boots.

**Jerold Santo:** Okay. What about dev? Are we still using \[unintelligible 01:26:42.05\] for dev?

**Gerhard Lazy:** Yes. For example, part of this, I have a near.op. And basically, that one I template just in time, which does exactly the same thing... But in this case, I write it locally to my file. I wouldn't need to. I could, for example, run OP every single time, the 1Password, to load them in the env, but I don't do that. But it's an option.

**Jerold Santo:** Say that again in different words.

**Gerhard Lazy:** Right now, if you wanted to use this in dev, you would need to run the command locally, to read the --

**Jerold Santo:** The OP.

**Gerhard Lazy:** Exactly. So to read the env. Op file, and maybe template it, like maybe write it to a disk, or load it in your environments, you'd need to run things through the OP CLI.

**Jerold Santo:** Can I continue to ignore that and just use my \[unintelligible 01:27:29.28\] as I have been? Because my secrets obviously in dev are going to be different from the secrets in prod anyway.

**Gerhard Lazy:** You could, yes.

**Jerold Santo:** What I really want to know is when this gets merged, is my setup going to be \[unintelligible 01:27:40.29\] \[laughs\] Oh, you have no secrets...

**Gerhard Lazy:** No, it shouldn't. Because this just configures it for prod. So whatever you're doing in development --

**Jerold Santo:** This is additional.

**Gerhard Lazy:** Additional, yes.

**Jerold Santo:** Gotcha. I could use it if I wanted to in dev, but I don't have to.

**Gerhard Lazy:** Correct.

**Jerold Santo:** Sweet. Cool. Awesome.

**Adam Staravia:** That's awesome.

**Jerold Santo:** Anything else? I feel like that was the coup de gas... The Easter egg.

**Gerhard Lazy:** That's why I left it last. That was it. \[laughs\]

**Jerold Santo:** \[01:28:06.24\] Awesome.

**Gerhard Lazy:** So my question is do we build a CDN or not? That's what I want to know. \[laughter\] That's like a title... "Let's build a CDN."

**Jerold Santo:** That might be a show title right there.

**Gerhard Lazy:** Yeah, that's the show title... Kaiden!

**Jerold Santo:** "Kaiden. Build a CDN?" \[laughs\] Yeah, I like that. To be determined, I think. Let's tinker. I think that's the answer. Let's tinker.

**Gerhard Lazy:** I like it.

**Jerold Santo:** And we'll talk to you about it again on the next Kaiden.

**Gerhard Lazy:** Yeah. And we're merging the Neon tech. So we're going to take that into production... Okay, so we are all good with the latency, so... All good. There are some issues with the Elixir configuration. I've left a couple of things for the Neon support. I have a support case open, so we're back and forth on that... Furthermore, I have a workaround which works, but the official documentation doesn't work for us. It's the official Neon tech documentation for Elixir configuration; some issues with the SSL, with the SNI... It doesn't work as advertised.

**Adam Staravia:** So we'll be on Neon.tech as of the shipping of this podcast? So when people listen to this we'll be on Neon?

**Gerhard Lazy:** I think so. It depends on when we ship it.

**Jerold Santo:** That's a week from today.

**Gerhard Lazy:** Yeah, a week from today is fine. Yeah.

**Adam Staravia:** So... If you're listening to this, go to Changelog.com and see if things are snappy, or if the latency upsets you.

**Jerold Santo:** See if it loads. \[laughs\]

**Gerhard Lazy:** It's still Vastly in front, so... By the way, Vastly will be serving your request, most likely.

**Jerold Santo:** Sign into the website and we'll give you a cookie. And if you have that cookie, Vastly just passes through to the apps, and you'll enjoy slower response times, because you're going to be hitting Neon... \[laughter\] But we hope you enjoy that cookie.

**Adam Staravia:** An easy way to do this for free, right? Just go to Changelog.com/community.

**Jerold Santo:** That's right.

**Adam Staravia:** And hey, while you're doing that, come and say hi in Slack, because we want to say hello to you. Lots of cool people in there, lots of good conversation... Home lab's been active, TV and Movies has been active... A lot of -- I think you've got your Wordle channel still yet, Jerold; I'm tracking that...

**Jerold Santo:** Oh, we picked up some Wordless thanks to State of the 'log. We've got a few new Wordless. Still going strong... I'm still keeping my streak alive, so...

**Adam Staravia:** A lot of fun. Alright, you all... Bye, friends.

**Jerold Santo:** Bye, friends.

**Adam Staravia:** Kaiden!

**Jerold Santo:** Kaiden!

**Gerhard Lazy:** Kaiden!
