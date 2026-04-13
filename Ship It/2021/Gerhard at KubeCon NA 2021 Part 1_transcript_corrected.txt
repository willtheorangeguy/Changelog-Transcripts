**Gerhard Lazy:** One of my favourite talks from Rubicon in May, the European one, was Overview and State of Linked, and you all did a fabulous job... But I have to say, between you and Mate, I'm not sure who was the better one. I think it was a great, great talk. No, seriously, how is Mate doing?

**William Morgan:** He is doing great. He is doing really fantastic. He's kind of a rising start in the CNCF. Furthermore, he was a Community Bridge participant as a student, just (I think) a year ago... And then he has already risen to the levels of Linked maintainer. So yeah, he's really fantastic.

**Gerhard Lazy:** I really love that story, like him shipping code... Going from nothing to shipping code for Linked - that was amazing to see. And the enthusiasm, and the fresh perspective - all that's been great.

So in May we heard many good things, many great things about Linked 2.10. I know that Linked 2.11 is out, so what is new, in the new version?

**William Morgan:** Yeah, great question. So 2.10 was a big step, and 2.11 is even bigger. This is the first time when we have introduced policy into Linked, which means that you can now control which services are allowed to connect in to communicate with each other. Prior to 2.11, whenever you told Linked "Hey, I'm service A, and I wanna talk to service B", Linked has done its best to make that happen. It'll do retries if there's a transient failure, it'll do load balancing, it'll do all this stuff. And now with 2.11, for the first time you can say "No, A is not allowed to talk to B, unless these conditions are met."

**Gerhard Lazy:** \[04:20\] Okay.

**William Morgan:** So that's a big -- you know, for anyone who's in the security world, this is the idea of micro-segmentation, and this sort of thing becomes very important.

**Gerhard Lazy:** How do you declare that? Do you have a UI, do you have a configuration? How does that work?

**William Morgan:** Yeah, so a lot of our design principles in Linked are to allow you to do powerful things with as little configuration as possible. And the way we do that typically is by sticking as close as we can to Kubernetes primitives. So rather than inventing some new version of a service - well, we just use regular Kubernetes services; rather than inventing an abstraction layer on top of these other things - we just give you those Kubernetes objects directly.

So we've tried to avoid introducing CRDs, and I think prior to 2.11 we had two CRDs I think in total, from two years of development, or five years of development, or however you want to count it. But with 2.11 we introduced two new CRDs.

The way that it works is you express policy by using a set of annotations that you can set at the cluster level, at the namespace level, at the workload level... Or, in addition to that, you can add these CRDs that basically specify the types of traffic that are allowed. And that combination together is really elegant, because it means you can express a wide variety of things, from either a very open cluster that only has certain exceptions, like this sensitive service - you can only talk to it under these conditions, all the way to "Everything's locked down, and the only traffic that can happen is traffic that I've explicitly allowed to happen", and everything kind of in between.

**Gerhard Lazy:** Yeah. Okay. That makes perfect sense, especially from the Kubernetes' primitives side; I really like how you're thinking about that. But one thing which I really loved about Linked was the visual element - the dashboards, the graphs, all that stuff. That was amazing. So I'm wondering, from that perspective, do you also allow some customization via the UI, which then gets translated to those native Kubernetes primitives?

**William Morgan:** Yeah, so one thing we've never done, and probably never will, is allowed you to create those objects through the UI. So we've always wanted the UI to be a read-only tool that allows you to understand the state of the system. But once you get into like -- you know, you're dragging a slider, or you're pressing buttons to implement YAML... It just gets very hairy very quickly. And the security concerns, and permissions, and all that stuff. So we've kept the UI totally read-only.

**Gerhard Lazy:** That sounds great to me. That is a very wise decision, and I'm sure we'll come back to this later, another time, not today... But that sounds great. So which is your Linked top-of-the-mind item? And this can be something that you will be working on, or something that is like a hard problem that you've been working for some time, or something that you're excited about Linked, which is outside this release or outside the features... Which is your top of your mind?

**William Morgan:** Yeah, so for me, I think it's a theme more than anything else... And it's a theme that we didn't really expect when we were first starting to develop Linked, but it's one around security, around especially security of the traffic in your cluster.

So we came into Linked in the early days of the project very reliability-focused. Our background was at Twitter, and Twitter was constantly down, at least at the time... So our vision for what we were doing was we were going to have load balancing, and retries, and blue-green deploys, and all these reliability techniques. And what we learned early on was that a lot of the use -- I mean, some people love that stuff, but a lot of the use of Linked was for Mutual TLS. Why? Because people wanted to encrypt the traffic in transit. Why? Because either they had these regulatory concerns - "Oh, we work with financial data, and the government basically says we have to do this", or they just have security concerns. "We're running in the cloud. We don't have any control over the network. The best practice is we should maintain confidentiality."

\[08:09\] So that was like our foray into the world of security, and that theme has continued to develop through the policy features, the micro-segmentation, and onto other features, more types of policies... You know, there's a lot more we can do in this area of "How do you secure the traffic in your cluster?" And it's a blossoming area, because everyone I think is becoming a little more comfortable with Kubernetes, so the operational concerns are -- I wouldn't say they're taken care of, but they're understood. And now they're in the world of "Oh, crap... Now I can run it, but how do I secure it? How do I make sure that if one node gets hacked, that everything doesn't fall apart?" Or more likely, if someone deploys a mistake, it can't accidentally delete our users, or expose sensitive information to the outside world.

So that theme has been just developing for us over the past couple of releases, and it's gratifying not just because things like that are cool, but because people are using it, and they're getting a lot of value out of it, which is kind of like the end goal of Linked; if no one's using it -- I don't know, to me that's a little unsatisfying.

**Gerhard Lazy:** Yeah. I know that that is a very big, complicated, meaty problem to tackle, which you're not going to solve in a patch release, maybe not even in a major release. It'll take many, many cycles to get it right... And it's changing as well, with all the new rules and regulations. I know that this is something which you are passionate about, because I've seen your blog post. I've only skimmed it, the one about MTLS in Kubernetes. Furthermore, I intend to go back and read it properly. That's a good one, so thank you for that. There's a lot there.

My top-of-mind is "Can Linked 2.11 still do linked install | subject apply -f?" Because that was amazing. You can install Linked in your Kubernetes with Linked? That just blew my mind when I first saw it, and I'm wondering, does it still work?

**William Morgan:** Yup, that still works. We've maintained that. That's not typically the production deployment, because people are moving into repeatable deployments, and Helm charts, and config-as-code... But yes, that still works. I think that's still really important, because a lot of people -- believe it or not, Linked has been around for six years at this point, or something... It was the first service mesh project ever. But people are still coming into it fresh face, like "Never heard of a service mesh before, I'm trying to understand this thing, I've just learned Kubernetes..." So there's a big audience to Linked every day, where you're not ready to like Helm it up; you're just trying to play around with this thing and understand it... So yeah, that still works.

**Gerhard Lazy:** How would you recommend someone that installs Linked in production? So this is a very nice getting started, which I find very valuable, especially when I'm trying things... I love when tools are really easy to use, and this is in my perspective one of the ways in which Linked is super-easy to get started with... But how would you recommend that someone installs Linked in production?

**William Morgan:** Yeah, so what we've seen basically is people using Helm, or Terraform, or tools that allow you to do it in a programmatic and repeatable way... And I think that's probably the best practice for production. You want to be able to - especially if you're in the world of spinning up multiple clusters, or starting to treat your clusters as cattle and not as pets, you want this deploys to be repeatable, and you want to know exactly how things were set up when you come back to it three years later. So you don't want it to be in someone's terminal window, and they closed their laptop three years ago, and then they left the company, and now you're like "Hm, I wonder how this was involved" So that's the best practice.

**Gerhard Lazy:** Okay. One of the things which I've seen, and I quite liked, especially when it comes to some projects which can be a bit more involved to set up, is there's an operator which is just meant to install things, and then you apply a thing, and the operator knows how to install itself... Because then the thinking goes the operator can also automate upgrades, which I think is an interesting proposition.

**William Morgan:** \[12:02\] Yeah.

**Gerhard Lazy:** So does Linked have something like that, or is Linked thinking about something like that?

**William Morgan:** It's certainly something we've discussed in the past, and I don't think there's a reason why we wouldn't do it. Easing upgrades especially is something I'd love to do. The upgrade to 2.11 is actually pretty easy, but going from 2.9 to 2.10 was painful. Some of the configs changed, and stuff like that. I don't know that that would have been 100% automatable, but it would have been something we could assist, at least. And there are other operations too, that I think an operator would be helpful with. So yeah, we're open to it. PRs welcome.

**Gerhard Lazy:** Nice. Very smooth, very smooth. Okay. So the upgrade from 2.10 to 2.11 - is it just apply the Helm upgrade? Is that all it takes?

**William Morgan:** That really should be it. We didn't change -- there was one or two breaking changes around the mechanics of some of the multi-cluster stuff, but the majority of 2.11 is really additive... Which, again, is a theme that we try and stick to with Linked. So all the policy stuff, which was a new feature - that's all built on top of all the MTLS stuff. And all the MTLS stuff is built on top of the Kubernetes primitives of service accounts, and mutating Webhooks, and whatever else. It just kind of compounds, and you get these very nice situations where the moment you install Linked - I mean, it's awesome that you can install it really quickly, but what's even more awesome to me is that when you install it and you mesh your pods, you actually have MTLS working out of the box there, without doing any config.

If you read that long, long MTLS guide that you talked about - the vast majority of that is complicated stuff, and at the end I'm like "But you don't have to do any of that, because you can just install Linked and it does all that stuff for you." And that means that all the policy stuff can then be built on top of the identities that MTLS provides, that are cryptographically-secure identities, and it's all done in this zero-trust fashion, where the enforcement point is at the pod granularity, it's not at the firewall or the edge of the cluster... So all this nice stuff happens.

