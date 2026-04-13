**Jerold Santo:** Hello, party people, and welcome back! It's JS Party time. Once again, we have an awesome panel, as we like to do every single week. I'm Jerold, I'm here, I'm joined by three amazing people. Let's start with Divya. Welcome back to JS Party.

**Divya Saharan:** Hello! Happy to be here.

**Jerold Santo:** And that's not all... We've got Ball! That rhymed. Nice.

**Kevin Ball:** Ball rhymes with all sorts of stuff. Hey! Happy to be here.

**Jerold Santo:** And last but certainly not least is Nick Nisi. What's up Nick?

**Nick Nisi:** Hoy, hoy!

**Jerold Santo:** Hoy, hoy. Is that going to be your call signal from now on?

**Nick Nisi:** I think so. That's how Mr. Burns answers the phone. "Uhm, hoy-hoy!" \[laughter\]

**Jerold Santo:** I like it. I actually like it a lot better when you do it with that affectation, so... I'd suggest keeping it, but doing it just like that next time.

**Nick Nisi:** Perfect.

**Kevin Ball:** We should do a JS Party where everyone adopts an accent. The whole thing.

**Jerold Santo:** Oh, my goodness.

**Nick Nisi:** That'd be terrible!

**Jerold Santo:** That'd be hard just to maintain that for 45 minutes.

**Divya Saharan:** That'd be so hard!

**Jerold Santo:** Well, we have awesome segments, as always. We're gonna start off talking about probably the biggest news in our space over the last couple of weeks, which is GitHub's announcement of their very own package registry. Then we're going to turn to some JavaScript trends. There's a nice post put out by the CB Compiler folks, all about what people are looking for in job skills, and the trends that are happening there in the JavaScript land in 2019... And then finish off with one of our favourite segments, which is shout-outs. I look forward to all that.

Let's start off with GitHub, the source of all code, the host of most code, and trying to be the host of many packages. This was a big announcement that happened last week, and it happened kind of in a weird way, if you ask me. Friday afternoon...?

**Divya Saharan:** Yeah, exactly. I only heard about it because I was at a conference, and then a fellow speaker was like "Hey, did you hear about the announcement?" And he only knew about it because he worked at Microsoft. \[laughs\]

**Jerold Santo:** Yeah... I mean, I'm not a PR person, but I know that a common tactic of PR people is when they want to bury a story - it has to come out, but they don't want to make it a big deal -they will announce it or put out a press release on a Friday afternoon. Famously, back in Antenna gate, with Apple, when Steve Jobs held that event on the campus, and really wanted Antenna gate just to end, back with the iPhone 4 (maybe it was), they had this event on Friday afternoon, and it was effective.

So it's just a strange thing... Maybe they're trying to fly under the radar. It's hard for GitHub to fly under our radar, because we are so integrated. I mean, "we" not Changelog, but "we" the developer community... So maybe they just thought "Hey, let's just do it now, and people will find out." What do you guys think about the Friday afternoon live stream?

**Nick Nisi:** \[04:11\] I saw a tweet about it 2-3 days before, and I thought it was very strange, because usually I find out about new GitHub features on the homepage. There will just be like a little box that says "Hey...!", and that links to their blog, and has whatever the new feature is. Draft PRs, or whatever. But I saw a tweet, and I'm like "Man, they never pre-announce an announcement like this", so... I was pretty excited to tune in, and I watched the live stream and was excited about it.

**Jerold Santo:** I was there long enough to get the gist of the announcement, and then -- it was Friday afternoon, I had other more relaxing things to be doing... So tell us about the stream itself, Nick. I know that Nat Friedman was up there, they brought up some demos... What was the overall feeling of that presentation?

**Nick Nisi:** It looks pretty cool. They did the typical thing with announcing new things, where they're like -- I can't remember the presenter's name, but he kept saying "Nothing up my sleeve" or "No tricks here." They're trying to tell you that it's not magic, this is actually working, and it's doing what we're saying...

**Jerold Santo:** This isn't vaporware?

**Nick Nisi:** Yeah... Which I thought was kind of funny. That was the big takeaway I got from it, other than the actual announcement.

**Kevin Ball:** Were they over-emphasizing that, to the extent where you're like "Hm... Maybe this is vaporware..." \[laughter\]

**Nick Nisi:** Maybe I caught on to that, but no, I don't think so.

**Jerold Santo:** So the details of this you can find in the show notes. Of course, you can just go to github.com/features/package-registry if you want to read it for yourself. It says "Your packages, at home with their code." And it says "With GitHub Package Registry you can safely publish and consume packages within your organization or with the entire world." They have -- I guess you could call it a limited set, or a starter set of supported ecosystems and language; NPM, Ruby Gems, Docker, NuGet, Maven, and I think that's it... There might be a couple more, but that's at least what they're launching with.

**Divya Saharan:** Yeah. I was really surprised Python wasn't on there.

**Nick Nisi:** Yeah.

**Divya Saharan:** Like, pip is in there, and Python is a huge community, and I was like "Where's Python?"

**Jerold Santo:** Yeah. Is that a diss, or is that just the MVP, trying to get something out there...

**Divya Saharan:** No idea.

**Jerold Santo:** It makes a lot of sense, right? I guess first impressions, maybe... Ball, you've been quiet so far - first impressions just of the concept; okay, now GitHub is going to be a package registry... Whether it becomes THE package registry for some of these ecosystems or not, I think that's still left to be found out, but... Just that they're moving into this space, what is your initial impressions?

**Kevin Ball:** Yeah, so there are two areas of this that I think are super-interesting, where GitHub can really make a difference relative to the status quo. One is I think this makes it far easier to set up internal package registries, to share code inside an organization... Because you don't have to figure out anything new, you don't have to set up your own server to manage it, you don't have to do any of that. You just use the tools you're already using, and you can make internal packages and set up an internal registry. So I think the organizational case for that is fascinating.

\[07:25\] The second piece that I think is a very interesting possibility, that we'll see if we can get to, is this potentially allows for end-to-end verification of "Is the code that is in a repository that's visible to the world - the code repository, the open source code, is that what is actually being used to generate the package?" Because we ran into situations like the event-stream hack, where there was discrepancy. People were obfuscating what's easily visible to the world, versus what's actually getting pushed into the registry. And there are obviously some complications here. Almost nobody is shipping raw code, at least in the JavaScript code; you're probably transpiring it, you're bundling it, you're doing whatever... Though actually in things like Ruby and Python and other languages that might be less true.

But what this enables is at least the potential to do end-to-end validation of "Is the code I'm looking at as an open source developer reviewing this actually what's getting installed in my system?"

