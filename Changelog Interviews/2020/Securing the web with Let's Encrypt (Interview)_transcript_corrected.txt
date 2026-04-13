**Adam Staravia:** Securing the internet is obviously a big deal. Back in May 2013 you thought so as well, and you started the Internet Security Research Group... But since then, Let’s Encrypt has issued (in all caps) one billion certificates, and that's a big deal. That was an announcement you made February 27th. Talk about that moment for you. What was that like, to pin that post?

**Josh AAS:** I still pretty clearly remember sitting around, debating with our staff whether we've issued one million certs in the first year or not. When we started, we had no idea what the scope of this would turn into. A billion is a big number, and it's amazing to get here. So many ideas never turn out to what you wish they would turn into, and it's pretty exciting that this team has built something that turned into what we wanted to be, which is serving so many websites around the internet. We're getting close to around 200 million now, and that's fantastic.

**Adam Staravia:** It's often interesting because you can take for granted what's right there in front of you today... So I kind of look at it like, new developers coming into the scene in the last two years - let's say since the inception of Let’s Encrypt - and just the idea that it's there, and it's fairly easy now to request a free certificate... We're in a day now where I suppose the security of the internet is much more important as we all become more dependent on it, and it's more prevalent in our everyday lives, especially in a day when right now we're using a Zoom chat, so we're assuming that this is encrypted... I'm not sure if we're seeing anything that's concerned...

**Jerold Santo:** Well, we're recording it ourselves, so maybe it's not too private...

**Adam Staravia:** Right. The point is that not all the Zoom calls are ones you want to put onto the internet.

**Jerold Santo:** Yeah.

**Adam Staravia:** Obviously, security is a pretty interesting thing, but we came from a day when SSL certificates were very difficult to get, generally expensive, and just the process was very cumbersome. Now it's a fairly easy process. People take that for granted.

**Josh AAS:** Yeah. On the one hand, we want to be in a position where people can take us for granted, because we want the service to just happen for people. Ideally, you could just set up web servers and not even know that you have an SSL certificate, let alone where or how you got it. We're all about automation and removing humans from the loop, so people have to do less.

\[04:22\] We'd love to get to a world where every time you spin up a server, it's just got the certs you need in the background, it installs them correctly, and everything just work; people don't need to know about us.

On the flip side, we do want people to know about us, because we're a non-profit, and we need people to know about the great work that we do, and help fund our work. So yeah, every day we go out and try to put ourselves in the position where people can take us for granted, but... It does have some negative consequences.

**Jerold Santo:** Kind of catch-22... What are your plans around that?

**Josh AAS:** We continue doing what we've been doing - providing great service, building things that people can rely on, and make the internet more secure. On the technical side, it just happens... But we've got great communications people, and they go out and talk about what we do, talk to potential funders, and so far it's working out great.

**Jerold Santo:** I always think about Wikipedia and their opportunity to throw Jimmy Wales' note up there once a year, usually in December, and say "Hey, we're a valuable resource. Send us your money." And I was thinking like "What's the Let’s Encrypt equivalent of that?" It's probably a bad idea... You've got 200 million sites, but you don't exactly want to be injecting anything into that experience. Like you said, you want to be as seamless as possible. So do you beat the drum mostly on the blog, or are there campaigns? What do you guys do to let people know what you're up to?

**Josh AAS:** We certainly don't want to go out there and inject messages into systems that people depend on. \[laughter\]

**Adam Staravia:** That's a very bad idea.

**Jerold Santo:** Yeah... I didn't think so.

**Josh AAS:** We've got a social media presence, a blog, we also have a lot of contacts and people who understand what we do and support us, and we meet with them all the time. We go to companies, explain what we're doing, "We're here for you." We talk to open source projects... Anywhere that we think understanding what we do can help. It's just a lot of work for you to go out there and do.

Sometimes the media picks up good things, like a billion certificates. That's really helpful, to get press coverage. Unfortunately, sometimes people find out about us when there's a problem, like when you have a service that so many people depend on. When things go wrong, that's when people notice. That's when they stop taking you for granted. That's not obviously something that we strive for. We'd prefer that never happened. But software is complicated, systems are complicated. Every system has problems once in a while.

Some people learn about us when we have problems, and that sort of doesn't inject the message into their life... Which hopefully is like "Look, this is something I depend on", and when there's an issue, you realize how much you depend on it. And the best way to help out is to support us.

**Adam Staravia:** What are some of the bigger problems you've had to mitigate over the years?

**Josh AAS:** It mostly just comes down to normal software bugs. We have a software stack called Boulder, that is sort of the core of the certificate authority. It's written in Go; it's non-trivial in size, although it's mostly been developed by an average of three engineers over five years.

So it's fairly complex, and it's non-trivial in size, and like all software, every once in a while there's a bug there... And those bugs can cause either stability, or compliance, or security issues. We haven't had too many security issues, but we have had some stability and compliance issues. When a bug pops up, usually we're very quick to fix it, but when you're serving 200 million websites...

**Adam Staravia:** Yeah.

**Josh AAS:** \[08:03\] ...any little thing becomes sort of a big thing. But I'm really proud of our track record here. We have a great track record for stability and reliability in security. And when incidents do come up, I'm particularly proud of how well we deal with them. We typically fix issues in a couple of hours max, then we go out and talk about it with public reports, and detailed public information, and lots of transparency very quickly. On most within a few hours. We really work hard to follow up and make sure that that type of problem doesn't happen again; we use those things as a learning experience.

**Adam Staravia:** Well, given the opportunity, and potentially even by design, the ability for people to take Let’s Encrypt for granted -- for the uninitiated, how do you describe Let’s Encrypt? What's Let’s Encrypt today?

**Josh AAS:** You mean how do I describe it to people who don't really understand what SSL certificates are?

**Adam Staravia:** No, let's take it from a developer's point of view. Somebody who kind of gets it, but doesn't -- they've heard of Let’s Encrypt, but they don't know all the bits and bobs; they don't know all the details of what Let’s Encrypt is. What do you do?

**Josh AAS:** Yeah, so if you're a developer and you want to set up an HTTPS site, you're going to need a certificate. Normally, without Let’s Encrypt in the world, you'd have to go find some place to buy a certificate and decide what kind of certificate you want, decide how much you want to pay... You'd probably have to create some sort of certificate sign in request, or fill out some form containing a bunch of details about what exactly you want in your certificate... It can be a pretty time-consuming, costly and complicated process, and it's frankly just really confusing. I think it's the biggest reason that people didn't deploy HTTPS prior to the existence of Let’s Encrypt.

So Let’s Encrypt really just tries to do away with all that. We try to make things as simple as possible. We have an API, you just submit a request using some API client software; you don't need to write it yourself or know how it works. You just download some software for whatever platform you want to use. That software knows how to talk to Let’s Encrypt. You just tell it what domains you want certificates for. Typically, the software will just go out and get the domains, complete the challenges, do what you need to do to get the cert, and then sometimes it'll even install it for you.

