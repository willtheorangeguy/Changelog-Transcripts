**Gerhard Lazy:** So I've attended the last Rubicon virtually - this was Rubicon EU - and I got the impression that the biggest trend then was EPF. Everybody was talking about it, and some were calling it "the JavaScript for the kernel", "Kernel 2.0", all sorts of references. How do you think about EPF, Liz?

**Liz Rice:** So I've also heard that idea of it being -- it's expressed as EPF is to the kernel what JavaScript is to an HTML page, in that it makes it programmable. Kind of interesting analogy, but it kind of makes my brain hurt, so I find it easy to just think about the kernel.

So what EPF allows us to do is to run custom programs that we load into the kernel, and we associate them with events. And because there are so many different types of events that we can attach our programs to, and because they're in the kernel, there's only one kernel per host, so these programs have access to pretty much everything that's happening on the entire machine, and that makes them incredibly powerful and incredibly useful for observing what's going on, security, and of course, networking as well. So yeah, I'm very excited about EPF.

**Gerhard Lazy:** \[04:15\] That was exactly my impression as well. I really like this idea where we have all those containers running on this host, and then you have many hosts... But still, when it comes to the hosts, why is this particular set of containers struggling? What is going on there? Networking is such a big issue, even today. I think things are getting better, but I remember 3–4 years ago it was like the Wild Wild West in the world of Kubernetes. IP tables? Oh, my goodness me. Don't get me started.

**Liz Rice:** \[laughs\]

**Gerhard Lazy:** Yes... So I think EPF is making things a little bit more visible, a little bit more understandable, and that helps.

**Liz Rice:** And we can skip past those IP tables by just --

**Gerhard Lazy:** Yes...

**Liz Rice:** ...we'll just ignore that. We'll just use EPF instead, and that does lead to some genuinely measurable performance improvements, which is really nice.

**Gerhard Lazy:** So when it comes to the end users, what is the EPF helping them with? Understanding things, networking? Is there something more to it? I mean, that's at the surface. If we peel back the first layer, what do we have underneath?

**Liz Rice:** So I think one thing to be clear about is that although a lot of us as engineers are getting very excited about EPF programs, and I love to talk about "Hey, let's write an EPF program", in reality, most people are not going to need to write EPF programs themselves, much like most of us aren't involved in kernel programming, but we use the kernel all the time. And I think we're increasingly going to see tools that build on EPF primitives, if you like, and offer us really useful abstractions. There are lots of different projects in the CNCF that are starting to do that, and I'm sure we're going to see some more coming forward.

There's a history of observability in particular using EPF. Brendan Gregg has been doing amazing work for several years with all these different command line tools you can use to measure, get metrics on pretty much everything that's happening across your system. But until recently, that's all been very command-line driven, quite low-level. How many TCP packets have been dropped is a very useful question to be able to answer, but sometimes you want a higher-level abstraction, and I think that's why we're seeing a lot of the innovation, in this bringing EPF power and capabilities into tools that are at the kind of levels that answer questions for end users.

**Gerhard Lazy:** Okay. So I know that one tool that you're very familiar with is Cilium, and I'm wondering where does Cilium and EPF meet, because end users - I think they would know more about Cilium features and what that helps them do, see and understand, and less about EPF specifically, the technology that Cilium makes use of.

**Liz Rice:** Yeah, so Cilium has always made use of EPF. It was originally created as a networking project that uses EPF to create that network plumbing between different end points in your system. And I think probably a lot of users just know it as a Kubernetes CNI. But it's actually a lot more than that. It's also offering sort of CNI with lots of bells and whistles, so things like observability, being able to look at network flows, network policies, so giving you security enforcement at a network level... And increasingly, some of our roadmap features take it to the next level with things like EPF by service mesh, which I think service mesh is a really great example of something whereby running code in the kernel we don't have to instrument each individual application, and that's a big benefit; it's going to make things much simpler for people to deploy.

**Gerhard Lazy:** \[07:58\] So does Cilium -- I know that it exposes all these metrics and all this visibility into what is happening under the hood, especially from a networking perspective and from a communication perspective... But Cilium - what are the components in the Cilium product, or project? ... I'm not sure how you want to call it. Because obviously, there's the CNI, and there are other things. What are the big components that make Cilium?

**Liz Rice:** Yeah, so when you run Cilium, you install a Cilium agent on every node, and if all you want is networking capabilities, then that gets you going. You probably want to start being able to see those network flows, and to do that, you'd install a component called Hubble, which collects this network information, and the Kubernetes identity is associated with it.

So if you look at Hubble flows, you can see traffic flowing between different Kubernetes pods. And then there's also a Hubble UI which pulls that flow of information, brings it into a much more sort of human-readable form... For example, showing you a service map, and showing you how traffic is flowing between these different Kubernetes services. And maybe there are issues. You can see the packets that are being dropped within that UI. So that's very useful in terms of debugging a network issue.

**Gerhard Lazy:** What about when it comes to alerting, monitoring, that side of things? ...when there is a problem, you being informed that "Hey, there's a problem." Is there such a component, or would you integrate Cilium with something else for that capability? What does that story look like?

**Liz Rice:** Yeah, you'd integrate that with something else. I think a lot of people will push the flow data into some kind of sim for example.

**Gerhard Lazy:** But I'm thinking about, for example, packet loss. There's a lot of congestion, or lots of retries, whatever the case may be. Is there a way to monitor or to consume the Cilium metrics, I'm assuming, and then have alerts?

**Liz Rice:** So you can absolutely get the metrics into Prometheus, or showing Grafana... There are some beautiful screenshots in the -- I can't quite remember where I saw them recently, but just this whole series of amazing Grafana graphs that you can use to diagnose your network.

**Gerhard Lazy:** Okay. I'm not sure whether you can tell by now that I'm really interested in trying Cilium out for real, in a production environment. I really am. And I'm trying to figure out what the components are.

So my next question would be "Where would you recommend that I start? Do I take the Helm chart, is there an operator? What does the Getting Started look like?

**Liz Rice:** So there are a few different options... There is a Helm chart, there's a command-line tool, the Cilium CLI, which makes it as simple as installing the CLI, and then "cilium install", and "cilium Hubble install" if you'd like to add that...

**Gerhard Lazy:** I like that Getting Started. Oh, yes.

**Liz Rice:** It does really make that Getting Started experience nice. Also, if you want a helping hand, we're just about to start a series of weekly install fests. So the idea is to have a session with someone who's experienced in Cilium, they're kind of guiding you through the process, and it'll be interactive, so that if people have issues and questions, they can get help along the way. So that's kicking off -- I think our first one is either this week or next week, but there's a new feature on the Cilium.io website to book your place on one of those install fests.

**Gerhard Lazy:** I love the sound of that. I wasn't expecting for that answer, but that's amazing. That's exactly what I'm looking for, so thank you, Liz, for thinking ahead of time...

**Liz Rice:** \[laughs\]

**Gerhard Lazy:** This is perfect. Okay, I really love where this is going. So I'm thinking of watching you code live, which is at the top of my list for this Rubicon. It's one of the must-do for me at this Rubicon, to watch you code live. Can you tell us a little bit more about that? Where the idea came from, how do you intend to do that, what are you intending to cover...

**Liz Rice:** Yeah, so I've done a few talks about EPF programming... There's lots of different frameworks and libraries that you can use, and you can write your user space code in different languages, like Python, and Go, and Rust now as well. My Rust isn't quite up to doing live-coding in that myself, but... \[laughs\]

**Gerhard Lazy:** \[12:10\] What do you use for live-coding?

**Liz Rice:** I typically use either -- Go is kind of my go-to language, but for ease of demonstrating a lot of EPF capabilities, I'll quite often use the BCC framework, which supports Python. That's also very easy to read in a live coding environment. And occasionally, I've done some that you see. Because the kernel programs, the EPF programs that you're actually running in the kernel, that are typically written in C, can now be written in Rust, so I'm going to have to up my Rust game... But because the kernel part is often written in C, a lot of EPF programmers are also comfortable in that language, and I'm therefore writing the user space part in C as well.

**Gerhard Lazy:** Okay. And what would you like to cover in those sessions? Which is your step number one, step number two? What do you tend to cover in those? I haven't watched one, but again, top of my list, as I mentioned.

**Liz Rice:** Yeah, so the kind of step one is usually Hello World. I think that's step one in any programming scenario. And running a little program in the kernel that will just trace out Hello World in response to perhaps a system call, or perhaps a network event. And that's very easy to set up.

Then maybe we go down the direction of "How do we get information in and out of the kernel? So there's a concept in EPF called maps, where there are shared data structures, so that we can parse information between EPF programs, or into user space, between kernel and user space. Or maybe we go in a networking direction. I did a virtual office hours yesterday, where I did some -- live-coding maybe is... I made my life easier in yesterday's virtual office hours by having some pre-prepared code and sort of commenting and uncommenting things out... But it's all running live, so... \[laughs\]

