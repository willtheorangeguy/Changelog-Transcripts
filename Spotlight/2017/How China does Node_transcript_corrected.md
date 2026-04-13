**Adam Staravia:** \[01:05\] In this episode I talked to Shiva Lou about how China does Node; software development is done very differently in China, pretty much because of the slow translations of documentation and books from English to Chinese, but also because of this Great Firewall of China you've heard about. It's a censorship and surveillance project by the government, and it makes it very hard to interact with the rest of the web. Let's take a listen.

\* \* \*

**Adam Staravia:** Let's start with what your name is and where you're from.

**Shiva Lou:** My name is Shiva, I am from China. I moved to the U.S. when I was 14, and I stayed there for about eight years, and then I moved back to China for a year. Now here we are, I've already been back for about a year or so, so that's why I'm here at the conference, to share a little bit about my experience, transitioning between the two worlds.

**Adam Staravia:** For those out there in the developer world - and any world, really - we hear about news from other countries, right? I've definitely heard about, but haven't looked too deeply into, because I guess it didn't matter to me - not so much like negatively, but it didn't impact my day-to-day life, so I didn't look much further into it. But I've heard about the Great Firewall of China, and I'm aware of this; I'm aware that China is a communist country, and you have different ways you live there than we do here in the United States. But for the web, we're sort of like a global economy, right? We're global people, where our national borders define us and separate us, but on the web we're a bit more like family.

**Shiva Lou:** Right.

**Adam Staravia:** So kind of give me a peek into your experience then, having lived and grown up in China, then moved here, then moved back... What's been your experience with the way we do the internet, I guess?

**Shiva Lou:** Okay. I'm going to start off by saying that China isn't really a communist country.

**Adam Staravia:** It's not...? Where does that come from?

**Shiva Lou:** I guess because the central party is called the Communist Party, but it's not exactly what you would picture what a communist regime is like... Although I don't really wanna talk much about politics...

**Adam Staravia:** No, I'm just glad you corrected me there. I don't want to put any misinformation out there, it's not my intent.

**Shiva Lou:** Okay. So I came to the U.S. in 2007, and at that time the Great Firewall wasn't built yet. Everything was open, Facebook was available, Wikipedia was as well, and I logged on to all these websites back home. In about 2008 and onwards, the Great Firewall started getting built, and it's been perfected over the years, and more and more websites -- at first it was just Facebook and Twitter, and then they added Gmail and Google, and a lot of other big websites that you would use in your day-to-day life in the U.S.

\[03:59\] That causes us a lot of trouble in the developer world, because everyone's used to use Google CDN or put a Facebook login on your site - that is just never gonna work in China, because the mass majority actually don't have access to these websites. I guess when transitioning from the two worlds, the biggest thing is that you have to change your habits a lot, from googling to like using Bing or Baidu, and you basically kind of lose contact with your friends on Facebook, because it just slows you down a lot more.

**Adam Staravia:** So these networks that we're so used to using actually are bubbles.

**Shiva Lou:** Right, yeah.

**Adam Staravia:** We don't think about it like that; we think that we create our own bubbles by choosing our friends, our networks or whatever, or the communities that we're involved in, I guess just by choosing one like Google. So Bing works in China?

**Shiva Lou:** Yeah.

**Adam Staravia:** How did they get around it?

**Shiva Lou:** Well, Microsoft has pretty good relations with the Chinese government.

**Adam Staravia:** But Google doesn't.

**Shiva Lou:** Google doesn't. Google is more of an internet company, and Microsoft started off as a software company, and that is how the basis went.

**Adam Staravia:** So give me the basis of your talk, then. You're obviously sharing some of your experiences with living behind a firewall, living behind, basically -- what would you call that? Separation? How do you describe this firewall and what it does to the community behind it?

**Shiva Lou:** Okay, so it's a very common practice for developers to log on to a VPN, that then goes across the borders every day, for work. That's the first thing that you do every day, to start working. For us, in the beginning it's actually okay, since as long as you are on VPN you can have access to everything... But VPN has always been on the hunt...

**Adam Staravia:** On the what?

