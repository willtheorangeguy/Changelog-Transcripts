**Erik St. Martin:** Welcome back, everybody, to another episode of Go Time. Today's episode is number 71. On the show today we have myself, Erik St. Martin, Carlisle Pinto...

**Carlisle Thompson:** Hi, there.

**Erik St. Martin:** Brian Petersen...

**Brian Petersen:** Thanks for giving me enough time to unmute myself. I appreciate that.

**Erik St. Martin:** And our special guest for today is Carmen Andon.

**Carmen Andon:** Hi!

**Erik St. Martin:** Do you want to give everybody maybe just a little history about yourself, to fill anybody in who's not already familiar with you?

**Carmen Andon:** Sure. Hi, everyone. I am a build infrastructure engineer at Travis CI. Our build infrastructure team uses Go. I entered the GO community as -- I think this is correct, Brian; tell me if I'm wrong - the first-ever Gopher Con scholarship recipient in 2015. It is?

**Brian Petersen:** It's kind of correct, yes. You were our first official scholarship recipient, but in 2014 we did distribute money unofficially, and helped people.

**Carmen Andon:** Right. Yeah, so I was the first official, but it sort of changed my life - I'm not being hyperbolic there when I say that - and I haven't looked back in terms of being a part of the Go community.

**Carlisle Thompson:** I would definitely love to hear how it changed your life. It sounds like such a delightful thing.

**Carmen Andon:** Well, what many people don't know -- so I do have a degree in what back then was called... Oh gosh, they've changed the name now; it was 17 years ago, but I have like a computer science but with fewer calories degree from my university... But then I didn't use it for 12–13 years, because I was a mom, and I went and had kids and I did other things, and I travelled and followed my husband as he was pursuing his degrees to be a college professor.

Then I kind of fell into the university town where he was teaching, I fell into a sysadmin job - a Windows sysadmin - and had to learn a lot of GUIs, Windows, Active Directory and whatnot, and then I kind of went into Linux from there, and then Bash. But I didn't remember a single thing about the C++, the C, the COBOL, the Java that I had learned - and I'm dating myself - in university.

So I wanted to learn a back-end language, and my self-teaching attempts failed. I tried Python and I failed, I tried Ruby and I failed... But I finally -- I think having gone to the Gopher Con... So I was at that time working for a startup, doing things, and it was an all-Python shop, and I was kind of still struggling with Python, kind of growing it, not quite... But then I heard from a friend in the Ladies Who Linux community, "Are you interested in this new language called Go? It's a systems-level language, you might like it." I was like, "Well, I don't know anything." They said "Well, why don't you go to the conference?" and I almost didn't go, because I thought "Well, I don't know anything about this language." Sort of impostor syndrome to the extreme, right?

\[04:02\] But then I went, and I think what I realized was all the -- it took away any kind of intimidation factor that you might have. I now met a community, I now went on Slack, I knew the people, people knew me, I saw how friendly and engaging and willing they were to help me, so that was what it took to finally learn a back-end language. That was just lovely. That then enabled me to kind of put that on my resume, and then I got a role in the Travis build infrastructure team.

**Carlisle Thompson:** A different trajectory, for sure. That's awesome.

**Brian Petersen:** That's awesome in a lot of ways. First, following your husband for stuff has to be a hard decision to make. Did you regret that? Did you feel like he paid it forward later for you? Did your career come out okay? These are strong, hard questions, but this isn't 20/20, we're doing the real deal here.

**Carmen Andon:** Right, so this is an interesting thing that I talk about with women who are in their 20s, 30s and 40s, this idea of "Do you follow your husband? Do you go your own way? Do you try to work it together?" and it's always going to be something that is going to hit women who also maybe are thinking about starting a family, and wondering what that's going to do... But the way that I'm thinking about it, and of course hindsight is 20/20, because everything's worked out okay, but my husband knew what he wanted to do when he grew up, so to speak. We met in the university, and he knew he wanted to be an architect in urban policy and designer. But I didn't really know, and I really didn't enjoy my computer science classes, my language classes, my systems analysis and design classes in college, so I was like, "Well, you know what you want to do..."

I once heard this parable of the base camp. Have you heard of this? I'll try to say it really quickly. In the 1950s or 1960s, seven European and American climbers decided they were going to go to Mount Everest and scale the summit of Mount Everest. And when they get there - this was before the days of the Nepalese and baton people providing assistance and lodging and whatnot. The onus was on the climbers to set up a base camp. So at the advice of some of the locals or other campers, they said "One of you has to stay behind and tend to the base camp while the other five or six of you scale the summit..." None of them wanted to stay, so they decided they would try a compromise. They would get everything ready and prime everything for the base camp, the food and everything, so they would try to put up the provisions as much as possible, and then they would all come up together, and then they would come down.

So indeed, they went up together, now one stayed down at the base camp. They reached the summit, no one died, and they come all the way back down, which is a feat, but what happens is when they get to the base camp, the water is frozen, animals have broken into the base camp and stolen all the food, so they have no more energy to be able to recuperate to get down to the very base of the mountain, because the base camp is probably about 20%-30% up. So all but one die, to tell the tale.

It's a cautionary tale to say that if you want to scale mountains, you can't really do so without somebody tending to the base camp. What I've learned from that in the context of a partnership or a marriage or what have you, in any kind of relationship, is that yes, two of you can scale mountains, but one of you has to always try to do what you can to tend to the base camp, and that has always resonated with me... So I kind of saw that as my thing. I didn't know what I wanted to be, I kind of played with different things in the interim while he did those things, and then when I finally found tech and just these systems administrative thing, I finally realized "Oh, this is what I want to be when I grow up." I was 33 at the time, and it was at that point where my husband said "Alright, I will do what I can to support you", and that's what it's been ever since.