**Gerhard Lazy:** I think that's the best way to approach it, if you think about it, because live coding is about going through it and explaining to users "This is what this does." It's less about typing. I think that's the least interesting part. And it's how we think about things, and how we start structuring things... I think that is really, really helpful. But yes, I will -- do you have a live coding session today?

**Liz Rice:** Yeah, I've got one 6:30 UK time today, and another one tomorrow that I think is a little bit earlier, but I've got to check my calendar...

**Gerhard Lazy:** Okay, okay. Great. Thank you for that. Okay. So I know that this Rubicon - one of the things that you do is you have a talk, cloud-native super-powers with EPF. I know that it's really late for you - 12:30 you said? I was looking... So I intend to join and keep you awake.

**Liz Rice:** Oh, thank you...

**Gerhard Lazy:** How are you heckling? Do you like heckling?

**Liz Rice:** I love heckling. I love questions. \[laughs\]

**Gerhard Lazy:** Okay, great. So that's what I intend to do. That sounds good.

**Liz Rice:** Fantastic.

**Gerhard Lazy:** I know that Duffle Cooley recently joined you... What's it being like working with him? And by the way, hi, Duffle, if you're listening.

**Liz Rice:** Yeah, Duffle is great. We're so pleased that he's joined us at Covalent. He's in L.A. at the moment, so he and Dan, our CEO, are our kind of on-site presence, and then most of the team are kind of involved more remotely. But yeah, we're super-excited to have Duffy; he's such a great -- he's got so much experience in networking as well. I've always sort of known him more on a security and obviously Kubernetes background. It turns out he has loads of networking experience as well, so... He's fabulous to have on board.

**Gerhard Lazy:** Okay. Do you get to pair with him, or just bounce ideas off? What does working with him look like? I know that you have live shows with him, I know about that... What happens outside of that?

**Liz Rice:** Yeah, so we are eight hours different, so that makes it a little bit more difficult to collaborate than ideal, but... Yeah, we're definitely figuring out some of the ways that we want to tell stories, doing Echo, which is our livestream; that's a lot of fun to do together... Yeah, it's a delight to have him in the company.

**Gerhard Lazy:** \[16:05\] That sounds great.: Speaking about Rubicon - I know that you'll be remote, virtual... I've seen even your Twitter tagline change; I'm thinking of doing the same, but it's a great idea. "I'll be at Rubicon, but virtually. So I'll be there, but you won't see me, unless it's online." What are you looking forward to the most at this Rubicon?

**Liz Rice:** Well, I'll be completely honest, I'm very much looking forward to the project updates announcements about new projects joining the CNCF. That's only in about an hour away from now, so... Keep your eye out for a project that we know and love becoming a CNCF project.

**Gerhard Lazy:** Hm... I'm looking forward to that. Okay. By the way, this goes life I think in about two weeks, so the announcements that you want to make, you can, because it's going to be post-Rubicon, so... If there's anything like that, it's fine.

**Liz Rice:** In that case... \[laughs\]

**Gerhard Lazy:** Go on.

**Liz Rice:** I'll trust you. It's only an hour away, anyway. It's not even secret, but we officially announced today that Cilium is becoming a CNCF incubation-level project, so... I'm excited about that...

**Gerhard Lazy:** Yes...!

**Liz Rice:** ...as a Cilium person, and I'm excited about that as a TOC person, because it means we've got networking finally on the landscape. We've got a couple of sandbox projects, but we didn't have anything that was really production-hardened filling that kind with C&I box on the landscape... So I feel like that's a really nice box that we're ticking from a CNCF perspective, and obviously, hugely exciting from a Cilium community perspective.

**Gerhard Lazy:** That sounds amazing. Wow, okay... Right. I mean, you've just added another big reason why I want to do certain things... But okay, okay. Let me not get ahead of myself. I always do that, I get too excited. I mean, this sounds great; I'm really looking forward to that, by the way. So for the people that can't attend Rubicon in person, like you and me, what would you recommend? How would you recommend that they feel part of it without actually being there in person?

**Liz Rice:** For me, I find that the interaction, even if it's chat, is what makes me feel connected to people. And also, if you're attending a talk and there are speakers, speakers love getting questions. It shows that you're paying attention. So don't be shy, type those questions in. Or if you are able to be there in person, ask questions. And I also think, although it can sometimes be a little bit difficult to take the leap into turning your camera on in some kind of hallway track event, but if you're tempted, even slightly tempted, it can be so rewarding to get into a video chat. Sometimes there'll be virtual office hours...

I think for us, in our timezone, most of the first social hallway track events are likely to be in the middle of the night, so maybe I'll be getting less of that this time, but...

**Gerhard Lazy:** Yes, that's right.

**Liz Rice:** And get into Slack... There'll be loads of people watching. Every time I go on Twitter and I see a photo of someone, I'm thinking "They're in L.A., and I'm kind of jealous." But I also know there are lots of us who aren't able to be there... So we're all in the same boat, and I'm sure we all chat to each other, whatever timezone we're in.

**Gerhard Lazy:** That's right. Slack does help, I have to say. Rubicon EU, I know just in our timezones, that made some things easier... But it was still virtual, so we had to adapt to that. So having Slack helped. Happy hours, the impromptu, ad-hoc sessions, where a bunch of us would get together, whether it was four or five of us, and we were talk - that would really help to meet people that you would normally meet. And it was like, I never had a bad conversation, even though people that I'd met for the first time. So that was a good experience.

I think the virtual office hours - that is a great idea. Conversations like these help, and more of this happening live would help for sure... But I think we're all trying to figure this out, and we don't expect it to be permanent. I mean, it's now -- I think this was an unfortunate situation, because from November I know that U.K. and much of Europe can go to the U.S., so it was just bad timing, I suppose.

**Liz Rice:** \[20:05\] Yeah... Although I hope that we do keep some of this virtual element going, because I see there were a lot of people who, for financial reasons or commitment reasons - you know, there were many reasons beyond Covid why people can't necessarily make it to an event. So I think if we can maintain some of the virtual elements, I do think that brings more people in. And it won't ever be quite the same as being there in person, but it is still an opportunity to connect.

I was actually going to say, the platform that they're using this time around seems quite good for... Certainly, when I did the virtual office hours yesterday - it works. You can have conversations with people. So yeah, we're getting there.

**Gerhard Lazy:** That is a very interesting perspective, and I do have to say, it makes a lot of sense, especially for, as you mentioned, people for which travelling is difficult; it is a considerable financial investment for many attendees, and it just opens up. We have so many more people joining this wonderful community that I don't think they would have the opportunity otherwise. So in a way, it is a blessing in disguise, and I think I did talk about this at some point... But I forgot about that, and you're right; so thank you for reminding me.

**Liz Rice:** \[laughs\]

**Gerhard Lazy:** So as we are preparing to wrap up, I'm wondering if there is anything interesting happening for EPF, or Cilium in the next six months that you would like to share.

**Liz Rice:** Well, I guess we've started off with those weekly install fests so that's our kind of initial -- I mean, I think from a feature roadmap perspective there are some pretty interesting things coming down the pipeline, and in particular I think kernel service mesh... In general, I think the whole service mesh space is pretty confusing right now, and I think we are all seeing some evolution in the different products that are out there, and Cilium is definitely going to be a big part of that story.

**Gerhard Lazy:** Okay... Well, I didn't need any more reasons, but I go them, to watch this even more closely and try it out myself, and try running it in production, just to see what's it like with some significant demands with traffic, to see how it holds up, to see what it shows us. I'm really excited about that, so...

**Liz Rice:** And if you do have any questions or issues, the Cilium Slack community is super-helpful, so jump in there and let us know how you get on. We want to hear.

**Gerhard Lazy:** That's another great tip. Thank you, Liz. Thank you very much for making the time; it's been an absolute pleasure, thank you.

**Liz Rice:** Thank you for having me.

**Break:** \[22:32\]

**Gerhard Lazy:** So out of everyone that I spoke to so far then, you're the first one that you're at Rubicon in person... So tell us what's it like for everyone that couldn't make it.

**Dan Magnum:** Yeah, absolutely. Well, first, it is incredibly nice to be able to see folks that I haven't been able to see in a number of years... And also some folks that I'd never met in person before. So regardless of the whole situation with Covid and all, I definitely feel very privileged to be here, and I don't take that lightly.