**Gerhard Lazy:** Okay. Do you have any dependency on something like cert manager, or maybe a specific Kubernetes version? What does that look like?

**William Morgan:** So for Kubernetes versions we basically try and support the most recent three Kubernetes versions... And often we'll have support for earlier ones, but it's not -- really the policy is like "Okay, the most recent three." Now, if you really have to do something with an older release, maybe we can make that work.

In terms of dependencies on cert manager - there's not an explicit dependency, but one thing you do have to figure out when you're running Linked is the certificate rotation, not of the pods themselves, but of the cluster-level issuer certificate. We have some docs on how to have that automated with a cert manager... Or you can just remember to do it. But by default, if you run that Linked install command, that generates a certificate that's only valid for a year. So you have a year then to figure "Okay, here's how I'm going to rotate it."

**Gerhard Lazy:** Right. That's a good one. Yeah, that actually catches quite a few people.

**William Morgan:** It does.

**Gerhard Lazy:** They don't think about that.

**William Morgan:** Yeah.

**Gerhard Lazy:** But maybe if you upgrade, does it get rotated part of the upgrade? Because that would solve the problem... No, it doesn't.

**William Morgan:** No, it doesn't, because -- I don't believe it does. Actually, I'm not sure.

**Gerhard Lazy:** Okay.

**William Morgan:** But in relation to this, there's also the trust certificate or the trust route, which definitely doesn't get rotated as part of an upgrade... And that also has a one-year expiration. So you know, it is easy to install, and it's easy to make things work, but like with any sophisticated piece of technology, as you push it into production, there's stuff that you need to be aware of. We actually wrote a production run book for Linked on Buoyant.io. So if you want our advice as the company that has installed Linked and helped people operate Linked in a lot of different places - and in fact, we operated it ourselves - if you want our best advice for how to install it, you can read through the run book; we talk about certificate rotation, and some other things you want to be aware of.

**Gerhard Lazy:** That's a good one. Okay, I didn't know about that. Thank you, that's a great, great tip.

**William Morgan:** \[15:55\] You've got to make sure you don't have clock skew between the nodes, because all these TLS certificates - you don't have time components, and if you've got a big clock skew, then things are not going to be able to connect, even though they should. There are details. It turns out computers are complicated; as much as we try to simplify them, there are details.

**Gerhard Lazy:** So I'm wondering, what are you looking forward to the most when it comes to Rubicon? This Rubicon which is --

**William Morgan:** Oh, for me that's easy, and it's actually not really project -- well, it's kind of project-related... It's just being there in person with other human beings. For me, that's so gratifying. I think open source can be a little isolating, because a lot of your interactions with people are. They come into the -- you know, in our case, the Slack channel, they're like "Hey, I have this problem", and then you help them fix it, and they're like "Thanks" and they leave. And then the next person comes and presents you with another problem, and you develop this kind of transactional relationship. And what you don't see in that, which you do see in person, what you don't see on Slack, does people then go off, and they deploy Linked, and they're really successful, and their company is thankful, and everything is working well... They don't come back to the Slack to say -- well, sometimes they do... But usually, they're like "Okay, cool! Now I can do the rest of my job."

But in-person, when you talk to these people, you realize there actually are a ton of people who are running Linked, it's solving big problems for them, and now they have an opportunity to come up and tell you about that. So that aspect has always been really amazing for me. And the virtual conferences, as much as I like the convenience of not having to hop on an airplane, they don't quite have this same thing. So... That's a long answer to a short question. I'm looking forward to the human interaction...

**Gerhard Lazy:** Oh, yes. Don't we all? Don't we all? I wish there wasn't a screen today, yeah. \[laughs\]

**Gerhard Lazy:** Another human that's not part of my family! Isn't that nice?! \[laughs\]

**William Morgan:** They're sick of hearing about it.

**Gerhard Lazy:** Right. Okay. So if someone's listening to this, and you are using Linked, and especially if it works, and you don't think you need to get back to William and the Buoyant team and the Linked community - that's actually wrong. Go and show a sign of gratitude. Say "Hey, thank you. This is great." Share your use case, share what you like about it. Even if everything is perfect, sharing that is worth it. People will appreciate it. And you've heard this from William, so... Do as William says, that's what I say.

**William Morgan:** Yeah. At a minimum, swing by -- if you're at Rubicon, swing by and say hi.

**Gerhard Lazy:** Yeah, that as well. That as well. I wish I could swing by, but I can't. Next one.

**William Morgan:** Next one.

**Gerhard Lazy:** If you come to Europe... Because that's where the next one will be. So anyway... For the people that can't attend Rubicon, like myself, and they'll be catching up on videos - any advice that you have for those people? How can they make the most out of it, even though they can't be there in person, and some of them are just catching up on the videos. What can they do?

**William Morgan:** Yeah. So you know, I don't know if I have great advice. My relationship with virtual conferences is not a great one... It's just a different experience. I don't know, I think like many of us, I sit in front of a screen all day, and it's really hard to want to keep doing that in any other form... But I will say, we have a Buoyant virtual booth, and we're trying to make that as fun and as interesting as possible. I'll be hanging out there... You know, even though I'm in-person at the event, I'll also be spending time on the virtual booth. We've got the run book, and a bunch of other Linked stuff... We've got an opportunity for you to get -- I think we're raffling off Linked swag... So if you visit us, you've got a chance that we'll actually ship you a hat and some shirts, and stuff.

So I don't know about the rest of the conference, but I think the Linked booth at least will be interesting.

**Gerhard Lazy:** Okay. Did you have time to check the talk schedule? Anything interesting, any talks that you're looking forward to?

**William Morgan:** Well, now I'm going to seem like a bad person, because I only looked at the Linked talks.

**Gerhard Lazy:** That's okay, that's fine. That's perfectly fine.

**William Morgan:** Yeah, we have one --

**Gerhard Lazy:** My kids are also the best, you know what I mean? \[laughs\]

**William Morgan:** \[19:43\] So there are two talks at Rubicon that I'm particularly excited about... Actually, one of them is going to be a ServiceMeshCon, which is a day zero event, which I have mixed feelings about as a conference... But there is a really cool talk there from the folks at Elk which is the largest retailer in the Nordics... And it's like a multi-billion-dollar business that everyone in that region knows about, about how they use Linked and Kubernetes to deplatform their entire company. So that one's really cool... That's Frederic, who is also a Linked ambassador, and is heavily involved with the project, so it's really awesome to see him be able to talk about what he did with it.

And then the other one that I'm really excited about is from (I guess) the other part of the world, which is the folks from Maintain Australia; they have this amazing story where they basically 10x their throughput using Linked, their entire system. They have a huge deployment through combination load balancing and some other stuff. So again, they talk about that at Rubicon proper. I think that's on Friday.

So those two things I'm really excited about, because I've been talking to these people, to both of them, for a long time, and... Yeah, I'm just really excited to get their story out there. They're both really exciting stories.

**Gerhard Lazy:** Okay. I will make sure to check them out as well. I will put them in the show notes for people to check them out if they'll be available... But that's great, thank you for sharing that.

When it comes to the people that you're most looking forward to meeting - anyone in particular that you want to shout out?

**William Morgan:** Oh, boy... Actually, I'm meeting a ton of people there... But is there anyone I want to shout out? No, I don't think so. \[laughs\]

**Gerhard Lazy:** That's good. It's too many. Let's pretend it's so many - like, no particular name comes to your mind. That's okay. That works, too.

**William Morgan:** You know, one thing that's weird is I'm going to be meeting people who have worked on Linked for a long time, who I've never actually met in-person. That part is exciting. I'm going to be meeting people who work at Buoyant who I've never actually met in-person... Even though I'm the CEO, I've never actually met them in-person, so I'm going to meet them for the first time at Rubicon. I mean, that's just a sign of the crazy times we live in.

**Gerhard Lazy:** Well, I hope everybody shows up, and everybody will be just as excited as you to meet them.

**William Morgan:** I hope so.

**Gerhard Lazy:** And happy afterwards. Like, they all want to do it again.

**William Morgan:** Yeah. Everyone will be smiling behind their mask...

**Gerhard Lazy:** Exactly, yeah. You can't see it. So yeah, if they're frowning -- well, actually, if they're frowning, you can see. But anyway, anyway... Anything interesting happening in the next six months for Linked that you want to share? Anything coming up?

**William Morgan:** Oh, boy. Gosh, I feel like we've just had all the interesting things happen at once. We had graduation happen just like a few months ago, 2.11... And now we're planning 2.12, and 2.13... Do we have anything specific beyond some really cool releases coming up? I don't know... A lot of what I've been focusing on recently has actually been on Buoyant Cloud, which is our SaaS kind of complement to Linked... And there's a free tier, so you can check it out, and you can use it without having to actually swipe your credit card, at least at small scales... And there, a lot of the exciting stuff we've been working on is how do we take all the cool stuff that's in Linked and actually extend that out, so that - you know, yes, you're getting metrics, but can we just post those metrics for you? Yes, you're getting data about which services are talking to which ones, can we draw that in a nice topology math for you? Yes, you're getting MTLS... Can we break down that traffic into these different categories? So there's a lot of cool stuff happening on the Buoyant Cloud side.

But yeah, I think from Linked - you know, a couple more releases... We're going to keep going down the path of policy... The other big thing we wanna focus on is a mesh expansion, which means running the data plane, the proxies themselves, which are these ultra-light Rust proxies - running them outside of Kubernetes... Control plane is still going to be in Kubernetes, but that way you can extend your mesh out to a VM, certain non-Kubernetes environments. Apparently, people run code outside of Kubernetes, so I hear...

