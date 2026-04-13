**Gerhard Lazy:** I love talking about crazy ideas executed well, which is why I'm excited to be speaking today with Matey and INDAR about Grafana On Call. Welcome to Ship it.

**Matey Kikuyu:** Hello. Yeah, thank you for having us. That's Matey.

**INDAR Kharkov:** Yes, and I'm so happy to be here. I'm very excited. I'm INDAR.

**Gerhard Lazy:** So how do you pronounce the name of the startup that you both co-founded before it became Grafana On Call?

**Matey Kikuyu:** It used to be called Amir... So whoever we asked, everybody had a different idea how to code.

**Gerhard Lazy:** Okay. So INDAR, how do you pronounce it?

**INDAR Kharkov:** It's Amir.

**Gerhard Lazy:** Amir.

**INDAR Kharkov:** Yes.

**Gerhard Lazy:** Okay, good. Good. So why do people need to be on-call?

**INDAR Kharkov:** Right now, businesses - they're required to be online, they're required to provide uninterrupted service, 24 hours, 7 days per week. There is a team behind every service, which makes sure it's live. And this team needs to be online all the time, and everybody needs to be ready to fix something. That's why people have on-call shifts, that everybody from the team is --

**Gerhard Lazy:** Responsible for, I assume, and they have to take turns.

**INDAR Kharkov:** Everybody from the team should be responsible for the service, and it's better if it's not a night for that person... And that's basically what is being on-call.

**Gerhard Lazy:** \[04:18\] So do you think that having a distributed team, Matey, which is around the whole world, helps with this, so that when it's daytime for someone, it's nighttime for someone else... And maybe the person that is on-call, it's preferably daytime for them. Do you think that helps?

**Matey Kikuyu:** Actually, that's the only one way to put people on-call. Not at night. Because we don't have any other ways to distribute 24 hours fair enough. So that's why different tools showed up, which helped people to distribute on-call pressure, or alert pressure... So if it's night for one person, it makes a lot of sense to send incidents to another person who is on the other side of the globe. But of course, not every team could afford that, not every company could afford that, so there are still a lot of on-call teams which are not distributed worldwide which don't have this fair on-call distribution.

**Gerhard Lazy:** Can you imagine this being outsourced, as a small company that is in a single location, and there's nighttime for all the employees - can you imagine outsourcing on-call?

**Matey Kikuyu:** I know examples of companies who outsource on-call successfully... But of course, it requires some efforts in culture, and you need to let another company in your infrastructure, you need to keep them updated, you need to make them know how to fix problems at night... Because if you do on-call good, that means that on-call person will be able to fix incidents by himself. In some companies, on-call happens in a way that a person just acts like the one who decides if this incident needs to be fixed now.

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** So it depends on which type of incidents do you have, and what's your SLA, and a lot of cultural facts.

**Gerhard Lazy:** Okay. I'm wondering, INDAR, if you've ever been on-call and woken up in the middle of the night?

**INDAR Kharkov:** We are a tiny team, and of course, we had a bunch of incidents that happened at our timezone. Luckily, probably 50% of our startup we were really distributed across the globe with Matey. So I was in San Francisco, and Matey was back in Europe, so we were able to have these 12-hour shifts. But when we were at the same location, we had to share the night shifts.

So yes, of course, I was on-call, and I had to wake up and fix something, and always when I woke up, I had to assemble the team to fix that incident. It was a tiny chance that I was able to fix something. Obviously, I could do some patch or hotfix and postpone it until the morning, but most of the time it needed immediate reaction of more than one person.

**Gerhard Lazy:** Okay. So can you imagine a world where people don't need to be on-call? What would that even look like? Can you imagine such a thing?

**INDAR Kharkov:** Of course. At some level of maturity, a service can be managed automatically, so real people would not need to get in the night and fix something unusual. But we don't have that level of maturity in any service yet. Every product is developing, and there is some error budget that needs to be reduced... And the errors are some unique errors that need some human response, that can't be fixed by the machine, can't be fixed automatically.

So I believe, for most of the services, people would still need to wake up in the night and do some job.

**Gerhard Lazy:** \[08:13\] I think waking up in the night - I think that's maybe the worst possible scenario when you're on-call... Preferably, there's someone when it's like daytime for them, and they don't need to wake up during the night... Because how good can you be at 3 AM or 4 AM, when you haven't had your coffee, you haven't had your routine, and you have to load all that up? Not to mention how peaceful is your sleep when you have to think that "Oh, any time my pager or my phone (whatever the case may be) may go off, and I need to be ready for that." So you're already setting yourself, just before you fall asleep, that "I may need to be woken up." As a result, you're half-asleep almost, because you need to be aware, I suppose. So what was your best on-call experience, Matey?

**Matey Kikuyu:** Interesting question. So the best on-call experience, of course, is when you are on-call, you know when you will be on-call, you prepared, and nothing happens. So your shift just passes by... \[laughter\]

**Gerhard Lazy:** I see. Okay.