In terms of comparing to previous Rubicons, I've actually been mostly to virtual Rubicons, just because we've been in this pandemic stage for so long. I did have the opportunity to go to Rubicon in San Diego in person, which obviously you remember, because we recorded a great podcast episode there... And it definitely feels different from that. The CNCF has done an incredible job of making this a very safe environment with their health and safety protocols, so that's been very impressive in terms of spacing, in terms of making sure everyone's comfort levels with being close to people or being in proximity of others is adhered to. That's been very impressive. There's absolutely less attendance than there has been at past Rubicons, and one of the things I've noticed is there's a lot more just community members here, rather than end users, I'd say, which has pros and cons. It's always really nice to talk to end users, because they're the folks that really motivate product roadmaps, and CNCF project roadmaps, and that sort of thing, and it's really valuable to hear from them... But it's also really nice to be able to collaborate with other projects. I've been spending a lot of time talking to other maintainers, talking to other companies, seeing what they're up to, talking about different integrations that could be possible... So it's a different feel, but its unique atmosphere I think is really advantageous in some respects.

**Gerhard Lazy:** That sounds great. So how did you make it work, Jared? Because I know that you're remote, but you have the virtual office hours... How did you make those work? Did they help? How did that feel for you?

**Dan Magnum:** Yeah, it's actually kind of interesting... I was just kind of thinking about it and reflecting a little bit while Dan was answering... I live in San Diego, so I'm actually fairly close, in proximity to where Rubicon is being held, in Los Angeles... But then my schedule ended up getting booked up with so many virtual commitments that it didn't make it super-possible to go up there and then do everything all at the same time.

So the CNCF did a good job in organizing this and making all the virtual events possible, to kind of be inclusive and make sure that as a hybrid event people are getting opportunities to participate either in person, but also back at home, wherever that may be.

So the virtual office hours that we'd run yesterday was quite successful, with a lot of people joining in, a lot of questions being asked also... So the ability to connect with people virtually and not feel left out from the in-person event running on is working quite well, and everyone's still feeling, as far as I could tell, pretty connected and getting lots of chances to participate, which is perfect.

**Gerhard Lazy:** Were there any questions that really stood out to you? ...something really memorable, that made you think, or something fascinating that you weren't expecting?

**Dan Magnum:** There were a lot of good questions yesterday. One of the things that I realized too is that while I'm presenting and questions are flooding in, it's perfect to have multiple people there, to be able to support and answer questions and do that asynchronously in addition to the ones we answer on camera... Because there's just too many questions to answer on camera, and also get through all the material.

So I was trying to focus on delivering the material, while everyone else was attacking all the questions. Dan, do you remember any specific ones that you were jumping on while I was presenting?

**Jared Watts:** \[27:33\] Yeah, absolutely. Like you said, there were a lot of really great questions. The ones that really stuck out to me... And this is something that's kind of been a point of interest for folks throughout all of Cross plane's lifecycle - that's handling of sensitive data. So with Cross plane we have two major sources of sensitive data, one of them being credentials to talk to cloud providers or external APIs, and the other one being credentials to communicate with the infrastructure that you're provisioning using those external APIs. And so some of the progress we've made around being able to supply external API credentials via secret stores like Vault, and injecting those into the file system of our providers, and that sort of thing, as well as some of the proposals around how we publish connection details to that infrastructure that comes up - it's always really exciting when you go from one conference to the next iteration of it, and you have some solutions for the folks that had questions about that the previous time, or you at least have something where you have a design for what it's going to look like... So this kind of topic areas around security, and credentials and that sort of thing was something that really stuck out to me in the questions that we got.

**Dan Magnum:** There was also a question that really stuck out in my mind, and now it just popped back in... Somebody asked "I can just go into the GCP console and in the UI and create infrastructure. Why do I need Cross plane at all?"

**Gerhard Lazy:** Ha-ha! That's a good one.

**Dan Magnum:** So the thing that really stuck in my mind is 1) hey, we could probably improve our educational content, and messaging, and really make it clearer to people what the value is. So that's an improvement we can make on our side, there's no question about it. But you know, a big point of the project is that a lot of times you most certainly don't want to be giving direct access to the cloud provider consoles to your developers and have them being able to willy-nilly create resources on their own. You want to be able to have a separation of concerns, and kind of gate the access that they get to resources there... So that is a big value selling point of the project. That kind of stuck to me, that - hey, maybe we need to be messaging that a little bit better.

**Gerhard Lazy:** Here's an idea for you... Next time someone asks you this, I think you should introduce Dan as the COO, Chief Click Ops Officer... \[laughs\] And say "We created a role." That was such a good thing. So Click Ops is real, and we have just the right antidote for it, and he's called Dan Magnum. \[laughs\] So yeah, that's a good one.

Okay, okay... This is actually something which I've been thinking about as well. I started using Cross plane to manage all my GKE clusters. It works great, I never want to go back... And not even to the CLI, which is really weird, because CLI is great, but Cross plane is better from that perspective, so I really enjoy that. And in that world, I was wondering - how can we handle secrets better? Because you know, secrets in Kubernetes by default, base64-encoded - well, sorry, that's not really secret. Anyone can get it. So that's a great one. I will definitely want to follow up on that...

But I have another thing on my mind, because San Diego was mentioned a couple of times... And I had an amazing run around the San Diego marina... So I'm wondering then - was the run in L.A. better than your San Diego one? What can you tell us about it?

**Dan Magnum:** So you're catching me at a good time... Right before this podcast I got back from the Sig Run event we had this morning, where there was about 15 of us or so that ran through L.A. And I can say absolutely that running in L.A. is not as good as running in San Diego. There are a lot of stoplights...

I had one run out to Dodger Stadium earlier this week, and that was pretty nice, but overall I would not recommend coming to Los Angeles as a destination spot for getting your runs in.

**Gerhard Lazy:** Right. So next Rubicon I'm thinking of a place where we can all enjoy running a lot more, right? Because that's the most important criteria for choosing the Rubicon location... \[laughter\] That's a good one. Do you run, Jared? I never asked, and I don't know. Do you run?

**Jared Watts:** I'm more of a person who likes to do their exercise in combination with a goal, like a direct activity... So surfing and ice hockey are my big exercise things. I just had an ice hockey game last night, so I'm having a little bit of trouble waking up this morning and feeling a little sore, a little banged up from some of the violence out there... So Dan saying he was getting back from his run this morning when I -- it's not the same morning that I have had so far.

**Gerhard Lazy:** I see. \[laughs\] Right. That's interesting, surfing. I've never tried it. I think out of the two activities, that sounds a very interesting one that I would be up for trying. So let's see where Rubicon happens next in the U.S. Is it Detroit? I've heard Detroit being mentioned. Is that real?

**Dan Magnum:** Yup. They announced yesterday -- Rubicon EU I believe is in Valencia, and Rubicon North America is going to be in Detroit, which is... I'm pumped about it, coming to the Midwest. I think that's kind of exciting, because we sometimes miss out on some events in the Midwest.

**Gerhard Lazy:** \[32:10\] I see, okay. No surfing there, I'm imagining, in Detroit, being in the Midwest...

**Dan Magnum:** I don't think so...

**Jared Watts:** I haven't heard of it as a surfing destination...

**Dan Magnum:** Concrete surfing, maybe. \[laughter\]

**Gerhard Lazy:** Yeah. Or Valencia. That's a good one. Okay... Yeah, that's more for like yachting, I suppose, or something like that. Okay. So let's talk about the big news. Cross plane was announced for incubation status, was it a few weeks ago before Rubicon? That is huge, and I'm wondering what changed for you? What changed for Cross plane day to day, as a project, with it entering the incubation phase? Jared, what do you think?

**Jared Watts:** Yes, the incubation thing is definitely something that I put a lot of effort into, with the due diligence, and making sure that the proposal is really covering all aspects of the project... So I've got a good finer on the pulse in terms of the project growth, and the maturity, and all that sort of stuff.

So one thing that's kind of interesting is that it is a bit of a long process, so the vetting and diligence is pretty thorough... Which is a good thing, because that's how you -- you know, projects that make it to this level are given a stamp of maturity, and the ecosystem as a whole can have confidence in them that they're mature, and that they're reliable, and they check a certain set of criteria...

So the process was a long thing, so it was a bit of a rolling experience there, where if the project is still maturing, and while we're almost at incubation but not quite... So with the announcement itself though, we absolutely saw a new influx of adopters and users coming in to check out the project. Looking at some of the metrics and stats, the graphs for GitHub stars, or Slack members etc. went vertical for about a week or two, which was really cool to see that - you know, hey, we've made some inroads and we built a community. But there's more people out there to reach, and the CNCF is helping us do that with declaring the project more mature, and making a lot of noise about it...

Day to day how the project is run is not changing, because the governance is there, and the project release processes and all this sort of things is pretty healthy and really well done... So that doesn't change. But the influx of people coming, and more people to try it out, and the community continuing to grow because now they feel it's mature enough to do that is really encouraging to see.