**Gerhard Lazy:** Mm-hm. There is a world outside of Kubernetes. Sometimes for me, it's hard to believe as well.

**William Morgan:** It's scary.

**Gerhard Lazy:** William, this has been everything I imagined it would be. Thank you very much for making the time. It's been my pleasure, thank you.

**William Morgan:** It's been an absolute pleasure to be here, and thank you for having me.

**Break:** \[23:32\]

**Gerhard Lazy:** So the first time and the last time that we spoke it was two Rubicons ago; that's how I measure it. And when I say Rubicons, I mean Rubicon North America. That was Changelog episode 375; we had a discussion with the Prometheus core maintainers, and you were one of them... And that was 2019, as I mentioned. So what is new with you, Frederic, since then?

**Frederic Branch:** So yeah, actually, since 2019, a lot has happened. I guess I can go chronologically from that point on. So in 2019 I actually did give a keynote at Rubicon in Barcelona - so that was the other Rubicon that was happening that year - about the future of observability. That was together with Tom, who I believe you spoke to at the same Rubicon as well.

**Gerhard Lazy:** Yes.

**Frederic Branch:** So we were talking about a couple of predictions that we felt like were going to happen to the observability space, and one of my predictions was that I felt like continuous profiling was going to establish itself as an area within observability. And for that keynote I had put together a proof of concept that I very creatively called ConProf (you know, continuous profiling). It got some traction, but I never really had enough time to work on it beyond the proof of concept. Yeah, I guess at some point the pandemic probably had some part in it... Half a year into the pandemic I felt like there still wasn't enough being done in that space, I felt... So I thought to myself it's kind of now or never, and I end of last year decided to make it my full-time job, and I founded Polar Signals.

I guess because of the history of when I worked at CoreOS, and we got acquired by Red Hat, I had quite a lot of interest from investors pretty much immediately... But at the same time, I didn't feel like we had explored the space enough to take on VC money immediately, and raise money that we wouldn't know what to do with. I guess it's just me personally, the kind of person I am. I wanted to understand what I would do with money if we raised it, so...

**Gerhard Lazy:** I would like to stop you there, because this is really important, and I don't think listeners know this... Having looked at what you're about, it's not enough to observe, you have to understand. I think this understanding runs very deep for you, and I can see the connection to "You have to understand. You have to really know what you're doing", and I would like to connect these two dots, because they're important, and they will keep coming back. But please, carry on.

**Frederic Branch:** Yeah. Thank you for making that point. I think I know where you're going. So we started the company, and a perfect friend from CoreOS times, he many years ago at a Gopher Con he told me "If you ever start a company, I want to be the first person to work with you. And he kept his word. In November 2020 he joined Polar Signals. Since then, a couple more people have joined, and in February of this year we launched a private invite-only beta of our product for continuous profiling... And I guess we should talk a little bit about what continuous profiling is.

\[27:56\] Essentially, profiling itself has been around ever since programming has. When we did our research, we found it had gone back at least to the '60s and '70s, because everybody, as soon as they started programming, needed to understand what was happening with the code that they had been writing. What was using the CPU time. And especially in the '60s and '70s it was so much more precious to have CPU time. So profiling has been around for a while. There had been two problems with it - one was for the longest time profiling was incredibly expensive to do in production. You would only do it to specific processes, on-demand, because you didn't want to create too much additional overhead.

There was one thing that kind of led to us being able to do this in production and always on, and one of those things is what we call sampling profiling. So instead of tracing exactly absolutely everything a process does, we only a hundred times per second look at what the program does at that particular moment in time, and capture the stack trace of what it does... Because essentially, the stack trace represents what the program is doing, right?

So for some hyperscalers this was already enough to build continuous profiling tools for them to consume internally, because they could do it always-on in production now.

Now, as it goes with so much cloud-native technology and developments, that wasn't necessarily accessible to everyone... And one of the really amazing things that also have happened somewhat recently has been EPF. EPF allows us to capture this data at an even lower overhead, because we can already capture it in the form that we are going to consume it afterwards. We don't need to use some pre-baked format that may have a ton of information that we don't need, a ton of detail we don't need. We can produce exactly the data that we want, and make that exportable to user space, and then ingest it into our storage.

So that was definitely also a huge part of what created a movement... But this doesn't really have to do with overhead. There's also another aspect, which is just kind of Kubernetes unifying the observability space, in a way. And I think we might have talked about this in our last session, actually... The way that Prometheus also, and Kubernetes have kind of standardized a lot of terms in our industry. It just makes us all speak the same language.

This is super-powerful, because all of a sudden, when I say pod, and you say pod, we immediately know what we're talking about. So this is much more cultural than it is technological, but it means that our knowledge is transferable. So this is incredibly powerful... And then the last piece is putting all of this together, EPF with Kubernetes now allows us to automatically discover all the containers that are running in our infrastructure, and be able to look at all the CPU time that is being consumed in our infrastructure at once. And the reason why this is so powerful is that all of a sudden we can now say "This stack trace in this binary is what's causing 20% of our CPU time." If we optimize this stack trace away, we're now saving 20% of CPU time in our infrastructure. That's huge. Think of the banks, automotive companies, any company that has a large cloud bill - they can save millions of dollars with these kinds of measurements. It's just, the reality is they can do these measurements today.

**Gerhard Lazy:** \[31:38\] And it doesn't really matter what language you're using, right? Because everything runs as a pod. It doesn't matter whether it's Java, whether it's Go, whether it's Erlang... It really doesn't matter. The point being is, you run this agent on your Kubernetes worker node, where all these pods are being scheduled, and you can see out of the pods which are being scheduled, out of the containers which are running within those pods, which are the ones that consume the most CPU. And I imagine this goes beyond CPU. It goes to memory, disk operations, network operations, operations, all that nice, important stuff that the kernel knows about, and it presents to you via EPF in a way that makes sense to you, and it doesn't matter what language is making that call... Whether you have a serverless framework... It really doesn't matter. It's really powerful.

I like the way you're thinking about this. I was going to ask you, Parca.dev is the thing that you're opening up to the world at this Rubicon, and I was going to ask you why do you ARCA. But I think the answer is "To cost-optimize." But maybe there's something more to it...

**Frederic Branch:** First, I think -- and we said this in our announcement as well... I think just the people that we are and the company that we are building - I think we needed to have an open source piece to be ourselves. So even if there wasn't anything else, that would probably would have already been enough of an argument for us... But I think more importantly, continuous profiling is - even though there are now several vendors, several projects out there - in the only one year that Polar Signals has existed, right? There are several companies that have sprung up, several vendors that have created products... But it's still a really young space, and it's still not very well understood. So in a way, the open source project is also about democratizing this for the community and educating the community about continuous profiling, so that when we talk about continuous profiling hopefully in a year or two everyone understands it, like when I say distributed tracing.

**Gerhard Lazy:** So if I understand correctly, it's your need to understand what the system does, and the itch that you're scratching is you wanting to understand what is happening on those nodes. So that's why you did it. As simple as that.

**Frederic Branch:** Absolutely.

**Gerhard Lazy:** I love that. I love that.

**Frederic Branch:** The back-story actually goes a little bit further than where I started. The reason why I even went into putting together that proof of concept with ConProf was because I read a paper by Google where they described these methodologies, how they used these kinds of methods to cut down on infrastructure costs every quarter by multiple percentage points. And I was just amazed by that for several reasons. One, I just wanted to have this tool while I was working on Prometheus. And the other one was I had worked on Prometheus - at least I thought to myself, "I think I know a thing or two about working with data over time." So I think that's kind of what ultimately created the circumstances of me wanting to create a tool like this.

**Gerhard Lazy:** So I got the tool up and running in seconds. That just shows easy it is to get started. This was just local. I didn't want to venture in our production Kubernetes cluster, because I have something else in mind for that... But in a few seconds, I could access the UI, I could see the CPU time, and the UI - what surprised me is it's better than the first Prometheus one that I remember. And I think the secret to this is your coffee machine. \[laughter\] Let me explain, okay? Let me explain. \[laughs\]

When I first heard of ARCA a few weeks back, I checked it out, and it was looking good, but it wasn't as polished as it is today. Just in a matter of a few weeks, I was astounded by how fast you're iterating on it. And I think that it's your new coffee machine. Is that it? What's the secret?

**Frederic Branch:** I would say it has a part in it... \[laughter\]

**Gerhard Lazy:** Okay...

**Frederic Branch:** \[35:41\] I think the UI is actually an evolution of several attempts at it. The very first one was actually within our closed source beta product, where... You know, when we launched it in February this year, we used this to work really closely with a couple of early users to understand what is it that they -- beyond the UI even, what is it that they want from an experience from a tool like this... But then also, of course, with ourselves using this software, like how do we want to use it.

I think there's so much Gooding that was going on from basically day one, because this is a tool that we've built for ourselves. We wanted to put that work into it.

**Gerhard Lazy:** What do you use the tool for? This is fascinating. I love this story. I mean, there's a theme here... Every great product dogwoods itself. And the developers, and the product, and the entire team that works on it, uses it on a daily basis, understands the shortcomings, and fixes them, maybe even before users see those problems. I think there's a theme here. But how do you use ARCA for ARCA? This question, and the answer, fascinates me.

**Frederic Branch:** Yeah, so actually, this is a cool topic that I think we even want to run blog post series about, because I think there are just so many aspects to this that I would love to talk about...

**Gerhard Lazy:** Can we have a short answer? Because this is a short piece... But it's obvious that we need a much longer one.

