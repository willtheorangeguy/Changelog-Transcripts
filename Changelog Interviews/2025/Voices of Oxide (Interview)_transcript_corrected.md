**Adam Staravia:** So Cliff, what is it you do here, man?

**Cliff Baffle:** I'm responsible for parts of the really low-level firmware on the computer. So everything from the machine turning on, up through fans and power management and all of that. Basically, all the stuff that happens before the thing our customers think of as the computer turns on.

**Adam Staravia:** Right.

**Cliff Baffle:** That's all -- well, me and my colleagues now, but originally it was me.

**Adam Staravia:** Is that like BIOS stuff, or is it --

**Cliff Baffle:** Well, before then, actually.

**Adam Staravia:** Before BIOS.

**Cliff Baffle:** From --

**Jerold Santo:** What's before BIOS?

**Cliff Baffle:** What's, indeed?

**Adam Staravia:** Okay...

**Cliff Baffle:** So these big AMD and Intel processors, and even the big ARM nowadays that you see in something like an iPad - there's actually a lot of work that has to go on to allow them to turn on. They need a bunch of different -- like, voltage supply is stable, they need a bunch of clock signals set up and devices set up, and you've got to get their flash ready for them before they wake up, so they can get their code out of it... And so there's almost always one or more small processors in the machine that are responsible for doing all of that dirty work, that nobody ever thinks about, because it happens at the moment between when you hit the power button and when the screen wakes up. So that's our job.

**Adam Staravia:** Pretty fast. Like 20 seconds? 15 seconds?

**Cliff Baffle:** Ours is milliseconds.

**Adam Staravia:** To me as a user, it's like 15 seconds, you know?

**Cliff Baffle:** Sure.

**Adam Staravia:** They mentioned PCBs, so you're building your own boards...

**Cliff Baffle:** Yeah.

**Adam Staravia:** So you're going first principles on a lot of this stuff.

**Cliff Baffle:** Yeah, absolutely.

**Adam Staravia:** And you're a first principles kind of guy?

**Cliff Baffle:** Yeah.

**Adam Staravia:** Do you like that?

**Cliff Baffle:** I think I actually designed the first board we made...

**Adam Staravia:** No way.

**Cliff Baffle:** Back before we hired actually qualified electrical engineers.

**Adam Staravia:** Okay... It was an MVP, or was it a --

**Cliff Baffle:** Yeah, it was just for testing out some of our circuits we proposed for the bigger, expensive board... Because it's nice to make cheap things that if they're wrong, you can throw them away.

**Adam Staravia:** Right.

**Cliff Baffle:** You know.

**Jerold Santo:** And so Oxide has this writing culture... I assume that you were kind of attracted to that, or kind of helped formulate it...

**Cliff Baffle:** No, it was pretty well established when I got here.

**Jerold Santo:** Okay.

**Cliff Baffle:** But the fact that -- we make people write a bunch of stuff during the application process; the materials, and like that whole packet of "Why do you want to work here? What's an interesting problem?" Because it really saves time in the interviews. But for a lot of people, that's daunting. For me, it was like "Oh, you want me to write a bunch of stuff? I like writing. I can do writing."

**Jerold Santo:** Nice.

**Cliff Baffle:** Yeah.

**Adam Staravia:** Was that a process you liked? This request for discussion, high? RFD's... Had you done it before? Is this something that was --

**Cliff Baffle:** Previous companies I'd worked for had a process around design docs that kind of was similar, but not exactly. We are way more writing-focused here, and in particular, most of the docs are living. So as we learn what we're doing, we go back and fix the docs that we wrote when we were done, to try to better reflect... So that way they can also serve as documentation for the next person that comes through. So it's not perfect, but I honestly couldn't really point to what I would change. Like, it's working pretty well, as long as you've got people that are invested in the process, and that are comfortable expressing themselves in writing.

**Adam Staravia:** Would you call it document-driven? Do you think you start with docs or an idea, or not so much a spec, but something fleshed out first before you do --

**Cliff Baffle:** I actually feel like one of the ways people sometimes have a hard time starting here is if they treat it too much like that. So it's not like you need to write a thousand paragraphs in English before you can write a line of code. A lot of things here start as a prototype. But then if you want to build consensus, if you want to get other people involved, if you want to try to get feedback, that's when you need to write everything down and share it.

**Adam Staravia:** Okay.

**Jerold Santo:** So when you were writing on your blog, this was about Rust, right?

**Cliff Baffle:** Lately, yeah.

**Jerold Santo:** But back then, when they founded it...

**Cliff Baffle:** Since like 2015. It's been mostly Rust.

**Jerold Santo:** Okay. So how'd you find Rust, and why'd you like it?

**Cliff Baffle:** So I was working in firmware at Google, doing high-altitude balloon tracking and communication stuff, and we were using C. And I've been using C since I was a kid, because my dad just flew up in it. But it's really hard to produce correct software that doesn't contain bugs, particularly on a team with different experience levels, working in C. And I was bringing people in at intern level, up through experienced developers, and trying to get everybody working together and productive as a team... And the problems with a lot of work in process, you can manage it. Car companies do this all the time, but it takes them a tremendous amount of overhead, and I just wanted some way out of that. So there were a couple of different alternative languages I was watching at the time, and Rust was the one that matured at about the right time, and got enough things right to be worth spending time on.

**Adam Staravia:** \[08:16\] This is 2019 you said?

**Cliff Baffle:** This would have been 2015, originally.

**Adam Staravia:** 2015, okay.

**Jerold Santo:** Way back. So you said "recently", but that was a decade ago...

**Cliff Baffle:** Yeah. I'm old.

**Jerold Santo:** Okay. I just wanted to point that out. \[laughs\] Alright, so you're writing Rust blogs, so you're writing Rust... Here comes Oxide, you start working on Oxide, you're writing more Rust...

**Cliff Baffle:** Yeah. I think Oxide was an interesting opportunity, because I don't super-care about our product.

**Adam Staravia:** Ooh. Tell me more.

**Jerold Santo:** \[laughs\]

**Cliff Baffle:** Like, I care that it's good. I want to make a good product.

**Adam Staravia:** Sure.

**Cliff Baffle:** But I'm never going to buy one of these. You're probably not ever going to buy one of these.

**Adam Staravia:** I can aspire to buy one...

**Cliff Baffle:** Yeah, you can aspire to buy one.

**Jerold Santo:** We'll pitch a home lab version. We can set that aside for now.

**Cliff Baffle:** Yeah, now we're talking... But it's like a fancy McLaren sports car, or like a Ferrari. I'm probably never going to buy one.

**Jerold Santo:** Right.

**Cliff Baffle:** So this product isn't for me. So I had to find other ways to really get motivated around it, and the main things are this is a team that really wants to try to do things right from the ground up, which I can get behind. That sounds like a hell of a challenge. The team is amazing. My co-workers are amazing. You should talk to more of them.

**Adam Staravia:** We will.

**Cliff Baffle:** Good. So you have to look for all the other ways to do this. And sort of the "How do you build an engineering org from a team that fits around a small restaurant table, to this size, and be able to bring in people that don't have relevant experience, and be able to bring in people that maybe had a career change, but are enthusiastic... And building a framework in the software, but also in the processes and the documentation to support expanding the team like that" - that's the thing I got really passionate about.

**Adam Staravia:** In the firmware world, is it written in Rust, or is it written in C?

**Cliff Baffle:** Our stuff's all Rust.

**Adam Staravia:** All Rust. So there's no -- there's one thing in C, right? Wasn't it like some operating system you had that's not Hubris, that still is C?

**Cliff Baffle:** Yeah. Helios is our sort of version of the Illumes operating system, which is descended from Suns Polaris. That's mostly C. It's also older, pretty well-tested C. It's not new, potentially buggy C, so we think it's a lower risk.

**Adam Staravia:** Does it change much?

**Cliff Baffle:** It doesn't change that much, although we've obviously had to extend it a bunch. But we've been doing a lot of the extending and changing in Rust. But other than that, all the stuff on top of that, all the stuff below that is all Rust.

**Adam Staravia:** That's a good thing.

**Cliff Baffle:** Yeah, we think it's good.

**Adam Staravia:** I was talking to somebody that said if they had to not write Rust here... Like let's say Go, for example.

**Cliff Baffle:** Alright...

**Adam Staravia:** They were like "Nah, nah... Can't do that." How do you feel about that?

**Cliff Baffle:** I don't love to Go specifically, but there are other languages that --

**Adam Staravia:** Nothing goes bad, but like compared to Rust for some of the things you solve...

**Cliff Baffle:** Not for what I'm doing.

**Adam Staravia:** ... Go's not in the picture there.

**Cliff Baffle:** No, it's not. I mean, there really aren't a lot of options on the systems I work on, which are like the 50 cent microcontroller that's inside your credit card. There's just not a lot of resources.

**Adam Staravia:** I never thought about that. A computer in my pocket. What makes Rust uniquely --

**Cliff Baffle:** There are probably a bunch of computers in your pocket right now, actually.

**Adam Staravia:** At least four. What makes Rust uniquely positioned for firmware?

**Cliff Baffle:** So Rust --

**Adam Staravia:** Or your lower-level things.

**Cliff Baffle:** The thing that Rust took from C and the C family is like - the C family gives you really fine-grained control over what the computer's resources are being used for at any given time. So you have tight control over how much memory is being used. You have tight control over whether memory is used at all, or if you try to solve a problem through some other way.

**Adam Staravia:** Or even size.

**Cliff Baffle:** Or size. Size of code, size of flash required...

**Adam Staravia:** Strings, numbers, bigger, smaller... Yeah.