**Gerhard Lazy:** Right. What about you, Dan? What makes you most excited about Cross plane reaching incubation status?

**Dan Magnum:** Absolutely. Well, Jared touched on a bunch of great things there, and Jared absolutely loved this effort, and a ton of effort and work went into it... So we're very appreciative to all of that he put in, and just let us sit back and work on the project. But kind of building on some of the things that he already mentioned, one of the things that I really love about Cross plane being an incubating project is a lot of folks that I talk to now, who are new folks that I'm meeting, at least have some sort of baseline knowledge of what our mission is, which allows us to kind of get to more advanced conversations faster.

I absolutely love talking to folks who don't know anything about Cross plane and want to hear about the big-picture vision, and that sort of thing... But we can really kind of get down to brass tacks and talk about more tangible things when folks come in and already have a little bit of an idea of what we're trying to do... And that gives us ideas as maintainer about "What do folks need to take this to the next level, and that sort of thing?" I think just that visibility has been a huge Boone for us already.

**Gerhard Lazy:** It's crazy that -- I remember 2019, when we started talking about Cross plane, this new thing... Some people had heard of it, but it was still very new. It took -- I'm not sure at what stage you were at then, but now you're incubating... There was a sandbox stage? Were you in sandbox back then, two years ago, 2019?

**Jared Watts:** We weren't even part of the CNCF at that point, in our first conversation...

**Gerhard Lazy:** Okay... When did you join the CNCF, by the way?

**Jared Watts:** In June 2020.

**Gerhard Lazy:** Okay... So it took about a year and a bit to go from sandbox to incubation.

**Jared Watts:** Yeah, exactly. We started the process to apply for incubation probably March of this year, so it was about nine months or so that we started getting serious and putting the proposal out there, and then the process itself took about six months.

**Gerhard Lazy:** \[36:06\] Yeah. I think that in my mind explains a lot about the level of busyness that I've seen, and the level of activity... Because even before then, I can imagine this must be a really thorough process, as you mentioned, for a good reason... And it's great to see this journey that you're on. I mean, 2019, as you mentioned, not even part of the CNCF, but you were there... Almost like, "Oh yes, that was there, and I wanted to use it since then." I'm finally using Cross plane, and I love what I see there, so I have so many questions... And I'm sure that many more people will have many more questions.

Which is the best way of, first, finding out about Cross plane, starting to use it, and then once you get a bit more intermediate in the Cross plane usage, what do you do next? What does that trajectory look like in your mind, Dan?

**Dan Magnum:** Yeah, so a lot of folks start off with just coming to our getting started guide, and getting introduced to what that looks like... And one of the decisions we've made in our Getting Started guide is to incorporate some of our actual more advanced concepts early on. And when I'm talking about more advanced concepts, that's mostly our composition engine and our packaging. And despite introducing these earlier, because they are tools that are used to build abstractions, folks actually get a nicer interface to using Cross plane right off the bat. They're able to use these advanced concepts without actually understanding all the little bits of it.

So usually, folks will go through that process, and in our Getting Started guide we have an abstraction of a database and show how that can create an RDS instance on AWS, or a Cloud SQL instance on GCP, all from the same spec, from the actual resource that you're creating in your Kubernetes cluster.

So generally, what folks will do is they'll go through that process, and they'll start to kind of see the bigger picture. And then honestly, a lot of the way that folks continue to dive into the project is, number one, looking at some of the content that we've put out there on YouTube, and that sort of thing... Victor joined Upbound and the Cross plane community and has been putting out some great content around that... And then also just our Slack workspace has exploded over the past six months or so, and there are countless folks in there just asking questions, learning more about it.

One of the really rewarding things to see as a maintainer is community members helping other community members. Because you know, earlier on it was mostly community members coming along and asking maintainers questions, and then answering those, and that didn't scale super-well. Now that we have end users helping each other use Cross plane and talking about what features they'd like to see, what things worked for their organizations, how that would affect others - that's really where we see folks really get into the weeds of Cross plane and start to understand how they can extend it for their specific use cases.

**Gerhard Lazy:** Yeah, building that community is super-important. I know that is such a huge and important part of what you do every day. I mean, I see everywhere - Twitter, YouTube, Slack... So much activity, and now that will only pick up. And you're right, there's a point where people have to start helping one another out, because it can't be on you, the project maintainers.

So I think that is one important thing for people listening to this, to try and help others. If you're into Cross plane and you know something - help your friend that you may not know yet, but get to know him/her, and see how you can help one another out.

One thing which I would like to say is that the GCP provider - there was a very recent version, I think 0.18 or 0.19, I can't remember exactly... That upgrade was very interesting, and I think that those things will become -- when you deprecated the GKE Cluster for the cluster, so there was like an export to be made, and then a re-import to be made... That was a fairly involved process. So I'm wondering, going forward, is that something that you're thinking about, Jared, in terms of how to make it smoother for users? Because if people will keep spending a lot of time on figuring that out or even performing it... To be honest, what I've done - I just didn't bother with the upgrade. I deleted all the clusters, removed, re-installed, because it was too involved. I tried it, but at step number five or six I said "Hm... This is just too much work." So I'm wondering how you're thinking about the continued usage and the upgrades going forward, so that users - their lives are easier.

**Jared Watts:** \[40:11\] Yeah, that's a perfect question. There are a couple of thoughts that come to mind. First is that there was a lot of thought put into that. It wasn't an easy decision of "Oh, hey, let's just make this change here and roll that out." Dan drove that effort to begin with, so he made a proposal about it, explained it very thoroughly, and gave the entire community a sense of what the situation is, with GCP having kind of a beta API that some people may want to depend on, and then a stable API which other people may want to depend on... So kind of supporting two different APIs from the cloud provider itself, with different varying levels of guarantees around breaking changes and things like that...

So Dan did a perfect job laying all that out, putting it out to the community, and then spending a couple of months actually with getting feedback and kind of understanding it. So that was a good thing there. And then Hassan did a perfect job of writing up a migration guide.

So something I learned from the Rook project - you know, storage orchestration for Kubernetes - that I'm also involved with, is that migrations are one thing, but if you don't provide any path at all for people, then that could be a failure. So there are some manual steps with that upgrade, or the migration, and having the guide to do that, to give people the opportunity - it was something I was definitely proud that we paid attention to that and had some empathy for the community to go ahead and invest in that.

And then the last comment I'll make there is that, you know, there are different levels of maturity and guarantees within the Cross plane ecosystem itself also. So Cross plane as a core project - you know, the functionality and machinery and tooling to build your own custom platforms etc, that is at a 1.0 or 1.5 almost now. That's stable, the API there. There are some guarantees around breaking changes and backwards compatibility and things like that... So we don't anticipate and haven't done any difficult migrations in core Cross plane in quite a while, and we're gonna stick to that... Unless we do like a 2.0, and that will be very explicit as well. But for the providers - they are not at that same level of stability yet, so they're still in an alpha/beta sort of phase, where there are going to be some of those breaking changes perhaps as things are being figured out and matured along the way... But we shouldn't see that in core Cross plane.

**Gerhard Lazy:** It's very nice that you've laid out all that background, because I remember looking at the issue that Dan opened - it was perfect, really well-thought-out. There wasn't a lot of engagement on the issue. Maybe that happened on Slack, or elsewhere... But I really like that I could follow the trail all the way to the source, and see "Well, this has been happening for a while. Thought has been put into this." You're right, that guide was perfect; I followed it, it worked, but I was thinking "Do I really want to do this? There's like too much stuff here, and I have to always -- like, step number 3 or 4." Then I still have to continue, there's like four others, or something like that... So I was like halfway through, and I thought "You know what - it would be easier to do that."

What I want to say is that having gone to the end, having gone to the latest version of the GCP provider, everything that I thought it would have, it had. So the new cluster resource behaved a lot better than the GKE Cluster one. So it was worth getting there. And once I had that, I found the extra properties, especially around auto-scaling, very useful. So I love seeing that. That was a great end state to get to.

So as we are about to wrap this up, anything coming in the next six months that you'd like to share with us?

**Dan Magnum:** So I'll talk a little bit about some of the future things that we have planned for Cross plane. And some of this -- you know, Cross plane, as we all know here, is a CNCF project, so when I talk about what I want to see in Cross plane, that doesn't necessarily mean it's going to happen... It's my personal desire for what happens, and my contribution to the roadmap as a maintainer. So we'll see how other maintainers and other community members feel about my proposals.

\[43:56\] One of the things that I am really interested in is our provider deployment model. Right now, the way provider packages work is it's essentially a stream of YAML, which is a bunch of different CRDs, and then it's a reference to an image that lives on a registry somewhere, or is already in your cluster, that you run, that runs the controllers for all of those different resource types that you're installing.