**Frederic Branch:** Yeah. Basically, boiled down, ARCA itself is a really performance-sensitive software. It has a specifically designed storage and query engine, so that we can actually do all these amazing things with continuous profiling. So we use ARCA to optimize ARCA... This is kind of a vicious cycle, because we keep creating this more and more performant software to create more and more performant software, to do even more powerful things, to optimize it even further.

**Gerhard Lazy:** Oh, yeah.

**Frederic Branch:** So it's really addicting almost.

**Gerhard Lazy:** I love that. I love that. We do the same thing; I'm a big fan of that. That's it. That loop is one of my favourite loops. Amazing. So just to switch gears a little bit, and think about the Rubicon and what's going to happen this week... What are you looking forward to the most at this Rubicon? Is there something you're looking forward to?

**Frederic Branch:** I think - of course, this probably reflects my own interests quite a lot, and what we do with ARCA as well... But I'm really excited about how the EPF space is evolving into more of a production-ready state, if that makes sense. I feel like it's very similar to the first hype wave of service mesh that we had, where everybody was talking about it, but no one was using it... And then one or two Rubicons after that, suddenly there were all of these great stories about how people were actually running it and using it in really useful ways.

And so I feel like we're kind of at a turning point with EPF as well, where so many people have gotten their hands on it that we're suddenly seeing all these really incredible applications for it. So I'm really looking forward to a bunch of the EPF talks that are coming out.

**Gerhard Lazy:** Any specific talks?

**Frederic Branch:** There's one by Derek Parker who works on the Delve debugger, which is kind of the de facto debugger in the Go community. I think he's doing some fascinating things. There are even some integrations into the debugger with EPF. I find that fascinating... But the really cool thing about EPF is almost its unpredictability of what you can do with it. Because it allows us to do such wild things anywhere in the kernel, attached to any kind of event, people have come up with super-innovative things that we were able to do in the past with kernel modules, but let's be honest, nobody really enjoyed the user experience of that. And now, all of these things are being productionized, and I'm just really excited about all the possibilities.

**Gerhard Lazy:** Hm. That sounds interesting. So anything EPF-related, that's where your interest is... You and Derek Parker, did you say?

**Frederic Branch:** Yeah.

**Gerhard Lazy:** \[39:51\] Okay. I've heard Derek ARCA... Derek Parker, okay... \[laughter\] That's a good one. Park-everywhere, right?

**Frederic Branch:** That was completely unintentional... \[laughs\]

**Gerhard Lazy:** Yeah, that's what happens... And I'm imagining that you're not going to attend the conference in-person, right?

**Frederic Branch:** Yeah... Unfortunately, as much as I would have wanted to, and unfortunately, travel restrictions are still in place for Europe to travel to the U.S. But you know, there's always another Rubicon.

**Gerhard Lazy:** Yeah, it was the same for me. You're right. I really wanted to be there in person. So what advice do you have for those who couldn't attend, and will be attending virtually, and some will be catching up on the videos, because they won't be able to attend virtually because of the time difference.

**Frederic Branch:** Yeah, I mean - look, it's like, half of the world that's not able to attend this Rubicon, so you're not alone... I know there are several folks that are doing just local meetups, or local virtual meetups, or just going for lunch or something, find your local group... Or if not, just watch the recordings. The platforms have become so much better since the first time we've done these virtual conferences. Just try to be a part of it as much as you can, given the circumstances...

You know, we've got Rubicon EU coming up next year, it's at the end of the winter, so no matter what happens, that's the time when Covid cases went down anyway. I feel like the next Rubicon in EU is going to be great. A lot of us are going to be able to attend that one, if not this one.

**Gerhard Lazy:** Those are some great tips. Is there anything interesting happening in the next six months for ARCA that you want to share?

**Frederic Branch:** I think in a way a lot what we're -- we shared it really early intentionally, to understand what the community also wants from a project like this. We intentionally did not immediately release multiple types of visualizations, or we didn't immediately go all-in on a query language, or stuff like that. We do think these things are on the horizon, but it's just so much -- you're going to create something so much better when you work with a community and talk to a lot of people. It's just like creating any product... But we just feel like we owe it to the open source community, because really, the open source community has made us who we are today... So if we can give back a little bit of that, then we've achieved our goal.

**Gerhard Lazy:** Wow. That's amazing. I wish everybody thought like that... And I think most people think like that in the CNCF space, and it just goes to show... That's it - this right here is the reason why the CNCF is as successful; because people think like you do. It's amazing to see that.

The one thing which I would like to do as we are wrapping this up is I want to congratulate you on the hiring page, which I think is a baseline for others to follow. It's simple, it's to the point, it's inviting... It makes me want to find out more, and that is saying a lot. So I would like to congratulate you once again... Like, well done for striking such a great balance... And I'm sure that it's so simple because a lot of thinking went into it, and a lot of refinement... And again, I'm seeing a trend here, which I really like; that's been great to see. Thank you.

**Frederic Branch:** Thank you.

**Break:** \[43:00\]

**Gerhard Lazy:** So the first time that I've heard about COSI was at Rubicon EU in May... And in that COSI talk, Andrew and Steven did an amazing job. My concluding thought was that it made me reconsider the operating system that I want for Changelog.com... And I do have to say that while I didn't get there, I'm really glad that we have this opportunity to talk with your amazing microphone, Andrew.

**Andrew Richard:** Yeah, I have since upgraded, since Rubicon EU. I think that was with my blue baby bottle this one is the Sennheiser mph 416. This one is made for like voiceover, so... Yeah, I'm loving it.

**Gerhard Lazy:** It's an amazing sound, I have to say, and there's also something natural there, so I really like it. You know, listening to that talk, and seeing the visuals that Steven produced - they were amazing. That was a great one.

**Andrew Richard:** Awesome.

**Gerhard Lazy:** So since Rubicon EU, which is about five months now, what is new in the world of COSI?

**Andrew Richard:** So COSI proper, as far as what it is, and the GitHub org, and outside of Talos, not much has looked like it has changed. But in Talos itself, we've been implementing a lot of the ideas, and kind of using that as a proving grounds, if you will, for the idea. And it's actually working out phenomenally well. We have since rewritten our entire networking stack of Talos on top of the concepts of COSI, and it's really, really cool -- I mean, where do I even start... When you submit your configuration to Talos, the controllers just pick it up, they know when to set up bonding, they know the order in which you should set up the interfaces to get bonding going, validation on whether the particular combination of options for an interface, say, just won't work... Tons of validation around things.

We've since launched a product called Lifespan, which we could probably get into more later, but it's basically a way to do automated WireGuard. And in Talos, all you really do is you set up two little configuration, you set them enabled true, or something to that effect, and, then all of a sudden, all these nodes know how to reconfigure themselves reactively... And this is all really because of the ideas around cozy. Otherwise, we're going to be stuck with SSH, and going in and manually executing classic UNIX utilities... And sure, it would work, but it would not feel clean; it would feel very hacky. So I'm pretty proud of what the team has been doing.

**Gerhard Lazy:** First, when I looked at Talos, it looked fascinating. The getting started part - I struggled a little bit. And you know, Sider came along, and that made some things easier... COSI was fascinating, because the concepts - they were not specific to an implementation, but they were like a standard that you were trying to build, and I really liked that.

I do have to say, since trying Sider - the first one I think was 0.1, when I struggled... I haven't tried it since. Furthermore, I know it's 0.3... So even though I would love to start with this, how would I start? Where would I go with Talos? Which is the first thing that I would do? What would you recommend?

**Andrew Richard:** Yeah, so we have the ability to basically spin up Kubernetes clusters right there on your laptop, built into our CLI. I'd say that that's the easiest way. If you want to get a feel for what it's like to interact with an operating system that's API-driven and has a CLI, and doesn't have SSH, and all these things, that is the easiest way - you just do a simple command. Tell a CTL cluster create.

\[47:55\] The good news is this kind of translates really well into, say, running it on bare metal. You could literally grab that configuration file, maybe modify the networking section a little bit, turn on a machine with an ISO file, and submit the configuration file that you had running from your mock environment... By the way, which runs in Docker or QEMU. Those are probably the two easiest ways. One has a benefit of being more developer-friendly... Let's say that you're developing an application, and you want something to represent your testing or production environments closely; that's when tell a CTL cluster create is really nice, because you could just spin up a Kubernetes cluster, you've got one a minute or two later, and it matches, at least API-wise, everything that you're going to run in production. And then getting that to work in actual bare metal - that's another story. Typically, that just involves networking, and that's where 90% of all the problems happen.

So at that point, it's really just crafting the networking section, as we just talked about. COSI is going to roll those out for you; well, Talos using COSI... The easiest way to get started on bare metal, I would say, is using the ISO. After that, PXE booting. PXE booting is a whole other level, and that's where we have our Sider product, which aims to streamline that whole process and really own it for you... But that's the natural progression that I would go towards. Of course, you have the cloud in there somewhere, and right after you -- you know, that's where they diverge, right when you're talking about using the ISO or not.

In the cloud it's a little bit different. You have to have some image that's been uploaded, and all of our documentation goes through how to upload the image. In our releases we have the assets already prepared for you. You follow the documentation to upload the image into your particular cloud, and all you do really is turn it on with the correct user data.

So what I'm getting at really at the end of the day is - it just really boils down to "How do I get Talos just simply installed, or running somewhere?", whether that's a VM, or containers, or bare metal... And then it's just knowing the configuration file. In the same way that with Kubernetes I know that I have Kubernetes; do I really care where it's running? I know that I can describe my application and how it should run using declarative YAML. We're bringing that same experience into the operating system.

So getting started - it's really just grasping the idea that you just need to turn Talos on, however that may be and wherever that may be, and get comfortable with the configuration file and being able to submit and update the system.