\[08:11\] That's how we've navigated it, so now I have friends who are my age who kind of did the other way around, they scaled their mountains on their own and their crew, but now they're looking at marriage and maybe having children, and asking about that, and what will happen next... So I guess I can say it through hindsight, but everything kind of turns out okay, and you have to be very careful to not always be the person tending to the base camp, because then you'll be resentful of the mountain climber, and you also have to be mindful if you're always the mountain climber to ask the base camp "Do you want your turn?"

**Brian Petersen:** I don't know about you guys, but I'm crying...

**Carlisle Thompson:** Oh, my gosh... \[laughs\]

**Brian Petersen:** Seriously, just tears. I need that relationship, thank you. And kudos to you too for figuring that out.

**Carlisle Thompson:** I was thinking, "This show is so awesome!" \[laughs\]

**Erik St. Martin:** Yeah, I don't think that could have been phrased any better.

**Brian Petersen:** Wow.

**Carlisle Thompson:** Yes, I think I relate to that, personally. It doesn't work when there are two people at a party, and they are both climbing and there is nobody tending to the base camp.

**Carmen Andon:** Yeah. And you know, I think traditionally women have felt the pressure to kind of do that and be that, but now we're in 2018, and we can feel like, you know... So more paternal leave for dads - that's happening, and that is enabling them, because there was what we call toxic masculinity about having to feel like you're the provider all the time... And now if you feel like "Wait a minute, I want to be the dad, I want to be the stay-at-home parent while the other person is the wage earner." That is a pathway that is possible now.

**Brian Petersen:** That is just -- it's so awesome.

**Carlisle Thompson:** Yeah.

**Brian Petersen:** I'm speechless, there's nothing left to talk about. Thanks so much for coming on, Carmen. We appreciate you so much... It's been a great show! \[laughter\]

**Carlisle Thompson:** That was so much wisdom imparted... Nothing else is going to be as awesome as that. \[laughter\]

**Carmen Andon:** It's so funny, because it was something that I heard and really resonated with me about ten years ago... Maybe just around when my second and my third child were born. That was the thing that I kind of was like "Okay..." and I knew that when I found the thing that I wanted to do, that I was going to do it with all my heart, and my husband understood "Yeah, now it's going to be my turn."

**Brian Petersen:** Wow.

**Carlisle Thompson:** But you know what I particularly love about this story? It's that you honoured yourself; you had the courage to just own the "I don't know" space. You didn't just "I'm going to do something because I have to... I have to do something!"

**Carmen Andon:** Oh, no, I did that... I did that, but I didn't go all the way into it. Before this, I work in admissions and financial aid at a university. I read lots of applications, I was a national director for a non-profit... I actually worked as a salesperson for a heavy metal radio station; that was a fun job...

**Brian Petersen:** Yes!

**Carmen Andon:** Yeah, I know, right? Go metal! But yeah, I did all these things, but I did it with the spirit of "Well, it's just what's going to help bring in some extra income", so that my husband could go to graduate school, or do his fellowship, or what have you... But there was never anything like the way I do now; I want to get involved in the community, I want to help make things better, I want to go to conferences, I want to do all those things that I'm doing now for tech.

**Carlisle Thompson:** But that is exactly what I'm talking about. I'm not saying I'm glad that you sat at home and ate bonbons all day, \[unintelligible 00:11:53.25\] but whatever you did, you didn't take it as your path. Things that didn't resonate with you, whatever you were doing... There's no right answer, but you didn't say "This is my path, for the lack of a better option, for the lack of an option that resonates with me." I love that.

**Carmen Andon:** \[12:20\] Well, I once gave a lightning talk at a doomsdays about four years ago, and I was trying to think about what I could say, and I'd always try to think about the long game, the deathbed perspective is what I call it... And what I realized is that our life expectancies are going to be longer, right? We're going to be living longer, and that means we're going to be working longer... But our time with our kids is going to be very short, and so they have this thing called the career rainbow, I think - it's a data visualization which shows how many years you're gonna actively be engaged in the workforce, and how many years you're going to be actively engaged as a parent.

That timeframe to be actively engaged as a parent, which is like 18, maybe 20 years, is far less than what we expect as workers. We're going to be in the workforce between 40 and 45 years. By the time I retire, in 30 years, the average retirement age is going to be up to 75. So when I thought about that, I was like, there's no need for me to rush and to sort of "Get there, get there and get there." I'll find that and then I will contribute. Now I do, I have 30 more years of work left, and so why rush?

**Carlisle Thompson:** Absolutely.

**Brian Petersen:** What a great story.

**Erik St. Martin:** There's another thing that I read a long time ago - I can't remember if it was like part of a book or something - where it talks about newer generations of people being in such a hurry to complete their life's work, and that the average age that people really kind of hit the peak of their careers is usually in the early 50s. If you look at most scientists and their discoveries and things like that, the age of the internet makes us feel like everybody's the 20 or 30-year-old millionaire, but those are really the edge cases.

**Carmen Andon:** Yeah, and it takes time to develop mastery. I once watched a talk by Bob Martin -- I don't know where the source of the information was, but it was like in every five years, half of the people in our industry have 5 years or less of experience. So I'm in good company, I guess I should see, and I also would like to impart some life wisdom in addition to getting that technical mastery.

**Brian Petersen:** Well, there you have it, folks. This is like the that you need in life you learned in kindergarten... Right here, from Carmen. So awesome.

