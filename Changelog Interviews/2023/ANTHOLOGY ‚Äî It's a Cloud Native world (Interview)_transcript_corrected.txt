**Adam Staravia:** So we're here with Beefy... But it's really Jeffrey...

**Jeffrey Sick:** Yeah. Full name is Jeffrey Sick, but pretty much everyone in the community calls me Beefy. People even on emails say "Hey, please talk to Beefy", and it's probably like "Okay, but why the heck is this person like J. Sick at the Linux Foundation?" It's like, no, everyone calls me Beefy.

**Adam Staravia:** Right. How did you -- did you give yourself this Beefy name, or is it...? I mean, it's your handle...

**Jeffrey Sick:** It is my handle.

**Adam Staravia:** Like, self-inflicted wound here?

**Jeffrey Sick:** No, no. Not even. A buddy of mine at this point like 25 years ago on ye old AOL Instant Messenger misspelled my name once. Stuck. Jeff, Jeff. And then the y was just like - you know, Jeff is pretty harsh. Most people like "Oh, Beefy", because that's kind of like more of a pet name, and smooth to say, fun to say... So yeah.

**Adam Staravia:** What's your favourite peanut butter?

**Jeffrey Sick:** Alright, my mother --

**Jerold Santo:** I was going to say, I thought your mom might have picked it.

**Jeffrey Sick:** My mother called me Jiffy Jeff for my entire life.

**Adam Staravia:** \[laughs\] I knew it!

**Jerold Santo:** She's a choosy mom.

**Jeffrey Sick:** And guess what? All we bought was If. "The Changelog, sponsored by..." \[laughter\]

**Jerold Santo:** Beefy...

**Adam Staravia:** Beefy. So what do you do, Jeff?

**Jeffrey Sick:** Recently, new title, shiny new title - head of projects at the CNCF. Most people, when they hear that, they go "Wait all of them?"

**Jerold Santo:** Yeah.

**Adam Staravia:** I would think all of them.

**Jeffrey Sick:** Yeah.

**Jerold Santo:** Pretty much...

**Jeffrey Sick:** Honestly, what I'm really doing is I'm a community member first. I came up as a Kubernetes contributor. Been around for a while, so I know a lot of people, I know a lot of the communities and open source projects around it... So I can go and talk with them and figure out "Hey, what do you need? How can we help better? What can we do better to enable your project?" New projects that are coming in, "Hey, how can these projects potentially collaborate?" Because I'm an engineer first, and then kind of schmooze, try to be nice to everyone second. So it's kind of hard to define my job, and a job description, but it's really talk to projects, see what the CNCF is doing, make community happy.

**Adam Staravia:** Gotcha. You take the requirements from the customers, and then you give them to the developers.

**Jerold Santo:** That's right.

**Adam Staravia:** I'm just kidding.

**Jeffrey Sick:** I joined the foundation, so I don't have to hear those words... \[laughter\]

\[07:59\]

*What you do within a tech is you take the specifications from the customers, and you bring them down to the software engineers.*

*Yes. Yes, that's, that's right.*

**Adam Staravia:** I recently watched Office Space, so I had to bring it in... Again.

**Jerold Santo:** How many projects are there?

**Jeffrey Sick:** 160. And right now, as of whatever today is -- the 10th, May 10th... I think there's 12. So there's some number above like seven or eight that are currently getting voted on to be adopted into what's called the CNCF sandbox. Think of it proof of concept projects, projects that don't necessarily have a large community, and they're looking to build a community - they apply to the CNCF sandbox, and then those get voted in. Yeah, I talk with my hands as well. I'm somewhat Italian.

**Adam Staravia:** I like it. I'm down with that. I talk with my hands too, when I get super-excited. And I'm super-excited right now. So you've got sandbox, you've got incubation, you've got graduated.

**Jeffrey Sick:** Oh, yes.

**Adam Staravia:** Okay. So you're not over all projects, but you are over most projects.

**Jeffrey Sick:** Let's talk to people in the CNCF and see which -- no. Honestly, it's over all projects, because I'm interacting with projects at every different level, it's just - I don't want to say I'm in charge of all of them. That's not true at all. But I would say I communicate with all of them, and I'm trying to help the CNCF work with projects in a better way.

**Adam Staravia:** Gotcha. Give us an example. How does that play out for recent, for you?

**Jeffrey Sick:** Recently, when I joined and one of the things that I've been really pushing for is a lot of the processes to grant projects access to cloud resources, that are like group cloud resources under the CNCF, or we have licensed scanning services - we want to give those to the projects, and then step out of the way. "Hey, we don't want to be the bottleneck." But most of the way that we grant that access is still a manual process, even though all of these things have APIs. Well, gee, you look at what Kubernetes has done with their community management... Like, creating a user group in Slack is - memes aside; like, laugh at home... You edit a YAML file. Oh, you're joining a GitHub group, or you've become like a SIG chair, you're editing a YAML file. And then once that file is committed, it's just Git Ops all the way down. Your access gets granted in GitHub, your access gets granted in Slack, all of that. Why don't we do that for all of these services that the CNCF is hosting? Right now, it's still Click Ops. That was cool when the foundation was 10 projects or 15 projects. We're at 160.

**Adam Staravia:** 160 projects...?!

**Jeffrey Sick:** And we're not slowing down.

**Jerold Santo:** And 12 more are being added. That's crazy.

**Jeffrey Sick:** No, those are up for vote... Those are up for TOC vote...

**Jerold Santo:** How many get rejected?

**Jeffrey Sick:** I actually don't have that off the top of my head. I would be willing to guess sandbox-wise it's probably 75% acceptance rate, but please do not hold me to that right now.

**Jerold Santo:** Alright, so 9 out of 12 are getting in.

**Jeffrey Sick:** Hey, hey...

**Jerold Santo:** \[laughs\] We're not naming names...

**Adam Staravia:** What is the - I guess "motivation" probably might not be the best word, but what does the CNCF do in terms of like -- you've got 160 projects... What's the long-term goal? Is it to be bigger than that? What service do you provide to the cloud-native world? What is it that you all do, or hope to do?

**Jeffrey Sick:** This is going to be interesting, because if you ask different people in the CNCF, you might get a different answer. And there might be a canned response, and I should know it... My answer is there is - aside from the couple stable patterns, like Kubernetes and the way that it has an API, and like declarative over imperative stuff, everything's stable right now. That pattern is established. What things and what problems, when consuming that pattern, need to be solved? A good example was "Okay, so now we can create all of these containers and orchestrate them in a meaningful way, but now we have a giant distributed system. What do we do in order to monitor that thing?" Well, Prometheus came out of that.

\[12:05\] So this is a long-winded way of saying we have this foundational technology, at this point we're accepting additional projects to help flesh out what cloud-native actually means. And the definition itself is evolving. We have a bunch of WebAssembly projects. Well, why is that? Because at its core, WebAssembly is - I don't want to say just another container runtime, because that would be bad. But it is another like application runtime. You build it a different way, it has a very different look and feel than a container, but still that idea still fits into the pattern of cloud-native. So that still solves a problem.

So - Geez, what would I do? TL;DR, we're accepting a bunch of projects because not all the problems or questions have been answered in what cloud-native is.

**Adam Staravia:** Gotcha. So you're attempting to, and in many ways succeeding in defining the foundation of cloud-native.

**Jeffrey Sick:** Yeah.

**Adam Staravia:** And everything was originally built on Kubernetes, because that's what I guess was the founding project that really kicked off... So we come back from the Dan Khan days, early CNCF days... Miss you, Dan. But like we were there when it was just two or three projects; a very small CNCF. The original founding days. And as we see it grow and grow over time, a lot of great stuff happened for open source, but you're on the inside, you see what's happening, you are in touch with all these projects. What is the mission? What is the endgame for CNCF?

**Jeffrey Sick:** Geez... Honestly, what is next? The definition of cloud-native in a nutshell is really doing distributed computing repeatably. I mean, that's my definition, in my old noggin. But that doesn't mean always use Kubernetes. Sure, right now, hey, Kubernetes is -- I mean, you look at all the stats, adoption's still up and to the right; it's a hockey stick. That doesn't necessarily mean it's going to be the same thing, or it's going to be THE answer.

So what is the end goal? We don't really have an end goal, aside from if you were doing some sort of distributed computing, like trying to solve or consume or build distributed computing, distributed platforms, how can we do it but make sure that how it's being done is in an open source way? Maybe Kubernetes goes by the wayside, and something else comes up. Maybe there is some new WebAssembly orchestration platform, and then everyone starts adopting that - we want to make sure that that's still possible.

Like, the reason why right now Kubernetes is like -- I don't want to say flagship, but the big thing that everyone thinks of with the CNCF is because of its popularity, not because the CNCF is saying "Everyone use Kubernetes." If something else just starts shooting up and to the right, we also want to be there to help enable them and make sure that the lessons we learned from Kubernetes just, again, hockey-sticking up, can be learned over here, so they have an even better experience than Kubernetes had. It had a lot of growing pains, so let's not have another project repeat that.