**Nick Nisi:** That's fascinating, and I think that that's the one main place where they could shine with this. I was trying to think of how they might do that, and this does work with GitHub Actions right out of the box. You can have an action that once you push to master, then take that and package it up, or something, and maybe they could have some kind of badge system where if this package was deployed via this specific action, it gets this badge, and that's like your certified pipeline badge. So it's still up to the packages maybe at that point to set up that verification system, because I'm not sure if they could do it in a global way... But at least then you know that it went through this automated system and not just somebody publishing straight from their desktop.

**Jerold Santo:** Chris in the chat is asking me a question, "Is this GitHub or is this Microsoft?" and what he means by that, I think... And we can't know, but product roadmaps take a long time, and huge new -- I mean, this is a whole other area of their business at this point; these things don't spike out in three weeks and then get released. And we know Microsoft has purchased GitHub - gosh, probably coming up on a year, or 18 months; I can't remember the exact timeframe. But the question is, was this a thing that was already up and moving with the previous GitHub management, with different leadership? Or is this a thing that Microsoft came and said "This is a next step." Because this is a huge next step for them branching out.

**Divya Saharan:** Yup. It's also really exciting, because with this it means that -- because a lot of the times with package registries, like if you think of NPM and Ruby Gems and so on, it's really hard to find, like... Because there's the package registry, and then there's where the code is hosted, and a lot of the community is in GitHub; people submit issues, pull requests... They see the code, and you kind of gather in one place, and not in the actual package management place.

**Jerold Santo:** Right.

**Divya Saharan:** So with this it's really nice, because it seems like a centralized location where people could be like "Oh, okay. I can easily discover packages in GitHub, and I can also see what are the open issues and things like that", without having to toggle between like "Oh, I'm on NPM, and now I have to go back to GitHub", or do the weird click-through, which is like "Where is the GitHub link?"

**Jerold Santo:** The weird click-through, yeah...

**Divya Saharan:** I always find myself -- I've done it so many times, but I'm always "The git... where is the GitHub link?"

**Nick Nisi:** That's all I do on NPM, is just find the GitHub link and then go there.

**Jerold Santo:** Right.

**Divya Saharan:** Exactly, and it's really frustrating... But yeah, so hopefully this will be much nicer, a better workflow. And like you're saying, Nick, with the GitHub Actions - I think that'll be really neat as well, because I find in general whenever I publish a package, I would have to use the NPM CLI, and then... It's basically like two different things I'm doing. I'd be like "Push to GitHub", and then from GitHub I have to version it, and then I have to be like "Okay, let me go publish it on NPM", and then figure out what's happening. I've messed it up a couple of times. Furthermore, I'm like "Wait, let me roll back! Roll back!" \[laughter\]

**Kevin Ball:** \[11:52\] I have a couple questions on this, that are perhaps less sunny... One question is -- one of the really nice things about some of the language-specific registries right now is you don't have to ask about "Where do I load things from?" I'm not much of a sysadmin person, but I know every time I have to muck with Linux and Ubuntu or whatever, I'm like "Shoot! Where do I load these packages from? Some of them are in the default registry; do I have to add registries? Do I have to do this, do I have to do that...?" It's much more of a headache than with Python or Ruby or JavaScript, where I'm just like "Okay, there is one registry, I'm going to install from there, and I'm good." So that's one area where I'm wondering, "Is this a step towards fragmentation in these language ecosystems?"

And then the second one, which is almost the inverse problem, is --

**Jerold Santo:** Centralization, right?

**Kevin Ball:** Centralization, right?

**Jerold Santo:** I know, I was torn as well.

**Kevin Ball:** I kind of like that NPM is a different company than GitHub, and a different company than whatever else. There's GitLab, and GitHub, and whatever. If everything is going through GitHub, which is Microsoft, are we continuing to consolidate power in our industry in those top four companies?

**Jerold Santo:** I know...

**Nick Nisi:** And this is definitely the "embrace and extend" part of Microsoft's past history.

**Jerold Santo:** The three-part strategy, yeah. It's such a weird dichotomy, because you do have both concerns. You have a fragmentation concern, and then you have a centralization concern, and I think they're both legitimate, you know? I could see both of them happening in certain ways, and both of them affecting negatively both the already diverse ecosystems, and then the convergent one ecosystem of GitHub.

Let's talk about it specifically inside the JavaScript, the front-end space - NPM is the only player in the game. You have other clients, you have the Yarn client, but when it comes to registries, it is NPM, and that has both spurred a lot of nourishment in terms of packages publishing, and the ease of use, and all that kind of stuff, but then it can also be lacking competition on the actual hosting and the registry side of things. In that regard, GitHub getting into this can basically put a fire under NPM's butt, and say "Hey, we've got features that you don't have" or "We can do things you don't have because we are the source code host as well, so step up your game", and that can make everybody better.

**Nick Nisi:** Just to confirm, do we think that this is directly competing with NPM's enterprise solutions?

**Divya Saharan:** I assumed it wasn't. I just assumed this was just a way for making the workflow easier, but it wasn't necessarily a competition. I don't know...

**Jerold Santo:** I would think it's direct competition myself. I mean, it's public or private, so I think there's definitely -- maybe not the on-premise stuff... Maybe. I don't know. But definitely in terms of where enterprises do their packages; I think it's a direct competition.

**Nick Nisi:** I do, too.

**Kevin Ball:** Yeah, if we look at what is their pitch at NPM for enterprise package, they have enterprise-grade JavaScript, whatever that means, but then they also say "Do you duplicate development, so manage your internal stuff in the same way you manage your open source stuff?" And then there's team management, which we also are already doing on GitHub... The only thing they have on here that I'm not sure is definitely addressed is this security expertise piece... But yeah, I think most of the value-adds that NPM enterprise have are very much challenged by this.

**Jerold Santo:** \[15:56\] Yeah. I just wanna comment on that enterprise-grade JavaScript; it makes me think of -- have you guys ever seen the enterprise version of Fizz Buzz, that made the rounds a couple of years ago? So funny! It was like this Java class that does Fizz Buzz, the programming quiz, in the most enterprise way possible. I'll try to find the code and put it in the show notes. It's spectacular. But that's what I think of enterprise-grade JavaScript -- it's like, "Are you writing the JavaScript for us, or...? How is it enterprise-grade? Is my code magically better because I'm using you as an enterprise provider?"

**Kevin Ball:** I mean there is also a sort of de-risking component here... Because I don't know if I'm -- I'm probably not the only one who's watched all the age-related drama on Twitter going down over the last few months...

**Divya Saharan:** Oh, definitely...