**Erik St. Martin:** You know, it's interesting too to meet people who have sort of done things in reverse, because like you said, in the tech industry it does feel like a lot of us focus on our careers first, and then family... And usually by the time you have a career, you're all in, and your family, whether you consciously do it or not, becomes secondary, and you don't really get the same valuable time you do when -- you know, kind of pre-career, and you're just focused on your family.

**Carmen Andon:** Well, I have a -- so my Twitter bio... I have stories about it, but one of the stories is it basically says "I can do many things, I'm just most needed in software right now." And the thing I think about in regard to that is that I have a set of life experiences that can be an asset to the community at large, right? So it's not necessarily my coding jobs, but some of the wisdom that I've had to gain in the hard knocks that I've had as a parent with special needs children, as a person who's worked in other industries, a person who has some of these perspectives - that may complement someone who may not have these perspectives because they just don't have as much life under their belts, but maybe really understands coding and whatnot.

\[16:19\] There was a recent blog that I read from a prominent woman in tech that said "Stay in engineering as long as possible, because as a junior engineer you're kind of expendable, you're not really that worth it." My response to that was "Maybe", but I never thought that way. Understanding that I as a "junior engineer" had some very valuable things that I could give to the table, and that more people that have diverse perspectives should and could think that way.

**Brian Petersen:** So changing the subject just a little bit... \[laughter\] Well, that's not a bad thing; I was not moving away from that same general topic... Carmen, you run Women Who Go New York City, or you're a part of Women Who Go New York City and also Ladies who Linux?

**Carmen Andon:** Right. Gosh, these are kind of -- yeah... So Women Who Go NYC was a chapter that I started with Jessica Weinberg at Gopher Con 2015, where I was a scholarship recipient. Since then, I've moved upstate, so I've given most of the admin tasks to Jessica, as well as Jonas. So they're running things over there, and I try my best to get down to the city and participate as much as possible.
And Ladies who Linux as well - it's in New York City, and I'm no longer there, but I try my best to try to help work with the community. I've shifted my efforts to Slack (the Women Who Go Slack) and try to offer remote pairing and remote code reviews for a group of women... So kind of like a remote meetup group.

**Brian Petersen:** That's really cool.

**Carlisle Thompson:** Are you doing this actively, on a regular basis, or is it on a needed basis?