**Cliff Baffle:** \[11:51\] ... Rust replicates that control pretty well. Languages like Go are less focused on that, and don't come out of the box with as much help in that area.

**Adam Staravia:** Do you mess with Go at all?

**Cliff Baffle:** I have a little bit, yeah.

**Adam Staravia:** How do you feel when you do that?

**Cliff Baffle:** It's okay. I mostly just kind of feel like a foreigner. Like, it's not really my native territory. I could get more comfortable with it if I needed to.

**Adam Staravia:** And what are you doing with Go when you do play with it?

**Cliff Baffle:** I do some like -- periodically I'll do like... They have like the Advent of Code exercises, or like programming exercises that people put out annually... And I try doing them in other languages, just to kind of keep my brain stretchy.

**Adam Staravia:** Yeah.

**Cliff Baffle:** So I've done stuff like that, but I've never used it in anger. Never for anything real.

**Jerold Santo:** Tell us about Hubris.

**Cliff Baffle:** Yeah, so... \[laughs\] So I tried really hard not to write Hubris. When I got here, they were -- there's this other operating system called Toque. It's also in Rust...

**Jerold Santo:** Okay...

**Cliff Baffle:** It targets the same sort of very low-level, deeply embedded --

**Adam Staravia:** How do you spell that, Toque?

**Cliff Baffle:** T-O-C-K.

**Adam Staravia:** Okay.

**Cliff Baffle:** Like you'd expect.

**Jerold Santo:** Like Ticktock.

**Cliff Baffle:** Yeah. But not like TikTok --

**Jerold Santo:** Not the platform. The way clocks work.

**Cliff Baffle:** Yeah. The original Ticktock.

**Jerold Santo:** Yeah.

**Cliff Baffle:** They were trying to use Ticktock, or --

**Jerold Santo:** Sorry...

**Cliff Baffle:** You fried my brain. So they were trying to use Toque when I got here. And I had some previous experience with Toque,

I know the people that wrote it... So I got in line and tried really hard to make it work for our application, but we just kept hitting areas where their design intent and the things we needed didn't really overlap. Like, Toque is mostly at the time being written with educational use cases in mind, so they wanted kids to be able -- kids... University students who are adults...

**Jerold Santo:** Okay...

**Cliff Baffle:** I'm old. To be able to dynamically reload programs on it as they're working, and nice use case stuff like that... But we really don't want that for security reasons. We want -- any code that runs on this better be what we shipped, when we shipped it. So we put a bunch of work into trying to work around that, and then finally in May 2020 I think I wrote an RFD that was like "Guys, I think we're going to have to do our own thing. Here's a rough sketch of how it might look like", and there were enough people here that had been involved in operating systems work before, that they all kind of... We pressed our heads together, and they said, "Okay, this might work. Like, take a week, and see how much we can prototype." And we got a thing working, and then it seemed compelling enough that now it's... There's... What - 64 to 70 computers running it inside every rack. All the little service processors you don't think about.

**Jerold Santo:** They're all running that.

**Cliff Baffle:** They're all running Hubris.

**Jerold Santo:** So how big or small is Hubris in terms of like line count, or whatever?

**Cliff Baffle:** So the core kernel is like a thousand lines of code...

**Jerold Santo:** That's not very much.

**Cliff Baffle:** ...but there's a bunch of other stuff you want to make it useful. But it runs right now on everything from like sub-50 cent microcontrollers that you wouldn't even spot on a printed circuit board, because they're just a tiny fleck of silicon, up through the big service processor that we use to run the Oxide rack, which is like a... It's basically a computer you would have been really excited to own in 1999 or 2000, but now it's $3, and inside another chip.

**Jerold Santo:** And does that job.

**Cliff Baffle:** Yeah.

**Adam Staravia:** Are there multiple instances of Hubris on a given full rack system?

**Cliff Baffle:** Yeah, so every slide has at least two. There's the service processor that is responsible for basically caring and feeding of the big AMD chip. Then there's a root of trust that handles security and crypto. That's a separate copy. And then there's... So there's those two on every compute sled, and there's two in every switch, there's two in every power supply... And that's everything in the rack. But then a bunch of our manufacturing tools are also running Hubris. So all the little boards we plug into a thing to program it, or to interpose in an interface for testing... It'll be like, you know, I need to remove this fan and simulate the fan controller... All of our tools for that are all Hubris-based.

**Adam Staravia:** Why so many copies? Is that hard to manage? It's like...

**Cliff Baffle:** Yes and no.

**Adam Staravia:** ...multiple updates, different versions potentially even...

**Cliff Baffle:** That's true. It has pluses and minuses. So the SP versus root of trust split, which is the main source of the many, many copies... There has to be at least one of these on each board...

**Jerold Santo:** Security...

**Cliff Baffle:** ...because the board's got to be able to power itself on. Because it might be the first one powering on and responsible for driving all the other ones.

**Adam Staravia:** Yeah, it's a specialized case. That makes sense to be a copy, but...

**Cliff Baffle:** So one makes sense. Why two? And the honest reason why two is we can buy one chip with the features we need to do the service processor. We can buy one chip with the crypto security features we need to do the root of trust. We can't get them both in one chip right now. And we can't afford to make our own chips.

**Adam Staravia:** \[16:10\] Okay. So when you can--

**Cliff Baffle:** We might merge those. Or we might not. There are advantages to having a \[unintelligible 00:16:14.11\]

**Adam Staravia:** Are you alluding to making chips in the future?

**Cliff Baffle:** I mean, we'll probably have to.

**Adam Staravia:** Yeah. Would it be a collab with like AMD, or an existing...

**Cliff Baffle:** AMD returns our phone calls now. It's very exciting.

**Adam Staravia:** Nice.

**Jerold Santo:** Is that new?

**Cliff Baffle:** Yeah, it's pretty new.

**Adam Staravia:** Like, "Hey, Oxide, we'll take that phone call." That's cool.

**Cliff Baffle:** Yeah, it's nice. Probably not. So we have some FPGAs on the newest generation server board, which are basically...

**Adam Staravia:** What's FPGA mean?

**Cliff Baffle:** Yeah, so Field Programmable Gate Array is the full nerd expansion. But the purpose of the chip is it's basically a bunch of... It's a Lego set for integrated circuits. You've got a bunch of generic logic circuits that you can then program to act like another chip... And it's slower and more expensive than the other chip would be, but if you can't afford the million-plus dollars to get started making your own chip, this is like a way to fake it, essentially. We have one of those on the next generation server kind of playing around with some things we would do if we made our own chip.

**Adam Staravia:** And Hubris is open source...

**Cliff Baffle:** Yeah.

**Adam Staravia:** Does anybody else use Hubris?

**Cliff Baffle:** I've heard from about five other companies that are using it in production.

**Adam Staravia:** Really?

**Cliff Baffle:** Yup. And I can't remember which one of them lets me say that publicly. Also, I can't remember them anyway right now... But I could check my notes.

**Adam Staravia:** Sure.

**Cliff Baffle:** Volvo is really interested, but we don't have the certifications that they would need as a car company... But I've been talking to somebody about what that would take.

**Adam Staravia:** They can contribute though, right? It's open source.

**Cliff Baffle:** They could. The thing they would need to contribute, unfortunately, is a bunch of money for consultants to go through the certification process... Which they're not excited about. So that's fine.

**Adam Staravia:** Well, they probably have -- maybe they have more money than you all now? \[unintelligible 00:17:56.03\]

**Cliff Baffle:** I hope Volvo has more money than we do. I hope so.

**Jerold Santo:** I bet they do.

**Adam Staravia:** I have no idea.

**Cliff Baffle:** It's Volvo.

**Adam Staravia:** Yeah, but car companies - they burn money. Don't they burn money?

**Cliff Baffle:** Yeah... There's like three other startups I've heard from that are using it in products. So that's pretty cool. I'd like to get more people using it, but there's some work we need to do to make it more friendly to people that aren't Oxide.

**Adam Staravia:** Right.

**Cliff Baffle:** Because right now, if there's a trade-off we have to make, and one thing would make us ship faster, and the other thing would make it more general for other customers, we almost always have to pick the "We ship faster" option.

**Adam Staravia:** Right.

**Jerold Santo:** One of the fun things about being here in the building with everybody is every once in a while a fan just goes crazy. This is not a person who enjoys -- like, a literal fan just starts... Like, what's going on when that happens?

**Cliff Baffle:** That's a great question. So one of two things is going on.

**Jerold Santo:** Okay.

**Cliff Baffle:** The good thing is somebody just ran something on that machine that's boosted all the CPUs. It's like when your laptop starts trying to take off.

**Jerold Santo:** Sure.

**Cliff Baffle:** So something made the CPUs go really fast, everything ramped up, the machine got hot, fan turns on, cools the machine back down. That's sort of the working as intended. What's probably happening here is that something's crashing.

**Jerold Santo:** Something's going wrong.

**Cliff Baffle:** We have a chip on the board that's a hardware watchdog that if it doesn't receive regular instructions on what to do with the fans, it assumes the worst, and it ramps the fans up to make sure we don't overheat.

**Jerold Santo:** To avoid... Okay.

**Cliff Baffle:** This means that if you're doing a firmware update on the service processor, the Hubris-based service processor that's responsible for sending those messages, and it's gone for more than watchdog, however the setting is seconds, then the chip kicks up, ramps the fans up, and then it wakes up and finishes doing its update, and then the fans go back down. So this is why -- I don't know if you saw earlier, but whenever those fans go up, I'm like...

**Jerold Santo:** You're like the watchdog for the watchdog --