**Adam Staravia:** Do you all want all open source projects that support cloud-native to be a part of the CNCF?

**Jeffrey Sick:** Not necessarily. Well, that's probably not a good thing to say for, you know, me and my employer... But honestly, I think that would not -- part of the charter in the CNCF, specifically the TOC, is they are not kingmakers. The TOC, the Technical Oversight Committee, which is like elected positions - they're the ones that pick which projects get adopted, which projects aren't adopted; they dictate who's in the CNCF, and then we the staff enable them --

**Adam Staravia:** Support.

**Jeffrey Sick:** Support, do all that sort of thing. So I'm coming at this as... "My opinion, man..." \[laughter\]

\[15:57\] *"Yeah, well, you know, that's just your opinion, man..."*

**Jeffrey Sick:** Honestly, I tangented. I already forgot the original question. \[laughs\]

**Jerold Santo:** Right. We're always over here in The Big Lebowski...

**Adam Staravia:** I could ask it again...

**Jeffrey Sick:** \[16:09\] Please. I will do The Big Lebowski references for the whole podcast, that's the problem.

**Jerold Santo:** \[laughs\]

**Adam Staravia:** These guys are trying to joke with me, and I'm trying to ask a question here...

**Jerold Santo:** We're hoping you forget it, so that he doesn't have to answer it... I'm with you, but I'm just saying, he's trying to dodge it. Let's keep going... \[laughs\]

**Adam Staravia:** \[unintelligible 00:16:22.20\] Let's try again.

**Jeffrey Sick:** Sure.

**Adam Staravia:** So I'm curious, because it seems like you've got a repeatable way to support projects.

**Jeffrey Sick:** Yes.

**Adam Staravia:** So it makes sense that if it's supporting cloud-native, and it's open source, you'd want it as part of your organization.

**Jeffrey Sick:** I remember now, yeah. So I will go back to, like, there's my personal answer, and then there's probably the party line.

**Adam Staravia:** Can you give us the personal answer?

**Jeffrey Sick:** The personal answer is I don't think that would be healthy for the ecosystem. Again, the tangent of the TOC and the fact that they say they are no kingmakers - same thing; I also think that if all projects were in one foundation, that's probably not healthy for the ecosystem. Like, cloud-native does not mean it as a CNCF project. There are plenty of other cloud-native things that are not in the CNCF.

**Adam Staravia:** Right.

**Jeffrey Sick:** Like, there's Nomad. HashiCorp has Nomad; that's a container orchestration platform. There's still a lot of work being put in and around Nomad, but that's not --

**Adam Staravia:** But they're an IPO-ed company though, so it makes sense why Nomad isn't there, because that would be troublesome for their business.

**Jeffrey Sick:** True, but Nomad is an open source project.

**Adam Staravia:** There's a weight though to being a project in the CNCF. You have the CNCF landscape, so by nature, you want to communicate what is and isn't. But at the same time, doesn't that give it a weight to a project that is?

**Jeffrey Sick:** Well, landscape is a bad example, because the CNCF landscape has projects that aren't CNCF adopted, or CNCF projects.

**Adam Staravia:** That's true. I'll give you that.

**Jeffrey Sick:** So I was actually thinking Nomad might actually be on the landscape. I haven't looked.

**Jerold Santo:** Well, let me give you this example... So we've been here for eight hours, ten hours... I have talked to two people who have said, "Hi, I'm X, and I'm with Project Y. We're in the CNCF." And it's like, there's a --

**Adam Staravia:** A trend.

**Jerold Santo:** There's clout to that.

**Jeffrey Sick:** Yeah.

**Jerold Santo:** So aren't the TOC then -- I mean, they are kind of are kingmakers in that sense, right? Because they're the ones who decide who's in, and everyone who says that they're in, now they're like cooler than they used to be.

**Adam Staravia:** They can leverage the brand equity of the CNCF.

**Jerold Santo:** Right.

**Jeffrey Sick:** True. But in that case, the TOC isn't like picking one technology over another, at least with the sandbox. What's usually happening is they're judging maturity, whether it does fit -- like, whether it is a cloud-native thing or not. If my transcoding software, or some other random project that has nothing to do with cloud computing gets submitted to the sandbox - which that happens - TOC doesn't want... Like, that's not the CNCF. They're the filter.

**Jerold Santo:** Yeah, it makes sense that it has to be like inside the scope.

**Adam Staravia:** There's a velvet rope.

**Jeffrey Sick:** So my personal opinion is I don't think that's healthy for the ecosystem.

**Jerold Santo:** Sure.

**Jeffrey Sick:** But that said - and I think the party line would be "If you want to be supported in the ecosystem, and have the namesake of the foundation behind you - yeah, you probably want to join the CNCF." I also have feelings that sometimes, some projects probably shouldn't have applied. But again, that's my personal opinions, and the TOC are the people that vote on it. Not me.

**Jerold Santo:** Your job is to support the ones that do make it in, however they need support.

**Jeffrey Sick:** \[19:52\] Yup. And honestly, projects that aren't in the CNCF, but are in the landscape - I'm still like around to support and talk to, because again, I don't think this is necessarily a bad thing to have projects outside. Also projects outside looking in could potentially spawn other projects that do want to come in.

**Jerold Santo:** Sure. Do you like this job?

**Jeffrey Sick:** Yeah. Best job I've ever had, and I'm not just saying that because...

**Adam Staravia:** It's being recorded?

**Jeffrey Sick:** Because it's being recorded, and I'm standing in a Linux Foundation event... No. My not-so-brief, but honestly, short resume career - I worked at the University of Michigan for 16 years, and then Red Hat for three. And then I started here a year and a half ago. So out of those -- not getting into like different departments at university, but out of those three areas, or places, Linux Foundation CNCF is the best.

**Jerold Santo:** And your path came through contributing to Kubernetes?

**Jeffrey Sick:** Yup. I actually did a little bit of contribution back in ye old days; we're talking 2014, when it was just open sourced and had to sign a Google CLA to contribute to it... Then my path at the university kind of took me away from it after probably a year, and then I started contributing again in early 2018, and wound up becoming Sig UI Chair. So the Kubernetes dashboard that some people kind of dunk on - they were having leadership issues; they just needed someone that could kind of come in and do more PM work. And also, I had a background in frontend work, so I came in and just helped them out, wound up becoming a Sig Chair for a few years, and then I stepped down after I mentored someone up.

**Jerold Santo:** Gotcha. It's a Cinderella story.

**Adam Staravia:** It's a Cinderella story... \[laughter\] So you say you like this job?

**Jeffrey Sick:** Yeah, I love it.

**Adam Staravia:** What do you like most? What is your favourite thing that you get to do every day?

**Jeffrey Sick:** I feel like this job actually has a real impact on people's lives. When I worked at the University of Michigan, one of the things I did was informatics, and like directly impacting patient care. I loved that. I'm not saying patient care and open source are similar, but there is definitely that impact where I know that I have helped and like impacted other people's lives here, similar to being able to help someone's patient care just by supporting like a clinical app that I wrote, that deals with the results. Different, but same. That just gives me warm, fuzzy feelings, because I don't know, I'm weird.

**Jerold Santo:** No, that's cool.

**Adam Staravia:** Make the world a better place. Change lives.

**Jeffrey Sick:** I was always taught to leave the world better than you found it. I'm one of those people that will make the bed in a hotel room when I'm leaving.

**Jerold Santo:** Hah! I didn't know those people existed.

**Adam Staravia:** They don't.

**Jeffrey Sick:** Okay, so I'm a psychopath apparently, or...? \[laughter\]

**Adam Staravia:** It's the endowment effect. That's what this is.

**Jerold Santo:** It's the Beefy effect.

**Adam Staravia:** The endowment effect is that you don't wash your rental.

**Jerold Santo:** Say what?

**Adam Staravia:** You don't wash your rental car, for example. It's the endowment effect. If you own it, you think it's more valuable. And when you don't own it, you think is less valuable. That's why we don't wash our rental cars.

**Jerold Santo:** Yeah, but he makes his bed in his hotel room.

**Adam Staravia:** I know! He's the anti-endowment effect.

**Jerold Santo:** Oh, okay.

**Jeffrey Sick:** Have either of you -- I can never remember the social experiment or the dude that did this, but Do either of you know about the shopping cart? I don't even know what to call it...

**Jerold Santo:** No.

**Jeffrey Sick:** Someone decided that you can tell whether a person was - not necessarily good or bad, but more focused on the whole, versus the self, based on what they do in a grocery store parking lot. Do they put their shopping cart back where they are supposed to put it or not? And then you can watch people, and if other people will actually take the shopping cart, like someone else's and put it away - it's like, they're the people that actually want to make the world a better place.