**Matey Kikuyu:** ...and no incidents occur. I think it could be more interesting to answer the question "What was the best experience of being on-call and having an incident?", which is a more tricky question. So Amir, our startup which was acquired by Grafana and became Grafana On Call - it was like a year and a half before acquisition. So we had real customers, we had real production, and of course, we were on-call. And of course, we had a lot of incidents. Small team, rushing to develop a lot - we were pushing things to production fast, and...

**Gerhard Lazy:** Move fast and break everything, yeah. I know it, okay...

**Matey Kikuyu:** ...break everything... But if you break something, you will return money to your customers. So there's one excuse.

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** So it was a tough time being on-call, and of course, we had a lot of incidents... And the best rotation for me was when I was able to fix everything by myself. I had all instruments somewhere, I knew how to use them, and I had the whole knowledge about the piece which was broken. And most of the time it was like this. So when I was alone, I was confident, I just pushed the fix, I knew how to reach out to customers, I knew how to figure out which customers were affected. And that was the best experience.

Of course, everything got a little bit worse when I needed to involve somebody from our team, or even when I needed to involve somebody for example from Slack, or from our customer team, when some of our customers somehow managed to overpass the rate limit and DDoS our infrastructure. Something like this, when it happened, it went worse.

**Gerhard Lazy:** Right. So when you depended on others, when you had to talk to others, especially when that person was your customer, and they thought they were doing the right thing, but obviously they weren't - that had maybe a cascading effect, in that something that they did have a knock-on effect on something else... I can imagine that happening. How much of this did you capture as learnings, and then shared with your team after the incident was over?

**Matey Kikuyu:** So one of the main things about incident management is not to consider incidents as something unique. They will happen, they will always happen, and if you don't change, the incident will show up again. The same incident. So the bubble of problems will start to grow, and at some moment you'll find yourself just fixing incidents, and doing nothing else.

\[11:50\] So of course, one of the main things is to share and build some action items after each incident. Of course, some incidents are like - okay, you go there, you reboot the server. It happens again, you go there, reboot the server. Again, you reboot the server. Again, and again, and you found out that you're doing it three times a day, and even if the incident is small, you need to bring some small group, like once a week, discuss what happened, and write down some action items, put them into your backlog, to mitigate this amount of technical debt you have in your infrastructure.

So we tried our best to do it from the very beginning when it was a two-people startup. We still had those meetings, we incorporated those learnings, we wrote a little bit of run books... Of course, in the very beginning it's very naive, small, self-made... But it helped us to grow a lot. We're building incident management tools, we need to have a proper incident management process.

**Gerhard Lazy:** Yeah, it makes sense. So I'm wondering about you, INDAR - what was your worst on-call experience when there was an incident? Thank you, Matey.

**INDAR Kharkov:** The worst experience ever is when you're trying to fix something, and you make it worse. You commit some code which actually evolves the problem into a bigger problem. For example, if it affected only one customer, and after you fix it, it affected all the customers. That's probably a nightmare for the on-call person.

**Gerhard Lazy:** Did that happen to you?

**INDAR Kharkov:** I can't say that it was critical for our business, but of course, when you wake up at 4 AM and you try to fix something, you can make mistakes. And once -- we were a Slack application in the very beginning, and basically I sent a message not to one person, but almost every person in the organization... That was, I can say, the worst experience I have ever had being on-call.

**Gerhard Lazy:** And did that notification wake up people? What was the effect of that notification being sent to everyone?

**INDAR Kharkov:** It didn't wake up, luckily. The script was to notify somebody when the person got online, which was really cool... But it was actually not that bad. We just kind of increased the level of -- you know, just more people learned about our product, and after that we just got a few more requests for the demo. So it was not that bad. But of course, from the developer point of view, it was not the best experience.

**Matey Kikuyu:** It was Go hacker on call rotation, and he just spammed all of our customers... And they were like "Wow. What's that?"

**Gerhard Lazy:** And they said "I want this. This is a great feature. Can I have it, please?" \[laughter\] So the problem was like "Now we have to ship it." You can't back out of it; it's not like a hidden feature, A/B testing sort of thing. No, everybody has to have it. Okay, interesting.

**Matey Kikuyu:** But it was very painful to understand that it was unexpected behaviour. Why INDAR mentioned that - because he didn't expect this. And it ended up well. Nobody died. But we spammed (I don't know) 20,000 people, and like "Oops. Sorry."

**Gerhard Lazy:** "Loops. It was a bit bigger than I thought." Yeah. I remember there was this issue with Outlook, where you would reply to people, and these mega-threads were taking entire servers down, because everybody would auto-respond... There was something like that. So this wasn't like that, right? It wasn't that bad.

**Matey Kikuyu:** No.

**Gerhard Lazy:** Okay. So in terms of bad incidents, have you ever deleted production data? Like, drop the entire database. "Oops. I was meant to drop my development database, not my production one." I've done it once; it was terrible. \[laughter\] But luckily, we could rebuild it all. It was a gruelling six hours, but we fixed it. I think that's the worst one that I can remember. This was maybe 15 years ago, maybe 10 years ago... I don't know. Something like that. And I was using one of those apps, the UIs to connect to my database, and I just had the wrong dropdown selected. I said "Yeah, of course I want to delete all the tables." I was like, "Okay, okay." I didn't even read the message. The whole production went down. That was bad. That was bad. Did anything like that happen to you?

