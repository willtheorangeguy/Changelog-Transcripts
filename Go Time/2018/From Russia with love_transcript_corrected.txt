**Erik St. Martin:** Welcome back, everybody, to another episode of Go Time. Today's episode is number 70. Today on the show we have myself, Erik St. Martin, Carlisle Pinto...

**Carlisle Thompson:** Hi, everybody.

**Erik St. Martin:** Brian Petersen...

**Brian Petersen:** Hello!

**Erik St. Martin:** And he's knitting...

**Brian Petersen:** Hey...!

**Erik St. Martin:** And our special guest for today is one of the organizers of Gopher Con Russia, Leo Kales.

**Leonid Kales:** Hello.

**Erik St. Martin:** Do you want to give the listeners maybe just a brief history of you and what you do, and the length of time you've been in the Go community?

**Leonid Kales:** Okay. I used to be a Go developer two years ago, and after that I started my developer relations work. Now I work at Data Art, as chief community manager. Also, my story about community started three years ago, when I started the first community in Novosibirsk, in far, far away Siberia, probably in the middle of nowhere. I built it from scratch. Do you know Yandex?

**Brian Petersen:** Yes.

**Leonid Kales:** The Russian Google, yeah. So our first meeting was in their office, and we had about 100 people there.

**Brian Petersen:** Nice, that's huge. How big is Novosibirsk in terms of people?

**Leonid Kales:** It's more than 1.5 million people there.

**Brian Petersen:** Wow...!

**Leonid Kales:** It's the third city in terms of population in Russia.

**Brian Petersen:** Okay.