**Kevin Ball:** But yeah, with that in the background there, there's like a "Hm... I depend on this for an awful lot of stuff. Is this company going to be around in another three years?"

**Jerold Santo:** Can you summarize that without slamming anybody? The drama.

**Kevin Ball:** Yes. So I'm not on the inside of this, I have no context over what is right or wrong... I know that there was once some buzz around a set of people being laid off from NPM, that the assertion made (as I understand it) was that this was done very inelegantly, and by a third-party coming in, rather than direct conversations with the executives, and that perhaps this was done to people who had just recently been hired. So it was done in a way that left a lot of people with a bad taste in their mouth.

Following that, I have seen a number of high-profile members of NPM saying that they are leaving NPM, often without saying too much more than that... So not weighing in on the drama, or the and the that. We did a -- I don't remember if it was JS party of Changelog, but there was an interview we did with Jeff Lem beck and his people... Well, I saw on Twitter that Jeff is leaving NPM. And a number of other folks who have been at least very visible in the community representing NPM have announced publicly that they are leaving NPM. So it makes me wonder what's going on behind the scenes there.

Running a company is bloody hard, and without knowing the background, I don't want to place judgment on one person on another, but it definitely seems like there is a lot of struggle happening there right now.

**Jerold Santo:** Well, if they are in distress, this will crank up the stress for sure, as they have now a heavyweight competitor. I guess we'll talk about the state of the package registry right now... Sign up for the Beta; I guess similar to GitHub Actions, which is I think still "Sign up for the beta", which has been a long time, by the way. Maybe showing some signs of big ships move slowly.

**Kevin Ball:** Google syndrome. How long was Gmail in beta?

**Jerold Santo:** 12 years, wasn't it something like that?

**Nick Nisi:** A couple of other interesting bits on this is that it does work within the APIs of the existing CLI apps that you would use. So you would still use NPM or Yarn or this, and I assume the same thing for Docker and Maven and all of those; I was more just interested in the NPM side of it, obviously... But then it also allows you to have public and private repos. And I think private is only for GitHub Pro, if I remember correctly...

**Divya Saharan:** I think it's free for all now. They've changed that recently.

**Nick Nisi:** For repos. I was wondering about private packages.

**Divya Saharan:** Oh, for packages.... Um, actually it might be Pro, yeah. That would make sense why people go Pro.

**Nick Nisi:** Yeah, it was giving incentive to go Pro. \[laughs\] But yeah, that will be interesting. I think that that coupled with the things that you can potentially do with Actions, or with some kind of certified pipeline, are the things that will make this stand out over just NPM, or Ruby Gems, or whatever the other package managers are.

**Divya Saharan:** Also, totally separately, but I've found it fascinating, because when GitHub announced their new registry, GitLab released an article saying "Hey, we did this before everyone else..." \[laughter\] It was an article saying they did this back in 2016, or something... It was like, "Okay, cool... Nice flex, GitLab." \[laughs\]

**Jerold Santo:** That is funny.

**Kevin Ball:** \[20:24\] I really want to like GitLab, and every time that I've tried their UI, I'm like "This is so much worse than GitHub."

**Divya Saharan:** Yeah.

**Kevin Ball:** The focus on design, interaction and UI isn't there. And I think they're doing some really innovative things, and I think they've done some great stuff for supporting the open source community and supporting the Vue community, which I love, but their product to me as a developer is pretty inferior relative to GitHub.

**Jerold Santo:** GitLab might become the new Dojo. Wasn't Dojo the "Dojo already did that?" \[laughter\]

**Nick Nisi:** I was going to make that joke...

**Jerold Santo:** I beat you to it. Okay, final thoughts on GitHub... A lot of this I think is kind of wait and see, our prognostication of what might happen, our fears, our desires. It's compelling; integrated products are compelling. I think there's an ideological tug of war here, because Git is distributed version control, and we've moved a lot of our stuff to one centralized for-profit company, and now here's a whole other area which was on a different for-profit company, and now it's like "Well, maybe GitHub will be a decentralized platform", and that usually ends up bad.

**Divya Saharan:** I think over time Microsoft will start owning everything. We use VS Code, we use GitHub, and now we'll use their registry... They'll just own every step of the process.

**Kevin Ball:** And what's interesting... There's like four(ish) companies that are dominating the industry right now. You have Microsoft, you have Google, you have Facebook, you have Apple... Did I miss any? I think that's pretty much it...

**Jerold Santo:** Did you say Amazon?

**Kevin Ball:** Oh, Amazon, right. 100%. Amazon. Of those, only one seems to have a bad reputation among developers. Facebook. Folks are kind of jumping on the bandwagon. "Oh, AWS is so awesome! Microsoft is so awesome, all these things they're doing...!" and they are awesome. They're doing a great job, building great things, and we're letting them continue to consolidate power, and consolidate -- as you say, Divya, eventually all of our stuff on this end will be using Microsoft products, and we'll be hosting everything on AWS, and blah-blah-blah... And if you're not hosting on AWS, you're hosting on Azure, or you're hosting on Google Cloud. That's a very fragile world to live in, and it's one where individuals have given up a lot of power.