**Jerold Santo:** Yeah. You know, in ye old days, supermarkets used to employ people that would walk your --

**Adam Staravia:** Well, guess what \[unintelligible 00:24:03.18\] still does it.

**Jerold Santo:** \[24:06\] ...stuff out to you. Do they still do that?

**Adam Staravia:** Sorry, I spoke too soon. They do it for some. Usually, for senior citizens, and --

**Jerold Santo:** Pregnant people...

**Adam Staravia:** I don't know about trendy people...

**Jerold Santo:** No, pregnant I said... \[laughs\] They're like "Nice shoes. I want to walk your groceries out." \[laughter\]

**Adam Staravia:** Trendy people...

**Jerold Santo:** Do you remember that, back in the day? Were you around back then?

**Jeffrey Sick:** Yes, but... Kind of a small town in Southeast Michigan, that never really happened.

**Jerold Santo:** They never did that?

**Jeffrey Sick:** If it was a senior citizen, or someone that needed help.

**Jerold Santo:** There was a position called bagger. Wasn't it called bagger?

**Jeffrey Sick:** Yeah. I mean, they still have baggers around now.

**Adam Staravia:** There's still baggers in my grocery store...

**Jerold Santo:** Yeah, but the bagger would actually walk with you out to your car, and load the bags into your car, and then they'd take your cart, and they'd take it back.

**Jeffrey Sick:** Now that's called whoever delivers something to your car when you mobile-order it from Target or like Pet Smart.

**Adam Staravia:** I do miss those days. There's something about that. I think you're onto something, Jerold, because what you said you liked about your job, and how you get to change lives is similar to this, because every step of the way you get to support, you get to make the process, the experience a little easier, a little bit better.

**Jeffrey Sick:** Yes, the CNCF is the bagger position of open source. I see where this is going now...

**Adam Staravia:** Well, I've got mad respect for the CNCF... I think you've unified a diverse -- let's hypothesize... If the CNCF did never exist, or it was never formed, if cloud-native was never termed - or even if it is termed, it doesn't matter - how would the world be if there was no CNCF to tie it all together?

**Jeffrey Sick:** That's actually tough to hypothesize... So one of the biggest benefits, thinking at a super-high level, is we're a neutral place for these large vendors to be able to collaborate and essentially make everything better for the consumer in a standardized way. Take that away, and what do you have? You have --

**Adam Staravia:** Proprietary.

**Jeffrey Sick:** Everything winds up being proprietary...

**Jerold Santo:** Right. And wasted effort.

**Adam Staravia:** No clarity, no focus on users...

**Jeffrey Sick:** I mean, they'll focus on users so far as once they get you in there...

**Jerold Santo:** Silence.

**Jeffrey Sick:** ...you're locked in. Like, major vendor lock-in. I think that's the biggest thing.

**Jerold Santo:** Yeah. That's probably true.

**Jeffrey Sick:** The vendor lock-in would be horrible. I can't even imagine it. And I'm trying to remember back in Heroku, PHP, like 2008–2009 days of hosting web services, everyone kind of had their own thing... But even then, it wasn't that bad. Stuff made sense. But also, no one was really sticking around long enough to potentially have - I won't say a monopoly, but a lion's share to lock you in, so it doesn't make sense to shift elsewhere. At that point, everything was VMs, right?

**Jerold Santo:** Yeah, exactly.

**Jeffrey Sick:** So... Hey, look, I can spin up a VM on my box, make sure it works, and then ship the whole thing. It sucks, but doable.

**Adam Staravia:** Sure. Jeff, I'm glad you talked to us, man.

**Jeffrey Sick:** Dude, this is awesome. Thank you.

**Adam Staravia:** Thank you for sharing your story, and the CNCF stuff, and all that good stuff.

**Jeffrey Sick:** Shout-out to Kara for dragging me away from the booth...

**Jerold Santo:** Real quick, what's your favourite project, and what's your least favourite project? Go!

**Jeffrey Sick:** Absolutely not. I refuse. \[laughter\] This interview was over. Imagine me knocking over the microphone.

**Jerold Santo:** Well, not the project. But the people. Tell us who is your favourite person, and your least -- I'm just messing...

**Jeffrey Sick:** Oh, actually, I can at least tell you my favourite person...

**Jerold Santo:** Okay.

**Jeffrey Sick:** I had a co-worker who was also a roommate, who is also my best friend, and he's my best man; he was my best man at my wedding.

**Jerold Santo:** Oh, wow.

**Jeffrey Sick:** We worked at the University of Michigan since the start, we both moved departments from Pathology over to Advanced Research Computing. I went to Red Hat, he went to Google. My best friend is Bob \[unintelligible 00:28:08.06\] He lives down the street from me.

**Jerold Santo:** That's cool.

**Jeffrey Sick:** \[28:12\] We are almost inseparable, except when I get to go to events and he doesn't. Trust me, if he was here, I would have been asking for another microphone, because we just would have done that.

**Jerold Santo:** We have another microphone. We would have got him on.

**Adam Staravia:** We do have one more if we need it. So... Bob, come on!!

**Jerold Santo:** That's cool.

**Jeffrey Sick:** Oh, are you going to Rubicon Chicago? I'll drag him over.

**Adam Staravia:** Let's talk off-mic. I've got ideas.

**Jerold Santo:** Alright, thanks, Jeff.

**Jeffrey Sick:** Thank you all.

**Break**: \[28:38\]

**Adam Staravia:** So the Kubernetes API... That's what you work on, right?

**Eddie Zane ski:** I work on the CLI.

**Adam Staravia:** Oh, the CLI. Okay, that's an abstraction of that, right? You're actually interfacing with the API, with the CLI, right?

**Eddie Zane ski:** We're probably the biggest consumer of the API.

**Adam Staravia:** Okay... How does that work, the CLI?

**Eddie Zane ski:** So are you familiar with how the Kubernetes project is broken up into special interest groups?

**Adam Staravia:** School me. School me.

**Eddie Zane ski:** Yeah. So we've got to SIG's. So basically, every part of the Kubernetes codebase --

**Adam Staravia:** What does a SIG mean?

**Eddie Zane ski:** Special Interest Group.

**Adam Staravia:** Okay.

**Eddie Zane ski:** So we've got a SIG for API machinery; they own the API and the stuff that runs on the master nodes... So I work on SIG CLI, which is the SIG for the command line tooling. So it's subject, customize, GUI, which is a like GUI framework for subject... A couple other subprojects... But yeah, so I've been working on that for four years now, and it's a lot of fun.

**Jerold Santo:** Subject, huh?

**Eddie Zane ski:** Yeah.

**Jerold Santo:** Is that official?

**Eddie Zane ski:** Well, you all noticed throughout this talk I say it many different ways on purpose, so...

**Jerold Santo:** Okay. So you rotate.

**Eddie Zane ski:** You just called me out early.

**Jerold Santo:** You're a diplomat.

**Adam Staravia:** So if you say tube cuttle here in a bit - that's on purpose.

**Eddie Zane ski:** I'm also going to say Cub Ectal, so...

**Jerold Santo:** Cub Ectal. \[unintelligible 00:34:04.00\]

**Adam Staravia:** Oh, gosh. Who says Cub Ectal?

**Jerold Santo:** Well, if you want to hit all the variations...

**Adam Staravia:** People say Cub Ectal?

**Eddie Zane ski:** Yup.

**Adam Staravia:** Is it for fun, or is it for serious?

**Eddie Zane ski:** I've heard both ways. \[laughs\]

**Jerold Santo:** Wow...

**Adam Staravia:** Why not, right? If you can interpret something 17 ways, why not be 18?

**Eddie Zane ski:** It's true.

**Jerold Santo:** I just think that maybe Kubernetes is so complex and intimidating that whenever we have people on to talk about it, we just bike-shed the subject thing. What do you think?

**Adam Staravia:** Sure.

**Jerold Santo:** I feel like you and I always end up right here, talking about the subject.

**Adam Staravia:** For sure. I mean --

**Eddie Zane ski:** You can go to kubectl.info, and it's a recording of Tim Hocking who originally wrote it saying how he pronounces it.

**Jerold Santo:** I think we had Tim on the show back in the day.

**Adam Staravia:** Yeah, we talked to Tim forever ago, basically. The godfather.

**Jerold Santo:** Yeah, when it first became a thing.

**Adam Staravia:** Yeah.

**Eddie Zane ski:** Nice.

**Adam Staravia:** He was at Google then. Is he still at Google?

**Eddie Zane ski:** He's still at Google, yeah.

**Adam Staravia:** Well, there you go. Food for you, Tim. Slay it. What should we know about the CLI? What's important with its development team, the SIG, how does it work...

**Jerold Santo:** Maintaining it...?

**Eddie Zane ski:** Yeah. So one of the hardest things we have to do is say no to people, all day.

**Adam Staravia:** Oh, I bet. I'm sure a lot of people have told you that, but... Everyone wants a short flag for everything, everyone wants a long flag for everything...