Now, the way that we actually set up that controller for you when you install a provider is we create a Kubernetes deployment, and that's the only way we do it right now. That doesn't have to be the case, right? The deployment is one way to manage your workload within a Kubernetes cluster; you could also create a Native function, you could create something external to your Kubernetes cluster; it could be a Lambda function on AWS that had access to your Kubernetes cluster, and you can also start to think of things as more granular than our monolithic providers we have right now, where you can think of just custom logic that you need to run that's kind of the glue between your different providers.

So those are a lot of different options, but essentially, what you can imagine there is an interface for different provider deployment models, and you can say "I'd like to install my provider, and I want Cross plane to use this deployment engine for it to set that up, and I can manage it in a certain way."

What that also gives you the ability to do is you may not manage your core Cross plane control plane, but you may manage some of the custom logic that you want to introduce into it. Obviously, thinking of a hosted control plane model you can think about that in a -- an external organization could run your control plane for you, but you kind of do that last-mile API interaction where you supply credentials, and that sort of thing, on your own infrastructure, in your own AWS account.

So thinking about some flexibility around that and some partitioning as well. Right now when you install a provider of AWS, you get all the provider types installed. You really shouldn't have to do that... So really customizing and making more granular provider installs and API extension mechanisms are something that's going to be top of mind for me over the next six months to a year.

**Gerhard Lazy:** I have so many questions to that... We are out of time, but I really want to hear what Jared is thinking about for the next six months.

**Jared Watts:** Awesome, yes. Quick thing for Dan there - you mentioned it's a community-driven project, and he has his own proposals etc. the community can always weigh in and see if there are good ideas... Historically speaking, Dan's proposals tend to be pretty well accepted and good ideas... So what he's saying there probably will be something the community likes.

So for me - I'll quickly throw in two things that I think are really exciting over the next six months. The provider coverage and the custom compositions. Provider coverage - we'll have a lot more to share about that pretty soon, but basically doing code generation to automatically generate Cross plane providers for the full surface area of c cloud provider's API. You know, AWS has almost 700 resources... So being able to have a Cross plane provider to do all of those resources and have very full coverage is very exciting, and that's coming along pretty soon.

And then the other one - custom compositions. The composition engine is fairly powerful, where you can compose together all of your resources and infrastructure, and then provide those as the high-level abstraction to developers... it's a powerful model, but then there are some things we could do to improve that. If you want to do some custom logic, or emulating, or flow control, or anything like that, we're enabling a way to do that, with the language of your choice. So to be able to extend the composition engine and be able to write however you want to, in whatever language you want to, some logic and details about generating custom compositions at runtime, which will kind of open the door to really any scenario that anyone can think of. So that'll be a nice kind of last-mile thing for scenarios that aren't really covered with the defaults' machinery right now.

**Gerhard Lazy:** Well, all I can say is please continue blowing my mind the way you are. There's a very special way that you blow my mind every single time I talk to you. This is amazing. Thank you very much.

\[47:58\] The other thing which I'd like to say is stay cool. Cross plane is really cool. Just keep doing what you're doing, and keep reconciling. I'm enjoying Rubicon, but especially reconciling. So thank you, Dan, thank you Jerold. This has been a pleasure.

**Dan Magnum:** Awesome.

**Jared Watts:** Right on. Thank you so much for having us again, Gerhard. I always love to be on this show.

**Dan Magnum:** Absolutely.

**Break:** \[48:14\]

**Gerhard Lazy:** So I know, David, that this is your first Rubicon, and I am very curious to hear what was it being like for you.

**David An sari:** It was very interesting. I really enjoyed the hybrid format of this Rubicon, because unfortunately I couldn't be there in person. I would like to go there in person, but unfortunately there was still a travel ban for most Europeans... So it was still very interesting to participate virtually, and to listen to talks, and being able to reach out people and to ask questions.

**Gerhard Lazy:** Okay. Did you slack? How did you reach out to people? Zoom? How did that work for you?

**David An sari:** Yeah, so mainly over the Meeting Play platform. When I was attending a talk, I could just ask my questions, and they got live-answered; so that was a nice experience. There was the possibility to reach out via Slack, but I didn't use Slack too much.

**Gerhard Lazy:** What about Zoom? Were there any Zoom sessions that you attended? I know that Priyanka used to do happy hour... I don't know whether she did this Rubicon, but that was one of my favourite sessions at a previous Rubicon EU, which was also a virtual one. No Zoom sessions.

**David An sari:** To be honest, I missed all the Zoom sessions. I wasn't aware that those Zoom sessions existed. Did you attend some?

**Gerhard Lazy:** Yeah. That's what I said - not this one; I attended the previous one, and that was actually my favourite part of the conference, so that Rubicon EU. This was -- I was going for a different experience. I was going more like talking to people like I'm talking to you... I attended a few talks, there were some specific ones that I really enjoyed, and I wanted just to get a bit more involved... There were virtual office hours, which I participated in a few... So I had a slightly different experience, closer to what I would have had if I had gone there in person, which I also couldn't do... So this was less of a virtual -- I tried to make it less of a virtual one for me, and more of an in-person without being there, which sounds a bit weird, but I enjoyed talking to people as much as I could, which is what happens when you're there. It's less about the talks, and it's more about the interactions, so that's what I did. I know that this was not just your first Rubicon, it was your first Rubicon as a speaker.

**David An sari:** That's correct.

**Gerhard Lazy:** How was that for you? Tell us about it.

**David An sari:** It was a lot of fun, and the experience was very good from start to end. I first applied (I think) a few months ago, directly after Rubicon Europe. I was actually listening to Ship It episode 2, where some tips were given on how to submit an abstract... So I submitted my abstract I think just two days after the episode came out, and it worked. I was lucky. And from then on, the communication went very well.

\[51:53\] There was very good content being given to the speakers on how to prepare, with checklists and deadlines, and the communication was very good from start to end. Especially Cody - he was answering very quickly, so that was nice. I pre-recorded the talk and I submitted it one month before the conference; that was the beginning of September. Then after I was very relaxed, because once I submitted the talk, I knew nothing can go really wrong. So I would just be there, the talk would play, and then I'd jump in for the Q&A... So it was a very relaxed and nice experience overall.

**Gerhard Lazy:** I attended the talk, I have to say, and I really enjoyed it, especially how quickly you're answering questions... And I think there is something unique about pre-recorded talks. Maybe the interaction isn't -- obviously, it's not the way you would interact if you were giving it in-person, and you had a connection with the audience, because... Well, you're not there, and you can't see the audience... So in that case, I think a pre-recorded talk makes sense. But the highlight of that is that you can answer questions as they come in. And it was great to see you answering some of those questions. I mean, some of them were tough ones, and not only was the talk really polished, by the way, because you could take your time to record, and re-record, and get it just right... Your video editing skills are perfect, by the way. I know that you've edited it yourself, and it was great. I really genuinely enjoyed watching it. So from my perspective as a viewer, it was great.

**David An sari:** Thank you very much.

**Gerhard Lazy:** You're welcome. During the talk, what was it like when you could -- basically, you were attending your own talk, and also you were answering questions. What was that like?

**David An sari:** So the experience was very good, and I think the talk being pre-recorded has many advantages for both speaker, but also for the attendees. Because for the attendees it is just frictionless. They have a better experience. They can ask questions live when they don't understand something, and I can directly answer via live chat. So that was good.

And as you mentioned, you can just pre-record the videos, you have multiples tries, you can edit it if you want... And to be honest, I was even having some parts of the videos which I had to edit and pre-record five times, just because the demo didn't work, for example... And it just results in a better end version, which you can then also share.

So the questions came in, and I could just answer them during the talk, and as the video was playing, I couldn't even pay attention to the video itself, because I was focusing on the Q&A part, and also the conversation thereafter was great.

My problem was a bit that my video was 32 minutes, and I had 35 minutes in total, so just 3 minutes left for Q&A. That was a bit short. But you can always continue the conversation after the talk.

**Gerhard Lazy:** So are you saying that you wish the talk was shorter, so that you would have had more time for Q&A?

**David An sari:** Yes. So if I had to do the talk again, I would shorten it by probably 3-4 more minutes, just to leave enough room for questions in the end... Because I think that's one of the most valuable parts of the talk, so that you have a vivid discussion. Because that's the most important part of a talk, the discussion in the end. It's less about us telling something to people, or teaching about a certain concept, it's more about the discussion which is valuable, so that you get feedback from the users, and you see which parts they don't understand, you see what they are interested in, the questions they ask around certain topics, or certain topics come up more often than other topics, for example.