**Jerold Santo:** Two last points that that makes me think of. The first one is that Microsoft -- you just named Microsoft and said that only one has a bad reputation with developers, and that it wasn't Microsoft, it was Facebook. And it's true. Microsoft has been on a very intentional (I don't know) five or six-year process of mending their relationship with the software developers that weren't always inside the Microsoft Windows camp. And they've done a heck of a job at it. It's evidenced by everybody using VS Code, like Divya is saying; everybody is using GitHub and loving GitHub, and Microsoft owns that, and it hasn't been bad for us yet... So it's just interesting how successful they've been at changing their reputation, because public opinions are a very hard thing to sway.

\[23:56\] The second thought I had is there's an adage, mostly about robotics and automation, and AI and whatnot, about Amazon - in the next ten years you will be either working for Amazon, or they will put you completely out of business. That's the path that Amazon is on, just in the more mainstream space. So in a lot of ways maybe in the software space, set aside AWS, Microsoft might be on that path where they might be the player when it comes to developer tools over the next 5–10 years.

**Divya Saharan:** Yeah. I think it's only in the recent few years when I've heard people say they would want to work for Microsoft... \[laughs\] I have not heard that in a really long time. And now there are lots of developers, very talented developers who are like "If Microsoft gave me a job, I would take it."

**Jerold Santo:** Right.

**Divya Saharan:** That's a huge shift. And that probably moves us to the next segment, on job skills stuff. We can talk about that later, but... It's just an interesting way of how they've positioned themselves. In the developer community they're seen quite well now. And they've obviously done a good job, so... Yeah.

**Nick Nisi:** Just to close it, there's a Twitter account, @npm_parody that speculates on what NPM might actually stand for, and I saw a tweet from them, "Nobody Protected Microsoft." \[laughter\]

**Kevin Ball:** I believe that NPM account was created specifically when the package manager was announced.

**Nick Nisi:** Oh, really?

**Kevin Ball:** All of their tweets are May 10th.

**Jerold Santo:** Could this be...

**Divya Saharan:** Weird... Conspiracy...

**Jerold Santo:** ...the new Horse JS?

**Kevin Ball:** Horse JS has longevity. They first tweeted May 10th, they last tweeted May 10th.

**Jerold Santo:** Oh, it's a one-and-one kind of thing.

**Kevin Ball:** This is a one-hit-wonder Twitter account.

**Break:** \[26:00\]

**Jerold Santo:** Alright, next up we turn our focus to JavaScript trends. The fine folks at CB Compiler have an interesting research and analysis they did; they call it "Game of Frameworks: JavaScript Trends of 2019", wherein they went out and surveyed -- I think it was 300 different job postings in April, from around AngelList, Stack Overflow, LinkedIn etc, and they compiled them down to find out what companies are posting about which skills specifically inside the JavaScript space companies are looking for, and they produced a nice chart. We will link all that in the show notes if you want to look at that chart.

I'll tell you right now that React is number UNO, so it wins the Game of Frameworks, I guess, even though -- is it a framework? I don't think it's a framework. That being said, how do we define these things? Node.js is one there, so... Is it a framework? Git is on there. Is Git a framework? \[laughs\]

**Divya Saharan:** Yeah, I think they call these skills...

**Kevin Ball:** \[27:55\] This is skills, not frameworks...

**Jerold Santo:** I know, but it was called "Game of Frameworks." I know it's a Game of Thrones reference, but it's like, where are the frameworks? Anyway. I'm nit-picking at this point.

**Nick Nisi:** Not a good reference.

**Jerold Santo:** Yeah. Trying too hard.

**Nick Nisi:** The thing that immediately stuck out to me was number seven, Java. I'm immediately "Is this just people spelling it Java, space, Script?" \[laughter\] Do people not realize that Java and JavaScript are different things? Those are the two things that I immediately thought of.

**Jerold Santo:** That might be a legit situation, if they're just going out and relaxing a bunch of job postings, and somebody put a space between... We have to follow up and ask them on that.

**Nick Nisi:** Luckily, Script is not number eight. \[laughter\]

**Jerold Santo:** "We need scripting skills, Nanchang skills..."

**Nick Nisi:** But you also see things on their like SQL, and Python, and stuff... So I think one of the things that that draws to my notice is folks don't want someone necessarily who's only paying attention to JavaScript. You need to understand some of the back-end technologies that you're going to be interacting with.

**Jerold Santo:** jQuery in the top ten there. Still legitimate.

**Divya Saharan:** I'm a little sad that Vue is so low on that list... \[laughs\] Why is it so low?! It's below Python... \[laughter\]

**Kevin Ball:** Python is actually ridiculously popular, but yeah, this is supposedly JavaScript jobs, so...

**Divya Saharan:** Or JavaScript developers... I mean, yeah...

**Nick Nisi:** At least your framework is on there.

**Divya Saharan:** Yeah, that's cool.

**Jerold Santo:** That's true.

**Kevin Ball:** \[laughs\] And not featured things, like Dojo, Ember...

**Divya Saharan:** Well, TypeScript is there, Nick, so \[unintelligible 00:29:30.24\] \[laughs\]

**Nick Nisi:** Yeah. \[laughs\]

**Kevin Ball:** I think it is interesting to think about this... It's hard to know without trend lines how much we should be considering this, but this is an interesting snapshot of what are people looking for. I do wonder -- it says 300 job listings, and then it has numbers next to them, so I'm wondering, is these 267 job listings out of 300 featured React? And if so, why does Angular have 195? Are these saying "React or Angular"? That seems a little off...

**Jerold Santo:** Oh, I bet they probably are. There are some job listings out there where they'll just list off a laundry list of skills that you should have in there, and it'll be a comma-separated list.

**Kevin Ball:** You should now React, Angular, Vue.js...

**Jerold Santo:** Right. 14 years of experience with GraphQL, stuff like that.

**Divya Saharan:** And there's also general ones, which is like not really tech-specific... There's like OOP, and then I think those design patterns as well, which I was like "That's interesting..." Because that's very general, and subjective.

**Nick Nisi:** The one that's curiously missing from here is JavaScript. It's not on there at all.

**Jerold Santo:** Maybe it's pre-supposed. \[laughs\]

**Nick Nisi:** Probably, but that's what we focus on in our interview process - fundamental JavaScript; no framework, no TypeScript, no webpack, no Java JavaScript...

**Jerold Santo:** What about in your listings? Is that how it is as well?

**Nick Nisi:** Yeah, I think so. I will have to double-check that though...

**Kevin Ball:** UUP, now we've got -- quick look...

**Nick Nisi:** Hah.

**Kevin Ball:** So let's step back a little bit from making fun of these folks, because -- I mean, I think there are things to make fun of, but it's actually a really hard problem if you're cross-cutting, which I think they are (it's across industries), to look at what are people putting in resumes and use that to derive something interesting. That's a very hard problem. But what do we think this indicates about finding a job right now, in tech, doing JavaScript? Are there insights that we can draw from this with our additional industry context?

**Divya Saharan:** \[31:53\] I think the expectation is much higher. So like, yes, you should know JavaScript, but there's also this expectation that you also know all these frameworks, you know TypeScript, or you've worked with webpack... So for someone who might be newer, or who has just started picking up skills, it's really overwhelming. And I've talked to a lot of people who have gone through boot camps, or are fresh out of school, and they're like "What should I focus on?" Usually, my answer is just like "Just get perfect at JavaScript, or whatever it is you want to do..." Because I think the flavours come and go. There are a lot of frameworks that come in; React is popular now, but who knows what will happen in five years... So like you're saying, Nick, just a solid understanding of one thing, and then working your way through... But I find a lot of job descriptions tend to just give you the laundry list of everything, and that's really hard for someone who's looking for a job, to be like "Wait, I only have one of this, or two", out of twenty.

**Nick Nisi:** Yeah, for sure. I think that if you have a good, firm understanding of the fundamentals, you can really jump in and pick up Vue, or React, or anything, pretty quickly. It's just JavaScript.