**Jerold Santo:** A lot of flags.

**Eddie Zane ski:** Everyone wants every feature as a flag or command...

**Jerold Santo:** How many flags does it currently have?

**Adam Staravia:** What's the language of the CLI?

**Eddie Zane ski:** It's all Go.

**Adam Staravia:** It's all Go. Okay.

**Eddie Zane ski:** Yup. Cobra...

**Adam Staravia:** I've been doing a lot of Bash scripting, and I'm like, you know, at some point I'm going to graduate from Bash to something else besides Bash... But it does a lot.

**Jerold Santo:** Oh, yeah.

**Adam Staravia:** Like, Bash scripting is a lot of fun, and it's pretty powerful, but I feel like my next -- if I keep going in this direction...

**Jerold Santo:** Going...?

**Adam Staravia:** Go. Yeah.

**Eddie Zane ski:** I mean, I feel like I'm learning Bash. I've never sat down to properly learn Bash, and you can do a lot with it.

**Adam Staravia:** Yeah. And thank God for ChatGPT, because I'm learning Bash left and right because of ChatGPT.

**Jerold Santo:** It's somewhat esoteric in my history, but I think having ChatGPT would make it super-easy to accomplish a lot of things.

**Adam Staravia:** \[36:00\] It is. I mean, there's a lot you can -- I mean, you can iterate quite a lot with it, which is a side tangent from crafting a CLI with Go, but...

**Jerold Santo:** Yeah, but even the looping and the conditionals inside the loops... There's weird times when you use the square brackets, you don't have to, and then there are flags, there's conditional flags inside the loops, and stuff...

**Eddie Zane ski:** How many square brackets do you use...

**Jerold Santo:** Yeah, multiple square brackets change things... It is esoteric, but powerful.

**Adam Staravia:** Very powerful. And it's already there.

**Jerold Santo:** And you use it just -- when I say 'you', I'm talking about me. You use it frequently enough that you always have to Google for the syntax.

**Adam Staravia:** Oh, yeah.

**Jerold Santo:** So again, GPTs for the win on that one.

**Adam Staravia:** Yeah, for sure. And on that note, I am very thankful, because -- well, this isn't about ChatGPT necessarily, but I think it has flattened the world to allow people who are Go-curious, or Bash-curious, or scripting-curious...

**Jerold Santo:** Kubectl-curious...

**Adam Staravia:** Tube cuttle, or -- what was the other one?

**Eddie Zane ski:** Tube CTL, Tube Control... Tube Ectal...

**Adam Staravia:** Tube Ectal, yeah.

**Jerold Santo:** Which is kind of cool to say, actually. Tube Ectal.

**Adam Staravia:** You know what you want, you can describe what you want, but you can't quite get there. But if you learn enough, then you can repeat yourself, you learn that stuff, and...

**Jerold Santo:** This episode brought to you by Open AI.

**Adam Staravia:** That's right, there you go. OpenAI.

**Jerold Santo:** How many flags does Subject have?

**Eddie Zane ski:** Oh, man, I can't tell you that.

**Adam Staravia:** Gosh...

**Eddie Zane ski:** We've got a lot. We've got a lot of sub-commands. We've got probably 20 sub-commands, maybe more, and they all have lots and lots of flags. Furthermore, we basically have an entire framework just to add flags to the commands if they get instantiated.

**Jerold Santo:** Oh, yes, the old flagging framework...

**Eddie Zane ski:** Yeah.

**Jerold Santo:** What's the biggest challenge? So you said no, but... Maybe personally. Maybe not as a team, but personally. You've been on the project for four years; we didn't exactly hear about how you got there or anything like that, but what are the challenges maintaining a project of that high demand and use?

**Eddie Zane ski:** Definitely contributors. We have a saying on Kubernetes, "Chop wood, carry water."

**Jerold Santo:** Say again?

**Eddie Zane ski:** "Chop wood, carry water."

**Jerold Santo:** "Chop wood, carry water."

**Eddie Zane ski:** Kind of doing the unglamorous work that someone has to do... And we need people to just come do that; triage issues, respond to open pull requests, review... One of the things I encourage lots of new people to do is you don't have to be a reviewer for the Kubernetes project to go and review pull requests. Just doing an initial pass of being like "Oh, this is probably a better way to write this if statement, so you don't have like three else's under it." Just like little things. So that's what I encourage a lot of new folks to do, is just start reviewing code, just start responding to issues.

**Jerold Santo:** Just comment on the issue.

**Eddie Zane ski:** Yeah. Just comment.

**Adam Staravia:** Who's contributing to the CLI?

**Eddie Zane ski:** Who's contributing to the CLI?

**Adam Staravia:** Is it the SIG team primarily, or is it outside contribution?

**Eddie Zane ski:** So I'm sure every SIG would say --

**Adam Staravia:** How risky is the code?

**Eddie Zane ski:** Well, it's probably part of the oldest codebase of Kubernetes itself, because you build the API server, and the node, and then you build the CLI at the same time to talk to everything... So we've got a lot of dragons that are there, and a lot of stuff we come across, and... So it's funny, people don't realize that Kubernetes is all JSON internally. You hear the Kubernetes and cloud-native world complain about YAML...

**Jerold Santo:** YAML, yeah.

**Eddie Zane ski:** And Kubernetes doesn't know YAML internally.

**Jerold Santo:** It's all JSON, huh?

**Eddie Zane ski:** It's all JSON.

**Jerold Santo:** That's news to me...

**Eddie Zane ski:** So it goes JSON, to YAML on the response, and then when it comes to the command line, we actually marshal it back to JSON, and then we have to go from JSON to figuring out what Go type we have; so if it's a pod, or a node, or something. So that's a large chunk of the code that we maintain, is just dealing with marshalling from format to format, and then figuring out what Go struct we have at the end of the day.

**Jerold Santo:** Why don't you just go from YAML to Go struct?

**Eddie Zane ski:** From YAML to Go struct... We could.

**Jerold Santo:** That would just take one marshal out of the \[unintelligible 00:39:42.10\]

**Eddie Zane ski:** It would. It's working with the -- the Go YAML world is kind of interesting. We could probably talk about that for a long time. But we have a forked version of the Go YAML project.

**Jerold Santo:** Gotcha.

**Eddie Zane ski:** There are many different versions, and the project bundles --

**Jerold Santo:** But this one is yours...

**Eddie Zane ski:** \[40:02\] Yeah, the project bundles like three of them. One didn't like preserve comments or something in your YAML... So when you're dealing with client-side YAML for users, you want to keep their comments around, and...

**Jerold Santo:** Well, that's one of the problems with JSON, is like no comments.

**Eddie Zane ski:** No comments, right? So...

**Jerold Santo:** So you've got three Yams in there?

**Eddie Zane ski:** We've got a couple versions of the same library, yeah. We try to keep one, but YAML is a special case.

**Jerold Santo:** Sure. Well, you've got to do what you've got to do.

**Adam Staravia:** I like YAML. It's not the worst.

**Eddie Zane ski:** It's not as bad as people make it out.

**Jerold Santo:** No...

**Eddie Zane ski:** I'd rather write YAML than JSON.

**Jerold Santo:** Agreed, for the most part. I feel like you can shoot yourself in the foot more with YAML.

**Eddie Zane ski:** Yes.

**Jerold Santo:** And complex YAML is very complex. But simple YAML s very simple. So I'm not against it.

**Adam Staravia:** Yeah... JSON might be easier to read if it's prettier-ed, potentially.

**Jerold Santo:** Yeah. It's more verbose.

**Adam Staravia:** Yeah. You can see the indentations and the nesting a lot better than you might, I guess -- well, I guess you can see either of those pretty easily, but...

**Eddie Zane ski:** I like it in YAML because my editor can show me the number of tab indents I have. So it can show me a 1, 2, 3, and that's really nice to see.

**Jerold Santo:** Yeah.

**Adam Staravia:** So that's your biggest challenge, is this marshalling around YAML?

**Jerold Santo:** Contributors!

**Eddie Zane ski:** New contributors, for sure.

**Adam Staravia:** Contributors.

**Eddie Zane ski:** Yeah. So people working on the project - I work with people from Google, Red Hat, we had someone from Shopify that unfortunately just got laid off; pour some out... A bunch of Googlers, Red Hatters.

**Adam Staravia:** Not gin though. Don't pour your gin out.

**Eddie Zane ski:** Yeah. And then we have people who come by, and they want to get involved in Kubernetes, and they're curious about things, and the CLI seems like a great entry point. As a project, we're still struggling with mentorship programs and onboarding. And one of the hard parts is maintainer burnout, because we can -- early on, I was very happy to sit down with someone for hours, and just walk them through stuff, answer every question, help them write their code... And then they make their one contribution, and then they disappear and don't come back. And you do that enough times, and you're feeling really crispy, so...

**Jerold Santo:** Yeah, it makes sense.