**INDAR Kharkov:** \[16:21\] I can say somebody from our team continuously wants to do that, but I guess we were experienced enough to add some pop-ups or some scripts that give you some --

**Matey Kikuyu:** INDAR is talking about me, because I have -- in the database query tool I use, I have production database selected by default, and every time INDAR sees this, he says "That's not good." \[laughter\]

**Gerhard Lazy:** Alright. But you haven't deleted it yet, so even you're doing that, I was something similar, by the way.

**Matey Kikuyu:** Yeah, yeah. \[laughs\]

**Gerhard Lazy:** Okay. I wanted to reseed stuff. That's how it happened. Stuff wasn't seeding properly, and it's just like "Let's just blow this thing down." And that's what happened. Okay... So you're still targeting production, okay. So what's preventing you from deleting it?

**Matey Kikuyu:** I think INDAR removed my access from production database recently, so... There's no chance to do it now. \[laughs\] I did go there a few weeks, but I think now I have no access. But actually, the dangerous part is migrations for us. We migrate our database prey frequently, and at some point we've developed some process around this. So we do a database copy, a full copy, we migrate it, we check how it went, we check if downtime happened in this toy copy; if it didn't, we migrate the main database, and we have some process around that to avoid problems...

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** Because that's the most dangerous thing for us, migrations. If migrations go wrong, it could take a few hours to restore.

**Gerhard Lazy:** What database do you use, can I ask? Well, I can ask, but you don't have to answer, is what I'm trying to say... You don't have to answer if you don't want. What database do you use?

**Matey Kikuyu:** Yeah, it's no secret we use a MySQL database. Actually, we decided not to use any fancy tools we don't know well at the beginning, because it's very important not to play with toys, but build stuff. So we've chosen a very established stack such as Django, Celery, MySQL, Rabbit... So it's very solid, we know how to work with it, and we just don't do any steps to other technologies.

**Gerhard Lazy:** So how do you run your database? Where does MySQL run?

**INDAR Kharkov:** We're using the hosted database as a primary, and we created a duplicate cluster in a completely other service, which has the copy of the database which is synchronized over some period of time... And if our primary service is down, let's say AWS or Google is down, we just use another provider, and we switch to it.

**Gerhard Lazy:** Which version of MySQL do you use? Or which flavour, not just version? Is it MariaDB, is it something else?

**Matey Kikuyu:** It's just a regular 5.7 MySQL.

**Gerhard Lazy:** Okay. Yeah, I don't think that's Maria. Is that the open source one? Actually, is it open source? Because I think Oracle acquired them... No? Isn't that what happened? I stopped using it maybe ten years ago, so I don't know what happened afterwards... And I think MariaDB is like the latest one. But okay, okay.

What about the stack? You mentioned you use Django, RabbitMQ, Celery... Do you use Kubernetes, or do you use something else?

**Matey Kikuyu:** Yes, we are on Kubernetes from the very beginning.

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** That's one innovative technology that we decided to pick...

**Gerhard Lazy:** That's really cool. And do you have one cluster, multiple clusters? What does that look like?

**INDAR Kharkov:** We do have one primary cluster, and we always have the second cluster, which is just waiting until the first one is down, and we can switch to it.

**Gerhard Lazy:** Interesting. Okay. And do you use multi-zone or single-zone? The nodes. Are they in a single zone? I'm assuming their in a single region...

**INDAR Kharkov:** Yeah, we do have a bunch of pools in different zones, I believe. And that's of course about our previous Amir times, because when we joined Grafana, we completely redesigned; we checked what was wrong with some parts and we kind of spent a couple of months on transitioning our infrastructure... And now it can be a little bit different.

**Break:** \[20:33\]

**Gerhard Lazy:** So what does the infrastructure look like for Grafana On Call today? .or Amir, however way you want to go. The present, or just before you were acquired. I'm trying to imagine your infrastructure setup, and the operations, and pushing code into prod... So if you can run us through that, I would really enjoy learning about that, INDAR.

**INDAR Kharkov:** Sure, I'd love to. We had all our code in our own instance of GitLab, and we used GitLab CI to push our code in the primary cluster, in our primary Kubernetes cluster. It was GKE, and we had a pretty interesting pipeline, which actually checked the databases, it makes all the clones, it ran all the migrations, it tested them... And only after everything successfully passed, we were doing the actual release, the actual migrations, everything.

Another nice part of our infrastructure was that from the beginning we used Amir, which is Grafana On Call now, for our own incident response management. When we just started the company, Amir, we both were working in startups, I was working in enterprise, and we both were trying to start using some IRM tools, and I've found that something doesn't satisfy me with the existing solutions. And when I met Matey again and started talking to him, I realized that we have some common opinion on the IRM tools. Matey had so many ideas about that thing. He was working for a startup, for Constructor.io, I believe; the one from San Francisco... Matey, you can tell us more about that experience of being on-call more... Because Matey was that real on-call engineer, and probably he was the first person who was interviewed about On Call by himself, Matey, and by me... \[laughter\]

