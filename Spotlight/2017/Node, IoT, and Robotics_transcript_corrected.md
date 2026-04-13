**Adam Staravia:** \[00:31\] Welcome to our Spotlight series titled The Future Of Node, recorded at Node Interactive 2016, in Austin, Texas. We produced this in partnership with the Linux Foundation, the Node.js Foundation, and it's sponsored by IBM and Strong Loop.

**Break:** \[00:43\] to \[01:05\]

**Adam Staravia:** In this episode I talked with Rachel White, Technical Evangelist at Microsoft, about Node, IoT, robotics... We talked about making robots, inspiring developers to try new things, having fun as a developer, letting go of impostor syndrome, RFID implants and making stuff for fun, outside our day-to-day jobs. Take a listen.

\*\*\*

**Adam Staravia:** So all I have as notes is IoT. That's all I have for notes.

**Rachel White:** Okay, that's fine.

**Adam Staravia:** Let's talk about Node Bots, let's talk about IoT... Are you part of Edge? What do you do at Microsoft?

**Rachel White:** I'm just a technical evangelist at Microsoft. I basically just work with developers and utilize Microsoft technology like Azure with Node deployment via pushing to GitHub; you can make a web app with Node super easily, and we have a whole slew of cognitive services, like facial recognition, emotional analysis, text-to-speech stuff... I've been making interesting and fun web application demos in Node, so that...

**Adam Staravia:** kind of have some of your story then, because you were saying that you don't write...

**Rachel White:** Production code.

**Adam Staravia:** ...production code, but you create demos to get people excited about the production code and what they could do with it. It's a unique position.

**Rachel White:** It's great, I love it. My only drawback is I need to stop making so many things with cats.

**Adam Staravia:** Okay... You're a cat fan, I assume. I saw your phone.

**Rachel White:** Yeah, I love cats, in a totally healthy, cat-lady way, not a "I'm going to be buried underneath lots of boxes and sweaters" way. Some of the web apps that I made though... Yesterday I spoke about a Twitter bot that I made utilizing a Twitter streaming API, Microsoft's Face API, which is facial recognition... It's really cool; it's a REST API, you hit an endpoint with the path to the image that you're going to use - in this case it's selfies... So people will tweet a selfie at this Twitter bot, which is called Magical NO, and I grab the image, I run it through the face API, and it gives me X/Y coordinates of a bunch of face landmarks, and then I run it through GraphicsMagick and do a bunch of overlays for cute noses and cute ears, and it does this whole new composited image that then gets tweeted back at the person.
I get paid to make things like that. I can get people excited to try out-of-the-box things that they might not necessarily be able to integrate into enterprise applications, but facial recognition could totally be...

**Adam Staravia:** Fun stuff!

**Rachel White:** \[03:47\] Yeah. You could totally use it for more applicable things. I would like to think that I am more reaching out to the people that may not have had too much experience with Node, and then they'll see this application -- I always open source everything that I make, and I write the README super documented, not making any assumptions about what the user might know, down to "Go to the website and install Node" and "Install NPM, and do all of these steps", so hopefully they can make their own weird and cool stuff by the end of it.

**Adam Staravia:** That's fascinating, because you get a chance to 1) open source fund interesting projects, but also use a creative side to yourself that -- I don't want to say not important, because it's not production code, but at the same time you have this level of freedom in your code that isn't restricted by business requirements, isn't restricted by revenue-generating things, that you can kind of like whimsically tinker, which to me is like a box of Legos.

**Rachel White:** Yeah, and the fascinating thing is I've only been working with Node for about the past year. After Scoff 2014, I was sitting in a Node Bots panel and I saw all the really awesome stuff that Rick Waldron and Kassandra Perch and Francis Glottal were making, and I was like "I want to do this!" And then it took me a week to blink an LED, because I used a yellow LED and it was too bright in the room, so I didn't even know that it was working.

**Adam Staravia:** What?!

**Rachel White:** And that was my first foray into Node, which I then kind of just pushed it aside because at that point in time I still was a frontend/full-stack JavaScript developers, and I didn't have that much time. I actually just got the Facebook memory on my phone yesterday - a year ago yesterday I finished my first Node project, which was also my first hardware project, and it was an automated cat feeder that I built utilizing Johnny-Five (a Node application) with a webpage, where you go and push a button, and it turns a servo and cat food comes out.