**Gerhard Lazy:** I can see where I've been going wrong, because I usually start in the cloud, and I usually start with PXE booting. And I think that is possibly the hardest way... So if you start there without knowing the lay of the land, you went in extreme mode, so good luck trying to figure all those things out. I think this was actually even before COSI, like six months ago, nine months ago, somewhere around there. And I know that you've made strides since then, and things are clear, things are better, as you would expect. So I think that I know what I'm going to do next, and for someone that doesn't ever run Docker locally, I just like everything in the cloud, because if it's on my machine - well, how do I know it will run in the cloud? But I know that Talos makes it slightly different; even though most things it runs locally, but it will not work the same in the cloud, and that's always a friction.

**Andrew Richard:** I wanna touch on that, because I actually think that that's really important to point out, and that's actually a huge motivating factor around Talos, was because I was managing Kubernetes clusters, and the first place that I was doing this we were debating, "Should we do this with bare metal? Can we run CoreOS?" Well, typically we ran CentOS, but we're also running this up in AWS... And I wanted this consistency story. And then we also had our developers that were saying "Hey, I want to be able to actually spin this up on my local laptop and not depend on anything that you guys have set up." Even though we went to great length to give them testing environments, they still ended up just creating their own.

\[52:02\] So Talos is really beautiful in that sense, because it's literally the same image. The same image that runs right there on your laptop can be rolled out to anywhere - Raspberry Pi's, the cloud, bare metal... Anywhere that you can imagine. And the experience is going to be consistent, more or less. Obviously, when you're running in containers, you have the element of a kernel being the host operating system's kernel, and networking, and stuff like that... But that's minor. Those are things that you can kind of craft after the fact.

**Gerhard Lazy:** I feel that you've shared a secret with us, or at least with me... And now I know what I need to do next, so thank you very much for that.

**Andrew Richard:** Of course.

**Gerhard Lazy:** The next thing which I'm thinking about is why would someone want to pick Talos over, let's say, Debian or Ubuntu? What would you say to them?

**Andrew Richard:** Yeah, so this is a question we usually get. One of the main reasons that you really would consider Talos over, like you said, something like Debian, is because these things simply come with way too much at the end of the day. They come with package managers, they come with an extra set of packages that you simply don't need if all you're concerned with is running Kubernetes. In some cases you even have to do upgrades of the nodes for things completely unrelated for the purposes of running Kubernetes. And this is just unnecessary, to put it simply.

So the first point is the minimalism that you're going to get with Talos. It's only about 15 MB. At the end of the day, you're going to get something tiny comparative to everything else out there. You're going to get no package manager. We don't even have SSH or Bash. And the reason why we did things like that - or why we removed those - was because if you've ever operated Kubernetes at any scale, you've found yourself constantly duplicating work. You had to manage users, you had to manage hardening, you had to manage automation... But at two different layers. You had Kubernetes itself that you had to worry about, and then at the operating system itself.

So the whole goal with Talos is to just remove that Node element entirely, so that you can focus on just the cluster. We like to tell people that we want them to look at the cluster as one giant machine; and then nodes simply as more compute to that. So it's just more CPU and RAM to a bigger machine. We can't really look at it like that if we have to concern ourselves with who's logging on there, what if they changed permissions, automating it... This overhead simply should go away. And that's first and foremost one of the reasons why you should consider Talos.

And secondly, we have a really strong security emphasis. We recently just went through a whole exercise of actually securing our supply chain. So now everything's completely reproducible, you can get all the checksums and make sure that you're actually running the intended version of Talos. The file system is read-only. As I mentioned, Talos is only 15 MB; what I didn't mention is that it's delivered as a Squashes, which is only read-only, and there is no other way to run it. It is also completely ephemeral.

Now, Kubernetes of course needs places to write things, and there's only one place in Talos that's writeable; it's /var. At least writeable in the sense that it's going to be persisted across reboots. Of course, we have /temp and things like that, but that is completely ephemeral and only Talos uses those places.

So you're going to get a much more hardened experience. You're going to get people that can't -- you're gonna completely eliminate the possibility of people going on there and making a node a snowflake. It's really just Kubernetes that can change. So that's a huge benefit when you're talking about running anything more than ten nodes.

**Gerhard Lazy:** I know that everybody's thinking about security chain attacks, and security of everything - software, developers, signing... Can you sign everything, from your commit to the release, to the artifact, to what it runs, when it runs, so that you can trace it all the way back to the origin of the code being written? That's really, really important. I really like this minimalist story, not just from a security perspective, but that you only run what you absolutely need, and you run it with the least privileges; that is very powerful, and I think it somehow has been forgotten in the age of containers and Docker, because it was like the Wild Wild West for a long time... And I'm really glad these concerns are now coming back, because I know how important they were 10–15 years ago. So I can see the cycle; we're back where we started.

\[56:28\] So from that perspective, I know that these minimalist systems, one of the things that they replace - and I wonder if Talos does the same thing - they replace glib for something like must. And what then tends to happen is glib is a lot more hardened, battle-hardened, battle-tested, so the performance on glib of anything tends to be better. So what I've seen is weird crashes, weird degradations, weird IO performance when you don't run glib. So what does Talos use?

**Andrew Richard:** We actually use Must, and we haven't seen that at all. And I think that may largely be due to the fact that the only reason that we run must - let's see... We only have a handful really on the roots. We have Contained, and we have sprogs, and maybe some LVM tooling, and then Talos itself. So the actual C libraries that are running in Talos are practically negligible; it's practically zero. We don't even have system. In fact, our unit system is a new unit system that we're building for the purposes of these style of operating systems, API-driven operating systems. So that is written in Go. Practically, everything that we do is in Go.

So I think maybe that can be contributed to the fact that we are running must, but we haven't run into any issues. And then, Kubernetes itself, since it's delivered in containers, those containers have glib. So the role that must really plays in our ecosystem is very small.

**Gerhard Lazy:** Yeah. I always had it different. Usually, the host would run glib, and the container would run must. And then that combination, from that direction, always seemed to create problems. This was about two years ago I remember, when we were looking at RabbitMQ the image, in the context of running it at performance, at scale, what's the most you can get, and then you have the Erlang VM, so it's slightly different... But I do remember the Alpine-based images had all sorts of weird issues that the Ubuntu ones never had. But now again, this is the container image, this is not the host. So I'm really curious to try it out for myself and see what is different. Who knows, performance could even be better. Which kernel version are you using, by the way?

**Andrew Richard:** We are on the latest LTS. I think it's 510.62

**Gerhard Lazy:** Nice. Okay, okay.

**Andrew Richard:** We used to run the latest Linux kernel, and we still kind of go back and forth on what we should do... And I think we're now leaning more towards LTS, because the changes that Linux sometimes introduces just cause us more headaches, especially when you're on the bleeding edge versions of it. But the latest LTS so far has been really great for us. We've been playing with the idea of maybe having LTS-style releases of Talos, which are pinned to LTS versions of the Linux kernel, and then having more edge versions, which are running the latest stable LTS. But today, we're still playing with the overall strategy that we want to take long-term, and we just kind of settled on LTS for now, because that's kind of a safe play.

**Gerhard Lazy:** So speaking about LTS' strategy and roadmaps - anything interesting coming in the next six months? So between this Rubicon and the next one for Talos and COSI?

**Andrew Richard:** Yeah, I'd say the biggest one is this week we're announcing Lifespan, which is -- I mean, I'm just super-excited about this idea, and I haven't even explained it yet...

**Gerhard Lazy:** Okay... Yes, please... That sounds very interesting. Please.

**Andrew Richard:** \[59:50\] Yes... The idea is that, since Talos can run practically anywhere, we're finding people want to bridge, say, bare metal clusters with instances running in the cloud. And so far, there hasn't been any good solutions for this. With Talos, we're kind of uniquely-positioned; since it's API-driven, we own the whole stack, we've got COSI managing the network... And so what we did is we went ahead, and we actually wrote a tooling to basically automate the key distribution and the peer discovery of WireGuard VPN. So I can spin up a cluster right here in my closet that's running on Raspberry Pi's, and extend that out to AWS really simply, really easily... And the latency is somewhere like -- I think the latency that WireGuard adds is somewhere around a millisecond... So it's negligible. But you get this consistent experience network-wise, regardless of where you're running that particular node. Even the pod traffic can be routed over it. Kubernetes can actually be configured to purely talk over the WireGuard network.

So the idea with this long-term, the vision is that we're going to have users/customers running in the data centre, bare metal, which is a large part of our user base - all of a sudden they have an influx in traffic, and they need to expand the cluster. But they don't have the resources. Okay, fine. Let's just expand out to AWS momentarily, and when things calm down, we'll scale it back down to our core infrastructure. Or even another data centre, spill it over to another data centre.

Now, a completely different use case, but very similar, is maybe the edge. I have some Raspberry Pi's that I actually want to join up to a cluster at the core, which is hosted in AWS. But maybe these Raspberry Pi's are running in shipping trucks, and they have intermittent network connectivity. That's kind of troublesome when you're talking about running the Kubernetes control plane... But a worker - you know, it can kind of go in and out, and I think the story there could be better on the Kubernetes side... But at least using WireGuard, as soon as they get any kind of networking, whether it's some Wi-Fi when they pull up to a store, or mobile data - they can join the cluster with WireGuard, and everything just seems as if they're right there, on the same network.

**Gerhard Lazy:** That's fascinating... So let me see if I understood this correctly. You're saying that you can scale out your Kubernetes clusters on-demand, wherever, whether it's your closet, or whether it's on the data centre, or the cloud... You can maintain the same privacy of the network, everything is encrypted, the data on those workers - you think it's ephemeral data, so that you don't store any state there, so that you can scale back in... And Lifespan makes this seamless. Is that what you're saying?