**Gerhard Lazy:** \[24:13\] Okay, interesting.

**INDAR Kharkov:** Yeah, we were thinking "Why not? Why not start something that is easy to start using, that the market expects?" Because everything that we tried to use was built around 2010, when the whole infrastructure was different. When Docker was not popular, when there was no Kubernetes, and so on; when there was no SaaS/PaaS, everything as a service... And yeah, we were thinking "Why not build something that lives in the same place where engineers live?" And we had an idea that we need to build something, some tool that helps engineers to be on-call. And that's how the idea started.

We've built a Slack application, because we were using Slack for our communications, and we just added a third tool, a third person in our team, that managed schedules for us, that managed on-call for us. That's how it started. And the funny thing is that our first tool that we used in our infrastructure was Amir. And all the time, all that 1,5 or 2 years we were using Amir as our primary incident response management system.

I already mentioned that we had this back-up system that lived in the cluster, that was really stable, and that expected to receive all the production load if something goes down; that was our replica of Amir.

**Gerhard Lazy:** Interesting. So how was this beginning for you, Matey, with Constructor? How did you see this period of becoming Amir more and more? How did that grow for you?

**Matey Kikuyu:** As INDAR mentioned, I used to be on-call in this awesome startup called Constructor.io. Thanks, Sam, they're cool. And one thing, you have incidents all the day, all the night; I was in charge of infrastructure, so that's when I started thinking about maybe building some tooling here, because the tooling which existed didn't fit me, for some reason. It was hard for me to formulate why exactly. So I started this as a mostly research project, like "I will build something in this field, and if I spend a lot of effort, I will build something awesome. But I don't know what it is."

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** The fun thing which INDAR almost touched is that when we were building our own incident management process, we just really wanted to use other tools, but we went so much in different directions with Amir, so we just so much didn't like them, so we just pinned another one cluster, and "Here's our own tool."

And there is one other story, how this cluster -- why did we have from the very beginning two fully functional clusters... That's because when we started our production, when we signed our first customers, a few days later the whole DigitalOcean went down.

**Gerhard Lazy:** Wow...

**Matey Kikuyu:** We had everything on DigitalOcean.

**Gerhard Lazy:** Like the whole region? Or the whole platform?