It was kind of exciting, because that one was the longest README I've ever written, and I was so exhausted from finishing it... I published the repo, I tweeted about it, I posted it to Hacker News, I went to sleep, I woke up, and it was all over the internet. Some site in Japan wrote about it...

**Adam Staravia:** I bet! They love cats there.

**Rachel White:** Yes. It went over really well, and so many people came up to me after giving talks about it, saying "I've never done any of these things before, and you really inspired be to try." That's something that I keep on hearing, and it makes me feel so good, because I want people to try new things. It's cool.

**Adam Staravia:** I was reading a book, Essentialism. Have you heard of the book or read it?

**Rachel White:** No.

**Adam Staravia:** I always ask that question, because a lot of people that I ran into have read it, especially in the tech community. One thing they said in there about learning is that you have to make learning fun. If learning is kind of boring, you don't absorb it the right way. It's that childlike -- when we are kids, we learn so much better than... Or probably not so much better than an adult, but kids are sponges, and the reason why they are is that most of what they approach is in a fun way. You probably agree with this, since this is kind of like your core role now - whenever you approach things with a fun attitude, it's so much easier to kind of just get lost in it and achieve flow quicker.

**Rachel White:** Yeah, and another thing too... A term that I learned recently from a good friend of mine who's a self-taught chef - autodidact learning, where you learn by doing, is pretty much the only way that I am good at absorbing any kind of information. If I can't visualize exactly how something is working, then I'm not going to get the concept of it. You could explain theory to me all day, and it's going to fly in one ear, out the other.

\[07:58\] I've been programming for like 15 years; I don't have a CS background, and I'm still really terrible at memorizing syntax, or... I don't know anything about any kind of Wording - I don't know any of that stuff, but I can probably figure anything out. I always tell people that I'm not a good engineer, and then there's always like "Oh, don't say that..." I'm like, "No, it's fine... Furthermore, I'm perfect at problem-solving though", which I would rather be proud of, because I could figure something out; it might just take me a little bit longer... So it's probably good that I'm not writing production code.

**Adam Staravia:** How do you feel when I say this: "Not an impostor"?

**Rachel White:** That was something that I struggled with for a really long time because of the situations that I was in, where when I did have the stress of writing code with testing and deadlines that people needed to use, I felt like I wasn't good enough because I wasn't fast enough. I don't really feel that way anymore now that I'm lucky enough to have the freedom to be able to kind of control what I output into the world, and really the only measure of my success in terms of my job is how many people like it, or how good I am at conveying my message. It's kind of hard to feel like an impostor when all I'm doing now is being myself, and feeling comfortable in it.

**Adam Staravia:** The reason why I ask that is because for The Changelog, our main show at Changelog (which is our overarching brand) we've come to grips with what we feel makes the show good (my co-host, Jerold, and I) is that we face our impostor syndrome so that our listeners don't have to. So over the last several years we've kind of coined certain inner taglines, so to speak, that kind of define us. "Hacker to the heart" is our main one now, because we feel like that's what really defines who we are. We're hackers, but we also get to the heart of the story. And we always felt that anywhere we go, we always feel some level of impostor syndrome.

Earlier, when I was sitting here talking to Thomas and Sam from IBM, I was thinking like "I don't belong here." Not that I'm saying, "Oh, I DO belong here", but I had this level of anxiety in me, thinking "I don't belong here!" And I was just thinking about the idea of people out there that feel like they don't belong... And what I think is cool about what you do is that you do it in a fun way and inviting people, and it's almost like a permission to mess up.

If you're doing it for fun, you can approach it and mess up, and be like "Ha-ha-ha! Whatever..." And the same with the people you're approaching - they don't have to feel like, "Oh man, I have to be an engineer, I have to get this right, I have to have this certain way that defines who I am, or whatever." You can kind of like go that impostor syndrome.

**Rachel White:** Yeah, and I definitely mess up all the time. I don't think I've ever given a conference talk without having some kind of technical difficulties... But you know what? It doesn't phase me anymore. I just talk through it and make jokes. Especially giving hardware demos at conferences - it always goes wrong.

I gave a hardware talk at Node Interactive EU, and I was doing four hardware demos. They all worked, but one of them - I switched to USB cords, and had a lot of serial port issues. I was like, "I don't know what's going on", and I started having a live conversation with someone that was in the front row of the audience - it was Kassandra Perch - and we were live debugging and figuring out the issue; it only derailed like three minutes, and then it was okay.

