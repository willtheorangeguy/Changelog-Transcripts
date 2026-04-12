**Erik St. Martin:** We are back with for another episode of Go Time. This is episode number 13. Before we kick off this show I want to give a quick shout out to our sponsors for this episode. Linde, Changelog's cloud server of choice, and Equinox.io, the best way to package and distribute your Go apps.

Today on the show we have myself, Erik St. Martin, Brian Petersen is also on the line...

**Brian Petersen:** A Brian Petersen without much sleep, apparently.

**Erik St. Martin:** So half of Brian Petersen is on the line, and then we also have Carlisle Campos...

**Carlisle Thompson:** Alive and kicking after Gopher Con.

**Erik St. Martin:** And our special guest for today's show is Francesc Cambó from the Go Team. Say hello, Frances.

**Francesc Cambó:** Hey, how are you doing?

**Erik St. Martin:** Good, good. So let's talk about Gopher Con, being that I think all of us were there, at least partially. Brian-half-sleep at Gopher Con...

**Brian Petersen:** Yeah, apparently. So this is our first show after Gopher Con. Gopher Con officially ended last Wednesday, it's now Thursday... I still haven't even read all my email or done my laundry.

**Francesc Cambó:** I just got to my inbox zero yesterday, and I was so proud. I'm done for the rest of the week.

**Erik St. Martin:** I spent airline time doing the inbox zero thing.

**Carlisle Thompson:** I haven't been at inbox zero for a long, long time.

**Brian Petersen:** So I didn't have to do laundry because I got so many shirts at Gopher Con, I'm just wearing them one at the time. At some point I'll run out... Then I'll have to maybe do laundry this weekend. But it's pretty nice getting a lot of shirts.

**Erik St. Martin:** How do people even manage collecting all of that swag? You need to bring a second suitcase just to bring home swag.

**Carlisle Thompson:** Or you do it like me... Because I was there the year before, I went prepared. My suitcase was small and pretty much empty, because I knew, like I basically only need one T-shirt, because I'm going to get T-shirts for the rest of the days.

**Erik St. Martin:** I can't keep mine, my wife likes to steal all of them. I think we need to have people make less comfortable shirts, and then they won't get stolen. \[laughter\] São Francisco, do you wanna talk to us a little bit about your talk at Gopher Con? It was actually fascinating to put that much attention on Nil, which I think from most people's perspective, when you talk about it, it's for bad reasons and not for good uses, and why nil should be embraced.

**Francesc Cambó:** Yeah, I agree. So the talk basically came up when I started talking with someone about how there were nil receivers that could work. If you define a function on a pointer receiver, if that pointer is nil, that doesn't mean that the method will fail. And after talking about that, we started talking about all the things where nil was useful, and I saw that there was kind of a theme where basically nil and Go is not something that should be avoided in general. I mean, you need to be careful, obviously, but it's something that can be really useful, so I thought it could be an interesting talk. But when I proposed the talk I was in a bar in Belgium, right after FOSDEM, and basically I just sent the abstract, and I was very excited about it, but when it got accepted, I was like "Oh wait, now I have to talk about nil for thirty minutes? That's going to be fun."

**Brian Petersen:** \[04:02\] I think you tweeted a picture of that, didn't you? I want to say you tweeted a picture of you holding up a beer, saying you were working on your proposal.

**Francesc Cambó:** Yeah, that was actually in FOSDEM, so in Brussels. I think it was in February probably, I don't remember. But yeah, I was surrounded by other Gophers. We had finished the Go dev room at FOSDEM, so lots of people surrounding us. Basically we did a proposal party where we just sent all our talk proposals at the same time pretty much, right before it was too late. So yeah, we were part of the people - do you know that peak that you get at the end, the last hours before you get to the deadline?

**Erik St. Martin:** The last 48 hours, where we get like 70%?

**Brian Petersen:** The procrastinators' party.

**Francesc Cambó:** Procrastinator - absolutely. Yes, that was me.

**Brian Petersen:** So how did you feel about going on first this year?

**Francesc Cambó:** I was pretty nervous... My talk changed a lot since I was notified that I was the opening keynote speaker. I was like, "Oh wait, what?" So I made it more of trying to get a mission of embracing nil, rather than just giving a bunch of technical facts, and I think it made the talk much better.

To be honest, I was nervous also about being the first person on stage, but then I saw Kelsey Hightower was right before me and he did an amazing job, that it was actually... It was very easy to get on stage after him, and also incredibly hard to try to compete against what he did.

**Erik St. Martin:** Yeah, the remix of that poem was awesome. We sent him home with a framed copy of it.

**Francesc Cambó:** Yeah, when I got on stage I said that he almost made me cry, and people laughed about it like it was a joke. It was not. I was almost crying. I was like, it's going to be hard to say that nil is a good thing while crying, so let's keep it calm. \[laughter\]

**Brian Petersen:** It was very moving.

**Erik St. Martin:** You were telling yourself on the inside, "Put yourself together now."

**Francesc Cambó:** Yeah, basically.

**Erik St. Martin:** So the nil talk was one of the ones I actually got to see a good portion of, and I really enjoyed it. Because there are a lot of use cases, and I was glad you pointed out one of my favourites, which is setting a channel to nil in a select, so that you can continue to select on the other channels.

**Francesc Cambó:** Yeah, it's something that is so simple... Once you understand it, it's so obvious, but many people when they write concurrent programs don't take that into account, and it will very often happen that they either have a busy loop, or they will leak memory, leak go routines, and things like that. So there are these little things that I'm trying to get people to keep in mind for whenever they actually need them.

**Erik St. Martin:** Yeah, speaking of leaking go routines, Ivan's talk with visualizing the concurrency, I've never seen leaking go routines look so awesome. \[laughter\]

**Francesc Cambó:** That was amazing, yeah.

**Erik St. Martin:** It's like, "How can this be so terrible but yet so beautiful at the same time?"

**Brian Petersen:** That's an interesting segue into one of the Go projects that I was keeping my eye on this week. He released that particular package Go Trace I want to say yesterday or the day before. It's at github.com/divan/gotrace. Really awesome tool.

**Francesc Cambó:** Yeah, I was checking it this morning and the animations are just so beautiful that I want to run it with everything. Basically the problem right now is that the browsers are not able to catch up with all the go routines that we start in Go. Maybe we should make go routines heavier, or browsers faster. But there's a problem here. \[laughs\]