**Shiva Lou:** We're on the hunt by either the security departments...

**Adam Staravia:** They're looking for you?

**Shiva Lou:** Right, right. So I was using one when I just went back, and then three months later it closed, so I had to use another service. A lot of my friends set up their own foreign servers. I just ended up using some services, and it's constantly unstable, and you have to look for the newest, best ones.

**Adam Staravia:** Okay. So I guess the thing I'm trying to figure out is that outside of the personal experience you've had as a developer, as someone trying to build stuff, for sure here in the United States - or even in other countries outside of China, I guess, from this example - we're used to, if there's information for how to be a better software developer, we pretty much have access to it if it's open, right? But that's not the case for China.

**Shiva Lou:** Right. I will say that the first lesson for software developers is how to connect to VPN on your own. Then I think the biggest barrier there still though is language, much less of developer experience in terms of whether you can get across, because for us developers, we can always get across.

**Adam Staravia:** Right. I was taking notice to something that's near and dear to us here at this conference (Node Interactive). Obviously, around a Node Conference, anybody who is in the Node community knows what NPM is, so seeing CPM, which is China's NPM -- so you had the language barrier, but then you also have this firewall barrier. Talk about the language barrier first. Clearly, from here to South America there's a language barrier; from here to China, there's a language barrier; from here to Germany as well... So there's a language barrier everywhere. What is your example of experiencing this language barrier?

**Shiva Lou:** \[08:15\] Right. I think the language barrier is only an issue in countries that don't use English as the working language. In China, a framework or an open source project like Node is only going to be popular if it has Chinese documentation and advocates in China. So very luckily for Node, there was a few very early adopters in China who wrote books on Node, and that's what people base their learning and studying from. I see a lot more people reading books than reading online documentations, surprisingly.

**Adam Staravia:** Really? Wow... So they actually have an in-hand, physical books, versus online documentation.

**Shiva Lou:** Yes, right.

**Adam Staravia:** Solve that problem, somebody.

**Shiva Lou:** Yeah...

**Adam Staravia:** So how current are these books? How often does a popular or somewhat popular software development book get translated?

**Shiva Lou:** I would say it depends on -- I'm not sure exactly how it works, but I think the more popular (O'Reilly books, for example) have a translation in the pipeline as soon as it's released.

**Adam Staravia:** Right. So they're released in English -- do they release all the languages, too? The reason why I ask that question is because you said earlier "working language." I think what you mean by that is if I'm a professional, and I'm doing work or something work-related, or something like that, then when you go to work you speak English. That's not the case in China.

**Shiva Lou:** No.

**Adam Staravia:** Are you familiar with other countries how often it's not the working language?

**Shiva Lou:** For example Japan is one of the bigger countries with English as a working language.

**Adam Staravia:** Right. So in Japan they don't go to work and speak Japanese, they go to work and speak English, primarily?

**Shiva Lou:** No, they would speak Japanese...

**Adam Staravia:** But they would read English...?

**Shiva Lou:** It depends on the company. Is it an international company that's primarily US-based? Most of our co-workers, even in China and Japan will speak professional English and write pretty good English, but it is harder beyond that. It's hard to make pleasantries in English.

**Adam Staravia:** Right. So with your talk, what were you really trying to make people aware of? What was the core goal for you?

**Shiva Lou:** Okay, so while I was in the U.S. I'd also never consider how certain websites are inaccessible in China. When I build my own site, I just use Google CDN, or Facebook logins and all these features, but when I'm back in China it's such a big problem, and also, there are so many internet users in China that it just can't get ignored.

The practice of people getting around these problems are very counter-intuitive than what we believe that are good practices in web development. I guess this talk is really just for people to be aware that there are these caveats that you need to think about when you have visitors from other countries. There's so many people using internet in China right now, that you're just going to get so much more volume if you have a website that's China-friendly.

**Adam Staravia:** That's a good thing, I like that, China-friendly. I'm China-friendly. I mean, I want to be friendly with everybody. We're obviously at a developer conference...

**Shiva Lou:** Right.