**Cliff Baffle:** I get yelled at in chat, but one of the computers is crashing --

**Jerold Santo:** Because you're one of the people that works out of the office generally...

**Cliff Baffle:** Yeah. And I might have written the code that's messing up, so...

**Jerold Santo:** So you'd better get out of your seat and go do something?

**Cliff Baffle:** So frequently I'm like "It's not me. It's not me. This one's not me."

**Jerold Santo:** So as being somebody who's regularly in the office, but most folks aren't, what does Ox Con do for you in terms of your camaraderie with your colleagues, or the excitement level? How do you feel about it?

**Cliff Baffle:** I get to find out how tall everybody is.

**Jerold Santo:** \[laughs\]

**Cliff Baffle:** \[20:13\] You can't tell that on the computer.

**Jerold Santo:** That's true.

**Cliff Baffle:** Like Aaron... Aaron's like damn near seven feet tall, but he looks normal on the computer. So that's been interesting. Other than that, gosh... I don't think the company would work without this, honestly. I mean, how would you even -- it doesn't even feel like you're at a real company. It's like you're watching a TV show of a company.

**Jerold Santo:** Good point.

**Adam Staravia:** Like The Office.

**Cliff Baffle:** Like The Office, or Silicon Valley.

**Adam Staravia:** Oh, gosh.

**Jerold Santo:** Ding!

**Adam Staravia:** Are you a fan?

**Cliff Baffle:** I worked there, so I couldn't really make it through the show... Like, my boss was personally a parody on the show.

**Jerold Santo:** "I worked there..."

**Cliff Baffle:** And he loved it.

**Jerold Santo:** Did he?

**Cliff Baffle:** Yeah. So Astro Teller at Google X was the inspiration for the Hold X guy in the show... And he thought it was hilarious. He had a showing of the episode where --

**Adam Staravia:** With the monkey guy. The guy that --

**Cliff Baffle:** Yeah.

**Adam Staravia:** Okay. Gosh...

**Cliff Baffle:** So... He did have a monkey. The real guy.

**Adam Staravia:** Oh, man... That was good.

**Cliff Baffle:** But yeah, so I was watching the show a little bit, and I'm like "Why are you making me watch this? This is my day job. I'm going to watch Game of Thrones, or something."

**Adam Staravia:** Yeah, I can understand that. So you've never gotten past season one, or even one episode.

**Cliff Baffle:** No, I made it like three episodes in.

**Adam Staravia:** How about now? You feel better about it since you're free of that world?

**Cliff Baffle:** I'm good.

**Adam Staravia:** You're in a different world now?

**Cliff Baffle:** I'm good.

**Adam Staravia:** Sadness...

**Jerold Santo:** He lived it.

**Cliff Baffle:** Yeah, I'm alright.

**Adam Staravia:** I was listening to Brian tell one of his stories, and I was like "Oh my gosh, that was literally in the show." Something he described from the stage today, regarding money and funding... And I was like "That was literally copied from it." I mean, it's real life, but it's there. And so I can understand that.

**Cliff Baffle:** Yeah.

**Adam Staravia:** For me, it's entertainment because I haven't worked for Google, and I haven't done your life... For you, I can imagine how it's PTSD.

**Cliff Baffle:** Yeah. I also don't watch a lot of TV, so I'm kind of picky about what I spend my time on. But... Hopefully we don't do anything to get a show made about us.

**Adam Staravia:** Or you do, and it's good.

**Cliff Baffle:** That could happen. That could happen.

**Jerold Santo:** Like Severance.

**Cliff Baffle:** I just started watching that... That's a hell of a show.

**Jerold Santo:** That's worth your time.

**Adam Staravia:** One thing I've been thinking about is churn. Is there any churn here at all?

**Cliff Baffle:** We've had people leave... Yeah.

**Adam Staravia:** Without being, you know TMI, what are some of the reasons? Have they been negative, or has it just been mutual separation...?

**Cliff Baffle:** I actually really like basically everybody who's left. For some people, this work environment doesn't work. Honestly, it barely works for me. Like, the all remote thing... I actually took this job because I turned down two other offers that were fully remote, because Oxide at the time wasn't...

**Jerold Santo:** Yeah.

**Cliff Baffle:** And this was in February 2020, so you can guess what happened next.

**Adam Staravia:** Yeah.

**Cliff Baffle:** So... Oh, well.

**Adam Staravia:** Literally next. The very next month, yeah.

**Cliff Baffle:** It's a good thing my doctors are great, but the whole remote thing doesn't work for some people. And sometimes you just can't ever really get in the swing of things.

**Jerold Santo:** Yeah.

**Cliff Baffle:** We've had folks where this turns out to set off others past work trauma... Like, we've all got like work PTSD from some shitty former boss. And if things are happening here that's too much like that, you might get freaked out and decide you need to leave, which I totally respect. We've had folks like Arian - Arian joined before me, and was involved in bringing me over here, and he just left last year because he's like "I've been here for five years. I feel like I've done all the startup stuff I can do here. I'm going to go do a new startup."

**Adam Staravia:** So just time.

**Cliff Baffle:** Yeah.

**Adam Staravia:** So mostly good reasons. Not like "This place sucks. I'm out of here."

**Cliff Baffle:** I think there's -- you could probably find people that think this place sucks.

**Adam Staravia:** Yeah?

**Cliff Baffle:** Yeah. I'm not totally sure who, but I'm pretty sure you could.

**Adam Staravia:** One person?

**Cliff Baffle:** Probably one or two.

**Adam Staravia:** Two people.

**Cliff Baffle:** I don't know.

**Adam Staravia:** Out of 80, that's pretty good odds.

**Cliff Baffle:** It's not too bad.

**Jerold Santo:** How do you feel about the uniform compensation stuff?

**Cliff Baffle:** I think it's amazing it's worked this long. It was part of the reason I joined. Because I came in all like knives out, expecting to negotiate...

**Jerold Santo:** Yeah.

**Cliff Baffle:** \[24:02\] ...and Steve's like "So what we're doing is we give people stock according to this formula, and we pay everybody the same amount of dollars." I'm like "Well, that'd save me a lot of stress. Sold."

**Jerold Santo:** Yeah. Probably the opposite of your time at Google.

**Cliff Baffle:** Yeah. A hundred percent. Oh, my God. My only real concern there is that one of the things I really like doing is bringing people in who either don't have a lot of experience in industry, or like are just out of school, or just out of some other job...

**Jerold Santo:** Right. Mentoring them up.

**Cliff Baffle:** Right. And like, are we comfortable bringing in people that are basically interns, and paying them pretty good Bay Area salaries? Maybe we are.

**Jerold Santo:** Yeah.

**Cliff Baffle:** But I do want us to be able to bring those people in, because that's how we get the next generation of us.

**Jerold Santo:** That's a good point.

**Cliff Baffle:** But if we can do that while keeping the compensation uniform, or at least fair, that would make me really happy.

**Jerold Santo:** Yeah.

**Adam Staravia:** What does it do for your personal ability to show up to not worry about compensation...

**Cliff Baffle:** A lot.

**Adam Staravia:** ...as much as you had to before?

**Cliff Baffle:** Oh, my God. So not having to worry that some of my coworkers are getting screwed over by having not like hardball negotiated in their interview... So I became a manager at Google, of a team that I had previously been on... And at that point, at the next promotion cycle, I was able to see everybody's salaries for the first time, and that was how I found out that there was like a hundred thousand dollars a year difference in salaries among people at the same level on my team.

**Jerold Santo:** Wow...

**Adam Staravia:** That's a lot of money.

**Cliff Baffle:** Yeah. And it was mostly us guys that had the higher numbers. It was kind of crap. So I don't have to worry about that here, which is great. And I feel like people are a little more comfortable talking about both job conditions, and also kind of like financial stress. Some people have been really open about like "My husband lost his job, and we've got the new kid, and so it's kind of rough right now..." I feel like people are a little more comfortable sharing that, because we all know what we each other make. So it's not like you're going to reveal that "Oh, wow, you're being really overpaid", and now all your colleagues are mad at you. So it's got its perks.

**Adam Staravia:** This may not be accurate, but one thing I thought about was the fact that it seems like you all are owners of the company. Like, everyone in there that works here owns --

**Cliff Baffle:** Small owner, yeah.

**Adam Staravia:** You all have equity. Some may have more, some may have less, and the compensation is the same across the board, but what changes is you have a different job. One person has a CEO job.

**Cliff Baffle:** Yeah.

**Adam Staravia:** Now, that person may have more equity, but that's because they also started the company.

**Cliff Baffle:** It's because they were here early.

**Adam Staravia:** The compensation is a little different. But the day-to-day, the check, the reason you show up, it seems like an even playing field, and you all are sort of owners in a way...

**Cliff Baffle:** Yeah.

**Adam Staravia:** ...as much as you can be owners, equitably.

**Cliff Baffle:** I really don't like hierarchy. When I'm managing people, I view -- manager's just a job. Like, it doesn't mean that I'm above you, or like in control of you, or better than you. It's that I'm going to do the manager things, you can do the engineering things, and we're both happy. And I'll develop skills here, you develop skills there. But I kind of feel like we've got the same thing going up through Steve. Steve is the CEO. He does the CEO work that we don't want to do.

**Adam Staravia:** Who wants to do that job, right?

**Cliff Baffle:** The sales guys --

**Adam Staravia:** That job he described on stage... I was like "Wow, that is a hard job."

**Cliff Baffle:** Yeah. Like, our sales team - they do the sales that I don't want to do. They're good at it, clearly. They actually make different amounts of money... Furthermore, they're the one corner case. Because salespeople - we have an incentive thing, where the more they sell, the more money they make...