**Adam Staravia:** Anybody else might have just crumbled under the pressure.

**Rachel White:** Yeah, and I'm like, "Oh, whatever... I have to get through this, otherwise we're going to sit here and stare at each other for 20 minutes." And even yesterday - I'm not giving hardware demos at the moment - I was demoting a new bot, and the internet was kind of spotty. It was still working, and surprisingly, I didn't have any code errors... I forgot how to use PowerPoint!

\[12:03\] So during my presentation, after I switched from the PowerPoint slides over to some live coding demonstrations, I needed to get back to my slides, but we were already halfway through, and I couldn't remember that they key command on Windows is Shift+F5 to get to a specific slide...

**Adam Staravia:** Of course, why would you remember that?

**Rachel White:** Well, I tried Alternate, I tried Control and I tried Function+F5, and it all didn't work, so then I just started clicking on every single slide to get back to the 23rd slide... And I was just like, "So, how's everybody doing? This is great..." And then even the workshop after that, the code that I deployed for people to use had a bug in it, so we had to fix it together in order to get it to work. But it did work eventually, and then everybody was really excited.

I think that mistakes are such a natural part of making something, and I kind of think it's more human to have that happen organically. I know that that stresses out a lot of people, especially when you're putting yourself out there, but I think that if everybody embraced their mistakes, we would be able to feel a lot more comfortable discussing a lot of different technical and even societal things...

**Adam Staravia:** Yeah. I think a lot of people get hung up on the things they feel like they're not good at, and it sort of paralyzes them, and that doesn't do anybody any good, because they get stuck, they never produce what would have been cool, and then the world doesn't grow from it.

**Rachel White:** Yeah. I think that that fear prevents a lot of people from making awesome stuff. I fall victim to that, too...

**Adam Staravia:** We all do.

**Rachel White:** There's a ton of stuff that I still want to make that I've been putting off for like two years, just because I'm afraid of starting it and then having to finish it, like video games...

**Adam Staravia:** Sometimes we don't do what we want to do because we're scared we'll succeed. We're like, "But if that actually worked, I'd have to do it..." And it's like, "Not today... I'll procrastinate."

**Rachel White:** That's exactly how my first conference talk happened. I'm perfect at writing abstracts, apparently, and I submitted the Robokitty abstract, and I was like, "Well, if it gets accepted, I guess I'll build it." And it got accepted, and then I had to build it, and I was like, "Oh, great... I put myself in this situation, and now I have to do it."

**Adam Staravia:** So tell me about Robokitty. What happened there?

**Rachel White:** That was my automated cat feeder.

**Adam Staravia:** I didn't know what the name was.

**Rachel White:** Yeah, it's called Robokitty. I was sitting at a bar with Jean Schopfer, and I was like "I think I want to start talking at conferences", because I spoke at JS Fest in 2014, but it wasn't a technical talk; it was a part of DHTML Cone 2000, which was satirical talks, and instead of giving a satirical talk, I spoke about my life as a kid and a teen, creating problems for other people on the internet because I was a total script kiddie on AOL, and have created a lot of problems. And it was really fun, and I was like, "I think I wanna talk at conferences and do technical stuff. It would be really fun."

She encouraged me to just apply, and I did. And now, here we are. I get to torture everyone with all the fun things I make.

**Adam Staravia:** How many talks later are we?

**Rachel White:** Oh my gosh... Well, over ten, definitely. This year I was invited to speak at Amazon, I spoke at Cascadia Fest, Dinosaurs... I was in Europe for two weeks in Stockholm and Amsterdam, and I spoke here... I've lost count. It's been a lot.

**Adam Staravia:** Too many to count.

**Rachel White:** Yeah.

**Adam Staravia:** So you enjoy that, I assume.

**Rachel White:** I do, I enjoy doing it. The majority of that was before I took the role of technical evangelist, so it was all in my spare time.

**Adam Staravia:** \[16:06\] Yeah, and now it's what you do.

**Rachel White:** I thought I was tired when I was doing it outside of work, and now that it's my job, I'm even more tired.

**Adam Staravia:** So let's talk about hardware for a bit...

**Rachel White:** Sure.