**Adam Staravia:** \[11:54\] I'm thinking to myself as you're saying that, "Who does that matter most to?" It's almost like when you say accessibility to the web, if I don't have an application that has a lot of users who maybe have accessibility problems - and language is definitely one of them - to me, it's like, for developers it totally makes sense that we should have translations; it totally makes sense for O'Reilly to ship a book not only in English but in any other native language where there's a need for it.

This message you're sharing about the language barrier, about being able to tap into the large China audience - who does that come up most to? Is it developers? Obviously when someone like Facebook builds what they built, their network, they're going to think, "Well, we should probably make it as accessible to anybody in the world as we can", but who does that matter most to, this idea you're sharing?

**Shiva Lou:** I think for us as a company - Autodesk has a lot of customers and partners in China. However, a lot of the engineering teams are in the U.S., so when they were developing, in the beginning they weren't thinking about these users in China. So if you're not thinking about the China market, it's fine...

**Adam Staravia:** That's what I mean. If it's not a part of your business model... Not that it doesn't matter, by any means, but if it's not my focus...

**Shiva Lou:** Right, yeah. If you already have customers in China, then you should be thinking about them.

**Adam Staravia:** But see, personally it is of interest to me, because I had never considered it; we run podcasts. I want everybody to listen to it. Now, naturally I speak English, that's my primary language, so I don't think it'd be worth it to me to have my podcast translated... However, we could transcript them - which we are doing - and those could easily be transcribed to different languages if we wanted to... But it is important to me to be inclusive to the whole world, including China, of course. I mean, you have so many people there... I would want anyone there who cares about the things that we care about, which is open source software development, open community, inclusivity, diversity - all those things that we really care about, I'd want them to be able to listen to my shows, too.

For someone like me, who uses Vastly as our CDN, which is a US-based company, what would happen if someone goes to Changelog.com? Our servers are Linde servers, they're based in the United States, our CDN is an international CDN... How would someone from China be impacted by going to Changelog.com? Would they be able to listen to my shows or would they not be able to?

**Shiva Lou:** They would be able to.

**Adam Staravia:** We don't force them to use Facebook, we don't use Google CDN... We have our own CDN.

**Shiva Lou:** Okay, cool. Well, any server that's outside the borders is going to be a bit slower than servers that are within the borders. So you're looking at a page load time of a couple seconds instead of milliseconds.

**Adam Staravia:** Yeah, milliseconds, for sure. We focus on speed.

**Shiva Lou:** Yeah. Then you definitely would need to have servers in China.

**Adam Staravia:** Plus, we built the website just for fun. We built it in Elixir, which is known to be pretty fast, because it sits on top of the Erlang VM, and we used Phoenix the web framework, and we purposefully used a smaller JavaScript footprint. We purposely didn't use frameworks that would have more than we needed just to have a couple features. Furthermore, we actually wrote our own JavaScript for our own web player; so we did some things to kind of keep it fast, for those reasons.

So for people like us, or people that aspire to be like us, to have that kind of focus, with speed and our own CDN, what can they get right, I guess? Using our own CDN, that's obviously helpful, but you've mentioned the speed barrier... What's the speed roughly for outside the borders? I'm just curious.

**Shiva Lou:** \[16:02\] It really depends on the weather.

**Adam Staravia:** It depends on the weather, okay...

**Shiva Lou:** I have no idea what the speed is in terms of the different servers, because it actually really changes depending on events, political events in the country, sometimes.

**Adam Staravia:** Wow... So this is a human thing. Like, some human is doing this. You said the weather, but it's really... It's the winds, but it's the political winds, so to speak.

**Shiva Lou:** Right.

**Adam Staravia:** So if I care about the China market, the internet, and I want to be open to those users there, those developers there, when you think about speed - that's one thing.

**Shiva Lou:** Right.

**Adam Staravia:** I'm sure the winds change, that happens, but aside from making a performant site, what else can I do to be mindful of the speed barrier?

**Shiva Lou:** So the best thing to do is always have a server within China, but it is very difficult, actually. For example, AWS just got its license in China, and to deploy on AWS you need to be a registered company in China, and have all your paperwork ready.

**Adam Staravia:** A small business is hard enough.