**Erik St. Martin:** Filing a bug for the browser, saying that it needs to increase performance so that we can show all of our go routines.

**Francesc Cambó:** Yeah.

**Erik St. Martin:** \[08:02\] It's a motivating factor.

**Francesc Cambó:** They look really cool. My favourite graph from everything he showed was the Eratosthenes Prime Sieve. I've seen that program many times before, and it's kind of hard to explain how it works. And after seeing that, I feel like anyone could just be like, "Oh, okay. I get it. I understand what all the go routines are doing, the data, how it's going through all the filters and everything." It's just beautifully simple.

**Erik St. Martin:** Visualizations are hard, too. That's something I've always struggled with, it's like how do you take some complex thing going on behind the scenes and visualize it so that you can easily understand it, and I think he did a perfect job at being able to see the data going between go routines and things like that, the transfer of execution. It's a really cool project, I'm waiting for the video to come out. I missed parts of it. That's the sad part that Brian and I have to struggle through. We don't always get to see all the talks.

**Francesc Cambó:** Actually, since you've mentioned videos, I've had this question many times - when are the videos coming out?

**Erik St. Martin:** They take about a month, because there's some post-production time. We have 25 videos that have to be produced, and then lightning talks. They're so massive they have to mail a hard drive.

**Francesc Cambó:** Oh, nice.

**Erik St. Martin:** Yeah, so it takes a couple of weeks, up to a month. I would say by time it's hit one month out, the videos should be out. I think last year 18 days or something along those lines is what it took us to get them live.

**Carlisle Thompson:** Did they all come out at once?

**Erik St. Martin:** Yeah, they send a hard drive of all of them, and then I set my computer loose on uploading to YouTube.

**Brian Petersen:** This year was a little different because we streamed live on YouTube...

**Erik St. Martin:** On Twitch.

**Brian Petersen:** Twitch, sorry. Thank you. Did I mention I need some sleep? So we did the live-streaming this year and I think we had a maximum of almost 2,000 people at any given time watching, which was amazing. And a total of almost 9,800, almost 10,000 people. Or was it 8,800, almost 9,000? One of those two.

**Erik St. Martin:** I think it was 9,000.

**Brian Petersen:** Yeah, a lot of people around the world watched at various points during Gopher Con, and that just made my day. It was really neat to be able to share the conference, that was a very local and specific thing, with the whole world.

**Francesc Cambó:** Yeah, one of the people that were there on Twitch was my mom, watching my talk.

**Erik St. Martin:** Oh, really? That's awesome.

**Francesc Cambó:** Yeah. Fun fact - she doesn't speak English... She loved the talk; she doesn't know what I said, but she loved the talk.

**Carlisle Thompson:** As Scott mentioned on Go Time FM gophers channel - the conference is local, but the content is pretty relevant to everybody, and it has a pretty wide range of talks, and of course people all over the world can benefit.

I want to mention this because it was so awesome... Yesterday the Remote Meetup streamed the Golf meetup, and it was amazing. This business of streaming is awesome, we need to keep doing it.

**Erik St. Martin:** Yeah, the only struggle with streaming is if it starts taking away from physical attendance. Because one's free, and one pays for everything. But I think people get a lot more out of attending. There's a lot that you can get out of just being there and being able to network. I guess videos would have taken away attendance if that was ever going to be a thing.

But I share some concerns though... We had some discussions with Kelsey and somebody else, I think it might have been Dave Cheney, where this whole nature of streaming and recording and stuff like that also starts kind of burning out speakers, because they constantly have to have new content and they can't continuously deliver and improve on a talk, because once they've given it, and it's been recorded, then it's kind of done; nobody wants to pay to go to a conference and see a talk that they already saw on YouTube.

**Francesc Cambó:** \[12:18\] On the other hand, conferences being slow at releasing the videos actually help us. \[laughter\]

**Erik St. Martin:** Yeah, exactly, because more people get to see your content, and things like that. For us, the videos going out was really just trying to help the community grow. The more content, the more people can be exposed to the language and the more growth we see in the community, which was kind of our motivating factor for releasing the videos.

**Brian Petersen:** Yeah, and my general theory has always been that whether we're releasing the videos or whether we're doing a live stream, most people come to conferences and the talks are almost secondary to all the rest - the networking, getting together with your friends, the community. A lot of people I talked to skipped out on talks at various times of the day and went off and did things with people that they don't get to see often. So there are benefits to going to the conference that aren't directly related to those talks, and you know that it's going to be on YouTube later, so there's no need to attend all of them.

**Erik St. Martin:** And Hack Day. Holy cow, people stayed for that. There was probably 800 people there.

**Brian Petersen:** That was a big surprise. I think we planned for half of that.

**Francesc Cambó:** Yeah, it was pretty amazing to see so many people working on random things. We had the Go project room, and before going there I was working on something else... I was actually releasing my podcast, because it was Wednesday, and I had totally forgotten about it. But it was hilarious, because people would keep on coming to me... It was like, "Oh, so what are you hacking on? Can we work together?" It was this very collaborative spirit of everyone trying to help each other, I loved it.

**Erik St. Martin:** You can help me release my podcast episode. \[laughter\]

**Francesc Cambó:** Yeah.

**Brian Petersen:** So tell us a little more about what went on in the Go project room.

**Francesc Cambó:** It was pretty funny, because we did not really have that much time to prepare it. So rather than trying to have a very strict schedule, what we decided was we had one of the meetings that we hold for every release meeting. This year was Go 1.7 release meeting, and we did that from 10 to 10:30, just half an hour, so people could see how a new version is released for Go. That was very powerful, because people sometimes think that it's something dark and magic... But no, it's just a bunch of people talking about what they - they want to make sure that everything is out, and there's no more bugs and things like that, so it was pretty good.

My favourite part was right after we had the dependency discussion. The dependency discussion is pretty interesting, because it's talking about one of the hot topics in the Go community - rendering. And not only rendering; talking about "Is rendering a good solution? How should we do it? What are the tools?"

I know that Chris Broad foot was there, and he took a bunch of notes, and I'm looking forward to the document that will explain basically about all the things that were discussed. But it was a very, very active discussion, that's for sure.

**Erik St. Martin:** That room was packed the entire time, and no riots. It was crazy.

**Brian Petersen:** That's what I was going to ask - nobody got stabbed, or anything? I mean, rendering - this is a hot topic. This can be contentious.

**Francesc Cambó:** Yeah. I know that some people were very passionate about it, but not to that point, unfortunately.