All this doesn't require you to know anything about how certificates work, or how you get them, or what's in them. It doesn't require any payment. One of the most important things about not requiring payment is that's not necessarily just about the amount of money involved. It's not free just because free equals zero dollars. It's free because if you're sitting in some big company and you want to set up a site really quickly, and you want to use best practices and deploy HTTPS, if you've got to go to accounting and get a credit card and get approval to spend money, and set up recurring charges, and things like that...

**Adam Staravia:** It's not going to happen.

**Josh AAS:** ...even if you're charging 10 cents a month, it's a pretty big friction for you. You're just going to say "I'm not going to go through this whole silly process. I'm just going to set up the site without HTTPS." And now you've got another insecure site on the web.

So not charging money is about not creating friction in the process, and not requiring humans to be involved any more than necessary. So yeah, Let’s Encrypt is a really automated, easy to use, free way to get a certificate.

**Jerold Santo:** We first covered Let’s Encrypt on the Changelog back in March 2017, episode 243. We had Jacob Hoffman-Andrews from the EFF on the show. Probably a fun episode to go back and listen to in light of the success you'll have had... Because that was very much near or shortly after the kick-off. So from there to a billion in under three years is pretty amazing. I think free is a huge aspect to that, but I'm just curious, from your perspective, what did all get right, in addition to making it free, which is a big aspect, of course? ...to get the spread on. You spread like crazy, which is amazing. What did you do right to get here?

**Josh AAS:** \[12:20\] First, let me recommend going back to that episode to anybody who wants to. Jacob is our lead software engineer, and he is brilliant. You'll never regret listening to him.

**Jerold Santo:** Yeah, he was a great guest.

**Josh AAS:** Like most things in cryptography adoption, it's all about ease of use. You can come up with the most brilliant security or cryptography mechanism you want, but if it's not easy enough to use, it's not going to see deployment. Not at scale anyway. So from the beginning, it's been all about ease of use. For us, that really means automation and really just making it, so people don't really have to do anything.

In order to automate, you just want to have computers do the work. On the Let's Encrypt site we've got a bunch of computers that do the work on our side. It's a little more complicated than that, but you know, computers do most of the work... And then on the client side, for people requesting certificates, we needed client software that works for everybody. And people use a lot of different stacks out there. Some people are on Linux, some people are on Windows, BSDs, and people are using Apache, NGINX... Whatever.

There are a lot of different deployment environments out there, and there's no way that we could write client software for all of those environments ourselves. It's just not possible. But we came up with a really well-documented and standardized protocol, and then our community - it's just amazing - has gone out and written hundreds of clients that work with this protocol. So now, no matter what your application stack is or your software stack, there's almost certainly a Let's Encrypt client out there for you to use, and all you need to do is just find that client, install it, and it will do most of the work for you. That's something we really couldn't have pulled off without our community.

**Jerold Santo:** Did you bootstrap any of that? Did you say "Well, we'll do the Apache integration, or the NGINX integration and get the ball rolling"? Or was there immediate community support post-announcement, and maybe the publishing of (is it a spec?) the actual way it works.

**Josh AAS:** Yeah, the protocol is called ACME, and it's an ITS specification now. Before that, we just published the spec for it. We did originally create a client that we developed not for very long, because we realized that us putting resources into one client ourselves just does not cover enough use cases. There's so much out there... So we really need to focus on the community-building clients and not use doing it.

And for that client, which has now been renamed to Cert bot, the Electronic Frontier Foundation (EFF) - they were volunteering most of the work to make that client anyway. It wasn't the Let's Encrypt server-side engineers doing it. So we decided pretty early on that it makes more sense to just turn that client over to EFF and make it an EFF project, since they were doing most of the work anyway. And we wanted to focus on supporting this strong community instead of building clients ourselves.

So we did sort of try to bootstrap it by building this client early on, and it served its purpose well... But it's at a much better home at EFF, and it's really grown into an amazing client over there.

**Adam Staravia:** When we go back to the inception of things - I don't want to go too far back, but just enough to understand the crux of the problem. Obviously, an unsecure web is an issue, but what was the biggest thing that stood out to you, that made sense to move forward with the Internet Research Group, and that being the foundation behind Let's Encrypt? What was the biggest problem happening, that was sort of like "This has got a stop."

**Josh AAS:** \[16:06\] Yeah... There are a few different people involved in starting IRG, and I think they all have their own personal motivations for why they wanted to get into this... I want to make clear this might not necessarily be true for all of them. But for me, at the time I was running the networking group at Mozilla, the group that does all the networking code in Firefox. And one of the most frustrating things about running that team is there was nothing you can do on the browser-side to make sites use HTTPS. So if the site doesn't use HTTPS, you're just stuck doing completely not secure networking, and there was no amount of code you can write, there's no clever code you can write; you're just stuck.

So if you're sitting there, in charge of the networking stack for a major browser, it's very frustrating that there's nothing you can do about this. You can't improve the situation. So we started thinking about "What's the problem here? Why are people not using HTTPS?" And the biggest problem seemed to be that getting and managing certificates was too complicated, or too costly, or too time-consuming. For whatever reason, people didn't want to do that. Everything else is pretty easy. If you want to turn on TLS in Apache or NGINX, it's a pretty easy config flag. The software is all there. Easy to turn it on. You just can't do it without a cert.

This really came to a head when I was participating in some of the discussions in the IETF about standardizing HTTP/2. That's kind of a mouthful, so I'm just going to call it H2 from here on out.

**Adam Staravia:** We do as well.

**Josh AAS:** One of the big discussions in the standardization process for H2 was "Should H2 require HTTPS? Should it require TLS?" And for me, that felt like a no-brainer. Like, yeah, obviously H2 should require TLS. At that point I think it was like 2011 or 2012 when this conversation was happening, and it seemed like we know that not using TLS is a huge problem. It's 2011. Why in the world would we ever create a new protocol that's not secure by default? That seemed just crazy.

**Adam Staravia:** Yeah.

**Josh AAS:** And there was a lot of pushbacks on that idea. Part of the pushback came from proxy providers; basically, people whose software and jobs depend on intercepting web traffic. So that's sort of the expected pushback. But other than that, it just seemed like a no-brainer to me. But there was another objection, which was that if you make H2 require HTTPS, you are effectively going to make it pay-to-play, and you're going to make it much harder to deploy, because you won't be able to deploy H2 without buying certificates... And you won't be able to deploy H2 without going through the certificate obtaining and managing processes. So the idea was that requiring TLS would make H2 deployment a handicap, basically, and pay-to-play.

That frankly felt pretty reasonable, and it felt to me like "If I'm going to continue with this position that it should require TLS, and that it's crazy to not to, then I need to be willing to deal with the criticism here. I need to have some answer to this." At the time, I didn't really have an answer. They were right - one of the great things about the web is that a lot of things don't require you to pay. And if we required TLS for H2, you would effectively be putting a financial tax on anybody who wanted to deploy H2.

**Adam Staravia:** \[20:05\] And likely, people wouldn't play.

**Josh AAS:** Right.

**Adam Staravia:** So what's the point of even creating the tech, or the new protocol, the new spec, unless people would use it... Except for the ones who can obviously pay.

**Jerold Santo:** Yeah, you hamper its adoption, and you also hamper the people who can't afford to adopt it, right?