**Shiva Lou:** Yes, exactly, and it's very difficult to incorporate something in China.

**Adam Staravia:** So you're not making it any easier.

**Shiva Lou:** Yeah, I'm sorry... \[laughs\]

**Adam Staravia:** Wouldn't it be easier - devil's advocate of me saying this, but wouldn't it be just easier to get rid of the firewall?

**Shiva Lou:** Yeah, well there's a lot of...

**Adam Staravia:** What's the purpose of it? Was it the people of China voting for this thing or desiring it, or was it something else? Maybe this is a whole different subject you don't want to go into, but just share what you can share about what we could do about it. Will it ever go away, I guess, is probably the bigger question, rather than get you into an uncomfortable situation where you have to explain something that's just tough. I'm not trying to put you in a corner and ask you that, I'm just trying to figure out why is getting rid of it not an option.

**Shiva Lou:** People in China can't really vote for it... We can't vote. It started in 2008 mainly because we were using Facebook and Twitter to incite protests, and they sometimes become pretty violent. That was in 2008. Afterwards, it just got expanded and any company - for example Google - who would not cooperate with the government on censoring certain word searches, they would get kicked out of the country, basically. They're not hesitant to even kick out Google.

**Adam Staravia:** Well, you've got your own version of it, right? You said Baidu...?

**Shiva Lou:** Baidu, yes.

**Adam Staravia:** Okay. And then you've got Bing - good job, Microsoft! What other search options do you have?

**Shiva Lou:** There's this company called 360 Search, this company called [Soon](https://www.sogou.com/), and there are a bunch of companies making their own search solutions. My personal experience is that they never really compare to Google, no matter how good they are, maybe because once Google went out of China there wasn't enough competition for people to be forced to...

**Adam Staravia:** To make it better. That's a good example of having a perfect user experience (I'm air quoting); I think Google has a good user experience, but I think that there obviously are some biases where if you compare the results from other engines that you might like those better, but I've always, in a blind taste test so to speak, I've always preferred Google's results, without any styles; not even looking at the page, but just in general, the results I get back seem to be more relevant to me.

\[20:12\] Let's flip it around then, let's talk about China to the outside. Your talk is on how China does Node, and I think what you're talking around is what we're being sharing here - the speed issues, the language barriers, educating developers on how to better think about using certain web services to communicate to China or be inclusive of China... What about the flip side? Do we have any issues reaching China's server, reaching China websites...? How does that work?

**Shiva Lou:** I have noticed that the services and websites and apps that I use that have all the servers in China are a bit slower outside of China than within.

**Adam Staravia:** But accessible though.

**Shiva Lou:** Yeah, accessible.

**Adam Staravia:** Okay. So there's no blocking out, it's just filtering what comes in.

**Shiva Lou:** Yes.

**Adam Staravia:** So I guess, since we're talking here, we're at Node Interactive, this series we're doing here is called The Future Of Node.js, talking about the future of Node... For those out there listening, these are people who are either in the ecosystem already, developers in the Node ecosystem, and they want to learn more about the future. What can you share, more from your talk or more from your ideas on the future of Node and where we're going? One thing I mentioned earlier, and we didn't get to dive much into, was the NPM of China, basically. How does that play out?

**Shiva Lou:** CPM I think actually stands for private, or company NPM. It actually doesn't stand for China, it stands for Company NPM.

**Adam Staravia:** I had that wrong... I just made an assumption.

**Shiva Lou:** I didn't know until a few days ago either, actually. I've just been using it...

**Adam Staravia:** Wow... Okay. So it's a mirror of NPM, right?

**Shiva Lou:** The registry, yes.

**Adam Staravia:** Right. And there's a little bit of latency, a couple of hours...

**Shiva Lou:** I think once a day, or so. So remember the Pad thing?

**Adam Staravia:** Yeah, Left Pad.

**Shiva Lou:** Yeah, Left Pad - it never affected China because when it happened we were like, "Oh, let's just stop mirroring that part. Let's just not sync that part."