And you even see how advanced your users are... I was a bit surprised, because people that joined didn't even know what RabbitMQ is, which made me think that maybe I should have introduced RabbitMQ even better at the start of the talk.

**Gerhard Lazy:** So I think the level at which the talk was intermediate-experienced, I believe. It wasn't a beginner talk. I also think - you're right, making it shorter is great, because there are two rules. Don't give out all the information. And I won't tell you the second rule. That's it.

**David An sari:** \[laughs\] I'm curious now... Do you hold it for the end? \[laughter\]

**Gerhard Lazy:** \[56:09\] No, I mean - there are two rules, and you only say one, right? Like, don't give out all the information; that's it. \[laughs\]

**David An sari:** Okay, now I get it. Now I get it.

**Gerhard Lazy:** Okay. \[laughs\] So the idea being that you want the audience -- I mean, that's basically what prompts the questions, right? If you tell them half the story... I mean, there's so much more than you could tell them, but what do THEY want to know? And then they come to you asking about questions that you haven't thought about... It's more about telling a user what's possible, getting users excited, making them imagine things, and then see what they do with that. I mean, was it exciting enough? What are they thinking? What do they wish you had told them that you haven't, for time reasons, for the conversation reasons...? As you mentioned, it's about the discussions. And the way you generate discussions is by making it interesting and short, and letting them decide "Well, what shall we do next?" It doesn't always work like that, obviously. You have to know your audience... But I think that's what happened here. So it was very compressed, it was very condensed, many concepts were introduced, and that's what it was meant to be. You know, "I'll give you a taste from many different things, and then you tell me what you would like to know more."

I'm wondering if maybe had you maybe spent more time in Slack, you could have continued some of those conversations there. I don't know. But what I do know is that another talk which I attended, that was Liz Rice's talk on EPF, in the talk the Q&A didn't work. We could ask questions, but she couldn't answer, and then we moved into Slack, and we had a good conversation between the different people there. It was mostly question answering, but also someone - I forget their name - added some extra information, and it was good to see in the Slack channel that conversation.

So I think that's a good idea, to say "Hey, if you want to know more if you wanna talk o me, I'll be there. Leet's hang out. Again, it's just an idea. Who know if it works out until you try it.

Okay, so what I'm hearing is that for first-speakers I think that having the talk prerecorded may be a better experience, because that's stage fright, being there for the first time, being overwhelmed by emotions, being overwhelmed by what's happening... There's too much stuff happening, right? Especially at a big conference like Rubicon. So it can be a bit overwhelming. So I'm wondering if this is a good idea of starting your Rubicon experience. How did you feel? Did you feel relaxed? What was the predominant feeling as you were giving this talk and as you were preparing for the talk?

**David An sari:** So as I started the talk, I was very relaxed, because I knew that everything was prerecorded, so nothing could go really wrong. I know that it can be intimidating when you go on stage, because if you do a live demo for example, many things can go wrong. So the talk being prerecorded is just much more comfortable for the speaker. So I could fully focus just on the questions part, and that was very valuable to the attendees.

**Gerhard Lazy:** So what are you thinking about the next Rubicon? Will you attend it in person, virtually, will you give a talk? Would you prefer to give a talk virtually, or would you like a prerecorded one? Or do you prefer to give a talk in person? What are you thinking?

**David An sari:** So if I have the chance to go to a conference in person, I would go there in person, because it's really about meeting the people. For me, a conference has two sides. The first side is really learning something, hearing talks, and having technical conversations, and the second part is meeting people and getting to know contributors to other projects. And that second part came a bit short for me this Rubicon, just because it was virtual. So for the Europe Rubicon next year, I'll try to go there in person.

**Gerhard Lazy:** Are you thinking of giving a talk, or submitting one?

**David An sari:** I would like to.

**Gerhard Lazy:** \[01:00:04.16\] So if the talk - let's imagine that it gets accepted. Are you thinking of giving it in-person, or prerecording, as you have this time?

**David An sari:** The next time I would give it in person, just to also practice.

**Gerhard Lazy:** Yeah. So what I'm looking up here - I just wanted to confirm because I sometimes get his name wrong. So there's this person that I admire when it comes to public speaking. His name is Matt Abrahams, and he gave a couple of talks about memorable communication, even wrote a book, a very good one - small one, but important one - Speaking Out Without Freaking Out. He had a TED talk, and he has a couple of great talks online, on YouTube, about how to make your communication memorable, how to deal with anxiety while giving talks publicly... Or there are different types of talking where you prepare, and the ad-hoc ones would just happen... And that really helped me to become a more confident speaker. So it may not work for you, but I would recommend checking it out and see if there's something valuable there, that relates to you. So that's what I would say. It helped me, and it may help you.

Cool... So what did you enjoy the most about this Rubicon?

**David An sari:** I enjoyed most that there were so many different tracks that I could choose from. The whole ecosystem is very wide. I think there were around 8, 9 or even 10 tracks in parallel. There were a lot of topics and talks to pick from, so that was a very good experience.

**Gerhard Lazy:** So it was a variety. Yes, it is a big conference, you're right. It's one of the biggest ones I know, and it's just so diverse. I love the diversity of Rubicon. I'm not aware of any conference that gets diversity better... And I mean diversity from all perspectives.

Any favourite talks, anything that stood out, that was memorable? ...because we spoke about memorable communication.

**David An sari:** I didn't watch --

**Gerhard Lazy:** There were too many. \[laughter\]

**David An sari:** So for me, it was quite late, since I'm in Europe... So on Wednesday my talk started at 11:30, so before that I just watched one talk, to see how things are working with the platform, and after I was too tired to continue watching talks at 1 AM. The next day I was watching one which was about a new generation of NATO, just to see how the NATO messaging system works compared to RabbitMQ. So I enjoyed watching that.

**Gerhard Lazy:** You do know that all these talks - first, you can watch them on-demand, in the platform, before they become available on YouTube. So what I tend to do - and this Rubicon this is what I've done... While I haven't watched the talks as they happened, only a few, what I've done - I would go back to the previous day, what I've missed... Because you're right, staying up until 3-4 o'clock - it doesn't really make sense. Well, at least not to me. And what I've done the next day - I would go over the previous talks, go over all of them, see if there's something that resonated with me, and if it did, I would watch parts of it, the parts that really stood out. And that was a good experience, because I could consume the talks much quicker before they become available on YouTube. So I could consume a lot more content, and content that was relevant for me. That is actually one of my favourite parts of the virtual conference, where all this recorded, and it's available as it happens. So I enjoy the platform. I think the platform enables you to consume and to connect to the conference differently. I thought that was good.

**David An sari:** What was the most valuable content to you?

**Gerhard Lazy:** I really enjoyed EPF, I have to say. Something like the whole EPF ecosystem - super, super-interesting, Liz Rice's talk, "Cloud-native superpowers with EPF." Because I just love the kernel, I just love that observability, understanding what's happening inside the kernel... That's the talk that really resonated with me; it's something that I picked up at the last Rubicon. But this one I could focus a bit more on the EPF ecosystem.

\[01:03:59.03\] I didn't even know that there's actually an EPF foundation. I learned about that at this conference. And yeah, it's just fascinating - networking, and the kernel, and performance and metrics, and that sort of thing.

My most important take-away about EPF is that it's all about kernel events. And events - I mean, I love eventing. It's a great concept. And I think the way it's implemented - the underpinnings are really solid. I can see some amazing things coming out of this.

**David An sari:** Have you used EPF in the projects you're working on?

**Gerhard Lazy:** Not yet, but all that is going to change in the next few months. So Parca.dev - that's one of the first things that I'll be setting up. And the next one will be Cilium. Cilium, with Hubble, and a couple more things... I think the level of observability from a kernel perspective is unique. I haven't seen anything like that before. And now that you mention that, I think the only utility that I've used that uses EPF under the hood was Net data, but not extensively. Only at a brief, superficial level. It's good, and it's not much different than it was before, with EPF, or since it and EPF integration, but that's the first one that I have used with EPF, now that I remember. What else would you like to talk about?

**David An sari:** One good experience was the speaker support. So there was a dedicated Slack channel, and support was answering, with a response time less than a minute. So when we asked a question, it just got flagged, and someone was saying they will look up the answer or get in touch with us. That was really great support.

**Gerhard Lazy:** Well, that sounds like VIP speaker support to me, and I'm glad that it worked so well in practice.

**David An sari:** It was, it was.

**Gerhard Lazy:** Yeah. I'm really happy when ideas like that work well out in practice, because you never know what's going to happen... But it just goes to show that Rubicon is a really well organized event. And there's so many moving parts to it... It's just crazy how much happens behind the scenes. And big props to all the organizers and to everyone that made it happen. It was difficult, because it was both in-person and virtual, and I think the combination worked really well. But next time, I'm also thinking of going in person. So Valencia, next year - I would very much like to be there. And who knows, maybe we'll meet. Wouldn't that be nice?