**Adam Staravia:** Do you do videos? Do you find ways to not repeat yourself in that way? So you can say "Here's me telling you how to do these things, and sit down with you." Maybe there's a video you could do, or documentation... That seems to be the easy -- you know, "Hey, why don't you just do documentation?" But is there a way you can sort of put down the wisdom, so to speak, from a mentorship perspective, and succession planning...? This is something that's big for Maintainer Month, is how can you operate with balance as a team, as an individual, and then also, how can you plan for secession when it's necessary?

**Eddie Zane ski:** It's definitely something we're working through with the project. We have tons of developer documentation, probably too much, that people don't read. It's overwhelming when you first come in. Getting your development environment set up - it's so many moving pieces. And container runtime really only works well on Linux, and most people aren't running Linux as their OS...

**Adam Staravia:** How dare them?!

**Eddie Zane ski:** Right?!

**Adam Staravia:** Linux. Linux for life!

**Eddie Zane ski:** But it's something we're definitely trying to work towards. We want to make as much onboarding materials as we can. We've had mentorship cohorts, but at the end of the day it's very complex as a codebase. And it's just old, and there's so much -- we don't say tribal knowledge anymore. What do we say? Preconceived knowledge...

**Adam Staravia:** Wisdom... Experience...

**Eddie Zane ski:** Decisions that were made a while ago, right? And people come in headstrong, really wanting to help out and contribute, and it's like "Well, we tried that, and here's why it didn't work six different times." And that is the hard part, is the context and the history; how do we communicate that to new people.

**Adam Staravia:** \[43:54\] Right. What's the process to become a contributor long-term? You put time into this person, you watch their codebase, and they gave one contribution and never came back. What is the process to have a long-term contribution plan? Is there a term of service? We hear from OSP Os like "Hey, comfort term of service." That means maybe a year, maybe it's six months, maybe it's three years... And then there's repetition in that... How do you all plan that out? Is there a form and function around that?

**Eddie Zane ski:** Do you know Mike McQuaid?

**Adam Staravia:** Yup.

**Eddie Zane ski:** So Mike McQuaid - he's the lead maintainer for Homebrew, and he's got a blog post that he wrote back in 2018 that's kind of resonated with me. It's "Don't mentor first-time contributors. Don't mentor second-time contributors. Mentor third-time contributors." And it's the idea that - like I explained, you get burnt out if you keep spending time on people who just don't come back. But if they've made two contributions, and they've come back for the third, it's like "Alright, cool, you're in it. You've gone through the hard part, the weeds. We can grow you into a maintainer." Because that's the goal at the end of the day, is to grow people into maintainers. We want as many as we can get.

**Jerold Santo:** Yeah.

**Adam Staravia:** What brings somebody back three times to the Kubernetes CLI, for example? What does is it that brings them back? Is it because they have a vested interest, they're super-curious, they have funded time interest, their employer pays for it? What are the attributes of a person who comes back again and again?

**Eddie Zane ski:** I don't have a good answer. I really don't. It's people who want to get involved and contribute back, and some people might be encouraged to get involved in open source... Some people want to learn Go, they want to learn Kubernetes in general... Yeah, we see people come for all different reasons. Some people really just want to build their resume, and just want to build up their GitHub stats, and show that they've contributed. So yeah, it is hard to filter through and apply the right time to the right folks.

**Jerold Santo:** So what do you think of this word, "rewrite"? Do you like that word?

**Eddie Zane ski:** It's a word... \[laughter\] It's part of the English language...

**Jerold Santo:** Okay... Have you ever considered it with the CLI? Not throw one out and start fresh, but start fresh alongside the one that exists.

**Adam Staravia:** Oh yes, the parallel...

**Jerold Santo:** The old big rewrite.

**Adam Staravia:** The parallel rewrite.

**Jerold Santo:** Because you've got a lot of baggage, according to you. And that's perhaps scary, but maybe in an open source world not so bad way of like - instead of just like trying to bring this one up to snuff, you just maintain it status quo and rewrite the sucker.

**Eddie Zane ski:** Yeah, so we have an initiative that we've been rewriting commands to like our new pattern that's more concise, and we've got like the options and the flags dangling off the command struct, and... You know, in the Go world that makes a lot of sense.

From scratch is an interesting one... The Kubernetes project as a whole - we are terrified of breaking users. So the example I like to give is I've been trying to get delete confirmation into this CLI for the longest time. When you delete a namespace in Kubernetes, you delete everything that was in that namespace. When you accidentally delete all namespaces in your cluster, you've wiped everything out, and you're going to have a bad time. And I could show you tons of GitHub issues where people say, "Why was it so easy for me to make this mistake? Why didn't it ask me are you sure you want to blow everything away?" And the reality is that we can't just start asking, "Are you sure you want to delete everything?" because your CI pipeline would break? We'd break everyone's build. People are updating their CI runs, and they don't know what version of the client they're using. They don't really read the release notes. So that's just an example. I've been trying to get delete confirmation in since I started.

**Jerold Santo:** Isn't that what SemVer is for? Major release.

**Eddie Zane ski:** We don't want to do a major release for the project. As far as we know, we can barely get people to upgrade the minor versions.

**Jerold Santo:** But majors are easier, because people get excited.

**Adam Staravia:** That's right. Is there something to learn from the way Linux is distributed? Like, LTS'ES, and versions, and... I mean, every time I do a new Ubuntu installation, it's 18, it's 22, it's 20... And I'm cool with that. There's an LTS, there's a spectrum of risk... It's clear... Is that a possibility with the CLI? I mean, this is a crucial piece. It's like the centrepiece for Kubernetes, for the most part, right? It's the main consumer of the API.

**Eddie Zane ski:** \[48:14\] It's definitely the first thing you reach for, right?

**Adam Staravia:** Right.

**Jerold Santo:** Yeah.

**Eddie Zane ski:** There are two answers there. So the first one - LTS is actually something we just started talking about again. So we were on Rubicon in Amsterdam two weeks ago, and Jeremy Rickard from Microsoft revived the talk around the working group for LTS. So we did it a couple of years ago, we determined that it wasn't something we wanted to do or support at the time, or had the capability... So that just got revived two weeks ago.

And then the other thing, subject is versioned as part of the Kubernetes project itself. So I can't release a separate version of subject.

**Jerold Santo:** That makes it harder.

**Adam Staravia:** It does.

**Eddie Zane ski:** Yeah. So we do have a proposal out that probably needs to get revived, but that was something we wanted to do. But then you get the problem of the compatibility and skew matrix. What version of the client is supported by what version of the API server?

**Jerold Santo:** Yeah...

**Adam Staravia:** Useful software gets upgraded. Here's one thing we learned from GitHub, and a lot of other things out there, where it's like, permission to mess up, permission to do something different. If you can release a different version of it in parallel, that has what everybody wants, and it fixes all the problems, and maybe internally it's easier to develop, and it's potentially easier to have contributors, and easier to document... Like, that has potential; there's an opportunity for that useful software just to get upgraded, because hey, this is just so useful. This person is using it, that company is using it... And it's sort of like a social norm to upgrade, because it's just... Useful.

**Eddie Zane ski:** Right. The rewriting thing would probably get like -- it probably would be impossible to get through. Any significant changes to the project go through what we call the KEEP process, the Kubernetes Enhancement Proposals. And I could just see like opening a KEEP for "Rewrite subject", and just like "No." That just gets closed, right?

**Jerold Santo:** Yeah.

**Adam Staravia:** What if you already did it?

**Eddie Zane ski:** What if we already did it?

**Adam Staravia:** That's right.

**Jerold Santo:** A first-time contributor shows up, "I rewrote this..."

**Eddie Zane ski:** There's nothing stopping us or anyone from doing that. The reality is we are changing the tires on a bus that's moving 1,000 miles an hour down the highway, right?

**Jerold Santo:** Maybe it actually turns into more like a yarn and NPM kind of situation, where it's not you guys that rewrite it, but it's somebody else that comes alongside and says, "Well, we can write our own CLI against the Kubernetes API, and here's seven ways it's better. And hey, who wants to use this?" And I don't know if you can actually just side-install that sucker and use -- maybe it's subject with -cuddle, or something.

**Eddie Zane ski:** That's a conference now.

**Jerold Santo:** Oh, it is?

**Eddie Zane ski:** Yeah.

**Jerold Santo:** Dang it!

**Eddie Zane ski:** In a perfect world that, Subject wouldn't exist, right?

**Jerold Santo:** Why is that?

**Eddie Zane ski:** You can think of it like SSH for a server. I don't want my developers SSH into my server. I don't want my developers pushing and making configuration changes to my production server. Furthermore, I want a trusted build entity that is applying these changes after they've been reviewed. So it's just kind of giving the developer keys to the castle.

**Adam Staravia:** Deleting namespaces.