**Jerold Santo:** Yeah. Compensation.

**Cliff Baffle:** ...which we're excited about, and we don't have a problem with. So yeah, I do think it helps with the sort of sense of like we're all in this together...

**Jerold Santo:** Yeah.

**Cliff Baffle:** Which is good.

**Adam Staravia:** 100%.

**Jerold Santo:** Well, we'll let you get back to it.

**Cliff Baffle:** Alright.

**Jerold Santo:** Thanks for chatting with us. It's been awesome.

**Cliff Baffle:** Yeah, my pleasure.

**Adam Staravia:** We appreciate it.

**Break**: \[27:28\]

**Adam Staravia:** What is the update on the update?

**Dave Pacheco:** Well, let's see... We're working on shipping the first version of what we call a self-service update for the Oxide rack. So today, the process for updating the Oxide system, including the control plane and everything, involves a support process where our support engineers are getting on the system through a debug interface... And that works pretty well for a lot of things, and it's very simple, but it doesn't work for a lot of customers to have an Oxide person involved in the whole upgrade operation. And so we want that to be something that they can do through the API, just like they can do all the rest of the infrastructure stuff. But that is kind of a big deal, because that means that the control plane is driving the update, which means the whole control plane is online during the update. People use different metaphors for this. It's replacing all the parts on the car while you're driving down the freeway, or replacing all the parts on the plane while it's in the air, or whatever, but... It's just a lot of work to make that work.

**Jerold Santo:** How long have you been working on that?

**Dave Pacheco:** I've been working on it for about two years.

**Jerold Santo:** How long has Oxide been working on that?

**Dave Pacheco:** We needed an update process for our MVP. And so that started before that and finished before that, because we launched before that... But that's the process that we use today, the support-based process.

**Jerold Santo:** This is like an upgraded rewrite.

**Dave Pacheco:** Kind of, yeah. So the idea behind the first version of update was what we called the minimum upgradeable product, which was Update... And so the idea here is that, you know, it's an MVP, we're shipping it really as fast as we can... But there's a lead time between when you deliver software to the factory and when you actually get it at the customer site... And that's a period in which we can continue working on the MVP. And so what we needed was for there to be enough in that first thing that we could update it to whatever software we wanted once we got to the customer site. And that became the minimum upgradeable product, which is Update, and that's the procedure that we have today.

So the priority there was about having a robust support procedure for recovering the software on any one of our compute sleds. And that's something that we knew we needed even separately from update. And so that's why it came first, was this idea - like, we need the ability to recover a sled (one of our compute sleds) no matter what state it was in, and we can use that to do our initial updates. And that's what we've been doing for the last two years. So in that sense, we've been working on it for a while. But in terms of being able to have the control plane do a more operator-friendly update, that's been about two years.

**Jerold Santo:** Gotcha.

**Dave Pacheco:** And actually, even that - there are a bunch of building blocks involved in that; what I've come to call dynamic reconfiguration of the system. So having the ability for any component to come and go while the system is running is kind of a prerequisite for that, but it also allowed us to deliver other important things that customers would expect to be there... Like the ability to remove a sled, replace a sled, add a new sled to the system. The first year of the update project was really building this foundation that we use for these other support procedures as well.

**Jerold Santo:** Gotcha.

**Adam Staravia:** \[31:47\] What exactly is an update? Is it big? Is it small?

**Dave Pacheco:** That's a perfect question, because --

**Adam Staravia:** What's happening?

**Dave Pacheco:** ...you think of the control plane as like "It's the control plane. It's just like one big piece of software", or something like that.

**Adam Staravia:** Sure.

**Dave Pacheco:** But actually, every single one of our -- so in a rack we've got 32 sleds, we've got two switches, and we've got a couple power shelf controllers. Every one of those has a service processor, a root of trust, and the root of trust has its own software, and the bootloader software. Then, on all the 32 sleds, we also have a host OS, which comes in two parts, for historic reasons around bootloaders and stuff. Then we have all the control plane software on top of that, including storage software, which is one per disk. What all this means is that when you update the software in an Oxide system, you're updating literally hundreds of components, and we're kind of doing it one at a time. And you're also going through all these intermediate states where you're running some of the old software and some of the new software. So you ask "What is an upgrade?" We're replacing all the software running on everything in the system. And it's a lot of different things.

**Adam Staravia:** It's a big deal then.

**Dave Pacheco:** Yeah. And that list I just gave doesn't even include a lot of stuff that for us gets bundled. CPU has microcode, NIC's have their own firmware. For the update system, that's simplified, because it all gets part of the host OS, but there's a lot of software in the system, and it's updating all of those things. But the whole idea of what we're doing is that operators don't have to think about any of that stuff. So our release process puts together a giant zip file; it's like two or three gigs of data. You download that from us, you can look at it if you want, you can validate it, whatever... But then you upload it to the API, and you hit Go, and then the system goes and churns for probably a couple of hours up front, and then you come back, and then the whole thing's updated. So the idea is that the operator is only thinking about this policy. They're not thinking about all those other things that are involved.

**Adam Staravia:** That's nice it's a zip file. I mean, several gigs, though...

**Dave Pacheco:** It's a lot of software, yeah.

**Adam Staravia:** I mean, even the bandwidth cost on that. Do you measure that? Does it matter, as you grow your customer base? I mean, obviously not, because you're getting paid lots of money... But you've got to worry about those things, right? Speed to get it, accessibility...

**Dave Pacheco:** It's a good question. It's not something we've been focusing on for the most part so far. It's the kind of thing where the customer is currently going to be responsible for getting that from whatever our download site is, whether that's GitHub, to the rack.

**Jerold Santo:** \[unintelligible 00:33:58.20\]

**Dave Pacheco:** Yeah. So they might get that on their laptop, downloading it from GitHub, or something like that. And then they'll upload it to the rack.

**Adam Staravia:** \[unintelligible 00:34:02.17\] Nice.

**Dave Pacheco:** Yeah, that part is GitHub's problem.

**Adam Staravia:** It's a release. Alright, that makes sense.

**Dave Pacheco:** Yeah. And then uploading it to the rack is over their network. And we've kind of been assuming it wouldn't be an issue... That's a fair question, whether they would consider that an issue.

**Adam Staravia:** I was thinking about size, the file size. I guess most people can download a couple of gigs pretty easily, without it being a major problem... But some people can't.

**Dave Pacheco:** It's definitely a lot.

**Adam Staravia:** I've been told that before. I guess if you're --

**Jerold Santo:** Most of their customers are not...

**Adam Staravia:** Yeah, they're probably not having this problem. I'm solving different problems here, Jerold.

**Jerold Santo:** What about air gaps? So some people opt for an air gap.

**Dave Pacheco:** Yeah, that's really important, too. This model works pretty well for air gaps, because you, the customer, are downloading it to your laptop, and then uploading it...

**Adam Staravia:** No connection required.

**Dave Pacheco:** No connection to the -- the rack definitely doesn't care. It doesn't even know if it's connected to the internet. That's fine. It doesn't care.

**Jerold Santo:** Right.

**Dave Pacheco:** You could imagine a nicer experience where the rack was connected to the internet, and could see, "Oh, Oxide's just published a new thing, and I'm going to download it." And maybe I only download certain parts that I need, or I download it one part at a time... Maybe that helps with some of the bandwidth stuff. But actually, it's not something most of our customers are interested right now. Most of them are actually more interested in the "I'm really not connected to the internet, and I'm doing this because I care about my security, and my privacy, and my data. I definitely don't want the rack talking to the internet", so that's why we've done it the way we've done it.

**Adam Staravia:** We talked to Cliff earlier about Hubris... So when you look at Hubris, that's the operating system. You mentioned a couple of chips, every different device on there... When the update comes through, is that on top of the API of Hubris? Or is that -- how are they compared to each other, this update and Hubris?

**Dave Pacheco:** Yeah, so Hubris is a sort of... It's an operating system. We use it in a couple of different components in the service processor and the root of trust, on all of these systems: on the sleds, the switches, and the PowerShell controllers. So it's one of the things that we update. It is also true that in order to update everything, we talk to the service -- or in order to update much of the system, we end up talking to the service processor, which is talking to that Hubris thing. So we end up using the current version of Hubris through the service processor to be able to update the service processor itself, the root of trust, the root of trust bootloader, and the host OS as well. All the control plane stuff is on top of that and doesn't go through Hubris.

**Adam Staravia:** \[36:12\] Is this a novel problem that you all invented, given your architecture?

**Dave Pacheco:** That's a good question. Yeah, a lot of the details are specific to our architecture and pretty novel. It's the sort of thing that I expect cloud providers today have their own bespoke software for. And in fact, large deployments of on-prem stuff will have their own bespoke software to do a lot of this stuff. But a lot of it is also stuffed that people kind of just don't update. Like, how often do you update your BIOS? How often does a company running on-prem software update their BIOS? Probably not all the time. But our model involves delivering a lot of value through stuff like that, and we do need to be able to update that stuff.

I remember back at one of my past jobs, we did have to go update the BIOS on 64 systems, or something like that. And you've been in the BIOS thing, right? You're clicking through the thing, and like how do you do that on 64 systems?

**Jerold Santo:** Oh yeah, \[unintelligible 00:36:59.09\]

**Dave Pacheco:** And at the time --

**Jerold Santo:** One at a time?

**Dave Pacheco:** This wasn't a productionized thing, but at the time I didn't know that term or whatever has this mode which is like "Send all my keystrokes to all the other panes."