**Adam Staravia:** ...which blends into the internet of things, and this new world we're in. I was actually talking to somebody several months ago who was a mechanical engineer. For whatever reason, his job was drying up; he had perfect smarts as an engineer, and I was encouraging him like "Hey, you've got the kind of mindset to get into software development, and you love hardware; you already know about all these things. Have you considered learning JavaScript and getting into these things?" For people like that, since you're an evangelist, it seems like your focus is on -- is it on bringing new people in or is it nurturing those who are already there?

**Rachel White:** It's both.

**Adam Staravia:** It's a balance of both?

**Rachel White:** It's definitely both. An interesting thing... A colleague of mine in New York, who's also a technical evangelist at Microsoft, who was a friend of mine before either of us worked at Microsoft, he comes from that electrical engineering/mechanical engineering -- I'm not sure which one it is... He does a ton of hardware stuff, and he's so smart...

**Adam Staravia:** That's what he was, from electrical engineering, but he has a mechanical engineering degree.

**Rachel White:** So his name is Andy Reimann, and he makes custom hardware for the NEW. He made custom mappers for additional memory, so you can do more stuff with a Nintendo, and now he started learning JavaScript and Node, and made this amazing thing called NE Spectre, with another guy, named Zach Johnson. What it is it's reading the memory from the Nintendo real-time, using Node.js and Socket.io, and it runs in the browser, so you can connect to it on your phone while people are playing games. There are things that you can modify, but every second you wait, you get another point...

For example, if somebody's playing Contra, you wait, and they get 25 points, and you hit in the browser "change random gun" and one of the players get a random gun while they're playing their own. That's something I love, especially people that don't come from programming backgrounds... They have a completely different way of thinking about stuff, and they have different situations that they can apply to things.

**Adam Staravia:** That's what I was trying to tell him, like... "You really should consider this, because..."

**Rachel White:** Yeah, it's really awesome.

**Adam Staravia:** You have a different approach than, I think -- well, on the Changelog, one of the things we ask most guests on that show is their backstory, and more often than not we ask them "What got you into programming? When did you fall in love with it? Where were you at in life?" and more often than not it's gaming.

It's a T3i, the Texas Instruments T3i I believe that's what it was called, but I didn't know. Jerold did, Mitchell Hashimoto did, and several guests who came on the show have started out -- it wasn't Mitchell, it was somebody else; I'm mixing up names. Either way... Gaming was this epicentre, a breeding ground of software developers. These are people who have gone on to do some really cool stuff.

Putting that back to you, do you find that the fun mechanism in what you do is what catches people? What is it that you feel attracts people to software development that may not have otherwise done so, or dig deeper where they may not have thought so?

**Rachel White:** I think that the fact that I don't speak about things in overly technical terminology, and I really try...

**Adam Staravia:** You seem very down to earth...

**Rachel White:** \[19:52\] Yeah, I really try and explain stuff in a way that makes sense. Like, I'm talking about Markov chains, I'm talking about stochastic stuff -- I had to look it up; I was like, "I don't know what this means." I know what Markov chains are and how they work - kind of - so I'm explaining it, and I'm giving the technical definition, and I'm like, "Yeah... Let's just look at a visual aid of how this works." Or really just breaking things down in a simple way, so that that is approachable.
I also think the fact that I'm presenting things in an interesting setting is interesting to some people, though at conferences you can definitely tell... You get a lot of different people. You get the people that are sent by their company, that are already developing enterprise applications; they could not care less what I'm talking about, but I'm not there trying to speak to them; they already are involved in the community and utilizing it. I'm there for the people that are like, "What if I could do that?" and I just want people to feel like they could.

**Adam Staravia:** We got derailed at the mention of my buddy trying to learn, and we kind of got back into this other groove, but I want to go deeper in the hardware, and that kind of fun stuff. So you've done some things with Node Bots, I believe, right?

**Rachel White:** Yeah, I'm involved in a lot of Node Bot stuff. I did the cat feeder... Another talk that I have is just about simple things that you can do with hardware that are impressive. People love lights, so there is one where you're controlling an LED strip that you have a flex sensor, and it makes the lights up incrementally. It's something simple, but it's super impressive.
There's the Node Bots NYC group where people go, and they meet up, and the format is like one person gets up and presents something really cool that they've made. Then there's like a little hack night, or something like that. But most of the stuff that I've done is just freely weird, and I just remembered something that you're probably going to enjoy to hear about... I actually have an RFID chip implanted in my hand.