**Eddie Zane ski:** Yeah. I'd rather not have to give people the client in the first place. So I think instead of building one from scratch, I'd love to see us get to a point where the Git Ops tooling and all this other stuff is in a place where you don't need it in the first place.

**Adam Staravia:** You can rewrite it in a different route, through --

**Jerold Santo:** \[laughs\] Write something else.

**Adam Staravia:** ...in the Git Ops world build that thing to make it obsolete.

**Eddie Zane ski:** Yeah, that's fair.

**Jerold Santo:** And then you can take a vacation. \[laughter\]

**Eddie Zane ski:** Yeah, I would love one of those.

**Adam Staravia:** What I like about this podcast though is we look at things like yarn and NPM, we look at -- we're not only in this cloud-native specific world, and sort of have tunnel vision; we sort of see outside all software, "What was done here to solve that problem, and what was wise about that choice that we can apply here?" That's what I love about the conversations I think we get to have, is that Jerold and I have the luxury and the privilege to speak software at large, really.

**Jerold Santo:** \[52:18\] Right. Plus we get to bike-shed things but not actually be the person that has to go paint the bike-shed...

**Adam Staravia:** That's right. We can give you the idea, Eddie. We're like "Godspeed, bro."

**Jerold Santo:** "I told Eddie to rewrite the thing, and he just won't do it." \[laughter\]

**Eddie Zane ski:** I've got a good one for you all then.

**Jerold Santo:** Okay...

**Eddie Zane ski:** So I also work on the build and test infrastructure for the project. And we're unique as a project in that we handle distribution of all of our own artifacts and binaries. And our artifacts aren't just binaries, they're containers and OCI images. So our CI bill is like $3 million a year. Google gives us $3 million of GCP credit - shout-out to them. Thank you, Tim.

**Jerold Santo:** Wow.

**Eddie Zane ski:** And I think it cost us like $250,000 a month for storage and network ingress and compute. And egress. And we're working very hard to get that down, actually. Amazon just also gave us a $3 million donation, and we set up a registry proxy --

**Jerold Santo:** Woo-hoo!

**Eddie Zane ski:** Yeah, thank you to Amazon. And for a while, everyone was downloading from our container registry. Because you can't just mirror a container registry like you can mirror a Linux kernel, right? So I think some work can probably be done on that space, but that's a problem that we deal with, that a lot of other projects don't deal with... We have to distribute and front the bill and host all this stuff ourselves.

**Adam Staravia:** That's a big bill.

**Jerold Santo:** That's a hard problem.

**Adam Staravia:** $3 million, just for CI.

**Eddie Zane ski:** Yeah.

**Jerold Santo:** Have you tried R2? \[laughter\] Free egress...

**Eddie Zane ski:** We are talking to Cloudflare for a bunch of different things.

**Adam Staravia:** They would love that, I bet.

**Jerold Santo:** I assume so, yeah.

**Eddie Zane ski:** Yeah, hopefully they help us out.

**Jerold Santo:** Yeah.

**Eddie Zane ski:** We want to do caching too, with Cloudflare, or Vastly, or someone. So shout-out to them, please...

**Adam Staravia:** We like them both.

**Eddie Zane ski:** We're very expensive as an open source project to support.

**Adam Staravia:** And crucial. It's a cloud-native world... Just trying to operate in it.

**Eddie Zane ski:** Yeah. \[laughs\]

**Adam Staravia:** You probably know our audience, to some degree... What else is left unsaid? What else should our audience know about crafting the CLI, and interacting with potential contributors, and...

**Jerold Santo:** Maintainer hacks...

**Adam Staravia:** Yeah, maintainer hacks... Sure.

**Eddie Zane ski:** So my maintainer hack is that I triage new issues first. And people kind of -- this is controversial, probably. A lot of people say you should start with the oldest issues, and triage them. We've found that our newest issues are probably the most relevant, just because -- we get hundreds of issues a week open on the project. And the way that the Kubernetes repo works is we have the main OK repo, the Kubernetes/Kubernetes repo, and then we have a staging repo. So a subject is a staging repo. So we don't actually accept pull requests to subject as a repo; it has to be made to the main project in the staging directory, and that gets replicated to our repo. So we track issues in both places, and we take PRs in one. So we've got issues all over the place. I can barely keep up with the issues that are on my repo, let alone the main one, so...

**Jerold Santo:** So first in, last out.

**Eddie Zane ski:** Yeah. So I start with the newest ones, because they're usually the freshest and most relevant, and a lot of times we can just close them right off the bat, because it's a support issue, or something else...

**Jerold Santo:** Or a new flag, and you're just like "No."

**Eddie Zane ski:** Or "You're eight versions behind. Please upgrade and try again."

**Jerold Santo:** Or it's an issue that's like "Help. I just deleted my whole namespace." \[laughs\]

**Eddie Zane ski:** Yeah, that one is really hard to --

**Adam Staravia:** "Sorry about that. Can I send you a bottle of gin, or commiserate with you?"

**Eddie Zane ski:** Yeah... We do have plans for that though. So we have been working on trying to get that in.

**Adam Staravia:** What is your day like with issues? How many hours a day, either directly in issues, or procrastinating, do you spend on issues?

**Jerold Santo:** \[55:57\] Procrastinating... \[laughs\] Wow. What a call-out.

**Eddie Zane ski:** Yeah. So - surprise, Kubernetes isn't my full-time job.

**Adam Staravia:** Okay...

**Jerold Santo:** Oh, I thought it was.

**Eddie Zane ski:** No. I used to work on the EKS team at Amazon. So I would spend most of my days on Kubernetes, and now I do stuff with supply chain security, and some other projects, like sig store. It's an OpenSSL project.

**Jerold Santo:** Yeah.

**Eddie Zane ski:** But yeah, so we have a bug triage once a month that we go through, where we'll go through as a group... And the idea behind this was that knowledge transfer, where we can talk through the history and the context that people don't have. And we invite lots of new people. So if you're listening, and you want to get involved, join us for our bi-monthly, our once a month bug scrub. We have bi-weekly SIG meetings...

**Adam Staravia:** You went from twice a week to every other week, to once a month, real quick.

**Eddie Zane ski:** I have a Kubernetes meeting every Wednesday. So bug triage is once a month, and then our general SIG meeting is twice a month.

**Adam Staravia:** Gotcha. Okay.

**Eddie Zane ski:** And so join us for that. It's github.com/kubernetes/community, and then the SIG CLI folder right at the top, it has meetings... So it's all public agenda, and it's all recorded, so... 9am Pacific time.

**Jerold Santo:** Cool.

**Adam Staravia:** There you go.

**Jerold Santo:** Well, thanks for talking to us, Eddie.

**Eddie Zane ski:** Yeah, thanks for having me, you all.

**Jerold Santo:** This was fun.

**Adam Staravia:** It was a blast.

**Eddie Zane ski:** Let's play Zelda...

**Jerold Santo:** Let's play Zelda.

**Eddie Zane ski:** That was awesome, guys.

**Jerold Santo:** Yeah, man...

**Eddie Zane ski:** Thank you so much.

**Jerold Santo:** That was fun.

**Break**: \[57:16\]

**Adam Staravia:** Where should we begin?

**Jerold Santo:** Apr.

**Adam Staravia:** Apr. Let's begin with Apr.

**Baron Schneider:** Alright.

**Adam Staravia:** Open source, CNCF, graduated...

**Baron Schneider:** No, not yet.

**Adam Staravia:** Not yet. Okay. Sorry.

**Baron Schneider:** \[59:48\] It's incubating. We will graduate at some point, but we're not rushing it. We want to make sure we get the most out of the CNCF incubating stage. Furthermore, we are doing lots of things in the CNCF, integrating with other projects... Furthermore, we really want to make sure we have this core integration with all the other CNCF projects before we graduate.

**Jerold Santo:** Okay. So yesterday you said you started Apr at Microsoft...?

**Baron Schneider:** Microsoft, yes. That's correct.

**Jerold Santo:** And you're working for them, and you built Apr as an open source project...

**Baron Schneider:** Correct.

**Jerold Santo:** And then -- well, first, what was it? And then tell that story. What was Apr when you built it then, and what happened next?

**Baron Schneider:** Yeah, so in 2018, I was at Microsoft, and I was working for the Azure CTO, called Mark Russinovich. That was an incubations team whose job was basically to look for bleeding edge technologies and come up with innovative open source technologies that could really give Microsoft a boost in the ecosystem. And yeah, I was mostly working on open source. I was contributing to Kubernetes, Terraform, a bunch of other projects along that lines... And then I met someone called Mark Russell, who today became the co-founder of my company, Diagram. And we were looking into how can we improve the lives of application developers, not necessarily DevOps or infrastructure people, on top of Kubernetes in the cloud native space? Because the ratio between the DevOps engineers and the application developer is ten to one in the favour of an application developer. We call them the silent majority of cloud-native, because if you look at the CNCF ecosystem, most of it is around how you Git Ops, and ops, and security, and supply chain, and CCD... But there's no one out there that's really solving the problems of like core distributed systems challenges. And this is why we came up with Apr as this core tool that developers can use to focus on their business logic, and not distributed systems issues.