**Kevin Ball:** It's just JavaScript... \[laughs\] I've actually been doing a lot of research on some of this question, of like "What are the skills that we expect of people at different levels?" Because I'm working on a new project focused on training tech leads, so people who are a little further up in the skill ladder. But as a part of that, I'm researching this whole progression... And I've found a fascinating resource that I'd like to share at progression.FYI, which is a gentleman in England who has put together essentially a collection of all these different career progression charts that different companies have published for engineering and for design. Various companies have written about their progression charts, open sourced things, whatever...

And shout-out, by the way, to Natalie Marley, who I've met at React Amsterdam, who pointed me at progression.FYI. It's super-cool stuff. But this guy Johnny Burch has put this together, and one of the things that I've found pouring through this is different companies call these different levels, different things. At one company they might call it Engineering 1 vs. Junior Developer vs. this, that and the other, but there are a lot of commonalities across them... And this isn't going to tell you which skills in terms of "Should I be learning React versus whatever?" But if you're entry-level, and you're a junior, typically what you're going to be doing is you're going to be working on pretty well-defined tasks, doing bug fixes, and really learning how to learn.

So your focus should be figuring out how to go deep. Pick one specialty, go deep. If you're in the front-end, maybe pick React, or something. Pick one framework, go really deep on that, and don't worry about all the other stuff, because junior developers are not being asked to integrate across five different things. They're focused within one area. And then as you go up the hierarchy a little bit, you get into mid-level, 2–3 years in; now you should be able to do something on your own within your area of expertise, and start to get touching other things. That's when you're gonna start to branch out into other skill areas. But yeah, if you're just coming out of a bootcamp, don't try to do all the things. Pick one, go deep on it.

**Jerold Santo:** That's a fascinating take. So would you say in 2019, if you're going to pick one to go deep, it seems like you can't miss with React right now.

**Kevin Ball:** If you are in the front-end, and you're looking for something that's going to get you a job, React is probably your best choice.

**Jerold Santo:** Sorry, Vue.js. Sorry, Divya.

**Divya Saharan:** Vue is still cool.

**Jerold Santo:** \[35:59\] It's still cool. \[laughs\] So Rich Howell in the chat is also a Vue developer, and is currently applying for work, and can confirm that it's pretty low on people's list. He says thankfully, his Vue experience transfers over to React pretty well. So that's one thing that you'll find over time, is a lot of the skills from all these things transfer over. There are some -- if you're deep into Angular and you know the bugs, the workarounds for the bugs, that skill will not translate. Maybe your process of finding those workarounds absolutely will, but you know how exactly to interact with this API because you've gotten that deep into it - that itself probably won't transfer over to another one, because they're not going to have that bug. They're not going to have that specific API. That being said, the general themes and architectural things in a lot of these frameworks will transfer over.

I think a lot of what happens with people is they just get analysis paralysis, and they're just like "What do I pick? What do I do? I've spent most of my time reading articles like this, of which one, because it's such a huge decision." And I guess my point here is just realize it's not that huge of a decision, and maybe just optimize for something like this - "Most jobs here... I'm just going to learn that one and go from there."

It does seem like today -- although maybe tomorrow Vue will be higher up... But if you're gonna just pick one and dive deep, it seems like React is in 2019 your best bet.

**Kevin Ball:** Yeah, there are some megatrends that are showing up across the board, that to your point -- like, if you learn in one example, it will then be easy to branch out. Staying in the front-end world - I think there are also some megatrends in the back-end - component-oriented development. Thinking about things as a set of components that can be interacted, and plug-and-play. React is doing that, Angular is doing that, Vue is doing that, Ember is doing that, Dojo is doing that, Mikhail is doing that, Svelte is doing that... That is the approach that we're going.

Start in React, because it's easy to get a job there. Dive deep, but have in mind, "Okay, how am I thinking about components? What are the boundaries? How are we doing that?" That understanding, that knowledge, that experience is going to translate no matter what framework you end up moving to in the next job, or whatever.

Similarly, things like declarative coding... We are increasingly moving to a declarative paradigm for our components, we're not imperatively doing things we're thinking about. "Here's what this thing should be", and letting the frameworks handle how and when. And that's another place where so long as what you're working in is doing that, which means maybe not focusing on jQuery... But if you're doing React, those skills are once again going to translate.

There's a lot of these megatrends... I identified five in a blog post earlier this year. But if you look for the bigger-picture questions, and start learning those within the context of one thing you're going deep on, you're not going to end up in trouble when suddenly the flavour of the month changes.

**Divya Saharan:** I'm going to assume that's what that list meant by design patterns... To be like, generally, declarative vs. imperative. And how you do something in React, which is overall very specific to the framework, but the pattern of doing it can be used in Angular, and can be used in Vue if you just change some syntax and the structure; essentially, they all call it different things, but they might mean the same. So if you master one framework and just know it really well, translating can be frustrating, but at the same time you have the tools, and you have those patterns that you already are familiar with, and they will probably translate quite easily once you get used to a different syntax, and everything.

Also, I think I posted in the chat, but have you seen that tweet that Emma tweeted a couple of days ago, about React being the kid who cuts school, and then Vue being the nice kid in school? \[laughs\]

**Jerold Santo:** No.

**Divya Saharan:** \[40:06\] She was trying to immortalize the different technologies, and I thought it was hilarious... And CSS is like flaky, unpredictable one. \[laughs\] It's so funny...

**Jerold Santo:** That is funny. We'll have to include that one in the notes as well. One other thing that I noticed in here - and then I want to kick it over to maybe Nick to talk about back-end too, because Node is popular... But inside of Node, what do you learn, what do you dive into there, if you're thinking more back-end JavaScript, is that there are a lot of things on this list - I'm not sure how long this list is; maybe 20 items, but I didn't count them, and they aren't numbered... But there are lots, like four at least that I'm just staring at, that have specifically to do with testing. Unit testing is one, Mocha another one (obviously, a very specific testing library), continuous integration, which you can't really use without tests; Jest, TDD... These are things in here. So in terms of big trends, especially in the dynamic language space -- now, TypeScript is in there as well, which might mitigate some of the tests that you have to write; and Nick can probably gush on that in a minute, but... Learn how to write automated tests for code, because yes, the specifics of the way you do it in this language, how do you mock in this language versus that etc. may not transfer over, but the skill of being able to write a test, to fully exercise a piece of code, you'll use for the rest of your career. So absolutely, that is something that is trending, and will continue to trend until we have machines that write all our tests for us. But then who's going to test the machines...?

What about the back-end, guys?

**Nick Nisi:** I think there's a core set of skills that you need to know about the back-end as well, similarly that there is about the front-end. The primary one that comes to mind when I'm thinking about back-end JavaScript - it seems like everything stems from Express, in some way, at least in what I've seen...