**Adam Staravia:** What?

**Rachel White:** Yeah, so I have a little RFID chip right here...

**Adam Staravia:** Can you feel it?

**Rachel White:** Yeah, do you want to touch it? It's right there.

**Adam Staravia:** Oh, I feel it. That's crazy.

**Rachel White:** \[laughs\] So I did a project where -- I don't know if you've played Fallout or if you remember those old terminals... The green CLI that you would get - I made a CSS version of it in a browser, that you scan an RFID tag, and if it's not me, like if it's any other RFID tag, it says "Access denied" and it flashes on the screen, and there's like a glow on the text. But then if I scan my hand, you get a bunch of 1990s hackers scrolling text with an ASCII skull that says "Access granted", and that project is the most ridiculous thing to show people, because obviously, they can't replicate it unless they go get an -- well, they could, but not with one in their body.
But it's a hardware example of something that's super weird, but all it is a Node.js application with Socket.io.

**Adam Staravia:** Dedicated.

**Rachel White:** ...and some fancy CSS. That's probably the weirdest thing that I've done.

**Adam Staravia:** Okay, so how did you get it into your body.

**Rachel White:** I went to a professional piercer in Brooklyn, and there's a company called Dangerous Things that sells them. It's a tiny RFID chip that's encased in surgical grade medical glass, and they have a syringe that has a really wide opening, and all they do is inject it into the web in your hand and pull the plunger, and that's it. It's in there.

**Adam Staravia:** Just like the movies. I've seen that in movies, and they're always like "UURRGGHHH!" Wasn't it in Bourne Identity? I believe he had something in, and then he finally dug it out, or something.

**Rachel White:** I didn't see that one. I mean, it's exactly the same thing as the one that they put in pets. They'll put it in a shoulder blade for a cat or a dog and then scan it if they get lost... I have one in my body. If you have... Is that an iPhone or an Android?

**Adam Staravia:** iPhone.

**Rachel White:** \[24:04\] Oh, iPhone closes off RFID stuff... But if somebody with an Android phone scans my hand, the text that pops up is "Follow me on Twitter" with my Twitter name.

**Adam Staravia:** What?!

**Rachel White:** Yeah.

**Adam Staravia:** Oh, my...

**Rachel White:** It's readable and writeable.

**Adam Staravia:** Can you change it?

**Rachel White:** Yeah, I can totally change it.

**Adam Staravia:** How?

**Rachel White:** It's not powered... It has a wire antenna that's wrapped around the chip, and the power comes from the devices that you're doing the scanning with. When it's close, then your field communication stuff allows you to -- it's tiny; I don't remember the size of text on it. I can pretty much just store a URL to a website or some text, and stuff like that. No sensitive information, or anything.

**Adam Staravia:** Okay... Very, very interesting. So this series we're doing for the conference is about the future - the future of Node. Someone with your experience, 15 years of experience developing software - the coolest job ever, in my opinion; hardware in your body - what role does Node play in the future of hardware, IoT...? Where are things going?

**Rachel White:** Oh my gosh... Hopefully they're still going in a weird direction, for me at least; otherwise I'm going to be out of a job. I hope that, honestly, there's more of a focus on making secure systems, especially the state of our world... I think that a lot of information needs to be more private. The big problem with hardware and IoT devices now that a lot of manufacturers are making are they just don't care; they're not assuming that their information's going to be vulnerable on their Wi-Fi connected crock pot. But the botnet thing that just happened recently - it's a careless process that people are taking into account, and one thing that I've seen a lot in the Node community and the hardware community - people are trying to think of ways to utilize these skills that we have using the technology that we have to help make things better for people, whether that is making a Twitter bot that automates your streaming timeline to make sure that you're not being harassed, and it will automatically report that to Twitter, or it will block the person that's harassing you... Or Node-powered hardware that helps people...

I hope that the future just encourages people to keep on being innovative and finding ways to utilize technology in ways that are more important than necessarily enterprise-based.

**Adam Staravia:** Hopefully this background noise isn't distracting to you, because this is the loudest it's been since I've been sitting here. Most people respect the fact that we're sitting here recording, but clearly not the people that are passing by.

**Rachel White:** Yeah.

**Adam Staravia:** Anything else on your mind? I know that you're an interesting person with fun ideas...