**Jerold Santo:** You just taught me that, right now. \[laughs\]

**Dave Pacheco:** Someone just opened up 64 panes, and was just like "Enter, Enter, Tab..."

**Adam Staravia:** Oh, my gosh. I would be that person.

**Jerold Santo:** That's a 64X developer right there.

**Dave Pacheco:** It's a real problem, right? ...when you have this software at such a low layer; it's not really designed to be interacted with by automation. Everyone that's hard to do this has had to come up with their own way to do it, basically.

**Jerold Santo:** Yeah. Well, one reason why you don't update your BIOS very often is because you've got to reboot your machine. And I know that ultimately, your guys' goal is like "No, reboot update", right?

**Dave Pacheco:** That's right.

**Jerold Santo:** That's not what you're working on now, though.

**Dave Pacheco:** That's going to be the next phase, and it's going to be a much smaller part of the problem for us. At least we expect.

**Jerold Santo:** It's going to be easier...

**Dave Pacheco:** You never know until you're done, but...

**Jerold Santo:** It's not going to take you two years...

**Dave Pacheco:** Right. So we've done a lot of the pieces involved in that. All the stuff we've been doing so far is like the orchestration... It's foundational stuff. So our system is based on what's called the plan-execute pattern, which means that before taking any action, the system generates a new intended state of the world, which we call a blueprint. And then it goes and executes that blueprint. And all that was really important foundational work for building a system that can be operated autonomously, which is also really important for the air gap thing... Because we can go test all kinds of things that can happen with just the planner part, without even worrying about the execution stuff.

**Jerold Santo:** Right.

**Dave Pacheco:** And then we can go test all the execution stuff given whatever plan we want, without having to have gotten a system into exactly that state. And it also lets you do all kinds of things, like ask the system "What are you going to do next?" before it does it. And "Why are you doing that thing?" You know what I mean?

**Jerold Santo:** Yeah.

**Dave Pacheco:** So these are really important operational things that we just need to have. That's the kind of stuff that's taken the first two years.

**Jerold Santo:** So you laid a lot of groundwork.

**Dave Pacheco:** That's right. And so now we're talking doing what we're calling non-disruptive updates. So this is doing updates without rebooting the customer VMs. We're still rebooting the sleds.

**Jerold Santo:** So do you move the VMs?

**Dave Pacheco:** Exactly. We're going to live-migrate the VMs. And now, I don't mean to oversimplify it, but that should be just a question of policy, which is like we're flipping a bit in that blueprint that says "This sled needs to be evacuated \[unintelligible 00:39:03.08\]

**Jerold Santo:** So let's say you have an Oxide rack, 16 sleds... Is that typical?

**Dave Pacheco:** Yeah, \[unintelligible 00:39:08.07\]

**Jerold Santo:** Alright. So we've got 16 sleds, and we need to run an update. This is in the new world, when this exists. And each sled has, I don't know, 30 VMs on it. Now we're doing math in our head... "Uh-oh, he's going to do a math problem." No, I'm not going to. And a couple of times run update. So I go put it on my thumb drive, off my laptop or whatever, plug it into the rack, and it's going to run. It's going to live-migrate VMs off of a sled one at a time, update that sled, reboot it, and then move some stuff back to that one, probably.

**Dave Pacheco:** Something like that. Yeah, that's where actually --

**Jerold Santo:** Distribute that load evenly across the other ones, in the meantime...

**Dave Pacheco:** That's where a lot of the complexity does come in with the non-disruptive update, is first, how do you mechanically move these things around? It's like a bin packing problem. But then there's also how do we make sure that we have the capacity to do that? If we're going to start doing -- if you've totally filled every sled...

**Jerold Santo:** If you're running your thing at max...

**Dave Pacheco:** Right, there's no place to put it.

**Jerold Santo:** ...there's nowhere to move them.

**Dave Pacheco:** Right.

**Jerold Santo:** Buy another rack.

**Dave Pacheco:** \[40:11\] Right. \[laughter\] Well, that's the thing. At scale, people actually don't care about this problem. Because keeping a couple of sleds capacity free when you've got 100 racks is like a very small fraction of your cost. And it actually makes sense for a lot of reasons. It also allows you to sustain failures, and put that stuff over there. But when you've only got one rack, that might be more of a problem. So then there's the question of how do you create an experience for the operator that communicates clearly what the trade-offs are, but also gets this input from them, which is like "What do you want to happen?" Do you want me, the rack, to prevent you from using all your capacity, so that you can update it? Or do you want to have the possibility that you go do an update, and we just say "Sorry, we're paused right now until you can tell us just like "Reboot all these VMs", or whatever you want to say."

**Jerold Santo:** Right. That reminds me, or that makes me think of failed updates in the self-service world, when this version's out; not the... What do you call it? Undisrupted?

**Dave Pacheco:** Non-disrupted.

**Jerold Santo:** Yeah, non-disrupted. With the current iteration you're working on now, can you guarantee that an update will finish?

**Dave Pacheco:** That's not what I thought you were going to say.

**Jerold Santo:** \[laughs\]

**Dave Pacheco:** Finish? No, because there are things outside our control. For example, one of the biggest challenges in self-service update - because the control plane is running, we have these intermediate states I mentioned, where you've got new version of software talking to old version of software. And how do you avoid that becoming a problem on our ability to change our own software, because you have to do backwards compatibility forever? And one of the ways we've addressed that is to say that there will be an order to the updates. So we will always update, for example, the host OS before we update the control plane that talks to it.

**Jerold Santo:** Okay.

**Dave Pacheco:** Because the reverse never happens right now. And so that's fine. But that means that if you're doing an update and one of the sleds is like out to lunch, and we can't talk to it, we don't know if we've been able to update it, we can't actually keep going and update the rest of the control plane.

**Jerold Santo:** You got a wait for that sled.

**Dave Pacheco:** Yeah. So we've got to tell the operator "Look, you either need to do (what's called) expunge the sled", which means to remove it from the control plane, and we'll pretend like it's just caught fire; like, it's failed, and we've moved everything else elsewhere. Or you've got to figure out what's wrong with it and bring it back. And that would be a support call. Probably a support call. And then \[unintelligible 00:42:14.11\] just unplugged it, and they just plug it back in, or whatever. Those sorts of things are always outside our control.

**Jerold Santo:** Now, what did you think I was going to say?

**Dave Pacheco:** I thought you were going to say an update that explodes; that like you start doing the update --

**Jerold Santo:** That was my next question.

**Dave Pacheco:** ...and the control plane is now down, and - what do you do?

**Jerold Santo:** Right.

**Dave Pacheco:** And that's my nightmare. That's been my fear for the last couple of years.

**Jerold Santo:** \[laughs\] That's why it's taken two years and you are not done yet...?

**Dave Pacheco:** Yeah, but seriously, that is why we've spent so much time on having the automation take these careful steps where every one of these steps we know is safe. As an example, we've got a Cockroach DB cluster that's storing all the control plane database data... We've got five nodes. We definitely don't want to bounce a sled that's hosting a Cockroach node while that Cockroach cluster is already unhealthy. That's just like a thing we want to make sure we never do. Because that increases the risk that we actually lose quorum on the cockroach cluster, and it's dead, and we're in trouble. So we have all these kinds of safeties built into the automation, all this testing, this whole pattern, and all this stuff. So that's like one angle. Obviously, testing is another angle, but that's kind of a given.

**Jerold Santo:** Sure.

**Dave Pacheco:** But it's a hard problem really, because part of what is involved in an upgrade is making backwards-incompatible changes to data formats, like database schemas, and things like that. And once you've done that, the old software can't read the new thing. So rollback is really not possible. What a lot of software does is it'll have a point of no return. Some call it a finalizer, or a deferred update, or something like that, where you basically get the whole thing kind of working before you've committed in that way, and then you ask the operator "Does everything seem to be okay?" and then they hit the button, and it's like "Okay, fine. Go."

\[43:57\] But even then, there's still risk there, because whatever it is you're activating by taking that last step hasn't been tested before that. And there's kind of no way to get around that. And that's kind of a future problem for us right now, but it's something we're going to have to deal with.

**Adam Staravia:** So it is your nightmare... Has it ever been, your nightmare? Meaning it's happened.

**Dave Pacheco:** Like, in my career, yeah.

**Adam Staravia:** Well, specifically for Oxide, and updates...

**Dave Pacheco:** No, no. It hasn't.

**Adam Staravia:** Any updates gone wrong?

**Dave Pacheco:** No, but we haven't started doing that in production yet, so there's still time for that, I guess...

**Adam Staravia:** How do you do it in production now?

**Dave Pacheco:** The process we used --

**Jerold Santo:** The manual way...

**Dave Pacheco:** Yeah, the manual thing when we -- so how the manual process that I was talking about at the very beginning works, basically it shuts down the whole control plane, and replaces all the software and brings it back up again.

**Adam Staravia:** How long is that process?

**Dave Pacheco:** It's actually not that -- it's shorter than the other way.

**Adam Staravia:** I feel like that's safer.

**Dave Pacheco:** It is safer.

**Adam Staravia:** I mean, I get the whole reason --

**Jerold Santo:** Downtime, man. Can't have it.

**Dave Pacheco:** It's downtime, and it's the self-service aspect. Although you could imagine a self-service version that looked more like that, but then the thing is like, if it's self-service, you're talking to an API, what's running that API while the thing is down? There's nothing, right? So that's why you've got to do what we've done.

**Jerold Santo:** It's got to be done.

**Adam Staravia:** So downtime's required now. Future is -- you said non-destructive?

**Jerold Santo:** Non-disruptive.