**Josh AAS:** Yeah... I mean, the big companies that do it - you know, Google, Facebook, whatever...

**Jerold Santo:** For sure.

**Josh AAS:** ...that's a lot of traffic on the web. So it still has a benefit, but I don't think we should be designing major protocols like H2 primarily just for the biggest players out there. As centralized as the web has become in many ways, I think it's still important to pursue some of the ideals of accessibility and making sure everyone has the ability to participate on the web.

So I thought those criticisms of requiring TLS were legitimate, and if I was going to run around telling everybody that they have to use TLS all the time, then we needed to deal with that problem. So I went back to the team I was working on then, and we talked about a lot of different possible solutions, but it was hard to find any solution that was going to solve the problem, and solve it in a reasonable amount of time. There were ideas where it's like "Well, if we do this, then maybe in 10–20 years the situation is different, and we can do this", but that's way too far. We should have done this 10–20 years ago, not be planning to do it 10–20 years in the future.

So the only solution we came up with that we were pretty sure would work, and that might work in a big way in 5 years or less, was that there just had to be a new certificate authority, that was public benefit, really easy to use, doesn't cost money, and available all over the globe. Available everywhere, to everyone. Without that, we just didn't see how we were going to get out of this.

To be honest, I don't think anybody involved in those discussions was thinking like "Man, I'm excited to spend the next 5 years of my life building a CA from scratch, and dropping all these other things that I wanted to do in my career, and build a CA." It wasn't the most attractive project. But it felt like this is what's gotta happen. If we don't do this, the web is going to be not secure for a long time.

So we did it. We went out and started a new CA. At the time, I knew nothing about how to build or run a CA, so it was a lot of learning from me, and I think everybody involved. I don't think anybody -- we had some advisors who had some experience, but I don't think anybody actually building the CA had ever built one before. So it was a big undertaking, but that's why we did it.

And here we are, five years later, and... When we started, I think 39% of all page loads - so not websites, but 39% of the time you loaded any particular web page, it would be encrypted. And that's mainly because of big websites like Google and Facebook and other big properties... And everything else wasn't. Here we are, five years later, and in the United States I think we're approaching 92%. Globally we're over 80% now. And those have a great trend line up. So five years later we've encrypted most of it. We've got some more work to do, but we got there.

**Break:** \[23:41\]