**Erik St. Martin:** \[15:52\] I really liked how that room turned out though. It kind of grew organically, and I think that it's something that we should continue to grow on its own; make more space and put some A/V in there and maybe live stream that, because there were a lot of valuable discussions that were going on, and it seemed a lot of people wanted to be involved in that, too. I think continuing to grow that each year will be nice as well.

**Francesc Cambó:** Yeah, I'm looking forward to next year, trying to do something even bigger.

**Erik St. Martin:** Speaking of bigger, we wanted to get... Because this year's mascot was a parade balloon - you know, like Macy's day parade... We wanted to get like a big one to float, and we never got around to that.

**Francesc Cambó:** That would have been amazing.

**Brian Petersen:** We probably would have had to have some special dispensation from the damn fire marshal, though. Don't get me started on that fire marshal.

**Carlisle Thompson:** We should have a Gopher parade to open Gopher Con.

**Erik St. Martin:** We need a Gopher fire marshal.

**Francesc Cambó:** A balloon gopher, just as a plushy, I would love that. So if you're thinking about presents to get me, now you know. \[laughter\]

**Erik St. Martin:** For anybody listening...

**Francesc Cambó:** For anybody listening... Yeah.

**Erik St. Martin:** A parade balloon gopher.

**Francesc Cambó:** Yeah.

**Erik St. Martin:** The little toys were fun that we did for 2015, too. I thought about getting more of those done. We'll have to keep toying with that idea. So did you have any favourite talks that you came out of that you liked, Frances?

**Francesc Cambó:** There were many talks that were very interesting. I really loved Ivan's talk on the visualization of concurrency, because I think it's something that I struggle with. I teach many people about Go, and it's very hard to visualize what a program is doing, and I feel like with this it is so much easier. My favourite talk though probably was Katrina's.

**Erik St. Martin:** Without a doubt. I haven't seen all the talks, but all the ones that I did see, that one... I think she put into perfect terms something that we all struggle with. She just kicked it off really well, with all the ingredients of a Twinkle. It's like, "I have a degree in molecular biology, I know what all of these things are, but I still can't turn it into a delicious pastry."

**Brian Petersen:** It was a great talk, very inspiring.

**Francesc Cambó:** My favourite part of the talk was... I mean, the presentation was amazing, and the slides were really fun. One of the slides was the metro in Barcelona, which I always appreciate... But my favourite part was the fact that she talked about how you can be fluent without being proficient. That is something I had never thought about, the fact that for instance if you're learning how to speak English, you could be totally fluent at asking beer when you're at a bar, but that doesn't mean that you know how to read Shakespeare, and that's totally fine. I think that applying that to teaching Go can be very interesting. Don't try to learn all the concurrency patterns, don't try to use generic - not generic, sorry. Whoops! \[laughter\] Unsafe. Don't try to use reflection. Just really understand the basics, be fluent in those basics and then move on from there. I thought that was very powerful, and she explained it in such a beautiful way. I loved the talk, really.

**Erik St. Martin:** Yeah, and the comparison to graphs I think really set some of that stuff home. For any of us that look at a language and are like "That makes total sense", we forget that we have all of these nodes of information, and we're just drawing connections between them; it makes it easy for us to do stuff.

Even behaviour... Like, I know in the Slack channel I've been quick to answer a question, and I'll link to a section of the language spec, and it makes it look like that's just knowledge I have in my head. Like, "Oh yeah, right here, in the language spec." And it's like no, often times I vaguely remember there being some rule about that, I look it up real quick and then link somebody to it. But the outside perspective is that there's a bunch of us running around, and we just memorize this stuff, and it's just not true.

**Carlisle Thompson:** \[20:11\] And I think she also did a really great job, like you were saying Frances, in articulating what we were thinking... I couldn't even point towards what she said before I heard her say it, and now I can, which is there is no clear path for a person who is a newcomer to Go to being proficient, or a person who's a beginner to programming and being proficient in Go; and we know Go is a very simple language to learn. So there should not be this barrier, and a lot of people were having this conversation at the conference and even after the conference.