**Kevin Ball:** \[laughs\]

**Jerold Santo:** Just learn Express

**Nick Nisi:** I'm currently using a project called Nests, which is like a TypeScript wrapper around Express, but it makes it more Angular (that's the way I describe it), in a good way.

**Jerold Santo:** Give the elevator pitch on Express. Explain what that is.

**Nick Nisi:** It's a way to handle routes for back-ends. You can define and say - when your server gets a call to this request (this URL, effectively), run this function and deliver something back. Then it gives you the ability to add in middleware and other things, so you can plug in and say "This route is only available to administrators, so before you actually serve it, double-check this route specifically, and make sure that the user is authenticated, to be able to see it. If not, throw them back in there; otherwise run the function." And kind of abstracting that away, so that you don't have to think about it on every single request.

**Jerold Santo:** Anybody have anything to add on the back-end space trends? What to learn, what to avoid maybe?

**Kevin Ball:** I think one thing that is tricky both on the front-end and on the back-end, and I think judging from what I've seen is something that you start to really wrap your head around a little later in the game - certainly a year or two at least into your career, if you're coming from bootcamp, and we have focused very much on early-career folks for this conversation... This is data manipulation and data management. How do I think about taking data, transforming it, using it in different ways, whether that's on the back-end, saying "What are the data stores that I'm working with and how do I normalize my data?", or on the front-end, saying "Okay, I'm loading this data from APIs, but it may not be exactly what I need for my UI, unless I'm using GraphQL, or if I am using GraphQL, thinking about how do I generate those queries?"

\[44:01\] That way that data flows through systems, and you can manipulate it, and thinking about things like transformations, and mapping, and all that stuff - that seems to be something that is a little harder for folks to pick than the kind of first UI logic, or in the back-end, sort of first logic around "Okay, I'm setting up these routes, and this type of thing", but really starts to be important as you go forward. That seems like you're just thinking about data and how data flows through an application is something that -- it's not really well-captured in one particular tool here, but definitely is something that I've seen folks struggle with, and that is really important as you start to move from entry-level to a little bit more senior.

**Nick Nisi:** For sure.

**Divya Saharan:** I think especially since it moves past just working on small features, and you have to think about the overall architecture, and whether it's scalable and maintainable; those are the things that you have to think about - how does the data flow, what is the architecture of the back-end, and how does it provide data to the front-end, and how does the front-end liaise with the back-end, and so on? And just understanding that requires a bit of experience, and having worked on different applications, having played around with things... Yeah, generally the more senior you get, the expectation is that you know how to do that, and how to work those problems.

**Nick Nisi:** Would you classify tooling as a back-end or a front-end thing? Like webpack, and other tooling like that.

**Kevin Ball:** Almost orthogonal.

**Jerold Santo:** Yeah, it depends on what kind of tooling you're talking about, I guess. Are you talking about back-end tooling, or front-end tooling?

**Nick Nisi:** NPM. \[laughter\]

**Jerold Santo:** I would say version control, communication and things like this cross all those chasms, but tooling very specific to -- I mean, Docker, I guess, would be another one that is general. Containers, that kind of stuff.

**Divya Saharan:** I feel like containers moves into DevOps space...

**Jerold Santo:** Well, at least to be able to use them, if not to create them, right?

**Divya Saharan:** Yeah, just like create a Docker file, and then like "Okay..."

**Jerold Santo:** That's very much where I'm still at; it's like "I can create a little Docker file, and I can do a thing, but..."

**Divya Saharan:** That's usually where I'm at, yeah. And half the time when Docker doesn't -- sometimes it has trouble with hot reloading, and then people will be like "Oh, just restart your whatever", and I'm like "Cool..." Just turn it off and on again; that's pretty much mine as well, if it doesn't work...

**Jerold Santo:** A lot of tools are like that. Git - you can get by on about eight Git commands for years. You're just like "Do the magic incantation..."

**Divya Saharan:** Oh, 100% yeah.

**Jerold Santo:** Just write them down, and use them, and eventually you might figure out... I still don't know exactly how Git works. I know there are a lot of pointers to SHA's and stuff, but I don't know; I just have all the commands memorized, and...

**Divya Saharan:** Yeah, and you don't need to use all of them. I think I've only used the Git bisect twice ever, and that was a mistake... \[laughs\]

**Jerold Santo:** Yeah, I used it once, and I'm like "Oh, I'm never doing this again..."

**Divya Saharan:** Exactly, because it's just like "I don't know what's happening."

**Jerold Santo:** I just decided to write fewer bugs.

**Divya Saharan:** Yeah.

**Nick Nisi:** I've done an advanced Git workshop once, and I spent the first hour-and-a-half going through the anatomy of a single commit.

**Jerold Santo:** Wow... You should do that on the show sometime.

**Divya Saharan:** It's very in-depth.

**Nick Nisi:** Yeah... There are a lot of interesting things in there.

**Kevin Ball:** If you choose to climb that ladder, it does open up a lot of fascinating things. I definitely have been called in more than once to recover, like "Oh my god, I feel like I lost my code", or "Oh, what happened here?" Just understanding how Git works, even if you don't necessarily know all the different commands, but if you're willing to put in the work to build that mental model of like "What actually is happening, and where are these things, and what are the many ways that I can find and get to them?", it does have benefits that flow out.

**Divya Saharan:** \[48:03\] I think also when you're starting to have arguments around whether you should squash your commits or do a merge is when you're like "Okay, I think I've levelled up my Git skills...", to a point where you can have an opinion on one versus the other.

**Jerold Santo:** Even if you're Nick and you have the wrong opinion... \[laughter\[

**Divya Saharan:** Hey, what does Nick think?

**Nick Nisi:** Squash all the way.

**Divya Saharan:** Oh, yes! I'm team squash, too. \[laughs\]

**Jerold Santo:** Nick is a pronounced forced pusher, so... You know who you're talking to.

**Nick Nisi:** Yeah.

**Jerold Santo:** You know who you're affiancing with right here.

**Divya Saharan:** I think I've had that opinion on teams before, because I'm like "I like clean history", and they're like "Well, clean history is everything", and I'm like "That's not clean. You're sorting through the garbage."

**Nick Nisi:** Exactly. The people who think that haven't used git bisect.

**Kevin Ball:** Often clean history is incorrect history.

**Jerold Santo:** Do you want to lie to your friends and family? Is that what you want to do?

**Divya Saharan:** Yeah, but most of world history is not raw; it's been cleaned up...

**Nick Nisi:** It's written by the winners.