**Andrew Richard:** That's exactly what I'm saying. Of course, there's little caveats, like -- the way WireGuard roughly works is you need at least one direction of communications. So in the case of, say, my private cluster running right here in my closet, it needs to be able to at least reach the workers. The workers don't necessarily need to reach it. It can establish the channel that way.

So there are some limitations within the system that you can find in the documentation stuff; over my head when it comes to networking. Something around Cones and NAT's, and stuff...

**Gerhard Lazy:** Is it IPv4, or IPv6? What network does it lay down? Or dual stack?

**Andrew Richard:** Either.

**Gerhard Lazy:** Wow. Okay, I want to try it out.

**Andrew Richard:** Yeah, you should.

**Gerhard Lazy:** I want to try out how it all actually works.

**Andrew Richard:** It's pretty neat. In fact, one of our engineers - he just created a video of him just spinning up Talos right there in Kemp, right there on his laptop, and then joined an AWS Graviton instance to it.

**Gerhard Lazy:** Wow, okay.

**Andrew Richard:** So it's pretty neat. I'm super-excited about it.

**Gerhard Lazy:** I will put that link in the show notes, because that sounds like something which I would want to try out. That sounds amazing. Okay, okay... So - shifting focus a little bit towards Rubicon and what's happening this week. First, will you be attending in person?

**Andrew Richard:** I will, I can't wait.

**Gerhard Lazy:** You will. Okay. Amazing. What are you most looking forward to? Meeting people, let me guess...

**Andrew Richard:** \[01:03:56.07\] I just want to see another human. That's exactly what it comes down to. No, actually - that is true, but more specifically, the thing that I'm really looking forward to is meeting everybody that works at Sider Labs. We've been fully remote for two years now. I think I've only met a couple of people that are currently at the company, and I just can't wait for us all to get together and just have dinner, go to the bar, whatever. Just have a good time and actually not have to worry about seeing each other over pixelated streams and audio issues. So just seeing another human is going to be really nice, and especially meeting everybody that's a part of the company.

**Gerhard Lazy:** Wow. So this is two out of three people -- actually, both people that go to Rubicon in person, you and William Morgan... You're both looking forward to the same thing. William Morgan from Linked, from Buoyant - he was saying the same thing. Meeting the rest of his company, meeting the community, and meeting another human being. He's really looking forward to that.

Okay, I think everybody's on the same page... And I have to say, those that couldn't make it in-person, myself including, we wish we could be there... But by the time EU comes along, I'm sure things will be easier, and then next year, for the next Rubicon North America, I hope to be there in-person, and meet all the great people that -- you know, Rubicon is so big; you can never meet everybody that you want to, but at least there will be fewer people this year, so it'll be a bit better for meeting in-person.

**Andrew Richard:** Yeah. And speaking of EU, we will be there as well, too... So maybe we could see each other than.

**Gerhard Lazy:** Amazing. Okay, yes. Tick! So what advice do you have for the people that can't attend the conference in-person? Anything that you recommend to them?

**Andrew Richard:** You know, nothing that you're not going to get from the CNCF as far as their recommendations go. Attend their virtual booths... I would say join the CNCF Slack. That was really fun when I did Rubicon EU; just talking to people, and all kinds of random channels... That was a blast. It did a decent job of giving me that camaraderie that you're looking for when you go to Rubicon. So I'd say that you should sign up for that immediately.

**Gerhard Lazy:** Okay. And then what about the people that want to do catch-up videos? Because for example, it may be too late in the night for them, and they can't be up all hours... Anything you would tell them?

**Andrew Richard:** Set aside enough time, because there are a lot of really cool things... And just try to prioritize. Because you're not going to get through all of them; figure out the ones that probably are most applicable to you, things you're most excited about, and just have fun watching them.

**Gerhard Lazy:** Speaking about that - which talks are you excited about? Anything in particular?

**Andrew Richard:** I've noticed my taste has changed ever since I've become into a role where I'm playing more of a management role and business role. I do get hands-on technically, but less and less overtime... So I'm finding myself gravitating more towards things like building community... There's a particular talk on how to make contributors maintainers... Building your brand, stuff like that.

Technical stuff - there is one on supply chain that I want to go look at... But I am reserving a lot of time for just talking to people as well. So I'll maybe grab a few, but they're going to be less technical.

**Gerhard Lazy:** Okay. Well, Andrew, this has been a pleasure. I'm really glad that we had this opportunity. Rubicon EU just flew by, and I didn't have time, but now I'm so glad that we had this time together. I'm really looking forward to trying Talos, to trying Sider, and seeing Lifespan, how well does it work in practice. Thank you very much for sharing all these amazing things with us.

**Andrew Richard:** Yeah, thank you for having me. It was a blast.

**Break:** \[01:07:29.11\]

**Gerhard Lazy:** So Rubicon is my favourite time to catch up with the cloud-native community, with the people, with the events, new features, new products... It's such an eventful time, Rubicon. I love it. But also new beginnings. So we only spoke -- was it like a month ago? It wasn't that long... Episode \#18.

**David Flanagan:** Yes, it was around 4–5 weeks ago I think it was...

**Gerhard Lazy:** And you have been really busy in this one month, right? So tell us about it. What happened in the last month?

**David Flanagan:** Well, we brought a new person into this world, which has been rather time-consuming...

**Gerhard Lazy:** Okay...

**David Flanagan:** I can't remember if we spoke about this during the last one...

**Gerhard Lazy:** We didn't.

**David Flanagan:** My wife was pregnant, and now we have a beautiful baby boy who's entered this world. His name is Caleb; he is two weeks and five days old... And because that wasn't enough change in a short period of time for me, I also decided "You know what - let's change jobs as well." So the last time we spoke, I was working at Equinix Metal, and I am now a developer advocate for Plum.

**Gerhard Lazy:** So I think that this is going to be my favourite announcement from this Rubicon, which is the newest and youngest member of the cloud-native community, Caleb. He's - what, two weeks? Three weeks?

**David Flanagan:** Two weeks and five days, yeah.

**Gerhard Lazy:** Well, I don't think there is a younger member of the cloud-native community. So two weeks and five days, you said... That's just crazy. Okay...

**David Flanagan:** Well, he will be watching some of the Rubicon festivities and talks remotely with me, as obviously in the U.K. we are travel-banned until November 1st... So I will be participating as much as I can through my laptop and through the video material... And I'm sure Caleb will be throwing up on me for a good few of those sessions.

**Gerhard Lazy:** \[laughs\] Or falling asleep, I would like to think... Like, during those boring sessions... Boring to him, obviously. Like, "Kubernetes what?!" He'll just fall asleep like "Spiffy this" or "Spiffy that?" Yeah, that sounds like a nice nursery rhyme. Anyway... I just thought about this - this is maybe the best strategy to shift your body clock to the West Coast timezone without actually travelling, right? Because a new baby will keep you awake through the night, so you can watch all the talks; you'll be awake. I hadn't thought about this, but this is genius, David.

**David Flanagan:** Yeah. And not is at the clock, and then you know my regular 7 or 8 hours asleep at all. So why not spend some of those times awake, catching up with some great cloud-native material, and stuff like that. It'll be good. And of course, it's Rubicon; it's been remote for the last four editions. I think this is the fourth remote one since the pandemic.

**Gerhard Lazy:** Yeah.

**David Flanagan:** So you know, the hallway track on Slack, and Discords, and Twitter... Twitter is always very active, so there's always something to keep you company during those late nights.

**Gerhard Lazy:** So which is your process of joining remote Rubicons? Tell me about it. And then I can share with you my process and see how it compares to yours. How do you do it?

**David Flanagan:** Well, I wish I could say I was really methodological about it, and I knew exactly what talks I was going to watch each day, but I don't. I really just kind of show up and log into the platform and see what's happening then and there. I definitely watched a lot of it after Rubicon, so that I could do the 2x on YouTube; I'm very guilty of 2x-ing a lot of these sessions and slowing down as required... But I do try to catch a few things live as much as possible, and it's really just -- especially with having a young one right now, my method is going to be slightly different from previous Rubicons. So I'm really just taking it day by day. We're on a DC event right now, I'm logging on, I'm going "Okay, I've got 40 minutes. What can I catch right now?" and just try to do as much as I can at the moment. But it's not as well-planned as I would expect. I'm sure you've got it down to the letter, right? You must know exactly every session you're gonna check out.

**Gerhard Lazy:** \[01:12:05.17\] Yeah, something like that... Actually, I try to drop in on all of them. I'm making use of three monitors, plus an iPad... I have a picture from the last Rubicon that I attended... And then I just like watch three sessions and I mute, and I just pick one, listen for a minute, then switch to another one, switch to another one... And that's how I just like consume three at the same time. And then when something is -- I mean, it's interesting, but maybe there's something more interesting, I just switch to another one. But I can consume three, that's my max. I think four will be a bit challenging.

When it comes to the sessions, I don't pick them ahead of time, because the titles and the descriptions can be misleading. I try to drop in on them as you would do, and then I just pick and choose. But I try to drop on all three of them, which is impossible if you're in-person... So I think this is the best way to do it virtually when it comes to consuming the talks. But what about interacting with the Rubicon, the rest of the attendees? How do you do that? Or do you even do that?

**David Flanagan:** Yeah, I do try and remain active. I'll go back to the schedule first, actually, just a little bit on that... So you're not the first person I've heard who has multiple talks running at the same time. There's that community member Notary who does four or five talks at the same time as well, and Slacking between them. I don't know how you do it. I'm a complete single-tasked. Furthermore, I don't have the focus or attention span to do multiples, so - mad respect there. But I'm always following the operations track mostly this Rubicon, as I was the chair of that track. I helped select all the talks that you're going to see.

**Gerhard Lazy:** Oh, wow. I didn't know that...