**Rachel White:** I just really hope that people keep on making stuff outside their day-to-day job that they're interested in... You know, it's easy to say, "Yeah, I only want to program if it's going to make me money", and I understand that's super important, but if you have the time and the capabilities, make cool stuff and weird stuff that people find interesting, that will get new programmers interested in trying something new, that will inspire a student that maybe just is writing Python or Java stuff...

\[27:52\] I also help out at a lot of hackathons, and some of the students are trying Node applications for the first time, and they're like, "I can't believe how easy this is." It's a perfect feeling to be able to expose people to something that they wouldn't have picked up and tried on their own.

**Adam Staravia:** I guess maybe one closing thought I might have is what - on the hardware side, or whatever side is more interesting to you - what's happening in Node right now that you're most excited about?

**Rachel White:** The Vessel is really, really great. I haven't gotten to play with it that much, but it has Node on it, so you don't have to run things... If I'm working with the Arduino and I want to run Johnny-Five, I have to just use an Arduino as a middle point, I guess. The code runs on my machine, instead of running on the microcontroller, but Vessel makes it even easier for people to run Node on the microcontroller and not having to be constantly tied to your computer.

I think that we're going to see a lot more community support for people that are building more Node-based hardware, now that they have the means to do so.

**Adam Staravia:** Yeah, especially with the VM-neutrality thing, it makes it a lot easier to open up the VM market, at least.

**Rachel White:** Yeah. Also, the Johnny-Five that came out - it also has a kit that is going to be able to have people make so much more Node-based hardware, and I'm really excited to see what people are going to make.

**Adam Staravia:** When you say Tesla, do you mean the car?

**Rachel White:** Oh, Vessel.

**Adam Staravia:** Vessel?

**Rachel White:** Yeah.

**Adam Staravia:** I thought you said Tesla, and I'm thinking like, "Dang! You must make some good money that you own a Tesla." I'm just kidding.

**Rachel White:** No, I don't have a car. \[laughs\] The Vessel.

**Adam Staravia:** What is a Vessel.

**Rachel White:** The Vessel is a microcontroller that has -- let me look... I can't remember. I'll pull it up. This is what I said, and I can't remember anything ever, unless it's weird facts about things...

**Adam Staravia:** No worries.

**Rachel White:** So, "The Vessel 2 is a robust IoT and robotics development platform that leverages all the libraries of Node.js to create useful devices in minutes." It has a ton of stuff already on it, which is great, too. Before, you would need to get just a regular Arduino that doesn't have Wi-Fi, and you have to add a Wi-Fi thing on it, or you have to use a particle photon that already is WI-Fi-enabled, and you'd have to get other things to be able to make stuff...

I'm perfect at speaking vaguely, but it has a ton of stuff already built on it - it has two USB ports, Wi-Fi, it has an Ethernet core if you need it, it's superfast... I've only done a little bit of work with it, but I know a lot of the people that are involved in the development community for it are working super hard... Plus, it's open source. If somebody wants to make some modules for it, they can just go ahead and do it, and submit it, and try and get it added in.

I think that it's only going to help especially the Johnny-Five community grow even more. Because before, we would have to rely on Chris Williams' voodoo spark firmware - which was great, and that's the first thing that I tried hardware on. That's what I had to install to get hardware to work with Node, but now there's such less of a boundary for people to just get up and running, instead of having to install some stuff in order to get where they need it to be.

**Adam Staravia:** \[31:16\] Yeah. Any closing thoughts? This is, like I said, The Future Of Node Series - we're trying our best to inform and encourage the community to try new things, to get involved.

**Rachel White:** Yeah. If you're thinking of making something but thing that people might not like it, do it anyway, because you're never going to know unless you try. I heard a quote from David Lynch once that was in regard to his films - when he has a vision, all the creative process that he has that goes into it is super important to him, and it has a lot of meaning while he's making something. But once you're done, and you release that into the world, your vision doesn't really matter anymore. That sounds unencouraging, but just think of when you put yourself out there the way that people will view the art that you're trying to make. Because I think that code is art - you're still making something from nothing...

**Adam Staravia:** Totally...

**Rachel White:** ... and I think that that's something that a lot of people don't think about, and I just want them to try.

**Adam Staravia:** It's a good message.

**Rachel White:** Yeah.

**Adam Staravia:** Thank you.

**Rachel White:** Thanks.

**Adam Staravia:** It was nice talking to you.

**Rachel White:** Yay! \[laughs\]