**Dave Pacheco:** Non-disruptive, yeah.

**Adam Staravia:** Meaning the VMs get migrated around versus shutdown, but you still reboot sleds.

**Dave Pacheco:** That's right.

**Adam Staravia:** You're still rebooting control planes, and stuff like that.

**Dave Pacheco:** Yup. But that's not visible to them, because we have enough --

**Jerold Santo:** Is there a world in which that isn't even required?

**Dave Pacheco:** Which part?

**Jerold Santo:** What if you didn't have to reboot anything?

**Dave Pacheco:** Oh. I think that's pretty dicey. It's definitely a thing that people have done...

**Adam Staravia:** Hot swap?

**Dave Pacheco:** Yeah. There are types of updates, or patches, running the latest kernel, where you kind of write the new one over here, and then you jump over there... But then the state --

**Jerold Santo:** It's just a pointer... \[laughs\]

**Dave Pacheco:** It is. It's all software, right?

**Jerold Santo:** That's right. Like, who says we have to reboot, you know?

**Dave Pacheco:** Yeah. That is definitely harder to do with stuff like \[unintelligible 00:46:02.02\] job is to attest to the software that's currently running.

**Jerold Santo:** Yeah. If you're going to change it out from underneath it \[unintelligible 00:46:11.13\]

**Dave Pacheco:** Yeah. You need to figure out what that means. And then there's also this risk that you're now in a different state than you would have been in if you had actually bounced that thing. So have you created a time bomb for yourself, where if that thing loses power and actually does power back on, is it going to do the same thing that it was doing? That's the thing I always -- bifurcated code paths, where you're like "This is the thing we sometimes do and this is the thing we do other times" is totally the kind of thing that results in something failing at runtime.

**Jerold Santo:** A catastrophic failure.

**Dave Pacheco:** Yeah.

**Jerold Santo:** Alright, fine. Bad idea.

**Dave Pacheco:** The thing you asked about, like my nightmare, right? The upgrade just explodes, and we're toast.

**Jerold Santo:** Yeah.

**Dave Pacheco:** Another thing that we've done there is try to create a lot of guardrails around the types of changes that we can make to the software, so that we know if we're making a change that's going to break things. So for example, if you're changing the database schema, we know that you're changing that, and we've operationalized that one. So that's kind of fine. If you're changing like an internal API, we make sure that you're doing it in a way where none of those intermediate states will expose us to a situation where those components don't speak a common version. And that's something I imagine other organizations do. I haven't actually really seen that before, but I think it's really important. Because that's the way that I've seen this fail in the past, is like, someone goes and makes a change to the API; they're "I'm not changing upgrade." So like they test everything, everything seems to work...

**Jerold Santo:** Right.

**Dave Pacheco:** And you go deploy it, and it blows up in the middle. It's like, we've tested the end point, we've tested the beginning point, and we just got unlucky in one of these intermediate states that wasn't tested... And so we've tried to identify the kinds of changes that would cause those problems, and then detect those at CI time for us, and at build time if we can.

**Jerold Santo:** That's cool. Any newer novel testing strategies that you've had to come up with as far as this? I don't know, fuzzing, or deterministic testing, or anything that's...

**Dave Pacheco:** \[48:00\] That's probably the biggest one. The other thing I would point to is that sort of distinction between the plan and execute stuff. We haven't actually gotten to this kind of thing, but one of the things we want to do with that is like property-based testing on the planner, where you're basically like sending all kinds of different inputs at it and putting constraints on what kinds of outputs can happen, and make sure it never does anything crazy.

**Jerold Santo:** Make sure it does that, yeah.

**Adam Staravia:** You were supposed to give a talk today...

**Dave Pacheco:** Yup.

**Adam Staravia:** It got rescheduled...

**Dave Pacheco:** That's true.

**Adam Staravia:** We're not going to be here for it...

**Dave Pacheco:** Right.

**Adam Staravia:** ...so you have to spill the beans.

**Dave Pacheco:** Yeah, so let's see. What was I going to talk about?

**Adam Staravia:** Updates... \[laughter\]

**Dave Pacheco:** So I've been doing this for a couple of years...

**Jerold Santo:** Update on the update.

**Dave Pacheco:** We have a surprising number of new faces... And so part of that talk is literally the stuff we were just talking about, like "What is update?"

**Adam Staravia:** What is it?

**Dave Pacheco:** Well, we've got a couple of hundred components that we've got to replace, and... Pick your metaphor, or whatever. And so part of it is just like laying that out. And what we do today... The stuff we've been talking about - why this is a problem for customers, what we're doing, current status of that, which is like we're planning to ship the self-service part very soon now, and then non-disruptive is coming after that... And then the rest of it was probably -- I don't know if that's fascinating to a broader audience, but it's kind of reflections on what it's been like to run a project for such a long term. And I don't know, maybe it is more generally interesting, but... I have a lot of fears about update at runtime, but my big fears about update as a project was that it would feel perpetually a year away, and we would make decisions day to day and week to week that ensured that it continued to be a year away. Because when something's like a month away and somebody asks you to do something else, you're like "Sorry, I've got to do this thing. We're shipping it in a month." But when something's a year away, it's very easy to be like "Well, here's a really important problem over here..." And it's hard to know what the next thing is to do on update.

That's been really a challenge the whole time, is like "What's the next step?" There are so many steps, and there are so many circular dependencies in those steps that you're like "Well, I've got this other important problem over here. Maybe I'll just kind of solve that." And that's fine. Sometimes that's the right call. But if you make that call...

**Jerold Santo:** Over and over again...

**Dave Pacheco:** ...even 20% of the time... Right, exactly. You just never get there.

**Adam Staravia:** You timeline stretches.

**Jerold Santo:** How close is it?

**Adam Staravia:** He said very soon. Didn't you hear him?

**Dave Pacheco:** Yeah. \[unintelligible 00:50:07.27\]

**Jerold Santo:** Within the next month, or...?

**Dave Pacheco:** That's the plan... \[laughter\]

**Jerold Santo:** That's not a year away, though.

**Dave Pacheco:** No, no, no, no, no. This was two years ago I was worried about it. Two years ago, I think I was like perpetually a year or two away.

**Jerold Santo:** Well, I saw the roadmap this morning, I saw last year's roadmap... It's not a roadmap --

**Dave Pacheco:** Did you diff them and see \[unintelligible 00:50:26.02\]

**Jerold Santo:** One of the things was Update, and then the priority this year is Update...

**Adam Staravia:** \[unintelligible 00:50:32.28\] which was first.

**Jerold Santo:** ...so ongoing...

**Dave Pacheco:** Accurate.

**Jerold Santo:** But almost ready.

**Dave Pacheco:** Yup.

**Adam Staravia:** Almost ready.

**Jerold Santo:** That's cool.

**Adam Staravia:** Well, why you? So we had a side conversation... He's been with Brian almost his whole career.

**Jerold Santo:** Really?

**Dave Pacheco:** That's true.

**Adam Staravia:** Sun, to Oracle, the acquisition, and then Joint... And then what makes you uniquely positioned for this task, this quest?

**Dave Pacheco:** I don't know if I'm uniquely positioned, but right after we shipped the MVP, this was one of my big worries about the products... And I was like "This is something I think I have a lot of experience with", in terms of building distributed systems, and reliable automation, and things like that. And so I thought this was a good opportunity for me to swing in and try to create the vision that I want us to get to, and then be able to execute that. So I was interested, and I asked, and that's how a lot of stuff works around here, so...

**Adam Staravia:** What has it been like casting the vision for it and getting feedback from the team? Because I'm thinking culture, I'm thinking the process of getting feedback on any idea... Because you're laying out all this groundwork, and you're doing all the work to kind of get to a direction. What is it like to put that idea out there, that vision out there, and get that feedback and start moving on it?

**Dave Pacheco:** It's great. I mean, I don't know if you all talked about the RFD process, but...

**Adam Staravia:** The RFD process, yeah.

**Dave Pacheco:** So when I started on this, the first step was writing an RFD. I think it's 4.18, if you want to find that...

**Adam Staravia:** Is this public, the RFDs?

**Dave Pacheco:** Some of them are and some of them aren't. I don't know what that one is. It probably could be, if we want it to be.

There's nothing particularly sensitive in it. But it's kind of laying out where we are. Lay of the land, this is where we are, these are the problems, here's where we're trying to go... And it was very specific in some ways. It was like this idea of plan-execute pattern, and the automation has to be safe, and all this stuff. But it was also very like "We have a lot of stuff to do, and I don't know what all the pieces are yet."

\[52:24\] So that was the first step, is getting everyone aligned on the vision. And that RFD itself was a team effort. I drafted this first version, but people are looking at that... And I think broadly, there were no surprises there. Everyone was like "Yeah, this all makes sense." And then that process just keeps happening. You get more and more specific designs, and say "Okay, let's get some feedback on this." And I do enjoy that part of it, and I enjoy the collaboration... And it goes pretty well. Like, it's not the sort of environment where you're worried about what so-and-so is going to think about this, and is someone going to be unproductive about it, or something.

**Adam Staravia:** Sure. We know that Rust is a foundational language here, obviously. We talked about this being somewhat of a novel problem... How is Rust uniquely positioned to help solve this problem? Like, what about Rust makes this problem easier than another language that you may choose to do this with?