**David Flanagan:** Yeah, I don't think I've actually told anyone. I didn't really talk about it on Twitter either, but I did chair that...

**Gerhard Lazy:** That's amazing. Wow...

**David Flanagan:** I helped pick all the talks. If you don't like them, it's sadly my fault, and one other person... But it should be a pretty good Rubicon.

**Gerhard Lazy:** Right. Okay... Well, then that means that you know all the talks that are -- well, not all the talks... Like, you have a good idea of the talks that are coming, the themes, the speakers... That's amazing. Anything that you would recommend in particular? Something that resonated with you from that track?

**David Flanagan:** Yeah, I think my bias definitely helped work some of the selection. I've got an affinity for Git Ops and infrastructure as code, so there are a lot of perfect sessions that feature using Argo for deployment... You know, we've talked a bit about that last time; I think we're both fans of the project... And we're just seeing more and more sessions submitted on Argo every single year, and it's just because of the demand. People want to be able to do this automated Git Ops dev-based deployment. So you'll see a lot of sessions there.

A lot of sessions on infrastructure as code, with Terraform and Cross plane really popular this year... We've seen a lot of submissions talking about Cross plane...

**Gerhard Lazy:** Interesting.

**David Flanagan:** ...which is great to see. And of course, there are a few preliminary sessions on there from some of my new teammates from Plum as well.

**Gerhard Lazy:** I see, okay. So when it comes to Git Ops, Flux or Argo? What do you think?

**David Flanagan:** Oh, I'm so on the fence... I actually use both. I really love the simplicity of Flux; it just seems to work. But I love the Argo UI, and I wish I could merge them together sometimes. Previously I mentioned that Flux are working on the UI; it's still super-early. I don't recommend people use it yet. There are many, many bugs. But I do tend to use Flux, but I'm getting more familiar and comfortable using Argo.

I think the challenge with Argo is the custom resources are slightly more complicated, especially when you have to adopt the App of Apps models, which is an app to deploy an app, which has sub-apps... And I haven't really got my head around that completely; I'm not as fluent with it as I am with Flux, but I definitely think both tools are really great. I don't think you can go wrong with using either. I think it comes down to just whichever one you've used first, whichever one you're comfortable with. They're both great projects.

**Gerhard Lazy:** Yeah. So it's a matter of trying them, I suppose, and seeing what works for you. That's one of my favourites.

**David Flanagan:** Well, we got this announcement - was it two years ago? Maybe you'll remember... But the team -- was it Intuit who were the original creators of Argo, and Flux. They had this big joint announcement where they said "We're going to consolidate both of the tools to get this one Git Ops tool to rule them all", and it was going to be called Git Ops Toolkit... It never really happened, and now we're back to this divergence data, where we have multiple tools kind of trying to fulfill the same thing.

**Gerhard Lazy:** \[01:16:07.02\] Yeah, 2019... I was actually there, at that Rubicon, and I was so excited. That was also the North America one. And I would like to dig more into that to see why that happened. I didn't get a chance to speak to the Flux team. They're on my list, they really are... But it's like -- you know, too many things happening. But the day will come. There's a Git Ops Days, I think; there's like a summit coming, like next week, I believe...

**David Flanagan:** Maybe. I can't remember exactly.

**Gerhard Lazy:** Yeah, something like that. It's happening as well, and that will be an interesting one to watch. But I would really like to understand what happened there with Flux and Argo, and what are the strengths and the weaknesses of one versus the other. The UI - that's like a good one.

I do have to say, even though I have tried Argo, I haven't tried Flux. So this Git Ops summit which is coming, I'm hoping, I'll be able to try it out in that context. I'm looking forward to that. Okay...

**David Flanagan:** I think the Flux chain is a bit better when it comes to being a bit more agnostic on the tools you wanna use to actually generate the YAML. You know, not all of our Git Ops repositories are straight YAML manifests; we're using tools to customize are the carvel dev tools, or we're using capital. There's so much choice there. Decision fatigue is real, especially in the cloud-native landscape...

Flux makes it a lot easier to say "I want to use a tool to generate the manifest before we do the apply stage." With Argo, I think it's a little bit more convoluted. There has to be a concept of a provider, if I remember correctly... And they're not all supported. But that could have changed since the last time--

**Gerhard Lazy:** Cool. I definitely have to follow up on it, so thank you for that. Thank you, I really appreciate it. In the context of Rubicon, coming back - so there's the operations track. Any other track that you're excited about?

**David Flanagan:** All of them, I think. I'm in a really unfortunate position, which you probably are as well - we need to really stay on top of a lot of this, as well as our day jobs... And we have our extracurricular activities where we need to be knowledgeable on a lot of these domains. So I really am watching all the tracks as much as possible, and 2x-ing all the talks on YouTube. But anything to do with continuous integration and delivery is something that I'm really keen on following, talks about infrastructure as code, of course... I definitely love tools that are doing this.

One of the reasons I joined Plum is just because it directly is everything I love doing with platforms, which is taking the primitive tools that we have, like Flux, and Argo, and Kubernetes, and cloud providers, and being able to give developers a platform to deploy their application. My interest and Plum's interest are just the same there. Infrastructure as code, continuous integration, continuous delivery - those are the main things I want to see from Rubicon this year.

**Gerhard Lazy:** I would like to dig into that a bit more, because that's like the other big thing that changed in the last month for you, the new job with Plum. I think Kat Cosgrove - is she there as well, at Plum, I believe?

**David Flanagan:** Yes. Matt Stratton, Kat Cosgrove and Laura Santa maria - they are my teammates. They're the developer advocacy team at Plum, and I'm joining in with some great people there, definitely.

**Gerhard Lazy:** Yeah, a big shout-out to them. That was the first thing which I wanted to do. And the second thing is asked you, as I asked you before, "Why Plum specifically?" Why Plum? Could you see this one coming? Let's be honest, did you see this one coming?

**David Flanagan:** Of course, of course.

**Gerhard Lazy:** Okay. \[laughs\]

**David Flanagan:** I always look back at my career, and I've always worked for relatively small shops. Every time I write a line of code, I've always been responsible for the deployment to production. And I've never had that throw over the wall scenario.

So infrastructure as code and continuous integration and deployment - these are just things that I've always had to do. I've never been able to dodge that bullet, unfortunately. I think I cut my teeth like the rest of us using Terraform and HCL, and I think -- Terraform is a fantastic tool. No one's ever going to say otherwise. But it has some really rough edges when it comes to programmatically defining some elements... Like, nodes in the cluster are doing loops or conditionals... These things get a little bit tricky because of the constraints of the HCL language.

\[01:19:54.29\] Now, I know with Terraform 0.10 they started to bring in some of these primitives, but these primitives already exist in high-level programming languages, which is where Plum shines. It comes down, and it says "Well, you can just define your resource graph using the language that you're familiar with." I'm a big fan of Go, I'm a big fan of TypeScript; they're both options available to me... But Plum also supports any of the .NET languages, it supports Python, and I'm sure there are other things coming, and there's some really cool announcements that I managed to found out just yesterday coming to Rubicon...

So there's all these languages that already have loops, conditionals, the ability to provide a single Funchal's my favourite thing on Plum. So I'm going a little scar bridge but been able to say I want a Kubernetes cluster on GCP, and I want different node pools that look like this. And I want a load balancer, and I want some applications deployed to that cluster as part of the bootstrap process. Now, I could do that as an HCL Terraform module, but as a TypeScript Plum application, I can actually make that a function call, publish it to NPM, and then anyone can pull that out. You can literally do NPM install raw good Kubernetes cluster package, call that function as many times as you want, get all these clusters with everything encapsulated in that way... And I just think that is a super-power. And I think once you see that, and you start to use that approach, looking at more abstractions like HCL or YAML, you're just like "Why? Why am I constraining myself to the opinions and the subjective nature of other people that think that that's the best way to do it, when my experience may be slightly different... And programming languages are the best way to encapsulate that knowledge.

**Gerhard Lazy:** So this is fascinating, from multiple perspectives. I see a couple of products, tools, however you want to call them, enter this space in recent months... One which is top of my mind, which is, by the way, an episode that's going to ship, I think, this week. I mean, by the time you're listening, it'll be like a few weeks back... Dagger. And I really like how they're making use of CUE and Build Kit. So CUE as a language to define these things sounds fascinating... So I'm wondering, how does CUE compare to HCL and Plum? Plum in the case of Plum being the actual programming language... Versus something like Cross plane, which is supposed to be your control cluster, which then you define your compositions and your -- there's something else we have called that I forget, Compositions, and - it's not an abstraction... Do you remember what it is? There's a composition in Cross plane...

**David Flanagan:** Yeah, the XRDs. So you can actually have a single resource, but then create multiple sub-resources below it. I think they're called compositions, or XRDs.

**Gerhard Lazy:** Yeah. And there's like another name... So it's two things. The compositions are the things that you can bind them in... But they have these providers, they interact with all the IaaS's you can declare you YAML, so you declare your GK cluster in Google, and it just makes it happen, and all the other things that you want are within that IaaS, and it works across IaaS's. So I'm wondering, how does Plum compare with Cross plane? Let's start with that. And how does Plum compare with Dagger, which is using CUE, rather than a programming language.

And CUE - I mean, it is kind of a programming language, but it's more like a data language; that's the way I see it. And I know that you know a bit more about CUE with Brian Petersen. You have CUE Blocks?

**David Flanagan:** Yeah, Brian Petersen and I are the creators and maintainers of CUE Blocks. We're both huge fans of CUE. We think it's just a great language for defining schema, applying constraints, and even doing some basic comprehensions and mathematics with them.

So it's not a Turing-complete programming language, but they are starting to add more query APIs and other things to bring it in line with some of that.