**Jerold Santo:** Okay. A core tool so developers can focus on their business logic and not distributed systems problems, is that what you said?

**Baron Schneider:** Yes. Yeah.

**Jerold Santo:** What are the distributed systems problems, and how does Apr deal with them?

**Baron Schneider:** So for example, as a developer you have to make sure that your application is first secure, and second of all reliables. And that usually translates into a lot of boilerplate code that you as a developer need to write on your own, to basically make your application more secure wherever it's running. And Apr will basically give you the security and reliability features out of the box, immediately.

And then you have to write state, you have to manage state at scale; you might be writing to Regis, or Dynamo DB, or Cassandra, or Google Firebase. But if you have multiple services running the same data all at once, you're probably going to want something like first write wins, or last write twins. And you're going to have to do Pub/Sub, and leader election, and config management, and secret management, and all of these infrastructure things really add up, when all you want to do is focus on your business logic so that you can ship your feature out and get your next promotion, right?

**Jerold Santo:** Right.

**Baron Schneider:** And so Apr really gives developers these APIs that give them all these Pub/Sub async eventing paradigms and service-to-service invocation and stateful management paradigm so they can focus on what matters most of them.

**Jerold Santo:** So would you describe it as a framework, or a toolkit, or...?

**Baron Schneider:** Yeah, I think a framework is a good definition of it. It's an API that you call, so it doesn't compile into your code. It's a sidecar architecture. So there's a process running next to your application, you talk to it via HTTP or gRPC, which makes the app really inclusive, because if you're a developer coming from Python, Java, C\#, Rust, whatever language, as long as it can talk HTTP, it can talk to Apr.

**Jerold Santo:** Okay. And so there are a bunch of client libraries probably for different languages that talk to Apr?

**Baron Schneider:** Yeah, there are. They make the development experience nicer. But if you want to, you can just drop into HTTP and gRPC directly.

**Jerold Santo:** Sure. Alright, so I have my business logic, and then it's calling over to Apr and telling Apr to store some data, give me some data...

**Baron Schneider:** \[01:03:40.01\] Yeah. Handle state at scale for you, do Pub/Sub between services... Yeah. But then the nice stuff for ops people is that no matter where you're running, you can basically tell Apr to work with the infrastructure of choice for your team. So Apr doesn't replace a state store, or a Pub/Sub, or a configuration store. It actually has this component model concept where you can plug it in to work with whatever database or Pub/Sub or secret store your cloud's running. So we have 100 of these community-contributed components that we maintain, and as a DevOps person, you can say "Hey, if I'm running Google Cloud, I'll have Apr work against Firebase", running on-prem, it'll work against Regis, and as a developer, you get really consistent API. So in a multi-cloud environment, you write your code once, and can basically configure Apr to work against whatever infrastructure you're running.

**Jerold Santo:** That sounds cool. Is there like a Apr stack? Is there like a default set of "These are the plugs that we recommend you plug in", but you can plug in whatever you want?

**Baron Schneider:** Yeah, you can basically plug in whatever you want. So that's a perfect question. We have the concept of a pluggable component. So for example, if you are using Apr to talk to some proprietary system that you can't contribute upstream back to Apr, we have a way for you to write that plugin and run it on your own. But we also have maturity levels. So we have alpha components, beta components, stable components, and we recommend people use stable components for production. Other than that, you're free to do whatever you want. Apr will make sure that all the best practices are really encapsulated in the API calls for you.

**Jerold Santo:** So how did Apr escape Microsoft? Or how did you escape Microsoft with Apr, or...?

**Adam Staravia:** ...was there an escape at all?

**Jerold Santo:** Or maybe you just left?

**Baron Schneider:** Yeah, so Apr was open sourced first in October 2019. It really picked up. We have a lot of end user adopters today, from IBM, to Microsoft, to Alibaba Cloud, NVIDIA... And NASA is running Apr in outer space as we speak, by the way.

**Jerold Santo:** That's cool.

**Baron Schneider:** I think that's the coolest use case of Apr.

**Jerold Santo:** That's got to feel good, right?

**Baron Schneider:** Yeah. It's like the ultimate edge deployment, which is nice. And so it really picked up, we saw a lot of community contribution... Then we decided that we're going to give it to a foundation, because we want to really make sure that it grows and that we bring other vendors in, and other companies. So it arrived in the CNCF, and we were, I think, the first or second project to make it straight into incubating. We skipped the sandbox phase, because we already had a lot of end user adoption, a lot of contributions coming in... And yeah, since then, the project really took off, and at some point VCs basically came up to me and were like "Hey, you know what - how about you \[unintelligible 01:06:13.26\] Microsoft? We think there's going to be good business here." And I basically told all of them no. So I was focused on my career at Microsoft, and Mark, my co-founder of Apr and Diagram also, which is our company, was also busy having Apr really take off the ground.

And a year later, we were having a hallway conversation, we were like "Look, we think Apr can have a much broader future, and we have our own vision for distributed systems and where this can go, and this needs to happen outside of Microsoft." So yeah, we basically started Diagram.

We left Microsoft in very good terms. We're still very friendly with all the people there. Microsoft is doing an awesome job on the project. They're contributing to the project, along with Alibaba and Intel; they're the main contributors who are on the Apr steering committee, alongside us, Diagram. And yeah, it's been a fun ride.

**Jerold Santo:** It's pretty cool to be able to start a project inside of Microsoft, work on it at Microsoft, for Microsoft, donate it -- or not even donate it. It's not the right word. When you CNCF something, is it donated?

**Baron Schneider:** Yeah, it is donated.

**Jerold Santo:** It is the right word.

**Adam Staravia:** It's the right word, yeah.

**Jerold Santo:** Okay, donate it to the CNCF... And then start a company around it that builds on it, or around it, or for it after that, as a startup...

**Adam Staravia:** Managed. It's a managed version of it.

**Jerold Santo:** Yeah.

**Baron Schneider:** Yeah.

**Adam Staravia:** That's a beautiful world, man. You were kind of saying no for a while.

**Baron Schneider:** \[01:07:41.21\] Yeah, for a long while I was so focused on building Apr into Azure Services, like Microsoft managed services. They have a service that integrates Apr, so that's what I was working on. And I always thought I would be like an entrepreneur, and start my own company at some point, but I didn't see it coming at that point in time, so I told the VCs "It's not for me right now." But some of them persisted, and in the end we took it and went.

**Jerold Santo:** So what turned the no into the yes? Was it a deal you couldn't turn down from a VC? Or was it your partner that was like "Come on, let's do this"?

**Baron Schneider:** It was a combination of things. I think mostly we saw Apr really take off, and we figured out yes, there can be a business model, especially around helping enterprises operate it on Kubernetes. Kubernetes is a complex piece of software to operate, and so we really saw the struggle of developers operating Apr on top of Kubernetes, and we knew we had something to give there. This is not something we could have done with Microsoft.

But also, ultimately our vision is to come out with a distributed systems API platform that developers from serverless platforms, and really platforms from all types of compute can leverage. So it's like serverless Apr. You can run it outside of Kubernetes, you can run it wherever you want. And to do that, it needs to be multi-cloud, and so that was another reason why we thought we'd leave Microsoft and started with our own company. We really want to build our vision of distributed systems through the Apr APIs.

**Jerold Santo:** Okay. What year was that, when you started Diagram?

**Baron Schneider:** It was January 2020.

**Jerold Santo:** So a year ago plus, and change.

**Baron Schneider:** Yes.

**Adam Staravia:** There are some nice logos here. You've got IBM Research - this is for your company, Diagram. IBM Research, Intel, Microsoft... Hey, it makes sense. You did that integration. Alibaba Cloud, Huawei, Bosch, Ignition Group, Tencent... I mean, these are major enterprise players.

**Baron Schneider:** Yeah. And there are a lot of other players who have not come out as public adopters yet. Really, some of the biggest names in the industry. And what's fascinating about Apr is that it was adopted by the tech-savvy enterprises before it was adopted by startups, for example. And you usually see it the other way around.

**Jerold Santo:** Yeah.

**Baron Schneider:** As a company offering commercial products on top of Apr, we're not complaining. That's worked out really well.

**Jerold Santo:** That sounds great for you guys. Why do you think that was? Is it because it solves enterprise-scale problems, or...?

**Baron Schneider:** Yes, I think startups, what's most important to them is to make sure that they deliver on their business, which means they want their infrastructure to be as reliable as possible. So they're not as likely to take on new bets on new technologies. But enterprises, on the other hand, they have resources, and they look at new technologies as a way to go to market faster, reach go to market faster, and really outpace your competition. So they're much more open to new tech. And I think also it's coming from Microsoft really gave it like the enterprise stamp that made people feel really comfortable adopting it.