**Carmen Andon:** There are several people who have taken me up on my offer and I work with them individually, in direct messages, but I helped start a black women channel. There was a [picture](https://twitter.com/kelseyhightower/status/885932075303534593) that [Vladimir](https://twitter.com/VladimirVivien) and [Johnny Tourniquet](https://twitter.com/jboursiquot) and [Bryan Lies](https://twitter.com/bryanl) shared widely at the last Gopher Con, which sort of showed several dozen black men together... And it was just such a wonderful thing to show the growth in that particular area of diversity. And then I tweeted, I was like "My goal is to have this same picture but with black women for Gopher Con 2018."

So we started a black women channel, and we couldn't get everyone -- there's so many people in different timezones, with people from European timezones, all the way to California timezones, so a 9-hour time difference... To be able to agree on a single time, so I'm kind of mentoring two or three individually and kinds of doing code reviews with them. But I think right now - I'm just going to say it right now in public - I'm going to revive that and see if we could do something in groups from here until Gopher Con.

**Brian Petersen:** That's awesome.

**Carlisle Thompson:** That is very cool. Very, very cool.

**Brian Petersen:** Speaking of Women Who Go New York City, I was talking with Jonas just the other day, and there is a strong need for speakers at Women Who Go NYC, so if anybody has something great they wanna share, or something you want to learn and teach everyone else, reach out, and I can put you in touch.

**Carmen Andon:** Right on! Thanks for that plug, Brian.

**Brian Petersen:** Hey, I'm here. All day long. So how about the [Go Developer Survey](https://blog.golang.org/survey2017-results)? The survey just came out, and lots of interesting news in there... Was there something that jumped out at you for the developer survey that you thought was unique, or more interesting, or maybe year over year, specifically?

**Carmen Andon:** \[20:06\] Yeah, so the one thing that I always kind of latch onto is this inclusion question. And I think about inclusivity because I have been a person who has maybe internalized that maybe I don't belong. It's really more relevant to people who maybe don't feel like they belong, whether that is true or only perceived... But one of the things I noticed in the Go -- so I was asked by a part of the Go team, because I'm one of the Working Group through Golang... "Hey, can you take a look at the survey and see if there's anything we should modify for the upcoming year?" So I looked at it, and everything looked okay. I didn't at the time see anything that I would change about it.
But when the survey results came out, I kind of took a closer look at the inclusivity question, and I was like "Oh, these are interestingly-worded things... Maybe we could discuss and see if we could reword some of the questions."

I'll give you a little back-story... My son was diagnosed with autism when he was two, and I've talked about this at my Gotham Go keynote, but one of the things that I did to try to understand that was to get a masters in it... And my masters did a lot of work with survey design and analysis. So one of the things that's in surveys is designer bias, whether we like it or not. The perspective of inclusivity in a survey design is by definition you have to decide what is default and what is not default, and why you would identify as an under-represented group, because that was the nature of the question, right?
So last year's survey, or the results of 2016, there were a lot of write-ins. One of the things that surprised me was "objection to the question" as a write-in... And I would love to speak to those 150 individuals and say "Well, what is it that you object to? Do you object to the way that the question was worded? Do you object to the fact that the question was asked at all? Do you object to the fact that maybe there isn't a category, or maybe the way that the multiple-choice was put in?" I would love to speak at length further with them.

The other thing that I thought was interesting was that about 33% to 37% in both years did not answer the question at all. They just skipped it. I guess it wasn't a required thing that you had to choose, right? So I would also love to know - well, that's interesting... One in three gophers didn't want to answer this question; now, what kind of assumptions can I make there? Can I make assumptions that they just didn't think that this was something worthwhile to answer, and why that is? One of the things is "I don't consider that I belong to any under-represented group", whatever that might be; I'm not going to make any assumptions.

So anyway... Those are the two things in the survey in terms of inclusion that I talk about. Because we always see about diversity and inclusion, and I always focus on inclusion, and it's something that's sometimes hard to scale because belonging and inclusion can be intensely personal. I've had talks with people who maybe don't feel included because they feel that they're of older age; I've had conversations about that with some gophers.

Some also are a part of a religious group that cannot drink alcohol or coffee, and so some of our conferences and meetups and events - they feel a little bit left out or there's no alternate for them. So it's things like that we maybe could include, but then again, there's this whole idea of "Okay, well then do we have to -- maybe just allow that write-in, but..."

\[23:58\] Anyway, so I went and I kind of looked at other tech communities. There was the Stack Overflow User Developer Survey. That, of course, gets far more submissions, but one of the things they did that kind of created a stir on Twitter was that they asked the gender question, and they didn't have any options for trans, non-binary or other gender minorities... So then the next year they included that, and that helped those that identify with the non-binary gender feel included. I felt like we didn't have anything like that, and lo and behold, I went, and I looked at the Rust survey, because gosh, how many times over time we think of Go, sometimes we think of other languages, and there's Rust... And for Rust, that was an option to check.

I have some non-binary friends and co-workers, and I kind of said \[unintelligible 00:24:49.13\] I kind of scrubbed the communities as these, and I said, "Which survey design or question do you like better?" and they were like "Well, I don't feel erased in the second one", meaning Rust.

These are just things to think about, and I don't know what the answers are, but I do know that -- the thing that I've talked about is I remember walking into Gopher Con in 2015 to the CoreOS pre-party... Do you remember that, Brian and Erik?

**Erik St. Martin:** Yeah.

**Carmen Andon:** I remember getting there, and walking in, and it was like 400 people in a room, watching [red beard](https://twitter.com/brianredbeard) talk. \[laughter\] And I remember I could count only like five or six other women, maybe ten... And I know that were few women in tech at that point, but this just hit me, and it just -- it was like a visceral emotional reaction, and I remember taking a picture, snapping from the back of the room, and sending it to my husband and saying "Oh my god, look at this..." My husband's reaction kind of gave me the perspective that I needed, which is "Welcome to my world." The reason why that gave me perspective was because my husband is from West Africa, so he is constantly reminded of his otherness, in all the ways, in the United States North-Eastern Academia, as a professor. He's the only black professor in his entire division. So I was like, "Huh, okay..."

I remember when he would take me to Ghana, or he would take me to some places in Brooklyn where his family lives, and I would be the only European, or white -- or I could say I'm Latina, but to them, I'm just white... And I remember, I never thought about my whiteness until I was the only white person in a room. I never think about my womanhood, if you will, until I'm the only one in a room, and these are only just the visible aspects of diversity, right? There's also lots of invisible, whether that's mental, or neurodevelopmental differences, or religious, or other things like that.

So that's kind of the things that just make me very interested and curious when it talks about our community and these axes of inclusion and diversity and whatnot.

**Brian Petersen:** I love that we are 42 minutes into this particular recording, and we've barely talked about Go, and it's still one of the most awesome shows we've ever done.

**Carmen Andon:** Really?

**Brian Petersen:** Oh, absolutely.

**Erik St. Martin:** Oh, yeah.

**Brian Petersen:** I'm awe-struck by your feeling of community, and your dedication to the community and the people around you, and just... Wow.

**Erik St. Martin:** And just your ability to articulate it.

**Brian Petersen:** Yeah.

**Carlisle Thompson:** I'm sitting here in awe, and with a lot of feelings, and not knowing what to say next... Just processing everything you said.

**Brian Petersen:** Yeah, how do you follow that up with light Go news from GitHub? You just don't.

**Carmen Andon:** Yeah, I know... And it's funny, because to me Go is the hard thing, coding is the hard thing, but to many others it's these conversations and topics that are far harder... So that's maybe what I can bring to the table. Yeah, these aren't easy conversations to have, but what I do know is that every person that I've met in the Go community has just been so wonderful.

I've talked to a lot of people, especially about this idea of inclusivity and diversity and what not, and so I would just love to talk more about it, and I do feel that community is super important, and it's what made me finally learn Go. It wasn't the syntax, and it wasn't the small language footprint, or the standard library... It was the people.

**Carlisle Thompson:** \[28:23\] One thing that you said that is hitting me really hard personally, is because like you, I'm Latina, and a woman, obviously, and going through the experience of college in the U.S., and getting a job in tech, it's amazing how much of an outsider you feel when you don't have people who look like you, and not only that, but sort of have the same background as you... It's so disconcerting, and you don't operate at full confidence. And not operating at full confidence shows. So you have to overcompensate somehow, you have to bring yourself up to task, right? And it takes years for you to feel like you're operating, at least to your satisfaction, up to a level of like mostly confident... But still, you're not up there, because when you step into another context where there are people like you, you contrast... Because you can see, "Okay, I am myself. I'm completely confident in this setting", and then you step into a setting where there aren't people like you - you're still operating at a high level of confidence, but you're not fully there.

And of course, it helps to have people who are empathetic to that and maybe can approach and ask questions differently, or whatever it is that people need to do... I don't even know. Maybe somebody can write a manual, I don't know. But it helps to -- for example, in the Go community people always try to think about inclusion, and working on those efforts, so just seeing that helps a lot... But it's hard.

**Carmen Andon:** Indeed.

**Erik St. Martin:** There are so many dimensions to it, too. There's the obvious ones that we're really prioritizing too, but even people just entering the tech field that are self-taught and end up at a company, that are surrounded by people with formal educations and degrees; there's kind of like an outcast feeling there, and then you add another one of these dimensions on top of that, and then it's just kind of a downfall as far as confidence goes.

**Carmen Andon:** Oh, yeah.

**Carlisle Thompson:** Yes, absolutely.

**Carmen Andon:** And socio-economic factors, geographic factors... Right? There's so many, and that's why I still -- you know, inclusivity is personal; it's intensely personal, and so you have to meet it there... And when I've met it there, I've often found more compassion than not, right? So that's what I try to do.

**Brian Petersen:** It's funny how many tiny little things hit in the inclusivity category... We were talking once at a job that I worked at about hiring new people and requiring them to get their own credit card to do personal travel, and that's a huge barrier for some people. Some people haven't had credited their entire life; some people are young, and they just don't have the ability to book thousands of dollars of things on a credit card, because they haven't built credit yet. There are lots of reasons why people might not have their own credit card, and that's a huge barrier to getting your job done if you're required.

**Carmen Andon:** \[32:05\] Good point.

**Brian Petersen:** Company-issued credit cards are a giant enabler for inclusivity, but it's something that people frequently just completely ignore.

**Carmen Andon:** Very good point. Same thing with conferences; I've tweet-stormed about this before, but if they're going to give a diversity of scholarship to a conference -- I mean, I was pretty lucky I got an airfare and I got hotel, but I also had an income from working, and I also had a husband to support me, to watch the kids, and I also could make my own per diem. But there have been people for whom attending any type of conference is a huge burden on them, and it's also a non-possibility...

So thinking about these things when we give scholarships, in addition to a conference fee, in addition to airfare or travel, in addition to hotel or accommodations, are we thinking about these other things? Socio-economic - I think about that often, and that credit card plays right into that, Brian.

**Brian Petersen:** Yeah, it's just one of the tiny things that some people take completely for granted, and others can't.

**Carmen Andon:** Yeah. I used a technical description to what all of this is about, especially when you say, Carlisle, that you over-compensate, and that is, when you look at the systems administrator \[unintelligible 00:33:27.07\] it's called "the people of the default." In a default system you don't need to worry about configuration, but if you were not default, and you were a snowflake server, you're constantly having to compensate by adjusting the configuration, and adjusting and adjusting and adjusting, and that can be like "Ugh..."

But true inclusivity and true diversity is where there is no default, and we all just kind of can -- we don't have to assume a default in another, and no one feels "other", but rather included. I hope that makes sense.

**Brian Petersen:** Very much. So we should -- I mean, it would be sad if we didn't get to talk a little bit about Travis... So tell us about your work and Travis, what you do and how you use Go if you're allowed.

**Carmen Andon:** Sure, yeah. I'm on the build infrastructure team. I'm one of the junior... Furthermore, I don't know, we don't use that language, so I'll stay away from it, but we basically -- if you've ever used Travis, whether you pay for it or you use it as part of your open source projects on GitHub, we try to give you an environment in Linux and Mac that's going to be a clean slate every time and help you run your tests, and every time you push a commit or push a PR, you can be confident that that won't break the build when you finally deploy it to production (so hosted CI). And the part that we work on is the build environment and also the infrastructures that the build environment run on.
So there's platform, and then there's build infrastructure engineering. I'm one of the people in the build infrastructure engineering.

The thing that I work on is the Mac -- recently; I used to work on the Linux part of things, but now I work on the Mac infrastructure, and the Mac is a special beast, if you will, because -- I can go on and on about it in terms of the engineering that's involved. Brad Fitzpatrick does a somewhat similar thing to what I do at scale, but just for Golang... Sort of running the binaries of all the Go runtime versions for the Darwin architecture.

So we do that at scale, and we use quite a bit of Go microservices to do that within the infrastructure, and a lot of the Go microservices help mediate, or are levels of abstraction to mediate between the worker or the agent that runs the builds, and the hypervisor that we have to use, which is sphere's VMware.

\[35:58\] And the reason why we use sphere... "Oh, why are you using sphere? Why don't you just use Docker?" We get that a lot in issues... It's because when you have Mac - OS X or macOS, if you will, you have to run it by licensed-on-Mac servers; you can't run it on Linux servers, and so all the wonderful container ecosystem that we have is no longer available to you, so you have to get really creative... And sometimes it's frustrating because you can kind of see where Linux is kind of evolving in this space (the container ecosystem) - I know Brian and Erik work directly on this Azure with \[unintelligible 00:36:36.13\] So having to mediate that with multiple microservices and the sphere API is a lot of what we try to do in our day-to-days for the Mac infrastructure.

And our worker agent, which is the largest codebase at Travis, if you will, or the largest kind of one-service, that's very mission-critical, is also written in Go, and all the back-ends for Docker and for GCE, all the different clouds, as well as our Mac cloud is written in Go.

**Brian Petersen:** That's awesome. So to clarify, when you run sphere, are you running it on Mac hardware?

**Carmen Andon:** Yeah.

**Brian Petersen:** Wow...

**Carmen Andon:** It has to be, yeah. There's a new product coming out that we may try some day. It's KVM. Developers that left to try to develop a KVM like thing for Mac hardware, which would be awesome, and it would really help out the CI the ecosystem for infrastructure in Mac.

**Brian Petersen:** Which product is that?

**Carmen Andon:** That's called Anna and Veered. We'll see where that goes, and we're gonna play around with it and see if that's something that would be viable, and then we could put it on Kubernetes and have one back-end to rule them all.

**Brian Petersen:** I've used Veered back when -- it was probably a little over a year and a half ago... Veered was a paid app on the Mac App Store, and then they pulled it and made it open source and kind of abandoned it, and moved over to [Anna](https://ankadoc.bitbucket.io/), which is their commercial version of it. But yeah, Veered was a perfect emulator, based on the have port of Have in BSD, which does virtualization at the KVM level.

**Carmen Andon:** Right... Okay. So the same developers I think decided to kind of expand that and make that more enterprise.

**Brian Petersen:** That's awesome. Really cool. The Veered app was really fast. It was much faster than Parallels and VMware at the time... But the last time I tried it, months ago, it was missing some updates that made it work well. So I think they've kind of left Veered alone while they were working on the Anna thing. But that's good for you... Not for me.

**Carmen Andon:** Yeah, we're watching it, and we'll see what comes of it this year.

**Brian Petersen:** That's really cool.

**Erik St. Martin:** So in the docs that we were sharing you mentioned that you kind of have a love for visual abstractions, and kind of had some examples of things that you found particularly exciting.

**Carmen Andon:** Yeah... Yeah, so that's one of the things that sort of was a barrier to my learning. People may debunk this or not, but we have a great capacity for visual learning, and I've read books about this... If you think about all the things that we use in terms of language surrounding computer abstraction, it's languages that are tangible things: trees, graphs, what have you... So I just love the idea of asking people this wonderful German word call Hopkins - "your head cinema", so what goes in your mental cinema when you're talking about an abstracting thing.

\[40:13\] At the last Gopher Con I asked a bunch of people this, and I found some lovely, curious answers that helped me dig and want to go and learn and find out more... But the one that really stuck with me is Rick Hudson -- for the Go community, they probably already knew this, but I will introduce him... [Rick Hudson](https://www.youtube.com/watch?v=aiv1JOfMjm0) is one of the primary developers and architects of the garbage collector in Golang, and especially was the one that kind of completely redid and improved the 1.5 garbage collector.

So I asked Rick - not expecting this answer at all, but I asked Rick, "Rick, what do you see in your Hopkins (mind cinema) when you think of the garbage collector?" When I asked other people, they would take some time to think, and sometimes they would say something like "I don't know, whatever...", but Rick was ready with an answer, and he said "A chessboard." And I went, "Tell me more!" and he basically went on to say "When I was a young kid, I learned chess as different, discrete pieces that had limitations in movement on a grid." And when you think about a garbage collector, that really could help you, because different operations in different phases in the garbage collector move along the heap up and down differently, right? So you kind of can look at the heap as maybe a single-column chess piece, if you will, or maybe multiple columns, depending on how many actors you have, right? But you have multiple actors and multiple things moving down a data structure of the heap.

I'm telling you all this not knowing what I knew then -- oh, sorry, what I know now. I'm telling you all of this because just hearing that from Rick, hearing that it was a chessboard, made me want to go learn more about the garbage collector, learn about its implementation, and learn just about garbage collection in general. It was like unlocking a beautiful thing for me. If I see Rick at this year's Gopher Con, I'm just going to hang out and speak with him all day, because I think he's just -- you know, he's got such a history prior to joining Google, at running workload \[unintelligible 00:42:15.01\] but Rick is in his fifth decade of work, and just the wisdom that he can give us... So anyway, that was one of the things that really surprised me.

The other thing in terms of like visual abstraction - I was speaking with Alan Donovan. Alan Donovan works at the Go team in New York City, and I was kind of asked to give a talk at Rubicon about the [Why of Go](https://www.infoq.com/presentations/go-concurrency-gc), and I was asked rather last-minute, so I was kind of like worrying a little bit, and I was like "What should I talk about?" He said, "Oh, you should talk about memory locality, it's so important." I was like "Tell me more", because I just had a fuzzy idea of what memory locality was... But he went on to talk about how memory locality is way better than when Java invented it like 20–25 years ago.

You think about memory locality, and he would talk about it in geospatial terms, in geography. So it used to be just a field, a small, relatively flat Kansas filed; but now you look at memory locality, and it's like a Swiss mountain, with a village down at the bottom, and then a summit at the top and all these levels. And when you have to make calls to different parts of memory, it's like having to travel on foot, either all the way down to the village, depending on how you've coded it, or being better about memory locality and just going 100 feet down the mountain on foot or 100 feet up.

So just hearing about that helped me really \[unintelligible 00:43:49.21\] and understand data types, true value types, structs and things in Go, and why memory locality was so important for Go, and why even the people working on optimizing for that in the Go team - why that was important. I needed metaphors and something tangible to be able to relate to grow my mental model of that, my Hopkins of that.

\[44:13\] So those are two of the main, most delightful ones I heard. I've heard many more, but those are two of the ones that I really enjoyed, and that have helped me kind of frame my way of looking and thinking about those two very hard things.

**Brian Petersen:** Wow. I'm really glad that somebody thinks about those really hard things, because they're things that I don't want to think about. I want to think about solving problems and getting things done, and I'm really grateful for the people who are visualizing chessboards and mountains, because I don't have to.

**Carmen Andon:** Yeah, yeah. And that's probably one of the things that kind of -- yeah, there's probably a barrier to why I haven't learned languages before. I remember caring about -- in C, what is \#include Lt;studio.HGT;? Why do we need that? Why do we need void? Instead of just having to ignore it and just push through and then maybe go to learn it later, I wanted to know every single thing sequentially, and dive into these dev holes, and sometimes that meant that I wasn't staying on the path... But I am who I am, and I really like talking about such things.

**Brian Petersen:** You've got to embrace that, you have to. The thing that I love about technology and learning and doing things is connecting things that really don't belong connected together... And I've found some of the most fun projects I've ever done have been bringing two projects that have nothing to do with each other, no really any business belonging together, and putting them together and seeing what happens. It's tons of fun. That's my thing. I get that, I know it, I love it.

**Carmen Andon:** Very cool.

**Brian Petersen:** Sometimes it's peanut butter and chocolate, and sometimes it's peanut butter and pineapples.

**Carmen Andon:** Hm, I'll have to try the pineapple/peanut butter one.

**Brian Petersen:** Let me know how it goes. \[laughter\]

**Carlisle Thompson:** Okay, ice-cream on toast.

**Carmen Andon:** Ice-cream on toast... I'll try it.

**Carlisle Thompson:** It's awesome.

**Erik St. Martin:** My mother had an uncle that used to put ketchup on ice-cream.

**Carmen Andon:** Well, I'm hoping out of that one... \[laughs\]

**Erik St. Martin:** Yeah, that's a little far. And speaking of visualization, a lot of people learn better by kind of seeing things visualized out, rather than kind of reading words and trying to come up with our own mental visualization of it... And a really cool one from two years ago at Gopher Con - Ivan Dangling did one on [visualizing concurrency in Go](https://www.youtube.com/watch?v=KyuFeiG3Y60).

**Brian Petersen:** Oh, yes...!

**Carmen Andon:** Yes, my favourite talk.

**Brian Petersen:** Epic.

**Carmen Andon:** Mm-hm.

**Brian Petersen:** It's out on YouTube. If you haven't seen it yet, it is well worth the time to watch that. It was so cool, watching the go routines fly across the screen with visualizations, it was amazing. Oh look, somebody just dropped a link in Slack. Good job, Erik!

**Carmen Andon:** Right on. Yeah, it helped me understand fan-out/fan-in worker patterns, and all the other well versed patterns for concurrency. That was like "Oh, so that's what that is...!" It was amazing.

**Brian Petersen:** "Oh, that...!" Well, this is just the best conversation ever, but the clock is ticking, so we should probably move on to Go projects and news, unless there's something anybody else wants to get in real quick...?

**Carlisle Thompson:** That's crazy, how did it end so fast? \[laughter\]

**Erik St. Martin:** Right...?

**Brian Petersen:** Just like the best movies ever - they end, and you don't even notice it.

**Carlisle Thompson:** This makes no sense.

**Carmen Andon:** Time flies when you're having a lovely conversation.

**Carlisle Thompson:** Yes.

**Brian Petersen:** So who wants to kick us off with some interesting news?

**Erik St. Martin:** \[48:06\] As far as interesting news, I don't know whether there's been anything news-wise that I recall the last week; there have been some interesting projects that I've found...

**Brian Petersen:** Fire them up, let's see.

**Erik St. Martin:** So the first one is from the Google Cloud platform on GitHub, and it's called [Scaffold](https://github.com/GoogleCloudPlatform/skaffold). It looks like a way to be able to build and deploy your applications that you're developing locally... I haven't dug too far deep into it, but it looks like it might be akin to [Draft](https://draft.sh/).

**Brian Petersen:** That was the impression I got. It was Draft without a server-side component, without a cluster side piece...

**Erik St. Martin:** And if anybody has actually had a chance to play with this, I'd love to talk to them, because I don't know whether I'll have time to set it up and play with it, but I'd love to hear feedback from anybody who has.

**Brian Petersen:** Yeah, +1 on that. So my big find of the week - oh, my gosh, I'm such a geek... [Slack-Term](https://github.com/erroneousboat/slack-term). So awesome being in Slack, in the terminal... Very nice. Much less memory used than the Electron client.

**Carmen Andon:** Oh, I'm hearing infinite echoes.

**Brian Petersen:** That was really cool, we should do that again. \[laughter\] "Much less memory used..."

**Carlisle Thompson:** That was really cool.

**Carmen Andon:** \[laughs\] Oh my god, there's so much echo right now...

**Erik St. Martin:** So as we know, I love security stuff, and I've found two cool projects from the security standpoint, and I think it's really awesome to see the infosec community adopting Go a lot more, too. One is called [Amass](https://github.com/caffix/amass). It's for doing subdomain enumeration, to be able to kind of brute force subdomains, and it's supposed to have a little bit of machine learning to guess, and it goes out to multiple public DNS servers, so that all the DNS queries aren't coming from a single IP address.

The other one I found is one called [Better cap](https://github.com/bettercap/bettercap). This looks like a -- they call it a Swiss army knife library, but it's a lot of networking stuff, so you can kind of... You can snoop Bluetooth low energy packets and Wi-Fi beacon frames, and do different types of stuff: ARP. Spoofing, DNS. Spoofing, all that good stuff... And it looks pretty slick.

**Brian Petersen:** I don't know, you've just said a bunch of things that made absolutely no sense to me, but yeah, you go with your bad self.

**Erik St. Martin:** \[laughs\]

**Brian Petersen:** Spoof this. So @jessfraz released [IMG](https://github.com/genuinetools/img), which must be one of the coolest projects out there I've seen in a long time. It's a standalone, daemon-less, unprivileged Dockerfile and OCI compatible container image builder... And that's a lot of buzzwords and hypes all in one, but the important part is that it's unprivileged Docker builder, so you can build Docker containers without being root and without having a Docker daemon running as root... And if you translate that a little bit farther up the chain, it means you could have Docker builders running in your Kubernetes cluster, or somewhere else on the network for you, unprivileged, and that's just going to be epic. That's going to be really cool.

**Erik St. Martin:** \[52:03\] Another cool project - the GitHub username is Brice; I don't know whether that's pronounced a different way, but the project is called [German](https://github.com/bcicen/grmon). It is a really cool way to visualize go routines live. It shows you all your go routines, the state that they're in, whether they're blocking in a select or receive, making miscalls, things like that.

**Brian Petersen:** Shut up, that's awesome! Look at the picture!

**Carmen Andon:** Oh, wow...

**Brian Petersen:** Too bad this is radio, because that picture is amazing. It's like top for your go routines.

**Erik St. Martin:** Yeah, it's pretty slick...

**Brian Petersen:** Wow... I'm impressed. That is super cool. Big, fat GitHub star on that. Nice one.

**Erik St. Martin:** Another new project from Peter Bourbon is [Casinos](https://github.com/peterbourgon/caspaxos). It's still kind of in its early phases, but he seems to be trying to implement that replicated state machine white paper, and it's supposed to not have leadership election, and things like that.

**Brian Petersen:** And no logs; no log replication with that either, right?

**Erik St. Martin:** Right.

**Brian Petersen:** I haven't read the paper, but I do read Twitter... And I play one on TV.

**Erik St. Martin:** Another cool one is if you want to learn the guts of stuff; I'll link this in the show notes and in Slack for anybody listening now... I came across a primer on the intermediate language that Go uses; it's essentially the Assembly language that the Go compiler outputs, and kind of understanding that. That's super cool. I haven't made it all the way through, but I did start reading through it.

**Brian Petersen:** That looks really cool, too.

**Erik St. Martin:** And then lastly - this is an article that I found on dev.to. There's this company that has released some games in Go. They've listed a couple of their names - Clock of Atonement and Bluebird of Happiness. But the interesting part about it is they list out all the OpenGL wrappers and MP3 libraries and things like that they used to create their games. So if you want to play around with doing some game development in Go, that's probably not a bad place to start.

**Brian Petersen:** Very cool. I'm still looking at the German thing, sorry. You lost me with the pretty visualizations of my go routines. In two more minutes I'm going to be compiling something and looking at the go routines as they work. You know what we should do? Oh my god, you guys... Oh, my god. Alright, the first person who instruments the Go tool itself with German and puts a video of it running up on YouTube or a blog gets a hand-knitted hat. I've got to see the Go tool itself, instrumented with German, running a Go installation or a compiled, something large enough where it actually makes sense; that would be really cool. You get a custom, hand-knitted Brian Petersen hat, which as we all know, has an unmeasurable intrinsic value.

**Carmen Andon:** Priceless!

**Brian Petersen:** Exactly. Carmen, are you on my hat list?

**Carmen Andon:** Now I am.

**Brian Petersen:** You are now...?

**Carmen Andon:** Right? Right, Brian?

**Brian Petersen:** What colours do you prefer?

**Carmen Andon:** Surprise me.

**Brian Petersen:** I'll pull up my Trello right now. It's huge, though. There's like 45 hats in the backlog...

**Carmen Andon:** Get in line... Sure. I'm fine like that.

**Brian Petersen:** Okay. Alright, you're in.

**Erik St. Martin:** \[55:46\] And I didn't have any more projects, but one news item we did skip over is that the Gopher Con CFP closes in one week. So if you would like a shot at speaking at Gopher Con, now is the time, all you slackers...

**Brian Petersen:** All you slackers... \[laughs\] Not slackers, these are the people who are being very thoughtful about their approach to submitting a CFP. They're not slackers, Eric.

**Erik St. Martin:** Some of them are slackers...

**Brian Petersen:** They're deliberate. You need to use better inclusive language. They're deliberate.

**Carmen Andon:** I would also like to mention that if you go to the golang.org site for speaker help, there are quite a few volunteers that will help you soundboard your CFP and prepare your CFP for submission, so... Make use of them if you want.

**Brian Petersen:** Yes.

**Erik St. Martin:** Yeah, and a couple of us on there are part of the CFP review committee for Gopher Con. We do have enough people on our review team that if you approach only one of them, they will just avoid ranking your talk, and it will get rated by the other 14 people.

**Brian Petersen:** We've got a lot of people.

**Carmen Andon:** The same kind of thing, yeah.

**Erik St. Martin:** Yeah, and they do the same thing if they submitted a proposal. They just don't review their own.

**Brian Petersen:** Yeah. In a legal world, we'd call that recusing yourself, but apparently that doesn't mean anything anymore, so... \[laughter\] Come to Go Time for the Go, stay for the politics.

**Carmen Andon:** For the legalese...

**Brian Petersen:** \[laughs\] Alright, should we skip \#FreeSoftwareFriday? Because we are way overtime now... Or do you want to sneak some in?

**Erik St. Martin:** I'm okay with skipping it this week. I don't think I have anything that I can think of off the top of my head this week.

**Brian Petersen:** Okay.

**Erik St. Martin:** Anything else anybody wanted to mention before we wrap the show up? I will take that as a no. Thanks so much for coming on the show, Carmen. It's been a blast, and eye-opening.

**Carmen Andon:** Thanks for having me.

**Erik St. Martin:** Thanks everybody else for being on the show, thank you to all of our listeners. You can find us on Twitter @GoTimeFM. If you want to be on the show, you have suggestions for guests or topics, file an issue on github.com/gotimefm/ping, and with that, goodbye everybody. We'll see you next week.

**Brian Petersen:** Goodbye, Carmen. Awesome show, thank you.

**Carmen Andon:** Thanks! Bye, everyone.

**Carlisle Thompson:** Bye! Thank you, Carmen.