Okay, David. Well, thank you for making the time. This was an absolute pleasure. Looking forward to meeting you at the next Rubicon.

**David An sari:** Thank you for having me.

**Break:** \[01:06:32.18\]

**Gerhard Lazy:** I'll ask that Steven was afraid to ask - and afraid, I'm doing air quotes. What even is Sig store? \[laughter\]

**Dan Loren:** So that's a funny story, actually... That question came from a chat between me and Steven, and we were just messing around a little bit. So I was actually the one that asked that question to Steven.

**Gerhard Lazy:** I see... \[laughter\] That's historic there...

**Dan Loren:** Yeah, he has a funny habit of dropping my name off and then posting our conversations, which I love to read on Twitter. He's great. \[laughter\]

**Gerhard Lazy:** Okay, so what did he answer when you asked him that? He just didn't...?

**Dan Loren:** Yeah, so Sig store is an open source project that is part of the Linux Foundation. It's not like a lot of traditional open source projects, because there's a bunch of awesome code on GitHub and in the community, but it also has some production infrastructure that that community is operating as a public benefit for the rest of the open source world. So there's a bunch of code, which is awesome - you can fork it, you can contribute to it - but we also maintain a running copy of that code, for people to use day to day and use in production.

So it's a couple of different components, but overall, the goal of the Sig store project is to make it easy and free to sign and verify open source software.

We were heavily inspired by the Lets Encrypt model. So if you're familiar with Lets Encrypt, what Lets Encrypt did, operating a free certificate authority for web browsers... They made it so all the web traffic became encrypted over a couple of years. These have been around since the early '90s, but we just weren't seeing movement in the percentage of web traffic that was encrypted, all the websites still have that red X at the top, years and years ago, if you remember what it was like before Lets Encrypt... And then they solved the problem by making it free, easy and automated to do it. So now with one line in your Kubernetes yams now you can just get free certificates for everything... Not overnight, because a ton of hard work went in from the Lets Encrypt people... Compared to the overall timeline the internet's been around, the shift was immediate almost. We try to do the same thing for open source software.

**Gerhard Lazy:** How is this different from PGP?

**Dan Loren:** Yeah, it's a great question. So PGP has been around for a while. PGP is a bunch of open source standards for cryptographic operations. This includes things like signing, verification, but also things like encryption of files, of messages, of all of these different things. So PGP is kind of like a huge cryptographic kitchen sink, and it also provides some basic primitives for PKI and key distribution and things like that, that are pretty opinionated. I don't know if you've ever heard of key signing parties, and the PGP web of trust, and stuff like that. It's a really cool, really elegant model, that just unfortunately hasn't caught on too much today.

Sig store takes a slightly different approach. It uses some different encryption standards, some slightly more modern ones. Particularly, we really rely on things like transparency logs, which weren't really around back when PGP got started; they'd really taken off across the browser ecosystem in probably the last decade... I think it hasn't even been quite that long. But they have a lot of benefits. PGP is completely decentralized, transparency logs are slightly more centralized, but they provide some cool guarantees where there's a central operator, but you don't actually have to trust them. So you get a lot of the benefits of both worlds, where somebody can run a service for you, which is easy, everybody can find it, everybody can use it, but you don't actually have to trust that operator. The only thing you have to trust is that they'll keep the thing running. And people can make back-ups and mirrors, but they can't tamper with that log, which eliminates a lot of the problems with centralized infrastructure.

**Gerhard Lazy:** Okay. So one of the things that I always use PGP for is signing my git commits. So I'm wondering what else should I be signing, and what should I be using from the Sig store ecosystem to sign things?

**Dan Loren:** \[01:12:00.12\] Yeah, so signing git commits is a pretty important topic. There's like the git commit -S flag, which uses your PGP keyring, which is set up in your computer, to sign those commits. That integration is actually baked pretty heavily into git. There are dozens of different ways to sign things, Sig store isn't the only way either... But git is pretty coupled to PGP today. And there's actually a bunch of ongoing work with some of the Git core maintainers and some other contributors to start refactoring that, and making it so that Git can use other techniques to sign things... We're helping with that work to hopefully make Sig store also kind of like a first-class citizen in the git signing world.

**Gerhard Lazy:** Okay.

**Dan Loren:** But separately, you want to sign everything. It's kind of where we're going here in this world. Signing commits is great; they can be used to back-up and provide other guarantees about who actually authored those commits as they travel from your computer, to GitHub, to forks across GitHub, to package managers and everything like that. But that's just one link in the software supply chain. Security has been a huge hot topic over the last couple of years, and signing commits is kind of the first step. You're on a computer, you're typing code on your keyboard... That is the birth of software, as that code gets entered into your editor. So signing that makes a lot of sense.

As it gets pushed up to a repository, and it gets tagged, you want to sign those tags too, so somebody knows that the release was authorized. As those tags get pulled down and compiled into artifacts, it makes sense to start signing those, too. And that's where Sig store is starting to see the most adoption right now, in signing various release artifacts. It could be zip files, or tarballs, or more commonly today we're starting to see container images used for generic package management artifacts. One of the projects in Sig store called Cosign is dedicated to signing container images.

And the kind of cool thing is because the container image standards have gotten so pervasive, we're starting to see people cram all their things into container images that aren't even container images.

**Gerhard Lazy:** Oh, yes.

**Dan Loren:** So the WebAssembly modules have a little specification for how to store those in a container image without having a whole new package manager. So all these artifacts that come out from your build system, from your CI/CD system are very important to sign too, because there are tons of different attacks that could happen when you lose that link between an opaque binary blob in the source code repository it actually came from.

**Gerhard Lazy:** I think Go has possibly the best time when it comes to signing, because you can do it from scratch, and then you don't worry where from the scratch comes from... I think it's from scratch; it's just empty, there's nothing there... But what about when you do, for example, from Ubuntu? That happens still quite a bit. Can you use Cosign to check that from Ubuntu - not just that layer, but everything underneath has been signed? Does that exist today?

**Dan Loren:** Yeah. We're talking about kind of base images and image hierarchies and stuff here when it comes to containers, but... Yeah, a couple of things there. Go has some awesome support for static compilation as a Go binary, which means you can throw it into a container image without any of the other operating system runtime stuff. So if you do it from scratch, that's awesome; there's no base image to check, the only thing in there is your binary and some configuration. So you can sign that resulting image, and in that case there's no base image to check. And you can actually look at a container and prove that it was from scratch later, after it was built. There would only be one layer inside of that, you don't have to worry.

There's been some other recent work in the OCI (Open Containers Initiative) to start propagating a lot more metadata around. One of the issues that's been around for a while is that if you did it from Ubuntu and you threw a Go application into there, it's really hard to figure out after it was built that it was actually from Ubuntu, or which Ubuntu that was. But a couple of months ago, one of my colleagues, Jason Hall at Red Hat, finally got a new field approved in the OCI specification for a standard base image annotation. So build tools can start setting that in these JSON manifests to indicate which Ubuntu was used, where it was found, what the digest of that was at that time... And you can actually check that later, so you don't even really need to trust that tool. So it's all about kind of leaving these breadcrumbs around.

Now that we have that new breadcrumb (you know, from the fairytale), you can follow that back, and you can find the Ubuntu image, and you can check to see if that was signed by the original publisher. So this is something that just in the last couple of months has started becoming possible.

**Gerhard Lazy:** Yeah, that's really cool.

**Dan Loren:** \[01:16:02.01\] A good use case there, if you want to see that in practice, is actually something that fits right between from scratch and Ubuntu, which are the distroless base image suite, if you're familiar with those...

**Gerhard Lazy:** Yes.

**Dan Loren:** Yeah, so they're way closer to from-scratch. They have just a couple of other files you might need, even if you have a static Go application. Things like CA certificates, timezone data... A bunch of small text files that your application might need or expect to be in certain places. And those are actually built and signed with the Sig store tooling...

**Gerhard Lazy:** Interesting.

**Dan Loren:** ...and they have a bunch of other cool properties, like they're reproducible, so we have a bunch of different build systems reproducing those builds and publishing, and kind of proofs that they reproduced them... So you can look all of that up in our transparency log, and verify it all the way back to the from-scratch.

**Gerhard Lazy:** As far as I know, distroless is a concept that comes from Google... And I'm wondering, is that something that you're involved with, distroless?

**Dan Loren:** Yeah, so I started that project with one of my co-workers, Matt Moore, years and years and years ago. We kind of did it as a proof of concept, to show what some of this stuff looked like. We were playing around with the Basel tool set at that time, and we got reproducible container builds working, and it was pretty cool. He even talked at a conference - I think it was like a Frog swamp UP when we just kept playing with the repository. We didn't really expect much to come out of it.