**Adam Staravia:** Wow. That's an easy way to avoid it. For those who aren't familiar, give us the deeper side of CPM. It's a mirror of the registry... What's the point of it? Is it because of the firewall?

**Shiva Lou:** Yeah, it's because it's much slower to download...

**Adam Staravia:** From elsewhere.

**Shiva Lou:** From NPM, yeah.

**Adam Staravia:** So who got the permission to synchronize this? Did they work with the government, did they work with somebody to bypass parts of the firewall to sync the registry?

**Shiva Lou:** So the firewall doesn't work in a way that you need permission to do things; you just do it until someone stops you. So NPM right now does not have anything political, basically, so there's no reason to censor it. And it's very important for the developers, so that's a very...

**Adam Staravia:** So basically until it may cross a line that should not be crossed, door are open.

**Shiva Lou:** Right, yes.

**Adam Staravia:** How does that make you feel? Does that make you happy/sad? That's got to make you sad, right?

**Shiva Lou:** Yeah, I am completely against it. I think most people, or most of my developer friends are against it, too. I have met a couple of people who have been working on this project, which I don't call them friends... \[laughs\] I think most people - if you work on this project, you could probably find a better job elsewhere, that's better for humanity...

**Adam Staravia:** I'm just kind of curious, if someone from China -- because you still live there? You live in the U.S. now, right?

**Shiva Lou:** \[24:05\] I'm still living in China for another month or so.

**Adam Staravia:** Okay, gotcha. So would you get in any trouble if someone from China heard you talking like this, or just in general sharing information about how things work?

**Shiva Lou:** I think the extent of what I've been talking about is pretty mild, so I shouldn't get in any trouble for this.

**Adam Staravia:** But it's possible.

**Shiva Lou:** Yes.

**Adam Staravia:** What I'm trying to get at is that the listeners listening to this should be thankful that you're sacrificing potentially, to some degree.

**Shiva Lou:** Yeah.

**Adam Staravia:** I'm not sure what level of sacrifice there is, but there's some concern for you.

**Shiva Lou:** Well, yeah, but I think this is pretty common knowledge already, so that's fine for me to talk about. It's pretty open... Everyone kind of knows about this now.

**Adam Staravia:** Okay. So for those who are right now in China, listening to this podcast - maybe we've got a hundred people; it's a big country, a lot of people there, maybe it's 10,000 people, I don't know... What do they need to know about CPM? What do they need to know about this concern you have of the firewall, this concern of the language barrier? What do the developers inside of China need to know?

**Shiva Lou:** Well, I think it's definitely more beneficial to learn English, because you're far ahead of people who have to wait and read Chinese documentation. I think that's actually the bottleneck for developers in China - not being able to be updated so quickly with English documentation.

**Adam Staravia:** You need to hear you say that; I wouldn't expect you to say that it'd be just easier to learn English, because it seems like it's part of your culture, your heritage, where you're from, to keep and maintain, rather than to give up.

**Shiva Lou:** Can you repeat that?

**Adam Staravia:** It wasn't really a question, I was just empathizing with you that I find it a little sad that the bottleneck is the translation, that the bottleneck is being forced to some degree, learning or speaking English.

**Shiva Lou:** Well, so computer programming is basically in English, so everyone is kind of forced to learn English.

**Adam Staravia:** I guess that's true, I'll take that back then. I'm not empathizing, I'm just kidding. \[laughter\] I'm a fan of Ruby - my roots are in Ruby, huge fan of Yukihiro Matsumoto, or Mate, as we know him, the creator of the Ruby language... Native Japanese speaker - he speaks Japanese as his primary language, but he came on our podcast and spoke English, but only we really asked him to, like "Hey, Mate, we'll speak slower, we'll take our time, we'll edit out the parts that don't work out right, we'll make it work..." We're open to having people like that on the show, obviously, that aren't only English speakers.

I'm not really sure what my question was, I've caught myself rambling. That's really all I have. Did you have anything you wanted to share with the Node world that I may not have asked you?

**Shiva Lou:** No, I think we have covered it, really.

**Adam Staravia:** Okay, I'll stop rambling then. Thank you, I appreciate it.

**Shiva Lou:** Okay.