So I really like Dagger... I have done an episode with Solomon on Rawhide Live, where we dug into Dagger and we did some deployments. I think it's a perfect tool, and I love seeing CUE used in this way. It's very similar to Terraform, in the regards of that you have to have something that understands the abstract form. The HCL, the YAML, or even the CUE is just compiling down to YAML at the end of the day anyway.

You're still constrained in that you can't do a lot of conditional logic. Loop logic does exist in CUE, and you can do some things like that... But then modifying things within the loop gets a bit difficult, because you've only got access to that array count. So it depends on your use case. But I think Dagger is great, and that they're moving beyond, into like where Boundary is as well. I'm not sure if you're familiar with HashiCorp's Boundary...

**Gerhard Lazy:** \[01:24:12.25\] No.

**David Flanagan:** But I think that second step is like "Okay, we provide the platform or the infrastructure, but what about the applications that then belong and live on that application?" And that's where Boundary comes in, fulfilling the continuous delivery component of your application. And Dagger kind of moves right into that and provides like a single interface to all of it, which I think is really cool. But the constraints are still there, very similar to HCL.

Cross plane things get fascinating. Cross plane still has defined -- you're still constrained by YAML. You can only see so much that is not programming, but you're not going to be able to provide a function that does a thing, but you can provide a composite resource that does a thing.

What I really love about Cross plane is that continuous reconciliation. That's something Plum doesn't do yet, as well, and it's the first thing I wanna change, and I'm going to be like "We need to get into this space."

**Gerhard Lazy:** Oh, yes.

**David Flanagan:** We have to control the actual reconciliation, and not just the client-side reconciliation. So I think Cross plane is killing it there. I don't think any other product is as good as Cross plane in that regard. The fact that I can have that controller running on my Kubernetes cluster, if I delete an S3 bucket, it's going to be recreated. Of course, there are things that can happen there that are bad; it could be data in the S3 bucket, and we have to build workflows onto it to restore it from a backup... These are not things that really happen yet. Cross plane is, and I know they are because they're a great team. Cross plane is great, they have a great reconciliation with Kubernetes event model, going to be a lot familiar with people, and they're going to be really happy with that approach. I want to see Plum do more of that, control the execution of Plum, and not just have a client-side.

And Dagger is great. Solomon and the team are fantastic. It's still not a programming language, but you can still do some really cool things with CUE. I think where Dagger is going to excel is that if something is difficult to do with Terraform, and even difficult to do with Cross plane, you have to have the provider first. Dagger has made it really easy to provide really superficial providers by just taking the queue and saying this is what I need to do. It's a very small amount of Go, there's not a lot of boilerplate, and I think we'll see a lot of adoption because of that... But hopefully, Plum is now a well-positioned place to try and help on both of those fronts as well.

**Gerhard Lazy:** The other tool that I've seen take a similar approach is CDK from Amazon, where you get to declare your infrastructure using a higher-level language. TypeScript - I know that's something which is pushed at Amazon, which makes sense, with CDK... I've used it briefly; it was okay. Way better than using the YAML alternative. That was like the most horrible YAML I've seen in my life, where you get to do like "inc", which is the function, and then get two arguments which are defined like in an array, and then you get an operation, you capture the result, and then you reuse that result as a variable. That was horrible, and all defined in the YAML. That was crazy. That was the craziest YAML I've seen. CDK was better in that respect, so I can see some similarities there.

It's interesting that you run it client-side. And when you say client-side, I imagine the CI could run it as well if it has all the secrets, but still, it's not built into the product. So that's interesting. Maybe there's a Plum cloud? I don't know. I don't know enough about Plum is what I'm getting at; and also, what I'm getting at is I would like to find out more... So you know what the follow-up is, right?

**David Flanagan:** Yeah. CDK is a really cool tool, and it's very similar to Plum. It doesn't have the provider support, and it doesn't support the Terraform providers out of the box... You know, like what Plum tries to do with their generators.

The CDK is awesome, and I think what really excels here is that Plum and CDKs shine when you're using TypeScript. I think it's such a great language for infrastructure as code, because it's strictly-typed. You can have interfaces that you can define for the different properties, you need to go out to expose, you're just using export keyword. All of these things just -- TypeScript is just great. I think if you haven't tried to do any infrastructure as code using TypeScript, or CDK, or Plum, you should just go try it. It's so cool.

\[01:27:56.28\] And the way that the Node ecosystem and TypeScript allows you to pass functions around, or even to first class, they can be exported, they can be renamed, they can be bound, there can be higher order, you can pass functions in functions... The flexibility there is phenomenal, so I encourage everyone to try TypeScript first, before going to any of the other languages.

**Gerhard Lazy:** But not you. You're Go, right?

**David Flanagan:** I do most of my Plum in TypeScript.

**Gerhard Lazy:** Really?

**David Flanagan:** I have started doing it in Go, and I just -- it's not as nice. Error checking all the time is still very present in Plum Go, so I just stick to TypeScript, actually. When I was working at Equinix Metal, I handled all the Tinker bell CI/CD infrastructure using Plum with Go, and it was super-painful.

**Gerhard Lazy:** Oh, interesting.

**David Flanagan:** I actually opened an issue going "Please let me do this in TypeScript."

**Gerhard Lazy:** Okay... And how did that go? Is it still open, the issue?

**David Flanagan:** We closed the issue and left it in Go just because the work was done, but TypeScript causes first class functions to support higher order functions, being able to pass them around, being able to publish it to NPM... There's just so many convenience factors there. That ecosystem is great. Dependencies in Go - does anyone love them? Probably not.

**Gerhard Lazy:** Yeah, I know... Things are better now. I mean, I still have nightmares from 6–7 years ago. Early Go, when it was just released. It was amazing as a language, but oh my goodness, the whole dependencies... I keep forgetting, there were all these tools which were being invented, which were like half-working, and mostly not working. I even forget the names of those tools, and they were so annoying. They were trying to be helpful, they were trying to address the pain, but I think they were causing more pain in the process. So I remember that, and that's actually a good point.

**David Flanagan:** Yeah, we used to vendor everything and commit them to our own Git repositories, which was terrible. And then we had that semi-official Dep, which just magically disappeared, because Good came out, with 1.10, or 1.11... 1.11 I think it was. And it's been better, I've got to say. Since more projects are now running Good, my life is easier, but it's still definitely challenging.

**Gerhard Lazy:** Okay. So as we are getting close to wrapping this up, I have one more thought which I wanna share with you... And it's more like a question, really. What happens with Rawhide?

**David Flanagan:** Oh, that's not stopping. I've been taking a nice break, spending time with my family for the last couple of weeks... But Rawhide Live will be back in anger in November, with just more -- you know, the cloud-native ecosystem is not standing still. There are so many projects out there. I think what we will see changing in Rawhide is I'll probably move away from just high-level introductions to all these tools.

It's great having the founder there and just showing people how to get started but I really want to get into use case-specific stuff. I've been talking to more people in the community and going "Why are you actually doing with this tool? What problem is it solving for you?" So I think we can show people not just the Getting Started guides from all these projects, but "Here's a real use case that this organization has, and here's what they're doing with this tool", to give people a bit more inspiration, and hopefully to remove some of that cognitive -- what did I call it there...? Fatigue. Decision fatigue. We want to try and remove some of this. If you're standing there, and you're like "What Git Ops tool do I use?" or "Which CI do I use?" Like, okay - what is your use case? Is it similar to this organization, or this one? Here's the one they use, and how they're going about it and what they do with it. So yeah, you'll see more use case-driven stuff in the next few months.

**Gerhard Lazy:** That's really exciting, because I'm thinking exactly the same way. I mean, it's great to have all these conversations to get people interested, and to get people steered into what resonates with them, so that they know what's out there... And there's so much out there, as you mentioned. But once you do that, you kind of start -- I don't know, you feel which way you'd want to go, which way gets you most excited, and then the next natural step is to explore that space. You don't want to stay shallow all the time. I mean, breadth is very important; there comes a point you want to go a bit deeper than the first hour or the first two hours, which is just the very early beginning of any tool, really.

**David Flanagan:** Yeah. Everything we do is difficult. Software development is not easy, it doesn't matter how long you've been doing it. In fact, it probably gets harder the longer you've been in it. But I think having that breadth of knowledge of what the tools are, when to use them and roughly what they do is really important for everyone. But at some point, you do need to go down and actually use it in anger. You have to be able to solve real problems with the tool. You might even actually be a consultant, and you can jump from company to company and just say "Oh, use this tool, and use that", and then move on and never actually have them implemented. But at some point, you do need to use these tools in a real use case-driven fashion... So yeah, I want to tackle that and make that easier for everyone.

**Gerhard Lazy:** Well, I'm really looking forward to the new and better Rawhide Live, and I'm looking forward to what you do next... But I encourage you taking these couple of weeks, months, however long it's going to be, to make sure everything is nice and smooth, the transition in the new job is smooth... The onboarding is very important, and very often it's skipped. You just get thrown straight in the middle of it. And that can be okay; it's not always bad. But sometimes it's better to just go slower, go smoother, take the lay of the land and enjoy it... Because we keep moving too fast through things, I feel... It's like an acceleration of the next thing, the next thing, and it's not enough time on enjoying or appreciating the present.

**David Flanagan:** I couldn't agree more. I've definitely taken another couple of weeks just to spend time with the family, and then I'll come back in November, hopefully do some Rawhide stuff. I've got big plans for Clustered, big plans for Rawhide Live, and with Plum being my new role, I think it's the first time in a long time that my particular interests in technology are directly aligned with the work that I'll be doing. So again, lots of great stuff.

**Gerhard Lazy:** And we're looking forward to that, David. Thank you very much for joining us. This was great, thank you.

**David Flanagan:** Thank you for having me, it's a pleasure.