**Adam Staravia:** For sure, yeah. Why is it important to have a managed version of Apr?

**Baron Schneider:** Yeah, so if you're running on Kubernetes, for example, you need to manage Apr yourself. And as an as a developer, you just talk to the Apr APIs. It's easy. But as an ops team, it's really difficult to babysit the control plane. On Kubernetes, every type of technology that has a control plane that manages a data plane, like a service mesh - you know, Into, Linked, Consul - Apr is no different. It's really troublesome, it's a lot of cognitive overhead for infrastructure teams.

**Adam Staravia:** For large teams.

**Baron Schneider:** You need to upgrade, downgrade, do certificate renewals, monitor, observe the infrastructure... So we basically do it for you, and we take all of that pain away for you. And then the other products we're coming out with is serverless Apr, so using Apr outside of Kubernetes on whatever compute platform you want: browser, WASM, Edge, Google Cloud Run, AWS, Lambda... Whatever computer you're running on, you'll be able to use Apr.

**Adam Staravia:** Is it a problem of scale that makes you want to go managed, or is it -- like, if I'm a small team with, let's say, a three-node Kubernetes cluster... Is managing Apr, myself, my ops team - not a big deal, right?

**Baron Schneider:** Yeah. If you're a small operation, then managing Apr yourself will probably be something that \[unintelligible 01:11:44.16\]

**Adam Staravia:** Right. It's once you go too much, much bigger. Huawei size, IBM Research size.

**Baron Schneider:** \[01:11:53.24\] Well, slightly smaller than that, too. We have perfect end users for Diagram, like Sharper Image, for example. They're a midsize company. They wrote their own application platform, and they replaced it with Apr internally, because they wanted to really \[unintelligible 01:12:06.29\] something that was standard. And they're a five-person development team, I think, and they're using our services to manage it, because they're a small team. They want to focus on their business logic. They don't want to focus on managing Apr. So this also helps smaller teams.

**Adam Staravia:** Yeah. Can you speak to the reluctant founder journey, to some degree? You said you eventually wanted to be an entrepreneur, you just aren't sure when... And speak to the "I have this open source project, I incubated, or I am incubating inside CNCF." Why incubate or donate to the CNCF? What does that benefit the project? Can you speak to all those details, for those listeners out there who are thinking, "I'm you, I'm a version of you at some point? I may do something like this." Why did you take this route? Why does this donation make sense, and this whole route make sense for, I guess, your journey?

**Baron Schneider:** Yeah. So we donated Apr to CNCF while we were at Microsoft. And the main reason why we did that was to really gain new contributors. Apr had a lot of contributors, but being vendor-neutral is something that's really important. If it's a project that spins out of Microsoft, or AWS, or Google, and it remains under their proprietary licenses or control, then users of other clouds might not feel so much inclined to take a bet on it... Because they will go like "Oh, it's a Microsoft thing, or it's an AWS thing, or it's a Google thing." But when you're doing it with CNCF, you get this vendor neutrality, and you gain these new audiences of contributors who are coming in from every walk of life; every cloud platform or technology that contributed to your project. So your end users grow, your contributor audience grows, and people see that this is really something that can adhere to many users, from many cloud platforms. We didn't want it just to become an Azure thing.

**Adam Staravia:** So the primary benefit is vendor-neutral.

**Baron Schneider:** Yes.

**Adam Staravia:** And new contributors, because you're seen as a level playing field, no bias...

**Baron Schneider:** Correct.

**Adam Staravia:** ...no corporate overlord necessarily...

**Baron Schneider:** Yeah.

**Adam Staravia:** Okay. How has that benefited Diagram? How has that benefited your company in terms of commercializing this open source, your journey to get venture-backed funding? How has that helped in all ways the business angle of -- has it been a lot easier, I suppose, to go this route?

**Baron Schneider:** So there are a lot of commercial entities that back open source projects that are not CNCF projects. I can name many. But I think the one major benefit of being in the CNCF was looking at the contributor growth since we joined, because Apr picked up a lot of new contributors ever since we joined in. When you pick up new contributors, eventually it translates into end users, which translates into new business. So yes, that makes commercializing it easier. You have to spend less time working on the open source project than you would have if it wasn't in CNCF, because you get this awesome power of the open source contributions helping your project... Where otherwise we would need to like fund a really, really large team to work on open source.

**Adam Staravia:** Right. What's the license of Apr itself, and is there anybody else who can do a Diagram?

**Baron Schneider:** Yes, everyone can.

**Adam Staravia:** Could Jerold and I be like "Hey, we're leaving here today, and we're going to compete."

**Baron Schneider:** Yes, you can definitely do that. Apr is Apache 2. That's mandated by the CNCF. So all CNCF projects are under an Apache 2 license, which is very flexible in how you commercialize it. You can do whatever you want, you can start your own service around it, Apr and any other project in the CNCF.

**Adam Staravia:** So you're competing on, I guess, your ability to do the managed service the best, right?

**Baron Schneider:** Yes.

**Adam Staravia:** So if somebody competes with you, they have the same Apr core, or whatever it might be. They can spin up a version of that. Now, it wouldn't be cool necessarily to do that, but they could. It's possible.

**Baron Schneider:** They could. Yeah, definitely. And we welcome competition. Look what's happening with Argo. It's a CNCF project that picked up a lot of traction \[unintelligible 01:15:49.03\] there are multiple companies trying to commercialize it today. Microsoft is commercializing Apr. I actually built Apr into a managed service, so I kind of in a way created some of my own future competition... Which was pretty cool; you know, the Microsoft people are great, and competition is good, because it makes everyone better...

\[01:16:10.05\] But yes, we believe that in Diagram, because Mark and me, my co-founder, created the Apr project, and we're core maintainers of the project, and we're also on the Apr steering committee, alongside Alibaba, Intel and Microsoft, then we have a very good overview into the project, and we have a very good understanding of the technical aspects of it.

**Jerold Santo:** But you didn't name yourself Apr Inc.

**Baron Schneider:** Yes, yes. We didn't. For two reasons. One is - well, a legal requirement. We can't, because Apr is under trademarks of CNCF. So that limits you. But even if it didn't have that limitation, we still wouldn't do that, because we don't want to tie the fate of our company to one single project. At some point Diagram will eclipse Apr. Apr is an amazing framework, helping a lot of developers out there today, and we will be invested in it for as long as the company lives. That's a promise to anyone out there listening to this... But we will also want to give our own take about distributed systems that might not necessarily have something to do with Apr. Our goal at Diagram is to make application developers more successful whatever they're doing, and Apr is one way of doing it. There may be others. And so we yeah, we named ourselves Diagram because that's an architectural term that helps buildings be built faster and more reliably. And that's what we want to do - we really want to enable architectural patterns for application developers to be better.

**Jerold Santo:** Is there a parallel to Apr, or a comparable that people may know about?

**Baron Schneider:** Yeah, so Apr is really polyglot, in that you can talk to it from any language. I think if you look at individual programming languages, you'll find equivalents, like Spring, for example, for Java. Or Spring Cloud. So it's like a Java framework that gives you all of these developer primitives. It's like Apr for Java. And you have Micro for Go. Yeah, those are the immediate two that I can think of.

**Jerold Santo:** Okay. That helps. So are there drawbacks to the polyglot style, versus -- I mean, I'm sure there are, but HTTP works pretty well, so...

**Baron Schneider:** Yeah, it does. I mean, if you're writing an extremely low-latency application, Apr might not be for you, because you still have an extra network \[unintelligible 01:18:18.26\]

**Jerold Santo:** Right.

3:And so if you're writing a trading application, and you need microseconds of latency, Apr might not be a fit for you. But we do believe that in terms of performance, it's good for 90% plus of use cases. Another reason why Apr might not be for you is if you need really, really specific features from like Kafka or AWS or Dynamo DB, because Apr is an abstraction layer on top of this infrastructure. In many cases, it adds features that you don't find on top of these cloud services, which is really helpful, but in some cases, you won't find the feature that you're looking for. So if you need something really esoteric, Apr might not be the best fit.

**Jerold Santo:** That makes sense. The lowest common denominator across what you're trying to do.

**Baron Schneider:** Yeah.

**Jerold Santo:** Cool. Anything else? Future? Is the project mature in terms of feature set, or is it like you've got huge plans for Apr? Do you feel like it's kind of done?

**Baron Schneider:** We have huge plans. We've recently added workflows, which is really nice... So a workflow as code type of programming model where you can tell your code "Hey, sleep for 100 years and then kick off this process", and that'll be reliable and secure. And we're adding cryptography APIs, blob streaming APIs, document store APIs, SQL APIs... There's a whole world of APIs getting added to Apr. We have eight today, and we're going strong on 12, I want to say, in the next year.

**Jerold Santo:** Awesome.

**Adam Staravia:** Very cool. Thanks, Baron.

**Baron Schneider:** Thank you for having me. Thank you.