Then a couple of years later, like it happens in open source, the Kubernetes release engineering team, so Stephen Augustus and his crew, moved all the Kubernetes-based images from Debian, or something like that, to distroless, without even really telling us. So all of a sudden, overnight, this became a piece of critical infrastructure for the entire container ecosystem, what started as like a little hobby project.

**Gerhard Lazy:** Wow. I'm connecting some very important dots right now... We don't have the time to go into this. You have no idea how relevant this is to many of the topics and threads that I have in the background. I intend to come back to this in a few months; maybe a few weeks, but I'm thinking months.

**Dan Loren:** Perfect.

**Gerhard Lazy:** But I'd like to talk about the big news right now...

**Dan Loren:** Sure.

**Gerhard Lazy:** ...and that is the Chain guard About page.

**Dan Loren:** \[laughs\]

**Gerhard Lazy:** That's one of my favourite About pages... Can you tell us the story about that? First, let me explain how it works, because I love that. So if you go to Chainguard.dev/about, and you click on the faces of the different people that are part of Chain guard, something amazing happens... And I'll let you discover that. \[laughs\] But can you tell us the story behind it, Dan?

**Dan Loren:** Sure. My version of the story is that we announced Chain guard, our new company, a couple of weeks ago. Scott Nichols, one of our co-founders, was working very hard on that website to get it set up. I can't do any kind of design at all; I'm terrible at frontend stuff, and everything like that, so I hadn't even really been paying too much attention to it... And the website went out, and it was awesome. And then everybody on Twitter just started laughing and telling all these jokes about the About page, and I had no idea what was happening. They were talking about all of these Easter eggs... And it took me a couple of days before somebody finally showed me what was happening.

Scott put in a hilarious Easter egg about my hair here that we're talking about now. If you click on anybody's faces on the About page, you get a pretty cool effect.

**Gerhard Lazy:** Okay... That is your hair. \[laughter\]

**Dan Loren:** I think it's a photoshopped, exaggerated version of my hair... But yeah.

**Gerhard Lazy:** Has the pandemic something to do with it?

**Dan Loren:** Yeah, so my hair has had a couple of phases in the last few years. But yeah, I basically haven't gotten it cut since the pandemic started. There was a brief face where -- I have a very curly hair, and I was just kind of going out like this for a while... But as you can tell now, it kept growing, and it has now collapsed under its own weight, and it has fallen down... So those pictures -- that hair is a little outdated, but it did look like that at one point in time.

**Gerhard Lazy:** That's crazy. That is my favourite part, by the way... \[laughs\]

**Dan Loren:** I think he was looking at the analytics stats for our page - because we've put an analytics thing on there - and the About page has more views than anything else on the website right now.

**Gerhard Lazy:** \[laughs\] So we'll just pile on top of that. Alright. The effect on Kim - I think it looks the best. I tried all the faces, but I think her - it suits her. \[laughs\]

**Dan Loren:** Yeah, I didn't even realize he did it for all the faces at first. I thought it was just mine.

**Gerhard Lazy:** For all of them, yeah.

**Dan Loren:** Yeah, it took me a little bit to realize the full extent of the Easter egg.

**Gerhard Lazy:** \[01:20:05.03\] Any other Easter eggs that you're aware of, that we should check out?

**Dan Loren:** Not that I'm aware of... You can ask Scott Nichols. He probably has more.

**Gerhard Lazy:** Yeah, Scott, please... Stop working on features. Give us more Easter eggs.

**Dan Loren:** Perfect.

**Gerhard Lazy:** So why do you think that the world needs Chain guard then?

**Dan Loren:** Yeah, I think we need something here. So I've been working on software supply chain security for probably the last three(ish) years, kind of full-time almost. I got worried about it a little bit before then... But yeah, I've been doing kind of nothing but that for about the last three years. The most of that time was at Google.

So yeah, three years ago nobody even understood it, the term wasn't around, nobody cared about it... We were kind of running around, telling everybody "You should be paying attention to what goes into these containers" and everybody said "Oh, we have other problems. This is fine." Until probably a year and a half ago was when things started turning around. We started getting all these reports of different open source libraries being attacked, or taken over by malicious actors... Companies started having internal attacks, insider threats... And finally, the huge one, the tipping point was the famous attack on SolarWinds, back in December of last year, the SUNBURST attack... And that kind of led to the downstream effects that all the other customers of SolarWinds had. The impact kind of led to the whole shift kind of overnight, and people saying "Yeah, we haven't been paying attention to this for years. What's going on? Let's go try to fix this."

**Gerhard Lazy:** Yeah.

**Dan Loren:** It led to government regulations, the EU is working on new standards, the U.S. government put out an executive order, calling for institutions to start figuring out what to do, and kind of change the way that we build software to fix all of this and make it more secure, leave a lot more of this kind of verifiable breadcrumbs (as we talked about) around, to make a lot of these attacks harder.

**Gerhard Lazy:** I'm really glad that the world is taking this seriously; it was high time. And thank goodness nothing worse happened... But it is obvious that we have to act fast on this, and I'm glad that you, first, are a small team of crazy people that really believe in this. I think that is the best way of driving change, and I'm glad that many other companies are paying attention.

I'm sure over the next year, next two years, this will just grow in popularity and importance, and I'm glad that someone like you is steering this. And when I tell you, I mean Chain guard.

**Dan Loren:** Well, thank you...

**Gerhard Lazy:** So I know that you're back from Rubicon now... Rubicon is over for you, at least in person. What was it like to be there in person?

**Dan Loren:** It wasn't as weird as I thought. I hadn't been around big crowds of people in a while, it's been a long time... I was at one smaller conference a couple of weeks ago and sort of warmed back up to it. It was just awesome to see the energy; I could tell the whole community needed this to get back together, set aside some time to talk about open source, and relax a little bit, as things start to get back to normal. It was exhausting though, I'll say that. Furthermore, it's a long week; those conference sessions were long days, and I think I just forgot how tiring these conferences can be.

**Gerhard Lazy:** I know that you had also Supply Chain Security Con. I almost called it Supply Chain Con. Crazy. \[laughs\] No, Supply Chain Security Con. Can even refer to it as a -1 event, which I think is important in relation to Rubicon. I really like that. How was that?

**Dan Loren:** Yeah, so Supply Chain Security Con was a day -1 event - I think I kind of made up that term. Rubicon has kind of had a long history of having day zero events, or collocated events the day before the conference. There's just been so many topics to cover, and so on, since we've had a Rubicon the organizers decided to have two of those. So the Monday of this week - the conference officially started Wednesday, but the Monday of this week we started off with a day -1 event called Supply Chain Security Con, that the Continuous Delivery Foundation and a bunch of other companies helped sponsor and put together.

**Gerhard Lazy:** Okay. So this makes me think of the coolness wall at Top Gear. I don't know if you remember that, I don't know if you watch Top Gear, but they had a wall, and they used to rank cars... And sub-zero were the really cool ones. Sub-zero was like the coolest car category they had. So -1 sounds a bit like sub-zero to me... I think there's a link there.

So as we are preparing to wrap this up, I have two more questions. Your favourite Rubicon moment, and what is coming in the next six months.

**Dan Loren:** Oh, my favourite Rubicon moment was the talk from Jon Johnson Jr. and Dan Magnum, on crazy things you can do with OCI registries.

**Gerhard Lazy:** Oh, yes.

**Dan Loren:** I can't wait until that recording gets posted, which you might have seen some of the buzz around on Twitter... They actually built a chat application. They worked inside OCI-compliant container industries. That was just awesome. They answered the actual Q&A for the talk using this chat application. So the audience was there, asking questions, and layers and container images were getting thrown around to make it all work... But that was awesome. That was my favourite moment.

**Gerhard Lazy:** Amazing. What's happening in the next six months for Chain guard, for you...? Anything interesting? Are you getting a haircut? \[laughs\]

**Dan Loren:** Probably, probably... It's getting a little long at this point. But yeah, for Chain guard we're figuring out what we're going to be doing. Getting our feet under ourselves, and just trying to stay focused and double down on the awesome momentum we've had in Sig store, and continuing to push that forward across all the different language ecosystems, and package managers, and container images around the world.

So yeah, I look for hopefully even more Sig store adoption than we're already seeing, and then starting to figure out what we're doing as a company.

**Gerhard Lazy:** Dan, thank you very much for making the time. This has been an absolute pleasure. I'm looking forward to next time, and I hope it won't be that long before we meet again. Thank you very much.

**Dan Loren:** Sure. Thanks a lot for having me.