**Dave Pacheco:** Yeah. So the big thing for me about Rust, that I really love, and I think that's been huge for Oxide, is its ability to help us ensure things, especially at build time, that need to be true of the system. That sounds really vague, but what I mean is you can catch so many problems early. And everyone talks about the obvious ones. We talked about this earlier, but everyone talks about the obvious ones, like, the borrow checker will help you find memory safety problems, but it also allows you to create abstractions for the rest of the team that can't be misused, right? So you can say "I'm creating this thing--" Maybe you represent it with an object, and you say "You can't do these two operations concurrently on it." Well, that's the thing that we can enforce in the type system, and you literally just can't compile the code that would do that. That's awesome.

And it sounds so low-level, but that's what a lot -- like, it's extending that same idea and applying those same tools to do it, that allows us to say "If you try to evolve the API in a backwards-incompatible way that won't work at upgrade time, depending on how you do it, you might get a build failure." You'll at least get a CI failure. I don't know if we have a minute to talk about it... I mean --

**Adam Staravia:** Gush, man. Gush.

**Dave Pacheco:** So one of the first things that I built here with Adam Levinthal is something called Drop shot, which basically lets you write an HTTP server and then generate an open API spec from the code. And then we feed that into something called Progenitor, which generates the clients for it. But that alone means that if you make an incompatible change to an API, even before we'd done any of the versioning stuff, your client fails to compile now... Which is like hugely valuable. And that's true, not just because of it doesn't have the operation in it, but like you passed an enum with three variants, and it now has four variants, and you need to like to accommodate for that fourth one, or something like that.

**Adam Staravia:** I call them ends...

**Dave Pacheco:** Yeah.

**Adam Staravia:** Just sayin'.

**Dave Pacheco:** Yeah. So anyway, we ended up extending that, so now that's how we do this versioning stuff, is we have a bunch of these open API specs that are the ones that this thing supports... And then we know if you've changed it, because we know if it generates a different thing, then you've changed it incompatibly. So Rust has facilitated all this stuff. And sorry, the last thing I want to say about that with the Drop shot thing is you've got your rich, structured types in Rust, and you're like all happy, "Because I'm in Rust land, and I've got my strong types." That carries all the way to the client, because of the way it goes -- like, Drop shot just takes those types and puts them in the open API spec, and then the client generates faithful things on the other side. So you basically get that strictness all the way through there.

**Adam Staravia:** Gush a little bit more on this then. Speak to your confidence in the code you write because it's Rust. I'll just -- easy shot you that one.

**Dave Pacheco:** Yeah. I mean, I'm reluctant to make any bold claims about the correctness of the code I write, lest I immediately walk back in there and there's some horrible thing happening...

**Adam Staravia:** Sure. If the fans spin, you know that's why.

**Dave Pacheco:** \[56:07\] But I mean, I'll say this... There are a lot of changes I've been able to make where I'll go work on the code for like four hours, and when it compiles, I know it's already correct. I know I haven't broken anything. And it's not as simple -- I know there's the cartoonish version, "if it compiles, it works." And I'm not talking about that. I'm talking about something that's either a refactor... This happens a lot with refactors. Or I'm building a new thing in terms of these things that already exist, and I'm plugging into the middle of it... And it's like, there's no way for this to be wrong at this point, because it fits neatly into the narrow interfaces on both sides of it. It's correct. And that is huge. It's so huge.

**Adam Staravia:** No nightmares.

**Dave Pacheco:** My previous experience was in Node.js, and it was the complete opposite of this. And part of the reason I love Rust is by the time we got to the end of the road at my last job when we were using Node.js everywhere, every single JavaScript function we had started with like 30 assertions about the types of all of its arguments. And I'm like "Why are we doing this? The computer can do this. It's what the compiler is for." And so I have so much more confidence in those things now.

And that gets back to why I think Rust is so valuable for this problem space, is that these things are so complicated... By allowing us to encode all these constraints into build time constraints, that allows us to evolve the software so much faster, and with so much more confidence. Someone can come in here and make a huge complicated change, and you're not wondering about "I wonder if they missed some callers", or something like that. It's like, no, you haven't. You've covered every single case. And that's huge.

**Adam Staravia:** It's huge. Right on, man. What else? Anything?

**Jerold Santo:** Tell us about Ox Con.

**Dave Pacheco:** Ox Con. Ox Con is awesome. So this has been something we've been doing for a while, and this is something we -- it's very similar to something we did at Joint, this sort of company-wide meetups, engineering-wide meetups. For a remote company, it works really well to be remote basically all the time, but it is also so valuable to have that time in person together, to get to -- there are so many conversations that don't happen if you haven't scheduled a meet for it. And we have other ways of trying to have those conversations anyway, but it's just really nice to have the FaceTime with people, and to also -- like, the small talk, and you're going to get dinner, and you're just like talking to people about whatever it is, you learn more about them... It's a perfect time.

So there's a mix of the structured time that we have... You know, Brian and Steve talking about all the exciting stuff over the last year. It's inspiring for people, it sort of gets everyone ginned up to talk about everything that we got to go do... And then there are other good, company-wide sessions talking about important projects and stuff like that, but then there's also all this breakout time that I started by talking about, which - as with any conference, the hallway track is almost... It's at least as important as the rest.

**Jerold Santo:** It's the best.

**Adam Staravia:** It is the best.

**Dave Pacheco:** Yeah, right? So that's huge...

**Adam Staravia:** Conference talks, not really... Hallway track only. Keynotes only, and then hallway track.

**Jerold Santo:** That's our move.

**Dave Pacheco:** This is so much more -- it's getting more mature and professionalized. We never had a stage before...

**Adam Staravia:** No?

**Dave Pacheco:** We never had like pro A/V before... So this whole week is a little bit of a dream. Ox Con already feels different. And then we've got the stage there, and then it like rained in the Bay Area in September this morning, and I was like "Am I dreaming, or what's going on here?"

**Adam Staravia:** Yeah.

**Dave Pacheco:** But it's a good time.

**Adam Staravia:** Thanks, Dave.

**Dave Pacheco:** Thank you. I appreciate it.

**Jerold Santo:** Thanks. It's been awesome.

**Break**: \[59:28\]

**Adam Staravia:** One of the things that stands out about Oxide is its design. I think you can have a good company, a successful company, but every company that's successful is set apart by its design. Can you talk about how you came to be here at Oxide, and the design story behind the brand?

**Ben Leonard:** Yeah. So I was working at a branding agency called Pentagram. Oxide was my last branding project. I was planning on leaving to work as a freelancer. I'd been at Pentagram for four or five years, I was ready to move on. And it just so happened that Oxide were looking for a designer just as I was leaving, and it felt like a unique opportunity.

Because what would happen is you'd work on these brands, and then you'd throw it over the fence, and then you'd check in on it like two years later, like "What have they done to my baby?"

**Jerold Santo:** They destroyed it.

**Ben Leonard:** "My boy, my boy...!" And so it was a unique opportunity to continue it on. And I'm kind of -- I was telling you about this before, I'm relentless. I like to fiddle with things.

**Jerold Santo:** You keep working on it.

**Ben Leonard:** Yeah, I kind of get bored with it as well, so I just want to tweak something... Recently, we made a modification to the logo that most people wouldn't even notice. It's slightly thicker, but it's something that's been bugging me this entire time...
**Adam Staravia:** I noticed.

**Ben Leonard:** Yeah, yeah, yeah.

**Adam Staravia:** When Steve was up here, I was like "Steve's shirt has the thinner logo..."

**Ben Leonard:** Yeah, yeah.

**Adam Staravia:** And on stage here, it's much thicker. I noticed that.

**Ben Leonard:** Right away, right away.

**Adam Staravia:** I saw it. I noticed kerning... Oh, yeah.

**Ben Leonard:** Yeah, so I'm always fiddling with stuff. But then the beauty of Oxide is I get to work across everything. So I'm working across -- generally, most of what I do is working on the product. So in my case, it's the web console. So I work on the design system, on the UI, but I'm also working on the brand, and the marketing, and the sales assets and all this stuff; on the industrial design... The beauty being is that those all inform each other. Because what tends to happen is you have your product team and your creative team, and they're very distinct. This is a bit in the weeds, but our --

**Adam Staravia:** Go in the weeds.

**Ben Leonard:** We have the same UI design system that drives every piece of design. We have the same colours, we have the same UI elements on both the website and the web console. They're kind of continuously informing each other. I mean, it's difficult, because I think there's been a shrinking of creativity in tech design, that is branding stopped being -- what it was is that the product itself, so the proliferation of SaaS, the product itself became the design. So the UI language of the product became the design.

Linear is a great example of this, which is the design of the product and the design of the creative are one and the same. What that can mean is the world of design within product is much smaller. And so what that can mean is you have -- everyone's always complaining that all tech looks the same now. And that's probably because product is much smaller, and if your brand looks like your product, then your world is much smaller.

I'm always figuring out how wide I can go with the branding, and keeping it still like it comes from the same world as everything else... And yeah, the industrial design, the creative, the product - there's so much to work on, so you have this variety.

**Adam Staravia:** This rack behind us... Would this rack behind us look like that at all if you weren't here?

**Ben Leonard:** It'd look a bit like that.

**Jerold Santo:** Same shape, tall...

**Ben Leonard:** Yeah -- if I wasn't here, it'd be squat, it'd be half the size... No, I think--

**Jerold Santo:** Less green, probably.

**Ben Leonard:** It might be less green...

**Jerold Santo:** \[laughs\] Or maybe more green.