**Adam Staravia:** I've got to imagine starting a CA from scratch is an undertaking... You'd mentioned that you had some advisors obviously giving some advice (that's what advisors do), but the majority of everyone involved in co-founding the Internet Security Research Group had no clue how to do some of these things... So how did you get a clue? How did you do this? What's involved in building a certificate authority?

**Josh AAS:** Well, we got some advice from people, like you said, and sort of laid out some of the basics of how it works. There is a document out there called The Baseline Requirements, which is a document built by the CA's in the browsers combined, sort of come together in a forum called CA/Browser Forum. They created a document of all the rules and requirements that all CA's are required to abide by. And you can figure out a lot about how a CA is going to have to work based on what those rules are... So we read those very carefully.

We hired some auditors who audit us every year, to make sure that we're compliant with those, and some other rules. Our auditors helped us figure out some stuff... But yeah, mostly we just consumed all this information and started drawing out plans for how things work, and then we had iterated on them until it all seemed like it would work. Then we went out and bought the hardware, signed the agreements... Just got to work. Some things had to be iterated on a couple of times, but... Pretty much how you figure out anything else you don't know.

**Adam Staravia:** Yeah. If I grabbed the right document, it's 68 pages. I could imagine that's quite a read, for one... Two, who gives the authority for a CA? Who do you get the authorization from to move forward?

**Josh AAS:** Yeah, so you can start a CA and you can do whatever you want as a CA. The question is who trusts you? So if you start a CA and you do whatever you want, pretty much nobody's going to trust you, so it doesn't matter that you're really running a CA. If you're running some sort of private CA, you need your clients to trust you. If you're running a public CA like Let's Encrypt, basically what that means is that the public trusts you. What that comes down to is the browsers trusting you.

So if you want to start a CA, you need at least all the major browsers to trust you. Today, that would be Google, Mozilla, Microsoft, Apple. Those are the big ones. If any one of them doesn't trust you, then this whole thing falls apart. You can't have a website that works in three of those browsers but not on iPhones, or something.

\[27:51\] So when you talk about becoming a publicly-trusted CA, what you're really talking about is getting those four browser makers to trust you... And they all run what are called root programs inside their organizations. And those root programs decide who they trust, and then follow-up on compliance from everybody they've already decided to trust.

So when you start a CA, you need to build your systems, then you need to get them audited against the current auditing guidelines for CA's. Then you take that audit report, and you include it with an application to each one of those root programs. So you're submitting at least four applications to four different root programs, and they all have their different ways of applying.

Some of them are relatively simple emails or bugs to file, and some of them are longer applications. But you apply to all four of them, and then you wait to get accepted. That can take anywhere from three months to three years to get accepted. Then, once you're accepted, you need to wait for them to actually put that trust into the browsers.

So for something like Chrome or Safari, what that means is you're waiting for them to ship a software update that includes your root of trust in it. And until that happens, until a user gets that update, their device still doesn't trust you.

**Adam Staravia:** Wow.

**Josh AAS:** In the case of Microsoft, it's more dynamic. They don't do it through software updates necessarily. If they see a cert they don't understand, they will query a server and check. So trust in the Microsoft ecosystem can be done pretty quickly. Once you're in, you're in. The real problem is stuff like Android in certain parts of the world. People have old Android devices that they don't get updates anymore, and they never get rid of them, and in some cases they're still manufacturing Android for devices... And those things are never going to get an update. So if you want to get those devices to trust you, you're really just talking about waiting for them to leave the ecosystem.

So the point of this is - between the time that you apply for trust and get approved, and then all the devices in the world actually trust you, you're talking about a period of 6–10 years.

**Adam Staravia:** Wow. So commitment is required, I suppose...

**Jerold Santo:** \[laughs\]

**Josh AAS:** Yeah...

**Adam Staravia:** ...without saying so much. You think about some people's plans for new ventures, whether they're small ideas or big ideas; any sort of itch that's scratched. So we talk to a lot of people who scratch itches around here and do something about it, and you have to think about your commitment level to said mission. If you have a horizon of say a year or two years, and you're building a CA, maybe you need to stretch that quite significantly to 5-6, or maybe even further.

**Josh AAS:** Yeah.

**Adam Staravia:** What was your horizon for this? Were you like 10–20 years that you kind of knew all this beforehand, or was it sort of learned as you go? Because you mentioned a lot of this was learning as you go.

**Josh AAS:** So what I've just described is the basic process of getting trusted from scratch. And that does require a big commitment. It requires quite a bit of money to get set up to a point where you can pass audits and even apply, and then every year while you're waiting for all this stuff to happen for 6–10 years you have to stay compliant, get audited every year. So you're talking millions of dollars and 6–10 years before you can even be a publicly-trusted CA in any meaningful sense. That's the basic process.

There is a way to make a shortcut, which is how Let's Encrypt was able to start without waiting 6–10 years first. So we did go through the process that I've just described, building up our own root of trust from scratch... But the world right now does not really rely on that yet, because it has not been long enough.

\[31:52\] And somewhere around mid-to-late next year we're going to switch over to our own root that's trusted from scratch. But from our inception through now, we have what's called a cross-signature... Which means we knew we didn't want to wait 6–10 years to start offering Let's Encrypt services, so we've found another CA that understood what we were trying to do and was willing to help. They had a root of trust that was already trusted.

What essentially happens is we create a contract, an agreement between us, and then their root of trust essentially lends its credibility to us. So they issued a certificate that our root is trusted by their root, and their root is trusted by the browsers, basically. So that's called a cross-signature. We acquired that before we did much of anything... Because without that agreement in place, there's really no CA.

So one of the first things we did was get that agreement, because without that agreement in place, there's no point in buying hardware and doing anything else... Because --

**Adam Staravia:** It's a long journey.

**Josh AAS:** ...we're not going to sit around and do nothing for 6–10 years. So that was a really critical agreement. We got that in place with a company called Iden Trust, who's been a great partner for a while now. So we're trusted through Iden Trust today, and mid-to-late next year we will stop using that cross-signature and just be trusted on our own.

**Adam Staravia:** That's a big deal.

**Josh AAS:** Yeah.

**Adam Staravia:** Will it be transparent, that trust, I suppose? ...since it's still you, it's still trust, it's still the same browser...

**Jerold Santo:** ...unless you're running an old Android device.

**Adam Staravia:** That's right.

**Josh AAS:** Yeah... You know, their root is really widely trusted, and that's been fantastic. And it's trusted all the way back into early Windows XP, and all the Android devices. The problem with that root is, you know, the longer a root is around, the more trusted it is, but eventually it expires. And that root expires next year.

I don't remember the exact lifetime on it, but I think that's a 20-year-old root, at least, if not more than 20 years. So the advantage of an old root is that it has really widely-trusted status, but the disadvantage is that it's going to expire soon. So we will be switching from an old root that's very well trusted, to a younger root that is also very well trusted, but admittedly not quite far back as Iden Trust. But if you're still running Windows XP on the public internet, you might have bigger problems than your certificate. Probably the same goes for ancient versions of Android.

**Adam Staravia:** You'd mentioned the dollars involved for those 6–10 years, and from just growing past blog posts from you or others at Let's Encrypt, it's primarily a people cost, so staff. Is there a lot of cost aside from that when it comes to to fast-track that you took, or the non-fast track? Or the cost is primarily people?

**Josh AAS:** Certainly the cost for us to run the CA today is primarily people. Roughly speaking, paying staff is about two-thirds of what we spend every year. There's startup costs, and then there are ongoing costs. For startup costs - usually, those cross-signing agreements do cost money, and that's a non-trivial amount of money... So when another company agrees to trust a new CA, they are responsible for that trust. If the new CA that they're trusting messes up, it's on them. So in exchange for the liability they're taking on by trusting, in our case, just some guy from Mozilla that walks into the office and says "I'm going to quit my job and start a new CA, and it's going to do all these amazing things. You should trust--"

**Adam Staravia:** Hypothetically, right?

**Josh AAS:** \[35:53\] Yeah... "You should trust us, and put your business and your reputation on the line" - it's not an easy ask. So these cross-signing agreements - there's a lot of liability involved, and for that reason they end up being non-trivial amounts of money. So that's a big startup cost for anybody. Then going forward from that, that's probably the biggest startup-specific cost, aside from maybe initial capital; you're going to need to buy servers, and HSMs, and things like that.

Ongoing, we have to buy a certain amount of hardware every year. We do use some cloud services, we use some external services, but mostly, aside from people, it's about the data centres and what's in them. Publicly-trusted CA's are not allowed to operate in the cloud, so we can't run our CA systems on AWS or GCP or Azure or something like that. We have our own hardware in special, secure rooms inside data centres, and they're not even normal data centres; they're special, walled-off rooms in data centres, with a bunch of extra biometric access, and stuff like that. That stuff is a non-trivial expense, and you've got all this hardware that goes inside, you're going to have a lot of redundancy... So we pay for that stuff, and that's where a lot of the rest of our budget goes.

**Adam Staravia:** Yeah. In a world where Let's Encrypt is ubiquitous, which is what we're getting to - liked you'd mentioned, 2,5 years ago 100 million certificates issued; a month or two ago, a billion. It's quite a massive growth. In a world where Let's Encrypt is ubiquitous, what's the point of other CA's? I'm just thinking, why would anybody not use free?

**Josh AAS:** There's a lot that other CA's do that we don't do. For example, we offer one specific type of certificate. You can't change very much about it. We think shorter certificate lifetimes are better, so we don't let anybody create a certificate that's longer than 90 days in lifetime. And we also don't offer human support. So there are a bunch of reasons to choose other CA's. For one thing, we don't sign this sort of normal contracts; some people have procurement requirements, or they want certain things in contracts from their vendors, and we don't do that. We don't provide support. You can't pay us for 24/7 phone support. If you don't like the type of certificate we offer, and you want something else, or you want it configured in some special way, we don't do that...

So we're sort of one size for everybody, and if that doesn't work for you, then there's luckily a lot of commercial CA's you can go to, and they'll be happy to help you, I'm sure.

**Adam Staravia:** So you're saying Let's Encrypt is for everybody, but not for everybody.

**Josh AAS:** Yeah, it's a pretty basic option. I think it's basic for two reasons. First, we're trying to be a really efficient organization, so... As complicated as running a CA is, we try to scope that complexity and limit it as much as we can. We don't want to offer a ton of choices to people, because complexity just leads to more bugs, more cost, and things like that.

Another thing we're really focused on is best practices. We tend to do whatever we think is the best practice. An example of that is the cryptographic algorithms that we offer, or the certificate lifetimes that we offer... Or you know, you can only get it through certain validation methods the way that we do it, because we think those are the only secure ones, or something like that.

But other people have other opinions. So between trying to be efficient and trying to focus on best practices, we offer a pretty limited service, that I think works for a lot of people, but not everybody.

And the web is huge. We may be serving 200 million sites right now, but there's a lot more than 200 million sites right now, and they should all be using HTTPS. So there needs to be a robust ecosystem of CA's in the world, so that people who need something else besides what Let's Encrypt provides have a place to go.

**Adam Staravia:** \[40:05\] Given the requirements to even be a trusted CA, it doesn't seem like something that there are just handfuls of people listening to the show saying "I'm going to drop what I'm doing today and become a CA." It's just such a long road. I almost think you have to really be invested, I suppose, in securing... And I guess that's a whole different kind of problem or different kind of business. But given the amount of effort it takes to get there.

To start a business today, you have to kind of get to product-market fit. Create a product that people want, and people will buy. In this case, you can do that as a CA, but still not be able to sell it because it takes you so long to become a valid resource for giving it the trust; the trust is such a big deal. It's an interesting business to create.

**Josh AAS:** Yeah, creating a CA is not a decision to take lightly, but the way that most people create CA's now is not to wait for that process to play out.

**Adam Staravia:** They do the cross, like you've done.

**Josh AAS:** A cross-signature... Or you just go acquire another CA. You just buy another CA.

**Adam Staravia:** Wow.

**Josh AAS:** There are at least a hundred existing publicly-trusted CA's. I'm not sure exactly how big the list is. They buy and sell each other all the time. Sometimes they go out of business. I don't remember how many publicly-trusted CA's there are, but there's at least a hundred... And if you want to start a CA, you're going to start a serious business. One way is to go spend x millions of dollars on the cross-sign, or you can spend x millions of dollars just to go buy a CA.

Most of these CA's you've never heard of. They're very small. They're not under-the-couch money, but if you're starting a trucking company, and you need to go buy ten million dollars' worth of trucks - that's something people do all the time. You can probably go buy a CA for something in that order of money, so in some ways it's not really that different from starting any other business, I would imagine. I only have experience with Let's Encrypt in the cross-sign, I've never actually bought another CA... But I don't think that the startup requirements are really that different, just because most people don't wait for the from-scratch process to play out.

**Jerold Santo:** You mentioned the other certificate types. I'm just curious on your thoughts on extended validation certificates and the idea of wrapping up identity into encryption; establishing a secure connection. And then you also have this extended validation, so you know at least the CA trusts that the person who owns the certificate is who they claim to be. What are your thoughts on that style? I know you don't offer it, but is it worthwhile?

**Josh AAS:** I don't know if I can say whether that's worthwhile for any particular -- you know, some people have specific needs, regulatory needs, or whatever... So I don't know if I can say whether that's worth any individual in general should do it. But I do have some thoughts... First, trying to include the identity of a legal organization in a cert does not affect encryption at all. You can't tie the two together. You can put them in the same cert next to each other, but EV certs and OV certs, which contain this legal identity information - the encryption is no different from a DV cert. It's the same.

The only theoretical value to that is if you display the identity to the user, and then let the user make a decision based on the identity they see. The problem there is -- well, there's a bunch of them. First, browsers are increasingly not showing that information to users, so there's no point in having it in the cert if the browsers aren't going to show it to them. And the reason the browsers aren't showing it as much anymore is that most researches show that people either don't look at it at all, or don't understand it when they do see it.

\[44:02\] So you're not going to build a secure system that relies on the average user on the internet looking at information and making informed decisions. That's just not how security works. If that's your plan, it's not gonna result in generally increased security for anybody. It only works when it happens automatically, and doesn't require people to look into it individually.

There's a bank out there called USA, and if you look at an EV cert from them, it says "United Something Automobile Something". The spelled out name of the business is very long, and nobody knows what USA stands for. They just know the bank has USA. So when you see that kind of information pop up in an EV cert, how can you possibly expect anybody to make a reasonable decision about that.

So I don't think that it's very useful to put identity information in a certificate that's used on the general internet... And the research backs that up, and browsers tend to agree and are dropping that from the UI.

**Adam Staravia:** Yeah, that's true.

**Josh AAS:** I don't have any stake in this - we don't issue it - so in some ways I don't really care, but it seems not very helpful, and probably it's not going to have a strong future on the internet.

**Jerold Santo:** No, I was just curious your thoughts on it.

**Adam Staravia:** I think at one point it was interesting because it was different. Not all certificates you've got gave you the option. So I can recall a day whenever you to GitHub.com, and it would say separately, twice almost; someone's double-branding even. You know, heavy on the brand side.

**Jerold Santo:** With a big, green background, and then it was like very official...

**Jerold Santo:** Yeah, it seemed official. It seemed cool, it seemed secure. So I would think - which I don't know all the research behind it, but from a UI perspective it's probably cumbersome because it's redundant... But it looked different from someone who didn't pay anything for their certificate, or didn't buy a certificate and then offered that... And it was unique. So you would see it happen on people who would want to pay for it, I suppose.

**Josh AAS:** Yeah... The problem there is that once you see it, it might seem like a good thing to you... Although, again, the research shows that people don't really react to it in a useful way. The problem is you don't notice the absence of it.

**Jerold Santo:** Right.

**Josh AAS:** If GitHub just didn't have that, you wouldn't say "Hey, it doesn't have that thing. I'm going to leave."

**Adam Staravia:** Yeah. I may hop onto GitHub today, and it doesn't have it today. I don't care.

**Josh AAS:** Right. So it just turns out not to be very useful. And also, there are a lot of issues with how it's validated. In domain validation, where you're just proving control of a server before you issue a cert, there are pretty clear and strong ways to do that validation. When people do identity validation, it basically involves phone calls, and faxing around document copies of your articles of incorporation, and copies of driver's licenses, and stuff like that. It's easier to mess with.

Pretty famously, recently someone registered Stripe Inc. in some state that's not where the normal Stripe payment company is... And since registration of businesses is by state, they had an EV cert that they had Stripe Inc. Obviously, that's not what you'd expect, but it's not a bad cert. They legitimately did own Stripe Inc. in North Carolina, or wherever it was that they did.

**Jerold Santo:** Right. It's like a namespace conflict, but it wasn't inappropriate. The CA that issued that certificate could have gone out to their business and got their articles of incorporation, and all the stuff, in the state that they're in. So it's completely valid.

**Josh AAS:** \[47:57\] Yeah. There's ultimately nothing wrong with that cert; they sort of arbitrarily revoked the cert, because they say "Well, we just don't like that cert." It brings a lot of arbitrariness into it. And that is a cool party trick, and it demonstrates some problems with EV certs, but the real issue is that nobody seems to care what's in the cert anyway, so it doesn't matter if you -- you know, nobody really looks at it or makes security decisions on the basis of that stuff anyway, so it doesn't matter. Namespace conflicts are sort of a second-order issue.

**Jerold Santo:** Right. I think it's interesting that it was for a time almost like a status symbol amongst technology companies to have that. It was like "We've arrived" or "We have enough money to buy the more expensive--", whatever it is. And really the browsers -- like you said, the browsers, when they started to move that out of the way, in the browsers, when the vendors say "Yeah, let's just go ahead... No one looks at it, except for nerds..." Most people don't even look at the address bar. They don't even know it exists, which is why the number one thing people google is "Google" or "Facebook". They google Facebook to go to facebook.com, when they could just type it into their address bars, because people don't...

**Adam Staravia:** Yeah, they're missing four characters...

**Jerold Santo:** ...look at the address bar, let alone "Is the background green? Does it have the thing?" You know... So really the browser vendors made that not a thing. I mean... That's super-interesting. They've kind of like -- because that was an advantage of a certain certificate or another; or it's kind of an upsell. Isn't it always an upsell? "Hey, get the Extended Validation Cert." And it's like, just the movements of the web, and the decision-making of the browser vendors basically just quashed the value there, because it was really only in the status symbol, like you said.

**Josh AAS:** Yeah. I mean, "the advantage" is not really an advantage, because it doesn't actually mean anything. It just takes up a bunch of UI space.

**Jerold Santo:** It's kind of fascinating.

**Josh AAS:** Yeah... Again, if your plan for security is to show average users some information and then expect them to make a perfect decision based on that information, that is not ever going to work. It doesn't work for EV, it doesn't work for anything else.

**Break:** \[50:21\]

**Jerold Santo:** So Josh, we've been talking about Let's Encrypt's success over the five(ish) years you've been doing this. A lot has changed since the beginning, a lot has changed since 2017 when we had Jacob on the show saying "Let's encrypt the web", mostly extreme amounts of adoption. You have some stats in your billion certificates blog post that in June 2017 approximately 59% of page loads used HTTPS globally, 64% in the U.S., and today that's 81% of page loads use HTTPS globally. I think you mentioned that earlier in the conversation. And we're at 91% in the United States. I wanted to reiterate that... That's a massive number. 91% in the U.S. So you guys have played a large role in that. And I'm curious, because there's also been -- like, the web has changed alongside you, and the trends are changing, and security is more important, and all these things... So I'm curious, how much do you feel you've been pushing this up the hill, and how much do you feel that maybe you've been riding a wave in the last couple of years?

**Josh AAS:** It doesn't feel like pushing it up a hill so much. I think there was a lot of demand. I think developers understand that using HTTPS is a good thing; they understand that without it, you're not secure. Furthermore, I don't think it's hard to convince most of them to do it. Furthermore, I think they're ready to do it if they have a reasonable option for doing it... And by reasonable I mean very easy to use.

\[52:25\] So we've put our service out there, and it's not that hard to convince people to use Let's Encrypt. We don't really market or engage in too many activities around really trying to convince people to use Let's Encrypt. Most of our efforts revolve around trying to get people to give back for using Let's Encrypt, and keep stuff going. But yeah, it definitely doesn't feel like pushing something uphill. It feels like people want to do the right thing, they just need the tools. And now they have them.

**Jerold Santo:** I think the developer mindset - it's my own personal opinion and experience - has changed, probably from "You should encrypt anything that's important...", I'm talking like 3–5 years ago that was kind of the ethos... Anything important - if you're signing in, obviously if you're making e-commerce transactions - those things should all be encrypted. Taking passwords etc. But that's pretty much what needs to be encrypted. And I think nowadays, generally speaking, the ethos is "Just encrypt it all."

**Adam Staravia:** All things.

**Jerold Santo:** Encrypt all the things.

**Josh AAS:** Yeah. The thing that gets me about the first argument, that only important things should be encrypted, is that people need to remember that when data is not encrypted, not only can it be read by other people, but it can be modified. So any unencrypted traffic can have stuff injected into it. And it doesn't matter whether that traffic is important or not. So if you're on your banking website in one tab, and you think "Oh, that's important. That needs to be encrypted", and you're over in another tab looking at memes, or something, and you think "These things are not important. These are just some mass-media GIFs flying around the internet. Why does that need to be encrypted?", the problem is that unencrypted traffic can be modified. So you can have malware or some kind of exploit loaded into the traffic for that tab, that exploits your computer and now does stuff with your banking info, because they owned your browser through the unencrypted traffic in the meme tab.

**Jerold Santo:** Don't go changing our memes.

**Josh AAS:** It is really not a good idea to try to draw distinctions between what is important and what is not, because it's all exploitable in the same ways, and that line just never gets drawn in the right place.

**Adam Staravia:** Yeah. Which makes celebrating a billion certificates all that more important, because you started out at the bottom, and now you're here, to use a rap song very wisely...

**Jerold Santo:** \[laughs\]

**Adam Staravia:** And that's the thing...

**Jerold Santo:** You used that rap song very wisely.

**Adam Staravia:** ... I mean, in 2017 a hundred million, and now you're at a billion, five years later - that's a big deal, and that means that so much more traffic and so many more people are not getting advantage taken over them. Or the opportunity to get the advantage taken over them because of being secure. And in a day prior to this, it cost money to enter; not that the money factor -- I think it was just a barrier to the entry to using SSL, for the Periods and the's of the world before, who said "Hey, only important traffic needs to be encrypted." And now it's like "Well, everything. For those reasons." And that's a big deal.

You mentioned that you haven't done much to get there, so -- I mean, going from zero to a hundred million, to a billion, no marketing, not much involved, just mostly community work, when you have to account for how you got here, how did you get here? What are the things you did to do that, specifically?

**Josh AAS:** \[55:58\] Well, like I said, there was a lot of pent-up demand, and we gave people the tools, and we made them easy to use. That's really the gist of it. And then some people start doing the right thing, you get the numbers high enough, and then the mindset of the world switches from "HTTPS is an optional thing that you can have if you want to spend time doing that" to "HTTPS is the standard thing that you need to do all the time, and if you don't do it, you have a problem."

One of the biggest accomplishments for us and for everybody -- you know, it's not just Let's Encrypt; we're not the only reason the web is where it is today. There's lots of different people working on different great projects around the world that have helped promote HTTPS... But one of the big accomplishments of that community is that HTTPS is considered the standard today.

**Adam Staravia:** Yeah.

**Josh AAS:** You set up a website. If you expect people to visit it, you need to have HTTPS. That's a huge mindset change. \[unintelligible 00:56:56.02\] ways in which the internet has changed similarly in the past for other technologies. It is hard for me to imagine -- or, not imagine... I don't know everything about the history of the internet, but I don't remember any other thing fundamentally changes how almost all this traffic flows across the internet in less than five years. I can't think of another watershed change to how the internet functionally works that played out that quickly. Furthermore, I'm a huge fan of IPv6, but that transition has been dragging out for a long time...

**Jerold Santo:** It's the slowest transition of all time.

**Josh AAS:** You know... And when we started Let's Encrypt, we were thinking "This cannot be an IPv6 trend line. It can't be that way. We've got to make sure this happens much faster than that."

There are a lot of other improvements to make to the internet, too. I hope this serves as an example of "If we want to make a change, we can do it." There's a bunch of other stuff we should fix. It is possible to change major parts of how the internet works in big ways, in a few years, under the right circumstances, with the right plan.

**Adam Staravia:** What you're sharing - it reminds me of this idea that I haven't quite verbalized yet, but it's this cog mentality. If you've ever heard of Seth Godwin, he wrote a book called Linchpin. The idea is to be a linchpin. I think, in many ways, as individuals, we try to be really important... And that kind of goes against the idea of cog mentality, which means that you're just a very sharp, very specific, very purposeful thing, as part of a much bigger, much more grand whole machine. So if it weren't for theare of the world, Josh, doing Let's Encrypt and all the effort here, then the browsers wouldn't be able to its thing, and then the site developers wouldn't be able to do their thing... So all these things are sort of in concert. A system. So this idea of a cog mentality really rings true here.

**Josh AAS:** Yeah. Well, we're happy to do what we do. But like I said, there's a lot of people who play in this. Running CA servers and providing the APIs is an important part of this, but we wouldn't be anywhere near where we are today if there weren't hundreds of people out there writing ACME protocol clients that work with Let's Encrypt, so people can just download software \[unintelligible 00:59:17.06\] it works.

The browsers have done a great job incentivizing moves to HTTPS by limiting new technology to HTTPS connections, and some UI work, things like that. So it's been the browsers, it's been the open source community, Let's Encrypt... Lots of people involved. Even within Let's Encrypt, there's so many people involved in it. There are the engineers that work on it, our sponsors, our funders... That's huge. We don't go anywhere unless somebody decides to write a pretty big check. And people who make those decisions, to write those checks - I feel like they often don't get enough credit, because it's not fun and open source-y, but that's a big deal.

So the fact that there are people out there and companies that understand what we're trying to do, and they're willing to write those checks, and stand up and really make the internet better - that's where it starts.

**Jerold Santo:** \[01:00:16.04\] Are there any standout organizations that have been supporting you, either in big ways, or for a long time, that you'd like to give a shoutout to? Because like you said, they don't get much credit. Maybe a logo on a web page somewhere. But do you have any major supporters? Like "We wouldn't be here if it weren't for this company, or this organization."

**Josh AAS:** Yeah, we've got over 70 corporate sponsors, so I'm definitely not going to be able to list them all here... But our platinum sponsors are our biggest supporters; they write the biggest checks, and they've been fantastic. Companies don't make the decisions, people inside those companies make the decisions, and I'm so glad that those people understand what we're doing and get it done.

Our platinum sponsors right now are Mozilla, Cisco, Electronic Frontier Foundation, OVH - a company that I think not a ton of people in the U.S. have heard of, but they're a great, huge cloud provider in Europe, and they have just been fantastic since very early on. And Google, specifically the Google Chrome team.

**Jerold Santo:** One thing that's amazing is what you've done with that money. In that same post, you talk about how you're serving 4x the websites that you were back then. And of course, now here you are at 200 million, so even more websites... And your budget hasn't increased 4x, or anywhere near that. You went from a 2.61 million annual budget in 2017 to 3.35 million now, and from 11 staff members to 13 staff members. So only adding two staff members in the course of three years, and 4x in your websites served - that's pretty good numbers.

**Josh AAS:** Yeah, internally we are obsessed with efficiency. Like I said, it's a huge deal for people to entrust us with millions of dollars over a year. There's a lot of good in the world that money can do. So when that money comes to us, it's our obligation to make sure that we use it wisely, and do the most good we can do with it. That means delivering the best service, to the most people that we can. We take that responsibility to be good shepherds of that money really seriously.

So whenever we talk about a new service, or like a new feature, or some way in which we're going to expand our service, we have a bunch of things that we think about to make sure that we're being efficient. One of the most important things is "Does it require any people to be involved with anything, anywhere on the chain?"

One of the reasons we don't offer phone support is if we did, we would have to fill a skyscraper with people sitting by the phone. So when we think about delivering a feature, that feature cannot require support. We need to make sure that it's so easy to use and so easy to document and so easy to automate that the people consuming the feature should not need support. Even the people who are the least technical. It should just happen. If they do need support, it should be as simple as reading a very easy to find a bit of documentation.

So ease of use is, again, hugely important for efficiency. If it's easy to use, then people don't need to talk to you as much. If even some very small part of 1% of the people using Let's Encrypt needed to actually talk to us on the phone about something, that would just be overwhelming. We can't do that. So everything has to be very easy to use.

Internally, we think a lot about how much data do we store. We're basically allergic to data. We only really hold on to what we really need to hold on to for either compliance purposes or to debug our own systems.

\[01:03:56.22\] But aside from that, we don't want to have more sensitive information than we need, we don't want to be sitting on piles of information where we have to pay for storage servers and things like that. We tend to just do what we need to do and not hold on tons of data. When we need to use an external service, we often find partners who are willing to provide the service free of charge to us, essentially as sponsors or donors.

We're just very concerned about efficiencies, so we're only 13 people today. We have a lot of specialized systems, but it's probably -- I don't know what people imagine we run when they think about what is Let's Encrypt's actual hardware, but it's like about three racks full of hardware. It's not a ton of hardware. It's all very carefully maintained in some ways, but you can fit -- you know, modern servers are crazy powerful. You can fit a lot of stuff in there, you don't need a lot of physical space.

We've got a couple different data centres, maybe three racks of hardware between them, and that's triple-redundant. In theory, if we needed to, we could just run the CA out of one rack hardware, and that would serve all 200 million sites pretty easily.

So if you automate everything and get computers to do all the work for you, you can be pretty efficient. It still requires -- I think this year we're going to spend a little under four million dollars, but that's really not that much money. I'm fairly confident that there are Fortune 500 companies out there that spend more than four million dollars on their internal PKI systems.

**Jerold Santo:** Right. So you mentioned earlier that you weren't sure you wanted to even spend the next five years of your life doing this, doing a CA, but you felt like somebody had to do it, and you were well-positioned and willing to. Here we are, you've done over a billion certificates, 200 million sites served, all these big numbers... And I think more importantly, those global trends, which from the very beginning you all have said you wanted to encrypt the whole web. The global trends I think are probably more important to you than Let's Encrypt's footprint on that. 81% globally, 91% in the U.S. Do you feel like Let's Encrypt has accomplished its mission? Is there still a lot left to do?

**Josh AAS:** Well, in the U.S. there's still 9% of page loads that are not encrypted. Globally it's still 19%.

**Jerold Santo:** \[laughs\]

**Josh AAS:** And I think if you're an engineer, you probably understand what I mean when I say something like "90% of the work is involved in finishing the last 10%." The 10% or 20% around the world that haven't moved to HTTPS yet, they're almost by definition the ones that are hardest to reach. They either don't know, or they don't have the tools, or they have some reason why they haven't switched, and it's the people for whom it was easy to switch have mostly already done it.

So I think that last 10% is going to be pretty -- it's not going to be as easy as the 10% before that. And also, this service needs to continue going. I don't know how long Let's Encrypt is going to need to be around, but it's quite possible that it'll be around 10, 20, 30 years. I have no idea. But it's not like once you've encrypted a site, your work is done. You've got to continue to issue new certificates on a regular basis.

So we need to be around for that, and in order to be around for that, we need to stay on the top of our game in terms of compliance and security. At the end of the day, people need to trust us. That's what it really comes down to. We're never done because trust is never done. If at any point the world loses confidence in us, we can either lose trust technically, where browsers don't trust us on a cryptographic level; if our donors don't trust us, we don't get the money we need to continue... So the job is certainly not done. We need to maintain high standards and stay trusted for a long time now.

I wasn't exactly thrilled about the idea of spending a huge chunk of my life building a CA and running it, but it turned out to be really great. It puts me in contact with so many people that are really passionate about making the web a better place, and that's something I am very happy with. I love working with our board members, and our partners, and our community. I can have enthusiasm on tap anytime I want it, just calling people up and talking about what's happening to us. So it's turned out to be great, and our staff are wonderful, so as a job, I really couldn't ask for more.

**Adam Staravia:** \[01:08:25.02\] Yeah, the benefits of a job often outweigh the job itself. Sometimes you don't really care for the job itself, or the mission... Not so much the mission-mission, but the fact that you get to interface with so many people who care - it's got to be uplifting for you.

In light of what Jerold asked you, I'm sure that this will be a little easier for you to answer - or maybe not - but what's on the horizon for you? Big picture. You mentioned 10, 30 years down the road, so you've got to have some sort of idea... Give us a snapshot, maybe 1–2 years in the future. What's something the nearest on the horizon not many people know about, that is something you can share today?

**Josh AAS:** Well, we're going to keep grinding and finishing encrypting the rest of the web; that we've already talked about. There are so many more things that need to be worked on... I don't know that -- you know, Let's Encrypt permission is pretty well scoped. We issue certificates, and our goal is to do 100% encryption, and be entrusted while we do that. In some ways, that's a very narrow scope, and it's a part of why we have done well, I think. But I think in doing this work, we've realized there are a bunch of other issues on the web that we need to solve. A couple of the ones that are top of my mind are -- there's a protocol called Border Gateway Protocol (BGP), and that is the protocol that's used to decide how and where traffic gets routed around the internet.

So if you're going to send a packet from Seattle to Philadelphia, what exact route is that going to take to get there. That's all determined by BGP. That protocol is not secure. It's very vulnerable, and I think the only reason it hasn't been exploited more is it's not very popular. People don't know about it, the attackers don't know about it. They've also had easier targets, but...

For as many security problems as we have, we've done a pretty good job working on them, and I think a useful way to think about the next 10–20 years of security is that I think we're going to keep pushing attackers down the stack. You improve application layer security, and then maybe the next step down the stack is the transport layer, or something like that. HTTPS, you encrypt that, and then the attacker has got a move on from there. And right now, I think the next layer down that has not been exploited to its full potential yet is BGP. I think of that as the soft underbelly of the internet. Attackers are going to take notice of it, and they are going to get better at it, and they can cause massive outages by doing that, they can reroute traffic wherever they want...

So I'm concerned about BGP, and that has some pretty direct impact on Let's Encrypt, in that certain types of BGP exploits can be used to mess with certificate issuance processes. That's true of any CA, it's not specific to Let's Encrypt; it's just part of our risk profile as an industry. But it's a hard thing to secure.

So I'm very interested in what we can do about BGP security going forward. That's going to require a lot of the big companies that operate the major pathways on the internet to change how they do things. So that's one thing I'm interested in, and we do some work around that at Let's Encrypt to mitigate the problem right now, and also try to invest a little bit in the long-term solutions there.

**Adam Staravia:** Interesting.

**Josh AAS:** \[01:11:54.27\] Another thing that both affects us and that I'm personally pretty passionate about is memory safety. In the same way that it seems crazy to us now that you would start a major website and not use HTTPS - we know so much about the risk of that, and it just seems crazy to do that now - I think we're also going to come to a point where we feel like it is crazy how people say stuff like "Well, I'm running a bank and I need to do some reverse-proxying, so I'm gonna spin up an instance of NGINX or Apache and do my reverse load balancing." Because what you're really saying there is "Why don't I just stick several million lines of C code on the edge of my network? And that'll probably be fine." That code is not safe.

We certainly should not be writing any new code in C and C++. The opportunity for vulnerabilities -- I mean, it absolutely will have vulnerabilities, and we need to get that type of code away from our networks to start with, and then probably away from most other things, too... So I would hope that in 10–20 years we think it's crazy to be deploying major (or maybe even minor) pieces of software that are written in languages that are not memory-safe.

So we're trying to remove code written in C and C++ from our infrastructure at Let's Encrypt. I think that's just a basic part of diligence applied to secure infrastructure. If your stack is some giant pile of C++ or C at the network edge, followed by OpenSSL written in C, followed by a Linux kernel written in C, glib - your whole pathway has got all this code that you just know is full of security holes. It absolutely is. You just can't claim that those are even close to secure systems. They're absolutely not. We're going to look back on this and say "That was crazy. We have better options today."

So we're trying to remove that kind of code from inside Let's Encrypt, because it's a huge liability, but we/I am looking into ways that we can try to move the needle on this problem in software in general.

**Adam Staravia:** What's your first step, do you think? What are some of your early insights on moving that needle?

**Josh AAS:** The first step is don't write any new code in C and C++, or any other memory-unsafe language. That should just be a given. If you can tolerate a garbage collector, if that's fine, then you have a ton of options - Java, Go, whatever. If you want a memory-safe language that doesn't use a garbage collector, go use Rust. You have that option now.

**Jerold Santo:** It seems like the next step would be having viable replacements for a lot of the software that's already out there.

**Josh AAS:** Yeah. The next step is we need to rewrite all the software that we already wrote in C and C++, and replace it. And when I tell people that, the most common reaction is like "You can't possibly expect us to rewrite the world. That's so unreasonable. You're not a realistic person when you say that." And you know, I really strongly object to that reaction. We're in a world full of talented people who care, and we can absolutely accomplish that if we want to.

If your goal is to rewrite a major web server or a major proxy server, or a major library or whatever, in Rust - let's just do it. Yeah, it'll take five years, it'll introduce some logic bugs along the way that will get fixed, but in the end, this software is going to be around for a very long time. And we need to eliminate that massive class of bugs, because vulnerability scanning, and audits, and static analysis, pentesting - that stuff doesn't even begin to deal with the problem. It's a good thing to do if you're stuck with C and C++, but it's absolutely not going to eliminate the bugs. That's just not going to go away until you rewrite it.

\[01:16:05.22\] What we're doing right now, where we just spin up giant piles of C and C++ without thinking about it is -- we should not be doing that. We can't be doing that 10–20 years from now if we want to try to have a more secure world than we have now. So I think we need to think bigger. We just need to think like "Yeah, let's rewrite the world." Rewriting a big web server is a big project, but I'm sure there are teams at any number of companies that could accomplish it on their own without a help, if they just decide to do it. Yeah, it'll be five years, but whatever; five years from now, you put in some effort, and now you've got a much more secure software system.

So I'd like to just see some more ambition and some more optimistic thinking about this stuff. I think it's really important. I don't want to be suffering from buffer overflows in everyday software that sits on the network edge 10–20 years from now.

**Adam Staravia:** My guess, Josh, is that you're well-positioned to encourage, considering what you've done in the last five years... Going from zero to a billion certificates issued is a big deal; you've found a way to create a CA in a world where it's very difficult. Obviously, there are protocols by -- was it the cross-signature? Is that what it's called?

**Josh AAS:** Yeah, cross-signature.

**Adam Staravia:** Cross-signature. Just that alone, that was a smart play, and you've been able to do so much... So I think you've probably piqued our interest, and as well many listeners listening to this show by saying so. We need you out there petitioning for this, and encouraging those out there that can do this to take on this mission to do so, and not look at the five or ten years that it might take to do it. We see such blowback when we don't consider the large-scale costs over many years. If this software isn't going to go anywhere in the next 10, 20 or 30 years, then we're going to rely on it. And just like securing the web is more important than it has ever been, having secure software that doesn't have memory issues or unsafe memory where you can do these things, it seems so clear to me.

**Josh AAS:** Yeah. It's got to happen.

**Adam Staravia:** Josh, thank you so much for your mission. Thank you so much for Let's Encrypt and the work you all have done; to you and the team. I know you're not a lone soldier in this mission, but the many behind you enabling this. But without you and many others doing this, we would have 51% less internet secured, so thank you very much for that. We appreciate your mission, and we appreciate you. Thank you, Josh.

**Josh AAS:** Thank you so much.