**Matey Kikuyu:** The whole Kubernetes offering they had. And INDAR said "Yeah! That's Kubernetes time. That's why I spent so much time on spinning up everything in Kubernetes." And just launched everything in GKE, in (I don't know) a few minutes. And at this moment, we had two full clusters in two different cloud providers.

**Gerhard Lazy:** Crazy. So hang on, hang on... Let me understand this correctly. You ended up with two Kubernetes clusters as a result of an incident which involved DigitalOcean Kubernetes going down...

**Matey Kikuyu:** Yes.

**Gerhard Lazy:** ...and INDAR said "What the hell? Let me just spin another one up", and he did, and a few minutes later, 30 minutes, whatever, the whole setup was back on GKE?

**Matey Kikuyu:** \[28:10\] Yes, yes. And it was a moment of celebrating Kubernetes, actually... So that's the imaginary situation why everybody is using Kubernetes. Exactly for this.

**Gerhard Lazy:** When was this? I'm really curious... When was this?

**INDAR Kharkov:** I guess DigitalOcean, they just -- I don't even know if the Kubernetes was in GA at that moment...

**Matey Kikuyu:** I think it was beta, something like this, to be fair...

**Gerhard Lazy:** Beta, okay. And you were running production in beta... Wow, that's very brave. I bet you've learned some lessons in that beta period...

**Matey Kikuyu:** We did...

**Gerhard Lazy:** Okay, that's interesting...

**INDAR Kharkov:** It was not beta, and I guess that was the very beginning. So our first customer - we had some agreement with them, so they were not paying, I believe, at that moment. It was in the very, very beginning of our life. So it was maybe the first or second month we started the company.

**Gerhard Lazy:** Interesting. So do you still run on DigitalOcean today?

**INDAR Kharkov:** No.

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** We have it as a back-up. We didn't tell Grafana about this, I think...

**Gerhard Lazy:** Tooth...! \[laughter\]

**Matey Kikuyu:** Or maybe we did...

**Gerhard Lazy:** Nobody from Grafana listen to this... Right? Okay...

**INDAR Kharkov:** We told Grafana we have this one cluster there...

**Gerhard Lazy:** So there will be a period between us recording this and this going live, so you have maybe a few weeks to do that... \[laughter\] So no one will hear. Make sure you do that.

**Matey Kikuyu:** Yeah. That's just a back-up, empty cluster, just in case something will go down we'll be able to jump there. This only one purpose.

**Gerhard Lazy:** Yeah. I mean, this is something which I'm thinking myself... We have a couple of episodes of Ship It, the Kaiden ones, where we talk about the multi-cloud. We're trying to diversify, so not just have Kubernetes; try a few platforms out and see what it would take to run our application on those platforms. It's the automation that gets us. What that means is that there should be no scripts, nothing like that; there should be something that reconciles everything continuously, something like Cross plane, where - you know why not use Linde, and use Fly, and use Brenda, and use maybe something else as well, so that it's both Kubernetes and something else, and it's distributed... It's just fun. Things like this -- I know not to everyone, but to me, it's fun to think like that.

So would you be considering at any point a platform instead of Kubernetes? Can you imagine that ever happening? Or do you just like Kubernetes too much? Because I love it.

**Matey Kikuyu:** Yeah, we really enjoy using it. It just works.

**Gerhard Lazy:** So what do you use in Kubernetes? I'm very curious. What are your baseline components? Ingress NGINX, or maybe something else for Ingress, cert manager, external DNS... What are the must-haves in your Kubernetes?

**INDAR Kharkov:** As we told before, from the very beginning, there was kind of agreement between us not to use any fancy technologies that are innovative and nobody uses except us. So we were trying to do only best-practice things... And even Kubernetes back in that time was like "Hmm... Should we do it or should we not?" But we were seeing the growth of managed solutions, and we were clearly seeing that all the major providers were doing their own Kubernetes, so we decided to use it... But we decided to use the most basic components over there. So we just had our payloads, or our deployments, and some load balancers. We even had NGINX controllers, but then we decided to use more managed solutions as possible.

**Gerhard Lazy:** Interesting. Because we run Ingress NGINX, and I'm thinking of replacing it with something else. Traffic was very interesting for a while... But it's interesting that you don't even use that. You just go for load balancers, and then that's it. Interesting. Okay. Do you use external DNS at all? What manages DNS, I'm wondering?

**INDAR Kharkov:** The same managed DNS from Google.

**Gerhard Lazy:** \[31:59\] Okay, interesting.

**Matey Kikuyu:** Yeah, one thing which we didn't -- the main component of our system is RabbitMQ. Because of course, writing -- so from the very beginning, Amir is very critical to deliver incidents for it. So we cannot lose incidents, we cannot lose data. So our software is a pipeline, so at the very beginning we receive the HTTP request, we put it as fast as possible to RabbitMQ, even if the database will go down; even if half the system wouldn't work, we will publish it to RabbitMQ. And okay, whatever happens later.

So we have multiple workers which consumed from this RabbitMQ, and for example, Slack - we have a lot of third-parties. We have Pillar which is making a phone call; we have other dependencies... And they sometimes go down, and that's why we have these retry-based systems. So our workers - they will try, try, try, again and again, a lot of fallbacks, a lot of ifs and else, but that's why we didn't use managed RabbitMQ, because we spent a lot of time trying to understand how exactly does it work, how exactly does it recover, and we wanted full control under RabbitMQ.

**Gerhard Lazy:** Right.

**Matey Kikuyu:** So the load balancer - it's not so critical for us to understand how it works. Of course, it's important, but not a lot of dark magic happens there. But RabbitMQ - what if it will lose connections, what if all three nodes will lose connections to each other? How will they reignite? So we made those trainings, we checked how it all works, how much memory does it need before freezing, and all of that. So that's the only one component which we're very crazy about having under our control.

**Gerhard Lazy:** Okay. I think this is going to be the best part of the podcast, and I wasn't expecting this, and neither were you... So here it comes. Do you know that I have been a core RabbitMQ engineer for the past six years?

**INDAR Kharkov:** Oh, wow. \[laughs\] No.

**Gerhard Lazy:** Good. I wish people could see your faces now... \[laughter\] So that means that the RabbitMQ team did something right in the past six years, if you could depend on it to not go down. Okay.

**INDAR Kharkov:** The first thing I want to say - great job. Thank you for this piece of software. It works great.

**Gerhard Lazy:** I will pass it on to the team.

**INDAR Kharkov:** Yeah. We were able to build the whole Amir and Grafana On Call on top of it, and it works great.

**Gerhard Lazy:** Amazing.

**INDAR Kharkov:** Especially with Celery. Celery has some things you should be aware of, but the connection between Celery and RabbitMQ is something which we like and enjoy working with.

**Gerhard Lazy:** That's really cool. Which version of RabbitMQ? How many nodes? Which queue type? I have so many questions... \[laughter\]

**INDAR Kharkov:** Should we go that deep?

**Gerhard Lazy:** Maybe just like in one sentence - which RabbitMQ version? 3.6, 3.7, 3.8, 3.9? What are you running? How many nodes? One, three, five? Whatever. How many clusters? And which queue type? Classic queue, classic mirrored? Quorum queue? Have you heard of Streams?

**INDAR Kharkov:** I believe we use the latest version, 3.9. We have a cluster of three nodes as for now, and I believe we used classic, residence.

**Gerhard Lazy:** Classic queues, okay. Mirrored? Do you use mirroring?

**INDAR Kharkov:** No, we don't.

**Gerhard Lazy:** Okay, that's great to know. Thank you for that, I enjoyed that.

**Break:** \[35:28\]

**Gerhard Lazy:** So if we were to start using On Call for Changelog.com, where do you think that we should start?

**Matey Kikuyu:** So the starting point for Grafana On Call is Grafana Cloud. We revealed a month ago the public beta preview, not ready yet, please use with caution version...

**Gerhard Lazy:** Like the DigitalOcean Kubernetes cluster, right? It can go down at any time. \[laughter\] Okay, okay, I get you. I get you.

**Matey Kikuyu:** Actually - yeah, we treat it like real production, and of course it's real production, and it will go to GA soon, so we're getting more and more serious about it... But actually, it's there for you to try, play with, give us your feedback. And it's Grafana Cloud, you just sign up, you will look at average Grafana, but on the left you'll have a round plugin icon called Grafana On Call, and that's it. So that's your starting point.

**Gerhard Lazy:** So if we already emit logs to Grafana Cloud, and we emit metrics to Grafana Cloud, how do we make use of those with Grafana On Call?

**Matey Kikuyu:** So Grafana On Call - it's very important to understand what is this product about. It's not about insane colours. Grafana itself is for, j-rating colours. It's not for managing large incidents, when you have like a 17-hour-long incident, and you need help and communication... It's not about that. Furthermore, it's focused on notification for right people, right time, according to on-call schedules and different channels. So if you need to go to Grafana and set up your alerts, feel free to play with unified alerting, which was revealed recently also... And after you configure your alerts, rules and thresholds, you could open the Grafana On Call, you'll see the small onboarding instructions there, like "Do a, b, c, d." So you click at integration there, and it's a quick integration with current Grafana.

**Gerhard Lazy:** Okay.

**Matey Kikuyu:** So it will automatically create a contact point for you in unified alerting, and start consuming alerts from the rest of Grafana. Your next steps are to configure on-call rotation. For on-call rotation we have a pretty interesting concept, which is a lot different from on-call schedulers our competitors have. Initially, we introduced these on-call rotation mechanics as a prototype. Just something quick, hacky, to give our clients to test, and it ended up to be so cool that we just stayed with it.

\[40:22\] So actually, we don't have an on-call rotation editor in our product at all. So you'll not find something like in pager duty. But we allow consumption of on-call sheets from Google Calendar, Outlook... Any calendar system you use. So you just go to Google Calendar, create a new calendar, share it with your colleagues, create time slots, and connect it with Grafana On Call.

It works well, because you already have your calendar app in your mobile phone. And the main thing which on-call editors should allow you to do is quick changes. For example, I need to -- I don't know, I have some family business, I need to leave my laptop; I'm on-call now, I need to overwrite, so I need to exchange on-call shifts with INDAR. How do I do it? Do I go to some large UI login, go deep, and make this change? Or I just open my calendar, create a time slot, and just create/overwrite there?

So we stayed with these mechanics and it worked well so far. Anything back we'd really appreciate, if you will have one. The next thing you could do is to connect your mobile phone, verify your mobile phone/SMS, set up escalation policies... So if incidents occurred, what Grafana On Call will do; who to notify. Somebody based on on-call schedule? What if this person would not respond? Five minutes later, notify for example Tom, because Mattias kept on-call shift... And yeah, that's all. That's all about Grafana On Call. So if you will notify in comfortable time.

**Gerhard Lazy:** So alerting - I know that when you configure alerts, you can also set up notifications... So what system to use to notify, and then it fires off those notifications. I don't fully understand how Grafana On Call fits into that chain, in that notifications won't be fired straight away; they need to basically adhere to some rules, which I imagine is just Grafana On Call, which knows maybe who to notify. Is that right? But I'm not quite clear...

**Matey Kikuyu:** There's a lot of confusion about this connection, because we actively work on this piece... And as you mentioned, you open Grafana Alerts and you see you could send alerts to Slack, you could send alerts to Telegram, to Twilio, and other destinations. So Grafana On Call has evolved the notification part. So it's a whole new product about this notification piece. So if you want just basic notifications, just send alerts to the Slack channel; you could send them straight away, without Grafana On Call. But if you want some magic around this, if you want a back-up, using escalations to achieve SLO...

**Gerhard Lazy:** Right, that makes sense.

**Matey Kikuyu:** ...you could go there. What we really enjoyed about Grafana when we joined is that big tent philosophy. So we designed Grafana On Call so it will be helpful for you even if you don't use other parts of Grafana. And other parts of Grafana - they don't need Grafana On Call. You could use Grafana On Call if you find it comfortable. If you don't, just use a competitor tool.

For example, you could use Grafana On Call with Rabbi, with Datadog, with any other system which could issue signals, alerts, whatever. You could write a cron job which will fire alerts there, and that's okay. No need to use Loki, Tempo, and other parts. Of course, we want to build a cool experience, and make you laugh all tools together. But we don't force you. So that's a very cool idea we enjoyed when we joined.

**Gerhard Lazy:** \[44:10\] That really resonates with me. I like that idea very much. Not forcing people... You don't have to use all of this stuff together. Just pick and choose whatever makes sense to you. And you can change your mind; that's okay, too. It's not like "Once you go down this path, that's it. It's really hard to go back."

I'm wondering, how do Los fit with Grafana On Call? Let's imagine that my uptime - let's just go with uptime - is three 9's. 99.9%. How does this concept - if at all; maybe it doesn't fit anywhere within Grafana On Call. So I'm wondering if there is a connection there with Los.

**Matey Kikuyu:** So we don't dictate any specific approach to this. So Los could be different. So how Grafana On Call could help here is that Grafana On Call is an instrument of making sure that in some timeframe somebody will pick up the incident. So if you have situations where an incident occurred and somebody received an alert and nobody reacted in three hours, this is where Grafana On Call will help.

So it wouldn't help you to mitigate spikes when your SLO reached for four seconds and came back again. It doesn't help with it. It helps a little bit, because we have grouping mechanics on our side also; so if you have a lot of spikes, it could group them all to one incident and help you to avoid alert storm and avoid alert fatigue... So we are addressing this problem as well. But it's a different point of view.

**Gerhard Lazy:** Yeah, I understand. Do you have any questions for me?

**Matey Kikuyu:** Yeah. I'm curious - so incidents is a situation where your infrastructure actually breaks into your personal life... So whenever you are, you should be connected, right? So you are sleeping, or you're having dinner with your family, and your work is interrupting you. So that's why we're addressing this problem, because we want to make it more comfortable for people. It's impossible to avoid.

So a question for you - how far do you think instruments should go? So what's that good balance between using instruments to help you to mitigate incidents and alerts, and doing some manual work, like opening Grafana, looking at graphs with a serious face and making decisions about incident mitigation or not?

**Gerhard Lazy:** Right. So the way I would answer this is by describing the ideal incident scenario. The ideal incident scenario for me would be I get a notification when something needs my attention. I would hate to be notified when something can fix itself, or when something is partially degraded, but it doesn't affect the majority of the users.

Let me give you an example. Currently - and I think this is us using... When I say "this is us", let me be more specific. This is me configuring alerts wrong in Grafana, in that if one probe - we're using synthetic monitoring - doesn't get a 200 response, I get a notification. Now, the first thing which I do, I look, like "Is this one probe, or is this across multiple probes?" If it's just one probe, I know that most likely there's an issue with that probe which is running in Grafana Cloud; our service is okay. Our service is fronted by a CDN, so the CDN would need to have a pretty bad day - which did happen, by the way... The first time in maybe five years when Vastly went down, it affected everyone. I was sunbathing. It was a very important moment... And I got all those incidents. It was like my day off. And I got so many alerts that day, because all the probes were failing.

\[47:59\] So when I get notified, I know that I need to investigate. So nothing automatically couldn't resolve itself. It wasn't a matter of restarting it, there was no disk which was getting full, nothing like that. So what that usually means is networking; in almost all cases for us, it just meant networking. So I would love to know which part of the network stack is the problem. Is it between a portion of the users and the CDN? Is it like a specific pop which maybe didn't fail over? Is it some data which was cached incorrectly in the CDN, and then that is being served, but everything is fine between the CDN, and the network is fine?

So going with the networking approach, which part of the network is the problem? And I would love basically to know where to pinpoint, where to start digging. It does happen that for example our Kubernetes - there are some issues with the networking, and the CDN cannot forward requests correctly. When that happens, we just serve stale content, except the dynamic requests. We still have a fair bit of those, and I wish we had fewer requests which were dynamic, which wouldn't depend on the origin being up. So that's okay. Again, for the majority of the users, the content can be served; the mp3 files, all the static assets, all that stuff. The website is up, it's not fully down... And that helps me figure out "Okay, so this is like a problem with the origin. We have only one, so things are simple... But I would expect us to have multiple origins, so that when one origin is down, it's okay. The traffic gets re-routed, and we just keep the healthy origin in the CDN.

So when I know which origin is down, is it something that I can fix? I would like to know straight away if the provider has an incident. Because we depend increasingly on other providers, so it would help to know, "Is it me, or is it a bigger issue?" In all incidents which we had previously it took me to investigate, to realize "You know what? It's actually the provider. There's nothing I can do other than fail over." I know I don't have more than one origin, so there's not much I can do other than wait. The CDN will serve the cache, so it's okay. Did that answer your question, Matey?

**Matey Kikuyu:** What I figured out from this answer is that you really want to have a lot of context during the incident, provided straight away with the incident.

**Gerhard Lazy:** Yes.

**Matey Kikuyu:** And that's a great answer. And actually, you don't want to be paged based on some rules which could be automated... So that's great feedback. I think we should check our backlog.

**INDAR Kharkov:** Yeah, that's great feedback, and I'm really happy about our decision to join Grafana... because Grafana is the best place to be as an IRM tool, because you already have all that information right in the database.

**Gerhard Lazy:** For sure. Now, I can give you some feedback from our last incident when Vastly went down, when parts of Grafana were affected as well. That is bad, right? When your incident tool is affected as well by the incident... And again, that happens very rarely; once every five years. I know that Amazon was down; it didn't affect us, but apparently it affected a lot of companies. I don't know to what extent Grafana was affected, but from our perspective, everything was okay.

Furthermore, I don't like having a single instance of anything. So I don't like depending on a single incident tool; I don't like depending on a single monitoring system, or metric system, or telemetry system. I don't like using a single Kubernetes cluster. Now, it's the real world, and we have to allocate our time accordingly, and there's just not enough hours in the day, so we have to prioritize; we are not there yet. But I'm moving Changelog to a world from an operational perspective where we have multiples of everything. One origin goes down - that's okay. One continent goes down - that's okay.

I know people say multi-cloud is very difficult to do right. I get it. Furthermore, I understand the challenge, and I'm going to slowly chip away at that. There are some simple solutions, I think, rather than like the big problem. We're not that big; we can use, for example, Fly.io to host an instance of Changelog. We need to migrate all our assets to S3. And when we do that, our app and our stateful data is less, and we don't have to have an instance of all our media in multiple regions, and that will solve a lot of the problems.

\[52:17\] The database, if we go to a hosted PostgreSQL, because that's what we use - maybe like Cockroach DB; I'm really interested in what that would look like - we don't have to move the data. It's already distributed, it's all handled for us. So then all we have to do is worry about our code, and then how do we distribute the code effectively across multiple providers? Now, that's a very interesting challenge, isn't it? But all the state, the hard problem - that's already in S3. And if S3 is down - well, should we have a single S3? No, we should have multiple. What does that look like? I'm really passionate about solving that problem. And then you have multiples of everything; if one goes down, that's okay. My system is not down. It's degraded. And sure, I want to be notified, like "This part is down", but it's like, you know, a news item. "Oh, this is interesting. Some interesting tweets. What else happened in the life of Changelog infrastructure?" That's the way I think about this. So incidents - and that's why I asked my question about being on-call. Maybe if you approach things wrong, nobody needs to be on-call. Maybe.

**Matey Kikuyu:** You know, black swans - they always come from the side you don't expect...

**Gerhard Lazy:** That's exactly right. Black Swan is a very, very good book. I wish you could see, it's right there. I'm going to read it again. It's amazing. Have you read The Black Swan, the book?

**Matey Kikuyu:** Yeah, of course.

**Gerhard Lazy:** Okay. That's exactly what I'm thinking.

**Matey Kikuyu:** That's like a tabletop book for those who build incident management software.

**Gerhard Lazy:** Amazing. That is a great -- yeah, I definitely recommend everybody reads that book to properly understand where I'm going with this... So that's great.

**INDAR Kharkov:** Did you read it from cover to cover?

**Gerhard Lazy:** Yeah. But I want to read it again, for sure. I have like a whole stack of books which I'm going to read this holiday season; that's what I'm looking forward to most. So by the time listeners are listening to this, you can ask me in the comments, and you can ask us what books have we read between recording this and this going live.

So as we are preparing to wrap this up, I'm wondering, what is the most important takeaway that you want all listeners to have from this conversation? INDAR, would you like to go first?

**INDAR Kharkov:** That's really cool that we as engineers can build tools for engineers, that are easily accessible, that are easy to use, and that can make our lives much easier. And that's really cool that we are already in this industry, and nobody except us can understand the problem better than us. And that gives us a unique opportunity to build the product that can change our lives as on-call engineers. That's what I really love about building that product; that gives me inspiration to wake up and make some new features, create these multiples... I really like the idea about multiples, and that's what we were doing all the time; we were figuring out new ways to deliver the incident, we were figuring out new ways to duplicate our infrastructure... And that's really inspiring.

**Gerhard Lazy:** Matey, what about you?

**Matey Kikuyu:** When I started this project it was like "I need a simple tool which will just consume incidents in one side, and output them in the other side. Eh, I know everything about this. Let's build it." Three years later, I have a conversation with you and I still figure out more and more about how do people work with incidents. Because this is the space where technology meets your real life. How do you feel about it, what do you expect, what is comfortable for you, what is not...

And my main take-away, and take-away for everyone I want to be, is that the incident management process is a unique thing. It should suit you, and that's the main qualification criteria for anything - for tools, for how should incidents look, how your on-call schedule should be organized... And that's it.

**Gerhard Lazy:** Well, that sounds great to me. Those are two great takeaways. Thank you very much for today's conversation. I myself learned a lot, and I'm really looking forward to what comes next for Grafana on-call. I really like the whole portfolio. Furthermore, I think it's going in a great direction, and I'm very excited to what next year - we're recording this in 2021, but you're listening in 2022... So what 2022 brings for the whole ecosystem.

Thank you very much, INDAR, thank you, Matey. It's been a great pleasure talking to you.

**Matey Kikuyu:** Thank you.

**INDAR Kharkov:** Thank you, Gerhard.