**Jerold Santo:** Which is why it can't be believed. It's untrustworthy.

**Nick Nisi:** I want to show things the way that they should have gone.

**Kevin Ball:** Right. Which could make it very hard to track down what went wrong. Anyway... We're way off the rails here, but it sounds like Jerold and I are on one side of a holy debate/war, and Divya and Nick are on another.

**Jerold Santo:** We've just found our next segment idea. \[laughter\]

**Break:** \[49:34\]

**Jerold Santo:** Okay, folks, one of our favourite segments is shout-outs. This is a great opportunity for us to shout out and thank or give props to a person, people, a project - anything really, that we think deserves some shout-outs and maybe hasn't got them, maybe has, but we all like to take a turn. Let's start off with Ball... Give us your shout-outs.

**Kevin Ball:** Alright, so I wanna shout-out a category, and then I'm gonna shout-out three particular examples. The category that I wanna shout-out is people who are doing work to bridge between design and development, and sort of emphasize UI-centric and design-centric front-end development. This is a place where stuff often goes wrong, and we've had whole conversations about challenges, even within the front-end development space, the divide and various other things... But there's a lot of people doing yeomen's work here.

Three particular people and instances I'm going to shout out. First, there was a recent article on Smashing Magazine by Stefan Kaltenegger; I probably butchered his name... But he did this article on essentially how you can work to bridge the gap between designers and developers, and it's just kind of a nice walkthrough of things that you can do as a developer and as a designer - I think more focused on the developer - to help bridge that gap. It also referenced out to a cool resource that I hadn't seen before called "Can't unsee", which gives you practice developing your design eye. So that's one of the three people I'm gonna shout-out on this subject.

\[52:09\] The next one is Ryan Singer, who wrote an article on the Signal vs. Noise blog recently about the place of UX, and looking at alternative ways of thinking about user experience as essentially being the boundary between any two things that are supply and demand. One, he was talking about - okay, between the user and the product, that's where we usually think about it, but actually this concept of design is really important at every place where you have interactions between different groups. I think that was really cool.

And then the final shout-out I'm going to do is for a conference that my friend Dylan Schliemann is involved with organizing. Conference organizers in general deserve shout-outs, but this one in particular is a conference called Half stack, which is focused on UI-centric front-end development. They are expanding from being only in London, to having events in Vienna, New York, and Phoenix, and various other things.

It's super-cool to see this UI-focused development stuff growing and being more present around the world, so props to those three people - to Stefan Kaltenegger, Ryan Singer and Dylan Schliemann, all of whose names I probably butchered.

**Jerold Santo:** Ball the Butcher. Alright, Divya, your turn.

**Divya Saharan:** Awesome. I'm going to shout out to a conference, and someone on this panel is organizing it... NEWS. It is really cool, and I've spoken at NEWS two years ago; it was actually my first conference talk, and I feel like the organizers were so cool, and awesome, and the conference itself was wonderful. It wasn't at the zoo, which it is going to be this year, which is super-exciting. Also, I'm so excited about the theme! \[laughs\] It's Life Aquatic, and it's so cool! I heard someone's gonna dress up as Steve Bissau...

**Jerold Santo:** Who is this someone you keep referring to?

**Divya Saharan:** I don't know...

**Jerold Santo:** Could it be Nick Nisi?

**Divya Saharan:** \[laughs\] Could it be...?! I'm more interested in who's going to be the jaguar shark more than anything. \[laughter\]

**Jerold Santo:** I feel like we have to get that done now...

**Divya Saharan:** Yeah. I feel like Nick will just come out with this kid dressed as the jaguar shark.

**Nick Nisi:** Perfect.

**Divya Saharan:** That'd be so cute...!

**Jerold Santo:** Perfection.

**Divya Saharan:** Baby shark.

**Nick Nisi:** Yes!

**Kevin Ball:** "Baby shark doot"

**Divya Saharan:** Oh no, please don't sing it!

**Jerold Santo:** Yeah, please don't. Please don't. Noon, it's too late...! It's in there.

**Divya Saharan:** Yeah, I know. Once it's in your head, you can't get it out. And then this is another shout-out to a tool that Route mentioned on the chat, which is Quokka.js. It's interesting, because this is a tool that I recently heard about, and it's funny that he posted it as well... So I was at Nations, which is a small conference, also really great, in DC, and NIR Kaufman was one of the speakers; he's big in the React community in New York. He spoke about Quokka, and it was so -- I had never heard of it, and I think it's really cool, because it allows you to prototype... It's like a scratch pad for when you're working on stuff, so you're like "Oh wait, I'm working with this library, and I don't know how it works", and you can kind of just use it as a scratch pad, and be like "Let me try different things", and then erase it when you're done, without having to mess up your files... Which I think is so cool and interesting. Even the way that it was presented to me...

Most of the time you look at a framework, and you look at the documentation, and then that's how you learn how it works; a library like Lodash, for example. But with this, you can actually work on the thing... Which I've done before. I've used Run Kit, and various things on NPM, where you're like "Okay, I wanna play around with this tool, and see what things are doing", but I think Quokka allows you to dig really deep into a specific library or tool, which is so interesting, just from a learning perspective... Going back to the conversation of scaling up - to be like "I'm a junior developer", to be like "I want to progress", I think that's such a great tool for you to just learn about how tools are created, how libraries are architecture, and so on.

And then the last thing - I really like shaders, just for fun. They don't really do anything for me in terms of getting me money, or a job...

**Jerold Santo:** \[56:45\] \[laughs\] They're doing something...

**Divya Saharan:** I get excited about them because I think they're really cool, and interesting, and totally different. I also like thinking and doing things outside what I normally do - it's always nice to switch gears - so sometimes in my free time I work on WebGL, and GLSL, which is like the shader language for the web... Super-cool. And there's a library that I recently discovered called Blotter.js, which is a JavaScript API for drawing text effects... And it's so cool! It's done by someone at this hacker school that I went to, called Recourse Centre... Also, a shout-out, because Recourse Centre is awesome. If you've never heard of it, it's like a retreat for developers, so if you're just trying to find your groove, you need to be around other people who are working on \[unintelligible 00:57:39.25\] and the idea is that you can work on a week, or a month -- no, actually it's a week, three months, or... I forget the time span. I did it for a week. So it's very low stakes; you can just take a week off of work and go there. You get to work on a project that you're really interested in.

I worked on WebGL and shaders, which is something I don't normally do... And you're surrounded by super-smart people, and you learn about different things. Yeah, definitely Recourse is a huge shout-out, and the community is awesome as well. If you wanna just plug into a community of developers who are really excited about what they do... That's not Twitter. Twitter has that, but you also have to sort of sort through the garbage, because you can't squash \[unintelligible 00:58:30.04\], or whatever... So yeah, those are my shout-outs.