**Ben Leonard:** We consulted a little bit with my old agency, Pentagram, industrial designers there, and we worked together on that a little bit. One thing that I'd learned from working on a hardware product previously is the first version was a small run that they distributed to people... And so they produced this thing, which is initially really magical, and then as soon as they mass-produce it, they think "Okay, we're going to have to make this cheaper, easier, more practical to make." And then the next version looked really, terrible. Because essentially, they were just trying to recreate what they've done, and "Okay, we can't do this complicated tile system, so we'll just print it directly on--" It was a PCIe card. And what it was - it was compromised in the worst way... So I think going into it from the beginning thinking "What are our limitations? We're going to make thousands of these, from the beginning..." I don't want to do things that just exist in this kind of initial run... And so figuring out what those compromises are. But industrial design, working with hardware is hard. I haven't done very much of it. But yeah, as soon as you're touching materiality, you're dealing with --

**Jerold Santo:** \[01:04:46.09\] Things are different.

**Ben Leonard:** Yeah. I mean, we were speaking about like colour; colour is the bane of my life. We have painted drive bays, we have powder coated metal, we have plastic pieces, and colour matching the green I think is --

**Adam Staravia:** Yes, that's probably got to be your thing, right?

**Ben Leonard:** Yeah.

**Adam Staravia:** Is that a little off sometimes?

**Ben Leonard:** Oh, it's a little off all the time. It's off all the time. And some of it's outside your control, so you have to think about how to handle that. So what you do is you avoid putting elements next to each other that might be different. If there's a little bit of separation, then visually you can get away with a little bit of difference between those things. One example is originally the rack was black, but it was a slight bluey black.

**Adam Staravia:** Like bluey as in the cartoon bluey?

**Ben Leonard:** Exactly.

**Adam Staravia:** Okay, bluey black. Disregard.

**Ben Leonard:** It was a cool black. Cool as in like colour temperature, not like cool black.

**Jerold Santo:** Oh, I thought you liked it.

**Ben Leonard:** Yeah, yeah. But my thought was as soon as we start integrating multiple components, then I'm trying to make sure I'm using the exact right black. Because --

**Jerold Santo:** Impossible.

**Ben Leonard:** And yeah, so --

**Adam Staravia:** That's hard.

**Ben Leonard:** You're trying, yeah. Although I don't know how much of it is me trying to avoid upsetting myself. Like, these things that no one else notices...

**Jerold Santo:** It sounds like a lot of it is internally-driven.

**Ben Leonard:** Stuff no one else notices.

**Adam Staravia:** Yeah. They're like "Whatever..."

**Ben Leonard:** This is like trauma-driven design. You guys have TDD, I have the same.

**Adam Staravia:** Do you get into the PCB design then, too? Or is it simply this -- and I don't want to simplify what you do, but...

**Jerold Santo:** "Just the easy stuff back there..."

**Adam Staravia:** ...do you get to step into that world where, like how is this -- because I think about Apple. Apple has done a great job of like branding everything.

**Ben Leonard:** Yeah, yeah, yeah.

**Adam Staravia:** From the look of their CPU, right? From their latest M1 chips, or the latest M series chips, it's a design to everything they do. Do you get into that as well?

**Ben Leonard:** I mean, Apple's a good example, because they're stunning inside as well. A little bit... Occasionally I dip my toe in and I get shouted to leave... The PCBs are currently green, and I think once I came into a channel, and I was saying "Hey guys, can we make the PCBs black?" And I'm thinking, "Okay, you change the colour of PCB... I don't know, just order black ones instead of green." I was told that's not the case.

**Adam Staravia:** I think it does have impact to like thermos, and stuff like that.

**Jerold Santo:** What did they tell you?

**Ben Leonard:** They told me some information, none of which I retained...

**Adam Staravia:** "Sorry I asked."

**Ben Leonard:** Maybe they weren't telling the truth, maybe they were just saying it because they were like "Yeah, yeah, yeah..."

**Adam Staravia:** Black was cool. I've seen black PCBs, they were cool.

**Ben Leonard:** Yeah, but there are manufacturing ramifications which mean that it's a bit more complicated than that. I think with the rack you have to take -- there's a balance. We can't go full Apple, and just invest so heavily in details, which costs money for little benefit... But what we can do is make sure that an item which is underappreciated... I like taking boring objects and boring designs and boring things and making them better. I think it's easy to come work with Nike and do some beautiful design for something that's already really compelling. But I think it's much better to take something for which design does not usually kind of feature and try and elevate that.

**Jerold Santo:** \[01:08:24.08\] So Oxide is big on the values... You go to the website, there are values. I'm sure you know all the values. They inform all the decisions, how you act... Do you have a design language or value system or something that drives your design for Oxide, that's separate, or maybe even congruent with that?

**Ben Leonard:** I think there are ideas. I think my approach to branding is you have one idea which should then filter through into everything, and that's how you make a holistic thing. It's not necessarily that this looks like this, it's that it comes from the same place. So with Oxide - Oxide is an old idea brought new. It's this old, crazy idea that you own your own hardware. And so you see that in the design language. You see the ASCII... I mean, the green is like this kind of terminal green... It has this kind of retro edge to it, and so the design language is like old meets new. And yeah, so I think nostalgia is a key part of it. I mean, you see over there, we have the logos, and nostalgia is a key thing. But you don't want to lean so much into nostalgia it's a kitsch. So yeah, I think that sort of referential thing to kind of old computing is a good thing.

**Jerold Santo:** Maybe that's why it speaks so well to us, because we're all about that.

**Ben Leonard:** Yeah, yeah, yeah.

**Jerold Santo:** Where the old meets the new is interesting.

**Adam Staravia:** Precisely. What gets you excited about what you do here? What makes you be like "Hell yeah!" Or however you say "Hell yeah."

**Ben Leonard:** I don't know what the British equivalent of "Hell yeah" is. I don't think we're that -- yeah, we're not that emotive.

**Jerold Santo:** \[laughs\]

**Ben Leonard:** Yeah.

**Adam Staravia:** What gets you properly excited? \[laughter\]

**Jerold Santo:** Now you're talking in language.

**Ben Leonard:** "I'm properly excited...!" No, I just I love to do a bit of everything. And it's the variety I think that really drives me. I've been here more than four years now, I think that's what -- variety is what keeps it interesting. And Oxide's the company where you get to do that; you have hardware, you have software, and everything kind of in between. And yeah, that's the thing that keeps me interested.

**Jerold Santo:** I would expect the opposite. Because at an agency - you'd think that's where the variety comes, because you're on to the next project. New company, new design language, new brand.

**Ben Leonard:** Yeah.

**Jerold Santo:** Whereas you decide to settle down with one brand, and do that for years and years, I would expect it to be less variety. But you've found that it goes wide.

**Ben Leonard:** I mean, I think certainly working at agency, I think it's always going to be much more varied than working at a startup. But I think for me there's this interesting tension between what's staying the same and what's different. There are things in the Oxide brand which have retained; logo more or less... The colours... But I think there are things that are kind of constantly changing. And obviously, I think Oxide as a company is changing, so the design needs are changing...

**Jerold Santo:** Sure.

**Ben Leonard:** As an example, I think we are growing, and so our marketing and sales needs are growing... Previously, there was very little collateral outside the rack, outside the web console and the website. That was it. So you have that kind of small world. But then, when you're kind of entering the world of sales and marketing, then that kind of opens the door to a bunch more design --

**Adam Staravia:** That thing in the door when we came in - was it a cart, with like a chip on it? Did you design it?

**Ben Leonard:** Yeah.

**Adam Staravia:** Does that coin come off the cart?

**Ben Leonard:** It does. It's got two sides.

**Adam Staravia:** \[unintelligible 01:12:08.16\] You designed that, right?

**Ben Leonard:** Yeah, yeah.

**Adam Staravia:** That's fun stuff, right?

**Ben Leonard:** Yeah. I mean, I think those are the palette cleanses. So the big pieces of merch tend to get made just as I finish something that's like drained my creative energy. Website is the big one, because -- I mean, I'm usually coding the thing, too; so I've designed it, I've coded it... It took so long that I'm ready for something else.

I don't know if you saw those, we have the little kind of rack stickers. Those I designed right after I'd done like a run of the website... And so those things are a nice, little --

**Adam Staravia:** A little cherry on top.

**Ben Leonard:** They're a way to kind of refill my creative cup a little bit.

**Adam Staravia:** Yeah. Are you excited about the growth? I imagine with new footprints, we're doing video... We talked to -- a little fourth wall breaking here behind the scenes... We talked to \[unintelligible 01:13:02.16\] about being able to put motion graphics into place, and collaborating on that... Is that exciting to you, to see the different areas you can do?

**Ben Leonard:** Yeah, for sure. I have a list as long as my arm of things that I will eventually get to. Motion is one of those things. There are things that I want to do, but you don't necessarily have the reason to do.

**Jerold Santo:** Yeah. You need an excuse.

**Ben Leonard:** I was chatting about this before, which is like the size of the gamma of like creativity, or things that you can do... Product design is much smaller, because it needs to be functional, and people are using it every day. There's also the zeitgeist of the way that people use products, and you need it to be designed in a way that's expected... And a website's a little larger, and then the kind of creative space is even larger than that. And then you just think about what are these one-off excuses to do something different. So like product launches, all those things that you can get a bit more experimental around.

**Adam Staravia:** We love the work you do.

**Jerold Santo:** Yeah, it's great work.

**Adam Staravia:** It's beautiful work.

**Ben Leonard:** Thank you very much.

**Adam Staravia:** I think the company is awesome, and I think the design really, in my opinion, is -- it's the glue. You can have a great product, you can have great software, but it's the final piece that says "This is just super-awesome." Basically, the design to me is what sets it apart.

**Ben Leonard:** Yeah. I mean, the design is what says you care about everything.

**Adam Staravia:** Yes. It shows intention, it shows trust, it shows all these things, and it's just really important.