**Leonid Kales:** Yeah. After that I started to work on different technical communities in Novosibirsk, so now I lead the Google developer group there, and we have several series of technical meetups - we have meetups about Golang, we have meetups about Android, we have meetups about DevOps, and so on. Also, we have one big conference there called [Deafest Siberia](https://gdg-siberia.com/). We started to organize this conference probably two years ago. We even had [Dave Cheney](https://twitter.com/davecheney) last year... In Siberia, can you imagine that? \[laughter\]

**Carlisle Thompson:** I can't imagine anybody in Siberia... It's so far and so cold.

**Brian Petersen:** Can you tell us a little bit about Siberia? Because in America the only thing that most people know about Siberia is that it's where people get sent for punishment, and I don't think that's accurate. Can you tell us what Siberia is really like? Is it really always cold?

**Carlisle Thompson:** Yeah, exactly. I need to know that.

**Leonid Kales:** No, it's not always cold. In the summer we have temperatures like 30 Celsius degrees.

**Brian Petersen:** That's hot.

**Leonid Kales:** Right now it's about -12, I think.

**Brian Petersen:** And that's cold.

**Leonid Kales:** Yeah.

**Brian Petersen:** That's very cold.

**Leonid Kales:** But you know, right now I'm in St. Petersburg - I moved from Novosibirsk last year - and today in St. Petersburg it's -20 Celsius degrees.

**Brian Petersen:** \[04:12\] Wow. Now, St. Petersburg is on the Western side of Russia, right?

**Leonid Kales:** Yeah, right.

**Brian Petersen:** Okay.

**Carlisle Thompson:** I just wanted to clarify, -20 Celsius is -4 Fahrenheit, and 30 degrees Celsius is 86 degrees Fahrenheit... So that's not bad. But is it like for a day, or is like for the whole summer?

**Leonid Kales:** It's for the day.

**Carlisle Thompson:** One day of the summer is hot, and the other days are cold?

**Leonid Kales:** Oh, no, no, no. In Novosibirsk, it's quite usual weather in the summer.

**Carlisle Thompson:** Okay. \[laughs\] Just to clarify.

**Brian Petersen:** That sounds like a nice, normal climate.

**Carlisle Thompson:** Yeah.

**Brian Petersen:** Good.

**Leonid Kales:** Yeah. Also, in Novosibirsk we have a lot of research institutes - more than 30, I think - and all of them are located in a special place called [Akademgorodok](https://en.wikipedia.org/wiki/Akademgorodok). It's a very scientific place.

**Brian Petersen:** It sounds very awesome, it sounds like a technical centre of awesomeness.

**Carlisle Thompson:** Well, I can't imagine anything that you said to be truthful... Starting with you got 100 people to show up at your first meetup - it's amazing!

**Erik St. Martin:** That's wild. Most meetups never get that big.

**Brian Petersen:** That is good!

**Carlisle Thompson:** Yeah, so now I'm triply glad that you're here, because you're going to -- I'm just looking forward to knowing more about Siberia, and the community there... It sounds really exciting.

**Erik St. Martin:** Is there generally quite a few Go developers in that area? Is Go a really popular language for a lot of companies there?

**Leonid Kales:** Yes, right now we have a lot of companies that use Go in production, but three years ago there were few companies there. Maybe one, or two. It was very hard to track all these people. Most of them were just interested in the topic; we probably had only ten Go developers there in the audience.

**Brian Petersen:** Wow. So you did a great job.

**Carlisle Thompson:** Yeah, absolutely. I'm curious - when people decide they want to learn Go in your community... Tell me again, when was this first meetup you had? Do people go to meetups, do they get together? Do they have workshops? What are the resources available to them? Because here in the U.S. - and even in Europe - there are conferences, there's the Slack accounts... Are people on Slack? Do you have your own Russian Slack communication? How do you connect to each other?

**Leonid Kales:** We have Russian-speaking Gopher Slack, with more than 2,000 people, I think.

**Carlisle Thompson:** Oh, that's cool.

**Leonid Kales:** Also, we have our own Russian-speaking podcast called [Golang Show](http://golangshow.com/)... And we will be happy to record an episode with Brian, in Moscow.

**Brian Petersen:** Yay!

**Leonid Kales:** Quite soon.

**Brian Petersen:** Very soon.

**Leonid Kales:** I'll be prepared.

**Brian Petersen:** And that's going to be big, because I'm going to announce a huge secret in my talk in Moscow. Huge.

**Carlisle Thompson:** What is the secret?

**Brian Petersen:** Well, it's a secret, I can't tell you. Nice try, though.

**Carlisle Thompson:** Thank you.

**Brian Petersen:** But it's huge.

**Erik St. Martin:** It's just the two of us right here... \[laughter\] Nobody will ever know.

**Leonid Kales:** \[07:59\] Yeah, also we have -- do you know Telegram?

**Carlisle Thompson:** Yeah.

**Brian Petersen:** Yes.

**Leonid Kales:** We also have two chats there.

**Carlisle Thompson:** That's a phone app, for people who don't know.

**Leonid Kales:** Yeah, it's like WhatsApp, but much better. \[laughter\]

**Brian Petersen:** Old people like me -- I don't know what that is. I'm still trying to figure out Instagram. \[laughter\] That's what I call it, just to make my daughter mad. "Are you playing on Instagram again?" "Shut up, dad..." \[laughter\]

**Leonid Kales:** By the way, we tried to organize [Gopher Con Russia](https://www.gophercon-russia.ru/) last year, but we weren't good enough, so it's our second try.

**Brian Petersen:** Well, it's going to be awesome this year.

**Leonid Kales:** Yeah, I think so, because we have right now more than 400 sign-ups for the conference.

**Brian Petersen:** Wow...

**Leonid Kales:** Yeah, and we have 20 amazing speakers.

**Brian Petersen:** I was looking at the speaker list yesterday, and you have perfect speakers lined up.

**Erik St. Martin:** Yeah, there are a number of great speakers there.

**Brian Petersen:** And half of Microsoft. \[laughter\]

**Leonid Kales:** Yeah.

**Erik St. Martin:** The question is though, how many of them were on there before they were at Microsoft? Because most of us have gravitated there only in the recent months.

**Brian Petersen:** That's true.

**Leonid Kales:** Yeah, that's true. By the way, we invited Ashley to our Siberian conference last year... \[laughs\] But we had some problems with business tickets to Russia, because the cost was too high.

**Brian Petersen:** It is very expensive. I just bought my plane tickets, and I could buy a car for how much I spent on my plane tickets.

**Leonid Kales:** Well, that's... Wow.

**Brian Petersen:** It's a good thing I didn't pay for them. I took it out of Erik's budget.

**Erik St. Martin:** \[laughs\] Are you trying to say I don't travel enough?

**Brian Petersen:** No, I'm trying to say that you're not getting a raise this year because I'm going to Russia. \[laughter\]

**Erik St. Martin:** You better make sure he has a good trip!

**Brian Petersen:** So this is going to be the first Gopher Con Russia... Tell us about the venue. What kind of building is it going to be held in? It's in Moscow, right?

**Leonid Kales:** Yes, obviously it's in Moscow.

**Brian Petersen:** Is it going to be in the Kremlin?

**Leonid Kales:** Not for sure... \[laughs\]

**Brian Petersen:** No?

**Leonid Kales:** No... Gophers are not allowed there.

**Brian Petersen:** No gophers allowed in the Kremlin... I'm going to try to find out if it's okay for gophers to go to the Kremlin and go inside. Because it's what I do. I have to break rules. So if I don't make it home, you guys understand why. I'm in jail, in Siberia.

**Leonid Kales:** \[laughs\] By the way, if you will have enough time, we can go to St. Petersburg, before or after the conference.

**Brian Petersen:** Oh, nice.

**Leonid Kales:** We can organize a local meetup if you want. So the venue will be in Moscow, it's called [Technologies](https://en.wikipedia.org/wiki/Technopolis_Moscow). It's quite a big, huge, comfortable conference hall. Nothing very special, but it's quite a nice place. I guess I was there for one conference before, and I like it.

**Brian Petersen:** Any place is special if it's full of gophers. That makes it special.

**Leonid Kales:** Yeah, definitely. And we will have a lot of gophers there.

**Brian Petersen:** I am so excited. So you said 400 people are coming this time? You sold 400 tickets?

**Leonid Kales:** Yeah, even more than 400.

**Brian Petersen:** \[12:01\] Oh, that's good. That's great for a first conference. Well done!

**Carlisle Thompson:** That is excellent, yeah.

**Leonid Kales:** Yeah. And if you want, I can tell you some numbers about Moscow gophers community.

**Brian Petersen:** Yes, sure.

**Carlisle Thompson:** Absolutely, yeah.

**Leonid Kales:** Let me check my notes. Oh, by the way, we also have a mailing list for the Russian-speaking community since 2010. The first Moscow meetup was five years ago, and they had 27 people there.

**Brian Petersen:** Wow.

**Carlisle Thompson:** Yeah, impressive.

**Leonid Kales:** Yup, so that's the history of Russia Gophers community. Also, we have quite a big community in St. Petersburg, about 700 gophers there. I'm not sure the community is very active, but still, we have it.

**Brian Petersen:** But they will be active now that you're there.

**Leonid Kales:** Yeah.

**Carlisle Thompson:** Before I forget - it doesn't have to be right now, but I want to make sure that you give us the link to at least some of the meetups you know, and link to how people can get an invitation to your Gopher Slack account... Also, another thing that I wanted to ask - is there any general Twitter account that people can follow, or Facebook groups, and information for how to get on Telegram? So we can have it for posterity on the show notes, okay?

**Leonid Kales:** Okay, sure. I will send it.

**Carlisle Thompson:** And another thing that I wanted to ask, along those lines - is there any dedicated place for people to look for Go jobs in Russia, or in your area?

**Brian Petersen:** Good question.

**Leonid Kales:** Well, we have a special website called Headhunter in Russia, and you can find any jobs there. It's the first source, I guess, and the special places are our Gopher Slack, we have a special channel there for job offers... And we have also a channel in Telegram for that.

**Carlisle Thompson:** Cool.

**Brian Petersen:** Very nice. So it sounds like the Go community in Russia is incredibly well organized; probably better organized than the one here. That's good news.

**Leonid Kales:** I really enjoyed the gophers' community in San Francisco. I went to some meetups there.

**Brian Petersen:** Oh, it is a good community there, that's true.

**Leonid Kales:** Also, I'm going to the Google I/O this year in May, so we can meet there, too.

**Brian Petersen:** Are you going to come to Microsoft Build, too?

**Leonid Kales:** If you can invite me, for sure.

**Brian Petersen:** Well, I'll work on that then. Very good. I think that's also in May. Maybe you could just make it a big, long trip.

**Leonid Kales:** Yup, why not. Because I can work totally remotely, so...

**Brian Petersen:** Perfect. Working remotely is the best kind of working.

**Leonid Kales:** Yeah, definitely.

**Brian Petersen:** So what sort of big companies outside [Yandex](https://en.wikipedia.org/wiki/Yandex) use Go in Russia?

**Leonid Kales:** For sure, one of the biggest is [Mail Ru Group](https://en.wikipedia.org/wiki/Mail. Ru). Do you know the social network [VKontakte (VK)](https://en.wikipedia.org/wiki/VKontakte)? It's like the Russia Facebook. They use Go in some of their backend services. And actually, there are a lot of smaller companies that use Go in their production also. I can mention [Vito](https://en.wikipedia.org/wiki/Avito.ru). It's like a Russian eBay, but a bit smaller than eBay, for sure. They also use Go in their backend services. That's the most well-known, I think. And not Russian, but Russian-speaking - the guys from Get, from Minsk... Do you know a company called [Juno](https://gett.com/juno/)? It's like Get in New York -- it's not like, it's Get in New York. So yeah, they have a lot of stuff in Go.

**Brian Petersen:** \[16:36\] Nice.

**Leonid Kales:** Yeah, they're very nice folks.

**Carlisle Thompson:** I just went to the Golang wiki page, and there is a page called [Go users](https://github.com/golang/go/wiki/GoUsers) that lists companies from around the world, and it's divided up by continent and then countries, and there are only two companies under Russia, so that definitely needs to be updated. What's there right now is Tools and Postman.

**Leonid Kales:** Yeah. By the way, Tools - we have a speaker from there. Yeah, I think we should update this list.

**Brian Petersen:** Nice. So are there any talks that you're particularly excited about for Gopher Con Russia? Any talks that look amazing? I know you can't pick any favourites, but there's got to be something that you're excited to watch.

**Leonid Kales:** Personally, I'm very excited to meet [Dmitry Yukon](https://twitter.com/dvyukov) in person, and to listen to his talk.

**Brian Petersen:** He's my hero.

**Leonid Kales:** Yeah, same to me.

**Brian Petersen:** I have a perfect Dmitry Yukon story. Erik, I don't know if you were there, you may remember this. At Gopher Con 2015 or 2014 - it was several years ago - Dmitry was a speaker, but I hadn't met him yet because he was going to speak on the second day, and it was the first day... So we were walking home from the pre-party, or walking home from the place where we were having beer the first night, and I had been talking to Dmitry by email forever, on Twitter, and I just told him what a big fan I was and how excited I was to meet him... So I'm walking home, and this really tall person walks up next to me and says "Hi." I had no idea who it was, so I said "Hi", and he kept trying to bring up conversation points, but I was tired, and I had two beers, and I was not talking well.

Then somebody else walked up and said "Oh, hi Dmitry!" It was Dmitry Yukon, and I felt like an a--hole. So there's my Dmitry Yukon story. Sorry, Dmitry. I was his biggest fan, and I didn't even recognize him.

**Erik St. Martin:** Knowing people from the internet is hard, though. Most of us have avatars that are not use, and even in person people look different from their avatar... I think that's an honest mistake.

**Brian Petersen:** It was. I still felt bad... I mean, this is the guy that made Go twice as fast in Go 1.4, or 1.5, or whatever it was... And then added all of that awesome race detection, and the profiler... He's a serious hero in the Go community. When I meet him in March again, I won't make that mistake.

**Carlisle Thompson:** So what would you like to have in your community? What sort of support, or access, or resource would you like to have in your Go community that you don't have right now?

**Leonid Kales:** Wow, so... If you are speaking about far, far away Siberia, I will be happier if more speakers will come to visit us and talk to our gophers in person. Maybe this is the most important point for us.

**Carlisle Thompson:** \[20:14\] Do you mean at your meetup?

**Leonid Kales:** For example, we can use Deafest Siberia as a place to meet. Yeah, because it's quite huge land, we have more than 700 people there... So it's quite reasonable to come to Siberia to talk to this audience.

**Carlisle Thompson:** Yeah.

**Brian Petersen:** Does Deafest happen in the same time every year?

**Leonid Kales:** Yes, I think it's always in autumn. This year it will be at the end of November, and last year it was in September... So quite close to the same dates.

**Brian Petersen:** Leo, I can't understand why you would have a hard time convincing anybody to come to Siberia in November. \[laughter\]

**Leonid Kales:** Because now it's a true Siberian experience.

**Brian Petersen:** \[laughs\] Snowshoes, and dog sleds...

**Leonid Kales:** \[laughs\] We had a guy from Brazil, it was his first time he saw snow. He was so happy... And our first time, the weather was -40 Celsius degrees, so a really true Siberian experience.

**Brian Petersen:** Oh, gosh...

**Leonid Kales:** And we have speakers from 12 different countries.

**Carlisle Thompson:** It truly must be an experience... Even for people who have seen snow, it must be so different. I can't even imagine. I would love to go.

**Leonid Kales:** Yeah, we can talk about that later.

**Brian Petersen:** Let's go, Carlisle. You and me - we're going to Deafest in November, in Siberia. Let's do it.

**Carlisle Thompson:** Let's do it, Brian. Let's plan. Oh my gosh, I need to --

**Brian Petersen:** I need to knit more hats.

**Leonid Kales:** We can plan everything in May.

**Brian Petersen:** Okay, it's a plan. So what has been the hardest part about organizing a conference for you? What's been really difficult?

**Leonid Kales:** To keep everything in mind, probably, the past dates, because... Yeah, usually something goes wrong at the end, you know?

**Brian Petersen:** Always something goes wrong.

**Leonid Kales:** Yeah, right. But I really enjoy to work on community-driven events, because they're quite different from commercial-based conferences. When I relocated to St. Petersburg I found that there are a lot of cool conferences in Moscow and in St. Petersburg, but they are pretty expensive for the developers. They cost like maybe $500 for a ticket. It's quite a high price... Even a one-day conference. I'm very proud that we have Gopher Con Russia as a community-driven event.

**Brian Petersen:** That's excellent. It's the community that makes Go amazing... Everywhere around the world, it's the community.

**Leonid Kales:** Yeah.

**Carlisle Thompson:** Absolutely.

**Leonid Kales:** By the way, I think Go communities are the most friendly communities I've ever seen.

**Brian Petersen:** I agree.

**Carlisle Thompson:** I hear that all the time.

**Brian Petersen:** So how many organizers are there for Gopher Con Russia? There's you, and a few others, right?

**Leonid Kales:** \[24:05\] Yeah, it's me, Alex - Alex is the organizer of the Moscow Gophers community. And we have Elena - she's responsible for organizing stuff, and me and Alex, we're more about the speakers, the program and so on.

**Brian Petersen:** So do you want to say hi to them on the air?

**Leonid Kales:** Yeah, I hope they're listening to me, so... Hi, guys!

**Brian Petersen:** Of course they're listening. They're shouting and screaming and rooting for you right now.

**Leonid Kales:** Yeah, I think so.

**Brian Petersen:** But Leo told us before the show that he was doing all the work, and that they weren't doing any... \[laughter\] So I hope he doesn't get in any trouble. I'm just teasing...

**Leonid Kales:** Yeah. By the way, we have one cool speaker I would like to highlight... It's [Elena Graham](https://twitter.com/webdeva). She's originally from Siberia, from Novosibirsk, and she also did great work for our community. She was leading a workshop for several months, about Go programming languages, there, on behalf of WTM group. It was very cool.

**Brian Petersen:** That's awesome. That name sounds really familiar, too.

**Carlisle Thompson:** Well, we talked about having her on the show.

**Brian Petersen:** Okay, that's why.

**Leonid Kales:** Yeah, she's very active. Now she lives in Berlin, in Germany.

**Carlisle Thompson:** What do you think, Leo, should we have her on the show?

**Leonid Kales:** Yeah, definitely.

**Carlisle Thompson:** Definitely, right? I agree.

**Brian Petersen:** So what kind of projects in Go are you most excited about, Leo?

**Leonid Kales:** Well, personally I'm really excited about [Robot](https://gobot.io/) and [Good](https://www.gocd.org/) stuff.

**Brian Petersen:** Nice...

**Leonid Kales:** But you know, right now I don't write a lot in Go. I do some automation in Go or in Python from time to time... That's probably why I'm so excited about these projects, because I'm trying to do some projects with it, with some hardware I have at home. It's more a hobby.

**Brian Petersen:** I think that's a universal thing. Everybody who does Go in any way has tried Robot in some way or another. It's one of the most fun projects out there. We love [Ron](https://twitter.com/deadprogram) so much.

**Leonid Kales:** Yeah. It's quite nice, quite handy stuff.

**Carlisle Thompson:** That's not true, I have not played with Robot.

**Leonid Kales:** You should try it.

**Brian Petersen:** Okay, not everybody... But if you come to Hack Day at Gopher Con you could play with Robot, because Ron runs an all-day-long workshop where he gives away free toys that you can program with Robot.

**Leonid Kales:** True.

**Erik St. Martin:** So before we jump over to the projects and news part of the show, I just want to recap about Gopher Con Russia - so it's one day, it's in March... What's the date?

**Leonid Kales:** It's on the 17th of March.

**Brian Petersen:** St. Patrick's Day.

**Erik St. Martin:** And for anybody who might want to attend who does not already have a ticket, are tickets still available, or are you sold out?

**Leonid Kales:** It's still available, yeah.

**Erik St. Martin:** And the site for that, for anybody who's interested, is [Gopher Con-Russia](https://www.gophercon-russia.ru/)...?

**Leonid Kales:** Yup.

**Erik St. Martin:** \[27:57\] Dot RU (.RU). I know we mentioned one or two speakers, but did you want to give a quick highlight of a few more speakers? Maybe a couple of the keynoters, or things like that.

**Leonid Kales:** Well, I don't want to highlight someone else. I think everyone is quite a brilliant speaker there, at the least. Yeah.

**Erik St. Martin:** I think that's definitely understandable. It's always hard to -- you don't want to leave anybody out.

**Leonid Kales:** Yeah, right.

**Brian Petersen:** I would list the names of all the speakers, but I'm not sure if I can pronounce them. I do know that there's a lot of people I know on this list though, which is really awesome. It's going to be a fun conference.

**Leonid Kales:** Yup.

**Erik St. Martin:** Brian needs to bring Go Time stickers.

**Brian Petersen:** I don't have -- Adam needs to FedEx me some Go Time stickers, because I don't have any and I leave Saturday.

**Erik St. Martin:** Something tells me you're not going to get them on time.

**Brian Petersen:** Oh, wait, I leave Saturday for Washington DC. I've still got time. I'll ping Adam. Furthermore, I get confused about where I'm travelling. Furthermore, I don't even know what day it is.

**Leonid Kales:** Probably I will bring some Siberian stickers for you, from our Go community.

**Brian Petersen:** Oh, nice. That would be excellent. I have a huge bag of stickers; everywhere I go, I collect more so that we can do sticker trading. That's a wonderful idea... And I'll bring my big bag, so that everybody can get stickers from places that they've never seen.

**Leonid Kales:** Yes, stickers' black market.

**Brian Petersen:** Black market stickers. That reminds me of an article I read, which is completely unrelated to Go, about black market records in Russia, in the '60s or '70s - maybe it was the '50s - where they used old X-ray pictures to make records, phonographs of music.

**Erik St. Martin:** Interesting. So they melted it down, and...?

**Brian Petersen:** No, they didn't even melt them down, they just pressed the records directly into old X-rays. So there are collections of these records where it's like somebody's broken foot, and it's Elvis. It's so cool. I'll have to dig up a link to it, but it was -- because that music was not legal, so it was an underground scene where they just found these old X-rays, and they used the old X-rays to make record pressings.

**Erik St. Martin:** People are creative. I wish I had that creativity to think of that... Like, "Here, I'm just going to use X-rays."

**Brian Petersen:** Why not? Kind of awesome.

**Erik St. Martin:** Okay, so does everybody want to move into projects and news?

**Brian Petersen:** Yes!

**Carlisle Thompson:** Yeah.

**Leonid Kales:** Yeah, let's go.

**Erik St. Martin:** Alright. I'll mention one thing quickly before moving on to the ones that can take much longer. Last week's episode we talked about Go, and there's been I think two more posts in that series; we talked about them coming out - they are out, so if you haven't read the additional posts in that series by Russ Cox, we'll link to them in the show notes.

The second item to talk about - it was 2–3 days ago, the results for the [2017 Go survey](https://blog.golang.org/survey2017-results) came out, which was fascinating.

**Brian Petersen:** What was interesting about it? I haven't read it yet.

**Erik St. Martin:** The link is in the show notes, but it was actually -- there's been a huge shift in the number of people who basically say they program Go outside of work, or they do it at work. They basically swapped. 2016 I think 66% of people or something like that - the top answer was "I program Go outside of work", and now at work seems to be the thing.

\[32:05\] Some of the other stuff I found interesting was actually the rankings based on language expertise and preferences. I expected to see -- obviously, Go was the top one in the list, but I expected to see a lot more like Python and Ruby and JavaScript... I didn't expect to see Java and C and C++ up there. This is in order of preference, but these languages have been around longer, so I think it's somewhat of an indicator of the communities that people are coming from when adopting Go... I mean, that'd be my assumption; if I had to answer my preference list, it would probably be Go first, and then the language I came from.

**Carlisle Thompson:** Yeah, that's a good assumption, I think.

**Erik St. Martin:** Some of the other things that were interesting was - I need to find it on the list, but it was asked how long people have been doing Go for, and that seems to be getting much bigger. Last year I think CLI programs were the top thing that people used Go to write, and now it seems to be API and RPC services. I need to find it on here, but another thing that surprised me was there is an answer "Web services that return HTML." That actually ranks higher than agents and daemons, libraries and frameworks, data processing pipelines... I didn't expect there to be as much there for web, because a lot of people are already using things like Node and Django and Rails and things like that, so I was actually surprised to see that.

**Brian Petersen:** I'm confused... Is that web servers that return HTML? Is that like just web apps?

**Erik St. Martin:** Yeah, so the answer itself said web services, and in parentheses it said "returning HTML", so I would probably think of that as something that actually serves the HTML, and not like a back-end service that delivers JSON to a front-end. That's actually really cool, because I didn't expect that to be -- I know people are doing it, but I didn't expect it to rank as high as it did over some of the other things.

**Brian Petersen:** That is interesting.

**Erik St. Martin:** And 50% or 48% of respondents said that they used Go as part of their daily routine...

**Brian Petersen:** I brush my teeth with Go every day, that makes sense... \[laughter\]

**Erik St. Martin:** We need gopher toothbrushes.

**Brian Petersen:** Oh, wow... That's our new swag for next year, Go toothbrushes... Because gophers should have good hygiene.

**Erik St. Martin:** I wonder whether people would take that personally, like "What are you trying to say? Are you saying that we're not well-groomed, or something...? Like, toothbrushes...?"

Some other interesting statistics out of that were operating system of choice that people use for development. 64% said Linux, 49% Mac, and 18% Windows. For some reason, I actually anticipated Mac being over Linux. I know a lot of us are Linux lovers for obviously writing our services against, but I still see mostly Macs, and things like that, for people using it.

**Brian Petersen:** I don't know if I believe that, unless they're talking about Vagrant or virtual machines, because every conference I go to, it's a sea of MacBook Pros, there's no Linux machines out there. I think there's something wrong with that.

**Erik St. Martin:** Maybe the Linux people don't like going to conferences.

**Brian Petersen:** Fair... Or maybe they bring their Macs because they're afraid of not fitting in...

**Erik St. Martin:** \[36:08\] No, actually -- I mean, if you think about it, I fall into that category really well, right? I develop exclusively on Linux - I have my Linux workstation, I have a Linux laptop I write code on... But I do all my admin stuff - social media, video chats and email and all that stuff, my to-do lists and stuff are all on my Mac, so when I travel, I bring my Mac.

**Brian Petersen:** That's true, good point.

**Erik St. Martin:** So the other interesting stat too was there was a swap - last year's survey showed Vim as being the top editor as far as preference goes, and it swapped with VS Code this year.

**Brian Petersen:** Wow, VS Code is in first place?

**Erik St. Martin:** VS Code is in first place.

**Brian Petersen:** That's amazing. VS Code is really an awesome place to do Go development. But so is Vim Go.

**Carlisle Thompson:** I think as more people enter the community, and they have different habits, we're going to see differences in what tools people use... So that makes total sense to me.

**Erik St. Martin:** And as far as community stuff goes, one thing that was actually astounding to me was that 40% of respondents said that they've never attended a Go remote meetup or Go conference or training, or Go Bridge event or anything in that manner. That was actually the top answer, 40% of people haven't done that. I'd be really curious to know why that is. Is it not having the opportunity to do so, or they feel they can learn enough through video content and blog posts and things like that? Or whether those things don't feel welcoming enough... I'd be interested -- because I wouldn't have expected that to be the top answer.

**Carlisle Thompson:** It's really hard to tell. We can speculate... That number would be more relevant if it was accompanied by geographical location...

**Brian Petersen:** True.

**Carlisle Thompson:** Because it makes such a big difference. If someone in San Francisco said "Oh, I'm doing Go, but I haven't attended anything", then we should be like "Oh, we need to do better, because the resources are there... People don't know, or what's going on?" But if someone in some really remote part of the U.S. or part of the world is saying "I haven't gone", then it's good, because they are doing Go in spite of not having access to these things.

**Brian Petersen:** Right.

**Erik St. Martin:** Oh, yeah.

**Carlisle Thompson:** It's completely different, depending on where people are.

**Erik St. Martin:** I think that's actually a perfect point, because even thinking about here locally in Tampa - we've been doing pretty bad about consistently holding meetups... Because it gets hard to find people to present or to have the time to create presentations, and sometimes just the overhead of trying to find a location for it and things like that, if you don't already have a company you can consistently do it at...

So even here locally, right? Anybody who lives here, and we're not running meetups here, or one didn't exist, and if you don't work for a company who's willing to send you to events, and you don't have meetups locally, you don't have the ability to go. So maybe that's also an indicator of the spread - we're starting to spread out of the big tech hubs and into the rest of the world.

**Carlisle Thompson:** Yeah. That also makes me want to ask Leo - Leo, did you take this survey, did you know about it?

**Leonid Kales:** Yes, and yes.

**Carlisle Thompson:** \[40:06\] Do you think a lot of people in your community knew about it and took it, too?

**Leonid Kales:** I'm not sure, actually, because I can't track that, but I think I spread this link to the community.

**Carlisle Thompson:** That's good.

**Leonid Kales:** I'm not sure about the Moscow community, but I shared the link to the Siberia community definitely.

**Carlisle Thompson:** So Russian is showing up as 3% of the respondents.

**Leonid Kales:** Well... Maybe.

**Carlisle Thompson:** That's good. Just as a comparison - Brazil, which is also a big country, is showing up as 2%. India is showing up as 2%, and India has been having a Go conference for a while now.

**Brian Petersen:** Yeah, that's very good.

**Erik St. Martin:** Where does China rank?

**Carlisle Thompson:** It's 2%.

**Erik St. Martin:** Interesting.

**Brian Petersen:** You know, a lot of this could be a language barrier, too.

**Erik St. Martin:** Oh yeah, I mean, we don't share the same mediums for getting news and being made aware of these things, and all of that... So it's always really hard to actually use it as final statistics and anything less than kind of gauge. I mean, even when we do a survey for Gopher Con -- I forget what the percentage of people is, but it's certainly less than 50% of people ever fill out the survey.

**Brian Petersen:** That's true. Leo, I forgot a very important question that I need to ask you - Vim or Emacs?

**Carlisle Thompson:** Oh, Geez...

**Leonid Kales:** Sorry?

**Brian Petersen:** Do you use Vim or Emacs?

**Leonid Kales:** I use Vim.

**Erik St. Martin:** Tabs or spaces -- no... \[laughter\]

**Brian Petersen:** Very good, Leo. It's all good, he uses Vim.

**Carlisle Thompson:** One thing that I wanted to mention too from the survey -- I don't know if Erik was going to get to it; if so, sorry Erik, I'm cutting ahead of you... In the community aspect, the answer to "I feel welcome in the Go community" last year the disagreement was 15 to 1 -- sorry, the agreement to disagreement... Yeah, that wasn't going to sound right. The agreement to disagreement last year was 15 to 1, and this year the agreement increased to 25 to 1. I think that's pretty cool.

**Brian Petersen:** That is very good.

**Erik St. Martin:** Oh, that's awesome. We're making people feel more welcome. So I think the last thing that I can think of offhand -- this is a really long thing, and it's an interesting read for anybody who actually wants to get into all the details outside the ones I've pointed out now... The two primary things that were kind of conveyed in problems people see with Go or why they're not using it where lack of generics and dependency management. That actually talks about they're going to try to focus on those two issues in 2018.

**Brian Petersen:** Nice. I don't want generics...

**Erik St. Martin:** I can't think of anything else in there offhand that I thought was interesting...

**Brian Petersen:** 100% of the people surveyed said that Go Time was their favourite podcast. \[laughter\]

**Carlisle Thompson:** Well, the English speakers, right?

**Brian Petersen:** No, 100%. All of them said Go Time was their favourite podcast. Even if they came from another place where they had a different podcast, they said Go Time was better. \[laughter\]

**Erik St. Martin:** \[44:00\] Brian has this Chrome filter called "Craze Brian", and when he turns it on, everything turns into 100% love. \[laughter\] It's like, every site he goes to, "100% of the people who use this site love Brian." \[laughter\]

**Brian Petersen:** That'd be an interesting Chrome filter. I'm gonna work on that, for Donald Trump.

**Erik St. Martin:** It would make you feel good every day, right?

**Brian Petersen:** True.

**Erik St. Martin:** Everywhere you go, the site somewhere in their compliments you. You install it, and you just give it your name, and done. Sell it for a dollar, be a millionaire.

**Brian Petersen:** Brilliant.

**Erik St. Martin:** I get my commission, because it's my idea though.

**Brian Petersen:** Sure, you can have a penny out of every dollar.

**Erik St. Martin:** I'll take it. Alright, so next on interesting projects and news - I haven't been trolling GitHub too much the past week or so, but... I can't remember, I think we mentioned the [Pwned Passwords list and service](https://haveibeenpwned.com/Passwords), but Matt Evans has created a [Go library for querying the pwned passwords list](https://github.com/mattevans/pwned-passwords) to see if a password has been compromised in a prior data leak.

**Brian Petersen:** That's excellent... Which reminds me of the dating app that lets you enter your password to find other people that have the same password for dating... Which makes so much sense! \[laughter\]

**Erik St. Martin:** Think about the number of people who still use "password1234" though... You'd end up with a ton of matches.

**Brian Petersen:** Well, that's why they're perfect for each other; if you're using "password123", then you guys were meant to be.

**Carlisle Thompson:** Just grab the first one, you cannot go wrong. First one on the list that pops up, that's it.

**Brian Petersen:** Sold. "She's my soulmate...!"

**Erik St. Martin:** But then people like me, who use my generated one password - there'd be nobody. Just loneliness.

**Brian Petersen:** Yeah...

**Erik St. Martin:** Alright, did anybody have any other projects or news that they came across this week?

**Carlisle Thompson:** Sorry, I have a slow come-back to that, but I have to say it... You can't be locked in security AND love, it can only be one. So if you don't find a match, that's a good thing, based on the password... \[laughter\] At least you're good with security, so... Who cares about love?

**Erik St. Martin:** We commend you on your selection of secure passwords. We're sorry, you're going to be lonely", right?

**Carlisle Thompson:** Yes. \[laughs\] Alright, moving on.

**Erik St. Martin:** That is such a weird way to find a date. "Please give me all the people who share the passwords with me."

**Carlisle Thompson:** That's not real, right?

**Brian Petersen:** Oh, I think it's real.

**Erik St. Martin:** It also seems like a really, terrible security idea. Like, "Oh, this match shares the same password as you." Now you go find all the sites, and you have somebody's name and knowing that they have that password.

**Brian Petersen:** That's perfect. Maybe it's just a great, big fishing experiment.

**Erik St. Martin:** That's quite possible, too.

**Brian Petersen:** I don't know.

**Leonid Kales:** Have you heard about the Get Contact application?

**Brian Petersen:** No.

**Leonid Kales:** It's an application - you sign up, and it collects all your contacts from the address book, and you can search for any phone numbers and find the name of the person. The fun story here is, for example, you can find out how other people wrote down in their address book; it's very fun. I can send you the name...

**Brian Petersen:** \[48:00\] Oh... That's scary.

**Leonid Kales:** It's very bad for the privacy, but a very funny application.

**Brian Petersen:** Yeah, because I have interesting names for people in my address book that I would not want anybody to ever know.

**Carlisle Thompson:** Oh, really?

**Brian Petersen:** Yeah, like Erik... I don't call him Erik in my address book; it's something completely different, and if Erik knew that, he would be mad at me for a long time. Those are things that we don't want public.

**Leonid Kales:** \[laughs\] Yeah.

**Erik St. Martin:** Alright. So \#FreeSoftwareFriday... Does anybody have stuff?

**Brian Petersen:** You know, I don't. I don't have a \#FreeSoftwareFriday this week; how sad is that?

**Carlisle Thompson:** Oh, if Brian doesn't, I feel not so bad for not having one either, just mainly because I didn't think about it. I haven't been having one. It's hard.

**Erik St. Martin:** Sometimes it's hard based on what you're doing, and if you're kind of doing the same thing for weeks on end, you may not be exposed to projects... Or when you are, you don't think to write that down, like "I need to give this person a shout-out."

**Carlisle Thompson:** Yeah.

**Erik St. Martin:** Leo, so at the end of every episode what we typically do is something we call \#FreeSoftwareFriday, where we give a shout-out to a project or a maintainer of open source - it does not have to be Go - just to kind of show our love and appreciation for what they do. I know this is on the spot, so it is okay if you don't have one, but if there's anybody or any project that you absolutely love and helps you out, feel free to give them a shout-out.

**Leonid Kales:** Well, maybe not today... Sorry, guys.

**Erik St. Martin:** Okay. So I do have one this week - source{d}, they have a [go-git](https://github.com/src-d/go-git) library, which is an implementation of Git completely in Go, and for a project that we are working on at work I'm doing some Git stuff, and I've been playing along with that as a library, rather than shelling out to the Git command itself. It's making things a lot cleaner and more fun.

**Brian Petersen:** That's really nice.

**Carlisle Thompson:** That's interesting.

**Brian Petersen:** [Source{d}](https://sourced.tech/), that's where [Francesc Cambó](https://twitter.com/francesc) went, right?

**Erik St. Martin:** Yes.

**Brian Petersen:** Awesome. Hi, Frances. We love you.

**Leonid Kales:** Yeah, they also have a speaker from there, at Gopher Con Russia.

**Erik St. Martin:** Oh, yeah?

**Carlisle Thompson:** Not Frances?

**Leonid Kales:** No, unfortunately. But yeah, we have Vadim - he is a Google developer expert on machine learning. Yeah, quite a cool guy. I will send his GitHub to the Slack.

**Brian Petersen:** \[50:54\] That's awesome, thank you.

**Erik St. Martin:** Alright, so if nobody has any other projects to give a shout-out to, I think we are at time. Thanks so much for coming on the show, Leo. Thank you to all of our listeners, thank you Carlisle for being on the show... Brian, we're no longer friends.

**Brian Petersen:** Oh, come on... \[laughter\] You know I'm just teasing, Erik. And I'll get rid of the nasty name in my phone book.

**Erik St. Martin:** I want to know what the ringtone is, too.

**Brian Petersen:** Oh, no, you don't. You really don't. I just posted a picture in Slack of the hat that I knitted during today's show for my new niece, Eva. Shout-out to Eva, who is tiny, tiny, tiny, and I'm looking forward to meeting her this weekend. I have to bring a hat.

**Erik St. Martin:** It's adorable. You need to post in on Twitter in reply to my commenting that you're knitting live so people can see the result.

**Brian Petersen:** Oh, good point. Okay, I'll go do that right now.

**Erik St. Martin:** Alright, so thanks again for listening, everybody. You can follow us on Twitter, @GoTimeFM. Head to gotime.fm to subscribe, and github.com/gotimefm/ping if you have suggestions for topics or speakers, including yourself. With that, goodbye everybody! We'll see you next week.

**Brian Petersen:** Goodbye! Thanks, Leo.

**Leonid Kales:** Thanks for having me.

**Carlisle Thompson:** Bye, everybody. Leo, this was great! Thank you.

**Leonid Kales:** Bye all.