**Jerold Santo:** Very good. Well, we appreciate the NEWS shout-out. Nick, give the pitch here. Do we have tickets for sale? Or what's the situation on NEWS?

**Nick Nisi:** Tickets for sale. It's August 9th. Our early bird tickets are going right now, and you can pick them up at NEJS.com. I would say that our CFP is still open, but by the time this goes out, it will not be. But that's okay, because we've got a lot of awesome proposals that have been submitted, and really looking forward to the painstaking task of having to say no to so many of them... Because that's always the toughest part of being a conference organizer.

Otherwise, it's August 9th at the Henry Poorly Zoo, the number one zoo in the world, according to many places...

**Divya Saharan:** Is it really?

**Nick Nisi:** I think so. At least it was at one point...

**Jerold Santo:** In the '80s. No, just kidding.

**Nick Nisi:** \[laughs\] Yeah, it's really cool.

**Jerold Santo:** At least in America, for sure, and maybe in the world, I believe. But it's a spectacular zoo. While we're talking conferences, real quick - and I'll get over to you here, Nick - I wanted to mention All Things Open. This fall in October there will be a large portion of Changelog folks at that conference... So if you're going to be there, give us a shout-out, let us know. We might organize something like a meetup, or a live show, or something; there'll be a lot of JS Party people there as well... So I just wanted to give everybody a heads-up that All Things Open, in October - it's in North Carolina - is a thing that we'll have representation, and we'd love to come out and see everybody, and come say hi. That's just a quick one there... Back to you, Nick, on your shout-outs.

**Kevin Ball:** Wait, I want to chime in on the zoo, really quick, as a former San Diego resident...

**Divya Saharan:** My gosh, San Diego Zoo is the best! Sorry, sorry... \[laughs\]

**Jerold Santo:** Second best.

**Kevin Ball:** \[01:00:19.08\] I don't know how to judge it, because I have not actually been to the Omaha Zoo, however I did look up a little bit of the statistics on them, and it looks like by -- when was this... At least a number of years back, by a number of five millions a year to one million a year, there are a lot more people who think the San Diego Zoo is a place worth going.

**Jerold Santo:** Hm... Now we've got a new ground war here.

**Nick Nisi:** Yup...

**Jerold Santo:** We've got Git styles and zoos we can go back and forth on.

**Kevin Ball:** That might just be a statement about San Diego versus Omaha, I don't know.

**Jerold Santo:** Yeah, I think it probably is. There's a lot more people. San Diego has a pretty nice weather. I haven't been to that zoo, but I've also heard that it's a great zoo, so... There's room in the world for more than one awesome zoo, but ours is the best. Alright, Nick. Your turn. \[laughter\]

**Nick Nisi:** Yeah... \[laughs\] My shout-outs - I'm going to shout out to Rene Baclava; I might be mispronouncing his name. He's a really cool guy who works at ESR. He runs a website called learn-dojo.com, and he's just putting out these really cool tutorials on different parts of using the New Dojo. It's just really great to see that, and the community, and they're really great tutorials as well... So shout-out to Rene for doing that.

Then I just have to shout out to Tim Pope, and specifically for his Vim Fugitive plugin. I just recently learned about the g command. I don't know when that got added, but I've been using g status, and g read, and all of these commands to work for the most part with Git, but then I just go back to the command line for things... And with g, you can look at diffs of your commands and then stage those individual hunks right from there, right from within Vim, and you never have to leave, and it's just so nice to be able to curate your Git commits and commit messages, all without ever having to leave them, so thank you, Tim Pope for that.

**Jerold Santo:** Alright. Last but not least - my shout-outs. I want to talk about something that maybe you know about, maybe you don't... It is Go Time. You may know that we have another show that's very similar to this one, called Go Time. And a lot like JS Party, where we had it going for a while, and we put JS Party on hiatus, and we tried to change some things to make things better, and we relaunched with an expanded panel - we had a very similar situation with Go Time.

Go Time when on a hiatus for almost a year, but I'm happy to say it's back now, and the panel is spectacular. You may know some of these names - Mat Ryder, Ashley McNamara, Johnny Tourniquet, Carmen Andon, Jana B. Logan (JBD), as well as Mark Bates. I will just say maybe there isn't too much overlap between JavaScript interests and Go interests, but the thing about Go Time is it's not just about Go -- in fact, we've rewritten the little blurb, which now says "A diverse panel and special guests discuss cloud infrastructure, distributed systems, microservices, Kubernetes, Docker... Oh, and also Go."

I am not a Go developer. I do have a vested interest in Go Time being successful. That being said, I don't have much to do with this show at all, besides I listen to it... And it's a lot like JS Party now; it's a ton of fun. The new panel is spectacular, and they're putting on some really, perfect show. The last one was "Go for beginners", very similar to the conversations that we're having here about getting into JavaScript and learning those things... But I specifically want to mention episode \#84, "Hardware hacking with Tiny Go and Gopher bot", in which Mat interviewed Ron Evans, aka Dead Program, who is just a very entertaining guy and has tons of information all about robotics. He started the Robot project, as well as the -- there was a Ruby and a JavaScript version as well. So that's just a spectacular way of getting to know that show.

\[01:04:12.07\] I just wanted to thank the new panellists, and say if you haven't heard of Go Time, or you gave it a listen a while ago, it's now a good time to check it back out, because it's filled with very awesome people. I want to thank them, and... Yeah, excited to have Go Time back.

**Divya Saharan:** The logo is so cool. I'm just looking at the mesh thing...

**Jerold Santo:** Thank you. Yeah, a little gopher head in there. Alright, any final words before we call it a day?

**Nick Nisi:** There's nothing wrong with force push. \[laughter\] In certain circumstances. \[laughter\]

**Jerold Santo:** Why did I have to ask...?

**Divya Saharan:** You should have said everyone but Nick. \[laughter\]

**Jerold Santo:** I'm going to end the show now, before Ball starts talking about the San Diego Zoo again... Okay, thank you everybody for sticking with us. This has been lots of fun. As always, more shows like this at Changelog.com/jsparty. Hey, do us a favour, if you liked this show - especially for people who are getting into this space, learning - give us a recommendation. We would really appreciate it. We love word of mouth; that means we're doing a good job, putting out good content for you... And that is actually, still, even with all the technology that we have and all the social networks - word of mouth referrals is still the best way that people find and listen to new podcasts, so we'd appreciate you doing that.

That's our show this week. We will see you next time.