For example Matt Maisonette did a beautiful [blog post](https://medium.com/@mattetti/go-is-for-everyone-b4f84be04c43) about Go being for everyone, and I think it is going to be very healthy for us to identify what we need to do and why we need to do these things, because I think a lot of us want people to join the community, and not just because we want everybody to do Go, but if you do want to do Go or try it out, there should be an easy path for you. You should be not only welcome in the community as a person, which I think we're doing a great job at that, and we can talk more about that too, but also as far as learning the language.

**Erik St. Martin:** And similar to that talk was Michael MATLAB's talk on contributing to Go, and even open source. I think that was valuable, because a lot of people feel like they're not at the skill level they need to be in order to contribute, and there are so many ways to contribute. One thing that I've advocated to people is that sometimes a solution to a problem is better than no solution. It's easy for somebody to come through and be like, "Oh, you could make this faster if you remove these couple allocations" or "It would look cleaner if you made these couple of abstractions", but we're looking at it after the fact, right? Seeing somebody's solution and thinking about how to tweak it to make it better is much easier than solving the initial problem, so I think that there's value in people contributing test cases or testing bugs to get steps to reproduce vague bugs people put and there are so many ways that people can contribute, but I think a lot of people are like "Well, I'm not at that standard. There's nothing I can do to help, and I shouldn't have any business being in the repo trying to submit patches."

**Francesc Cambó:** Yeah, that actually takes very well with something else that we discussed in the Go project room during hack day, which are we have these... We had actually two different talks with two different sessions where we ended up discussing the same things, which is the user feedback and the diversity of discussion. Surprisingly, we ended up talking about pretty much the same things, which were we needing more people in the community; to do that, we need to teach more people, and to teach more people we need better ways to basically welcome people that have never programmed in any other language.

We have things like the Go Tour, which I think is a great tool for people that have already programmed in other languages, but if you come from no programming experience at all, when we say "Oh yeah, the for loop is like C++, just without the parenthesis", it's not incredibly helpful.

So we're talking more about okay, so how do we get this started, what kind of resources we want them to get together? Katrina was talking a lot about what kind of resources are available in the Ruby community, and I think that that is something that hopefully during this year and coming up to next Gopher Con we'll have new things and new projects about how to basically get more Gophers involved.

**Erik St. Martin:** \[24:11\] I think some of the tour too can be misleading. I was helping somebody who was walking through the tour and there was one particular exercise where I think all it wanted you to do was a loop through a multidimensional array - it was a slices section - and basically allocate the slices for this multidimensional slice. But the example really explained it as like outputting a greyscale image; and really what the value wasn't important. It gave some examples, but even just in the phrasing of the question, it made it sound like it was this advanced thing, like they wanted you do draw an image with a multidimensional array, and it kind of locked this person up and like, "Wait, wait... I've never drawn images, and stuff like that." So I think having a feedback loop on some of those things where things might seem more advanced that they really are and just changing the wording of it can help a lot, too. And anybody who can submit advice or things that they run into that seem harder than they feel it should have been.

**Francesc Cambó:** You know, we definitely welcome pull requests.

**Erik St. Martin:** That's right, the tour is part of the repo, for pull requests, isn't it?

**Francesc Cambó:** Yeah. I actually maintain it partly, so if you send pull requests, or even better, if you don't know how to improve it, but you know that it is not clear, just send bugs. From the tour there is a little bug button on the right corner on the top. From there you go to the GitHub repo, which is github.com/golang/store, and then you can just send your issues or your bugs in there, and hopefully I will take care of them.

I agree that in general the exercises tend to be a little bit too complex, and it's not always related to Go. One of the examples is the first exercise ever. It is a for loop to compute a square root of a number using Newton's method. That by itself just sounds scary, and it turns out it's just a for loop. So it can be a little bit confusing at the beginning.

**Erik St. Martin:** Yeah, and I think for anybody who has more of a formal background some of these things seem clearer than people who are more autodidact, they've taught themselves to program and maybe don't have the formal...

**Carlisle Thompson:** While on subject, there was a lightning talk by this guy, and I keep forgetting his name... I'm looking on the Gopher Con repo for the 2016 talks and I can't identify him in there, maybe he hasn't added it yet. In any case, he has this proposal about doing an open source collaborative effort in putting together a book, and he has some specific ideas I thought were brilliant. I'm hoping he was going to go forward with that. I'd love to get people connected to get that... Landon Jones, yes. He's a firecracker. I hope this takes off.

**Francesc Cambó:** What talk was this you said?

**Carlisle Thompson:** It was a lightning talk on the first day.

**Erik St. Martin:** Yeah, he was talking about building a book for high-school students, or something along those lines. I didn't see the talk, but I remember people referring to it.

**Brian Petersen:** He cornered me in the hallway. His idea for the book is called The Little Gopher. It sounds fascinating. He's even trying to line up Renee to help with some illustrations.

**Francesc Cambó:** Cool. I'll check it out whenever the talks are out.

**Carlisle Thompson:** If Renee cannot help him, I know a designer who can take Renee's graphics and really do something amazing.

**Francesc Cambó:** \[28:03\] Now that you mentioned Renee, I have to say that if Katrina's was my favourite talk, Renee's was probably the second one, or maybe the first one. It is hard to choose, because they're very different, but Renee's talk was amazing, and I'm just so happy you had such a non-technical talk at such a conference. It was great.

**Erik St. Martin:** Yeah, I mean, the Gopher is a staple of our community, so when she submitted a proposal we were like, "Alright, we have to do this.

**Brian Petersen:** Yeah, this has to happen. And it was kind of interesting that she wanted to do the talk with all the stage lights dimmed and only the screen; that caused the whole Convention Centre staff to go into a full panic. "We can't possibly do that. What if there's a fire and people get up and trip over each other because the house lights are down?" So we had to ask Kelsey specifically to mention, "Stay in your seats, don't move. We're going to dim the lights. Keep calm, don't panic."

**Erik St. Martin:** Yeah, that talk was just phenomenal. I'm really happy she came out and got to give everybody a little insight into the Gopher. It was kind of fun, and I think it was a welcomed mind-break for a lot of people, too. Because you're kind of overwhelmed with all this new content, so being able to sit back and relax and have some fun with the Go Gopher...

And I loved that she credited a lot of artists who have been doing our work surrounding the Gopher recently, too. It's kind of fun to see her take on that.

**Carlisle Thompson:** I want to encourage people to watch it, if they didn't watch it at the conference. It's not just an amazing talk about the Gopher... She really went deep into the design process, her process, how she approached it, and you will never look at the Sophie the same again.

**Brian Petersen:** My favourite part was that she stayed after the talk and gave out those cute little Gopher sheets with custom-drawn Gophers on the back of them that she autographed. I don't know how many people were able to take advantage of that, but I saw dozens and dozens of people walking around with them. I thought that was adorable.

**Francesc Cambó:** It was pretty funny, because there was a really long line, and then a bunch of people from the Go team waiting for her to finish going get lunch. And when the line was over, the people from the Go Team started lining up, because we also wanted them. They were amazing. My new desktop background is the Gopher she drew for me. It's just amazing.

**Erik St. Martin:** It's like "I can eat, or I can have a custom-drawn Gopher."

**Brian Petersen:** That's not a choice. When she made one for me, the first thing she asked me was "What are your girl's names again, Brian?" So I told her my daughters' names, because last year after Gopher Con both of my daughters painted pictures of a gopher, and we mailed them to Renee. And she said, as she was drawing the picture for my girls, she said "I've got those hanging in my living room", and I was just like "Oh my god, oh my heart..." \[laughs\] I was so impressed.

So this is a good time for us to stop and take a break and thank our sponsor Linde. Linde is Changelog's cloud server of choice. It's what Adam and Jerold are using to build their new CMS and the future of Changelog is riding on Linde. You can get a Linde server up and running in seconds. The easiest way to get started is by going to linode.com/gotime. You can choose your flavour of Linux, the resources you want and the location of your node. They've got eight data centres spread across the world and plans start at ten dollars a month. The nice thing about Linde is that you get full root access. You can run VMs or containers, your private Git server, you can run Hugo and have your own blog. You get native SSD storage, fast 40 GBS networking and nice Intel i5 processors. Furthermore, you have a fancy control panel where you can reboot things and resize things and clone your VMs, as well as a CLI tool that you can use to manage, and an API, so that you can call it remotely. Furthermore, you can use the code 'gotime20' to get two free months, which is $20 credit. Furthermore, you should tell your friends about that, so everybody can go off and get their own servers. Again, go to linode.com/gotime so you can get started.

**Erik St. Martin:** \[32:15\] And to keep us on the air.

**Brian Petersen:** Yay!

**Erik St. Martin:** So are there any other talks anybody was able to see that were interesting? I know Donnie Behold's talk was really well received as well, Mining the Go Developer Community. I didn't get to see that one. Was that something you got to see, Frances?

**Francesc Cambó:** Yeah, I got to watch it and it was very interesting. Basically, he kind of did my job, because I tried to make the community better and "Yeah, that is actually very interesting data." There were a lot of interesting things, like how people are using rendering, what kind of tooling they're using, if people are using debuggers or not... I think it's a very good place to start to basically try to have a campaign on... If you want everybody to use go FMT - I mean, go FMT is the one that everybody uses... But things like error check - how many people are using that, that is a very interesting conversation. And try to get more people to use the tools that everybody agrees increase the quality of the code. So yeah, I loved the talk.

**Brian Petersen:** Here's something that's just blowing my mind. We've got one of our very remote people on Slack right now, saying that his favourite talk was the Inside The Map Implementation from Keith Randall. The reason this blows my mind is that I know he wasn't at Gopher Con, and he watched it over the live stream. I'm just having a little bit of a joyous moment right here.

**Francesc Cambó:** Yeah, I have to say that Keith's talk was so technical but so funny at the same time that I loved it. My favourite part was when basically in a very fine example of trolling he said, "Oh, Go doesn't have generics, but you can fix it with unsafe." I was like, "Oh my god! You didn't go there." \[laughter\]

**Brian Petersen:** Yeah, what was that... A map of function pointers?

**Francesc Cambó:** Yeah, it was pretty amazing. I mean, the whole thing - how it was done and everything, it inspired me to try to implement Go Maps by myself too, but at the same time I feel like for some people it might be a little bit too... Like, I don't want people to be so attracted to unsafe that they're gonna just be using it everywhere. Maps are already there; have fun, enjoy them, don't reinvent the wheel, and especially, don't reinvent unsafe wheels, if possible.

**Erik St. Martin:** The thing I love about the unsafe package is basically it makes you... It's like you want to delete a GitHub repo you have to type the repo's name to be sure; so every time you go to use unsafe you have to say 'unsafe'. It just keeps beating it into you, "I should not be doing this."

**Francesc Cambó:** Yeah. I had an idea, I don't know if you saw it... I [tweeted about how you can give an alias](https://twitter.com/francesc/status/920740297713291265) when you're doing imports. So you could do `import totes safe "unsafe"`, so instead of `unsafe. Pointer` you have `totes safe. Pointer`. That fixes the problem.

**Erik St. Martin:** Totally safe dot... \[laughter\]

**Francesc Cambó:** Totally safe dot pointer. Yeah, and it works.

**Carlisle Thompson:** That sounds like a website we should have.

**Brian Petersen:** I think we need to make a new top-level domain,.pointer.

**Francesc Cambó:**.totessafe.io, yeah... \[laughter\]

**Brian Petersen:** Actually, that would be a good vanity package for any Go package. You could use the vanity URL totes safe,.totes safe

**Erik St. Martin:** \[36:00\] With the tagline "You can trust us."

**Brian Petersen:** We promise.

**Erik St. Martin:** Yeah, there were so many good talks. So back to the Go Project room, I want to make sure we touch on that too, because I know it's definitely something Carlisle was interested in speaking with you while you were on the show... The Diversity of discussions. I wasn't in on that, how did that go?

**Francesc Cambó:** It went really well, it was full all the way. That was very interesting, seeing so many people interested in talking about Diversity, and not only people that are members of minorities represented at Gopher Con, black people and women, and LGBTQ etc., but there were also a lot of allies that were there to represent and basically to give support. That was very interesting.

We talked about many things. One of the things that I tried to propose, and I hope is going to happen - the same way there was this talk about mining the Go community, and that understands how Gophers do technical things, I was wondering if we could do something similar about who are those Gophers, where are they? Do they live somewhere in the States, in cities where they have meetups, or are they far apart? Do they have kids? Is it easy for them to attend conferences like Gopher Con, or do they prefer things like the remote meetups organized by Go Bridge? Is that useful for them? That was pretty interesting.

Then we moved into talking about how to make the Go community more approachable. There was a lot of discussion on basically improving the newcomers' documents that we have right now. I could say they're not bad, but we could definitely do much better. There were a lot of people talking about how to make those better, how to learn a little bit from the Ruby community. The Ruby community has a lot of funny examples; it is not only about technology, it is also about having fun while learning and things like that, and trying to apply that to the Go community. I think it's very interesting.

There was also - I don't want to say his name wrong, Johnny Tourniquet. He pointed out that it is good to have those materials, but once we have them we need to go out to other communities and teach. He was talking how he's going to schools that don't have any technological plan, they don't have a technical curriculum. And he goes there and volunteers to teach kids that otherwise cannot have access to programming classes, and he teaches that in Go. I think that is amazing, I'd like to see more of that.

I think that both things - having better materials for newcomers and then the Go community ourselves going out to reach into these communities that otherwise don't have access to it could make our community much better, much more diverse and also much larger and welcoming.

**Brian Petersen:** I think Erik and I had a conversation not too long ago, sometime in the last year, about how Go needed the Go equivalent of Ruby's Why The Lucky Stiff. Those absolutely crazy articles with cartoons that actually taught programming while you weren't busy thinking about it, because you were having so much fun learning.

**Francesc Cambó:** \[39:53\] Yeah. I don't know if you've seen this thing - I love it, and I'm going to try to copy it somehow. It is Swift Playgrounds.

**Brian Petersen:** Oh, the ones on iPad or iPhone?

**Francesc Cambó:** Yes. So basically you learn to program by calling functions, and there's these little... I'm not really sure how to describe, it's like the weirdest animal ever. It just goes around collecting gems and jumping into places, and all of those are functions that you call. But then on top of that you can write for loops and things like that. I think that something like that could be very useful for Go.

I've been working on something similar to that; I'm still in a very, very early stage, but that is one of the projects that basically came out from that discussion in the Go Project room.

**Brian Petersen:** Were there other discussions about specific projects or specific things that could be done to increase the diversity of the community in general?

**Francesc Cambó:** We discussed the impact of what Women Who Go has been doing and what Gorge has been doing, and I think that it is very powerful. All the impact that they've had so far is very positive, so that is something that we should keep on doing.

There is also another idea that I think came from Katrina. Katrina works at GitHub, and they sponsored this thing called First Robotics. We were wondering, could robotics be a good place for Go to be taught? So if we're able to make Robot work easily on the robots, then it could be a fun thing for kids to learn how to program those bots and go around just by writing Go.

**Carlisle Thompson:** Were you at the San Francisco meetup yesterday, Frances?

**Francesc Cambó:** Yes, I was there, but I had to leave, so I missed Burch's [Jana Burch Logan] [talk](https://youtu.be/xteEImopTic?t=2469). I know it was recorded, so I'm looking forward to watching it, too.

**Carlisle Thompson:** Yeah, that's exactly what I was going to mention. She is going to put out a proposal to have an abstraction of a lot of the interface that will be required for Go to work with the hardware, including robotics and Robots. Whenever that comes out, people should try to contribute. To make that happen, we will need to have a better interface.

**Erik St. Martin:** And Ron Evans from the Hybrid Group, who does our Robot room every year for Hack Day, he loves kids. I don't think there's anything he loves more than teaching kids about robotics and programming.

**Brian Petersen:** Yeah, we had a call with him a couple of months before Gopher Con, and it's probably important that everybody knows that he donates all of his time, and he gets sponsors for all of that equipment. He does this because he loves it. He told us in an off-hand sort of way that the whole programming thing is kind of a sideline that he does to fund playing with kids and robots. The guy really loves what he's doing, and we sure appreciate how much time he spends with us at the Gopher Con.

**Erik St. Martin:** Did you get to hack on any robots, anybody?

**Carlisle Thompson:** I actually had to leave early, which was a huge mistake. That was actually a totally different day, it was totally relaxed, everybody had done their talks, everybody had watched their talks, and I felt such a relaxed atmosphere. The next year I'm not going to make this mistake again, because I did the same mistake last year. So next year I'm going to stay for the whole day.

**Erik St. Martin:** \[43:48\] Yeah, so Hack Day was really like a happy accident. The first year we were talking about everybody was probably going to be flying home, flying for different states, different countries, so they would fly out at random parts of the day... Like, let's just reserve this space for longer - we get a better rate anyway - and then people can just kind of hang out and collaborate until they have to leave for their flight. Then it turned out half the people stayed; they wanted to stay, so we kind of turned it into this thing.

I think we had - Brian, Dave Cheney and I had a discussion about it, and I think the Hack Day thing is misleading. The name was kind of borrowed from elsewhere, and it doesn't have the same meaning for us, so I think next year we're going to name it Community Day, to focus more on what the day is about, just kind of hanging out with community members and having those discussions with the Go Team or collaborating with people on open source projects. And we'll probably do a better job at outlining all the things that will take place on the day, so it doesn't feel so much when you're booking your flight, like "Do I need to stay for this?"

**Brian Petersen:** It's hard, because we want it to be not organized, but you have to provide at least the shell of organization, so people have an idea of how they can use that time and why it would be worthwhile for them to do it. Then there's the concept of how do people find each other. We put out little tablets at the end of the tables and put numbers on all the tables, so people could meet each other at table 32 if they wanted to work on a particular project. That worked out really well, but that's really as deep as I want to go into organization on Hack Day. I want it to be a day when you can just hang out with your buddies and work on stuff.

I saw a lot of really remote teams that were doing team meetings, face-to-face meetings for the first time all year, in teams that had worked together. That was kind of fun, to see companies having face-to-face meetings at Gopher Con on Hack Day. That was cool.

**Erik St. Martin:** Frances, were you about to say something?

**Francesc Cambó:** Yeah, I was going to say, something that I really appreciated from the Robot Room was there were actually a bunch of people just playing around with drones, flying around. It looked really fun, and it made me think about, you know, there are conferences that I've been to, like Devon, that have these side conferences called Devon For Kids, where they have introductory courses for kids that want to learn to program, and I think that that could be an amazing thing to try. I know that you had this Family Track, which by the way, that was an amazing idea, and thank you for doing that... Having a little bit more of a technical side of the family track, where kids can just go and play with robots, that'd be pretty fun.

**Erik St. Martin:** Yeah, so that was actually something that we tried to do. I think we were too late in the planning of it, because it started to turn into... We were planning a second conference, and it was like "Now we have to market this, we have to find sponsors for this..." But I think it's something we definitely want to continue to pursue; we just gotta figure out how to slide that into the planning, and if anybody who's listening works for a company who wants to sponsor something like that, that takes a huge load off of us. That's something that we would ideally like to give to kids for free, and not charge for children to attend that.

**Francesc Cambó:** Yeah, that would be pretty amazing.

**Brian Petersen:** So now's a good time for us to talk about our other sponsor of the show, Equinox. Equinox does packaging and distribution and updating for Go applications. They have amazing command line tooling that allows you to package up your Go application and it cross-compiles it for all the different environments that Go supports, and then uploads it to Equinox's servers, and your customers or your end users can download Debian packages, RPMs, Microsoft Windows installers, Mac packages or use Homebrew to install your applications.

\[48:09\] So they've got hosted downloads and a download page, and it's kind of the neatest thing that I've used in terms of the distribution of an app. You can use their library, their Go package to create your command line tools to autoupdate it. You can make a flag, say "Update" and it will go off to the Equinox servers, download just the diff of the next binary and update your package. Or if your users like Homebrew or the Linux package managers, they can just run an update that way. So it's a great way to keep your applications up to date, and it significantly reduces the support burden that you have as an open source maintainer or even as a company that has applications that are distributed out across lots of desktops.

Equinox is free for community and personal projects, and they have very affordable plans for businesses. You should go to equinox.io/gotime to learn more about it. I strongly endorse it.

**Erik St. Martin:** And Alan Shrive, grok.

**Brian Petersen:** And everything Alan does, exactly. I use grok almost every day, and they don't even sponsor the show. \[laughter\] We love grok.

**Francesc Cambó:** Is Equinox also funded by Alan Shrive?

**Erik St. Martin:** Yes.

**Francesc Cambó:** I didn't know that. He's cool.

**Erik St. Martin:** Yeah, we all love Alan. He was walking around Gopher Con, too. It was awesome that we got to see him again.

**Brian Petersen:** Yes, he was one of our first speakers at Gopher Con 2014. Awesome stuff.

**Erik St. Martin:** I think Adam pointed out that he was featured in our recap video, which was awesome. Did you get to see the recap video that we played on day two?

**Francesc Cambó:** Yeah, I got to see it, that was really cool.

**Erik St. Martin:** The Changelog guys, they turned that thing around in a hotel room overnight.

**Brian Petersen:** Yeah, talk about some rapid production... It's funny, because I saw Peter Hell berg walking into the auditorium before the show, and I said "Hey Peter, you need to get your cell phone out and record the show when it starts." He's like, "Why?" I said, "Just trust me, Peter." \[laughter\] So he got to see himself on the big screen. That was cool.

**Erik St. Martin:** Yeah, I'm glad I wasn't in there.

**Brian Petersen:** Why is that, Erik? Let's talk about that.

**Erik St. Martin:** Let's not talk about that.

**Brian Petersen:** I have to get recorded and go on the big video thing, why is Erik St. Martin not on the big video thing?

**Erik St. Martin:** Because - and I almost refer to myself in the third person there... Because I don't know, I don't really like cameras. \[laughter\] I was going to say "Because Erik doesn't like cameras."

**Francesc Cambó:** You should try to get your brother on the video. Nobody will know.

**Erik St. Martin:** Yeah, he probably would have done it, too. He probably could have got up there and just spoke for me.

**Carlisle Thompson:** Yeah, we talked about that.

**Erik St. Martin:** My stand-in.

**Carlisle Thompson:** You're going to be at the Kubernetes conference, right Erik?

**Erik St. Martin:** I'm going to submit a proposal.

**Brian Petersen:** Excellent. Then you have to get on camera.

**Carlisle Thompson:** Yeah.

**Erik St. Martin:** Yeah, that's true.

**Carlisle Thompson:** Maybe he didn't know that, Brian.

**Erik St. Martin:** Right, now you're ruining it. You're supposed to tell me after I submit the proposal.

**Brian Petersen:** They told me that it was not going to be recorded or streamed, so you're fine, Erik. It will be okay.

**Erik St. Martin:** Then I end up in Frances's place, where it's like "Wait... What? They accepted it?" \[laughter\]

**Brian Petersen:** Now what?

**Francesc Cambó:** Yeah.

**Erik St. Martin:** So I think we're almost out of time. Do we want to move on to any projects that we found in the community or any other news? I know most of us have been hiding away at Gopher Con for the past week, so...

**Brian Petersen:** \[51:43\] I do have one good Gopher Con story that I have to share before we move on. Ivan Danilo from the Visualizing Concurrency talk - the day Gopher Con ended, we ended up in an elevator at the same time, and he came me kind of stern look, and he said, "We're going to have the next Gopher Con in Barcelona, correct?" \[laughter\]

**Francesc Cambó:** Oh, yes!

**Brian Petersen:** And I kind of didn't know what to say. I said, "You know, Barcelona would be a beautiful place to have a Gopher Con. I've never thought of having one there, but I've been to Barcelona and it's beautiful. That's a great idea." And he continues to stare and "Look, I think it's a great idea." It was very Russian-mafia looking, I felt a little threatened.

**Carlisle Thompson:** I'd be very glad to see that. Also, that reminds me, Gopher Con Brazil is happening. It's going to be on November 11 and 12, with possibly a workshop on the 13th, but we'll see about that one. The date is set, so start booking the tickets. The hotel is already settled as well. The website should be up maybe tonight.

**Brian Petersen:** Wow.

**Carlisle Thompson:** Yeah, it's happening.

**Erik St. Martin:** You move fast.

**Carlisle Thompson:** Uh-huh.

**Erik St. Martin:** Oh, and speaking of Renee, too... The logo that she turned around, that was awesome.

**Carlisle Thompson:** Yeah. To clarify, Renee did a sketch for our logo and it was so cute. It's a little gopher with a belly and sitting on the beach, drinking something.

**Francesc Cambó:** I really want to see that logo now.

**Carlisle Thompson:** I'll paste it on the channel for you right now.

**Brian Petersen:** You can't upload it on a podcast. \[laughter\]

**Carlisle Thompson:** But we have a Gophers channel. So the CFP - people are asking - is going to be up next week. The registration should be up tomorrow, the website should be up tomorrow, the CFP should be up next week, and we're also going to have the prospectus to send to potential sponsors next week as well. So talk to me... There are six organizers, I'm one of them. Talk to me if you're interested in sponsoring. I'm sorry, that's it. I'll stop now.

**Erik St. Martin:** No, it's a good thing. Back to hacking... Somebody totally registered github.com/totesafe.

**Brian Petersen:** No way.

**Carlisle Thompson:** That must have been Scott.

**Erik St. Martin:** I think it was Florin who did it.

**Brian Petersen:** \[laughs\] That is so wrong.

**Erik St. Martin:** I'm interested to see what shows up there. Is that like the staging area for the unsafe package?

**Brian Petersen:** \[laughs\] We need totesafe.io now.

**Francesc Cambó:** I think he got it, too.

**Erik St. Martin:** He registered that, too. \[laughter\]

**Francesc Cambó:** That is the problem when you give bad ideas in public - people will do them.

**Brian Petersen:** That's true.

**Erik St. Martin:** I don't know how much time we have to talk about community stuff, but one project I did see was Bundy. They took a lot of concepts from Bold, and added geospatial indexing to it, which I thought was really cool.

**Brian Petersen:** Yeah, I looked at Bundy this morning when you posted it into the show notes section, and it looks pretty interesting. The more interesting part for me was that they built it specifically to be a storage backend for Raft, so it meets the Raft storage interface or HashiCorp's Raft implementation. So you can use Bundy as a Raft store, which is kind of slick.

**Erik St. Martin:** I hadn't even caught that part of it.

**Brian Petersen:** Well, you have to read it, Erik. I've to open it up.

**Erik St. Martin:** I read the cool part, geospatial indexing.

**Brian Petersen:** Well, that wasn't the cool part for me. My cool part was the Raft part.

**Erik St. Martin:** Well, now Raft can store its stuff geospatially. \[laughter\]

**Brian Petersen:** That kind of makes sense, since Raft is so distributed.

**Erik St. Martin:** Something tells me that geospatial indexes aren't exposed to that interface.

**Brian Petersen:** Yeah, I'm guessing they're not. You're probably right there.

**Erik St. Martin:** I think we are we about out of time. Do we want to move into \#FreeSoftwareFriday?

**Brian Petersen:** Yes, let's.

**Carlisle Thompson:** Can I mention one quick thing?

**Erik St. Martin:** You sure can.

**Carlisle Thompson:** Because it's very much in the spirit of Operon. I want to mention that there is now a Clever Gopher channel on Gopher Slack for you to post and see pictures of our copies in clever places and poses.

**Erik St. Martin:** \[56:10\] There's been a lot of interesting photos that have come through there. And I also find it interesting that every episode there's a new channel that's announced, or discovered, or created on the show. \[laughter\] Every single episode.

**Brian Petersen:** It's true. I think the best one was Florin's picture of the gopher in the cockpit of an airplane. It looked like a 737 to me, I'm not sure. It might be an Airbus, but there's a gopher in the cockpit of an airplane.

**Carlisle Thompson:** I didn't think that was allowed, and I was thinking "How did he manage that? Did he arm-wrestle the pilots? Did he get arrested afterwards?"

**Erik St. Martin:** I'm hoping TSA wasn't involved. Although what was this swag... Was it year one that there was some piece of swag that was triggering something in TSA and everybody was getting their bags checked?

**Brian Petersen:** Oh, what was that?

**Erik St. Martin:** I can't remember what it was now, but there was some piece of swag that had some sort of powder or something on it, that was triggering...

**Brian Petersen:** ...a lot of trouble on the way home. I remember that now.

**Erik St. Martin:** Sorry...

**Brian Petersen:** Oops... No pocket knives, right? Oh, and Scott Mansfield said the same thing in the Slack - "No pocket knives as Gopher Con swag." Good call.

**Erik St. Martin:** Well, you could put it in your checked luggage.

**Brian Petersen:** You could.

**Erik St. Martin:** I also liked Dave Cheney's top tip: travelling with circuit boards and loose wires, they go in your checked baggage. A lot of us were travelling with hardware for Hack Day.

**Francesc Cambó:** Yeah, what could go wrong with that? \[laughter\]

**Erik St. Martin:** I was really worried none of it was gonna show up. Like, I'd get the bag and it'd be mostly empty. Because almost the entire bag that I had checked had tons of logic analyzers and bus pirates and raspberry pies and loose wires and sensors and stuff. I was like, "This is not going to end well."

**Brian Petersen:** Yeah, you got the big flag for extra screening.

**Erik St. Martin:** Yeah, that's why I put Brian's name on that luggage.

**Brian Petersen:** \[luggage\] Checked bag for Brian Petersen, right here. Alright, let's do \#FreeSoftwareFriday, we're running out of time.

**Erik St. Martin:** Cool. You want to go first, Brian?

**Brian Petersen:** You bet. So I'll briefly explain again, \#FreeSoftwareFriday is just our place to give a shout-out to open source projects and/or their maintainers for things that we use frequently and that we love. Today I'd like to give a shout-out to - this is kind of a cheat, but I used it a lot this week... So Docker is one of my favourite free software tools, and sure makes life easier sometimes. Thank you, Docker.

**Erik St. Martin:** How about you, Carlisle?

**Carlisle Thompson:** On the topic of Brazil, there's this open source project called Sure. It's a Platform as a Service, open source of course. It was put out by Globo.com. Globe is this huge media company in Brazil. It's a project that came out of Brazil, and most of the maintainers if not all are Brazilian developers. I'm not an infra person, I usually don't deal with infra, only the minimum, but it's been described to me as like an alternative to Heroku. It's a huge project, I was surprised when I saw it. It's been used by big companies, so check it out. Furthermore, it could be useful to you.

**Erik St. Martin:** And apparently all written in Go.

**Brian Petersen:** It is, yeah.

**Carlisle Thompson:** Yeah, of course.

**Brian Petersen:** It's been around for two years, too. It's been out for a long time. It's very stable now.

**Carlisle Thompson:** I actually met Andrews Medina and other developers at Gopher Con.

**Brian Petersen:** That's awesome.

**Erik St. Martin:** Frances, do you have a project that you want to give a shout-out to? Feel free to say no, we're blind siding you here.

**Francesc Cambó:** Does it need to be written in Go?

**Erik St. Martin:** It does not need to be written in Go.

**Francesc Cambó:** \[01:00:00.27\] Then I think I'm going to go with something that is actually for real, but we use regularly for the Google Cloud Platform Podcast, Audacity.

**Erik St. Martin:** Yeah, that is a good one.

**Brian Petersen:** Nice.

**Francesc Cambó:** Open source digital audio editor, and it is great. It works so well. It makes our podcast sound way better, without knowing really what we're doing.

**Brian Petersen:** Good call.

**Erik St. Martin:** I don't know whether Adam and the Changelog crew is still using that behind the scenes, but I know they used to use Audacity a lot, so we don't even have to give them a link to put on Twitter; I'm pretty sure he knows that one.

**Brian Petersen:** Do we have the best deal or what? We just get to talk and somebody else does all the post-production work, and the website... I love this plan.

**Erik St. Martin:** Right? So mine - actually, I recently started using it again, and I used to be a big proponent of it - is Direct, direnv.net. It's written in Go, and it's a cool little program you run in your shell so that basically when you CD into a directory it looks for a.entry file, and then you can basically load up environment variables or execute shell commands and all kinds of stuff. That's ridiculously nice for when you have to mangle your path or environment variables based on the project that you're working on. It's just seamless, you just kind of create that.entry file and done, you don't have to think about it again.

**Brian Petersen:** Yeah, Direct is especially nice if you want to have a custom Go path per project; you just drop that.entry file in there that changes your Go path. It's kind of custom-built for that, purpose-built. Very nice.

**Erik St. Martin:** And I think that is it. I want to thank everybody for coming on the show, I want to thank all the listeners who are listening live right now and hacking us from the Slack channel, everybody who will be listening... Definitely refer any Go programmers or people who are interested in the Go language to the podcast. Thanks everybody on the panel, especially thank you to Frances for coming on the show.

**Brian Petersen:** Thank you, Frances!

**Francesc Cambó:** Thank you for having me!

**Carlisle Thompson:** Thank you!

**Erik St. Martin:** If you're not subscribed, we are on iTunes and Play Store. You can subscribe at GoTime.fm. Big shout out to our sponsors for the show today, Linde and Equinox.io.

If you have something you would like to discuss or suggestions for guests to come on the show, github.com/GoTimFM/ping. I think that's it. It's a lot to cover, but I think I got it all.

**Brian Petersen:** You did well, Erik. Good job!

**Carlisle Thompson:** This was great, thanks! Bye!

**Brian Petersen:** Bye-bye. Thank you.

**Francesc Cambó:** Bye.

**Erik St. Martin:** Bye.
